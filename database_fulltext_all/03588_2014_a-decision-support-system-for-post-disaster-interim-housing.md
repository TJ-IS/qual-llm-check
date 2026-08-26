---
otero_id: 3588
otero_key: "VTZ7AYMG"
title: "A decision support system for post-disaster interim housing"
authors: "Terry R. Rakes; Jason K. Deane; Loren P. Rees; Gary M. Fetter"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Terry R. Rakes <sup>a,</sup>⁎, Jason K. Deane <sup>a</sup>, Loren P. Rees <sup>a</sup>, Gary M. Fetter <sup>b</sup>

<sup>a</sup> Department of Business Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, VA 24061, United States <sup>b</sup> College of Business, Valparaiso University, 1909 Chapel Drive, Valparaiso, IN 46383, United States

## a r t i c l e i n f o

Article history: Received 12 December 2013 Received in revised form 12 May 2014 Accepted 21 June 2014 Available online 1 July 2014

Keywords: Decision support systems Integer programming Heuristics Disaster management

## a b s t r a c t

The Northridge earthquake of 1994 displaced almost 10,000 families and destroyed major transportation infrastructure within Southern California, and Hurricane Katrina created the largest national housing crisis since the Dust Bowl of 1930, destroying over 300,000 homes and leaving over one million people seeking shelter. Numerous smaller disasters each year such as tornados, costal or inland <sup>fl</sup>ooding, and less severe earthquakes also destroy homes and displace families, although on a much smaller scale. Arranging housing for disaster victims ranks as a top priority after the immediate needs for food and medical care are met. This task becomes more challenging as families are displaced for a longer period of time due to increases in costs, government involvement, and expectations of the victims. In early 2009, FEMA released the <sup>fi</sup>rst-ever National Disaster Housing Strategy which calls for improved planning and outlines the key principles and policies guiding disaster sheltering, interim housing, and restoration of permanent housing. While all three housing problems are very dif<sup>fi</sup>cult, the provision of adequate temporary or interim housing is perhaps the most challenging. A few researchers have addressed the issue of optimal allocation of temporary housing, but have focused primarily on the <sup>fi</sup>rst part of the problem which focuses on the selection of adequate capacity from among available interim housing alternatives. The second part of the problem, which consists of recommending housing alternatives to individual families from the pool of temporary housing units selected in phase one such that educational, healthcare, and socio-economic needs are met, has not yet been addressed to the best of our knowledge. We propose a decision support system for assigning families to housing units which addresses these needs. We develop a benchmark integer programming model for developing a balanced housing plan, and then use the model to evaluate three heuristics which could be practically applied with our system. We use a prototypical example to illustrate the model and evaluate the heuristics, and to demonstrate their appropriateness for the development of realistic real-time housing recommendations.

© 2014 Elsevier B.V. All rights reserved

## 1. Introduction

Natural disasters such as hurricanes, earthquakes, <sup>fi</sup>res, <sup>fl</sup>oods, and tsunamis, and man-made disasters such as terrorists' attacks, have the potential to disrupt lives and displace families in enormous numbers. When homes are destroyed and families are displaced, providing shelter and housing is essentially a three-phase process. First, short-term emergency shelters must be located to provide safe space, food, and emergency medical care for the displaced families. These shelters may also serve as processing centers where information can be gathered about the families and their immediate and longer term needs. Once the sheltering phase is complete, which could last for a few days up to a few weeks, families are sometimes able to return home if the disaster damage is minimal and their previous homes are structurally and environmentally safe. However, this is often not the case. Disasters, especially large-scale events, commonly cause lasting structural and environmental damage to many homes and business, in which case families may be displaced for much longer periods of time. In the case of Hurricane Katrina, many families are still unable to return home eight years later.

In this situation, we enter the second phase of the problem, providing interim or temporary housing for families. It is important to note that the de<sup>fi</sup>nition of family in relation to housing is very broad, and may consist of a housed group which is based on a traditional nuclear family, an extended family, or simply a co-residence arrangement. Although interim housing may last for several years, the goal of disaster relief planners is to limit the length of this phase as much as possible in order to minimize the adverse effects which families experience when separated from their socio-economic, medical, and educational support structures. If this interim period lasts too long or involves moving families too far from their previous neighborhood, families may never return to rebuild their old neighborhoods because of broken social ties or a general feeling of not belonging. The goal of interim housing is to allow the family to live a normal life until they can return to their home or to other permanent housing, which FEMA identi<sup>fi</sup>es as the

Parameters

focus of the third phase. While all three phases of this housing problem are very dif<sup>fi</sup>cult, the provision of adequate temporary or interim housing is perhaps the most challenging.

In early 2009, The Federal Emergency Management Authority (FEMA) published its National Disaster Housing Strategy which outlines their guidelines for planning and providing housing in all three phases [9]. Their report states that “the needs and expectations of disaster victims in interim housing are greater than those in shelters, and our experience has taught us the importance of addressing these issues early in disaster response and throughout the recovery process.” They also af<sup>fi</sup>rm that “housing is the connector to how we live our lives and interact with the social networks within our communities. While interim housing cannot replicate a household's pre-disaster conditions, it can be planned to integrate delivery of essential support or ‘wrap-around’ services, such as referrals for mental health, emotional, and spiritual support; job placement; childcare; social services; and other resources that can help make temporary housing viable.”

Researchers have long understood the importance of socio-economic impacts on displaced families [2,12,14]. When families are forced to live isolated from their familiar surroundings and friends, they may experience emotional dif<sup>fi</sup>culties and broken social ties which could ultimately lead to a reluctance to return and rebuild the former community. El-Anwar and El-Rayes [2] discussed the importance in this regard of minimizing the distance between the displaced family's preferred location and its assigned temporary housing location. Other factors which affect the level of socioeconomic disruption include the capacity of temporary housing alternatives to support the economical, medical, educational, and safety needs of displaced families [3,27,31].

While many researchers have explored these effects, little attention has been given to the development of quanti<sup>fi</sup>able methods for recommending housing alternatives to families in consideration of these factors. In a series of three studies, El-Anwar et al. develop a model, and eventually an automated system, for identifying desirable housing alternatives [3–5]. While their research is a major step forward, they do not suggest any mechanism for recommending the best alternatives to families from the identi<sup>fi</sup>ed housing pool. Without a mechanism for matching families with alternatives, it is likely that many families will choose an area that either is far removed from their area of preference or does not have the necessary healthcare and educational support services which allow them to function properly. The only housing matching mechanism we are aware of is the FEMA Housing Portal [8] which allows web users to query a database of available temporary housing alternatives. However, FEMA's mechanism does not provide any information on nearby availability of hospitals and schools, nor does it allow planners to balance the needs of numerous displaced families. This portal is essentially a “multiple listing service” for housing alternatives which leaves users to sort through numerous housing options with little support and feedback. What seems to be needed is a decision support system for matching families with speci<sup>fi</sup>c housing alternatives. Decision support system design for disaster management has been a popular topic in the literature [10,11,22,23,25], and systems have been developed for many areas of disaster management, including nuclear and radiological emergencies [28], earthquakes [7], and health emergencies [13,16,26]. While such free and open source decision support systems for disaster management certainly bene<sup>fi</sup>t from public– private collaboration to deploy and maintain [20], the <sup>fi</sup>rst step is the development of a prototype system.

The purpose of this paper is to present a decision support system for making speci<sup>fi</sup>c recommendations to families with respect to their interim housing alternatives. First, we develop an integer programming model which serves as a benchmark for our system development. The model solution represents a “greater-good” set of housing assignments that would balance the aforementioned objectives across all families. The model also serves as a learning tool to better understand the housing problem, and could serve as a planning tool for determining whether the available alternatives allow for feasible housing of all families.

However, the model solution is impractical as a real-time decision aid as each family is interested in the best housing alternative relative to their needs only, and families present themselves for assistance sequentially as opposed to as a group. Next, we present a set of heuristics which can approximate the benchmark solution while serving each family on an individual basis, and we evaluate the heuristics through a hypothetical example. Next, we discuss the DSS design for the implementation of the best heuristic. Finally, we offer conclusions and possible areas for future research.

## 2. The interim housing model

The interim housing model is designed to minimize the total distance from the family's preferred neighborhood and the distances from necessary support services across all displaced families while making sure that there are suf<sup>fi</sup>cient housing units to accommodate the families and suf<sup>fi</sup>cient school capacity in a given area. In this example, we consider educational and healthcare support services, although other important services such as spiritual support and childcare services could also be included. Consider the following de<sup>fi</sup>nitions:

<table><tr><td colspan="2">Variables</td></tr><tr><td> $X_{ij}$ </td><td>assignment of family i to housing alternative j (1 = yes, 0 = no).</td></tr></table>

<table><tr><td colspan="2">Parameters</td></tr><tr><td> $W_{if}$ </td><td>relative weight for each family  $i$  on the importance of factor  $f$ ( $f = 1$  for socioeconomic area,  $f = 2$  for healthcare services, $f = 3$  for educational services)</td></tr><tr><td> $F_{sj}$ </td><td>maximum number of families of size  $s$  which can be housed by alternative  $j$ </td></tr><tr><td> $A_i$ </td><td>area of preference (original neighborhood or locus of socio-economic support structure) for family  $i$ </td></tr><tr><td> $D_{A_{i},j}$ </td><td>distance from area  $A_i$  to alternative  $j$ </td></tr><tr><td> $H_{jt}$ </td><td>distance to the nearest healthcare facility type  $t$  from alternative  $j$  ( $t = 1$  for hospital,  $t = 2$  for mental health services facility,  $t = 3$  for clinic)</td></tr><tr><td> $E_{jk}$ </td><td>distance to within-district educational facility type  $k$  from alternative  $j$  ( $k = 1$  for pre-k, kindergarten, or elementary school,  $k = 2$  for middle school,  $k = 3$  for high school)</td></tr><tr><td> $N_{it}^{H}$ </td><td>healthcare need matrix (1 indicates a need in family  $i$  for healthcare type  $t$ , 0 indicates no need)</td></tr><tr><td> $N_{ik}^{E}$ </td><td>educational need matrix derived from  $B_{ik}$  (1 indicates a need in family  $i$  for educational service type  $k$ , 0 indicates no need)</td></tr><tr><td> $B_{ik}$ </td><td>number of school-age children in family  $i$  at level  $k$ </td></tr><tr><td> $C_{kd}$ </td><td>additional capacity of school(s) of type  $k$  in school district  $d$ </td></tr><tr><td> $L_d$ </td><td>set of housing alternative locations in school district  $d$ </td></tr><tr><td> $S_i$ </td><td>size of family  $i$ </td></tr><tr><td> $smax_j$ </td><td>maximum size of a family that can be housed at alternative  $j$ </td></tr><tr><td> $s'$ </td><td>lower size limit designed for a housing alternative of size  $s$ .</td></tr></table>

The parameter s′ is the minimum size family that an alternative is designed for, but not necessarily that it can accommodate. Suppose we have alternatives that have 2, 3, or 4 bedrooms so that they are designed for a maximum of 4, 6, or 8 people, respectively. The resulting values of s′ would be 1, 5, and 7, respectively. That is, a two-bedroom unit would be designed to handle a minimum of one person and a maximum of 4. A three-bedroom unit would be designed to handle from 5 to 6 people (although, as we will see later, a three-bedroom unit could house less than 5 people if necessary to provide enough temporary housing for all families). A four-bedroom unit would be designed to handle 7 or 8 people, although again it could house fewer if necessary. Thus, s′ is the family size at which we must move up to the next largest capacity unit.

We now de<sup>fi</sup>ne the housing planning model as follows:

$$
\begin{array}{l} M i n Z = \sum_ {i} \sum_ {j} W _ {i 1} D _ {A _ {i j}} X _ {i j} + \sum_ {i} \sum_ {j} \sum_ {t} W _ {i 2} H _ {j t} N _ {i t} ^ {H} X _ {i j} \\ \qquad + \sum_ {i} \sum_ {j} \sum_ {k} W _ {i 3} E _ {j k} N _ {i k} ^ {E} X _ {i j} \end{array}\tag{1}
$$

$$
\sum_{\substack{i\\ S_{i}\geq s^{\prime}}}X_{ij}\leq \sum_{s = s^{\prime}}^{smax_{j}}F_{sj}\quad \text{for each} s^{\prime},j\tag{2}
$$

$$
\sum_ {i} \sum_ {j \in L _ {d}} B _ {i k} X _ {i j} \leq C _ {k d} \quad \text {   for   each   } k, d\tag{3}
$$

$$
\sum_ {j} X _ {i j} = 1 \quad \text {   for   each   } i\tag{4}
$$

$$
X _ {i j} = \{0, 1 \} \quad \text {   for   each   } i, j.\tag{5}
$$

The <sup>fi</sup>rst term of the objective function calculates the total distance from all suggested family housing alternatives to their preferred area. The second term of the objective function represents the total distance from housing alternatives to necessary healthcare services. For any recommended alternative, the healthcare need matrix indicates the need of a particular healthcare service by a family with the presence of a 1 (families may have multiple healthcare needs and thus have 1's in several columns). By summing over healthcare need types and multiplying by the distance from the considered housing alternative to the closest healthcare facility of that type, we obtain the total travel distance by all families to receive the types of healthcare they need. The third term is identical to the second except that it deals with educational needs. Families may have school-age children in several age groups and will certainly want to send them to an appropriate school without excessive travel. Finally, each term in the objective function may be weighted differently. The $W _ { i f }$ allow for a multiplier to be applied to any category f which is deemed to be of greater importance to family i. Using a weighted objective function is acceptable because the entire objective function is in the same units (miles).

The constraints in Eq. (2) for each possible family size and housing alternative will assure that the number of families suggested for a particular housing alternative will not exceed the capacity of that alternative. As described above, families could be housed in a unit which is designed to hold more people than the family contains, but not less. During the planning phase when housing alternatives are identi<sup>fi</sup>ed, we would hope that adequate capacity is identi<sup>fi</sup>ed and thus a feasible solution exists. However, if capacity is not suf<sup>fi</sup>cient, dummy alternatives can be added to create a feasible scenario, and any families recommended for the dummy alternatives would represent the special cases which cannot be handled through the normal process. For example, when this de<sup>fi</sup>cit situation exists, FEMA often brings in temporary trailers and creates housing parks to handle the over<sup>fl</sup>ow. The constraints from Eq. (3) ensure that families with children are recommended for alternatives that have suf<sup>fi</sup>cient capacity within the school district where that alternative is located and for the school level of the child. The constraints from Eq. (4) assure that each family is assigned to exactly one housing alternative. Finally, the last constraint (Eq. (5)) stipulates that the decision variables are treated as binary.

As mentioned above, using a weighted objective function in this model is acceptable because the entire objective function is in the same units (miles). However, while acceptable, it is not totally desirable. Even when units in an objective function are commensurate, their scales may be vastly different, creating dif<sup>fi</sup>culties in determining appropriate weights. In this example, the distance back to the family's socioeconomic area of preference is likely to be much higher than the distance to newly assigned schools or available medical care. Thus, using weights of, say, $\left( W _ { i 1 } , W _ { i 2 } , W _ { i 3 } \right) = \left( 1 , 2 , 1 \right)$ does not necessarily mean that we are putting twice as much emphasis on minimizing distance from medical care as we might assume. If the total family mileage from their area of preference is ten times as great as the mileage from medical services, a weight of 2 to 1 would do little to effect any preference change. In this scenario, determining appropriate weights is a very dif<sup>fi</sup>cult task for a decision maker.

To alleviate this problem, we suggest a minor but well-established modi<sup>fi</sup>cation to the model which utilizes goals or ideals for each component of the objective function and then seeks to minimize the weighted deviation from those goals. These goals generally represent the lowest possible value for the objective function component as if it were the only component in the objective function.

With the addition of the following parameters:

$$
\begin{array}{l l} G _ {1} & \text { total   mileage   target   for   socioeconomic   displacement } \\ G _ {2} & \text { total   mileage   target   for   health   care   access } \\ G _ {3} & \text { total   mileage   target   for   educational   access. } \end{array}
$$

we formulate the modi<sup>fi</sup>ed interim housing model as:

Min $Z = { { Q } _ { 1 } } + { { Q } _ { 2 } } + { { Q } _ { 3 } }$

6

$$
\left(\frac {\left(\sum_ {i} \sum_ {j} W _ {i 1} D _ {A _ {i j}} X _ {i j}\right) - G _ {1}}{G _ {1}}\right) = Q _ {1}\tag{7}
$$

$$
\left(\frac {\left(\sum_ {i} \sum_ {j} \sum_ {t} W _ {i 2} H _ {j t} N _ {i t} ^ {H} X _ {i j}\right) - G _ {2}}{G _ {2}}\right) = Q _ {2}\tag{8}
$$

$$
\left(\frac {\left(\sum_ {i} \sum_ {j} \sum_ {k} W _ {i 3} E _ {j k} N _ {i k} ^ {E} X _ {i j}\right) - G _ {3}}{G _ {3}}\right) = Q _ {3}\tag{9}
$$

$$
\sum_{\substack{i\\ S_{i}\geq s^{\prime}}}X_{ij}\leq \sum_{s = s^{\prime}}^{smax_{j}}F_{sj}\qquad \text{for each} s^{\prime},j\tag{10}
$$

$$
\sum_ {i} \sum_ {j \in L _ {d}} B _ {i k} X _ {i j} \leq C _ {k d} \quad \text {   for   each   } k, d\tag{11}
$$

$$
\sum_ {j} X _ {i j} = 1 \quad \text {   for   each   } i\tag{12}
$$

$$
X _ {i j} = \{0, 1 \} \quad \text {   for   each   } i, j.\tag{13}
$$

## 3. An interim housing example

To illustrate application of the interim housing assignment model, we present a hypothetical situation involving 500 displaced families and 10 interim housing alternatives. In this context, a housing alternative is a location with multiple housing units. These might be apartment complexes, manufactured housing parks, unoccupied former military or government housing, etc. which are each capable of housing multiple families. The capacity to house families of size s at each alternative j is expressed through $F _ { s j } ,$ as described above. Fig. 1 illustrates the scenario, where coastal <sup>fl</sup>ooding has forced these 500 families to seek inland housing. Each family's former residence was in one of the 6 areas of the disaster-affected region, which acts as their socioeconomic area of preference when calculating the distance to each of the alternatives. Fig. 1 also shows the locations of schools and medical facilities.

Based on this scenario, we generate random but reasonable values for each of the parameters of the housing model. We generate the distance from each area of preference to each of the housing alternatives and the capacity (number of housing units) for each housing alternative. We assume that units would typically have 2, 3, or 4 bedrooms providing designed capacity for 4, 6, or 8 persons, respectively. We then generate a family pro<sup>fi</sup>le for each family which includes the size of the family, as well as the number of school-age children in each level (pre-k/kindergarten and elementary, middle school, and high school) and the number of persons in the household who require access to medical services located at hospitals, mental health facilities, and clinics. Where possible, we use typical census data to assure realism, such as the 2010 census <sup>fi</sup>gure for percent of households with children of 33.5% [6], which we use to extrapolate the likely percentage of households with children in each age group. Next, we generate the distances from housing alternatives to both healthcare and educational facilities in each of the categories outlined above. Finally, we generate the healthcare and educational need matrices, realizing that any family can have multiple healthcare and/or educational needs, such as having a grade school and a middle school student and an elderly parent in need of clinic care. In a real disaster, this information would be collected and entered into our database during the sheltering phase by disaster case workers as displaced families are registered for assistance.

This hypothetical dataset resulted in a model instance with 5003 variables and 539 constraints. Because of the size of the model, we use the CPLEX optimizer which is capable of solving very large problems. One of the major challenges in solving large-scale IP problems is the translation of data into the correct model format for solution. To assist in this process, we develop a computer program to read the input parameters and matrices and generate formatted CPLEX code as a text <sup>fi</sup>le, which can then be read by and executed in CPLEX. For the example problem, CPLEX found a feasible solution in .11 s. To test scalability, we run a larger problem with 1000 families and 20 housing alternatives (20,003 variables and 1069 constraints) and obtain a solution in .45 s. This speed is possible because CPLEX uses numerous pre-solve and compaction routines. The model could take longer to solve if the constraints are tighter, but this certainly illustrates that the model can be solved for relatively large problems. This could be very important if disaster planners wanted to use this model as a planning tool to determine feasibility of their housing pool for a hypothetical group of displaced families based on the demographics of their local area. However, as we pointed out earlier, though the model might be ef<sup>fi</sup>cient enough to use as a real-time planning tool, it is not suitable for the real situation. Families are interested in the best recommendation for their family as opposed to the “greater-good.” Also, the families do not present themselves as a group for advice, but will arrive sequentially. Therefore, the value of the model for our situation is to serve as a benchmark to evaluate heuristics which are used in our housing recommender system.

![](/api/attachments/VTZ7AYMG/fulltext/images/a70e2b2de55706eba67d18ec85e5c0423c54971a2f32300b550d6a154f9d7072.jpg)  
Numbers inside flooded areas are displaced neighborhoods; Circled numbers represent housing alternative locations; H= Hospital; C=Clinic; MH = Mental health facility; ES=Elementary school; MS=Middle School; HS=High School  
Fig. 1. Hypothetical layout of disaster-affected region.

## 4. Heuristics

When mathematical formulations have proved computationally intractable, researchers have generally turned to heuristics to provide good but not necessarily optimal solutions. Many of these have been based on the common greedy principle [17,18,21,24,30,32,33]. Others have been based on principles such as primal effective capacity [1], attempts to reduce the core problem size [15], and numerous other strategies. In our situation, the need for heuristics is not prompted by computational intractability, although certainly our integer programming benchmark model could become intractable if the problem size expands signi<sup>fi</sup>cantly. Instead, our need for heuristics is driven by the fact that the solution of the integer programming model requires that we have all parameter information available at once, which means practically that all families would have to register their housing requests and then wait for a recommendation until all others have also registered. This is contrary to the intent of a decision support system. Additionally, the model solution provides a “greater-good” solution which is not going to be accepted by all families. Disaster managers can only recommend a housing alternative; they cannot mandate an alternative to a family. While the benchmark solution tells us what is possible in terms of feasibly housing everyone while providing services in the best overall fashion, it is not realistic as a real-time recommendation system.

In a similar fashion, many of the heuristics mentioned above also require that all alternatives are presented at once so that we can make the best myopic choice from among the alternatives, and therefore are not suitable. The most suitable type of heuristic for our purpose is a form of the “nearest neighbor” heuristic which is also a greedy heuristic but allows a choice based on a subset of alternatives, and allows one choice at a time [19]. In the nearest neighbor approach, the entire graph is not necessary, only the local region. Knowledge of alternatives beyond the neighbors is not needed or taken into account, just as we must make a recommendation based on the current family with no knowledge of the families yet to come. In the remainder of this section, we present three heuristics that mirror the way families would actually make their decision.

## 4.1. Greedy size (GS)

In our benchmark model designed to establish the best set of housing decisions that would minimize total socioeconomic distance, housing unit size is treated as a constraint such that everyone is assigned in a way that feasibly uses the available space. However, for some families, minimal housing size may be an important objective. Since size (number of bedrooms) is at least one indicator of housing cost, and postdisaster most families will face some decrease in income or increase in expenses, families may be more concerned with <sup>fi</sup>nding the smallest available unit which is large enough to house their family, with location serving as a secondary criteria used to <sup>fi</sup>lter among those units tied for the smallest. Our <sup>fi</sup>rst greedy heuristic is used to mimic this behavior. First, the system will determine the number of bedrooms that will adequately house the family. Next, the support system will identify all housing alternatives that have a unit of that size and suf<sup>fi</sup>cient capacity in the school district for their children (if any). They will accept a larger unit only if no units exist at any location at their minimal size level. Within the units that qualify based on size and school capacity, the system will move to the secondary criteria of minimizing socioeconomic distance and will greedily choose the smallest. This process will be repeated as each family presents itself for assistance, moving through the solution space of available housing in a manner similar to our “nearest-neighbor” discussion earlier. An algorithm for searching the housing database would contain the following steps.

1. Set i = 1 (<sup>fi</sup>rst family), all $X _ { i j } = 0 , D _ { t o t a l } = 0 ,$ , and $W D _ { t o t a l } = 0$

2. Calculate necessary bedrooms nb for family i (if family size ≤ 4, then nb = 2; if family size N 4 and ≤ 6, then nb = 3; if family size N 6, then nb = 4)

3. Determine minimum available housing size S which is adequate for family i

3a. $\mathrm { I f } n b = 2 ,$ , go to step 3b. If nb = 3, go to step 3c. If nb = 4, go to step 3d.

3b. If a 2-bedroom unit is available in any housing alternative and there is suf<sup>fi</sup>cient school capacity in that alternative's school district for family i's children (if any), set $S = 2$ and go to step 4. Otherwise, go to step 3c.

3c. If a 3-bedroom unit is available in any housing alternative and there is suf<sup>fi</sup>cient school capacity in that alternative's school district for family i's children (if any), set S = 3 and go to step 4. Otherwise, go to step 3d.

3d. Set S = 4. Continue.

4. Set $W D _ { m i n } = \infty \mathrm { a n d } A l t = 0 .$

5. Set $k = 1$ (<sup>fi</sup>rst housing alternative)

6. If no units of size S exist within alternative k, or if the school district sd for k does not have capacity for i's children, go to step 9. Otherwise, continue.

7. Calculate the total distance $D _ { k }$ and the total weighted distance WD from alternative k to family i's area of preference, necessary schools, and necessary hospitals, based on family i's stated weights.

8. If $W D _ { k } < W D _ { m i n } ,$ set $W D _ { m i n } = W D _ { k }$ and $A l t = k .$ Continue.

9. If more housing alternatives exist, set k = k + 1 and return to step 6. Otherwise, continue.

10. Letting j = Alt, set $X _ { i j } = 1 .$ . Set $D _ { t o t a l } = D _ { t o t a l } + D _ { j }$ and $W D _ { t o t a l } =$ $W D _ { t o t a l } + W D _ { m i n } .$

11. $X _ { i j } = 1 ,$ , and the values of S and $D _ { j }$ and $W D _ { m i n }$ represent the solution for family i.

12. Reduce the number of available units of size S within housing alternative j by 1. If family i has school-age children, reduce the capacity at each level within school district sd by the number of children at that school level in family i.

13. If there are more families, set $i = i + 1$ and return to step 2. Otherwise, continue.

14. The set of nonzero $X _ { i j }$ and the values of $D _ { t o t a l }$ and $W D _ { t o t a l }$ represent the solution across all families.

The advantage to this logic in terms of a decision support system designed to help a large number of families is that it is likely to yield a feasible solution as long as the situation is feasible. Since each family is recommended a unit which is at their minimum need level, the set of recommendations will satisfy the housing availability constraint in our benchmark model as long as a feasible solution exists. However, because the heuristic only considers available school capacity at the time of selection and does not look at “opportunity cost” related to the current choice, there is potential for infeasibility in the school capacity constraint near the end of the selection process. While the heuristic is likely to yield a feasible solution, the socioeconomic distance may be signi<sup>fi</sup>- cantly higher since it is a secondary criterion, and a current recommendation cannot be examined in terms of future opportunity cost as those future family parameters are not yet known. Therefore, the order in which families present themselves for assistance can have an impact on the quality of the <sup>fi</sup>nal solution.

## 4.2. Greedy location (GL)

If families are more interested in minimizing total distance to socioeconomic support services, then the distance <sup>fi</sup>lter would be applied <sup>fi</sup>rst. First, the system will determine the number of bedrooms that will adequately house the family. Next, the support system will calculate the total socioeconomic distance for this family for each housing alternative. Beginning with the alternative with the best location (lowest distance), the system will recommend the alternative as long as it has a unit available that has at least as many bedrooms as the minimum necessary and is in a school district that has suf<sup>fi</sup>cient capacity for their chil dren (if any). If the <sup>fi</sup>rst alternative is not feasible, the system will move through the remaining alternatives until a suitable one is found or infeasibility is declared (because families may choose units larger than they need, families near the end of the selection order may <sup>fi</sup>nd that no unit of suf<sup>fi</sup>cient size remains). This process will be repeated for each family. A description of the process is as follows.

Test results for the housing recommendation heuristic

<table><tr><td rowspan="4"></td><td colspan="9">Housing surplus</td></tr><tr><td colspan="3">High</td><td colspan="3">Medium</td><td colspan="3">Low</td></tr><tr><td rowspan="2">Avg. % distance above optimal</td><td colspan="2">Infeasible assignments (out of 500 families)</td><td rowspan="2">Avg. % distance above optimal</td><td colspan="2">Infeasible assignments (out of 500 families)</td><td rowspan="2">Avg. % distance above optimal</td><td colspan="2">Infeasible assignments (out of 500 families)</td></tr><tr><td>Max</td><td>Avg</td><td>Max</td><td>Avg</td><td>Max</td><td>Avg</td></tr><tr><td>Greedy size (GS)</td><td>11.76</td><td>3</td><td>.030</td><td>12.20</td><td>4</td><td>.030</td><td>14.02</td><td>8</td><td>0.46</td></tr><tr><td>Greedy location (GL)</td><td>8.14</td><td>3</td><td>.027</td><td>9.91</td><td>4</td><td>.166</td><td>10.38</td><td>20</td><td>6.88</td></tr><tr><td>Greedy hybrid (GH)</td><td>8.47</td><td>3</td><td>.027</td><td>10.07</td><td>4</td><td>.141</td><td>10.81</td><td>18</td><td>4.89</td></tr></table>

1. Set i = 1 (<sup>fi</sup>rst family), all $X _ { i j } = 0 , D _ { t o t a l } = 0 ,$ , and $W D _ { t o t a l } = 0$

2. Calculate necessary bedrooms nb for family i (if family size ≤ 4, then nb = 2; if family size N 4 and $\leq 6 ,$ then nb = 3; if family size N 6, then $n b = 4 )$

3. Set $W D _ { m i n } = \infty \mathrm { a n d } A l t = 0 .$

4. Set $k = 1$ (<sup>fi</sup>rst housing alternative)

5. If no units of size nb or greater exist within alternative $k ,$ or if the school district sd for k does not have capacity for i's children, go to step 9. Otherwise, continue.

6. If the smallest available unit at k has a number of bedrooms N nb, set nb(k) to this number of bedrooms. Otherwise, set nb $( k ) = n b .$

7. Calculate the total distance $D _ { k }$ and the total weighted distance $W D _ { k }$ from alternative k to family i's area of preference, necessary schools, and necessary hospitals, based on family i's stated weights.

8. If $W D _ { j } < W D _ { m i n } ,$ set $W D _ { m i n } = W D$ and Alt = k. Continue.

9. If more housing alternatives exist, set $k = k + 1$ and return to step 5. Otherwise, continue.

10. If Alt = 0, there is no suitable housing for family i. Go to step 14.

11. $\mathsf { L e t t i n g } j = A l t$ , set $X _ { i j } = 1$ . Set $D _ { t o t a l } = D _ { t o t a l } + D _ { j }$ and $W D _ { t o t a l } =$ $W D _ { t o t a l } + W D _ { m i n } .$

12. $X _ { i j } = 1 ,$ and the values of nb(j) and $D _ { j }$ and $W D _ { m i n }$ represents the solution for family i.

13. Reduce the number of available units of size nb(j) within housing alternative j by 1. If family i has school-age children, reduce the capacity at each level within school district sd by the number of children at that school level in family i.

14. If there are more families, set $i = i + 1$ and return to step 2. Otherwise, continue.

15. The set of nonzero $X _ { i j }$ and the values of $D _ { t o t a l }$ and $W D _ { t o t a l }$ represent the solution across all families.

Once again, the order in which families present themselves for assistance will have a large in<sup>fl</sup>uence on the quality of the solution. Because this heuristic focuses <sup>fi</sup>rst and foremost on location distance, and because size (and therefore capacity) is a secondary criterion, infeasibility is possible. However, as long as there is an ample supply of housing, in feasibility is likely not to be problematic.

## 4.3. Greedy hybrid (GH)

Each of the previous recommendation schemes was designed to mimic a possible selection strategy employed by displaced families. However, it is obvious that not all families will have the same priorities among size (cost) and distance. An effective decision support system must be able to consider different priorities among families. We gauge the priorities by asking each family to rank the importance of size and the importance of distance on a scale of 1 to 10. These values become weights in a hybrid scheme used to <sup>fi</sup>nd good compromise recommendations. Methodologies have been developed for comparing alternatives on different criteria, such as Analytical Hierarchy Process [29]. However, schemes such as AHP generally require pairwise comparison among alternatives. This is <sup>fi</sup>ne for smaller problems, but virtually impossible for a problem such as ours. Instead, we follow an approach similar to that of Lee [19], and construct a ratio measure which merges our two criteria into a goodness or <sup>fi</sup>tness measure. Speci<sup>fi</sup>cally, we de<sup>fi</sup>ne the <sup>fi</sup>tness of a solution for the housing situation to be $F _ { i j }$ as follows:

![](/api/attachments/VTZ7AYMG/fulltext/images/53064a3a0b7b94136f6b546739f4167ee9a180c460ffd94801b6a80088271921.jpg)  
Fig. 2. Flowchart for the housing DSS.

![](/api/attachments/VTZ7AYMG/fulltext/images/5d5fca6c45a56b1929ab755d9638b2b03ac20d0b41acc56fb9f84ae319d5bea5.jpg)  
Fig. 3. Result window for the selection DSS.

$$
F _ {i j} = \frac {\omega_ {i 1} W D _ {i j}}{M - \omega_ {i 2} B}
$$

where $\omega _ { i 1 }$ and $\omega _ { i 2 }$ are family i's weights from the ranking process on total socioeconomic distance and bedrooms, respectively; $W D _ { i j }$ is the total weighted distance from alternative j to family i's work, schools, and medical care; B is the number of bedrooms under consideration for family i; and M represents 1 plus the maximum possible value for $\omega _ { i 2 } B .$ In this case, the smaller the value of $F _ { i j } ,$ the better the solution. The heuristic can be described as follows.

1. Set i = 1 (<sup>fi</sup>rst family), all $X _ { i j } = 0$ and $W D _ { t o t a l } = 0$

2. Calculate necessary bedrooms nb for family i (if family size $\leq 4 ,$ then nb = 2; if family size N 4 and ≤ 6, then $n b = 3 ;$ if family size N 6, then nb = 4)

3. Set $F I T _ { m i n } = \infty \mathrm { a n d } A l t = 0 .$

4. Set $k = 1$ (<sup>fi</sup>rst housing alternative)

5. If no units of size nb or greater exist within alternative k, or if the school district sd for k does not have capacity for i's children, go to step 9. Otherwise, continue.

6. If the smallest available unit at k has a number of bedrooms N nb, set nb(k) to this number of bedrooms. Otherwise, set $n b ( k ) = n b$

7. Calculate the total weighted distance $W D _ { k }$ from alternative k to family i's area of preference, necessary schools, and necessary hospitals.

8. Calculate the solution <sup>fi</sup>tness FIT for family i and alternative k using nb(k) and WD and the <sup>fi</sup>tness weights provided by family i. I $\mathsf { f } F I T < F I T _ { m i n } , \mathsf { s e t } F I T _ { m i n } = F I T$ and $A l t = k .$ Continue.

9. If more housing alternatives exist, set k = k + 1 and return to step 5. Otherwise, continue.

10. If Alt = 0, there is no suitable housing for family i. Go to step 14.

11. Letting j = Alt, set X<sub>ij</sub> = 1. Set WD<sub>total</sub> = WD<sub>total</sub> + WD<sub>j</sub>.

12. $X _ { i j } = 1 ,$ , and the values of nb(j) and WD represents the solution for family i.

13. Reduce the number of available units of size nb(j) within housing alternative j by 1. If family i has school-age children, reduce the capacity at each level within school district sd by the number of chil dren at that school level in family i.

14. If there are more families, set $i = i + 1$ and return to step 2. Otherwise, continue.

15. The set of nonzero $X _ { i j }$ and the value of $W D _ { t o t a l }$ represent the solution across all families.

As with the other two heuristics, order of family selection is important, and infeasibility is a possibility. However, this heuristic should provide a good balance between location distance and feasibility, and will better re<sup>fl</sup>ect the preferences of the families.

## 4.4. Comparison of the heuristics

In order to test the selection heuristics, we develop an experiment to control for several important factors. One factor which impacts the performance of the heuristics is the level of housing capacity or availability. We de<sup>fi</sup>ne three levels of housing surplus or oversupply; low, medium, and high. These are an average oversupply of approximately 5% (low), 20% (medium), and 30% (high). The crossing of these three surplus levels with the three heuristics creates the nine major cells in Table 1.

The other important factors are controlled for in the way in which we perform multiple replications within each cell. First, it is important to vary the order in which families are presented for assistance, as this order has a major impact on the outcome. Therefore, we take a family pro<sup>fi</sup>le (group of 500 families) and analyze them according to 100 random orderings. Next, to make sure that the process is generalizable across possible family pro<sup>fi</sup>les, we repeat the process for 10 replications. Within each replication, we generate new values for the distance weights, <sup>fi</sup>tness weights, family size, area of preference, and demographic factors (school-age children, elders, etc.) according to the dataset presented in our hypothetical example. For each replication within each cell, we compute the benchmark optimal solution for minimum distance, and then report the average percentage across these 1000 runs (100 orderings times 10 replications) of the heuristic solution's weighted distance as compared to the minimum “greatergood” distance obtained from the benchmark mathematical programming model. For example, in Table 1, a value of 8.14 in the “Avg. % Distance Above Optimal” column would indicate that, across all runs for that heuristic and housing capacity level, the total weighted distance of the heuristic solution is 8.14% higher than that of the benchmark optimal value. Also, we record the occurrences of infeasibilities (instances where a housing unit of adequate size and/or school capacity does not exist for a family). These generally occur near the end of the selection order and involve a relatively small number of families. From a practical standpoint, these are the families that would require special handling, such as relocation to a more removed site or temporary placement in a FEMA trailer or other non-standard alternative. We report on both the maximum number of infeasibilities out of 500 families that occurred in any ordering across any replication, as well as the average number of infeasibilities out of 500

Several <sup>fi</sup>ndings are apparent from Table 1.

1. Regardless of housing oversupply, GS is always the worst at minimizing the weighted distance in comparison to the “greater-good” benchmark, but is always the best at minimizing infeasible selections. This is not surprising given that housing size is the primary <sup>fi</sup>lter and distance is a secondary <sup>fi</sup>lter.

2. GL is always the best in terms of average percent distance above optimal and the worst (or tied for the worst) in terms of infeasibility.

Again, this is logical given that location is the primary <sup>fi</sup>lter and size is the secondary <sup>fi</sup>lter.

3. GH seems to represent a good compromise. Across all levels of oversupply, GH is better than GS in terms of average percent distance above optimal, and better than GL in terms of minimizing infeasibilities. Also, in the worst case scenario of low housing supply, we only give up a small increase in average percent distance above optimal for GH in comparison to GL (10.81 versus 10.38) in order to reap the bene<sup>fi</sup>ts of lower infeasibility. This is especially important since low housing supply is likely to be the post-disaster norm.

4. Looking at the column for low housing surplus, GH appears to present a good compromise between GS and GL. Also, because it directly incorporates the preferences of the families, it is likely to represent a higher level of satisfaction at the individual family level.

Based on our analysis, it seems reasonable to focus on GH as the selection methodology in our DSS. The next section discusses the structure of the DSS.

![](/api/attachments/VTZ7AYMG/fulltext/images/92c21b538456d07ac764eda0ff966fbffb801038e20a9c49957bbd571568210e.jpg)  
Fig. 4. Detailed description of a suggested alternative.

## 5. The DSS

The <sup>fl</sup>owchart for the housing selection DSS is given in Fig. 2. In the <sup>fi</sup>rst three steps, we collect family information for the current family (size, neighborhood preference, and family structure) and preference information. This is merged with external data on housing availability, school capacity, geo-spatial data on the distances between neighborhoods and alternatives, etc.

This data is used to calculate the top three recommendations for the family using the hybrid heuristic. Basically, the heuristic is run three times, and each time the previous recommendation(s) is removed from consideration. Provided the heuristic yields a feasible alternative, the results are presented in the format shown in Fig. 3.

At this point, the family representative can view the details of the alternatives, as shown in Fig. 4. Fig. 4 presents a textual description of the alternative including distances and typical cost, as well as a spatial diagram of the housing location in relation to preferred neighborhood, preferred hospitals, and schools. As an example, Google Earth's Developer Interface can accept address pairs and draw lines between them during the rendering of a spatial drawing.

After reviewing all alternatives, a family decision maker can change distance or <sup>fi</sup>tness weights and generate new alternatives, or select from the current alternatives. Once a selection is made, the external data is updated to re<sup>fl</sup>ect the lowered capacity at the chosen housing alternative and to re<sup>fl</sup>ect the reduced school capacity, if the family has school-age children.

If there was no feasible alternative from which to choose, the family will be referred to a counselor for assistance in meeting their special needs. This process will be repeated for each family that presents itself for assistance, or until all available housing has been exhausted.

## 6. Conclusions and future research

Interim housing of disaster victims is an enormous problem which is only beginning to be studied. While others have suggested mechanisms for identifying safe and adequate interim housing alternatives, little has been done to address the problem of actually recommending available alternatives to families. We develop a decision support system for recommending housing alternatives to families that takes into account health, educational, and social needs of displaced families and the ability of possible housing alternatives to meet those needs. We <sup>fi</sup>rst develop a benchmark model for <sup>fi</sup>nding the best overall solution which balances needs across all families, and demonstrate its application with a hypothetical example. We believe the benchmark model represents a contribution in that it could be used as a planning tool using general census data to ascertain whether available housing is suf<sup>fi</sup>cient (feasible), and to reveal whether current planning has created alternatives which are likely to be agreeable to displaced families. While this benchmark model is important for establishing what is possible in the sense of the “greater-good,” it is not viable for a real-time decision support system or recommender system where families arrive sequentially and parameters for all of the families are not know a priori.

Next, we develop three heuristics which focus on housing unit size, socioeconomic distance, and a combination of the two. For each heuristic, we compare its results to that of the benchmark model and look at its ability to <sup>fi</sup>nd a good overall (and feasible) set of solutions. Of the three heuristics, the Greedy Hybrid heuristic offered the best balance between minimizing the socioeconomic distance for all families, matching the size of the housing unit to the family needs, and <sup>fi</sup>nding a feasible plan for all families. We believe a contribution of our work lies in the development of the heuristics. Beyond the fact that no one (to our knowledge) has tackled this problem in a systematic manner, we do believe that the hybrid heuristic is novel in the way that it employs a <sup>fi</sup>tness ratio. We have only seen a few other papers which have used this approach, and none within the disaster management area. We believe the Greedy Hybrid heuristic is a very suitable strategy for real-time housing recommendation, and thus we use it as the cornerstone of our decision support system.

While the development of the housing decision support system represents a step forward in addressing the post-disaster housing problem, there are still open issues for future research. Our conversations with our local Emergency Management Of<sup>fi</sup>ce have identi<sup>fi</sup>ed two major issues which remain. The <sup>fi</sup>rst has to do with temporary workers that are brought in after a disaster to help with repair and rebuilding efforts. These workers must be housed, which adds to the demand for housing capacity and may not have been fully accounted for in pre-planning. Also, these workers may bring their families and thus have similar socioeconomic needs as our disaster victims, or they may be unaccompanied and have an entirely different set of needs. Depending on their job and the length of their stay in the area, some housing units might be used as rolling housing where the different trades would come and go in phases as the reconstruction work proceeds. This is certainly an interesting area for further exploration. The second issue deals with coordination among local, state, and federal agencies which may all be participating in support functions. If multiple agencies are involved in housing recommendation, then coordination of the housing supply database is a very important issue. This may also be an area worthy of future attention.

## References

[1] Y. Akcay, H. Li, S. Xu, Greedy algorithm for the general multidimensional knapsack problem, Annals of Operations Research 150 (1) (2007) 17–29.

[2] O. El-Anwar, K. El-Rayes, Post-disaster Optimization of Temporary Housing Efforts, Proc. Of the ASCE Construction Research Congress, 2007.

[3] O. El-Anwar, K. El-Rayes, A. Elnashai, Multi-objective optimization of temporary housing for the 1994 Northridge earthquake, Journal of Earthquake Engineering 12 (S2) (2008) 81–91.

[4] O. El-Anwar, K. El-Rayes, A. Elnashai, Optimizing large-scale temporary housing arrangements after natural disasters, Journal of Computing in Civil Engineering 23 (2) (2009) 110–118.

[5] O. El-Anwar, K. El-Rayes, A. Elnashai, An automated system for optimizing post-disaster temporary housing allocation, Automation in Construction 18 (2009) 983–993.

[6] H. El Nasser, P. Overberg, Census Reveals Plummeting U.S. Birthrates, USA Today, 2011. (available at http://usatoday30.usatoday.com/news/nation/census/2011-06- 03-fewer-children-census-suburbs\_n.htm 2011 (last visited November 2013)).

[7] H. Engelmann, F. Fiedrich, Decision Support for the Members of an Emergency Operation Centre After an Earthquake, Proceedings of the 4th ISCRAM Conference 2007 pp. 317-326 (Delft NL).

[8] FEMA Housing Portal, available at https://asd.fema.gov/inter/hportal/home.htm (last visited November 2013).

[9] FEMA, National Disaster Housing Strategy, U.S. Department of Homeland Security, 2009.

[10] D. Fogli, G. Giovanni, Knowledge-centered design of decision support systems for emergency management, Decision Support Systems 55 (1) (2013) 336–347.

[11] D. Fogli, G. Guida, Enabling Collaboration in Emergency Management Through a Knowledge-based Decision Support System, in: A. Respìcio, F. Burstein (Eds.), Fusing Decision Support Systems into the Fabric of the Context, IOS Press, Amsterdam, Nederland, 2012, pp. 291–302.

[12] B. Friday, Rebuilding Shelter After Natural Disasters: Three Decades of USAID Experience in Latin America and the Caribbean, USAID report, Contract No. PCE-I-00-96- 00008-00, Delivery Order Number 3, , PADCO, Inc., 1999

[13] M. Giacomin, G. Guida, M. Rossi, A. Viola, A Knowledge-based Decision Support System for Crisis Management in the Field of Public Health, Proceedings Workshop on Intelligent Decision Support in Process Environment, 2005, (Siena, Italy).

[14] J. Golec, A contextual approach to the social psychological study of disaster recovery, Journal of Mass Emergencies and Disasters 1 (1983) 255–276.

[15] R.R. Hill, Y.K. Cho, J.T. Moore, Problem reduction heuristic for the 0–1 multidimen sional knapsack problem Computers & Operations Research 39 (2012) 19–26

[16] J. Jenvald, M. Morin, T. Timpka, H. Eriksson, Simulation as Decision Support in Pandemic In<sup>fl</sup>uenza Preparedness and Response, Proceedings of the 4th ISCRAM Conference, 2007, pp. 295–304, (Delft, NL).

[17] G. Kochenberger, B. McCarl, F. Wyman, A heuristic for general integer programming, Decision Sciences 5 (1) (1974) 36–44

[18] A.A. Kuehn, M.J. Hamburger, A heuristic program for locating warehouses, Management Science 9 (1963) 643–666

[19] S. Lee, The role of centrality in ambulance dispatching, Decision Support Systems 54 (2012) 282–291.

[20] J.P. Li, R. Chen, J. Lee, H.R. Rao, A case study of private–public collaboration for humanitarian free and open source disaster management software deployment, Decision Support Systems 55 (1) (2013) 1–11.

[21] R. Loulou, E. Michaelides, New greedy heuristics for the multidimensional 0–1 knapsack problem, Operations Research 27 (6) (1979) 1101–1114

[22] D. Mendonça, G.E.G. Beroggi, W.A. Wallace, Decision support for improvisation during emergency response operations, International Journal of Emergency Management 1 (1) (2001) 30–38

[23] E.W.T. Ngai, T.K.P. Leung, Y.H. Wong, M.C.M. Lee, P.Y.F. Chai, Y.S. Choi, Design and development of a context-aware decision support system for real-time accident handling in logistics, Decision Support Systems 52 (2012) 816–827.

[24] I. Petrakis, C. Hass, M. Bichler, On the impact of real-time information on <sup>fi</sup>eld service scheduling, Decision Support Systems 53 (2012) 282–293.

[25] Project 196320, “An Integrated Decision Support System for Crisis Management”, Supported by Regione Lombardia, Italy, FSE, Misura D4, November 2004–December 2005.

[26] Project 2006203, HEALTHREATS — Integrated Decision Support System for Health Threats and Crises Management, Supported by the European Union, Executive Agency for Health and Consumers, May 2007–September 2010.

[27] R. Quercia, L. Bates, The Neglect of America's Housing: Consequences and Policy Responses, Working Paper 2002-02, Center for Urban and Regional Studies, , University of North Carolina, Chapel Hill, 2002.

[28] W. Raskob, V. Bertsch, J. Geldermann, S. Baig, F. Gering, Demands to and Experience With the Decision Support System RODOS for Off-site Emergency Management in the Decision Making Process in Germany, Proceedings of the 2nd ISCRAM Conference, 2005, pp. 269–278, (Brussels, Belgium).

[29] T.L. Saaty, Decision making with the analytic hierarchy process, International Journa of Services Sciences 1 (1) (2008) 83–98.

[30] S. Senju, Y. Toyoda, An approach to linear programming with 0–1 variables, Management Science 15 (4) (1968) B196–B207.

[31] A. Shlay, Housing in the broader context in the U.S. Housing Policy Debate 6 (3) (1995).

[32] Y. Sun, G.J. Koehler, A location model for a web service intermediary, Decision Support Systems 42 (2006) 221–236.

[33] Y. Toyoda, A simpli<sup>fi</sup>ed algorithm for obtaining approximate solutions to zero–one programming problems, Management Science 21 (12) (1975) 1417–1427.

Terry R. Rakes is the William and Alix Houchens professor of Business Information Technology at Virginia Tech. He received the Ph.D. in Management Science, M.B.A., and B.S.I.E. from Virginia Tech. His research interests are in analytics and big data analysis, text and data min ing, geographic information systems, disaster planning and logistics, information security, and the application of decision support and arti<sup>fi</sup>cial intelligence methodologies to problems in information systems. He has published in Management Science, Decision Sciences, Decision Support Systems, Annals of Operations Research, OMEGA, European Journal of OR, Operations Research Letters, Information and Management, Journal of Information Science, and others.

Jason K. Deane is an associate professor of Business Information Technology in the Pamplin College of Business at Virginia Tech. He received a Ph.D. in Decision and Information Sciences from the University of Florida, and an M.B.A. and B.S. in Business Administration from Virginia Tech. His current research interests are in the areas of arti<sup>fi</sup>cial intelligence, computer-aided decision support systems, information system security, large scale optimization and information retrieval. He has published in such journals as Decision Support Systems, Annals of Operations Research, Information Technology and Management, International Journal of Physical Distribution and Logistics Management, Operations Manage ment Research, and others.

Loren Paul Rees is the Andersen professor of Business Information Technology. He received the Ph.D. in Industrial and Systems Engineering, B.E.E. from Georgia Tech, and M.S.E.E. from the Polytechnic Institute of Brooklyn. Dr. Rees' current research focuses on managerial issues in information technology security; on nonparametric simulation optimization; and on the application of wireless broadband capabilities to rural and/or developing areas. He has pub lished in Naval Research Logistics, IIE Transactions, Decision Sciences, Transportation Research, Journal of American Medical Informatics Association, Journal of the Operational Research Society, Computers and Operations Research, Communications of the ACM, Decision Support Systems, and others.

Gary Fetter is an assistant professor in the College of Business at Valparaiso University. His research interests are in decision modeling, information technology, and operations and supply chain management especially in the area of disaster and extreme events. He received the Ph.D. in Management Science from Virginia Polytechnic Institute and State University and is a member of the Decision Sciences Institute, the Institute for Operations Research and Management Science, and the International Community on Information Systems for Crisis Response and Management.
