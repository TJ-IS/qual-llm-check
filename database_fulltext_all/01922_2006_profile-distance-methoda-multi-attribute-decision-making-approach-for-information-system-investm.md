---
otero_id: 1922
otero_key: "ANEZNGRW"
title: "Profile distance method—a multi-attribute decision making approach for information system investments"
authors: "Edward W.N. Bernroider; Volker Stix"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Profile distance method—a multi-attribute decision making approach for information system investments

Edward W.N. Bernroider <sup>T</sup>, Volker Stix

Vienna University of Economics and Business Administration, Department of Information Business, Augasse 2-6, A 1090 Vienna, Austria Available online 10 May 2005

## Abstract

This article addresses the area of decision making for information systems (IS). We recognize the great demand for methods and techniques that can be of practical help by presenting a new, conceptual approach, the profile distance method, to support the IS selection problem. This approach combines the merits of two prominent concepts individually applied in decision making: the utility ranking method (URM) and the data envelopment analysis (DEA). In addition, the method involves calculating distances between the desired system profile defined in the additive multi-attribute utility model and the individual alternative profiles calculated by the DEA derived optimization process. The results can be visualized to support the decision maker in justifying and communicating the model outcomes. The proposed method is illustrated within a real-life case study concerning an enterprise resource planning (ERP) software selection problem. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Decision support; Information systems; Data envelopment analysis; Utility ranking method; Linear programming

## 1. Introduction

Information systems (IS) play a major role in developing and sustaining competitive advantage in the global marketplace [16,31]. IS can transform business and revolutionize the way business is conducted [6].

Literature reports extensively on diverse problems associated with IS evaluation [26]. Those problems can be derived from the difficulty of understanding the complex factors involved in IS decision making, such as scope and impact of the decision, the concept of value and its multi-dimensional facets, natures of IS benefits and costs, associated risks, strategy alignment, human and organizational mechanics or political issues.

The evaluation of IS investment proposals has been a recognized research area for a long time. Already in the 1960s, researchers began working on IS related evaluation issues [20,28]. Since then, IS evaluation has become one of the most researched and written about topics in IS research, resulting in a large number of evaluation techniques available today. Research exists helping to assess the wide spectrum of methodical aids through taxonomies [25], classifications [17,18], and surveys of methods [39]. Olson shows how major decision aids supporting selection problems work and concludes with a comparison of techniques with respect to practical implementation [32]. Despite these efforts, organizational studies have shown that in practice business management fails to appreciate the portfolio of investment appraisal techniques available. Many companies are justifying their IS expenditure on the basis of what could be called <sup>d</sup>acts of faith<sup>T</sup> [5]. Where formal evaluation takes place, it is predominantly based on conventional accountancy approaches such as methods implement ing discounted cash flow analysis [8]. The accountancy methods can be applied to any corporate investment proposal and are widely understood by senior managers, but do not accurately capture the benefits resulting from investments in IS [30]. More complex or IS-specific evaluation methods to capture the full consequences of an IS investment are seldom adopted by business managers. This situation further worsens in small to medium sized compared to large enterprises [8]. If a formal, non-financial technique for IS evaluation is chosen to support the IS investment appraisal, it is very likely a simple scoring and ranking technique [35]. These methods appeal to management due to their intuitive, simple and costeffective application. They are relatively transparent, allowing others to see the logic of the results and enabling the inclusion of the full range of intangible consequences. These criteria seem to be the key to application success of any methodical aid.

In this paper we propose a new, conceptual approach, named profile distance method, to support IS selection problems. By combining the basic concept of the popular utility scoring and ranking technique with data envelopment analysis (DEA), we recognize their appealing benefits while making up for a number of their limitations. The results can be visualized to support the decision maker in justifying and communicating the model outcomes. Because the method consists of solving a linear program (LP), it is easy to implement on any personal computer. Its underlying concepts are logically sound and comprehensible. We illustrate this with a real-world case on a prototype implementation, which refers to an enterprise resource planning (ERP) software selection.

The remainder of this article is structured as follows. First, we provide more information on the methodical background for the incorporated concepts. Next, we summarize the research issues. In Section 4, we develop the new approach and subsequently show its application. Finally, Section 6 concludes the results and sketches the on-going research.

## 2. Methodical background

## 2.1. Utility ranking method

Four basic approaches can be identified in the evaluation methods available: the financial, the ratio, the portfolio, and the multi-criteria approaches [34,36]. The method described in this article follows a multi-criteria, more precisely <sup>b</sup>multiple attribute decision making<sup>Q</sup> (MADM) approach, which in general is applicable to a wide range of human choices [42]. MADM refers to making preference decisions over a finite number of alternatives that are characterized by multiple, usually conflicting, attributes. In the field of IS evaluation the MADM approach <sup>d</sup>Information Economics<sup>T</sup> received considerable attention [33]. The model gives the decision makers the means to identify and assess a comprehensive set of evaluation attributes in the IS evaluation problem setting; therefore, it primarily assists in the important generation of attributes. Other more general frameworks provide assistance to identify places where important criteria, especially benefits, might be found, e.g., [19].

A MADM problem can be expressed by a matrix, where columns indicate the attributes considered and rows denote the competing alternatives. Each MADM problem needs to be solved by one of the numerous MADM methods available. It is essential for many compensatory MADM methods to obtain comparable scales by normalization of attribute ratings. Solving the MADM problem can imply the aggregation of utilities into an overall evaluation for each alternative leading to a final ranking. Zanakis et al. give simulation comparison of eight popular and widely used methods [43]. The most popular method to practitioners due to its simplicity is the additive weighting technique which uses utility functions with precise assignments concerning utilities and weights.

The overall suitability of each alternative is thereby calculated by averaging the score of each alternative with respect to every attribute with the corresponding importance weighting. In the remainder of this article, we will refer to a MADM approach based on additive multi-attribute decision making as a utility ranking method (URM). Known extensions to URM allow for imprecision concerning the inputs, follow-up sensitivity analysis or simulation, e.g., based on simultaneous changes of weights [13,27,37].

## 2.2. Data envelopment analysis

The original DEA model referred to as CCR-model proposed by Charnes, Cooper and Rhodes [14] maps a fractional linear measure of efficiency into a linear programming (LP) format. The efficiency measure defined by multiple inputs and outputs is used to assess different decision making units (DMUs) without the need to know their production function. This non-parametric approach optimizes an LP per DMU yielding weights with respect to the chosen inputs and outputs for every DMU. Consequently, the relative efficiency rating calculated by DEA in respect of a DMU is defined as the ratio of the sum of its weighted output levels to the sum of its weighted input levels. Through solving the LP each DMU is free to choose its optimal weights in order to make itself look best under the restriction that no other DMU, given the same weights, is more than 100% efficient. As a result, a Pareto frontier is attained, characterized by at least one 100% efficient DMU on the boundary envelop of the input–output variable space. For a complete introduction into DEA, see [15,40], and for an up to date scheme for classifying the DEA literature, we refer to [21].

Data envelopment analysis was originally used for assessing the relative efficiency of organizational DMUs such as universities [1], governmental organizations [12] or bank branches [11]. In the context of decision analysis, the use of DEA as a discrete alternative MADM technique has been gaining considerable attention in academic literature. DEA can be applied to rank decision making alternatives, to provide insights into specific strengths and weaknesses of alternatives, or to support group decisions by using an Assurance Region DEA model. The latter can take into account the various views of evaluators by including upper and lower bounds as the assurance region constraints for output weights in the underlying LP while assuming an input value of one for every alternative [15]. A case-based evaluation of various DEA ranking approaches and MADM techniques showed that DEA approaches seem to be advantageous since they require less information from decision makers and analysts for ranking alternatives [38]. Other adopters of DEA for decision making used the methodology to screen, respectively limit the number of alternatives, for further evaluation by other MADM techniques, e.g., for technology selection problems in the area of manufacturing [7,29]. Recent approaches analyzed the usage of DEA for IS evaluation and suggested its application in a real-life setting as an MADM technique [9].

The predominant situation found in IS decisions is characterized by a large set of attributes together with a small set of IS alternatives. Due to the nature of DEA–the freedom of each alternative to show his best representation by choosing an individual weighting scheme in the underlying LP–its application in terms of IS decisions results in high efficiencies with no or limited discrimination power. Suggestions to overcome these general DEA limitations are based on modifications of the LP constraints [4]. A new approach avoiding the constraint modification is based on introducing unobserved alternatives under certain assumptions [3]. Our approach solves the ranking issue by adding a penalty function to the DEA model.

## 3. Research issues

This paper develops a method combining the merits of the two prominent concepts presented in the previous sections, URM and DEA, by utilizing their compatibility in terms of MADM. Thereby, we seek to advance the state of the art by addressing the following limitations in IS decision making:

(1) The difficulty to assess, understand and compare the full spectrum of decision making attributes as a whole, i.e., the profiles of the alternatives under evaluation.

(2) The problem of identifying the selection criteria playing the decisive role for the IS selection.

(3) The problem of achieving a clear-cut ranking.

(4) The lack of simple, user-friendly and communicative techniques for dealing with complex decision settings hindering their acceptance by decision makers in practice.

(5) The problem of computationally complex procedures and, hence, the difficulties in implementation on computer systems.

In particular, by targeting these limitations the decision maker gains insights on the organizational fit for each IS alternative. The concept of organizational fit is a core research construct to explain implementation and usage success in diverse IT contexts [22,41]. In the context of IS, research further emphasizes that decision makers should assess the fit between their organization and the target system prior to its adoption, e.g., for ERP, see Ref. [23]. For ERP systems, taking this measure is regarded as critical especially for implementation success.

The proposed approach is characterized by a fully automated multi-phased procedure. It enables the decision to explore the overall suitability of an alternative in terms of distances based on attribute weights between an alternative and the desired profile. While the attribute weights are gained from calculating our model, a modified DEA-based optimization, the desired profile is defined by the pre-selected weights defined in URM. Intermediate and final results can be visualized to support the decision maker in justifying and communicating the model outcomes. As mentioned, the method involves calculating distances between the desired system profile and the individual alternative profiles. A related idea was proposed by Hwang and Yoon who developed the Technique for Order Preference by Similarity (TOP-SIS) based on the concept that the chosen alternative should have the shortest distance from the positiveideal solution and the longest distance from the negative-ideal solution [24,42]. In contrast to TOP-SIS, where a positive-, respectively, negative-ideal solution needs to be defined in terms of weighted, normalized attributes, we do not need any additional information besides the given URM specific utilities and weights.

The next section develops the new method. Our goal is to translate the basic idea of combining URM and DEA into a simple model that can be of practical help in IS decision making and to demonstrate its application in practice. In-depth methodological elaborations were widely avoided to improve readability and practicability.

## 4. Developing the new model

The original fractional model optimizes the weighted output per weighted input, where the weights are the variables. We start with the original CCR-DEA model as described in, e.g., [2], which translates the fractional program into an LP by adding constraint (3) keeping the denominator equal to 1. Here we have $n$ DMUs each with $m$ input attributes represented through the $m \times n$ matrix $X$ and s output attributes stored in the $s \times n$ matrix Y. The vectors v and u are the weight vectors for input and output attributes, respectively. We have for each DMU a different LP which can lead to a different optimal solution. The parameter k selects the DMU for which the optimization should be performed.

$$
h _ {k} = \max _ {u, v} \sum_ {r = 1} ^ {s} u _ {r} y _ {r k}\tag{1}
$$

subject to

$$
\sum_ {i = 1} ^ {m} v _ {i} x _ {i j} - \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} \geq 0 \quad \text { for   } j = 1, \dots , n\tag{2}
$$

$$
\sum_ {i = 1} ^ {m} v _ {i} x _ {i k} = 1\tag{3}
$$

$$
u _ {i}, v _ {j} \geq 0 \quad \text { for   all } i, j
$$

$$
4. 1. \text { Adding   a   penalty   function }
$$

By adding a penalty function to the objective (1) of the DEA model which measures the distance from a given desired weight profile, we incorporate the basic URM. Since for URM all inputs are implicitly treated to be one, we consider an output weight-profile only. Let w be a vector which defines this profile for each given output weight $o _ { i }$ relative to $o _ { 1 }$ . Thus, $w _ { 3 } { = } 2$ means that the weight assigned to attribute 3 should be 2 times larger than the weight for attribute 1. Consequently, $w _ { 1 }$ is always 1. Note that this profile w has to be expressed in relative figures, because multiplying all weights with a positive number would not change ranking (neither for URM nor for DEA). So we suggest

$$
h _ {k} = \max _ {u, v} \sum_ {r = 1} ^ {s} u _ {r} y _ {r k} - \alpha f (u, w)\tag{4}
$$

where f is the function measuring distance between the weight vector u and the desired profile w. a is a fade factor controlling the tradeoff between pure DEA (a=0) and pure URM $( \alpha \to _ { \infty } )$ . Hence, we allow the decision maker to change the model outcome by fading between both techniques, thereby exploring the organizational fit of the current alternative under evaluation.

## 4.2. Applying a linear optimization

We chose the sum of absolute distances as the distance measure f. Thus, $\begin{array} { r } { f ( u , w ) = \sum _ { r = 1 } ^ { s } | u _ { i } - w _ { i } u _ { 1 } | } \end{array}$ . It can be seen that the resulting problem cannot be expressed in a linear form. By calculating the optimization problem in two phases, we can, however, relax the equation system to an LP, which is easy to solve and accessible in almost every computer-aided working place.

In phase 1, we set a=0 and thus solve the original DEA problem (1). From that solution, we can extract the relative weight vector wˆ with $\hat { w } _ { i } = u _ { i } / u _ { 1 } , i =$ $1 , \ldots , s$ . Comparing wˆ with our desired profile w, we know for each attribute whether $\hat { w } _ { i } > w _ { i }$ or not.

In phase 2, we add for each $i = 1 , \ldots , s$ one additional constraint to (2), depending on the relation between $\hat { w } _ { i }$ and $w _ { i }$ as follows:

$$
\alpha d _ {i} (u _ {i} - w _ {i} u _ {1}) \geq 0\tag{5}
$$

with

$$
d _ {i} = \left\{ \begin{array}{c} 1, \hat {w} _ {i} > w _ {i} \\ - 1, \text { else } \end{array} \right.
$$

Note that a in Eq. (5) only ensures that the constraint is redundant whenever a=0 and thus leading to the traditional DEA. The following objective function is used in this new LP.

$$
h _ {k} = \max _ {u, v} \sum_ {r = 1} ^ {s} u _ {r} y _ {r k} - \alpha \sum_ {i = 1} ^ {s} d _ {i} (u _ {i} - w _ {i} u _ {1})\tag{6}
$$

The additional constraints in Eq. (5) ensure that the distance measure at the right hand side of Eq. (6) is always positive and thus sums up to a positive penalty. The relaxation of the problem can be seen to allow the first weight-profile wˆ (estimated through DEA) to approximate the desired weight-profile w only from one direction with respect to each attribute. Phase 1 determines from which side the optimization should take place. The final optimization model can be defined as:

$$
h _ {k} = \max _ {u, v} \sum_ {r = 1} ^ {s} u _ {r} y _ {r k} - \alpha \sum_ {i = 1} ^ {s} d _ {i} (u _ {i} - w _ {i} u _ {1})\tag{7}
$$

subject to

$$
\begin{array}{l} \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} - \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} \geq 0 \quad \text { for   } j = 1 \dots n \\ \sum_ {i = 1} ^ {m} v _ {i} x _ {i k} = 1 \\ \alpha d _ {i} (u _ {i} - w _ {i} u _ {1}) \geq 0 \quad \text { for   } i = 1 \dots , s \\ u _ {i}, v _ {j} \geq 0 \quad \text { for   all   } i, j \end{array}
$$

## 5. Case application

The developed model was tested within a real-life case study concerning an ERP software selection problem faced by the Austrian subsidiary called Primagaz Austria of an international wholesaler of liquid and gaseous fuels and related products (SHV Holdings N.V.). Before presenting the results, we provide short information on the company and ERP project background as well as on the selection methodology applied by the company. For a more detailed description about the company and the undertaken ERP adoption, see Ref. [10].

## 5.1. Background information

Today, Primagaz Austria has 90 employees, generates annual revenues of 55 million, and supplies 12,000 Austrian end-customers with their petroleum gas products and services, while pointing out that they are an ISO-9002 certified tank gas provider. Since the headquarters in France allow their subsidiaries to develop their own IT/IS strategies, the company was independent in their ERP decision. Until 2003, all primary functions run on a 20-year-old COBOL-based system in an out-of-date Novell NetWare environment. Limitations of this software infrastructure were the driving force behind the ERP adoption decision. For example, the system did not allow embracing the Austrian subdivisions causing redundant data storage. The back-office operations could not be linked or integrated with front-office operations, meaning that every working place needed two PCs (Windows/ Netware). External operations were neglected, e.g., there was no internet connection possible to support external data inquiries. Reporting functionality was limited, e.g., no longer time scales (reports over the last 7 years) were supported. In addition, monthly reports could only be produced within a delay of 5 days after the end of the month. The system required new programming by the vendor for every change in the data export interface. These were needed for more sophisticated reporting or controlling purposes. Also, the accounting capabilities did not meet the requirements. Because no further releases of the legacy system could be expected to overcome these shortcomings, business management decided to replace the legacy system.

## 5.2. Chosen decision making approach

Although ERP adoption was initiated due to technical reasons, Primagaz viewed their ERP project as important vehicle to support and enhance the company’s long-term strategic position. Thus, the strategic value of ERP and its degree of alignment in the organizational context was perceived by business management as the starting point for defining ERP requirements. This approach follows the recommendations found in literature concerning the concepts of strategic alignment and organizational fit in developing the IS/IT infrastructure [22].

The company’s ERP decision making methodology was based on the URM complemented with vendor-related perceptions and a separate financial analysis. The financial view comprised software licence, consulting, travelling, and hardware costs for the first and following years. Through the URM, they wanted the desired system to achieve a high ERP utility score through simple additive weighting based on a number of preselected attributes reflecting their specific range of targeted software-specific functionalities and benefits. The requirements comprised the categories (1) controlling and reporting, (2) accounting, (3) logistics, (4) purchasing, (5) needs of local divisions, (6) services and engineering, (7) sales, and (8) business management. Several attributes were defined in each group for evaluation summing up to 73 criteria. The weights and utility values were defined by a decision committee with key users from all functional departments.

URM provided a final utility score for each alternative leading to a ranking in terms of softwarespecific requirements. The overall utility score besides being difficult to interpret did not account well for providing information on the level of suitability in terms of organizational fit of each system. However, the decision committee did not use any other specific methodical aid to evaluate the level of organizational fit in order to support their primary objective of aligning their new IS infrastructure capabilities with their strategic focus.

## 5.3. Applying the new model

As already indicated, the company used the URM as a decision aid to rank the alternatives according to their desired profile defined by weights. The weighted utility scores for the three preselected alternatives (we will refer to them as A, B and C) were 253, 288 and 252, respectively. The score was calculated from 73 attributes belonging to the eight main functional sub-classes given in the previous section. As can easily be seen, alternative B outranks its opponents whereas A and C seem to have a tie, i.e., according to URM, they can be considered as equally good. This situation demonstrates the shortcomings of the URM: the resulting utility scores are hardly interpretable and do not provide a clear-cut ranking.

From the given weights in the URM, the relative weight profile w, as defined in the previous section, was extracted with respect to the eight attribute classes. This implicitly defined the ideal profile of the company and is illustrated in Fig. 1. As can be seen, the company placed a relative importance on accounting (2), and sales (7), while under-weighting their needs in terms of logistics (3), purchasing (4), and local divisions (5).

![](/api/attachments/ANEZNGRW/fulltext/images/d0ff123ac670b1a592ef4a1c4fb0992eb4a5a0cb245157838bd511fae7e5714f.jpg)  
Fig. 1. Desired profile w over eight main classes.

Knowing w, we started phase 1 of our profile distance method by setting the fade-factor a=0 in the optimization model (7) resulting again in a pure DEA calculation. As expected, the basic DEA model revealed that all alternatives were 100% efficient with different weight profiles for each of the three alternatives k (see Figs. 2–4). This lack of discrimination is a recognized problem in DEA applications [2]. From the results of phase 1, wˆ and hence d, the direction vector, were derived for each alternative.

From this point, a can be varied between zero (plain DEA) and l (plain URM) for each alternative yielding to intermediate profiles shown in Figs. 2–4. It should be noted that the precision of movements of a was 1E-7 and already a=0.7910204 yielded the URM profile for all alternatives. All weights were additionally constrained to stay within a ratio of at most 1:10.

![](/api/attachments/ANEZNGRW/fulltext/images/003fb2e53eb17bd3af6016815e9068ffd3fcb117f4f04fae6052398528833f2a.jpg)  
Fig. 2. Profiles fading from DEA to the desired one for alternative A.

![](/api/attachments/ANEZNGRW/fulltext/images/5dba976a591313d6396906a26599aa05b3e42b03254d96467bb2312747fa1d0f.jpg)  
Fig. 3. Profiles fading from DEA to desired one for alternative B.

It can be seen that alternative B (Fig. 3) does not have any intermediate profiles at the given precision. Within our resolution, it directly switches to the desired profile when raising a. This is not very surprising considering the high utility score of alternative B shown via URM. The first DEA-based profile indicates, however, that alternative B’s relative strength seems to be concentrated on accounting (2), an area with a high relative importance to the company. Thus, a new insight was provided for the decision maker.

The remaining alternatives A and C are posing the main challenge for the new model. Both methodical aids applied separately, i.e., the URM and DEA, do not allow for any discrimination between those alternatives. The pure URM approach yields approximately the same overall utility scores. The plain DEA approach classifies both systems as 100% efficient. In this setting, the proposed profile distance method supplies the decision maker with valuable insights. As Fig. 2 denotes, alternative A offers its main advantages in accounting (2) and logistics (3). When a is raised, already the intermediate profiles fit relatively well to the desired one (see also Table 1). It can be seen that from the first intermediate profile on, the strong emphasis placed on accounting (2) vanishes, which is a very interesting structural information. It demonstrates that alternative A does not need to overweight the impact of accounting to remain competitive. On the other hand, this adjustment improves organizational fit by 35% as reflected through a drop from distance 502 to 328 (see Table 1). Alternative A, however, still puts higher weights on logistics (3). From the second intermediate profile on, this is achieved at the expenses of sales (7), and business management (8), which can therefore be regarded as minor weaknesses.

![](/api/attachments/ANEZNGRW/fulltext/images/c385b857c1507585bd80316127804e630d2b9a548ac71cf314e1d4161810a9ce.jpg)  
Fig. 4. Profiles fading from DEA to desired one for alternative C.

Fig. 4 shows the performance of alternative C, which presents itself as inappropriate regarding the company’s needs. The results reveal that the attribute logistics (3), services and engineering (6) and sales (7) need to be weighted extensively higher compared to the other alternatives in order to remain competitive. This, however, has a negative impact on the improvement of the distances between the intermediate profiles to the desired one (see Table 1). Consequently, alternative C was unable to adapt and thus kept its own shape until finally forced into the desired profile through the model.

Table 1  
Transition points (significance of a: 1E-7)

<table><tr><td rowspan="2">α</td><td colspan="3">Distance measure (DEA efficiency in %)</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td>0.0000000</td><td>502 (100%)</td><td>386 (100%)</td><td>472 (100%)</td></tr><tr><td>0.0000002</td><td>328 (100%)</td><td>386 (100%)</td><td>472 (100%)</td></tr><tr><td>0.0000003</td><td>256 (100%)</td><td>386 (100%)</td><td>472 (100%)</td></tr><tr><td>0.0000004</td><td>256 (100%)</td><td>386 (100%)</td><td>454 (100%)</td></tr><tr><td>0.0000005</td><td>153 (100%)</td><td>0 (100%)</td><td>449 (100%)</td></tr><tr><td>0.0000007</td><td>153 (100%)</td><td>0 (100%)</td><td>443 (100%)</td></tr><tr><td>0.3408758</td><td>153 (100%)</td><td>0 (100%)</td><td>0 (88%)</td></tr><tr><td>0.7910204</td><td>0 (88%)</td><td>0 (100%)</td><td>0 (88%)</td></tr></table>

Bold figures mark points of change.

It should be noted that the distance for profiles is monotonously decreasing with respect to a. This implies that each profile can appear only once while changing a. Table 1 shows the transition points of a when using a maximum precision of 1E-7. The entries in the columns show for each DMU the corresponding distance and the DEA efficiency of the chosen profile given a. Figures in bold indicate changes for that specific transition level. The small magnitude of a is due to the model data and does not imply un-/importance.

Alternative A can be seen to be preferable for a in [0.0000002; 0.0000005), whereas alternative B is dominant in all other cases. Alternative A can approximate the desired profile earlier than its two competitors, however, only up to a certain amount. Alternative C, however, never exceeds the two others. The table also reveals that a had to be risen by an order of magnitude to force alternative A and C into the desired profile, at which point they were no longer DEA efficient.

Because alternatives A and C were so close, with respect to URM, we conducted a sensitivity analysis. Here, two random attributes in alternative C were increased in order to make alternative C by one point better than alternative A (with respect to URM). The experiments showed that there were no significant changes in the results of the profile distance method, especially in the figures illustrated above. This means that even when the URM shows that alternative C is better than alternative A, the profile distance method reveals alternative C’s weaknesses with respect to its bad matching profile. Consequently, our proposed method showed its use to investigate alternatives with similar overall utility values by indicating that alternative A provides a better organizational fit than alternative C.

The ex post MADM analysis provided here is based on the organization’s perception of softwarespecific benefits only. As already indicated, in the real-life setting, the overall value of each alternative was complemented with a separate vendor- and costspecific evaluation. From the vendor perspective, negative perceptions concerning customer responsiveness of supplier B caused the company to exclude the corresponding system from their final choice set. Therefore, the project team had to decide between alternatives A and C and, due to cost advantages, finally chose our would-be recommendation A.

## 6. Conclusions and further research

Although the analyzed company based their ERP decision making on a structured and methodical approach starting with a strategic assessment of their needs, their methodology showed limitations in the context of the given research issues. The case therefore provided us with an ideal setting to demonstrate the newly introduced profile distance method. The method utilizes the important concept of organizational fit, i.e., by exploring the distance to the desired product profile. It improves ranking and identifies decisive selection criteria—all of which were not assessed appropriately by the company. Additionally, the method offers structural information with an intuitive meaningful graphical representation. These illustrations can help the decision maker to better understand system-specific strengths and weaknesses or can serve as an impulse to reconsider the companies’ desired profile.

The proposed approach combines the merits of two prominent concepts, URM and DEA, individually applied in decision making while making up for a number of their limitations. In the URM, the overall utility values cannot be interpreted easily and they often are sensitive to small changes in the inputs. By analyzing distance metrics and exploring strengths and weaknesses with respect to a desired profile, the decision maker relaxes these URM-specific limitations. The DEA limitations concerning no clear-cut ranking of alternatives or unrealistic (extreme) weighting schemes were also addressed.

As for any selection method, limitations concerning its application can be elements of the contextual setting of the IS investment, e.g., time frame, size, or involved stakeholder. This implies that IS projects have certain characteristics that influence the applicability of evaluation approaches. Although we believe that the proposed distance profile method can service a broad diversity of IS evaluation situations, we seek, on the one hand, to define the significant requirements with further case study applications resulting. In addition, we aim to transform our prototype implementation of the proposed methodology into a standardized software environment to allow decision makers and students to test the methodology more comprehensively. On the other hand, we seek to elaborate on the technical issues addressed in the basic model development in this publication. These issues comprise among others the discussion of different distance metrics and their global solving strategies beyond linear programs.

## Acknowledgements

The authors thank Ulrike Andres (CEO of Primagaz) for offering us the opportunity to investigate their decision case, Andrew B. Whinston (Editor-in-Chief) and his team for their editorial services, as well as three anonymous reviewers for their valuable comments and advice.

## References

[1] M. Abbott, C. Doucouliagos, The efficiency of Australian universities: A data envelopment analysis, Economics of Education Review 22 (2003) 89– 97.

[2] N. Adler, L. Friedman, Z. Sinuany-Stern, Review of ranking methods in the data envelopment analysis context, European Journal of Operations Research 140 (2002) 249 – 265.

[3] R. Allen, E. Thanassoulis, Improving envelopment in data envelopment analysis, European Journal of Operational Research 154 (2004) 363– 379.

[4] P. Anderson, N.C. Peterson, A procedure for ranking efficient units in data envelopment analysis, Management Science 39 (1993) 1261 – 1264.

[5] J.L. Andresen, A Framework for Selecting an IT Evaluation Method—in the Context of Construction, BYG-DTU, Technical University of Denmark (2001).

[6] D.E. Avison, C.H. Cuthbertson, P. Powell, The paradox of information systems: Strategic value and low status, The Journal of Strategic Information Systems 8 (1999) 419– 445.

[7] R.C. Baker, S. Talluri, A closer look at the use of data envelopment analysis for technology selection, Computers and Industrial Engineering 32 (1997) 101 – 108.

[8] E.W.N. Bernroider, S. Koch, ERP selection process in midsize and large organizations, Business Process Management Journal 7 (3) (2001) 251– 257.

[9] E.W.N. Bernroider, V. Stix, The evaluation of ERP systems using data envelopment analysis, Proceedings of IRMA 2003, 2003, pp. 283–286.

[10] E.W.N. Bernroider, V. Stix, Enrichment of a utility ranking method using data envelopment analysis—a case study of an ERP selection problem, Proceedings of IRMA, 2004, pp. 292–295.

[11] P.V. Boufounou, Evaluating bank branch location and performance—a case-study, European Journal of Operational Research 87 (1995) 389 – 402.

[12] W.F. Bowlin, Evaluating performance in governmental organisations, The Government Accountants Journal 35 (1986) 50–57.

[13] J. Butler, J. Jia, J. Dyer, Simulation techniques for the sensitivity analysis of multicriteria decision models, European Journal of Operational Research 103 (1997) 531 – 546.

[14] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the efficiency of decision making units, European Journal of Operational Research 2 (1978) 429–444.

[15] W.W. Cooper, L.M. Seiford, K. Tone, Data envelopment analysis, Kluwer Academic Publishers, London, 2000.

[16] T.H. Davenport, Mission critical-realizing the promise of enterprise systems, Harvard Business School Press, Boston, 2000.

[17] B. Farbey, F. Land, D. Targett, Evaluating investments in IT, Journal of Information Technology 7 (1992) 109–122.

[18] B. Farbey, F. Land, D. Targett, How to assess your IT investment: A study of methods and practice, Butterworth-Heinmann, Oxford, 1993.

[19] B. Farbey, D. Targett, F. Land, The great IT benefit hunt, European Management Journal 12 (3) (1994) 270 – 279.

[20] A.B. Frielink (Ed.), Auditing automatic data processing, Elsevier, Amsterdam, 1961.

[21] S. Gattoufi, M. Oral, A. Reisman, A taxonomy for data envelopment analysis, Socio Economic Planning Sciences 38 (2–3) (2004) 141– 158.

[22] J.C. Henderson, N. Venkatraman, Strategic alignment: Leveraging information technology for transforming organizations, IBM Systems Journal 32 (1) (1993) 4 – 16.

[23] K.-K. Hong, Y.-G. Kim, The critical success factors for eRP implementation: An organizational fit perspective, Information and Management 40 (1) (2002) 25 – 40.

[24] C.L. Hwang, K.P. Yoon, Multiple attribute decision making: Methods and applications, Springer, New York, 1981.

[25] Z. Irani, Investment justification of information systems: A focus on the evaluation of MRPII, Technical report, Department of Manufacturing and Engineering Systems, Brunel University, Uxbridge, 1998.

[26] Z. Irani, Information systems evaluation: Navigating through the problem domain, Information and Management 40 (2002) 11– 24.

[27] A. Jimenez, S. Rios-Insua, A. Mateos, A decision support system for multiattribute utility evaluation based on imprecise assignments, Decision Support Systems 36 (1) (2003) 65– 79.

[28] E.O. Joslin, Computer selection, Addison-Wesley, London, 1968.

[29] M. Khouja, The use of data envelopment analysis for technology selection, Computers and Industrial Engineering 28 (1995) 123– 132.

[30] R. Kumar, Understanding the value of information technology enabled responsiveness, Electronic Journal of Information System Evaluation 1 (2000).

[31] K.C. Laudon, J.P. Laudon, Management information systems, 8th ed., Prentice Hall, London, 2003.

[32] D.L. Olsen, Decision aids for selection problems, Series in operations research, Springer, New York, 1996.

[33] M.M. Parker, R.J. Benson, H.E. Trainor, Information economics, Linking business performance to information technology, Prentice-Hall, New Jersey, 1988.

[34] J. Rainer, V. Stix, IT appraisal methods and methodologies—a critical literature review, Proceedings of IRMA, 2004, pp. 37 – 40.

[35] D. Remenyi, A. Money, M. Sherwood-Smith, Z. Irani, The effective measurement and management of IT costs and benefits, 2nd ed., Butterworth-Heinemann, Oxford, 2000.

[36] T.J.W. Renkema, E.W. Berghout, Methodologies for information systems investment evaluation at the proposal stage: A comparative review, Information and Software Technology 39 (1997) 1 – 13.

[37] S. Rios-Insua, A. Jimenez, A. Mateos, Sensitivity analysis in a generic multi-attribute decision support system, in: K.J. Engemann, G.E. Lasker (Eds.), Advances in decision technology and intelligent information systems, The International Institute for Advanced Studies in Systems Research and Cybernetics, Ontario, 2003, pp. 31–35.

[38] J. Sarkis, A comparative analysis of DEA as a discrete alternative multiple criteria decision tool, European Journal of Operational Research 123 (2000) 543– 557.

[39] P.G. Sassone, Cost benefit analysis of information systems: A survey of methodologies, Proceedings of the ACM Conference on Supporting Group Work, 1988, pp. 126 – 133.

[40] E. Thanassoulis, Introduction to the theory and application of data envelopment analysis—a foundation text with integrated software, Kluwer Academic Publishers, London, 2001.

[41] P. Weill, M.H. Olson, An assessment of the contingency theory of management information systems, Journal of Management Information Systems 6 (1) (1989) 59 – 85.

[42] K.P. Yoon, C.-L. Hwang, Multiple attribute decision making: An introduction, Sage University Paper series on quantitative applications in the social sciences, Sage Publications, Thousand Oaks, CA, 1995.

[43] S.H. Zanakis, A. Solomon, N. Wishart, S. Dublish, Multiattribute decision making: A simulation comparison of select methods, European Journal of Operational Research 107 (3) (1998) 507– 529.

![](/api/attachments/ANEZNGRW/fulltext/images/2b6d027a02f5d5438568b7716d56ab4d41e8674b3b601bc77121b3a3912fa806.jpg)  
Edward W.N. Bernroider received an MS degree in applied informatics from the University of Salzburg (1997) and a PhD degree in business administration from the Vienna University of Economics and Business Administration (2001), where he is employed as Assistant Professor since 1998. His current research and industry projects focus on evaluation/selection methodologies in IT/IS decisions, IT/IS controlling, and the international software industry.

![](/api/attachments/ANEZNGRW/fulltext/images/1c4e58b05c7dfab23995bfc3f36ddd80c948ad21bbc3f160eea909a4839e51d1.jpg)

Volker Stix studied computer science at the Technical University of Vienna. His PhD thesis covered optimizational and computational aspects in quadratic non-convex global programming. Since 2001, he is assistant professor at the Vienna University of Economics and Business Administration. His research interests include decision support systems in information technologies especially with focus on adaptation and usability of theoretical models for decision makers.
