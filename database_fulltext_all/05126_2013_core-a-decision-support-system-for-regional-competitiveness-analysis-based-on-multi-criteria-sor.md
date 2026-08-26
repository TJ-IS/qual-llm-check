---
otero_id: 5126
otero_key: "S8MDX8ZG"
title: "Core: A decision support system for regional competitiveness analysis based on multi-criteria sorting"
authors: "Eduardo Fernandez; Jorge Navarro; Alfonso Duarte; Guillermo Ibarra"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Core: A decision support system for regional competitiveness analysis based on multi-criteria sorting

Eduardo Fernandez ⁎, Jorge Navarro, Alfonso Duarte, Guillermo Ibarra

Faculty of Civil Engineering, Ciudad Universitaria, Autonomous University of Sinaloa, Blvd. Las Americas s/n, Culiacan, Sinaloa, CP, 80040, Mexico

## a r t i c l e i n f o

Article history: Received 30 September 2011 Received in revised form 13 August 2012 Accepted 9 December 2012 Available online 20 December 2012

Keywords: Decision support Competitiveness analysis Multi-criteria sorting Outranking methods

## a b s t r a c t

If regional competitiveness is equated to the capacity to attract and preserve investments, then the perception investors have of the region's characteristic is fundamental. This perception is a result of a complex integration of multiple criteria. This paper approaches the analysis of regional competitiveness by techniques of multi-criteria sorting. An ELECTRE-based preference model is used in the framework of the new THESEUS multi-criteria evaluation method for making competitiveness assignments. The model's parameters are inferred from a set of assignment examples. This model is implemented in the CORE decision support system, which satis<sup>fi</sup>es a requirement of Sinaloa State Government in Mexico. CORE performs very well analyzing the competitiveness of Mexican regional entities. This will allow governments to better de<sup>fi</sup>ne their policies by placing <sup>fi</sup>nancial resources more ef<sup>fi</sup>ciently. The model and the system are conceived to easily emigrate towards other regional contexts.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Through centuries economists have identi<sup>fi</sup>ed in academic literature different factors and mechanisms which, when interrelated, allow economic development of a country or region and, in synthesis, can be de<sup>fi</sup>ned as the capacity to maintain sustained increase in product per capita and its fair distribution [17]. These elements comprise, among others, prior historical conditions, natural resources available, geographic location, ef<sup>fi</sup>cient application of resources in a competitive market with an increasing division of labor, physical and human capital accumulation, technological progress and diffusion combined with legal, cultural and institutional elements that allow them to be displayed [17,21]. Globalization has increased the opportunities of countries and regions to reach the economic growth faster thanks to the possibility of attracting capitals, capability for innovation and capacity for faster and greater access to growing markets. At the same time, however, the countries are becoming more fragile and may be suddenly sanctioned for bad performance, experiencing the opposite (capital <sup>fl</sup>ight, drain of highly quali<sup>fi</sup>ed human resources, loss of markets), thereby affecting the income of the population.

Papers on territorial competitiveness are strongly in<sup>fl</sup>uenced by the work of Michael Porter [22], who provided an important conceptual framework and notably stimulated an interest of the international community in this topic. Territorial competitiveness is based on the capacity of one geographic unit to maintain its medium and long term economic growth, sustained increase in capital investment, product per capita and exportations in order to improve the income and welfare of its population. However, the evaluation of its economic performance must also take into account the quality of its regulatory framework, governmental institutions and actions that favor or hinder the performance of companies, resource availability, infrastructure, innovation capabilities, and all the facilities available to the productive units so they can compete in the best markets of their sector and region. For the companies, the ideal conditions for competing are the existence of a market economy governed by the rule of law, respect for intellectual property, and transparency with no government-protected monopolies. Therefore, it is assumed that prevalence of modern institutions and democratic systems favoring free market will provide territories with strong competitive capabilities that help companies located in such economic space succeed.

It is not so important for public policies to measure competitiveness as to <sup>fi</sup>nd a suitable way to in<sup>fl</sup>uence its enhancement. Considering that the level of competitiveness is an effect of multiple factors, detection of causal relationships between them is necessary to <sup>fi</sup>nd out its determinants, and this should be done beyond a mere qualitative description. Only a more or less precise quantitative description will allow the evaluation of the public action impact on competitiveness. It is necessary to characterize a mathematical function (in its most general sense) that allows evaluating changes in competitiveness with regard to changes in attributes of the social object that have in<sup>fl</sup>uence on it and are modi<sup>fi</sup>able by the action of public policies. On the basis of such model, a “competitiveness simulator” could be created as an instrument for the assessment of policies aimed at its enhancement.

In [24], Sala-I-Martin et al. pointed out the popularization, in economic literature, of partially correlating the rate of economic growth to a substantial number of variables with this kind of regression models:

$$
\gamma = \alpha + \beta_ {1} \cdot x _ {1} + \beta_ {2} \cdot x _ {2} + \dots + \beta_ {n} \cdot x _ {n} + \varepsilon
$$

where γ is the dependent variable and x are the explanatory or causal variables; α and $\beta _ { \mathrm { i } }$ are constants to be determined; and ε represents the magnitude of error.

If the assessment of competitiveness is seen as a multicriteria decision problem, and if γ is a “proxy” variable re<sup>fl</sup>ecting competitiveness, the above model can be seen as a weighted-sum value function. This kind of models requires mutual preference independence and constant compensation ratio, which are quite severe mathematical conditions. Interaction among criteria is not modeled. In order to re<sup>fl</sup>ect such interaction, a non-additive value functional model based on the Choquet Integral should be used (cf. [2,14,18]). As the above model is totally compensatory, the extremely negative evaluation of some causal variables can be compensated with positive evaluations of other attributes. A partially compensatory model, including capability to exercise the veto when the status of some attributes is very unfavorable, could re<sup>fl</sup>ect better the perception of competitiveness.

To the best of our knowledge, this work approaches the analysis of regional competitiveness for the <sup>fi</sup>rst time by modern techniques of multicriteria decision analysis (MCDA). The aim of MCDA is to assist a decision maker (DM) in choosing, ranking and sorting alternatives (actions, objects) according to multiple criteria [4]. Many decision support systems (DSSs) have been designed using MCDA to help DMs in analyzing problems and making easier decisions (e.g. [3–5,8,20]). Here, we propose an assessment of competitiveness by using a fuzzy outranking relation model. Fuzzy relations are an excellent alternative to the functional approach, since they are more general, have greater expressive capacity and are capable of modeling situations of intransitivity and incomparability [13].

The main aim of this paper is to present a “what if” analyzer, which is in fact a “competitiveness simulator”. It uses certain reference information about competitiveness in order to construct a causal model in terms of many explanatory variables. Thus, a DM can explore the effect of changes on some causal variables, performing “what $\mathrm { i f } ^ { \prime }$ analyses on which public policies for competitiveness improvements can be designed. This model is implemented in a decision support system which satis<sup>fi</sup>es a need of Sinaloa State Government in Mexico.

This paper is structured as follows: some theoretical background is presented in Sections 2 and 3. The main models are described in Section 4. The CORE system implementation is discussed in Section $5 ,$ and some experimental results are given in Section 6. Final conclusions are presented in Section 7.

## 2. Background

The World Competitiveness Report 2009–10 de<sup>fi</sup>nes competitiveness as a set of institutions, policies and factors that determine the level of productivity of a country (cf. [25]). Hence the Global Competitiveness Index (GCI) measures the set of institutions, policies and factors that make possible the real growth and medium-term economic prosperity [25]. According to the GCI methodology, countries are divided according to their historical stage of development at the present, in three categories: economies whose growth rests on the exploitation of their resources (Factor-driven stage), those progressing due to more ef-<sup>fi</sup>cient performance of their productive activities and institutional processes (Efficiency-driven stage) and the mature ones, whose growth rests on the innovation (Innovation-driven stage). The differentiation between these categories is based on the use of the Gross Domestic Product (GDP) per capita variable (at exchange rate prices). Twelve subfactors of competitiveness, grouped into three higher hierarchical factors are considered at present: Basic Requirements, Efficiency

Enhancers, Innovation and Sophistication Factors. Each of these factors is itself an index. The GCI is the result of a weighted sum of these factors, but the “weights” of each factor are different according to the respective type of economy (see Fig. 1 and Table 1). At the same time, each of the twelve factors at the second hierarchical level contains numerous explanatory variables in a linear regression model.

A mandatory reference in Mexico is the Mexican Institute for Competitiveness (IMCO). It is a private institution that sells index evaluation and construction services at different levels of the Mexican government. Institute's reports de<sup>fi</sup>ne synthetically competitiveness as a capacity of a territory to bring investments, since the rest of variables, such as growth, income, access to markets, etc. depends on this one. This institution characterizes the social object (as far as competitiveness is concerned) in terms of ten factors, which at the second hierarchical level are disaggregated into 122 causal variables. The IMCO uses the Gross Domestic Product as “proxy” measure of competitiveness CP. Every region is characterized by a pair $( \mathbf { x } , C P ) ;$ x is a vector of $\Re ^ { N }$ , whose dimensions are measures of causal variables; and $C P$ is the measure of competitiveness. Reference information is composed of a set $T = \{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \dots \mathbf { x } _ { M } \}$ , where M is the number of characterized regions. A functional model $U ( \mathbf { x } ) = w _ { 0 } + w _ { 1 } x _ { 1 } + \ldots w _ { N } x _ { N }$ (x is the i-th component of the vector x) that approaches the $C P$ measure is obtained from T by employing regression techniques [16].

## 3. Analysis of competitiveness: different perspectives

With regard to competitiveness and its analysis, three different problems can be distinguished:

a) Estimation. If competitiveness is de<sup>fi</sup>ned as an index composed of several measures, the problem of estimating competitiveness consists of assigning a value to this index for a potential stage of the social object (that might be the present one) under analysis.

b) Ranking. Given a set of regions in a similar context (countries, states, provinces, municipalities, cities), this problem consists of establishing an order within the set in the sense of decreasing competitiveness.

c) Sorting. In general, classi<sup>fi</sup>cation means assigning objects to preexisting categories. A special case of this process appears when there is an order of preference between categories, i.e., it is possible to associate them with an assessment. Then classifying turns into evaluating, assigning a qualitative evaluation to each object. Competitiveness could be evaluated, for instance, on the scale {Very low, Low, Below average, Average, Above average, High, Very high}. These categories imply relative judgments, however, well de<sup>fi</sup>ned in the context of a set of regions that are being compared.

To the best of our knowledge, the existing competitiveness analysis methods are oriented to estimation and ranking, mainly by constructing an index that is calculated from a weighted-sum model of several factors, which, at the same time, are modeled as weighted-sum functions of several causal variables (cf. [16,25]). A competitiveness index like GCI arises from that model. It is a real number, useful for estimation and ranking. This can be seen as an ef<sup>fi</sup>cient way to synthesize information. But such information is needed for making decisions, so competitiveness analysis should be considered an instance of more general multi-criteria decision problems. However, seen as a tool for multi-criteria analysis, weighted-sum models suffer important criticisms: i) the model is totally compensatory, the extremely negative evaluation of some causal variables can be compensated with positive evaluations of other attributes; ii) mutual preference independence and constant compensation ratio are necessary conditions for model's validity; iii) the model cannot handle ordinal and qualitative information (hence, ordinal or qualitative causal variables must become cardinal in order to keep meaningfulness of the results); and iv) the model cannot handle imprecise information.

![](/api/attachments/S8MDX8ZG/fulltext/images/2d47314570cef62a0d1191cbeb3a4c048a8ad716715e82e9671558ddb31dad0b.jpg)  
Fig. 1. The 12 pillars of competitiveness

## 3.1. Evaluation of competitiveness as a multicriteria sorting problem

Evaluation judgment is coarser than those of estimation and ranking, but even more robust with respect to the handling of imprecise information. As far as competitiveness is concerned, in the absence of universally accepted one-dimensional measure for it, laxness of evaluation could be recommendable. Moreover, if there is preference for processing information from human experts rather than that of indirect measures, the experts feel much more comfortable when employing a qualitative scale for their judgments than giving a measure or an order for the set under analysis.

Let's consider that $\mathbf { C t } = \{ C _ { 1 } , \hdots C _ { M } \}$ is a set of ordered categories for the evaluation of the competitiveness. Let's suppose that if i>j, $C _ { i }$ is better than $C _ { j } .$ Be U a universe of x objects that are described by a set $\mathbf { G } = \left\{ g _ { 1 } , \ \ldots \ g _ { N } \right\}$ of attributes (causal variables of changes (also called explanatory variables) in competitiveness); x objects represent geographical regions or localities in the context of the analysis of competitiveness. The evaluation of competitiveness poses the following problem: for each $\mathbf { x } \in U$ determine $C _ { i } { \in } { \bf c } _ { \bf t }$ so that the predicate “the competitiveness associated with x is evaluated as $C _ { i } "$ is more acceptable than its alternative “the competitiveness associated with x is evaluated as $C _ { j } "$ at any $j \neq i . S 0 ,$ evaluating competitiveness is equivalent to having a function F: U→Ct so that each x∈U is associated with just one $C _ { i } { \in } { \bf { C } } { \bf { t } }$ . Function F is the mathematical model of the competitiveness evaluation policy.

Deep down, all methods of interest that approach the general problem of multicriteria evaluation try to model the decision policy which is implicit in a set T of reference examples. This set could result from statistical information, past decisions or new ad hoc decisions created by human experts or DMs capable of sorting reference objects. According to how they process reference information to create the model of sorting policy, different multicriteria procedures can be divided into [11]:

Table 1  
Weights of the three main subindexes at each stage of development.  
Source: Taken from WEF, World Competitiveness Report 2009–2010. http:// www.weforum.org/documents/GCR09/index.html

<table><tr><td>Subindex</td><td>Factor driven stage (%)</td><td>Efficiency driven stage (%)</td><td>Innovation driven stage (%)</td></tr><tr><td>Basics requirements</td><td>60</td><td>40</td><td>20</td></tr><tr><td>Efficiency enhancers</td><td>35</td><td>50</td><td>50</td></tr><tr><td>Innovation and sophistication factors</td><td>5</td><td>10</td><td>30</td></tr></table>

a) Statistical methods;

b) Arti<sup>fi</sup>cial Intelligence Techniques;

c) Analogy-based methods;

d) Multicriteria preference model-based methods.

Linear and quadratic discriminant analyses are the most popular method of those corresponding to point a) (cf. [7]). Symbolic logic methods (e.g. [15]) together with arti<sup>fi</sup>cial neural systems are exponents of b). The K-nearest neighbor method together with the closeness relation proposed in [10] exempli<sup>fi</sup>es the classi<sup>fi</sup>cation–evaluation by analogy. Here, we are interested in multicriteria preference model-based methods. These try to build an explicit mathematical model that would include the decision-making policy as if it resulted from a decisionmaker's preferences (e.g. [1,26]). In [7], Doumpos and Zopounidis provide experimental evidences of advantages of this kind of models, such as UTADIS, MHDIS and ELECTRE-TRI with regard to statistical classi-<sup>fi</sup>cation procedures.

Be M(x,y,p) a predicate meaning that the model M with parameters p prescribes that “the object x is at least as acceptable as the object y” from the point of view of a decision maker (someone, something or some persons that establish(es) the decision making policy). If the model is adequate, then the following is necessary

$$
\forall (\boldsymbol {x}, \boldsymbol {y}) \in U \times U M (\boldsymbol {x}, \boldsymbol {y}, \boldsymbol {p}) \Rightarrow C (\boldsymbol {x}) \succsim C (\boldsymbol {y})\tag{1}
$$

$( C ( \mathbf { x } ) \approx C ( \mathbf { y } )$ means that the category assigned to x is not inferior to that of y).

The degree of model adaptation depends not only upon its formula, but also on the values of parameters it employs. Reference information is used to adjust them and to calibrate, “syntonize” the model. By limiting ourselves to the reference set, the expression (1) turns into:

$$
\forall (\boldsymbol {a}, \boldsymbol {b}) \in T \times T M (\boldsymbol {a}, \boldsymbol {b}, \boldsymbol {p}) \Rightarrow C (\boldsymbol {a}) \succsim C (\boldsymbol {b}).\tag{2}
$$

In the context of the evaluation of competitiveness Eqs. (1) and (2) transform into statements:

1) “If $M ( \mathbf { x } , \mathbf { y } , \mathbf { p } )$ is true then competitiveness of x is evaluated in a category non-inferior (“at least as good as”) to the competitiveness of $\mathbf { y } " .$

2) “If for two given reference objects $( \mathbf { a } , \mathbf { b } ) , M ( \mathbf { a } , \mathbf { b } , \mathbf { p } )$ is true, then the competitiveness of a is evaluated in a category non-inferior to the competitiveness of $\mathbf { b } "$ .

To the best of our knowledge, the most up-to-date multicriteria sorting methods have not yet been employed in the analysis of competitiveness.

## 4. Description of the new proposal

The competitiveness sorting method shown below has immediate precedents in two papers of ours [9,11]. In [11] we proposed a procedure to <sup>fi</sup>t parameters of the preference-based model by using reference information together with implication (Eq. (2)). In [9], THESEUS method was proposed for multicriteria sorting using expression (1). Bases of the proposal in the context of competitiveness analysis are listed below:

i. Use a fuzzy outranking relation model for the predicate $M ( \mathbf { x } , \mathbf { y } ,$ p). σ(x,y,p) measures the degree of credibility of the statement $\mathbf { \ " } \mathbf { x }$ is at least as competitive as $\mathbf { y } ^ { \mathfrak { n } } .$ . For a certain $\lambda > 0 . 5$ , the condition $\sigma ( \mathbf { x } , \mathbf { y } , \mathbf { p } ) { \ge } \lambda$ means that the object x should not be inferior in competitiveness to y.

ii. Use the condition $\forall ( \mathbf { a } , \mathbf { b } ) \in T \times T \sigma ( \mathbf { a } , \mathbf { b } , \mathbf { p } ) \geq \lambda \Rightarrow C ( \mathbf { a } ) \succeq C ( \mathbf { b } )$ to <sup>fi</sup>t the model and obtain values of its parameters $\boldsymbol { \mathfrak { p } } ^ { * }$ as in Fernandez et al. [11].

iii. Following [9], the competitiveness assignment of an object x will be obtained from implications

$$
\forall \boldsymbol {b} \in T \sigma (\boldsymbol {x}, \boldsymbol {b}, \boldsymbol {p} ^ {*}) \geq \lambda \Rightarrow C (\boldsymbol {x}) \succsim C (\boldsymbol {b})
$$

$$
\forall \boldsymbol {b} \in T \sigma (\boldsymbol {b}, \boldsymbol {x}, \boldsymbol {p} ^ {*}) \geq \lambda \Rightarrow C (\boldsymbol {b}) \succsim C (\boldsymbol {x})
$$

where $C ( \mathbf { x } ) \overset { } { \underset { } { \sim } } C ( \mathbf { y } )$ means that the category of x re<sup>fl</sup>ects at least the same competitiveness as that corresponding to y.

iv. The position of x in the complete ranking of the set $T \cup \{ { \bf x } \}$ can be obtained by using F and σ.

The different elements of the proposal are described below.

## 4.1. Fuzzy outranking relation

Let's consider a pair $( \mathbf { x } , \mathbf { y } ) \in U \times U .$ . Let's suppose that the decision maker tries to establish a comparison of the objects x and y by analyzing the state of the attributes of each of them. According to the philosophy of ELECTRE methods (cf. [23]), the result will depend on the assessment of strength of concordance and discordance coalitions. If the concordance coalition with outranking relation (criteria supporting the assertion “x is at least as good as y”) is suf<sup>fi</sup>ciently strong and if the discordance coalition (set of criteria against it) is weak enough, the decision maker (or the model re<sup>fl</sup>ecting it) can reasonably establish the preference statement that we'll denote by xSy. If σ(x,y) is the degree of credibility of xSy predicate, then

$$
\sigma (\boldsymbol {x}, \boldsymbol {y}) = T n (c (\boldsymbol {x}, \boldsymbol {y}), N d (\boldsymbol {x}, \boldsymbol {y}))\tag{3}
$$

where $c ( \mathbf { x } , \mathbf { y } )$ is the degree of credibility of the concordance predicate, Nd(x,y) is the degree of credibility of the non-discordance predicate, and Tn denotes conjunction.

In ELECTRE III, the concordance index $c ( \mathbf { x } , \mathbf { y } )$ is de<sup>fi</sup>ned as follows:

$$
c (x, y) = \sum_ {G} w _ {j} c _ {j} (\boldsymbol {x}, \boldsymbol {y})\tag{4}
$$

where:

w<sub>j</sub> is the weight of the j-th criterion $\left( w _ { 1 } + w _ { 2 } + . . . + w _ { N } { = } 1 \right)$ $c _ { j } ( \mathbf { x } , \mathbf { y } )$ is the marginal (partial) concordance index for the j-th criterion. This index is calculated by:

$$
c _ {j} (x, y) = \left\{ \begin{array}{c c} 0 & \text { if } g _ {j} (y) - g _ {j} (x) \geq p _ {j} \\ \left(g _ {j} (x) - g _ {j} (y) + p _ {j}\right) / \left(p _ {j} - q _ {j}\right) & \text { if } q _ {j} <   g _ {j} (y) - g _ {j} (x) <   p _ {j} \\ 1 & \text { otherwise } \end{array} \right.\tag{5}
$$

$p _ { j }$ and q denote the preference and indifference thresholds for criterion j (p<sub>j</sub>≥q<sub>j</sub>≥0).

Let $D _ { x , y } = \{ j \in G$ such that $g _ { j } ( \mathbf { y } ) - g _ { j } ( \mathbf { x } ) \geq p _ { j } \}$ be the discordance coalition with xSy. When g contains cardinal information, the intensity of discordance is measured in comparison with a veto threshold $\nu _ { j } ,$ which is the maximum difference $g _ { j } ( \mathbf { y } ) - g _ { j } ( \mathbf { x } )$ compatible with σ(x, $\mathbf { y } ) > 0$ . Following [19], we shall use here a simpli<sup>fi</sup>cation of the original formulation of discordance indices in the ELECTRE-III method which is given by

$$
N d (x, y) = \min _ {j \in D _ {x, y}} \left[ 1 - d _ {j} (x, y) \right]\tag{6}
$$

$$
d _ {j} (\boldsymbol {x}, \boldsymbol {y}) = \left\{ \begin{array}{c} 1 \text {   iff   } \nabla_ {j} \geq v _ {j} \\ \nabla_ {j} - u _ {j}) / \left(v _ {j} - u _ {j}\right) \text {   iff   } u _ {j} <   \nabla_ {j} <   v _ {j} \\ 0 \text {   iff   } \nabla_ {j} \geq v _ {j} \end{array} \right.\tag{7}
$$

where $\nabla _ { j } = g _ { j } ( \mathbf { y } ) - g _ { j } ( \mathbf { x } )$ and $u _ { j }$ is a discordance threshold (see Fig. 2). Using the product operator as t-norm, Eq. (3) turns into

$$
\sigma (x, y) = c (x, y) \cdot (1 - d (x, y)).\tag{8}
$$

Similar models have been implemented in other DSSs (e.g. [5,20]). Other fuzzy outranking models have been used in [3,8].

## 4.2. Method for obtaining fuzzy outranking model parameters

Expression (8) assumes that model parameter values (weights, thresholds) have been assigned. Henceforward, when we want to insist on the fact that σ value depends on such assignment we shall write σ(x,y,p).

Below is brie<sup>fl</sup>y described the method proposed in [11] to infer the parameters of an outranking model in multicriteria classi<sup>fi</sup>cation problems. This method extends directly to the competitiveness classi-<sup>fi</sup>cation model.

![](/api/attachments/S8MDX8ZG/fulltext/images/198a1b70b837099c760702aa4c13319ebbbbeba304cbbf25f8521b66f4eb16e5.jpg)  
Fig. 2. Partial discordance relation d<sub>j</sub>(x,y).

De<sup>fi</sup>nition 1. For a set of parameters p, we de<sup>fi</sup>ne the following binary relations over T×T:

$$
\begin{array}{l} (a, b) \in S (\lambda) \text {   iff   } \sigma (a, b, p) \geq \lambda (\lambda - \text { outranking }) \\ (a, b) \in P (\lambda) \text {   iff   } \sigma (a, b, p) \geq \lambda \land \sigma (b, a, p) <   0. 5 (\lambda - \text { strict   preference }) \\ (a, b) \in Q (\lambda) \text {   iff   } \sigma (a, b, p) \geq \lambda \land 0. 5 \leq \sigma (b, a, p) <   \lambda (\lambda - \text { weak   preference }) \\ (a, b) \in R (\lambda) \text {   iff   } \sigma (a, b, p) <   \lambda \land \sigma (b, a, p) <   \lambda (\lambda - \text { incomparability }). \end{array}
$$

For each $( \mathbf { a } , \mathbf { b } ) \in T \times T ,$ if the model $\sigma ( \mathbf { a } , \mathbf { b } , \mathbf { p } )$ is correct, there should be a correspondence between the categorization of a,b and preference, indifference and incomparability relations, de<sup>fi</sup>ned above. It is convenient to de<sup>fi</sup>ne the following sets:

$$
\begin{array}{l} D _ {P} = \Big \{(a, b) \in P (\lambda) \text { with } C (a) = C _ {j}, C (b) = C _ {k} \text { where } k > j \Big \} \\ D _ {Q} = \Big \{(a, b) \in Q (\lambda) \text { with } C (a) = C _ {j}, C (b) = C _ {k} \text { where } k > j \Big \} \\ D _ {I} = \Big \{(a, b) \in I (\lambda) \text { with } C (a) = C _ {j}, C (b) = C _ {k} \text { where } j \neq k \Big \} \\ C _ {S} = \Big \{(a, b) \in S (\lambda) \text { with } C (a) = C _ {j}, C (b) = C _ {k} \text { where } j \geq k \Big \}. \end{array}
$$

The <sup>fi</sup>rst three sets re<sup>fl</sup>ect inconsistencies of the reference information model. Let's denote cardinalities of the above sets by n , n , n , and $n _ { S } ,$ respectively. Obviously, these values depend on p. According to [11] we propose to infer model parameters from the solution of the following multiobjective optimization problem:

Maximize P $\left( n _ { P } , n _ { Q } , n _ { I } \right)$ ; Maximize n<sub>S</sub>:

ð<sup>9</sup>Þ

As in [11] we propose to employ NSGA-II algorithm [6], which is the benchmark in evolutionary methods of multiobjective optimization. Individual's structure and parameters of the evolutionary algorithm are similar to the implementation in [11], although with a noticeable difference in the size of the individual.

Individuals are represented by a string composed of 5N+1 positions as is shown in Fig. 3. For a detailed description of this evolutionary approach see [11].

## 4.3. Model exploitation with THESEUS method

According to [9], under outranking-based sorting methods, and as a consequence of incomparability, the capacity of a reference set for making well-determined assignments (a suf<sup>fi</sup>ciently narrow range of categories to which an object can be assigned) is related to an appropriate characterization of the categories. If a reference set should characterize the decision policy, a single reference action representing each category may be insuf<sup>fi</sup>cient ([12]). Each new element in the reference set is a piece of information which may contribute to a better characterization of its category, and the sorting method should be able to take advantage of this additional information. Here, we use the THESEUS multi-criteria sorting method proposed in [9]. In comparison with other outranking sorting methods, THESEUS can handle more reference information, thus providing more appropriate assignments.

Once the model parameters have been found as in Section 4.2, the relations (P,Q,I) correspond to the information in T. An element of T can only belong to one category, but there may be several, even plenty of elements of that set in the same evaluation category. To emphasize this idea, the notation $\mathbf { b } ^ { k , h }$ will be henceforward used to identify an element of T that is evaluated in the category $C _ { k } , \mathrm { i } . \mathbf { e } . , C ( \mathbf { b } ^ { k , h } ) = C _ { k } .$ Now, let's consider a new object $\mathbf { x } \in U .$ . For each $\mathbf { b } ^ { k , h } \in T ,$ , one of the following assumptions must be true:

$$
\begin{array}{l l} \text {A.} (x, b ^ {k, h}) \in P (\lambda); \\ \text {B.} (x, b ^ {k, h}) \in Q (\lambda); \\ \text {C.} (x, b ^ {k, h}) \in I (\lambda); \\ \text {D.} (b ^ {k, h}, x) \in P (\lambda); \\ \text {E.} (b ^ {k, h}, x) \in Q (\lambda); \\ \text {F.} (b ^ {k, h}, x) \in R (\lambda). \end{array}
$$

The core idea of THESEUS method is to identify an evaluation of x that is as compatible as possible with P, Q and I [9]. It is a decision-making problem where the best statement $E _ { j } = " \mathbf { x }$ should be assigned to $C _ { j }$ category” should be selected. The quality of the decision of selecting $E _ { j }$ should depend on the strength of the arguments against that statement. If the opposition against $C _ { j }$ is stronger than the opposition against $C _ { i } ,$ the last one should be a better evaluation.

Given a pair (x,C ) and a <sup>fi</sup>xed value of λ, let's de<sup>fi</sup>ne the following sets:

$$
\begin{array}{l} D _ {P} ^ {\prime} = \Big \{b ^ {k, h} \in T \text {   so   that   } j > k \text {   and   } \Big (b ^ {k, h}, x \Big) \in P (\lambda) \Big \} \\ D _ {Q} ^ {\prime} = \Big \{b ^ {k, h} \in T \text {   so   that   } j > k \text {   and   } \Big (b ^ {k, h}, x \Big) \in Q (\lambda) \Big \} \\ D _ {I 1} ^ {\prime} = \Big \{b ^ {k, h} \in T \text {   so   that   } | j - k | \geq 2 \text {   and   } \Big (b ^ {k, h}, x \Big) \in I (\lambda) \Big \} \\ D _ {I 2} ^ {\prime} = \Big \{b ^ {k, h} \in T \text {   so   that   } | j - k | = 1 \text {   and   } \Big (b ^ {k, h}, x \Big) \in I (\lambda) \Big \}. \end{array}
$$

Inconsistencies included in $D ^ { \prime } { } _ { I 2 }$ may be consequences of the “granularity” of description. The above sets re<sup>fl</sup>ect inconsistencies existing between the already <sup>fi</sup>tted model and the possibility to classify the new object within $C _ { j }$ category. Let's denote cardinalities relative to the above sets by $n _ { P } ^ { \prime } , n _ { Q } ^ { \prime } , n _ { I 1 } ^ { \prime }$ and $n ^ { \prime } { } _ { I 2 } .$ The problem of assigning x is a decision making situation in which the alternatives are elements of $\mathbf { c t } ,$ , i.e., statements $E _ { j } ,$ taking into account the values of $n _ { P } ^ { \prime } , n _ { Q } ^ { \prime } ,$ n $' _ { I 1 } , n ^ { \prime } _ { I 2 }$ that represent the arguments against each assignment.

THESEUS considers the following functions of $E _ { j } \colon$

$$
N _ {1} = n _ {P} ^ {\prime} + n _ {Q} ^ {\prime} + n _ {1 I} ^ {\prime}\tag{10}
$$

$$
N _ {2} = n _ {2 I} ^ {\prime}\tag{11}
$$

and the assignment of x is performed by minimizing $( N _ { 1 } , N _ { 2 } )$ under lexicographic priority favoring $N _ { 1 }$

Once C(x) has been obtained, the position of x in the complete ranking of the set $T \cup \{ { \bf x } \}$ can be obtained by comparing C(x) with $C ( \mathbf { y } )$ for al $\mathbf { y } \in T .$ . Such comparisons are performed according to:

C x better thanC $\left( b ^ { k , h } \right) \Rightarrow x$ is ranked better than every y∈T such that ${ \mathsf { C } } ( y ) = C _ { k } ;$

<table><tr><td> $u_1$ </td><td> $v_1$ </td><td> $u_2$ </td><td> $v_2$ </td><td>...</td><td>...</td><td> $u_N$ </td><td> $v_N$ </td><td> $w_1$ </td><td>...</td><td> $w_N$ </td><td> $q_1$ </td><td>...</td><td> $q_N$ </td><td> $p_1$ </td><td>...</td><td> $p_N$ </td><td> $\lambda$ </td></tr></table>

Fig. 3. Individual coding.

C x worse than $\widehat { \mathbf { \xi } } _ { { \mathrm { { r } } } } \left( \boldsymbol { b } ^ { k , h } \right) \Rightarrow x$ is ranked worse than every $y \in T$ such that $\mathsf C ( y ) = C _ { k }$

$\mathrm { I f } C ( \mathbf { x } ) = C ( \mathbf { b } ^ { k , h } )$ , x is ranked better than $\mathbf { b } ^ { k , h }$ if and only $\mathrm { i f } F _ { n } ( \mathbf { x } ) { > } F _ { n } ( \mathbf { b } ^ { k , h } )$ where $F _ { n }$ is the net <sup>fl</sup>ow score given by $\begin{array} { r } { F _ { n } ( a ) = \Sigma _ { c \in A - \{ a \} } [ \sigma ( a , c ) - \sigma ( c , a ) ] } \end{array}$ $A { = } T \cup \{ \mathbf { x } \}$

## 5. CORE system implementation

As the subject matter of the agreement made with the Sinaloa State Government and the National Council of Science and Technology (CONACyT), we have developed the system CORE (acronym of Competitiveness Analysis of Regional Entities) for the analysis and evaluation of competitiveness of municipalities in the State of Sinaloa, and by extension, of the regions all over the country. The system was developed upon request of the Government of Sinaloa, with the principal aim to analyze and evaluate competitiveness of the municipalities of this state, and make comparisons with the rest of the country. Naturally, CORE can be used to analyze any Mexican region. Below are described main functions of the system:

$$
\text { Administration }: \left\{ \begin{array}{c} \text { Reference   example   storing } \\ \text { Inclusion   of   a   new   reference   element } \\ \text { Inclusion   of   a   new   region   to   be   evaluated } \\ \text { Inference   of   outranking   model   parameters } \end{array} \right.
$$

Reportsandanalysesof competitiveness

Assignment of competitiveness category Evaluation of factors of competitiveness Assignment of competitiveness rank “What if” analysis for competitiveness

A reference set must be provided to CORE. This set should be composed of objects described as (name, values of the explanatory variables, competitiveness category). Such information could be provided by human experts, or be obtained from existing data bases and “proxy” measures of competitiveness. This reference set is the basis for applying the method by Fernandez et al. [11] in order to infer the parameters of a fuzzy outranking relation.

Competitiveness analysis in CORE is based on solving a multi-criteria sorting problem with THESEUS method. Some advantages of such approach were discussed in Section 3.1.1. Given an object x (representing certain territorial entity), with a known description in terms of the set of explanatory variables, CORE assigns x to one competitiveness category. Analysis “what if” is performed by the user by modifying one or several explanatory variables. Relative rank of x may be suggested by combining its assignment with additional information provided by the fuzzy outranking relation.

## 5.1. Reference example storing

CORE contains the information provided by IMCO [16]. This database includes information about 390 reference municipalities, each one characterized by 122 causal variables. These variables are grouped together into the following ten factors:

\- Reliable and objective legal system

\- Sustainable environmental management

\- Inclusive, prepared and healthy society

\- Dynamic economy and stable indicators

\- Stable and functional political system

\- Markets of ef<sup>fi</sup>cient factors (capital, labor and energy)

\- World class precursor sectors (telecommunications, transportation and <sup>fi</sup>nancial sector)

\- Ef<sup>fi</sup>cient and effective governance

\- Good use of international relations

\- Economic sectors with potential.

Together with the measure of competitiveness (municipality's gross domestic product), IMCO's database provides a measure of each of the ten factors calculated in corresponding terms of the functional model $U ( \mathbf { x } ) = w _ { 0 } + w _ { 1 } x _ { 1 } + \ldots \ w _ { N } x _ { n }$ that approaches the CP measure.

By partitioning the range of municipality's gross domestic product the CORE system can associate every regional entity with a category on a scale of competitiveness {Very low, Low, Below average, Average, Above average, High, Very high}. This scale can be easily modi<sup>fi</sup>ed. In each of the ten factors mentioned above, each regional entity is grouped according to the same scale. After this processing, each of the 390 regional entities from the IMCO's database is described by a vector of 122 causal variables together with a vector of 11 dependent variables; ten of them correspond to the above factors; the rest is the general evaluation of competitiveness.

CORE offers the possibility to modify the reference information; the description of any of 390 municipalities can be edited or a new reference entity can be added. A subset can be taken from the IMCO's database as a reference set; thus, THESEUS classi<sup>fi</sup>cation method can be used in CORE to evaluate objects that are in IMCO's own information base and compare results.

CORE is prepared to easily emigrate towards other sets of explanatory variables, factors of competitiveness and reference information. The mandatory structure of reference data is (name, values of the explanatory variables, competitiveness category). Such information may be provided by human experts, or be obtained from existing data bases and “proxy” measures of competitiveness, as done with the IMCO's database and municipality's gross domestic product.

## 5.2. Inclusion of new objects for evaluation

This function allows stating names and description of variables of new regional entities whose analysis is wanted, but that are not included in the reference database.

## 5.3. Inference of outranking model parameters

Once the reference information is stored or updated, the method in [11] is applied to infer the outranking model parameters (weights and veto thresholds) as was discussed in Section 4.2.

## 5.4. Reports and analyses of competitiveness

One or various objects whose description in 122 dimensions is already present in the information database is/are selected (Fig. 4). For these objects, the system offers the following reports:

Evaluation of factors of competitiveness;

Assignment of competitiveness (Fig. 5).

The rank of objects selected within the entire set of objects whose description in 122 causal variables is available (Fig. 6).

These reports, combined with the capacity for editing information on the status of causal variables, allow carrying out the “what if” analysis: to analyze which effects the changes of these variables produce on the evaluation of competitiveness, or on the position that a determined regional entity occupies in the general ranking. An exploration can determine the causal variables that can most cheaply improve the category of competitiveness in the context of any regional entity.

A typical work session with CORE involves exploration and decision phases. As example, let us suppose that the Major of Culiacan wants a higher category for his/her city that would also result in a higher rank as compared to some other Sinaloa municipalities (El Fuerte, Mazatlan, Los Mochis). At the current stage Culiacan is sorted as $\mathbf { \ " } \mathrm { A v e r a g e " }$ (see Fig. 5) and ranked 142nd in the set of municipalities included in CORE's

![](/api/attachments/S8MDX8ZG/fulltext/images/655ed3b26e5a434eb45b4aa5225b5918e6de246f9f06a9b3c9e5b8682f557915.jpg)  
Fig. 4. Selection of municipalities and causal variables

database (see Fig. 6). Among many explanatory variables, only three variables are selected by the Major to perform the “what if” analysis (see Fig. 4). Such selection is determined by the Major's beliefs about how easy or cheap may be to achieve their improvement. Culiacan competitiveness is evaluated and ranked under better values of those causal variables. This search process is a simulation since the actual competitiveness has not been modi<sup>fi</sup>ed. CORE is answering the question “how would change Culiacan competitiveness if those variables were improved to reach certain levels?” Maybe after some trials the Major <sup>fi</sup>nds the values in Fig. 7, which are subsequently used by the competitiveness simulator to provide the results in Figs. 8 and 9. This ends the current exploration phase. The Major may accept the prescription and design good strategies to achieve the levels shown in Fig. 7 (decision phase). Or he/she may perform other exploration with additional causal variables. This process continues until obtaining a completely satisfactory prescription.

## 6. Some experimental results

The IMCO's database is used as reference set. By partitioning the range of municipality's gross domestic product, each regional entity is assigned to a category on a scale of competitiveness {Very low, Low, Below average, Average, Above average, High, Very high}. Table 2 shows the information on the number of municipalities by their level of competitiveness.

![](/api/attachments/S8MDX8ZG/fulltext/images/8b5ccf6d19c020529a29a7d7bb25e57eb0a076c5bf7fce07cf86078ea5e42896.jpg)  
Fig. 5. Assignment of competitiveness.

![](/api/attachments/S8MDX8ZG/fulltext/images/e0cb65594e364ff07de06b02cbd8b8a61ee3df9e9f420adc18d41e9b704fe10a.jpg)  
Fig. 6. General rank.

There are more than 2400 municipalities in Mexico. To estimate the capacity to correctly classify municipalities not belonging to the set of 390 we took as reference, the following experiment was carried out: each of the 390 municipalities with known evaluation was evaluated by CORE using as reference set the remaining 389 objects; the assignment suggested by the system was compared with the known assignment. The results were very satisfactory. In 390 cases, there were 363 coincidences between the assignments proposed by CORE and the actual assignments. With only 27 non-coincidences the classi<sup>fi</sup>cation accuracy was 93.07%. In 14 cases of error the system suggested to assign the object to a category adjacent to the actual one. Although interaction among explanatory variables is not considered by the model of Eqs. (4)–(8), the <sup>fi</sup>tted fuzzy outranking model combined with THESEUS sorting method provides satisfactory results. As was discussed in [1,9,12], more examples in the reference set will provide better results. In comparison, the classi<sup>fi</sup>cation accuracy provided by the IMCO's linear regression model was only 75%.

## 7. Conclusions

If the regional competitiveness can be understood as capacity to attract and preserve investments, then the perception investors have of the region's characteristic is fundamental. This perception, either positive or negative to different extents, is a result of a complex integration of multiple criteria. This paper has perhaps the merit of enlightening the competitiveness analysis from a dominant multicriteria perspective. The competitiveness evaluation is here considered as a multicriteria sorting problem. In CORE decision support framework, the new outranking-based THESEUS method is applied to making the assignments of regional entities to competitiveness categories. This method performed very well analyzing the competitiveness of 390 Mexican regional entities, which is the universe of the currently available information. The model of competitiveness based on constructing a weightedsum function is clearly outperformed.

![](/api/attachments/S8MDX8ZG/fulltext/images/b45b0ad7e61b88e24b6e3321e95afb45d6c5fbdc1343786408913ef8de86a287.jpg)  
Fig. 7. New values of some causal variables.

![](/api/attachments/S8MDX8ZG/fulltext/images/04adbb1ebb57f01d90ab4db9a0fcc3d6e1341656518e48e7c13d0b4db67adc75.jpg)  
Fig. 8. Improved competitiveness.

CORE declines to construct an index of competitiveness for several reasons: i) limitations of weighted sum function models that are unable to re<sup>fl</sup>ect preference dependence, veto, incomparability and lack of compensation; ii) arbitrariness of some parameters appearing in the indices; iii) competitiveness is a complex, integrating concept, which does not allow description by one sole economic dimension; its evaluation is essentially indirect; and iv) if there are attempts to use evaluations of human experts, these latter feel more comfortable when expressing their judgments in qualitative scales. CORE substitutes the numerical measure of an index for an evaluation within categories in a scale that can be enough subtle as to agree with user's wishes. The response is coarser than that of an index, but considerably more robust and consistent with approximate and indirect character of the input information.

CORE is a tool placed at a disposal of the Government of Sinaloa and the rest of the country. This system, which re<sup>fl</sup>ects in a robust way the level of competitiveness of different regions, allows governments to better de<sup>fi</sup>ne their policies by placing <sup>fi</sup>nancial resources more ef<sup>fi</sup>ciently. Although the present version of CORE uses causal variables, factors and reference information from the Mexican Institute for Competitiveness, the system is conceived to easily emigrate towards other sets of explanatory variables, factors of competitiveness and reference information.

![](/api/attachments/S8MDX8ZG/fulltext/images/076e0513dee91b3f3b52603421c74ca697843967f615ecd2f213dfe2312f8d54.jpg)  
Fig. 9. Improved rank order.

Table 2  
Total of municipalities by category.

<table><tr><td>Competitiveness</td><td>Number of municipalities</td></tr><tr><td>Very high</td><td>3</td></tr><tr><td>High</td><td>12</td></tr><tr><td>Above average</td><td>79</td></tr><tr><td>Average</td><td>109</td></tr><tr><td>Below average</td><td>114</td></tr><tr><td>Low</td><td>65</td></tr><tr><td>Very low</td><td>8</td></tr></table>

## Acknowledgments

We acknowledge the support from the National Council for Science and Technology (CONACyT) and the Government of Sinaloa (projects CONACyT 57255 and Sin-2007-C01-70978).

## References

[1] J. Almeida-Dias, J. Figueira, B. Roy, A multiple criteria sorting method where each category is characterized by several reference actions: the ELECTRE TRI-NC method, European Journal of Operational Research 217–3 (2012) 567–579.

[2] S. Angilella, S. Greco, F. Lamantia, B. Matarazzo, Assessing non-additive utility for multicriteria decision aid, European Journal of Operational Research 158 (2004) 734–744.

[3] J.P. Brans, B. Mareschal, The PROMCALC & GAIA decision support system for multicriteria decision aid, Decision Support Systems 12 (1994) 297–310.

[4] Y. Chen, D.M. Kilgour, K.W. Hipel, Screening in multiple criteria decision analysis, Decision Support Systems 45–2 (2008) 278–290.

[5] S. Damart, L.C. Dias, V. Mousseau, Supporting groups in sorting decisions: methodology and use of a multi-criteria aggregation/disaggregation DSS, Decision Support Systems 43–4 (2007) 1464–1475.

[6] K. Deb, Multi-Objective Optimization using Evolutionary Algorithms, John Wiley & Sons, Chichester-New York-Weinheim-Brisbane-Singapore-Toronto, 2001.

[7] M. Doumpos, C. Zopounidis, Multicriteria Decision Aid Classi<sup>fi</sup>cation Methods, Kluwer Academic Publishers Dordrech-Boston-London. 2002

[8] M. Doumpos, C. Zopounidis, A multicriteria decision support system for bank rating, Decision Support Systems 50–1 (2010) 55–63.

[9] E. Fernandez, J. Navarro, A new approach to multicriteria sorting problems based on fuzzy outranking relations: the THESEUS method, European Journal of Opera tional Research 213 (2011) 405–413.

[10] E. Fernandez, J. Navarro, A. Duarte, Multicriteria sorting using a valued preference closeness relation. European Journal of Operational Research 185 (2008) 673-686.

[11] E. Fernandez, J. Navarro, S. Bernal, Multicriteria sorting using a valued indifference relation under a preference-disaggregation paradigm, European Journal of Operational Research 198 (2009) 602–609.

[12] J. Figueira, S. Greco, B. Roy, R. Słowiński, ELECTRE methods: main features and recent developments, in: C. Zopounidis, P. Pardalos (Eds.), Handbook of Multicriteria Analysis, Applied OptimizationSpringer, Heidelberg, 2010, pp. 51–89, (Dordrecht London New York).

[13] J. Fodor, M. Roubens, Fuzzy Preference Modeling and Multicriteria Decision Support, Kluwer, Dordrecht, 1994.

[14] M. Grabisch, The application of fuzzy integrals in multicriteria decision making, European Journal of Operational Research 89 (1996) 445–456.

[15] S. Greco, B. Matarazzo, R. Slowinski, Rough sets theory for multicriteria decision analysis, European Journal of Operational Research 129 (2001) 1–47.

[16] IMCO, State competitiveness. Aspirations and reality.(In Spanish) http://imco.org. mx/imco/docbase/capitulosPublications/archivoCapitulo(93).pdf 2008.

[17] W.A. Lewis, Economic development with unlimited supplies of labour, The Manchester School 22–2 (1954) 139–191.

[18] J.L. Marichal, M. Roubens, Determination of weights of interacting criteria from a reference set, European Journal of Operational Research 124 (2000) 641–650.

[19] V. Mousseau, L.C. Dias, Valued outranking relations in ELECTRE providing manageable disaggregation procedures, European Journal of Operational Research 156–2 (2004) 467–482.

[20] E. Natividade-Jesus, J. Coutinho-Rodriguez, C. Henggeler-Antunes, A multicriteria decision support system for housing evaluation, Decision Support Systems 43–3 (2007) 779–790.

[21] F. Perroux, Economic space: theory and applications, Quarterly Journal of Economics 64 (1950) 89–104.

[22] M. Porter, The Competitive Advantage of Nations, The Free Press, New York, 1990.

[23] B. Roy, The outranking approach and the foundations of ELECTRE methods, Theory and Decision 31 (1991) 49–73.

[24] X. Sala-i-Martin, G. Doppelhofer, R.I. Miller, Determinants of long-term growth: a Bayesian averaging of classical estimates (BACE) approach, The American Eco nomic Review 94–4 (2004) 813–835, (http://www.jstor.org/stable/3592794).

[25] WEF, The World Competitiveness Report 2009–2010.Geneve http://www.weforum. org/documents/GCR09/index.html 2009.

[26] C. Zopounidis, M. Doumpos, Building additive utilities for multi-group hierarchical discrimination: the M.H.DIS method, Optimization Methods and Software 14–3 (2000) 219–240.

Eduardo Fernandez was born in Cuba in 1951. He received the BSc degree in Physics from the University of Havana in 1973; the PhD degree in Computer Aided Design of Electronic Circuits, from Poznan University of Technology in 1987. He is currently Senior Professor of the Faculty of Civil Engineering, Autonomous University of Sinaloa (UAS), Mexico. His main areas of interest are multi-criteria and intelligent decision support.

Professor Fernandez is a member of the Mexican National System of Researchers, the International Society on Multi Criteria Decision Making, the Euro Working Group on Multi-Criteria Decision, and the Ibero-American Network on Multi-Criteria Decision He has been nominated three times for “OR in Development” Prize.

Jorge Navarro was born in Mexico in 1965. He received the BSc degree in Mathematics, the MSc and PhD degrees in computer science from the Autonomous University of Sinaloa in 1989, 2000 and 2005 respectively. He is currently Senior Professor of the Faculty of Computer Science, Autonomous University of Sinaloa. His main areas of interest include multi-criteria and intelligent decision support.

Professor Navarro is a member of the Mexican National System of Researchers and the Ibero-American Network on Multi-Criteria Decision. He has been nominated twice fo “OR in Development” Prize.

Alfonso Duarte was born in Mexico, in 1980. He received the BSc degree in Computer Science from the Autonomous University of Sinaloa in 2001. He is currently Assistant Professor in the University of Occidente. He was nominated for “OR in Development” Prize.

Guillermo Ibarra was born in Mexico in 1954. He received the BSc, MSc and PhD degrees in Economy from the Autonomous University of Sinaloa (1976), and from the National Autonomous University of Mexico (UNAM) in 1983 and 1993 respectively. He is now a senior professor in the Faculty of International Studies and Public Policies, Autonomous University of Sinaloa. His main area of interest includes competitiveness analyses. His latest book is “Santa Monica, the rising of a sustainable city” (2011), JP Editor.

Professor Ibarra is a member of the Mexican National System of Researchers, the Acad emy of Political Science, and the American Historical Association.
