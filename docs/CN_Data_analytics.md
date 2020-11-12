# 药物重新定位的GHDDI数据分析


已经进行了全面的数据挖掘和分析工作，以呈现这些具有COVID-19治疗潜力的现有药物列表。分析基于不同的原理包括抗冠状病毒活性、广谱抗病毒活性和RNA依赖性RNA聚合酶(RDRP)等病毒靶标高度保守的抗病毒药物。我们将不断更新这些列表中的新发现。




## 既往冠状病毒相关药物发现记录的数据分析结果




收集先前发表冠状病毒实验结果阳性的候选药物。




| Drug name                     | DrugBank ID                                      | Mechanism of action                                          | Experimental activity                                        | Methods                                               | Measurement | Value    | Unit |
| ----------------------------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------- | ----------- | -------- | ---- |
| Remdesivir                    | [DB14761](https://www.drugbank.ca/drugs/DB14761) | Nucleobindin-1 (NUCB1) Inhibitors                            | Severe acute respiratory syndrome (SARS-CoV) remission/reduction, IN VITRO | Viral replication assay                               | IC-50       | 1.00E-08 | M    |
| Emetine                       | [DB13393](https://www.drugbank.ca/drugs/DB13393) | Platelet-Derived Growth Factor (PDGF) Inhibitors;Signal Transduction Modulators;Angiogenesis Inhibitors | Middle East respiratory syndrome coronavirus (MERS-CoV) remission/reduction, IN VITRO | Cytopathicity assay                                   | IC-50       | 1.50E-07 | M    |
| Nafamostat mesilate           | [DB12598](https://www.drugbank.ca/drugs/DB12598) | Tryptase Inhibitors                                          | Middle East respiratory syndrome coronavirus (MERS-CoV) remission/reduction, IN VITRO | Vero cells (TMPRSS2-expressing) transfected with MERS | IC-50       | 1.00E-09 | M    |
| Alisporivir                   | [DB12139](https://www.drugbank.ca/drugs/DB12139) | P-Glycoprotein (MDR-1; ABCB1) Inhibitors;Cyclophilin Inhibitors | Coronavirus acute respiratory syndrome remission/reduction, IN VITRO | RNA assay                                             | IC-50       | 8.00E-07 | M    |
| Niclosamide                   | [DB06803](https://www.drugbank.ca/drugs/DB06803) | Cytochrome P450 CYP1A2 Inhibitors;Quorum Sensing (Pseudomonas aeruginosa) Inhibitors;Neuropeptide Y4 (NPY Y4) Receptor Positive Allosteric Modulators;Autophagy Inducers;Wnt Signaling Inhibitors | Severe acute respiratory syndrome (SARS-CoV) remission/reduction, IN VITRO | Cytopathicity assay                                   | IC-50       | 1.00E-07 | M    |
| Rupintrivir                   | [DB05102](https://www.drugbank.ca/drugs/DB05102) | HRV 3C Protease Inhibitors                                   | Coronavirus acute respiratory syndrome remission/reduction, IN VITRO | Viral replication assay                               | IC-50       | 3.00E-07 | M    |
| Geldanamycin                  | [DB02424](https://www.drugbank.ca/drugs/DB02424) | Signal Transduction Modulators;Heat Shock Protein 90 (Hsp90) Inhibitors | Severe acute respiratory syndrome (SARS-CoV) remission/reduction, IN VITRO |                                                       | IC-50       | 9.10E-07 | M    |
| Sinefungin                    | [DB01910](https://www.drugbank.ca/drugs/DB01910) | Coactivator Associated Arginine Methyltransferase 1 (CARM1; PRMT4) Inhibitors;Histone-Lysine N-Methyltransferase SETD7 (SET7/9) Inhibitors;Protein-L-Isoaspartate(D-Aspartate) O-Methyltransferase (PCMT1; PIMT) Inhibitors;Epigenetic Modifier Modulators | Replicase Polyprotein 1ab (pp1ab) (SARS) inhibition, IN VITRO |                                                       | IC-50       | 3.83E-07 | M    |
| Mycophenolic acid sodium salt | [DB01024](https://www.drugbank.ca/drugs/DB01024) | Inosine 5'-Monophosphate Dehydrogenase (IMPDH) Inhibitors    | Middle East respiratory syndrome coronavirus (MERS-CoV) remission/reduction, IN VITRO | Cytopathicity assay                                   | IC-50       | 1.70E-07 | M    |
| Mycophenolate mofetil         | [DB00688](https://www.drugbank.ca/drugs/DB00688) | Hydroxycarboxylic Acid Receptor 2 (HCAR2; NIACR1; GPR109A) Agonists;Signal Transduction Modulators;Inosine 5'-Monophosphate Dehydrogenase (IMPDH) Inhibitors | Coronavirus acute respiratory syndrome remission/reduction, IN VITRO | Viral replication assay                               | IC-50       | 2.30E-07 | M    |
| Chloroquine                   | [DB00608](https://www.drugbank.ca/drugs/DB00608) |                                                              | Coronavirus acute respiratory syndrome remission/reduction, IN VITRO |                                                       | IC-50       | 8.00E-10 | M    |
| Gemcitabine hydrochloride     | [DB00441](https://www.drugbank.ca/drugs/DB00441) | Ribonucleoside-Diphosphate Reductase Inhibitors;Pyrimidine Antagonists | Coronavirus acute respiratory syndrome remission/reduction, IN VITRO | Cytopathicity assay                                   | IC-50       | 4.40E-07 | M    |
| Promazine                     | [DB00420](https://www.drugbank.ca/drugs/DB00420) | Signal Transduction Modulators;Dopamine Receptor Antagonists | Coronavirus acute respiratory syndrome remission/reduction, IN VITRO | Cytopathicity assay                                   | MIC         | 1.00E-07 | M    |
| Azithromycin                  | [DB00207](https://www.drugbank.ca/drugs/DB00207) | Nonsense Mutation Suppressors;50S Ribosomal Protein Inhibitors | Middle East respiratory syndrome coronavirus (MERS-CoV) remission/reduction, IN VITRO | Luciferine/luciferase assay                           | IC-50       | 1.00E-07 | M    |
| cyclosporin                   | [DB00091](https://www.drugbank.ca/drugs/DB00091) | Cyclophilin Inhibitors;Mitochondrial Permeability Transition (MPT) Inhibitors | Coronavirus acute respiratory syndrome remission/reduction, IN VITRO | RNA assay                                             | IC-50       | 8.00E-07 | M    |




## 广谱抗病毒数据分析结果




基于体外病毒感染试验结果(EC50≤1 μM)和临床数据(体内活性)，我们确定了51个分子对至少5种病毒。
![顶部51 DVI图](http://ghddiai.oss-cn-zhangjiakou.aliyuncs.com/file/Top51BSAAs.png)




| Drug name | ID | Number of virus species | Virus species list | Discovered MOA |
|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tenofovir | [DB14126](https://www.drugbank.ca/drugs/DB14126) | 15 | FLUAV;HCV;HBV;HSV;ADV;DENV;Parainfluenza virus;RSV;Rhinovirus;CMV;VZV;Xenotropic murine leukemia virus-related virus;HIV-2;HIV-1;HSV 2 | Reverse Transcriptase/Ribonuclease H (HIV-1) Inhibitors;Reverse Transcriptase/Ribonuclease H (Viral) Inhibitors |
| Brincidofovir | [DB12151](https://www.drugbank.ca/drugs/DB12151) | 13 | EBOV;CMV;HSV;VZV;BKV;ADV;JC polyomavirus;EBV;HTLV-1;HPV;HSV 1;VACV;HSV-6 | DNA Polymerase Inhibitors |
| Nitazoxanide | [DB00507](https://www.drugbank.ca/drugs/DB00507) | 13 | FLUAV;FLUBV;HBV;HCV;DENV;RSV;ADV;NoV;RuV;HIV-1;JEV;MERS-CoV;ZIKV | Signal Transduction Modulators;Viral Maturation Inhibitors;Pyruvate Synthase (Pyruvate-Ferredoxin Oxidoreductase; PFOR) (Protozoal) Inhibitors;Myc Proto-Oncogene Protein (c-Myc) Inhibitors;Hemagglutinin (HA) (Viral) Inhibitors;Protein Disulfide-Isomerase A3 (PDIA3) Inhibitors;Viral Fusion Inhibitors;Pyruvate Synthase (Pyruvate-Ferredoxin Oxidoreductase; PFOR) (Bacterial) Inhibitors |
| Mycophenolic acid | [DB01024](https://www.drugbank.ca/drugs/DB01024) | 13 | Avian flu;HCV;FLUBV;Filovirus;FLUAV;MERS-CoV;CoV;WNV ;DENV;ZIKV;RSV;Parainfluenza virus;BKV | Inosine 5'-Monophosphate Dehydrogenase (IMPDH) Inhibitors |
| Tenofovir alafenamide fumarate | [DB09299](https://www.drugbank.ca/drugs/DB09299) | 11 | FLUAV;HCV;HBV;HSV;Parainfluenza virus;ADV;DENV;RSV;Rhinovirus;CMV;VZV | Reverse Transcriptase/Ribonuclease H (HIV-1) Inhibitors;Reverse Transcriptase/Ribonuclease H (Viral) Inhibitors |
| Ribavirin | [DB00811](https://www.drugbank.ca/drugs/DB00811) | 11 | Avian flu;FLUBV;HCV;FLU;FLUAV;RSV;EV;Parainfluenza virus;HSV;HEV;LASV | Inosine 5'-Monophosphate Dehydrogenase (IMPDH) Inhibitors;Equilibrative Nucleoside Transporter ENT1 Inhibitors |
| [(2R,3R,4S,5S)-5-(4-amino-5H-pyrrolo[3,2-d]pyrimidin-7-yl)-3,4-dihydroxypyrrolidin-2-yl]methyl (2S)-2-amino-3-methylbutanoate | [CID: 71761401](https://pubchem.ncbi.nlm.nih.gov/compound/71761401) | 10 | Filovirus;SARS-CoV;FLUAV;FLUBV;Parainfluenza virus;DENV;ADV;Rhinovirus;RSV;WNV | RNA Polymerase Inhibitors |
| Remdesivir | [DB14761](https://www.drugbank.ca/drugs/DB14761) | 10 | MERS-CoV;Filovirus;EBOV;CoV;SARS-CoV;MARV;HCV;RSV;ZIKV;2019nCoV | Nucleobindin-1 (NUCB1) Inhibitors |
| Tilorone hydrochloride | [CID: 33958](https://pubchem.ncbi.nlm.nih.gov/compound/33958) | 10 | CHIKV;CMV;EBOV;HAV;HBV;HCV;HSV 1;MARV;MERS-CoV;WNV | Signal Transduction Modulators;Interferon Inducers |
| Cidofovir | [DB00369](https://www.drugbank.ca/drugs/DB00369) | 10 | CMV;HSV;EBV;VZV;JC polyomavirus;ADV;BKV;HSV 1;HSV 2;HPV | DNA Polymerase Inhibitors |
| PTC299 | [CID: 49787172 ](https://pubchem.ncbi.nlm.nih.gov/compound/49787172 ) | 9 | FLUAV;HCV;PV;Parainfluenza virus;WNV ;RSV;ADV;HSV;DENV | Signal Transduction Modulators;Vascular Endothelial Growth Factor (VEGF) Inhibitors;Angiogenesis Inhibitors |
| (4-chlorophenyl) (1S)-6-chloro-1-[4-[(3S)-3,4-dihydroxybutoxy]phenyl]-1,3,4,9-tetrahydropyrido[3,4-b]indole-2-carboxylate | [CID: 67986080](https://pubchem.ncbi.nlm.nih.gov/compound/67986080) | 8 | FLUAV;PV;ADV;Parainfluenza virus;WNV ;RSV;HSV;DENV | VEGF Expression Inhibitors;Angiogenesis Inhibitors |
| Favipiravir | [DB12466](https://www.drugbank.ca/drugs/DB12466) | 8 | FLUAV;FLUBV;FLUCV;2019nCoV;CCHFV;CHIKV;EBOV;MARV | Viral Polymerase Inhibitors |
| OSU-03012 | [CID: 10027278](https://pubchem.ncbi.nlm.nih.gov/compound/10027278) | 8 | Filovirus;FLUAV;MARV;EBOV;HCV;ZIKV;HSV;DENV | Acetyl-Coenzyme A Synthetase (Fungal) Inhibitors;Signal Transduction Modulators;Heat Shock Protein 90 (Hsp90) Inhibitors;Phosphoinositide Dependent Kinase (PDK) 1 Inhibitors;Serine/Threonine-Protein Kinase PKH2 (Fungal) Inhibitors;Heat Shock Protein 70 (Hsp70) Inhibitors;Apoptosis Inducers |
| valaciclovir | [DB00577](https://www.drugbank.ca/drugs/DB00577) | 7 | HSV;CMV;EBV;HBV;HSV 1;HSV 2;VZV | DNA Polymerase Inhibitors; DNA Directed DNA Polymerase Inhibitors |
| Chloroquine | [DB00608](https://www.drugbank.ca/drugs/DB00608) | 7 | CoV;DENV;HIV-1;CHIKV;EBOV;FLUAV;HCV |  |
| Ciclosporin | [DB00091](https://www.drugbank.ca/drugs/DB00091) | 7 | HCV;FLUBV;CoV;HBV;FLUAV;HIV-1;CMV | Cyclophilin D Inhibitors;Signal Transduction Modulators;Serine/Threonine-Protein Phosphatase 2B (PPP3CC; PP2Bgamma; Calcineurin) Inhibitors;INS Expression Inhibitors |
| Silvestrol | [CID: 11787114](https://pubchem.ncbi.nlm.nih.gov/compound/11787114) | 7 | CoV;HCV;MERS-CoV;EBOV;EBV;HPV;Rhinovirus | Eukaryotic Initiation Factor 4A (eIF4A) Inhibitors;Apoptosis Inducers |
| Sirolimus | [DB00877](https://www.drugbank.ca/drugs/DB00877) | 7 | CMV;HCV;BKV;FLUAV;HIV-1;KSHV;RVFV | CCR5 Expression Inhibitors;Signal Transduction Modulators;Proteasome Inhibitors;Drugs Targeting B-Lymphocyte Antigen CD19;Mammalian Target of Rapamycin (mTOR; FRAP1) Inhibitors |
| Deferiprone | [DB08826](https://www.drugbank.ca/drugs/DB08826) | 7 | CMV;BKV;VZV;JC polyomavirus;HSV;ADV;EBV | Chelating Agents; Cytochrome P450 CYP4F2 Inhibitors; Iron Absorption Inhibitors; Lipoxygenase 5 Inhibitors |
| NITD-008 | [CID: 136896143](https://pubchem.ncbi.nlm.nih.gov/compound/136896143) | 6 | Filovirus;HCV;EV;DENV;ZIKV;WNV | RNA-Directed RNA Polymerase (NS5) (Dengue Virus) Inhibitors |
| Aciclovir | [DB00787](https://www.drugbank.ca/drugs/DB00787) | 6 | HBV;HSV;VZV;EBV;HSV 1;HSV 2 | DNA Polymerase Inhibitors |
| KIN-269 | [CID: 86263464](https://pubchem.ncbi.nlm.nih.gov/compound/86263464) | 6 | FLUAV;CoV;FLUBV;RSV;WNV ;DENV | Interferon Regulatory Factor 3 (IRF-3) Activators |
| (-)-Epigallocatechin gallate | [DB12116](https://www.drugbank.ca/drugs/DB12116) | 6 | ADV;HCV;CMV;HSV;FLUAV;ZIKV | SGLT-1 Inhibitors;Tumor NADH Oxidase (tNOX) Inhibitors;Immune Checkpoint Inhibitors;Viral Attachment Inhibitors;Aromatase Inhibitors;beta-Amyloid (Abeta) Aggregation Inhibitors;VEGFR-2 (FLK-1/KDR) Inhibitors;Efflux Pump (Bacterial) Inhibitors;NF-kappaB (NFKB) Activation Inhibitors;Fatty Acid Synthase (FAS) Inhibitors;Signal Transduction Modulators;Dual-Specificity Tyrosine-(Y)-Phosphorylation Regulated Kinase 1A (DYRK1A) Inhibitors;Proteasome Inhibitors;Indoleamine 2,3-dioxygenase 1 (IDO1; IDO) Inhibitors;beta-Amyloid (Abeta) Protein Neurotoxicity Inhibitors;AP-1 Transcription Factor Complex Inhibitors;Glycoprotein 120 (gp120) Inhibitors;PDGFR Family Inhibitors;beta-Secretase (BACE) Inhibitors;Prolyl Endopeptidase (prolyl oligopeptidase; POP) Inhibitors;Antioxidants;Telomerase Reverse Transcriptase (TERT) Inhibitors;Antiamyloidogenic Agents;Angiogenesis Inhibitors;Serine Protease NS3 (HCV) Inhibitors;Wnt Signaling Inhibitors |
| Sunitinib malate | [DB01268](https://www.drugbank.ca/drugs/DB01268) | 6 | HCV;EBOV;RSV;DENV;ZIKV;WNV | Proto-Oncogene Tyrosine-Protein Kinase Receptor Ret (RET; CDHF12; PTC) Inhibitors;VEGFR-3 (FLT4) Inhibitors;VEGFR-2 (FLK-1/KDR) Inhibitors;Signal Transduction Modulators;PDGFRbeta Inhibitors;KIT (C-KIT) Inhibitors;Leucine-Rich Repeat Kinase 2 (LRRK2; Dardarin) Inhibitors;CSF1R (c-FMS) Inhibitors;Flt3 (FLK2/STK1) Inhibitors;VEGFR-1 (Flt-1) Inhibitors;Angiogenesis Inhibitors |
| Lamivudine | [DB00709](https://www.drugbank.ca/drugs/DB00709) | 6 | HBV;HCV;EV;EBV;HIV-1;HIV-2 | DNA Polymerase Inhibitors;Reverse Transcriptase/Ribonuclease H (HIV-1) Inhibitors;Reverse Transcriptase/Ribonuclease H (Viral) Inhibitors |
| Azithromycin | [DB00207](https://www.drugbank.ca/drugs/DB00207) | 6 | EBOV;SARS-CoV;MERS-CoV;RSV;FLUAV;HIV-1 | Nonsense Mutation Suppressors;50S Ribosomal Protein Inhibitors |
| NHC | [CID: 197020](https://pubchem.ncbi.nlm.nih.gov/compound/197020) | 6 | HCV;Avian flu;SARS-CoV;FLUBV;FLUAV;RSV |  |
| 3-Bromo-3-deazaneplanocin | [CID: 66552950](https://pubchem.ncbi.nlm.nih.gov/compound/66552950) | 6 | FLUAV;FLUBV;Filovirus;EBV;HSV;Parainfluenza virus |  |
| Ganciclovir | [DB01004](https://www.drugbank.ca/drugs/DB01004) | 6 | CoV;HSV;CMV;VZV;EBV;ADV | DNA Polymerase Inhibitors |
| Zidovudine | [DB00495](https://www.drugbank.ca/drugs/DB00495) | 6 | Avian flu;Xenotropic murine leukemia virus-related virus;EBV;EV;HSV;HTLV-1 | P-Glycoprotein (MDR-1; ABCB1) Inhibitors;Breast Cancer-Resistant Protein (BCRP; ABCG2) Inhibitors;Reverse Transcriptase/Ribonuclease H (HIV-1) Inhibitors |
| ABI-1968 | [CID: 135565845](https://pubchem.ncbi.nlm.nih.gov/compound/135565845) | 6 | HBV;HSV;CMV;BKV;HPV;JC polyomavirus |  |
| aUY-11 | [CID: 52914323](https://pubchem.ncbi.nlm.nih.gov/compound/52914323) | 5 | FLU;HCV;FLUAV;CMV;HSV | Viral Fusion Inhibitors |
| Geldanamycin | [DB02424](https://www.drugbank.ca/drugs/DB02424) | 5 | SARS-CoV;HCV;HBV;CMV;HSV | Signal Transduction Modulators;Heat Shock Protein 90 (Hsp90) Inhibitors |
| ODE-(S)HPMPA | [CID: 10031478 ](https://pubchem.ncbi.nlm.nih.gov/compound/10031478 ) | 5 | HCV;HBV;HSV;ADV;CMV |  |
| HDP-PME-cPr-DAP | [CID: 15958371](https://pubchem.ncbi.nlm.nih.gov/compound/15958371) | 5 | HBV;EBV;CMV;VZV;HSV |  |
| Di-O-decanoylcurcumin | [CID: 46866178](https://pubchem.ncbi.nlm.nih.gov/compound/46866178) | 5 | FLUAV;FLUBV;HSV;RSV;Parainfluenza virus |  |
| [(2S,3S,5R)-3-(dimethylamino)-5-(5-methyl-2,4-dioxopyrimidin-1-yl)oxolan-2-yl]methyl (2S)-2-amino-3-phenylpropanoate | [CID: 46933910](https://pubchem.ncbi.nlm.nih.gov/compound/46933910) | 5 | FLUAV;FLUBV;RSV;HSV;Parainfluenza virus |  |
| Erlotinib hydrochloride | [DB00530](https://www.drugbank.ca/drugs/DB00530) | 5 | Filovirus;HCV;RSV;EBOV;DENV | Signal Transduction Modulators;EGFR (HER1; erbB1) Inhibitors |
| NITD-982 | [CID: 53362039](https://pubchem.ncbi.nlm.nih.gov/compound/53362039) | 5 | FLUAV;FLUBV;HCV;DENV;RSV | Dihydroorotate Dehydrogenase (DHODH) Inhibitors |
| Di-O-tryptophanylphenylalaninecurcumin | [CID: 46866177](https://pubchem.ncbi.nlm.nih.gov/compound/46866177) | 5 | FLUAV;FLUBV;RSV;HSV;Parainfluenza virus |  |
| Lycorine | [CID: 72378](https://pubchem.ncbi.nlm.nih.gov/compound/72378) | 5 | CoV;HCV;SARS-CoV;DENV;WNV |  |
| (2S,4R)-4-(1H-Benzimidazol-2-ylsulfanyl)-1-(9H-fluoren-2-ylmethyl)-N-(2-methoxyethyl)pyrrolidine-2-carboxamide | [CID: 56854033](https://pubchem.ncbi.nlm.nih.gov/compound/56854033) | 5 | FLUBV;HCV;FLUAV;DENV;RSV |  |
| Lobucavir | [DB12531](https://www.drugbank.ca/drugs/DB12531) | 5 | HBV;HSV;VZV;CMV;HIV-1 | DNA Polymerase Inhibitors |
| C4-Ethyl-O-gamma-folylcurcumin | [CID: 135934890](https://pubchem.ncbi.nlm.nih.gov/compound/135934890) | 5 | FLUAV;FLUBV;RSV;HSV;Parainfluenza virus |  |
| Lopinavir | [DB01601](https://www.drugbank.ca/drugs/DB01601) | 5 | HIV-1;HIV-2;MERS-CoV;2019nCoV;ZIKV | HIV Protease Inhibitors |
| Gemcitabine hydrochloride | [DB00441](https://www.drugbank.ca/drugs/DB00441) | 5 | FLUAV;CoV;HCV;ZIKV;HSV | Ribonucleoside-Diphosphate Reductase Inhibitors;Pyrimidine Antagonists |
| 4-amino-1-[(2R,4R,5R)-5-azido-3,3-difluoro-4-hydroxy-5-(hydroxymethyl)oxolan-2-yl]pyrimidin-2-one | [CID: 23519651](https://pubchem.ncbi.nlm.nih.gov/compound/23519651) | 5 | Filovirus;EBOV;HCV;RSV;Parainfluenza virus | RNA-Directed RNA Polymerase (NS5B) (HCV) Inhibitors;RNA-Directed RNA Polymerase (Respiratory Syncytial Virus) Inhibitors |
| HPMPA-(S) | [CID: 72253](https://pubchem.ncbi.nlm.nih.gov/compound/72253) | 5 | VZV;HSV;EBV;CMV;ADV |  |
| Oseltamivir | [DB00198](https://www.drugbank.ca/drugs/DB00198) | 5 | FLUAV;FLU;Avian flu;FLUBV;Parainfluenza virus | Neuraminidase (Sialidase) (Influenza Virus) Inhibitors |
| LDC-4297 | [CID: 71730493](https://pubchem.ncbi.nlm.nih.gov/compound/71730493) | 5 | FLUAV;CMV;HSV;VZV;ADV | Signal Transduction Modulators;Cyclin-Dependent Kinase 7 (CDK7) Inhibitors;Apoptosis Inducers |




##   从不同试验中选择的具有RDRP抑制MOA的顶级抗病毒候选药物




| Drug name      | DrugBank ID                                      | Mechanism of action                                          | Experimental activity                                        | Measurement | Value    | Unit |
| -------------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | -------- | ---- |
| Beclabuvir     | [DB12225](https://www.drugbank.ca/drugs/DB12225) | RNA-Dependent RNA Polymerase (NS5B) (HCV) Inhibitors         | Hepatitis C (HCV) remission/reduction, IN VITRO              | IC-50       | 3.00E-09 | M    |
| Remdesivir     | [DB14761](https://www.drugbank.ca/drugs/DB14761) | RNA-Dependent RNA Polymerase Inhibitor                       | Ebola virus disease remission/reduction, IN VITRO            | IC-50       | 1.00E-08 | M    |
| Valopicitabine | [DB13920](https://www.drugbank.ca/drugs/DB13920) | RNA-Dependent RNA Polymerase (NS5B) (HCV) Inhibitors         | Hepatitis C (HCV) remission/reduction, IN VITRO              | IC-50       | 9.00E-08 | M    |
| Mericitabine   | [DB12045](https://www.drugbank.ca/drugs/DB12045) | RNA-Dependent RNA Polymerase (NS5B) (HCV) Inhibitors         | Hepatitis C (HCV) remission/reduction, IN VITRO              | IC-50       | 1.30E-07 | M    |
| Lumicitabine   | [DB14808](https://www.drugbank.ca/drugs/DB14808) | RNA-Dependent RNA Polymerase (Respiratory Syncytial Virus) Inhibitors | Infection, respiratory syncytial virus (RSV) remission/reduction, IN VITRO | IC-50       | 2.60E-07 | M    |
| Sofosbuvir     | [DB08934](https://www.drugbank.ca/drugs/DB08934) | RNA-Dependent RNA Polymerase (NS5B) (HCV) Inhibitors         | Infection, dengue virus remission/reduction, IN VITRO        | IC-90       | 4.00E-07 | M    |
| Adafosbuvir    | [DB14906](https://www.drugbank.ca/drugs/DB14906) | RNA-Dependent RNA Polymerase (NS5B) (HCV) Inhibitors         | Infection, dengue virus remission/reduction, IN VITRO        | IC-50       | 1.10E-06 | M    |
| Balapiravir hydrochloride | [DB12283](https://www.drugbank.ca/drugs/DB12283) | RNA-Dependent RNA Polymerase (NS5B) (HCV) Inhibitors          | Infection, dengue virus remission/reduction, IN VITRO        | IC-50     |1.9E-06  | M    |
| Galidesivir | [DB11676](https://www.drugbank.ca/drugs/DB11676) |RNA-Dependent RNA Polymerase Inhibitors|  Infection, Zika virus remission/reduction, IN VITRO                             | IC-50     | 2.96E-06 | M    |
| Favipiravir   | [DB12466](https://www.drugbank.ca/drugs/DB12466) |RNA-Dependent RNA Polymerase Inhibitors| Infection, rabies virus remission/reduction, IN VITRO                             | MIC       |  4.0E-06   | M    |


* 根据相应试验的最佳IC-50测量值选择的化合物。




<br>


{[English](https://ghddi-ailab.github.io/Targeting2019-nCoV/Data_analytics/), [中文](https://ghddi-ailab.github.io/Targeting2019-nCoV/CN_Data_analytics/)}




上次更新：{{git_revision_date_localized}}
