---
otero_id: 8920
otero_key: "SFZTRTYH"
title: "A Web-based decision support system with ELECTRE III for a personalised ranking of British universities"
authors: "Christos Giannoulis; Alessio Ishizaka"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.06.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Web-based decision support system with ELECTRE III for a personalised ranking of British universities

Christos Giannoulis <sup>a</sup>, Alessio Ishizaka <sup>b,</sup>⁎

<sup>a</sup> Faculty of Technology, Department of Electronic and Computer Engineering, University of Portsmouth, Anglesea Building, Anglesea Road, Portsmouth PO1 3DJ, United Kingdom <sup>b</sup> Portsmouth Business School, University of Portsmouth, Richmond Building, Portland Street, Portsmouth PO1 3DE, United Kingdom

## a r t i c l e i n f o

Available online 18 June 2009

Keywords: Multi-criteria decision method ELECTRE III University rankings

## a b s t r a c t

Reliance upon multi-criteria decision methods, like ELECTRE III, has increased many folds in the past few years. However, ELECTRE III has not yet been applied in ranking universities. League tables are important because they may have an impact on the number and quality of the students. The tables serve an indication of prestige. This paper describes a three-tier Web-system, which produces a customised ranking of British Universities with ELECTRE III re<sup>fl</sup>ecting personal preferences, where information is uncertain and vague Using this case study, the bene<sup>fi</sup>ts of ELECTRE III in the ranking process are illustrated.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Professor William Cooper is particularly known through his work on DEA (Data Envelopment Analysis) [26]. His paper [17] has been elected as one of the most in<sup>fl</sup>uential papers published in the European Journal of Operational Research. Professor Cooper has applied DEA widely to the performance analysis in the public and private sectors, especially in education. He was the <sup>fi</sup>rst (founding) Dean at Carnegie Mellon University's School of Urban and Public Affairs (now the H.J. Heinz III School of Public Policy and Management, USA) and a founding member of the Graduate School of Industrial Administration at Carnegie Mellon. He always strives for the improvement of the quality in education as it can be seen in his papers [3,5,10,15,18,19].

The evaluation of education with ranking lists of universities has become, over the past few years, increasingly popular. Some examples in United Kingdom are the Times Higher Education, The Complete University Guide, The Guardian University Guide and the Sunday Times University Guide all of which produce leagues tables based on statistical data from the Higher Education Statistical Agency (HESA) and the National Student Survey (NSS). These rankings have a sizeable impact on universities as they may have some indication of prestige and a direct in<sup>fl</sup>uence on the number and quality of applicants. However the ranking of universities does not use rigorous methodologies like ones used in Professor Cooper's work. The methodology used to rank universities is a simple weighted sum, which has several limitations. First, the weights are predetermined with very little, if any, justi<sup>fi</sup>cation of their value. Therefore, it is assumed that the criteria have the same importance (i.e. weight) for everybody. This is clearly not true as each person is different and has different preferences. Moreover, commercial league tables use a simple aggregation, which is compensatory and does not differentiate between universities having strengths in different areas.

This paper has been prepared to celebrate the 95th birthday of Professor Cooper and his motivation to evaluate education with new methods. We have thus developed a new interactive online way to rank universities with the multi-criteria decision method ELECTRE III [42] (http://www.pbs.port.ac.uk/IshizakaA/). As ELECTRE III may be complicated for new users, a simple and an advanced version has been developed. These two versions are user-friendly, free, Web accessible and have tailored functionalities, which is not the case for the old commercial off-the-shelf software supporting the ELECTRE III (http:// www.lamsade.dauphine.fr/english/software.html). However, the commercial software was used to validate the results of our Web decision support tool.

Hereinafter, we will review methods used for rankings universities. In Section 3, the ELECTRE III algorithm is described. Section 4 describes the design and implementation of the decision support tool, and Section 5 evaluates the implemented system. Finally, the concluding section summarises the main points arising from this project.

## 2. Rankings systems

## 2.1. Commercial rankings

Several commercial universities ranking schemes are annually published. Alongside, criticisms of these rankings have also increased [13,34,37,51,53,55]. These leagues tables are based on a weighted sum of performances, which has some methodological problems. As each criterion is measured in a different unit, they need to be transformed to commensurate units in order to be summed together. The problem is that numerous ways of standardising exist (commercial rankings generally uses z-transformation) and they often lead to a different <sup>fi</sup>nal ranking. An example can be found in [39], where the authors emphases that “prior normalization of data is not a neutral operation, and the <sup>fi</sup>nal result of aggregation may well depend on the normalization method used”. The same normalisation problem is also observed in the Analytic Hierarchy Process (AHP), where different normalisations may lead to a rank reversal [7,30]. Moreover, AHP is dif<sup>fi</sup>cult to use with a large volume of data, due to the high number of pairwise comparisons required [29].

![](/api/attachments/SFZTRTYH/fulltext/images/a0ccd2a2115c7ef16cb9d69fd52f61cc78ee6dc094678a39bc5a4483d1757ea1.jpg)  
Fig. 1. Non-dominance in interpretation of DEA radial models. Note: Alternatives a1 and a3 are supported optimal solutions; a2 is an optimal non supported solution, the DEA does not consider a2 as an ef<sup>fi</sup>cient solution because it is not on the ef<sup>fi</sup>cient frontier. This type of problem occurs only in DEA radial models. Non-radial DEA models do not have such a problem. Therefore, a1 becomes ef<sup>fi</sup>cient in the non-radial DEA models.

## 2.2. DEA

Data Envelopment Analysis (DEA) is an often used ranking technique [2,33,44,46,47], which does not require any normalisation. The global score of each Decision Making Unit (DMU) is de<sup>fi</sup>ned as the ratio of the sum of its weighted output levels to the sum of its weighted input levels. The analogy with multi-criteria methods is striking if we replace the name “DMU” with “alternatives”, “outputs” with “criteria to be maximised” and “inputs” with “criteria to be minimised”. The particularity of this method is that weights are not allocated by users or experts; moreover it does not employ a common set of weights for all alternatives. Instead, for each alternative a different set of weights is calculated with a linear optimisation procedure. The aim of the optimisation is to select weights in order to highlight their particular strength. Some constraints are added in order to ensure that when these weights are applied to all other candidates, none of the scores exceed 100%, the perfect ef<sup>fi</sup>ciency. DEA has been widely used to rank universities or schools [1,4–6,9–11,14,16,18,23,25,31,32] and in many other sectors as compiled in [24]. However, there are some limitations to DEA, which are highlighted below:

• “DEA is not designed to select a single winner” [21,52]. DEA identi<sup>fi</sup>es all alternatives that are located on the ef<sup>fi</sup>cient frontier as the best alternatives without distinction. When the list of alternatives is large, the number of ef<sup>fi</sup>cient alternatives may also be large. Further analysis must then be applied to select the best alternative. We know that multiplier restriction method (e.g., cone ratio) has been developed to reduce the number of ef<sup>fi</sup>cient DMUs. It is possible to identify a single best alternative, using DEA [26]. See also [46,47].

• “The ranking of inef<sup>fi</sup>cient alternatives depends upon which DEA model is used for performance evaluation” [12,45]. See [48].

• “A conventional use of DEA does not consider the weakness of some candidates”[45,52]. Any alternative which has the highest score on one criterion is often regarded as ef<sup>fi</sup>cient, irrespectively of how low it scores on all other criteria. This issue is due to the <sup>fl</sup>exibility in allocating weights in its conventional use, which allows DEA to focus on a few criteria, not putting importance on the others. Note that a new type of DEA [46,47] does not have such a problem. See also [48].

• “DEA becomes less discriminating as more information is provided” [52]. This problem derives from the critic above. The likelihood that one alternative scores well on one criterion increases with the number of criteria. Thus, unlikely other decision supports methods, the more criteria you have, the less discriminating the method becomes.

• Alternatives that are not on the ef<sup>fi</sup>cient frontier are not considered as candidates for the <sup>fi</sup>nal selection [12]. The conventional use of DEA does not recognise optimal non supported alternatives as ef<sup>fi</sup>cient. See Fig. 1.

• All alternatives on the ef<sup>fi</sup>cient frontier serve as a ranking basis for all other alternatives even if some non-ef<sup>fi</sup>cient alternatives may be more attractive than ef<sup>fi</sup>cient alternatives [12]. See Fig. 2.

There is an extensive literature which describes techniques to improve the DEA. They generally require more information from the user. The most used techniques use value judgements to constrain weight (multiplier) <sup>fl</sup>exibility [54]. However the exercise of bounding the weights is not trivial as restrictions are subjective and depends on the measurement units of the different inputs and outputs [45]. In order to help the user, visual methods have been developed [8,23]. These methods are time-consuming and dif<sup>fi</sup>cult to use with a large amount of inputs and outputs. Of course, this study is fully aware of the recent study [48] that restricts weight (multiplier) by strong complementary slackness condition. Hence, the approach does need any subjective information for weight restriction.

## 2.3. Ranking with pseudo-criteria

The multi-criteria ranking methods described above, alongside the shortcomings described, are not adapted for uncertain, indeterminate and imprecise data, as explained below:

• Imprecise criteria, because of the dif<sup>fi</sup>culty of determining them: students evaluate some criteria (e.g. “Student satisfaction”, “Graduate prospects”) for the university, where they are studying but judgements are made without a common reference with the other universities [13].

• Indeterminate criteria, because the method for evaluating the criteria is selected relatively arbitrarily between several possible de<sup>fi</sup>nitions. For example, does the “Staff/student ratio” incorporate part-time lecturers and part-time students? How is spending divided between the criteria “Academic Service Spend” and “Facilities Spend”?

![](/api/attachments/SFZTRTYH/fulltext/images/9ab76aa56411d93a45eac77a30408f3addfac6bf93d290d299111a6d75e16882.jpg)  
Fig. 2. Importance among alternatives in DEA. Note: Alternatives a1, a2 and a3 are on the ef<sup>fi</sup>cient frontier serve a ranking basis for a4 in the DEA radial model with the assumption of convexity on ef<sup>fi</sup>ciency frontier. The assumption excludes the alternative a4. The alternative is on a higher linear or convex indifference utility curve. The type o problem does not occur in DEA non-radial models. It is true that DEA needs to incorporate information for consensus building among decision makers.

• Uncertain criteria, because the measured values refer only to a point in time and some values vary over time. For example: the “Employability” of a university's graduates depends on the economic situation. The “Investments in facilities” may not be uniformly distributed over time.

The ELECTRE III allows imprecise, indeterminate and uncertain criteria inherent to complex human decision processes by relying on the use of pseudo-criteria and indifference and preference thresholds. See Section 3. Furthermore, very bad performance on one criterion may not be compensated by good scores on the other criteria, depending on the veto threshold. ELECTRE III has been widely used in ranking problems, for instance in ranking the stocks for investment selection [28], for choosing a sustainable demolition waste management strategy [41], for the selection of energy systems [38], for ranking urban stormwater drainage [35] or for housing evaluation [36] but it has not yet been applied for ranking universities.

## 3. ELECTRE III

## 3.1. Introduction

ELECTRE III relies upon the construction and the exploitation of the outranking relations. The two distinct phases are depicted in Fig. 3:

a) Construction of the outranking relation: Alternatives are pairwise compared (A,B). Each pairwise comparison is characterised by an outranking relation. To say that “alternative A outranks alternative B” means that “A is at least as good as B”. Therefore three outranking relations exists: A is “indifferent”, “weakly preferred” or “strictly preferred” to B depending on the difference between the performance of the alternatives and the thresholds given by the user. See Section 3.2.

b) Exploitation of the outranking relation: Two pre-rankings are then constructed with two antagonist procedures (ascending and descending distillation). The combination of the two pre-ranking gives the <sup>fi</sup>nal ranking. See Section 3.3.

## 3.2. Building the outranking relations

## 3.2.1. Pseudo-criteria

True criteria, which are the simplest and traditional form of criterion, do not have thresholds. Only the difference between the scores on the criteria is used to determine which option is preferred. In order to take into account imprecision, uncertainty and indetermination in complex decision problems, pseudo-criteria are used. The indifference q and preference p thresholds allow the construction of a pseudo-criterion. Thus, three relations between alternatives A and B can be considered:

![](/api/attachments/SFZTRTYH/fulltext/images/397e13aca9590ec070cdadcf08049fd4f112e039eded3632940830a3c3444a9a.jpg)  
Fig. 3. ELECTRE III process <sup>fl</sup>ow.

a) A and B are indifferent if the difference between the performance of the two alternatives is below the indifference threshold:

$$
A \mid B \leftrightarrow z (A) - z (B) \leq q\tag{1}
$$

where z(X): performance of the alternative X q: indifference threshold

b) A is weakly preferred to B if the difference between the performance of the two alternatives is in between the indifference and the preference threshold:

$$
A \mathbf {Q} B \leftrightarrow q <   z (A) - z (B) \leq p\tag{2}
$$

where z(X): performance of the alternative X q: indifference threshold p: preference threshold of the alternative

c) A is strictly preferred to B if the difference between the performance of the two alternatives is higher than the preference threshold:

$$
A \mathbf {P} B \leftrightarrow z (A) - z (B) \geq p\tag{3}
$$

where z(X): performance of the alternative X. p: preference threshold of the alternative.

## 3.2.2. Concordance index

The concordance index (Eq. (4)) indicates the truthfulness of the assertion “A outranks $B ^ { \prime \prime } \left( A \ S B \right) ^ { 1 } . C = 1$ indicates the full truthfulness of the assertion and C=0 indicates that the assertion is false. The graphical representation is given in Fig. 4.

$$
C (A, B) = \frac {1}{w} \sum_ {i = 1} ^ {n} w _ {i} c _ {i} (A, B)\tag{4}
$$

where $\begin{array} { r } { W { = } \sum _ { i = 1 } ^ { n } w _ { i } } \end{array}$

$$
c _ {i} (A, B) = \left\{ \begin{array}{l l} 1 & \text { if } z _ {i} (B) - z _ {i} (A) \leq q _ {i} \\ \frac {p _ {i} (z _ {i} (A)) + z _ {i} (A) - z _ {i} (B)}{p _ {i} (z _ {i} (A)) - q _ {i} (z _ {i} (A))} & \text { if } q _ {i} <   z _ {i} (B) - z _ {i} (A) <   p _ {i} \\ 0 & \text { if } z _ {i} (B) - z _ {i} (A) \geq p _ {i} \end{array} \right.\tag{5}
$$

Here,

w : weight of the criterion i n: number of criteria z (X): performance of the alternative X as regards to the criterion i q : indifference threshold for the criterion i p : preference threshold of the alternative on the criterion i

## 3.2.3. Discordance index

If the difference of performances between the alternative A and B, on a criterion i, is higher than the veto threshold $\nu _ { i } ,$ it is cautious to refuse the assertion “A outranks B”. The discordance index for

Table 1

![](/api/attachments/SFZTRTYH/fulltext/images/470e06faf584e8066d044230a26e17b8f4723bac5ea0f15d0323c2f22d4d1d59.jpg)  
Fig. 4. Concordance Index between alternatives A and B. Note: Zone $1 . z _ { \mathrm { i } } ( B ) - z _ { \mathrm { i } } ( A ) \leq q _ { \mathrm { i } } ,$ the alternatives A and B are indifferent, which means a concordance on the assertion “A outranks B”. Zone 2: $q _ { \mathrm { i } } { < } z _ { \mathrm { i } } ( B ) - z _ { \mathrm { i } } ( A ) { < } p _ { \mathrm { i } }$ the alternative B is weakly preferred to A, which means a partial concordance on the assertion “A outranks B”. Zone $3 \colon Z _ { \mathrm { i } } ( B ) -$ $z _ { \mathrm { i } } ( A ) { \geq } p _ { \mathrm { i } } ,$ the alternative B is strictly preferred to A, which means a null-concordance on the assertion “A outranks B”.

each criterion i is given in (Eq. (6)). Fig. 5 shows the graphical representation.

$$
D _ {i} (A, B) = \left\{ \begin{array}{l l} 0 & \text { if } z _ {i} (B) - z _ {i} (A) \leq p _ {i} \\ \frac {z _ {i} (B) - [ z _ {i} (A) + p _ {i} ]}{v _ {i} - p _ {i}} & \text { if } p _ {i} <   z _ {i} (B) - z _ {i} (A) \leq v _ {i} \\ 1 & \text { if } z _ {i} (B) - z _ {i} (A) \geq v _ {i} \end{array} \right.\tag{6}
$$

Here,

z<sub>i</sub>(X): performance of the alternative X as regards to the criterion i. p : preference threshold of the alternative on the criterion i. v : veto threshold for the criterion i.

## 3.2.4. Degree of credibility

Considering the concordance (Eq. (4)) and discordance indices $\left( \operatorname { E q . } \left( 6 \right) \right)$ , the degree of credibility (Eq. (7)) indicates if the outranking hypothesis is true or not. If the concordance index (Eq. (4)) is higher or equal to the discordance index of all criteria (Eq. (6)), then the degree of credibility (Eq. (7)) is equal to the concordance index (Eq. (4)). If the concordance index (Eq. (4)) is strictly below the discordance index (Eq. (6)), then the degree of credibility (Eq. (7)) is equal to the concordance index (Eq. (4)) lowered in direct relation to the importance of those discordances.

![](/api/attachments/SFZTRTYH/fulltext/images/a2d2d912f0fdecfed68921d6818aa10b0f07ce53d8943300fe196993d38a0e94.jpg)  
Fig. 5. Discordance Index between alternatives A and B. Note: Zone $1 : z _ { \mathrm { i } } ( B ) - z _ { \mathrm { i } } ( A ) \leq p _ { \mathrm { i } } ,$ the alternatives B is weakly preferred to A, which means no-discordance on the assertion “A outranks B”. Zone $2 \colon p \mathrm { i } { < } z \mathrm { i } ( B ) { - } z \mathrm { i } ( A ) { < } \nu \mathrm { i } ,$ the alternative B is strictly preferred to A, which means a weak discordance on the assertion “A outranks B”. Zone 3: $z _ { \mathrm { i } } ( B ) - z _ { \mathrm { i } } ( A ) { \geq } \nu _ { \mathrm { i } } ,$ , the difference between A and B exceed the veto threshold, which means a total discordance on the assertion “A outranks B”

Performance matrix of universities (U1–U6).

<table><tr><td>Alternatives</td><td>Academic services spend</td><td>Completion</td><td>Entry standards</td><td>Facilities spend</td><td>Good honours</td></tr><tr><td>U1</td><td>947</td><td>79</td><td>400</td><td>228</td><td>69.7</td></tr><tr><td>U2</td><td>1406</td><td>64</td><td>350</td><td>204</td><td>47.6</td></tr><tr><td>U3</td><td>677</td><td>90</td><td>300</td><td>349</td><td>61.8</td></tr><tr><td>U4</td><td>561</td><td>65</td><td>247</td><td>188</td><td>52.3</td></tr><tr><td>U5</td><td>1006</td><td>88</td><td>352</td><td>437</td><td>65.8</td></tr><tr><td>U6</td><td>765</td><td>77</td><td>280</td><td>198</td><td>55.6</td></tr></table>

$$
S (A, B) = \left\{ \begin{array}{l l} C (A, B) & \text { if } D _ {i} (A, B) \leq C (A, B) \forall i \\ C (A, B) \cdot \Pi_ {i \in J (A, B)} \frac {(1 - D _ {i} (A , B))}{(1 - C (A , B))} & \text { otherwise } \end{array} \right.\tag{7}
$$

where J(A,B) is the set of criteria for which $D _ { i } ( A , B ) { > } C ( A , B )$

Then, the degrees of credibility are gathered in a credibility matrix.

Example 1. In order to illustrate the ranking process of ELECTRE III, we will use in following example with six universities and <sup>fi</sup>ve criteria. See Table 1.

For each criterion of Table 1, thresholds and criteria weights are determined by the user. See Table 2.

After calculation of the concordance and discordance indexes, the degrees of credibility are constructed and gathered in the credibility matrix. See Table 3. It can be seen that the two degrees of credibility, attached at each pair of alternatives (one in each way) does not produce a symmetric credibility matrix. The next step is to exploit this matrix. See Section 3.3.

## 3.3. Distillation procedures

From the credibility matrix, a graph can be drawn. Each alternative is linked with each other alternative with two arrows, one each way, indicating the credibility index. For a large number of alternatives, the graph is highly complex. An automated procedure, named distillation, must be used to rank the alternatives. The name distillation has been chosen for the analogy with alchemists, who distil mixtures of liquid to extract a magic ingredient. The algorithm for ranking all alternatives yields two pre-orders.

The <sup>fi</sup>rst pre-order is obtained with a descending distillation, selecting the best-rated alternatives initially and <sup>fi</sup>nishing with the worst. The best alternatives are extracted from the whole set by applying very stringent rules (Eq. (8)). In this sub-set, the best alternatives are selected by applying less restrictive rules (Eq. (10)) (same previously used rules would not bring a different result). The procedure continues with incrementally lesser restrictive rules and incrementally smaller sub-sets of alternatives. The procedure terminates when only one alternative remains or a group of alternatives that cannot be separated. The second distillation uses the same process but on the original set of alternatives amputated from the best alternative(s) resulting from the <sup>fi</sup>rst distillation. Thus, a new sub-set is obtained at each distillation, which contains the best alternative(s) of the remaining set. At each distillation, the extracted alternative(s) will be ranked on a lower position.

Thresholds and criteria weights de<sup>fi</sup>ned by the user.

<table><tr><td>Criterion</td><td>Academic services spend</td><td>Completion</td><td>Entry standards</td><td>Facilities spend</td><td>Good honours</td></tr><tr><td>Indifference (q)</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.05</td></tr><tr><td>Preference (p)</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td></tr><tr><td>Veto (v)</td><td>0.4</td><td>0.5</td><td>0.4</td><td>0.3</td><td>0.4</td></tr><tr><td>Weight (w)</td><td>0.1</td><td>0.3</td><td>0.3</td><td>0.2</td><td>0.1</td></tr></table>

Table 3 Credibility matrix.

<table><tr><td></td><td>U1</td><td>U2</td><td>U3</td><td>U4</td><td>U5</td><td>U6</td></tr><tr><td>U1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>U2</td><td>0</td><td>1</td><td>0</td><td>0.97</td><td>0</td><td>0.62</td></tr><tr><td>U3</td><td>0.0053</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0.97</td></tr><tr><td>U4</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0.22</td></tr><tr><td>U5</td><td>0.88</td><td>0.11</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>U6</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

Table 4  
First round of the quali<sup>fi</sup>cation.

<table><tr><td></td><td>U1</td><td>U2</td><td>U3</td><td>U4</td><td>U5</td><td>U6</td></tr><tr><td>Outranks</td><td>U4, U6</td><td>U4</td><td>U4, U6</td><td>—</td><td>U1, U3, U6</td><td>U4</td></tr><tr><td>Strength</td><td>2</td><td>1</td><td>2</td><td>0</td><td>3</td><td>1</td></tr><tr><td>Weakness</td><td>1</td><td>0</td><td>1</td><td>4</td><td>0</td><td>3</td></tr><tr><td>Qualification</td><td>1</td><td>1</td><td>1</td><td>-4</td><td>3</td><td>-2</td></tr></table>

As each alternative is linked with each other by two arrows, one each way, but not necessarily with a symmetric credibility index, a second pre-order is constructed with an ascending distillation. In this case, the worst rated alternatives are selected <sup>fi</sup>rst and the distillation terminates with the assignment of the best alternative(s).

For the distillation, the condition needed to state that an alternative A is preferred to B is de<sup>fi</sup>ned as follow: an alternative A is preferred to B if the degree of credibility of “A outranks B” is higher than a threshold $\lambda _ { 2 }$ and signi<sup>fi</sup>cantly higher than the degree of credibility “B outranks A” (Eq. (8)).

$$
S (A, B) > \lambda_ {2} \text { AND } S (A, B) - S (B, A) > s (\lambda_ {0})\tag{8}
$$

where $\lambda _ { 2 }$ is the largest credibility index, which is just below the cutoff level $\lambda _ { 1 }$ as follows:

$$
\lambda_ {2} = \max _ {\{s (A, B) \leq \lambda_ {1} \}} S (A, B) \quad \forall \{A, B \} \in G\tag{9}
$$

where G is the set of alternatives. $\lambda _ { 1 }$ is the following cut-off level:

$$
\lambda_ {1} = \lambda_ {0} - s (\lambda_ {0})\tag{10}
$$

where $\lambda _ { 0 }$ is the highest degree of credibility in the following credibility matrix:

$$
\lambda_ {0} = \max _ {A, B \in G} S (A, B)\tag{11}
$$

and $s ( \lambda _ { 0 } )$ is the following discrimination threshold:

$$
s (\lambda_ {0}) = \alpha + \beta \cdot \lambda_ {0}\tag{12}
$$

We use α=0.3 and $\beta = - 0 . 1 5$ because the two values are recommended values from [43].

![](/api/attachments/SFZTRTYH/fulltext/images/c67b88f28785c45d406052480db46991303aa78514acd1f355dc7fadbd4ed080.jpg)  
Fig. 6. Descending and ascending distillation pre-orders of 6 Universities (U1–U6).

Table 5 Ranking matrix.

<table><tr><td></td><td>U1</td><td>U2</td><td>U3</td><td>U4</td><td>U5</td><td>U6</td><td>Sum  $P^{+}$ </td></tr><tr><td>U1</td><td>-</td><td>R</td><td>I</td><td> $P^{+}$ </td><td> $P^{-}$ </td><td> $P^{+}$ </td><td>2</td></tr><tr><td>U2</td><td>R</td><td>-</td><td>R</td><td> $P^{+}$ </td><td> $P^{-}$ </td><td> $P^{+}$ </td><td>2</td></tr><tr><td>U3</td><td>I</td><td>R</td><td>-</td><td> $P^{+}$ </td><td> $P^{-}$ </td><td> $P^{+}$ </td><td>2</td></tr><tr><td>U4</td><td> $P^{-}$ </td><td> $P^{-}$ </td><td> $P^{-}$ </td><td>-</td><td> $P^{-}$ </td><td> $P^{-}$ </td><td>0</td></tr><tr><td>U5</td><td> $P^{+}$ </td><td> $P^{+}$ </td><td> $P^{+}$ </td><td> $P^{+}$ </td><td>-</td><td> $P^{+}$ </td><td>5</td></tr><tr><td>U6</td><td> $P^{-}$ </td><td> $P^{-}$ </td><td> $P^{-}$ </td><td> $P^{+}$ </td><td> $P^{-}$ </td><td>-</td><td>1</td></tr></table>

With successive distillations, the cut-off level $\lambda _ { 1 }$ is progressively reduced, which makes the condition weaker and it is much easier for A to be preferred than B. However the discrimination threshold contains some arbitrariness as the recommended values α and β are empirical values [50]. Other values could be used, which may slightly change the ranking.

## 3.4. Extraction

When A outranks B, A is given the score +1 (strength) and B is given −1 (weakness). For each alternative, the individual strengths and weakness are added together to give the <sup>fi</sup>nal quali<sup>fi</sup>cation score. Within the descending distillation, the alternative with the highest quali<sup>fi</sup>cation score is assigned to a rank and removed from the credi bility matrix. The process is repeated with the remaining alternatives until all alternatives are ranked.

In the case of several alternatives with the same quali<sup>fi</sup>cation score, the process is repeated within this subset until either an alternative has a higher quali<sup>fi</sup>cation score or the highest degree of credibility $\lambda _ { 0 }$ is equal to 0, which means that it is not possible to decide between the remaining options in the subset and therefore they are declared indifferent.

The ascending distillation procedure works in a similar way to the descending distillation with the exception that the procedure assigns the alternative having the lowest quali<sup>fi</sup>cation score.

Example 2. From the credibility matrix (Table 3), the highest credibility degree is $\lambda _ { 0 } = 1$ and we can calculate $\lambda _ { 1 } = 1 - ( 0 . 3 – 0 . 1 5 \cdot 1 ) = 0 . 8 5$ and therefore $\lambda _ { 2 } = 0 . 6 6$ . The <sup>fi</sup>rst quali<sup>fi</sup>ed university is U5. See Table 4.

The distillation is repeated with the <sup>fi</sup>ve remaining universities. Then, the same process is applied for the ascending distillation. See Fig. 6.

## 3.5. Final ranking

The <sup>fi</sup>nal ranking is obtained through the combination of the two pre-orders. See Section 3.4. The results from the partial pre-orders are aggregated into the ranking matrix. We have four possible cases:

i. A is higher ranked than B in both distillations or A is better than B in one distillation and has the same ranking in the other distillation then A is better than B: $A \ \mathbf { P } ^ { + } \ B$

![](/api/attachments/SFZTRTYH/fulltext/images/66dc0cc24c988f80fa72e602fcd6a18372f56de9802801e3ae00674390e50dcf.jpg)  
Fig. 7. Final ranking.

![](/api/attachments/SFZTRTYH/fulltext/images/1c015cdeebfee6b965ec374b1017e7370c59a938464be2dc7be53922e6f43c35.jpg)  
Fig. 8. Three-tier architecture.

ii. A is higher ranked than B in one distillation but B is better ranked than A the other distillation then A is incomparable to B: A R B.

iii. A has the same ranking than B in both distillations then A is indifferent to B: A I B.

iv. A is lower ranked than B in both distillations or A is lower ranked than B in one distillation and has the same rank in the other distillation then A is worst than B: $A \Gamma ^ { - } B .$

The <sup>fi</sup>nal ranking is obtained by adding the number of P<sup>+</sup>. In case of tie, the comparison between the two alternatives with the same score decides between an indifferent or incomparable relation See Example 3.

Example 3. If we consider the two pre-orders of Fig. 6, the resulting ranking matrix is given in Table 5:

The <sup>fi</sup>nal ranking is given in Fig. 7, where it can be seen that U1, U2 and U3 have the same scores but U1 and U3 are indifferent and U2 is incomparable to the two other alternatives.

## 4. Overview of the decision support system

## 4.1. Introduction

The system architecture is three-tier as shown in Fig. 8. It divides the functionality into independent logical layers, each one responsible for different operations of the application and opaque to the other layers.

The <sup>fi</sup>rst layer runs on standard Web browsers. In this tier, the users enter their weighted criteria and related thresholds for the ranking of universities and receive back a personalised ranking. The middle tier contains the Web server, where the ELECTRE III method runs as described in Section 3. Its implementation uses an oriented object design with C#. This layer is independent from the other and therefore can be reusable or upgradable for other decision problems. The bottom layer stores the performance of the universities, which are those used by The Complete University Guide. See Table 6. The Times Higher Education uses the same criteria with the exception that it merges the criteria “Academic Services Spend” and “Facilities Spend”

Table 6  
Criteria used for the ranking of universities [49].

<table><tr><td>Criterion</td><td>Description</td></tr><tr><td>Student satisfaction</td><td>Evaluation of students on the teaching quality.</td></tr><tr><td>Research assessment</td><td>Average quality of the research undertaken.</td></tr><tr><td>Entry standards</td><td>Average UCAS tariff score of new students under the age of 21.</td></tr><tr><td>Staff/student ratio</td><td>Average staffing level.</td></tr><tr><td>Academic services spend</td><td>Expenditures per student in all academic services.</td></tr><tr><td>Facilities spend</td><td>Expenditures per student on staff and student facilities.</td></tr><tr><td>Good honours</td><td>Percentage of graduates achieving a first or upper second class honours degree.</td></tr><tr><td>Graduate prospects</td><td>Employability of a university&#x27;s graduates.</td></tr><tr><td>Completion</td><td>Completion rate of those studying at the university.</td></tr></table>

in one criterion: “Services & Facilities Spend”. The selection of these criteria may be considered controversial. They have been retained in our study because it allows a comparative evaluation of our system with the existing ones (Section 5). However, users are not obliged to select all criteria. In the next section, we discuss the user interface.

## 4.2. User interface

## 4.2.1. Introduction

The user interface is very important, as it is the link between a person and the system. Because users of this support decision system are unlikely to know ELECTRE III, we have implemented a simple version for them and an advanced version for more experienced users. The goal is to attract users with the simple version and then upgrade them to the advance version. Both versions are based on a wizard style with <sup>fi</sup>ve steps easily to follow (start page, criteria selection, weights settings, threshold settings and ranking display). The algorithm used is the same for the two versions (see Section 3), only the user interface and the required values differs.

## 4.2.2. Simple version

The simple version is created for unfamiliar users of the ELECTRE III method or for users wishing to see the universities rankings quickly. As a verbal scale is intuitively appealing, user-friendly and more common in our everyday lives, it has been preferred in this version for the criteria weights and thresholds. The drawback of the userfriendliness is that some arbitrary choice must be made, in this case how the verbal scale is converted to numbers. Table 7 shows the conversion for the weights (scale 2–10) and the indifference thresholds (multiplicative factor 0.2–1).

In order to minimise the number of inputs required, we have used the double threshold model, where only the indifference threshold is required. The value of the veto preference threshold is the double of the value of the preference threshold, which is the double of the value of the indifference threshold. See Fig. 9. It is an arbitrary choice used in other applications [40], which allows a gain of time and an increase of the usability.

## 4.2.3. Advanced version

The advanced version is aimed at users who are or who become familiar with the ELECTRE III. In contrast with the simple version, where

## Table 7

Conversion verbal to numerical scale

<table><tr><td>Verbal scale</td><td>Weights</td><td>Indifference thresholds</td></tr><tr><td>Very low</td><td>2</td><td>0.2</td></tr><tr><td>Low</td><td>4</td><td>0.4</td></tr><tr><td>Medium</td><td>6</td><td>0.6</td></tr><tr><td>High</td><td>8</td><td>0.8</td></tr><tr><td>Very high</td><td>10</td><td>1</td></tr></table>

You are in: Home : Rankings

1. Criteria : 2. Weights : 3. Thresholds : 4. My Rankings

![](/api/attachments/SFZTRTYH/fulltext/images/063f80f3d78b2d52f87b87e9b7050fe957f9059181f0bd10119b7fb59beb78b1.jpg)  
Fig. 9. Simple version with verbal inputs.

there is no <sup>fi</sup>xed scale nor for weights neither for thresholds. Users can enter weights on the numerical scale of their choice (e.g.1–10 or 1–100). The thresholds are de<sup>fi</sup>ned with a multiplicative parameter a and an additive parameter b. See Fig. 10. For example, suppose that the user select b=15 and a=0.1 and the performance of alternative X is 100. All alternatives with a performance 100±25 (25=15+100·0.1) are indifferent to the alternative X.

4.2.4. Final ranking

The commercial software for ELECTRE III uses a graph for representing the results. It allows the distinction between indifferent and incomparable. However, this representation is not possible with a large number of alternatives, as it is very dif<sup>fi</sup>cult to read the results. Our solution uses a table to display the ranking of the 113 universities. It can seen that rankings depend highly from the criteria and weights

![](/api/attachments/SFZTRTYH/fulltext/images/806fc5a33d36762b91b8d53e649a3f44100edb328c7ecbc568984e2d3fdc00e9.jpg)

## Multiple Criteria UK Universities Rankings

Contact Help

You are in: Home : Rankings

We need your feedback. Please, spend a minute to participate to our survey.

1. Criteria : 2. Weights : 3. Thresholds : 4. My Rankings

## Your university rankings are:

<table><tr><td>Rank</td><td>Institution</td><td>Student Satisfaction</td><td>Research Assessment</td><td>Entry Standards</td></tr><tr><td>1</td><td>Cambridge</td><td>4.2</td><td>6.6</td><td>530</td></tr><tr><td>2</td><td>Oxford</td><td>4</td><td>6.5</td><td>514</td></tr><tr><td>3</td><td>London School of Economics</td><td>3.8</td><td>6.4</td><td>473</td></tr><tr><td>3</td><td>Imperial College</td><td>3.7</td><td>6.4</td><td>473</td></tr><tr><td>5</td><td>St Andrews</td><td>4.1</td><td>5.7</td><td>471</td></tr><tr><td>6</td><td>Edinburgh</td><td>3.6</td><td>5.6</td><td>466</td></tr><tr><td>7</td><td>Warwick</td><td>3.8</td><td>6</td><td>452</td></tr><tr><td>7</td><td>Durham</td><td>3.8</td><td>5.7</td><td>448</td></tr><tr><td>9</td><td>University College London</td><td>3.8</td><td>6</td><td>440</td></tr><tr><td>10</td><td>York</td><td>3.8</td><td>5.8</td><td>429</td></tr><tr><td>10</td><td>Bath</td><td>3.8</td><td>5.7</td><td>430</td></tr><tr><td>10</td><td>Bristol</td><td>3.7</td><td>5.7</td><td>435</td></tr><tr><td>10</td><td>Manchester</td><td>3.6</td><td>5.7</td><td>414</td></tr><tr><td>10</td><td>Dundee</td><td>3.8</td><td>5.1</td><td>472</td></tr><tr><td>15</td><td>Kings College London</td><td>3.8</td><td>5.5</td><td>408</td></tr><tr><td>15</td><td>Glasgow</td><td>3.8</td><td>5.2</td><td>430</td></tr></table>

Fig. 11. Final customised ranking. Note: In this case, the universities of York, Bath, Bristol, Manchester and Dundee are all ranked 10. The <sup>fi</sup>rst four are indifferent (in grey) and the last one is incomparable (in yellow).

## Multiple Criteria UK Universities Rankings

Contact Help

We need your feedback.

Please, spend a minute to

participate to our survey

You are in: Home : Rankings

## 1. Criteria :2. Weights : 3. Thresholds : 4. MyRankings

## Your university rankings are:

<table><tr><td>Rank</td><td>Institution</td><td>Student Satisfaction</td><td>Student-Staff Ratio</td><td>Completion</td></tr><tr><td>1</td><td>Lampeter</td><td>3.8</td><td>26.3</td><td>77</td></tr><tr><td>2</td><td>Leeds Metropolitan</td><td>3.5</td><td>24.2</td><td>83</td></tr><tr><td>3</td><td>Lincoln</td><td>3.7</td><td>23.7</td><td>84</td></tr><tr><td>3</td><td>London South Bank</td><td>3.7</td><td>25.7</td><td>72</td></tr><tr><td>5</td><td>Greenwich</td><td>3.6</td><td>23.7</td><td>80</td></tr><tr><td>6</td><td>York St. John</td><td>3.7</td><td>22.7</td><td>85</td></tr><tr><td>7</td><td>Bath Spa</td><td>3.9</td><td>21.7</td><td>86</td></tr><tr><td>8</td><td>Edge Hill</td><td>3.8</td><td>22.1</td><td>78</td></tr><tr><td>9</td><td>Roehampton</td><td>3.7</td><td>21.5</td><td>80</td></tr><tr><td>9</td><td>Bedfordshire</td><td>3.8</td><td>21.7</td><td>75</td></tr><tr><td>11</td><td>University of the Arts - London</td><td>3.4</td><td>21</td><td>87</td></tr><tr><td>12</td><td>Sheffield Hallam</td><td>3.6</td><td>20.6</td><td>85</td></tr><tr><td>12</td><td>Cumbria</td><td>3.5</td><td>21.2</td><td>76</td></tr><tr><td>14</td><td>Middlesex</td><td>3.5</td><td>22.9</td><td>72</td></tr></table>

Fig, 12. Additional comparison in final customised ranking, Note: Compared with Fig, 11. other criteria and weights can lead to a very different ranking

Table 8  
Status of ranked universities.

<table><tr><td>Status</td><td>Colour</td><td>Description</td></tr><tr><td>Normal</td><td>No colour</td><td>One university per rank.</td></tr><tr><td>Indifferent</td><td>grey</td><td>Two or more universities have the same rank and are indifferent.</td></tr><tr><td>Incomparable</td><td>yellow</td><td>Two or more universities have the same rank and are incomparable.</td></tr></table>

selected by the user. See Figs. 11 and 12. The distinction between indifferent and incomparable universities is made with colours. See Table 8.

## 5. Evaluation

There were two types of evaluation that were conducted: a questionnaire and an observation of users. We sent a questionnaire by email to 800 students of our university, as the application has been conceived mainly to help students in the selection of a university. They were asked to visit the Web-system and answer an anonymous questionnaire. This approach was selected in order that students can complete the questionnaire where, when and only if they want it. The disadvantage of this unpressured voluntary exercise is a low participation: 20 participants (2.5% response rate). However, the collected data gives us some signi<sup>fi</sup>cant indications.

Eighty percent of the respondents claimed that the university ranking was of interest to them but only 55% have already visited a Website providing this type of ranking. This observation is in line with past researches [22,27] indicating that students do not rely on commercial rankings in choosing their university in UK. Only one participant knew ELECTRE III before. Fifty percent of the participants used only the simple version, 20% of the participants used only the advanced version and 30% used both versions. Users, even those unfamiliar with ELECTRE III, were able to understand and appreciate the working of the system. When they were asked to assess the Websystem (Figs. 13 and 14), the results clearly indicate that the system was helpful and better than the other current solutions.

For the second evaluation, a group of 10 masters' students were observed. All students <sup>fi</sup>rst used the simple version, which is easier and selected by default on the welcome page. At the beginning, some students asked the purpose of the thresholds. Then after, they found the system easy and straightforward to use. All students rated the system far superior to the current commercial rankings as the user can select the criteria, their allocated weight and it returns more information (e.g. indifferent and incomparable universities). Finally, they encouraged the developers to implement a similar system ranking universities by specialities (like business schools or engineering faculties).

![](/api/attachments/SFZTRTYH/fulltext/images/ac95d10de508e6337a5551b1a90a891733c2af434dff413d16a09e27f5aa0713.jpg)  
Fig. 14. Bar chart of comparison with other Websites.

## 6. Conclusion

Professor Cooper was one of the <sup>fi</sup>rst researchers to evaluate the performance of education institutions, especially with DEA. Acknowledging his contribution in performance evaluation, we have seen that DEA has a problem when used as a ranking method [45]. It has even been called “Multiattribute for lazy decision maker” [20] as no input is required from the user. Today, several commercial rankings of Universities are periodically published. These ranking have been severely criticised and may not be as useful as students do not rely on them for selecting their university. Oswald [37] concludes that “Britain needs a wider range of rankings” in order to help students. Our websystem respond to this need as it provides a personalised ranking of the 113 of<sup>fi</sup>cial British Universities. It cannot be ascertained that a university is always better than another as the ranking depends on the criteria and weights selected by the user. Ranking universities rely on imprecise, indeterminate and uncertain criteria; therefore ELECTRE III with its pseudo-criteria was appropriate for this problem. Furthermore it allows:

\- to bypass the problem of the full aggregation of incommensurate performances,

\- to reveal any disastrous criterion with the veto threshold,

\- to distinguish between indifferent and incomparable alternatives, and - to compare a very large number of universities (the limitation is given by the physical storage of data and not from ELECTRE III).

However, ELECTRE III suffers from some issues in the exploitation process of the outranking relations. As the graph of the relations may be complicated, especially for a large number of alternatives, an automatic process must be used to generate the <sup>fi</sup>nal ranking. For this purpose, the distillation has been developed. The drawback of the distillation is that an arbitrary threshold has to be selected, which may have an impact on the <sup>fi</sup>nal ranking. In our future research, we will investigate the impact of this threshold on the <sup>fi</sup>nal ranking. We will also research other methods to exploit the outranking relations.

![](/api/attachments/SFZTRTYH/fulltext/images/2e2bd9cc790206bb6f600e71bda3ecd0a0bf911d1685945f3394181cab4316d8.jpg)  
Fig. 13. Bar chart evaluating the tool.

## Acknowledgements

The authors are indebted to their colleagues Vijay Pereira, David Whitmarsh, Michael Wood and two anonymous referees for their valuable comments and suggestions, which have greatly improved the earlier version of the paper.

## References

[1] M. Abbott, C. Doucouliagos, The ef<sup>fi</sup>ciency of Australian universities: a data envelopment analysis, Economics of Education Review 22 (1) (2003) 89–97.

[2] N. Adler, L. Friedman, Z. Sinuany-Stern, Review of ranking methods in the data envelopment analysis context, European Journal of Operational Research 140 (2) (2002) 249–265.

[3] T. Ahn, V. Arnold, A. Charnes, W. Cooper, DEA and ratio ef<sup>fi</sup>ciency analyses for public institutions of higher learning in Texas, Research in Governmental and Nonpro<sup>fi</sup>t Accounting 5 (1989) 165–185.

[4] F. Arcelus, An ef<sup>fi</sup>ciency review of university departments, International Journal of Systems Science 28 (7) (1997) 721–729.

[5] V. Arnold, I. Bardhan, W. Cooper, S. Kumbhakar, New uses of DEA and statistical regressions for ef<sup>fi</sup>ciency evaluation and estimation — with an illustrative application to public secondary schools in Texas, Annals of Operations Research 66 (4) (1996) 255–277.

[6] A. Athanassopoulos, E. Shale, Assessing the comparative ef<sup>fi</sup>ciency of Higher Education Institutions in the UK by the means of Data Envelopment Analysis, Education Economics 5 (2) (1997) 117–134.

[7] V. Belton, A. Gear, On a shortcoming of Saaty's method of analytical hierarchies Omega 11 (3) (1983) 228–230.

[8] E. Bernroider, V. Stix, Pro<sup>fi</sup>le distance method — a multi-attribute decision making approach for information system investments, Decision Support Systems 42 (2) (2006) 988–998.

[9] A. Bessent, W. Bessent, Determining the comparative ef<sup>fi</sup>ciency of schools through Data Envelopment Analysis, Educational Administration Quarterly 16 (2) (1980) 57–75.

[10] A. Bessent, W. Bessent, J. Kennington, B. Reagan, An application of mathematical programming to assess productivity in the Houston independent school district, Management Science 28 (12) (1982) 1355–1367.

[11] A. Bessent, W. Bessent, A. Charnes, W. Cooper, N. Thorogood, Evaluation of educational program proposals by means of DEA, Educational Administration Quaterly 2 (1983) 82–107.

[12] D. Bouyssou, Using DEA as a tool for MCDM: some remarks, Journal of the Operational Research Society 50 (9) (1999) 974–978.

[13] R. Bowden, Fantasy Higher Education: university and college league tables, Quality in Higher Education 6 (1) (2000) 41–60.

[14] T. Breu, R. Raab, Ef<sup>fi</sup>ciency and perceived quality of the nation's “top 25” National Universities and National Liberal Arts Colleges: an application of data envelopment analysis to higher education, Socio-Economic Planning Sciences 28 (1) (1994) 33–45

[15] P. Brockett, W. Cooper, L. Lasdon, B. Parker, A note extending Grosskopf, Hayes, Taylor and Weber, “Anticipating the consequences of school reform: a new use of DEA”, Socio-Economic Planning Sciences 39 (4) (2005) 351–359.

[16] H. Cengiz, M. Yuki, Measuring value in MBA programmes, Education Economics 6 (1) (1998) 11-25.

[17] A. Charnes, W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (6) (1978) 429–444.

[18] A. Charnes, W. Cooper, E. Rhodes, Evaluating program and managerial ef<sup>fi</sup>ciency: an application of data envelopment analysis to program follow through, Management Science 27 (6) (1981) 668–697.

[19] W. Cooper, L. McAlister, Can research be basic and applied? You bet. It better be for B-schools! Socio-Economic Planning Sciences 33 (4) (1999) 257–276.

[20] J. Doyle, Multiattribute choice for the lazy decision maker: let the alternatives decide! Organizational Behavior and Human Decision Process 62 (1) (1995) 87–100.

[21] J. Doyle, R. Green, Data envelopment analysis and multiple criteria decision making, Omega 21 (6) (1993) 713–715.

[22] C. Eccles, The use of university rankings in the United Kingdom, Higher Education in Europe 27 (4) (2002) 423–432

[23] S. El-Mahgary, R. Lahdelma, Data envelopment analysis: visualizing the results, European Journal of Operational Research 83 (2) (1995) 700–710.

[24] A. Emrouznejad, B. Parker, G. Tavares, Evaluation of research in ef<sup>fi</sup>ciency and productivity: a survey and analysis of the <sup>fi</sup>rst 30 years of scholarly literature in DEA Socio-Economic Planning Sciences 42 (3) (2008) 151–157

[25] L. Friedman, Z. Sinuany-Stern, Scaling units via the canonical correlation analysis in the DEA context, European Journal of Operational Research 100 (3) (1997) 629–637.

[26] F. Glover, T. Sueyoshi, Contributions of Professor William W. Cooper in operations research and management science, European Journal of Operational Research 197 (1) (2009)1-16.

[27] R. Gunn, S. Hill, The impact of league tables on university application rates, Higher Education Ouaterly 62 (3) (2008) 273-296

[28] N. Huck, Pairs selection and outranking: an application to the S&P 100 index, European Journal of Operational Research 196 (2) (2009) 819–825.

[29] A. Ishizaka, A multicriteria approach with AHP and clusters for supplier selection, Paper Presented at the 15th International Annual EurOMA Conference, Groningen, 2008.

[30] A. Ishizaka, A.W. Labib, Towards <sup>fi</sup>fty years of the analytic hierarchy process, Keynote Paper presented at the 50th Operational Research Society Conference, York, 2008.

[31] J. Johnes, Data envelopment analysis and its application to the measurement of ef<sup>fi</sup>ciencyin higher education,Economicsof Education Review 25 (3)(2006) 273–288.

[32] J. Johnes, L. Yu, Measuring the research performance of Chinese higher education institutions using data envelopment analysis, China Economic Review 19 (4) (2008) 679–696.

[33] M. Mannino, S.N. Hong, I.J. Choi, Ef<sup>fi</sup>ciency evaluation of data warehouse operations, Decision Support Systems 44 (4) (2008) 883–898.

[34] S. Marginson, Global university rankings: implications in general and for Australia, Journal of Higher Education Policy and Management 29 (2) (2007) 131–142.

[35] C. Martin, Y. Ruperd, M. Legret, Urban stormwater drainage management: the development of a multicriteria decision aid approach for best management practices, European Journal of Operational Research 181 (1) (2007) 338–349

[36] E. Natividade-Jesus, J. Coutinho-Rodrigues, C.H. Antunes, A multicriteria decision support system for housing evaluation, Decision Support Systems 43 (3) (2007) 779–790.

[37] A. Oswald, An economist's view of university league tables, Public Money & Management 21 (3) (2001) 5–6.

[38] A. Papadopoulos, A. Karagiannidis, Application of the multi-criteria analysis method Electre III for the optimisation of decentralised energy systems, Omega 36 (5) (2008) 766–776.

[39] J.C. Pomerol, S. Barba-Romero, Multicriterion Decision in Management: Principles and Practice, Kluwer Academic Publishers, 2000.

[40] M. Rogers, Using ELECTRE III to aid the choice of housing construction process within structural engineering, Construction Management and Economics 18 (3) (2000) 333–342.

[41] N. Roussat, C. Dujet, J. Méhu, Choosing a sustainable demolition waste management strategy using multicriteria decision analysis, Waste Management 29 (1) (2009) 12–20.

[42] B. Roy, ELECTRE III: algorithme de classement base sur une présentation <sup>fl</sup>oue des préférences en présence de critères multiples, Cahiers du CERO 20 (1) (1978) 3–24.

[43] B. Roy, D. Bouyssou, Aide Multicritère d'Aide a la Décision: Méthodes et Cas, Economica, Paris, 1993.

[44] C. Serrano-Cinca, Y. Fuertes-Callén, C. Mar-Molinero, Measuring DEA ef<sup>fi</sup>ciency in internet companies, Decision Support Systems 38 (4) (2005) 557–573.

[45] T. Stewart, Relationships between data envelopment analysis and multicriteria decision analysis, Journal of the Operational Research Society 47 (5) (1996) 654–665.

[46] T. Sueyoshi, M. Goto, DEA–DA for bankruptcy-based performance assessment: misclassi<sup>fi</sup>cation analysis of Japanese construction industry, European Journal of Operational Research (2009), doi:10.1016/j.ejor.2008.1011.1039 (advance online publication).

[47] T. Sueyoshi, M. Goto, Can R&D expenditure avoid corporate bankruptcy? Comparison between Japanese machinery and electric equipment industries using DEA– discriminant analysis, European Journal of Operational Research 196 (1) (2009) 289–311.

[48] T. Suevoshi. K. Sekitani, An occurrence of multiple projections in DEA-based measurement of technical ef<sup>fi</sup>ciency: theoretical comparison among DEA models from desirable properties, European Journal of Operational Research 196 (2) (2009) 764–794.

[49] The league table of UK universities, The Complete University Guide, 2009 http:// www.thecompleteuniversityguide.co.uk/single.htm?ipg=6310#How%20the% 20League%20Table%20works (2008)

[50] E. Takeda, A method for multiple pseudo-criteria decision problems, Computers & Operations Research 28 (14) (2001) 1427–1439.

[51] P. Taylor, R. Braddock, International university ranking systems and the idea of university excellence, Journal of Higher Education Policy and Management 29 (3) (2007) 245–260.

[52] C. Tofallis, Selecting the best statistical distribution using multiple criteria, Computers & Industrial Engineering 54 (3) (2008) 690–694.

[53] J. Vaughn, Accreditation, commercial rankings, and new approaches to assessing the quality of university research and education programmes in the United States, Higher Education in Europe 27 (4) (2002) 433–441.

[54] Y.-M. Wang, K.-S. Chin, G.K.K. Poon, A data envelopment analysis method with assurance region for weight generation in the analytic hierarchy process, Decision Support Systems 45 (4) (2008) 913–921.

[55] M. Yorke, A good league table guide, Quality Assurance in Education 5 (2) (1997) 61–72.

Christos Giannoulis obtained his MSc in Software Engineering at the School of Computing of the University of Portsmouth in 2008 His research interests are on the fields of software development methods, project management and decision analysis.

Alessio Ishizaka is Senior Lecturer at the Portsmouth Business School of the University of Portsmouth. He received his PhD from the University of Basel (Switzerland). He worked successively for the University of Exeter (UK). University of York (UK) and Audencia Grande Ecole de Management Nantes (France). His research is in the area of decision-making. He was the co-organiser of a special AHP stream on the 50th Operational Research Society Conference, York, 2008 and he is a founding member of the Decision Deck Association (http://www.decision-deck.org/).
