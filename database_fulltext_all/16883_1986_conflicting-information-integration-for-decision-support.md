---
otero_id: 16883
otero_key: "7JP43MVU"
title: "Conflicting information integration for decision support"
authors: "Donald E. Brown; Bernard G. Duren"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90003-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conflicting Information Integration For Decision Support

Donald E. BROWN and Bernard G. DUREN
University of Virginia, Charlottesville, VA 22901, USA

The integration of information from multiple sources is a topic of increasing importance to the design of advanced decision support systems for a variety of situation assessment tasks. The integration of information is especially difficult when the multiple sources provide conflicting information. In general, approaches to this problem have used either probability-based techniques or techniques based on one of the newer theories of uncertainty. This paper surveys these current approaches to the conflicting information problem and then describes a new approach based on information theory.

Keywords: Decision support systems, Information fusion, Uncertainty management, Relative-entropy.

![](/api/attachments/7JP43MVU/fulltext/images/eeedd4183828e01fc5424653607c725ec174a4c42a9e5c575b615b6582431f63.jpg)

Bernard G. Duren graduated from Indiana University (A.B. Mathematics, 1967) and the Georgia Institute of Technology (M.S. Operations Research, 1972). Currently enrolled in Systems Engineering, University of Virginia. Research Interests include situation assessment processes (e.g., in multisensor surveillance), information theoretic models of uncertain inference, and C3 Systems Theory.

![](/api/attachments/7JP43MVU/fulltext/images/da6ff2cac115323ad87165e2f5590dc8c00e4bcdbc3968779a9ef3a9f7d4a9c1.jpg)

Donald E. Brown is an Assistant Professor in the Department of Systems Engineering at the University of Virginia. He received his Ph.D. in Industrial and Operations Engineering from the University of Michigan. He has designed information systems for a number of federal agencies and has also consulted for both governmental and private organizations. His current research is in the areas of knowledge representation and inference, information fusion techniques, model general and design aiding systems.

tion and management, and design aiding systems.

## 1. Introduction

Currently there is considerable interest in computer-based tools for describing an ambiguous or uncertain situation given observed data and subjective assessments. These tools, referred to as interpretation or situation assessment systems, may be required as components for more complex systems designed to perform diagnosis, control, monitoring or instruction.

The strategy for solving interpretation problems is to iteratively perform a series of inference tasks with each task supported by interacting knowledge sources and shared processing resources. Fundamental activities supporting the inference tasks are information acquisition and integration. The goal of the interpretation process is to provide the decision maker with a clearer picture of an uncertain or ambiguous situation. The process is terminated either by time constraints or by exhausting the usefulness of the information sources.

Within the situation assessment function the topic of multisource information integration is of fundamental importance to the design of computer-based decision aiding systems. Information sources are typically varied and may consist of humans, electronic sensors, computer models, or combinations of these. The information provided by these disparate sources frequently contains uncertainties and even inconsistencies. It is not unusual, for instance, for human experts to provide dramatically different estimates for the likelihood of an uncertain event (e.g. [39] and [26]). Multiple sources may also employ different communications paths which produce variable processing delays, inconsistent query procedures, and shifting baselines for similar sources. Finally, even if error statistics are available for the sources, these statistics may also be unreliable.

In practice, the problems of computer-based interpretation and situation assessment are difficult to solve. There are a number of technical barriers to overcome, but the most basic problem is the effective combination of information from diverse sources. Within this problem area the specific task of integrating conflicting information is particularly difficult and important.

This paper presents a new approach to the problem of conflicting information integration in decision support systems. The next section reviews and critiques the major approaches that have been advocated as appropriate for this problem. In section 3 we present our method and in section 4 we provide an example of its use. Finally, section 5 contains a summary of our results and our conclusions.

## 2. Existing Methods for Information Integration

A number of approaches have been advanced for reconciling or aggregating information from multiple sources. In general, these approaches are based on either probability theory or one of its recent competitors. In this section we briefly survey integration methods from these two diverse areas.

## 2.1. Probability Based Methods

Probabilistic methods for integrating multi-source information have been developed to support situation assessment tasks for a wide variety of applications. To provide structure to the array of different probabilistic approaches we divide them into two categories based on their field of origin. First, there are approaches developed primarily out of work in decision theory. These methods are generally concerned with aggregating forecasts or probability assessments. A second category derives from the computer-based decision aiding literature and is now closely associated with expert systems.

Within the first category of probabilistic based techniques, one of the most well-known methods for combining expert judgments is the Delphi approach advocated by [2]. This approach and that of [42] seek to resolve conflict between human experts through consensus. Two major problems hamper applications of consensus techniques: (1) there is no theoretical justification for consensus, and (2) incentives for consensus may not exist. It is also obvious that the approach is applicable only to human information sources.

Also within the decision theoretic category of probabilistic approaches are those that use a Bayesian construction to aggregate conflicting information. These approaches are generally associated with combining forecasts. Winkler ([43]) considers the problem of combining several calibrated forecasts of a single variable. He uses an approximation to Bayes' rule due to [6], that under certain conditions the prior distribution may be approximated by a uniform distribution over the relevant interval. The results also assume normal forecasts and knowledge of the covariance matrix. Winkler and Makridakis ([44]) provide five different procedures for estimating the requisite aggregation weights when the covariance matrix is unknown.

The approach of [43] is considered in its most general form by Morris ([23],[24],[25]). The problem of combining forecasts is treated by a two-stage Bayesian process. However, Morris ([25]) cautions that the product form used in this analysis is only applicable to continuous random variables. Some controversy has surrounded this work. [32] argues that the definitions of calibration in [23] are inconsistent and the conditions for the results in [23] and [25] may be impossible to obtain.

In general the problem of multisource information integration is more complex than combining expert forecasts or probability assessments. The differences involve both the nature of the evidence provided and the structure of the decision task. The former differences are readily apparent when disparate information sources provide evidence relevant to only limited events. For example, suppose we would like to estimate the likelihoods of various scenarios for the theft of nuclear material from a holding facility. One expert may be able to provide probability assessments for scenarios involving terrorist groups and be completely unknowledgeable about scenarios involving embezzlement or organizational variables. A second expert may provide probability estimates for both embezzlement and terrorist scenarios, and the latter may conflict with the first expert's assessments. It is clear that the approaches available from decision theory are incapable of treating this problem in a straightforward fashion. A related problem, noted in [10], is that the learning model through conditional probabilities inherent in Bayesian techniques does not allow for revision of previously accepted evidence.

A second set of differences between situation assessment and forecast aggregation stems directly from the structure of the requisite inference task. This task may be considerably more complicated due to the decision maker's conceptual knowledge of the decision environment. The task, for instance, may be one of pattern recognition in which relevant information is cascaded through a conceptual network. As suggested by [35], methods are needed for constructing complex judgements from simpler, more elementary judgments.

However, our approach is similar to the work from decision theory in providing a situation independent framework for information integration. Hence, the procedures remain unchanged as the decision environment shifts. Another important similarity is that subjective information is utilized. However, the information need not be expressed solely as probability distributions, and there is no requirement to calibrate the information sources. This provides for greater generality in our proposed information theoretic approach.

Within the second category, there are a number of approaches for computer-based decision aiding that use probability theory to integrate information. Knowledge-based expert systems typified by the work of [37], [5] and [21] all use techniques based on probability theory to integrate available information. In addition, [31] describes the use of a consensus method for resolving the conflicting information problem. However, there is a fundamental difference in purpose between these methods and our approach to the information integration problem. These systems are designed to perform their integration tasks within the confines of a well specified and tightly controlled domain. This contrasts sharply with our approach, which is domain independent, Essentially our goal is to aid in situation assessment rather than replicate a human expert.

Automated decision structuring systems unlike expert systems are not restricted to a specific domain. One of the first systems in this category was developed by [18] to construct decision trees based on inputs interactively derived from a user. [22] and [38] describe applications of this program to command and control, and group decision making. Because of the limitations of the decision tree structure Pearl, et al. ([27]) developed GODDESS. This program uses and/or graphs to structure the decision problem. Conflicting expert opinions are combined using the Delphi method. In a sense our approach is aimed at aiding situation assessment in the same fashion that GODDESS and similar systems aid in decision structuring. The emphasis here is on the specific problem of merging conflicting information. As such, our objectives may be viewed as complimentary to the automated decision structuring approaches.

## 2.2. Approaches Based on Alternative Theories of Uncertainty

Since the 1960's several theories of uncertainty have been advanced as alternatives to probability theory. In many instances there theories have been advocated as more appropriate vehicles than probability theory for integrating conflicting information. One of these, possibility theory ([46]) grew out of the notion of fuzzy sets ([45]). Prade in [28] and [29] examines this theory relative to other inference techniques with particular emphasis on the work of [33]. Goodman ([9]) proposed the application of possibility theory to the specific case of information aggregation in target tracking. However, he also uses probability theory to achieve a workable system. [30] also uses a variant of possibility theory for information fusion. From the situation assessment standpoint many of the problems evident in the decision theoretic approaches still apply. There are also problems unique to this theory. In particular, a number of lattice operators have been proposed and each has different characteristics (see [1]). The theory also rests on the assessment of membership functions. Watson, Weiss, and Donnell ([41]) indicate that the question of how to assess such values in practice has received surprisingly little attention.

Another theory that has generated considerable interest in the context of information integration is the theory of belief functions. The theory is based on the work in [35], [33], [3] and [34]. In [12] and [11] this theory was applied to combine evidence in structural damage assessment. [8], [19] and [20] investigated the use of belief functions to combine information from multiple sensors. Shafer ([36]) describes a procedure that is appropriate for a variety of information integration tasks. This procedure uses a result due to Richard Jeffrey ([15]) known as Jeffrey's rule of conditioning. A similar procedure using Jeffrey's rule is described in [4] as a means for updating subjective probabilities when Bayes' rule is not directly applicable.

Kranz and Miyamoto ([17]) consider the problem of combining evidence from two sources using belief functions. In their example one source provides frequency information while the other provides only diagnostic or case specific evidence. The implied judgmental process model correlates well with recent research reported in [40] and [16], who indicate that subjects integrate case specific information reasonably well, but fail to adequately account for frequency data. [7] considers a similar example concerned with merging a wholistic assessment and another assessment constructed from decomposed judgements.

Several problems have been noted by [19] in the application of the theory of belief functions. The first is that the theory is not appropriate when the evidence contains gross errors rather than measurement errors.

A second and more severe problem is that Dempster's rule is only applicable to bodies of evidence that are 'evidentally' independent. Evidential independence is conceptually and operationally different from statistical independence (see [33]). In practice it does not seem difficult to find evidently dependent information that needs to be aggregated (cf. [19]). No method is known for combining evidently dependent evidence.

In contrast with approaches based on these new theories, the approach described here is based on information theory and, hence, probability theory. We accrue several advantages from pursuing our investigations via information theory. First, decision theory rests on probability theory. Since situation assessment is the first step in decision making, it is extremely important that results from information integration be usable by a normative theory for alternative selection. Second, there is a large body of psychological literature describing the use, interpretation, and assessment of probabilities. Third, the theory is easily capable of describing both continuous and discrete random variables. Finally, probability is the standard method for describing uncertainty in the overwhelming majority of disciplines, both applied and theoretical.

## 3. A Relative-Entropy Approach to Information Integration

The purpose of our approach is to provide the basis for a computationally tractable and behaviorally meaningful procedure for aiding in situation assessment. This is accomplished through a formal structure for multisource conflicting information integration. In this section we describe the details of the approach.

Our formulation of the multisource conflicting information problem models information as constraints on an unknown probability distribution. This approach has several advantages.

First, it allows for the explicit incorporation of many natural language expressions of uncertainty. For example, the expression, 'For this situation I'm sure the average number of accidents will be less than one in ten years,' becomes

$$
\sum_ {i = 0} ^ {M} i q _ {i} \leq 1,
$$

where $q_{i}$ is the probability of i accidents ( $i = 0, \ldots, M$ ) over a ten year horizon. Thus, our approach can capture and formally utilize information in a variety of natural language expressions. This is a clear advantage over approaches that require extensive use of elaborate assessment mechanisms to acquire the requisite probability distributions.

A second advantage of modeling information by constraints is that it allows for imprecision in the information from the sources and in the decision maker's beliefs. This is an advantage which our approach shares with the possibilistic and belief function approaches described in the previous section. Instead of requiring the decision maker or the sources to commit to a specific probability distribution, the method we propose requires only the specification of a region believed to contain the unknown distribution. This is a marked improvement over Bayesian techniques in which assessment of complete prior distributions and likelihoods is necessary.

Our approach to the conflicting information problem is to find a merged viewpoint from the competing information sets. This is accomplished by a two step procedure. In the first step we find points which represent the minimum amount of information required to change a distribution in the decision maker's belief set to one in each of the source's information sets. The second step then finds a merged viewpoint as the point which minimizes the same information measure between the points obtained in the first step. In the remainder of this section we formally describe this procedure.

Suppose $X$ is a discrete random variable with values in $\Theta = (\theta_1, \theta_2, \ldots, \theta_m)$ . Let $q_i = \Pr(X = \theta_i)$ for $i = 1, 2, \ldots, m$ . We suppose that $q$ is desired but unknown. Now the information sources provide constraints on $q = (q_1, q_2, \ldots, q_m)$ . Suppose there are $J$ sources. Then source $k \in (1, 2, \ldots, J)$ provides information of the form

$$
\sum_ {i = 1} ^ {m} f _ {j} \left(\theta_ {i}\right) q _ {i} = 0,\tag{1}
$$

for $j = 1,2,\ldots ,r_k$ ( $r_k < n$ , otherwise the problem has a unique solution) and

$$
\sum_ {i = 1} ^ {m} g _ {j} \left(\theta_ {i}\right) q _ {i} \leq 0,\tag{2}
$$

for $j = 1,2,\ldots ,s$ .Let

$$
\Omega = \left\{q: \sum_ {i = 1} ^ {m} q _ {i} = 1; q _ {i} \geq 0 \quad \text { for } \quad i = 1, \dots , m \right\}.
$$

The constraints in (1) and (2) define subsets of $\Omega$ since the q in the constraints must be a probability vector. We label these subsets $\Psi_{1}, \Psi_{2}, \ldots, \Psi_{J}$ and refer to them as the information sets.

Conflicting information is modeled in this formalism as empty intersections between information sets. Thus, $\Psi_{i} \cap \Psi_{j} = \emptyset$ for $i \neq j$ and $i, j \in (1, \ldots, J)$ . If the intersection between information sets is not empty, then we proceed in one of two ways. Suppose $\Psi_{i}$ and $\Psi_{j} (i \neq j)$ are information sets with nonempty intersection. Then a first approach is to relabel the information sets so that $\Psi_{i'} = \Psi_{i} \cap \Psi_{j}^{c}$ , $\Psi_{j'} = \Psi_{j} \cap \Psi_{i}^{c}$ , and $\Psi_{k} = \Psi_{j} \cap \Psi_{i}$ , where $k \notin (1, \ldots, J)$ and $\Psi_{h}^{c}$ denotes the complement of $\Psi_{h}$ in $\Omega$ . A second approach redefines $\Psi_{i}$ as $\Psi_{i} \cap \Psi_{j}$ and eliminates $\Psi_{j}$ from the collection of information sets. The choice of method is strictly domain dependent. If it is important to retain all the information provided by the sources then the first approach seems more appropriate. Otherwise, only the information shared by the sources is considered relevant, and this suggests the second method. A possible third approach would consider only the information not shared by the sources to be relevant. In fact, the specifics of the domain may require a unique procedure. Regardless of the choice, the overall integration method we describe here has the generality to accommodate both conflicting and overlapping information among the sources.

Now in addition to the information sources, the decision maker also provides inputs to the integration process in the form of constraints on q. These constraints define another subset of $\Omega$ which we label $\Phi$ . For our purposes $\Phi \cap \Psi_{i} = \varnothing$ for $i = 1, \ldots, J$ . If this were not the case, then our problem would not be one of competing and conflicting information sources, since the decision maker would be in agreement with one or more of them. As it is, he or she must select an integrated viewpoint which accommodates all of the information sources. If there is overlap between the belief set of the decision maker and the information sets of the sources, then we form disjoint subsets of $\Phi \cup (\bigcup_{i=1}^{J} \Psi_{i})$ using one of the two methods suggested above. The region of overlap can then be treated as either a member of the decision maker's belief set or one of the information sets depending on the circumstances of the particular domain.

The problem then is to integrate the information represented by $\Psi_{1},\ldots,\Psi_{J}$ given the decision maker's initial beliefs, represented by $\Phi$ . Since $\Phi$ is the initial viewpoint of the decision maker, our procedure does not restrict the merged viewpoint to lie within $\Phi$ . This is a significant difference between our procedure and Bayesian methods. Instead we treat $\Phi$ as information with which to obtain points in the information sets provided by the sources to use for the merging operation.

Our procedure uses an information theoretic measure known as relative-entropy. The relative-entropy between two probability vectors, p and q is defined as

$$
I (q, p) = \sum_ {i = 1} ^ {m} q _ {i} \ln (q _ {i} / p _ {i}).\tag{3}
$$

This measure has a number of important properties that recommend its use. In particular, it satisfies axioms of information and inference [13]. For our purposes one of its most important aspects is that it measures the amount of information required to convert p into q. It has also been used by [14] as a means of updating a decision maker's prior for rare events given multiple expert opinions expressed as mean values. Our procedure generalizes the method in [14] by permitting information in the form of arbitrary constraint sets for the decision maker and the information sources.

In the first step of our procedure we find the points in each of the $\Psi_{i}$ ( $i=1,\ldots,J$ ) that minimize the relative-entropy with $\Phi$ . Specifically we minimize (3) subject to $p \in \Phi$ and $q \in \Psi_{i}$ for $i = 1, \ldots, J$ . We use $q'(i)$ for the points in the $\Psi_{i}$ at which this minimum is obtained. Thus, points are obtained which represent the minimum amount of information necessary to update a distribution in $\Phi$ to a distribution in each of the information sets.

The second step of our procedure finds an integrated viewpoint. This is done by solving for the $q^{*}$ which minimizes.

$$
\sum_ {i = 1} ^ {J} I (q, q ^ {\prime} (i)),\tag{4}
$$

For $q \in \Omega$ . The integrated solution, $q^{*}$ , represents the distribution which is minimally distant in an information sense from each of the points in the information sets found through our first step. Thus, it represents the distribution which would require the sources to make the least change and still accommodate the other sources and the decision maker's initial beliefs.

The $q^{*}$ we obtain from our procedure is unique when the information provided is expressed in terms of linear equalities and inequalities. From a practical standpoint, it is important that the solution to the integration be unique, since it can then be used in decision making. This can be accomplished in a straightforward fashion, since the machinery for doing so exists in decision theory. Uniqueness is a solution characteristic shared with several of the other integration methods surveyed in section 2. However, unlike these other methods, our approach provides a unique solution to problems where information is provided in the general form of constraint sets on probability distributions. This is significant for decision support systems where the unstructured nature of the problem domain frequently requires methods for incorporating information expressed in more general formats.

Results from recent research mentioned earlier by [40] and [16] provide strong evidence that ours is a behaviorally sound approach. Their results imply that information integration designs that separate frequency information from diagnostic or case specific information may be extremely effective. Our approach accommodates this segregation by allowing for frequency information in the initial viewpoint or decision maker's belief set, and case-specific information on the constraints of the information sets.

## 4. An Example

It is useful to illustrate the general methods of the previous section with an example. Although based on an actual risk assessment problem, the example which we describe here has been intentionally simplified to highlight the use of our technique as an integration procedure.

A large oil company plans to ship by road a hazardous petrochemical product from one of its refineries to m processing plants. This will be the first time that this particularly hazardous product has been shipped by road and, one truck with product will be sent to each of the m sites. M tank trucks have been modified to handle the product and drivers will attend a special course emphasizing the safe handling of the material. The company would like to estimate the probabilities of 0 to M serious accidents. For our purposes we do not define a serious accident but assume that the company has been able to do so in a sufficiently precise manner.

Since we are interested in the number of serious accidents which occur, this number becomes our random variable X and $\Theta=(0,1,\ldots,m)$ . Information is made available to the company from a group of insurance industry experts on the transportation of hazardous materials and by an internal group of engineers. The decision maker is the vice president in charge of the product.

The insurance industry group expresses their information in terms of the expected number of accidents. In particular, they believe that the expected number of accidents lies between 0.75 and 1.5. Letting $\Psi_{1}$ be the information set for the insurance analysts we have

$$
\Psi_ {1} = \left\{q \in \Omega : 0. 7 5 \leq \sum_ {i = 0} ^ {9}: \eta_ {i} \leq 1. 5 \right\}.\tag{5}
$$

The company's internal experts also provide a mean value estimate, namely, 0.1. They also estimate the variance for the number of accidents given this mean value to be greater than 0.1. Finally, they believe that there is a positive probability of any number of accidents (up to 9) and provide a lower bound for this probability of 1.0 $(10)^{-3}$ . This produces a second information set

$$
\Psi_ {2} = \left\{q \in \Omega : 0. 1 = \sum_ {i = 0} ^ {9} i q _ {i}; 0. 1 <   \sum_ {i = 0} ^ {9} (i - 0. 1) ^ {2} q _ {i}; \right.
$$

$$
\left. 1. 0 (1 0) ^ {- 3} \leq p _ {i} \quad \text { for } \quad i = 0, \dots , 9 \right\}.\tag{6}
$$

Finally, the decision maker (DM) provides an estimate of the requisite probabilities. Specifically, the DM believes that the probability of no accidents is twice as large as the probability of 1 accident, and four times as large as the probability of 2 accidents. He or she is uncertain about the value of the remaining probabilities, but feels that there is a one in fifty likelihood of more than two accidents. This information yields

$$
\Phi = \left\{q \in \Omega : q _ {0} = 2 q _ {1} = 4 q _ {2}; \sum_ {i = 3} ^ {9} q _ {i} = 0. 0 2 \right\}.\tag{7}
$$

It should be noted that $\Psi_{1}$ , $\Psi_{2}$ , and $\Phi$ are pairwise disjoint. Hence, for this example the information available from the different sources is conflicting.

The first step of the algorithm finds points, $p'(1)$ and $p'(2)$ in $\Psi_{1}$ and $\Psi_{2}$ , respectively, that are closest to $\Phi$ in relative-entropy. This is done by performing two minimizations. The first minimizes (3) subject to q in the $\Psi_{1}$ of (5) and p in the $\Phi$ of (7), and yields $p'(1)$ . Then (3) is minimized again for $p \in \Phi$ , but with $q \in \Psi_{2}$ given by (6). This produces $q'(2)$ . Both $q'(1)$ and $q'(2)$ for this problem are shown in table 1.

In the second step of our procedure, an integrated viewpoint is obtained. For our example this means minimizing (4) with the values given in table 1 for $q'(1)$ and $q'(2)$ . The result of this process, $q'$ , is shown in table 2. It is interesting to note that the integrated viewpoint takes account of the greater precision in estimating provided by the company's internal experts. In this example, they provided not only a precise value for the mean, but also a constraint on the variance. The solution to this problem represents the unique probability distribution that requires the least change in an information theoretic sense by the sources and also accounts for the opinion of the decision maker.

Results from the First Step of the Integration Procedure.

<table><tr><td>X</td><td> $q'(1)$ </td><td> $q'(2)$ </td></tr><tr><td>0</td><td>0.5527</td><td>0.9108</td></tr><tr><td>1</td><td>0.2813</td><td>0.0813</td></tr><tr><td>2</td><td>0.1432</td><td>0.0072</td></tr><tr><td>3</td><td>0.0010</td><td>0.0001</td></tr><tr><td>4</td><td>0.0011</td><td>0.0001</td></tr><tr><td>5</td><td>0.0011</td><td>0.0001</td></tr><tr><td>6</td><td>0.0011</td><td>0.0001</td></tr><tr><td>7</td><td>0.0011</td><td>0.0001</td></tr><tr><td>8</td><td>0.0012</td><td>0.0001</td></tr><tr><td>9</td><td>0.0162</td><td>0.0001</td></tr></table>

Table 2  
The Integrated Viewpoint.

<table><tr><td>X</td><td>q*</td></tr><tr><td>0</td><td>0.7855</td></tr><tr><td>1</td><td>0.1674</td></tr><tr><td>2</td><td>0.0357</td></tr><tr><td>3</td><td>0.0011</td></tr><tr><td>4</td><td>0.0011</td></tr><tr><td>5</td><td>0.0011</td></tr><tr><td>6</td><td>0.0012</td></tr><tr><td>7</td><td>0.0012</td></tr><tr><td>8</td><td>0.0012</td></tr><tr><td>9</td><td>0.0045</td></tr></table>

## 5. Conclusions

Methods for merging conflicting information may be classified as either using probability theory or one of several alternative approaches to the calculus of uncertainty. Within the former category most methods have concentrated on merging forecasts or probability assessments. There is a clear need for more general methods of information integration. Expert system techniques tend to be domain specific, while automated decision structuring systems lack formal methods for combining conflicting evidence from disparate sources. Among the methods using alternative theories of uncertainty, those based on the theory of belief functions have been the most numerous. However, several significant problems, most notably with evidential dependence, have restricted the use of these methods.

Given the disadvantages of current information integration methods, we have proposed a technique based on an information theoretic measure, relative-entropy. This method updates a probability mass function given information in the form of constraints. Significant characteristics of this method are

(1) It provides a behaviorally meaningful method of combining frequency data with case specific information.

(2) The approach is computationally tractable and easily implemented.

(3) Natural language expressions are explicitly used to generate constraints. Hence, formal probability assessment techniques are not required.

A decision aiding system that uses this method would essentially partition the knowledge base into a section derived from multiple and possibly conflicting sources and a section consisting of a priori information. The updating process itself is dynamic with new information from multiple sources being used to update the previous distribution.

Our research in this area is continuing. We are currently investigating methods of explicitly incorporating source reliability into the integration problem. We are also investigating the relationships between the relative-entropy approach described here and other approaches based on the theory of belief functions.

## References

[1] Bandler, W. and L.J. Kohout, Unified Theory of Multiple-Valued Logical Operators in the Light of the Checklist Paradigm; Proc. 1984 IEEE Int. Conf. Systems, Man, and Cybernetics (1984) 356–364.

[2] Dalkey, N.C., Delphi, Technical Report P-3704, The Rand Corporation (1967).

[3] Dempster, A.P., Upper and Lower Probabilities Induced by a Multivalued Mapping, Annals of Math. Stat. 38 (1967) 325–339.

[4] Diaconis, P. and S.L. Zabell, Updating Subjective Probability, J. Amer. Stat. Assoc. 77 (1982) 822–830.

[5] Duda, R.O., P.E. Hart, K. Konolige and R. Reboh, A Computer-Based Consultant for Mineral Exploration, Final Report, SRI, Menlo Park, CA (1979).

[6] Edwards, W., H. Lindman and L.J. Savage, Bayesian Statistical Inference for Psychological Research, Psychol. Review 70 (1963) 193–241.

[7] Freeling, A.N.S., Reconciliation of Multiple Probability Assessments, Organizational Behavior and Human Performance 10 (1981) 395–414.

[8] Garvey, T.D., J.D. Lowrance and M.A. Fischler, An Inference Technique for Integrating Knowledge from Disparate Sources, Proceedings Int. Joint Conf. on Artificial Intelligence, Vancouver (1981).

[9] Goodman, I.R., PACT: Possibilistic Approach to Correlation and Tracking; proc. 16th Asilmar Conf. Circuits, Systems and Computers 259–363.

[10] Harper, W.L., Rational Conceptual Change, Philosophy of Science Association 2 (1977) 462–494.

[11] Ishizuka, M., K.S. Fu and J.T.P. Yao, Inference Procedures under Uncertainty for the Problem-Reduction Method, Information Sciences 28 (1982) 179–206.

[12] Ishizuka, M., K.S. Fu and J.T.P. Yao, SPERIL: An Expert System for Damage assessment of Existing Structures, Proceedings 6th Intl. Conf. on Patt. Recog. (1982) 932–937.

[13] Shore, J.E. and R.W. Johnson, Axiomatic Deviation of the Principle of Maximum Entropy and the Principle of Minimum Cross-Entropy, IEEE Transactions on Information Theory, IT 27 (1981) 472–482.

[14] Sampson, A.R. and R.L. Smith, Assessing Risks Through the Determination of Rare Event Probabilities, Operations Research 30 (1982) 839–866.

[15] Jeffrey, R.C., The Logic of Decision, Mc-Graw-Hill, New York (1965).

[16] Johnson, E.S., Expertise and Decision Making Under Uncertainty: Performance and Process, in: M. Chi, R. Glaser and M. Fall, eds., The Nature of Expertise (1985) forthcoming.

[17] Kranz, D.H. and Miyamoto, J., Priors and Likelihood Ratios as Evidence, Journal of the American Statistical Association 78, no 303f (1983) 418–423.

[18] Leal, A. and J. Pearl, An Interactive Program for Conversational Elicitation of Decision Structures, IEEE Transactions on Systems, Man, and Cybernetics SMC-7, No. 5 (1977) 368–376.

[19] Lowrance, J.D. and T.D. Garvey. Evidential Reasoning: A Developing Concept, Proc. IEEE Conf. Cybernetics and Society (1982) 6–9.

[20] Lowrance, J.D. and T.D. Garvey Evidential Reasoning: An Implementation for Multisensor Integration, SRI International Technical Note 307, Palo Alto, CA (1983).

[21] McDermott, J., R1: The Formative years, AI Magazine 2(2) (1981) 21-29.

[22] Merkhofer, M., A. Mitler, B. Robinson and R. Korsan, Decision Structure Aid: Characterization and Preliminary Implementation, SRI, Menlo Park, CA (1977).

[23] Morris, P.A., Decision Analysis Expert Use, Management Science 20 (1974) 1233–1241.

[24] Morris. P.A., Combining Expert Judgments: A Bayesian Approach, Management Science 23 (1977) 679–693.

[25] Morris. P.A., An Axiomatic Approach to Expert Resolution, Management Science 29 (1983) 24–32.

[26] Okrent, D., A General Evaluation Approach to Risk-Benefit for Large Technological Systems and Its Application to Nuclear Power, NSF Project GI-39416 Final Report, School of Engineering and Applied Science, UCLA (1977).

[27] Pearl, J., A. Leal and J. Saleh, GODDESS: A Goal-Directed Decision Structuring System, IEEE Transactions on Pattern Analysis and Machine Intelligence PAMI-4, No. 3 (1982).

[28] Prade, H., A Synthetic View of Approximate Reasoning Techniques, Inter. Joint Conference on Artificial Intelligence, Karlsruhe, Germany (1983) 130–136.

[29] Prade, H., A Computational Approach to Approximate and Possible Reasoning with Applications to Expert Systems, IEEE Trans. Pattern Analysis Machine Intell PAMI-7 (1985) 260–285.

[30] Rauch, H.E., Probability Concepts for an Expert System Used for Data Fusion, Artificial Intelligence (1984) 53–60.

[31] Reboh, R., Extracting Useful Advice from Conflicting Expertise, Int. Joint Conf. on Artificial Intelligence, Karlsruhe, Germany (1983) 145–150.

[32] Schervish, M.J., Combining Expert Judgments, Technical Report No. 294, Department of Statistics, Carnegie-Mellon University, Pennsylvania (1983).

[33] Shafer, G., A Mathematical Theory of Evidence, Princeton Univ. Press (1976).

[34] Shafer, G., Allocations of Probability, Ann. Prob. 7(5) (1979) 827–839.

[35] Shafer, G., Constructive Probability, Synthese 48 (1981a) 1–60.

[36] Shafer, G., Jeffrey's Rule of Conditioning, Philosophy of Science 48 (1981) 337–362.

[37] Shortliff, E. and B. Buchanan, A Model of Inexact Reasoning in Medicine, Mathematical Biosciences 23 (1975) 351–379.

[38] Steeb, R. and E. Johnston, A Computer Based Interactive System for Group Decision Making, IEEE Trans. Systems, Man, and Cybernetics, SMC-11 (1981).

[39] U.S. Nuclear Regulatory Commission, Reactor Safety Study, An Assessment of Accident Risks in U.S. Commercial Nuclear Power Plants, WASH 1400 (NUCREG 75/014), Washington, DC (1975).

[40] Ward, S.L., Comparison of Several Alternative Models for Subjective Estimates, Proc. IEEE Intl. Conf. Cybernetics and Society (1982) 214–217.

[41] Watson, S.R., J.J. Weiss and M.L. Donnell, Fuzzy Decision Analysis, IEEE Trans. Systems, Man, and Cybernetics, SMC-9 (1979) 1–9.

[42] Winkler, R.L., The Consensus of Subjective Probability Distributions, Management Science 15 (1968) B-61 through B-75.

[43] Winkler, R.L., Combining Probability Distributions from Dependent Information Sources, Management Science 27 (1981) 479–488.

[44] Winkler, R.L. and S. Makridakis, The Combination of Forecasts, J. Royal Statist. Soc. A, 146 (Part 2) (1983) 150–157.

[45] Zadeh, L.A., Fuzzy Sets, Memo ERL, No. 64-44, University of California, Berkeley, CA (1964).

[46] Zadeh, L.A., Fuzzy Sets as a Basis for a Theory of Possibility, Int. J. Fuzzy Sets Systems 1 (1978) 3–28.
