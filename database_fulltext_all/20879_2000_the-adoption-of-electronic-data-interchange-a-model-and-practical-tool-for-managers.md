---
otero_id: 20879
otero_key: "VMDX9BPB"
title: "The adoption of electronic data interchange: a model and practical tool for managers"
authors: "Frederick Kaefer; Elliot Bendoly"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00087-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The adoption of electronic data interchange: a model and practical tool for managers

Frederick Kaefer <sup>a,)</sup>, Elliot Bendoly <sup>b,1</sup>

<sup>a</sup> Information Systems and Operations Management, Loyola UniÕersity Chicago, 820 North Michigan AÕenue, Chicago, IL 60611, USA Operations and Decision Technologies, Indiana UniÕersity, Bloomington, IN 47405, USA

Accepted 17 April 2000

## Abstract

Despite the benefits of standards-based Electronic Data Interchange EDI modes of communication, only a smallŽ . percentage of organizations have adopted even a single form of EDI. Organizations are often unable to assess the benefits resulting from the adoption of EDI due to the complexity of operational issues. This paper develops a model and decision support tool for identifying if EDI adoption is cost effective. In contrast to previous research, the model presented allows for the simultaneous adoption of multiple modes of communication. This tool is used to predict the appropriateness of EDI adoption with greater than 85% accuracy. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: EDI; Decision support; Interorganizational information systems; Long-term planning; Technology adoption model

## 1. Introduction

Electronic data interchange EDI enables busi-Ž . ness organizations to efficiently work together, quickly exchanging transaction information in standardized formats. Despite the benefits of EDI, it is estimated that out of millions of businesses in the United States, only 44,000 companies exchange business data electronically 11 . This study develops <sup>w</sup> <sup>x</sup> a model to identify scenarios in which the adoption of EDI is beneficial to an organization. The model developed is the first of its kind to allow for the simultaneous adoption of multiple modes of communication and the sharing of enablement costs. The term modes of communication is used to reflect the consideration of both EDI and non-EDI possibilities and thus communication between firms and<sup>r</sup>or between representatives of firms. The resulting metamodel presented here is intended to serve as a decision support tool for managers considering EDI adoption.

The decision to adopt EDI is complicated by the fact that a variety of fundamentally different EDI and non-EDI options are currently available. Organizations can establish direct connections to each other through the use of leased telephone lines or indirect connections through the use of the Internet. In either case, communications can be managed independently or through the use of intermediary services of Value Added Networks VANS . In addition, when EDI isŽ . not implemented, alternate modes of communication including phone, fax and automated fax can be used for conducting business transactions.

Strategic decisions regarding technology adoption need not require a single all-encompassing mode of communication, to be taken in isolation. In fact, it is not uncommon today for a single organization to have several hundred business partners, many of which use distinct and special purpose VANs and different formats of data available for use in transactions. One notable example is that of the Texas Instruments semiconductor group, which processes nearly 180,000 EDI messages each month, most of which travel over seven distinct VANs 1 . In scenar-<sup>w</sup> <sup>x</sup> ios where multiple partners exist, use of individual modes of communication and the cost associated with establishing or enabling such modes may be shared across more than one partner. Fig. 1 illustrates the structure of the multiple mode problem. If individual partners are compatible with more than one of the modes under consideration by the organization, there may exist some optimal subset of modes to be adopted.

Studies of EDI adoption and implementation typically survey large organizations that have already adopted EDI. This research derives a decision support tool for managers that are considering the adoption of EDI. The perspective taken is that of a single supplier capable of utilizing a variety of communication modes. Theoretical contributions include the development of a model and measures of problem structure. A full factorial design based on these measures is used to thoroughly evaluate the model through simulation. Our results show that the feasibility and optimality of EDI adoption is dependent on a combination of multiple defined problem characteristics, which reflect business environment factors. Insights into the impact that problem characteristics have on the adoption decision are discussed.

![](/api/attachments/VMDX9BPB/fulltext/images/e2a330ecedec92e0dad6995e18fd9570c7d459f3d2ccc60be37ab56317a84daa.jpg)  
Fig. 1. Problem structure in the multiple-mode scenario.

The structure of this paper is as follows. Following a brief review of related literature, the single supplier multiple-mode model is presented. This is immediately followed by a section in which structural measures are defined for use in characterizing specific problems. The test problem generation methodology and solution procedures are then presented, followed by the computational results of the study. The final section provides conclusions and suggestions for future research.

## 2. Related literature

The decision to implement a selected communication technology, or set of technologies, is not a trivial one. Cunningham and Tynan 5 stress that<sup>w</sup> <sup>x</sup> although a vast amount of information is required to support trading relationships, it is also clear that such information may simultaneously take the form of various document types, both paper and electronic, associated with the modes of transfer available to a firm and its customers. In addition to the number of communication alternatives,, decision-makers must take into account complicating factors such as financial, technological and contractual restrictions on the use of each alternative.

Financial restrictions, although often identified as a primary barrier to new technology adoption, can easily be misunderstood. Technology adoption costs need not be viewed in the potentially deterrent lumpsum forms typically associated with the implementation process as a whole. Rather, initial adoption costs may be amortized over a large number of transactions and, hence, should be considered in this light. However, even from such a vantage, transaction cost benefits may not warrant relatively high technology enablement costs. When the net benefit from the adoption of an alternate communication technology is negative, such an option may not only be suboptimal to the current system, it may also be financially infeasible.

Technological restrictions are significant when communication with an individual party is limited to only those modes already used by that party. Such restrictions, accompanied by a limited pool of trading partners, may pressure firms to adopt costly technologies in attempts to capture even relatively marginal gains in revenue. Such actions may in turn provide somewhat paradoxical phenomena regarding the relationship between trade volume and EDI use, when viewed from a case-by-case perspective 8 .

The negative impact of financial and technological restrictions has been reiterated by numerous professionals in the IS community. As Arunchalam’s 3<sup>w</sup> <sup>x</sup> survey of IS managers revealed, 36.3% of those responding considered non-automation and nonsophistication of customers to be a serious barrier to EDI adoption. Such a finding regarding compatibility supports that of Premkumar et al. 14 in their com-<sup>w</sup> <sup>x</sup> prehensive field analysis. From this same survey, 30.2% found high setup costs to be an impediment, while 15.9% cited the lack of trading partners as significant. At the same time, however, 32.5% of those responding cited long-run cost efficiency as a driver for adoption, with 48.1% stressing the improvements in customer service made possible through adoption. Such findings demonstrate sensitivity to short-term versus long-term analysis of the adoption issue.

In addition to these considerations, contractual restrictions, due to physical and operational capacities on product supply further limit the extent to which modes of communication may effectively be used. Since the total volume of transactions faced over the planning horizon may be dependent upon the total physical volume of goods and services provided to contracted business partners, firms necessarily gauge their adoption decisions by the limitations of their own productivity. The complicating nature of these factors considered simultaneously can make the decision process extremely difficult, even when only a small number of technologies and communicating partners are considered. For this reason, organizations stand to gain substantially from the availability of models and solution procedures designed to identify preferable adoption decisions.

EDI adoption decisions have previously been examined in a number of contexts. These contexts can be contrasted by the number of communication technologies available and by the nature of those parties involved in communication. The predominant context examined, however, allows for the adoption of only a single EDI mode of communication 13,15 .<sup>w</sup> <sup>x</sup> In these scenarios, a single buyer plays the dominant role in the ultimate adoption decision. Wang and Seidmann 15 compare two policies of buyer influ-<sup>w</sup> <sup>x</sup> ence in single-mode EDI adoption, and the effectiveness of such policies. In contrast, Mukhopadhyay et al. 13 focus on the benefits that result from the<sup>w</sup> <sup>x</sup> adoption of a single EDI mode.

The effective use of EDI has also been studied in several operational contexts, particularly inventory control. Banerjee and Banerjee 4 and Anvari 2 use<sup>w x</sup> <sup>w x</sup> economic order quantity based formulations to illustrate the coordination benefits made possible via EDI-based communications. Ernst and Kamrad 6<sup>w</sup> <sup>x</sup> use more sophisticated policies in studying the allocation of warehouse inventory in fixed-order intervals, given the availability of EDI. However, in none of these cases are idiosyncratic elements of EDI integrated within the formulations used to distinguish its effects from those of electronic commerce in general. Furthermore, as before, single modes of EDI communication are used in depicting the systems studied. Unfortunately, while providing a means of simplification, the single-mode assumption is somewhat limiting in its ability to depict real world applications.

## 3. Model formulation

The EDI adoption problem is modeled as a 0–1 Integer Program. The formulation of the model has many parallels with classical location–allocation formulations 7,12 . Specifically, the model can be<sup>w</sup> <sup>x</sup> compared to a capacitated single-factory scenario in which goods are shipped to a subset of demand zones via uncapacitated and technologically dissimilar warehouses. In the model presented here, the organization’s output of a particular good or service is limited over the time horizon by a quantity Q. A fixed set of potential modes of communication, L, exist by which the organization can conduct transactions with any number of <sup><</sup> <sup><</sup> J potential buyers of that product. The objective is to select those subsets of modes and buyer contracts that maximize the profit of the organization.

The adoption policy finally used takes into account the output capacitation of the organization, Q, and the quantity demanded, $V _ { j } ,$ if a contract is established with buyer $j$ for the time period under consideration. The quantity that is demanded by a specific buyer is independent of the number of transactions they may use in procuring that volume. Furthermore, each buyer may only be compatible with a sub-set of the possible modes of communication, $S _ { j }$ . The contractual gain gross income less production and ship- Ž ping cost derived from a relationship with a particu- . lar buyer j is designated here as $K _ { j }$ . The costs of activating a particular mode of communication in- Ž stallation and<sup>r</sup>or mediator establishment, etc. is. designated as a mode enablement cost $F _ { l }$ and the costs related to specific buyer use translation, train-Ž ing, transaction cost, etc. designated as a set of costs . $C _ { j l } .$ Table 1 presents a summary of the notation used in the model.

Based on this notation, the multiple-mode adoption model is presented in Fig. 2. The objective function 1 captures the gains available throughŽ . contracting, less the fixed and variable costs necessitated by the subsequent contract transactions. Constraints 2 require that a mode of communications Ž . be enabled $( P _ { l } )$ prior to its use with any of the contracted buyers $( B _ { j l } ) _ { \ l }$ Ž .. Constraints 3 stipulate that those transactions considered with a particular buyer

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 1
Summary of model notation
J Index set of buyers
L Index set of modes of communications;
 $L = L_{EDI} \cup L_{NonEDI}$ $S_{j}$  Index set of modes by which the supplier can transact with buyer j;  $S_{j} \subset L$ ,  $S_{j} \neq \{\varnothing\}$ 
R Index set of buyers that are compatible with at least one non-EDI mode
 $K_{j}$  Revenue expected through establishing contract with buyer j
 $F_{l}$  Fixed cost of enabling mode l
 $C_{jl}$  Cost of using mode l for contract associated transactions with buyer j
 $V_{j}$  Volume dedicated if contract is established with buyer j
Q Full capacity of supplier over planning horizon
 $P_{l}$  Mode enablement variable;  $P_{l} = 1$  if mode l is enabled, 0 otherwise
 $B_{jl}$  Buyer mode-usage variable;  $B_{jl} = 1$  if mode l is used for transactions with buyer j; 0 otherwise
</div>

Fig. 2. The multiple-mode adoption model MMA .Ž .

$$
\max \sum_ {j \in J} K _ {j} \sum_ {l \in S _ {j}} B _ {j l} - \sum_ {l \in L} F _ {l} P _ {l} - \sum_ {j \in J} \sum_ {l \in S _ {j}} C _ {j l} B _ {j l}\tag{1}
$$

$$
\sum_ {j \in J} B _ {j l} \leq | J | P _ {l}
$$

$$
\forall l \in S _ {j}\tag{2}
$$

$$
\sum_ {l \in S _ {j}} B _ {j l} \leq 1
$$

$$
\forall j \in J\tag{3}
$$

$$
\sum_ {j \in J} \sum_ {l \in S _ {j}} V _ {j} B _ {j l} \leq Q
$$

$$
P _ {l} \in \{0, 1 \}\tag{4}
$$

$$
B _ {j l} \in \{0, 1 \}
$$

$$
\forall l \in L
$$

$$
\forall j \in J, \forall l \in L\tag{5}
$$

(6)

be limited to at most one mode of communication. Constraint 4 limits the number of contracts estab-Ž . lished with buyers by the volume demanded and the capacity of the organization. Constraints 5 and 6 Ž . Ž . restrict the variables to values of 0 or 1.

## 4. Measures of problem characteristics

To better understand the nature of problem instances in the outlined model, summaries of problem characteristics have been constructed. These measures are based on the perceived relevance of the three restrictive issues discussed earlier. The first two measures consist of Modal Compatibility MC ,Ž . which draws directly upon the issue of technology restrictions to adoption, and Capacitated Allowance Ž .CA , which alludes to the criticality of contractual constraints. Financial restrictions are embodied by the latter two measures of Enablement Cost Insensitivity ECI and Transaction Cost Sensitivity TCS , Ž . Ž . which focus on trade-offs between the long-run expenditure and cost savings associated with technology adoption. In this section, each of these four measures will be discussed in turn. It should further be noted that although the terms chosen to label these measures were selected with the intent of expressing intuitive managerial issues, the authors realize that alternate terms may appear more suitable to others.

Modal Compatibility provides a measure of network density. As a network density measurement, the values of MC fall within a continuum between 0 and 1. An MC value of 0 is associated with scenarios in which each buyer is compatible with only a single mode. When MC is 1, all buyers may use any of the potential modes of communication. MC is specified as follows:

$$
\mathrm{MC} (\text { Modal   Compatibility }) = \frac {\left(\Sigma_ {J} | S _ {j} | / | J |\right) - 1}{| L | - 1}
$$

The second measure, Capacitated Allowance, represents the ratio of supplier capacity to the sum of all potential demands. By this definition, the values of CA are non-negative. When CA takes a value close to 0, only a very small proportion of the total available demand may be accommodated. At a CA value of 1 or greater, the supplier may simultaneously satisfy the demand of all buyers. CA has the following form:

$$
\mathrm{CA} (\text { Capacitated   Allowance }) = \frac {Q}{\sum_ {J} V _ {j}}
$$

Transaction Cost Sensitivity relates variable transaction costs of non-EDI modes to potential contractual revenues. The measure is defined over the set of buyers compatible with non-EDI modes, R. TCS is the ratio of the sum of the maximal non-EDI transaction costs to the sum of potential contractual gains.

TCS Transaction Cost Sensitivity Ž .

$$
= \frac {\sum_ {R} \max \left(C _ {j l}\right) l \in S _ {j} \cap L _ {\text { NonEDI }}}{\sum_ {R} K _ {j}}
$$

It is assumed that transaction costs are infinite for all incompatible modes and always less than or equal to contractual gains for all compatible modes. By definition, TCS takes values between 0 and 1. At values near 0, the TCS measure suggests that transaction costs of at least one non-EDI mode are insignificant relative to contractual gains. TCS values of 1 indicate that the cost of using non-EDI modes of communication outweigh the benefits reaped through contractual gain. Only non-EDI modes are used in the derivation of TCS since the measure is designed to capture the costs associated with not adopting EDI.

The last measure, Enablement Cost Insensitivity, provides a measurement of the importance of fixed costs of EDI adoption within a given problem. The measure is defined as the ratio of the average potential contractual gain to the cost of enabling the EDI mode having the least fixed cost.

$$
\begin{array}{r l} \text { ECI(EnablementCostInsensitivity)} \\ & = \frac {\sum_ {J} K _ {j} / | J |}{\min (F _ {l}) l \in L _ {\mathrm{EDI}}} \end{array}
$$

As a result of this definition, ECI takes on only non-negative values. ECI values close to 0 suggest that many contracts of average revenue are necessary to justify EDI adoption. ECI values of 1 or greater suggest that a single contract of average revenue is sufficient to justify EDI adoption.

The feasibility of EDI adoption cannot be identified by any one of these measures in isolation. For example, a firm capable of accommodating only a small number of buyers low CA and lowŽ <sup><</sup> <sup><</sup> J . may still be able to adopt EDI if the level of revenue gained from each contract is relatively high high Ž ECI . However, if the level of revenue gained from. each contract is low, the adoption of EDI will most likely not be feasible for that firm. In general, the feasibility of EDI adoption can be ascertained by computing the product of the three measures <sup><</sup> <sup><</sup> J , CA and ECI, i.e. the ratio of the total expected revenue to the minimum EDI enablement cost, assuming revenues and volumes are uncorrelated. If this ratio is less than 1, the feasibility of EDI adoption is unlikely.

$$
\begin{array}{r l} | J | \cdot \mathrm{CA} \cdot \mathrm{ECI} (\text { Feasibility   of   EDI   adoption }) & \\ = \frac {Q \cdot \Sigma_ {J} K _ {j} / \Sigma_ {J} V _ {j}}{\min (F _ {l}) l \in L _ {\mathrm{EDI}}} \end{array}
$$

## 5. Problem generation and solution procedure

## 5.1. Problem generation

In order to ensure a full range of test cases, a full factorial design was implemented. The factors included the number of buyers and each of the four measures defined in the previous section. Three levels were specified per factor, each level corresponding to a range of factor values. Five problems were randomly generated for each factor level combination, resulting in a total of 1215 problem cases. The

Estimated Total Number of Transactions three ranges from which the number of buyers was drawn were 20,80 , 81,140 , and 141,200 . For all<sup>w</sup> <sup>x w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> other factors, the three ranges used were 0,0.334 ,<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x w</sup> <sup>x</sup> 0.334,0.667 , and 0.667,1 .

Using current cost estimates, six categories of communication modes were used in problem generation, allowing for a total of 64 mode enablement combinations. These categories included telephone, fax, automated fax and three categories of EDI. Distinctions in cost across the three EDI categories capture the use of different technologies and levels of system customization. For each of the six categories, increases in enablement costs are offset by decreases in costs of transaction when sufficient transactions take place. Fig. 3 provides log–log plots of the relationships between total communication costs and number of transactions, for each of the categories of interest. Regions that appear horizontal illustrate the impact of initial enablement costs on the overall cost relationship.

The EDI cost parameters used in our simulation are based on industry figures. Fixed and variable costs depend on whether or not the EDI modes are Internet based, as well as whether or not a VAN is employed. However, both enablement and transaction costs of different EDI modes vary even within these specifications. Use of a VAN may require higher transaction costs, but the software costs for VAN-based systems may be appreciably small. Customized in-house EDI systems tend to be much more expensive, where the translation software of a customized EDI system alone can cost as much as \$50,000 1 . In a recent case study examining the<sup>w</sup> <sup>x</sup> total measurable costs of implementing EDI, these costs were estimated at \$143,600, including training, hardware and software costs 9 .<sup>w</sup> <sup>x</sup>

## 5.2. Solution procedure

The solution procedure began with the calculation of upper and lower bounds on the objective function. For each combination, the set of compatible buyers was sorted by the ratio of net revenue to capacity demanded. The net revenue was in turn calculated as the difference between contract revenue and the least expensive transaction cost among the modes available. For each mode combination, a potential lower bound was computed by selecting the most cost-effective buyers one by one until the next immediate buyer’s demand exceeded the remaining capacity. The best potential lower bound across all mode combinations then served as the effective lower bound for the problem case. Potential upper bounds were calculated at each mode combination by including a proportion of the next immediate buyer’s net revenue based on the proportion of demand to remaining capacity. Again, the best upper bound was selected from the set of mode combinations.

If there was no difference between these bounds, the solution for the lower bound objective was taken as optimal. In all other cases, an implicit enumeration procedure was implemented using the lower bound as an initial solution. The sub-procedure began by sorting the mode combinations by descending potential upper bounds. Mode combinations were then examined in this order, by performing a depth first search on the buyer set. If the potential upper bound of the next mode combination in the sorted list does not exceed the current incumbent solution, the search terminated.

![](/api/attachments/VMDX9BPB/fulltext/images/9a8248281e33d1e1cab5465e46cfbbfee784ed6cbb6c937caa11fb325c68654e.jpg)  
Fig. 3. Trade-offs between communication modes based on transaction volume.

## 6. Computational results

The solution procedure was implemented in the programming language C, and run on a 180 MHz Pentium-based PC. Due to the combinatorial nature of the model studied, not all problems could be solved exactly in the time allotted. Out of the 1215 cases examined, only 506 of the solutions were verified within 60 s of CPU time. On average, the initial upper and lower bounds calculated were very tight. For those cases in which optimal solutions were verified, the upper bound was only 3.8% greater, on average, than the initial lower bound. Furthermore, the best solutions found were on average 2.2% lower than the initial upper bound. In the 709 nonverified cases, the upper bounds were observed to be only 0.9%, on average, above the initial lower bound, with the best solutions only 0.5% below this upper bound. Although these latter cases were not solved exactly, the quality of the best solutions found is illustrated by the tightness of the bounds derived.

The methodology selected for the interpretation of these computational results was logistic regression, a technique appropriately suited for the consideration of binary outcomes 10 . Logistic regression is a <sup>w</sup> <sup>x</sup> technique through which a binary categorical 0,1 4 response variable, representing a dichotomy within the population, is related to a set of explanatory independent variables. The analysis essentially involves the estimation of a standard regression equation, whose unbounded dependent variable ranging Ž from <sup>y</sup>\` to \`. is transformed into a variable restricted to the range 0,1 . Due to the nature of the <sup>w</sup> <sup>x</sup> transformation utilized and the resulting output, discussions of the estimated relationships tend to involve reference to the likelihood or odds that an observation falls within one of the two categories.

## 6.1. Solution analysis

The 506 cases in which solutions were verified were used to examine the potential relationships that exist between the problem factors and the types of communication modes ultimately adopted. Of particular interest were cases in which EDI adoption occurred. Relative frequency comparisons, similar to that used in examining problem solvability, revealed no obvious nonlinear relationships.

Table 2  
Estimated coefficients of fit for EDI adoption in verified solutions

<table><tr><td></td><td>Constant</td><td>|J|</td><td>MC</td><td>CA</td><td>ECI</td><td>TCS</td></tr><tr><td> $\beta$ </td><td>-8.204</td><td>0.025</td><td>-5.021</td><td>6.011</td><td>5.586</td><td>2.832</td></tr><tr><td>Significance</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R</td><td>NA</td><td>0.289</td><td>-0.328</td><td>0.373</td><td>0.313</td><td>0.183</td></tr></table>

The log-likelihood of EDI adoption was modeled as a linear combination of the four problem factors and the number of buyers. The estimated model correctly classified 85.6% of all cases observed. Table 2 provides a summary of the coefficients of fit and their significance levels, along with the individual R-values of each included term.

All factors contributed to the explanatory power of the model. Based on the coefficient of fit, for every unit increase in the number of potential buyers $( | J | )$ , the likelihood of adoption increases by a factor of $\begin{array} { r l } { \mathrm { e } ^ { 0 . 0 2 5 } = } & { { } 1 . 0 2 5 } \end{array}$ , or 2.5%. Higher levels of CA correspond to greater likelihood of EDI adoption, since an organization can amortize EDI enablement costs across a larger number of buyers. As an organization is more insensitive to enablement costs, signified by higher values of ECI, it can more readily consider adopting EDI. Similarly, as transaction costs become more important, corresponding to higher levels of TCS, lower transaction cost EDI modes will be adopted. Lower levels of MC, reflecting fewer choices of modes to use with each buyer, lead to the necessity to adopt a larger variety of modes, often including EDI.

## 6.2. Use of decision support tool

Our research identifies relationships that impact the optimality of adopting EDI. A manager, once identifying her specific situation’s characteristics, can use the findings of this research to support EDI adoption decisions. The graphical illustrations presented in the figures that appear in this section are intended to help the decision maker be more confident in the decision making process. The overall

Likely Feasible, Likely Optimal when MC=0 and TCS=1 practical implications of this research stem from our observation that EDI adoption is optimal only in operating environments characterized by specific combinations of financial, technological and contractual traits. In operating environments without an appropriate mix of attributes, EDI adoption may not be ideal or even feasible. With the tool presented here, decision makers can assess the appropriateness of their specific environment along the same lines and, therefore, support a decision of whether or not to adopt EDI using the findings of this research.

Insight into the likelihood of EDI adoption is gained through the interpretation of the combined effects of all of the significant factors. It has already been mentioned that the likelihood of the feasibility of EDI adoption is a function of the number of potential buyers Ž<sup><</sup> <sup><</sup> J . Ž . , capacitated allowance CA and insensitivity to initial enablement costs ECI .Ž . Furthermore, the likelihood that EDI adoption is optimal was shown to be a function of all five factors mentioned above. Fig. 4 presents graphical representations of these two functions to illustrate the impacts that the different factors have on both feasibility and optimality. In order to provide a two-dimensional representation of these relationships, the three factors common to both functions serve as a foundation for the graphs. CA and ECI serve as primary axes of these graphs. The three graphs presented are based on low, medium and high number of potential buyers Ž<sup><</sup> <sup><</sup> J ., respectively. Furthermore, in order to illustrate the full range of effects that technological compatibility across buyers Ž . Ž . MC and variable transaction costs TCS have on likelihood of optimality, best MCŽ . <sup>s</sup>0, TCS<sup>s</sup>1 and worst MCŽ . <sup>s</sup>1, TCS<sup>s</sup>0 case scenarios are presented.

Four distinct regions are clearly identifiable in Fig. 4. The white region represents those scenarios in which the adoption of EDI is not likely feasible. Stated above, this occurs when the product of <sup><</sup> <sup><</sup> J , CA and ECI is less than unity. A second region, shaded light gray, represents those scenarios in which the adoption of EDI is likely feasible, but not likely to be optimal. In such situations, even though a firm could afford to adopt EDI, more profitable communication options exist. It is interesting to note that beyond a certain minimum number of potential buyers, this region is non-existent. This suggests that given a high number of such buyers and in the presence of sufficient technological compatibility and transaction cost savings, EDI adoption feasibility is a sufficient condition for the likelihood of optimality. On a similar note, the black-shaded region represents those scenarios in which EDI adoption optimality is likely, provided feasibility, regardless of the values of MC and TCS.

Perhaps most interesting is the dark gray region, in which the likelihood of EDI adoption being an optimal decision is sensitive to values of MC and TCS, conditional on the feasibility of such adoption. As a result, scenarios that fall within this region require the simultaneous consideration of all five

![](/api/attachments/VMDX9BPB/fulltext/images/755d77f4a814f4f43967c87bd9f1a8cca5e3d49003c1ed43f5e0726d0b606e41.jpg)  
a) J = 20

![](/api/attachments/VMDX9BPB/fulltext/images/872a32d4ca0482999a533932a8fc7ea395a8d158391ef87b1696da18704267b4.jpg)  
b) J = 110

![](/api/attachments/VMDX9BPB/fulltext/images/8ac8ff02a70eea89b8a62ab3d38a93e6125f4d7e6c94357049e0f4b2a9d16c68.jpg)  
c) J = 200  
Likely Not Feasible Likely Feasible, Likely Not Optimal

Likely Feasible, Likely Optimal for All Values of MC and TCS

Fig. 4. Feasibility and optimality likelihood frontiers for EDI adoption.

factors. In lieu of the methodology proposed here, the complexity indicative of such scenarios may be sufficient to deter the consideration of such options by small to mid-sized firms. By our results, such firms positioned close to the sub-optimal light grayŽ . region need to ensure sufficient operational sensitivity to transaction costs and restrictive modal compatibility, particularly in the form of several buyer relationships requiring EDI for establishment, if EDI is to be a preferred option. The operationalization of the adoption environment into the factors considered here, and the availability of the logistic regression models developed provide a convenient means of checking that such conditions are met. Therefore, in a very real sense the summary model serves to provide managers with a practical tool for support in such complex decisions making scenarios.

To illustrate the dynamics inherent to the dark gray region, consider a firm characterized by a moderate number of potential business partners, about half of which it can feasibly supply at its current capacity level, and faced with mid-level fixed costs for adopting EDI. As the number of communication options deemed acceptable by its potential partners goes down, the firm may be forced to adopt more costly modes simply in order to engage in the more profitable of these relations. Under less restrictive compatibility constraints, as firms economize on transaction costs, perhaps in part due to a reengineering process, the long-term cost benefits accrued through EDI adoption begin to dwindle in comparison. Again, although such assessments can be performed visually, and somewhat subjectively as a result, the meta-model decision support tool presented here promises a much more refined and unbiased glance for managers faced with the EDI adoption decision.

## 7. Conclusion

The purpose of this study was to identify those scenarios under which the adoption of EDI is beneficial to an organization. The model developed is the first of its kind to allow the simultaneous adoption of multiple modes of communication and the sharing of enablement costs. Capacity and compatibility constraints are also enforced. To better understand the tradeoffs presented by the cost structure and constraints of the model, four measures of structure are introduced. An evaluation of the model and the associated tradeoffs is carried out through the use of a full factorial design based on these measures.

Using these factors, logistic regression models for predicting EDI adoption were constructed. These regression models provide a practical tool for predicting if the adoption of EDI is beneficial. In over 500 exactly solved problem instances, this tool accurately predicted over 85% of the EDI adoption decisions. This tool was just as effective in predicting near-optimal solutions of problems that could not be verified in a prescribed time limit. Also worth noting is that all factors identified were shown to have significant effects on the likelihood of EDI adoption optimality. Given these results, the likelihood functions of EDI adoption feasibility and optimality were compared. In this comparison, four distinct regions, based on all factors, are identified. These regions illustrate the importance of problem factor interaction in the final EDI adoption decision.

Our results show that the question of EDI adoption is particularly complicated for firms characterized by physical capacity restrictions, a limited pool of candidate trading partners and<sup>r</sup>or financial limitations with respect to adoption. For such firms, the potential gains available via EDI adoption can only be realized in the presence of excessive transactional costs and<sup>r</sup>or EDI requirements set forth by business partners. The decision support tool presented here is particularly helpful in facilitating complicated technology adoption decisions such as these.

Future research issues take a variety of forms. From an analytical standpoint, alternate structural measures need to be identified, to better predict the appropriateness of EDI adoption. Furthermore, a multiple planning horizon extension of the model should be considered to incorporate the reality of asynchronous contracting. From a practical standpoint, the model and decision tool should be applied to actual data, in order to provide verification and to identify additional issues. Furthermore, it is important to note that this methodology need not be restricted to contemporary EDI adoption decisions, as it retains a robustness that can be applied to future communication technology considerations as they arise.

## References

<sup>w</sup> <sup>x</sup> 1 R. Adhikari, EDI heads for the Net, InformationWeek 578 Ž .1996 59.

<sup>w</sup> <sup>x</sup> 2 M. Anvari, Electronic data interchange and inventories, International Journal of Production Economics 26 1992 143–Ž . 153.

<sup>w</sup> <sup>x</sup> 3 V. Arunchalam, Electronic data interchange: issues in adoption and management, Information Resources Management Journal 10 2 1997 22–31.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 A. Banerjee, S. Banerjee, Coordinated, orderless inventory replenishment from a single supplier and multiple buyers through electronic data interchange, International Journal of Technology Management 7 4 1992 328–336.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 C. Cunningham, C. Tynan, Electronic trading, interorganizational systems and the nature of buyer–seller relationships: the need for a network perspective, International Journal of Information Management 13 1993 3–28.Ž .

<sup>w</sup> <sup>x</sup> 6 R. Ernst, B. Kamrad, Allocation of warehouse inventory with electronic data interchange and fixed order intervals, European Journal of Operational Research 103 1997 117–128.Ž .

<sup>w</sup> <sup>x</sup> 7 A.M. Geoffrion, G.W. Graves, Multicommodity distribution system design by Bender’s decomposition, Management Science 20 5 1974 822–844.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 P.J. Hart, C.S. Saunders, Emerging electronic partnerships: antecedants and dimensions of EDI Use from the supplier’s perspective, Journal of Management Information Systems 14 Ž . Ž .4 1998 87–111.

<sup>w</sup> <sup>x</sup> 9 R. Hornback, An EDI costs<sup>r</sup>benefits framework, http: <sup>r r</sup>www.ecworld.org <sup>r</sup> Resource Center<sub>– –</sub><sup>r</sup>Case Studies<sup>r</sup>hornback.html, cited May 7, 1998 .Ž .

<sup>w</sup> <sup>x</sup> 10 D.W. Hosmer, S. Lemeshow, Applied Logistic Regression, Wiley, New York, 1989.

<sup>w</sup> <sup>x</sup> 11 R. Kalakota, A.B. Whinston, Frontiers of Electronic Commerce, Addison-Wesley, Reading, MA, 1996.

<sup>w</sup> <sup>x</sup> 12 A.A. Kuehn, M.J. Hamburger, A heuristic program for locating warehouses, Management Science 9 4 1963 643–666. Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 T. Mukhopadhyay, S. Kekre, S. Kalathur, Business value of information technology: a study of electronic data interchange, MIS Quarterly 19 2 1995 137–156.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 G. Premkumar, K. Ramamurthy, S. Nilakanta, Implementation of electronic data interchange: an innovation diffusion perspective, Journal of Management Information Systems 11 Ž . Ž . 2 1994 157–186.

<sup>w</sup> <sup>x</sup> 15 E.T.G. Wang, A. Seidmann, Electronic data interchange: competitive externalities and strategic implementation policies, Management Science 41 3 1995 401–418.Ž . Ž .

![](/api/attachments/VMDX9BPB/fulltext/images/d6d1eea45e96312c253ebb436dea3d998f8aafd1c9332c8e4f806dd5ccf241ab.jpg)

Frederick Kaefer is an assistant professor of information systems in the Information Systems and Operations Management Department of the School of Business Administration at Loyola University Chicago. He has a Ph.D. in MIS from the University of Iowa. His research interests are in the planning and use of communication systems. Before joining the Loyola University faculty, he was an assistant professor at the Indiana University Kelley School of Business.

Elliot Bendoly is a doctoral student in operations and decision technologies at the Indiana University Kelley School of Business. He received his B.A in economics and B.S. in engineering from Case Western Reserve University. His research interests include the modeling of technology adoption<sup>r</sup>implementation processes, enterprise resource planning issues and design and use of effective decision support tools. Prior to coming to Indiana University, he worked as a core competency engineer at the Intel Corporation.
