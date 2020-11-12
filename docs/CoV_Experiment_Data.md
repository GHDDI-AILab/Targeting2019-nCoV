#  Data Download 


We are releasing the following datasets from our big data platform. We are making our best efforts to mine all experimental data of previous coronavirus related studies. If you have other specific data need or have datasets to contribute, please contact us @[**here**](https://github.com/GHDDI-AILab/Targeting2019-nCoV/issues). We will update our datasets periodically to provide more information to help your research combat the disease. 


### Broad-spectrum antiviral agents

* Based on in vitro viral infection assay results (EC50<=1uM) and clinical data (in vivo active), 462 molecules were found against at least 2 virus species. 

    * [Full Dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/Antivirus_Drug_Profile_k2.csv)


### Annotated preclinical studies on coronavirus

* A collection of 1101 in vitro and in vivo records for 256 small molecules and biologics related to SARS/MERS 

  * [Full dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/pharmacology_SARS_MERS.xlsx)

### Unannotated preclinical studies on coronavirus targets

* A collection of 816 records for 479 molecules from various sources. We currently don't have the capability to annotate the sources or confirm the correctness of all datasets. This dataset may contains missing values and "dirty" data. Please use the data carefully and make your own effort to confirm the data source (journals, patents, websites) and extract useful (signal) information from the set. Some datasets use standardized value PX=-log[M].   
  * [Full dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AllAssay_coronavirus_all.csv)

* Some subsets extracted:

  * [*PX>6(measurement <1uM) active set*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AllAssay_coronavirus_active.csv)

  * [*IC50 values for 562 molecules*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_IC50_for_562_molecules.csv)

  * [*Ki inhibition constant for 207 molecules*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_Ki_inhibition_constant_for_207_molecules.csv)

  * [*Inhibition rate for 153 molecules*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_inhibition_rate_for_153_molecules.csv)

  * [*EC50 values for 30 molecules*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_EC50_for_30_molecules.csv)

  * [*pKi values for 14 molecules*](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/coronavirus_pKi_for_14_molecules.csv)

* SMILES of 986 molecules tested for coronavirus, but we are not sure if they are active or inactive at enzymatic/cellular level 
  * [SMILES](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/AllAssay_coronavirus_986_SMILES.csv)
  
  
### Previous clinical effort for SARS/MERS 

* A collection of clinical and preclinical drug pipelines related to SARS/MERS, but without clinical conclusion. Most of these pipelines are deactivated.  

 * Downloadable datasets: 
    * [Drugs in pipeline for SARS](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/file_clinicaldrug_sars.csv)
    * [Drugs in pipeline for MERS](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/file_clinicaldrug_mers.csv)
    * [Drugs in pipeline for Coronavirus](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/file_clinicaldrug_cov.csv)


### Literature Mining

* A comprehensive literature mining result kindly provided by [Causaly](https://www.causaly.com), focusing on chemicals/drugs, genes and molecular mechanisms. This data includes 2090 relationships, 1229 aggregrate relationships, and 976 articles based on a search query of "Chemicals&Drugs,Genes,Cellular&Molecular Mechanisms [AFFECTING] [Genus:Coronavirus]" with the data source coming from MEDLINE and PubMedCentral. This search resulted in several Target Concepts including: sars coronavirus, middle east respiratory syndrome coronavirus, human coronavirus, etc.
  * [Full dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/Causaly-GHDDI_dataset.xlsx)

The following figure is the keyword relationship network: 

![Image of network](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/graph_resized.png)

[Full Image](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/graph_network_causaly.png)

* The aggregate relationship data can be found in this [dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/literature_aggregate_relationships.xlsx)

* This data describes source concept items and classifies them into different categories. Some relevant categories include: Amino Acid Peptide Protein, Biologically Active Substance, Chemical, Nucleic Acid, etc.

* Literature articles and relationships data gives a list of 977 relevant articles and shows the evidence of the relationship from the original article.

  * [Dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/literature_articles_and_relationships.xlsx)

* Literature evidence data lists all relevant source concepts (biological substances, chemicals, etc) and its relation to an article. Overall, there are over 2000 relevant pieces of information relevant to coronavirus. 

  * [Dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/literature_articles_all.xlsx)


## Compound Libraries for drug repurposing. 

 * Please visit [Drugbank](https://www.drugbank.ca/) to download the most recent data
   The latest release of DrugBank (version 5.1.5, released 2020-01-03) contains 13,490 drug entries including 2,636 approved small molecule drugs, 1,365 approved biologics (proteins, peptides, vaccines, and allergenics), 131 nutraceuticals and over 6,350 experimental (discovery-phase) drugs. Additionally, 5,191 non-redundant protein (i.e. drug target/enzyme/transporter/carrier) sequences are linked to these drug entries. Each entry contains more than 200 data fields with half of the information being devoted to drug/chemical data and the other half devoted to drug target or protein data.
   
 * [Selleck Libraries](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/selleck_libraries.zip) 
   This zip archive contains drug libraries provided by [selleck.cn](https://www.selleck.cn/) to be used for drug repurposing.
   
 * [CAS COVID-19 Antiviral Candidate Compounds Dataset](https://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/antiviral_with_properties.sdf)


{[English](https://ghddi-ailab.github.io/Targeting2019-nCoV/CoV_Experiment_Data/), [Chinese](https://ghddi-ailab.github.io/Targeting2019-nCoV/CN_CoV_Experiment_Data/)}

Last update: {{ git_revision_date_localized }}

<br>
<br>

Your [**feedback**](https://github.com/GHDDI-AILab/Targeting2019-nCoV/issues) is highly appreciated.
