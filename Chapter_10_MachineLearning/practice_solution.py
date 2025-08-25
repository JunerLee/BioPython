#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 10 练习题答案: 机器学习入门 - 模式识别的艺术

本文件包含第十章所有练习题的完整答案，
展示了机器学习在生物信息学中的实际应用。

答案包括：
1. 数据预处理和探索性分析
2. 监督学习 - 分类任务  
3. 无监督学习 - 聚类分析
4. 模型评估和优化
5. 综合实战项目

每个答案都包含详细的生物学解释和最佳实践。
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, make_blobs
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.model_selection import StratifiedKFold, validation_curve
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 分类算法
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

# 聚类算法
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# 评估指标
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, roc_auc_score, roc_curve, 
                           confusion_matrix, silhouette_score, 
                           adjusted_rand_score, classification_report)

# 特征选择
from sklearn.feature_selection import SelectKBest, f_classif, RFE

import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def solution_1_data_preprocessing():
    """
    答案1: 数据预处理和探索性分析
    
    这个练习展示了生物数据预处理的完整流程，
    包括缺失值处理、异常值检测和数据标准化。
    """
    print("=" * 60)
    print("🧬 答案1: 蛋白质数据预处理")
    print("=" * 60)
    
    # 创建模拟蛋白质数据
    np.random.seed(42)
    n_proteins = 100
    
    # 生成符合生物学特征的蛋白质数据
    protein_data = {
        # 分子量: 10-100 kDa，对数正态分布
        'molecular_weight': np.random.lognormal(np.log(30000), 0.5, n_proteins),
        
        # 等电点: 4-10，正态分布偏向酸性
        'isoelectric_point': np.random.normal(6.5, 1.5, n_proteins),
        
        # 氨基酸数量: 与分子量相关，平均分子量110 Da/氨基酸
        'amino_acid_count': None,  # 稍后计算
        
        # 疏水性指数: -2到2，正态分布
        'hydrophobicity': np.random.normal(0, 0.8, n_proteins),
        
        # 不稳定性指数: 0-100，指数分布
        'instability': np.random.exponential(25, n_proteins)
    }
    
    # 计算氨基酸数量（基于分子量，加入噪声）
    protein_data['amino_acid_count'] = (protein_data['molecular_weight'] / 110 + 
                                       np.random.normal(0, 20, n_proteins)).astype(int)
    
    # 确保数值在合理范围内
    protein_data['isoelectric_point'] = np.clip(protein_data['isoelectric_point'], 3, 12)
    protein_data['amino_acid_count'] = np.clip(protein_data['amino_acid_count'], 50, 2000)
    protein_data['instability'] = np.clip(protein_data['instability'], 0, 100)
    
    # 转换为DataFrame
    df = pd.DataFrame(protein_data)
    
    # 添加一些缺失值（模拟实际数据情况）
    missing_indices = np.random.choice(df.index, 8, replace=False)
    missing_columns = np.random.choice(df.columns, 8, replace=True)
    for idx, col in zip(missing_indices, missing_columns):
        df.loc[idx, col] = np.nan
    
    # 添加一些异常值（模拟数据质量问题）
    outlier_indices = np.random.choice(df.index, 3, replace=False)
    df.loc[outlier_indices[0], 'molecular_weight'] = 200000  # 异常大的蛋白质
    df.loc[outlier_indices[1], 'instability'] = 150  # 异常高的不稳定性
    df.loc[outlier_indices[2], 'hydrophobicity'] = 5  # 异常高的疏水性
    
    print("🔍 数据集基本信息:")
    print(f"数据形状: {df.shape}")
    print(f"前5行数据:")
    print(df.head().round(2))
    
    print(f"\n📊 描述性统计:")
    print(df.describe().round(2))
    
    print(f"\n⚠️ 缺失值检查:")
    missing_summary = df.isnull().sum()
    print(missing_summary[missing_summary > 0])
    print(f"总缺失值: {df.isnull().sum().sum()}")
    
    # 处理缺失值 - 用均值填充数值型特征
    print(f"\n🔧 处理缺失值...")
    df_clean = df.copy()
    for column in df_clean.columns:
        if df_clean[column].dtype in ['float64', 'int64']:
            mean_value = df_clean[column].mean()
            df_clean[column].fillna(mean_value, inplace=True)
            print(f"  {column}: 用均值 {mean_value:.2f} 填充")
    
    # 异常值检测 - 使用IQR方法
    print(f"\n🚨 异常值检测 (IQR方法):")
    outliers_info = {}
    
    for column in df_clean.select_dtypes(include=[np.number]).columns:
        Q1 = df_clean[column].quantile(0.25)
        Q3 = df_clean[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df_clean[(df_clean[column] < lower_bound) | 
                           (df_clean[column] > upper_bound)]
        
        if len(outliers) > 0:
            outliers_info[column] = len(outliers)
            print(f"  {column}: {len(outliers)} 个异常值")
    
    # 数据标准化
    print(f"\n⚖️ 数据标准化...")
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df_clean),
        columns=df_clean.columns,
        index=df_clean.index
    )
    
    print("标准化后的数据统计:")
    print(df_scaled.describe().round(3))
    
    # 绘制相关性热图
    print(f"\n📈 绘制特征相关性热图...")
    plt.figure(figsize=(10, 8))
    
    correlation_matrix = df_clean.corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    
    sns.heatmap(correlation_matrix, 
                mask=mask,
                annot=True, 
                cmap='coolwarm', 
                center=0,
                fmt='.2f',
                square=True)
    plt.title('蛋白质特征相关性热图')
    plt.tight_layout()
    plt.savefig('protein_correlation_heatmap.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 生物学解释
    print(f"\n🧬 生物学意义解释:")
    high_corr_pairs = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_val = correlation_matrix.iloc[i, j]
            if abs(corr_val) > 0.5:
                high_corr_pairs.append((
                    correlation_matrix.columns[i],
                    correlation_matrix.columns[j],
                    corr_val
                ))
    
    for feat1, feat2, corr in high_corr_pairs:
        print(f"  {feat1} 与 {feat2}: r={corr:.3f}")
        
        if 'molecular_weight' in [feat1, feat2] and 'amino_acid_count' in [feat1, feat2]:
            print("    → 生物学解释: 分子量与氨基酸数量正相关是合理的")
        elif 'instability' in [feat1, feat2]:
            print("    → 生物学解释: 不稳定性可能与蛋白质结构相关")
    
    print("✅ 练习1完成！数据预处理是机器学习成功的关键步骤。")
    return df_clean, df_scaled


def solution_2_gene_function_classifier():
    """
    答案2: 基因功能分类器
    
    这个练习展示了监督学习在基因功能预测中的应用，
    比较不同分类算法的性能。
    """
    print("\n" + "=" * 60)
    print("🧬 答案2: 基因功能分类器")
    print("=" * 60)
    
    # 创建基因分类数据
    np.random.seed(42)
    
    X, y = make_classification(
        n_samples=300, 
        n_features=8, 
        n_classes=3, 
        n_informative=6,
        n_redundant=2,
        n_clusters_per_class=1,
        flip_y=0.02,  # 2%的标签噪声
        random_state=42
    )
    
    # 添加特征名称（生物学相关）
    feature_names = [
        'gc_content',           # GC含量
        'gene_length',          # 基因长度
        'exon_count',           # 外显子数量
        'intron_length',        # 内含子长度
        'promoter_strength',    # 启动子强度
        'conservation_score',   # 保守性评分
        'expression_level',     # 表达水平
        'methylation_level'     # 甲基化水平
    ]
    
    # 创建DataFrame
    df = pd.DataFrame(X, columns=feature_names)
    df['function_class'] = y
    
    # 添加类别名称
    class_names = {0: '结构蛋白', 1: '酶', 2: '调节蛋白'}
    df['function_name'] = df['function_class'].map(class_names)
    
    print("📊 基因分类数据信息:")
    print(f"样本数量: {len(df)}")
    print(f"特征数量: {len(feature_names)}")
    print(f"类别分布:")
    for class_id, count in df['function_class'].value_counts().items():
        print(f"  {class_names[class_id]}: {count} ({count/len(df)*100:.1f}%)")
    
    # 可视化数据分布
    print(f"\n📊 数据可视化...")
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    # 子图1: 类别分布柱状图
    ax = axes[0]
    class_counts = df['function_class'].value_counts()
    bars = ax.bar([class_names[i] for i in class_counts.index], 
                  class_counts.values,
                  color=['skyblue', 'lightcoral', 'lightgreen'])
    ax.set_title('基因功能类别分布')
    ax.set_ylabel('样本数量')
    for bar, count in zip(bars, class_counts.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                str(count), ha='center', va='bottom')
    
    # 子图2-3: 特征分布箱线图
    for i, features_group in enumerate([feature_names[:4], feature_names[4:]]):
        ax = axes[i+1]
        df[features_group].boxplot(ax=ax)
        ax.set_title(f'特征分布组 {i+1}')
        ax.tick_params(axis='x', rotation=45)
    
    # 子图4: PCA可视化
    ax = axes[3]
    pca_vis = PCA(n_components=2)
    X_pca = pca_vis.fit_transform(X)
    
    for class_id in range(3):
        mask = y == class_id
        ax.scatter(X_pca[mask, 0], X_pca[mask, 1], 
                  label=class_names[class_id], alpha=0.6, s=30)
    
    ax.set_xlabel(f'PC1 ({pca_vis.explained_variance_ratio_[0]:.1%})')
    ax.set_ylabel(f'PC2 ({pca_vis.explained_variance_ratio_[1]:.1%})')
    ax.set_title('PCA可视化')
    ax.legend()
    
    # 子图5: 不同类别下GC含量的分布
    ax = axes[4]
    for class_id in range(3):
        data = df[df['function_class'] == class_id]['gc_content']
        ax.hist(data, alpha=0.5, label=class_names[class_id], bins=15)
    ax.set_xlabel('GC含量')
    ax.set_ylabel('频率')
    ax.set_title('GC含量在不同类别中的分布')
    ax.legend()
    
    # 子图6: 特征相关性热图
    ax = axes[5]
    corr_subset = df[feature_names[:5]].corr()
    im = ax.imshow(corr_subset, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xticklabels(corr_subset.columns, rotation=45, ha='right')
    ax.set_yticklabels(corr_subset.columns)
    ax.set_title('特征相关性')
    
    plt.tight_layout()
    plt.savefig('gene_classification_eda.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 数据分割和预处理
    print(f"\n🔧 数据预处理...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"训练集大小: {X_train.shape}")
    print(f"测试集大小: {X_test.shape}")
    
    # 数据标准化
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 训练多个分类模型
    print(f"\n🤖 训练分类模型...")
    
    models = {
        '逻辑回归': LogisticRegression(random_state=42, max_iter=1000),
        '决策树': DecisionTreeClassifier(random_state=42, max_depth=10),
        '随机森林': RandomForestClassifier(random_state=42, n_estimators=100),
        'SVM': SVC(random_state=42, probability=True),
        '朴素贝叶斯': GaussianNB()
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\n训练 {name}...")
        
        # 训练模型
        model.fit(X_train_scaled, y_train)
        
        # 预测
        y_pred = model.predict(X_test_scaled)
        y_proba = model.predict_proba(X_test_scaled) if hasattr(model, 'predict_proba') else None
        
        # 计算评估指标
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # 交叉验证
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='f1_weighted')
        
        results[name] = {
            'accuracy': accuracy,
            'precision': precision, 
            'recall': recall,
            'f1': f1,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'y_pred': y_pred,
            'y_proba': y_proba,
            'model': model
        }
        
        print(f"  准确率: {accuracy:.3f}")
        print(f"  精确率: {precision:.3f}")
        print(f"  召回率: {recall:.3f}")
        print(f"  F1分数: {f1:.3f}")
        print(f"  交叉验证F1: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
    
    # 可视化模型比较
    print(f"\n📊 模型性能比较...")
    plt.figure(figsize=(12, 6))
    
    model_names = list(results.keys())
    metrics = ['accuracy', 'precision', 'recall', 'f1']
    metric_labels = ['准确率', '精确率', '召回率', 'F1分数']
    
    x = np.arange(len(model_names))
    width = 0.2
    
    for i, (metric, label) in enumerate(zip(metrics, metric_labels)):
        values = [results[model][metric] for model in model_names]
        plt.bar(x + i*width, values, width, label=label, alpha=0.8)
    
    plt.xlabel('模型')
    plt.ylabel('分数')
    plt.title('模型性能比较')
    plt.xticks(x + width * 1.5, model_names, rotation=45)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('model_performance_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 选择最佳模型
    best_model_name = max(results.keys(), key=lambda k: results[k]['f1'])
    best_result = results[best_model_name]
    best_pred = best_result['y_pred']
    
    print(f"\n🏆 最佳模型: {best_model_name}")
    print(f"最佳F1分数: {best_result['f1']:.3f}")
    
    # 详细分类报告
    print(f"\n📋 详细分类报告:")
    print(classification_report(y_test, best_pred, 
                              target_names=['结构蛋白', '酶', '调节蛋白']))
    
    # 混淆矩阵
    print(f"\n📊 混淆矩阵...")
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_test, best_pred)
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['结构蛋白', '酶', '调节蛋白'],
                yticklabels=['结构蛋白', '酶', '调节蛋白'])
    plt.title(f'{best_model_name} - 混淆矩阵')
    plt.ylabel('真实标签')
    plt.xlabel('预测标签')
    
    # 在每个格子中添加百分比
    total = cm.sum()
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            percentage = cm[i, j] / total * 100
            plt.text(j+0.5, i+0.7, f'({percentage:.1f}%)', 
                    ha='center', va='center', fontsize=10, color='gray')
    
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 特征重要性分析
    if hasattr(best_result['model'], 'feature_importances_'):
        print(f"\n🔍 特征重要性分析...")
        importances = best_result['model'].feature_importances_
        
        # 创建特征重要性DataFrame
        feature_importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importances
        }).sort_values('importance', ascending=False)
        
        print("特征重要性排名:")
        for idx, row in feature_importance_df.iterrows():
            print(f"  {row['feature']}: {row['importance']:.3f}")
        
        # 可视化特征重要性
        plt.figure(figsize=(10, 6))
        plt.barh(range(len(feature_names)), importances[np.argsort(importances)])
        plt.yticks(range(len(feature_names)), 
                   [feature_names[i] for i in np.argsort(importances)])
        plt.xlabel('重要性分数')
        plt.title(f'{best_model_name} - 特征重要性')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('feature_importance.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    # 生物学意义解释
    print(f"\n🧬 生物学意义解释:")
    print(f"在基因功能分类任务中，{best_model_name}表现最佳:")
    print(f"• 结构蛋白基因通常具有相对稳定的表达模式")
    print(f"• 酶基因往往有特定的序列保守域")  
    print(f"• 调节蛋白基因表达受到严格的时空调控")
    print(f"• GC含量、基因长度等序列特征是重要的预测因子")
    
    print("✅ 练习2完成！监督学习可以有效预测基因功能。")
    return results, feature_names


def solution_3_cell_clustering():
    """
    答案3: 单细胞聚类分析
    
    这个练习展示了无监督学习在单细胞数据分析中的应用，
    帮助发现不同的细胞亚型。
    """
    print("\n" + "=" * 60)
    print("🧬 答案3: 单细胞聚类分析")
    print("=" * 60)
    
    # 生成模拟单细胞数据
    np.random.seed(42)
    
    # 创建三个细胞群，模拟不同的表达模式
    X, true_labels = make_blobs(
        n_samples=100, 
        n_features=50, 
        centers=3,
        cluster_std=1.5,
        random_state=42
    )
    
    # 模拟基因表达数据特点 - 转换为对数正态分布
    X = np.exp(X)  # 使数据呈对数正态分布
    X = np.maximum(X, 0.1)  # 确保所有值为正
    
    # 创建基因和细胞名称
    gene_names = [f'Gene_{i:02d}' for i in range(1, 51)]
    cell_names = [f'Cell_{i:03d}' for i in range(1, 101)]
    
    # 创建DataFrame
    df = pd.DataFrame(X, columns=gene_names, index=cell_names)
    
    # 为了更好地模拟单细胞数据，添加一些特殊表达模式
    # 让不同细胞群在特定基因上有差异表达
    cell_types = {0: 'Stem_cells', 1: 'Differentiated', 2: 'Mature_cells'}
    
    # 干细胞特异性基因（前10个基因）
    stem_mask = true_labels == 0
    df.loc[df.index[stem_mask], gene_names[:10]] *= 3
    
    # 分化细胞特异性基因（中间10个基因）
    diff_mask = true_labels == 1
    df.loc[df.index[diff_mask], gene_names[20:30]] *= 2.5
    
    # 成熟细胞特异性基因（后10个基因）
    mature_mask = true_labels == 2
    df.loc[df.index[mature_mask], gene_names[40:50]] *= 4
    
    print("🔬 单细胞数据信息:")
    print(f"细胞数量: {df.shape[0]}")
    print(f"基因数量: {df.shape[1]}")
    print(f"表达值范围: [{df.values.min():.2f}, {df.values.max():.2f}]")
    
    # 真实细胞类型分布
    true_distribution = pd.Series(true_labels).value_counts().sort_index()
    print(f"\n真实细胞类型分布:")
    for cell_id, count in true_distribution.items():
        print(f"  {cell_types[cell_id]}: {count} ({count/len(df)*100:.1f}%)")
    
    # 数据预处理
    print(f"\n🔧 数据预处理...")
    
    # 1. 对数转换（处理偏态分布）
    df_log = np.log1p(df)
    print(f"对数转换后范围: [{df_log.values.min():.2f}, {df_log.values.max():.2f}]")
    
    # 2. 标准化
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_log)
    print(f"标准化后均值: {df_scaled.mean():.3f}, 标准差: {df_scaled.std():.3f}")
    
    # PCA降维分析
    print(f"\n🔍 主成分分析...")
    pca = PCA(n_components=10)  # 先看前10个主成分
    df_pca_full = pca.fit_transform(df_scaled)
    
    # 选择前两个主成分用于可视化
    df_pca = df_pca_full[:, :2]
    
    explained_var_ratio = pca.explained_variance_ratio_
    print(f"前10个主成分解释方差比: {explained_var_ratio}")
    print(f"PC1解释方差: {explained_var_ratio[0]:.1%}")
    print(f"PC2解释方差: {explained_var_ratio[1]:.1%}")
    print(f"前两个主成分累计解释方差: {explained_var_ratio[:2].sum():.1%}")
    
    # 绘制方差解释比例
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.bar(range(1, 11), explained_var_ratio[:10])
    plt.xlabel('主成分')
    plt.ylabel('解释方差比例')
    plt.title('各主成分解释方差')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(range(1, 11), np.cumsum(explained_var_ratio[:10]), 'bo-')
    plt.xlabel('主成分数量')
    plt.ylabel('累计解释方差比例')
    plt.title('累计解释方差')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('pca_analysis.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 尝试不同的聚类算法
    print(f"\n🎯 聚类分析...")
    
    clustering_methods = {
        'K-Means': KMeans(n_clusters=3, random_state=42, n_init=10),
        'DBSCAN': DBSCAN(eps=1.0, min_samples=5),
        '层次聚类': AgglomerativeClustering(n_clusters=3),
        '高斯混合': GaussianMixture(n_components=3, random_state=42)
    }
    
    clustering_results = {}
    
    for name, clusterer in clustering_methods.items():
        print(f"\n执行 {name} 聚类...")
        
        # 聚类
        if name == '高斯混合':
            clusterer.fit(df_scaled)
            labels = clusterer.predict(df_scaled)
        else:
            labels = clusterer.fit_predict(df_scaled)
        
        # 评估指标
        unique_labels = set(labels)
        n_clusters = len(unique_labels) - (1 if -1 in labels else 0)
        
        if n_clusters > 1 and n_clusters < len(df):
            silhouette = silhouette_score(df_scaled, labels)
            ari = adjusted_rand_score(true_labels, labels)
        else:
            silhouette = -1
            ari = -1
        
        clustering_results[name] = {
            'labels': labels,
            'silhouette': silhouette,
            'ari': ari,
            'n_clusters': n_clusters
        }
        
        print(f"  发现聚类数: {n_clusters}")
        print(f"  轮廓系数: {silhouette:.3f}")
        print(f"  调整兰德指数: {ari:.3f}")
        
        if n_clusters > 0:
            cluster_sizes = np.bincount(labels[labels >= 0])
            print(f"  聚类大小: {cluster_sizes}")
    
    # 可视化聚类结果
    print(f"\n📊 可视化聚类结果...")
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for idx, (name, result) in enumerate(clustering_results.items()):
        ax = axes[idx]
        labels = result['labels']
        
        if result['n_clusters'] > 0:
            # 处理DBSCAN的噪声点
            unique_labels = set(labels)
            colors = plt.cm.viridis(np.linspace(0, 1, len(unique_labels)))
            
            for label_id, color in zip(unique_labels, colors):
                if label_id == -1:
                    # 噪声点用黑色表示
                    mask = labels == label_id
                    ax.scatter(df_pca[mask, 0], df_pca[mask, 1], 
                             c='black', marker='x', s=20, alpha=0.5, label='噪声')
                else:
                    mask = labels == label_id
                    ax.scatter(df_pca[mask, 0], df_pca[mask, 1], 
                             c=[color], alpha=0.6, s=30, label=f'群{label_id}')
        
        ax.set_title(f'{name}\n轮廓系数: {result["silhouette"]:.3f}')
        ax.set_xlabel(f'PC1 ({explained_var_ratio[0]:.1%})')
        ax.set_ylabel(f'PC2 ({explained_var_ratio[1]:.1%})')
        
        if idx < 4:  # 只在前4个子图添加图例
            ax.legend(fontsize=8, loc='best')
    
    # 真实标签
    ax = axes[4]
    for true_label in range(3):
        mask = true_labels == true_label
        ax.scatter(df_pca[mask, 0], df_pca[mask, 1], 
                  label=cell_types[true_label], alpha=0.6, s=30)
    ax.set_title('真实细胞类型')
    ax.set_xlabel(f'PC1 ({explained_var_ratio[0]:.1%})')
    ax.set_ylabel(f'PC2 ({explained_var_ratio[1]:.1%})')
    ax.legend(fontsize=8)
    
    # 空白
    axes[5].axis('off')
    
    plt.tight_layout()
    plt.savefig('clustering_results.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 选择最佳聚类方法
    valid_methods = {k: v for k, v in clustering_results.items() 
                    if v['silhouette'] > 0}
    
    if valid_methods:
        best_method = max(valid_methods.keys(), 
                         key=lambda k: valid_methods[k]['silhouette'])
        best_labels = clustering_results[best_method]['labels']
        
        print(f"\n🏆 最佳聚类方法: {best_method}")
        print(f"轮廓系数: {clustering_results[best_method]['silhouette']:.3f}")
        print(f"调整兰德指数: {clustering_results[best_method]['ari']:.3f}")
        
        # 创建聚类热图
        print(f"\n🎨 绘制聚类热图...")
        
        # 选择表达变异最大的20个基因
        gene_std = df.std(axis=0)
        top_genes = gene_std.nlargest(20).index
        
        # 按聚类标签排序细胞
        if best_labels is not None:
            # 处理噪声点（DBSCAN产生的-1标签）
            valid_cells = best_labels >= 0
            sorted_indices = []
            
            for cluster_id in sorted(set(best_labels[best_labels >= 0])):
                cluster_cells = np.where((best_labels == cluster_id) & valid_cells)[0]
                sorted_indices.extend(cluster_cells)
            
            # 添加噪声点到末尾
            if -1 in best_labels:
                noise_cells = np.where(best_labels == -1)[0]
                sorted_indices.extend(noise_cells)
            
            df_sorted = df.iloc[sorted_indices]
            labels_sorted = best_labels[sorted_indices]
            
            # 创建聚类热图
            plt.figure(figsize=(12, 8))
            
            # 创建行颜色（代表聚类）
            unique_clusters = sorted(set(labels_sorted[labels_sorted >= 0]))
            if -1 in labels_sorted:
                unique_clusters.append(-1)
            
            colors = plt.cm.Set1(np.linspace(0, 1, len(unique_clusters)))
            color_map = dict(zip(unique_clusters, colors))
            
            row_colors = [color_map[label] for label in labels_sorted]
            
            # 绘制热图
            g = sns.clustermap(
                df_sorted[top_genes], 
                row_colors=row_colors,
                cmap='RdBu_r',
                center=df_sorted[top_genes].median().median(),
                row_cluster=False,  # 不对行聚类，保持我们的排序
                col_cluster=True,   # 对列（基因）聚类
                figsize=(12, 8),
                cbar_kws={'label': '表达水平'},
                yticklabels=False  # 隐藏细胞名称
            )
            
            g.ax_heatmap.set_xlabel('基因')
            g.ax_heatmap.set_ylabel('细胞')
            plt.suptitle(f'{best_method} - 细胞聚类热图', y=1.02)
            
            plt.savefig('cell_clustering_heatmap.png', dpi=150, bbox_inches='tight')
            plt.show()
            
            # 分析每个聚类的特征基因
            print(f"\n🧬 聚类生物学特征分析:")
            
            for cluster_id in unique_clusters:
                if cluster_id >= 0:  # 跳过噪声点
                    cluster_cells = best_labels == cluster_id
                    cluster_size = sum(cluster_cells)
                    
                    # 计算该聚类的平均表达
                    cluster_mean = df.loc[df.index[cluster_cells]].mean()
                    
                    # 找出高表达基因（前5个）
                    top_expressed_genes = cluster_mean.nlargest(5)
                    
                    print(f"\n聚类 {cluster_id} ({cluster_size} 个细胞):")
                    print(f"  高表达基因:")
                    for gene, expr in top_expressed_genes.items():
                        print(f"    {gene}: {expr:.2f}")
                    
                    # 推测细胞类型
                    if gene in gene_names[:10]:  # 干细胞特异性基因
                        print(f"  可能的细胞类型: 干细胞")
                    elif gene in gene_names[20:30]:  # 分化细胞特异性基因
                        print(f"  可能的细胞类型: 分化中细胞")
                    elif gene in gene_names[40:50]:  # 成熟细胞特异性基因
                        print(f"  可能的细胞类型: 成熟细胞")
    
    # 生物学意义总结
    print(f"\n🧬 生物学意义总结:")
    print(f"单细胞聚类分析帮助我们:")
    print(f"• 识别不同的细胞亚型和状态")
    print(f"• 发现细胞分化轨迹和谱系关系")
    print(f"• 找到特异性表达的marker基因")
    print(f"• 理解细胞异质性的生物学基础")
    print(f"• 为进一步的功能实验提供候选目标")
    
    print("✅ 练习3完成！无监督学习是探索生物数据结构的强大工具。")
    return clustering_results, df, df_scaled


def solution_4_model_optimization():
    """
    答案4: 模型评估和优化
    
    这个练习展示了机器学习模型优化的完整流程，
    包括交叉验证、超参数调优和过拟合分析。
    """
    print("\n" + "=" * 60)
    print("🧬 答案4: 模型评估和优化")
    print("=" * 60)
    
    # 创建模拟的生物分类数据
    np.random.seed(42)
    
    X, y = make_classification(
        n_samples=500, 
        n_features=20, 
        n_informative=12, 
        n_redundant=4,
        n_classes=2, 
        flip_y=0.05,  # 5%标签噪声
        class_sep=0.8,  # 适中的类别分离度
        random_state=42
    )
    
    print("📊 数据信息:")
    print(f"样本数: {X.shape[0]}")
    print(f"特征数: {X.shape[1]}")
    print(f"正负样本比例: {np.bincount(y)} ({np.bincount(y)[1]/(np.bincount(y)[0]+np.bincount(y)[1])*100:.1f}% 阳性)")
    
    # 数据分割
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"\n分割后:")
    print(f"训练集: {X_train.shape[0]} 样本")
    print(f"测试集: {X_test.shape[0]} 样本")
    
    # 数据标准化
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"数据已标准化 (训练集均值: {X_train_scaled.mean():.3f}, 标准差: {X_train_scaled.std():.3f})")
    
    # 任务4.1: 交叉验证
    print("\n" + "-" * 40)
    print("任务4.1: 交叉验证评估")
    print("-" * 40)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # 使用分层k折交叉验证
    cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    # 多种评估指标的交叉验证
    scoring_metrics = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
    cv_results = {}
    
    for metric in scoring_metrics:
        scores = cross_val_score(rf, X_train_scaled, y_train, 
                                cv=cv_strategy, scoring=metric)
        cv_results[metric] = scores
        print(f"{metric:>10}: {scores.mean():.3f} ± {scores.std():.3f} {scores}")
    
    # 可视化交叉验证结果
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    metric_names = list(cv_results.keys())
    means = [cv_results[m].mean() for m in metric_names]
    stds = [cv_results[m].std() for m in metric_names]
    
    plt.bar(metric_names, means, yerr=stds, capsize=5, alpha=0.7)
    plt.title('5折交叉验证结果')
    plt.ylabel('分数')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.boxplot([cv_results[m] for m in metric_names], labels=metric_names)
    plt.title('交叉验证分数分布')
    plt.ylabel('分数')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cross_validation_results.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 任务4.2: 超参数调优
    print("\n" + "-" * 40)
    print("任务4.2: 超参数调优")
    print("-" * 40)
    
    # 定义参数网格
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2', None]
    }
    
    total_combinations = np.prod([len(v) for v in param_grid.values()])
    print(f"参数组合总数: {total_combinations}")
    print(f"使用3折交叉验证进行网格搜索...")
    
    # 网格搜索
    grid_search = GridSearchCV(
        RandomForestClassifier(random_state=42), 
        param_grid, 
        cv=3,  # 使用3折以节省时间 
        scoring='f1', 
        n_jobs=-1,
        verbose=0
    )
    
    grid_search.fit(X_train_scaled, y_train)
    
    print(f"\n最佳参数: {grid_search.best_params_}")
    print(f"最佳CV分数: {grid_search.best_score_:.3f}")
    
    # 在测试集上评估最佳模型
    best_model = grid_search.best_estimator_
    y_pred_best = best_model.predict(X_test_scaled)
    test_f1 = f1_score(y_test, y_pred_best)
    test_accuracy = accuracy_score(y_test, y_pred_best)
    
    print(f"测试集性能:")
    print(f"  F1分数: {test_f1:.3f}")
    print(f"  准确率: {test_accuracy:.3f}")
    
    # 分析参数影响
    print(f"\n参数影响分析...")
    results_df = pd.DataFrame(grid_search.cv_results_)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 分析n_estimators的影响
    ax = axes[0]
    n_est_values = param_grid['n_estimators']
    n_est_scores = []
    
    for n_est in n_est_values:
        mask = results_df['param_n_estimators'] == n_est
        mean_score = results_df[mask]['mean_test_score'].mean()
        n_est_scores.append(mean_score)
    
    ax.plot(n_est_values, n_est_scores, 'o-')
    ax.set_xlabel('n_estimators')
    ax.set_ylabel('平均F1分数')
    ax.set_title('树的数量对性能的影响')
    ax.grid(True, alpha=0.3)
    
    # 分析max_depth的影响
    ax = axes[1]
    depth_values = [d for d in param_grid['max_depth'] if d is not None]
    depth_scores = []
    
    for depth in depth_values:
        mask = results_df['param_max_depth'] == depth
        mean_score = results_df[mask]['mean_test_score'].mean()
        depth_scores.append(mean_score)
    
    ax.plot(depth_values, depth_scores, 'o-')
    ax.set_xlabel('max_depth')
    ax.set_ylabel('平均F1分数')
    ax.set_title('树的深度对性能的影响')
    ax.grid(True, alpha=0.3)
    
    # 分析min_samples_split的影响
    ax = axes[2]
    split_values = param_grid['min_samples_split']
    split_scores = []
    
    for split in split_values:
        mask = results_df['param_min_samples_split'] == split
        mean_score = results_df[mask]['mean_test_score'].mean()
        split_scores.append(mean_score)
    
    ax.plot(split_values, split_scores, 'o-')
    ax.set_xlabel('min_samples_split')
    ax.set_ylabel('平均F1分数')
    ax.set_title('最小分割样本数对性能的影响')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('hyperparameter_analysis.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 任务4.3: 过拟合分析
    print("\n" + "-" * 40)
    print("任务4.3: 过拟合分析")
    print("-" * 40)
    
    # 使用验证曲线分析过拟合
    depths = [1, 3, 5, 10, 15, 20, 30, None]
    
    print("计算验证曲线...")
    train_scores, val_scores = validation_curve(
        DecisionTreeClassifier(random_state=42), 
        X_train_scaled, y_train,
        param_name='max_depth', 
        param_range=[d for d in depths if d is not None] + [100],  # None用100代替
        cv=5, 
        scoring='accuracy',
        n_jobs=-1
    )
    
    # 计算均值和标准差
    train_mean = train_scores.mean(axis=1)
    train_std = train_scores.std(axis=1)
    val_mean = val_scores.mean(axis=1)
    val_std = val_scores.std(axis=1)
    
    # 绘制验证曲线
    plt.figure(figsize=(10, 6))
    
    x_values = [d if d is not None else 100 for d in depths[:-1]] + [100]
    
    plt.plot(x_values, train_mean, 'o-', label='训练分数', color='blue', alpha=0.8)
    plt.fill_between(x_values, train_mean-train_std, train_mean+train_std, 
                     alpha=0.2, color='blue')
    
    plt.plot(x_values, val_mean, 'o-', label='验证分数', color='red', alpha=0.8)
    plt.fill_between(x_values, val_mean-val_std, val_mean+val_std, 
                     alpha=0.2, color='red')
    
    plt.xlabel('最大树深度')
    plt.ylabel('准确率')
    plt.title('验证曲线 - 过拟合分析')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 标注过拟合区域
    overfit_threshold = 0.05
    for i, (train_acc, val_acc) in enumerate(zip(train_mean, val_mean)):
        gap = train_acc - val_acc
        if gap > overfit_threshold:
            plt.axvline(x_values[i], color='orange', alpha=0.5, linestyle='--')
            plt.text(x_values[i], val_acc-0.02, f'过拟合\n差距:{gap:.3f}', 
                    ha='center', fontsize=8, color='orange')
    
    plt.tight_layout()
    plt.savefig('overfitting_analysis.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 分析结果
    print(f"\n过拟合分析结果:")
    for i, depth in enumerate(x_values):
        gap = train_mean[i] - val_mean[i]
        if gap > overfit_threshold:
            print(f"深度 {depth}: 训练分数={train_mean[i]:.3f}, 验证分数={val_mean[i]:.3f}, 差距={gap:.3f} (过拟合)")
        else:
            print(f"深度 {depth}: 训练分数={train_mean[i]:.3f}, 验证分数={val_mean[i]:.3f}, 差距={gap:.3f}")
    
    optimal_depth_idx = np.argmax(val_mean)
    optimal_depth = x_values[optimal_depth_idx]
    print(f"\n推荐的最优深度: {optimal_depth} (验证分数最高: {val_mean[optimal_depth_idx]:.3f})")
    
    # 任务4.4: 特征选择
    print("\n" + "-" * 40)
    print("任务4.4: 特征选择")
    print("-" * 40)
    
    print("原始特征数:", X_train_scaled.shape[1])
    
    # 方法1: 基于统计的特征选择
    print("\n方法1: 基于F统计量的特征选择")
    selector_stats = SelectKBest(score_func=f_classif, k=10)
    X_train_stats = selector_stats.fit_transform(X_train_scaled, y_train)
    X_test_stats = selector_stats.transform(X_test_scaled)
    
    # 获取选择的特征
    selected_features_stats = selector_stats.get_support()
    feature_scores = selector_stats.scores_
    
    print(f"选中的特征索引: {np.where(selected_features_stats)[0]}")
    print(f"特征分数前5名:")
    top_features = np.argsort(feature_scores)[::-1][:5]
    for i, feat_idx in enumerate(top_features):
        print(f"  特征{feat_idx}: F分数={feature_scores[feat_idx]:.2f}")
    
    # 方法2: 递归特征消除
    print("\n方法2: 递归特征消除(RFE)")
    rfe = RFE(LogisticRegression(random_state=42, max_iter=1000), n_features_to_select=10)
    X_train_rfe = rfe.fit_transform(X_train_scaled, y_train)
    X_test_rfe = rfe.transform(X_test_scaled)
    
    selected_features_rfe = rfe.support_
    feature_ranking = rfe.ranking_
    
    print(f"RFE选中的特征索引: {np.where(selected_features_rfe)[0]}")
    print(f"特征重要性排名:")
    for i in range(len(feature_ranking)):
        if feature_ranking[i] == 1:  # 选中的特征排名为1
            print(f"  特征{i}: 排名{feature_ranking[i]} (选中)")
    
    # 方法3: 基于模型的特征选择
    print("\n方法3: 基于随机森林的特征重要性")
    rf_selector = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_selector.fit(X_train_scaled, y_train)
    
    feature_importances = rf_selector.feature_importances_
    important_features = np.argsort(feature_importances)[::-1][:10]
    
    print(f"重要性最高的10个特征:")
    for i, feat_idx in enumerate(important_features):
        print(f"  特征{feat_idx}: 重要性={feature_importances[feat_idx]:.3f}")
    
    # 比较特征选择前后的性能
    print("\n特征选择效果比较:")
    
    models_to_test = {
        '原始特征': (X_train_scaled, X_test_scaled),
        'F统计量选择': (X_train_stats, X_test_stats),
        'RFE选择': (X_train_rfe, X_test_rfe)
    }
    
    feature_selection_results = {}
    
    for method_name, (X_tr, X_te) in models_to_test.items():
        # 使用逻辑回归测试
        lr = LogisticRegression(random_state=42, max_iter=1000)
        lr.fit(X_tr, y_train)
        y_pred = lr.predict(X_te)
        
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        feature_selection_results[method_name] = {
            'accuracy': accuracy,
            'f1': f1,
            'n_features': X_tr.shape[1]
        }
        
        print(f"{method_name:>15}: 准确率={accuracy:.3f}, F1={f1:.3f}, 特征数={X_tr.shape[1]}")
    
    # 可视化特征选择效果
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    methods = list(feature_selection_results.keys())
    accuracies = [feature_selection_results[m]['accuracy'] for m in methods]
    f1s = [feature_selection_results[m]['f1'] for m in methods]
    
    x = np.arange(len(methods))
    width = 0.35
    
    plt.bar(x - width/2, accuracies, width, label='准确率', alpha=0.8)
    plt.bar(x + width/2, f1s, width, label='F1分数', alpha=0.8)
    
    plt.xlabel('特征选择方法')
    plt.ylabel('性能分数')
    plt.title('特征选择效果比较')
    plt.xticks(x, methods, rotation=45)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    n_features = [feature_selection_results[m]['n_features'] for m in methods]
    colors = ['blue', 'orange', 'green']
    
    plt.bar(methods, n_features, color=colors, alpha=0.7)
    plt.xlabel('特征选择方法')
    plt.ylabel('特征数量')
    plt.title('选择的特征数量')
    plt.xticks(rotation=45)
    
    for i, (method, n_feat) in enumerate(zip(methods, n_features)):
        plt.text(i, n_feat + 0.5, str(n_feat), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('feature_selection_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 生物学解释
    print(f"\n🧬 模型优化的生物学意义:")
    print(f"• 交叉验证确保模型在不同数据子集上的稳定性")
    print(f"• 超参数调优帮助找到最适合生物数据特征的模型配置")
    print(f"• 过拟合检测防止模型过度记忆训练数据的噪声")
    print(f"• 特征选择识别真正有预测价值的生物标记物")
    print(f"• 这些技术确保模型的泛化能力和临床应用价值")
    
    print("✅ 练习4完成！模型优化是构建可靠AI系统的关键。")
    return grid_search, feature_selection_results


def solution_5_cancer_subtype_project():
    """
    答案5: 综合项目 - 癌症亚型分类
    
    这是一个完整的机器学习项目，整合了前面学到的所有技术，
    模拟真实的癌症亚型分类任务。
    """
    print("\n" + "=" * 60)
    print("🧬 综合项目: 癌症亚型分类")
    print("=" * 60)
    
    print("""
🔬 项目背景:
基于基因表达数据的乳腺癌分子亚型分类是精准医疗的重要应用。
不同亚型有不同的治疗策略和预后：

• Luminal A: 激素受体阳性，预后最好，内分泌治疗敏感
• Luminal B: 激素受体阳性，Ki-67高，可能需要化疗
• HER2+: HER2扩增，靶向治疗(如曲妥珠单抗)有效
• Basal-like: 三阴性，预后最差，主要依靠化疗

我们的任务是构建一个自动分类器来辅助临床诊断。
    """)
    
    # 步骤1: 数据生成和探索
    print("\n" + "-" * 50)
    print("步骤1: 数据生成和探索")
    print("-" * 50)
    
    np.random.seed(42)
    
    # 模拟4种亚型的基因表达模式
    n_samples_per_class = [120, 100, 80, 100]  # 不平衡数据，模拟真实情况
    n_genes = 100
    subtype_names = ['Luminal A', 'Luminal B', 'HER2+', 'Basal-like']
    
    all_data = []
    all_labels = []
    
    print("生成各亚型的基因表达数据...")
    
    for subtype_id, (n_samples, subtype_name) in enumerate(zip(n_samples_per_class, subtype_names)):
        print(f"  生成 {subtype_name}: {n_samples} 个样本")
        
        # 基础表达水平 (对数正态分布)
        base_expression = np.random.lognormal(2, 0.8, (n_samples, n_genes))
        
        # 添加亚型特异性表达模式
        if subtype_id == 0:  # Luminal A
            # ESR1, PGR相关基因高表达 (前25个基因)
            base_expression[:, :25] *= np.random.uniform(2, 3, (n_samples, 25))
            # 增殖相关基因低表达
            base_expression[:, 75:] *= np.random.uniform(0.3, 0.7, (n_samples, 25))
            
        elif subtype_id == 1:  # Luminal B  
            # ESR1, PGR相关基因中等表达
            base_expression[:, :25] *= np.random.uniform(1.5, 2.5, (n_samples, 25))
            # 增殖相关基因高表达 (25-50个基因)
            base_expression[:, 25:50] *= np.random.uniform(2.5, 4, (n_samples, 25))
            
        elif subtype_id == 2:  # HER2+
            # HER2及相关基因极高表达 (50-75个基因)
            base_expression[:, 50:75] *= np.random.uniform(3, 5, (n_samples, 25))
            # 增殖基因高表达
            base_expression[:, 25:50] *= np.random.uniform(2, 3, (n_samples, 25))
            
        elif subtype_id == 3:  # Basal-like
            # 基底样特异基因高表达 (75-100个基因)
            base_expression[:, 75:] *= np.random.uniform(2.5, 4, (n_samples, 25))
            # 激素受体基因低表达
            base_expression[:, :25] *= np.random.uniform(0.2, 0.5, (n_samples, 25))
        
        # 添加噪声
        noise = np.random.normal(0, base_expression * 0.1)  # 相对噪声
        base_expression += noise
        base_expression = np.maximum(base_expression, 0.1)  # 确保表达值为正
        
        all_data.append(base_expression)
        all_labels.extend([subtype_id] * n_samples)
    
    X = np.vstack(all_data)
    y = np.array(all_labels)
    
    # 创建特征名称（模拟真实基因名）
    gene_categories = {
        'ESR_related': list(range(0, 25)),
        'Proliferation': list(range(25, 50)), 
        'HER2_pathway': list(range(50, 75)),
        'Basal_markers': list(range(75, 100))
    }
    
    gene_names = []
    for category, indices in gene_categories.items():
        for i, idx in enumerate(indices):
            gene_names.append(f'{category}_{i+1:02d}')
    
    print(f"\n数据集概况:")
    print(f"总样本数: {X.shape[0]}")
    print(f"基因数量: {X.shape[1]}")
    print(f"类别分布:")
    for i, (name, count) in enumerate(zip(subtype_names, n_samples_per_class)):
        print(f"  {name}: {count} ({count/sum(n_samples_per_class)*100:.1f}%)")
    
    # 步骤2: 数据预处理
    print("\n" + "-" * 50)
    print("步骤2: 数据预处理")
    print("-" * 50)
    
    # 创建DataFrame方便处理
    df = pd.DataFrame(X, columns=gene_names)
    df['subtype'] = [subtype_names[i] for i in y]
    df['subtype_id'] = y
    
    # 2.1 处理缺失值(模拟一些缺失)
    print("模拟并处理缺失值...")
    missing_indices = np.random.choice(len(df), 20, replace=False)
    missing_genes = np.random.choice(gene_names, 20, replace=True)
    
    for idx, gene in zip(missing_indices, missing_genes):
        df.loc[idx, gene] = np.nan
    
    print(f"  添加了 {df.isnull().sum().sum()} 个缺失值")
    
    # 用中位数填充缺失值（比均值更稳健）
    for gene in gene_names:
        if df[gene].isnull().any():
            median_value = df[gene].median()
            df[gene].fillna(median_value, inplace=True)
    
    print(f"  用中位数填充后，缺失值: {df[gene_names].isnull().sum().sum()}")
    
    # 2.2 对数转换处理偏态分布
    print("对数转换...")
    df_log = df.copy()
    df_log[gene_names] = np.log1p(df[gene_names])  # log(1+x)
    
    # 2.3 标准化
    print("标准化...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_log[gene_names])
    
    # 2.4 处理类别不平衡
    print(f"类别不平衡比例: {dict(zip(*np.unique(y, return_counts=True)))}")
    print("将在模型训练时使用class_weight='balanced'来处理不平衡")
    
    # 步骤3: 探索性数据分析
    print("\n" + "-" * 50)
    print("步骤3: 探索性数据分析") 
    print("-" * 50)
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    # 3.1 类别分布
    ax = axes[0]
    subtype_counts = df['subtype'].value_counts()
    bars = ax.bar(subtype_counts.index, subtype_counts.values, 
                  color=['lightblue', 'lightcoral', 'lightgreen', 'gold'])
    ax.set_title('癌症亚型分布', fontsize=14)
    ax.set_ylabel('样本数量')
    plt.setp(ax.get_xticklabels(), rotation=45)
    
    for bar, count in zip(bars, subtype_counts.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
                str(count), ha='center', va='bottom')
    
    # 3.2 主成分分析可视化
    ax = axes[1]
    pca_vis = PCA(n_components=2)
    X_pca = pca_vis.fit_transform(X_scaled)
    
    colors = ['blue', 'red', 'green', 'orange']
    for i, subtype in enumerate(subtype_names):
        mask = df['subtype'] == subtype
        ax.scatter(X_pca[mask, 0], X_pca[mask, 1], 
                  c=colors[i], label=subtype, alpha=0.6, s=30)
    
    ax.set_xlabel(f'PC1 ({pca_vis.explained_variance_ratio_[0]:.1%})')
    ax.set_ylabel(f'PC2 ({pca_vis.explained_variance_ratio_[1]:.1%})')
    ax.set_title('PCA可视化')
    ax.legend(fontsize=8)
    
    # 3.3 差异表达基因热图
    ax = axes[2]
    # 计算每个亚型的平均表达
    subtype_means = df_log.groupby('subtype')[gene_names].mean()
    
    # 选择差异最大的20个基因
    gene_vars = df_log[gene_names].var()
    top_var_genes = gene_vars.nlargest(20).index
    
    im = ax.imshow(subtype_means[top_var_genes].T, aspect='auto', cmap='RdBu_r')
    ax.set_xticks(range(len(subtype_names)))
    ax.set_xticklabels(subtype_names, rotation=45)
    ax.set_ylabel('基因')
    ax.set_title('差异表达热图(Top 20)')
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    
    # 3.4 基因表达分布
    ax = axes[3]
    sample_genes = ['ESR_related_01', 'Proliferation_01', 'HER2_pathway_01', 'Basal_markers_01']
    for gene in sample_genes:
        if gene in df_log.columns:
            ax.hist(df_log[gene], alpha=0.5, bins=30, label=gene.replace('_', ' '))
    ax.set_xlabel('log(表达水平)')
    ax.set_ylabel('频率')
    ax.set_title('关键基因表达分布')
    ax.legend(fontsize=8)
    
    # 3.5 t-SNE可视化
    ax = axes[4]
    print("计算t-SNE...")
    tsne = TSNE(n_components=2, random_state=42, perplexity=30)
    X_tsne = tsne.fit_transform(X_scaled[:300])  # 使用部分数据加速
    
    for i, subtype in enumerate(subtype_names):
        mask = df['subtype'].iloc[:300] == subtype
        ax.scatter(X_tsne[mask, 0], X_tsne[mask, 1], 
                  c=colors[i], label=subtype, alpha=0.6, s=30)
    
    ax.set_xlabel('t-SNE 1')
    ax.set_ylabel('t-SNE 2') 
    ax.set_title('t-SNE可视化')
    ax.legend(fontsize=8)
    
    # 3.6 方差分析
    ax = axes[5]
    pca_full = PCA()
    pca_full.fit(X_scaled)
    explained_var = pca_full.explained_variance_ratio_[:20]
    
    ax.bar(range(1, 21), explained_var)
    ax.set_xlabel('主成分')
    ax.set_ylabel('解释方差比例')
    ax.set_title('主成分解释方差')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cancer_eda_comprehensive.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 步骤4: 特征工程和选择
    print("\n" + "-" * 50)
    print("步骤4: 特征工程和选择")
    print("-" * 50)
    
    X_processed = X_scaled.copy()
    
    # 4.1 单变量特征选择
    print("单变量特征选择...")
    selector_univariate = SelectKBest(score_func=f_classif, k=50)
    X_univariate = selector_univariate.fit_transform(X_processed, y)
    selected_genes_univariate = np.array(gene_names)[selector_univariate.get_support()]
    
    print(f"  选择了 {len(selected_genes_univariate)} 个基因")
    print(f"  前5个最重要的基因:")
    scores = selector_univariate.scores_
    top_indices = np.argsort(scores)[::-1][:5]
    for i, idx in enumerate(top_indices):
        print(f"    {gene_names[idx]}: F分数 {scores[idx]:.2f}")
    
    # 4.2 递归特征消除
    print("\n递归特征消除...")
    rf_for_rfe = RandomForestClassifier(n_estimators=50, random_state=42)
    rfe = RFE(rf_for_rfe, n_features_to_select=40)
    X_rfe = rfe.fit_transform(X_processed, y)
    selected_genes_rfe = np.array(gene_names)[rfe.support_]
    
    print(f"  RFE选择了 {len(selected_genes_rfe)} 个基因")
    
    # 4.3 基于模型的特征重要性
    print("\n基于随机森林的特征重要性...")
    rf_importance = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_importance.fit(X_processed, y)
    
    importances = rf_importance.feature_importances_
    important_indices = np.argsort(importances)[::-1][:30]
    selected_genes_importance = [gene_names[i] for i in important_indices]
    
    print(f"  选择重要性最高的 {len(selected_genes_importance)} 个基因")
    print(f"  前5个最重要的基因:")
    for i, idx in enumerate(important_indices[:5]):
        print(f"    {gene_names[idx]}: 重要性 {importances[idx]:.3f}")
    
    # 4.4 创建组合特征（基因比值）
    print("\n创建组合特征...")
    # ESR相关基因与HER2通路基因的比值
    esr_genes = [g for g in gene_names if g.startswith('ESR')]
    her2_genes = [g for g in gene_names if g.startswith('HER2')]
    
    if esr_genes and her2_genes:
        esr_mean = df_log[esr_genes].mean(axis=1)
        her2_mean = df_log[her2_genes].mean(axis=1)
        esr_her2_ratio = esr_mean / (her2_mean + 1e-6)  # 避免除零
        
        print(f"  创建ESR/HER2比值特征")
        print(f"  不同亚型的ESR/HER2比值:")
        for subtype in subtype_names:
            mask = df['subtype'] == subtype
            ratio_mean = esr_her2_ratio[mask].mean()
            print(f"    {subtype}: {ratio_mean:.2f}")
    
    # 使用最佳特征选择结果
    X_selected = X_univariate  # 使用单变量选择的结果
    
    # 步骤5: 模型训练和优化
    print("\n" + "-" * 50)
    print("步骤5: 模型训练和优化")
    print("-" * 50)
    
    # 数据分割
    X_train, X_test, y_train, y_test = train_test_split(
        X_selected, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"训练集: {X_train.shape[0]} 样本")
    print(f"测试集: {X_test.shape[0]} 样本")
    
    # 5.1 训练多个基础模型
    models_to_try = {
        'LogisticRegression': LogisticRegression(
            random_state=42, max_iter=1000, class_weight='balanced'
        ),
        'RandomForest': RandomForestClassifier(
            n_estimators=100, random_state=42, class_weight='balanced'
        ),
        'SVM': SVC(
            random_state=42, probability=True, class_weight='balanced'
        ),
        'XGBoost': RandomForestClassifier(  # 用随机森林代替XGBoost
            n_estimators=200, max_depth=6, random_state=42, class_weight='balanced'
        ),
        'NeuralNetwork': MLPClassifier(
            hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42
        )
    }
    
    model_results = {}
    
    print("训练基础模型...")
    for model_name, model in models_to_try.items():
        print(f"\n训练 {model_name}...")
        
        # 训练模型
        model.fit(X_train, y_train)
        
        # 预测和评估
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test) if hasattr(model, 'predict_proba') else None
        
        # 计算指标
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # 交叉验证
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1_weighted')
        
        model_results[model_name] = {
            'model': model,
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'y_pred': y_pred,
            'y_proba': y_proba
        }
        
        print(f"  准确率: {accuracy:.3f}")
        print(f"  F1分数: {f1:.3f}")
        print(f"  交叉验证F1: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
    
    # 5.2 超参数调优（针对最佳模型）
    best_basic_model = max(model_results.keys(), key=lambda k: model_results[k]['f1'])
    print(f"\n最佳基础模型: {best_basic_model}")
    
    if best_basic_model == 'RandomForest':
        print("对随机森林进行超参数调优...")
        param_grid_rf = {
            'n_estimators': [100, 200],
            'max_depth': [10, 20, None],
            'min_samples_split': [5, 10],
            'min_samples_leaf': [2, 4]
        }
        
        grid_search = GridSearchCV(
            RandomForestClassifier(random_state=42, class_weight='balanced'),
            param_grid_rf, cv=3, scoring='f1_weighted', n_jobs=-1
        )
        
        grid_search.fit(X_train, y_train)
        
        print(f"最佳参数: {grid_search.best_params_}")
        print(f"最佳CV分数: {grid_search.best_score_:.3f}")
        
        # 更新最佳模型
        best_model = grid_search.best_estimator_
        y_pred_final = best_model.predict(X_test)
        y_proba_final = best_model.predict_proba(X_test)
        
        final_accuracy = accuracy_score(y_test, y_pred_final)
        final_f1 = f1_score(y_test, y_pred_final, average='weighted')
        
        print(f"优化后测试集性能:")
        print(f"  准确率: {final_accuracy:.3f}")
        print(f"  F1分数: {final_f1:.3f}")
    else:
        best_model = model_results[best_basic_model]['model']
        y_pred_final = model_results[best_basic_model]['y_pred']
        y_proba_final = model_results[best_basic_model]['y_proba']
        final_accuracy = model_results[best_basic_model]['accuracy']
        final_f1 = model_results[best_basic_model]['f1']
    
    # 步骤6: 模型评估
    print("\n" + "-" * 50)
    print("步骤6: 模型评估")
    print("-" * 50)
    
    # 6.1 详细分类报告
    print("详细分类报告:")
    print(classification_report(y_test, y_pred_final, target_names=subtype_names))
    
    # 6.2 混淆矩阵
    print("\n混淆矩阵分析:")
    cm = confusion_matrix(y_test, y_pred_final)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=subtype_names, yticklabels=subtype_names)
    plt.title('癌症亚型分类混淆矩阵')
    plt.ylabel('真实亚型')
    plt.xlabel('预测亚型')
    
    # 添加准确率信息
    for i in range(len(subtype_names)):
        for j in range(len(subtype_names)):
            if i == j:  # 对角线元素
                accuracy_per_class = cm[i, j] / cm[i, :].sum()
                plt.text(j+0.5, i+0.7, f'({accuracy_per_class:.1%})', 
                        ha='center', va='center', color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('cancer_confusion_matrix.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 分析每个类别的性能
    for i, subtype in enumerate(subtype_names):
        class_mask = y_test == i
        class_predictions = y_pred_final[class_mask]
        class_accuracy = accuracy_score([i] * sum(class_mask), class_predictions)
        print(f"{subtype}: 准确率 {class_accuracy:.1%}, 样本数 {sum(class_mask)}")
    
    # 6.3 ROC曲线 (多分类)
    if y_proba_final is not None:
        print("\n绘制ROC曲线...")
        plt.figure(figsize=(10, 8))
        
        # 为每个类别绘制ROC曲线
        for i, subtype in enumerate(subtype_names):
            # 将多分类问题转换为二分类 (one-vs-rest)
            y_binary = (y_test == i).astype(int)
            y_score = y_proba_final[:, i]
            
            fpr, tpr, _ = roc_curve(y_binary, y_score)
            auc_score = roc_auc_score(y_binary, y_score)
            
            plt.plot(fpr, tpr, label=f'{subtype} (AUC = {auc_score:.3f})', 
                    linewidth=2)
        
        plt.plot([0, 1], [0, 1], 'k--', alpha=0.6)
        plt.xlabel('假阳性率 (1 - 特异度)')
        plt.ylabel('真阳性率 (敏感度)')
        plt.title('多分类ROC曲线 (One-vs-Rest)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('cancer_roc_curves.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    # 步骤7: 模型解释
    print("\n" + "-" * 50)
    print("步骤7: 模型解释")
    print("-" * 50)
    
    # 7.1 特征重要性分析
    if hasattr(best_model, 'feature_importances_'):
        print("特征重要性分析:")
        feature_importance = best_model.feature_importances_
        important_features = np.argsort(feature_importance)[::-1]
        
        print("最重要的10个基因:")
        for i, feat_idx in enumerate(important_features[:10]):
            gene_name = selected_genes_univariate[feat_idx]
            importance = feature_importance[feat_idx]
            print(f"  {i+1:2d}. {gene_name}: {importance:.3f}")
        
        # 可视化特征重要性
        plt.figure(figsize=(12, 6))
        top_features = important_features[:15]
        top_importance = feature_importance[top_features]
        top_names = [selected_genes_univariate[i] for i in top_features]
        
        plt.barh(range(len(top_names)), top_importance)
        plt.yticks(range(len(top_names)), top_names)
        plt.xlabel('特征重要性')
        plt.title('Top 15 特征重要性')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig('cancer_feature_importance.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    # 7.2 错误案例分析
    print("\n错误案例分析:")
    misclassified = y_test != y_pred_final
    if sum(misclassified) > 0:
        print(f"总共 {sum(misclassified)} 个误分类案例:")
        
        error_analysis = {}
        for true_class, pred_class in zip(y_test[misclassified], y_pred_final[misclassified]):
            key = f"{subtype_names[true_class]} → {subtype_names[pred_class]}"
            error_analysis[key] = error_analysis.get(key, 0) + 1
        
        for error_type, count in error_analysis.items():
            print(f"  {error_type}: {count} 例")
    
    # 7.3 生物学意义解释
    print(f"\n🧬 生物学意义解释:")
    print(f"基于基因表达的癌症亚型分类具有重要临床意义:")
    print(f"")
    print(f"分类性能:")
    print(f"• 总体准确率: {final_accuracy:.1%}")
    print(f"• 加权F1分数: {final_f1:.3f}")
    print(f"")
    print(f"临床应用价值:")
    print(f"• Luminal A亚型预测准确，可指导内分泌治疗")
    print(f"• HER2+亚型识别关键，决定靶向治疗方案")
    print(f"• Basal-like亚型预后最差，需积极化疗")
    print(f"• 可作为病理诊断的重要补充工具")
    print(f"")
    print(f"关键预测基因:")
    if hasattr(best_model, 'feature_importances_'):
        top_3_genes = [selected_genes_univariate[i] for i in important_features[:3]]
        for gene in top_3_genes:
            if gene.startswith('ESR'):
                print(f"• {gene}: 激素受体通路，区分Luminal亚型")
            elif gene.startswith('HER2'):
                print(f"• {gene}: HER2通路，识别HER2+亚型")
            elif gene.startswith('Basal'):
                print(f"• {gene}: 基底样标记，识别三阴性乳腺癌")
            elif gene.startswith('Proliferation'):
                print(f"• {gene}: 增殖相关，区分Luminal A/B")
    
    # 步骤8: 结果总结和报告
    print("\n" + "-" * 50)
    print("步骤8: 项目总结报告")
    print("-" * 50)
    
    # 计算一些额外的统计信息
    total_samples = len(y)
    n_features_original = len(gene_names)
    n_features_selected = X_selected.shape[1]
    
    # 计算每类的AUC
    class_aucs = []
    if y_proba_final is not None:
        for i in range(len(subtype_names)):
            y_binary = (y_test == i).astype(int)
            y_score = y_proba_final[:, i]
            auc = roc_auc_score(y_binary, y_score)
            class_aucs.append(auc)
    
    mean_auc = np.mean(class_aucs) if class_aucs else 0
    
    # 找出最难区分的亚型组合
    most_confused = ""
    max_confusion = 0
    for i in range(len(subtype_names)):
        for j in range(len(subtype_names)):
            if i != j and cm[i, j] > max_confusion:
                max_confusion = cm[i, j]
                most_confused = f"{subtype_names[i]} 与 {subtype_names[j]}"
    
    report = f"""
    
🏥 癌症亚型分类项目总结报告
=====================================

📊 数据概况:
   • 总样本数: {total_samples}
   • 基因数量: {n_features_original} → {n_features_selected} (特征选择后)  
   • 癌症亚型: {len(subtype_names)} 类
   • 类别分布: 不平衡 (最多{max(n_samples_per_class)}, 最少{min(n_samples_per_class)})

🤖 最佳模型:
   • 算法: {best_basic_model}
   • 总体准确率: {final_accuracy:.1%}
   • 加权F1分数: {final_f1:.3f}
   • 平均AUC: {mean_auc:.3f}

🔍 关键发现:
   • 最重要的预测基因: {', '.join([selected_genes_univariate[i] for i in important_features[:3]]) if hasattr(best_model, 'feature_importances_') else 'N/A'}
   • 最难区分的亚型: {most_confused} ({max_confusion}例误分类)
   • 模型优势: 特征选择有效，处理不平衡数据

⚕️ 临床意义:
   • 该模型可辅助乳腺癌分子亚型诊断
   • 结合常规病理检查提高诊断准确性
   • 为个性化治疗方案提供分子依据
   • 特别适用于疑难病例的辅助诊断

📋 技术细节:
   • 特征选择: 单变量F统计量选择 (前50个基因)
   • 数据预处理: 对数转换 + 标准化
   • 类别不平衡: 使用class_weight='balanced'
   • 模型验证: 5折分层交叉验证

⚠️ 局限性:
   • 样本量相对较小，需更大规模验证
   • 模拟数据可能与真实数据存在差异
   • 缺乏外部验证集评估泛化能力
   • 未考虑批次效应和技术变异

🚀 下一步工作:
   • 收集更大规模的真实临床数据
   • 引入深度学习方法 (如CNN、Transformer)
   • 整合多组学数据 (基因组、蛋白组、代谢组)
   • 开发用户友好的临床决策支持系统
   • 进行前瞻性临床试验验证

📈 性能基准:
   • Luminal A: {(cm[0,0]/cm[0,:].sum() if len(cm) > 0 else 0):.1%} 准确率
   • Luminal B: {(cm[1,1]/cm[1,:].sum() if len(cm) > 1 else 0):.1%} 准确率  
   • HER2+: {(cm[2,2]/cm[2,:].sum() if len(cm) > 2 else 0):.1%} 准确率
   • Basal-like: {(cm[3,3]/cm[3,:].sum() if len(cm) > 3 else 0):.1%} 准确率

💡 创新点:
   • 整合多种特征选择方法
   • 考虑类别不平衡问题
   • 提供详细的生物学解释
   • 完整的机器学习项目流程

=====================================
项目完成时间: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
建议引用: "基于机器学习的乳腺癌分子亚型分类研究"
    """
    
    print(report)
    
    print("\n" + "="*60)
    print("🎉 综合项目完成！")
    print("="*60)
    print("""
🏆 恭喜你完成了完整的机器学习项目！

你已经掌握了：
✅ 端到端的机器学习项目流程
✅ 生物医学数据的特殊处理方法
✅ 多分类问题的建模和评估
✅ 不平衡数据的处理策略
✅ 特征工程和模型优化技术
✅ 结果解释和临床意义分析

这个项目展示了机器学习在精准医疗中的巨大潜力。
你现在具备了在生物信息学领域应用AI技术的能力！

下一步建议：
🚀 尝试真实的癌症数据集 (TCGA, GEO)
🚀 学习深度学习框架 (PyTorch, TensorFlow)
🚀 探索单细胞分析工具 (Scanpy, Seurat)
🚀 参与生物信息学开源项目

记住：机器学习是工具，生物学洞察是灵魂！
    """)
    
    return {
        'best_model': best_model,
        'results': model_results,
        'final_accuracy': final_accuracy,
        'final_f1': final_f1,
        'selected_genes': selected_genes_univariate,
        'report': report
    }


def main():
    """运行所有练习的答案"""
    print("🧬 Chapter 10: 机器学习入门练习 - 完整答案")
    print("这些答案展示了机器学习在生物信息学中的实际应用")
    print("="*80)
    
    try:
        print("开始运行所有练习答案...")
        
        # 答案1: 数据预处理
        print("\n🔬 运行答案1: 数据预处理...")
        df_clean, df_scaled = solution_1_data_preprocessing()
        
        # 答案2: 基因功能分类
        print("\n🔬 运行答案2: 基因功能分类...")
        classification_results, feature_names = solution_2_gene_function_classifier()
        
        # 答案3: 单细胞聚类
        print("\n🔬 运行答案3: 单细胞聚类...")
        clustering_results, cell_df, cell_scaled = solution_3_cell_clustering()
        
        # 答案4: 模型优化
        print("\n🔬 运行答案4: 模型优化...")
        grid_search, feature_selection_results = solution_4_model_optimization()
        
        # 答案5: 综合项目
        print("\n🔬 运行答案5: 综合项目...")
        project_results = solution_5_cancer_subtype_project()
        
        print("\n" + "="*80)
        print("🎯 所有练习答案运行完成！")
        print("="*80)
        
        print("""
📚 学习成果总结:

通过这5个练习，你已经完整掌握了：

1️⃣ 数据预处理 (答案1):
   • 缺失值和异常值处理
   • 数据标准化和转换
   • 相关性分析和可视化

2️⃣ 监督学习 (答案2): 
   • 多分类问题建模
   • 模型比较和选择
   • 特征重要性分析

3️⃣ 无监督学习 (答案3):
   • 聚类算法比较
   • 降维和可视化
   • 生物学意义解释

4️⃣ 模型优化 (答案4):
   • 交叉验证评估
   • 超参数调优
   • 过拟合检测和特征选择

5️⃣ 综合应用 (答案5):
   • 完整项目流程
   • 多组学数据整合
   • 临床应用价值评估

🎉 你现在已经具备了在生物信息学领域
   应用机器学习技术的完整技能！

继续保持学习的热情，在实践中不断提升！ 🧬💻🚀
        """)
        
    except Exception as e:
        print(f"❌ 运行过程中遇到错误: {e}")
        print("请检查环境依赖和数据生成过程")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()