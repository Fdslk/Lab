---
title: Drug-Target
grammar_cjkRuby: true
---

 - Article name ：drug-target network
type：review article published in the nature journal
Goal：**to understand drug targets in the context of cellular and disease networks**
Works：
1.analyze properties of drug-target networks as part of cellular networks
2.Assess retrospectively and prospectively network-based relationships between drugs and their targets, quantitying ongoing trends and shifts in drug discovery
3.Quantify interrelationships between drug targets and disease-gene products.
 - main database: DrugBank database 
 	 database link: https://www.drugbank.ca/public_users/confirmations/wait
 - drug target network target 在这里主要指的是protein;in the drug network, nodes represent drugs, and two drugs are connected to each other if they share at least one target protein.
 - secend network in the complementary 'target-protein network',nodes are ptotein, and two proteins are connected if they are both targeted by at least one common drug.
 - drug targest and human disease gene:
	 A map of disorder-disease gene association in the OMIM Morbid Map was generated recently.Similarly to the TP network was generated from the human disease map, where tewo genes network was generated from the human disease map, where two genes are connected if they are associated with the same disease.
	
 6.Cellular network-based relationships between drug targets and disease genes
 7.The increase in new drug targets has been relatively slow in the aftermath of the sequencing of the human genome.Palliative drugs target proteins that are not the actual cause of the disease, but whose activity can be perturbed to counteract the symptoms of disease-causing proteins.
 - We examined etiologucal and palliative drugs in the DT network by quanitying the relations between drug targets and disease-gene products in the human PPI set.
 - Discussion the concepts of network biology to i==ntegrate data from DrugBank== and ==OMIM with information on gene expression and PPIs==, allowing us to address three questions regarding drug developemt.

main method:

 - Drug databases : DrugBank database combines detailed drug data(chemical, pharmacological and pharmaceutical) with cemprehensive drug-target infomation(primary squence, three-dimensional structure and pathway involvement),
 - OMIM database and diseaseome map. contains the most complete known disorder-gene associations.The human Diseasome Network was constructed by linking disorders to genes if mutations in a gene are implicated in formation of a disorder.
 - Topological features of a networks. The degree of a node is the number of edges connecting to the node.The giant component' is the largest connected component of the network.The clustering coeffient' is defined as ![enter description here][1], where n denotes the number of direct links connecting the ki nearest neighbors of the center of a fully interlinked cluster.If the clustering coefficient is close to 0, then the node is part of a loosely connected group.The average of Ci over all nodes of a network assesses network modularity.
 - Randomization of drug-drug protein associations.
 - Time stamping the drugs : http://www.accessdata.fda.gov/scripts/cder/drugsatfda/
 - protein-protein interaction data: The gaint component of the PPI network contains 7279 proteins, of which 253 are targets of approved drugs and 1159 are associated with diseases.
 - Gene expression microarray data.There were 293 approved drug targets and 808 of all drug targets that have expression information.
 - Tp network and disease-gene relations on PPI we mapped drugs to diseases by searching for disease keywords in the indications field of drug infomation obtained from the ==DrugBank database==, first automatically and then by validating resulting associations manually.For each drug-disease pair, ==we calculated the minimum distance on the PPI map between pairs of target proteins and disease-associated proteins from PPIs==
 - statistical tests:All the t-test were done in mathematica(Wolfram Reserach)using the ==HypothesisTest package==
	
according to this paper, I could draw a conclusion that the main target of the drug are the proteins, especially the diseased-associated proteins.And then based on the mathmatical method to calculate the nuknown connection between the drug and the targets. 


  [1]: ./images/1517132534506.jpg