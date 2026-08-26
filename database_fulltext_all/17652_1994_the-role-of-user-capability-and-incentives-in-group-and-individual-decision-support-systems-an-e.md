---
otero_id: 17652
otero_key: "8YJXZ4VN"
title: "The role of user capability and incentives in group and individual decision support systems: An economics perspective"
authors: "Rajiv M. Dewan; Stephen C. Hansen"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90072-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The role of user capability and incentives in group and individual decision support systems: An economics perspective

Rajiv M. Dewan \*

Northwestern University, Evanston, IL, USA

Stephen C. Hansen

Stanford University, Stanford, CA, USA

We model the decision making processes in decision support systems and programs as sequential information acquisition processes and compare their usefulness. A Bayesian decision maker is shown to be indifferent between the two approaches. In contrast, a decision maker with bounded rationality prefers the decision support systems approach. The model is extended to group decision support systems where the interaction between the decision makers and the group facilitator is modelled as a non-cooperative economics game. We show that in some instances the group facilitator would prefer precommitment to an interaction plan rather than allow evolutionary planning of the interaction. This planning is similar to that in a program and may take the form of an organization chart.

Keywords: Decision support systems; Programs; Group DSS; Bayesian; Bounded rationality; Economics model; Incentive conflict; Non-cooperative game; Organization chart

![](/api/attachments/8YJXZ4VN/fulltext/images/4e41394e4193d00def305d86029ba576ecb15e12b6c6dfe66d46090a5050dd49.jpg)  
Rajiv M. Dewan received his Ph.D in Business with a concentration in Computers and Information Systems from the University of Rochester in 1986. He is interested in application of economics to issues in information management, database design, design of computer networks and interaction between information systems design and other functional areas of business management.

![](/api/attachments/8YJXZ4VN/fulltext/images/26258f6028673b7e358d9678979ef049d88859ffc3bacbbc006daf06bfc90e85.jpg)  
Stephen C. Hansen received his Ph.D. in Industrial Administration with a concentration in Accounting from Carnegie Mellon University in 1988. He is interested in the interplay between incentives and information and uses tools of Information Economics to address topics in Managerial Accounting and Auditing.

## 1. Introduction

As personal computers become a part of every manager's work bench, there is an increasing emphasis on end-user computing. In end-user computing the decision maker is involved in all of the three phases of the decision making process: intelligence, design and choice [20]. Decision support systems are specialized systems designed to support all of the phases.

The objective of the decision support systems $^{1}$ is to provide the decision maker with a user-friendly, consistent interface to data and decision making models. The man-machine interface is designed to foster a dialogue that lets the decision maker's expertise guide the machine, and the machine provide useful decision making information. When more than one decision maker is involved in this process, then the system is called a group decision support system. Group decision support systems provide for a dialogue not only between man and machine, but also among the different decision makers.

The usefulness of Decision Support Systems (DSS) has been examined from many different perspectives. Decision support systems are posited to be more useful in unstructured environments by Gorry & Scott-Morton [11] and Keen & Scott-Morton [16]; in strategic rather than operational settings by Anthony [2] and in settings in which the information is noisier and planning expensive by Dewan [9]. Empirical evidence and other composite views may be found in [1], [3], [14], [17], [21], [22], [23] and others.

User capabilities and decision environment characteristics contribute to making a decision unstructured. The environment specific factors, such as noise and repetition of decisions, have been examined in $[9]$ . In this paper we focus on the role of the human factors, bounded rationality and incentive conflict, in determining the usefulness of decision support systems.

Cyert and March characterize the decision making process in unstructured environments as having sequential attention to goals and local rationality $[6]$ . We model the decision making process as a sequential information acquisition process so as to retain these characteristics. The model follows that in Moore and Whinston $[18]$ and Dewan $[9]$ .

Our benchmark is a Bayesian decision maker. He has perfect recall, can form expectations over all future states, and uses all available information to pick a strategy that maximizes his expected utility. He is shown to be indifferent between programs and decision support systems because he can include the best possible strategy in the program.

In the first variant of the benchmark model, we consider the effect of bounded rationality. Bounded rationality may take the form of the decision maker's inability to form expectations over all future states, or inability to use all the available information. Such a decision maker would prefer the decision support systems approach over the programs approach because as the analysis progresses, the decision support system can take advantage of information revealed beyond the horizon of the program. If instances of decision making with unstructured decisions are construed as instances with decision maker of bounded rationality, then this result is in agreement with the literature on the usefulness of decision support systems cited earlier.

In the second variant we investigate the effect of incentive conflict when more than one decision maker is involved in a decision making process. This is the case with Group Decision Support Systems. Incentive conflict has a confounding effect on sequential planning. The additional information revealed in the sequential process is used by the group facilitator for better planning and by the individual participants to further their own interests. In such instances, from an organizational or a group facilitator's viewpoint, it can be better to have all the decision makers interact in a programmed fashion. Precommitment to an interaction plan as in an organization chart may improve performance.

A mathematical model of the decision making process and the role of bounded rationality is examined in the next section. The third section is devoted to analyzing the role of incentive conflict in the design of group decision support systems.

## 2. Model

## 2.1. The decision making environment

The decision environment is modeled as in [9] and [18]. The decision maker makes a decision that results in some payoff. As the outcome is uncertain, he may choose to gather information using modules. Modules are a combination of a model from a model base and data from a database. Formally, the decision environment is modelled as a seven tuple:

$$
D = \left\langle \tilde {x}, \xi , \Delta , \mathcal {Y}, M, F (\cdot), c (\cdot) \right\rangle ,
$$

where;

$\tilde{x}$ is a random variable defined on the outcome space $^{2}$ ;

$\xi$ is the prior probability induced on $\tilde{x}$ ;

$\Delta$ is the set of final decisions $\delta$ with a payoff of $\delta(\bar{x})$ with the set $\Delta$ assumed to be absolutely bounded by $\bar{\delta}$ .

y is the set of modules from which the decision maker may select individual modules with replacement;

$Y$ is an individual module, $Y \in \mathcal{Y}$ ;

$$
\begin{array}{c} y \\ \vec {y} \end{array}
$$

y is a signal from an individual module Y;

$\vec{y}$ is a sequence of signals called a response;

M is the maximum number of modules that may be used $^{3}$ ;

$F(y_{1},\ldots ,y_{m}|x)$ is the likelihood function specifying decision makers beliefs after a response has been received;

$c(y, \vec{y})$ is the the module usage cost.

Initially we assume that we have a single decision maker who is a Bayesian with a risk-neutral utility function. The decision maker utilizes all available information to update his prior beliefs so as to compute the action choice with highest expected net value. Two decision making processes, one in which the decision maker uses a decision support system and the other in which he uses a program, are modeled next.

## 2.2. Decision support systems

When using a decision support system, the decision maker is conducting a sequential sampling experiment. At each stage the decision maker uses his updated prior to decide on the next action. The following sequence of events summarizes this procedure.

## 2.2.1. Sequence of events

1) The decision maker decides whether to make a final decision or to use a particular module.

2) If a module is used, then he updates his priors and re-considers Step 1.

Each time the decision maker is at Step 1 above, he has to evaluate the possible signal that might be produced in Step 2 and the effect it would have on his priors. The effect would of course depend on his choice the next time he will be in Step 1 and so on. This problem is modelled as a dynamic program. The following definition is needed before the problem can be formulated.

Definition A strategy, denoted $\sigma(\vec{y})$ is a mapping from responses $\vec{y}$ to a sequence of module choices from $\mathcal{Y}$ and an action choice from $\Delta$ . The set of strategies that use $M$ or fewer modules is denoted $\Sigma_{M}$ .

The following example serves to illustrate the decision making model and feasible strategies. It is the Project Evaluation example from [9].

Example 1 Project Evaluation. Consider the following project evaluation decision setting. The project may be ‘good’ or ‘bad’, i.e., $\tilde{x} \in \{Good, Bad\}$ . The prior distribution of outcomes is $\xi(\tilde{x} = Good) = g$ and $\xi(\tilde{x} = Bad) = 1 - g$ . At each stage, the decision maker has a final decision of either implementing the project (denoted D) or rejecting the project (denoted R). Hence $\Delta = \{D, R\}$ . The matrix below describes the payoff.

<table><tr><td></td><td>D</td><td>R</td></tr><tr><td>Good</td><td> $x_{1}$ </td><td>0</td></tr><tr><td>Bad</td><td> $-x_{2}$ </td><td>0</td></tr></table>

The decision maker has a module available that he may use again and again. The module generates a 'Yes' or a 'No' signal. A 'Yes' signal is obtained with a probability of $p_1$ when the project is good and with a probability $p_2$ when it is bad. Without loss of generality, the 'Yes' signal is assumed to increase the probability of good project and 'No' to decrease it $^4$ . Hence the module may signal 'No' when the project is good (Type I error) with probability $1 - p_1$ and signal 'Yes' when the project is bad (Type II error) with probability $p_2$ . Hence $P[Y|Good] = 1 - P[N|Good] = p_1$ and $P[Y|Bad] = 1 - P[N|Bad] = p_2$ . Each use of the module is independent, i.e., $P(y_1, \ldots, y_m|x) = \prod_{i=1}^{m} P(y_i|x)$ where $x$ may be Good or Bad. These probabilities specify the likelihood functions. Let $c$ be the constant usage cost.

Consider the following strategy.

$$
\left\{ \begin{array}{l} \sigma (\theta) \end{array} \right. = u s e a m o d u l e,
$$

$$
\sigma (Y) \quad = u s e a m o d u l e,
$$

$$
\sigma (N) \quad = u s e a m o d u l e
$$

$$
\sigma (Y Y) = d o \text {   the   project   },
$$

$$
\sigma (Y N) = \text {use a module},
$$

$$
\sigma (N Y) = \text { use   a   module },
$$

$$
\left\{ \begin{array}{l l} \sigma (N N) & = r e j e c t t h e p r o j e c t, \\ \dots \end{array} \right.
$$

This strategy can be represented by the strategy tree shown in Figure 1. In the figure every odd (root is in level 1) level node represent responses and nodes in even levels represent module usage decisions. This is similar to a game tree between nature (modules) and the decision maker. □

Returning to the general formulation, consider a decision maker who has received a response $\vec{y}$ . Let $W_{\vec{y}}$ denote the expected value of the decision at this response. If he decides to make a final decision, then he will pick the best possible final decision and receive $E^{B}[\tilde{x}|\vec{y}] = \max_{d\in \Delta}\int E[d(\tilde{x})|\vec{y}]dF(\tilde{x}|\vec{y})$ . If he decides to gather more information, then he will use a module with a cost of $c(y,\vec{y})$ where $y$ is a signal he might receive from the additional module. The net expected value that he will get after using a module $Y$ is $\int (w_{\vec{y} y} - c(y,\vec{y}))dF(Y = y|\vec{y})$ .

Expressed as a dynamic program, the strategy choice problem is:

Problem D:

$$
\max _ {\sigma \in \Sigma_ {M}} W _ {\theta}.
$$

![](/api/attachments/8YJXZ4VN/fulltext/images/e7c61b52716578eb32edbc325302427dac34ff8167e915c2170013b1118de35a.jpg)  
Fig. 1.

Subject to:

$$
W _ {\vec {y}} = \max _ {\sigma \in \Sigma_ {M \vec {y}}} \left\{ \begin{array}{l l} \int (W _ {\vec {y} y} - c (y, \vec {y})) d F (\sigma (\vec {y}) = y | \vec {y}), & \text { if } \sigma (\vec {y}) \in \mathcal {Y}; \\ E ^ {B} [ \tilde {x} | \vec {y} ], & \text { otherwise }. \end{array} \right.
$$

where $E^B[\tilde{x}|\vec{y}] = \max_{d\in \Delta}\int E[d(\tilde{x})|\vec{y}]dF(\tilde{x}|\vec{y})$ and $\Sigma_M$ is the set of strategies that use $M$ or fewer modules.

The constraints in the above problem insure that at each stage the decision maker will only pick strategies that are sequentially rational. Sequential attention to goals and local rationality are key characteristics of strategic and unstructured decision making $[6]$ . The following example illustrates the problem.

Example 2 Consider the project evaluation example above where at most one module may be used. Writing out the constraints we get:

$$
\begin{array}{l l} W _ {0} = \max \left\{ \begin{array}{l l} \left(W _ {y} - c (y, 0)\right) P [ y ] + \left(W _ {n} - c (n, 0)\right) P [ n ], & \text { if   a   module   is   used; } \\ E ^ {B} [ \tilde {x} | 0 ], & \text { otherwise. } \end{array} \right. \\ W _ {y} = E ^ {B} [ \tilde {x} | y ] \\ W _ {n} = E ^ {B} [ \tilde {x} | n ] \end{array}
$$

In the above y denotes a “Yes” response and a n denotes a “No” response from the module.

For sake of specificity, let $x_{1} = -x_{2} = 1.0$ , g = 0.7, $p_{1} = 0.9$ and $p_{2} = 0.1$ . We illustrate the dynamic program by solving the problem backwards from a time when the decision maker has received a signal from a module.

Consider a decision maker who has received a Yes from a module. Using Bayes rule we get $P[Good|Yes]=0.955$ and $P[Bad|Yes]=0.045$ .

The expected value of the project conditional on a Yes response is calculated as $E[\tilde{x}|Yes]=1.0\cdot P[Good|Yes]-1.0\cdot P[Bad|Yes]=0.91$ . Since implementing the project has a greater value of 0.91 over not implementing the project (value 0.0), the decision maker will implement the project if he receives a Yes signal, i.e., $W_{y}=E^{B}[\tilde{x}|Yes]=0.91$ .

Now consider a decision maker who has received a No signal. The conditional expected value is computed as above to be $E[\tilde{x}|No]=-0.59$ . So in this case the decision maker will reject the project giving $W_{n}=E^{B}[\tilde{x}|No]=0$ .

At the initial stage, the decision maker has to decide whether to use a module or make a final decision. If he were to use the module, then the expected value is $(W_{y}-c)P[Yes]+(W_{n}-c)P[No]$ . The marginal probabilities are computed to be P[Yes]=0.66 and P[No]=0.34. Hence the expected value of the project if the decision maker uses a module is $0.91\cdot0.66+0.0\cdot0.33-0.1=0.5$ .

The expected value of the project if a module is not used is $E[\tilde{x}]=x_{1}g-x_{2}(1-g)=0.4$ .

Comparing the options, the best strategy is to use a module and then do the project only if the module produces a Yes signal. This results in the highest ex-ante expected value of 0.5.

## 2.3. The programs approach

The second approach to making a decision is the programs approach. If the decision maker writes a program, ex-ante he precommits to the use of modules based on specific responses. In economics this is referred to as ex-ante precommitment to a game tree. The following sequence of events describes the process used to design and implement a program.

## 2.3.1. Sequence of events

1) The decision maker decides to make a final decision or gather information using a program. If he decides to use a program then he plans and codes the best program.

2) The decision maker follows the “prewired” program picked in Step 1. The modules of the program are then conditionally executed as specified in the program.

3) Once the program has finished processing, the decision maker makes a final decision.

The program can be represented by a decision tree. Ex ante, the decision maker determines the conditions under which he will use modules, and what he will do as a function of each response. These are the most powerful programs available. Any feasible sequence of evaluations can be programmed.

Using the notation developed in the previous section, the problem of picking the decision tree with the highest ex-ante expected value is described by the following problem:

Problem P:

$$
\max _ {\sigma \in \Sigma_ {M}} V _ {\theta}
$$

Subject to:

$$
V _ {\vec {y}} = \left\{ \begin{array}{l l} \int (V _ {\vec {y} y} - c (y, \vec {y})) d F (\sigma (\vec {y}) = y | \vec {y}), & \text { if } \sigma (\vec {y}) \in \mathcal {Y}; \\ E ^ {B} [ \tilde {x} | \vec {y} ], & \text { otherwise }. \end{array} \right.
$$

The decision maker decides on the program at a stage when no modules have been used and hence he maximizes $V_{\theta}$ . The constraint relates the value of the program at an intermediate stage to succeeding stages. Note the difference between these constraints and those in problem D. In program D the decision has to be locally and globally optimal, while that in program P has to be just globally optimal. The decision maker solves problem P and follows through on the strategy selected. This differs from the decision support systems approach, where the decision maker has to solve a family of problems, problem D for each response $\vec{y}$ that is realized.

In the following sections, the decision support systems approach is compared to the program approach under different conditions. In the first scenario the decision maker is a Bayesian. In the next scenario he has bounded rationality. Lastly, the effect of incentive conflict among different decision makers in a group context is examined.

## 3. Effect of decision maker capabilities and incentives

In this section we compare the decision support systems approach to the programs approach under three different scenarios.

## 3.1. A Bayesian decision maker

A Bayesian decision maker picks the decision that maximizes the expected value. The maximized value is called the Bayes Risk and the maximizing decision is called the Bayes Decision. He always uses any additional information to replace his distribution over uncertain states of the world with a new conditional distribution called the posterior. A characteristic of a Bayesian decision maker is that he uses all the available information to compute the posterior distribution. He can examine all the future states with infinite look ahead and can use it to compute the strategy with highest expected value. In this sense the Bayesian decision maker is unboundedly rational.

Consider a Bayesian decision maker at a stage when no modules have been used. The decision maker has to decide whether to use a program or a decision support system. He solves problem P and problem D, and chooses the one with higher value.

In each case, the decision maker has the option of not using any modules and selecting a final action. Hence, if the decision maker uses modules (selects a non-empty program or uses a decision support system), the expected value of the project must be positive.

The first theorem compares the optimal program and the optimal decision support system.

Theorem 1 A risk neutral Bayesian decision maker has the same ex-ante value for both the programs and the decision support systems approaches.

Please see the Appendix for a proof.

The proof relies on the fact that the decision maker can precommit to any strategy and that, ex-ante, the probability of any response is the same in both the cases. It is important to note that this equality is established only for the ex-ante problems. As the modules are used, the decision maker has more information in the decision support systems case. Furthermore, the cost of previously used modules is sunk. Hence, in general, the ex-post trees will be different. This difference, however, vanishes in ex-ante expectations.

A problem similar to this one has been examined by statisticians, such a DeGroot [7], in the area of sequential sampling. Consider a statistician who wishes to gather additional information. He considers two kinds of sampling plans: simultaneous and sequential. Sequential sampling uses past responses to decide on future sampling and is similar to the decision support systems approach. In simultaneous sampling, on the other hand, the statistician only determines the number of samples. He uses a fixed number of observations and does not condition his future sampling on past responses. In this sense the samples are drawn simultaneously. It is easy to see that sequential sampling dominates simultaneous, ([7], page 332). For instance, if the optimal simultaneous plan is to sample 10 times and accept if 8 yesses are obtained, then a sequential plan that terminates on receipt of eight yesses dominates the simultaneous plan. The potential for early termination reduces costs.

Our work performs a different type of comparison than that of the statisticians. While the decision support systems approach is similar to sequential sampling, the programs approach is not similar to simultaneous sampling. In particular, a program allows conditional execution which is not possible in simultaneous sampling. We compare a predetermined sampling tree (a program) to a sampling tree that evolves with additional information which is revealed as the decision making progresses (a decision support system). Further, since the program and decision support system have the same value, Theorem 1 shows that the programs approach dominates simultaneous sampling plans.

The next subsection looks at the effect of constraining the look-ahead capability on the value of decision support systems.

## 3.2. A decision maker with bounded rationality

One of the key characteristics of a Bayesian decision maker is that he has an unbounded look ahead. In this subsection we relax this assumption and instead assume that the decision maker can look ahead only L modules.

For decision makers without bounds on look ahead, the value of the organization at any response $\vec{y}$ depends on whether it is optimal to use the next module. At the $L^{th}$ module the boundedly rational decision maker has no means of determining the next “optimal” action and hence he must resort to heuristics. Now let us examine the models formulated earlier and see how they must be changed to account for the decision maker’s bounded rationality.

In the program approach the problem faced by the decision maker is the same as that faced by a decision maker with an upper bound on the number of modules that he may use. This is problem P from the previous subsection with M replaced by $\min\{M, L\}$ .

The decision support system changes from the problem in the previous subsection. The decision maker's horizon is always $L$ (unless constrained by wealth or time constraints) and this limit does not decrease as information is acquired. By hypothesis, the decision maker uses a heuristic to determine what he does at the end of the horizon. At any response $\vec{y}$ , let the value generated by using the heuristic be $w_{\vec{y}}$ .

The decision support systems problem is given below.

Problem DB:

$$
\max _ {\sigma \in \Sigma_ {M}} W _ {\theta}
$$

Subject to:

$$
W _ {\vec {y}} = \sum_ {\sigma \in \Sigma_ {M \vec {y}}} \left\{ \begin{array}{l l} \int \big (W _ {\vec {y} y} - c (  y  ,   \vec {y}) \big) d F \big (\sigma (  \vec {y}  ) = y   |   \vec {y} \big), & \text {if} \sigma (  \vec {y}  ) \in \mathcal {Y} \text {and} |   \vec {y} | <   L; \\ \int \big (w _ {\vec {y} y} - c (  y  ,   \vec {y}  ) \big) d F \big (\sigma (  \vec {y}  ) = y   |   \vec {y} \big), & \text {if} \sigma (  \vec {y}  ) \in \mathcal {Y} \text {and} |   \vec {y} | = L; \\ E ^ {B} \big [ \tilde {x}   |   \vec {y} \big ], & \text {otherwise}. \end{array} \right.
$$

where $E^{B}[\tilde{x}|\vec{y}] = \max_{d\in \Delta}\int E[d(\tilde{x})|\vec{y}]dF(\tilde{x}|\vec{y})$ and $\Sigma_M$ is the set of strategies that use $M$ or fewer modules.

The value $w_{\vec{y}}$ represents the value of the heuristic decision made when a response of $\vec{y}$ has been obtained.

Theorem 2 A risk neutral decision maker with bounded rationality weakly prefers the decision support systems over the programs.

Please see the Appendix for a proof.

This result agrees with the general view that a decision support system is better than a program in situations where the decision maker does not have the capacity to predict the states of the world that will result from his decisions $[1]$ , $[11]$ and $[16]$ . This includes decisions in environments that are called unstructured and decision making processes called non-programmable [4]. In such cases there is an economic value to the decision support systems approach.

## 3.3. Multiple decision makers with incentive conflict: GDSS

In this subsection we analyze the planning decision made by a group facilitator in a group decision support setting. The planning decision is analogous to the project evaluation decision analyzed in previous subsections.

In many settings a single decision maker may not have the capability or the expertise to make the decision by himself. In such settings the decision support systems concept is extended to that of Group Decision Support Systems (GDSS) that use groups of decision makers. In addition to the interface to data and models provided by decision support systems, group decision support systems also provide an interface between decision makers. DeSanctis and Gallupe, in $[8]$ , propose a classification of group decision support systems into three levels with differing degrees of support for group decision making. Group decision support systems at Level 1 provide a means for communication using large screen output devices or devices for vote gathering and tabulation. Systems at Level 2 provide, in addition to services provided by Level 1 systems, planning tools and models that may be used individually or collectively. Level 3 is the most general one in which machine and human experts are integrated into the decision making process in a variety of interaction patterns. Group decision support systems of Level 3 are modeled in this paper.

The decision maker who plans and manages the interaction between decision makers is called the “group facilitator”. We assume that the group facilitator is the project leader and that his incentives are aligned with that of the residual claimants of the organization. The group facilitator decides whether to preplan decision maker interactions or to let the interactions evolve with the revealed information.

In the setting of project evaluation discussed in earlier sections, the decision makers have the expertise to run the modules and the group facilitator wishes to use the decision makers and associated modules to maximize his utility. If there were no incentive conflict or if the effort of participants were observable by all, then the decision makers would always provide the relevant signals and the foregoing models and discussions would be sufficient. In particular, forcing contracts $[15]$ , which compensate the participants only if they work hard, would be sufficient.

If we add in incentive conflicts and unobservability of effort, the previous models must be changed to take into account the changed behavior of the decision makers.

The strategy choices faced by participants are affected, both by incentive conflicts between the group facilitator and participants and incentive conflict between the participants themselves.

To appreciate the effect of unobservability and incentive conflict between the group facilitator and the decision makers, consider a group facilitator who uses a GDSS with just one agent who is risk neutral but effort averse $^{5}$ . (The effect of incentive conflict between the participants is examined later in this section.) The agent's unobservable effort affects the quality of his private $^{6}$ signal. If an agent takes a low effort, $a_{L}$ , then that agent receives an uninformative signal. If an agent takes a high effort, $a_{H}$ , then that agent observes an informative signal $^{7}$ . In each case the signal is private. The agent may or may not be truthful in reporting his signal to the group facilitator. In particular he will report what ever is in his best interest. In the following let $\hat{y}$ be the report when the agent observes y. Two further assumptions underlie the model. Firstly, the group facilitator cannot randomize over hiring decision makers. Secondly, the facilitator does not offer randomized contracts.

Each person in this economic game, the facilitator and the decision makers, make decisions that are in their best interest. This game can be modeled as a number of related optimization problems, as in [12], or equivalently by a single optimization problem as in [15]. We use the latter approach with maximization of group facilitator's utility as the objective function. The self-utility maximizing behavior of the other participant is expressed via constraints on the group facilitator's optimization – he cannot force the other decision maker to do things that are not in his best interest. Details of the optimization problem follow.

Problem G:

max $W_{\theta}$

(1)

subject to:

$$
W _ {\vec {y}} = \max _ {\sigma \in \Sigma} \left\{\int \left(W _ {\vec {y} y} - c (y, \vec {y}; E ^ {B} [ \tilde {x} | y, \vec {y}; a _ {H} ])\right) d F (\sigma (\vec {y}) = y | \vec {y}; a _ {H}), \quad \text {if} \sigma (\vec {y}) \in \mathcal {Y}; \right.\tag{2}
$$

$$
\text { otherwise }.
$$

$$
E \left[ U \left(c (y, E ^ {B} [ \tilde {x} | y; a _ {H} ]), a _ {H}\right) \right] \geqslant \max _ {\hat {y} (y)} E \left[ U \left(c (\hat {y}, E ^ {B} [ \tilde {x} | \hat {y}; a _ {H} ]), a _ {L}\right) \right]\tag{3}
$$

$$
U \left(c (y, E ^ {B} [ \tilde {x} | y; a _ {H} ]), a _ {H}\right) \geqslant U \left(c (\hat {y}, E ^ {B} [ \tilde {x} | y; a _ {H} ]), a _ {H}\right) \quad \forall \hat {y} \neq y\tag{4}
$$

$$
E \Big [ U \big (c \big (y, E ^ {B} \big [ \tilde {x} | y; a _ {H} \big ] \big), a _ {H} \big) \Big ] \geqslant u\tag{5}
$$

where $E^{B}[\tilde{x}|\vec{y}]=\max_{d\in\Delta}\int E[d(\tilde{x})|\vec{y}]dF(\tilde{x}|\vec{y}),\Sigma_{M}$ is the set of strategies that use M or fewer modules, $U(\cdot)$ is the agent's utility function that is separable in effort and wage terms and reflects risk neutrality and effort aversion, and u is the reservation utility of the agent.

Problem G is similar to problem D with additional constraints. Equations (1) and (2) above are as before. The remaining are examined in reverse order.

The agent knows that in equilibrium he will work hard and be truthful. He knows that the group facilitator knows this too. Therefore in equilibrium he expects to be compensated by $c(y, E^{B}[\tilde{x}|y; a_{H}])$ . If the decision maker works hard and tells the truth then he should expect to make his reservation utility of u. This constraint is expressed in Equation (5). It has been called the “Individual Rationality” constraint in information economics literature [15].

Equation (4) examines the agent's choice of report after he has worked hard and observed his private signal. The agent will report the truth only if it is incentive compatible to do so. For truth telling to be incentive compatible, the utility from reporting $y$ when the signal is $y$ has to be higher than reporting $\hat{y} \neq y$ for all $y$ , point wise. In other words, there must be no circumstances in which the agent will prefer to lie. This constraint is formulated in equation (4). This is a version of the truth telling constraint as in [5].

Equation (3) asserts that at the time when the agent makes his effort choice he must have higher expected utility with higher action choice regardless of the report when he picks the low action. So the agent must have higher expected utility regardless of his reporting strategy $\hat{y}(y)$ ; even including a strategy that might call for telling a lie after selecting lower effort $a_{L}$ . This equation is complex because the Revelation Principle [19] is not applicable in this sequential information acquisition game.

The game changes when we admit the possibility of having more than one decision maker, in addition to the group facilitator, in the system. The strategy choices of each decision maker will be contingent on his beliefs about other decision maker's action and reporting choices. Each decision maker's compensation is contingent on the outcome which, in turn, depends on action and reporting choices of all agents. Therefore the constraints in the group facilitators problem are formulated assuming a Nash equilibrium among the decision makers. Further details of the formulation are presented in Appendix 2. The following example illustrates the multiple decision maker case $^{8}$ .

Example 3 This example is an extension of the project evaluation example described earlier. Assume that each decision maker can take a high action, $a_{H}$ , or low action, $a_{L}$ , that influences the quality of his signal. Actions and signals are unobservable by the group facilitator. If the decision maker picks action $a_{H}$ , then he receives an informative signal and incurs an effort disutility of $u_{a}$ . Each decision maker must receive at least u from participating in the decision. The group facilitator chooses a compensation plan and an interaction strategy so as to maximize his ex-ante profit.

![](/api/attachments/8YJXZ4VN/fulltext/images/11058c3e9b10fd313dd17e46d530d1db93ca9af1f6a04021dcf87757d490f042.jpg)

An important feature of our group decision support system is that the report of the decision makers is public. The first decision maker's report is observed by both the group facilitator and the second decision maker before the second decision maker makes his report. No other communication is allowed between the decision makers.

The essential ingredient of this model is that now the cost of a decision maker (and his module) is conditioned on the response. The group facilitator motivates the decision makers by offering them contracts which are conditioned on the signals of the modules as well as the outcome of the project (if implemented).

The entire set of two decision maker organizations with homogeneous modules is examined in [13]. Under the parameters $u = 0.05$ , $u_{a} = 0.05$ , $x_{1} = 170.0$ , $x_{2} = 700.0$ , $p_{1} = 0.85$ , $p_{2} = 0.80$ , and $g = 0.80$ , the optimal program organization tree is shown in Figure 2. The facilitator implements the project when both decision makers recommend or both decision makers do not recommend the project. The reason why the facilitator implements the project when he received two No signals is explained below. This organization can be viewed as one of sequential voting. The first decision maker casts a public vote, then the second decision maker votes. The project is implemented if both vote for or against the project. The derivation of this optimal contract is shown in Appendix 2. This strategy provides an expected profit of 0.3967.

The next step is to illustrate that this organization is not sequentially rational and hence could not arise from flexible group interactions where the participants do not precommit to an organization chart. The argument is as follows: The group facilitator implements the project given two 'No' signals solely to provide additional information he can use to motivate the decision makers. Ex ante, the potential additional information from ('No', 'No') signals from two decision makers reduces the group facilitator's costs sufficiently to overcome the lost revenues of implementing the project given unfavorable signals. However, once the first 'No' has been reported the expected value from following through on the strategy is -31.404. If the group facilitator could offer the decision makers their expected compensation under the contract and not implement the project, then his losses would be reduced to -15.630. Therefore if the group facilitator received a 'No' signal from the first decision maker he would never implement the project. Since the facilitator will not implement the project given a No signal in a decision support system approach, the only relevant possible organizations are:

i. hire no decision makers and implement the project;

ii. hire no decision makers and not implement the project;

iii. hire one decision maker and implement the project if he recommends the projects; and

iv. hire a decision maker. If he recommends the project then hire another one. Do the project only if both recommend the project.

Using a similar procedure as in Appendix 2, the expected profits can be calculated for each of these possible organizations. Comparing the results shows that the optimal sequentially rational organization is to hire no decision makers and implement the project, which yields an expected value of zero. □

The example provides an instance in which the group facilitator is better off precomitting to an interaction strategy. In, absence of precommitment, the group facilitator cannot credibly maintain the optimal program and still motivate the decision makers to work hard and report truthfully. One possible commitment mechanism is to have an organization chart. The sequence of evaluations are hardwired and are not modified as a consequence of revealed information. The strategy expressed in the organization chart does not have to meet the interim sequential rationality constraints and can generate higher expected profits.

## 4. Discussion and conclusions

This paper compares decision support systems and programs from an economic perspective. The decision maker can either precommit to an execution plan (programs), or he can reoptimize his plan at every stage of the decision making process (decision support systems). This paper focuses on the differences between the two. It identifies a situation in which there is no ex-ante difference, and finds contrasting settings in which either a decision support system or a program is preferred.

The Bayesian decision maker is an idealized economic model of a perfectly rational decision maker. The reoptimization permitted by the decision support systems approach offers no value to a Bayesian decision maker beyond what can be obtained from a program. He can always assess the value of future module usage and place the optimal plan in a program.

Bounded rationality makes the reoptimization inherent in the decision support system approach worthwhile. A boundedly rational decision maker does not have infinite look-ahead and hence any precommitted plan in the program is suboptimal. When the decision maker uses the decision support system approach, he can use more than the ex-ante information after he has used a module. The decision maker uses this additional information to plan further ahead than he could with a program. This makes the decision support system approach more valuable than the program approach.

The group interaction planning problem faced by the group facilitator is analogous to that faced by the decision maker in the earlier setting with one difference. The modules are implemented by other decision makers who may have incentives that conflict with that of the group facilitator. In such a situation, the group facilitator overcomes these incentive problems by offering payments conditional on the decision makers' signals. This makes the cost of a decision maker dependent on the responses of the other decision makers. Ex ante, over all responses, these costs may be small. However ex interim, when specific responses occur these costs are large and in a decision support system the group facilitator may not find it sequentially rational to follow through on the contract. In the decision support systems approach the group facilitator will not be able to use as large a contract set as in the programs case. This can make the program approach preferable. If one views business organizations as making a series of group decisions, then this may partly explain the common use of organization charts.

These results, obtained from an economics perspective, complement the analysis of decision support systems from other perspectives. The decision support systems approach offers additional insight to the decision maker that may be used for sensitivity analysis, better control, adaptability, etc. Further, these factors also affect the confidence of the decision maker about the decision and his motivation to carry out the suggested action. However, in a decision support system, the additional involvement of the decision maker increases the cost of making decisions. This is particularly true for decisions that are of a recurrent nature, as the kind handled by institutional decision support systems $[10]$ . All of these factors must be considered in picking the decision support systems approach over the programs approach.

## Appendix 1

Proof of Theorem 1 The proof of Theorem 3 in [9] applies here. We prove the theorem in two stages. Firstly, we show that the feasible set of strategies in problem D is contained in that of problem P. Secondly, we show that if a strategy solves problem P then it is feasible in problem D.

(1) Note that if $\sigma$ satisfies the constraint in problem D then it will satisfy the constraints in problem P. Hence the set of feasible and optimal strategies of problem D are contained in that of problem P.

(2) Let $\sigma^{*}$ solve P with value $V_{\theta}^{*}$ but not solve problem D. Then there must be some response $\vec{y}$ for which, in P:

$$
V _ {\vec {y}} <   \max _ {\sigma \in \sigma_ {M \vec {y}}} \left\{ \begin{array}{l l} \int (V _ {\vec {y} y} - c (y, \vec {y})) d F (\sigma (\vec {y}) = y | \vec {y}), & \text { if } \sigma (\vec {y}) \in \mathcal {Y}; \\ E ^ {B} [ \tilde {x} | \vec {y} ], & \text { otherwise }. \end{array} \right.
$$

In this case we can strictly improve the solution to P. This contradicts the hypothesis that $\sigma^{*}$ solves P. Hence any $\sigma^{*}$ that solves P is feasible in D.

The proof follows from (1) and (2) above. $\square$

Proof of Theorem 2 Let $W_{\theta}^{H}$ denote the value computed by the decision maker with bounded rationality when he uses the heuristic $w_{\vec{y}} = E^{B}[\tilde{x}|\vec{y}]$ for $|\vec{y}| = L$ . This amounts to “naively” assuming that he will not use more than $L$ modules. Let $V_{\theta}$ denote the value of the program. By Theorem 1, $W_{\theta}^{H} = V_{\theta}$ . Note that the decision maker knows that the heuristic understates the value of modules when $L$ modules have been used. He knows this because, at any stage, $W_{\vec{y}} \geqslant E^{B}[\tilde{x}|\vec{y}]$ . Hence by induction, the boundedly rational decision maker knows that $W_{\theta} \geqslant W_{\theta}^{H} \geqslant V_{\theta}$ .

## Appendix 2

This appendix presents the group facilitator's contracting problem in Example 3 using the standard economic contracting notation. The group facilitator will be referred to as the principal, while the decision makers will be referred to as the agents.

The principal ex ante precommits to:

(i) a set of responses to the agent's reports, and

(ii) a set of payments to the agents contingent on the outcome and reports.

The principal's objective is to maximize ex ante expected revenues minus ex ante expected contracting costs. For the organization in Figure 2, the ex ante expected revenues are $(gp_1^2 + g(1 - p_1)^2)x_1 - ((1 - g)p_2^2 + (1 - g)(1 - p_2)^2)x_2$ .

Since the principal is risk neutral, maximizing profits for this specific organization is equivalent to minimizing contracting costs. The contracts of the two are independent because we have no organizational constraints linking the earnings of the two decision makers. An example of such a constraint would be to pay both agents a fixed amount that they must divide amongst themselves. The principal can minimize the contracting costs separately for each agent.

Agent 1 Action Choice  
![](/api/attachments/8YJXZ4VN/fulltext/images/a8b3bd0fa0f961ce679961f822dfdd162e9fb9848e5455049d063ecfd53fbab4.jpg)

The notation for a generic payment to the first agent in $s_{1}$ (outcome, report 1, report 2) where “outcome” is the outcome of the project, “report 1” is the first agent’s report, and “report 2” is the second agent’s report. The generic payment to the second agent, $s_{2}$ (outcome, report 1, report 2) is defined in a similar fashion.

The next step is to examine the principal's choice of payments to the first agent. The first agent's game tree is shown in Figure 3. An important feature of the tree is that it assumes that the second agent will follow the equilibrium strategies of always working hard and providing the principal with truthful reports. The various constraints follow:

(i) Given that agent one has taken the high action and observed a 'No' signal, he prefers to not recommend the project over recommending the project.

$$
\begin{array}{l} \big (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2}) \big) \big (s _ {1} (0, N R, R) - u _ {a} \big) \\ \quad + g \big (1 - p _ {1} \big) ^ {2} \big (s _ {1} (x _ {1}, N R, N R) - u _ {a} \big) + (1 - g) \big (1 - p _ {2} \big) ^ {2} \big (s _ {1} (x _ {2}, N R, N R) - u _ {a} \big) \\ \geqslant g p _ {1} (1 - p _ {1}) \big (s _ {1} (x _ {1}, R, R) - u _ {a} \big) + (1 - g) p _ {2} (1 - p _ {2}) \big (s _ {1} (x _ {2}, R, R) - u _ {a} \big) \\ \quad + \big (g \big (1 - p _ {1} \big) ^ {2} + (1 - g) \big (1 - p _ {2} \big) ^ {2} \big) \big (s _ {1} (0, R, N R) - u _ {a} \big) \end{array}
$$

(ii) Given that agent one has taken the high action and observed a 'Yes signal, he prefers to recommend the project over not recommending the project.

$$
\begin{array}{l} g p _ {1} ^ {2} \big (s _ {1} (x _ {1}, R, R) - u _ {a} \big) + (1 - g) p _ {2} ^ {2} \big (s _ {1} (x _ {2}, R, R) - u _ {a} \big) \\ \quad + \big (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2}) \big) \big (s _ {1} (0, R, N R) - u _ {a} \big) \\ \geqslant \big (g p _ {1} ^ {2} + (1 - g) p _ {2} ^ {2} \big) \big (s _ {1} (0, N R, R) - u _ {a} \big) + g p _ {1} (1 - p _ {1}) \big (s _ {1} (x _ {1}, N R, N R) - u _ {a} \big) \\ \quad + (1 - g) p _ {2} (1 - p _ {2}) ^ {2} \big (s _ {1} (x _ {2}, N R, N R) - u _ {a} \big) \end{array}
$$

(iii) Given that agent one has taken the low action, he is indifferent between recommending and not recommending the project. This condition is a direct result of the other constraints [13, Lemma 8]. The intuition is that in a two report two outcomes model there is sufficient structure to restrict the agent's behavior on the unreached subgame.

$$
\begin{array}{l} \big (g (1 - p _ {1}) + (1 - g) (1 - p _ {2}) \big) s _ {1} (0, N R, R) + g (1 - p _ {1}) s _ {1} (x _ {1}, N R, N R) \\ \quad + (1 - g) (1 - p _ {2}) s _ {1} (x _ {2}, N R, N R) \\ \quad = g p _ {1} s _ {1} (x _ {1}, R, R) + (1 - g) p _ {2} s _ {1} (x _ {2}, R, R) + \big (g p _ {1} + (1 - g) p _ {2} \big) s _ {1} (0, R, R N) \end{array}
$$

(iv) The first agent prefers to take the high action over the low action given the behaviors described in (i)-(iii)

$$
\begin{array}{l} g p _ {1} ^ {2} \big (s _ {1} (x _ {1}, R, R) - u _ {a} \big) + (1 - g) p _ {2} ^ {2} \big (s 1 (x _ {2}, R, R) - u _ {a} \big) \\ \quad + \big (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2}) \big) \big (s _ {1} (0, R, N R) - u _ {a} \big) \\ \quad + \big (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2}) \big) \big (s _ {1} (0, N R, R) - u _ {a} \big) \\ \quad + g (1 - p _ {1}) ^ {2} \big (s _ {1} (x _ {1}, N R, N R) - u _ {a} \big) + (1 - g) (1 - p _ {2}) ^ {2} \big (s _ {1} (x _ {2}, N R, N R) - u _ {a} \big) \\ \geqslant g p _ {1} s _ {1} (x _ {1}, R, R) + (1 - g) p _ {2} s _ {1} (x _ {2}, R, R) + \big (g p _ {1} + (1 - g) p _ {2} \big) s _ {1} (0, R, R N) \end{array}
$$

(v) Ex ante, the first agent earns at least his expected minimum utility by accepting the contract.

$$
\begin{array}{l} g p _ {1} ^ {2} \big (s _ {1} (x _ {1}, R, R) - u _ {a} \big) + (1 - g) p _ {2} ^ {2} \big (s _ {1} (x, R, R) - u _ {a} \big) \\ \quad + \big (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2}) \big) \big (s _ {1} (0, R, N R) - u _ {a} \big) \\ \quad + \big (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2}) \big) \big (s _ {1} (0, N R, R) - u _ {a} \big) \\ \quad + g (1 - p _ {1}) ^ {2} \big (s _ {1} (x _ {1}, N R, N R) - u _ {a} \big) + (1 - g) (1 - p _ {2}) ^ {2} \big (s _ {1} (x _ {2}, N R, N R) - u _ {a} \big) \\ \geqslant u \end{array}
$$

Using these constraints, the principal's problem is:

$$
\begin{array}{l} \min _ {s _ {1}} g p _ {1} ^ {2} s _ {1} (x _ {1}, R, R) + (1 - g) p _ {2} ^ {2} s _ {1} (x _ {2}, R, R) \\ \quad + (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2})) s _ {1} (0, R, N R) \\ \quad + (g p _ {1} (1 - p _ {1}) + (1 - g) p _ {2} (1 - p _ {2})) s _ {1} (0, N R, R) \\ \quad + g (1 - p _ {1}) ^ {2} s _ {1} (x _ {1}, N R, N R) + (1 - g) (1 - p _ {2}) ^ {2} s _ {1} (x _ {2}, N R, N R) \end{array}
$$

subject to (i) to (v).

For the parameter values given in example three, the optimal set of payments to the first agent are:

$$
s _ {1} (x _ {1}, R, R) = v / \left(g p _ {1} (p _ {1} - p _ {2})\right),
$$

$$
s _ {1} (x _ {2}, R, R) = 0,
$$

$$
s _ {1} (0, R, N R) = 0,
$$

$$
s _ {1} (0, N R, R) = 0,
$$

$$
s _ {1} (x _ {1}, N R, N R) = 0,
$$

$$
s _ {1} \left(x _ {2}, N R, N R\right) = v / \left(\left(1 - g\right) \left(1 - p _ {2}\right) \left(p _ {1} - p _ {2}\right)\right)
$$

The procedure for deriving the optimal payments for the second agent is similar to that of the first agent. The only difference is that the second agent can observe the first agent's report before he makes any decisions. There are now nine constraints: (i)-(iv) when the second agent observes a positive recommendation, (i)-(iv) when the second agent observes a negative recommendation, and the minimum utility level constraint.

For the parameter values given in example three, the optimal set of payments to the second agent are

$$
s _ {2} (x _ {2}, R, R) = \Big (v \big (g p _ {1} + (1 - g) p _ {2} \big) ^ {2} \Big) / \big (g (1 - g) p _ {1} p _ {2} (p _ {1} - p _ {2}) \big),
$$

$$
s _ {2} (x _ {2}, R, R) = 0,
$$

$$
s _ {2} (0, R, N R) = \left(v \left(g p _ {1} + (1 - g) p _ {2}\right)\right) / \left((1 - g) p _ {2} \left(p _ {1} - p _ {2}\right)\right),
$$

$$
s _ {2} (0, N R, R) = \left(v \left(1 - \left(g p _ {1} + (1 - g) p _ {2}\right)\right)\right) / \left(g \left(1 - p _ {1}\right) \left(p _ {1} - p _ {2}\right)\right),
$$

$$
s _ {2} (x _ {1}, N R, N R) = 0,
$$

$$
s _ {2} \left(x _ {2}, N R, N R\right) = \left(v \left(1 - \left(g p _ {1} + (1 - g) p _ {2}\right)\right) ^ {2}\right) / \left(g (1 - g) \left(1 - p _ {1}\right) \left(1 - p _ {2}\right) \left(p _ {1} - p _ {2}\right)\right)
$$

## References

1 S.L. Alter, Decision Support Systems: Current practices and challenges, Addison-Wesley, 1980.

2 R.N. Anthony, Planning and control systems: A framework for analysis, Harvard University GSB, 1965.

3 P. Berger and F. Edelman, IRIS: A transaction based DSS for human resource management, in Proceedings of Conference on DSS, Ed. Carlson, E.D., also in Database, Vol. 8, Winter 1977.

4 R.H.C. Bonczek, C.W. Holsapple and A.B. Whinston, The evolving roles of models in Decision Support Systems, Decision Sciences, Vol. 11, No. 2, 1980.

5 J. Christensen, Communication in agencies, The Bell Journal of Economics, Vol 12, No. 2, 1981.

6 R.M. Cyert and J.G. March, A behavioral theory of the firm, Prentice-Hall, 1963.

7 M.H. De Groot, Optimal Statistical Decisions, McGraw Hill, 1970.

8 G. DeSanctis and R.B. Gallupe, A foundation for the study of Group Decision Support Systems, Management Science, Vol. 33, No. 5, May 1987.

9 R.M. Dewan, An economics perspective into the usefulness of Decision Support Systems and Programs, Decision Support Systems, Vol. 8, No. 4, 1992.

10 J.J. Donovan and S.E. Madnick, Institutional and ad-hoc decision support systems and their effective use, Data Base, Vol. 8, No. 3, Winter 1977.

11 G.H. Gorry and M.S. Scott-Morton, A framework for management information systems, Sloan Management Review, Fall 1971.

12 S. Grossman and O. Hart, An analysis of the Principal-Agent problem, Econometrica, Vol. 51, pp. 7–45, 1983.

13 S.C. Hansen, Designing an Organization of Project Evaluators, Ph.D. Dissertation at Carnegie Mellon University, 1988.

14 W.D. Haseman, GPLAN: An operational DSS, Data Base, Vol. 8, No. 3, Winter 1977.

15 B. Holmstrom, Moral Hazard and Observability, The Bell Journal of Economics, Vol. 10, No. 1, 1980.

16 P.G.W. Keen and M.S. Scott-Morton, M.S., Decision Support Systems: An organizational perspective, Addison-Wesley, 1978.

17 R.L. Klaas, A DSS for airline management, Data Base, Vol. 8, No. 3, Winter 1977.

18 J.C. Moore and A.B. Whinston, A model of decision-making with sequential information-acquisition, Decision Support Systems, Part 1 in Vol. 2, 285–307, 1986 and Part 2 in Vol. 3, 47–72, 1987.

19 R. Myerson, Incentive Compatibility and the Bargaining Problem, Econometrica, 47, Jan 1979.

20 H.A. Simon, The new science of management decision, Harper and Row, 1960.

21 R.H. Sprague and H.J. Watson, Bit by bit: Toward Decision Support Systems, California Management Review, XXII, 60–68, Fall 1979.

22 G.R. Wagner, Realizing DSS benefits with IFPS Planning Language, Proceedings of Thirteenth Hawaii International Conference on Systems Sciences, 1980.

23 H.J. Watson, R.H. Sprague and D.W. Kroeber, An empirical study of information systems evolution, Proceedings of Tenth Hawaii International Conference on Systems Sciences, 1977.
