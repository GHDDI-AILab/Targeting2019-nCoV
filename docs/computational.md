# Computational Efforts for 2019-nCoV

We will continuously publish our computational efforts including AI based prediction, physics-based virtual screening, molecular dynamics simulations, and other cheminformatics and bioinformatics related inferences on this page. This effort is to facilitate community wide experimental effort. Please be noted that for any data-driven approach, the interpretation scope of prediction has to be aligned with the original scientific scope of the training set. In addition, for various type of predictive models, noises and biases inherited from training set or empirical parameters, limitations of different mathematical approximations have to be considered. Therefore, these computational results have to be further analyzed by experienced medicinal chemists and biologists and eventually to be backed up by related wet-lab experiments before any rigorous scientific conclusion. The web-based service based on these predictive models will be open to public soon to facilitate your own screening efforts using your own compound libraries. 

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


###B. Structure based (none-docking) AI model

The structure based AI model was constructed based on GHDDI self developed docking independent advanced deep learning system to achieve exponential computational cost saving (screening 10^5 ligands in minutes) with inherited structural flexibility learned in complex neuron network for structure based virtual screening. The model was trained based on a large collection of existing 3D structure information and their related ligand biochemical data, together up to 1.5 million training samples. The model is universal for all targets with 3D structure available. The model performance on DUD.E set with average AUC = 0.98 (maxAUC=1.0 minAUC=0.83 over 102 targets) for 98 targets and another self collected benchmark set using true inactive ligand as negative samples instead of computational generated decoyed in DUD.E set with average AUC = 0.80 (maxAUC=0.96 minAUC=0.57 over 83 targets). 

Virtual screening efforts have been performed for the following targets of 2019-nCoV (catalytic sites were identified as  inhibition pocket)

#### RNA-dependent RNA polymerase
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_top200.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_topclusters.csv)

#### Helicase 
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_top200.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_topclusters.csv)

#### 3C-like protease
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_top200.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_topclusters.csv)

#### Papain-like protease
* [Top Predicted Active Compounds SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_top200.csv)
* [Predicted Active Clusters SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/3CL_topclusters.csv)

