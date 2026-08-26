---
otero_id: 2426
otero_key: "NAH5DD8H"
title: "Forecasting remaining useful life: Interpretable deep learning approach via variational Bayesian inferences"
authors: "Mathias Kraus; Stefan Feuerriegel"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113100"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Forecasting remaining useful life: Interpretable deep learning approach via variational Bayesian inferences

Mathias Kraus<sup>\*</sup>, Stefan Feuerriegel

![](/api/attachments/NAH5DD8H/fulltext/images/514ee7a2348a6b8d9b127e01e425ee8aaff0c9184cb76163d6bdaf5f58eb373f.jpg)

ETH Zurich, Weinbergstr. 56/58, Zurich 8092, Switzerland

## A R T I C L E I N F O

Keywords: Forecasting Remaining useful life Machine learning Neural networks Deep learning

## A B S T R A C T

Predicting the remaining useful life of machinery, infrastructure, or other equipment can facilitate preemptive maintenance decisions, whereby a failure is prevented through timely repair or replacement. This allows for a better decision support by considering the anticipated time-to-failure and thus promises to reduce costs. Here a common baseline may be derived by fitting a probability density function to past lifetimes and then utilizing the (conditional) expected remaining useful life as a prognostic. This approach finds widespread use in practice because of its high explanatory power. A more accurate alternative is promised by machine learning, where forecasts incorporate deterioration processes and environmental variables through sensor data. However, machine learning largely functions as a black-box method and its forecasts thus forfeit most of the desired interpretability. As our primary contribution, we propose a structured-efect neural network for predicting the remaining useful life which combines the favorable properties of both approaches: its key innovation is that it ofers both a high accountability and the flexibility of deep learning. The parameters are estimated via varia tional Bayesian inferences. The diferent approaches are compared based on the actual time-to-failure for aircraft engines. This demonstrates the performance and superior interpretability of our method, while we finally discuss implications for decision support.

## 1. Introduction

Maintenance of physical equipment, machinery, systems and even complete infrastructure represents an essential process for ensuring successful operation. It helps in minimizing downtime of technical equipment [1], eliminate the risk thereof [2], or prolong the life of systems [3]. Maintenance is often enforced by external factors, such as regulations or quality management [4]. Yet maintenance burdens in dividuals, businesses and organizations with immense costs. For in stance, the International Air Transport Association (IATA) reported that maintenance costs of 49 major airlines increased by over 3% from 2012 to 2016, finally totaling \$15.57 billion annually.<sup>1</sup>

Decision support in maintenance can be loosely categorized according to two diferent objectives depending on whether they serve a corrective or preemptive purpose.<sup>2</sup> The former takes place after the failure of machinery with the goal of restoring its operations back to normal. Conversely, preemptive maintenance aims at monitoring these operations, so that the time-to-failure can be predicted and acted upon in order to mitigate potential causes and risk factors by, for instance, replacing deteriorated components in advance. Preemptive actions help in reducing downtime and, in practice, promise substantial financial savings, thus constituting the focus of this paper.

Preemptive maintenance is based on estimations of the remaining useful life (RUL) of the machinery. While preventive maintenance makes these forecasts based on human knowledge, predictive maintenance utilizes data-driven models. Diferent models have been proposed that can be categorized by which input data is utilized (see Section 2 for an overview). In the case of raw event data, the conven tional approach involves the estimation of probability density functions. If sensor data is available, the prominent approach draws upon machine learning models [8, 9]. The latter fosters non-linear relationships between sensor observations and RUL estimates, which aid in obtaining more accurate forecasts.

Machine learning models are subject to an inherent drawback: they frequently operate in a black-box fashion [10-12], which, when providing decision support, directly impedes potential insights into the underlying rules behind their decision-making. However, interpretability is demanded for a variety of practical reasons. For instance, practitioners desire to benchmark predictive models with their own expertise, as well as to validate the decision-making rules from machine learning models against common knowledge [13]. Further, managers can identify potential causes of a short machine lifetime and, thus, outline means by which to reduce errors [14]. Moreover, accountability in RUL forecasts is sometimes even required by regulatory agencies, such as, e.g., in aircraft or railroad maintenance [e.g. 15, 16].

Interpretability refers to machine learning models where the decision logic of the model itself is transparent. Notably, the concept of interpretability difers from post-hoc explainability that aims for a different objective. Here, a single (or multiple random) forecast is de composed, thus highlighting potential relationships but without any structural guarantees [17]. That is, explainability takes an arbitrary model as input and, based on it, attempts to unravel the decision logic behind it, but does so only for a local neighborhood of the input rather than deriving its actual structure. Hence, post-hoc explanations are often not reliable, result in misleading outputs and, because of that, the need for interpretable machine learning has been named an important objective for safety-aware applications [18]. By constructing models that are inherently interpretable, practitioners obtain insights into the underlying mechanisms of the model [19]. In keeping with this, we formulate our research objective as follows.

OBJECTIVE: Forecasting remaining useful life via machine learning with the additional requirement that the model fulfills the definition of “interpretability” .

We develop interpretable deep learning models for forecasting RUL as follows: we propose a novel structured-efect neural network that represents a viable trade-of between attaining accurate forecasts and the interpretability from simple distributional estimations. In order to estimate its parameters, we develop an innovative estimation technique based on variational Bayesian inferences that minimize the Kullback-Leibler divergence.<sup>3</sup>

We demonstrate the efectiveness of our approach in terms of interpretability and prediction performance as follows. We utilize the public “ Turbofan Engine Degradation Simulation” dataset [20] with sensor measurements from aircraft engines. This dataset is widely referred to as a baseline for comparing predictive models in maintenance and RUL predictions; see e.g., Butcher et al. [21] and Dong et al. [22]. Here the goal is to forecast the remaining useful life until irregular operations, such as breakdowns or failures, take place. The proposed structured-efect neural network outperforms the distribution-based approaches, reducing the forecast error by 51.60 %. While our approach is surpassed slightly by deep learning, it fulfills the definition of being interpretable, i.e., it maintains the same accountability as the much simpler probabilistic approaches.

The remainder of this paper is structured as follows. Section 2 provides an overview on predicting remaining useful life for preemptive maintenance. Section 3 then introduces our methodological framework consisting of probabilistic approaches, machine learning and the novel structured-efect neural network that combines the desirable properties of both. The resulting performance is reported in Section 4, where we specifically study the interpretability of the diferent approaches. Finally, Section 5 concludes with a discussion of our findings and implications of our work with respect to decision support.

## 2. Background

Previous research has developed an extensive range of mathema tical approaches in order to improve maintenance and, due to space constraints, we can only summarize core areas related to our work in the following. For detailed overviews, we refer to Heng et al. [6], Liao and Kottig [23], Navarro and Rychlik [24] and Si et al. [7], which provide a schematic categorization of run-to-failure, condition monitoring and predictive methods that estimate the remaining useful life of the machinery. Depending on the underlying approach, the resulting strategy can vary between corrective, responsive, or preemptive maintenance operations. Predictive maintenance, in particular, gives rise to a multitude of variants, e.g., probabilistic approaches and fully data-driven methods that rely upon machine learning together with granular sensor data. The intuition behind inserting sensor measurements into predictive models is that the latter can quantify the environment numerically, the operations and the potential deterioration [25]. The observed quantities can be highly versatile and include vibration, oil analysis, temperature, pressure, moisture, humidity, loading, speed, and environmental efects [7]. As such, sensor measurements are likely to supersede pure condition-based signals in their contribution to overall prognostic capability.

In order to carry out preemptive measures, one estimates the remaining useful life (RUL) and then applies a suitable strategy for scheduling maintenance operations (such as a simple threshold rule that triggers a maintenance once RUL undercuts a safety margin) in a costeficient manner [16, 26, 27]. Mathematically, the RUL at time t can be formalized as a random variable Y that depends on the operative environment and its past use $X _ { t } , . . . , X _ { 2 } , X _ { 1 } , \mathrm { i . e . }$ ,

$$
\mathbb {E} \left[ Y _ {t} | X _ {t},..., X _ {2}, X _ {1} \right].\tag{1}
$$

Here the variables $X _ { 1 } , . . . , X _ { t }$ can refer to event data tracking past failures [28], numerical quantities tracing the machines condition over time as an early warning of malfunctioning [7], or measurements of its use as a proxy for deterioration [24].

## 2.1. Probabilistic lifetime models

Probabilistic models utilize knowledge about the population of machinery by learning from the sensor observations of multiple machines. This knowledge is obtained by utilizing predefined probability density functions that specify the probability distributions over machinery lifetimes. Mathematically, when X is not available, the RUL estimation turns into $\begin{array} { r } { \mathbb { E } \left[ Y _ { t } | X _ { t } , . . . , \dot { X } _ { 2 } , X _ { 1 } \right] = \mathbb { E } \left[ Y _ { t } \right] = \frac { \mathbb { E } \left[ t + Y _ { t } \right] } { R ( t ) } } \end{array}$ , where R(t) is the survival function at t. Common choices include exponential, loglogistic, log-normal, gamma, and Weibull distributions [e.g. 6] . We refer to [24] for a detailed survey. For instance, the Weibull distribution has been found to be efective even given few observations of lifetimes, which facilitates its practical use [29]. Both log-normal and Weibull distributions can be extended by covariates for sensor-data, which we describe below in Section 3.5 but are then constrained to the mathematical structure, rather than flexibility when calibrating a data-driven approach through machine learning.

Probabilistic approaches are common choices as they benefit from straightforward use, direct interpretability and reliable estimates, that are often required in practical applications and especially by the regulatory body. However, a focus is almost exclusively placed on raw event data, thereby ignoring the prognostic capacity of sensor data.

Probabilistic approaches can theoretically be extended to accommodate sensor data, resulting in survival models. Since its initial proposal by [30], the proportional hazards model has been popular for lifetime analysis in general [31] and the estimation of RUL in particular. A key advantage of the proportional hazards model over many other approaches is that the interaction between a number of influencing factors can be easily combined with a baseline function that describes the general lifetime of the machinery. More precisely, the proportional hazards model assumes that the probability estimates consist of two components, namely, a structural efect and random efects described by covariates [7]. As will be discussed later, our structuredefect neural network is built on a similar idea; however, it exploits deep learning to increase the predictive power of the RUL in contrast to the proportional hazards model, which utilizes an exponential model to describe the random efect.

## 2.2. Machine learning in lifetime predictions

Machine learning has recently received great traction for RUL as the flexibility of these models facilitates a superior prognostic capacity. For instance, linear regression models ofer the advantage of high interpretability when predicting RUL. Extensions by regularization yield the lasso and ridge regression, which have been found to be efective for high-dimensional sensor data [32]. To overcome the limitations of linear relationships, a variety of non-linear models have been utilized, including support vector regression [8], random forests [9], and neural networks [33]. We refer to Heng et al. [6] and Si et al. [[7]] for a detailed overview of the proposed models. However, non-linear models generally fall short in terms of their explanatory power [10].

Even though machine learning demonstrates high predictive power, these models struggle with the nature of sensor data as time series. It is common practice to make RUL estimates based purely on the sensor data at one specific point in time [7]. This simplifies $\mathbb { E } \left[ Y _ { t } | X _ { t } , . . . X _ { 1 } \right]$ to $\mathbb { E } \left[ Y _ { t } | X _ { t } \right] ,$ thereby ignoring the past trajectory of sensor measurements. Yet the history of sensor measurements is likely to encode valuable information regarding the past deterioration and usage of machinery. As an intuitive example, a jet engine that experiences considerable vibration might require more frequent check-ups. As a remedy, feature engineering has been proposed in order to aggregate past usage profiles onto feature vectors that are then fed into the machine learning model [34]. Formally, this yields $\mathbb { E } \left[ Y _ { t } | \phi ( X _ { t } , . . . , X _ { 1 } ) \right]$ or $\mathbb { E } \left[ Y _ { t } | X _ { t } , \phi ( X _ { t - 1 } , . . . , X _ { 1 } ) \right]$ , where the aggregation function ϕ could, for in stance, extract the maximum, minimum, or variability from a sensor time series. As a result, the features could theoretically be linked to interpretations but this is largely prohibited by the nature of the machine learning model.

Advances from deep neural networks have only recently been uti lized for the prediction of RUL. In Babu et al. [35] , the authors apply convolutional neural networks along the temporal dimension in order to incorporate automated feature learning from raw sensor signals and predict RUL. In other works, long short-term memory networks (LSTMs), as a prevalent form of recurrent neural networks, have been shown to perform superior to traditional statistical probability regression methods in predicting RUL [22, 36, 37]. Thereby, the LSTM can make use of the complete sequence of sensor measurements by processing complete sequences with the objective of directly estimating the formula $[ Y _ { t } | X _ { t } , . . . , X _ { 1 } ]$ with varying, machine-dependent t. In addition, LSTMs entail a high degree of flexibility, which helps to accurately model highly non-linear relationships. This commonly lowers the forecast error, which further translates into improved maintenance operations.

Deep neural networks are rarely utilized in practical applications for a variety of reasons. Arguably, this is not only because deep neural networks have only recently begun to be used for estimating RUL, but also because they are widely known to be black-box functions with limited to no interpretability. Hence, it is the contribution of this paper to develop a combination of structural predictions and deep learning in order to reach a favorable trade-of between interpretability and prognostic capacity. As points of comparison, we draw upon previous works for RUL predictions, including those concerned with machine learning, feature engineering, and deep learning.

## 2.3. Verification in machine learning

Interpretability of machine learning is particularly important in mission-critical systems, which requires the development of assessment techniques that reliably identify unlikely types of error [56]. One approach to uncovering cases where the model may be incompatible with the desired behavior is to systematically search for worst-case results during evaluation [e.g. 57]. Formal verification proves that machine learning models are specification consistent [e.g. 58]. While the field of formal verification has been subject to research, these approaches are impeded by limited scalability, especially in response to modern deep learning systems.

## 2.4. Explainable vs. interpretable machine learning

Explainable machine learning refers to post-hoc explaining predic tions without elucidating the mechanisms with which models work. Examples of such post-hoc interpretations are local linear approximation of the model's behavior [e.g. partial dependence plots; see 38] or decompositions of the final prediction into the contribution of each input feature [e.g. SHAP values; see 39]. Another widely applied approach to obtaining explanations is to render visualizations to determine qualitatively what a model has learned [40]. However, explainable machine learning is limited in understanding the underlying process of estimation. Notably, it is also limited to a local neighborhood of the input space or the prediction.

In contrast, interpretable machine learning is to encode an interpretable structure a priori, which allows looking into their mechanisms in order to understand the complete functioning of predictions for all possible input features [41]. Here global relationships are directly encoded in the structure of the model. As such, the relationship in individual features or outcomes for average cases is explicitly modeled. Naturally, linear models have become a prevalent choice for applications in (safety-)critical use cases, where a complete traceability of the model's estimation is inevitable. Hence, the estimation (rather than predictions) can now be compared against prior knowledge or used for obtaining insights.

## 3. Methods

This research aims at developing forecasting models for the remaining useful life that, on the one hand, obtain a favorable out-ofsample performance while achieving a high degree of interpretability at the same time. Hence, this work contributes to the previous literature by specifically interpreting the relevance of diferent sensor types and usage profiles in relation to the overall forecast. To date, probabilistic models of failure rates have been widely utilized for predicting the remaining useful life due to their exceptional explanatory power. We thus take the interpretable feature of this approach and develop a method that combines it with the predictive accuracy of deep learning.

We compare the forecasting performance of our structured-efect neural network with the following approaches: (i) naïve empirical estimations, (ii) probabilistic approaches, (iii) traditional machine learning, (iv) traditional machine learning with feature engineering for time series applications, and (v) deep neural networks. All of the aforementioned methods are outlined in the following.

## 3.1. Naïve empirical estimation of remaining useful life

Naïve empirical estimation of remaining useful life describes the approximation of RUL utilizing past lifetimes of the machinery. Let Z denote the random variable referring to the total lifetime of a machinery, and let $Z _ { 1 } , . . . , Z _ { n }$ denote n realizations of this random variable. Then we utilize the mean of these realizations to estimate the total lifetime of a machinery, i.e.,

<table><tr><td>Approach</td><td>Decision variable</td><td>Input variables</td><td>Maintenance strategy</td><td>Operationalization</td></tr><tr><td>Run-to-failure</td><td>—</td><td>—</td><td>Corrective</td><td>Service on failure</td></tr><tr><td>Condition monitoring</td><td>Latent state</td><td>Event/sensor data</td><td>Responsive</td><td>Service when latent state indicates (upcoming) failure</td></tr><tr><td>Physics-based RUL models</td><td>Physics-based RUL</td><td>Simulation models</td><td>Preemptive</td><td>Service when RUL reaches predefined threshold</td></tr><tr><td>Probabilistic RUL models</td><td>Population-wide (or conditional) RUL</td><td>Event data</td><td>Preemptive</td><td>Service when RUL reaches predefined threshold</td></tr><tr><td>Sensor-based RUL predictions (e.g., proportional hazards model, machine learning)</td><td>System-specific RUL</td><td>Sensor data</td><td>Preemptive</td><td>Service when RUL reaches predefined threshold</td></tr></table>

$$
\mathbb {E} [ Z ] = \frac {1}{n} \sum_ {i = 1} ^ {n} Z _ {i}.\tag{2}
$$

We can now translate this estimation of the total lifetime into an estimation of the RUL by subtracting the time the machinery has been in use since last being maintained. Let $Y _ { t }$ denote the random variable that describes the RUL of a machinery at time t. Then we estimate $Y _ { t }$ by

$$
\mathbb {E} \left[ Y _ {t} \right] = \mathbb {E} \left[ Z \right] - t.\tag{3}
$$

## 3.2. Probabilistic lifetime models

In accordance with our literature review, we draw upon two prominent probability density functions P that model the lifetime expectancy of machinery, namely, the Weibull distribution, and the lognormal distribution [e.g. 42]. Let, again, Z denote the random variable referring to the total lifetime of the population. Then the probability density functions of the Weibull distribution and the log-normal distribution at time step $t > 0$ are given by

$$
P _ {\mathrm{Weibull}} (Z; a, b) = \frac {a}{b} \bigg (\frac {Z}{a} \bigg) ^ {b - 1} e - (\frac {Z}{a}) ^ {b} \quad \mathrm{and}\tag{4}
$$

$$
P _ {\mathrm{log-normal}} (Z; a, b) = \left\{\frac {1}{\sqrt {2 \pi} b Z} e - \frac {(\log (Z) - a) ^ {2}}{2 b ^ {2}}, \quad Z > 0, 0, \right.\tag{\(Z \leq 0\),}
$$

(5)

respectively, with distribution parameters a and b. All distribution parameters are estimated based on past event data; more precisely, the historical time-spans between failures of the machinery are inserted as the lifetime Z. This allows us to estimate the expected lifetime of the machinery after a maintenance event, as well as the corresponding variance.

The mean value of the diferent probability density functions could provide estimates of the remaining useful life for unseen data observations. However, this would ignore the knowledge that the machine has already functioned over t time steps. Hence, we are interested in the conditional expectation, given that the machine had the last maintenance event t time steps ago. This results in an estimated RUL at time t of

$$
\mathbb {E} \left[ Y _ {t} \right] = \mathbb {E} _ {Z \sim P} [ Z | Z > t ] - t.\tag{6}
$$

To compute the previous expression, we draw upon the cumulative distribution function F(Z;⋅) and the definition of the conditional prob ability. We then rewrite 6 into

$$
\mathbb {E} \left[ Y _ {t} \right] = \mathbb {E} _ {Z \sim P} [ Z | Z > t ] - t = \mathbb {E} _ {Z \sim P} \left[ \frac {Z}{1 - F (Z ; \cdot)} \right] - t.\tag{7}
$$

Unfortunately, there is no (known) closed-form solution to the expected conditional probability of a Weibull distribution. Hence, we utilize Markov chain Monte Carlo to approximate Eq.(7) for both, the Weibull distribution and the log-normal distribution, in order to come up with the expected remaining lifespan (conditional on the time of the last maintenance event).

## 3.3. Traditional machine learning

In the following, let f refer to the diferent machine learning models with additional parameters w. Then, in each time step t, the machine learning model f is fed with the current sensor data $X _ { t }$ and computes the predicted RUL, given by $\widetilde { Y } _ { t } = f ( X _ { t } ; w )$ , such that $Y _ { t } \approx { \widetilde { Y } } _ { t } .$ The deviation between the true RUL, $Y _ { t } ,$ and the forecast $\widetilde { Y } _ { t }$ defines the prediction error that we try to minimize. Hence, the optimal parameters can be determined by an optimization problem

$$
w ^ {*} = \operatorname{argmin} _ {w} | | Y _ {t} - f (X _ {t}; w) | |.\tag{8}
$$

A variety of models f are common in predicting remaining useful life; see the surveys in Heng et al. [6] and Si et al. [7]. We adhere to previous choices and thus incorporate a variety of baseline models that consist of both linear and non-linear models. Linear models include ridge regression, lasso, and elastic net, all of which are easily interpretable and have been shown to perform well on many machine learning tasks with high-dimensional and even collinear features [43]. The set of non-linear baseline models includes random forest and sup port vector regression (SVR).

Table 2  
Our feature engineering draws upon the above aggregation which is later set to 50 in accordance with previous research. The expressions loc max and loc min refer to the local maximum and minimum of the inputs.

<table><tr><td>Aggregation function</td><td>Formula</td><td>Interpretation</td></tr><tr><td>Max</td><td> $\max(X_1, ..., X_t)$ </td><td>Extrema</td></tr><tr><td>Min</td><td> $\min(X_1, ..., X_t)$ </td><td>Extrema</td></tr><tr><td>Mean</td><td> $\mu = \frac{1}{t} \sum_{i=1}^{t} X_i$ </td><td>Average sensor measurement</td></tr><tr><td>Range</td><td> $\max - \min$ </td><td>Variability</td></tr><tr><td>Sum</td><td> $\sum_{i=1}^{t} X_i$ </td><td>Total signal</td></tr><tr><td>Energy</td><td> $\sum_{i=1}^{t} X_i^2$ </td><td>Total signal with focus on peaks</td></tr><tr><td>Standard deviation</td><td> $\sigma = \sqrt{\frac{1}{t} \sum_{i=1}^{t} (X_i - \mu)^2}$ </td><td>Variability</td></tr><tr><td>Skewness</td><td> $\frac{1}{t} \sum_{i=1}^{t} \left( \frac{X_i - \mu}{\sigma} \right)^3$ </td><td>Symmetry of deviation</td></tr><tr><td>Kurtosis</td><td> $\frac{1}{t} \sum_{i=1}^{t} \left( \frac{X_i - \mu}{\sigma} \right)^4$ </td><td>Infrequent extreme deviations</td></tr><tr><td>Peak-to-peak</td><td> $\frac{1}{n_1} \sum_{i=1}^{n_1} \text{loc max} + \frac{1}{n_2} \sum_{i=1}^{n_2} \text{loc min}$ </td><td>Bandwidth</td></tr><tr><td>Root mean square</td><td> $\sqrt{\frac{1}{t} \sum_{i=1}^{t} X_i^2}$ </td><td>Total load focus on peaks</td></tr><tr><td>Entropy</td><td> $- \sum_{i=1}^{t} P(X_i) \log P(X_i)$ </td><td>Information signal</td></tr><tr><td>Arithmetic mean of power spectral density</td><td> $20 \log_{10} \frac{\frac{1}{t} \sum_{i=1}^{t} \text{fft}(X_i)}{10^{-5}}$ </td><td>Frequency of oscillations</td></tr><tr><td>Line integral</td><td> $\sum_{i=1}^{t-1} |X_{i+1} - X_i|$ </td><td>Path length</td></tr><tr><td>Kalman filter</td><td> $Y_t - b - \sum_{i=1}^{p} a_i X_{t-i}$ </td><td>Unexpected deviation</td></tr></table>

All models are then fed with two diferent sets of features: (1) We take the current sensor measurements $X _ { t }$ when predicting the RUL estimate $Y _ { t } .$ However, this approach ignores the trajectory of historic sensor data. (2) As a remedy, we rely upon feature engineering as a means of condensing the past time series into a feature vector, as described in the following.

Feature engineering provides a means by which to encode the past usage of machinery into an input vector for the predictive model. Yet previous research has only little guidance at hand regarding what type of features are most useful. Hence, we adapt the choice of aggregation functions from Mosallam et al. [34], as detailed in Table 2. For instance, vibration is known to accelerate deterioration, but it is unclear whether this is caused by sudden peaks (i.e., minima or maxima), frequent changes $( \mathrm { i . e . } _ { \cdot }$ , standard deviation), or a constantly high tremor $( \boldsymbol { \mathrm { i . e . } } ,$ average). Mathematically, each aggregation function $\phi$ takes a sequence of past sensor measurements $X _ { t } , . . . , X _ { 1 }$ as input and then computes a new input feature $\phi ( X _ { t } , . . . , X _ { 1 } )$ . These aggregation functions are necessary to map the complete trajectory onto a fixed, predefined number of features that can be readily processed by the machine learning models.

To determine the best hyperparameter combination in traditional machine learning, we implemented group 10-fold cross-validation in order to minimize the bias associated with random sampling of training and validation data. The group approach also ensures that we do not split maintenance cycles during cross-validation and that the same maintenance cycle is not present in both the training and validation set.

## 3.4. Recurrent neural network

Recurrent neural networks refer to a special class of deep neural networks that can learn from sequences of varying lengths, rather than a fixed size of feature vector [Goodfellow et al. 44]. This is beneficial to our setting, as it allows us to directly inject time series with sensor data into the RNN and predict the remaining useful life from it. The math ematical formalization is as follows: let $f _ { \mathrm { N N } }$ denote a traditional (or deep) neural network that defines a mapping $[ X _ { t } , h _ { t - 1 } ] \mapsto h _ { t }$ with hidden states $h _ { t - 1 } , h _ { t } \in \mathbb { R } ^ { n }$ and a suitably chosen dimension n. Then a prediction from a complete sequence can be made via

$$
R N N _ {\Theta} = f _ {\mathrm{NN}} ([ X _ {t}, f _ {\mathrm{NN}} ([ X _ {t - 1}, \dots f _ {\mathrm{NN}} ([ X _ {1}, 0 _ {n} ]) ]) ]).\tag{9}
$$

In other words, the RNN iterates over the sequence, while updating it hidden state $h _ { t } ,$ which summarizes the already-seen sequence, similar to an internal state. This recurrent relationship between the states introduces the possibility of passing information onwards from the current state $h _ { t }$ to the next $h _ { t + 1 }$ . Therefore, RNNs can process sequences of arbitrary length, making them capable of utilizing the complete trajectory of sensor data. To illustrate this, Fig. 1 presents the processing of sequential data by means of unrolling the recurrent structure.

Diferent variants of recurrent neural networks have been proposed in earlier research; see [44]. In this work, we choose the long short-term memory from [45] because it is capable to keep information over long sequences, and it enjoys widespread use in research and practical applications [46-48]. For deep neural networks, we reduce the computational runtime for hyperparameter tuning and instead follow conventional guidelines, whereby a random sample of the training data ( 10%) serves for validation.

## 3.5. Proposed structured-efect neural network

## 3.5.1. Model specification

We now propose our structured-efect model. This approach en forces a specific structure that lends to intuitive interpretation. More precisely, it combines non-parametric approaches for modeling the expected RUL through a probabilistic density function with the flexibility of machine learning in order to incorporate sensor measurements and thus capture the heterogeneity from machine-specific deterioration processes.

![](/api/attachments/NAH5DD8H/fulltext/images/154cb6b8695954e74019ea83d6994b075b6c6686223af1c27e01b6970311ef31.jpg)  
Fig. 1. Recurrent neural network that recursively applies the same simple neural network $f _ { \mathrm { N N } }$ to the input sequence $X _ { 1 } , . . . , X _ { t }$ with outputs $o _ { 1 } , . . . , o _ { t }$ The states $h _ { 1 : }$ $\ldots , h _ { t - 1 }$ encode the previous sequence into a fixed-size feature vector.

The idea of building structured models loosely resembles earlier research eforts related to proportional hazards models [30] that present a popular choice in lifetime analysis. This class of survival models decomposes its estimations into components referring to the baseline function and a function of covariates: the baseline specifies the general lifetime across all machines via the same function $\lambda ( t )$ . The latter fur ther assumes machine-specific efects through additional covariates that describe the random efects. Our structured-efect neural network follows a similar intuition, as it assumes a population-wide general lifetime common across all machines and further sensor-based deviations in order to model the within-machine heterogeneity due to the diferent usage profiles.

Our structured-efect model splits the estimated remaining useful life into three components, namely, a non-parametric baseline, a covariate-based prediction, and a recurrent component which specifically incorporates the historic trajectory of sensor measurements. These components help in explaining the variance among the diferent machine lifetimes and, for this purpose, we again draw upon the history of sensor measurements $X _ { t } , . . . , X _ { 1 } ,$ . Let λ(t) denote the non-parametric part with the explicit probabilistic lifetime model and let further $R N N _ { \Theta }$ refer to a recurrent neural network (such as a long short-term memory) with weights Θ. Then the prediction of the structured-efect neural network $S E N N _ { \Theta } ( t ; X _ { t } , . . . , X _ { 1 } )$ follows the form

with distribution parameters a and b. Thus, the first component is identical to the probabilistic lifetime models that we utilize as part of our benchmarks. Second, the linear component can either be fed directly with $X _ { t } \mathrm { o r } ,$ alternatively, one could also apply feature engineering to it, i.e., giving $\phi ( X _ { t } , . . . , X _ { 1 } )$ . The benefit of the latter is that we again obtain a linear structure where one can assess the relevance of individual predictors by looking at the coeficients. Here we further assume a linear combination as used in ordinary least squares and, as an extension, introduce priors, so that we yield a regularization, where the coeficients in the linear component are estimated via the least absolute shrinkage operator (lasso). This performs implicitly variable selection in the linear component as some coeficients are directly set to zero [49]. Third, the recurrent neural network is implemented via a long short-term memory as this represents the state-of-the-art in sequence learning [44].

## 3.5.2. Model estimation through variational Bayesian inferences

We now detail how we estimate the parameters inside the structured-efect neural network. We refer to θ as the combined set of unknown parameters and X as the overall dataset including all sensor measurements. Then the objective is to determine the optimal parameters

$$
\theta^ {*} = \operatorname{argmax} _ {\theta} P (\theta \mid X).\tag{12}
$$

We solve the previous optimization problem through a variational Bayesian method. The predominant reason for this choice over traditional optimization is that the latter would merely give point estimates

$$
S E N N _ {\Theta} (t; X _ {t}, \dots , X _ {1}) = \underbrace {\lambda (t)} _ {\text { Non - parametric   componentwith   explicit   lifetime   model }} + \underbrace {\beta^ {T} X _ {t}} _ {\text { Linear   componentwith   current   condition }} + \underbrace {R N N _ {\Theta} (X _ {t} , \dots , X _ {1} , t)} _ {\text { Recurrent   componentwith   deep   neural   network }}\tag{10}
$$

with coeficients β. Model variations are discussed later in Section 4.5.

While our model follows a similar intuition behind the proportional hazards model in decomposing the prediction, it also reveals clear diferences, as it introduces a recurrent neural network that allows for considerably higher flexibility in modeling the variance and even incorporates the complete sequence of sensor measurements and not just a simple vector of covariates. Moreover, the specific way of our model formulation entails a set of further advantages. On the one hand, it circumvents again the explicit need for feature engineering. On the other hand, it achieves a beneficial trade-of between interpretability of non-parametric approaches and the flexibility of non-linear predictions from sensor data. Here the deep neural network needs to explain a considerably smaller variance compared to an approach based solely on a neural network, thereby facilitating the estimation of the network weights. To this end, practitioners can decompose the prediction into a population-wide baseline and machine-specific heterogeneity, based on which they can explicitly quantify the relative contribution of each components through the corresponding coeficients. As such, one can identify reasons why the remaining useful life attains a certain value (e.g., a negative value from the recurrent component indicates a strong deterioration over time) or one can attribute deterioration to unexpected behavior. Moreover, the proposed approach is highly extensible and can easily be generalized to other parameterizations or domains.

We later experiment with diferent variations of the structured-ef fect model. These difer in the choices with which we specify the dif ferent components. First, we adhere to conventional approaches in predictive maintenance [24] by assuming that the lifetimes follow either a conditional Weibull or a conditional log-normal distribution. That is, we obtain

$$
\lambda (t) = \mathbb {E} _ {Z \sim \mathrm{Weibull} (a, b)} [ Z | Z > t ] - t \quad \text { and } \quad \lambda (t) = \mathbb {E} _ {Z \sim \mathrm{log-normal} (a, b)} [ Z | Z > t ] - t\tag{11}
$$

of the diferent parameters, whereas variational Bayesian inferences yield quantifications of uncertainty. For instance, this allows us to obtain confidence assessments concerning the relative importance of the diferent components and thus facilitates the interpretability of our approach.

In our model estimation, we treat all parameters as latent variables with a pre-defined prior distribution and, subsequently, maximize the overall likelihood of the parameters according to the following procedure. That is, utilizing Bayes' theorem, Eq.(12) is rewritten to

$$
P (\theta \mid X) = \frac {P (X \mid \theta) P (\theta)}{P (X)} = \frac {P (X \mid \theta) P (\theta)}{\int P (X \mid \theta) P (\theta) \mathrm{d} \theta}.\tag{13}
$$

As a result, the denominator can be computed through sampling methods, with the most prominent being Markov chain Monte Carlo (MCMC). However, MCMC methods are computationally expensive as the runtime scales exponentially with the dimensions of θ. Thus, this algorithm becomes intractable for large-scale or high-dimensional datasets. As a remedy, we propose the use of variational Bayes for approximating the posterior distributions. We derive a variational lower bound, called ELBO, for our structured-efect neural network in Section A.

## 3.5.3. Estimation parameters

In our experiments, we optimize the SENN-model by utilizing the Adam optimizer with learning rate 0.005 and all other parameters set to the default values. All implementations are performed in Python utilizing the probabilistic programming library “pyro”(http://pyro.ai/). Code for reproducibility is available online.<sup>4</sup>.

As part of our computational experiments, we later draw upon the following architectures of the structured-efect neural network: (1) we assume the non-parametric component to follow a Weibull or lognormal prior distribution, where the underlying distribution parameters are modeled as informative normal prior distributions. Mathematically, this is given by $a { \sim } N ( a _ { \mathrm { e m p i r i c a l } } ,$ 1) and $\begin{array} { r } { b { \sim } N ( b _ { \mathrm { e m p i r i c a l } } , } \end{array}$ 1). (2) The linear component is modeled such that the coeficients stem from normal prior distributions $( \boldsymbol { \mathrm { i } } . \boldsymbol { \mathrm { e } } . ,$ , as used in ordinary least squares). This is formalized by $\beta _ { i } { \sim } N ( 0 , \ 1 0 )$ , where we allow for a wider standard deviation to better handle variations in the relative influence of the predictors. As an alternative, we also implement weakly informative prior distributions $( \mathrm { i . e . , }$ , Laplace priors). The latter enforce a regularization similar to the least absolute shrinkage operator in the sense that certain coeficients are set exactly to zero in order to perform implicit variable selection and come up with a parsimonious model structure. (3) The recurrent component is implemented as a long short-term memory network with two layers containing 100 and 50 neurons, respectively. To reduce computational costs, we follow common approaches and utilize the trajectory of the previous 50 sensor values at all time steps. All weights in the network are implemented as variational parameters that follow a Gaussian prior with standard deviation of 1. Utilizing Eq.(A10), we optimize the three components simultaneously.

## 4. Computational experiments

## 4.1. Dataset

For reasons of comparability, all computational experiments are based on the “ Turbofan Engine Degradation Simulation” dataset, which is widely utilized as a baseline for comparing predictive models in maintenance and RUL predictions; see e.g., Butcher et al. [21] and Dong et al. [22] . The objective is to predict the RUL (measured in cycles) based on sensor data from 200 aircraft engines.<sup>5</sup> More specifically, it includes measurements from 21 sensors. Unfortunately, however, the exact name of each sensor is sanitized. In addition, the dataset comes with a pre-determined split into a training set (100 engines) and a test set (also 100 engines). The average RUL spans 82.30 cycles with a standard deviation of 54.59. Moreover, half of the engines experience a failure within 77 cycles, while only 25% exceed 118 cycles.

## 4.2. Prediction performance for remaining useful life

The prediction results for all models are listed in Table 3. Here we report the mean absolute error, as it represents a widely utilized metric for this dataset [50]. The benefit of this metric is that practitioners can easily translate the forecast error into a number of cycles that would serve as a security margin. The table also compares two diferent fea ture sets for traditional machine learning, i.e., on which we use only the sensor measurements from the current time step or on which we additionally apply aggregation functions to the sensors as part of feature engineering.

The empirical RUL in the first row reflects the performance of our naïve benchmark when using no predictor (i.e., predicting the average RUL of the machines). The following conditional expectations are based on the Weibull and log-normal distribution, that result in improvements of 39.17% and 38.32%, respectively. Among the traditional machine learning models, we find the lowest mean absolute error when using the random forest, which yields an improvement of 35.08% compared to the log-normal-based conditional expectation. Thereby, our results identify a superior performance through the use of feature engineering for the majority of traditional machine learning models. Recurrent neural networks outperform traditional machine learning. In particular, the LSTM yields the overall lowest mean absolute error, outperforming the random forest with feature engineering by 37.12% and the empirical RUL by 60.51%.

The structured-efect neural networks outperform traditional machine learning. Utilizing a log-normal distribution along with feature engineering yields an improvement of 25.44% compared to the best traditional machine learning model. Thereby, feature engineering accounts for 11.91% of the improvement, strengthening the assumption that feature engineering of sensor data facilitates the prediction of RUL.

## 4.3. Forecast decomposition for RUL prediction

We now demonstrate how the proposed structured-efect model achieves accountability over its RUL forecasts. That is, we leverage the linear model specification and compute the estimated values for each summand in Eq.(10) when making a RUL prediction. Yet the model can still adapt to non-linearity since the neural network can absorb the variance that cannot be explained by the other components.

Fig. 2 illustrates the interpretability of the RUL forecasts for an example engine. More specifically, we can understand how predictions are formed by decomposing the forecasts from the structured-efect model into three components – namely, the probabilistic RUL model, the linear combination of sensor measurements, and an additional neural network – as follows:

1. As we can see, the distribution-based lifetime component accounts for a considerable portion of the forecast. The maximum values in the example exceed 100, which is considerably higher than the maximum value computed by the recurrent component. The component reaches this value when making a prediction after around 50 cycles and, with each subsequent usage cycle, lowers the estimated remaining useful life. Notably, it is identical across all engines as it encodes the prior knowledge before considering the engine-specific deterioration process.

2. The second component specifies a linear combination of sensor measurements, which allows the predictions to adapt to the specific usage profiles of individual engines and explains the within-engine and within-time variability. It thus no longer yields a smooth curve but rather an engine-specific pattern. Formally, this component refers to $\beta ^ { T } X _ { t }$ and, in order to determine the relevance of sensor i, we simply interpret the coeficients in the vector $\beta .$

3. While the previous linear component still achieves full account ability over its forecasts, we now introduce the final component for modeling the remaining noise. Here we draw upon (deep) neural networks, as they are known to efectively model non-linearities. However, we thus lose the explanatory power for this component, as neural networks largely operate in a black-box fashion. In our example, we see that the recurrent part entails a non-linear curve but takes higher values in later cycles. This indicates that a linear combination is not always suficient for making predictions and, as a remedy, the structured-efect model can benefit from additional non-linear relationships and from accumulating the usage profile over time.

Notably, the magnitude of the recurrent component is much smaller than the magnitude of the other components. This is beneficial, as the SENN attributes most of the explained variance to other, interpretable model components. Methodologically, it is likely to be based on the following: at timestep t, the SENN makes prediction of the RUL from the current sensor data $X _ { t } ,$ and the trajectory of sensor data $X _ { t } , X _ { t - 1 } , X _ { t - 2 } , . . . , X _ { 1 }$ . As shown in Table 3, $X _ { t }$ is highly informative for estimating RUL and, by following stochastic gradient descent, it optimizes in the direction where the loss function decreases the most (i.e. in the direction of both the distribution-based and the linear component). Only after optimizing the interpretable components, the model updates the recurrent component to further push predictive performance via non-linear mappings.

Table 3  
Comparison of prediction performance over remaining useful life across diferent model specifications. Here we specifically report whether the models only utilize sensor measurements from the current time step or whether aggregation functions have been applied to it as part of feature engineering. Consistent with earlier works [50], the mean absolute error (MAE) is given. The best-performing model in each panel is highlighted in bold. Additionally, we perform t-tests between each mode and the best performing model from each of the four categories. The t-tests are based on the MAE of the forecasted RUL to show that improvements are at a statistically significant level.

<table><tr><td rowspan="2" colspan="2">Method</td><td rowspan="2">MAE</td><td colspan="4">Forecast comparison (t-statistic)</td><td colspan="4">Forecast comparison (P-value)</td></tr><tr><td>Best baseline</td><td>Best machine learning</td><td>Best LSTM</td><td>Best structured-effect LSTM</td><td>Best baseline</td><td>Best machine learning</td><td>Best LSTM</td><td>Best structured-effect LSTM</td></tr><tr><td colspan="11">BASELINES WITHOUT SENSOR DATA</td></tr><tr><td colspan="2">Empirical RUL</td><td>45.060</td><td>8.286</td><td>24.933</td><td>16.974</td><td>18.865</td><td>0.468</td><td>0.486</td><td>0.778</td><td>0.642</td></tr><tr><td colspan="2">Conditional expectation (Weibull)</td><td>27.794</td><td>0.288</td><td>8.309</td><td>9.615</td><td>8.018</td><td>0.293</td><td>0.462</td><td>0.666</td><td>0.457</td></tr><tr><td colspan="2">Conditional expectation (log-normal)</td><td>27.409</td><td>—</td><td>4.420</td><td>15.269</td><td>10.285</td><td>—</td><td>0.464</td><td>0.669</td><td>0.451</td></tr><tr><td colspan="11">TRADITIONAL MACHINE LEARNING</td></tr><tr><td colspan="2">Ridge regression</td><td>19.193</td><td>-6.789</td><td>1.438</td><td>5.270</td><td>2.768</td><td>0.012*</td><td>0.139</td><td>0.450</td><td>0.322</td></tr><tr><td colspan="2">Ridge regression (with feature engineering)</td><td>18.382</td><td>-8.029</td><td>0.427</td><td>3.297</td><td>2.778</td><td>0.010*</td><td>0.132</td><td>0.343</td><td>0.399</td></tr><tr><td colspan="2">Lasso</td><td>19.229</td><td>-7.015</td><td>0.766</td><td>6.577</td><td>4.145</td><td>0.015*</td><td>0.222</td><td>0.500</td><td>0.401</td></tr><tr><td colspan="2">Lasso (with feature engineering)</td><td>18.853</td><td>-7.842</td><td>0.550</td><td>5.949</td><td>2.324</td><td>0.014*</td><td>0.293</td><td>0.432</td><td>0.390</td></tr><tr><td colspan="2">Elastic net</td><td>19.229</td><td>-7.276</td><td>0.990</td><td>5.190</td><td>2.829</td><td>0.015*</td><td>0.222</td><td>0.500</td><td>0.401</td></tr><tr><td colspan="2">Elastic net (with feature engineering)</td><td>18.245</td><td>-9.055</td><td>0.458</td><td>4.244</td><td>2.572</td><td>0.009**</td><td>0.132</td><td>0.297</td><td>0.245</td></tr><tr><td colspan="2">Random forest</td><td>17.884</td><td>-4.927</td><td>0.058</td><td>5.909</td><td>4.487</td><td>0.006**</td><td>0.102</td><td>0.240</td><td>0.198</td></tr><tr><td colspan="2">Random forest (with feature engineering)</td><td>17.793</td><td>-9.495</td><td>—</td><td>2.924</td><td>3.263</td><td>0.006**</td><td>—</td><td>0.236</td><td>0.180</td></tr><tr><td colspan="2">SVR</td><td>18.109</td><td>-7.321</td><td>0.240</td><td>5.756</td><td>3.976</td><td>0.011*</td><td>0.129</td><td>0.288</td><td>0.230</td></tr><tr><td colspan="2">SVR (with feature engineering)</td><td>21.932</td><td>-4.706</td><td>3.081</td><td>9.440</td><td>3.740</td><td>0.092*</td><td>0.310</td><td>0.583</td><td>0.531</td></tr><tr><td colspan="11">RECURRENT NEURAL NETWORKS</td></tr><tr><td colspan="2">LSTM</td><td>11.188</td><td>-11.596</td><td>-4.981</td><td>—</td><td>-1.441</td><td>0.000***</td><td>0.000***</td><td>—</td><td>0.003**</td></tr><tr><td colspan="11">STRUCTURED-EFFECT NEURAL NETWORKS</td></tr><tr><td>Distribution</td><td>Linear component</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Weibull</td><td>None</td><td>15.862</td><td>-11.266</td><td>-1.015</td><td>4.424</td><td>1.825</td><td>0.000***</td><td>0.066*</td><td>0.255</td><td>0.200</td></tr><tr><td>Weibull</td><td>Regularized</td><td>17.433</td><td>-8.617</td><td>-0.213</td><td>3.536</td><td>2.746</td><td>0.000***</td><td>0.094*</td><td>0.261</td><td>0.220</td></tr><tr><td>Weibull</td><td>Feature engineering</td><td>13.392</td><td>-8.526</td><td>-2.595</td><td>1.352</td><td>0.068</td><td>0.000***</td><td>0.004**</td><td>0.144</td><td>0.134</td></tr><tr><td>Weibull</td><td>Regularized feature engineering</td><td>14.989</td><td>-10.918</td><td>-1.579</td><td>1.710</td><td>1.381</td><td>0.000***</td><td>0.049*</td><td>0.284</td><td>0.183</td></tr><tr><td>log-normal</td><td>None</td><td>15.061</td><td>-6.294</td><td>-1.420</td><td>1.627</td><td>1.702</td><td>0.000***</td><td>0.057*</td><td>0.261</td><td>0.198</td></tr><tr><td>log-normal</td><td>Regularized</td><td>16.319</td><td>-48.200</td><td>-0.779</td><td>4.582</td><td>1.334</td><td>0.000***</td><td>0.094*</td><td>0.310</td><td>0.211</td></tr><tr><td>log-normal</td><td>Feature engineering</td><td>13.267</td><td>-13.620</td><td>-2.912</td><td>1.764</td><td>—</td><td>0.000***</td><td>0.000***</td><td>0.142</td><td>—</td></tr><tr><td>log-normal</td><td>Regularized feature engineering</td><td>14.545</td><td>-11.331</td><td>-1.736</td><td>3.293</td><td>0.651</td><td>0.000***</td><td>0.038*</td><td>0.252</td><td>0.162</td></tr></table>

Significance level: \* 0.1, \*\* 0.01, \*\*\* 0.001.

![](/api/attachments/NAH5DD8H/fulltext/images/4312bdc983707a8b96053340e172d94f4cefda9f0d196a727879afbac7e7334e.jpg)

We can further compute the fraction of variance explained by the diferent components relative to the overall variance of the actual RUL values. Thereby, we quantify the contribution of each component to the overall forecast. Accordingly, this is defined by

Fig. 2. This plot visualizes the RUL predictions made by the structured-efect LSTMs based on a lognormal and normal priors in the linear component for an example engine. It decomposes the forecasts using the structured-efect model into three components that facilitate interpretations of how predictions are formed. (1) The distribution-based lifetime component contributes a considerable portion of the overall forecasts. as it is well suited to model the overall nature of the remaining useful life. This part is identical across all engines. (2) The sensor measurements introduce a variability that adapts to the specific usage profile of an engine. This component originates from a Bavesian linear model and we can trace the forecast back to individual sensors. (3) The recurrent neural network introduces a non-linear component that operates in black-box fashion.

$$
1 - \frac {\sum_ {t} (\tilde {Y} _ {t} - \tilde {\Psi} _ {t}) ^ {2}}{\sum_ {t} \left(\tilde {Y} _ {t} - \frac {1}{T} \sum_ {t} \tilde {Y} _ {t}\right) ^ {2}},\tag{14}
$$

where T denotes the total number of observations and $\widetilde { \Psi } _ { t }$ is the prediction of the component under study. Accordingly, we obtain a score of

![](/api/attachments/NAH5DD8H/fulltext/images/7ee92f88ee57dca4c7936646f74fd203a41c27ced16818a74118a85509500469.jpg)

![](/api/attachments/NAH5DD8H/fulltext/images/0071fed582c1975a56335b72a6305d652802423400b8ff4820375dd2606f8ab0.jpg)  
Fig. 3. These histograms illustrate the posterior distribution of the estimated parameters (i.e., shape, mean and scale) inside the structured-efect neural network (with log-normal structure and normal priors in the linear component). Here the estimations are compared for both distributions, namely, the Weibull and log-normal distributions. Altogether, the posteriors quantify the uncertainty of the estimated parameters.

![](/api/attachments/NAH5DD8H/fulltext/images/0c16f64ca857534eee2fef01b13b0253e01ba52cf78ef825038d9e544e251e49.jpg)

![](/api/attachments/NAH5DD8H/fulltext/images/6743ce2f10d863ea556fa563ee4b9571ac8fb86667debb180a6b70e920986c9f.jpg)  
0.175 for the non-parametric part, 0.408 for the linear component, and 0.064 for the recurrent component. This matches our expectations and, once more, highlights the overall importance of the distribution-based part of the overall forecast, as well as the role of the neural network in modeling secondary variations.

## 4.4. Estimated parameters

It is common practice to compute parameters in predictive models as point estimates [43], while our optimization technique based on variational Bayesian inferences allows for uncertainty estimates. This yields a key benefit, since we can validate our confidence in the structural components of the model by studying the posterior distribution of the parameter estimates. Fig. 3 depicts these parameters

## Table 4

Reported here are the posterior estimates of the efect size as measured by the coeficients $\beta _ { i }$ inside the linear component of the structured-efect neural network. The coeficients entail direct interpretations (similar to ordinary least squares) as to how a certain percentage of change in a sensor measurement afects the RUL prediction. In addition, standardized coeficients are reported, as they allow for the ranking of variables by importance.

<table><tr><td>Sensor</td><td>Mean estimate</td><td>Standard deviation</td><td>Standardized coefficient</td></tr><tr><td> $X_9$ </td><td>-33.169</td><td>0.498</td><td>-16.506</td></tr><tr><td> $X_{12}$ </td><td>49.721</td><td>0.250</td><td>12.440</td></tr><tr><td> $X_{21}$ </td><td>44.932</td><td>0.258</td><td>11.601</td></tr><tr><td> $X_7$ </td><td>48.154</td><td>0.230</td><td>11.073</td></tr><tr><td> $X_{11}$ </td><td>-24.622</td><td>0.357</td><td>-8.796</td></tr><tr><td> $X_{20}$ </td><td>42.850</td><td>0.184</td><td>7.880</td></tr><tr><td> $X_{14}$ </td><td>-22.540</td><td>0.317</td><td>-7.155</td></tr><tr><td> $X_4$ </td><td>-16.183</td><td>0.275</td><td>-4.447</td></tr><tr><td> $X_{15}$ </td><td>-13.934</td><td>0.297</td><td>-4.145</td></tr><tr><td> $X_2$ </td><td>-12.446</td><td>0.316</td><td>-3.931</td></tr><tr><td> $X_6$ </td><td>19.678</td><td>0.159</td><td>3.126</td></tr><tr><td> $X_3$ </td><td>-7.851</td><td>0.318</td><td>-2.494</td></tr><tr><td> $X_{17}$ </td><td>-9.951</td><td>0.208</td><td>-2.066</td></tr><tr><td> $X_8$ </td><td>-4.121</td><td>0.367</td><td>-1.511</td></tr><tr><td> $X_{16}$ </td><td>-0.273</td><td>2.105</td><td>-0.574</td></tr><tr><td> $X_{13}$ </td><td>-1.424</td><td>0.348</td><td>-0.495</td></tr><tr><td> $X_{19}$ </td><td>0.234</td><td>2.028</td><td>0.474</td></tr><tr><td> $X_{10}$ </td><td>0.126</td><td>1.900</td><td>0.239</td></tr><tr><td> $X_{18}$ </td><td>-0.095</td><td>1.936</td><td>-0.184</td></tr><tr><td> $X_1$ </td><td>-0.070</td><td>1.937</td><td>-0.135</td></tr><tr><td> $X_5$ </td><td>0.001</td><td>1.993</td><td>0.002</td></tr></table>

specifying the Weibull and log-normal distribution inside the structured-efect models.

Table 4 further reports the posterior distribution of the coeficients $\beta _ { i }$ from the linear component of the structured-effect neural network (shown is the SENN model based on a log-normal and normal priors for $\beta _ { i } )$ . These measure the efect size, i.e., how a change in a sensor measurement afects the forecast. We see that the confidence regions for the diferent coeficients vary considerably. For reasons of comparability, we further report the standardized coeficients $\beta _ { i } \operatorname { v a r } ( \beta _ { i } ) / \operatorname { v a r } ( Y _ { 1 } , . . . , Y _ { t } )$ which correct for the variance of the predictor, as well as the outcome [51]. As a result, this value allows us to rank variables by their importance.

## 4.5. Model variations

We experimented with alternative specifications of our structured effect neural network as follows.

First, we extended the neural network by an additional weighting factor $\gamma \cdot$ This yields a component $\gamma \ R N N _ { \Theta } .$ . However, it resulted in an inferior performance in all of our experiments due to severe overfitting.

Second, we experimented with a two-stage estimation approach. Here we first optimized the non-parametric component and the linear component by traditional gradient descent. Afterwards, we optimized the recurrent component against the residuals from the first stage. This approach is generally easier to train as there are fewer parameters in each stage. Yet we found an inferior performance as compared to the proposed SENN: the mean absolute error increased to 16.209. This is possibly owed to the fact that it prevents information sharing between the diferent components. Details are reported in Appendix B.

## 5. Discussion

## 5.1. Implication for decision support

Estimates of the remaining useful life can facilitate decision support with the objective of replacing deteriorated components and thus mitigating potential risks and failures that generally result in increased costs. Our approach to predicting remaining useful life is thus of direct relevance to practitioners. According to a McKinsey report, the use of accurate prediction models for RUL as a cornerstone for predictive maintenance can typically reduce the downtime of machinery by 30% to 50% and, at the same time, increase the overall life of machines by

<table><tr><td colspan="5">Stylized characteristics of different models in machine learning. Here we extend the categorization from [43, p. 351] to include deep learning and our structured-effect neural network.</td></tr><tr><td>Method</td><td>Predictive performance</td><td>Interpretability</td><td>Non-linearities</td><td>Estimation</td></tr><tr><td>Probabilistic models</td><td>Poor (but reliable as no variance is associated with it)</td><td>Good (often used along a simple threshold)</td><td>Poor (or rather constrained by how well outcomes follow a distribution)</td><td>Good (when using sampling over analytic forms)</td></tr><tr><td>Linear machine learning</td><td>Fair (regularization, especially, can yield parsimonious models and reduces the risk of overfitting)</td><td>Good (as coefficients directly quantify the effect size)</td><td>Poor (often not regarded or only interaction terms or predefined transformations such as logit)</td><td>Good (closed-form solution for ordinary least squares; optimization problems for regularization)</td></tr><tr><td>Non-linear machine learning</td><td>Good (still regarded as the benchmark against which other models have to compete)</td><td>Poor (with the exception of certain approaches, e.g., random forests, that rank variable importance but still don’t yield accountability of forecasts)</td><td>Good (can adapt well to subgroups, non-linear response curves and interactions)</td><td>Fair (often efficient estimations, but without uncertainty quantification)</td></tr><tr><td>Deep learning</td><td>Good (given sufficient training data)</td><td>Poor</td><td>Good (even when taking sequences as input)</td><td>Poor (challenging hyperparameter tuning)</td></tr><tr><td>Structured-effect neural network</td><td>Good (theoretically identical to deep learning)</td><td>Good (full accountability of the structured effect)</td><td>Good (included but only confined to the variance that cannot be explained by the structured effect)</td><td>Fair (time-consuming sampling but less prone to unfavorable hyperparameters)</td></tr></table>

20% $\tan 4 0 \% . ^ { 6 } \mathrm { { B y } }$ knowing the exact time-to-failure, companies can plan maintenance ahead of time and, therefore, make preparations for eficient decision support. As a result, even small improvements in predictive power translate into substantial operational cost savings.

As a direct implication for management, this research shows that forward-looking predictive analytics is capable of heavily influencing the way decision support in maintenance operations is conducted. However, predictive models are most powerful when fed by a large number of predictors (i.e. sensors) that describe the condition of the machinery and the environmental efects that influence the system. Therefore, managers should encourage the implementation of additional sensors to further improve accuracy when forecasting the timeto-failure. Moreover, investments in artificial intelligence are oftentimes necessary for the majority of firms who have not yet taken their first step into the age of deep learning.

## 5.2. Implications for the use of analytics

Trajectories of sensor data accumulate relevant information regarding the past usage profile of the machinery and, thereby, facilitate a prognosis regarding the risk of failure. Mathematically, this results in the objective of finding a mapping $f \colon [ X _ { 1 } , . . . , X _ { t } ] \mapsto Y _ { t }$ that is not dependent on the current time step t and thus utilizes a time series with historic measurements of arbitrary length in order to infer a prediction from it. The task can be accomplished by a special type of deep learning – namely, recurrent neural networks – as these networks can sequentially process past measurements and store the processed knowledge in their hidden layers. Even though the benefits are obvious, the use of such networks in decision support systems research remains scarce with few exceptions [e.g. 52-54].

Deep learning is often believed to require extensive amounts of data in order to be successful. However, our approach, based on variational Bayesian estimation, represents a viable alternative that can overcome this limitation. Instead of vast quantities of input data, it advocates domain knowledge that is explicitly encoded in a structural model. In our case, we already know the approximate shape of the predicted variable and can incorporate this via a probability density function into our structural part of the model. As a result, the predetermined structure can be fitted fairly easily with variational inference and thus presents a path towards encoding domain knowledge into deep neural networks. The structured efect reduces the variance and thus makes it easier to describe the remaining variance with a neural network.

## 5.3. Implications from interpretable forecasts

Our approach contributes to interpretability of deep learning. Here we remind the reader of the diference between explainability and interpretability in machine learning [17-19]. Explainability merely allows a post-hoc analysis of how predictions were computed in a local neighborhood. In contrast, interpretability presents a stronger notion: it requires machine learning models to attain complete transparency of their decision logic. Thus, we contribute to a novel approach for interpretable machine learning to decision support, that can eventually benefit (safety-)critical application fields where accountable models are required.

The high degree of interpretability of our approach reveals further implications. In practice, gaining insights into the estimated RUL aids engineers in identifying potential risks and weak spots when designing machinery. For instance, a high coeficient for a sensor measuring moisture could encourage designers to improve the sealing of a given piece of machinery. By shedding light on the prediction process, structured-efect neural networks enable novel conclusions regarding the relevance of each sensor.

Decision support as a discipline takes the demands of all stakeholders into account. With regard to the latter, managers, for instance, need to understand the decision-making of automated systems. However, this requirement is not fulfilled by recent trends in advanced analytics and especially deep learning, as these mostly operate in a black-box fashion [e.g. 44]. As a remedy, our structured-efect neural network shows improvements in predictive performance as compared to traditional machine learning, while also allowing for a high degree of interpretability. Table 5 compares the stylized characteristics of our structured-efect neural network to other approaches.

Sensors have always been an important part of predictive main tenance, as they allow to monitor and to adjust small changes so that small problems do not turn into big problems [e.g. 55]. Many diferent sensors monitoring diferent measurements can be the key to better understanding processes and preventing early failures and consequent downtime. However, complex relationships between potentially large number of sensors and the efect on machinery demand for advanced, non-linear modeling of the remaining useful life. Thus, to fully exploit the information obtained from sensors, interpretability is of great use. Our structured-efect neural network bridges the gap between these key specifications.

## 5.4. Limitations and potential for future research

Recently, dropout as a Bayesian approximation has been proposed as a simple, yet eficient means to obtain uncertainty estimates for neural networks [59]. This approach leads to models with fewer parameters, which generally facilitates optimization. Further, computa tionally costs for optimization are lower, compared to the costs when utilizing variational Bayesian inference. However, Bayesian approximation via dropout does not provide uncertainty estimates for coeficients in our model. Additionally, Bayesian approximation via dropout comes at the cost of not being capable of including prior information about the coeficients into the model. As the latter is particularly important for predictive maintenance where expert knowledge is in evitable, we decided to utilize variational Bayesian inference.

## 5.5. Concluding remarks

Decision support as a field has developed a variety of approaches to improve the cost eficiency of maintenance, especially by predicting the remaining useful life of machinery and linking operational decisionmaking to it. Common approaches for predictive maintenance include statistical models based on probability density functions or machine learning, which further incorporates sensor data. While the former still serves as widespread common practice due to its reliability and interpretability, the latter has shown considerable improvements in prediction accuracy.

This research develops a new model that combines both advantages. Our suggested structured-efect neural network achieves accountability similar to simple distribution-based RUL models as its primary component, as well as a linear combination of sensor measurements. The remaining variance is then described by a recurrent neural network from the field of deep learning, which is known for its flexibility in adapting to non-linear relationships. For this purpose, all parameters are modeled as latent variables and we propose variational Bayesian inferences for their estimation in order to optimize the Kullback-Leibler divergence. Our findings reveal that our structured-efect neural network outperforms traditional machine learning models and still allows one to draw interpretable conclusions about the sources of the deterioration process.

## Declaration of Competing Interest

None

## Acknowledgement

This work was part-funded by the Swiss National Science Foundation (SNF), Project 183569.

## Appendix A. Derivation of ELBO for structured-efect neural network

Our suggested approach draws upon variational Bayesian methods and approximates the true posterior via a variational distribution $Q _ { \lambda } ( \theta ) \approx P ( \theta$ | X). Here $Q _ { \lambda } ( \theta )$ refers to a family of distributions that is indexed by λ and, hence, our optimization problem translates into finding the optimal λ along with the corresponding distribution $Q _ { \lambda ^ { * } }$ . The following theorems state the mathematical definition of ${ \boldsymbol { \lambda } } ^ { * }$ and introduce a tractable approx imation.

Theorem 1. The optimal $\lambda ^ { * }$ is given by

$$
\lambda^ {*} = \operatorname{argmin} _ {\lambda} \mathbb {E} _ {Q _ {\lambda}} [ \log Q _ {\lambda} (\theta) ] - \mathbb {E} _ {Q _ {\lambda}} [ \log P (X, \theta) ] + \log P (X).\tag{A1}
$$

Proof. The fit between the variational distribution $Q _ { \lambda } ( \theta )$ and the posterior distribution $P ( \theta \mid X )$ can be measured by the Kullback-Leibler divergence. Hence, we yield

$$
\lambda^ {*} = \operatorname{argmin} _ {\lambda} K L (Q _ {\lambda} (\theta) | | P (\theta \mid X)).\tag{A2}
$$

Inserting the definition of the Kullback-Leibler divergence results into

$$
\lambda^ {*} = \operatorname{argmin} _ {\lambda} \mathbb {E} _ {Q _ {\lambda}} [ \log Q _ {\lambda} (\theta) ] - \mathbb {E} _ {Q _ {\lambda}} [ \log P (\theta \mid X) ] = \operatorname{argmin} _ {\lambda} \mathbb {E} _ {Q _ {\lambda}} [ \log Q _ {\lambda} (\theta) ] - \mathbb {E} _ {Q _ {\lambda}} [ \log P (X, \theta) ] + \log P (X).\tag{A4}
$$

Theorem 2. The marginal likelihood of the modellog ( )P X can be approximated by the evidence lower bound, ELBO(λ), i.e.,

Unfortunately, Eq. (1) is intractable, as it depends on the marginal likelihood of the model, log ( )P X . Therefore, the following theorem derives an approximation for the marginal likelihood of the model.

$$
\log P (X) \geq \mathbb {E} _ {Q _ {\lambda}} [ \log P (X, \theta) ] - \mathbb {E} _ {Q _ {\lambda}} [ \log Q _ {\lambda} (\theta) ] = E L B O (\lambda).\tag{A5}
$$

Proof. Utilizing Jensen's inequality, it holds that

$$
\log P (X) = \log \int P (X, \theta) \mathrm{d} \theta = \log \int P (X, \theta) \frac {Q _ {\lambda} (\theta)}{Q _ {\lambda} (\theta)} \mathrm{d} \theta = \log \mathbb {E} _ {Q _ {\lambda}} \left[ \frac {P (X , \theta)}{Q _ {\lambda} (\theta)} \right] \geq \mathbb {E} _ {Q _ {\lambda}} \left[ \log \frac {P (X , \theta)}{Q _ {\lambda} (\theta)} \right] = \mathbb {E} _ {Q _ {\lambda}} [ \log P (X, \theta) ] - \mathbb {E} _ {Q _ {\lambda}} [ \log q (\theta) ].\tag{A7}
$$

Theorem 3. The optimal $\lambda ^ { * }$ can be approximated by

\* = argmax ( ). ELBO

(A8)

Proof. From Eqs. (1) and (2), it immediately follows that

\* = argmin log ( ) ( ).P X ELBO

(A9)

Aslog $P ( X )$ is constant with respect to $\lambda ,$ the value $\lambda ^ { * }$ can be approximated by maximizing ELBO(λ). \_

In order to optimize ELBO(λ), we utilize gradient descent with the gradients defined by

$$
\nabla_ {\lambda} E L B O (\lambda) = \nabla_ {\lambda} \mathbb {E} _ {Q _ {\lambda}} [ \log P (X, \theta) ] - \mathbb {E} _ {Q _ {\lambda}} [ \log q (\theta) ] = \mathbb {E} _ {Q _ {\lambda}} [ \nabla_ {\lambda} \log q (\theta) (\log P (X, \theta) - \log q (\theta)) ].\tag{A11}
$$

We further utilize Monte Carlo integration to obtain the estimates of the ELBO(λ) and the gradient.

## Appendix B. Two-stage estimation

Analogous to our SENN, we chose the non-parametric component λ to follow a log-normal prior. The underlying distribution parameters were modeled as normal prior distributions, i.e., $a { \sim } N ( a _ { \mathrm { e m p i r i c a l } } ,$ , 1) and $\begin{array} { r } { b \sim N ( b _ { \mathrm { e m p i r i c a l } } . } \end{array}$ , 1). The linear component β was modeled such that the coeficients stem from normal prior distributions, $. \mathbf { e } . , \beta _ { i } { \sim } N ( 0$ , 10). The recurrent component $R N N _ { \Theta }$ was implemented as a long short-term memory network with two layers containing 100 and 50 neurons, respectively. Formally, the estimation is specified by as follows:

• Stage 1: \*, \* = arg max $P ( \lambda , \beta \mid X )$

• Stage 2: RNN<sup>\*</sup> = arg max (RNN | ,P X \*, \*). RNN

## References

[1] B. Heidergott, T. Farenhorst-Yuan, Gradient estimation for multicomponent main tenance systems with age-replacement policy, Oper. Res. 58 (3) (2010) 706–718.

[2] H. Groenevelt, L. Pintelon, A. Seidmann, Production lot sizing with machine breakdowns, Manag, Sci, 38 (1) (1992) 104–123

[3] A. Dogramaci, N.M. Fraiman, Replacement decisions with maintenance under uncertainty: an imbedded optimal control model, Oper. Res. 52 (5) (2004) 785–794.

[4] H.L. Lee, M.J. Rosenblatt, Simultaneous determination of production cycle and inspection schedules in a production system, Manag, Sci, 33 (9) (1987) 1125–1136

[5] A.K. Jardine, D. Lin, D. Banjevic, A review on machinery diagnostics and prognostics implementing condition-based maintenance, Mech. Syst. Signal Process. 20 (7) (2006) 1483–1510.

[6] A. Heng, S. Zhang, A.C. Tan, J. Mathew, Rotating machinery prognostics: state of the art, challenges and opportunities, Mech. Syst. Signal Process. 23 (3) (2009) 724–739.

[7] X.-S. Si, W. Wang, C.-H. Hu, D.-H. Zhou, Remaining useful life estimation: a review on the statistical data driven approaches, Eur. J. Oper. Res. 213 (1) (2011) 1–14.

[8] M. Baptista, S. Sankararaman, I. P. de Medeiros, C. Nascimento, H. Prendinger, E.M. Henriques, Forecasting fault events for predictive maintenance using datadriven techniques and ARMA modeling, Comput. & Ind. Eng. 115 (2018) 41–53.

[9] M. Seera, C.P. Lim, S. Nahavandi, C.K. Loo, Condition monitoring of induction motors: a review and an application of an ensemble of hybrid intelligent models, Expert Syst. Appl. 41 (10) (2014) 4891–4903.

[10] L. Breiman, Statistical modeling: the two cultures, Stat. Sci. 16 (3) (2001) 199–231.

[11] H. Jang, A decision support framework for robust R & D budget allocation using machine learning and optimization, Decis, Support, Syst, 121 (2019) 1–12

[12] H.S. Subramania, V.R. Khare, Pattern classification driven enhancements for human-in-the-loop decision support systems, Decis. Support. Syst. 50 (2) (2011) 460-468.

[13] D. Delen, H. Zaim, C. Kuzey, S. Zaim, A comparative analysis of machine learning systems for measuring the impact of knowledge management practices. Decis. Support. Syst, 54 (2) (2013) 1150–1160.

[14] K.L. Reifsnider, S.W. Case, Damage tolerance and durability of material systems, Wiley Interscience, New York, NY, 2002.

[15] Y. Liu. B. Stratman, S. Mahadevan. Fatigue crack initiation life prediction of railroad wheels, Int. J. Fatigue 28 (7) (2006) 747–756.

[16] N. Papakostas, P. Papachatzakis, V. Xanthakis, D. Mourtzis, G. Chryssolouris, An approach to operational aircraft maintenance planning, Decis. Support. Syst. 48 (4) (2010) 604-612.

[17] Z.C. Lipton, The mythos of model interpretability, Commun. ACM 61 (10) (2018) 36–43.

[18] C. Rudin, Please stop explaining black box models for high stakes decisions, Conference on Neural Information Processing Systems, 2018.

[19] Y. Lou, R. Caruana, J. Gehrke, G. Hooker, Accurate intelligible models with

pairwise interactions, SIGKDD International Conference on Knowledge Discovery and Data Mining. 2013, pp. 623–631

[20] A. Saxena, K. Goebel, C-mapss data set, NASA Ames Prognostics Data Repository, 2008.

[21] J.B. Butcher, D. Verstraeten, B. Schrauwen, C.R. Day, P.W. Haycock, Reservoir computing and extreme learning machines for non-linear time-series data analysis, Neural Netw. 38 (2013) 76–89.

[22] D. Dong. X.-Y. Li. F.-O. Sun. Life prediction of iet engines based on LSTM-recurrent neural networks. Prognostics and System Health Management Conference. JEEE. 2017.

[23] L. Liao, F. Kottig, Review of hybrid prognostics approaches for remaining useful life prediction of engineered systems, and an application to battery life prediction, IEEE Trans. Reliab. 63 (1) (2014) 191–207.

[24] J. Navarro, T. Rychlik, Comparisons and bounds for expected lifetimes of reliability systems, Eur, J. Oper, Res, 207 (1) (2010) 309–317

[25] M. Dong, D. He, Hidden semi-Markov model-based methodology for multi-senso equipment health diagnosis and prognosis, Eur. J. Oper. Res. 178 (3) (2007) 858–878.

[26] M.J. Kim, V. Makis, Joint optimization of sampling and control of partially ob servable failing systems, Oper, Res, 61 (3) (2013) 777–790

[27] S. Plitsos, P.P. Repoussis, I. Mourtos, C.D. Tarantilis, Energy-aware decision support for production scheduling, Decis. Support. Syst. 93 (2017) 88–97.

[28] D. Ghosh, R. Sharman, H. Raghav Rao, S. Upadhyaya, Self-healing systems: survey and synthesis Decis, Support, Syst, 42 (4) (2007) 2164–2185

[29] M. Mazhar, S. Kara, H. Kabernick, Remaining life estimation of used components in consumer products: life cycle data analysis by Weibull and artificial neural net works, J. Oper. Manag. 25 (6) (2007) 1184–1193.

[30] Cox, Regression Models and life-tables, J. R. Stat. Soc. 34 (2) (1972) 187–220

[31] Y. Wang, S. Wang, Y. Fang, P.Y. Chau, Store survival in online marketplace: an empirical investigation, Decis, Support, Syst, 56 (2013) 482–493

[32] S. Zihajehzadeh, E.J. Park, Regression model-based walking speed estimation using wrist-worn inertial sensor, PLoS ONE 11 (10) (2016) e0165211.

[33] A. Riad, H. Elminir, H. Elattar, Evaluation of neural networks in the subject of prognostics as compared to linear regression model, Int. J. Eng. & Tech. 10 (6) (2010) 52–58.

[34] A. Mosallam, K. Medjaher, N. Zerhouni, Nonparametric time series modelling for industrial prognostics and health management, Int. J. Adv. Manuf. Technol. 69 (5- 8) (2013) 1685–1699.

[35] G.S. Babu, P. Zhao, X. -L. Li, Deep convolutional neural network based regression approach for estimation of remaining useful life, Database Systems for Advanced Applications, 9642 Springer, 2016, pp. 214–228.

[36] Y. Wu, M. Yuan, S. Dong, L. Lin, Y. Liu, Remaining useful life estimation of en gineered systems using vanilla LSTM neural networks, Neurocomputing 275 (2018) 167–179.

[37] S. Zheng, K. Ristoyski, A. Farahat. C. Gupta, Long short-term memory network for remaining useful life estimation. IEEE International Conference on Prognostics and

Health Management, IEEE, 2017, pp. 88–95.

[38] M.T. Ribeiro, S. Singh, C. Guestrin, Why Should I trust you? Explaining the predictions of any classifier, SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, pp. 1135–1144.

[39] S.M. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, Advances in Neural Information Processing Systems, 2017, pp. 4765–4774.

[40] L. van der Maaten, G. Hinton, Visualizing data using t-SNE, J. Mach. Learn. Res. 9 (2008) 2579–2605 Nov.

[41] W. J. Murdoch, C. Singh, K. Kumbier, R. Abbasi-Asl, B. Yu, Interpretable machine learning: definitions, methods, and applications, arXiv preprint 2019.

[42] P.J. Vlok, J.L. Coetzee, D. Banjevic, A.K.S. Jardine, V. Makis, Optimal componen replacement decisions using vibration monitoring and the proportional-hazards model, J. Oper. Res. Soc. 53 (2) (2002) 193–202.

[43] T. Hastie, R. Tibshirani, J.H. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, second, Springer, New York, NY, 2009.

[44] I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, Cambridge, MA, 2017.

[45] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (8) (1997) 1735–1780.

[46] T. Fischer, C. Krauss, Deep learning with long short-term memory networks for financial market predictions, Eur. J. Oper. Res. 270 (2) (2018) 654–669.

[47] M. Kraus, S. Feuerriegel, A. Oztekin, Deep learning in business analytics and operations research: models, applications and managerial implications, arXiv preprint 2018.

[48] S. Srivastava, S. Lessmann, A comparative study of LSTM neural networks in fore casting dav-ahead global horizontal irradiance with satellite data, Sol. Energy 162 (2018) 232–247.

[49] R. Tibshirani, Regression shrinkage and selection via the lasso, J. R. Stat. Soc. Ser. B Methodol, 58 (1) (1996) 267–288.

[50] E. Ramasso, Investigating computational geometry for failure prognostics, Int. J. Prosthodont. Health Manag. 5 (1) (2014) 1–18.

[51] J. Bring, How to standardize regression coeficients, Amer. Statist. 48 (3) (1994) 209–213.

[52] J. Evermann, J. -R. Rehse, P. Fettke, Predicting process behaviour using deep

learning, Decis. Support. Syst. 100 (2017) 129–140.

[53] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decis. Support. Syst. 104 (2017) 38–48.

[54] N. Mahmoudi, P. Docherty, P. Moscato, Deep neural networks understand investor better, Decis. Support. Syst. 112 (2018) 23–34.

[55] J. Rabatel, S. Bringay, P. Poncelet, Anomaly detection in monitoring sensor data for preventive maintenance, Expert Expert Syst. Appl. 38 (6) (2011) 7003–7015.

[56] W. Xiang, P. Musau, A.A. Wild, D.M. Lopez, N. Hamilton, X. Yang, J. Rosenfeld, T.T. Johnson, Verification for Machine Learning, Autonomy, and Neural Networks Survey, arXiv preprint arXiv:1810.01989, 2018.

[57] A. Athalye, N. Carlini, D. Wagner, Obfuscated gradients give a false sense of se curity: circumventing defenses to adversarial examples, International Conference on Machine Learning. 2018

[58] G. Singh, T. Gehr, M. Mirman, M. Püschel, M. Vechev, Fast and efective robustness certification, Conference on Neural Information Processing Systems, 2018, pp. 10802–10813.

[59] Y. Gal, Z. Ghahramani, Dropout as a Bayesian approximation: representing mode uncertainty in deep learning, in: International Conference on International Conference on Machine Learning in: 2016, pp. 1050–1059.

Mathias Krausis a PhD student at the Chair of Management Information Systems at ETH Zurich. Previously, he has completed his Bachelor's and Master's studies in computer science and mathematics at the Karlsruhe Institute of Technology. His research focuses on applications of machine learning and statistics for data analytics, with a focus on deep neural networks and Bayesian inference.

Stefan Feuerriegelis an assistant professor for management information systems at ETH Zurich. His research focuses on cognitive information systems and business intelligence, including text mining and sentiment analysis of financial news. Previously, he obtained his Ph.D. from the University of Freiburg where also worked as a research group leader at the Chair for Information Systems Research. He has co-authored research publications in the European Journal of Operational Research, the European Journal of Information Systems, the Journal of Information Technology and Decision Support Systems.
