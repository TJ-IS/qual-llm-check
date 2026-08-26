---
otero_id: 6638
otero_key: "WSHMUN7N"
title: "A decision support model for tax revenue collection in Greece"
authors: "N.D. Goumagias; D. Hristu-Varsakelis; A. Saraidaris"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.12.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support model for tax revenue collection in Greece

N.D. Goumagias ⁎, D. Hristu-Varsakelis, A. Saraidaris

Computational Systems and Software Engineering Laboratory, Department of Applied Informatics, University of Macedonia, 156 Egnatia St. 54006, Thessaloniki, Greece

## a r t i c l e i n f o

Article history: Received 10 January 2011 Received in revised form 25 November 2011 Accepted 22 December 2011 Available online 30 December 201

Keywords: Tax optimization Dynamic programming Markov chains Decision making Greece

## a b s t r a c t

In the midst of the <sup>fi</sup>nancial crisis currently unfolding in Greece, tax revenue collection is considered a top priority. This work describes a dynamic, Markov-based decision support model, aimed at predicting the behavior of a risk-neutral enterprise in Greece, and at evaluating tax policies before they are implemented. We use our model to i) analyze the effectiveness of an alternative taxation option periodically offered by the Greek government, ii) show that in the current environment, a rational enterprise has no incentive to disclose its pro<sup>fi</sup>ts, and iii) identify “virtuous” combinations of parameters which lead to full disclosure of pro<sup>fi</sup>ts © 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Faced with perhaps its most serious debt crisis in modern history, Greece is currently implementing a series of austerity measures and reforms. One of the central components prescribed in the “rescue package” overseen by the EU and the IMF calls for a dramatic increase in tax revenues and the minimization of tax evasion, the latter being one of the country's most serious and persistent problems.

The basic components of the current tax system for incorporated entities are a <sup>fl</sup>at tax rate (currently set at 24%) on pro<sup>fi</sup>ts, random audits for identifying tax evaders, and monetary penalties for underreporting income. Typically, the government does not have adequate information on a <sup>fi</sup>rm's pro<sup>fi</sup>ts, which may be manipulated through a variety of methods. Two of the most often used include i) manipulation of <sup>fi</sup>nancial statements to under-report income, and ii) invoices (often issued by another, usually short-lived <sup>fi</sup>rm) that document supposed expenses and are used to offset pro<sup>fi</sup>ts.

Penalties for tax evasion depend on the amount of unreported income, and the time elapsed since the offense took place. Speci<sup>fi</sup>cally, a <sup>fi</sup>rm found to have concealed income must pay any tax originally due on that income, plus a 2% monthly penalty on that tax. Thus, “older” tax evasion decisions are potentially more costly than recent ones. The total penalty amount is subject to a 2/3 “discount” for prompt settlement once the evasion is discovered, and is capped at twice the original tax owed.

The <sup>fi</sup>rm's<sup>1</sup> true pro<sup>fi</sup>t may be revealed by performing an audit. Because of scarce resources, Greece can only audit a limited number of cases each year, estimated at approximately 5%. Thus, in an effort to collect revenue and promote full disclosure, the government retains the right to audit businesses “retroactively” for up to <sup>fi</sup>ve years in the past. Any tax evasion activity beyond that horizon is essentially capitalized by the <sup>fi</sup>rm. Because of this, the audit probability is comparatively higher for <sup>fi</sup>rms which have not been audited for the last four years.

A somewhat unusual feature of the Greek tax system is that the government periodically offers businesses the option to “close” past tax declarations to any audits, for a fee which is to be paid for each tax year a business would like to exempt from possible audits. Because the statute of limitations on tax declarations is usually <sup>fi</sup>ve years, the government has in the past offered this option in roughly <sup>fi</sup>ve-year intervals. This “closure option” can be viewed as a kind of middle ground: it may allow an entity to cover-up past transgressions, at some cost, but it also provides the government with some tax revenue (if a suf<sup>fi</sup>cient number of businesses opt to use it), although that revenue may be less than what is properly owed. For our purposes, the option works roughly as follows. The government declares that closure will be available in the current <sup>fi</sup>scal year and will cover a given number of years in the past. The <sup>fi</sup>rm <sup>fi</sup>les this year's tax statement as usual, and declares some nominal pro<sup>fi</sup>t. It pays any tax owed on that pro<sup>fi</sup>t, plus a <sup>fi</sup>xed amount for each <sup>fi</sup>scal year it wants to cover under the closure option. In exchange for that additional amount, the government agrees to consider the past tax statement(s) as truthful and never audit them.<sup>2</sup> If a <sup>fi</sup>rm does not avail itself of the closure option, it may <sup>fi</sup>nd itself with a higher probability of being audited, as many of its peers effectively “remove” themselves from the audit pool. The most recent closures have been occurring roughly every 4–5 years during 1998–2006 (e.g., [9,10]). It is clear that Greece considers closure to be an integral part of the tax system, and a new round took place in 2010. Currently, the effectiveness of the closure option is unclear, and there is a widespread feeling that the auditing system and level of penalties are not adequate to prevent tax evasion.

The purpose of this work is to describe a decision support model which incorporates the salient features of the Greek tax system currently in place, as it pertains to <sup>fi</sup>rms. Our model, in the form of a dynamical system with inputs, is mainly designed to explore an enterprise's propensity to “cheat” under various scenarios, as the latter seeks to maximize the present value of her long-term expected pro<sup>fi</sup>ts. The main parameters of the model will be the tax rate, the probability of the <sup>fi</sup>rm being audited, the probability of the government offering the closure option in any given year, the cost of the option to the <sup>fi</sup>rm, and the penalty for unreported pro<sup>fi</sup>ts. We will describe the <sup>fi</sup>rm's evolution within the tax system by means of a Markov decision process. Our main goal is to compute the optimal behavior expected of a “typical” risk-neutral rational enterprise and identify the states in which tax evasion is an optimal policy for the <sup>fi</sup>rm. This will allow us to i) “chart” in our parameter space the region(s) which lead to honest behavior (i.e., full disclosure of pro<sup>fi</sup>ts) and maximization of government revenues, and ii) evaluate the closure option as a revenue-collecting measure and determine whether it promotes or deters tax evasion. We are also interested in knowing the extent to which a <sup>fi</sup>rm's decisions in the current year depend on past decisions, e.g., its tax evasion policy within the last <sup>fi</sup>ve years. We expect that for certain parameter values, which we would like to compute, the <sup>fi</sup>rm's optimal decisions will be independent of past behavior.

The proposed model may be useful as a tool for gauging the effectiveness of the current system, and for guiding future tax policy. Besides evaluating tax policies before they are implemented, our model can help identify those which are both <sup>fi</sup>nancially responsible and business-friendly, in the sense that they are harsh enough to make tax evasion unpro<sup>fi</sup>table, but no harsher.

## 1.1. Related work

Relevant work in the DSS literature includes [15] who applied Bedford's law to tax evasion and other types of <sup>fi</sup>nancial fraud, and [4], who presented a numerical study of [15] using a genetically optimized arti<sup>fi</sup>cial neural network. The work in [12] examined the strategic use of deceptive language in managerial <sup>fi</sup>nancial fraud via linguistic cues and suggested the use of linguistic analysis by auditors to <sup>fl</sup>ag questionable <sup>fi</sup>nancial disclosures. Early work on models for optimal taxation begins with [1] who proposed a macroeconomic equilibrium model for optimal taxation, based on portfolio allocation. In that work, an agent decides the optimal allocation of her gross income between a risky asset (undeclared income) and a risk-free asset (income disclosed). Several improvements on that model followed in subsequent work, including [2] which concentrated purely on the effects of increased probability of detection on the agent's level of evasion, and [5] where it was argued that the basic model was not adequate to describe tax evasion, and that tax rates should also be considered along with enforcement. See also [14] for a treatment of taxation from the point of view of dynamical systems and optimal control. Some discussion regarding the criteria based on which the agent makes tax evasion decisions can be found in [6]. The work in [16] considered the trade-off between <sup>fi</sup>nes and audit probabilities, and discussed government policies that account for the <sup>fi</sup>rm's attitude toward risk.

Other works, such as [8,7] went on to introduce the morality of taxpayers and auditors as variables. In [11], “morality” is captured by assigning premiums to auditors that reveal tax evasion, in order to counter the incentive for accepting bribes. More recent work regarding optimal taxation includes [19], who explored a model for linear taxation with a non-zero minimum tax. With respect to Greece, the tax evasion literature (most notably [13,18]) provides some theoretical and empirical discussion but little hard analysis.

To the best of the authors' knowledge, there have been no decision support models, and little examination of optimal taxation from the point of view of the <sup>fi</sup>rm (i.e., not in macro-economic terms) which aims to maximize the present value of her expected income through tax evasion. Furthermore, there have been no rigorous studies of the “closure option” and its effects on tax revenues; despite this, Greece recently announced a new round of closure for 2011, apparently in an effort to offset reductions in other income streams. These facts, combined with the urgency of Greece's current situation, highlight the need for decision tools that will allow one to test the effectiveness of various taxation scenarios, and to assess the policy of closurein particular. This work aims to contribute precisely in that direction.

The remainder of this paper is structured as follows: In Section 2 we describe the dynamics of a decision process in which an enterprise's after-tax pro<sup>fi</sup>t are determined each year by its own actions (e.g., by deciding how much pro<sup>fi</sup>t to reveal, and whether to make use of the closure option), as well as the actions of the government (e.g., tax penalty levels, number of audits mounted and whether to offer the closure option). We pose an optimization problem whose solution, obtained via dynamic programming, determines the <sup>fi</sup>rm's behavior, and thus the expected revenue collected by the government. In Section 3 we obtain and discuss numerical results for various scenarios of practical interest, depending on whether closure is available or not.

## 2. Model

We consider a <sup>fi</sup>rm which, at the end of each <sup>fi</sup>scal year, must declare its net pro<sup>fi</sup>t to the government or tax authority. We proceed to describe the core components of our model, in the form of an Markov decision process which captures the salient features of the Greek tax system. We will make use of the following notation. The integer k=0, 1, 2,...will denote discrete time, and x will be the value of the quantity x at time k. Individual elements of a vector, x, or matrix M, will be indicated by [x] and $[ M ] _ { i j } ,$ respectively. Finally, $0 _ { i \times j }$ will denote a i-by-j matrix of zeros.

## 2.1. State space

We will le $_ { \cdot s _ { k } \in S }$ be the tax status of a representative <sup>fi</sup>rm in year k, with

$$
\mathcal {S} = \{V _ {1},..., V _ {5}, O _ {1},..., O _ {5}, N _ {1},..., N _ {5} \},\tag{1}
$$

where

• V : the <sup>fi</sup>rm is being audited so that its true income for the last i=1, …, 5 years is veri<sup>fi</sup>ed.

• O : the <sup>fi</sup>rm has decided to use the closure option and has neither employed closure nor been audited in the past i=1, …, 5 years,

• N<sub>i</sub>: the <sup>fi</sup>rm's last audit or closure was $i = 1 , . . . , 5$ years ago. Thus, the <sup>fi</sup>rm has i unaudited tax years and will now make its (i+1)-st consecutive decision since its last audit/closure.

At the same time, $c _ { k } \in \mathcal { C }$ will be the status of the closure option in year k, where

$$
\mathcal {C} = \{\text { option   available }, \text { option   not   available } \}\tag{2}
$$

The elements of and were labeled as above mainly for the purpose of facilitating the discussion. However, for the sake of notational convenience, we will sometimes refer to them by integer, in their order of appearance in $\begin{array} { r } { S \mathrm { o r } \mathcal { C } , \mathrm { i . e . , } V _ { 1 } \mathrm { \to } 1 , V _ { 2 } \mathrm { \to } 2 , . . . , N _ { 5 } \mathrm { \to } 1 \le } \end{array}$ for states in , and <sup>S C</sup>optionavailable→1, optionnotavailab $| e \to 2$ for .

Each year, k, the <sup>fi</sup>rm makes its decisions in the form of a twoelement vector, $u _ { k }$ whose <sup>fi</sup>rst element $[ u _ { k } ] _ { 1 } \in [ 0 , 1 ]$ is the fraction of its pro<sup>fi</sup>ts to conceal, whereas $[ u _ { k } ] _ { 2 } \in \{ 1 , 2 \}$ corresponds to its selection on whetherto use the option (if available). Based on the above, we de<sup>fi</sup>ne the <sup>fi</sup>rm's state vector at time k to be

$$
x _ {k} = \left[ s _ {k}, c _ {k}, h _ {k} ^ {T} \right] ^ {T},\tag{3}
$$

where $\textstyle s _ { k } \in S , c _ { k } \in { \mathcal { C } } ,$ , and $h _ { k } \in [ 0 , 1 ] ^ { 5 }$ will contain a history of the <sup>fi</sup>rm's <sup>S C</sup>latest <sup>fi</sup>ve decisions with respect to tax evasion. We will refer to $s _ { k }$ as the <sup>fi</sup>rm's “Markov state” to distinguish it from the state (vector) prop-$\operatorname { e r } , x _ { k } .$

## 2.2. State evolution

Each year, the <sup>fi</sup>rm's status will evolve in $\mathcal { S } \times \mathcal { C } \times \left[ 0 , 1 \right] ^ { 5 }$ according to <sup>S - C - ½ </sup>a Markov decision process, with transition probabilities that depend on whether the government audits the <sup>fi</sup>rm or offers the closure option, and on whether the <sup>fi</sup>rm decides to use the option. Speci<sup>fi</sup>cally,

$$
x _ {k + 1} = A x _ {k} + B u _ {k} + n _ {k}, \quad x (0) \text {   given },\tag{4}
$$

where

$$
A = \left[ \begin{array}{c c c} 0 & & \\ & 0 & \\ & & H \end{array} \right], H = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right], B = \left[ \begin{array}{c c} 0 & 0 \\ \vdots & \vdots \\ 0 & 0 \\ 0 & 1 \end{array} \right], n _ {k} = \left[ \begin{array}{c} w _ {k} \\ \epsilon_ {k} \\ 0 _ {5 \times 1} \end{array} \right]\tag{5}
$$

and the terms $\epsilon _ { k } { \in } { \mathcal { C } } , w _ { k } { \in } { \mathcal { S } }$ are (independent) random variables whose <sup>C S</sup>distributions are discussed next

Assuming that the government offers the option with a <sup>fi</sup>xed probability, $p _ { o } ,$ each year, we can write

$$
P r (\epsilon_ {k} = i) = \left\{ \begin{array}{l l} p _ {o} & \text { if } i = 1 \\ 1 - p _ {o} & \text { if } i = 2 \end{array} \right. \quad \text {(option available)}\tag{6}
$$

where, for notational convenience we have labeled the elements of by integer.

The term $w _ { k }$ in (4) determines the <sup>fi</sup>rst element of the state vector (i.e., the <sup>fi</sup>rm's “next” Markov state in $s )$ . Before writing down the probability distribution for $w ,$ <sup>S</sup>it will be helpful to have some intuition as to what kinds of transitions are possible in . Based on our descrip-<sup>S</sup>tion of the Greek tax system, there will be three possible transition diagrams: i) $c _ { k } = 1$ (the option is offered) and $[ u _ { k } ] _ { 2 } = 1$ (the <sup>fi</sup>rm takes the option), ii) $c _ { k } = 1$ and $[ u _ { k } ] _ { 2 } = 2$ (the <sup>fi</sup>rm declines the option), and iii) $c _ { k } = 0$ (option not available). The situation is illustrated in Fig. 1, where cases ii) and iii) described previously have transition diagrams which are structurally identical but differ in their transition probabilities. For example, if the option is available and the <sup>fi</sup>rm has decided to use it (Fig. 1-A) then, with probability 1, it will transition to an option (O ) state, where its past i decisions with respect to tax evasion will be considered for closure, while its current decision will be stored in its history vector (via (5)) and may be scrutinized in the future. If there is no option available, or if there is but the <sup>fi</sup>rm has declined it (Fig. 1-B) then in the next year the <sup>fi</sup>rm moves to either a $N _ { i }$ state $( \mathrm { i . e . } ,$ , “accumulates” one more tax statement which may be audited in the future) or a $V _ { i }$ state (it is audited). The transition from $N _ { 5 }$ to itself indicates the fact that, because of the statute of limitations, a <sup>fi</sup>rm's tax history can usually only be scrutinized for <sup>fi</sup>ve years in the past. For each transition diagram we can write down a corresponding Markov matrix whose (i, j)-th element represents the probability of transitioning from the j-th to the i-th element of $s .$ We will denote these matrices (see Appendix A) by $M _ { n o } ,$ <sup>S</sup>for the case where the option is not offered $( c _ { k } = 2 ) , M _ { a }$ for the case where $c _ { k } = 1$ and the <sup>fi</sup>rm accepts, and $M _ { d }$ if $c _ { k } = 1$ but the <sup>fi</sup>rm declines the option.

![](/api/attachments/WSHMUN7N/fulltext/images/e23eef54ba60830f826ae9f5e90894541533f8f1d517cbdc1604a9e1738f90a3.jpg)  
Fig. 1. A: transition diagram in the case where closure is available and the <sup>fi</sup>rms uses it. B: transitions when closure is available but the <sup>fi</sup>rm declines, or is not available at al (these two cases have structurally identical diagrams and are differentiated only by their transition probabilities). Each arrow represents a non-zero transition probability between a pair of Markov states in . The transition probabilities are omitted to avoid clutter, but are included in Appendix A.

Returning now to $( 4 )$ , the above discussion implies that $w _ { k } ^ { \prime } s$ distribution will depend on $x _ { k }$ and $[ u _ { k } ] _ { 2 } ,$ because the random transitions that the <sup>fi</sup>rm undergoes in depend on its existing state as <sup>S</sup>well as its decision to accept or reject the option (if it is offered). In particular,

$$
P r \left(w _ {k} = i \mid x _ {k} = \left[ j, q, h _ {k} ^ {T} \right] ^ {T}, [ u _ {k} ] _ {2} = m\right) = P _ {q i j} (m), \quad i, j \in \{1, \dots , 1 5 \}, q \in \{1, 2 \}\tag{7}
$$

where, for q and u <sup>fi</sup>xed, the $P _ { q i j } ( m )$ form one of the Markov matrices $M _ { n o } , M _ { a } , M _ { d } ,$ , governing the <sup>fi</sup>rm's transitions in :

$$
P _ {q i j} (m) = \left\{ \begin{array}{l l} [ M _ {n o} ] _ {i j} & \text { if } q = 2, \forall m \quad \text {(no option)} \\ [ M _ {a} ] _ {i j} & \text { if } q = 1, m = 1 \quad \text {(option taken)} \\ [ M _ {d} ] _ {i j} & \text { if } q = 1, m = 2 \quad \text {(option declined)} \end{array} \right.\tag{8}
$$

## 2.3. State rewards and optimal value function

Let R denote the <sup>fi</sup>rm's annual pro<sup>fi</sup>t, r the nominal tax rate (currently at 0.24), β the annual penalty rate for past uncollected taxes applied in the event of an audit (currently at 0.24 as well) and, <sup>fi</sup>nally, ‘ the cost of closure as a fraction of the <sup>fi</sup>rm's pro<sup>fi</sup>ts. Based on our earlier discussion of how tax penalties are determined (Section 1), the <sup>fi</sup>rm's reward associated with making a decision $u _ { k }$ while at state $x _ { k }$ is

$$
g (x _ {k}, u _ {k}) = g \Big (\Big [ s _ {k}, c _ {k}, h _ {k} ^ {T} \Big ] ^ {T}, u _ {k} \Big) = R \cdot \left\{ \begin{array}{l l} 1 - r + r [ u _ {k} ] _ {1} & s _ {k} \in \{1 1,..., 1 5 \} \\ 1 - r + r [ u _ {k} ] _ {1} - \ell (s _ {k} - 5) & s _ {k} \in \{6,..., 1 0 \} \\ 1 - r + r [ u _ {k} ] _ {1} - r \sum_ {i = 1} ^ {s _ {k}} [ h _ {k} ] _ {6 - i} \\ - \frac {3}{5} \beta r \sum_ {i = 1} ^ {s _ {k}} i [ h _ {k} ] _ {6 - i} & s _ {k} \in \{1,..., 5 \} \end{array} \right.\tag{9}
$$

where we have again labeled elements of $s$ and by integer. The top term in the right-hand side of (9) corresponds to the reward obtained if the <sup>fi</sup>rm conceals an amount of $R [ u _ { k } ] _ { 1 }$ . The second term is the reward when the <sup>fi</sup>rm uses the option and thus pays ‘ per year since its last audit or closure. The last term is the <sup>fi</sup>rm's reward in the event of an audit, where its past history of tax evasion is used to calculate the back taxes owed and the penalty.

Assuming a time horizon of N years, the <sup>fi</sup>rm is then faced with the problem of choosing its policy, $u _ { k } ,$ , so as to maximize its discounted expected reward:

$$
\max _ {u _ {k}} \mathop {\mathbb {E}} _ {w _ {k}, \epsilon_ {k}} \left\{\sum_ {k = 0} ^ {N - 1} \gamma^ {k} g (x _ {k}, u _ {k}) \right\},\tag{10}
$$

where $\gamma \in ( 0 , 1 ]$ is a discount factor. Here, we will be interested mainly in the case where the <sup>fi</sup>rm assumes its economic lifetime will be in-<sup>fi</sup>nite and acts accordingly, thus we will not be concerned with possible end-of-horizon effects. However, such effects can easily be incorporated into the model, by adding a $\gamma ^ { N } g _ { N } ( x _ { N } )$ term to (10), in order to capture, for example, a situation where the <sup>fi</sup>rm does not make a decision in its last year of economic lifetime.

To apply dynamic programming [3], let $J _ { k } ( \boldsymbol { x } _ { k } )$ be the optimal expected reward that can be obtained from time k onwards, starting from $x _ { k } .$ . Then, the $J _ { k }$ will satisfy the following recursive equation:

$$
\begin{array}{l} J _ {k} (x _ {k}) = \max _ {u _ {k}} \Big \{g (x _ {k}, u _ {k}) + \gamma   \mathbb {E} _ {w _ {k}, \epsilon_ {k}} J _ {k + 1} \big (x _ {k + 1} \big) \Big \}, \\ J _ {N} (x _ {N}) = g _ {N} (x _ {N}) \end{array}\tag{11}
$$

subject to the state dynamics (4).

Assuming that the <sup>fi</sup>rm expects to operate inde<sup>fi</sup>nitely $( N {  } \infty )$ , its optimal decisions are then obtained by solving the stationary Bellman equation associated with Eq. (11), i.e.

$$
J _ {\infty} (x) = \max _ {u} \left\{g (x, u) + \gamma \underset {w, \epsilon} {\mathbb {E}} J _ {\infty} (A x + B u + n) \right\}\tag{12}
$$

Finally, given the probability distributions for w and (Section 2.2), and the state Eqs. (4), (12) can be re-written as

$$
J _ {\infty} (i, q, h) = \max _ {u} \left\{g (i, q, h, u) + \gamma \sum_ {t = 1} ^ {2} \sum_ {j = 1} ^ {1 5} P _ {q j i} ([ u ] _ {2}) \operatorname * {P r} (\epsilon = t) J _ {\infty} (j, t, H h + e _ {5} [ u ] _ {1}) \right\}\tag{13}
$$

where $e _ { 5 } = [ 0 , \ 0 , \ 0 , \ 0 , \ 1 ] ^ { T }$ and, for convenience, we have slightly abused the notation by writing the argument of J as $( i , q , h )$ instead of $x = [ i , q , h ^ { T } ] ^ { T }$ , and that of g as (i, q, h, u) instead of $( x = [ i , q , h ^ { T } ] ^ { T }$ uht), with $i = 1 , . . . , | S | , q = 1 , . . . , | \mathcal { C } | , h { \in } [ 0 , 1 ] ^ { 5 }$

<sup>¼ j jS ¼ j jC</sup>Notice that the reward function (9) as well as the state transitions Eq. (4) are linear in the fraction of pro<sup>fi</sup>ts to be concealed, $[ u _ { k } ] _ { 1 }$ , for all k. Thus, using an argument similar to that from [17], we can conclude that all the $J _ { k } ,$ as well as $J _ { \infty , }$ will be linear in $[ u _ { k } ] _ { 1 }$

Consequently, J will be maximized at the boundary of $[ u _ { k } ] _ { 1 } ^ { \prime } s$ feasible region, and the <sup>fi</sup>rm should follow a “bang-bang” policy of either $[ u _ { k } ] _ { 1 } = 0 \mathrm { o r } [ u _ { k } ] _ { 1 } = 1$ each year (we will have more to say about these extreme values shortly). This implies a signi<sup>fi</sup>cant reduction in computational complexity, because it will be suf<sup>fi</sup>cient to consider $h \in \{ 0 , 1 \} ^ { 5 }$ , and calculate (13) only on a <sup>fi</sup>nite set of $| { \boldsymbol { S } } | ^ { \cdot } | { \boldsymbol { C } } | ^ { \cdot } 2 ^ { 5 } = 8 6 9$ <sup>j jS jCj ¼</sup>states. The latter can be done in a straightforward manner using value iteration.

## 2.4. Parameter dependence

We are interested in determining the optimal expected reward's dependence on the main parameters of the tax system as described in the previous Section, including the tax rate, r, penalty factor, $\beta ,$ and closure cost, $\ell .$

For an annual closure probability $p _ { o } { \in } ( 0 , 1 )$ , the reward function (9) is decreasing in r, β and ‘. Moreover, the parameters $r , \beta$ and ‘ affect neither the state transitions (4) nor the probability distributions with respect to which the expectation is taken in Eq. (11). We conclude that the term $\mathbb { E } J _ { k + 1 }$ in Eq. (11) will be decreasing in r, β or $\ell ,$ for any $k ,$ <sup>þ</sup>and thus, based on [17], the same property will be shared by $J _ { \infty } .$

The effect of the probability of the closure option being offered, $p _ { o } ,$ on the value function depends on i) whether the <sup>fi</sup>rm's expected reward is higher if the option is offered, and if so, ii) whether it is better for the <sup>fi</sup>rm to use the option. If we assume the <sup>fi</sup>rm's state vector is $x _ { k } = [ j , 1 , h _ { k } ^ { T } ] ^ { T }$ , with $j = 1 1 , . . . , 1 5$ (i.e., the <sup>fi</sup>rm is not in a V or O Markov state, and closure is available), then the <sup>fi</sup>rm has a choice of either transitioning to a closure state (according to the probabilities in $( 7 ) )$ or taking its chances and perhaps being audited in the next period, with higher probability than if the option was not available at all. One can then check that, based on the rewards Eq. (9) and transition probabilities (8), the <sup>fi</sup>rm's expected reward by taking the option at some time k will be higher than that obtained by declining it, iff the probability of an audit, given that the <sup>fi</sup>rm forgoes the option while in the j-th Markov state, $P _ { 1 1 j } ( 2 )$ , satis<sup>fi</sup>es

$$
P _ {1 1 j} (2) \geq \theta (j, h _ {k}) \triangleq \frac {\ell \cdot (j - 1 0)}{r \cdot \left(\sum_ {i = 1} ^ {j - 1 0} [ h _ {k} ] _ {6 - i} + \frac {3}{5} \beta \sum_ {i = 1} ^ {j - 1 0} i [ h _ {k} ] _ {6 - i}\right)} \quad j = 1 1,..., 1 5,\tag{14}
$$

with $( j - 1 0 )$ being the number of years since the <sup>fi</sup>rm's last closure or audit event, and $h _ { k }$ the lower <sup>fi</sup>ve elements of the <sup>fi</sup>rm's state vector. Furthermore, if $P _ { 2 1 j } { \ge } \theta ( j , h _ { k } )$ as well (where $P _ { 2 1 j }$ is the probability of transitioning to an audit Markov state given that closure was not available), then saying $\ " \mathrm { y e s } \ "$ to closure is preferable to not having the option at all. Because the audit probability is increased if a <sup>fi</sup>rm is given the option and declines it (relative to the case where there was no option at all), i.e., $P _ { 1 1 j } ( 2 ) > P _ { 2 1 j } ,$ , it will always be advantageous for the <sup>fi</sup>rm to have (and use) the option if it would be willing to do so under the “usual” lower audit probabilities. On the other hand, if $P _ { 1 1 j } ( 2 )$ is below the threshold θ in (14) then so is $P _ { 2 1 j } ,$ , meaning that the <sup>fi</sup>rm's reward would be lower under the option if taking the option is more expensive than discarding it. In general, the threshold θ that makes the option desirable for the <sup>fi</sup>rm depends on the <sup>fi</sup>rm's state vector $( \mathrm { i . e . }$ , on the Markov state $, j ,$ it is in, and on its past history of decisions, $h _ { k } .$ However, there are choices for $\beta , \ell ,$ and r (including those in use today, discussed in the next section) which are of practical interest and lead to the option being to the <sup>fi</sup>rm's advantage uniformly, for any j and $h _ { k } .$

Based on the above discussion, if $P _ { 2 1 j } { > } \theta ( j , h _ { k } )$ along the optimal trajectory, then the <sup>fi</sup>rm will always say yes to closure, and having the option to do so is better than the alternative. In that case, the value functions $J _ { k }$ will be increasing in the closure probability, $p _ { o } ,$ for all k. To see why that is, notice that the reward function (9) is independent of $p _ { o }$ and of the actual availability of closure, $c _ { k } .$ Also, in terms of the state transitions $( 4 ) , p _ { o }$ only affects $P r ( \epsilon = 1 )$ (the probability of arriving at a state where the <sup>fi</sup>rm has the option to use closure) and none of the remaining elements of the state vector (in particular, $s _ { k } )$ on which the reward function depends. Thus, the term $\mathbb { E } J _ { k + 1 } ( A x _ { k } + B u _ { k } + n _ { k } )$ in (11) will be increasing in $p _ { o } ,$ because an in-<sup>þ</sup>crease in $p _ { o }$ simply corresponds to a higher probability of a more favorable outcome (namely closure). These facts imply [17] that the long-term optimal reward function $. J _ { \infty }$ will be increasing in $p _ { o }$ as well.

Using similar arguments, one can show that if either $P _ { 1 1 j } ( 2 )$ or $P _ { 2 1 j }$ are below the threshold (14), then the value function will be decreasing in $p _ { o }$ because in those cases $p _ { o }$ increases the probability of a lower-payoff event, while leaving the state transitions and reward function unaffected. Finally, in the extreme case where $p _ { o } = 0 ,$ the closure cost ‘ becomes irrelevant (since closure is never offered), while if $p _ { o } = 1$ and $P _ { 2 1 j } { > } \theta ( j , h _ { k } )$ , then the value function will be independent of $\beta$ (because the <sup>fi</sup>rm employs closure every year and will never be audited).

## 2.5. Assumptions and parameter selection

Our model includes a few assumptions which require justi<sup>fi</sup>cation. For simplicity, we will assume that the <sup>fi</sup>rm's annual pro<sup>fi</sup>t, R, is constant throughout its economic life. It is straightforward to allow R to rise at a steady rate, by manipulating the discount coef<sup>fi</sup>cient $\gamma ;$ the model could also be easily adapted to include any other pre-de<sup>fi</sup>ned growth pro<sup>fi</sup>le for R. In the following, we will assume an interest rate of 3%, corresponding to $\gamma = 1 / ( 1 + 0 . 0 3 ) = 0 . 9 7 0 9$

Regarding the choices of $[ R , [ u _ { k } ] _ { 1 }$ , and ‘, we will always refer to “relative” amounts, so that, for example, $R = 1 0 0 ,$ , and R $[ u _ { k } ] _ { 1 }$ is the percentage of year k pro<sup>fi</sup>t to be hidden from the authorities. We chose this approach for the following reasons. The <sup>fi</sup>rm's decisions are, of course, based on its true pro<sup>fi</sup>t, which the government does not know. Expressing the cost of closure, ‘, as a percentage of the <sup>fi</sup>rm's net pro<sup>fi</sup>t, and $[ u _ { k } ] \cdot$ <sub>1</sub> as the fraction of pro<sup>fi</sup>ts to be hidden, will make it easier to draw conclusions as to the effectiveness of tax measures and behavior of the <sup>fi</sup>rm. Furthermore, given an estimate of the size of the country's “hidden economy” (studies such as [13] place it at around 40% for Greece), the quantities computed by the model can be converted to estimates of absolute amounts.

Regarding the range of values for $[ u _ { k } ] _ { 1 } \in [ 0 , 1 ]$ , it may be impossible for a <sup>fi</sup>rm to systematically claim zero annual pro<sup>fi</sup>ts by overstating expenses and/or hiding income. There are several practical reasons for this, including pressure by shareholders or capital markets to demonstrate pro<sup>fi</sup>tability, and other safeguards in the accounting system, so that at least some income will be documented (e.g., via sales invoices which some clients will likely demand in the course of business). There are at least two possible approaches here. One is to set some upper bound $u _ { m a x } { < } 1$ , so that a <sup>fi</sup>rm with pro<sup>fi</sup>t R can never hide more than $u _ { m a x } R .$ This is meaningful in certain settings, but again requires knowledge – by the government – of the <sup>fi</sup>rm's true pro<sup>fi</sup>t. Instead, here we will allow $u _ { m a x } = 1$ , and interpret the model's results in a “marginal” sense: $[ u _ { k } ] _ { 1 } = 1$ simply means that the <sup>fi</sup>rm should hide as much of its pro<sup>fi</sup>t as possible, or that the next euro that could be hidden, should be hidden.

Our model can easily be used to examine the effects of applied tax rates and audit probabilities, however, these quantities will be kept <sup>fi</sup>xed to their estimated current levels. We do this in order to isolate the effect of tax-penalties and closure cost on the <sup>fi</sup>rm's behavior, and because, in the case of audits, an increase is not easy to implement (e.g., it may require hiring of new personnel, training, etc.). Because of space considerations, we discuss only income tax and ignore VAT collection and payments by the <sup>fi</sup>rm, which are subject to a separate mechanism and can be incorporated in the model at a later stage.

With respect to the audit probability distribution and closurerelated data, there is a scarcity of of<sup>fi</sup>cial reports. In order to demonstrate our model, we have estimated the various parameters of interest using other sources, including reports in the Greek <sup>fi</sup>nancial press, which suggest that audits can cover no more than approximately 5% of all <sup>fi</sup>rms in a given year, and that the cost of closure for the options offered during 1998–2008 was approximately 2–3% of pro<sup>fi</sup>ts for the average <sup>fi</sup>rm. Based on these, we assumed an overall audit probability of 0.05. This probability is distributed heavily (80%) towards <sup>fi</sup>rms with past tax declarations whose statute of limitations is about to expire, i.e., a 0.0025 probability that the <sup>fi</sup>rm audited is drawn from those with 1–4 years since their last audit or closure, and a 0.04 probability that it is one of those which have not been audited for <sup>fi</sup>ve years. Of course, the model can be easily adjusted to different parameter values at the hands of government entities which would have more precise knowledge of the parameters.

As we have already mentioned, the probability of an audit in creases when the <sup>fi</sup>rm rejects the option to use closure. That increase will depend on the number of <sup>fi</sup>rms which choose the option of closure, leaving the rest to increased scrutiny. There is little of<sup>fi</sup>cial data on this; here, we have used a rough estimate of 2/3 for the fraction of <sup>fi</sup>rms who opt to use closure, meaning that the audit probability is roughly tripled for those who don't. Arguably, the rate of participation is determined largely by expectations, whose dynamics are however, beyond the scope of this paper. Finally, we chose the annual probability of closure being offered to be ${ P r ( \epsilon = 1 ) = 0 . 2 }$ , because that value is near the current average. We opted for a probabilistic treatment of closure mainly for two reasons. One was that it is easily implementable in practice and makes for a tractable model. The other reason is that we would like to make comparisons between random vs. periodic closure. In Greece, there is a history of closure being offered quasi-periodically, roughly every 5 years (as the statute of lim itations on tax statements is about to elapse). One may hypothesize that this is anticipated by <sup>fi</sup>rms which may alter their policy to take advantage. As our numerical experiments will show, this can indeed happen and it is best for the government to not allow <sup>fi</sup>rms to anticipate when the option will be offered (in fact, it seems best not to offer it at all).

## 3. Running the model: results and discussion

We implemented our model as a MATLAB-based application, and obtained results on a series of scenarios of practical importance, regarding the effect of tax penalties and the closure option on <sup>fi</sup>rm behavior and government revenues. The MATLAB code is included in Appendix B. The experiments described below are arranged based on whether the closure option is: i) stochastically available $\left( p _ { o } = 0 . 2 \right)$ , ii) always available $( p _ { o } = 1 )$ , iii) never available $( p _ { o } = 0 )$ and iv) available every <sup>fi</sup>ve <sup>fi</sup>scal years, where for the latter scenario the basic model was modi<sup>fi</sup>ed so that $P r ( \epsilon _ { k } = i )$ was periodic in $k .$ In each case, we kept the tax rate and audit probabilities <sup>fi</sup>xed, and allowed the closure cost to vary in the range between $\ell = 0 . 0$ and $\ell = 0 . 5 0 ,$ <sup>¼</sup>, in increments of 0.01 (values beyond 0.50 are not consid-<sup>¼</sup>ered realistic, given the current tax rate of $r = 0 . 2 4 )$ . In that range, we determined a kind of boundary, (in the tax penalty–closure cost space) at which the behavior of the <sup>fi</sup>rm changes from being dishonest in every feasible<sup>3</sup> state, to being honest in a) at least one feasible state, and b) in all feasible states. We will refer to these as the total and partial honesty boundaries, respectively. We are also interested in the boundary at which the <sup>fi</sup>rm's policy changes from always using the option, to discarding it, in a) at least one feasible state and b) in every feasible state, for a range of tax penalty coef<sup>fi</sup>cients. For simplicity, we absorbed the $3 / 5 \cdot$ “prompt payment” discount factor in (9) into the per annum tax penalty coef<sup>fi</sup>cient, $\beta .$ Thus any tax penalty multipliers discussed henceforth are $\ " \mathrm { n e t } \ "$ (after discount) values. In order to study the effects of tax penalties over a wider range, we have “removed” the 200% upper bound on accumulated tax penalties which is in place today, as discussed in Section 1, and considered the range from $\beta = 0 . 1 4 4$ (the current level, after discount), to $\beta = 4 ,$ or 400%, in increments of 0.05.

![](/api/attachments/WSHMUN7N/fulltext/images/0e4913d12877849d73fe2cd35f761e7c759fab0e0f53fcf5baec08da652d941e.jpg)  
Fig. 2. Partial (dashed) and total (solid) tax penalty, honesty boundaries when the closure option is available with probability 0.2 each year. The <sup>fi</sup>rm uniformly chooses a policy of maximum tax evasion in the light gray area, and always declares all pro<sup>fi</sup>ts in the white area. In the dark gray region the <sup>fi</sup>rm's policy is state-dependent.

## 3.1. Stochastically available option

In this case, the <sup>fi</sup>rm does not know a priori whether closure will be available but does know the corresponding probability distribution, which is set to $p _ { o } = 0 . 2$ each year. Fig. 2 shows the output of our model, in the form of the total honesty boundary over which the <sup>fi</sup>rm declares 100% of its pro<sup>fi</sup>t in all feasible states (white area) and the partial honesty boundary below which the <sup>fi</sup>rm declares as little pro<sup>fi</sup>t as possible (light gray area). In the dark gray area between the two boundaries, the <sup>fi</sup>rm's policy is state-dependent. The <sup>fi</sup>rst group of states at which the <sup>fi</sup>rm alters its behavior as the tax penalty rises from very low values are those for which $s = 1 5$ and $s = 1 4 ,$ i.e., the <sup>fi</sup>rm is in the $N _ { 5 }$ or $N _ { 4 }$ Markov state — unaudited for at least four years, with no closure-option at her disposal. On the other hand, the last states to $" S W i t c h "$ to honest behavior as we cross the upper boundary in Fig. 2 are those with $s = 1 1$ , where the <sup>fi</sup>rm is in $N _ { 1 } -$ audited one year ago. In the area between the two boundaries, the <sup>fi</sup>rm is honest in at least one feasible state.

![](/api/attachments/WSHMUN7N/fulltext/images/19ec7112a45874a8ad1ee351638357cb5b25efd155b17f76c4f50094fe19da62.jpg)  
Fig. 3. Partial (dashed) and total (solid) option usage boundaries when the option is available with probability 0.2 each year. The option is used always at points below the lower boundary (light gray area), never at points above the upper boundary(white area).

We notice that as the closure cost, ‘, approaches the current tax rate, the tax penalty multiplier required to enforce total honesty declines from 11.8 to 3.5 (i.e., 350% of back taxes owed), and remains constant for higher values of ‘. For the same range of ‘, the partial honesty boundary declines from $\beta { = } 9 . 6 ~ \mathrm { t o } ~ \beta { = } 1 . 6$ . We observe that both boundaries are situated well above the current net penalty coef-<sup>fi</sup>cient (approximately 0.14), even for relatively high closure costs. This agrees with the widely accepted assessment that tax evasion in Greece is high in part because the current combination of $\ell , \beta ,$ and audit probabilities are ineffective. In that case, the option provides <sup>fi</sup>rms with a less costly way of settling their tax obligations. We will have more to say about this in a moment.

Fig. 3 illustrates the appeal of closure to the <sup>fi</sup>rm. Points below the lower boundary (light gray area) correspond to option cost/tax penalty combinations where it is optimal for the <sup>fi</sup>rm to use the option in every feasible state. Between boundaries (dark gray area), the <sup>fi</sup>rm ignores the option in at least one feasible state. Finally, above the upper boundary (white area), the <sup>fi</sup>rm never uses the option. The lower boundary, separating the areas of total ${ \tt V S } .$ partial option acceptance, indicates the highest percentage of net pro<sup>fi</sup>t that a <sup>fi</sup>rm would be willing to pay always in order to “lock in” past gains earned through tax evasion. At today's tax penalty of $\beta = 0 . 1 4$ , the <sup>fi</sup>rm should be willing to pay up to approximately $\ell = 0 . 0 5$ , or 5% of its net pro<sup>fi</sup>t, i.e., well above the current estimate of $2 - 3 \% .$

The upper boundary of Fig. 3, beyond which the <sup>fi</sup>rm never makes use of the option, also rises in steps, from approximately $\ell = 0 . 0 7$ when $\beta = 0 ,$ <sup>¼</sup>, to almost 0.32 when β reaches 1.3. This indicates how much of a closure cost the <sup>fi</sup>rm is willing to accept as the tax penalty increases, as long as tax evasion remains its most pro<sup>fi</sup>table choice. For even higher tax penalties the upper boundary declines similar to the lower boundary; this is because (see also Fig. 2) tax evasion becomes pro<sup>fi</sup>table in fewer and fewer states, and thus the <sup>fi</sup>rm is willing to pay gradually less in order to avoid a possible audit.

## 3.2. Option available every fiscal year

There is a set of <sup>fi</sup>rms and freelancers in Greece, that settle their tax-obligation solely through closure every year. In this case the closure option is called “self-assessment”. We examined the effectiveness of this policy, in terms of the government's and <sup>fi</sup>rm's expected earnings. In that case our model indicated that the partial and total honesty boundaries are situated at more than 12 times the uncollected taxes. Such a tax penalty seems unrealistic; it appears therefore that tax evasion cannot be curbed under this scenario unless the audit mechanism is signi<sup>fi</sup>cantly reinforced. This argues against the frequent use of the closure option as a revenue collecting mechanism.

![](/api/attachments/WSHMUN7N/fulltext/images/383d5c8d5055105b585b1bf3b13903cedb51fce4b1d8c5cdfada8fb6ad7f2da5.jpg)  
Fig. 4. Partial (dashed) and total (solid) option usage boundaries when the option is available every year. The option is used always at points below the lower boundary (gray area), and never at points above the upper boundary (white area). In the dark gray region the <sup>fi</sup>rm's policy is state-dependent.

The lower boundary of total-to-partial option appeal (see Fig. 4) increases from approximately $\ell = 0 . 0 7 \ \mathrm { t } 0 \ \ell = 0 . 3 2$ for a range of β between 0 and 3.3, followed by a slight decrease to ‘ 0:28 for $\beta = 4 .$ In <sup>¼</sup>the light gray region, it is optimal for the <sup>fi</sup>rm to use the option every year. The upper threshold, over which the <sup>fi</sup>rm refuses the option, rises in steps from $\ell = 0 . 0 7$ to $\ell = 0 . 3 6$ for the range of β between 0 and 2.65, followed by a decrease to $\ell = 0$ :34 when $\beta = 3 . 9$ indicating <sup>¼</sup>that the <sup>fi</sup>rm is willing to accept higher closure costs as long as that cost remains lower than the current tax rate. Overall, our model suggests that if the option is offered every year, enforcing honesty via suf<sup>fi</sup>ciently high tax penalties may be infeasible, while for a modest range of tax penalty coef<sup>fi</sup>cients most <sup>fi</sup>rms would not make use of the closure option.

## 3.3. The option is never available

If the closure option is never offered by the government, tax evasion persists in every feasible state at today's tax penalty rates. In order to make “full disclosure” an optimal policy for the form in at least one feasible state, the tax penalty needs to be approximately $\beta { = } 1 . 7 \ ( \mathrm { i } . { \bf e } . ,$ a 170% annual tax penalty rate on back taxes owed). The <sup>fi</sup>rst feasible states in which the <sup>fi</sup>rm turns honest as β rises are those with $s = 1 5$ and $s { = } 1 4$ (those with four or more years unaudited). When $\beta = 4 . 9 $ , the <sup>fi</sup>rm becomes honest in every feasible state, the last group of states to “switch” being those with $s = 1 1$ (Markov state $N _ { 1 } )$ . Thus, in the absence of a closure option, the <sup>fi</sup>rm's optimal policy with today's parameters is to evade taxes, however the tax penalties required to change that are considerably lower than when the option is offered frequently.

## 3.4. Option available in five year time intervals

In the case where <sup>fi</sup>rms may guess that the government will offer the option periodically in an effort to collect revenue from past years whose statute of limitations is about to expire (as is likely to be the case in Greece, given the recent history),the situation is similar to that when the option is offered annually. In particular, the tax penalty thresholds for partial or total honesty, exceed 12 times the amount of uncollected taxes, and the <sup>fi</sup>rm's optimal policy is identical to that of Section 3.2, i.e., conceal pro<sup>fi</sup>ts when possible and use the closure option when available.

![](/api/attachments/WSHMUN7N/fulltext/images/96187e0f5e6f8b0aff13c9d43c864767286cf72017c0a63d83c5050e9aced2dc.jpg)  
Fig. 5. Partial (dashed) and total (solid) option usage boundaries when the option is available in <sup>fi</sup>ve-year intervals. In the light gray area the option is used in every feasible state. At points above the upper boundary (white area) the option is never used. In the dark region the firm's policy is state-dependent

Fig. 5 illustrates the appeal of closure to the <sup>fi</sup>rm. The percentage of net pro<sup>fi</sup>t that a <sup>fi</sup>rm would be willing to pay for using the option at (at least) one feasible state increases from ‘ 0:04 to ‘ 0:19 for β ranges between 0 and 1.85, suggesting that the government cannot hope to collect amounts that are much higher than what it can obtain today. Above $\beta = 1 . 8 5$ the lower boundary declines to $\ell = 0 . 1 7$ for $\beta = 4 .$ In this set of states (those with $s = 1 5 )$ <sup>¼</sup>, the <sup>fi</sup>rm is willing to pay a progressively higher closure cost(as long as that cost remains lower than the current tax rate). The same set of states also determine the upper boundary of Fig. 5; in order for the <sup>fi</sup>rm to stop employing the closure option, ‘ must increase from approximately $\ell = 0 . 0 7$ to $\ell = 0$ :36 for β ranging between 0 and 1.55. Beyond this range the upper boundary decreases gradually to $\ell = 0 . 2 7$ for $\beta = 4 .$

## 3.5. Comparing government vs. firm expected revenues

Assuming that the <sup>fi</sup>rm is risk-neutral, with an in<sup>fi</sup>nite economic life, and that it employs an optimal tax evasion and option usage strategy, we computed (via Eq. (13)) the present value of the expected <sup>fi</sup>rm revenues and government tax revenues per <sup>fi</sup>rm, for each of the scenarios discussed previously. The results are listed in Table 1, in terms of % of the <sup>fi</sup>rm's annual pro<sup>fi</sup>t, and assume that future revenues are discounted assuming again a 3% rate of in<sup>fl</sup>ation.

We observe that the <sup>fi</sup>rm maximizes its expected revenues in the case where the option is available every year; that is the worst-case scenario from the point of view of the government. Tax revenue improves gradually if the option is offered periodically every <sup>fi</sup>ve years or 20% of the time, with the highest revenue collected when the option is not offered at all. Offering the option periodically (last line of Table 1), and thus allowing <sup>fi</sup>rms to anticipate closure, leads to a higher tax revenue than if the option was offered each year. Intuitively, this is explained by the fact that the optimal policy in both cases is $u = [ 1 , 1 ] ^ { T }$ uniformly, i.e., always take advantage of the option and hide all pro<sup>fi</sup>t. Consequently, the <sup>fi</sup>rm will pay the same amount for closure in either case (either yearly or as a lump sum every <sup>fi</sup>ve years). However, if closure occurs every <sup>fi</sup>ve years, the <sup>fi</sup>rm is exposed to a small probability of an audit between closures, so its long-term expected income is slightly less than if it could use closure yearly and never be audited. These <sup>fi</sup>gures support the argument that, in the current state of affairs, the closure option is appealing to <sup>fi</sup>rms, and that it is not a productive revenue collecting mechanism: it limits the effectiveness of tax penalty as a tax-deterrent, and promotes tax evasion by providing a cheaper alternative to tax compliance.

The results for the “no-option” scenario suggest that tax penalties would be an important part of the tax revenue collected in that case, since it is optimal for the <sup>fi</sup>rm to conceal as much of its pro<sup>fi</sup>t as possible. However, it may be argued that the government will sometimes encounter dif<sup>fi</sup>culties in actually collecting tax penalties and back taxes owed in the event of an audit (e.g., the <sup>fi</sup>rm may ultimately be unable to pay because of bankruptcy or other reasons). We adjusted the basic model so as to take this alternative into consideration. Although there are no of<sup>fi</sup>cial data on the percentage of audits which result in an inability to collect, we estimate this <sup>fi</sup>gure to be approximately 60%, based on recent discussions in the Greek parliament about the percentage of long-term overdue taxes the government considered uncollectable in 2010. In that case, when the <sup>fi</sup>rm applies its optimal policy as before, the expected government revenues in the right column of Table 1 decrease to 106.9 (option never available), to 92.99 (option given 20% of the time), 98.54 (option given every <sup>fi</sup>ve years). The <sup>fi</sup>gure for the “option always available” scenario remains at 74.8, because in that case the <sup>fi</sup>rm uses the option every year, and is never audited. The best scenario for the government is still to never offer the option, followed by offering it periodically, while the worst-case scenario is again to offer it every year. The tax revenue gap between best (from the point of view of the government) two cases becomes narrower as the government is the percentage of uncollected back taxes and penalties increases. Once the effectiveness of the collection mechanism is reduced below 45%, then the highest tax revenue is obtained by always offering the option.

Comparison of expected <sup>fi</sup>rm and government revenues under different option availability scenarios, with $r = 0 . 2 4 , \beta = 0 . 2 4 , \ell = 0 . 0 2 3$ and a 5% overall audit probability. <sup>¼</sup>Numbers are expressed in % of the <sup>fi</sup>rm's annual pro<sup>fi</sup>t, discounted at a 3% annual rate of in<sup>fl</sup>ation. The <sup>fi</sup>gures for the last scenario (“every <sup>fi</sup>ve years”) are for an initia state of $\dot { \boldsymbol { x } } = [ 1 1 , 2 , 0 , 0 , 0 , 0 ,$ 1]<sup>T</sup>, i.e., the <sup>fi</sup>rm hid all its pro<sup>fi</sup>t since its last closure, 1 year ago, and has no closure option at its disposal for the next 4 years

<table><tr><td>Option availability</td><td>Expected firm profit (net)</td><td>Expected Government Revenue per firm</td></tr><tr><td>Never available</td><td>3254.6</td><td>178.7</td></tr><tr><td>Stochastic (20%)</td><td>3307.9</td><td>125.3</td></tr><tr><td>Always available</td><td>3358.3</td><td>74.8</td></tr><tr><td>Every five years</td><td>3313.9</td><td>120.2</td></tr></table>

The fact that, in Table 1, <sup>fi</sup>rm revenues in increase for higher probabilities of the closure option being offered, is not coincidental. Based on the parameter values used here (as per our estimates discussed in Section 2.5), we veri<sup>fi</sup>ed that the audit probabilities with no option available, as well as when the option is given and the <sup>fi</sup>rm declines it, are greater than the threshold (14), for all j and for any choice of disclosure history, $h _ { k } .$ Thus, (see discussion in Section 2.4), the <sup>fi</sup>rm's long-term expected reward will be increasing in the probability of closure being available, $p _ { o } .$ Fig. 6 shows the corresponding (decreasing) government tax revenues.

Finally, the problem discussed here can be viewed as a zero-sum game between the government (which may or may not offer closure) and the <sup>fi</sup>rm (which chooses whether to conceal its pro<sup>fi</sup>ts). In that setting, $p _ { o }$ and [u] represent the government's and the <sup>fi</sup>rm's mixed strategies, respectively. Although a full game-theoretic analysis is beyond the scope of this paper, the results presented here are suggestive of an equilibrium at $p _ { o } = 0$ (never offer the option) and $[ u ] _ { 1 } = 1$ (always conceal as much pro<sup>fi</sup>t as possible) under the parameters in place today. That is because, at $p _ { o } = 0$ , the government cannot unilaterally improve its revenue by raising $p _ { o }$ when the <sup>fi</sup>rm acts optimally for itself (the <sup>fi</sup>rm's value function is increasing in $p _ { o } ,$ so that raising $p _ { o }$ causes the government to loose some revenue); at the same time, maximal tax evasion is optimal for the <sup>fi</sup>rm when $p _ { o } = 0$

## 4. Conclusions

We have described a decision support model for exploring the problem of tax evasion and revenue collection in Greece. The model, formulated as a Markov decision process, i) incorporates the basic features of the Greek tax system and its effect on the decisions made by <sup>fi</sup>rms regarding whether or not to conceal their pro<sup>fi</sup>ts, and ii) includes a relatively unconventional revenue collection tool which is used in Greece and gives <sup>fi</sup>rms a “closure option” which effectively “erases” part of their past tax behavior, in exchange for payment. Under our approach, the parameters on which a <sup>fi</sup>rm's optimal policy depends are: the tax rate, the probability of being audited, the tax penalty for undeclared pro<sup>fi</sup>ts, the probability of the closure option being offered, and the cost of closure. Given these, our model computes (via dynamic programming) the optimal decisions for a rational, risk-neutral <sup>fi</sup>rm, which seeks to maximize its long-term revenue by potentially concealing its pro<sup>fi</sup>ts from authorities and/or using the closure option to protect itself from audits and penalties.

![](/api/attachments/WSHMUN7N/fulltext/images/d9c8ea63ce082e182d59ac264221e447369a6970eb13907508b9e2909f7dd84d.jpg)  
Fig. 6. Expected tax revenues versus probability of closure being offered each year, assuming the <sup>fi</sup>rm employs its optimal policy regarding the fraction of its pro<sup>fi</sup>ts that it hides.

As expected, the <sup>fi</sup>rm's optimal value function is decreasing in the tax penalty coef<sup>fi</sup>cient, the tax rate and the cost of closure. In general, its monotonicity with respect to the probability of closure depends on the parameters mentioned above, as well as the <sup>fi</sup>rm's policy of tax evasion. However, for the parameter values currently used in Greece, the value function is increasing in the probability of closure being offered, independently of the <sup>fi</sup>rm's policy on tax evasion. This implies that a higher likelihood of the option being offered leads to a decrease in tax revenues.

As a consequence of risk-neutrality, the <sup>fi</sup>rm's optimal policy is “bang-bang”, i.e., either declare or conceal all pro<sup>fi</sup>ts. The mapping from states to tax evasion decisions is generally parameterdependent. However, the parameter space contains regions where the <sup>fi</sup>rm's decision is constant with respect to its state. We used the proposed model to “chart” these regions in the closure cost vs. tax penalty space, for the current tax system in Greece. The boundaries between regions are important because they de<sup>fi</sup>ne a locus of tax parameters which separate tax evasion from honest behavior on the part of the <sup>fi</sup>rm, and may thus be used to guide tax policy decisions.

Regarding the situation in Greece, the numerical results obtained from our model suggest that the combination of tax penalties, audit probabilities and closure costs is such that the <sup>fi</sup>rm has an incentive to evade taxes to the maximum extent possible. Given the cost associated with mounting additional audits, the way to enforce honesty might be to raise tax penalties. However, the presence of a relatively cheap closure option means that the required tax penalties must be unrealistically high. Unless the remaining parameters are altered, the existence of the option reduces tax revenues and reinforces the incentive for tax evasion. That is because, despite the fact that the government may be able to collect additional revenue by making the option slightly more expensive, its use gives <sup>fi</sup>rms a cheaper alternative to regular tax payments. Thus, closure effectively rewards cheaters and does not seem to be a sound revenue collection tool. From a tax revenue viewpoint, closure makes sense only if the government is unable to collect a signi<sup>fi</sup>cant portion (over 50%) of back taxes and tax penalties owed.

There are several extensions of this work which we are currently exploring. One has to do with the inclusion of variations in the tax rates and a VAT collection/audit mechanism. VAT must be paid periodically by the <sup>fi</sup>rm (every three months) and is subject to audits which are semi-independent from those for the <sup>fi</sup>rm's annual tax statements and carry their own penalties. Our model could be augmented to include VAT-compliance states and some “coupling” with the regular audit process, so that, for example, non-payment of VAT raises the probabilities of the <sup>fi</sup>rm having its main tax declaration audited.

We are also interested in the differentiation between large (e.g., publicly traded) and small entities, and their tax evasion behavior, as well as in policies that take into consideration a <sup>fi</sup>rm's riskaversion via the introduction of an appropriate utility function. Given an estimate of the cost of a tax audit, one could then revisit the problem by asking that audit probabilities and penalties be such that the system can at least pay for itself (see e.g., [16]), in addition to avoiding excessive penalties that would mean the end of the <sup>fi</sup>rm.

Finally it would be interesting to formulate the problem examined here as a robust control problem, where the <sup>fi</sup>rm optimizes its revenue by viewing the government's choices as a random disturbance. In that setting, one could “lift” the assumption of stochastic option availability, and instead consider any sequence of choices on behalf of the government regarding the closure option, with the <sup>fi</sup>rm planning for the worst.

## Appendix A. Markov transition matrices

<table><tr><td rowspan="14"> $M_{no} =$ </td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0025</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0025</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.04</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0.9975</td><td>0.9975</td><td>0.9975</td><td>0.9975</td><td>0.9975</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.9975</td><td>0.9975</td><td>0.9975</td><td>0.9975</td><td>0.9975</td><td>0.9975</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.9975</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.9975</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.96</td><td>0.96</td></tr></table>

A:1

Table A.2. Transition probabilities $M _ { n o } \mathrm { : }$ closure is not available

$$
M _ {a} = \left[ \begin{array}{c c c c c c c c c c c c c c c} 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} \\ 0 & 0 & 0 & 0 & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} \\ 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & \text {空} & \text {空} & \text {空} \\ 0 & 0 & 0 & 0 & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} \\ 0 & 0 & 0 & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} \\ 0 & 0 & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} & \text {空} \\ 0 & 0 & \text {空} & \text {空} & \text {空} \\ 0 & 0 & \text {空} & \text {空} \\ 0 & 0 & \text {空} \\ 0 & 0 \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \\ 0 & \text {空} \end{array} \right]\tag{A.2}
$$

Table A.3. Transition probabilities M : closure is available and the <sup>fi</sup>rm decides to use it.

$$
M _ {d} = \left[ \begin{array}{c c c c c c c c c c c c c c c} 0. 0 0 7 5 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0. 0 0 7 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0. 0 0 7 5 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0. 0 0 7 5 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \end{array} \right]\tag{A.3}
$$

Table A.4. Transition probabilities $M _ { d } \mathbf { : }$ closure is always available and the <sup>fi</sup>rm declines it.

## Appendix B. MATLAB code

%%%%%%%%%%%%%%%%%FILEmdp-tax.m %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

```matlab
%This file handles the case of a stochastically available option.
%It computes the firm's maximum long-term expected rewards and optimal decisions
%with respect to tax evasion and use of the closure option (when the latter
%is available), starting from every possible state with a binary-valued (i.e.,
% all-or-nothing) 5-year history of tax evasion (see eq. 13).
%
%OUTPUT: The last row of the matrix Jk contains the firm's rewards starting from
% each possible state. The last row of Sk contains the corresponding
% government revenues (if DOGOV has been set to 1).
% States are identified with columns of Jk and Sk by lexicographic order.
% See functions nexti.m and column2state.m for computing the correct column
% number given the firm's state (s,c,h), and vise versa.

clear all

global Jk
%Firm reward matrix (eq. (11)). Jk will be filled in by row using
%value iteration. Columns of Jk will correspond to firm states (see
%discussion in Section 2.3).

global Sk %Similar to Jk but for Government revenues.

global PERIODIC
%BOOLEAN set to indicate whether the option is offered
%periodically. This file is designed to work with
%PERIODIC=0 ONLY.
PERIODIC=0; %This file is tailored to NON-periodic option.

global v %Probability of closure being available each year.
v=0.2; %Set closure probability (v=1 means closure always available)

global gam
gam=1/(1+0.03); %Gamma - discount factor

global DOGOV
DOGOV=0; %Set to 1 to compute government revenues explicitly. Useful if
%one wishes to take into account complications such as the
%government being unable to collect a portion of the tax owed
%(see discussion in Sec. 3.5)

%Tax parameters (Sec. 2.3)
global R %Firm annual revenue
R=100;
global r
r=0.24; %tax rate
global b
b=0.24; %0.24; %xxx tax penalty rate
global l
l=0.023;% closure cost as a fraction of firm's annual revenue

Nstates=15*2*2^5;
%number of discrete states on which the firm's reward will be computed
eps=0.01; %convergence threshold
Jk=zeros(1,Nstates);
Sk=Jk;
uopt=Jk; %holds optimal decision with respect to tax evasion at each state
aopt=Jk; %holds optimal decision with respect to closure usage

%% Begin Value Iteration

converged=0; %Boolean flag
k=1; %initialize the 1st row of Jk
for i=1:Nstates %fill in rewards for all states
    %The state (see eq. 4) is a 7-tuple (s, c, h) where h is 5-dimensional.
    %Determine which 7-tuple the counter i corresponds to.
    s=floor((i-1)/(2*2^5))+1; %Markov state
    c=floor(mod(i-1,2*2^5)/(2^5))+1; %Closure availability
    hs=mod(i-1,2^5); %now form history vector, h
    hs=dec2bin(hs,5);
    h=zeros(5,1);
    for j=1:5
    h(j)=str2num(hs(j));
    end
```

```matlab
%compute rewards/gov.revenues with no history of tax evasion by the
%firm
Jk(i)=g(s,c,h,0);
Sk(i)=ggov(s,c,h,0);

end

while (converged==0)
    k=k+1 %fill in a new row of Jk, Sk
    tempFirm=zeros(1,Nstates);
    tempGov=tempFirm;
    %compute firm & government rewards, optimal decisions for all states
    for j=1:Nstates
    [tempFirm(j), tempGov(j), uopt(j), aopt(j)]=expreward(j,k);
    end
    %Append new rows to Jk, Sk
    Jk=[Jk; tempFirm];
    Sk=[Sk; tempGov];
    %display firm reward corresponding to the state x_k=(1,2,[0 0 0 0 0]')
    %i.e., starting from an audit, no option available, clean history
    %Jk(k,1)
    Jk(k,33)
    uopt(33)

%find nr of states in which firm is evading / using option.
    [evade, useoption, nrfeas, afeas]=checkfeasible(uopt,aopt)

    %check for convergence
    maxdiff=max(abs(Jk(k,:)-Jk(k-1,:)))
    if (maxdiff)<eps
    converged=1;
    end

end

fprintf(1,'firm rewards=%f\n',Jk(k,33));
fprintf(1,'gov.t. rewards=%f\n',100*1/(1-gam)-Jk(k,33));

%%%/%,%/%/%/%/%/%/%% end of FILE mdp_tax.m %,%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%%
%%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%($)%$$
%$See description of mdp_tax.m
%mddperiodic_tax.m operates in a similar manner but is tailored to the case where

%the option is available periodically.

clear all
global Jk
%Firm reward matrix (eq. (11)). Jk will be filled in by row using
%value iteration. Columns of Jk will correspond to firm states (see
%discussion in Section 2.3).

global Sk %Similar to Jk but for Government revenues.

global PERIODIC
%BOOLEAN set to indicate whether the option is offered
%periodically. This file is designed to run with
%PERIODIC=1 option ONLY.
PERIODIC=1;

global CLOSURE_PERIOD
CLOSURE_PERIOD=5; %period for closure option

%global v %Probability of closure being available each year.
%v=1; %Set closure probability (v=1 means closure always available)

global gam
gam=1/(1+0.03); %Gamma - discount factor

global DOGOV
DOGOV=0; %Set to 1 to compute government revenues explicitly. Useful if
%one wishes to take into account complications such as the
%government being unable to collect a portion of the tax owed
%(see discussion in Sec. 3.5)
```

```matlab
%Tax parameters (Sec. 2.3)
global R %Firm annual revenue
R=100;
global r
r=0.24; %tax rate
global b
b=0.24; %tax penalty rate
global l
l=0.023;% closure cost as a fraction of firm's annual revenue

Nstates=15*2*2^5;
eps=0.01;

Jk=zeros(1,Nstates); ful if
Sk=Jk;
uopt=Jk;
aopt=Jk;

converged=0;
k=1; %initialize the first row of Jk

for i=1:Nstates %fill in rewards for all states
    %determine which state x_k=(s,c,h) j corresponds to
    s=floor((i-1)/(2*2^5))+1;
    c=floor(mod(i-1,2*2^5)/(2^5))+1;
    %hs=mod(i-1,2^5);
    %hs=dec2bin(hs,5);
    %h=zeros(5,1);
    %for j=1:5
    % h(j)=str2num(hs(j));
    %end
    Jk(i)=g(s,c,[0 0 0 0 0]',0);
    Sk(i)=ggov(s,c,[0 0 0 0 0]',0);

end

%initialize the remaining time steps within the 1st period
for q=2:CLOSURE_PERIOD
    k=k+1;
    Jk(q,:)=Jk(1,:);
    Sk(q,:)=Sk(1,:);

end

%Apply value iteration
while (converged==0)

    %for a 5-year period, fill 5 rows of Jk
    for q=1:CLOSURE_PERIOD
    k=k+1 %add a row
    tempFirm=zeros(1,Nstates);
    tempGov=tempFirm;

    for j=1:Nstates %fill in rewards for all states
    [tempFirm(j), tempGov(j), tempu(j), tempa(j)]=expreward(j,k);
    end

    Jk=[Jk; tempFirm];
    Sk=[Sk; tempGov];
    uopt=[uopt; tempu];
    aopt=[aopt; tempa];

end

%compare rows k to k-5.
maxdiff=max(abs(Jk(k-CLOSURE_PERIOD+1:k,:)-Jk(k-2*CLOSURE_PERIOD+1:k-CLOSURE_PERIOD,:)))
```

```matlab
%display firm reward from state x_k=(1,1,[0 0 0 0 0])';
Jk(k,33)
%Sk(k,33)
if maxdiff<eps
    converged=1;
end

end

%display firm and gov't rewards when the firm begins from state
%x_k=(11,2,[0 0 0 0 1]), i.e., the firm hid all its profits since
%its last closure, 1 year ago, and has no closure option at its disposal
%for the past 4 years.
fprintf(1,'firm rewards=%f\n',Jk(k,nexti(11,2,[0 0 0 0 1]'));
fprintf(1,'gov.t. rewards=%f\n',100*1/(1-gam)-Jk(k,nexti(11,2,[0 0 0 0 1]')));

%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%*****%<nl>%
%Function expreward(i,k)
%INPUTS: index i of a column in the reward matrix Jk
%
%
k: stage of value iteration
%OUTPUTS: er: firm's expected reward
%
egovr: gov't expected revenue
%
u1,u2: firm's optimal decisions (tax evasion, closure usage).
function [er, egovr, u1, u2]=expreward(i,k)

global gam
global DOGOV

%The firm's state is a 7-tuple (see eq. 3).
%Determine which 7-tuple i corresponds to
[s,c,h]=findstate(i);

%determine expected reward under decision u

%reward function is independent of c - closure state, so we can just
%evaluate it before hand and use it whether c=1 or c=2
g0=g(s,c,h,0);
g1=g(s,c,h,1);

if (c==2) %no option available
    %compute expected value with u1=0 or u1=1
    %CASE 1: no tax evasion, i.e., u1=0; u2=1;
    [firmrev govrev]=expval(s,c,h,k,0,1);
    er0=g0+gam*firmrev; %add using discounting
    if (DOGOV) %work out government revenue explicitly
    egr0=ggov(s,c,h,0)+gam*govrev;

    else
    egr0=0;
    end

    %CASE 2: Max. tax evation, i.e., u1=1; u2=1;
    [firmrev govrev]=expval(s,c,h,k,1,1);
    er1=g1+gam*firmrev;
    if (DOGOV)
    egr1=ggov(s,c,h,1)+gam*govrev;
    else
    egr1=0;
    end

    %find maximum, record optimal decision
    values=[er0,er1];
    gvalues=[egr0, egr1];
    [er, u1]=max(values);
    egovr=gvalues(u1);
    u1=u1-1; %convert index (1 or 2) to 0 or 1.
    u2=0; %there is no option to consider
```

```matlab
else
    if (c==1) %c=1, option available

    %compute exp. reward with u1=0 or u1=1, while TAKING THE OPTION
    %u1=0;
    %u2=1;
    [firmrev govrev]=expval(s,c,h,k,0,1);
    er01=g0+gam*firmrev;
    if (DÓGOV)
    egr01=ggov(s,c,h,0)+gam*govrev;
    else
    egr01=0;
    end

    %u1=1; u2=1;
    [firmrev govrev]=expval(s,c,h,k,1,1);
    er11=g1+gam*firmrev;
    if (DÓGOV)
    egr11=ggov(s,c,h,1)+gam*govrev;
    else
    egr11=0;
    end

    %compute exp val with 0 or 1, while REJECTING THE OPTION
    %u1=0; u2=2;
    [firmrev govrev]=expval(s,c,h,k,0,2);
    er02=g0+gam*firmrev;
    if (DÓGOV)
    egr02=ggov(s,c,h,0)+gam*govrev;
    else
    egr02=0;
    end

    %u1=1; u2=2;
    [firmrev govrev]=expval(s,c,h,k,1,2);
    er12=g1+gam*firmrev;
    if (DÓGOV)
    egr12=ggov(s,c,h,1)+gam*govrev;
    else
    egr12=0;
    end

    %pick the best value, record decisions for u1, u2 values=[er01 er11 er02 er12];
    govvalues=[egr01 egr11 egr02 egr12];
    [er, idx]=max(values);
    egovr=govvalues(idx);
    u1=mod(idx-1,2);
    u2=floor((idx-1)/2)+1;
    else
    fprintf(1,'Oops...\n');

    pause;
    end
end

%The firm's state is a 7-tuple (see eq. 3).
%This function takes as input an integer i corresponding
%to a column of Jk, uopt, or aopt, and determines which 7-tuple
%corresponding to that column
function [s c h]=findstate(i)

s=floor((i-1)/(2*2^5))+1;
c=floor(mod(i-1,2*2^5)/(2^5))+1;

hs=mod(i-1,2^5);
hs=dec2bin(hs,5);
h=zeros(5,1);
for j=1:5
    h(j)=str2num(hs(j));
end

%
```

%%%%%%%%% F1LE expva1.m %%%%%%%%%%%%%%%%%%%%%

```matlab
%Function expval(s,c,h,k,u1,u2). Used in Value Iteration to computes the
%expected reward firm and government rewards from stage k onwards.
%
%INPUTS: s: firm's Markov state
%    c: closure state (see Sec. 2.1)
%    h: firm's tax evasion history vector
%    k: Value iteration stage
%    u1: firm's current decision with respect to tax evasion (u1 is the
%    fraction of profit the firm chooses to conceal).
%    u2: firm's current decision to use (or not) the closure option.
%
%OUTPUT: efirmrev: expected firm revenue while at the state defined
%    by (s,c,h), making decision u1, u2.
function [efirmrev egovrev]=expval(s,c,h,k,u1,u2)

%see main file
global Jk
global Sk
global PERIODIC
global DOGOV

%initialize firm and gov't revenue values to 0.
efirmrev=0;
egovrev=0;

%See Sec. 2.1
H=[0 1 0 0 0
    0 0 1 0 0
    0 0 0 1 0
    0 0 0 0 1
    0 0 0 0 0];

e5=[0 0 0 0 1]';
%Based on the firm's decision, the next history vector will be...
nexth=H*h+e5*u1;

i=s;

for t=1:2 %iterate on closure being available next year, or not
    for j=1:15
    %the next possible sstate will be x_k=(j,t,H*h+e_5*u_1)
    if (PERIODIC==0)
    efirmrev=efirmrev+Pr(c,j,i,u2)*Pre(t)*Jk(k-1,nexti(j,t,nexth));
    if (DOGOV)
    egovrev=egovrev+Pr(c,j,i,u2)*Pre(t)*Sk(k-1,nexti(j,t,nexth));
    end
    else
    efirmrev=efirmrev+Pr(c,j,i,u2)*PrePer(t,k)*Jk(k-1,nexti(j,t,nexth));
    if (DOGOV)
    egovrev=egovrev+Pr(c,j,i,u2)*PrePer(t,k)*Sk(k-1,nexti(j,t,nexth));
    end
    end
    end
end

end

end

%*****/%*****/%*****/%***** end of FILE expval.m
```

%%%%%%%%%%%%%%%%%FILEg.m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

```matlab
%Function g(s,c,h,u1) firm reward (see eq. 9).
%
%INPUTS: s: Firm's Markov state (see Sec. 2.1)
%    c: closure state - NOT USED HERE
%    h: firm's tax evasion history vector
%    u1: firm's current decision with respect to tax evasion (u1 is the fraction of profit the firm chooses to conceal).
%OUTPUT: rew: firm's reward while at state x=(s,c,h'), making decision u1.
function rew=g(s,c,h,u1)
```

```matlab
%Tax parameters (see Section 2.3)
global R %Firm annual revenue - set in main file
global r %tax rate
global b %tax penalty rate
global l %closure cost as a fraction of firm's annual revenue

rew=0;
%reward computation. See eq. (9) for formula and explanation
if (s>=11 && s <=15) %we are in a N1...N5 state (no audit/ no option)
    rew=1-r+r*u1;
else
    if (s>=6 && s<=10) %We are in an 01,...,05 (option) state
    rew=1-r+r*u1-l*(s-5);
    else
    if (s>=1 && s<=5) %We are in a V1...V5 (audit) state
    sh=0;
    sih=0;
    for i=1:s
    sh=sh+h(length(h)-i+1);
    sih=sih+i*h(length(h)-i+1);
    end
    %penalty if audited. Includes 3/5 discount term for prompt pmt
    rew=1-r+r*u1-r*sh-(3/5)*b*r*sih;
    else
    fprintf(1,'Oops...\n');
    pause;
    end
    end
end

rew=rew*R;

end

%1-r*(1-u)=1-r+ru

%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%%/
```

```matlab
%Function ggov(s,c,h,u1)
%
%INPUTS: s: firm's Markov state (see eq. (4)).
%    c: option state
%    h: firm's tax evasion history vector
%    u1: firm's decision with respect to tax evasion (see Sec. 2.1).
%OUTPUT: rew=government revenues when the firm is in state x_k=(s,c,h) and
%    conceals u1 fraction of its profit.
%Note: Government revenue can usually be computed in the main file simply
%from knowledge of the firm's optimal reward. This function is provided for
%experimentation with various options, such as the government being unable
%to collect a portion of the revenue it is owed.

function rew=ggov(s,c,h,u1)

%Tax parameters (see Section 2.3)
global R %Firm annual revenue - set in main file
global r %tax rate
global b %tax penalty rate
global l %closure cost as a fraction of firm's annual revenue

%Set to <1 if some penalties/back taxes go uncollected
fraction_collected=1;

%h
rew=0;
if (s>=11 && s <=15)
    rew=r*(1-u1);
else
    if (s>=6 && s<=10)
    rew=r*(1-u1)+1*(s-5);
```

```matlab
else
    if (s>=1 && s<=5)
    sh=0;
    sih=0;
    for i=1:s
    sh=sh+h(i);
    sih=sih+i*h(i);
    end
    rew=r*(1-u1)+fraction_collected*(r*sh+r*(3/5)*b*sih);
    else
    fprintf(1,'Oops...\n');
    pause;
    end
end

rew=rew*R;

end
%/%/%/%/%/%/%/%/%/%/%% end of FILE ggov.m %/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%%
% Pr(q,i,j,m): see eq. (8).
% INPUTS: q=1 (option available) or 2 (no option).
% i: starting state
% j: end state
% m: 1 (firm takes option) or 2 (firm declines option).
%OUTPUT: probability of transitioning from state j to state i given the %availability of the closure option (q) and firm's decision to use the %option (m)
%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/
function p=Pr(q,i,j,m)
```

%Transition matrix without option

<table><tr><td colspan="15">Mno=[</td></tr><tr><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0.0025</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0025</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0025</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.04</td><td>0.04</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="14">%Transition matrix with option Ma=[</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr></table>

<table><tr><td colspan="15">%Transition matrix with option available &amp; firm declines</td></tr><tr><td>Md=[0.0075</td><td>0.0075</td><td>0.0075</td><td>0.0075</td><td>0.0075</td><td>0.0075</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0075</td><td>0.0075</td><td>0.0075</td><td>0.0075</td><td>0.0075</td><td>0.0075</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0075</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0075</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.12</td><td>0.12</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-0.9925</td><td>0.9925</td><td>0.9925</td><td>0.9925</td><td>0.9925</td><td>0.9925</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.9925</td><td>0.9925</td><td>0.9925</td><td>0.9925</td><td>0.9925</td><td>0.9925</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.9925</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.9925</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.88</td><td>0.88</td></tr></table>

```matlab
if (q==2) %closure not available
    p=Mno(i,j);
else
    if (q==1) && (m==1) %take option
    p=Ma(i,j);
    else
    if (q==1) && (m==2) %decline
    p=Md(i,j);
    else
    fprintf(1,'0oops...\n');
    pause;
    end
end

%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%%%
%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%%%
% Pre(t,k) corresponds to Pr(e_k=i) in eq. (6)
% INPUTS: t=1 if closure is available, 0 otherwise
% OUTPUT: probability that closure is given
%
%/%/%/%/%/%/%/%/%/%/%/%%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%/$%$
function p=pre(t)

%c is the probability of closure - defined in the main mdp.m file global v

%uncomment this statement for stochastic closure
if (t==1) %closure available
    p=v;
else %no closure
    p=1-v;
end

%,%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/
%,%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/
%,%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/%%/
%,%/######///%
% PrePer(t,k) corresponds to Pr(e_k=i) in eq. (6) in the case
% where the option is given periodically, with period CLOSURE_PERIOD
% INPUTS: t=1 if closure is available, 0 otherwise
% OUTPUT: probability that closure is given
%
%,%/######///%
function p=PrePer(t,k)
```

```matlab
global CLOSURE_PERIOD %set in mdpperiodic_tax.m
%CLOSURE_PERIOD=5; %closure period in years

if mod(k,CLOSURE_PERIOD)==1 %we are in a year where closure is offered
    if (t==1)
    p=1;
    else
    p=0;
    end
else %not in a year where closure is offered
    if (t==1)
    p=0;
    else
    p=1;
    end
end

%%%%,%,%,%,%,%,%,%,%% end of FILE PrePer.m %,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%%,FILE checkfeasible.m %,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%%,function [evade, useoption, nrfeas, afeas]=checkfeasible(uopt,aopt)
global v

H=[0 1 0 0 0
    0 0 1 0 0
    0 0 0 1 0
    0 0 0 0 1
    0 0 0 0 0];
e5=[0 0 0 0 1]';
feasible=0*uopt;

converged=0;
feasible(1)=1; %seed initial state
while (~converged)

savedfeasible=feasible;

for i=1:length(feasible)

    if (feasible(i)==1) %find next feasible states

    %find state and controls
    [s,c,h]=column2state(i);
    u1=uopt(i);
    a1=aopt(i);

    %Based on the firm's decision, the next history vector will be...
    nexth=H*h+e5*u1;

    %find which are the next possible states

    vstate=zeros(15,1);
    for j=1:15
    vstate(j)=(Pr(c,j,s,a1)~=0);
    end

    %mark states
    for j=1:15
    if vstate(j)==1
    if (v>0)
    feasible(nexti(j,1,nexth))=1;
    end
```

```matlab
if (v<1)
    feasible(nexti(j,2,nexth))=1;
end
end
end
end
if (feasible==savedfeasible)
    converged=1;
end
end

evade=sum(uopt.*feasible);
useoption=sum((aopt==1).*feasible);
nrfeas=sum(feasible);

%states in which the option is not available or the firm was just audited
%should not be counted as feasible for the use of the option (firm has no
%'active' past decisions for which it may want to use the option).
reduce=0;
for i=1:length(feasible)
    [s,c,h]=column2state(i);
    if (feasible(i)==1) && (s<=5) && (c==1)
    reduce=reduce+1;
    end
    if (feasible(i)==1) && (c==2)
    reduce=reduce+1;
    end
end
afeas=nrfeas-reduce;

%%%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%%/File column2state.m
%Input: i, a column number (for the matrices containing firm rewards, Jk,
%or gov. revenue, Sk).
%Output: (s,c,h) elements of the firm's state vector.

function [s,c,h]=column2state(i)

%The firm's state is a 7-tuple (see eq. 3).
%Determine which 7-tuple i corresponds to
s=floor((i-1)/(2*2^5))+1; %Markov state
c=floor(mod(i-1,2*2^5)/(2^5))+1; %closure state

hs=mod(i-1,2^5); %now form history vector, h
hs=dec2bin(hs,5);
h=zeros(5,1);
for j=1:5
    h(j)=str2num(hs(j));
end

%%%/%/%/%/%/%/%/%/%% end of FILE column2state.m
%Function nexti(j,t,h). In the article (see Sec. 2.1) the firm's state
%is a 7-tuple (j,t,h) where j is the firm's tax status, c is the state of
%the closure option (available or not) and h is the firm's tax evasion
%history 5-vector.
%
%When applying value iteration, the firm's states are numbered sequentially
%and set in correspondence to the columns of the reward matrix Jk in the
%main file. The function nexti(...) converts the firm's state, as described
%by (j,t,h) to the index of the corresponding column in Jk.

%

%INPUTS: j is the firm's tax status (see Sec. 2.1)
%    c: closure state
%    h: firm's tax evasion history vector
%OUTPUT: column index of state x_k=(j,t,h) in the reward matrix Jk (main
%file).
```

function x=nexti(j,t,h)

%The index returned corresponds to the state's lexicographic order,

%I.e. (j=1,c=1,h=[0 0 0 0 0])-->1

% (j=1,c=1,h=[0 0 0 0 1])-->2

$$
\% \dots (j = 1, c = 1, h = [ 1 1 1 1 1 ]) -- > 32
$$

$$
\% \quad (j = 1, c = 2, h = [ 0 0 0 0 0 ]) -- > 3 3, \text {etc...}
$$

%convert (i,t,h) to 1...Nstate

1astdec=h(5)+h(4)\*2+h(3)\*4+h(2)\*8+h(1)\*16+1;

x=2\*2^5\*(j-1)+2^5\*(t-1)+1astdec;

end

%%%%%%%%%%%%%%%%%endofFILEnexti.m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

## References

[1] P. Allingham, H. Sandmo, Income tax evasion: a theoretical analysis, Journal of Public Economics 1 (6) (Jun. 1972) 988–1001.

[2] J.C. Baldry, Tax evasion and labour supply, Economic Letters 3 (1979) 53–56.

[3] D.P. Bertsekas, Dynamic programming and optimal control, Athena Scienti<sup>fi</sup>c 3 (2005).

[4] Sukanto Bhattacharya, Dongming Xu, Kuldeep Kumar, An ANN-based auditor decision support system using Benford's law, Decision Support Systems 50 (2011) 576–584.

[5] C.T. Clotfelter, Tax evasion and tax rates: an analysis of individual returns, The Review of Economics and Statistics 65 (1983) 363–373.

[6] E. Eide. Tax evasion with rank dependent expected utility. Unpublished paper, University of Oslo, Department of Private Law, 2002.

[7] B. Frey, L.P. Feld, Deterrence and Morale in Taxation: An Empirical Analysis, CESifo working paper, 2002, p. 760

[8] J.P.F. Gordon, Individual morality and reputation costs as deterrence to tax evasion, European Economic Review 33 (1989) 797–805.

[9] Greek ministry of <sup>fi</sup>nance. n.3259/2004 (pol.1034/2005) (in Greek), 2004.

[10] Greek ministry of <sup>fi</sup>nance. n.3697/2008 (pol.1130/2008) (in Greek), 2008.

[11] J. Hindriks, M. Keen, A. Muthoo, Corruption, extortion and evasion, Journal of Public Economics 88 (1996) 161–170.

[12] S. L Humphreys, K. C. Mof<sup>fi</sup>t, M. B. Burns, J. K. Burgoon, and W. L. Felix. Identi<sup>fi</sup>cation of fraudulent <sup>fi</sup>nancial statements using linguistic credibility analysis. Decision Support Systems 50 (3) (2011) 585–594.

[13] K. Kanellopoulos, I. Kousoulakos, B. Rapanos, The underground economy in Greece: what of<sup>fi</sup>cial data show, Greek Economic Review 14 (1992) 215–236.

[14] F.E. Kydland, E.C. Prescott, Dynamic optimal taxation, rational expectations and optimal control, Journal of Economic Dynamics and Control 2 (1980) 79–91.

[15] M.J. Nigrini, A taxpayer compliance analysis of Benford's law, Journal of American Taxation 18 (1) (1996).

[16] A.M. Polinsky, S. Shavell, The optimal tradeoff between the probability and magnitud of <sup>fi</sup>nes, The American Economic Review 69 (5) (Dec. 1979) 880–891.

[17] J.E. Smith, K.F. McCardle, Structural properties of stochastic dynamic programs Operations Research 50 (5) (2002) 796–809.

[18] N. Tatsos, Economic fraud and tax evasion in greece (in Greek), Papazisis Publishings, 2001.

[19] A. Vasin, P. Vasina, Tax optimization under tax evasion, the role of penalty constraints, Economics Education and Research Consortium 1 (2009) 1–44.

Nikolaos D. Goumagias is a Ph.D. candidate in the department of Applied Informatics at the University of Macedonia, Greece. He received the B.Sc. degree in Economics from the Aristotle University of Thessaloniki in 2004, and the M.Sc. degree in Accounting and Financial Management from the Lancaster University Management School in 2006. His research focuses on decision support models, with applications in economic systems, behavioral <sup>fi</sup>nance and <sup>fi</sup>nancial derivatives.

Dimitrios Hristu-Varsakelis is an assistant professor in the Department of Applied Informatics at the University of Macedonia in Thessaloniki Greece. He reveiced his Ph.D. in Engineering Sciences from Harvard University. Before joining the University of Macedonia he served as a faculty member at the University of Maryland, College Park. His research interests are in the areas of decision-making and optimization, dynamics of socio-economic systems, and bio-inspired decision-making. His work has appeared in Energy Policy, Economic Modeling, the IEEE Transactions on Automatic Control and Automatica, among others.

Anastasios Saraidaris received his Ph.D. from the department of Applied Informatics at th University of Macedonia, Greece. He received the B.Sc. degree in Economics from the Aristotle University of Thessaloniki in 2001, and the MBA from the University of Aberystwyth in Wales, UK. He is currently a Taxation Specialist with the Greek Ministry of Finance. His research focuses on public finance, and corporate income taxation and fiscal studies.
