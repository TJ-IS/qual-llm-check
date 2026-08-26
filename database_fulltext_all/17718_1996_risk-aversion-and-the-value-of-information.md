---
otero_id: 17718
otero_key: "AV23PYZT"
title: "Risk aversion and the value of information"
authors: "Raja Nadiminti; Tridas Mukhopadhyay; Charles H. Kriebel"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00023-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Risk aversion and the value of information

Raja Nadiminti, Tridas Mukhopadhyay, Charles H. Kriebel \*

Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh, PA 15213-3890, USA

## Abstract

Determining the value of information is a fundamental research problem for information system scientists. Unfortunately, very little research exists that examines the relationship between risk aversion and the value of information. This is surprising because empirical studies show that most managers are risk averse rather than risk neutral. Moreover, the small literature that exists appears to be in conflict. We have developed a framework to examine the relationship between the value of information and risk aversion. We show that the method of payment for information must be considered in determining this relationship. We have used the Arrow–Pratt measure of risk aversion to derive explicit conditions under which the value of information increases (decreases) with risk aversion. From our analysis it is clear that earlier work has depicted a limited view of the relationship between risk aversion and value of information. Our analysis is applicable to the ex-post evaluation of transaction processing systems and a subset of decision and expert support systems.

Keywords: Information economics; Value of information; Risk aversion; Costless information; Costly information

## 1. Introduction

Determining the value of information is a fundamental research problem for information system (IS) scientists. Information economics provides a natural framework for investigating this research question. Recent work in this area has examined the value of information in a general setting as well as in specific instances. For example, Barua, Kriebel and Mukhopadhyay [5] have developed a general framework linking IS design with information value. Moore and Whinston [19,20], on the other hand, have developed a formal model of decision support systems using the information economics approach. Similarly, Barron and Saharia [4] have determined optimal information structures for the seller of a search good.

Unfortunately, very little research exists that examines the relationship between risk aversion and the value of information. This is surprising because empirical studies show that most managers are risk averse rather than risk neutral $[27]$ . Moreover, the small literature that exists appears to be in conflict. Consider, for example, two studies one by Freixas and Kihlstrom $[9]$ and the other by Tull and Hawkins $[27]$ . Freixas and Kihlstrom conclude that as risk aversion increases, demand for information decreases. They offer the following explanation for this counter intuitive result.

"When the decision to buy information is made, the buyer does not know whether he will receive good news or bad when information arrives. Thus, ex-ante, the returns to information is uncertain, and more risk averse buyers should be less willing to accept the risks associated with its acquisition (9, p. 93)."

Tull and Hawkins, on the other hand, conclude that the dollar value of information is more for a more risk averse decision maker. Their result implies that a more risk averse decision maker would have a greater demand for information. Thus, these two studies appear to be in conflict.

The purpose of our analysis is to better explain how information systems evaluation may depend on factors beyond the specific decision setting, such as attitude toward risk and conditions of payment. What sets our paper apart from other work is the more realistic assumption of risk aversion rather than risk neutrality. Through our analysis, we are also able to reconcile the seeming discrepancies in the work by Freixas and Kihlstrom and the work by Tull and Hawkins.

We show that the relationship between risk aversion and the demand for information depends on the method of payment for the information. Information can either be costless or costly. The payment for costly information in turn can be either ex-ante or contingent upon its positive incremental value. In this paper, we develop a framework to handle different types of information systems with differing modes of payment. From our analysis it is clear that earlier work has depicted a limited view of the relationship between risk aversion and the value of information.

Our framework applies to a broad range of information systems. Our model can be used to analyze structured decisions and some semistructured decisions. $^{1}$ Thus, our results hold for transaction processing systems and a subset of decision and expert support systems. However, we require that the capabilities of the systems are well understood and, thus, exclude ex-ante evaluation of unknown capabilities.

The role of the information system in our model is to assign probabilities to the relevant states of nature. The success of a decision depends upon which specific state materializes. The payoff obtained is independent of the system used and is contingent on the success of the decision (i.e., a match between the action and the revealed state of nature). Given two different systems, the probabilities assigned to the states by the systems are expected to be different. We examine how risk averse managers would evaluate information provided by such systems. Would a more risk averse manager ascribe more or less value compared to another manager to the same information?

Our analysis does not concern the classic decision theory question of whether or not a decision maker should purchase information from some source ex-ante. The answers to that issue are well known [12]. Rather we consider how the method of payment will influence the demand for information from existing sources by a decision maker with a negative exponential utility function. The literature in information economics contains the result that there is no general monotonic relationship between the (classical) information value and risk aversion. We derive explicit conditions under which the value of information increases (decreases) with risk aversion.

The organization of the paper is as follows. In Section 2, we discuss the relevant prior work. Next we describe the basic model in Section 3. We consider the value of costless information in Section 4 and costly information in Section 5. We discuss the implications of our work in Section 6 and offer concluding remarks in Section 7.

## 2. Prior work

Research in information economics has led to a formal framework for determining the value of information. The value of information is examined from both demand and supply viewpoints. The demand value of information is the maximum amount in dollars that a buyer would be willing to pay for the information [12]. The supply value, on the other hand, is the minimum amount the supplier is willing to accept to provide the information. The demand and supply values are usually not the same except for linear and exponential utility functions [21]. Our focus in this paper is on the demand value of information. $^{2}$

The traditional measure of the risk of a gamble is the variance of its return. However, this measure does not take into account the expected return on risk. Rothschild and Stiglitz [22] introduce a definition of risk for gambles with identical expected return. A gamble Y is considered riskier than a gamble X if the cumulative distribution of Y is the sum of the cumulative distribution of X and a noise component. Sarin and Weber [23] review models of perceived riskiness and measures of risk based on the expected utility theory literature. They also discuss several risk-value models where the preference for a gamble is determined by its riskiness and its value.

The Arrow–Pratt measure of risk aversion is based on the concavity of the utility function $[3]$ , and is independent of the value of the gamble. It is a widely used measure of absolute risk aversion. Dyer and Sarin $[7]$ propose a measure of relative risk aversion. Their measure compares an individual's utility function to his strength of preference function. Bell $[6]$ introduces an absolute measure of risk for one-switch utility functions that characterize a change of the preferred alternative gamble beyond a threshold level of wealth (i.e., the switching point).

The research on risk aversion and value of information is scant. However, we have two notable examples. Tull and Hawkins [27] use a certainty equivalent to measure the value of costless information. They conclude that a risk averse person will value information more highly than one who is risk neutral. Freixas and Kihlstrom [9], on the other hand, consider costly information, and show that demand for information decreases with an increase in risk aversion. We show that demand for information can increase or decrease with risk aversion for both costly and costless information.

Finally, we mention the work by Gould [10] who examined the relationship between riskiness of a project and the value of perfect information. When riskiness is measured by the variance of the project payoff, the value of perfect information decreases with the riskiness of the project. However, when riskiness is measured in the Rothschild–Stiglitz sense, the value of perfect information increases with the riskiness of the project. Our results complement those of Gould with the difference that we focus on the Arrow–Pratt measure of risk aversion of the decision maker rather than the riskiness of the project.

## 3. Basic model

There are many different objectives for determining the value of information. For example, Ahituv [1] states that the value of information depends on at least three issues:

1. Whose value is being measured? Individual or group?

2. Which value is being measured? Perceived or normative?

3. When is the value being measured? Ex-post or ex-ante?

Our objective is to measure the ex-post, normative value of information to an individual decision maker. Our focus is on a risk averse manager who may receive information from an internal information system services department or acquire information from an external source for a payment. Thus, we consider different methods of payment for the information in our analysis.

Our analysis is to help managers evaluate one or more existing sources of information. We require that the capabilities of the systems are well understood. In other words, a fully developed system or a functional prototype is assumed to be available. Thus, the evaluation of the information source is ex-post and based on the use of the information. However, the evaluation is performed before the state of nature is revealed because there may be a considerable time gap between taking an action and realizing the payoff. $^{3}$ Our analysis is not applicable to ex-ante evaluation of proposed system development projects.

## 3.1. Decision problem

Consider a decision maker (DM) with n mutually exclusive and exhaustive activities or decision alternatives. The success of an activity or decision alternative is contingent upon the occurrence of the corresponding state of nature. $^{4}$ If the state i occurs, then the DM receives $x_{i}$ for each dollar invested in the activity i and nothing otherwise. $^{5}$ The DM has an endowment of “a” dollars which she/he invests in the alternative that maximizes her/his expected utility. The subjective probability that alternative i succeeds (or state i occurs) is $p_{I}$ with $\Sigma p_{i}=1$ . Then the DM chooses activity a if $p_{\alpha}\mathrm{U}(ax_{\alpha})\geq p_{j}U(ax_{j})$ for $\forall j\in(1,n)$ , where $U(\cdot)$ is her/his utility function. For the DM, $p_{\alpha}$ can also be interpreted as her/his subjective probability of success.

If the DM uses a different information system or gains additional information, her/his subjective probability of state i changes to $q_{i}$ with $\sum q_{i}=1$ . However, neither the decision alternatives nor the corresponding payoffs change in this scenario. Suppose the DM selects activity $\beta$ as a result, $q_{\beta}U(ax_{\beta})\geq q_{j}U(ax_{j})$ for $\forall j\in(1,n)$ . We ask the following questions in this context. What is the dollar value of the information system?

How does the dollar value of the IS change with the risk aversion of the DM?

## 3.2. Example

The decision problem described above applies to a broad range of Information Systems (IS). As stated before, we are concerned about ex-post evaluation, and, thus, assume that the IS is not a mere concept, but it exists in reality. We discuss a specific example to illustrate our point.

Consider the credit approval problem for consumer loans faced by the managers of banks, credit unions, and other financial institutions. Traditionally, an IS to support credit decisions provides information on a number of factors such as income, outstanding debts, payment history, buying habits, etc. Recently, many organizations have implemented rule-based systems to support credit decisions. For example, American Express pioneered in this arena by introducing its Authorizer's Assistant in 1987 with 800 rules based on knowledge acquired from its five best authorizers [2]. Generally a prototype is first developed and rigorously tested with a sizable number of prior cases before such systems are actually used for credit approval. We therefore can examine the ex-post value of such an expert system and compare it with the value of the existing IS.

Analyzing this credit approval problem using our framework, we find that the DM has two mutually exclusive decision alternatives — approve or deny the credit request based on an evaluation of credit worthiness. $^{7}$ Compared to the existing IS, the expert system is expected to lead to a different subjective probability for credit worthiness. (Note that the payoff for each alternative — i.e., the net gain or loss due to credit approval or disapproval — is not altered by the expert system.) The question then concerns the value of the expert system compared to the existing IS for a risk averse manager. In addition, it would be interesting to determine how this value changes depending upon the degree of risk aversion.

## 3.3. Characterization of risk aversion

Next consider the utility function of the risk averse DM. We know that the utility function must be concave. The more concave the expected utility function is, the more risk averse the DM [28]. Thus, one can measure risk aversion as the second derivative of the utility function. But this measure is susceptible to the magnitude of the utility function. To overcome this, we can normalize this measure by the first derivative. This is the well known Arrow–Pratt measure of absolute risk aversion [3].

We assume constant risk aversion on the part of the DM. That is, her/his attitude toward risk is independent of the payoff. This assumption is reasonable if the payoffs of the decision alternatives lie within a reasonable range. Then the utility function is a positive affine transformation of $-e^{-cx}$ , where c is the measure of risk aversion [17]:

$$
- U ^ {\prime \prime} (x) / U ^ {\prime} (x) = c.
$$

Note that the greater the value of c, the larger the risk aversion. For our analysis, we choose the following utility function:

$$
U (x) = 1 - \mathrm{e} ^ {- c x}.\tag{1}
$$

This utility function has its range between zero and one, and is strictly increasing in the dollar payoff, x.

## 3.4. Method of payment

As noted before, the value of the IS and its relationship with risk aversion is not the same for different methods of payment. Prior research has examined only one method of payment at a time leading to apparently contradictory results. We consider three common methods of payment:

1. Costless Information: In this case, the DM does not make any explicit payment for the information she/he receives. This case is applicable to organizations where end user departments do not pay the IS department for their services. Instead, the top management allocates resources to the IS area based on the estimated work load and subsidizes the end users. This case is also applicable to decision situations where information is a public good. Due to the nondestructive nature of information, a DM can often obtain information for free from libraries and many private and public agencies.

2. Ex-ante Payment: Here the DM makes a payment for information before making her/his decision. As a result, she/he is left with less resources to invest in the chosen decision alternative or activity. This situation applies to an end user department that makes a payment to the IS department based on a chargeback method that reduces the available budget for the department. This is also the common method of payment for external sources, such as consultants, market research firms and information services organizations, e.g., Dow Jones Information Service.

3. Contingent Payment: The advantage of this method of payment is that the DM can use all of her/his resources in the selected activity and pay for the information after she/he realizes the payoff. If the gain from using information is negative, there is no payment. The maximum value of the payment depends on the additional gain realized from using the information. Although this method of payment is common in legal services, $^{8}$ it may be appropriate for specialized information services as well. For example, in the 1980's, Creative Output, Inc., of Milford, CT developed a proprietary software package called Optimized Production Technology (OPT) and licensed it to customers. The fee charged for employing OPT was a percentage of cost savings it generated [18].

## 4. Costless information

In the case of costless information, the value of the IS can be measured in terms of utility or dollars. We are interested in the dollar measure since it allows us to understand how much the

DM may be willing to spend for a specific IS. In addition, it allows us to compare the value of costless information with costly information. However, we note that the decision problem for the DM is to maximize expected utility. Thus, to measure the value of the IS in terms of dollars, we need a mapping from the utility function to dollars. We use the certainty equivalence (CE) of activities for this purpose.

Consider the case when the DM selects decision alternative or activity a without an IS. $^{9}$ If the DM is indifferent between receiving R dollars for certain and investing in activity a, then R is the certainty equivalent of the uncertain activity faced by the DM. In terms of the utility function, we can express this definition more formally as:

$$
\begin{array}{l} U (R) = p _ {\alpha} U (a x _ {\alpha}), \\ \text { or, } R = U ^ {- 1} \big \{p _ {\alpha} U (a x _ {\alpha}) \big \}. \end{array}
$$

For the utility function given in (1),

$$
R = - 1 / c \ln \left\{\left(1 - p _ {\alpha} \left(1 - e ^ {- c a x _ {\alpha}}\right) \right. \right\}.
$$

Note that each uncertain activity has at most one certainty equivalent if the utility function is strictly increasing in dollars [17]. This is true for the utility function (1).

We measure the dollar value of the IS as the difference in the certainty equivalence (CE) of the investment made with the IS ( $CE_{IS}$ ) and without the IS ( $CE_{\phi}$ ). Thus, the value (V) of the IS is

$$
\begin{array}{r l} V = \mathrm{CE} _ {\mathrm{IS}} - \mathrm{CE} _ {\phi} & = U ^ {- 1} \left\{q _ {\beta} U (a x _ {\beta}) \right\} \\ & - U ^ {- 1} \left\{p _ {\alpha} U (a x _ {\alpha}) \right\}. \end{array}
$$

In terms of the utility function in (1),

$$
\begin{array}{c} V = 1 / c \ln \left[ \left\{1 - p _ {\alpha} (1 - e ^ {- c a x _ {\alpha}}) \right\} \right. \\ \left. / \left\{1 - q _ {\beta} (1 - e ^ {- c a x _ {\beta}}) \right\} \right]. \end{array}\tag{2}
$$

To determine how the value of information changes with risk aversion, we take the first order partial derivative of V in (2) with respect to the measure of risk aversion, c:

$$
\begin{array}{r l} \partial V / \partial c & = 1 / c \left[ \left\{q _ {\beta} a x _ {\beta} \mathrm{e} ^ {- c a x _ {\beta}} / \left(1 - q _ {\beta} (1 - \mathrm{e} ^ {- c a x _ {\beta}})\right) \right\} \right. \\ & \quad - \left\{p _ {\alpha} a x _ {\alpha} \mathrm{e} ^ {- c a x _ {\alpha}} / \left(1 - p _ {\alpha} (1 - \mathrm{e} ^ {- c a x _ {\alpha}})\right) \right\} \Big ] \\ & \quad - (1 / c ^ {2}) \ln \left[ \left\{1 - p _ {\alpha} (1 - \mathrm{e} ^ {- c a x _ {\alpha}}) \right\} \right. \\ & \quad / \left\{1 - q _ {\beta} (1 - \mathrm{e} ^ {- c a x _ {\beta}}) \right\} \Big ]. \end{array} \tag {3}
$$

It is clear from (3) that a risk averse person will take into account the subjective probabilities with and without the IS $(q_{\beta} \text{ and } p_{\alpha})$ as well as the payoffs of the selected activity $(x_{\beta} \text{ and } x_{\alpha})$ in judging the value of the IS. An alternative way to interpret (3) is to recognize that there are two possible effects of an IS. First, the IS may assign a different probability of state occurrence $(q_{i} \neq p_{i})$ , but the payoff of the selected activity may not change $(x_{\beta} = x_{\alpha})$ . Second, both the subjective probability of state occurrence and the selected activity (consequently the payoff) change due to the IS. We consider each of these situations separately.

## 4.1. Uncertainty reduction

Let the payoff of the selected activity be the same before and after receiving information such that $x_{\alpha}=x_{\beta}=k$ (say) in Eq. (3). Since the payoff of the activity selected before and after receiving information is the same, $q_{\beta}>p_{\alpha}$ or $q_{\beta}x_{\beta}>p_{\alpha}x_{\alpha}$ . That is, the expected payoff is higher with the IS. This may be interpreted as a case where the effect of the IS is to reduce the uncertainty of a positive payoff. $^{11}$ This corresponds to a reduction in initial uncertainty, and has been studied widely for different situations [11,14]. Behavioral research on information value has also considered similar attributes, such as reliability and verifiability [16,24,25,29].

In this case, the activity selected after receiving the information is not qualitatively different from the one selected without the IS. Here the IS can be interpreted as a transaction processing system where the nature of the activity performed is unaffected by the IS, but the subjective probability of the selected activity is improved due to, for example, an increase in information accuracy. This analysis also applies to a special case where all activities have the same payoff but are not equally likely to succeed. We wish to see how a more risk averse DM views the value of information in this situation. To make our analysis tractable, we consider three levels of payoffs: (i) very low, (ii) very high, and (iii) moderate.

Case (i): Very Low Payoff

When $ak$ is very small, $\mathbf{e}^{-cak}\to 1$ and, hence,

$$
\lim _ {e ^ {- c a x} \rightarrow 1} \partial V / \partial c = a k / c (q _ {\beta} - p _ {\alpha}) > 0 \text {   as   } q _ {\beta} - p _ {\alpha} > 0.
$$

When stakes are very low, the more risk averse person would find the same information to be more valuable. In other words, a highly risk averse person values the same reduction in uncertainty more than a moderately risk averse person.

Case (ii): Very High Payoff

Since $ak$ is very large, $\mathrm{e}^{-cak}\to 0$ , and

$$
\begin{array}{r l}\lim _ {e ^ {- c a k} \rightarrow 0} \partial V / \partial c&= - (1 / c ^ {2}) \ln ((1 - p _ {\alpha}) / (1 - q _ {\beta}))\\&<   0 \text {   as   } 1 - p _ {\alpha} > 1 - q _ {\beta}.\end{array}
$$

Thus, when the stakes are high, the more risk averse person would find the same information less valuable. High stakes cause high anxiety, probably more so for more risk averse managers. Thus, for a low risk averse manager, the reduction of uncertainty of high payoff activities is quite good news. For highly risk averse persons, the news is not as good. For them, the same effect can be achieved if the uncertainty is reduced further.

Case (iii): Moderate Payoff

When ak is neither very high nor very low, $0 < e^{-cak} < 1$ . Consider a specific case: c = 1, a = 1, k = 0.1. That is, the DM has one dollar to invest with a rate of return of 10% and her/his risk parameter has a value of unity. Note that

![](/api/attachments/AV23PYZT/fulltext/images/f9cb57e7204fd3c63f23395534c8340b2438b25f5975bce1d87a4c142fbc5a82.jpg)  
Value of information increases with risk aversion in the shaded region. The area of the shaded region changes with c and k.
Fig. 1. Risk aversion and uncertainty reduction.

If $p_{\alpha} = 0.1$ and $q_{\beta} = 0.5$ , $\partial V / \partial c$ is negative;  
If $p_{\alpha} = 0.6$ and $q_{\beta} = 1.0$ , $\partial V / \partial c$ is positive.

Thus, $\partial V/\partial c$ can be both positive and negative. In other words, a more risk averse individual will have more value for information under some conditions and less value for information under some other conditions. After analyzing the behavior of $\partial V/\partial c$ for different values of $p_{\alpha}$ and $q_{\beta}$ and cak, we find the following result (see Fig. 1). When we move from high uncertainty to moderate uncertainty (e.g., subjective probability increasing from 0.1 to 0.5), the more risk averse person has less value for that information. However, when we move from moderate uncertainty to near perfect information, the more risk averse individual has more value for that information. In other words, a more risk averse person values near perfect information more than imperfect information.

In summary, there is no uniform relationship between the value of costless information and risk aversion when the effect of the information is to reduce uncertainty, but not to change the payoff of the activity selected.

Finally, if the uncertainty about the payoff is sufficiently reduced then the DM may choose an activity with lower payoff $(x_{\alpha} > x_{\beta})$ with information. However, the effect of risk aversion is not clear cut in this case, and must be examined using the original relation (3).

## 4.2. Higher payoff possibility

Now let us consider the case where the subjective probability of the selected activity before and after receiving information is the same $p_{\alpha}=q_{\beta}$ , but the corresponding payoffs are different. Unlike the previous case, the activity selected after receiving the signal is qualitatively different from the one selected without the signal. The IS in this case can be interpreted as a decision support system. $^{12}$ As Keen and Scott Morton [15] suggest, a major objective of DSS is to improve the effectiveness of decision making which may lead to higher payoffs.

Assuming a positive value of the information, it follows that state $\beta$ has a higher payoff than state $\alpha$ , $x_{\beta} > x_{\alpha}$ . Initially, the DM feels that state a is more likely to occur than state $\beta$ ( $p_{\beta} < p_{\alpha}$ ), and selects $\alpha$ . After receiving the information, she/he comes to think that state $\beta$ is as probable as state $\alpha$ and, thus, invests in state $\beta$ . We wish to see how a more risk averse DM views the value of information in this situation. We consider two cases.

Case (i): Low Probability of State Occurrence
When $q_{\beta}, p_{\alpha} \rightarrow 0$

$$
\lim _ {p _ {\alpha}, q _ {\beta} \rightarrow 0} \partial V / \partial c = 0.
$$

When $\alpha$ and $\beta$ are very unlikely to happen, risk aversion does not come into the picture. In other words, a more risk averse manager does not find additional value in any information that leads to the choice of an activity with higher payoff but that seems to have the same low subjective probability of success as the activity selected without the information. As expected, the low subjective probability of success dominates her/his evaluation of the information.

Case (ii): Intermediate Probability of State Occurrence

In this case, $0 < p_{\alpha} = q_{\beta} < 1$ . $\partial V / \partial c$ is negative in this case. To see that $\partial V / \partial c$ is negative, note that $\partial^2 V / \partial c\partial x_\beta$ is negative. Since,

$$
\begin{array}{r l} \partial V / \partial x _ {\beta} & = - a q _ {\beta} \mathrm{e} ^ {- c a x _ {\beta}} \\ & \quad / \left[ 1 - q _ {\beta} (1 - \mathrm{e} ^ {- c a x _ {\beta}}) \right] 0, \partial / \partial c \left[ \partial V / \partial x _ {\beta} \right] \\ & = - a ^ {2} q _ {\beta} x _ {\beta} \mathrm{e} ^ {- c a x _ {\beta}} \left[ \left(1 - q _ {\beta} (1 - \mathrm{e} ^ {- c a x _ {\beta}})\right) \right. \\ & \quad \left. - q _ {\beta} \mathrm{e} ^ {- c a x _ {\beta}} \right] \div \left[ 1 - q _ {\beta} (1 - \mathrm{e} ^ {- c a x _ {\beta}}) \right] ^ {2}, \end{array}
$$

or

$$
\begin{array}{l} \partial / \partial c \left[ \partial V / \partial x _ {\beta} \right] <   0 \text {if} \\ \left[ \left(1 - q _ {\beta} (1 - e ^ {- c a x _ {\beta}})\right) - q _ {\beta} e ^ {- c a x _ {\beta}} \right] > 0, \end{array}
$$

or

$$
\partial / \partial c \left[ \partial V / \partial x _ {\beta} \right] <   0 \text {   if   } 1 - q _ {\beta} > 0.
$$

Thus, $\partial^{2}V/\partial x_{\beta}\partial c$ is negative, or $\partial/\partial x_{\beta}(\partial V/\partial c)$ is negative. So as $x_{\beta}$ increases, $\partial V/\partial c$ decreases. Note that the minimum value of $x_{\beta}$ is $x_{\alpha}$ and when $x_{\beta}=x_{\alpha}$ , $\partial V/\partial c$ is zero. In other words, the maximum value of $\partial V/\partial c$ is zero. Therefore,

$$
\partial V / \partial c <   0 \forall x _ {\beta} > x _ {\alpha}.
$$

The information that changes the activity selected without altering the subjective probability of success $(p_{\alpha}=q_{\beta})$ , is always less valuable to a more risk averse individual. This result underscores the importance of the subjective probability of the selected activity in determining the value of information for a risk averse manager. A more risk averse manager is not swayed by the increased expected payoff of the new activity. As risk aversion increases, the DM is more keen on reducing the uncertainty of the payoff and less concerned about any information that does not help lessen her/his misgivings about the payoff situation.

In summary, the value of costless information does not monotonically vary with risk aversion. The relationship between the value of information and risk aversion depends on the subjective probabilities of state occurrence with and without IS and the payoff structure. When the payoff of the selected activity is the same with and without information, the value of information increases with risk aversion for small payoffs and decreases for large payoffs. For intermediate levels of payoff, the value of information may increase or decrease with risk aversion. However, when the selected activity after receiving information has the same subjective probability as the one chosen without the IS, the value of information reduces with risk aversion.

## 5. Demand for costly information

As discussed in Section 3, we consider two methods of payment for costly information. In the first method, the payment is made before the DM makes her/his investment in the chosen activity. The payment is made only after the gain is realized in the second method. Although the value of information is different in these two situations, the impact of risk aversion on information value is similar. We examine these two methods in this section.

## 5.1. Ex-ante payment

In this situation, the DM has to spend a portion of her/his initial endowment for the IS before she/he makes the investment in the chosen activity b. We wish to know the maximum amount $(r_{e})$ the DM will be willing to pay for information in this case. Clearly, the amount she/he will be willing to pay will make her/him indifferent between receiving and not receiving the information. Thus,

$$
p _ {\alpha} \left(1 - \mathrm{e} ^ {- c a x _ {\alpha}}\right) = q _ {\beta} \left(1 - \mathrm{e} ^ {- c (a - r _ {e}) x _ {\beta}}\right),
$$

where the DM selects activity $\alpha$ without the IS and activity $\beta$ with the IS. We can express the value of information as

$$
r _ {e} = a + \frac {1}{c x _ {\beta}} \ln \left(1 - \frac {p _ {\alpha}}{q _ {\beta}} (1 - e ^ {- c a x _ {\alpha}})\right).\tag{4}
$$

Since we are interested in deriving the relationship between risk aversion (c) and value of information ( $r_{e}$ ), we differentiate (4) with respect to c.

$$
\frac {\partial r _ {e}}{\partial c} = \frac {1}{c ^ {2} x _ {\beta}} \ln \left(1 - \frac {p _ {\alpha}}{q _ {\beta}} (1 - e ^ {1 - c a x _ {\alpha}})\right)
$$

$$
\begin{array}{l} - \left(\frac {1}{c x _ {\beta}} \frac {p _ {\alpha}}{q _ {\beta}} a x _ {\alpha} \mathrm{e} ^ {- c a x _ {\alpha}}\right) \\ / \left(1 - \frac {p _ {\alpha}}{q _ {\beta}} (1 - \mathrm{e} ^ {- c a x _ {\alpha}})\right). \end{array}\tag{5}
$$

Note that if $p_{\alpha}/q_{\beta}=0$ or $p_{\alpha}/q_{\beta}=1$ , $\partial r_{e}/\partial c=0$ . To determine the sign of $\partial r_{e}/\partial c$ for other values of $p_{\alpha}/q_{\beta}$ , we note that

$$
\begin{array}{r l} \frac {\partial r _ {e}}{\partial c} > 0 & \text { if } - \frac {1}{c ^ {2} x _ {\beta}} \ln t - \left(\frac {1}{c x _ {\beta}} \frac {p _ {\alpha}}{q _ {\beta}} a x _ {\alpha} \mathrm{e} ^ {- c a x _ {\alpha}}\right) \\ & / t > 0, \end{array}
$$

where

$$
t = \left(1 - \frac {p _ {\alpha}}{q _ {\beta}} (1 - \mathrm{e} ^ {- c a x _ {\alpha}})\right).
$$

Alternatively,

$$
\frac {\partial r _ {e}}{\partial c} > 0 \text {   if   } - t \ln t - \frac {p _ {\alpha}}{q _ {\beta}} c a x _ {\alpha} e ^ {- c a x _ {\alpha}} > 0.
$$

Denote $T = -t \ln t$ and $S = \frac{p_{\alpha}}{q_{\beta}} cax_{\alpha} e^{cax_{\alpha}}$ . Note that $T$ is concave in $p_{\alpha}/q_{\beta}$ while $S$ is linear in $p_{\alpha}/q_{\beta}$ (see Fig. 2). These two curves intersect at $p_{\alpha}/q_{\beta} = 0$ and $p_{\alpha}/q_{\beta} = 1$ . Thus,

(1) For $p_{\alpha}\langle q_{\beta}, \partial r_{e}/\partial c > 0$ . In this range the demand for information increases with risk aversion. If the subjective probability of success is higher for the activity selected after receiving the information, a more risk averse manager will be willing to make a higher ex-ante payment for that information.

(2) For $p_{\alpha} = q_{\beta}$ , $\partial r_e / \partial c = 0$ . This result holds whenever $p_{\alpha} = q_{\beta}$ and is independent of the actual value of $p_{\alpha}$ or $q_{\beta}$ . In other words, if information does not increase the subjective probability of success of the activity selected, a more risk averse manager would not consider such information to be any more or less valuable than would a less risk averse manager. The subjective probability of success must change for a more risk averse manager to attribute higher value to the information for which payment is made ex-ante.

![](/api/attachments/AV23PYZT/fulltext/images/2c057306cac8dafda168e2ed5dfaa5f86107834dc4ce536d2d2c4d6fdba2a255.jpg)  
Value of information increases with risk aversion if $p_{\alpha} < q_{\beta}$ .  
Fig. 2. Value of information for ex-ante method of payment.

(3) For $p_{\alpha} > q_{\beta}$ , $\partial r_{e}/\partial c < 0$ . In this range the demand for information decreases with risk aversion. Assuming $r_{e} > 0$ , $x_{\alpha} < x_{\beta}$ . Thus, a more risk averse manager will value the information less if it leads to the selection of an activity with lower subjective probability of success even if it has a higher payoff.

In summary, a more risk averse manager cares about the subjective probability of success of the activity selected with information. If this probability improves due to the information received, a highly risk averse manager values that information more than a moderately risk averse manager. In other words, the highly risk averse manager wants to be as sure as possible about a positive payoff.

## 5.2. Contingent payment

The primary difference between the ex-ante method of payment and contingent payment is that with contingent payment, the DM can use the full initial endowment in the chosen activity, while with the ex-ante method she/he cannot. Although not widely practiced, the contingent payment option is an attractive method for marketing information services. A variation of this method occurs when the customer is given a full refund if not satisfied after a fixed period. Periodicals and external database services often follow this pricing strategy for an introductory period to induce new customers to use their services. As source data automation technologies (e.g., optical scanners) become widespread, the explosion of data may necessitate the use of this method of pricing for more information providers.

Once again, we note that the DM will pay the maximum amount $(r_{c})$ that will make her/him indifferent between receiving and not receiving the information. If she/he chooses activity $\alpha$ without information and activity $\beta$ after receiving information, we state:

$$
p _ {\alpha} (1 - \mathrm{e} ^ {- c a x _ {\alpha}}) = q _ {\beta} (1 - \mathrm{e} ^ {- c (a x _ {\beta} - r _ {c})}).
$$

Thus, the maximum amount the DM will pay for the information is

$$
r _ {c} = a x _ {\beta} + \frac {1}{c} \ln \left(1 - \frac {p _ {\alpha}}{q _ {\beta}} (1 - e ^ {- c a x _ {\alpha}})\right).\tag{6}
$$

We assume that $r_{c}$ is positive. Once again, we differentiate $r_{c}$ with respect to c to obtain

$$
\begin{array}{r l} \frac {\partial r _ {c}}{\partial c} = & - \frac {1}{c ^ {2}} \ln \left(1 - \frac {p _ {\alpha}}{q _ {\beta}} (1 - e ^ {- c a x _ {\alpha}})\right) \\ & - \left(\frac {1}{c} \frac {p _ {\alpha}}{q _ {\beta}} a x _ {\alpha} e ^ {- c a x _ {\alpha}}\right) \\ & / \left(1 - \frac {p _ {\alpha}}{q _ {\beta}} (1 - e ^ {- c a x _ {\alpha}})\right). \end{array}\tag{7}
$$

Notice the similarity between Eqs. (5) and (7). Indeed,

$$
\frac {\partial r _ {c}}{\partial c} = x _ {\beta} \frac {\partial r _ {e}}{\partial c}.
$$

Since $x_{\beta}>0$ , the sign of $\frac{\partial r_{c}}{\partial c}$ is identical to that of $\frac{\partial r_{e}}{\partial c}$ for different values of $p_{\alpha}/q_{\beta}$ . Thus, the value of information is different for ex-ante and contingent methods of payment, but the impact of risk aversion on information value differs only by a constant multiple.

## 6. Discussion

Our framework is applicable to two broad situations. First, a manager with a one-shot decision may consider acquiring additional information from existing internal or external sources. Second, a manger may con supplanting an existing system with a new system. In each case, we can examine whether a more risk averse manager would attribute more or less value to the same information for different modes of payment.

How strong is the tie between our information value framework and the existing typology of information systems? For example, one may ask how does our analysis apply to transaction processing systems (TPS), decision support systems (DSS), or expert systems (ES)? $^{13}$ Before answering this question, we should note two basic characteristics of the system typology. First, the development approach differs across system types. While TPS deal essentially with large amounts of data, DSS and ES are concerned with model base and knowledge base development, respectively. Second, while some systems are used for structured decision making (e.g., TPS), others may be used for semistructured and unstructured decisions also.

We are concerned with the value of information from the end user point of view. Thus our framework does not relate to the development approach, but it bears upon the system usage. In particular, our model applies to structured decisions and some semistructured decisions, but not to unstructured decisions. Unstructured decisions are excluded because we assume that the relevant states of nature and payoff corresponding to each decision alternative are known and independent of the IS used. Thus we expect our model to be applicable to all TPS and to some DSS and ES. This is not a major limitation since the bulk of the information technology investments in most firms are in transaction processing systems $[8]$ .

The key idea in our approach is to recognize that subjective probabilities of state occurrences often change with information and may lead to a change in the activity selected. We are interested in learning how the value of information changes with risk aversion. To answer this question, we must distinguish between costless and costly information. Both the value of information and its relationship with risk aversion change with the mode of payment. Next, we should note that a fundamental consideration for a risk averse manager is the subjective probability of the chosen activity. Let p be the subjective probability of the activity chosen using the existing system and q be the same with a new system. Then the following three cases emerge from our analysis.

Case 1: p < q. The knowledge based credit approval system discussed in Section 3.2 can be used as an example of this case if we assume that the subjective probability (q) of a loan approved by the new system being credit worthy is higher than that (p) of a loan authorized by the manual system. In addition, the DM may receive the system from the corporate management for free or may acquire it from her/his budget for a specific price.

A risk averse manager is expected to prefer this situation when the subjective probability of success increases due to the use of an IS. For costly information, the value of information increases with risk aversion as the uncertainty of the payoff reduces. For costless information, the same result holds if the subjective probability increases from moderate to near certainty when the magnitude of the payoff does not change. The reaction of risk averse managers to costless information is not so unambiguous for other conditions. For example, when the stakes are high, a more risk averse manager would attribute less value to information that does not lead to a higher payoff.

Case 2: p = q. An example of this case concerns a situation where the management of a retail chain is considering the amount of a product to order from the manufacturer. For the sake of simplicity, assume that the manufacturer will accept only two possible order quantities: low (100) and high (200). Note that the payoff from each of these amounts is dependent upon the profit margin and the corresponding order quantity. $^{14}$ Additionally, the payoff structure is independent of the information system used. Thus, the management is faced with two mutually exclusive decision alternatives and wants to know the probability that the demand will exceed the order quantity. Assume that this probability is judged as 0.7, and 0.3 for the low and high order quantity based on available data. Thus, the decision would be to order 100 items only (p = 0.7).

Alternatively, management may consider acquiring additional information before making the decision. The nature of information obtained may depend on the complexity of the product market. For example, if the decision concerns a spare part for an automobile in the US market, the potential market size can be determined based on publicly available automobile sales data (costless information). On the other hand, the decision to order fashion merchandise may require the services of a market research company (costly information). Assume that the revised subjective probability of demand exceeding the high level is 0.7 such that the high order quantity is chosen. Note in this example p = q = 0.7.

In this case the payoff of the activity selected after using the information is higher, but the subjective probability of success is the same. A more risk averse manager will not consider such costly information more valuable than a less risk averse manager. The same result holds for costless information if the subjective probability of success is low. For moderate levels of this probability, however, the value declines with risk aversion.

Case 3: p > q. For the sake of brevity, we can modify the previous example to illustrate this case. Let the revised subjective probability of demand exceeding the high level be 0.55 such that the high order quantity is chosen again. Note that in this example $p = 0.7 > q = 0.55$ .

For costly information, the value of information declines as risk aversion increases if the subjective probability of the selected activity is less with the IS. For costless information, the result is not clear cut and would require the consideration of the values of the payoff of the activities selected as well as the probabilities with and without IS.

These results apply to existing sources of information only. These sources include both internal information services and external sources such as market research or management consulting firms and public and private data bases. We assume that the manager has some experience with the source and knows how the use of the information provided changes her/his subjective probability distribution. Thus, the information value we determine is of interest to both the decision maker and the information provider. If a more risk averse DM finds an information source less valuable, there is a potential that she/he may look for other sources. For the information provider it is instructive to know what type of information is more valuable to risk averse managers.

Our research does not address the issue of new systems projects where the effect of the IS on the DM's subjective probability distribution may be hard to determine. However, if a prototype proceeds the actual development, it will be easier to use our analysis. Similarly, our analysis is applicable to system enhancement projects where the effect of IS is easier to understand.

## 7. Conclusion

Most managers are risk averse. Yet, most research on the value of information assumes the DM to be risk neutral. In addition, the prior work on risk aversion and value of information appears to be in conflict. We develop a general model of the value of information for a risk averse DM. Our results show that while prior works on this topic contain no flaws, they depict a limited view of the relationship between risk aversion and the value of information $^{15}$ .

We show that the value of information to a risk averse decision maker is different for costly and costless information. In the case of costly information, the subjective probabilities of state occurrences with and without IS should be taken into account in determining the relationship between risk aversion and the value of information. For costless information, the payoff structure of the activities is also a relevant factor in determining this relationship.

Our research examined the value of information for a single risk averse DM. A natural extension would be to examine this issue from the perspective of a team of risk averse DMs. The analysis for the team, however, is likely to be more difficult. For example, one has to first define the risk aversion of a group. Another interesting case occurs when two or more DMs can share an IS. The value of the IS is not adequate for any one manager to merit buying the information, but the total benefit to all managers exceeds the cost of the IS. Then each manager would want to ensure that acquiring the information indeed improves her/his expected utility. However, she/he would reveal her/his true preference for the IS only if her/his expected utility increases by doing so.

We note some restrictions in our modeling framework. We consider mutually exclusive activities, and thus do not allow the DM to invest in more than one activity. If the activities are not mutually exclusive, a manager may pursue more than one decision alternative. We also do not include the possibility that the IS may change the DM's knowledge of the activity payoffs. Similarly, we do not allow an activity to be a limited success. One can follow Gould [10] in allowing a project to be a partial success. The information systems literature has not considered the role of risk aversion in assessing the value of information. We hope that our work will motivate others to study this important concept and, thus, fill in this current void in information systems research.

## Acknowledgements

This research was supported in part by the National Science Foundation under Grant No. IRI-9012740. We thank Anitesh Barua and Randolph B. Cooper for their helpful comments.

## References

[1] N. Ahituv, A Systematic Approach toward Assessing the Value of an Information System, MIS Quarterly 4, No. 4 (1980) 61–75.

[2] A. Alper, Expert System versus Credit Fraud, Computerworld, April 13 (1987) 25ff.

[3] K. Arrow, The Value of and Demand for Information, in: Essays in the Theory of Risk Bearing (Markham, Chicago, 1971) pp. 268–278.

[4] T. Barron and A.N. Saharia, Optimal Information Structures for the Seller of a Search Good, Information Systems Research 1, No. 2 (1990) 188–204.

[5] A. Barua, C.H. Kriebel and T. Mukhopadhyay, MIS and Information Economics: Augmenting Rich Descriptions with Analytical Rigor in Information Systems Design, Proceedings of the International Conference on Information Systems, Boston, 1980, pp. 327–340.

[6] D.E. Bell, One-Switch Utility Functions and a Measure of Risk, Management Science 34, No. 12 (1988) 1416-1424.

[7] J.S. Dyer and R.K. Sarin, Relative Risk Aversion, Management Science 28, No. 8 (1982) 875–886.

[8] J.C. Emery, Management Information Systems: The Critical Strategic Resource (Oxford University Press, NY, 1987).

[9] X. Freixas and R.E. Kihlstrom, Risk Aversion and Information Demand, in: M. Boyer and R.E. Kihlstrom (eds.), Bayesian Model in Economic Theory (Elesevier, Amsterdam, 1984) pp. 93–104.

[10] J.P. Gould, Risk, Stochastic Preference, and the Value of Information, Journal of Economic Theory 8, No. 1 (1974) 64–84.

[11] R.W. Hilton, The Determinants of Cost Information Value: An Illustrative Analysis, Journal of Accounting Research 17, No. 2 (1979) 411–435.

[12] R.W. Hilton, The Determinants of Information Value: Synthesizing Some General Results, Management Science 27, No. 1 (1981) 57–64.

[13] J. Hirshleifer, The Private and Social Value of Information and the Reward to Inventive Activity, American Economic Review 61 (1971) 561–574.

[14] H. Itami, Adaptive Behavior: Management Control and Information Analysis (American Accounting Association, Sarasota, FL, 1977).

[15] P.G.W. Keen and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley, Reading, MA, 1978).

[16] W.R. King and B.J. Epstein, Assessing the Information System Value: An Experimental Study, Decision Sciences 14, No. 1 (1983) 34–45.

[17] D.M. Kreps, A Course in Microeconomic Theory (Princeton University Press, 1990).

[18] R. Lundrigan, What is this Thing They Call OPT? Production and Inventory Management 27 (2nd Quarter) (1986) 2–12.

[19] J. Moore and A.B. Whinston, A Model of Decision Making with Sequential Information Acquisition (Part 1), Decision Support Systems 2, No. 4 (1986) 285–307.

[20] J. Moore and A.B. Whinston, A Model of Decision Making with Sequential Information Acquisition (Part 2), Decision Support Systems 3, No. 1 (1987) 47–72.

[21] H. Raiffa, Decision Analysis (Addison-Wesley, Reading, MA, 1970).

[22] M. Rothschild and J.E. Stiglitz, Increasing Risk: I. A Definition, Journal of Economic Theory 2, No. 3 (1970) 225–243.

[23] R.K. Sarin and M. Weber, Risk-Value Models, European Journal of Operational Research 70 (1993) 135–149.

[24] H.J. Snavely, Accounting Information Criteria, Accounting Review 42, No. 2 (1967) 223–232.

[25] E.B. Swanson, Management Information Systems: Appreciation and Involvement, Management Science 21, No. 2 (1974) 178–188.

[26] H. Theil, Economics and Information Theory (Rand McNally, Chicago and North-Holland, Amsterdam, 1967).

[27] D.S. Tull and D.I. Hawkins, Marketing Research: Measurement and Method (Macmillan, New York, 1990).

[28] H.R. Varian, Microeconomic Analysis (Norton, NY, 1984).

[29] R.W. Zmud, An Empirical Investigation of the Dimensionality of the Concept of Information, Decision Sciences 9, No. 2 (1978) 187–195.

Raja Nadiminti was a doctoral student at the Graduate School of Industrial Administration, Carnegie Mellon University. His research interest was primarily in the economics of information systems. He died in March 1993 in an accident. The research reported here is based on his first Summer Paper. Those who knew him would recognize that this article only began to demonstrate his potential.

Tridas Mukhopadhyay is an Associate Professor of Industrial Administration at Carnegie Mellon University. He received his Ph.D. in computer and information systems from the University of Michigan in 1987. His research interests include business value of information technology, economic impacts of electronic data interchange, software development productivity, and cost analysis. His primary area of interest is in the economics of information technology. His research appears in Information Systems Research, Journal of Manufacturing and Operations Management, MIS Quarterly, Omega, IEEE Transactions on Software Engineering, Journal of Operations Management, Accounting Review, Management Science, Journal of Management Information Systems, Decision Support Systems, Journal of Experimental and Theoretical Artificial Intelligence, Journal of Organizational Computing and other publications. He is an Associate Editor for Information Systems Research and is a member of the Editorial Board of Journal of Management Information Systems and Journal of Organizational Computing.

Charles H. Kriebel is Professor of Industrial Administration at the Graduate School of Industrial Administration, Carnegie Mellon University. He received his Ph.D. in Industrial Management from MIT in 1964 where he was a Ford Foundation Fellow and a faculty member. He was Departmental Editor of Management Science for 12 years and is an Advisory Board Member of ISR. He has published more than 100 articles in leading professional journals, including Behavioral Science, Communications of the ACM, Decision Sciences, Econometrica, Management Science, MIS Quarterly, and Operations Research. His research interests include economics of information systems and technology, MIS, productivity, impacts of technology, manufacturing, and strategy.
