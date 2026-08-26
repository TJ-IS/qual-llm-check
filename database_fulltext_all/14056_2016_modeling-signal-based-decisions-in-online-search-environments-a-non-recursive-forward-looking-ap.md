---
otero_id: 14056
otero_key: "XRE9PABD"
title: "Modeling signal-based decisions in online search environments: A non-recursive forward-looking approach"
authors: "Madjid Tavana; Francisco J. Santos-Arteaga; Debora Di Caprio; Kevin Tierney"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2015.10.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling signal-based decisions in online search environments: A non-recursive forward-looking approach

Madjid Tavana <sup>a,b,</sup>\*, Francisco J. Santos-Arteaga <sup>c,f</sup>, Debora Di Caprio <sup>d,e</sup>, Kevin Tierney

<sup>a</sup> Business Systems and Analytics Department, Distinguished Chair of Business Analytics, La Salle University, Philadelphia, PA 19141, USA

<sup>b</sup> Business Information Systems Department, Faculty of Business Administration and Economics, University of Paderborn, D-33098 Paderborn, Germany

<sup>c</sup> Departamento de Economı´a Aplicada II, Facultad de Econo´micas, Universidad Complutense de Madrid, Campus de Somosaguas, 28223 Pozuelo, Spain

<sup>d</sup> Department of Mathematics and Statistics, York University, Toronto M3J 1P3, Canada

<sup>e</sup> Polo Tecnologico IISS G. Galilei, Via Cadorna 14, 39100 Bolzano, Italy

<sup>f</sup> School of Economics and Management, Free University of Bolzano, 39100 Bolzano, Italy

## A R T I C L E I N F O

Article history: Received 18 May 2015 Received in revised form 4 September 2015 Accepted 4 October 2015 Available online 22 October 2015

Keywords: Information acquisition Product improvement Signals Learning Utility theory Sequential search

## A B S T R A C T

Consider a rational decision maker (DM) who must acquire a finite amount of information sequentially online from a set of products. The DM receives signals on the distribution of the product characteristics. Each time an observation is acquired, DMs redefine the probability of improving upon the products observed. The resulting information acquisition process depends on the values of the characteristics observed, the number and potential realizations of the remaining observations, and the type of signal received. We construct two functions determining the information acquisition behavior of DMs and illustrate numerically the importance of the characteristic on which signals are issued.

\- 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

## 1.1. Motivation

The elimination of the uncertainty faced in most real-life decisions and its transformation into risk constitutes one of the main incentives for the design of information acquisition algorithms [13,43,44]. Consider the search problem faced by a decision maker (DM) who must sequentially acquire information on a set of products whose main characteristics are grouped into two differentiated categories. The acquisition of information by rational DMs constitutes a fundamental subject of analysis in a wide array of disciplines, ranging from consumer behavior and economics to psychology, management and operations research.

Each discipline provides its own approach to the problem involving a DM who must generally decide when to stop gathering information based on the last observation acquired and some simplifying (martingale-based) assumptions regarding the value of the potential expected realizations [8].

The standard framework of analysis that both the management and operations research literature build upon considers the introduction of a new technology to the market [35–37,41,58]. The algorithms designed in these papers determine the information acquisition incentives of the DMs and their stopping rules based on the expected value of the next characteristic realized and the information acquisition costs faced by the DM [31,54,58]. The use of standard dynamic programming techniques to illustrate the existence of information acquisition thresholds requires imposing several formal restrictions on the corresponding return functions.

In these models, three important constraints are generally imposed on the algorithms that determine the information acquisition behavior of the DMs, namely,

1. The DM seldom considers recalling previous partially observed products (Shepherd and Levesque [53] are an exception).

2. The information acquisition incentives of the DM do not depend on the number or the potential realizations of the observations remaining to be acquired.

3. The DM does not consider the set of potential improvements that may be realized relative to the products observed previously.

A similar intuition applies to the technology acceptance models based on the subjective perception of the DM when observing different characteristics of a given product [10,23,59]. At the same time, the previous models do not consider the strategic quality inherent to the process of information transmission [9,28,29,47]. In other words, the operations research literature generally overlooks the strategic implications that different signaling strategies regarding the value of unknown technological characteristics have for the information acquisition and choice behavior of the DM.

An important exception is given by the game theoretical branch of the operations research literature [50]. This research area concentrates on the strategic incentives driving the diffusion of technology but does not consider the information acquisition process of the DM when defining his technology adoption decisions. This line of research has been further developed by the economics and the consumer choice literature, which have both formally and empirically described the strategic effect that signals have on the information acquisition and choice incentives of the DM [8,40].

The potential applications of these algorithmic structures lie within the decision support and the consumer choice literature. As in the corresponding theoretical settings, the applications of these information acquisition models rely on simplifying assumptions that allow for the use of dynamic programming techniques to obtain optimal sequential choice policies. These simplifications range from heuristic mechanisms that limit the number of alternatives evaluated by the DM [19] and the elimination of recall [34] to the absence of optimal information acquisition thresholds or analysis of their behavior [5,49,62].

## 1.2. Contribution

The current paper studies the information acquisition behavior of a rational DM who is sequentially gathering n 2 N observations from a set of products whose attributes have been grouped into two differentiated categories. This simplification is applied in several disciplines, which concentrate on a small number of characteristic categories when describing the products available to the DMs. For example:

\- consumer choice analysts utilize quality and preference [30],

\- economists consider performance and cheapness [38], and

\- operations researchers concentrate on variety and quality [6].

The defining quality of our paper relies on the formalization of the information acquisition process of the DM, which will be defined for each observation available on the following criteria:

\- the values of all the characteristics observed previously,

\- the number and potential realizations of all the remaining observations, and

all possible combinations of the potential realizations of the remaining observations and the characteristics observed.

These criteria together prevent the use of standard dynamic programming techniques in the design of the information acquisition algorithm. In particular, the information acquisition incentives of DMs will be based on:

\- the number of observations that remain to be acquired,

\- the potential values of these observations, and

\- the subjective probability that these values allow the DM to observe a product that delivers a higher utility than the best among the ones observed.

These incentives must be redefined each time an observation is acquired, as suggested, for example, by Saad and Russo [51].

Given the value of the realizations observed and the number of observations remaining to be acquired, the information acquisition behavior of the DM will be determined by the following:

\- a continuation function describing the utility that the DM expects to obtain from continuing to acquire information on a partially observed product, and

\- a starting function defining the expected utility the DM expects to obtain from starting to check the characteristics of a new product.

Fig. 1 illustrates the possibility spaces that must be considered by the DM when defining his information acquisition process. The variable x (i = 1, 2) represents the first and the second characteristic of the initial product; x<sup>n</sup> refers to a new second product, while x<sup>nþ1</sup> refers to a new third product. Fig. 1a describes the twoobservation scenario, where the spaces of potential realizations to be considered by the DM are bidimensional. Fig. 1b shows that in the three-observation setting, the DM must consider one threedimensional space versus the union of three different threedimensional spaces. Similarly, in the case with four observations, the DM will have to consider the union of two four-dimensional spaces (when continuing) versus the union of eight different fourdimensional spaces (when starting). This figure highlights the non-recursivity of the information acquisition process analyzed in the current paper.

Fig. 1 also illustrates the increase in the dimensionality of the problem faced by the DM as he considers acquiring additional observations. More precisely, the setting that would result from considering more than three observations cannot be analyzed directly. We synthesize the information acquisition incentives of the DM within two real-valued functions that determine the expected utility derived from the potential use given to the remaining observations. That is, we simplify a problem requiring the analysis of a multiple-dimensional continuous environment into a two-dimensional one, which makes it tractable and allows for a verifiable analysis of the behavior of the DM.

Moreover, firms will be allowed to issue signals on the characteristics defining their products, thus prompting the DM to update his expected search utilities following both Bayesian and subjective learning rules. Each time an observation is acquired, the DM has to modify the probability of improving upon the products already observed with the remaining observations available and also account for the distributional implications derived from the signal.

We will illustrate how the characteristic on which the signals are issued plays a fundamental role in determining the information acquisition incentives of the DM. This will be the case even if the signals are considered reliable by the DM and indicate improvement in one of the characteristics of the product. In particular, issuing signals on the second characteristic may have the opposite effect of that intended by the firm.

Given the number of observations that are expected to be acquired by the DM, our model allows firms to forecast the information acquisition behavior of the DM as well as the probability of having their products inspected and considered for purchase. This possibility introduces an important strategic component, particularly in the formalization of online search environments and the subsequent design of decision support tools to guide the information acquisition process of the DM [1,22,57].

![](/api/attachments/XRE9PABD/fulltext/images/1247cb72e161227cb9ea04f1524943a64fc99589dee14516ce02902b136ef3ab.jpg)  
a. Possibility spaces when the DM can acquire two observations

![](/api/attachments/XRE9PABD/fulltext/images/57977355376bd77e78fb5ab484e302d4e3f7a9eff3e8cac174bfa29c3d09454e.jpg)  
b. Possibility spaces when the DM can acquire three observations  
Fig. 1. Possibility spaces defining the information acquisition process of the DM.

The paper proceeds as follows. Section 2 addresses the standard notation and basic assumptions required to develop the model. Section 3 defines the expected search utility functions within a reference two-observation and three-observation environment. Section 4 introduces signals and the Bayesian learning process in the search utility functions of the DM. Section 5 extends the analysis to a search environment with signals and four observations. Section 6 numerically illustrates the main results. Section 7 describes the sequential information acquisition process of the DM. Section 8 summarizes the main findings and highlights their managerial significance, and Section 9 concludes. An appendix explicitly describes the information acquisition process of the DM when accounting for the signals issued by the firms.

## 2. Basic notations and main assumptions

The main assumptions on which the expected search utilities are built correspond to those described by Di Caprio et al. [14]. To keep the current paper self-contained, we restate them below.

Let X be a nonempty set and  be a preference relation defined on X. A utility function representing a preference relation $\succeq o n X$ is a function $u : X \to R$ such that:

$$
\forall x, \quad y \in X, \quad x \succeq y \Leftrightarrow u (x) \geq u (y)\tag{1}
$$

The symbol $\geq$ will be used to denote the standard partial order on the reals. When $X \subseteq \mathbb { R }$ and  coincides with , we say that u is a utility function on X.

The set of all products will be denoted by G. We let $X _ { 1 }$ and $X _ { 2 }$ represent the sets of all possible variants for the first and second characteristic of a product in $G ,$ respectively. It should be noted that these characteristics can be interpreted as categories composed of different attributes chosen from the taxonomy of the product. The DM evaluates each characteristic numerically after he acquires information on the corresponding attributes of the product. Additionally, $X = X _ { 1 } \times X _ { 2 } ,$ , so that every product in $G$ can be described by a pair $\langle x _ { 1 } , x _ { 2 } \rangle$ i in $X , X _ { i } ,$ with $i = 1 , 2 ,$ , is called the ith characteristic factor space, while X stands for the characteristic space.

We make the following technical assumptions, which will be required to define the expected search utility functions.

Assumption 1. For every $i = 1 , 2 ,$ , there exists an $\alpha _ { i } , \beta _ { i } > 0 ,$ , with $\alpha _ { i } \neq \beta _ { i }$ , such that $\cdot X _ { i } = \left[ \alpha _ { i } , \beta _ { i } \right]$ , where $\alpha _ { i }$ and $\beta _ { i }$ are the minimum and maximum of $X _ { i \cdot } |$

Hence, the set of all products, $G ,$ is identified with a compact and convex subset of $R ^ { 2 }$

Assumption 2. The characteristic space X is endowed with a strict preference relation $\succ . \mathsf { I }$

Assumption 3. There exists a continuous additive utility function u representing  on X such that each one of its components $u _ { i } : X _ { i } \longrightarrow R ,$ with i = 1, 2, is a continuous utility function on $X _ { i \cdot } \mathbf { \overline { { \Pi } } }$

Recall that a utility function $u : X _ { 1 } \times X _ { 2 }  R$ representing a preference relation  on $X _ { 1 } \times X _ { 2 }$ is called additive (Wakker [60]) if there exists u $: X _ { i }  \overline { { R } } ,$ with $i = 1 , 2 ,$ , such that $\forall \langle x _ { 1 } , x _ { 2 } \rangle \in X _ { 1 } \times X _ { 2 }$ $u ( \langle x _ { 1 } , x _ { 2 } \rangle ) = u _ { 1 } ( x _ { 1 } ) + u _ { 2 } ( x _ { 2 } ) .$

The additive separability property of the utility function follows naturally from the sequential information acquisition process of the DMs. We could, however, consider products that require a nonseparable utility representation due to their complementarity among characteristics. In this case, we could interpret the relationship between both types of characteristics in such a way that the second dimension represents the portion of the second characteristic that is not explained by the first one. Thus, each characteristic could also be interpreted as a category encompassing several related properties of a product [56]. As a result, search processes would be defined by observable $( X _ { 1 } )$ and experience $\left( X _ { 2 } \right)$ components, the latter requiring a more detailed inspection of the product to be verified [45].

Assumption 4. For every $i = 1 , 2 , \mu _ { i } : X _ { i } \longrightarrow [ 0 ,$ , 1] is a continuous probability density on $X _ { i } ,$ whose support, the set $\{ x _ { i } \in X _ { i } : \mu _ { i } ( x _ { i } ) \neq 0 \}$ , will be denoted by $S u p p ( \mu _ { i } ) . \mathbf { \equiv }$

The probability densities $\mu _ { 1 }$ and $\mu _ { 2 }$ account for the subjective ‘‘beliefs’’ of the DM. That is, for $i = 1 , 2 , \mu _ { i } ( X _ { i } )$ is the subjective probability that a randomly observed product from G corresponds to an element $x _ { i } \in Y _ { i } \subseteq X _ { i }$ as its ith characteristic. The probability densities $\mu _ { 1 }$ and $\mu _ { 2 }$ are assumed to be independent. However, the information acquisition structure described in this paper allows for subjective correlations to be defined among different characteristics within a given product. Considering a correlated environment would not modify the main theoretical structure built in this paper, although it would lead to different quantitative results from the numerical simulations.

We follow the standard economic theory of choice under uncertainty and assume that the DM elicits the ith certainty equivalent (CE) value induced by $\mu _ { i }$ and $u _ { i }$ as the reference point against which to compare the information collected on the ith characteristic of a given product. Given $i \leq 2 ,$ , the certainty equivalent of $\mu _ { i }$ and $u _ { i } ,$ denoted by $c e _ { i } ,$ is a characteristic in $X _ { i }$ that the DM is indifferent to accept in place of the expected one obtained using $\mu _ { i }$ and $u _ { i \cdot }$ That is, for every $i \leq 2 , c e _ { i } = u _ { i } ^ { - 1 } ( E _ { i } )$ where $E _ { i }$ denotes the expected value of $u _ { i \cdot }$ The existence and uniqueness of the ith certainty equivalent value $c e _ { i }$ are guaranteed by the continuity and strictly increasing nature of $u _ { i } ,$ respectively.

In our theoretical framework, after observing the value of the first characteristic from an initial product, the DM has to decide whether to check the second characteristic from the same product or to check the first characteristic from a new product. In this regard, DMs are tacitly assumed to have a well-defined preference order both within and between characteristics. That ${ \mathrm { i } } s ,$ the first characteristic will be assumed to be more important and, as a result, provide a higher expected utility to the DM than the second one.

## 3. Acquiring observations without signals

In this section, we begin by describing our online search algorithm in the case of two observations without signals. Afterward, we introduce the ‘‘improvement probabilities’’, which are the key to computing the enhanced expected utilities when considering any number of observations. Finally, we discuss the three-observation case as a way of understanding how the improvementprobabilities are implemented in the search algorithm.

## 3.1. The basic case: acquiring two observations without signals

Consider the case where the DM is allowed to acquire two observations. Note that the DM always starts by checking the first characteristic of any product.

We show below that the decision to allocate the second available piece of information depends on two real-valued functions defined on $X _ { 1 }$ . The DM considers the sum $E _ { 1 } + E _ { 2 }$ corresponding to the expected utility values of the pairs $\langle u _ { 1 } , \mu _ { 1 } \rangle$ and $\langle u _ { 2 } , \mu _ { 2 } \rangle$ , as the main reference value when calculating both these functions.

Assume that the DM has already checked the first characteristic from an initial product, $x _ { 1 } ,$ and that he uses his remaining piece of information to observe the second characteristic from this product, $x _ { 2 } .$ Clearly, the expected utility gain over $E _ { 1 } + E _ { 2 }$ varies with the observed value $x _ { 1 } .$ Thus, for every $x _ { 1 } \in X _ { 1 } ,$ , let:

$$
P ^ {+} (x _ {1}) = \{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) > E _ {1} + E _ {2} - u _ {1} (x _ {1}) \}\tag{2}
$$

and

$$
P ^ {-} (x _ {1}) = \{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) \leq E _ {1} + E _ {2} - u _ {1} (x _ {1}) \}\tag{3}
$$

$P ^ { + } ( x _ { 1 } )$ and $P ^ { - } ( x _ { 1 } )$ define the set of values x from the initial product such that their combination with $x _ { 1 }$ delivers a higher or lower equal utility, respectively, than a randomly chosen product from $G .$

Let $F \colon X _ { 1 } \to R$ be defined by:

$$
\begin{array}{l} F (x _ {1}) \stackrel {{\text { def }}} {{=}} \int_ {P ^ {+} (x _ {1})} \mu_ {2} (x _ {2}) (u _ {1} (x _ {1}) + u _ {2} (x _ {2})) d x _ {2} \\ \qquad + \int_ {P ^ {-} (x _ {1})} \mu_ {2} (x _ {2}) (E _ {1} + E _ {2}) d x _ {2} \end{array}\tag{4}
$$

$F ( x _ { 1 } )$ describes the DM’s expected utility derived from checking the second characteristic of the initial product after observing that the value of its first characteristic is given by $x _ { 1 }$ . Note that if $u _ { 1 } ( x _ { 1 } ) + u _ { 2 } ( x _ { 2 } ) \leq E _ { 1 } + E _ { 2 } ,$ , then choosing a product from G randomly delivers an expected utility of $E _ { 1 } + E _ { 2 }$ to the DM, which is higher than the utility obtained from choosing the initially observed product, which is $u _ { 1 } ( x _ { 1 } ) + u _ { 2 } ( x _ { 2 } )$

Now consider the expected utility that the DM could gain over the initial (partially observed) product if the second piece of information is used to observe the first characteristic from a different product $\mathbf { \nabla } _ { x _ { 1 } ^ { n } } .$ . For every $x _ { 1 } \in X _ { 1 }$ , define $H : X _ { 1 } \to R$ as follows:

$$
H (x _ {1}) \stackrel {\text { def }} {=} (u _ {1} (x _ {1}) + E _ {2}) + C\tag{5}
$$

with

$$
C \stackrel {d e f} {=} \mu_ {1} (x _ {1} ^ {n} \leq x _ {1}) (E _ {1} + E _ {2}) + \mu_ {1} (x _ {1} ^ {n} > x _ {1}) (u _ {1} (x _ {1} ^ {n}) + E _ {2})\tag{6}
$$

$H ( x _ { 1 } )$ describes the expected utility derived from checking the first characteristic of a new product after observing $x _ { 1 } . \operatorname { I f } x _ { 1 } ^ { n } { \leq } x _ { 1 }$ , the new product observed by the DM does not deliver a higher utility than the initial one, and the payoff obtained from such an event is set equal to $E _ { 1 } + E _ { 2 } .$ . This reference value has been chosen to generate a similar payoff environment to the one defined by the function $F ( x _ { 1 } ) .$

Note, however, that the payoffs assigned to the outcomes $x _ { 1 } > x _ { 1 } ^ { n } \geq c e _ { 1 }$ and $c e _ { 1 } > x _ { 1 } ^ { n } > x _ { 1 }$ within C may seem counterintuitive. In the former case, the new observation is located above the CE value but does not improve upon the initial product, leading to a payoff of $E _ { 1 } + E _ { 2 } . A$ similar intuition applies when considering the latter case, with the new observation located below the CE value but its expected utility accounted for as a payoff (because x<sup>n</sup> $> x _ { 1 } )$

The current approach to the information acquisition behavior of DMs considers only potential improvements relative to the initial reference product, whose value is determined by $x _ { 1 } .$ In this case, the function $F ( x _ { 1 } )$ completely eliminates any uncertainty regarding the initial product, while DMs only observe the initial product partially within $H ( x _ { 1 } )$

However, the function $H ( \cdot )$ allows for an additional product to be observed relative to $F ( \cdot ) .$ . This observational advantage distorts the incentives of DMs when a small number of observations are considered. Larger amounts of observations thus eliminate the resulting effect, as intuition prescribes and the numerical simulations will illustrate.

To account for the set of potential improvements based on the number of remaining observations, we rewrite the expression for C within $H ( x _ { 1 } )$ in the following way:

$$
C = \psi_ {1} (1, 0, \mu_ {1}) (E _ {1} + E _ {2}) + \psi_ {1} (1, 1, \mu_ {1}) (u _ {1} (x _ {1} ^ {n}) + E _ {2})\tag{7}
$$

where $\psi _ { 1 }$ stands for the binomial distribution that will be introduced in the following section.

Finally, note that the expected utilities F and H determine the information acquisition behavior of the DM. That is, after observing $x _ { 1 } ,$ , the DM will either continue acquiring information on the initial product or start acquiring information on a new one depending on whether the function F or H takes the highest value at x . It can also be that $F ( x _ { 1 } ^ { * } ) = H ( x _ { 1 } ^ { * } )$ at a given $x _ { 1 } ^ { * } \in X _ { 1 }$ ; that is, the DM is indifferent between continuing with the initial product and starting a new one. These $x _ { 1 } ^ { * }$ values behave as information acquisition thresholds that partition $X _ { 1 }$ into subintervals whose values induce the DM to either continue acquiring information on the initial product or to switch and start checking a new one.

## 3.2. Potential improvement probabilities

The information acquisition setting with bidimensional products and two observations described in the previous section has been extensively analyzed by Di Caprio and Santos Arteaga [11], Di Caprio et al. [14] and Tavana et al. [56]. It provides a useful set of guidelines in environments with information-constrained DMs as well as the basic framework on which to add sophistication to the assimilation capacities of the DM. We remain constrained within a bidimensional product environment but require the DM to be sophisticated enough to forecast the expected improvements that may arise from any of the remaining observations available. These improvements are relative to a given reference product whose value may change as additional information is acquired.

A general formulation will be sketched after introducing two intuitivesettings with three and four observations. Before describing these settings, we must define the forecasting capacities of the DM.

A binomial distribution determined by the number of observations remaining to be acquired by the DM will be used to define his sequential dynamic behavior. The probability that l among the remaining n observations improve upon the observed characteristic $x _ { 1 }$ and deliver an expected product better than the one that has been partially observed is given by the following binomial distribution:

$$
\psi_ {1} (n, l, \mu_ {1} (x _ {1} ^ {n} > x _ {1})) = \binom {n} {l} \mu_ {1} (x _ {1} ^ {n} > x _ {1}) ^ {l} (1 - \mu_ {1} (x _ {1} ^ {n} > x _ {1})) ^ {n - l}\tag{8}
$$

where $\mu _ { 1 } ( x _ { 1 } ^ { n } > x _ { 1 } )$ is the probability that a new randomly selected product is endowed with a better first characteristic than the currently observed one, which is endowed with $x _ { 1 } .$

Similarly, when the second characteristic is considered, all possible combinations delivering an improvement over the initial partially observed product should be accounted for by:

$$
\begin{array}{l} \psi_ {2} (n, l, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1}))) \\ = \binom {n} {l} \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1})) ^ {l} (1 - \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1}))) ^ {n - l} \end{array}\tag{9}
$$

where $\mu _ { 2 } ( x _ { 2 } ^ { n } \in P ^ { + } ( x _ { 1 } ) )$ is the probability that a new, randomly selected product has a second characteristic belonging to the set $P ^ { + } ( x _ { 1 } )$ determined by the observed $x _ { 1 }$ realization.

The combination of $\psi _ { 1 } ( n , l , \mu _ { 1 } ( x _ { 1 } ^ { n } > x _ { 1 } ) )$ and $\psi _ { 2 } ( n , l , \mu _ { 2 }$ $( x _ { 2 } ^ { n } \in P ^ { + } ( x _ { 1 } ) ) ,$ Þ determines the probability that a randomly selected product is endowed with an expected set of $\mathrm { { \dot { X } } } _ { 1 }$ and $X _ { 2 }$ characteristics that are better than the partially observed product defined by $( x _ { 1 }$ $P ^ { + } ( x _ { 1 } ) )$ ).

To simplify the notation, we will refer to both these binomials by $\psi _ { 1 } ( n , l , \mu _ { 1 } )$ and $\psi _ { 2 } ( n , l , \mu _ { 2 } ) ,$ , respectively, while accounting for the corresponding values of n and l.

## 3.3. Acquiring three observations without signals

We now introduce the information acquisition scenario with three observations to provide some basic intuition on the sequential structure of the decisions faced by the DM.

Consider the information acquisition problem faced by a DM after having gathered the first observation from an initial product, given by x , when a total of three observations can be acquired. In this case, the DM must calculate two enhanced versions of the original functions $F ( x _ { 1 } )$ and $H ( x _ { 1 } )$ . These new functions must account for the two observations left to be acquired by the DM and the probability that such observations provide a product that is better than the initially observed one, which will be used throughout this section and the following one as the main reference value. When calculating the enhanced function $F ( x _ { 1 } )$ , we must account for the fact that the DM uses the second piece of information available to acquire $x _ { 2 }$ and observe the initial product fully, i.e., the DM observes $( x _ { 1 } , x _ { 2 } )$ . As a result, the payoff obtained by the DM depends on the expected realization of $x _ { 2 }$ and that of $x _ { 1 } ^ { n } ,$ i.e., the first characteristic from the new product observed, with the following combinations being considered regarding the third and final observation:

(1-0) This option corresponds to the subcase defined by the $\psi _ { 1 } ( 1$ $0 , \ \mu _ { 1 } )$ binomial probability. It implies that after fully observing the initial product, the final observation x<sup>n</sup> does not provide a characteristic higher than $x _ { 1 } .$ . As a result, because the final observation does not improve upon the initial one and the DM has not yet observed $x _ { 2 } ,$ the expected outcome following from this event is defined by the CE product: $\psi _ { 1 } ( 1 , 0 , \mu _ { 1 } ) ( E _ { 1 } + E _ { 2 } )$ . That is, the default payoff derived from an unsuccessful search is assumed to be given by the CE product.

(1-1) This option corresponds to the subcase defined by the $\psi _ { 1 } ( 1 ,$ 1, $\mu _ { 1 } )$ binomial probability. It implies that after fully observing the initial product, the final observation $x _ { 1 } ^ { n }$ provides a characteristic higher than $x _ { 1 } .$ . As a result, because the final observation improves upon the initial one and the DM has not yet observed $x _ { 2 } ,$ the expected outcome following from this event is given by: $\psi _ { 1 } ( 1 , 1 , \mu _ { 1 } ) ( u _ { 1 } ( x _ { 1 } ^ { n } ) + E _ { 2 } )$

When defining the enhanced version of function $H ( x _ { 1 } ) .$ , we must account for the fact that the DM has one more observation left to acquire than in the $F ( x _ { 1 } )$ setting, as the second observation has not been used to acquire x . Thus, the sets of possible combinations that must be considered when defining the enhanced versions of function $H ( x _ { 1 } )$ always include one observation more than those defining the enhanced $F ( x _ { 1 } )$ setting. The following combinations arise from the set of two observations that the DM has left to acquire in this case, with the notation describing the same type of sequential pattern as the one introduced in the subcases above.

(2-0) This option implies that none of the two observations left provides a $1 x _ { 1 } ^ { n } > x _ { 1 }$ . Therefore, the expected outcome following from this event is defined by the certainty equivalent product: $\psi _ { 1 } ( 2 , 0 , \mu _ { 1 } ) ( E _ { 1 } + E _ { 2 } )$

(2-1) This option implies that only one of the two observations left provides a $x _ { 1 } ^ { n } > x _ { 1 }$ . It also implies that the observation leading to $x _ { 1 } ^ { n } > x _ { 1 }$ must be the second one. That ${ \mathrm { i } } s ,$ if the observation providing $x _ { 1 } ^ { n } > x _ { 1 }$ had been the first one, the second observation would have been used by the DM to acquire $x _ { 2 } ^ { n } ,$ , leading to the (1-1) subcase described below. Thus, the DM ends up with a partially observed product $( x _ { 1 } ^ { n } , c e _ { 2 } )$ . The resulting expected payoff is therefore given by: $\bar { \psi _ { 1 } } ( 2 , 1 , \mu _ { 1 } ) ( u _ { 1 } ( x _ { 1 } ^ { n } ) + E _ { 2 } )$

(1-1) This option implies that the first observation acquired leads to a characteristic $x _ { 1 } ^ { n } > x _ { 1 }$ , which allows the DM to use the remaining observation to acquire $x _ { 2 } ^ { n } ,$ i.e., the second characteristic from the new product observed. This is trivially the optimal way to proceed because $x _ { 1 } ^ { n } > x _ { 1 }$ and all second characteristics are equally distributed. Note that the set of possible outcomes derived from observing x<sup>n</sup> is defined by (1–0) and (1–1).

$$
\begin{array}{l} \text { The   resulting   expected   payoff   is   therefore   given   by: } \psi_ {1} \\ (1, 1, \mu_ {1}) [ \psi_ {2} (1, 1, \mu_ {2}) (u _ {1} (x _ {1} ^ {n}) + u _ {2} (x _ {2} ^ {n})) + \psi_ {2} (1, 0, \mu_ {2}) \\ (E _ {1} + E _ {2}) ]. \end{array}
$$

The basic reference product upon which the DM is expected to improve as a result of the information acquisition process is given by $( x _ { 1 } , P ^ { + } ( x _ { 1 } ) )$ . That is, the characteristic initially observed determines the reference point on which the information acquisition process is based. The consequences for the information acquisition process of DMs will become evident below, as we describe the different sections that compose the algorithm. The intuitive explanation for this assumption may range from framing effects together with optimism or pessimism on the side of the DMs [27] to subjective motivations based on the value of the information being acquired [52]. Moreover, when acquiring three or more observations, shifting the reference points to the CE product implies forcing the DM to ignore combinations of products that could potentially improve upon the CE product.

We are now able to write an expression for the functions $F ( x _ { 1 } )$ and $H ( x _ { 1 } )$ in a setting with three observations. We will denote these functions by $F ( x _ { 1 } | 3 )$ and $H ( x _ { 1 } | 3 )$ , respectively.

$$
\begin{array}{l} F (x _ {1} | 3) \stackrel {{d e f}} {{=}} \int_ {P ^ {+} (x _ {1})} \mu_ {2} (x _ {2}) (u _ {1} (x _ {1}) + u _ {2} (x _ {2})) d x _ {2} + A \\ \qquad + \int_ {P ^ {-} (x _ {1})} \mu_ {2} (x _ {2}) (E _ {1} + E _ {2}) d x _ {2} + B \end{array}\tag{10}
$$

where

$$
\begin{array}{c} A = \int_ {P ^ {+} (x _ {1})} \mu_ {2} (x _ {2}) [ \psi_ {1} (1, 0, \mu_ {1}) (E _ {1} + E _ {2}) \\ + + \psi_ {1} (1, 1, \mu_ {1}) (u _ {1} (x _ {1} ^ {n}) + E _ {2}) ] d x _ {2} \end{array}\tag{11}
$$

$$
\begin{array}{l} B = \int_ {P ^ {-} (x _ {1})} \mu_ {2} (x _ {2}) [ \psi_ {1} (1, 0, \mu_ {1}) (E _ {1} + E _ {2}) \\ \quad + \psi_ {1} (1, 1, \mu_ {1}) (u _ {1} (x _ {1} ^ {n}) + E _ {2}) ] d x _ {2} \end{array}\tag{12}
$$

The reference value framework assumed in the current section implies that the set of acceptable expected outcomes within B relates directly to the potential realizations of $x _ { 2 } \in P ^ { + } ( x _ { 1 } )$ . That is, the realizations of the second characteristic from the initial product have a reference effect on the resulting expected payoffs derived from the posterior observations calculated within both A and B. As we will see later, the current framework makes more intuitive sense as the number of observations increases. This is the case even though it may seem intuitively correct to define the expected improvements to be achieved relative to the CE product, that is, with the new characteristic x<sup>n</sup> being located above the $c e _ { 1 }$ value and the corresponding $P ^ { + } ( x _ { 1 } ^ { n } )$ set requiring that $x _ { 2 } ^ { n } > c e _ { 2 }$ when added to $x _ { 1 } ^ { n } .$ The requirements, $x _ { 1 } > c e _ { 1 }$ and $x _ { 2 } ^ { n } > c e _ { 2 }$ , also imply that many potential combinations of characteristics that lead to expected products with a higher utility than that of the CE product would be eliminated. Clearly, in a sequential information acquisition setting, as the DM observes products leading to a higher utility than that of the CE product, the highest among these products will be used as the reference on which improvements must be defined. We return to this topic later in the paper. Now consider the function $H ( x _ { 1 } | 3 )$

$$
H (x _ {1} | 3) \stackrel {\text { def }} {=} (u _ {1} (x _ {1}) + E _ {2}) + C\tag{13}
$$

where

$$
\begin{array}{l} C = \psi_ {1} (2, 0, \mu_ {1}) (E _ {1} + E _ {2}) + \psi_ {1} (2, 1, \mu_ {1}) (u _ {1} (x _ {1} ^ {n}) + E _ {2}) \\ \quad + \psi_ {1} (1, 1, \mu_ {1}) [ \psi_ {2} (1, 1, \mu_ {2}) (u _ {1} (x _ {1} ^ {n}) + u _ {2} (x _ {2} ^ {n})) \\ \quad + \psi_ {2} (1, 0, \mu_ {2}) (E _ {1} + E _ {2}) ] \end{array}\tag{14}
$$

Note that in the function $H ( x _ { 1 } | 3 )$ , the improvements must be calculated with respect to the partially observed product defined by $x _ { 1 } .$ . The additional observation available to the DM modifies the set of potential improvements when compared to the function $F ( x _ { 1 } | 3 )$ . The latter function is based on the weighted average that follows from the expected realizations of $x _ { 2 }$ and the corresponding $P ^ { + } ( x _ { 1 } )$ sets. Here, improvements are based on a new observed product calculated with respect to the set $P ^ { + } ( x _ { 1 } )$ defined by the partially observed first product absent any potential $x _ { 2 }$ realization.

## 4. Signals and learning

## 4.1. Basic intuition

As already stated in the introduction, we will consider a uniform density function when defining the subjective beliefs of the DM. In addition to providing a simpler formal framework, the uniform density reflects the total uncertainty and maximum entropy faced by the DM when acquiring information [55]. The analysis can be performed using any other continuous probability function, but the main results obtained relating to the different signal effects between $X _ { 1 }$ and $X _ { 2 }$ would remain unchanged.

The initial density function considered by the DM is therefore given by:

$$
\mu_ {i} (x _ {i}) = \left\{ \begin{array}{l l} \frac {1}{\beta_ {i} - \alpha_ {i}} & \text { if } x _ {i} \in [ \alpha_ {i}, \beta_ {i} ] \\ 0 & \text { otherwise } \end{array} \right.\tag{15}
$$

for $i = 1 , 2 .$ . We assume that receiving a credible positive signal implies that a percentage g of the probability mass accumulated on the lower half of the distribution is shifted to the upper half. The corresponding conditional density function is given by:

$$
\pi (\theta , \gamma | x _ {i}) = \left\{ \begin{array}{l l} \frac {1}{(\beta_ {i} - \alpha_ {i})} + \gamma \frac {1}{(\beta_ {i} - \alpha_ {i})} = \frac {1 + \gamma}{(\beta_ {i} - \alpha_ {i})} & \text { if } x _ {i} \in \left(\frac {\alpha_ {i} + \beta_ {i}}{2}, \beta_ {i} \right] \\ \frac {1}{(\beta_ {i} - \alpha_ {i})} - \gamma \frac {1}{(\beta_ {i} - \alpha_ {i})} = \frac {1 - \gamma}{(\beta_ {i} - \alpha_ {i})} & \text { if } x _ {i} \in \left[ \alpha_ {i}, \frac {\alpha_ {i} + \beta_ {i}}{2} \right] \end{array} \right.\tag{16}
$$

After receiving a positive signal, rational DMs update their initial beliefs, given by $\mu _ { i } ( x _ { i } ) .$ , following Bayes’ rule. Therefore, if a signal u is received, the updated beliefs of the DM will be given by:

$$
\mu_ {i} (x _ {i} | \theta) = \frac {\pi (\theta , \gamma | x _ {i}) \mu_ {i} (x _ {i})}{\int_ {X _ {i}} \pi (\theta , \gamma | x _ {i}) \mu_ {i} (x _ {i}) d x _ {i}}\tag{17}
$$

It may seem intuitively appealing to assume that positive signals generating first-order stochastic dominant beliefs lead to higher expected utility levels for all possible $X _ { 1 }$ values. We will show numerically that this is not necessarily the case. Moreover, even if this were the case, signals will shift the respective threshold values between the search utilities toward higher or lower $x _ { 1 }$ realizations depending on the characteristic on which they are issued.

The belief functions defined above will be used to determine the probability that l among the n remaining observations deliver a better product than the one observed, which is given by the following binomial distribution:

$$
\psi_ {i} (n, l, \mu_ {i} (x _ {i} | \theta)) = \binom {n} {l} \mu_ {i} (x _ {i} | \theta) ^ {l} (1 - \mu_ {i} (x _ {i} | \theta)) ^ {n - l}\tag{18}
$$

## 4.2. Updating the potential improvement probabilities

To add intuition to the presentation, we will assume that $\gamma = 1 /$ 2. Thus, the DM knows that if a signal u is received, the probability of observing a characteristic from the upper half of X , with $i = 1 , 2 ,$ is twice that of observing one from the lower half. Initially, we have that:

$$
\pi (\theta | x _ {i}) = \left\{ \begin{array}{l l} \frac {3}{2 (\beta_ {i} - \alpha_ {i})} & \text { if } x _ {i} \in \left(\frac {\alpha_ {i} + \beta_ {i}}{2}, \beta_ {i} \right] \\ \frac {1}{2 (\beta_ {i} - \alpha_ {i})} & \text { if } x _ {i} \in \left[ \alpha_ {i}, \frac {\alpha_ {i} + \beta_ {i}}{2} \right] \end{array} \right.\tag{19}
$$

with $i = 1 , 2$ . The conditional density $\pi ( \theta | x _ { i } )$ that results from the signal received is presented in Fig. 2.

As a result, after performing the corresponding Bayesian update, the DM accounts for the signals received either on the first or the second characteristic as follows:

$$
\mu_ {i} (x _ {i} | \theta) = \frac {\pi (\theta | x _ {i}) \mu_ {i} (x _ {i})}{\int_ {X _ {i}} \pi (\theta | x _ {i}) \mu_ {i} (x _ {i}) d x _ {i}}\tag{20}
$$

where $i = 1 , 2 .$ . These probabilities will be used to define the weights determining the initial A and B terms within the corresponding function F. Moreover, as explained above, these are the probabilities used to define the binomial improvements based on the initial observed realization $x _ { 1 } .$ . However, these probabilities must be adapted by the DM to compute the product expected to be obtained from the potential improvements that may be achieved over the initial partially observed product. Together with the first realization observed, the DM knows that half the probability mass from the realizations located on the lower half has been shifted to those on the upper half. The DM must consider both the value of $x _ { 1 }$ and the resulting truncated distribution when calculating the expected product that may be obtained after a given number of observations. We describe this updating process in the next subsection.

## 4.3. Updating the expected search products

The probabilities incorporated into the search equation after signals are received for either $X _ { 1 }$ or $X _ { 2 }$ must be based on the first characteristic observed, $x _ { 1 } ,$ and the resulting potential improvements over the corresponding updated CE products. Moreover, the probability improvements over $x _ { 1 }$ and the corresponding set $P ^ { + } ( x _ { 1 } )$ should depend on which one is the characteristic being signaled, as they are generally defined over different domains. For example, in the $X _ { 1 }$ case, the signal divides the domain into two intervals that are given by $[ x _ { 1 } , c e _ { 1 } ]$ and $[ c e _ { 1 } , \beta _ { 1 } ]$ . We explain below how the DM shifts the probability densities that define the corresponding expected search products. Adjusting the interval limits when signals are received on $X _ { 2 }$ allows the same analysis to be performed.

When calculating the corresponding subjective probabilities, note that the density on which the issued signal is based is given by $\pi ( \theta | x _ { i } )$ with i = 1, 2. Consider a given $x _ { 1 } \in X _ { 1 }$ realization. To simplify the notation, assume that the initial realization observed by the DM is given by $x \in X _ { 1 }$ . When computing the new updated densities necessary to calculate the expected value of the product observed, the DM knows that the density of the lower half of the distribution is given by $( 1 / ( 2 ( \beta _ { 1 } - x ) ) )$ ) and that this density is defined over the domain $[ x , \ ( ( \alpha _ { 1 } + \beta _ { 1 } ) / 2 ) ]$ . This equation also defines the probability mass that is shifted to the upper side of the distribution, which is:

$$
\int_ {x} ^ {((\alpha_ {1} + \beta_ {1}) / 2)} \frac {1}{2 (\beta_ {1} - x)} d X _ {1} = \frac {((\alpha_ {1} + \beta_ {1}) / 2) - x}{2 (\beta_ {1} - x)}\tag{21}
$$

Note now that to calculate the density of each point located on the upper side of the domain $[ ( ( \alpha _ { 1 } + \beta _ { 1 } ) / 2 ) , \beta _ { 1 } ]$ , we have to divide the entire mass of the upper part uniformly over all the values within its domain. The probability mass located on the upper side of the distribution is given by $\frac { ( ( \beta _ { 1 } - \alpha _ { 1 } ) / 2 ) } { \beta _ { 1 } - x } + \frac { ( ( \alpha _ { 1 } + \beta _ { 1 } ) / 2 ) - x } { 2 ( \beta _ { 1 } - x ) } ,$ where the second part of this expression is the density mass shifted to the upper side of the distribution depending on the value of the $x \in X _ { 1 }$ realization observed by the DM.

![](/api/attachments/XRE9PABD/fulltext/images/b8b27dcbd6621ed105651bef405ff944da0df47f9455603bb86011c3278c0297.jpg)

![](/api/attachments/XRE9PABD/fulltext/images/f5f20cffd0b08e61ef6ccdd5a3a8b269c5d696587632c0c1bf3add0bc2bde090.jpg)  
b. Conditional density after observing the signal  
Fig. 2. The conditional density p(u|x ) as a result of the signal u.

We denote with $s _ { 1 }$ the probability mass of each of the points located in the upper domain of the density. Therefore, the following equation must hold for each one of these points:

$$
\int_ {((\alpha_ {1} + \beta_ {1}) / 2)} ^ {\beta_ {1}} s _ {1} d X _ {1} = \frac {((\beta_ {1} - \alpha_ {1}) / 2)}{\beta_ {1} - x} + \frac {((\alpha_ {1} + \beta_ {1}) / 2) - x}{2 (\beta_ {1} - x)}\tag{22}
$$

which solves for:

$$
s _ {1} = \frac {1}{\beta_ {1} - x} + \frac {\left(\left(\alpha_ {1} + \beta_ {1}\right) / 2\right) - x}{2 \left(\beta_ {1} - x\right) \left[ \beta_ {1} - \left(\left(\alpha_ {1} + \beta_ {1}\right) / 2\right) \right]}\tag{23}
$$

The process determining the shift in the probability mass between domain intervals is summarized in Fig. 3 below.

Consider, for example, the domains that will be assumed through the numerical simulations for $X _ { 1 } = [ 5 , 1 0 ]$ and $X _ { 2 } = [ 0 , 1 0 ]$ The above process leads to the following densities subjectively defined by the DMs based on the intervals where the domain is located. These densities will be used to calculate the improved product that is expected to be obtained by the information acquisition process. Note that within a uniform setting and a risk neutral environment with $u _ { i } ( x _ { i } ) = x _ { i } ,$ such as those assumed throughout this paper, we have that $c e _ { i } = ( \alpha _ { i } + \beta _ { i } ) / 2$ , for $i = 1 , 2 .$

If the signals are issued on $X _ { 1 } ,$ the DM must consider two possible cases. If $x \geq c e _ { 1 }$ , then:

$$
\xi (x _ {1} | \pi (\theta | x _ {1})) = \frac {1}{\beta_ {1} - x} \text {   for   } x _ {1} \in (x, \beta_ {1} ]\tag{24}
$$

$$
\xi (x _ {2} | \pi (\theta | x _ {1})) = \frac {1}{\beta_ {2} - c e _ {1 | \theta} - c e _ {2} + x} \text {   for   } x _ {2} \in (c e _ {1 | \theta} + c e _ {2} - x, \beta_ {2} ]\tag{25}
$$

![](/api/attachments/XRE9PABD/fulltext/images/b2f96e8cfe4565238ae6c47ce8f7a12ed0306c5f0becc2ab4614bed4c7ffbb0b.jpg)  
a. Initial uniform density function after observing x

![](/api/attachments/XRE9PABD/fulltext/images/6a582abcfbcd76ddb5bc8f9173267c717d88215d949b6676db28da4fa71456b0.jpg)  
b. Subjective density function after observing x  
Fig. 3. Subjective probability mass shift based on the realization x.

If $x < c e _ { 1 }$ then:

$$
\xi \left(x _ {1} \mid \pi (\theta \mid x _ {1})\right) = \left\{ \begin{array}{l l} \frac {1}{\beta_ {1} - x} + \frac {\left(\left(\alpha_ {1} + \beta_ {1}\right) / 2\right) - x}{2 \left(\beta_ {1} - x\right) \left[ \beta_ {1} - \left(\left(\alpha_ {1} + \beta_ {1}\right) / 2\right) \right]} & \text { if } x _ {1} \in \left(c e _ {1}, \beta_ {1} \right] \\ \frac {1}{2 \left(\beta_ {1} - x\right)} & \text { if } x _ {1} \in [ x, c e _ {1} ] \end{array} \right.\tag{26}
$$

while the distribution on $X _ { 2 }$ remains identical to the $\xi ( x _ { 2 } | \pi ( \theta | x _ { 1 } ) )$ just described. The variables $c e _ { i | \theta } ,$ with $i = 1 , 2$ , denote the CE value of the i-th characteristic after a signal is received regarding their distributions.

If the signals are issued on $X _ { 2 } ,$ , the DM must also consider two possible cases. I $x \geq c e _ { 1 } + c e _ { 2 | \theta } - c e _ { 2 }$ , then:

$$
\xi (x _ {1} | \pi (\theta | x _ {2})) = \frac {1}{\beta_ {1} - x} \text {   for   } x _ {1} \in (x, \beta_ {1} ]\tag{27}
$$

variety of qualitative results determining the relative strength of the shifts observed in the functions F and H. In this regard, the effects of optimism or pessimism regarding the expected utility derived from the potential product improvements can be easily analyzed within the current framework.

The reallocation of probability if more than one improved product is observed has been performed according to the following equations, where all the expressions have been simplified to a common denominator.

If the signals are issued on $X _ { 1 }$ , the DM must consider the following cases:

If $x \geq c e _ { 1 }$ , then:

$$
\xi (x _ {1} | \pi (\theta | x _ {1})) = \left\{ \begin{array}{l l} \frac {(1 + (n / 1 0 0))}{\beta_ {1} - x} & \text { if } x _ {1} \in \left(\frac {\beta_ {1} + x}{2}, \beta_ {1} \right] \\ \frac {(1 - (n / 1 0 0))}{\beta_ {1} - x} & \text { if } x _ {1} \in \left[ x, \frac {\beta_ {1} + x}{2} \right] \end{array} \right.\tag{31}
$$

$$
\xi (x _ {2} | \pi (\theta | x _ {2})) = \left\{ \begin{array}{l l} \frac {1}{\beta_ {2} - x} + \frac {((\alpha_ {2} + \beta_ {2}) / 2) - x}{2 (\beta_ {2} - x) [ \beta_ {2} - ((\alpha_ {2} + \beta_ {2}) / 2) ]} & \text { if } x _ {2} \in (c e _ {2}, \beta_ {2} ] \\ \frac {1}{2 (\beta_ {2} - x)} & \text { if } x _ {2} \in [ c e _ {1} + c e _ {2 | \theta} - x, c e _ {2} ] \end{array} \right.\tag{28}
$$

$$
\xi (x _ {2} | \pi (\theta | x _ {1})) = \left\{ \begin{array}{l l} \frac {(1 + (n / 1 0 0))}{\beta_ {2} - c e _ {1 | \theta} - c e _ {2} + x} & \text { if } x _ {2} \in \left(\frac {\beta_ {2} + c e _ {1 | \theta} + c e _ {2} - x}{2}, \beta_ {2} \right] \\ \frac {(1 - (n / 1 0 0))}{\beta_ {2} - c e _ {1 | \theta} + c e _ {2} + x} & \text { if } x _ {1} \in \left[ c e _ {1 | \theta} + c e _ {2} - x, \frac {\beta_ {2} + c e _ {1 | \theta} + c e _ {2} - x}{2} \right] \end{array} \right.\tag{32}
$$

If $x < c e _ { 1 }$ , then

$$
\xi (x _ {1} | \pi (\theta | x _ {1})) = \left\{ \begin{array}{l l} \left[ \frac {1}{\beta_ {1} - x} + \frac {((\alpha_ {1} + \beta_ {1}) / 2) - x}{2 (\beta_ {1} - x) [ \beta_ {1} - ((\alpha_ {1} + \beta_ {1}) / 2) ]} + \frac {n / 1 0 0}{2 (\beta_ {1} - x)} \right] \left(1 + \frac {n}{1 0 0}\right) & \text {if} x _ {1} \in \left(\frac {\beta_ {1} + x}{2}, \beta_ {1} \right] \\ \left[ \frac {1}{\beta_ {1} - x} + \frac {((\alpha_ {1} + \beta_ {1}) / 2) - x}{2 (\beta_ {1} - x) [ \beta_ {1} - ((\alpha_ {1} + \beta_ {1}) / 2) ]} + \frac {n / 1 0 0}{2 (\beta_ {1}} - x) \right] \left(1 - \frac {n}{1 0 0}\right) & \text {if} x _ {1} \in \left(c e _ {1}, \frac {\beta_ {1} + x}{2} \right] \\ \frac {(1 - (n / 1 0 0))}{2 (\beta_ {1} - x)} & \text {if} x _ {1} \in [ x, c e _ {1} ] \end{array} \right.\tag{33}
$$

If $x < c e _ { 1 } + c e _ { 2 | \theta } - c e _ { 2 } ,$ , then:

$$
\begin{array}{l} \xi (x _ {1} | \pi (\theta | x _ {2})) = \frac {1}{\beta_ {1} - x} \text {for} x _ {1} \in (x, \beta_ {1} ] \\ \xi (x _ {2} | \pi (\theta | x _ {2})) = \frac {1}{\beta_ {2} - c e _ {1} - c e _ {2 | \theta} + x} \text {for} x _ {2} \in (c e _ {1} + c e _ {2 | \theta} - x, \beta_ {2} ] \end{array}\tag{29}
$$

(30)

Finally, we allow for an additional reallocation of densities between both intervals when more than one improved product is expected to be observed through the information acquisition process of the DM. That is, being able to observe more than one improved product should provide the DM with a different expected payoff, in this case one that is higher than observing a unique one.

We have accounted for this effect in a subjective manner. We are aware of the fact that different reallocation processes lead to a

The distribution on $X _ { 2 }$ remains identical to the $\xi ( x _ { 2 } | \pi ( \theta | x _ { 1 } ) )$ just described for $x \geq c e _ { 1 }$

If, on the other hand, the signals are issued on $X _ { 2 } ,$ , the DM must consider the following cases:

I $\begin{array} { r } { \displaystyle { \harpoonright _ { x } } \ge c e _ { 1 } + c e _ { 2 | \theta } - c e _ { 2 } , } \end{array}$ then:

$$
\xi (x _ {1} | \pi (\theta | x _ {2})) = \left\{ \begin{array}{l l} \frac {(1 + (n / 1 0 0))}{\beta_ {1} - x} & \text { if } x _ {1} \in \left(\frac {\beta_ {1} + x}{2}, \beta_ {1} \right] \\ \frac {(1 - (n / 1 0 0))}{\beta_ {1} - x} & \text { if } x _ {1} \in \left(x, \frac {\beta_ {1} + x}{2} \right] \end{array} \right.\tag{34}
$$

$$
\xi (x _ {2} | \pi (\theta | x _ {2})) = \left\{ \begin{array}{l l} \left[ \frac {1}{\beta_ {2} - x} + \frac {((\alpha_ {2} + \beta_ {2}) / 2) - x}{2 (\beta_ {2} - x) [ \beta_ {2} - ((\alpha_ {2} + \beta_ {2}) / 2) ]} + \frac {n / 1 0 0}{2 (\beta_ {2} - x)} \right] \left(1 + \frac {n}{1 0 0}\right) & \text {if} x _ {2} \in \left(\frac {\beta_ {2} + c e _ {1} + c e _ {2 | \theta} - x}{2}, \beta_ {2} \right] \\ \left[ \frac {1}{\beta_ {2} - x} + \frac {((\alpha_ {2} + \beta_ {2}) / 2) - x}{2 (\beta_ {2} - x) [ \beta_ {2} - ((\alpha_ {2} + \beta_ {2}) / 2) ]} + \frac {n / 1 0 0}{2 (\beta_ {2}} - x) \right] \left(1 - \frac {n}{1 0 0}\right) & \text {if} x _ {2} \in \left(c e _ {2}, \frac {\beta_ {2} + c e _ {1} + c e _ {2 | \theta} - x}{2} \right] \\ \frac {(1 - (n / 1 0 0))}{2 (\beta_ {2} - x)} & \text {if} x _ {2} \in [ c e _ {1} + c e _ {2 | \theta} - x, c e _ {2} ] \end{array} \right.\tag{35}
$$

If $x < c e _ { 1 } + c e _ { 2 | \theta } - c e _ { 2 } ,$ then:

$$
\xi (x _ {2} | \pi (\theta | x _ {2})) = \left\{ \begin{array}{l l} \frac {(1 + (n / 1 0 0))}{\beta_ {2} - c e _ {1} - c e _ {2 | \theta} + x} & \text { if } x _ {2} \in \left(\frac {\beta_ {2} + c e _ {1} + c e _ {2 | \theta} - x}{2}, \beta_ {2} \right] \\ \frac {(1 - (n / 1 0 0))}{\beta_ {2} - c e _ {1} + c e _ {2 | \theta} + x} & \text { if } x _ {1} \in \left(c e _ {1} + c e _ {2 | \theta} - x, \frac {\beta_ {2} + c e _ {1} + c e _ {2 | \theta} - x}{2} \right] \end{array} \right.\tag{36}
$$

The distribution on $X _ { 1 }$ remains identical to the $\xi ( x _ { 1 } | \pi ( \theta | x _ { 2 } ) )$ just described for $x \geq c e _ { 1 } + c e _ { 2 | \theta } - c e _ { 2 }$

To simplify the notation, we will denote the functions defined above by $\xi ( x _ { i } ) ,$ with the subscript $i = 1 , \ 2$ referring to the characteristic on which the signal has been issued.

We use these density equations to calculate the expected product received by a DM after observing a given signal on either the first or the second set of characteristics. These equations increase the utility derived from the expected product whenever the DM expects to observe more than one improved product fully.

In this respect, $n = 0 . 5$ if the DM expects to observe one improved product fully and an additional one partially. A value of $n = 1$ is assigned by the DM when two improved products are expected to be fully observed and so on, with any new fully observed product adding a value of one to n; a partially observed product adds a value of 0.5.

The reference value of 100 relative to which the improved products shift probability could be modified to account for the degree of optimism of the DM. Clearly, when $n { = } 1 0 0$ , the probability mass has been fully shifted to the corresponding upper subinterval of the domain. This redistribution of the density implies that we have assumed that the DM accounts for the possibility of selecting the best product among the potentially acceptable products expected to be observed.

To provide additional intuition, we explicitly define the fourobservation case with signals based on the density functions introduced in this section. The appendix provides an explicit illustration of how the model actually operates when signals are received on both $X _ { 1 }$ and $X _ { 2 }$ and how it is simulated when four observations are considered.

## 5. Acquiring observations with signals

Assume that the DM receives a signal on the distribution of one of the characteristic factor spaces. The DM has to calculate two enhanced versions of the original functions $F ( x _ { 1 } )$ and $H ( x _ { 1 } ) .$ . These new functions must account for the number of observations left to be acquired by the DM and the probability that such observations provide a product better than the one initially observed, which constitutes the main reference value. The DM follows an identical pattern to that of the two- and three-observation cases when defining the sets of combinations resulting from the search. However, the potential improvement probabilities as well as the expected products obtained from the search are both determined by the initial observation and the type of signal issued by the firm.

## 5.1. The four-observation case

Now consider the information acquisition problem faced by a DM who has gathered the first observation from an initial product, given by $x _ { 1 }$ , when a total of four observations can be acquired. We will not provide a detailed account of the search payoff possibilities as in the case with three observations, but a basic schema is developed in the appendix.

When calculating the enhanced function $F ( x _ { 1 } | 4 , \theta ) ,$ , we must account for the fact that the DM uses the second piece of information available to acquire x and observe the initial product fully; i.e., the DM observes $( x _ { 1 } , x _ { 2 } )$ . As a result, the payoff obtained by the DM depends on the expected realization of $x _ { 2 }$ and that of $x _ { 1 } ^ { n } ,$ i.e., the first characteristic from the new product observed. The following combinations must be considered when calculating the term A within the function $F ( x _ { 1 } | 4 , \theta )$ based on three remaining observations: (2-0), (2-1), and (1-1).

$$
\begin{array}{l} (2 \text {-0}): \int_ {P ^ {+} (x _ {1} | \theta)} \mu_ {2} (x _ {2} | \theta) [ \psi_ {1} (2, 0, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (E _ {1} + E _ {2} | \theta) ] d x _ {2} \\ (2 \text {-1}): \int_ {P ^ {+} (x _ {1} | \theta)} \mu_ {2} (x _ {2} | \theta) [ \psi_ {1} (2, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (u _ {1} (x _ {1} ^ {n}) + E _ {2} | \xi (x _ {i})) ] d x _ {2} \\ (1 \text {-1}): \int_ {P ^ {+} (x _ {1} | \theta)} \mu_ {2} (x _ {2} | \theta) \psi_ {1} (1, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) \\ [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (u _ {1} (x _ {1} ^ {n}) + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i})) \\ + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (E _ {1} + E _ {2} | \theta) ] d x _ {2} \end{array}
$$

We have employed the notation $\left( E _ { 1 } + E _ { 2 } | \boldsymbol { \theta } \right)$ to define the certainty equivalent outcome from the search process when one of the certainty equivalent values is based on a signaled characteristic factor space. Similarly, we will use $\left( \cdot \ : | \xi ( x _ { i } ) \right)$ to indicate the subjective expected product computed by the DM whenever the potential improvements resulting from the search include at least a $u _ { i } ( x _ { i } ^ { n } )$ term, with $i = 1 , 2 $

Note that the interval limits defining the term A are based on the signal received by the DM. Consider, for example, a signalbased improvement on the first characteristic:

$$
P ^ {+} (x _ {1} | \theta) = \{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) > E _ {1 | \theta} + E _ {2} - u _ {1} (x _ {1}) \}\tag{37}
$$

and

$$
P ^ {-} (x _ {1} | \theta) = \{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) \leq E _ {1 | \theta} + E _ {2} - u _ {1} (x _ {1}) \}\tag{38}
$$

$P ^ { + } ( x _ { 1 } | \theta )$ and $P ^ { - } ( x _ { 1 } | \theta )$ define the set of values $x _ { 2 }$ from the initial product such that their combination with $x _ { 1 }$ delivers a utility that is higher or less than or equal to a randomly chosen product from $G ,$ respectively. We will use the same notation, namely, $P ^ { + } ( x _ { 1 } | \theta )$ and $P ^ { - } ( x _ { 1 } | \theta )$ , when considering the sets defining signal-based improvement on the second characteristic, which are determined by $E _ { 2 | \theta } .$ The context within which the corresponding functions will be used prevents any confusion between cases.

When defining the enhanced version of function $H ( x _ { 1 } | 4 , \theta ) ,$ , we must account for the fact that the DM has one more observation left to acquire than in the $F ( x _ { 1 } | 4 , \theta )$ setting because the second observation has not been used to acquire $x _ { 2 } .$ . The following combinations arise from the set of three observations that the DM has left to acquire when computing $H ( x _ { 1 } | 4 , \theta ) \colon ( 3 { - } 0 ) , ( 3 { - } 1 ) , ( 2 { - } 1 )$ (2-2).

$$
\begin{array}{l} (3 \text {-0}): \psi_ {1} (3, 0, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (E _ {1} + E _ {2} | \theta) \\ (3 \text {-1}): \psi_ {1} (3, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (u _ {1} (x _ {1} ^ {n}) + E _ {2} | \xi (x _ {i})) \\ (2 \text {-1}): \psi_ {1} (2, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (u _ {1} (x _ {1} ^ {n}) \\ \qquad + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i})) + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (E _ {1} + E _ {2} | \theta) ] \\ (2 \text {-2}): \psi_ {1} (2, 2, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) \max \{(u _ {1} (x _ {1} ^ {n}) \\ \qquad + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i}))  ,   (u _ {1} (x _ {1} ^ {n + 1}) + E _ {2} | \xi (x _ {i})) \} \\ \qquad + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} ^ {n} | \theta))) (u _ {1} (x _ {1} ^ {n + 1}) + E _ {2} | \xi (x _ {i})) ] \end{array}
$$

## 6. Numerical simulations

This section presents several numerical simulations illustrating the information gathering behavior of the DM when acquiring any amount between two and five observations while receiving signals on the first or the second characteristic. It should be emphasized that a larger number of observations could be considered and a general form derived for any positive (but bounded) number of observations. Simulations will be provided for a risk neutral DM, although a considerable set of potential settings can be analyzed by applying the formal environment described in the paper. The following parameter values will be employed throughout the numerical simulations

(i) Characteristic spaces: $X _ { 1 } = [ 5 , 1 0 ] , X _ { 2 } = [ 0 , 1 0 ] ;$

(ii) Utility functions: $u _ { 1 } ( x _ { 1 } ) = x _ { 1 } , u _ { 2 } ( x _ { 2 } ) = x _ { 2 } ;$ and

$$
\begin{array}{l} \text {(iii) Probability densities:} \quad \forall x _ {1} \in X _ {1}, \quad \mu_ {1} (x _ {1}) = 1 / 5; \quad \forall x _ {2} \in X _ {2}, \\ \mu_ {2} (x _ {2}) = 1 / 1 0. \end{array}
$$

We now illustrate the effect induced by positive signals regarding the distribution of $X _ { 1 }$ and $X _ { 2 }$ on the information acquisition behavior of the DM. A formal explicit analysis can be found in the appendix. To facilitate comparisons among the threshold values generated within the different scenarios, the support of the respective signal-induced probability functions will remain unchanged throughout the simulations. In all figures, the horizontal axis represents the set of $x _ { 1 }$ realizations that may be observed by the DM, with the corresponding subjective expected utilities defined on the vertical axis.

The basic reference risk neutral setting with two observations and signals issued on the first and the second characteristic is represented in Fig. 4a and b, respectively. Observe the dominance throughout the whole domain of the function $H ( x _ { 1 } )$ over $F ( x _ { 1 } )$ and of $H ( x _ { 1 } | \theta )$ over $F ( x _ { 1 } | \theta )$ . We will maintain this simplified notation throughout the simulations to differentiate the signaled from the unsignaled settings. As we will see in the rest of the numerical simulations, this initial dominance effect wears off as a higher number of observations become available to the DM. Clearly, when only two observations are acquired, continuing with the initial product observed implies ending up with a unique product: either the initial one if it provides a utility higher than $( c e _ { 1 } , c e _ { 2 } )$ or a randomly chosen product if the utility derived from the initial one is below that of $( c e _ { 1 } , c e _ { 2 } )$

However, when acquiring information on a new product, the DM will have two products to choose from, the initial and a new one, both partially observed. The new product is added to the total utility of the DM, who biases his incentives toward observing a product other than the initial one.

This effect is eliminated in Di Caprio and Santos Arteaga [11], where a unique final product is accounted for in the choice set of the DM through both functions F and H. The current framework is designed to accommodate a large amount of potential observations and it is to be treated as such, with a large bias arising toward diversification when a small number of observations are acquired.

Note that we have defined the set of potential improvements upon the reference realization in terms of either the $( x _ { 1 } , P ^ { + } ( x _ { 1 } ) )$ or the $\left( x _ { 1 } , P ^ { + } ( x _ { 1 } | \theta ) \right)$ pair. This assumption accounts for any framing effect on the side of the DM that may be induced by the (partial) observation of the initial product. At the same time, it conditions any potential improvement on the information available to the DM, who does not know the outcome from the second observation but is able to compute the set of acceptable realizations.

We could also assume that the DM shifts the reference product whenever the next potential realization is located above the initially observed $x _ { 1 } .$ In this case, the structure of the algorithm requires adding a new dimension to the process, as the DM must also account for the value of all the remaining observations while conditioned by such a realization and the initial one. Thus, each potential observation that the DM wants to consider as a determinant of his search behavior adds a dimension to the information acquisition process, as has been shown in Di Caprio et al. [15].

![](/api/attachments/XRE9PABD/fulltext/images/32014c2b7bc651e49a827afca02563f57101183885a125ccc8eeb218dd27b520.jpg)  
a. Signal received on $x _ { 1 }$

![](/api/attachments/XRE9PABD/fulltext/images/d1a8e6aae46dcd2eac73a9c3177fe36184857116dededcbd8f5b1cfc304286ba.jpg)  
b. Signal received on $x _ { 2 }$  
Fig. 4. Information acquisition incentives with two observations.

Fig. 5 illustrates how the three-observation setting delivers information acquisition incentives that differ considerably from those obtained when two observations are acquired. This setting presents an important decrement in the Starting dominance pattern obtained within the two-observation environment. That is, the Starting option still dominates the Continuing option through most of the $X _ { 1 }$ domain but to a much lesser extent than in the twoobservation case.

Fig. 6 illustrates the case in which a fourth observation is acquired. The DM will favor the acquisition of information on the product initially observed over starting with a new product. At the same time, note how the dominant Continuing tendency extends over a wider interval in the X signaling case when compared to the $X _ { 2 }$ case. The exact interval values are presented in Table 1.

Now consider the case with five observations represented in Fig. 7. Note that when signals are issued on $X _ { 1 }$ , the functions F and H display lower expected utilities through a considerable interval within the domain. This effect becomes more evident as we approach ce and is due to the increment in the CE value required by the DM, which shifts from 12.5 to 13.25. This increment in the CE value decreases the probability of improving upon the initial observation with the potential realizations from $X _ { 2 } .$ That ${ \mathrm { i } } s ,$ the remaining observations must improve upon the initial reference product determined by $x _ { 1 }$ and $P ^ { + } ( x _ { 1 } )$ . This latter set shrinks when signals are issued on $X _ { 1 }$ , while its associated distribution remains unchanged, excluding several $X _ { 2 }$ realizations from constituting acceptable products for the DM.

![](/api/attachments/XRE9PABD/fulltext/images/00042c2dbc9c5c862d1fcb7b2750333a6c93c7ed08b6f646399856fb2abade9d.jpg)

![](/api/attachments/XRE9PABD/fulltext/images/cdbac6a0b6ead2e651d434946671371d37802918ba511b11d7e452698b65c2a5.jpg)  
b. Signal received on $x _ { 2 }$  
Fig. 5. Information acquisition incentives with three observations.

The simulations in Fig. 7 illustrate the upward shift that the signals issued on $X _ { 2 }$ cause on the search utilities of the DM compared to the more intricate effect derived from issuing signals on $X _ { 1 }$ . This difference is derived from the fact that the DM eliminates (to a certain extent) the uncertainty associated with $X _ { 1 }$ after acquiring the initial observation, while the uncertainty associated with $X _ { 2 }$ persists when deciding how to allocate the next observation. As a result, we can see how positive signals issued on the characteristics of a given product do not necessarily increase the willingness of the DM to acquire such a product. Indeed, the incentives of the DM to continue acquiring information on the initially observed product decrease if the improvements are introduced on $X _ { 2 } ,$ i.e., positive signals actually lead to a smaller continuation interval when issued on $X _ { 2 } .$

Threshold values and continuation intervals (F(	) > H(	)).

<table><tr><td rowspan="2"></td><td colspan="4">Observations</td></tr><tr><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="2">Absent signals</td><td rowspan="2">-</td><td>[5, 5.6966]</td><td>[5, 7.9294]</td><td>[5, 7.0851]</td></tr><tr><td>[9.9030, 10]</td><td>[9.8990, 10]</td><td>[9.8968, 10]</td></tr><tr><td rowspan="2">Signals on  $X_1$ </td><td rowspan="2">-</td><td>[5, 6.3125]</td><td>[5, 8.6141]</td><td>[5, 7.2151]</td></tr><tr><td>[9.8963, 10]</td><td>[9.8887, 10]</td><td>[9.8846, 10]</td></tr><tr><td rowspan="2">Signals on  $X_2$ </td><td rowspan="2">-</td><td>[5, 5.6500]</td><td>[5, 7.8319]</td><td>[5, 6.4025]</td></tr><tr><td>[9.9003, 10]</td><td>[9.8960, 10]</td><td>[9.8937, 10]</td></tr></table>

![](/api/attachments/XRE9PABD/fulltext/images/6f74c69011ee1edf73284c3fa37aa3fe1f6127733658acf8d5c60b9de0ae877a.jpg)

![](/api/attachments/XRE9PABD/fulltext/images/6f1d7e901d149bc27ebd9d629b220346dff40ecb2336426d39a38f5ef0f86568.jpg)  
b. Signal received on $x _ { 2 }$  
Fig. 6. Information acquisition incentives with four observations.

## 7. The information acquisition process

The numerical simulations presented in the previous section illustrate a subset of the potential pairwise comparisons performed by the DM at different steps of the information acquisition process. Some general remarks on the properties of the information acquisition process of the DM follow.

(i) The comparisons performed by the DM will be generally based on the expected utility derived from continuing to acquire information on the partially observed product with the highest $x _ { 1 }$ and the utility derived from starting to acquire information on a new product. As stated in Section 4, it is trivial to show why the DM considers the partially observed product with the highest $x _ { 1 }$ over any other that is partially observed when defining the corresponding function F.

b. Signal received on $x _ { 2 }$  
![](/api/attachments/XRE9PABD/fulltext/images/46c18661739ac50e9ca199ccb5383bc61bc1fa9eaec93d004f0aa3511170a492.jpg)

![](/api/attachments/XRE9PABD/fulltext/images/a0a28f34b7584589e2429d82b1497ad7ed4e7a10490e22b604dfebffdd411e28.jpg)  
Fig. 7. Information acquisition incentives with five observations.

(ii) If all the previous products have been completely observed, the DM faces the information acquisition setting described in Sections 4 and 5 but adapted to the number of remaining observations. That is, the formal settings defined in both sections describe the information acquisition incentives of the DM either when he starts acquiring information or after having fully observed a given number of products.

(iii) The reference product that the DM must improve upon is given by the product that provides the highest utility among all those previously observed. In particular, the functions F and H will be conditioned by the first characteristic from the highest utility-providing product that has been fully observed.

(iv) The information acquisition process must be adjusted as the number of remaining observations decreases and whenever the products observed modify the reference values considered by the DM.

The online information acquisition process of the DM: basic guidelines. Continue $\mathrm { I f } \ F ( x _ { 1 } | n , \theta ) > H ( x _ { 1 } | n , \theta ) ,$ , the DM acquires the second observation from the initial product observed, i.e., x . After acquiring $x _ { 2 } ,$ the DM will have completely observed the initial product, (x , x ), while being endowed with $n - 2$ remaining observations. Trivially, the DM must observe the first characteristic from a new second product, $x _ { 1 } ^ { n } ,$ , and then decide once again whether to continue with the newly observed product or to start acquiring information on a third one. His decision will be determined by the corresponding functions Fðx<sup>n</sup>jn2; uÞ and Hðx<sup>n</sup>jn2; uÞ. These functions are based on the x<sup>n</sup> observed, and their reference values will be defined with respect to the initial fully observed product if it provides a utility higher than the certainty equivalent one. The same continuing versus starting decision must be made by the DM after acquiring the next observation. Start $\begin{array} { r } { \textrm { I f } F ( x _ { 1 } | n , \theta ) < H ( x _ { 1 } | n , \theta ) , } \end{array}$ , the DM acquires information on a new product. In this case, he will have observed two products partially, whose first characteristics are given by $x _ { 1 }$ and $x _ { 1 } ^ { n } ,$ while being endowed with $n - 2$ remaining observations. The DM must now decide between continuing with either $x _ { 1 }$ or x<sup>n</sup> and starting to acquire information on a new product. As already stated, he will consider the highest value between $x _ { 1 }$ and $x _ { 1 } ^ { n } ,$ denoted by $x _ { 1 } ^ { M }$ , in order to define the corresponding functions $F ( x _ { 1 } ^ { M } | n { - } 1 , \mathbf { \dot { \theta } } )$ and $H ( x _ { 1 } ^ { M } | n { - } 1 , \theta )$ Continue $\mathrm { I f } F ( x _ { 1 } ^ { M } | n - 1 , \theta ) > H ( x _ { 1 } ^ { M } | n - 1 , \theta ) ,$ , the DM fully observes the product with the highest first characteristic; i.e., he observes $x _ { 2 } ^ { M } ,$ , and then, he once again faces the problem of either continuing with the remaining partially observed product or starting with a new one. This decision must be conditioned on the $n - 3$ remaining observations. Start $\begin{array} { r } { \mathrm { I f } F ( x _ { 1 } ^ { M } | n - 1 , \theta ) < H ( x _ { 1 } ^ { M } | n - 1 , \theta ) , } \end{array}$ the DM will observe the first characteristic from a third product, $\mathrm { i } . \mathbf { e } . , x _ { 1 } ^ { n + 1 }$ . Given the potential realizations of thi characteristic, the DM must again define the resulting functions F and H based on the number of remaining observations and the highest value among all the partially observed products.

Fig. 8 provides an intuitive description of how the information acquisition process of the DM evolves sequentially.

Initially, the DM has n observations left to acquire. After acquiring the first observation, $x _ { 1 } ,$ the DM must choose between continuing to acquire information on the product observed and starting to acquire information on a new product. His decision is based on which function, either F or H, provides the highest expected utility. The information acquisition process of the DM proceeds according to the guidelines described in Table 2 until he exhausts all of his available information.

It should be emphasized that the information acquisition setting described in the current paper can be defined to account for any positive number of available observations.

## 8. Managerial implications

Consider the immediate consequences derived from our model regarding the strategic quality of the sequential information acquisition process of the DM. Note that this process has also been shown to condition the production plans of firms, given the considerably different reactions of the DM to improvements introduced on the first and the second characteristic. Our model can be used to

\- Develop decision support and expert systems as optimal sequential information acquisition strategies, where information is only acquired if the benefits derived from the information exceed its cost [42,52]. A similar remark applies to the design of the information dashboards guiding managerial decision making processes [2,21,24].

\- Extend papers in a heterogeneous direction, as in Li and Zhu [32], where a group of homogeneous experts must be hired to forecast the stochastic market demand for a new product that is about to be introduced in the market.

![](/api/attachments/XRE9PABD/fulltext/images/d386e5ae1bc64d3b1c6c961c6d23595cbaa921708295b64fbca4810a1011d42c.jpg)  
Fig. 8. The sequential information acquisition process of the DM.

\- Design dynamic extensions of standard multiple-criteria decision making models [7], accounting for the fact that in our model, the DM considers the set of potential realizations expected to be observed and modifies his threshold values after acquiring each observation.

\- Formalize the information acquisition and choice processes considered by the consumer choice literature, where frictions in the acquisition of information, such as limits in the cognitive capacity of the DM, the existence of context effects, and the transmission of superfluous information, have been described but not formalized [4,5,16,46].

\- Analyze the effect of memory capacity and previous experience in determining the payoffs expected to be received and the resulting information acquisition behavior of the DM, i.e., study the generation of a potential base of loyal consumers [3].

\- Study the equilibrium implications derived from the strategic transmission of information within imperfectly competitive scenarios, extending into the game theoretical branch of operations research [50,39,18]. That is, the results displayed by an online search engine can be interpreted by the DM as bidimensional objects, composed of a succinct description and additional information that can only be obtained after accessing the corresponding website. In this respect, our model provides a formal reference framework to study online search processes and, for example, compute the probability of accessing a given website based on its relative position within the ranking displayed by the search engine. Following this particular approach would complement the results obtained by papers such as those of Wang et al. [61], who propose a method to estimate the probability that a product is purchased after being observed by a DM, and Dou et al. [17], who analyze how firms can use their position in the ranking delivered by online search engines to differentiate their products from those of rivals. The main implications of the current paper for this research area are described below.

(i) Consider an online search environment where the DM must evaluate search and experience goods. Huang et al. [26] illustrate how observing experience goods requires a greater amount of time per page, leading to a lower number of pages being evaluated than when observing search goods. As already indicated, our second characteristic can be interpreted as an experience component that complements the first one. When considered in terms of costs, improvements in the second characteristic have a negative effect on the expected payoffs of the firms. At the same time, due to their effect on the threshold values computed by the DM, improvements in the first characteristic may also be used to limit the total number of products observed by the DM.

(ii) Finally, consider the online recommendations provided to a DM based on his purchasing history [63,25,33]. Recommendation agents are software agents who, after eliciting the preferences of individual consumers, make recommendations accordingly. These recommendations involve the description of a series of characteristics from an unobserved product by unknown third parties. Absent credibility and trust considerations [20] and strategic reporting [12,48], the DM must choose which recommendation to follow. The (subjective) evaluation of the considerable amount of consumer reviews available to the DMs online provides a similar set of implications [64].

## 8.1. Memory capacity and search costs

Consider the set of implications relating the current model to the scenarios faced by a DM who is performing online searches. In this type of environment, the full memory capacity with which the DM is endowed when defining his search strategy is a fundamental property of our model. That is, the capacity of the DM to remember and compare the characteristics of the products observed with the potential realizations resulting from the search should be a fundamental requisite of any online search model. As stated in the introduction, the management and the operations research literature concentrate on computing stopping search rules based on the expected value of the next characteristic and the information acquisition costs faced by the DM. This focus on the costs deviates attention from memory, a relation that should be inverted when analyzing online search environments. That is, the cost of shifting among different online results is relatively small, while the first characteristics of the alternatives displayed by an online search engine are easily observable, increasing the capacity of the DM to remember previous realizations from the search.

It should be noted that the introduction of information acquisition costs within the current search process is straightforward. Given the findings of Huang et al. [26], three possibilities could be considered depending on the level of sophistication required from the DM. One possibility would consist of assigning a given cost to each of the remaining potential observations of the first characteristic and a higher cost to those of the second characteristic. These costs should then be added to the corresponding functions F and H. A similar, though less demanding, approach would be to assign a fixed cost incurred by the DM when acquiring the next observation and compare it to the expected utility derived from the search. Finally, an intermediate possibility would consist of assuming that continuing requires the DM to assume a higher cost than starting. This would lead to a downward shift in both functions F and H. However, the size of the shift would be larger for F, decreasing the corresponding continuation regions in all the figures.

The capacity of our model to incorporate diverse types of information costs based on the number and type of remaining observations confers an advantage over other models that rely uniquely on a given fixed cost.

## 9. Conclusions

We have studied the information acquisition behavior of a rational DM who is gathering a sequentially finite number of observations from a set of products whose attributes have been grouped into two main characteristics. The introduction of signals within our formal setting has allowed us to determine the strategic consequences that issuing different types of signals has on the information acquisition behavior of the DM.

Consequently, the model introduced in this paper can be applied to any of the research areas linked by their analysis of the optimal information acquisition behavior of rational DMs, such as economics, consumer choice and the decision and game theoretical branches of operations research. Applications to knowledge management and decision support systems follow immediately from our formal setting, particularly when considering the introduction and acceptance of novel technological products and when analyzing online search environments.

From a formal point of view, the main extension of the current model should aim to increase the dimension of the products on which observations are acquired. As the dimension of the product increases, the set of potential combinations and expected payoffs that must be considered by the DM also increases, which increments the sophistication required on the assimilation capabilities of the DM.

## Acknowledgements

The authors would like to thank the anonymous reviewers and the editor for their insightful comments and suggestions.

## Appendix A. Appendix

## Explicit calculations

Consider the expression for the functions F and H in the setting with four observations and signals

$$
\begin{array}{l} F (x _ {1} | 4, \theta) \stackrel {{d e f}} {{=}} \int_ {P ^ {+} (x _ {1} | \theta)} \mu_ {2} (x _ {2} | \theta) (u _ {1} (x _ {1}) + u _ {2} (x _ {2}) | \xi (x _ {i})) d x _ {2} \\ \qquad + A + \int_ {P ^ {-} (x _ {1} | \theta)} \mu_ {2} (x _ {2} | \theta) (E _ {1} + E _ {2} | \theta) d x _ {2} + B \end{array}
$$

where

$$
\begin{array}{l} A = \int_ {P ^ {+} (x _ {1} | \theta)} \mu_ {2} (x _ {2} | \theta) [ \psi_ {1} (2, 0, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (E _ {1} + E _ {2} | \theta) \\ \quad + \psi_ {1} (2, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (u _ {1} (x _ {1} ^ {n}) + E _ {2} | \xi (x _ {i})) \\ \quad + \psi_ {1} (1, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (u _ {1} (x _ {1} ^ {n}) \\ \quad + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i})) + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (E _ {1} + E _ {2} | \theta) ] ] d x _ {2} \\ B = \int_ {P ^ {-} (x _ {1} | \theta)} \mu_ {2} (x _ {2} | \theta) [ \psi_ {1} (2, 0, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (E _ {1} + E _ {2} | \theta) \\ \quad + \psi_ {1} (2, 1, \nu_ {\mu_ {1}} (x _ {1} ^ {n} > x _ {1} | \theta)) (u _ {1} (x _ {1} ^ {n}) + E _ {2} | \xi (x _ {i})) \\ \quad + \psi_ {1} (1, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2}. (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (u _ {1} (x _ {1} ^ {n}) \\ \quad + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i})) + \psi_ {2}. (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (E _ {1} + E _ {2} | \theta) ] ] d x _ {2} \end{array}
$$

Note that both the A and B terms define potential improvements over the CE product, with the new characteristic $x _ { 1 } ^ { n } > x _ { 1 }$ and the corresponding $P ^ { + } ( x _ { 1 } | \theta )$ set based on all the potential realizations of $x _ { 1 } .$ . This latter set requires x<sup>n</sup> to deliver a product that is better than the CE product, $\left( E _ { 1 } + E _ { 2 } | \boldsymbol { \theta } \right)$ , when added to $x _ { 1 } ^ { n }$

$$
\begin{array}{l} H (x _ {1} | 4, \theta) \stackrel {{d e f}} {{=}} (u _ {1} (x _ {1}) + E _ {2} | \theta) + C \\ C = \psi_ {1} (3, 0, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (E _ {1} + E _ {2} | \theta) \\ \quad + \psi_ {1} (3, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) (u _ {1} (x _ {1} ^ {n}) + E _ {2} | \xi (x _ {i})) \\ \quad + \psi_ {1} (2, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (u _ {1} (x _ {1} ^ {n}) \\ \quad + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i})) + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (E _ {1} + E _ {2} | \theta) ] \\ \quad + \psi_ {1} (2, 2, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) \max \{(u _ {1} (x _ {1} ^ {n}) \\ \quad + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i}))  ,   (u _ {1} (x _ {1} ^ {n + 1}) + E _ {2} | \xi (x _ {i})) \} \\ \quad + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (u _ {1} (x _ {1} ^ {n + 1}) + E _ {2} | \xi (x _ {i})) ] \end{array}
$$

The additional observation available to the DM modifies the set of potential improvements when compared to the function $F ,$ which is determined by a weighted average based on the expected realizations of $x _ { 2 }$ and the resulting sets $P ^ { + } ( x _ { 1 } | \theta )$ and $P ^ { - } ( x _ { 1 } | \theta )$

Below, we explicitly illustrate what the model actually simulates when signals are received on both $X _ { 1 }$ and $X _ { 2 }$ within the four-observation setting.

Signals on $X _ { 1 }$

Throughout this subsection, we have $c e _ { 1 } = 7 . 5 , c e _ { 2 } = 5 ,$ $c e _ { 1 | \theta } = 8 . 1 2 5$ and

$$
P ^ {+} (x _ {1} | \theta) = \left\{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) > E _ {1 | \theta} + E _ {2} - u _ {1} (x _ {1}) \right\}
$$

$$
P ^ {-} (x _ {1} | \theta) = \{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) \leq E _ {1 | \theta} + E _ {2} - u _ {1} (x _ {1}) \}
$$

The binomial distribution determining the potential improvements within $X _ { 1 }$ for a given initial observation $x _ { 1 }$ is given by:

$$
\psi_ {1} (n, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) = \left\{ \begin{array}{l l} \frac {n !}{l ! (n - l) !} \left[ (1 0 - x _ {1}) \frac {3}{1 0} \right] ^ {l} \left[ 1 - (1 0 - x _ {1}) \frac {3}{1 0} \right] ^ {n - l} & \text { if } x _ {1} \in (7. 5, 1 0 ] \\ \frac {n !}{l ! (n - l) !} \left[ \frac {7 . 5 - x _ {1}}{1 0} + \frac {7 . 5}{1 0} \right] ^ {l} \left[ 1 - \left(\frac {7 . 5 - x _ {1}}{1 0} + \frac {7 . 5}{1 0}\right) \right] ^ {n - l} & \text { if } x _ {1} \in [ 5, 7. 5 ] \end{array} \right.
$$

This binomial describes the probability mass accumulated within the interval $[ x _ { 1 } ,$ , 10] defined by the $x _ { 1 }$ observation.

The corresponding binomial accounting for potential improvements within $X _ { 2 }$ is given by:

$$
\begin{array}{l} \psi_ {2} (n, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) \\ = \frac {n !}{l ! (n - l) !} \left[ \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {l} \left[ 1 - \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {n - l}, \\ \forall x _ {1} \in [ 5, 1 0 ] \end{array}
$$

We are taking as a reference point the product defined by the initial $x _ { 1 }$ realization observed. Thus, all improvements are defined over the interval $[ x _ { 1 }$ , 10] of $X _ { 1 }$ and over the interval $[ \beta _ { 2 } - [ ( c e _ { 1 | \theta } + c e _ { 2 } ) - x _ { 1 } ]$ , 10] of X . The expected utilities determining the information acquisition behavior of the DM are based on these intervals, which define the probability mass available for expected improvements over the initial partially observed product that are contained within the set $P ^ { + } ( x _ { 1 } | \theta )$ . These probabilities are subjectively calculated by the DM and were defined in Section 5 as $\xi ( x _ { 1 } | \pi ( \theta | x _ { 1 } ) )$ and $\xi ( x _ { 2 } | \pi ( \theta | x _ { 1 } ) )$ .

Subjective improvements are computed with respect to the risk neutral $c e _ { 1 }$ value within the interval [5, 10] on which the first characteristic is defined. Truncating this interval affects the product that is expected to be obtained by the DM. Note that observing a particular $x _ { 1 }$ realization modifies the expected utility received by the DM in terms of the product that is expected to be obtained. That is, the initial observation conditions the potential improvement realizations contained within the interval $[ x _ { 1 } ,$ , 10]. Therefore, for each $x _ { 1 }$ observed, the DM must calculate an expected payoff such that the interval $[ x _ { 1 } ,$ 10] contains a probability mass equal to one and accounts also for the truncated distribution defined after receiving the signal.

We provide an explicit calculation for the expression below:

$$
\begin{array}{c} \psi_ {1} (1, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (u _ {1} (x _ {1} ^ {n}) \\ + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i})) + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (E _ {1} + E _ {2} | \theta) ] \end{array}
$$

defined within the set $P ^ { + } ( x _ { 1 } | \theta )$ and composing the term A. The expression must be divided into two separate parts depending on the realization of $x _ { 1 }$ observed by the DM. In this case, for $x _ { 1 } \in [ 7 . 5$ 10], the expression is equal to:

$$
\begin{array}{l} \int_ {1 3. 1 2 5 - x _ {1}} ^ {1 0} \left(\frac {1}{1 0}\right) \left\{\frac {1 !}{1 ! (1 - 1) !} \left[ (1 0 - x _ {1}) \frac {3}{1 0} \right] ^ {1} \left[ 1 - (1 0 - x _ {1}) \frac {3}{1 0} \right] ^ {1 - 1} \frac {1 !}{1 ! (1 - 1) !} \right. \\ \times \left[ \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {1} \left[ 1 - \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {1 - 1} \\ \times \left(\int_ {x _ {1}} ^ {1 0} \frac {1}{1 0 - x _ {1}} x _ {1} ^ {n} d x _ {1} ^ {n} + \int_ {1 3. 1 2 5 - x _ {1}} ^ {1 0} \frac {1}{x _ {1} - 3 . 1 2 5} x _ {2} ^ {n} d x _ {2} ^ {n}\right) + \frac {1 !}{1 ! (1 - 1) !} \\ \times \left[ (1 0 - x _ {1}) \frac {3}{1 0} \right] ^ {1} \left[ 1 - (1 0 - x _ {1}) \frac {3}{1 0} \right] ^ {1 - 1} \frac {1 !}{0 ! (1 - 0) !} \left[ \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {0} \\ \times \left[ 1 - \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {1 - 0} (8. 1 2 5 + 5) \Bigg \} d x _ {2} \end{array}
$$

while for $x _ { 1 } \in \left[ 5 , 7 . 5 \right]$ , we have

$$
\begin{array}{l} \int_ {1 3. 1 2 5 - x _ {1}} ^ {1 0} \left(\frac {1}{1 0}\right) \left\{\frac {1 !}{1 ! (1 - 1) !} \left[ \frac {7 . 5 - x _ {1}}{1 0} + \frac {7 . 5}{1 0} \right] ^ {1} \right. \\ \times \left[ 1 - \left(\frac {7 . 5 - x _ {1}}{1 0} + \frac {7 . 5}{1 0}\right) \right] ^ {1 - 1} \frac {1 !}{1 ! (1 - 1) !} \left[ \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {1} \\ \times \left[ 1 - \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {1 - 1} \\ \times \left(\int_ {x _ {1}} ^ {7. 5} \frac {2 . 5}{5 0 - 5 x _ {1}} x _ {1} ^ {n} d x _ {1} ^ {n} + \int_ {7. 5} ^ {1 0} \frac {1 2 . 5 - x _ {1}}{5 0 - 5 x _ {1}} x _ {1} ^ {n} d x _ {1} ^ {n} \right. \\ + \left. \int_ {1 3. 1 2 5 - x _ {1}} ^ {1 0} \frac {1}{x _ {1} - 3 . 1 2 5} x _ {2} ^ {n} d x _ {2} ^ {n}\right) + \frac {1 !}{1 ! (1 - 1) !} \\ \times \left[ \frac {7 . 5 - x _ {1}}{1 0} + \frac {7 . 5}{1 0} \right] ^ {1} \left[ 1 - \left(\frac {7 . 5 - x _ {1}}{1 0} + \frac {7 . 5}{1 0}\right) \right] ^ {1 - 1} \frac {1 !}{0 ! (1 - 0) !} \\ \times \left[ \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {0} \\ \times \left[ 1 - \frac {1 0 - (1 3 . 1 2 5 - x _ {1})}{1 0} \right] ^ {1 - 0} (8. 1 2 5 + 5) \Bigg \} d x _ {2} \end{array}
$$

Note that the main difference between both expressions is defined in terms of the product that is expected to improve upon the initial partially observed one. For $x _ { 1 } \in [ 7 . 5 , 1 0 ]$ , improvements in terms of the expected product are determined by two standard uniform probabilities defined by the corresponding functions $\xi ( x _ { 1 } | \pi ( \theta | x _ { 1 } ) )$ and $\xi ( x _ { 2 } | \pi ( \theta | x _ { 1 } ) )$ . The product that is expected to be observed involves more complex calculation when the initial observation is given by $x _ { 1 } \in \left[ 5 , 7 . 5 \right]$ . In this case, the improvements over the initial observation must be calculated in terms of the truncated uniform distribution defined between [x , 7.5] and $( 7 . 5 , 1 0 ]$ . The analysis of the $X _ { 2 }$ setting below explicitly describes how a truncated distribution affects the calculation of the expected utilities of the DM.

Signals on $X _ { 2 }$

Throughout this subsection, we have $c e _ { 1 } = 7 . 5 , c e _ { 2 } = 5$ $c e _ { 2 | \theta } = 6 . 2 5$ , and

$$
P ^ {+} (x _ {1} | \theta) = \{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) > E _ {1} + E _ {2 | \theta} - u _ {1} (x _ {1}) \}
$$

$$
P ^ {-} (x _ {1} | \theta) = \{x _ {2} \in X _ {2} \cap S u p p (\mu_ {2}): u _ {2} (x _ {2}) \leq E _ {1} + E _ {2 | \theta} - u _ {1} (x _ {1}) \}
$$

The corresponding binomial distribution determining the potential improvements within $X _ { 1 }$ is given by

$$
\begin{array}{l} \psi_ {1} (n, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) \\ = \frac {n !}{l ! (n - l) !} \left[ \frac {1 0 - x _ {1}}{5} \right] ^ {l} \left[ 1 - \left(\frac {1 0 - x _ {1}}{5}\right) \right] ^ {n - l}, \quad \forall x _ {1} \in [ 5, 1 0 ] \end{array}
$$

while the binomial determining potential improvements within $X _ { 2 }$ is divided into two subsets

The same intuition as that of the previous $X _ { 1 }$ setting applies in this case. However, in this case, the truncated distribution affects $X _ { 2 }$ and, therefore, the calculation of the expected utility received by the DM when he continues to observe the initial product. The resulting expressions are somewhat more complex than those in the $X _ { 1 }$ case described above because the modified probability enters the calculation of the function $F _ { \ast }$ This can be observed in particular when computing the expected improvements for $x _ { 1 } \in [ 8 . 7 5 , 1 0 ]$ . In this case, the realizations of the second characteristic may be located either within the interval $[ 1 3 . 7 5 - x _ { 1 } , ~ 5 ]$ or the interval [5, 10]. This fact will determine the value of the function $\mu _ { 2 } ( x _ { 2 } | \boldsymbol { \theta } )$ considered by the DM when defining the terms A and B within the equation $F _ { 1 } ( x _ { 1 } | \boldsymbol { \theta } )$

As in the case with signals on $X _ { 1 } ,$ we provide an explicit calculation of the expression

$$
\begin{array}{l} \psi_ {1} (1, 1, \mu_ {1} (x _ {1} ^ {n} > x _ {1} | \theta)) [ \psi_ {2} (1, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) \\ \times \left(u _ {1} (x _ {1} ^ {n}) + u _ {2} (x _ {2} ^ {n}) | \xi (x _ {i})\right) + \psi_ {2} (1, 0, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) (E _ {1} + E _ {2} | \theta) ] \end{array}
$$

defined within the set $P ^ { + } ( x _ { 1 } | \theta )$ and composing the term A. This expression must be divided into three separate parts depending on the realization of $x _ { 1 }$ observed by the DM and the expected realizations of $x _ { 2 } .$ In this case, for $x _ { 1 } \in [ 5 , ~ 8 . 7 5 ] ,$ , the above expression is equal to:

$$
\begin{array}{l} \int_ {1 3. 7 5 - x _ {1}} ^ {1 0} \left(\frac {3}{2 0}\right) \left\{\frac {1 !}{1 ! (1 - 1) !} \left[ \frac {1 0 - x _ {1}}{5} \right] ^ {1} \right. \\ \times \left[ 1 - \left(\frac {1 0 - x _ {1}}{5}\right) \right] ^ {1 - 1} \frac {1 !}{1 ! (1 - 1) !} \left[ (1 0 - (1 3. 7 5 - x _ {1})) \frac {3}{2 0} \right] ^ {1} \\ \times \left[ 1 - \left[ (1 0 - (1 3. 7 5 - x _ {1})) \frac {3}{2 0} \right] \right] ^ {1 - 1} \\ \times \left(\int_ {x _ {1}} ^ {1 0} \frac {1}{1 0 - x _ {1}} x _ {1} ^ {n} d x _ {1} ^ {n} + \int_ {1 3. 7 5 - x _ {1}} ^ {1 0} \frac {1}{x _ {1} - 3 . 7 5} x _ {2} ^ {n} d x _ {2} ^ {n}\right) \\ + \frac {1 !}{1 ! (1 - 1) !} \left[ \frac {1 0 - x _ {1}}{5} \right] ^ {1} \left[ 1 - \left(\frac {1 0 - x _ {1}}{5}\right) \right] ^ {1 - 1} \frac {1 !}{0 ! (1 - 0) !} \\ \times \left[ (1 0 - (1 3. 7 5 - x _ {1})) \frac {3}{2 0} \right] ^ {0} \\ \times \left[ 1 - \left[ (1 0 - (1 3. 7 5 - x _ {1})) \frac {3}{2 0} \right] \right] ^ {1 - 0} (7. 5 + 6. 2 5) \Bigg \} d x _ {2} \end{array}
$$

while for $x _ { 1 } \in [ 8 . 7 5 , 1 0 ]$ and $x _ { 2 } \in [ 1 3 . 7 5 - x _ { 1 } , 5 ]$ , we have:

$$
\begin{array}{l}\int_ {1 3. 7 5 - x _ {1}} ^ {5} \left(\frac {1}{2 0}\right) \left\{\frac {1 !}{1 ! (1 - 1) !} \left[ \frac {1 0 - x _ {1}}{5} \right] ^ {1} \left[ 1 - \left(\frac {1 0 - x _ {1}}{5}\right) \right] ^ {1 - 1} \frac {1 !}{1 ! (1 - 1) !} \right.\\\times \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] ^ {1} \left[ 1 - \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] \right] ^ {1 - 1}\\\times \left(\int_ {x _ {1}} ^ {1 0} \frac {1}{1 0 - x _ {1}} x _ {1} ^ {n} d x _ {1} ^ {n} + \int_ {1 3. 7 5 - x _ {1}} ^ {5} \frac {5}{1 0 0 - 1 0 (1 3 . 7 5 - x _ {1})} x _ {2} ^ {n} d x _ {2} ^ {n} \right.\\+ \int_ {5} ^ {1 0} \frac {1 5 - (1 3 . 7 5 - x _ {1})}{1 0 0 - 1 0 (1 3 . 7 5 - x _ {1})} x _ {2} ^ {n} d x _ {2} ^ {n}\left. \right) + \frac {1 !}{1 ! (1 - 1) !} \left[ \frac {1 0 - x _ {1}}{5} \right] ^ {1}\\\times \left[ 1 - \left(\frac {1 0 - x _ {1}}{5}\right) \right] ^ {1 - 1} \frac {1 !}{0 ! (1 - 0) !} \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] ^ {0}\\\times \left[ 1 - \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] \right] ^ {1 - 0} (7. 5 + 6. 2 5) \Bigg \} d x _ {2}\end{array}
$$

$$
\psi_ {2} (n, 1, \mu_ {2} (x _ {2} ^ {n} \in P ^ {+} (x _ {1} | \theta))) = \left\{ \begin{array}{l l} \frac {n !}{l ! (n - l) !} \left[ (1 0 - (1 3. 7 5 - x _ {1}) \frac {3}{2 0} \right] ^ {l} \left[ 1 - (1 0 - (1 3. 7 5 - x _ {1})) \frac {3}{1 0} \right] ^ {n - l} & \text { if } x _ {1} \in [ 5, 8. 7 5 ] \\ \frac {n !}{l ! (n - l) !} \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] ^ {l} \left[ 1 - \left(\frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0}\right) \right] ^ {n - l} & \text { if } x _ {1} \in [ 8. 7 5, 1 0 ] \end{array} \right.
$$

and for $x _ { 1 } \in [ 8 . 7 5 , 1 0 ]$ and $x _ { 2 } \in [ 5 , 1 0 ]$ , we have:

$$
\begin{array}{l} \int_ {5} ^ {1 0} \left(\frac {3}{2 0}\right) \left\{\frac {1 !}{1 ! (1 - 1) !} \left[ \frac {1 0 - x _ {1}}{5} \right] ^ {1} \left[ 1 - \left(\frac {1 0 - x _ {1}}{5}\right) \right] ^ {1 - 1} \frac {1 !}{1 ! (1 - 1) !} \right. \\ \times \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] ^ {1} \left[ 1 - \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] \right] ^ {1 - 1} \\ \times \left(\int_ {x _ {1}} ^ {1 0} \frac {1}{1 0 - x _ {1}} x _ {1} ^ {n} d x _ {1} ^ {n} + \int_ {1 3. 7 5 - x _ {1}} ^ {5} \frac {5}{1 0 0 - 1 0 (1 3 . 7 5 - x _ {1})} x _ {2} ^ {n} d x _ {2} ^ {n} \right. \\ + \int_ {5} ^ {1 0} \frac {1 5 - (1 3 . 7 5 - x _ {1})}{1 0 0 - 1 0 (1 3 . 7 5 - x _ {1})} x _ {2} ^ {n} d x _ {2} ^ {n}) + \frac {1 !}{1 ! (1 - 1) !} \left[ \frac {1 0 - x _ {1}}{5} \right] ^ {1} \\ \times \left[ 1 - \left(\frac {1 0 - x _ {1}}{5}\right) \right] ^ {1 - 1} \frac {1 !}{0 ! (1 - 0) !} \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] ^ {0} \\ \times \left[ 1 - \left[ \frac {5 - (1 3 . 7 5 - x _ {1})}{2 0} + \frac {1 5}{2 0} \right] \right] ^ {1 - 0} (7. 5 + 6. 2 5) \Bigg \} d x _ {2} \end{array}
$$

It should be noted that the expressions defining the expected product improvements within A and B are identical in both the $x _ { 2 } \in [ 1 3 . 7 5 - x _ { 1 } , 5 ]$ and the $x _ { 2 } \in [ 5$ , 10] cases for $x _ { 1 } \in [ 8 . 7 5$ , 10] because these realizations of $X _ { 2 }$ take place in expected terms and are therefore not observed at the time the DM makes the information acquisition decision. Thus, as in the previous $X _ { 1 }$ case, expected product improvements are determined by the intervals defined by the initial $x _ { 1 }$ realization and the resulting set $P ^ { + } ( x _ { 1 } | \theta )$

The difference between the $X _ { 1 }$ and $X _ { 2 }$ signaling settings should be evident from the simulated equations described above.

## References

[1] A.S. Abrahams, R. Barkhi, Concept comparison engines: a new frontier of search, Decis. Support Syst. 54, 2013, pp. 904–918.

[2] F. Adam, J.C. Pomerol, Developing practical decision support tools using dashboards of information, in: F. Burstein, C.W. Holsapple (Eds.), Handbook of Decision Support Systems 2. Variations, Springer-Verlag, Berlin, 2008.

[3] A. Arad, Past decisions do affect future choices: an experimental demonstration, Org. Behav. Hum. Decis. Process 121, 2013, pp. 267–277.

[4] D. Ariely, Controlling the information flow: effects on consumers’ decision making and preferences, J. Consum. Res. 27, 2000, pp. 233–248.

[5] J.N. Bearden, T. Connolly, Multi-attribute sequential search, Org. Behav. Hum. Decis. Process. 103, 2007, pp. 147–158.

[6] J.D. Bohlmann, P.N. Golder, D. Mitra, Deconstructing the pioneer’s advantage: examining vintage effects and consumer valuations of quality and variety, Manag. Sci. 48. 2002 pp. 1175-1195

[7] G. Campanella, R.A. Ribeiro, A framework for dynamic multiple-criteria decision making, Decis. Support Syst. 52, 2011, pp. 52–60.

[8] C.P. Chamley, Rational Herds, Cambridge University Press, 2004.

[9] S. Cho, K.F. McCardle, The adoption of multiple dependent technologies, Oper. Res 57, 2009, pp. 157–169.

[10] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Q. 13, 1989, pp. 319–340.

[11] D. Di Caprio, F.J. Santos Arteaga, An optimal information gathering algorithm, Int J. Appl. Decis. Sci. 2, 2009, pp. 105–150.

[12] D. Di Caprio, F.J. Santos Arteaga, Strategic diffusion of information and preference manipulation, Int. J. Strateg. Decis. Sci. 2, 2011, pp. 1–19.

[13] D. Di Caprio, F.J. Santos Arteaga, M. Tavana, Information acquisition processes and their continuity: transforming uncertainty into risk, Inform. Sci. 274, 2014, pp. 108-124.

[14] D. Di Caprio, F.J. Santos Arteaga, M. Tavana, The optimal sequential information acquisition structure: a rational utility-maximizing perspective, Appl. Math. Model, 38, 2014, pp. 3419–3435.

[15] D. Di Caprio, F.J. Santos Arteaga, M. Tavana, An optimal sequential information acquisition model subiect to a heuristic assimilation constraint. Benchmark.: Int J. 2015, (accepted for publication).

[16] K. Diehl. When two rights make a wrong: searching too much in ordered environments. I. Mark, Res. XLII, 2005, pp. 313–322.

[17] W. Dou, K.H. Lim, C. Su, N. Zhou, N. Cui, Brand positioning strategy using search engine marketing, MIS Q. 34, 2010, pp. 261–279.

[18] S. Erat, S. Kavadias, Introduction of new technologies to competing industria customers, Manag. Sci. 52, 2006, pp. 1675–1688.

[19] F.M. Feinberg, J. Huber, A theory of cutoff formation under imperfect information, Manag. Sci. 42, 1996, pp. 65–84.

[20] F. Fouss, Y. Achbany, M. Saerens, A probabilistic reputation model based on transaction ratings, Inform. Sci. 180, 2010, pp. 2095–2123.

[21] B.R. Gaines, Organizational knowledge acquisition, in: C.W. Holsapple (Ed.) Handbook of Knowledge Management. 1. Knowledge Matters, Springer-Verlag, Berlin, 2003.

[22] G. Haubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Mark. Sci. 19, 2000, pp. 4–21.

[23] T.J. Hess, A.L. McNab, K.A. Basoglu, Reliability generalization of perceived ease of use, perceived usefulness, and behavioral intentions, MIS Q. 38, 2014, pp. 1–28.

[24] C.W. Holsapple, Handbook of Knowledge Management. 2. Knowledge Directions, Springer-Verlag, Berlin, 2003.

[25] R.E. Hostler, V.Y. Yoon, Z. Guo, T. Guimaraes, G. Forgionne, Assessing the impact of recommender agents on on-line consumer unplanned purchase behavior, Inform Manag. 48, 2011, pp. 336–343.

[26] P. Huang, N.H. Lurie, S. Mitra, Searching for experience on the web: an empirical examination of consumer behavior for search and experience goods, J. Mark. 73, 2009, pp. 55–69.

[27] D. Kahneman, A. Tversky, Choices, Values, and Frames, Cambridge University Press, 2000.

[28] L.J. Kornish, Technology choice and timing with positive network effects, Eur. J. Oper. Res. 173, 2006, pp. 268–282.

[29] H.D. Kwon, Invest or exit? Optimal decisions in the face of a declining profit stream Oper. Res. 58, 2010, pp. 638–649.

[30] J. Lee, J.-N. Lee, Understanding the product information inference process in electronic word-of-mouth: an objectivity-subjectivity dichotomy perspective, Inform. Manag. 46, 2009, pp. 302–311.

[31] M. Levesque, L.M. Maillart, Business opportunity assessment with costly, imper fect information, IEEE Trans. Eng. Manag. 55, 2008, pp. 279–291.

[32] Y. Li, K. Zhu, Information acquisition in new product introduction, Eur. J. Oper. Res 198, 2009, pp. 618–625.

[33] Y.-M. Li, C.-L. Chou, L.-F. Lin, A social recommender mechanism for location-based group commerce, Inform. Sci. 274, 2014, pp. 125–142.

[34] C. Lim, J.N. Bearden, J.C. Smith, Sequential search with multi-attribute options, Decis. Anal. 3, 2006, pp. 3–15.

[35] S.A. Lippman, K.F. McCardle, Uncertain search: a model of search among technologies of uncertain values, Manag. Sci. 37, 1991, pp. 1474–1490.

[36] J.B. MacQueen, Optimal policies for a class of search and evaluation problems, Manag. Sci. 10, 1964, pp. 746–759.

[37] J. MacQueen, R.G. Miller, Optimal persistence policies, Oper. Res. 8, 1960, pp. 362– 380.

[38] F. Malerba, R. Nelson, L. Orsenigo, S. Winter, Demand, innovation, and the dynamics of market structure: the role of experimental users and diverse preferences, J. Evol. Econ. 17, 2007, pp. 371–399.

[39] J.W. Mamer, K.F. McCardle, Uncertainty, competition and the adoption of new technology, Manag. Sci. 33, 1987, pp. 161–177.

[40] D. Mayzlin, Y. Dover, J. Chevalier, Promotional reviews: an empirical investigation of online review manipulation, Am. Econ. Rev. 104, 2014, pp. 2421–2455.

[41] K.F. McCardle, Information acquisition and the adoption of new technology, Manag. Sci. 31, 1985, pp. 1372–1389.

[42] V.S. Mookerjee, B.L. Dos Santos, Inductive expert system design: maximizing system value, Inform. Syst. Res. 4, 1993, pp. 111–140.

[43] J.C. Moore, A.B. Whinston, A model of decision-making with sequential information-acquisition (Part 1), Decis. Support Syst. 2, 1986, pp. 285–307.

[44] J.C. Moore, A.B. Whinston, A model of decision-making with sequential information-acquisition (part 2), Decis. Support Syst. 3, 1987, pp. 47–72.

[45] P. Nelson, Information and consumer behavior, J. Polit. Econ. 78, 1970, pp. 311– 329.

[46] N. Novemsky, R. Dhar, N. Schwarz, I. Simonson, Preference fluency in choice, J. Mark Res XLJV 2007 pp. 347–356

[47] K.A. Paulson Gjerde, S.A. Slotnick, M.J. Sobel, New product innovation with multiple features and technology constraints, Manag. Sci. 48, 2002, pp. 1268– 1284.

[48] R.A. Peterson M.C. Merino Consumer information search behavior and the Internet, Psychol. Mark. 20, 2003, pp. 99–121.

[49] B.T. Ratchford, Cost-benefit models for explaining consumer choice and information seeking behavior, Manag. Sci. 28, 1982, pp. 197–212.

[50] J. Reinganum, On the diffusion of new technology: a game theoretic approach, Rev. Econ. Stud. 48, 1981, pp. 395–405.

[51] G. Saad, J.E. Russo, Stopping criteria in sequential choice, Org. Behav. Hum. Decis. Process. 67. 1996, pp. 258–270.

[52] F.J. Santos Arteaga, D. Di Caprio, M. Tavana, A self-regulating information acqui sition algorithm for preventing choice regret in multi-perspective decision making, Bus. Inform, Syst, Eng, 6 2014 pp. 165–175

[53] D.A. Shepherd, M. Levesque, A search strategy for assessing a business opportunity, IEEE Trans. Eng. Manag. 49, 2002, pp. 140–154.

[54] J.E. Smith, C. Ulu, Technology adoption with uncertain future costs and quality, Oper. Res. 60, 2012, pp. 262–274.

[55] M. Tavana, A subjective assessment of alternative mission architectures for the human exploration of Mars at NASA using multicriteria decision making, Comput. Oper. Res. 31, 2004, pp. 1147–1164.

[56] M. Tavana, D. Di Caprio, F.J. Santos Arteaga, An optimal information acquisition model for competitive advantage in complex multiperspective environments, Appl. Math. Comput. 240, 2014, pp. 175–199.

[57] Y. Tong, X. Wang, C.-H. Tan, H.-H. Teo, An empirical study of information contribution to online feedback systems: a motivation perspective, Inform. Manag. 50, 2013, pp. 562–570.

[58] C. Ulu, J.E. Smith, Uncertainty, information acquisition, and technology adoption, Oper. Res. 57, 2009, pp. 740–752.

[59] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a unified view, MIS Q. 27, 2003, pp. 425–478.

[60] P. Wakker, Additive Representations of Preferences. A New Foundation of Decision Analysis, Kluwer Academic Publishers, Dordrecht, 1989.

[61] H. Wang, Q. Wei, G. Chen, From clicking to consideration: a business intelligence approach to estimating consumers’ consideration probabilities, Decis. Support Syst. 56, 2013, pp. 397–405.

[62] L.L. Wilde, On the formal theory of inspection and evaluation in product markets Econometrica 48, 1980, pp. 1265–1279.

[63] B. Xiao, I. Benbasat, E-commerce product recommendation agents: use, characteristics, and impact, MIS Q. 31, 2007, pp. 137–209.

[64] Z. Yan, M. Xing, D. Zhang, B. Ma, EXPRS: an extended page rank method for product feature extraction from online consumer reviews, Inform. Manag. 2015http://dx.doi.org/10.1016/j.im.2015.02.002, (in press).
