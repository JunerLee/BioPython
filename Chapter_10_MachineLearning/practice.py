#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 10 练习题: 机器学习入门 - 模式识别的艺术

这些练习将帮助你巩固机器学习的基础概念，
并学会在生物信息学中应用这些技术。

练习顺序：
1. 数据预处理和探索性分析
2. 监督学习 - 分类任务
3. 无监督学习 - 聚类分析
4. 模型评估和优化
5. 综合实战项目

每个练习都包含：
- 背景描述
- 任务要求
- 期待输出
- 提示信息
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def exercise_1_data_preprocessing():
    """
    练习1: 数据预处理和探索性分析
    
    背景：
    你获得了一个包含100个蛋白质的数据集，包含以下特征：
    - 分子量 (molecular_weight)
    - 等电点 (isoelectric_point) 
    - 氨基酸数量 (amino_acid_count)
    - 疏水性指数 (hydrophobicity)
    - 不稳定性指数 (instability)
    
    任务：
    1. 生成模拟数据
    2. 进行描述性统计分析
    3. 检查缺失值和异常值
    4. 数据标准化
    5. 绘制相关性热图
    """
    print("=" * 60)
    print("🧬 练习1: 蛋白质数据预处理")
    print("=" * 60)
    
    # TODO: 创建模拟蛋白质数据
    # 提示: 使用np.random设置随机种子确保结果可重现
    np.random.seed(42)
    
    # TODO: 创建100个蛋白质的特征数据
    # 生物学背景设定：
    # 分子量: 5-150 kDa （大多数蛋白质在此范围），对数正态分布
    # 等电点: 4.0-11.0 （蛋白质pI范围），正态分布偏酸性  
    # 氨基酸数量: 50-2000 （结构域到大型蛋白质），与分子量相关
    # 疏水性指数: -2.5到2.5 （GRAVY值范围），正态分布
    # 不稳定性指数: 0-100 （Instability Index），指数分布
    
    protein_data = {
        'molecular_weight': None,  # 请完成
        'isoelectric_point': None,  # 请完成
        'amino_acid_count': None,   # 请完成
        'hydrophobicity': None,     # 请完成
        'instability': None         # 请完成
    }
    
    # TODO: 转换为DataFrame
    df = pd.DataFrame(protein_data)
    
    # TODO: 添加一些缺失值(随机选择5个位置)
    
    # TODO: 添加一些异常值(将几个数值设置为极端值)
    
    print("数据集基本信息:")
    print(f"数据形状: {df.shape}")
    # TODO: 显示前5行数据
    
    print("\n描述性统计:")
    # TODO: 显示describe()结果
    
    print("\n缺失值检查:")
    # TODO: 检查并显示缺失值数量
    
    # TODO: 处理缺失值(用均值填充)
    
    # TODO: 检测异常值(使用IQR方法或Z-score方法)
    
    # TODO: 数据标准化
    scaler = StandardScaler()
    # df_scaled = ...
    
    # TODO: 绘制相关性热图
    plt.figure(figsize=(10, 8))
    # correlation_matrix = ...
    # sns.heatmap(correlation_matrix, ...)
    plt.title('蛋白质特征相关性热图')
    plt.show()
    
    print("✅ 练习1完成！")
    return df  # 返回处理后的数据


def exercise_2_gene_function_classifier():
    """
    练习2: 基因功能分类器
    
    🧬 生物学背景：
    基于多维特征预测基因功能类别：
    - 结构蛋白基因：编码胶原蛋白、酸蛋白等结构成分
    - 酶基因：编码催化生化反应的酶类
    - 调节蛋白基因：编码转录因子、信号分子等
    
    🔍 特征工程：
    - GC含量：与基因表达水平相关
    - 基因长度：与功能复杂性相关
    - 外显子数量：反映调控复杂性
    - 保存性评分：重要功能基因更保守
    - 表达水平：不同功能类别表达模式不同
    - 甲基化水平：表观遗传修饰影响基因表达
    """
    print("\n" + "=" * 60)
    print("🧬 练习2: 基因功能分类器")
    print("=" * 60)
    
    # TODO: 创建基因分类数据
    # 使用make_classification创建3分类问题
    # n_samples=300, n_features=8, n_classes=3, n_informative=6
    np.random.seed(42)
    
    # X, y = make_classification(...)
    X, y = None, None  # 请完成
    
    # 添加生物学意义明确的特征名称
    feature_names = [
        'gc_content',           # GC含量：与基因表达级别和染色质结构相关
        'gene_length',          # 基因长度：复杂功能基因通常更长
        'exon_count',           # 外显子数：反映替代剖接复杂性
        'intron_length',        # 内含子长度：调节元件分布区域
        'promoter_strength',    # 启动子强度：基础转录活性
        'conservation_score',   # 进化保守性：功能重要性指示
        'expression_level',     # 表达水平：组织特异性和时间动态
        'methylation_level'     # 甲基化水平：表观遗传调控状态
    ]
    
    # TODO: 创建DataFrame
    df = pd.DataFrame(X, columns=feature_names)
    df['function_class'] = y
    
    print("基因分类数据信息:")
    print(f"样本数量: {len(df)}")
    print(f"特征数量: {len(feature_names)}")
    print(f"类别分布:\n{df['function_class'].value_counts()}")
    
    # TODO: 可视化类别分布
    plt.figure(figsize=(12, 4))
    
    # 子图1: 类别分布柱状图
    plt.subplot(1, 3, 1)
    # df['function_class'].value_counts().plot(kind='bar')
    plt.title('基因功能类别分布')
    
    # 子图2: 特征分布箱线图(选择前4个特征)
    plt.subplot(1, 3, 2)
    # df[feature_names[:4]].boxplot()
    plt.title('特征分布')
    
    # 子图3: 不同类别下某个特征的分布
    plt.subplot(1, 3, 3)
    # for class_id in range(3):
    #     data = df[df['function_class'] == class_id]['gc_content']
    #     plt.hist(data, alpha=0.5, label=f'Class {class_id}', bins=15)
    plt.title('GC含量在不同类别中的分布')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # TODO: 数据分割
    # X_train, X_test, y_train, y_test = train_test_split(...)
    
    # TODO: 数据标准化
    # scaler = StandardScaler()
    # X_train_scaled = ...
    # X_test_scaled = ...
    
    # TODO: 训练多个分类模型
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.svm import SVC
    from sklearn.naive_bayes import GaussianNB
    
    models = {
        '逻辑回归': LogisticRegression(random_state=42),
        '决策树': DecisionTreeClassifier(random_state=42),
        '随机森林': RandomForestClassifier(random_state=42),
        'SVM': SVC(random_state=42),
        '朴素贝叶斯': GaussianNB()
    }
    
    results = {}
    
    # TODO: 训练每个模型并评估
    for name, model in models.items():
        print(f"\n训练 {name}...")
        
        # 训练模型
        # model.fit(...)
        
        # 预测
        # y_pred = model.predict(...)
        
        # 计算准确率
        # accuracy = accuracy_score(...)
        
        # 存储结果
        # results[name] = {'accuracy': accuracy, 'y_pred': y_pred}
        
        print(f"  准确率: {None}")  # 请完成
    
    # TODO: 可视化模型比较
    plt.figure(figsize=(10, 6))
    # model_names = list(results.keys())
    # accuracies = [results[name]['accuracy'] for name in model_names]
    # plt.bar(model_names, accuracies)
    plt.title('模型性能比较')
    plt.ylabel('准确率')
    plt.xticks(rotation=45)
    plt.show()
    
    # TODO: 选择最佳模型并显示详细报告
    # best_model = max(results.keys(), key=lambda k: results[k]['accuracy'])
    # best_pred = results[best_model]['y_pred']
    
    print(f"\n最佳模型: {None}")  # 请完成
    print("分类报告:")
    # print(classification_report(y_test, best_pred, 
    #                           target_names=['结构蛋白', '酶', '调节蛋白']))
    
    # TODO: 绘制混淆矩阵
    plt.figure(figsize=(8, 6))
    # cm = confusion_matrix(y_test, best_pred)
    # sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
    #             xticklabels=['结构蛋白', '酶', '调节蛋白'],
    #             yticklabels=['结构蛋白', '酶', '调节蛋白'])
    plt.title('混淆矩阵')
    plt.show()
    
    print("✅ 练习2完成！")
    return results


def exercise_3_cell_clustering():
    """
    练习3: 单细胞聚类分析
    
    🧬 科学背景：
    单细胞RNA测序(scRNA-seq)是现代细胞生物学的革命性技术。
    通过分析单个细胞的基因表达谱，我们可以：
    • 发现新的细胞亚型和状态
    • 揭示细胞分化轨迹和谱系关系
    • 理解疾病中的细胞异质性
    • 识别稀有细胞类型和状态
    
    🔍 数据特点：
    - 高维性：每个细胞~20,000个基因
    - 稀疏性：大部分基因不表达(dropout)
    - 噪声：技术噪声和生物噪声
    - 异质性：细胞周期、状态差异
    
    📊 分析流程：
    1. 质量控制：过滤低质量细胞和基因
    2. 归一化：消除技术变异和批次效应
    3. 特征选择：找到高变异基因(HVGs)
    4. 降维：PCA消除噪声，t-SNE/UMAP可视化
    5. 聚类：识别细胞群体
    6. 注释：识别细胞类型和marker基因
    """
    print("\n" + "=" * 60)
    print("🧬 练习3: 单细胞聚类分析")
    print("=" * 60)
    
    # TODO: 生成模拟单细胞数据
    # 使用make_blobs创建3个细胞群
    # n_samples=100, n_features=50, centers=3
    np.random.seed(42)
    
    # X, true_labels = make_blobs(...)
    X, true_labels = None, None  # 请完成
    
    # TODO: 模拟基因表达数据特点(对数正态分布)
    # X = np.exp(X)  # 转换为对数正态分布
    
    # 创建基因名称
    gene_names = [f'Gene_{i:02d}' for i in range(1, 51)]
    cell_names = [f'Cell_{i:03d}' for i in range(1, 101)]
    
    # TODO: 创建DataFrame
    df = pd.DataFrame(X, columns=gene_names, index=cell_names)
    
    print("单细胞数据信息:")
    print(f"细胞数量: {df.shape[0]}")
    print(f"基因数量: {df.shape[1]}")
    print(f"表达值范围: [{df.values.min():.2f}, {df.values.max():.2f}]")
    
    # TODO: 数据预处理
    # 1. 对数转换 (log1p)
    # df_log = np.log1p(df)
    
    # 2. 标准化
    # scaler = StandardScaler()
    # df_scaled = scaler.fit_transform(df_log)
    
    # TODO: PCA降维分析
    from sklearn.decomposition import PCA
    
    # pca = PCA(n_components=2)
    # df_pca = pca.fit_transform(df_scaled)
    
    print(f"\nPCA解释方差比: {None}")  # 请完成
    print(f"累计解释方差: {None}")  # 请完成
    
    # TODO: 尝试不同的聚类算法
    from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
    from sklearn.mixture import GaussianMixture
    from sklearn.metrics import silhouette_score, adjusted_rand_score
    
    clustering_methods = {
        'K-Means': KMeans(n_clusters=3, random_state=42),
        'DBSCAN': DBSCAN(eps=0.5, min_samples=5),
        '层次聚类': AgglomerativeClustering(n_clusters=3),
        '高斯混合': GaussianMixture(n_components=3, random_state=42)
    }
    
    clustering_results = {}
    
    # TODO: 执行聚类并评估
    for name, clusterer in clustering_methods.items():
        print(f"\n执行 {name} 聚类...")
        
        # 聚类
        # if name == '高斯混合':
        #     labels = clusterer.fit_predict(df_scaled)
        # else:
        #     labels = clusterer.fit_predict(df_scaled)
        
        labels = None  # 请完成
        
        # 评估指标
        if labels is not None and len(set(labels)) > 1:
            # silhouette = silhouette_score(df_scaled, labels)
            # ari = adjusted_rand_score(true_labels, labels)
            silhouette = None  # 请完成
            ari = None  # 请完成
        else:
            silhouette = -1
            ari = -1
        
        clustering_results[name] = {
            'labels': labels,
            'silhouette': silhouette,
            'ari': ari
        }
        
        print(f"  轮廓系数: {silhouette}")
        print(f"  调整兰德指数: {ari}")
    
    # TODO: 可视化聚类结果
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for idx, (name, result) in enumerate(clustering_results.items()):
        ax = axes[idx]
        labels = result['labels']
        
        if labels is not None:
            # scatter = ax.scatter(df_pca[:, 0], df_pca[:, 1], 
            #                     c=labels, cmap='viridis', alpha=0.6)
            ax.set_title(f'{name}\nSilhouette: {result["silhouette"]:.3f}')
            # plt.colorbar(scatter, ax=ax)
    
    # 真实标签
    ax = axes[4]
    # scatter = ax.scatter(df_pca[:, 0], df_pca[:, 1], 
    #                     c=true_labels, cmap='Set1', alpha=0.6)
    ax.set_title('真实标签')
    # plt.colorbar(scatter, ax=ax)
    
    # 空白
    axes[5].axis('off')
    
    for ax in axes[:5]:
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
    
    plt.tight_layout()
    plt.show()
    
    # TODO: 创建最优聚类的热图
    # 选择轮廓系数最高的聚类方法
    # best_method = max(clustering_results.keys(), 
    #                   key=lambda k: clustering_results[k]['silhouette'])
    # best_labels = clustering_results[best_method]['labels']
    
    print(f"\n最佳聚类方法: {None}")  # 请完成
    
    # TODO: 绘制聚类热图
    # 选择表达变异最大的20个基因
    # gene_std = df.std(axis=0)
    # top_genes = gene_std.nlargest(20).index
    
    plt.figure(figsize=(12, 8))
    # TODO: 创建聚类热图
    # 提示: 按聚类标签排序细胞，然后绘制热图
    plt.title('细胞聚类热图')
    plt.show()
    
    print("✅ 练习3完成！")
    return clustering_results


def exercise_4_model_optimization():
    """
    练习4: 模型评估和优化
    
    背景：
    使用乳腺癌数据集练习模型优化技术：
    - 交叉验证
    - 超参数调优
    - 过拟合检测
    - 特征选择
    
    任务：
    1. 加载数据
    2. 实现交叉验证
    3. 网格搜索优化超参数
    4. 分析过拟合现象
    5. 特征选择
    """
    print("\n" + "=" * 60)
    print("🧬 练习4: 模型评估和优化")
    print("=" * 60)
    
    # TODO: 创建分类数据
    # 使用make_classification创建二分类问题，有一些噪声特征
    np.random.seed(42)
    
    # X, y = make_classification(
    #     n_samples=500, n_features=20, n_informative=10, 
    #     n_redundant=5, n_classes=2, flip_y=0.05, random_state=42
    # )
    X, y = None, None  # 请完成
    
    print("数据信息:")
    print(f"样本数: {X.shape[0] if X is not None else 'None'}")
    print(f"特征数: {X.shape[1] if X is not None else 'None'}")
    print(f"正负样本比例: {np.bincount(y) if y is not None else 'None'}")
    
    # TODO: 数据分割
    # X_train, X_test, y_train, y_test = train_test_split(...)
    
    # TODO: 数据标准化
    # scaler = StandardScaler()
    # X_train_scaled = ...
    # X_test_scaled = ...
    
    # 任务4.1: 交叉验证
    print("\n" + "-" * 40)
    print("任务4.1: 交叉验证")
    print("-" * 40)
    
    from sklearn.model_selection import cross_val_score, StratifiedKFold
    from sklearn.ensemble import RandomForestClassifier
    
    # TODO: 使用5折交叉验证评估随机森林
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # cv_scores = cross_val_score(rf, X_train_scaled, y_train, 
    #                            cv=StratifiedKFold(5), scoring='accuracy')
    cv_scores = None  # 请完成
    
    print(f"交叉验证分数: {cv_scores if cv_scores is not None else 'None'}")
    print(f"平均准确率: {cv_scores.mean() if cv_scores is not None else 'None':.3f} ± {cv_scores.std() if cv_scores is not None else 0:.3f}")
    
    # 任务4.2: 超参数调优
    print("\n" + "-" * 40)
    print("任务4.2: 超参数调优")
    print("-" * 40)
    
    from sklearn.model_selection import GridSearchCV
    
    # TODO: 定义参数网格
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    
    print(f"参数组合总数: {np.prod([len(v) for v in param_grid.values()])}")
    
    # TODO: 网格搜索
    # grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='f1', n_jobs=-1)
    # grid_search.fit(X_train_scaled, y_train)
    
    grid_search = None  # 请完成
    
    print(f"最佳参数: {grid_search.best_params_ if grid_search else 'None'}")
    print(f"最佳CV分数: {grid_search.best_score_ if grid_search else 'None':.3f}")
    
    # 任务4.3: 过拟合分析
    print("\n" + "-" * 40)
    print("任务4.3: 过拟合分析")
    print("-" * 40)
    
    # TODO: 比较不同复杂度模型的训练误差和验证误差
    from sklearn.model_selection import validation_curve
    
    # 以树的深度为例分析过拟合
    # depths = [1, 3, 5, 10, 15, 20, None]
    # train_scores, val_scores = validation_curve(
    #     DecisionTreeClassifier(random_state=42), 
    #     X_train_scaled, y_train,
    #     param_name='max_depth', param_range=depths,
    #     cv=5, scoring='accuracy'
    # )
    
    depths = None  # 请完成
    train_scores = None  # 请完成
    val_scores = None  # 请完成
    
    # TODO: 绘制验证曲线
    if train_scores is not None and val_scores is not None:
        plt.figure(figsize=(10, 6))
        
        # train_mean = train_scores.mean(axis=1)
        # train_std = train_scores.std(axis=1)
        # val_mean = val_scores.mean(axis=1)
        # val_std = val_scores.std(axis=1)
        
        # plt.plot(depths, train_mean, 'o-', label='训练误差', color='blue')
        # plt.fill_between(depths, train_mean-train_std, train_mean+train_std, alpha=0.1, color='blue')
        # plt.plot(depths, val_mean, 'o-', label='验证误差', color='red')
        # plt.fill_between(depths, val_mean-val_std, val_mean+val_std, alpha=0.1, color='red')
        
        plt.xlabel('树的深度')
        plt.ylabel('准确率')
        plt.title('验证曲线 - 过拟合分析')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    # 任务4.4: 特征选择
    print("\n" + "-" * 40)
    print("任务4.4: 特征选择")
    print("-" * 40)
    
    from sklearn.feature_selection import SelectKBest, f_classif
    from sklearn.feature_selection import RFE
    
    # TODO: 使用统计方法选择特征
    # selector = SelectKBest(score_func=f_classif, k=10)
    # X_train_selected = selector.fit_transform(X_train_scaled, y_train)
    # X_test_selected = selector.transform(X_test_scaled)
    
    # selected_features = selector.get_support()
    # print(f"选中的特征索引: {np.where(selected_features)[0]}")
    
    # TODO: 使用递归特征消除
    from sklearn.linear_model import LogisticRegression
    
    # rfe = RFE(LogisticRegression(random_state=42), n_features_to_select=10)
    # rfe.fit(X_train_scaled, y_train)
    
    # print(f"RFE选中的特征: {np.where(rfe.support_)[0]}")
    # print(f"特征排名: {rfe.ranking_}")
    
    # TODO: 比较特征选择前后的性能
    # 使用选择后的特征训练模型并比较性能
    
    print("✅ 练习4完成！")
    return grid_search


def exercise_5_cancer_subtype_project():
    """
    练习5: 综合项目 - 癌症亚型分类
    
    背景：
    这是一个综合性项目，模拟真实的癌症亚型分类任务。
    你需要整合前面学到的所有技术：
    - 数据预处理
    - 特征工程  
    - 模型训练和选择
    - 结果评估和可视化
    
    任务：
    1. 生成模拟的癌症基因表达数据
    2. 完整的数据预处理流程
    3. 特征工程和选择
    4. 训练多个模型并调优
    5. 模型解释和结果可视化
    6. 撰写分析报告
    """
    print("\n" + "=" * 60)
    print("🧬 综合项目: 癌症亚型分类")
    print("=" * 60)
    
    print("""
项目背景:
你是一名生物信息学研究员，需要基于基因表达数据
自动识别乳腺癌的分子亚型：

1. Luminal A - 激素受体阳性，预后较好
2. Luminal B - 激素受体阳性，增殖活跃  
3. HER2+ - HER2扩增，靶向治疗敏感
4. Basal-like - 三阴性，预后较差

你的任务是构建一个准确的分类器，
帮助临床医生进行精准诊断。
    """)
    
    # TODO: 步骤1 - 数据生成和探索
    print("\n" + "-" * 50)
    print("步骤1: 数据生成和探索")
    print("-" * 50)
    
    # 创建4类癌症亚型数据
    np.random.seed(42)
    
    # 模拟4种亚型的基因表达模式
    n_samples_per_class = [120, 100, 80, 100]  # 不平衡数据
    n_genes = 100
    
    # TODO: 为每个亚型创建特异性表达模式
    # 提示: 每个亚型在不同基因上有高表达
    
    all_data = []
    all_labels = []
    
    for subtype_id, n_samples in enumerate(n_samples_per_class):
        # TODO: 创建每个亚型的表达数据
        # 基础表达水平 + 亚型特异性表达 + 噪声
        
        # base_expression = np.random.lognormal(3, 1, (n_samples, n_genes))
        # # 添加亚型特异性表达模式
        # ...
        
        # all_data.append(subtype_expression)
        # all_labels.extend([subtype_id] * n_samples)
        pass
    
    # X = np.vstack(all_data)
    # y = np.array(all_labels)
    X, y = None, None  # 请完成
    
    # 创建特征名称（基因名）
    gene_names = [f'Gene_{i:04d}' for i in range(1, n_genes+1)]
    subtype_names = ['Luminal A', 'Luminal B', 'HER2+', 'Basal-like']
    
    if X is not None and y is not None:
        print(f"数据集大小: {X.shape}")
        print(f"类别分布: {dict(zip(*np.unique(y, return_counts=True)))}")
    
    # TODO: 步骤2 - 数据预处理
    print("\n" + "-" * 50)
    print("步骤2: 数据预处理")
    print("-" * 50)
    
    # 2.1 处理缺失值(模拟一些缺失)
    # 2.2 对数转换处理偏态分布
    # 2.3 标准化
    # 2.4 处理类别不平衡
    
    # TODO: 步骤3 - 探索性数据分析
    print("\n" + "-" * 50)
    print("步骤3: 探索性数据分析") 
    print("-" * 50)
    
    # TODO: 绘制多个可视化图表
    # 3.1 类别分布
    # 3.2 主成分分析可视化
    # 3.3 差异表达基因热图
    # 3.4 特征相关性分析
    
    # TODO: 步骤4 - 特征工程和选择
    print("\n" + "-" * 50)
    print("步骤4: 特征工程和选择")
    print("-" * 50)
    
    # 4.1 单变量特征选择
    # 4.2 递归特征消除
    # 4.3 基于模型的特征重要性
    # 4.4 创建组合特征
    
    # TODO: 步骤5 - 模型训练和优化
    print("\n" + "-" * 50)
    print("步骤5: 模型训练和优化")
    print("-" * 50)
    
    # 5.1 训练多个基础模型
    # 5.2 超参数调优
    # 5.3 集成学习方法
    # 5.4 处理类别不平衡
    
    models_to_try = [
        'LogisticRegression',
        'RandomForest', 
        'SVM',
        'XGBoost',  # 如果可用
        'NeuralNetwork'
    ]
    
    # TODO: 步骤6 - 模型评估
    print("\n" + "-" * 50)
    print("步骤6: 模型评估")
    print("-" * 50)
    
    # 6.1 交叉验证
    # 6.2 多种评估指标
    # 6.3 混淆矩阵
    # 6.4 ROC曲线和AUC
    # 6.5 精确率-召回率曲线
    
    # TODO: 步骤7 - 模型解释
    print("\n" + "-" * 50)
    print("步骤7: 模型解释")
    print("-" * 50)
    
    # 7.1 特征重要性分析
    # 7.2 SHAP值(如果可用)
    # 7.3 错误案例分析
    # 7.4 生物学意义解释
    
    # TODO: 步骤8 - 结果总结和报告
    print("\n" + "-" * 50)
    print("步骤8: 结果总结")
    print("-" * 50)
    
    report = """
    项目总结报告:
    ==============
    
    1. 数据概况:
       - 样本数: {samples}
       - 基因数: {genes}  
       - 亚型数: {subtypes}
       - 类别分布: {distribution}
    
    2. 最佳模型:
       - 算法: {best_algorithm}
       - 准确率: {accuracy:.3f}
       - F1分数: {f1_score:.3f}
       - AUC: {auc:.3f}
    
    3. 关键发现:
       - 最重要的预测基因: {top_genes}
       - 最难区分的亚型组合: {difficult_pairs}
       - 模型的主要局限性: {limitations}
    
    4. 临床意义:
       - 该模型可以辅助{clinical_application}
       - 建议结合{additional_info}进一步验证
       - 下一步研究方向: {future_work}
    
    5. 技术细节:
       - 特征选择方法: {feature_selection}
       - 超参数优化: {hyperparameter_tuning}
       - 交叉验证策略: {cross_validation}
    """.format(
        samples="待完成",
        genes="待完成", 
        subtypes="待完成",
        distribution="待完成",
        best_algorithm="待完成",
        accuracy=0.0,
        f1_score=0.0,
        auc=0.0,
        top_genes="待完成",
        difficult_pairs="待完成", 
        limitations="待完成",
        clinical_application="待完成",
        additional_info="待完成",
        future_work="待完成",
        feature_selection="待完成",
        hyperparameter_tuning="待完成",
        cross_validation="待完成"
    )
    
    print(report)
    
    print("\n✅ 综合项目完成！")
    print("\n" + "=" * 60)
    print("🎉 恭喜你完成了机器学习入门的所有练习！")
    print("=" * 60)
    print("""
你已经掌握了：
✅ 数据预处理和探索性分析
✅ 监督学习分类算法
✅ 无监督学习聚类分析  
✅ 模型评估和优化技术
✅ 特征工程和选择方法
✅ 综合项目实战经验

下一步建议：
🚀 尝试真实的生物数据集
🚀 学习深度学习框架
🚀 探索专业生物信息学工具
🚀 参与开源项目贡献

记住：机器学习是工具，生物学知识是灵魂！
    """)
    
    return report


def main():
    """运行所有练习"""
    print("="*80)
    print("🧬 Chapter 10: 机器学习入门练习 - 循序渐进掌握AI技能")
    print("="*80)
    print("""
📚 学习路径设计：

🔰 练习1: 数据预处理 (基础 ⭐)
   • 掌握数据清洗和预处理的基本技能
   • 理解生物数据的特点和处理方法
   • 为后续建模打下坚实基础

🎯 练习2: 基因功能分类 (进阶 ⭐⭐)
   • 学习监督学习的核心概念
   • 比较不同分类算法的性能
   • 理解生物特征工程的重要性

🔬 练习3: 单细胞聚类分析 (进阶 ⭐⭐)
   • 探索无监督学习的奥秘
   • 发现隐藏的细胞亚型模式
   • 掌握降维和聚类技术

⚖️ 练习4: 模型评估和优化 (高级 ⭐⭐⭐)
   • 深入理解模型评估体系
   • 学会防止过拟合和欠拟合
   • 掌握超参数调优技巧

🏆 练习5: 综合实战项目 (专家 ⭐⭐⭐⭐)
   • 整合所有技能完成真实项目
   • 体验完整的机器学习工作流程
   • 达到独立解决问题的能力

建议：按顺序完成，每个练习都为下一个奠定基础！
    """)
    
    try:
        print("\n" + "="*60)
        print("🚀 开始你的机器学习之旅...")
        print("="*60)
        
        # 练习1: 数据预处理 (基础级)
        print("\n🔰 准备进入练习1: 数据预处理基础...")
        input("按回车键继续 → ")
        exercise_1_data_preprocessing()
        
        # 练习2: 基因功能分类 (进阶级)
        print("\n🎯 准备进入练习2: 监督学习进阶...")
        input("完成练习1后，按回车继续 → ")
        exercise_2_gene_function_classifier()
        
        # 练习3: 单细胞聚类 (进阶级)
        print("\n🔬 准备进入练习3: 无监督学习探索...")
        input("完成练习2后，按回车继续 → ")
        exercise_3_cell_clustering()
        
        # 练习4: 模型优化 (高级)
        print("\n⚖️ 准备进入练习4: 高级模型优化...")
        input("完成练习3后，按回车继续 → ")
        exercise_4_model_optimization()
        
        # 练习5: 综合项目 (专家级)
        print("\n🏆 准备进入练习5: 专家级综合实战...")
        input("完成练习4后，按回车挑战最终项目 → ")
        exercise_5_cancer_subtype_project()
        
        print("\n" + "="*80)
        print("🎉 恭喜！你已完成所有机器学习练习！")
        print("="*80)
        print("""
🏅 成就解锁：
✅ 数据预处理专家
✅ 监督学习实践者 
✅ 无监督学习探索者
✅ 模型优化大师
✅ 综合项目完成者

你现在已经具备了：
🧠 机器学习的理论基础
🛠️ 实际项目的开发能力
🔬 生物数据的分析技能
🎯 解决实际问题的经验

下一步建议：
🚀 尝试真实的生物数据集
📚 深入学习深度学习框架
🌟 参与开源项目贡献
        """)
        
    except KeyboardInterrupt:
        print("\n\n⏸️ 练习已暂停。你可以随时重新开始！")
    except Exception as e:
        print(f"\n❌ 练习过程中遇到错误: {e}")
        print("💡 提示: 请检查代码并完成TODO部分")
        print("🔧 每个练习都有详细的提示和注释帮助你完成")


if __name__ == "__main__":
    main()