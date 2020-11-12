#   数据下载




我们正在从我们的大数据平台发布以下数据集。我们正在尽最大努力挖掘之前冠状病毒相关研究的所有实验数据。如果您有其他特定数据需求或需要数据集，请联系我们@[**此处**](https://github.com/GHDDI-AILab/Targeting2019-nCoV/issues)。我们将定期更新我们的数据集，以提供更多信息，帮助您的研究对抗该疾病。




### 广谱抗病毒药物


* 基于体外病毒感染试验结果(EC50≤1 μM)和临床数据(体内活性)，发现了462个分子对至少2种病毒。


    * [完整数据集](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/Antivirus_Drug_Profile_k2.csv)




### 有注释的冠状病毒临床前研究


* 收集了256种与SARS/MERS相关的小分子和生物制剂的1101份体外和体内记录


  * [完整数据集](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/pharmacology_SARS_MERS.xlsx)


### 冠状病毒靶标的无注释临床前研究


* 收集了来自各种来源的479个分子的816条记录。我们目前没有能力注释源或确认所有数据集的正确性。该数据集可能包含缺失值和“脏”数据。请仔细使用数据，并尽自己的努力确认数据源(期刊、专利、网站)，并从数据集中提取有用(信号)信息。一些数据集使用标准值PX =-log[M]。
  * [完整数据集](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AllAssay_coronavirus_all.csv)


* 提取的一些子集：


  * [*PX > 6(测量值 < 1 μM)活动集*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AllAssay_coronavirus_active.csv)


  * [*562个分子的IC50值*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_IC50_for_562_molecules.csv)


  * [*207个分子的Ki抑制常数*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_Ki_inhibition_constant_for_207_molecules.csv)


  * [*153个分子的抑制率*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_inhibition_rate_for_153_molecules.csv)


  * [*30分子的EC50值*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_EC50_for_30_molecules.csv)


  * [*14个分子的pKi值*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_pKi_for_14_molecules.csv)


* 检测了986个分子的冠状病毒SMILES，但我们不确定它们在酶/细胞水平上是有活性的还是无活性的
  * [SMILES](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AllAssay_coronavirus_986_SMILES.csv)




### 既往SARS/MERS的临床工作


* 收集与SARS/MERS相关但无临床结论的临床和临床前药物管道。这些管道大多被停用。


 * 可下载数据集：
    * [正在研发的治疗SARS的药物](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/file_clinicaldrug_sars.csv)
    * [正在进行的MERS治疗药物](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/file_clinicaldrug_mers.csv)
    * [冠状病毒在研药物](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/file_clinicaldrug_cov.csv)




### 文献挖掘


* [Causaly]惠赠的全面文献挖掘结果(https://www.causaly.com)关注化学物质/药物、基因和分子机制。该数据包括2090条关系、1229条聚合关系和976篇文章，基于“Chemicals&Drugs,Genes,Cellular&Molecular Mechanisms[AFFECTING][Genus:Coronavirus]”的检索查询，数据源来自MEDLINE和PubMedCentral。该检索得到了几个目标概念，包括：sars冠状病毒、中东呼吸综合征冠状病毒、人冠状病毒等。
  * [完整数据集](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/Causaly-GHDDI_dataset.xlsx)


下图为关键词关系网络：


![网络图像](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/graph_resized.png)


[完整图像](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/graph_network_causaly.png)


* 聚合关系数据可以在此[数据集]中找到(https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/literature_aggregate_relationships.xlsx)


* 该数据描述了源概念项目，并将其分类为不同的类别。一些相关类别包括：氨基酸肽蛋白、生物活性物质、化学物质、核酸等。


* 文献文章和关系数据提供了977篇相关文章的列表，并显示了来自原始文章的关系证据。


  * [数据集](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/literature_articles_and_relationships.xlsx)


* 文献证据数据列出了所有相关来源概念(生物物质、化学品等)及其与文章的关系。总体而言，有超过2000条与冠状病毒相关的信息。


  * [数据集](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/literature_articles_all.xlsx)




## 用于药物再利用的化合物库。


 * 请访问[Drugbank](https://www.drugbank.ca/)下载最新数据
DrugBank的最新版本(版本5.1.5，发布日期2020-01-03)包含13,490个药物条目，包括2,636种获批的小分子药物、1,365种获批的生物制剂(蛋白质、肽、疫苗和过敏原)、131种营养保健品和超过6,350种实验性(发现阶段)药物。此外，5,191个非冗余蛋白(即药物靶标/酶/转运蛋白/载体)序列与这些药物条目相关联。每个条目包含200多个数据字段，一半信息用于药物/化学数据，另一半用于药物靶标或蛋白质数据。


 * [Selleck库](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/selleck_libraries.zip)
该zip档案包含由[selleck.cn](https://www.selleck.cn/)用于药物再利用。


 * [CAS COVID-19抗病毒候选化合物数据集](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/antiviral_with_properties.sdf)


上次更新：{{git_revision_date_localized}}


<br>
<br>


您的[**反馈**](https://github.com/GHDDI-AILab/Targeting2019-nCoV/issues)受到高度赞赏。
