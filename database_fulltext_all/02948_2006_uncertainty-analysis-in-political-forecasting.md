---
otero_id: 2948
otero_key: "379WEVXM"
title: "Uncertainty analysis in political forecasting"
authors: "Gleiber Fernandes Royes; Rogério Cid Bastos"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.09.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Uncertainty analysis in political forecasting

Gleiber Fernandes Royes<sup>\*</sup>, Roge´rio Cid Bastos

Universidade Federal de Santa Catarina—Curso de Po´s-Graduac¸a˜o em Cieˆncia da Computac¸a˜o, Floriano´polis—SC—Brazil

Received 28 June 2004; received in revised form 11 September 2004; accepted 13 September 2004 Available online 19 October 2004

## Abstract

Medicine, engineering, and finance are traditional fields for the application of Fuzzy Logic (FL); however, in social sciences, the utilization of FL can be intensely explored as a valuable analysis instrument. Joining fuzzy with Multiple Criteria Decision Making (MCDM), the natural complex and uncertain criteria of social problems can be adequately explored. A suitable uncertainty analysis is the focal point in the social field. In this direction, an intelligent computational method for election forecasting is proposed as a practical result of this research. The main objective is to present a more flexible methodology for political assessment comparing to traditional methods. © 2004 Elsevier B V All rights reserved

Keywords: Fuzzy MCDM; Decision making; Linguistic terms; Political analysis; Fuzzy LR-type interval

## 1. Introduction

The central problem to be evaluated in this research is the limitation of statistical methods dealing with the subjective uncertainty that is present in social fields, particularly in election forecasting. Fundamental suppositions necessary, such as the application of the normal distribution and the independence among events, for statistical methods are not usually applicable for election prediction. Such suppositions are difficult to prove in the real world due to the voter’s behavior. Particular convictions are usually influenced by other opinions, so the voter’s opinions are not independent events—the next section presents more details about this discussion. Statistical methods are indicated to deal with random uncertainties estimating probabilities of future events. However, they were not conceived to treat the partial occurrence of an event. The main data source to be analyzed in election forecasting is the voter’s opinion (and imprecision is the central characteristic of this opinion). Imprecision is the key for a suitable analysis in election investigation. Contradictorily statistical methods request high precision levels, renouncing the strong presence of the human factor that is the center of the decision process in political analysis. Another aspect to be considered is the high complexity and quantity of factors which influence the prediction in politics.

These complex subjective criteria must be aggregated and assessed to produce a satisfactory decision aid [this task will be developed with the help of a Multiple Criteria Decision Making (MCDM) [20] technique]. Hence, the central problem to be considered in this research is the difficulty statistical methods have in treating adequately the kind of uncertainty and imprecision usually existent in political prognostics.

The new methodology here proposed contrast the traditional statistical models for manipulating the imprecise information. This new solution is based on the manipulation of fuzzy sets [19]. The lack of more detailed investigation into the exploration of vague and imprecise information about politics and social sciences served as motivation for this research. Traditional methods of analysis do not deal with the real type of uncertainty present in politics. Statistical methods are used to make prognosis of politics. However, the exploration of other methods is rare because of the unfamiliarity of experts concerning the potential of Computational Intelligent methods that may help to deal with the complex and fuzzy decision in this field.

The main idea to apply Fuzzy Logic (FL) [19] to politics resides in the fact that the political expert reasoning is strongly based on vague and uncertain statements. Normally, neither are precise data available (the voter’s opinion is usually inexact) nor required by the human expert in order to produce adequate predictions (only statistical methods require artificial exact values to present prognostics). The reasoning employed in politics is not exact such as:

Electors’ acceptance of candidate C is equal to 0.86 and his party acceptance is equal to 0.94, so the chances that candidate C will be elected are equal to 0.92.

The natural subjective reasoning form would be:

Electors’ acceptance of candidate C is high and his party acceptance is high, so the chances that candidate C will be elected are strong.

Fuzzy Logic implements the second reasoning form computationally, showing the language used in politics in a direct and realistic way. Therefore, the fuzzy thinking enables the qualitative and subjective analysis, representing the uncertainty present in the problem. This analysis is made by the application of linguistic terms and its respective membership functions.

The practical aim of this work is to explore a new methodology to deal with the vagueness present in political analysis, using a fundamental and complex task as initial target: <sup>b</sup>predict, with reasonable accuracy, possible election winners<sup>Q</sup>. This kind of prediction can be made either before the campaign, as a realistic simulation of the candidate’s chances to support the analysis of the adequate candidate for a party, or during the campaign to adjust some details according to the current results (the influence of some satisfactory/unsatisfactory points could then be examined). Another important advantage of an intelligent decision system, especially in this suggested field, is to supply another <sup>b</sup>opinion<sup>Q</sup>, completely free from personal beliefs, extern pressures or even some biased circumstances of a particular political situation. The election forecasting is not an easy task and normally demands the examination of complex qualitative aspects. A previous work [14] introduces the possibilities of applying a fuzzy rulebased system in politics, but in a distinct aspect: the reelection chances of one current president, governor or mayor.

For the election prediction, a group of fundamental subjective variables was defined with the expert assistance and also with the support of some relevant literature [6,11,13] concerning political analysis. These variables are considered as criteria in a Fuzzy Multiple Criteria Decision Making (MCDM) [20] system. MCDM has been utilized as an important technique in several problems in which the final conclusion depends on different and complex evaluation factors. Some important works which apply Fuzzy MCDM, in distinct fields, can be seen in Refs. [3,5,7,18]. In politics, the prognosis of voting scenarios is usually based on complex criteria which must be carefully weighted and aggregated to produce accurate prognosis. Then, these prognosis can be applied as fundamental resources for detailed analysis. In the methodology suggested here, the candidates are represented as alternatives which will be assessed in accordance with the initial criteria. Thus, it will be possible to combine the use of fuzzy for subjectivity and uncertainty with the capacity of multiple criteria in helping decision making, rating and ranking groups of alternatives.

The next section discusses the main limitations of statistical methods in election forecasting. Section 3 details the problem of election prediction and specifies the new methodology of analysis suggested. In Section 4, the MCDM rating and ranking techniques are presented with a particular modification to the positive and negative ideal concepts applied to produce the expected results. Next, Section 5 exhibits a short practical example of the whole process. Finally, Section 6 shows the conclusions and some points to be further explored.

## 2. Limitations of statistical models for election forecasting

The literature about the elector’s behavior (and more precisely about the election forecasting) is vast [1,2,6,11] and numerous in models. However, the fundamental tools for the great part of these theories are the statistical methods. These models try to describe the voter’s behavior in estimating equations obtained via mechanisms, like linear regression [2] or binary and multinomial logit [1]. These statistical methods are usually applied to posterior analysis of elections with two candidates (simpler scenarios comparing to multiparty elections).

However, some difficulties may occur on the application of these statistical methods. First, the main information source for election forecasting is the subjective, changeable, and not independent voter’s opinion. Second, the theoretical suppositions necessary for the statistical methods are not usually verified in practice. The supposition that random variables have a normal probability distribution (in general the most usually requested due to its important characteristics) is only assured by the Central Limit Theorem [15] resource. In cases of sampling, this theorem is not always probabilistic. In fact, the researcher has great chances of not obtaining the random sample in the real sense required when he selects electors to perform the previsions. Furthermore, in these cases, the independence basic supposition (the occurrence of one event does not change the probability of the occurrence of another event) among the sample elements is not usually verified in political context. The voter opinion is frequently influenced by the dominant ideology, by the opinion of other voters, by the media, and by the opinion of political analysts (voters are not independent variables). Hence, a sampling of electors’ opinions rarely would be represented by an ideal normal distribution and the addition of new opinions does not tend to this expected function as the Central Limit Theorem proves (this irregular behavior is a common situation in social scenarios). Therefore, two basic assumptions of statistical models are difficult to be verified in practice in election forecasting: the voters (whose opinion is fundamental for the prognosis) do not usually present the characteristic of a normal and independent behavior. Statistical conclusions based on hypothetical normal samplings may be elementary to construct; however, this analysis will be not trustful in election prediction, since its own main assumptions were not respected. The probabilistic models are based on the uncertain derived from event occurrences. However, the kind of uncertain present in election forecasting is distinct. The uncertain in this domain is derived from the degree of an event is observed: the degree of investments in the candidate’s campaign can be considered low, medium, or high? These linguistic imprecise values traduce the correct kind of uncertain present in this situation.

Another important aspect to be considered is that there are few statistical works presenting electoral prognosis of multiparty elections. One statistical model for multiparty elections using conditional logit can be seen in Ref. [1]. This kind of voting is not vastly explored due to the increase of complexity with the higher number of factors (criteria) necessary to elaborate the predictions (some statistical models become complex when the number of variables is high). Therefore, a Fuzzy MCDM system is an interesting alternative solution in this context, surpassing several of these restrictions.

## 3. The problem evaluation and the methodology proposed

The practical problem to be solved is how to build up a methodology that can give support to the complex task of election forecasting, starting from some important qualitative information. This task is still more difficult when the voting involves more than two candidates (a multiparty election [1]). The prediction of election results usually involves varied complex criteria that may be satisfactorily addressed by MCDM techniques. The objective is to present an initial model that makes use of five basic criteria previously pointed out by experts and also emphasized in the political literature. The alternatives $A _ { i } ( i { = } 1 , ~ 2 , ~ . ~ . ~ . , ~ n )$ represent the candidates, or probable candidates that will dispute a multiparty election. The subjective criteria $C _ { j } \ ( j { = } 1 , \ 2 , \ . . . , \ m )$ are used to evaluate the chances each candidate has to win the election. The performance assessment of each alternative (candidate) is made qualitatively via linguistic terms (see Table 1) which are more realistic in the context of politics than crisp exact values. The membership function format of each term can be chosen among triangular, trapezoidal, bell, type S, or type Z functions. That characteristic represents a special prerogative (the decision maker can define more accurately the uncertainty) compared with other restrictive Fuzzy MCDM models [4,5,18].

For example, each linguistic term is represented, as default, by a Trapezoidal Membership Function. Trapezoidal numbers [10] may be denoted by four parameters $\{ a , b , c , d \}$ (where $- \infty { < } a { \le } b { \le } c { \le } d { < } \infty )$ 0 with the Membership Function (MF):

$$
f (x) = \left\{ \begin{array}{l l} \frac {x - a}{b - a}, & \quad a \leq x \leq b. \\ 1, & \quad b \leq x \leq c. \\ \frac {d - x}{d - c}, & \quad c \leq x \leq d. \\ 0, & \quad \text { otherwise } \end{array} \right.
$$

Because of its simplicity, flexibility, and computational efficiency, this kind of function has been used intensively in varied applications. As default for the application here presented, this trapezoidal membership function reflects the fuzziness present in the problem and also corresponds to the initial expert evaluation related to the adequate representation about each term. Table 1 shows the linguistic values used for all initial criteria (these values are the model defaults).

The criteria linguistic terms represented as trapezoidal functions (the universe of discourse is normalized in [0,1])

<table><tr><td>Linguistic term</td><td>Trapezoidal membership function</td></tr><tr><td>Low (L)</td><td>(0,0,0.1,0.2)</td></tr><tr><td>Medium low (ML)</td><td>(0.1,0.2,0.3,0.4)</td></tr><tr><td>Medium (M)</td><td>(0.3,0.45,0.55,0.7)</td></tr><tr><td>Medium high (MH)</td><td>(0.6,0.7,0.8,0.9)</td></tr><tr><td>High (H)</td><td>(0.8,0.9,1,1)</td></tr></table>

![](/api/attachments/379WEVXM/fulltext/images/227afe4ed0ec9a246702dbc6bdd4f923e3e04c769bca5bff28989f2ae90dc4e1.jpg)  
Fig. 1. Membership functions of the criteria linguistic terms (default).

The decision maker can also add or remove linguistic terms according to a specific situation. For example, if more detailed information is available, the accuracy and the number of terms can probably be increased.

Fig. 1 represents the membership functions of the linguistic terms of the default criteria graphically. With this representation, it is clear to observe the vagueness and uncertainty present in the proposed political problem: there are fuzzy regions in which clear distinctions between terms are not precise.

The definition about the relevant criteria for election forecasting is a difficult task. For the solution here proposed, an initial list of five fundamental items were chosen. However, the model admits the addition of new evaluation items and also the removal of some of the initial five criteria. In other words, the model may be adapted to regional specific circumstances. The input data for the majority of criteria must be collected by available opinion pools or by the opinion of experts in political sciences. The criteria are listed below:

(1) Candidate’s party organization in the specific region where the election will take place $( \mathbf { C } _ { 1 } ) \colon$ Considering this factor individually, candidates having an organized party will have more chances of triumph (positive criterion).

(2) The candidate’s Rejection rate $( \mathrm { C } _ { 2 } ) { : }$ : The rejection rate represents a counterbalance criterion in relation to the other criteria. This information is obtained by the spontaneous opinion of electors about the candidate who is considered the worst among all contenders. Obviously, candidates having low levels of rejection will have more chances (negative criterion).

Table 2

(3) Popular identification with the candidate’s party $( \mathrm { C } _ { 3 } ) { \mathrm { : } }$ : More elevated levels of popular acceptance for a party are usually linked to its ideological trends that can be either more or less approved by the voters. Anyway, candidates whose political party is more popularly accepted will have more possibilities to win the election (positive criterion).

(4) The candidate’s personal quality (the candidate’s profile) $\mathrm { ( C _ { 4 } ) } \mathrm { : }$ This is the most subjective criterion. It is related to the candidate’s personal characteristics, such as competence, intelligence, morality, and also personal appearance. Electors with precarious education, known as irrational [13], usually incline to vote for candidates that present an image of great morality and intelligence, or even that pass an image of a careful personal presentation (positive criterion).

(5) The prevision of investments in the candidate’s campaign (C<sub>5</sub>): The campaign is promoted by investments in media publicity: newspapers, magazines, and TV programs. Another kind of promotion is obtained by the organization of rallies, contests, and conventions. Again, the weight of this criterion depends on the voter’s profile: normally, more informed electors are not manipulated by electoral campaigns (positive criterion).

The way the criteria are combined and aggregated to produce the final position of each candidate is the central subject of the next section.

## 4. Rating and ranking the alternatives

Two of the most important tasks using the MCDM technique are basically [20]:

How to obtain the overall aggregated index for each one of the alternatives, given the initial input values for the criteria and the respective weights (the rating of alternatives). Linguistic fuzzy values are aggregated by the model here described;

<sup>!</sup> The form of ranking the alternatives (the alternatives, the candidates, must be classified in order of importance).

First, it is necessary to evaluate the weight of importance related to each criterion in order to obtain the aggregated values of each alternative. The model default is the selection of the same weight for all criteria, but the user can interactively modify them, offering different values. This process forms a vector of weights ${ \tilde { W } } _ { n } .$

$$
\tilde {W} _ {n} = (\tilde {w} _ {1}, \tilde {w} _ {2}, \dots , \tilde {w} _ {n})
$$

where each element $\tilde { w } _ { j } ( j { =                      } 1 , 2 , . . . , n )$ corresponds to the respective criterion weight.

The scale of weights’ definition also utilizes linguistic terms (for example, trapezoidal fuzzy values), which are applied to define the criterion importance (see Table 2) qualitatively. The main strategy of this solution applying fuzzy terms instead of exact values is to explore the natural qualitative reasoning employed in politics. An imprecise value, such as <sup>b</sup>Little Important<sup>Q</sup>, will be more expressive and adequate to represent the importance of a criterion than a crisp value, such as 2 or 3.

The Decision Maker can either use one of the fuzzy values defined in Table 2, or define other distinct terms with other function formats, just like the process described before for the fuzzy input values of each criterion. Therefore, the input value Medium for the criterion personal qualities $\mathrm { ( C _ { 4 } ) }$ might be represented by a bell function, while its respective weight Very Important could be defined by a type S function. The idea is not only to supply a default solution, but also to explore the ability of more experienced Decision Makers, given the possibility to experiment particular solutions.

The rating of alternatives is represented as a Decision Matrix $( \tilde { D } _ { m \times n } )$ (see the matrix format below), where every element $\tilde { x } _ { i j }$ represents the respective fuzzy input value of each alternative related to each criterion. The formats of the linguistic terms are equal to Table 1 or another format defined by the system user. These input fuzzy values are directly supplied by the Decision Maker.

The default membership functions of the criteria weights

<table><tr><td>Linguistic term</td><td>Trapezoidal membership function</td></tr><tr><td>Least important</td><td>(0,0,0.1,0.2)</td></tr><tr><td>Little important</td><td>(0.1,0.2,0.3,0.4)</td></tr><tr><td>Medium important</td><td>(0.3,0.45,0.55, 0.7)</td></tr><tr><td>Important</td><td>(0.6,0.7,0.8,0.9)</td></tr><tr><td>Very important</td><td>(0.8,0.9,1,1)</td></tr></table>

$$
\tilde {D} _ {m \times n} = \left[ \begin{array}{c c c c} \tilde {x} _ {1 1} & \tilde {x} _ {1 2} & ... & \tilde {x} _ {1 n} \\ \tilde {x} _ {2 1} & \tilde {x} _ {2 2} & ... & \tilde {x} _ {2 n} \\ ... & ... & ... & ... \\ \tilde {x} _ {m 1} & \tilde {x} _ {m 2} & ... & \tilde {x} _ {m n} \end{array} \right]
$$

Where $m$ is the number of alternatives and $n ,$ , the number of criteria.

In the solution here proposed, each element $\tilde { x } _ { i j }$ is transformed in a fuzzy interval of LR-type (the complete discussion about Left and Right type functions can be observed in the work of Dubois and Prade [8]) to allow the necessary posterior arithmetic operations among distinct formats of fuzzy values. LR fuzzy intervals are very useful as a unified representation to distinct types of information, approximating its membership functions. That solution provides a simplified technique to manipulate fuzzy intervals, replacing the convolution-like algebraic operations [17]. The convolution-type operations are straightforward formulations, but imply sequences of tedious computations.

Continuing with the solution applying LR-type intervals, on a next step, the weighted fuzzy matrix $\tilde { V } _ { m \times n }$ is constructed multiplying (multiplication of fuzzy intervals of LR-type, instead of the convolutionlike operation) the transformed input fuzzy number of each alternative for the respective criterion weight (the weights are also transformed in LR fuzzy intervals, using the format described in Eq. (2)):

$$
\tilde {v} _ {i j} = \tilde {x} _ {i j} ^ {*} \tilde {w} _ {j}\tag{1}
$$

The fuzzy values are converted in fuzzy intervals of LR-type, whose basic idea is to approximate the membership function of a fuzzy interval $\tilde { M } ,$ as a combination of the Left (L) and Right (R) reference functions. The LR fuzzy interval can be defined by four parameters:

$$
\tilde {M} = (\underline {{m}}, \bar {m}, \alpha , \beta) _ {\mathrm{LR}}\tag{2}
$$

where $\underline { m }$ is the center left (or peak left) of the membership function of $\tilde { M } ; \bar { m }$ , the center right, and a and $\beta ,$ respectively, the left and right spreads of the function. The membership function of M<sup>˜</sup> is presented below, L and R being strictly decreasing continuous functions from [0,1] to [0,1] with ${ \mathrm { L } } ( 0 ) { \mathrm { = R } } ( 0 ) { \mathrm { = } } 1$ and ${ \mathrm { L } } ( 1 ) { = } { \mathrm { R } } ( 1 ) { = } 0$ :

$$
\mu_ {\tilde {M}} = \left\{ \begin{array}{l l} \mathrm{L} \big (\big (\underline {{m}} - x \big) / \alpha \big) & \quad \text { for } \quad \quad x \leq \underline {{m}} \\ 1 & \quad \text { for } \quad \quad \underline {{m}} \leq x \leq \overline {{m}} \\ \mathrm{R} \big ((x - \bar {m}) / \beta \big) & \quad \text { for } \quad \quad x \geq \bar {m} \end{array} \right.
$$

Therefore, the product of two fuzzy values converted in a LR fuzzy interval, using the notation exhibited in Eq. (2), is given by:

$$
\begin{array}{l} A = \tilde {x} _ {i j}, \quad B = \tilde {w} _ {j}, \quad \tilde {v} _ {i j} = A ^ {*} B, \quad A > 0, \quad B > 0, \\ A ^ {*} B \cong (\underline {{m}} _ {a} \underline {{m}} _ {b}, \bar {m} _ {a} \bar {m} _ {b}, \underline {{m}} _ {a} \alpha_ {b} + \underline {{m}} _ {b} \alpha_ {a}, \bar {m} _ {a} \beta_ {b} + \bar {m} _ {b} \beta_ {a}) _ {\mathrm{LR}} \end{array} \tag {3}
$$

Considering the concept of LR representation, the method might perform the multiplication of distinct kinds of fuzzy values, which permits the implementation of the suggested model flexibility and avoids the application of the convolution-type operations.

Applying the matrix $\tilde { V } _ { m \times n }$ obtained via the product described in Eq. (1), it is possible to pass to the next step, obtaining the aggregated rating values and the ranking of alternatives.

Several methods used for ranking the alternatives and also for assessing the relative importance of multiple criteria are commented in Fuller’s work [9]. The adequate method depends on the necessities and characteristics of the specific problem. For the election forecasting, an extension of the positive $( A ^ { + } )$ and negative ideal (A<sup>-</sup>) concepts [4,12] was applied. That choice was made because this method has been suggested as a promising solution [4,12,18] when the problem uses directly linguistic terms; and also due to its straightforward use and comprehension, even when the number of alternatives and criteria is elevated. In addition, such a solution is not computer demanding in comparison with some other popular methods. The positive and negative ideal concepts represent the extremes between the appropriate result of one hypothetical alternative and the inappropriate result of it (the best and the worst hypothetical candidates).

The best alternative (in this case, the winner candidate) will be that one having the shortest distance to the positive ideal solution and, at the same time, having the longest distance to the negative ideal solution. The general forms of the positive and negative ideal solutions vectors are respectively:

$$
A ^ {+} = \big (\tilde {\boldsymbol {a}} _ {1} ^ {+}, \tilde {\boldsymbol {a}} _ {2} ^ {+},..., \tilde {\boldsymbol {a}} _ {n} ^ {+} \big),
$$

$$
A ^ {-} = \big (\tilde {\boldsymbol {a}} _ {1} ^ {-}, \tilde {\boldsymbol {a}} _ {2} ^ {-},..., \tilde {\boldsymbol {a}} _ {n} ^ {-} \big),
$$

$$
i = 1, 2, \dots n \quad (\text { where   } n \text {   is   the   number   of   criteria })
$$

$\tilde { a } _ { i } ^ { + }$ and $\tilde { a } _ { i } ^ { - }$ representing a fuzzy number or interval. In the solution here presented, they will represent fuzzy intervals of LR-type, using the same notation presented in Eq. (2). The approach using the positive and negative ideal solutions is similar to other previous contributions, such as Refs. [4,12,18]. However, the difference is exactly related to the meaning of each element in $A ^ { + }$ and $A ^ { - }$ . They are not always triangular or trapezoidal numbers, as proposed in other works, but in fact, they are representations of LR-type fuzzy intervals which enable a generalization of distinct functions. Therefore, for the new approach introduced, each element is represented in $A ^ { + }$ and $A ^ { - }$ , respectively, as:

$$
\tilde {\boldsymbol {a}} _ {i} ^ {+} = (\underline {{m}}, \bar {m}, \alpha , \beta) _ {\mathrm{LR}},\tag{4}
$$

$$
\tilde {\boldsymbol {a}} _ {i} ^ {-} = (\underline {{m}}, \bar {m}, \alpha , \beta) _ {\mathrm{LR}}\tag{5}
$$

The analysis of the best alternatives becomes possible with this solution, even when distinct kinds of fuzzy intervals (or numbers) to input values and to criteria weights are supplied. This solution is better explored in the numerical example exposed next.

The distances of Hamming between each alternative to $A ^ { + }$ and $A ^ { - }$ are calculated:

$$
d _ {j} ^ {+} = \sum_ {i = 1} ^ {m} | \tilde {\boldsymbol {a}} _ {i} ^ {+} - \tilde {\nu} _ {i j} |, j = 1, 2, \dots n\tag{6}
$$

$$
d _ {j} ^ {-} = \sum_ {i = 1} ^ {m} | \tilde {\nu} _ {i j} - \tilde {a} _ {i} ^ {-} |, j = 1, 2, \dots n\tag{7}
$$

Where n represents the number of alternatives to be compared with both the best and worst solution and m, the number of criteria. As both the ideal (positive and negative) and the $\tilde { \nu } _ { i j }$ values are LR fuzzy intervals, the subtractions above have the following format:

$$
A = \tilde {a} _ {i} ^ {+}, B = \tilde {\nu} _ {i j},
$$

$$
\begin{array}{r l} A - B & = \left(\underline {{m}} _ {a} - \underline {{m}} _ {b}, \bar {m} _ {a} - \bar {m} _ {b}, \left(\underline {{m}} _ {a} + \alpha_ {a}\right) \right. \\ & \quad \left. - \left(\underline {{m}} _ {b} + \alpha_ {b}\right), \left(\bar {m} _ {a} + \beta_ {a}\right) - \left(\bar {m} _ {b} + \beta_ {b}\right)\right) _ {\mathrm{LR}} \end{array}\tag{8}
$$

$$
A = \tilde {a} _ {i} ^ {-}, B = \tilde {\nu} _ {i j},
$$

$$
\begin{array}{r} B - A = \left(\underline {{m}} _ {b} - \underline {{m}} _ {a}, \bar {m} _ {b} - \bar {m} _ {a}, \left(\underline {{m}} _ {b} + \alpha_ {b}\right) \right. \\ \left. - \left(\underline {{m}} _ {a} + \alpha_ {a}\right), \left(\bar {m} _ {b} + \beta_ {b}\right) - \left(\bar {m} _ {a} + \beta_ {a}\right)\right) _ {\mathrm{LR}} \end{array}\tag{9}
$$

Finally, a crisp performance index $( P _ { i } )$ is calculated, representing the real final aggregated value for each alternative i:

$$
P _ {i} = \frac {d _ {i} ^ {-}}{d _ {i} ^ {+} + d _ {i} ^ {-}}\tag{10}
$$

The performance index $( P _ { i } )$ is used for ranking the alternatives. In other words, the best alternative is the one having the highest index. Hence, a decreasing order can be easily formed. The next section presents a practical example, detailing the most important rating and ranking steps of a real voting.

## 5. A practical example

This section is dedicated to introduce a real case of voting prediction. The election for mayor in the year 2000, in Floriano´ polis, the capital of the state of Santa Catarina, Brazil, was selected in order to compare the system results with the real election outcome. The necessary information about alternatives and weights of criteria were collected using some opinion pools and the information support provided by institutes as Instituto Brasileiro de Geografia e Estatı´stica (IBGE) [Brazilian Institute of Geography and Statistics] and Instituto Brasileiro de Opinia˜o Pu´ blica e Estatı´stica (IBOPE) [Brazilian Institute of Public Opinion and Statistics]. The information used here was the one available before or at the beginning of the election. In general, exact values or even complete data were not available, making the acceptance of linguistic terms by the system primordial. This facility permits the adequate representation and treatment of imprecise values.

The first task was to investigate whether some new criteria could be relevant to that specific voting. The analysis of the local voter’s behavior (for example, if the voters are rational [13]) and profile pointed to the employment of the five standard criteria: candidate’s party organization, rejection rate, popular identification with the candidate’s party, the candidate’s profile and investments in the candidate’s campaign. The weights were also obtained by the examination of the local voter’s behavior, having the assistance of experts, and via the available data related to the local influence of the five factors. These definitions are imprecise estimations, since exact weights are difficult or impossible to be obtained. Good estimations could be provided with more accurate information available about the criteria weights.

Table 3 shows the respective weights selected for each of the criteria $( \mathbf { C } _ { 1 } , \mathbf { C } _ { 2 } , \dots , \mathbf { C } _ { 5 } )$ . For the weights, the default terms accompanied by its respective trapezoidal functions are used.

It is possible to verify that criteria $( \mathbf { C } _ { 2 }$ and $\mathrm { C } _ { 4 } )$ directly related to the candidate’s profile evaluation, were considered as being more important than criteria $\mathrm { ( C _ { 1 } }$ and $\mathrm { C } _ { 3 } )$ , related to the candidate’s party. This characteristic certainly emphasizes the general voter’s profile, more influenced by the candidate’s profile than by the candidate’s ideological trends (usually a characteristic of less rational voters).

For the formats of the criteria input values, the default values defined in Table 1 and graphically exhibited in Fig. 1 were not used. This can be justified by the fact that functions type $P _ { i }$ presented in Table 4 and Fig. 2 are more adequate to the specific case.

Table 3  
Weights for each criterion with the LR fuzzy interval representation

<table><tr><td>Weight</td><td>Linguistic value</td><td>LR-type representation</td></tr><tr><td> $w_{1}$ </td><td>MI—medium important(0.3,0.45,0.55,0.7)</td><td>(0.45,0.55,0.15,0.15)</td></tr><tr><td> $w_{2}$ </td><td>I—important (0.6,0.7,0.8,0.9)</td><td>(0.7,0.8,0.1,0.1)</td></tr><tr><td> $w_{3}$ </td><td>LI—little important(0.1,0.2,0.3,0.4)</td><td>(0.2,0.3,0.1,0.1)</td></tr><tr><td> $w_{4}$ </td><td>VI—very important (0.8,0.9,1,1)</td><td>(0.9,1,0.1,0)</td></tr><tr><td> $w_{5}$ </td><td>VI—very important (0.8,0.9,1,1)</td><td>(0.9,1,0.1,0)</td></tr></table>

Table 4  
The criteria linguistic terms exclusively defined for the practical problem

<table><tr><td>Linguistic term</td><td> $P_{i}$  membership function</td></tr><tr><td>Low (L)</td><td>(0,0,0.2,0.3)</td></tr><tr><td>Medium low (ML)</td><td>(0.2,0.25,0.35,0.4)</td></tr><tr><td>Medium (M)</td><td>(0.35,0.45,0.55,0.65)</td></tr><tr><td>Medium high (MH)</td><td>(0.55,0.7,0.8,0.95)</td></tr><tr><td>High (H)</td><td>(0.8,0.9,1,1)</td></tr></table>

It is possible to demonstrate the system operation based on fuzzy intervals of LR-type using distinct kinds of membership functions to weights and criteria inputs (trapezoidal and $P _ { i }$ functions).

The initial Decision Matrix is constructed using the available information (see Table 5). Fuzzy input values represent the initial rating of each candidate related to each one of the five criteria presented in the previous section. The number of candidates (in other words, the number of alternatives) running for that election was also equal to five. Table 6 shows the Decision Matrix with the initial rates already translated by the system to the format of LR fuzzy intervals, using the notation exhibited in Eq. (2).

Having the vector of weights properly determined (see Table 3) and the rating of alternatives (candidates) carefully defined by the Decision Maker (see Table 5), the system pass on to the next step. Now, the ratings (fuzzy estimations) of each candidate in the transformed decision matrix (see Table 6) are multiplied by the respective criterion weights, using Eq. (3). Table 7 shows the Weighted Matrix constructed by the system using Eq. (1).

![](/api/attachments/379WEVXM/fulltext/images/446cea984b45544f56451538225601859fdc5ea3bc6c103c835b20189bfea2a9.jpg)  
Fig. 2. The selected membership functions formats for the criteria ratings (to the numerical example).

Table 5  
The original decision matrix $( \tilde { D } _ { 5 } { \times } _ { 5 } )$ with the initial ratings

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td>Portanova</td><td>L (0,0,0.2,0.3)</td><td>MH (0.55,0.7,0.8,0.95)</td><td>M (0.35,0.45,0.55,0.65)</td><td>M (0.35,0.45,0.55,0.65)</td><td>L (0,0,0.2,0.3)</td></tr><tr><td>Vanio</td><td>MH (0.55,0.7,0.8,0.95)</td><td>MH (0.55,0.7,0.8,0.95)</td><td>ML (0.2,0.25,0.35,0.4)</td><td>ML (0.2,0.25,0.35,0.4)</td><td>M (0.35,0.45,0.55,0.65)</td></tr><tr><td>Grando</td><td>ML (0.2,0.25,0.35,0.4)</td><td>M (0.35,0.45,0.55,0.65)</td><td>M (0.35,0.45,0.55,0.65)</td><td>MH (0.55,0.7,0.8,0.95)</td><td>ML (0.2,0.25,0.35,0.4)</td></tr><tr><td>Amin</td><td>H (0.8,0.9,1,1)</td><td>ML (0.2,0.25,0.35,0.4)</td><td>MH (0.55,0.7,0.8,0.95)</td><td>H (0.8,0.9,1,1)</td><td>H (0.8,0.9,1,1)</td></tr><tr><td>Blasi</td><td>H (0.8,0.9,1,1)</td><td>MH (0.55,0.7,0.8,0.95)</td><td>ML (0.2,0.25,0.35,0.4)</td><td>ML (0.2,0.25,0.35,0.4)</td><td>M (0.35,0.45,0.55,0.65)</td></tr></table>

The subsequent step uses the Weighted Matrix and the positive and negative ideal solutions to calculate the distances between the ratings of each candidate and the ratings of a supposed ideal positive and negative candidate (the positive ideal and negative ideal solutions also use values in the format of fuzzy LR-type intervals as presented in Eqs. (4) and (5)). The imaginary positive and negative ideal candidates are represented below. It seems important to say that the second element in the first vector related to criterion $\mathrm { C } _ { 2 }$ represents the ideal candidate whose rejection rate does not exist. The same interpretation is valid for the negative ideal candidate, whose second element represents the maximum rejection rate:

$$
\begin{array}{c} A ^ {+} = ((1, 1, 0, 0), (0, 0, 0, 0), (1, 1, 0, 0), \\ (1, 1, 0, 0), (1, 1, 0, 0)), \end{array}
$$

$$
\begin{array}{c} A ^ {-} = ((0, 0, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0), \\ (0, 0, 0, 0), (0, 0, 0, 0)) \end{array}
$$

Applying Eqs. (6) and (7), the distances $( d _ { i } ^ { + }$ and $d _ { i } ^ { - } )$ of each candidate to the ideal positive and ideal negative candidate are calculated (the difference is obtained via Eqs. (8) and (9)). Finally, the last step produces the ranking order of the candidates, applying the performance index $( \boldsymbol { P } _ { i } )$ obtained by Eq. (10). Table 8 illustrates the distances and also the final ranking order of the five candidates. In order to exemplify this, candidate Amim’s calculations, achieving the first ranking place are presented next:

$$
\tilde {\nu} _ {1 4} = (0. 4, 0. 5 5, 0. 1 8, 0. 1 5),
$$

$$
\tilde {\nu} _ {2 4} = (0. 1 7, 0. 2 8, 0. 1 3, 0. 1 5),
$$

$$
\begin{array}{c} d _ {4} ^ {+} = | \tilde {a} _ {1} ^ {+} - \tilde {\nu} _ {1 4} | + | \tilde {a} _ {2} ^ {+} - \tilde {\nu} _ {2 4} | + | \tilde {a} _ {3} ^ {+} - \tilde {\nu} _ {3 4} | + | \tilde {a} _ {4} ^ {+} \\ - \tilde {\nu} _ {4 4} | + | \tilde {a} _ {5} ^ {+} - \tilde {\nu} _ {5 4} | \end{array}
$$

$$
\tilde {v} _ {5 4} = (0. 8 1, 1, 0. 1 8, 0. 0)
$$

$$
\tilde {\nu} _ {4 4} = (0. 8 1, 1, 0. 1 8, 0. 0),
$$

$$
\tilde {v} _ {3 4} = (0. 1 4, 0. 2 4, 0. 1, 0. 1 2),
$$

$$
d _ {4} ^ {+} = 6. 3 7
$$

$$
\begin{array}{c} d _ {4} ^ {-} = | \tilde {\nu} _ {1 4} - \tilde {a} _ {1} ^ {-} | + | \tilde {\nu} _ {2 4} - \tilde {a} _ {2} ^ {-} | + | \tilde {\nu} _ {3 4} - \tilde {a} _ {3} ^ {-} | + | \tilde {\nu} _ {4 4} \\ - \tilde {a} _ {4} ^ {-} | + | \tilde {\nu} _ {5 4} - \tilde {a} _ {5} ^ {-} | \end{array}
$$

$$
d _ {4} ^ {-} = 1 3. 6 3
$$

First, the score distances relative to the Ideal Positive and Negative Solutions are calculated via Eqs. (6) and (7). The values of each $a _ { i } ^ { + }$ and $a _ { i } ^ { - }$ are taken from the vectors previously described $\boldsymbol { ( A } ^ { + }$ and $A ^ { - } )$ and Amim’s performances related to each criterion (with the values already converted on LR intervals and also multiplied for the respective weights) are obtained by the elements of line four in matrix $\tilde { V } _ { 5 } { \times } _ { 5 }$ (see Table 7). The differences are calculated using Eqs. (8) and (9).

The transformed decision matrix $( \tilde { D } _ { 5 } { \times } _ { 5 } )$ with the ratings as fuzzy LR-type intervals (notation presented in Eq. (2))

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td>Portanova</td><td>(0,0.2,0,0.1)</td><td>(0.7,0.8,0.15,0.15)</td><td>(0.45,0.55,0.1,0.1)</td><td>(0.45,0.55,0.1,0.1)</td><td>(0,0.2,0,0.1)</td></tr><tr><td>Vanio</td><td>(0.7,0.8,0.15,0.15)</td><td>(0.7,0.8,0.15,0.15)</td><td>(0.25,0.35,0.15,0.15)</td><td>(0.25,0.35,0.15,0.15)</td><td>(0.45,0.55,0.1,0.1)</td></tr><tr><td>Grando</td><td>(0.25,0.35,0.15,0.15)</td><td>(0.45,0.55,0.1,0.1)</td><td>(0.45,0.55,0.1,0.1)</td><td>(0.7,0.8,0.15,0.15)</td><td>(0.25,0.35,0.15,0.15)</td></tr><tr><td>Amin</td><td>(0.9,1,0.1,0)</td><td>(0.25,0.35,0.15,0.15)</td><td>(0.7,0.8,0.15,0.15)</td><td>(0.9,1,0.1,0)</td><td>(0.9,1,0.1,0)</td></tr><tr><td>Blasi</td><td>(0.9,1,0.1,0)</td><td>(0.7,0.8,0.15,0.15)</td><td>(0.25,0.35,0.15,0.15)</td><td>(0.25,0.35,0.15,0.15)</td><td>(0.45,0.55,0.1,0.1)</td></tr></table>

Table 7  
The weighted matrix $\tilde { V } _ { 5 } { \times } _ { 5 }$ obtained via Eq. (3)

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td>Portanova</td><td>(0,0.11,0,0.08)</td><td>(0.49,0.64,0.17,0.2)</td><td>(0.09,0.16,0.06,0.08)</td><td>(0.4,0.55,0.13,0.1)</td><td>(0,0.2,0,0.1)</td></tr><tr><td>Vanio</td><td>(0.31,0.44,0.17,0.2)</td><td>(0.49,0.64,0.17,0.2)</td><td>(0.05,0.1,0.05,0.08)</td><td>(0.22,0.35,0.16,0.15)</td><td>(0.4,0.55,0.13,0.1)</td></tr><tr><td>Grando</td><td>(0.11,0.19,0.11,0.13)</td><td>(0.31,0.44,0.11,0.13)</td><td>(0.09,0.16,0.06,0.08)</td><td>(0.63,0.8,0.2,0.15)</td><td>(0.22,0.35,0.16,0.15)</td></tr><tr><td>Amin</td><td>(0.4,0.55,0.18,0.15)</td><td>(0.17,0.28,0.13,0.15)</td><td>(0.14,0.24,0.1,0.12)</td><td>(0.81,1,0.18,0)</td><td>(0.81,1,0.18,0)</td></tr><tr><td>Blasi</td><td>(0.4,0.55,0.18,0.15)</td><td>(0.49,0.64,0.17,0.2)</td><td>(0.05,0.1,0.05,0.08)</td><td>(0.22,0.35,0.16,0.15)</td><td>(0.4,0.55,0.13,0.1)</td></tr></table>

Having the distances already calculated, the last step produces the aggregated performance of each alternative. For candidate Amim, the Performance Index is finally computed:

$$
P _ {4} = \frac {d _ {4} ^ {-}}{d _ {4} ^ {+} + d _ {4} ^ {-}} = \frac {1 3 . 6 3}{6 . 3 7 + 1 3 . 6 3} = 0. 6 8
$$

The ranking order (see Table 8) coincides with the final results of the election. The short distance between Vanio and Blasi accurately defines the difference that happened in the real voting. Another positive aspect of the system results was the confirmation of the high difference between the winner (Amim) and the other candidates. However, a distorting aspect (apparently insignificant) was Grando’s index performance: Grando’s index was distant from Blasi’s in real voting.

## 6. Conclusions and future work

The Fuzzy Multi-Criteria technique reveals a promising way of making predictions in politics. One important advantage of this new technique, comparing with the traditional statistical methods, seems to be the possibility to adapt the model, adding or removing criteria or even altering the weights of some criteria, for instance, conform the electoral reality of each region (flexibility). In statistical solutions, the modification of some equations in order to improve quality results is usually a demanding task. Another important contribution to this field is related to the natural FL capacity to deal with linguistic imprecise terms, which are the main information source in this domain. This capacity makes the model more intelligibly used by nonexpert operators, enabling the direct natural human reasoning.

The distances to positive and negative ideal solutions, the performance indexes, and the final ranking order

<table><tr><td></td><td> $d_{i}^{+}$ </td><td> $d_{i}^{-}$ </td><td> $P_{i}$ </td><td>Ranking</td></tr><tr><td>Portanova</td><td>15.06</td><td>4.94</td><td>0.25</td><td>5</td></tr><tr><td>Vanio</td><td>12.75</td><td>7.25</td><td>0.36</td><td>4</td></tr><tr><td>Grando</td><td>11.60</td><td>8.40</td><td>0.42</td><td>2</td></tr><tr><td>Amin</td><td>6.37</td><td>13.63</td><td>0.68</td><td>1</td></tr><tr><td>Blasi</td><td>12.39</td><td>7.65</td><td>0.38</td><td>3</td></tr></table>

A future improvement for the proposed model is the introduction of a comparative solution for specifying criteria weights. A comparative scale of importance can be applied by the Decision Maker as a means to extract the influence of each criterion more accurately. Another important factor to be observed is that the initial default function formats of linguistic terms related to weights and alternatives performances are a generalized approximation. To use the system in a particular situation effectively, the whole uncertain information must be revised by local political experts in order to possibly redefine some of these values or even to add or remove some criterion.

The innovative approach to the positive and negative ideal concepts by the application of LR fuzzy intervals allowed the implementation of a highly adaptable method, comparing with previous solutions. However, a more rigorous analysis must be made to evaluate the impact that this LR intervals transformation presents in relation to the possibility of some waste in the uncertainty, initially defined by the user. Moreover, a detailed sensitivity analysis [16] must be made concerning the method of Ideal Positive and Negative Solutions. Finally, another important investigation would be the determination of which criterion might be considered the most relevant in relation to the resulting ranking of alternatives. It would be possible to make a more detailed investigation into the factors which determine the current ranking situation after such a study.

The proposed method was applied in election forecasting; however, it can be used as a platform that might support the Decision Maker in many other complex situations. The model might be used for other problems that involve uncertainty and complex criteria, such as the planning of governmental public actions, the simulation of viability of new methods employed by an organization, the selection of new employers by enterprises, and so on. For this kind of experiment, it is necessary to replace the voting criteria with the relevant criteria of the new problem.

In addition to the Fuzzy MCDM tool, a Case Based Reasoning (CBR) scheme could be used to help on analyzing the present situation (as a complementary mechanism). A base of relevant cases might be maintained to allow the recovery of past similar scenarios. These similar scenarios (information about important occurrences that decided or changed the scenario) could be used to assist the exploration and simulation over the new situation. The gradual increasing of new experimented cases would act as a learning mechanism for the model.

The first tests, as illustrated by the example presented in this paper, have shown promising results to help Decision Makers in complex situations, mainly in political forecasting scenarios.

## References

[1] R. Alvarez, When politics and models collide: estimating models of multiparty elections, American Journal of Political Science 42 (1) (1998) 55–96.

[2] H. Asher, Voting behavior research in the 1980s: an examination of some old and new problem areas, in: Ada Finifter (Ed.), State of Political Science II, American Political Science Association, Washington, 1983.

[3] N. Belacel, Multicriteria assignment method PROAFTN: methodology and medical application, European Journal of Operational Research 125 (1) (2000 (Aug.)) 175–183.

[4] C. Chen, Extensions of the TOPSIS for group decision-making under fuzzy environment, Fuzzy Sets and Systems 114 (1) (2000 (Aug.)) 1 – 9.

[5] C. Chen, A fuzzy approach to select the location of the distribution center, Fuzzy Sets and Systems 118 (1) (2001 (Feb.)) 65– 73.

[6] R. Dalton, M. Wattenberg, The not so simple act of voting, in: Ada Finifter (Ed.), State of Political Science II, American Political Science Association, Washington, 1993.

[7] O. Despica, S.P. Simonovic, Aggregation operators for soft decision making in water resources, Fuzzy Sets and Systems 115 (1) (2000 (Oct.)) 11 – 33.

[8] D. Dubois, H. Prade, Fuzzy numbers: an overview, in: J.C. Bezdec (Ed.), Analysis of Fuzzy Information, Mathematics and Logic 1, CRC Press, Boca Raton, 1987.

[9] R. Fuller, C. Carlsson, Fuzzy multiple criteria decision making: recent developments, Fuzzy Sets and Systems 78 (1) (1996 (Mar.)) 139–153.

[10] A. Kaufmann, M.M. Gupta, Introduction to Fuzzy Arithmetic Theory and Application, Van Nostrand Reinhold, New York, 1991.

[11] G. King, Why Are American Presidential Election Campaign Pools So Variable When Votes Are So Predictable? Cambridge University Press, 1993.

[12] G. Liang, Fuzzy MCDM based on ideal and anti-ideal concepts, European Journal of Operational Research 112 (3) (1999 (Feb.)) 682–691.

[13] W.E. Miller, J. Shanks, The New American Voter, Harvard University Press, London, 1996.

[14] G.F. Royes, R.C. Bastos, Fuzzy sets in political science, Joint 9th IFSA World Congress and 20th Nafips International Conference, 2001.

[15] B. Thorne, W.L. Carlson, Applied Statistical Methods for Business, Economics, and the Social Sciences, Prentice Hall, New Jersey, 1997.

[16] E. Triantaphyllou, Multi-Criteria Decision Making Methods: a Comparative Study, Kluwer Academic Publishers, 2000.

[17] R.R. Yager, D.P. Filev, Essentials of Fuzzy Modeling and Control, John Wiley & Sons, New York, 1994.

[18] C.H. Yeh, H. Deng, Y. Chang, Fuzzy multicriteria analysis for performance evaluation of bus companies, European Journal of Operational Research 126 (3) (2000 (Nov.)) 541–556.

[19] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965).

[20] H.J. Zimmermann, Fuzzy Set Theory and its Applications, Kluwer Academic, Boston, 1991, pp. 338 – 353.

![](/api/attachments/379WEVXM/fulltext/images/a2ccffaa7208df2645fdcd7fc09be0fcec0dc3fff5e0830ad601fafc36060af5.jpg)  
Gleiber F. Royes is a software analyst of the Brazilian government in Floriano´ polis, Santa Catarina. He has been a Professor for many years of Graduate Programs in Computer Science in several institutions of Brazilian South. Dr. Gleiber received his Dr. Degree in Computer Science (Expert Systems subarea) from the Federal University of Santa Catarina (Brazil) and his MS Degree in Computer Science from the Federal University of Rio Grande do Sul

(Brazil). His main interests are in fuzzy sets and fuzzy logic, decision making systems, and case-based reasoning models.
