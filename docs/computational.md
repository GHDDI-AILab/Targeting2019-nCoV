# Computational Efforts for 2019-nCoV

We will continuously publish our computational efforts including AI based prediction, physics-based virtual screening, molecular dynamics simulations, and other cheminformatics and bioinformatics related inferences on this page. This effort is to facilitate community wide experimental effort. Please be noted that for any data-driven approach, the interpretation scope of prediction has to be aligned with the original scientific scope of the training set. In addition, for various type of predictive models, noises and biases inherited from training set or empirical parameters, limitations of different mathematical approximations have to be considered. Therefore, these computational results have to be further analyzed by experienced medicinal chemists and biologists and eventually to be backed up by related wet-lab experiments before any rigorous scientific conclusion. The web-based service based on these predictive models will be open to public soon to facilitate your own screening efforts using your own compound libraries. The models and results are constantly updated upon the collection of new evidence. 

## Drug Repurposing Effort 

### A. Ligand based AI models

We have tried different training sets containing different virus species and their targets to build target specific or phenotype based classification AI models using GHDDI self-developed HAG-net deep learning system. We only selected models showing 5-fold cross-validation AUC>0.8 as qualification for further predictive practice and the results are ensemble predictions. Viral targets, including RDRP, Helicase, 3C-like protease of 2019nCoV showing relatively higher cross-species conservation are prioritized in this effort.  We use these models to predict different bioactivities of approved or investigational stage drug molecules (~12K) in GHDDI stock as part of the drug repurposing effort. As we are constantly improving our algorithm and expand our training data, the results will be updated periodically. 


#### 1. Heterogeneous antiviral AI model
Training Data: Using heterogeneous records of antiviral bioactivity data including target based and phenotype based records from various species and in vitro assays, a total of 76247 compounds with 37332 active and 38915 inactive molecules (EC50 <=100nM for at least one viral species as active). 
Performance (5-fold cross-validation): AUC avg. = 0.94

* [Active Known Drugs in Training data SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_ViralMix.xlsx )
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/globalvirus_top200.csv)
* [Predicted Active clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/globalvirus_topclusters.csv)

#### 2. Phenotypic antiviral AI model
Training Data: Using heterogeneous records of antiviral bioactivity data of phenotype based records from various species and in vitro assays, a total of 7305 compounds with 3751 active and 3554 inactive molecules (EC50 <=100nM for at least one viral species as active). 
Performance (5-fold cross-validation): AUC avg. = 0.90 

* [Active Known Drugs in Training data SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_ViralPhe.xlsx)
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AntivirusPhe_top200.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AntivirusPhe_topclusters.csv)

#### 3. RNA-dependent RNA polymerase AI model
Training Data: Using heterogeneous records of RNA-dependent RNA polymerase related bioactivity data from various species and in vitro assays, a total of 583 compounds with 60 active and 517 inactive molecules (IC50 <=100nM as active).  
Performance (5-fold cross-validation): AUC avg. = 0.898 

* [Active Known Drugs in Training data SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_RdRP.xlsx)
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/RDRP_top200.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/RDRP_topclusters.csv)

#### 4. Helicase AI model
Training Data: Using heterogeneous records of Helicase related bioactivity data from various species and in vitro assays, a total of 788 compounds with 42 active and 746 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.868

* [Active Known Drugs in Training data SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_helicase.xlsx)
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/helicase_top200.csv)
* Predicted Active Clusters: Due to a small number of active compounds, there were no significant clusters identified.

#### 5. 3C-like protease AI model 
Training Data: Using heterogeneous records of 3C-like protease related bioactivity data from various species and in vitro assays, a total of 457 compounds with 58 active and 399 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.832 

* [Active Known Drugs in Training data SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_3CL.xlsx)
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_top200.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_topclusters.csv)


### B. Structure based (none-docking) AI model
The structure based AI model was constructed based on GHDDI developed HAG-net. The model was trained based on all existing drug targets 3D information and their related biochemical data for up to 2 million molecules. The model is universal for all targets with 3D structures. The model performance is evaluated using DUD.E set with average AUC of 0.98 and true negative internal benchmark set with average AUC of 0.8. Given a target 3D structure, the center coordinate(x, y, z) of the binding pocket, and screening library SMILES list as input, we are able to screen every 10K compounds in 4 min, which is exponentially faster than traditional docking screening methods. This is a beta testing version of this model, the results will be constantly updated after model upgrade. Here is the sample prediction results for various targets of nCoV-SARS-2.

#### 1. RNA-dependent RNA polymerase(RDRP) (NTP binding site)  
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/rdrp_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/rdrp_stock_clusters_2.csv)

#### 2. Helicase (NTP binding site) 
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/helicase_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/helicase_stock_clusters_2.csv)

#### 3. 3C-like protease (catalytic site) 
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3cl_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3cl_stock_clusters_2.csv)

#### 4. Papain-like protease (catalytic site)  
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/plpro_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/plpro_stock_clusters_2.csv)

