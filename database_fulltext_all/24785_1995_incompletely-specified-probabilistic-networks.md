---
otero_id: 24785
otero_key: "VHNHJNPG"
title: "Incompletely Specified Probabilistic Networks"
authors: "Stephen F. Roehrig"
year: "1995"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1995.11518092"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Incompletely Specified Probabilistic Networks

Stephen F. Roehrig

To cite this article: Stephen F. Roehrig (1995) Incompletely Specified Probabilistic Networks, Journal of Management Information Systems, 12:3, 81-96, DOI: 10.1080/07421222.1995.11518092

To link to this article: http://dx.doi.org/10.1080/07421222.1995.11518092

![](/api/attachments/VHNHJNPG/fulltext/images/ce4b106f43508f1703080a8a1c0e3bd7d52be74eaf6b79b58cc32d0c159a6fe2.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/VHNHJNPG/fulltext/images/af6c3d4624175451675df11e5a31199b49856fdb59d59898f8853492945bdcd7.jpg)

Submit your article to this journal ↗

![](/api/attachments/VHNHJNPG/fulltext/images/1434187e2f5b724b5d9001e766ea295e778902eca51bc0765ae6f9b0207d5630.jpg)

View related articles ↗

# Incompletely Specified Probabilistic Networks

STEPHEN F. ROEHRIG

STEPHEN F. ROEHRIG is Assistant Professor of Information Systems and Public Policy at the Heinz School of Public Policy and Management, Carnegie Mellon University. He holds a B.S. and an M.S. in mathematics from the University of Rhode Island, and a Ph.D. in decision sciences from the University of Pennsylvania. Dr. Roehrig has research interests in knowledge representation, uncertain and defeasible reasoning, and genetic methods of problem solving.

ABSTRACT: Probabilistic networks, used as an adjunct or alternative to the logical models used in artificial intelligence (AI) and decision support systems (DSS), offer a way to compactly represent a distribution over a set of random variables. Nonetheless, the specification of a given network may require conditional probabilities that are simply unavailable. In this paper a means for analyzing incompletely specified networks is presented, and some general rules are derived from the application of the method to some simple networks. The use of the technique in MIS settings is illustrated.

KEY WORDS AND PHRASES: automated reasoning, decision modeling, probabilistic networks.

THE DEVELOPMENT OF PROBABILISTIC NETWORKS AS AN ADJUNCT OR ALTERNATIVE to the logical models used in artificial intelligence (AI) and decision support systems (DSS) is a substantial achievement. However, there remains in any application the twofold problem of setting up the network and assessing the probabilities. The traditional approach has been to rely on expert opinion for both phases of the construction. Conditional independence assumptions of various sorts [15, 20] speed the work by streamlining the network and reducing the number of probabilities that must be obtained. Often, however, assumptions are suspect and the probabilities assigned are speculative.

Automating the process of building probabilistic networks is still in an early stage of development. Work on the discovery of causal models $[9, 12, 26, 29]$ has resulted in several means for supplying network structures for a set of variables given data about their interactions. In each case, however, these data (typically correlations) must be extensive; with a limited set of interactions, the number of causal models that can be eliminated from contention is small. The problem is that determining causality (however defined!) requires a precise set of simultaneous interrelationships among several variables.

The problem of “finding the numbers” will continue to be a difficult one, despite the availability of more and more data. Interesting domains are often precisely that because of a dearth of reliable information. Probabilistic networks reduce the difficulty of specifying a complete probability distribution, but a given network is unusable unless all the probabilities it calls for are available.

In this paper we take a different tack. The question we ask is, to what extent can we arrive at probabilistic conclusions when a network is incompletely specified? Since, by definition, an incompletely specified network only partially determines a distribution over all the variables represented by the nodes, additional assumptions must be imported. The assumptions we choose are, of course, subject to debate, but they are explicit, and in a form that makes it relatively straightforward to understand and modify them.

## Background

MUCH HAS BEEN WRITTEN ABOUT THE LOGICIST/PROBABILIST DEBATE in AI [2, 6, 11, 13], but without going into detail, suffice it to say that both approaches have known sets of virtues and shortcomings. Logicists argue that probabilities are inappropriate in general discourse and reasoning, since the numbers cannot be ascertained with any precision, if at all. Probabilists maintain that logic alone is insufficient for defeasible reasoning, or reasoning under uncertainty.

Out of this strongly pitched battle came probabilistic networks [20, 25]. As developed by Pearl and others, probabilistic networks

are directed acyclic graphs in which each node represents a random variable, or unknown quantity, which can take on two or more possible values. The arcs signify the existence of direct causal influences between the linked variables, and the strengths of these influences are quantified by conditional probabilities. [20]

As a simple example, imagine a company worried about a competitor who, it is conjectured, is planning to introduce a directly competing product. If this were the case, the competitor would likely be buying the (known) necessary raw materials, driving up their prices. However, these materials are used in some of the competitor's existing products, so strong sales of the raw materials might only signal a boost in production of those existing products. Also, if the competitor just hired a new ad agency, this would possibly be a signal that it was preparing to offer the new product.

Figure 1 shows a probabilistic network for this situation. Each node free of incoming arcs is labeled with a probability—the a priori likelihood of the proposition being true. The remaining nodes are labeled with conditional probabilities which describe the probability that the proposition represented by the node will be true given the verity of the nodes directly preceding it in the network. Because the network encodes certain independence assumptions (e.g., price increase is independent of new product given buy raw material), the probability distribution over all five nodes can be decomposed as:

$$
\operatorname * {P r} (a, b, c, d, e) = \operatorname * {P r} (a) \operatorname * {P r} (b) \operatorname * {P r} (c \mid a) \operatorname * {P r} (d \mid a, b) \operatorname * {P r} (e \mid d).
$$

![](/api/attachments/VHNHJNPG/fulltext/images/0d76623ebed0fedae6f6aef0d06f4a43e69200c61c19523682979a6c8c88093e.jpg)  
Figure 1. The "New Product?" Problem

Once the network topology is determined (that is, the independences have been decided) and the probabilities ascertained, it is possible to calculate the probability of any node given knowledge of any others. For instance, if company executives found that a new ad agency was retained by the competitor, but raw material prices were not on the rise, the probability of the new product introduction could be determined. There are several algorithms available for performing this sort of probabilistic inference $[17, 19, 20]$ . It should be noted that, in large problems, the use of the network to capture independence assumptions considerably improves the tractability of the solution process.

Throughout Pearl's work there is a strong emphasis, supported by theoretical arguments, on the information contained in the structure of the network. He maintains that this structure, along with the interpretation of it he provides, is singularly more important than the numbers used to quantify the links. This was his answer to the logicists.

The position taken here is that structure is important, but not necessarily in the same way that Pearl saw it. When analyzing a set of relationships between variables, a network having an arc for each relationship can be constructed. If the relationships are gathered in a systematic way—most important, if all questions about direct or indirect influence can be answered—the structure of this network will contain information about conditional independences. If the relationships are gathered in a less formal way, because of a shortage of information, the network structure will be less informative but it still may be possible to make inferences from it.

## Incomplete Probabilistic Specification

ORDINARY PROBABILISTIC NETWORKS REQUIRE THAT ALL RELEVANT CONDITIONAL probabilities are specified. We do not make that assumption here. We take as given a set of propositions (e.g., $a, b, \ldots$ ), and another set of qualified relationships (e.g., $a$ tends to bring about $b$ ) between them. The propositions and relationships can be visualized with a network of nodes and arcs. However, we do not make any conditional independence assumptions (although this is an obvious extension that we intend to pursue); all we want to do is determine if, for some probabilistic interpretation of the relationships, we can deduce properties of a probability distribution over all the propositions. Thus, our graphs do not reflect known or assumed conditional independence assumptions.

A good example of a situation where only incomplete information is available is the one where, perhaps for reasons of confidentiality, we have access to only a subset or projection of a database table. Here we will normally not have enough information to specify independence relationships, but may have sufficient data to quantify some conditional probabilities.

A simple instance of this situation might occur when we are interested in determining the likelihood of a certain disease D given two symptoms S1, S2 (see Figure 2). In many databases, query size controls are in place that block answers to queries resulting in small counts. The reasoning behind such controls is that a clever user might be able to infer sensitive information about an individual even though personal data such as name or SSN are absent. For the probabilistic network of Figure 2, $\Pr(D \mid S1, S2)$ might be unavailable due to the small number of data points, yet $\Pr(D \mid S1)$ and $\Pr(D \mid S2)$ might be easily found. In this case, the network is incompletely specified, but some relevant data are known.

Another example arises when we try to reason from newspaper accounts, perhaps quotes from various players in a public policy debate. Analyzing statements of politicians in terms of first order logic can be rather difficult, because as soon as a contradiction appears, we are sunk. However, some parts of the argument may be quantifiable in less absolute, possibly probabilistic, terms. If this is so, then it is reasonable to try to see where the argument leads.

As a concrete example, the network of Figure 3 was developed from a New York Times article $[27]$ analyzing the potential effects of various factors on job shortages. The imprecise or conjectural nature of many of the links makes it very unlikely that a full probabilistic specification could be assembled, but the tendencies indicated by each of the individual links in the network are broadly accepted by economists.

First we must be clear on the probabilistic meaning of sentences such as “students tend to be young,” “high serum PSA often indicates prostate cancer,” or “greater efficiency usually leads to lower costs.” There are two propositions, say s for student and y for young. The four interpretations we consider are:

1. We might assume, first of all, that our sentence means

$$
\operatorname * {P r} (y \mid s) = t \text {   or   } \operatorname * {P r} (y \mid s) \geq t
$$

for some value of t, presumably (but not necessarily) larger than 0.5. This says that when considering only the two propositions s and y, we would bet that someone was young when we knew that person was a student. If other factors influence our judgment of y, we assume that they have been marginalized out.

![](/api/attachments/VHNHJNPG/fulltext/images/8294c42cf8a3c81599a147904b59d0c963589b3e773474c1a260498aa8abd278.jpg)  
Figure 2. Two Symptoms Indicating a Disease

2. If knowing that someone is a student increases belief that she is young over a similar belief for an arbitrary person, we would have

$$
\operatorname * {P r} (y \mid s) > \operatorname * {P r} (y).
$$

3. If we think that studentness increases the chance that a person is young as compared to someone who is not a student, we have

$$
\operatorname * {P r} (y \mid s) > \operatorname * {P r} (y \mid \neg s).
$$

In this case, both probabilities may be low, but $\Pr(y \mid s)$ is the larger. This condition is called “positive association” in [18], and is in fact equivalent to positive correlation between y and s.

4. Perhaps in the overall problem, of which “students tend to be young” is a fragment, there is another factor t that also has a bearing on students’ age. Then we might suppose the sentence means

$$
\operatorname * {P r} (y \mid s, t) > \operatorname * {P r} (y \mid \neg s, t) \text {   and   } \operatorname * {P r} (y \mid s, \neg t) > \operatorname * {P r} (y \mid \neg s, \neg t).
$$

In light of Simpson's paradox [24, 28], this interpretation may be quite different probabilistically from point 2 above. This interpretation has been studied by Wellman [30] in the context of qualitative probabilistic networks.

Because of the existence of distributions exhibiting Simpson's paradox, point 3 is not implied by point 4, and examples where point 3 does not guarantee point 4 are easy to find. Thus, these two are somewhat independent. Interpretations 2 and 3 are equivalent, since by rewriting 2,

(1)

$$
\begin{array}{r l} \operatorname * {P r} (e \mid a) & > \operatorname * {P r} (e) \\ & > \operatorname * {P r} (e \mid a) \operatorname * {P r} (a) + \operatorname * {P r} (e \mid \neg a) \operatorname * {P r} (\neg a) \end{array}\tag{2}
$$

we get:

(3)

$$
\operatorname * {P r} (e \mid a) (1 - \operatorname * {P r} (a)) > \operatorname * {P r} (e \mid \neg a) \operatorname * {P r} (\neg a)\tag{4}
$$

$$
\operatorname * {P r} (e \mid a) > \operatorname * {P r} (e \mid \neg a).
$$

It seems, however, that the first view is the most natural probabilistic view of most “tends” statements, so this case will be considered in more detail.

What we want to do is decide the likelihood of a particular proposition given (a) the truth of some others, and (b) the set of known relationships. For a fully specified probabilistic network, this is called probabilistic inference, and a number of methods have been worked out to achieve it. Our situation is different, of course, since we do

Figure 3. Economic Factors Affecting Job Shortage (Source: New York Times, July 17, 1993)

Downloaded by [University of Pennsylvania] at 09:37 09 May 2016

![](/api/attachments/VHNHJNPG/fulltext/images/0ef491461ac2bde40ca01ba50aaab3a5290efb4858bb6b4e7a231e3c36a6ee7d.jpg)

not have a fully specified network. While there are a number of techniques for imputing a distribution given partial information (one of these, maximum entropy, is discussed below), here we explore a different idea, sampling of distributions.

In general there will be an infinite space of distributions satisfying the conditions specified by a given set of (underconstraining) relationships. In Monte Carlo fashion, we explore this space, keeping track of the implications each such distribution has for the proposition in which we are interested.

Suppose, for example, we are told that “All Stars tend to be good hitters,” “Good hitters tend to be poor fielders,” and “All Stars tend to be good fielders.” If Joe is known to be an All Star and a good hitter, can we tell if he is a good fielder? Well, no; there are distributions with reasonable quantifications for “tends” which go both ways. But if we look at all distributions, or a representative subset of them, which are in accord with the evidence, we can obtain a second-order understanding that may help us make up our mind about Joe.

Letting A :: All Star, H :: good hitter, and F :: good fielder, we take the statements above to mean

(5)

$$
\operatorname * {P r} (H | A) \geq 0. 5\tag{6}
$$

$$
\operatorname * {P r} (F | H) \leq 0. 5\tag{7}
$$

$$
\operatorname * {P r} (F | A) \geq 0. 5.
$$

With these constraints, we ask in what proportion of distributions is Joe, the known All Star, likely to be a good fielder?

## Sampling Distributions

NEXT WE NEED TO DISCUSS MEANS OF GENERATING THE RANDOM DISTRIBUTIONS. For a network with three propositions, say, any such distribution can be characterized as a set of eight probabilities, one for each possible outcome set over the three propositions, with all eight summing to one. To be neutral, we will draw distributions uniformly, although the method described can be extended to produce modal “distributions of distributions.” To motivate the development, we first discuss the procedure for lower dimensions, then extend it.

The simplest case is the two-dimensional one where we wish to choose

$$
(y _ {1}, y _ {2}) \colon 0 \leq y _ {1}, y _ {2} \leq 1, y _ {1} + y _ {2} = 1,
$$

with $(y_{1}, y_{2})$ uniform over $[0, 1] \times [0, 1]$ . To do this, draw $x_{1}, x_{2}$ independently from $\varepsilon(1)$ , the exponential distribution with parameter 1. Then set

$$
y _ {1} = \frac {x _ {1}}{x _ {1} + x _ {2}}, y _ {2} = \frac {x _ {2}}{x _ {1} + x _ {2}}.
$$

$y_{1}$ and $y_{2}$ obviously sum to one and are bounded between 0 and 1. To show that they are uniform, we set $z_{1} = x_{1} + x_{2}, z_{2} = x_{1} / x_{1} + x_{2}$ , and compute the joint density of $(z_{1}, z_{2})$ . The joint density of $x_{1}$ and $x_{2}$ is

$$
p (x _ {1}, x _ {2}) = e ^ {- (x _ {1} + x _ {2})}
$$

for $0 \leq x_{1}, x_{2} \leq \infty$ . Let

$$
\left(z _ {1}, z _ {2}\right) = \boldsymbol {g} \left(x _ {1}, x _ {2}\right) = \left(x _ {1} + x _ {2}, \frac {x _ {1}}{x _ {1} + x _ {2}}\right).
$$

Then $\mathbf{g}$ is one-to-one on $0 \leq x_1, x_2 \leq \infty$ , and its range is $S = \{(z_1, z_2): z_1 > 0, 0 < z_2 < 1$ . On $S$ ,

$$
\boldsymbol {g} ^ {- 1} \left(z _ {1}, z _ {2}\right) = \left(z _ {1} z _ {2}, z _ {1} - z _ {1} z _ {2}\right),
$$

so that

$$
J _ {g - 1} \left(z _ {1}, z _ {2}\right) = \left| \begin{array}{c c} z _ {2} & 1 - z _ {2} \\ z _ {1} & - z _ {1} \end{array} \right| = - z _ {1}.
$$

The joint density of $(z_{1}, z_{2})$ is

$$
p \left(z _ {1}, z _ {2}\right) = \frac {p _ {X} \left(\boldsymbol {g} ^ {- 1} \left(z _ {1} , z _ {2}\right)\right)}{\left| J _ {\boldsymbol {g}} \left(\boldsymbol {g} ^ {- 1} \left(z _ {1} , z _ {2}\right)\right) \right|} = z _ {1} e ^ {- \left(z _ {1} z _ {2} + \left(z _ {1} - z _ {1} z _ {2}\right)\right)} = z _ {1} e ^ {- z _ {1}},
$$

that is, $z_{2}$ is independent of $z_{1}$ , and $z_{2}$ is uniform over (0,1). By the symmetry of the construction, this shows that $y_{1}$ and $y_{2}$ are both uniform on (0,1).

The proof above used the dummy variable $z_{1} = x_{1} + x_{2}$ . Had we set

$$
z _ {1} = \frac {x _ {1}}{x _ {1} + x _ {2}}, z _ {2} = \frac {x _ {2}}{x _ {1} + x _ {2}},
$$

the inverse calculation would not have worked; with this definition the transformation is not one-to-one, and in fact the inverse does not exist. In higher dimensions, we will use the same trick. What we show is that n-dimensional normalized exponentially distributed random deviates are uniform on all subspaces of dimension n-1.

As we move up to three dimensions, we see that we do not want each of $y_{1}, y_{2}, y_{3}$ to be uniform. Consider the plane $y_{1} + y_{2} + y_{3} = 1$ in the unit cube. Projection of this plane on any two-dimensional subspace yields a triangular region. For instance, projecting onto the $y_{1} - y_{2}$ plane, we get the triangular region bounded by the coordinate axes and the line $y_{1} + y_{2} = 1$ . It is true that a uniform distribution of points over the plane $y_{1} + y_{2} + y_{3} = 1$ will project into a uniform distribution over the triangle in the $y_{1} - y_{2}$ plane. But it is easy to see that each of $y_{1}$ and $y_{2}$ will not be uniform on [0,1]; their densities will be ramp-shaped. Thus, in the unit cube, what we seek is a distribution over points

$(y_{1},y_{2},y_{3})$ such that

$$
y _ {1} + y _ {2} + y _ {3} = 1,
$$

$(y_{1},y_{2})$ is uniform in $y_{1} > 0,y_{2} > 0,y_{3}\leq 1 - y_{1},$

$$
(y _ {1}, y _ {3}) \text {   is   uniform   in   } y _ {1} > 0, y _ {3} > 0, y _ {2} \leq 1 - y _ {1},
$$

$$
(y _ {2}, y _ {3}) \text {   is   uniform   in   } y _ {2} > 0, y _ {3} > 0, y _ {1} \leq 1 - y _ {2}.
$$

All of these conditions may be proved at once by symmetrically applying the following argument, which is a simple extension of the previous one.

Draw $x_{1}, x_{2}$ , and $x_{3}$ independently from $\varepsilon(1)$ , and set

$$
y _ {1} = \frac {x _ {1}}{x _ {1} + x _ {2} + x _ {3}}, \frac {x _ {2}}{x _ {1} + x _ {2} + x _ {3}}, \frac {x _ {3}}{x _ {1} + x _ {2} + x _ {3}}.
$$

Following the earlier argument, set $z_{1} = x_{1} + x_{2} + x_{3}, z_{2} = x_{1} / (x_{1} + x_{2} + x_{3}), z_{3} = x_{1} / (x_{1} + x_{2} + x_{3})$ and compute the joint density of $(z_{1}, z_{2}, z_{3})$ . Now

$$
\mathbf {g} ^ {- 1} (z _ {1}, z _ {2}, z _ {3}) = (z _ {1} - z _ {1} z _ {2} - z _ {1} z _ {3}, z _ {1} z _ {2}, z _ {1} z _ {3}).
$$

Once again we have $J\mathbf{g}^{-1}(z_1, z_2) = -z_1$ , and we find

$$
p \left(z _ {1}, z _ {2} z _ {3}\right) = z _ {1} e ^ {- \left(\left(z _ {1} - z _ {1} z _ {2} - z _ {1} z _ {3}\right) + z _ {1} z _ {2} + z _ {1} z _ {3}\right)} = z _ {1} e ^ {- z _ {1}}.
$$

Thus, $(z_{2}, z_{3})$ is uniformly distributed on its domain $z_{1}, z_{2} > 0, z_{3} \leq 1 - z_{1}$ . Applying this result to the variables $y_{1}, y_{2}, y_{3}$ shows that $(y_{1}, y_{2}, y_{3})$ is uniformly distributed in $0 < y_{i}, i = 1 \ldots n, \Sigma y_{i} = 1$ . Extension to the eight-dimensional case, the one necessary for distributions over three propositions, and for even higher dimensions, is obvious.

For each distribution generated in this way, the probability that Joe is a good fielder is easily computed. Choosing $\Pr(F \mid A,H) > 0.5$ as a cutoff above which we judge Joe to be a good fielder, a proportion can be tallied. As it turns out, in 65 percent of the distributions satisfying the conditions, Joe is likely to be a good fielder.

## Sampling versus Maximum Entropy

THE GENERAL SITUATION WE ARE CONSIDERING IS ONE IN WHICH the joint probability distribution is underconstrained. As mentioned above, another way of attacking the problem is to derive a special joint distribution that agrees with the given data and contains the least additional information. Suppose $P_{ij\ldots k}$ is the underlying distribution, where each of the variables $i,j,\ldots,k$ indexes the possible outcomes of the propositions $A_{i}, B_{j}, \ldots, C_{k}$ . Then the entropy of the distribution is defined by

$$
H = - \sum_ {i, j, \dots k} P _ {i j \dots k} \log (P _ {i j \dots k}),
$$

where the sum is taken over all possible combinations of the $i,j,\ldots,k$ . Minimizing the information is equivalent to maximizing entropy, hence the method's name. The probability values thus chosen are the most noncommittal, subject to the constraints of the known values. Shore and Johnson [23] have argued that the selection of any other value would be inconsistent, because any other choice would imply more information than was given in the problem.

To apply this principle, the given information is written in the form of constraints on an otherwise arbitrary (complete) distribution. These constraints underspecify the distribution. Maximizing the entropy function subject to the constraints is a nonlinear mathematical programming problem, which can be solved using standard algorithms.

Maximum entropy appears at first sight to be exactly what we're after in the case where we have insufficient information. Let's see how it works for Joe the hard-hitting All Star. Assume, as before:

(8)

$$
\operatorname * {P r} (H | A) \geq 0. 5\tag{9}
$$

$$
\operatorname * {P r} (F \mid H) \leq 0. 5\tag{10}
$$

$$
\operatorname * {P r} (F | A) \geq 0. 5.
$$

Expanding in terms of the event probabilities, we can write the first constraint as:

$$
\begin{array}{r l} \operatorname * {P r} (A, H, F) + \operatorname * {P r} (A, H, \neg F) & \geq 0. 5 (\operatorname * {P r} (A, H, F) + \operatorname * {P r} (A, H, \neg F) \\ & \quad + \operatorname * {P r} (A, \neg H, F) + \operatorname * {P r} (A, \neg H, \neg F)). \end{array}
$$

The other conditionals are rewritten similarly, and an additional constraint enforcing the usual sums-to-one condition is added. Maximizing the entropy subject to the given probability constraints results in a distribution uniform over the set of eight events. That is, the conditional probability constraints do not, so far as maximum entropy is concerned, contain any information at all!

On reflection, this result is inescapable; maximum entropy looks for the distribution “closest” to uniform (least information) that agrees with the available data. Since the uniform distribution itself agrees with the data, that is the one selected. On the other hand, despite its grounding in a plausible assumption (the maximum entropy principle), the result is confusing. First we say that all we know is, for example, $\Pr(h \mid A) \geq 1/2$ , and then are forced to conclude that $\Pr(h \mid A) = 1/2$ . Because of the incongruity of this conclusion, we feel that sampling is a more cognitively appealing approach.

## A Sample of Results

A WIDE VARIETY OF THREE- THROUGH SIX-NODE NETWORK TOPOLOGIES have been examined using the simulation procedure. Several of the more interesting or illuminating configurations are discussed here. A more complete collection of examples is being assembled in a working paper.

For these examples, each arc is labeled with either $a + \text{or } a -$ ; a “+” on an arc from $x$ to $y$ signifies that $\Pr(y|x) > 0.5$ , while “-” indicates $\Pr(y|x) < 0.5$ . Of course, values other than 0.5 could be (and have been) used, but a constant value makes it easier to get a feel for what is going on.

The first group shows a simple linear chain (see Figure 4). For each network, the last two lines show the proportion of distributions for which the given probability obtains. For the left-most network, 81 percent of the sampled distributions that had $\Pr(b \mid a) \geq 0.5$ and $\Pr(c \mid b) \geq 0.5$ had $\Pr(c \mid a, b) \geq 0.5$ . For this network, the “dilution effect” of chaining is apparent. For the sequence $\Pr(c \mid b)$ , $\Pr(c \mid a, b)$ , $\Pr(c \mid a)$ , the proportions are 1.00, 0.81, and 0.77. It is perhaps not obvious that the fraction having $\Pr(c \mid a, b) \geq 0.5$ is less than one when all the distributions have $\Pr(c \mid b) \geq 0.5$ . The explanation is that we are considering proportions of distributions with a particular property, not conditional probabilities for a fixed distribution.

Also apparent in this group of networks is a natural symmetry. The proportions for the first two are complements (the proportions sum to 1), as are those for the last two.

To illustrate the effect of adding an additional arc, consider the set shown in Figure 5. Looking at the second network in each group of four, we see that the addition of a “+” arc from $a$ to $b$ makes a significant change, even though we are looking for those distributions for which $\Pr(c \mid a,b) \geq 0.5$ , that is, we’re assuming both $a$ and $b$ are known to be true. The lower network is the one representing Joe, the good-hitting All Star. If we didn’t have the arc from $a$ to $b$ , that is, if we didn’t know that All Stars tend to be good hitters, we would be ambivalent about Joe’s fielding. However, once we know the All Star–good hitter connection, we might come to favor the idea that Joe can field as well. It appears that the All Star–good fielder arc now takes precedence.

Next look at the following two networks having four nodes. The first is the standard "Nixon diamond" (a::Nixon, b::Republican, c::Quaker, d::militaristic), while the second has the conflicting influences in the upper half of the diamond (see Figure 6).

The difference between the two is straightforward. In the first, because we know a, we have reason to believe both b and c with equal strength. Thus, the likelihood of d is evenly balanced. For the second network, we should disbelieve c, and so the positive arc from c to d has little or no effect; we would need to know $\Pr(d \mid \neg c)$ , which we are assuming is unknown.

As a last example, consider the following group of three networks. In each, a has a positive relationship with d, but there are differing connections with two other nodes b and c, neither of which has a connection with d (see Figure 7).

Once again, the simulation method yields some counterintuitive results. Focusing on the first network, it is apparent that knowing a alone might give more reason to believe b than if we knew some of the other consequences of a as well. When we look at the other two networks, it seems that knowing a as well as some other consequences (b or b and c) that are not suggested by a diminishes the likelihood that d will have high probability. We stress that we are not talking about the probabilities associated with a fixed probabilistic network, but more generally about proportions of distributions with certain properties.

Figure 5. Adding an Arc  
![](/api/attachments/VHNHJNPG/fulltext/images/5a8a8a5390889957c3e6199bcb0a5948a4870274718ce70a455b517f230b4665.jpg)

## Simpson's Paradox

CONSIDER THE SUMMER VACATIONER WHO LEAVES THE COUNTRY IN MIDSEASON, with his favorite baseball player comfortably leading the league in hitting. When he returns after season's end, he learns that this player, call him Player A, has lost the batting title to Player B. He naturally assumes that during the second half of the season, his favorite player must have hit for a lower average than the eventual winner. Intuitively, many people argue that if Player A has a higher average in the first half, but loses overall to Player B, then Player B must have had the higher average in the second half.

Many others will recognize this apparently simple reasoning problem as an instance of Simpson's paradox [1, 3, 4, 5, 14, 18, 21, 24, 28]. While this scenario seems to be sufficiently rich in detail to warrant a firm conclusion, in fact it could be that Player A had a higher average than Player B in the first and second halves, but still lost overall. Although the overall batting average is determined by a weighted sum of the two half-seasons, the weights may be far from even, giving rise to counterintuitive results.

Table 1 presents a numerical example of Simpson's paradox, in the context of two baseball players over the course of a season. While this sort of counterintuitive construction has been much analyzed, we briefly consider it in terms of an incompletely specified network.

![](/api/attachments/VHNHJNPG/fulltext/images/e5ce7fc8248157bc4ad0bf70bb8a672a74ec65c692dac233fd6bed252d39b793.jpg)  
Figure 6. Four-Node Networks

![](/api/attachments/VHNHJNPG/fulltext/images/aed8b245bf3b9a42d9a6930c845e7f095c183f411d0816ef994b7ca3f375269e.jpg)  
Figure 7. One Cause with Many Effects

The diagram for the instance in Table 1 is given in Figure 8. p stands for the proposition that Player A has an at-bat, and h is the proposition that a hit is made. Thus, $\neg p$ represents an at-bat for Player B, and $\neg h$ stands for failure to get a hit. s refers to the first half of the season, and $\neg s$ to the second half.

The plus sign on the arc $p \to h$ is supposed to indicate the fact that Player A will more likely get a hit in any at-bat than will Player B, at least for a known value of $s$ (= true or false, depending on the date). The arc $p \to s$ records the information that Player A had fewer at-bats than Player B in the first half of the season. However, if we don't know in which half of the season an at-bat occurred—that is, if we have no information about $s$ —the appropriate diagram should look like Figure 9. We have labeled the only remaining arc with a question mark, indicating that there is uncertainty in the outcome. If this sign is negative, then Simpson's paradox has obtained.

In terms of the complete diagram (e.g., Figure 8), Simpson's paradox will obtain whenever (1) the influence recorded on $p \to h$ is positive, and (2) the combination (however calculated) of those on $p \to s$ and $s \to h$ exceeds that on $p \to h$ .

Given the plethora of examples in the literature, Simpson's paradox may seem a commonplace. Nonetheless, most people do find it paradoxical. Despite the existence of “Simpson’s paradox in real life” examples, it may be that we, as reasoners laboring with incomplete information, actually do a fairly good job. The heuristic “If Player A beats Player B in both halves of the season, he wins overall” might after all be the right one.

Now, since the batting average problem is one of a surprising distribution over three propositions (player A/player B, first half/second half, hit/no hit), a plausible reaction is to ask “how often” such surprises can occur. Note that the paradoxical result is not one of a bad probabilistic outcome in a situation where the odds (and thus an expected value) suggest otherwise. Rather, the distribution itself is only partially determined. But if distributions satisfying the constraints of the problem only rarely exhibit “paradoxical behavior,” then it seems justified, in the absence of additional information, to reason as intuition suggests.

Table 1. Simpson's Paradox in Baseball

<table><tr><td rowspan="2"></td><td colspan="2">1st Half</td><td colspan="2">2nd half</td><td colspan="2">Season</td></tr><tr><td>Player A</td><td>Player B</td><td>Player A</td><td>Player B</td><td>Player A</td><td>Player B</td></tr><tr><td>At bats</td><td>200</td><td>300</td><td>300</td><td>200</td><td>500</td><td>500</td></tr><tr><td>Hits</td><td>72</td><td>105</td><td>84</td><td>54</td><td>156</td><td>159</td></tr><tr><td>Average</td><td>0.360</td><td>0.350</td><td>0.280</td><td>0.270</td><td>0.312</td><td>0.318</td></tr></table>

![](/api/attachments/VHNHJNPG/fulltext/images/501d623288199af3337006b188e3295741d6bc2db5e19cd11e2c893a2434ef39.jpg)  
Figure 8. Generic Network Diagram for Simpson's Paradox

With the symbolization of the batting average problem, the setup of Simpson's paradox has

$$
\operatorname * {P r} (h \mid p, s) > \operatorname * {P r} (h \mid \neg p, s), \operatorname * {P r} (h \mid p, \neg s) > \operatorname * {P r} (h \mid \neg p, \neg s).
$$

Of the distributions satisfying these conditions, we can look for the proportion satisfying $\Pr(h \mid \neg p) > \Pr(h \mid p)$ , that is, those representing Simpson's paradox. In extended simulations we found the likelihood of "paradoxical" behavior to be 3 percent, a figure that compares well with the 3.8 percent found in a study of Simpson's paradox in airline on-time data [7].

## Discussion

SPACE LIMITATIONS WORK AGAINST A MORE COMPLETE SET OF EXAMPLES, but the ones given illustrate that the sampling method developed here can be useful in analyzing incompletely specified probabilistic networks.

There are obvious limitations to the method of sampling. Networks with large numbers of nodes present formidable computational difficulties, not only with (1) the sheer size of the distributions, but also because of (2) the diminishing proportion of distributions generated that satisfy the given conditional probability constraints. But

Figure 9. Collapsed Diagram for Simpson's Paradox

more satisfactory methods do not seem to be available.

The literature on Monte Carlo solution techniques for ordinary probabilistic networks suggests that the algorithm for distribution generation might be modified so that the conditional constraints are automatically satisfied. This would alleviate difficulty 2. It might also be possible to devise a means for chaining together results on subgraphs of a larger network, but this would likely run counter to the goal of minimizing the need for additional assumptions.

Perhaps the most obvious immediate use of the ideas proposed here is to judge or “calibrate” alternate assumptions (explicit or implicit) made by various other automated reasoning schemes. Decision, and conclusion revision, in the face of incomplete information is an increasingly pressing problem for AI and decision theory, and a clear methodological champion has yet to be crowned. The sampling procedure suggested here will, we hope, prove useful in sorting out those methods that can treat the broadest range of indeterminate situations.

## REFERENCES

1. Abramson, N.S.; Kelsey, S.F.; Safar, P.; and Sutton-Tyrrell, K. Simpson's paradox and clinical trials: what you find is not necessarily what you prove. Annals of Emergency Medicine, 21 (1992), 1480–1482.

2. Bhatnager, R.K., and Kanal, L.N. Handling uncertain information: a review of numeric and non-numeric methods. In L.N. Kanal and J.F. Lemmer (eds.), Uncertainty in Artificial Intelligence. New York: North Holland, 1986, pp. 3–26.

3. Bickel, P.J.; Hammel, E.A.; and O'Connell, J.W. Sex bias in graduate admissions: data from Berkeley. Science, 187 (1975), 398–404.

4. Blyth, C.R. On Simpson's paradox and the sure-thing principle. Journal of the American Statistical Association, 67 (1972), 364–366.

5. Blyth, C.R. Some probability paradoxes in choice from among random alternatives. Journal of the American Statistical Association, 67 (1972), 366–381.

6. Buchanan, B.G., and Shortliffe, E.H., eds. Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project. Reading, MA: Addison-Wesley, 1984.

7. Caulkins, J.P.; Larkey, P.D.; and Yuan, Y. Adjusting ratings for tournament difficulty: the case of rating airlines' on-time performance. Working paper 92–25, Carnegie Mellon University, Heinz School of Public Policy and Management, Pittsburgh, 1992.

8. Cheeseman, P.C. A method for computing generalized Bayesian probability values for expert systems. Proceedings 8th International Joint Conference on Artificial Intelligence, Karlsruhe, West Germany, 1983, pp. 198–202.

9. Cooper, G., and Herskovits, E. A Bayesian method for the induction of probabilistic networks from data. Technical Report KSL-91-02, Knowledge Systems Laboratory, Stanford University, 1991.

10. Gale, W.A., ed. Artificial Intelligence and Statistics. Reading, MA: Addison-Wesley, 1986.

11. Genesereth, M.R., and Nilsson, N.J. Logical Foundations of Artificial Intelligence. Palo Alto, CA: Morgan Kaufmann, 1987.

12. Glymour, C.; Scheines, R.; Spirtes, P.; and Kelly, K. Discovering Causal Structure: Artificial Intelligence, Philosophy of Science, and Statistical Modeling. Orlando, FL: Academic Press, 1987.

13. Harman, G. Change in View: Principles of Reasoning. Cambridge, MA: MIT Press, 1986.

14. Haunsperger, B., and Saari, D.G. The lack of consistency for statistical decision procedures. The American Statistician, 45 (1991), 252–255.

15. Heckerman, D. Probabilistic Similarity Networks. Cambridge, MA: MIT Press, 1992.

16. Kanal, L.N., and Lemmer, J.F. Uncertainty in Artificial Intelligence. New York: North Holland, 1986.

17. Lauritzen, S.L., and Spiegelhalter, D.J. Local computations with probabilities on graphical structures and their application to expert systems. Journal of the Royal Statistical Society, Series B50 (1988), 157–224.

18. Lindley, D.V., and Novick, M.R. The role of exchangeability in inference. Annals of Statistics, 9 (1981), 45–58.

19. Neapolitan, R.E. Probabilistic Reasoning in Expert Systems. New York: Wiley, 1990.

20. Pearl, J. Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference. San Mateo, CA: Morgan Kaufmann, 1988.

21. Saari, D.G. The source of some paradoxes from social choice and probability. Journal of Economic Theory, 4 (1987), 1–22.

22. Shachter, R.D. Probabilistic inference and influence diagrams. Operations Research, 36 (July–August 1988), 589–604.

23. Shore, J.E., and Johnson, R.W. Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy. IEEE Transactions on Information Theory, IT–26, 1 (January 1980), 26–37.

24. Simpson, E.H. The interpretation of interaction in contingency tables. Journal of the Royal Statistical Society, B13 (1951), 238–241.

25. Spiegelhalter, D.J. A statistical view of uncertainty in expert systems. In Gale, W.A. (ed.), Artificial Intelligence and Statistics. Reading, MA: Addison-Wesley, 1986.

26. Spirtes, P.; Glymour, C.; and Scheines, R. Causation, Prediction and Search. New York: Springer-Verlag, 1993.

27. Uchitelle, L. Experts say a lack of hiring stems from weak spending. The New York Times, July 17, 1993.

28. Wagner, C.H. Simpson's paradox in real life. The American Statistician, 36 (1982), 46–48.

29. Wedelin, D. Discovering causal structure from data. Technical Report, Department of Computer Science, Chalmers University of Technology, 1993.

30. Wellman, M.P. Fundamental concepts of qualitative probabilistic networks. Artificial Intelligence, 20 (1990), 687–701.
