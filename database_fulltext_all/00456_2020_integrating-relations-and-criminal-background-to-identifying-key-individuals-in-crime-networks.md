---
otero_id: 456
otero_key: "5Z8MK2QG"
title: "Integrating relations and criminal background to identifying key individuals in crime networks"
authors: "Fredy Troncoso; Richard Weber"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113405"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating relations and criminal background to identifying key individuals in crime networks

Fredy Troncoso<sup>a,⁎</sup>, Richard Weber<sup>b</sup>

<sup>a</sup> Departamento de Ingeniería Industrial, Facultad de Ingeniería, Universidad del Bío- Bío, Concepción, Chile

<sup>b</sup> Departamento de Ingeniería Industrial, Facultad de Ciencias Físicas y Matemáticas, Universidad de Chile, Santiago, Chile

## A R T I C L E I N F O

Keywords: Crime analytics Criminal groups Social networks Node evaluation Human and social capital Field theory

## A B S T R A C T

One of the most common methods used in the social network analysis of criminal groups is node importance evaluation, which focuses on the links between network members to identify likely crime suspects. Because such traditional node evaluators do not take full advantage of group members' individual criminal propensities, a new evaluator called the social network criminal suspect evaluator (SNCSE) is proposed. SNCSE incorporates members' individual criminal propensities into the node importance evaluation and employs a novel perspective based on concepts of human and social capital, an ego network structure, and an analogy between social interaction and field theory. SNCSE is applied to solve two real-world problems. Its efectiveness is compared with that of traditional evaluators. The results show that integrating criminal propensity into network analysis enables the more accurate identification of key suspects compared to alternative evaluators.

## 1. Introduction

Investigating individual and group criminality requires large quantities of resources and demands ever greater amounts of domain knowledge, skills, expertise, and time as criminal behavior becomes more sophisticated [35]. One way of increasing the eficiency and efectiveness of investigative work would be to improve the identification of individual suspects for any given crime. This would enable authorities responsible for public safety and crime prevention to better focus their scarce resources on the most likely candidates and drop their pursuit of the least likely candidates. The benefits could be particularly significant in cases where the initial population of possible suspects is large.

Criminal groups can be understood as social networks, implying that the traditional social network analysis (SNA) can be successfully used for their investigation. SNA extracts information from social net works using techniques such as node importance evaluation to identify key individuals and identify, for example, members of criminal groups. In traditional and non-traditional [36] [31] social network methods, the links between nodes are the main elements for analysis. However, additional information often exists on each member's propensity to commit certain types of ofenses. The incorporation of this information in the techniques for the analysis of social networks could significantly enhance the efectiveness of investigative work [29]. The present study proposes a new approach for node evaluation that incorporates the criminal propensities of individual network members into the SNA of criminal groups. The study considers these propensities as well as links between nodes, generating results that provide better support for in vestigative work, particularly in criminal group analysis.

Section 2 of this article reviews the literature regarding applications of the social network approach to criminal group analysis, the tools this analysis traditionally uses, and the need for a new node importance evaluator that incorporates the criminal propensity of network members. Section 3 develops the newly proposed evaluator, discusses its theoretical basis, lays out the conditions for its application, and shows an example of its application. Section 4 applies the evaluator to two real-world datasets, showing its efectiveness. Finally, Section 5 presents the conclusions of this study and suggestions for future research.

## 2. Background

According to Wasserman [33], a social network can be defined as a set of nodes linked among each others, thus building pattern of relationships. Groups of criminals can be modeled by such networks where each ofender is represented by a node and connections among them are displayed by arcs allowing the exchange of physical and/or non-physical resources [20]. Understanding criminals as part of a network rather than as individual units, opens a new perspective for crime investigation, at least for those kinds of delinquency that require the participation of various actors [18]. Using social network analysis (SNA) to analyze and explain the criminal group phenomenon is eficient and efective because the group members are involved in a process of social networking, both for the provisioning of illicit goods and services and the protection, regulation, and extortion of those involved in their provision and consumption [20].

Analyzing criminal groups in a social network context generally aims to identify criminal structures and/or key individuals based on the links between them. To this end, information from databases both public and private is utilized. The use of social network analysis to extract criminal intelligence has been used since 1991 [28] and widely employed, especially on published databases of terrorist groups since the attacks of September 11, 2001 [34] [23] [26] [14]. However, some kinds of criminal groups, such as terrorist cells and collusion networks, manipulate the relationships among their members, making their network very hard to represent and analyze [10].

In criminal investigative work using the social network approach, a key step is to establish a representative link between network members. This is very important to clearly define how the relationships among the members will be measured [6]. It requires that data describing human behavior garnered from diverse sources be properly modeled and transformed, which is one of the main problems arising in the spatiotemporal mining of social networks [7]. Human interactions are in herently multiplex with diferent types of relationships among the individuals which can lead to multilayers of information to consider [1]. Link analysis is the sub-area of SNA where such data are collected and used to establish links between nodes of the network [28] [9].

The relevant information could be found in many diferent sources being the principal approaches for link construction [15]:

Self-report (establishes a link according to the declaration of each actor),

Communication (establishes a link based on the interaction between individuals; e.g. money transfer or phone calls),

Similarity, also called homophily (establishes a link based on the fact that individuals that are “close to each other” tend to be similar in their socio-demographic attributes and social behavior), and

Co-occurrence (establishes a link between two individuals if they happened to spend time together at the same place; e.g. classmates at school or prison inmates).

An important approach used to extract information from social networks is node importance evaluation. It uses centrality measures [20] and node evaluation algorithms, all of which focus on links of the network. The most common centrality measures employed are the de gree, closeness, betweenness, and eigenvector [19] [30], and the common algorithms are PageRank [22] and HITS [12]. In crime analysis, a node's importance is evaluated to identify particular structures within the network and its most important actors [8].

In addition to links, this study posits that information on network members' criminal background [5] should also be included as the propensity to belong to a criminal group (Pcg). Because this propensity is a node attribute, traditional node evaluators, which focus strictly on links, are not adequate for the task.

In light of the above and with the goal of achieving a more complete and efective analysis of criminal groups, the present study proposes a new node importance evaluator that considers the links between individuals as well as their respective propensities to belong to a criminal group. This approach provides an efective identification of the most important individuals in a crime network. The evaluator and the theoretical concepts that underpin it are formally introduced in the fol lowing section.

3. A novel evaluator including links and propensity to belong to a criminal group

The proposed new evaluator emerges from a novel perspective based on concepts borrowed from the theories of human and social capital, an analytic structure built around an ego network, and an analogy between the social interaction of individuals and the interactions of particles in field theory. It is this perspective that will enable the new evaluator to integrate links between individuals with their propensities to belong to a criminal group.

## 3.1. The novel evaluation approach - an overview

The ability of an individual to carry out a given economic activity can be determined by a set of attributes that reflect his or her acquisition of skills and knowledge over time. These attributes constitute the person's human capital, where the greater this capital, the more he or she will be able to identify and take advantage of economic opportunities [25]. Human capital has been the subject of studies from a variety of approaches and perspectives, much of them being conducted from a social perspective.

In the same way, an individual's ability to engage in a given criminal economic activity will depend on their human capital for committing certain types of ofenses. This criminal human capital can be de termined by some of the individual's attributes expressing his/her relevant knowledge and skills. If these attributes and the resulting criminal human capital can be somehow determined, an individual possessing a high level of human capital for a particular criminal activity can be readily classified as a strong suspect for past or present involvement in it

Using the concept of group human capital, which measures the contribution of an individual to a criminal group, and more specifically to a gang, a microeconomic model of gang formation has been proposed in [4]. According to this model, a criminal group demands a certain minimum level of human capital from each of its members based on minimum required skills and a basic level of commitment to the group. By determining individuals' criminal group human capital, those with the highest levels of such capital can be classified as the individuals most likely to belong to a criminal group.

## 3.2. A representation for the criminal group human capital

An individual's social capital is determined by the set of contacts he/ she maintains social relations via the respective links in a social network. This social capital must be considered when determining an individual's human capital because it is influenced by its contacts' human capital [3]. The criminal group human capital of an individual is thus determined by the criminal group human capital of those to which he/ she is linked.

To express the criminal human capital, $H c g _ { i } ,$ we first define $G ( N , A )$ as a graph representing a social network composed of a set N of nodes or individuals and a set A of arcs or links between the individuals. Then,

$$
H c g _ {i} = P c g _ {i} + H C c g _ {i} \forall i \in N\tag{1}
$$

where.

$P c g _ { i }$ is the propensity of an individual i to belong to a criminal group without considering the contribution made by the other suspect network members to which individual is related. To obtain this value, we consider a set of attributes that measure the acquisition of knowledge and skills for some type of group crime. This value is given by

$$
P c g _ {i} = r (S _ {i}) \forall i \in N\tag{2}
$$

in which $S _ { i }$ is the set of relevant attributes of individual i and r is some function, chosen under a certain context, that transforms this set into a

![](/api/attachments/5Z8MK2QG/fulltext/images/357b48d143487aa8c42d05f31899c198907691fc8205cbfc490a3b33c63d4736.jpg)  
Fig. 1. Ego network of individual i for obtaining HCcg.

propensity value.

HCcg represents the criminal group human capital individual i re ceives from the individuals to which he/she is connected.

The contribution of others to an individual's human capital is a function of his/her social capital represented by the set of links to those with which he/she has relations. To define the function that will represent this contribution, we center the analysis on an ego network. In general, the ego network of an individual i is the network built with i at the center, known as $E g o ,$ and the set of individuals with whom i is directly related $^ { \mathrm { t o , } }$ called Alters, as shown in Fig. 1.

In this ego network, the social capital of individual i (or Ego) is a function of his/her Alters' criminal human capital and of their links to i. Assuming that criminal group human capital is the desired characteristic and that this capital is transferred to i from the Alters through these links, the general function representing the contribution to i's criminal group human capital is given by

$$
H C c g _ {i} = f (H c g, s l) _ {V _ {i}} \forall i \in N\tag{3}
$$

where f is a function that expresses the criminal group human capital transferred from the set of individuals $V _ { i } \subset N$ to i via their social links sl. It is important that an appropriate form is adopted for this function so that a truly representative value for this transfer is obtained. In the next subsection, we present a key relationship for determining this form.

## 3.3. Social interaction and field theory: A key relationship

An appropriate form to represent the criminal group human capital must reflect the fact that the transfer of human capital from one individual to another depends on their link's strength. In other words, the stronger the link, the greater the amount of human capital that can be transferred [3].

The form finally chosen for the function was inspired by an analogy between social interaction among individuals and the interaction between particles described by field theory [13]. A similar analogy underlies certain node evaluation algorithms, which measure the topological potential of a node based on structural aspects of the network [21] [32] [16] [2]. According to field theory, every particle generates a field around itself that exerts a force or influence on every other particle located within its radius of action. Borrowing this idea, we assume that an individual's human capital exerts an influence on other individuals within his or her radius of action.

The potential of a particle i is expressed by the following Gaussian function:

$$
\varphi (i) = \sum_ {j = 1} ^ {n} m _ {j} e ^ {- \left(\frac {d _ {i j}}{\sigma}\right) ^ {2}}\tag{4}
$$

where n is the number of particles, $m _ { j }$ represents the mass of particle $j ,$ $d _ { i j }$ is the topological distance between particles i and $j ,$ and σ is a parameter that controls the particles' region of influence.

Using a Gaussian function such as in Eq. (4) to represent the transfer of human capital allows us to capture the fact that the interaction between individuals has local characteristics and that the human capital's influence decays as the link weakens.

Using $\operatorname { E q . }$ . (4), we propose the following function to represent individual i’s criminal group human capital:

$$
H C c g _ {i} = \sum_ {j \in V} H c g _ {j} e ^ {- \left(\frac {d _ {i j}}{\sigma}\right) ^ {2}}, \forall i \in N\tag{5}
$$

where σ governs the region of influence over which a network member can contribute criminal group human capital to another member and $d _ { i j }$ represents the social distance between suspects i and j.

Given the properties of the Gaussian function, the region of influence of each node is approximately $3 \sigma / \sqrt { 2 }$ . When $\sigma \ge \sqrt { 2 } D / 3$ (D is the diameter of the network), the influence region expands to the whole network [21]. Therefore $\sigma = \sqrt { 2 } D / 3$ will be the value to which the parameter will be set.

It should be noted that the human capital transferred from individual j to individual i includes part of the human capital j received from individuals he/she is directly linked to but who are not necessarily directly linked to i.

Thus, the influence of individuals directly linked to i includes the influence of individuals not directly linked to i. In other words, the measurement of an individual's contribution to criminal group human capital indirectly takes into account the influence of all the individuals in the network.

## 3.4. Social network criminal suspect evaluator: The novel node evaluator

We now formally introduce our proposed new node importance evaluator that considers links and the propensity to belong to a criminal group, which we will call the social network criminal suspect evaluator (SNCSE). Substituting Eq. (5) into Eq. (1), we obtain

$$
H c g _ {i} = r (S _ {i}) + \sum_ {j \in N} H c g _ {j} e ^ {- \left(\frac {d _ {i j}}{\sigma}\right) ^ {2}} \forall i \in N\tag{6}
$$

This can be written in matrix form as

$$
(I - E) H c g = R\tag{7}
$$

where I is the identity matrix, E is a square matrix with elements $e ^ { - \left( \frac { d _ { i j } } { \sigma } \right) ^ { 2 } } \geq 0 \forall i , j \in N ,$ , Hcg is the column vector of elements Hcg $\forall \ : i \in N$ and H is the column vector of elements $r ( S _ { i } ) \geq 0 .$ . To determine how the evaluator can be applied to a suspect network, observe first that it has the following form:

$$
x _ {i} = c _ {i} + \sum_ {j \in N} a _ {i j} x _ {j}\tag{8}
$$

This form is a system of linear equations similar to the one used for solving Leontief's input-output model [17]. The Leontief input-output model is a quantitative economic technique that represents the interdependencies between diferent areas of a national economy or different regional economies. In that model, $a _ { i j }$ is interpreted as the input of product i per unit of output of $j ,$ x as the output of the emphith industry and $c _ { i }$ is the amount of the c th product in the bill of goods. The

matrix form is

$$
(I - A) X = C\tag{9}
$$

where X and C are column vectors containing n components and A is the square matrix containing elements $a _ { i j } .$

The input-output model assumes that the $a _ { i j }$ values are non-nega tive, as can be deduced from the definition of a product input and the postulate that each primary production process has only one output. dij <sup>2</sup>

$$
e ^ {- \left(\frac {d _ {i j}}{\sigma}\right) ^ {2}}
$$

The same is also true of the e values in Eq. (6), in which a single type of human capital $( \mathrm { i . e . } ,$ , criminal group) is transferred to obtain a diferent level of the same type, and the minimum transferable amount from one individual to another is zero.

The main formal question in the input-output model is the existence of a static solution to the system of linear equations (Eq. (8)) that produces a bill of goods without negative outputs. Such a solution can be found if the corresponding dynamic system of product transfer is stable [27].

In a suspect network, a negative value for criminal group human capital has no meaning, as it would imply that, upon transferring part of his or her human capital, an individual becomes, in some sense, the opposite of suspect. In reality, of course, such a transfer can only make one individual less suspect than another. To ensure that the system of equations in Eq. (6) produces non-negative outputs, the dynamic system that transfers criminal group human capital between individuals must be stable. The level of human capital in this dynamic system is obtained via the following system of diference equations:

$$
I H c g _ {t + 1} - E H c g _ {t} = R\tag{10}
$$

where t is a discrete-time criminal group human capital transference and a stable solution is reached when $H c g _ { ( t + 1 ) } = H c g _ { t } = H c g _ { }$ . This solution will represent the maximum criminal group human capital levels that can be attained in a suficiently large amount of time. A solution for the system in Eq. (10) arrived at through iteration can be expressed as

$$
H c g _ {t} = E ^ {t} H c g _ {0} + (I + E + E ^ {2} + \dots + E ^ {t - 1}) R = E ^ {t} H c g _ {0} + R \sum_ {k = 0} ^ {t - 1} E ^ {k}\tag{11}
$$

where the criminal group human capital converges to a stable value if and only if the absolute values of the eigenvalues $\lambda _ { i }$ of the matrix E are less than 1, that is, $\begin{array} { r } { | \lambda _ { i } | \ < \ 1 \ \forall \ i \ \in \ N } \end{array}$ [27], in which case $I + E + E ^ { 2 } + \ldots$ converges to $\left( I - E \right) ^ { - 1 }$ and $E ^ { t } H c g _ { 0 }$ to the null matrix, and Hcg is obtained by $H c g = ( I - E ) ^ { - 1 } R$

If E is a nonnegative, indecomposable matrix, none of whose column sums is greater than one and whereby at least one of the column sums is less than one, then $\left| \lambda _ { i } \right| ~ < ~ 1 ~ \forall ~ i \in { \cal N } ~ [ 2 7 ]$ . To guarantee this last condition, we divide the E matrix by the scale factor $\begin{array} { r } { \sum _ { i j \in N } e ^ { - \left( \frac { d _ { i j } } { \sigma } \right) ^ { 2 } } } \end{array}$ . Thus, the SNCSE is

$$
H c g _ {i} = r (S _ {i}) + \frac {\sum_ {j \in N} H c g _ {j} e ^ {- \left(\frac {d _ {i j}}{\sigma}\right) ^ {2}}}{\sum_ {i j \in N} e ^ {- \left(\frac {d _ {i j}}{\sigma}\right) ^ {2}}} \forall i \in N\tag{12}
$$

After obtaining the $H c g _ { i }$ of each individual i of the network, those whose criminal group human capital increased the most with respect to their initial capital Pcg will be defined as the most important in dividuals. This increase is represented by the following:

$$
\varDelta H c g _ {i} = H c g _ {i} - r (S _ {i}) \forall i \in N\tag{13}
$$

## 3.5. Application to the example network

We will use an example network to show that the results of SNCSE are consistent with the results of the traditional node evaluator, and we explain the way it works. Fig. 2 shows our example network. This network has 12 nodes and 11 edges. All the edges have a value equal to 1.

![](/api/attachments/5Z8MK2QG/fulltext/images/19c6cd6f0255a3ba37851233fea383b997e2f47c69962f17cb2049aed1f52f31.jpg)  
Fig. 2. Example network.

In the example network of Fig. 2, nodes 1, 6, 7 and 12 are the most important. These nodes must be identified as the most important in the network by any evaluator of node importance. Nodes 1 and 12 must have the same importance, and node 6 and node 7 must also have the same importance.

Table 1 shows the results of the application of centrality measures from SNA, the node evaluation algorithms, and the proposed evaluator: SNCSE.

In Table 1, the evaluators degree, betweenness, closeness, eigenvector, page rank, and hits and our proposed evaluator, SNCSE, identify nodes 1, 6, 7, and 12 as the most important in the network (in bold). These results show that the SNCSE is consistent with the results of traditional evaluators. However, SNCSE gave a diferent level of im portance to nodes 1, 12, 6, and 7. This diferent level of importance is due to Pcg. Nodes 1 and 12 have the same level of Pcg, equal to 0.4. The sum of the Pcg of the neighbors of node 12 (7, 8, 9, 10, and 11) is 3.4. This sum is greater than the sum of Pcg of the neighbors of node 1 (2, 3, 4, 5, and 6), which is 2.4. For this reason, the criminal influence of the neighbors of node 12 is greater than the neighbors of node 1, and SNCSE better evaluates node 12 in that node 1 and node 12 become the best-evaluated nodes in the network. Nodes 6 and 7 have the same level of Pcg, equal to 0.4. Node 7 is closer to node 12 than node $^ { 6 , }$ and SNCSE evaluates node 7 as better than node 6. In general, each node on the right side (1, 2, 3, 4, 5, and 6) is closer to nodes with more Pcg than the nodes on the left side (7, 8, 9, 10, 11, and 12), and the SNCSE better evaluates the nodes on the right side than the equivalent nodes on the left side.

## 4. Applications of the social network criminal suspect evaluator

In the previous section, we introduced the SNCSE node evaluator, we analyzed the conditions for its application and applied the SNCSE to an example network. In this section, we present two applications and test SNCSE efectiveness. In the first application, the SNCSE is applied to identify members of a criminal group committing burglary in an uninhabited place. We used a dataset provided by the Crime Analysis Unit of the Public Prosecutor's Ofice of “Región del Biobío, $\mathrm { C h i l e } ^ { \dprime }$ . In the second application, the SNCSE is applied to identify members whit the role of a leader in the Greek terrorist group November 17.

We propose the following generic methodology to apply SNCSE:

First, the network is established and social distances among nodes are determined. Next, we determine the propensity to belong to a criminal group (Pcg). Finally, we apply SNCSE to evaluate the nodes' importance.

In a particular application this methodology has to be adapted. The following subsections present particular applications providing ideas on how to apply the proposed evaluator SNCSE in diferent real-world cases.

Table 1  
Results of evaluators applied to the network example.

<table><tr><td>Node</td><td>Degree</td><td>Betweenness</td><td>Closeness</td><td>Eigenvector</td><td>Page Rank</td><td>Hits</td><td>Pcg</td><td>Hcg</td><td> $SNCSE(\Delta Hcg)$ </td></tr><tr><td>1</td><td>5</td><td>34</td><td>26</td><td>0.475</td><td>0.217</td><td>0.475</td><td>0.4</td><td>0.5245</td><td>0.1245</td></tr><tr><td>2</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.4</td><td>0.4238</td><td>0.0238</td></tr><tr><td>3</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.5</td><td>0.5238</td><td>0.0238</td></tr><tr><td>4</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.6</td><td>0.6238</td><td>0.0238</td></tr><tr><td>5</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.7</td><td>0.7238</td><td>0.0238</td></tr><tr><td>6</td><td>2</td><td>30</td><td>24</td><td>0.341</td><td>0.086</td><td>0.341</td><td>0.4</td><td>0.4441</td><td>0.0441</td></tr><tr><td>7</td><td>2</td><td>30</td><td>24</td><td>0.341</td><td>0.086</td><td>0.341</td><td>0.4</td><td>0.4457</td><td>0.0457</td></tr><tr><td>8</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.6</td><td>0.6255</td><td>0.0255</td></tr><tr><td>9</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.7</td><td>0.7255</td><td>0.0255</td></tr><tr><td>10</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.8</td><td>0.8255</td><td>0.0255</td></tr><tr><td>11</td><td>1</td><td>0</td><td>36</td><td>0.199</td><td>0.049</td><td>0.199</td><td>0.9</td><td>0.9255</td><td>0.0255</td></tr><tr><td>12</td><td>5</td><td>34</td><td>26</td><td>0.475</td><td>0.217</td><td>0.475</td><td>0.4</td><td>0.5613</td><td>0.1613</td></tr></table>

## 4.1. Application to the public Prosecutor's ofice of “Región del Biobío, Chile” dataset

In order to show its usefulness for crime investigation, we applied SNCSE to a data set provided by the Crime Analysis Unit of the Public Prosecutor's Ofice of “Región del Biobío, Chile”. This organization investigates crimes and conducts the corresponding actions in the south of Chile. The mentioned data set includes 1598 ofenses committed between 2004 and 2017. Some registers of this set are shown in Table 2.

The columns in Table 2 have the following interpretation. “Cause Code” is the key to a criminal case investigated by the Crime Analysis Unit. It includes one or more suspects, labeled by the “Suspect Code”, and one or more “Ofenses”. “Date” is the date on which the ofense was committed.

In this subsection, SNCSE will be used to evaluate nodes considering their propensity to belong to a criminal group committing burglaries in an uninhabited place. This particular group has been investigated back in 2018 by the Crime Analysis Unit. As a result of this investigation, ground-truth information for each node is available.

## 4.1.1. Establish network and determine social distances

If two suspects have the same cause code, we connected them via a link since they acted together in at least one ofense. Table 3 shows some examples of the number of criminal cases committed jointly by the suspects i and j (sl<sub>ij</sub>), and their social distance (d<sub>ij</sub>) obtained via Eq. (14).

$$
d _ {i j} = \frac {\min \{s l _ {i j} > 0 \forall i , j \in N \}}{s l _ {i j}}\tag{14}
$$

Fig. 3 shows the graph obtained where 77 nodes are linked via 374 arcs. Those suspects that have been identified by previous investigations as responsible for robbery in an uninhabited place are indicated by a circle.

## 4.1.2. Determine the propensity to belong to a criminal group (Pcg)

We assume that a suspect's previous criminal activities are relevant to estimate their propensity to belong to a criminal group (Pcg). Hence, we calculate two values for each suspect: the number of robberies between 2016 and 2017 (their recent experience) and the total number of such ofenses during the observed period (their overall experience). Next, we compute the average and standard deviation for these two values over all 77 suspects.

Table 2  
Subset of the database provided by the Crime Analysis Unit.

<table><tr><td>Cause Code</td><td>Suspect Code</td><td>Offense</td><td>Date</td></tr><tr><td>1200754382</td><td>TPGQ_36</td><td>Fighting in a Public Place</td><td>20-09-2012</td></tr><tr><td>1200756723</td><td>LRCJ_3</td><td>Burglary in an uninhabited place</td><td>11-09-2012</td></tr><tr><td>1200729201</td><td>AOJR_27</td><td>Injuries</td><td>02-09-2012</td></tr><tr><td>1200714814</td><td>JAQP_69</td><td>Injuries</td><td>25-08-2012</td></tr><tr><td>1200694081</td><td>HRVP_33</td><td>Drug possession</td><td>24-08-2012</td></tr><tr><td>1200678932</td><td>RUDQ_5</td><td>Injuries</td><td>19-08-2012</td></tr><tr><td>1200678866</td><td>PZLU_72</td><td>Criminal possession of a weapon</td><td>18-08-2012</td></tr><tr><td>1200653591</td><td>LPFU_18</td><td>Theft</td><td>10-08-2012</td></tr><tr><td>1200634593</td><td>SAPQ_22</td><td>Injuries</td><td>07-08-2012</td></tr></table>

Table 3  
Relation between suspects.

<table><tr><td>Suspect i</td><td>Suspect j</td><td> $sl_{ij}$ </td><td> $d_{ij}$ </td></tr><tr><td>ABCD_32</td><td>EFGH_33</td><td>3</td><td>0.33</td></tr><tr><td>XBCQ_37</td><td>AFWP_41</td><td>1</td><td>1</td></tr><tr><td>RDEN_32</td><td>MOOA_86</td><td>1</td><td>1</td></tr><tr><td>PAPA_32</td><td>MAMA_32</td><td>1</td><td>1</td></tr><tr><td>PACG_3</td><td>AAAA_10</td><td>3</td><td>0.33</td></tr><tr><td>AIGD_13</td><td>JIAI_57</td><td>2</td><td>0.5</td></tr></table>

Fig. 4 displays the 77 suspects using the two dimensions mentioned before. The dotted lines next to the axes represent the average values of the respective axis. The other lines indicate the average values plus a standard deviation; thus leading to nine rectangles.

Suspects with highest overall experience and highest recent experience, i.e., those in the upper right rectangle, received $P c g = 0 . 9 .$ The opposite case, i.e., the lower left rectangle (low level of experience and few current activities) is classified as $P c g = 0 . 1$

The other values of Pcg are determined following the practice applied at the Criminal Analysis Unit where the level of recent activities weighs more than the overall experience when it comes to estimate Pcg. The number next to the asterisks in each rectangle shown in Fig. 4 indicates the respective value of Pcg.

## 4.1.3. Apply SNCSE

Table 4 shows part of the results obtained by the application of the evaluators to the network of Fig. 4. The evaluators considered are the centrality measures from SNA (degree, betweenness, closeness, and eigenvector), the node evaluation algorithms (page rank and hits) and the proposed SNCSE. The table only shows the results for the members of the criminal group committing burglaries in an uninhabited place.

Table 4 shows the members sorted by their value from SNCSE. The leaders of the criminal band are marked with an asterisk (\*).

The test of the efectiveness of SNCSE consisted of identifying the members of a criminal group committing burglaries in an uninhabited place into the first positions in the ranking generated by SNCSE. Then, we compared these results with the rankings generated by the SNA centrality measures and node evaluation algorithms. Table 5 shows the ranking of the 20 suspects with the highest evaluated indices by each evaluator.

Table 5 shows the members of the criminal group marked in bold and leaders marked by an asterisk (\*). SNCSE identified more members of the criminal group than other evaluators (SNCSE 8 and the other evaluators 5). SNCSE concentrated more members in the first positions and assigned a better place to the leaders.

![](/api/attachments/5Z8MK2QG/fulltext/images/669a003bdb2802d78d7656b95a308a01d44e7f0be084eec82d4c83f9ba56fa6a.jpg)  
Fig. 3. Suspects network.

Propensity to Commit Burglary in an Uninhabited Place  
![](/api/attachments/5Z8MK2QG/fulltext/images/cdbc159bef99bbc6e0bd2eb89866bbcb6e0519e748de8af70d890a72ed43fa19.jpg)  
Number of offenses committed during the years 2016 and 2017  
Fig. 4. Estimating the propensity to commit burglary in an uninhabited place.

Fig. 5 shows a comparison among SNCSE and the other evaluators. Each chart represents the percentage of members of a criminal group classified out of all suspects evaluated and ordered top to bottom.

In each chart of Fig. 5, an evaluator performed better than the others if its curve was nearest to the point (0.1). If the curve of an evaluator is nearer than another evaluator to this point, then the evaluator concentrates the members of the criminal group in the first po sitions of the ranking and identifies all the members “earlier”. SNCSE was able to include the group members “earlier” than the other evaluators, that is, it was able to concentrate the group members in the higher positions in the ranking.

In Eq. (15), we propose a performance measure for comparison of the evaluators in a quantitative manner.

$$
\text { Performance } = \frac {\sum_ {i \in N} y _ {i}}{| N |}\tag{15}
$$

where $y _ { i }$ is the percentage of members of the criminal group identified by the first i ranked suspects, i.e., the value that corresponds to member i on the curve of the respective evaluator in Fig. 5, and |N| is the total number of ranked suspects.

Table 6 shows the performance of each evaluator considered. As seen, SNCSE outperformed all other evaluators.

SNCSE considers that the suspects strongly linked to individuals with higher criminal propensity may be associate with a criminal group. This fact can lead to a False Positive (a suspect identified as a member of a group when it is not). Such a False Positive delays the criminal investigative process since investigative resources are spent unnecessarily. However, a False Negative (a suspect identified as not being a member of a criminal group when in reality it is) is generally more relevant than a False Positive given the social cost associated.

Fig. 6 shows False Positive Rates (FPR, triangles) and False Negative Rates (FNR, Circles) for the two best evaluators (SNCSE and Betweenness) and the mean values of these rates considering all the evaluators, for six diferent rankings of suspects. As can be seen, SNCSE outperforms consistently the alternative evaluators for FPR as well as for FNR, respectively. The SNCSE has False Negative Rates lower than the False Positive Rates for all rankings except for the ranking 10.

## 4.2. Application to the network of the Greek terrorist group November 17

The revolutionary organization November 17 (N17) [24] was founded following the violent suppression of student protests at the Athens Polytechnic School by security forces of the Greek military junta in November 1973. N17 was a Marxist-Leninist group opposed to capitalism, imperialism, and the military. N17 have attacked a variety of targets since 1975, using assassination and bombing. The frequency of attacks has not been high, with the group being reliant on stolen weapons and material to conduct its operations. The last attack that the group is known to have undertaken was the assassination of the British Defense Attaché to Athens, Brigadier Saunders, in June 2000. Following a botched bombing attempt in 2002, in which group member Savas Xiros was injured and subsequently arrested, abundant information about the organization and structure of N17 was released into the public domain. It is believed, but not confirmed, that N17 no longer exists in a form that is capable of conducting terrorist operations.

Table 4  
Results of evaluators for each of the key suspects.

<table><tr><td>Suspect</td><td>Degree</td><td>Betweenness</td><td>Closeness</td><td>Eigenvector</td><td>PageRank</td><td>Hits</td><td>SNCSE</td></tr><tr><td>JFAM_32*</td><td>13</td><td>559.278</td><td>181</td><td>0.228</td><td>0.033882245</td><td>0.03195465</td><td>0.01515586</td></tr><tr><td>CAAR_9</td><td>18</td><td>1147.43</td><td>156</td><td>0.27</td><td>0.047489832</td><td>0.056184881</td><td>0.012817484</td></tr><tr><td>RIQJ_5</td><td>9</td><td>218.711</td><td>178</td><td>0.255</td><td>0.018858344</td><td>0.034209921</td><td>0.011789292</td></tr><tr><td>LDSS_60</td><td>9</td><td>51.76</td><td>232</td><td>0.245</td><td>0.014519162</td><td>0.015022989</td><td>0.011402661</td></tr><tr><td>BAQV_66*</td><td>11</td><td>684.414</td><td>163</td><td>0.257</td><td>0.027518859</td><td>0.038799971</td><td>0.01135948</td></tr><tr><td>MIAP_11</td><td>10</td><td>141.676</td><td>191</td><td>0.307</td><td>0.018384241</td><td>0.027499563</td><td>0.011125503</td></tr><tr><td>JIAI_57</td><td>9</td><td>162.551</td><td>215</td><td>0.196</td><td>0.020166234</td><td>0.017267781</td><td>0.01059808</td></tr><tr><td>AICD_13</td><td>8</td><td>64.753</td><td>223</td><td>0.232</td><td>0.01333435</td><td>0.016132859</td><td>0.010379399</td></tr><tr><td>DEHB_70</td><td>6</td><td>65.7</td><td>200</td><td>0.158</td><td>0.014296928</td><td>0.025553392</td><td>0.00890763</td></tr><tr><td>VMAU_52</td><td>4</td><td>0</td><td>264</td><td>0.111</td><td>0.007196447</td><td>0.004325847</td><td>0.008604627</td></tr><tr><td>YRUR_58</td><td>5</td><td>41.732</td><td>249</td><td>0.057</td><td>0.013776418</td><td>0.008310711</td><td>0.008498517</td></tr><tr><td>BAPV_41</td><td>11</td><td>359.606</td><td>187</td><td>0.13</td><td>0.029172162</td><td>0.026457822</td><td>0.008447545</td></tr></table>

In this section, we present the application of the proposed SNCSE to identify members with the role of “Leader” using the available N17 dataset. We take the data generated by a previous study [24] [11] as input for our analysis. Eight of 22 terrorists in the network were identified as Leaders.

Table 7 shows the resources that each member of N17 controlling, its faction, and its role in the group. Table 7 also shows the abbreviated name in () and the \* indicate the members with leader role.

## 4.2.1. Network and determination of distances

Using news summaries and trial reports, the network was obtained by [11] and is shown in Fig. 7; see also [24]. Our analysis is based on this network.

Next, we have to establish the distances $d _ { i j }$ among individuals in the N17 network. We determine these distances based on the factions that the members belong to; see Table 7.

The main factions are: 1st Generation Founders (G), the Sardanopoulos faction (S), and the Koufontinas faction (K).

On the basis of these factions, we establish the respective distances as shown in Eq. 16

$$
d _ {i j} = \left( \begin{array}{l l} 0. 2 5 & \text { if   terrorists } i \text { and } j \text { belong   to   the   same   faction } \\ 0. 5 & \text { if   terrorists } i \text { and } j \text { belong   to   different   factions } \\ 0. 7 5 & \text { if } i \text { or } j \text { does   not   belong   to   any   faction } \end{array} \right)\tag{16}
$$

## 4.2.2. Determination of Pcg

In this case, Pcg represents the propensity of a member to take the role of a leader in the terrorist organization. To determine Pcg, we propose a simple score based on the relation between each attribute shown in Table 7 and the role.

Prior to establish this score, we simplify the set of attributes by merging those that have identical distributions as will be shown next. As can be seen in Table 7, the attributes Weapons and Safe houses have identical columns and we selected Weapons as the representative attribute. The attributes Drugs, Human traficking, and Weapons smuggling have the same distributions; we selected Drugs as the representative attribute. Similarly, the attributes Bank robberies and Stealing weapons have the same distribution; we selected Bank robberies as the representative attribute. The attribute Attacks takes the same value for all terrorists and is discarded from the analysis. Thus, the attributes considered in determining the capability of being a leader are Money, Weapons, Drugs, and Bank robberies.

Having simplified the attribute set, we now use the information gain

Table 5  
Ranking of suspects generated by each evaluator.

<table><tr><td>Ranking</td><td>Degree</td><td>Betweenness</td><td>Closeness</td><td>Eigenvector</td><td>PageRank</td><td>Hits</td><td>SNCSE</td></tr><tr><td>1</td><td>CAAR_9</td><td>CAAR_9</td><td>CAAR_9</td><td>MIAP_11</td><td>CAAR_9</td><td>CAAR_9</td><td>JFAM_32*</td></tr><tr><td>2</td><td>JFAM_32*</td><td>BAQV_66*</td><td>BAQV_66*</td><td>CAAR_9</td><td>JFAM_32*</td><td>BAQV_66*</td><td>CAAR_9</td></tr><tr><td>3</td><td>BAPV_41</td><td>JFAM_32*</td><td>RIQJ_5</td><td>BAQV_66*</td><td>BAPV_41</td><td>RIQJ_5</td><td>RIQJ_5</td></tr><tr><td>4</td><td>BAQV_66*</td><td>BAPV_41</td><td>JFAM_32*</td><td>RIQJ_5</td><td>BAQV_66*</td><td>FJFR_66</td><td>LDSS_60</td></tr><tr><td>5</td><td>AACQ_32</td><td>CAFV_4</td><td>BAPV_41</td><td>LDSS_60</td><td>CAFV_4</td><td>JFAM_32*</td><td>BAQV_66*</td></tr><tr><td>6</td><td>MIAP_11</td><td>JACV_57</td><td>MALL_60</td><td>AICD_13</td><td>CASQ_64</td><td>AACQ_32</td><td>MIAP_11</td></tr><tr><td>7</td><td>CAFV_4</td><td>MALL_60</td><td>MIAP_11</td><td>ORAA_44</td><td>JIAI_57</td><td>MIAP_11</td><td>JIAI_57</td></tr><tr><td>8</td><td>JIAI_57</td><td>RIQJ_5</td><td>CAFV_4</td><td>JFAM_32*</td><td>AACQ_32</td><td>FEMC_15</td><td>AICD_13</td></tr><tr><td>9</td><td>LDSS_60</td><td>FJFR_66</td><td>LACS_13</td><td>CAFV_4</td><td>SAAR_55</td><td>LACS_13</td><td>DEHB_70</td></tr><tr><td>10</td><td>RIQJ_5</td><td>AIAP_3</td><td>DEHB_70</td><td>JIAI_57</td><td>RIQJ_5</td><td>CAFV_4</td><td>VMAU_52</td></tr><tr><td>11</td><td>AICD_13</td><td>JIAI_57</td><td>FJFR_66</td><td>JNLT_23</td><td>RIRR_1</td><td>BAPV_41</td><td>YRUR_58</td></tr><tr><td>12</td><td>CASQ_64</td><td>CASQ_64</td><td>JIAR_4</td><td>LACS_13</td><td>MIAP_11</td><td>DEHB_70</td><td>BAPV_41</td></tr><tr><td>13</td><td>FJFR_66</td><td>AACQ_32</td><td>JACV_57</td><td>AACQ_32</td><td>FJFR_66</td><td>JASN_2</td><td>CAFV_4</td></tr><tr><td>14</td><td>CAVP_33</td><td>MIAP_11</td><td>HEVF_70</td><td>DEHB_70</td><td>ORAA_44</td><td>ORAA_44</td><td>JNLT_23</td></tr><tr><td>15</td><td>FEMC_15</td><td>LACS_13</td><td>CASQ_64</td><td>FJFR_66</td><td>SEGG_15</td><td>YAMP_75</td><td>ORAA_44</td></tr><tr><td>16</td><td>ORAA_44</td><td>CAVP_33</td><td>JAAP_52</td><td>SAAC_73</td><td>LACS_13</td><td>CASQ_64</td><td>SEAU_35</td></tr><tr><td>17</td><td>RIRR_1</td><td>RIRR_1</td><td>JIAI_57</td><td>BAPV_41</td><td>FEMC_15</td><td>JIAR_4</td><td>JDTB_51</td></tr><tr><td>18</td><td>SAAR_55</td><td>CMNC_36</td><td>RIRR_1</td><td>FEMC_15</td><td>JIAR_4</td><td>MAMA_25</td><td>WDMM_20</td></tr><tr><td>19</td><td>DEHB_70</td><td>HEVF_70</td><td>JHAR_70</td><td>SEAU_35</td><td>MASP_25</td><td>MALL_60</td><td>LACS_13</td></tr><tr><td>20</td><td>JACV_57</td><td>FEMC_15</td><td>AACQ_32</td><td>HEVF_70</td><td>MALL_60</td><td>JIAI_57</td><td>HEVF_70</td></tr></table>

SNCSE v/s Degree  
![](/api/attachments/5Z8MK2QG/fulltext/images/ef5b52bb020ee11f2b03fb531800067ad0efbdcc195926f74be271e8b7c2163d.jpg)  
SNCSE v/s Betweenness

SNCSE v/s Closeness  
![](/api/attachments/5Z8MK2QG/fulltext/images/29d5db61b6fd19d8ecaff3cd67af3a4a5a070e4e322a2a6889b59bb52432617b.jpg)

![](/api/attachments/5Z8MK2QG/fulltext/images/c017e09245892205b69f6c160674d6328f421954be3644b933b3cce1e5f095d4.jpg)  
SNCSE v/s Page Rank

SNCSE v/s Eigenvector  
![](/api/attachments/5Z8MK2QG/fulltext/images/fa4e92524668bd9eee0457456e95c546c99de841731dd242f12c539449b9f800.jpg)  
SNCSE v/s Hits

![](/api/attachments/5Z8MK2QG/fulltext/images/1b1ef1ce8ae60fee95fc377f72f83cfc2e2841f2a2629ac1beadb3568106f880.jpg)  
Cumulative Percentage of Ranked Imputec

![](/api/attachments/5Z8MK2QG/fulltext/images/170f99087dbc6791f81f733851902f1d55908797a130f0f3538d5b99881d21dd.jpg)  
Cumulative Percentage of Ranked Imputed  
Fig. 5. Efectiveness test: Inclusion of members of a criminal group committing burglaries in an uninhabited place.

Table 6  
Performance of each evaluator considered.

<table><tr><td>Evaluator</td><td>Performance</td></tr><tr><td>SNCSE</td><td>0.7316</td></tr><tr><td>Betweenness</td><td>0.6266</td></tr><tr><td>Page Rank</td><td>0.6201</td></tr><tr><td>Degree</td><td>0.5931</td></tr><tr><td>Eigenvector</td><td>0.5725</td></tr><tr><td>Closeness</td><td>0.5552</td></tr><tr><td>Hits</td><td>0.5552</td></tr></table>

criterion to establish the relation between each one of the remaining attributes and the role. An attribute's information gain is defined as the diference between the prior uncertainty and expected posterior uncertainty using the attribute. This measure determines the part of information contained in each attribute that will help us to characterize the role. The values are shown in Table 8.

The Pcg function for each member of the group is represented by Eq. 17:

$$
P c g _ {i} = 1 - \sum_ {k} P _ {k} S _ {k i}\tag{17}
$$

where $P _ { k }$ is the normalized value of information contained in the at tribute k and $S _ { k i }$ is the value (1 or 0) of the attribute k for the member i. Fig. 8 shows the Pcg level of each member of the terrorist group.

As expected, Fig. 8 shows that the individuals with the highest Pcg are the leaders except two: 6-Dimitris Koufontinas (DK\*) and 3-Christodoulos Xiros (CX\*). The analysis of the SNCSE application will focus mainly on the eight leaders.

False Positive – False Negative Rate Best Evaluators  
![](/api/attachments/5Z8MK2QG/fulltext/images/b0a0b374aaaf9ee80f1e8d148c29c131e44c8eebb1987dbd070db78c9285a3eb.jpg)  
Fig. 6. False Positive - False Negative Rate of two best evaluators and Mean Rates.

## 4.2.3. Apply SNCSE

Table 9 shows the results obtained by the evaluators applied to the network of Fig. 4 and the performance of each evaluator according to Eq. (15). Table 9 is organized by descending order of SNCSE.

Table 9 shows the good performance obtained by the evaluators except for Betweenness. SNCSE achieves the best performance closely followed by Hits and Degree. Despite the low Pcg level of the leaders 6- Dimitris Koufontinas (DK \*) and 3-Christodoulos Xiros (CX \*), SNCSE ranks them within the first nine positions as shown in Fig. 8.

Table 10 shows that traditional evaluators rank 3-Christodoulos Xiros (CX\*) among the first four places and 6-Dimitris Koufontinas (DK\*) among the first five places. That is, given their role as leaders, they get a key position in the network. This key position is used by SNCSE and assign 3-Christodoulos Xiros (CX\*) and 6-Dimitris

Koufontinas (DK\*) a better position than the operational members (except 15-Savas Xiros (SX)), despite their low Pcg.

As Fig. 8 reveals, the members 4-Constantinos Karatsolis (CK), 9- Iraklis Kostaris (IK), 12-Patroclos Tselentis (PT), and 18-Thomas Serifis (TS) have a medium level of Pcg. Table 10 shows through the traditional evaluators that these members do not have a key position in the network. Therefore, SNCSE dismisses them as leaders.

Fig. 9 compares SNCSE to the other evaluators and its analysis is similar to the one in Fig. 5 in subsection 4.1.3. The y-axis of each chart represents the percentage of leaders of the Greek terrorist group November 17 identified out of all members evaluated. The x-axis represents all group members ordered from top to bottom according to the respective evaluator. SNCSE concentrates more leaders in the first positions than all other evaluators. If we consider a ranking of eight members, equal to the number of leaders, SNCSE has only one falsepositive (15-Savas Xiros (SX)) and only one false negative (3-Christo doulos Xiros (CX \*)), the same number as Hits (see Table 10).

Table 7  
Resource control, Role, and Faction in the Greek terrorist group November 17.

<table><tr><td rowspan="2">Name</td><td rowspan="2">Money</td><td rowspan="2">Weapons</td><td>Safe</td><td>Attacks</td><td>Drugs</td><td>Human</td><td>Weapons</td><td>Bank</td><td>Stealing</td><td rowspan="2">Faction</td><td rowspan="2">Role</td></tr><tr><td>houses</td><td></td><td></td><td>trafficking</td><td>smuggling</td><td>robberies</td><td>weapons</td></tr><tr><td>1-Alexandros Giotopoulos (AG*)</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>G</td><td>Leader</td></tr><tr><td>2-Anna (An*)</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>G</td><td>Leader</td></tr><tr><td>3-Christodoulos Xiros (CX*)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Leader</td></tr><tr><td>4-Constantinos Karatsolis (CK)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>S</td><td>Operational</td></tr><tr><td>5-Constantinos Telios (CT)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Operational</td></tr><tr><td>6-Dimitris Koufontinas (DK*)</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Leader</td></tr><tr><td>7-Dionysis Georgiadis (DG)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Operational</td></tr><tr><td>8-Elias Gaglias (EG)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Operational</td></tr><tr><td>9-Iraklis Kostaris (IK)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>S</td><td>Operational</td></tr><tr><td>10-Nikitas (Ni*)</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>G</td><td>Leader</td></tr><tr><td>11-Ojurk Hanuz (OH)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>-</td><td>Operational</td></tr><tr><td>12-Patroclos Tselentis (PT)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>S</td><td>Operational</td></tr><tr><td>13-Pavlos Serifis (PS*)</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>S</td><td>Leader</td></tr><tr><td>14-Sardanopoulos (Sa*)</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>S</td><td>Leader</td></tr><tr><td>15-Savas Xiros (SX)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Operational</td></tr><tr><td>16-Sotirios Kondylis (SK)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>-</td><td>Operational</td></tr><tr><td>17-Fotis (Fo*)</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>G</td><td>Leader</td></tr><tr><td>18-Thomas Serifis (TS)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>S</td><td>Operational</td></tr><tr><td>19-Vassilis Tzortzatos (VT)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Operational</td></tr><tr><td>20-Vassilis Xiros (VX)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>K</td><td>Operational</td></tr><tr><td>21-Yiannis (Yi)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>-</td><td>Operational</td></tr><tr><td>22-Yiannis Skandalis (YS)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>-</td><td>Operational</td></tr></table>

![](/api/attachments/5Z8MK2QG/fulltext/images/6bf8e6fb02a971c083d80bea6486a7905cbc1cccdc941dc05d509185c4be8925.jpg)  
Fig. 7. Network of the Greek terrorist group November 17.

Table 8  
Normalized information gain for each attribute.

<table><tr><td>Attribute</td><td>Money</td><td>Weapons</td><td>Drugs</td><td>Bank robberies</td></tr><tr><td>Value</td><td>0.2650</td><td>0.6409</td><td>0.0012</td><td>0.0928</td></tr></table>

## 5. Conclusions and future research

An investigation of criminal groups requires that large quantities of resources be focused on key individuals to detect the existence of such groups or prevent their formation. By conceptualizing criminal groups as social networks, the identification of these individuals can be ap proached using node importance evaluators. This study proposed a novel evaluator called the SNCSE, which, in addition to network links, incorporates the propensity of each network member to belong to a criminal group toward achieving a more complete and efective analysis of criminal groups, thereby incorporating all available information.

SNCSE was applied to two real-world problems. The first application considered a dataset of suspects provided by the Public Prosecutor's Ofice of Región del Biobío-Chile. SNCSE outperformed alternative evaluators by identifying the most important nodes in the network. SNCSE included a greater number of members of a criminal group among the top-ranked suspects and positioned them higher within that ranking, therein considering the propensity of belonging to a criminal group (Pcg). This higher positioning of the members of a criminal group among the top-ranked individuals is an outcome that could have a significant positive impact on the short-term results of a criminal investigation and thus also on the eficient use of investigative resources. The False Positive and False Negative rates in SNCSE are lower than other evaluators, which leads to less delay in the criminal investigative process (less False Positives) and a lower social cost (less False Negatives). Additionally, because SNCSE incorporates social relations into its evaluations, the top-ranked suspects tend to be those who have the most significant network links. This fact suggests that the suspects

![](/api/attachments/5Z8MK2QG/fulltext/images/35676a7e2d12d003f46d6de558f939c085ac046705156a098c6d93ab53d3cfdb.jpg)  
Fig. 8. Pcg of each member of the Greek terrorist group November 17.

Table 9  
Results of evaluators for each member of the Greek terrorist group November 17.

<table><tr><td>Name</td><td>Degree</td><td>Betweenness</td><td>Closeness</td><td>Eigenvector</td><td>PageRank</td><td>Hits</td><td>SNCSE</td></tr><tr><td>13-Pavlos Serifis (PS*)</td><td>14</td><td>41.138</td><td>32</td><td>0.404</td><td>0.096269077</td><td>0.097432583</td><td>0.056837062</td></tr><tr><td>1-Alexandros Giotopoulos (AG*)</td><td>10</td><td>25.353</td><td>32</td><td>0.317</td><td>0.073880973</td><td>0.080972418</td><td>0.047085237</td></tr><tr><td>14-Sardanopoulos (Sa*)</td><td>6</td><td>0.924</td><td>40</td><td>0.215</td><td>0.043655781</td><td>0.057213798</td><td>0.038287937</td></tr><tr><td>2-Anna (An*)</td><td>6</td><td>0.833</td><td>41</td><td>0.204</td><td>0.047194061</td><td>0.056114225</td><td>0.037225992</td></tr><tr><td>6-Dimitris Koufontinas (DK*)</td><td>10</td><td>20.817</td><td>33</td><td>0.319</td><td>0.071133845</td><td>0.076903173</td><td>0.037212596</td></tr><tr><td>15-Savas Xiros (SX)</td><td>11</td><td>73.314</td><td>32</td><td>0.25</td><td>0.104142682</td><td>0.070114691</td><td>0.0371833</td></tr><tr><td>17-Fotis (Fo*)</td><td>6</td><td>3.121</td><td>37</td><td>0.207</td><td>0.050544048</td><td>0.061863212</td><td>0.0371424</td></tr><tr><td>10-Nikitas (Ni*)</td><td>6</td><td>3.121</td><td>37</td><td>0.207</td><td>0.050544048</td><td>0.061863212</td><td>0.0371424</td></tr><tr><td>3-Christodoulos Xiros (CX*)</td><td>11</td><td>23.814</td><td>32</td><td>0.342</td><td>0.074657644</td><td>0.07777342</td><td>0.034665621</td></tr><tr><td>21-Yiannis (Yi)</td><td>6</td><td>6.542</td><td>37</td><td>0.222</td><td>0.024447563</td><td>0.025742454</td><td>0.031620428</td></tr><tr><td>18-Thomas Serifis (TS)</td><td>6</td><td>2.977</td><td>42</td><td>0.192</td><td>0.051045426</td><td>0.053007751</td><td>0.02079457</td></tr><tr><td>9-Iraklis Kostaris (IK)</td><td>6</td><td>4.098</td><td>42</td><td>0.195</td><td>0.050538886</td><td>0.057009788</td><td>0.018059999</td></tr><tr><td>12-Patroclos Tselentis (PT)</td><td>6</td><td>0.917</td><td>42</td><td>0.212</td><td>0.042716851</td><td>0.047196148</td><td>0.017932102</td></tr><tr><td>11-Ojurk Hanuz (OH)</td><td>5</td><td>0</td><td>43</td><td>0.19</td><td>0.022090638</td><td>0.018807343</td><td>0.017253429</td></tr><tr><td>22-Yiannis Skandalis (YS)</td><td>5</td><td>0</td><td>43</td><td>0.19</td><td>0.022090638</td><td>0.018807343</td><td>0.017253429</td></tr><tr><td>4-Constantinos Karatsolis (CK)</td><td>3</td><td>0</td><td>49</td><td>0.103</td><td>0.032270328</td><td>0.036794374</td><td>0.013208241</td></tr><tr><td>5-Constantinos Telios (CT)</td><td>3</td><td>20</td><td>45</td><td>0.075</td><td>0.039143434</td><td>0.022725228</td><td>0.009663123</td></tr><tr><td>20-Vassilis Xiros (VX)</td><td>4</td><td>2.03</td><td>40</td><td>0.143</td><td>0.040051405</td><td>0.046611113</td><td>0.007686253</td></tr><tr><td>16-Sotirios Kondylis (SK)</td><td>1</td><td>0</td><td>52</td><td>0.032</td><td>0.010223008</td><td>0.004145296</td><td>0.002548613</td></tr><tr><td>19-Vassilis Tzortzatos (VT)</td><td>1</td><td>0</td><td>52</td><td>0.032</td><td>0.01703266</td><td>0.012435887</td><td>0.002214273</td></tr><tr><td>7-Dionysis Georgiadis (DG)</td><td>1</td><td>0</td><td>52</td><td>0.032</td><td>0.01703266</td><td>0.012435887</td><td>0.002214273</td></tr><tr><td>8-Elias Gaglias (EG)</td><td>1</td><td>0</td><td>65</td><td>0.01</td><td>0.019294346</td><td>0.004030658</td><td>0.002013481</td></tr><tr><td>Performance</td><td>0.801136</td><td>0.698863</td><td>0.761363</td><td>0.778409</td><td>0.761363</td><td>0.812500</td><td>0.823863</td></tr></table>

Table 10  
Ranking of members generated by each evaluator.

<table><tr><td>Ranking</td><td>Degree</td><td>Betweenness</td><td>Closeness</td><td>Eigenvector</td><td>PageRank</td><td>Hits</td><td>SNCSE</td></tr><tr><td>1</td><td>PS*</td><td>SX</td><td>SX</td><td>PS*</td><td>SX</td><td>PS*</td><td>PS*</td></tr><tr><td>2</td><td>CX*</td><td>PS*</td><td>PS*</td><td>CX*</td><td>PS*</td><td>AG*</td><td>AG*</td></tr><tr><td>3</td><td>SX</td><td>AG*</td><td>AG*</td><td>DK*</td><td>CX*</td><td>CX*</td><td>Sa*</td></tr><tr><td>4</td><td>AG*</td><td>CX*</td><td>CX*</td><td>AG*</td><td>AG*</td><td>DK*</td><td>An*</td></tr><tr><td>5</td><td>DK*</td><td>DK*</td><td>DK*</td><td>SX</td><td>DK*</td><td>SX</td><td>DK*</td></tr><tr><td>6</td><td>An*</td><td>CT</td><td>Yi</td><td>Yi</td><td>TS</td><td>Ni*</td><td>SX</td></tr><tr><td>7</td><td>IK</td><td>Yi</td><td>Ni*</td><td>Sa*</td><td>Ni*</td><td>Fo*</td><td>Fo*</td></tr><tr><td>8</td><td>Ni*</td><td>IK</td><td>Fo*</td><td>PT</td><td>Fo*</td><td>Sa*</td><td>Ni*</td></tr><tr><td>9</td><td>PT</td><td>Ni*</td><td>VX</td><td>Ni*</td><td>IK</td><td>IK</td><td>CX*</td></tr><tr><td>10</td><td>Sa*</td><td>Fo*</td><td>Sa*</td><td>Fo*</td><td>An*</td><td>An*</td><td>Yi</td></tr><tr><td>11</td><td>Fo*</td><td>TS</td><td>An*</td><td>An*</td><td>Sa*</td><td>TS</td><td>TS</td></tr><tr><td>12</td><td>TS</td><td>VX</td><td>IK</td><td>IK</td><td>PT</td><td>PT</td><td>IK</td></tr><tr><td>13</td><td>Yi</td><td>Sa*</td><td>TS</td><td>TS</td><td>VX</td><td>VX</td><td>PT</td></tr><tr><td>14</td><td>OH</td><td>PT</td><td>PT</td><td>OH</td><td>CT</td><td>CK</td><td>OH</td></tr><tr><td>15</td><td>YS</td><td>An*</td><td>OH</td><td>YS</td><td>CK</td><td>Yi</td><td>YS</td></tr><tr><td>16</td><td>VX</td><td>OH</td><td>YS</td><td>VX</td><td>Yi</td><td>CT</td><td>CK</td></tr><tr><td>17</td><td>CK</td><td>YS</td><td>CT</td><td>CK</td><td>OH</td><td>OH</td><td>CT</td></tr><tr><td>18</td><td>CT</td><td>CK</td><td>CK</td><td>CT</td><td>YS</td><td>YS</td><td>VX</td></tr><tr><td>19</td><td>DG</td><td>DG</td><td>DG</td><td>DG</td><td>EG</td><td>DG</td><td>SK</td></tr><tr><td>20</td><td>EG</td><td>EG</td><td>SK</td><td>SK</td><td>DG</td><td>VT</td><td>VT</td></tr><tr><td>21</td><td>SK</td><td>SK</td><td>VT</td><td>VT</td><td>VT</td><td>SK</td><td>DG</td></tr><tr><td>22</td><td>VT</td><td>VT</td><td>EG</td><td>EG</td><td>SK</td><td>EG</td><td>EG</td></tr></table>

who are linked to such individuals may also be associated with criminal groups. Sub-networks consisting of the highest-ranked individuals' ego networks could, therefore, be used as a base for broadening criminal group investigations.

The second application considered a public dataset of the Greek terrorist group November 17. This application proves that the SNCSE identifies efectively key individuals with an apparent low propensity and with a key position in the network. The SNCSE also underestimated efectively the importance of individuals with a medium propensity and without a key position in the network.

Regarding future research, the following extensions are of particular interest:

Developing a methodology to detect communities in the sub-networks constituting the ego networks of each of the n highest-ranked suspects. This would strengthen eforts to identify criminal groups.

• Incorporating the propensities to various types of group crimes into the newly proposed evaluator. This would enrich the information used in the node evaluation.

Using available information such as criminal causes, ofenses, date of the ofenses, frequency of ofenses, convictions, age, and sex, among others. Advanced machine learning techniques may be employed to better estimate Pcg based on the before-mentioned information.

![](/api/attachments/5Z8MK2QG/fulltext/images/fc07b90f809e4aab037bbcad6fdaa9a455e784ee8d935f070f8460d82146ad0b.jpg)

![](/api/attachments/5Z8MK2QG/fulltext/images/277139d9ba64f1ef919b9309791bcdcd07ca4d6bd28aa20735eeb63e292a39de.jpg)

![](/api/attachments/5Z8MK2QG/fulltext/images/ca46d5cf4800059b19c6c21d748320c56920097ebb0736d3934006244d982407.jpg)

![](/api/attachments/5Z8MK2QG/fulltext/images/6d453ccc2b5c855fe4292cd7f182e21f56c58ee6b62132a594c151c2e59c0c8a.jpg)

![](/api/attachments/5Z8MK2QG/fulltext/images/7dfed583730a4c378a1b5a5df11fbd4c3b92f0ecba4c9b23656318cc1ab226ba.jpg)

![](/api/attachments/5Z8MK2QG/fulltext/images/2bc2a0ddb1993e2e0b82c918ae161732ac817df0489567aa33e2d827dc1c3a2a.jpg)  
Fig. 9. Efectiveness test: Identification of leader role in the Greek terrorist group November 17.

## Acknowledgments

The authors gratefully acknowledge the support of the Santiagobased Complex Engineering Systems Institute (CONICYT PIA/BASAL AFB180003), the Anillo projectACT87 “Quantitative methods in security”, FONDEF project ID20I10230ANID and the Ph.D. program in Engineering Systems at the Universidad de Chile. The first author was the recipient of a CONICYT grant number 21120226 to pursue doctoral studies in Engineering Systems at the Universidad de Chile. The first author acknowledges the Criminal Analysis Unit of the Public Prosecutor's Ofice of Región del Biobío-Chile for the technical support and providing the dataset under a collaboration and internship agreement. The first author also acknowledges the financial support of Universidad del Bío-Bío by the Initiation Research Project2060204IF/I and Macro Facultad de Ingeniería by the ProjectING 2030 I+D 20-34.

The second author acknowledges financial support by FONDEF project ID16I10222 CONICYT.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.dss.2020.113405.

## References

[11. P V, Bindu P. Santhi Thilagam, Deepesh Abuia Discovering suspicious behavior ir multilayer social networks, Comput. Hum. Behav. 73 (2017) 568–582.

[2] Qing Cheng, Jincai Huang, Zhong Liu, Cheng Zhu, Evaluation method of efect from network attack considering node multi-property feature, Mechatronic Science, Electric Engineering and Computer (MEC), 2011 International Conference on, pages 1947–1952, IEEE, 2011.

[3] James S. Coleman, Social capital in the creation of human capital, Am. J. Sociol.

(1988) S95–S120.

[4] W. Antony, Dnes and Nuno Garoupa. Behavior, human capital and the formation of gangs, Kyklos 63 (4) (2010) 517–529.

[5] Troncoso Espinosa Fredy Humberto, Prediction of recidivism in thefts and burglaries using machine learning, Indian J. Sci. Technol. 13 (06) (2020) 696–711, https://doi.org/10.17485/ijst/2020/v13i06/149853 ISSN 0950–7051.

[6] Katherine Faust, George E. Tita, Social networks and crime: pitfalls and promises fo advancing the field, Ann. Rev. Criminol. 2 (1) (2019) 99–122.

[7] Lise Getoor, Christopher P. Diehl, Link mining: a survey, ACM SIGKDD Explor. Newslett. 7 (2) (2005) 3–12.

[8] R. Grassi, F. Calderoni, M. Bianchi, A. Torriero, Betweenness to assess leaders in criminal networks: New evidence using the dual projection approach, Soc. Networks 56 (2019) 23–32

[9] R.V. Hauck, H. Atabakhsb, P. Ongvasith, H. Gupta, Hsinchun Chen, Using coplink to analyze criminal-justice data, Computer 35 (3) (2002) 30–37 Mar.

[10] Brian Hayes, Computing science: connecting the dots, Am. Sci. 94 (5) (2006) 400–404.

[11] C. Irwin, C. Roberts, N. Mee, Counter terrorism overseas, Dstl Report, Dstl/ CD053271/1.1.2002

[12] Jon M. Kleinberg, Authoritative sources in a hyperlinked environment, J. ACM 46 (5) (September 1999) 604–632 (ISSN 0004-5411).

[13] L. Lev Davidovich Landau, E. Evgenii Mikhailovich Lifshits, The Classical Theory of Fields, volume 2, Butterworth-Heinemann, 1975.

[14] Mark A. Lauchs, Robyn L. Keast, Vy Le, Social network analysis of terrorist networks: can it add value? Pak. J. Criminol. 3 (3) (2012) 21–32.

[15] Hady W. Lauw, Ee-Peng Lim, Hweehwa Pang, Teck-Tim Tan, Social network discovery by mining spatio-temporal events, Comput. Math. Org. Theory 11 (2) (2005) 97-118.

[16] Lv Le, Hewei Yu, A new method for evaluating node importance in complex networks based on data field theory, Networking and Distributed Computing (ICNDC), 2010 First International Conference on, pages 133–136, IEEE, 2010.

[17] Wassily Leontief, Input Output Economics, Oxford University Press, 1986.

[18] Jasmien Lismont, Eddy Cardinaels, Liesbeth Bruynseels, Sander De Groote, Bart Baesens, Wilfried Lemahieu, Jan Vanthienen, Predicting tax avoidance by means of social network analytics, Decis. Support. Syst. 108 (2018) 13–24.

[19] Jean Marie McGloin, David S. Kirk, Social network analysis, Handbook of Quantitative Criminology, pages 209–224, Springer, 2010.

[20] Jefrey Scott McIllwain, Organized crime: A social network approach, Crime Law Soc, Chang, 32 (4) (1999) 301–323

[21] Nan He, Gan Wen-Yan, et al., Evaluate nodes importance in the network using data field theory, Convergence Information Technology, 2007. International Conference on, pages 1225–1234, IEEE, 2007.

[22] Lawrence Page, Sergey Brin, Rajeev Motwani, Terry Winograd, The Pagerank Citation Ranking: Bringing order to the web. Technical Report 1999–66. Stanford InfoLab. 1999 November. (Previous number = SIDL-WP-1999-0120).

[23] Jialun Qin, Jennifer J. Xu, Daning Hu, Marc Sageman, Hsinchun Chen, Analyzing terrorist networks: A case study of the global salafi jihad network, Intelligence and Security Informatics, pages 287–304, Springer, 2005.

[24] C.J. Rhodes, E.M.J. Keefe, Social network topology: a bayesian approach, J. Oper.

[25] Theodore W. Schultz, Investment in human capital, Am. Econ. Rev. 51 (1) (1961) 1–17.

[26] Muhammad Akram Shaikh, Wang Jiaxin, Investigative data mining: Identifying key nodes in terrorist networks, Multitopic Conference, 2006. INMIC’06. IEEE, pages 201-206. JEEE. 2006

[27] Robert Solow, On the structure of linear models, Econometrica (1952) 29–46.

[28] Malcolm K. Sparrow, The application of network analysis to criminal intelligence: An assessment of the prospects, Soc. Networks 13 (3) (1991) 251–274.

[29] Fredy Troncoso, Richard Weber, A novel approach to detect associations in criminal networks, Decis. Support. Syst. 128 (January 2020) 113–159, https://doi.org/10. 1016/j.dss.2019.113159.

[30] Renée C. van der Hulst, Introduction to social network analysis (sna) as an investigative tool, Trends Org. Crime 12 (2) (2009) 101–121.

[31] Véronique Van Vlasselaer, Cristián Bravo, Olivier Caelen, Tina Eliassi-Rad, Leman Akoglu, Monique Snoeck, Bart Baesens, Apate: A novel approach for automated credit card transaction fraud detection using network-based extensions, Decis. Support. Syst. 75 (2015) 38–48.

[32] Teng Wang, Yanni Han, Wu. Jie, Evaluate nodes importance in directed network using topological potential, Information Engineering and Computer Science (ICIECS), 2010 2nd International Conference on, pages 1–4, IEEE, 2010.

[33] Stanley Wasserman, Social network analysis: Methods and applications, Volume 8,

[34] Jennifer Xu, Byron Marshall, Siddharth Kaza, Hsinchun Chen, Analyzing and vi sualizing criminal network dynamics: A case study, Intelligence and Security Informatics, pages 359–377, Springer, 2004.

[35] Jennifer J. Xu, Hsinchun Chen, Crimenet explorer: A framework for criminal network knowledge discovery, ACM Trans. Inf. Syst. 23 (2) (April 2005) 201–226 (ISSN 1046-8188)

[36] Ahmad Zareie, Amir Sheikhahmadi, Mahdi Jalili, Mohammad Sajjad Khaksar Fasaei, Finding influential nodes in social networks based on neighborhood correlation coeficient, Knowledge-Based Systems, page 105580, 2020 (ISSN 0950- 7051).

Fredy Troncoso is Professor at the Department of Industrial Engineering of the Faculty of Engineering, Universidad del Bío-Bío, Chile since 2008. He is Industrial Engineer from University of Bío-Bío, Chile and holds a Phd. in Systems of Engineering, from University of Chile. Since 2014 he has been a professor of data mining in postgraduate courses and actively participates in applied research projects. His research interests include data mining, net mining, and artificial intelligence.

Richard Weber is Professor at the Department of Industrial Engineering of the Faculty of Physical and Mathematical Sciences, Universidad de Chile. From 1992 to 1998 he worked as data mining consultant for the company Management Intelligenter Technologien GmbH, Aachen in Germany before joining Universidad de Chile in 1999. Richard Weber was visiting professor at the University of Osaka in 1992, the University of Tokvo in 2003 the University of Alberta in 2006, KU Leuven, Belgium in 2013, University of Vienna in 2017, and Aachen University in Germany (2015, 2016, 2017, 2018, and 2019). His research interests include data mining, dynamic data mining, and computational intelligence. He is Associate Editor of the journals “Applied Soft Computing" and “Journal of the Operational Research Society" and serves on the editorial board of the journal “Intelligent Data Analysis". He is senior member of JEEE and member of ACM and INFORMS. Richard Weber holds a B.Sc. in Mathematics as well as a MS and a Ph.D., both in operations research. from Aachen University. Germany.
