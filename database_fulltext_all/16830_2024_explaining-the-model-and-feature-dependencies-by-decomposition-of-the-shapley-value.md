---
otero_id: 16830
otero_key: "YJ2D98Y2"
title: "Explaining the model and feature dependencies by decomposition of the Shapley value"
authors: "Joran Michiels; Johan Suykens; Maarten De Vos"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2024.114234"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Explaining the Model and Feature Dependencies by Decomposition of the Shapley Value

Joran Michiels<sup>a,∗</sup>, Johan Suykens<sup>a</sup>, Maarten De Vos<sup>a,b</sup>

<sup>a</sup>Stadius group in the Department of Electrical Engineering, KU Leuven University, Kasteelpark Arenberg 10, 3001, Leuven, Belgium <sup>b</sup>Department of Development and Regeneration, KU Leuven University, Herestraat 49, 3000, Leuven, Belgium

## Abstract

Shapley values have become one of the go-to methods to explain complex models to end-users. They provide a model agnostic post-hoc explanation with foundations in game theory: what is the worth of a player (in machine learning, a feature value) in the objective function (the output of the complex machine learning model). One downside is that they always require outputs of the model when some features are missing. These are usually computed by taking the expectation over the missing features. This however introduces a non-trivial choice: do we condition on the unknown features or not? In this paper we examine this question and claim that they represent two diferent explanations which are valid for diferent end-users: one that explains the model and one that explains the model combined with the feature dependencies in the data. We propose a new algorithmic approach to combine both explanations, removing the burden of choice and enhancing the explanatory power of Shapley values, and show that it achieves intuitive results on simple problems. We apply our method to two real-world datasets and discuss the explanations. Finally, we demonstrate how our method is either equivalent or superior to state-to-of-art Shapley value implementations while simultaneously allowing for increased insight into the model-data structure.

Keywords: Explainable AI, Feature attribution, End-user, Shapley value, Black box, Feature dependencies

## 1. Introduction

Black box machine learning methods have shown remarkable results on complex prediction tasks in the past years. Widespread adoption in practical settings is limited however. This is believed to be partly due to the lack of insights in the model’s inner workings, making validating the model very dificult. A popular choice to gain insight in the model’s decisions are model agnostic local post-hoc explanations. These explain one sample (local) and its corresponding prediction by sampling any (model agnostic) already trained model (post-hoc).

One local post-hoc explanation, the SHapley Additive exPlanation (SHAP) [17], has become increasingly popular in the last few years. Apart from its excellent Python module, this is likely due to the solid game-theoretic background of the method: other than the degree of approximation, nothing is left to the choice of the user, or so it seems. As has been recently noticed in related literature [11, 14, 26] the game-theoretic concept does not translate literally to machine learning models, leading to interpretation problems when features are dependent. It should be noted that similar problems can arise in other posthoc explanations such as LIME [20]. They are however not covered in related papers (nor in our work). This is likely because uniqueness is one of the main selling points of SHAP, unlike other explanation methods.

In our opinion, central to the understanding of these interpretation problems is the distinction between the model and the result (the model combined with the data), and the corresponding explanations. We qualitatively argue that diferent settings can have diferent requirements for local post-hoc explanations with a simple example (inspired by [11] and [26]). Assume the following risk model $f _ { r }$ and dependent features:

$$
\begin{array}{l} f _ {r} ([ X _ {1}, X _ {2} ]) = X _ {1} \\ X _ {1}, X _ {2} \quad \text { binary } \\ X _ {1} \not \perp X _ {2} \end{array}\tag{1}
$$

Let us imagine two diferent fictive settings with diferent feature definitions in Table 1. Although the assumed data

Table 1: Diferent settings with diferent features

<table><tr><td></td><td> $X_1$ </td><td> $X_2$ </td><td> $f_r(\cdot)$ </td></tr><tr><td>court</td><td>recidivist</td><td>race</td><td>future recidivism</td></tr><tr><td>hospital</td><td>high HR</td><td>obesity</td><td>heart attack</td></tr></table>

distribution is simplified, it is known that for both settings the features tend to be associated [15, 21]. Given a certain sample, with SHAP we can explain its output by determining what efect every feature value has towards the output. In the first setting $f _ { r }$ is an indicator for recidivism of a convict. By Article 6 of the European Court of Human Rights, a convict x can demand an explanation of the algorithm involved in the courts decision. In this case the explanation should attribute $f _ { r } ( [ { \pmb x } _ { 1 } , { \pmb x } _ { 2 } ] )$ ) completely to $\mathbf { x } _ { 1 } .$ , showing the absence of racial bias in the model. The second setting needs a diferent explanation. For patient x with a high heart attack risk, a good explanation should arguably attribute part of $f _ { r } ( [ { \pmb x } _ { 1 } , { \pmb x } _ { 2 } ] )$ to ${ \mathbf { { x } } } _ { 2 } ,$ , since changing $\mathbf { x } _ { 2 }$ by losing weight could decrease the heart rate (HR), which in term reduces the odds of having a heart attack according to the model. Note that this last attribution is solely due to the dependency in the data.

Thus, although the model and data distribution are the same, diferent settings seem to require diferent kinds of explanations. The first explanation explains the model while the second tries to explain the model combined with the data, which we call the actual result. Preferably, a good method should account for both settings. In this paper, we show that a SHAP value for a feature can be split up into a direct (model corresponding) attribution and an attribution via other dependent features, allowing the end-user (e.g. convict or patient) to easily grasp the explanation of both the model and the result. Specifically, the contributions of this paper are:

• identification of the aforementioned distinction between explaining the model and explaining the result,

• an interpretation of a previously noticed decomposition [10] as a unification of the two most common Shapley value implementations [1, 11],

• a new model-agnostic implementation of Shapley values with accompanying plots that provide enhanced insights in model and data,

• experiments demonstrating the correctness of our approach and its superiority over the current state-ofart [13] to quantify the efect of dependent features.

## 2. Background

This section covers the necessary theoretical background of explanations based on Shapley values and their inherent problem with dependent features.

## 2.1. Shapley additive explanations

SHAP is a post-hoc (i.e. after training) method to interpret the output of a complex model for a particular sample x (note the bold font) [17]. It constructs a local approximation g of the original prediction model $f$ around x and is of the form:

$$
g \left(X ^ {\prime}\right) = \phi_ {0} + \sum_ {i = 1} ^ {M} \phi_ {i} X _ {i} ^ {\prime} \quad \text { with } \quad X ^ {\prime} \in \{0, 1 \} ^ {M} \phi_ {i} \in \mathbb {R},\tag{2}
$$

with $X ^ { \prime }$ the so-called simplified input of the original input $X ,$ , and $\phi _ { i }$ the actual SHAP values or feature attributions. To transform $X ^ { \prime }$ to X a local mapping function $h _ { x }$ is defined. In general any mapping $X = h _ { \pmb { x } } \left( X ^ { \prime } \right)$ can be utilized, in practice $X _ { i } ^ { \prime }$ will be defined as an indicator whether the particular input feature is present or not, i.e. for particular input x, $X _ { i } ^ { \prime } = \mathbf { 1 } \left[ X _ { i } = \pmb { x } _ { i } \right]$ . In this case M is equal to the number of features and the explanation efectively becomes an additive function on feature presence.

To select reasonable feature attributions $\phi _ { i }$ for the explanation model, three properties are imposed.

1. Local accuracy:

$$
f (\pmb {x}) = g (\pmb {x} ^ {\prime})\tag{3}
$$

i.e. at the sample to explain x, the explanation matches the original model.

## 2. Missingness:

$$
X _ {i} ^ {\prime} = 0 \implies \phi_ {i} = 0,\tag{4}
$$

i.e. if the original input X already had a missing feature, its attribution is always zero. The equivalent form,

$$
f (h _ {\boldsymbol {x}} (x ^ {\prime} \cup i)) = f (h _ {\boldsymbol {x}} (x ^ {\prime} \backslash i)) \forall x ^ {\prime} \implies \phi_ {i} = 0\tag{5}
$$

with $x ^ { \prime }$ ∪ i meaning $x _ { i } ^ { \prime } = 1$ and with $x ^ { \prime } \backslash i$ meaning $x _ { i } ^ { \prime } = 0 ,$ , is clearer.

## 3. Consistency:

For any two models $f _ { 1 }$ and $f _ { 2 } { \mathrm { : } }$

$$
\begin{array}{c} f _ {1} \left(h _ {\boldsymbol {x}} \left(x ^ {\prime}\right)\right) - f _ {1} \left(h _ {\boldsymbol {x}} \left(x ^ {\prime} \backslash i\right)\right) \\ \geq f _ {2} \left(h _ {\boldsymbol {x}} \left(x ^ {\prime}\right)\right) - f _ {2} \left(h _ {\boldsymbol {x}} \left(x ^ {\prime} \backslash i\right)\right) \forall x ^ {\prime} \in \{0, 1 \} ^ {M} \\ \implies \phi_ {i} \left(f _ {1}, \boldsymbol {x}\right) \geq \phi_ {i} (f _ {2}, \boldsymbol {x}) \end{array}\tag{6}
$$

In words, this says that $\mathrm { { \^ 6 6 4 f } \ a }$ model changes so that some simplified input’s contribution increases or stays the same regardless of the other inputs, that input’s attribution should not decrease” [17].

Only one<sup>1</sup> possible set of feature attributions satisfies these properties [17]:

$$
\phi_ {i} (f, \boldsymbol {x}) = \frac {1}{M !} \sum_ {R} f \left(h _ {\boldsymbol {x}} \left(S ^ {R} \cup \{i \}\right)\right) - f \left(h _ {\boldsymbol {x}} \left(S ^ {R}\right)\right),\tag{7}
$$

where R is a permutation of the ordering of simplified inputs and $S ^ { R }$ the set of simplified inputs preceding i in this ordering. To make the formula less cluttered, we use $\left( S ^ { R } \right)$ to denote $\left( \left[ X _ { S ^ { R } } ^ { \prime } = 1 , X _ { \bar { S } ^ { R } } ^ { \prime } = 0 \right] \right)$ . The values $\phi _ { i }$ are known as Shapley values in cooperative game theory [22]. In practice, when the simplified inputs correspond to feature presence, $\phi _ { i }$ is the average over all orderings of the change in model output when adding feature i to the preceding, already ‘known’ features. Equation (7) requires the output of the model when features are missing: $f \left( h _ { \mathbf { x } } \left( X ^ { \prime } \right) \right)$ when $X ^ { \prime } \neq x ^ { \prime }$ . This involves some empirical expectation of $f \left( h _ { \mathbf { x } } \left( X ^ { \prime } \right) \right)$ over a set of training samples. What expectation to choose - conditioning on the missing features or not - will appear to be a controversial topic.

## 2.2. Missing features

The original SHAP paper [17] assumed a seemingly natural way to express the expectation of the model output with missing features: conditioning on known features $S ,$

$$
f \left(h _ {\boldsymbol {x}} \left(X ^ {\prime}\right)\right) = E \left[ f (X) | X _ {S} = \boldsymbol {x} _ {S} \right]. (\text { conditional   SHAP })\tag{8}
$$

In practice, the exact data distribution is unknown. Therefore [17] proposed to use independent features. Then the expectation can be easily approximated by averaging over K background samples $x ^ { k }$ :

$$
E \left[ f (X) | X _ {S} = \pmb {x} _ {S} \right] \approx E \left[ f \left([ \pmb {x} _ {S}, X _ {\bar {S}} ]\right) \right]\tag{9}
$$

$$
\approx \frac {1}{K} \sum_ {k} f \left(\left[ \boldsymbol {x} _ {S}, x _ {\bar {S}} ^ {k} \right]\right),\tag{10}
$$

with missing features S<sup>¯</sup>. A later contribution by the same authors [16] focussed on avoiding the feature independence assumption by exploiting the structure of tree models. Part of the community also followed this direction: [1, 2] estimate the conditional data distribution $p \left( X _ { \bar { S } } | X _ { S } \right)$ to better approximate (8), [27] uses the data distribution assumed by probabilistic PCA to ‘exactly’ compute the SHAP value and [12] simplifies the empirical conditional distribution through prior knowledge of dependencies. For a complete comparison of diferent estimations of conditional SHAP values, we refer to [19].

Some recent papers have tried to advocate a diferent estimation of the model output when features are missing. [8, 10, 11] analyse the missing feature problem from a causal perspective. The conditioning on known features is argued to be interventional, instead of observational (as was implicitly assumed in conditional SHAP). Computing interventional conditional distributions requires a causa graph over the features. [11] distinguishes between the true real world features $\tilde { X }$ and the model inputs X. There can be causal relations between the former but not between the latter. [10] does not make this distinction and the resulting SHAP values are arguably the true causal output efects. The authors therefore deemed their explanations causal Shapley values. To illustrate the diference with the approach of [11], a causal graph for a model with three input features is shown in Figure 1 for both approaches.

Contrary to causal Shapley values [10] the method of [11] does not require any knowledge of the causal relations between the (real world) features. The authors show that the particular causal structure (e.g Figure 1a) leads to a model output equivalent to the left hand side of (9):

$$
f \left(h _ {\boldsymbol {x}} \left(X ^ {\prime}\right)\right) = E \left[ f \left(\left[ \boldsymbol {x} _ {S}, X _ {\bar {S}} \right]\right) \right]. (\text {   interventional   SHAP   })\tag{11}
$$

Without the weight of the coalition, the contribution for one permutation $R ,$ of feature i then becomes

$$
\phi_ {i, S ^ {R}} = E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) \right] - E \left[ f \left([ \boldsymbol {x} _ {S ^ {R}}, X _ {\bar {S} ^ {R}} ]\right) \right]\tag{12}
$$

![](/api/attachments/YJ2D98Y2/fulltext/images/4c523541b92aed776269f85820bd5de3edeada529558100baa6ada619cf6097a.jpg)

![](/api/attachments/YJ2D98Y2/fulltext/images/0a1282b023733cfb1fdb2fe5b02e14afc20b537cb9bc82909af1a1dcb3909452.jpg)  
(b)  
Figure 1: Example causal structures assumed by respectively interventional SHAP [11] (a) and causal Shapley values [10] (b). In (a) the ${ \tilde { X } } _ { i }$ are the real world features and $X _ { i }$ the model inputs. This distinction is not made in (b). For both cases $Z$ is a latent confounder. The dotted lines are the observed statistical dependencies which are taken into account by conditional SHAP, and the new method pro posed in this paper.

instead of

$$
\begin{array}{c} \phi_ {i, S ^ {R}} = E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i} \right] \\ - E \left[ f ([ \boldsymbol {x} _ {S ^ {R}}, X _ {\bar {S} ^ {R}} ]) | \boldsymbol {x} _ {S ^ {R}} \right] \end{array}\tag{13}
$$

for conditional SHAP, with $S _ { i } ^ { R }$ the set $S ^ { R }$ including feature i. In short, interventional SHAP breaks the dependencies between $X _ { i }$ and $X _ { \bar { S } _ { i } ^ { R } }$ , while conditional SHAP allows for them to have an efect. It is important to note that interventional SHAP keeps the dependencies within $X _ { \bar { S } _ { i } ^ { R } }$ [11].

[26] uses the axiomatic approach to study the attribution problem. They test interventional and conditional SHAP against a list of desirable properties. Contrary to the properties imposed in Section 2.1, these are at the level of the model f not at the level of the model approximations $\left( f \left( h _ { \mathbf { x } } \left( X ^ { \prime } \right) \right) \right)$ when $X ^ { \prime } \neq x ^ { \prime } )$ , e.g. missingness (5) becomes ‘dummy’.

Dummy:

$$
f ([ x _ {i}, x _ {\backslash i} ]) = f ([ d, x _ {\backslash i} ]) \forall x, d \implies \phi_ {i} = 0\tag{14}
$$

The authors show that conditional SHAP fails this property (and others), while interventional SHAP does not.

## 3. Related work

Recently [6] also suggested the same distinction as described in our introduction and motivate each of the approaches with a use case. Interventional SHAP seems the method of choice when a loan applicant wants to see what features directly increase their likelihood of being granted a loan. If we want to know more about the natural mechanism of gene expression in a patient with a type of blood cancer, the conditional SHAP value is preferred and identified more of the true underlying variables. They call this approach ‘true to the data’. In contrast with this paper, no attempt to unify both types of SHAP values was undertaken.

Similar to our contribution, [10] decomposes the causal Shapley value into a direct and indirect efect and applies the decomposition to a theoretical example to show how diferent causal graphs result in diferent Shapley values. They do not provide a possible implementation and neither do they motivate using the decomposition in practice. Here we interpret this decomposition as a unification of conditional and interventional SHAP, and provide an implementation and illustrations to increase the understanding of the method. Furthermore we compare it with other state-of-the art Shapley implementations.

Shapley residuals [13] can capture limitations of regular Shapley value implementations. They are represented by residual vectors $r _ { i }$ measuring how distant all contributions for specific $S \left( \phi _ { i , S } \right)$ are from the contributions of the nearest inessential game. In an inessential game every player (in case of machine learning a feature value) contributes a fixed amount to the objective regardless of S. As shown in [13] the contributions of the nearest inessential game are the actual Shapley values $\left( \phi _ { i , S } = \phi _ { i } \right)$ . In case of conditional SHAP value, Shapley residuals quantify the efect of dependent features. Specifically, it is argued that the norm of $r _ { i }$ relates to the efect of dependencies between feature i and other features on the SHAP value. For interventional SHAP values, the residuals capture efects of feature interactions in the model (e.g. of the term $X _ { 1 } X _ { 2 }$ in model $f ( X _ { 1 } , X _ { 2 } ) = X _ { 1 } + X _ { 2 } + X _ { 1 } X _ { 2 } )$ . Explaining such feature interaction (also see Shapley-Interaction interaction indices [25]) is not the interest of this paper.

[29] also design a Shapley value implementation that provides a more involved explanation when dependencies between input features exist. In fact, they assign a contribution to every causal link (or edge in causal graph) while still adhering to the fundamental axioms described in Section 2.1. A connection with conditional SHAP is made but interventional SHAP values are not discussed. Similarly to causal Shapley values [10] a causal graph over the features is required.

Another important diference between interventional and conditional SHAP values is that the former evaluates the machine learning model on out of distribution samples. Intervening on feature values results in samples which do not represent the underlying data distribution (also called of-manifold). It is shown that this allows for adversarial attacks that can manipulate explanations to hide unwanted model biases [23]. While we acknowledge this issue, interventions still provide important insight into the model as motivated in our introduction (e.g. for bias detection) and in [6]. Interestingly, a recent paper proposes an interpretation of interventional Shapley values with samples on the manifold [28]. A more direct approach to defend against the adversarial attacks [23] employing knockof imputation is introduced in [4]. For more information on the of-manifold problem we direct the reader to [7, 30]. In our paper, the focus will be on the meaningful usage and desired theoretic properties of SHAP values, and not on their robustness or eficiency.

The missing feature problem in SHAP values and its solutions are diferent from the general problems with missing values in datasets and their solutions (e.g. data imputation). The calculation of Shapley values via Equation 7 requires model outputs when features are unknown even when the dataset itself has no missing values. Furthermore, this computation happens after model training (it is a post-hoc method) while missing values in the dataset typically have to be addressed before or during training.

Lastly, [5] provides an accessible overview of the many algorithms to compute Shapley values.

## 4. Explaining model and result

The properties defined in [26] (such as (14)) quantify the model correspondence of the explanations. Conditional SHAP, not adhering to many of these properties, sacrifices this model correspondence for more result-centric feature attributions. These latter attributions arguably show the actual statistical relations between inputs and output (or result). Note that the relations may not be fully present in the data. The model fitting enforces some domain and/or data knowledge. Also, the complexity of the model might be limited for computational reasons, meaning that the ‘true’ relations in the data are not uncovered. On this point we do not completely agree with [6]. They mention that conditional SHAP values are true to the data and interventional SHAP values true to the model. As we argued, conditional SHAP values are both true to the data and true to the model.

Causal Shapley values [10] show the true causal relations between inputs and output, and thus also explain the result. The big diference is that conditional SHAP relies on association (or statistical dependence) and the causal Shapley value on causation. For example in Figure 1b $X _ { 2 }$ and $X _ { 3 }$ have a common cause Z and will be associated (note the dotted line) without a causal relationship. We agree with [10] that causal relations are more intuitive than observed statistical dependencies. However, in practice causal knowledge about the input features is often unavailable, hence the use of conditional SHAP in the rest of this paper.

It should be clear that in the introductory example interventional SHAP values are preferred in court; and in the hospital setting the conditional version would be better. Conditional SHAP also finds the feature’s attribution through other dependent features. We can show that the feature’s attribution can be split up into its ‘direct’ interventional efect and its ‘indirect’ dependent efect. This decomposition of the SHAP value can be used in both the court and hospital setting.

## 4.1. Decomposition of the SHAP value

Since our interest is decomposing the output efect into an interventional efect of $\mathbf { \Delta } _ { \mathbf { \mathcal { X } } _ { i } }$ and its efect via the unknown features ${ \bar { S } } _ { i } ,$ , we determine the efect of intervening on $\mathbf { \nabla } x _ { i }$ when the features in S are already known. I.e. the effect of setting $X _ { i } = x _ { i }$ (breaking X ’s dependencies) on $f _ { S } ( \left[ X _ { i } , X _ { \bar { S } _ { i } } \right] ) = f ( \left[ \bar { \bf x } _ { S } , \dot { X _ { i } } , X _ { \bar { S } _ { i } } \right] )$ ). This is equal to:

$$
\begin{array}{c} E \left[ f _ {S} \left(\left[ \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i}} \right]\right) \right] - E \left[ f _ {S} (X _ {\bar {S}}) \right] \\ = E \left[ f \left(\left[ \boldsymbol {x} _ {S}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i}} \right]\right) | \boldsymbol {x} _ {S} \right] - E \left[ f ([ \boldsymbol {x} _ {S}, X _ {\bar {S}} ]) | \boldsymbol {x} _ {S} \right] \end{array}\tag{15}
$$

This efect can be interpreted as a part of the contribution for one permutation R in case of the conditional SHAP value:

$$
\begin{array}{r l} & {\phi_ {i, S ^ {R}} (f, \boldsymbol {x}) = E \left[ f (X) | X _ {S ^ {R}} = \boldsymbol {x} _ {S ^ {R}}, Z _ {i} = \boldsymbol {x} _ {i} \right]} \\ & {\qquad - E \left[ f (X) | X _ {S ^ {R}} = \boldsymbol {x} _ {S ^ {R}} \right]} \\ & {\qquad = E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i} \right]} \\ & {\qquad - E \left[ f ([ \boldsymbol {x} _ {S ^ {R}}, X _ {\bar {S} ^ {R}} ]) | \boldsymbol {x} _ {S ^ {R}} \right]} \\ & {\qquad = \Big (E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}} \right]} \\ & {\qquad - E \left[ f ([ \boldsymbol {x} _ {S ^ {R}}, X _ {\bar {S} ^ {R}} ]) | \boldsymbol {x} _ {S ^ {R}} ]\right)} \\ & {\qquad + \left(E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i} \right] \right.} \\ & {\qquad - E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}} ]\right)} \\ & {\qquad = \phi_ {i, S ^ {R}, i n t} (f, \boldsymbol {x}) + \phi_ {i, S ^ {R}, d e p} (f, \boldsymbol {x}).} \end{array}\tag{16}
$$

We have arrived at an equivalent decomposition as in [10] but without causal operations. From (16) we see that the contribution of a feature i (for a permutation R) is the sum of an interventional output efect of $\mathbf { \Delta } _ { \mathbf { \mathcal { X } } _ { i } }$ conditioned on ${ \pmb x } _ { S ^ { R } }$ and the output efect of knowing $\mathbf { \Delta } _ { \mathbf { \mathcal { X } } _ { i } }$ on the unknown variables, again conditioned on ${ \pmb x } _ { S ^ { R } }$ . Notice the similarity between $\phi _ { i , S ^ { R } , i n t } ( f , \pmb { x } )$ and interventional SHAP (12): the dependencies between $X _ { i }$ and $X _ { \bar { S } _ { \bar { i } } ^ { R } }$ are still broken. Consequently, the causal motivation behind interventional SHAP still holds and this decomposition successfully connects the interventional and conditional approach to dealing with missing features.

Note that above interpretation also holds for the Shapley value since that is an average over all $\phi _ { i , S ^ { R } } ( f , { \pmb x } )$ ). Thus, the conditional SHAP value can be split up into two SHAP value parts. Although these parts are not real SHAP values (there respective sums do not equal the original output values, i.e. no local accuracy), they arguably provide both a model and a result explanation.

As explained in the related work, Shapley residuals [13] for a particular model $f$ and feature i can be interpreted as the geometric diference between the contributions $\phi _ { i , S }$ for all S and the SHAP value $\phi _ { i } .$ , i.e. $r _ { i } \in \mathbb { R } ^ { | S | }$ and $r _ { i , S } =$ $\phi _ { i , S } - \phi _ { i } .$ Thus, they define a decomposition of similar form as Equation (16) which was not discussed in [13], namely:

$$
\phi_ {i, S ^ {R}} (f, \boldsymbol {x}) = \phi_ {i} (f, \boldsymbol {x}) + r _ {i, S ^ {R}}\tag{17}
$$

This allows us to claim the following proposition.

Proposition 1. The associated SHAP part of the Shapley residual is always zero.

<sup>Proof.</sup> The SHAP part can be found by averaging (17) over all R:

$$
\frac {1}{M !} \sum_ {R} \phi_ {i, S ^ {R}} (f, \pmb {x}) = \phi_ {i} (f, \pmb {x}) + \frac {1}{M !} \sum_ {R} r _ {i, S ^ {R}}.\tag{18}
$$

Since the left hand side is exactly equal to the SHAP value we arrive at:

$$
\frac {1}{M !} \sum_ {R} r _ {i, S ^ {R}} = 0.\tag{19}
$$

□

Because the associated SHAP part will always be zero, the concept of Shapley residuals can not be used to split the SHAP value into a sum of parts.

## 4.2. Theoretical validation

It is easily proven that the interventional part passes the dummy property (14), underlining its model correspondence. Also, for an independent distribution the interventional SHAP part coincides with the interventional SHAP value.

Proposition 2. Interventional SHAP part passes the dummy property (14), i.e.

$$
f ([ x _ {i}, x _ {\backslash i} ]) = f ([ d, x _ {\backslash i} ]) \forall x, d \implies \phi_ {i, i n t} = 0\tag{20}
$$

<sup>Proof.</sup> Take feature i to be a missing feature:

$$
f ([ x _ {i}, x _ {\backslash i} ]) = f ([ d, x _ {\backslash i} ]) \quad \forall x, d.\tag{21}
$$

Its feature value contribution for permutation $R ,$

$$
\begin{array}{r l} \phi_ {i, S ^ {R}, i n t} (f, \boldsymbol {x}) & = E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}} \right] \\ & - E \left[ f ([ \boldsymbol {x} _ {S ^ {R}}, X _ {\bar {S} ^ {R}} ]) | \boldsymbol {x} _ {S ^ {R}} \right] \\ & = E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}} \right] \\ & - E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, X _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}} \right] \end{array}\tag{22}
$$

is zero since both terms are equal by (21). The actual SHAP part, an average over the former diferences, is thus also zero.

Furthermore, since a decomposition should split the conditional SHAP value into an interventional efect and an efect through the dependent features, it is desired that the interventional SHAP part is equal to the conditional SHAP value for independent variables.

Proposition 3. The interventional SHAP part of an independent variable is equal to the conditional SHAP value, i.e.

$$
X _ {i} \perp       \perp X _ {\backslash i} \implies \phi_ {i, i n t} = \phi_ {i}\tag{23}
$$

<sup>Proof.</sup> The feature value contribution for permutation $R ,$

$$
\begin{array}{r l} \phi_ {i, S ^ {R}} (f, \boldsymbol {x}) & = E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i} \right] \\ & - E \left[ f ([ \boldsymbol {x} _ {S ^ {R}}, X _ {\bar {S} ^ {R}} ]) | \boldsymbol {x} _ {S ^ {R}} \right] \\ & = E \left[ f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, X _ {\bar {S} _ {i} ^ {R}} \right]\right) | \boldsymbol {x} _ {S ^ {R}} \right] \\ & - E \left[ f ([ \boldsymbol {x} _ {S ^ {R}}, X _ {\bar {S} ^ {R}} ]) | \boldsymbol {x} _ {S ^ {R}} \right] \\ & = \phi_ {i, S ^ {R}, i n t} (f, \boldsymbol {x}) \end{array}\tag{24}
$$

since $X _ { i } \perp \perp X _ { \bar { S } _ { i } ^ { R } }$ . Averaging the above equation over al permutations proofs the proposition.

Proposition 4. Our proposed decomposition (16) divides the model output efect among the model’s additive components. Writing $\begin{array} { r } { f ( X ) = \sum _ { A \subset F } f ( X _ { A } ) } \end{array}$ then

$$
\begin{array}{c} \phi_ {i, i n t} (f, \boldsymbol {x}) = \phi_ {i, i n t} \left(\sum_ {A \subseteq F | i \in A} f _ {A}, \boldsymbol {x}\right) \\ \phi_ {i, S ^ {R}, d e p} (f, \boldsymbol {x}) = \phi_ {i, S ^ {R}, d e p} \left(\sum_ {A \subseteq F | S _ {R} \subseteq A} f _ {A}, \boldsymbol {x}\right) \end{array}\tag{25}
$$

<sup>Proof.</sup> Using Equation (16) and knowing that the expectation of a sum of variables is equal to the sum of its individual expectations, we find that parts of the additive function cancel each other resulting in the claimed properties.

We can gain extra intuition by considering a linear model: $\textstyle f = \sum _ { i } a _ { i } X _ { i }$ . In this case, the interventional SHAP values $\psi _ { i }$ , interventional SHAP parts $\phi _ { i , i n t }$ and dependent SHAP parts $\phi _ { i , d e p }$ for a sample x simplify to:

$$
\psi_ {i} = a _ {i} \left(\boldsymbol {x} _ {i} - E [ X _ {i} ]\right) = f (\boldsymbol {x}) - f \left(\left[ \boldsymbol {x} _ {\backslash i}, E [ X _ {i} ] \right]\right),\tag{26}
$$

$$
\phi_ {i, i n t} = \frac {1}{M !} \sum_ {R} a _ {i} (\pmb {x} _ {i} - E [ X _ {i} | \pmb {x} _ {S ^ {R}} ])\tag{27}
$$

$$
= \frac {1}{M !} \sum_ {R} f (\boldsymbol {x}) - f \left(\left[ \boldsymbol {x} _ {\backslash i}, E [ X _ {i} | \boldsymbol {x} _ {S ^ {R}} ] \right]\right),
$$

$$
\phi_ {i, d e p} = \frac {1}{M !} \sum_ {R} \sum_ {j \in \bar {S} _ {i} ^ {R}} a _ {j} (E [ X _ {j} | \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i} ] - E [ X _ {j} | \boldsymbol {x} _ {S ^ {R}} ]).\tag{28}
$$

First of all, notice that the interventional SHAP value corresponds with the change in model output when setting the respective feature to its average value. The interventional SHAP part, on the other hand, is the average over all permutations of the change in model output when intervening with a conditional mean. The conditioning is on the feature values appearing before i in the permutation. In one of the experiments below we will argue why the latter mean can be more realistic. Note that the above observations are only exact for a linear machine learning model. Lastly, as expected from Proposition 4, $\phi _ { i , i n t }$ only depends on $X _ { i } { } ^ { \ ' } \mathrm { s }$ coeficient, while the dependent SHAP part $\phi _ { i , d e p }$ depends on all the other coeficients.

## 4.3. Implementation

Computing the SHAP values from (7) exactly is only feasible if the model has a few inputs, since it requires a sum over all possible orderings of inputs. To eficiently compute the SHAP value for models with more inputs, [17] proposes Kernel SHAP which interprets the computation of Equation (7) as performing a weighted linear regression. This is shown to be more sample-eficient than straightforwardly sampling the sum in (7). Computation of the SHAP parts can not be expressed as a weighted linear regression. Hence, to calculate the interventional SHAP part, we use a more rudimentary sampling approach as proposed by [24].

The complete procedure for a sample x is as follows:

1. obtain or estimate the conditional data distribution $p \left( X _ { \bar { S } } | X _ { S } \right)$ ;

2. compute the conditional SHAP values by applying Kernel SHAP, estimating $\begin{array} { r } { E \left[ f ( X ) | X _ { S } = \pmb { x } _ { S } \right] \approx \frac { \breve { 1 } } { K _ { 1 } } \sum _ { k } f \left( \left[ \pmb { x } _ { S } , \pmb { x } _ { \bar { S } } ^ { k } \right] \right) } \end{array}$ sampled from $p ( X _ { \bar { S } } | X _ { S } \overset { \cdot } { = } x _ { S } ) \colon$

3. compute the interventional SHAP parts:

(a) sample $K _ { 2 }$ feature permutations;

(b) for each permutation R sample single data point

$$
x _ {\bar {S} ^ {R}} ^ {1} \text {   from   } p (X _ {\bar {S} ^ {R}} | X _ {S ^ {R}} = \boldsymbol {x} _ {S ^ {R}});
$$

$$
\frac {1}{K _ {2}} \sum_ {R} f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, \boldsymbol {x} _ {i}, x _ {\bar {S} _ {i} ^ {R}} ^ {1} \right]\right) - f \left(\left[ \boldsymbol {x} _ {S ^ {R}}, x _ {\bar {S} ^ {R}} ^ {1} \right]\right);
$$

4. compute the dependent SHAP parts by subtracting the interventional parts from the SHAP values.

Practically, $K _ { 1 }$ and $K _ { 2 }$ are increased until suficient convergence is achieved. Due to the decreased sample efficiency [17], we advise $K _ { 2 }$ to be taken bigger than $K _ { 1 }$

The above procedure can be applied for any conditional data distribution which can be sampled. In our experiments we used a multivariate Gaussian distribution and a Gaussian copula (as proposed by [1]). The complete algorithm in the case of a multivariate Gaussian data distribution is available in the Appendix. Like the original Kernel SHAP, our implementation is model agnostic and thus can be used with any model f including neural networks and support vector machines.

## 5. Experiments

Returning to the toy example in the introduction, with $X _ { 1 }$ and $X _ { 2 }$ both Bernoulli distributed with $p = 0 . 5$ and $P ( X _ { 1 } = X _ { 2 } ) = 0 . 7$ , we can exactly compute the SHAP parts. For the sample output $f _ { r } ( X _ { 1 } = 1 , X _ { 2 } = 1 ) = 1$ they are shown as a force plot [18] in Figure 2. We see that the convict’s race has no interventional efect. Whether the patient is obese does have an output efect via its dependent feature ‘high heart rate’ which is clearly shown in the explanation.

We continue this section by first comparing the interventional and dependent SHAP part to the state-of-theart, whereafter the combined explanation is examined.

![](/api/attachments/YJ2D98Y2/fulltext/images/04392e03b2e2896ae703b4950ea89576d5c1f014899a9e55e0755bd90dc5dce6.jpg)  
Figure 2: Force plot on sample from the introduction dataset. The top bar shows the standard conditional SHAP value [1]. Each value is decomposed into an interventional and dependent SHAP part which are sized relatively to the conditional SHAP value and shown on respectively the second and third bar. As can be seen, race or obesity has no direct interventional efect on the model output. They do have an indirect dependent efect via their dependent features, prior recidivism and high heart rate respectively.

## 5.1. Interventional SHAP part

To underline the model correspondence of the interventional SHAP part, we conduct a first experiment. [6] trains a logistic regression model on a large dataset of loans and examines which explanation, interventional or conditiona SHAP values, helped a loan applicant in decreasing their risk of default. Generally speaking, the goal is to find the best method to determine which sequence of features are to be changed (intervened upon) to influence the model output favourably. In case of the Boston Housing dataset [9], we can consider a mayor who likes to increase the median house price in his town. To this extent, the town mayor can set the features with the most negative SHAP values to the mean feature value and check the change in median house price. In this experiment, the explanation is better if the median house price increases faster. Note that it is implicitly assumed that the features can be changed (unlike race for example). This is also assumed by [6].

In Figure 3a we show the change in house price when the features are selected by consulting, respectively, the interventional SHAP value, the interventional SHAP parts, the conditional SHAP values. Motivated by the theoretical observations in Section 4.2, a linear model (ordinary least squares) is used. Note that the efective model of [6] is also linear since the SHAP values are computed on the log odds. The dataset is assumed to be multivariate Gaussian.

It is also interesting to consider imputing with the mean conditioned on the (still) unchanged features. This can be considered a more reasonable way to increase the median house price: how much we can realistically change a feature (e.g. decrease the crime rate) depends on many other features (e.g. the quality of the education in the town measured by the pupil-teacher ratio PTRATIO). The results are shown in Figure 3b.

The experiments are also repeated for a non-linear model (a random forest) and are shown in the Appendix.

![](/api/attachments/YJ2D98Y2/fulltext/images/143541daede9542b53f9138c09a07ea944c12f27771db8c77f903bbf473b0c5a.jpg)  
(a)

![](/api/attachments/YJ2D98Y2/fulltext/images/94d911d2e5585f25d62c40aa5fa9696a9d311dde1b2d1ba5d229f024fb31b8fd.jpg)  
(b)  
Figure 3: Change in house price when imputing selected features with respectively the regular mean (a) and the mean conditioned on the unchanged features (b). A linear model is used to predict the house price. The values are computed for 200 random towns and averaged.

![](/api/attachments/YJ2D98Y2/fulltext/images/8d39b2b478740a6655cc9f9dc380118172f31cf49fd18dfdd4caf6f64ba7cfdf.jpg)  
Figure 4: The dependency attribution of our method and the state of-the-art [13] as a function of the correlation coeficient between two Gaussian variables in an additive model with feature interaction (Equation (29) with $a _ { 1 2 } = 2 )$

## 5.2. Dependent SHAP part

Regarding attributions via dependent features we can compare our approach with Shapley residuals [13]. Consider the following two-dimensional additive model with feature interaction and data distribution:

$$
\begin{array}{l} f ([ X _ {1}, X _ {2} ]) = X _ {1} + X _ {2} + a _ {1 2} X _ {1} X _ {2}, \\ [ X _ {1}, X _ {2} ] \sim \mathcal {N} \left([ 0, 0 ], \left[ \begin{array}{c c} 1 & \alpha \\ \alpha & 1 \end{array} \right]\right). \end{array}\tag{29}
$$

For a sample $[ X _ { 1 } = 1 , X _ { 2 } = 1 ]$ the conditional SHAP value and dependent SHAP part for $i \in \{ 1 , 2 \}$ are :

$$
\begin{array}{l} \phi_ {i} = 1 + 0. 5 a _ {1 2} (1 - \alpha), \\ \phi_ {i, d e p} = 0. 5 (1 + a _ {1 2}) \alpha . \end{array}\tag{30}
$$

The Shapley residual vector [13] and its norm are:

$$
\begin{array}{l} r _ {i} = \left[ \begin{array}{c} 0. 5 a _ {1 2} - (1 + 0. 5 a _ {1 2}) \alpha \\ - 0. 5 a _ {1 2} + (1 + 0. 5 a _ {1 2}) \alpha \end{array} \right] \\ | | r _ {i} | | = \sqrt {2} | 0. 5 a _ {1 2} - (1 + 0. 5 a _ {1 2}) \alpha |. \end{array}\tag{31}
$$

The relationship of both dependent attributions with respect to the correlation α is shown in Figure 4.

## 5.3. Combined explanation

We apply our method again to the Boston Housing dataset [9]. This time the model used is a high accuracy random forest and the dataset is assumed to be (multivariate) Gaussian distributed. Figure 5 depicts one complete explanation, showing a series of interesting local interventional and dependent efects. For example, the crime rate per capita (CRIM ) being 0.17004 has a big positive effect on the median house price in this town, and the efect is largely interventional. This means that the CRIM of this town has a strong efect on the output via its specific weights in the model. The pupil-teacher ratio PTRATIO also has positive efect. A significant part of this efect is through its dependent features: it influences the distributions of the dependent features which in term increase the expected model output via their specific weights. We can also see that the model has a small racial bias: the interventional part of B is non-zero. Note that B is equal to $1 0 0 0 ( b - 0 . 6 3 ) ^ { 2 }$ with b the black proportion of population [9]. The weighted distance to employment centres (DIS ) has a dependent and interventional part that difer in their sign. As a direct result one part will be bigger than the SHAP value and efectively contain the SHAP value. To provide a concise representation through the force plot, the SHAP parts are downscaled and the faded colour reveals the true sizes of the parts.

![](/api/attachments/YJ2D98Y2/fulltext/images/7e06fe7f0c9c0f9ae8f01015da948172ed791de006ae2f3e11ee336499222062.jpg)  
Figure 5: Force plot on sample from Boston Housing dataset

Finally to show that our method generalizes to diferent datasets and their assumed distribution we apply the method to the Algerian Forest Fires dataset [3] and use a Gaussian copula to model the distribution [1]. We use a random forest to predict the probability of a forest fire based on temperature (T ), relative humidity (RH ), wind speed (Ws) and Rain. A complete explanation can be found in Figure 6a with a corresponding classic (interventional) SHAP explanation [18] in Figure 6b. Additionally, in the interest of studying the interventional and dependent connections between features and output, a partia correlation graph was constructed. This allows us to measure the degree of association between two variables, after removing the efect of all other controlling variables. Figure 7 shows the partial correlation graph for the Algerian Forest Fires dataset, where $f _ { F }$ is the log odds output of the trained model. This graph can be compared with the (normal) correlation between the features and their respective interventional and dependent SHAP parts in Table 2. All reported values are Spearman’s rank correlations.

## 6. Discussion

The explanation for the toy example (Figure 2) is sufficient in both settings. In the court setting, the convict can clearly see the absence of racial bias. In the hospital setting, it is clear that the patient’s obesity has an efect on the risk of a heart attack. We also notice the dependent part of $X _ { 2 }$ (prior recidivism or high heart rate) being zero. As explained in Section 4, the dependent SHAP part characterizes the efect of a feature value on the model output through its dependent features. None of the dependent features of $X _ { 1 }$ can afect the model output when $X _ { 1 }$ is set to a value x : changing $X _ { 2 }$ (race or obesity) will not change the output since it is already determined by $X _ { 1 } = x _ { 1 }$ , i.e. $f _ { r } ( [ x _ { 1 } , X _ { 2 } ] ) = x _ { 1 }$ . Thus the dependent part of $X _ { 2 }$ is zero as expected.

![](/api/attachments/YJ2D98Y2/fulltext/images/8e2a8b91a1a92bd8a8e144121a3bc17e7f8cb424fa9743305f95eba513ca2a1f.jpg)  
(a)

![](/api/attachments/YJ2D98Y2/fulltext/images/4bd59d45720c8819e3e713f41332ca40f7ebff19c66f3298b09b2af655a91822.jpg)  
(b)  
Figure 6: Force plot on a correctly classified sample of the Alge rian Forest Fires dataset with our approach (a) and the approach of [18] (b) respectively. The top axis denotes the probability (for interpretability) and the one below denotes the log odds (on which the SHAP values and parts are actually computed).

![](/api/attachments/YJ2D98Y2/fulltext/images/a6abbddfe5fec69cf7c7d74fccd474cf0655dfa544c44e83644b60e3d21a0d33.jpg)  
Figure 7: Partial correlation graph between features and output of the model $f _ { F } .$ . Spearman’s partial correlations are shown on the edges. Red and blue edges respectively show positive and negative correlation. The line width of the edge varies linear with the absolute value of the correlation

Table 2: Correlations between feature values and their SHAP values

<table><tr><td> $\phi$ \i</td><td>Ws</td><td>RH</td><td>T</td><td>Rain</td></tr><tr><td> $\phi_{i,int}(f_F)$ </td><td>0.86</td><td>-0.69</td><td>0.79</td><td>-0.88</td></tr><tr><td> $\phi_{i,dep}(f_F)$ </td><td>0.41</td><td>-0.29</td><td>-0.52</td><td>0.75</td></tr></table>

The other results should validate the interventional and dependent SHAP part and show their equivalence or superiority to the state-of-the-art. Secondly the combined explanation should explain both the model and the result, and should enhance interpretability for diferent settings and data distributions.

## 6.1. Interventional SHAP part

From Figure 3a we can see that on average selecting and mean imputing the features with the biggest negative interventional SHAP part is a better approach to increase the house price than using the conditional SHAP values. Using interventional SHAP values (not parts) still achieves bigger increases in house price, confirming the results of [6]. Both interventional approaches clearly outperform the conditional SHAP approach, confirming their model correspondence. In fact, interventions guided by conditional SHAP values can result in a significant decrease in house price. This can occur when features are highly correlated but have opposite direct efects on the model output via their respective weights. In the Appendix we illustrate this with a simple example. It also has additional experiments that show the significance of the results.

Figure 3a also shows that interventional SHAP values are more true to the model than interventional SHAP parts. This is as expected since for a linear model the exact interventional SHAP value is equal to the change in model output when imputing with the marginal mean (see (26)). If instead of the marginal, the conditional mean is used, interventional SHAP part comes out on top (Figure 3b). Again, because of (27), this is an expected result. Note that these observations are independent of the fitting procedure for the linear model: as long as the resulting model is linear, (26) and (27) will hold and the experiments should lead to the same conclusions. These results show that the interventional SHAP part is indeed a direct model (or interventional) efect and is more representative when the intervention is done with the arguably more intuitive conditional mean. Additionally it adheres to the dummy property (Proposition 2). Thus we can claim that our decomposition provides equivalent interventional insight as interventional SHAP [11].

For a non-linear model, (26) and (27) do not hold. Although the diferences between the approaches are less significant in case of a random forest (see the Appendix), they are still in line with the results for a linear model.

## 6.2. Dependent SHAP part

Figure 4 shows that the dependent SHAP part increases linear with the correlation and is zero when the features are independent, as desired. The norm of the Shapley residual follows a less intuitive trajectory: it is not zero for independent features and does not monotonically increase with the correlation coeficient. Even more, it is zero at a certain non-zero correlation. Shapley residuals for conditional SHAP values also account for feature interactions in the model not only for interactions in the data, a observation not made in [13]. To efectively explain the model and the result, the dependent attribution should not attribute importance solely to feature interactions in the model (which Shapley residuals do for $\alpha = 0 )$ Therefore it is clear that our method is preferred. Furthermore, Shapley residuals can not be interpreted as additive parts of Shapley values: as claimed by Proposition 1 and confirmed by summing the components of $r _ { i }$ in Equation (31) this part would always be zero. This makes residuals unsuitable for intuitive representation through force plots, unlike our method.

## 6.3. Combined explanation

The explanation for the sample of the Algerian Forest Fire dataset (6a) allows to validate the model output: a lay person would agree with the large interventional efect of the temperature being 37 degrees Celsius. Furthermore, the combined explanation of interventional and dependent parts allow to motivate certain actions to change the expected result (fire or no fire). We can read that dropping water on this forest should directly decrease the probability of a fire (high interventional efects of relative humidity RH and Rain). A smaller (and possible delayed) but significant dependent efect is also expected. This informa tion can not be distilled with the approach of [18] (Figure 6b).

The correlations between features and their SHAP values in Table 2 are supported by the partial correlations between features and output shown in Figure 7. Table 2 and Figure 7 both provide a limited view into the modeldata structure: they are expected to show similarities but are not comparable in an absolute sense. The partial correlations between each input and the output $f _ { F }$ resemble the correlations between each input and its interventional SHAP part. Furthermore, the big positive correlation of Rain with its dependent SHAP part (in contrast with its big negative correlation with its interventional SHAP part) can be attributed to positive partial correlations with other features (T , Ws) and their high positive partial correlation with the output $f _ { F } ,$ . These observations validate the decomposition and show how it can give more insight into the model-data structure than other SHAP implementations. Note that Shapley flow [29] would provide even more insight into the model and data dependencies, but their approach is less practical since it require a causal graph and the explanations can not be represented through the popular force plots [18].

In practice, our method can be used on any dataset (and model) regardless of its size and its number of features, and the computational cost can be controlled by the parameters of the method.

If no reasonable estimation of the data distribution can be made (either data driven or knowledge driven) and/or the interest is clearly in interventional output efects, interventional SHAP is the method of choice. If suficient causal knowledge is available it might be interesting to look into causal Shapley values [10] or Shapley flow [29]. In all other cases we advise to use our method, since there is only information gain with regards to (standard) conditional SHAP. An overview of the insights our approach provides compared to related approaches is given in Table 3.

We conclude this section by summarizing how to interpret and use our decomposition into SHAP parts. As classical SHAP values, both parts provide an expected change in model output. The interventional SHAP part can be interpreted as the expected change in model output when the feature value is changed without afecting the other features. This can used to detect bias (e.g. of a convict’s race in a recidivism prediction model) or to select features on which to intervene for an immediate efect (e.g. on the Boston housing dataset, where a mayor wants to increase the house price as fast as possible). If the intervention happened in a natural setting, it is expected that its dependent variables will also change to adhere to the data distribution. This causes a possibly delayed efect that is captured by the dependent SHAP part (the longer-term efect in e.g. patient treatment and on the risk of forest fire).

## 7. Limitations

As is often the case with new explanation methods (as those proposed by [1], [26] and [11]), validation is mostly done through theory and (our own) intuition. Further work could consist of discussing the results and also the general method formulation with domain experts.

There are also some shortcomings of the method. First of all, the distinction between model and result might only be apparent to the machine learning researcher. The domain expert who is not familiar with machine learning or even statistics might not be interested in this distinction. Secondly, just like conditional SHAP and unlike interventional ${ \mathrm { S H A P } } ,$ our method requires conditionally sampled feature values. In our real data experiments we used a multivariate Gaussian distribution and a Gaussian copula. Other approaches are proposed by [1].

## 8. Conclusion

This paper started by motivating a new point of view on post-hoc explanations: an apparent distinction between model and result explanations. To remove this burden of choice, we derive a novel method, extending conditional SHAP, to combine and unify both explanations. Through theory and experiments we show that our method provides equivalent interventional insight as interventional SHAP while additionally explaining feature dependencies better that the existing state-of-the art. Finally, we contributed a novel Shapley value implementation and accompanying force plots suitable for a wide selection of settings, without requiring causal knowledge.

Table 3: Suitability of our decomposition and related Shapley implementations to simultaneously explain diferent important aspects of the model-data structure. The greyed-out methods require knowledge of the causal graph. In case of causal Shapley values the parentheses denote the lack of implementation. For Shapley residuals, it is clear from our experiment in Section 5.2 that they are not always suitable for explaining dependencies in the data.

<table><tr><td></td><td>model</td><td>result (model+data)</td><td>interactions in model</td><td>dependencies in data</td></tr><tr><td>decomposition SHAP</td><td>✓</td><td>✓</td><td></td><td>✓</td></tr><tr><td>Shapley flow [29]</td><td>✓</td><td>✓</td><td></td><td>✓</td></tr><tr><td>causal Shapley values [10]</td><td>(✓)</td><td>✓</td><td></td><td>(✓)</td></tr><tr><td>Shapley residuals [13]</td><td></td><td></td><td>✓</td><td>(✓)</td></tr><tr><td>conditional SHAP [1]</td><td></td><td>✓</td><td></td><td></td></tr><tr><td>interventional SHAP [11]</td><td>✓</td><td></td><td></td><td></td></tr></table>

## Acknowledgements

This project has received funding from the Flemish Government (AI Research Program) and from the FWO (‘Artificial Intelligence (AI) for data-driven personalised medicine’, G0C9623N and ‘Deep, personalized epileptic seizure detection’, G0D8321N) and Leuven.AI Institute.

## Declaration of interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Code availability

Python code to calculate SHAP parts and corresponding plots on any dataset are available at https://github. com/JoranMichiels/decomposition-shap. The experiments of this paper are also included.

## Appendix A. Implementation with Gaussian data distribution

To compute the interventional and dependent SHAP parts, we need access to the conditional data distribution $p \left( X _ { \bar { S } } | X _ { S } = \pmb { x } _ { S } \right)$ with S a subset of the features. If we assume a multivariate Gaussian data distribution, the conditional distribution is also Gaussian with mean $\mu _ { \bar { S } | S }$ and covariance matrix $\Sigma _ { \bar { S } | S }$ . Write

$$
\Sigma = \left[ \begin{array}{l l} \Sigma_ {S S} & \Sigma_ {S \bar {S}} \\ \Sigma_ {\bar {S} S} & \Sigma_ {\bar {S} \bar {S}} \end{array} \right] \mathrm{and} \mu = \left[ \begin{array}{l} \mu_ {S} \\ \mu_ {\bar {S}} \end{array} \right],\tag{32}
$$

then

$$
\mu_ {\bar {S} | S} = \mu_ {\bar {S}} + \Sigma_ {\bar {S} S} \Sigma_ {S S} ^ {- 1} (\pmb {x} _ {S} - \mu_ {S})
$$

and

(33)

$$
\Sigma_ {\bar {S} | S} = \Sigma_ {\bar {S} \bar {S}} - \Sigma_ {\bar {S} S} \Sigma_ {S S} ^ {- 1} \Sigma_ {S \bar {S}}.\tag{34}
$$

Now the algorithm to compute the SHAP parts can be formulated:

1: given dataset $\mathbf { X } _ { N \times M }$ , sample to explain x, model $f ,$ parameters $K _ { 1 }$ and $K _ { 2 }$

2: compute mean µ and covariance matrix Σ from $\mathbf { X } _ { N \times M }$

3: compute the conditional SHAP values $\phi _ { i }$ by applying Kernel SHAP, estimating every $E \big [ f ( X ) | X _ { S } = \pmb { x } _ { S } \big ]$ ≈ $\begin{array} { r } { \frac { 1 } { K _ { 2 } } \sum _ { k } f \left( \left[ \pmb { x } _ { S } , \pmb { x } _ { \bar { S } } ^ { k } \right] \right) } \end{array}$ with $x _ { \bar { S } } ^ { k }$ sampled from $\bar { \mathcal { N } ( \mu _ { \bar { S } | S } , \Sigma _ { \bar { S } | S } ) } .$

4: for $i = 0$ to M do

5: for k = 0 to K<sub>2</sub> do

$$
6: \quad R \leftarrow \text { Permutation } (\{1, 2, \dots M \})
$$

$$
7: \quad \text {   sample   } x _ {\bar {S ^ {R}}} ^ {0} \text {   from   } \mathcal {N} (\mu_ {\bar {S ^ {R}} | S ^ {R}}, \Sigma_ {\bar {S ^ {R}} | S ^ {R}})
$$

8: end for

$$
\begin{array}{r l} & {\mathrm{endfor}} \\ {9: \quad} & {\phi_ {i, i n t} \leftarrow \frac {1}{K _ {2}} \sum_ {R} f \left(\left[ \pmb {x} _ {S ^ {R}}, \pmb {x} _ {i}, x _ {S _ {i} ^ {- R}} ^ {0} \right]\right) - f \left(\left[ \pmb {x} _ {S ^ {R}}, x _ {S ^ {- R}} ^ {0} \right]\right)} \end{array}
$$

10: $\phi _ { i , d e p } \gets \phi _ { i } - \phi _ { i , i n t }$

11: end for

A lengthy description of the Kernel SHAP algorithm is available in [1]. Lines 4 to 9 compute the interventional SHAP parts in the same way as the normal SHAP values were computed in [24].

## Appendix B. Results non-linear model

Because of Equations (26) and (27), interpretation of the results with a linear model is more straightforward. For completeness’ sake, we shown the results with a nonlinear model here. The experiments of Figure 3 were repeated with a random forest in Figure 8. As discussed above, while the diferences between the approaches are less significant, they are still in line with the results for a linear model.

![](/api/attachments/YJ2D98Y2/fulltext/images/7c37307ba2999fc3d1f7ecbf0eab31ea1749d373862652c391f6d7a6a48045c0.jpg)  
(a)

![](/api/attachments/YJ2D98Y2/fulltext/images/ee4a2564ca723ee8c506169078bbb84032731b7c902414463cc7b3826633c4ad.jpg)  
(b)  
Figure 8: Change in house price when imputing selected features with respectively the regular mean (a) and the mean conditioned on the unchanged features (b). A random forest is used to predict the house price. The values are computed for 200 random towns and averaged.

## Appendix C. Interventions based on conditional SHAP values

In Figure 3 the green line represents the change in model output when intervening on the features with the most negative conditional SHAP values. Conditional SHAP values do not directly correspond with changes in model output when a feature gets replaced without changing other features. This is also why it fails the dummy property (14): even features who are not in the model formulation can still have a non-zero attribution. By extension, as shown in Figure 3, mean imputing a feature with a negative conditional SHAP (to attempt to remove the negative efect) can still decrease the model output. We will illustrate this with an example. Consider the following model and data

distribution:

$$
\begin{array}{c} f ([ X _ {1}, X _ {2} ]) = 1 0 0 X _ {1} - 1 0 0 0 X _ {2}, \\ [ X _ {1}, X _ {2} ] \sim \mathcal {N} \left([ 0, 0 ], \left[ \begin{array}{c c} 1 & 0. 5 \\ 0. 5 & 1 \end{array} \right]\right). \end{array}\tag{35}
$$

For sample $[ X _ { 1 } = 1 , X _ { 2 } = 1 ]$ we get:

$$
\begin{array}{c} \phi_ {1, i n t} = 7 5, \\ \phi_ {1, d e p} = - 2 5 0, \\ \phi_ {1} = 7 5 - 2 5 0 = - 1 7 5. \end{array}\tag{36}
$$

We see that $X _ { 1 } = 1$ has a very big negative SHAP value which is mostly due to its very big dependent SHAP part. If you would change $X _ { 1 }$ from 1 to the mean in an attempt to remove this big negative efect, the model output still decreases significantly. This is reflected by $\phi _ { 1 , i n t }$ which is positive and as we argue in Section 6.1 corresponds to the interventional changes to the model, in contrast with the conditional SHAP value.

## Appendix D. Significance of results

Contrary to regular machine learning practice the averages in Figure 3 and Figure 8 are not accompanied with standard deviations. This was a deliberate choice. Since some towns are very dificult to improve while others can be improved quite easily, the standard deviations are very large and make the results seem insignificant (see Figure 9). A better metric to judge the significance is the per town diference of both interventional approaches with conditional SHAP depicted in Figure 10 (for a linear model) and Figure 11 (for a random forest). Here, in addition to the mean we show the actual diferences for some towns instead of a standard deviation because these values are far from Gaussian. We can see a significant diference between the approaches.

## References

[1] Aas, K., Jullum, M., and Løland, A. (2021a). Explaining individ ual predictions when features are dependent: More accurate ap proximations to shapley values. Artificial Intelligence, 298:103502.

[2] Aas, K., Nagler, T., Jullum, M., and Løland, A. (2021b). Explaining predictive models using shapley values and non parametric vine copulas. Dependence Modeling, 9(1):62–81.

[3] Abid, F. and Izeboudjen, N. (2019). Predicting forest fire in algeria using data mining techniques: Case study of the decision tree algorithm. In International Conference on Advanced Intelligent Systems for Sustainable Development, pages 363–370. Springer.

[4] Blesch, K., Wright, M. N., and Watson, D. (2023). Unfooling shap and sage: Knockof imputation for shapley values. In World Conference on Explainable Artificial Intelligence, pages 131–146. Springer.

[5] Chen, H., Covert, I. C., Lundberg, S. M., and Lee, S.-I. (2023). Algorithms to estimate shapley value feature attributions. Nature Machine Intelligence, 5(6):590–601.

[6] Chen, H., Janizek, J. D., Lundberg, S., and Lee, S.-I. (2020). True to the model or true to the data? arXiv preprint arXiv:2006.16234.

![](/api/attachments/YJ2D98Y2/fulltext/images/940a535af929901c9ab4fc7d9a4ed88fc8afde1d76ae32b9c2dc461ccbf2eb80.jpg)  
Figure 9: Change in house price when mean imputing selected fea tures. A linear model is used to predict the house price. The values are computed for 200 random towns and averaged. The shaded re gion represents one standard deviation.

[7] Frye, C., de Mijolla, D., Begley, T., Cowton, L., Stanley, M., and Feige, I. (2020a). Shapley explainability on the data manifold. arXiv preprint arXiv:2006.01272.

[8] Frye, C., Rowat, C., and Feige, I. (2020b). Asymmetric shapley values: incorporating causal knowledge into model-agnostic explainability. Advances in Neural Information Processing Systems, 33:1229–1239.

[9] Harrison Jr, D. and Rubinfeld, D. L. (1978). Hedonic housing prices and the demand for clean air. Journal of environmental economics and management, 5(1):81–102.

[10] Heskes, T., Sijben, E., Bucur, I. G., and Claassen, T. (2020). Causal shapley values: Exploiting causal knowledge to explain individual predictions of complex models. Advances in Neural Information Processing Systems, 33.

[11] Janzing, D., Minorics, L., and Bl¨obaum, P. (2020). Feature relevance quantification in explainable ai: A causal problem. In International Conference on Artificial Intelligence and Statistics, pages 2907–2916. PMLR.

[12] Jiang, G., Zhuang, F., Song, B., Zhang, T., and Wang, D. (2023). Prishap: Prior-guided shapley value explanations for correlated features. In Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, pages 955–964.

[13] Kumar, I., Scheidegger, C., Venkatasubramanian, S., and Friedler, S. (2021). Shapley residuals: Quantifying the limits of the shapley value for explanations. Advances in Neural Informa tion Processing Systems, 34:26598–26608.

[14] Kumar, I. E., Venkatasubramanian, S., Scheidegger, C., and Friedler, S. (2020). Problems with shapley-value-based explanations as feature importance measures. In International Conference on Machine Learning, pages 5491–5500. PMLR.

[15] Lockwood, S. K., Nally, J. M., Ho, T., and Knutson, K. (2015). Racial disparities and similarities in post-release recidivism and employment among ex-prisoners with a diferent level of education. Journal of Prison Education and Reentry, 2(1):16–31.

[16] Lundberg, S. M., Erion, G. G., and Lee, S.-I. (2018a). Consistent individualized feature attribution for tree ensembles. arXiv preprint arXiv:1802.03888.

[17] Lundberg, S. M. and Lee, S.-I. (2017). A unified approach to interpreting model predictions. In Advances in Neural Information Processing Systems, pages 4765–4774.

[18] Lundberg, S. M., Nair, B., Vavilala, M. S., Horibe, M., Eisses, M. J., Adams, T., Liston, D. E., Low, D. K.-W., Newman, S.-F., Kim, J., et al. (2018b). Explainable machine-learning predictions

for the prevention of hypoxaemia during surgery. Nature Biomed ical Engineering, 2(10):749.

[19] Olsen, L. H. B., Glad, I. K., Jullum, M., and Aas, K. (2024). A comparative study of methods for estimating model-agnostic shapley value explanations. Data Mining and Knowledge Discovery, pages 1–48.

[20] Ribeiro, M. T., Singh, S., and Guestrin, C. (2016). ” why should i trust you?” explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining, pages 1135–1144.

[21] Rossi, R. C., Vanderlei, L. C. M., Gon¸calves, A. C. C. R., Van derlei, F. M., Bernardo, A. F. B., Yamada, K. M. H., da Silva, N. T., and de Abreu, L. C. (2015). Impact of obesity on autonomic modulation, heart rate and blood pressure in obese young people. Autonomic neuroscience, 193:138–141.

[22] Shapley, L. S. (1953). A value for n-person games. Contributions to the Theory of Games, 2(28):307–317.

[23] Slack, D., Hilgard, S., Jia, E., Singh, S., and Lakkaraju, H. (2020). Fooling lime and shap: Adversarial attacks on post hoc explanation methods. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, pages 180–186.

[24] Strumbelj, E. and Kononenko, I. (2014). Explaining predic-<sup>ˇ</sup> tion models and individual predictions with feature contributions. Knowledge and information systems, 41(3):647–665.

[25] Sundararajan, M., Dhamdhere, K., and Agarwal, A. (2020). The shapley taylor interaction index. In International conference on machine learning, pages 9259–9268. PMLR.

[26] Sundararajan, M. and Najmi, A. (2020). The many shapley val ues for model explanation. In International Conference on Machine Learning, pages 9269–9278. PMLR.

[27] Takeishi, N. (2019). Shapley values of reconstruction errors of pca for explaining anomaly detection. In 2019 International Conference on Data Mining Workshops (ICDMW), pages 793– 798. IEEE.

[28] Taufiq, M. F., Bl¨obaum, P., and Minorics, L. (2023). Manifold restricted interventional shapley values. In International Conference on Artificial Intelligence and Statistics, pages 5079–5106. PMLR.

[29] Wang, J., Wiens, J., and Lundberg, S. (2021). Shapley flow: A graph-based approach to interpreting model predictions. In International Conference on Artificial Intelligence and Statistics, pages 721–729. PMLR.

[30] Yeh, C.-K., Lee, K.-Y., Liu, F., and Ravikumar, P. (2022). Threading the needle of on and of-manifold value functions for shapley explanations. In International Conference on Artificial Intelligence and Statistics, pages 1485–1502. PMLR.

![](/api/attachments/YJ2D98Y2/fulltext/images/2430741f6d0b174984101a29c2e9ac2cd6d7ec8d2cc5cdfce3903fe3d394a295.jpg)  
(a)

![](/api/attachments/YJ2D98Y2/fulltext/images/3797d7e58aa3e219f5066be950295fc0814523e63e8d348e3dceb31047190178.jpg)  
(b)  
Figure 10: The per town diference of both interventional approaches with conditional SHAP when imputing selected features with re spectively the regular mean (a) and the mean conditioned on the unchanged features (b). A linear model is used to predict the house price. The mean over 200 towns is a solid line. For ten randomly selected towns, actual diferences are plotted (see-through lines).

![](/api/attachments/YJ2D98Y2/fulltext/images/04661f7d30c632f6a57e68f1e04403762812e98616fd80c06d70b547b0e2da55.jpg)  
(a)

![](/api/attachments/YJ2D98Y2/fulltext/images/e39a8fa2587fa2ab048ced7e77e62f9b5408befea8321c2f5c3cc38d04fdb781.jpg)  
(b)  
Figure 11: The per town diference of both interventional approaches with conditional SHAP when imputing selected features with respec tively the regular mean (a) and the mean conditioned on the un changed features (b). A random forest is used to predict the house price. The mean over 200 towns is a solid line. For ten randomly selected towns, actual diferences are plotted (see-through lines).
