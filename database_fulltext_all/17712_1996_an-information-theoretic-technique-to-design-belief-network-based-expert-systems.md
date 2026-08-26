---
otero_id: 17712
otero_key: "34YBYHFR"
title: "An information theoretic technique to design belief network based expert systems"
authors: "Sumit Sarkar; Ram S. Sriram; Shibu Joykutty; Ishwar Murthy"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00020-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An information theoretic technique to design belief network based expert systems

Sumit Sarkar ${}^{a,1}$ , Ram S. Sriram ${}^{b}$ , Shibu Joykutty ${}^{a}$ , Ishwar Murthy ${}^{a}$

$^{a}$ Department of Information Systems and Decision Sciences, College of Business Administration, Louisiana State University,

Baton Rouge, LA 70803, USA

$^{b}$ School of Accountancy, Georgia State University, Atlanta, GA 30303, USA

## Abstract

This paper addresses the problem of constructing belief network based expert systems. We discuss a design tool that assists in the development of such expert systems by comparing alternative representations. The design tool uses information theoretic measures to compare alternative structures. Three important capabilities of the design tool are discussed: (i) evaluating alternative structures based on sample data; (ii) finding optimal networks with specified connectivity conditions; and (iii) eliminating weak dependencies from derived network structures. We have examined the performance of the design tool on many sets of simulated data, and show that the design tool can accurately recover the important dependencies across variables in a problem domain. We illustrate how this program can be used to design a belief network for evaluating the financial distress situation for banks.

Keywords: Belief networks; Expert systems; Information theory; Knowledge acquisition; Probabilistic reasoning

## 1. Introduction

The representation of uncertainty, and its subsequent manipulation, has become an important issue in expert systems. Different uncertainty calculi that have been proposed for this task include probability theory $[8,23]$ , the Dempster–Shafer theory of evidence $[32]$ , the certainty factor calculus $[33]$ , and fuzzy set theory $[42]$ . Each of these calculi have their relative advantages and disadvantages over the other ones, and the choice of a calculus often depends on the task that is being represented in an expert system. Among the different belief calculi, probability theory has the richest historical and philosophical foundations for representing uncertainty [5,11,16]. Probability measures have a sound theoretical basis, and provide a meaningful communication tool for representing uncertainty. For example, the statement “the probability that it will rain today is 0.6” can be easily interpreted; other uncertainty measures do not have an equally well-understood interpretation. Subsequently, probability measures can be empirically tested, which is not possible for any of the other measures. For this reason, many researchers have addressed the problem of representing beliefs in expert systems using probability measures [10,33]. An important drawback has been that traditional rule-based expert systems, which are very appropriate for representing deterministic knowledge, have been shown to have some severe limitations for representing uncertainty using a probability calculus $[13,31]$ . It has been shown in recent years that belief networks provide a theoretically consistent representation scheme for capturing uncertainty using probability measures $[21,24]$ .

Consider the example of an investor assessing a firms profitability based on the financial ratios Return on Assets (ROA) and Return on Equity (ROE). In practice, observing a set of values for the ratios ROA and ROE usually does not allow the investor to categorically determine whether a firm is consistently profitable or not. Instead, the observed ratios either strengthen or weaken the investors' belief that the firm is profitable. This relationship between the firms' profitability and its ratios ROA and ROE can be represented using a belief network as shown in Fig. 1. In a belief network, the nodes correspond to the different variables of interest (e.g., ROA, ROE and Profitability in this example). Each variable is categorical in nature; for each candidate firm ROA and ROE are either above the industry average or below the industry average, respectively, while Profitability is considered to be either Good or Poor.

Each variable in the belief network has a probability distribution associated with it. The arcs in the network signify dependencies between the linked variables. When a variable has one or more parent nodes in the network, then the probability distribution for that variable is stored conditioned on all combinations of the outcomes of its parent variable(s). Since the variable ROA does not have any parent node in Fig. 1, the probability distribution associated with it is the prior probability for each outcome of that variable. The variable Profitability has two parents, and, therefore, the distribution associated with it is conditioned on all the possible outcomes of ROA and ROE. Thus, the first element of the left column in the matrix is the probability that a firms' Profitability is Good when both ROA and ROE are above average. Similarly, the second element in the left column is the probability that a firms' Profitability is Good, when ROA is above average and ROE is below average, etc. The probability that the firms' Profitability is Poor for different outcomes of ROA and ROE are indicated in the right column. Representing uncertainty using probabilities as shown allow them to be used for making inferences about some variable of interest, based on observing the value(s) of one or more other variables. For example, if the ratio ROA for a firm is observed to be above average, then the distributions stored in the network can be used to evaluate the revised belief that the firms' Profitability is Good. This, then, is the way a belief network is used as an expert system. The interested reader is referred to Ref. [24] for details of belief propagation techniques in network structures.

Designing a belief network for a problem domain requires identification of the structure of the network, followed by specification of the conditional and prior probabilities for the variables in the network. To obtain the desired structure, experts have to identify the important determinants for each variable of interest in the problem domain. Subsequently, the probability parameters that are required to specify the underlying dependencies are elicited from domain experts. In practice, this is a hard problem. While experienced domain experts can often provide good probability estimates [41], nevertheless, obtaining a complete and consistent set of prior and conditional probabilities for all required dependencies is usually very difficult. Furthermore, humans (even domain experts) can demonstrate many forms of biases in their judgments [40,41]. Therefore, in order to obtain accurate assessments, knowledge engineers need to be trained in probability elicitation techniques. Both domain experts and knowledge engineers are often expensive resources for an organization, and elicitation of probabilistic knowledge requires a large investment of time and effort on their part. Usually, the expert(s) would like to consider many alternative feasible structures for representing a problem domain. In order to evaluate such structures, additional probability parameters are needed to completely specify each structure. This drastically increases the number of probability parameters that the expert(s) must provide, which substantially adds to the knowledge elicitation costs. Furthermore, it increases the likelihood of more inconsistencies across the probability parameters obtained. Often, the expert is simply unable to provide accurate estimates for so many different probability parameters. Subsequently, choosing the most appropriate structure is usually done in an ad-hoc manner. The focus of this research then is to develop a systematic method for designing belief network structures that successfully overcomes the above difficulties.

![](/api/attachments/34YBYHFR/fulltext/images/2d32819e7ba15a8aa6c4866c25c3fcae341a80572fd370685746a12ce576a885.jpg)  
Fig. 1. Representing probabilistic dependencies in a belief network.

The objectives of this paper are twofold. First, we discuss a design tool that uses rigorous analytical techniques to assist in the development of belief network based expert systems. The design tool is a program that has been developed in C. The techniques incorporated in the program are based upon a prior body of theoretical work for comparing alternative structures $[29,30]$ . The prior research has shown that the well-known mutual information measure is appropriate for evaluating belief network structures. The design tool uses this mutual information measure to compare different structures, when the underlying probability distribution across variables in the network is known. The program can also be used to estimate the necessary probability parameters from sample data. This is of particular interest, since large volumes of historical data are available in computerized form for many business applications. Such data reflects probabilistic dependencies across entities of interest in their respective problem domains, and can serve as an important source of knowledge for building belief-network based expert systems. Further, using such data for estimation purposes can greatly reduce the burden of eliciting probability estimates from experts when designing such systems. This point is crucial, since, as discussed earlier, it is often infeasible to obtain a large number of probability estimates that are reliable and consistent from the experts alone. Three important capabilities of the design tool are discussed: (i) evaluating alternative structures based on sample data; (ii) finding optimal networks with specified connectivity conditions; and (iii) eliminating weak dependencies from derived network structures. These capabilities are demonstrated on simulated data obtained by generating random samples from known network structures with specified probability distributions. We have examined the performance of the design tool on many additional sets of simulated data that are obtained from network structures that are themselves randomly generated. The design tool is shown to be fairly accurate in recovering from sample data the underlying dependencies across variables in a problem domain.

The second objective of this paper is to show how the design tool can be used to design a belief network based expert system for a real-world application. We address the decision problem faced by auditors in examining the financial viability of banks. An important practical requirement for a belief network based system is that it should represent the important dependencies across variables in the problem domain in a parsimonious manner for efficient belief propagation (i.e., only the essential dependencies should be stored by the system). We show how variables that are not directly measurable (called latent variables) can be used to obtain efficient structures. The use of latent variables help in obtaining structures that are consistent with an experts' reasoning process. The design tool is used to obtain computationally efficient network structures that are strongly supported by the sample data.

The rest of the paper is organized as follows. Section 2 discusses the information theoretic techniques that form the basis for comparing alternative representations. In Section 3, we discuss the capabilities of the design tool that is used to compare alternatives. Experiments conducted to examine the performance of the design tool are also presented in this section. In Section 4, we discuss the problem of evaluating financial distress for banks, and demonstrate how the design tool can be used to build a belief network for this application. Concluding remarks are presented in Section 5.

## 2. Evaluating belief network structures

In this section, we provide a summary of theoretical results obtained in prior research that form the basis for comparing alternative belief network representations $[29,30]$ . We first discuss the choice of an appropriate measure for performing the desired comparisons, and then discuss two important results that lead to a computationally tractable technique for comparing alternatives.

## 2.1. Theoretical considerations

A belief network structure represents a joint distribution over the different variables in the

STRUCTURE I  
![](/api/attachments/34YBYHFR/fulltext/images/3f4e234f22c144c57dd7d8ad1236e09785c4521ce2983864fd9dea5e1ba4b913.jpg)

![](/api/attachments/34YBYHFR/fulltext/images/2bb8920ef2ff1fbc0f6465b9ce88bdf5e0f3f90de2103f72363fde70493faaf0.jpg)  
STRUCTURE II

Fig. 2. Two alternative network structures.

network. The joint distribution can be represented as a product of the conditional and prior probabilities used to specify the network. For instance, the portion of the belief network shown in Fig. 1 can be represented by the following product form:

$$
P (\text { Profitability }, \text { ROA }, \text { ROE })
$$

$$
\begin{array}{r l} & = P (\text { Profitability } | \mathrm{ROA}, \mathrm{ROE}) \\ & \times P (\mathrm{ROA}) P (\mathrm{ROE}). \end{array}
$$

In general, for a problem with variables $X_{1},\ldots ,X_{n}$ , the product form is given by:

$$
P \left(X _ {1}, \dots , X _ {n}\right) = \Pi_ {i = 1, n} P \left(X _ {i} \mid F \left(X _ {i}\right)\right).
$$

$F(X_{i})$ refers to the set of parent variables for $X_{i}$ . For variables with no parents, $F(X_{i}) = \emptyset$ , which indicates that the marginal probabilities are stored for those variables.

For illustration, consider the two structures shown in Fig. 2 as candidate networks for representing the important dependencies across variables $X_{1}$ , $X_{2}$ , $X_{3}$ , $X_{4}$ and $X_{5}$ . For the moment, we assume that the complete underlying probability distribution over all the variables in the network is available (we subsequently show how this assumption can be relaxed in practice). Usually, the complete joint distribution cannot be used in its entirety because of the enormous number of probability parameters that would have to be stored and manipulated. In order to choose between the two alternatives, we must determine the best set of probability parameters for each structure, and then evaluate the structures by comparing the probability parameters associated with each structure with the true underlying distribution, respectively. We need a measure that we can use to determine the best set of probability parameters for each structure, as well as, to compare alternative structures.

Measures used to compare probability distributions are called scoring rules [37]. The expected score associated with a feasible alternative, $S(\underline{p},\underline{r})$ , is a function of the vectors p and r, where p denotes the true distribution (expressed as a vector of the probability masses corresponding to the different states that each variable may have), and r the distribution associated with the alternative. A scoring rule is said to be proper if $S(\underline{p},\underline{p}) \geq S(\underline{p},\underline{r})$ . This implies that assessments other than p cannot get a higher score than $\underline{p}$ itself. Among the various possible proper scoring rules, three that have received particular attention in the literature are: (i) the quadratic scoring rule [6]; (ii) the logarithm scoring rule [12]; and (iii) the spherical scoring rule [26]. A requirement often imposed on a scoring rule is that the score depend only on the probability assigned to the event that is actually realized (called the principle of relevance [37]). For instance, in a three event state space, the two assessments (0.6, 0.3, 0.1) and (0.6, 0.2, 0.2) should receive the same score if the first event was realized (if one of the other two events were to occur, the two assessments would get different scores). The logarithm rule is the only proper scoring rule that satisfies this requirement for any arbitrary distribution [37]. It has been shown that using the logarithm rule is equivalent to using the I-Divergence measure commonly used in communication theory [15]. Sarkar et al. [29] have performed an experimental comparison of the logarithm and the quadratic rule over a large range of probability distributions and loss parameters, and show that the results obtained using the logarithm rule are usually better than those obtained using the quadratic rule.

For the above reasons, the logarithm rule is deemed appropriate for comparing alternative belief network representations. The logarithm rule evaluates the distance between the true distribution and the distribution associated with a feasible network structure using the formula shown:

$$
S (\underline {{p}}, \underline {{r}}) = - \sum_ {i} p _ {i} \log r _ {i}.\tag{i}
$$

A high score is preferred as it indicates that r is close to p. The score is maximized when the distributions p and r are identical. We state a result that allows us to obtain the “best” set of probability parameters for a given structure in a simple and intuitively appealing manner.

Result 1: When using the logarithm rule, the best set of probability parameters that correspond to a given topology T is one where $P_{T}(X_{i}|F(X_{i})) = P(X_{i}|F(X_{i}))$ for all i.

The above result is obtained by deriving the optimality conditions for maximizing the logarithm score associated with a given network structure (a formal proof of this result is shown in [30]). Thus, for Structure I in Fig. 2, the optimal conditional probability distribution associated with variable $X_5$ for that structure is obtained by estimating the true conditional probability distribution $P(X_5|X_3,X_4)$ . This result will hold irrespective of the rest of the network structure. Subsequently, the full joint distribution for that structure is obtained by independently estimating the different conditional and marginal probability distributions that constitute the product-form for the structure. The complete true distribution underlying the problem domain is not required; only the relevant conditional and marginal distributions need to be evaluated. Estimating the conditional and marginal probabilities can be done much more easily and with greater accuracy than estimating a complete joint distribution.

Once the probability parameters are obtained, then the two structures can be compared to each other by evaluating the logarithm measure associated with each structure, and choosing the one with a higher score (as shown in Eq. (i)). It has been shown that the mutual information across the conditioned and conditioning variables for each term that appears in the product-form can be used to compare the two structures [30]. The mutual information between variables $X_{i}$ and $F(X_{i})$ is defined as [15]:

$$
\begin{array}{r l} & I \big (X _ {i}; F (X _ {i}) \big) \\ & = \sum_ {X _ {i}, F (X _ {i})} P \big (X _ {i}, F (X _ {i}) \big) \\ & \times \log \frac {\big (P \big (X _ {i} , F (X _ {i}) \big)}{P (X _ {i}) \cdot P \big (F (X _ {i}) \big)}. \end{array}
$$

The mutual information $I(X_{i};F(X_{i}))$ represents the amount of information contributed by the variables $F(X_{i})$ about variable $X_{i}$ . The best topology is characterized as follows:

Result 2: The structure with a higher logarithm score is the one that has a higher sum of mutual information terms for components of the product-form distribution, i.e., the topology with a higher $\sum_{i=1,n} I(X_i; F(X_i))$ .

As a result, a structure is preferred if the set of variables that constitute the conditioning (parent) variables are highly informative about the child variable, for each component of the product-form. The evaluation function, $\Sigma_{i=1,n} I(X_{i};F(X_{i}))$ , is linearly separable in the mutual information terms associated with each variable. Therefore, if two alternative structures differ only in the parent sets associated with one node in the network, then the only mutual information terms needed for comparing the two structures are those associated with that node. Thus, the two structures shown in Fig. 2 can be compared by evaluating just the expressions $I(X_{5};X_{3},X_{4})$ and $I(X_{5};X_{2},X_{3})$ from the underlying distribution, and then choosing the structure with the higher associated mutual information term. This is intuitively appealing since different structures are compared only on the basis of the differences in their structures. More generally, the above result allows us to identify the right parent set for each node of the network, independent of the rest of the network. Therefore, a potentially hard problem (in terms of combinatorial possibilities) is rendered relatively easy by this decomposition. The only constraint is that there be no cycles in the network, since that is not a legitimate representation for any underlying joint distribution.

Using the mutual information measure can also help to detect the right set of dependencies that exist across variables in a network. In the example networks shown in Fig. 2, both the variables $X_{3}$ and $X_{4}$ depend on variable $X_{1}$ . Usually, the variables $X_{3}$ and $X_{4}$ would display a mutual dependence in such a situation (i.e., $I(X_{4};X_{3})>0$ ). However, when the mutual information measure is being used, then considering both $X_{1}$ and $X_{3}$ as a parent set for $X_{4}$ evaluates as exactly the same as when only $X_{1}$ is considered as a parent for $X_{4}$ , i.e., $I(X_{4};X_{1},X_{3})=I(X_{4};X_{1})$ . This property of the mutual information measure is used to eliminate spurious dependencies from showing up in a network structure.

## 3. A design tool to evaluate belief networks

In this section, we discuss the design tool that uses the analytic results to compare alternative network structures. The design tool is a program developed in C that can be used in several different ways to assist developers of belief network based expert systems. We first discuss the three important capabilities of the design tool in assisting users to obtain belief networks: (i) evaluating alternative structures based on sample data; (ii) finding optimal networks with specified connectivity conditions; and (iii) eliminating weak dependencies from derived network structures. These features are demonstrated on simulated data obtained by generating random samples from known network structures with specified probability distributions. We have examined the performance of the design tool on many additional sets of simulated data. These simulated data sets are obtained from network structures that are themselves randomly generated. Finally, we also present the results of experiments that illustrate how well the design tool is able to recover from sample data the important dependencies across variables in a problem domain.

## 3.1. Evaluating alternative structures based on sample data

The design tool requires as input the number of different variables being considered for inclusion in a network structure, the maximum number of realizations that each variable may have, and a collection of records where each record stores the actual realizations of all the variables of interest for each instance of a problem. This collection of records constitutes the sample data for the problem domain, and is made available to the program through external data files. The design tool prompts the user to provide alternative feasible structures that are to be considered. Using a question answer interface, it requires the user to specify the parent set for each variable included in a structure. The user can compare multiple network structures at a time. For each suggested topology it does the following. It evaluates the mutual information term associated with every variable and its corresponding parent set. This is accomplished by estimating from the sample data the necessary conditional and marginal probabilities associated with that variable. It then uses the sum of the mutual information terms to compare a topology with other suggested topologies, and identifies the structure with the highest value. The program also provides estimates for prior and conditional probabilities associated with different nodes for the selected structure.

![](/api/attachments/34YBYHFR/fulltext/images/b5be593b6be22fb65d3238e8a2feb7d559c851f04d3beb6bdaeb71f832e0c813.jpg)  
Fig. 3. A network structure used to generate sample data.

The program also allows users to evaluate alternative parent sets for a variable without requiring users to specify complete topologies. We have used this feature to examine the performance of the program on data sets generated from many different network structures. One structure used for this purpose is shown in Fig. 3. Each variable in this network can take on up to 3 different values. The network has a known probability distribution associated with it. Sample data was generated from this distribution using Monte Carlo simulation, where each sample (record) consisted of a single realization of each of the variables in the network. We used the program to determine, based on the sample data, whether variable $X_4$ was more strongly dependent on variable $X_1$ or on variable $X_2$ (i.e., does $X_1$ make a better predictor for $X_4$ , or does $X_2$ ?). The program evaluated $I(X_4; X_1)$ and $I(X_4; X_2)$ by estimating the necessary conditional and marginal probabilities from the sample data. We performed such a comparison using as few as 250 samples to estimate the necessary probability parameters. The program correctly identified $X_2$ as the parent for $X_4$ . Similarly, when three feasible parents, $X_1$ , $X_2$ and $X_3$ , were examined for variable $X_7$ , the program correctly selected $X_3$ as the best parent variable. Proceeding in a similar manner, we have been able to reconstruct the complete network by finding the best set of parent variables for each node, one at a time.

## 3.2. Finding the best degree-constrained network structure

Quite often, an important pragmatic requirement for an expert system is that it should perform its reasoning in a specified time frame. The response time for belief network based expert systems is critically dependent on the number of parent variables that nodes are allowed to have in the network. This is so because the complexity of belief revision algorithms are exponential in the size of the largest parent set in a network [17]. We call the size of the largest parent set in a network as the degree of the network.

When the desired response time is stringent, then it is necessary to limit the allowable degree of belief networks that are considered for implementation. The second capability of the design tool is to assist users in obtaining the best degree-constrained network representation. In this mode, the design tool prompts users to provide the following information: (i) the allowable degree of networks to consider; and (ii) for each variable, the set of other variables from which its parent set may be drawn. Based on this user provided information and the sample data, the program identifies the best degree-constrained network structure as follows. For each variable, the program generates all feasible parent sets that include the specified number of variables. It evaluates the mutual information measure for each parent set, and selects the parent set that is most informative for the variable under consideration. Repeating this process for all variables in the network, it arrives at the best solution.

One of the network structures used to test this feature of the design tool is shown in Fig. 4. The prior and conditional distributions associated with variables in this network were specified, and sample data generated as before. The program was instructed to find the best structure with a degree constraint of 2 (which is the degree of the true network as well). For variable $X_{4}$ , the parent set was selected from $\{X_{1}, X_{2}, X_{3}\}$ , for $X_{5}$ it was selected from $\{X_{1}, X_{2}, X_{3}, X_{4}\}$ , and for $X_{6}$ it was selected from $\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}\}$ (i.e., all lexicographically preceding variables). When a sample size of 100 was used to estimate probability parameters, the program selected the right parent sets for $X_{4}$ and $X_{5}$ . For $X_{6}$ , it selected $(X_{3}, X_{4})$ instead of the true parent set $(X_{2}, X_{3})$ . When the sample size was increased to 500, it detected the correct parent set for $X_{6}$ as well.

![](/api/attachments/34YBYHFR/fulltext/images/17eb7b2763cd84cbec6edd16c4add6bd70c0a263e33752ffe1811f5fd8eabede.jpg)  
Fig. 4. Second test network.

## 3.3. Eliminating weak dependencies from derived network structures

The third capability of the design tool is to eliminate insignificant dependencies from the network. While the degree constraint ensures that belief network structures under consideration are efficient for making inferences, the structure may nevertheless include redundant arcs across some of the nodes. This is because in practice, we may not know beforehand the exact number of parent variables that each variable should have. If the degree constraint is larger than the number of truly predictive variables for a node in the network, then the program would identify as many variables in the parent set as the degree will allow. In theory the mutual information test should exactly identify only those parents that contribute additional information. However, it is not possible to identify independence and conditional independence properties in an exact manner when estimating probabilities from samples. For instance, sampling errors lead to the mutual information conveyed by two parent variables to be usually more than that conveyed by either one of the two taken individually, even for those variables that have only one parent in the original network. Therefore, when identifying the parent set for a variable, we wish to include those variables that can significantly contribute additional information about that variable.

The design tool eliminates weak dependencies in the network by performing a significance test on the mutual information terms associated with having additional variables in parent sets of nodes in the network. The likelihood-ratio chi-square test is appropriate for this purpose. When used in this mode, the program prompts the user to specify the set of feasible parent variables for each node in the network. The following procedure is used for each node in the network. The program first considers all parent sets that consist of a single variable and finds the one that is most predictive. The selected variable is tested for significance by comparing the mutual information term against the chi-square value for the appropriate degree of freedom. The applicable degree of freedom depends on the number of possible realizations of the parent variable being considered, and is evaluated by the program. The program performs the significance test at the 5% significance level. If the mutual information term is not found to be significant, then the program concludes that the node under consideration should have no parent. If the mutual information term is significant, the program stores the predictive variable as the best parent set of size 1. The program then finds the best two variable parent set. The difference in the mutual information terms for the different parent sizes is tested using the chi-square value for the appropriate degree of freedom (which now depends on the number of possible realizations for each of the two parent sets being compared). The process is repeated until increasing the number of variables in the parent set does not lead to a significant increase in the mutual information value.

We have tested this capability of the design tool on data generated from the network shown in Fig. 3. The parent set for each variable was chosen from its lexicographically preceding variables. When 100 sample records were used, the program excluded the three arcs $(X_{1}, X_{3})$ , $(X_{1}, X_{5})$ and $(X_{2}, X_{5})$ at the 5% significance level. At the same time, it included arc $(X_{3}, X_{5})$ although $X_{3}$ was not a parent of $X_{5}$ in the true distribution. The program identified the exact set of parent variables for each node in the network when 500 sample records were used instead to estimate the different probability parameters.

## 3.4. Performance evaluation of the design tool

In the preceding sections, we demonstrated the ability of the design tool to recover underlying network structures for two small sized problems. Subsequently, we conducted extensive experiments to examine how the program works for problem sizes ranging from 10 nodes to 30 nodes. The experiments were performed using many different belief network structures for each problem size. The accuracy of the design tool was measured in terms of how “close” network structures obtained from the program were to network structures that were used to generate sample data.

The belief network structures used in the experiment were themselves randomly generated using another program (which is called the generating program). Binary variables were considered for the generated networks. For the generated structures, each variable was allowed to have up to 4 variables in its parent set. For a given problem size, the generating program first randomly generated the number of realizations that each variable may have. Then, for each variable the program randomly generated the number of parents (within the specified size restrictions). For each node, based on its randomly generated parent size, the program randomly identified the parent variable set from the other variables. In order to eliminate cycles in the structures that were generated, the feasible parent set for each node was restricted to its lexicographically preceding variables. Once the structure was specified for a network, it was used to randomly generate probability distributions associated with each node in the network. For variables with no parents, only the prior probability distributions were needed. For variables with parents, the conditional probability distributions were generated for each possible realization of its parent set. Finally, based on these prior and conditional probability distributions, the sample data was randomly generated for each variable in the network.

The sample data was then used as input for the design program. The design program was also provided with the following information: (i) the lexicographic order of the variables, (ii) the number of realizations for each variable in the network, (iii) the number of variables constituting the parent of each variable in the network, and (iv) the true parent set for each variable in the network. Sample data from ten different networks were generated for each problem size, and the accuracy of the design tool was averaged over these instances. The design tool was tested in two different ways. First, it was used to identify from a nodes' lexicographically preceding variables, the best set of parents corresponding to the true size of its parent set. This enabled us to examine how accurately the design tool could compare alternative parent sets of the same size given different samples sizes. Table 1 summarizes the performance of the design tool for this test. Each row in the table corresponds to a combination of problem size (in number of nodes) and sample size (in number of records used to estimate probabilities). The performance of the design tool is reflected by the number of arcs correctly identified by the design tool for each such combination. The last column in Table 1 represents the percentage of arcs that were correctly detected on average.

Table 1  
Performance of design tool when parent sizes are known

<table><tr><td>Problem size (# of nodes)</td><td>Sample size</td><td>Average # of arcs in network</td><td>Avg. # of arcs correctly detected</td><td>% Accuracy</td></tr><tr><td rowspan="4">10</td><td>100</td><td>16.0</td><td>11.1</td><td>69.4%</td></tr><tr><td>500</td><td>15.1</td><td>13.9</td><td>92.0%</td></tr><tr><td>1000</td><td>15.8</td><td>14.7</td><td>93.0%</td></tr><tr><td>2000</td><td>15.1</td><td>14.2</td><td>94.0%</td></tr><tr><td rowspan="4">20</td><td>100</td><td>38.8</td><td>22.7</td><td>58.5%</td></tr><tr><td>500</td><td>38.1</td><td>35.1</td><td>92.1%</td></tr><tr><td>1000</td><td>36.2</td><td>34.4</td><td>95.0%</td></tr><tr><td>2000</td><td>40.0</td><td>39.5</td><td>98.8%</td></tr><tr><td rowspan="4">30</td><td>100</td><td>63.6</td><td>29.2</td><td>45.9%</td></tr><tr><td>500</td><td>65.1</td><td>56.4</td><td>86.6%</td></tr><tr><td>1000</td><td>65.7</td><td>63.0</td><td>95.9%</td></tr><tr><td>2000</td><td>68.0</td><td>67.1</td><td>98.7%</td></tr></table>

The results in Table 1 clearly indicate that the design tool is very accurate in predicting the true parent variables of different nodes in a network for samples consisting of 500 or more records. Further, the performance was found to be equally good for networks of all the three sizes that were examined.

Next, the design tool was used to identify the set of significant parent variables for each node in a network. This enabled us to examine how accurately the design tool could identify the exact parent set when testing for statistical significance given different sample sizes. In our experiments, we allowed for a 5% Type 1 error, or a 95% confidence level. The accuracy of the design tool was averaged over ten instances as before. Table 2 summarizes the performance of the design tool for this test. Once again, when sample sizes of 500 or more records were available, the design tool could recover around 90% of all the arcs in a network. In addition to the arcs correctly identified, this table also indicates the number of additional arcs indicated by the program, as well as the number of existing arcs that were dropped by the program. While few arcs were missed out on average for sample sizes of 500 or larger, a relatively larger number of extraneous arcs were picked up by the program (ranging from 6% to 47% of the number of arcs in a network). Further, the number of extraneous arcs increased as the size of the network grew larger. A possible explanation is that for larger networks, there are many more feasible parent sets (of any given size), and, hence, more opportunities to pick redundant arcs in the network.

The experimental results indicate that when the parent sizes are available to the design tool, it is very good at recovering the right structure. Further, the program accomplishes that with relatively small sample sizes. Thus, if the design tool is used to compare alternative structures specified by an user, then it is very reliable in identifying the better network structure. Similarly, when it is used to obtain degree-constrained network structures, it identifies optimal structures very accurately. However, when used to identify the statistically significant parent variables for each node, it is less accurate. The ability to detect existing arcs improves with the size of sample data as is to be expected. However, increasing the sample size does not seem to significantly affect the number of extraneous arcs selected by the program. The analysis indicates that the design tool is not as reliable when selecting parent sets for individual variables based on significance tests than when it is used to compare alternatives.

## 4. Constructing belief networks for evaluating financial distress in banks

The experiments described in the previous section show that the techniques we use are quite robust for evaluating alternative structures. The implemented program makes it relatively easy to evaluate belief network structures that represent different dependencies across variables in a problem domain. In this section, we show how the design tool can be used to design a belief network structure for the decision problem faced by auditors when examining the financial viability of banks. We briefly describe the problem environment, and discuss why a belief network representation could be appropriate for this task. We then show how the use of latent (unmeasurable) variables help in obtaining parsimonious models. Finally, we illustrate how a belief network can be generated for such an application with the help of the design tool.

Table 2  
Performance of design tool when parent sizes are not known

<table><tr><td rowspan="2">Problem size (# of nodes)</td><td rowspan="2">Sample size</td><td rowspan="2">Average # of arcs in network</td><td colspan="2">Arcs correctly detected (5% level)</td><td colspan="2">Arcs added incorrectly (5% level)</td><td colspan="2">Arcs deleted incorrectly (5% level)</td></tr><tr><td>Avg. #</td><td>%</td><td>Avg #</td><td>%</td><td>Avg. #</td><td>%</td></tr><tr><td rowspan="4">10</td><td>100</td><td>16.0</td><td>8.4</td><td>52.5%</td><td>3.3</td><td>20.6%</td><td>7.6</td><td>47.5%</td></tr><tr><td>500</td><td>15.1</td><td>12.1</td><td>80.1%</td><td>1.3</td><td>8.6%</td><td>3.0</td><td>19.9%</td></tr><tr><td>1000</td><td>15.8</td><td>14.0</td><td>88.6%</td><td>1.4</td><td>8.9%</td><td>1.8</td><td>11.4%</td></tr><tr><td>2000</td><td>15.1</td><td>13.7</td><td>90.7%</td><td>0.9</td><td>6.0%</td><td>1.4</td><td>9.3%</td></tr><tr><td rowspan="4">20</td><td>100</td><td>38.8</td><td>20.6</td><td>53.1%</td><td>10.6</td><td>27.3%</td><td>18.2</td><td>46.9%</td></tr><tr><td>500</td><td>38.1</td><td>34.2</td><td>89.8%</td><td>11.8</td><td>30.9%</td><td>3.9</td><td>10.2</td></tr><tr><td>1000</td><td>36.2</td><td>33.3</td><td>91.9%</td><td>8.1</td><td>22.4%</td><td>2.9</td><td>8.0%</td></tr><tr><td>2000</td><td>40.0</td><td>39.8</td><td>99.5%</td><td>10.0</td><td>25.0%</td><td>0.2</td><td>0.5%</td></tr><tr><td rowspan="4">30</td><td>100</td><td>63.6</td><td>32.3</td><td>50.8%</td><td>29.8</td><td>46.8%</td><td>31.3</td><td>49.2%</td></tr><tr><td>500</td><td>65.1</td><td>56.5</td><td>86.8%</td><td>21.1</td><td>32.6%</td><td>8.6</td><td>13.2%</td></tr><tr><td>1000</td><td>65.7</td><td>62.1</td><td>94.5%</td><td>23.7</td><td>36.1%</td><td>3.6</td><td>5.5%</td></tr><tr><td>2000</td><td>68</td><td>67.1</td><td>98.7%</td><td>21.5</td><td>31.6%</td><td>0.1</td><td>0.1%</td></tr></table>

## 4.1. The going-concern decision for banking institutions

During audit of a bank, auditors consider whether there is reasonable doubt as to the financial viability of the audited bank. The financial stability evaluation is a difficult and complex decision. The increase in bank failures witnessed in the US in the last few years has made the financial stability evaluation even more important. For auditors, the most important evidence of financial instability is provided by the financial statements in the form of financial ratios. The financial ratios indicate such problems as “poor loan quality”, “inadequate capital”, or “managerial inefficiency”.

In recent years, many alternative models have been proposed for examining the financial viability of banks $[1,2,4,7,14,18–20,28,39]$ . According to one body of auditing researchers, an auditor's judgment process of financial stability can be viewed as that of belief revision, where an auditor starts with an initial belief regarding the viability of an institution, and then revises the belief upward or downward, depending on the observed evidence $[3,9,22]$ . A belief network based expert system would be appropriate for modeling the financial viability task in such a fashion, since it provides an automated means of performing the revision of belief. Auditors can input data which they deem relevant in a given situation and then use the network to provide the revised belief in the viability of the bank under consideration. Based on the revised beliefs, the auditor can choose to either pass a judgement on the bank, or perform further analysis on one or more aspects of the banks financial viability.

When predicting a banks future, a large number of different financial ratios are used. For expositional simplicity, we consider the nine ratios shown in Table 3 that have been frequently used in prior studies [34,35]. Since belief network representations require categorical data, the different ratios are classified as either above the group average, or below the group average, for each bank.

Using financial ratios to make predictions about financial stability is a complex process, and it usually takes an auditor a large number of years of experience. Due to cognitive limitations, it is usually hard even for experienced auditors to evaluate the effect of a large number of evidence variables simultaneously on some unobservable decision variable [18]. In practice, auditors examine different aspects of a banks performance, and then arrive at a comprehensive evaluation regarding its financial health. When analyzing a banks performance, four important factors considered by an auditor are: loan quality, efficiency, profitability, and capital adequacy [34,35]. Three of these factors, loan quality, efficiency and profitability are not directly measurable (we call such variables as intermediate variables). Instead auditors use surrogate financial ratios to examine a bank's performance in these areas. Such intermediate variables have been called latent variables in the econometric and sociology literature [27,36,38]. The use of these intermediate latent variables help to decompose large complex problems into smaller tractable ones.

Table 3  
Financial ratios used in study

<table><tr><td>Variable name</td><td>Description</td></tr><tr><td>1. PROVNLNS</td><td>Provision for loan losses to Net Loans</td></tr><tr><td>2. PROVOPIN</td><td>Provision for loan losses to Total Operating Income</td></tr><tr><td>3. NLNSASST</td><td>Net Loan/Total Assets</td></tr><tr><td>4. ROA</td><td>Net Income/Average Total Assets</td></tr><tr><td>5. ROE</td><td>Net Income/Average Total Equity</td></tr><tr><td>6. MARGIN</td><td>(Total Interest Income – Total Interest Expenses)/Total Assets</td></tr><tr><td>7. OPINCAST</td><td>Total Operating Income/Total Assets</td></tr><tr><td>8. OEOPINC</td><td>Total Operating Expenses/Total Operating Income</td></tr><tr><td>9. CAPADQ</td><td>Total Equity Capital/Total Assets</td></tr></table>

![](/api/attachments/34YBYHFR/fulltext/images/b8bc1513c542b22710ff70c23230a7ed16a296a6786477e58f5abcb503a3c949.jpg)  
Fig. 5. A belief network structure without latent performance factors.

We include such intermediate variables in belief networks for two important reasons. First, by incorporating these variables, we can obtain parsimonious models that capture the important dependencies, without having to store a joint distribution that completely enumerates the conditional probability for the Financial Distress variable for every combination of outcomes of different variables in the network. For example, if we were to represent the dependencies directly between the measurable financial ratios and the Financial Distress condition of a bank, we would have a network of the form shown in Fig. 5.

Since there are nine incoming arcs to the decision node (the Financial Distress condition) in the network, the distribution that has to be stored must include the conditional probabilities associated with all the possible realizations for the set of nine observable variables. This requires storing and processing an enormous number of probability parameters when the system is to be used in practice. In addition, obtaining precise estimates for all these parameters is very hard. The latent variables serve as mediating factors between the measurable variables and the final hypothesis, and their use can substantially reduce the number of parameters required to represent the relevant dependencies. For example, consider the case where the latent factor Loan Quality captures the effect of the ratios PROVLNS, PROVOPIN and NLNASST on the Financial Distress variable. The revised structure would be as shown in Fig. 6.

![](/api/attachments/34YBYHFR/fulltext/images/5d9dd688d601a72bbe47b94061e27865efce4d464190729d3aef334a0f2e4185.jpg)  
Fig. 6. Using latent factors in the network structure.

Using the Loan Quality factor as an intermediate variable helps to reduce the number of incoming arcs for the Financial Distress node in the network, by having the arcs from PROVLNS, PROVOPIN and NLNASST point to the Loan Quality node instead. The added increase in probability parameters required as a result of incorporating this new Loan Quality variable is more than adequately compensated by the reduction in the probability parameters required for the Financial Distress variable. For instance, if all the variables are considered to be binary, then the number of additional probability parameters required to capture the conditional probability distribution associated with the Loan Quality node is $2^{4}$ (i.e., 16). However, the reduction in parameters required for the Financial Distress node is $2^{10}-2^{8}$ , which is 768. Even when the intermediate variable, Loan Quality, is allowed to take on three values instead of two, the number of new parameters required, $3\times2^{3}$ (which is 24) is a small fraction of the parameters eliminated for the Financial Distress node (which is $2^{10}-3\times2^{7}=640$ ). This example clearly illustrates how incorporating intermediate latent variable make the representation far more compact, and subsequently much more efficient for belief propagation.

A second reason for incorporating intermediate variables in the belief network structure is that the resulting structure would match the experts intuitive model of the problem. Prior studies indicate that users more readily accept expert systems which use a reasoning model that matches their reasoning process [25]. For example, when using such a structure, the effect of a measurable variable like PROVOPIN on the Financial Distress condition of a firm is examined as follows. First, the belief regarding the latent variable Loan Quality is revised, and then this revised belief is used to update the belief regarding the Financial Distress condition.

## 4.2. Designing the belief network

We show how our program can be used to examine feasible belief network structures for this particular problem. The study uses data on the nine financial ratios obtained from 911 commercial banks $^{2}$ , 126 of which eventually filed for bankruptcy. The sample included banks of varying sizes from all regions of the United States. In order to use the latent factors in the belief network model, we needed the historical information about these factors as well. However, such information was not publicly available. Therefore, in order to illustrate the design process, we have augmented the available data by artificially generating data for the three intermediate latent factors. This was done by using the available financial ratios to classify each bank on the three intermediate factors. We have used the rules shown below to generate this data. While the rules used are ad hoc, they capture the essential nature of these variables.

## Loan quality

\- If all the three ratios, PROVNLNS, PROVO-PIN and NLNASST are above group average, then Loan Quality = Good

\- If any two of the three ratios, PROVNLNS, PROVOPIN and NLNASST are above average, and the other ratio is within 20% of the average, then Loan Quality = Average

\- For all other cases, Loan Quality = Poor

## Profitability

\- If at least two of the ratios ROA, ROE and MARGIN are above average then Profitability = Good

![](/api/attachments/34YBYHFR/fulltext/images/922f97cb5ff47a497ad2c6a518e163e1bf1493098c3eeb89ea98a0f9cb5b35d2.jpg)  
Fig. 7. A belief network for predicting financial distress in banks.

\- If exactly one of the ratios ROA, ROE and MARGIN is above average then Profitability = Average

\- If all three ratios ROA, ROE and MARGIN are below average then Profitability = Poor Efficiency

\- If the ratio OEOPINC is below average then Efficiency = Good

\- If both the ratios OEOPINC and OPINCAST are above average, then Efficiency = Average $^{3}$

\- If the ratio OEOPINC is above average, and OPINCAST is below average, then Efficiency = Poor

The entire data set (that include the financial ratios, the intermediate latent variables and the subsequent bankruptcy status for each bank in the sample) was provided as input to the program. To ensure that the available data captured the dependencies that are typically expected across the different variables for this problem, we used the design tool to compare the predictive power of some of the ratios that have been identified in prior studies as important predictors of the financial distress situation. The design tool was used to rank the predictive power of these individual ratios. This was accomplished by providing as alternative structures the different ratios, one at a time, as parents of the financial distress variable. The different alternatives were ranked using the mutual information measure. These rankings were found to be consistent with results obtained in prior studies.

To obtain the desired belief network, we allowed the program to determine, for the financial distress node and the intermediate variables, the best parent sets of different sizes ranging from one to five variables. For each of the three intermediate variables, all the financial ratios were provided as feasible parent variables. For the financial distress variable, the feasible parent variables included all the financial ratios as well as the three intermediate variables. We also used the program to perform the significance tests for parents generated for each node. For example, to determine the final parent set for the Loan Quality variable, the program first calculated the mutual information independently conveyed by each financial ratios about Loan Quality. The ratio PROVOPIN was found to be the most predictive. Although the variable Loan Quality was generated based on the ratios PROVLNS, PROVOPIN and NLNASST only, the other financial ratios, when considered one at a time, also demonstrated significant predictive power for Loan Quality. This was because of the correlations that exist between the financial ratios under consideration. Subsequently, the program considered the set of two parents that were most predictive, and found the ratios PROVOPIN and NLNASST as the most predictive pair. The improvement in the mutual information for the two parent case over the single parent case (i.e., using both PROVOPIN and NLNASST as compared to using only PROVOPIN) was found to be significant at the 5% level. As expected, the best three-parent set was determined to be PROVLNS, PROVOPIN and NLNASST. Once again, the additional parent (PROVLNS) was found to significantly increase the mutual information measure. When parent sets with four variables were considered, then none of the other ratios was found to contribute significantly to the Loan Quality variable. This was consistent with the way the data was generated for the Loan Quality variable. The program obtained the parent set for the intermediate variables Profitability and Efficiency in a similar manner. The significant parent sets identified for each intermediate variable are shown in Fig. 7. As expected, the program selected exactly those financial ratios as parents for Profitability and Efficiency that were used to generate the data itself.

Next, the program examined the financial ratios as well as the intermediate variables as potential parents for the Financial Distress node. The variables selected as the best parent(s) for the Financial Distress variable are shown in Table 4.

<table><tr><td colspan="2">Optimal parent sets of different sizes for the financial distress node</td></tr><tr><td>No. of parents</td><td>Variables selected</td></tr><tr><td>1</td><td>ROA</td></tr><tr><td>2</td><td>Profitability, Efficiency</td></tr><tr><td>3</td><td>Profitability, Efficiency, Loan Quality</td></tr><tr><td>4</td><td>Profitability, Efficiency, Loan Quality, CAPADQ</td></tr><tr><td>5</td><td>Profitability, Efficiency, Loan Quality, CAPADQ, MARGIN</td></tr></table>

It is interesting to note that the financial ratio ROA was most predictive of the Financial Distress condition when a single variable was considered as a parent. When two variables were considered, then Profitability and Efficiency taken together conveyed the maximum information about the Financial Distress condition. The fact that ROA was not included any more is not unusual, since our technique explicitly considers the mutual interaction of the variables in the parent set. The best parent set of size three included the three intermediate variables Profitability, Efficiency and Loan Quality. We found that the increase in mutual information on adding Loan Quality to the parent set was not significant at the 5% level. A likely reason for this is that we have used fairly rudimentary rules to generate data for the Loan Quality variable. An experienced auditor would usually be able to classify the Loan Quality of a bank in a more precise manner. When such information is used for constructing the network, we expect Loan Quality to be more significant. We found that the financial ratio CAPADQ was included in the best parent set, along with the three intermediate variables, when parent sets consisting of four variables were considered. Once again, the increase in mutual information was not significant at the 5% level. The same was true for the best five-variable parent set, which included MARGIN to the earlier solution.

In practice, we expect designers to consider solutions that result in the most logical structure for an application domain. Thus, even when the effect of a variable is not at the level of significance often associated with statistical tests, the expert may feel that it should be incorporated in the network. In such cases, an important consideration will be to examine the effect of the additional variable towards the computational efficiency of the resulting network (when used to make inferences in actual use). For instance, having three intermediate variables as parents for the Financial Distress node requires a conditional probability distribution for that node with 54 probability parameters. Adding CAPADQ as the fourth parent requires 108 probability parameters. The increase in computational requirements for propagating beliefs is proportional to the increase in the probability parameters required. Since having a larger number of variables as parents usually leads to better solutions (in some small measure), the decision to include them will depend on the computational resources that are available in the work environment. Benchmark tests can be performed to estimate the response times that result from different sizes of the parent set. Results of such tests can help to decide whether a larger parent set is worthwhile or not.

## 5. Discussion

In this paper, we present a design tool to assist in the development of belief network based expert systems. The design tool uses information theoretic measures to compare alternative structures. The program can estimate the necessary probability parameters for network representations from sample data. Three important capabilities of the design tool are discussed with the help of examples. They are: (i) evaluating alternative structures; (ii) finding optimal networks with specified connectivity; and (iii) eliminating weak dependencies from derived network structures. We examine the performance of the design tool on many sets of simulated data, and show that the design tool is fairly accurate in recovering the important dependencies across variables in a problem domain. We illustrate how this program can be used to design a belief network for evaluating the financial distress situation for banks. We also show that the use of intermediate latent variables can lead to a parsimonious representation of the important dependencies for the financial distress problem. The techniques implemented in the design tool allow different structures to be easily evaluated, and can enable designers to consider many alternatives before arriving at a final design.

An interesting aspect of the design tool is that it allows users who have expertise in the application domain to guide the search for a desired network structure using their domain knowledge. Such users can often restrict the search process to consider only those structures that are appropriate for the relevant problem. The experimental results indicate that when used in this fashion, the program can serve as a powerful design tool. Relatively naive users can use the design tool to generate computationally efficient structures, and test the dependencies in proposed structures for statistical significance when sample data is used to generate these structures. When used in this fashion, the program will usually identify the right set of predictive attributes for each variable. The potential drawback is that it could also select additional variables that may not always be truly predictive.

In this research, the design of a belief network for the financial distress problem has been of an exploratory nature. An important issue for future research is to examine the performance of such a belief network based expert system. One way to do this would be to empirically validate an expert system that uses a belief network mechanism by comparing it to practising auditors. Designs obtained from the current program can be implemented in the expert system, and used to revise beliefs about a bank's financial distress status based on observations of the financial ratios that are part of the structure. The results obtained from the system could then be compared with revised beliefs of auditors when provided with the same information. To this end, we are currently examining the financial distress problem in further detail.

## Acknowledgements

We wish to thank the anonymous referees whose helpful comments and suggestions have improved the quality of this paper.

## References

[1] E.I. Altman, Financial Ratios, Discriminant Analysis, and the Prediction of Corporate Bankruptcy, Journal of Finance, September (1968) 589–609.

[2] E.I. Altman, R. Haldeman and P. Narayanan, Zeta Analysis: A New Model to Identify Bankruptcy Risk of Corporations, Journal of Banking and Finance, June (1977) 29–54.

[3] S.K. Asare and W.F. Messier, A Review of Audit Research Using the Belief-Adjustment Model, in: L.A. Ponemon and D.R.L. Gabhart (Eds.), Auditing: Advances in Behavioral Research (Springer-Verlag, Berlin, 1991) pp. 75-91.

[4] R. Barniv and A. Raveh, Identifying Financial Distress: A New Nonparametric Approach, Journal of Business Finance and Accounting, Summer (1989) 361–383.

[5] D. Bobrow, Qualitative Reasoning About Physical Systems (Elsevier, Amsterdam, 1984).

[6] G.W. Brier, Verification of Forecasts Expressed in Terms of Probability, Monthly Weather Review 78(1) (1958) 1–3.

[7] C.J. Casey and N. Bartczak, Using Operating Cash Flow Data to Predict Financial Distress: Some Extensions, Journal of Accounting Research, Spring (1985) 384–401.

[8] G.F. Cooper, NESTOR: A Computer-Based Medical Diagnostic Aid that Integrates Causal and Probabilistic Knowledge, PhD Dissertation, Stanford University, Stanford, CA, 1984.

[9] W.N. Dilla, R.G. File, I. Solomon and L.A. Tomassini, Predictive bankruptcy Judgements by Auditors: A Probabilistic Approach, in L.A. Ponemon and D.R.L. Gabhart (Eds.), Auditing: Advances in Behavioral Research (Springer-Verlag, Berlin, 1991) 75–91.

[10] R.O. Duda, P.E.Hart, K.Konolige and R.Reboh, A Computer-Based Consultant for Mineral Exploration, Final Report, SRI Projects 6415, SRI International, Menlo Park, CA, September 1979.

[11] T.L. Fine, Theories of Probability (Academic Press, New York, 1973).

[12] I.J. Good, Rational Decisions, Journal of the Royal Statistical Society B14 (1952) 107–114.

[13] D.E. Heckerman, Probabilistic Interpretation for MYCIN's Certainty Factors, in: L.N. Kanal and J.F. Lemmer (Eds.), Uncertainty in Artificial Intelligence (North Holland, Amsterdam, 1986).

[14] F.L. Jones, Current Techniques in Bankruptcy Prediction, Journal of Accounting Literature 6 (1987) 131–164.

[15] S. Kullback, Information Theory and Statistics (Wiley, New York, 1959).

[16] H. Kyburg, Probability and Inductive Logic (MacMillan, London, 1970).

[17] S.L. Lauritzen and D.J. Spiegelhalter, Local Computation with Probabilities in Graphical Structures and Their Applications to Expert Systems, Journal of the Royal Statistical Society B 50(2) (1988) 157–224.

[18] R. Libby, The Use of Simulated Decision Makers in Information Evaluation, The Accounting Review, July (1975) 475–489.

[19] D. Martin, Early Warning of Bank Failure, Journal of Banking and Finance 1 (1977) 29–276.

[20] W.F. Messier, Jr. and J.V. Hansen, Inducing Rules for Expert Systems Development, Management Science 34(12) (1988) 1403–1415.

[21] R.E. Neapolitan, Probabilistic Reasoning in Expert Systems: Theory and Algorithms (Wiley, New York, 1990).

[22] J.A. Ohlson, Financial Ratios and the Probabilistic Prediction of Bankruptcy, Journal of Accounting Research, Spring (1980) 109–131.

[23] J. Pearl, Fusion, Propagation, and Structuring in Belief Networks, Artificial Intelligence 29 (1986) 241–288.

[24] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufman, San Mateo, CA, 1988.

[25] R. Quinlan, Decision Trees and Decision Making, IEEE Transactions on Systems, Man and Cybernetics 20 (1990) 339–346.

[26] T.B. Roby, Belief States and the Uses of Evidence, Behavioral Science 10 (1965) 255–270.

[27] D.E. Rumelhart and J.L. McClelland, Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vols. I and II (MIT Press, Cambridge, MA, 1986).

[28] L.M. Salchenberger, E.M. Cinar and N.A. Lash, Neural Networks: A New Tool for Predicting Thrift Failures, Decision Sciences 23(4) (1992).

[29] S. Sarkar and I. Murthy, Criteria to Evaluate Approximate Belief Network Representations in Expert Systems, Decision Support Systems 15 (1995) 323–350.

[30] S. Sarkar and I. Murthy, Some Theoretical Results for Approximating Belief Network Structures, Working Paper, Department of Information Systems & Decision Sciences, Louisiana State University, Baton Rouge, 1994.

[31] S. Schocken and P.R. Kleindorfer, Artificial Intelligence Dialects of the Bayesian Belief Revision Language, IEEE Transactions on Systems, Man and Cybernetics 19 (1989) 1106–1121.

[32] G. Shafer, A Mathematical Theory of Evidence (Princeton University Press, Princeton, NJ, 1976).

[33] E.H. Shortliffe and B.G. Buchanan, A Model of Inexact Reasoning in Medicine, in: B.G. Buchanan and E.H. Shortliffe (Eds.), Rule-Based Expert Systems (Addison Wesley, Reading, MA, 1984).

[34] J.F. Sinkey, A Multivariate Statistical Analysis of the Characteristics of Problem Banks, Journal of Finance, March (1975) 21–35.

[35] J.F. Sinkey, Problem Banks: Identification and Characteristics, Journal of Bank Research, Winter (1975) 208–217.

[36] P. Spirtes, C. Glymour and R. Scheines, Causation, Prediction and Search, Lecture Notes in Statistics (Springer-Verlag, Berlin, 1993).

[37] C.-A.S. Stael von Holstein, Assessment and Evaluation of Subjective Probability Distributions, The Economic Research Institute at the Stockholm School of Economics, Stockholm, 1970.

[38] L. Steeles, Components of Expertise, AI Magazine, Winter (1990).

[39] K.Y. Tam and M.Y. Kiang, Managerial Applications of Neural Networks: The Case of Bank Failure Predictions, Management Science 38(7) (1992) 926–947.

[40] A. Tversky and D. Kahneman, Judgement Under Uncertainty: Heuristics and Biases, Science 185 (1974) 1124-1131.

[41] R.L. Winkler and R.M. Poses, Evaluating and Combining Physicians' Probabilities of Survival in an Intensive Care Unit, Management Science 39(12) (1993) 1526–1543.

[42] L.A. Zadeh, The Concept of a Linguistic Variable and Its Application to Approximate Reasoning, Information Sciences 9 (1975) 43–80.

![](/api/attachments/34YBYHFR/fulltext/images/5ba4323a3d533ce07f86a1fbc2fe37f1097b4df92f3549edda4e08ddc37761a5.jpg)

Sumit Sarkar is Assistant Professor of Management Information Systems at the College of Business at Louisiana State University. He received his MS and PhD degrees in Computers and Information Systems from the University of Rochester. His current research interests include the design of knowledge-based systems, the representation of uncertainty in expert systems and databases, and the

economics of information systems. He is a member of AAAI, ACM, INFORMS and IEEE Computer Society.

![](/api/attachments/34YBYHFR/fulltext/images/84e4be1bc95497835911f868d4eeb3a77f5ad712a089a46e6bf8a3da948c9159.jpg)

Ram S. Sriram is an Associate Professor of Accounting Information Systems at Georgia State University. He received his PhD in Accounting from University of North Texas. He is also a Certified Public Accountant and Certified Fraud Examiner. His current research interests are in the areas of auditing, neural networks, and expert systems.

![](/api/attachments/34YBYHFR/fulltext/images/c86a3aaef36be1f22531e67aef56ae62d567238c9139f01fb5526017d341b6e5.jpg)

Shibu Joykutty received his BS degree in Physics from Gandhi University, Kerala, India in July 1987, and his MS degree in Operations Research and Computer Applications from Cochin University of Science and Technology, India, in December 1989. He worked as a Programmer Analyst and Consultant at Delta Management Consultants from January 1990 to December 1992. He received his MS degree in Quantitative Business Analy-

sis from Louisiana State University, Baton Rouge, in May 1995. Currently he is an internal auditor at the Corporate Audit Services at Sprint, Inc.

![](/api/attachments/34YBYHFR/fulltext/images/7b956f0ae1ccacfedcde4a762960a67a0ddefb6988648236277d4e7437147fe4.jpg)

Ishwar Murthy is Associate Professor in the Department of Information Systems and Decision Sciences at Louisiana State University, Baton Rouge. He received his PhD Degree in Management Science from Texas A&M University. Dr. Murthy's research interests include Network Optimization, Multiobjective Optimization and Mathematical Programming Applications in Telecommunications and Expert Systems. His published

articles have appeared in Annals of Operations Research, European Journal of Operational Research, Naval Research Logistics and Operations Research, among others.
