---
otero_id: 16132
otero_key: "5VMGTXUT"
title: "Hybrid assessment method for software engineering decisions"
authors: "Rita A. Ribeiro; Ana M. Moreira; Pim van den Broek; Afonso Pimentel"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.12.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hybrid assessment method for software engineering decisions

Rita A. Ribeiro <sup>a,</sup>⁎, Ana M. Moreira <sup>b</sup>, Pim van den Broek <sup>c</sup>, Afonso Pimentel <sup>a,b</sup>

<sup>a</sup> UNINOVA, CTS, Departamento Engenharia Electrotécnica, Faculdade de Ciências e Tecnologia, Universidade Nova de Lisboa, 2829-516 Caparica, Portugal

<sup>b</sup> CITI, Departamento de Informática, Faculdade de Ciências e Tecnologia, Universidade Nova de Lisboa, 2829-516 Caparica, Portugal

<sup>c</sup> Department of Computer Science, University of Twente, P.O. Box 217, 7500 AE Enschede, The Netherlands

## a r t i c l e i n f o

Article history: Received 22 March 2010 Received in revised form 10 December 2010 Accepted 19 December 2010 Available online 24 December 2010

Keywords: Multi-criteria decision making Non-functional software requirements Software engineering Aggregation operators

## a b s t r a c t

During software development, many decisions need to be made to guarantee the satisfaction of the stakeholders requirements and goals. The full satisfaction of all of these requirements and goals may not be possible, requiring decisions over con<sup>fl</sup>icting human interests as well as technological alternatives, with an impact on the quality and cost of the <sup>fi</sup>nal solution. This work aims at assessing the suitability of multi-criteria decision making (MCDM) methods to support software engineers' decisions. To ful<sup>fi</sup>l this aim, a HAM (Hybrid Assessment Method) is proposed, which gives its user the ability to perceive the in<sup>fl</sup>uence different decisions may have on the <sup>fi</sup>nal result. HAM is a simple and ef<sup>fi</sup>cient method that combines one single pairwise comparison decision matrix (to determine the weights of criteria) with one classical weighted decision matrix (to prioritize the alternatives). To avoid consistency problems regarding the scale and the prioritization method, HAM uses a geometric scale for assessing the criteria and the geometric mean for determining the alternative ratings.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

In software development, many choices need to be made and decisions to be taken; these depend on obtaining answers for some critical questions, such as: Which non-functional requirements can be satis<sup>fi</sup>ed and, from those, which should be implemented <sup>fi</sup>rst? Which of them are the main drivers for the software architecture design? What is the software architecture design style, or combination of styles, that best satis<sup>fi</sup>es a set of quality attributes? Is there a way to help project managers to decide which requirements should be addressed (as the development spiral evolves and widens, it brings more requirements than those already identi<sup>fi</sup>ed)? The answer to such questions can help software engineers greatly to implement products, or applications, while ensuring better satisfaction of stakeholders' requirements. So far, only a handful of research works have addressed some of these questions, particularly on how the prioritization of a set of alternatives, or ranking, based on a set of criteria, helps software engineers to make informed decisions about software development [6,16,18,22,23,26,32]. Those rankings have been used to help in answering the questions above and others related with planning and managing team work, for example.

The aim of Multi-Criteria Decision Making (MCDM) methods [13,33,36] is to rank a set of alternatives (e.g., non-functional requirements, architectural styles) that best satisfy a given set of criteria (e.g., stakeholders, requirements). Although MCDM methods are widely used as supporting tools for decision making in several domains (see for example [7,13,15,18,28,32,33]), many have limitations. For instance, the well known AHP method [29–31] presents two main drawbacks: (i) its partial linear scale and its prioritization method — either the arithmetic average or the eigenvectors prioritization approach [5,11,20,33,34]; (ii) the high number of pairwise contributions, one per criterion matrix plus 1, just for a level-1 problem (e.g., for a problem with 6 criteria and 4 alternatives the user has to <sup>fi</sup>ll six (4,4)-matrices and one (6,6)-matrix). Hence, the main motivation for this work is to de<sup>fi</sup>ne a simple MCDM method to support software development decisions, while, at the same time, to provide trade-offs between criteria weights, which have a compensatory nature and avoid known limitations in terms of scale and ranking method.

In this paper we discuss HAM (Hybrid Assessment Method), an integrated MCDM method that combines one pairwise comparison matrix with one classical multicriteria decision matrix, hence requiring only 2 matrices for the reasoning process. In short, HAM's two major distinctive characteristics are:

HAM borrows the interesting pairwise comparison capability from the AHP method [14,29,30] to automatically determine criteria weights by using trade-offs between attributes (in our case requirements). However, it avoids the problematic Saaty scale and prioritization method by using Ma-Zheng's scale [20] and the geometric means of rows [5,11], respectively.

HAM uses a classical weighted decision matrix [36], pro<sup>fi</sup>ting from its simplicity and ef<sup>fi</sup>ciency, but substitutes the weighted average by the geometric means to ensure uniformity and compatibility in the combined proposed method.

The main objective of HAM is to support software engineers to make better, well-thought decisions, by providing a systematic process to prioritize a set of alternatives based on a set of criteria. A preliminary version of HAM was <sup>fi</sup>rst devised by the authors as a tool support for Software Product Lines [9], within the AMPLE project [2] and in [27], but its formalization, rationale and generality were not yet discussed nor published.

This paper is organized in eight sections. This <sup>fi</sup>rst section summarizes the problem addressed. Section 2 motivates this problem by explaining its context and highlighting its importance for software development. Section 3 presents the background foundations for HAM. It starts with a taxonomy for MCDM methods, chooses four representatives, compares them according to a set of criteria, and <sup>fi</sup>nishes with a brief overview of the current state of the art of MCDM in software engineering. Section 4 details HAM, describing its procedural steps and their respective formalization. Section 5 illustrates HAM with an example, discusses its calculation process and compares the results of using the HAM's geometric means prioritization operator with the results using arithmetic means. Section 6 introduces HAM's supporting tool and Section 7 discusses the method's advantages and drawbacks. Section 8 concludes the paper presenting some <sup>fi</sup>nal remarks, and highlights the generalization of HAM's usage for any decision-making domain as our goal for the near future.

## 2. Importance of software engineering decisions

Handling Non-Functional Requirements (NFRs) [33] (also known as quality attributes) is a complex task, commonly not (or at most super<sup>fi</sup>cially) considering the impact of different stakeholders' preferences on each other or on the choices required during development. For example, deciding on the list of requirements and qualities the system should satisfy may be dif<sup>fi</sup>cult, never mind exploring one or more corresponding software architecture<sup>1</sup> designs, which requires a long and dif<sup>fi</sup>cult period of re<sup>fi</sup>nement and <sup>fi</sup>ne-tuning. This hard task is usually driven by the system qualities, and the architects' expertise and experience. The <sup>fi</sup>nal architecture may, therefore, never become something truly concrete on the developers' team minds, or even in the <sup>fi</sup>nal system. Selecting a good architecture is a fundamental step of software development, but often it is “lost somewhere” among the various systems' modules resulting from designing the system.

We believe we can do better. We can provide a systematic process, making available the most appropriate information, techniques and tools to support the developers' choices. For example, if we are able to perform a rigorous trade-off analysis on the requirements, in particular on the system qualities – which are those that will have a stronger impact on the structure and therefore the system's software architecture – we will be in a position to make better informed decisions, even before we need to make any architectural choices [1,8]. Hence, based on the qualities identi<sup>fi</sup>ed (or a subset of interest) and eventual additional qualities, HAM should encompass to:

(1) identify the stakeholders' preferences and objectives (these objectives refer to system qualities) on what the system should do, providing a ranking of the qualities, taking into consideration the stakeholders' importance;

(2) import these qualities to the architectural phase and choose an architecture that tries to satisfy the ranking obtained initially;

(3) obtain a ranking of products that can be commercialized independently of the core, aiming at deciding what should be developed <sup>fi</sup>rst, for example;

(4) allow software engineers to perform what-if analysis regarding changes in priorities for the implementation of qualities, consideration of new candidate alternatives (e.g. other architectures), new architectural styles, new functional requirements, and so forth.

The <sup>fi</sup>rst point tells us about the stakeholders' goals, and helps solving potential differences in opinion they may have in terms of the qualities the future system (or product, or family of products), should satisfy. A typical example is that the security and response time are usually the con<sup>fl</sup>icting quality attributes, that is, if we need a strongly secure system, it may well be that the response time will increase. The qualities that con<sup>fl</sup>ict each other are fundamental information in a trade-off analysis (point 4). In such cases, we should look at the initial stakeholders' desires, and check which of the con<sup>fl</sup>icting qualities is ranked higher. This ranking can, from thereafter, be used as a guide by the developers to try their best to satisfy the stakeholders' wishes. This, together with the other potential con<sup>fl</sup>icting qualities, should guide the information to be passed over to the architect.

The second point is about having available trustworthy information from where architects can stem a <sup>fi</sup>rst vision of the software architecture. System qualities are the criteria with higher impact on the architecture. Therefore, it is necessary to identify and prioritize those we need to address. The main dif<sup>fi</sup>culty the architects face is to choose the architectural alternative, or combination of alternatives, that best satis<sup>fi</sup>es the set of chosen qualities. The choice of the wrong architectural style, or combination of styles, can bring serious problems throughout the software lifecycle, having a strong impact on the success or failure of the system. As explained in [1], different requirements may pull the architecture in various directions; each quality leads to a number of architectural choices, each one satisfying the system requirements and serving the stakeholder needs with varying levels of stakeholder satisfaction.

The third point addresses questions related with the identi<sup>fi</sup>cation and selection of new sellable components or products by transforming a software system into components and consequently unveiling new business opportunities. Or, in the case of a software product line, decide which product from a range of several products, should <sup>fi</sup>rst hit the market. The ranking for potential candidate components or products to be developed may support decision makers in identifying new business opportunities with less risks and costs.

The fourth point gives developers the <sup>fl</sup>exibility to play with different choices and understand their impact on the ranking and, consequently, on the decisions they have to make. This is very important, because, it also enables storing decisions and their respective rationale, which might be useful in future similar decision processes.

An example of a real application using the preliminary HAM is described in [16].

## 3. An overview of multi-criteria decision making

Multi-Criteria Decision Making (MCDM) methods use formal techniques to support decision makers to choose between a discrete set of alternatives [7,13,33,36]. This process is performed by analysing a <sup>fi</sup>nite set of alternatives with respect to a set of criteria. A criterion represents a rule on which a judgement has to be made. The alternatives, which represent the options available to the decision maker, have to be prioritized and classi<sup>fi</sup>ed using the judgments or contributions of each criterion.

Although multi-criteria problems can be very different and diverse, there are some common features to all of them [36], such as:

Alternatives: <sup>fi</sup>nite set of candidate solutions of a problem. Criteria: each problem has a set of independent attributes that has to be satis<sup>fi</sup>ed by the alternatives.

Units: each criterion may be measured in different units, for example, kilos or meters; however, they all have to use a normalized classi<sup>fi</sup>cation being either a numeric scale or a qualitative scale (e.g., not important, important, very-important).

Weights: these represent the relative importance of each criterion. They can be directly assigned by the decision maker or automatically generated by a trade-off method.

Decision Matrix: the problem can be expressed in a matrix. Usually, the columns represent the criteria and the lines the alternatives. An element $x _ { i j }$ of the matrix indicates the degree to which alternative $A _ { i }$ satis<sup>fi</sup>es criterion $C _ { j } .$

## 3.1. MCDM approaches

Usually, any MCDM method involves an initial process of eliciting the decision makers' preferences or judgments regarding the contributions of alternatives to criteria as well as the respective weights associated with the criteria. Afterwards, MCDM methods use mathematical algorithms to determine the prioritization of alternatives [36]. The logical principle of these methods is to rely on judgements of experts to derive the ranking of alternatives [33]. MCDM methods are used in a broad variety of problems, from <sup>fi</sup>nancial applications, sports, e-business, software engineering, to selecting the best site for landing a spacecraft [1,7,15,18,23,26,32].

There are many MCDM methods described in the literature and Fig. 1 represents a general taxonomy, adapted from [7,36], for the most well-known multi-criteria methods. This taxonomy depicts four categories of methods, each of which with at least two well-known methods in each category [27].

To perform a comprehensible comparative study of MCDM method's advantages and disadvantages to support software engineering decisions, but avoiding a lengthy comparison process (out of scope in this work), we picked-up a representative method from each category and compared them using <sup>fi</sup>ve criteria. The rationality for choosing the four methods was based on their widespread usage and record publications. For example, AHP has more than 1000 references, and, as mentioned in [33], AHP, WA (Weighted Average) and TOPSIS are the most well known MCDM methods.

The following list describes the main characteristics of the four candidate methods for the comparison:

Maxmin [13,36] from the non-compensatory category. This method selects the alternative whose lowest score on the criteria is maximal It is a simple method using the logic “a chain is only as strong as its weakest link” [11]; for example, an astronaut's life or death in orbit may depend upon his/her worst vital organ. This method's main advantages are the use of a pessimist attitude (less risky) and the inclusion of very simple calculations. Its three main disadvantages are: not to allow judgements among criteria; not to provide compensatory behaviour between criteria; and to choose an alternative solely based on satisfaction of one single criterion.

Weighted Average (WA) [13,33,36] from the Scoring Methods category. The WA logic is that the <sup>fi</sup>nal score of alternatives is obtained by the weighted sum of each criterion satisfaction value. WA is the most well-known and widely used MCDM method because it is simple, easy to use and understand, and allows some compensatory trade-offs among criteria with their weights. Furthermore, any spreadsheet can act as a tool support since it only requires one decision matrix. However, it does not offer pairwise comparisons or logical consistency checking. Hence, no dependencies or relationships between criteria can be expressed.

TOPSIS (Technique for Order Preference by Similar to Ideal Solution) [33,36] from the Ranking Methods category. This method de<sup>fi</sup>nes the order of the alternatives by their distance to an ideal solution. The basic principle of this method is to <sup>fi</sup>nd a solution with the shortest distance from the positive-ideal solution and the biggest distance from the negative-ideal solution. It uses the Euclidean distance (or any other) to calculate the shortest distance. This method [36] is easy to understand and it ensures that the tradeoff among attributes is compensatory. However, it requires more calculations and its major drawback is requiring the a-priori de<sup>fi</sup>nition of two parameters (the positive and negative ideal solution); thus, it is a context-dependent method.

![](/api/attachments/5VMGTXUT/fulltext/images/ac7a947c50aa2e872c4051f00f39be9e91ab5e13f704dcb197e502934a2f645a.jpg)  
Fig. 1. MCDM taxonomy (adapted from [8]).

Analytic Hierarchy Process (AHP) [11,29–31,33] from the Comparative Methods category. It is one of the most widely known methods offering pairwise comparison trade-offs. AHP relies on expert judgements to derive priority scales (ranking of alternatives). The comparisons are made using a scale of judgments that represent how much more one element is important than another with respect to a given criterion. AHP also provides a measure for detecting logical inconsistencies for these judgements. Nonetheless, its major disadvantages are the inconsistencies introduced by the linear scale and the need for a large number of pairwise comparisons (e.g., considering 4 criteria and 5 alternatives the user has to provide 50 judgements), which makes it dif<sup>fi</sup>cult to analyse results for each single matrix. In summary, AHP is low in ef<sup>fi</sup>ciency and in usability. Besides lacking ef<sup>fi</sup>ciency, AHP has consistency problems imposed by the used linear scale [1 .. 9], as pointed out by Triantaphyllou and Dong [11,33].

## 3.2. Comparison of MCDM methods

The methods brie<sup>fl</sup>y described in the previous subsection were compared to assess their main strengths and weaknesses regarding their suitability for software engineering decision support. We have used four criteria for this comparison, whose choice was based on relevant features for software engineering decisions:

Ef<sup>fi</sup>ciency: this criterion assesses if the method is time-consuming in terms of processing and implementation.

Usability/understandability: this is a quality attribute that assesses how easy user interfaces are to use. The word “usability” in this context also refers to how easy it is to understand the method (by any novice MCDM practitioner such as software engineers (our target users)).

Pairwise comparisons: it is proven by psychological studies that it is easier to compare elements two-by-two (pairwise) to determine their relative importance (weights), instead of assigning importance directly to elements [14]. This feature is particularly interesting to perform trade-offs between criteria in software engineering where we need, for example, to achieve a decision between non-functional requirements or even reaching consensus between stakeholders.

Compensatory: this criterion checks if the method allows some compensatory behaviour between criteria, that is, if all criteria contribute to the <sup>fi</sup>nal result.

Based on the criteria list above, we compared the four chosen MCDM methods, using a simple discrete scale with three levels (0 – Bad; 1 – Reasonable; 2 – Good) and assuming that any method would require the satisfaction of all criteria, meaning that there should not be a criterion with “bad” classi<sup>fi</sup>cation. Table 1 shows the scores provided by the authors to each criterion and the <sup>fi</sup>nal aggregated score using a simple average.

Table 1  
Comparing MCDM methods

<table><tr><td></td><td>Efficiency</td><td>Pair-wise comparisons</td><td>Compensatory</td><td>Usability</td><td>Final score</td></tr><tr><td>Maxmin</td><td>2</td><td>0</td><td>0</td><td>2</td><td>1.00</td></tr><tr><td>WA</td><td>2</td><td>0</td><td>2</td><td>2</td><td>1.50</td></tr><tr><td>TOPSIS</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0.75</td></tr><tr><td>AHP</td><td>0</td><td>2</td><td>2</td><td>1</td><td>1.25</td></tr></table>

Considering the characteristics of each candidate method, we classi<sup>fi</sup>ed their contributions for each criterion. For example, considering that Maxmin is a MCDM method with a very simple logic, its ef<sup>fi</sup>ciency and usability are good; therefore the assigned value was 2. Another example is pairwise comparisons: since AHP is the only method in the set of candidates with this feature, we classi<sup>fi</sup>ed it with 2 and the others with 0.

Table 1 indicates that WA is the best candidate with a total score of 1.5. However, since none of the methods satisfy all criteria $( C _ { \mathrm { i j } } { > } 0 )$ and the winner only lacks the pairwise comparison criterion, we decided to integrate WA and AHP (the best 2 candidates) and the result is the proposed Hybrid Assessment Method (HAM). Details about the proposed method are discussed in Section 4.

## 3.3. Multi-criteria methods in software engineering

MCDM methods are not new to the software engineering world (e.g. [1,4,15,19,35]). There are several situations where these methods have been used to solve different types of problems, in particular to identify and prioritize con<sup>fl</sup>icting Non-Functional Requirements (NFRs) [8,35], or even just prioritizing requirements in Requirements Engineering [4,21]. Until recently, efforts have been focused on solving con<sup>fl</sup>icts between aspects for stakeholders, using more formal ways to deal with the issues at hand, and incipient usage of MCDM methods was also proposed to create rankings of concerns, both aspectual and non-aspectual [4,6,16,27].

As mentioned before, a typical example of a con<sup>fl</sup>ict, many times mentioned in the literature, involves the NFRs security and response time, where, on one hand, the system needs to be secure and, on the other hand, its response time needs to be minimized [6,24]. Security and response time contribute negatively to each other since more security measures imply higher response time [8]. Thus, it is not possible to simultaneously maximize security and minimize response time, since they are both in con<sup>fl</sup>ict.

The motivation for developing HAM is to provide support for the following software engineering decisions:

• Provide a prioritization (ranking) for non-functional requirements (NFR) to help software engineers to decide which qualities are more important to be satis<sup>fi</sup>ed and, in case of con<sup>fl</sup>ict, which should be prioritized over others;

• Recommend the best architecture by ranking architectural alternatives considering the stakeholders opinions;

• Allow “what-if” analysis to perform system behaviour analysis by simulating changes to it. For example:

i What happens if a new stakeholder or NFR is added to the system? Does the NFR rank change? What is the impact of adding new NFRs to the system?

ii What is the impact on the architecture if a new NFR is added? Will the architecture suffer? Will this “disturb” the current balance of the architecture, or change the implementation order?

iii What happens if we change the contribution value of a given architecture to an NFR, for example? Will this affect the <sup>fi</sup>nal ranking of the architecture styles?

However, this work focuses on HAM's model and algorithm and not on its functionalities to support the software engineering decision process. An in-depth discussion about its functionalities regarding answering the above questions and other software engineering decisions is left for more specialized papers on the topic.

## 4. Hybrid Assessment Method (HAM)

HAM is a two-phase process, composed of <sup>fi</sup>ve steps in total, as shown in Fig. 2 [27]. The <sup>fi</sup>rst step is to elicit the criteria and the alternatives. The second step performs trade-offs between criteria using pairwise comparisons. The third step is to calculate the criteria priority vector, normalize the respective weights and calculate the consistency ratio. If the consistency ratio is under 10% (or b8% if the matrix has less than 5 criteria) [31,33], the logical consistency of the pairwise matrix is considered to be suf<sup>fi</sup>cient. If it is 10% or higher, the values should be revised until the consistency ratio becomes less than 10%. These three steps belong to Phase 1 of our process and, roughly, correspond to an automated determination of weights for the decision matrix.

![](/api/attachments/5VMGTXUT/fulltext/images/d6435ac1132f22c83cba56fd511dc1c10f210201dab83dfb50b4f398ee28b997.jpg)  
Fig. 2. HAM step by step.

Phase 2 starts in step four, which elicits the contributions of each alternative with respect to each criterion, using a classical WA's decision matrix. The <sup>fi</sup>fth and <sup>fi</sup>nal step is an aggregation process to determine the prioritization of alternatives (ranking) using a geometric aggregation operator [11]. This step concludes our process by providing the ratings for each alternative.

## 4.1. HAM scale

HAM uses the Ma-Zheng [20] scale because, according to [11,33], it is more appropriate for the kind of problems we are handling. For instance, Triantaphyllou et al. [33] performed an exhaustive study considering the choice of scale as a typical multi-criteria problem, where the criteria are: inversions and indiscriminations. Inversion happens when we know the real ranking of alternatives and the method being tested ranks them in a different order. For example, the real ranking of three alternatives is equal to (1N3N2) and the tested method result is (1N2N3). Indiscrimination happens when the tested method yields a tie between two or more alternatives, for example, if the calculated result is (1N3=2). Furthermore, Triantaphyllou tested 78 different scales, classi<sup>fi</sup>ed as Class 1, Class 2, …, Class 78, which depict different performances in terms of the two above mentioned criteria and also on the number of criteria used.

For HAM we observed that the best class of scales is Class 1, since it covers the majority of the sizes of sets of criteria and considers equal weights for the criteria. For software engineering problems, inversion and indiscrimination are equally important. Note that Class 1 includes the selected Ma-Zheng scale, shown in Table 2.

To better clarify our selection we also performed a comparative behavioural study between three well-known scales (depicted in Fig. 3): the Saaty's scale, an exponential scale (with c=2 to make it comparable with the other scales), and the Ma-Zheng scale. The Y-axis depicts the normalized scale values and the X-axis presents the interface scale used in HAM, to ensure user-friendliness in the dialog with the user. Table 2 shows: the interface scale (used to facilitate the visualization/interaction process); the Ma-Zheng scale (used in HAM selected internal calculations); the Linguistic interpretations (for all scales discussed); and the AHP scale (Saaty). As can be observed in Fig. 3, Saaty's scale has a quasi-linear behaviour, which may cause consistency problems. Moreover, it is not discriminative enough in the positive ranges (from extremely important to equal importance)

with respect to their reciprocals, since they should depict a more similar inverse behaviour.

Comparing the Ma-Zheng scale with the exponential one we observe that in the interval [1 .. 1/9] the Ma-Zheng scale (Table 2) presents quasi-evenly distributed values and in the interval [9 ..1] an almost exponential behaviour. According to [11] the Ma-Zheng scale is a good choice and since it depicts a smoother behaviour for smaller importance/preferences than the exponential scale with c= 2 for comparative purposes with the other scales (Fig. 3), hence we selected the former.

In addition, it should be highlighted that we used a more intuitive numerical scale in the interface (Column 1 of Table 2) so that the decision maker does not have to know details about the less userfriendly Ma-Zheng scale. Another interesting aspect in the interface scale, is how we depict the inverse rating values, $c _ { j i } = 1 / c _ { i j }$ (both used by HAM and AHP), since we represent them with negative values to facilitate the user dialog with the software system. For example, if an alternative criterion is rated with “high importance” (value 4 in column 1 of Table 2), when we want to express its opposite, i.e., “low importance”, we use its negation $( \mathrm { i } . \mathrm { e } _ { \cdot } , - 4 )$ . Another example is that for equal importance we believe that using 0 to express “no” preference, instead of 1, allows a more intuitive classi<sup>fi</sup>cation for users. The interface developed also includes the linguistic interpretation to better guide novice users. Notice, however, that we use the Ma-Zheng scale for HAM calculations.

## 4.2. HAM computations

This section speci<sup>fi</sup>es a stepwise process of the computations performed by HAM, as described in Fig. 2. The <sup>fi</sup>rst step of Phase 1 is to identify the criteria and the alternatives. Let nc be the number of criteria and na the number of alternatives. The second step elicits the decision maker judgements for the relative importance of each pairwise comparisons; these importance are the elements of the criteria matrix c of dimension nc. For all i and j with 1≤ibj≤nc the ith and jth criterion are compared, leading to the value c using Table 2, second column (HAM scale). The remaining entries of the matrix are determined by c $_ { j i } = 1 / c _ { i j } ,$ i.e. the inverse function. In the third step, HAM calculates the priority vector for the criteria, which represents the weights for Phase 2, using the geometric mean. The geometric mean has been selected for the prioritization method for pairwise matrices, following the conclusions of Dong [11] about its superior suitability over Saaty's eigenvalue method. Thus, the geometric mean is given by:

Table 2  
HAM Interface rating values, HAM Scale, interpretation, AHP comparative scale.

<table><tr><td>HAM interface numerical rating</td><td>HAM scale (calculations done with Ma-Zheng)</td><td>Linguistic interpretation</td><td>Comparative AHP scale (Saaty)</td></tr><tr><td>8</td><td>9/1</td><td>Extremely high importance</td><td>9</td></tr><tr><td>6</td><td>9/3</td><td>Very High importance</td><td>7</td></tr><tr><td>4</td><td>9/5</td><td>High importance</td><td>5</td></tr><tr><td>2</td><td>9/7</td><td>Medium high importance</td><td>3</td></tr><tr><td>0</td><td>9/9</td><td>Equal importance</td><td>1</td></tr><tr><td>-2</td><td>7/9</td><td>Medium low importance</td><td>1/3</td></tr><tr><td>-4</td><td>5/9</td><td>Low importance</td><td>1/5</td></tr><tr><td>-6</td><td>3/9</td><td>Very low importance</td><td>1/7</td></tr><tr><td>-8</td><td>1/9</td><td>Extremely low importance</td><td>1/9</td></tr><tr><td>Intermediate values</td><td>Intermediate values</td><td>Intermediate values</td><td>Intermediate values</td></tr></table>

![](/api/attachments/5VMGTXUT/fulltext/images/1c9dad0c942dac6a9c4f053f74df2d06c393c43c6585f76af4e8d3fcdd0cad96.jpg)  
Fig. 3. Scales comparison.

$$
w _ {i} = n c \sqrt {\prod c _ {i j}}\tag{1}
$$

Normalizing this vector, we obtain the vector NW of normalized weights:

$$
n   w _ {j} = \frac {w _ {j}}{\sum w _ {j}}\tag{2}
$$

The next step is to compute the consistency index CI of the c matrix criteria [16], which is de<sup>fi</sup>ned as:

$$
C I = \frac {\lambda - n c}{n c - 1}\tag{3}
$$

where λ, instead of being the largest eigenvalue of c [30,33], is an average of the normalized weighted vector (i.e., normalized priority vector nw in Eq. (2)) divided by the normalized priority vector nw, as described in [3,31]. That is, this calculation is performed by multiplying the pairwise matrix by the nw vector and then divides each obtained vector value by its respective nw vector value. Then, this consistency index must be compared with a Random Index (RI), which is the average of the consistency indices of random reciprocal matrices. For the Ma-Zheng scale we used 1000 reciprocal matrices to calculate the RIs in Table 3.

Next, the consistency ratio (CR) is computed by:

$$
C R = \frac {C I}{R I}\tag{4}
$$

Finally, to assess the logical consistency of the reciprocal matrices, CR should be less than 10% for reciprocal matrices with size nN4; less than 8% for (4,4) matrices and less than 5% for (3,3) matrices [31]. This concludes Phase 1 of the HAM algorithm.

In Phase 2, the contributions of alternatives to each criterion (step 4 of the HAM process, or step 1 of Phase 2) are again elicited from the decision makers. For each 1≤i≤na and 1≤j≤nc the matrix element $a _ { i j }$ of the decision matrix a is determined in Table 2.

Table 3  
Random Index (RI) values for the Ma-Zheng scale and for Saaty's scale.

<table><tr><td>Number of criteria</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>HAM RI for HAM (Ma-Zheng scale)</td><td>0</td><td>0.3416</td><td>0.5508</td><td>0.7008</td><td>0.7962</td></tr><tr><td>AHP RI (Saaty&#x27; scale) [28]</td><td></td><td>0.58</td><td>0.9</td><td>1.12</td><td>1.24</td></tr></table>

The aggregation method to determine the prioritization of alternatives in the <sup>fi</sup>fth step of the HAM process, is again the calculation of the geometric means but using the obtained normalized priority vector of Phase 1 for its weights, such as:

$$
r _ {i} = \prod_ {1} ^ {n} a _ {i j} ^ {n w _ {j}}\tag{5}
$$

Then the obtained r vector is normalised, giving the rated alternatives:

$$
R a t e \_ A l t _ {i} = \frac {r _ {i}}{\sum r _ {i}}\tag{6}
$$

The decreasing ordered alternatives show the <sup>fi</sup>nal ranking, where the best decision alternative is the one with the highest Rate\_Alt value.

## 5. Illustrative example

This section presents an illustrative example for selecting an architectural style in software engineering development. For the example we consider four criteria and three alternatives. The criteria are: usability, performance, security and modularity. The candidate architectural styles (alternatives) are: MVC, Backboard and Client-Server. Since this is an example, the elicited values for the matrices (Phase 1 and Phase 2), are just illustrative and do not represent opinions of the software engineers. In the implemented tool the user dialog is done with the simpli<sup>fi</sup>ed interface scale, presented in Table 2, but behind the scenes the calculations are performed using the Ma-Zheng scale. From the user perspective (HAM interface scale) the illustrative example is summarized in Table 4.

Note that in Phase 1 the user only needs to provide the values for the cells above the diagonal line. The diagonal is <sup>fi</sup>lled with zeros (by default) and HAM automatically adds the values below the diagonal. In Phase 2 the user is required to classify each alternative regarding each criterion using the HAM interface scale.

The following subsection presents the results obtained with the computational model proposed for HAM (Section 4), which, as mentioned before, uses the Ma-Zheng scale and the geometric mean as the aggregation operator for both phases of HAM. The second subsection compares the results with an approach using the weighted average in both phases. The third sub-section compares the results of using HAM selected scale with the same problem using the AHP scale. In these sub-sections we will show the illustrative example already with the appropriate calculation scales (either the selected HAM scale or the AHP scale), according to Table 2.

Illustrative example with Ham interface scale.

<table><tr><td></td><td>Usability</td><td>Performance</td><td>Security</td><td>Modularity</td></tr><tr><td colspan="5">Phase 1</td></tr><tr><td>Usability</td><td>0</td><td>-5</td><td>-6</td><td>-2</td></tr><tr><td>Performance</td><td>5</td><td>0</td><td>1</td><td>6</td></tr><tr><td>Security</td><td>6</td><td>-1</td><td>0</td><td>5</td></tr><tr><td>Modularity</td><td>2</td><td>-6</td><td>-5</td><td>0</td></tr><tr><td colspan="5">Phase 2</td></tr><tr><td>MVC</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Blackboard</td><td>-6</td><td>-4</td><td>4</td><td>6</td></tr><tr><td>Client-Server</td><td>4</td><td>3</td><td>6</td><td>1</td></tr></table>

Table 5  
Phase 1: Example for HAM scale and geometric prioritization.

<table><tr><td></td><td>Usability</td><td>Performance</td><td>Security</td><td>Modularity</td></tr><tr><td>Usability</td><td>1</td><td>4/9</td><td>3/9</td><td>7/9</td></tr><tr><td>Performance</td><td>9/4</td><td>1</td><td>9/8</td><td>9/3</td></tr><tr><td>Security</td><td>9/3</td><td>8/9</td><td>1</td><td>9/4</td></tr><tr><td>Modularity</td><td>9/7</td><td>3/9</td><td>4/9</td><td>1</td></tr></table>

For calculating the consistency index CR, we used the HAM RI from Table 3 for nc=4, i.e., RI=0.5508; for the comparison with AHP we used RI= 0.9 (Table 3).

## 5.1. HAM approach

Phase 1. Pairwise comparison to determine criteria weights (importance).

After eliciting the pairwise contributions (just for the values above the diagonal) HAM <sup>fi</sup>lls the pairwise matrix with their reciprocals. Then we are able to calculate the weights (Eq. (1)), normalized weights (Eq. (2)), and the consistency (Eqs. (3) and (4)), as shown in Table 5. This phase uses a pairwise matrix to automatically obtain the weights for each criterion (quality attribute).

The left matrix represents the pairwise matrix using the Ma-Zheng scale, selected for HAM. On the right side we have the calculations for W (Eq. (1)) and also for NW (Eq. (2)). The last column, on the right side, depicts the calculations for λ (Eq. 3), which amounts to the multiplication of the pairwise matrix with the NW vector and then the division of each obtained vector value by the respective NW vector value. Details of these calculations for λ can be found in [16].

As can be observed, the logical consistency is ensured since CRb8%, which is the recommended value for small matrices [31].

## Phase 2. Decision process to determine alternative ratings

In this phase, again, after eliciting the contributions of each alternative for each criterion (shown in Table 4), we calculate the ratings (Eq. (5)) and the normalized ratings (Eq. (6)) for each alternative, using the HAM selected scale for the calculations (Table 3). This phase uses a classical decision matrix, where lines depict alternatives and columns depict criteria, and the prioritization operator is also the geometric mean (see Table 6).

The best candidate is the software architecture Client–Server with a rating of 40.432%, followed by MVC with 38.781%. The worst choice is clearly Blackboard with only 20.787%. In such a situation, and depending on the problem being developed, we could use a simple Client–Server architecture style, or use a combination of Client–Server and MVC, where MVC could be used on the server side, for example.

<table><tr><td colspan="4">Geometric</td></tr><tr><td>W</td><td>NW</td><td rowspan="5"></td><td>λ</td></tr><tr><td>0.583</td><td>0.130</td><td>4.044</td></tr><tr><td>1.660</td><td>0.372</td><td>4.044</td></tr><tr><td>1.565</td><td>0.350</td><td>4.009</td></tr><tr><td>0.661</td><td>0.148</td><td>4.024</td></tr><tr><td rowspan="2">4.468</td><td rowspan="2">1.000</td><td>CI =</td><td>0.010</td></tr><tr><td>CR =</td><td>1.84%</td></tr></table>

5.2. Comparison of geometric means versus arithmetic means as prioritization operators

In this section we also use the Ma-Zheng scale, but instead of the geometric means prioritization operator we use the simple weighted average for the calculations, both for Phase 1 [3,31] and Phase 2 [13,33,36]. The results obtained are depicted in Table 7.

As can be observed, the ranking of the alternative architectures (1st – Client–Server, 2nd – MVC, 3rd – Blackboard) is the same as the one obtained with the geometric approach, as should be expected for such a small illustrative example and considering we are using the same geometric scale. However, visible differences can be spotted in the respective rating values:

• geometric: 40.432, 38.781, 20.787

• arithmetic 39.944, 35.719, 24.337

## 5.2.1. Phase 1

The importance for criteria (i.e., requirements) in Table 7 shows that the most important requirement is “performance” followed by “security” (respectively 0.366 and 0.355 in column NW). Now, comparing these values with Table 5, column NW, geometric approach, we detect a bigger difference between the two criteria (0.372 and 0.35), clearly showing that the geometric approach is more discriminative. However, when the comparison values are low (e.g., usability compared with modularity has a medium low importance=7/9) then the arithmetic approach discriminates more 0.127 versus 0.152 in Table 4, column NW), which is against what we want, i.e., to be more discriminative for high values and less discriminative for lower values. In addition, notice that the values for the consistency index CI vary, and that the logical consistency of the geometric approach is better, since it presents a lower value (1.84% versus 1.96%).

## 5.2.2. Phase 2

Similarly, the same logic is observed in the ratings of the two best alternatives (Client–Server and MVC). However, in this phase, the geometric approach clearly distinguishes when an alternative is rather bad (Blackboard obtains 20.787% and 24.337%, respectively in the geometric versus arithmetic approach). Another interesting point is that in the geometric approach there is not so much distinction between the MVC and the Client–Server architectures, which allows (as it should be) the software engineer to consider their rating, instead of just discarding the MVC architectural style (as it was suggested by the big difference of results given by the arithmetic approach).

Table 6  
Phase 2: Example for HAM.

<table><tr><td rowspan="2">Weights</td><td>0.1337</td><td>0.3467</td><td>0.3474</td><td>0.1723</td><td colspan="2">Geometric</td></tr><tr><td>Usability</td><td>Performance</td><td>Security</td><td>Modularity</td><td>Ratings</td><td>Rate-Alt (%)</td></tr><tr><td>MVC</td><td>9/5</td><td>9/5</td><td>9/5</td><td>9/5</td><td>1.800</td><td>38.781</td></tr><tr><td>Blackboard</td><td>3/9</td><td>5/9</td><td>9/5</td><td>9/3</td><td>0.965</td><td>20.787</td></tr><tr><td>Client-Server</td><td>9/5</td><td>9/6</td><td>9/3</td><td>9/8</td><td>1.877</td><td>40.432</td></tr><tr><td>Total=</td><td></td><td></td><td></td><td></td><td>4.687</td><td></td></tr></table>

Table 7  
Example with HAM scale and weighted average prioritization in both phases.  
Phase 1: Pairwise comparison to determine criteria weights

<table><tr><td colspan="5">Arithmetic</td></tr><tr><td></td><td>Weights</td><td>NW</td><td rowspan="5"></td><td>Consistency</td></tr><tr><td>Usability</td><td>0.639</td><td>0.127</td><td>4.146</td></tr><tr><td>Performance</td><td>1.844</td><td>0.366</td><td>4.115</td></tr><tr><td>Security</td><td>1.785</td><td>0.355</td><td>3.958</td></tr><tr><td>Modularity</td><td>0.766</td><td>0.152</td><td>3.911</td></tr><tr><td>Total</td><td>5.033</td><td>1.000</td><td colspan="2">CI = 0.011CR = 1.96%</td></tr></table>

In summary, we can say that the geometric operator offers more balanced results for higher values and more discriminative results for lower values. The logic is that if an alternative is clearly bad it should be immediately discarded (case of the blackboard architectural style), but, if it has some potential, it should be further analyzed by the software developers (case of Client–Server versus MVC). In the latter case, the decision maker can use the <sup>fl</sup>exibility offered by HAM and perform a “what-if” analysis to assess which of the two candidates is better, Client–Server or MVC. Of course, this would not rule out the hypotheses of making a combination between two or more architectural styles, but if a trade-off was necessary, the developer has a more clear distinction between the importance of each architectural style. This obliges him/her to think twice about the path to take, making adhoc decisions harder to justify. So, once more, what-if analysis gives him the <sup>fl</sup>exibility to try different combinations of quality attributes, adding some, removing others, or changing their importance-values, until a consensus is reached among stakeholders. On the other hand, if the developers do not want to perform further analysis, they can always decide in favour of the “best” classi<sup>fi</sup>ed by HAM, which was the Client–Server alternative.

## 5.3. Comparison with the AHP scale

This section compares the same illustrative example but using the AHP scale (see Table 2) and, as prioritization method, the weighted average, which is a simpler equivalent version of the eigenvector approach [3,30].

Phase 2: Decision process to determine alternatives ratings with weighted average

<table><tr><td colspan="3">Arithmetic</td></tr><tr><td></td><td>Ratings</td><td>Rate–Alt (%)</td></tr><tr><td>MVC</td><td>1.800</td><td>35.719%</td></tr><tr><td>Blackboard</td><td>1.226</td><td>24.337%</td></tr><tr><td>Client–Server</td><td>2.013</td><td>39.944%</td></tr></table>

The results obtained for Phase 1 (determination of weights for the quality attributes) using the AHP scale are illustrated in Table 8. These results demonstrate clearly the superiority of the HAM scale as the consistency index (CR) is now above the logical threshold of 8% (8.543%) (recommended for small matrices by Saaty [31]) Therefore, using AHP scale can distort results that are cognitively consistent and logical because of its lack of discrimination power, which may cause an almost random behaviour. (The scale appropriateness was discussed in Section 4.1.)

Regarding Phase 2 (results in Table 9) another interesting point to observe is that this same lack of discriminative power when using the AHP scale re<sup>fl</sup>ects on the <sup>fi</sup>nal ranking since now the “best” alternative is the MVC followed closely by Client Server. Clearly the AHP scale is also good for discriminating “bad” alternatives (where its behaviour is closer to the Ma-Zheng scale, used by HAM) but for good alternatives it can have unexpected behaviours as it only follows a linear averaging logic.

Note that the lack of consistency in the AHP scale is clearly visible in this small illustrative example and for our purposes, to support software engineering decisions, it is rather inferior to the scale and prioritization method selected for the HAM method and tool.

## 6. Tool support

This section describes the preliminary prototype tool that was developed for the HAM method. The tool's main window is displayed in Fig. 4. The example shown therein considers four criteria (stakeholders of the software system: company, user, administration, architect) and four alternative requirements to be assessed: safety, portability, extensibility, usability and interoperability. This example

## Table 8

Phase 1: Example with HAM scale and weighted average prioritization.  
Phase I–equivalent AHP scale values (Table 2)

<table><tr><td></td><td>Usability</td><td>Performance</td><td>Security</td><td>Modularity</td></tr><tr><td>Usability</td><td>1.00</td><td>0.17</td><td>0.14</td><td>0.33</td></tr><tr><td>Performance</td><td>6.00</td><td>1.00</td><td>2.00</td><td>7.00</td></tr><tr><td>Security</td><td>7.00</td><td>0.50</td><td>1.00</td><td>6.00</td></tr><tr><td>Modularity</td><td>3.00</td><td>0.14</td><td>0.17</td><td>1.00</td></tr><tr><td>Total</td><td>17.00</td><td>1.81</td><td>3.31</td><td>14.33</td></tr></table>

Phase I–AHP results for quality attributes weights

<table><tr><td>NW</td><td rowspan="5" colspan="2"></td><td>Consistency</td></tr><tr><td>0.054</td><td>4.034</td></tr><tr><td>0.500</td><td>4.378</td></tr><tr><td>0.352</td><td>4.388</td></tr><tr><td>0.094</td><td>4.122</td></tr><tr><td rowspan="2" colspan="2"></td><td>CI =</td><td>0.077</td></tr><tr><td>CR =</td><td>8.543%</td></tr></table>

Table 9  
Phase 2: Example with HAM scale and weighted average prioritization.

<table><tr><td rowspan="2">Weights</td><td>0.054</td><td>0.500</td><td>0.352</td><td>0.094</td><td colspan="2">Arithmetic</td></tr><tr><td>Usability</td><td>Performance</td><td>Security</td><td>Modularity</td><td>Ratings</td><td>(%)</td></tr><tr><td>MVC</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.000</td><td>40.469%</td></tr><tr><td>Blackboard</td><td>0.14</td><td>0.20</td><td>5.00</td><td>6.00</td><td>2.432</td><td>19.683%</td></tr><tr><td>Client-Server</td><td>5.00</td><td>4.00</td><td>7.00</td><td>2.00</td><td>4.923</td><td>39.848%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>12.355</td><td>1.000</td></tr></table>

![](/api/attachments/5VMGTXUT/fulltext/images/5ea1f442b011c5d46b0cbadecfefc2ad89f560788c1f78feb7b48e9375be07ff.jpg)  
Fig. 4. HAM Tool main window.

was used to show the potential of HAM to also support decisions about priorities for implementing requirements, taking into consideration preferences and importance of the involved stakeholders.

Considering the top-half of the window, we can observe, on the left-hand side, a tree-like structure with the goal of the assessment and the selected criteria and alternatives. In the middle there is the pairwise comparison matrix. This is where the tradeoffs between the criteria will be done. We just need to <sup>fi</sup>ll the right-upper side of the pairwise matrix (using the interface scale of Table 2). The lowerleft cells will be <sup>fi</sup>lled automatically. The tool processes all calculations using Ma-Zheng's scale, as discussed in previous sections. On the right-hand side is a vector that will display the calculated weights of the criteria (normalized). If the criteria weights are inconsistent, a message pops-up warning the user. Under the pairwise matrix we can see a combo box with the Assign Value. This component is used to assign values to the pairwise matrix cells using Table 2 interface scale. In the bottom-half of the window, we can see a short scale help, so that the user has quick access to the scale. To <sup>fi</sup>ll both decision matrices we can use the mentioned combo box or use the keyboard. Finally, on the right-hand side the rating vectors are shown, where the ratings of the criteria (top) and the alternatives (bottom) are displayed. The ratings are displayed in absolute percentage.

When <sup>fi</sup>nished <sup>fi</sup>lling the pairwise matrix, we press the “Calculate Weights” button. You can view the criteria normalized weights (i.e., priority vector) in the weights vector. As explained in Section 2, if the consistency ratio is greater than 8% (for matrices of 4\*4 or lower) and for greater ones N10%, the user is prompted with an error message and adjustments must be done in the pairwise comparison matrix to ensure the comparisons are logical. When performing any what-if analysis the user can also edit the pairwise matrix by doing “Edit→Matrix to <sup>fi</sup>ll→Pairwise Matrix” and press the “Calculate Weights” button. To go back to editing the decision matrix, just do “Edit→Matrix to <sup>fi</sup>ll →Decision Matrix”.

Once Phase 1 is <sup>fi</sup>nished, pressing the “Calculate Ratings” button will provide the importance/weights for criteria. The criteria ratings are displayed as a weight vector, as shown on top right of Fig. 4.

These partial results can also be saved by pressing the “Save…” button, or going to “File→Save…”, which will open a save dialog box. Just select the location where you want to save the project and the name of the <sup>fi</sup>le. This will create a new Microsoft Excel <sup>fi</sup>le with the name you provided, or a new sheet in the <sup>fi</sup>le if it exists.

The tool also allows the addition of new criteria, for example a new Stakeholder, or new alternatives, for example a new NFR, to the existing analysis. For instance, to add a new criterion just do “Edit→Add new criterion”. A new window opens and you can enter the name of the Stakeholder you want to add. This allows what-if analysis.

The process for Phase 2 is somewhat similar, with the difference that there are no pairwise comparisons and the values elicited are direct judgements of users regarding each criterion for each alternative. This matrix must be completely <sup>fi</sup>lled by a decision maker or domain specialist, e.g. a software engineer. After <sup>fi</sup>lling this decision matrix the user must press the “Calculate Ratings” button and the <sup>fi</sup>nal rating per alternative is displayed in the ratings vector (bottom right).

The tool was developed in Java 1.6 [31] using Eclipse IDE 3.4.1 [12] to implement the HAM algorithm and NetBeans IDE 6.5 [25] to develop the Graphical User Interface.

## 7. HAM discussion

Note that the normalizations of w and r are not strictly necessary. They are performed since normalised vectors are easier to understand, particularly in the common percentage scale. Note also that the columns of the pairwise decision matrix are not normalized, as they are in the AHP method. This is because the values of the decision matrix are dimensionless quantities. As a consequence, HAM can use the weighted geometric method without suffering from the anomalies of the AHP method, where, for instance, when an alternative is added, the ordering of the other alternatives may change. Moreover, the consideration of the same scale and the geometric mean, in both phases of HAM, provides consistency, <sup>fl</sup>exibility and robustness for the proposed approach, as explained in Section 4.

By using the geometric mean and avoiding the problematic Saaty's scale we managed to achieve a smoother behaviour for the decision maker judgments and the user-friendlier interface scale used in the HAM tool offers a more transparent usage. Also, by using a twophase approach, we are able to automatically calculate the weights for the criteria, to perform trade-offs in both phases and to avoid the extra time needed for the complete Saaty's approach. We simpli<sup>fi</sup>ed the user interaction by displaying a user-friendly interface scale to facilitate novice users to elicit judgements about relative importance of criteria.

In summary, HAM's method's main characteristics are:

a. From comparative methods, HAM uses just one pairwise comparison matrix to perform the trade-off analysis between criteria and obtain their relative importance (or weights), while ensuring logical consistency.

b. From scoring methods, HAM uses the decision matrix logic of WA with weights obtained from the AHP pairwise comparisons to determine the <sup>fi</sup>nal ratings and ranking for the alternatives.

c. Since the AHP scale and prioritization method suffer from some <sup>fl</sup>aws, such as its linear scale and prioritization operator [10,17], we included Ma-Zheng's scale [20] and the geometric means as ranking/prioritization method, as suggested in [17].

d. To ensure consistency and uniformity in HAM, we also used the Ma-Zheng scale and the geometric means in the second phase for determining the <sup>fi</sup>nal ranking.

As any other MCDM method, HAM has advantages and drawbacks, particularly for supporting software engineering decisions. HAM's advantages are:

• It is a consistent, robust and <sup>fl</sup>exible method.

• It allows trade-offs between criteria importance (e.g., NFRs) resulting in the automatic determination of their relative importance (weights).

• It provides sound ratings of alternatives (e.g., architectural choices) by using both a scale and an aggregation operator, scienti<sup>fi</sup>cally proven as superior to the base constituting methods of HAM.

• It provides a user-friendly interface, enriched by using a simple interface scale as the dialog media with the users.

• It enables the addition of new criteria and/or alternatives at any time, obviously at the expense of having to perform new calculations.

• By combining a scoring method with a comparative method (Fig. 1) we avoid the time-consuming problems of comparative methods and pro<sup>fi</sup>t from having trade-offs for criteria weights importance.

• It allows consistent what-if analysis (e.g., what happens if we add a new requirement to the system, or if we change the values of importance or contribution? Will this change the suggested architecture?).

## And the drawbacks of HAM are:

• As any other MCDM method, judgments made by experts (assigned values) always include judgments and HAM only ensures logical consistency for pairwise judgments (comparative method phase).

• As any other MCDM method, it is a decision support model and not a decision making model, not substituting decision makers, and only supporting them to make educated decisions.

• It does not support group decision making (consensus about contribution values for each criteria must be done outside the method).

• Of course, when we are dealing with speci<sup>fi</sup>c problems, such as software engineering decisions, HAM requires technical knowledge about the context domain for providing judgements for relative importance of criteria, as well as to provide evaluations for the alternatives.

## 8. Concluding remarks

Our goal was to de<sup>fi</sup>ne a multi-criteria method to assist software engineers in their decisions through the early stages of the software development life cycle. We studied several classical multi-criteria methods, and concluded that none of them fully satis<sup>fi</sup>ed our needs, in particular in terms of ef<sup>fi</sup>ciency, pairwise comparisons, compensatory behaviour and usability. During this study, we revisited the <sup>fl</sup>aws regarding scale and aggregation method in the mathematical background of the two most promising methods to use (from the classes of scoring and comparative methods). To address these de<sup>fi</sup>ciencies, the Hybrid Assessment Method (HAM) was proposed

HAM is a hybrid method as it combines a comparison method with a scoring method: it uses only one pairwise comparison decision matrix and combines it with one classical weighted decision matrix. It uses a geometric scale and the geometric mean for determining the priority ratings. Moreover, it can be applied to different types of problems, even though here our motivation was to support software engineering decisions.

Until recently, the importance played by system qualities in software development was dubious. That is, everyone knew and knows how important they are; but treating their in<sup>fl</sup>uence on each other as well as their impact on the developed software was still a cumbersome and informal process. Most often, each quality was added to the code, without a clear view of the in<sup>fl</sup>uence such new scattered code (as usually a system quality has an impact on several modules of the system) really had on the <sup>fi</sup>nal software. And the more qualities are handled in this fashion, the more likely it is to increase severely the maintenance dif<sup>fi</sup>culties and evolution complexity. Therefore, being able to study each quality independently <sup>fi</sup>rst and then their impact on each other and on other modules of the system is a great step forward on modularization and, consequently, on software maintenance and evolution. HAM offers support for this type of study.

Indeed, HAM supports the identi<sup>fi</sup>cation the stakeholders' goals, these corresponding to system qualities, and is able to rank these qualities taking into consideration the stakeholders preferences. Software developers, in particular software architects, can then consider these qualities as the main driver to design the system's software architecture. But HAM also addresses questions related with identi-<sup>fi</sup>cation or selection of new sellable components or products supporting decision makers in identifying new business opportunities with less risks and costs. Finally, HAM gives developers the <sup>fl</sup>exibility to play with different choices and understand their impact on the ranking and, consequently, on the <sup>fi</sup>nal decisions they have to make.

Moreover, HAM offers the above functionalities always ensuring consistency, ef<sup>fi</sup>ciency, pairwise comparisons (criteria trade-offs). Moreover, it guarantees logical consistency, provides automatic calculation of criteria weights and its reasoning process is reasonably straightforward. The prototype-supporting tool we developed is a proof-of-concept and validation or our claims. We believe HAM is a consistent, robust and <sup>fl</sup>exible method, particularly when compared with other existing ones. As future work we will continue improving the tool to generalize its usage for any decision-making domain.

To conclude, we will now address HAM's suitability and appropriateness for software engineering decision support. HAM provides a systematic rigorous method to support software engineers' decisions when dif<sup>fi</sup>cult alternative choices come into play. Therefore, HAM aims identifying the stakeholders' preferences and goals (the latter refer to system qualities) on what the system should do. To accomplish this, HAM allows us to rank system qualities taking into consideration the stakeholders' importance. If some of these qualities contribute negatively to each other [8], as the example given in Section 2 for response time and security, then we can identify that earlier in the software development process. Moreover, since system qualities are the main software architecture drivers, having a ranking of the qualities according to the stakeholders' wishes, and knowing which of those qualities are in con<sup>fl</sup>ict, is very valuable information to design the <sup>fi</sup>rst draft of the software architecture. But HAM offers other useful utilities for software engineers and enterprise managers. For example, suppose that a company wants to launch in the market a range of new products. HAM can help the company manager to decide which product may be wanted in the market, and therefore deploy an economic version <sup>fi</sup>rst and only then decide on deploying more sophisticated versions. Another useful functionality of the method (and its supporting tool) is to arm decision makers with the <sup>fl</sup>exibility to play with different choices and understand their impact on the ranking and, consequently, on the <sup>fi</sup>nal decisions they have to make.

## Acknowledgements

We would like to express our gratitude to João Araújo, Catarina Gomes, António Costa and João Santos who provided contributions for the preliminary version of HAM. This work has been partially supported by the European Commission grant IST-33710 – Aspect-Oriented, Model-Driven Product Line Engineering (AMPLE).

[32] B. Srdjevic, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (4) (2007) 2261–2273.

[31] T.L. Saaty, Decision Making for Leaders, University of Pittsburgh, 1986.

[34] Y.-M. Wang, T.M.S. Elhag, An approach to avoiding rank reversal in AHP, Decision Support Systems 42 (2006) 1474–1480.

[33] E. Triantaphyllou, Multiple Criteria Decision Making Methods: a Comparative Study, Kluwer Academic Publishers, 2000

[22] J. McCaffrey, Multi-attribute global inference of quality (MAGIQ), Software Test and Performance Magazine 2 (7) (2005) 28–32.

[10] P. Clements, R. Kazman, M. Klein, Evaluating Software Architectures: Methods and Case Studies, Addison Wesley, 2002

[23] N.R. Mead, Requirements Prioritization Case Study Using AHP, https://buildsecurityin.uscert.gov/daisy/bsi/articles/bestpractices/requirements/534.html? branch=1&language=1.

[9] P. Clements, L. Northrop, Software Product Lines: Practices and Patterns, Addison-Wesley, 2002.

## References

[8] L. Chung, B.A. Nixon, E. Yu, J. Mylopoulos, Non-Functional Requirements in Software Engineering, Kluwer Academic Publishing, 1999.

[1] N. Ahmad, P.A. Laplante, Software project management tools: making a practical decision using AHP, In Proceedings of the 30th Annual IEEE/NASA Software Engineering Workshop SEW-30 (SEW'06), 2006.

[24] A. Moreira, A. Rashid, J. Araújo, Multidimensional Separation of Concerns. Requirements Engineering, 2005.

[30] T.L. Saaty, The Analytical Hierarchy Process, Network: McGraw-Hill, 1980.

[7] S. Chen, L. Hwang, Fuzzy Multiple Attribute Decision Making - Methods And Applications, Springer-Verlag, 1992.

[11] Y. Dong, Y. Xu, H. Li, M. Dai, A comparative study of the numerical scales and the prioritization methods in AHP, European Journal of Operational Research 186 (2008) 229–242.

[26] T.C. Pais, R.A. Ribeiro, L.F. Simões, DaRuan, Uncertainty in dynamically changing input data, Computational Intelligence in Complex Decision System, World Scienti<sup>fi</sup>c, 2009.

[2] AMPLE, http://www.ample-project.net 2009.

[3] D.R. Anderson, D.J. Sweeny, T.A. Williams, Quantitative Methods for Business, South-Western College publishing Co., 2003.

[28] T.L. Saaty, L.G. Vargas, Prediction, Projection and Forecasting in Applications of the Analytical Hierarchy Process in Economics, Finance, Politics, Games and Sports, Kluwer Academic Publishers, Boston, 1991.

[5] J. Barzilai, W. Cook, B. Golany, consistent weights for judgements matrices of the relative importance of alternatives, Operations Research Letters 6 (3) (1987).

[35] R. Wieringa, N. Maiden, N. Mead, C. Rolland, Requirements engineering paper classi<sup>fi</sup>cation and evaluation criteria: a proposal and a discussion, Requirements Engineering 11 (1) (2006) 102–107.

[4] Perini Anna, Ricca Filippo, Susi Angelo, Tool-supported requirements prioritization. Comparing the AHP and CBRank methods, Information and Software Technology 51 (2009) 1021–1032.

[6] I.S. Brito, F. Vieira, A. Moreira, R.A. Ribeiro, Handling conflicts in aspectual requirements compositions. Lecture Notes in Computer Science (LNCS), Transactions on Aspect-Oriented Software Development III, 4620, 2007, pp. 144–166; M. Lindvall, R.T. Tvedt, P. Costa, An empirically-based process for software architecture evaluation, Empirical Software Engineering, 8, Springer, 2003, pp. 83–108.

[27] A. Pimentel, Multi-criteria analysis for architectural choices in software product lines, Master's Dissertation in Computer Science, 20098, Universidade Nova Lisboa.

[14] S.I. Gass, Decision Making, Models AND Algorithms: a First Course, Wiley, 1985.

[29] T.L. Saaty, Fundamentals of the Analytic Hierarchy Process. RWS Publications, 4922 Ellsworth Avenue, Pittsburgh, PA 15413, , 2000.

[13] J. Figueira, S. Greco, M. Ehrgott, Multiple criteria decision analysis: state of the art surveys, International Series in Operations Research & Management Science 78 (2005)8 Springer.

[12] Eclipse, http://www.eclipse.org/.

[25] NetBeans, www.netbeans.org.

[15] B. Golden, E. Wasil, P. Harker, The Analytic Hierarchy Process: Applications and Studies, Springer, Berlin, 1989.

[16] C. Gomes, R.A. Ribeiro, A. Pimentel, SWDSS – an experience in transforming a single system into a software product line, Proceedings of the 4th Iberian Conference on Information Systems and Technologies, Povoa de Varzim PORTUGAL, 2009 pp. 161–1668, June.

[17] Java Sun, http://java.sun.com/javase/6/docs/api/.

[20] D. Ma, X. Zheng, 9/9-9/1 Scale Method of AHP, 2nd International Symposium on the AHP, Pittsburgh, PA, USA, 1991, pp. 197–202.

[18] Y. Lee, K. Kozar, Investigating the effect of website quality on ebusiness success: an analytic hierarchy process (AHP) approach, Decision Support Systems 42 (3) (2006) 1383–1401.

[19] M. Lindvall, R.T. Tvedt, P. Costa, An empirically-based process for software architecture evaluation, Empirical Software Engineering 8 (2003) 83–1088 Springer.

[21] N.A.M. Maiden, P. Pavan, A. Gizikis, H. Kim, O. Clause, X. Zhu, Integrating decisionmaking techniques into requirements engineering, Proceedings of Eighth International Workshop on Requirements Engineering: Foundation for Software Ouality Colocated with RE'02 Conference, Essen Germany, 2002

[36] K. Yoon, C. Hwang, Multiple Attribute Decision Making—an Introduction, A SAGE University Paper, 1995

![](/api/attachments/5VMGTXUT/fulltext/images/4361aac2bc3c9b4612395ecfae12c08a034409e481c96298d1169c61c3680e65.jpg)

Rita A. Ribeiro obtained her B.A. (5 years degree) in Management & Business Administration from ISEG (PT) in 1981. She received her M.Sc. in Information Systems technology from George Washington University (USA) in 1988 and her PhD in Arti<sup>fi</sup>cial Intelligence from the University of Bristol (UK) in 1993. Since 2002 she is the head of the research group on Computational Intelligence (CI) at UNINOVA (www.uninova.pt/ca3), which focus on CI in Space related applications. She started her academic career in 1984 and is now an invited associate professor at Universidade Nova Lisboa and a senior researcher at Uninova. She has been involved in several national and international research projects, from which the European

Space Agency (ESA) <sup>fi</sup>nanced 14 projects. She published more than 100 scienti<sup>fi</sup>c papers mainly in the topics of fuzzy multicriteria decision making, fuzzy optimization, fuzzy knowledge-based systems and applied decision support systems

![](/api/attachments/5VMGTXUT/fulltext/images/eaf811810ef142a0570b2d3b36b6f9cec89c8604382cdc2004426077816ff96b.jpg)

Ana Moreira is an Associate Professor at Universidad Nova de Lisboa, where s obtained her BSc (5 years degree) in Computer Science 1987 and her MSc in Software Engineering in 1991. She received her PhD in Computer Science from University of Stirling (UK) in 1994. She leads the Software Engineering group at Universidade Nova de Lisboa since 2006. Her main research topics are aspectoriented software engineering, software architecture and design, model-driven development, software product lines and trade-off analysis. She is a member of the editorial board of the journals “Transactions on AOSD” and “Software and Systems Modeling” and also a member of the Steering Committee for MODELS and AOSD. She is cofounder of two international movements: Early Aspects (www.early-aspect.net) and pUML (preciseUML, www.cs.york.ac.uk/puml/). More information can be found at http: //www-ctp.di.fct.unl.pt/\~amm/.

![](/api/attachments/5VMGTXUT/fulltext/images/57f91a9ec44b3c79529d3a43c4c51f9bc6bf7ec7ff4c8a74100e8338bb59a5a7.jpg)

Pim van den Broek obtained his M.Sc in Theoretical Physics from the University of Groningen, the Netherlands, in 1974. He received his PhD in Theoretical Physics from the University of Nijmegen, the Netherlands in 1979. From 1984 he is a staff member of the University of Twente the Netherlands, in the chair Software Engineering. His main research interests are Application of Soft Computing to Software Engineering, Computational Techniques in Fuzzy Logic and Speci<sup>fi</sup>cation Techniques of Software Product Lines.

![](/api/attachments/5VMGTXUT/fulltext/images/62deec46f617a25b8dea09ffbfcf61caf255e18f2ba7c20fec03373e26f707a6.jpg)

Afonso Pimentel obtained his BSc in Computer Science in 2007 at Universidade Nova de Lisboa. He obtained his MSc in 2009 also at Universidade Nova de Lisboa. He was a Research Engineer for Universidade Nova de Lisboa from 2008 to 2009. His main research interests are software architectures, software product lines, multicriteria analy sis. He is currently working as a consultant at Opensoft – Soluções Informáticas.
