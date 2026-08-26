---
otero_id: 17155
otero_key: "QZBQPDA7"
title: "Task-allocation between DSS and problem owner: The example of box & jenkins time-series analysis"
authors: "Han G. van Dissel; Hans P. Borgman; Adrie J.M. Beulens"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90028-p"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Task-Allocation between DSS and Problem Owner: The Example of Box & Jenkins Time-series Analysis

Han G. van DISSEL\*, Hans P. BORGMAN\* and Adrie J.M. BEULENS\*\*

\*Rotterdam School of Management, Erasmus University, Rotterdam, The Netherlands

\*\*Haagse Hogeschool, Den Haag, The Netherlands

The advent of so-called knowledge-based elements in DSS seems to shed new light on the allocation of tasks between decision maker and DSS. Expert Systems or Knowledge Based DSSs incorporate domainknowledge, thereby taking over tasks that used to be the sole responsibility of users and enabling non-expert decision-makers to make expert-quality decisions. In view of these new capabilities, we critically analyse in this article the task-allocation between these 'enhanced' DSSs and the problem-owner. The discussion is based on a framework in which the unstructured nature of DSS-tasks and the implied goals of the problem-owner play a central role. The implications are illustrated with a case on Box-Jenkins time-series analysis, a typical example of a DSS application based on an elaborate mathematical model for a relatively complex task.

Keywords: Problem Specification, Task-Allocation, Decision Support, Time-series Analysis.

## 1. Introduction

‘Sales are going down, what’s causing it?’ ‘I want this new facility for my division, but how can I justify it?’ These are typical questions for which DSS’s have traditionally been claimed to ‘make a difference’. It is however a long way from these vague unprecize questions to the formal financial scenario’s and LP-matrices that many DSS’s employ. ‘Problems do not come neatly packaged’, Keen and Scott Morton [8] already noted in their seminal work in 1978, and the single most important goal in using a DSS is to ‘package’ the problems, to provide insight into the problem structure [1,5].

Based on this notion we will develop a framework for tasks and knowledge involved in using a model-based DSS. The focus will be on the question as to which tasks can be taken over by the DSS. This question has become relevant since the advent of knowledge-based elements. Abstracting from technological (im)possibilities, the issue seems to center down on the goals and nature of DSS-tasks.

After describing the framework, an example will be presented on the use of DSS for time series analysis using the Box & Jenkins approach. An application for which numerous DSS software tools have been developed and which is typical for DSS-applications based on an elaborate mathematical model for a relatively complex task. For those unfamiliar with the Box & Jenkins technique, a short introduction is provided. We end with a discussion of the example, placed within the framework presented.

## 2. Nature of Goals of DSS-Tasks

Although a generally accepted definition of the term DSS still seems to be lacking, most authors agree on at least a few key concepts $[8,17]$ . One of them is support of the decision maker, as opposed to replacement. Another is the concept of semi- or unstructuredness of the task for which the DSS is employed. For our discussion it is important to operationalize this latter concept. Referring to $[12,14,16]$ the degree of unstructuredness of a problem is defined here as the incompleteness of the problem owner's specification of:

\- initial state, including available resources,

– goal state, including evaluation criteria,

\- possible alternatives and their consequences (required transformations).

As Taylor [17] argues, unstructuredness is not a characteristic of the task or problem itself but a perception of the problem owner. A problem which appears well-structured to one person can be highly unstructured to another.

If problem solving is viewed as a state-space transformation from an initial state to a goal state, given a set of constraints, then it is by definition impossible to 'solve' an unstructured problem. Problem solving demands a complete and formal specification of the problem and it is just this what lacks in 'unstructured' problems. Support in a DSS should therefore focus primarily on structuring the problem, i.e. on providing the problem owner with insight into the initial state, the goal state and possible alternatives and their consequences.

The role of formal (O.R.-)models in DSS is, in the above view, twofold. In the first place they play an essential role as a feedback mechanism in the decision cycle (see fig. 1). By inspecting and interpreting model-results one can better comprehend and – if necessary – adjust the problem specification. This forces problem owners to be explicit about relevant parameters, assumptions and preferences and will allow them to gain insight into the structure of the problem.

The second – and more obvious – role of the formal models is to ‘solve’ the problem, once it has been completely and formally specified. It will however be clear that where non-trivial problem domains are concerned, ‘complete’ specifications are unfeasible so some adjustment of the ‘solution’ on the part of the user will still be required, making insight into the problem structure even more important.

Summarizing the above, we can state that in DSS-tasks two distinct types of knowledge are involved:

\- knowledge about the problem structure. The implied goal of using a DSS is first and foremost to bring structure into a problem which is in the perception of the problem owner as yet more or less unstructured. The problem owner wants to gain knowledge about the problem structure.

<table><tr><td></td><td>low</td><td>high</td></tr><tr><td>low</td><td>A</td><td>B</td></tr><tr><td>high</td><td>C</td><td>D</td></tr></table>

Fig. 2. Types of Knowledge Involved in Using a Model-Based DSS.

\- modelling knowledge. The importance of formal (mathematical) models in DSS-tasks, as described above, demands a certain proficiency of DSS-users in formulating, using and appraising these models and their outcomes.

Fig. 2 shows both dimensions in a $2 \times 2$ matrix. As stated above, the essence of using a DSS is represented in the transition from low to high problem structure knowledge, i.e. in the matrix from cell A to cell B. Since using a DSS automatically implies modelling (be it in mathematical terms or any other) of the problem domain, modelling knowledge is also involved. Note however that to the problem owner cell C has little added value over cell A and cell D not over B. In the case of a real world problem, problem owners have no direct interest in the abstract DSS-model or in modelling aspects, their concern is in real problems and solutions.

![](/api/attachments/QZBQPDA7/fulltext/images/ceed25b0d77393c136df0bf07b7ca359733894348ebd41e0c699a1764770e443.jpg)  
Fig. 1. The Decision Cycle in Using a Model-Based DSS.

We will refer to the distinction between problem structure knowledge and modelling knowledge in our discussion of DSS enhancements and their implications for task-allocation in the next sections. This discussion will be illustrated with a case description of a typical DSS-task, namely time series analysis, both from a decision maker's and from a mathematical modelling viewpoint.

## 3. Box & Jenkins Time Series Analysis

Forecasts may help managers in organizations in their decision making by determining likely consequences of decisions and reducing uncertainty. Consequently the modelling of a system to obtain is not a goal by itself but an important component in the context of a decision making process. In real world situations a good forecaster is pragmatic in the sense that given the problem context he will use whatever works to give a good forecast.

A series of discrete equidistant observations of a variable ordered by the time in a dynamic system is usually called a time series. Time series analysis is used to transform descriptive data into explanatory data. The observed series $z_{t}$ for $t = 1, 2, \ldots, n$ of a time series are considered realisations of a stochastic process. The basic assumption is that the processes underlying the data will evolve in the future and that the observations available may be used to determine the characteristics of the stochastic process which generated the observations. Time series analysis can be applied to obtain an ex post insight in the behaviour of a system and to forecast the behaviour of the system using a model of it.

For the analysis of time series a number of methods are available. One group of methods assumes that the values (observations) of the time series are statistically independent. Examples are regression analysis and exponential smoothing. The models of this group of methods have the generic form:

$$
z _ {t} = f \left(x _ {1}, x _ {2}, \dots , x _ {n}; t\right) + a _ {t},
$$

where $a_{t}$ is the random error component and $x_{1},\ldots,x_{n}$ are the exogenous variables.

Another group of methods does not make the assumption of independence of the observations. The successive values of the time series are dependent as functions of common error terms. The Box & Jenkins method (Box and Jenkins, 1970) uses the dependency between observations to produce forecasts that are in general likely to be more accurate than forecast generated with regression analysis or exponential smoothing. The Box & Jenkins method is based on a linear filter model. The linear filter operation consists of taking the weighted sum of foregoing observations. In a linear filter a so called white noise series is transformed to an output series $z_t$ by a linear filter $\Psi$ . This group of models has the following form:

$$
z _ {t} = \mu + \Psi_ {0} a _ {t} + \Psi_ {1} a _ {t - 1} + \Psi_ {2} a _ {t - 2} + \dots ,
$$

where $\mu$ is the average of the series, $a_{t-i}$ the error term in period t-i and $\Psi_{i}$ the parameter corresponding to $a_{t-i}$ . If the series is stationary the observations fluctuate around the average $\mu$ . It can be shown that many useful time series models exist that are special cases of this model. An example of such a special case is an autoregressive process of order p:

$$
z _ {t} = \mu + \Phi_ {1} z _ {t - 1} + \Phi_ {2} z _ {t - 2} + \dots + \Phi_ {p} z _ {t - p} + \epsilon_ {t}.
$$

This model relates $z_{t}$ to the linear cumulation of foregoing values plus an error $\epsilon_{t}$ . Similar it is possible to relate $z_{t}$ linear to the foregoing $\epsilon$ 's and obtain a moving average process of order q:

$$
z _ {t} = \mu + \epsilon_ {t} - \Theta_ {1} \epsilon_ {t - 1} - \Theta_ {2} \epsilon_ {t - 2} - \dots - \Theta_ {q} \epsilon_ {t - q}.
$$

Combining the autoregressive and moving average processes gives:

$$
\begin{array}{r l} z _ {t} & = \mu + \Phi_ {1} z _ {t - 1} + \Phi_ {2} z _ {t - 2} + \dots + \Phi_ {p} z _ {t - p} - \Theta_ {1} \epsilon_ {t - 1} \\ & - \Theta_ {2} \epsilon_ {t - 2} - \dots - \Theta_ {q} \epsilon_ {t - q} + \epsilon_ {t} \end{array}
$$

which is called an ARMA model of order $(p, q)$ .

The Box & Jenkins models [2] represent a generalized class of univariate and multivariate time series model. Only one class, the so called ARIMA (Auto Regressive Integrated Moving Average) models, a class of univariate models which takes only one time series into account, will be dealt with in this case. Integrated indicates that before determining the order of p and q often a discrete difference of the original series is taken to obtain a stationary series. By convention the structure of an ARIMA model is described by $(p, d, q) \times (P, D, Q)L(\lambda)$ . With p, P and q, Q as the number of normal and seasonal autoregressive and moving average terms respectively, d and D the number of normal and seasonal differences, L the period length of the season and $\lambda$ the transformation applied to the series.

![](/api/attachments/QZBQPDA7/fulltext/images/d4efa7c2fad44ab6816d0e1e37e52eeeeee5d99c246d0c489d0ce609ad19c88c.jpg)  
Fig. 3. The Box & Jenkins Method for Time Series Analysis. The Dashed Line Represents an Additional Iterative Loop Observed in Practice.

## 4. Tasks and Knowledge Involved

In the book of Box and Jenkins [2] a method for analysing and forecasting time series using linear filter models is described. Fig. 3 depicts the main steps in their method. In the first step a class of models is chosen. Taking the decision making context and the time series that are available into account an analyst may e.g. choose to identify an ARIMA or Transfer Function model. Transfer Function models relate the behaviour of one or more input series to the behaviour of an output series. In the second step an analyst must identify a specific structure of the model from the general class of models.

To help the analyst to make decisions on the structure he can use a number of identification tools, e.g. spike diagrams of the Auto Correlation Function (ACF) and the Partial Auto Correlation Function (PACF), a range-mean plot of the series, or just a graph of the original or transformed series. All these tools are based on a number of mathematical transformations which can be programmed. The choice of a specific model structure will depend on the analyst. To use these tools effectively demands a lot of statistical and modelling knowledge from the analyst.

In essence, in the case of an ARIMA-model, during the identification first the transformation needed to obtain a stationary time series has to be identified and secondly the order of the normal and seasonal autoregressive and moving average parameters by comparing the sample ACF and PACF patterns to patterns that can theoretically be expected. In practice the choice of a model will often depend on the quality and availability of the data. The third step is completely programmable by way of an optimization algorithm which estimates, provided that the correct model has been selected, the parameter values of the identified model. In the fourth step the estimated model must be validated both quantitatively and qualitatively using the residuals of the estimated model as control. Again a number of programmable tools are available such as e.g. a spike diagram of the residuals, the ACF and PACF of the residuals or a periodogram. In the fifth step the estimated and checked model can be used for generating forecasts and determining confidence intervals.

During the time series analysis process a number of decisions have to be made by the analyst who also has to relate the results obtained to the decision context. Especially during the model identification often a lot of non-statistical considerations are taken into account (see e.g. [3]). The suggestion that is given by fig. 3 that only one major decision moment exists when applying the Box & Jenkins method is an oversimplification of the actual real world time series modelling process and only based on statistical modelling principles. In practice the modelling process also involves the interpretation of the problem context and is an iterative process where users, when applying the method, may execute the steps in different sequences. If adequate interactive computer-software is available which allows for immediate feedback one will find, by observing analysts, that, especially for deciding on the stationarity of the series and including contextual assumptions in the model structure, the identification step is executed many times, until satisfying results are obtained.

Only hereafter will the identified model be estimated.

There are a number of potential problems related to the use of the Box & Jenkins method in practice. In the first place, to use the method effectively and efficiently, apart from extensive expertise in the application of the method, also knowledge of the decision making situation and the ability to translate this knowledge is required. On top of this many commercially available packages are not only calculation intensive but also require a lot of experience to use them. Especially the interpretation of the results obtained from the mathematical transformations applied is often difficult and inconclusive.

For time series analysis an analyst can be supported by providing efficient computerized tools for data management, model management and evaluating decision alternatives. The DSS concepts offer a framework for building information systems to support users in this type of decision making processes.

## 5. Different Approaches for Task-Allocation

In [4] we discussed the functional requirements, design and implementation of a Box & Jenkins time series analysis package, developed for use within a major dutch bank. This package is an example of what we would like to call a first generation DSS. A set of well known mathematical algorithms were programmed and made accessible by building a very user-friendly interactive software package around them. The main assets lie in the user-friendliness of the system and in the fact that relatively few computer-knowledge is required to use the package. However problems that are inherent to the method used such as e.g. the amount of statistical knowledge needed for order selection during model identification, were not solved by the package. The 'solution' in the case of the dutch bank was to have the analyses done by an O.R.-specialist who is familiar with the statistical intricacies acting as an intermediary for the actual problem owner. Many examples of this type of 'first-generation' DSS have been described in literature (see e.g. [9,10,13,18]). More recently the limitations of this kind of DSS applications have been recognized. New approaches to make

DSS even more useful have been proposed for the DSS field.

In principle two different approaches may be followed for improving DSS in the case of Box & Jenkins time series analysis. The first type of approach we would like to call statistics-bound. This approach is a logical consequence of the decision optimizing paradigm often found in the operations research discipline. By improving algorithms or inventing new ones one may try to optimize or limit the number of decisions that has to be made by the analyst. This type of approach reduces the modelling knowledge needed. In the case of the Box & Jenkins method much work has been published on statistical criteria which can be used in the order selection process to decide which model structure fits best on the available data (see $[15]$ for an extensive overview). Examples of such criteria are the Swartz criterium and the Akaike Information Criterium (AIC). For example the AIC leads to choosing the model for which the expression:

$$
A I C _ {(p, q)} = \ln \left[ \sigma_ {(p, q)} ^ {2} + 2 (p + q) / T \right]
$$

is minimized. In this formula p and q designate the order of the ARMA model, T the number of observations and $\sigma_{(p,q)}^{2}$ is the maximum likelihood estimator of the disturbance variance. Examples of commercially available software that include these tests and automatically determine the ‘optimal’ model specification for a given time series, using a (statistical) rule-based expert system approach, are AutoBox Plus and Forecast Pro (see [11] for a comparative review of these and other forecasting programs). This statistics-bound approach leads independent of the forecaster in principle to the same choice of model structure.

However in practice it may be less desirable to use them since they do not explicitly allow for including any context knowledge. To allow context knowledge to be included in the model statistical criteria are often not very appropriate because they are derived from the input series only. Important information, like e.g. the nature of an intervention that could affect the forecast, is not always implicitly included in the time-series and hard or impossible to detect by statistical criteria only. Another drawback is that if one uses automatic model generation and fitting, models are often difficult to interpret. An important aspect of time series analysis is that users often prefer to use models they understand (they reflect the behaviour of part of the object system as they understand it) over models with best mathematical fit as for example generated by the aforementioned automatic model generation software.

With respect to the applicability of the Box & Jenkins time series analysis and forecasting method there have been and continue to be mixed feelings. Often made remarks are that the method is too difficult to use due to the amount of statistical modelling knowledge needed and that the method can not be applied if there are not enough historic values of the time series. The latter may occur for many economic or financial time series where there are problems with the normalization, availability, integrity and accuracy of historic values. In this area analyst often seem to prefer to postulate and use simple regression models that one can understand. These models may perform in such cases equally well as Box & Jenkins models. In the technical field the situation is a bit different. In many cases enough observations of time series are available with adequate integrity and accuracy for Box & Jenkins analysis.

A second type of approach for improving DSS we would like to call context-bound. This approach is different from the approach based on statistical optimization. E.g. instead of striving to identify the statistically ‘optimal’ model solely based on an input time series the forecaster is now explicitly involved in the order selection process on the basis of context knowledge. This ‘context knowledge’ may cause him to choose to identify a simpler model than statistically optimal, because in a certain context communicating the model to others is very important. Or he may opt for a particular model because he knows of comparable situations where the same kind of model has been very successful. While these practices may methodologically be doubtful, for practical work they can be very convincing. Another important reason to use the context-bound approach is in the possible inclusion of information which is not explicitly or implicitly included in the time series used. Examples of this non-included information are interventions like a new marketing campaign, or the discovery of a new replacement product that seriously affects the forecast. Especially applying expert systems technology has been suggested to further improve context type of support given by a

DSS. Keen [9] called this type of DSS: enhanced-DSS. Approaches where additional support is given by including expert system type of technology do allow for the inclusion of context knowledge. These system are sometimes called expert support systems to separate them from the typical expert systems and admitting the role of the human expert in providing the overall problem solving direction as well as specific knowledge not incorporated in the system [7].

From these points the use of the Box & Jenkins method can be improved if more of the qualitative context criteria with respect to the choice of a class of models to be used and with respect to the identification of the model structure can systematically be included into the application software. For the user the opportunity is then created to enter context knowledge about the object system which is incorporated into the time series models to be analysed.

As an example we may take a real world production process. On a production line in a continuous process sequences of chocolate bars are made on parallel lanes. For operational control it is important to keep track of product measurements (size and weight). If forecasts are generated that these measurements get out of predefined limits an intervention is done and process control parameters are adjusted. Time series data are amply available, well defined and accurately to measure. As a result Box & Jenkins time series analysis and forecasting can and has been used to support the control of the process. There is a lot known about this control system that one would like to incorporate into the analysis process. For example statistical analysis of produced measurements revealed a systematic non-time dependent variance over product lanes. Further analysis over all product lanes revealed that the processes seem to drift towards the control limits, unless certain control measures are taken and unless some other intervention suddenly changes the direction of the drift. It was felt that one should be able to enter this information on the object system into the forecasting system and that this information should be reflected in the final model selected. This thus means that the object system-model knowledge is reflected in the time series model and preferred over the best fit generated on the basis of statistical optimization. For the example this implied that one had to use separate time series for the different lanes, that to model the time independent behaviour and the drift a MA component had to be incorporated and that intervention models had to be used. All these reflecting the context knowledge available.

## 6. Conclusion

Providing problem owners with insight into the problem structure is the important goal of using a DSS. Formal (mathematical) models can and do play an important role in this process, but many problem owners lack the modelling knowledge needed to conceptualize, specify and interpret them. Using expert-system techniques to automate this modelling process can help to close the knowledge gap between problem owner and model-based DSS. The danger with statistics bound approaches is that during the modelling process assumptions will have to be made by the system about parameters or specific context information not included in the initial (vague and incomplete) problem specification. This implies that the original intention of DSS to “support rather than replace the decision maker” [8] gets lost, leading possibly to a solution which may be optimal from a mathematical viewpoint but which mismatches the real problem situation (Mitroff’s ‘error of the third kind [19]).

Context-bound approaches do not seem prone to this type of error. Their inherent danger however is that abstract DSS-models are often too distant from the problem owner's context-bound terms, thereby requiring more modelling knowledge than we can reasonably expect. Combining both approaches indicated in this article, focussing on the problem owner's goals, is probably the best way to ensure continuing success for DSS.

## 7. References

[1] Ackhoff, R.L. (1979). The Future of Operational Research is Past, Journal of Operational Research Society, Vol 30, No. 2.

[2] Box, G.E.P. & Jenkins, G.M. (1970). Time-series Analysis. Forecasting and Control. Holdon Day, San Francisco.

[3] Butter, F.A.G. den & Verbon, H.A.A. (1983). The Specification Problem in Regression Analysis. In: Time-Series Analysis: Theory and Practice 3, O.D. Anderson (ed), North-Holland Publ. Comp, Amsterdam.

[4] Dissel, H.G. van, Beulens, A.M.J. & Gels, M.C. (1984). The DSS Approach for the Design and Use of a Box & Jenkins Time-Series Analysis and Forecasting Package. Informatie, 26, 6 (article in Dutch).

[5] Holtzman, S. (1989). Intelligent Decision Systems. Addison-Wesley, Reading, Mass.

[6] Houdeshel, G. & Watson, H.J. (1987). The Management Information and Decision Support (MIDS) System at Lockheed-Georgia. MIS Quarterly, 11, 1.

[7] Luconi, F.L., Malone, T.W. & Scott Morton, M. (1986). Expert Systems: The Next Challenge for Managers. Sloan Management Review, Summer.

[8] Keen, P.G.W. & Scott Morton, M. (1978). Decision Support Systems: An Organizational Perspective. Addison-Wesley, Reading, Mass.

[9] Keen, P.G.W. (1986). Decision Support Systems: The Next Decade. In: Decision Support Systems: a Decade in Perspective, McLean, E.R. & Sol, H.G. (eds.), North-Holland Publ. Comp., Amsterdam.

[10] Nunen, J.A.E.E. van & Benders, J. (1982). A Decision Support System for Location and Allocation Problems within a Brewery. Operation Research Proceedings 1981, Springer Verlag, Berlin.

[11] PC-Magazine, (1989). Inside the World of Numbers. Vol. 8, no 5.

[12] Reitman, W.R. (1964). Heuristic Decision Procedures, Open Constraints and the Structure of Ill-Defined Problems. In: M.W. Shelly II & Bryan, G.L. (eds.), Human Judgments and Optimality. Wiley, New York.

[13] Sauder, R.L. & Westerman, W.M. (1983). Computer Aided Train Dispatching: Decision Support Through Optimization. Interfaces, 13, 6.

[14] Schwenk, C.R. (1983). Laboratory Research on Ill-Structured Decision Aids: The Case of Dialectical Inquiry. Decision Sciences, 13.

[15] Sneek,, J.M. (1984). Modelling Procedures for Univariate Time Series. VU Uitgeverij, Amsterdam.

[16] Taylor, R.N. (1974). Nature of Problem Ill-Structuredness: Implications for Problem Formulation and Solution. Decision Sciences, 5.

[17] Taylor, R.N. (1988) Affective Responses with a Complex DecisionMaking Task: The Influence of ‘Perceptually’ Ill-Structured Problems. Decision Sciences, 19.

[18] Thierauf, R.J. (1982). Decision Support Systems for Effective Planning and Control. A Case Study Approach. Prentice Hall, Englewood Cliffs, N.J.

[19] Mitroff, l I.I. & Featheringham, T.R. (1974). On Systemic Problem Solving and the Error of the Third Kind. Behavioral Science. Vol. 19.
