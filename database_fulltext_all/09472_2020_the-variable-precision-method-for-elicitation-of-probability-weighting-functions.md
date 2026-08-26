---
otero_id: 9472
otero_key: "EAEQT2GH"
title: "The variable precision method for elicitation of probability weighting functions"
authors: "Junyi Chai; Eric W.T. Ngai"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113166"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

The variable precision method for elicitation of probability weighting functions

Junyi Chai, Eric W.T. Ngai

Decision Support Systems

![](/api/attachments/EAEQT2GH/fulltext/images/6568704dd27fd03feb9878dc391767152c40c55748203b17df12b230f90ff7da.jpg)

PII: S0167-9236(19)30195-2

DOI: https://doi.org/10.1016/j.dss.2019.113166

Reference: DECSUP 113166

To appear in: Decision Support Systems

Received date: 5 March 2019

Revised date: 2 October 2019

Accepted date: 2 October 2019

Please cite this article as: J. Chai and E.W.T. Ngai, The variable precision method for elicitation of probability weighting functions, Decision Support Systems (2019), https://doi.org/10.1016/j.dss.2019.113166

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# The Variable Precision Method for Elicitation of Probability Weighting Functions

Junyi Chai (The Corresponding Author)

Division of Business and Management, Beijing Normal University-Hong Kong Baptist University United International College, Zhuhai, China.

Email: donchaiam@gmail.com Phone: +852 5138 0601.

ORCID: 0000-0003-1560-845X

Eric W. T. Ngai

Department of Management and Marketing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, China.

Email: eric.ngai@polyu.edu.hk Phone: +852 2766 7296.

ORCID: 0000-0002-7278-7434

## Abstract

This study introduces a nonparametric method to elicit decision weights under prospect theory. These weights carry the attitudes and subjective beliefs of individuals toward risks and uncertainties. Our variable precision method adopts a dynamic mechanism that can elicit the measuring points of individual probability weighting flexibly. These points are used to exhibit violations of expected utility theory, which measures individual risk attitudes and captures subjective beliefs on probabilities. Our method is flexible, tractable, and cognitively less demanding compared with other nonparametric elicitations in the literature. Experimental studies are conducted on a sample of Hong Kong (China) residents to verify our method. Our experimental results yield a prevailing inverse-S shape. We conduct the analyses and uncover their implications by comparing them with the results of residents of Beijing, Shanghai, Paris, and Amsterdam.

Keywords: Prospect theory; probability weighting; tradeoff method; nonparametric elicitation; behavioral decision making

## 1. Introduction

A long tradition considers decision theory (DT) as descriptive and normative [1, 2, 3]. Descriptive theories

consider what it is, whereas normative theories consider what ought to be. Descriptive theories attempt to

give an accurate description of reality, whereas normative theories attempt to tell what reality should be like.

Specifically, descriptive DT is concerned with characterizing and interpreting regularities of decisions that

people are disposed to make. Differently, normative DT seeks to provide an account of choices that people

ought to be disposed to make. The distinction between descriptive and normative theories is in their

interpretation rather than their mathematical model [4]. Beyond this dichotomy, decision analysts advocate

“prescriptive” theories toward solving practical problems in the real world [5]. Prescriptive DT attempts to

provide recommendations for decision-makers that conform to desired normative principles. Thus,

prescriptive DT can also be called engineering of decisions and bridges the gap between descriptive and

normative theories [6]. Problems of supplier selection, such as ranking [7, 8] and sorting tasks [9, 10], are

typical applications of prescriptive DT. Detailed reviews of the literature can be found in [11, 12].

Prospect theory (PT) [13] is a typical descriptive DT that is used to characterize the choices that people make as well as to analyze their individual attitudes and subjective beliefs. The original PT is motivated by des pointed out in Allais’s paradox [14], which cannot be explained by expected utility theory of von Neumann and Morgenstern (vNM) [15]. Deeply rooted in principles of cognitive psychology, PT depicts the patterns that are created when people choose among probabilistic outcomes in which the probabilities are uncertain. Cumulative prospect theory (CPT) [16] amends its 1979 version [13] after rank-dependent utility theory (RDU) is incorporated [17]. Different from PT and CPT as descriptive theories, RDU and vNM are normative theories. CPT separates utilities and probabilities as gains and losses, which contain core characters such as loss aversion, reference dependence, diminished sensitivity, and probability weighting. The development of PT/CPT helped Kahneman win the 2002 Nobel Prize in Economics. For a full treatment of PT, refer to the literature [17, 18, 19].

Although PT is widely believed to be an excellent descriptive theory with behavioral and psychological insights, functional forms of utility and decision weights are characterized by their qualitative properties. Thus, we need proper assessment methods to measure the shape of utility and decision weights exhibited by subjects in laboratory experiments. Our target is to uncover the attitudes and subjective beliefs of people as well as deviations of their rationality (i.e., bounded rationality [20]) when making choices under risks and uncertainties. The assessment methods used to elicit the PT utility and weighting functions fall into two categories. (1) Parametric methods assume a functional form of the utility and weighting functions, which must be subjective and may not reflect the real world. (2) Nonparametric methods make no assumptions on functional forms and rely on a two-stage process. The utility is assessed in the first stage and then applied to elicit the probability weighting function in the second stage. These methods are purely free of parameters and do not rely on a predefined functional form. Thus, they reflect the factual attitudes of experiment subjects under risks and uncertainties.

The family of nonparametric methods has been popular in the last twenty years. The most popular approach in assessing utility is the tradeoff (TO) method developed by Wakker and Deneffe [21], which has been the common preliminary for nonparametric elicitation of decision weights. Once one has obtained a measure of utility from a subject, one can proc to measure probability weightings nonparametrically. In literature, Abdellaoui [22] (Abd00) provided the most direct and simplest method. Bleichrodt and Pinto [23] (BP00) introduced a method through linear interpolation under the assumption of linearity in utility. Abdellaoui, Vossmann, and Weber [24] (AVW05) then incorporated BP00 and Abd00 for decisions under uncertainty. Abdellaoui, Bleichrodt, and Paraschiv [25] contributed a four-step procedure by using utility midpoint for losses. van de Kuilen and Wakker [26] (vKW11) advanced a midweight method for both risk and uncertainty. Although nonparametric methods tend to be less time consuming than parametric methods, this family of methods is generally quite cognitively demanding and could occur error propagation.

We introduce the new variable precision (VP) method in this study for the nonparametric elicitation of probability weightings. This method requires only two utility measuring points for a three-outcome standard sequence. Experimenters can elicit any number of probability weighting measuring points by constructing the same number of preference indifferences with the simplest structure and interpolating a dynamic outcome that is highly controlled by VP parameters. The advantage of our VP method is considerable. However, the range of standard sequences is difficult to control (vKW11, p. 594) when using the TO method in utility elicitation. Similar to Abd00, $p = \mathbf { w } ^ { - 1 } ( j / n )$ that is derived from a standard sequence $( x _ { 1 } , . . . , x _ { \mathrm { j } } , . . . , x _ { \mathrm { n } } )$ , and experimenters would never realize whether n will be fine. Experimenters generally offer n arbitrarily. Similar to BP00, the value of the interpolated Zs (i.e., upper bound) is restricted only by $Z \mathbf { s } < x _ { \mathrm { { n } } } ;$ thus, experimenters would never be able to determine the range $( x _ { 0 } , \ x _ { \mathrm { n } } )$ . The VP method possesses the advantage of the midweight method by vKW11, that is, experimenters only require two new outcomes in utility elicitation. and flexibility, enhance experiment tractability, and minimize the cognitive demand. This study provides two main contributions. First, we propose the VP method, which can be used as an alternative to other nonparametric methods and has numerous advantages. Second, we use this method in lab experiments on a sample of residents of Hong Kong (China), which has never been done before. This study is valuable as that researchers can apply our VP method to design experiments for analyses in various samples of people and our analyses of experimental results provide meaningful evidence for policymakers and business consultants. We analyze the attitudes and behaviors of Hong Kong residents and conduct detailed comparisons with residents of Beijing and Shanghai of China. We compare the revealed patterns of risk attitudes and individual preferences among different regions of people. This study could benefit future research in the field of decisions, economics, and psychology. This paper is structured as follows. Section 2 briefly revisits the theoretical background, and Section 3 reviews the PT measurements, including parameterization and elicitations of utility and probability weightings. Section 4 introduces the VP method, and Section 5 presents our experimental studies on college students from Hong Kong (China). Section 6 presents the experimental results and conducts nonparametric and parametric analyses, and Section 7 provides comparisons and evaluations of the VP method. Finally,

Section 8 concludes the paper, and supplementary material and data analyses are provided in the Appendices.

## 2. Background

We briefly review the details of PT and rank-dependent utility (RDU) as our background. RDU was developed by Schmeidler [27] through an axiomatic method on the subjective expected utility (SEU) of Savage [28, 29]. When the SEU’s sure-thing principle is weakened to apply only “comonotonic” acts, SEU can be generalized to allow nonadditive probabilities. RDU can degenerate as SEU when the probability is additive from another perspective. Cumulative PT perfectly carries the descriptive ability of PT and normative ability of RDU, which extends PT to rank-dependent and many-outcome lotteries. Choquet integrals [30] have been utilized to compute the weighted values of outcomes and separate gains and losses in both utility and probability weighting. CPT thus far is reference-dependent, sign dependent, and rank dependent.

Outcome x are monetary, where outcome set $\mathbb { R } ^ { + }$ represents gains, whereas $\mathbb { R } ^ { - }$ represents losses. The value V(.) of a simple prospect that pays \$x with probability p (and nothing otherwise) is given as $\quad V ( x , p ) =$ w(p) u(x). The subjective value of outcome x is measured by a utility function u(.). The effect of probability $p$ on the attractiveness of the prospect is measured by the probability weighting function w(.). Utility function from a reference point with $u ( 0 ) = 0$ so that u(.) is concave for gains and convex for losses. The w(.) accommodates diminishing sensitivity to changes in probabilities with two reference points: impossibility and certainty. CPT is sign-dependent; both $u ( . )$ and $w ( . )$ are segregated into gain and loss portions. CPT is rank dependent: w(.) is evaluated by cumulative probabilities that depend on the rank of outcomes.

Suppose a prospect $( x _ { 1 } , p _ { 1 } ; x _ { 2 } , p _ { 2 } ; x _ { 3 } , p _ { 3 } )$ yields $x _ { i }$ with probability $p _ { i }$ for $i = 1 , 2 , 3$ . The probabilities are nonnegative and add up to one. For either $0 \leq x _ { 1 } \leq x _ { 2 } \leq x _ { 3 }$ or $0 \geq x _ { 1 } \geq x _ { 2 } \geq x _ { 3 }$ , this prospect can be evaluated by $w ( p _ { 3 } ) u ( x _ { 3 } ) + [ w ( p _ { 3 } + p _ { 2 } ) - w ( p _ { 3 } ) ] u ( x _ { 2 } ) + [ 1 - w ( p _ { 3 } + p _ { 2 } ) ] u ( x _ { 1 } )$ , where a strictly increasing and continuous utility function u: ℝ ⟶ ℝ and a strictly increasing and continuous weighting function w that maps [0,1] to [0,1] with $w ( 0 ) = 0$ and w(1) = 1 exist. For the complete sign-ranked outcomes $x _ { 1 } \leq \cdots \leq x _ { k } \leq 0 \leq x _ { k + 1 } \leq \cdots \leq x _ { n } .$ , the prospect $( x _ { 1 } , p _ { 1 } ; \ldots ; x _ { n } , p _ { n } )$ can be evaluated by the following:

$$
\sum_ {i = 1} ^ {k} \pi_ {i} ^ {-} u (x _ {i}) + \sum_ {j = k + 1} ^ {n} \pi_ {j} ^ {+} u (x _ {j})\tag{2.1}
$$

where the decision weights for losses are $\pi _ { i } ^ { - } = w ^ { - } ( p _ { 1 } + \cdots + p _ { i } ) - w ^ { - } ( p _ { 1 } + \cdots + p _ { i - 1 } )$ for $i \geq 2$ and $\pi _ { 1 } ^ { - } = w ^ { - } ( p _ { 1 } )$ , and the decision weights for gains are $\pi _ { j } ^ { + } = w ^ { + } \big ( p _ { j } + \dots + p _ { n } \big ) - w ^ { + } \big ( p _ { j + 1 } + \dots + p _ { n } \big )$ for $j \le n - 1$ and $\pi _ { n } ^ { - } = w ^ { - } ( p _ { n } )$ . These probability weightings do not necessarily add up to one.

## 3. Parameterization and Elicitation Methods

Parameterization establishes functional forms for fitting the qualitative (rather than quantitative) properties of utility $u ( . )$ and probability weighting w(.). This process concerns how to depict the shape of u(.) and $w ( . )$ as well as how to elicit their parameters exhibited by individuals. We describe related works here as the preliminary of our VP method.

## 3.1 PT Measurements: Parameterization

The shape of $u ( . )$ is assumed concave for gains, convex for losses, and steeper for losses than for gains. Tversky and Kahneman [16] (TK92) relies on the following power function:

$$
u (x) = \left\{ \begin{array}{c l} x ^ {\alpha} & x \geq 0 \\ - \lambda (- x) ^ {\beta} & x <   0 \end{array} \right.\tag{3.1}
$$

where the parameters were estimated as $\alpha = 0 . 8 8 , \beta = 0 . 8 8$ , and ?? = 2.25 based on their data. To date, no canonical definition or measure of loss aversion exists.

Existing literature generally shows that the $w ( . )$ is an inverse-S shape that tends to overweight low probabilities and underweight moderate to large probabilities. The sum of complementary probabilities tends to be less than one. In the parameterization of $w ( . )$ , Goldstein and Einhorn [31] (GE87) assumed that the relations between $w ( . )$ and the probabilities $p$ are linear in a log-odds metric known as PW(A). Prelec [32] proposed a functional form that accommodated three principles: (1) overweighting of low probabilities and underweighting of moderate to high probabilities, (2) subproportionality, and (3) subadditivity. These principles can be summarized as an axiom called “compound invariance”. He then suggested the two-parameter specification PW(B) that can be further degenerated as the one-parameter form PW(C). As another representative, TK92 proposed the one-parameter specification PW(D). These parametric specifications generally impose an inverse-S shaped w(.).

Although the prevailing form of $w ( . )$ is an inverse-S shape, existing literature also reveals some mixed evidence. Hey and Orme [33] and Harless and Camerer [34] proposed the usage of the power function PW(E) that entirely excludes inverse-S shapes. The convex-shaped w(.) was obtained in empirical studies by vKW11’s experimental studies based on the population of Amsterdam, which was also supported by the experiments of Qiu and Steiger [35]. The S-shaped $w ( . )$ was also supported by Goeree, Holt, and Palfrey [36]. Stott [37] determined the almost linear $w ( . )$ that accommodated the functional form of PW(C) with the parameter 0.94. Our experimental studies employ all of the aforementioned specifications for parametric analyses.

Interaction of u(.) and w(.): Typically, the concavity of u(.) contributes to risk aversion for pure gain; convexity of $u ( . )$ contributes to risk-seeking for pure loss. Both conditions are reinforced by the as put forward by Fox and Poldrack [38] (FP14, hereafter). For mixed prospects, loss aversion contributes to risk aversion. The outcome valuation by $u ( . )$ and probability weighting by $w ( . )$ appear to contribute independently to risk preference.

## 3.2 Nonparametric Elicitation of Utility: The Tradeoff Method

FP14 stated that the elicitation methods of $u ( . )$ and $w ( . )$ can be classified as (1) statistical methods [39], (2) parametric methods [40, 41, 42], and (3) nonparametric methods. The advantage of nonparametric methods is that they exhibit the actual phenomena of an individual’s attitude based purely on data; they have no assumption on the functional forms. Therefore, nonparametric methods are more transparent and suitable for prescriptive applications than the two other categories. We verify these advantages in the experimental

studies presented in Section 6.

Nonparametric elicitations include a two-stage process. The first stage is to elicit a standard sequence as inputs of the second stage. We briefly describe this process as follows. Subjects are required to make judgments between two two-outcome prospects, such as $( x , p ; y )$ , which offers \$x with probability p (\$y otherwise) to fulfill the indifference $( x _ { 0 } , p ; R ) \sim ( x _ { 1 } , p ; r )$ . The values of $r , R , x _ { 0 } ,$ , and $p$ are all given. Subjects provide the outcome $x _ { 1 }$ such that the indifference relation is satisfied. By iterating the constructions of indifferences as $( x _ { 1 } , p ; R ) \sim ( x _ { 2 } , p ; r )$ to obtain $x _ { 2 } ,$ one can obtain an increasing sequence of outcomes $( x _ { 0 } ,$ $x _ { 1 } , . . . , x _ { \mathrm { n } } )$ $x _ { \mathrm { j } }$ $j = 0 , . . . , n$ is spaced equally in terms of the subjects’ subjective valuation of outcomes, which is formally expressed as $u ( x _ { \mathrm { j } } ) – u ( x _ { \mathrm { j - 1 } } ) =$ $u ( x _ { \mathrm { j + 1 } } ) – u ( x _ { \mathrm { j } } ) { \mathrm { ~ f o r ~ } } j = 1 , . . . , n – 1$ . The outcome $x _ { \mathrm { j } }$ is a midpoint outcome in terms of utility in the subsequence $( x _ { \mathrm { j } - 1 }$ $x _ { \mathrm { j } } , x _ { \mathrm { j + 1 } } )$ . A similar process can be followed to obtain a (decreasing) standard sequence $( x _ { 0 } , x _ { 1 } , . . . , x _ { \mathrm { n } } )$ for losses, where $0 { \geq } r > R > x _ { 0 } > x _ { 1 } > \ldots > x _ { \mathrm { n } }$

## 3.3 Nonparametric Elicitation of Probability Weighting: An Overview

The elicitation of probability weighting captures the true pattern of $w ( . )$ from measured data to exhibit an individual’s attitude towards risk or ambiguity. The most direct and simplest method is presented in [22]. Given an increasing standard sequence $( x _ { 0 } , x _ { 1 } , . . . , x _ { \mathrm { { n } } } )$ , the lowest and highest outcome $x _ { 0 }$ and $x _ { \mathrm { n } }$ satisfy the indifferences $( x _ { \mathrm { n } } , p _ { \mathrm { i } } ; x _ { 0 } ) \sim x _ { \mathrm { i } } , { \mathrm { f o r } } i = 1 , . . . , n - 1$ . This condition can be linked to a lottery between the best and worst outcomes (with a probability $p _ { \mathrm { i } } )$ , which is assumed the indifference with each internal outcome $x _ { \mathrm { i } }$ (gain/loss for sure), as long as a probability $p _ { \mathrm { i } }$ exists that is assigned to $x _ { \mathrm { i } }$ for $n { - } 1$ internal outcomes. Given that utilities are equally spaced, inverse decision weights can be obtained by $p _ { \mathrm { i } } { = } w ^ { - 1 } ( i / n )$ that correspond to each of the outcomes x<sub>i</sub>.

Unlike $\mathrm { \ A b d { } 0 0 ^ { \circ } s }$ method that fixes a standard sequence, BP00’s method fixes the probability and then interpolates new outcomes, which are denoted as $Z r$ (i.e., lower outcomes) and Zs (i.e., higher outcomes). Interpolated outcomes are not necessarily included in the standard sequence. BP00’s method states that utility functions do not deviate significantly from linearity. By incorporating the methods of Abd00 and

BP00, AVW05’s method is more feasible for decisions under uncertainty. With respect to a standard sequence, this method first normalizes the utility of the largest outcome as one, so $w ( P _ { \mathrm { L } } ) = u ( x _ { \mathrm { j } } )$ (outcome x<sub>j</sub> is of the event $A _ { \mathrm { j } } )$ as presented by Abd00 (i.e., Eq. 3). It subsequently determines u(x<sub>j</sub>) through linear interpolations as presented by BP00. vKW11 advances a midweight method that allocates the probability of a middle outcome among the high-valued and low-valued outcomes, such that the prospect value remains unchanged. This method can be regarded as a state-of-the-art method in the family of nonparametric elicitations of w(.).

## 4. The Variable Precision Elicitation of Decision Weights

## 4.1 The Variable Precision Method

The core idea of our VP method is to interpolate an outcome $x _ { m }$ that can be controlled by a variable degree of precision. For simplicity, we consider the gains for the exposition of the VP method. Our method can be implemented for losses almost as immediately as that for gains. We consider a three-outcome (increasing) standard sequence $( x _ { 0 } , x _ { 1 }$ , and $x _ { 2 } )$ for gains, where the initial $x _ { 0 }$ is given. The new outcomes $x _ { 1 }$ and $x _ { 2 }$ are elicited through two indifferences $( x _ { 1 } , p ; y ) { \sim } ( x _ { 0 } , p ; Y )$ and $( x _ { 2 } , p ; \ y ) { \sim } ( x _ { 1 } , p ; \ Y )$ , where ?? and ?? are two reference outcomes for $0 \leq y < Y < x _ { 0 }$ . An individual is asked to specify $x _ { 1 }$ and $x _ { 2 }$ through the two indifferences, so $x _ { 0 } < x _ { 1 } < x _ { 2 }$ for gains. The first indifference yields the following:

$$
w (p) [ u (x _ {1}) - u (x _ {0}) ] = \big (1 - w (p) \big) [ u (Y) - u (y) ].\tag{4.1}
$$

The second indifference yields the following:

$$
w (p) [ u (x _ {2}) - u (x _ {1}) ] = \big (1 - w (p) \big) [ u (Y) - u (y) ].\tag{4.2}
$$

Considering all of these equations, we can derive the following:

$$
u (x _ {1}) - u (x _ {0}) = u (x _ {2}) - u (x _ {1})\tag{4.3}
$$

The outcome $x _ { 1 }$ is the utility midpoint of $x _ { 0 }$ and $x _ { 2 }$ from another perspective. For losses, we can duplicate a similar process for negative prospects (i.e., a decreasing standard sequence $x _ { 0 } , \ x _ { 1 } , \ x _ { 2 }$ for $0 \ge y > Y > x _ { 0 } > x _ { 1 } > x _ { 2 } )$ . The utility relation $2 u ( x _ { 1 } ) = u ( x _ { 0 } ) - u ( x _ { 2 } )$ is again applied for losses.

Linear approximation in utility is a common hypothesis [43]. It is consistent with the results in the literature [21, 43, 44] and empirically tested in [45]. $\mathrm { B P 0 0 ^ { \circ } s }$ method is based on a linear interpolation of the two outcomes $Z \mathbf { r }$ and $Z s$ (by fixing $p )$ and has forcefully proved the reasonability of the current hypothesis. We consider a utility unit denoted as $\Delta$ for $\Delta { = } u ( x _ { 2 } ) - u ( x _ { 1 } )$ (exactly as it will be $\Delta = u ( x _ { 1 } ) - u ( x _ { 0 } ) )$ . For a linear utility in $\left[ x _ { 1 } , \ x _ { 2 } \right]$ , the unit can be given by $\Delta = \dot { \rho } ( x _ { 2 } - x _ { 1 } )$ . This unit exclusively depends on the difference between two adjacent outcomes as $x _ { 2 } - x _ { 1 }$ . Similar to $[ x _ { 0 } , \ x _ { 1 } ]$ , the unit can be given by $\Delta = \ddot { \rho } ( x _ { 1 } - x _ { 0 } )$ . We then derive $\Delta = { \dot { \rho } } ( x _ { 2 } - x _ { 1 } ) = { \ddot { \rho } } ( x _ { 1 } - x _ { 0 } ) = \rho \theta$ . In the experiments, a sophisticated manner is set at $\theta = ( x _ { 2 } - x _ { 0 } ) / 2$ , which is called an outcome unit. This manner is for a more precise measurement that is illustrated in our experimental studies. Consequently, $\Delta = \rho \theta$ can hold true for $\theta = ( x _ { 2 } - x _ { 0 } ) / 2$ . When $\{ x _ { 0 } , \ x _ { 1 } , \ x _ { 2 } \}$ is a decreasing standard sequence of losses, this result holds true with a slight difference (i.e., $\Delta < 0$ and $\theta < 0 )$ . For both gains and losses, we hold $\rho > 0$ since $u ( . )$ is assumed a strictly increasing function per se.

The next step is to establish preference differences. We define a disturbance factor ??, which is measured by $\delta = \lambda \theta / \gamma$ , where integers $\lambda , \gamma \in \mathbb { Z } , \ \gamma \geq 1$ , and $\lambda \in \{ 1 - \gamma , \dots , \gamma - 1 \}$ . A precision-varied outcome $x _ { m }$ is defined as $x _ { m } = x _ { 1 } + \delta .$ . In this sense, utility midpoint $x _ { 1 }$ is a reference point in constructing $x _ { m }$ . Parameter ?? controls the level of equidistant segmentations on $[ x _ { 0 } , x _ { 1 } ]$ and $[ x _ { 1 } , x _ { 2 } ]$ . The interpolated $x _ { m }$ can be interpreted as a deviation of the reference $x _ { 1 : }$ , where such deviations are further controlled by parameter ??. Independent parameter ?? is installed by experimenters subjectively, whereas ?? fully depends on the ?? value.

The indifferences are constructed as $x _ { m } { \sim } ( x _ { 2 } , p _ { m } ; x _ { 0 } )$ , which suggests the same attractiveness between a two-outcome prospect $( x _ { 2 } , p _ { m } ; x _ { 0 } )$ and a sure outcome $x _ { m } ,$ where $m = ( 1 - \gamma , \dots , 0 , \dots , \gamma - 1 )$ ). The indifference implies the following based on the CPT/RDU:

$$
w \left(p _ {m}\right) = \frac {u \left(x _ {m}\right) - u \left(x _ {0}\right)}{u \left(x _ {2}\right) - u \left(x _ {0}\right)} = \frac {\Delta - \left[ u \left(x _ {1}\right) - u \left(x _ {m}\right) \right]}{2 \Delta}\tag{4.4}
$$

Given $x _ { m } = x _ { 1 } + \delta$ and $\Delta = \rho \theta$ for $\rho > 0$ , we can derive the following:

$$
w (p _ {m}) = \frac {\rho \theta - \rho (x _ {1} - x _ {m})}{2 \rho \theta} = \frac {\theta - (x _ {1} - x _ {m})}{2 \theta} = \frac {\theta + \delta}{2 \theta}\tag{4.5}
$$

Given $\delta = \lambda \theta / \gamma$ , we can derive the following:

$$
w (p _ {m}) = \frac {\theta + \delta}{2 \theta} = \frac {\gamma + \lambda}{2 \gamma} \text {and} p _ {m} = w ^ {- 1} \left(\frac {\gamma + \lambda}{2 \gamma}\right)\tag{4.6}
$$

This method implies that the probability weighting function ?? can be elicited by constructing a series of indifferences $x _ { m } { \sim } ( x _ { 2 } , p _ { m } ; x _ { 0 } )$ , where the outcome $x _ { m }$ is parametrically controlled by ?? and ??. The experimenters install the degree of precision ?? for $1 \leq \gamma \in \mathbb { Z }$ and the value of ?? for $\lambda \in \{ 1 - \gamma , \dots , \gamma -$ 1}. Subjects provide the answer to $p _ { m }$ by examining the indifferences. The decision weights can be fully revealed by the subjects’ answers over $p _ { m }$

For losses, we consider the decreasing standard sequence $\{ x _ { 0 } , \ x _ { 1 } \ , x _ { 2 } \}$ , where $x _ { 0 } > x _ { 1 } > x _ { 2 }$ . We can find a sequence of probability $q _ { m }$ for $\mathfrak { m } = ( 1 - \gamma , \dots , 0 , \dots , \gamma - 1 )$ that satisfies $x _ { m } { \sim } ( x _ { 2 } , q _ { m } ; x _ { 0 } )$ , where $x _ { m } = x _ { 1 } + \delta$ and $x _ { 2 } < x _ { m } < x _ { 0 } < 0$ . We can derive $w ( q _ { m } ) = ( \theta + \delta ) / 2 \theta = ( \gamma + \lambda ) / 2 \gamma$ , which finally yields $q _ { m } = w ^ { - 1 } ( ( \gamma + \lambda ) / 2 \gamma )$ for losses.

The precision degree is exclusively controlled by the parameter ??. The ?? value depends on ?? by sequentially assigning from $1 - \gamma$ to $\gamma - 1$ , which is called the dependent parameter. The ?? value can be segmentation is measured by $\theta / \gamma .$ . The ?? value is the ?? value multiplied by ??/??, where ?? indicates the $\theta / \gamma ,$ extent of deviations of the outcome $x _ { 1 : }$ , which is exactly the utility midpoint of $x _ { 0 }$ and $x _ { 2 }$ . The VP method can elicit a total of $2 \gamma - 1$ data points of the probability weighting function that corresponds to $2 \gamma - 1$ assignments of ??. Thus, the probability weighting function can be measured in any desired degree of precision as desired by experimenters. For example, for $\gamma = 3$ , we can obtain five $( 2 \gamma - 1 = 5 )$ data points as $w ^ { - 1 } ( 1 / 6 ) , w ^ { - 1 } ( 2 / 6 ) , w ^ { - 1 } ( 3 / 6 ) , w ^ { - 1 } ( 4 / 6 )$ , and $w ^ { - 1 } ( 5 / 6 )$ , which correspond to the ?? assignments as ˗2, ˗1, 0, 1, and 2, consecutively. Another example of utilizing vKW11’s data $( x _ { 0 } ~ = 6 0 , ~ x _ { 1 } ~ = 9 2 . 2 5$

, and $x _ { 2 } ~ = ~ 1 2 3 )$ is as follows: when setting $\gamma = 6$ and $\theta / \gamma = 3 1 . 5 / 6 = 5 . 2 5$ , 11 interpolated outcomes $x _ { m } { = } ( 6 6 , . . . , 9 2 . 2 5 , . . . , 1 1 8 . 5 )$ can be utilized to build 11 indifferences to elicit 11 data points of the probability

weighting function w(.).

We analyze three special cases. If $\gamma = 1$ $\lambda = 0$ , and $\delta = 0$ are set, then $w ( p _ { m } ) = \gamma / 2 \gamma = 1 / 2$ because of the indifference $x _ { 1 } { \sim } ( x _ { 2 } , p _ { m } ; x _ { 0 } )$ . We then derive $p _ { m } = w ^ { - 1 } ( 1 / 2 )$ . This case implies that no partition exists in two half-intervals $[ x _ { 0 } , x _ { 1 } ]$ and $[ x _ { 1 } , x _ { 2 } ] .$ ; the interpolated outcome $x _ { m }$ is reduced to the utility midpoint $x _ { 1 } ,$ , which is also the midpoint of probability weightings. For one extreme, if $\lambda = \gamma$ , and $\delta = \theta$ , then $x _ { m }$ is reduced to the lower boundary of the sequence $x _ { 0 }$ . We derive $p _ { m } = w ^ { - 1 } ( 0 ) = 0$ because of the indifference $x _ { 0 } { \sim } ( x _ { 2 } , p _ { m } ; x _ { 0 } )$ . For the other extreme, if $\lambda = - \gamma .$ , and $\delta = - \theta$ , then $x _ { m }$ is $x _ { k }$ $p _ { m } = w ^ { - 1 } ( 1 ) = 1$ because of the indifference $x _ { 2 } { \sim } ( x _ { 2 } , p _ { m } ; x _ { 0 } )$ . Excluding the two extremes, the dependent parameter ?? is bounded as $\lambda \in \{ 1 - \gamma , \dots , \gamma - 1 \}$ , rather than $\{ - \gamma , \dots , \gamma \}$

## 4.2 Acceptability of Linear Approximation in Utility

The VP method assumes linear approximation in utility over the interval $[ x _ { 0 } , x _ { 2 } ]$ , which is consistent with the common hypothesis of linear utility for moderate amounts of money [43]. Previous experimental studies have forcefully supported that the deviation from linearity in utility function is insignificant if a fine standard sequence exists (e.g., Wakker and Deneffe [21]; BP00, p. 1489; vKW11, p. 586). The linearity of utility can be directly examined from the elicited three-outcome sequence at the first stage by utilizing the VP method. Once deviations from linearity are strong, an experimenter can correct it through adjusting the reference outcomes to the end of a sufficiently fine sequence.

In order to warrant this assumption, we provide an application condition of the VP method. We simply consider the case of gains that follow. Our method is applicable when the precision degree $\gamma \in \mathbb { Z }$ satisfies the condition as follows:

$$
\gamma <   \frac {x _ {2} - x _ {0}}{2 | x _ {2} + x _ {0} - 2 x _ {1} |}\tag{4.7}
$$

This inequality says that $| ( x _ { 2 } - x _ { 1 } ) - ( x _ { 1 } - x _ { 0 } ) | < \theta / \gamma$ for $\theta = ( x _ { 2 } - x _ { 0 } ) / 2$ . When the utility over the interval $\left[ x _ { 0 } , \ x _ { 2 } \right]$ is absolutely linear, we ideally have $\Delta = \dot { \rho } ( x _ { 2 } - x _ { 1 } ) = \ddot { \rho } ( x _ { 1 } - x _ { 0 } ) = \rho \theta$ for ${ \dot { \rho } } = { \ddot { \rho } } = \rho$

Inequality $0 < \theta / \gamma$ is thus always satisfied for any degree of precision. The utility function is convex if $x _ { 2 } - x _ { 1 } < x _ { 1 } - x _ { 0 }$ , whereas it is concave if $x _ { 2 } - x _ { 1 } > x _ { 1 } - x _ { 0 }$ . The absolute value of the difference between $x _ { 2 } - x _ { 1 }$ and $x _ { 1 } - x _ { 0 }$ measures the deviation of linearity in utility. Dividing the outcome unit ?? by the artificial setting ?? is the precision in terms of the outcome values. The value $\theta / \gamma$ is the smallest unit of the partition in $x _ { 2 } - x _ { 0 }$ from another perspective. The inequality ensures that the smallest unit that is controlled by the precision ?? can be salient to the extent that the assumption of linear utility approximation is fully acceptable. If the difference between $x _ { 2 } - x _ { 1 }$ and ${ x _ { 1 } - x _ { 0 } }$ is larger (or equal) to the smallest precisions, we can identify that the assumption does not hold true for the VP method.

We further emphasize the condition of linear approximation in utility for strengthening the rigor of our method. Different from other comparable methods, the setting of the precision degree in the VP method offers a powerful tool that can measure quantitatively applicability of a nonparametric method. As ?? can be set as experimenters’ desires, this stated condition implies the upper boundary of ??. In a laboratory, the ?? settings should neither be extremely small nor extremely large. The settings of an excessively small ?? could weaken the advantage of the VP method. The settings of an excessively large ?? could also enlarge the bias in the assessment of the probability weighting function (i.e., in the probability near impossibility and certainty of the probability scale) and be more laborious. One should tradeoff accuracy and necessity when choosing ??. Experimenters should consider how many measuring points they would like to elicit for sketching the probability weighting function. As our experimental studies, two precision degrees $\gamma = 5$ and $\gamma = 6$ are chosen to elicit 9 and 11 points, respectively. Generally, eliciting around 10 measuring points can be suitable over a reasonable number of subjects.

## 5. Measuring Utility and Decision Weights: An Experimental Study

This section presents our experimental studies that utilize the TO method to measure utility as the preliminary stage. The VP method is then applied to measure the probability weighting function.

(a) Subjects: A total of N = 46 participants with various profiles<sup>2</sup> were recruited from The Hong Kong Polytechnic University (PolyU). The participants were self-selected from a mailing list of 6,752 potential participants through the SONA Research Participation System. We initially conducted a pilot study to adjust the experiment protocol (6 subjects; 2 females; median age 32; research assistants). Formal experiments were conducted at the Behavioral Research Lab (BRL), Department of Management and Marketing, PolyU. Four subjects were eliminated from the analysis because their answers did not fully satisfy our defined linearity condition. Our analysis is thus based on the remaining 42 subjects (26 females; median age 21).

(b) Procedure: Subjects were seated in front of personal computers in an experimental room (can accommodate a maximum of 15 people in BRL). Four sessions were conducted successively (average of 11 participants showed up for one session). After receiving experimental instructions, the subjects were provided with two pilot-trial questions to familiarize themselves with the procedure. The formal questions then followed. The experiments contained two successive sections: one for gains and one for losses. The first section is the elicitation of utility (TO-experiments), whereas the second section is the elicitation of probability weightings (PW-experiments). The outputs of the TO-experiments (i.e., x<sub>1</sub> and x<sub>2</sub>) are the inputs of the subsequent PW-experiments. The default currency was Hong Kong Dollars (HKD or “\$”). Each subject was paid 40 HKD (approximately USD \$5.1) for their participation.

(c) Stimuli: Table 1 shows that options A and B yield stakes and corresponding probabilities. It contains four stakes and two values of probabilities. In the TO-experimental trials, we fixed all probabilities p and $q$ (where $p = q )$ . The stakes of gambles varied in the experimental trails. The subjects selected between two options. In the PW-experimental trials, the stakes $x _ { 0 }$ and $x _ { 2 }$ are fixed, and $x _ { m }$ is provided dynamically among trials. Subjects were asked to select a value for the probability $P ,$ such that two options were indifferent (equally attractive) to him/her. The outcome $x _ { m }$ was automatically calculated by following the logic of the VP method, and the values of $x _ { 1 }$ and $x _ { 2 }$ were obtained as before. Computer programs outputted each $x _ { m }$ to construct each trial. The subjects were encouraged to answer questions at their own

pace.

Table 1. Framing of the prospect pairs.

<table><tr><td>TO</td><td>Option A</td><td>Option B</td></tr><tr><td>Trails</td><td>q% Chance to Win (Loss)  $x_{i}$ (100-q)% Chance to Win (Loss) y</td><td>p% Chance to Win (Loss)  $x_{i-1}$ (100-p)% Chance to Win (Loss) Y</td></tr><tr><td>PW</td><td>Option A</td><td>Option B</td></tr><tr><td>Trails</td><td>100% Chance to Win (Loss)  $x_{m}$ [0% Chance to Win (Loss)  $x_{0}$ ]</td><td>P% Chance to Win (Loss)  $x_{2}$ (100-p)% Chance to Win (Loss)  $x_{0}$ </td></tr></table>

(d) Measuring Utility in TO Experiments: For gains, we set $\boldsymbol { y } = \mathbb { 8 } 3 \mathbb { K } , \boldsymbol { Y } = \mathbb { 8 } 4 \mathbb { K } , \boldsymbol { x } _ { 0 } = \mathbb { 8 } 6 \mathbb { K } , ( \mathrm { K } { = } 1 , 0 0 0 ) ^ { 3 }$ and set $p \ = \ 2 5 \%$ . The indifferences were built as follows: $( x _ { 1 } , 0 . 2 5 ; 3 K ) { \sim } ( 6 K , 0 . 2 5 ; 4 K )$ and $( x _ { 2 } , 0 . 2 5 ; 3 K ) { \sim } ( x _ { 1 } , 0 . 2 5 ; 4 K )$ . The (increasing) standard sequence results were $x _ { 0 } , x _ { 1 } .$ , and $x _ { 2 } .$ For the losses, we set y = ˗ 3K, Y = ˗ 4K, $x _ { 0 } ~ = ~ - ~ 8 \mathsf { K }$ , and $\begin{array} { r l r } { p } & { { } = } & { 7 5 \% . } \end{array}$ The indifference was built as $( - 3 K , 0 . 7 5 ; x _ { 1 } ) { \sim } ( - 4 K , 0 . 7 5 ; - 8 K )$ and $( - 3 K , 0 . 7 5 ; x _ { 2 } ) { \sim } ( - 4 K , 0 . 7 5 ; x _ { 1 } )$ . The (decreasing) standard sequence results were $x _ { 0 } , x _ { 1 } ,$ and $x _ { 2 }$ . The elicited sequences for the gains and losses had equal distances in terms of utility, and $x _ { 1 }$ was the utility midpoint of x<sub>0</sub> and x<sub>2</sub>.

A bisection method was developed by Abd00 and applied by vKW11. This method only requires the subjects’ acts of selection between two options, which might be more consistent [46] but more laborious (it requires at least five iterations for one output). The VP method only requires two outcomes, and all subsequent processes rely on them. Therefore, employ this method after trading off consistency and time consumption. The details of the five iterations are presented in Appendix A.

(e) Measuring Results in Utility: All further measurements in our test depended on $x _ { 1 }$ and $x _ { 2 } .$ . Like vKW11, we elicited twice to lower the noise. The average of the two elicitations was adopted as the input of subsequent PW experiments. We ruled out four subjects for further analysis at the individual level because their answers failed to fulfill our defined acceptability of linearity. Given that we intended to install the precisions as $\gamma = 5$ and $\gamma = 6 .$ , the average values of $x _ { 1 }$ and $x _ { 2 }$ must entail the inequality $| x _ { 2 } + x _ { 0 } -$ $2 x _ { 1 } | < \theta / 6$ for $\theta = | x _ { 2 } - x _ { 0 } | / 2$ , to ensure a permissible deviation from linearity. Our analyses will be

based on the remaining 42 subjects.

Overall, the mean values of $x _ { 1 }$ and $x _ { 2 }$ are 9,320 (˗11,410) and 12,800 $\left( - 1 4 , 9 3 0 \right) ^ { 4 }$ for gains (losses). Together with $x _ { 0 } = 6 , 0 0 0 \ ( \mathrm { x } _ { 0 } = \ - 8 , 0 0 0 )$ , the deviations in linearity for gains (losses) are fully acceptable. For gains, 30 (12) out of the 42 subjects exhibited a concave (convex) utility function. For losses, 15 (27) out of the 42 subjects exhibited a concave (convex) utility function. The results are robust for gender, age, and field of study.

(f) Measuring Probability Weightings in the PW Experiments: Utilizing the VP method, we set two degrees of precision in the elicitations of probability weighting functions. We intended to double the verifications on the risk attitudes of participants and the demonstrations of tractability of the VP method. In the first part (9p\_PW\_Exp), we install the precision $\gamma = 5 .$ We can then elicit the 9 measuring points as $w ^ { - 1 } ( i / 1 0 )$ for $i = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 )$ . In the second part (11p\_PW\_Exp), we install the precision $\gamma = 6$ We then immediately elicit 11 measuring points as $w ^ { - 1 } ( i / 1 2 )$ for i = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11).

We apply the mean value of the measured $x _ { 1 }$ (9,320) and ${ \bf X } _ { 2 }$ (12,800) as an example to illustrate the intermediate processes in constructing indifferences. The outcome unit can be obtained by $\theta ^ { + } = ( 1 2 8 0 0 -$ $6 0 0 0 ) / 2 = 3 4 0 0$ . By setting $\gamma = 5 ,$ , we generate 9 measuring points. Given that $\delta = \lambda \theta ^ { + } / \gamma$ and ${ x _ { m } } ^ { + } = { x _ { 1 } } ^ { + } + \delta$ where ${ x _ { 1 } } ^ { + } = 9 3 2 0$ , the intermediate results are illustrated in Appendix B. After setting $\gamma = 6 ,$ , we similarly elicit 11 measuring points. 11p\_PW\_Exp has more partitions in the utility space over $[ x _ { 0 } ,$ $x _ { 2 } ]$ as $\theta ^ { + } / \gamma = 5 6 7$ , compared with $\theta ^ { + } / \gamma = 6 8 0$ in 9p\_PW\_Exp.

We employed the direct matching method in the PW experiments because it is the simplest. We elicited 40 measuring points (20 for gains and 20 for losses). If employing the bisection method as TO experiments, one subject would face at least 200 trials that can be highly laborious and time-consuming. We applied a “multifold precision-variable approximation” method to induce subjects’ answers and obtain more consistent results.

Table 2 illustrates the procedure followed by computer programs to determine $\mathbf { w } ^ { - 1 } ( 1 / 2 )$ from the indifference $\mathbf { x } _ { \mathrm { m } } { \sim } ( \mathbf { x } _ { 2 } , ~ \mathbf { w } ^ { - 1 } ( 1 / 2 ) ; ~ \mathbf { x } _ { 0 } )$ where $\mathbf { X } _ { \mathrm { m } }$ is the utility midpoint $\mathbf { X } _ { 1 }$ (for gains, $\lambda = 0 , ~ \delta = 0$ , and $x _ { m } = x _ { 1 } = 9 , 3 2 0 )$ . “Range” indicates the output ranges that can be refined. “Precision” indicates the interval of two alternatives offered to subjects. “Start point” consists of three types: middle, start, and end, which suggest how to refine the outputs. Given that the second approximation (“middle”) means that the previous option of 60% is the middle point of the range 20%, then the computer-provided alternatives vary from (60˗10)% to (60+10)% at intervals of 2 unit in the two consecutive alternatives. Setting “start” offers alternatives {60%, 62%, ... , 80%}, whereas setting “end” offers alternatives {40%, 41%, ..., 60%}. Except for the first approximation, the following are installed as “middle” in our experiment. We conducted three approximations so that all outputs are the integers. The fourth approximation can also be performed to attain a precision of 0.5%. For each approximation, the number of alternatives provided to the subjects is equal to one (start point) plus the ratio of the range to the precision (e.g., 11 alternatives in our experiments).

Table 2. A multifold precision-variable approximation method for inducing $\mathbf { w } ^ { - 1 } ( 1 / 2 )$

<table><tr><td>Appr.</td><td>Range</td><td>Precision</td><td>Start Point</td><td>Alternatives of P offered to subjects</td><td>Choices</td></tr><tr><td>1</td><td>100</td><td>10 unit</td><td>-</td><td>{0, 10, 20, ..., 90, 100}</td><td>60%</td></tr><tr><td>2</td><td>20</td><td>2 unit</td><td>Middle</td><td>{50, 52, 54, ..., 68, 70} from 60%</td><td>64%</td></tr><tr><td>3</td><td>10</td><td>1 unit</td><td>Middle</td><td>{54, 55, 56, ..., 72, 74} from 64%</td><td>61%</td></tr><tr><td>4</td><td>5</td><td>0.5 unit</td><td>Middle</td><td>{58.5, 59, 59.5, ..., 63, 63.5} from 61%</td><td>61.5%</td></tr></table>

The approximation method advances the direct matching in lowering the subjects’ bias through multiple VPs. Some overlapping parts exist in terms of the ranges between two approximations. This scenario is actually desirable because it offers an opportunity for the subjects to amend their previous answers by reconsiderations<sup>5</sup>. Also, this approximation method is easy for implications by computer programs.

## 6. Analyses of Probability Weighting Functions

## 6.1 Results of Measuring Probability Weighting

We pooled the data for analysis and employed the data of median probability weighting. The means were similar to the medians, whereas the standard deviations were mostly less than 0.1 for gains and losses. We present clear counts of the subjects for gains and losses in Appendix C and illustrate the point-by-point raw statistics in Appendix D.

Figure 1 Median Probability Weighting Function for Gains and Losses  
![](/api/attachments/EAEQT2GH/fulltext/images/03f77ef8816b61ef2013507b2d9605187eb95f4b9614677eded9f1e747188838.jpg)

Figure 1 illustrates the results of our elicitation in probability weighting. We established two precisions as ?? = 5 and ?? = 6 for an intercomparison, and the results are shown in Figures 1-1 and 1-2, respectively. We used blue rhombus points for gains and red square points for losses. No significant differences existed between the gains and the losses when the two figures were observed separately because the red and blue points were in accordance with each other. Moreover, no significant differences existed between the two precision settings when the two figures were observed together. The elicitations were consistent over varied precisions. The four curves (red and blue) in the two figures generally fit the inverse-S shape, which is prevailing in the literature. Specifically, the moderate to high probabilities were significantly underweighted, while the low probabilities were only slightly overweighed. The probabilities of 0% to approximately 40% performed extremely close to their corresponding decision weight w(.). However, the probabilities beyond 40 until certainty clearly showed a deviation from the linear line w(p)=p that illustrates a deviation of expected utility theory and the risk-aversion pattern of people. The elicited functions revealed highly similar patterns. The exhibited deviations were robust in the double verification under different precision settings.

We conducted two comparisons with the benchmark in terms of measurements and their implications to justify the effectiveness of our method. First, we compared the elicited PW results of our method with that of Abd00. Abd00 recruited 46 subjects who were either undergraduate or Ph.D. students in economics in Paris, France. We repeated their results in Figure 1-1, with black dots for gains and black crosses for losses. Our method and that of Abd00 recorded slight risk-seeking patterns in the probabilities of 0% to approximately 40%. However, the subjects from Paris and Hong Kong exhibited risk aversion in the probabilities beyond 40% until certainty. While our subjects were more in accordance with gains and losses compared with that of Abd00, the subjects in $\mathrm { \ A b d { } 0 0 ^ { \circ } s }$ Paris experiment were more averse to risk over gains than over losses.

Second, we compared our elicited results with that of vKW11, as shown in Figure 1-2. vKW11 recruited 78 subjects who were undergraduate students from a wide range of disciplines at the University of Amsterdam in the Netherlands. We repeated their results (only for gains), with black dots exhibiting a complete convex curve. The results illustrated a risk-aversion behavior in all probabilities of 0% to 100%. Subjects are optimistic if $\mathbf { w } ( \mathfrak { p } )$ is concave, pessimistic if $\mathrm { w } ( \mathfrak { p } )$ is convex, and rational if the curve obeys w(p)=p. Thus, people in Amsterdam hel essimistic attributes toward all probabilities of events, and the extent of pessimism was strong when the probability was small. Conversely, people in Paris and Hong Kong were relatively more rational when the probability was small (approximately under 40%) but became pessimistic when the probabilities of events increased from 40% to 100%.

## 6.2 Nonparametric Analyses

## 6.2.1 Classification of Individual Probability Weighting

We evaluated individual probability weightings through a classification system that was applied in BP00 and vKW11. We used the data result in 11p\_PW\_Exp hereafter because it contained numerous measuring points. We used slope differences as the evaluation criterion, as it measured the changes in the average slope of the probability weighting function between two neighboring probability intervals. Individual probability weighting can be classified into four categories. First, we identified the lower (upper) subadditivity if the slope difference was negative (positive) in the three interval crossings [8%, 34%] (three interval crossings [66%, 92%]). Second, we identified the inverse-S shape if it satisfied the lower and upper subadditivities. Third, we identified the concavity (convexity) if at least eight slope differences were negative (positive) as well as if the upper (lower) subadditivity was not exhibited. Fourth, we identified the linearity if at least eight slope differences were zero as well as if the upper (lower) subadditivity was not exhibited.

Table 3 shows the results of the individual weighting functions and their classifications. The results revealed the strongest evidence in the upper subadditivity, followed by the lower subadditivity. As the intersection, the inverse-S shape was significant for gains (38.1%) and losses (42.9%). Nearly one-third of the subjects were identified as convex (pessimistic) functions. Their percentage significantly dominated that of the concave (optimistic) functions (i.e., 2.4%). Absolute rationality was exhibited by only one subject, whose weighting function was purely linear in gains and losses. Moreover, we determined that 9.5% (14.3%) of the subjects remained unclassified for gains (losses), in which only one subject revealed an abnormal S-shaped weighting only for losses.

Table 3. Classification of Individual Weighting Functions According to “Slope Differences”

<table><tr><td>11p_PW_Exp</td><td>11p for Gains</td><td>11p for Losses</td></tr><tr><td>Upper subadditivity</td><td>36/42 (85.7%)</td><td>37/42 (88.1%)</td></tr><tr><td>Lower subadditivity</td><td>18/42 (42.9%)</td><td>20/42 (47.6%)</td></tr><tr><td>Inverse-S shape</td><td>16/42 (38.1%)</td><td>18/42 (42.9%)</td></tr><tr><td>Convex</td><td>15/42 (35.7%)</td><td>15/42 (35.7%)</td></tr><tr><td>Concave</td><td>1/42 (2.4%)</td><td>1/42 (2.4%)</td></tr><tr><td>Linear</td><td>1/42 (2.4%)</td><td>1/42 (2.4%)</td></tr><tr><td>Unclassified</td><td>4/42 (9.5%, S shape: 0/42)</td><td>6/42 (14.3%, S shape: 1/42)</td></tr></table>

## 6.2.2. Analyses on Curves of Probability Weighting Functions

Diminished sensitivity was exhibited by the lower (and upper) subadditivity. This feature suggested that the probability weights of an outcome decreased with the distance from the natural boundaries of zero (and one). Generally, people are increasingly sensitive near impossibility $( p = 0 \% )$ and certainty $( \boldsymbol { p } = 1 0 0 \% )$ . Table 3 implies that subjects who exhibited upper subadditivity were pronounced among subjects (over 85% for gains and losses), which was nearly double that of subjects who exhibited lower subadditivity. Furthermore, Table 3 suggests that the distortions of the median probability weighting near zero were weaker compared with the distortions near one as well as closely linear. According to our experimental results, the certainty effect was stronger than the possibility effect. Therefore, Hong Kong residents tended to be more sensitive to the certainty than to the impossibility.

In the literature, Bruhin, Fehr-Duda, and Epper [47] concluded that Chinese optimism in lottery valuation is prevalent based on experiments in Beijing (China). According to the empirical studies of Kachelmeier and Shehata [48] in Beijing and Hsee and Weber [49] in Shanghai, Chinese respondents are relatively more risk-seeking compared with Westerners. However, the result in our experiments did not echo these findings. Table 3 shows that the percentages of lower subadditivity and concave individual probability weighting were not pronounced. Our data showed that more than half of the subjects did not exhibit optimistic attitudes for low probabilities, and nearly one-third of the subjects exhibited pessimism for all probabilities. Informally, the subjects in our experiments were predominantly consistent in feeling that a 95% chance was much less than certainty, whereas less than half felt that a 5% chance was much more than an impossibility. Our results showed that compared with Beijing [47, 48] or Shanghai [49], optimistic people living in Hong Kong were relatively few<sup>6</sup>.

We explained our findings on significant patterns of Hong Kong residents from two perspectives. First, substantial cultural differences exist between Hong Kong and other Chinese cities such as Beijing [47, 48] and Shanghai [49]. Hong Kong is regarded as the city with the highest degree of economic freedom in the world and was ranked first successively from 1995 to 2016 by the Heritage Foundation and the Wall Street

Journal<sup>7</sup>. People living in such a society have the highest freedom in terms of personal choices, including employment, production, consumption, and investments. These choices in turn force individuals to make prudent decisions and psychologically reduce people’s subjective belief in “luck.” Further studies can be possible future directions.

Second, the departure from the previous literature could be attributed to differences in the order of magnitude of the gambling stakes. According to FP14 [50], risk-seeking behavior for gains tends to be salient when the order of magnitude of stakes is low<sup>8</sup>. In our experiments, a subject who was indifferent toward a gamble of (\$12,800, 60%; \$6,000) and a sure payment of \$9,320 tended to strictly prefer (\$128, 60%; \$60) over \$93.2. Stakes that are two orders of magnitude lower will promote the tendency of people to become risk-seeking (for gains). Compared with the experiments in the literature [47, 48, 49], our gambling stakes were at least two orders of magnitude higher. Thus, risk-seeking patterns may not be largely salient<sup>9</sup>.

Finally, the conclusion in [47, 48, 49] could be supported if our findings were compared with that of vKW11. vKW11 reported a purely convex (strictly pessimistic) weighting function, in which 23.44% of subjects exhibited concave and 53.13% of subjects exhibited convex. Figure 1-2 shows that the conclusions of previous studies can be rewritten, as Hong Kong residents were more risk-seeking (optimistic) compared with a portion of the population of Westerners, such as those living in Amsterdam. Additional investigations are recommended for future studies.

## 6.3 The Parametric Analyses

Several parametric specifications of the probability weighting function have been reported in the literature.

Section 3.1 shows that their representatives contain a family of two-parameter weighting functions, including

GE87’s PW(A) and Prelec’s (1998) PW(B), a family of one-parameter weighting functions, including Prelec’s (1998) PW(C) and TK92’s PW(D), and a non-inverse-S power function PW(E). We estimated all of these listed parametric specifications by utilizing our experimental data. The histograms of parameter distributions are presented in Appendix E. Appendix F exhibits our examinations of gender differences.

We estimated the corresponding parameters for each subject and specification as shown in Table 4. The median values of the estimated parameters are in the 5th (gains) and 11th (losses) rows, followed by the standard errors in parentheses. We applied the Chi-squared (Pearson’s $x ^ { 2 } )$ parameter to each subject to measure the deviations between the actual data and data expected by different specifications. In particular, $\textstyle x ^ { 2 } = \sum _ { i = 1 } ^ { 1 1 } ( ( o _ { i } - e _ { i } ) ^ { 2 } / e _ { i } )$ , where $o _ { i }$ is the value of the ith actual data point, and $e _ { i }$ is the value of the ith accepted data point. The average values of the Chi-squared parameters of all subjects are given in the 6th (gains) and 12th (losses) rows. Furthermore, we estimated the Chi-squared distances of the parametric fits from the median data as shown in the 7th (gains) and 13th (losses) rows. These results clearly show that the two-parameter families perform better than the one-parameter family, where GE87’s specification is the best parametric fitting. Within the one-parameter family, TK92’s specification is better than Prelec’s. The use of Hey and Orme’s [33] power family is remarkably unqualified because its distances from our data are extreme specification are also shown in the 8th (9th) row for gains and 14th (15th) row for losses for a full comparison. The corresponding Chi-squared distances shown in parentheses.

Table 4. Results of representative parametric specifications of $\mathbf { w } ( . )$ based on our 11p\_PW\_Exp

<table><tr><td>Classification</td><td colspan="2">Two-parameter specifications</td><td colspan="3">One-parameter specifications</td></tr><tr><td>Representative studies</td><td>PW(A): GE87</td><td>PW(B): Prelec [32]_1</td><td>PW(C): Prelec [32]_2</td><td>PW(D): TK92</td><td>PW(E): Hey and Orme [33]</td></tr><tr><td>w(p)=</td><td> $\frac{\delta p^{\gamma}}{\delta p^{\gamma}+(1-p)^{\gamma}}$ </td><td> $e^{-\delta(-\ln p)^{\gamma}}$ </td><td> $e^{-(-\ln p)^{\gamma}}$ </td><td> $\frac{p^{\gamma}}{[p^{\gamma}+(1-p)^{\gamma}]^{1/\gamma}}$ </td><td> $p^{\gamma}$ </td></tr><tr><td colspan="6">Parameter Estimate for Gains</td></tr><tr><td>Median values of estimated parameters</td><td> $\delta^{+}=0.7667$  (0.031) $\gamma^{+}=0.6466$  (0.022)</td><td> $\delta^{+}=1.0839$  (0.030) $\gamma^{+}=0.6270$  (0.023)</td><td> $\gamma^{+}=0.6238$  (0.027)</td><td> $\gamma^{+}=0.6911$  (0.018)</td><td> $\gamma^{+}=1.2293$  (0.067)</td></tr><tr><td>Average Chi-squared parameter ( $x^{2}$ )</td><td>0.0278</td><td>0.0289</td><td>0.0499</td><td>0.0424</td><td>0.1024</td></tr></table>

Journal Pre-proof

<table><tr><td>Distance from median data</td><td>0.0068</td><td>0.0071</td><td>0.0121</td><td>0.0086</td><td>0.0519</td></tr><tr><td>Parameters fitting based on median data</td><td> $\delta^{+}=0.7629$  $\gamma^{+}=0.7283$  $(x^{2}=0.0017)$ </td><td> $\delta^{+}=1.0986$  $\gamma^{+}=0.6970$  $(x^{2}=0.0030)$ </td><td> $\gamma^{+}=0.6687$  $(x^{2}=0.0103)$ </td><td> $\gamma^{+}=0.7062$  $(x^{2}=0.0082)$ </td><td> $\gamma^{+}=1.1966$  $(x^{2}=0.0515)$ </td></tr><tr><td>Parameters fitting based on mean data</td><td> $\delta^{+}=0.7470$  $\gamma^{+}=0.7219$  $(x^{2}=0.0032)$ </td><td> $\delta^{+}=1.1101$  $\gamma^{+}=0.6862$  $(x^{2}=0.0045)$ </td><td> $\gamma^{+}=0.6552$  $(x^{2}=0.0135)$ </td><td> $\gamma^{+}=0.6971$  $(x^{2}=0.0105)$ </td><td> $\gamma^{+}=1.1966$  $(x^{2}=0.0605)$ </td></tr><tr><td colspan="6">Parameter Estimate for Losses</td></tr><tr><td>Median Estimated parameters</td><td> $\delta^{-}=0.7482$  $(0.034)$  $\gamma^{-}=0.6962$  $(0.026)$ </td><td> $\delta^{-}=1.0931$  $(0.029)$  $\gamma^{-}=0.6596$  $(0.024)$ </td><td> $\gamma^{-}=0.6254$  $(0.023)$ </td><td> $\gamma^{-}=0.6817$  $(0.017)$ </td><td> $\gamma^{-}=1.2222$  $(0.077)$ </td></tr><tr><td>Average Chi-squared parameter  $(x^{2})$ </td><td>0.0220</td><td>0.0235</td><td>0.0483</td><td>0.0405</td><td>0.1219</td></tr><tr><td>Distance from median data</td><td>0.0023</td><td>0.0040</td><td>0.0114</td><td>0.0077</td><td>0.0587</td></tr><tr><td>Parameters fitting based on median data</td><td> $\delta^{-}=0.7603$  $\gamma^{-}=0.7018$  $(x^{2}=0.0021)$ </td><td> $\delta^{-}=1.0952$  $\gamma^{-}=0.6738$  $(x^{2}=0.0039)$ </td><td> $\gamma^{-}=0.6478$  $(x^{2}=0.0109)$ </td><td> $\gamma^{-}=0.6918$  $(x^{2}=0.0075)$ </td><td> $\gamma^{-}=1.1897$  $(x^{2}=0.0582)$ </td></tr><tr><td>Parameters fitting based on mean data</td><td> $\delta^{-}=0.7439$  $\gamma^{-}=0.7353$  $(x^{2}=0.0031)$ </td><td> $\delta^{-}=1.1165$  $\gamma^{-}=0.6985$  $(x^{2}=0.0044)$ </td><td> $\gamma^{-}=0.6646$  $(x^{2}=0.0144)$ </td><td> $\gamma^{-}=0.7023$  $(x^{2}=0.012)$ </td><td> $\gamma^{-}=1.2216$  $(x^{2}=0.0544)$ </td></tr></table>

Figure 2. Parameter fittings of median probability weighting functions in 11p\_PW\_Exp  
![](/api/attachments/EAEQT2GH/fulltext/images/9e74924a633982c077cddc10c152a42f550b3b1c47534a3312dfefca3529cf7d.jpg)

![](/api/attachments/EAEQT2GH/fulltext/images/e6c01969cb5269eb973e369aa2e2a8c6dc135279eef4e876567a37acf190c59f.jpg)  
1. Blue dots show median PW for gains;  
2. Black dashed line is linearity $\mathbf { w } ( \mathfrak { p } ) = \mathfrak { p } ;$  
1. Blue squares show median PW for losses;  
2. Black dashed line is linearity $\mathbf { w } ( \mathfrak { p } ) = \mathfrak { p } ;$

$$
\delta = 0. 7 6 6 7
$$

$$
\delta = 0. 7 4 8 2
$$

$$
\gamma = 0. 6 4 6 6
$$

$$
\gamma = 0. 6 2 7 0;
$$

$$
\delta =
$$

$$
\gamma = 0. 6 9 6 2; \mathrm{PW(B)}
$$

$$
\gamma = 0. 6 5 9 6;
$$

$$
\delta = 1. 0 9 3 1
$$

<table><tr><td>with γ = 0.6911; PW(E) is Dash Curve with γ =1.2293.</td><td>γ =0.6254; PW(E) is Dash Curve with γ =1.2222.</td></tr></table>

Note: We did not illustrate the PW(C) curve because it is extremely close to the PW(B) curve, i.e., $\delta = 1 . 0 8 3 9$ in PW(B) for gains and δ =1.0931 in PW(B) for losses.

Figure 2 shows the different parametric fittings of the median probability weighting function. A two-parameter family shown in red and blue curves performs better than the others, whereas the non-inverse-S shaped power function shown in the dashed curve performs worst. Observing GE87’s PW(A), the probability weightings for gains suggest a stronger deviation from linearity than that for losses because of the smaller γ for gains. The parameter γ can be further interpreted as an index of deviation from rationality [54]. A systematic comparison between our estimated parameters and those in literature is detailed in Appendix G, which has extended the summary from FP14 (Table A.3).

## 6.4 Discussion

The advantages and disadvantages of the adoption of parametric and nonparametric elicitations have been verified in the literature [38]. Parametric methods have advantages in exhibiting highly featured functional forms, as numerous statistical toolkits are available. However, parametric methods must select a parametric formulation in advance, which generally cannot uncover real patterns in experimental data. Table 4 shows that the parametric method in our experiments is obviously unqualified to select the group of power functions for analyses. Furthermore, Prelec’s one-parameter specifications are likewise not the best options.

Human preference is contributed by outcome valuation u(.) and probability weighting w(.), independently. u(.) and w(.) capture different aspects of individual attitudes. Their overlap is not salient. Nonparametric methods, such as Abd00, vKW11, and our VPM, have advantages in examining u(.) and w(.) separately. Thus, nonparametric methods can minimize co-linearity effects between utility and decision weights. Given no prior parametric regulations, nonparametric methods can uncover actual patterns based purely on data.<sup>10</sup>

Our experimental results reveal that Hong Kong residents are pessimistic near the certainty $( \boldsymbol { p } = 1 0 0 \% )$

whereas pessimistic and optimistic groups appear to be polarized near the impossibility $( \boldsymbol { p } = 0 \% )$ . Although an inverse-S shape is accommodated, no parametric formulations can fit all of the measuring points, particularly regarding low probabilities. Our parametric analysis recognizes that the two-parameter functional form of GE87 may be the best fit. However, Figure 2 shows that the distances from our data in low probabilities (i.e., 0% to 34%) are still larger than those in the median and high probabilities (i.e., 34% to 100%)<sup>11</sup>.

## 7. Comparisons with Other Nonparametric Methods

In the literature, vKW11’s midweight method has been recognized as the state-of-the-art approach, while Abd00’s method could be the most popular method for nonparametric elicitations [38]. We consider vKW11 and Abd00 as our main competitors. Multiple criteria are considered to evaluate these methods, in which the performances of vKW11 and Abd00 are the benchmark to justify the superiority of the VP method. The criteria include the conditions in standard sequence construction, the independence of indifference construction, the unfavorable impacts of chaining and error propagation, the effect of cognitive demand, the efficiency of PW elicitations, the distribution of measuring points, and the flexibility in experiments and in the laboratory. We summarize the performances of vKW11, Abd00, and our VP method under all the criteria in Table 5, then rank these methods according to superiority. Finally, we clarify possible limitations in the use of our proposed method in a laboratory.

## (A) Conditions in standard sequence construction

Standard sequence construction by the TO method is a common first stage for all nonparametric methods. In the literature, Abd00’s method first fixes a standard sequence then elicits probabilities of each internal outcome in that sequence. Conversely, the method of BP00 first fixes the probabilities then interpolates new outcomes that are not necessarily included in the standard sequence. Meanwhile, AVW05’s method incorporates BP00 and Abd00 for event-contingent prospects. A sufficiently complete standard sequence is required by Abd00, BP00, and AVW05. However, using these methods is hard to control the range of the sequence, which is a considerable drawback. vKW11<sup>12</sup> or our VP method (VPM henceforth) can resolve this problem because only two outcomes are needed in the first stage. The obtained inverse probability weightings can be exploited to derive additional probabilities. This mechanism substantially reduces the conditions in standard sequence construction in utility elicitation and thus overcomes the common drawback of all nonparametric elicitation. In other words, either vKW11 or the VPM can minimize the conditions in the construction of a standard sequence. Therefore, we can justify that VPM \~ vKW11≻Abd00 under this criterion, where “\~” represents the equivalent superiority, and “≻” means “superior to.”

## (B) Independence of indifference construction

vKW11 entails a treelike, n-level structure of indifferences (Figure 5 in [26], pp. 586 and 588). The probabilities used in the nth-level indifferences are inverse decision weights derived from their parent (i.e., the n-1 level). In other words, indifferences constructed in vKW11 are not independent but rely on their parent indifferences. This key feature in vKW11 could trigger unfavorable effects, including chaining and error propagation. Neither the VPM nor Abd00 relies on a hierarchical indifference and can induce indifferences independently. Therefore, we can justify that VPM \~ Abd00≻vKW11.

## (C) Impacts of chaining and error propagation

All nonparametric elicitations require choices between multiple two-outcome prospects. The subjects in the experiments could determine chaining relations among questions regarding choices, then answer these questions heuristically and untruthfully. Subjects could respond inconsistently or fall back on decision heuristics, such as using expected value maximization [38]. Given that chaining could weaken the robustness of elicited measurements, its effects are disadvantageous to all nonparametric methods. In addition, the subjects’ responses are chained in elicitations of utility and probability weightings. Errors could occur and are propagated in the standard sequence (i.e., the first stage) and in the subsequent steps (i.e., the second stage).

We analyze the chaining and error propagation from two stages. First, unfavorable impacts are experienced in the construction of a standard sequence through multiple chained choices. The VPM and vKW11 require only the least outcomes (only $x _ { 1 }$ and $x _ { 2 } )$ in this sequence, whereas Abd00 entails a complete sequence. Thus, the VPM and vKW11 minimize the impacts in the utility elicitation stage. Second, impacts are experienced in the construction of multiple indifferences. In vKW11’s treelike structure, choices in each level rely on the previous level where chaining is strengthened. Moreover, any errors in the parent levels are inevitably propagated into the children levels. For example, errors in the elicitation of $\mathbf { w } ^ { - 1 } ( 1 / 4 )$ and $\mathbf { w } ^ { - 1 } ( 3 / 4 )$ are undesirably propagated when $\mathbf { w } ^ { - 1 } \mathopen { } \mathclose \bgroup \left( 1 / 8 \aftergroup \egroup \right)$ and $\mathbf { w } ^ { - 1 } \big ( 7 / 8 \big )$ are elicited. Therefore, the impacts of chaining and error propagation are dramatically strengthened in the elicitation stage of probability weighting. Compared with vKW11, either VPM or Abd00 has a lower impact on chaining and error propagation because the subjects answers on the one question regarding choices rarely influence future stimuli.In summary, we can justify that $\mathrm { V P M } \sim \mathrm { v K W } 1 1 { \sim } \mathrm { A b d } 0 0$ in the first stage, whereas $\mathrm { \Delta V P M } \sim \mathrm { A b d } 0 0 { \sim } \mathrm { v K W } 1 1$ in the second stage. By combining the two stages, we can clearly conclude that the VPM surpasses vKW11 and Abd00 in this evaluation criterion, as illustrated by VPM≻Abd00 and VPM≻vKW11.

## (D) Impact of cognitive demanding

Nonparametric methods desirably preserve the relationship between measured utility and an individual’s actual options to uncover actual patterns exhibited by the subjects. Compared with (semi-) parametric and statistical methods, relatively high cognitive demanding exists in the group of nonparametric methods (Table A.4 in [38], p. 555). FP14 [38] (p. 552) pointed out that, “It (i.e., vKW11’s method) is extremely cognitively demanding because determining decision weights beyond the first midpoint requires participants to choose between pairs of two-outcome prospects whose probabilities also vary.” However, the VPM and Abd00 have the simplest structure of indifferences. A mixture of $x _ { 2 }$ and $x _ { 0 }$ is indifferent with one sure outcome $x _ { \mathrm { m } }$ as $( x _ { 2 } ,$ $p _ { \mathrm { m } } ; x _ { 0 } ) \sim x _ { \mathrm { m } } .$ This structure is the simplest and accomplishes the lowest cognitive demand in the group of nonparametric elicitations. Therefore, we can justify that VPM \~ Abd00≻vKW11 in this criterion.

## (E) Efficiency of PW elicitations

Each level in vKW11, except the first, includes two indifferences that can generate two measuring points. Each constructed indifference can produce one measuring point of decision weights, which has the highest efficiency in terms of data point generation. The VPM and Abd00 can achieve this level of efficiency. Nevertheless, BP00’s method requires two indifferences for one measuring point. Therefore, we can justify that “VPM \~ vKW11 \~ Abd00≻other methods” in the criterion of efficiency.

## (F) Distribution of measuring points in probability weighting

Through the use of vKW11, the elicited points of probability weighing are polarized in the distribution toward certainty $( p = 1 )$ and impossibility $( p = 0 )$ . Experimenters can elicit two measuring points, that is, $\mathbf { w } ^ { - 1 } ( 1 / 2 ^ { \mathrm { n } } )$ and $\mathbf { w } ^ { - 1 } ( ( 2 ^ { \mathrm { n } } { - } 1 ) / 2 ^ { \mathrm { n } } )$ , from two $\mathrm { n } ^ { \mathrm { t h } } .$ -level indifferences and elicit a total of 2n˗1 points. Although vKW11 is efficient, the concentration of points to two boundaries is unfavorable because key patterns in the middle probabilities may not be uncovered. This defect appears in vKW11 but is absent in the VPM and Abd00, in which measuring point distributions can be well distributed across the entire scale of probabilities from certainty to impossibility. Therefore, we conclude the rank of three methods as VPM \~ Abd00≻vKW11 in this criterion.

## (G) Flexibility in experiments and in the laboratory

The construction of indifferences in the VPM is strictly controlled by VP parameters. Flexible settings of precision variability make VPM more tractable in the laboratory. Multiple precision ?? can be installed, and multiple curves of $\mathbf { w } ( . )$ can be elicited, similar to our experiment. Experimenters can co-reference one another for comparable results, which are favorable in uncovering actual patterns of subjects. After ?? is installed, 2?? − 1 data points can be derived from $2 \gamma + 1$ observed indifferences (two indifferences at the first stage). Because using the VPM is less laborious, experimenters can be flexible in the laboratory. For example, multiple elicitation times and the use of their mean can reduce noise. In addition, the initial outcome $x _ { 0 }$ and reference outcomes y and Y can be adjusted in a timely manner to reach a sufficiently fine standard sequence (BP00, p. 1489). Conclusively, the VPM achieves the highest flexibility among all nonparametric elicitations. Therefore, we can justify that VPM≻Abd00 and VPM≻vKW11 in this criterion.

Table 5. Evaluations of outstanding nonparametric methods and ranking of superiority

<table><tr><td>Item</td><td>Criteria of Evaluation</td><td>The VP Method (VPM)</td><td>The Midweight Method (vKW11)</td><td>The popular Method (Abd00)</td><td>Ranking of Superiority</td></tr><tr><td>(A)</td><td>Conditions in eliciting utility</td><td>Minimized</td><td>Minimized</td><td>Benchmark (non-minimized)</td><td>VPM ~ vKW11 &gt;Abd00</td></tr><tr><td>(B)</td><td>Independence</td><td>Independent</td><td>Non-Independent</td><td>Independent</td><td>VPM ~ Abd00 &gt;vKW11</td></tr><tr><td rowspan="2">(C)</td><td rowspan="2">Error Propagation &amp; Chaining</td><td colspan="3">In the first stage: VPM ~ vKW11 &gt; Abd00</td><td rowspan="2">VPM&gt;vKW11; VPM&gt;Abd00</td></tr><tr><td colspan="3">In the second stage: VPM ~ Abd00 &gt; vKW11</td></tr><tr><td>(D)</td><td>Cognitive demanding</td><td>Less cognitive demanding</td><td>Benchmark</td><td>Less cognitive demanding</td><td>VPM ~ Abd00 &gt;vKW11</td></tr><tr><td>(E)</td><td>Efficiency</td><td>Highest</td><td>Highest</td><td>Highest</td><td>VPM ~ Abd00 ~ vKW11</td></tr><tr><td>(F)</td><td>Distribution</td><td>Uniform</td><td>Benchmark (highly polarized)</td><td>Uniform</td><td>VPM ~ Abd00 &gt;vKW11</td></tr><tr><td>(G)</td><td>Flexibility</td><td>The most flexible</td><td>Benchmark</td><td>More flexible</td><td>VPM&gt;vKW11; VPM&gt;Abd00</td></tr></table>

In summary, we justify the superiority of our VPM via thorough comparisons. The VPM is compared with the state-of-the-art vKW11 and the most popular Abd00 methods through the use of seven evaluation criteria. The VPM retains the favorable features of vKW11 in (A) by simplifying the first stage. Moreover, vKW11. In addition, the VPM achieves the highest efficiency of elicitations (E), similar to Abd00 and vKW11. Meanwhile, the VPM can overcome the defect of vKW11 in terms of point polarization (F). Finally, owing to precision settings, the flexibility of the VPM is the highest among all the nonparametric methods (G).

Limitations exist in using VPM. Firstly It requires a relatively large interval $[ x _ { 0 } , x _ { 2 } ]$ to leave the space of setting the precision degree ??. If the interval is excessively small, then a relatively large ?? will cause interpolated outcomes (particularly for ?? = 1 − ?? and ?? = ?? − 1) to become extremely near x<sub>0</sub> or x<sub>2</sub>. Elicitations from $( x _ { 2 } , p _ { \mathrm { m } } ; x _ { 0 } ) \sim x _ { \mathrm { m } }$ thus require high cognitive demanding; even the VP method becomes completely invalid. The upper boundary constraints of ?? also ensure validity that is far from reasonability.

The ?? value should be reasonably installed; not extremely small (to ensure sufficient measuring points) and not extremely large (to ensure sufficient differentiation between $x _ { \mathrm { m } }$ and $x _ { 0 } / x _ { 2 } )$ . Finally, the larger interval $[ x _ { 0 } ,$ x<sub>2</sub>] can weaken the acceptability of linear utility assumption<sup>13</sup>. Experimenters should cautiously set the initial $x _ { 0 }$ and reference outcomes y and Y for a sufficiently fine standard sequence $( x _ { 0 } , x _ { 1 }$ , and x<sub>2</sub>).

## 8. Conclusion

We introduced a new method for eliciting probability weighting under PT through using a simple precision-variable mechanism. Our experiments demonstrated the feasibility and advantages of our method of measuring risk attitudes. We argued that the present VP method advanced the family of nonparametric elicitation methods because it is more direct, efficient, and flexible, and less cognitively demanding. This method can minimize the required measurements of utility and maximize the flexibility of measurement of probability weighting. Experimenters can now capture deviations of expected utility in a tractable manner nearly without measuring utility. The VP method is built upon the descriptive decision theory PT. We compare our method with other nonparametric elicitations in a qualitative way. Our experiments uncover meaningful patterns among Hong Kong residents. We compare our experimental results with the results of different groups in Beijing, Shanghai, Paris, and Amsterdam. We find that more than half of subjects are optimistic (risk-seeking) toward low probabilities of events, and one third are pessimistic (risk-aversion) for all probabilities. Optimistic groups in Hong Kong are relatively fewer than those in Beijing and Shanghai of China. These results generally reject previous findings that the Chinese are relatively more optimistic than Westerners. Yet, we support previous findings if the Westerners refer in particular to the people living in Amsterdam. Our subjects in Hong Kong are rational when probabilities are small (approximately under 40%) but become pessimistic when probabilities increase, which echoes the patterns of Paris residents.

Empirical findings of this paper were based on a sample of students in the large university of Hong Kong, which provide references for policymakers (e.g., pension design) or business targets (e.g., insurance planning), yet may affect the generalizability of this study. Selecting a sample from other demographic groups is expected for future studies. In the theoretical aspect, new foundations and models of nonparametric elicitations are needed in the future in order to make PT testable and falsifiable.

Acknowledgments: We are grateful for the constructive comments of the referees on an earlier version of this paper. We are also indebted to Peter Wakker for his helpful comments. The first author was supported in part by Beijing Normal University-Hong Kong Baptist University United International College Research Grant under R201917. The second author was supported in part by the RGC Collaborative Research Fund under grant numbers E-RB0E and E-RB29.

## References

[1] K.R. MacCrimmon, Descriptive and Normative Implications of the Decision-Theory Postulates. in K. Borch and J. Mossin (ed.), Risk and Uncertainty, St. Martins Press, New York (1968) 3–32.

[2] P. Thagard, From the Descriptive to the Normative in Psychology and Logic. Philosophy of Science, 49 (1982) 24–42.

[3] C. Starmer, Developments in Non-Expected Utility Theory: The Hunt for a Descriptive Theory of Choice under Risk. Journal of Economic Literature 38 (2000) 332–382.

[4] I. Gilboa, Theory of Decision Under Uncertainty. Cambridge University Press, 2009.

[5] D.E. Bell, H. Raiffa, A. Tversky (eds.), Decision Making: Descriptive, Normative, and Prescriptive Interactions. Cambridge University Press, Cambridge, 1988.

[6] L.R. Keller, Decision Research with Descriptive, Normative, and Prescriptive Purposes – Some Comments. Annals of Operations Research 19 (1989) 485-487.

[7] J. Chai, J.N.K. Liu, Dominance-based Decision Rules Induction for Multicriteria Ranking. International Journal of Machine Learning and Cybernetics 4 (2013), 427-444.

[8] J. Chai, E.W.T. Ngai, Multi-perspective Strategic Supplier Selection in Uncertain Environments. International Journal of Production Economics 166 (2015) 215-225.

[9] J. Chai, J.N.K. Liu, A Novel Believable Rough Set Approach for Supplier Selection. Expert Systems with Applications 41 (2014) 92-104.

[10] J. Chai, E.W.T. Ngai, J.N.K. Liu, Dynamic Tolerant Skyline Operation for Decision Making. Expert Systems with Applications 41 (2014) 6890-6903.

[11] J. Chai, J.N.K. Liu, E.W.T. Ngai, Application of Decision-making Techniques in Supplier Selection: A Systematic Review of Literature. Expert Systems with Applications 40 (2013) 3872-3885.

[12] J. Chai, E.W.T. Ngai, Decision-Making Techniques in Supplier Selection: Recent Accomplishments and What Lies Ahead, Expert Systems with Applications, in press, 2019.

[13] D. Kahneman, A. Tversky, Prospect Theory: An Analysis of Decision under Risk. Econometrica 47 (1979) 263–291.

[14] M. Allais, Le Comportement de l’Homme Rationnel devant le Risque: Critique des Postulats et Axiomes de l’Ecole Américaine. Econometrica 21 (1953) 503–546.

[15] J. von Neumann, O. Morgenstern, Theory of Games and Economic Behavior. Princeton University Press, Princeton, 1944.

[16] A. Tversky, D. Kahneman, Advances in Prospect Theory: Cumulative Representation of Uncertainty. Journal of Risk and Uncertainty 5 (1992) 297–323.

[17] N. Barberis, Thirty Years of Prospect Theory in Economics: A Review and Assessment. Journal of Economic Perspectives 27 (2013) 173–195.

[18] P.P. Wakker, Prospect Theory: For Risk and Ambiguity. Cambridge University Press, Cambridge, UK, 2010.

[19] D. Arnott, S.J. Gao, Behavioral Economics for Decision Support Systems Researchers. Decision Support Systems, 122 (2019) 1-12.

[20] B. Aviad, G. Roy, A Decision Support Method, based on Bounded Rationality Concepts, to Reveal Feature Saliency in Clustering Problems. Decision Support Systems 54 (2012) 292-303.

[21] P.P. Wakker, D. Deneffe, Eliciting von Neumann-Morgenstern Utilities when Probabilities Are Distorted or Unknown. Management Science 42 (1996) 1131–1150.

[22] M. Abdellaoui, Parameter-Free Elicitation of Utility and Probability Weighting Functions. Management Science 46 (2000) 1497–1512.

[23] H. Bleichrodt, J.L. Pinto, A Parameter-Free Elicitation of the Probability Weighting Function in Medical Decision Analysis. Management Science 46 (2000) 1485–1496.

[24] M. Abdellaoui, F. Vossmann, M. Weber, Choice-Based Elicitation and Decomposition of Decision Weights for Gains and Losses under Uncertainty. Management Science 51 (2005) 1384–1399.

[25] M. Abdellaoui, H. Bleichrodt, C. Paraschiv, Loss Aversion under Prospect Theory: A Parameter-Free Measurement. Management Science 53 (2007) 1659–1674.

[26] G. van de Kuilen, P.P. Wakker, The Midweight Method to Measure Attitudes toward Risk and Ambiguity. Management Science 57 (2011) 582–598.

[27] D. Schmeidler, Subjective Probability and Expected Utility without Additivity. Econometrica 57 (1989) 571-587.

[28] L.J. Savage, The Foundations of Statistics. Wiley, New York. 2nd edn. Dover Publications, New York, 1972.

[29] J. Chai, C. Li, P.P. Wakker, T.V. Wang, J. Yang. Reconciling Savage's and Luce's Modeling of Uncertainty: The Best of Both Worlds. Journal of Mathematical Psychology 75 (2016) 10-18.

[30] G. Choquet, Theory of Capacities. Annales de l'lnstitut Fourier 5 (1953) 131-295.

[31] W.M. Goldstein, H.J. Einhorn, Expression Theory and the Preference Reversal Phenomena. Psychological Review 94 (1987) 236–254.

[32] D. Prelec, The Probability Weighting Function. Econometrica 66 (1998) 497–527.

[33] J.D. Hey, C. Orme, Investigating Generalizations of Expected Utility Theory Using Experimental Data. Econometrica 62 (1994) 1291-1326.

[34] D.W. Harless, C.F. Camerer, The Predictive Utility of Generalized Expected Utility Theories. Econometrica 62 (1994) 1251-1289.

[35] J. Qiu, E.M. Steiger, Understanding the Two Components of Risk Attitudes: An Experimental Analysis. Management Science 57 (2011) 193–199.

[36] J.K. Goeree, C.A. Holt, T.R. Palfrey, Risk Averse Behavior in Generalized Matching Pennies Games.

Games and Economic Behavior 45 (2003) 97-113.

[37] H.P. Stott, Cumulative Prospect Theory’s Functional Menagerie. Journal of Risk and Uncertainty 32 (2006) 101-130.

[38] C.R. Fox, R.A. Poldrack, Prospect Theory on the Brain, in: P.W. Glimcher, E. Fehr (Eds.), Handbook of Neuroeconomics, Elsevier, New York, 2014, pp. 533–567.

[39] R. Gonzalez, G. Wu, On the Shape of the Probability Weighting Function. Cognitive Psychology 38 (1999) 129–166.

[40] S.M. Tom, C.R. Fox, C. Trepel, R.A. Poldrack, The Neural Basis of Loss Aversion in Decision-Making under Risk. Science 315 (2007) 515-518.

[41] T. Tanaka, C.F. Camerer, Q. Nguyen, Risk and Time Preferences: Linking Experimental and Household Survey Data from Vietnam. American Economic Review 100 (2010) 557–571.

[42] O. Toubias, E. Johnson, T. Evgeniou, P. Delquié, Dynamic Experiments for Estimating Preferences: An Adaptive Method of Eliciting Time and Risk Parameters. Management Science 59 (2013) 613–640.

[43] M. Rabin, Risk Aversion and Expected-utility Theory: A Calibration Theorem. Econometrica 68 (2000) 1281–1292.

[44] M. Abdealloui, O. L’Haridon, C. Paraschiv, Experienced vs. Described Uncertainty: Do We Need Two Prospect Theory Specifications? Management Science 57 (2011) 1879–1895.

[45] E. Diecidue, P.P. Wakker, M. Zeelenberg, Eliciting Decision Weights by Adapting de Finetti’s Betting-Odds Method to Prospect Theory. Journal of Risk and Uncertainty 34 (2007) 179–199.

[46] R. Bostic, R.J. Herrnstein, R.D. Luce, The Effect on the Preference Reversal Phenomenon of using Choice Indifferences. Journal of Economic Behavior & Organization 13 (1990) 193-212.

[47] A. Bruhin, H. Fehr-Duda, T. Epper, Risk and Rationality: Uncovering Heterogeneity in Probability Distortion. Econometrica 78 (2010) 1375-1412.

[48] S.J. Kachelmeier, M. Shehata, Examining Risk Preferences Under High Monetary Incentives: Experimental Evidence From the People’s Republic of China. American Economic Review 82 (1992) 1120–1141.

[49] C.K. Hsee, E.U. Weber, Cross-National Differences in Risk Preferences and Lay Predictions. Journal of Behavioral Decision Making 12 (1999) 165–179.

[50] C.A. Holt, S.K. Laury, Risk Aversion and Incentive Effects. American Economic Review 92 (2002) 1644–1655.

[51] R.H. Thaler, Mental Accounting and Consumer Choice. Marketing Science 4 (1985) 199-214.

[52] R.H. Thaler, Mental Accounting Matters. Journal of Behavioral Decision Making 12 (1999) 183–206.

[53] H. Fehr-Duda, A. Bruin, T.F. Epper, R. Schubert, Rationality on the Rise: Why Relative Risk Aversion Increases with Stake Size. Journal of Risk and Uncertainty 40 (2010) 147-180.

[54] A. Tversky, P.P. Wakker, Risk Attitudes and Decision Weights. Econometrica 63 (1995) 1255-1280.

## Biographical Notes:

Dr. Junyi Chai is currently an Assistant Professor in Division of Business Management with Beijing Normal University-Hong Kong Baptist University United International College. Dr. Chai received his Ph.D. from The Hong Kong Polytechnic University. He was a research visitor of Erasmus University Rotterdam, University of Zurich, and National University of Singapore. His research interests include various aspects of Decision Theories and Analytics with their applications in Information and Operations Management. His publications have appeared in international journals including International Journal of Production Economics, Decision Support Systems, Journal of Mathematical Psychology, Expert Systems with Applications, International Journal of Machine Learning and Cybernetics, Industrial Management & Data Systems, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems and others, which have been cited by 1000+ times (Google Scholar) or 500+ times (Web of Science).

Prof. Eric Ngai is an Associate Head and Professor in Information and Operations Management at the Department of Management and Marketing, The Hong Kong Polytechnic University. His current research Chain Management, Decision Support Systems, AI research and Social Media Technology and Applications. He has over 140 refereed international journal publications including MIS Quarterly, Journal of Operations Management, Production & Operations Management, INFORMS Journal on Computing, Decision Support Systems and others.

## Highlights:

1. A novel non-parametric method is proposed to elicit decision weights based on prospect theory.

2. A dynamic mechanism is provided for exhibiting violations of human rationality, measuring individual risk attitudes, and capturing people’s subjective beliefs.

3. This method is considered flexible, tractable, and less cognitively demanding compared with other non-parametric elicitations in the literature.

4. Experimental studies are conducted to verify the proposed method based on a sample of residents of Hong Kong, China.
