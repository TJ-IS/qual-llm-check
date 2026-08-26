---
otero_id: 19772
otero_key: "52TG4NU2"
title: "LINDA-BN: An interpretable probabilistic approach for demystifying black-box predictive models"
authors: "Catarina Moreira; Yu-Liang Chou; Mythreyi Velmurugan; Chun Ouyang; Renuka Sindhgatta; Peter Bruza"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113561"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# LINDA-BN: An interpretable probabilistic approach for demystifying black-box predictive models

Catarina Moreira <sup>\*</sup>, Yu-Liang Chou, Mythreyi Velmurugan, Chun Ouyang, Renuka Sindhgatta, Peter Bruza

School of Information Systems, Queensland University of Technology, Brisbane, Australia

## A R T I C L E I N F O

Keywords: Interpretable machine learning Post-hoc interpretation Probabilistic inference Bayesian network Predictive analytics Explainable AI

## A B S T R A C T

The use of sophisticated machine learning models for critical decision-making faces the challenge that these models are often applied as a ‘black-box’. This has led to an increased interest in interpretable machine learning, where post-hoc model-agnostic algorithms present a useful mechanism for generating interpretations of complex learning models. This paper proposes a novel approach based on Bayesian Networks to generate local post-hoc model-agnostic interpretations of a black-box predictive model. Consequently, the proposed approach presents features that are conditionally dependent between each other and that are directly influencing the class variable This enables the decision-maker to better understand how features are related and why a certain prediction was made. Compared to the existing post-hoc interpretation methods, the contribution of our approach is three-fold: (1) as a probabilistic graphical model, the extracted Bayesian network can provide interpretations through conditional dependencies in a graphical structure regarding what input features and how/why they contributed to a prediction; (2) for complex decision problems with many features, a Markov blanket can be generated from the extracted Bavesian network to provide interpretations with a focused view on those input features that directly contributed to a prediction; (3) the extracted Bayesian network enables the identification of four different rules which can inform the decision-maker about the confidence level in a prediction, thus helping the decision-maker assess the reliability of predictions learned by a black-box model. We implemented the proposed approach, applied it in the context of two well-known public datasets and analysed the results, which are made available in an open-source repository: https://github.com/catarina-moreira/LINDA\_DSS.

## 1. Introduction

The rapidly growing adoption of Artificial intelligence (AI) has led to the development of supervised machine learning, in particular, deep neural networks, for generating predictions of high accuracy [1]. While the advancement has the potential to make a significant improvement to the state-of-the-art in operational decision-making across various business domains and processes, the underlying models are often opaque and do not provide the decision-maker with any understanding of their internal predictive mechanisms. This opaqueness in machine learning models is known as the black-box problem. Immediate consequences of trusting predictions from opaque models might result in severe losses for businesses (and people), unfair job losses, or even lead to negative im pacts in certain societal groups (for instance, racial and gender discrimination) [2]. This has posed an open challenge to data scientists and business analysts on how to endow machine intelligence with capabilities to explain the underlying predictive mechanisms in a way that helps decision-makers understand and scrutinize the machinelearned predictions.

The recent body of literature in machine learning has emphasised the need to interpret and explain the (machine) learned predictions. Methods and techniques have been proposed for explaining black-box models which are known as interpretable machine learning [3] or, in a broader context, explainable AI (XAI) [4]. So far, there exists two different mechanisms to address model interpretability. One is to have an interpretable model that provides transparency at three levels: the entire model, the individual components and the learning algorithm [5]. For example, both linear regression models and decision tree models are interpretable models.

Another mechanism to address model interpretability is to develop model-agnostic algorithms that consist of extracting explanations and visualisations from the sophisticated internal representations of a trained machine learning model [6]. These approaches are particularly useful to generate explanations independently of the algorithm that was used to learn the model. An alternative to model-agnostic methods is to use model-specific interpretation methods that are optimised for a spe cific learning algorithm (such as neural networks, XGBoost, etc.). Both model-agnostic and model-specific methods are called post-hoc in terpretations. The existing post-hoc interpretation techniques present knowledge about the various levels of impact of individual input fea tures on the corresponding prediction (see a review in [3]).

In this paper, we propose a novel approach underpinned by an extended framework of Bayesian networks for generating post-hoc interpretations of a black-box predictive model, with a focus on providing interpretations for any instance of prediction learned by the model (known as local interpretations). We name this framework the Local Interpretation-Driven Abstract Bayesian Network (LINDA-BN), which supports extracting a Bayesian network as an approximation (or an abstraction) of a black-box model for a specific prediction learned from any given input. Consequently, interpretations are computed through conditional dependencies between features, representing in fluences from each feature towards the class variable. We hypothesise that this property is fundamental in the current state-of-the-art deep learning models such as neural networks to provide an understanding of why certain features are significant for the predictions of a specific data point. In neural networks, for instance, when independent fea tures pass through the first hidden layer of the network, the features are no longer independent between each other, but they become correlated. For this reason, we argue that local explanations should not be computed in terms of weights of individual features, but rather as weights of features in a graphical structure that share dependencies and influence each other. We implemented our approach, applied it in the context of two well-known public datasets and analysed the re sults, which are made available in an open-source repository (https://github.com/catarina-moreira/LINDA\_DSS).

Compared to the existing model-agnostic interpretation methods, the contribution of our approach is three-fold.

• The extracted Bayesian network not only can provide interpretations about what input features contributed to the corresponding predic tion. As a probabilistic graphical model, it also represents knowledge about dependencies (in the form of conditional probabilities) be tween input features and prediction, thus generating interpretations about why certain input features contributed to the prediction.

• For complex decision problems with a large number of features, the extracted Bayesian network is often complicated to be analysed by a human. In this case, LINDA-BN supports generating a Markov blan ket from the extracted Bayesian network. The Markov blanket de termines the boundaries of a decision system in a statistical sense and presents a graph structure covering a decision (e.g., a prediction), its parents, children, and the parents of the children. As such, the Markov blanket of the extracted Bayesian network provides inter pretation with a focused view on those input features that directly contributed to the corresponding prediction.

• The extracted Bayesian network enables the identification of four different rules which can inform the decision-maker about the con fidence level in a given prediction. As such, the interpretations provided in our approach can help the decision-maker assess the reliability of predictions learned by a black-box model.

In the rest of the paper, we continue to introduce the relevant con cepts and review the related research efforts in Section 2.

We present our approach underpinned by the framework LINDA-BN in Section 3. Next, we report the experiments and discuss the results of the analysis in Section 4. Finally, we conclude the paper with an outlook to future work (Section 5).

## 2. Background and related work

In this section, we present the main concepts that are used throughout our work, and review research efforts that are related to the proposed framework.

## 2.1. Concepts

Prior to discussing existing work that relates to our approach on providing interpretations of a black-box machine learning model pre diction, we note the following definitions:

• black-box predictor: It is a machine learning opaque model, whose internals are either unknown to the observer or they are known but are not understandable by humans.

• Interpretability: The ability to extract symbolic information out of a black-box that can provide the meaning in understandable terms to a human [7].

• Explainability: The ability to highlight decision-relevant parts of the used representations of the algorithms and active parts in the algo rithmic model, that either contribute to the model accuracy on the training set, or a specific prediction for one particular observation [8].

One can see interpretability as the extraction of symbolic informa tion from the black-box (machine-level) that already needs some degree of semantics and explainability as the conversion of this symbolic in formation to a human understandable way (human-level).

## 2.2. Related work

Various approaches have been proposed in the literature to address the problem of interpretability. Generally, this problem can be classified into two major models: Interpretable models and model-agnostic models. Interpretable models are by design already interpretable, providing the decision-maker with a transparent white-box approach for prediction. Decision trees, logistic regression, and linear regression are commonly used interpretable models. These models have been used to explain predictions of specific prediction problems [9]. Model-agnostic approaches, on the other hand, refer to the derivation of explanations from a black-box predictor by extracting information about the under lying mechanisms of the system. In addition, studies have focused on providing model-specific post-hoc explanations [10]. The focus of our work is to build model-agnostic post-hoc methods as they have the flexibility of being applied to any predictive model as compared to model-specific post-hoc approaches. To discover the predictive blackbox models, in this work we focus on the widely cited post-hoc models that include LIME [11] and SHAP [12].

## 2.2.1. LIME

Local Interpretable Model-agnostic Explanations (LIME) [11] ex plains the predictions of any classifier by approximating it with a locally faithful interpretable model. Hence, LIME generates local in terpretations by perturbing a sample around the input vector within a local decision boundary [11,13]. Each feature is associated with a weight that is computed using a similarity function that measures the distances between the original instance prediction and the predictions of the sampled points in the local decision boundary. Linear regression is learned to determine the local importance of each feature.

LIME has been extensively applied in the literature. For instance, Stiffler et al. [14] used LIME to generate salience maps of a certain re gion showing which parts of the image affect how the black-box model reaches a classification for a given test image. Tan et al. [15] applied LIME to demonstrate the presence of uncertainty in the explanations that could raise concerns in the use of the black-box model and diminish the value of the explanations under different sources of uncertainty in the explanation. Their work demonstrates the presence of three sources of uncertainty: randomness in the sampling procedure, variation with sampling proximity, and variation in the explained model across different data points. Anchor [16] is an extension of LIME that attempts to address some of the limitations by maximizing likelihood on how a certain feature might contribute to a prediction. Anchor introduces IF THEN rules as explanations as well as the notion of coverage, which allows the decision-maker to understand the boundaries in which the generated explanations are valid.

## 2.2.2. SHAP

The SHAP (SHapley Additive exPlanations) is an explanation method which uses Shapley values [17] from coalitional game theory to fairly distribute the gain among players, where contributions of players are unequal [12]. Shapley values are a concept in economics and game theory and consist of a method to fairly distribute the payout of a game among a set of players. One can map these game-theoretic concepts directly to an XAI approach: a game is the prediction task for a single instance; the players are the feature values of the instance that collaborate to receive the gain. This gain consists of the difference between the Shapley value of the prediction and the average of the Shapley values of the predictions among the feature values of the instance to be explained [18].

Strumbelj and Kononenko [18] claim that in a coalition game, it i usually assumed that n players form a grand coalition that has a certain value. Given that we know how much each smaller (subset) coalition would have been worth, the goal is to distribute the value of the grand coalition among players fairly (that is, each player should receive a fair share, taking into account all sub-coalitions). Lundberg and Lee [12] on the other hand, present an explanation using SHAP values and the dif ferences between them to estimate the gains of each feature.

To fairly distribute the payoff among players in a collaborative game, SHAP makes use of four fairness properties: (1) Additivity, which states that amounts must sum up to the final game result, (2) Symmetry, which states that if one player contributes more to the game, (s)he cannot get less reward, (3) Efficiency, which states that the prediction must be fairly attributed to the feature values, and (4) Dummy, which says that a feature that does not contribute to the outcome should have a Shapley value of zero.

In terms of related literature, Miller Janny Ariza-Garzo´n and Segovia-Vargas [19] adopted SHAP values to assess the logistic regression model and several machine learning algorithms for granting scores in P2P (peerto-peer) lending; the authors point out SHAP values can reflect disper sion, nonlinearity and structural breaks in the relationships between each feature and the target variable. They concluded that SHAP could provide accurate and transparent results on the credit scoring model. Parsa et al. [20] also highlight that SHAP could bring insightful meanings to inter pret prediction outcomes. For instance, one of the techniques in the model, XGBoost, not only is capable of evaluating the global importance of the impacts of features on the output of a model, but it can also extract complex and non-linear joint impacts of local features.

## 2.2.3. Probabilistic graphical model

The literature of interpretable methods for explainable AI based on probabilistic graphical models (PGM) is mostly dominated by models based on counterfactual reasoning in order to derive explanations for a specific local datapoint.

The counterfactual explanation based on PGM comprises of a con ditional assertion whose antecedent is false and whose consequent de scribes how the world would have been if the antecedent had occurred. It provides interpretations as a mean to point out which changes would be necessary to accomplish the desired goal, rather than supporting the understanding of why the current situation had a certain predictive outcome [21]. For instance, in a scenario where a machine learning algorithm assesses whether a person should be granted a loan or not, a counterfactual explanation of why a person did not have a loan granted could be in the form of a scenario if your income was higher than \$15,000 you would be granted a loan [22]. Unlike other explanation methods that depend on approximating an interpretable model within a perturbed decision boundary, counterfactual explanations have the strength that it is always truthful to the underlying model by providing direct outputs of the algorithms [11].

Counterfactual explanations are part of causal inference methods, which are based on causal reasoning and are focused on the estimation of the causal effects from treatments and actions [23]. In 2000, Pearl proposed a framework (the ladder of causation) that proposes different levels of causal relationships during causal inference. Level $^ { 1 , }$ Associa tion, entails the sensing of regularities or patterns in the input data, expressed as relations; it focuses on the question what. Level $^ { 2 , }$ Inter vention, predicts the effects of deliberate actions, expressed as causal relationships. And Level 3, Counterfactuals, involve constructing a theory of the world that explains why certain actions have specific effects and what happens is the absence of such actions [23]. A simple and naive approach for generating counterfactual explanations is searching by trial and error. In this approach, the feature values are randomly changed for the instance of interest and stops searching when the desired output is predicted.

The counterfactual approach was proposed for the evolution of advertisement placement in search engines [24]. Johansson et al. [25] claim that counterfactual thinking has been adopted in the context of machine learning applications to predict the result of several different actions, policies, and interventions using non-experiment data. More over, the Counterfactual Gaussian Process (CGP) approach has been created by Schulam and Saria [26] for modelling the effects of sequences of actions on continuous time series data and facilitate the reliability of medical decisions [27].

Although counterfactual explanations are useful, they do not explain why a certain prediction is made. On the contrary, they assume a hy pothetical scenario where the prediction would be contrary to the output of that particular data point. Our approach aims to use a probabilistic model to provide local explanations that provide insights into the fea tures influencing a datapoint, instead of generating hypothetical sce narios to justify it.

## 3. The local interpretation-driven abstract Bayesian network framework

In this section, we present our framework built upon an extended framework of Bayesian networks that can generate post-hoc modelagnostic interpretations for a single data point of prediction: the local interpretation-driven abstract Bayesian network (LINDA). We start with a brief introduction to Bayesian networks (Section 3.1) and structure learning (Section 3.2). Readers that are familiar with the knowledge can proceed directly to the proposed framework (Sections 3.3–3.5).

## 3.1. Bayesian networks

A Bayesian Network (BN) is a directed acyclic graph (DAG) in which each node represents a random variable, and each edge represents a direct influence from the source node to the target node. The graph represents (in)dependence relationships between variables, and each node is associated with a conditional probability table that specifies a distribution over the values of the node given each possible joint assignment of the values of its parents [28].

Bayesian networks can represent essentially any full joint probability distribution, which can be computed using the chain rule in probability theory [29]. Let $\mathcal { G }$ be a BN graph over the variables $X _ { 1 } , \cdots , X _ { n }$ . We say that a probability distribution, $P r ,$ over the same space factorizes ac cording to if Pr can be expressed using the following Eq. [30]:

$$
P r (X _ {1}, \dots , X _ {n}) = \prod_ {i = 1} ^ {n} P r (X _ {i} | P a _ {X _ {i}})\tag{1}
$$

In $\operatorname { E q . } 1 , P a _ { X i }$ corresponds to all the parent variables of $X _ { i \cdot }$ The graph structure of the network, together with the associated factorization of the joint distribution allows the probability distribution to be used effectively for inference (i.e. answering queries using the distribution as our model of the world). For some query Y and some observed variable $e ,$ the exact inference in Bayesian networks is given by the following Eq. [30]:

$$
P r (Y | E = e) = \alpha P r (Y, e) = \alpha \sum_ {w \in W} P r (Y, e, w), \quad \text { with } \alpha = \frac {1}{\sum_ {y \in Y} P r (y , e)}\tag{2}
$$

Each instantiation of the expression $P r ( Y = y , e )$ can be computed by summing up all joint entries that correspond to assignments consistent with y and the evidence variable e. The set of random variables W cor responds to variables that are neither query nor evidence. The α parameter specifies the normalization factor for distribution $P r ( Y , e ) ;$ and this normalization factor is informed by certain assumptions made in Bayes rule [29].

## 3.2. Structure learning in Bayesian networks

Bayesian networks are made of two important components: a directed acyclic graph, G , representing the network structure, and a set of probability parameters, Θ, representing the conditional dependence relations. Learning a BN is a challenging problem when the network representation G is unknown. Given a dataset $\mathcal { D }$ with m observations, $P r ( \mathcal { G } , \theta | D )$ ) is composed of two steps, structure learning and parameter learning, as follows [31]:

$$
P r (\mathcal {G}, \Theta | D) = \underbrace {P r (\mathcal {G} | D)} _ {\text { structure   learning }} \cdot \underbrace {P r (\Theta | G , D) _ {\text { parameter   learning }}}\tag{3}
$$

Structure learning aims to find the directed acyclic graph $\mathcal { G }$ by maximizing $P r ( \mathcal { G } | D )$ . Parameter learning, on the other hand, focuses on estimation of the parameters Θ given the graph $\mathcal { G }$ obtained from structure learning. According to [32,33], considering that parameters Θ represent independent distributions (as assumed in Naïve Bayes), the learning process can be formalised as follows [31]:

$$
P r (\Theta | G, D) = \prod_ {i} P r (\Theta_ {X _ {i}} | \Pi_ {X _ {i}}, D)\tag{4}
$$

It is important to note that structure learning is well known to be both NP-hard [34] and NP-complete [35] due to the following equation: Pr(G |D)∝Pr(G )Pr(D |G) (5)

which can be decomposed into

$$
\begin{array}{l} P r (\mathcal {D} | G) = \int P r (\mathcal {D} | G, \Theta) P r (\Theta | G) d \Theta \\ = \prod_ {i} \int P r (X _ {i} | \Pi_ {X _ {i}}, \Theta_ {X _ {i}}) P r (\Theta_ {X _ {i}} | \Pi_ {X _ {i}}) d \Theta_ {X _ {i}} \end{array}\tag{6}
$$

In structure learning, it is often used the BIC score, a frequentist measure, to maximise, $P r ( \mathcal { G } , \theta | D )$ , due to its simplicity.

$$
\operatorname{Score} (\mathscr {G}, D) = B I C (\mathscr {G}, \theta | D) = \sum_ {i} \log \operatorname * {P r} \left(X _ {i} \mid \Pi_ {X _ {i}}, \Theta_ {X _ {i}}\right) - \frac {\log (n)}{2} \left| \Theta_ {X _ {i}} \right|\tag{7}
$$

According to Scutari et al. [31], structure learning via score max imisation is performed using general-purpose optimisation techniques. Typically heuristics adapted to take advantage of these properties to increase the speed of structure learning. The most common are greedy search strategies that employ local moves designed to affect only a few local distributions, to that new candidate DAGs can be scored without recomputing the full $P r ( { \mathcal { D } } | G )$ . This can be done either in the space of the DAGs with hill climbing and tabu search [29]. In this paper, we opted for a greedy Hill Climbing approach to learn the structure G , due to its simplicity and effective results [32].

## 3.3. Local interpretation-driven abstract Bayesian network (LINDA-BN)

State-of-the-art techniques for constructing predictive models underpinned by machine intelligence usually adopt a ‘black-box approach, where the reasoning behind the predictions remains opaque (particularly in regard to deep learning models). Consequently, the underlying predictive mechanisms remain largely incomprehensible to the decision-maker. The challenge is how to endow machine intelligence with capabilities to explain the underlying predictive mechanisms in a way that helps decision-makers understand and scrutinize the machinelearned decisions. In this section, we propose an extended framework of Bayesian Networks for generating model-agnostic local interpretations of black-box predictive models. We name this framework the Local Interpretation-Driven Abstract Bayesian Network (LINDA-BN). It supports extracting a Bayesian network as an approximation (or an abstraction) of a black-box model for a specific prediction learned from any given input. Note that explanations can be constructed from the graphical representations of LINDA-BN, and we will address the explanation generation component as a direction for future work.

The basic idea behind the proposed framework LINDA-BN rests in three main steps: i) permutation generation, ii) Bayesian network learning, and iii) computation of the Markov Blanket of the class vari able (representing the result of a prediction). The proposed model aims to augment a decision-maker’s intelligence towards a specific decision problem, providing interpretations that can either reinforce the pre dictions of the black-box or lead to a complete distrust in these pre dictions (identification of misclassifications). Fig. 1 shows a general illustration of the proposed framework.

Given an input vector of continuous features $\overrightarrow { X } = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { n } \} \in \mathbb { R } ^ { n }$ and a black-box predictor, ${ \widehat { y } } \left( { \overrightarrow { X } } \right)$ , the goal is to introduce a set of permu tations $\overrightarrow { X } _ { i } ^ { ' }$ in the features of $\overrightarrow { X }$ in a permutation variance ϵ ∈ [0,1] in such a way that each feature will be permuted using a uniform distribution over the interval $[ x _ { i } - \epsilon , x _ { i } + \epsilon ]$ . The goal is to analyse how introducing a small perturbation can impact the predictions of the black-box prediction, $\widehat { \boldsymbol { y } } \left( \overrightarrow { \mathbfit { X } } _ { i } ^ { ' } \right)$ , generating a new statistical distribution describing small varia tions of the input vector ${ \vec { X } } .$ . The goal is to learn a Bayesian network structure out of this statistical sample using a Greedy Hill Climbing approach. We used this statistical sample and passed it through the blackbox to classify it. This way, we obtained a new labelled training set from which a Bayesian network can be learned. Given that the learning process in a Bayesian network requires discrete data, it was necessary to discretise the features obtained during the permutation process into probability intervals. To achieve this, we discretised the data into quartiles of 4 bins, which specify conditional probability intervals between features. Our hypothesis is the following: if the data point falls within the correct decision region of the black-box predictor, leading to a correct class classification, $c ,$ then the predictions of all the permutations, ̂y $\hat { \cdot } \left( \overrightarrow { X } _ { i } ^ { ' } \right)$ , should be close to certainty, i.e. favouring one of the assignments of the class variable with $P r ( C l a s s = c \mid$ $X _ { i } ^ { \prime } ) \approx 1$ . This can strengthen the decision-maker's trust in the predictions of the black-box predictor. $\operatorname { I f } ,$ however, the data point, ${ \vec { X } } ,$ , is very close to the black-box’s decision boundary, then one would expect that the permuta tions will be spread around the different regions demarcated by the decision boundary, leading to more diversified statistical distributions of predictions, and a higher uncertainty in the classification of the respective class Pr(Class $= c | X _ { i } ^ { \prime } ) < < 1$ . Such situations have the potential to alert the decision-maker that the black-box predictor is not very certain about the classification of the given data point. Section 3.5 is centered in this topic.

Since the network structure shows dependencies between the input features and the class variable. then it is possible to extract what features contributed to the prediction and why, allowing a deeper understanding about the impact that the features have in the class variable, or even provide the decision-maker additional insights about the decision

![](/api/attachments/52TG4NU2/fulltext/images/bf2a3cb84eca07cc9421157f5b2ed8fcf9c70a1f14e869ff43dd379b0d10c942.jpg)  
Fig. 1. A general illustration of the proposed framework LINDA-BN.

problem.

For complex decision problems with a large number of features, the local interpretable network that is learned from the generated permu tations is extremely complicated to be analysed by a human, so a Markov Blanket is returned, instead, as a summarisation of the main variables influencing the class variable. The Markov blanket determines the boundaries of a system in a statistical sense. It is computed by deter mining the parents, the children, and the children of the parents of the class variable (the variable of interest). These correspond to the vari ables that are directly influencing the class variable.

It can be shown that a node is conditionally independent of all other nodes given values for the nodes in its Markov blanket. Hence, if a node is absent from the class attribute’s Markov blanket, its value is completely irrelevant to the classification [30]. Algorithm 1 describes the algorithm that we used to generate the proposed local interpretable abstract Bayesian network.

It is important to highlight that the proposed approach is based on probabilistic graphical models, and for that reason, it cannot fulfil the properties that are satisfied in game theory explainable algorithms, such as SHAP. So the proposed model does not meet properties such as additivity, consistency, efficiency, and dummy properties. However, it fulfils the axioms of probability theory and all the rules that derive from them. It also provides other properties that SHAP does not have, such as exploring conditional independence to determine features directly influencing the class variable. Our approach also enables its extension to a causal model, which would allow a causal analysis in terms of which features have a causal effect in the class variable (our future research direction). In SHAP, the dummy property states that a feature that does not contribute to the outcome should have a Shapley value of zero. In contrast, in the proposed model, this property is equivalent to the probability rule that the probability of an empty set is 0: Pr(∅) = 0.

## 3.4. Interpreting graphical representations through reasoning

This section analyses how to interpret the different situations where a random variable can influence another in the local interpretable Bayesian network model.

In a common cause structure, Fig. 2(a), the local interpretable model approximates to a Naïve Bayes classifier, which means that having knowledge about the class variable will make the feature variables $X _ { 1 }$ $X _ { 2 } , \cdots ,$ X conditionally independent, and consequently uncorrelated. This means that knowing about $X _ { 1 }$ does not bring any additional infor mation to the decision-maker. Although human decision-makers tend to assess and interpret these structures as cause/effect relationships as a way to simplify and linearise the decision problem due to bounded ra tionality constraints, statistically, common cause structures do not imply causal effects in Bayesian networks [28]. The consideration of the class variable as a prior in interpretations for a single datapoint may indicate a high uncertainty obtained in the statistical sample of the permuted features, suggesting that the data point that is being interpreted may be very close to the predictive black-box decision boundary (Section 3.5 addresses this with greater detail).

The other type of structure that one can often find in the local interpretable model is the v-structure, also called common effect (Fig. 2 (b), which approximates to a linear regression representation. This means that the features become conditionally independent of the class, if and only if one has knowledge about the class variable. Being uncertain about the class will lead to an influence from the features, $X _ { 1 } , X _ { 2 } , \cdots , X _ { N } .$ In terms of the proposed local interpretable model, this means that the features have a direct effect in the class variable, and humans can interpret it through an abductive reasoning process.

Abduction is a mode of human reasoning, which was brought into prominence by the American philosopher C.S. Peirce [36]. In Peirce’s view abduction is an inference of the form: “The surprising fact C is observed. But is A were true, C would be a matter of course. Hence, there is reason to suspect that A is true”. The abductive inference is thus a process of justifying an assumption, hypothesis or conjecture in pro ducing the class of interest. Peirce states that abduction might explain a given set of data, or might facilitate observationally valid predictions, or might permit the discounting of other hypotheses. By engaging in abduction, the decision maker interpreting the graph structure is afforded a simpler and more compact account [36].

Abduction is not a sound form of inference like deduction, and so even though the decision-maker might suspect A, there is a degree of uncertainty. Abduction is sometimes termed “inference to the best explanation” where there is no guaranteed certainty in the explanation. In other words, given a set of observations, the decision-maker uses abduction to find the simplest, most likely and compact explanation from the graph structure. The Markov blanket of the class variable is a way of supporting the decision maker’s abductive reasoning process.

## 3.5. Rules for local interpretations

The graphical nature of the proposed framework LINDA-BN enables the identification of certain parts that can help the decision-maker assess the reliability of the predictions of the black-box for single datapoints. To this end, we propose a set of four rules that correspond to four different patterns that the proposed model can identify, depending on how close to the decision boundary a data point is. By analysing the confidence of the interpretable model with regards to the class variable together with the structure of the network, one can provide useful guidelines to the decision-maker that can be later be used to generate human-centric and understandable explanations (which is not the focus of this work).

```txt
Algorithm 1: Local Interpretation-Driven Abstract Bayesian Network Generator
Input: local_vec, single vector from which we want to generate interpretations
black_box, a predictive model
ε, variance range to permute the features (default = 0.1)
n_samples, number of permuted samples to generate (default = 300)
class_var, string with the name of the class variable
Output: G, the Local Interpretable Abstract Bayesian Network
1: /* Generate permutations via a uniform distribution within a permutation range */
2: perms = GeneratePermutations(x, model, ε, n_samples)
3:
4: /* Discretise continuous features according to the number of quartiles */
5: perms_discr = DiscretisePermutations(perms, quartiles = 4)
6:
7: /* Learn BN from discrete permutations using a Greedy Hill Climbing Search */
8: bn = LearnBN_GreedyHillClimbing(perms_discr)
9:
10: /* Compute BN's marginal distributions */
11: bn_inf = ComputeMarginalDistributions(bn)
12:
13: /* Compute BN's Markov blanket */
14: bn_markov = ComputeMarkovBlanket(bn, class_var)
15:
16: if bn.nodes <= 10 then
17: return bn_inf /* return full network */
18: else
19: return bn_markov /* return Markov blanket */
20: end if
21:
```

The proposed rules to assess the confidence of the black-box pre dictions using the proposed framework are the following:

• Rule 1: High confidence in predictions. If the black-box predicts a class c for a given datapoint, ${ \overrightarrow { X } } ,$ and the class variable is contained in a common-effect structure in G with a probability Pr(Class = c) ≈ 1, then the interpretable model, G , supports the prediction of $\vec { X }$ and its respective Markov blanket determines the most relevant features.

As mentioned in Section $3 . 4 ,$ common-effect structures in $\mathcal { G }$ approximate to a linear regression representation in which there is a direct influence from the features to the class. When Pr(Class = c) ≈ 1, then this means that the data point falls in a well-defined decision region, as illustrated in Fig. 3. Since the likelihood of the class is close to certainty, the decision-maker can make use of the class’ respective Markov blanket for explanation and perform an abductive reasoning process in which the decision-maker will seek to find the simplest and most likely conclusion out of the Markov blanket.

• Rule 2: Unreliable predictions. If the interpretable network, G , has a structure where the class variable is independent of all other feature variables, that is Class ⊥ $\{ X _ { 1 } , \cdots , X _ { N } \}$ , then this corresponds to an unrealistic decision scenario because the features are uncorrelated from the class variable and providing information about them does not make any change in the probability Pr(Class = c). Thus, the classification ${ \widehat { y } } \left( { \overrightarrow { X } } \right)$ is incorrect, and it should be communicated to the decision-maker as an unreliable prediction.

Sometimes, due to problems in generalising the black-box predictor, there can be classifications that are erroneous and unrealistic. In these rare scenarios, the Local Interpretable model can learn from the permuted instances of ${ \overrightarrow { X } } ,$ a graphical structure in which Class ⊥ $\{ X _ { 1 } , \cdots ,$ X } (Fig. 4 shows an example). In these situations, the Markov Blanket contains only the class variable, which makes it easy to identify the independence in the class variable. Moreover, it can be easily concluded that the classification ${ \widehat { y } } \left( { \overrightarrow { X } } \right)$ is incorrect and it should be communicated to the decision-maker as an unreliable and unrealistic prediction that results from a poor generalisation of the black-box.

![](/api/attachments/52TG4NU2/fulltext/images/92a2443ba4e6316d5a6eba763660adee0bd766d719929a4d6b2f80af8f76b3ee.jpg)  
Fig. 2. Different graph structures for probabilistic reasoning.

![](/api/attachments/52TG4NU2/fulltext/images/fa2ea75a26f920380ab1ff30b5f37bc75809a5df82a24b44b7a646224307956d.jpg)

![](/api/attachments/52TG4NU2/fulltext/images/94ba7f31447c41ae4e94cb5b4d71614d3dec97cc8f7c88fa4762d26eee6189b5.jpg)  
Fig. 3. Graphical representation of a pattern representing Rule 1, a high confidence in the prediction of the black-box, supported by an interpretable graph showing what are the most relevant features influencing the class variable.

![](/api/attachments/52TG4NU2/fulltext/images/f101a98e308cbf165ed46e987ba5d24f6e747cbfd69eaa3e3930dea0a1a1f20f.jpg)  
Fig. 4. Graphical representation of a pattern representing Rule 2, a distrusted prediction of the black-box, supported by an interpretable graph showing that knowing information about the features does not make any changes in the class variable.

• Rule 3: Contrast Effects. If the black-box predicts ${ \widehat { y } } \left( { \overrightarrow { X } } \right) = c ,$ and the maximum likelihood of the class variable in ¿ is $P r ( C l a s s = { \overline { { c } } } )$ , then there is a contradiction between the local interpretable abstract model and the prediction computed by the black-box, suggesting that the datapoint is very close to the decision boundary, which can either be correctly or incorrectly classified. Thus. the decision-maker should analyse the Markov Blanket of the class variable represent ing ${ \vec { X } } ,$ and assess whether the relationships between the features justify the class.

In situations where the data point is very close to a decision boundary, the permutation of the datapoint $\vec { X }$ will generate a statistical distribution within a certain neighbourhood of X. Due to the complexity and non-linearity of the decision boundary, the statistical distribution can increase the likelihood. $P r ( C l a s s = { \overline { { c } } } )$ , contradicting the prediction of the black-box, ${ \widehat { y } } \left( { \overrightarrow { X } } \right) = c .$ . In these situations, even if the black-box managed to predict correctly X, the uncertainty is high in the predic tion, and it should be recommended to the decision-maker to assess the features of X in order to assess its reliability. Fig. 5 shows an example of a contrast effect.

• Rule 4: Uncertainty in predictions. If the black-box predicts ${ \widehat { y } } \left( { \overrightarrow { X } } \right) =$ $c ,$ and the probability of the class variable in $\mathcal { G }$ is $P r ( C l a s s = c ) < <$ 1, but still with a maximum likelihood favouring class c, then datapoint X falls near the decision boundary. Even if the class is in accordance with the prediction of the black-box, then there is an underlying uncertainty attached to its prediction. Thus, the decisionmaker should analyse the Markov Blanket of the class variable rep resenting ${ \overrightarrow { X } } ,$ and assess whether the relationships between the fea tures justify the class.

![](/api/attachments/52TG4NU2/fulltext/images/52cd78f2f58e7e559061639d0b0a6475f8502e29307dfea55770a5bf21797a66.jpg)

![](/api/attachments/52TG4NU2/fulltext/images/3cd8fc19252495e712f8f5e9fc325470ce0fdcec2b037bd611cd313dc57035e8.jpg)  
Fig. 5. Graphical representation of a pattern representing Rule 3, a contrast effect, where the local interpretable abstract model reinforces a class that is different from the one predicted by the black-box.

This situation is very similar to the contrast effect (Rule 3) with the difference that the class variable in G is still consistent with the pre dictions of $\hat { y } \left( \overrightarrow { X } \right)$ . However, the statistical distribution of the predictions of the permutations of $\vec { X }$ have high uncertainty and do not allow the decision-maker to be fully confident in the prediction of ${ \widehat { \vec { X } } } .$ . Thus, depending on the degree of uncertainty of $P r ( C l a s s = c )$ , the decision maker should analyse the Markov Blanket of the class variable repre senting ${ \vec { X } } ,$ and assess whether the relationships between the features justify the class. Fig. 6 shows an example of an uncertain prediction. Although the likelihood of the variable Class is in accordance with ${ \widehat { \vec { X } } } = { \widehat { \vec { X } } } = { \widehat { \vec { X } } } = { \widehat { \vec { X } } } = { \widehat { \vec { X } } } = { \widehat { \vec { X } } } = { \widehat { \vec { X } } } = { \widehat { \vec { X } } } = { \widehat { \vec { X } } } =$ $c ,$ the local interpretable abstract model shows full uncertainty in the prediction: the prediction is as good as flipping a coin.

## 4. Evaluation

Given that there are no standard evaluation metrics for XAI [3], in this, we present a thorough analysis of the proposed LINDA-BN model in accordance to the rules that we put forward in Section 3.5. We performed an analysis in terms of two well-known public datasets from the litera ture, namely the Pima Indians diabetes dataset and the Breast Cancer Wisconsin [37], both from the UCI Machine Learning Repository.<sup>1</sup> We have made available a public repository with Jupyter notebooks with the proposed model and all the experiments that we made for this research work: https://github.com/catarina-moreira/LINDA\_DSS.

To demonstrate the effectiveness and generalisation of the proposed model-agnostic algorithm, we applied LINDA to two different types of classifiers: (1) an interpretable model, using decision trees, and (2) an opaque model, using deep neural networks. We chose these algorithms, because they are representative white-box and a black-box algorithms in the literature [6].

In Section 4.1, we present the main experimental setup for our analysis. Section 4.2.1, presents an analysis of the impact of the per mutation variance in the proposed LINDA model. In Section 4.2.2, we make a statistical analysis of the distribution of the interpretations generated by LINDA over both datasets and the different rules together with existing interpretable approaches such as LIME [11] and SHAP [12]. Finally, Section 4.2.3, describes how the proposed interpretable model performs in more complex decision scenarios.

## 4.1. Design of experiments

In order to assess the performance and interpretations generated by the proposed LINDA model, we trained a deep learning neural network for two well-known public datasets from the literature, namely the Pima Indians diabetes dataset and the Breast Cancer Wisconsin datasets. The general information of these two datasets is summarised in Table 1.

The methodology applied to train the models was the following: given an unbalanced dataset, we randomly selected entries of the overrepresentative class in order to match the same amount of datapoints of the under-representative class. We then scaled the features between 0 and 1, and used 70% of the data to train, 15% to test the model, and 15% to validate the model during training.

## 4.2. Evaluation on a black-box model

We used a deep neural network to train the model and evaluated the model. We checked the loss and accuracy training curves and found that our model was not overfitting the data. We performed a grid search approach in order to find the best performing neural network model. The characteristics of the models can be found in Table 2. As such, the learned models apply sophisticated internal working mechanisms and run as a black-box when making predictions. We would like to highlight that the purpose of this paper is not to build state of the art black boxes, but rather train a black box model and check if we can get any additional insights about their internal mechanics using the proposed explainable algorithm.

## 4.2.1. Analysis of the impact of different permutation variances

As in other representative interpretable models in the literature (like LIME and SHAP), LINDA-BN performs permutations between an interval in the range $[ x _ { i } - \epsilon , x _ { i } + \epsilon ]$ on the input vector’s features $\begin{array} { r } { \vec { X } = \{ x _ { 1 } , x _ { 2 } , \ } \end{array}$ , x } in order to generate a statistical distribution of how the predictions of the black-box change with the features.

We have conducted a series of experiments to understand the impact of the ϵ parameter (the permutation boundary). The different experiments are represented in Fig. 7 of this document. A very small ϵ (Fig. 7 - left), will lead to a particular location, which would not allow us to find any potential classifications (rules 2, 3, and 4). If we put a very high $\epsilon ,$ then this can take over a large portion of the decision space $( { \mathrm { F i g . ~ } } 7 - { \mathrm { r i g h t } } )$ , which would lead to poor identification of true positives and true negatives. A potential acceptable indicator of a good trade-off between true positives/negatives (Rule 1) and false positives/negatives (rules 2, 3, and 4) is $\epsilon = 0 . 1$ . We also complemented this analysis by investigating the impact of ϵ for diabetes and breast cancer datasets. We performed a set of experiments, where we varied ϵ ∈ [0,1], and analysed how many times the proposed interpretable model returned a structure that is consistent with the rules proposed in Section 3.5. The obtained results are summarised in Fig. 8.

![](/api/attachments/52TG4NU2/fulltext/images/8faa48cad73c880a6e447048febd986a116df8934385a6dbbfcac0d89287eca5.jpg)

![](/api/attachments/52TG4NU2/fulltext/images/58a22cad644f00fb5a59145849e3d72e52682e11eac99113ae7c12529d00a068.jpg)  
Fig. 6. Graphical representation of a pattern representing Rule 4, uncertainty in the prediction, where the local interpretable abstract model shows that the black-box prediction is as good as flipping a coin.

Table 1  
Summary of the Diabetes and the Breast Cancer datasets.

<table><tr><td></td><td>Diabetes dataset</td><td>Breast cancer dataset</td></tr><tr><td>Dataset Size</td><td>768</td><td>569</td></tr><tr><td>Number of Features</td><td>9</td><td>30</td></tr><tr><td>Class Variable</td><td>Binary</td><td>Binary</td></tr><tr><td>Size of Positive Values</td><td>268</td><td>212</td></tr><tr><td>Size of Negative Values</td><td>500</td><td>357</td></tr><tr><td>Dataset Size After Balancing Data</td><td>536</td><td>424</td></tr></table>

Table 2  
Deep neural network architecture found for the best performing model in the Diabetes and the Breast Cancer datasets.

<table><tr><td>Parameters</td><td>Diabetes</td><td>Breast cancer</td></tr><tr><td>Model Accuracy</td><td>0.7380</td><td>0.9840</td></tr><tr><td>Num. Hidden Layers</td><td>5</td><td>4</td></tr><tr><td>Num. Neurons per Hidden Layer</td><td>12</td><td>12</td></tr><tr><td>Hidden Layer Activation function</td><td>Relu</td><td>Relu</td></tr><tr><td>Output Layer Activation function</td><td>Softmax</td><td>Softmax</td></tr></table>

Taking a close look at the Diabetes dataset in Fig. 8, results show that low variance makes the interpretable model very confident in its in terpretations, with 92% of the data points (both from the training set and test set) falling in Rule 1 (high confidence in the prediction). This is due to the fact that, for a very small permutation interval, the probability of hitting a decision boundary is very small. This is confirmed with the verification of the low amount of data points falling in Rule 4 (uncer tainty in the predictions) or Rule 3 (contrast effects). When the permu tation variance starts to increase, the model becomes less certain about the predictions. Consequently, Rule 1 starts to decrease exponentially, while Rule 4 starts to show a lot of uncertainty in the interpretations generated for the different data points. One can see that when the per mutation variance reaches half of the feature space (note that we assume that the features of the black-box are scaled between 0 and 1 as in standard machine learning applications), then there comes the point where the uncertainty is so high that the interpretable model stops having confidence in almost 90% of its interpretations. Additionally, almost 80% of the data points start falling in Rule 4.

In terms of the impact of the permutation variance for the breast cancer dataset, the scenario tends to be slightly different. Just like in the diabetes dataset, when the permutation variance interval is very small, the statistical distribution of the predictions learned by the proposed LINDA model majorly falls in Rule 1. However, when the permutation variance starts to increase together with the uncertainty levels, we start to notice an increase of contrast effects (Rule 3), rather than uncertainty in the predictions (Rule 4). The reason for this is due to the effectiveness of the black-box. Note that the accuracy of the deep neural network model for the diabetes dataset was $7 3 . 8 0 \% ,$ while the learned model for the breast cancer dataset achieved an accuracy of 98.40%. Since the majority of the data points fall in well-defined decision regions, when the permutation variance increases, the statistical distribution of predictions will tend to show misclassifications (a statistical distribution more concentrated in the opposite region of the decision boundary). Fig. 8 also shows that permutation variances superior to 0.2 do not decrease the certainty of the interpretability of correctly predicted datapoints. How ever it does increase the number of contrast effects (Rule 3), reinforcing again the idea that bigger permutation intervals will make the distribu tions point towards opposite directions of the decision boundary.

In order to extract interpretable models that are both highly confi dent in the interpretations, but can also flag possible misclassifications, we decided to set the permutation variance to 0.1 for the remaining parts of this analysis. Note that in our available public framework, the user is free to change this parameter, but as default, we consider it to be 0.1.

## 4.2.2. Analysis of rules for local interpretations

In this section, we analyse the impact of the proposed rules in the different classifications: true positives, true negatives, false positives, and false negatives. The goal with this analysis is to understand if the proposed rules can provide the decision-maker with some insights on whether or not, the decision-maker is facing a correct classification or a possible misclassification. Table 3 shows the percentage of data points over the different proposed rules for both diabetes and breast cancer datasets, using ϵ = 0.1.

Decision Support Systems xxx (xxxx) xxx

![](/api/attachments/52TG4NU2/fulltext/images/68b37ba1cd3f9ec4c5eed3c7d8826e1034e4393e3cc06a787e8f9487526915c2.jpg)  
Fig. 7. Impact of the permutation variance boundary ϵ.

![](/api/attachments/52TG4NU2/fulltext/images/7295c51ebd2aeb36d5aa3f7ca50903a39995b843bdd5f88b455b99da85ce12f6.jpg)

![](/api/attachments/52TG4NU2/fulltext/images/e3e2b243d86c94cb31eb2d8e8d698c294c6339020a795324d8e215f1b8b2702a.jpg)  
Fig. 8. Impact of the permutation variance boundary in the different proposed rules.

• Correct classifications majorly coincide with Rule 1, leading to highly confident predictions. For the breast cancer dataset, for instance, all data points classified as true positives and true negatives were categorised as Rule 1 with high confident interpretations. For the diabetes dataset, since the black-box had a poorer performance, then the percentage of correctly classified datapoints is already smaller. Still, 86% of the true positives in the training set fell under the category of Rule 1 and in the test set 75%. Regarding the true negatives, more than 90% of the data points had interpretations supporting a true classification of a non-diabetes case. When compared with interpretations from the state-of-the-art algorithms, one can see that both LIME and SHAP also tend to reinforce the features that are contributing positively to class diabetes. Fig. 9 shows an example of an interpretation of a correctly classified datapoint (ϵ = 0.1) and the respective interpretations for LIME and SHAP. For the case of misclassifications, there was a significant amount of datapoints belonging to the set of false positives and the false negatives that were also categorised as Rule 1. In these exam ples, the interpretable model could not provide significant insights into why there was a misclassification.

An example of how to interpret the graphical model in Fig. 9 is, for instance, like the report presented in Fig. 10, which can be found in the publicly available repository. The reader should note that the focus of this paper is on developing an interpretable model, that is, a framework that provides algorithms with the ability to extract symbolic information out of the black-box. The automatic generation of human-centric un derstandable explanations out of interpretable models is part of an explainability module, which we plan to explore in future work.

• Nonexistence of Rule 2. As illustrated in Fig. 8, Rule 2, which cor responds to the cases where the class variable is independent of the

Table 3  
Overview of the distribution of the datapoints for the Diabetes and Breast Cancer datasets over the proposed rules using LINDA in order to determine the confidence of the computed interpretations using a deep neural network (black-box model) as the classifier.

<table><tr><td colspan="2"></td><td colspan="4">Diabetes</td><td colspan="4">Breast cancer</td></tr><tr><td>Rules</td><td>Set</td><td>TP</td><td>TN</td><td>FP</td><td>FN</td><td>TP</td><td>TN</td><td>FP</td><td>FN</td></tr><tr><td rowspan="2">Rule 1</td><td>Train</td><td>0.8662</td><td>0.91</td><td>0.7627</td><td>0.7419</td><td>0.9931</td><td>0.8786</td><td>1.0000</td><td>0.1667</td></tr><tr><td>Test</td><td>0.7576</td><td>0.96</td><td>0.57</td><td>0.8571</td><td>1.0000</td><td>0.8286</td><td>1.0000</td><td>0.0000</td></tr><tr><td rowspan="2">Rule 2</td><td>Train</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>Test</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td rowspan="2">Rule 3</td><td>Train</td><td>0.0828</td><td>0.016</td><td>0.1186</td><td>0.0645</td><td>0.0000</td><td>0.0643</td><td>0.0000</td><td>0.6667</td></tr><tr><td>Test</td><td>0.1818</td><td>0.0000</td><td>0.14</td><td>0.0000</td><td>0.0000</td><td>0.1143</td><td>0.0000</td><td>0.0000</td></tr><tr><td rowspan="2">Rule 4</td><td>Train</td><td>0.0509</td><td>0.0787</td><td>0.1186</td><td>0.1935</td><td>0.0069</td><td>0.0571</td><td>0.0000</td><td>0.1667</td></tr><tr><td>Test</td><td>0.0606</td><td>0.04</td><td>0.29</td><td>0.1429</td><td>0.0000</td><td>0.0571</td><td>0.0000</td><td>0.0000</td></tr></table>

Decision Support Systems xxx (xxxx) xxx  
![](/api/attachments/52TG4NU2/fulltext/images/3d714c6b9090bef7a3045a359610488a5c55cea9a611bb900d49daddaba77f4b.jpg)  
Fig. 9. Correct prediction high confidence (a true positive).

## REPORT

Knowing about the patient's Glucose levels makes SkinThickness, Insulin, BMl, Age and DiabetesPedigreeFunction NOT RELEVANT to assessDiabetes.

The features CONTRIBUTING for Diabetesare BloodPressure and Pregnancies.

Recommendation: Given the confidence of the explanation (100%), the model is certain that the patient has Diabetes

Fig. 10. Example of a report that could be generated to explain the interpretable model in Fig. 9.

features, is extremely rare. This rule only starts to emerge for per mutations superior to 0.2 in the diabetes dataset, and are nonexistent in the cancer dataset. This suggests that permutation vari ances of 0.1 do not point towards unrealistic and erroneous classi fications. Fig. 11 shows an example of an unreliable prediction that was found in the test set of the diabetes dataset, using a variance of ε = 0.25 and the respective LIME and SHAP interpretations. Note that this specific data point corresponds to a misclassification (a false positive).

• Contrast effects, Rule 3, majorly coincide with misclassifications. When a datapoint falls very close to the decision boundary, then when permuting that datapoint, there can be a significant statistical distribution of the predictions falling on the region of the decision boundary of the opposite class. According to the analysis in Table 3, in the Diabetes dataset, Rule 3 majorly occurred in the set of falsepositive points, that is datapoints that were misclassified. But there is also a significant percentage of data points in the set of true pos itives. Although these points were correctly classified, the contrast effect that is captured by the proposed interpretable model might indicate that these are cases correctly classified near the decision boundary. Thus, the decision-maker should be aware that although there was a correct classification, this classification might not have occurred due to the appropriate input feature values. Fig. 12 shows an example of a Rule 3 in the Diabetes dataset for ϵ = 0.1. When comparing with LIME and SHAP, one can notice that it is not very clear that this datapoint represents a misclassification.

![](/api/attachments/52TG4NU2/fulltext/images/db59d06cbc2f79f7510b481b71f02b55b3f53befb7e6f8df234f1be4de414a3f.jpg)  
Fig. 11. Misclassification in accordance with Rule 2, an unreliable prediction (a false positive).

• Uncertainty in predictions, Rule 4, majorly coincides with mis classifications. In the experiments that were performed, using ϵ = 0.1, Table 3 shows that the data points showing higher uncertainty in the likelihood of the class variable are mostly present in the sets of the false positives and the false negatives. In other words, in the set of misclassified data points. This is more noticeable in the diabetes dataset, in which the black-box predictor achieves an average accu racy of 73.8% where there are more misclassified data points. On the other hand, when one looks at the breast cancer dataset since there were almost no misclassified data points (accuracy of 0.9840), the percentage of data points falling in Rule 4 are nearly zero. Fig. 13 illustrates an example of a false positive data point, in which the interpretable model show maximum uncertainty in the class variable node. In terms of LIME and SHAP, it is hard to identify any principles that could point the decision-maker about a possible misclassification. In other words, the rules proposed in this work have the potential to guide the user in identifying misclassifications. For instance, in Rule 2 (Fig. 11), we find a graphical structure where the class variable is independent of the features, then this is an indication that the black box was unable to classify this datapoint correctly, and there is the potential that this data point represents a misclassification.

Note that evaluation in explainable AI algorithms is still an open research question. Approaches are still being proposed in the literature, and for that reason, there is still not a standard approach for this [38]. The evaluation that we attempted to do in this study was with respect to the rules four rules that we proposed and their consistency. For instance, we found Rule 1 (full confidence in the explanation) to be the dominant rule in both true positives and true negatives. We found rules 3 and 4 to significantly occur in false positives and false negatives. We also found rare occurrences of Rule 2 in this last subgroup of data as well. Rules 2–4 can indicate a potential misclassification to the user, which is something unique and novel in the literature of XAI. Regarding the possibility of using decision trees, the main disadvantage of using these models is because they grow exponentially large and they become very difficult to understand at a human level. In fact, Bayesian networks approximate to decision-trees in terms of information with the advantage of providing a more compact model.

In the next section, we describe how more complex decision prob lems are addressed by the proposed interpretable model.

## 4.2.3. Interpretations for complex decision scenarios

For small decision problems (at most ten random variables), the proposed LINDA model displays the full interpretable network. For more complex decision problems, however, this would become unreadable for a human decision-maker. The breast cancer dataset is an example of such a complex decision problem that contains a set of thirty features, which are mapped into random variables. This results in a graphical structure too complex for any human to analyse. For such datasets, the proposed LINDA model provides the decision-maker with a Markov Blanket of the variable of interest, instead of the full local interpretable Bayesian network, together with information about in which rule the network pattern corresponds to and respective marginal probabilities.

This representation enables the summarisation of information, enabling a fast and compact data-driven interpretation of a local data point. Fig. 14 shows an example of an interpretable network that was extracted out of a true positive data point. The complexity of the network does not enable any human interpretations to take place. However, when looking at the Markov blanket together with the mar ginal probabilities of the random variables, then one can clearly identify a common-effect structure in which six features directly influence the class variable and contribute to its value. Moreover, the statistical dis tribution of the permutations shows full confidence in the diagnosis, suggesting that the data point falls within Rule 1, and consequently, there is high confidence that it is a correct prediction. The depth of this Markov blanket can potentially be extended to different depths, depending on the decision-maker’s needs (for example, a non-expert decision-maker would be satisfied with the Markov blanket in Fig. 14. However a medical doctor would probability explore other depths and

![](/api/attachments/52TG4NU2/fulltext/images/4791f1a172dcacb1cbf3e1c184ca6aa9ff8d3ae352b2441fe3f989ca1159948b.jpg)  
Fig. 12. Misclassification in accordance with Rule 3, a contrast effect.

![](/api/attachments/52TG4NU2/fulltext/images/a918aca103e57ec6f68e8e47279b84a7b4a7a3af0dd60224df131bb7c82474cd.jpg)  
Fig. 13. Correct classification in accordance with Rule 4, uncertainty in predictions (true positive).

![](/api/attachments/52TG4NU2/fulltext/images/e0602f8cae0197970bba769fb1fb2813dabc96683c08490e96362e90dfe7995b.jpg)  
Fig. 14. Markov blanket representation of a local interpretable Bayesian network with 30 nodes for the breast cancer dataset. The Markov blanket is in accordance with Rule 1 and represents a correct classification.

analyse the relationship between more variables and their indirect in fluences towards the class variable).

## 4.3. Evaluation on a white-box interpretable model

The proposed method is meant for interpreting black-box models. But since it is model-agnostic, it can also be applied to white-box models. In this section, we apply LINDA-BN to a Decision Tree classifier, which is a representative white-box interpretable model. We trained a decision tree for both diabetes and breast cancer datasets. The overall accuracy of the model for the diabetes dataset was 60% and for the breast cancer data was 94%. Given that the resulting tree was too complex for a human user to analyse, for each data instance that we wanted to generate ex planations, we extracted the decision tree path from the root node until the decision leaf node. Similarly to the previous experiments, we ana lysed the impact of the four rules that we proposed in terms of true positives, false positives, true negatives and false negatives. Table 4 shows the obtained results.

Table 4 indicates that the Bayesian network approximates to the decision tree as highlighted in previous research [39]. For the diabetes dataset. one can see that in the true positives. LINDA-BN was able to show high confidence (Rule 1) on approximately 84% of the datapoints in the test set and 77% in the training set. Only 13% of the true positive instances were assigned to rule 3 and only 8% to rule 4. This suggests that the algorithm performs very well, and only a very small portion of the datapoints were near the decision boundary. Similar conclusions can be taken for the Cancer dataset and for the true negative instances. When ever the algorithm makes a correct classification, LINDA-BN is able to represent the majority of the datapoints as rule 1 with a high confidence in the results. Fig. 15 shows an example of a true positive and a true negative classified by a decision tree and explained by the LINDA-BN.

Table 4 also indicates that a significant amount of datapoints clas sified as false positives or false negatives fall in either rules 3 or 4, which may suggest a misclassification. Taking a closer look at the diabetes dataset, one can see that for the majority of the false positive datapoints in the test set. the explanation model was highly confident in the prediction, although the datapoints were misclassified. In this case, the user could not get any additional insights about the correctness of the results. However, if one looks at the false negatives, one can already see that the vast majority of these datapoints fall in rules 3 and 4, suggesting a misclassification.

Table 4  
Overview of the distribution of the datapoints for the Diabetes and Breast Cancer datasets over the proposed rules using LINDA in order to determine the confidence of the computed interpretations using a decision tree (white-box model) as the classifier.

<table><tr><td colspan="2"></td><td colspan="4">Diabetes</td><td colspan="4">Breast cancer</td></tr><tr><td>Rules</td><td>Set</td><td>TP</td><td>TN</td><td>FP</td><td>FN</td><td>TP</td><td>TN</td><td>FP</td><td>FN</td></tr><tr><td rowspan="2">Rule 1</td><td>Train</td><td>0.7766</td><td>0.4140</td><td>0.0000</td><td>0.0000</td><td>0.9603</td><td>0.6042</td><td>0.0000</td><td>0.0000</td></tr><tr><td>Test</td><td>0.8400</td><td>0.5769</td><td>0.7857</td><td>0.06666</td><td>0.9583</td><td>0.7941</td><td>1.0000</td><td>0.0000</td></tr><tr><td rowspan="2">Rule 2</td><td>Train</td><td>0.0106</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>Test</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td rowspan="2">Rule 3</td><td>Train</td><td>0.1330</td><td>0.5000</td><td>0.0000</td><td>0.0000</td><td>0.0066</td><td>0.2291</td><td>0.0000</td><td>0.0000</td></tr><tr><td>Test</td><td>0.0800</td><td>0.3846</td><td>0.2143</td><td>0.5333</td><td>0.0000</td><td>0.1470</td><td>0.0000</td><td>0.6667</td></tr><tr><td rowspan="2">Rule 4</td><td>Train</td><td>0.0800</td><td>0.0860</td><td>0.0000</td><td>0.0000</td><td>0.0331</td><td>0.1667</td><td>0.0000</td><td>0.0000</td></tr><tr><td>Test</td><td>0.0800</td><td>0.0385</td><td>0.0000</td><td>0.4000</td><td>0.04166</td><td>0.0588</td><td>0.0000</td><td>0.3333</td></tr></table>

![](/api/attachments/52TG4NU2/fulltext/images/acc5b0a53bc0d501bd55c46a3dfc93f24c423a077e6c72f5e5ea66f59e283650.jpg)  
Fig. 15. Example of explanation for a correct classifications in a true positive (TP) and a true negative (TN) instance using a decision tree (white-box model) and the proposed LINDA-BN. The generated explanations fell both on Rule 1, which indicates a high confidence in the prediction of the white-box model.

To summarise, the proposed LINDA-BN can provide some guidance to the user if there is a high or low confidence in the predictions, but it does not mean that is can always detect potential misclassifications. Experiments shows that in a significant amount of examples, there is the potential to detect possible miclassifications. Fig. 16 shows an example of a true positive and a true negative classified by a decision tree and explained by the LINDA-BN.

## 5. Comparison with LIME and SHAP

In this section, we provide a deeper discussion between the main differences of the proposed approach and current state-of-the-art algo rithms, such as LIME and SHAP. The main advantages of the proposed model can be summarised as follows:

• Instead of individual feature importance, the proposed approach presents features that are conditionally dependent between each other and that are directly influencing the class variable. This prop erty is very important, especially in deep neural networks. When in dependent features pass through the first hidden layer of a deep neural network, the features are no longer independent between each other, but they become correlated. For this reason, the more hidden layers the network has, the more the learning algorithm tends to overfit. For this reason, we argue that local explanations should not be computed in terms of individual weights of features, but rather as features influencing each other. When compared to the current stateof-the-art algorithms, LIME computes weights of individual features that positively/negatively contribute to a certain prediction. In contrast, SHAP computes the individual feature’s Shapley values. SHAP also allows the user to explore different plots to get better un derstandings about the impacts of each features in the prediction. However. both LIME and SHAP do not show any understanding of how these features depend on and/or correlate with each other.

![](/api/attachments/52TG4NU2/fulltext/images/50e040dc9eb7f934645f8e55c6db1be534bf1eeb2a6a583fc7927fde23b7432b.jpg)  
Fig. 16. Example of explanation for an misclassification in false positive (FP) and a false negative (FN) instance using a decision tree (white-box model) and the proposed LINDA-BN. The generated explanations both fell on Rule 3, which indicates a low confidence on the predictions.

• The proposed model enables the establishment of four different rules that can provide guidance to the decision-maker on when to trust a prediction from the black-box based on the structure of the local probabilistic graphical model that was learned. These rules cannot be easily mapped into approaches such as LIME and SHAP.

• The local probabilistic graphical model can provide the foundation for causal analysis and the first building block for approaches that propose causability [8], that is, approaches that provide the decisionmaker with a causal understanding of why a certain prediction was computed.

## This proposed model also has several limitations:

• Stability of the explanations is comparable to LIME since the way the local features are permuted is similar to that algorithm. This means running the proposed model with different structure learning algo rithms (different from the Greedy Hill-Climbing algorithm) may lead to different graphical structures and consequently, different in terpretations. SHAP, on the other hand, guarantees a unique expla nation, because it satisfies a set of properties to compute a fair distribution of contributions for each of feature through Shapley values.

• The performance of our method decreases exponentially with the number of features. This is also true for LIME and SHAP: for very big feature spaces, the algorithm’s performance is very poor. For the specific case of the proposed approach, learning a Bayesian network structure from a complete dataset is NP-Hard, and consequently time consuming.

## 6. Conclusions

In this paper, we proposed a new post-hoc interpretable framework, the Local Interpretation-Driven Abstract Bayesian Network (LINDA-BN). This framework consists of learning a Bayesian network as an approxi mation of a black-box model from a statistical distribution of predictions from a local datapoint.

The major contribution of the proposed framework is the ability to identify four different rules which can inform the decision-maker about the confidence level in a given prediction of a specific data point. As such, the interpretations provided in our approach can help the decisionmaker assess the reliability of predictions learned by a black-box model. These rules correspond to the different patterns that can be found in the learned Bayesian network, and they are summarised as follows:

• Rule 1 - High confidence in predictions: a common-effect structure in which the features are directly influencing the class, and the maximum likelihood of the class is close to one, suggesting a correct classification

• Rule 2 - Unreliable predictions: when the class variable is indepen dent of the features, then the explanation suggests a misclassification.

• Rule 3 - Contrast Effects: when the maximum likelihood of the class variable in the learned Bayesian network favours a class opposite to the black-box model, suggesting a misclassification.

• Rule 4 - Uncertainty in the predictions: when the likelihood of the class variable has very high levels of uncertainty, suggesting that the decision-maker should assess the network in order to understand if the features are supporting the class.

Experimental findings showed that rules 3 and 4 usually occurred in sets of false positives and false negatives, suggesting that the proposed framework might provide a possible approach to identify mis classifications in black-box models. On the other hand, the correct classifications (true positives and true negatives), were mostly associated with Rule 1 with common-effect graph structures and maximum likeli hood in the class variable close to one, again providing a potential method to identify correct classifications and promote trust in the decision-maker.

The proposed model also works for multiclass classification. Regarding image data (and text data), the proposed model would work in a similar way as LIME where image segmentation techniques could potentially be used to enhance the superpixels selection and to allow for the removal of certain superpixels as a permutation mechanism. This will be part of the next steps for our research.

For future work, we would like to extend the proposed approach from an interpretable framework to an explainable one. A key, open challenge along this direction is to convert the symbolic rules proposed in this study into explainable arguments that could be used to directly communicate with the decision-maker regarding why a certain prediction was computed out of a black-box and the reasons of why/why not a decision-maker should trust in the predictions. Another action item for future work is to extend the evaluation of LINDA-BN to real-life, more complex datasets (e.g., event logs recorded in enterprise information systems that capture the execution of business processes in modern organisations [40]).

## References

[1] W.J. Murdoch, C. Singh, K. Kumbier, R. Abbasi-Asl, B. Yu, Interpretable machine learning: definitions, methods. and applications. Proceedings of the Nationa Academy of Sciences 116 (2019), https://doi.org/10.1073/pnas.1900654116.

[2] Q.V. Liao, D.M. Gruen, S. Miller, Questioning the AI: informing design practices for explainable AI user experiences, Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems (2020) 1–15, https://doi.org/10.1145 3313831.3376590. abs/2001.02478.

[3] R. Guidotti, et al., A survey of methods for explaining black-box models, ACM Comput. Surv. 51 (2018) 93:1–93:42.

[4] H. Lakkaraju, et al., Faithful and customizable explanations of black-box models, in: Proceedings of the 2019 AAAI Conference on AIES 2019, 2019, pp. 131–138.

[5] Z.C. Lipton. The mythos of model interpretability. CACM 61 (2018) 36–43

[6] C. Molnar, Interpretable Machine Learning: A Guide for Making Black-Box Models Explainable. Leanpub. 2020

[7] F. Doshi-Velez, B. Kim, Towards a rigorous science of interpretable machine learning, arxiv (2017), 1702.08608

[8] A. Holzinger, G. Langs, H. Denk, K. Zatloukal, H. Müller, Causability and explainability of artificial intelligence in medicine, Wiley Interdisciplinary Rev.: Data Min. Knowl. Discov. 9 (2019), e1312.

[9] M. Siering, A.V. Deokar, C. Janze, Disentangling consumer recommendations: explaining and predicting airline recommendations based on online reviews, Decis. Support. Syst. 107 (2018) 52–63.

[10] B. Kim, J. Park, J. Suh, Transparency and accountability in ai decision support: explaining and visualizing convolutional neural networks for text information. Decis, Support, Syst. 134 (2020) 113302.

[11] M.T. Ribeiro, S. Singh, C. Guestrin, “Why should I trust you?”: explaining th predictions of any classifier, in: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016 pp. 1135–1144.

[12] S. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, in: Proceedings of the 31st Annual Conference on Neural Information Processing Systems (NIPS), 2017.

[13] M.A.-M. Radwa Elshawi, Youssef Sherif, S. Sakr, Interpretability in healthcare a comparative study of local machine learning interpretability techniques, in: Proceedings of IEEE Symposium on Computer-Based Medical Systems (CBMS), 2019.

[14] M. Stiffler, A. Hudler, E. Lee, D. Braines, D. Mott, D. Harborne, An analysis of the reliability of lime with deep learning models, in: Proceedings of the Dstributed Analytics and Information Science International Technology Alliance, 2018.

[15] H.F. Tan, K. Song, M. Udell, Y. Sun, Y. Zhang, Why Should you Trust my Interpretation? Understanding Uncertainty in Lime Predictions, 2019.

[16] M.T. Ribeiro, S. Singh, C. Guestrin, Anchors: high-precision model-agnostic explanations, in: Proceedings of the 32nd AAAI International Conference on Artificial Intelligence, 2018.

[17] L.S. Shapley, A Value for n-Person Games, Rand coporation, 1952, 15.

[18] E. Strumbelj, I. Kononenko, Explaining prediction models and individual

[19] A.C. Miller Janny Ariza-Garzon, ´ Javier Arroyo, M.-J. Segovia-Vargas, Explainability of a machine learning granting scoring model in peer-to-peer lending, in: Proceedings of IEEE Access, 2020.

[20] A.B. Parsa, A. Movahedi, H. Taghipour, S. Derrible. A. (Kouros)Mohammadian Toward safer highways, application of xgboost and shap for real-time accident detection and feature analysis Accid Anal, Prey, 136 (2020) 105405

[21] S. Wachter, B. Mittelstadt, C. Russell, Counterfactual Explanations without Opening the Black-Box: Automated Decisions and the Gdpr, 2018.

[22] C.T. Ramaravind, K. Mothilal, Amit Sharma, Examples are not enough, learn to criticize! criticism for interpretability, in: Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency, 2020.

[23] J. Pearl, The seven tools of causal inference, with reflections on machine learning, Commun. ACM 62 (2019) 7.

[24] L. Bottou, J. Peters, J. Quinonero-Candela, ˜ D.X. Charles, D.M. Chickering, E. Portugaly, D. Ray, P. Simard, E. Snelson, Counterfactual reasoning and learning systems: the example of computational advertising, J. Mach. Learn. Res. 14 (2013) 3207-3260.

[25] F.D. Johansson, U. Shalit, D. Sontag, Learning Representations for Counterfactual Inference, 2016.

[26] P. Schulam, S. Saria, Reliable Decision Support Using Counterfactual Models, 2017.

[27] E.C. Neto, Towards Causality-Aware Predictions in Static Machine Learning Tasks: The Linear Structural Causal Model Case, 2020.

[28] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann Publishers, 1988

[29] S. Russel, P. Norvig, Artificial Intelligence: A Modern Approach, Pearson Education, 3rd edition, 2010.

[30] D. Koller, N. Friedman, Probabilistic Graphical Models: Principles and Techniques, The MIT Press, 2009.

[31] M. Scutari, C. Vitolo, A. Tucker, Learning bayesian networks from big data with greedy search: computational complexity and efficient implementation, Stat. Comput. 29 (2019) 1095–1108.

[32] D. Heckerman, D. Geiger, D. Maxwell, Learning bayesian networks: the combination of knowledge and statistical data, Mach. Learn. 20 (1995) 197–243.

[33] D. Heckerman, A Tutorial on Learning With Bayesian Networks, Technical Report, Microsoft Research Advanced Technology Division, Microsoft Corporation, 1995.

[34] D.M. Chickering, D. Heckerman, Learning Bayesian Networks is NP-Hard, Technical Report, Tech. Rep. MSR-TR-94-17. Microsoft Corporation. 1994.

[35] D.M. Chickering, Learning Bayesian Networks is NP-Complete, Springer New York, 1996, pp. 121–130.

[36] D. Gabbay, J. Woods, Advice on abductive logic, Logic J. IGPL 14 (2006) 189–219.

[37] S. Piri, D. Delen, T. Liu, A synthetic informative minority over-sampling (simo) algorithm leveraging support vector machine to enhance learning from imbalanced datasets, Decis. Support. Syst. 106 (2018) 15–29.

[38] S. Mohseni, N. Zarei, A multidisciplinary survey and framework for design and evaluation of explainable ai systems, arxiv (2020) 1–45, cs.HC/1811.11839.

[39] M. Hunt, B. von Konsky, S. Venkatesh, P. Petros, Bayesian networks and decision trees in the diagnosis of female urinary incontinence, in: Proceedings of the 22nd Annual International Conference of the IEEE Engineering in Medicine and Biology Society. 2000

[40] R. Sindhgatta, C. Ouyang, C. Moreira, Exploring interpretability for predictive process analytics. in: Proceedings of the 18th International Conference on Service Oriented Computing (ICSOC), 2000.

Dr Catarina Moreira is a lecturer in the School of Information Systems at Queensland University of Technology. She is a pioneer in the development of non-classic probabilistic graphical models for cognition and decision-making. Her work also comprises machine learning/deep learning models, multi-modal image data fusion techniques for medical decision-making and innovative human interactive probabilistic models for explainabl AI.

Mr Yu-Liang Chou is a PhD student in the School of Information System at the Queensland University of Technology. His research interests focus on the causality in explainable artificial intelligence. In the prior years, he has gained experience from a research project in text mining for sentiment analysis and GPS transmission protocol optimization

Miss Mythrevi Velmurugan is currently a PhD candidate in the School of Informatior Systems at the Oueensland University of Technology, researching the use of AI explain ability in predictive process analytics.

Dr Chun Ouvang is a senior lecturer in the School of Information Systems at Oueensland University of Technology. Her PhD focused on system modelling and verification using nets. In the last decade, she has developed strong research interests in and contributed to the areas of data-driven process analytics, process automation, and recently explainable predictive analytics.

Dr Renuka Sindhgatta is a lecturer in the School of Information Systems at the Queensland University of Technology. Her PhD focused on building predictive models for business processes with the operational data. She has contributed to topics on process mining and data analytics, including explainable machine learning for business processes.

Prof Peter Bruza is a professor in the School of Information Systems at the Queensland University of Technology. His research spans cognitive science, applied logic and infor mation retrieval. He is a pioneer of the field of quantum cognition which aims to develop a new genre of models of the human cognition using the formalism of quantum theory.
