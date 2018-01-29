---
title: Drug-Target
grammar_cjkRuby: true
---

 - Article name ：**==drug-target network==**
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

 - article name **==Drug Target Protein-Protein Interaction networks:A Systematic perspective==**
	 - type: method article published by the BioMed Research International
	 - main ways: According to some special topological structures of the drug targets, there are significant differences between known targets and other proteins.(**intermediaries, source, of the drug stimulus, and special topological features**)
	 - ==exsiting method to predict drug target==:
		 - build a bipartite graph composed of US food and Drug Administration-approved drugs and proteins linked by drug target binnary associations.
		 - using the chemical 2D structural similarity
			 - ==Relating protein pharmacology by ligand chemistry #768000==
		 - using the phenotypic side-effect similarities
			 - ==Drug target identifcation using side-eﬀect similarity #768000==
		 - topographical analysis of the complex network of intercellular protein interactions may also lead to new avenues for targets prediction.
	- data resource: PPI Database  HPRD, IntAct, BoGRID,MINT, and DIP.
		- ==there is a question that how we can find the target protein data in the DrugBank #801e00==
	- ==related software==:
		- pepstats, an online software from EMBOSS to calculate statistics of protein properties.(then all proteins which belong to the dataset will have 39 chemical and physical properties).

![data resources][2]

 - Discussion:
	 - (1)the intermediaries which play an important role on interactions of the drug targets network
	 - (2)the sources which convert drug stimulus into the desirable therapeutic effects and spread to other proteins
	 - (3)the proteins which have special topological and functional significance
	 
- conclusions:
	- (1) the drug targets have special topological structures that are different with normal proteins(==these special topological structures may help drug targets to respond to drug stimulus==).
	- (2)drugs usually have a high centrality value in the drug-therapy network and act on multiple molecular targets in the human system.
- novol point in this paper, taking the eccentricity, Modularity and Coreness into consideration.
	- eccentricity(离心率)
		- 指定一个距离，所谓的距离就是两个顶点之间的所连接彼此的边的数目，离心率就是在这些距离中取最大的那个距离，也就是边数最多的那个，![][3]
		- the eccentricity shows the easiness of a protein to be functionally reached by all other proteins in the network.That means a protein with low eccentricity is subject to a more stringent or complex regulation so that it could easily influence seveal other proteins.
	- Modularity(模板)
		- the degree to which the components of the network may be separated and recombined.就是将蛋白质分成两个group/community
	- Coreness(核数)


  [1]: ./images/1517132534506.jpg
  [2]: ./images/1517193498490.jpg
  [3]: ./images/1517217530206.jpg