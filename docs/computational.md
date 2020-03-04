## Computational Efforts for 2019nCoV

We are here to publish our initial computational efforts including AI based prediction, physics-based virtual screening, molecular dynamics simulations and other chemoinformatics and bioinformatics related inferences. Please be noted that due to uncertainty of various predictive models. Computational results have to be backed up by related wet-lab experiments before any scientific conclusion to be reached. This effort is to facilitate community wide experimental follow up on specific target specific assay or antiviral screening effort. The predictive models web-based service will be open to public soon to facilitate your own virtual screening efforts for your own compound libraries. 

### Drug Repurposing 

A. Ligand based AI model

We have tried different training sets containing different organisms and their targets to build target specific or phenotype based classification AI models using GHDDI developed GHDDI_HAG-net. We only selected models AUC>0.8 for as qualified model for further prediction. Targets including RDRP, Helicase, 3C-like protease of 2019nCoV showing relatively higher cross-species conservation are prioritized in this effort.  We use these models to predict different bioactivity of approved or investigational stage drugs molecules (~12K) in GHDDI stock  as part of the repurposing effort. 

1. Heterogeneous antiviral AI model
Training Data: Using heterogeneous records of antiviral bioactivity data including target based and phenotype based records from various species and in vitro assays, a total of 76247 data points with 37332 active and 38915 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.934

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)

2. Phenotypic antiviral AI model
Training Data: Using heterogeneous records of antiviral bioactivity data of phenotype based records from various species and in vitro assays, a total of 7187 data points with 37332 active and 38915 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.934

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)

3. RNA-dependent RNA polymerase AI model
Training Data: Using heterogeneous records of RNA-dependent RNA polymerase related bioactivity data from various species and in vitro assays, a total of 564 compounds with 47 active and 517 inactive molecules (IC50 <=100nM as active).  
Performance (5-fold cross-validation): AUC avg. = 0.844 

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)

4. Helicase AI model
Training Data: Using heterogeneous records of Helicase related bioactivity data from various species and in vitro assays, a total of 788 compounds with 42 active and 746 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.868

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)

5. 3C-like protease AI model 
Training Data: Using heterogeneous records of 3C-like protease related bioactivity data from various species and in vitro assays, a total of 457 compounds with 58 active and 399 inactive molecules (IC50 <=100nM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.82 

* [Active Known Drugs SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)
* [Active Prediction SMILES Download](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/)


B. Structure based (none-docking) AI model
The structure based AI model was constructed based on GHDDI developed GHDDI_HAG-net using information of target 3D structures information and their related biochemical data. The model is universal for all targets with 3D structures. The model performance is evaluated using DUD.E set and other benchmark set with average AUC of XXX

6. Network based drug-virus inhibition AI model
Training data: Using the cell-based assay data (10uM as cutoff) and animal model data tested for various virus species, the global drug-virus inhibition knowledge graph was constructed based on 7218 positive links connecting 6651 drugs and 21 virus species.
Performance 10 times 10-fold cross validation: AUC avg. = 0.913
[Predictive results download](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/DVIpredictlist-top10.csv): Top 10 potential drugs were predicted for each virus species, including COVID-19, SARS, and MERS.
The sub-network specific for coronavirus was shown below, with 173 reported links and 30 predicted links.
![Coronavirus Network](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronanet.png)

