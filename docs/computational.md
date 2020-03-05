# Computational Efforts for 2019nCoV

We are here to publish our initial computational efforts including AI based prediction, physics-based virtual screening, molecular dynamics simulations and other cheminformatics and bioinformatics related inferences. Please be noted that due to uncertainty of various predictive models. Computational results have to be backed up by related wet-lab experiments before any scientific conclusion to be reached. This effort is to facilitate community wide experimental follow up on specific target specific assay or antiviral screening effort. The predictive models web-based service will be open to public soon to facilitate your own virtual screening efforts for your own compound libraries. 

## Drug Repurposing 

### A. Ligand based AI model

We have tried different training sets containing different organisms and their targets to build target specific or phenotype based classification AI models using GHDDI developed GHDDI_HAG-net. We only selected models AUC>0.8 as qualified model for further prediction. Targets including RDRP, Helicase, 3C-like protease of 2019nCoV showing relatively higher cross-species conservation are prioritized in this effort.  We use these models to predict different bioactivity of approved or investigational stage drugs molecules (~12K) in GHDDI stock as part of the repurposing effort. 

#### 1. Heterogeneous antiviral AI model
Training Data: Using heterogeneous records of antiviral bioactivity data including target based and phenotype based records from various species and in vitro assays, a total of 76247 data points with 37332 active and 38915 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.934

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_ViralMix.xlsx )
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/x)

#### 2. Phenotypic antiviral AI model
Training Data: Using heterogeneous records of antiviral bioactivity data of phenotype based records from various species and in vitro assays, a total of 7305 compounds with 3751 active and 3554 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_ViralPhe.xlsx)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/x)

#### 3. RNA-dependent RNA polymerase AI model
Training Data: Using heterogeneous records of RNA-dependent RNA polymerase related bioactivity data from various species and in vitro assays, a total of 583 compounds with 60 active and 517 inactive molecules (IC50 <=100nM as active).  
Performance (5-fold cross-validation): AUC avg. = 0.844 

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_RdRP.xlsx)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/x)

#### 4. Helicase AI model
Training Data: Using heterogeneous records of Helicase related bioactivity data from various species and in vitro assays, a total of 788 compounds with 42 active and 746 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.868

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_helicase.xlsx)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/x)

#### 5. 3C-like protease AI model 
Training Data: Using heterogeneous records of 3C-like protease related bioactivity data from various species and in vitro assays, a total of 457 compounds with 58 active and 399 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.82 

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AKD_3CL.xlsx)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/x)


### B. Structure based (none-docking) AI model
The structure based AI model was constructed based on GHDDI developed HAG-net. The model was trained based on all existing drug targets 3D information and their related biochemical data. The model is universal for all targets with 3D structures. The model performance is evaluated using DUD.E set and other benchmark sets with average AUC of XXX.



