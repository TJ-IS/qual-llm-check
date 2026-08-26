---
otero_id: 17528
otero_key: "JZF35MRM"
title: "Probabilistic inference and path analysis"
authors: "Stephen F. Roehrig"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00056-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Probabilistic inference and path analysis

Stephen F. Roehrig

Heinz School of Public Policy and Management, Carnegie Mellon University Pittsburgh, PA 15213-3890, USA

## Abstract

Discussions of network-based probabilistic techniques in artificial intelligence often mention path analysis as an ideological precursor, but the fundamental connections between the two paradigms have not been explored. This paper details an analogy between the two, and shows that a number of computational results in the AI/expert system literature are directly obtainable from path analysis.

Keywords: Probabilistic networks; Path analysis; Artificial intelligence

## 1. Introduction

A number of papers and books on network-based probabilistic methods mention another inference paradigm using graphs. The superficial resemblance of path analysis to Bayesian networks [9], influence diagrams [10], probabilistic similarity networks [6], and other variations on their common theme is obvious to anyone familiar with causal modeling in economics and the social sciences. Path analysis and related structural equation modeling techniques have existed for some time, but the parallels between these “statistical” methods and the “probabilistic” ones that are increasingly familiar to workers in AI have not been fully examined.

This paper shows that path analysis can be interpreted and applied as a probabilistic inference technique, comparing favorably with many of the methods currently in use. In addition, because the stochastic relationships between propositions in path diagrams are stored as correlations instead of the more familiar conditional probabilities, it is possible in some circumstances to employ the methods of Glymour, et al. [5] to test the validity of the network representation itself.

We begin with a brief review of path analysis and define some causal modeling terminology. Next, probabilistic networks are considered, especially the conditional independence relations worked out by Pearl [9]. Then, in Section 4, the connections between these two network-based representational frameworks are developed. With the intersection of path analysis and probabilistic networks thus established, two further sections explain how probability propagation can be realized in singly connected path diagrams, first for “top-down” propagation (which is the norm in expert systems applications) and then for general probabilistic inference.

## 2. Path analysis

Path analysis was developed by the geneticist Sewall Wright as a means of investigating the ramifications of various causal models in population genetics [12,13]. A number of sizable examples of its use may be found in [1]. It is based on regression, using a system of equations that follows directly from the proposed causal model and some linearity assumptions.

Qualitatively, path analysis imposes two structural requirements. The first is that a (weak) causal order be placed on the variables in the path model. This requirement enables the construction of a path diagram, which is a network that links the variables (nodes) with directed arcs. The second requirement is that the proposed model be causally closed. The idea here is that all relevant causes must be included in the analysis. If the investigator feels that there may be some unmeasured variables which are causally related, these can be collected in an auxiliary variable of “unidentified causes,” but it must be further assumed that these unnamed causes are uncorrelated with those explicitly included.

Quantitatively, path analysis assumes that variables connected by arcs in the diagram are linearly related. However, as in all regression, the linearity is really in the coefficients of the regression equation; nothing prevents the incorporation of additional variables which are, for example, multiplicative composites of the “real” variables. When path analysis is related to probabilistic inference, much use of this fact will be made.

A simple example will illustrate the basic ideas. Suppose we have data consisting of measurements of three related variables x, y, and z, and we believe that x and y are causes of z. To satisfy the requirement of causal closure, any and all other factors causally connected with z are subsumed by another variable, say u. In addition, there may or may not be a correlation between x and y, but provision is made for correlation in the path diagram.

When the raw data are standardized to have zero sample mean and unit sample variance (such variables are denoted by upper case letters), the appropriate normal equations are

$$
p _ {1} \Sigma X ^ {2} + p _ {2} \Sigma X Y = \Sigma X Z,
$$

$$
p _ {1} \Sigma X Y + p _ {2} \Sigma Y ^ {2} = \Sigma Y Z.\tag{1}
$$

![](/api/attachments/JZF35MRM/fulltext/images/245fff65eabc79363572b8ebe61b685596f8c7d60fdb6d964af3db4a51ec2697.jpg)  
Fig. 1. Path diagram with coefficients.

After solving these, the completed path diagram, with path coefficients attached looks like Fig. 1.

Returning to the normal Eqs. (1) it can be seen that because the variables are standardized, dividing through by $n^{2}$ results in

$$
p _ {1} + p _ {2} r _ {x y} = r _ {x z},
$$

$$
p _ {1} r _ {x y} + p _ {2} = r _ {y z}.\tag{2}
$$

This version of the equations for the path coefficients shows that the correlations between a variable and its predecessors in the path diagram are the primary data in the path model. They serve a function similar to that of conditional probabilities in probabilistic networks.

## 2.1. Interpretation of the path diagram

Predicted values for the variable z are obtained by standardizing given values of x and y, substituting into the regression equation (using the path coefficients), and converting back to an unstandardized result. But what if only, say, x is known? It turns out that the path diagram summarizes all the information needed to recover the regression of Z onto X alone.

For a reduced diagram consisting of a single causal variable, for example $X \rightarrow Z$ , the contribution of Y is subsumed. The path coefficient for this simplified diagram is $r_{xz}$ , and we can write $r_{xz} = p_{1} + p_{2} r_{xy}$ ,

as in the first of Eqs. 2. This corresponds (graphically) to navigating two routes from X to Z, one direct and one by means of the correlation $r_{xy}$ . This ability to immediately construct a reduced diagram is a very useful feature, which we call “collapsing.” A given diagram automatically contains the complete analysis for any subgraph of the original diagram. The rules for manipulating path diagrams imply that in the absence of knowledge of a particular predictor variable, it may be collapsed into the remaining diagram. The effect is to take a collapsed variable at the value that other, known, variables predict for it, either through direct arcs or correlations or both.

## 2.2. Treks

The idea of collapsing a node into the diagram, as illustrated above, is directly related to the notion of a trek. A trek between two nodes A and B is defined to be either (1) a direct path between them, in either direction and possibly through intermediate nodes, or (2) a pair of paths from a third node C, such that one path is directed from C to A and the other from C to B. Either or both of these component paths may have intermediate nodes.

It turns out [7] that the correlation between any two variables in a path diagram can be determined by considering all treks between them. For each trek, one simply multiplies together the path coefficient on each arc, and sums these products over all the treks. The result is the required correlation.

As an example, consider the path diagram of Fig. 2. The treks connecting Y and Z are

(1) $Y \to Z$ ,

(2) $Z \leftarrow X \rightarrow Y$ , and

(3) $Z \leftarrow X \leftarrow W \rightarrow Y$ .

The correlation between $Y$ and $Z$ is thus

$$
r _ {y z} = p _ {y z} + p _ {x z} p _ {x y} + p _ {x z} p _ {w x} p _ {w y}.
$$

More complicated graphs can contain much larger numbers of treks between any pair of variables. Glymour, et al. [5] have proposed an efficient algorithm for finding them.

$$
\begin{array}{c c c} W & \xrightarrow {p _ {w y}} & Y \\ & p _ {w x} \Bigg \downarrow & \Bigg \downarrow p _ {x y} \\ X & \xrightarrow {p _ {x z}} & Z \end{array}
$$

Fig. 2. A more complicated path diagram.  
![](/api/attachments/JZF35MRM/fulltext/images/29dadc64c30b1737a1f88d2cbc9f066cdd0c261ae5d2dc7372b16d3ff9f513bb.jpg)  
Fig. 3. A simple network.

## 3. Probabilistic networks

The term probabilistic network is a generic one, and various species of this class go by the names Bayesian network, influence diagram, independence network, and random Markov field. A very large example of the use of probabilistic networks is described in [6], and several other fields where they are used are discussed in [3]. The function of the network is to encode conditional dependences between random variables represented by the nodes. Directed arcs indicate direct dependence, and are attributed with conditional probabilities. In the present discussion, as in virtually all previous treatments of probabilistic networks, the random variables depicted by the nodes are allowed to take on only a finite number of values.

Common to all probabilistic networks is the idea that the specification of a relatively small number of marginal and conditional probabilities is sufficient to completely describe a joint distribution over all the variables. A network is fully specified when (1) each node with no incoming arcs is given a marginal probability, and (2) each node with an arc or arcs entering is described by a set of conditional probabilities, the conditioning being done over the node's immediate predecessors. Under the assumption that all relevant “causal factors” or “influences” have been faithfully denoted by arcs, the joint distribution can be obtained as a special factorization of the given information.

As an example, consider the network in Fig. 3. Since it has no predecessors, node a is quantified with the marginal $\Pr(a)$ . The probabilities of the remaining nodes can be determined by $\Pr(a)$ and the conditionals $\Pr(b|a)$ , $\Pr(c|a)$ , $\Pr(d|b,c)$ and $\Pr(e|d)$ .

One way that the joint distribution $\Pr(a,b,c,d,e)$ can be factored is

$$
\begin{array}{c} \operatorname * {P r} (a, b, c, d, e) = \operatorname * {P r} (a) \operatorname * {P r} (b | a) \operatorname * {P r} (c | a, b) \\ \times \operatorname * {P r} (d | a, b, c) \operatorname * {P r} (e | a, b, c, d). \end{array}
$$

But because of the critical assumption that the network records all direct causal factors, the factorization above can be simplified to

$$
\begin{array}{l} \operatorname * {P r} (a, b, c, d, e) \\ = \operatorname * {P r} (a) \operatorname * {P r} (b | a) \operatorname * {P r} (c | a) \operatorname * {P r} (d | b, c) \operatorname * {P r} (e | d), \end{array}
$$

which contains only local relationships. In practice, the developers of the network (perhaps a domain expert and a “knowledge engineer”) need only evaluate probabilities conditioned on immediate predecessors. The coherence of the resulting distribution (although not necessarily its accuracy) is thus guaranteed.

A probabilistic network represents a static, a priori picture of the domain of interest. In the absence of additional information, probabilistic dependence between a pair of variables is indicated by a trek joining them. However, if we are given information about the values of some of the variables, the dependence situation changes. Using concepts developed by Pearl [9] and others, it is possible to determine if one variable is dependent on another, given definite knowledge about the states of other variables. Typically, a probabilistic network is used to determine the effects of incoming evidence, so this situation is common. We denote by E the so-called “evidence set,” that is, the set of variables whose values we have somehow come to know.

The dependence rule given here follows Charniak [3], and again considers paths between nodes. It distinguishes between three types of nodes: linear, converging and diverging. For example, node b in Fig. 3 is linear, having one predecessor and one successor. Similarly, node a is diverging, since it has more than one successor, and node d is converging by virtue of its multiple predecessors. In the definition which follows, a node is classified as one of these three types in the context of the path under consideration; arcs not contained in the path in question are ignored.

The dependence rule says that a variable x is dependent on a variable y given evidence E (which cannot contain either x or y) if there is a d-connecting path from x to y given E. A path from x to y is d-connecting given E if every interior node n in the path has the property that either

(1) it is linear or diverging and not a member of $E$ or

(2) it is converging, and either $n$ or one of its descendants is in $E$ .

When the set E is empty, this new definition reduces to the one involving treks given previously. Indeed, if $E = \varnothing$ , part 2 of the rule cannot come into play. From part 1, any directed path constitutes a d-connecting path. Also, if there exists a node z in the path, such that there is a directed path from z to x and also one from z to y (i.e., a trek), then all nodes in this path are either linear or diverging (the unique diverging node being z). Thus part 1 applies. Note, however, that a d-connecting path can be no more complicated than this without evidence nodes. If there were two (or more) diverging nodes in the path, then it can be seen that at least one converging node would also have to be incorporated. But this is prohibited, since converging nodes are not allowed unless there is evidence to “enable” them. (This intuitive argument can be made rigorous by introducing the notion of a topological ordering on the nodes.)

To illustrate the definition, consider Fig. 3 again. Notice that b and c are dependent, because of the d-connecting path (trek) $b \leftarrow a \rightarrow c$ connecting them. Suppose we learn the state of node a, so that $E = \{a\}$ . Part 1 of the rule for d-connecting paths no longer applies, since now conditioning on b tells us nothing new about c - knowledge of b cannot influence belief in c because a is “fixed.” In addition, b and c cannot be d-connected through d, since neither d nor its descendant e are in E. Thus knowledge of a renders b and c conditionally independent.

What if the states of both a and e become known? In this case, the trek $b \leftarrow a \rightarrow c$ is still blocked by a, but now the evidence node e tells us something about d, which in turn can give us information about the relationship between b and c. So now b and c are dependent again; specifically we have

$$
\operatorname * {P r} (c | a, e, b) \neq \operatorname * {P r} (c | a, e).
$$

There is considerable value in structuring a problem domain in terms of a probabilistic network. But generally, one wishes to assess the impact of evidence. For this, a calculus of probability propagation is required. Work in this area has been done by Pearl [9], Lauritzen and Spiegelhalter [8], Shachter [10], and others. Cooper [4] has shown that the general inference problem on acyclic graphs is NP-hard. Later in this paper a new propagation calculus is described.

## 4. Path analysis and probability

To this point, a number of similarities between path analysis and probabilistic networks have been described. Both theories are used to posit causal structure, both use networks to encode local relationships, and both follow the same rules for detecting global dependencies. But their respective areas of application have traditionally been quite different. Probabilistic networks have been used as a knowledge representation and reasoning framework. Path analysis has been used as a means of understanding causal relationships and as a prediction tool. It is possible, however, to think of the representation and reasoning applications of probabilistic networks in another light. Given the information encoded in a probabilistic network, the inference procedures which take place when new evidence becomes available might be thought of as predicting the new belief state of a reasoner whose thought processes obey the laws of probability. When viewed this way, it seems worthwhile to examine how the predictive mechanisms of the two methods compare.

The case we treat is the special one in which all the network nodes represent propositions, which may only be true or false. The slightly more complex situation where nodes have a finite set of outcomes can often be reduced to a larger collection of true-false propositions, but the conversion process is not covered here. Each node has a variable associated with it, which records the truth or falsehood of the proposition represented by the node. If 1.0 stands for true, and 0.0 for false, then values in the interior of this interval represent some degree of belief in the truth of the proposition. We will see that this measure is actually a probability.

## 4.1. A single causal variable

Beginning with the simplest case, consider two variables x and y. We take the data which describe x, y, and the relationship between them to be a series of observations; individual observations simply record the verity of each variable. In general, the situation can be summarized by

$$
\begin{array}{l} x = 0, y = 0 \text {occurred} n _ {1} \text {times}, \\ x = 0, y = 1 \text {occurred} n _ {2} \text {times}, \\ x = 1, y = 0 \text {occurred} n _ {3} \text {times}, \\ x = 1, y = 1 \text {occurred} n _ {4} \text {times}, \end{array}
$$

with the total number of observations being $n \equiv n_{1} + n_{2} + n_{3} + n_{4}$ . Assuming that x is a cause of y, the two-node path diagram is that of Fig. 4.

Given the above data, x is true $(n_{3} + n_{4})/n$ of the time. Thus

$$
\hat {\mu} _ {x} = \frac {n _ {3} + n _ {4}}{n} \hat {\sigma} _ {x} = \sqrt {\hat {\mu} _ {x} (1 - \hat {\mu} _ {x})},
$$

because x is Bernoulli. Using uppercase X to represent the standardized version of x, and recalling that the standardization process is

$$
X = \frac {x - \hat {\mu} _ {x}}{\hat {\sigma} _ {x}},
$$

we find that

$$
x \in [ 0, 1 ] \mapsto X \in \left[ - \sqrt {\hat {\mu} / (1 - \hat {\mu})}, \sqrt {(1 - \hat {\mu}) / \hat {\mu}} \right],
$$

where the subscripts are dropped for simplicity.

Now it is possible to see what path analysis “predicts” for the variable y given some “belief”

$$
X \xrightarrow {p} Y.
$$

Fig. 4. A simple two-node diagram.

in x. First of all, the path coefficient p in the path diagram above is

$$
p = \frac {\sum_ {1} ^ {n} X Y}{n} = \dots = \frac {n _ {1} n _ {4} - n _ {2} n _ {3}}{n \hat {\sigma} _ {x} \cdot n \hat {\sigma} _ {y}}.
$$

Suppose now that x = 1, that is that the proposition associated with the variable x is found to be true. Path analysis will then predict some value for y. The procedure is to standardize x = 1.0, multiply by p, and unstandardize the result at y. A little algebra shows that the result is $y = n_{4}/(n_{3} + n_{4})$ , which is precisely the probability $\Pr(y|x)$ , as computed from the frequencies given above.

In the probabilistic framework, having partial belief in x - knowing it only with some probability b, say - also gives rise to a definite belief in y. We simply imagine some new event $x'$ , which when known with certainty prompts the given belief in x: $\Pr(x|x') = b$ . Then

$$
\begin{array}{r l} \operatorname * {P r} (y | \operatorname * {P r} (x) = b) & = \operatorname * {P r} (y | x) \operatorname * {P r} (x | x ^ {\prime}) \\ & + \operatorname * {P r} (y | \neg x) \operatorname * {P r} (\neg x | x ^ {\prime}). \end{array}
$$

In the path analytic framework, the obvious thing to do is to assign the probability b to the variable x: x = b. Then standardizing and multiplying by the path coefficient, as before, will result in some predicted value for Y. Unstandardizing this to y will be the prediction for y given the belief b for x. Pursuing this line,

$$
y = p \left(\frac {b - \hat {\mu} _ {x}}{\hat {\sigma} _ {x}}\right) \hat {\sigma} _ {y} + \hat {\mu} _ {y}.
$$

Substituting expressions involving the $n_{i}$ into the above yields, after some algebra

$$
\begin{array}{r l} & y = \frac {b n _ {1} n _ {4} - b n _ {2} n _ {3} + n _ {2} n _ {3} + n _ {2} n _ {4}}{(n _ {1} + n _ {2}) (n _ {3} + n _ {4})} \\ & \quad = b \left(\frac {n _ {4}}{n _ {3} + n _ {4}}\right) + (1 - b) \left(\frac {n _ {2}}{n _ {1} + n _ {2}}\right) \\ & \quad = b \operatorname * {P r} (y | x) + (1 - b) \operatorname * {P r} (y | \neg x) \\ & \quad = \operatorname * {P r} (y | x) \operatorname * {P r} (x | x ^ {\prime}) + \operatorname * {P r} (y | \neg x) \operatorname * {P r} (\neg x | x ^ {\prime}) \\ & \quad = \operatorname * {P r} (y | x ^ {\prime}). \end{array}
$$

That is, the prediction (by means of regression) of path analysis is in agreement with that of probability theory. In fact, the slope of the unstandardized regression line is given by

$$
s = \operatorname * {P r} (y | x) - \operatorname * {P r} (y | \neg x).
$$

Standardization scales x and y by $\hat{\sigma}_{x}$ and $\hat{\sigma}_{y}$ respectively, so that the slope of the standardized regression line (which in this case is also the sample correlation $r_{xy}$ ) is just

$$
p = r _ {x y} = \left(\operatorname * {P r} (y | x) - \operatorname * {P r} (y | \neg x)\right) \frac {\hat {\sigma} _ {x}}{\hat {\sigma} _ {y}}.\tag{3}
$$

Previously it was pointed out that when a node (such as y in the preceding section) has only a single arc entering, the path coefficient is equivalent to the correlation between the two variables. So for the elementary case treated above, we have $p = r_{xy}$ . Now, the correlation between two variables is a symmetric relationship, so the path coefficient is sufficient information (and in the proper form) to find the probability of x given some knowledge of y. In this sense, Bayes rule is “built-in” to the representation. It is possible to take advantage of this fact in probabilistic inference over larger portions of a graph.

## 4.2. Multiple causes

When two or more variables $x_{1}, x_{2}, \ldots$ act as causes of a variable y, the relationship between path analysis and probability is somewhat more complicated. The basic problem is that linearity assumptions of path analysis appear initially to be at odds with the way probability theory combines evidence. In general, this difficulty can be overcome by the addition of derived variables. For example, consider the case of two causes $x_{1}$ and $x_{2}$ , and the diagram of Fig. 5.

By the rules for reading probabilistic networks, $x_{1}$ and $x_{2}$ are independent. (This fact remains true when the graph of Fig. 5 is embedded in a larger graph, provided the larger graph is singly connected.) We have

![](/api/attachments/JZF35MRM/fulltext/images/130b1eba1c02adeb43cbca5876be61dff8d0488d8296629558e90c09daca91b7.jpg)  
Fig. 5. Two causes and a single effect.

$$
\begin{array}{l} P r (y) = \operatorname * {P r} (y | x _ {1}, x _ {2}) \operatorname * {P r} (x _ {1}) \operatorname * {P r} (x _ {2}) \\ \qquad + \operatorname * {P r} (y | \neg x _ {1}, x _ {2}) \operatorname * {P r} (\neg x _ {1}) \operatorname * {P r} (x _ {2}) \\ \qquad + \operatorname * {P r} (y | x _ {1}, \neg x _ {2}) \operatorname * {P r} (x _ {1}) \operatorname * {P r} (\neg x _ {2}) \\ \qquad + \operatorname * {P r} (y | \neg x _ {1}, \neg x _ {2}) \operatorname * {P r} (\neg x _ {1}) \operatorname * {P r} (\neg x _ {2}). \end{array}\tag{4}
$$

Eq. 4 shows that the values of $x_{1}$ and $x_{2}$ must be combined nonlinearly to arrive at the correct probability for y. Therefore, a nonlinear term, the product $x_{1}x_{2}$ , is added to the path diagram and regression equations. This term is standardized in the usual way. (The data required for this process will be considered shortly.) Postulating a regression equation of the form

$$
Y = p _ {1} X _ {1} + p _ {2} X _ {2} + p _ {1 2} X _ {1} X _ {2},
$$

it turns out that the path coefficients can be written as follows.

$$
\begin{array}{l} p _ {1} = \left(\operatorname * {P r} (y | x _ {1}, \neg x _ {2}) - \operatorname * {P r} (y | \neg x _ {1}, \neg x _ {2})\right) \frac {\hat {\sigma} _ {x _ {1}}}{\hat {\sigma} _ {y}}, \\ p _ {2} = \left(\operatorname * {P r} (y | \neg x _ {1}, x _ {2}) - \operatorname * {P r} (y | \neg x _ {1}, \neg x _ {2})\right) \frac {\hat {\sigma} _ {x _ {2}}}{\sigma_ {y}}, \\ p _ {1 2} = \left(\operatorname * {P r} (y | x _ {1}, x _ {2}) - \operatorname * {P r} (y | \neg x _ {1}, x _ {2}) \right. \\ \left. - \operatorname * {P r} (y | \neg x _ {1}, x _ {2}) + \operatorname * {P r} (y | \neg x _ {1}, \neg x _ {2})\right) \frac {\hat {\sigma} _ {x _ {1 2}}}{\hat {\sigma} _ {y}}. \end{array}\tag{5}
$$

Extension to the case of three or more causes is straightforward.

The product term may or may not be necessary. Examination of the equation for $p_{12}$ shows that this term will vanish when

$$
\begin{array}{r l} & {\operatorname * {P r} \big (y | x _ {1}, x _ {2} \big) - \operatorname * {P r} \big (y | \neg x _ {1}, x _ {2} \big)} \\ & {\qquad = \operatorname * {P r} \big (y | \neg x _ {1}, x _ {2} \big) - \operatorname * {P r} \big (y | \neg x _ {1}, \neg x _ {2} \big).} \end{array}\tag{6}
$$

This amounts to saying that the incremental influence of, say $x_{1}$ , is independent of the probability of $x_{2}$ . (This reasoning can be symmetrically applied to $x_{1}$ and $x_{2}$ in the reverse order.) This is a new independence relation, which neither implies nor is implied by the independence of $x_{1}$ and $x_{2}$ .

Many expert systems in business applications have used the “certainty factors” model of uncertainty management $[2]$ . In such systems, although the formulae for evidence combination are nonlinear, they do not take into account the product nonlinearity which is obvious in the probabilistically correct formulation given above. Thus a large class of commonly occurring situations simply cannot be modeled. In any context where two or more pieces of evidence individually increase (resp. decrease) belief in a consequent, but their appearance collectively decreases (resp. increases) that belief, certainty factors and similar schemes fall short. While the exact formulation for evidence combination in the certainty factors model is not purely linear, an assumption quite similar to that of Eq. 6 is inherently made.

The linearity expressed in Eq. 6 is also quite different from the “noisy OR-gate” sometimes used in probabilistic networks to simplify probability assessment [9]. In fact, the noisy OR is very much a non-linear combination scheme, in which the product term plays a prominent role.

## 4.3. Data requirements

It is clear from the relations between path coefficients and conditional probabilities displayed above that eliciting conditionals is sufficient to fully specify the path diagram. However, since path analysis typically uses correlations as the basic quanta, it is worthwhile to consider exactly which correlations are needed to complete the diagram. Again considering the case of two causes (but observing that generalization is possible), the following facts further relate the two methods.

First of all, because of the implied independence of $x_{1}$ and $x_{2}$ in Fig. 5, the correlation $r_{x_{1}x_{2}}$ is zero. (This isn't necessarily the case in a multiply connected graph, but we postpone for now the complications arising from multiple paths.) Also, it is true in general that

$$
r _ {x _ {1} x _ {2}} = \frac {\Sigma \left(x _ {1} - \hat {\mu} _ {x _ {1}}\right) \left(x _ {2} - \hat {\mu} _ {x _ {2}}\right)}{\sqrt {\Sigma \left(x _ {1} - \hat {\mu} _ {x _ {1}}\right) ^ {2}} \sqrt {\Sigma \left(x _ {2} - \hat {\mu} _ {x _ {2}}\right) ^ {2}}},
$$

which may be rearranged as

$$
\hat {\mu} _ {x _ {1 2}} = \hat {\sigma} _ {x _ {1}} \hat {\sigma} _ {x _ {2}} r _ {x _ {1} x _ {2}} + \hat {\mu} _ {x _ {1}} \hat {\mu} _ {x _ {2}},\tag{7}
$$

so we can determine the mean of the product term given the means of $x_{1}$ and $x_{2}$ and the correlation between them.

Similarly, $r_{x_1,x_{12}}$ can be expanded as

$$
r _ {x _ {1}, x _ {1 2}} = \frac {\left(1 - \hat {\mu} _ {x _ {1}}\right) \hat {\mu} _ {x _ {1 2}}}{\hat {\sigma} _ {x _ {1}} \sigma_ {x _ {1 2}}},\tag{8}
$$

and likewise for $r_{x_2,x_{12}}$ .

Finally, the correlation $r_{y,x_{12}}$ is

$$
\begin{array}{l} r _ {y, x _ {1 2}} = \frac {\Sigma (x _ {1 2} - \hat {\mu} _ {x _ {1 2}}) (y - \hat {\mu} _ {y})}{\sqrt {\Sigma (x _ {1 2} - \hat {\mu} _ {x _ {1 2}}) ^ {2}} \sqrt {\Sigma (y - \hat {\mu} _ {y}) ^ {2}}}, \\ \vdots \\ = \frac {\hat {\mu} _ {x _ {1} x _ {2} y} - \hat {\mu} _ {x _ {1} x _ {2}} \hat {\mu} _ {y}}{\hat {\sigma} _ {y} \sigma_ {x _ {1 2}}}, \end{array}\tag{9}
$$

where we have assumed knowledge of $\hat{\mu}_{x_1x_2y}$ .

How do path analysis and the conditional probability approach compare? Table 1 summarizes the data requirements for both methods, for the case just considered involving two causes and one effect. The table does not imply any direct correspondence between elements in any particular row (except for the first two).

The last row in the table contains, at least for path analysis, the correlation between $x_{1}$ and $x_{2}$ . Once again, under the assumption of independence between these two variables, this will be zero. If the two are dependent, then path analysis will use the correlation as a measure of this dependence. The appropriate term (or terms) for the conditional probability approach, under a dependence assumption, cannot be specified a priori, since such dependence must come from the influence of variables 'earlier' in the graph. That is, Fig. 5 is really not the whole story.

Comparison of data requirements

<table><tr><td>Path analysis</td><td>Cond. prob.</td></tr><tr><td> $\hat{\mu}_{x_1}$ </td><td> $\Pr(x_1)$ </td></tr><tr><td> $\hat{\mu}_{x_2}$ </td><td> $\Pr(x_2)$ </td></tr><tr><td> $\hat{\mu}_y$ </td><td> $\Pr(y|x_1, x_2)$ </td></tr><tr><td> $\hat{\mu}_{x_2x_2y}$ </td><td> $\Pr(y|x_1, \neg x_2)$ </td></tr><tr><td> $r_{x_1y}$ </td><td> $\Pr(y|\neg x_1, x_2)$ </td></tr><tr><td> $r_{x_2y}$ </td><td> $\Pr(y|\neg x_1, \neg x_2)$ </td></tr><tr><td> $r_{x_1x_2}$ </td><td>?</td></tr></table>

The situation for three or more causes and one effect follows the same general pattern. Assuming n independent causes and one effect, means for all possible variables formed as products of $x_{1},\ldots,x_{n}$ , z (with each term appearing only once) will be required. However, those consisting of more than one $x_{i}$ , but not involving z are derivable using relationships similar to those shown earlier. This leaves $2^{n}$ means. Coupled with the n correlations

$$
r _ {x _ {i}, z,} i = 1, \dots , n,
$$

the path analysis approach requires $2^{n} + n$ values. Conditional probability approaches require the same number; $2^{n}$ conditional probabilities.

$$
\operatorname * {P r} \left(z \mid x _ {1} = i _ {1},..., x _ {n} = i _ {n}\right), i _ {i},..., i _ {n} \in \{0, 1 \},
$$

and $n$ marginal probabilities for the $x_{i}$ .

It needs to be emphasized that these figures are for the special case where the cause variables are exogenous. In general, patterns like the ones considered here – that is, several causes and one effect, may appear anywhere in a larger network. The statements and formulae above hold whenever there are no common antecedents to the causes under consideration. When such antecedents do exist, they will form a loop, and it is no longer always possible to consider the causes (here called $x_{1}$ , $x_{2}$ and so forth) to be independent.

## 5. Top-down propagation in singly connected graphs

Singly connected graphs have special properties that make the propagation of probabilities along them fairly straightforward. Consider the generic singly connected graph in Fig. 6. If evidence is made available at top-level nodes, and if the graph will be used to infer new probabilities of interior or bottom-level nodes, then path analysis provides an easy means of performing the propagation. In fact, once the path diagram is fully specified, the process is quite similar to the certainty factors model, except the results are in keeping with the laws of probability.

Table 2  
![](/api/attachments/JZF35MRM/fulltext/images/477bbb30072870c8d3d0727737895f2fd05aa8bb83d601fad4a99200efde89aa.jpg)  
Fig. 6. A generic single connected graph.

Suppose that evidence regarding the truth or falsehood (or even the probabilities) of the propositions in some subset E of top-level nodes is obtained. In Fig. 6, this amounts to knowledge about $E \subseteq \{0, 1, 2\}$ . For each node in E, the variable associated with that node is instantiated with the appropriate number between 0 and 1, and then each of these variables is standardized. The standardization will in general be different at each node, since each variable may have a different mean value.

If there are top-level nodes for which no information is available, their standardized values are taken to be zero. This amounts to assuming them to be at their mean values. This procedure works because all the top-level nodes are uncorrelated. It is also possible to think of this situation in terms of the collapsing mechanism discussed earlier. If a node for which no evidence is available were to be collapsed into the remainder of the graph, path coefficients on the arcs connecting the remaining top-level nodes to the interior would be modified by accumulating the influence due to the removed node. But since the correlations are all zero, no change in the graph would result, other than the pruning of the uninstantiated node and the arc or arcs which lead into the remainder of the diagram.

With a standardized value obtained for each top-level node, propagation proceeds by multiplying each node value by path coefficients and summing at the next lower node in the graph. If the actual probabilities associated with interior nodes are of interest, these values may be unstandardized. At nodes where multiplicative terms are incorporated, the procedure is as follows. Each standardized variable associated with an individual (nonmultiplicative) proposition is temporarily unstandardized, and then the appropriate products formed. It is these products which are transformed according to the mean and variance of the product variable. Once all variables are standardized, multiplication by path coefficients and summation continues.

![](/api/attachments/JZF35MRM/fulltext/images/bd47a22c2c50545b3e9f8aeb7c60ac8de84d687bd921354a7e2677ac3974d049.jpg)  
Fig. 7. An example graph.

## 5.1. An example

To illustrate the procedures discussed above, we work through an example in some detail. The graph for this example as shown in Fig. 7. While simple in structure, it contains all the features of a general singly connected graph.

The quantification of the graph can be done in either of two ways: with marginal and conditional probabilities, or with means and correlations. In order to relate the path analytic method to probabilistic networks, which may be more familiar, we start with conditionals and illustrate how they are mapped over to correlations. For this example, we will use the data in Table 2.

It is straightforward, using the conditional probabilities, to work through the diagram from the top, calculating the mean of each variable. These, along with standard deviations and the ranges of each standardized variable are shown in Table 3. The column headed “min” records the minimum value of the standardized variable (which corresponds to the probability 0.0), while “max” gives the maximum (probability 1.0). Note that the results for the product variable ab were obtained from Eq. 7.

<table><tr><td colspan="2">Conditionals for the example</td></tr><tr><td>Pr(a) = 1/4</td><td>Pr(b) = 1/8</td></tr><tr><td>Pr(c|a) = 1/2</td><td>Pr(c|¬a) = 1/4</td></tr><tr><td>Pr(d|a,b) = 7/8</td><td>Pr(d|a, ¬b) = 3/4</td></tr><tr><td>Pr(d|¬a,b) = 7/8</td><td>Pr(d|¬a, ¬b) = 3/8</td></tr><tr><td>Pr(e|d) = 3/4</td><td>Pr(e|¬d) = 1/4</td></tr></table>

Table 3  
Standardization data

<table><tr><td>Var</td><td>μ</td><td>σ</td><td>min</td><td>max</td></tr><tr><td>a</td><td>0.250</td><td>0.433</td><td>-0.577</td><td>1.732</td></tr><tr><td>b</td><td>0.125</td><td>0.331</td><td>-0.378</td><td>2.646</td></tr><tr><td>c</td><td>0.313</td><td>0.464</td><td>-0.674</td><td>1.483</td></tr><tr><td>d</td><td>0.520</td><td>0.499</td><td>-1.040</td><td>0.962</td></tr><tr><td>e</td><td>0.510</td><td>0.500</td><td>-1.020</td><td>0.981</td></tr><tr><td>ab</td><td>0.031</td><td>0.174</td><td>-0.180</td><td>5.568</td></tr></table>

From these, the path coefficients can be calculated, using Eqs. 3 and 5. For example, the coefficient on the arc from A to D is given by

$$
\left(\operatorname * {P r} (d | a, \neg b) - \operatorname * {P r} (d | \neg a, \neg b)\right) \frac {\hat {\sigma} _ {a}}{\hat {\sigma} _ {d}} = . 3 2 5.
$$

The completed path diagram is shown in Fig. 8. Note the curved arcs joining A with AB and AB with B. These represent correlation unexplained by straightline arcs, and are used to recover the correlations $r_{ad}$ and $r_{bd}$ . For instance, $r_{ad}$ consists of the path coefficient $p_{ad}$ (0.325) plus the effects of the indirect path from A, along the curved arc to AB, and then down the direct arc from AB to D. Thus

$$
r _ {a d} = 0. 3 2 5 + (0. 3 1 1) (- 0. 1 3 1) = 0. 2 8 4.
$$

For future reference, Table 4 gives a complete set of correlations between the variables. Note that many of these are derived, in that they are not part of the initial specification. Data gathering is done on the local level, but the correlation between any pair of variables, however distant in the graph, can be computed by considering the treks between them.

![](/api/attachments/JZF35MRM/fulltext/images/9de7acd346ed7a9d6dba0a0f8fab1e29eb192544f82f2a937933c8d2a422c1af.jpg)  
Fig. 8. The completed path diagram.

Table 4  
Correlations among all variables

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>AB</td></tr><tr><td>A</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td>0.0</td><td>1.0</td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td>0.234</td><td>0.0</td><td>1.0</td><td></td><td></td><td></td></tr><tr><td>D</td><td>0.284</td><td>0.269</td><td>0.066</td><td>1.0</td><td></td><td></td></tr><tr><td>E</td><td>0.142</td><td>0.134</td><td>0.033</td><td>0.5</td><td>1.0</td><td></td></tr><tr><td>AB</td><td>0.311</td><td>0.475</td><td>0.073</td><td>0.128</td><td>0.064</td><td>1.0</td></tr></table>

Now suppose it is learned that a and b are both true. To determine the resulting probabilities of the remaining variables, the procedure described earlier is followed. Specifically, we set A = 1.732 B = 2.646.

Since the product $ab = (1.0)(1.0) = 1.0$ , the standardized value is AB = 5.568. Entering the path diagram with these values, we find

$$
\begin{array}{r l} D & = (1. 7 3 2) (. 3 2 5) + (5. 5 6 8) (-. 1 3 1) \\ & + (2. 6 4 6) (. 3 3 1) = . 7 0 9 3, \end{array}
$$

which, when unstandardized, yields d = 7/8 (within roundoff error), as expected. Passing the value of D downward, we get

$$
E = (. 7 0 9 3) (. 5) = . 3 5 4 7 \mapsto c = . 6 8 7 5.
$$

Similarly, $C = (1.732)(.234) = .4053$ , so $c = .5$ .

## 6. Probabilistic inference on singly connected graphs

There may be instances in which top-down propagation is sufficient for a particular application of probabilistic networks. In other circumstances, however, the ability to specify evidence at arbitrary nodes and determine its effect on any other node is quite useful. The correlational framework of path analysis makes this feasible and efficient. In this section we show how this is done on singly connected graphs.

![](/api/attachments/JZF35MRM/fulltext/images/1567702d25fa297c402dba6f3130816b4fef12f7833917021c654cf0cc099ffc.jpg)  
Fig. 9. A diagram with reversed arcs.

The basic idea is that a fully specified path diagram implicitly contains the correlation between any two variables. With this in mind, consider first a single evidence node y, and some other node x for which the impact of the evidence needs to be determined. That is, we wish to find $\Pr(x|y)$ . The simplest way to do this would be to create a new, much simplified path diagram $y \rightarrow x$ , complete with path coefficient $p_{yx}$ . As we have seen, the path coefficient in such a diagram is no more than the simple correlation between x and y, which we just said is implicitly available. This observation in fact solves the inference problem.

For example, in Fig. 8 suppose the evidence node is e and we wish to compute $\Pr(a|e)$ . The table of correlations can be consulted for $r_{ae}$ , or it may be computed directly. The treks joining a and e are the paths $a \rightarrow d \rightarrow e$ and $a \cap ab \rightarrow d \rightarrow e$ . By summing over products of coefficients on the component arcs, we find

$$
\begin{array}{r l} r _ {a e} & = p _ {a d} p _ {d e} + r _ {a, a b} p _ {a b, d} p _ {d e} \\ & = (. 3 2 5) (. 5) + (. 3 1 1) (-. 1 3 1) (. 5) = . 1 4 2. \end{array}
$$

Finally, $\Pr(a|e)$ is found by standardizing e=1, multiplying by $r_{ae}(=p_{ae})$ and unstandardizing at A. The result is $\Pr(a|e)=.31$ .

For large evidence sets, the process is slightly more complex. It is possible that product terms may have to be considered. However, all the necessary information is recorded in the path diagram, and the equations used to obtain the product terms and their correlations have already been presented. As an example, suppose that the evidence set $E = \{c, e\}$ and we wish to know the impact on node a. Again, a path diagram like that in Fig. 9 would make the task trivial.

![](/api/attachments/JZF35MRM/fulltext/images/5dcd7cc01742181f3f8a5aa4b57f65331cdab736f4d01011c4af17159061ac66.jpg)  
Fig. 10. Graph fragment for multiple evidence nodes.

![](/api/attachments/JZF35MRM/fulltext/images/a5da17536b20d2a2967e7bb645ef9c6aa8ce29463a5ec46deeb32352c27aa4b3.jpg)  
Fig. 11. Final graph linking A, C, and E.

To find path coefficients for this graph, the required data are the means $\mu_{a}$ , $\mu_{c}$ , $\mu_{e}$ , and $\mu_{ce}$ , and the correlations $r_{ca}$ , $r_{ea}$ , $r_{ce}$ , $r_{c,ce}$ , $r_{e,ce}$ and $r_{ce,a}$ . The first three means are already available, and $\mu_{ce}$ is readily computed from Eq. 7. Likewise, the first three correlations are either already available or easily computed, and $r_{ce,a}$ , $r_{c,ce}$ fall out from Eq. 8. This leaves $r_{ce,a}$ .

Because the original graph is singly connected, and we are only interested in the connection between A, C, and E, we can make use of the graph fragment in Fig. 10. The path coefficients are the correlations between a and c, and between a and e. From this graph, the joint probability of the three variables is read off as

$$
\operatorname * {P r} (a, c, e) = \operatorname * {P r} (a) \operatorname * {P r} (c | a) \operatorname * {P r} (e | a).
$$

Pr(a) is known, and the remaining RHS terms are obtained directly from the correlations. (For example, setting a = 1, standardizing and multiplying by $r_{ae}$ and unstandardizing at e yields $\Pr(e|a)$ .) This process gives $\mu_{ace}$ , and Eq. 9 produces $r_{a,ce}$ . Thus all the terms for the path analysis regression have been found. The regression itself amounts to solving a set of 3 linear equations in 3 unknowns. To obtain $\Pr(a|c,e)$ , one sets c = 1, e = 1, standardizes, and multiplies by the path coefficients. Unstandardizing at a gives the final result. The final graph linking A, C, and E is shown in Fig. 11.

## 7. Conclusions

This paper has drawn an analogy between path analysis and the network-based probabilistic inference methods currently popular in artificial intelligence. The analogy is not perfect – path analysis is a linear technique, while probability theory is not. However, incorporating derived nonlinear terms in the regressions (still linear in the coefficients) enables path analysis to duplicate the way probability theory combines evidence.

From this observation, and from other parts of the analogy regarding the way dependencies are represented in the two types of networks, it is possible to develop a straightforward evidence propagation scheme. The technique was presented in the context of singly connected graphs, but some extensions to the multiply connected case are possible.

The connection between path analysis and probabilistic networks might serve as a means to draw the social science community into closer contact with computer science and information systems groups working on knowledge representation and refinement. There has been considerable research on just how one might deduce the “correct” causal model, given a body of data or opinion. If probabilistic networks are judged to be a convenient framework for a given problem, the analogy to path analysis provides a means of bidirectional translation between the two groups.

## References

[1] Blalock, Hubert M., Jr., ed., Causal Models in the Social Sciences, 2nd ed., Aldine de Gruyter, Hawthorne, New York, 1985.

[2] B.G. Buchanan and E.H. Shortliffe, Eds., Rule-Based

Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project (Addison-Wesley, Reading MA, 1984).

[3] E. Charniak, Bayesian Networks Without Tears, Al Magazine (Winter 1991).

[4] G.F. Cooper, The Computational Complexity of Probabilistic Inference Using Bayesian Networks, Artificial Intelligence 42 (1990).

[5] C. Glymour, R. Scheines, P. Spirtes and K. Kelly, Discovering Causal Structure: Artificial Intelligence, Philosophy of Science, and Statistical Modeling (Academic Press, Orlando, FL, 1987).

[6] D. Heckerman, Probabilistic Similarity Networks (MIT Press, Cambridge, MA, 1991).

[7] D. Heise, Causal Analysis (Wiley, New York, 1975).

[8] S.L. Lauritzen and D.J. Spiegelhalter, Local Computations with Probabilities on Graphical Structures and their Application to Expert Systems, Journal of the Royal Statistical Society, Series B50 (1988).

[9] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference (Morgan Kaufmann, San Mateo, CA, 1988).

[10] R.D. Shachter, Probabilistic Inference and Influence Diagrams, Operations Research 36 No. 4 (July-August 1988). [11] H.A. Simon, Spurious Correlations: A Causal Interpretation, Journal of the American Statistical Association 49 (1954).

[12] S. Wright, Correlation and Causation, Journal of Agricultural Research 20 (1921).

[13] S. Wright, The Method of Path Coefficients, Annals of Mathematical Statistics 5 (1934).

Stephen F. Roehrig is Assistant Professor of Information Systems and Public Policy at The Heinz School of Public Policy and Management, Carnegie Mellon University. He hold a BS and MS in mathematics from the University of Rhode Island, and a PhD in decision sciences from the University of Pennsylvania. Roehrig has research interests in knowledge representation, uncertain and defeasible reasoning, and genetic methods of problem solving.
