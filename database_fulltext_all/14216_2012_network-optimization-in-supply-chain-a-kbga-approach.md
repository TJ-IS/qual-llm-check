---
otero_id: 14216
otero_key: "SCH353KA"
title: "Network optimization in supply chain: A KBGA approach"
authors: "A. Prakash; Felix T.S. Chan; H. Liao; S.G. Deshmukh"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.10.024"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Network optimization in supply chain: A KBGA approach

A. Prakash <sup>a</sup>, Felix T.S. Chan <sup>a,</sup>⁎, H. Liao <sup>b</sup>, S.G. Deshmukh <sup>c</sup>

<sup>a</sup> Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Hung Hom, Hong Kong

<sup>b</sup> College of Engineering, Industrial and Information Engineering, The University of Tennessee, USA

<sup>c</sup> Department of Mechanical Engineering, Indian Institute of Technology, Hauz Khas, New Delhi-110016, India

## a r t i c l e i n f o

Article history: Received 28 February 2011 Received in revised form 12 October 2011 Accepted 23 October 2011 Available online 26 October 2011

Keywords: Supply chain Knowledge Management Genetic Algorithm Knowledge Based Genetic Algorithm

## a b s t r a c t

In this paper, we present a Knowledge Based Genetic Algorithm (KBGA) for the network optimization of Supply Chain (SC). The proposed algorithm integrates the knowledge base for generating the initial population, selecting the individuals for reproduction and reproducing new individuals. From the literature, it has been seen that simple genetic-algorithm-based heuristics for this problem lead to and large number of generations. This paper extends the simple genetic algorithm (SGA) and proposes a new methodology to handle a complex variety of variables in a typical SC problem. To achieve this aim, three new genetic operators— knowledge based: initialization, selection, crossover, and mutation are introduced. The methodology developed here helps to improve the performance of classical GA by obtaining the results in fewer generations. To show the ef<sup>fi</sup>cacy of the algorithm, KBGA also tested on the numerical example which is taken from th literature. It has also been tested on more complex problems.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The current business environment is becoming increasingly uncertain, unpredictable, complex, and as a result, more and more competitive. Increased competition means that companies face the dual challenge of cutting costs while being more responsive to the customers [1]. The researchers and practitioners throughout the world realize that though there may be diverse and situation speci<sup>fi</sup>c solutions to the problems posed by these challenges, <sup>fl</sup>exibility has to be the essential feature of the tools to handle these changes. As competition and complexity has increased, Supply Chain Management (SCM) has emerged as an increasingly important issue for companies. A supply chain links design, sourcing, manufacturing, and logistics activities across organizations. The chain links suppliers and customers, beginning with the production of raw material by a supplier, and ending with the consumption of a product by the customer. In a supply chain, the <sup>fl</sup>ow of goods between a supplier and customer passes through several stages, and each stage may consist of many facilities [37]. In recent years, the supply chain network (SCN) design problem has been gaining importance due to increasing competitiveness introduced by the market globalization [2,3,4]. The network design problem is one of the most comprehensive strategic decision problems that need to be optimized for long-term ef<sup>fi</sup>cient operation of whole supply chain. It determines the number, location, capacity and type of plants, warehouses, and distribution centers to be used. It also establishes distribution channels, and the amount of materials and items to consume, produce, and ship from suppliers to customers. Most of supply chain network design problems can be reduced to capacitated facility location problem (CFLP) which is known to be NP-complete [16]; therefore, most of supply chain network design problems are NP-hard [34,43].

In the present article, a new algorithm, KBGA, has been proposed and shows the application of it in the SCN optimization problem. The SCN problem is a very complex problem and the decision making is also very dif<sup>fi</sup>cult for the managers. In this study, two objectives have been considered, those are 1) minimization of the total average cost per <sup>fi</sup>ll demand and 2) maximization of the demand <sup>fi</sup>ll rate. Both of the objectives are con<sup>fl</sup>icting in nature, therefore a pareto optimal front has been achieved by applying KBGA. In the KBGA, the knowledge of the human being has been considered for the improvement of quality of solution. The knowledge base has helped in four stages of the algorithm: initialization, selection, crossover, and mutation. With the help of knowledge base, all these steps provide the improved solution within very few generations. To show the ef<sup>fi</sup>cacy of the proposed algorithm over Simple GA (SGA), a bench mark problem from the literature has been taken and it is also tested on the few moderate size of the problems.

The remainder of this paper is described as following: Section 2 presents the literature review of supply chain network optimization and employment of genetic algorithm in it. Section 3 delineates the complexity of the problems whereas the mathematical model has been described in Section 4. Section 5 describes the background of Simple GA (SGA). The role of knowledge management has been revealed in Section 6. The proposed algorithm knowledge based genetic algorithm (KBGA) has been discussed in Section 7 and the detailed procedure of KBGA has been portrayed in Section 8. Section 9 illustrates the Numerical analysis of the given problem by using the proposed algorithm. In Section 10, the paper has been concluded with some issues and future scope of the research.

## 2. Literature review

In literature, there are different studies dealing with the design problem of supply networks and these studies have been surveyed by Erenguc et. al. [19], and Pontrandolfo and Okogbaa [35]. In traditional SCM, the focus of the integration of SCN is usually on single objective such as minimum cost or maximum pro<sup>fi</sup>t [5,39,40]. These approaches are involved in tackling the various components of costs or the tradeoffs between those components. Amiri [5] has presented a lagrangian relaxation approach to minimize the total cost of two stage supply chain. Costa et al. [13] have worked on three stage supply chain network optimization problem. The objective of the research is to minimize the total cost of supply chain. Recently, multi objective optimization of SCNs has been considered by different researchers in literature [9,11,12]. Chan et.al. [10] developed a hybrid approach based on Genetic Algorithm (GA) and Analytic Hierarchical Process (AHP) for production and distribution problems in multifactory supply chain models. Guillen et al. [24] have worked on multi-objective supply chain network designing problem. They employed a branch and bound algorithm and the objectives are pro<sup>fi</sup>t of supply chain and customer service. Whereas Altiparmak et al. [4] have considered total cost, customer service and capacity utilization to design a supply chain network. Shen and Qi [38] proposed an integrated stochastic supply chain design model that takes into consideration the location, inventory and routing costs. They considered a three-tiered supply chain system consisting of one or more suppliers, distribution centers and customers with uncertain demand that follows a certain probability distribution. Inventory holding costs and transportation costs were assumed to exhibit economies of scale Cardona-Valdes et al. [8] have presented a study of multi-echelon supply chain network designing problem and they have considered the economical aspect with customer service level Prakash and Deshmukh [36l have also presented an approach to allocate the warehouse to the customers. They have also taken as a multi-criteria problem by considering transportation time and transportation cost.

Due to the complexity of the problem, various researchers are attracted towards the application of GA [6,17,21]. A hierarchical combination of mixed-integer programming and a genetic algorithm has been proposed in Truong and Azadivar [44] to determine simultaneously the values of quantitative as well as policy variables. Altiparmak et al. [3] have also applied the GA to solve such problem with three objectives: minimization of total cost, maximization of customer service, and maximization of capacity utilization. Farhani and Elahipana [20] have also applied GA for distribution network optimization. They considered two objectives: minimization of costs and minimization of the backorders. Gen et al., [22] have proposed a GA based approach to cope with network multiple objective problems. Lee et al. [27] have also applied the GA for the optimization of reverse logistics network problem.

From the aforementioned literature review, it has been seen that the researchers are concerned about the customer satisfaction i.e. to ful<sup>fi</sup>ll the demand within time and decrease the cost. Therefore, these two objectives are also considered in the present study. The SCN optimization is a complex problem, so many researches are intended to application of GA in SCN problem but still it needs more exploration. Most of the researchers have concentrated on the improvement of the supply chain performance and very few have considered the performance improvement of the algorithm concurrently. Keeping in mind the same, the present study give an outlook over both the objectives: performance improvement of supply chain and performance improvement of algorithm. If the improved algorithm will be applied, the quality of the solution will be better within lesser time. The present paper proposes a new algorithm which has the inherent search capability of GA with the power of knowledge and it is known as Knowledge Based Genetic Algorithm (KBGA). KBGA uses both the tacit and explicit knowledge.

## 3. Problem description

In supply chain network designing problem, logistic cost form the major part of a supply chain's costs. Inventory control and distribution planning, as fundamental logistical processes, affect the total costs of the supply chain to a great extent, but, on the other hand, have a great effect on the customers' demand <sup>fi</sup>ll rate. Every supplier should deliver the right amount of goods, at the right time, and to the right place. The detailed problem has been described as following.

In the present research, a case study has been taken into the consideration to show the complexity of the network optimization problem in supply chain. This problem is identical as considered by Ding et al. [18]. In this case there is a supply chain for “Classic” boots of an Italian textile company. The company outsourced production to outside contractors and it focuses only on marketing issues. For the actual situation, the product is made by a unique supplier in Vietnam (Supplier 1). Boots are then collected in containers and transported by boat from Hochimin harbor to Genova harbor. From Genoa, boots are transported by trucks to the central warehouse near Ferrara, where they are stored. The product is then distributed to the retailers of the Italian market. The network is shown in Fig. 1 with the available transportation links.

The main objective to solve such supply chain network optimization problem is to evaluate the selection of different suppliers or set of the suppliers and transportation links simultaneously, whereas the performance criteria are the total cost and demand <sup>fi</sup>ll rate. Simultaneously, this study also satis<sup>fi</sup>es some other goals like the impact of the performance by demand variation and the impact of inventory policy changing. From the <sup>fi</sup>gure, supplier 1 is the actual or existing supplier which is situated in Vietnam and one of the new or proposed suppliers (supplier 2) is in the Far East whereas supplier 3 is in the East Europe and the last one (supplier 4) is the local supplier i.e. that is situated in Italy itself. In this study, to evaluate the total cost, six different costs have been taken into consideration. These costs are the engagement cost, purchasing cost, transportation cost, inventory holding cost, ordering cost and penalty cost due to un<sup>fi</sup>lled demand of the orders. The cost provided from all the suppliers and duties according to their physical situations are given in Table 1. From the table, it is clearly shown that supplier 2 provides the boots at the lowest cost. The transportation features are provided in Table 2. Table 2 shows the transportation lead time and cost for each transportation link. From the table, it can be said that the transportation cost of supplier 4 is less than any other supplier, whereas supplier 2 has the more transportation cost. Supplier 3 and supplier 4 are more responsive because they are closer to the central warehouse. Only one transportation mode, using trucks, is provided for each of them. For both the suppliers, the supply lead-time is very short, but on the other hand, the price is much higher than that of the two suppliers from Far East.

![](/api/attachments/SCH353KA/fulltext/images/b4b3839e62dff2e6aa83c42c66900ecae3516e01c449418c133fbf5fe297f8ad.jpg)  
Fig. 1. Potential suppliers and transportation modes.

Table 1  
Parameters for suppliers.

<table><tr><td>Supplier ID</td><td>Engagement cost</td><td>Price per pair</td><td>Duties</td><td>Supply lead-time (day)</td><td>Min. order size (pair)</td></tr><tr><td>1</td><td>0</td><td>12.0</td><td>10%</td><td>15.0</td><td>1000</td></tr><tr><td>2</td><td>100000</td><td>10.0</td><td>20%</td><td>20.0</td><td>1000</td></tr><tr><td>3</td><td>80000</td><td>14.0</td><td>0</td><td>10.0</td><td>500</td></tr><tr><td>4</td><td>100000</td><td>16.0</td><td>0</td><td>8.0</td><td>500</td></tr></table>

The mathematical modeling of the abovementioned problem has been delineated in the next section.

## 4. Mathematical modeling

In the present problem of supply chain network optimization, the objective is to assign the suppliers and their transportation link in such a manner which can ful<sup>fi</sup>ll the demand at optimum cost. The mathematical model including notations, parameters, and objective functions with constraints is as follows:

## 4.1. Notations

i Supplier's index (1,2,3…..n)

j Transportation links' index (1, 2, 3….m)

k Number of days

o Number of orders

## 4.2. Parameters

$C _ { E n g }$ Total Engagement Cost

$C _ { I n v }$ Total Inventory Cost

C<sub>Pur</sub> Total Purchasing Cost

$C _ { O r d }$ Total Ordering Cost

$C _ { T r a n s }$ Total Transportation Cost

d Mean of Daily demand quantity

$D _ { T o t a l }$ Total demand of items

$D _ { L o s t }$ Total Lost Demand

$P C _ { L }$ Total Penalty Cost on lost demand

p penalty cost per item

$e c _ { i }$ engagement cost for ith supplier

$N _ { p u r _ { 1 } }$ Number of items purchased from ith supplier

$U C _ { i }$ Unit purchasing cost (determined by ith supplier)

Table 2

Parameters for transportation links.

<table><tr><td rowspan="2">ID</td><td rowspan="2">Transport modes</td><td colspan="3">Transportation lead-time</td><td>Unit cost</td></tr><tr><td>Distribution type</td><td>Mean (day)</td><td>Std. dev. (day)</td><td>Per pair</td></tr><tr><td>L1-1</td><td>Boat + truck</td><td>Normal</td><td>20</td><td>1</td><td>0.5</td></tr><tr><td>L1-2</td><td>Boat + plane + truck</td><td>Normal</td><td>8</td><td>0.8</td><td>2.0</td></tr><tr><td>L1-3</td><td>Plane + truck</td><td>Normal</td><td>5</td><td>0.5</td><td>4.0</td></tr><tr><td>L2-1</td><td>Boat + truck</td><td>Normal</td><td>25</td><td>2</td><td>0.5</td></tr><tr><td>L2-2</td><td>Boat + plane + truck</td><td>Normal</td><td>10</td><td>1</td><td>2.0</td></tr><tr><td>L2-3</td><td>Plane + truck</td><td>Normal</td><td>5</td><td>0.5</td><td>4.0</td></tr><tr><td>L3</td><td>Truck</td><td>Constant</td><td>4</td><td>0</td><td>1.0</td></tr><tr><td>L4</td><td>Truck</td><td>Constant</td><td>2</td><td>0</td><td>0.2</td></tr></table>

$N _ { k }$ Inventory of items per day

h Holding cost per item per day

$n _ { o i }$ Number of orders placed to ith supplier

$o c$ Ordering cost per order

$T R _ { i j }$ Number of transshipped items from jth transportation link of ith supplier

$t c _ { i j }$ Transportation cost per item from jth transportation link of ith supplier

$O R _ { \mathrm { { s u p } } }$ Order placed to ith supplier

$L B _ { \mathrm { s u p _ { i } } }$ f lower bound limit of order placed to ith supplier (minimum number of items ordered)

## 4.3. Objectives

The objectives are to minimize the total average cost per <sup>fi</sup>ll demand and maximize the demand <sup>fi</sup>ll rate. The mathematical formulation for both the objective function is given below

$$
\operatorname{Min} f _ {1} = \frac {\left(C _ {E n g} + C _ {P u r} + C _ {O r d} + C _ {T r a n s} + C _ {I n v} + P C _ {L}\right)}{\left(D _ {\text { Total }} - D _ {\text { Lost }}\right)}\tag{1}
$$

$$
M a x f _ {2} = \frac {(D _ {T o t a l} - D _ {L o s t})}{D _ {T o t a l}}.\tag{2}
$$

To calculate the <sup>fi</sup>rst objective, the individual cost can be calculated as follows:

$$
C _ {E n g} = \sum_ {i} e c _ {i} ^ {*} z _ {i} \quad \forall i\tag{3}
$$

$$
C _ {P u r} = \sum_ {i} N _ {p u r _ {i}} * U C _ {i} \quad \forall \mathrm{i}\tag{4}
$$

$$
C _ {O r d} = \sum_ {i} \sum_ {o} n _ {o i} ^ {*} o c ^ {*} y _ {o i} \quad \forall o, i\tag{5}
$$

$$
C _ {T r a n s} = \sum_ {i} \sum_ {j} T R _ {i j} ^ {*} t c _ {i j} ^ {*} x _ {i j} \quad \forall i, j\tag{6}
$$

$$
C _ {I n v} = \sum_ {k} N _ {k} * h \quad \forall k\tag{7}
$$

$$
P C _ {L} = D _ {L o s t} * p\tag{8}
$$

Which are subjected to:

$$
\sum_ {i} O R _ {\sup _ {i}} \geq D _ {T o t a l}\tag{9}
$$

$$
O R _ {\sup _ {i}} \geq L B _ {\sup _ {i}} \quad \forall i\tag{10}
$$

$$
O R _ {\sup _ {i}} = \sum_ {j} T R _ {i j} * x _ {i j} \quad \forall j\tag{11}
$$

$$
\sum_ {i} \sum_ {j} T R _ {i j} * x _ {i j} \geq D _ {T o t a l} \quad \forall \mathrm{i}, \mathrm{j}\tag{12}
$$

$$
x _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if   jth   transportation   link   of   ith   supplier   is   activated } \\ 0 & \text { otherwise } \end{array} \right.\tag{13}
$$

$$
y _ {o i} = \left\{ \begin{array}{l l} 1 & \text { if   oth   order   is   placed   to   ith   supplier } \\ 0 & \text { otherwise } \end{array} \right.\tag{14}
$$

$$
z _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   ith   supplier   is   engaged } \\ 0 & \text { otherwise } \end{array} \right.\tag{15}
$$

$$
k, o, p, N _ {k}, L B _ {\sup _ {i}} \geq 0.\tag{16}
$$

The <sup>fi</sup>rst objective function (Eq. (1)) is to minimize the average of all the incurred cost. The last cost component is the penalty cost which will be incurred for failing to meet demand.

The second objective function (Eq. (2)) is to maximize the demand <sup>fi</sup>ll rate i. e. the lost demand should be minimize.

Eqs. (3) to (8) show the formulation of different costs like engagement cost, purchasing cost, ordering cost, transportation cost, and inventory cost. The novelty of this mathematical model is to penalize on each lost demand. The penalty cost has been stated in mathematical form in Eq. (8).

The constraints are given in Eqs. (9) to (16). Eq. (9) shows that the order placed to the supplier should not be less than demand of the customers whereas Eq. (10) illustrates that the order placed to an individual supplier should not be less than a minimum number of items or lower bound of the order. The total number of transshipped items from all the transportation links of a supplier should be equal to the order placed to that supplier and it should be more than total demand of customers. These constraints have been modeled mathematically in Eqs. (11) and (12). Finally, constraints in Eqs. (13)–(15) enforce the binary nature of the con<sup>fi</sup>guration decisions while Eq. (16) imposes the non-negativity restriction of the decision variables corresponding to transshipment, orders etc.

## 5. Background of SGA

Simple GA is an ‘intelligent’ probabilistic search algorithm that simulates the process of evolution by taking a population of solutions and applying genetic operators in each reproduction. Each solution in the population is evaluated according to some <sup>fi</sup>tness measure. Fitter solutions in the population are used for reproduction. New ‘off spring solutions are generated and un<sup>fi</sup>t solutions in the population are replaced. The cycle of evaluation–selection–reproduction is continued until a satisfactory solution is found [23,29]. Holland [25] <sup>fi</sup>rst described a GA, which is commonly called the Classical GA (CGA). The working of the CGA can best be understood by the following steps, which are shown in Fig. 2.

Step 1 Generate the initial population. Determine the size of the population and the maximum number of the generation.

Step 2 Calculate the <sup>fi</sup>tness value of each member of the initial population.

Step 3 Calculate the selection probability of each member of the initial population using the ratio of <sup>fi</sup>tness value of that initial population to the summation of the <sup>fi</sup>tness values of the individual solutions.

Step 4 Select a pair of members (parents) that can be used for reproduction using selection probability.

Step 5 Apply the genetic operators such as crossover, mutation, and inversion to the parents. Replace the parents with the new off-spring to form a new population. Check the size of the new population. If it is equal to the initial population size, then go to step 6, otherwise go to step 4.

Step 6 If the current generation is equal to the maximum number of the generation then stop, else move to step 2.

After searching a large amount of the literature in the area of GA application in supply chain, it has been found that there is a need of more exploration of this are in the research. This research intends to demonstrate the advantage of Knowledge Management in GA applications in the area of the network optimization problem of supply chain that is known for its computational complexity.

## 6. Background of KM

As Francis Bacon, an English philosopher, said, “Knowledge is power”. To learn new things, maintain valuable heritage, create core competences, and initiate new situations, the power of knowledge is a very important resource for both individual and organizations now and in the future. According to Nonaka [31], Knowledge has been de<sup>fi</sup>ned as “justi<sup>fi</sup>ed true belief” that increases an organization's capacity for effective action. It has two dimensions: explicit and tacit knowledge. Davenport and Prusak [15] de<sup>fi</sup>ne knowledge as a <sup>fl</sup>uid mix of framed experience, values, contextual information, and expert insight that provides a framework for evaluating and incorporating new experiences and information. They suggest that it originates and is applied only in the mind of knower and holders of tacit knowledge in organizations. It is embodied in documents, repositories, organizational routines, processes, practices and norms. To respond to competitive challenges, otherwise-independent <sup>fi</sup>rms have become more closely coupled than in the past, often working in parallel to complete assignments spanning traditional boundaries and functional areas. Knowledge Management (KM) provides processes to capture a part of tactic knowledge through informal methods and pointers and fairly high percentage of explicit knowledge, reducing the loss of organizational knowledge [32].

![](/api/attachments/SCH353KA/fulltext/images/4fca89336762fd40bc2e5df4c18994f6d13d59d8fdfa326b087731e4c8606f0e.jpg)  
Fig. 2. Flowchart of Simple Genetic Algorithm (SGA)

“KM is the formalization of and access to experience, knowledge and expertise that create new capabilities, enable superior performance, encourage innovation and enhance customer value” [7]. According to Tiwana [41], Knowledge Management is the ability to create and retain greater value from core business competencies. Beckman [7] realizes that Knowledge Management is the systematic, explicit, and deliberate building, renewal, and application of knowledge to maximize an enterprise's knowledge-related effectiveness and returns from its knowledge assets. Whereas, Tiwana and Balasubramanyam [42] feel that Knowledge Management addresses business problems particular to business—whether it's creating and delivering innovative products or services or managing and enhancing relationship with existing and new customers, partners, and suppliers, or administrating and improving work practices and processes. Nietok [30] examines that knowledge has a connotation of ‘potential for action’ and is different from information in terms of its more immediate link with performance. It is linked to the values and experience of the user, and therefore takes many forms. One may have knowledge of certain facts. Meiller et al. [28] observed that there are four components of a knowledge base system: learning, simulation, problem solving and evaluation. They have used it for healthcare system. A KM strategy can help tear down traditional cross functional boundaries. KM entails helping people share and put knowledge into action by creating access, context, infrastructure, and simultaneously reducing learning cycles [14,15,33].

In the present paper, the knowledge based tool is motivated by the ideas proposed by Wadhwa and Saxena [45]. The creation of today's knowledge base requires blending of knowledge from diverse disciplinary and personal skills based on perspectives where creative cooperation is critical for innovation. An integrated framework of KM has been shown in Fig. 2. It shows the conversion of information to knowledge and integration of knowledge base with knowledge utilization. To convert the information to knowledge, the process follows the various activities as veri<sup>fi</sup>cation, acquiring the <sup>fi</sup>ltered information, classi<sup>fi</sup>cation and creation of the knowledge from this information. All the acquired knowledge is stored in the knowledge base. After accumulation, the knowledge has been distributed to the knowledge users by following the steps like adaptation, attraction, engaging the people and teaches them how to use this knowledge. The knowledge synergy based thinking showed in Fig. 3 can signi<sup>fi</sup>- cantly bene<sup>fi</sup>t the KM guided manufacturing endeavors.

## 7. Proposed Knowledge Based Genetic Algorithm (KBGA)

Although GA is a global search technique, its practical usefulness depends on the initialization of the problem, crossover and mutation techniques and selection scheme for the next generation. Therefore, a number of techniques have been developed for handling all the above constraints. In the network optimization problem of supply chain, various researchers have explore the application of GA to improve the system performance but very few researchers have worked on the improvement of supply chain performance as well as algorithm performance.

In the present paper, we have introduced a concept of improving the performance of GA by exercising the knowledge based system, which will develop a faster algorithm for better performance of the system. It will employ on the basis of both tacit and explicit knowledge. For a search stratagem, it is very essential that it should also handle the inherent characteristics and complexities of the environment. By employing the knowledge of the environment like supply chain and the complexities, i.e. <sup>fl</sup>exibilities, we can get the better result within lesser time than SGA. As it works with the knowledge base, it is identi<sup>fi</sup>ed as KBGA. The proposed algorithm works not only for improving the performance measures of the system like traditional GA but the performance of the algorithm (Fig. 4). To enhance this idea, the knowledge based initialization, knowledge based crossover, knowledge based mutation, and knowledge based selection have also been incorporating in the algorithm. The procedure of the algorithm has been described in the next section.

## 8. Procedure of KBGA for Network Optimization Problem

As stated in the previous section, it is clear that the strong point of KBGA over SGA is the knowledge based generation of the initial population instead of random generation. It is followed by the knowledge based selection (KBS), Knowledge based crossover (KBC), and Knowledge based mutation (KBM) to provide the wider search space within lesser time. The full procedure of KBGA has been shown in Figs. 5–8. All the steps of the proposed algorithm (KBGA) are as follows:

## 8.1. Knowledge based initialization (KBI)

In the <sup>fi</sup>rst step of the algorithm, an initial population set of the solutions has been generated on the basis of the knowledge based system. In this step, <sup>fi</sup>rstly the information related to the system environment like (supply chain structure, types of transportation links etc.), suppliers (location, unit price, lead time, minimum order size etc.), transportation (mode, transportation lead time, cost etc.), demand, inventory policy has been collected and <sup>fi</sup>ltered.

After that the performance measures, on which the system concentrates, and the requirements have been decided. After this decision making, the existing network has been evaluated with some best known alternatives on the basis of performance measures. This depends on the knowledge of network manager, supply chain managers. The tacit and explicit types of knowledge will be used for this evaluation. After evaluation all the practiced alternatives, the best alternative will be selected and it will be the <sup>fi</sup>rst solution or the starting point of the algorithm. This will be collected in the knowledge base. Therefore, the initial seed is already improved; the later generation will give the better results within lesser generation or converged to the better results in lesser generations.

![](/api/attachments/SCH353KA/fulltext/images/a4c30326217fb868a0628c33c22446b10cd3500038de884042c97dc8fc6113e2.jpg)  
Fig. 3. An integrated framework of Knowledge Management.

![](/api/attachments/SCH353KA/fulltext/images/f0a565358c43e8e5008df17707bb55646030feecc36dbfb4f1c7e4a9eb3aeb3c.jpg)  
Fig. 4. Flowchart of KBGA.

The knowledge base provides the initial population for the proposed algorithm. Thus, here all the constraints related to the system or problem has been taken into the consideration. Hence, it can be said that the seed of initial population will work better than randomly generated population. After getting the initial population, the evaluation process is started and it is described in the next section.

For initialization, various information is needed and on the basis of these information, the chromosome is formed. For example, the supplier information will show about how many suppliers are considered and the engagement cost is also known for each supplier. The location is also a very important information as the taxes or duties are decided on the basis of location of the supplier. The information of the available transportation modes at each supplier with the cost is also important, whereas the demand information is also important to form a chromosome. The structure of chromosome is identical as taken by Ding et al. [18]. The chromosome will be represented as in Fig. 6.

From Fig. 6, it is clear that <sup>fi</sup>rst four variables are shown for supplier means if one is selected put 1 otherwise 0. Whereas next 8 variables are for the weight allocated to the various transportation modes. In the last two columns, the reorder point and demand quantity for the selected supplier is represented.

## 8.2. Evaluation

In this step, each sequence has been calculated according to the evaluation criteria, which is a problem speci<sup>fi</sup>c function. In the real world state of affairs, several objectives work at the same time. Thus, the proposed algorithm provides the facility to specify several objectives. The user can specify the relative weighted average for each objective. In the proposed algorithm (KBGA), the knowledge based system is highly ef<sup>fi</sup>cient for sustaining the solution feasibility. In the present study, there are two objectives have taken into consideration. Those are total cost and demand <sup>fi</sup>ll rate. Both are con<sup>fl</sup>icting in nature. Therefore a pareto front has been considered to satisfy both objectives.

## 8.3. Knowledge based selection (KBS)

After the evaluation of all the sequences, a subset of the initial population is selected on random basis. It works on the basis of Darwinism “Survival of the Fittest” but not as a greedy algorithm. In KBGA, the selection is also affected by the knowledge base system to improve the performance of the algorithm.

In this algorithm, the selection is based on Neo Darwinism [26], which can sub-divide the procedure of selection of three categories: a) Directional selection, b) Steady selection and c) Unruly selection. The directional selection is based on the mean value (increasing or decreasing both) of the population whereas steady selection, which is based on normalizing, eliminates the chromosomes with excessive values. It is called steady selection due to provide the steady state search space. The chromosomes are eliminated according to the moderate values in unruly selection. To execute all three types of selection, there are several methods of the selection e.g. tournament selection, roulette wheel selection, logarithmic scales selection etc.

In the knowledge base system, all types of selection schemes with their characteristics and their performance in different systems have been placed. According to this knowledge, the suitable selection scheme has been applied for the selection of a subset of the initial population for the next stage of the algorithm.

## 8.4. Knowledge based crossover (KBC)

Following the KBS, the surviving chromosomes are selected to form the new off springs to explore the wider search space. The knowledge based crossover gives the inherent characteristics to the off springs from parents. Initially, a sub-set of survived chromosomes has been randomly selected according to the crossover probability. To perform the crossover, there are several crossover schemes e.g. single point crossover, partial mapping crossover, uniform crossover, cycle crossover etc. with some speci<sup>fi</sup>c characteristics.

The characteristics of each crossover scheme and their performance for different types of system environments and problems have been kept in the knowledge base and it will be updated as increasing the knowledge. The tuning of the crossover probability is also a concern in the proposed algorithm. The performance of the system for the different environments at the various crossover probabilities has been captured and placed in the knowledge base. Another facility to check the unfeasible new offspring has been provided to the user. If any parent reproduce an unfeasible solution that will be checked and discarded with the help of knowledge base system.

## 8.5. Knowledge based mutation

Following the above step, the next genetic operator, named as mutation, empowers the algorithm to explore the search space. It modi<sup>fi</sup>es single chromosome by altering the genes or bits instead of recombining the two chromosomes. In the proposed algorithm, a knowledge base has been created to store the knowledge about the performance of various mutation operators e.g. inversion, insertion, displacement etc. in the different system environments with a variety of objective function. It also has the knowledge about the outcomes with the different ranges of the mutation probability. According to Michalewicz (1992), the selection of the appropriate value of the mutation probability is an art not a science. Hence, it is cleared now that knowledge (explicit or implicit) can help to determine the value of genetic parameter (Fig. 9).

![](/api/attachments/SCH353KA/fulltext/images/90ae988cb1b795186aeaaa140d70970672e6c2b40f4251faee93321079484ecb.jpg)  
Fig. 5. Initialization process of KBGA.

## 8.6. Termination criteria

After mutation, the selected populations, equal to the size of initial population, have to be entered to the next generation out of the extended population of the chromosomes. The whole process will be repeated until satisfy the termination criteria. The termination criteria can be characterized by the number of generations or the prede-<sup>fi</sup>ned level of the output.

![](/api/attachments/SCH353KA/fulltext/images/de4afdbe5830a1c4d8b0846718cac6a84123f32df16110d5dcda6507f9c39aa9.jpg)  
Fig. 6. Representation of chromosome.

## 9. Numerical analysis

In the present study, a supply chain network optimization problem has been addressed and due to much complexity it is solved by the improved version of genetic algorithm which is having the power of knowledge also. This algorithm is known as knowledge based genetic algorithm and it is employed for supply chain network optimization. As the real world problem, the demand is uncertain and it follows the normal distribution. The main objective of the present study is the demand satisfaction or demand <sup>fi</sup>ll rate and unit cost; both of these objectives are con<sup>fl</sup>icting in nature, therefore a pareto front has been achieved which shows the various optimal point according to the weights. The engagement cost has been introduced the cost of contract negotiation. For economies of scale, there is minimum order size has been set out by each supplier. It is also assumed that the order has been directly given to the suppliers. A supplier can refuse the order if it is less than the minimum order size. Another novelty of this study is that the penalty cost for the lost demand has also been considered.

![](/api/attachments/SCH353KA/fulltext/images/4bb51a0f1b965677dbb6c1285fc2f80e1b1ed8ab92b1c26088b7d4a285bc2c31.jpg)  
Fig. 7. Knowledge based selection.

![](/api/attachments/SCH353KA/fulltext/images/57dee2586d988a90f3ad25840abc21e1360628838b583703b00438e69dc0c0c9.jpg)  
Fig. 8. Knowledge based crossover.

As the problem statement is identical as considered in Ding et al. [18]. Therefore the demand is 300 pairs of boots. Initially the penalty cost has not been considered and compared it with the results addressed from Ding et al. [18]. The results obtained from SGA [18] have been shown in Fig. 10.

The results obtained from KBGA have been shown in Fig. 11, without considering the lost sales penalty. It shows the smoothness of the curve and it delineates that after reaching beyond the 98.5% of <sup>fi</sup>ll rate, the unit price will almost be the same. Therefore, it will try to improve the suppliers' service also.

The ef<sup>fi</sup>cacy of KBGA has been shown in the results. The convergence rate is also faster as in SGA it converges in 2000 generations [18] whereas in KBGA it converges only in 144 generations.

The results are also obtained for with lost sales penalty and shown in Fig. 12. The <sup>fi</sup>gure shows that after considering the lost sales penalty the unit price is comparatively very high and in this case it will be very near to real world situation.

Several important solutions have been summarized in Table 3. From the table, it can be said that the results can be classi<sup>fi</sup>ed in two categories: solutions up to the demand <sup>fi</sup>ll rate 95.8% select the same supplier portfolio i.e. S2 and S3 whereas solutions below demand <sup>fi</sup>ll rate 95% there is need of only one supplier S2. The study shows that the supplier S2 is an ef<sup>fi</sup>cient supplier. Whereas, SGA search the results only up to 97.2% of demand <sup>fi</sup>ll rate with multiple suppliers. The reorder point is also lower in the solution achieved by KBGA. The order quantity is also lower than results suggested by SGA. Therefore, it affects the inventory cost of the supply chain and makes an effort to mitigate the effect of high inventory and make the lean supply chain also. On the other hand, it is clear that as the demand <sup>fi</sup>ll rate decreases, the reorder point is decreased and order quantity is increased. It also lessens the inventory but lost the sale simultaneously. Therefore, the lesser inventory is not always justi<sup>fi</sup>ed as it is also the cause of lost sale and it increases the cost as the penalty of lost sales. From the table, it can be concluded that multiple suppliers are bene<sup>fi</sup>cial for more demand <sup>fi</sup>ll rate as unique supplier is bene<sup>fi</sup>cial only below 95.8% of demand <sup>fi</sup>ll. The justi<sup>fi</sup>cations of the advantages of selecting the multiple suppliers are also shown from the other results also in Table 3.

![](/api/attachments/SCH353KA/fulltext/images/c88cd700df24b695b03569e398f7095a3fc5be63c4bf2ab266a0a9941a71ed13.jpg)  
Fig. 9. Knowledge based mutation

![](/api/attachments/SCH353KA/fulltext/images/6c52ef7b8aa7fe8c7dbe2cb2578ca439168046956f82599159b2968f452dfd6b.jpg)  
Fig. 10. Results obtained from SGA. Adopted from Ding et al. 2006.

To show the ef<sup>fi</sup>ciency to handle the complex problem, the KBGA has also been tested on the more complex problems i.e. with increasing demand. It has also tested on demand of 400 and 500. The obtained pareto fronts have been shown in Fig. 13. The convergence rate is also very fast. The algorithm has been converged only in 178 generations for demand of 400. For demand of 500, KBGA has been converged in 243 generations which shows the faster convergence rate.

From the above shown results, it can be scrutinized that the proposed algorithm (KBGA) is an ef<sup>fi</sup>cient algorithm for tackling the complex problems of supply chain. The power of knowledge has also been shown from the results on comparing with SGA. The study shows that KBGA provides the solution in less generation i.e. less time than SGA. The present study is enhanced the theoretical approach to solve such complex problem and numerical analysis shows that it can be worked for real supply chain problems with some amendments. The study is much intended to show the ef<sup>fi</sup>cacy of KBGA and the numerical results strengthen the above concept.

Pareto Front without lost sales penalty (d=300)  
![](/api/attachments/SCH353KA/fulltext/images/255e02a66062e74abd13b475eb98ed46f52b1818df7a1f2317b4f4e851ef06e0.jpg)  
Fig. 11. Pareto front obtained from KBGA without lost sales penalty (d=300).

![](/api/attachments/SCH353KA/fulltext/images/e8d605cd35b7c355ac851da49f83df390a63ed29f97abcb1e7b6c3675bdf89fb.jpg)  
Fig. 12. Pareto front obtained from KBGA with lost sales penalty (d= 300).

Various pareto solutions (d=300).

<table><tr><td>E1</td><td>E2</td><td>Supplier portfolio</td><td>Transportation allocation weights (%)</td><td>Reorder point</td><td>Order quantity</td></tr><tr><td>38.26</td><td>100</td><td>S2 + S3</td><td>L2 (14 + 25 + 33) + L3(28)</td><td>6273</td><td>1587</td></tr><tr><td>38.14</td><td>99.99</td><td>S2 + S3</td><td>L2 (17 + 19 + 36) + L3(28)</td><td>6142</td><td>1562</td></tr><tr><td>36.42</td><td>97.5</td><td>S2 + S3</td><td>L2 (28 + 15 + 29) + L3(28)</td><td>6085</td><td>1550</td></tr><tr><td>35.37</td><td>95.8</td><td>S2 + S3</td><td>L2 (32 + 12 + 28) + L3(28)</td><td>5322</td><td>1507</td></tr><tr><td>30.44</td><td>90.5</td><td>S2</td><td>L2 (38 + 23 + 49)</td><td>5536</td><td>1185</td></tr><tr><td>27.08</td><td>87.5</td><td>S2</td><td>L2 (38 + 21 + 41)</td><td>5283</td><td>1110</td></tr><tr><td>21.92</td><td>82.0</td><td>S2</td><td>L2 (42 + 19 + 38)</td><td>4892</td><td>1005</td></tr><tr><td>19.75</td><td>80.0</td><td>S2</td><td>L2 (46 + 19 + 35)</td><td>5227</td><td>1005</td></tr></table>

The proposed heuristic KBGA has been coded in C++ programming language and the experiment has been carried out on an IBM PC with a Pentium IV CPU −1.9 GHz processor. To sum up, for all the aforementioned results not only authenticate the supremacy of the proposed algorithm over existing heuristic but provide also a new dimension to the solution of complex combinatorial problems in real time.

## 10. Conclusion

The present paper provides a new insight to the practitioner to solve the different combinatorial problems e.g. network optimization in the supply chain context. The network optimization in the <sup>fl</sup>exible supply chain context is a very complex problem for the practitioners. Because the dynamics of a system comprising a huge number of more or less independently acting self-controlled entities within a network is hard to predict and evaluate in real operation, appropriate algorithm is required for this purpose. The proposed algorithm, KBGA, improves the performance of traditional GA through introducing the knowledge base system which includes both explicit and implicit knowledge. Therefore, the most signi<sup>fi</sup>cant contribution of this research is to develop new algorithm which is known as Knowledge Based Genetic Algorithm (KBGA) for improving the performance of supply chain. The proposed algorithm, KBGA, improves the performance of traditional GA through introducing the knowledge base system which includes both explicit and implicit knowledge. It mainly emphasizes on the initialization, selection and genetic operators. The effectiveness of the productivity of classical meta-heuristics based on knowledge rather than information is intended towards creating worthy knowledge and giving suf<sup>fi</sup>cient privileges to the same. This research can also be exploited to other multi objective problems with more <sup>fl</sup>exible attributes. In the new economy brought about by globalization, the fast changing nature of the technology warrants consideration for the formation of knowledge integration with such meta-heuristics. To show the ef<sup>fi</sup>cacy of the proposed KBGA, a comparative study has also been made with SGA. This study shows the faster convergence rate of KBGA with better quality solution. A knowledge-based view of the algorithm is necessary to understand the requirement of the real world attributes and vis-à-vis the algorithm capability.

Pareto fronts with lost sale penalty  
![](/api/attachments/SCH353KA/fulltext/images/d67e0b6508cae51eeae643a2b54d52bb46dd997dd13bbf495e522ce11a1d172a.jpg)  
Fig. 13. Pareto front obtained from KBGA with lost sales penalty (d=400 and 500).

This research has enlightened the domain of supply chain network optimization as it discusses about the commitment of faster delivery at minimum cost. The mangers can apply the solutions with providing more constraints accordance with the environment of the market and supply chain. The network optimization problem can also give a new vision to the managers of supply chain to achieve the solution in such a way that can ful<sup>fi</sup>ll the demand of the customer with minimum average cost per product. Therefore, it will provide a two dimensional approach at the same time. However, the conclusion that while particular improvement initiatives is bene<sup>fi</sup>cial towards certain performance dimension; it may negatively affect other performance measure underlines caution to the managers to be careful in selecting the improvement initiatives. This research provides a new insight about the optimization algorithms in theoretical manner but it can be employed in real industry problems also with some new constraints and the numerical analysis proved the same concept.

As a future scope, this research can be stretched out to various problems of the supply chain environment that cover the balancing or allocation of resources. This research can also be employed for the multi-criterion decision making problems in FMS environment as well as <sup>fl</sup>exible supply chain environment.

## Acknowledgments

The work described in this paper was substantially supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No. PolyU 510410). The authors also thank the editor and the reviewers for their valuable comments and suggestions that have led to the substantial improvement of the paper.

## References

[1] H. Akkermans, Emergent supply networks: system dynamics simulation of adaptive supply agents, Proceedings of the 34th Hawaii Int. Conference on System Sciences, 2001, pp. 2123–2126.

[2] F. Altiparmak, M. Gen, L. Lin, A genetic algorithm for supply chain network design Proceedings of the 35th International Conference on Computers and Industrial Engineering, 2005, pp. 111–116.

[3] F. Altiparmak, M. Gen, L. Lin, I. Karaoglan, A steady-state genetic algorithm for multi-product supply chain network design, Computers and Industrial Engineer ing 56 (2) (2009) 521–537.

[4] F. Altiparmak, M. Gen, L. Lin, T. Paksoy, A genetic algorithm approach for multiobjective optimization of supply chain networks, Computers and Industrial Engineering 51 (2006) 196–215.

[5] A. Amiri, Designing a distribution network in a supply chain system: formulation and ef<sup>fi</sup>cient solution procedure, European Journal of Operational Research 171 (2) (2006) 567–576.

[6] H. Aytug, M. Khouja, F.E. Vergara, Use of genetic algorithms to solve production and operations management: a review, International Journal of Production Researches 41 (17) (2003) 3955–4009.

[7] T. Beckman, A methodology for knowledge management, in: M.H. Harmza (Ed.), Proceedings of the IASTED Int. Conf. on AI and Soft Computing, ASC'97, Banff, IASTED ACT Press, 1997, pp. 29–32.

[8] Y. Cardona-Valdés, A. Alvarez, D. Ozdemir, A bi-objective supply chain design problem with uncertainty, Transportation Research Part C 19 (2011) 821–832.

[9] F.T.S. Chan, S.H. Chung, A multi-criterion genetic algorithm for order distribution in a demand driven supply chain, International Journal of Computer Integrated Manufacturing 17 (4) (2004) 339–351.

[10] F.T.S. Chan, S.H. Chung, S. Wadhwa, A hybrid genetic algorithm for production and distribution, Omega 33 (2004) 345–355.

[11] C. Chen, W. Lee, Multi-objective optimization of multi-echelon supply chain networks with uncertain product demands and prices, Computers and Chemical Engineering 28 (2004) 1131–1144.

[12] S. Chopra, P. Meindl, Supply Chain Management: Strategy, Planning and Operation, Prentice Hall, Upper Saddle River, USA, 2004.

[13] A. Costa, G. Celano, S. Fichera, E. Trovato, A new ef<sup>fi</sup>cient encoding/decoding procedure for the design of a supply chain network with genetic algorithms, Computers and Industrial Engineering 59 (2010) 986–999.

[14] T.H. Davenport, D.W. Delong, M.C. Beers, Successful knowledge management projects, Sloan Management Review 39 (2) (1998) 43–57.

[15] T. Davenport, L. Prusak, Working Knowledge: How Organizations Manage What They Know, Harvard Business School Press, Boston, MA, 1998.

[16] P.S. Davis, T.L. Ray, A branch-and-bound algorithm for the capacitated facilities location problem, Naval Research Logistics 16 (1969) 331–344.

[17] C. Dimopoulos, A.M.S. Zalzala, Recent developments in evolutionary computation for manufacturing optimization: problems, solutions and comparisons, IEEE Transactions on Evolutionary Computation 4 (2) (2000) 93–113.

[18] H. Ding, L. Benyoucef, X. Xie, A simulation-based multi-objective genetic algorithm approach for networked enterprises optimization, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 19 (2006) 609–623.

[19] S.S. Erenguc, N.C. Simpson, A.J. Vakharia, Integrated production/distribution planning in supply chains: an invited review, European Journal of Operational Research 115 (1999) 219–236.

[20] R.Z. Farahani, M. Elahipanah, A genetic algorithm to optimize the total cost and service level for just-in-time distribution in a supply chain, International Journal of Production Economics 111 (2008) 229–243.

[21] M. Gen, R. Cheng, Genetic Algorithms and Engineering Optimization, Wiley, New York, 2000.

[22] M. Gen, R. Cheng, L. Lin, Network Models and Optimization: Multiobjective Genetic Algorithm Approach, Springer, London, 2008.

[23] D.E. Goldberg, B. Korb, K. Deb, Messy genetic algorithm: motivation analysis and <sup>fi</sup>rst results, Complex System publications (1989) 493–530.

[24] G. Guillen, F.D. Mele, M.J. Bagajewicz, A. Espuna, L. Puigjaner, Multiobjective supply chain design under uncertainty, Chemical Engineering Science 60 (2005) 1535–1553.

[25] H.H. Holland, Adaptation in Natural and Arti<sup>fi</sup>cial Systems, Univ. of Michigan Press, Detroit, 1975.

[26] A. Kumar, Prakash, M.K. Tiwari, R. Shankar, A. Baveja, SSolving machine-loading problem of a <sup>fl</sup>exible manufacturing system with constraint-based genetic algorithm, European Journal of Operational Research 175 (2006) 1043–1069

[27] J.E. Lee, M. Gen, K.G. Rhee, Network model and optimization of reverse logistics by hybrid genetic algorithm, Computers and Industrial Engineering 56 (3) (2009) 951–964.

[28] Y. Meiller, S. Bureau, W. Zhou, S. Piramuthu, Adaptive knowledge-based system for health care applications with RFID-generated information, Decision Support Systems 51 (1) (2011) 198–207.

[29] Z. Michaelwicz, Genetic Algorithm+Data Structure =Evaluation Programs, Springer Verlag, New York, 1992.

[30] M. Nietok, From R&D management to knowledge management: an overview of studies of innovation management, Technological Forecasting and Social Change 70 (2003) 135–161.

[31] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 1 (5) (1994) 14–37

[32] I. Nonaka, H. Takeuchi, The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation, Oxford University Press, New York, NY, 1995.

[33] C. O'Dell, J. Grayson, If We Only Knew What We Know: Identi<sup>fi</sup>cation and Transfer of Internal Best Practices, American Productivity and Quality Center, Houston, TX, 1997.

[34] M.S. Pishavee, M. Rabbani, A graph theoretic-based heuristic algorithm for responsive supply chain network design with direct and indirect shipment, Advances in Engineering Software 42 (2011) 57–63.

[35] P. Pontrandolfo, O.G. Okogbaa, Global manufacturing: a review and a framework for planning in a global corporation, International Journal of Production Economics 37 (1) (1999) 1–19.

[36] A. Prakash, S.G. Deshmukh, A multi-criteria customer allocation problem in supply chain environment: an arti<sup>fi</sup>cial immune system with fuzzy logic controller based approach, Expert System with Applications 38 (4) (2011) 3199–3208.

[37] E.H. Sabri, B.M. Beamon, A multi-objective approach to simultaneous strategic and operational planning in supply chain design, Omega 28 (2000) 581–598.

[38] Z.-J.M. Shen, L. Qi, Incorporating inventory and routing costs in strategic location models, European Journal of Operation Research 179 (2) (2007) 372–389.

[39] S.S. Syam, A model and methodologies for the location problem with logistical components, Computers and Operations Research 29 (2002) 1173–1193.

[40] A. Syarif, Y. Yun, M. Gen, Study on multi-stage logistics chain network: a spanning tree-based genetic algorithm approach, Computers and Industrial Engineering 43 (2002) 299–314.

[41] A. Tiwana, The Knowledge Management Toolkit, Prantice hall, 2000.

[42] A. Tiwana, R. Balasubramaniam, A design knowledge management system to support collaborative information product evolution, Decision Support Systems 31 (2001).241-262

[43] M.K. Tiwari, N. Raghavendra, S. Agarwal, S.K. Goyal, A Hybrid Taguchi-Immune approach to optimize an integrated supply chain design problem with multiple shipping, European Journal of Operational Research 203 (2010) 95–106.

[44] T.H. Truong, F. Azadivar, Optimal design methodologies for con<sup>fi</sup>guration of supply chains, International Journal of Production Researches 43 (11) (2005) 2217–2236.

[45] S. Wadhwa, A. Saxena, Supply chain <sup>fl</sup>exibility and knowledge management: a decision knowledge sharing focus, Studies in Informatics and Control 15 (1) (2006) 133–145.

![](/api/attachments/SCH353KA/fulltext/images/7fdb82a6cfb3d425b2b2a506f7e5bb32e3399e12867f087a54fb2e03bae5753e.jpg)

Dr. Anuj Prakash is a young researcher who has done his Ph.D. from IIT Delhi. He is working in the domain of FMS, CIM, supply chain management, Operation Management, Optimization. His research involves GA, SA, AIS, and Fuzzy Systems applications to the <sup>fl</sup>exible system problems. He has some good publications in some internationals journals and conferences.

Dr. Haitao Liao is an Assistant Professor in Department of Industrial & Information Engineering and Nuclear Engineering Department at the University of Tennessee, Knoxville. He received his Ph.D. degree from the Department of Industrial and Systems Engineering at Rutgers University. He also received M.S. degrees in Industrial Engineering and Statistics, both from Rutgers University. His research interests focus on Modeling of Accelerated Testing, Probabilistic Risk Assessment, Maintenance Models and Optimization, Spare Part Inventory Control, and Prognostics. His current research is sponsored by National Science Foundation and U.S. Nuclear Regulatory Commission. He is a member of IIE and INFORMS. He is a recipient of National Science Foundation CAREER Award in 2010 and the 2010 William A.J. Golomski Award.

![](/api/attachments/SCH353KA/fulltext/images/823765407e63a508378064d3a58cc10412fb5f60804ea0086a6cab348c595f4b.jpg)

Dr. Felix T. S. Chan received his BSc Degree in Mechanical Engineering from Brighton Polytechnic (now University), UK, and obtained his MSc and PhD in Manufacturing Engineering from the Imperial College of Science and Technology, University of London, UK. Dr Chan is now an Associate Professor in the Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University. His current research interests are Logistics and Supply Chain Management, Distribution Coordination, Systems Modelling and Simulation, Supplier Selection. To date, he has published nine book chapters, over 200 refereed international journal papers and 200 peer reviewed international conference papers. He is a Chartered Member of the Chartered Institute of Logistics and Transport in Hong Kong.

![](/api/attachments/SCH353KA/fulltext/images/98e188812bd47c1562dfa59029113cefbbb94ab25e170ff526b629c5ba2c64d8.jpg)

Prof. S.G. Deshmukh is a Professor in the Mechanical Engi neering Department at Indian Institute of Technology (IIT), Delhi. His papers have been published in many reputable international journals like International Journal of Operations & Production Management, International Journal of Productivity and Performance Management. Production Planning and Control, International Journal of Production Research, etc.
