---
otero_id: 6036
otero_key: "EXXYYAGR"
title: "Principal–agent learning"
authors: "Fidan Boylu; Haldun Aytug; Gary J. Koehler"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.01.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Principal–agent learning

Fidan Boylu <sup>a,</sup>⁎, Haldun Aytug <sup>b</sup>, Gary J. Koehler <sup>b</sup>

<sup>a</sup> Operations and Information Management, School of Business, University of Connecticut, CT, USA

<sup>b</sup> Information Systems and Operations Management Department, 351 Stuzin, The Warrington College of Business Administration, University of Florida, Gainesville, FL 32611, USA

## a r t i c l e i n f o

Article history: Received 11 June 2008 Received in revised form 24 November 2008 Accepted 4 January 2009 Available online 8 January 2009

Keywords: Discriminant analysis Principal–agent Strategic gaming Utility-based learning

## a b s t r a c t

In this paper we present a merging, and hence an extension, of two recent learning methods, utility-based learning and strategic or adversarial learning. Recently, utility-based learning brings to the forefront the learner's utility function during induction. Strategic learning anticipates strategic activity in the induction process when the instances are intelligent agents such as in classi<sup>fi</sup>cation problems involving people or organizations. We call the resulting merged model principal–agent learning and present an induction process and example. Our model collapses to utility-based models when the agents do not engage in strategic behavior and to strategic learning when the learner's utility is not considered.

Published by Elsevier B.V.

## 1. Introduction and preliminaries

In this paper we present a merging and, hence an extension, of two recent learning methods, utility-based learning and strategic or adversarial learning. Our focus of attention is on supervised learning for classi<sup>fi</sup>cation tasks. We use the terms “learning” and “data mining” interchangeably. We begin with a brief review of these recent learning paradigms.

## 1.1. Utility-based learning

Utility-based data mining [28] explores data mining problems where the learner (we call the principal) considers a full array of economic issues when learning. For example, added to the usual concerns about generalization, the principal may consider the cost of data acquisition [20,25,26], the costs of misclassi<sup>fi</sup>cations [1,9,11,15,24,37], the time taken to label an instance [1] and other aspects related to economic considerations.

A recent paper in the utility-based learning area questions the effectiveness of traditional error-centric approach for label acquisition problem and offers a decision-centric approach that incorporates utility information [29]. As we also stress in this paper, they argue that previously introduced strategies identify and acquire information that is estimated to minimize the model's statistical prediction error. These error-centric strategies do not consider the decision-making context in which the model will be used. Usually a decision maker may have different goals in mind then merely minimizing the prediction error.

Especially when restricted by the cost of acquiring information, only focusing on prediction error may bring in economical harm to the decision maker. Thus, one of the major considerations when designing models that learn from data should be the maximization of expected utility which minimizes the costs to the decision maker.

## 1.2. Strategic learning and adversarial classification

Recently, Boylu et al. [6,5,3] and Dalvi et al. [12] looked at learning problems where the instances, represented by a vector of attributes, are intelligent agents. They anticipate a principal's classi<sup>fi</sup>cation rule and then engage in strategic behavior to obtain a positive classi<sup>fi</sup>cation by altering their attributes, if possible. Boylu et al. [6,5,3] argue that this behavior should be considered as part of the induction process and use rational expectation theory to completely characterize a simple form of the problem for inferring linear discriminant functions (LDFs) using support vector machines. In [3], Boylu et al. raise the need for anticipating strategic agent activity. In [5] they present a general framing of strategic learning within the context of other learning models. In [6], they provide a detailed induction method for strategic learning that uses mixed integer programming models and illustrate their approach with a credit approval problem. They call this problem setting “Induction over Strategic Agents” or “Strategic Learning”. In Ref. [4] they offer a genetic programming algorithm for solving the strategic learning problem.

Dalvi et al. [12] describe a somewhat similar scenario. They formulate the problem as a game with two players, an adversarial agent and a principal (they call them Adversary and Classi<sup>fi</sup>er, respectively), where the agent tries to alter true negative instances for a positive classi<sup>fi</sup>cation. The authors show that if the agent incurs a unit cost for altering an instance, there exists a Nash equilibrium solution. Since <sup>fi</sup>nding Nash equilibria is prohibitive in the general case, they focus on a one-step game between the agent and principal. Using a Naïve Bayes Classi<sup>fi</sup>er, the principal obtains better results if he anticipates agent activities. They illustrate this with a spam <sup>fi</sup>ltering application. They call their problem setting “Adversarial Classi<sup>fi</sup>cation”.

Other forms of learning capture various aspects of such gaming. For example, Mannino and Koushik [22] look at inverse classi<sup>fi</sup>cation as part of a sensitivity analysis with similarity based learning, and seek to <sup>fi</sup>nd the minimum required change to an instance to reclassify it as a member of the preferred class. Jiang et al. [19] look at the deductive use of a decision tree where the input data may be distorted (due a variety of causes, some of which may be strategic behavior). Various forms of leader–follower learning [2] and reinforcement learning [32] exhibit some aspects of iterative learning in response to changes by the principal and agents.

## 1.3. A new paradigm

In this paper we generalize these approaches and merge utility based learning with strategic/adversarial learning. The resulting model we call principal–agent learning following a common paradigm in economics, the principal–agent problem. We then look at an induction principle for this class of problems.

The principal–agent learning model expands over the prior strategic learning models by merging utility considerations of the principal into the induction process when undertaken in the presence of strategic agents. This results in a modi<sup>fi</sup>cation of the induction process that is discussed in Section 6. The principal–agent learning model generalizes over the utility-based learning models by considering strategic activity by agents. The resulting principal–agent learning model collapses to a utility-based model in the absence of strategic agents and to a strategic learning model in the absence of utility-based considerations by the principal.

In Section 2 we present a formal model for principal–agent learning. In Section 3 we consider induction principles and focus on statistical learning theory to provide bounds on the principal's expected utility, which in turn are used to provide a goal for induction. This is pursued in Section 4. Section 5 illustrates the methodology by mapping a strategic learning problem studied in the literature to our principal–agent learning model which is solved in Section 7. Section 6 summarizes the induction process for the principal–agent learning model. Finally, in Section 8 we offer conclusions and directions for future research.

## 2. Formal model of principal–agent learning

In the traditional principal–agent problem found in economics, the principal delegates decision-making to one or more agents who share in the output according to a mutually acceptable contract between the principal and agents. The principal seeks to maximize his/her expected utility by selecting a sharing contract over the net output derived from agent effort. Agents are also utility-based decision makers.

With some abuse of this basic model, we call our learner the principal. Instead of choosing a sharing contract, a data mining principal chooses the function that will be used to classify instances (agents) as positive or negative. Agents can anticipate this and exert effort to achieve a positive classi<sup>fi</sup>cation. Of course, in addition to considering other economic impacts, the principal would like only truly positive agents to be classi<sup>fi</sup>ed as positive and truly negative agents classi<sup>fi</sup>ed as negative. This is not always possible, especially with strategic gaming. Hence the principal must consider the various trade-offs during induction. This we call principal–agent learning.

We start our investigation with a formal statement of the principal's problem followed by an analysis of the agent problem when agents may act strategically. Notation used in Sections 2–4 is summarized in Table 1.

<table><tr><td colspan="2">Agents (subscript i may be suppressed)</td></tr><tr><td>n</td><td>Number of attributes (or features).</td></tr><tr><td>X</td><td>Instance space.  $X \subseteq \Re^n$ .</td></tr><tr><td> $x_i$ </td><td>Agent i&#x27;s vector of attributes.  $x_i \in X$ .</td></tr><tr><td>C</td><td>Possible classes for agents.</td></tr><tr><td> $y(x_i)$ </td><td>Agent i&#x27;s true class.  $y(x_i) \in C$ .</td></tr><tr><td> $d_i(o)$ </td><td>Agent i&#x27;s vector of attribute changes for principal&#x27;s classification function o( ).</td></tr><tr><td> $d_i(w,b)$ </td><td>Agent i&#x27;s vector of attribute changes when the principal uses a linear discriminant function with parameters (w,b).</td></tr><tr><td>Y</td><td>The set of feasible attribute changes.</td></tr><tr><td>e(d)</td><td>Agent effort to alter attributes by vector d.</td></tr><tr><td>t(x)</td><td>Desired label of agent x.</td></tr><tr><td>u(e(d),o)</td><td>Agent utility.</td></tr><tr><td> $\bar{u}$ </td><td>Reservation utility level.</td></tr><tr><td>r</td><td>Reservation cost.</td></tr><tr><td colspan="2">Principal (arguments of functions may be suppressed for ease of notation)</td></tr><tr><td> $\alpha \in \Lambda$ </td><td>Parameters.</td></tr><tr><td>o(x,α)</td><td>Classification function for x ∈ X.</td></tr><tr><td>Z(y(xi),o(xi+ di(o),α))</td><td>Net income for classifying agent i as o(xi+di(o),α) when he is actually y(xi).</td></tr><tr><td>U( )</td><td>Utility of net income.</td></tr><tr><td>F(x)</td><td>Sampling distribution over X.</td></tr><tr><td colspan="2">Statistical learning theory</td></tr><tr><td>l</td><td>Sample size.</td></tr><tr><td>S</td><td>Training sample, S=((x1,y1),...,,(x1,y1)).</td></tr><tr><td>Uemp(α)</td><td>Sampled expected utility (empirical utility) over the training set for parameters α ∈ Λ</td></tr><tr><td>R(α)</td><td>Risk functional giving the expected loss for parameters α ∈ Λ.</td></tr><tr><td>L(y(x),o(x,α))</td><td>Loss function for classifying x as o(x,α) when it is actually y(x).</td></tr><tr><td>Remp(α)</td><td>Empirical risk (expected loss) over the training set for parameters α ∈ Λ</td></tr><tr><td>η</td><td>Confidence level.</td></tr><tr><td>h</td><td>Capacity measure.</td></tr><tr><td>Rstruct(h,l,η)</td><td>Structural risk. Rbound(α) upper bound on R(α). A ≤ L( ) ≤ B bounds on the loss function.</td></tr><tr><td colspan="2">Support vector machine</td></tr><tr><td>w</td><td>Vector of weights for the linear discriminant function.</td></tr><tr><td>b</td><td>Intercept for the linear discriminate function.</td></tr><tr><td>ξi</td><td>The shortfall of a training point i in its margin from the hyperplane.</td></tr><tr><td>C</td><td>Positive trade-off parameter between margin and training error.</td></tr><tr><td>γ</td><td>Trade-off reflecting bounds A and B on the loss function.</td></tr></table>

## 2.1. The principal's problem

As in utility-based learning, the principal is considered risk averse or risk neutral with utility function U(Z) over net income, Z, and wishes to discover a classi<sup>fi</sup>cation rule embodied as a function from the instance space $X \subseteq \Re ^ { n }$ over agents' n attributes (or features) to a set C of possible labels. For example, $C = [ a , b ] \subseteq \Re$ could be per-<sup>½ -</sup>formance levels. For a credit approval classi<sup>fi</sup>cation task, $C = \{ - 1 , + 1 \}$ might represent that an agent is credit worthy (+1) or not (−1).

The classi<sup>fi</sup>cation function applied to agent x∈X, o(x,α), is parametrically de<sup>fi</sup>ned by α∈Λ. For example, for LDFs of the form w′x+b, then $\alpha = ( \mathbf { w } , b )$ and Λ would be the set of permissible values for these two parameters (usually $\alpha = ( \mathbf { w } , b ) { \in } \Re ^ { n + 1 } )$ and

$$
o (x, \alpha) = \left\{ \begin{array}{l l} - 1 & \text { if } w ^ {\prime} x + b <   0 \\ + 1 & \text { if } w ^ {\prime} x + b \geq 0. \end{array} \right.
$$

Thus the principal seeks to <sup>fi</sup>nd $\alpha \in \Lambda$ for $o { : } X {  } C$ that maximizes expected utility. (The arguments of function o(x,α) are often suppressed notationally for ease of presentation leaving either o( ) or just o).

Let $y ( x ) \in C$ be the true label of an instance $x \in X .$ Let net income $Z ( y ( x ) , o ( x , \alpha ) )$ re<sup>fl</sup>ect any value coming from the use of o(x,α) less any cost of data acquisition or usage of $o ( x , \alpha )$ . The principal “learns” by solving the expected utility problem

$$
\max _ {\alpha \in \Lambda} \int U (Z (y (x), o (x, \alpha))) d F (x)
$$

where F is an unknown distribution function over $x \in X .$ Since F is unknown, an induction principle must be invoked to solve the expected utility problem. This is addressed in Section 3.

The expected utility problem can be viewed as an alternative representation to the common learning approach of minimizing a loss function (usually chosen to be the number of misclassi<sup>fi</sup>cations or a cost function of misclassi<sup>fi</sup>cations). In contrast to that approach, the goal here is utility maximization. When the utility considerations come into play, solving the problem of minimizing the number of misclassi<sup>fi</sup>cations may not necessarily coincide with maximizing utility. In fact, in some cases a principal may deliberately allow some misclassi<sup>fi</sup>cations in favor of gained utility from other economic aspects of the situation.

As in utility-based learning, the principal seeks to determine a classi<sup>fi</sup>cation function, $o { : } X {  } C ,$ , for use over instances drawn from instance space X. Given this will be determined by the principal when instances represent self-interested, intelligent agents, we offer the possibility that agents may act strategically to alter their true attributes, $x \in X ,$ , to obtain a new set of attributes, $\mathbf { \boldsymbol { x } } + d ( \mathbf { \boldsymbol { o } } )$ , that will give a preferred classi<sup>fi</sup>cation. Here $d ( o )$ represents the vector of attribute changes that an agent would invoke in response to the principal's classi<sup>fi</sup>cation function, o.

Thus, the principal needs to anticipate this gaming and learn by solving the expected utility problem

$$
\max _ {\alpha \in \Lambda} \int_ {x \in X} U (Z (y (x), o (x + d (o), \alpha))) \mathrm{d} F (x)\tag{1}
$$

This differs from the utility-based model by the inclusion of agent activities vis-à-vis $x + d ( o )$ . If agents are not self-interested and cannot act strategically then $d ( o ) = 0$ reducing the problem to the standard utility-based model. When agents can act strategically, we assume they will choose $d ( o )$ optimally to satisfy their own objectives. This is called incentive compatibility in economics [17].

## 2.2. The agent problem

When instance space X represents self-interested, intelligent agents, we assume the agents are utility maximizers with a utility function $u ( e , o )$ over effort level e( ) and classi<sup>fi</sup>cation outcome $o ( \mathbf { \xi } ) ,$ Each agent has a true type $y ( x ) \in C .$ . The classi<sup>fi</sup>cation outcome is decided by the principal's classi<sup>fi</sup>cation function o( ). When agents are self-interested entities (such as a person or collectively as a company, for example), they may act strategically to alter their true attributes x to obtain new attributes $x + d$ that would yield a desired classi<sup>fi</sup>cation. For example, a person applying to a university may try to alter attributes to increase their chance of acceptance. A low effort change might be joining academic clubs in high school. A high effort change might involve hiring consultants as discussed in [27].

Standard game theory assumes that both principal and agents attempt to maximize their own utility assuming parameters of both parties are common knowledge. Agents maximize their utility according to o( ) which requires effort represented as $e ( d )$ . The principal anticipates optimal agent action knowing that agents act depending on $o ( \mathbf { \xi } )$

Thus, agents desire to maximize their utility u(e,o). However, no agent will exert effort if they would not achieve a desired classi<sup>fi</sup>cation or if the amount of effort required to achieve this classi<sup>fi</sup>cation results in a utility that doesn't exceed their minimal utility, their reservation utility level, ū, for achieving the goal. This consideration is called the individual rationality constraint.

Suppose $t ( x ) \subseteq C$ is a single, desired classi<sup>fi</sup>cation of an agent with attribute vector x. Then the agent problem can be summarized as

$$
\begin{array}{l} d (o) \in \underset {d \in Y} {\operatorname{argmax}} u (e (d), o) \\ \text { s.t. } \\ o (x + d) = t (x) \\ u (e (d), o) \geq \overline {{u}} \end{array}
$$

where feasible changes to x are speci<sup>fi</sup>ed by set Y. If there is no feasible solution, an agent sets $d ( o ) = 0$ . More involved models can be imagined where an agent may have many desired classi<sup>fi</sup>cations, each with different utilities. The agent problem can be extended to allow the utility function to also be a function of a random component (like the state of current economic conditions), wherein we would change the optimization objective and individual rationality constraint to be over expected utility. However, these extensions will be differed to later research.

## 3. Induction principle

The principal needs to solve Eq. (1) to determine an optimal classi<sup>fi</sup>cation function. Towards this end, a common induction approach, called supervised learning, is for the principal to procure a sample of instances (a training set) having correct category labels and use this training set to discover a classi<sup>fi</sup>cation function. For example, in a binary classi<sup>fi</sup>cation problem, a sample

$$
S = ((x _ {1}, y _ {1}), \dots , (x _ {l}, y _ {l}))
$$

consists of l observations where $x _ { i }$ is a vector of attributes (or features) for instance i and $y _ { i }$ its true label.

When the induction principle constrains the principal's problem to the training data as in

$$
\max _ {\alpha \in \Lambda} \sum_ {i = 1} ^ {l} U (Z (y (x _ {i}), o (x _ {i} + d _ {i} (o), \alpha)))\tag{2}
$$

the expected utility collapses to “empirical utility” or “sampled expected utility” denoted as $U _ { \mathrm { e m p } } ( \alpha )$ (for example, see [25]). This is similar to induction based on empirical risk where over-<sup>fi</sup>tting is often the result as observed in many studies such as [13]. An important alternative is offered by statistical learning theory [34].

A major concern of all learning methods is generalization. Arguably, statistical learning theory [34] provides one of the best frameworks for studying learning problems where there are minimal statistical assumptions. This theory provides bounds on generalization error. Statistical learning theory starts with two assumptions: (1) that sampling is i.i.d and (2) that the unknown distribution remains <sup>fi</sup>xed after the learner induces the classi<sup>fi</sup>cation function. Regarding the <sup>fi</sup>rst point, Boylu et al. [6] argue that strategic behavior does not affect the i.i.d assumption and, to the contrary, without taking into account agent behavior, this feature may be violated. Similar reasoning preserves assumption (2) in the sense that the induction process anticipates the eventual distribution resulting from strategic agent behavior.

The most popular implementation of statistical learning theory is induction using support vector machines [10]. Support vector machines (SVMs) have nice properties not found in most data mining methods. They are guaranteed to <sup>fi</sup>nd an optimal solution (unlike neural network induction or decision tree methods); they scale to very large problems, even in<sup>fi</sup>nitely large ones; and they handle non-linear feature mappings naturally; etc. (see Ref. [10]). SVMs are a popular data mining technique and have been applied in many areas [10] including going concern opinions [23], web page <sup>fi</sup>ltering [8], document <sup>fi</sup>ltering [31], and credit rating [16,33].

Statistical learning theory addresses the generalizability of induction methods. A risk functional captures the expected loss of using an induced function as

$$
R (\alpha) = \int_ {x \in X} L (y (x), o (x, \alpha)) \mathrm{d} F (x)\tag{3}
$$

Here $L ( \mathbf { \theta } )$ is a loss function. As in our principal–agent case, because F is unknown, an induction principle must be used.

When the induction principle is to constrain the loss function to the training data and then to minimize the number of misclassi<sup>fi</sup>cations, the risk functional collapses to “empirical $\mathrm { \ r { \ r i s k } } ^ { \prime \prime }$ and is denoted as $R _ { \mathrm { e m p } } ( \alpha ) .$ When the loss function is an indicator function, we have for a sample size, l,

$$
R _ {\mathrm{emp}} (\alpha) = \frac {1}{l} \sum_ {i = 1} ^ {l} L (x _ {i}, o (x _ {i}, \alpha))
$$

Statistical learning theory uses a structural risk minimization principle [34]. In such settings, the risk functional is bounded above and that bound is minimized. Many such bounds have been derived following the initial work [34] by Vapnik who showed that with an indicator loss function, that for any $\alpha \in \Lambda$ with a probability at least 1−η the bound

$$
R (\alpha) \leq R _ {\text { emp }} (\alpha) + \frac {R _ {\text { struct }} (h , l , \eta)}{2} \left(1 + \sqrt {1 + \frac {4 R _ {\text { emp }} (\alpha)}{R _ {\text { struct }} (h , l , \eta)}}\right) \equiv R _ {\text { bound }} (\alpha)
$$

holds where the structural risk $R _ { \mathrm { s t r u c t } }$ depends on the sample size, the con<sup>fi</sup>dence level, $\eta ,$ and the capacity, h, of the target function class. Here

$$
R _ {\mathrm{struct}} (h, l, \eta) = \frac {h (4 l n (2 l / h) + 4) - l n (\eta / 4)}{l}
$$

The capacity, h, measures the hypothesis space's richness or expressiveness. For binary classi<sup>fi</sup>cation, h is the maximal number of points (k) that can be separated into two classes in all possible $2 ^ { k }$ ways using functions of the hypothesis space. This is called the VCdimension. For LDFs, the VC-dimension is $h = n + 1$ [35]. Since we cannot directly minimize $R ( \alpha )$ because $F ( \mathbf { \theta } )$ is unknown, the structural risk minimization principle seeks to minimize $R _ { \mathrm { b o u n d } } ( \alpha )$ . Support vector machines provide an induction method that implements the structural risk minimization principle.

We note the similarity of the expected risk minimization problem (Eq. (3)) and the principal's expected utility maximization (Eq. (1)). Letting $L = - U ( Z )$ and allowing for strategic agent changes to x transforms the principal's problem to a risk minimization problem. In the next section we explore this induction.

## 4. Principal–agent induction

Vapnik gives two general bounds on risk minimization [34] (others have derived additional bounds). The <sup>fi</sup>rst can be used when the loss function is bounded by

$$
A \leq L () \leq B
$$

for all $\alpha \in \Lambda$ The second can be used when there are unbounded cases. We focus on the <sup>fi</sup>rst case here assuming that for the learning problem there is a natural bound on how much a principal can extract by manipulating aspects of the classi<sup>fi</sup>cation problem. The following bound was derived by Vapnik [34]:

$$
\begin{array}{l} R (\alpha) \leq R _ {\text { emp }} (\alpha) + \frac {(B - A) R _ {\text { struct }} (h , l , \eta)}{2} \\ \times \left(1 + \sqrt {1 + \frac {4 R _ {\text { emp }} (\alpha)}{(B - A) R _ {\text { struct }} (h , l , \eta)}}\right) \equiv R _ {\text { bound }} (\alpha). \end{array}
$$

Note, this is just a different weighting between empirical and structural risk than the bound for the indicator loss function.

As mentioned above, support vector machines implement the structural risk minimization principle (see [10] for example). They determine a hyperplane in a feature space that best separates positive from negative examples. The objective of the support vector machine problem maximizes the margin between the positive and negative examples (for completely separable datasets) which, in turn, leads to smaller VC-dimensions and then to a smaller risk bound. For nonseparable problems, an additional term trades-off margin with classi<sup>fi</sup>cation error.

The general 2-norm SVM model is formulated as a quadratic optimization problem with linear constraints as

$$
\begin{array}{l} \min w ^ {\prime} w + \gamma \sum_ {i = 1} ^ {\ell} \xi_ {i} \\ \text { s.t. } \\ y _ {i} (w ^ {\prime} x _ {i} + b) \geq 1 - \xi_ {i} \quad i = 1, \ldots , \ell \end{array}
$$

where 1/w′w is the margin and ξ allows for classi<sup>fi</sup>cation errors on the training set for non-separable problems. Implementing these ideas in the context of principal–agent learning, the parameter γ trades-off classi<sup>fi</sup>- cation error with margin taking into account B−A. A 1-norm version is

$$
\begin{array}{l} \min | w | + \gamma \sum_ {i = 1} ^ {\ell} \xi_ {i} \\ \text { s.t. } \\ y _ {i} (w ^ {\prime} x _ {i} + b) \geq 1 - \xi_ {i} \quad i = 1, \ldots , \ell \end{array}
$$

which is a linear program [7, 14].

We illustrate these notions in the next section by focusing on the problem studied by Boylu et al. [6] and map it to the setting of this paper. We then solve that application using γ to adjust for the principal's utility.

## 5. Application

Consider the problem studied by Boylu et al. [6]. They looked at a credit approval problem (which we study in Section 7). The classi<sup>fi</sup>cation function form was LDFs and labeling was binary (i.e., $C = \{ + 1 , - 1 \} )$ . We map their problem to the principal–agent setting in this section and then solve and compare the results when using a principal's utility function often employed in economic settings.

In the Boylu et al. [6] case, all agents seek to be labeled $\mathsf { a s } + 1 .$ Thus $t ( x _ { i } ) = + 1$ and, noting the use of LDF classi<sup>fi</sup>cation functions, $o ( x _ { i } + d ) = t ( x _ { i } )$ becomes

$$
w ^ {\prime} [ x _ {i} + D (w) d ] + b \geq 1
$$

where diagonal matrix $D ,$ with diagonal components of +1 and −1, orients the moves d to re<sup>fl</sup>ect directions leading to better scores under o( ). That is,

$$
D _ {j, j} (w) = \left\{ \begin{array}{l l} + 1 & w _ {j} \geq 0 \\ - 1 & w _ {j} <   0 \end{array} \right.
$$

In mapping the Boylu et al. [6] problem to the principal–agent setting of this paper, we say agent i has a utility function of the form

$$
u _ {i} (e, o) = v _ {i} \frac {1 + o (x _ {i} + d _ {i} (w , b))}{2} - c ^ {\prime} i d _ {i} (w, b)
$$

where $c _ { i } , v _ { i } { > } 0$ and $\bar { u } _ { i } = 0 . \nu _ { i }$ is the utility of being labeled as $\mathsf { a } + 1$ . Here we replaced $d _ { i } ( o )$ with $d _ { i } ( w , b )$ ) re<sup>fl</sup>ecting the form of the classi<sup>fi</sup>cation function. Effort is linear with $e _ { i } ( d _ { i } ) = { c _ { i } } ^ { \prime } d _ { i } ( w , b )$ . Notice that the <sup>fi</sup>rst term of the utility is zero if o( ) isn't +1, otherwise it is $\nu _ { i \cdot }$ The agent move problem, with $Y = \Re _ { \geq 0 } ^ { n } ,$ , for agent i is then

$$
\begin{array}{l} d _ {i} (w, b) \in \underset {d _ {i} \geq 0} {\operatorname{argmax}} v _ {i} \frac {1 + o (x _ {i} + d _ {i} (w , b))}{2} - c ^ {\prime} i d _ {i} (w, b) \\ \text { s.t. } \quad w ^ {\prime} [ x _ {i} + D (w) d _ {i} (w, b) ] + b \geq 1 \\ v _ {i} \frac {1 + o (x _ {i} + d _ {i} (w , b))}{2} - c ^ {\prime} i d _ {i} (w, b) \geq 0 \end{array}
$$

Thus, the individual rationality constraint

$$
v _ {i} \frac {1 + o (x _ {i} + d _ {i} (w , b))}{2} - c ^ {\prime} i d _ {i} (w, b) \geq \overline {{u}} _ {i}
$$

under a positive classi<sup>fi</sup>cation is equivalent in their setting to

$$
v _ {i} - c ^ {\prime} i d _ {i} (w, b) \geq \overline {{u}} _ {i}
$$

or simply

$$
v _ {i} - \overline {{u}} _ {i} \geq c ^ {\prime} i d _ {i} (w, b)
$$

which gives a maximum reservation constraint implying effort cannot exceed this value. Boylu et al. [6] term the quantity $\nu _ { i } - \bar { u } _ { i }$ a reservation cost, $, r _ { i } .$

This agent problem has the following solution. For non-zero w, let $j ^ { * }$ satisfy

$$
j ^ {*} \in \arg \min _ {j, w _ {j} \neq 0} \frac {(c _ {i}) _ {j} \max (0 , 1 - (b + w ^ {\prime} x _ {i}))}{| w _ {j} |}
$$

then for

$$
z _ {i} ^ {*} (w, b) = \frac {\max (0 , 1 - (b + w ^ {\prime} x _ {i}))}{| w _ {j ^ {*}} |}
$$

we have

$$
d _ {i} (w, b) = \left\{ \begin{array}{l l} z _ {i} ^ {*} (w, b) 1 _ {j ^ {*}} & \text { if } (c _ {i}) _ {j ^ {*}} z _ {i} ^ {*} (w, b) \leq r _ {i} \\ 0 & \text { otherwise } \end{array} \right.
$$

As for the principal, Boylu et al. [6] considered asymmetric costs of misclassi<sup>fi</sup>cation and a consumer good-will penalty imposed on requiring true positive customers to exert effort to obtain a positive classi<sup>fi</sup>cation. That is, without this consideration, their induction method stressed generalization improvements resulting from requiring true positive agents to exert effort to retain a positive labeling.

So, in our setting, net income would be computed by

$$
Z = I - \lambda \sum_ {y _ {i} = + 1} w ^ {\prime} D (w) d _ {i} (w, b) - \sum_ {i = 1} ^ {\ell} C _ {y _ {i}} \xi_ {i}\tag{4}
$$

where $I { > } 0$ is the principal's net income from all sources not directly considered, $0 { < } C _ { + 1 } { < } C _ { - 1 }$ re<sup>fl</sup>ects the asymmetric costs for misclassi<sup>fi</sup>cation amounts

$$
\xi_ {i} = \max \left\{0, 1 - y _ {i} (w ^ {\prime} x _ {i} + w ^ {\prime} D (w) d _ {i} (w, b) + b) \right\}
$$

and $0 { \leq } \lambda { < } C _ { + 1 }$ is a penalty associated with requiring positive customers to exert effort to remain positive. Boylu et al. [6] implicitly used a linear utility function giving, in the principal–agent learning setting, $U ( Z ) = Z .$

A 1-norm version of the principal's problem reduces, under the structural risk minimization principle, to:

$$
\begin{array}{l} \min _ {w, b} | w | + \gamma \Bigg (\lambda \sum_ {y _ {i} = + 1} w ^ {\prime} D (w) d _ {i} (w, b) + \sum_ {i = 1} ^ {\ell} C _ {y _ {i}} \xi_ {i} \Bigg) \\ \text {s.t.} y _ {i} \{w ^ {\prime} x _ {i} + w ^ {\prime} D (w) d _ {i} (w, b) + b \} \geq 1 - \xi_ {i} i = 1, \dots , \ell \end{array}\tag{5}
$$

where $\gamma { > } 0$ re<sup>fl</sup>ects the trade-off between empirical and structural risk in line with the principal's utility.

Surprisingly, they were able to characterize a solution to the $2 \AA ^ { - }$ norm version of Eq. (5) for a special case as shown below. This is summarized in the following Theorem.

Theorem. If

(1) all agents have the same utility functions and individual rationality constraints,

(2) $\lambda { = } 0 , \gamma { = } 1$

and

(3) S is linearly separable

then $( w ^ { * } , b ^ { * } )$ solves

$$
\begin{array}{l} \min _ {w, b} w ^ {\prime} w \\ \text { s.t. } \quad y _ {i} \{w ^ {\prime} x _ {i} + b \} \geq 1 \quad i = 1, \ldots , \ell \end{array}
$$

if and only if $\left( \frac { 2 } { 2 + . t ^ { * } } \boldsymbol { W } ^ { * } , \frac { 2 \boldsymbol { b } ^ { * } - \boldsymbol { t } ^ { * } } { 2 + \boldsymbol { t } ^ { * } } \right)$ solves the 2-norm version of Eq. (5) where $t ^ { * }$ is given by

$$
t ^ {*} = r \max _ {j} | w _ {j} ^ {*} | / c _ {j}.
$$

This says that for the 2-norm version of strategic learning, under the required conditions, a solution that ignores agent strategic gaming $( w ^ { * } , b ^ { * } )$ can be altered (by scaling and shifting the hyperplane) to form a solution to the principal–agent problem. For the general problem where these assumptions don't hold they present a mixed integer programming formulation (see Table 2) that is useful for relatively small instances. In Boylu et al. [4] a genetic algorithm is developed that produces good approximate solutions to the 2-norm strategic learning version of Eq. (5) in reasonable time. For both the special and general cases, they show the solutions to strategic learning are Nash Equilibria for the accompanying game-theoretic version of the problem.

## 6. Principal–agent induction process

Here we brie<sup>fl</sup>y summarize the overall induction process for principal–agent learning. The 1-norm model, Eq. (5), differs from the strategic learning model of Boylu et al. [6] only by the inclusion of the parameter γ which is dependent on the principal's utility function and captures different weighting between empirical and structural risk resulting from $A \leq L ( \mathbf { \varepsilon } ) \leq B .$ . Thus, before solving Eq. (5), one needs to determine parameter γ. This is more involved than just determining A and B since there are also trade-offs with other terms in the SVM problem (e.g., the term penalizing forcing positive agents to move to retain a positive labeling). To determine γ, we search for γ using a grid search solving Eq. (5) for each candidate value and using the results to compute the principal's expected utility. The solution to Eq. (5) for the maximizing γ is the solution we use to solve the principal–agent learning problem.

An MIP for the general case (formulation P4).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(2-Norm)  $\min_{\xi_{i}\geq0}w'w+\sum_{i=1}^{r}C_{y_{i}}\xi_{i}+\lambda\sum_{y_{i}=1}q_{i}$  or
(1-Norm)  $\min_{\xi_{i}\geq0}\sum_{j=1}^{n}\left(w_{j}^{+}+w_{j}^{-}\right)+\sum_{i=1}^{r}C_{y_{i}}\xi_{i}+\lambda\sum_{y_{i}=1}q_{i}$ 
s.t.
effort( $y_{i}=+1$ ):
 $w'x_{i}+b+q_{i}\geq1-\xi_{i}$ $M-MV_{i}\geq\xi_{i}$ $MV_{i}\geq q_{i}\geq0$ $t_{i}\geq q_{i}$ 
effort( $y_{i}=-1$ ):
 $-w'x_{i}-b\geq1-\xi_{i}$ $\xi_{i}\geq2V_{i}$ $1-w'x_{i}-b+MV_{i}\geq t_{i}+\varepsilon$ 
max adjustment:
 $r_{i}\frac{(w^{+}+w^{-})_{j}}{(c_{i})_{j}}\leq t_{i}\leq r_{i}\frac{(w^{+}+w^{-})_{j}}{(c_{i})_{j}}+MH_{ij}\quad j=1,\ldots,n,i=1,\ldots,\ell$ $\sum H_{ij}=n-1$ $i=1,\ldots,\ell$ 
absolute value:
 $w=w^{+}-w^{-}$ $M_{I}l_{j}\geq w_{j}^{+}\geq0$ $j=1,\ldots,n$ $M_{I}-M_{I}l_{j}\geq w_{j}^{-}\geq0$ $j=1,\ldots,n$ 
integrality:
 $I_{j},H_{ij},V_{i}\in\{0,1\}$
</div>

## 7. Illustrative example of the principal–agent learning problem

We illustrate the principal–agent learning model using a credit approval problem. The starting data for this problem is publicly available at the UCI repository (http://www.ics.uci.edu/\~mlearn/MLRepository. html) and is referred to as credit-screening data. We randomly sampled 400 instances having no missing values. There are 15 attributes (6 numerical and 9 categorical). All categorical attributes were replaced by binary dummy variables yielding 40 attributes in all. We used a strati<sup>fi</sup>ed, 5-fold cross validation sampling analysis on the 400 cases. Here we set $C _ { - 1 } { = } 1 . 1 , C _ { + 1 } { = } 1 . 0 , \nu _ { i } { - } \bar { u } _ { i } { = } 3 0$ and $\lambda { = } 0 . 8$ for Problem (5) and for the MIP of Table $2 \varepsilon = 1 0 ^ { - 7 } , M = 1 0 , 0 0 0$ , and $M _ { I } = 1 0 0$

In Boylu et al. [6] the principal implicitly used a linear utility $U ( Z ) = Z .$ Agents also used a linear utility as discussed in Section 5. Here we illustrate our proposed setting by assuming the principal has a more commonly employed utility function, a constant absolute risk aversion utility function (see Safra and Segal [30]) of $U ( Z ) = - e ^ { - p Z }$ where p is the Arrow–Pratt risk aversion parameter. Thus

$$
L () = - U () = e ^ {p \left(\lambda \sum_ {y _ {i} = + 1} w ^ {\prime} D (w) d _ {i} (w, b) + \sum_ {i = 1} ^ {f} C y _ {i} \zeta_ {i} - I\right)}.
$$

We use parameter values I=80 and $p = 0 . 5 .$

We conduct a series of inductions comparing the resulting principal's utility using three scenarios. In the <sup>fi</sup>rst, we assume the principal ignores any agent strategic activity or utility considerations and just uses SVM to determine his classi<sup>fi</sup>er. We call these inductions the non-strategic SVM solutions. In the second scenario we assume the principal takes into account strategic agent behavior but not his own utility considerations. This is the case studied by Boylu et al. [6] and we call these inductions the strategic learning solutions. In the third scenario the principal considers strategic agent behavior and his own utility considerations. We call these inductions the principal–agent solutions. In performing the principal– agent induction discussed in Section 6, we employed a coarse grid search over γ∈[1,50] using increments of 0.1 yielding γ values for the <sup>fi</sup>ve training sets of 47.2, 3.2, 36.3,17.3 and 23, respectively. All principal–agent solutions and strategic learning solutions were found using CPlex 10.2 [18] on the 1-norm problem of Table 2 (where parameter γ is added for the principal–agent problems). Weka [36] was used to solve the nonstrategic SVM solutions.

Table 3 compares the average of the <sup>fi</sup>ve principal–agent solutions to the average of the <sup>fi</sup>ve non-strategic SVM solutions and the strategic learning solutions of Boylu et al. [6]. The principal's utility is reported as the value $- p \Big ( \lambda \sum _ { y _ { i } = { ~ + ~ } 1 } w \prime D ( w ) d _ { i } ( w , b ) + \sum _ { i = 1 } ^ { \ell } ~ C _ { y _ { i } } \xi _ { i } - I \Big )$ which is the negative of the exponent of the utility function (the negative is used so that increasing values re<sup>fl</sup>ect increasing utilities). Hence, the average of these values re<sup>fl</sup>ects a geometric average of the utilities.

We see in the training cases that, on average, the principal–agent version returns more utility to the principal. This is consistent with the principal's goal to maximize utility. Both dominate and are very different from a SVM solution that ignores strategic behavior. We also see that the principal–agent version misclassi<sup>fi</sup>es fewer negative cases and more positive cases than does the strategic learning solutions and both misclassify fewer negative cases and more positive cases than the non-strategic SVM solutions. We also see that the principal–agent version prevents more negative cases from altering their attributes to attain a positive classi<sup>fi</sup>cation than do the strategic learning solutions (the agents who altered their attributes are said to have “moved” in Table 3). Both prevent more movement than does the non-strategic SVM solutions. Likewise, the principal–agent version forces more positive agents to expend effort to retain a positive classi<sup>fi</sup>cation (i.e., more moved) than do the strategic learning solutions. Both force more than do the SVM solutions. This is consistent with the misclassi<sup>fi</sup>cation results. In short, the more utility the principal extracts, the more positive agents must work to retain a positive classi<sup>fi</sup>cation and the more negative agents are restricted from strategic activity. This is also consistent with our choice of parameters satisfying $C _ { - 1 } { > } C _ { + 1 } { > } \lambda$

In terms of generalization, we see the same patterns, the average principal–agent utility is greater than the average from the strategic learning solutions and both dominate the SVM solution that ignores strategic behavior (see the results on the test set). We also see the same pattern in misclassifying fewer negative cases and more positive cases and in forcing more strategic activity by positive agents and less by negative agents. In short, the methodology appears to generalize well and the outcomes have strong face validity giving results that were anticipated.

With only one exception (the number of negatives moved) all results of paired t-tests were statistically signi<sup>fi</sup>cant at the 0.05 level for results of non-strategic SVM training solutions versus principal– agent learning and all but one case (the number of positive misclassi<sup>fi</sup>cations) for non-strategic SVM solutions versus the strategic learning solutions. For the test sets all were signi<sup>fi</sup>cant at the 0.075 level except for the number of negatives moved. As can be seen in Table 3, the principal–agent solutions and strategic learning solutions are much closer to each other and none pass a statistically signi<sup>fi</sup>cant difference at the 0.10 level. This is the result of parameter choices that impact the utility function and the sample sizes. Indeed, for sample 2 the γ value of 3.2 resulted in a principal–agent solution very close to the strategic learning solution (recall that the strategic learning model has an implicit value of γ of 1.0). However, the average performance as discussed above demonstrates the general tendency of these treatments.

## 8. Conclusions and future directions

In this paper, we focused on supervised learning for classi<sup>fi</sup>cation tasks and gave a formal model for principal–agent learning that is independent of the speci<sup>fi</sup>c learning method or hypothesis space. In this model the main concern is to maximize the learner's utility during induction when the subjects of classi<sup>fi</sup>cation are selfinterested units. This is a new paradigm that is applicable to many data mining problems. As a speci<sup>fi</sup>c example, we considered a principal with a constant absolute risk aversion utility function, agents having linear utilities, a linear discriminant hypothesis space and SVM learning. A credit approval problem was used to illustrate the procedure and bene<sup>fi</sup>ts.

In principal–agent learning, the learner plays the role of a principal who seeks to classify agents who are also utility maximizing entities. Interestingly, in this setting, both principal and agents aim to maximize their own utilities turning them into adversaries each with con<sup>fl</sup>icting goals of interest (i.e., maximizing their own utility).

Table 3 Comparison of solutions.

<table><tr><td colspan="2"></td><td>Positives moved</td><td>Negatives moved</td><td>Pos. misclassifications</td><td>Neg. misclassifications</td><td>Principal&#x27;s utility</td></tr><tr><td rowspan="3">Train</td><td>Non-strategic</td><td>2.6 (3.4)</td><td>39.4 (50.3)</td><td>3.4 (5.1)</td><td>177.6 (0.5)</td><td>-159.4 (65.4)</td></tr><tr><td>Strategic</td><td>22.0 (21.9)</td><td>20.8 (35.5)</td><td>9.8 (5.8)</td><td>47.0 (28.6)</td><td>-21.0 (36.5)</td></tr><tr><td>Principal agent</td><td>30.6 (3.6)</td><td>7.2 (1.9)</td><td>12.4 (5.6)</td><td>30.8 (5.0)</td><td>-4.1 (3.5)</td></tr><tr><td rowspan="3">Test</td><td>Non-Strategic</td><td>0.6 (0.5)</td><td>9.6 (13.7)</td><td>1.2 (2.1)</td><td>44.4 (0.5)</td><td>-13.4 (15.4)</td></tr><tr><td>Strategic</td><td>4.0 (4.8)</td><td>5.6 (7.6)</td><td>5.0 (4.6)</td><td>13.4 (3.6)</td><td>19.9 (4.5)</td></tr><tr><td>Principal agent</td><td>7.6 (1.1)</td><td>4.2 (3.1)</td><td>5.8 (2.9)</td><td>12.2 (4.8)</td><td>20.8 (4.7)</td></tr></table>

Values are averages (standard deviations).

As with utility-based learning, principal–agent learning has many avenues of potential research. We showed here how the work by Boylu et al. [6] <sup>fi</sup>ts this paradigm (with a linear utility function). This used support vector machine induction. Other induction models like decision trees, nearest neighbor, neural networks, etc. need to be examined in this context.

It is well-known that as sample size increases the structural error decreases given o( ) is expressive enough to approximate the target function. It is also known that as the capacity of the function class (h) increases the structural error increases. For linear functions h=n+1. From the perspective of the principal collecting more data, (i.e., higher l and n values), a <sup>fi</sup>rst impact is to decreases utility as it costs more to collect more data, yet the right n and higher l is likely to decrease structural error and hence increase the overall utility with improved decision making resulting from the induction process. Incorporating the question of feature selection and data collection into the formulation of a utility maximizing principal would be a valuable contribution.

The principal–agent problem [21] that economists focus their analysis on is most commonly related with the cases where the principal is less informed. The current research assumes that the principal knows about certain parameters such as the costs and the problem that the agent faces. A major area of future research is when the parties involved are less omniscient as such information is not available in practice. In such cases, a principal and agents usually try to roughly predict each others' parameters. Several formulations for those cases have been presented (Boylu et al. [6]) but many questions and alternative avenues of investigation still remain open.

In addition, the agent problem can be extended to allow the utility function to also be a function of a random component (like the state of current economic conditions), whereinwe would change the optimization objective and individual rationality. This would be an interesting extension.

## References

[1] A. Arnt, S. Zilberstein, Learning policies for sequential time and cost sensitive classi<sup>fi</sup>cation, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 39–46.

[2] S. Bhattacharyya, K.K. Tharakunnel, Reinforcement Learning in Leader–Follower Multiagent Systems: Framework and an algorithm, Information and Decision Sciences, University of Illinois, Chicago, IL, 2005

[3] F. Boylu, H. Aytug, G.J. Koehler, Learning in the presence of self-interested agents, Proceedings of the 39th Annual Hawaii International Conference on System Sciences (HICSS'06), Track, vol. 7, 2006.

[4] F. Boylu, H. Aytug, G.J. Koehler, Using genetic algorithms to solve the strategic learning problem, Proceedings of the INFORMS 06 Workshop on Arti<sup>fi</sup>cial Intelligence and Data Mining, Pittsburg, PA, 2006.

[5] F. Boylu, H. Aytug, G.J. Koehler, Systems for strategic learning, Information Systems and E-Business Management 6 (2) (2008) 205–220.

[6] F. Boylu, H. Aytug, G.J. Koehler, Induction over strategic agents, Information Systems Research (in press).

[7] P.S. Bradley, O.L. Mangasarian, Feature selection via concave minimization and support vector machines, in: Jude W. Shavlik (Ed.), Proceedings of the Fifteenth International Conference on Machine Learning, July 24–27 1998, Madison, Wisconsin, USA.

[8] M. Chau, H. Chen, A machine learning approach to web page <sup>fi</sup>ltering using content and structure analysis, Decision Support Systems 44 (2) (2008).

[9] M. Ciraco, M. Rogalewski, G. Weiss, Improving classi<sup>fi</sup>er utility by altering the misclassi<sup>fi</sup>cation cost ratio, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 46–53.

[10] N. Cristianini, J. Shawe-Taylor, An Introduction to Support Vector Machines and Other Kernel-based Methods, Cambridge University Press, Cambridge, UK, 2000.

[11] S. Crone, S. Lessmann, R. Stahlblock, Utility based data mining for time series analysis: cost sensitive learning for neural network predictors, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 59–69.

[12] N. Dalvi, P. Domingos, Mausam, S. Sanghai, D. Verma, Adversarial classi<sup>fi</sup>cation, Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), Seattle, 2004, pp. 99–108.

[13] R. Eisenbeis, Discussion, Supplement to Srinivasan, V. and Kim, Y. H. 1987, Credit granting: A comparative analysis of classi<sup>fi</sup>cation procedures. J. Fin. 42(3) 665–680 (1987).

[14] G. Fung, O.L. Mangasarian, A feature selection Newton method for support vector machine classi<sup>fi</sup>cation, Data Mining Institute Technical Report 02-03, University of Wisconsin, Madison, 2002.

[15] R. Holte, C. Drummond, Cost-sensitive classi<sup>fi</sup>er evaluation, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, p. 3.

[16] Z. Huang, H. Chen, C. Hsu, W. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[17] L. Hurwicz, On informationally decentralized systems, in: R. Rardner, B. Mcguire (Eds.), Decision and Organization, North Holland Press, Amsterdam, 1972, pp. 297–336.

[18] ILOG, ILOG CPLEX, Reference Manual and User Manual, ILOG, Gentilly, France, 2007 V10.2.

[19] Z. Jiang, V.S. Mookerjee, S. Sarkar, Lying on the web: implications for expert systems redesign, Information System Research 16 (2) (2005) 131–148.

[20] A. Kapoor, R. Greiner, Reinforcement learning for active model selection, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 17–24.

[21] J.J. Laffont, D. Martimort, The Theory of Incentives: The Principal–Agent Model, Princeton University Press, Princeton, NJ, 2002.

[22] M. Mannino, M. Koushik, The cost minimizing inverse classi<sup>fi</sup>cation problem: a genetic algorithm approach, Decision Support Systems 29 (3) (2000) 283–300.

[23] D. Martens, L.M.L. Bruynseels, B. Baesens, M.M.T.A. Willekens, J. Vanthienen, Predicting going concern opinion with data mining, Decision Support Systems 45 (4) (2008) 765–777.

[24] K. McCarthy, B. Zabar, G. Weiss, Does cost-sensitive learning beat sampling for classifying rare classes? Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 69–78.

[25] P. Melville, M. Saar-Tsechansky, F. Provost, R. Mooney, Economical active featurevalue acquisition through expected utility estimation, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 10–17.

[26] C. Morrison, P. Cohen, Noisy information value in utility-based decision making, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 34–39.

[27] J. Porter, A Booming Business in MBA Coaches, 2007 http://www.businessweek. com/bschools/content/may2007/bs20070524\_906621.htm

[28] F.J. Provost, Toward Economic machine learning and utility based data mining, Proceedings of the ACM SIGKDD Workshop on Utility-based Data Mining, Chicago, IL, 2005, p. 1.

[29] M. Saar-Tsechansky, F. Provost, Decision-centric active learning of binary-outcome models, Information Systems Research 18 (1).(2007) 4–22

[30] Z. Safra, U. Segal, Constant risk aversion, Journal of Economic Theory 83 (1) (1998) 19–42.

[31] D. Song, R.Y.K. Lau, P.D. Bruza, K. Wong, D. Chen, An intelligent information agent for document title classi<sup>fi</sup>cation and <sup>fi</sup>ltering in document-intensive domains, Decision Support Systems 44 (1) (2007) 251–265.

[32] R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, MIT Press, Cambridge, MA, 1998.

[33] T. Van Gestel, B. Baesens, P. Van Dijcke, J. Garcia, J.A.K. Suykens, J. Vanthienen, A process model to develop an internal rating system: sovereign credit ratings, Decision Support Systems 42 (2) (2006) 1131–1151.

[34] V. Vapnik, Statistical Learning Theory, John Wiley & Sons, New York, NY, 1998.

[35] V. Vapnik, A. Chervonenkis, The necessary and suf<sup>fi</sup>cient conditions for uniform convergence of means to their expectations, Theory of Probability and its Applications 26 (1981) 532-553

[36] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, 2nd Edition, Morgan Kaufmann, San Francisco, 2005.

[37] B. Zadrozny, One-bene<sup>fi</sup>t learning: cost-sensitive learning with restricted cost information, Proceedings of the KDD-05 Workshop on Utility-Based Data Mining, Chicago, IL, 2005, pp. 53–59.

Fidan Boylu is an assistant professor in the School of Business at the University of Connecticut. She has a B.S. degree in electrical and electronics engineering, an MBA and Ph.D. from University of Florida. Her research interests include data mining and machine learning, Her work was nominated for a best paper award in HICCS 2006, She has taught courses on system analysis and design, business information systems and database management.

Haldun Aytug is an associate professor in the Warrington School of Business at the University of Florida. Dr. Aytug's current research focuses on machine learning applications and capacity modeling for e-commerce applications. His research has been funded by the National Science Foundation, Intel Corporation and Applied Materials. He has published in INFORMS Journal on Computing, Decision Support Systems, European Journal of Operational Research among others.

Gary I. Koehler is the John B. Higdon Eminent Scholar and Professor of Information Systems and Operations Management in the Warrington School of Business at the University of Florida. He has published in Decision Support Systems, Operations Research, Management Science, Informs Journal on Computing, Evolutionary Computations, SIAM Journal on Control and Optimization, Annals of Operations Research, European Journal of Operational Research, Decision Sciences, Journal of Finance and others. His current research interests are in e-commerce related areas.
