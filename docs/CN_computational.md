# COVID-19的GHDDI计算结果


我们将在这一页上持续发表我们的计算药物发现工作，包括基于AI的预测、基于物理的虚拟筛选、分子动力学模拟以及其他化学信息学和生物信息学相关的推论。这一努力是为了促进社区范围内的实验工作。请注意，对于任何数据驱动的方法，预测的解释范围必须与训练集的原始科学范围一致。此外，对于各种类型的预测模型、从训练集或经验参数继承的噪声和偏倚，必须考虑不同数学近似的局限性。因此，这些计算结果必须由有经验的药物化学家和生物学家进一步分析，并最终在任何严格的科学结论之前得到相关湿实验室实验的支持。[基于网络的服务](http://aidd.ghddi.org/covid19/)基于这些预测模型是开放的，便于你自己使用自己的化合物库进行筛选工作。在收集新证据后，模型和结果不断更新。


## 用于COVID-19的GHDDI Web虚拟筛选服务


[我们的网络服务现在可用，可以作为虚拟筛选工具。](http://aidd.ghddi.org/covid19/)




## 药物重复努力


### A.基于配体的AI模型


我们尝试了包含不同病毒种类及其靶标的不同训练集，利用GHDDI自主开发的HAG-net深度学习系统构建了基于靶标特异性或表型的分类AI模型。我们只选择了显示5倍交叉验证AUC > 0.8的模型作为进一步预测实践的验证，结果是综合预测。病毒靶标，包括RDRP、Helicase、SARS-CoV-2的3 C样蛋白酶，表现出相对较高的跨物种保守性，在这项工作中被优先考虑。  作为药物再利用工作的一部分，我们使用这些模型预测GHDDI库存中获批或研究阶段药物分子(~12K)的不同生物活性。随着我们不断改进算法和扩展训练数据，结果将定期更新。




#### 1.异质性抗病毒AI模型


训练数据：使用抗病毒生物活性数据的异质记录，包括来自不同种属和体外试验的基于靶标和基于表型的记录，共有76247种化合物具有37332个活性和38915个非活性分子(至少一种病毒种属的EC50≤100 nM为活性)。
性能(5倍交叉验证)：AUC平均值。= 0.94


* [训练数据SMILES下载中的活性已知药物](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_ViralMix.xlsx )
* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/globalvirus_top200.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/globalvirus_topclusters.csv)


#### 2.表型抗病毒AI模型


训练数据：使用不同种属和体外试验基于表型记录的抗病毒生物活性数据的异质性记录，共有7305种化合物具有3751个活性和3554个非活性分子(至少一种病毒种属的EC50≤100 nM为活性)。
性能(5倍交叉验证)：AUC平均值。= 0.908


* [训练数据SMILES下载中的活性已知药物](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_ViralPhe.xlsx)
* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AntivirusPhe_top200.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AntivirusPhe_topclusters.csv)


#### 3. RNA依赖的RNA聚合酶AI模型


训练数据：使用来自不同物种和体外试验的RNA依赖性RNA聚合酶相关生物活性数据的异质性记录，共有583种化合物，306个活性分子和277个非活性分子(IC50 < = 1 μM为活性)。
性能(5倍交叉验证)：AUC平均值。= 0.952


* [训练数据SMILES下载中的活性已知药物](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_RdRP.xlsx)
* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/RDRP_top200.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/RDRP_topclusters.csv)


#### 4. Helicase AI模型


训练数据：使用来自不同种属和体外试验的Helicase相关生物活性数据的异质性记录，共有878种化合物具有127个活性分子和751个非活性分子(IC50 < = 1 μM为活性分子)。
性能(5倍交叉验证)：AUC平均值。= 0.926


* [训练数据SMILES下载中的活性已知药物](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_helicase.xlsx)
* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/helicase_top200.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/helicase_topclusters.csv)


#### 5.3 C样蛋白酶AI模型


训练数据：使用来自不同种属和体外试验的3 C样蛋白酶相关生物活性数据的异质性记录，共有457种化合物具有132个活性分子和325个非活性分子(IC50 < = 1 μM为活性)。
性能(5倍交叉验证)：AUC平均值。= 0.89


* [训练数据SMILES下载中的活性已知药物](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_3CL.xlsx)
* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_top200.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_topclusters.csv)




### B.基于结构的AI模型


该模型是基于GHDDI开发的HAG-net构建的。该模型是基于所有现有的药物靶标3D信息及其高达200万个分子的相关生化数据进行训练的。该模型适用于所有具有3D结构的目标。使用平均AUC为0.98的DUD.E集和平均AUC为0.8的真负内部基准集对模型性能进行评价，给定目标3D结构、结合口袋的中心坐标(x，y，z)和筛选库SMILES列表作为输入。




#### 1.SARS-CoV-2 RNA依赖性RNA聚合酶(RDRP)(NTP结合位点)


* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/rdrp_stock_top200_2.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/rdrp_stock_clusters_2.csv)


#### 2. SARS-CoV-2螺旋酶(NTP结合位点)


* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/helicase_stock_top200_2.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/helicase_stock_clusters_2.csv)


#### 3. SARS-CoV-2 3 C-样蛋白酶(催化位点)


* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3cl_stock_top200_2.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3cl_stock_clusters_2.csv)


#### 4.SARS-CoV-2木瓜蛋白酶样蛋白酶(催化位点)


* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/plpro_stock_top200_2.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/plpro_stock_clusters_2.csv)


#### 5.人TMPRSS2(催化位点)


* [最高预测活性化合物SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/TMPRSS2_stock_top200_2.csv)
* [预测的活动群集SMILES下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/TMPRSS2_stock_clusters_2.csv)


#### 基准


对于所有上述靶标，使用Autodock Vina over Drugbank发布的5.15版库8764化合物的常规对接结果可以[此处下载](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/vina_dock_all_drugbank515.csv)。在12 CPU上并行筛选每个目标的计算时间约为36小时。


![对接基准](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/docking.jpeg)




### C.基于网络的AI模型


我们根据体外病毒感染试验结果和体内结果，确定了数千种抗病毒化合物和各自的病毒种类可用于检索。此外，我们还基于该数据构建了抗病毒化合物-表型网络AI模型，并预测了这些化合物未检测的抗病毒活性。基于网络的AI模型被提出作为基于GHDDI的HAG-net系统的矩阵完成模型。该模型在19308个子图中进行了训练，子图由二部相互作用网络上的化合物-表型对组成。训练数据集包含6189个活性(IC50<=1 μM)相互作用对和13119个非活性(IC50>1 μM)对。该模型显示4827个测试集化合物-表型关系的AUC为0.95。实验观察和AI预测的抗病毒活性可用于查询，每个化合物-表型关系显示为1(活性)和0(非活性)之间的概率评分。




<br>


上次更新：{{git_revision_date_localized}}
