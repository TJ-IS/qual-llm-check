---
otero_id: 16848
otero_key: "CDBQG6DQ"
title: "A new class of intelligent knowledge-based systems with an optimisation-based inference engine"
authors: "Madan G. Singh; Roderick Cook"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90170-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A New Class of Intelligent Knowledge-Based Systems with an Optimisation-Based Inference Engine

Madan G. SINGH and Roderick COOK
Complex Systems Group Control Systems Centre UMIST, P.O.
Box 88, Manchester M601QD, England

In this paper we describe a new class of intelligent knowledge-based system (IKBS) which can be used principally for managerial decision making applications. This class of applications often requires a framework for knowledge acquisition which allows the system to use the knowledge of several experts. In addition, since in most business decision making the objective is to maximise profits, there is a need for an inference engine which allows optimisation to be carried out. The new class of IKBS which is described in this paper has both these properties, i.e., the ability to use the knowledge of multiple experts in a convenient way and an inference engine which by performing optimisations is able to pick out the profit maximising decisions. As an illustration of these concepts, a system for allocation decision making is described. The system 'Retail-opt' allows the user to solve problems like allocation of space in retail outlets, allocation of space in mail order catalogues, pricing policy decisions for discounted airline tickets, etc. In the paper, the basic concepts behind 'Retail-opt' are described and an application of 'Retail-opt' to the problem of retail space allocation in a Scandinavian Department Store is given. A number of other systems which use these concepts for more complicated competitive decision making situations are also described.

Keywords: Intelligent Knowledge Based Systems; Decision Support Systems

![](/api/attachments/CDBQG6DQ/fulltext/images/cc6405dc71e5702520a238c020c11759ca1f294977ca987b0067a57308540353.jpg)

Roderick Cook received an M.Sc. (1975) and Ph.D (1978) from the University of Manchester for research into the numerical solution of nonlinear equations. From 1977 to 1981 he was a temporary lecturer at the University of Liverpool and from 1981 has held the post of Computer Officer in the Control Systems Centre, UMIST. His current research interests fall into two main areas, design and development of decision support systems for higher managerial tasks and development of numerical methods for solving large interconnected systems of equations on multiprocessor architectures.

## 1. Introduction

An Intelligent Knowledge-Based System (IKBS) consists of two parts as shown in Fig. 1: an inference engine and a knowledge base which can be interrogated.

![](/api/attachments/CDBQG6DQ/fulltext/images/c16f2c27835bdd7fb6820da9a59ddd3f755a8872f7494f41075f4e3ea72ed01b.jpg)  
Fig. 1. A Knowledge-Based System.

Most of the successful applications of knowledge-based techniques have used a large number of 'If-Then' production rules in the inference engine. The main merit of this is that from the resulting tree structure, it is quite easy to backtrack. Thus, the system is able to provide to the user, if required, the basis of its reasoning process.

It is well recognised [1] that one of the main bottlenecks which arises in the development of knowledge-based techniques is in the knowledge acquisition phase. The extraction of knowledge from human experts is a non-trivial task which is

![](/api/attachments/CDBQG6DQ/fulltext/images/efee074ae6d4500d57dadf41d54d4c7f0a2b5ce3d0980245048107cf9647df3e.jpg)

with applications to Engineering Systems and to Management Systems. He is the author of 11 books and of over 100 articles.

Madan G. Singh received a Ph.D from Cambridge in 1973. He was elected to the Chair of Control Engineering at UMIST in 1979 and was the Head of the Control Systems Centre in UMIST between 1981-83. Between 1980-84 he also held a part-time Visiting Research Professorship of Management Science at INSEAD, Fontainebleau, France. He was awarded the D.Sc. degree by the University of Toulouse in 1978. Madan Singh's principal research interests are in complex systems theory long and laborious since the expert often finds it difficult to articulate his ‘rules’. It would be desirable to be able to use the expert knowledge of several experts. However, this is particularly difficult to do since each new expert’s knowledge introduces contradictions in the logic which require significant effort to resolve.

Another difficulty with the current generation of knowledge-based systems is that they often have a very limited range of applicability. This comes about because the knowledge base of most systems is very meagre. If one splits up the knowledge base into components coming from:

(i) Common sense knowledge,

(ii) Encyclopedia knowledge, and

(iii) Expert knowledge

then, the current generation of IKBS only as a small amount of (iii). The next generation of IKBS will need amongst other things, to provide ways of representing knowledge in the form of [1] such as:

\- Causal models

\- Strategies and plans

\- Expectations and defaults

\- Temporal and spatial continuity

\- Abstractions and approximations

\- Beliefs

\- Conflicts and contradictions

\- Multiple sources of expertise

\- Parallel processing

\- Learning from experience

In this paper, we describe a new class of IKBS which incorporates many of the above factors. In addition, it incorporates a crucial aspect which is particularly important in managerial decision making; problems where the principal objective is to maximise profits; i.e., optimisation.

## 2. The New Class of IKBS

The new class of IKBS is comprised of 3 main components, which are described in the sections

below:

(1) The 'Shell' which defines the class of applications;

(2) The knowledge acquisition mechanism; and

(3) The optimisation-based inference engine.

## 2.1. The 'Shell'

The ‘Shell’ in the new class of IKBS is at the heart of the knowledge base and it has causal mathematical models. These models are very general and are specialised to a specific application in the knowledge acquisition phase. In mathematical terms, these could be in the form of systems of algebraic equations, ordinary differential equations, partial differential equations, logical relationships, etc. They could equally well be in the form of optimisations linked by ‘If-Then’ rules. In any case, the mathematical structure of the ‘Shell’ comprises two interlinked parts, i.e., the Structural Equations and the Parameters. The structural equations are sufficiently general to represent a wide class of applications. The parameters allow the system to be specialised to a specific case via the acquisition of expert knowledge from one or more experts in the Knowledge Acquisition Phase. These concepts are clarified in ‘Retail-opt’ system of section 3.

## 2.2. Knowledge acquisition

The knowledge acquisition phase is the next aspect which is different in the new class of IKBS described in this paper in relation to the current generation of IKBS. It allows the incorporation of many of the aspects mentioned in section 1; for example, strategies and plans, expectations and defaults, temporal and spatial continuity, abstractions and approximations, conflicts and contradictions, multiple sources of expertise, and learning from experience. This phase has two parts which could be termed ‘Knowledge Elicitation’ and ‘Parameter Estimation’.

In the knowledge elicitation phase, the user or group of users parameterise the 'Shell' by determining the parametric values which specialise the 'Shell' to a specific situation. For example, if the 'Shell' incorporates all allocation problems, the knowledge elicitation phase allows us to specialise it to a single one in a specific situation; for example, the problem of allocating shelf space between different items on a shelf in a store in a specific location. This is done through a variety of mechanisms, for example:

(1) Incorporation of experimental data;

(2) Incorporation of knowledge of one multi-ple experts;

(3) Incorporation of cross-sectional data;

(4) Incorporation of strategies and plans:

(5) Incorporation of conflicts and contradictions;

(6) Learning from experience.

Virtually all of this information can be fed into the computer in an interactive mode. The user could also feed in the level of confidence he or she has in any particular piece of information. The skill of the system designer obviously lies in the design of the questions which allows the system to extract both 'hard' information as well as 'gut feel' information from one or more experts. The 'gut feel' information could incorporate (4), (5) or (6) above and much more.

There are significant merits in being able to use both ‘hard’ and ‘gut feel’ information, particularly in managerial applications where the ‘hard’ information could be obtained from historical data which has the limitation of being applicable strictly to the past whilst managerial ‘gut feel’ could be used to modulate the system to introduce also managerial intuition about the future.

In the ‘Parameter Estimation’ phase of knowledge acquisition, the data obtained from the knowledge elicitation phase is suitably weighted in order to incorporate the user group’s level of confidence in any particularly part of it. It is then operated upon by a suitable statistical algorithm which calculates the best possible parametric values to fit this data. The Statistical algorithm to be used for any particular situation will depend on the nature of the mathematical structures incorporated within the ‘Shell’. For example, if the ‘Shell’ is static, i.e., the problem being solved is concerned with decision making at a particular point in time, then standard multivariate regression analysis [2] may be adequate for parameter estimation. If the ‘Shell’ is concerned with dynamical decision making, i.e., decisions taken at different points in time whilst taking into account spatial and temporal continuities, then the vast arrays of parameter estimation techniques available or dynamical systems may be used [3,4].

## 2.3. The Inference Engine

The Inference Engine in these new IKBS has a capability of doing optimisation. This is of vital importance in many applications, and in particular, in higher managerial decision making applications where it is usually necessary to maximise profits.

Since by the end of the knowledge acquisition phase, the computer has a defined Mathematical Model with an appropriate Parameter Set for a particular situation, one can now use the vast array of techniques available for optimisation $[4,5,6]$ . These techniques would obviously be different for the different kinds of 'Shells'. For example, if the 'Shell' is static, one could use non-linear programming techniques for the optimisation $[4,5]$ . For dynamical shells, dynamical optimisation may be necessary $[6]$ .

## 2.3.1. Backtracking

In all knowledge-based systems, it is vital to be able to explain the reasoning behind a particular decision. The merit of the optimisation framework is that it allows the computer to be used in the things it does best, i.e., number crunching. However, very few of the optimisation algorithms involve inefficient tree searches. Thus, backtracking here is not convenient in the way it is done in the current generation of IKBS. However, it is easy to provide a reasoning for the decisions recommended by the system. The most powerful way of doing this is through graphics where the user can see the lower profits (or higher costs) resulting from a neighbouring suboptimal decision.

Having briefly described the 'Shell', the 'Knowledge Acquisition' phase and the 'Inference Engine' in general terms, we are now in a position to describe a detailed application of these ideas in the development of the General Allocation System 'Retail-opt' which has been developed by the authors in Manchester.

## 3. 'Retail-opt'

Retail-opt is a proprietary decision support system which incorporates the ideas described in section 2. It was developed to tackle the vast variety of decision making problems in managerial systems where it is vital that every allocation decision maximises profits.

## 3.1. The Shell [7]

The ‘Shell’ for Retail-opt is a set of non-linear algebraic equations and inequalities. We will first describe the shell in terms of retail space allocation problems and then discuss how the same framework carries over quite naturally to many other allocation problems.

Suppose that the retailer's stores has K products ( $K \leqslant 12$ in Retail-opt). The objective function, i.e., the total profit of the retailer, is composed of a set demand and cost functions for individual products.

The demand function incorporates both the individual space elasticities and the cross elasticities between products. The unit demand $q_{i}$ for each product is modelled as:

$$
q_{i} = \alpha_{i}s_{i}^{\beta_{i}}\prod_{\substack{j = 1\\ j\neq i}}^{K}s_{j}^{\delta_{i}},
$$

where:

$\beta_{i}$ is the direct elasticity w.r.t. a unit of shelf space $s_{i}$ ;

$\delta_{i,j}$ is the cross space elasticity between products i and j;

$\alpha_{i}$ is a scaling factor.

N.B. $\delta_{ij}$ can be positive or negative depending upon whether products $i$ and $j$ are complementary or substitute products. $\delta_{ij}$ is not necessarily equal to $\delta_{ji}$ .

The total store gross margins over the K products is then:

$$
\sum_ {i = 1} ^ {K} w _ {i} q _ {i} = \sum_ {i = 1} ^ {K} w _ {i} \alpha_ {i} s _ {i} ^ {\beta_ {i}} \prod_ {\substack {j = 1 \\ j \neq 1}} ^ {K} s _ {j} ^ {\delta_ {i, j}}
$$

where $w_{i}$ is the margin rate for product i.

Turning to the cost side, the store costs associated with a product are modelled as:

$$
\gamma_ {i} q _ {i} ^ {\tau_ {i}} = \gamma_ {i} \alpha_ {i} ^ {\tau_ {i}} s _ {i} ^ {\beta_ {i} \tau_ {i}} \prod_ {\substack {j = 1 \\ j \neq i}} ^ {K} s _ {j} ^ {\delta_ {i j} \tau_ {i}}
$$

where:

$\tau_{i}$ is the operating cost elasticity associated with increased sales of produce i;

$\gamma_{i}$ is a scaling factor.

The total store costs over all K products is then:

$$
\sum_ {i = 1} ^ {K} \gamma_ {i} q _ {i} ^ {\tau_ {i}}
$$

Hence the profit of the store is:

$$
\sum_ {i = 1} ^ {K} w _ {i} q _ {i} - \sum_ {i = 1} ^ {K} \gamma_ {i} q _ {i} ^ {\tau_ {i}}
$$

There are also a number of constraints which need to be imposed.

(i) Store capacity constraint: The total shelf space allocated cannot exceed the available shelf space, $S^{*}$ .

(ii) Product availability constraint: Unlimited supplies of a product may not be available, therefore the sales, $q_{i}$ , are constrained by a product availability limit $Q_{i}^{*}$ .

N.B $Q_{i}^{*}$ can be set infinite in ‘Retail-opt’ if there is no limit on $q_{i}$ .

(iii) Shelf space constraints: An upper bound, $S_{i}^{u}$ , and a lower bound, $S_{i}^{L}$ , can be imposed on the shelf space allocatable to product i. Lower bounds may be set for a product because the retailer believes it is essential for his ‘image’ to carry this product irrespective of immediate profitability, or because it is a new product which needs to make an impact. Upper bounds may be set for products at a later stage of the life cycle to keep the store up-to-date.

(iv) Non-negativity constraints: The shelf space $s_{i}, i = 1, K$ , are required to be positive to ensure sensible values.

The 'Shell' can be summarised as:

$$
\max \left\{\sum_{i = 1}^{K}w_{i}\alpha_{i}s_{i}^{\beta_{i}}\prod_{\substack{j = 1\\ j\neq i}}^{K}s_{j}^{\delta_{1j}} - \sum_{i = 1}^{K}\gamma_{i}\alpha_{i}^{\tau_{i}}s_{i}^{\beta_{i}\tau_{i}}\prod_{\substack{j = 1\\ j\nu i}}^{K}s_{j}^{\delta_{1j}\tau_{i}}\right\}
$$

subject to:

$$
\sum_ {i = 1} ^ {K} s _ {i} \leqslant S ^ {*}
$$

$$
\alpha_ {i} s _ {i} ^ {\beta_ {i}} \prod_ {\substack {j = 1 \\ j \neq i}} ^ {K} s _ {j} ^ {\delta_ {i j}} \leqslant Q _ {i} ^ {*}, \quad i = 1, \dots , K
$$

$$
\begin{array}{r l} & s _ {i} ^ {\mathrm{L}} i \leqslant 1 _ {i}, \leqslant s _ {t} ^ {\mathrm{U}}, \tilde {K} \\ & s _ {i} \geqslant 0, \dots , K \end{array}
$$

The units of the quantities in the model can be interpreted in several ways. In this paper and in the example later, the units are as follows:

$$
\begin{array}{l l} \text {shelf space} & s: - \text {square metres} \\ \text {sales} & q: - \text {money (f1000)} \\ \text {costs} & c: - \text {money (f1000)} \end{array}
$$

The margin rate $w_{i}$ is defined as:

$$
\frac {(\text { price   sold   at }) - (\text { price   bought   at })}{(\text { price   sold   at })}
$$

The above formulation is due to Corstjens and Doyle [7] who tested it along with their suggested optimisation procedure. Corstjens and Doyle applied their model for a retailer with 140 shops, a sales turnover of \$30 million and a merchandise consisting of a range of quality candy, ice-cream and greeting cards. Their results showed considerable improvements of the order of 20% on the actual profitability of smaller stores and over 3% on the performance of larger stores. The results were also found to be superior to those of PROGRALI and OBM methods.

Swinnen has recently independently tested most of the commercially available software product groups and four supermarkets belonging to a Belgian chain. His results are reproduced below:

These results of Swinnen [8] show that this is by far the most attractive 'Shell' to use for this class of problems.

3.1.1. Generalisation of the 'Shell' to other allocation problems

Although the formulation of the 'Shell' in section 3.1 was done bearing in mind the problem of retail space allocation in supermarkets and hypermarkets, it is easy to see that in fact the 'Shell' is much more general. For example, the same 'Shell' could be used for, amongst others, the following applications:

(1) Page and subpage allocation in mail order catalogues, holiday brochures, etc.

(2) Allocation of sales effort (measured in man days) amongst different categories of products (e.g., allocation of sales effort between Automobile Insurance, Civil Responsibility Insurance, Fire Insurance etc. for an Insurance office with a limited sales force).

(3) Allocation of Seats in airlines amongst differently discounted seats.

(4) Allocation of advertising budgets, etc.

In each of the above 4 cases, the relationship between the sales on the one hand and the allocation variable on the other, is concave. There are upper and lower bounds on the allocation variables and most of the other factors incorporated in the 'Shell' of section 3.1 also exist here.

Table 1

<table><tr><td>Method</td><td>Supermarket 1</td><td>Supermarket 2</td><td>Supermarket 3</td><td>Supermarket 4</td></tr><tr><td></td><td colspan="4">Computation of Profits per week in Belgian Francs</td></tr><tr><td>Corstjens- Doyle</td><td>34.768</td><td>28.328</td><td>26.529</td><td>17.091</td></tr><tr><td>HOPE</td><td>31.903</td><td>26.997</td><td>25.621</td><td>16.103</td></tr><tr><td>OBM</td><td>31.115</td><td>27.102</td><td>24.946</td><td>15.919</td></tr><tr><td>PROGRALI</td><td>30.601</td><td>27.005</td><td>25.323</td><td>14.855</td></tr><tr><td>CPI</td><td>32.352</td><td>25.681</td><td>24.846</td><td>14.069</td></tr></table>

Thus, the ‘Shell’ of section 3.1 is in fact very general and could be used to tackle a wide variety of allocation problems in managerial decision making. ‘Retail-opt’ allows the user to name the allocation variable at the outset.

## 3.2. Knowledge acquisition

The first part of the knowledge acquisition phase is devoted to knowledge elicitation. In the present version of ‘Retail-opt’, there are two options. The first involves the user feeding in the various parameters based upon a priori analysis of historical data. The second uses the skill and judgement of one or more managers who essentially do a number of experiments in their head and give their ‘gut feel’ response to various ‘what-if’ questions. Future versions would have a third option which allows the user to answer similar questions based on historical information and to weight the responses as a function of the confidence expressed by the managers in each piece of data. We will next show an example of these questions and answers based on the experience and judgement of the marketing director of a Scandinavian department store where 3 departments were considered.

## 3.2.1. Knowledge elicitation in the scandinavian department store example

The three departments were Knitwear, Shirts and Outerwear. The total store capacity was 1506 m $^{2}$ and the lower and upper bounds for Knitwear and Shirts were set by the manager to 250 m $^{2}$ and 650 m $^{2}$ , respectively, whilst for the bulkier Outerwear, the corresponding limits were $350 \, m^{2}$ and $750 \, m^{2}$ . The average margin rates for the three departments were, respectively: 0.3930, 0.3920 and 0.3800.

Figure 2 shows the screen into which the 'hard' information about current space ( $m^{2}$ ) and the associated sales (annual in 1000s of currency units) and costs (annual in 1000s of currency units) have been introduced.

Next, the manager fed in his 'gut feel' information of the kind 'what would you expect would happen to the sales and costs of Knitwear, Shirts and outerwear if we decreased the space allocated to Knitwear by 29% and correspondingly increased the space for Shirts by 18% and for outerwear by 18%. Figure 3 shows the corresponding screen.

The manager used 'gut feel' information of the kind: "The Shirts manager is young and dynamic and he would probably be able to achieve proportionately higher sales than the Outerwear manager by perhaps using his 18% more space more effectively by putting in say a line of designer shirts". Figure 4 shows the screen which has incorporated the managerial 'gut feel'.

The manager thus felt that reducing space for Knitwear by 29% would cause a decrease of 15% in sales volume and 14% in variable costs whilst the corresponding increases of 18% in Shirts would cause sales to increase by 25% and costs by 30%. Similarly, an 18% increase in the space for outerwear will cause the sales to increase by 15% and costs by 4%. The next version of ‘Retail-opt’ will also allow the manager to express the level of confidence he has in this ‘gut-feel’ experiment which he does in his head.

In the case of 3 products, the manager fills in 12 such screens. Figure 5 shows the 12th screen.

THE CURRENT ALLOCATION
SALES AND COSTS FOR EACH PRODUCT

<table><tr><td rowspan="2">PRODUCT NAME</td><td rowspan="2">CURRENT ALLOCATION</td><td rowspan="2">ASSOCIATED SALES</td><td colspan="2">ASSOCIATED COSTS</td></tr><tr><td>FIXED</td><td>VARIABLE</td></tr><tr><td>KNITWEAR</td><td>589.</td><td>28411.</td><td>400.</td><td>2181.</td></tr><tr><td>SHIRTS</td><td>303.</td><td>12739.</td><td>500.</td><td>1225.</td></tr><tr><td>OUTWEAR</td><td>614.</td><td>25514.</td><td>600.</td><td>1989.</td></tr></table>

Fig. 2.

INPUT THE EXPECTED SALES AND COSTS FROM
THE ALLOCATION DECISION( SCREEN 1 OF 12 )

<table><tr><td>PRODUCT NAME</td><td colspan="2">PROPOSED ALLOCATION</td><td colspan="2">ASSOCIATED SALES</td><td colspan="2">ASSOCIATED COSTS VARIABLE</td><td>TOTAL</td></tr><tr><td>KNITWEAR</td><td>420.</td><td>-29.0%</td><td>28411.</td><td>0.0%</td><td>2181.</td><td>0.0%</td><td>2581.</td></tr><tr><td>SHIRTS</td><td>359.</td><td>18.0%</td><td>12739.</td><td>0.0%</td><td>1225.</td><td>0.0%</td><td>1725.</td></tr><tr><td>OUTWEAR</td><td>727.</td><td>18.0%</td><td>25514.</td><td>0.0%</td><td>1989.</td><td>0.0%</td><td>2589.</td></tr></table>

Fig. 3.

INPUT THE EXPECTED SALES AND COSTS FROM
THE ALLOCATION DECISION( SCREEN 1 OF 12 )

<table><tr><td rowspan="2">PRODUCT NAME</td><td rowspan="2" colspan="2">PROPOSED ALLOCATION</td><td rowspan="2" colspan="2">ASSOCIATED SALES</td><td colspan="3">ASSOCIATED COSTS</td></tr><tr><td colspan="2">VARIABLE</td><td>TOTAL</td></tr><tr><td>KNITWEAR</td><td>420.</td><td>-29.0%</td><td>24149.</td><td>-15.0%</td><td>1876.</td><td>-14.0%</td><td>2276.</td></tr><tr><td>SHIRTS</td><td>359.</td><td>18.0%</td><td>15924.</td><td>25.0%</td><td>1593.</td><td>30.0%</td><td>2093.</td></tr><tr><td>OUTWEAR</td><td>727.</td><td>18.0%</td><td>29341.</td><td>15.0%</td><td>2069.</td><td>4.0%</td><td>2669.</td></tr></table>

Fig. 4.

INPUT THE EXPECTED SALES AND COSTS FROM THE ALLOCATION DECISION (SCREEN 12 OF 12)

<table><tr><td rowspan="2">PRODUCT NAME</td><td rowspan="2" colspan="2">PROPOSED ALLOCATION</td><td rowspan="2" colspan="2">ASSOCIATED SALES</td><td colspan="3">ASSOCIATED COSTS</td></tr><tr><td colspan="2">VARIABLE</td><td>TOTAL</td></tr><tr><td>KNITWEAR</td><td>499.</td><td>-15.0%</td><td>26706.</td><td>-6.0%</td><td>2050.</td><td>-6.0%</td><td>2450.</td></tr><tr><td>SHIRTS</td><td>257.</td><td>-15.0%</td><td>11465.</td><td>-10.0%</td><td>1078.</td><td>-12.0%</td><td>1578.</td></tr><tr><td>OUTWEAR</td><td>750.</td><td>22.0%</td><td>30107.</td><td>18.0%</td><td>2128.</td><td>7.0%</td><td>2728.</td></tr></table>

Fig. 5.

Each screen could be filled out by one Manager or by a committee of managers etc. Thus, multiple sources of expertise could be utilised.

Once all 12 screens have been fed in, the program goes into the parameter estimation phase and calculates the parameters of the model as well as a statistical measure of consistency (goodness of fit). On an IBM PC XT with 256K of memory and a math coprocessor, this took about 3–4 seconds.

Figures 6 and 7 shows the model. Here it is shown in terms of numerical values of the elasticities but it is just as easy to do this graphically.

The user has the option at this stage to modify his responses if desired or modify these coefficients if desired.

Once the user is reasonably happy with the knowledge acquired, as represented by this model, we can go on to examine the inference engine.

## 3.3. The inference engine

The unique feature of the inference engine here is the possibility of maximising profits. In the case of ‘Retail-opt’, this is possible using one of the

THE CURRENT ALLOCATION
SALES AND COSTS FOR EACH PRODUCT

<table><tr><td rowspan="2">PRODUCT NAME</td><td rowspan="2">CURRENT ALLOCATION</td><td rowspan="2">ASSOCIATED SALES</td><td colspan="2">ASSOCIATED COSTS</td></tr><tr><td>FIXED</td><td>VARIABLE</td></tr><tr><td>KNITWEAR</td><td>589.</td><td>28411.</td><td>400.</td><td>2101.</td></tr><tr><td>SHIRTS</td><td>303.</td><td>12739.</td><td>500.</td><td>1225.</td></tr><tr><td>OUTWEAR</td><td>614.</td><td>25514.</td><td>600.</td><td>1989.</td></tr></table>

## DATA FOR KNITWEAR

CAPACITY : 1506.

LOWER BOUND : 250. DIRECT SPACE ELASTICITY : 0.7713

UPPER BOUND : 650. CROSS SPACE ELASTICITY BETWEEN KNITWEAR

PRODUCT AVAILABILITY LIMIT : INFINITE AND SHIRTS : 0.1068

MARGIN RATE : 0.3930 AND OUTWEAR : -0.0904

OPERATING COST ELASTICITY : 0.7294

SCALING FACTOR FOR SALES : 2.0E+02

SCALING FACTOR FOR COSTS : 1.5E+00

Fig. 6.

various optimisation methods available for solving such non-linear optimisation problems. Thus the user is given the screen shown in Fig. 8.

Responding Max in the main menu causes 'Retailopt' to find the optimal shelf space allocation and hence to maximise the stores profit. Once he has done this, then the optimal allocation can be displayed. In Figures 9 and 10 we show the results of the optimisation for the Scandinavian Store. On an IBM PC XT with 256K of memory and an 8087 math coprocessor, this optimisation took about 40 seconds to an accuracy of 5% in any constraint. Larger numbers of products require more computation time at the same level of accuracy.

'Retail-opt' also gives a breakdown of the optimal sales, costs and profits for each product.

Further backtracking can be provided by representing the model graphically with the optimal solution marked on it. This is shown in Figures 11, 12 and 13 where the profits have been plotted by fixing all other allocations of shelf spaces at their optimal values except one. As we can see, any small variation away from the optimum in any of the variables causes a reduction in profits. It is thus easy to see how sensitive the solution is.

We note that here ‘Retail-opt’ allowed an improvement of a impressive 6.3% in profitability through the use of the optimisation based inference engine.

Figure 11a shows the effects of reallocating shelf space from Shirts to Outwear, keeping the shelf space for Knitwear constant. Figure 11a shows that the total profits decrease as the shelf space allocation moves away from the optimal. Figure 11b shows that the profits from Outwear increase while those from Shirts decrease and that

## DATA FOR SHIRTS

CAPACITY : 1506.

LOWER BOUND : 250. DIRECT SPACE ELASTICITY : 0.7250

UPPER BOUND : 650. CROSS SPACE ELASTICITY BETWEEN SHIRTS

PRODUCT AVAILABILITY LIMIT : INFINITE AND KNITWEAR : 0.0554

MARGIN RATE : 0.3920 AND OUTWEAR : 0.1073

OPERATING COST ELASTICITY : 0.8693

SCALING FACTOR FOR SALES : 7.1E+01

SCALING FACTOR FOR COSTS : 4.7E-01

CAPACITY : 1506.

LOWER BOUND : 350. DIRECT SPACE ELASTICITY : 0.5520

UPPER ROUND : 750. CROSS SPACE ELASTICITY BETWEEN OUTWEAR

PRODUCT AVAILABILITY LIMIT : INFINITE AND KNITWEAR : 0.0019

MARGIN RATE : 0.3800 AND SHIRTS : 0.0929

OPERATING COST ELASTICITY : 0.4557

SCALING FACTOR FOR SALES : 4.3E+02

SCALING FACTOR FOR COSTS : 2.5E+01

Fig. 7.

because of the cross effects, the profits from Knitwear decrease even though the shelf space for Knitwear is held constant.

Figs. 12 and 13 show the effects of reallocating shelf space from Knitwear to Shirts and from Outwear to Shirts, respectively. As before, the total profits decrease as the shelf space allocation moves away from the optimal.

3.4. Strategic and operational decision making using Retail-opt

Having developed the knowledge-based decision support system ‘Retail-opt’ and examined how it works in its principal application area, i.e., retail space allocation in stores, let us now illustrate the use of ‘Retail-opt’ in strategic and operational decision making by senior managers.

In the context of retail-outlets, once the knowledge base, as represented by the model which has

MAIN MENU

NEW : ENTER A NEW EXAMPLE

OLD : ENTER AN OLD EXAMPLE FROM DISK

SAV : SAVE THE CURRENT EXAMPLE ON THE DISK

MOD : MODIFY THE CURRENT EXAMPLE

PRI : PRINT OUT THE CURRENT EXAMPLE

MAX : FIND THE ALLOCATION WHICH MAXIMIZES PROFIT

DSP : DISPLAY THE PROFIT FOR AN ALLOCATION

RET : RETURN TO MS-DOS

WHAT NOW ?max

Fig. 8.

Fig. 10.  
CURRENT AND OPTIMAL ALLOCATIONS

<table><tr><td>CURRENT ALLOCATION</td><td>OPTIMAL ALLOCATION</td></tr><tr><td>KNITWEAR : 589.</td><td>KNITWEAR : 623.</td></tr><tr><td>SHIRTS : 303.</td><td>SHIRTS : 533.</td></tr><tr><td>OUTWEAR : 614.</td><td>OUTWEAR : 350.</td></tr><tr><td>GIVING A PROFIT OF 19353.</td><td>GIVING A PROFIT OF 20566.</td></tr></table>

Fig. 9.

THE OPTIMAL ALLOCATION
SALES AND COSTS FOR EACH PRODUCT

<table><tr><td>PRODUCT NAME</td><td colspan="2">OPTIMAL ALLOCATION</td><td colspan="2">ASSOCIATED SALES</td><td colspan="2">ASSOCIATED COSTS</td><td colspan="2">ASSOCIATED PROFITS</td></tr><tr><td>KNITWEAR</td><td>623.</td><td>6%</td><td>33659.</td><td>18%</td><td>2912.</td><td>13%</td><td>10316.</td><td>18%</td></tr><tr><td>SHIRTS</td><td>533.</td><td>76%</td><td>18955.</td><td>49%</td><td>2438.</td><td>41%</td><td>4993.</td><td>46%</td></tr><tr><td>OUTWEAR</td><td>350.</td><td>-43%</td><td>19880.</td><td>-22%</td><td>2296.</td><td>-11%</td><td>5258.</td><td>-27%</td></tr></table>

![](/api/attachments/CDBQG6DQ/fulltext/images/de6f66bfc3053ddef65986fa185b31957edd962c986fe321e44498b31df9f876.jpg)  
Fig. 11a.

![](/api/attachments/CDBQG6DQ/fulltext/images/7e85330662236874d379b7bc1dce3f55f77c5f7ab56d1bb83474ee284cfc342c.jpg)  
Fig. 11b.

been fitted by a combination of ‘hard’ and ‘gut feel’ information and is agreed by management to be a reasonable representation of their reality, it can be used as a tool for both operational and strategic decision making. Strategic decisions are of the following kinds:

![](/api/attachments/CDBQG6DQ/fulltext/images/f00e17d5bd193c049df07aa0d5aaeb638be024ab8245a2ff8c3c7d6efbd29116.jpg)  
Fig. 12.

![](/api/attachments/CDBQG6DQ/fulltext/images/28d9268e1e86a9d34b6ba2d6699444bbcbf905e3237a8fd369c09a470dbe097c.jpg)  
Fig. 13.

(1) What happens if the margin rates change, i.e., for which products should one aim to negotiate a better margin with the suppliers; what happens if we wish to market a particular product more aggressively, e.g., reduce the margin rate on groceries to compete with other retailers?

(2) How often should one change the allocation of the store and parts of the store?

(3) How bit should the space bands be between which the optimum will be sought?

This and many other questions can be resolved in a cheap and easy way by the system by merely changing some of the information interactively before the inference engine (optimisation) performs its function.

## 3.5. Other applications of 'Retail-opt'

‘Retail-opt’ has also been used for recommending space allocation decisions in holiday brochures. In Figures 14 and 15 we show the results of the use of ‘Retail-opt’ for allocating space in a part of the brochures of a leading British tour operator using the managerial expertise of this company. As we can see, here again, a massive profit improvement could be achieved.

Further applications of 'Retail-opt' are currently being studied.

## 4. Other applications

Finally, we describe other classes of managerial decision problems for which knowledge-based systems can be built using the framework of this paper. The first of these concerns problems of competition. These are resolved by the system 'Mark-opt' which has also been developed in Manchester.

CURRENT AND OPTIMAL ALLOCATIONS

<table><tr><td>CURRENT ALLOCATION</td><td>OPTIMAL ALLOCATION</td></tr><tr><td>majorca : 150.</td><td>majorca : 100.</td></tr><tr><td>monorca : 70.</td><td>monorca : 50.</td></tr><tr><td>ibiza : 69.</td><td>ibiza : 40.</td></tr><tr><td>mainland : 65.</td><td>mainland : 40.</td></tr><tr><td>canaries : 140.</td><td>canaries : 100.</td></tr><tr><td>GIVING A PROFIT OF 1407.</td><td>GIVING A PROFIT OF 1564.</td></tr></table>

Fig. 14.

THE OPTIMAL ALLOCATION
SALES AND COSTS FOR EACH PRODUCT

<table><tr><td colspan="9">SALES AND COSTS FOR EACH PRODUCT</td></tr><tr><td>PRODUCT NAME</td><td colspan="2">OPTIMAL ALLOCATION</td><td colspan="2">ASSOCIATED SALES</td><td colspan="2">ASSOCIATED COSTS</td><td colspan="2">ASSOCIATED PROFITS</td></tr><tr><td>majorca</td><td>100.</td><td>-33%</td><td>4466.</td><td>23%</td><td>304.</td><td>4%</td><td>578.</td><td>38%</td></tr><tr><td>monorca</td><td>50.</td><td>-29%</td><td>1410.</td><td>-39%</td><td>178.</td><td>-10%</td><td>103.</td><td>-63%</td></tr><tr><td>ibiza</td><td>40.</td><td>-33%</td><td>845.</td><td>-28%</td><td>80.</td><td>-7%</td><td>80.</td><td>-45%</td></tr><tr><td>mainland</td><td>40.</td><td>-38%</td><td>1301.</td><td>-19%</td><td>114.</td><td>-4%</td><td>143.</td><td>-28%</td></tr><tr><td>canaries</td><td>100.</td><td>-29%</td><td>4257.</td><td>55%</td><td>185.</td><td>9%</td><td>659.</td><td>79%</td></tr></table>

Fig. 15.

## 4.1. Mark-opt

‘Mark-opt’ [9,10] is a software suite which provides a decision support capability in a key area of marketing, i.e., the negotiation process between manufacturers and retailers. In any negotiation, it is of great importance to understand the imperatives of the person you are negotiating with. ‘Mark-opt’ allows the negotiator to feed in all the information that he has about his own company, that about the company he is negotiating with, information about his own company's competitors as well as that on the competitors of the company he is negotiating with as well as information about the market. From all this information, 'Mark-opt' allows the user to calculate various scenarios, e.g., where the retailers respond quickly to each other's competitive price moves, or where one manufacturer optimises whilst the others don't or where all others optimise as well.

Where the sales, costs and profits are in 1000s of pounds and the space in tenth's of page.

‘Mark-opt’ can also be used as a strategic marketing tool. Some of the more interesting strategic scenarios where ‘Mark-opt’ can be used include:

\- Pricing policies for white label and own label products from the point of view of a manufacturer as well as from that of a retailer;

\- Marketing strategies for manufacturers with poor brand image: trade-offs between brand image improvement (through advertising, ReD, etc.) against improvements in manufacturing efficiency;

\- Use of optimisation where the competitors are not doing so;

\- The impact on the profitability of all manufacturers and retailers if a single manufacturer raises or lowers his prices by a small amount.

For manufacturers, it is possible to calculate safe negotiating ranges which might not invite retaliation from competitors but which nevertheless yield reasonable profits. For retailers, 'Markopt' enables them to obtain better margins and calculate their best shelf space allocation for the brands of different manufacturers so as to maximise total profits.

This description is not only a valid one for products sold through supermarkets and hyper-markets but it could also be used to describe the selling of any product which is sold through intermediaries before reaching the end user.

The problem of competition between manufacturers has been considered in the mathematical economics literature as has the problem of vertical integration. However, the whole system above has never been considered mathematically since it was thought to be an unsolvable problem. Arnold, Singh and Corstjens [9], [10] recently provided the first solution ever of this hitherto unsolved problem in marketing and 'Mark-opt' incorporates their basic method as extended to the case of multiple manufacturers and multiple retailers.

![](/api/attachments/CDBQG6DQ/fulltext/images/02a7ead628ca538499d08a1dc5e5d5f860fb0747dffb21966f51b2860b7cdf12.jpg)  
Fig. 16. Structure of the System being Considered.

‘Mark-opt’ takes into account the manufacturers costs (including economies of scale), the retailer costs (fixed plus variable) as well as the perception of the consumers about the brands of different manufacturers, etc.

## 4.1.1 The 'Shell'

The ‘Shell’ of ‘Mark-opt’ is a set of mathematical models, one for each manufacturer and for each retailer. These models comprise a set of nonlinear algebraic equations or inequalities. To represent the competitive aspects, each manufacturer/retailer has an objective function which is to maximise profits. Thus the ‘Shell’ comprises in this case a set of interacting optimisation problems.

## 4.1.2. Knowledge acquisition

Knowledge acquisition in ‘Mark-opt’ involves the fitting of parametric values into the mathematical models of each manufacturer/retailer in the ‘Shell’. Since the system ‘Mark-opt’ will most likely be used by a manufacturer, the process of knowledge acquisition starts by the manufacturer feeding in ‘hard’ information about his own production costs, economies of scale, brand image (such as represented by price elasticity, shelf space elasticity). Next, the user feeds in ‘Gut feel’ information about the competing manufacturers (Is their manufacturing as efficient as ours? Is their brand considered better or worse than ours by the consumers? and the retailers (Are they all equally efficient?). These two kinds of information are integrated into the ‘Shell’ in order to provide the framework for ‘Scenario Analysis’

## 4.1.3. Inference engine

The inference engine in this case is far more complicated than for ‘Retail-opt’ since at best, one can do a bit of ‘Scenario Analysis’ in these immensely complex competitive situations. However, even this is of great value in strategic decision making for companies since billions of dollars may well hang on such decisions. The inference engine in ‘Mark-opt’ allows one to examine various scenarios where the manufacturers/retailers respond to each other’s moves by maximising their profits in each situation. The mathematical framework of interest here is ‘Game Theory’ and essentially, the inference engine in ‘Mark-opt’ has, at its heart, a mechanism for finding Nash Equilibria of various Gaming situations amongst different players.

## 4.2. Applications of 'Mark-opt'

‘Mark-opt’ was developed by one of the authors during studies carried out for one of the world’s largest consumer goods manufacturers. The first commercial licences for the use of ‘Mark-opt’ have been purchased by a leading US Oil Company and a major business school.

'Mark-opt' runs on an IBM PC XT with 256K of memory and an 8087 coprocessor.

Finally, we describe a dynamical version of 'Mark-opt'.

## 4.3. A dynamical version of 'Mark-opt'

The decision making in the competitive decision tool ‘Mark-opt’ is at a particular point in time. To do strategic decision making with ‘Mark-opt’ therefore requires us to use it at different points in time where competitive ‘snap shots’ can be taken. It is attractive, for strategic decision making to consider dynamical shells. This is being done in a project directed by Professor Singh in Manchester. A similar framework to that of ‘Mark-opt’ is being used except that the ‘Shell’ now comprises difference equations and summations to e maximised for each manufacturer/retailer and the ‘Inference Engine’ now has a differential game at its core. This system will be described elsewhere.

## 5. Conclusions

In this paper, we have described a new framework for designing intelligent knowledge-based systems which uses optimisation or game theory within its inference engine. The knowledge acquisition phase in this new class of IKBS is also more sophisticated since it allows one to use strategies and plans, multiple sources of expertise, abstractions and approximations, conflicts and contradictions, learning from experience, etc. The heart of the new IKBS has causal models and is able to account for spatial and temporal continuity.

In the more complicated applications like "Mark-opt" and the dynamical competitive tool, there is also scope for using parallel processing. Thus the new class of systems are able to incorporate many of the properties suggested by Dr. D. Lennat for future IKBS.

## References

[1] Lenat, D., Keynote Address on Artificial Intelligence, Multiconference of the Simulation Society of America, San Diego, CA (Jan. 1985).

[2] Mosteller, F., E. Rourke and G.B. Thomas, Probability and Statistics, Addison-Wesley, Reading MA (1961).

[3] Sorenson, H.W., Parameter Estimation, Marcel Dekker, New York (1980).

[4] Singh, M.G. and A. Titli Systems: Decomposition, Optimisation and Control, Pergamon Press, Oxford, New York (1978).

[5] Hadley, Non-linear and Dynamic Programming", Addison Wesley, Reading MA (1984).

[6] Sage, A.P. and C.W. White Optimum Systems Control, Prentice Hall, Englewood Cliffs NJ (1976).

[7] Corstjens, M. and P. Doyle A model for optimising retail space allocations, Management Sci. 27 (1981) 822–833.

[8] Swinnen, G. Supermarket chain Product Mix Decision, Ph.D. Thesis, University of Antwerp (1983).

[9] Arnold, J., M.G. Singh and M. Corstjens A decision support system for marketing, LSS (1984).

[10] Singh, M.G., J. Bhondi and M. Corstjens 'Mark-opt' – a decision support system for marketing, IEEE Trans SMC (1985) in press.
