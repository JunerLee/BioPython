#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 10: 机器学习入门 - 模式识别的艺术

本章演示完整的机器学习工作流程：
Part 1: 监督学习 - 基因功能分类
Part 2: 无监督学习 - 细胞亚型发现
Part 3: 模型评估与优化
Part 4: 深度学习初探

生物学类比：
机器学习就像训练一个病理学家
- 监督学习：用已知诊断的病例教会识别疾病
- 无监督学习：发现未知的疾病亚型
- 深度学习：像人脑一样多层次理解复杂模式
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 分类算法
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# 聚类算法
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# 评估指标
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, roc_auc_score, roc_curve, 
                           confusion_matrix, silhouette_score, 
                           adjusted_rand_score, classification_report)

import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def print_section(title):
    """打印章节标题"""
    print("\n" + "="*60)
    print(f"🧬 {title}")
    print("="*60)


# ====================
# Part 1: 监督学习 - 基因功能分类
# ====================

def create_gene_classification_data():
    """
    创建基因功能分类的示例数据
    
    生物学背景：
    根据基因的序列特征预测其功能类别
    - 类别0：管家基因（housekeeping）
    - 类别1：转录因子（transcription factor）
    - 类别2：激酶（kinase）
    """
    print_section("Part 1: 监督学习 - 基因功能分类")
    
    np.random.seed(42)
    n_samples = 300
    
    # 创建特征（基因序列特征）
    # 特征1：GC含量
    # 特征2：长度
    # 特征3：保守性评分
    # 特征4：表达水平
    # 特征5：进化速率
    
    features = []
    labels = []
    
    # 管家基因特征
    for i in range(100):
        gc_content = np.random.normal(0.45, 0.05)  # 中等GC含量
        length = np.random.normal(1500, 300)        # 中等长度
        conservation = np.random.normal(0.8, 0.1)   # 高保守性
        expression = np.random.normal(0.7, 0.1)     # 高表达
        evolution_rate = np.random.normal(0.2, 0.05) # 低进化速率
        
        features.append([gc_content, length, conservation, expression, evolution_rate])
        labels.append(0)
    
    # 转录因子特征
    for i in range(100):
        gc_content = np.random.normal(0.55, 0.05)   # 较高GC含量
        length = np.random.normal(2000, 400)        # 较长
        conservation = np.random.normal(0.6, 0.15)  # 中等保守性
        expression = np.random.normal(0.3, 0.1)     # 低表达
        evolution_rate = np.random.normal(0.4, 0.1) # 中等进化速率
        
        features.append([gc_content, length, conservation, expression, evolution_rate])
        labels.append(1)
    
    # 激酶特征
    for i in range(100):
        gc_content = np.random.normal(0.50, 0.05)   # 中等GC含量
        length = np.random.normal(2500, 500)        # 长
        conservation = np.random.normal(0.7, 0.1)   # 较高保守性
        expression = np.random.normal(0.5, 0.15)    # 中等表达
        evolution_rate = np.random.normal(0.3, 0.08) # 较低进化速率
        
        features.append([gc_content, length, conservation, expression, evolution_rate])
        labels.append(2)
    
    # 创建DataFrame
    feature_names = ['GC_content', 'length', 'conservation', 'expression', 'evolution_rate']
    df = pd.DataFrame(features, columns=feature_names)
    df['function'] = labels
    
    print("📊 数据集信息：")
    print(f"  样本数量: {len(df)}")
    print(f"  特征数量: {len(feature_names)}")
    print(f"  类别分布: {df['function'].value_counts().to_dict()}")
    print("\n📊 特征统计：")
    print(df[feature_names].describe().round(3))
    
    return df, feature_names


def visualize_feature_distributions(df, feature_names):
    """可视化特征分布"""
    print("\n📊 可视化特征分布")
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    function_names = {0: 'Housekeeping', 1: 'TF', 2: 'Kinase'}
    colors = ['blue', 'orange', 'green']
    
    for idx, feature in enumerate(feature_names):
        ax = axes[idx]
        for func_id in [0, 1, 2]:
            data = df[df['function'] == func_id][feature]
            ax.hist(data, alpha=0.5, label=function_names[func_id], 
                   color=colors[func_id], bins=20)
        ax.set_xlabel(feature)
        ax.set_ylabel('Frequency')
        ax.set_title(f'Distribution of {feature}')
        ax.legend()
    
    # 空白子图
    axes[-1].axis('off')
    
    plt.tight_layout()
    plt.savefig('feature_distributions.png', dpi=150, bbox_inches='tight')
    plt.show()


def train_classification_models(df, feature_names):
    """
    训练多种分类模型并比较性能
    
    生物学类比：
    就像用不同的方法诊断疾病
    - 逻辑回归：根据症状的线性组合判断
    - 决策树：像医生的诊断流程图
    - 随机森林：多个医生投票决定
    - SVM：找到最佳的诊断边界
    """
    print_section("训练分类模型")
    
    # 准备数据
    X = df[feature_names].values
    y = df['function'].values
    
    # 划分训练集和测试集（70%训练，30%测试）
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # 数据标准化（重要！）
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"训练集大小: {X_train.shape}")
    print(f"测试集大小: {X_test.shape}")
    
    # 定义模型
    models = {
        '逻辑回归': LogisticRegression(random_state=42, max_iter=1000),
        '决策树': DecisionTreeClassifier(random_state=42, max_depth=5),
        '随机森林': RandomForestClassifier(random_state=42, n_estimators=100),
        'SVM': SVC(random_state=42, probability=True),
        '朴素贝叶斯': GaussianNB()
    }
    
    # 训练和评估每个模型
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
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
        
        results[name] = {
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
        print(f"  精确率: {precision:.3f}")
        print(f"  召回率: {recall:.3f}")
        print(f"  F1分数: {f1:.3f}")
        print(f"  交叉验证: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
    
    return results, X_test_scaled, y_test, scaler


def visualize_model_comparison(results):
    """可视化模型性能比较"""
    print("\n📊 模型性能比较")
    
    # 提取指标
    models = list(results.keys())
    metrics = ['accuracy', 'precision', 'recall', 'f1']
    
    # 创建比较图
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(models))
    width = 0.2
    
    for i, metric in enumerate(metrics):
        values = [results[model][metric] for model in models]
        ax.bar(x + i*width, values, width, label=metric.capitalize())
    
    ax.set_xlabel('Model')
    ax.set_ylabel('Score')
    ax.set_title('Model Performance Comparison')
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(models, rotation=45)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('model_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()


def demonstrate_overfitting():
    """
    演示过拟合现象
    
    生物学类比：
    过拟合就像记住了所有训练病人的名字和症状，
    但遇到新病人就不会诊断了
    """
    print_section("过拟合与欠拟合")
    
    print("""
🔍 什么是过拟合？
过拟合就像一个医学生死记硬背了所有病例，
但不理解疾病的本质规律，遇到新病例就束手无策。

🔍 如何避免过拟合？
1. 增加训练数据（看更多病例）
2. 简化模型（抓住主要症状）
3. 正则化（防止过度依赖某个特征）
4. 交叉验证（在不同医院验证）
5. 早停（适可而止）
    """)
    
    # 创建示例数据
    np.random.seed(42)
    X = np.sort(np.random.rand(100, 1) * 10, axis=0)
    y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
    
    # 训练不同复杂度的模型
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    from sklearn.pipeline import Pipeline
    
    degrees = [1, 4, 15]
    titles = ['Underfitting', 'Good Fit', 'Overfitting']
    
    for ax, degree, title in zip(axes, degrees, titles):
        # 创建多项式回归
        polynomial_features = PolynomialFeatures(degree=degree)
        linear_regression = LinearRegression()
        pipeline = Pipeline([
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression)
        ])
        
        pipeline.fit(X, y)
        
        # 预测
        X_plot = np.linspace(0, 10, 300)[:, np.newaxis]
        y_plot = pipeline.predict(X_plot)
        
        # 绘图
        ax.scatter(X, y, alpha=0.5, label='Data')
        ax.plot(X_plot, y_plot, color='red', label=f'Degree {degree}')
        ax.set_xlabel('X')
        ax.set_ylabel('y')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('overfitting_demo.png', dpi=150, bbox_inches='tight')
    plt.show()


# ====================
# Part 2: 无监督学习 - 细胞亚型发现
# ====================

def create_cell_expression_data():
    """
    创建单细胞基因表达数据
    
    生物学背景：
    模拟不同细胞类型的基因表达谱
    - 干细胞
    - 分化中的细胞
    - 成熟细胞
    """
    print_section("Part 2: 无监督学习 - 细胞亚型发现")
    
    np.random.seed(42)
    
    # 创建三种细胞类型的表达数据
    n_genes = 50
    gene_names = [f"Gene_{i:03d}" for i in range(1, n_genes+1)]
    
    # 干细胞（高表达多能性基因）
    stem_cells = np.random.lognormal(2, 0.5, (30, n_genes))
    stem_cells[:, :10] *= 2  # 前10个基因高表达（干性标记）
    
    # 分化中的细胞（中间状态）
    diff_cells = np.random.lognormal(2, 0.6, (40, n_genes))
    diff_cells[:, 10:25] *= 1.8  # 中间基因高表达（分化标记）
    
    # 成熟细胞（特定基因高表达）
    mature_cells = np.random.lognormal(2, 0.4, (30, n_genes))
    mature_cells[:, 30:45] *= 2.5  # 后面基因高表达（成熟标记）
    
    # 合并数据
    all_cells = np.vstack([stem_cells, diff_cells, mature_cells])
    
    # 创建真实标签（用于验证，但不用于训练）
    true_labels = np.array([0]*30 + [1]*40 + [2]*30)
    
    # 创建DataFrame
    cell_names = [f"Cell_{i:03d}" for i in range(1, 101)]
    df = pd.DataFrame(all_cells, columns=gene_names, index=cell_names)
    
    print(f"📊 数据集信息：")
    print(f"  细胞数量: {df.shape[0]}")
    print(f"  基因数量: {df.shape[1]}")
    print(f"  表达值范围: [{df.values.min():.2f}, {df.values.max():.2f}]")
    
    return df, true_labels


def perform_clustering_analysis(df, true_labels):
    """
    执行多种聚类分析
    
    生物学类比：
    就像在显微镜下观察细胞，根据形态将相似的归为一组
    """
    print_section("聚类分析")
    
    # 数据预处理
    # 1. 对数转换（处理偏态分布）
    df_log = np.log1p(df)
    
    # 2. 标准化
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_log)
    
    # 3. PCA降维（可视化用）
    pca = PCA(n_components=2, random_state=42)
    df_pca = pca.fit_transform(df_scaled)
    
    print(f"PCA解释方差比: {pca.explained_variance_ratio_}")
    print(f"累计解释方差: {pca.explained_variance_ratio_.sum():.1%}")
    
    # 尝试不同的聚类算法
    clustering_methods = {
        'K-Means': KMeans(n_clusters=3, random_state=42),
        'DBSCAN': DBSCAN(eps=3, min_samples=5),
        'Hierarchical': AgglomerativeClustering(n_clusters=3),
        'GMM': GaussianMixture(n_components=3, random_state=42)
    }
    
    results = {}
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for idx, (name, clusterer) in enumerate(clustering_methods.items()):
        print(f"\n执行 {name} 聚类...")
        
        # 聚类
        if name == 'GMM':
            labels = clusterer.fit_predict(df_scaled)
        else:
            labels = clusterer.fit_predict(df_scaled)
        
        # 评估
        if len(np.unique(labels)) > 1:
            silhouette = silhouette_score(df_scaled, labels)
            ari = adjusted_rand_score(true_labels, labels)
        else:
            silhouette = -1
            ari = -1
        
        results[name] = {
            'labels': labels,
            'silhouette': silhouette,
            'ari': ari,
            'n_clusters': len(np.unique(labels[labels >= 0]))
        }
        
        print(f"  聚类数: {results[name]['n_clusters']}")
        print(f"  轮廓系数: {silhouette:.3f}")
        print(f"  调整兰德指数: {ari:.3f}")
        
        # 可视化
        ax = axes[idx]
        scatter = ax.scatter(df_pca[:, 0], df_pca[:, 1], 
                           c=labels, cmap='viridis', 
                           alpha=0.6, s=30)
        ax.set_title(f'{name}\nSilhouette: {silhouette:.3f}')
        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
        plt.colorbar(scatter, ax=ax)
    
    # 真实标签
    ax = axes[4]
    scatter = ax.scatter(df_pca[:, 0], df_pca[:, 1], 
                       c=true_labels, cmap='Set1', 
                       alpha=0.6, s=30)
    ax.set_title('True Labels')
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
    plt.colorbar(scatter, ax=ax)
    
    # 空白
    axes[5].axis('off')
    
    plt.tight_layout()
    plt.savefig('clustering_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    return results, df_scaled, pca


def determine_optimal_clusters(df_scaled):
    """
    确定最优聚类数
    
    生物学类比：
    就像确定组织中有几种不同的细胞类型
    """
    print_section("确定最优聚类数")
    
    k_range = range(2, 11)
    inertias = []
    silhouettes = []
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(df_scaled)
        
        inertias.append(kmeans.inertia_)
        silhouettes.append(silhouette_score(df_scaled, labels))
    
    # 可视化
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 肘部法则
    axes[0].plot(k_range, inertias, 'bo-')
    axes[0].set_xlabel('Number of Clusters (k)')
    axes[0].set_ylabel('Inertia')
    axes[0].set_title('Elbow Method')
    axes[0].grid(True, alpha=0.3)
    
    # 轮廓系数
    axes[1].plot(k_range, silhouettes, 'ro-')
    axes[1].set_xlabel('Number of Clusters (k)')
    axes[1].set_ylabel('Silhouette Score')
    axes[1].set_title('Silhouette Analysis')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('optimal_k.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    optimal_k = k_range[np.argmax(silhouettes)]
    print(f"🎯 基于轮廓系数，最优聚类数为: {optimal_k}")
    
    return optimal_k


def create_cluster_heatmap(df, labels):
    """创建聚类热图"""
    print("\n📊 创建聚类热图")
    
    # 按聚类标签排序
    sorted_idx = np.argsort(labels)
    df_sorted = df.iloc[sorted_idx]
    labels_sorted = labels[sorted_idx]
    
    # 选择差异最大的基因
    gene_std = df.std(axis=0)
    top_genes = gene_std.nlargest(20).index
    
    # 创建热图
    plt.figure(figsize=(12, 8))
    
    # 创建聚类颜色条
    cluster_colors = ['red', 'blue', 'green', 'orange', 'purple']
    row_colors = [cluster_colors[label] if label >= 0 else 'gray' 
                  for label in labels_sorted]
    
    # 绘制热图
    g = sns.clustermap(df_sorted[top_genes], 
                       row_colors=row_colors,
                       cmap='RdBu_r',
                       center=0,
                       row_cluster=False,
                       col_cluster=True,
                       figsize=(10, 8),
                       cbar_kws={'label': 'Expression'})
    
    g.ax_heatmap.set_xlabel('Genes')
    g.ax_heatmap.set_ylabel('Cells')
    plt.suptitle('Cell Clustering Heatmap', y=1.02)
    
    plt.savefig('cluster_heatmap.png', dpi=150, bbox_inches='tight')
    plt.show()


# ====================
# Part 3: 特征工程与模型优化
# ====================

def demonstrate_feature_engineering():
    """
    演示特征工程的重要性
    
    生物学类比：
    特征工程就像选择合适的生物标记物
    好的标记物让诊断事半功倍
    """
    print_section("特征工程的艺术")
    
    print("""
🔬 特征工程在生物学中的应用：

1. 序列特征：
   - k-mer频率（DNA/蛋白质motif）
   - GC含量、密码子使用偏好
   - 二级结构预测分数

2. 结构特征：
   - 氨基酸理化性质
   - 溶剂可及性
   - 二面角

3. 网络特征：
   - 基因共表达
   - 蛋白质相互作用
   - 代谢通路参与度

4. 组合特征：
   - 特征交互项
   - 多项式特征
   - 特征比率
    """)
    
    # 创建示例：序列特征提取
    def extract_sequence_features(sequence):
        """从DNA序列提取特征"""
        features = {}
        
        # GC含量
        gc_count = sequence.count('G') + sequence.count('C')
        features['gc_content'] = gc_count / len(sequence)
        
        # k-mer频率（2-mer为例）
        kmers = ['AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC',
                 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']
        for kmer in kmers:
            features[f'kmer_{kmer}'] = sequence.count(kmer) / (len(sequence) - 1)
        
        # 序列长度
        features['length'] = len(sequence)
        
        return features
    
    # 示例序列
    sequences = [
        "ATGCGATCGTAGCTAGCTAGCTAGCTAGCTA",
        "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG",
        "ATATATATATATATATATATATATATATAT"
    ]
    
    print("\n示例：DNA序列特征提取")
    for i, seq in enumerate(sequences, 1):
        features = extract_sequence_features(seq)
        print(f"\n序列{i}: {seq[:20]}...")
        print(f"  GC含量: {features['gc_content']:.2f}")
        print(f"  长度: {features['length']}")
        print(f"  AT二聚体频率: {features['kmer_AT']:.2f}")


def hyperparameter_tuning_demo():
    """
    演示超参数调优
    
    生物学类比：
    就像优化PCR条件，需要调整温度、时间、浓度等参数
    """
    print_section("超参数调优")
    
    # 创建示例数据
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=200, n_features=10, 
                              n_informative=5, n_redundant=5,
                              n_classes=2, random_state=42)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # 定义参数网格
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    
    print("🔍 网格搜索超参数...")
    print(f"参数组合总数: {np.prod([len(v) for v in param_grid.values()])}")
    
    # 网格搜索
    rf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(rf, param_grid, cv=5, 
                               scoring='f1', n_jobs=-1)
    
    grid_search.fit(X_train, y_train)
    
    print(f"\n最佳参数: {grid_search.best_params_}")
    print(f"最佳交叉验证分数: {grid_search.best_score_:.3f}")
    
    # 测试集性能
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    test_score = f1_score(y_test, y_pred)
    print(f"测试集F1分数: {test_score:.3f}")
    
    # 可视化参数影响
    results_df = pd.DataFrame(grid_search.cv_results_)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 参数重要性
    param_importance = []
    for param in ['n_estimators', 'max_depth']:
        param_values = results_df[f'param_{param}'].unique()
        mean_scores = []
        for val in param_values:
            mask = results_df[f'param_{param}'] == val
            mean_scores.append(results_df[mask]['mean_test_score'].mean())
        
        ax = axes[0] if param == 'n_estimators' else axes[1]
        ax.plot(param_values, mean_scores, 'o-')
        ax.set_xlabel(param)
        ax.set_ylabel('Mean CV Score')
        ax.set_title(f'Effect of {param}')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('hyperparameter_tuning.png', dpi=150, bbox_inches='tight')
    plt.show()


# ====================
# Part 4: 深度学习初探
# ====================

def introduction_to_deep_learning():
    """
    深度学习在生物信息学中的应用介绍
    """
    print_section("深度学习初探")
    
    print("""
🧠 深度学习在生物学中的革命性应用：

1. AlphaFold - 蛋白质结构预测
   - 输入：氨基酸序列
   - 输出：3D结构坐标
   - 准确度：接近实验水平

2. 基因表达预测
   - 输入：DNA序列
   - 输出：表达水平
   - 应用：理解基因调控

3. 药物发现
   - 输入：分子结构
   - 输出：活性预测
   - 加速：缩短研发周期

4. 医学影像分析
   - 输入：病理切片
   - 输出：疾病诊断
   - 优势：超越人类专家

5. 单细胞分析
   - 输入：scRNA-seq数据
   - 输出：细胞类型、轨迹
   - 发现：新的细胞亚群
    """)
    
    # 简单的神经网络示例（使用sklearn）
    from sklearn.neural_network import MLPClassifier
    
    print("\n📊 简单神经网络示例")
    
    # 创建XOR问题（非线性可分）
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])  # XOR输出
    
    # 训练神经网络
    mlp = MLPClassifier(hidden_layer_sizes=(4,), 
                        activation='relu',
                        max_iter=1000,
                        random_state=42)
    mlp.fit(X, y)
    
    # 预测
    predictions = mlp.predict(X)
    
    print("XOR问题（需要非线性边界）：")
    print("输入 -> 预期输出 -> 预测输出")
    for i in range(len(X)):
        print(f"{X[i]} -> {y[i]} -> {predictions[i]}")
    
    # 可视化决策边界
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 线性模型（失败）
    ax = axes[0]
    log_reg = LogisticRegression()
    log_reg.fit(X, y)
    
    xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 100),
                         np.linspace(-0.5, 1.5, 100))
    Z = log_reg.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdBu')
    ax.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap='RdBu', edgecolor='black')
    ax.set_title('Linear Model (Fails)')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    
    # 神经网络（成功）
    ax = axes[1]
    Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdBu')
    ax.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap='RdBu', edgecolor='black')
    ax.set_title('Neural Network (Success)')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    
    plt.tight_layout()
    plt.savefig('neural_network_xor.png', dpi=150, bbox_inches='tight')
    plt.show()


# ====================
# 主函数
# ====================

def main():
    """主函数 - 运行完整的机器学习教程"""
    
    print("="*60)
    print("🧬 Chapter 10: 机器学习入门 - 模式识别的艺术")
    print("="*60)
    print("""
欢迎来到机器学习的世界！
在生物学中，我们经常需要从复杂的数据中识别模式。
机器学习就是让计算机学会这种模式识别能力。
    """)
    
    # Part 1: 监督学习
    print("\n" + "="*60)
    print("📚 第一部分：监督学习 - 教会计算机识别")
    print("="*60)
    
    # 创建基因分类数据
    df_genes, feature_names = create_gene_classification_data()
    
    # 可视化特征分布
    visualize_feature_distributions(df_genes, feature_names)
    
    # 训练分类模型
    results, X_test, y_test, scaler = train_classification_models(df_genes, feature_names)
    
    # 比较模型性能
    visualize_model_comparison(results)
    
    # 演示过拟合
    demonstrate_overfitting()
    
    # Part 2: 无监督学习
    print("\n" + "="*60)
    print("📚 第二部分：无监督学习 - 发现隐藏模式")
    print("="*60)
    
    # 创建细胞表达数据
    df_cells, true_labels = create_cell_expression_data()
    
    # 确定最优聚类数
    optimal_k = determine_optimal_clusters(StandardScaler().fit_transform(np.log1p(df_cells)))
    
    # 执行聚类分析
    clustering_results, df_scaled, pca = perform_clustering_analysis(df_cells, true_labels)
    
    # 创建聚类热图
    best_clustering = 'K-Means'
    create_cluster_heatmap(df_cells, clustering_results[best_clustering]['labels'])
    
    # Part 3: 特征工程与优化
    print("\n" + "="*60)
    print("📚 第三部分：特征工程与模型优化")
    print("="*60)
    
    # 特征工程演示
    demonstrate_feature_engineering()
    
    # 超参数调优
    hyperparameter_tuning_demo()
    
    # Part 4: 深度学习
    print("\n" + "="*60)
    print("📚 第四部分：深度学习初探")
    print("="*60)
    
    # 深度学习介绍
    introduction_to_deep_learning()
    
    # 总结
    print("\n" + "="*60)
    print("📚 课程总结")
    print("="*60)
    
    print("""
🎯 本章核心要点：

1. 机器学习基础
   ✅ 监督学习：有标签数据的学习（分类、回归）
   ✅ 无监督学习：无标签数据的学习（聚类、降维）
   ✅ 模型评估：准确率、精确率、召回率、F1分数

2. 实践技能
   ✅ 数据预处理：标准化、归一化、对数转换
   ✅ 特征工程：提取、选择、构造特征
   ✅ 模型选择：比较不同算法的性能
   ✅ 超参数调优：网格搜索、交叉验证

3. 生物学应用
   ✅ 基因功能预测
   ✅ 细胞类型识别
   ✅ 疾病分类诊断
   ✅ 药物靶点发现

4. 注意事项
   ⚠️ 避免过拟合：使用交叉验证
   ⚠️ 类别不平衡：调整采样或权重
   ⚠️ 特征选择：去除噪声特征
   ⚠️ 结果解释：结合生物学知识
    """)
    
    print("""
🚀 恭喜你完成了机器学习入门课程！

你已经掌握了：
- 使用scikit-learn进行机器学习
- 理解监督与无监督学习的区别
- 评估和优化模型性能
- 应用机器学习解决生物学问题

下一步建议：
1. 尝试真实的生物数据集（GEO、TCGA）
2. 学习深度学习框架（TensorFlow、PyTorch）
3. 探索专业工具（Scanpy、DESeq2）
4. 参与Kaggle生物信息学竞赛

记住：机器学习是工具，生物学知识是灵魂。
将两者结合，你就能在生物信息学领域大有作为！

祝你在生物信息学的道路上越走越远！🧬💻🔬
    """)


if __name__ == "__main__":
    main()