---
otero_id: 7670
otero_key: "SJFEAKGW"
title: "Parametric evaluation of research units with respect to reference profiles"
authors: "Miłosz Kadziński; Roman Słowiński"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.02.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Miłosz Kadziński <sup>a,</sup>⁎, Roman Słowiński <sup>a,b</sup>

<sup>a</sup> Institute of Computing Science, Poznań University of Technology, Poznań, Poland

<sup>b</sup> Systems Research Institute, Polish Academy of Sciences, Warsaw, Poland

## a r t i c l e i n f o

Article history: Received 21 January 2014 Received in revised form 30 January 2015 Accepted 3 February 2015 Available online 8 February 2015

Keywords: Multiple criteria decision aiding Reference pro<sup>fi</sup>les Outranking Inference procedure Class cardinalities Parametric evaluation

## a b s t r a c t

We introduce a method that jointly considers multiple criteria sorting and ranking. The method derives from a real-world problem of parametric evaluation of research units carried out by the Polish Ministry of Science and Higher Education. It assigns the units to three classes representing different qualities of both acquired effects and activities undertook in the evaluation period. Although units placed in the same class are guaranteed the same level of funding, they are not considered indifferent in the subsequent analysis and, thus, need to be ordered from the best to the worst in each class. A proposed outranking relation compares the units pairwise and the result is exploited so as to get a ranking of the units. The ranking is transformed to class assignments based on the attained comprehensive scores and ranks. To enhance interpretability of the results, we infer two reference pro<sup>fi</sup>les (arti<sup>fi</sup>cial reference research units) separating the classes so that each class accumulates units ranked not worse than the corresponding lower pro<sup>fi</sup>le and worse than the respective upper pro<sup>fi</sup>le. The procedure takes into account desired cardinalities of classes, i.e., shares of units that are judged as leading, average, or weak. We discuss several procedures with different ways of inferring the reference pro<sup>fi</sup>les and scoring the units. We also analyze robustness of the results.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Each multiple criteria decision aiding (MCDA) method is distinguished by the type of admitted preference information, the procedures used to construct a preference model, and the techniques used to work out a <sup>fi</sup>nal recommendation [36]. Usually, these methods are designed for dealing with either ranking and choice (e.g., [8,20,37,46]) or sorting problems (e.g., [9,19,32]). In this paper, we introduce a novel MCDA method able to deal with multiple criteria sorting and ranking considered jointly. Its development has been motivated by the speci<sup>fi</sup>c requirements of the Polish Ministry of Science and Higher Education facing a real-world problem of the parametric evaluation of research units.

Every 3 years, the ministry is carrying out an evaluation of research units applying for the statutory activity funds. This evaluation, called categorization, is performed within groups of few tens of units having similar activity pro<sup>fi</sup>les, called groups of joint evaluation (GJE). The categorization consists in assigning each unit of a GJE to one of three classes corresponding to different qualities of both acquired effects and activities undertook in the evaluation period. These effects and activities are represented by four independent criteria. The assignment procedure needs to respect desired cardinalities of classes, i.e., shares of alternatives that can be judged as leading, average, or weak units (see [33,40,50]). Let us emphasize that multiple criteria evaluation of education and/or research quality of different units, universities, cities, and countries is an appealing issue that has recently motivated a wide variety of studies (see, e.g., [10,23,38]).

In our application, the research units from a GJE assigned to the same class are getting the same funding level. However, they are not considered indifferent in the subsequent analysis. It is the case since the Ministry would like to differentiate over- and underperforming units within each class, to potentially distinguish a small subset of the leading research units that merit additional funds in case they prove clearly better than the remaining units, and to provide all of them with a feedback on their effectiveness against all other units. This indicates the need for ordering the units within a given GJE from the best to the worst one.

The ranking is transformed to class assignments based on the attained comprehensive scores and ranks. To enhance the interpretability of the results, some reference pro<sup>fi</sup>les (arti<sup>fi</sup>cial reference research units) separating the classes need to be constructed so that each class accumulates the units not worse than the corresponding lower pro<sup>fi</sup>le and worse than the respective upper pro<sup>fi</sup>le. The need for inclusion of the reference pro<sup>fi</sup>les in the method was indicated by the representatives of the Ministry. Moreover, within the method, the existing research units need to be considered jointly with the reference pro<sup>fi</sup>les. This requirement implies that one cannot <sup>fi</sup>rst rank the existing units and only then discover the pro<sup>fi</sup>les dividing the ranking into pre-de<sup>fi</sup>ned proportions so that to separate the classes. Instead, the ranking and class assignments need to be constructed simultaneously. Respecting desired class cardinalities imposes constraints on the ranks attained by the reference pro<sup>fi</sup>les.

Let us note that decision aiding in the context of traditional sorting problems with unsized classes is based on the absolute evaluation of each alternative to be assigned. Considering the alternatives' intrinsic values, e.g., all of them can be assigned to the same class while some other classes may remain empty [2]. When taking into account desired class cardinalities, this formulation of the sorting problem does not hold. Considering such requirements creates a partial dependence between the alternatives and implies the need for introducing a relative comparison approach. This can be achieved by integrating the constraints on the class cardinality into the assignment process. Even if the relative comparisons need to be performed, this does not contradict, however, the interpretability of the pre-de<sup>fi</sup>ned and ordered decision classes. First, it is the particular decision aiding context that provides constraints on the size of the classes. Second, the de<sup>fi</sup>nition of decision classes in sorting problems is <sup>fi</sup>rst and foremost related to the way in which alternatives assigned to each class would be further processed. This treatment needs to be the same for all alternatives assigned to the same class, which holds for our problem in the phase related to granting the funds.

When comparing the alternatives in a pairwise fashion with respect to their performances on all criteria, we wish to avoid compensatory aggregation of scienti<sup>fi</sup>c achievements measured on different scales. Thus, each criterion is characterized by the following parameters: its weight, expressing its relative importance with respect to other criteria, as well as by its indifference and preference thresholds corresponding to the differences between performances of units compared pairwise on this criterion that are negligible or signi<sup>fi</sup>cant, respectively. In other words, the indifference and preference thresholds permit to discriminate between indifference, weak preference, and strict preference in a pairwise comparison of units on this criterion. The comparison of a pair of units on all criteria is then summarized by a valued outranking relation de<sup>fi</sup>ned in a speci<sup>fi</sup>c way.

The rank of each unit (including existing research units and reference pro<sup>fi</sup>les) and, thus, the corresponding assignment is determined by its comprehensive score resulting from exploiting the outranking relation on the set of all units using the net <sup>fl</sup>ow score (NFS) procedure (see, e.g., [4,45]). Generally speaking, this procedure assigns to each alternative $a \in A { \textbf { a } }$ “measure of its desirability” by aggregating arguments which are in favor of its strength and weakness. We discuss different scoring procedures, which may be divided into two groups. On the one hand, a unit may get a score of one when it outranks another unit in the pairwise comparison, or no score, otherwise. Alternatively, it may be assigned a score between zero and one, corresponding to the degree of credibility of the outranking. In any case, a comprehensive score of each unit is obtained as the sum of scores corresponding to the outranking of this unit over all the others. The comprehensive score thus represents the relative power of a unit derived from its pairwise comparisons with all remaining units. Since the existing research units and reference pro<sup>fi</sup>les are considered jointly in the ranking procedure, let us emphasize that each existing research unit (reference pro<sup>fi</sup>le) is compared against all reference pro<sup>fi</sup>les (existing units) and the remaining existing units (reference pro<sup>fi</sup>les).

Let us remind that reference pro<sup>fi</sup>les have been already used in different contexts in MCDA. For example, in the ELECTRE Tri sorting method (see, e.g., [48,14]), the class pro<sup>fi</sup>les are interpreted as bounds between the classes. Traditionally, these pro<sup>fi</sup>les had to be provided directly by the decision maker (DM), but various elicitation techniques for admitting indirect preference information have been proposed. In particular, Mousseau and Słowiński [41] suggest to infer the ELECTRE Tri preference model parameters from the assignment examples given by the DM, using non-linear optimization. Further, Ngo The and Mousseau [42] use mixed-integer linear programming (MILP) to infer these class pro<sup>fi</sup>les, considering other parameters as <sup>fi</sup>xed. Moreover,

Cailloux et al. [7] propose elicitation procedure to infer class pro<sup>fi</sup>les from assignment examples provided by multiple DMs. On the other hand, in ELECTRE Tri-C [3] and ELECTRE Tri-rC [35], the alternatives are not compared against the class boundaries but rather with characteristic pro<sup>fi</sup>les that contain the representative description of each class. Finally, Rolland [43] introduce decision rules using reference pro<sup>fi</sup>les (levels) for multiple criteria ranking. The results show that employing reference levels overcomes the usual weakness of the ranking methods based on pairwise comparisons, which is the sensitivity of the ranking to the change of the considered set of alternatives. The disaggregation approach for inferring these pro<sup>fi</sup>les in an indirect way is discussed by Zheng [49].

The organization of the paper is as follows. In the next section, we introduce notation that will be used along the paper. The decision aiding process with the proposed method is described in Section 3. The details of mathematical preference modeling underlying the introduced approach are outlined in Sections 4 and 5. They concern the de<sup>fi</sup>nition of the employed model, procedures for deriving recommendation with the use of reference pro<sup>fi</sup>les selected according to some prede<sup>fi</sup>ned rules, as well as algorithms for analyzing robustness of the suggested recommendation. The use of the presented method is illustrated on a problem of parametric evaluation of research units in Poland (see Section 6). Although the study consists in assigning the units to three classes, when introducing the method, we discuss a more general case with any number of classes greater than one. The last section concludes the paper.

## 2. Notation and basic concepts

We shall use the following notation:

$A = \{ a _ { 1 } , a _ { 2 } , . . . , a _ { i } , . . . , a _ { n } \} - a$ <sup>fi</sup>nite set of n alternatives (research units);

$G = \{ g _ { 1 } , g _ { 2 } , . . . , g _ { j } , . . . , g _ { m } \} - a$ <sup>fi</sup>nite set of m evaluation criteria, g $\cdot A \to \mathbb { R }$ for al $j \in J = \{ 1 , 2 , . . . , m \} ;$

$X _ { j } = \{ x _ { j } \in \mathbb { R } : g _ { j } ( a _ { i } ) = x _ { j } , a _ { i } \in A \}$ —the set of all different evaluations on $g _ { j } , j \in J ;$ we assume, without loss of generality, that the greater $g _ { j } ( a _ { i } )$ the better alternative $a _ { i }$ on criterion $g _ { j } ,$ for all $j \in J ;$

$x _ { i } ^ { 1 } , x _ { i } ^ { 2 } , . . . , x _ { i } ^ { n _ { j } ( A ) } .$ -the ordered values of $\stackrel { \cdot } { X _ { j } } , \stackrel { k } { X _ { j } } < x _ { j } ^ { k } + \stackrel { 1 } { \cup } , k = 1 , . . . , n _ { j } ( A ) -$ 1, where $\overset { \smile } { n _ { j } } ( A ) = \lvert X _ { j } \rvert$ and $\begin{array} { r } { n _ { j } ( A ) \leq n ; } \end{array}$

$C _ { h } , h = 1 , . . . , p -$ pre-de<sup>fi</sup>ned preference ordered classes such that $C _ { h + 1 }$ is preferred to $C _ { h } , h = 1 , . . . , p - 1 ; H = \{ 1 , 2 , . . . , p \} ;$

$R = \{ r _ { 1 } , . . . , r _ { p \mathrm { ~ - ~ } 1 } \}$ —reference pro<sup>fi</sup>les separating the classes; they are unknown a priori and need to be constructed according to some rules;

$B = A \cup R { - } \mathsf { a }$ set of existing alternatives and reference pro<sup>fi</sup>les which are all treated equally in the ranking procedure.

Outranking relation is a preference model intended to represent preferences of a DM on a set of alternatives by a pairwise comparison function:

$$
s \left(g _ {1} (a), g _ {1} (b), \dots , g _ {m} (a), g _ {m} (b)\right): \mathbb {R} ^ {2 m} \rightarrow \mathbb {R}, \quad \text { for } a, b \in A.
$$

In this study, we adopt the procedure for construction of the outranking relation used in the PROMETHEE method (see, e.g., [5,6,17, 18]). PROMETHEE and its further extensions have proven to be well suited for real-world multiple criteria problems in various areas such as, e.g., stock trading [1], equipment selection [47], bank rating [15], infrastructure assessment [21], energy market [24], outsourcing in information systems [11], or climate protection [39]. In this method, for each criterion $g _ { j } , j = 1 , . . . , m ,$ , one considers a preference function $\pi _ { j } ( a , b )$ , such that for all $a , b \in B \colon$

$$
\pi_ {j} (a, b) = F _ {j} \left(d _ {j} (a, b)\right) \in [ 0, 1 ],
$$

where $d _ { j } ( a , b ) = g _ { j } ( a ) - g _ { j } ( b )$

Let us denote by w<sub>j</sub> the weight assigned to criterion $g _ { j } , j = 1 , . . . , m ,$ expressing relative importance of g<sub>j</sub> in set G. Without loss of generality, we assume that the weights of criteria sum up to one, i.e., $\begin{array} { r } { \sum _ { j = 1 } ^ { m } w _ { j } = 1 } \end{array}$ Remark that these weights are not interpreted here as weights of criteria in a weighted sum of criteria. In the latter preference model, alike in the whole family of compensatory preference models it belongs, the weights play the role of substitution rates among criteria. In the outranking model, the weights are not multiplied by performances on the corresponding criteria but, instead, they underline the relative strength of criteria in a voting-like procedure for or against outranking of one alternative over another.

The criteria are also associated with indifference q and preference p thresholds. For consistency, $p _ { j } \ge q _ { j } \ge 0 , j = 1 , . . . ,$ m. Knowing the difference between evaluations of alternatives $a , b \in B$ on a particular criterion g , one is able to represent situations of weak or strict preference and indifference among a and b on $g _ { j } .$ . The type of relation implies value assigned to a marginal preference function $\pi _ { j } ( a , b )$

$$
\pi_ {j} (a, b) = \left\{ \begin{array}{l l} w _ {j}, & \text { if } g _ {j} (a) - g _ {j} (b) \geq p _ {j}, \\ w _ {j} \Big [ \Big (g _ {j} (a) - g _ {j} (b) \Big) - q _ {j} \Big ] \Big / \Big (p _ {j} - q _ {j} \Big) & \text { if } p _ {j} \geq g _ {j} (a) - g _ {j} (b) \geq q _ {j}, \\ 0, & \text { if } g _ {j} (a) - g _ {j} (b) \leq q _ {j}. \end{array} \right.\tag{1}
$$

Note that in case a is weakly preferred to b, we may employ different non-linear scoring schemes. In particular, we may de<sup>fi</sup>ne a middle level for the preference function, e.g. ${ \mathrm { i f } } p _ { j } \geq g _ { j } ( a ) - g _ { j } ( b ) \geq q _ { j } ,$ then $\pi _ { j } ( a , b ) =$ $0 . 5 w _ { j } .$ . Furthermore, if the DM provides a preference threshold $p _ { j }$ only, then:

$$
\pi_ {j} (a, b) = \left\{ \begin{array}{l l} w _ {j}, & \text { if } g _ {j} (a) - g _ {j} (b) \geq p _ {j}, \\ 0, & \text { if } g _ {j} (a) - g _ {j} (b) <   p _ {j}. \end{array} \right.\tag{2}
$$

To express the degree in which a is preferred to b on all criteria, we will refer to an aggregated preference index:

$$
\pi (a, b) = \sum_ {j = 1} ^ {m} \pi_ {j} (a, b) \text {   for   all   } (a, b) \in B \times B.
$$

Remark that π(a, $b ) \in [ 0 , 1 ] ,$ , where π(a, $b ) = 0 \operatorname { i f } g _ { j } ( a ) - g _ { j } ( b ) \leq q _ { j } ,$ $j = 1 , . . . ,$ , m (a is at most indifferent to b on all criteria), and $\pi ( a , b ) =$ 1 if $g _ { j } ( a ) - g _ { j } ( b ) \geq p _ { j } , j = 1 , . . . , m$ (a is strictly preferred to b on all criteria).

## 3. Decision aiding with the proposed approach

Parametric evaluation of research units can be aided with the proposed approach through the <sup>fi</sup>ve-step process illustrated in Fig. 1.

Step 1. The process begins by de<sup>fi</sup>ning the problem: a set of alternatives (research units) A (i.e., a group of joint evaluation), a set of criteria $G ,$ the units' performances on the criteria representing the quality of their effects in the evaluation period, and a set of ordered classes C.

![](/api/attachments/SJFEAKGW/fulltext/images/a611e774f76aa42f34e82e547fac36711152feab0a106d16537c699d02ea6cc1.jpg)  
Fig. 1. Decision aiding process for the proposed approach.

Step 2. Then in Step 2, the preference information is elicited. To enable comparison of units with respect to their performances, we assume that the DM provides for each criterion $g _ { j } \in G$ its weight w as well as the indifference $q _ { j }$ and preference $p _ { j }$ thresholds. Let us remind that $w _ { j }$ should be interpreted as the voting power $\operatorname { o f } g _ { j } ,$ which depends neither on the range of the criterion scale nor on the encoding chosen. For the problem of parametric evaluation of research units, the DM has a clear understanding of the importance of each criterion. Further, the indifference and preference thresholds are interpreted as, respectively, the greatest performance difference for which the situation of indifference holds on g and the smallest performance difference for which the situation of preference occurs on $g _ { j } .$

Remark that instead of the two discrimination thresholds, (s)he may provide preference threshold $p _ { j }$ only. Such model is certainly easier to explain since a sharp transition from indifference to strict preference is more intuitive for the DMs who are not familiar with the outranking methods. Nevertheless, in some decision making situations, using pseudo-criteria with a pair of comparison thresholds is appealing. In particular, it allows accounting for a situation of weak preference where neither of the two preceding situations can be distinguished as appropriate (i.e., when there are insuf<sup>fi</sup>cient reasons to deduce the strict preference in favor of one alternative, but they are clear and positive enough to invalidate the indifference between the alternatives). The experience of using outranking methods in real-world decision problems shows that the assumption about providing values for the indifference and preference thresholds is not unrealistic. Once their meaning is explained, the experts, being aware what is the precision of criteria, are able to indicate how much difference is negligible or signi<sup>fi</sup>cant.

Moreover, we assume that the DM speci<sup>fi</sup>es shares of alternatives in A that should be assigned to each class $C _ { h } , h =$ $1 , . . . , p .$ Let us denote the minimal and maximal bounds for such a share by $N _ { h } ^ { \mathrm { p e r c \cdot m i n } }$ and $N _ { h } ^ { \mathrm { p e r c \mathrm { ~ - ~ } m a x } }$ (in %). In case these are equal, we may denote the required share by $N _ { h } ^ { \mathrm { p e r c } }$ . Remark that such constraints are not related only with the preferences of the DM but also with the particular sorting context. For our problem, they are implied by a limited budget of the Ministry granting funds for a statutory activity of research units.

Prior to discovering the reference pro<sup>fi</sup>les separating the classes, the DM may de<sup>fi</sup>ne constraints with respect to their performances on different criteria. These may rely either on expert knowledge about the targets that should be satis<sup>fi</sup>ed by a unit assigned to a given class, or on results of the statistical analysis of performances attained by the units within GJE.

Finally, the proposed approach requires to assign a comprehensive score to each unit (including existing research units and reference pro<sup>fi</sup>les). First, the scoring procedure constructs an outranking relation on the set of units. Then this relation is exploited to compute for each unit its comprehensive score as a sum of scores derived from unit's pairwise comparisons against all other units. We propose several exploitation procedures, out of which the DM should choose one to be used for scoring the units. On the one hand, (s)he may wish to use a procedure with binary (win/no win) scores. It assigns a single score to a unit in case it proves better when compared pairwise with some other unit, and no score otherwise. On the other hand, (s)he may employ a scheme with continuous scores corresponding to the degree of credibility of an outranking relation. In this case, a unit is rewarded for each individual aspect in which it proves its superiority over another unit. These procedures are discussed in detail in Section 4.2.

Step 3. Step 3 consists of constructing the disaggregation model for inferring reference pro<sup>fi</sup>les compatible with the preference information provided by the DM. This model is composed of two types of constraints:

• these concerning performances of reference pro<sup>fi</sup>les to be inferred and their comparison with the existing research units, and

• constraints that guarantee that the scoring procedure would work as intended and that the resulting class assignments would respect desired class cardinalities.

For clarity, we discuss these different types of constraints separately in Sections 4.1 and 4.2. Nevertheless, they are subsequently incorporated into a single model so that both the inference of reference pro<sup>fi</sup>les and their comparison with the existing units within the joint ranking/sorting procedure are conducted simultaneously.

The desired result of applying this procedure for the case of three decision classes is presented in Fig. 2. Let us remind that the role of reference pro<sup>fi</sup>les is to transform the ranking into class assignments. Precisely, each class accumulates existing research units which are scored not worse than the respective lower pro-<sup>fi</sup>le and worse than the upper pro<sup>fi</sup>le. To respect desired class cardinalities, the construction of the pro<sup>fi</sup>les needs to account for the ranks they attain. This can be achieved by controlling the number of existing research units ranked at least as good and lower than each pro<sup>fi</sup>le.

In general, there may exist more than one compatible set of reference pro<sup>fi</sup>les. In this perspective, in MCDA, one employs two different approaches for deriving a recommendation. One of them concerns selection of a single preference model instance that matches preferences and requirements of the DM in the “best” way (for a discussion, see, e.g., [16,28,31]). We take advantage of this approach in Step 4. The other approach, which is further employed in Step 5, takes into account all compatible preference model instances and investigates robustness of the delivered recommendation (see, e.g., [12–14,25]).

![](/api/attachments/SJFEAKGW/fulltext/images/4a44eeee9dcb609e6ead5d3801cf11cc8829e0e2017a3bc38d13324aea11393b.jpg)  
Fig. 2. Desired result of the joint ranking/sorting procedure for the case of three quality classes.

Step 4. Step 4 consists of building a recommendation with respect to a single representative set of reference pro<sup>fi</sup>les. We propose some pre-de<sup>fi</sup>ned rules for its selection. In particular, the DM may wish the pro<sup>fi</sup>les to be either as good or as bad as possible (see Section 5.1 for details). Then the selection procedure consists in solving a single MILP problem, which leads to indicating:

• the performances of reference pro<sup>fi</sup>les which can be interpreted as requirements that a research unit should satisfy to be assigned to a particular class;

• the assignments of all units which determine their funding level for the next evaluation period;

• the scores of all units re<sup>fl</sup>ecting their desirability and effectiveness against the remaining units; these scores along with the ranks can be used to distinguish over- and underperforming units within each class.

Step 5. The analysis of a single representative set of reference pro<sup>fi</sup>les is surely less abstract than that of the whole set of compatible sets of reference pro<sup>fi</sup>les. In such a way, the DM can see a score of each unit along with the univocal recommendation. Nevertheless, the selection algorithm from Step 4 introduces some degree of arbitrariness, which may affect the results. To verify how fragile they are, in Step 5, we may conduct robustness analysis taking into account the recommendation obtained for all compatible sets of reference pro<sup>fi</sup>les. We suggest to focus on the possible and necessary assignments, which are con<sup>fi</sup>rmed by, respectively, at least one and all compatible sets (see Section 5.2 for details). On the one hand, the necessary assignment is robust, which means that the recommendation is the same whatever compatible set of reference pro<sup>fi</sup>les. On the other hand, the possible assignment, in case of being imprecise, reveals that the recommendation may vary if some other procedure for selection of a representative set of reference pro<sup>fi</sup>les was chosen.

## 4. Disaggregation model for inferring compatible reference pro<sup>fi</sup>les

In this section, we present a mathematical program for inferring reference pro<sup>fi</sup>les separating the classes. This model is constructed in Step 3 of the decision aiding process presented in Section 3.

## 4.1. Performances of reference profiles

First, we de<sup>fi</sup>ne a set of constraints concerning performances of reference pro<sup>fi</sup>les $g _ { j } ( r ) , j \in J $ . We distinguish two cases depending on whether the DM provides for criterion g a preference threshold p only, or both indifference q<sub>j</sub> and preference $p _ { j }$ thresholds.

π a; b for $( a , b ) \in A \times A , j \in J ,$ is known and computed with 2 ; <sup>ð Þ ð Þ </sup>for r ∈ R; a ∈ B and j ∈ J :

$$
\left. \begin{array}{l} [ C _ {1} ] v _ {r, a} ^ {j} \leqslant 1 / M \cdot \Big (g _ {j} (r) - g _ {j} (a) - p _ {j} \Big) + 1, \\ [ C _ {2} ] v _ {r, a} ^ {j} \geqslant 1 / M \cdot \Big (g _ {j} (r) - g _ {j} (a) - p _ {j} + \varepsilon \Big), \\ [ C _ {3} ] \pi_ {j} (r, a) \leqslant v _ {r, a} ^ {j}, \\ [ C _ {4} ] \pi_ {j} (r, a) \geqslant v _ {r, a} ^ {j} + w _ {j} - 1, \\ [ C _ {5} ] \pi_ {j} (r, a) \geqslant 0, \\ [ C _ {6} ] \pi_ {j} (r, a) \leqslant w _ {j}, \\ [ C _ {7} ] v _ {r, a} ^ {j} \in \{0, 1 \}, \end{array} \right\} E (r, a)
$$

$$
[ P R _ {1} ] g _ {j} (r _ {h}) \geqslant g _ {j} (r _ {h - 1}) + \varepsilon , h = 2, \dots , p - 1,
$$

$$
x _ {j} ^ {n _ {j} (A)} \geqslant g _ {j} ^ {\max} (r _ {h}) \geqslant g _ {j} (r _ {h}) \geqslant g _ {j} ^ {\min} (r _ {h}) \geqslant x _ {j} ^ {1}, h = 1, \dots , p - 1,
$$

$$
x _ {j} ^ {n _ {j} (A)} - x _ {j} ^ {1}
$$

Let us <sup>fi</sup>rst consider the case of a given preference threshold $p _ { j }$ only (see constraint set $E _ { \mathrm { p r o f i l e s } } ^ { \mathrm { p r e f } } ) .$ . Since performances $g _ { j } ( r ) , j \in J ,$ are unknown, we need to relate the difference $g _ { j } ( r ) - g _ { j } ( a )$ , for r being a reference pro<sup>fi</sup>le in R and a being either an alternative in A or another reference pro<sup>fi</sup>le, with marginal preference index $\pi _ { j } ( r , a )$ . This relation is represented by constraint set $E ( r , a )$ in the following way. With each pair $( r , a ) \in R \times B$ and criterion $g _ { j } \in G ,$ , we associate a binary variable $\nu _ { r , a \cdot } ^ { j }$ It is equal to 0, if r is not preferred to a on $g _ { j } ,$ i.e., $g _ { j } ( r ) < g _ { j } ( a ) + p _ { j }$ (see constraint $\big [ C _ { 1 } \big ] \big )$ . In case r is preferred to a on $g _ { j } , \mathrm { i } . e . , g _ { j } ( r ) \geq g _ { j } ( a ) + p _ { j } ,$ , it is equal to 1 (see constraint [C ]). Now, if $\begin{array} { r } { v _ { r , a } ^ { j } = 1 } \end{array}$ , then marginal preference index $\pi _ { j } ( r , a )$ is equal to $w _ { j }$ (see constraints $[ C _ { 4 } ]$ and $\big [ C _ { 6 } \big ] )$ , while if $\begin{array} { r } { v _ { r , a } ^ { j } = 0 , } \end{array}$ , then $\pi _ { j } ( r , a )$ is equal to 0 (see constraints [C ] and $\left[ C _ { 5 } \right] )$ ). This is represented graphically in Fig. 3. Additionally, we require performances of an upper pro<sup>fi</sup>le of each class to be better than the performances of the corresponding lower pro<sup>fi</sup>le on each criterion (see $\left[ P R _ { 1 } \right] )$ . Finally, in case the DM speci<sup>fi</sup>ed some real interval $[ g _ { j } ^ { \operatorname* { m i n } } ( r _ { h } ) , g _ { j } ^ { \operatorname* { m a x } } ( r _ { h } ) ]$ allowed for the performance $g _ { j } ( r _ { h } ) _ { \ l }$ , this is respected with [PR ].

In case the DM provided both indifference $q _ { j }$ and preference threshold $p _ { j } ,$ with each pair $( r , a ) \in R \times B$ and criterion $g _ { j } \in G ,$ we associate three binary variables: v<sup>p,</sup> <sup>j</sup>, v<sup>i,</sup> <sup>j</sup> , and $v _ { r , a } ^ { w , j }$ (see constraint set $E ^ { \prime } ( r , a ) ,$ ). They correspond to zones of strict preference, indifference, and weak preference between r and a, respectively. Only one of these variables may be instantiated with one, while the remaining ones are set to zero. This is guaranteed by constraint [CV ]. Which binary variable is set to one is determined by a comparison of $g _ { j } ( r ) - g _ { j } ( a )$ with indifference q and preference p thresholds. For example, $\begin{array} { r } { \mathrm { i f } g _ { j } ( r ) - g _ { j } ( a ) \geqslant p _ { j } , } \end{array}$ then $\begin{array} { r } { \check { \nu { p , j } } = 1 , \nu _ { r , a } ^ { i , j } = 0 } \end{array}$ , and $\nu _ { r , a } ^ { w , j } = 0 \left( \mathsf { s e e } \left[ C P _ { 1 } \right] \right.$ and $[ C V _ { 1 } ] ) .$ . This, in turn, implies that $\pi _ { j } ( r , a ) = w _ { j }$ (see [CP ] and [CP ]). Since ${ \nu _ { r , a } ^ { i , j } } = 0$ and $v _ { r , a } ^ { w , j } = 0 ,$ , constraints $\left[ C I _ { 1 } - C I _ { 3 } \right]$ and $[ C W _ { 1 } - C W _ { 4 } ]$ are always satis<sup>fi</sup>ed, being eliminated. On the other hand, i $\dot { v } _ { r , a } ^ { i , j } = 1$ , then $\pi _ { j } ( r , a ) = 0$ , and $\mathrm { i f } \ v _ { r , a } ^ { w , j } = 1$ , then $\pi _ { j } ( r , a ) = w _ { j } \cdot [ ( g _ { j } ( r ) - g _ { j } ( a ) ) - q _ { j } ] / ( p _ { j } - q _ { j } )$ . This is represented graphically in Fig. 4.

![](/api/attachments/SJFEAKGW/fulltext/images/f91487face6d9abf98b07e1e3b54846d646fe5aaf22b1b141d0c11a8efccc3b9.jpg)  
Fig. 3. Marginal preference function in case the DM provides a preference threshold only.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\left.\begin{array}{l}\pi_{j}(a,b)\text{ for } (a,b)\in A\times A, j\in J,\text{ is known and computed with (1)},\\ \text{for } r\in R,a\in B\text{ and } j\in J:\\\ [CP_1]g_j(r)-g_j(a)\geqslant p_j-M\Big(1-v_{r,a}^{p,j}\Big),\\ [CP_2]\pi_j(r,a)\geqslant w_j-M\Big(1-v_{r,a}^{p,j}\Big),\\ [CP_3]\pi_j(r,a)\leqslant w_j+M\Big(1-v_{r,a}^{p,j}\Big),\\ [CI_1]g_j(r)-g_j(a)\leqslant q_j+M\Big(1-v_{r,a}^{i,j}\Big),\\ [CI_2]\pi_j(r,a)\geqslant 0-M\Big(1-v_{r,a}^{i,j}\Big),\\ [CI_3]\pi_j(r,a)\leqslant 0+M\Big(1-v_{r,a}^{i,j}\Big),\\ [CW_1]g_j(r)-g_j(a)\leqslant p_j+M\Big(1-v_{r,a}^{w,j}\Big),\\ [CW_2]g_j(r)-g_j(a)\geqslant q_j- M\Big(1-v_{r,a}^{w,j}\Big),\\ [CW_3]\pi_j(r,a)\geqslant w_j\cdot\Big[(g_j(r)-g_j(a))-q_j\Big]/\Big(p_j-q_j\Big)-M\Big(1-v_{r,a}^{w,j}\Big),\\ [CW_4]\pi_j(r,a)\leqslant w_j\cdot\Big[(g_j(r)-g_j(a))-q_j\Big]/\Big(p_j-q_j\Big)+M\Big(1-v_{r,a}^{w,j}\Big),\\ [CV_1]v_{r,a}^{p,j}+v_{r,a}^{i,j}+v_{r,a}^{w,j}=1,\\ [CV_2]v_{r,a}^{p,j},v_{r,a}^{i,j},v_{r,a}^{w,j}\in\{0,1\},\\\end{array}\right\}\text{E}^{\prime}(r,a)\text{E}^{\text{ind-pref profiles}}\\ \text{for } r\in R,a\in B\text{ and } j\in J:\\\ E^{\prime}(a,r) (\text{corresponding to } E(r,a) \text{ with inverse positions of } a \text{ and } r),\\ [PR_1],[PR_2].\end{array}\right\}$
</div>

## 4.2. Scoring procedures

Let us now discuss exemplary scoring procedures and the way of accounting for desired class cardinalities speci<sup>fi</sup>ed by the DM.

First, we refer to a scoring procedure, which compares alternatives pairwise and grants each alternative a score in the range [0, 1]. This score is equal to a comprehensive preference index $\pi ( { \boldsymbol { a } } , { \boldsymbol { b } } )$ . Then a comprehensive score of $a \in B$ is computed as $\begin{array} { r } { S c ( { a } ) = \sum _ { b \in B } \pi ( a , b ) ; } \end{array}$ see constraint set $E _ { s c o r e s } ^ { \mathrm { c o n t i n u o u s } }$ . This scoring procedure is represented graphically in Fig. 5a). To respect desired cardinalities for each class $C _ { h } ,$ we need to ensure that only a pre-de<sup>fi</sup>ned share of the whole set of research units $a \in A$ is at least as good as the reference pro<sup>fi</sup>le $r _ { h \mathrm { ~ - ~ } 1 }$ and worse than $r _ { h } .$ This is achieved with constraints $[ P _ { 3 } - P _ { 8 } ] .$ . Precisely, $\mathrm { i f } S c ( a ) \prec S c ( r _ { h - 1 } )$ and $S c ( a ) < S c ( r _ { h } )$ , then the binary variable $\nu _ { a , C _ { h } } ^ { \mathsf { C O M P } }$ is set to one. Thus, the sum of binary variables $\nu _ { a , C _ { h } } ^ { \mathsf { C O M P } }$ for all $a \in A$ corresponds to the number of existing research units, which are ranked at least as good as reference pro<sup>fi</sup>le $r _ { h \_ } \_ 1$ and worse than $r _ { h } .$ This sum needs to be not less than $\lceil N _ { h } ^ { \mathrm { p e r c \cdot m i n } }$ n⌉ and not greater than $\lceil N _ { h } ^ { \mathrm { p e r c \cdot m a x } }$ ⋅ n⌉ (or equal to $\lceil N _ { h } ^ { \mathrm { p e r c } }$ n⌉ if the DM provided precise desired class cardinality).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
for  $a, b \in B$ :
 $[P_{1}] \pi(a, b) = \sum_{j=1}^{m} \pi_{j}(a, b),$ 
for  $a \in B$ :
 $[P_{2}] Sc(a) = \sum_{b \in B} \pi(a, b),$ 
for  $a \in A$ :
 $[P_{3}] \sum_{h=1}^{p} v_{a, C_{h}}^{\text{COMP}} = 1,$ 
for  $a \in A, h = 1, \ldots, p$ :
if h &gt; 1:
 $[P_{4}] Sc(a) \geqslant Sc(r_{h-1}) - M\left(1 - v_{a, C_{h}}^{\text{COMP}}\right),$ 
if h &lt; p:
 $[P_{5}] Sc(a) + \varepsilon \leqslant Sc(r_{h}) + M\left(1 - v_{a, C_{h}}^{\text{COMP}}\right),$ $[P_{6}] v_{a, C_{h}}^{\text{COMP}} \in \{0, 1\},$ 
for  $h = 1, \ldots, p$ :
 $[P_{7}] \sum_{a \in A} v_{a, C_{h}}^{\text{COMP}} \geq [N_{h}^{\text{perc-min}} \cdot n],$ $[P_{8}] \sum_{a \in A} v_{a, C_{h}}^{\text{COMP}} \leq [N_{h}^{\text{perc-max}} \cdot n.]$
</div>

A different scoring procedure assumes that alternatives are compared pairwise and the alternative which proves better is granted a score of one (see constraint set $E _ { s c o r e s } ^ { \mathrm { b i n a r y } } )$ . For example, if the strength of arguments in favor of a when compared to b, which is materialized with $\pi ( { \boldsymbol { a } } , { \boldsymbol { b } } )$ , is greater than the strength of arguments in favor of b when compared to a $( \pi ( b , a ) )$ ), then binary variable $\nu _ { a , b }$ in constraint $[ W _ { 4 } ]$ is set to one. Otherwise, it is instantiated with zero. This scoring procedure is represented graphically in Fig. 5b). Alternatively, a may be granted a score only if arguments supporting its strength are suf<sup>fi</sup>ciently great (e.g., if π(a, b) is not less than some cutting level $\lambda > 0 . 5$ pre-de<sup>fi</sup>ned by the DM; see $\left[ W _ { 1 } ^ { \prime } \right] )$ . In any case, a comprehensive score $S c ( a )$ of each alternative or reference pro<sup>fi</sup>le $a \in B$ is computed by summing up scores resulting from pairwise comparisons with all remaining $\begin{array} { r } { b \in B , \mathrm { i . e . , } S c ( a ) = \sum _ { b \in B } \nu _ { a , b } . } \end{array}$ Then desired class cardinalities are accounted analogously as in E <sub>scores</sub><sup>continuous</sup>. The procedure with binary scores is interesting because when computing Sc(a), for $a \in B ,$ it eliminates the undesired compensation between a single large value $\pi ( { \boldsymbol { a } } , { \boldsymbol { b } } )$ and several small values π(c, a), for $b , c \in B .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
for  $(a,b)\in A\times A$ :
 $[W_{1}]$ $v_{a,b}=1$ , if  $\pi(a,b)&gt;\pi(b,a)$ $[W_{1}^{\prime}]$  (or  $\pi(a,b)\geq\lambda$ ),
 $[W_{2}]$ $v_{a,b}=0$ , if  $\pi(a,b)\leq\pi(b,a)$ $[W_{2}^{\prime}]$  (or  $\pi(a,b)&lt;\lambda$ ),
for  $(a,b)\in R\times A$  or  $A\times R$ :
 $[W_{3}]$ $\pi(a,b)=\sum_{j=1}^{m}\pi_{j}(a,b),$ $[W_{4}]$ $\pi(a,b)\geqslant\pi(b,a)+\varepsilon-M(1-v_{a,b}),$ $[W_{4}]$ $\pi(a,b)\leqslant\pi(b,a)+M\nu_{a,b},$ $[W_{4}^{\prime}]$  (or  $\pi(a,b)\geqslant\lambda-M(1-v_{a,b})$ ),
 $[W_{4}^{\prime}]$  (or  $\pi(a,b)+\varepsilon\leqslant\lambda+M\nu_{a,b}$ ),
for  $a\in B$ :
 $[W_{5}]$  Sc(a) =  $\sum_{b\in B}v_{a,b}$ ,
 $E_{card}^{class}.$
</div>

Let us denote by $\mathcal { R } ^ { D M }$ the set of preference model instances (in <sup>R</sup>particular, reference pro<sup>fi</sup>les) compatible with the DM's preference information. It is de<sup>fi</sup>ned by a set of constraint $E _ { \mathrm { D M } } = E _ { \mathrm { p r o f i l e s } } \cup E _ { \mathrm { s c o r e s } } ,$ where $E _ { \mathrm { p r o f i l e s } }$ is equivalent to $E _ { \mathrm { p r o f i l e s } } ^ { \mathrm { i n d \_ p r e f } }$ whether the DM provided indifference thresholds or not and $E _ { s c o r e s }$ is equivalent to E<sub>scores</sub><sup>binary</sup> or $E _ { s c o r e s } ^ { \mathrm { c o n t i n u o u s } }$ depending on the selected scoring procedure.

The following variables are involved in formulation of $E _ { \mathrm { D M } } \mathrm { : }$

$g _ { j } ( r _ { h } ) \mathrm { f o r } h = 1 , . . . , p - 1$ , involved in $E _ { \mathrm { p r o f i l e s } }$ <sub>s</sub> (these variables represent the performances of the reference pro<sup>fi</sup>les),

$\pi _ { j } ( r , a )$ and $\pi _ { j } ( a , r )$ for $r \in R , a \in B ,$ , and $j \in J ,$ involved in $E _ { \mathrm { p r o f i l e s } }$ (these variables represent marginal preference indices for pairs consisting of a pro<sup>fi</sup>le and a unit),

$\boldsymbol { \nu } _ { r , a } ^ { j }$ and $\nu _ { a , r } ^ { j }$ used in case $E _ { \mathrm { p r o f l e s } } = E _ { \mathrm { p r o f l e s } } ^ { \mathrm { p r e f } } , 0 \Gamma \nu _ { r , a } ^ { p , j } , \nu _ { r , a } ^ { i , j } , \nu _ { r , a } ^ { w , j } , \nu _ { a , r } ^ { p , j } , \nu _ { a , r } ^ { i , j }$ , and $v _ { a , r } ^ { w , j }$ used in case $E _ { \mathrm { p r o f i l e s } } \doteq E _ { \mathrm { p r o f i l e s } } ^ { \mathrm { i n d \_ p r e f } }$ for $r \in R , a \in B ,$ and $j \in J$ (these binary variables represent either preference or its lack, or preference, weak preference, and indifference on a given criterion for pairs consisting of a pro<sup>fi</sup>le and a unit);

$\pi ( \boldsymbol { a } , \boldsymbol { r } )$ and $\pi ( r , a )$ for $r \in R$ and $a \in B ,$ involved in $E _ { s c o r e s }$ (these variables represent comprehensive preference indices for pairs consisting of a pro<sup>fi</sup>le and a unit; note that $\pi ( { \boldsymbol { a } } , { \boldsymbol { b } } )$ for $a , b \in A ,$ , are constants);

$S c ( a )$ for $a \in B ,$ involved in $E _ { s c o r e s }$ (these variables represent comprehensive scores attained by the units);

$\nu _ { a , C _ { h } } ^ { \mathrm { C O M P } }$ for $a \in A$ and $h \in H ,$ , involved in $E _ { \mathrm { s c o r e s } }$ (these binary variables represent assignment of a unit $a \in A$ to class $C _ { h } ) ;$ ;

• $\nu _ { a , r }$ and $\nu _ { r , a }$ for $a \in A$ and $r \in R ,$ , involved in E<sub>scores</sub><sup>binary</sup> (these binary variables represent superiority of a unit over a pro<sup>fi</sup>le, or vice versa; note that $\nu _ { a , b }$ for $a , b \in A$ , are constants).

![](/api/attachments/SJFEAKGW/fulltext/images/239c000525347f853a564a99b09ff60f96c69a38c0eb8e91f6ae2abc31943ba5.jpg)  
Fig. 4. Marginal preference function in case the DM provides indifference and preference thresholds.

## 5. Multiple criteria ranking and sorting with inferred reference pro<sup>fi</sup>les

In this section, we discuss procedures for both selection of a single set of representative reference pro<sup>fi</sup>les as well as robustness analysis. They are employed in Steps 4 and 5 of the decision aiding process presented in Section 3.

## 5.1. Selection of a representative set of reference profiles

When selecting a single set of representative reference pro<sup>fi</sup>les, one may consider different requirements. In particular, one may select the pro<sup>fi</sup>les which are either as good or as bad as possible. Such pro<sup>fi</sup>les can be interpreted as performance vectors that a research unit should attain to be assigned to a particular class. For interpretability of the results, it is also reasonable to require the performances of the pro<sup>fi</sup>les to be balanced with respect to the extreme performances of alternatives on different criteria. In this way, we avoid selection of the pro<sup>fi</sup>les, which are relatively good on some criteria, while being relatively bad on the others. This is achieved by solving problem (3).

p−1 p−1 m Maximize or Minimize : δ<sub>h</sub> γ<sup>X</sup> δ<sub>h j</sub> h 1 h 1 j 1

3

![](/api/attachments/SJFEAKGW/fulltext/images/89c5a8de6ad5d82e4e7ab6a61b579e473b19def536a19128bb8c14136d1fb977.jpg)

$$
\left. \begin{array}{l} E _ {\mathrm{DM}}, \\ \text {for} h = 1, \dots , p - 1, j \in J: \\ \delta_ {h j} \leq \left(g _ {j} (r _ {h}) - x _ {j} ^ {1}\right) / \left(x _ {j} ^ {n _ {j} (A)} - x _ {j} ^ {1}\right), \\ \left(\text {or} \delta_ {h j} \geq \left(g _ {j} (r _ {h}) - x _ {j} ^ {1}\right) / \left(x _ {j} ^ {n _ {j} (A)} - x _ {j} ^ {1}\right)\right), \\ \delta_ {h} \leq \delta_ {h j}, \\ \left(\text {or} \delta_ {h} \geq \delta_ {h j}\right), \end{array} \right\} E _ {\text {inference}}
$$

where $\gamma$ is an arbitrarily small positive value, e.g., 0.001.

Now, let us explain the objective function in case the selected pro<sup>fi</sup>les are required to be as good as possible (an explanation for the case of pro-<sup>fi</sup>les required to be as bad as possible can be formulated analogously). A coef<sup>fi</sup>cient $\left( g _ { j } ( r _ { h } ) - x _ { j } ^ { 1 } \right) \Big / \left( x _ { j } ^ { n _ { j } ( A ) } - x _ { j } ^ { 1 } \right)$ fo $j \in J$ and $h \in \{ 1 , . . . , p - 1 \}$ which is used in the above constraint set, represents the location of $g _ { j } ( r _ { h } )$ on a scale delimited by the extreme performances of existing research units: $x _ { j } ^ { n _ { j } ( A ) }$ and $x _ { j } ^ { 1 } .$ For example, if it is equal to 0.75, the distance of $g _ { j } ( r _ { h } )$ from $\boldsymbol { x } _ { j } ^ { 1 }$ is three times greater than its distance from $x _ { i } ^ { n _ { j } ( A ) }$ Apart from the variables included in $E _ { \mathrm { D M } }$ (these are listed in Section 4.2), the constraint set $E _ { \mathrm { i n f e r e n c e } }$ involves the following variables:

$\delta _ { h j } \mathrm { f o r } h = 1 , . . . , p - 1 \mathrm { a n d } j \in J ,$ , which bound the aforementioned coef<sup>fi</sup>cients from below; consequently, the greater $\cdot \delta _ { h j } ,$ the bette $r _ { h }$ on g<sub>j</sub>;

$\delta _ { h } \operatorname { f o r } h \in \{ 1 , . . . , p - 1 \}$ , which bound the values of respective variables $\delta _ { h j } \mathrm { f o r } j \in J ,$ from below; thus, the greater $\delta _ { h } ,$ , the better the worst performance of $r _ { h }$ on any criterion $g _ { j } .$

b) binary scores

![](/api/attachments/SJFEAKGW/fulltext/images/e3ebe4efad43069a8ada2b905421365233f08f6c5d3ab45f967e8cd1bc128de3.jpg)  
Fig. 5. Scoring procedure with (a) continuous scores and (b) binary scores

To select the pro<sup>fi</sup>les that are as good as possible with relatively balanced performances on different criteria, we maximize $\begin{array} { r } { \sum _ { h } ^ { p \mathrm { ~ - ~ } 1 } \delta _ { h } , } \end{array}$ thus requiring the worst performance of each pro<sup>fi</sup>le to be as good as possible. As a secondary target, we optimize $\begin{array} { r } { \sum _ { h } ^ { p } \stackrel { - } { = } 1 \sum _ { j } ^ { m } = 1 \delta _ { h j } , } \end{array}$ thus maximizing the pro<sup>fi</sup>les' performances on the individual criteria.

## 5.2. Robustness analysis

Robustness analysis is understood as a theoretical basis and a diversity of particular multiple criteria decision support methods that take into account internal and external uncertainties observed in the actual decision situations. In this paper, we are interested in investigating the robustness of the provided recommendation, i.e., whether it is valid for all or for the most plausible sets of model parameters. We focus on the assignmentrelated results. In this case, it is reasonable to consider the possible and necessary assignments. Precisely, given a set $\mathcal { R } ^ { \mathrm { D M } }$ of compatible preference model instances, for each alternative $a \in A ,$ the possible assign ment $C _ { P } ( a )$ is de<sup>fi</sup>ned as the set of indices of classes $C _ { h }$ for which there exists at least one compatible preference model instance assigning a to $C _ { h }$ , and the necessary assignment $C _ { N } ( a )$ as the set of indices of classes $C _ { h }$ for which all compatible preference models assign a to $C _ { h }$ (see [26, 32]).

Computing the possible assignment for $a \in A$ requires considering problem (4) for each $h \in H .$ It veri<sup>fi</sup>es whether score $S c ( a )$ of $a \in A$ can be simultaneously at least as good as score of the lower pro<sup>fi</sup>le $r _ { h \mathrm { ~ - ~ } 1 }$ and less than score of the upper pro<sup>fi</sup>le $r _ { h }$ of class $C _ { h } ,$ in the set of compatible preference model instances (de<sup>fi</sup>ned with the constraint set $E _ { \mathrm { D M } } )$ . We assume here that $\varepsilon ,$ which is used in both $E _ { D M }$ and newly added constraints, is a variable rather than a constant (as stated previously in Section 4.1); it is used to transform strict inequalities into non-strict ones.

Maximize : ε

$$
\left. \begin{array}{l} E _ {\mathrm{DM}}, \\ S c (a) \geqslant S c (r _ {h - 1}), \text { if } h > 1, \\ S c (a) + \varepsilon \leqslant S c (r _ {h}), \text { if } h <   p. \end{array} \right\} E ^ {P} (a, h)\tag{4}
$$

$\mathrm { I f } \varepsilon ^ { * } = \operatorname* { m a x } \varepsilon , \ s . \mathrm { t } . E ^ { P } ( a , h )$ , is greater than $0 ,$ and $E ^ { P } ( a , h )$ is feasible, then a is possibly assigned to $C _ { h } .$ Note that if the possible assignment $C _ { P } ( a )$ is univocal, then it is equivalent to the necessary assignment $C _ { N } ( a )$ . On the contrary, if the possible assignment is non-univocal, the necessary assignment is empty $( C _ { N } ( a ) = \mathcal { O } )$ . This holds for all sorting procedures where assignments are derived from the comparison of comprehensive scores with the thresholds between consecutive classes (see [34]). Note that when investigating robustness of the delivered recommendation, we may additionally account for the truth of the necessary and possible assignment-based preference relations as well as the observed extreme class cardinalities as proposed in [29].

## 6. Case study

Let us consider exemplary data concerning twenty Polish research units to be assigned to one of the three classes $C _ { 1 } { - } C _ { 3 }$ (with $C _ { 1 }$ being the worst, and $C _ { 3 }$ the best one). The units are evaluated on the following four criteria:

• scienti<sup>fi</sup>c activity $\left( g _ { 1 } \right)$ , including scienti<sup>fi</sup>c publications in journals included in the Journal Citation Reports (JCR), Polish ministerial lists, or European Reference Index for the Humanities as well as monographs, chapters, and number of patents; the evaluation re<sup>fl</sup>ects an average number of points gained for publications by a single researcher of the unit;

• scienti<sup>fi</sup>c potential $\left( g _ { 2 } \right)$ , including the ability to grant PhD and habilitation degrees, number of PhDs, habilitations, and professor titles granted in the evaluation period as well as prestigious memberships (e.g., being an editor of a JCR journal, member of an editorial board of such a journal, or coordinator of an international working group or institution); all achievements are scored and these scores are summed up to get an evaluation;

• material effects of unit's activities (g )—representing money acquired from grants or cooperation with industry (not included in the statutory grant from the Ministry);

• remaining (non-material) effects of unit's activities $\left( g _ { 4 } \right)$ —subjective evaluation of ten most important achievements of unit's members conducted by experts of the evaluation team.

The performances of 20 considered research units are given in Table 1. As recently noted in [22], a problem representation has a signi<sup>fi</sup>cant impact on decision processes. However, in case of outranking-based methods, we suggest using a table representation (such as Table 1) or parallel coordinate plots instead of heat maps. It is the case since speci<sup>fi</sup>cation of comparison thresholds is easier when analyzing the original performances of alternatives instead of their mapping into colors representing different performance intervals or levels.

We assume the DM to have provided weight $w _ { j }$ and preference threshold $p _ { j }$ for each criterion $g _ { j }$ (see Table 2). According to the DM's preferences, the scienti<sup>fi</sup>c activity of a research unit $\left( g _ { 1 } \right)$ is the most important criterion. The desired distribution of class cardinalities is as follows: 25 % and 40 % of research units should be assigned, resepectively, to $C _ { 3 }$ or $C _ { 2 } ,$ and the remaining 35 % should go to C .

First, let us focus on the procedure with continuous scores. Solving problem (3), we inferred representative reference pro<sup>fi</sup>les which are as good as possible (see Table 3). To respect the desired class cardinalities, the pro<sup>fi</sup>les are such that there are 5 research units at least as good as PR2, which separates classes $C _ { 2 }$ and $C _ { 3 } ,$ and 13 units not worse than pro<sup>fi</sup>le PR1 separating $C _ { 1 }$ and $C _ { 2 } .$ The scores, class assignments, and ranks of the units and pro<sup>fi</sup>les are provided in Table 1 (continuous scores). Units with ranks 1–5 (RU5, RU19. RU9,

Performance matrix for 20 research units. Scores, class assignment, and ranks of research units and discovered pro<sup>fi</sup>les according to two different scoring procedures

<table><tr><td rowspan="2"></td><td rowspan="2"> $g_1$ </td><td rowspan="2"> $g_2$ </td><td rowspan="2"> $g_3$ </td><td rowspan="2"> $g_4$ </td><td colspan="2">Continuous scores</td><td colspan="2">Binary scores</td></tr><tr><td>Sc(a)</td><td>Class (rank)</td><td>Sc(a)</td><td>Class (rank)</td></tr><tr><td>RU1</td><td>90</td><td>86</td><td>46</td><td>30</td><td>15.05</td><td> $C_3(5)$ </td><td>18</td><td> $C_3(4)$ </td></tr><tr><td>RU2</td><td>40</td><td>90</td><td>14</td><td>48</td><td>9.65</td><td> $C_2(12)$ </td><td>6</td><td> $C_1(16)$ </td></tr><tr><td>RU3</td><td>88</td><td>40</td><td>50</td><td>12</td><td>9.70</td><td> $C_2(11)$ </td><td>15</td><td> $C_2(7)$ </td></tr><tr><td>RU4</td><td>82</td><td>94</td><td>26</td><td>48</td><td>15.40</td><td> $C_3(4)$ </td><td>16</td><td> $C_3(5)$ </td></tr><tr><td>RU5</td><td>94</td><td>100</td><td>40</td><td>36</td><td>17.60</td><td> $C_3(1)$ </td><td>19</td><td> $C_3(3)$ </td></tr><tr><td>RU6</td><td>78</td><td>76</td><td>30</td><td>50</td><td>13.05</td><td> $C_2(7)$ </td><td>14</td><td> $C_2(8)$ </td></tr><tr><td>RU7</td><td>74</td><td>70</td><td>50</td><td>20</td><td>10.40</td><td> $C_2(10)$ </td><td>11</td><td> $C_2(11)$ </td></tr><tr><td>RU8</td><td>80</td><td>64</td><td>32</td><td>38</td><td>10.85</td><td> $C_2(9)$ </td><td>12</td><td> $C_2(10)$ </td></tr><tr><td>RU9</td><td>100</td><td>74</td><td>48</td><td>40</td><td>16.20</td><td> $C_3(3)$ </td><td>20</td><td> $C_3(2)$ </td></tr><tr><td>RU10</td><td>60</td><td>60</td><td>30</td><td>30</td><td>6.25</td><td> $C_1(17)$ </td><td>7</td><td> $C_2(13)$ </td></tr><tr><td>RU11</td><td>64</td><td>72</td><td>12</td><td>46</td><td>8.80</td><td> $C_2(14)$ </td><td>7</td><td> $C_2(13)$ </td></tr><tr><td>RU12</td><td>78</td><td>76</td><td>36</td><td>12</td><td>9.45</td><td> $C_2(13)$ </td><td>13</td><td> $C_2(9)$ </td></tr><tr><td>RU13</td><td>50</td><td>80</td><td>20</td><td>18</td><td>6.65</td><td> $C_1(16)$ </td><td>6</td><td> $C_3(16)$ </td></tr><tr><td>RU14</td><td>62</td><td>88</td><td>22</td><td>48</td><td>10.95</td><td> $C_2(8)$ </td><td>10</td><td> $C_2(12)$ </td></tr><tr><td>RU15</td><td>30</td><td>44</td><td>30</td><td>18</td><td>2.50</td><td> $C_1(21)$ </td><td>3</td><td> $C_1(19)$ </td></tr><tr><td>RU16</td><td>40</td><td>54</td><td>40</td><td>32</td><td>5.75</td><td> $C_1(18)$ </td><td>4</td><td> $C_1(18)$ </td></tr><tr><td>RU17</td><td>70</td><td>30</td><td>12</td><td>12</td><td>4.30</td><td> $C_1(19)$ </td><td>1</td><td> $C_1(20)$ </td></tr><tr><td>RU18</td><td>32</td><td>18</td><td>28</td><td>22</td><td>2.45</td><td> $C_1(22)$ </td><td>1</td><td> $C_1(20)$ </td></tr><tr><td>RU19</td><td>100</td><td>80</td><td>40</td><td>42</td><td>16.90</td><td> $C_3(2)$ </td><td>21</td><td> $C_3(1)$ </td></tr><tr><td>RU20</td><td>24</td><td>58</td><td>30</td><td>18</td><td>2.55</td><td> $C_1(20)$ </td><td>1</td><td> $C_1(20)$ </td></tr><tr><td>PR1</td><td></td><td></td><td></td><td></td><td>8.45</td><td>(15)</td><td>7</td><td>(15)</td></tr><tr><td>PR2</td><td></td><td></td><td></td><td></td><td>14.95</td><td>(6)</td><td>16</td><td>(6)</td></tr></table>

Table 2  
Preference thresholds and weights provided by the decision maker.

<table><tr><td></td><td> $g_1$ </td><td> $g_2$ </td><td> $g_3$ </td><td> $g_4$ </td></tr><tr><td> $p_j$ </td><td>4</td><td>4</td><td>2</td><td>2</td></tr><tr><td> $w_j$ </td><td>0.45</td><td>0.25</td><td>0.1</td><td>0.2</td></tr></table>

RU4, and RU1) are assigned to $C _ { 3 } ;$ their scores are not less than $S c ( \mathrm { P R } 2 ) = 1 4 . 9 5$ . Further, units with ranks 7–14 are assigned to C<sub>2</sub>; their scores are at least as good as $S c ( \mathrm { P R } { 1 } ) = 8 . 4 5$ but less than Sc(PR2). Note that units assigned to the same class remain comparable. For example, RU5 proves to be the best with a score of 17.60, while the last unit in $C _ { 3 } ,$ RU1, has the score of 15.05. In the same spirit, the range of scores in $C _ { 2 }$ is between 13.05 (RU6) and 8.80 (RU11).

Pro<sup>fi</sup>les PR2 and PR1 can be interpreted as balanced performance vectors representing minimal requirements that a research unit should satisfy to be assigned to class $C _ { 3 }$ or $C _ { 2 } ,$ respectively. To support this claim, we present the inferred pro<sup>fi</sup>les in Fig. 6, along with the performances of all research units.

To verify robustness of the delivered recommendation, we need to consider problem (4) for each pair of an existing research unit $a \in A$ and a class $C _ { h } , h = 1 , 2 , 3$ . The analysis performed on this data set reveals that in case all different reference pro<sup>fi</sup>les respecting desired class cardinalities are used, the assignments presented in Table 1 can be considered as robust. Thus, for each unit, the assignments obtained with the representative preference pro<sup>fi</sup>les are equal to both the necessary and possible ones. This means that although the ranks and scores attained by the research units may vary, their class assignments remain the same, not being in<sup>fl</sup>uenced by the procedure for selection of the reference pro<sup>fi</sup>les.

Let us also consider a scoring procedure with binary scores. Each alternative a (research unit or reference pro<sup>fi</sup>le) is granted a score of one if it proves better in the pairwise comparison against another alternative b, i.e., $\pi ( a , b ) > \pi ( b , a )$ . The reference pro<sup>fi</sup>les inferred in this case are provided in Table 3 (binary scores). Compared to the previous ones, performances of PR2 are slightly better, and performances of PR1 slightly worse. Again, scores, class assignments, and ranks attained by the alternatives are given in Table 1 (binary scores). Obviously, all scores are integer values. Five research units with the score not less than $S c ( \mathrm { P R } 2 ) = 1 6 $ are assigned to $C _ { 3 } ;$ another eight units with the score at least as good as $S c ( \mathrm { P R 1 } ) = 7$ , but worse than 16 are placed in $C _ { 2 } .$

## 7. Conclusions

In this paper, we introduced a novel approach to joint sorting and ranking of research units. These units are evaluated on multiple criteria representing the level of effects they acquired and activities they undertook in the evaluation period. For interpretability of the results, we constructed reference pro<sup>fi</sup>les separating the classes. To leave units assigned to the same class comparable, they are <sup>fi</sup>rst ranked and then assigned to the respective class based on the attained score. Ranking procedure is based on non-compensatory pairwise comparisons including both existing research units and reference pro<sup>fi</sup>les to be discovered. To account for desired class cardinalities and taking into account the role played by the reference pro<sup>fi</sup>les, we imposed constraints on the ranks they need to attain. We discussed different inference procedures conditioned by the preference information of the DM, as well as a set of procedures with both continuous and binary scores gained by the alternatives. We also proposed some rules for selecting precise and representative performances of the reference pro<sup>fi</sup>les, and we have shown how to conduct robustness analysis of the delivered recommendation. We demonstrated practical use of the approach by considering a case study of sorting/ranking 20 Polish research units with respect to 4 criteria.

Inferred representative reference pro<sup>fi</sup>les.

<table><tr><td colspan="5">Continuous scores</td></tr><tr><td></td><td> $g_1$ </td><td> $g_2$ </td><td> $g_3$ </td><td> $g_4$ </td></tr><tr><td>PR1</td><td>68.00</td><td>65.47</td><td>34.00</td><td>34.00</td></tr><tr><td>PR2</td><td>85.16</td><td>84.00</td><td>42.58</td><td>42.58</td></tr><tr><td colspan="5">Binary scores</td></tr><tr><td></td><td> $g_1$ </td><td> $g_2$ </td><td> $g_3$ </td><td> $g_4$ </td></tr><tr><td>PR1</td><td>64.00</td><td>61.20</td><td>32.00</td><td>32.00</td></tr><tr><td>PR2</td><td>86.00</td><td>84.90</td><td>43.00</td><td>43.00</td></tr></table>

Let us mention that the current procedure used by the Polish Ministry for parametric evaluation of research units is also based on non-compensatory pairwise comparisons of research units including reference pro<sup>fi</sup>les. It is also using the procedure with continuous scores. However, the reference pro<sup>fi</sup>les are de<sup>fi</sup>ned prior to calculation, as multiples of median values of performance distributions of considered units on particular criteria, and the desirable class cardinalities are not speci<sup>fi</sup>ed.

Obviously, in this paper, we have not exhausted all possible ways of constructing and exploiting the outranking relation. While maintaining the main idea of joint multiple criteria ranking and sorting with reference pro<sup>fi</sup>les, it may be appealing, e.g., to account for the veto phenomenon in the construction phase or to use a different net <sup>fl</sup>ow score procedure in the exploitation phase.

Finally, let us remark that the ranking and sorting result can be interpreted a posteriori in terms of decision rules involving elementary conditions on a subset of criteria in the premise and specifying a binary relation or unit assignment in the conclusion (see [27,44]). Such explanations are important for justifying that the <sup>fi</sup>nal recommendation is logical, valid, and correct because they prove to be useful in making explicit the experts logic and assumptions [30].

The proposed inference and scoring procedures are based on the use of MILP. In particular, constraint set $E _ { \mathrm { p r o f i l e s } } ^ { \mathrm { p r e f } }$ involves $2 ( p - 1 ) m ( n + 2 )$ binary variables $( 2 ( p \mathrm { ~ - ~ } 1 ) m ( n + \dot { 2 } ) = 2 \times ( p \mathrm { ~ - ~ } 1 )$ pro<sup>fi</sup>les × m criteria × (n + 2) alternatives), while E<sub>pro</sub>fi<sub>les</sub><sup>ind</sup> <sup>‐</sup> <sup>pref</sup> three times as many of them. Further, E<sub>scores</sub><sup>continuous</sup> involves $p ( n + 2 )$ binary variables, whereas E<sub>scores</sub><sup>binary</sup> employs additiona $2 ( p - 1$ )n binary variables. Thus, for example, to infer reference pro<sup>fi</sup>les in our illustrative study, we solved MILPs with 418 and 498 binary variables for scoring procedures with continuous and binary scores, respectively. The execution time on Intel Atom CPU D325 1:80 GHz with 4GB RAM and GLPK solver was a few hours. Considering the typical size of groups of common evaluation of research units, the respective MILP problems are still manageable with the existing solvers. Nevertheless, as proved by the extensive experiments conducted by Cailloux et al. [7], nowadays problems with a few thousands of binary variables cannot be solved in a reasonable time of several hours. Taking this into account, the practical usefulness of the proposed approach is limited to sets consisting of several tens of alternatives.

## Acknowledgments

The <sup>fi</sup>rst author wishes to acknowledge <sup>fi</sup>nancial support from the Polish National Science Centre (grant SONATA, no. DEC-2013/11/D/ ST6/03056). The authors thank two anonymous referees for their remarks which helped us to signi<sup>fi</sup>cantly improve the paper.

![](/api/attachments/SJFEAKGW/fulltext/images/af1e3dab42cc33503e6ec444eeea651956b347011e7e06fac1c99d093c4aa532.jpg)  
Fig. 6. Research units' performances and inferred pro<sup>fi</sup>les for the procedure with continuous scores.

## References

[1] A. Albadvi, S.K. Chaharsooghi, A. Esfahanipour, Decision making in stock trading: An application of PROMETHEE, European Journal of Operational Research 177 (2) (2007) 673–683.

[2] J. Almeida Dias, Multiple criteria decision aiding for sorting problems: Concepts, methodologies, and applications(PhD Dissertation) Technical University of Lisbon, 2011.

[3] J. Almeida Dias, J. Figueira, B. Roy, Electre Tri-C: A multiple criteria sorting method based on characteristic reference actions, European Journal of Operational Research 204 (3) (2010) 565–580.

[4] D. Bouyssou, Ranking methods based on valued preference relations: A characterization of the net <sup>fl</sup>ow method, European Journal of Operational Research 60 (1) (1992) 61–67.

[5] J. Brans, B. Mareschal, The PROMCALC & GAIA decision support system for multicriteria decision aid, Decision Support Systems 12 (1994) 297–310.

[6] J. Brans, P. Vincke, B. Mareschal, How to select and how to rank projects: The PROMETHEE method, European Journal of Operational Research 24 (2) (1986) 228–238.

[7] O. Cailloux, P. Meyer, V. Mousseau, Eliciting ELECTRE TRI category limits for a group of decision makers, European Journal of Operational Research 223 (1) (2012) 133-140

[8] A. Certa, M. Enea, T. Lupo, ELECTRE III to dynamically support the decision maker about the periodic replacements con<sup>fi</sup>gurations for a multi-component system, Decision Support Systems 55 (1) (2013) 126–134

[9] S. Chakhar, I. Saad, Dominance-based rough set approach for groups in multicriteria classification problems Decision Support Systems 54 (2012) 372-380

[10] J.-K. Chen, I.-S. Chen, Inno-Qual ef<sup>fi</sup>ciency of higher education: Empirical testing using data envelopment analysis, Expert Systems with Applications 38 (3) (2011) 1823–1834.

[11] Y.-S. Chen, T.-C. Wang, C.-Y. Wu, Strategic decisions using the fuzzy PROMETHEE for IS outsourcing, Expert Systems with Applications 38 (10) (2011) 13216–13222.

[12] S. Corrente, S. Greco, M. Kadziński, R. Słowiński, Robust ordinal regression in preference learning and ranking, Machine Learning 93 (2–3) (2013) 381–422.

[13] S. Corrente, S. Greco, R. Słowiński, Multiple criteria hierarchy process in robust ordinal regression, Decision Support Systems 53 (3) (2012) 660–674.

[14] L. Dias, V. Mousseau, J. Figueira, J. Clmaco, An aggregation/disaggregation approach to obtain robust conclusions with ELECTRE TRI, European Journal of Operational Research 138 (2) (2002) 332–348.

[15] M. Doumpos, C. Zopounidis, A multicriteria decision support system for bank rating, Decision Support Systems 50 (1) (2010) 55–63.

Doumpos, C. Zopounidis, E. Galariotis, Inferring robust decision models in multicriteria classi<sup>fi</sup>cation problems: An experimental analysis, European Journal of Operational Research 236 (2) (2014) 601–611.

[17] S. Eppe, Y. De Smet, Approximating Promethee II's net <sup>fl</sup>ow scores by piecewise linear value functions, European Journal of Operational Research 223 (3) (2013) 651–665.

[18] S. Eppe, Y. De Smet, An adaptive questioning procedure for eliciting PROMETHEE II's weight parameters, International Journal of Multicriteria Decision Making 4 (1) (2014) 1–30.

[19] E. Fernandez, J. Navarro, A. Duarte, G. Ibarra, Core: A decision support system for regional competitiveness analysis based on multi-criteria sorting, Decision Support Systems 54 (3) (2013) 1417–1426.

[20] E. Fernandez, R. Olmedo, An agent model based on ideas of concordance and discordance for group ranking problems Decision Support Systems 39 (3) (2005) 429–443

[21] H. Gervasio, L.S. da Silva, A probabilistic decision-making approach for the sustainable assessment of infrastructures. Expert Systems with Applications 39 (8) (2011) 7121–7131.

[22] J. Gettinger, E. Kiesling, C. Stummer, R. Vetschera, A comparison of representations for discrete multi-criteria decision problems, Decision Support Systems 54 (2) (2013).976-985

[23] C. Giannoulis, A. Ishizaka, A web-based decision support system with ELECTRE III for a personalised ranking of British universities, Decision Support Systems 48 (3) (2010) 488–497.

[24] M. Goumas, V. Lygerou, An extension of the PROMETHEE method for decision making in fuzzy environment: Ranking of alternative energy exploitation projects, European Journal of Operational Research 123 (3) (2000) 606–613.

[25] S. Greco, M. Kadziński, V. Mousseau, R. Słowiński, Robust ordinal regression for multiple criteria group decision problems: UTAGMS-GROUP and UTADISGMS. GROUP, Decision Support Systems 52 (3) (2012) 549–561.

[26] S. Greco, V. Mousseau, R. Słowiński, Multiple criteria sorting with a set of additive value functions, European Journal of Operational Research 207 (4) (2010) 1455–1470.

[28] E. Jacquet-Lagrèze, Y. Siskos, Preference disaggregation: 20 years of MCDA experience, European Journal of Operational Research 130 (2) (2001) 233–245.

[29] M. Kadziński, K. Ciomek, R. Słowiński, Modeling assignment-based pairwise comparisons within integrated framework for value-driven multiple criteria sorting, European Journal of Operational Research 241 (3) (2015) 830–841.

[30] M. Kadziński, S. Corrente, S. Greco, R. Słowiński, Preferential reducts and constructs in robust multiple criteria ranking and sorting, OR Spectrum 36 (4) (2014) 1021–1053.

[31] M. Kadziński, S. Greco, R. Słowiński, Selection of a representative set of parameters for robust ordinal regression outranking methods, Computers & Operations Research 39 (11) (2012) 2500–2519.

[32] M. Kadziński, S. Greco, R. Słowiński, Robust ordinal regression for dominance-based rough set approach to multiple criteria sorting, Information Sciences 283 (2014) 211–228.

[33] M. Kadziński, R. Słowiński, DIS-CARD: A new method of multiple criteria sorting to classes with desired cardinality, Journal of Global Optimization 56 (3) (2013) 1143–1166.

[34] M. Kadziński, T. Tervonen, Stochastic ordinal regression for multiple criteria sorting problems, Decision Support Systems 55 (11) (2013) 55–66.

[35] M. Kadziński, T. Tervonen, J. Figueira, Robust multi-criteria sorting with the outranking preference model and characteristic pro<sup>fi</sup>les, Omega (2015), http://dx.doi.org/10.1016/j.omega.2014.06.004 (in press).

[36] G. Kou, Y. Shi, S. Wang, Multiple criteria decision making and decision support systems—guest editor's introduction, Decision Support Systems 51 (2) (2011) 247–249.

[37] M.-T. Lu, S.-W. Lin, G.-H. Tzeng, Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems 56 (2013) 259–269.

[38] T. Lupo, A fuzzy ServQua based method for reliable measurements of education quality in italian higher education area, Expert Systems with Applications 40 (17) (2013) 7096–7110.

[39] L. Markl-Hummel, J. Geldermann, A local-level, multiple criteria decision aid for climate protection FURO Journal on Decision Processes 2 (1–2) (2014) 121–152

[40] V. Mousseau, L. Dias, J. Figueira, On the notion of category size in multiple criteria sorting models, Cahier du LAMSADE 205, Université Paris-Dauphine, Paris, France, 2003.

[41] V. Mousseau, R. Słowiński, Inferring an ELECTRE TRI model from assignment examples, Journal of Global Optimization 12 (2) (1998) 157–174.

[42] A. Ngo The, V. Mousseau, Using assignment examples to infer category limits for the ELECTRE TRI method, Journal of Multi-Criteria Decision Analysis 11 (1) (2002) 29–43.

[43] A. Rolland Reference-based preferences aggregation procedures in multi-criteria decision making, European Journal of Operational Research 225 (3) (2013) 479-486.

[44] R. Słowiński, S. Greco, B. Matarazzo, Rough set and rule-based multicriteria decision aiding, Pesquisa Operacional 32 (2) (2012) 213–269.

[45] M. Szelag, S. Greco, R. Słowiński, Rule-based approach to multicriteria ranking, in: M. Doumpos, E. Grigoroudis (Eds.), Multicriteria decision aid and arti<sup>fi</sup>cial intelligence: Links, theory and applications, Wiley-Blackwell, London, 2013, pp. 127–160 (Chapter 6).

[46] G. van Valkenhoef, T. Tervonen, T. Zwinkels, B. de Brock, H. Hillege, ADDIS: A decision support system for evidence-based medicine, Decision Support Systems 55 (2) (2013) 459–475.

[47] B. Yilmaz, M. Dagdeviren, A combined approach for equipment selection: F-PROMETHEE method and zero–one goal programming, Expert Systems with Applications 38 (9) (2011) 11641–11650.

[48] W. Yu, ELECTRE TRI: Aspects méthodologiques et manuel d'utilisation, Document du LAMSADE no 74, Université Paris-Dauphine, 1992.

[49] J. Zheng, Preference elicitation for reference based aggregation models: Algorithms and procedures(PhD Thesis) Ecole Centrale Paris, 2012

[50] J. Zheng, O. Cailloux, V. Mousseau, Constrained multicriteria sorting method applied to portfolio selection, in: R.I. Brafman, F.S. Roberts, A. Tsoukiàs (Eds.), Algorithmic decision theory—Second International Conference, ADT 2011, Piscataway, NJ, USA, October 26-28, 2011. Proceedings, Lecture Notes in Computer Science, vol. 6992, Springer, 2011, pp. 331–343.

Miłosz Kadziński is an Assistant Professor at the Poznan University of Technology, member of the Laboratory of Intelligent Decision Support Systems (IDSS) within the Institute of Computing Science. He defended his Ph.D. thesis concerning computer decision support in 2012. His main research interests are in Multiple Criteria Decision Making (MCDM) and exploratory data analysis. He holds the MCDM Doctoral Dissertation Award 2013 by the International Society on MCDM and the EURO Doctoral Dissertation Award 2013 – top 3 <sup>fi</sup>nalist – by EURO — The Association of European Operational Research Societies. He has been distinguished by the Polish Academy of Sciences (Best Paper in Technical Sciences 2013), Polish Ministry of Science and Higher Education (for scienti<sup>fi</sup>c achievements), and Foundation for Polish Science (START Scholarship in 2013 and 2014). He has been also acknowledged with the Best Reviewer Award by EJOR in 2012, 2013 and 2014. His works have been published in journals such as Omega, EJOR, DSS, Computers & OR, GDN, OR Spectrum, JOGO, and Machine Learning.

Roman Słowiński is Professor and Founding Head of the Laboratory of Intelligent Decision Support Systems within the Institute of Computing Science, Poznan University of Technology. As member of the Polish Academy of Sciences (PAS), he is currently the president of the Poznan Branch of the PAS. His area of expertise covers multiple criteria decision aiding, preference modeling, rough set theory, granular computing and knowledge discovery. Author or co-author of 14 books and more than 200 papers in major scienti<sup>fi</sup>c journals. Laureate of the EURO Gold Medal (1991), and Doctor Honoris Causa of PolytechMons (2000), University of Paris Dauphine (2001) and Technical University of Crete (2008). He holds, moreover, the Edgeworth-Pareto Award, by International Society on Multiple Criteria Decision Making (1997) and the 2005 Prize of the Foundation for Polish Science, regarded as the most prestigious scienti<sup>fi</sup>c award in Poland. Since 1999, he is editor-inchief of the European Journal of Operational Research. Senior Member of the IEEE.
