# GHDDI Computational Effort for COVID-19

We will continuously publish our computational drug discovery efforts including AI-based prediction, physics-based virtual screening, molecular dynamics simulations, and other cheminformatics and bioinformatics related inferences on this page. This effort is to facilitate community wide experimental effort. Please be noted that for any data-driven approach, the interpretation scope of prediction has to be aligned with the original scientific scope of the training set. In addition, for various type of predictive models, noises and biases inherited from training set or empirical parameters, limitations of different mathematical approximations have to be considered. Therefore, these computational results have to be further analyzed by experienced medicinal chemists and biologists and eventually to be backed up by related wet-lab experiments before any rigorous scientific conclusion. The [web-based service](http://aidd.ghddi.org/covid19/) based on these predictive models is open to facilitate your own screening efforts using your own compound libraries. The models and results are constantly updated upon the collection of new evidence. 

## GHDDI Web Virtual Screening Service for COVID-19

[Our web service is now available and can be used as a virtual screening tool.](http://aidd.ghddi.org/covid19/)


## Drug Repurposing Effort 

### A. Ligand based AI models

We have tried different training sets containing different virus species and their targets to build target specific or phenotype based classification AI models using GHDDI self-developed HAG-net deep learning system. We only selected models showing 5-fold cross-validation AUC>0.8 as qualification for further predictive practice and the results are ensemble predictions. Viral targets, including RDRP, Helicase, 3C-like protease of SARS-CoV-2 showing relatively higher cross-species conservation are prioritized in this effort.  We use these models to predict different bioactivities of approved or investigational stage drug molecules (~12K) in GHDDI stock as part of the drug repurposing effort. As we are constantly improving our algorithm and expanding our training data, the results will be updated periodically. 


#### 1. Heterogeneous antiviral AI model

Training Data: Using heterogeneous records of antiviral bioactivity data including target based and phenotype based records from various species and in vitro assays, a total of 76247 compounds with 37332 active and 38915 inactive molecules (EC50 <=100nM for at least one viral species as active). 
Performance (5-fold cross-validation): AUC avg. = 0.94

* [Active Known Drugs in Training data SMILES Download](file/AKD_ViralMix.xlsx )
* [Top Predicted Active Compounds SMILES Download](file/globalvirus_top200.csv)
* [Predicted Active clusters SMILES Download](file/globalvirus_topclusters.csv)

#### 2. Phenotypic antiviral AI model

Training Data: Using heterogeneous records of antiviral bioactivity data of phenotype based records from various species and in vitro assays, a total of 7305 compounds with 3751 active and 3554 inactive molecules (EC50 <=100nM for at least one viral species as active). 
Performance (5-fold cross-validation): AUC avg. = 0.908

* [Active Known Drugs in Training data SMILES Download](file/AKD_ViralPhe.xlsx)
* [Top Predicted Active Compounds SMILES Download](file/AntivirusPhe_top200.csv)
* [Predicted Active Clusters SMILES Download](file/AntivirusPhe_topclusters.csv)

#### 3. RNA-dependent RNA polymerase AI model

Training Data: Using heterogeneous records of RNA-dependent RNA polymerase related bioactivity data from various species and in vitro assays, a total of 583 compounds with 306 active and 277 inactive molecules (IC50 <=1μM as active).  
Performance (5-fold cross-validation): AUC avg. = 0.952

* [Active Known Drugs in Training data SMILES Download](file/AKD_RdRP.xlsx)
* [Top Predicted Active Compounds SMILES Download](file/RDRP_top200.csv)
* [Predicted Active Clusters SMILES Download](file/RDRP_topclusters.csv)

#### 4. Helicase AI model

Training Data: Using heterogeneous records of Helicase related bioactivity data from various species and in vitro assays, a total of 878 compounds with 127 active and 751 inactive molecules (IC50 <=1μM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.926

* [Active Known Drugs in Training data SMILES Download](file/AKD_helicase.xlsx)
* [Top Predicted Active Compounds SMILES Download](file/helicase_top200.csv)
* [Predicted Active Clusters SMILES Download](file/helicase_topclusters.csv)

#### 5. 3C-like protease AI model 

Training Data: Using heterogeneous records of 3C-like protease related bioactivity data from various species and in vitro assays, a total of 457 compounds with 132 active and 325 inactive molecules (IC50 <=1μM as active). 
Performance (5-fold cross-validation): AUC avg. = 0.89 

* [Active Known Drugs in Training data SMILES Download](file/AKD_3CL.xlsx)
* [Top Predicted Active Compounds SMILES Download](file/3CL_top200.csv)
* [Predicted Active Clusters SMILES Download](file/3CL_topclusters.csv)


### B. Structure based AI model

This model was constructed based on GHDDI developed HAG-net. The model was trained based on all existing drug targets 3D information and their related biochemical data for up to 2 million molecules. The model is universal for all targets with 3D structures. The model performance is evaluated using DUD.E set with average AUC of 0.98 and true negative internal benchmark set with average AUC of 0.8. Given a target 3D structure, the center coordinate(x, y, z) of the binding pocket, and screening library SMILES list as input. 


#### 1. SARS-CoV-2 RNA-dependent RNA polymerase(RDRP) (NTP binding site)  

* [Top Predicted Active Compounds SMILES Download](file/rdrp_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](file/rdrp_stock_clusters_2.csv)

#### 2. SARS-CoV-2 Helicase (NTP binding site) 

* [Top Predicted Active Compounds SMILES Download](file/helicase_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](file/helicase_stock_clusters_2.csv)

#### 3. SARS-CoV-2 3C-like protease (catalytic site) 

* [Top Predicted Active Compounds SMILES Download](file/3cl_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](file/3cl_stock_clusters_2.csv)

#### 4. SARS-CoV-2 Papain-like protease (catalytic site)  

* [Top Predicted Active Compounds SMILES Download](file/plpro_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](file/plpro_stock_clusters_2.csv)

#### 5. Human TMPRSS2 (catalytic site)

* [Top Predicted Active Compounds SMILES Download](file/TMPRSS2_stock_top200_2.csv)
* [Predicted Active Clusters SMILES Download](file/TMPRSS2_stock_clusters_2.csv)

#### Benchmark

Conventional Docking results using Autodock Vina over Drugbank released version 5.15 library 8764 compounds for all above targets can be [download here](file/vina_dock_all_drugbank515.csv). Computational time for screening each target is about ~36 hours on 12 CPU in parallel. 

![Docking benchmark](file/docking.jpeg)


### C. Network based AI model 

We have curated thousands of antiviral compounds and respective virus species available for search based on in vitro viral infection assay results and in vivo results. In addition, we have constructed an antiviral compound-phenotype network AI model based on this data and predicted untested antiviral activities of these compounds. The network based AI model was proposed as a matrix completion model based on GHDDI’s HAG-net system. The model was trained over 19308 subgraphs made up of compound-phenotype pairs on the bipartite interaction network. The training dataset contains 7,737 active (IC50<=1uM) and 16,398 inactive (IC50>1uM) interactions. The model shows an AUC of 0.95 over 4827 testing set compound-phenotype relations. The experimentally observed and AI predicted antiviral activities are available to query, and each compound-phenotype relation is shown as a probability score between 1 (active) and 0 (inactive).

More details about this work can be found [here](https://arxiv.org/abs/2102.01649).


{[English](https://ghddi-ailab.github.io/Targeting2019-nCoV/computational/), [中文](https://ghddi-ailab.github.io/Targeting2019-nCoV/CN_computational/)}

<br>

Last update: {{ git_revision_date_localized }}
