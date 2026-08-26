---
otero_id: 8148
otero_key: "XZ82P2CR"
title: "<b>Research Note</b>—Toward a Causal Interpretation from Observational Data: A New Bayesian Networks Method for Structural Models with Latent Variables"
authors: "Zhiqiang (Eric) Zheng; Paul A. Pavlou"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0224"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/XZ82P2CR/fulltext/images/d2c76336cd370fd1935822c147575ef082956ece01a9c9df9ccdd9fd8596461c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Note—Toward a Causal Interpretation from Observational Data: A New Bayesian Networks Method for Structural Models with Latent Variables

Zhiqiang (Eric) Zheng, Paul A. Pavlou,

Zhiqiang (Eric) Zheng, Paul A. Pavlou, (2010) Research Note—Toward a Causal Interpretation from Observational Data: A New Bayesian Networks Method for Structural Models with Latent Variables. Information Systems Research 21(2):365-391. http:// dx.doi.org/10.1287/isre.1080.0224

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XZ82P2CR/fulltext/images/f00de810c0a12423db45b41f6dd491827e8ac873b981ce348dce68543b69843e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Toward a Causal Interpretation from Observational Data: A New Bayesian Networks Method for Structural Models with Latent Variables

Zhiqiang (Eric) Zheng

School of Management, University of Texas at Dallas, Richardson, Texas 75083, ericz@utdallas.edu

Paul A. Pavlou

Fox School of Business and Management, Temple University, Philadelphia, Pennsylvania 19122, pavlou@temple.edu

ecause a fundamental attribute of a good theory is causality, the information systems (IS) literature has Bstrived to infer causality from empirical data, typically seeking causal interpretations from longitudinal, experimental, and panel data that include time precedence. However, such data are not always obtainable and observational (cross-sectional, nonexperimental) data are often the only data available. To infer causality from observational data that are common in empirical IS research, this study develops a new data analysis method that integrates the Bayesian networks (BN) and structural equation modeling (SEM) literatures.

Similar to SEM techniques (e.g., LISREL and PLS), the proposed Bayesian networks for latent variables (BN-LV) method tests both the measurement model and the structural model. The method operates in two stages: First, it inductively identifies the most likely LVs from measurement items without prespecifying a measurement model. Second, it compares all the possible structural models among the identified LVs in an exploratory (automated) fashion and it discovers the most likely causal structure. By exploring the causal struc tural model that is not restricted to linear relationships, BN-LV contributes to the empirical IS literature by overcoming three SEM limitations (Lee, B., A. Barua, A. B. Whinston. 1997. Discovery and representation of causal relationships in MIS research: A methodological framework. MIS Quart. 21(1) 109–136)—lack of causality inference, restrictive model structure, and lack of nonlinearities. Moreover, BN-LV extends the BN literature by (1) overcoming the problem of latent variable identification using observed (raw) measurement items as the only inputs, and (2) enabling the use of ordinal and discrete (Likert-type) data, which are commonly used in empirical IS studies.

The BN-LV method is first illustrated and tested with actual empirical data to demonstrate how it can help reconcile competing hypotheses in terms of the direction of causality in a structural model. Second, we conduct a comprehensive simulation study to demonstrate the effectiveness of BN-LV compared to existing techniques in the SEM and BN literatures. The advantages of BN-LV in terms of measurement model construction and structural model discovery are discussed.

Key words: causality; Bayesian networks; structural equation modeling; observational data; Bayesian graphs History: Vallabh Sambamurthy, Senior Editor and Associate Editor. This paper was received on October 25, 2006, and was with the authors 20 months for 2 revisions. Published online in Articles in Advance May 12, 2009.

## 1. Introduction

Because a fundamental attribute of a good theory is causality (Bagozzi 1980), causality inference (X causes Y ) is deemed invaluable in the social and behavioral sciences in general and information systems (IS) research in particular. However, despite the enhanced sophistication of IS studies in terms of theory and empirical testing, causality has not received the requisite attention. Similar to most other disciplines (e.g., Mitchell and James 2001, Shugan 2007), the IS discipline tends to avoid issues of causality because of the difficulty in inferring causal relationships from data, and because causality is only inferred from pure theory. This is partly because of the fact that causality inference requires strict conditions. Though there is no consensus on the necessary and sufficient conditions for inferring causality, Popper’s (1959) three conditions for inferring causality are generally accepted: (1) X precedes Y ; (2) X and Y are related; and (3) no confounding factors explain the X <sub>→</sub> Y relationship. To satisfy these strict conditions, researchers need to use longitudinal, experimental, or panel data with time precedence between variables X and Y to account for confounds and reverse causality (Allison 2005).<sup>1</sup> However, it is often impossible to obtain such data in IS research (Mithas et al. 2006, p. 223) and observational (cross-sectional, nonexperimental) data are often the only data available. Therefore, our objective is to develop a method to help infer causality using observational data that are commonly used in empirical IS research.

Following the literature that maintains that “near” (versus “absolute”) causality inference is possible from observational data (e.g., Granger 1986, Holland 1986), we develop a new data analysis method built on the Bayesian networks (BN) and structural equation modeling (SEM) literature that offers a causal interpretation to relationships among latent variables (LVs) in structural equation models.<sup>2</sup> Our proposed method (termed BN-LV—Bayesian networks for latent variables) encodes the relationships among LVs in a graphical model as conditional probabilities, it accounts for potential confounds, and it discovers the most likely causal structure from observational data. The proposed BN-LV method seeks to (1) sensitize IS researchers about the importance of causality and present the possibility to infer causal relationships from data, (2) offer a method to IS researchers to help infer causality among constructs from observational data while overcoming key SEM limitations, and (3) help spawn future research in refining SEM-based methods that render causal interpretations.

According to Lee et al. (1997), SEM methods have three key limitations: lack of causality inference, restrictive model structure, and lack of nonlinearities. First, though SEM was originally designed to model causal relationships, causality has gradually faded away from SEM studies (Pearl 2000). In fact, a review of the literature suggests that SEM studies do not attempt to infer causality, and most SEM (Cartwright 1995) and IS researchers (Gefen et al. 2000) believe that SEM models cannot infer causality.<sup>3</sup> The inability for causal inference has forced IS researchers to refrain from even discussing issues of causality in IS studies. Second, most SEM studies specify one model structure and use data to confirm or disconfirm this specific structure by operating in a confirmatory mode.<sup>4</sup> This prevents the automated exploration of alternative or equivalent models. Chin (1998) warns that overlooking equivalent models is common in SEM studies, and Breckler (1990) showed that only 1 of 72 published SEM studies even suggests the possibility of alternative models. Third, SEM only encodes linear relationships among constructs, essentially ignoring the possibility of nonlinear relationships.<sup>5</sup>

To address these three SEM limitations, we developed the BN-LV method, which has three key properties: First, it encodes the relationships among constructs as conditional probabilities that, according to Druzdzel and Simon (1993), can offer a causal interpretation (as opposed to SEM, which uses correlation that does not imply causality). Second, BN-LV can automatically discover the most likely structural model from observational data without imposing a prespecified structure, thus exploring alternative SEM models. Third, BN-LV does not rely on any functional form (e.g., linear) to capture the relationships among constructs, thus allowing potentially nonlinear relationships to freely emerge in the structural model.

Similar to existing SEM techniques (e.g., LISREL and PLS), the proposed BN-LV method operates in two stages: measurement model construction and structural model discovery.<sup>6</sup> First, BN-LV inductively identifies the LVs given the measurement items in an exploratory mode. This is achieved by our proposed LVI (Latent Variable Identification) algorithm, which is based on testing the conditional independence axiom (Kline 1998, Heinen 1996). This axiom asserts that the measurement items of the same LV are supposed to be caused by the LV and thus should be independent of each other (conditional on the LV). Second, after the LVs are identified, BN-LV exploratory discovers the most likely causal structure among the LVs. In particular, we develop the OL (ordered logit) scoring function to select competing structures specifically for ordinal and discrete (Likerttype) data, which are common in IS research. Besides, BN-LV can also be used in a confirmatory mode by examining the fitness of a potential causal structure. Overall, the inputs to the BN-LV method are the raw measurement items, and the final output is the most likely causal BN graph that links the identified LVs.

We describe how BN-LV works with actual empirical data to demonstrate how BN-LV can help reconcile competing hypotheses in terms of the directionality of causality when integrating trust with the technology acceptance model (TAM) (Gefen et al. 2003, Pavlou 2003), specifically the relationship between two constructs: trust and ease of use. Carte and Russell (2003) argue that it is a common error in IS research not to examine the reverse causality between two variables X and Y (Carte and Russell 2003, p. 487): “Investigators need to be aware of theoretical rationale justifying the X Y or Y X causal orders.” However, solely relying on theories to reconcile the directionality of causality may not be sufficient because there can be equally plausible theories, such as the direction of causality between trust and ease of use. BN-LV is particularly useful in these circumstances by providing a datadriven method to reconcile competing hypotheses. This also has implications for new theory development (where there is no theory basis), which is common in IS research because of the rapid change of IT.

To evaluate BN-LV relative to existing data analysis techniques for testing the measurement and the structural model, we conducted a large-scale simulation study by varying four data dimensions: sample size, noise, linearity, and normality. First, we compared LVI with the exploratory factor analysis (EFA) (SAS Proc Factor) and the confirmatory factor analysis (PLS) for measurement model testing. Second, we compared BN-LV with LISREL and PLS in terms of structural model testing. Third, we compared our proposed OL scoring function with two existing BN scoring functions—a Bayesian-Dirichlet-based function (Heckerman 1996) and a Gaussian-based function (Glymour et al. 1987). The results show that BN-LV overall outperforms all of the other techniques under three of the four simulated conditions (size, linearity, normality), except when the data are noisy, because SEM methods (LISREL and PLS) tend to work well with noisy data (Fornell and Larcker 1981).

This study contributes to the IS literature by proposing a new data analysis method for inferring causal relationships from observational, cross-sectional, Likert-type data that are prevalent in IS research. Our BN-LV method has several advantages over alternative SEM methods: First, it tests the measurement model by identifying the appropriate LVs from raw measurement items, operating in an exploratory mode without imposing a determined measurement model structure (as opposed to SEM). Our novel use of the conditional independence axiom enables causal interpretation between the LV and its associated measurement items, thereby being the only method that is consistent with the theory of measurement. Second, BN-LV infers causal (as opposed to correlation) links between the identified LVs by testing all plausible structural models in an automated fashion and discovering the most likely one. This exploratory nature offers a major advantage over SEM techniques that require manual specification of plausible models, especially for complex models where such manual work becomes virtually impossible. This property also becomes valuable where there is little or no prior theory to guide the structure specification or when researchers want to let the data “speak out.” Also, BN-LV can still differentiate among prespecified candidate structures, allowing IS researchers to test competing theories or question existing ones in a confirmatory mode. Finally, BN-LV offers a causal interpretation among the LVs in the structural model by representing conditional probabilities. BN-LV relaxes the assumption of linear structures imposed by SEM methods, and BN-LV clearly outperforms SEM techniques (LISREL and PLS) when the structural model is tested with nonlinear simulated data.

The paper is organized as follows. Section 2 reviews the philosophical origins of causality, discusses the challenges of inferring causality from data, and reviews existing approaches for inferring causality (propensity scores, SEM, and BN). Section 3 presents the method development for the two components of BN-LV—the LVI algorithm that identifies LVs from raw measurement items (measurement model) and the OL scoring function that helps build a Bayesian network to identify causal relationships among LVs (structural model). Section 4 describes the steps of the proposed BN-LV method and evaluates the proposed method through an extensive empirical study with actual data and a large-scale experiment with simulated data. Section 5 discusses the study’s contributions and the advantages and limitations of BN-LV.

## 2. Literature Review

## 2.1. Philosophical Origins of Causality

The notion of causality entails a relationship of a cause to its effect. As early as 350 b.c., Aristotle proposed four distinct causes: the material, the formal, the efficient, and the final.<sup>7</sup> Aristotle’s “four causes” is the basis of the modern scientific concept that specific stimuli produce standard results under certain conditions. Descartes (1637) argued that causality can be understood and that cause is identical to substance. Kant (1781) posited cause as a basic category of understanding, arguing that causality is a world of “things in themselves.”

Aristotle (350 b.c.), Descartes (1637), and Kant (1781) posit that causality can be comprehended, but other philosophers disagree. In response to Aristotle’s “four causes,” Spinoza (1662) believed that all final causes are nothing but human fictions. Plato, in his famous “Allegory of the Cave,”<sup>8</sup> questioned that humans can understand causality. Hume (1738) holds the same opinion, concluding that causality is not real but a fiction of the mind. To account for the origin of this fiction, Hume (1738) used the doctrine of association. He argues that we only learn by experience the frequent conjunction of objects, without ever being able to comprehend anything like the true causal connection between them (Hume 1738, p. 46). Similarly, Pearson (1897), a founder of modern statistics, denied that causality was anything beyond frequency of association.

Summarizing the philosophical origins on causality, there is no consensus whether causality is real, simple association among phenomena, artifact, or the mind, or even fiction (Shugan 2007). Despite these doubts that causality is real or not, throughout history there have been many attempts to operationalize and infer causality from data, as discussed below.

## 2.2. Operationalizing Causality from Data

Hume (1738) laid the foundations for the modern view of causality. Hume’s (1738) definition of X causes Y stresses three conditions that can be verified through observation: (1) precedence: X precedes Y in time; (2) contiguity: X and Y are contiguous in space and time; and (3) constant conjunction: X and Y always co-occur (or not co-occur).

Contemporary research has attempted to operationalize causality through data-driven probabilities. Suppes’ (1970) well-known operational causality definition states that event X causes event Y if the probability of Y is higher given X than without X, i.e., $P ( Y \mid X ) > P ( Y \mid { \sim } X )$ . This definition is consistent with Hume’s (1738) constant conjunction criterion, yet it makes Hume’s criterion probabilistic. A problem arises because there is often a third (confounding) factor. A common example is that atmospheric current Z causes both lightning X and thunder Y . This satisfies $P ( Y \mid X ) > P ( Y \mid \sim X )$ ; however, lightning does not cause thunder. Suppes (1970) solves this problem by necessitating that X and Y have no common cause, thus avoiding a statistical confounding. This condition is also stressed in Popper (1959) who adds a condition that no third variable Z accounts for the X–Y association. Cartwright (1995) argues that avoiding confounds requires that the relevant probabilities be assessed relative to background contexts where all other causal factors are held fixed. Probability may thus infer causality if the data from which the probabilities are computed are obtained with appropriate care to avoid confounds.

The view that conditional probability can allow for causality inference has long been proposed in the causality literature (Glymour et al. 1987, Pearl and Verma 1991, Spirtes et al. 2000). Druzdzel and Simon (1993) explain that conditional probabilities make it possible to represent asymmetries among variables and, thereby, causality. There is strong evidence that human beings are not indifferent to causal relationships and often give causal interpretation to conditional probabilities (Shugan 2007). In particular, many studies seek to operationalize causality discovery from data with conditional probabilities (e.g., Heckerman 1996, Pearl 2000).

## 2.3. Methods for Inferring Causality from Observational Data

Inferring causality can take place with temporal or cross-sectional data, with each approach having a different focus. According to Granger (1986, p. 967):

In cross-sectional causation one is asking why a particular unit is placed in a certain part of the distribution for the variable of interest. In temporal causality one is asking why parameters of that distribution have changed through time. The two types are very different in nature and probably require different definitions and methods of analysis.

The well-known Granger causality, for example, addresses causality for time-series data. Temporal causality often uses experimental methods that permit randomization (Mithas et al. 2006). However, because such data are often difficult or even impossible to obtain, we focus on methods for inferring causality from observational, cross-sectional data that are common in empirical information systems research. Causality inference from such data is well-accepted in the statistics (Holland 1986, Rubin and Waterman 2006), econometrics (Granger 1986), computer science (Druzdzel and Simon 1993), and IS literatures (Lee et al. 1997). We review three main methods—SEM, propensity scores, and BN.

2.3.1. Structural Equation Modeling (SEM). SEM is one of the most common data analysis methods in IS research. Gefen et al. (2000) report that 45% of empirical papers in Information Systems Research and 25% papers in Management Information Systems Quarterly use SEM techniques. Its popularity stems from its advantage over regression analysis, path analysis, factor analysis, panel models, and simultaneous equation models. Although SEM was originally developed to model causal relationships, SEM methods are no longer believed to infer causality (see Footnote 3). To overcome this limitation, IS researchers have attempted to extend SEM methods to allow for causality inference. Lee et al. (1997) proposed an eightstep framework that attempts to represent and discover causal relationships from SEM data. Their idea is to integrate confirmatory analysis in SEM with exploratory analysis using TETRAD.<sup>9</sup> However, Lee et al. (1997) did not elaborate on how causal relationships can be discovered from data, nor did they demonstrate how TETRAD can be integrated with SEM methods.

2.3.2. Propensity Scores. The propensity score method was originally proposed by Rosenbaum and Rubin (1983) to help assess causal effects of interventions. For example, Rubin and Waterman’s (2006)

intervention—a pharmaceutical salesman’s visit to a doctor—was shown to have a causal effect on a doctor’s drug prescription. Their approach first summarizes all covariates into a single propensity score by regressing (often through a logistic regression) the treatment (salesman’s visit) on a set of covariates. The propensity score is thus the probability of a doctor being visited as a function of all covariate variables. Mithas et al. (2006) used this approach to show the causal effect of customer relationship management applications on one-to-one marketing effectiveness. They prescribed a set of assumptions that researchers must make to infer causality with the aid of propensity scores at the individual, firm, and economy levels. However, existing propensity scores methods only deal with one cause (treatment) and one effect. They are not applicable to the causal graph discovery problem we aim to address in this paper, where the graph (or structural model) is composed of a network of multiple causes and effects.

2.3.3. Bayesian Networks (BN). BNs are graphical structural models that encode probabilistic relationships among variables (Heckerman 1996). The BN literature has made major advances in inferring causal relationships from observational data (Binder et al. 1997, Pearl 1998, Spirtes et al. 2002). We follow Heckerman’s (1996) and Friedman et al. (2000) notation to represent a generic graph (Figure 1). A graph $G \langle V , E \rangle$ is referred to as a DAG (directed acyclic graph), when the edges E linking node V are directed and acyclic. Directed means E has an asymmetric edge over $V ,$ and acyclic means that the directed edges do not form circles.

Associated with each edge is a conditional probability. A BN is a DAG that encodes a set of conditional probabilities and conditional independence assertions about variables V (Heckerman 1996). Lack of possible arcs in G encodes conditional independencies. Let $V = ( X _ { 1 } , \ldots , X _ { m } )$ , where m is the number of variables and $X _ { i }$ is both the variable and its matching node in G. Denote $\pi _ { i }$ as the parents of node X in G. As in Figure 1, node C’s parents are A and B. Given the structure in $G ,$ the joint probability distribution for V is given by:

Figure 1 A Generic Bayesian Network with Five Nodes  
![](/api/attachments/XZ82P2CR/fulltext/images/fa22c52b6742afd096ab6926e37d740b4837448ca22c55ab97050c23e86f1dad.jpg)

$$
p (x) = \prod_ {i = 1} ^ {m} p (x _ {i} \mid \pi_ {i}).\tag{1}
$$

From the chain rule of probability, we have:

$$
p (x) = \prod_ {i = 1} ^ {m} p (x _ {i} \mid x _ {1}, \ldots , x _ {i - 1}).\tag{2}
$$

A graph G represents causal relationships when there is an edge from A to $B ,$ if and only if A is a direct cause of B in G (Spirtes et al. 2002). For instance, when Figure 1 is a causal graph, an edge $A  C$ is interpreted as A is directly causing C or that C is causally dependent on A. Druzdzel and Simon (1993) introduced the basic conditions by which BN could reflect a causal structure: A BN is causal if and only if (a) each node of G and all of its predecessors describe variables involved in a separate mechanism in the graph, and (b) each node without predecessors represents an exogenous variable. More formally, a causal Bayesian network is defined in terms of d-separation and the causal Markov assumption.

d-Separation. A set of variables Z is said to d-separate variable X from variable $\boldsymbol { Y } ,$ if an only if Z blocks every path from X to Y (Pearl 2000). Graphically, d-separation typically exhibits itself in two cases: (1) $X  Z  Y$ and (2) $X \left. Z \right. Y$ . The intuition behind this is: X and Y become independent of each other if they are conditioned on variable Z. X causes Y through Z in case (1) and X and Y have a common cause Z in case (2). There is also a third case $X \right. Z ^ { \prime } \left. Y ,$ denoting that X and Y have a common effect Z	. This case is opposite to d-separation: If two variables are independent, they will become dependent once conditioned on $Z ^ { \prime }$ A set Z that d-separates X and Y should therefore not belong to $Z ^ { \prime } .$ The notion of d-separation is especially useful in constructing a BN because it controls possible confounds in the form of Z.

Causal Markov Assumption. This is the central assumption that defines a causal BN. According to this assumption, each node is independent of its nondescendants in the graph, conditional on its parents in the graph. Simply put, given a node’s immediate cause, we can disregard the causes of its ancestors. The parents of a node form the smallest set of variables for which the relevant conditional independence holds. This assumption greatly reduces the complexity of Equation (2) and the joint probability of Figure 1 simplifies to: $P ( A , B , C , D , E ) = P ( A ) \times P ( B ) \times$ $P ( C \mid A , B ) \times P ( E \mid C ) \times P ( D \mid C )$ . By accepting the causal Markov assumption, we can then infer some causal relationships from observational data (Friedman et al. 2000).

## 3. Method Development

## 3.1. Rationale and Overview of the Proposed Method

The main interest of SEM studies is the structural model, i.e., the relationships among LVs (or theoretical constructs). LVs are assumed to be unobservable phenomena that are not directly measurable. What is observable, however, are the measurement items of each LV, the raw inputs to an SEM model. SEM studies thus also address the measurement model—the relationships among the measurement items and their LVs— that test how well the LVs were actually measured.

First, given a set of measurement items, how can we identify the overarching LVs? This question does not often arise in the SEM literature because the common SEM methods (e.g., confirmatory factor analysis (CFA) in LISREL and PLS) mostly work in a confirmatory mode by prespecifying which measurement items load on which LVs (Gefen et al. 2000). Lee et al. (1997) criticize this confirmatory mode, pointing out BN as a potential alternative for exploratory analysis. However, building a BN in the presence of hidden LVs is a nontrivial problem that has long been recognized as one of the crucial, yet unsolved problems in the BN literature (Cooper 1995, Friedman 1997). There are two fundamental issues to be addressed: (1) detecting the structure (or location) of LVs, and (2) calculating the values of the identified LVs.

The BN literature only addresses the second issue without dealing with the structure problem.<sup>10</sup> Elidan and Friedman (2001) show that even learning the dimensionality—the number of possible values—of LVs is hard. Cooper (1995) and Chickering and

Heckerman (1997) consider a simple case where there only exists a single hidden LV with a known structure. What remains unknown and needs to be determined is only the value of this LV. This simplifies the hidden LV problem to a special type of missing data problem where all values of the LV are missing. Imputation methods, such as the expectation maximization algorithm, can be used to impute the missing values. Similarly, Binder et al. (1997) assume that the complete network structure that includes the location of the LVs is known, and the goal is to learn the BN parameters in the presence of LVs. However, when a certain structure is involved, the difficulty arises from having an unlimited number of hidden LVs and an unlimited number of network structures to contain them (Cooper 1995). Determining network structures is thus NP-hard<sup>11</sup> and heuristic methods may be necessary. For instance, Elidan et al. (2000) propose a “natural” approach by identifying the “structure signature” of hidden LVs, which uses a heuristic to identify “semicliques” when each of the variables connects to at least half of the others. If such a semiclique is detected, a hidden variable is introduced as the parent node to replace the semiclique. Silva et al. (2006) questioned this ad-hoc approach and proposed a method for determining the location of LVs based on a TETRAD difference that, loosely speaking, captures the intercorrelations among four variables (Spirtes et al. 2000, p. 264). However, the approach of Silva et al. (2006) only focuses on linear continuous LVs for which the correlation-based TETRAD difference is applicable.

In sum, though the BN literature has made some progress in developing methods for detecting “hidden” LVs from data, to the best of our knowledge constructing a BN with LVs from measurement items has still not been achieved. The proposed LVI algorithm is thus developed (§3.2) to fill in this gap. It uses the axiom of conditional independence as the building block that provides a causal interpretation to the measurement model (§3.2.1); the value of an LV is determined by nonlinear programming that maximizes conditional independence (§3.2.2). The actual algorithm is presented in §3.2.3, which takes the raw measurement items as inputs and outputs the identified LVs.

Second, after the LVs are identified, how can we discover the most probable causal structure among the LVs? Two generic issues need to be addressed: (1) How can we determine that one causal structure is better than the other? (2) How can we search for the best structure among all possible graphs, a problem known to be NP-hard? We first adopt the popular PC algorithm (named after Peter and Clark in Spirtes et al. 2000) to generate a good initial Bayesian network to reduce the number of searchers needed (§3.3.1). We then refine this initial graph using a scoring approach (§3.3.2) to compare potential candidate structures. The two state-of-the-art scoring functions in the BN literature are the Bayesian-Dirichlet metric (Cooper and Herskovits 1992, Heckerman et al. 1996) and the Gaussian metric (Glymour et al. 1987). However, neither scoring function is applicable to the Likert-type data commonly used in IS, which render discrete and ordinal data. Specifically, the Bayesian-Dirichlet metric assumes a multinomial distribution, with parameters distributed as Dirchlet. Its multinomial assumption, which is applicable to general discrete data, ignores the ordinal nature of Likert-type data. The Gaussian metric treats data as continuous with a Gaussian distribution, ignoring the discrete nature of Likert-type data.

To fill in this gap, we develop a new scoring function, the proposed OL metric (§3.3.2.1). However, the OL metric only computes the overall fitness of a candidate structure and it does not infer if a given structure is significantly better than the other. In view of this, we develop a Chi-square test (§3.3.2.2). Integrating the OL metric and the Chi-square test, we can then determine if a certain structure is significantly better than the other. Finally, to intelligently search for the best causal structure, we adopt the greedy equivalence search (GES) searching strategy (which is proven to be optimal by Chickering 2002) for BN construction (§3.3.2.3).

Overall, the proposed BN-LV method can both identify the measurement model and also test the structural model. The BN-LV method operates in two major stages: (1) it first identifies the “hidden” LVs given a set of measurement items (described in §3.2), and (2) it generates an equivalent class of graphs among the LV, scores each candidate graph using the OL scoring function, and searches for the structure with the highest fitness score (described in §3.3).

## 3.2. Stage 1. Identifying Latent Variables from Measurement Items

The theory of measurement assumes that the LVs “cause” the direct measurement items (or indicators).<sup>12</sup> In theory, given an LV, the measurement items are independent from each other (Kline 1998). This is formally referred to as the axiom or assumption of conditional (or local) independence. Conditional independence is the basis of the theory of measurement and “the defining attribute of any latent structure analysis” (Heinen 1996, p. 4). However, existing SEM or BN models do not directly test this axiom. SEM methods mainly use correlation- or covariance-based factor analysis methods to categorize measurement items under LVs to test the measurement model.<sup>13</sup> Herein, we propose a new algorithm that takes the raw measurement items as the only inputs and thus outputs the most likely LVs. This is accomplished by identifying the most likely measurement model for these measurement items by directly testing the axiom of conditional independence.

3.2.1. Testing the Axiom of Conditional Independence. The conditional independence axiom (Heinen 1996, p. 4; Spirtes et al. 2000, p. 253; Bollen 1989) asserts that $R _ { x _ { i } x _ { j } \mid y } .$ —the conditional correlation between any two measurement items $x _ { i }$ and $x _ { j }$ given the latent variable y—should approach zero for any pair of $x _ { i }$ and $x _ { j }$ where $i , j \in ( 1 , \ldots , m )$ and $i \neq j . \ R _ { x _ { i } x _ { j } | y } \mathbf { i } s$ computed as follows:

$$
R _ {x _ {i} x _ {j} | y} = \frac {R _ {x _ {i} x _ {j}} - R _ {x _ {i} y} R _ {x _ {j} y}}{\sqrt {(1 - R _ {x _ {i} y} ^ {2}) (1 - R _ {x _ {j} y} ^ {2})}}.\tag{3}
$$

<sup>12</sup> This property of “reflective” LV is shown in SEM models as an arrow starting from the LV and pointing to the measurement items. <sup>13</sup> Only one approach (Sarkar and Sriram 2001) uses conditional independence to discover composite attributes, which can be viewed as a group of attributes caused by LVs. However, it assumes that the dependent variable (in the case of Sarkar and Sriram 2001, bank failure) of the BN is known, and that given the dependent variable, the composite attributes are independent. This is a strict condition that SEM studies do not meet.

We choose the common t-test

$$
t = \frac {r}{\sqrt {(1 - r ^ {2}) / (n - 2)}}
$$

for correlation coefficient r of a sample size n to determine if $R _ { x _ { i } x _ { j } | y }$ is significantly different from zero. If $t > 1 . 9 6$ when n is sufficiently large, we assume that the correlation is nonzero $( p < 0 . 0 5 ) . ^ { 1 4 }$ This test is called into question for LVs with only two measurement items (say, $x _ { 1 }$ and x<sub>2</sub>. For example, $R _ { x _ { 1 } x _ { 2 } | y }$ is always one when $y$ is a linear combination of $x _ { 1 }$ and $x _ { 2 } ,$ similar to computing the factor scores in a principal components factor analysis. This implies that this test cannot empirically verify the axiom with only two items per LV. Torgerson (1958) observed the same phenomenon that he referred to as “measurement by Fiat,” because it often leads to rejection of the measurement model. It is no accident that many researchers (e.g., Kline 1998) recommend using more than two measurement items per LV in SEM studies whereas LISREL recommends at least four measurement items per LV for the measurement model to converge.

3.2.2. Determining the Latent Scores. A remaining caveat above is that the axiom of conditional independence cannot be empirically tested because the LV (i.e., y in Equation (3)), at least in principle, is not directly measurable and, thus, it cannot be empirically fixed. To test the conditional independence of a measurement model, an estimate of the value of the LV, referred to as latent scoring, must first be assessed. A common latent scoring method is raw sumscore, which uses the simple sum of the measurement items. A variant of the raw sumscore method is the weighted average. For example, a usual method for estimating the values of LVs is principal components factor analysis where the factor loadings are used as weights for computing the latent scores. However, the use of the raw sumscore or a weighted average lacks theoretical justification (Skrondal and Rable-Hesketh 2004).

We propose an optimal weighting method to compute the latent scores to directly maximize conditional independence. Without loss of generality, suppose an LV y has m indicators $x _ { 1 } , x _ { 2 } , \ldots , x _ { m }$ . Let $\alpha _ { 1 } , \ \alpha _ { 2 } ,$ $\begin{array} { r } { \alpha _ { m } ( \sum _ { i = 1 } ^ { m } \alpha _ { i } = 1 ) } \end{array}$ be the corresponding weights. We then have $\begin{array} { r } { y = \sum _ { i = 1 } ^ { m } \alpha _ { i } x _ { i } . } \end{array}$ , using the weighted average approach.<sup>15</sup>

We formulate the problem of assigning latent scores as an optimization problem of finding the optimal weight vector $\alpha ^ { * } = ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { m } )$ , such that the maximum of all the $m \times ( m - 1 ) / 2$ pairs of conditional correlation $R _ { x _ { i } x _ { j } | y }$ in absolute value is minimized.<sup>16</sup> Formally, the optimization problem is formulated below:

$$
\begin{array}{l} \alpha^ {*} = \underset {\alpha_ {1}, \ldots , \alpha_ {m}} {\arg \min} \left(\underset {1 \leq i, j \leq m, i \neq j} {\max} \left| R _ {x _ {i} x _ {j} | y} \right|\right) \\ \text {s.t.} 0 \leq \alpha_ {i} \leq 1, i \in (1, \ldots , n) \\ \sum_ {i = 1} ^ {m} \alpha_ {i} = 1 \\ y = \sum_ {i = 1} ^ {m} \alpha_ {i} x _ {i}. \end{array}\tag{4}
$$

Once the optimal weight $\alpha ^ { * }$ is determined (given $0 \leq \alpha _ { i } \leq 1 ) , ^ { 1 7 }$ the latent score of $y$ is fixed. The proposed minmax approach ensures that the conditional independence axiom is met even in the worst case scenario (i.e., the max of $R _ { x _ { i } x _ { j } | y } )$ . However, if no such $\alpha ^ { * }$ is found to satisfy the axiom of conditional independence, then the research design or the measurement items may be highly problematic.

3.2.3. The Proposed Latent Variable Identification (LVI) Algorithm. The LVI algorithm seeks to discover the smallest possible set of LVs (to ensure a parsimonious model with as few LVs) for the measurement items to be partitioned into disjoint sets while assuring that the axiom of conditional independence is satisfied within each disjoint set. The notation used in the LVI algorithm is described in Table 1. LVI has two steps (Table 2).

Table 1 Notation for the LVI Algorithm

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $X$ </td><td>A set of  $m$  measurement items,  $X = (X_1, X_2, \ldots, X_m)$ </td></tr><tr><td> $x_i$ </td><td>A measurement item of  $X$ </td></tr><tr><td> $k$ -item set</td><td>An item set having  $k$ -measurement items</td></tr><tr><td> $L_k$ </td><td>Set of valid  $k$ -item sets that satisfy the axiom of local independence</td></tr><tr><td> $G_k$ </td><td>Set of candidate  $k$ -item sets (with  $k$  items that may not satisfy the axiom of conditional independence)</td></tr><tr><td>C-1</td><td>The necessary condition that two measurement items of the same LV should be moderately correlated</td></tr><tr><td>C-2</td><td>The axiom of conditional independence is detailed in §4.1</td></tr></table>

The flowchart of the LVI algorithm is shown in Figure 2 and its algorithmic steps are outlined in Appendix A. The inputs to the LVI algorithm are the measurement items and the outputs are the disjoint item sets, each of which represents an LV. Each $L _ { 1 }$ contains a measurement item. $L _ { 2 }$ is generated using only the necessary condition C-1. This is because the axiom of conditional independence of $L _ { 2 }$ is not directly testable (§3.2.2). Therefore, the LVI algorithm works best for LVs that are measured with more than two measurement items, as is strongly recommended by SEM researchers (e.g., Kline 1998, Bollen 1989). Then, LVI generates $L _ { k + 1 }$ from $L _ { k }$ by examining candidate item sets based on C-1 and C-2 (see also Table 1).

Step 2 prunes all valid item sets by eliminating all subsets and overlapping measurement items. To ensure the smallest number of LVs, the LVI algorithm begins from the largest item set (the one with the most measurement items) among all $L _ { k } .$ It then eliminates the overlapping items from the item set that is affected the least, after removing any overlapping items. Finally, the LVI algorithm outputs the disjoint item sets, each of which represents an underlying LV, and the value of each LV is computed according to formulation (4).<sup>18</sup>

## 3.3. Stage 2. Constructing a Causal Bayesian Network for Structural Models

After the LVs are identified and their values are computed, the next step is to build a BN to test the causal relationships among the LVs. This corresponds to the structural model testing part of SEM. The common approach to learning a BN from data is by specifying a scoring function (typically variations of the likelihood function) of each candidate network structure and then selecting the BN with the highest score (Friedman et al. 2000). Because examining the possible network structure is NP-hard, the search algorithms (for the optimal structure) in the BN literature are almost exclusively variations of greedy algorithms. To reduce the number of searches, Spirtes et al. (2002) proposed the generic PC algorithm to generate an initial starting point and then used a greedy search algorithm based on the scoring function to reduce search complexity. We follow this common practice and discover the most likely BN in two steps: (1) generate an initial class of equivalent BN using PC2 (our proposed variation of the PC algorithm), and (2) select the most likely causal BN using a new scoring function designed specifically for ordinal and discrete (Likerttype) data that are commonly found in IS research.

3.3.1. Generating Equivalent Classes of Bayesian Networks from Data. Given a set of data, is it possible to create a unique causal Bayesian network? The consensus is that one cannot distinguish between BN that specify the same conditional independence from data alone. It is possible that two or more BN structures represent the exact same constraints of conditional independence (every joint probability distribution generated by one BN structure can also be generated by the other). In this case, the BN structures are said to be likelihood equivalent.

When learning an equivalent class of structures from data, we can conclude that the true BN is possibly any one of the networks in this class (Friedman et al. 2000). An equivalence class of network structures can be uniquely represented by a partially directed graph, where a directed edge $X  Y$ suggests that all members of the equivalence class contain the arc $X  Y$ . Otherwise, an undirected X–Y edge denotes that some members of the class contain arc X <sub>→</sub> Y while others contain arc $Y  X$ . Learning the causal relationships among LVs can be regarded as the process of “directing” a graph.

The BN literature (e.g., Glymour et al. 1987, Heckerman et al. 1995) has developed methods to generate equivalent structures that have the same

## Table 2 Detailed Steps of the LVI Algorithm

Step 1: Identify all sets of measurement items (item sets) that satisfy the axiom of conditional independence

LVI uses a maximum spanning approach. It starts with a randomly selected measurement item and it incrementally adds items to the item set. It stops when no item can be added to the item set without violating the axiom. Denote $L _ { k }$ the item set with k measurement items that meet the conditional independence axiom. The core step of the algorithm is to span from $L _ { k } \mathrm { ~ t 0 ~ } L _ { k + 1 }$ the item set containing k 1 measurement items that still meet the axiom. This is done by adding an item not already in $L _ { k }$ into $L _ { k } ,$ , and then testing the axiom for the new item set with these $k + 1$ items using the method in §3.2.1. This step can incur high computational cost because it involves the optimization procedure to determine the latent score. We impose one condition to limit the possible combinations of $L _ { k + 1 }$ to reduce the computation cost: The correlation between any two items in $L _ { k + 1 } ,$ say, $\boldsymbol { \chi } _ { j }$ and $x _ { j } ,$ should be at least moderate (Kline 1998, p. 190). The user may specify a threshold to determine “moderate” correlation. We use a low correlation of $r = 0 . 5$ as the generic threshold. Then, we eliminate the candidate item sets with $k + 1$ items that do not meet the conditions in the first place.

Step 2: Prune the generated item sets from Stage 1 into disjoint (discriminant) sets

LVI first identifies the supersets of item sets and then deletes all subsets. For example, suppose two item sets $A = \{ x 1 , x 2 , x 3 \}$ and $B = \{ x 1 , x 2 , x 3 , x 4 \}$ are generated by Step 1. Clearly B is a superset of A. In this case, we need to delete subset A to ensure convergent validity. We then deal with item sets that have overlapping items. For example, suppose two item sets $A = \{ x 1 , x 2 , x 3 \}$ and $B = \{ x 1 , x 4 , x 5 , x 6 \}$ have an overlapping item x1 (i.e., x1 loads on both A and B). SEM methods would consider x1 a problematic item because it violates discriminant validity. Skrondal and Rable-Hesketh (2004, p. 8) suggest either accepting that an item may belong to two or more LVs or discarding the problematic item (Goldstein 1994). Our algorithm detects such problematic items and, by default, we assume the user decides to keep the items. The LVI algorithm then determines the LV that the item is more likely to belong to This is done by testing the impact of deleting the measurement item from the two LVs on the value max $( R _ { x _ { i } x _ { j } | y } )$ among the residual measurement items The measurement item is then assigned to the LV that is affected the most.

underlying undirected graph. As reviewed earlier, theories of causal BN are based on the d-separation and the causal Markov assumptions. Pearl and Verma (1991) established theorems to operationalize the construction of BN using d-separation. Let $R _ { x , y | z }$ be the partial correlation of variable X and Y given $Z ,$ from a triplet of variables X Y Z, where Z is any set of variables besides X and Y . If X and Y are not d-separated given any $Z ( R _ { x , y | z } \neq 0 )$ , then there is an edge between X and Y . We thus need to test the condition $R _ { x , y \mid z } \neq 0$ for all possible combinations of $Z .$ This is again NP-hard (Spirtes et al. 1998). Spirtes et al. (2002) proposed the PC algorithm that tests the d-separation condition for any possible combinations of $X , Y ,$ and Z to determine if there is a link between X and Y . Though the PC algorithm is found to not be as accurate as the scoring approach in general (Silva et al. 2006, p. 211), it is more efficient and it can thus generate BN structures that serve as good starting points for other scoring-based algorithms.

Figure 2 Flowchart of the Steps of the LVI Algorithm  
![](/api/attachments/XZ82P2CR/fulltext/images/e38dd9de5906592f9f92f6efdb80dfa0e29b7a1e31fc853fa5f4f5f0a27e72e1.jpg)

Our approach also uses the PC algorithm to discover an initial causal structure as the input to the scoring-based algorithm in §3.3.2. We slightly modified the PC algorithm to make it consistent with SEM techniques and we termed our version of the algorithm PC2 (Appendix B). Algorithm PC2 refines the PC algorithm in two dimensions: (1) the PC algorithm uses Fisher’s Z test, which requires all variables to be normally distributed, but the PC2 algorithm relaxes this assumption by using the aforementioned t-test for correlation coefficients to determine the significance of $R _ { x , y | z }$ (Equation (2)); (2) the PC2 algorithm incorporates Verma and Pearl’s (1992) five rules for directing graphs.

The output of the proposed PC2 algorithm is a partially causal BN $B _ { s }$ because some edges may remain undirected. This is a direct result of the limited capacity of Verma and Pearl’s (1992) five rules for directing links. Our empirical studies suggest that these five rules are too specific. For example, Rule 3 states that if $X  Y , \ Y  Z ,$ and $X { - } Z ,$ then direct the link between X and Z as $X \to Z$ . This rule only covers a few cases we might encounter in BN construction. The PC2 algorithm is thus ineffective in orienting those links that are not covered by these five rules. However, we found PC2 to be adequate in identifying nonedges (i.e., nodes that should not be connected), and it is a fine starting point for causal BN discovery.

3.3.2. Refining Bayesian Network Using the Ordered Logit Scoring Function. The problem of learning a Bayesian network can also be perceived as a process of finding a class of $B _ { s }$ that best matches data D. To compare two $\mathsf { B N s } { \ - } { \ - } B _ { S 1 }$ and $B _ { S 2 } .$ —we need to test the ratio $P ( B _ { s 1 } \mid D ) / P ( B _ { s 2 } \mid D )$ given data D. By computing such ratios for pairs of BN structures, we can rank order a set of competing structures. Following Bayes’ rules, we have

$$
\frac {P (B _ {s 1} \mid D)}{P (B _ {s 2} \mid D)} = \frac {[ P (B _ {s 1} , D) / P (D) ]}{[ P (B _ {s 2} , D) / P (D) ]} = \frac {P (B _ {s 1} , D)}{P (B _ {s 2} , D)}.
$$

Therefore, it is possible to score the likelihood of a Bayesian network $B _ { s }$ given $D$ by computing the joint probability $P ( B _ { s } , D )$

3.3.2.1. The Ordered Logit (OL) Scoring Function. As pointed out in §3.1, none of the existing scoring functions is intended specifically for SEM data, especially for Likert-type data that are commonly used in IS research. We develop a new scoring function termed ordered logit (OL) specifically for ordinal and discrete data (Likert-type data). For a particular node x given a set of q parents $\pi ,$ its conditional probability can be estimated by the following OL function:

$$
P (x / \pi , \theta) = \mathrm{OL} \left(\alpha + \sum_ {i = 1} ^ {q} \beta_ {i} \pi_ {i}\right),\tag{5}
$$

where ) represents the set of parameters of the intercept and coefficient $\beta _ { i }$ by running an ordered logistic regression (Borooah 2002) with x as the dependent variable and the $q$ parents as the independent variables. The proposed OL function is derived in Appendix C. The joint probability of a $B _ { s }$ and data D is computed as follows.

Suppose there are n records. Let $X ( x _ { 1 } \cdots x _ { m } )$ be a set of m discrete variables. Each variable $x _ { i }$ has $r _ { i }$ possible values and a set of parents $\pi _ { i }$ . Let $\pi _ { i j k }$ denote the kth parent for record j of variable $x _ { i }$ . Suppose there are $q _ { i }$ such parents. Then,

$$
P (B _ {s}, D) = P (B _ {s}) \prod_ {j = 1} ^ {n} \prod_ {i = 1} ^ {m} \mathrm{OL} \left(\alpha_ {i j} + \sum_ {k = 1} ^ {q _ {i}} \beta_ {i j k} \pi_ {i j k}\right).\tag{6}
$$

Once $P ( B _ { s } )$ and the data D are known, we have full knowledge about the domain for the purpose of learning network structures. Cooper and Herskovits (1992) assume that $P ( B _ { s } )$ is constant, that is, all network structures are equally likely without further knowledge. This is a necessary assumption if we do not allow the users to specify their own priors about the network structure. Therefore, we can omit the component $P ( B _ { s } )$ when computing Equation (6).

3.3.2.2. Goodness-of-Fit Test Based on Ordered Logit. A goodness-of-fit test is needed to compare competing structures. SEM techniques have various tests for the overall fitness of a structural model (Gefen et al. 2000).<sup>19</sup> Here, we develop a $\chi ^ { 2 }$ test based on the OL scoring function. Similar to SEM, we assume that the null model is the measurement model that has no paths among its LVs. Let $X ( x _ { 1 } \cdots x _ { m } )$ be a set of m latent variables. In the null model, $P ( B _ { s } , D ) =$ $p ( x _ { 1 } ) \times p ( x _ { 2 } ) \cdot \cdot \cdot \times p ( x _ { m } )$ . Assume each variable $x _ { i }$ has $r _ { i }$ possible values $x _ { i } ^ { 1 } \cdots x _ { i } ^ { r _ { i } }$ . Suppose there are n records. Define $n _ { i j }$ to be the number of cases in the data D in which variable $x _ { i }$ has the value $x _ { i } ^ { j } .$ . Then, $p ( x _ { i } ) =$ $\textstyle \prod _ { j = 1 } ^ { r _ { i } } ( n _ { i j } / n )$ and the overall likelihood for the null model is:

$$
L _ {0} = p (B _ {s}, D _ {i}) = \prod_ {i = 1} ^ {m} \prod_ {j = 1} ^ {r _ {i}} \frac {n _ {i j}}{n}.\tag{7}
$$

For a particular BN, we know from Equation (6) that $\begin{array} { r } { L _ { 1 } = \prod _ { i = 1 } ^ { m } \prod _ { j = 1 } ^ { n } \mathrm { O L } ( \alpha _ { i j } + \sum _ { k = 1 } ^ { q _ { i } } \beta _ { i j k } \pi _ { i j k } ) } \end{array}$

Given the two likelihoods, an appropriate goodnessof-fit test is the $\chi ^ { 2 }$ test $- 2 \ln ( L _ { 1 } - L _ { 0 } )$ , with degree of freedom as n minus the total number of local parameters estimated. We know there are $\textstyle \sum _ { i = 1 } ^ { n } { \bigl ( } r _ { i } - 1 { \bigr ) }$ intercepts (  and $\textstyle \sum _ { i = 1 } ^ { n } q _ { i }$ coefficients (\*) to be estimated, where $r _ { i }$ is the possible number of values of $x _ { i }$ and $q _ { i }$ is the total number of parents of $x _ { i }$ .

Therefore, the degrees of freedom are given by:

$$
d f = n - \sum_ {i = 1} ^ {m} (r _ {i} - 1) - \sum_ {i = 1} ^ {m} q _ {i}.\tag{8}
$$

Using the $\chi ^ { 2 }$ test, we can determine if a particular graph structure is significantly better than any competing graphs (see Footnote 18).

3.3.2.3. Searching for the Best Structure. After running the PC2 algorithm, we already have an initial graph $B _ { s }$ . Our only task is to then refine the initial BN graph and orient the undirected edges (e.g., X–Y ) in $B _ { s }$ . According to Pearl and Verma (1991), two graphs G and $G ^ { \prime }$ are structurally different and distinguishable if and only if they have a different underlying undirected graph and at least one different V -structure (i.e., converging directed edges into the same node, such as $X \right. Z \left. Y )$ . From this theorem, if G and $G ^ { \prime }$ have the same undirected structure, the only edges that must be directed are those that participate in V -structures (also referred to as colliders by Spirtes et al. 2000). Suppose we need to select between two competing structures $B _ { s 1 } ( X \to Y )$ with $B _ { s 2 } \ ( Y  X )$ to orient the direction for X–Y . We first need to investigate if the direction reversal yields different V -structures. If it does, we must check if the likelihoods of the two structures are significantly different according to the Chi-square test, and we choose the one with the highest fitness score.

However, a local change in one part of the network can affect the evaluation of a change in another part of the network, making the search for the optimal structure NP-hard (Chickering 2002). Chickering (2002) developed a greedy equivalence search (GES) algorithm that is asymptotically optimal, and it is now considered as the best causal model search algorithm to date (Silva et al. 2006). This searching strategy is herein adopted. The main objective of GES is to reduce the search space. GES has two phases: First, it greedily (according to a scoring criterion such as the OL function) adds dependencies by considering all possible single-edge additions. Once the greedy algorithm stops at a local maximum, a second-phase greedy algorithm considers all possible single-edge deletions. The algorithm terminates after no significant improvement can be further achieved in the second phase and the final graph is outputted. This represents the method’s final output.

## 4. Evaluating the Bayesian Networks for Latent Variables (BN-LV) Method

The BN-LV method (Figure 3) integrates both the measurement model (via the LVI algorithm) and the structural model (via the OL scoring function). BN-LV takes the raw measurement items as inputs (Step 1, Figure 3) and it identifies the LVs that govern these items using the LVI algorithm (Step 2, Figure 3). The value of the LVs is simultaneously computed by LVI through formulation (4) (Step 3, Figure 3). Then, an initial graph is generated using the PC2 algorithm on the identified LVs (Steps 4 and 5, Figure 3). The graph is refined based on the OL scoring function (Step $6 ,$ Figure 3), and it then outputs the most likely causal BN graph (Step 7, Figure 3).

The computational complexity of BN-LV is tested in Appendix D. Section 4.1 offers an illustrative example to describe the step-by-step process of the BN-LV method using actual empirical data. Because of data complexity<sup>20</sup> and space constraints, we can only provide details at a summary level for Stage 2 of the algorithm (Steps 4–7, Figure 3). Still, for a smaller artificial data set, we show the detailed calculations behind Stage 2 of the BN-LV method as a tutorial (see Footnote 18).

Figure 3 Flowchart of the Steps of the BN-LV Algorithm  
![](/api/attachments/XZ82P2CR/fulltext/images/4f956558ec27e1f541b16029fa68a7c868cc140b810d557788cda153fc5c22aa.jpg)

Table 3 The Correlation Matrix for the Raw Measurement Items

<table><tr><td></td><td>SAT1</td><td>SAT2</td><td>Trust1</td><td>Trust2</td><td>Trust3</td><td>EOU1</td><td>EOU2</td><td>EOU3</td><td>USEF1</td><td>USEF2</td><td>USEF3</td><td>INT1</td><td>INT2</td></tr><tr><td>SAT1</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SAT2</td><td>0.867</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Trust1</td><td>0.725</td><td>0.694</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Trust2</td><td>0.695</td><td>0.615</td><td>0.819</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Trust3</td><td>0.722</td><td>0.676</td><td>0.912</td><td>0.869</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EOU1</td><td>0.583</td><td>0.532</td><td>0.603</td><td>0.658</td><td>0.622</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EOU2</td><td>0.455</td><td>0.377</td><td>0.476</td><td>0.551</td><td>0.510</td><td>0.720</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EOU3</td><td>0.558</td><td>0.477</td><td>0.569</td><td>0.616</td><td>0.561</td><td>0.865</td><td>0.864</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>USEF1</td><td>0.613</td><td>0.550</td><td>0.604</td><td>0.636</td><td>0.675</td><td>0.667</td><td>0.718</td><td>0.730</td><td>1.0</td><td></td><td></td><td></td><td></td></tr><tr><td>USEF2</td><td>0.527</td><td>0.425</td><td>0.464</td><td>0.476</td><td>0.512</td><td>0.541</td><td>0.577</td><td>0.620</td><td>0.695</td><td>1.0</td><td></td><td></td><td></td></tr><tr><td>USEF3</td><td>0.545</td><td>0.520</td><td>0.665</td><td>0.646</td><td>0.649</td><td>0.585</td><td>0.472</td><td>0.564</td><td>0.602</td><td>0.582</td><td>1.0</td><td></td><td></td></tr><tr><td>INT1</td><td>0.310</td><td>0.319</td><td>0.431</td><td>0.373</td><td>0.413</td><td>0.393</td><td>0.312</td><td>0.296</td><td>0.392</td><td>0.387</td><td>0.497</td><td>1.0</td><td></td></tr><tr><td>INT2</td><td>0.336</td><td>0.355</td><td>0.447</td><td>0.397</td><td>0.385</td><td>0.381</td><td>0.285</td><td>0.306</td><td>0.393</td><td>0.361</td><td>0.530</td><td>0.773</td><td>1.0</td></tr></table>

## 4.1. Illustrating the BN-LV Method Using Empirical Data to Test Competing Causal Models

We describe BN-LV by illustrating how it can help reconcile competing structural models using actual empirical data. The step-by-step illustration demonstrates how BN-LV can test competing hypotheses in terms of the direction of causality between trust and ease of use when integrating the classic TAM model with the construct of trust (Figure 5).<sup>21</sup> Specifically, Pavlou (2003) argued and showed trust to influence ease of use while Gefen et al. (2003) argued and showed the opposite direction of causality. To make the comparison meaningful, we selected five constructs that are common across the two structural models—intentions (INT), usefulness (USEF), ease of use (EOU), trust (Trust), and satisfaction (SAT).<sup>22</sup>

4.1.1. Identifying Latent Variables from Measurement Items. In Stage 1 (the first three steps in Figure 3), BN-LV identifies the LVs from the measurement items. The raw data are the 13 measurement items associated with the 5 LVs (Pavlou 2003). Each item is measured on a seven-point Likert-type scale. The correlation matrix of the 13 measurement items is shown in Table 3 with a significance level at 0.162 (p < 005 level, n 151).

Following the flowchart of LVI (Figure 2), $L _ { 1 }$ is first initiated and consists of 13 item sets {S1}, {S2}, {T1}    and so on (abbreviation of each item is used). $L _ { 2 }$ is then generated based on the weak constraint that the pairwise correlation should be moderate $( \mathrm { i } . \mathrm { e } . , > 0 . 5 0 )$ , following condition C-1. This is done by checking with the correlation matrix (Table 3). Fiftythree such item sets meet the condition, including {S1, S2}, {S1, T1}    and so on. $L _ { 3 }$ needs to satisfy both conditions (C-1 and C-2) for any three-item combination. This yields five item sets in Table 4 together with the weight vector and the MinMax(R)—the objective function in formulation (4). LVI then determines that there is no $L _ { 4 }$ that meets C-2 (the best candidate is {T1, T2, T3, U1} with MinMax(R) <sub>=</sub> 0.194). In sum, LVI completes generating item sets, resulting in 5 item sets in $L _ { 3 }$ and 53 item sets in $L _ { 2 } .$

Table 4 The Weight Vector and MinMaxR Values

<table><tr><td>L3</td><td>Weights</td><td>MinMax(R)</td></tr><tr><td>{T1, T2, T3}</td><td>(0.15, 0.12, 0.73)</td><td>0.133</td></tr><tr><td>{E1, E2, E3}</td><td>(0.09, 0.16, 0.75)</td><td>0.106</td></tr><tr><td>{U1, U2, U3}</td><td>(0.84, 0.07, 0.09)</td><td>0.112</td></tr><tr><td>{T2, T3, U1}</td><td>(0.04, 0.84, 0.12)</td><td>0.118</td></tr><tr><td>{E1, E3, U1}</td><td>(0.04, 0.87, 0.09)</td><td>0.103</td></tr></table>

Next, LVI prunes all those item sets as follows: First, it identifies the supersets of these 53 item sets in $L _ { 2 }$ and drops those subsets correspondingly (51 of them). Only two item sets in $L _ { 2 }$ remain: {S1, S2} and {I1, I2}. We then identify the overlapping items in $L _ { 3 } .$ . Notice that item U1 loads on three item sets (last three rows) (Table 4), which suggests that it is a potentially problematic item. LVI recommends keeping U1 with the set {U1, U2, U3} because it affects this item set the most (dropping it would lead to a weak $L _ { 2 }$ of {U2, U3} with a correlation of 0.582). The other two sets {T2, T3, U1} and {E1, E3, U1} are then dropped. Therefore, LVI eventually outputs the final disjoint item sets {S1, S2}, {I1, I2}, {T1, T2, T3}, {E1, E2, E3}, and {U1, U2, U3}. The corresponding latent scores are computed using the optimal weights in Table 4 for $L _ { 3 }$ and equal weight of 0.5 for $L _ { 2 }$

4.1.2. Constructing the Most Likely Graph Among the Identified LVs. Stage 2 in BN-LV (corresponding to Steps 4–7 in Figure 3) discovers the most likely graph among the five LVs. It first initiates a fully connected and undirected graph that connects any two LVs (Step 4, Figure 3). Step 5 in Figure 3 applies algorithm PC2 and generates the graph (left panel of Figure 4). Note that PC2 fails to identify any causal directions for these links. Step 6 of Figure 3 applies the proposed OL scoring function with the GES search strategy to identify the directionality of these links. The result shown (right panel of Figure 4) closely corresponds to Pavlou’s (2003) structural model for these five LVs.

4.1.3. Using BN-LV to Reconcile Competing Hypotheses on Causal Links. Gefen et al. (2003) proposed a different structural model in which the direction between EOU and Trust is EOU Trust while

Pavlou (2003) proposed that Trust  EOU. Both studies provide compelling theoretical justifications. In such cases, Carte and Russell’s (2003, p. 487) solution that seeks theoretical justification may be of little help. In contrast, BN-LV offers a “let data speak” approach to reconcile competing structural models. We examine the interrelationships among the five LVs—Trust, EOU, USEF, INT, SAT—for the two competing models (Figure 5).<sup>23</sup> The data support the case of Trust <sub>→</sub> EOU. The likelihoods are <sub>−</sub>908.8 for Pavlou (2003) and 952.3 for Gefen et al. (2003). The Trust EOU direction of causality thus improves the likelihood by 43.5. The degrees of freedom for the Chi-square test (Equation (8)) is 6 between the 2 graphs (Figure 5) and the critical value is 14.5 $( p < 0 . 0 { \bar { 5 } } ) . ^ { 2 \bar { 4 } }$ The improvement of Pavlou’s (2003) model over the model of Gefen et al (2003) is significant and distinguishable. Though we cannot obviously draw definite conclusions from one data set, this example illustrates how BN-LV can empirically reconcile between competing structural models in terms of the direction of causality in certain relationships.<sup>25</sup>

## 4.2. Simulation Experiments to Evaluate the BN-LV Method Relative to Competing Techniques

We further systematically evaluate the BN-LV method using a simulation experiment. The data generating process (DGP) is first described, followed by

Figure 4 Graphs Generated by the Proposed BN-LV Method

Graph after applying the PC2 algorithm (Step 5, Figure 3)

Graph after applying the OL scoring function (Step 7, Figure 3)

![](/api/attachments/XZ82P2CR/fulltext/images/99abaca6e62b103c74e9814105d70f74f207b853c800d2dc4f429af599eaa863.jpg)

the evaluation of the BN-LV method’s two core components—the LVI algorithm for identifying the LVs, and the OL scoring function for discovering the optimal graph structure (most likely causal BN).

4.2.1. The Data Generating Process (DGP) for the Simulation Experiments. The blueprint graph structure for our simulated data comes from Pavlou (2003, p. 90). The structural model (Figure 6) depicts the constructs that are hypothesized to affect consumer intentions to transact online. We only selected the study’s principal constructs—Trust, Risk, EOU, USEF, and INT—while the control variables were omitted for simplicity. In particular, Trust is deemed exogenous while EOU, USEF, Risk, and INT are deemed endogenous (Figure 6).

We simulated the data according to the above theoretical structure, following the DGP specified in Silva et al. (2006) and Spirtes et al. (2000, p. 114). The DGP was composed of three steps:

Step 1. The exogenous variables were first independently generated following a normal distribution.

Step 2. Values of the endogenous variables were then generated as a linear function of their parents with a normally distributed error term $\varepsilon _ { e }$

Step 3. Values of the indicators were generated directly from each of their corresponding latent variables, adjusted by a normally distributed noise term $\varepsilon _ { i } .$

First, we generated the exogenous construct Trust with a normal distribution N 4 3. We attempted to be consistent with Pavlou (2003) who used a 7-point Likert-type scale with mean 4. The variance was chosen to be 3, such that 95% of times the simulated values fall within the range 06 74. The endogenous LVs were simulated using the path coefficients (Figure 6). For instance, the only parent of EOU is Trust with a path coefficient 0.64. We thus generated the value of EOU from the linear equation EOU <sub>=</sub> $1 . 4 4 + 0 . 6 4 \times \mathrm { T r u s t } + \varepsilon _ { e } ,$ where the intercept 1.44 was chosen for the mean of EOU to be 4. The noise term $\varepsilon _ { e }$ follows $N ( 0 , \delta _ { e } ^ { 2 } )$ . Noise $\delta _ { e }$ was varied by three levels: low, medium, and high, which were instantiated as 0.3, 0.6, and 0.9, respectively. The same procedure was used for the other principal constructs in Figure 6.

We simulated four indicators per LV (LVI algorithm requires three indicators per LV while LISREL recommends four). Each indicator was simulated as the LV plus an error term $\varepsilon _ { i } .$ . Likewise, $\varepsilon _ { i }$ followed a normal distribution $N ( 0 , \delta _ { i } ^ { 2 } )$ while $\delta _ { i }$ has 3 levels: 0.3, 0.6, and 0.9. We then converted the indicator values into 7-point Likert scales—1 for the simulated value below 1.49, 2 for the value within the range 1.5–2.49, and so on. We argue that this is consistent with the subjects actual responses to survey questionnaire items, where each Likert anchor reflects a range of values.

Figure 5 Competing SEM Models for Integrating TAM with Trust  
![](/api/attachments/XZ82P2CR/fulltext/images/2d04edbb5f6e0d6d0247015d3669e42cadf07f817888770082c4781f39423786.jpg)

Figure 6 The Blueprint Graph Structure for the Simulated Data  
![](/api/attachments/XZ82P2CR/fulltext/images/7fd7b6787512fa055e8af8f713f0f76e990fb9cecdca820a330c1137c548d14b.jpg)  
Source. Adapted from Pavlou 2003.

4.2.2. Manipulation of Experimental Dimensions. In this experiment, we simulated the data across four dimensions: sample size, noise, normality, and linearity.

Sample Size. We simulated three sample sizes—50, 250, and 1,000—to represent small, medium, and large sample sizes, respectively. In SEM, as a rule of thumb, sample sizes below 100 are considered small, between 200–300 are considered moderate, and >500 are considered large (Gefen et al. 2000). LISREL is sensitive to small sample sizes while PLS can handle small sample sizes with bootstrapping (Chin 1998).

Noise. Because noise affects data quality and the structural models built with noisy data, we varied the noise levels of both $\delta _ { e }$ and $\delta _ { i }$ from low (0.3), medium (0.6), to high (0.9).

Normality. SEM assumes data normality (Gefen et al. 2000). To examine how violation of this assumption affects model performance, we simulated the exogenous construct Trust from a uniform distribution between 0.5 and 7.5. Note that a nonnormal Trust also renders the other constructs nonnormal because the other constructs are endogenous.

Linearity. SEM assumes linear relationships among LVs while the BN literature does not make this restrictive assumption. We simulated the endogenous variables to follow an exponential function of their parents plus a normal error term. We used a cumulative exponential distribution with parameter 0 set to be equal to the path coefficients. For example, EOU was $\mathrm { E O U } = 0 . 5 + 7 \times ( 1 - \exp ( - 0 . 6 4 \times \mathrm { T r u s t } ) ) + \varepsilon _ { e }$ with the scale parameters (0.5 and 7) chosen to ensure a mean of 4.

These 4 dimensions yielded a total of 15 combinations. There were five scenarios: three noise levels for the normal and linear data, one level of nonnormality, and one level of nonlinearity. Each scenario had 3 sizes: 50, 250, and 1,000. Because it is customary to use multiple runs to average out the randomness that arises from the normally distributed error terms, we used 5 runs for each of the 15 combinations, resulting in a total of 75 data sets. The total number of data sets was limited by the manual data analysis procedures in LISREL and PLS. Therefore, we only examined one level of noise (medium noise) for the nonnormality and nonlinearity cases and we used only five runs for each combination.

4.2.3. Measurement Model Comparison. We compared the LVI algorithm with the two commonly used methods for measurement model testing: EFA and CFA. For EFA, we used the principal components factor analysis (Proc Factor in SAS 9.1) using the Eigenvalue >1 criterion. For CFA, we used the CFA procedure in PLS Graph 3.0. Note that this comparison is more generous to the CFA method because it takes more inputs (the number of factors) than the exploratory LVI and EFA.

We ran each method on the 75 simulated data sets. Each data set consisted of 20 indicators (4 measurement items for each of the 5 constructs). Dayton and Macready (1988) proposed using omission and intrusion error rates to evaluate the results of measurement model testing (factor analysis). The omission error rate is the percentage of manifest items that are not included in any LV. Intrusion is the error rate that manifest items that are misassociated with certain LVs. Spirtes et al. (2000) and Silva et al. (2006) use similar metrics, termed omission rate and commission rate, respectively (the percentage of LVs not specified in the true measurement model). These metrics result in four evaluation criteria:

1. Latent Omission LO. The error rate associated with omitted LVs. It is computed as the number of true LVs that are not identified by the method under investigation, divided by the total number of true LVs (five in our simulated study).

2. Latent Commission LC. The error rate associated with misidentified LVs. It is computed as the number of LVs that are identified by the method (however, not the true LVs), divided by the total number of true LVs.

3. Indicator Omission IO. The error rate associated with missing indicators (items). It is computed as the number of items that are in the true measurement model but do not appear in the measurement model generated by the method under investigation, divided by the total number of items in the true measurement model (20 in our simulated study).

Table 5 Measurement Model Comparison Results

<table><tr><td colspan="4">Simulated dimensions</td><td colspan="4">LVI</td><td colspan="4">EFA (SAS Proc Factor)</td><td colspan="2">CFA (PLS)</td></tr><tr><td>Size</td><td>Noise</td><td>Normality</td><td>Linearity</td><td>LO</td><td>LC</td><td>IO</td><td>IC</td><td>LO</td><td>LC</td><td>IO</td><td>IC</td><td>LC</td><td>IC</td></tr><tr><td>1,000</td><td>Low</td><td>Yes</td><td>Yes</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.6</td><td>0.4</td><td>0.6</td><td>0.4</td><td>0.68</td><td>0.59</td></tr><tr><td>1,000</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.36</td><td>0</td><td>0.36</td><td>0</td><td>0.6</td><td>0.4</td><td>0.6</td><td>0.4</td><td>0.36</td><td>0.4</td></tr><tr><td>1,000</td><td>High</td><td>Yes</td><td>Yes</td><td>0.64</td><td>0</td><td>0.64</td><td>0</td><td>0.36</td><td>0.16</td><td>0.36</td><td>0.16</td><td>0.2</td><td>0.2</td></tr><tr><td>1,000</td><td>Medium</td><td>No</td><td>Yes</td><td>0.48</td><td>0</td><td>0.48</td><td>0</td><td>0.6</td><td>0.28</td><td>0.6</td><td>0.28</td><td>0.68</td><td>0.54</td></tr><tr><td>1,000</td><td>Medium</td><td>Yes</td><td>No</td><td>0.4</td><td>0</td><td>0.4</td><td>0</td><td>0.28</td><td>0.04</td><td>0.28</td><td>0.05</td><td>0.28</td><td>0.14</td></tr><tr><td>250</td><td>Low</td><td>Yes</td><td>Yes</td><td>0</td><td>0.12</td><td>0</td><td>0.06</td><td>0.6</td><td>0.4</td><td>0.6</td><td>0.4</td><td>0.8</td><td>0.82</td></tr><tr><td>250</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.26</td><td>0.08</td><td>0.26</td><td>0.04</td><td>0.52</td><td>0.32</td><td>0.52</td><td>0.32</td><td>0.36</td><td>0.12</td></tr><tr><td>250</td><td>High</td><td>Yes</td><td>Yes</td><td>0.44</td><td>0</td><td>0.44</td><td>0</td><td>0.32</td><td>0.22</td><td>0.32</td><td>0.2</td><td>0.08</td><td>0.04</td></tr><tr><td>250</td><td>Medium</td><td>No</td><td>Yes</td><td>0.16</td><td>0.24</td><td>0.16</td><td>0.11</td><td>0.52</td><td>0.56</td><td>0.52</td><td>0.56</td><td>0.6</td><td>0.31</td></tr><tr><td>250</td><td>Medium</td><td>Yes</td><td>No</td><td>0.24</td><td>0.16</td><td>0.24</td><td>0.06</td><td>0.28</td><td>0.08</td><td>0.28</td><td>0.08</td><td>0.08</td><td>0.03</td></tr><tr><td>50</td><td>Low</td><td>Yes</td><td>Yes</td><td>0.12</td><td>0.28</td><td>0.12</td><td>0.22</td><td>0.56</td><td>0.24</td><td>0.56</td><td>0.28</td><td>0.76</td><td>0.85</td></tr><tr><td>50</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.12</td><td>0.12</td><td>0.12</td><td>0.06</td><td>0.36</td><td>0.24</td><td>0.36</td><td>0.2</td><td>0.44</td><td>0.21</td></tr><tr><td>50</td><td>High</td><td>Yes</td><td>Yes</td><td>0.16</td><td>0.28</td><td>0.16</td><td>0.18</td><td>0.28</td><td>0.2</td><td>0.28</td><td>0.17</td><td>0.32</td><td>0.18</td></tr><tr><td>50</td><td>Medium</td><td>No</td><td>Yes</td><td>0.08</td><td>0.34</td><td>0.08</td><td>0.13</td><td>0.48</td><td>0.2</td><td>0.48</td><td>0.17</td><td>0.88</td><td>0.38</td></tr><tr><td>50</td><td>Medium</td><td>Yes</td><td>No</td><td>0.24</td><td>0.04</td><td>0.24</td><td>0.02</td><td>0.32</td><td>0.2</td><td>0.32</td><td>0.14</td><td>0.36</td><td>0.13</td></tr><tr><td>Average</td><td></td><td></td><td></td><td>0.25</td><td>0.11</td><td>0.25</td><td>0.06</td><td>0.45</td><td>0.263</td><td>0.45</td><td>0.25</td><td>0.46</td><td>0.33</td></tr></table>

4. Indicator Commission IC. The error rate associated with misclustered indicators (items). It is computed as the total number of items generated by the method under investigation that are misclustered under their nonhypothesized LVs.

These four criteria can be readily computed by the LVI algorithm that directly outputs the LVs and the associated items. However, the LO and IO criteria are not applicable to the PLS CFA because the true number of LVs is already prespecified. Also, because the SAS Proc Factor and the PLS CFA output LVs with the loadings of each item associated with the LVs, there is no consensus as to what determines a good LV given its loadings. A common guideline for ensuring discriminant validity is that the loading of an item on its hypothesized LV to be reasonably high (e.g., >0.70) while the item loadings on the other LVs should be substantially smaller $( \mathrm { e . g . } , \ < 0 . 4 0 )$ (Gefen et al. 2000). A conservative rule of thumb is for the difference between the hypothesized and nonhypothesized indicators to be at least 0.2. If this rule is violated and an item loads on more than one LV, we detect the indicator as IC. If any indicators from different LVs load into a single LV, we detect LC because the method does not discriminate among these items. If an indicator does not load onto any LV, IO is detected. Finally, if an LV in the true measurement model is not identified by the method, we detect an LO.

Table 5 presents the summary results for LVI, EFA (SAS Proc Factor), and CFA (PLS) for an average over five runs. Column 1 indicates the sample size. Column 2 indicates the noise level (low, medium, or high). Column 3 indicates whether the data is generated from a normal distribution and Column 4 indicates whether there is a nonlinearity, as described above. Table 5 shows that on average the LVI algorithm outperforms the EFA and CFA methods. As the sample size increases, the LVI error shifts from commission to omission. PLS CFA is the least sensitive to sample size. Noise has a negative effect on the performance of the LVI algorithm. Nonnormality affects the CFA the most (e.g., the LC rate goes from 0.36 to 0.68 for n  1 000). However, nonlinearity does not appear to have a clear impact on the three methods.

We ran two repeated measure ANOVA analyses: One between the LVI and the EFA (Table 6) and one between the LVI and the CFA (Table 7) to examine the role of the four simulated dimensions (sample size, noise, normality, and linearity).

Table 6 shows that the LVI is significantly superior to the EFA in terms of LO, LC, and IC (p-value < 005) and marginally significant in terms of IO (p-value 0051) (within subjects). The between subjects comparison shows the LVI to be generally superior to the EFA in terms of sample size, noise, and nonlinearity but not in terms of nonnormality.

Table 6 ANOVA Results Between LVI and EFA (SAS Proc Factor)

<table><tr><td>Comparison</td><td>Source</td><td>Measure</td><td>F-value</td><td>Significance (p-value)</td></tr><tr><td rowspan="4">Within</td><td rowspan="4">LVI vs. EFA</td><td>LO</td><td>4.188</td><td>0.045</td></tr><tr><td>LC</td><td>5.415</td><td>0.023</td></tr><tr><td>IO</td><td>3.947</td><td>0.051</td></tr><tr><td>IC</td><td>6.075</td><td>0.016</td></tr><tr><td rowspan="16">Between</td><td rowspan="4">Sample size</td><td>LO</td><td>27.067</td><td>0.000</td></tr><tr><td>LC</td><td>5.178</td><td>0.008</td></tr><tr><td>IO</td><td>28.189</td><td>0.000</td></tr><tr><td>IC</td><td>2.243</td><td>0.114</td></tr><tr><td rowspan="4">Noise</td><td>LO</td><td>3.066</td><td>0.053</td></tr><tr><td>LC</td><td>10.858</td><td>0.000</td></tr><tr><td>IO</td><td>3.122</td><td>0.050</td></tr><tr><td>IC</td><td>5.417</td><td>0.007</td></tr><tr><td rowspan="4">Nonnormality</td><td>LO</td><td>0.282</td><td>0.597</td></tr><tr><td>LC</td><td>2.516</td><td>0.117</td></tr><tr><td>IO</td><td>0.287</td><td>0.594</td></tr><tr><td>IC</td><td>1.356</td><td>0.248</td></tr><tr><td rowspan="4">Nonlinearity</td><td>LO</td><td>3.785</td><td>0.056</td></tr><tr><td>LC</td><td>11.362</td><td>0.001</td></tr><tr><td>IO</td><td>4.588</td><td>0.036</td></tr><tr><td>IC</td><td>11.503</td><td>0.001</td></tr></table>

Table 7 shows the comparison between LVI and CFA. The within-subjects comparison shows that the LVI algorithm significantly outperforms CFA in terms of both LC and IC. The between-subjects comparison also shows that the LVI outperforms the CFA on virtually all accounts except under sample size for LC.

4.2.4. Structural Model Comparison. This section compares BN-LV with four methods: PLS, LISREL, and two BN methods—the BD-metric approach based on the Dirichlet assumption of the data (Heckerman 1996) and the Gaussian approach that assumes data normality (Glymour et al. 1987). The graph (structural model) generated by the five methods is compared against the prespecified graph (Pavlou 2003) on which the data was simulated. Following Spirtes et al. (2000), we use three comparison criteria:

Table 7 ANOVA Results Between LVI and CFA (PLS)

<table><tr><td>Comparison</td><td>Source</td><td>Measure</td><td>F-value</td><td>Significance</td></tr><tr><td rowspan="2">Within</td><td rowspan="2">LVI vs. CFA</td><td>LC</td><td>41.789</td><td>0.000</td></tr><tr><td>IC</td><td>57.274</td><td>0.000</td></tr><tr><td rowspan="8">Between</td><td rowspan="2">Sample size</td><td>LC</td><td>0.611</td><td>0.546</td></tr><tr><td>IC</td><td>3.885</td><td>0.025</td></tr><tr><td rowspan="2">Noise</td><td>LC</td><td>27.521</td><td>0.000</td></tr><tr><td>IC</td><td>48.402</td><td>0.000</td></tr><tr><td rowspan="2">Nonnormality</td><td>LC</td><td>14.505</td><td>0.000</td></tr><tr><td>IC</td><td>9.009</td><td>0.004</td></tr><tr><td rowspan="2">Nonlinearity</td><td>LC</td><td>14.505</td><td>0.000</td></tr><tr><td>IC</td><td>4.294</td><td>0.042</td></tr></table>

1. Path Omission PO. The error rate associated with omitted paths (links). It is computed as the number of paths that are in the true structural model (graph) but were not identified by the method under investigation, divided by the total number of paths (eight in our simulated study) in the underlying structural model (Pavlou 2003).

2. Path Commission PC. The error rate associated with misidentified paths. It is computed as the number of paths that are identified by the method but do not appear in the true model, divided by the total number of paths in the true model.

3. Path Misdirection PM. The error rate associated with misdirected paths. It is computed as the number of misoriented directions of causality as opposed to the true structural model, divided by the number of true directions (eight in our study).

We further separated the comparison into confirmatory (PLS and LISREL) (Table 8) and exploratory results (BN) (Table 9).

Table 8 Structural Model Comparison Between BN-LV with PLS and LISREL (Confirmatory Mode)

<table><tr><td colspan="4">Simulated dimensions</td><td colspan="2">BN-LV</td><td colspan="2">PLS</td><td colspan="2">LISREL</td></tr><tr><td>Size</td><td>Noise</td><td>Normality</td><td>Linearity</td><td>PO</td><td>PC</td><td>PO</td><td>PC</td><td>PO</td><td>PC</td></tr><tr><td>1,000</td><td>Low</td><td>Yes</td><td>Yes</td><td>0.05</td><td>0.00</td><td>0.00</td><td>0.15</td><td>0.08</td><td>0.00</td></tr><tr><td>1,000</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.05</td><td>0.00</td><td>0.00</td><td>0.10</td><td>0.05</td><td>0.00</td></tr><tr><td>1,000</td><td>High</td><td>Yes</td><td>Yes</td><td>0.00</td><td>0.00</td><td>0.08</td><td>0.05</td><td>0.13</td><td>0.00</td></tr><tr><td>1,000</td><td>Medium</td><td>No</td><td>Yes</td><td>0.05</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.08</td><td>0.02</td></tr><tr><td>1,000</td><td>Medium</td><td>Yes</td><td>No</td><td>0.00</td><td>0.15</td><td>0.03</td><td>0.20</td><td>0.08</td><td>0.13</td></tr><tr><td>250</td><td>Low</td><td>Yes</td><td>Yes</td><td>0.08</td><td>0.03</td><td>0.10</td><td>0.08</td><td>0.15</td><td>0.00</td></tr><tr><td>250</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.03</td><td>0.00</td><td>0.08</td><td>0.00</td><td>0.20</td><td>0.00</td></tr><tr><td>250</td><td>High</td><td>Yes</td><td>Yes</td><td>0.00</td><td>0.03</td><td>0.23</td><td>0.05</td><td>0.25</td><td>0.08</td></tr><tr><td>250</td><td>Medium</td><td>No</td><td>Yes</td><td>0.08</td><td>0.00</td><td>0.10</td><td>0.03</td><td>0.18</td><td>0.00</td></tr><tr><td>250</td><td>Medium</td><td>Yes</td><td>No</td><td>0.03</td><td>0.00</td><td>0.20</td><td>0.13</td><td>0.18</td><td>0.08</td></tr><tr><td>50</td><td>Low</td><td>Yes</td><td>Yes</td><td>0.15</td><td>0.00</td><td>0.33</td><td>0.00</td><td>0.38</td><td>0.00</td></tr><tr><td>50</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.13</td><td>0.00</td><td>0.30</td><td>0.03</td><td>0.35</td><td>0.00</td></tr><tr><td>50</td><td>High</td><td>Yes</td><td>Yes</td><td>0.15</td><td>0.00</td><td>0.33</td><td>0.05</td><td>0.43</td><td>0.00</td></tr><tr><td>50</td><td>Medium</td><td>No</td><td>Yes</td><td>0.10</td><td>0.00</td><td>0.30</td><td>0.00</td><td>0.43</td><td>0.00</td></tr><tr><td>50</td><td>Medium</td><td>Yes</td><td>No</td><td>0.18</td><td>0.00</td><td>0.30</td><td>0.05</td><td>0.53</td><td>0.00</td></tr><tr><td colspan="4">Averages</td><td>0.07</td><td>0.01</td><td>0.16</td><td>0.06</td><td>0.23</td><td>0.02</td></tr></table>

Table 9 Structural Model Comparison Between BN-LV with Dirichlet and Gaussian Methods (Exploratory Mode)

<table><tr><td colspan="4">Simulated dimensions</td><td colspan="2">Common BN error rates</td><td>BN-LV (OL)</td><td>BN (Dirichlet)</td><td>BN (Gaussian)</td></tr><tr><td>Size</td><td>Noise</td><td>Normality</td><td>Linearity</td><td>PO</td><td>PC</td><td>PM</td><td>PM</td><td>PM</td></tr><tr><td>1,000</td><td>Low</td><td>Yes</td><td>Yes</td><td>0.05</td><td>0</td><td>0.28</td><td>0.55</td><td>0.38</td></tr><tr><td>1,000</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.25</td><td>0</td><td>0.23</td><td>0.43</td><td>0.28</td></tr><tr><td>1,000</td><td>High</td><td>Yes</td><td>Yes</td><td>0.18</td><td>0</td><td>0.20</td><td>0.50</td><td>0.50</td></tr><tr><td>1,000</td><td>Medium</td><td>No</td><td>Yes</td><td>0.2</td><td>0</td><td>0.13</td><td>0.38</td><td>0.45</td></tr><tr><td>1,000</td><td>Medium</td><td>Yes</td><td>No</td><td>0.03</td><td>0.15</td><td>0.18</td><td>0.33</td><td>0.53</td></tr><tr><td>250</td><td>Low</td><td>Yes</td><td>Yes</td><td>0.2</td><td>0.03</td><td>0.23</td><td>0.45</td><td>0.48</td></tr><tr><td>250</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.3</td><td>0</td><td>0.20</td><td>0.40</td><td>0.35</td></tr><tr><td>250</td><td>High</td><td>Yes</td><td>Yes</td><td>0.25</td><td>0.03</td><td>0.20</td><td>0.33</td><td>0.30</td></tr><tr><td>250</td><td>Medium</td><td>No</td><td>Yes</td><td>0.28</td><td>0</td><td>0.20</td><td>0.38</td><td>0.35</td></tr><tr><td>250</td><td>Medium</td><td>Yes</td><td>No</td><td>0.3</td><td>0</td><td>0.18</td><td>0.13</td><td>0.30</td></tr><tr><td>50</td><td>Low</td><td>Yes</td><td>Yes</td><td>0.53</td><td>0</td><td>0.15</td><td>0.18</td><td>0.18</td></tr><tr><td>50</td><td>Medium</td><td>Yes</td><td>Yes</td><td>0.4</td><td>0</td><td>0.15</td><td>0.33</td><td>0.20</td></tr><tr><td>50</td><td>High</td><td>Yes</td><td>Yes</td><td>0.41</td><td>0</td><td>0.08</td><td>0.13</td><td>0.15</td></tr><tr><td>50</td><td>Medium</td><td>No</td><td>Yes</td><td>0.3</td><td>0</td><td>0.20</td><td>0.20</td><td>0.23</td></tr><tr><td>50</td><td>Medium</td><td>Yes</td><td>No</td><td>0.3</td><td>0</td><td>0.08</td><td>0.10</td><td>0.07</td></tr><tr><td colspan="4">Averages</td><td></td><td></td><td>0.18</td><td>0.32</td><td>0.31</td></tr></table>

BN-LV operates in both a confirmatory and an exploratory mode<sup>26</sup> while PLS and LISREL operate solely in a confirmatory mode. Therefore, alternative BN approaches (BD-metric and Gaussian) that operate in an exploratory mode must be used for a complete comparison with BN-LV. For the confirmatory mode, a link is considered missing if a hypothesized path is not significant (PO error). A PC error occurs if nonhypothesized link is significant. The PM error is irrelevant because the true direction of the causal links is already prespecified. Table 8 shows that on average BN-LV outperforms both PLS and LISREL with respect to the PO and PC error rates.

Table 9 compares the three BN methods. To make the results consistent, we only apply the three scoring functions to orient directions after an initial graph is generated by algorithm PC2. Therefore, the only relevant criterion is the PM error rate. Table 9 shows that on average our OL function outperforms both the Dirichlet and the Gaussian functions.

Tables 10 and 11 report the ANOVA results with repeated measures. The results demonstrate that BN-LV statistically outperforms the two competing SEM methods in both the confirmatory and in the exploratory mode.

Table 10 ANOVA Results Between BN-LV with Dirichlet and Gaussian Methods (Exploratory Mode)

<table><tr><td rowspan="2"></td><td colspan="3">BN (Dirichlet)</td><td colspan="3">BN (Gaussian)</td></tr><tr><td>Source</td><td>F-value</td><td>Significance</td><td>Source</td><td>F-value</td><td>Significance</td></tr><tr><td>Within</td><td>Dirichlet</td><td>110.454</td><td>0.000</td><td>Gaussian</td><td>53.391</td><td>0.000</td></tr><tr><td rowspan="4">Between</td><td>Size</td><td>30.853</td><td>0.000</td><td>Size</td><td>20.847</td><td>0.000</td></tr><tr><td>Noise</td><td>5.577</td><td>0.006</td><td>Noise</td><td>1.149</td><td>0.323</td></tr><tr><td>Normality</td><td>0.799</td><td>0.374</td><td>Normal</td><td>1.077</td><td>0.303</td></tr><tr><td>Linearity</td><td>21.586</td><td>0.000</td><td>Linear</td><td>0.129</td><td>0.720</td></tr></table>

4.2.5. Discussion of Simulation Results. Based on the simulated results, BN-LV has certain advantages over PLS and LISREL under the following conditions.

Sample Size. The BN-LV method performs consistently better than PLS and LISREL as sample sizes increase (PO errors decrease and PC errors stay low). LISREL substantially improves with larger sample sizes while PLS shows little improvement from medium to large sample sizes. BN-LV is clearly preferred for small sample sizes. Taken together, BN-LV is generally superior to PLS and LISREL across the spectrum of sample sizes 50 250 1 000.

Noise. In terms of noise, PLS and LISREL are shown to generally perform well for high noise levels, consistent with Fornell and Larcker (1981) who find that SEM model fitness based on structure consistency may improve as both the model and the theory decline. BN-LV turns out to be more sensitive to high data noise, especially for the measurement model.

Linearity. When the true relationship among LVs is not linear, BN-LV is shown to be superior to PLS and

Table 11 ANOVA Results Between BN-LV with PLS and LISREL (Confirmatory Mode)

<table><tr><td rowspan="2"></td><td colspan="4">PLS</td><td colspan="4">LISREL</td></tr><tr><td>Source</td><td>Error rate</td><td>F-value</td><td>Significance</td><td>Source</td><td>Error rate</td><td>F-value</td><td>Significance</td></tr><tr><td rowspan="2">Within</td><td rowspan="2">PLS</td><td>PO</td><td>13.595</td><td>0.000</td><td rowspan="2">LISREL</td><td>PO</td><td>53.852</td><td>0.000</td></tr><tr><td>PC</td><td>8.686</td><td>0.004</td><td>PC</td><td>0.881</td><td>0.351</td></tr><tr><td rowspan="8">Between</td><td rowspan="2">Size</td><td>PO</td><td>78.860</td><td>0.000</td><td rowspan="2">Size</td><td>PO</td><td>81.377</td><td>0.000</td></tr><tr><td>PC</td><td>8.151</td><td>0.001</td><td>PC</td><td>2.730</td><td>0.072</td></tr><tr><td rowspan="2">Noise</td><td>PO</td><td>1.289</td><td>0.282</td><td rowspan="2">Noise</td><td>PO</td><td>0.569</td><td>0.569</td></tr><tr><td>PC</td><td>0.631</td><td>0.535</td><td>PC</td><td>0.610</td><td>0.546</td></tr><tr><td rowspan="2">Normality</td><td>PO</td><td>0.158</td><td>0.692</td><td rowspan="2">Normality</td><td>PO</td><td>0.506</td><td>0.479</td></tr><tr><td>PC</td><td>0.199</td><td>0.657</td><td>PC</td><td>0.145</td><td>0.865</td></tr><tr><td rowspan="2">Linearity</td><td>PO</td><td>1.421</td><td>0.237</td><td rowspan="2">Linearity</td><td>PO</td><td>2.560</td><td>0.114</td></tr><tr><td>PC</td><td>12.755</td><td>0.001</td><td>PC</td><td>13.791</td><td>0.000</td></tr></table>

LISREL. This is expected because BN-LV explicitly allows nonlinearities to emerge in the relationships among principal constructs. The main impact of nonlinearity on PLS and LISREL is the PC error in the structural model. For example, for sample size n 1 000, the average PC error for PLS doubles from 0.10 to 0.20 (other dimensions held constant).

Normality. In terms of nonnormality, BN-LV is not affected when the data violate the normality assumption in the measurement model or in the structural model. In contrast, the CFA turns out to be very sensitive to data normality. The effect of nonnormality on LISREL appears to interact with sample size. For large sample sizes, nonnormality has a negative impact on LISREL (PO error increases from 0.05 to 0.08); for medium sample size, PO error decreases from 0.2 to 0.18. However, nonnormality does not considerably affect PLS for the structural model (Chin 1998). Therefore, BN-LV is clearly superior to LISREL but performs comparably to PLS.

The results for the structural model show that both PLS and LISREL make high omission errors in general while PLS commits the highest PC error rate. Therefore, BN-LV outperforms PLS and LISREL both in the PC and the PO error rate.

The simulation study also highlighted the difficulty in manually testing the measurement and the structural model for 75 data sets in PLS and LIREL (each data set required about 30 minutes to calculate the measurement and structural model). In contrast, the automated nature of BN-LV greatly facilitated model estimation (about few seconds per data set). Thus, when there is a need for automating the process of exploring multiple causal structures, particularly for complex models that prohibit a manual specification of all possible structural models, BN-LV is clearly superior to PLS and LISREL.

## 5. Discussion

This study contributes to and has implications for the following literatures: First, it contributes to the empirical IS literature and the social and behavioral sciences in general by proposing a new data analysis method for inductively identifying LVs from raw measurement items and inferring the most likely causal structural model among the identified LVs. Second, it contributes to the BN literature by (a) allowing the identification of multi-item LVs with the proposed LVI algorithm and by (b) allowing discrete and ordinal data in BN with the proposed OL scoring function. Third, it contributes to the SEM literature by addressing three key limitations of existing SEM methods (Lee et al. 1997)—identifying causal links in the structural model, identifying the measurement and structural models in an exploratory manner, and allowing nonlinearities.

## 5.1. Implications for Empirical IS Research

The first contribution is to develop a comprehensive (measurement model construction and structural model discovery) data analysis method for inferring causal relationships among constructs, using observational, cross-sectional data that are discrete and ordinal. In fact, the majority of empirical studies in the IS literature use this type of data in Likert-type scales.

In terms of the measurement model, the proposed LVI algorithm has several advantages over competing methods. First, in contrast to common factor analysis techniques that rely on “rule-of-thumb” heuristics and approximate solutions, LVI offers an exact solution to the measurement model by categorizing all measurement items into LVs. Second, in contrast to CFA methods that impose a certain structure on the data, LVI operates in an exploratory mode, thus allowing the data to “speak out” and be categorized under the most likely LVs. Because BN-LV does not require IS researchers to prespecify which measurement items should belong to each LV, it allows them to explore how new measurement items could be classified into new LVs. By identifying problematic items (those that cannot be categorized under LVs), it allows IS researchers to reevaluate potentially problematic such items. Most important, the LVI algorithm directly tests the fundamental axiom of conditional independence, thus allowing a causal interpretation to the relationship between the LVs and their identified measurement items, consistent with the principles of the psychometric theory of measurement.

In terms of the structural model, BN-LV tests the d-separation conditions and uses the proposed OL scoring function to generate the most likely causal Bayesian network. This allows the inference of causality in structural models without imposing a prespecified structure. By operating in an exploratory mode, BN-LV automatically examines all plausible structural models and selects the most likely one. This provides a major advantage over competing SEM methods that require manual specification of plausible models, especially for complex models where such manual work becomes virtually impossible. This advantage becomes valuable where there is little or no prior theory or when IS researchers want to rely purely on data. This has implications for new theory development (where there is no existing theory basis), which is particularly common in IS research because of the rapid evolution of IT and the introduction of new IT systems.

Finally, as a “conditional probability” method, BN-LV fundamentally differs from existing data analysis tools that rely on the correlation or covariance matrix. Because conditional probabilities can help infer causality (e.g., Druzdzel and Simon 1993, Shugan 1997), the BN-LV method provides IS researchers with another tool to infer causality from observational data.

## 5.2. Implications for the Bayesian Networks Literature

Despite the touted potential of Bayesian networks to facilitate research in the IS literature (Lee et al. 1997), existing BN methods have two key limitations that preclude their application to empirical SEM studies: (1) They cannot readily handle LVs measured with multiple measurement items,<sup>27</sup> and (2) they are not suitable for discrete and ordinal data such as those obtained from Likert-type scales (which are both prevalent in IS research). The proposed BN-LV method overcomes these limitations.

First, our proposed LVI algorithm provides a general method that allows the identification of “hidden” LVs from raw measurement items through an optimal weighting method that maximizes conditional independence. Also, the LVI algorithm does not impose a certain prespecified structure on the measurement model, nor does it make any distributional assumptions. More important, the LVI algorithm uses the axiom of conditional independence as its building block. To our knowledge, this renders the proposed LVI algorithm as the only approach consistent with the theory of measurement: it offers a causal interpretation to the measurement model by specifying directional links from the measurement items to the LVs.

Second, BN-LV extends the BN literature to allow the use of ordinal and discrete data. The proposed OL scoring function overcomes this long-held limitation. Moreover, our simulation results show that OL outperforms the two state-of-the-art BN approaches— the Bayesian Dirichlet and the Gaussian metrics—for ordinal and discrete data.

## 5.3. Implications for Structural Equation Modeling (SEM) Research

As reviewed earlier, SEM methods no longer claim to infer causality, though they were originally designed to model causal relationships. In fact, Pearl (2000) notably observed:

I believe that the causal content of SEM has been allowed to gradually escape the consciousness of SEM practitioners mainly for the following two reasons: (1) SEM practitioners have sought to gain respectability for SEM by keeping causal assumptions implicit, since statisticians, the arbiters of respectability, abhor such assumptions because they are not directly testable and; (2) The algebraic, graph-less language that has dominated SEM research lacks the notational facility needed for making causal assumptions, as distinct from statistical assumptions, explicit. By failing to equip causal relations with distinct mathematical notation, the founding fathers in fact committed the causal foundation of SEM to oblivion. Their disciples today are seeking foundational answers elsewhere (p. 209).

In contrast, BN-LV takes advantage of conditional probabilities to encode directional relationships among LVs, thus permitting a causal interpretation in SEM models. This helps overcome the limitation of SEM methods to infer causality.

Most SEM studies specify one model structure and use data to confirm this specific structure, thus operating in a confirmatory mode.<sup>28</sup> Diligent researchers are supposed to explore plausible alternative models and the lack of an automated method for exploring alternative models potentially overlooks equivalent models (Chin 1998). BN-LV helps overcome this limitation by generating an equivalent class of graphs among LVs based on d-separation tests, scoring each candidate graph using the proposed OL scoring function, and selecting the one with the highest score. In doing so, BN-LV allows IS researchers to operate in an exploratory mode and allows the data to inductively identify the most likely structural model.

SEM encodes relationships among LVs as linear equations, thereby ignoring potential nonlinear relationships. In contrast, BN-LV uses conditional probabilities that do not assume any functional (linear) form, thus allowing nonlinear relationships to emerge among LVs in the structural model. Accounting for nonlinearities is an important strength of the BN-LV method. Our simulation study corroborates this by showing the superiority of BN-LV for data with nonlinearities.

In sum, BN-LV has certain advantages over existing SEM data analysis methods under the following conditions:

1. In the early stages of research when a hypothesis has not yet been developed, particularly when a researcher prefers to let data “speak by themselves” as opposed to testing a prespecified measurement or structural model.

2. When theory and the literature provide little guidance on the causal structure of a structural model, particularly when the researcher needs to inductively explore several potential structural models to identify the most appropriate one.

3. When there is need to automate the process for exploring potential causal structures, in particular for complex models with numerous permutations among LVs that prohibit the researcher from manually specifying all potential models.

4. When the researcher needs to have a stronger causal interpretation. The conditional probabilitybased BN-LV method is theoretically closer to the notion of causality than existing correlation- or covariance-based methods.

5. When the data violate normality assumptions and when the true relationships among the LVs are nonlinear. BN-LV is also found to be more robust to small sample size. However, SEM approaches are less sensitive to high data noise.

Therefore, BN-LV can be used under these conditions to complement existing SEM methods.

## 5.4. Limitations and Suggestions for Future Research

The paper also has a number of limitations, which create some interesting opportunities for future research.

First, because this paper focuses on observational (cross-sectional, nonexperimental data), we address only two of Popper’s (1959) conditions for inferring causality (correlation between X and Y and accounting for potential confounds), excluding the condition that X must temporally precede Y . Following Granger (1986) who distinguishes between temporal and cross-sectional causality, our method does not claim to create the necessary and sufficient conditions for inferring “absolute” causality, but it is posited as a method of inferring “near” causality from observational, nonexperimental data. However, if temporal ordering among variables is already known from the data, the BN-LV method can sort all variables in a temporal order and add a constraint to only allow the preceding variables to cause the subsequent variables when constructing the BN. This approach will permit longitudinal or experimental data to be used in the BN-LV method, and the temporal constraint will also greatly reduce the complexity of the BN construction. The challenge for future research, however, is to identify the temporal ordering among variables from longitudinal data.

Second, the BN-LV method aims to discover the most likely causal structure in a probabilistic (not deterministic) fashion. By no means does the most likely causal structure discovered by the BN-LV necessarily capture the definite causal model. As noted in §2, there is still disagreement among many philosophers and researchers about the possibility to infer causality from data deterministically or probabilistically. In response to some philosophers who argue that causality can only be inferred from controlled experiments that account for all potential confounds, BN-LV examines the relationship between X and Y while capturing possible confounds Z by evaluating d-separation conditions. Though rigorous researchers are supposed to account for all potential confounds, future research could develop a formal method to test whether the existing confounds Z in the data are “adequate” to assure that the X Y relationship is truly and significantly causal.

Third, BN-LV only deals with LV identification given observed measurement items. However, it does not address the more general missing variable problem—how to build a model when potentially relevant LVs are unobserved and thus may not have been necessarily captured by the data (raw measurement items). When a relevant variable is missing from the set of Z variables, it may cause inconsistency in the d-separation condition of BN-LV. An intuitive solution is to search for the missing (unobserved) variables. Hutchinson et al. (2000, p. 325) call this a “needle in a haystack” problem because seeking all missing variables is unending and it is very likely that the key sources of unobserved effects may never be found. Indeed, a major challenge for causality inference is to account for all possible confounding variables (Mitchell and James 2001, Allison 2005). Recent advances in econometrics and marketing have looked into this problem, primarily via latent class modeling and mixture models. It is assumed that responses are not from a single population (group). However, what causes the group membership is unobserved and cannot be determined a priori. These studies do represent a major step toward identifying missing variables but the literature has still not addressed the general structure problem of LVs, discussed in §3.1. Most studies make specific assumptions on the structure of the LVs. Once the structure is known, the LV identification problem is simplified as one of finding the parameters that fit the LV structure best. This is best reflected by the finite mixture model where each observation may arise from two or more unobserved groups that have a common distribution but different parameters. Still, the “missing variables” problem remains a caveat in the literature. Solutions to this problem by future research can be readily integrated into the proposed BN-LV method to provide a more accurate set of Z variables for accounting for the d-separation condition.

Fourth, besides BN, the propensity scores approach (Mithas and Krishnan 2009) is a promising causal method. However, existing methods are not readily applicable to the complex nexus of causal relationships in the structural model addressed here. There are two key challenges to extend the propensity scores approach to our problem: (1) determining the propensity scores in the presence of multiple causes, and (2) identifying the right cloning for a given individual in the presence of multiple values of a given variable. Both issues need to be investigated by future research.

Finally, BN techniques cannot distinguish between structures that entail the same likelihood, especially when the two structures have the same V -structures (see our discussion in §3.3 and Spirtes et al. 2000, p. 60). In these cases, theoretical arguments may be necessary to specify the best structure. However, the BN-LV method is a data analysis method that only examines the measurement and structural model and does not address issues of theory development, measurement development, data collection, or theory implications. Similar to the study of Lee et al. (1997) study, future research could explore how the proposed BN-LV method can be integrated into a comprehensive method for theory building, empirical validation, and theory implications.

## Concluding Remarks

Causality is a fundamental characteristic of a good theory, but the difficulty in inferring causality has forced researchers to either infer causality from pure theory (Carte and Russell 2003) or from longitudinal (Granger 1986), experimental (Cook and Campbell 1979), or panel (Allison 2005) data. This paper is an attempt to revive the pursuit of causality in structural models from observational data in the IS literature in particular and the social sciences in general, and encourage IS researchers to bring causality considerations back into IS studies. The proposed BN-LV method aims to provide a tool for IS researchers to better understand how causal relationships can be inferred in structural models from observational data. We hope the proposed data analysis method serves as a modest starting point for enhancing methods for inferring causality and building causal theories in the IS literature. Given the enhanced sophistication of IS research in terms of theory and methods, causality can become an important consideration in the IS literature.

## Appendix A. The LVI Algorithm

The algorithmic steps of the LVI algorithm are outlined in Table A1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table A1 Steps of the LVI Algorithm
Input:  $X = (X_{1}, X_{2}, \ldots, X_{m})$ 
Output: disjoint item sets, each of which represents an LV
1.  $L_{1} \leftarrow \text{all } \{x_{i}\}, i \in (1, \ldots, m)$ 
2.  $L_{2} \leftarrow \text{all } \{x_{i}, x_{j}\}$  that meet C-1,  $i, j \in (1, \ldots, m), i \neq j$  /* (see §3.2.3)
3. for  $(k = 2; L_{k} \neq \phi \text{ and } k \leq m - 1; k++)$  {
4. generate  $L_{k+1}$ ;
(a)  $C_{k+1} \leftarrow \text{adding } x_{i} (x_{i} \notin L_{k}) \text{ to } L_{k}$  /* adding  $x_{i}$  one at a time
(b) Eliminate  $C_{k+1}$  that do not meet C-1
(c) Eliminate  $C_{k+1}$  that do not meet C-2
5. }
6. Prune  $L_{k}$  for all  $k \in (1, \ldots, m)$  /* (see §3.2.3)
(a) Identify supersets and delete all subsets
(b) Detect overlapping measurement items and determine which item set to keep the items /* start from the largest item sets and then go down the list to ensure the minimum number of LVs
7. Output all  $L_{k}$
</div>

## Appendix B. The Proposed PC2 Algorithm

Table B1 summarizes the steps of Algorithm PC2. For more detailed discussion of Algorithm PC, please refer to Spirtes et al. (2000). The proposed PC2 algorithm has three main steps:

• Step 1 initiates a fully connected, undirected graph.

• Step 2 computes $R _ { x , y \mid z }$ for all possible X, Y , and Z. If $R _ { x , y \mid z } = 0 ,$ , then delete the edge between X and Y .

• Step 3 orients the graph using five rules of directing an undirected graph (Verma and Pearl 1992).

## Table B1 The Proposed PC2 Algorithm

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1. Start with the complete (all nodes are connected), undirected graph G

Step 2. Generate reduced undirected graph  $G'$ 

(1) Test if  $R_{x,y|z}=0$  for each edge

(2) Delete the edges that are d-separated by Z (where  $R_{x,y|z}=0$ )

Step 3. Direct  $G'$  using the following five rules:

Rule 1. For each triple of vertices X, Y, Z such that the pair X, Y, and the pair Y, Z are each adjacent in C but the pair X, Z are not adjacent in C, orient X-Y-Z as  $X\to Y\leftarrow Z$  if and only if Y does not d-separate X and Z and if it does not introduce a cycle of direction. If this edge reverses the previous orientation, then make it bidirectory

Rule 2. If  $X\to Y$ , Y-Z and X and Z are not adjacent, then direct  $Y\to Z$ 

Rule 3. If  $X\to Y$ ,  $Y\to Z$ , and X-Z, then direct  $X\to Z$ 

Rule 4. If X-Y, Y-Z, Y-W,  $X\to W$ ,  $Z\to W$ , then  $Y\to W$ 

Rule 5. If X-Y, Y-Z, X-Z, Z-W,  $W\to X$ , then  $X\to Y$  and  $Z\to Y$
</div>

## Appendix C. Deriving the OL Metric

We assume that a subject’s response (e.g., to a measurement item) is a choice among r ordered values, rendering r possible ordered values $( 1 , \ldots , r )$ of a variable (node) x. For this type of choice behavior, the OL model is appropriate (Borooah 2002). Let $p _ { i } = P ( x = i \mid \pi )$ and $i \in ( 1 , \ldots , r )$ be the conditional probability of x i given its parents . We have the following OL functions:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\begin{array}{rl} &amp; {\log it(p_1) = \log (p_1 / 1 - p_1) = \alpha_1 + \sum_{i = 1}^q\beta_i\pi_i}\\ &amp; {\log it(p_1 + p_2) = \log (p_1 + p_2 / 1 - p_1 - p_2) = \alpha_2 + \sum_{i = 1}^q\beta_i\pi_i}\\ &amp; {\dots}\\ &amp; {\log it(p_1 + p_2 + \dots +p_{r - 1})}\\ &amp; {\quad = \log (p_1 + p_2 + \dots +p_{r - 1} / 1 - p_1 - p_2 - \dots -p_{r - 1})}\\ &amp; {\quad = \alpha_{r - 1} + \sum_{i = 1}^q\beta_i\pi_i}\\ &amp; {p_1 + p_2 + \dots +p_r = 1.} \end{array}$
</div>

An ordered logistic regression estimates $( r - 1 )$ intercepts $\alpha _ { 1 } , \ldots , \alpha _ { r - 1 }$ and $q$ coefficients (\*s). Note that each possible value i has a different regression equation with different $\alpha _ { i }$ but with the same $\beta .$ Once the parameters are estimated, it is possible to derive the individual conditional probability $p _ { i } , \ i \in ( 1 , \ldots , r )$ from the set of equations above. The OL function is defined as the solution of $p _ { i }$ to the above equations.

## Appendix D. The Time Complexity of the BN-LV Method

The proposed BN-LV algorithm can be decomposed into three parts: algorithm LVI, PC2, and the OL scoring function. We discuss the computation complexity for each of these three components below:

1. The LVI Algorithm. Assume there are n measurements. Item set $L _ { k }$ has at most $n / k$ item sets. And there are at most $( n - k )$ candidate items need to be evaluated. At each step, LVI needs to check two conditions: C-1 and C-2. The most expensive one is condition C-2, whose complexity depends on the optimization procedure (Equation (4)). Let us denote this complexity as oC2. Therefore, the overall complexity is given by:

$$
\sum_ {k = 1} ^ {n} (n / k) \times (n - k) \times o (C) = \left[ n ^ {2} \sum_ {k} 1 / k - n (n + 1) / 2 \right] \times o (c 2).
$$

$\scriptstyle \sum _ { k = 1 } ^ { n } 1 / k$ is the Harmonic series, which diverges very slowly. When $n = 1 , 0 0 0 .$ , the value is 7.48. Therefore, we can treat it as a constant. Hence, the complexity is $n ^ { 2 } o ( c 2 )$ , the number of tests that must be examined.

2. PC2 Algorithm. Spirtes et al. (2000, p. 86) demonstrates that the PC2 complexity is given by $\bar { n ^ { 2 } } ( n - 1 ) ^ { k - 1 } / ( k - 1 ) !$ where k is the maximum number of edges a node can have.

Table D1 Illustration of the Computational Cost of BN-LV Method

<table><tr><td></td><td>Original sample</td><td>10 × Original data points</td></tr><tr><td>TAM model (Pavlou 2003)</td><td>&lt;1 second</td><td>&lt;1 second</td></tr><tr><td>(k=8, m=3, n=151)</td><td>(151 data points)</td><td>(1,510 data points)</td></tr><tr><td>TAM-trust model (Pavlou 2003)</td><td>&lt;1 second</td><td>3.5 seconds</td></tr><tr><td>(k=13, m=5, n=151)</td><td>(151 data points)</td><td>(1,510 data points)</td></tr><tr><td>Extended TPB model</td><td>≈3 minutes</td><td>≈6 hours</td></tr><tr><td>(Pavlou and Fygenson 2006)</td><td></td><td></td></tr><tr><td>(k=24, m=14, n=266)</td><td>(266 data points)</td><td>(2,660 data points)</td></tr></table>

3. The OL Scoring Function. The number of edges that need to be directed at the worst case is $n ^ { k } .$ , suggesting that the scoring function needs to run $n ^ { k }$ times ordered logistic regression.

To investigate how the time complexity of the BN-LV method varies as a function of the number of measurement items (denoted by k), the number of constructs (denoted as m), and the number of data points (denoted as n), Table D1 presents the results of six scenarios. The three rows represent three data sets used in prior research with different level of complexity. The second column represents the original data set and the third column represents the original data set bootstrapped to artificially generate 10 times larger data sets. The results (on a 2 GB RAM and 2 GHZ CPU computer) show that BN-LV is more sensitive to the number of measurement items than to the number of data points. In sum, BN-LV can easily run on typical data sets encountered in most empirical IS studies.

## References

Allison, P. D. 2005. Causal inference with panel data. Amer. Sociol. Association Annual Meeting, Philadelphia. http://www. allacademic.com/meta/p23194\_index.html.

Aristotle. 350 b.c. Physics, Book II. Translated by R. P. Hardie, R. K. Gaye in 1994. Massachusetts Institute of Technology, Cambridge. http://classics.mit.edu/Aristotle/physics.2.ii.html.

Bagozzi, R. P. 1980. Causal Modes in Marketing. Wiley, New York.

Binder, J., D. Koller, S. Russell, K. Kanazawa. 1997. Adaptive probabilistic networks with hidden variables. Machine Learn. 29 213–244.

Bollen, K. A. 1989. Structural Equations with Latent Variables. John Wiley and Sons, New York.

Borooah, V. 2002. Logit and Probit: Ordered and Multinomial Models. Sage Publications, Thousand Oaks, CA.

Breckler, S. J. 1990. Application of covariance structure modeling in psychology: Causes for concern? Psych. Bull. 107(2) 260–372.

Carte, T., C. Russell. 2003. In pursuit of moderation: Nine common errors and their solutions. MIS Quart. 27(3) 479–501.

Cartwright, N. 1995. Probabilities and experiments. J. Econometrics 67(1) 47–59.

Chickering, D. 2002. Optimal structure identification with greedy search. J. Machine Learn. Res. 3(3) 507–554.

Chickering, D., D. Heckerman. 1997. Efficient approximation for the marginal likelihood of Bayesian networks with hidden variables. Machine Learn. 29 181–212.

Chin, W. W. 1998. Issues and opinion on structural equation mod eling. MIS Quart. 22(1) 7–16.

Cook, T. D., D. T. Campbell. 1979. Quasi-Experimentation: Design and Analysis for Field Settings. Rand McNally, Chicago.

Cooper, G. 1995. A Bayesian method for learning belief networks that contain hidden variables. J. Intelligent Inform. Systems 4 71–88.

Cooper, G., E. Herskovits. 1992. A Bayesian method for the induction of probabilistic networks from data. Machine Learn. 9 309–347.

Davis, F. D. 1989. Perceived usefulness, perceived ease of use and user acceptance of information technology. MIS Quart. 13(3) 319–340.

Dayton, M., G. Macready. 1988. Concomitant-variable latent-class models. J. Amer. Statist. Assoc. 83(401) 173–178.

Descartes, R. 1637. Discourse on method. Translated by J. Cottingham, R. Stoothoff, D. Murdoch, and A. Kenny (1991). The Philosophical Writings of Descartes. Cambridge University Press, Cambridge, UK.

Druzdzel, M., H. Simon. 1993. Causality in Bayesian belief networks. Proc. 9th Annual Conf. Uncertainty Artificial Intelligence UAI, Washington, DC, 3–11.

Elidan, G., N. Friedman. 2001. Learning the dimensionality of hid den variables. Proc. 17th Conf. Annual Uncertainty Artificial Intelligence UAI, Seattle, WA, 144–151.

Elidan, G., N. Lotner, N. Friedman, D. Koller. 2000. Discovering hidden variables: A structure-based approach. Adv. Neural Inform. Processing Systems 13(1) 30–37.

Fornell, C., D. Larcker. 1981. Evaluation structural equation models with unobserved variables and measurement error. J. Marketing Res. 18(1) 39–50.

Friedman, N. 1997. Learning belief networks in the presence of missing values and hidden variables. Proc. Internat. Conf. Machine Learn. ICML 97, Nashville, TN, 125–133.

Friedman, N., M. Linial, I. Machman, D. Peer. 2000. Using Bayesian networks to analyze expression data. J. Computational Biol. 7(3/4) 601–620.

Gefen, D., E. Karahanna, D. W. Straub. 2003. Trust and TAM in online shopping: An integrated model. MIS Quart. 27(1) 51–90.

Gefen, D., D. W. Straub, M.-C. Boudreau. 2000. Structural equation modeling and regression: Guidelines for research practice. Comm. Association Inform. Systems 4(7) 1–70.

Glymour, C., R. Scheines, P. Spirtes, K. Kelly. 1987. Discovering Causal Structure: Artificial Intelligence, Philosophy and Statistical Modeling. Academic Press, San Diego.

Goldstein, E. 1994. Psychology. Brooks/Cole Publishing Company, Belmont, MA.

Granger, C. 1986. Statistics and causal inferences: Comment. J. Amer. Statist. Association 81(396) 967–968.

Heckerman, D. 1996. A tutorial on learning Bayesian networks. Technical Report MSR-TR-95-06, Microsoft Research, Redmond, WA. http://citeseer.ist.psu.edu/heckerman95tutorial.html.

Heckerman, D., D. Geiger, D. Chickering. 1995. Learning Bayesian networks: The combination of knowledge and statistical data. Machine Learn. 20 197–243.

Heinen, T. 1996. Latent Class and Discrete Latent Trait Models. Sage Publications, New York.

Holland, P. 1986. Statistics and causal inference. J. Amer. Statist. Association 81 945–960.

Hume, D. 1738. A treatise of human nature. Report, Clarendon Press, Oxford, UK (1996).

Hutchinson, W., W. Kamakura, J. Lynch. 2000. Unobserved heterogeneity as an alternative explanation for reversal effects in behavioral research. J. Consumer Res. 27 323–344.

Kant, I. 1781. The Critique of Pure Reason. Translation by J. M. D. Meiklejohn. 1999. Cambridge University Press, London. http:// eserver.org/philosophy/kant/critique-of-pure-reason.txt.

Kenny, D., C. Judd. 1984. Estimating the nonlinear and interactive effects of latent variables. Psych. Bull. 96(1) 201–210.

Kline, R. B. 1998. Principles and Practice of Structural Equation Modeling. Guilford Press, New York.

Lee, B., A. Barua, A. B. Whinston. 1997. Discovery and representation of causal relationships in MIS research: A methodological framework. MIS Quart. 21(1) 109–136.

Mitchell, T. R., L. R. James. 2001. Building better theory: Time and the specification of when things happen. Acad. Management Rev. 26(4) 530–547.

Mithas, S., M. Krishnan. 2009. From association to causation via a potential outcomes approach. Inform. Systems Res. 20(2) 295–313.

Mithas, S., D. Almirall, M. Krishnan. 2006. Do CRM systems cause one-to-one marketing effectiveness? Statist. Sci. 21(2) 223–233.

Pavlou, P. A. 2003. Consumer acceptance of electronic commerce: Integrating trust and risk with the technology acceptance model. Internat. J. Electronic Commerce 7(3) 69–103.

Pearl, J. 1998. Graphs, causality, and structural equation models. Sociol. Methods Res. 27(2) 226–284.

Pearl, J. 2000. Causality: Models, Reasoning and Inference. Cambridge University Press, Cambridge, UK.

Pearl, J., T. Verma. 1991. A theory of inferred causation. Proc. Principles Knowledge Presentation Reasoning 2(1) 441–452.

Pearson, K. 1897. Mathematical contributions to the theory of evolution. Proc. Roy. Soc. London 60 489–503.

Plato. 360 b.c. The Republic. Translated by Benjamin Jowett in 1893. Wikisource, New York. http://en.wikisource.org/wiki/ TheRepublic.

Popper, K. 1959. The Logic of Scientific Discovery. Basic Books, New York.

Rubin, D., R. Waterman. 2006. Estimating the causal effects of marketing interventions using propensity score methodology. Statist. Sci. 21(2) 206–222.

Sarkar, S., R. Sriram. 2001. Bayesian models for early warnings of bank failures. Management Sci. 47(10) 1457–1475.

Shugan, S. M. 2007. Causality, unintended consequences and deducing shared causes. Marketing Sci. 26(6) 731–741.

Silva, R., R. Scheines, C. Glymour, P. Spirtes. 2006. Learning the structure of linear latent variables. J. Machine Learn. Res. 7 191–246.

Skrondal, A., S. Rable-Hesketh. 2004. Generalized Latent Variable Modeling. Chapman & Hall, London.

Spinoza, B. 1662. On the improvement of the understanding. Translated by R. H. M. Elwes. In The Chief Works of Benedict de Spinoza. 1883. G. Bell & Sons, London.

Spirtes, P., C. Glymour, R. Scheines. 2000. Causation, Prediction, and Search. MIT Press, Cambridge, MA.

Spirtes, P., C. Glymour, R. Scheines. 2002. Data mining tasks and methods: Probabilistic and causal networks: Mining for probabilistic networks. Handbook of Data Mining and Knowledge Discovery. Oxford University Press, New York.

Spirtes, P., T. Richardson, C. Meek, R. Scheines, C. Glymour. 1998. Using path diagrams as a structural equation modeling tool. Sociol. Methods Res. 27(2) 182–225.

Suppes, P. 1970. A Probabilistic Theory of Causality. North Holland Publishing Company, Amsterdam.

Torgerson, W. S. 1958. Theory and Methods of Scaling. Wiley, New York.

Verma, T., J. Pearl. 1992. An algorithm for deciding if a set of observed independencies has a causal explanation. Proc. 8th Annual Conf. Uncertainty Artificial Intelligence UAL, Stanford University, Palo Alto, CA, 323–330.
