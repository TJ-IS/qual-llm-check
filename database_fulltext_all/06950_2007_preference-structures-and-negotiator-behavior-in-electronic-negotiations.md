---
otero_id: 6950
otero_key: "57B2W758"
title: "Preference structures and negotiator behavior in electronic negotiations"
authors: "Rudolf Vetschera"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Preference structures and negotiator behavior in electronic negotiations ☆

Rudolf Vetschera

University of Vienna, Vienna, Austria

Received 14 September 2005; received in revised form 22 November 2006; accepted 21 March 2007 Available online 28 March 2007

## Abstract

Electronic Negotiation Support Systems allow users to construct a formal model of their preferences, which is then used during the negotiation process. In this paper, we analyze whether preferences embedded in such models are actually reflected in the behavior of negotiators and negotiation outcomes. Empirical results indicate that elements of negotiator behavior, like initial offers or the extent of concessions made during the negotiation, closely correspond to individual preferences. The same holds for the structure of the compromise. In contrast, the impact of negotiator preferences on reaching an agreement or the efficiency of the compromise is rather weak. @.2007 1

Keywords: Negotiation support systems; Preference model; Utility; Empirical research

## 1. Introduction

Different types of negotiation support systems (NSS) have been proposed in the literature [6,16,17,23,37]. Similarly to classifications in the area of Group Decision Support Systems [12,45], classifications for NSS [19] are often based on the level of (analytical) support for negotiators. Analytical tools enable negotiators to represent their preferences in a convenient form to evaluate offers or determine concessions. Fig. 1 shows a general framework for analytical, preference-based negotiation support.

Analytical decision support is based on two key elements: The first is a prescriptive theory, which defines rational behavior in an axiomatic way and provides methods for rational decision making. Rational behavior as defined in prescriptive theory still leaves room for subjective preferences, which are encoded in a model using parameters elicited from negotiators, for example attribute weights. In a group decision or negotiation context, different parties might use different preference models [47] or specify parameters only imprecisely [25] to reach consensus.

The methods from prescriptive theory and the preference model determine (as far as the recommendations of the model are followed) the behavior of negotiators. This behavior, and the actions of the opponent, lead to an outcome of the negotiation. Thus, analytical support induces a “directed change” in behavior as defined by Silver [39].

![](/api/attachments/57B2W758/fulltext/images/18218826271e960e6ecbcd306b23992b923cb6017f2bb53397c1f818c8e846d6.jpg)  
Fig. 1. Framework of preference-based negotiation support.

Previous empirical research on NSS [11,15,37,38] has focussed on the impact of analytical support on negotiation outcomes, as represented by the dashed line in Fig. 1. These studies have indicated that analytical methods can increase the likelihood of achieving a (Pareto-efficient) compromise [27] as well as the satisfaction of negotiators [15].

In this paper, we study the impact of preference-based support in NSS at a more detailed level, focusing on the relationships represented by bold arrows in Fig. 1. We study whether preferences embedded in a model actually influence behavior and outcomes. This is a fundamental assumption, on which all types of preference-based systems are based: if preference models bore no relationship to actual behavior, the entire process of preference elicitation and encoding performed in many DSS is in vain.

This paper is based on the analysis of negotiation experiments with the NSS Inspire [21], which uses multi-attribute utility theory [18] to model preferences. We study how certain properties of utility functions influence bargaining behavior and the outcomes of negotiations.

Although the relationships shown in Fig. 1 are essential to analytic, model-based negotiation support, the impact of preference structures on negotiations has seldom been studied empirically. This is rather surprising, as empirical studies have thoroughly analyzed the impacts of many other characteristics of negotiators like their national culture [44], reputation [42] or fear of “loosing face” [46]. One study related to our research question was performed by Northcraft et al. [31] who, based on theoretical results [29,30] performed experiments on the effect of different shapes of nonlinear utility functions on negotiator behavior. In another set of experiments, Bottom [4] used differences in utility functions for gains and losses to explain the impact of framing effects on negotiation outcomes. Curhan et al. [10] considered the relationship between preferences and negotiation processes as a feedback loop and explored the impact of processes on preferences.

The remainder of our paper is structured as follows: in Section 2, we formulate our hypotheses relating negotiators' utility functions to behavior and outcomes. Section 3 provides an overview of the data used and descriptive statistics. In Section 4, we present the empirical results. Section 5 concludes the paper by summarizing our main results, discussing consequences and outlining areas of future research.

## 2. Hypotheses

## 2.1. Structural properties of utility functions

Preferences in multi-attribute decision problems can be represented in different forms. Inspire uses an additive, multi-attribute utility function

$$
u (X) = \sum_ {k} w _ {k} u _ {k} (x _ {k})\tag{1}
$$

where $x _ { k }$ is the value of alternative X in attribute $k ,$ w and $u _ { k } ( . )$ are the weight and the single-attribute (marginal) utility function for attribute k.

By using an additive utility function, Inspire imposes certain restrictions on preferences, for example, the assumption of preferential independence between attributes [18]. Nevertheless, there is considerable room for individual differences. We characterize individual preferences using three structural properties of the utility functions:

• The attribute weights $w _ { k } ,$

• the monotonicity of the single-attribute utility functions, and

• the shape (linear, convex, concave) of the singleattribute functions.

A similar classification was developed by Mumpower [29] to study the impact of utility functions on negotiation problems. He classified utility functions according to weights, functional form (shape) and aggregation rule. Since Inspire always uses an additive function, the aggregation rule cannot be studied using our data.

Attribute weights reflect the importance a decision maker assigns to an attribute and thus can be expected to influence a negotiator's behavior. Monotonicity of single-attribute utility functions represents the direction into which a negotiator wants to influence the attribute. We therefore expect it to have a considerable impact on behavior and outcomes and include it in our analysis, although it was not considered in [29].

Mumpower [29] and Northcraft et al. [30,31] studied the impact of the shape of single-attribute utility functions. Once an agreement is reached, the outcome for negotiators is certain. Therefore the shape of a single-attribute utility function does not represent risk preference, but the marginal contribution to overall utility from each attribute. While standard microeconomic theory assumes decreasing marginal utility and thus concave utility functions, increasing marginal utility for some attributes is not considered as unusual in a multi-attribute context [18].

For a negotiator who exhibits increasing marginal utility in an issue, deviating from the best possible value would lead to a considerable loss in utility. Conversely, if the single-attribute utility function is concave, deviating from the best outcome would mean only a small loss in utility. Thus we expect the shape of marginal utility functions to have a considerable impact on how tough a negotiator bargains with respect to that attribute.

## 2.2. Behavior during negotiations

We distinguish three phases of a negotiation process:

• The initial offers made by each party at the beginning of the negotiation,

• the ongoing concessions during the negotiation process, and

• the final acceptance of a compromise, if one is reached.

If the analytical negotiation support is effective, the preferences of negotiators should be reflected in all three phases. In this subsection, we discuss the first two stages. Based on the structural properties of utility functions, we formulate the following hypotheses:

<sup>Hypothesis H1.</sup> The value of the initial offer in an attribute will be positively influenced (in the direction of the negotiator's preferences) by the weight and the convexity of the marginal utility function for that attribute.

A higher attribute weight means that this attribute is more important to the negotiator. We can therefore expect that the negotiator will start with a high demand in this attribute. Similarly, as we have already discussed, we expect negotiators who have a convex marginal utility function in an attribute to negotiate particularly tough, leading to a high initial demand. Although there are, to our knowledge, no empirical studies on the impact of attribute weights or the shape of utility functions on initial offers, hypothesis H1 can still be related to existing empirical research. Prior studies [5] have used aspiration or reservation levels of negotiators as explanatory variables and have shown that negotiators with higher aspiration or reservation levels also start with higher initial demands.

Finally, H1 refers to the direction of a negotiator's preferences, which is related to the monotonicity of single-attribute utilities. When a negotiator is expected to negotiate toughly with respect to an attribute and has a monotonically decreasing single-attribute function, we expect the negotiator to pick a low attribute value as initial offer.

<sup>Hypothesis H2.</sup> The weight of an attribute and the convexity of the marginal utility function will negatively influence the amount of concessions in that attribute.

The argument underlying this hypothesis is similar to H1: a negotiator interested in obtaining a particularly good result in an attribute will make less concessions. In hypothesis H2, we do not explicitly refer to the direction of preference, since we expect the size of the concessions to be independent of the direction.

<sup>Hypothesis H3.</sup> There is a positive relationship between the initial offer and the size of concessions a negotiator makes in an attribute.

While one could view demanding initial offers and small concessions both as indicators of tough bargaining and expect a complementary relationship, H3 views the two variables as substitutes. By making a tough first offer, the negotiator creates room for future concessions. In anonymous electronic negotiations, where the parties initially have no information about each other, this behavior might be also seen as a kind of “insurance” against possible tough bargaining by unknown opponents. Hypothesis H3 is consistent with existing empirical research, which has shown a positive relationship between initial offers and concessions [5,28] and the success of a “reformed sinner” strategy combining tough initial offers and large concessions.

## 2.3. Outcomes of negotiations

Empirical studies on negotiations focus on different aspects of outcomes. Several empirical studies used agreement as an indicator of success [9,27]. But this indicator does not take into account the quality of the compromise. For this purpose, the sum of utilities of both parties was often used [11,13,14,27,32,36]. This measure was criticized because it focuses on one specific solution, while the set of Pareto-optimal solutions might contain many different solutions [40,43]. Therefore, we use Pareto-optimality as our second outcome measure. This measure was used in other studies, either alone [1] or in combination with joint payoffs [2].

As a third dimension, we consider individual outcomes. Rather than aggregated utility values, we use outcomes in each attribute to allow for a more detailed analysis of the impact of preferences.

While previous empirical studies did not link properties of utility functions to outcome dimensions, there is still some evidence of such relationships. A theoretical framework is provided by the dual concern model of negotiations. This model originates from the Managerial Grid of Blake and Mouton [3], which was later on modified by Thomas and Kilmann to characterize bargaining styles [5,41,35]. It uses two dimensions to classify negotiation strategies: concern for one's own outcome and concern for the opponent's outcome.

In empirical studies, concern for one's own outcome was often measured by aspiration levels. When preferences are represented by utility functions, we can relate concern for an attribute to the weight and the shape of the marginal utility function. A high weight is a direct indicator of high importance. While the shape of the single-attribute utility function is not directly related to importance, negotiators having a convex utility function will suffer a relatively high loss when deviating from the best value. We therefore expect them to have higher concern for that attribute, and exhibit tougher bargaining behavior.

The dual concern model predicts different negotiation strategies and outcomes for different combinations of concern. Negotiators who have low concern for their own outcome, but high concern for their opponent's outcome, will follow a yielding strategy, which is very likely to lead to a compromise. But the compromise will favor their opponent and is likely to be inefficient. Negotiators who follow the yielding strategy will not try to maximize their outcome, so the solution could be dominated. Furthermore, their opponents already obtain a good outcome with little effort and might not be motivated enough to improve their position up to the efficient frontier. The opponents could also consider full exploitation of the yielding negotiator as too risky, since even a yielding negotiator could change the strategy when finding out that the opponent is doing much better.

Negotiators who have high concern for their own outcomes, but low concern for their opponent's outcome, will follow a contending strategy, which often leads to an impasse. High concern both for the own and the opponent's outcomes leads to a problemsolving strategy resulting in an efficient compromise.

Outcomes of negotiations result from the interaction of both parties. Therefore hypotheses which refer to outcome dimensions as dependent variables need to take into account the preferences of both negotiators. The interaction between the preferences can be referred to as the level of conflict which is inherent in the problem being negotiated. It should be noted that here conflict is viewed as a property of the problem, not of the compromise solution, as it was used among others by Clyman [7].

The level of conflict between negotiators can be measured by considering the gradients of the two negotiators' utility functions in attribute space [20]. If the two gradients point into opposite directions, the level of conflict is highest, if they point into the same direction, there is not conflict at all. The latter case implies that both parties also want to influence all attributes in the same direction. When, as in the negotiation case used for our experiments, parties influence each attribute in the opposite direction, the minimum level of conflict occurs when the gradients of the two utility functions are orthogonal.

Ignoring the nonlinearity of single-attribute utility functions, the gradient of an additive utility function (1) can be approximated by the weight vector. If the level of conflict is low, the gradients are orthogonal and the two parties assign high weights to different attributes. The parties can use a log-rolling strategy to exploit these differences and make concessions in attributes less important to them, which makes it easier to reach a compromise [29,26].

We therefore use the scalar product of weight vectors to measure conflict of interest. This approach is a special case of the measure proposed by Kersten and Noronha [20], who considered general gradients rather than weight vectors, and also the case of weak opposition in which the gradients form an obtuse angle. In empirical studies [14,34], pre-assigned attribute weights were used in a similar way to manipulate the level of conflict.

In addition to weights, convexity of single-attribute utility functions also influences the level of conflict. The conflict in an attribute will be very high if both parties have convex utility functions. Negotiators who have convex utility functions in a larger number of attributes are more likely to have high concern for their own outcome, and thus are more likely to follow a contending or problem-solving strategy.

Both the scalar product and convexity are based on the assumption that the parties want to influence each attribute in opposite directions, as indicated in the case description. Since in some cases, subjects did not follow the case description in this respect, we consider the number of attributes which both parties want to change in the same direction as another factor influencing outcomes.

Since the fact that two parties have convex utility functions in the same attributes implies that they have convex utility functions at all, we cannot test the two effects at the same time. Therefore we formulate two variants of our hypothesis about agreements:

<sup>Hypothesis H4.</sup> Negotiators are less likely to reach an agreement, if

• the level of conflict, as measured by the scalar product of weight vectors, is higher;

• the number of attributes which both parties want to influence in the same direction is lower; and

• H4a the number of attributes in which both parties have convex single-attribute utility functions is higher;

• H4b the parties have convex single-attribute utility functions in a larger number of attributes.

The dual concern model predicts that a high interest in a party's own outcome is necessary to achieve an efficient agreement, although it reduces the likelihood of reaching an agreement. Thus we expect convex utility functions to have a positive influence on efficiency. A similar argument holds for the level of conflict: if preferences of the two parties are strictly opposite, all alternatives are Pareto-optimal. If gradients of the utility functions are orthogonal, many alternatives are dominated and it might be more difficult to find an efficient compromise.

Concerning monotonicity, we expect parties who want to influence an attribute in the same direction to agree on the common best value in this attribute and thus to obtain an efficient compromise more easily. We therefore formulate the following hypothesis relating to the efficiency of outcomes:

<sup>Hypothesis H5.</sup> If negotiators reach an agreement at all, the compromise is more likely to be efficient, if

• the level of conflict, as measured by the scalar product of weight vectors, is higher;

• the number of attributes which both parties want to influence in the same direction is higher; and

• H5a the number of attributes in which both parties have convex single-attribute utility functions is higher;

• H5b the parties have convex single-attribute utility functions in a larger number of attributes.

The fact that negotiators reached an agreement, as well as efficiency, are aggregate constructs which refer to the compromise as a whole. The compromise (if one is reached) specifies values for all attributes. Results at the attribute level can directly be related to the concern of a negotiator for the own outcome in that attribute. Considering both negotiators simultaneously, we therefore expect:

<sup>Hypothesis H6.</sup> The result which a negotiator achieves in an attribute will be better, if

• the negotiator has a higher weight for that attribute;

• the opponent has a lower weight for that attribute;

• the negotiator has a convex single-attribute utility function for that attribute;

• the opponent does not have a convex single-attribute utility function for that attribute;

• the monotonicity of the single-attribute utility function corresponds to the direction implied in the case description;

• the monotonicity of the opponent's single-attribute utility function does not correspond to the direction implied in the case description.

## 3. Method, measurement and data

We test our hypotheses using an existing data base of negotiation experiments conducted with the NSS Inspire [21] on the Internet in the time frame 1996 – 2004. During this time, over 3000 negotiations were performed using Inspire. Inspire was developed as a tool for teaching and research. It is used in courses on international negotiations, decision analysis, information systems, or similar subjects at several universities all over the world. Most of the experiments used for our study were carried out as part of course assignments. Out of the 4020 subjects who provided information about their occupation, 2997 (74.55%) were students. Students are rewarded with course credits for participating in the experiments. Credits are not linked to their performance; in most cases, instructors are not informed about outcomes of negotiations.

Negotiations in Inspire are conducted anonymously, all negotiators are identified only by self-defined user names. Communication between users takes place exclusively via the system, so it is not possible for a negotiator to infer the identity of the opponent e.g. from an e-mail address. Although the system does not prevent the negotiators from revealing their identity, it is not possible for their opponents to verify this information.

The experiments follow a predefined sequence. When users first log into the system, the case description is presented to them, which contains public information

Properties of single-attribute utilities

<table><tr><td rowspan="2"></td><td colspan="2">Price</td><td colspan="2">Delivery</td><td colspan="2">Payment</td><td colspan="2">Returns</td></tr><tr><td>Buyer</td><td>Seller</td><td>Buyer</td><td>Seller</td><td>Buyer</td><td>Seller</td><td>Buyer</td><td>Seller</td></tr><tr><td colspan="9">Weights</td></tr><tr><td>Mean</td><td>0.3828</td><td>0.4062</td><td>0.2297</td><td>0.1721</td><td>0.1777</td><td>0.2286</td><td>0.2098</td><td>0.1930</td></tr><tr><td>SD</td><td>0.1320</td><td>0.1317</td><td>0.0957</td><td>0.0871</td><td>0.0874</td><td>0.0888</td><td>0.1067</td><td>0.0986</td></tr><tr><td>Min</td><td>0.0000</td><td>0.0100</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>Max</td><td>0.9700</td><td>0.9709</td><td>0.9100</td><td>0.7000</td><td>1.0000</td><td>0.7400</td><td>0.8000</td><td>0.9700</td></tr><tr><td>W</td><td>***2260403</td><td></td><td>***3393878</td><td></td><td>***1669570</td><td></td><td>***2725191</td><td></td></tr><tr><td colspan="9">Monotonicity (%)</td></tr><tr><td>Strictly decreasing</td><td>67.20</td><td>1.74</td><td>71.17</td><td>4.69</td><td>7.63</td><td>79.52</td><td>79.25</td><td>4.60</td></tr><tr><td>Decreasing</td><td>21.73</td><td>1.12</td><td>20.04</td><td>5.18</td><td>1.96</td><td>7.99</td><td>12.76</td><td>1.56</td></tr><tr><td>Not monotonic</td><td>10.17</td><td>21.02</td><td>7.90</td><td>24.68</td><td>9.42</td><td>8.57</td><td>6.11</td><td>9.82</td></tr><tr><td>Increasing</td><td>0.22</td><td>19.28</td><td>0.13</td><td>15.84</td><td>8.17</td><td>0.67</td><td>0.58</td><td>7.81</td></tr><tr><td>Strictly increasing</td><td>0.67</td><td>56.85</td><td>0.76</td><td>49.62</td><td>72.82</td><td>3.26</td><td>1.29</td><td>76.22</td></tr><tr><td> $\chi^2 Original$ </td><td>***3541.22</td><td></td><td>***3104.00</td><td></td><td>***2979.56</td><td></td><td>***3467.68</td><td></td></tr><tr><td> $\chi^2 Reversed$ </td><td>***131.13</td><td></td><td>***461.61</td><td></td><td>***61.15</td><td></td><td>***98.92</td><td></td></tr><tr><td colspan="9">Shape (%)</td></tr><tr><td>Convex</td><td>35.16</td><td>31.64</td><td>55.15</td><td>16.56</td><td>20.93</td><td>21.91</td><td>40.52</td><td>18.43</td></tr><tr><td>Linear</td><td>0.49</td><td>0.27</td><td>1.20</td><td>0.04</td><td>23.56</td><td>21.33</td><td>21.51</td><td>22.85</td></tr><tr><td>Concave</td><td>64.35</td><td>68.09</td><td>43.64</td><td>83.40</td><td>55.51</td><td>56.76</td><td>37.97</td><td>58.72</td></tr><tr><td> $\chi^2$ </td><td>***1374.03</td><td></td><td>***1085.52</td><td></td><td>***498.33</td><td></td><td>***143.19</td><td></td></tr></table>

p levels are indicated as follows: <sup>⁎</sup>pb5%, <sup>⁎⁎</sup>pb1%, <sup>⁎⁎⁎</sup>pb0.01%.

for both sides and confidential information for their own side. Inspire can be used with different cases, but for this analysis, we use only negotiations based on one single case, the “Cypress-Itex”-case. This case describes a buyer–seller negotiation where the parties negotiate about four attributes of a purchase contract: price, delivery time, payment terms and conditions for the return of defective parts. In each attribute, the parties must select a value from a pre-defined set of discrete values. There are 5 possible values for price, 4 for delivery time and 3 each for the remaining two attributes.

In the next step, the system elicits the preferences of users via a modified conjoint measurement method [21]. After the preference elicitation, negotiators fill in a pre-negotiation questionnaire, which records demographical data as well as expectations for the upcoming negotiation, and the subjective evaluation of the ease and user-friendliness of the utility elicitation procedure.

Regression results for initial offers — hypothesis H1 (all data)

<table><tr><td>Property</td><td></td><td>Price</td><td>Delivery</td><td>Payment</td><td>Returns</td></tr><tr><td rowspan="3">Convex</td><td> $\beta$ </td><td>***0.0214</td><td>0.0048</td><td>**0.0277</td><td>***0.0508</td></tr><tr><td>t</td><td>3.6100</td><td>0.5800</td><td>2.8400</td><td>6.3300</td></tr><tr><td>p</td><td>0.0003</td><td>0.5620</td><td>0.0045</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Monotonic</td><td> $\beta$ </td><td>***0.1128</td><td>***0.1454</td><td>***-0.1437</td><td>***0.1500</td></tr><tr><td>t</td><td>34.1230</td><td>38.6340</td><td>-38.4880</td><td>37.9660</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Weight</td><td> $\beta$ </td><td>**0.0670</td><td>***0.2667</td><td>***0.3376</td><td>***0.3313</td></tr><tr><td>t</td><td>3.1440</td><td>6.7230</td><td>7.4490</td><td>9.5720</td></tr><tr><td>p</td><td>0.0017</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="4">Role=Sell</td><td> $\beta$ </td><td>***-0.0410</td><td>***-0.1771</td><td>***0.0555</td><td>***-0.0354</td></tr><tr><td>t</td><td>-7.2300</td><td>-20.5720</td><td>6.6670</td><td>-4.8280</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td> $R^{2}$ </td><td>0.2353</td><td>0.4049</td><td>0.2810</td><td>0.2827</td></tr></table>

p levels are indicated as follows: <sup>⁎</sup>pb5%, <sup>⁎⁎</sup>pb1%, <sup>⁎⁎⁎</sup>pb0.01%.

Regression results for initial offers — hypothesis H1 (correct monotonicity only)

<table><tr><td>Property</td><td></td><td>Price</td><td>Delivery</td><td>Payment</td><td>Returns</td></tr><tr><td rowspan="3">Convex</td><td> $\beta$ </td><td>***0.0304</td><td>***0.0287</td><td>**0.0302</td><td>***0.0302</td></tr><tr><td>t</td><td>5.3860</td><td>3.3420</td><td>2.9250</td><td>3.6540</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>0.0008</td><td>0.0035</td><td>0.0003</td></tr><tr><td rowspan="3">Monotonic</td><td> $\beta$ </td><td>***0.0398</td><td>***0.0511</td><td>***0.0721</td><td>***0.0482</td></tr><tr><td>t</td><td>6.4320</td><td>5.7150</td><td>-4.9600</td><td>4.1810</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Weight</td><td> $\beta$ </td><td>***0.0794</td><td>***0.3827</td><td>***0.4148</td><td>***0.3772</td></tr><tr><td>t</td><td>3.9230</td><td>9.4040</td><td>8.9350</td><td>11.0090</td></tr><tr><td>p</td><td>0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="4">Role=Sell</td><td> $\beta$ </td><td>***0.0358</td><td>***0.1327</td><td>***0.0511</td><td>***0.0309</td></tr><tr><td>t</td><td>-6.7330</td><td>-15.0710</td><td>6.0140</td><td>-4.2960</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td> $R^{2}$ </td><td>0.0314</td><td>0.1561</td><td>0.0491</td><td>0.0469</td></tr></table>

p levels are indicated as follows: <sup>⁎</sup>pb5%, <sup>⁎⁎</sup>pb1%, <sup>⁎⁎⁎</sup>pb0.01%.

During the actual negotiations, which can last up to three weeks, users exchange offers containing values for all attributes, as well as free text messages. Utility values of their own and the opponent's offers are presented to the users in graphical and numerical forms. Inspire logs all the offers and text messages as well as the final compromise, if the parties reach an agreement. Using the utility functions, Inspire then determines whether the compromise is Pareto-optimal. If it is dominated, the system displays alternatives which dominate it and negotiations may continue. Since we are mainly interested in the direct effects of preference structures, this second stage is not included in our analysis. Finally, a post-negotiation questionnaire is administered to the users, in which their subjective assessments of the negotiation process and the system are recorded.

In total, 2990 negotiations were set up using the “Cypress-Itex” case in the period under study. Excluding incomplete experiments, the data base used for this study contains 2241 usable negotiation records. In this sample, 1561 negotiations (69.66%) resulted in an agreement, 686 agreements (43.95%) were Pareto-optimal.

Table 1 gives an overview of the properties of the utility functions. We classify monotonicity into five categories, differentiating between strictly monotonic and monotonic functions. As Table 1 shows, some negotiators had non-monotonic utility functions or even monotonic functions which contradicted the case description. The latter cases probably indicate a misunderstanding of the case description or an error during utility elicitation. Non-monotonic functions could also be an indicator of strategic behavior by subjects who assigned high utilities to a likely compromise value in order to reach a high utility level.

To obtain an indicator of the shape of the singleattribute utility functions, we used a similar method as Pennings and Smidts [33]. A generalized exponential function was fitted to the standardized data. Depending on the parameter value, functions were then classified as convex, concave or (approximately) linear.

In all structural parameters, there are significant differences between buyers and sellers. While such differences can naturally be expected for monotonicity, they also occur for the other properties. The difference in monotonicity remains significant when the direction is adjusted for the different roles. This is an important indicator of the effectiveness of the case description. Subjects playing different roles perceived the case differently. This increases the credibility of our experiments as a whole, and in particular of the preference models.

Regression results for concessions — hypotheses H2 and H3

<table><tr><td>Property</td><td></td><td>Price</td><td>Delivery</td><td>Payment</td><td>Returns</td></tr><tr><td rowspan="3">Monotonic</td><td> $\beta$ </td><td>**-0.0132</td><td>***-0.0283</td><td>***-0.0357</td><td>***-0.0383</td></tr><tr><td>t</td><td>-2.7070</td><td>-5.4110</td><td>-6.2910</td><td>-5.3190</td></tr><tr><td>p</td><td>0.0068</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Convex</td><td> $\beta$ </td><td>***-0.0458</td><td>**-0.0280</td><td>-0.0130</td><td>***-0.0701</td></tr><tr><td>t</td><td>-5.7090</td><td>-2.7860</td><td>-0.9830</td><td>-5.2490</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>0.0054</td><td>0.3260</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Weight</td><td> $\beta$ </td><td>***-0.4029</td><td>***-0.6787</td><td>***-0.8266</td><td>***-1.0133</td></tr><tr><td>t</td><td>-14.3370</td><td>-14.2140</td><td>-13.6170</td><td>-17.9050</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Role=Sell</td><td> $\beta$ </td><td>***-0.0385</td><td>***0.3545</td><td>***-0.1683</td><td>***0.1156</td></tr><tr><td>t</td><td>-5.0560</td><td>32.3150</td><td>-15.1160</td><td>9.7040</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="4">Initial offer</td><td> $\beta$ </td><td>***0.6649</td><td>***0.8009</td><td>***0.7863</td><td>***0.7709</td></tr><tr><td>t</td><td>34.8890</td><td>44.6610</td><td>40.7890</td><td>32.5250</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td> $R^2$ </td><td>0.3581</td><td>0.4878</td><td>0.4054</td><td>0.3161</td></tr></table>

p levels are indicated as follows: <sup>⁎</sup>pb5%, <sup>⁎⁎</sup>pb1%, <sup>⁎⁎⁎</sup>pb0.01%.

Table 5  
Binomial regression results for agreement — hypothesis H4

<table><tr><td></td><td>Estimate</td><td>Std. Error</td><td>z value</td><td>Pr(&gt;|z|)</td></tr><tr><td colspan="5">Hypothesis H4: H4a</td></tr><tr><td>Intercept</td><td>***1.73599</td><td>0.28362</td><td>6.121</td><td>&lt;0.0001</td></tr><tr><td>Scalar product weights</td><td>**-2.97302</td><td>1.00113</td><td>-2.970</td><td>0.0030</td></tr><tr><td>N. common convex</td><td>***-0.37547</td><td>0.06761</td><td>-5.553</td><td>&lt;0.0001</td></tr><tr><td>N. same direction</td><td>* 0.16185</td><td>0.07677</td><td>2.108</td><td>0.0350</td></tr><tr><td colspan="5">AIC: 2715.5</td></tr><tr><td colspan="5">Hypothesis H4: H4b</td></tr><tr><td>Intercept</td><td>***2.10068</td><td>0.29128</td><td>7.212</td><td>&lt;0.0001</td></tr><tr><td>Scalar product weights</td><td>**-3.01805</td><td>1.00010</td><td>-3.018</td><td>0.0026</td></tr><tr><td>N. convex utilities</td><td>***-0.19424</td><td>0.02823</td><td>-6.882</td><td>&lt;0.0001</td></tr><tr><td>N. same direction</td><td>*0.17312</td><td>0.07690</td><td>2.251</td><td>0.0244</td></tr><tr><td colspan="5">AIC: 2698.1</td></tr></table>

p levels are indicated as follows: <sup>⁎</sup>pb5%, <sup>⁎⁎</sup>pb1%, <sup>⁎⁎⁎</sup>pb0.01%.

## 4. Results

## 4.1. Process

We estimate regression equations on the initial offers and total concessions in each attribute. Table 2 shows the results for initial offers, adjusted for the direction of improvement for the respective role. Thus, a positive coefficient indicates a “tougher” initial offer. For this regression (as well as Table 4), the indicators for monotonicity are also adjusted so that positive values indicate the correct direction according to the case description. In most cases, the results confirm hypothesis H1. There is a significant positive impact of weights in all attributes. For convexity, H1 is confirmed for three attributes. There is also a significant impact of monotonicity: subjects with incorrect monotonicity make less tough initial offers.

![](/api/attachments/57B2W758/fulltext/images/a1f72a70633f4037a66b68ce594696c8bde8d2b347b56375204d3d83b71d2b80.jpg)  
Fig. 2. Number of convex utilities and compromise.

H1 refers to initial offers in terms of the negotiator's preferences (and not the direction specified by the case). We therefore performed a second analysis where we dropped subjects who had the wrong monotonicity. The results of this analysis are shown in Table 3. Surprisingly, the fit of the model decreases dramatically. One reason seems to be the highly skewed distribution of initial offers for this group: in all attributes, more than 70% of all users initially demanded the best possible value.

To test hypotheses H2 and H3, we estimate linear regression models on concessions in each attribute (Table 4). Concessions are measured as the difference between the initial offer and the final compromise, where both values are standardized according to the direction of improvement specified in the case.

In hypothesis H2, we argue that negotiators with a high weight or convex utilities negotiate more toughly and thus make less concessions. This hypothesis is largely confirmed. The only exception occurs in the attribute payment terms, where convexity of the singleattribute utility function does not have a significant impact. Contrary to our expectations, monotonicity does have a significant impact: negotiators make less concessions in an attribute if their utility function for this attribute is monotonic in the correct direction.

Hypothesis H3 relates initial offers and concessions to each other. The results confirm the substitution effect between these tactics, which was already found in previous studies [5,28]: when negotiators make demanding initial offers, they are also more willing to make concessions later on.

Table 6  
Binomial regression results for efficiency — hypothesis H5

<table><tr><td></td><td>Estimate</td><td>Standard error</td><td>z value</td><td>Pr(&gt;|z|)</td></tr><tr><td colspan="5">Hypothesis H5: H5a</td></tr><tr><td>Intercept</td><td>0.09362</td><td>0.29681</td><td>0.315</td><td>0.7525</td></tr><tr><td>Scalar product weights</td><td>-0.76664</td><td>1.06780</td><td>-0.718</td><td>0.4728</td></tr><tr><td>N. common convex</td><td>**-0.25190</td><td>0.08600</td><td>-2.929</td><td>0.0034</td></tr><tr><td>N. same direction AIC: 2320.7</td><td>0.13996</td><td>0.07203</td><td>1.943</td><td>0.0520</td></tr><tr><td colspan="5">Hypothesis H5: H5b</td></tr><tr><td>Intercept</td><td>0.34941</td><td>0.30365</td><td>1.151</td><td>0.2499</td></tr><tr><td>Scalar product weights</td><td>-0.81624</td><td>1.06929</td><td>-0.763</td><td>0.4453</td></tr><tr><td>N. convex utilities</td><td>***-0.13991</td><td>0.03173</td><td>-4.409</td><td>&lt;0.0001</td></tr><tr><td>N. same direction AIC: 2309.7</td><td>*0.15818</td><td>0.07250</td><td>2.182</td><td>0.0291</td></tr></table>

p levels are indicated as follows: <sup>⁎</sup>pb5%, <sup>⁎⁎</sup>pb1%, <sup>⁎⁎⁎</sup>pb0.01%.

![](/api/attachments/57B2W758/fulltext/images/22e763a243f4756f4fa2bf4283017799b6e280a0bd585001f2899c7a18824a85.jpg)  
Fig. 3. Number of utilities with same monotonicity and frequency of efficient compromise.

## 4.2. Outcomes

We test hypothesis H4 by estimating binomial glm models using a logistic link function [24] to account for the binary dependent variable of achieving a compromise. Separate models are estimated for the two variants H4a and H4b (Table 5).

Both models support the hypothesis. A higher level of conflict, as measured by the scalar product of weights, significantly reduces the probability of reaching an agreement. Attributes which both parties want to influence in the same direction increase the probability of agreement, although this influence is only significant at the 5% level. The models also indicate a highly significant impact of convexity for both variants of hypothesis H4. According to Akaike's information criterion (AIC), the model for hypothesis H4b provides a better fit than the model for hypothesis H4a. Thus the individual property of convex utility is sufficient to increase the likelihood of an impasse, it is not necessary that this type of preferences is matched by the other party. However, the explanatory power of the model is rather weak (deviance = 2690.1 vs. 2750.8 for the null model).

Fig. 2 displays the relative frequency of agreements for different numbers of convex utility functions involved. There is a clear declining trend, which is only interrupted when most utilities are convex. However, these cases refer to very few experiments, 6 or more convex utility functions occurred in only about 4% of all experiments.

To test hypotheses H5a and H5b (Table 6), we use similar models. These results provide only partial support for our hypotheses, and in some instances contradict them. Concerning the level of conflict, H5 must be rejected. The number of attributes influenced in the same direction has only a weakly significant effect, which nevertheless can clearly be observed in a plot of the data (Fig. 3).

The only highly significant impact results from convexity. However, the direction of this effect is contrary to our expectations. While hypothesis H5, based on the dual concern model, argued that strong interest in the negotiator's own outcome would lead to an efficient compromise, the influence is negative in both models. Again, the model using individual counts of convex utility functions provides a slightly better fit according to the AIC criterion.

Regression results for compromise values — hypothesis H6

<table><tr><td colspan="2"></td><td>Price</td><td>Delivery</td><td>Payment</td><td>Returns</td></tr><tr><td rowspan="3">Weight buyer</td><td> $\beta$ </td><td>***-0.4722</td><td>***-33.6446</td><td>***62.9952</td><td>***-12.4333</td></tr><tr><td>t</td><td>-13.5500</td><td>-14.0970</td><td>13.1060</td><td>-18.3980</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Weight seller</td><td> $\beta$ </td><td>***0.3265</td><td>***23.8557</td><td>***-44.5086</td><td>***9.3317</td></tr><tr><td>t</td><td>9.4190</td><td>8.9760</td><td>-9.6940</td><td>12.7070</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Convex buyer</td><td> $\beta$ </td><td>***-0.0469</td><td>***-1.8044</td><td>**-3.2949</td><td>***-0.8846</td></tr><tr><td>t</td><td>-4.7050</td><td>-3.8920</td><td>-3.1500</td><td>-5.8890</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>0.0001</td><td>0.0017</td><td>&lt;0.0001</td></tr><tr><td rowspan="3">Convex seller</td><td> $\beta$ </td><td>**0.0261</td><td>-0.3833</td><td>***-4.0513</td><td>0.3604</td></tr><tr><td>t</td><td>2.6200</td><td>-0.5880</td><td>-3.9960</td><td>1.8640</td></tr><tr><td>p</td><td>0.0089</td><td>0.5565</td><td>0.0001</td><td>0.0624</td></tr><tr><td rowspan="3">Monotonic buyer</td><td> $\beta$ </td><td>***0.0300</td><td>***1.4897</td><td>***3.8086</td><td>***0.6914</td></tr><tr><td>t</td><td>4.7550</td><td>4.4900</td><td>11.0590</td><td>6.9920</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td rowspan="4">Monotonic seller</td><td> $\beta$ </td><td>***0.0520</td><td>***2.5991</td><td>***4.9123</td><td>***0.7159</td></tr><tr><td>t</td><td>10.9810</td><td>12.9930</td><td>11.2470</td><td>10.4980</td></tr><tr><td>p</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td> $R^2$ </td><td>0.2383</td><td>0.2382</td><td>0.2603</td><td>0.3215</td></tr></table>

p levels are indicated as follows: <sup>⁎</sup>pb5%, <sup>⁎⁎</sup>pb1%, <sup>⁎⁎⁎</sup>pb0.01%.

Our final hypothesis H6 refers to the attribute values in the compromise. To test this hypothesis, we estimate linear regression models on the compromise values of each attribute. The results shown in Table 7 largely confirm hypothesis H6. Higher attribute weights influence each attribute in the direction which is better for the party concerned. In most cases, convexity has a similar effect. As could be expected, if parties want to maximize an attribute, its compromise level increases. To take into account that the effects of weights and convexity work in the opposite direction if negotiators have the wrong direction of preference, the same model (except for monotonicity) was estimated using only subjects with the correct monotonicity. The results for this data set were very similar and thus are not reported here.

## 5. Conclusions

The main aim of this study was to analyze the fundamental assumptions in preference-based decision and negotiation support indicated in Fig. 1. To a considerable extent, our empirical analysis has confirmed the existence of those relationships. In particular, the preferences encoded in utility functions are strongly reflected in the behavior during negotiations, concerning both initial offers and the amount of concessions.

The present study, which is based on experiments using a single system, does not allow us to infer whether subjects performed more consistently with their preferences than they would have done without the system. But the close relationship between elicited preferences and actual behavior is nevertheless reassuring. If elicited preferences make a difference between subjects possessing different utility functions, it is also quite likely that explicit knowledge and use of one's utility function would also make a difference.

While the link between preference model and actual behavior could clearly be established, the subsequent step to outcomes is less clear. Whether negotiators will reach an agreement at all, and if so, whether it will be efficient, can be predicted only to a rather limited extent from their utility functions. Evidently, other factors have a strong impact on these outcome dimensions. But this result can also be seen as encouraging to negotiators: no negotiation is a priori doomed to fail because of the preferences of the parties involved; there is always a chance of reaching agreement, even if preferences indicate a strong conflict. Of course, the opposite is also true: even negotiations involving favorable combinations of preferences might fail.

The particular structure of a compromise, once it is found, reflects the preferences of negotiators more closely. Negotiators using Inspire are indeed able to achieve good results in the attributes which are important to them. Although we did not explicitly model the intermediate steps leading to this influence, this relationship is a positive sign for the effectiveness of preference-based decision and negotiation support.

While our study thus conveys a positive message concerning the possibility of preference-based decision and negotiation support, it nevertheless has certain limitations. Although the size of the database used for our analyses is larger than in most empirical studies, the data used here was collected using just one NSS, one type of preference model, and one negotiation case. Thus, generalizability remains an open question and requires further empirical work. Like in all similar experimental studies, we only measured and analyzed the attributes of the problem which were listed in the case description and for which utility functions were elicited. It remains possible that the subjects, in addition to those attributes, considered additional attributes (like fairness) in their decisions and thus had “discrepant values” [8] which could not be considered in our analysis.

Our empirical results raise several new questions, which warrant further research. As the models for agreement and efficiency only have a low explanatory power, the question arises which other factors influence those two outcome dimensions. Reaching consensus probably does not only depend on preferences of negotiators, but also on personal factors like the ability to build a relationship with the opponent [22]. The results about outcomes also pose some challenges to negotiation research: The fact that negotiators with convex utilities, who presumably have a high concern for their own outcomes, are less likely to find an efficient solution contradicts the dual concern model. It is also puzzling that the likelihood of an agreement and its efficiency seem to depend more on individual characteristics than on the interaction of preferences between the two parties.

The present study has looked at behavior during negotiations only at the rather aggregate level of total concessions and initial offers. Going into more detail, to the level of individual offers and counteroffers, could add insight into the impact of preferences on negotiator behavior, and perhaps also offer additional explanations for negotiation results.

## References

[1] R. Barkhi, V.S. Jacob, H. Pirkul, An experimental analysis of face to face versus computer mediated communication channels, Group Decision and Negotiation 8 (4) (1999) 325–347.

[2] G.E. Beroggi, An experimental investigation of virtual negotiations with dynamic plots, Group Decision and Negotiation 9 (5) (2000) 415–429.

[3] R. Blake, J. Mouton, The Managerial Grid, Gulf, Houston, 1964.

[4] W.P. Bottom, Negotiator risk: sources of uncertainty and the impact of reference points on negotiated agreements, Organizational Behavior and Human Decision Processes 76 (2) (1998) 89–112.

[5] P.J. Carnevale, D.G. Pruitt, Negotiation and mediation, Annual Review of Psychology 43 (1992) 531–582.

[6] D.K. Chiu, S. Cheung, P.C. Hung, S.Y. Chiu, A.K. Chung, Developing e-negotiation support with a meta-modeling approach in a web services environment, Decision Support Systems 40 (2005) 51–69.

[7] D.R. Clyman, Measuring cooperation in negotiations: the impossible dream, in: R.J. Zeckhauser, R.L. Keeney, J.K. Sebenius (Eds.), Wise Choices: Decisions, Games, and Negotiations, Harvard Business School Press, Boston, Mass, 1996, pp. 388–399.

[8] D.R. Clyman, T.M. Tripp, Discrepant values and measures of negotiator performance, Group Decision and Negotiation 9 (4) (2000) 251–274.

[9] D. Coursey, Bilateral bargaining, Pareto optimality, and the empirical frequency of impasse, Journal of Economic Behavior and Organization 3 (1982) 243–259.

[10] J.R. Curhan, M.A. Neale, L. Ross, Dynamic valuation: preference changes in the context of face-to-face negotiation, Journal of Experimental Social Psychology 40 (2004) 142–151.

[11] M.M. Delaney, A. Foroughi, W.C. Perkins, An empirical study of the efficacy of a computerized negotiation support system (NSS), Decision Support Systems 20 (1997) 185–197.

[12] G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (1987) 589–609.

[13] A. Foroughi, W.C. Perkins, M.T. Jelassi, An empirical study of an interactive, session-oriented computerized negotiation support system (NSS), Group Decision and Negotiation 4 (1995) 485–512.

[14] A. Foroughi, W.C. Perkins, L.M. Jessup, A comparison of audioconferencing and computer conferencing in a dispersed negotiation setting: efficiency matters! Journal of Organizational and End User Computing 17 (3) (2005) 1–26.

[15] B. Jain, J. Solomon, The effect of task complexity and conflict handling styles on computer-supported negotiations, Information and Management 37 (4) (2000) 161–168.

[16] M. Jarke, Knowledge sharing and negotiation support in multiperson decision support systems, Decision Support Systems 2 (1) (1986) 93–102.

[17] M.T. Jelassi, A. Foroughi, Negotiation support system: an overview of design issues and existing software, Decision Support Systems 5 (2) (1989) 167–181.

[18] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, J. Wiley & Sons, New York 1976.

[19] G.E. Kersten, E-negotiation Systems: Interaction of People and Technologies to Resolve Conflicts, Interneg Research Report INR 08/04 2004.

[20] G.E. Kersten, S.J. Noronha, Rational agents, contract curves, and inefficient compromises, IEEE Transactions on Systems, Man and Cybernetics 28 (3) (1998) 326–338.

[21] G.E. Kersten, S.J. Noronha, WWW-based negotiation support: design, implementation, and use, Decision Support Systems 25 (2) (1999) 135–154.

[22] S. Koeszegi, K. Srnka, E.-M. Pesendorfer, Comparing Webbased Negotiation Processes: A Combined Qualitative–Quantitative Approach, Tech. Rep. OP 2004-02, Dept. of Business Studies, University of Vienna 2004.

[23] L.-H. Lim, I. Benbasat, A theoretical perspective of negotiation support systems, Journal of Management Information Systems 9 (3) (1992) 27–44.

[24] J.S. Long, Regression Models for Categorical and Limited Dependent Variables, Sage, Thousand Oaks 1997.

[25] A. Mateos, A. Jimenez, S. Rios-Insua, Monte Carlo simulation techniques for group decision making with incomplete information, European Journal of Operational Research 174 (2006) 1842–1864.

[26] R.G. Milter, T.A. Darling, J.L. Mumpower, The effects of substantive task characteristics on negotiators' ability to reach efficient agreements, Acta Psychologica 93 (1996) 207–228.

[27] D.A. Moore, T.R. Kurtzberg, L.L. Thompson, M.W. Morris, Long and short routes to success in electronically mediated negotiations: group affiliations and good vibrations, Organizational Behavior and Human Decision Processes 77 (1) (1999) 22–43.

[28] S. Moran, I. Ritov, Initial perceptions in negotiations: evaluation and response to ‘logrolling’ offers, Journal of Behavioral Decision Making 15 (2) (2002) 101–124.

[29] J.L. Mumpower, The judgement policies of negotiators and the structure of negotiation problems, Management Science 37 (10) (1991) 1304–1324.

[30] G.B. Northcraft, S.E. Brodt, M.A. Neale, Negotiating with nonlinear subjective utilities: why some concessions are more equal than others, Organizational Behavior and Human Decision Processes 63 (3) (1995) 298–310.

[31] G.B. Northcraft, J.N. Preston, M.A. Neale, P.H. Kim, M.C. Thomas-Hunt, Non-linear preference functions and negotiated outcomes, Organizational Behavior and Human Decision Processes 73 (1) (1998) 54–75.

[32] M. Olekalns, P.L. Smith, Social motives in negotiation: the relationships between dyad composition, negotiation processes and outcomes, International Journal of Conflict Management 14 (3/4) (2003) 233–254.

[33] J.M.E. Pennings, A. Smidts, The shape of utility functions and organizational behavior, Management Science 49 (9) (2003) 1251–1263.

[34] W.C. Perkins, J.C. Hershauer, A. Foroughi, M.M. Delaney, Can a negotiation support system help a purchasing manager, Journal of Supply Chain Management 32 (2) (1996) 37–45.

[35] D.G. Pruitt, Strategic choice in negotiation, The American Behavioral Scientist 27 (2) (1983) 167–194.

[36] J.M. Purdy, P. Nye, P.V. Balakrishnan, The impact of communication media on negotiation outcomes, International Journal of Conflict Management 11 (2) (2000) 162–187.

[37] A. Rangaswamy, G. Shell, Using computers to realize joint gains in negotiations: toward an “Electronic bargaining table”, Management Science 43 (8) (1997) 1147–1163.

[38] A. Rangaswamy, K. Starke, Computer-mediated negotiations: review and research opportunities, in: A. Kent (Ed.), Encyclopedia of Microcomputers, vol. 25, Dekker, New York, 2000, pp. 47–71.

[39] M.S. Silver, Decision support systems: directed and nondirected change, Information Systems Research 1 (1990) 47–70.

[40] J. Teich, P. Korhonen, H. Wallenius, J. Wallenius, Conducting dyadic multiple issue negotiation experiments: methodological recommendations, Group Decision and Negotiation 9 (4) (2000) 347–354.

[41] K.W. Thomas, Conflict and conflict management: reflections and update, Journal of Organizational Behavior 13 (1992) 265–274.

[42] C.H. Tinsley, K.M. O'Connor, B.A. Sullivan, Tough guys finish last: the perils of a distributive reputation, Organizational Behavior and Human Decision Processes 88 (2002) 621–642.

[43] T.M. Tripp, H. Sondak, An evaluation of dependent variables in experimental negotiation studies: impasse rates and Pareto efficiency, Organizational Behavior and Human Decision Processes 51 (1992) 273–295.

[44] A. Valenzuela, J. Srivastava, S. Lee, The role of cultural orientation in bargaining under incomplete information: differences in causal attributions, Organizational Behavior and Human Decision Processes 96 (2005) 72–88.

[45] R. Vetschera, Group decision and negotiation support — a methodological survey, OR Spektrum 12 (1990) 67–77.

[46] J.B. White, R. Tynan, A.D. Galinsky, L. Thompson, Face threat sensitivity in negotiation: roadblock to agreement and joint gain,

Organizational Behavior and Human Decision Processes 94 (2004) 102–124.

[47] Q. Zhang, J.C. Chen, P.P. Chong, Decision consolidation: criteria weight determination using multiple preference formats, Decision Support Systems 38 (2004) 247–258.

<sup>Rudolf Vetschera</sup> is a professor of organization and planning at the school of Business, Economics and Statistics, University of Vienna, Austria. He holds a PhD in economics and social sciences from the University of Vienna, Austria. Before his current position, he was full professor of Business Administration at the University of Konstanz, Germany. He has published three books and about seventy papers in reviewed journals and collective volumes. His main research area is in the intersection of organization, decision theory, and information systems, especially in network organizations.
