---
otero_id: 17279
otero_key: "5CCVG4PK"
title: "An economics perspective on the usefulness of decision support systems"
authors: "Rajiv M. Dewan"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90051-p"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An economics perspective on the usefulness of decision support systems

Rajiv M. Dewan

Northwestern University, Evanston, IL 60208, USA

Decision making in a decision support system is modeled as a sequential information acquisition process with noisy information sources and costly information assimilation. The net benefit from using a Decision Support Systems approach is compared to that from a Programs approach. DSS provides greater benefits for ad-hoc decisions and this advantage increases as the information sources become noisier. Programs are preferred for recurrent decisions. Increased assimilation costs decrease the number of alternatives examined.

Keywords: Decision Support Systems, Programs, Planning, Noisy information, Economics model, Ad-hoc decisions, Recurrent decisions, Institutional Decision Support Systems, Bayesian update cost, Information assimilation cost.

![](/api/attachments/5CCVG4PK/fulltext/images/7f83d398d247640a71908cd6a6c5c0fc74a56456bc2f99da5dc77271f7d30588.jpg)

Rajiv M. Dewan received his Ph.D. in Business with a concentration in Computers and Information Systems from the University of Rochester in 1986. He is interested in application of economics to issues in information management, database design, design of computer, computer networks and interaction between information systems design and other functional areas of business management.

## 1. Introduction

The decision making process can be broken down into three phases which are intelligence, design and choice $[16]$ . Decision Support Systems represent a significant advance in the use of Information Technology in business organizations because they support all of the phases of the decision making process. An end-user is responsible not only for making a business decision but also for planning and executing processes for acquiring the information needed to make the decision. The planning in such systems is evolutionary, in that, it evolves with the sequentially acquired information. Indeed, in unstructured environments, in which ‘optimal’ solutions are rarely found, the decision making process is central to timely and effective decisions. In such environments, the emphasis of decision making is not only on the final decision but on the whole decision making process.

Early in the literature on decision making in business, Simon suggested that decision processes fall along a continuum with Programs being at one extreme and DSS at the other extreme [16]. From then on, considerable attention has been focussed on factors that affect the choice of decision processes and, in particular, the choice of Decision Support Systems over Programs $^{1}$ . The work in this area can be classified by the perspective used: Administrative, activity based or behavioral.

Following Simon's administrative viewpoint, Gorry and Scott-Morton [9] and Keen and Scott-Morton [12] classify decisions into Structured, Semi-Structured and Unstructured, depending on whether the goals, processes, input and output for the different phases of the decision making process are clearly specified. The DSS approach is posited to be better suited for unstructured decisions while Programs are better suited for structured decisions.

Anthony [2] classified decisions based on managerial activities into operational, managerial and strategic. Strategic decisions are generally unstructured. The inputs to the decision and their impact on decisions are generally not clear. At one extreme, DSS are better for strategic decisions while, at the other extreme, Programs are favored for operational decisions.

Cyert and March [4] using a behavioral perspective showed that local rationality and sequential attention to goals are hallmarks of decision making at higher levels of a business organization. These are key features of the DSS approach to decision making and hence such systems are better suited to business decision making.

While only the three basic regimes of analysis of decision making have been discussed above, many composite views and empirical evidence about DSS usage in different environments have been presented in $[1,3,10,13,17,18,19]$ and others.

As in [7] and [15], an economic perspective to usefulness of Decision Support Systems approach is presented in this paper. In the spirit of Cyert and March's behavioral perspective, the DSS decision making process is modelled in this paper as a sequential information acquisition process that leads to a final decision. The Programs approach, in which all the planning is done ex-ante, is used as a bench mark to compare the performance of DSS in different settings. The focus of the paper is on the choice of a decision making approach, DSS or Programs, that results in highest value net of all decision making costs including the planning costs. Factors that influence this choice are examined.

Many environmental factors play a role in determining the choice of an approach $^{2}$ . These factors are examined by Keen in [11]. In this paper we focus on two factors, Bayesian update cost and noisiness of information sources, that capture some of the notion of unstructuredness in business.

Noisiness of information sources is endemic in strategic business decision making. This is because the effect of information gathered in an unstructured environment on the decision is rarely unambiguous or certain. There are probabilities of error associated with, both, information generation and inference. For instance, interest rate may play a role in forecast of car sales but the interest rate forecast and its effect on car sales cannot be stated with unlimited precision. Contrast this to a more structured environment of determination of bond value given a spot interest rate. The relationship between bond value and interest is well specified and the measurement of spot rate may involve very little error. This is a structured environment and a program can be easily written to compute this. Indeed, many such programs are available.

The Bayesian update cost is defined to be the cost of assimilation of information. It excludes the cost of generation of the information. To appreciate the concept of Bayesian update cost, ponder on the following thought experiment.

A thought experiment. Consider a manager making a strategic decision about plant capacity. The forecast of sales depends on numerous environmental factors and the manager may use a variety of data and programmed models, called modules in this paper, to make the decision. Suppose that the manager is presented with a very fast processor that makes the time taken to run modules negligible. Even in this case the time taken to make the decision may not be negligible. This is the ‘human processing’ time and its cost is the Bayesian update cost.

The cost associated with ‘human processing’ is called the Bayesian update cost or the information assimilation cost. All costs related to module usage that are not captured in the Bayesian update cost are lumped into module usage cost.. Unstructured environments are considered to be ‘fuzzy’ and complicated. Decisions in such environments require greater ‘human processing’ than ones in a structured environment. Thus the Bayesian update reflects the difficulty of making decisions in such environments.

It is important to note that when a decision maker plans a program then the planning cost includes the Bayesian update cost of each module that the plans to use. This is because the control structure of a program is determined by the effect of potential information that may be revealed by a module. This is in contrast to the DSS approach in which this cost is not incurred until the decision maker has that information to contend with. This makes planning a program very expensive in environments with Bayesian update cost. However, if this decision is recurrent, then this cost may be amortized over several instances of the decision. In case of DSS, the planning cost cannot, in general, be amortized $^{3}$ .

The results obtained from the economics perspective in this paper agree with the results from the perspectives outlined above. Using the model it is shown that the decision making process in DSS is ‘locally optimal’—a key feature of business decision making that is identified by Cyert and March. Further more, the planning is evolutionary and takes the information available at every stage into account. This also agrees with Cyert and March’s results.

In this paper it is shown that DSS is preferred for ad-hoc decisions when the information is noisy and, further more, that this preference is strengthened when the information becomes noisier. This agrees with previously reported preference for DSS in unstructured [9] and strategic [2] decision making in business environments [4]—all in environments that have noisy information sources. The effect of noisiness on approach choice for recurrent decisions is some what counter-intuitive: If the decisions are often repeated, then noisier information sources may make Programs approach more preferable because the extra cost of planning for gathering more, albeit inferior, information is amortized over a large number of decisions.

The evolutionary nature of the DSS reduces the amount of planning that has to be done ex-ante. Hence in presence of Bayesian update costs, the DSS approach is preferred for ad-hoc decisions. For recurrent decisions, the cost is amortized over many decisions and the program or the Institutional DSS approach as in [8] may be preferred. The frequency of decision making at which this switch takes place depends on the update cost and noisiness of modules.

A mathematical model of economic choice of best decision making approach is presented in the next section. The section following that is devoted to analyzing the model and presenting some insights into the usefulness of DSS over Programs.

## 2. Model

A model of decision environment that is similar, in spirit, to that in [15] is used in this paper. The decision environment is described by an eight tuple

$$
D = \langle \tilde {x}, \xi , \Delta , \mathscr {Y}, M, F (\cdot), b (\cdot), c (\cdot) \rangle .
$$

A random variable, $\tilde{x} \in R$ , is defined on the outcome space of the decision problem and $\xi$ is the probability induced on $\tilde{x}$ by the distribution of outcomes. The induced distribution is assumed to be a part of decision maker's prior beliefs.

The decision maker may use a number of modules to gather information before making a final decision from a set, $\Delta$ , of final decisions. Each decision results in a different payoff function. Hence, by composition of functions, the decision may be viewed as a map from outcomes to payoffs. The payoff of state x is $\delta(x)$ if $\delta \in \Delta$ is chosen. The set $\Delta$ is assumed to be absolutely bounded by $\bar{\delta}$ .

The decision maker has a portfolio of modules, denoted by the set Y, from which he may select individual modules with replacement. The decision maker may use at most M modules. This limit may arise for technological reasons such as a time constraint or for economic reasons such as a wealth constraint $^{4}$ . Individual modules are denoted by Y and signals from modules are denoted by y. A sequence of signals, $y_{1},\ldots,y_{m}$ , is called a response and is often denoted by $\vec{y}$ . Let $\theta$ denote a null response. The modules may be noisy, i.e., for some $x\in X$ , $P[y|x]<1$ for all Y=y. However, they may change the decision maker's beliefs about the distribution over the outcomes. The beliefs are expressed as a set of likelihood functions $F(Y_{1}=y_{1},\ldots,Y_{m}=y_{m}\mid\tilde{X}=x)$ where $F(\cdot)$ is the conditional distribution of response $y_{1}$ from $Y_{1},\ldots,y_{m}$ from $Y_{m}$ for $m\leqslant M$ .

Two kinds of costs are modeled in this paper — Bayesian update and planning cost and module usage cost. The Bayesian update cost, $b(Y)$ , is a function of the module selected. It is the cost of using any signal produced by $Y \in Y$ to update the current beliefs. The module usage cost $c(y, \vec{y})$ includes all costs related to module usage other than the planning cost. It is assumed that $b(Y) \leqslant \bar{b}$ and that $c(y, \vec{y}) \leqslant \bar{c}$ for all $Y \in Y$ , $\vec{y} \in \vec{Y}$ and Y = y. The following example serves to highlight the difference between the two costs.

Example 1. Consider a decision maker who decides to use a module Y in a program if $\vec{y}$ is a response. The decision maker has to preplan his course of action that would follow the usage of module Y. Thus he incurs a cost of $b(Y)$ . Now suppose that the probability of receiving $\vec{y}$ is p, then the module is actually executed within the program with probability p. The total cost of running the program $\nu$ times (considering only module Y) is $b(Y) + \nu p \int c(y, \vec{y}) \, \mathrm{d}F(y | \vec{y})$ . In contrast, if a Decision Support System approach is used then the decision maker defer the update to when a signal actually occurs. Hence in this case the cost would be $p\nu(b(Y) + \int c(y, \vec{y}) \, \mathrm{d}F(y | \vec{y}))^5$ .

The decision maker is assumed to be a Bayesian with a risk-neutral utility function. This implies that the decision maker uses all the information available to update his prior beliefs and picks a course of action that results in maximum expected utility. Since the decision maker is risk-neutral, he is indifferent between a lottery and its expected value. As a consequence, the decision maker can be modeled as a net expected benefit maximizer.

Consider the sequence of events when a decision maker uses a decision support system:

(1) Decide whether to use a module or make a final decision;

(2) If no module is to be used, then make a final decision and stop;

(3) Use the module, observe the signal and update beliefs;

(4) Go back to step 1.

The Bayesian decision maker uses his information to decide on a course of action at step 1 of the above sequence. But this decision, in turn, depends on subsequent decisions. Hence, the decision maker has to formulate a strategy for future decisions and pick a strategy that has highest expected net payoff. Strategies are formally defined next.

Let 0 denote a null decision and let $\vec{Y}$ denote the set of responses that may be received.

Definition 1. A strategy, denoted by $\sigma$ , is a mapping $\vec{\mathcal{Y}} \to \mathcal{Y} \cup \Delta \cup \{0\}$ .

Given the sequence of events above, not all strategies are feasible. For instance, if the strategy does not include a module after a response $y_{1}y_{2}$ , then no strategy that maps a non-null module to $y_{1}y_{2}\vec{y}$ is feasible ( $y_{1}y_{2}\vec{y}$ denotes a response whose first two signals are $y_{1}y_{2}$ ). Further, a strategy may include the use of at most M modules.

Definition 2. Any strategy that can result from the sequence of events and uses fewer than M modules is a feasible strategy.

Lemma 1. A strategy is feasible if and only if

$$
\begin{array}{l} \sigma (\theta) \in \mathcal {Y} \cup \Delta , \\ \sigma (Y _ {1} = y _ {1}) \\ \in \left\{ \begin{array}{l l} \mathcal {Y} \cup \Delta & \text { if } \sigma (\theta) = Y _ {1} \quad \text { and } 1 <   M, \\ \{0 \} & \text { otherwise. } \end{array} \right. \\ \sigma (Y _ {1} = y _ {1}, \ldots , Y _ {m} = y _ {m}) \\ \in \left\{ \begin{array}{l l} \mathcal {Y} \cup \Delta & \text { if } \sigma (Y _ {1} = y _ {1}, \ldots , Y _ {m - 1} = y _ {m - 1}) \\ & = Y _ {m} \quad \text { for } m <   M, \\ \Delta & \text { if } m = M, \\ \{0 \} & \text { otherwise. } \end{array} \right. \end{array}
$$

Proof. Let $\sigma$ be a feasible strategy generated by the sequence of events. Consider the decision maker at the start when he has not yet received any responses and $M > 0$ . He has the option of using a module or making a final decision. Hence $\sigma(\theta) \in \mathcal{Y} \cup \Delta$ for $M > 0$ . Now assume that his is true for $m - 1 < M$ . Since the response is produced by this sequence, $\sigma(y_1, \ldots, y_{m-2}) = Y_{m-1}$ ad so on to $\sigma(\theta) = Y_1$ . If $m = M$ then the decision maker has to make a final decision, i.e., $\sigma(\vec{y}) \in \Delta$ . If $m < M$ then he may use another module or make a final decision. Hence $\sigma(\vec{y})\in\mathcal{Y}\cup\Delta$ . By induction we are done. $\square$

Given any strategy satisfying the hypothesis, consider the following procedure:

0. $\tilde{y} = \theta$ ;

1. If $\sigma(\vec{y}) \in \Delta$ then do not use any modules and instead make the final decision $\sigma(\vec{y})$ and STOP;

2. If $\sigma(\vec{y}) \in \mathcal{Y}$ then use the module $\sigma(\vec{y})$ . Let $\vec{y} = \vec{y} y$ where $y$ is the signal from $\sigma(\vec{y})$ ;

3. Go to step 1.

This procedure has the same sequence of events as above and is feasible.

Let $\Sigma_{M}$ denote the set of feasible strategies that use M or fewer modules. The definition of strategy in this paper does not require finiteness of the set of modules, signal spaces or decisions. To forestall measurability problems, we assume that $b(\cdot)$ , $c(\cdot)$ and $\delta(\cdot)$ are uniformly bounded over their domains. Further, the noise in modules is explicitly modeled. While a decision problem with noisy information can be remodeled, without loss of generality, as another with noise free information $^{6}$ , this redefinition complicates comparative statics of effect of noise on optimal strategies $^{7}$ . Indeed, if we make the assumptions in [15], the feasible strategy definitions in this paper can be shown to reduce to that in [15]. The following example serves to illustrate the decision making model and feasible strategies.

Example 2. Project Evaluation. Consider the following project evaluation decision setting. The project may be ‘good’ or ‘bad’, i.e., $\tilde{x} \in \{Good, Bad\}$ . The prior distribution of outcomes is $\xi(\tilde{x} = Good) = g$ and $\xi(\tilde{x} = Bad) = 1 - g$ . At each stage, the decision maker has a final decision of either implementing the project (denoted D) or rejecting the project (denoted R). Hence $\Delta = \{D, R\}$ . The matrix below describes the payoff.

<table><tr><td></td><td>D</td><td>R</td></tr><tr><td>Good</td><td> $x_{1}$ </td><td>0</td></tr><tr><td>Bad</td><td> $-x_{2}$ </td><td>0</td></tr></table>

The decision maker has a module available that he may use again and again. The module generates a 'Yes' or a 'No' signal. A 'Yes' signal is obtained with a probability of $p_1$ when the project is good and with probability $p_2$ when it is bad. Without loss of generality, the 'Yes' signal is assumed to increase the probability of good project and 'No' to decrease it $^8$ . Hence the module may signal 'No' when the project is good (Type I error) with probability $1 - p_1$ and signal 'Yes' when the project is bad (Type II error) with probability $p_2$ . Hence $P[Y|Good] = 1 - P[N|Good] = p_1$ and $P[Y|Bad] = 1 - P[N|Bad] = p_2$ . Each use of the module is independent, i.e., $P(y_1, \ldots, y_m|x) = \Pi_{i=1}^m P(y_i|x)$ . This specifies the likelihood functions. Let $b$ and $c$ be the constant Bayesian update and usage costs respectively.

Consider the following strategy.

$$
\sigma (\theta) = \text { use   the   module },
$$

$$
\sigma (\mathrm{Y}) = \text { use   a   module },
$$

$$
\sigma (\mathbf {N}) = \text { use   a   module },
$$

$$
\sigma (\mathbf {Y Y}) = \text { do   the   project },
$$

$$
\sigma (\mathrm{YN}) = \text { use   a   module },
$$

$$
\sigma (\mathbf {N Y}) = \text { use   a   module },
$$

$$
\sigma (\mathbf {N N}) = \text { reject   the   project },
$$

It can be represented by the strategy tree shown in fig. 1a where every odd (root is in level 1) level node represent responses and nodes in levels represent module usage decisions. This is similar to a game tree between nature (modules) and the decision maker.

## 2.1. Cost benefit analysis

Consider a decision maker who has received a response $\vec{y}=(Y_{1}=y_{1},\ldots,Y_{m}=y_{m})$ . Let $V_{y}$ denote the expected value of the decision at this response. If he decides to make a final decision, $\delta \in \Delta$ , he will get $\operatorname{E}[\delta(\tilde{x}) | \vec{y}]$ . On the other hand, if he elects to use a module $Y \in \mathcal{Y}$ then he will incur a planning cost of $b(Y)$ and if the module produces a signal $y$ then he will incur an additional cost that is a usage cost of $c(y, \vec{y})$ . The net expected value that he will get after using a module $Y \in \mathcal{Y}$ is $\int(V_{\vec{y}y} - b(Y) - c(y, \vec{y})) \, \mathrm{d}F(Y = y | \vec{y})$ .

![](/api/attachments/5CCVG4PK/fulltext/images/c4f236c8501abd419c5ea677879928a1599093db97db61ecb0bc6096f95e4988.jpg)  
Fig. 1a. A strategy tree.

At each stage the decision maker will pick a course of action that results in the highest expected payoff. This, in turn, depends on his expectations of outcomes from even later stages. The decision maker wants to pick a strategy that maximizes net value. Hence he wants to base his decisions on a strategy that maximizes the value. The ex-ante strategy choice problem is formulated below.

Problem D1:

$$
\max _ {\sigma \in \Sigma_ {M}} V _ {\theta}
$$

subject to

$$
V _ {\vec {y}} = \left\{ \begin{array}{l l} \int \left(V _ {\vec {y} y} - b (Y) - c (y, \vec {y})\right) \\ \quad \times \mathrm{d} F (\sigma (\vec {y}) = y | \vec {y}) & \text { if } \sigma (\vec {y}) \in \mathscr {Y}, \\ \int \delta (x) \mathrm{d} F (x | \vec {y}) & \text { if } \sigma (\vec {y}) \in \Delta , \\ 0 & \text { otherwise }. \end{array} \right.
$$

Let $\sigma^{*}$ solve an instance of the problem and let $y_{1},\ldots ,y_{m},\delta$ be a response-final decision sequence that occurs in this strategy. The final decision $\delta$ that follows the response $\vec{y}$ is shown to be the best decision that the decision maker could have made given the response.

Definition 3. A strategy, $\sigma$ , in which every sequence $y_1, \ldots, y_m$ , $\delta$ is such that $\delta \in \operatorname{argmax}_{d \in \Delta} \mathrm{E}[d(x) | \vec{y}]$ is a Bayes efficient strategy.

Let $\Sigma_M^B, \Sigma_M^B \subset \Sigma_M$ , denote the set of Bayes efficient strategies.

Lemma 2. Let $\sigma$ solve $D1$ . Then $\sigma \in \Sigma_M^B$ , i.e., $\sigma$ is Bayes efficient.

The proof is simple and is omitted here. It relies on induction to show that if $\sigma$ is not Bayes efficient then it does not solve D1 $^{9}$ .

The above lemma motivates the following definition.

Definition 4 An information gathering strategy, $\alpha : \vec{\mathcal{Y}} \to \mathcal{Y} \cup \{0\}$ , is defined as $\alpha(\vec{y}) = \sigma(\vec{y})$ if $\sigma(\vec{y}) \in \mathcal{Y}$ and $\alpha(\vec{y}) = 0$ otherwise for each strategy $\sigma$ .

Let $A_{M}$ be the set of information gathering strategies with fewer than M modules.

Information gathering strategy is a feasible strategy without specification of final action. In fact, feasible strategies may be viewed as extensions of information gathering strategies in which the final decision is also specified. By Lemma 2 only extensions in $\Sigma_{M}^{B}$ need be considered.

The problem can be formulated as a search for the best information gathering strategy.

Problem D2:

$$
\max _ {\alpha \in A _ {m}} W _ {\theta}
$$

subject to

$$
W _ {y} = \left\{ \begin{array}{l l} \int \left(W _ {\dot {y} \dot {y}} - b (Y) - c (y, \vec {y})\right) \\ \times \mathrm{d} F (\alpha (\vec {y}) = y | \vec {y}) & \text { if } \alpha (\vec {y}) \in \mathcal {Y} \\ \mathrm{E} ^ {B} [ x | \vec {y} ] & \text { otherwise } \end{array} \right.
$$

where $\mathrm{E}^B [x|\vec{y}] = \max_{\mathrm{d}\in \Delta}\int \mathrm{E}[d(x)|\vec{y} ]\mathrm{d}F(\mathbf{x}|\vec{\mathbf{y}}).$

We next show the equivalence between D1 and D2.

Lemma 3. For any $\sigma \in \Sigma_M^B$ , construct an information acquisition strategy $\alpha$

$$
\alpha (\vec {y}) = \left\{ \begin{array}{l l} \sigma (\vec {y}) & \text { if } (\vec {y}) \in \mathcal {Y}, \\ 0 & \text { otherwise }. \end{array} \right.
$$

Then $V(\vec{y}) = W(\vec{y})$ for all $\vec{y}$ such that $\sigma(\vec{y}) \in \mathcal{Y} \cup \Delta$ .

Proof. First consider any $\vec{y}$ such that $\sigma(\vec{y}) \in \Delta$ . $V_{y'} = W_{y'} = \mathrm{E}^{B}[x \mid y]$ , by formulation D1 and D2.

Now consider $\vec{y}$ such that $\sigma (\vec{y})\in \mathcal{Y}$ and $V_{y}\neq W_{y}$ .

If $V_{y'} > W_{y'}$ then $f(V_{y'y} - b(Y) - c(y, \vec{y})) \, \mathrm{d}F$ ( $y \mid \vec{y}$ ) > $f(W_{y'v} - b(Y) - c(y, \vec{y}) \, \mathrm{d}F(y \mid \vec{y})$ .

Hence $\int V_{\dot{y} y}\mathrm{d}F(y|\vec{y}) > W_{\dot{y} y}\mathrm{d}F(y|\vec{y}).$

By the monotonicity property of Lebesgue integrals over positive measures, there exists a set of responses $\vec{y}$ of positive measure such that $V_{\vec{y}} > W_{\vec{y}}$ for $\vec{y} \in \vec{Y}$ .

Now induction to M modules provides a contradiction to the first hypothesis that has been proved above. Proof follows by reductio-ad-absurdum.

Lemma 4. For any $\alpha \in A_M$ , construct the following strategy

$$
\sigma (\vec {y}) = \left\{ \begin{array}{l l} \alpha (\vec {y}) & \text {if} \alpha (\vec {y}) \in \mathcal {Y}, \\ \delta^ {*} & \text {if} \alpha (y _ {1}, \ldots , y _ {m}) = 0 \quad \text {and} \\ & \alpha (y _ {1}, \ldots , y _ {m - 1}) \in \mathcal {Y}, \\ 0 & \text {otherwise}, \end{array} \right.
$$

where $\delta^{*} \in \operatorname{argmax}_{d \in \Delta} E[\delta(x) | \vec{y}]$ . Then $\sigma(\vec{y})$ is Bayes efficient. Further, Then $V(\vec{y}) = W(\vec{y})$ for all $\vec{y}$ such that $\sigma(\vec{y}) \in \mathcal{Y} \cup \Delta$ .

The proof is similar to that of Lemma 3 and is omitted here.

These lemmas show the relationship between Bayes efficient strategies and information gathering strategies. The next theorem asserts the equivalence between formulations D1 and D2.

Theorem 1. If $\alpha$ solves $D2$ than the strategy constructed as in Lemma 4 solves $D1$ . Conversely, if $\sigma$ solves $D1$ then an information acquisition strategy constructed as in Lemma 3 solves $D2$ . Further, they have the same optimal net benefit.

Proof. Follows easily from Lemma 3 and 4 and the observation that $V_{\vec{y}}$ for $\vec{y}$ such that $\sigma(\vec{y})=0$ play no role in determining solution to the problems.

Theorem 1 validates the formulation D2. This simplifies the problem considerably as the search is restricted to $A_{M}$ which is much smaller than $\Sigma_{M}$ .

For any response $\vec{y} = (y_1, \ldots, y_m)$ let $A_{My}$ be a subset of $A_M$ with domain restricted to responses with $n$ , $m < n \leqslant M$ , signals with the first $m$ being $y_1, \ldots, y_m$ .

Theorem 2. The Bellman's optimality condition holds and the problem can be formulated as

$$
\max _ {\alpha \in A _ {M}} W _ {\theta}
$$

Subject to

$$
W _ {y ^ {\prime}} = \max _ {\alpha \in A _ {M y ^ {\prime}}} \left\{ \begin{array}{l l} \int \left(W _ {y ^ {\prime} y} - b (Y) - c (y, \vec {y})\right) \\ \times \mathrm{d} F (\alpha (\vec {y}) = y | \vec {y}) & \text { if } \alpha (\vec {y}) \in \mathcal {Y}, \\ \mathrm{E} ^ {B} [ x | \vec {y} ] & \text { otherwise } \end{array} \right.
$$

where $E^B [x\mid \vec{y}] = \max_{d\in \Delta}\int \mathrm{E}[d(\mathrm{i}x)\mid \vec{y} ]\mathrm{d}F(x\mid \vec{y}).$

Proof. Note that if $\alpha$ satisfies the constraint in the dynamic program (denoted DP) then it will satisfy the constraints in Problem D2. Hence the set of feasible and optimal strategies of the dynamic program are contained in that of D2.

To show equality, it is next shown that the set of feasible $\alpha$ for D2 is contained in the set of optimal $\alpha$ for DP.

Let $\alpha^{*}$ solve D2 with value $W_{\theta}^{*}$ but not solve DP. Then there must be some response $\vec{y}$ for which, in D2

$$
W _ {y ^ {\prime}} <   \max _ {\epsilon \in A _ {M y ^ {\prime}}} \left\{ \begin{array}{l l} \int \left(W _ {y ^ {\prime} y} - b (Y) - c (y, \vec {y})\right) \\ \times \mathrm{d} F (\alpha (\vec {y}) = y | \vec {y}) & \text { if } \alpha (\vec {y}) \in \mathcal {Y}, \\ E ^ {B} [ x | \vec {y} ] & \text { otherwise }. \end{array} \right.
$$

In this case we can strictly improve the solution to D2. This contradicts the hypothesis that $\alpha^{*}$ solves D2. The proof follows by reductio ad absurdum.

Results similar to Theorem 2, with somewhat different models, may be found in [15] and [5]. This result exhibits the optimality of sequential nature of the Decision Support Systems approach.

There is another perspective of the problem in which strategies are viewed as trees as fig. 1a in Example 2. To simplify the exhibition of this perspective, let the space of signals for each module $Y \in Y$ be countable. In this case, the nodes of the tree are countable and by induction it can be shown that

$$
\begin{array}{l} V _ {\theta} = \sum_ {\vec {y}: \sigma (\vec {y}) \in \Delta} \mathrm{E} ^ {B} \big [ x | \vec {y} \big ] \mathrm{P} \big [ \vec {Y} \big ] \\ - \sum_ {\vec {y}: \sigma (\vec {y}) \in \mathcal {Y}} c (y, \vec {y}) \mathrm{P} \big [ \vec {y} \big ] \\ - \sum_ {\vec {y}: \sigma (\vec {y}) \in \mathcal {Y}} b (\sigma (\vec {y})) \mathrm{P} \big [ \vec {y} \big ]. \end{array}
$$

Note that $\{\vec{y}:\sigma(\vec{y})\in\Delta\}$ are the leaf nodes and that $\{\vec{y}:\sigma(\vec{y})\in\mathcal{Y}\}$ are the internal nodes of the strategy tree. Hence the net benefit is the difference between the expected value at leaf nodes and the expected cost at internal nodes. Optimal strategies are the ones with the largest difference.

## 2.2. The program approach

In this approach the information acquisition strategy is not developed in an evolutionary fashion as in the Decision Support Systems approach, but it is 'hard-wired' into a program. The decision maker selects the best information gathering strategy and plans the details of Bayesian update that he would have to do after each signal of each module in the strategy. This provides the specification for the program which is then implemented $^{10}$ . Note that, in contrast, in the Design Support Systems approach the best strategy is used to pick only the next step in the acquisition process.

The problem of picking the best strategy for a program approach for a decision that is repeated $\nu$ times each period is

$$
U _ {\theta} ^ {\nu} = \max _ {\alpha \in A _ {M}} \nu U _ {\theta} - \sum_ {\vec {y}: \alpha (\vec {y}) \in \mathcal {Y}} b (\alpha (\vec {y}))
$$

subject to

$$
U _ {\vec {y}} = \left\{ \begin{array}{l} \int \left(U _ {\vec {y} \vec {y}} - c (y, \vec {y})\right) d F (\alpha (\vec {y}) = y | \vec {y}) \\ \text {if} \alpha (\vec {y}) \in \mathcal {Y}, \\ E ^ {B} [ x | \vec {y} ] \quad \text {otherwise.} \end{array} \right.
$$

Note that the second term in objective function is the planning cost of the program. All internal nodes have to be planned for.

As with the Decision Support Systems approach, it can be shown that the problem can be formulated with, both, general and information gathering strategies. Using induction it can be shown that, for any strategy,

$$
\begin{array}{l} U _ {\theta} ^ {\nu} = \nu \sum_ {\vec {y}: \sigma (\vec {y}) \in \Delta} \mathrm{E} ^ {B} \big [ x | \vec {y} \big ] \mathrm{P} \Big [ \vec {Y} \Big ] \\ - \nu \sum_ {\vec {y}: \sigma (\vec {y}) y e \mathcal {Y}} c (y, \vec {y}) \mathrm{P} \Big [ \vec {y} \Big ] \\ - \sum_ {\vec {y}: \sigma (\vec {y}) \in \mathcal {Y}} b \big (\sigma (\vec {y}) \big). \end{array}
$$

Note the similarity between $\nu V_{\theta}$ and $U_{\theta}^{\nu}$ . The only difference for each strategy is in the planning cost. In case of the Design Support Systems approach, the planning cost for a decision repeated $\nu$ times is $\nu \sum_{\vec{y}: \sigma(\vec{y}) \in \mathcal{Y}} b(\sigma(\vec{y})) \mathrm{P}[\vec{y}]$ whereas that for the program approach is $\sum_{\vec{y}: \sigma(\vec{y}) \in \mathcal{Y}} b(\sigma(\vec{y}))$ . The program incurs a higher planning cost, but this cost is not repeated for every instance of the decision.

## 3. Analysis and examples

The decision environment affects the choice of approaches, DSS or program, and the choice of best strategies in these approaches. As mentioned in the introduction, there is considerably theory and empirical evidence to the value of Decision Support Systems in unstructured managerial decision environments. In this section we use the economic models of DSS and Program decision making developed in the previous section to identify and study the impact of specific environment characteristics that affect the performance in Decision Support Systems and Programs.

## 3.1. Bayesian update cost

The Bayesian update cost is one of the key characteristics of unstructured managerial environments. This cost is a result of difficulties in updating the priors, given information, in an unstructured environment. It affects Decision Support Systems and Programs differently. To exhibit the effect of Bayesian update costs, in this section, all modules are assumed to be identical.

First consider the effect of Bayesian update cost on DSS. Information acquisition costs go up as the Bayesian update costs go up. Hence one would expect fewer modules to be used as the Bayesian update costs increase. A stronger statement of this effect can be made as the modules are assumed to be identical.

Definition 5. A strategy $\sigma$ is an extension of strategy $\sigma'$ if $\sigma(\vec{y}) = \sigma'$ for all $\vec{y} \in \vec{\mathcal{Y}}$ for which $\sigma(\vec{y}) \in \mathcal{Y}$ .

The next theorem relates the optimal strategies in environments that are identical in all respects except in Bayesian update costs.

Theorem 3. Let D and $D'$ be two identical decision environments except that $b < b'$ . Let $\sigma'$ be an optimal strategy for $D'$ . Then there exists an optimal strategy $\sigma$ for D that is an extension of $\sigma'$ .

The following lemma is used in the proof of the above theorem.

Lemma 5. Let $D$ and $D'$ be identical decision environments except that $b < b'$ . Let $\sigma$ be any strategy in $\Sigma_{m}^{B}$ and $\vec{y} = (\vec{y}, \ldots, y_{m})$ be any response in the domain of that strategy. Then $V_{\vec{y}} \geqslant V_{\vec{y}}'$ .

Proof. The proof is by induction backwards from M to m.

Let $i = M$ . $V_{y' = Vy'}' = E^B[x \mid \vec{y}]$ for all $\vec{y}$ with $M$ signals.

If $m = M$ then we are done.

Let $m < M$ and assume that the lemma is true for level $i$ , $m < i < M$ . For each $\vec{y}$ with $i - 1$ signals,

$$
V _ {y ^ {\prime}} = \max _ {\sigma \in \Sigma_ {M y} ^ {B}} \left\{ \begin{array}{l l} \int \left(V _ {y y} - b - c (y, \vec {y})\right) & \\ \times \mathrm{d} F (\sigma (\vec {y}) = y | \vec {y}) & \text { if } \sigma (\vec {y}) \in \mathcal {Y}, \\ \mathrm{E} ^ {B} [ x | \vec {y} ] & \text { otherwise }. \end{array} \right.
$$

$$
V _ {y} ^ {\prime} = \max _ {\sigma \in \Sigma_ {M y} ^ {B}} \left\{ \begin{array}{l l} \int \left(V _ {y y} ^ {\prime} - b ^ {\prime} - c (y, \vec {y})\right) & \\ \times \mathrm{d} F (\sigma (\vec {y}) = y | \vec {y}) & \text { if } \sigma (\vec {y}) \in \mathcal {Y}, \\ \mathrm{E} ^ {B} [ x | \vec {y} ] & \text { otherwise }. \end{array} \right.
$$

Note that $V_{y} \geqslant V_{y}'$ because $V_{yy}$ is in level $i$ for which the hypothesis is true and $b' > b$ .

By induction we are done.

Proof. (Theorem 3.) For level 0 the hypothesis follows from the definition of $V_{\theta}$ .

Assume that the hypothesis is true for all $\vec{y}$ with m, m < M signals.

If $m = M$ then in both cases they will not use a module.

Let $m$ be such that $m < M$ and let $\sigma'(\vec{y}) \in \mathcal{Y}$ for some response $\vec{y}$ with $m$ signals. By assumption of this inductive proof, $\vec{y}$ would be a valid response from the strategy for $D$ . Since $\sigma'(\vec{y}) \in \mathcal{Y}$ , it must be true that $V_{\vec{y}}' \geqslant E^B[x \mid \vec{y}]$ . By Lemma 5, $V_{\vec{y}}' \geqslant V_{\vec{y}}' \geqslant E^B[x \mid \vec{y}]$ . Hence a module may be used in an optimal solution to $D$ .

By induction we are done.

Theorem 3 shows that increasing Bayesian update costs decrease the number of modules used and it characterizes the solutions. It suggests that the optimal strategy in the low Bayesian update cost cases are an extension of those in which the update costs are higher. In special cases, as in

Example 3 later in this section, we can make tighter statements.

Programs are affected differently from DSS by Bayesian update costs. From the strategy tree formulations of the problem it can be seen that for any one given strategy, $\sigma \in \Sigma_{M}^{B}$ , the net benefit in the Program and DSS approaches differ only in the Bayesian update cost. The total update costs for a decision repeated $\nu$ times is shown below.

$$
\mathrm{DSS}: \nu \sum_ {\vec {y}: \sigma (\vec {y}) \in \mathcal {Y}} b \mathrm{P} [ \vec {y} ],
$$

where $P[\vec{y}]$ is the unconditional probability of having a response $\vec{y}$ in $\sigma$ .

$$
\text { Program: } \sum_ {\vec {y}: \sigma (\vec {y}) \in \mathcal {Y}} b.
$$

From the above formulas it can be seen that the planning costs in the program are b times the number of internal nodes in the strategy tree and in case of a decision support system they are b times the expected depth of the tree. Further, for $\nu = 1$ it can be seen that for any strategy the total update costs are lower in the DSS approach because the costs are weighted by the unconditional probability of being at that node. Hence, in optimality, the DSS approach would be preferred. For large enough $\nu$ this switches ad the total update costs for any strategy in the program approach are lower. This would be reflected in the choice DSS systems for ad-hoc decisions and Institutional DSS or Programs for recurrent ones. This is illustrated in the example below.

Example 3. Consider the project evaluation environment of the previous example.

Let $p_1 = 1.0$ and $p_2 = p$ . Then the probability of Type I error (rejecting a good project) is zero and probability of Type II error (accepting a bad project) is $p$ . In other words, the modules are noisy in only one direction. In such an environment it can be shown that in the optimal strategy the project is always rejected if a No signal is received. In this instance the strategy tree is a skewed tree of the type shown in fig. 1b. In this case the maximum number of modules that may be used in a strategy fully characterizes the strategy.

![](/api/attachments/5CCVG4PK/fulltext/images/d5ad01cd55407b8ea5292b57fdfa425ed275675ac666c659cd0756a4cf435067.jpg)  
Fig. 1b. Skewed strategy tree.

The net values in the DSS, $NV_{D}$ , and in the Program approach, $NV_{P}$ , are shown below (usage costs are assumed to be zero).

$$
\begin{array}{l} \mathrm{NV} _ {D} = \nu \left(\max \left\{g x _ {1} - (1 - g) p ^ {n} x _ {2}, 0 \right\} \right. \\ \left. - b \sum_ {i = 0} ^ {n - 1} g + (1 - g) p ^ {i}\right), \\ \mathrm{NV} _ {P} = \nu \left(\max \left\{g x _ {1} - (1 - g) p ^ {n} x _ {2}, 0 \right\}\right) - n b. \end{array}
$$

To further simplify the example, let $gx_{1}=(1-g)x_{2}=x$ . Then $gx_{1}-(1-g)p^{n}x_{2}$ is non-negative for $n=1,2,\ldots$ and the inner maximization can be removed. The formulae reduce to

$$
\begin{array}{l} \mathrm{NV} _ {D} = \nu x (1 - p ^ {n}) - b \nu \left(n g + (1 - g) \frac {1 - p ^ {n}}{1 - p}\right), \\ \mathrm{NV} _ {P} = \nu x (1 - p ^ {n}) - n b. \end{array}
$$

The strategy selection problem reduces to maximizing the net value over $n \in \{1, 2, \ldots, M\}$ . Relax the constraint to $n \in R$ and $n \geqslant 0$ . It can be shown that $NV_{P}$ is strictly concave in in >0 and that $NV_{D}$ is concave for $n \geqslant 0$ if $\mathrm{i}x > b(1 - g)/(1 - p)$ .

![](/api/attachments/5CCVG4PK/fulltext/images/6d38b112e4f6c8e1816198e9d102756197f57461f576a9c06de464f6406e953a.jpg)  
Fig. 2. Planning cost and module usage.

Not that the constraint $x > b(1 - g)/(1 - p)$ is equivalent to $x_{2}P[Reject |bad] > b$ . Examining the net value equation, it can be seen that $x_{2}P[R |bad]$ is the incremental value of a module and b is the incremental cost. Further it can be easily seen that $NV_{D}$ is non-positive if $x \leqslant b(1 - g)/(1 - p)$ . Hence no modules would be used.

Setting the first derivatives of net value with respect to n to zero we get the optimal number of modules to be

$$
\begin{array}{l} n _ {p} ^ {*} = \frac {\log (- b / (\nu x \log (p)))}{\log (p)}, \\ n _ {d} ^ {*} = \frac {\log \left(\frac {b g}{(b (1 - g) / (1 - p) - x) \log (p)}\right)}{\log (p)}. \end{array}
$$

Fig. 2 is a plot of $n_{d}^{*}$ and $n_{p}^{*}$ versus the Bayesian update cost b.

For ad-hoc decisions it can be seen that DSS results in the use of a larger number of modules in the strategy. This agrees with the previous researchers' results that the DSS approach results in examination of more alternatives for ad-hoc decisions. This reverses for recurrent decisions when the program approach does better because the update costs incurred during planning are amortized over a number or decision instances.

Fig. 3 provides another perspective on this. It is a plot of the difference between the net value of DSS and Program approaches for optimal strategies versus the probability of Type II error. The plots from top to bottom are for decisions with frequency of 1 to 4. For ad-hoc decisions, the one with frequency of one, the DSS approach results in greater net value. For recurrent decisions, for frequency 4 in this example, the program approach does better. This difference is because of update planning costs. This agrees with the previous researchers' result that the DSS approach is better for ad-hoc decisions.

![](/api/attachments/5CCVG4PK/fulltext/images/188b2e57df7640429b9a587735b10ad9abb212fd4e9d9d62f577a4475c1ba1ea.jpg)  
Fig. 3. DSS vs program: Frequency and noise.

## 3.2. Effect of module noisiness

Information from modules used in unstructured environments is rarely unambiguous. It may lead to errors of Type I and Type II. Such modules are called noisy information sources. Larger number of modules have to be used as the modules get noisier to get the same precision in posterior distribution of outcomes. This intuition is reflected in fig. 4 which is a plot of the optimal number of modules in DSS and Program approaches to the project evaluation decision of the previous example versus the error rate p.

![](/api/attachments/5CCVG4PK/fulltext/images/867f4137c03ef5525c397b52ac146eb90a8ca6bd1d59fa421747a909f9ab5c23.jpg)  
Fig. 4. Number of modules: noise and frequency.

Fig. 3, which is based on the same Project Evaluation decision, provides a comparison of the two approaches for noisy modules. First consider the curve for frequency of one. It provides a comparison of DSS and program approaches for ad-hoc decisions. As the modules get noisier, the advantage of using DSS over Programs increases. This agrees with the prior research result that the DSS approach is favored in unstructured environments that are characterized by noisy information sources.

As the frequency increases, the program approach becomes advantageous because of the amortization of planning costs over many decisions. This is reflected in the curves for frequencies 2, 3 and 4 in fig. 3.

## 4. Conclusions

There are many factors in unstructured environments that make the DSS approach beneficial. While earlier researchers have used behavioral, administrative and activity based approaches to predict the usefulness of Decision Support Systems paper, an economics based model is used in this paper.

A maximization is proposed for selection of the best strategy in each approach. The value of the best strategy in each approach is then used to evaluate the program versus the DSS approach. A few words about the use of optimization models in study of decision making in unstructured environments are in order. It is not expected that the model presented in this paper be used by an individual decision maker to select the best strategy to making a particular decision. Indeed, in many instances it would be more difficult to estimate the parameters of the model than to make the decision itself. Further, as Keen points out in [11], it is difficult to evaluate the DSS approach and use a cost-benefit analysis to justify decision support systems. Instead, the purpose of the model is to provide researchers with a fresh perspective on usefulness of Decision Support Systems. Section 3 of this paper is devoted to deriving such insights from the model. The effect of two environment factors, module noisiness and information assimilation cost, both of which are significant in unstructured environments, is examined.

Information assimilation costs reduce the number of modules used, alternatives examined and the net value of the decision in both of the two approaches. However, for ad-hoc decisions, it makes the DSS approach, which by its evolutionary nature required less planning, preferable. For recurrent decisions, the planning cost that results from the information assimilation cost is amortized over many decision instances and this makes the program approach preferable.

Fig. 3 reveals that the effect of information assimilation cost on number of modules used is highly non-linear with the rate of change being much larger in some ranges of the cost. One should expect greater investment in cost reduction strategies such as use of multi-media output, color monitors, carefully constructed graphs and tables in such instances.

Module noisiness reinforces the effect of information assimilation cost. For ad-hoc decisions, increased noisiness results in greater preference for the DSS approach. For recurrent decisions, on the other hand, increased noisiness make the program approach increasingly preferable as a greater investment can be made, ex-ante, in planning to counter the decrease in module quality. This larger cost is then amortized over many decisions.

In [7] it is shown that the DSS approach is advantageous, even in absence of update costs, when the decision maker has bounded rationality. This would be an additional tradeoff that would have to be considered along with the ones identified in this paper for selecting the best approach to making an unstructured decision.

## References

[1] S.L. Alter, Decision Support Systems: Current practices and challenges (Addison-Wesley, 1980).

[2] R.N. Anthony, Planning and control systems: A framework for analysis, Harvard University GSB (1965).

[3] P. Berger and F. Edelman, IRIS: A transaction based DSS for human resource management, in: Proceedings of Conference on DSS, Ed. E.D. Carlson, also in Database 8 (Winter 1977).

[4] R.M. Cyert and J.G. March, A behavioral theory of the firm (Prentice-Hall, 1963).

[5] M.H. De Groot, Optimal Statistical Decisions (McGraw Hill, 1970).

[6] Joel S. Demski, Information Analysis, Second edition (Addison-Wesley, 1980).

[7] R.M. Dewan, and S.C. Hansen, A comparison of the economic value of Decision Support Systems and Programs, Working Paper, J.L. Kellogg Graduate School of Management, Northwestern University, Evanston, IL 60208, (1990).

[8] J.J. Donovan and S.E. Madnick, Institutional and ad-hoc decision support systems and their effective use, Data Base 8, No. 3 (Winter 1977).

[9] G.H. Gorry and M.S. Scott-Morton, A framework for management information systems, Sloan Management Review (Fall 1971).

[10] W.D. Haseman, GPLAN: An operational DSS, Data Base 8, No. 3 (Winter 1977).

[11] P.G.W. Keen, Value Analysis: Justifying Decision Support Systems, MIS Quarterly 5, No. 1 (March 1981).

[12] P.G.W. Keen and M.S. Scott-Morton, Decision Support Systems: An organizational perspective (Addison-Wesley, 1978).

[13] R.L. Klaas, A DSS for airline management, Data Base 8, No. 3 (Winter 1977).

[14] J. Marschak and R. Radner, Economic Theory of Teams, Cowles Foundation Monograph 22, Yale University Press, New Haven (1972).

[15] J.C. Moore, and A.B. Whinston, A model of decision-making with sequential information-acquisition, Decision Support Systems, Part 1 in Vol. 2, 285–307 (1986) and Part 2 in Vol. 3, 47–72 (1987).

[16] H.A. Simon, The new science of management decision (Harper and Row, 1960).

[17] R.H. Sprague, and H.J. Watson, Bit by bit: Toward Decision Support Systems, California Management Review, XXII, 60–68 (Fall 1979).

[18] G.R. Wagner, Realizing DSS benefits with IFPS Planning Language, Proceedings of Thirteenth Hawaii International Conference on Systems Sciences (1980).

[19] H.J. Watson, R.H. Sprague and D.W. Kroeber, An empirical study of information systems evolution, Proceedings of Tenth Hawaii International Conference on Systems Sciences (1977).
