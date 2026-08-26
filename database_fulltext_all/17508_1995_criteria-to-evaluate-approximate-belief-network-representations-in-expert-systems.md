---
otero_id: 17508
otero_key: "S44268F8"
title: "Criteria to evaluate approximate belief network representations in expert systems"
authors: "Sumit Sarkar; Ishwar Murthy"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00045-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Criteria to evaluate approximate belief network representations in expert systems

Sumit Sarkar, Ishwar Murthy

Department of Quantitative Business Analysis, College of Business Administration, Louisiana State University, Baton Rouge, LA 70803, USA

## Abstract

The representation of uncertainty, and reasoning in the presence of uncertainty, has become an important area of research in expert systems. Belief networks have been found to provide an effective framework for the representation of uncertainty using probability calculus. Unfortunately, belief propagation techniques for general network structures are computationally intense. In this paper, we present belief network representations that approximate the underlying dependency structure in a problem domain in order to allow efficient propagation of beliefs. An important issue then is one of obtaining the 'best' approximate representation. A criterion is required to measure the closeness of the approximate to the actual. We examine desirable features of measures that compare approximate representations to the actual one. We identify two well-known measures, called the logarithm rule and the quadratic rule, as having special properties for evaluating approximations. We present a new result that shows the equivalence of using the logarithm rule to that of finding the maximum likelihood estimator. Next, we discuss the modeling implications of using the logarithm rule and the quadratic rule in terms of the nature of solutions that are obtained, and the computational effort required to obtain such solutions. Finally, we use a decision theoretic approach to compare such solutions using a common frame of reference. A simple decision problem is modelled as a belief network, and the comparison is performed over a wide range of probability distributions and cost functions. Our results suggest that the logarithm rule is very appropriate for evaluating approximate representations.

Keywords: Belief networks; Expert systems; Probabilistic reasoning; Scoring rules; Approximate representations; Performance analysis

## 1. Introduction

In recent years, the representation of uncertainty, and reasoning in the presence of uncertainty, has become an important area of research in expert systems. In particular, network structures, called belief networks, have been found to provide an effective framework for the representation of uncertainty using probability calculus [7] [10] [19] [23]. Pearl [24], and Lauritzen and Spiegelhalter [19] have made important contributions towards uncertain reasoning using belief networks. They have presented techniques that can propagate beliefs in such networks in a manner consistent with probability theory. The feasibility of using such networks has been demonstrated for several application areas [1] [2] [14] [42].

In order to use belief-network based expert systems, knowledge engineers must address the problem of constructing such networks for the application domains of interest. This is a critical task, since the performance of an expert system will be highly dependent on the accuracy of the knowledge that is represented in the belief network. In storing domain specific knowledge, a belief network representation must include information about all relevant objects in the problem domain and the dependencies between them. Further, an important requirement for expert systems to perform in real-world applications is that the system should make inferences in a reasonably short time. For this to occur, the representation must also allow for efficient manipulation of information stored in it. In principle, belief network representations can be used to capture all dependencies that may exist across objects of interest. Unfortunately, belief propagation techniques for such general network structures are computationally intense. In fact, Cooper [8] has shown that a theoretically accurate probabilistic inference scheme for multiply connected networks is NP-Hard. Hence, the current practice of achieving computational efficiency is by approximating the inference process, for instance by using simulation based techniques [4] [11] [15] [35]. In this research we propose an alternate approach wherein we consider belief network representations that are approximate. Such representations allow belief propagation techniques to conform to probability calculus and operate within specified levels of computational complexity.

In any application, there typically exists many feasible approximate representations of the probability distribution describing the underlying dependencies. An important issue then is one of obtaining the 'best' approximate representation. Loosely speaking, the best approximate representation is one that is 'closest' in some sense to the dependency structure underlying the application domain. A criterion is then required to measure the closeness of the approximate to the actual.

Obviously, the best representation depends on the criterion that is used. What are the desirable features of any criterion used? Given a choice of possible measures which one is most appropriate? These are the questions that this paper seeks to answer.

In this paper, we first discuss the nature of approximate belief network representations, and identify the factors that determine the computational complexity of making inferences in such networks. We then examine desirable features of measures that compare approximate probabilistic representations to the actual one. Functional forms of measures that satisfy these requirements have been identified in the literature on probability assessments. We show that the logarithm rule and the quadratic rule have some special properties for evaluating assessments. We discuss a known result wherein using the logarithm rule is shown to be equivalent to using the I-Divergence measure. In addition, we present a new result, wherein using the logarithm rule is shown to be equivalent to finding the maximum likelihood estimator. We then compare the use of the logarithm rule and the quadratic rule for obtaining approximate representations in two ways. First, we discuss the modeling implications of using each of these measures. This focuses on the nature of solutions that are obtained when using these measures, and the computational effort required to obtain such solutions. The best solution obtained using the logarithm rule is usually different from the one obtained using the quadratic rule. We use a decision theoretic approach to compare such solutions using a common frame of reference. A simple decision problem is modelled as a belief network, and the comparison is performed over a wide range of probability distributions and cost functions.

This paper is organized as follows. In section 2, we present an overview of belief networks, and characterize structures that are amenable to efficient belief propagation techniques. This also serves the purpose of providing the necessary background and motivation for the issues examined in subsequent sections. In section 3, we discuss the desirable properties of measures used to assess probability distributions. We also demonstrate the equivalence of using the logarithm rule, the I-Divergence measure and the maximum likelihood estimator in the context of this problem. The modeling implications of using the logarithm and quadratic rules are presented in section 4. We compare the performance of representations obtained using the logarithm rule and the quadratic rule respectively in section 5. In section 6, we use a simple example to illustrate how the logarithm rule may be used to evaluate two different approximate structures. A summary of our findings are provided in section 7.

## 2. Representation and propagation of beliefs using network structures

In this section, we discuss properties of belief networks that make them effective for representing uncertainty in expert systems. We identify topological features of belief networks that characterize the computational effort involved in propagating beliefs in such networks. This provides a basis for classifying the complexity of belief network structures, and helps in identifying desirable approximate representations. Finally, we discuss the role of a measure in obtaining efficient belief network structures.

## 2.1. Belief networks in expert systems

Belief networks are directed acyclic graphs in which nodes represent propositions, and arcs signify dependencies between the linked propositions (the terms variables and events are used interchangeably with propositions). The belief accorded to different propositions are stated as probabilities (prior or posterior, as the case may be), and the strengths of the dependencies are quantified by conditional probabilities. A collection of propositions with associated dependencies can be conveniently represented using a belief network as shown in Figure 1(a). The nodes denote propositions of interest in the problem domain. For illustration purposes, consider a hypothetical example in which the nodes refer to attributes of mutual funds that may be used to classify different instances of funds (this example is loosely adapted from an example presented in [37]). Each attribute is considered to be categorical. For example, Fund Types may be classified as: Growth, Growth and Income, and Aggressive Growth; Yield classified as: Under 3%, Over 3%; Price-Earnings Ratio classified as: Above Market, Below Market; long term Projected Earnings Growth classified as: Less than 20%, Greater than 20%, and, Volatility as: Above Market, Below Market. Each arc between two nodes represents a dependency across these attributes, and the direction of the arc indicates an ordering of the attributes. For instance, in Figure 1(a), nodes Fund Type and Yield are predecessors of Price-Earnings Ratio. This indicates that the dependencies between the attributes Fund Type, Yield and Price-Earnings Ratio are represented by storing the conditional probability associated with each value of Price-Earnings Ratio for all possible values of the variables Fund Type and Yield. The absence of a link between two nodes indicates that the attributes are not directly related. Instead, their dependence is mediated by attributes that lie on the paths connecting them. In probabilistic terms, this means that the two nodes are conditionally independent of each other, given the intermediate nodes on the path between them. In Figure 1(a), the nodes Fund Type and Volatility are shown to be conditionally independent of each other given realizations for the attributes Yield and Price-Earnings Ratio. We should note that if a variable has more than one conditioning event, then, strictly speaking, the belief network represents a hypergraph [25]. In Figure 1(a), node Projected Earnings Growth is dependent on two nodes Fund Type and Price-Earnings Ratio; in general, this dependency cannot be captured by the individual dependencies of node Projected Earnings Growth on nodes Fund Type and Price-Earnings Ratio; respectively. Figure 1(b) represents an equivalent belief network, with the variables A through E used to represent the attributes in Figure 1(a). For notational convenience, we subsequently use such symbolic variable names. We return to the example for evaluating mutual funds in section 6, where we discuss how different approximate representations are compared using the logarithm measure.

![](/api/attachments/S44268F8/fulltext/images/581dc859d478aedf417e46223eb5583e3ae43b88a18b2fecc154d8ff236fb7b8.jpg)  
a. Belief Network for Mutual Funds

![](/api/attachments/S44268F8/fulltext/images/105eaf1d11af22767d86e5cc05d13de9b1ccd1393ebb415b0ecaac9247f4adfc.jpg)  
Fig. 1. Belief networks.  
b. Equivalent Network with Symbolic Names belief networks.

A belief network represents a joint distribution $P(X_{1},\ldots,X_{n})$ over the variables of interest $X_{1},\ldots,X_{n}$ . The chain-rule allows joint distributions to be represented as a product of conditional distributions in the following manner:

$$
\begin{array}{l} \mathrm {P(X_ {1} ,\ldots, X_ {n})} \\ = \mathrm {P(X_ {1})\times \prod_ {i = 2,n} P(X_ {i} |X_ {1} ,\ldots, X_ {i - 1}).} \end{array}
$$

Such a representation is called a product-form representation, and is often written as follows:

$$
\mathrm{P} \left(\mathrm{X} _ {1}, \dots , \mathrm{X} _ {\mathrm{n}}\right) = \mathrm{P} \left(\mathrm{X} _ {1}\right) \times \prod_ {\mathrm{i} = 2, \mathrm{n}} \mathrm{P} \left(\mathrm{X} _ {\mathrm{i}} \mid \mathrm{F} \left(\mathrm{X} _ {\mathrm{i}}\right)\right).
$$

Here, $F(X_{i})$ refers to the set of variables on which event $X_{i}$ is conditioned, and is called the parent set for variable $X_{i}$ . For instance, the belief network shown in Figure 1(b) can be completely specified by specifying the following marginal and conditional distributions for all realizations of the variables: P(A), P(B|A), P(C|A, B), P(D|A, C), P(E|B, C).

A belief network is therefore characterized by a structure (or topology), and, a set of probability parameters. The structure provides information regarding conditional independence across events represented in the network. The probability parameters (usually expressed as conditional probabilities) quantify the dependence of an event on its conditioning (parent) events.

A belief network can be used to compute the probability of any realization of a set of variables as a result of observing some other variables. Many different schemes have been proposed to propagate beliefs in general network structures. Each of these schemes belong to one of two classes of propagation techniques – exact propagation of probabilities, or, stochastic simulation. Schemes that belong to the former category are presented in [5] [19] [24], while simulation based schemes are presented in [4] [11] [15] [35], among others.

![](/api/attachments/S44268F8/fulltext/images/772d6cbbe4b75737af2b1770d7f537edc7c5516a88a97d251e4376a046249527.jpg)  
a. Completely Connected

![](/api/attachments/S44268F8/fulltext/images/40d0a079eb18c8ca87a205961252628b6939d5394b74b300b147e7f357a34205.jpg)  
b. Completely Disconnected

![](/api/attachments/S44268F8/fulltext/images/f69b7ec7591f5f11a9350969ea74a61a0710c6e4e2624aeeb1d6375b435dd31f.jpg)  
c. Incompletely Connected  
Fig. 2. Belief networks with different connectivity levels.

## 2.2. Computational complexity of belief propagation in networks

The computational complexity of belief propagation schemes depend entirely on the structure of the network, and not on the probability parameters themselves. Two extreme instances are the completely connected and the completely disconnected structures. For a completely connected network, each variable is dependent on all its preceding variables (Figure 2a). This corresponds to a structure that is computationally the most intense for making inferences. In a completely disconnected network, none of the variables are conditioned on any other variables (Figure 2b). This implies that the variables are mutually independent, and observing one of the variables to be true will not affect our belief in other variables in any way; hence no computations would be required for inference. Using the chain rule, the product-form representation for the completely connected network may be written as: P(A, B, C, D, E)

$$
= \mathrm{P} (\mathrm{A}) \mathrm{P} (\mathrm{B} | \mathrm{A}) \mathrm{P} (\mathrm{C} | \mathrm{AB}) \mathrm{P} (\mathrm{D} | \mathrm{ABC}) \mathrm{P} (\mathrm{E} | \mathrm{ABCD})
$$

By virtue of mutual independence of variables, the completely disconnected network shown in Figure 2(b) is represented as:

$$
\mathrm{P} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}) = \mathrm{P} (\mathrm{A}) \mathrm{P} (\mathrm{B}) \mathrm{P} (\mathrm{C}) \mathrm{P} (\mathrm{D}) \mathrm{P} (\mathrm{E})
$$

Figure 2(c) is an instance of a belief network that is incompletely connected, i.e. it does not have the full complement of arcs that are feasible. The complexity of propagating beliefs using this structure lies somewhere between the above two extreme cases. This network can be represented as: P(A, B, C, D, E)

$$
= \mathrm{P} (\mathrm{A}) \mathrm{P} (\mathrm{B} | \mathrm{A}) \mathrm{P} (\mathrm{C} | \mathrm{A}) \mathrm{P} (\mathrm{D} | \mathrm{AC}) \mathrm{P} (\mathrm{E} | \mathrm{BC})
$$

Lauritzen and Spiegelhalter [19] have devised a technique to propagate beliefs that is applicable for any general network structure. Their method is efficient for sparse network structures, although, like all exact techniques, it is of exponential complexity for complete or near-complete networks. It is regarded to be one of the efficient techniques that have been developed for arbitrary general network structures [22]. The computational complexity of their scheme is shown to be of the order $O(\mathrm{nr}^{\mathrm{m}})$ , where n is the number of variables in the network, r is the maximum number of realizations that a variable may have, and m is the size of the largest clique [22]. The size of a clique in turn depends on the number of conditioning variables (size of the parent set) that a variable has in the product-form expression. Therefore, if the number of parents for a variable is large, then the computational complexity of performing belief propagation in the network is high.

In general, it is expected that each variable will be conditionally independent of other variables in the network given a set of conditioning variables. The efficiency of update mechanisms will depend on the maximum number of variables that constitute the conditioning set for any term in the product-form, which determines the order of the joint distribution for the network. The product-form expression for the network shown in Figure 2(a) is of order 5, since the parent set for variable E includes all the other variables in the network. Similarly, the product-form expression for the network shown in Figure 2(c) is of order 3, because the largest term in the product-form expression consists of three variables. Therefore, the time taken to perform inferences will be much more for the structure in Figure 2(a) as compared to Figure 2(c), since the complexity of inference mechanisms increase exponentially with the order of the product-form distribution.

On the other hand, the ability of a belief network to capture the underlying dependencies across variables improves with increasing connectivity of the structure. By allowing a larger number of parents for each variable, one can better represent the dependencies that are inherent among the variables in the network. Clearly, a completely connected network should be able to represent every dependency that exists in the problem domain in an exact fashion. Similarly, a completely disconnected network will not be able to represent any dependencies across variables. Thus, there is a clear trade-off in the richness of representation that is possible using a belief network with given connectivity, and the computational complexity of making inferences in that network. Performing inferences in completely connected belief networks are too time-consuming to be considered acceptable for most real applications. For instance, when evaluating mutual funds, a fund manager may have to deal with a large number of factors that could affect the performance of a fund. Even if the number of variables was as few as twenty, using the complete joint distribution would not be computationally feasible. Therefore, practically feasible representations are those that are constrained in the number of conditioning variables allowed for each variable in the component terms. We call such representations approximate belief network representations, or in short, approximate representations.

## 2.3. The role of a measure in obtaining efficient network structures

Traditionally, construction of belief networks has required eliciting from domain experts a belief network topology along with its associated probability parameters. In recent years, researchers have developed techniques to obtain belief network structures from historic databases. In both of these approaches, the choice of an appropriate measure plays an important role in obtaining efficient network structures.

When a belief network is directly obtained from domain experts, many different topologies are usually examined. There does not exist any standard criteria for either evaluating alternate network structures, or, identifying the appropriate probability parameters for any given topology. When different structures are considered feasible, then selecting any one among these structures is usually done in an ad-hoc manner. Once a structure is selected, the probability parameters are chosen such that they correspond to the expert's true beliefs. Often, the structure imposes restrictions on what values the parameters can take. In such instances, the parameters are adjusted so that they are as close to the experts beliefs as possible. This can lead to additional problems in obtaining the final structure. For instance, consider the conditional probabilities associated with the variable D in Figure 2(c). If the selected structure does not completely capture the dependencies in the problem domain, then it may not be possible to choose parameters that will lead to inferences that completely agree with the experts beliefs. In such instances, parameters associated with other events that are related to D are often modified as well. This adjustment process could propagate to many other nodes in the network, making it even harder to evaluate the goodness of the final representation. The designers of the expert system PROSPECTOR [10] document many instances where the expert specified parameters were modified in order to take advantage of efficient tree structures for propagating beliefs. In order to compare alternate representations, an appropriate criterion is required to evaluate different representations. Ideally, we require a measure that will help identify the best structure among different feasible structures, as well as determine the probability parameters that should be used with the chosen structure. The measure should enable us to determine the representation that is closest to the true dependency structure that exists in the problem domain when exact representations are computationally prohibitive.

The construction of belief networks from databases appears to be a promising approach for application areas where large amounts of historic data are easily available. Usually, the objective is to obtain networks with structures that are convenient for making inferences. One commonly used structure is the tree structure, as it is very efficient for propagating beliefs. Techniques to obtain efficient structures require some criterion to determine when one structure better captures the dependencies that are displayed by the observed data as compared to some other structure(s). In essence, this is equivalent to determining the best approximate representation that conforms to the specified structural requirements. For instance, Chow and Liu [6] have addressed the problem of representing a joint distribution over n variables by a distribution that supports a tree structure. They use the I-Divergence measure [18] to compare different tree structures with the actual distribution. Rebane and Pearl [27] have extended the methodology proposed by Chow and Liu to recover the structure of a singly connected network using the same I-Divergence measure from a joint distribution that is known to support such a structure. Herskovitz and Cooper [16] have developed an algorithm, called Kutató, that begins with the assumption of marginal independence among variables, and obtains a network incrementally by adding the arc that results in a belief network with minimum entropy. In Cooper and Herskovitz [9], the authors address the problem of finding the most probable belief network given a database using an algorithm called K2. Smyth and Goodman [37] develop a scheme called ITRULE, that takes sample data in the form of discrete attribute vectors, and generates a set of K best rules (where K is a user-defined parameter). They too use an entropy based measure, called the J-measure, to compare rules. Spirtes, Glymour and Scheines [38] discuss two algorithms that recover belief networks from data by checking for conditional independencies across sets of variables using estimated probabilities. The first one, called the SGS algorithm, is computationally intense. They modify this algorithm, which is then called the PC algorithm, such that it can efficiently discover sparse networks underlying a problem domain. When such networks do not exist, or noise in the data prevent accurate estimation of probabilities, they recommend heuristics similar to those used in K2 for practical implementations. In the related problem of obtaining decision trees from data, Quinlan [26] has developed an algorithm called ID3 that uses an entropy based measure to obtain the best decision tree. Uthurusamy et al. [43] use a quadratic measure to obtain decision trees in their algorithm called INFERULE, and demonstrate the resulting structures to be superior to those obtained by ID3. In all of these examples, the measure plays a critical role in comparing different structures, and obtaining relatively sparse structures that effectively capture the dependency across different events in the domain.

## 3. Measures to evaluate approximate representations

As discussed earlier, the choice of an appropriate criterion is very important since the best approximate representation will depend on the criterion chosen, and may be different when different measures are used. First, we formally state the problem. Next, we provide an overview of the existing literature on measures used to evaluate approximate probability distributions, and discuss some fundamental desirable properties for an appropriate measure. Finally, we identify two measures, the quadratic and the logarithm measures, as potentially useful measures.

## 3.1. Generalized problem formulation

The general problem of constructing approximate belief networks can be viewed as one of determining a probability distribution that best approximates the joint distribution underlying the problem domain. Let $P(X_{1},\ldots,X_{n})$ be the underlying distribution and $P_{a}(X_{1},\ldots,X_{n})$ be the approximate distribution that is desired. The distribution $P(X_{1},\ldots,X_{n})$ is either obtained from an expert, or estimated from data. If there are no constraints on the form of the approximate distribution $P_{a}(X_{1},\ldots,X_{n})$ , then it should coincide with the underlying distribution. However, as discussed in Section 2.2, such representations are often inefficient for belief propagation. Feasible approximate distributions are those that are constrained in the following manner. The approximate representation must belong to the family of product-form distributions that are constrained in the number of parents that any variable is allowed to have. If m is the maximum number of conditioning variables allowed, then it must be possible to represent the distribution $P_{a}(X_{1},\ldots,X_{n})$ by the product-form $\Pi_{i=1,n}P_{a}(X_{i}|F(X_{i}))$ , where $P_{a}(X_{i}|F(X_{1})) = P_{a}(X_{1})$ , for some ordering of the variables, such that $max_{i}\{|F(X_{i})|\} \leq m$ . Such distributions will be said to have a connectivity of order m, and the corresponding product-form distributions will be of order $m + 1$ .

In order to determine the best approximate representation for a given m, we need to measure how close the approximate distribution is to the actual one. The best approximate representation $P_{a(\cdot)}$ is one that is closest to $P(\cdot)$ in terms of some measure of closeness $M(P, P_{a})$ . If $P_{a}(\cdot)$ is identical to $P(\cdot)$ , then $M(P, P_{a})$ should be minimized, and

$P_{a}(^{\prime})$ is an exact representation. The resulting optimization problem is:

$$
\text { Min } \mathrm{M} (\mathrm{P}, \mathrm{P} _ {\mathrm{a}})
$$

$$
\begin{array}{l} \text { where } P _ {a} = \Pi_ {i = 1, n} P _ {a} (X _ {i} | F (X _ {i})) \\ \text { s.t. } | F (X _ {i}) | \leq m \quad \{\text { Connectivity   Constraints } \} \end{array}
$$

Finding the ‘best’ belief network representation satisfying the connectivity constraints requires determining the topology that supports the best approximation, and, the optimal probability parameters associated with that topology.

## 3.2. Scoring rules

Approximate probability distributions have been analyzed for the purpose of judging subjective probability assessments made by experts (e.g. weather forecasts by meteorologists). A reasonable measure is a function of the approximate probability distribution and subsequent observations of the actual realizations. Terminologies used for such measures include scoring rules, reward functions [40], incentive functions [20], and scoring systems [36]. We adopt the term scoring rule in this paper.

Scoring rules are designed to (i) evaluate different probability assessments, and (ii) encourage assessors to provide their true ('honest') estimates. Let Y be an uncertain quantity represented by a probability distribution F on an outcome space S, and let $E_{1}, E_{2}, \ldots, E_{n}$ constitute an n-fold partition of S (i.e., they are a set of n mutually exclusive and exhaustive events). The probability mass in $E_{j}$ is denoted by $p_{j}$ , where $p_{j} = P(Y \in E_{j})$ . The vector $\mathbf{p} = (p_{1}, \ldots, p_{n})$ , represents the true probability values, and $\mathbf{r} = (r_{1}, \ldots, r_{n})$ represents the assessors stated beliefs. The assessment receives a score $S_{k}(\mathbf{r})$ if the $k^{th}$ event occurs. The expected score for the assessed distribution r is $S(\mathbf{p}, \mathbf{r})$ , where $S(\mathbf{p}, \mathbf{r}) = \Sigma_{k} p_{k} S_{k}(\mathbf{r})$ .

A desirable property of such rules is that the score should be maximized when the assessment coincides with the actual. Scoring rules that satisfy this requirement are those for which $S(\mathbf{p}, \mathbf{p}) \geqslant S(\mathbf{p}, \mathbf{r})$ for any p and r (i.e. assessments other than p cannot get a higher score than p itself).

Such rules are called proper scoring rules. Scoring rules could also be defined in a way such that a low score is preferred to a high score. In that case, the rule would be proper if the score is minimized by setting r = p.

An assessment is evaluated based on the assessed distribution r, and the event that is realized. Scoring rules, therefore, should be non-decreasing functions of $r_{k}$ , where k is the event realized (i.e., $S_{k}(r)$ is non-decreasing in $r_{k}$ ). This ensures that an assessment $r_{k}^{\prime}$ will get a higher score than $r_{k}$ if k is the event realized and $r_{k}^{\prime} > r_{k}$ . There are potentially an infinite number of functions that may serve as proper scoring rules. McCarthy [21], Marschak [20], and Shuford et al. [36], among others, have provided different characterizations for the functional form of proper scoring rules for different situations. Among the various possible proper scoring rules, three have received particular attention in the literature. They are:

\- Quadratic scoring rule [3], defined as:

$$
\mathrm{S} (\mathbf {p}, \mathbf {r}) = - \Sigma \left(\mathrm{p} _ {\mathrm{k}} - \mathrm{r} _ {\mathrm{k}}\right) ^ {2}.
$$

\- Logarithmic scoring rule [13], defined as: $\mathbf{S}(\mathbf{p},\mathbf{r}) = \sum \mathbf{p}_{\mathrm{k}}\log \mathbf{r}_{\mathrm{k}}.$

\- Spherical scoring rule [28], defined as: $\mathrm{S}(\mathbf{p},\mathbf{r}) = \Sigma (\mathbf{p},\mathbf{r}) = \Sigma \mathbf{p}_{\mathrm{k}}\mathbf{r}_{\mathrm{k}} / (\Sigma \mathbf{r}_{\mathrm{i}}^{2})^{0.5}$ .

It is easily seen that any linear transformation of a proper scoring rule is also a proper rule.

## 3.3. Properties of the quadratic rule

The choice is more limited when additional features are required of a scoring rule. In particular, when it is required that the rule be a function of the discrepancy $(p_{i}-r_{i})$ then the quadratic rule is the only one that satisfies this requirement [31]. Savage [31] also shows that it is the only proper rule that is symmetric over p and r (i.e. $S(\mathbf{p},\mathbf{r})=S(\mathbf{r},\mathbf{p})$ ). It is easy to see that the quadratic rule is equal to the negative of the second-norm function (which is the euclidean distance in the n-dimensional vector space). Therefore, maximizing the quadratic rule is equivalent to minimizing the second-norm vector function. Subsequently, this rule exhibits all the desirable properties of such a norm function, including the triangle inequality property. This measure has been used in [43] to obtain sparse decision trees from data.

## 3.4. Properties of the logarithm rule

A different requirement often imposed on a scoring rule is that the score depend only on the probability assigned to the event that is actually realized (called the principle of relevance [40]). For instance, in a three event state space, the two assessments (0.6, 0.3, 0.1) and (0.6, 0.2, 0.2) should receive the same score if the first event was realized (if one of the other two events were to occur, the two assessments would get different scores). It has been shown that the logarithm rule is the only proper scoring rule that satisfies this requirement for any arbitrary n [40] [31]. Proof of uniqueness of the logarithmic rule has been demonstrated in [40].

An important limitation of the logarithm rule is that it is not a norm function [17]. However, in the context of evaluating belief networks, the logarithm rule is equivalent to two important criteria that have been used in practice to learn dependency structures from historical data. These are: (i) the information theoretic measure called the I-Divergence measure [18]; and (ii) the statistical maximum likelihood criterion. We first discuss the well-known equivalence between the I-Divergence measure and the logarithm rule in evaluating belief network structures. Next, we prove that finding the maximum likelihood estimate from among all the feasible solutions is also equivalent to using the logarithm rule.

## 3.4.1. Logarithm rule and the I-Divergence measure

In communication theory, the I-Divergence measure has been widely used to determine the best estimate of an unknown probability distribution. Subsequently, the I-Divergence measure has been used by Chow and Liu [6] to obtain tree structured representations. Many other researchers have also used this measure in obtaining network structures [12] [27] [44] [45]. It is defined as the difference in the information contained in the actual distribution p and the information contained in the approximate distribution r about the actual distribution p. The I-Divergence measure $D(\mathbf{p}, \mathbf{r})$ is expressed as:

$$
\mathrm{D} (\mathbf {p}, \mathbf {r}) = \sum \mathrm{pi} \log \frac {\mathrm{pi}}{\mathrm{r} _ {\mathrm{i}}} = \sum \mathrm{pi} \log \mathrm{pi} - \sum \mathrm{pi} \log \mathrm{r} _ {\mathrm{i}}
$$

This measure is always positive when the distributions p and r are different, and zero when they are identical [18]. Since the expression $\Sigma_{pi}$ log pi does not depend on the approximate representation, it is easy to see that the logarithm scoring rule is a linear transformation of the I-Divergence measure, and minimizing the I-Divergence measure is equivalent to maximizing the logarithm scoring rule. Hence, the best solution obtained using the logarithm rule is also the one that minimizes the difference in information between the approximate and actual representations, respectively.

Smyth and Goodman [37] use an entropy based measure, which they call the J-measure, in their scheme called ITRULE, that generates a set of K best probabilistic rules from sample data. As pointed out by the authors, the J-measure is a special instance of the I-Divergence measure, and is used to quantify the goodness of a rule of the form “If X = x then Y = y with probability p”. In a belief network, when such a rule is included, then corresponding rules for all other realizations of X must also be included. In that case, using the J-measure becomes equivalent to the I-Divergence measure.

## 3.4.2. Logarithm rule and the maximum likelihood estimate

The maximum likelihood estimator is widely used for estimating distributions in statistical analysis. Cooper and Herskovitz [9] have formulated the problem of constructing the best approximate belief network from data as one of finding the most probable network given a database. Assuming that all feasible network structures are equally likely when no information is available, this is equivalent to finding the belief network (structure with associated parameters) whose joint distribution maximizes the likelihood among all feasible solutions given the data. We show that the belief network that maximizes the logarithm score is also one that is the maximum likelihood estimator.

Consider the problem of determining the belief network that is the maximum likelihood estimator. Let the true distribution that characterizes the problem domain be $\mathrm{P}(\mathbf{X}) = \mathrm{P}(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n})$ , and let $\mathrm{P}_{\mathrm{a}}(\mathbf{X}) = \mathrm{P}_{\mathrm{a}}(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n})$ be some unknown distribution that satisfies the connectivity constraint. When the belief network is induced from historical data, then $\mathrm{P}(\mathbf{X})$ is the best estimate of the true underlying distribution. Let the sample data consist of s instances of the set of variables, denoted by $X^{S} = \{x^{1}, \ldots, x^{s}\}$ . For instance, we may have the following five data instances for three binary variables: $X^{S} = \{(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 0, 1), (1, 0, 0)\}$ .

For distribution $P_{a}(X)$ , the likelihood function is:

$$
\mathrm{L} = \prod_ {\mathrm{j}} \mathrm{P} _ {\mathrm{a}} (\mathbf {x} ^ {\mathrm{j}}) = \prod_ {\mathrm{j}} \prod_ {\mathrm{i} = 1, \mathrm{n}} \mathrm{P} _ {\mathrm{a}} \left(\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}} \mid \mathrm{F} \left(\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}}\right)\right)
$$

Let $L'$ be defined as the log likelihood, i.e. $L' = \log L$ . Then:

$$
\begin{array}{r l} \mathrm {L^ {\prime}} & = \log \prod_ {\mathrm{j}} \prod_ {\mathrm{i} = 1, \mathrm{n}} \mathrm {P_ {a}} (\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}} | \mathrm{F} (\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}})) \\ & = \sum_ {\mathrm{j}} \sum_ {\mathrm{i} = 1, \mathrm{n}} \log \mathrm {P_ {a}} (\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}} | \mathrm{F} (\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}})) \\ & = \sum_ {\mathrm{i} = 1, \mathrm{n}} \sum_ {\mathrm{j}} \log \mathrm {P_ {a}} (\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}} | \mathrm{F} (\mathrm{x} _ {\mathrm{i}} ^ {\mathrm{j}})) \end{array}
$$

Each instance $(\mathbf{x}_{i}^{j}, \mathbf{F}(\mathbf{x}_{i}^{j}))$ is a subset of the jth instance in the database. Each such subset corresponds to one of a finite number of realizations for the variables included in the subset. For instance, the pair of variables $(\mathbf{x}_{1}, \mathbf{x}_{2})$ in the example mentioned earlier can take on four values: $\{(0, 0), (0, 1), (1, 0), (1, 1)\}$ . Let the total number of such possibilities associated with the set of variables $(\mathbf{x}_{i}, \mathbf{F}(\mathbf{x}_{i}))$ be $r_{i}$ , and the true and approximate conditional probabilities associated with each realization be denoted as $\mathrm{P}^{\mathrm{k}}(\mathbf{x}_{i} | \mathrm{F}(\mathbf{x}_{i}))$ and $\mathrm{P}_{\mathrm{a}}^{\mathrm{k}}(\mathbf{x}_{i} | \mathrm{F}(\mathbf{x}_{i}))$ for k = 1, $r_{i}$ . Further, let the total number of occurrences for each realization of $(\mathbf{x}_{i}, \mathbf{F}(\mathbf{x}_{i}))$ be $f^{\mathrm{k}}(\mathbf{x}_{i}, \mathbf{F}(\mathbf{x}_{i}))$ , for k = 1, $r_{i}$ . Then: $\sum \log \mathrm{P}_{\mathrm{a}}(\mathbf{x}_{i}^{\mathrm{j}} | \mathrm{F}(\mathbf{x}_{i}^{\mathrm{j}}))$

$$
\begin{array}{r l} & \sum_ {j} \log P _ {a} (x _ {i} ^ {j} | F (x _ {i} ^ {j})) \\ & = \sum_ {k} f ^ {k} (x _ {i}, F (x _ {i})) \log P _ {a} ^ {k} (x _ {i} | F (x _ {i})) \end{array}
$$

The estimate for the true underlying joint distribution $P^{k}(x_{i}, F(x_{i}))$ is obtained by finding, for each feasible realization of $(x_{i}, F(x_{i}))$ , the proportion of instances in the database with that realization as compared to the total number of instances, i.e.

$$
\mathrm{P} ^ {\mathrm{k}} \left(\mathrm{x} _ {\mathrm{i}}, \mathrm{F} \left(\mathrm{x} _ {\mathrm{i}}\right)\right) = \frac {\mathrm{f} ^ {\mathrm{k}} \left(\mathrm{x} _ {\mathrm{i}} , \mathrm{F} \left(\mathrm{x} _ {\mathrm{i}}\right)\right)}{\mathrm{s}}.
$$

Therefore:

$$
\begin{array}{r l} & \sum_ {k} f ^ {k} (x _ {i}, F (x _ {i})) \log P _ {a} ^ {k} (x _ {i} | F (x _ {i})) \\ & = s \sum_ {k} \frac {f ^ {k} (x _ {i} , F (x _ {i}))}{s} \log P _ {a} ^ {k} (x _ {i} | F (x _ {i})) \\ & = s \sum_ {k} P ^ {k} (x _ {i}, F (x _ {i})) \log P _ {a} ^ {k} (x _ {i} | F (x _ {i})) \end{array}
$$

Subsequently, we have:

$$
\begin{array}{r l} \mathrm{L} ^ {\prime} & = \sum_ {i = 1, n} s \sum_ {k} \mathrm{P} ^ {k} (x _ {i}, F (x _ {i})) \log \mathrm{P} _ {a} ^ {k} (x _ {i} | F (x _ {i})) \\ & = s \sum_ {i = 1, n} \sum_ {k} \mathrm{P} ^ {k} (x _ {i}, F (x _ {i})) \log \mathrm{P} _ {a} ^ {k} (x _ {i} | F (x _ {i})) \end{array}
$$

A well-known property of the logarithm transformation is that $L'$ is maximized when L is maximized. Since s is fixed for a given database, we have:

$$
\begin{array}{l} \text {Max L^{\prime}} \\ = \text {Max} \sum_ {\mathrm{i=1,n}} \sum_ {\mathrm{k}} \mathrm{P} ^ {\mathrm{k}} (\mathrm{x} _ {\mathrm{i}}, \mathrm{F} (\mathrm{x} _ {\mathrm{i}})) \log \mathrm{P} _ {\mathrm{a}} ^ {\mathrm{k}} (\mathrm{x} _ {\mathrm{i}} | \mathrm{F} (\mathrm{x} _ {\mathrm{i}})) \end{array}
$$

Next, consider the problem formulation (as stated in section 3.1) when the logarithm rule is used. To obtain the best approximation, we must solve the following optimization problem:

$$
\begin{array}{r l} & \text { Max } \sum_ {\mathbf {X}} \mathrm{P} (\mathbf {X}) \log \mathrm{P} _ {\mathrm{a}} (\underline {{\boldsymbol {X}}}) \\ & \text { where } \mathrm{P} _ {\mathrm{a}} = \prod_ {\mathrm{i} = 1, \mathrm{n}} \mathrm{P} _ {\mathrm{a}} (\mathrm{x} _ {\mathrm{i}} | \mathrm{F} (\mathrm{x} _ {\mathrm{i}})) \\ & s. t. | F (\mathrm{x} _ {i}) | \leq m \end{array}
$$

The objective function can be manipulated as shown:

$$
\begin{array}{r l} & \text { Max } \sum_ {\mathbf {X}} P (\mathbf {X}) \log \prod_ {i = 1, n} P _ {a} (x _ {i} | F (x _ {i})) \\ & = \text { Max } \sum_ {\mathbf {X}} P (\mathbf {X}) \sum_ {i = 1, n} \log P _ {a} (x _ {i} | F (x _ {i})) \end{array}
$$

$$
\begin{array}{l} = \text { Max } \sum_ {\mathbf {X}} \sum_ {i = 1, n} \mathrm{P} (\mathbf {X}) \log \mathrm{P} _ {\mathrm{a}} (\mathrm{x} _ {i} | \mathrm{F} (\mathrm{x} _ {i})) \\ = \text { Max } \sum_ {i = 1, n} \sum_ {\mathbf {X}} \mathrm{P} (\mathbf {X}) \log \mathrm{P} _ {\mathrm{a}} (\mathrm{x} _ {i} | \mathrm{F} (\mathrm{x} _ {i})) \\ = \text { Max } \sum_ {i = 1, n} \sum_ {\mathrm{xi}, \mathrm{F} (\mathrm{xi})} \mathrm{P} (\mathrm{x} _ {i}, \mathrm{F} (\mathrm{x} _ {i})) \\ \log \mathrm{P} _ {\mathrm{a}} (\mathrm{x} _ {i} | \mathrm{F} (\mathrm{x} _ {i})) \\ = \text { Max } \sum_ {i = 1, n} \sum_ {\mathrm{k}} \mathrm{P} ^ {\mathrm{k}} (\mathrm{x} _ {i}, \mathrm{F} (\mathrm{x} _ {i})) \\ \log \mathrm{P} _ {\mathrm{a}} ^ {\mathrm{k}} (\mathrm{x} _ {i} | \mathrm{F} (\mathrm{x} _ {i})) \\ \text { where   k   is   as   defined   earlier. } \end{array}
$$

The above expression is the same as the one obtained for the maximum likelihood estimator; hence using the two criteria are equivalent.

## 4. Modeling features of the quadratic and logarithm scoring rules

In choosing a measure to evaluate approximate representations, a proper scoring rule is clearly very desirable. As discussed in section 3, the quadratic and the logarithm scores have been shown to have some additional desirable properties that make them appropriate for evaluating approximations. Therefore, in this section, we discuss some modeling implications of using these two rules, respectively.

## 4.1. Modeling using the logarithm scoring rule

In many applications, an expert (or experts) may be able to specify either one or a small number of alternate topologies for a problem domain. If a unique topology is specified, the problem reduces to one of determining the best set of probability parameters given the topology. When alternate topologies are to be considered, then the best representation for each topology (in terms of the probability statistic) is compared using the chosen measure. We examine how the quadratic and logarithm scores can be used in these circumstances.

The logarithm rule leads to a problem formulation with some very attractive properties. We state a result that enables us to obtain the probability parameters relatively easily.

Proposition: When using the logarithm rule, the best set of probability parameters for a given topology are those that preserve the joint probabilities of the component terms for the corresponding product-form representation. This result follows from the fact that the objective function for the associated optimization problem contains the logarithm of the approximate distribution which is a product-form, and subsequently may be expressed as the sum of the logarithm of the individual components of the approximate distribution. Since the logarithm rule is a proper scoring rule, the objective function is optimized when the probability parameters associated with each component of the approximate distribution are equal to the corresponding parameters for the actual distribution. A formal proof of this result is shown in [30]. Consider the topology shown in Figure 2(c) as an approximation to the completely connected representation shown in Figure 2(a). By virtue of the above property, the best set of probability parameters obtained using the logarithm rule will satisfy the following conditions:

$$
\begin{array}{l} \bullet \mathrm {P_ {a} (A) = P(A)} \\ \bullet \mathrm {P_ {a} (B|A) = P(B|A)} \\ \bullet \mathrm {P_ {a} (C|A) = P(C|A)} \\ \bullet \mathrm {P_ {a} (D|A,C) = P(D|A,C)} \\ \bullet \mathrm {P_ {a} (E|B,C) = P(E|B,C)} \end{array}
$$

This property holds for any feasible topology that is considered as an approximation. An outcome of this property is that if the topology is specified, then the probability parameters for each component can be easily obtained. The joint distribution for the complete representation is obtained by using the appropriate product-form for the given topology.

The logarithm rule can also be efficiently applied for those instances where the best representation is to be chosen from one of a small number of alternate structures that are provided by the expert. The best set of probability parameters for each alternative is easily obtained. The best topology is then selected by evaluating the score for the optimal set of parameters associated with each topology. The number of terms in the evaluation function increases exponentially with the number of variables in the problem domain. For example, if there are n binary variables being considered, then the number of terms to be computed is $2^{n}$ . However, useful approximate representations will usually have low order productforms. This allows the scoring function to be decomposed into smaller components. For the topology shown in Figure 2(a) the score is:

$$
\begin{array}{l} = \sum_ {\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}} \mathrm{P} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}) \\ \times \log \mathrm {P_ {a}} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}) \\ = \sum_ {\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}} \mathrm{P} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}) \\ \log (\mathrm {P_ {a}} (\mathrm{A}) \times \mathrm {P_ {a}} (\mathrm{B} | \mathrm{A}) \times \mathrm {P_ {a}} (\mathrm{C} | \mathrm{A}) \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text { } \\ = \sum_ {\mathrm{A}} \mathrm{P} (\mathrm{A})   \log   \mathrm {P_ {a}} (\mathrm{A}) + \sum_ {\mathrm{A}, \mathrm{B}} \mathrm{P} (\mathrm{A}, \mathrm{B}) \\ \log   \mathrm {P_ {a}} (\mathrm{B} | \mathrm{A}) + \sum_ {\mathrm{A}, \mathrm{C}} \mathrm{P} (\mathrm{A}, \mathrm{C})   \log   \mathrm {P_ {a}} (\mathrm{C} | \mathrm{A}) \\ + \sum_ {\mathrm{A}, \mathrm{C}, \mathrm{D}} \mathrm{P} (\mathrm{A}, \mathrm{C}, \mathrm{D})   \log   \mathrm {P_ {a}} (\mathrm{D} | \mathrm{A}, \mathrm{C}) \\ + \sum_ {\mathrm{B}, \mathrm{C}, \mathrm{E}} \mathrm{P} (\mathrm{B}, \mathrm{C}, \mathrm{E})   \log   \mathrm {P_ {a}} (\mathrm{E} | \mathrm{B}, \mathrm{C}) \\ = \sum_ {\mathrm{A}} \mathrm{P} (\mathrm{A})   \log   \mathrm{P} (\mathrm{A}) + \sum_ {\mathrm{A}, \mathrm{B}} \mathrm{P} (\mathrm{A}, \mathrm{B}) \\ \log   \mathrm{P} (\mathrm{B} | \mathrm{A}) + \sum_ {\mathrm{A}, \mathrm{C}} \mathrm{P} (\mathrm{A}, \mathrm{C})   \log   \mathrm{P} (\mathrm{C} | \mathrm{A}) \\ + \sum_ {\mathrm{A}, \mathrm{C}, \mathrm{D}} \mathrm{P} (\mathrm{A}, \mathrm{C}, \mathrm{D})   \log   \mathrm{P} (\mathrm{D} | \mathrm{A}, \mathrm{C}) \\ + \sum_ {\mathrm{B}, \mathrm{C}, \mathrm{E}} \mathrm{P} (\mathrm{B}, \mathrm{C}, \mathrm{E})   \log   \mathrm{P} (\mathrm{E} | \mathrm{B}, \mathrm{C}) \\ = 0. 5 7 8 4 9 6 3 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 8. 5 7 8 4 9 6 3 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 8. 5 7 8 4 9 6 3 1 2 0 0 0 0 0 0 0 0 0, \\ = - (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. -) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-} (1. +) ^ {-}
$$

{follows from the proposition stated earlier}.

The overall score for the representation can be obtained by evaluating each of the component expressions independently. Since the number of variables that are allowed in any component is restricted to $m + 1$ , each expression can be evaluated by computing a relatively smaller number of terms. Assuming that all variables are binary, the maximum number of terms that need to be evaluated for any one expression will be $2^{m+1}$ . Since there will be a total of n such expressions, the total number of terms to be evaluated is no more than $n \cdot 2^{m+1}$ . For n much greater than m, it is easy to see that there will be enormous computational savings in using the decomposed version of the evaluation function. When variables are not restricted to be binary, the computational savings will be even greater.

When the topology for the approximate representation is not specified (e.g. when the network structure is being induced from data), then finding the best representation is a hard problem. All feasible topologies must be considered, and the best logarithm solution for each of these topologies must be compared in order to determine the optimal representation. For each feasible topology, the above property of the logarithm scoring rule is still applicable; however, the number of topologies that need to be considered increases exponentially with the number of variables in the network. The problem appears to be hard, although some special cases have been shown to be tractable [6]. Heuristic techniques will be required to obtain good solutions for such problem instances in general [38].

## 4.2. Modeling using the quadratic scoring rule

Determining the best solution is more difficult when the quadratic scoring rule is used to evaluate different representations. Unlike when using the logarithm rule, using the quadratic rule does not help in decomposing the objective function into its different components. The product-form nature of the approximate representation has to be enforced by incorporating constraints into the optimization formulation. For a given topology, determining the best solution requires solving the resulting optimization problem. For the topology shown in Figure 2(c), the optimization problem will be:

$$
\begin{array}{r l} & {\mathrm{Min} \mathrm{S} (\mathrm{P}, \mathrm{P} _ {\mathrm{a}})} \\ & {\quad = \mathrm{Min} \sum_ {\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}} \left(\mathrm{P} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}) \right.} \\ & {\quad \left. - \mathrm{P} _ {\mathrm{a}} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E})\right) ^ {2}} \end{array}
$$

$$
\begin{array}{r l} & \text {s.t.} P _ {a} (A, B, C, D, E) \\ & = P _ {a} (A) \times P _ {a} (B | A) \times P _ {a} (C | A) \\ & \quad \times P _ {a} (D | A, C) \times P _ {a} (E | B, C) \end{array}
$$

for all realizations of the variables.

The problem is one of non-linear optimization, with a quadratic objective function and non-linear constraints. The exact nature of the constraints depends on the product-form of the approximate distribution (the optimization problem formulation is discussed in further detail in [Sarkar, 1993]). Exact analytic solutions do not exist for such problems in general, and numerical approximation techniques must be used to solve them. Such techniques are not guaranteed to find the global optimal solutions. A serious drawback is that the number of terms that are to be computed will grow exponentially with the size of the problem, making it intractable for large problem sizes.

fashion. Clearly, exact solutions will not be feasible for large problem instances.

When alternate topologies are considered, then the best quadratic solution for each topology needs to be obtained, and the scores compared. When no topologies are specified, then finding the best quadratic solution is a very difficult problem. The best quadratic approximation for all feasible topologies have to be compared using the quadratic score. Obtaining the best solution for a given topology requires computations that increase exponentially with the size of the problem. The number of feasible topologies that must be considered also increase in an exponential

## 5. Experimental comparison of the quadratic and logarithm scoring rules

The logarithm rule is much easier to use than the quadratic rule when the best representation is desired for a given topology, or one among a few topologies is to be selected. The best representation obtained when using the logarithm rule will usually not be the same as the one obtained using the quadratic rule. In this section we compare the quality of the solutions obtained from these rules using a decision theoretic framework. We describe a decision problem that is modeled as a belief network. The decision problem consists of five binary variables which are interrelated. The nature of the dependencies among the variables is shown in Figure 3(a). We assume that the topology for the approximate representation is fixed, and as shown in Figure 3(b). A brief discussion on the choice of the actual and approximate representations is required here. The approximate topology chosen is one that may be easily converted to a tree-structure by incorporating auxiliary variables [29]. Joint distributions that correspond to tree structures are those in which all component terms have at most one conditioning variable. This makes such representations very efficient for propagating beliefs; hence, the structure shown in Figure 3(b) is an efficient one. The only difference between the actual and approximate topology is that the arc BE appears in the actual topology and not in the approximate. This enables us to subsequently examine different distributions by varying the strength of the dependency associated with this arc.

![](/api/attachments/S44268F8/fulltext/images/8cdff1d6b86c72e40d98679c2f08e40c8e75e1437082b07b4b6b49e3c5a77891.jpg)  
Fig. 3. Belief Network for the Decision Problem.

We obtain the best representation for a given approximate topology when using the quadratic and logarithm rule respectively. The solutions obtained when using each of these rules are compared as follows. The node A is considered to be the hypothesis variable. The decision problem is to predict whether the hypothesis variable is true or not when some of the other variables have been observed. When the actual representation is used, then the revised belief that the hypothesis is true is obtained by using the distribution associated with the actual representation. Similarly, when an approximate representation is used, then the revised belief is obtained by using the distribution associated with the approximate representation. When an approximate representation is used instead of the actual one, the decisions made may or may not coincide with ones made with the actual representation. When the decisions made are the same, then no losses are deemed to incur. When decisions made are not the same, then the use of the approximate distribution results in losses that are characterized as Type I and Type II losses. We evaluate the expected losses associated with the quadratic and logarithm approximations when different sets of variables are observed, as well as for a wide range of Type I and Type II errors. Subsequently, we perform this analysis for different distributions associated with the actual topology by varying the strength of dependency associated with the arc BE. The expected losses associated with each approximation are summarized and compared.

## 5.1. The decision problem

The decision problem is to predict whether the hypothesis variable A is true or false. In practice, decisions are made without exact knowledge about A. It may be possible to observe some of the variables B, C, D and E before a decision has to be made about variable A. Knowledge of the value of other variables will affect our belief in event A. For instance, the variables C and E may be observed to be true prior to making a decision. The belief in A is revised to account for this information using the actual and approximate representations, respectively. The posterior probabilities obtained for event A using the different distributions are then used for prediction.

There are two types of errors associated with making a prediction in the absence of perfect information. If A is predicted to be “Not True” when it is actually true, then we have a Type I error, and when A is predicted to be “True” when it is actually not true, we have a Type II error. The costs associated with these wrong decisions are denoted by $C_{1}$ and $C_{2}$ respectively. If the prediction is correct then there is no cost associated with the decision. The approximate representations are analyzed by evaluating the decisions made when using the approximate distributions respectively and comparing them with the decision made when using the actual distribution. The expected costs when using the approximate and actual distributions are analyzed for different values of $C_{1}$ and $C_{2}$ .

## 5.2. Actual and approximate distributions

The joint distribution for the actual network in Figure 3(a) can be obtained by specifying the joint distribution P(A, B, C), and the conditional distributions P(E|B, C) and P(D|E, C) for all realizations of the variables. In order to simplify the specification of the complete distribution, the joint distribution for the variables (A, B, C) is chosen identical to that for variables (D, E, C). The distributions used for the variables (A, B, C) and (C, D, E) are shown in Table 1. Table 2 displays the joint distribution for (B, C, E), which is equivalent to specifying the conditional distribution P(E|B, C). Table 3 displays the resulting complete joint distribution over the five variables. In these tables, an entry of the form P(A) = 0.5 indicates that the probability of event A being true is 0.5, whereas earlier, the notation P(A) has been used to denote the complete distribution for variable A. For notational convenience, we use P(A) to refer to a specific outcome for event A (i.e. event A is true) for the example considered in this section.

Joint distributions for (A, B, C) and (C, D, E)

<table><tr><td>P(A) = 0.5</td><td>P(B) = 0.6</td><td>P(C) = 0.4</td><td></td></tr><tr><td>P(AB) = 0.4</td><td>P(AC) = 0.3</td><td>P(BC) = 0.31</td><td>P(ABC) = 0.25</td></tr><tr><td>P(C) = 0.4</td><td>P(D) = 0.5</td><td>P(E) = 0.6</td><td></td></tr><tr><td>P(CD) = 0.3</td><td>P(CE) = 0.31</td><td>P(DE) = 0.4</td><td>P(CDE) = 0.25</td></tr></table>

Table 2
Distribution P(B, C, E)

<table><tr><td>P(B) = 0.6</td><td>P(C) = 0.4</td><td>P(E) = 0.6</td><td></td></tr><tr><td>P(BC) = 0.31</td><td>P(BE) = 0.38</td><td>P(CE) = 0.31</td><td>P(BCE) = 0.26</td></tr></table>

The best quadratic and logarithm solutions are obtained for the approximate topology. The logarithm approximation is easily obtained, since it preserves the marginal distribution P(A) and the conditional distributions P(B | A), P(C | A, B), P(E | C) and P(D | C, E) from the actual network. The quadratic approximation requires solving the optimization problem presented in Section 3.1 in which the objective function is the quadratic score (details of this formulation are discussed in [30]). A non-linear optimization code, called NCONF, from the IMSL library of mathematical routines has been used to obtain the quadratic solution. The routine uses a successive quadratic programming algorithm $[32]$ $[33]$ $[41]$ . Due to the existence of multiple local optima, the procedure could terminate at some locally optimal solution. To reduce the likelihood of using local optima that are not global, the procedure is run with different starting solutions, and the best solution is chosen. In addition, to ensure that the solution obtained is indeed a good one (if not the best), the quadratic score for the IMSL solution is compared with the quadratic score for the logarithm solution. If the quadratic score for the logarithm solution is better than for the IMSL solution, then the IMSL solution is discarded, and more solutions are generated using some other starting points. This is repeated until the IMSL solution obtained has a better quadratic score than the best logarithm solution. This ensures that neither of the approximations being compared dominates the other one for both the quadratic and the logarithm score. The probability masses for the approximate solutions (when the actual distribution is as shown in Table 3) are displayed in Appendix I.

## 5.3. Costs using the actual and approximate distribution

In order to evaluate the performance of the two approximate solutions, the costs of using the actual and the two approximate distributions have to be determined for the decision problem. We illustrate this with the help of an example. In this example, we assume that the exact distribution is as shown in Table 3, and the approximate distributions are as shown in Appendix I. We further consider an instance where the variables C and E have been observed before a prediction is to be made about the hypothesis variable A. Consider the case when both variables C and E are observed to be true. The posterior belief in variable A being true (i.e. P(A|CE)) is first evaluated using the actual distribution. Using the probabilities for the actual distribution in Table 3, we obtain P(A|CE) = P(ACE)/P(CE) = 0.23746/0.31 = 0.766. The cost of making a decision can then be evaluated using the decision tree shown in Figure 4. At the decision node, the decision maker can do one of two things: predict that A is “True”, or that A is “Not True”. Subsequent to this decision, A may actually turn out to be true or not.

<table><tr><td colspan="5">Complete joint distribution</td></tr><tr><td>P(A) = 0.5</td><td>P(B) = 0.6</td><td>P(C) = 0.4</td><td>P(D) = 0.5</td><td>P(E) = 0.6</td></tr><tr><td>P(AB) = 0.4</td><td>P(AC) = 0.3</td><td>P(AD) = 0.29035</td><td>P(AE) = 0.4</td><td>P(BC) = 0.31</td></tr><tr><td>P(BD) = 0.32694</td><td>P(BE) = 0.38</td><td>P(CD) = 0.3</td><td>P(CE) = 0.31</td><td>P(DE) = 0.4</td></tr><tr><td>P(ABC) = 0.25</td><td>P(ABD) = 0.23778</td><td>P(ABE) = 0.27175</td><td>P(ACD) = 0.22624</td><td>P(ACE) = 0.23746</td></tr><tr><td>P(ADE) = 0.23778</td><td>P(BCD) = 0.23746</td><td>P(BCE) = 0.26</td><td>P(BDE) = 0.27175</td><td>P(CDE) = 0.25</td></tr><tr><td>P(ABCD) = 0.1915</td><td>P(ABCE) = 0.20968</td><td>P(ABDE) = 0.2012</td><td>P(ACDE) = 0.1915</td><td>P(BCDE) = 0.20968</td></tr><tr><td>P(ABCDE) = 0.16909</td><td></td><td></td><td></td><td></td></tr></table>

The prediction that minimizes the cost will be chosen. The cost of predicting A to be “True” is $(1-\mathrm{P}(\mathrm{A}|\mathrm{CE})) \times \mathrm{C}_{2}$ , while the cost of predicting A to be “Not True” is $\mathrm{P}(\mathrm{A}|\mathrm{CE}) \times \mathrm{C}_{1}$ . Strictly speaking, the costs of prediction are expected costs, based on the probability that A is true or false. However, we reserve the term expected cost for later use, when we find the expectation over the range of all possible values of $C_{2}$ . Therefore, when $(1-\mathrm{P}(\mathrm{A}|\mathrm{CE})) \times \mathrm{C}_{2} < \mathrm{P}(\mathrm{A}|\mathrm{CE}) \times \mathrm{C}_{1}$ , we are better off in predicting A to be “True”, otherwise we would predict A to be “Not True”. A similar analysis is performed for other possible realizations of the observed variables C and E.

![](/api/attachments/S44268F8/fulltext/images/f70362251dda8fdc301d203a9c8d24a9ac0523e4d424cc8804b7f544e69a68a6.jpg)  
Fig. 4. Decision Tree with Actual Probabilities.

![](/api/attachments/S44268F8/fulltext/images/21f27314dc60ca0921462e78ac334983893ead0b326bbc7bc71a17383b2de8d7.jpg)  
Fig. 5. Cost Curve for the Actual Distribution.

tions of the observed variables C and E.
From the above analysis we see that the decision depends on the ratio of the costs $C_{1}$ and $C_{2}$ , and not on the absolute costs. Therefore, with no loss of generality, we can set $C_{1}$ to 1 and analyze the cost for different values of $C_{2}$ . We predict A to be true when $(1-\mathrm{P}(\mathrm{A}\mid\mathrm{CE}))\times\mathrm{C}_{2}<\mathrm{P}(\mathrm{A}\mid\mathrm{CE})\times\mathrm{C}_{1}$ , or equivalently when $\mathrm{C}_{2}<\mathrm{P}(\mathrm{A}\mid\mathrm{CE})\times\mathrm{C}_{1}/(1-\mathrm{P}(\mathrm{A}\mid\mathrm{CE}))=\mathrm{P}(\mathrm{A}\mid\mathrm{CE})/(1-\mathrm{P}(\mathrm{A}\mid\mathrm{CE}))=0.766/0.234=3.273=\mathrm{Q}$ (where Q is defined as the posterior ‘odds’ for the hypothesis being true). The cost involved in making such a prediction is $(1-\mathrm{P}(\mathrm{A}\mid\mathrm{CE}))\times\mathrm{C}_{2}=0.234\times\mathrm{C}_{2}$ . When $C_{2}\geq\mathrm{P}(\mathrm{A}\mid\mathrm{CE})/(1-\mathrm{P}(\mathrm{A}\mid\mathrm{CE}))$ , we predict A to be “Not True” with a cost equal to $\mathrm{P}(\mathrm{A}\mid\mathrm{CE})=0.766$ . The cost curve as a function of $C_{2}$ is shown in Figure 5.

When an approximate distribution is used instead of the actual one, the posterior belief in A will usually be different from the actual one. For instance, when the logarithm approximation is used, the posterior probability is $P_{l}(A|CE)=P_{l}(ACE)/P_{l}(CE)=0.2325/0.31=0.75$ (these numbers are easily computed from the table shown in Appendix I). The variable A is predicted “True” when $C_{2}<Q_{l}=P_{l}(A|CE)/(1-P_{l}(A|CE))=0.75/0.25=3$ , and, “Not True” otherwise. When the decision made using the approximate distribution is the same as the decision made using the actual distribution, the cost for prediction is also the same. When the decision is different, the cost is higher for the approximate. In this example, the decision using the approximate distribution is the same as that when using the actual distribution for those values of $C_{2}$ where $C_{2} \leq 3$ or $C_{2} \geqslant 3.273$ . When $3 < C_{2} < 3.273$ , then we would predict A to be “Not True” when using the approximate distribution, which would lead to a cost equal to $P(A | CE) = 0.766$ . This is higher than the cost when using the actual distribution ( $= 0.234 \cdot C_{2}$ ).

The cost curve using the logarithm approximation is shown in Figure 6. The cost curve using the actual distribution is OBG, while that using the approximate distribution is OEAG. The triangle EAB characterizes the loss region for the approximate distribution. AB identifies the range of values for $C_{2}$ over which a loss occurs, and AE is the maximum loss that may occur when using the approximate distribution. The range AB is the difference between the correct posterior ‘odds’ Q, and the approximate one which is $Q_{l}$ . The ratio $m = 100 \times AE/ED$ is the maximum %loss when using the approximate distribution (expressed as a % of the expected cost when using the actual distribution). For this example, we have $AB = Q - Q_{l} = 3.273 - 3 = 0.273$ , and $m = 100 \times AE/ED = 100 \times ((BC/ED) - 1) = 100 \times ((Q/Q_{l}) - 1) = 9.1\%$ .

A similar analysis is performed using the quadratic solution. For that solution we have $P_{q}(A \mid CE) = P_{q}(ACE)/P_{q}(CE) = 0.24238/0.3198 = 0.758$ . Variable A will be predicted “True” when $C_{2} < P_{q}(A \mid CE)/(1 - P_{q}(A \mid CE)) = 0.758/0.242 = 3.132$ , and the decision will result in a loss when $3.132 < C_{2} < 3.273$ . In this case the range of $C_{2}$ where a loss occurs is AB = 0.141, and, m = 4.5%.

## 5.4. Consolidation of loss parameters

The above analysis is performed for decisions made after different sets of observed variables, and the results summarized. The range AB, and the maximum percentage loss m, are two parameters to compare for different approximate distributions. A third parameter we compare is the expected loss expressed as a percentage of the expected cost when using the actual distribution.

We define M, the cumulative maximum percentage loss for a given distribution, as: $M = \max\{m\}$ , over all possible sets of observed variables. Thus, M is the maximum of the m's, which is itself the maximum percentage loss for a given set of observations. Since we are going to compare the summary statistics subsequently, we use M as one measure of the goodness of an approximation. For the sake of brevity, we drop the qualifier cumulative in the rest of this section.

It is harder to consolidate the range AB, which is the interval of $C_{2}$ over which some loss is incurred when using the approximate distribution. In order to do so for different problem instances, we interpret this interval as the probability of incurring a loss when using an approximate distribution, and call it the 'Loss Probability' associated with such a distribution.

The loss interval for $C_{2}$ is translated into the “Loss Probability” in the following manner. $C_{2}$ is the ratio of the costs associated with the two types of errors (since $C_{1}$ has been fixed equal to 1). Each value of $C_{2}$ refers to that particular ratio of costs of making Type I and Type II errors respectively. Its domain is the real line [0, infinity). For instance, $C_{2}=1$ refers to all instances where $C_{1}=C_{2}$ . Similarly, $C_{2}=0.5\leftrightarrow C_{2}=0.5\cdot C_{1}$ , and $C_{2}=2\leftrightarrow C_{2}=2\cdot C_{1}$ .

![](/api/attachments/S44268F8/fulltext/images/6dcccdf03a6391dd15c51b1864ef57995ad5baf912ea78d9c4d6945d054d678f.jpg)  
Fig. 6. Cost Curve Using the Logarithm Approximation.

Consider the following two loss intervals:

$$
\begin{array}{l l} \text { Interval   1: } & [ 0. 5, 1 ] \Leftrightarrow [ C _ {2} = 0. 5 C _ {1}, C _ {2} = C _ {1} ] \\ \text { Interval   2: } & [ 1, 2 ] \Leftrightarrow [ C _ {2} = C _ {1}, C _ {2} = 2 C _ {1} ] \end{array}
$$

The range of the intervals are 0.5 and 1 for these two cases. This seems to imply that the second interval is more significant than the first. However, since the interval values reflect the ratio of two costs, it seems more appropriate that these two intervals be considered equivalent for evaluating the approximate distributions. A transformation scheme that achieves this objective by using a variable X as a surrogate for $C_{2}$ is shown below:

$$
\begin{array}{r l} X = C _ {2} & \text { when } C _ {2} \leq 1 \\ = 2 - \frac {1}{C _ {2}} & \text { when } C _ {2} > 1 \end{array}
$$

The transformation maps the values of $C_{2}$ in the interval [0, infinity) onto the interval [0, 2] for values of X, and centers the interval for X around 1, with the distance from 1 reflecting the proportionate rather than the absolute difference between the two type of costs. When using this transformation, the effective intervals for the variable X in the above two cases become [0.5, 1] and [1, 1.5] respectively, which translate to the same ranges. Another intuitively appealing feature of this transformation is that the range of X evaluated for the actual and approximate posterior probabilities $p = P(A \mid CE)$ and $p_{a} = P_{a}(A \mid CE)$ respectively, is the same as that for the posterior of the negation of event A, i.e. for $P(\sim A \mid CE)$ and $P_{a}(\sim A \mid CE)$ .

The values of X that correspond to the two endpoints of the loss interval $C_{2}=Q$ and $C_{2}=Q_{a}$ are denoted by Z and $Z_{a}$ respectively (thus, X lies in the interval between Z and $Z_{a}$ if and only if $C_{2}$ is in the interval between Q and $Q_{a}$ ). Using an approximate distribution results in a loss only when X is in $[Z, Z_{a}]$ . Therefore, the probability of incurring a loss when using an approximate distribution is given by the probability that X lies in $[Z, Z_{a}]$ . For computational convenience, we assume X to be uniformly distributed over [0, 2]. As a result, the probability of incurring a loss when an approximate distribution is used is given by $R = |Z - Za| / 2$ , which we call the 'Loss Probability'. It should be noted that the above transformation is used only to help consolidate the loss interval for different sets of observed variables. The actual loss interval is adequate for evaluating approximate representations in individual cases.

We define a third parameter L that captures both the range of C2 over which a loss occurs, as well as, the rate of loss, when using approximate solutions. L is defined as the expected loss over the entire range of X (and hence $C_{2}$ ), expressed as a percentage of the expected cost using the actual distribution, i.e.:

$$
L = \frac {\text { Expected   Cost   Using   Approximation } - \text { Expected   Cost   Using   Actual }}{\text { Expected   Cost   Using   Actual }}.
$$

The expected costs using the actual and approximate distributions are given by the areas under the cost curves for the two distributions, respectively. L is a function of Q and $Q_{a}$ , where $Q_{a}$ is the odds that the hypothesis is true when an approximate distribution is used. The expression for L is different for different ranges of values of Q and $Q_{a}$ . The different expressions are shown below, with the derivations presented in Appendix II:

Case I: Both Q and $Q_{a}$ are less than or equal to 1

$$
\mathrm{L} = \frac {\left(\mathrm{Q} _ {\mathrm{a}} - \mathrm{Q}\right) ^ {2}}{\mathrm{Q} (4 - \mathrm{Q})}
$$

Case II: Both Q and $Q_{a}$ are greater than or equal to 1

$$
\mathrm{L} = \frac {\log \frac {\mathrm{Q} _ {\mathrm{a}}}{\mathrm{Q}} + \frac {\mathrm{Q}}{\mathrm{Q} _ {\mathrm{a}}} - 1}{1 . 5 + \log \mathrm{Q}}
$$

Table 4  
Loss parameters when C and E are observed to be true

<table><tr><td></td><td>Expected Loss (L)</td><td>Loss Probability (R)</td><td>Maximum Loss (M)</td></tr><tr><td>Logarithm approximation</td><td>0.146%</td><td>0.0278</td><td>9.1%</td></tr><tr><td>Quadratic approximation</td><td>0.03%</td><td>0.0137</td><td>4.5%</td></tr></table>

Case IIIa: Q is less than 1 and $Q_{a}$ is greater than 1

$$
\mathrm{L} = \frac {1 + 2 \log \mathrm{Q} _ {\mathrm{a}} + 2 \frac {\mathrm{Q}}{\mathrm{Q} _ {\mathrm{a}}}}{\mathrm{Q} (4 - \mathrm{Q})} - 1
$$

Case IIIb: Q is greater than 1 and $Q_{a}$ is less than 1

$$
\mathrm{L} = \frac {\mathrm{Q} _ {\mathrm{a}} ^ {2} + \mathrm{Q} (4 - 2 \mathrm{Q} _ {\mathrm{a}})}{3 + 2 \log \mathrm{Q}} - 1
$$

The loss parameters, when both C and E are observed to be true, are as shown in Table 4. For this case, both Q and $Q_{a}$ are greater than 1, and therefore Case II is used to calculate L.

A similar analysis is performed for all feasible sets of observable variables. Table 5 summarizes the loss parameters for different numbers of variables observed before prediction. For the belief network used in the study, there are four observable variables B, C, D and E. Hence, the number of variables that may be observed before prediction can be 0, 1, 2, 3 or 4. Each row in Table 5 displays the loss parameters averaged over all possible realizations for each combination of a given number of variables observed. For instance, when the number of observed variables is two, there are six different combinations of variables that may be observed. For each such combination, there are four distinct realizations. Therefore, the parameters displayed in that particular row in Table 5 is an average over a total of 24 distinct realizations. Similarly, other rows in the table show the summary values of the loss parameters for all possible realizations.

## 5.5. Loss analysis for different actual distributions

The best logarithm and the quadratic solutions are compared over a large number of actual distributions. The different distributions are obtained by varying the strength of the dependency between nodes B and E, since the arc (B, E) is missing from the approximate representation (refer to Figure 3). In the actual distribution the variable E is conditioned on the two variables B and C. Therefore, different dependencies between variables B and E can be obtained by varying the parameters P(BE) and P(BCE). The values that parameters P(BE) and P(BCE) may take are constrained by the probabilities specified for the rest of the distribution. We conduct our comparison by varying the parameter P(BE) over the range [0.3, 0.5] in steps of 0.04. For each such value of P(BE), P(BCE) is varied over [0.22, 0.3] in steps of 0.02 (the parameter P(BE) has a total feasible range of [0.22,0.6]; however for values of P(BE) below 0.3, and above 0.5, the corresponding feasible range of P(BCE) is less than [0.22, 0.3]). We note that variables B and E are conditionally independent of each other with respect to C when P(BE) = 0.380417 and P(BCE) = 0.24025 (i.e. the actual distribution does not have arc BE as part of its belief network, and an exact representation is possible).

Table 5  
Consolidated loss parameters for given distribution

<table><tr><td rowspan="2"># of variables Observed</td><td colspan="2">Expected Loss (L%)</td><td colspan="2">Loss Probability (R)</td><td colspan="2">Max Loss (M%)</td></tr><tr><td>Log</td><td>Quad</td><td>Log</td><td>Quad</td><td>Log</td><td>Quad</td></tr><tr><td>0</td><td>0.000</td><td>0.006</td><td>0.0000</td><td>0.0064</td><td>0.00</td><td>1.30</td></tr><tr><td>1</td><td>0.003</td><td>0.025</td><td>0.0028</td><td>0.0088</td><td>2.29</td><td>7.16</td></tr><tr><td>2</td><td>0.107</td><td>0.109</td><td>0.0136</td><td>0.0132</td><td>31.69</td><td>37.64</td></tr><tr><td>3</td><td>0.134</td><td>0.126</td><td>0.0127</td><td>0.0121</td><td>42.04</td><td>66.31</td></tr><tr><td>4</td><td>0.000</td><td>0.003</td><td>0.0000</td><td>0.0016</td><td>0.00</td><td>1.84</td></tr><tr><td>Cum Avg</td><td>0.074</td><td>0.079</td><td>0.009</td><td>0.011</td><td>-</td><td>-</td></tr></table>

Table 6  
Loss analysis for different distributions

<table><tr><td rowspan="2">P(BE)</td><td rowspan="2">Range of P(BCE)</td><td colspan="2">Expected Loss (L%)</td><td colspan="2">Loss Probability (R)</td><td colspan="2">Max Loss (M%)</td></tr><tr><td>Log</td><td>Quad</td><td>Log</td><td>Quad</td><td>Log</td><td>Quad</td></tr><tr><td>0.3</td><td>[0.22,0.3]</td><td>1.0254</td><td>1.0376</td><td>0.0385</td><td>0.0403</td><td>134.26</td><td>186.12</td></tr><tr><td>0.34</td><td>[0.22,0.3]</td><td>0.4738</td><td>0.5044</td><td>0.0242</td><td>0.0269</td><td>88.39</td><td>143.13</td></tr><tr><td>0.38</td><td>[0.22,0.3]</td><td>0.2290</td><td>0.2466</td><td>0.0127</td><td>0.0157</td><td>67.75</td><td>126.22</td></tr><tr><td>0.42</td><td>[0.22,0.3]</td><td>0.2336</td><td>0.2340</td><td>0.0155</td><td>0.0166</td><td>68.44</td><td>112.24</td></tr><tr><td>0.46</td><td>[0.22,0.3]</td><td>0.4866</td><td>0.4398</td><td>0.0256</td><td>0.0265</td><td>76.50</td><td>108.98</td></tr><tr><td>0.5</td><td>[0.22,0.3]</td><td>1.0408</td><td>0.9010</td><td>0.0376</td><td>0.0407</td><td>115.21</td><td>140.16</td></tr></table>

![](/api/attachments/S44268F8/fulltext/images/c83445b82e6dfa57261438c1a0c3b5034149688734a7c2d41d6a5a62edefd4c7.jpg)  
Fig. 7. Expected Loss L (%) for Logarithm and Quadratic Approximation.

![](/api/attachments/S44268F8/fulltext/images/932a1c6aca341454b1186ec8e507cbbf03838039691058d52d897d0835a0012f.jpg)  
Fig. 8. Loss Probability R for Logarithm and Quadratic Approximation.

For each set of values for parameters P(BE) and P(BCE), the complete distribution is generated for the actual problem, and the best logarithm and quadratic solutions are obtained. The loss parameters are evaluated for each of the approximate solutions. The results are aggregated for different values of P(BE), and presented in Table 6. Figures 7 and 8 show the parameters L and R respectively for the approximations obtained when using the two scoring rules.

The expected loss L, when using the logarithm solution, decreases when P(BE) increases from 0.3 to 0.38, and then increases for increasing P(BE). This is to be expected since the dependence across B and E is relatively weakest when P(BE) = 0.38, and is stronger for higher and lower values of P(BE). When using the quadratic approximation, the expected loss L is lowest when P(BE) = 0.42; however it is only marginally more for P(BE) = 0.38. Overall, the expected loss functions are very similar for the two solutions. The probability of a loss, R, is lower for the logarithm solution for the entire range of P(BE) considered. However, the differences between the logarithm and quadratic solutions are relatively small. The parameter M is also lower for the logarithm approximation for the entire range of P(BE).

These results seem to indicate that, on average, the logarithm solutions perform at least as well as the quadratic solutions, if not better. However, the magnitude of the differences are quite small, and may not be significant. The quadratic solutions used are not necessarily optimal, because of the error inherent in the numerical approximation code that is used. This problem will be faced by practitioners working on real applications as well, since exact solution techniques are currently not available for problems of this nature.

A natural question that may arise is why not to use the loss function itself as a rule to determine the best approximation, i.e. an approximation that minimizes the expected loss. When exact loss functions are available for a problem domain, then it is clearly desirable to use such functions. However, such functions are often hard to obtain. Even when such functions are available, they are often too complex for meaningful analysis. For instance, obtaining the best representation while using the loss function discussed in the example in section 5 would be computationally extremely hard for large problem instances.

## 6. An example using the logarithm rule

In section 4, we have shown that the logarithm rule can be used relatively easily to obtain probability parameters for approximate representations. Further, in section 5, we show that the probability parameters obtained when using the logarithm rule perform as well as, if not better than, the parameters obtained using the quadratic rule. In this section, we use a simple example to illustrate how the logarithm rule may be used to evaluate two different approximate structures. We consider the hypothetical problem of evaluating mutual funds that was introduced in section 2. A complete network representation over the five variables could be as shown in Figure 9a. In this example, we consider approximate representations that are of order 3.

![](/api/attachments/S44268F8/fulltext/images/1730078cbb0573f72f498ccd8bb9d26f8dfe52951166081b4f1cd2a5faebe003.jpg)  
Fig. 9. Actual and Approximate Networks for the Mutual Funds Example.

The expert may provide two possible approximate network representations as shown in Figures 9b and 9c, respectively. In order to compare two approximate representations, we first need to obtain the joint distribution for the complete network, i.e. the actual distribution, either from an expert, or, estimated from historical data if available. This is because any valid measure evaluates an approximate distribution by measuring its distance from the actual. If the logarithm rule is used, obtaining the joint distribution for a given topology is easy. This is because, when using the logarithm rule, the conditional probability distribution associated with each variable in the approximation is preserved. For example, given the structure in Approximation I, the best approximate distribution for the variable Volatility, conditioned on the two variables Yield and PE Ratio, is equal to the corresponding actual (which is obtained either from the expert, or estimated from data). Similarly, the best approximate distribution for the variable Proj Growth, conditioned on the two variables Fund Type and PE Ratio, is equal to the actual distribution for the variable Proj Growth, conditioned on the two variables Fund Type and PE Ratio, etc. Hence, once the conditional distribution associated with each variable is obtained for a structure, the complete joint distribution can be computed by multiplying the component distributions in accordance with the product-form of that structure. The logarithm measure is then evaluated for the two approximate distributions with respect to the actual distribution (as discussed in section 4.1), and the network with a higher score is selected.

We note that approximate representations often miss dependencies that exist in the problem domain. For instance, the complete network shown in Figure 9a indicates that Volatility is directly dependent on Fund Type, which is not captured in either of the approximate representations considered. When Approximation I is used in practice, the variable Volatility will affect Fund Type; however, it will do so indirectly through the variables Yield and PE Ratio. On the other hand, by ignoring this direct dependency (as well as some others shown in Figure 9a), belief updates can be made using the structure in Approximation I far more efficiently than when using the complete network. In summary, accuracy in belief representation is traded off for computational convenience.

## 7. Conclusions

In this paper we have examined different criteria that may be used to evaluate belief networks. Desirable properties of measures that may be used are discussed, and proper scoring rules are shown to be appropriate. There are many scoring rules that are proper; however the logarithm and the quadratic rule have been shown to have some additional features that make them very attractive. These two rules were closely examined in the context of evaluating different belief networks, and obtaining optimal representations. The logarithm rule was shown to have very good modeling features, in that it can be implemented relatively easily, as compared to the quadratic rule. We performed extensive experimentation that compared the solutions obtained using the logarithm rule and the quadratic rule, respectively, using a decision theoretic approach. The solutions obtained when using the logarithm rule were found to be at least as good as the solutions obtained using the quadratic rule. This research clearly suggests that the logarithm rule is very appropriate for evaluating belief networks.

We have also discussed some commonly used measures that are equivalent to using the logarithm rule, viz. the I-Divergence measure and the maximum likelihood criteria. Another criterion

that has been considered for evaluating alternate networks is the entropy function [16]. Assuming that the conditional probabilities associated with each component of the product-form distribution is as estimated from data, they develop an algorithm that obtains a network with minimum entropy. While there are some obvious similarities in the functional form of the entropy function and the logarithm rule, the best solution obtained by these two approaches are not necessarily the same [30]. Using the logarithm rule (or any of the other equivalent criteria) is more appropriate than the minimum entropy approach as suggested in [16], since no additional assumptions are required regarding the probability parameters associated with different components of the approximate distribution.

## Appendix

Appendix 1: Logarithm and quadratic solutions for the distribution in Table 3

Table 7  
Logarithm and quadratic solutions for distribution in Table 3

<table><tr><td></td><td>ACTUAL</td><td>LOG APPROX</td><td>QUAD APPROX</td></tr><tr><td>ABCDE</td><td>0.16909</td><td>0.15625</td><td>0.16890</td></tr><tr><td>ABCD ~ E</td><td>0.02240</td><td>0.03125</td><td>0.02588</td></tr><tr><td>ABC ~ DE</td><td>0.04058</td><td>0.03750</td><td>0.04128</td></tr><tr><td>ABC ~ D ~ E</td><td>0.01792</td><td>0.02500</td><td>0.02090</td></tr><tr><td>AB ~ CDE</td><td>0.03210</td><td>0.03750</td><td>0.04039</td></tr><tr><td>AB ~ CD ~ E</td><td>0.01418</td><td>0.01250</td><td>0.01289</td></tr><tr><td>AB ~ C ~ DE</td><td>0.02996</td><td>0.03500</td><td>0.03772</td></tr><tr><td>AB ~ C ~ D ~ E</td><td>0.07375</td><td>0.06500</td><td>0.06585</td></tr><tr><td>A ~ BCDE</td><td>0.02240</td><td>0.03125</td><td>0.02588</td></tr><tr><td>A ~ BCD ~ E</td><td>0.01235</td><td>0.00625</td><td>0.00396</td></tr><tr><td>A ~ BC ~ DE</td><td>0.00538</td><td>0.00750</td><td>0.00632</td></tr><tr><td>A ~ BC ~ D ~ E</td><td>0.00988</td><td>0.00500</td><td>0.00320</td></tr><tr><td>A ~ B ~ CDE</td><td>0.01418</td><td>0.01250</td><td>0.01289</td></tr><tr><td>A ~ B ~ CD ~ E</td><td>0.00364</td><td>0.00417</td><td>0.00411</td></tr><tr><td>A ~ B ~ C ~ DE</td><td>0.01324</td><td>0.01167</td><td>0.01204</td></tr><tr><td>A ~ B ~ C ~ D ~ E</td><td>0.01894</td><td>0.02167</td><td>0.02102</td></tr><tr><td>~ ABCDE</td><td>0.04058</td><td>0.03750</td><td>0.04128</td></tr><tr><td>~ ABCD ~ E</td><td>0.00538</td><td>0.00750</td><td>0.00632</td></tr><tr><td>~ ABC ~ DE</td><td>0.00974</td><td>0.00900</td><td>0.01009</td></tr><tr><td>~ ABC ~ D ~ E</td><td>0.00430</td><td>0.00600</td><td>0.00511</td></tr><tr><td>~ AB ~ CDE</td><td>0.02996</td><td>0.03500</td><td>0.03772</td></tr><tr><td>~ AB ~ CD ~ E</td><td>0.01324</td><td>0.01167</td><td>0.01204</td></tr><tr><td>~ AB ~ C ~ DE</td><td>0.02797</td><td>0.03267</td><td>0.03522</td></tr><tr><td>~ AB ~ C ~ D ~ E</td><td>0.06883</td><td>0.06067</td><td>0.06149</td></tr><tr><td>~ A ~ BCDE</td><td>0.01792</td><td>0.02500</td><td>0.02090</td></tr><tr><td>~ A ~ BCD ~ E</td><td>0.00988</td><td>0.00500</td><td>0.00320</td></tr><tr><td>~ A ~ BC ~ DE</td><td>0.00430</td><td>0.00600</td><td>0.00511</td></tr><tr><td>~ A ~ BC ~ D ~ E</td><td>0.00790</td><td>0.00400</td><td>0.00259</td></tr><tr><td>~ A ~ B ~ CDE</td><td>0.07375</td><td>0.06500</td><td>0.06585</td></tr><tr><td>~ A ~ B ~ CD ~ E</td><td>0.01894</td><td>0.02167</td><td>0.02102</td></tr><tr><td>~ A ~ B ~ C ~ DE</td><td>0.06883</td><td>0.06067</td><td>0.06149</td></tr><tr><td>~ A ~ B ~ C ~ D ~ E</td><td>0.09848</td><td>0.11267</td><td>0.10735</td></tr></table>

Appendix II: Expected loss when using approximate distributions

The loss parameter L for an approximate distribution is defined as:

$$
L = \frac {\text { Expected   Cost   Using   Approximation } - \text { Expected   Cost   Using   Actual }}{\text { Expected   Cost   Using   Actual }}
$$

The cost curves for the actual and approximate distributions are plotted as a function of X (which is a transformation of $C_{2}$ ). The expected cost for the actual and approximate distributions are obtained by finding the area under these cost curves. For the actual representation, the cost of prediction, K(p), is:

$K(p) = \text{Min}\left\{(1 - p) \times C_2, p\right\},$ where $p$ is the posterior probability that event $A$ is true when using the actual representation

i.e.

$$
\mathrm{K} (\mathrm{p}) = \left\{ \begin{array}{l l} (1 - \mathrm{p}) \times \mathrm{C} _ {2} & \text { when } \mathrm{C} _ {2} \leq \frac {\mathrm{p}}{(1 - \mathrm{p})} = \mathrm{Q} \\ \mathrm{p} & \text { when } \mathrm{C} _ {2} > \mathrm{Q} \end{array} \right.
$$

For approximate representations, $p_{a}$ is the evaluated posterior probability that A is true. Thus:

$$
\mathrm{K} \left(\mathrm{p} _ {\mathrm{a}}\right) = \left\{ \begin{array}{l} (1 - \mathrm{p}) \times \mathrm{C} _ {2} \\ \text {when} \mathrm{C} _ {2} \leq \frac {\mathrm{p} _ {\mathrm{a}}}{(1 - \mathrm{p} _ {\mathrm{a}})} = \mathrm{Q} _ {\mathrm{a}} \\ \mathrm{p} \\ \text {when} \mathrm{C} _ {2} > \mathrm{Q} _ {\mathrm{a}} \end{array} \right.
$$

X is a transformation of $C_{2}$ , defined as follows:

$$
\mathrm{X} = \left\{ \begin{array}{l l} \mathrm{C} _ {2} & \text {when} \mathrm{C} _ {2} \leq 1 \\ 2 - \frac {1}{\mathrm{C} _ {2}} & \text {when} \mathrm{C} _ {2} > 1 \end{array} \right.
$$

The cost K is expressed as a function of X, and, the expected costs and corresponding losses evaluated for the different cases considered below.

Case Ia: $\mathbf{Q} \leq \mathbf{Q}_{\mathrm{a}} \leq 1$

The cost curves are expressed as a function of $C_{2}$ and X respectively, and shown in Figure 10. We have:

$$
\mathrm{K} (\mathrm{p}) = \left\{ \begin{array}{l} (1 - \mathrm{p}) \times \mathrm{C} _ {2} = (1 - \mathrm{p}) \times \mathrm{X} \\ \text {when X\leq\frac{p}{(1 - p)} = Q} \\ \mathrm{p} \\ \text {when X > Q} \end{array} \right.
$$

The expected cost $EK(p)$ is given by:

$$
\begin{array}{l} \mathrm{EK(p)} \\ = \int_ {[ 0, Q ]} (1 - p). X. f (X) d X + \int_ {[ Q, 2 ]} p. f (X) d X \end{array}
$$

X is assumed to be uniformly distributed over [0,2]. Therefore:

$$
\begin{array}{r l} \mathrm{EK(p)} & = \frac {(1 - p)}{2} \int_ {[ 0, Q ]} X d X + \frac {p}{2} \int_ {[ Q, 2 ]} d X \\ & = \frac {(1 - p)}{4} Q ^ {2} + \frac {p}{2} (2 - Q) \end{array}
$$

![](/api/attachments/S44268F8/fulltext/images/62a39036c6c10f951c4630c8ceb1228817e5085eeed43ca47607d10392492cf0.jpg)

![](/api/attachments/S44268F8/fulltext/images/d0e3245adf066490b82cc7e9fe6d9a427b1bf3cae27dd91c519449ca5062ebee.jpg)  
Fig. 10. Cost curves for Actual and Approximate Distributions when $Q \leq Q_{a} \leq 1$ .

![](/api/attachments/S44268F8/fulltext/images/2da7570baf9d0c5ffe8f5ee0f64ae771f94ac5cd74c1d1c57009cc9674c45bf2.jpg)  
Fig. 11. Cost curves for Actual and Approximate Distributions when $Q_{a} \leq Q \leq 1$ .

Similarly, the expected cost when using an approximate representation is:

$$
\begin{array}{r l} & \mathrm {EK(p_ {a})} \\ & = \int_ {[ 0, \mathrm{Qa} ]} (1 - p) \cdot \mathrm{X.f(X)} \mathrm{dX} + \int_ {[ \mathrm{Qa}, 2 ]} p. f (\mathrm{X}) \mathrm{dX} \\ & = \frac {(1 - p)}{4} Q _ {\mathrm{a}} ^ {2} + \frac {p}{2} (2 - Q _ {\mathrm{a}}) \end{array}
$$

Therefore, we have:

$$
\begin{array}{r l} \mathrm{L} & = \frac {\mathrm{EK} (\mathrm{p} _ {\mathrm{a}}) - \mathrm{EK} (\mathrm{p})}{\mathrm{EK} (\mathrm{p})} \\ & = \frac {\frac {(1 - \mathrm{p})}{4} \left(\mathrm{Q} _ {\mathrm{a}} ^ {2} - \mathrm{Q} ^ {2}\right) + \frac {\mathrm{p}}{2} (\mathrm{Q} - \mathrm{Q} _ {\mathrm{a}})}{\frac {(1 - \mathrm{p})}{4} \mathrm{Q} ^ {2} + \frac {\mathrm{p}}{2} (2 - \mathrm{Q})} \\ & = \frac {(1 - \mathrm{p}) \left(\mathrm{Q} _ {\mathrm{a}} ^ {2} - \mathrm{Q} ^ {2}\right) + 2 \mathrm{p} (\mathrm{Q} - \mathrm{Q} _ {\mathrm{a}})}{(1 - \mathrm{p}) \mathrm{Q} ^ {2} + 2 \mathrm{p} (2 - \mathrm{Q})} \end{array}
$$

$$
\begin{array}{r l} & = \frac {(1 - p) (Q _ {a} ^ {2} - Q ^ {2}) + 2 (1 - p) Q ^ {2} - 2 (1 - p) Q Q _ {a}}{(1 - p) Q ^ {2} + 2 p (2 - Q)} \\ & = \frac {(1 - p) (Q _ {a} - Q) ^ {2}}{(1 - p) Q ^ {2} + 2 p (2 - Q)} \\ & = \frac {(Q _ {a} - Q) ^ {2}}{Q ^ {2} + 2 Q (2 - Q)} = \frac {(Q _ {a} - Q) ^ {2}}{Q (4 - Q)} \end{array}
$$

Case Ib: $\mathrm{Q_a}\leq \mathrm{Q}\leq 1$

The expressions for expected costs using the approximate and actual representations are identical to Case Ia, and therefore so is L. The cost curves are shown in Figure 11. Case IIa: $Q \geqslant Q_{a} \geqslant 1$

Since both Q and $Q_{a}$ are $\geqslant1$ , the cost expressed as a function of the transformation X is different from the cost expressed as a function of $C_{2}$ . The values of X that correspond to $C_{2}=Q$ and $C_{2}=Q_{a}$ are denoted by Z and $Z_{a}$ respectively (e.g. $Z = 2 - 1 / Q$ ; etc). The cost curves are shown in Figure 12. Here,

![](/api/attachments/S44268F8/fulltext/images/20dd9e37e9e005083e0cbcfa981fb662694faa2b373ec09b135f7c2d2956336f.jpg)

![](/api/attachments/S44268F8/fulltext/images/ba1c73ce211eb894c8ad2a26b42a7a72332ce74859551b6dfbbe5604ccd8c9b1.jpg)  
Fig. 12. Cost curves for Actual and Approximate Distributions when $Q \geqslant Q_{a} \geqslant 1$ .

$$
\begin{array}{r l} \mathrm{K(p)} & = (1 - \mathrm{p}) \times \mathrm{C} _ {2} = (1 - \mathrm{p}) \times \mathrm{X} \\ & \text {when X\leq 1} \\ & = (1 - \mathrm{p}) \times \mathrm{C} _ {2} = (1 - \mathrm{p}) \times \frac {1}{2 - \mathrm{X}} \\ & \text {when 1 <   X\leq Z} \\ & = \mathrm{p} \\ & \text {when X > Z} \end{array}
$$

The expected cost $E K(p)$ is given by:

EK(p)

$$
\begin{array}{r l} & = \int_ {[ 0, 1 ]} (1 - p) \cdot X. f (X) d X \\ & \quad + \int_ {[ 1, Z ]} \frac {1 - p}{2 - X}. f (X) d X + \int_ {[ Z, 2 ]} p. f (X) d X \\ & = \frac {1 - p}{4} + \frac {1 - p}{2} \log \frac {1}{2 - Z} + \frac {p}{2} (2 - Z) \\ & = \frac {1 - p}{4} + \frac {1 - p}{2} \log Q + \frac {p}{2 Q} \end{array}
$$

Similarly,

$$
\begin{array}{r l} \mathrm{EK} (\mathrm{p} _ {\mathrm{a}}) & = \int_ {[ 0, 1 ]} (1 - \mathrm{p}). \mathrm{X}. \mathrm{f} (\mathrm{X}) \mathrm{dX} \\ & + \int_ {[ 1, \mathrm{Za} ]} \frac {1 - \mathrm{p}}{2 - \mathrm{X}}. \mathrm{f} (\mathrm{X}) \mathrm{dX} \\ & + \int_ {[ \mathrm{Za}, 2 ]} \mathrm{p}. \mathrm{f} (\mathrm{X}) \mathrm{dX} \\ & = \frac {1 - \mathrm{p}}{4} + \frac {1 - \mathrm{p}}{2} \log \mathrm{Q} _ {\mathrm{a}} + \frac {\mathrm{p}}{2 \mathrm{Q} _ {\mathrm{a}}} \\ & \mathrm{L} = \frac {\mathrm{EK} (\mathrm{p} _ {\mathrm{a}}) - \mathrm{EK} (\mathrm{p})}{\mathrm{EK} (\mathrm{p})} \\ & = \frac {\frac {1 - \mathrm{p}}{4} + \frac {1 - \mathrm{p}}{2} \log \mathrm{Q} _ {\mathrm{a}} + \frac {\mathrm{p}}{2 \mathrm{Q} _ {\mathrm{a}}} - \frac {1 - \mathrm{p}}{4} - \frac {1 - \mathrm{p}}{2} \log \mathrm{Q} - \frac {\mathrm{p}}{2 \mathrm{Q}}}{\frac {1 - \mathrm{p}}{4} + \frac {1 - \mathrm{p}}{2} \log \mathrm{Q} + \frac {\mathrm{p}}{2 \mathrm{Q}}} \\ & = \frac {\frac {1 - \mathrm{p}}{2} \log \frac {\mathrm{Q} _ {\mathrm{a}}}{\mathrm{Q}} + \frac {\mathrm{p}}{2 \mathrm{Q}} \left(\frac {\mathrm{Q}}{\mathrm{Q} _ {\mathrm{a}}} - 1\right)}{\frac {1 - \mathrm{p}}{4} + \frac {1 - \mathrm{p}}{2} \log \mathrm{Q} + \frac {\mathrm{p}}{2 \mathrm{Q}}} \end{array}
$$

$$
\begin{array}{l} = \frac {\frac {1 - p}{2} \log \frac {Q _ {a}}{Q} + \frac {1 - p}{2} \left(\frac {Q}{Q _ {a}} - 1\right)}{\frac {1 - p}{4} + \frac {1 - p}{2} \log Q + \frac {1 - p}{2}} \\ = \frac {\log \frac {Q _ {a}}{Q} + \frac {Q}{Q _ {a}} - 1}{1 . 5 + \log Q} \end{array}
$$

Case IIb: $\mathrm{Q_a\geqslant Q\geqslant 1}$

The analysis for this case is identical to that for Case IIa, and so is the expression for L.

Case IIIa: $\mathrm{Q} < 1$ and $\mathrm{Q}_{\mathrm{a}} > 1$

The expected cost when using the actual distribution is identical to Case Ia, while the expected cost when using the approximate distribution is identical to that for Case IIa. Therefore,

$$
\begin{array}{r l} \mathrm{L} & = \frac {\frac {1 - \mathrm{p}}{4} + \frac {1 - \mathrm{p}}{2} \log \mathrm{Q} _ {\mathrm{a}} + \frac {\mathrm{p}}{2 \mathrm{Q} _ {\mathrm{a}}}}{\frac {(1 - \mathrm{p})}{4} \mathrm{Q} ^ {2} + \frac {\mathrm{p}}{2} (2 - \mathrm{Q})} - 1 \\ & = \frac {1 + 2 \log \mathrm{Q} _ {\mathrm{a}} + 2 \frac {\mathrm{Q}}{\mathrm{Q} _ {\mathrm{a}}}}{\mathrm{Q} (4 - \mathrm{Q})} - 1 \end{array}
$$

Case IIIa: $\mathrm{Q} > 1$ and $\mathrm{Q}_{\mathrm{a}} < 1$

Here, the expected cost when using the actual distribution is identical to Case IIa, while the expected cost when using the approximate distribution is identical to that for Case Ia.

$$
\begin{array}{r l} \mathrm{L} & = \frac {\frac {(1 - p)}{4} Q _ {a} ^ {2} + \frac {p}{2} (2 - Q _ {a})}{\frac {1 - p}{4} + \frac {1 - p}{2} \log Q + \frac {p}{2 Q}} - 1 \\ & = \frac {Q _ {a} ^ {2} + Q (4 - 2 Q _ {a})}{3 + 2 \log Q} - 1 \end{array}
$$

## References

[1] A.M. Agogino and A. Rege, "IDES: Influence Diagram Based Expert System," Mathematical Modelling, Volume 8, pp. 227-233, 1987.

[2] I.A. Beinlich, H.J. Suermondt, R.M. Chavez and G.F. Cooper, "The ALARM Monitoring System: A Case Study with Two Probabilistic Inference Techniques for Belief Networks," Proceedings of the Conference on Artificial Intelligence in Medical Care, pp. 247–256, 1989.

[3] G.W. Brier, “Verification of Forecasts Expressed in Terms of Probability,” Monthly Weather Review, Volume 78, no. 1, pp. 1–3, January 1958.

[4] R.M. Chavez and G.F. Cooper, "An Empirical Evaluation of a Randomized Algorithm for Probabilistic Inference," in Uncertainty in Artificial Intelligence 5, M. Henrion, R.D. Shachter, L. Kanal and J.F. Lemmer (eds.), North Holland, Amsterdam, pp. 191-208, 1990.

[5] P. Cheeseman, “A Method of Computing Generalized Bayesian Probability Values for Expert Systems,” Proceedings of the 8th International Joint Conference on Artificial Intelligence, vol. 1, Karlsruhe, West Germany, 1983.

[6] C.K. Chow and C.N. Liu, "Approximating Discrete Probability Distributions with Dependence Trees," IEEE Transactions on Information Theory, vol. IT-14, no. 3, pp. 462–467, May 1968.

[7] G.F. Cooper, "NESTOR: A Computer-Based Medical Diagnostic Aid that Integrates Causal and Probabilistic Knowledge," Ph.D. Dissertation, Stanford University, Stanford, CA, 1984.

[8] G.F. Cooper, "The Computational Complexity of Probabilistic Inference Using Bayesian Belief Networks," Artificial Intelligence, vol. 42, pp. 393-405, 1990.

[9] G.F. Cooper and E. Herskovitz, "A Bayesian Method for Constructing Bayesian Belief Networks from Databases," Proceedings from the 7th Annual Conference on Uncertainty in Artificial Intelligence, pp. 86–94, 1991.

[10] R.O. Duda, P.E. Hart, K. Konolige and R. Reboh(1979), "A Computer-Based Consultant for Mineral Exploration," Final Report, SRI Projects 6415, SRI International, Menlo Park, California, September 1979.

[11] R. Fung and K. Chang, "Weighing and Integrating Evidence for Stochastic Simulation in Bayesian Networks," in Uncertainly in Artificial Intelligence 5, M. Henrion, R.D. Shachter, L. Kanal and J.F. Lemmer (eds.), North Holland, Amsterdam, pp. 209-220, 1990.

[12] D. Geiger, "An Entropy-Based Learning Algorithm of Bayesian Conditional Trees," Uncertainty in Artificial Intelligence: Proceedings of the Eighth Conference, D. Dubois, M.P. Wellman, B. D'Ambrosio and P. Smets (eds.), pp. 92–97, 1992.

[13] I.J. Good, “Rational Decisions,” Journal of the Royal Statistical Society, Ser. B, Vol. 14, pp. 107–114, 1952.

[14] D.E. Heckerman, E.J. Horvitz and B.N. Nathwani, "Update on the Pathfinder Project," Proceedings of the Symposium on Computer Applications in Medical Care, pp. 203-207, 1989.

[15] M. Henrion, “Propagating Uncertainty in Bayesian Networks by Probabilistic Logic Sampling,” in Uncertainty in Artificial Intelligence 2, J.F. Lemmer and L. Kanal (eds.), North Holland, Amsterdam, pp. 149–164, 1988.

[16] E. Herskovitz and G.F. Cooper, “Kutato: An Entropy-Driven System for Construction of Probabilistic Expert Systems from Databases,” Uncertainty in Artificial Intelligence 6, P.P. Bonnisone, M. Henrion, L.N. Kanal and J.F. Lemmer (eds.), North Holland, Amsterdam, pp. 117–125, 1991.

[17] D. Kazakos and T. Cotsidas, "A Decision Theory Approach to the Approximation of Discrete Probability Densities," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. PAMI-2, no. 1, pp. 61–67, January 198.

[18] S. Kullback, Information Theory and Statistics, Wiley: New York, 1959.

[19] S.L. Lauritzen and D.J. Spiegelhalter, “Local Computation with Probabilities in Graphical Structures and Their Applications to Expert Systems,” Journal of the Royal Statistical Society B, vol. 50, no. 2, pp. 157–224, 1988.

[20] J. Marschak, “Remarks on the Economics of Information,” In The Contributions to Scientific Research in Management, Los Angeles: University of California, 1959.

[21] J. McCarthy, “Measures of the Value of Information,” Proceedings of the National Academy of Sciences, pp. 654–655, 1956.

[22] R.E. Neapolitan, Probabilistic Reasoning in Expert Systems: Theory and Algorithms, John Wiley and Sons, Inc., NY, 1990.

[23] J. Pearl, “Reverend Bayes on Inference Engines: A Distributed Hierarchical Approach,” Proceedings of the National Conference in AI, Pittsburg, pp. 133–36, 1982.

[24] J. Pearl, “Fusion, Propagation, and Structuring in Belief Networks,” Artificial Intelligence, vol. 29, pp. 241–288, 1986.

[25] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufman, San Mateo, California, 1988.

[26] J.R. Quinlan, “Induction of Decision Trees,” Machine Learning, Vol. 1 (1), pp. 81–106, 1986.

[27] G. Rebane, and J. Pearl, "The Recovery of Causal Polytrees from Statistical Data," Proceedings of the 3rd Workshop on Uncertainty in AI, Seattle, pp. 222-228, 1987.

[28] T.B. Roby, “Belief States and the Uses of Evidence,” Behavioral Science, vol. 10, pp. 255–270, 1965.

[29] S. Sarkar, "Using Tree Structures to Approximate Belief Networks in Expert Systems," Proceedings of the Second Annual Workshop on Information Technologies and Systems, V.C. Storey and A.B. Whinston (eds.), pp. 235-244, 1992.

[30] S. Sarkar and I. Murthy, "Some Theoretical Results in Obtaining Approximate Representations for Belief Networks," Working Paper, Louisiana State University, Baton Rouge, 1993.

[31] L.J. Savage, “Elicitation of Personal Probabilities and Expectations,” Journal of the American Statistical Association, vol. 66, no. 336, December 1971.

[32] K. Schittkowski, “Nonlinear Programming Codes,” Lecture Notes in Economics and Mathematical Systems, 183, Springer-Verlag, Berlin, Germany, 1980.

[33] K. Schittkowski, “On the Convergence of a Sequential Quadratic Programming Method with an Augmented Lagrangian Line Search Function,” Mathematik Operationsforschung und Statistik, Serie Optimization, 14, pp. 197–216, 1983.

[34] M.J. Shaw, “Applying Inductive Learning to Enhance Knowledge-Based Expert Systems,” Decision Support Systems, vol. 3, pp. 319–332, 1987.

[35] R.D. Shachter and M. Peot, “Simulation Approaches to General Probabilistic Inference on Belief Networks,” in Uncertainty in Artificial Intelligence 5, M. Henrion, R.D. Shachter, L. Kanal and J.F. Lemmer (eds.), North Holland, Amsterdam, pp. 221–231, 1990.

[36] E.H. Shuford, A. Albert, and H.E. Massengill, "Admissible Probability Measurement Procedures," Psychometrika, 31, pp. 125-145, 1966.

[37] P. Smyth and R.M. Goodman, "An Information Theoretic Approach to Rule Induction from Databases," IEEE Transactions on Knowledge and Data Engineering, vol. 4, no. 4, pp. 301–316, 1992.

[38] P. Spirtes, C. Glymour and R. Scheines, Causation. Prediction, and Search, Springer-Verlag Lecture Notes in Statistics, New York, 1993.

[39] S. Srinivas, S. Russell and A. Agogino, "Automated Construction of Sparse Bayesian Networks from Unstructured Probabilistic Models and Domain Information," Uncertainty in Artificial Intelligence 5, North-Holland, pp. 295–308, 1990.

[40] C.-A.S. Stael von Holstein, “Assessment and Evaluation of Subjective Probability Distributions,” The Economic Research Institute at the Stockholm School of Economics, Stockholm, 1970.

[41] J. Stoer, “Principles of Sequential Quadratic Programming Methods for Solving Nonlinear Programs,” Computational Mathematical Programming, Edited by K. Schittkowski, NATO ASI Series, 15, Springer-Verlag, Berlin, Germany, 1985.

[42] H.J. Suermondt and M.D. Amylon, "Probabilistic Prediction of the Outcome of Bone-Marrow Transplantation,"

Proceedings of the Symposium on Computer Applications in Medical Care, pp. 208–212, 1989.

[43] R. Uthurusamy, U.M. Fayyad and S. Spangler, "Learning Useful Rules from Inconclusive Data," Knowledge Discovery in Databases, G. Piatetsky-Shapiro and W.J. Frawley (eds.), pp. 141-157, 1991.

[44] A.K.C. Wong and C.C. Wang., "Classification of Discrete Biomedical Data with Error Probability Minimax," Proceedings of the Seventh International Conference of the Cybernetics Society, Washington, DC, pp. 19-21, 1977.

[45] S.K.M. Wong and F.C.S. Poon, “Comments on Approximating Discrete Probability Distributions with Dependence Trees,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 11, no. 3, pp. 333–335, March 1989.

![](/api/attachments/S44268F8/fulltext/images/7f93241a301fc1be08680e14287fbba4666fbc6c96f6067bc2bbe624405116d9.jpg)

Sumit Sarkar is currently Assistant Professor of Management Information Systems at the College of Business at Louisiana State University. He received his Ph.D. in Computers and Information Systems from the University of Rochester. His current research interests are in the areas of expert systems, databases and the economics of information systems. He is a member of ACM and TIMS.

![](/api/attachments/S44268F8/fulltext/images/21d686c57a30e67126096f040825602bd2e1912886f2922625bfa4a0b4079351.jpg)

Ishwar Murthy is Associate Professor in the Department of Quantitative Business Analysis at Louisiana State University, Baton Rouge. He received his Ph.D Degree in Management Science from Texas A & M University. His current research interests are in Network Optimization, Multiobjective Optimization and Mathematical Programming Applications in Telecommunications.
