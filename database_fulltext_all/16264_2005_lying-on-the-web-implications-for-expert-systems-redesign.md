---
otero_id: 16264
otero_key: "N3J3H3GY"
title: "Lying on the Web: Implications for Expert Systems Redesign"
authors: "Zhengrui Jiang; Vijay S. Mookerjee; Sumit Sarkar"
year: "2005"
journal: "Information Systems Research"
doi: "10.1287/isre.1050.0046"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/N3J3H3GY/fulltext/images/bb7a55c76dfe5df1f8e3337d5a03cad71d83c070e9b067cdafcde2ff395dc6c3.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Lying on the Web: Implications for Expert Systems Redesign

Zhengrui Jiang, Vijay S. Mookerjee, Sumit Sarkar,

To cite this article:

Zhengrui Jiang, Vijay S. Mookerjee, Sumit Sarkar, (2005) Lying on the Web: Implications for Expert Systems Redesign. Information Systems Research 16(2):131-148. http://dx.doi.org/10.1287/isre.1050.0046

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2005 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/N3J3H3GY/fulltext/images/0976c3b4ce9d6e82685b56e89bcaa1c37248f30492e95d5c06eced92b07f0d4b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Lying on the Web: Implications for Expert Systems Redesign

Zhengrui Jiang, Vijay S. Mookerjee, Sumit Sarkar School of Management, University of Texas at Dallas, Richardson, Texas 75083-0688 {zxj011000@utdallas.edu, vijaym@utdallas.edu, sumit@utdallas.edu}

W<sup>e</sup> <sup>consider</sup> <sup>a</sup> <sup>new</sup> <sup>variety</sup> <sup>of</sup> <sup>sequential</sup> <sup>information</sup> <sup>gathering</sup> <sup>problems</sup> <sup>that</sup> <sup>are</sup> <sup>applicable</sup> <sup>for</sup> <sup>Web-based</sup>applications in which data provided as input may be distorted by the system user, such as an applicant for a credit card. We propose two methods to compensate for input distortion. The first method, termed knowledge base modification, considers redesigning the knowledge base of an expert system to best account for distortion in the input provided by the user. The second method, termed input modification, modifies the input directly to account for distortion and uses the modified input in the existing (unmodified) knowledge base of the system. These methods are compared with an approach where input noise is ignored. Experimental results indicate that both types of modification substantially improve the accuracy of recommendations, with knowledge base modification outperforming input modification in most cases. Knowledge base modification is, however, more computationally intensive than input modification. Therefore, when computational resources are adequate, the knowledge base modification approach is preferred; when such resources are very limited, input modification may be the only viable alternative.

Key words: sequential information gathering; expert systems; input distortion; noise handling History: Salvatore March, Senior Editor; H. R. Rao, Associate Editor. This paper was received on February 13, 2004, and was with the authors 5 months for 2 revisions.

## 1. Introduction

Over the last few decades, expert systems have been implemented for a wide range of business applications. These include, among others, financial planning, providing help desk support, recommending products to customers, software debugging, configuring equipment, and the diagnosis of illnesses in the medical domain (Turban and Aronson 2000). These systems provide several benefits such as improved decision making, consistent and reproducible decisions, shorter decision-making times, and the ability to provide expertise in many places at the same time. The variety of applications for which expert systems are used continues to grow as the costs to develop and deploy such systems reduce over time.

During operation, an expert system typically acts as a consultant to the user. The system asks questions to the user, responses to which help the system identify the cause of a problem (or the solution to a problem) by examining its knowledge base. This consultation process is usually interactive in nature, as this allows the system to efficiently and cost-effectively collect information, i.e., collect items of information pertinent to the current problem instance.

Recently, many expert systems are being deployed over the Web. For instance, many financial institutions, through their websites, allow customers to apply for credit cards (e.g., www.credit-cards-comparison-charts. com, www.creditcardmall.com). Other websites elicit personal user information and preferences that are fed to expert systems that help target potential customers of a product or service in online marketing campaigns.

## 1.1. Problem Motivation

Expert systems that are deployed over the Web are facing an important challenge in the form of noisy input data supplied to the system during its use. A variety of factors contribute to the presence of noisy input data. The most significant cause is probably the deliberate falsification of input data by Web users. Tapscott (1999) has reported that “at least 4 out of 10 Internet users admit to giving false answers to website questionnaires to capture a preferred benefit,”

and those who lie on the Web “routinely give bogus names, incomes, ages, and gender or say they live somewhere they don’t.” Web users also lie to protect their privacy and possible misuse by firms of any personal data they provide (Fox et al. 2000). Another factor that contributes to lying is that there is no faceto-face interaction between the user and the organizations’ agents in an online environment. Thus, there are no visual or nonverbal cues that could potentially help an agent recognize that a user is lying. The likelihood of input data falsification is further increased because of the relative anonymity of the Web user, combined with the fact that users do not need to expend any significant effort to consult the system. Besides intentional distortion of input data, factors such as poor interface design or lack of computing and typing skills could lead to random mistakes in the input data supplied by a user.

Regardless of the cause of noise, incorrect input data can lead to errors in a firm’s decision-making process. In the case of credit card applications, highrisk customers may be wrongly approved while deserving customers may be denied. Similarly, in the case of data collected to support a marketing campaign, a firm may solicit someone who is not interested or miss someone who may have been willing to purchase. In all these situations, it becomes important for the organization to take measures that either reduce noise (e.g., through better interface design, by providing incentives to reduce lying) or compensate for it after it has occurred.

Noise handling methods are needed because reduction measures are not likely to completely eliminate input noise. While warning users of the severe consequences of lying is easy, enforcement is usually not. If the disincentives of lying are not enforced (e.g., because the verification process to establish the correct information is costly), users may eventually begin to ignore them. Furthermore, users may perceive that they benefit more from lying than from the incentive provided by the firm to be truthful. Thus, noise compensation techniques are still necessary to improve the decisions recommended by expert systems, in particular those that operate in a Web environment.

## 1.2. Previous Research

Depending on how the initial knowledge base is obtained, expert systems can broadly be classified into inductive systems and deductive systems. For inductive expert systems, decision rules (e.g., a decision tree) are learned from training data. Deductive systems, on the other hand, are usually based on expertprovided decision rules.

Existing literature on handling noise in expert systems has mainly focused on the development of inductive systems to operate in a noisy environment. Within this area, the most popular noise handling technique is decision tree pruning (Quinlan 1986, Mingers 1989, Breslow and Aha 1997). Quinlan (1986) found that pruned decision trees perform better than unpruned decision trees in the presence of input data noise. While pruning is usually applied as a post processing technique (i.e., the tree is pruned after it is induced), other approaches prune the decision tree during its construction; i.e., the induction process itself is modified to cope with noise (Clark and Niblett 1989, Mookerjee et al. 1995). In addition to pruning, a number of fuzzy learning methods have been used to derive fuzzy rules that perform well with noise and/or incomplete training data (Lee 1990, Hong and Chen 2000, Wu et al. 2003). Finally, version space-based learning strategies have also been shown to perform well with noisy and uncertain data sets (Hirsh 1994, Hong and Tsang 1997). Typically, all the above-mentioned techniques work well only when the noise in the training and test data have similar patterns.

In contrast to inductive systems, the rules of a deductive system are provided by experts. Hence, noisy input data does not affect the creation of rules, but is relevant to consider when the system is consulted. When an expert system operates in an offline mode, it may be possible to remove noise in the input data before the data is supplied to the system. Due to these reasons (i.e., noise has no impact on the rules, inputs can usually be cleaned before consulting the system), noise handling in deductive systems has not been an active research area. However, with more expert systems being deployed over the Web, noise resulting from deliberate falsification (or from other random causes) becomes a real obstacle. Even in offline systems, noise may still be an issue if the data cannot be cleaned (or is too costly to clean) before consultation. For example, offline expert systems have been developed for audit planning and audit risk analysis (Graham et al. 1991, Delisio et al.

1993). In these systems, certain inputs may be costly to obtain accurately. For example, accurately estimating the value of inventory assets may require a physical inspection of the material held at various factory sites. Thus, the system may be required to work with inventory figures that are noisy. This study attempts to address the problem of designing deductive expert systems that need to operate with noisy input data.

## 1.3. Contributions

We propose two methods to cope with noise. The first method, which we term knowledge base modification (KM), considers modifying the knowledge base (specifically, a decision tree) to account for distortion in the inputs provided by the user. This method involves a one-time computational effort to modify the knowledge base; however it is very efficient during operation. It is appropriate when the distortions in inputs are relatively stationary (i.e., input noise levels do not change much over time), and the improvement in decision making is significant. The second method—termed input modification (IM)—involves a preprocessing step during which the observed inputs are modified to account for distortions. This method involves modifying an observed input to the most likely true value of the input given the observation(s) made by the system. The modified input is then fed into the existing (unmodified) knowledge base. The IM method may sometimes be preferable because the KM method requires frequent knowledge base redesign if the input noise levels fluctuate.

The problem is formulated as one where an organization has available to it (1) a decision tree that leads to the desired outcomes (recommendations) when accurate input data is available, and (2) a set of beliefs about the accuracy of each possible input data item provided by users. In the KM method, a revised decision tree is obtained, which specifies optimal recommendations for all feasible combinations of observed input values. The IM method does not require any modification of the original decision tree. The KM and IM methods are compared along several dimensions with the original decision tree. Experimental results indicate that both types of modification substantially improve the accuracy of recommendations, with knowledge base modification outperforming input modification in most cases.

Input modification, however, requires less computational effort than knowledge modification. Therefore, knowledge modification is the preferred approach when computational resources are not a limiting factor; when such resources are very limited, input modification may be the only viable alternative.

The rest of the paper is organized as follows. Section 2 describes the overall model of noise and assumptions. Section 3 provides details of the two proposed noise handling methods. Section 4 presents results of experiments conducted using the proposed methods. In §5, we consider two variations of the proposed methods and provide overall recommendations concerning the choice of a noise handling method. Section 6 summarizes the contributions of this work and identifies opportunities for future research.

## 2. Input Noise Model

We illustrate our model of noise using decision rules for a hypothetical credit rating application shown in Table 1 below. We propose this example in the context of credit screening for online credit card applications, where the objective is to decide whether an application should be approved, and, if so, the kind of card (e.g., platinum, gold, or regular) that should be issued to a particular customer. Table 1 shows four inputs that could be required from a user: Income (high, medium, low),<sup>1</sup> Bachelor’s Degree (yes, no), Employment (yes, no), and Bankruptcy (yes, no). Bankruptcy refers to whether the applicant has ever filed for bankruptcy. For expositional simplicity, we assume in this example that the four inputs are independent. Based on a consultation session, the system recommends a credit risk category: high risk (HR), medium risk (MR), or low risk (LR) that could be used to determine the kind of card to be offered to the customer. The last column of this table shows the joint probability of the inputs in each row of the table. A dash entry in the table represents that the input could be “Y” or “N.”

2.1. Estimating Probabilities for True Input States To account for the presence of noise in the observations, it is necessary to estimate the probability of true input values based on noisy observations. Let True refer to the true input vector underlying an observed input vector Observed; the observations could refer to all the possible inputs that could be obtained for a given problem, or they could refer to a subset of the possible inputs. We are interested in estimating P -True Observed for all feasible sets of input values, expressed as:

Table 1 Decision Table for the Credit-Granting System Example

<table><tr><td rowspan="2">Rules</td><td colspan="4">Inputs</td><td rowspan="2">Outcome</td><td rowspan="2">Joint prob.</td></tr><tr><td>Income</td><td>Bachelor&#x27;s degree</td><td>Employment</td><td>Bankruptcy</td></tr><tr><td>CR0</td><td>H</td><td>—</td><td>—</td><td>—</td><td>LR</td><td>0.600</td></tr><tr><td>CR1</td><td>M</td><td>Y</td><td>Y</td><td>—</td><td>LR</td><td>0.126</td></tr><tr><td>CR2</td><td>M</td><td>—</td><td>N</td><td>—</td><td>MR</td><td>0.090</td></tr><tr><td>CR3</td><td>M</td><td>N</td><td>Y</td><td>—</td><td>MR</td><td>0.084</td></tr><tr><td>CR4</td><td>L</td><td>—</td><td>—</td><td>Y</td><td>HR</td><td>0.020</td></tr><tr><td>CR5</td><td>L</td><td>—</td><td>—</td><td>N</td><td>MR</td><td>0.080</td></tr></table>

$$
\begin{array}{l} P (\text { True } \mid \text { Observed }) \\ = \frac {P (\text { Observed } \mid \text { True }) \cdot P (\text { True })}{P (\text { Observed })}. \end{array}\tag{1}
$$

When the number of inputs under consideration is even moderately high, it becomes difficult to obtain reliable estimates for P -Observed  True directly as a very large number of probability parameters have to be estimated. For example, if there were n binary inputs, then we would need to estimate probability terms for True vectors corresponding to each of the $2 ^ { n }$ possible Observed vectors. Because there would be $2 ^ { n }$ different True vectors for which such parameters would need to be estimated for each Observed vector, we would need to estimate a total of $2 ^ { 2 n }$ different probability parameters to calculate the above expression for all feasible observations. It is clearly impossible for domain experts to provide so many estimates. Even when the estimates are obtained from data, the amount of data required to make reliable estimates could be prohibitively high. To make tractable the number of parameters to be estimated, we make two assumptions:

Assumption 1. P -Observed<sub></sub>True<sub>=</sub>  P -Observed <sub></sub> True, where i is an index over the inputs.

Assumption 2. P -Observed <sub></sub> True <sub>=</sub> P -Observed <sub></sub> True<sub>i</sub> for all i.

Assumption 1 implies that each individual input observation is conditionally independent of other input observations given the set of true input values. In other words, the probability associated with each input observation is dependent on the true state of the input vector, and not on other noisy observations. We expect this to be reasonable in most circumstances. For instance, a user may falsify her income to obtain a favorable recommendation, but at the same time she may be honest about her education background if she perceives it to be beneficial for the desired outcome. Assumption 2 can be interpreted to mean that the observed state of an input i is conditionally independent of the true states of other inputs, given the true state of input i. In other words, applicants distort data at the level of the individual input level rather than at the aggregate profile level. It is possible that some applicants are able to foresee the inputs they will be asked to provide in the sequential decision process, and may make the extra cognitive effort of manipulating their response for a current input based on the set of their true states for inputs already provided as well as the inputs they may be asked to provide subsequently. Typically, though, we expect respondents to distort data on each input based primarily on the true value of that input and their expectation of the impact of the distortion on the eventual recommendation by the system.

Figure 1 provides a graphical representation of the dependencies (and conditional independencies) between the observed and true input states. The box circumscribing the $T _ { i } \mathbf { s }$ is used to denote the dependencies across all true input states.<sup>2</sup> While it is possible in some situations that an input state is independent of other inputs, to keep our model fairly general we do not make this assumption. Assumption 1 eliminates the need for arcs connecting the $O _ { i } ^ { \prime } \mathbf { s }$ (observed states) directly. Assumption 2 eliminates arcs from $T _ { j }$ to $O _ { i }$ for all $j \neq i .$ The assumptions taken together imply that observation $O _ { i }$ is conditionally independent of all other observed and true states, given the true state $T _ { i } .$

Bachelor’s degree (D)

Figure 1 Graphical Representation of Dependencies Between Observed and True States  
![](/api/attachments/N3J3H3GY/fulltext/images/c2030b074cb4de34917f5ededcfcd543550fad3e526faff945b96421fffb910d.jpg)

The above assumptions are used to simplify the term P -Observed  True as follows:

$$
P (\text { Observed } \mid \text { True }) = \prod_ {i} P (O b s e r v e d _ {i} \mid T r u e _ {i}).\tag{2}
$$

Equation 1 can now be rewritten as:

$$
P (\text { True } \mid \text { Observed }) = \frac {\prod_ {i} P (O b s e r v e d _ {i} \mid T r u e _ {i}) \cdot P (\text { True })}{P (\text { Observed })}.\tag{3}
$$

The task of estimating P -True <sub></sub> Observed, which is essentially one of determining the likelihood of a true vector given the observations (Berger 1985, pp. 27–31), is considerably simplified as the parameters needed in the revised expression are the terms P-Observed $T r u e _ { i } )$ for each i, and the term P-True. The terms $P ( O b s e r v e d _ { i } \mid T r u e _ { i } )$ for each i can be obtained either from domain experts, or from sample data collected for that purpose. In contrast to Equation (1), for n binary inputs only 2n independent parameters would need to be obtained (two for each input) instead of $2 ^ { 2 n }$ . Given the relatively fewer number of parameters needed, reliable estimates may be obtained with reasonable amounts of data. P -True, the second term in the numerator, is simply the joint probability of a true input vector. This can be estimated from historical data. Based on (2) and the distribution of the true vectors, we can calculate the probability that a vector is observed:

Figure 2 (a) Input Distortion Matrices; (b) Input Marginal Distributions  
(a)  
Income (I)

<table><tr><td></td><td>High</td><td>Medium</td><td>Low</td></tr><tr><td>High</td><td>0.9</td><td>0.05</td><td>0.05</td></tr><tr><td>Medium</td><td>0.35</td><td>0.6</td><td>0.05</td></tr><tr><td>Low</td><td>0.25</td><td>0.35</td><td>0.4</td></tr></table>

<table><tr><td></td><td>Yes</td><td>No</td></tr><tr><td>Yes</td><td>0.95</td><td>0.05</td></tr><tr><td>No</td><td>0.35</td><td>0.65</td></tr></table>

(b)  
Income (I)

<table><tr><td>High</td><td>0.6</td></tr><tr><td>Medium</td><td>0.3</td></tr><tr><td>Low</td><td>0.1</td></tr></table>

Bachelor’s degree (D)

$$
P (\text { Observed }) = \sum_ {r} P (\text { Observed } \mid \text { True } ^ {r}) P (\text { True } ^ {r}),\tag{4}
$$

where r is the index over all possible true vectors.

Figure 2 illustrates the distortion matrices and marginal distributions for each input in the credit rating application. Each entry in a distortion matrix stands for the probability of an observed input state (column) given the true input state (row). To illustrate the process of calculating the left-hand-side quantity in Equation (3), consider an observed input vector $( I ^ { O } =$ $\mathrm { } ^ { \prime \prime } \hat { \bf M } , ^ { \prime \prime } D ^ { O } = { } ^ { \prime \prime } \Upsilon , ^ { \prime \prime } E ^ { O } = { } ^ { \prime \prime } { \bf N } , ^ { \prime \prime } B ^ { O } = { } ^ { \prime \prime } { \bf N } ^ { \prime \prime } )$ corresponding to the observed states of the inputs Income, Bachelor’s Degree, Employed, and Bankruptcy. To obtain the probability that the true input vector is $( I ^ { T } = { } ^ { \prime \prime } \mathrm { H } , { } ^ { \prime \prime } { \bf \hat { \Sigma } } { \bf \Sigma } { \bf \hat { \Sigma } } ^ { T } = { } $ “Y,” $\mathrm { \bar { } { \cal E } ^ { \mathrm { \scriptscriptstyle T } } } = \mathrm { \mathrm { } { } ^ { \mathrm { \prime \prime } } { \Upsilon } , { } ^ { \mathrm { \prime \prime } } \mathrm { \ } { \cal B } ^ { \mathrm { \scriptscriptstyle T } } = \mathrm { } { } ^ { \mathrm { \prime \prime } } \mathrm { \Upsilon } ^ { \mathrm { \bar { \prime \prime } } } ) }$ , we first use Equation (2) to calculate

$$
\begin{array}{r l} & P \big (I ^ {O} = “ \mathrm{M}, ” D ^ {O} = “ \mathrm{Y}, ” E ^ {O} = “ \mathrm{N}, ” B ^ {O} = “ \mathrm{N}" | I ^ {T} = “ \mathrm{H}, ” \\ & \qquad \qquad \qquad \qquad \qquad \qquad D ^ {T} = “ \mathrm{Y}, ” E ^ {T} = “ \mathrm{Y}, ” B ^ {T} = “ \mathrm{Y}" \big) \\ & \qquad = P \big (I ^ {O} = “ \mathrm{M}" | I ^ {T} = “ \mathrm{H}" \big) \cdot P \big (D ^ {O} = “ \mathrm{Y}" | D ^ {T} = “ \mathrm{Y}" \big) \\ & \qquad \cdot P \big (E ^ {O} = “ \mathrm{N}" | E ^ {T} = “ \mathrm{Y}" \big) \cdot P \big (B ^ {O} = “ \mathrm{N}" | B ^ {T} = “ \mathrm{Y}" \big) \\ & \qquad = 0. 0 0 3 8. \end{array}
$$

Based on the distortion matrices and marginal distributions shown in Figure 2, we have $P ( I ^ { T } = ^ { \prime \prime } \mathrm { H } , ^ { \prime \prime } D ^ { T } =$ $^ { \prime \prime } \Upsilon , ^ { \prime \prime } E ^ { T } = ^ { \prime \prime } \Upsilon , ^ { \prime \prime } B ^ { T } = ^ { \prime \prime } \Upsilon ^ { \prime \prime } ) = 0 . 0 5 4$ and $P ( I ^ { O } = { } ^ { \prime \prime } \mathrm { M } , { } ^ { \prime \prime }$

Employed (E)

<table><tr><td></td><td>Yes</td><td>No</td></tr><tr><td>Yes</td><td>0.9</td><td>0.1</td></tr><tr><td>No</td><td>0.45</td><td>0.55</td></tr></table>

Bankruptcy (B)

<table><tr><td></td><td>Yes</td><td>No</td></tr><tr><td>Yes</td><td>0.2</td><td>0.8</td></tr><tr><td>No</td><td>0.01</td><td>0.99</td></tr></table>

<table><tr><td>Yes</td><td>0.6</td></tr><tr><td>No</td><td>0.4</td></tr></table>

Employed (E)

<table><tr><td>Yes</td><td>0.7</td></tr><tr><td>No</td><td>0.3</td></tr></table>

Bankruptcy (B)

<table><tr><td>Yes</td><td>0.2</td></tr><tr><td>No</td><td>0.8</td></tr></table>

$0 ^ { O } = ^ { \prime \prime } \Upsilon , ^ { \prime \prime } E ^ { O } = ^ { \prime \prime } \mathrm { N } , ^ { \prime \prime } B ^ { O } = ^ { \prime \prime } \mathrm { N } ^ { \prime \prime } ) = 0 . 0 3 8 9 .$ From (3), we obtain

$$
P \big (I ^ {T} = “ \mathrm{H}, ” D ^ {T} = “ \mathrm{Y}, ” E ^ {T} = “ \mathrm{Y}, ” B ^ {T} = “ \mathrm{Y}" | I ^ {O} = “ \mathrm{M}, ”
$$

$$
D ^ {O} = “ \mathrm{Y}, ” E ^ {O} = “ \mathrm{N}, ” B ^ {O} = “ \mathrm{N} ”) = 0. 0 0 4 9.
$$

The likelihood of all other feasible true input vectors can be calculated analogously.

## 3. Solution Approaches

As briefly discussed in §1, there are two methods to address noise in input data, the knowledge base modification (KM) method and the input modification (IM) method. In the KM method, the original knowledge base is modified based on the most likely outcome given each possible observed vector. In the IM method, the observed inputs are used to infer the most likely true values of the inputs that are then fed into the existing (unmodified) knowledge base. In this section, we begin with a detailed description of the two methods, and then illustrate them using the credit rating system example introduced in the previous section. We finally highlight the conceptual differences between KM and IM.

## 3.1. Knowledge Modification

The inputs to the KM method include the original decision tree (or True tree for simplicity), the joint input probability distributions, and the distortion matrices for all variables. The output to the KM method is a modified decision tree that we name a KM tree. Before the KM tree can be generated, we need to first compute the fully enumerated KM table, which includes the KM recommendations for all possible observed vectors. The KM recommendations for a given observed input vector, in turn, depend on the conditional probabilities of all true vectors given the observed vector. The KM method consists of the following five steps.

Step 1. Find the probabilities of all possible true input vectors given an observed vector.

Using (3), we find the conditional probabilities of all true input vectors given an observed vector, denoted by Observed. P(Observed) is obtained based on (4).

Step 2. Find the KM recommendation for the given observed vector.

Sum up the conditional probabilities of all true vectors that have the same recommendation. The recommendation with the highest total probability becomes the KM recommendation.

Step 3. Construct the fully enumerated KM table.

This is obtained by iterating Step 1 and Step 2 for all possible observed vectors.

Step 4. Construct the condensed KM table.

The KM table is compressed to create the condensed KM table. The compression logic for starting with a fully enumerated decision table to remove redundant input entries has been outlined in prior studies (e.g., Reinwald and Soland 1966, Schwayder 1974).

Step 5. Generate the KM decision tree.

Using the condensed decision table and the probability distribution of observed vectors, the optimum KM tree can be found using AO∗ search (Mookerjee and Mannino 1997), a variant of branch and bound search. The output of this step is the KM tree.

## 3.2. Input Modification

In the IM method, the True tree, the marginal distributions of the variables, and the distortion matrices for the variables are needed to generate the IM recommendations for observed input vectors. The partial order of the variables acquired is determined by the True tree structure. For each variable acquired, its most likely true input state is chosen based on the following Bayes formula:

$$
P (X ^ {T} \mid X ^ {O}) = \frac {P (X ^ {O} \mid X ^ {T}) P (X ^ {T})}{P (X ^ {O})},\tag{5}
$$

where $X ^ { O }$ and $X ^ { T }$ represent the observed state and the true state of a variable, respectively. The procedure for the IM method consists of the following steps.

Step 1. Find the most likely true state from the observed value of the variable represented by the root node, and traverse the tree based on this state.

Step 2. If the current node is a decision node, then it represents the IM recommendation for the observed inputs. If not, compute the most likely true state for the current variable, and traverse the tree accordingly.

Step 3. Repeat Step 2 until a decision node is reached.

## 3.3. Illustration Using the Credit Rating System Example

We illustrate the KM and IM methods using the credit rating system example.

3.3.1. Knowledge Modification. To illustrate how the first two steps work, consider Observed $( I n c o m e = { ^ { \prime \prime } \mathrm { L } } , { ^ { \prime \prime } }$ Bachelor’s $D e g r e e = ^ { \prime \prime } \Upsilon , ^ { \prime \prime } E m p l o y e d = ^ { \prime \prime } \Upsilon , ^ { \prime \prime }$ $B a n k r u p t c y = " \mathrm { N } ^ { \prime \prime } )$ . First, we compute the conditional probabilities of all true vectors given this observed vector. Second, we add the conditional probabilities of all true input vectors that result in the same outcome. The sum of these probabilities for the low-risk category is $0 . 4 7 0 ,$ and the sums for the medium- and high-risk categories are 0.451 and 0.079, respectively. Therefore, we pick LR as the KM recommendation for the observed vector $( ^ { \prime \prime } \mathrm { L } , ^ { \prime \prime } ^ { \prime \prime } \Upsilon , ^ { \prime \prime } ^ { \prime \prime } \Upsilon , ^ { \prime \prime } ^ { \prime \prime } \mathrm { N } ^ { \prime \prime } )$

In the third step, by repeating Step 1 and Step 2 for all other possible observed vectors, we get the KM table. The fully enumerated KM table is compressed in the fourth step. In the final step, the KM tree is generated from the condensed KM table. For this example, the KM tree is different from the True tree only in one branch. In Figure 3, we show on the right the tree fragment in the KM tree that replaces the shaded fragment in the True tree. It is interesting to observe some similarities and differences between the True tree and the KM tree. Clearly, in the KM tree more information is sometimes needed to come up with a recommendation. For example, when income is observed to be low in the KM tree, additional inputs have to be gathered before a recommendation can be made.

3.3.2. Input Modification. We now illustrate the IM method using the True tree shown in Figure $3 ( \mathsf { a } )$ . Assume that $" \mathrm { L } ^ { \prime \prime }$ is the observed state for Income, which is the root node variable. To find the most likely true state, we calculate the conditional probabilities (based on Equation (5)) and find that $P ( I n c o m e ^ { T } = ^ { \prime \prime } \mathrm { H } ^ { \prime \prime } \mid I n c o m e ^ { O } = ^ { \prime \prime } \mathrm { L } ^ { \prime \prime } ) = 0 . 3 5 3 , P ( I n c o m e ^ { T } =$ $^ { \prime \prime } \mathrm { M } ^ { \prime \prime } \mid I n c o m e ^ { O } = ^ { \prime \prime } \mathrm { L } ^ { \prime \prime } ) = 0 . 1 7 7 .$ , and $P ( I n c o m e ^ { T } =$ $^ { \prime \prime } \mathrm { L } ^ { \prime \prime } \mid I n c o m e ^ { O } = ^ { \prime \prime } \mathrm { L } ^ { \prime \prime } ) = 0 . 4 7 1$ . We conclude that the most likely true state is $" \mathrm { L } ^ { \prime \prime }$ itself. Following the right-most branch marked “low,” the variable Bankruptcy is reached. We assume that the observed state for Bankruptcy is $^ { \prime \prime } \mathrm { N } . ^ { \prime \prime }$ To determine the most likely true state for Bankruptcy, the following probabilities are calculated: $P ( B a n k r u p t c y ^ { T } = " \Upsilon " |$ Bankruptc $y ^ { O } = \mathrm { ^ { \prime \prime } N ^ { \prime \prime } } ) = 0 . 1 6 8$ and $P ( B a n k r u p t c y ^ { T } =$ $^ { \prime \prime } \mathrm { N } ^ { \prime \prime }$ <sub></sub> Bankrupt $z y ^ { O } = ^ { \prime \prime } \mathrm { N } ^ { \prime \prime } ) = 0 . 8 3 2$ . We therefore conclude that the most likely true state for Bankruptcy is $^ { \prime \prime } \mathrm { N } . ^ { \prime \prime }$ Following the $" \mathrm { n o } ^ { \prime \prime }$ branch of this node, a decision node “MR” is reached. Therefore the IM recommendation for the observed vector $( ^ { \prime \prime } \mathrm { L } , ^ { \prime \prime } ^ { \prime \prime } \mathrm { Y } , ^ { \prime \prime } ^ { \prime \prime } \mathrm { Y } , ^ { \prime \prime }$ $^ { \prime \prime } \mathrm { N } ^ { \prime \prime } )$ is $\mathrm { \Omega } ^ { \prime \prime } \mathrm { M R } \mathrm { \Omega } ^ { \prime \prime }$

Figure 3 True Tree and KM Tree for the Credit Granting System  
![](/api/attachments/N3J3H3GY/fulltext/images/2ff03b00fe968a376db47a3a8416693e7bf3282a23651e923a803dd0117be231.jpg)

(b) KM tree fragment replacing the shaded  
![](/api/attachments/N3J3H3GY/fulltext/images/81c38d96dc1f911f56393134975f36779e5eb46b4c38f7748d53b103269e9eca.jpg)

## 3.4. Conceptual Comparison

IM and KM differ in terms of the constraints imposed on the methods. In IM, we are given a decision tree and are required to traverse the tree in a manner so as to compensate for noise in the inputs. Therefore, the partial order described by the given decision tree must be preserved by the IM method. In KM, there is no constraint imposed on the decision tree produced by the method. In IM a noisy input (in the extreme case, even one with no information value) may get acquired if this input appears in a path that is being traversed in the original decision tree. The KM method, on the other hand, would eliminate inputs that were noisy in favor of others that were less affected by noise. IM would be especially disadvantaged if, for instance, an input with considerable noise appeared at the root of the decision tree. Because such an input would likely provide very little discrimination, and because new inputs cannot be added to the tree, the accuracy of decisions recommended by the IM decision tree would likely suffer.

The IM method, however, can be beneficial in some situations. If the noise level is relatively low, it may not affect the decision of whether or not a certain input should be gathered. Then, to account for noise, the only adjustment needed is to map the observed state of an input to the most likely true state and use the original decision tree as if the input was observed in this state. Another situation in which the use of IM may be appropriate is one in which the level of input noise changes frequently. In KM, the entire decision tree would need to be recalculated if the noise level changed; in IM only the strategy to traverse the original decision tree would need to be changed. We show in §5.4 that the computational overhead for IM is significantly smaller than that for KM.

## 4. Experimental Study

In this section, we report the results of a series of numerical experiments conducted to compare the performance of KM and IM versus that of the True tree. Some analytical findings concerning these methods are also presented here. The performance of a method is primarily measured in terms of its accuracy, i.e., the percentage of correct recommendations made in the consultation phase. We conduct a variety of experiments based on simulated as well as real-world data. We first discuss the main factors that affect performance, followed by the experimental design, the experimental procedures, and finally the discussion of experimental results.

## 4.1. Factors and Hypotheses

We consider three factors that might affect the performance of the proposed methods: algorithm, noise, and dependency. Each factor and its anticipated effects are discussed below.

4.1.1. Algorithm. We are interested in the difference in performance of the two proposed methods (KM and IM). To provide a baseline measure of performance, we report the performance of the True tree, i.e., the original decision tree with no accommodation made for input noise. We expect KM to outperform IM over a wide range of situations because KM does not need to satisfy the constraint of preserving the partial order of the True tree. We also expect IM to perform better than the True tree because IM makes some effort to address noise in the input while the True tree does not. The following two hypotheses summarize our expectations about the performance of the three algorithms.

Hypothesis 1. KM outperforms IM over a wide range of factors.

Hypothesis 2. IM outperforms True tree over a wide range of factors.

4.1.2. Noise. The noise (or distortion level) in an input variable is defined as the probability of its observed state being different from its true state. Noise in an input can be computed directly from the input’s distortion matrix and the marginal distribution of the input. For example, if a ternary variable has the distortion matrix and marginal distribution shown in Figure 4, then the distortion level for this variable, denoted by , equals

$$
\begin{array}{l} \sum_ {i} P (T r u e _ {i}) (1 - P (O b s e r v e d _ {i} | T r u e _ {i})) \\ = P (H) (1 - P _ {1 1}) + P (M) (1 - P _ {2 2}) + P (L) (1 - P _ {3 3}). \end{array}\tag{6}
$$

In our experiments, the first -n <sub>−</sub> 1 diagonal elements for an -n <sub>×</sub> n distortion matrix are randomly generated. The last one is calculated based on the distortion level  and the marginal distribution of the variable. For a nonbinary variable, all nondiagonal elements in the ith row equal $( 1 - P _ { i i } ) / ( n - 1 )$

Figure 4 Distortion Matrix and Marginal Distribution of a Ternary Variable

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">(Observed)</td><td rowspan="2">Marginal probability</td></tr><tr><td>H</td><td>M</td><td>L</td></tr><tr><td rowspan="3">(True)</td><td>H</td><td> $P_{11}$ </td><td> $P_{12}$ </td><td> $P_{13}$ </td><td> $P(H)$ </td></tr><tr><td>M</td><td> $P_{21}$ </td><td> $P_{22}$ </td><td> $P_{23}$ </td><td> $P(M)$ </td></tr><tr><td>L</td><td> $P_{31}$ </td><td> $P_{32}$ </td><td> $P_{33}$ </td><td> $P(L)$ </td></tr></table>

With respect to the effect of the level of noise on the accuracy of the methods, we have two analytical findings (please refer to Appendices A and B for proofs):

Proposition 1. For any expert system, there exists a distortion level $\alpha _ { 0 } ,$ such that if the distortion level for all variables is less than $\alpha _ { 0 } ,$ then given an observed vector, the KM method and IM method will always provide the same recommendation as the one given by the True tree.

Proposition 2. If all elements in the same column of the distortion matrix of an input variable are equal, then (a) the variable will not appear in the KM tree; and (b) if the variable appears in some branches of the True decision tree, the final recommendation made by the IM method will not be affected by the observed state of the variable.

The above two propositions capture the behavior of the two methods at two extremes. Proposition 1 considers the case where noise is sufficiently low for all variables. From this proposition it is clear that if the noise in all input variables is sufficiently low, neither KM nor IM is needed. The second proposition deals with the other extreme: noise in a particular variable is so high that no information can be inferred from its observed value. It can be shown that if the distortion matrix of a variable satisfies the “if condition” described in Proposition 2, then the posterior distribution of a variable given its observed state is the same as its prior distribution. For this case, the KM method is more efficient than the IM method because the KM method drops such a variable from the KM tree, while the IM method acquires the input if it is in the True tree.

Because the above propositions only consider extreme values of noise (very low and very high), we need to study the impact of noise over a wide range of values. For simplicity and ease of exposition, the experiments reported in this section use the same distortion level () for all inputs. As discussed in §3.4, the KM approach is better able to adapt to noise than the IM approach because the partial order of the True tree does not need to be preserved by the KM approach. Therefore, we expect the performance difference between KM and IM to increase as noise increases. We also expect IM to perform better than the True tree because the True tree does not account for noise at all. Our expectations concerning noise are formulated in Hypotheses 3 and 4 below.

Hypothesis 3. The performance of IM relative to KM deteriorates with noise.

Hypothesis 4. The performance of the True tree relative to KM and IM deteriorates with noise.

4.1.3. Dependency. The dependency across input variables may also affect the performance of the proposed methods. This is because with higher dependency across the inputs, it may be possible to use the states of other inputs to infer the state of a noisy input. We measure dependency by the mutual information (MI) across the input variables. For example, if V is a vector of five variables $V _ { 0 } , V _ { 1 } , \dots , V _ { 4 } ,$ then the mutual information across the input variables is computed as follows:

$$
\operatorname{MI} (V _ {0}, V _ {1}, \dots , V _ {4}) = \sum_ {\overline {{V}}} P (\overline {{\mathbf {V}}}) \ln \frac {P (\overline {{\mathbf {V}}})}{\prod_ {i = 0} ^ {4} P (V _ {i})}.\tag{7}
$$

Dependency can be expected to improve the performance of KM relative to IM. With higher dependency, KM can collect additional inputs as corroborative evidence to compensate for the noise in a given input; e.g., if income is noisy, then education and/or homeownership can be additionally acquired to compensate for the noise in the income variable. Because IM cannot acquire any inputs outside of those in the True tree, the performance gap between KM and IM should increase as dependency increases. When comparing the performance difference between IM and the True tree, because both methods are restricted to the same set of inputs, we do not expect that dependency across the inputs will affect the relative performance of the two methods.

Hypothesis 5. The performance difference of IM relative to KM deteriorates with an increase in variable dependency.

Hypothesis 6. The performance of IM relative to the True tree is not affected by variable dependency.

## 4.2. Experimental Design

The polynomial regression model shown in (8) is used. Here, we are primarily interested in examining what factors affect the performance difference, rather than predicting the magnitude of the difference.

$$
\left\{ \begin{array}{l} E (\Delta A C C _ {\mathrm{KM-TRUE}}) \\ E (\Delta A C C _ {\mathrm{KM-IM}}) \\ E (\Delta A C C _ {\mathrm{IM-TRUE}}) \end{array} \right\} = \beta_ {0} + \beta_ {1} D i s t o r t i o n + \beta_ {2} \mathrm{MI} + \beta_ {3} D i s t o r t i o n \cdot \mathrm{MI},\tag{8}
$$

where

$\Delta A C C _ { \mathrm { K M - T R U E } }$ is the performance difference between KM and the True tree,

$\Delta A C C _ { \mathrm { K M - I M } }$ is the performance difference between KM and IM, and

$\Delta A C C _ { \mathrm { I M - T R U E } }$ is the performance difference between IM and the True tree.

In the experiments, all the simulated knowledge bases contain five binary input variables and three possible outcomes. The MI across these variables is controlled by choosing appropriate conditional probabilities (probability of an input variable state given another input variable state) across the input variables. The Distortion level is randomly chosen to be within !0 05" and is equal for all inputs. Note that because we have used binary variables, a distortion level of 0 implies no noise whereas a distortion level of 0.5 represents maximum noise. The response variables in (8) are computed directly from the accuracy of the different methods, which can be obtained by following the experimental procedures described below.

## 4.3. Experimental Procedure

The overall procedure is as follows. The program first generates a True decision tree by following these three steps: (1) a True decision table is generated by randomly choosing one of the three possible outcomes for all possible combinations of input vectors; (2) the distributions for the input vectors are generated by randomly setting some marginal distributions and some conditional probabilities (which determine the dependency across variables); (3) the True decision tree is constructed from the True decision table. After the original knowledge base is obtained, a distortion level is randomly chosen from the interval !0 05". The KM tree is then constructed by following the procedure given in §3. Finally, the accuracy of the different methods is determined by processing a large number of randomly generated test cases.

Figure 5 Test Case Generation and Processing  
![](/api/attachments/N3J3H3GY/fulltext/images/c460c577d3686e3b739df44e4bb02847ec95bcad8d046cb7b2f35d90c881380c.jpg)

The procedures for test case generation and processing are shown in Figure 5. For each simulated online visitor, we first randomly generate the true input vector. The true outcome for the visitor is determined by feeding the true vector into the True tree. The observed vector for this visitor is next obtained by distorting the true vector according to the chosen level of distortion. The KM, IM, and True tree recommendations are then found. The process is repeated 100,000 times to simulate 100,000 online visitors. The accuracy of a method is the percentage of correct recommendations made by the method.

To generate sufficient observations for the regression analysis, we randomly generate 100 different True trees. For each True tree, 10 different levels of distortion are used. The final data set therefore contains 1,000 rows, and each row includes the values of Distortion, MI, and the accuracy of the three methods.

## 4.4. Experimental Results

The following two t-tests were conducted to test Hypothesis 1 and Hypothesis 2:

$$
\left\{ \begin{array}{l l} H _ {0} \colon \Delta A C C _ {\mathrm{KM-IM}} = 0, \\ H _ {1} \colon \Delta A C C _ {\mathrm{KM-IM}} > 0, \end{array} \right.\tag{T1}
$$

$$
\left\{ \begin{array}{l} H _ {0} \colon \Delta A C C _ {\mathrm{IM-TRUE}} = 0, \\ H _ {1} \colon \Delta A C C _ {\mathrm{IM-TRUE}} > 0. \end{array} \right.\tag{T2}
$$

Table 2 Actual Classifications of the Methods

<table><tr><td rowspan="2">True outcome</td><td colspan="3">Classification</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td rowspan="3">A</td><td>61.6% (KM)</td><td>21.5% (KM)</td><td>16.9% (KM)</td></tr><tr><td>57.8% (IM)</td><td>22.9% (IM)</td><td>19.2% (IM)</td></tr><tr><td>54.3% (True)</td><td>23.3% (True)</td><td>22.4% (True)</td></tr><tr><td rowspan="3">B</td><td>14.4% (KM)</td><td>68.6% (KM)</td><td>17.0% (KM)</td></tr><tr><td>17.4% (IM)</td><td>65.1% (IM)</td><td>17.5% (IM)</td></tr><tr><td>21.8% (True)</td><td>56.1% (True)</td><td>22.1% (True)</td></tr><tr><td rowspan="3">C</td><td>16.7% (KM)</td><td>18.1% (KM)</td><td>65.2% (KM)</td></tr><tr><td>18.3% (IM)</td><td>22.2% (IM)</td><td>59.4% (IM)</td></tr><tr><td>21.1% (True)</td><td>23.5% (True)</td><td>55.4% (True)</td></tr></table>

In both tests, $H _ { 0 }$ is strongly rejected with a p-value less than 0.001. We therefore conclude that KM performs better than IM, and IM, in turn, performs better than the True tree. In Table 2, we report the actual classification provided by the three methods. The first row of this table shows that for test cases with a true class of $^ { \prime \prime } \mathrm { A , \prime \prime }$ KM correctly classified 61.6% of them as class $^ { \prime \prime } \mathrm { A , \prime \prime }$ and incorrectly classified 21.5% and 16.9% of them as class $\prime \prime \mathrm { B } ^ { \prime \prime }$ and class $^ { \prime \prime } { \mathsf { C } } , ^ { \prime \prime }$ respectively. Thus KM is not only the most accurate, but has the lowest misclassification rate within each misclassification category. IM dominates the True tree both in terms of overall accuracy and misclassifications. The experiment indicates that KM is a better classifier than IM, which is a better classifier than the True tree.

To examine the impacts of noise and dependency on the relative performance of the different methods, we ran three separate step-wise regressions based on model (8). The fitted response functions are listed in the first row of Table 3. The significance level was set to 0.10 in the regressions; i.e., only those variables that were found to be significant with a p-value of 0.10 or below were kept in the response functions. From the results, we conclude that both noise, dependency, and their interaction significantly affect the performance of the three methods.

We also examined the isolated effect of a factor (MI or Distortion) on the performance differences. To do this, we separately regressed the accuracy difference between pairs of methods on each factor $( \mathrm { i . e . , }$ ignoring the other factors and interaction effects). The regression coefficients and the associated t-values are reported in the last two rows of Table 3. We find that except for the coefficient in the right-bottom cell of Table 3, all other coefficients are positive and statistically significant.

From the regression results, we find that Hypotheses 3 and 4 are supported. Thus the relative advantage of KM over IM (IM over True tree) is higher at higher levels of input distortion. Hypotheses 5 and 6 are also supported. This confirms our expectation that KM should benefit from variable dependency, while IM is not benefited from variable dependency.

## 4.5. Graphical Results

We conducted a number of controlled experiments to graphically depict the nature of impact of the various factors on performance. In these experiments, a factor of interest was varied while the others were kept constant.

4.5.1. Input Distortion. Figure 6 displays the impact of input distortion on the performance of the various methods. In this experiment, the distortion of one variable was varied from 0 to 1 in steps of 0.1, while the distortions of all other variables were kept at 0.2. The symmetric nature of the KM and IM curves (Figure 6(a)) is expected. As the level of distortion increases beyond 0.5 (note all variables are binary), the impact of noise diminishes because the amount of information contained in the input increases. Hence, the accuracy of KM and IM is the lowest at a distortion level of 0.5 and the accuracy is symmetric around this level of distortion. Note, however, that the accuracy of the True tree continues to degrade beyond the 0.5 distortion level because the True tree does not account for noise in the inputs. In Figure 6(b) we show the relative improvement in accuracy achieved as a result of using KM over IM. As can be seen from this figure, the percent improvement tends to increase as the distortion changes from 0 to 0.5 and decrease afterward.

Table 3 Impact of Noise and Dependency on the Three Methods (t Value in Parenthesis)

<table><tr><td></td><td> $\Delta ACC_{KM-TRUE}$ </td><td> $\Delta ACC_{KM-IM}$ </td><td> $\Delta ACC_{IM-TRUE}$ </td></tr><tr><td>Response functions</td><td>0.00188 + 0.0339MI + 0.309Dist + 0.2004MI · Dist</td><td>-0.0014 + 0.0916MI + 0.0676Dist - 0.068MI · Dist</td><td>0.00328 - 0.0577MI + 0.241Dist + 0.268MI · Dist</td></tr><tr><td> $\partial\Delta ACC/\partial Dist$ </td><td>0.38 (24.98)</td><td>0.034 (3.16)</td><td>0.35 (21.12)</td></tr><tr><td> $\partial\Delta ACC/\partial MI$ </td><td>0.072 (6.95)</td><td>0.074 (13.83)</td><td>-0.0022 (0.20)</td></tr></table>

(a) Accuracy and distortion  
Figure 6 Impact of Distortion on Accuracy  
![](/api/attachments/N3J3H3GY/fulltext/images/aea463927ad590f2030979a84266efa9787487e917bfbe4f9263878b769a74ae.jpg)

(b) Relative improvement of KM over IM  
![](/api/attachments/N3J3H3GY/fulltext/images/dd52a11740c8ccf91250fa55579bc907c6824b22d0ba4c321fe7d9f8074933d7.jpg)

4.5.2. Input Dependency. To study input dependency in a realistic context, we use a modified version of the credit rating system example in §3. Within the four input variables, we assume that both Employment and Income depend on Bachelor’s Degree, while Bankruptcy depends on Income. Using this context, five dependency levels (very high, high, moderate, low, and zero dependency or independent) are created. The distortion levels for all variables are kept at 0.1. The results are plotted in Figure 7. Figure 7(a) shows that as input dependency increases, the accuracy of the

Figure 7 Impact of Input Dependency on Accuracy and KM Tree Size (a) Accuracy of KM and IM  
![](/api/attachments/N3J3H3GY/fulltext/images/162be2ae57712e282efdb57908b4aa28435b2c1e9823f0e1c325a628aacb4f40.jpg)

(b) KM tree size  
![](/api/attachments/N3J3H3GY/fulltext/images/a1705f95abf8d65db6a80348bfadb97f65c528175d1b4d383e0881e4a65545ee.jpg)

KM and IM methods increases and their performance gap widens. From Figure 7(b), we observe that the KM tree size increases at high and very high levels of input dependency. These patterns can be explained by the fact the KM method is able to collect additional inputs to compensate for noise and therefore better able to adapt to a noisy environment. However, this ability is not very useful when the inputs are not correlated, i.e., observing corroborative inputs is only useful when the inputs are dependent.

## 4.6. Testing with Real-World Data

To test the robustness of the methods, we conducted a series of experiments using a credit card application approval data set taken from the University of California, Irvine, machine learning repository (http:// www.ics.uci.edu/<sub>∼</sub>mlearn/MLRepository.html). The data has 2 classes, 15 variables, and 690 instances. The instances were treated as decision rules in our experiments. To make the data appropriate for the proposed methods, we preprocessed the original data as follows. First, we removed the duplicate and conflicting instances as well as instances with missing values (490 instances remained after preprocessing). Second, we converted continuous attributes to binary attributes based on the interval split provided by the decision tree induction algorithm C4.5. Third, because the proposed methods require a complete True decision tree or fully enumerated decision table, we first built a decision tree using C4.5 and used this tree to determine the classes for those input vectors that were not in the data set. Finally, the joint distribution of input vectors was computed as the product of the marginal distributions of all input variables that were obtained from the real data.

After the fully enumerated True decision table was obtained, we varied the distortion level of one variable from 0 to 1 in steps of 0.1, and fixed the distortion level for all other variables at 0.1. The impact of distortion on accuracy is shown in Figure 8. From

## Figure 8 Impact of Distortion Using Real-World Data

(a) Accuracy of IM, KM, and true  
![](/api/attachments/N3J3H3GY/fulltext/images/43ff61ba66c0aaee8e4d2fa6463ae42a874b7f5a0e38029bf122c9957d89e172.jpg)

(b) Relative improvement of KM over IM  
![](/api/attachments/N3J3H3GY/fulltext/images/bb019f61d14dbe7aba3a74d686d8461239bf6ae1e7294f065aedd28e8bcbf0fe.jpg)

the figure, we find that KM always performs better than IM, and IM, in turn, generally outperforms the True tree. Statistical tests confirmed that both performance differences are significant with a p-value of less than 0.01. Also, the advantage of KM over IM is generally higher when the distortion is around 0.5 than when it is near 0 or 1. These conclusions are consistent with our findings using simulated data.

## 4.7. Dependent Noise

So far, we have assumed that the observed state of each input is conditionally independent of the observed state of other inputs given the true states of the inputs. Under this assumption, the probability that a user lies about one input is independent of whether she lies about other inputs. To test the robustness of the methods in situations when the above assumption is violated, we conducted a series of experiments using the credit approval data set. The KM and IM methods were used assuming that the distortions in the input variables were independent. However, in the testing phase, the distortions of the 5 of the 15 variables were made to be dependent. Specifically, if a user lied about the first of these five input variables, then she is more likely to lie about the other four input variables. We define $R ,$ the distortion dependence ratio, as $\alpha _ { L } / \alpha _ { T } ,$ , where the distortion level is $\alpha _ { L }$ for the four inputs when the user lied on the first input, and $\alpha _ { T }$ otherwise. The weighted average of $\alpha _ { L }$ and $\alpha _ { T }$ was used in the design phase for KM and IM. We vary R from 1 to 10 in the experiments. Figure 9 shows the accuracy of the three methods when the distortions in the first five variables are interdependent. From the figure we find that the performance ordering KM > IM > True is preserved under dependent noise. We repeated this experiment 10 more times by selecting other sets of five variables and found that the ordering KM > IM > True is still preserved in most cases. The inequalities KM > IM and IM > True are statistically significant with a p-value of less than 0.001.

Figure 9 Impact of Dependent Error Generation  
![](/api/attachments/N3J3H3GY/fulltext/images/0e687867128c3350e0c1f70bf88f86cc18bac766eebe35257e0ee85d13892c44.jpg)

## 5. Variations of KM and IM

In addition to the KM and IM methods, we consider two variations of these methods, denoted by KM-V and IM-H. We first present these variations and then compare all four methods along two dimensions: accuracy and complexity.

## 5.1. KM-V

Similar to KM, the KM-V method also modifies the knowledge base to account for user input noise. The difference between the KM and KM-V methods lies in how the recommendation is generated for a given observed vector. As discussed in §3, the KM method modifies the knowledge base using the most likely outcome given an observed vector. The KM-V method, on the other hand, modifies the knowledge base using the outcome of the most likely true vector given an observed vector. Thus, Step 2 of the KM method is replaced by the following step in KM-V:

Step 2 (KM-V). Given an observed input vector, find the true vector with the highest conditional probability, and choose the recommendation associated with this most likely true vector as the KM-V recommendation for the observed vector.

We expect KM-V to be less accurate than KM but, in some situations, require less computational effort.

## 5.2. IM-H

Similar to the IM method, the IM-H method directly modifies input data to account for noise. The IM-H method also acquires inputs based on the True tree structure, and after observing an input follows the branch that corresponds to the most likely true state for that input. The difference between IM and IM-H lies in the conditioning event: IM determines the most likely true state for the current variable conditioned only on the observed state of the current variable, while IM-H finds the most likely true state based on the observed state of the current variable as well as the observed states of previously acquired variables in the path of the tree. The detailed probability calculation formulas for both IM and IM-H are shown in Appendix C. We expect IM-H to be more accurate than IM but also require more computational effort.

## 5.3. Accuracy

We conduct additional experiments to compare the performance of all four methods with the True decision tree. The noise and dependency level are randomly chosen. Table 4 summarizes the performance differences across the four proposed methods based on 1,000 observations. The results strongly (with a p-value of less than 0.001) support the following accuracy ordering: KM > KM-V > IM-H > IM. From Table 4, we find that the differences within the two knowledge modification methods and within the two input modification methods are not substantial.

When all input variables are mutually independent, we are able to show the following (proof in Appendix D):

Proposition 3. If all input variables are mutually independent, then KM-V, IM, and IM-H always provide the same recommendation.

In Proposition 3, the conclusion concerning IM and IM-H is intuitive. If all variables are independent, then the observed states of other variables will not provide any information on the true state of a given variable. With respect to the KM-V method, it can be shown that if the input variables are mutually independent, then the most likely true vector can be obtained by choosing the most likely true state for each variable based only on the observed state of that variable. As shown in Appendix D, this simplification makes KM-V essentially the same as the IM method.

Table 4 Performance Comparison Across Methods

<table><tr><td>Method</td><td>TRUE</td><td>KM</td><td>KM-V</td><td>IM</td><td>IM-H</td></tr><tr><td>Mean accuracy</td><td>0.543</td><td>0.647</td><td>0.632</td><td>0.601</td><td>0.612</td></tr><tr><td>Std. dev.</td><td>0.186</td><td>0.160</td><td>0.172</td><td>0.174</td><td>0.171</td></tr></table>

## 5.4. Complexity

We examine the computational complexity involved in the knowledge base modification for KM and KM-V, and the effort required to compute the IM and IM-H recommendations for all possible observed vectors. If the number of variables is n and the maximum number of states for all variables is r, then it can be shown that the worst-case complexity associated with IM-H is $O ( n ^ { 2 } r ^ { 3 n } )$ , that of KM and KM-V is $O ( n r ^ { 2 n } )$ , and that of IM is just $O ( n r ^ { 2 } )$ . Therefore, the IM-H method is computationally more expensive than the two knowledge base modification methods, and the two knowledge modification methods are, in turn, more complex than the IM method.

We conducted experiments to study the average computational effort required for redesign. The program was coded in C and run on a PC with an Intel Celeron 1.80 GHz processor. We varied the number of binary variables from 5 to 12, and recorded the computation times for each method. The results are summarized in Table 5. We find that the redesign times for KM, KM-V, and IM-H all increase exponentially with the number of variables. For example, when the number of variables increases from 11 to 12, the redesign times for KM and KM-V increases by a factor of $2 ^ { \hat { 2 } }$ (approximately), and that for IM-H increases by a factor of about 2<sup>3</sup>. As expected, IM takes very little time. From Table 5, we can see that in the 12-variable case, IM-H is close to three orders of magnitude more time-consuming than KM and KM-V, and KM and KM-V are almost three orders of magnitude more time-consuming than IM. The experimental complexity ordering indicated in Table 5 is consistent with the theoretical complexity ordering.

## 5.5. Summary of Results

Based on our analyses, we conclude that the knowledge base modification methods outperform the input modification methods in terms of accuracy. Within the two knowledge base modification methods, KM performs better than KM-V. Except for mutually independent inputs, the computational effort required for the two methods is similar. When the inputs are mutually independent, KM-V requires much less effort than KM; however, for this condition, KM-V only performs as well as IM. Therefore, we recommend KM over KM-V. In general, IM-H does not show much superiority over IM in terms of accuracy, while the computation overhead of IM-H is several orders of magnitude higher. Therefore, we do not recommend IM-H. In summary, in choosing an appropriate method for expert system redesign, we only need to consider the KM and IM methods. The advantage of KM over IM is its accuracy, while the advantage of IM over KM is its simplicity. Therefore, in situations where computational cost of redesign is not a major concern, KM should be used. On the other hand, in situations where frequent knowledge base recomputation is costly or infeasible, IM may be preferable.

Table 5 Total KB Redesign Time vs. Number of Binary Variables (in Milliseconds)

<table><tr><td rowspan="2">Method</td><td colspan="8"># of var.</td></tr><tr><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>KM</td><td>0</td><td>0</td><td>8</td><td>24</td><td>180</td><td>711</td><td>3,930</td><td>14,227</td></tr><tr><td>KM-V</td><td>0</td><td>0</td><td>8</td><td>40</td><td>165</td><td>695</td><td>4,165</td><td>14,335</td></tr><tr><td>IM</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>16</td><td>16</td></tr><tr><td>IM-H</td><td>0</td><td>16</td><td>110</td><td>750</td><td>17,937</td><td>170,110</td><td>1,578,885</td><td>11,893,787</td></tr></table>

## 6. Discussion and Future Research

Although uncertainty in input data is a real obstacle to the widespread deployment of expert systems that acquire information from users in a sequential manner, we know of no previous research that has addressed this problem. This research analyzes the situation where the organization wishes to compensate for noisy inputs to make the best possible recommendation. There are several related issues in the context of noisy inputs that merit further research. First, a more general objective would be to maximize the overall system value to the organization by explicitly considering trade-offs between the costs associated with acquiring the noisy input data with the error costs associated with possible incorrect decisions that may result from making recommendations without fully resolving all the uncertainty in the decisionmaking process. Second, a more general model of noise could allow errors in one input to be related to errors in another. This could happen where the input variables are not independent of each other, and users provide (inadvertently or purposefully) incorrect input values. Finally, users could attempt to “beat” the system by providing incorrect inputs. Our future research will address these issues.

Two further variants of the KM method may be considered. Under the first variant, we would still pick the most likely outcome, but as an additional step require that the probability of this outcome be higher than a certain threshold. The use of a threshold becomes especially relevant when the different recommendations are evaluated to be more or less uniformly distributed. For example, with three possible recommendations, if the probability of each recommendation is close to one-third, then it may be unacceptable to use any of these recommendations. The question of course arises as to what needs to be done under such circumstances. The most obvious solution is to flag this case as one that requires more information to solve; i.e., information outside the existing set of inputs must be brought to bear on the problem. Another solution is to try to improve the measurement quality within the existing set of inputs (e.g., attempt to reduce the level of distortion through resampling or other such means). The second variant is to use the recommendation that minimizes error cost. To use an error cost approach, it is necessary to come up with misclassification costs of the kind $C ( R _ { i } , R _ { j } )$ , where $R _ { i }$ is the correct recommendation for a given observed state and $R _ { j }$ is the chosen recommendation. With the use of such misclassification costs, the recommendation that minimizes the expected misclassification cost can be found. We are, however, somewhat ambivalent about the use of the error cost minimizing recommendation because it may be controversial to apply misclassification costs in a problem domain where human expertise is the “gold standard” for the knowledge. On the other hand, if the rules are being induced from data, the use of misclassification costs to arrive at the least cost recommendation is more acceptable.

## Appendix

## A. Proof of Proposition 1

We denote the true input vector by True and observed input vector by Obs. The state of the ith variable in True and Obs is denoted by True and Obs , respectively. If all of the diagonal elements of a distortion matrix are $( 1 - \alpha )$ , then the distortion of the variable is  (assume $\alpha < 1 / 2 )$ .

KM. We first find a distortion level $\alpha _ { 1 }$ such that the KM method will always produce the same recommendation as the one given by the True tree. Based on Assumptions 1 and 2 discussed in $\ S 2 ,$ we obtain the following conditional probabilities when $\bar { \mathbf { V } } ^ { O }$ is observed:

$$
P (\mathbf {T r u e} = \mathbf {V} ^ {O} \mid \mathbf {O b s} = \mathbf {V} ^ {O}) = \frac {P (\mathbf {T r u e} = \mathbf {V} ^ {O})}{P (\mathbf {O b s} = \mathbf {V} ^ {O})} (1 - \alpha) ^ {N}.\tag{A1}
$$

$$
\begin{array}{l} P (\mathbf {T r u e} \neq \mathbf {V} ^ {O} \mid \mathbf {O b s} = \mathbf {V} ^ {O}) \\ = \sum_ {\mathbf {V} ^ {r} \neq V ^ {O}} \frac {P (\mathbf {T r u e} = \mathbf {V} ^ {r})}{P (\mathbf {O b s} = \mathbf {V} ^ {O})} \prod_ {i} P (O b s _ {i} = V _ {i} ^ {O} \mid T r u e _ {i} = V _ {i} ^ {r}) \\ <   \frac {1}{P (\mathbf {O b s} = \mathbf {V} ^ {O})} \sum_ {\mathbf {V} ^ {r} \neq V ^ {O}} [ P (\mathbf {T r u e} = \mathbf {V} ^ {r}) (1 - \alpha) ^ {N - 1} \alpha ] \\ = \frac {1}{P (\mathbf {O b s} = \mathbf {V} ^ {O})} [ 1 - P (\mathbf {T r u e} = \mathbf {V} ^ {O}) ] (1 - \alpha) ^ {N - 1} \alpha . \end{array}\tag{A2}
$$

Apparently, a sufficient condition for the KM recommendation to be the same as that given by the True tree when $\mathbf { V } ^ { O }$ is observed is $( \mathrm { A } 1 ) \geq ( \mathrm { A } 2 )$ , which is equivalent to

$$
\begin{array}{r l} P (\mathbf {T r u e} = \mathbf {V} ^ {O}) (1 - \alpha) & \geq [ 1 - P (\mathbf {T r u e} = \mathbf {V} ^ {O}) ] \alpha \\ & \Rightarrow \alpha \leq P (\mathbf {T r u e} = \mathbf {V} ^ {O}). \end{array}\tag{A3}
$$

If we let $\alpha _ { 1 } = P ( \mathbf { T r u e } = \mathbf { V } ^ { \mathrm { m i n } } )$ , where $\mathbf { V } ^ { \mathrm { m i n } }$ satisfies $P ( \mathbf { T r u e } =$ $\mathbf { V } ^ { \mathrm { m i n } } ) \leq P ( \mathbf { T r u e } = \mathbf { V } ^ { r } ) , \forall \mathbf { V } ^ { r } \neq \mathbf { V } ^ { \mathrm { m i n } }$ , then based on the above derivation, we conclude that regardless of what is observed, the KM method will always give the same recommendation as given by True tree.

IM. If we can find a distortion level $\alpha _ { 2 }$ such that regardless of what is observed, the most likely true state for each variable is always the observed state itself, then it is guaranteed the IM method will always produce the same recommendation as the one given by the True tree. We first obtain the two conditional probabilities given an observed state for the ith variable:

$$
P \big (T r u e _ {i} = V _ {i} ^ {O} \mid O b s _ {i} = V _ {i} ^ {O} \big) = \frac {(1 - \alpha) P \big (T r u e _ {i} = V _ {i} ^ {O} \big)}{P \big (O b s _ {i} = V _ {i} ^ {O} \big)},\tag{and}
$$

(A4)

$$
P \big (T r u e _ {i} = V _ {i} ^ {j} \neq V _ {i} ^ {O} \mid O b s _ {i} = V _ {i} ^ {O} \big) \leq \frac {\alpha \cdot P \big (T r u e _ {i} = V _ {i} ^ {j} \big)}{P \big (O b s _ {i} = V _ {i} ^ {O} \big)}.\tag{A5}
$$

For the most likely true state to be the same as the observed state, the following is necessary:

$$
\alpha <   \frac {P \big (T r u e _ {i} = V _ {i} ^ {O} \big)}{P \big (T r u e _ {i} = V _ {i} ^ {O} \big) + P \big (T r u e _ {i} = V _ {i} ^ {j} \big)}, \quad \forall V _ {i} ^ {j} \neq V _ {i} ^ {O}.\tag{A6}
$$

We denote the least and most likely state for the ith variable by $S _ { i } ^ { \mathrm { L L } } \mathrm { a n d } S _ { i } ^ { \mathrm { M L } }$ , and define $\alpha _ { i }$ as:

$$
\alpha_ {i} = \frac {P (T r u e _ {i} = S _ {i} ^ {\mathrm{LL}})}{P (T r u e _ {i} = S _ {i} ^ {\mathrm{LL}}) + P (T r u e _ {i} = S _ {i} ^ {\mathrm{ML}})}.\tag{A7}
$$

By enforcing $\alpha < \alpha _ { 2 } = \operatorname* { m i n } _ { i } \{ \alpha _ { i } \}$ , (A6) holds for all variables. Therefore, the condition $\alpha < \alpha _ { 2 }$ ensures that IM and the True tree always produce the same recommendation.

In summary, if the distortions of all variables are below $\alpha _ { 0 } = \operatorname* { m i n } \{ \alpha _ { 1 } , \alpha _ { 2 } \} .$ , it is guaranteed that KM and IM always produce the same recommendation as the one given by the True tree.

We have assumed that the diagonal elements of each distortion matrix are equal in the discussion. Even if this is not the case, as long as the smallest diagonal element is greater than $( 1 - \alpha _ { 0 } ) .$ , KM and IM always give the same recommendation as the one provided by the True tree.

## B. Proof of Proposition 2

Suppose the vth input variable has S possible states and its distortion matrix satisfies the condition specified in Proposition 2. Let $O _ { k } , T _ { l } \left( k , l = 0 , 1 , \ldots , S - 1 \right)$ denote the observed states and the true states for this variable. Then, for all $O _ { k } ,$ the following always holds:

$$
P (O _ {k} \mid T _ {l}) = P (O _ {k} \mid T _ {n}), \quad \forall l \neq n, l, n = 0, 1, \dots , S - 1.\tag{A8}
$$

Therefore, we can denote the conditional probability in the kth column by $P ( O _ { k } \mid T )$ such that

$$
P (O _ {k} \mid T) = P (O _ {k} \mid T _ {l}), \quad \forall l = 0, 1, \ldots , S - 1.\tag{A9}
$$

Proof of -a. We divide all true input vectors into M groups so that all rules in the same group have the same outcome in the True decision table. Let $G _ { m }$ represent the set of rules that have the same outcome, where $m = 0 , 1 , \ldots , M - 1$ is the index on different outcomes. We define $P _ { m } ( \mathbf { O b s } ^ { O } )$ as the probability that one of the rules in $G _ { m }$ is the true input vector if $\mathbf { O b s } ^ { O }$ is the observed input vector. Based on the two assumptions given in $\ S 2 ,$ we have

$$
\begin{array}{l} P _ {m} (\mathbf {O b s} ^ {O}) = \sum_ {r \in G _ {m}} P (\mathbf {T r u e} ^ {r} \mid \mathbf {O b s} ^ {O}) \\ \qquad = \frac {1}{P (\mathbf {O b s} ^ {O})} \sum_ {r \in G _ {m}} \bigg [ P (\mathbf {T r u e} ^ {r}) \prod_ {i} P \big (O b s _ {i} ^ {O} \mid T r u e _ {i} ^ {r} \big) \bigg ] \\ \qquad = \frac {P \big (O b s _ {v} ^ {O} \mid T \big)}{P (\mathbf {O b s} ^ {O})} \sum_ {r \in G _ {m}} \bigg [ P (\mathbf {T r u e} ^ {r}) \prod_ {i \neq v} P \big (O b s _ {i} ^ {O} \mid T r u e _ {i} ^ {r} \big) \bigg ]. \end{array}\tag{A10}
$$

The KM recommendation for $\mathbf { O b s } ^ { O }$ is the same as the outcome for $G _ { B }$ (the group of rules with the highest probability sum) if $P _ { B } ( \mathbf { \bar { O } b s } ^ { O } ) \geq P _ { m } ^ { \mathbf { \bar { ( } } \mathbf { O b s } ^ { O } ) }$ m, which is equivalent to:

$$
\begin{array}{l} \sum_ {r \in G _ {B}} \bigg [ P (\mathbf {T r u e} ^ {r}) \prod_ {i \neq v} P \big (O b s _ {i} ^ {O} \mid T r u e _ {i} ^ {r} \big) \bigg ] \\ \geq \sum_ {r \in G _ {m}} \bigg [ P (\mathbf {T r u e} ^ {r}) \prod_ {i \neq v} P \big (O b s _ {i} ^ {O} \mid T r u e _ {i} ^ {r} \big) \bigg ], \quad \forall   m. \end{array}\tag{A11}
$$

By varying only the state of the vth variable of $\mathbf { O b s } ^ { O } ,$ , we can obtain a total of $S - 1$ different observed input vectors. These vectors have the same value for all variables except the vth variable. For any one of them, denoted by $\mathbf { O b s } ^ { P } ,$ we have the following:

$$
\begin{array}{l} P _ {m} \left(\mathbf {O b s} ^ {P}\right) = \frac {P \left(O b s _ {v} ^ {P} \mid T\right)}{P \left(\mathbf {O b s} ^ {P}\right)} \sum_ {r \in G _ {m}} \left[ P \left(\mathbf {T r u e} ^ {r}\right) \prod_ {i \neq v} P \left(O b s _ {i} ^ {P} \mid T r u e _ {i} ^ {r}\right) \right] \\ = \frac {P \left(O b s _ {v} ^ {P} \mid T\right)}{P \left(\mathbf {O b s} ^ {P}\right)} \sum_ {r \in G _ {m}} \left[ P \left(\mathbf {T r u e} ^ {r}\right) \prod_ {i \neq v} P \left(O b s _ {i} ^ {O} \mid T r u e _ {i} ^ {r}\right) \right] \\ (\text {since} O b s _ {i} ^ {O} = O b s _ {i} ^ {P} \text {for} i \neq v). \end{array} \tag {A12}
$$

Multiplying both sides of (A11) by $P ( O b s _ { v } ^ { P } \mid T ) / P ( \mathbf { O b s } ^ { P } )$ we have:

$$
P _ {B} (\mathbf {O b s} ^ {P}) \geq P _ {m} (\mathbf {O b s} ^ {P}), \quad \forall m.\tag{A13}
$$

Therefore, the KM outcome for $\mathbf { O b s ^ { P } }$ is the same as that for $\mathbf { O b s } ^ { O }$ . Analogously, we find that all observed vectors that differ from $\tilde { \mathbf { O b s } } ^ { O }$ only in the vth variable receive the same KM recommendation as that for $\mathbf { O b s } ^ { O }$ . Consequently, the S rules that differ only in the state of the vth variable in the KM table can be compressed into one rule with $\hat { \textbf { d } } ^ { \prime \prime } - \mathbf { \Lambda } ^ { \prime \prime }$ value for that variable.

Similarly, all other sets of observed vectors that only differ in the state of the vth variable can also be condensed into one rule. Consequently, in the final condensed KM table, there will be only $\mu _ { - } \bar { { \mathbf { \zeta } } } _ { \prime \prime }$ values for variable v and thus the variable will not appear in the KM tree.

Proof of -b. From (A14) below, we conclude that under this case the most likely true state is always the one with the highest prior distribution, regardless of what is observed. Therefore, the IM recommendation is independent of the observed state of the vth variable.

$$
P (T _ {l} \mid O _ {0}) = \frac {P (O _ {0} \mid T _ {l}) P (T _ {l})}{P (O _ {0})} = \frac {P (O _ {0} \mid T)}{P (O _ {0})} P (T _ {l}).\tag{A14}
$$

## C. Calculating the Most Likely True State for IM and IM-H

We denote the ith variable reached in a consultation process by $X _ { ( i ) }$ . The variables examined before $X _ { ( i ) }$ are therefore $X _ { ( 0 ) } , \dot { X } _ { ( 1 ) } , \dot { \ldots } , X _ { ( i - 1 ) }$ . The true value of $X _ { ( i ) }$ is denoted by $X _ { ( i ) } ^ { T } ,$ and the observed value of $X _ { ( i ) }$ is denoted by $X _ { ( i ) } ^ { O }$ . At each node, IM chooses the most likely $X _ { ( i ) } ^ { T }$ based on $\ddot { P ( X _ { ( i ) } ^ { T } \mid X _ { ( i ) } ^ { O } ) }$ which is obtained as shown below.

$$
P \big (X _ {(i)} ^ {T} = x _ {j} \mid X _ {(i)} ^ {O} \big) = \frac {P \big (X _ {(i)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {T} = x _ {j} \big)}{\sum_ {X _ {(i)} ^ {T}} P \big (X _ {(i)} ^ {O} \mid X _ {(i)} ^ {T} \big) P \big (X _ {(i)} ^ {T} \big)}\tag{A15}
$$

IM-H makes the decision based on $P ( X _ { ( i ) } ^ { T } \mid X _ { ( i ) } ^ { O } , X _ { ( i - 1 ) } ^ { O } , . . . ,$ $X _ { ( 0 ) } ^ { O } )$ , calculated as shown below.

$$
\begin{array}{l} P \big (X _ {(i)} ^ {T} = x _ {j} \mid X _ {(i)} ^ {O}, X _ {(i - 1)} ^ {O}, \ldots , X _ {(0)} ^ {O} \big) \\ = \frac {P \big (X _ {(i)} ^ {O} , X _ {(i - 1)} ^ {O} , \ldots , X _ {(0)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {T} = x _ {j} \big)}{\sum_ {X _ {(i)} ^ {T}} P \big (X _ {(i)} ^ {O} , X _ {(i - 1)} ^ {O} , \ldots , X _ {(0)} ^ {O} \mid X _ {(i)} ^ {T} \big) P \big (X _ {(i)} ^ {T} \big)}, \end{array}\tag{A16}
$$

where

$$
\begin{array}{l} P \big (X _ {(i)} ^ {O}, X _ {(i - 1)} ^ {O}, \ldots , X _ {(0)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {T} = x _ {j} \big) \\ = P \big (X _ {(i)} ^ {T} = x _ {j} \big) \sum_ {X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T}} P \big (X _ {(i)} ^ {O}, X _ {(i - 1)} ^ {O}, \ldots , X _ {(0)} ^ {O}, \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T} \mid X _ {(i)} ^ {T} = x _ {j} \big) \\ = P \big (X _ {(i)} ^ {T} = x _ {j} \big) \sum_ {X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T}} \big [ P \big (X _ {(i)} ^ {O}, X _ {(i - 1)} ^ {O}, \ldots , X _ {(0)} ^ {O} \mid X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T}, \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T} \mid X _ {(i)} ^ {T} = x _ {j} \big) \big ] \\ = P \big (X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) \sum_ {X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T}} \big [ P \big (X _ {(i - 1)} ^ {O} \mid X _ {(i - 1)} ^ {T} \big) \\ \qquad \qquad \qquad \times \dots \times P \big (X _ {(0)} ^ {O} \mid X _ {(0)} ^ {T} \big) P \big (X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T} \mid X _ {(i)} ^ {T} = x _ {j} \big) \big ] \end{array}
$$

(the last equality follows from Assumptions 1 and 2).

If the variables are not independent, the conditional probability $P ( X _ { ( i - 1 ) } ^ { T } , \ldots , X _ { ( 0 ) } ^ { T } \mid X _ { ( i ) } ^ { T } )$ can be calculated using the True decision table.

## D. Proof of Proposition 3

IM and IM-H Will Always Give the Same Recommendation. We adopt the same notation in Appendix C. To prove that IM-H and IM always give the same recommendation when the variables are independent, we only need to prove $P ( X _ { ( i ) } ^ { T } \mid X _ { ( i ) } ^ { O } ) = P ( X _ { ( i ) } ^ { T } \mid X _ { ( i ) } ^ { O } , \dot { X } _ { ( i - 1 ) } ^ { O } , \ldots , X _ { ( 0 ) } ^ { O } )$ for every node in every path. We first examine the conditional probability for IM-H. The denominator in the right-hand side of (A16) can be further simplified if the variables are independent:

$$
\begin{array}{l} P \big (X _ {(i)} ^ {O}, X _ {(i - 1)} ^ {O}, \ldots , X _ {(0)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {T} = x _ {j} \big) \\ \qquad = P \big (X _ {(i)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {T} = x _ {j} \big) \\ \qquad \cdot \sum_ {X _ {(i - 1)} ^ {T}, \ldots , X _ {(0)} ^ {T}} \big [ P \big (X _ {(i - 1)} ^ {O} \mid X _ {(i - 1)} ^ {T} \big) P \big (X _ {(i - 1)} ^ {T} \big) \big ] \\ \qquad \times \dots \times \big [ P \big (X _ {(0)} ^ {O} \mid X _ {(0)} ^ {T} \big) P \big (X _ {(0)} ^ {T} \big) \big ] \\ \qquad = P \big (X _ {(i)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {T} = x _ {j} \big) \prod_ {k = 0} ^ {i - 1} P \big (X _ {(k)} ^ {O} \big). \end{array}\tag{A17}
$$

Substituting (A17) into the right-hand side of (A16) and canceling the common term $\textstyle \prod _ { k = 0 } ^ { i - 1 } P ( X _ { ( k ) } ^ { O } )$ in the numerator and denominator, we have

$$
\begin{array}{l} P \big (X _ {(i)} ^ {T} = x _ {j} \mid X _ {(i)} ^ {O}, X _ {(i - 1)} ^ {O}, \ldots , X _ {(0)} ^ {O} \big) \\ = \frac {P \big (X _ {(i)} ^ {O} \mid X _ {(i)} ^ {T} = x _ {j} \big) P \big (X _ {(i)} ^ {T} = x _ {j} \big)}{\sum_ {X _ {(i)} ^ {T}} P \big (X _ {(i)} ^ {O} \mid X _ {(i)} ^ {T} \big) P \big (X _ {(i)} ^ {T} \big)} = P \big (X _ {(i)} ^ {T} = x _ {j} \mid X _ {(i)} ^ {O} \big). \end{array}\tag{A18}
$$

IM and KM-V Will Always Give the Same Recommendation. It can be shown that if the input variables are mutually independent, then the most likely true vector can be obtained by choosing the most likely true state based on the observed state for every variable. If we feed this most likely true vector into the True tree, we will find that the tree path traversed is exactly the same as the path traversed under the IM method if the same observed vector is used. Therefore we conclude that IM and KM-V will always give the same recommendation if the variables are independent.

## References

Berger, J. O. 1985. Statistical Decision Theory and Bayesian Analysis. Springer Series in Statistics. Springer, New York.

Breslow, L. A., D. W. Aha. 1997. Simplifying decision trees: A survey. Knowledge Engrg. Rev. 12(1) 1–40.

Clark, P., T. Niblett. 1989. The CN2 induction algorithm. Machine Learning 3(4) 261–283.

Delisio, J., M. McGowan, W. Hamscher. 1993. PLANET: An expert system for audit risk assessment and planning. 5th Annual Conf. Intelligent Systems Accounting, Finance Management, Stanford University, Stanford, CA (November 11–13).

Fox, Susannah, L. Rainie, J. Horrigan, A. Lenhart, T. Spooner, C. Carter. 2000. Trust and privacy online: Why Americans want to rewrite the rules. The Pew Internet and American Life Project Report (August 20). http://www.pewinternet.org/ reports/pdfs/PIP\_Trust\_Privacy\_Report.pdf.

Graham, L. E., J. Damens, G. Van Ness. 1991. Developing risk advisor: An expert system for risk identification. Auditing 10(1) 69–96.

Hirsh, H. 1994. Generalizing version space. Machine Learning 17 5–46.

Hong, T. P., J. B. Chen. 2000. Processing individual fuzzy attributes for fuzzy rule induction. Fuzzy Sets Systems 112(1) 127–140.

Hong, T. Z., S. S. Tsang. 1997. A generalized version space learning algorithm for noisy and uncertain data. IEEE Trans. Knowledge Data Engrg. 9(2) 336–340.

Lee, C. C. 1990. Fuzzy logic in control systems: Fuzzy logic controller—Part I and Part II. IEEE Trans. Systems, Man, Cybernetics 20(2) 404–435.

Mingers, J. 1989. An empirical comparison of pruning methods for decision tree induction. Machine Learning 4(2) 227–243.

Mookerjee, V., M. Mannino. 1997. Sequential decision models for expert system optimization. IEEE Trans. Knowledge Data Engrg. 9(5) 675–687.

Mookerjee, V., M. Mannino, R. Gilson. 1995. Improving the performance stability of inductive expert systems under input noise. Inform. Systems Res. 6(4) 328–356.

Quinlan, J. R. 1986. The effect of noise on concept learning. R. S. Michalski, J. G. Carbonell, T. M. Mitchell, eds. Machine Learning, Vol. 2. Morgan Kaufmann, Los Altos, CA, 149–166.

Reinwald, L., R. Soland. 1966. Conversion of limited-entry decision tables to optimal computer programs. J. ACM 13(3) 339–358.

Schwayder, K. 1974. Extending the information theory approach to converting limited-entry decision tables to computer programs. Comm. ACM 17(9) 532–537.

Tapscott, D. 1999. IBM is showing leadership on the privacy issue. Computerworld 33(17) 34 (April 26).

Turban, E., J. E. Aronson. 2000. Decision Support Systems and Intelligent Systems. Prentice Hall, Englewood Cliffs, NJ.

Wu, W. Z., W. X. Zhang, H. Z. Li. 2003. Knowledge acquisition in incomplete fuzzy information systems via the rough set approach. Expert Systems 20(5) 280–286.
