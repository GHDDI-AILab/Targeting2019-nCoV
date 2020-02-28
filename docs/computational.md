## Computational Efforts for 2019nCoV

We are here to publish our initial computational efforts including AI based prediction, physics-based virtual screening, molecular dynamics simulations and other chemoinformatics and bioinformatics related inferences. Please be noted that due to uncertainty of various predictive models. Computational results have to be backed up by related wet-lab experiments before any scientific conclusion to be reached.

### Drug Repurposing 

We have tried different training sets containing different organisms and their targets to build target specific or phenopytic based predictive classification models. We only selected models AUC>0.9 for as qualified model for further prediction. We use these models to predict drugbank(version5.1.5) 8773 drugs (approved or investigational stage) as part of the repurposing effort. 
 
1. Ligand based RNA-dependent RNA polymerase AI model
Training Data: Using heterogeneous records of RNA polymerase (including ) bioactivity data from various species and in vitro assays, a total of 564 data points with 47 active and 517 inactive molecules (IC50 <=100nM as active). 

2. Ligand based antiviral AI model
Training Data: Using heterogeneous records of 3C-like protease bioactivity data from various species and in vitro assays, a total of 76247 data points with 37332 active and 38915 inactive molecules (IC50 <=100nM as active). 

3. Structure based virtual screening for 3C-Like protease using AI model






