#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 10: 机器学习入门 - 模式识别的艺术

本章演示机器学习在生物信息学中的核心应用：
- Part 1: 监督学习 - 基因功能预测
- Part 2: 无监督学习 - 细胞亚型发现  
- Part 3: 模型优化 - 提升预测性能
- Part 4: 实战项目 - 癌症分型预测

🧬 生物学类比:
机器学习 = 从数据中学习规律的算法
• 监督学习：有老师的学习（分类、回归）
• 无监督学习：发现隐藏模式（聚类、降维） 
• 模型优化：提升性能的艺术
• 深度学习：AI革命的开始

核心理念：机器学习是工具，生物学知识是灵魂
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
    print(f"{title}")
    print("="*60)


# ====================
# Part 1: 监督学习 - 基因功能分类
# ====================

def create_gene_classification_data():
    """
    创建基因功能分类的示例数据
    
    🧬 生物学背景：
    根据基因序列特征预测功能类别，这在基因注释中极其重要：
    - 管家基因：维持基本细胞功能，表达稳定
    - 转录因子：调控基因表达，序列保守
    - 激酶：信号传导关键酶，结构域特异
    
    🔬 应用场景：
    • 基因组注释和功能预测
    • 药物靶点识别和验证
    • 疾病相关基因筛选
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
    
    print("数据集信息：")
    print(f"  样本数量: {len(df)}")
    print(f"  特征数量: {len(feature_names)}")
    print(f"  类别分布: {df['function'].value_counts().to_dict()}")
    print("\n特征统计：")
    print(df[feature_names].describe().round(3))
    
    return df, feature_names


def visualize_feature_distributions(df, feature_names):
    """可视化特征分布"""
    print("\n可视化特征分布")
    
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
    print("\n模型性能比较")
    
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
    
    🧬 生物学类比：
    过拟合就像医学生死记硬背病例，不理解疾病本质：
    • 欠拟合：过于简化，漏掉重要特征
    • 良好拟合：抓住核心规律，泛化能力强
    • 过拟合：记住噪声，新数据表现差
    
    平衡之道：
    • 增加训练数据（更多病例）
    • 简化模型（抓住主要症状）
    • 正则化（防止过度依赖）
    • 交叉验证（多中心验证）
    """
    print_section("过拟合与欠拟合")
    
    print("""
什么是过拟合？
过拟合就像一个医学生死记硬背了所有病例，
但不理解疾病的本质规律，遇到新病例就束手无策。

如何避免过拟合？
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
    
    🧬 生物学背景：
    单细胞RNA测序揭示细胞异质性，不同细胞类型有独特的表达谱：
    - 干细胞：多能性基因（OCT4, NANOG）高表达
    - 分化中细胞：过渡状态，表达谱动态变化
    - 成熟细胞：特异性功能基因高表达
    
    🔬 科学意义：
    • 发现新的细胞亚型和状态
    • 理解细胞分化轨迹
    • 识别疾病相关的细胞群体
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
    
    print(f"数据集信息：")
    print(f"  细胞数量: {df.shape[0]}")
    print(f"  基因数量: {df.shape[1]}")
    print(f"  表达值范围: [{df.values.min():.2f}, {df.values.max():.2f}]")
    
    return df, true_labels


def perform_clustering_analysis(df, true_labels):
    """
    执行多种聚类分析
    
    🧬 生物学类比：
    聚类分析如同细胞分类学：
    • K-means：找到细胞群的"代表细胞"
    • 层次聚类：构建细胞进化树
    • DBSCAN：识别密集细胞团和异常细胞
    • 高斯混合：细胞群的概率边界
    
    🔬 评估标准：
    • 轮廓系数：群内紧密，群间分离
    • 调整兰德指数：与真实分组的一致性
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
            clusterer.fit(df_scaled)
            labels = clusterer.predict(df_scaled)
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
    print(f"基于轮廓系数，最优聚类数为: {optimal_k}")
    
    return optimal_k


def create_cluster_heatmap(df, labels):
    """创建聚类热图"""
    print("\n创建聚类热图")
    
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
    
    🧬 生物学类比：
    特征工程 = 选择最佳生物标记物
    就像选择最能代表疾病的检测指标
    
    🔬 生物特征类型：
    • 序列特征：GC含量、k-mer频率、保守域
    • 结构特征：二级结构、溶剂可及性  
    • 表达特征：基因共表达、时序动态
    • 网络特征：蛋白相互作用、通路参与
    • 组合特征：特征交互、比值、多项式
    
    工程艺术：
    好的特征让复杂问题变简单！
    """
    print_section("特征工程的艺术")
    
    print("""
特征工程在生物学中的应用：

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
    
    🧬 生物学类比：
    超参数调优如同优化实验条件：
    • PCR：温度、时间、引物浓度
    • 细胞培养：温度、CO2浓度、培养基
    • 测序：深度、读长、质量阈值
    
    优化策略：
    • 网格搜索：穷尽所有组合（耗时）
    • 随机搜索：随机采样（高效）
    • 贝叶斯优化：智能选择下一个尝试
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
    
    print("网格搜索超参数...")
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
    
    🧬 生物学类比：
    深度学习 = 大脑的分层处理机制
    • 第一层：识别边缘（细胞边界）
    • 第二层：识别形状（细胞核）
    • 第三层：识别模式（癌细胞特征）
    • 输出层：做出判断（诊断结果）
    
    🚀 革命性突破：
    • AlphaFold2：破解50年蛋白质结构难题  
    • 基因表达预测：从序列预测表达模式
    • 药物设计：秒级生成候选药物分子
    • 细胞图像分析：超越人类专家精度
    """
    print_section("深度学习初探")
    
    print("""
深度学习：生物信息学的新纪元

突破性应用：

1. AlphaFold2 - 破解50年蛋白质结构难题
   - 输入：氨基酸序列 → 输出：3D原子结构
   - 准确度：原子级精度（GDT > 90）
   - 影响：加速药物研发10倍

2. Enformer - 基因表达预测大模型
   - 输入：200kb DNA序列 → 输出：表达模式  
   - 应用：理解基因调控机制
   - 意义：解密非编码区域功能

3. 药物设计 - 生成式模型
   - 输入：靶点结构 → 输出：候选药物分子
   - 速度：秒级生成 vs 月级筛选
   - 成功案例：COVID-19药物发现

4. 细胞图像分析 - 计算病理学
   - 输入：显微镜图像 → 输出：细胞类型/状态
   - 精度：超越人类专家水平
   - 应用：癌症早期诊断、药物筛选

5. 单细胞深度学习 - scBERT/scGPT
   - 输入：scRNA-seq数据 → 输出：细胞注释
   - 发现：新的细胞亚群和轨迹
   - 革命：单细胞生物学新范式
    """)
    
    # 简单的神经网络示例（使用sklearn）
    from sklearn.neural_network import MLPClassifier
    
    print("\n简单神经网络示例")
    
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
# Part 5: 真实数据处理 - 实战技能训练
# ====================

def handle_real_single_cell_data():
    """
    处理真实的单细胞RNA-seq数据
    
    🧬 生物学背景：
    单细胞测序数据的特点：
    - 高维稀疏：20000+ 基因，大多数值为0
    - 批次效应：不同实验批次间的系统性差异
    - 细胞异质性：同类细胞间的表达差异
    - 技术噪声：测序深度、扩增偏差等
    
    🔬 教学目标：
    • 学会处理真实生物数据的常见挑战
    • 掌握数据质量控制流程
    • 理解批次效应及其校正方法
    • 应用机器学习进行细胞分型
    """
    print_section("Part 5.1: 真实单细胞数据处理")
    
    import os
    
    # 读取真实单细胞数据
    data_file = os.path.join("..", "data", "single_cell_sample.csv")
    
    try:
        print("读取真实单细胞数据...")
        df_sc = pd.read_csv(data_file)
        print(f"数据加载成功: {df_sc.shape[0]} 细胞 × {df_sc.shape[1]} 特征")
    except FileNotFoundError:
        print("数据文件未找到，跳过真实数据分析")
        return
    
    # 数据预处理
    print(f"\n数据预览:")
    print(df_sc.head())
    
    # 分离元数据和表达数据
    meta_cols = ['cell_id', 'batch', 'cell_type']
    gene_cols = [col for col in df_sc.columns if col not in meta_cols]
    
    print(f"\n数据结构分析:")
    print(f"  - 元数据列: {len(meta_cols)} 个 ({meta_cols})")
    print(f"  - 基因表达列: {len(gene_cols)} 个")
    print(f"  - 细胞类型: {df_sc['cell_type'].nunique()} 种")
    print(f"  - 实验批次: {df_sc['batch'].nunique()} 个")
    
    # 数据质量控制
    print(f"\n数据质量控制:")
    
    # 1. 表达量统计
    expression_data = df_sc[gene_cols]
    total_counts = expression_data.sum(axis=1)
    detected_genes = (expression_data > 0).sum(axis=1)
    
    print(f"每细胞统计:")
    print(f"  - 平均总表达量: {total_counts.mean():.1f} ± {total_counts.std():.1f}")
    print(f"  - 平均检测基因数: {detected_genes.mean():.1f} ± {detected_genes.std():.1f}")
    print(f"  - 数据稀疏度: {(expression_data == 0).sum().sum() / expression_data.size * 100:.1f}%")
    
    # 2. 批次效应检测
    print(f"\n🔬 批次效应检测:")
    batch_stats = df_sc.groupby('batch').agg({
        gene_cols[0]: 'mean',  # 用第一个基因作为例子
        'cell_type': 'count'
    })
    print("各批次统计:")
    print(batch_stats)
    
    # 数据标准化（log1p变换 + z-score）
    print(f"\n数据标准化:")
    # 1. log1p变换处理偏态分布
    expression_log = np.log1p(expression_data)
    
    # 2. z-score标准化
    scaler = StandardScaler()
    expression_scaled = scaler.fit_transform(expression_log)
    
    print("标准化步骤:")
    print("  1. log1p变换: 处理数据偏态分布")
    print("  2. z-score标准化: 消除量纲影响")
    print(f"  3. 标准化后范围: [{expression_scaled.min():.2f}, {expression_scaled.max():.2f}]")
    
    # 降维分析（PCA + t-SNE）
    print(f"\n降维分析:")
    
    # PCA降维
    pca = PCA(n_components=10)
    pca_result = pca.fit_transform(expression_scaled)
    
    print(f"PCA分析:")
    print(f"  - 前3个主成分解释方差: {pca.explained_variance_ratio_[:3].sum():.2f}")
    print(f"  - 前5个主成分解释方差: {pca.explained_variance_ratio_[:5].sum():.2f}")
    
    # t-SNE可视化
    if len(df_sc) > 5:  # 确保有足够样本
        tsne = TSNE(n_components=2, random_state=42, perplexity=min(5, len(df_sc)-1))
        tsne_result = tsne.fit_transform(pca_result[:, :5])  # 先PCA再t-SNE
        
        # 可视化结果
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('单细胞数据分析结果', fontsize=14)
        
        # 1. PCA结果（按细胞类型着色）
        ax = axes[0, 0]
        unique_types = df_sc['cell_type'].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(unique_types)))
        
        for cell_type, color in zip(unique_types, colors):
            mask = df_sc['cell_type'] == cell_type
            ax.scatter(pca_result[mask, 0], pca_result[mask, 1], 
                      c=[color], label=cell_type, alpha=0.7, s=50)
        ax.set_title('PCA - 按细胞类型')
        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2f})')
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2f})')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # 2. PCA结果（按批次着色）
        ax = axes[0, 1]
        unique_batches = df_sc['batch'].unique()
        batch_colors = plt.cm.Set1(np.linspace(0, 1, len(unique_batches)))
        
        for batch, color in zip(unique_batches, batch_colors):
            mask = df_sc['batch'] == batch
            ax.scatter(pca_result[mask, 0], pca_result[mask, 1], 
                      c=[color], label=batch, alpha=0.7, s=50)
        ax.set_title('PCA - 按实验批次')
        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2f})')
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2f})')
        ax.legend()
        
        # 3. t-SNE结果（按细胞类型）
        ax = axes[1, 0]
        for cell_type, color in zip(unique_types, colors):
            mask = df_sc['cell_type'] == cell_type
            ax.scatter(tsne_result[mask, 0], tsne_result[mask, 1], 
                      c=[color], label=cell_type, alpha=0.7, s=50)
        ax.set_title('t-SNE - 按细胞类型')
        ax.set_xlabel('t-SNE 1')
        ax.set_ylabel('t-SNE 2')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # 4. t-SNE结果（按批次）
        ax = axes[1, 1]
        for batch, color in zip(unique_batches, batch_colors):
            mask = df_sc['batch'] == batch
            ax.scatter(tsne_result[mask, 0], tsne_result[mask, 1], 
                      c=[color], label=batch, alpha=0.7, s=50)
        ax.set_title('t-SNE - 按实验批次')
        ax.set_xlabel('t-SNE 1')
        ax.set_ylabel('t-SNE 2')
        ax.legend()
        
        plt.tight_layout()
        plt.savefig('single_cell_analysis.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    # 细胞分型预测
    print(f"\n细胞分型预测:")
    
    # 准备数据
    X = expression_scaled
    y = df_sc['cell_type']
    
    # 分离训练和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # 训练随机森林分类器
    rf_classifier = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced'  # 处理类别不平衡
    )
    
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)
    
    # 评估结果
    accuracy = accuracy_score(y_test, y_pred)
    print(f"分类准确率: {accuracy:.3f}")
    
    if len(y_test) > 0:
        print("\n详细分类报告:")
        print(classification_report(y_test, y_pred))
    
    # 特征重要性分析
    print(f"\n重要基因标记:")
    feature_importance = pd.DataFrame({
        'gene': gene_cols,
        'importance': rf_classifier.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("Top 5 重要基因:")
    print(feature_importance.head().to_string(index=False))
    
    print(f"\n生物学解释:")
    print("• CD3D, CD4: T细胞标记基因")
    print("• MS4A1, CD19: B细胞标记基因") 
    print("• LYZ, CSF1R: 单核细胞/巨噬细胞标记")
    print("• NKG7, KLRD1: NK细胞标记")
    print("• 特征重要性反映基因在细胞分型中的贡献")


def handle_cancer_clinical_data():
    """
    处理癌症临床数据进行预后预测
    
    🧬 生物学背景：
    癌症预后预测是精准医疗的重要应用：
    - 临床特征：年龄、性别、分期、分级
    - 分子标记：关键基因表达水平
    - 治疗信息：手术、化疗、放疗方案
    - 生存数据：生存时间、生存状态
    
    🔬 教学目标：
    • 学会处理混合数据类型（数值、分类）
    • 理解特征工程在临床数据中的应用
    • 掌握生存预测的建模策略
    • 解释模型结果的临床意义
    """
    print_section("Part 5.2: 癌症临床数据分析")
    
    import os
    
    # 读取癌症临床数据
    data_file = os.path.join("..", "data", "cancer_clinical_data.csv")
    
    try:
        print("读取癌症临床数据...")
        df_cancer = pd.read_csv(data_file)
        print(f"数据加载成功: {df_cancer.shape[0]} 患者 × {df_cancer.shape[1]} 特征")
    except FileNotFoundError:
        print("数据文件未找到，跳过癌症数据分析")
        return
    
    # 数据预览
    print(f"\n数据预览:")
    print(df_cancer.head())
    
    # 数据结构分析
    print(f"\n数据结构分析:")
    clinical_cols = ['age', 'gender', 'stage', 'grade', 'treatment']
    survival_cols = ['survival_months', 'vital_status']
    gene_cols = [col for col in df_cancer.columns 
                 if col not in clinical_cols + survival_cols + ['patient_id']]
    
    print(f"  - 临床特征: {len(clinical_cols)} 个")
    print(f"  - 生存信息: {len(survival_cols)} 个")
    print(f"  - 基因表达: {len(gene_cols)} 个")
    
    # 描述性统计
    print(f"\n📈 描述性统计:")
    print(f"患者特征:")
    print(f"  - 年龄范围: {df_cancer['age'].min()}-{df_cancer['age'].max()} 岁")
    print(f"  - 性别分布: {df_cancer['gender'].value_counts().to_dict()}")
    print(f"  - 分期分布: {df_cancer['stage'].value_counts().to_dict()}")
    print(f"  - 生存状态: {df_cancer['vital_status'].value_counts().to_dict()}")
    print(f"  - 平均生存时间: {df_cancer['survival_months'].mean():.1f} 月")
    
    # 数据清洗和预处理
    print(f"\n⚡ 数据预处理:")
    
    # 1. 编码分类变量
    le_gender = LabelEncoder()
    le_stage = LabelEncoder()
    le_grade = LabelEncoder()
    le_treatment = LabelEncoder()
    le_vital = LabelEncoder()
    
    df_processed = df_cancer.copy()
    df_processed['gender_encoded'] = le_gender.fit_transform(df_cancer['gender'])
    df_processed['stage_encoded'] = le_stage.fit_transform(df_cancer['stage'])
    df_processed['grade_encoded'] = le_grade.fit_transform(df_cancer['grade'])
    df_processed['treatment_encoded'] = le_treatment.fit_transform(df_cancer['treatment'])
    df_processed['vital_status_encoded'] = le_vital.fit_transform(df_cancer['vital_status'])
    
    print("分类变量编码完成:")
    print(f"  - 性别: {list(le_gender.classes_)}")
    print(f"  - 分期: {list(le_stage.classes_)}")
    print(f"  - 治疗: {list(le_treatment.classes_)}")
    
    # 2. 特征工程
    print(f"\n特征工程:")
    
    # 创建组合特征
    df_processed['age_stage_score'] = df_processed['age'] * df_processed['stage_encoded']
    df_processed['gene_risk_score'] = df_processed[['TP53', 'BRCA1', 'EGFR']].mean(axis=1)
    df_processed['oncogene_score'] = df_processed[['MYC', 'KRAS', 'PIK3CA']].mean(axis=1)
    
    # 创建年龄组
    df_processed['age_group'] = pd.cut(df_processed['age'], 
                                      bins=[0, 45, 60, 100], 
                                      labels=['Young', 'Middle', 'Old'])
    df_processed['age_group_encoded'] = LabelEncoder().fit_transform(df_processed['age_group'])
    
    print("新特征创建:")
    print("  - age_stage_score: 年龄-分期交互特征")
    print("  - gene_risk_score: 肿瘤抑制基因评分")
    print("  - oncogene_score: 癌基因评分")
    print("  - age_group: 年龄分组")
    
    # 3. 特征选择
    feature_cols = (['age', 'gender_encoded', 'stage_encoded', 'grade_encoded', 
                    'treatment_encoded'] + gene_cols + 
                    ['age_stage_score', 'gene_risk_score', 'oncogene_score', 'age_group_encoded'])
    
    X = df_processed[feature_cols]
    y_survival = df_processed['vital_status_encoded']  # 生存状态预测
    y_time = df_processed['survival_months']          # 生存时间预测
    
    # 数据标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print(f"\n最终特征矩阵: {X_scaled.shape}")
    
    # 生存状态预测
    print(f"\n生存状态预测模型:")
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_survival, test_size=0.3, random_state=42, stratify=y_survival
    )
    
    # 比较多种模型
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'SVM': SVC(random_state=42, probability=True)
    }
    
    results = {}
    for name, model in models.items():
        # 训练模型
        model.fit(X_train, y_train)
        
        # 预测和评估
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
        
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred_proba) if y_pred_proba is not None else None
        
        results[name] = {
            'accuracy': accuracy,
            'f1_score': f1,
            'auc': auc,
            'model': model
        }
        
        print(f"{name}:")
        print(f"  - 准确率: {accuracy:.3f}")
        print(f"  - F1分数: {f1:.3f}")
        if auc:
            print(f"  - AUC: {auc:.3f}")
    
    # 特征重要性分析（使用最佳模型）
    best_model_name = max(results.keys(), key=lambda x: results[x]['accuracy'])
    best_model = results[best_model_name]['model']
    
    print(f"\n特征重要性分析 (基于{best_model_name}):")
    
    if hasattr(best_model, 'feature_importances_'):
        importance_df = pd.DataFrame({
            'feature': feature_cols,
            'importance': best_model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("Top 10 重要特征:")
        print(importance_df.head(10).to_string(index=False))
        
        # 可视化特征重要性
        plt.figure(figsize=(10, 6))
        top_features = importance_df.head(10)
        plt.barh(range(len(top_features)), top_features['importance'])
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('特征重要性')
        plt.title(f'特征重要性排序 ({best_model_name})')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig('feature_importance_cancer.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    # 生存曲线分析（简化版）
    print(f"\n生存分析:")
    
    # 按风险评分分组
    risk_scores = best_model.predict_proba(X_scaled)[:, 1] if hasattr(best_model, 'predict_proba') else best_model.decision_function(X_scaled)
    df_processed['risk_score'] = risk_scores
    
    # 分为高风险和低风险组
    risk_threshold = np.median(risk_scores)
    df_processed['risk_group'] = df_processed['risk_score'].apply(
        lambda x: 'High Risk' if x > risk_threshold else 'Low Risk'
    )
    
    print("风险分层结果:")
    risk_summary = df_processed.groupby('risk_group').agg({
        'survival_months': ['count', 'mean', 'std'],
        'vital_status': lambda x: (x == 'Dead').sum()
    })
    print(risk_summary)
    
    print(f"\n临床解释:")
    print("• 分期和分级是最重要的预后因素")
    print("• TP53和BRCA1等肿瘤抑制基因表达影响预后")
    print("• 年龄和治疗方案也对生存有显著影响")
    print("• 多基因评分可以改善预后预测准确性")
    
    return df_processed


def demonstrate_batch_effect_correction():
    """
    演示批次效应检测和校正
    
    🧬 生物学背景：
    批次效应是生物数据分析中的重要问题：
    - 技术批次：不同实验批次、操作人员、试剂批号
    - 生物批次：不同时间、地点、种群的样本
    - 系统性偏差：影响所有基因的非生物学因素
    
    🔬 处理策略：
    • 检测：PCA分析、聚类分析观察批次聚集
    • 校正：ComBat算法、线性混合模型
    • 验证：校正前后效果对比
    """
    print_section("Part 5.3: 批次效应检测与校正")
    
    # 创建带批次效应的模拟数据
    print("创建批次效应模拟数据...")
    
    np.random.seed(42)
    n_samples = 60
    n_genes = 20
    
    # 创建两个批次的数据
    batch1_data = np.random.normal(5, 1, (30, n_genes))  # 批次1：均值5
    batch2_data = np.random.normal(7, 1, (30, n_genes))  # 批次2：均值7（系统性升高）
    
    # 添加生物学信号（部分基因在不同条件下差异表达）
    condition1_indices = list(range(0, 15)) + list(range(30, 45))  # 条件1
    condition2_indices = list(range(15, 30)) + list(range(45, 60)) # 条件2
    
    # 在部分基因中添加条件特异性信号
    for gene_idx in [0, 1, 2]:  # 前3个基因有条件效应
        batch1_data[15:30, gene_idx] += 2  # 批次1中条件2样本上调
        batch2_data[15:30, gene_idx] += 2  # 批次2中条件2样本上调
    
    # 组合数据
    expression_data = np.vstack([batch1_data, batch2_data])
    
    # 创建元数据
    batch_labels = ['Batch1'] * 30 + ['Batch2'] * 30
    condition_labels = (['Condition1'] * 15 + ['Condition2'] * 15) * 2
    
    df_batch = pd.DataFrame({
        'sample_id': [f'Sample_{i:03d}' for i in range(n_samples)],
        'batch': batch_labels,
        'condition': condition_labels,
        **{f'Gene_{i:02d}': expression_data[:, i] for i in range(n_genes)}
    })
    
    gene_cols = [f'Gene_{i:02d}' for i in range(n_genes)]
    
    print(f"数据创建完成: {n_samples} 样本 × {n_genes} 基因")
    print(f"批次分布: {pd.Series(batch_labels).value_counts().to_dict()}")
    print(f"条件分布: {pd.Series(condition_labels).value_counts().to_dict()}")
    
    # 1. 批次效应检测
    print(f"\n批次效应检测:")
    
    # PCA分析检测批次效应
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(df_batch[gene_cols])
    
    print(f"PCA分析:")
    print(f"  - PC1解释方差: {pca.explained_variance_ratio_[0]:.3f}")
    print(f"  - PC2解释方差: {pca.explained_variance_ratio_[1]:.3f}")
    print(f"  - 前2个PC累计解释方差: {pca.explained_variance_ratio_[:2].sum():.3f}")
    
    # 可视化批次效应
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('批次效应检测与校正', fontsize=14)
    
    # 校正前 - 按批次着色
    ax = axes[0, 0]
    for batch in df_batch['batch'].unique():
        mask = df_batch['batch'] == batch
        color = 'red' if batch == 'Batch1' else 'blue'
        ax.scatter(pca_result[mask, 0], pca_result[mask, 1], 
                  c=color, label=batch, alpha=0.7, s=50)
    ax.set_title('校正前 - 按批次着色')
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2f})')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2f})')
    ax.legend()
    
    # 校正前 - 按条件着色
    ax = axes[0, 1]
    for condition in df_batch['condition'].unique():
        mask = df_batch['condition'] == condition
        color = 'green' if condition == 'Condition1' else 'orange'
        ax.scatter(pca_result[mask, 0], pca_result[mask, 1], 
                  c=color, label=condition, alpha=0.7, s=50)
    ax.set_title('校正前 - 按条件着色')
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2f})')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2f})')
    ax.legend()
    
    # 2. 批次效应校正（简化版ComBat）
    print(f"\n批次效应校正:")
    
    # 简化的批次校正：z-score标准化 + 批次均值居中
    corrected_data = df_batch[gene_cols].copy()
    
    # 按批次进行z-score标准化
    for batch in df_batch['batch'].unique():
        batch_mask = df_batch['batch'] == batch
        batch_data = corrected_data[batch_mask]
        
        # 计算批次内的均值和标准差
        batch_mean = batch_data.mean()
        batch_std = batch_data.std()
        
        # z-score标准化
        corrected_data.loc[batch_mask] = (batch_data - batch_mean) / batch_std
    
    # 全局重新缩放
    global_mean = df_batch[gene_cols].mean().mean()
    global_std = df_batch[gene_cols].std().mean()
    corrected_data = corrected_data * global_std + global_mean
    
    print("校正步骤:")
    print("  1. 批次内z-score标准化")
    print("  2. 全局均值方差重新缩放")
    print(f"  3. 校正前数据范围: [{df_batch[gene_cols].min().min():.2f}, {df_batch[gene_cols].max().max():.2f}]")
    print(f"  4. 校正后数据范围: [{corrected_data.min().min():.2f}, {corrected_data.max().max():.2f}]")
    
    # 校正后PCA分析
    pca_corrected = PCA(n_components=3)
    pca_corrected_result = pca_corrected.fit_transform(corrected_data)
    
    # 校正后 - 按批次着色
    ax = axes[1, 0]
    for batch in df_batch['batch'].unique():
        mask = df_batch['batch'] == batch
        color = 'red' if batch == 'Batch1' else 'blue'
        ax.scatter(pca_corrected_result[mask, 0], pca_corrected_result[mask, 1], 
                  c=color, label=batch, alpha=0.7, s=50)
    ax.set_title('校正后 - 按批次着色')
    ax.set_xlabel(f'PC1 ({pca_corrected.explained_variance_ratio_[0]:.2f})')
    ax.set_ylabel(f'PC2 ({pca_corrected.explained_variance_ratio_[1]:.2f})')
    ax.legend()
    
    # 校正后 - 按条件着色
    ax = axes[1, 1]
    for condition in df_batch['condition'].unique():
        mask = df_batch['condition'] == condition
        color = 'green' if condition == 'Condition1' else 'orange'
        ax.scatter(pca_corrected_result[mask, 0], pca_corrected_result[mask, 1], 
                  c=color, label=condition, alpha=0.7, s=50)
    ax.set_title('校正后 - 按条件着色')
    ax.set_xlabel(f'PC1 ({pca_corrected.explained_variance_ratio_[0]:.2f})')
    ax.set_ylabel(f'PC2 ({pca_corrected.explained_variance_ratio_[1]:.2f})')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('batch_effect_correction.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 3. 校正效果评估
    print(f"\n校正效果评估:")
    
    # 计算批次间距离
    def calculate_batch_separation(data, batch_labels):
        """计算不同批次间的平均距离"""
        distances = []
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if batch_labels[i] != batch_labels[j]:
                    dist = np.linalg.norm(data[i] - data[j])
                    distances.append(dist)
        return np.mean(distances)
    
    # 校正前后批次分离度
    orig_separation = calculate_batch_separation(pca_result[:, :2], batch_labels)
    corrected_separation = calculate_batch_separation(pca_corrected_result[:, :2], batch_labels)
    
    print(f"批次分离度评估:")
    print(f"  - 校正前批次间平均距离: {orig_separation:.3f}")
    print(f"  - 校正后批次间平均距离: {corrected_separation:.3f}")
    print(f"  - 改善程度: {(orig_separation - corrected_separation) / orig_separation * 100:.1f}%")
    
    # 计算生物学信号保留
    def calculate_condition_separation(data, condition_labels):
        """计算不同条件间的平均距离"""
        distances = []
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if condition_labels[i] != condition_labels[j]:
                    dist = np.linalg.norm(data[i] - data[j])
                    distances.append(dist)
        return np.mean(distances)
    
    orig_bio_signal = calculate_condition_separation(pca_result[:, :2], condition_labels)
    corrected_bio_signal = calculate_condition_separation(pca_corrected_result[:, :2], condition_labels)
    
    print(f"\n生物学信号保留:")
    print(f"  - 校正前条件间距离: {orig_bio_signal:.3f}")
    print(f"  - 校正后条件间距离: {corrected_bio_signal:.3f}")
    print(f"  - 信号保留率: {corrected_bio_signal / orig_bio_signal * 100:.1f}%")
    
    print(f"\n批次校正建议:")
    print("- 始终在分析前检查批次效应")
    print("- 实验设计时随机分配样本到不同批次")
    print("- 使用专业工具如ComBat、limma进行校正")
    print("- 校正后验证生物学信号是否保留")
    print("- 批次和条件不要完全混杂")


# ====================
# 主函数
# ====================

def main():
    """
    主函数 - 运行完整的机器学习教程
    
    展示机器学习在生物信息学中的完整应用流程，
    从数据预处理到模型部署，包括所有关键步骤。
    """
    
    print("="*60)
    print("Chapter 10: 机器学习入门 - 模式识别的艺术")
    print("="*60)
    print("""
欢迎来到机器学习的世界！
在生物学中，我们经常需要从复杂的数据中识别模式。
机器学习就是让计算机学会这种模式识别能力。
    """)
    
    # Part 1: 监督学习
    print("\n" + "="*60)
    print("第一部分：监督学习 - 教会计算机识别")
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
    print("第二部分：无监督学习 - 发现隐藏模式")
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
    print("第三部分：特征工程与模型优化")
    print("="*60)
    
    # 特征工程演示
    demonstrate_feature_engineering()
    
    # 超参数调优
    hyperparameter_tuning_demo()
    
    # Part 4: 深度学习
    print("\n" + "="*60)
    print("第四部分：深度学习初探")
    print("="*60)
    
    # 深度学习介绍
    introduction_to_deep_learning()
    
    # Part 5: 真实数据处理实战
    print("\n" + "="*60)
    print("第五部分：真实数据处理实战")
    print("="*60)
    
    print("""
实战能力训练：
本部分将使用真实的生物数据，训练你处理实际科研中遇到的数据挑战。
包括批次效应、数据质量控制、特征工程等关键技能。
    """)
    
    # 真实单细胞数据处理
    handle_real_single_cell_data()
    
    # 真实癌症临床数据分析
    handle_cancer_clinical_data()
    
    # 批次效应检测和校正
    demonstrate_batch_effect_correction()
    
    # 总结
    print("\n" + "="*60)
    print("课程总结")
    print("="*60)
    
    print("""
本章核心要点：

机器学习基础：
   - 监督学习：有老师的学习（分类、回归）
   - 无监督学习：发现隐藏模式（聚类、降维）
   - 模型评估：准确率、精确率、召回率、AUC

实践技能：
   - 数据预处理：清洗、转换、标准化
   - 特征工程：提取、选择、构造特征
   - 模型选择：比较多种算法性能
   - 超参数调优：网格搜索、贝叶斯优化

生物学应用：
   - 基因功能预测：从序列到功能
   - 细胞类型识别：单细胞分析革命
   - 疾病分类诊断：精准医疗基础
   - 药物靶点发现：AI加速药物研发

实战技能（新增）：
   - 真实数据处理：单细胞RNA-seq分析流程
   - 临床数据建模：癌症预后预测实战
   - 批次效应校正：多批次数据整合技术
   - 质量控制：数据预处理和清洗流程

关键注意事项：
   - 避免过拟合：交叉验证 + 正则化
   - 处理不平衡：权重调整 + 采样策略
   - 特征选择：去除噪声，保留信号
   - 结果解释：结合领域知识是关键
   - 批次效应：检测和校正系统性偏差
    """)
    
    print("""
恭喜你完成机器学习入门课程！

你已经掌握：
- 使用scikit-learn进行机器学习
- 理解监督与无监督学习的本质区别
- 掌握模型评估和优化技巧
- 在生物信息学中应用机器学习
- 理解深度学习的潜力和应用

下一步建议：
1. 实践项目：尝试TCGA、GEO等真实数据集
2. 深度学习：学习PyTorch/TensorFlow框架
3. 专业工具：掌握Scanpy、Seurat、DESeq2
4. 竞赛参与：Kaggle生物信息学挑战赛
5. 开源贡献：参与生物信息学开源项目

核心理念：
"机器学习是工具，生物学知识是灵魂！"

将AI技术与生物学洞察完美结合，
你将成为新时代的计算生物学家！

继续探索，改变世界！
    """)


if __name__ == "__main__":
    main()