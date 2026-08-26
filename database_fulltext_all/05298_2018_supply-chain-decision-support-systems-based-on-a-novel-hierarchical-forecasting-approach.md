---
otero_id: 5298
otero_key: "GAUV26KX"
title: "Supply chain decision support systems based on a novel hierarchical forecasting approach"
authors: "Marco A. Villegas; Diego J. Pedregal"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Supply chain decision support systems based on a novel hierarchical forecasting approach

![](/api/attachments/GAUV26KX/fulltext/images/8a5bd987f0c3faa5de5335036045461319584b46b61a5313a083fefce5f7478c.jpg)

Marco A. Villegas, Diego J. Pedregal

<table><tr><td>PII:</td><td>S0167-9236(18)30124-6</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.08.003</td></tr><tr><td>Reference:</td><td>DECSUP 12977</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>22 March 2018</td></tr><tr><td>Revised date:</td><td>23 July 2018</td></tr><tr><td>Accepted date:</td><td>4 August 2018</td></tr></table>

Please cite this article as: Marco A. Villegas, Diego J. Pedregal, Supply chain decision support systems based on a novel hierarchical forecasting approach. Decsup (2018), doi:10.1016/j.dss.2018.08.003

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Supply chain decision support systems based on a novel hierarchical forecasting approach

Marco A. Villegas, Diego J. Pedregal\*

ETSI Industriales. University of Castilla-La Mancha. 13071 Ciudad Real, Spain.

## Abstract

Time series forecasting plays an important role in many decision support systems, also in those related to the management of supply chains. Forecast accuracy is, therefore, essential to optimise the efficiency of any supply chain. One aspect that is often overlooked is the fact that sales of many products within an organization are assembled as complex hierarchies with different levels of aggregation. Very often forecasts are produced regardless of such structure, though forecasting accuracy may be improved by taking it into account. In this paper an approach for hierarchical time series forecasting based on State Space modelling is proposed. Previous developments provide solutions to the hierarchical forecasting problem by algebra manipulations based on forecasts produced by independent models for each time series involved in the hierarchy. The solutions produce optimal reconciled forecasts for each individual forecast horizon, but the link along time that is implied by the dynamics of the models is completely ignored. Therefore, the novel approach in this paper improves upon past research at least in two key points. Firstly, the algebra is already encoded in the State Space system and the Kalman Filter algorithm, giving an elegant and clean solution to the problem. Secondly, the State Space approach is optimal both across the hierarchy, as expected, but also along time, something missing in past developments. The approach is assessed by comparing its forecasting performance to the existing methods, through simulations and using real data of a Spanish grocery retailer.

Keywords: Forecasting, Hierarchical forecasting, Reconciliation, State Space, Decition Support System.

# ACCEPTED MANUSCRIPT

## 1. Introduction

Many decision support systems in most business and industrial sectors rely on time series forecasting. The efficiency of such systems depends crucially on the accuracy of forecasts. To reach that end, many different techniques have been reported in the literature, from more traditional ones, like ARIMA or ExponenTial Smoothing to other more modern, typically combinations of traditional methods with wavelets, Artificial Neural Networks, Deep Learning, etc. (Harrison and Stevens, 1976; Harvey, 1989; Young et al., 1999; Fildes et al., 2006; Hyndman and Khandakar, 2008; Sun et al., 2008; Choi et al., 2011; Lu et al., 2012; Durbin and Koopman, 2012; Box et al., 2015).

One aspect that is often overlooked is the fact that sales of many products within an organization are aggregated across geographic or logical dimensions to form hierarchical structures. The data is then forecast at different levels of aggregation which have been reported as beneficial in terms of robustness and accuracy. However, independent forecasts of all time series at all levels of aggregation have the undesired property of being inconsistent across the hierarchy. Therefore, a strategy for reconciling forecasts across aggregation levels to improve consistency is required.

Several approaches have been proposed in the literature to deal with this problem, based on different assumptions and codified with different labels, namely bottom-up, top-down, middle-out and reconciled (see section 2 below). In this paper, a State Space (SS) approach for the general treatment of hierarchies is proposed, providing a framework that gives an unified solution for all types available. This framework even permits a new category, namely combined hierarchies, defined as any feasible logical combination of the aforementioned categories. In this framework, all the previous cases are seen as particular examples of a combined hierarchy, in which each node is defined as any of such categories. In other words, our approach to the problem would consist on defining the hierarchy structure and the type of each single node.

This approach improves upon recent research (mainly Hyndman et al., 2011, 2016) at least in two fundamental ways. Firstly, the appropriate SS form and the associated optimal recursive algorithms provide an elegant optimal solution to the hierarchical forecasting problem without the need to resort to any additional algebra (e.g. check Hyndman et al., 2011). Secondly and most importantly, given the recursive nature of the solution to the state estimation problem thanks to the Kalman Filter, the optimality is propagated along time, i.e., the solution preserves the time consistency implied by the dynamical behaviour of the individual models for each time series. This fact is completely ignored in all previous studies and is the key development of this paper.

The layout of the paper is as follows. Section 2 reviews the most relevant literature on the topic. Section 3 states the problem of forecasting a hierarchy. Section 4 reviews SS fundamentals. Section 5 shows how a general hierarchy may be set up in the SS framework. Several reflections emerge from the results of a numerical simulation (Section 6) and the experimentation on real data of a Spanish grocery retailer (Section 7). The paper concludes with a final discussion and afterthoughts in Section 8.

## 2. Literature review

Research on hierarchical time series have been reported in the literature for several decades. Examples of early studies include Grunfeld and Griliches (1960); Orcutt et al. (1968); Shlifer and Wolff (1979); Barnea and Lakonishok (1980); Gross and Sohl (1990); Dangerfield and Morris (1992); Fliedner (1999); Weatherford et al. (2001); etc. In supply chain scenarios, for example, disaggregated demand data is usually available for every shop or distribution center. At this level, natural hierarchies can be formed aggregating data corresponding to the criteria of interest. Logical hierarchies can be formed when data are grouped based on relevant criteria to the business. Families (or groups) of products in grocery industries, for example, have an important role as a business variable for supply chain orchestration (Fliedner and Lawrence, 1995; Muir, 1979). Synthetic hierarchies can be defined simply by attending to the nature of time series themselves. In these cases, time series are first classified into groups according to their structural components so as to optimize modeling, and then are aggregated to form the next level of the hierarchy (Fliedner, 2001).

A number of different approaches for optimizing hierarchical forecasts have been proposed in recent years. The bottom-up approach entails forecasting the lowest level in the hierarchy and propagating the forecasts upwards according to the hierarchy structure (Orcutt et al., 1968; Dangerfield and Morris, 1992). The top-down strategy forecasts the uppermost level time series and then disaggregate down the forecasts to lower levels using different approaches, normally proration or by ratios of every single time series with respect to the aggregate, as described by Gross and Sohl (1990); Strijbosch et al. (2008); Boylan (2010). Middle-out approach combines both previous approaches by forecasting a middle level and then aggregating bottom-up as well as disaggregating top-down. Optimal reconciliation is proposed as a way of modifying individual forecasts and making them compatible, without the need to fix any of them on a priori grounds, the procedure has been also extended to temporal hierarchies (Hyndman et al., 2011, 2016; Athanasopoulos et al., 2017).

Debate as to which approach is best in forecasting terms has been going on for some time. Some studies are in favor of top-down approaches (Grunfeld and Griliches, 1960; Gross and Sohl, 1990; Fliedner, 1999), others prefer the bottom-up strategy (Orcutt et al., 1968; Dangerfield and Morris, 1992; Zellner and Tobias, 2000; Weatherford et al., 2001), while others advocate a reconciled approach (Hyndman et al., 2011, 2016). Some more theoretically oriented studies have focused on analyzing the conditions under which approach produces more accurate forecasts than others (Shlifer and Wolff, 1979; Lütkepohl, 1984; Widiarta et al., 2009; Sbrana and Silvestrini, 2013; Rostami-Tabar et al., 2016).

At present, discussions remain inconclusive and will probably persist over the following decades, for several reasons. Firstly, empirical comparisons suggest that there is no single approach that outperforms the rest, as the results depend on the complexity of the hierarchy, the quality of the data at each level, the accuracy of the models, etc. Secondly, setting out general conditions on which any hierarchy is better optimized on theoretical grounds presupposes ideal conditions that may or may not be met in experiments with real data, thus weakening importance for day to day practice. Finally, discussions are becoming more complicated because of the emergence of novel ways to optimize a hierarchy (for example, the reconciled approach).

This paper seeks to take the debate a step further by i) proposing a new strategy based on SS models that encompass all the previous aggregation approaches as particular cases, ii) by generalizing the hierarchy setup by which each node type has to be defined independently, iii) by taking advantage of the SS form that provides forecasts consistent across the hierarchy and along time. To the best of our knowledge, this is the first time that consistency along time is explicitly considered in hierarchical forecasting problems.

## 3. Hierarchical forecasting

The problem of hierarchical forecasting consists in finding optimal forecasts for all the time series involved in a hierarchy in such a way that the forecasts add up according to the constraints imposed by the hierarchy. There are many types of hierarchies and even more ways to organize the same data into different hierarchies. The total sales of a company could be disaggregated first into regions and then in product families, or vice-versa, leading to different hierarchies in each case. Figure 1 shows an example of a simple hierarchy, composed of three levels and eight nodes or time series, five of which are at the bottom level, as in Hyndman et al. (2016).

![](/api/attachments/GAUV26KX/fulltext/images/fe99e0b0c508cd8674e1ef201574febb4a4d4d4df9b0dc8da2c00eecbb94de67.jpg)  
Figure 1: An example of a simple hierarchy

A hierarchy may be represented as a multivariate model with a number of constraints. However, relevant hierarchies are assumed to be large, making their multivariate representation infeasible. Thus, a more appropriate approach consists in identifying univariate models for each time series at every level in the hierarchy, and achieving forecast reconciliation in a second stage.

Any hierarchy or grouping data structure may be expressed as a linear transformation of the bottom level variables. The ensuing matrix transforms the data or the forecasts at the bottom layer into the whole data structure in a straightforward manner. Taking $y_{node}$ the data at any node in the hierarchy of Figure 1,

such transformation is

$$
\left( \begin{array}{c} y _ {T O T A L} \\ y _ {A} \\ y _ {B} \\ y _ {A A} \\ y _ {A B} \\ y _ {A C} \\ y _ {B A} \\ y _ {B B} \end{array} \right) = \left( \begin{array}{c c c c c} 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} y _ {A A} \\ y _ {A B} \\ y _ {A C} \\ y _ {B A} \\ y _ {B B} \end{array} \right)\tag{1}
$$

or simply $y_{t} = S b_{t}$ , where $y_{t}$ is the vector of data or forecasts of all the time series, S is the summing matrix (Hyndman et al., 2011) defining the hierarchy and $b_{t}$ is the data or forecasts at the bottom level.

## 4. State Space modelling

The general linear Gaussian SS model implemented in this paper is shown in Equation (2).

Transition equation:

Observation equation:

$$
\begin{array}{r l} \alpha_ {t + 1} = T \alpha_ {t} + R \eta_ {t}, & \eta_ {t} \sim N (0, Q) \\ y _ {t} = Z \alpha_ {t} + C \epsilon_ {t}, & \epsilon_ {t} \sim N (0, H) \end{array}\tag{2}
$$

In these equations $\alpha_{t}$ is a non-observable state vector of length n; $\eta_{t}$ and $\epsilon_{t}$ are the state and observational vectors of zero mean Gaussian noises, with dimensions $r \times 1$ and $h \times 1$ , respectively; both are considered independent or each other along this paper, but in general applications may be allowed to be correlated with covariance $S = Cov(\eta_{t}, \epsilon_{t})$ of dimension $r \times h$ ; $y_{t}$ is the $k \times 1$ vector of output data. The initial state vector is assumed to be stochastic with Gaussian distribution, i.e., $\alpha_{1} \sim N(a_{1}, P_{1})$ , and independent of all data and noises involved in the system.

The remaining elements in (2) are the so called system matrices with appropriate dimensions, i.e.:

$$
\begin{array}{l l l l l} T \colon & n \times n; & R \colon & n \times r; & Q \colon & r \times r; \\ Z \colon & k \times n; & C \colon & k \times h; & H \colon & h \times h. \end{array}
$$

All the system matrices may be time varying, but they are not explicitly considered here simplify the

# ACCEPTED MANUSCRIPT

notation.

Further sophistication may be introduced in both equations by means of additional matrices taking into account either linear or non-linear input-output relationships. These particular configurations with a number of extensions not quoted here (such as non-gaussian and non-linear models) are implemented in the SSpace toolbox written by the authors for the MATLAB environment (The MathWorks, Inc, 2018; Villegas and Pedregal, 2018). This toolbox is based on several references, like Harvey (1989), Young et al. (1999), Durbin and Koopman (2012), Casals et al. (2016). Other pieces of software related to this are, among many others, Commandeur et al. (2011), Koopman et al. (2009), Taylor et al. (2007), Gómez (2015).

Many standard univariate techniques considered for forecasting actually fit into the present framework. Typical examples are ExponenTial Smoothing (ETS) or ARIMA models, but others not so common in this area are also implementable, like Unobserved Components (UC) models (Harvey, 1989; Durbin and Koopman, 2012; Young et al., 1999). In addition, SS systems offer an exceptional framework in which all the hierarchical approaches, bottom-up, top-down, middle-out and reconciled, fit in quite naturally. Even any logical mixture of these approaches, combined with any mixture of models, may be used simultaneously across any hierarchy, as described in the next section. This allows to use the most convenient model and approach for each part of the hierarchy. To sum up, SS methodology provides the possibility of a unified treatment of all possible cases.

## 4.1. The Kalman Filter

It is well-known that the Kalman Filter (KF) is a recursive algorithm that provides the optimal estimation of the states and their covariances of a SS system at any point in time by minimizing the mean squared error, conditional on all information available up to that point in time (Kalman, 1960). There have been many formulations of the recursive equations, of which the decomposition in prediction and correction steps is especially illustrative in the present context. The algorithm is shown in Equation (3), where $a_{t} = E(\alpha_{t}|Y_{t - 1})$ , $a_{t|t} = E(\alpha_t|Y_t)$ , $P_{t} = Var(\alpha_{t}|Y_{t - 1})$ , $P_{t|t} = Var(\alpha_t|Y_t)$ , $Y_{t - 1}$ and $Y_{t}$ stand for all information available up to $t - 1$ or $t$ , respectively. The variable $v_{t}$ is known as the innovation (with time covariance matrix $F_{t}$ ), the information that cannot be predicted from all the information available at the previous step.

$$
\text { Correction   step: } \quad \text { Prediction   step: }
$$

$$
\begin{array}{c c} v _ {t} = y _ {t} - Z a _ {t} \\ F _ {t} = Z P _ {t} Z ^ {\prime} + C H C ^ {\prime} \\ K _ {t} = P _ {t} Z ^ {\prime} F _ {t} ^ {- 1} \\ a _ {t | t} = a _ {t} + K _ {t} v _ {t} & a _ {t + 1} = T a _ {t | t} \\ P _ {t | t} = P _ {t} - K _ {t} F _ {t} K _ {t} ^ {\prime} & P _ {t + 1} = T P _ {t | t} T ^ {\prime} + R Q R ^ {\prime} \end{array}\tag{3}
$$

Additionally, the forecast for the output data is produced by $y_{t+1} = Za_{t+1}$ . Given an appropriate initialization of the KF, i.e. appropriate values for $a_{1}$ and $P_{1}$ , the algorithm proceeds recursively applying the correction equation after the prediction equation for $t = 1, 2, \cdots, N$ .

Correction equations are skipped if missing data is present. Forecasts are the natural outcome of the KF if the output data is set to missing information, because the correction equations do not apply and the prediction equations are applied recursively. The issue of initialization, especially for non-stationary models, is a complex one for which the solution applied in this paper and implemented in SSpace is the exact initial KF as in Durbin and Koopman (2012).

The KF assumes all system matrices are known. However, in real situations this is very rarely the case. Therefore, prior to the application of the KF, estimation of the unknown parameters should be carried out. There are many ways to do this task, of which Maximum Likelihood in time domain via error decomposition is very often preferred, because of its good statistical properties in very general situations. See details in Durbin and Koopman (2012), also Young et al. (1999) for frequency domain approaches.

## 4.2. An example

A simple example is proposed here in order to illustrate the SS approach. Let's consider an ARMA(2, 1) model in Equation (4).

$$
y _ {t} = \phi_ {1} y _ {t - 1} + \phi_ {2} y _ {t - 2} + \epsilon_ {t} + \theta \epsilon_ {t - 1}, V a r (\epsilon_ {t}) = \sigma^ {2}\tag{4}
$$

The SS representation of this model is not unique, but one that is often used in the literature is

$$
\begin{array}{c} \left( \begin{array}{l} \alpha_ {1, t + 1} \\ \alpha_ {2, t + 1} \end{array} \right) = \left( \begin{array}{l l} \phi_ {1} & 1 \\ \phi_ {2} & 0 \end{array} \right) \left( \begin{array}{l} \alpha_ {1, t} \\ \alpha_ {2, t} \end{array} \right) + \left( \begin{array}{l} 1 \\ \theta \end{array} \right) \epsilon_ {t} \\ y _ {t} = \left( \begin{array}{l l} 1 & 0 \end{array} \right) \left( \begin{array}{l} \alpha_ {1, t} \\ \alpha_ {2, t} \end{array} \right) \end{array}\tag{5}
$$

Matching system (5) with the general SS system (2) identifies the system matrices for this particular case, i.e.,

$$
\begin{array}{l} T = \left( \begin{array}{c c} \phi_ {1} & 1 \\ \phi_ {2} & 0 \end{array} \right); \quad R = \binom{1}{\theta} \epsilon_ {t} \quad Q = \sigma^ {2} \\ Z = \left( \begin{array}{c c} 1 & 0 \end{array} \right) \qquad C = 0 \qquad H = 0 \end{array}
$$

Matrices T, Q and R depend on the parameters of the ARMA(2,1) model and given the data may be estimated by Maximum Likelihood. With the estimated values placed in these matrices, the KF in Equation (3) gives the optimal estimation of the states, forecasts and their covariances. Generalizations of this example to ARMA $(p,q)$ models is straightforward.

## 5. Hierarchies in SS form

The problem stated in Section 3 may be solved by building an overall SS system that comprises all the models in a hierarchy with the constraints imposed by the hierarchy structure and all the information involved. It is assumed that the base models have been identified previously in some way, either automatically or manually. In order to build the overall SS structure, such models ought to be cast in SS form, though not necessarily identified within a SS framework.

The overall SS system representing the hierarchy is built in two steps:

\- Build up the overall system by block concatenation.

\- Add hierarchical constraints depending on the type of hierarchy.

# ACCEPTED MANUSCRIPT

## 5.1. Build overall system

Assuming that the univariate models for all variables are set up in SS form, the model for the i-th variable may be written as in Equation (2) with a superscript $\binom{(i)}{i}$ added to every single element in the SS formulation. Such superscript runs from 1 to the number of variables k.

The first step, then, consists of building an overall SS system based on k systems of type (2) (k = 8 in example of Figure 1). This is possible by block concatenation of the individual systems, see Equation (6).

$$
\left( \begin{array}{c} \alpha_ {t + 1} ^ {(1)} \\ \vdots \\ \alpha_ {t + 1} ^ {(k)} \end{array} \right) = \left( \begin{array}{c c c} T ^ {(1)} & \ldots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \ldots & T ^ {(k)} \end{array} \right) \left( \begin{array}{c} \alpha_ {t} ^ {(1)} \\ \vdots \\ \alpha_ {t} ^ {(k)} \end{array} \right) + \left( \begin{array}{c c c} R ^ {(1)} & \ldots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \ldots & R ^ {(k)} \end{array} \right) \left( \begin{array}{c} \eta_ {t} ^ {(1)} \\ \vdots \\ \eta_ {t} ^ {(k)} \end{array} \right)
$$

$$
\left( \begin{array}{c} y _ {t} ^ {(1)} \\ \vdots \\ y _ {t} ^ {(k)} \end{array} \right) = \left( \begin{array}{c c c} Z ^ {(1)} & \ldots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \ldots & Z ^ {(k)} \end{array} \right) \left( \begin{array}{c} \alpha_ {t} ^ {(1)} \\ \vdots \\ \alpha_ {t} ^ {(k)} \end{array} \right)\tag{6}
$$

$$
+ \left( \begin{array}{c c c} C ^ {(1)} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & C ^ {(k)} \end{array} \right) \left( \begin{array}{c} \epsilon_ {t} ^ {(1)} \\ \vdots \\ \epsilon_ {t} ^ {(k)} \end{array} \right)
$$

$$
C o v \left( \begin{array}{c} \eta_ {t} ^ {(1)} \\ \vdots \\ \eta_ {t} ^ {(k)} \end{array} \right) = \left( \begin{array}{c c c} Q ^ {(1)} & \ldots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \ldots & Q ^ {(k)} \end{array} \right); \quad C o v \left( \begin{array}{c} \epsilon_ {t} ^ {(1)} \\ \vdots \\ \epsilon_ {t} ^ {(k)} \end{array} \right) = \left( \begin{array}{c c c} H ^ {(1)} & \ldots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \ldots & H ^ {(k)} \end{array} \right)
$$

Once more, this system is in form (2). Given its block diagonal structure, using system (6) on the whole dataset is exactly equivalent to using the $k$ individual SS systems independently.

## 5.2. Add hierarchical constraints

Let's rename all the system matrices in (6) in compact form as their counterparts of system (2) with superscript $(^{(K)})$ added to them. Then, the second step consists in finding out a modified observation equation that replicates all the univariate models and the constraints imposed by the hierarchy at the same time. This is achieved by pre-multiplying the overall observation equation by a matrix $S^{(*)}$ , given in Equation (7).

$$
S ^ {(*)} = \left( \begin{array}{c c} S ^ {(K)} & S \end{array} \right)\tag{7}
$$

Matrix $S^{(*)}$ is actually a combination of matrix S that defines the hierarchy structure and a new matrix $S^{(K)}$ that has to be found depending on the type of system (bottom-up, etc.). The dimension of $S^{(K)}$ is $k \times m$ , where m is the number of aggregated variables.

\- Bottom-up: $S^{(K)} = 0$ . Pre-multiplying the observation equation by $S^{(*)}$ in this case leaves the system as it is. In this case, forecasts may be produced simply as the aggregation of individual forecasts without any need of the overall system. A more efficient version of this model, with less states, is found by declaring $S^{(K)}$ as an empty matrix and using an overall system that only comprises the models at the bottom level. Indeed, this is the preferred form when the system is purely bottom-up. However, this less efficient version is preferred for the sake of the combined systems defined below.

\- Top-down: as in the case of bottom-up, but inserting the forecasts obtained by the individual model of $y_{TOTAL}$ as actual data. As in the previous case, the top-down system may be defined more efficiently with less states, but this form is retained.

\- Reconciled: $S^{(K)} = \left( \begin{array}{cc} -I & 0 \end{array} \right)$ , where $I$ is an identity matrix of a dimension equal to the number of aggregated variables ( $m$ ) and the rest are a block of zeros of appropriate dimension ( $(k - m) \times m$ ). In this case, $y_t^{(K)}$ is a composition of zeros for the aggregated data and the disaggregated series $b_t$ .

\- Combined: the way each case above is set up allows for their combination in a single hierarchy by selecting appropriate values for the diagonal elements of matrix $S^{(K)}$ and the data affecting it. For example, by setting $S^{(K)}(i,i) = -1$ and zeros for the $i-th$ aggregate variable that node is chosen as reconciled. Otherwise, set $S^{(K)}(i,i) = 0$ and missing data or the forecasts of the univariate model for $i-th$ aggregated series, for bottom-up or top-down options, respectively. One must bear in mind that the middle-out case quoted in the literature is just a particular case of a combined hierarchy. Therefore, rather than speaking about hierarchy types (i.e., bottom-up, reconciled, etc.) a thorougher nomenclature would be to talk of node types.

The optimality of the system built in this way rely on three sets of assumptions:

\- The typical ones referred to the individual models identified for each time series. These also apply to the rest of hierarchical forecasting methods. Models should be correctly specified, meaning in general

# ACCEPTED MANUSCRIPT

that all the statistical properties assumed about the models have to be met. Very often such assumptions have to do with the correct identification of the individual models, constancy of parameters over time and specific perturbation properties (they should be Gaussian with zero mean, constant variance and serially independent).

\- Those related to the general SS system in equations (2), as were stated in the paragraph immediately after. The most important ones are that all the perturbations involved are assumed serially independent, with zero mean and constant covariance matrices, independent of each other and of the initial state vector.

\- Time consistency of optimal reconciled forecasts with the dynamical models assumed for the individual time series. The way the system is built and the posterior application of the recursive algorithms ensure that all the constraints imposed by the hierarchy are fulfilled, and also ensure the consistency of the forecasts with the dynamical behaviour expected from the individual models identified for each time series. Time consistency is disregarded in all previous studies.

## 5.3. Discussion

The path followed to build the SS hierarchical system illustrates how the transition equation embodies the dynamical systems of all the independent univariate models, while the observation equation just defines both the hierarchy structure and node types. Thus, the two-step KF in Equation (3) renders the optimal one-step-ahead forecasts of the states: in the prediction step, which only uses the transition equation system matrices, the independent forecasts are computed regardless of the hierarchy, while the correction step updates them by imposing the appropriate constraints according to the hierarchy structure. Such a correction is done by minimizing the Mean Squared Error, conditional on all information available at any time, on the univariate models for all series and on the constraints imposed by the hierarchy.

An additional benefit of this approach is that it neatly takes advantage of the KF optimality without any further assumptions or any further algebra. In the particular case of the top-down systems, there is no need to elaborate on how the top forecasts have to be disaggregated (Gross and Sohl, 1990). The advantages also apply to reconciled systems, in which additional objective functions ought to be assumed, opening the door to different options (Hyndman et al., 2011, 2016).

# ACCEPTED MANUSCRIPT

The main advantage of the SS approach and the reason why this research is undertaken is the fact that any hierarchical forecast is produced based on past optimal forecasts previously obtained with the hierarchical system. Therefore, the forecasts are consistent both hierarchical-wise and time-wise, i.e., forecasts fulfill all the constraints imposed by the hierarchy and are consistent with the time dynamics of the univariate models optimally identified. Clearly, this is neither the case of Hyndman et al. (2011) reconciled approach nor the top-down of all the previous literature, where the interest is focused exclusively on finding cross sectional coherence among all the forecasts without any reference to the optimal forecasts obtained for previous time periods, losing the consistency along the temporal dimension.

The following simple example illustrates the point of time consistency of the SS reconciled forecasts in contrast to other approaches. Let's assume two independent AR(1) processes,

$$
\begin{array}{c c} x _ {1, t} = 0. 8 x _ {1, t - 1} + a _ {1, t}, & \text {var} (a _ {1, t}) = 1 \\ x _ {2, t} = - 0. 8 x _ {2, t - 1} + a _ {2, t}, & \text {var} (a _ {2, t}) = 1 \end{array}\tag{8}
$$

It is well known that the eventual forecast function of both processes decay exponentially to zero, the first one from either the positive or negative side, while the second alternating sign at every step around zero. The aggregation of the two processes $(y_{t}=x_{1,t}+x_{2,t})$ is an AR(2) because the coefficients of the two AR(1) processes are equal and opposite in sign and the variance of both noises is the same (Granger and Morris, 1976). A simulation of the above models produces forecasts like the ones shown in Figure 2. The standard procedure is done in the R environment with the hts package (Hyndman et al., 2011), while the SS forecasts are done in MATLAB with the SSpace toolbox (Villegas and Pedregal, 2018). The example is done in a way such that the base AR models are exactly the same in both cases, making sure that the observed differences are strictly and solely due to the aggregation procedures. The SS reconciled forecasts resemble what is expected in theory, while the standard procedure produces forecasts that are combinations of the expected. In this sense, SS approach is time-consistent, while the standard method computed with hts package is not.

The possibilities of combined systems open up the door to further considerations. Taking the hierarchy in Figure 1, the adjusted forecasts will be different depending on the type assigned to each node. Figure 3 shows just a few possibilities that naturally differ from those in which all the nodes are of the same type.

![](/api/attachments/GAUV26KX/fulltext/images/7df8cacd5915cad782e1faf9c611050326f63f1f3e531173f105e7d49f30ffe6.jpg)

![](/api/attachments/GAUV26KX/fulltext/images/5bc2c7a6facfdfdd744e01fc50d3a1f6135601683d63786399f5f7b909044692.jpg)

![](/api/attachments/GAUV26KX/fulltext/images/4c921d29bfce502131504ac25fdcb4164b1df871298854344737c534537367e0.jpg)  
Figure 2: Forecasts of two simulated AR(1) processes $(x_{1,t}$ and $x_{2,t})$ and its aggregate $y_{t} = x_{1,t} + x_{2,t}$ obtained with the SSpace (State Space) and hts (Standard).

![](/api/attachments/GAUV26KX/fulltext/images/607b23d28f37cd927344c9d2d7955d9706f80eca6d204a0e2a9638ce434fd0be.jpg)  
Figure 3: Some of the possible options for the top structure of the hierarchy in Figure 1. TD, BU and R stand for top-down, bottom-up and reconciled, respectively.

Then, for the same hierarchy there are many different ways to produce forecasts, all optimal from the point of view of minimizing the mean squared error, but with different sets of information/constraints. The selection of each node type may be carried out by a lengthy empirical process, resembling data mining procedures, or by imposing constraints based on previous experience. Not every possible combination is logical, but the number of logical combinations is certainly very high, increasing with the number of nodes and the depth and width of the hierarchy. This is an area that requires more research and is beyond the scope of this paper.

Kahn (1998) mentioned the idea of a hybrid approach combining the advantages of top-down and bottom-up. As previously discussed, our approach provides a framework that takes this idea of flexibility to a new extent, allowing to assign a combination strategy to each node in the hierarchy. Moreover,

## further considerations are:

\- The proposed approach makes it easy to integrate multivariate models as part of the hierarchy. Instead of a block concatenation of univariate models, the corresponding block would be replaced by the appropriate multivariate module.

\- Judgmental forecasts may be incorporated into the hierarchy at any node by selecting them as a top-down node.

\- Node types may be also time dependent, keeping the hierarchy and time consistency and building forecasts on past optimal forecasts based on the hierarchy structure. A system might be bottom-up at some points in time and top-down at others, meaning that by means of the latter the forecasts are forced to reach a certain level at certain time stamps.

\- Simulations are also possible, for example, it is possible to set scenarios to answer questions such us what future paths are compatible with certain future values at certain nodes.

\- Optimal confidence bands or prediction intervals may be estimated automatically from the standard KF output in the usual way.

## 6. Simulations

In this section we develop a simulation study to compare the proposed methodology with existing alternatives. The simulation process is basically a replication of the one described in Hyndman et al. (2011) with minor modifications. All bottom level series are simulated as ARIMA $(p,d,q)$ processes with $d = 1$ , $p \in (0,2)$ and $q \in (0,2)$ with parameter values chosen randomly with equal probability within the stationary and invertible regions. The hierarchy structure remains the same, i.e., 3 levels, with eight series at bottom-level that are aggregated by pairs to form the four series at level 2, two series at level 1, and the most aggregated series at the top level.

The bottom-level series are first generated and then aggregated to form the hierarchy. The same covariance matrix is used to allow for correlation between bottom level series from the same level 1 group. Such

matrix is

$$
\left[ \begin{array}{c c c c c c c c} 7 & 3 & 2 & 1 & 0 & 0 & 0 & 0 \\ 3 & 7 & 2 & 1 & 0 & 0 & 0 & 0 \\ 2 & 2 & 6 & 3 & 0 & 0 & 0 & 0 \\ 1 & 1 & 3 & 6 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 7 & 3 & 2 & 1 \\ 0 & 0 & 0 & 0 & 3 & 7 & 2 & 1 \\ 0 & 0 & 0 & 0 & 2 & 2 & 6 & 3 \\ 0 & 0 & 0 & 0 & 1 & 1 & 3 & 6 \end{array} \right]
$$

Datasets of 100 samples were generated, taking the first 90 samples as the training partition for identifying and fitting the models, and the last 10 observations as the out-of-sample partition. Automatic identification of ARIMA models was done using SSpace (Villegas and Pedregal, 2018) following the algorithm implemented in the forecast package in R (Hyndman and Khandakar, 2008). The fitted models were used to produce 1-to-7 steps-ahead predictions for each of the 15 series.

Once the individual models and predictions were calculated, reconciled forecasts were produced according to the different approaches discussed in Section 5, i.e., bottom-up, top-down and reconciled, using both hts (Hyndman et al., 2011) and SSpace (Villegas and Pedregal, 2018) implementations. The simulation was repeated 1000 times. Table 1 shows the Root Mean Squared Error (RMSE) in the out-of-sample for each of the approaches and for each of the 15 series. For convenience, an entry for the independent forecast has been also included, though not consistent with the hierarchy. The best alternative for each horizon and level is shown in bold. Since the bottom-up approach simply aggregates the bottom level forecasts all the way to the top level, results are equivalent for both hts and SSpace and they are shown in a single entry. On the other hand, different results are drawn for top-down and reconciled strategies, and RMSE values are shown separately for each implementation.

One important point is that all models automatically identified are exactly the same in both implementations (hts and SSpace). Thence, the accuracy differences observed in Table 1 are only due to the differences in reconciling approaches.

Since random ARIMA processes were used both to generate the series and (automatically) identify the models, the bottom-up strategy results favored, explaining its good performance. However, the value of this particular setup relays on providing a common ground for comparing existing approaches (hts) with the proposed approach (SSpace), leaving apart the aforementioned discussion on top-down vs bottom-up. The mean RMSE value for bottom-up (9.77) is indeed the best of all, even better than the independent forecasts (10.52 mean RMSE).

Table 1: RMSE for out-of-sample forecasting of the simulated data.

<table><tr><td rowspan="2"></td><td rowspan="2">Independent</td><td rowspan="2">Bottom-up</td><td colspan="2">Top-down</td><td colspan="2">reconciled</td></tr><tr><td>hts</td><td>sspace</td><td>hts</td><td>sspace</td></tr><tr><td>Total</td><td>28.59</td><td>24.30</td><td>28.59</td><td>28.59</td><td>26.66</td><td>24.63</td></tr><tr><td>A</td><td>18.50</td><td>16.64</td><td>35.28</td><td>18.50</td><td>17.97</td><td>16.89</td></tr><tr><td>B</td><td>18.93</td><td>16.88</td><td>34.95</td><td>18.74</td><td>18.42</td><td>17.24</td></tr><tr><td>AA</td><td>11.19</td><td>10.58</td><td>24.89</td><td>11.43</td><td>11.05</td><td>10.62</td></tr><tr><td>AB</td><td>10.78</td><td>9.86</td><td>25.05</td><td>10.83</td><td>10.70</td><td>10.09</td></tr><tr><td>BA</td><td>11.18</td><td>10.59</td><td>26.60</td><td>11.64</td><td>11.35</td><td>10.77</td></tr><tr><td>BB</td><td>10.58</td><td>9.71</td><td>28.95</td><td>10.37</td><td>10.54</td><td>9.88</td></tr><tr><td>AAA</td><td>6.01</td><td>6.01</td><td>15.92</td><td>6.42</td><td>6.32</td><td>6.11</td></tr><tr><td>AAB</td><td>6.54</td><td>6.54</td><td>21.39</td><td>6.99</td><td>6.77</td><td>6.48</td></tr><tr><td>ABA</td><td>5.88</td><td>5.88</td><td>16.28</td><td>6.39</td><td>6.30</td><td>5.93</td></tr><tr><td>ABB</td><td>5.76</td><td>5.76</td><td>17.52</td><td>6.18</td><td>6.23</td><td>5.95</td></tr><tr><td>BAA</td><td>6.25</td><td>6.25</td><td>19.85</td><td>6.76</td><td>6.61</td><td>6.33</td></tr><tr><td>BAB</td><td>6.19</td><td>6.19</td><td>22.43</td><td>6.72</td><td>6.59</td><td>6.28</td></tr><tr><td>BBA</td><td>5.69</td><td>5.69</td><td>29.05</td><td>6.00</td><td>6.12</td><td>5.77</td></tr><tr><td>BBB</td><td>5.72</td><td>5.72</td><td>24.85</td><td>6.02</td><td>6.12</td><td>5.77</td></tr><tr><td>Average</td><td>10.52</td><td>9.77</td><td>24.77</td><td>10.77</td><td>10.52</td><td>9.91</td></tr></table>

Some observations can be highlighted from Table 1. Regarding global averages (last row), results seem to be scattered around the independent forecasts (10.52), except for top-down[hts] value sitting apart (24.77), a finding in common with Hyndman et al. (2011). Reconciled[sspace] method (9.91) outperforms all alternatives except bottom-up (9.77), including the independent baseline (10.52).

Regarding top-down and reconciled approaches, SSpace systematically provides better results than the counterpart in hts for all series. This result comes to support the claim about the convenience of keeping consistency across time while reconciling across hierarchy. As previously discussed in Section 5, the proposed approach for reconciling forecasts also maintains consistency with models across time, which is expected to increase coherence and performance of the final system.

Pairwise t-tests for the 6 approaches were computed. As expected from results in Table 1, top-down[hts] vs the rest returned a p-value smaller than $10^{-8}$ for all possible comparisons. The best of all approaches is the bottom-up (being consistent with the experiment design as previously discussed) which compared to independent is said to be different with 99% of confidence (p-value $5.2 \times 10^{-4}$ ), but not significantly different from reconciled[sspace] (p-value 0.51). Finally, both reconciled approaches are different with 99% of confidence (p-value $7 \times 10^{-3}$ ).

## 7. Hierarchical demand forecasting

In this section we apply the proposed approach to predict the demand of a Spanish grocery retailer. The dataset contains daily observations on the sold units of 97 products covering the period 2013:Q1-2014:Q2. The hierarchical structure used is described in Table 2. The top level contains aggregated demand for the whole company. At level 1, demand is disaggregated by type of dish: first courses, pastas, meats, fish and desserts. At level 2 products are grouped in seventeen different families: salads, creams, omelets, other first courses, spaghetti, macaroni, beef, chicken, pork, lamb, other meats, cod, tuna, salmon, other fish, fruits and creamy desserts. And finally, at the bottom level we have 97 disaggregated series for the individual products, and the hierarchy therefore involves 120 time series (97 disaggregated and 23 aggregated).

Table 2: Hierarchy for grocery demand data

<table><tr><td>Level</td><td>N° of series per level</td><td>Aggregation vector</td></tr><tr><td>Company</td><td>1</td><td>[5]</td></tr><tr><td>Type of food</td><td>5</td><td>[4 2 5 4 2]</td></tr><tr><td>Family of products</td><td>17</td><td>[10 2 4 7 3 3 12 5 6 5 7 5 5 5 4 7 7]</td></tr><tr><td>Products</td><td>97</td><td></td></tr></table>

An optimal ARIMA model was selected for each series using the automatic identification algorithm in Hyndman and Khandakar (2008), as done in the simulation study discussed above. A rolling window procedure with 8 forecasting origins was implemented to produce 7-step-ahead forecasts, and the models were re-identified at every forecasting origin. Once more, top-down, bottom-up and reconciled approaches were computed using hts package and SSpace.

Table 3 contains the mean absolute percentage error (MAPE) for each forecast horizon and hierarchical forecasting approach. The table is organized in several blocks, one for each hierarchical level and the mean MAPE across all levels. MAPE for independent forecasts is shown in the first row of each section. The approach with smallest MAPE is shown in bold for each horizon. The last column contains the average MAPE across all forecast horizons. Since the bottom-up approach produces identical results in both implementations, they are shown in a single entry, while results for top-down and reconciled approaches are shown separately.

Some ideas emerge from this empirical study: (1) the bottom-up strategy is systematically out-performed in all horizons and levels by either top-down or reconciled approaches. (2) As we move down in the hierarchy, the reconciled approach excels at longer horizons (5, 6 and 7 steps ahead), while the top-down approach does better at shorter horizons (1, 2 and 3 steps ahead). (3) The SSpace approach seems to systematically out-perform hts implementation for longer horizons (4, 5, 6 and 7 steps ahead) both in top-down and reconciled approaches, while hts work better at shorter horizons in both approaches as well (with some exceptions, see for example Level 1 of Table 3).

## 8. Conclusions

In this paper, a new approach for hierarchical time series forecasting based on SS modelling is proposed as an essential part of a decision support system within a supply chain management framework. The key point is that the SS structure with its associated recursive algorithms provide a solution that preserves the time consistency of the forecasts, a property that is missing in all the previous approaches. Moreover, forecasts are always produced on the basis of past optimal forecasts, instead of focusing just on the raw forecasts at each single step, enhancing the coherency of the approach.

It is worth noting that the standard optimal filtering of the overall SS system by the Kalman Filter provides per se an elegant solution to the problem of hierarchical forecasting without any need to resort to additional algebra.

The new approach provides an unified treatment of top-down, bottom-up, middle-out and reconciled approaches reported in the literature. This is a further advantage of converting the hierarchical forecasting problem into a standard SS system. This fact simplifies the assumptions on which the approach relies on. For example, there is no need to formulate further assumptions about the way to disaggregate down the time series in top-down approaches (Gross and Sohl, 1990), or to propose any additional objective function in reconciled approaches (Hyndman et al., 2011).

Table 3: MAPE for out-of-sample forecasting of the alternative hierarchical approaches applied to a Spanish retailer demand data.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="8">Forecast horizon</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>AVG</td></tr><tr><td colspan="10">Top level</td></tr><tr><td>Independent</td><td></td><td>6.97</td><td>8.13</td><td>8.27</td><td>16.23</td><td>17.23</td><td>17.13</td><td>17.01</td><td>13.00</td></tr><tr><td>Bottom-up</td><td></td><td>7.60</td><td>10.14</td><td>10.12</td><td>17.42</td><td>18.77</td><td>18.61</td><td>18.61</td><td>14.47</td></tr><tr><td rowspan="2">Top-down</td><td>hts</td><td>6.97</td><td>8.13</td><td>8.27</td><td>16.23</td><td>17.23</td><td>17.13</td><td>17.01</td><td>13.00</td></tr><tr><td>sspace</td><td>6.97</td><td>8.13</td><td>8.27</td><td>16.23</td><td>17.23</td><td>17.13</td><td>17.01</td><td>13.00</td></tr><tr><td rowspan="2">reconciled</td><td>hts</td><td>7.15</td><td>8.15</td><td>8.18</td><td>15.96</td><td>17.69</td><td>17.39</td><td>17.61</td><td>13.16</td></tr><tr><td>sspace</td><td>7.14</td><td>9.12</td><td>10.96</td><td>18.79</td><td>18.80</td><td>17.20</td><td>17.00</td><td>14.14</td></tr><tr><td colspan="10">Level 1</td></tr><tr><td>Independent</td><td></td><td>10.84</td><td>10.98</td><td>10.74</td><td>18.61</td><td>20.31</td><td>21.03</td><td>20.18</td><td>16.10</td></tr><tr><td>Bottom-up</td><td></td><td>10.92</td><td>12.86</td><td>13.36</td><td>20.77</td><td>21.81</td><td>21.22</td><td>20.92</td><td>17.41</td></tr><tr><td rowspan="2">Top-down</td><td>hts</td><td>9.89</td><td>10.91</td><td>11.19</td><td>18.85</td><td>20.40</td><td>20.93</td><td>20.03</td><td>16.03</td></tr><tr><td>sspace</td><td>9.93</td><td>9.86</td><td>10.47</td><td>18.32</td><td>19.00</td><td>18.61</td><td>18.15</td><td>14.91</td></tr><tr><td rowspan="2">reconciled</td><td>hts</td><td>9.95</td><td>11.15</td><td>11.22</td><td>18.42</td><td>20.56</td><td>20.97</td><td>19.97</td><td>16.04</td></tr><tr><td>sspace</td><td>10.73</td><td>11.61</td><td>12.92</td><td>18.75</td><td>18.21</td><td>16.88</td><td>16.65</td><td>15.11</td></tr><tr><td colspan="10">Level 2</td></tr><tr><td>Independent</td><td></td><td>14.06</td><td>17.23</td><td>18.47</td><td>26.50</td><td>27.07</td><td>28.26</td><td>25.70</td><td>22.47</td></tr><tr><td>Bottom-up</td><td></td><td>15.92</td><td>20.48</td><td>21.89</td><td>29.33</td><td>30.53</td><td>30.43</td><td>28.43</td><td>25.29</td></tr><tr><td rowspan="2">Top-down</td><td>hts</td><td>14.05</td><td>16.66</td><td>17.94</td><td>26.78</td><td>27.40</td><td>28.37</td><td>25.64</td><td>22.41</td></tr><tr><td>sspace</td><td>17.11</td><td>20.82</td><td>20.83</td><td>27.24</td><td>28.72</td><td>28.10</td><td>25.85</td><td>24.10</td></tr><tr><td rowspan="2">reconciled</td><td>hts</td><td>13.95</td><td>15.20</td><td>17.13</td><td>26.80</td><td>27.64</td><td>28.49</td><td>25.70</td><td>22.13</td></tr><tr><td>sspace</td><td>15.76</td><td>17.80</td><td>20.04</td><td>26.38</td><td>25.92</td><td>24.68</td><td>22.93</td><td>21.97</td></tr><tr><td colspan="10">Bottom level</td></tr><tr><td>Independent</td><td></td><td>28.62</td><td>31.05</td><td>33.81</td><td>44.16</td><td>44.68</td><td>45.26</td><td>43.14</td><td>38.68</td></tr><tr><td>Bottom-up</td><td></td><td>28.62</td><td>31.05</td><td>33.81</td><td>44.16</td><td>44.68</td><td>45.26</td><td>43.14</td><td>38.68</td></tr><tr><td rowspan="2">Top-down</td><td>hts</td><td>28.21</td><td>30.26</td><td>32.42</td><td>43.57</td><td>43.78</td><td>44.54</td><td>42.14</td><td>37.85</td></tr><tr><td>sspace</td><td>32.01</td><td>32.63</td><td>34.40</td><td>43.72</td><td>44.03</td><td>43.38</td><td>41.50</td><td>38.81</td></tr><tr><td rowspan="2">reconciled</td><td>hts</td><td>28.52</td><td>31.31</td><td>33.32</td><td>44.95</td><td>45.58</td><td>46.40</td><td>43.72</td><td>39.11</td></tr><tr><td>sspace</td><td>30.39</td><td>31.42</td><td>33.08</td><td>42.52</td><td>41.95</td><td>41.15</td><td>39.97</td><td>37.21</td></tr><tr><td colspan="10">Average</td></tr><tr><td>Independent</td><td></td><td>24.98</td><td>27.66</td><td>29.53</td><td>38.93</td><td>39.53</td><td>40.14</td><td>38.05</td><td>34.12</td></tr><tr><td>Bottom-up</td><td></td><td>25.33</td><td>28.22</td><td>30.15</td><td>39.48</td><td>40.13</td><td>40.48</td><td>38.51</td><td>34.61</td></tr><tr><td rowspan="2">Top-down</td><td>hts</td><td>24.67</td><td>26.97</td><td>28.40</td><td>38.54</td><td>38.89</td><td>39.60</td><td>37.29</td><td>33.48</td></tr><tr><td>sspace</td><td>28.05</td><td>29.30</td><td>30.26</td><td>38.67</td><td>39.18</td><td>38.53</td><td>36.70</td><td>34.38</td></tr><tr><td rowspan="2">reconciled</td><td>hts</td><td>24.94</td><td>27.91</td><td>29.10</td><td>39.60</td><td>40.30</td><td>41.04</td><td>38.50</td><td>34.49</td></tr><tr><td>sspace</td><td>26.70</td><td>28.42</td><td>29.46</td><td>37.80</td><td>37.17</td><td>36.24</td><td>35.03</td><td>32.97</td></tr></table>

# ACCEPTED MANUSCRIPT

The SS framework permits the generalization of the problem by defining the type of each single node in a hierarchy by means of combined hierarchies. Such heterogeneity may be even time-varying, if required. Confidence intervals or prediction intervals may be built with the aid of the standard output of the Kalman Filter.

The new approach is evaluated on simulations and on real data of a Spanish grocery retailer. Both experiments show that the proposed approach provides significantly better results than existing approaches.

Future research may develop in many different directions, like i) extending this study to more data bases of different nature, ii) testing different forecasting methods for the base univariate time series, iii) finding algorithms to optimise the implementation of combined hierarchies, iv) practical implementation of the methods on real Supply Chains in real life to improve their management.

Certainly, Supply Chain Management is a field where the hierarchical forecasting is most appealing, since hierarchies embedded in the data appear naturally. Hierarchical forecasting helps in taking advantage of this hidden information to enhance better forecasts that will help to increase customer satisfaction, reduce inventory stockouts, schedule production more effectively, lower safety stock requirement, reduce product obsolescence costs, managing shipping better and improving pricing and promotion management.

## 9. Acknowledgements

This work was supported by the European Regional Development Fund and Spanish Government (MINECO/FEDER, UE) under the project with reference DPI2015-64133-R and by the Vicerrectorado de Investigación y Política Científica from UCLM by DOCM 31/07/2014 [2014/10340]. We also would like to thank two anonymous referees for their valuable comments.

## 10. References

Athanasopoulos, T., Hyndman, R., Kourentzes, N., and Petropoulos, F. (2017). Forecasting with temporal hierarchies. European Journal of Operational Research, 262(1):60–74.

Barnea, A. and Lakonishok, J. (1980). An analysis of the usefulness of disaggregated accounting data for forecasts of corporate performance. Decision Sciences, 11(1):17–26.

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., and Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control. John Wiley & Sons, 5th edition.

Boylan, J. (2010). Choosing levels of aggregation for supply chain forecasts. Foresight, 18:9–13.

Casals, J., Garcia-Hiernaux, A., Jerez, M., Sotoca, S., and Trindade, A. (2016). State-Space Methods for Time Series Analysis: Theory, Applications and Software. Forthcoming by Chapman and Hall/CRC.

Choi, T., Yu, Y., and Au, K. (2011). A hybrid sarima wavelet transform method for sales forecasting. Decision Support Systems, (51):130–140.

Commandeur, J., Koopman, S., and Ooms, M. (2011). Statistical software for state space methods. Journal of Statistical Software, 41(1):1–18.

Dangerfield, B. and Morris, J. (1992). Top-down or bottom-up: Aggregate versus disaggregate extrapolations. International Journal of Forecasting, 8(2):233–241.

Durbin, J. and Koopman, S. (2012). Time series analysis by state space methods. Number 38. Oxford University Press.

Fildes, R., Goodwin, P., and Lawrence, M. (2006). The design features of forecasting support systems and their effectiveness. Decision Support Systems, (42):351–361.

Fliedner, E. B. and Lawrence, B. (1995). Forecasting system parent group formation: An empirical application of cluster analysis. Journal of Operations Management, 12(2):119–130.

Fliedner, G. (1999). An investigation of aggregate variable time series forecast strategies with specific subaggregate time series statistical correlation. Computers & Operations Research, 26(10):1133 - 1149.

Fliedner, G. (2001). Hierarchical forecasting: Issues and use guidelines. Industrial Management & Data Systems, 101(1):5–12.

Granger, C. and Morris, M. (1976). Time series modelling and interpretation. Journal of the Royal Statistical Society. Series A, 139(2):246–257.

Gross, C. W. and Sohl, J. E. (1990). Disaggregation methods to expedite product line forecasting. Journal of Forecasting, 9(3).

Grunfeld, Y. and Griliches, Z. (1960). Is aggregation necessarily bad? The Review of Economics and Statistics, 42(1):1–13.

Gómez, V. (2015). Ssmmatlab: A set of matlab programs for the statistical analysis of state space models. Journal of Statistical Software, 66(9):1–37.

Harrison, P. and Stevens, C. (1976). Bayesian forecasting. Journal of the Royal Statistical Society. Series B (Methodological), (38):205–247.

Harvey, A. (1989). Forecasting, structural time series models and the Kalman filter. Cambridge university press.

Hyndman, R. J., Ahmed, R. A., Athanasopoulos, G., and Shang, H. L. (2011). Optimal combination forecasts for hierarchical time series. Computational Statistics & Data Analysis, 55(9):2579 - 2589.

Hyndman, R. J. and Khandakar, Y. (2008). Automatic Time Series Forecasting: The Forecast Package for R. Journal of Statistical Software, 3(27):1–22.

Hyndman, R. J., Lee, A. J., and Wang, E. (2016). Fast computation of reconciled forecasts for hierarchical and grouped time series. Computational Statistics & Data Analysis, 97:16 – 32.

Kahn, K. B. (1998). Revisiting top-down versus bottom-up forecasting. Journal of Business Forecasting Methods & Systems, 17(2):14.

Kalman, R. (1960). A new approach to linear filtering and prediction problems. Transactions of the ASME - Journal of Basic

Engineering, (82):35–45.

Koopman, S., Harvey, A., Doornik, J., and Shephard, N. (2009). STAMP 8.2: Structural Time Series Analyser and Modeller and Predictor. Timberlake Consultants Limited.

Lu, C., Lee, T., and Lian, C. (2012). Sales forecasting for computer wholesalers: A comparison of multivariate adaptive regression splines and artificial neural networks. Decision Support Systems, (54):584–596.

Lütkepohl, H. (1984). Forecasting contemporaneously aggregated vector arma processes. Journal of Business & Economic Statistics, 2(3):201–214.

Muir, J. W. (1979). The pyramid principle. In Proceedings of 22nd Annual Conference, American Production and Inventory Control Society, pages 105–7.

Orcutt, G., Watts, H., and Edwards, J. (1968). Data aggregation and information loss. The American Economic Review, 58(4):773–787.

Rostami-Tabar, B., Babai, M. Z., Ducq, Y., and Syntetos, A. (2016). Non-stationary demand forecasting by cross-sectional aggregation. International Journal of Production Economics, 170:297–309.

Sbrana, G. and Silvestrini, A. (2013). Forecasting aggregate demand: Analytical comparison of top-down and bottom-up approaches in a multivariate exponential smoothing framework. International Journal of Production Economics, 146(1):185 – 198.

Shlifer, E. and Wolff, R. (1979). Aggregation and proration in forecasting. Management Science, 25(6):594–603.

Strijbosch, L. W. G., Heuts, R. M. J., and Moors, J. J. A. (2008). Hierarchical estimation as a basis for hierarchical forecasting. IMA Journal of Management Mathematics, 19(2):193–205.

Sun, Z., Choi, T., Au, K., and Yu, Y. (2008). Sales forecasting using extreme learning machine with applications in fashion retailing. Decision Support Systems, (46):411–419.

Taylor, C., Pedregal, D., Young, P., and Tych, W. (2007). Environmental time series analysis and forecasting with the captain toolbox. Environmental Modelling & Software, 22(6):797–814.

The MathWorks, Inc (2018). MATLAB - The Language of Technical Computing, Version R2015b. Natick, Massachusetts. URL http://www.mathworks.com/products/matlab/.

Villegas, M. A. and Pedregal, D. J. (2018). Sspace: A toolbox for state space modelling. Journal of Statistical Software, in press.

Weatherford, L., Kimes, S., and Scott, D. (2001). Forecasting for hotel revenue management: Testing aggregation against disaggregation. The Cornell Hotel and Restaurant Administration Quarterly, 42(4):53 – 64.

Widiarta, H., Viswanathan, S., and Piplani, R. (2009). Forecasting aggregate demand: An analytical evaluation of top-down versus bottom-up forecasting in a production planning framework. International Journal of Production Economics, 118(1):87 – 94.

Young, P., Pedregal, D., and Tych, W. (1999). Dynamic harmonic regression. Journal of forecasting, 18(6):369–394.

Zellner, A. and Tobias, J. (2000). A note on aggregation, disaggregation and forecasting performance. Journal of Forecasting, 19(5):457–465.

# ACCEPTED MANUSCRIPT

## Biography

Marco A. Villegas studied computer engineering and received his Masters degree in Computing from Universitat Politècnica de Catalunya (Spain) in 2012. After a few years of working experience as a dataminer, he completed his Ph.D. in State Space modeling for time series analysis in 2018 at the University of Castilla-La Mancha, in Ciudad Real. His research interests focus on data mining, pattern recognition, time series analysis, and their applications in business analytics contexts.

Diego J. Pedregal is a Professor at the Business Administration department of Universidad de Castilla-La Mancha (Spain). He received his first degree in Economics (Econometrics and Time series analysis) in June 1991 from the Universidad Autónoma de Madrid (UAM, Spain); his M.A. in Public Finance in June 1992 from the Institute for Fiscal Studies (Spain); his Ph.D. in March 1995 from the UAM; and enjoyed a post-doc position at Lancaster University (UK). His research interests include the identification and estimation of linear and nonlinear systems, and state space methods applied to time series and forecasting, with applications to Economics and Engineering.

## Highlights

\- Decision Support System built based on hierarchical forecasting systems in a State Space framework.

\- Forecasts are produced consistently across the hierarchy AND along time. This second dimension never taken into account in previous studies.

\- The State Space form subsumes top-down, bottom-up, middle-out and reconciled reported on previous literature as particular cases.

\- The Kalman Filter working on the State Space model provides elegantly the optimal solution without any need for further algebra.

![](/api/attachments/GAUV26KX/fulltext/images/1cb2d26ad14fdcbeb240a841670688356b62637f90c96a4c5b4cd31089029c96.jpg)  
Figure 1

![](/api/attachments/GAUV26KX/fulltext/images/bf2b4ac118f68128e3aecc58235230057de728665766227120aeedd024f0828d.jpg)  
Figure 2

![](/api/attachments/GAUV26KX/fulltext/images/ea2ee8eadaf158ac134c5adab5a6b1f554623efdb79998deb89ebbd7b7f93e0a.jpg)  
Figure 3
