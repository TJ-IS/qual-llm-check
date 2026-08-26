---
otero_id: 9376
otero_key: "S9BR6B2Q"
title: "ForeSim-BI: A predictive analytics decision support tool for capacity planning"
authors: "Duarte Dinis; Ângelo Palos Teixeira; Ana Barbosa-Póvoa"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113266"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ForeSim-BI: A predictive analytics decision support tool for capacity planning

Duarte Dinis<sup>a,⁎</sup>, Ângelo Palos Teixeira<sup>b</sup>, Ana Barbosa-Póvoa<sup>a</sup>

<sup>a</sup> Center for Management Studies, Instituto Superior Técnico, Universidade de Lisboa, Lisboa, Portugal

<sup>b</sup> Center for Marine Technology and Ocean Engineering, Instituto Superior Técnico, Universidade de Lisboa, Lisboa, Portugal

## A R T I C L E I N F O

Keywords: Decision support systems Predictive analytics Capacity planning Forecasting Maintenance

## A B S T R A C T

This paper proposes a decision support tool for maintenance capacity planning of complex product systems. The tool – ForeSim-BI – addresses the problem faced by maintenance organizations in forecasting the workload of future maintenance interventions and in planning an adequate capacity to face that expected workload. Developed and implemented from a predictive analytics perspective in the particular context of a Portuguese aircraft maintenance organization, the tool integrates four main modules: (1) a forecasting module used to predict future and unprecedented maintenance workloads from historical data; (2) a Bayesian inference module used to transform prior workload forecasts, resulting from the forecasting module. into predictive forecasts after observations on the maintenance interventions being predicted become available; (3) a simulation module used to characterize the forecasted total workloads through sets of random variables, including maintenance work types, maintenance work phases, and maintenance work skills; and (4) a Bayesian network module used to combine the simulated workloads with historical data through probabilistic inference. A linear programming model is also developed to improve the eficiency of the decision-making process supported by Bayesian networks, The tool uses real industrial data, comprising 171 aircraft maintenance proiects collected at the host organization, and is validated by comparing its results with real observations of a given maintenance intervention to which predictions were made and with a model simulating current forecasting practices employed in industry. Significantly more accurate forecasts have been obtained with the proposed tool, resulting in an im portant cost saving potential for maintenance organizations.

## 1. Introduction

Capacity planning is of the utmost importance in a multitude of sectors [1–3]. In Maintenance, Repair, and Overhaul (MRO) organizations it allows the prediction of the amount and types of resources required to perform the maintenance interventions, in particular man power diferentiated by skills. For complex product systems<sup>1</sup> [4], which include aircraft and aircraft engines, locomotives and trains, ships, but also industrial plants, refineries and wind turbines, to name a few, the maintenance work is divided between scheduled maintenance [5], consisting in prespecified inspection tasks carried out at predetermined intervals and whose workload is essentially deterministic, and unscheduled maintenance [6], which depends on the probabilistic nature of failures and whose workload is inherently stochastic and can reach up to > 50% of the total work [5]. Several maintenance capacity planning approaches have been proposed to be used in industrial practice [1]. Al-Fares and Dufuaa [7] divide these approaches between deterministic and stochastic. Applied to maintenance contexts, examples of the former include the work of Dijkstra et al. [8], in which a decision support system based on optimization models is developed to determine the size and composition of aircraft maintenance teams, or the work of Yan et al. [9], in which a mathematical programming model is developed considering multiple types of maintenance certificates. An example of the latter include the work of De Bruecker et al. [10], that addresses an aircraft maintenance workforce problem with mixed integer linear programming and heuristic techniques, or the work of Kurz [11], that presents an aircraft engine overhaul capacity planning problem modelled as a queuing network. Not specifically directed at maintenance, De Bruecker et al. [12] presents an extensive literature review regarding workforce planning problems.

As recognized by Al-Fares and Dufuaa [7], forecasting is an essential component of the capacity planning process, as it allows MROs to estimate the workload of future maintenance interventions. Several forecasting methods have been proposed in the literature [13]. Sanders and Manrodt [14] state that, despite the advancements on quantitative forecasting theory, most organizations still rely on judgmental fore casting practices [15], which are considered less accurate and subjected to biases. To the best of the authors' knowledge, common forecasting practices employed by MROs include rudimentary quantitative approaches such as descriptive statistics and simple linear regression, adjusted posteriorly through judgemental techniques such as overplanning [16], in what is known as integrating forecasting [17]. High environmental uncertainty and data variability [14] are determinant factors in making MROs to rely on such approaches, despite the extensive amount of available historical data and the use of sophisticated Enterprise Resource Planning (ERP) systems [18], which are often im plemented not without challenges [19]. Nonetheless, examples of the application of quantitative forecasting approaches to maintenance contexts include the work of Salman [20], in which time series techniques are used to predict the workload of electronic components in a weather forecasting system, and the work of Eickemeyer et al. [21], in which Bayesian networks are used to forecast human and machine hours for the regeneration of complex product systems.

This paper proposes ForeSim-BI, a tool to support the capacity planning process of maintenance organizations of complex product systems from a predictive analytics (PA) perspective [22]. The motivation for the development of the proposed tool is the inability of current approaches in accurately forecasting the workload of future maintenance interventions and in planning an adequate capacity to face that expected workload. To address this challenge, ForeSim-BI was developed and implemented in the particular case of a Portuguese aircraft MRO, in cooperation with industry experts and according to their inputs and needs, and is based on 171 aircraft maintenance projects collected at the host organization. The tool consists in the integration of four diferent modules – a forecasting module, a Bayesian inference (BI) [23] module, a simulation module, and a Bayesian network (BN) [24] module – into a single decision support tool (Fig. 1). Through the in tegration of the developed modules, a common solution for decision support tools addressing maintenance planning [8,25,26], ForeSim-BI improves the forecasting capabilities of maintenance organizations by providing more accurate workload forecasts than current employed approaches, while dealing more efectively with the uncertainty of the capacity planning process. On the one hand, papers addressing maintenance capacity planning such as [8–11] do not explicitly consider the uncertainty of the workload, nor its evolution through time. On the other hand, papers addressing maintenance forecasting such as [20,21] do not explicitly consider updating mechanisms with the acquisition of new information, nor the characterization of the workloads through diferent variables of interest. The consideration of all these aspects is an innovation of the proposed tool, which is expected to decrease the amount of overestimated resources, i.e. those resources estimated in higher quantities than those found to be needed during the maintenance interventions, and underestimated resources, i.e. those that are not estimated in suficient quantities, thus improving the operational and financial performance of MROs.

The developed tool is tested and validated by comparing simulated workloads with real workload values of a maintenance intervention to which predictions were made and with a model simulating current forecasting practices employed in industry.

The remainder of the paper is organized as follows. In Section 2, the used dataset is characterized. In Section 3, the modules of the proposed tool are presented and the tool is validated with real data referring to aircraft maintenance interventions. Finally, in Section 4, conclusions are drawn on the performed work and future research opportunities are identified.

## 2. Maintenance data

## 2.1. Data characteristics

The proposed tool is intended to be applicable to a broad range of sectors, whose quantities being analysed should present the following characteristics: (1) contain both deterministic and stochastic components; (2) vary through time; and (3) be characterizable through different variables of interest. Most of, if not all, complex product systems present these characteristics as their maintenance workload consists of deterministic and stochastic components resulting, respectively, form scheduled and unscheduled maintenance, increases through time as a result of the natural degradation of systems, and can be characterized through diferent technical skills. Notwithstanding the broader applicability of the proposed tool, it has been developed in the particular context of aircraft maintenance and the used data is presented in the following sections.

## 2.2. Aircraft maintenance data

Strict regulations oblige aircraft MROs to document all maintenance tasks performed on the aircraft. This determines the availability of large amounts of data, including the type of maintenance performed, e.g. scheduled ys. unscheduled. the instant when the tasks have beer

![](/api/attachments/S9BR6B2Q/fulltext/images/930a17403a7fe47857342be08b4e731b187d5b6b191f9c992dc6e7a49b2f4f44.jpg)  
— — → Updated information flow with each new check— Normal information flow

Fig. 1. Integration of ForeSim-BI in the MRO prediction process.

Table 1  
Collected ‘C’ checks and corresponding intervals.

<table><tr><td>Check</td><td>C</td><td>2C</td><td>3C</td><td>4C</td><td>C (5C)</td><td>2C (6C)</td><td>3C (7C)</td><td>4C (8C)</td></tr><tr><td>Intervals</td><td>5000 FH/FC or 30 MO</td><td>10,000 FH/FC or 60 MO</td><td>15,000 FH/FC or 90 MO</td><td>20,000 FH/FC or 120 MO</td><td>25,000 FH/FC or 150 MO</td><td>30,000 FH/FC or 180 MO</td><td>35,000 FH/FC or 210 MO</td><td>40,000 FH/FC or 240 MO</td></tr></table>

performed during the intervention, e.g. reception phase vs. delivery phase, and the technical skills that performed the work, e.g. structures vs. avionics. By summing the working hours spent in each task according to these categories, it is possible to obtain the respective workloads in each project and to analyse them through a predictive analytics approach, as it is the case in this research work.

This section presents the collected data, a sample of which is provided in Table A.1, Appendix A. The data refers to 171 aircraft main tenance projects collected at the host MRO, each representing a main tenance intervention, or check, performed on a particular aircraft type.

## 2.2.1. Maintenance checks

Aircraft maintenance consists in tasks performed according to time or usage limitations, i.e. scheduled maintenance, or after the identification of discrepancies, i.e. unscheduled maintenance. Scheduled main tenance is intended to prevent deterioration of the inherent safety and reliability levels of the aircraft, while unscheduled maintenance is performed to restore those levels when deterioration has occurred [27].

Tasks with the same time or usage limitations are organized in maintenance checks, comprising each check a given set of scheduled maintenance tasks, performed at a given interval. Table 1 presents the collected checks and corresponding intervals. The checks under analysis consist in four types of heavy maintenance [5] interventions (‘C’, ‘2C’, ‘3C’, and ‘4C’), known collectively as ‘C’ checks, which repeat themselves throughout the aircraft service life at fixed time intervals. For example, for the particular aircraft type under study, when an aircraft reaches 25,000 flight hours (FH)/flight cycles (FC) or 150 months (MO) it performs a second ‘C’ check (also known as ‘5C’), and so forth. The collected data comprises 2 cycles of ‘C’ checks (Table 1).

The checks are divided in two sets for the purpose of this research work: one set comprising the 5000 FH ‘C’ checks up to the ‘7C’ checks; and a second set comprising the ‘8C’ checks. The first set is used to implement the forecasting model presented in Section 3.1, which, in turn, is used to predict the total workload of the ‘8C’ check and to generate values for the workload random variables as explained in Section 3.3. The second set is used to validate the proposed tool as explained in Section 3.5.

## 2.2.2. Maintenance workload

In this paper, the quantity being forecasted is the total maintenance workload, i.e. the total number of hours needed to perform the main tenance tasks, which can be interpreted as processing time under scheduling theory. From common probability distributions used to model processing times [28], in particular to model unscheduled maintenance repair times [29], the lognormal distribution is considered a suitable descriptor of the total maintenance workload as it is strictly positive and right-skewed (e.g. [28]).

In order to explore this assumption, each maintenance check sample in the first set, i.e. from the ‘C’ checks up to the ‘7C’ checks, was tested against the null hypothesis of the sample following a lognormal dis tribution with the Kolmogorov-Smirnov (K-S) test [30,31]. In all samples the computed two-tailed p-value was greater than the significance level α = 0.05, meaning that the null hypothesis could not be rejected. Results are presented in Table 2, including values for the K-S statistic, D [31].

Table 2  
Kolmogorov-Smirnov test results.

<table><tr><td>Check</td><td>C</td><td>2C</td><td>3C</td><td>4C</td><td>5C</td><td>6C</td><td>7C</td></tr><tr><td>D</td><td>0.186</td><td>0.092</td><td>0.097</td><td>0.083</td><td>0.132</td><td>0.254</td><td>0.414</td></tr><tr><td>p-Value</td><td>0.655</td><td>0.972</td><td>0.930</td><td>0.916</td><td>0.668</td><td>0.213</td><td>0.274</td></tr></table>

## 3. ForeSim-BI – predictive analytics tool

This section presents the diferent modules that comprise the proposed tool. The tool is also validated by comparing simulated workload values with real workloads of a sample of ‘8C’ checks and with a model simulating current forecasting practices employed by MROs.

## 3.1. Forecasting module

As previously mentioned, the purpose of the forecasting module is to estimate workload probability distributions for future and unprecedented maintenance checks from historical data. The module is based on a multiplicative error state space formulation of the additive Holt-Winters (AHW) exponential smoothing model [32], applied to the data points corresponding to the sample means of the collected ‘C’ checks. The AHW forecasting model is appropriate for time series with trend and seasonality, patterns that are expected to exist in aircraft maintenance workload given the cyclic nature of scheduled maintenance, as explained in Section 2, and the upward trend of unscheduled maintenance resulting from aircraft aging [33]. The used AHW model is given by the following equations [32]:

$$
l _ {t} = l _ {t - 1} + b _ {t - 1} + \alpha (l _ {t - 1} + b _ {t - 1} + s _ {t - m}) \varepsilon_ {t}\tag{1}
$$

$$
b _ {t} = b _ {t - 1} + \beta (l _ {t - 1} + b _ {t - 1} + s _ {t - m}) \varepsilon_ {t}\tag{2}
$$

$$
s _ {t} = s _ {t - m} + \gamma (l _ {t - 1} + b _ {t - 1} + s _ {t - m}) \varepsilon_ {t}\tag{3}
$$

$$
\mu_ {t + h} = l _ {t} + h b _ {t} + s _ {t + h - m}\tag{4}
$$

where m is the length of the seasonal cycle, $l _ { t s } b _ { t s }$ and $s _ { t }$ are estimates of the level, trend, and seasonal components, respectively, of the time series at time $t , \mu _ { t + h }$ is the forecast mean for h periods ahead, and the smoothing parameters α, $\beta ,$ and $\gamma$ are constants between 0 and 1 [32]. ε is the relative error given by [32]:

$$
\varepsilon_ {t} = \frac {(y _ {t} - \mu_ {t})}{\mu_ {t}}\tag{5}
$$

where $y _ { t }$ is the observation and $\mu _ { t }$ is the forecast mean, at time t.

The forecast variance of this model, for h periods ahead from the forecast origin $n ,$ i.e. the last time t to which observations are available, is given by [32]:

$$
\nu_ {n + h} = \sigma_ {n + h} ^ {2} = (1 + \sigma_ {\varepsilon} ^ {2}) \theta_ {h} - \mu_ {n + h} ^ {2}\tag{6}
$$

where

$$
\sigma_ {\varepsilon} ^ {2} \approx \frac {1}{n} \sum_ {t = 1} ^ {n} \varepsilon_ {t} ^ {2}\tag{7}
$$

Table 3  
AICc values for the tested forecasting models (lowest value in bold)

<table><tr><td>Model</td><td>SES</td><td>HLM</td><td>AHW</td><td>MHW</td></tr><tr><td>AICc</td><td>31.17</td><td>56.26</td><td>-4.51</td><td>-3.35</td></tr></table>

$$
\theta_ {h} = \left\{ \begin{array}{c} \mu_ {n + 1} ^ {2}, h = 1 \\ \mu_ {n + h} ^ {2} + \sigma_ {\varepsilon} ^ {2} \sum_ {j = 1} ^ {h - 1} c _ {j} ^ {2} \theta_ {h - j}, h \geq 2 \end{array} \right.\tag{8}
$$

$$
c _ {j} = \alpha + \beta j\tag{9}
$$

State space models, such as the AHW with multiplicative errors presented before, allow mean values and variances of workload probability distributions to be calculated for future and unprecedented maintenance checks from historical data of previously performed checks.

The AHW has been selected among other forecasting models through the bias corrected Akaike's Information Criteria (AICc) for small samples [34,35]. It presents the lowest AICc value with the collected data when tested against multiplicative error state space formulations of the simple exponential smoothing (SES), Holt's linear method (HLM), and multiplicative Holt-Winters (MHW) [32]. Results for the AICc values are presented in Table 3.

The tested models have been implemented through the minimization of the mean squared error (MSE) [32], an error measure commonly used to select the values of the smoothing parameters [36].

## 3.2. BI module

The BI module is intended to transform prior forecasts into predictive forecasts as new observations on the check being predicted become available. Prior forecasts result from a particular state of knowledge and reflect a particular state of uncertainty regarding the maintenance work being predicted. As new observations become available, the original state of knowledge (and state of uncertainty) can be updated into a new, updated, state. This is possible through Bayesian inference, an approach already applied in other maintenance contexts [23,37].

With the classical (or frequentist) statistical approach, the parameters of any given probability distribution are treated as unknown constants, estimated through sample statistics, and to which probability statements are made about confidence intervals containing the true values of the parameters. On the contrary, with the Bayesian approach, the parameters are interpreted as random variables, described by probability distributions that can be updated with observed data [38]. This is done through the Bayes' theorem applied to probability distributions (e.g. [39]):

$$
f (\lambda \mid y) = \frac {f (y \mid \lambda) f (\lambda)}{f (y)}\tag{10}
$$

where $f ( \lambda | y )$ is the posterior distribution for the parameter λ given the observation $y , f ( y | \lambda )$ is the likelihood function of λ, f(λ) is the prior distribution for the parameter $\lambda ,$ and $f ( y )$ is the marginal probability of the observed data, given by the following equation for a continuous sample space (e.g. [39]):

$$
f (y) = \int f (y \mid \lambda) f (\lambda) d \lambda\tag{11}
$$

## 3.2.1. Updating prior forecasts into predictive forecasts

As discussed in Section 2, the random variable of interest, $X ,$ representing the total workload of a given maintenance check, is described by the lognormal distribution with parameters λ unknown and $\xi$ known given by (e.g. [28]):

$$
f (x \mid \lambda , \xi) = \left\{ \begin{array}{c} \frac {1}{x \sqrt {2 \pi \xi^ {2}}} \exp \left[ - \frac {1}{2} \left(\frac {\ln x - \lambda}{\xi}\right) ^ {2} \right], x > 0 \\ 0, o t h e r w i s e \end{array} \right.\tag{12}
$$

where $\gimel$ and $\xi$ are related to the mean $\mu$ and standard deviation σ, obtained through forecasting, by the following equations (e.g. [28]):

$$
\xi = \sqrt {\ln \left(1 + \frac {\sigma^ {2}}{\mu^ {2}}\right)}\tag{13}
$$

$$
\lambda = \ln (\mu) - \frac {\xi^ {2}}{2}\tag{14}
$$

or through the following equations, by using Eqs. (13) and (14) to solve for $\mu$ and σ:

$$
\mu = \exp \left(\lambda + \frac {\xi^ {2}}{2}\right)\tag{15}
$$

$$
\sigma = \sqrt {\mu^ {2} (\exp (\xi^ {2}) - 1)}\tag{16}
$$

By assuming a prior distribution for the parameter λ under study that is an appropriate conjugate of the distribution describing $X ,$ a considerable mathematical simplification can be achieved in obtaining the posterior distribution. Such pairs of distributions are called conjugate distributions [38]. According to Ang and Tang [38], the normal distribution is a conjugate distribution of X and, therefore, it is convenient to assume that the parameter $\gimel$ from Eq. (12) is normally distributed with mean $\mu ^ { \prime }$ and standard deviation $\sigma .$ The prior distribution of $\lambda , f ( \lambda )$ , is then given by:

$$
f (\lambda) = \frac {1}{\sqrt {2 \pi \sigma^ {\prime 2}}} \exp \left[ - \frac {1}{2} \bigg (\frac {\lambda - \mu^ {\prime}}{\sigma^ {\prime}} \bigg) ^ {2} \right]\tag{17}
$$

The posterior distribution for the parameter λ given the observation $y , f ( \lambda | y ) ;$ , is also a normal distribution with probability density function:

$$
f (\lambda \mid y) = \frac {1}{\sqrt {2 \pi \sigma^ {\prime \prime 2}}} \exp \left[ - \frac {1}{2} \biggl (\frac {\lambda - \mu^ {\prime \prime}}{\sigma^ {\prime \prime}} \biggr) ^ {2} \right]\tag{18}
$$

where $\mu ^ { \prime \prime }$ and $\sigma ^ { \prime \prime }$ are the mean and standard deviation of $f ( \lambda | y ) ,$ , respectively, given by:

$$
\mu^ {\prime \prime} = \frac {\xi^ {2} \mu^ {\prime} + \sigma^ {\prime 2} \ln y}{\xi^ {2} + \sigma^ {\prime 2}}\tag{19}
$$

$$
\sigma^ {\prime \prime} = \sqrt {\frac {\xi^ {2} \sigma^ {\prime 2}}{\xi^ {2} + \sigma^ {\prime 2}}}\tag{20}
$$

The posterior distribution $f ( \lambda | y )$ allows to update the knowledge about $\lambda ,$ and consequently about the mean $\mu$ of the total workload, X, after an observation y becomes available.

The conditional probability distribution of the total workload X after observation $y , f ( x | y )$ , is called the predictive distribution [39], which is given by:

$$
f (x \mid y) = \int f (y \mid \lambda , \xi) f (\lambda \mid y) d \lambda\tag{21}
$$

The predictive distribution $f ( x | y )$ of the total workload X also follows a lognormal distribution given by:

$$
f (x \mid y) = \frac {1}{x \sqrt {2 \pi \xi_ {p r e d} ^ {2}}} \exp \left[ - \frac {1}{2} \left(\frac {\ln x - \lambda_ {p r e d}}{\xi_ {p r e d}}\right) ^ {2} \right]\tag{22}
$$

where $\lambda _ { p r e d }$ and $\xi _ { p r e d }$ are the parameters of the predictive distribution f (x|y), given by:

$$
\lambda_ {p r e d} = \mu^ {\prime \prime}\tag{23}
$$

$$
\xi_ {p r e d} = \sqrt {\xi^ {2} + \sigma^ {\prime \prime 2}}\tag{24}
$$

![](/api/attachments/S9BR6B2Q/fulltext/images/feac10e88ee1bc9b30d032fe0c4f2dc0787596538f7de5574b1b043e8941616a.jpg)  
Normal information flow ——Updated information flow with each new observation y  
Fig. 2. Updating procedure of prior forecasts into predictive forecasts.

Through Eqs. (15) and (16) it is possible to calculate the mean $\mu _ { p r e d }$ and standard deviation $\sigma _ { p r e d } $ respectively, of the updated (or predictive) lognormal distribution describing the total workload X of a given maintenance check. This updates the uncertainty one has about the variability of the process being analysed.

## 3.2.2. Updating procedure

An updating procedure is presented in Fig. 2 to transform the prior total workload forecasts $f ( x | \lambda ,$ ξ), obtained with the forecasting module presented in Section 3.1, into updated forecasts, given by the predictive distribution $f ( x | y )$ of the total workload X after an observation y becomes available. These forecasts are hereby called predictive forecasts and the procedure to obtain them is described as follows:

Step 1. Determine $f ( x | \lambda , \xi ) _ { i }$ , representing the uncertainty on the total workload X:

1.a Estimate the mean μ and standard deviation σ of the total workload X through the forecasting model presented in Section

3.1, and transform μ and σ into the parameters λ and $\xi ,$ respectively, according to Eqs. (13) and (14);

Step 2. Determine the prior distribution f(λ), representing the un certainty on the parameter $\lambda ,$ from historical data of maintenance checks previously performed:

2.a Assume the mean $\mu ^ { \prime }$ of $f ( \lambda )$ as the parameter λ from Step 1.a, i.e. $\mu ^ { \prime } = \lambda ;$

2.b Calculate the standard deviation $\sigma ^ { \prime }$ of f(λ) through the equation:

$$
\sigma^ {\prime} = \overline {{C V}} \times \mu^ {\prime}\tag{25}
$$

where $\overline { { C V } }$ is the mean coeficient of variation of maintenance checks from historical data given by:

$$
\overline {{C V}} = \frac {1}{n} \sum_ {c = 1} ^ {n} C V _ {c} = \frac {1}{n} \sum_ {c = 1} ^ {n} \frac {S E _ {\lambda_ {c}}}{\lambda_ {c}}\tag{26}
$$

where n is the number of maintenance check types c in the historical data, $C V _ { c }$ is the coeficient of variation of each maintenance check type $c , S E _ { \lambda c }$ is the standard error of each maintenance check type $c ,$ and $\gimel _ { c }$ is the parameter of the lognormal distribution of the total workload of each maintenance check type c, given by Eq. (14);

Step 3. Determine the posterior distribution $f ( \lambda | y ) ,$ , representing the updated uncertainty on the parameter $\lambda ,$ through Eq. (18), and update the parameters $\mu ^ { \prime }$ and σ′ of Step 2 with the parameters $\mu ^ { \prime \prime }$ and $\sigma ^ { \prime \prime }$ obtained through Eqs. (19) and (20), respectively;

Step 4. Determine the predictive distribution $f ( x | y )$ of the total workload X through Eq. (22) and use this distribution to generate the predictive forecasts;

Step 5. Repeat Steps 3 and 4 each time a new observation on the workload being predicted is obtained.

## 3.3. Simulation module

The developed simulation module is based on a Monte Carlo (MC) simulation model that takes into account the predictive forecasts obtained with the BI module and is intended to generate discrete random values for the total workload of future and unprecedented maintenance checks, which are then loaded into the BN module as simulated main: tenance checks (Fig. 1).

Notwithstanding the importance of accurately predicting the total workload of future maintenance checks, and of updating this information as new observations become available, the predicted total workload is of limited practical use if not characterized with a higher level of detail. According to inputs from experts of the host MRO, three sets of workload random variables have been defined to characterize the total workload, including maintenance work types, maintenance work phases, and maintenance work skills. The random variables and the process to generate their values are presented in the following sections.

## 3.3.1. Defined random variables

In this work. besides the total workload WL. three other sets of random variables have been established: (1) maintenance work types; (2) maintenance work phases; and (3) maintenance work skills. The maintenance work types, WT , refer to diferent categories of maintenance tasks defined by the host MRO. The maintenance work phases, $W P _ { j } ,$ , refer to the diferent time periods in which maintenance interventions can be divided [40]. These phases can be used to define timeframes in the maintenance projects for the accomplishment of tasks. Finally. the maintenance work skills. $W S _ { k } ,$ refer to the different technical skills of the aircraft maintenance technicians [40]. All the aforementioned variables are treated as random variables, but while values for the total workload are generated through simulation of a known probability distribution, the lognormal distribution, workload values for the remainder variables are generated through bootstrapping (e.g. [41]) from samples of maintenance checks of the same type as the one being predicted.

Each workload set is mutually exclusive and collectively exhaustive relatively to the total workload, resulting in the following sum of random variables:

$$
W L = \sum_ {i} W T _ {i} = \sum_ {j} W P _ {j} = \sum_ {k} W S _ {k}\tag{27}
$$

## 3.3.2. Bootstrapping of workload random variables

As previously mentioned, while values of the total workload are generated through simulation of a known probability distribution, values of the remainder workload random variables are generated through bootstrapping of samples of maintenance checks of the same type as the one being predicted. Each of these samples is considered independent and identically distributed, from an unknown cumulative distribution function (CDF), and where the best knowledge about the CDF is the sample itself [41]. In order to obtain better approximations for the unknown CDFs, it is possible to resample repeatedly and randomly the original samples.

The first step in the bootstrapping procedure is sampling with replacement. Let $\boldsymbol { x } _ { i } ~ = ~ ( x _ { 1 } , . . . , x _ { n } )$ be the sample of a given workload random variable X. The sampling with replacement procedure consists in drawing random sample points from x , assuming that the probability of each sample point is equal to 1/n. Then, an additional step is needed. In order to ensure that the generated random values for the workload variables respect the condition imposed by Eq. (27), the values need to be normalized relatively to the total workload.

In aircraft maintenance, some workload variables are expected to change with the total workload, while others are not. By scaling the values of all the established variables relatively to the total workload, one is assuming that all the variables are dependent on the latter. This is not a reasonable assumption to make. For example, the workloads of Phase 1 - Reception and Phase 6 – Delivery [24], which refer to a limited number of maintenance tasks in each check type, are not expected to change as much as the workload of Phase 4 – Repairs [24], which increases with the aircraft degradation over time [33] and contributes heavily to the maintenance total workload as discussed before.

The sample correlation coeficient (e.g. [42]), r, can be used to determine which workload random variables are more correlated with the total workload and, therefore, expected to change with it. A parti cular correlation value, denoted $r _ { c u t } ,$ can be defined as a cut-of criterion to determine which variables are considered correlated with the total workload. Since each random variable has its own value of $^ { \cdot } r ,$ calculated between itself and the total workload, only variables with values of r higher than $r _ { c u t }$ are, arbitrarily, considered to be correlated with the total workload. For example, considering $r _ { c u t } = 0 . 5 ,$ only the variables with $r \geq 0 . 5$ are considered to be correlated with the total workload. In this work, variables with $r ~ < ~ r _ { c u t }$ assume the value obtained through the sampling procedure with replacement directly. The remainder, i.e. those with $r \geq r _ { c u t } ,$ are further scaled through the following equation:

$$
x _ {p} ^ {\prime} = \frac {(w l ^ {*} - \sum x _ {q} ^ {*}) x _ {p} ^ {*}}{\sum x _ {p} ^ {*}}\tag{28}
$$

constrained to the following:

$$
w l ^ {*} = \sum_ {p} x _ {p} ^ {\prime} + \sum_ {q} x _ {q} ^ {*}\tag{29}
$$

where ${ x _ { p } } ^ { \prime }$ is the scaled value of ${ x _ { p } } ^ { * } ,$ which is the value of a dependent workload variable, $X _ { p } ,$ obtained through sampling with replacement, ${ x _ { q } } ^ { * }$ is the value of an independent workload variable, $X _ { q } ,$ also obtained through sampling with replacement, and $w l ^ { * }$ is the value of the total workload, $W L ,$ obtained through simulation of the lognormal distribu tion.

Diferent values of $r _ { c u t }$ were tested to determine the value that presented the lowest errors in estimating future workloads. The tests were conducted by estimating values for the workload variables with the proposed tool and then comparing them with observations of the‘8C’ check (Table 1). The results are presented in Table 4.

The used error measures were the mean absolute error (MAE) and the mean absolute percentage error (MAPE), commonly used to measure forecasting accuracy [43], calculated according to Eqs. (30) and (31), respectively:

$$
M A E = \frac {1}{n} \sum_ {i = 1} ^ {n} | E _ {i} |, E _ {i} = F _ {i} - D _ {i}\tag{30}
$$

$$
M A P E = \frac {1}{n} \sum_ {i = 1} ^ {n} \left| \frac {E _ {i}}{D _ {i}} \right|\tag{31}
$$

where n is the number of workload variables in the set under analysis, E is the error of the workload variable i, F is the predicted workload to be planned in the workload variable i, equal to the upper bound of the selected workload interval when using the proposed tool, and $D _ { i }$ is the observed workload in the workload variable i.

The results presented in Table 4 show that the lowest MAE and lowest MAPE are obtained with $r _ { c u t } = 0 . 5$ in the three estimations. With $r _ { c u t } = 0 . 3 ,$ , low values are also obtained in the second and third observation, but an error higher than the one obtained with $r _ { c u t } = 0 . 5$ is verified in the first observation. In the third observation, the lowest MAPE is obtained with an $r _ { c u t } = 0 . 7$ , however, as it is discussed in Section 3.5, the MAPE is not considered an appropriate measure to assess the accuracy of the predictions in the particular case of this work.

Taking these results into account, a correlation coeficient of 0.5 is considered in this work as the cut-of value.

The sampling of the workload random variables is performed differently depending on the availability of observations on the maintenance check being predicted. This is explained in the following sections.

3.3.2.1. Sampling without observations. When no observations on the maintenance check being predicted exist, values for its workload random variables have to be generated from samples of the most recent check type, c, of the same type as the check being predicted, to which data is available. These are called henceforth ‘original samples’. For example, if the check being predicted is a ‘5C’ check (Table 1), the random values need to be bootstrapped from samples of the 5000 FH ‘C’ check. Let $w t _ { i l c } ~ = ~ ( w t _ { i 1 c } , . . . , w t _ { i n c } )$ be the original sample of the maintenance work type i, WT , $w p _ { j l c } = ( w p _ { j 1 c } , . . . , w p _ { j n c } )$ be the original sample of the maintenance work phase j, $W P _ { j c } ,$ and ws $\mathbf { \Psi } _ { k l c } ~ = ~ ( w s _ { k 1 c } , . . . , w s _ { k n c } )$ be the original sample of maintenance work skill $k ,$ WS<sub>kc</sub>.

3.3.2.2. Sampling with observations. When one or few observations on a maintenance check being predicted are available, values for its workload random variables can be generated from these samples, henceforth called ‘new samples’. Let $w t _ { i l ^ { \prime } c ^ { \prime } } = ( w t _ { i 1 c ^ { \prime } } , . . . , w t _ { i n ^ { \prime } c ^ { \prime } } )$ be the new sample of the maintenance work type $i , \ W T _ { i c ^ { \prime } } , \ w p _ { j l ^ { \prime } c ^ { \prime } } =$ (wp<sub>j1c′</sub>, $. . . , w p _ { j n ^ { \prime } c ^ { \prime } } )$ be the new sample of the maintenance work phase j, $, \ W P _ { j c ^ { \prime } } ,$ and $w s _ { k l ^ { \prime } c ^ { \prime } } = ( w s _ { k 1 c ^ { \prime } } , . . . , w s _ { k n ^ { \prime } c ^ { \prime } } )$ be the new sample of maintenance work skill $k ,$ WS .

## 3.3.3. Simulation procedure

The simulation procedure presented in Fig. 3 was developed to generate values for the total workload, $W L ,$ and for the remainder workload random variables: maintenance work types, WT ; maintenance work phases, $W P _ { j } ;$ and maintenance work skills, $W S _ { k } .$ The procedure is described as follows:

Step 1. Compute the correlation coeficient, $r ,$ between the samples of total workload variable, WL, and the samples of each of the remainder workload variables, $W T _ { i } , W P _ { j } ,$ and $W S _ { k } ,$ for the most recent check type, $c ,$ of the same type as the check being predicted (Table 1), to which data is available;

Step 2. Generate values for the total workload, WL, through simulation of the lognormal distribution with parameters $\mu _ { p r e d }$ and $\sigma _ { p r e d }$ obtained from the Bayesian inference process presented in Section 3.2.1;

MAE and MAPE for diferent values of $r _ { c u t }$ (lowest values for each observation in bold).

<table><tr><td rowspan="2"> $r_{cut}$ </td><td colspan="4">Observation 1</td><td colspan="4">Observation 2</td><td colspan="4">Observation 3</td></tr><tr><td>0</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0</td><td>0.3</td><td>0.5</td><td>0.7</td></tr><tr><td>MAE</td><td>290</td><td>284</td><td>168</td><td>319</td><td>121</td><td>54</td><td>54</td><td>74</td><td>139</td><td>105</td><td>105</td><td>118</td></tr><tr><td>MAPE</td><td>28%</td><td>31%</td><td>23%</td><td>36%</td><td>31%</td><td>12%</td><td>12%</td><td>14%</td><td>18%</td><td>16%</td><td>16%</td><td>15%</td></tr></table>

Step 3. Generate values for the workload random variables, $W T _ { i } ,$ $W P _ { j } ,$ and $W S _ { k } ,$ , through sampling with replacement:

3a. If no observations exist on the maintenance check being pre dicted, generate values from the original samples, $w t _ { i l c } , ~ w p _ { j l c } ,$ and ws ;

3b. If observations exist on the maintenance check being predicted, generate values from the new samples, $w t _ { i l ^ { \prime } c ^ { \prime } } , w p _ { j l ^ { \prime } c ^ { \prime } } ,$ and $w s _ { k l ^ { \prime } c ^ { \prime } } ,$

Step 4. Assess the value of the correlation coeficient, r, calculated in Step 1 for the workload random variables $W T _ { i } , \ W P _ { j } ,$ , and WS :

4a. If the workload random variable has $r < r _ { c u t } ( r _ { c u t } = 0 . 5 $ in the case of this work), assume the generated value through sampling with replacement as the value of the variable, as the variable is assumed to be uncorrelated with the total workload;

4b. If the workload random variable has $r \ \ge \ r _ { c u t }$ scale the variable according to Eq. (28), as it is considered to be correlated with the total workload:

Step 5. Collect the obtained sample of simulated values for the random variables WL, WT , $W P _ { j } ,$ and $W S _ { k }$ ;

Step 6. Repeat steps 2 through 4 until a suficiently large number of simulated samples is obtained.

## 3.4. BN module

The BN module (Fig. 1), based on BN models previously developed in [24] to predict the workload of maintenance interventions from historical data, combines in this research work historical data with simulated data generated in the simulation module. By doing so, MROs concentrate in a single decision support tool the ability to predict the workload of incoming maintenance checks for capacity planning, both known and unprecedented. Very briefly, a BN consists in a directed acyclic graph (DAG) and a set of conditional probability tables (CPTs) [44,45]. Conditional dependencies are defined between nodes in the DAG, representing random variables, when directed arcs are established between them. As soon as the state of any given variable is known by providing evidence to that variable, it is possible to perform probabilistic inference on any of the remainder variables as their conditional probabilities change. In addition, as new data is loaded into the BN, learning techniques such as the Expectation-Maximization (EM) algorithm [46,47] allow the CPTs to be updated accordingly.

## 3.4.1. The interval selection problem

As mentioned previously, the total workload is characterized in this research work according to three sets of workload variables including maintenance work types, maintenance work phases, and maintenance work skills. Similarly to the BNs developed in [24], one BN model has been established for each of these sets, with arcs being defined from the total workload to the remainder workload variables. The purpose of these arcs is to allow the probabilistic inference of the workload intervals of the remainder workload variables, once evidence is provided to the total workload. In practice, the objective is to determine which intervals in the remainder workload types are the most probable to occur, and hence selected, given that a total workload has been selected to be planned. A diference exists nonetheless relatively to BNs previously developed in [24]: the intervals of the total workload have been discretized in 100 man-hours, instead of 500. This considerably improves the accuracy of the proposed tool as demonstrated in Section 3.5.

One problem resulting from the developed BNs for maintenance capacity planning refers to the selection of workload intervals in the workload variables to which inference has been performed. By providing evidence to a given total workload interval, several combinations with different probabilities for the workload intervals are possible for the remainder workload variables, but only few combinations are equal to the total workload selected to be planned, as imposed by

![](/api/attachments/S9BR6B2Q/fulltext/images/2bf87c470a1cab56267f58f0e9e4569b0deab26548bd5024e588d16d1633b668.jpg)  
Fig. 3. Simulation procedure of the total workload and remainder workload variables.

Eq. (27). If the workload intervals have to be manually selected so they add up to the chosen total workload, this constitutes a tedious task for the decision-maker, with no guarantees of optimality.

An LP model has been developed to address this problem and, as a result, to improve the eficiency of the decision-making process with BNs for maintenance capacity planning.

## 3.4.2. LP model

For the sake of clarity, the term ‘workload type’ is used henceforth in this section as a synonym of ‘workload random variable’, reserving the term ‘variable’ to the variables of the LP model.

The LP model for the selection of workload intervals is divided in two stages. The first stage refers to the selection of the total workload interval and can be stated as follows:

Minimize x wl <sub>j j</sub>

(32)

$$
\text { subject   to } x _ {j} \sum_ {j} p _ {j} \geq p _ {\text { cumulative }}\tag{33}
$$

$$
\sum_ {j = 1} ^ {n} x _ {j} = 1\tag{34}
$$

$$
x _ {j} = \left\{ \begin{array}{l l} 1 & \text {   if   interval   } j \text {   from   total   workload   is   selected   } \\ 0 & \text {   otherwise   } \end{array} \right.\tag{35}
$$

where x is a binary variable equal to 1 if interval j of the total workload is selected and equal to 0 otherwise, $w l _ { j }$ is the workload of interval j of the total workload, equal to the upper bound of the interval, $p _ { j }$ is the probability of interval j, and, finally, p is a parameter defining a minimum value for the cumulative probability of interval j.

The objective function presented in $\operatorname { E q . }$ (32) refers to the mini mization of the selected total workload interval. The objective function is subjected to the constraint presented in Eq. (33), which determines that the selected interval has to have a given minimum value of cumulative probability. The cumulative probability of the workload intervals describes the CDF of the total workload WL, $P ( W L \leq w l )$ , and in that sense establishing a minimum value for it means that workload values with lower cumulative probabilities will be covered for capacity planning purposes. A value of 90% for the cumulative probability of the total workload has been found to constitute a reasonable compromise between the risk of overplanning and the risk of not planning enough capacity in the developed BNs with discrete workload intervals of 100 man-hours in the total workload. This value may be adjusted in order to better reflect the decision-maker attitude towards risk. The constraint imposed by Eq. (34) determines that only one interval is to be selected for the total workload. This is represented in Fig. 4.

The second stage of the model refers to the selection of the re mainder workload types and can be stated as follows:

$$
M a x i m i z e \sum_ {i} \sum_ {j} x _ {i j} p _ {i j}\tag{36}
$$

$$
s u b j e c t t o \sum_ {i} \sum_ {j} x _ {i j} w _ {i j} = w l ^ {*}\tag{37}
$$

$$
\sum_ {j = 1} ^ {n} x _ {i j} = 1 \qquad i = 1, 2, \dots , m\tag{38}
$$

$$
x _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if   interval   } j \text {   from   workload   type   } i \text {   is   selected } \\ 0 & \text { otherwise } \end{array} \right.\tag{39}
$$

where $x _ { i j }$ is a binary variable equal to 1 if interval j from workload type i is selected and equal to 0 otherwise, $p _ { i j }$ is the probability of interval j from workload type $i , w _ { i j }$ is the workload of interval j from workload type i, equal to the upper bound of the interval, and, finally, wl<sup>∗</sup> is the total workload selected to be planned, obtained in the first stage of the model.

The objective function presented in Eq. (36) refers to the maximization of the sum of the probabilities of the selected intervals. This ensures that the workload intervals with higher probabilities are preferably selected. The objective function is subjected to the constraint presented in Eq. (37), which determines the intervals that are to be selected by imposing that the sum of the workload intervals is to be equal to the total workload chosen to be planned, and to the constraint presented in $\operatorname { E q . }$ (38), which determines that one and only one interval is to be selected in each workload type. This is represented in Fig. 5.

## 3.5. Validation

The results presented in this section were obtained by using the proposed tool and a model simulating current practices used by MROs to predict the workloads of future maintenance checks, henceforth called engineering estimates [48]. In addition to the analysis of the estimation errors obtained with each approach, a comparison between both methods is presented.

## 3.5.1. Results obtained with ForeSim-BI

The accuracy assessment of each approach is based on the errors of each workload variable $i , E _ { i } ,$ equal to the diference between the predicted workload value, $F _ { i } ,$ and the observed workload value $D _ { i } .$ In the case of the proposed tool, $F _ { i }$ is equal to the upper bound of the workload interval selected to be planned by the LP model presented in Section 3.4.2. Values of the MAE and MAPE were also calculated, according to Eqs. (30) and (31), respectively. The results are presented in Table 5, and important conclusions can be drawn from it. The work types, work phases, and work skills, are masked for confidentiality reasons.

First, the proposed tool produces a percentage error (PE) of 13%, (709 in a total of 5291 man-hours) in the total workload when predicting the first occurrence of an ‘8C’ check (Table 1). Taking into account that the first ‘8C’ check is predicted with data up to the ‘7C’

![](/api/attachments/S9BR6B2Q/fulltext/images/1d67b9d3f988c3c97c24b75cd85243e7b9a41d3c62290674c477c09013665a5e.jpg)  
Fig. 4. Representation of a workload interval, wl<sup>∗</sup>, selected in the 1st stage of the LP model for the total workload WL.

P(W₃)

P(Wi)

P(W1)  
![](/api/attachments/S9BR6B2Q/fulltext/images/6d2d045f27aacc0b777bd6e67904cd1ce63d90c90a49aa20e3247cdc4a1566c0.jpg)  
(a)

![](/api/attachments/S9BR6B2Q/fulltext/images/bb5d41c5e4fb01fa972073dc37e459960052da270755ee0ecd6f226ff3b9e8f6.jpg)  
(b)

![](/api/attachments/S9BR6B2Q/fulltext/images/12f170c15a16acd0b28253a1ce43c82d17862d6f0fd195127812661de84f62cf.jpg)  
(c)

![](/api/attachments/S9BR6B2Q/fulltext/images/0a9e7a0eba81109e0f2144085b2e546b8665526f9cd815ab8035f202bc98be40.jpg)  
(d)  
Fig. 5. Representation of the conditional probability distributions for the maintenance workload types W<sub>1</sub> (a), W<sub>2</sub> (b), W<sub>3</sub> (c), W<sub>i</sub> (d), with workload intervals w<sub>1</sub><sup>∗</sup>, w <sup>∗</sup>, w <sup>∗</sup>, w <sup>∗</sup> selected in the 2nd stage of the LP model.

check, and that 30 months of operation separate the $\mathrm { { } ^ { \circ } { 7 } C ^ { \prime } }$ check from the ‘8C’ check, a PE of 13% in the total workload is possible for a planning horizon of more than two years. This error occurs when using the tool automatically with the constraint of selecting the lowest interval with a minimum cumulative probability of 90% in the total workload, as determined by the LP model presented in Section 3.4.2. In any case, the produced predictions should be closely monitored and adjusted when necessary for decision-making.

Second, the PE on the total workload falls to 0% in the second observation and remains at that level in the third observation, maintaining the same constraint of selecting the lowest interval with a minimum cumulative probability of 90% in the total workload. This indicates that the Bayesian inference procedure efectively adjusts the predictive distribution at each observation.

Third, a downward trend can be observed on the MAE of all the workload variables. This indicates that the bootstrapping procedure improves the distribution of the simulated total workload among the remainder workload variables with the addition of each new observation to the new sample. On a related note, the MAPE is not considered an appropriate measure to assess the accuracy of the predictions on the workload variables. As recognized by Makridakis [49] and Kim and Kim [50], the MAPE presents important problems and its use is even inadvisable in some circumstances [43]. In particular, the MAPE can be distorted when extremely large PEs occur [49], as it is the case. For example, PEs of > 500% are obtained for the work phase 3, $W P _ { 3 } ,$ in the second and third observations.

Finally, relevant errors are still obtained in some of the workload random variables after two observations, i.e. when comparing the predictions with the third observation. For example, an error of 308 man-hours (31%) occurs in the work type 3, WT , of −277 man-hours (−7%) in the work phase 2, $W P _ { 2 } ,$ and of −212 man-hours (−9%) in the work skill 1, $W S _ { 1 }$ . Nonetheless, the bootstrapping procedure behaved correctly in each of these cases from the second to the third observation: a decrease of 100 man-hours can be observed in the predicted workload of $W T _ { 3 } ;$ an increase of 200 man-hours occurs in the predicted workload of $W P _ { 2 } ;$ and an increase of 100 man-hours occurs in the predicted workload of $W S _ { 1 }$ . However, further attention should be given on modelling the workload random variables. A bootstrapping procedure was used in this work to generate values for the workload random variables, but other approaches should also be explored. Bayesian inference is a possibility, notwithstanding the mathematical complexities resulting from the use of uncommon probability dis tributions to model the random variables and from the need to equal the sum of such distributions to the total workload distribution.

Predicted (F ) and observed (D ) workloads, error (E ) and percentage error (E /D ), and MAE and MAPE obtained with the proposed tool for three observations of the ‘8C’ check (man-hours).

<table><tr><td rowspan="2"></td><td colspan="4">Observation 1</td><td colspan="4">Observation 2</td><td colspan="4">Observation 3</td></tr><tr><td> $F_i$ </td><td> $D_i$ </td><td> $E_i$ </td><td> $E_i/D_i$ </td><td> $F_i$ </td><td> $D_i$ </td><td> $E_i$ </td><td> $E_i/D_i$ </td><td> $F_i$ </td><td> $D_i$ </td><td> $E_i$ </td><td> $E_i/D_i$ </td></tr><tr><td>Total WL</td><td>6000</td><td>5291</td><td>709</td><td>13%</td><td>6200</td><td>6183</td><td>17</td><td>0%</td><td>6500</td><td>6489</td><td>11</td><td>0%</td></tr><tr><td>WT1</td><td>1300</td><td>1853</td><td>-553</td><td>-30%</td><td>1900</td><td>2068</td><td>-168</td><td>-8%</td><td>1900</td><td>2096</td><td>-196</td><td>-9%</td></tr><tr><td>WT2</td><td>0</td><td>17</td><td>-17</td><td>-100%</td><td>0</td><td>93</td><td>-93</td><td>-100%</td><td>100</td><td>85</td><td>16</td><td>18%</td></tr><tr><td>WT3</td><td>1600</td><td>1078</td><td>522</td><td>48%</td><td>1400</td><td>1093</td><td>307</td><td>28%</td><td>1300</td><td>992</td><td>308</td><td>31%</td></tr><tr><td>WT4</td><td>500</td><td>93</td><td>407</td><td>437%</td><td>100</td><td>594</td><td>-494</td><td>-83%</td><td>600</td><td>667</td><td>-67</td><td>-10%</td></tr><tr><td>WT5</td><td>2500</td><td>2083</td><td>417</td><td>20%</td><td>2700</td><td>2156</td><td>544</td><td>25%</td><td>2400</td><td>2434</td><td>-34</td><td>-1%</td></tr><tr><td>WT6</td><td>100</td><td>168</td><td>-68</td><td>-40%</td><td>100</td><td>178</td><td>-78</td><td>-44%</td><td>200</td><td>215</td><td>-15</td><td>-7%</td></tr><tr><td>MAE</td><td></td><td></td><td>331</td><td>-</td><td></td><td></td><td>281</td><td>-</td><td></td><td></td><td>106</td><td>-</td></tr><tr><td>MAPE</td><td></td><td></td><td>-</td><td>113%</td><td></td><td></td><td>-</td><td>48%</td><td></td><td></td><td>-</td><td>13%</td></tr><tr><td>WP1</td><td>300</td><td>296</td><td>4</td><td>1%</td><td>300</td><td>330</td><td>-30</td><td>-9%</td><td>400</td><td>343</td><td>57</td><td>17%</td></tr><tr><td>WP2</td><td>4100</td><td>3271</td><td>829</td><td>25%</td><td>3700</td><td>3937</td><td>-237</td><td>-6%</td><td>3900</td><td>4177</td><td>-277</td><td>-7%</td></tr><tr><td>WP3</td><td>100</td><td>42</td><td>58</td><td>140%</td><td>100</td><td>15</td><td>85</td><td>579%</td><td>100</td><td>15</td><td>85</td><td>579%</td></tr><tr><td>WP4</td><td>100</td><td>41</td><td>59</td><td>146%</td><td>100</td><td>41</td><td>59</td><td>146%</td><td>100</td><td>41</td><td>59</td><td>146%</td></tr><tr><td>WP5</td><td>1100</td><td>1199</td><td>-99</td><td>-8%</td><td>1500</td><td>1385</td><td>115</td><td>8%</td><td>1400</td><td>1427</td><td>-27</td><td>-2%</td></tr><tr><td>WP6</td><td>300</td><td>444</td><td>-144</td><td>-32%</td><td>500</td><td>476</td><td>24</td><td>5%</td><td>600</td><td>488</td><td>112</td><td>23%</td></tr><tr><td>MAE</td><td></td><td></td><td>199</td><td>-</td><td></td><td></td><td>92</td><td>-</td><td></td><td></td><td>103</td><td>-</td></tr><tr><td>MAPE</td><td></td><td></td><td>-</td><td>59%</td><td></td><td></td><td>-</td><td>126%</td><td></td><td></td><td>-</td><td>129%</td></tr><tr><td>WS1</td><td>1800</td><td>1750</td><td>50</td><td>3%</td><td>2100</td><td>2082</td><td>18</td><td>1%</td><td>2200</td><td>2412</td><td>-212</td><td>-9%</td></tr><tr><td>WS2</td><td>2600</td><td>1965</td><td>635</td><td>32%</td><td>2200</td><td>2272</td><td>-72</td><td>-3%</td><td>2300</td><td>2376</td><td>-76</td><td>-3%</td></tr><tr><td>WS3</td><td>600</td><td>561</td><td>39</td><td>7%</td><td>700</td><td>631</td><td>69</td><td>11%</td><td>800</td><td>614</td><td>186</td><td>30%</td></tr><tr><td>WS4</td><td>200</td><td>275</td><td>-75</td><td>-27%</td><td>300</td><td>271</td><td>29</td><td>11%</td><td>300</td><td>322</td><td>-22</td><td>-7%</td></tr><tr><td>WS5</td><td>100</td><td>175</td><td>-75</td><td>-43%</td><td>200</td><td>146</td><td>54</td><td>37%</td><td>200</td><td>147</td><td>53</td><td>36%</td></tr><tr><td>WS6</td><td>700</td><td>566</td><td>134</td><td>24%</td><td>700</td><td>781</td><td>-81</td><td>-10%</td><td>700</td><td>618</td><td>82</td><td>13%</td></tr><tr><td>MAE</td><td></td><td></td><td>168</td><td>-</td><td></td><td></td><td>54</td><td>-</td><td></td><td></td><td>105</td><td>-</td></tr><tr><td>MAPE</td><td></td><td></td><td>-</td><td>23%</td><td></td><td></td><td>-</td><td>12%</td><td></td><td></td><td>-</td><td>16%</td></tr></table>

Predicted $\left( \boldsymbol { F } _ { i } ^ { \prime } \right)$ and observed (D ) workloads, error (E ′) and percentage error $( E _ { i } ^ { \prime } / D _ { i } ) ,$ , and MAE and MAPE obtained with a model simulating current engineering estimates for three observations of the ‘8C’ check (man-hours).

<table><tr><td rowspan="2"></td><td colspan="4">Observation 1</td><td colspan="4">Observation 2</td><td colspan="4">Observation 3</td></tr><tr><td> $F_i'$ </td><td> $D_i$ </td><td> $E_i'$ </td><td> $E_i' / D_i$ </td><td> $F_i'$ </td><td> $D_i$ </td><td> $E_i'$ </td><td> $E_i' / D_i$ </td><td> $F_i'$ </td><td> $D_i$ </td><td> $E_i'$ </td><td> $E_i' / D_i$ </td></tr><tr><td>TotalWL</td><td>4184</td><td>5291</td><td>-1107</td><td>-21%</td><td>5291</td><td>6183</td><td>-891</td><td>-14%</td><td>5737</td><td>6489</td><td>-752</td><td>-12%</td></tr><tr><td>WT1</td><td>1354</td><td>1853</td><td>-499</td><td>-27%</td><td>1853</td><td>2068</td><td>-215</td><td>-10%</td><td>1960</td><td>2096</td><td>-136</td><td>-6%</td></tr><tr><td>WT2</td><td>8</td><td>17</td><td>-9</td><td>-53%</td><td>17</td><td>93</td><td>-77</td><td>-82%</td><td>55</td><td>85</td><td>-30</td><td>-35%</td></tr><tr><td>WT3</td><td>868</td><td>1078</td><td>-210</td><td>-19%</td><td>1078</td><td>1093</td><td>-15</td><td>-1%</td><td>1086</td><td>992</td><td>94</td><td>9%</td></tr><tr><td>WT4</td><td>209</td><td>93</td><td>116</td><td>125%</td><td>93</td><td>594</td><td>-501</td><td>-84%</td><td>344</td><td>667</td><td>-324</td><td>-49%</td></tr><tr><td>WT5</td><td>1629</td><td>2083</td><td>-454</td><td>-22%</td><td>2083</td><td>2156</td><td>-73</td><td>-3%</td><td>2119</td><td>2434</td><td>-314</td><td>-13%</td></tr><tr><td>WT6</td><td>116</td><td>168</td><td>-52</td><td>-31%</td><td>168</td><td>178</td><td>-11</td><td>-6%</td><td>173</td><td>215</td><td>-42</td><td>-20%</td></tr><tr><td>MAE</td><td></td><td></td><td>223</td><td>-</td><td></td><td></td><td>149</td><td>-</td><td></td><td></td><td>157</td><td>-</td></tr><tr><td>MAPE</td><td></td><td></td><td>-</td><td>46%</td><td></td><td></td><td>-</td><td>31%</td><td></td><td></td><td>-</td><td>22%</td></tr><tr><td>WP1</td><td>244</td><td>296</td><td>-52</td><td>-18%</td><td>296</td><td>330</td><td>-34</td><td>-10%</td><td>313</td><td>343</td><td>-30</td><td>-9%</td></tr><tr><td>WP2</td><td>2717</td><td>3271</td><td>-554</td><td>-17%</td><td>3271</td><td>3937</td><td>-666</td><td>-17%</td><td>3604</td><td>4177</td><td>-573</td><td>-14%</td></tr><tr><td>WP3</td><td>27</td><td>42</td><td>-14</td><td>-34%</td><td>42</td><td>15</td><td>27</td><td>182%</td><td>28</td><td>15</td><td>13</td><td>91%</td></tr><tr><td>WP4</td><td>54</td><td>41</td><td>14</td><td>34%</td><td>41</td><td>41</td><td>0</td><td>0%</td><td>41</td><td>41</td><td>0</td><td>0%</td></tr><tr><td>WP5</td><td>785</td><td>1199</td><td>-413</td><td>-34%</td><td>1199</td><td>1385</td><td>-186</td><td>-13%</td><td>1292</td><td>1427</td><td>-135</td><td>-9%</td></tr><tr><td>WP6</td><td>357</td><td>444</td><td>-87</td><td>-20%</td><td>444</td><td>476</td><td>-32</td><td>-7%</td><td>460</td><td>488</td><td>-28</td><td>-6%</td></tr><tr><td>MAE</td><td></td><td></td><td>189</td><td>-</td><td></td><td></td><td>158</td><td>-</td><td></td><td></td><td>130</td><td>-</td></tr><tr><td>MAPE</td><td></td><td></td><td>-</td><td>26%</td><td></td><td></td><td>-</td><td>38%</td><td></td><td></td><td>-</td><td>21%</td></tr><tr><td>WS1</td><td>1515</td><td>1750</td><td>-234</td><td>-13%</td><td>1750</td><td>2082</td><td>-332</td><td>-16%</td><td>1916</td><td>2412</td><td>-496</td><td>-21%</td></tr><tr><td>WS2</td><td>1562</td><td>1965</td><td>-403</td><td>-20%</td><td>1965</td><td>2272</td><td>-307</td><td>-14%</td><td>2118</td><td>2376</td><td>-258</td><td>-11%</td></tr><tr><td>WS3</td><td>438</td><td>561</td><td>-123</td><td>-22%</td><td>561</td><td>631</td><td>-70</td><td>-11%</td><td>596</td><td>614</td><td>-18</td><td>-3%</td></tr><tr><td>WS4</td><td>176</td><td>275</td><td>-98</td><td>-36%</td><td>275</td><td>271</td><td>3</td><td>1%</td><td>273</td><td>322</td><td>-49</td><td>-15%</td></tr><tr><td>WS5</td><td>37</td><td>175</td><td>-138</td><td>-79%</td><td>175</td><td>146</td><td>29</td><td>20%</td><td>160</td><td>147</td><td>13</td><td>9%</td></tr><tr><td>WS6</td><td>456</td><td>566</td><td>-110</td><td>-20%</td><td>566</td><td>781</td><td>-215</td><td>-28%</td><td>674</td><td>618</td><td>56</td><td>9%</td></tr><tr><td>MAE</td><td></td><td></td><td>185</td><td>-</td><td></td><td></td><td>159</td><td>-</td><td></td><td></td><td>148</td><td>-</td></tr><tr><td>MAPE</td><td></td><td></td><td>-</td><td>32%</td><td></td><td></td><td>-</td><td>15%</td><td></td><td></td><td>-</td><td>11%</td></tr></table>

## 3.5.2. Comparison between ForeSim-BI and current engineering estimates

Table 6 presents the results obtained with a model simulating current forecasting practices employed by MROs to predict the workloads of future maintenance checks. The model assumes the following: (1) simple linear regression, calculated through the method of least squares, to obtain the total and remainder workloads when no ob servations on the check being predicted are available; and (2) mean values of the observed workloads when observations on the check being predicted exist.

The comparison of the two approaches clearly shows that significant lower errors are obtained for the total workload with ForeSim-BI. With current estimates, the PE on the total workload of the first observation is of −21% (−1107 in a total of 5291 man-hours), of −14% (−891 in a total of 6183 man-hours) in the second observation. and of – 12% (−752 in a total of 6489 man-hours) in the third observation. Also, with the exception of the first observation and the work type variables $W T _ { i }$ in the second, significantly lower MAEs are obtained with the proposed tool. In the first observation, generally lower, but nonetheless comparable MAEs are obtained in the workload variables with current engineering estimates.

The obtained results indicate that current engineering estimates tend to underestimate the workloads. This can be observed on the total workload, which is systematically underestimated, and, generally speaking, on the remainder workload variables. In order to better visualize the tendency of current estimates in underestimating the workloads and to demonstrate the higher accuracy of ForeSim-BI, average values of the observed workloads of the ‘8C’ checks, $\overline { { D } } _ { i } ,$ of the predicted workloads with the proposed tool, ${ \overline { { F _ { i } } } } ,$ and those predicted with current estimates, ${ \overline { { F _ { i } } } } ^ { \prime } { } _ { ; }$ , were calculated in each workload variable i for the three observations. Average errors were then calculated for both approaches. The results presented in Table 7 and Fig. 6 confirm the tendency of current engineering estimates to underestimate maintenance workloads. Underestimating workloads in the capacity planning process result in increased overtime costs given the fact that the diference between predicted and observed workloads has to be compensated during the execution of the maintenance checks. From a financial standpoint, assuming that the 917 man-hours of average error for the total workload obtained with current estimates (Table 7) would have to be performed as overtime, and that according to the Portuguese labour law the overtime hourly rate is 137.5% in average, this would represent an increased cost of 6% in one aircraft maintenance project, a mark of tens of thousands of euros. As MROs intervene several aircraft simultaneously, such costs increase proportionally. With ForeSim-BI, the consequence would be the distribution of the overestimated 245 manhours among maintenance tasks in other aircraft, a problem of operational nature rather than financial and with a more limited impact for MROs.

Average errors for three observations of the 8C' check obtained with ForeSim BI, ${ \overline { { E } } } _ { i } ,$ and with current engineering estimates, $\overline { { E _ { i } } } ^ { \prime }$ (man-hours).

<table><tr><td></td><td> $\overline{D}_{i}$ </td><td> $\overline{F}_{i}$ </td><td> $\overline{F}_{i}'$ </td><td> $\overline{E}_{i}$ </td><td> $\overline{E}_{i}'$ </td></tr><tr><td>TotalWL</td><td>5988</td><td>6233</td><td>5071</td><td>245</td><td>-917</td></tr><tr><td>WT1</td><td>2006</td><td>1700</td><td>1723</td><td>-306</td><td>-283</td></tr><tr><td>WT2</td><td>65</td><td>33</td><td>26</td><td>-31</td><td>-38</td></tr><tr><td>WT3</td><td>1055</td><td>1433</td><td>1011</td><td>379</td><td>-44</td></tr><tr><td>WT4</td><td>452</td><td>400</td><td>215</td><td>-52</td><td>-236</td></tr><tr><td>WT5</td><td>2224</td><td>2533</td><td>1944</td><td>309</td><td>-280</td></tr><tr><td>WT6</td><td>187</td><td>133</td><td>152</td><td>-54</td><td>-35</td></tr><tr><td>WP1</td><td>323</td><td>333</td><td>284</td><td>10</td><td>-38</td></tr><tr><td>WP2</td><td>3795</td><td>3900</td><td>3197</td><td>105</td><td>-598</td></tr><tr><td>WP3</td><td>24</td><td>100</td><td>32</td><td>76</td><td>9</td></tr><tr><td>WP4</td><td>41</td><td>100</td><td>45</td><td>59</td><td>5</td></tr><tr><td>WP5</td><td>1337</td><td>1333</td><td>1092</td><td>-4</td><td>-245</td></tr><tr><td>WP6</td><td>469</td><td>467</td><td>420</td><td>-2</td><td>-49</td></tr><tr><td>WS1</td><td>2081</td><td>2033</td><td>1727</td><td>-48</td><td>-354</td></tr><tr><td>WS2</td><td>2204</td><td>2367</td><td>1882</td><td>162</td><td>-323</td></tr><tr><td>WS3</td><td>602</td><td>700</td><td>532</td><td>98</td><td>-70</td></tr><tr><td>WS4</td><td>289</td><td>267</td><td>241</td><td>-23</td><td>-48</td></tr><tr><td>WS5</td><td>156</td><td>167</td><td>124</td><td>11</td><td>-32</td></tr><tr><td>WS6</td><td>655</td><td>700</td><td>565</td><td>45</td><td>-90</td></tr></table>

![](/api/attachments/S9BR6B2Q/fulltext/images/ee7ba9e111ee8eed623aa23c4effd0484267f77ee31e4d926c90d3593f98c083.jpg)  
Fig. 6. Average errors for three observations of the ‘8C’ check obtained with ForeSim-BI, ${ \overline { { E _ { i } } } } ,$ and with current engineering estimates, $\overline { { E _ { i } } } ^ { \prime }$ (man-hours).

As a final comment, the results for the proposed tool were obtained through BN models with discrete workload intervals of 100 man-hours, which were considered adequate for decision-making by experts of the host MRO. Nonetheless, errors will always occur with the discretization of workloads. For example, in $W P _ { 4 } ,$ the observed workload was always of 41 man-hours, and the workload predicted with the proposed tool of 100 man-hours, resulting in a systematic error of 59 man-hours, against an error of 0 man-hours for the second and third observations with current engineering estimates. BN models with smaller workload intervals, or even with continuous conditional probabilities for the workloads, constitute future research opportunities.

## 4. Conclusion and future research

A decision support tool for maintenance forecasting and capacity planning of complex product systems is proposed in this work. The tool $- F o r e S i m { \bf - } B I - ,$ developed and implemented in the particular case of a Portuguese aircraft MRO, integrates four modules into a single decision support tool that provides to maintenance organizations the ability of predicting the workload of both known and unprecedented maintenance interventions. First, the forecasting module, used to predict the total workload of future and unprecedented maintenance interventions, is combined with the BI module, developed to update prior forecasts into predictive forecasts as observations on the maintenance interventions being predicted become available. The forecasting module is based on a state space formulation of the AHW model, which presented the lowest AICc against other exponential smoothing models. The use of alternative forecasting models, such as ARIMA models, constitutes an important research opportunity. In addition, lognormal distributions are assumed for the total workload of the maintenance interventions and normal distributions for the lognormal parameter λ in the BI module. These have been found to be reasonable and convenient assumptions with the used data, but further research should be dedicated to test these and potential alternative distributions. Second, the simulation module is used to characterize the total workload with a higher level of detail, an essential aspect for efective capacity planning. This is achieved through the definition of three sets of random variables to characterize the total workload, including maintenance work types, maintenance work phases, and maintenance work skills. A bootstrapping procedure is also implemented to generate random discrete workload values for these variables. Finally, the BN module combines historical data with simulated data generated in the simulation module. A LP model is also developed to address the workload interval selection problem that occurs with the established BNs for capacity planning.

ForeSim-BI is tested and validated by comparing simulated work loads for a given aircraft maintenance intervention with real workloads of the same intervention. Moreover, the proposed tool is compared with a model simulating current forecasting practices employed by MROs. Interesting results are obtained with ForeSim-BI, particularly the reduction to 0% of the percentage error in the total workload with only one observation. A downward trend can also be observed in the MAE of all the considered workload variables and the superiority of ForeSim-BI over current forecasting practices has been demonstrated, resulting in an important cost saving potential for maintenance organizations. Lower errors are obtained with the proposed tool for the total workload and, generally speaking, for the remainder workload variables. Nonetheless, important errors are still obtained after two observations of the predicted intervention. This calls for future research regarding two aspects: (1) to study alternative approaches to bootstrapping in generating values for the workload variables, being Bayesian inference a technique that may be considered in this regard, notwithstanding the mathematical complexity involved; and (2) to develop BN models with smaller workload intervals, or even with continuous conditional prob abilities for the workloads, to reduce or eliminate errors resulting from discretization. On a related note, the MAPE has shown to be inadequate in measuring the accuracy of the predictions on the workload variables. Research on more appropriate error measures should be explored with similar examples to the ones presented in this paper.

As main conclusion, ForeSim-BI has shown to be an important quantitative tool, applied from a predictive analytics perspective, to support maintenance organizations of complex product systems in predicting and planning known and unprecedented maintenance interventions. The tool demonstrates how historical data and new observations can be used to improve the decision-making process of MROs in capacity planning, by producing accurate predictions automatically.

## CRediT authorship contribution statement

Duarte Dinis: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing - original draft, Writing - review & editing, Visualization. Ângelo Palos Teixeira: Conceptualization, Methodology, Investigation, Writing - review & editing, Supervision. Ana Barbosa-Póvoa: Conceptualization,

## Appendix A

Writing - review & editing, Supervision.

## Acknowledgments

This work was supported by the Portuguese National Science Foundation (FCT) under Grant PD/BD/52345/2013.

Sample of data collected at the host MRO including check types, total workloads, and workloads per work types (WT), per work phases (WP), and per work skills (WS) (man-hours).

<table><tr><td>Check</td><td>TotalWL</td><td>WT1</td><td>WT2</td><td>WT3</td><td>WT4</td><td>WT5</td><td>WT6</td><td>WP1</td><td>WP2</td><td>WP3</td><td>WP4</td><td>WP5</td><td>WP6</td><td>WS1</td><td>WS2</td><td>WS3</td><td>WS4</td><td>WS5</td><td>WS6</td></tr><tr><td>C</td><td>1506.8</td><td>263.1</td><td>955.4</td><td>151.6</td><td>0.0</td><td>26.0</td><td>110.8</td><td>18.0</td><td>352.0</td><td>255.2</td><td>525.4</td><td>342.2</td><td>14.0</td><td>202.0</td><td>285.6</td><td>630.2</td><td>327.7</td><td>0.0</td><td>61.3</td></tr><tr><td>2C</td><td>1868.9</td><td>431.9</td><td>776.8</td><td>432.8</td><td>0.0</td><td>90.2</td><td>137.3</td><td>18.0</td><td>202.0</td><td>424.0</td><td>1001.9</td><td>217.0</td><td>6.0</td><td>279.4</td><td>619.6</td><td>355.0</td><td>501.1</td><td>0.0</td><td>113.8</td></tr><tr><td>3C</td><td>3745.2</td><td>1410.3</td><td>463.5</td><td>425.3</td><td>2.9</td><td>863.7</td><td>579.6</td><td>19.0</td><td>124.6</td><td>1056.6</td><td>2418.0</td><td>108.5</td><td>18.5</td><td>604.4</td><td>826.4</td><td>0.0</td><td>1445.9</td><td>698.0</td><td>170.6</td></tr><tr><td>4C</td><td>3113.6</td><td>1148.3</td><td>670.5</td><td>775.3</td><td>4.0</td><td>101.3</td><td>414.3</td><td>19.0</td><td>131.1</td><td>488.8</td><td>2341.8</td><td>114.5</td><td>18.5</td><td>890.8</td><td>703.7</td><td>0.0</td><td>1299.2</td><td>8.0</td><td>211.9</td></tr><tr><td>5C</td><td>1748.2</td><td>90.5</td><td>851.6</td><td>597.9</td><td>0.0</td><td>18.8</td><td>189.4</td><td>31.2</td><td>191.9</td><td>374.6</td><td>877.7</td><td>250.2</td><td>22.6</td><td>172.9</td><td>541.8</td><td>88.7</td><td>783.3</td><td>0.0</td><td>161.6</td></tr><tr><td>6C</td><td>1878.7</td><td>318.0</td><td>878.6</td><td>487.3</td><td>0.0</td><td>8.3</td><td>186.7</td><td>29.2</td><td>203.4</td><td>439.6</td><td>991.9</td><td>196.0</td><td>18.6</td><td>180.9</td><td>597.4</td><td>73.7</td><td>820.7</td><td>0.0</td><td>206.1</td></tr><tr><td>7C</td><td>3011.9</td><td>133.5</td><td>954.6</td><td>1323.1</td><td>0.0</td><td>130.2</td><td>470.5</td><td>40.7</td><td>179.9</td><td>585.3</td><td>1944.4</td><td>238.9</td><td>22.7</td><td>252.7</td><td>781.8</td><td>66.1</td><td>1140.8</td><td>391.4</td><td>379.2</td></tr><tr><td>8C</td><td>6489.5</td><td>667.4</td><td>2096.4</td><td>2433.8</td><td>84.5</td><td>215.1</td><td>992.3</td><td>40.6</td><td>342.7</td><td>1427.2</td><td>4176.6</td><td>487.7</td><td>14.7</td><td>322.0</td><td>2411.6</td><td>147.1</td><td>2376.4</td><td>618.0</td><td>614.4</td></tr></table>

## References

[1] V. Guide, R. Srivastava, M.S. Spencer, An evaluation of capacity planning techniques in a remanufacturing environment, Int. J. Prod. Res. 35 (1997) 67–82, https:/ doi.org/10.1080/002075497195984.

[2] B. Almada-Lobo, J.F. Oliveira, M.A. Carravilla, Production planning and scheduling in the glass container industry: a VNS approach, Int. J. Prod. Econ. 114 (2008) 363–375, https://doi.org/10.1016/j.ijpe.2007.02.052.

[3] G. Figueira, P. Amorim, L. Guimarães, M. Amorim-Lopes, F. Neves-Moreira, B. Almada-Lobo, A decision support system for the operational production plannin and scheduling of an integrated pulp and paper mill, Comput. Chem. Eng. 77 (2015) 85–104. https://doi.org/10.1016/i.compchemeng.2015.03.017

[4] J. Zhou, J. Zhu, H. Wang, Strategic cooperation with capital-constrained supplier and downstream competition in complex product systems, Comput. Ind. Eng. 139 (2020) 106139, https://doi.org/10.1016/j.cie.2019.106139.

[5] P. Samaranayake, S. Kiridena, Aircraft maintenance planning and scheduling: an integrated framework, J. Qual. Maint. Eng. 18 (2012) 432–453, https://doi.org/10. 1108/13552511211281598

[6] N. Papakostas, P. Papachatzakis, V. Xanthakis, D. Mourtzis, G. Chryssolouris, An approach to operational aircraft maintenance planning, Decis, Support. Syst. 48 (2010) 604–612. https://doi,org/10.1016/i,dss,2009.11.010

[7] H.K. Al-Fares, S.O. Dufuaa, Maintenance forecasting and capacity planning, in: M Ben-Dava S O Duffuaa A Baouf J Knezevic D Ait-Kadi (Fds ) Handb Maint Manag, Eng, Springer, London, 2009, pp. 157–190

[8] M.C. Dijkstra, L.G. Kroon, J.A.E.E. van Nunen, M. Salomon, A DSS for capacity planning of aircraft maintenance personnel, Int. J. Prod. Econ. 23 (1991) 69–78, https://doi.org/10.1016/0925-5273(91)90049-Y.

[9] S. Yan, T.H. Yang, H.H. Chen, Airline short-term maintenance manpower supply planning, Transp. Res. A Policy Pract. 38 (2004) 615–642, https://doi.org/10. 1016/i.tra.2004.03.005

[10] P. De Bruecker, J. Van Den Bergh, J. Beliën, E. Demeulemeester, A model enhancement heuristic for building robust aircraft maintenance personnel rosters with stochastic constraints, Eur. J. Oper. Res. 246 (2015) 661–673, https://doi.org/10 1016/i,eior.2015.05.008

[11] J. Kurz, Capacity planning for a maintenance service provider with advanced information, Eur. J. Oper. Res. 251 (2016) 466–477, https://doi.org/10.1016/j.ejor. 2015.11.029

[12] P. De Bruecker, J. Van Den Bergh, J. Beliën, E. Demeulemeester, Workforce plan ning incorporating skills: state of the art, Eur. J. Oper. Res. 243 (2015) 1–16, https://doi.org/10.1016/j.ejor.2014.10.038.

[13] D.C. Montgomery, C.L. Jennings, M. Kulahci, Introduction to Time Series Analysis and Forecasting, John Wiley & Sons, 2008, https://doi.org/10.1017 CBQ9781107415324.004

[14] N.R. Sanders, K.B. Manrodt, The eficacy of using judgmental versus quantitative forecasting methods in practice, Omega 31 (2003) 511–522, https://doi.org/10. 1016/i.omega.2003.08.007

[15]. R.D. Klassen. B.E. Flores. Forecasting practices of Canadian firms: survey results and comparisons, Int. J. Prod. Econ. 70 (2001) 163–174, https://doi.org/10.1016/ S0925-5273(00)00063-3

[16] J. Mula, R. Poler, G.S. García-Sabater, F.C. Lario, Models for production planning under uncertainty: a review, Int. J. Prod. Econ, 103 (2006) 271–285, https://doi. org/10.1016/i.iipe.2005.09.001

[17] M. Arvan, B. Fahimnia, M. Reisi, E. Siemsen, Integrating human judgement into

quantitative forecasting methods: a review, Omega (United Kingdom) 86 (2019) 237–252, https://doi.org/10.1016/j.omega.2018.07.012.

[18] H.S. Kilic, S. Zaim, D. Delen, Development of a hybrid methodology for ERP system selection: the case of Turkish airlines, Decis. Support. Syst. 66 (2014) 82–92, https://doi.org/10.1016/j.dss.2014.06.011.

[19] J. May, G. Dhillon, M. Caldeira, Defining value-based objectives for ERP systems planning, Decis. Support. Syst. 55 (2013) 98–109, https://doi.org/10.1016/i.dss 2012.12.036

[20] I.A. Salman, Forecasting models for maintenance work load with seasonal components, Annu. Symp. Reliab. Maint. 2004 - RAMS, 2004, pp. 514–520, , https://doi. org/10.1109/RAMS.2004.1285499

[21] S.C. Eickemeyer, F. Herde, P. Irudayaraj, P. Nyhuis, Decision models for capacity planning in a regeneration environment, Int. J. Prod. Res. 52 (2014) 7007–7026 https://doi.org/10.1080/00207543.2014.923122

[22] A. Gandomi, M. Haider, Beyond the hype: big data concepts, methods, and analytics, Int. J. Inf. Manag. 35 (2015) 137–144.

[23] Y.-S. Huang, C.-C. Hung, C.-C. Fang, Bayesian enhanced decision making for deteriorating repairable systems with preventive maintenance, Nav. Res. Logist. 55 (2008) 105–115, https://doi.org/10.1002/nav.20268.

[24] D. Dinis, A. Barbosa-Póvoa, Â. Teixeira, Valuing data in aircraft maintenance through big data analytics: a probabilistic approach for capacity planning using Bayesian networks, Comput. Ind. Eng. 128 (2019) 920–936, https://doi.org/10. 1016/i.cie.2018.10.015

[25] S.O. Dufuaa, A.A. Andijani, An integrated simulation model for efective planning of maintenance operations for Saudi Arabian Airlines (SAUDIA), Prod. Plan. Control 10 (1999) 579–584, https://doi.org/10.1080/095372899232876.

[26] F.I. Khan, M.M. Haddara, Risk-based maintenance (RBM): a quantitative approach for maintenance/inspection scheduling and planning, J. Loss Prev. Process Ind. 16 (2003) 561–573, https://doi.org/10.1016/j.jlp.2003.08.011.

[27] ATA, ATA MSG-3 Operator/Manufacturer Scheduled Maintenance Development, Revision 2007.1, Air Transport Association of America Inc, Washington DC, 2007.

[28] K.R. Baker, D. Trietsch, Principles of Sequencing and Scheduling, John Wiley & Sons. 2009.

[29] M.B. Kline. Suitability of the lognormal distribution for corrective maintenance repair times, Reliab. Eng, 9 (1984) 65–80. https://doi,org/10.1016/0143-8174(84) 90041-6.

[30] F.J. Massey, The Kolmogorov-Smirnov test for goodness of fit, J. Am. Stat. Assoc. 46 (1951) 68. https://doi,org/10.2307/2280095.

[31] L.H. Miller, Table of percentage points of Kolmogorov statistics, J. Am. Stat. Assoc. 51 (1956) 111. https://doi.org/10.2307/2280807.

[32] R.J. Hyndman, A.B. Koehler, J.K. Ord, R.D. Snyder, Forecasting With Exponential Smoothing, Springer Berlin Heidelberg, 2008, https://doi,org/10.1007/978-3-540 71918-2.

[33] R.A. Pyles, Aging Aircraft - USAF Workload and Material Consumption Life Cycle Patterns, (2003).

[34] N. Sugiura, Further analysts of the data by Akaike's information criterion and the finite corrections, Commun. Stat. - Theory Methods. 7 (1978) 13–26, https://doi. org/10.1080/03610927808827599.

[35] C.M. Hurvich, C.-L. Tsai, Regression and time series model selection in small samples, Biometrika 76 (1989) 297–307, https://doi.org/10.1093/biomet/76.2. 297.

[36] J.V. Segura, E. Vercher, A spreadsheet modeling approach to the Holt-Winters optimal forecasting, Eur. J. Oper. Res. 131 (2001) 375–388, https://doi.org/10.1016 S0377-2217(00)00062-X

[37] D.F. Percy, Maintenance based on limited data, Complex Syst. Maint. Handb, Springer London, London, 2008, pp. 133–154, , https://doi.org/10.1007/978-1- 84800-011-7.6.

[38] A.H.-S. Ang, W.H. Tang, Probability Concepts in Engineering, Second edition, Wiley, 2007.

[39] W.M. Bolstad, Introduction to Bayesian Statistics, John Wiley & Sons, Hoboken, NJ, 2004.

[40] D. Dinis, A. Barbosa-Póvoa, Â. Teixeira, A supporting framework for maintenance capacity planning and scheduling: development and application in the aircraft MRO industry, Int. J. Prod. Econ. 218 (2019) 1–15, https://doi.org/10.1016/j.ijpe.2019. 04.029.

[41] D.P. Kroese, T. Taimre, Z.I. Botev, Handbook of Monte Carlo Methods, John Wiley & Sons, Inc., Hoboken, NJ, USA, 2011, https://doi.org/10.1002/9781118014967.

[42] R.E. Walpole, R.H. Myers, S.L. Myers, K. Ye, Probability & Statistics for Engineers & Scientists. Ninth edition. Prentice Hall. Boston. 2012

[43] R.J. Hyndman, A.B. Koehler, Another look at measures of forecast accuracy, Int. J. Forecast. 22 (2006) 679–688, https://doi.org/10.1016/j.ijforecast.2006.03.001.

[44] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Elsevier, 1988, https://doi. org/10.1016/C2009-0-27609-4.

[45] F.V. Jensen, T.D. Nielsen, Bayesian Networks and Decision Graphs, Springer, 2007.

[46] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete dat via the EM algorithm, J. R. Stat. Soc. Ser. B 39 (1977) 1–38.

[47] S.L. Lauritzen, The EM algorithm for graphical association models with missing data, Comput. Stat. Data Anal. 19 (1995) 191–201, https://doi.org/10.1016/0167- 9473(93)E0056-A

[48] J.J. Bergman, J.S. Noble, R.G. McGarvey, R.L. Bradley, A Bayesian approach to demand forecasting for new equipment programs, Robot. Comput. Integr. Manuf. 47 (2017) 17–21, https://doi.org/10.1016/j.rcim.2016.12.010.

[49] S. Makridakis, Accuracy measures: theoretical and practical concerns, Int. J. Forecast. 9 (1993) 527–529, https://doi.org/10.1016/0169-2070(93)90079-3.

[50] S. Kim, H. Kim, A new metric of absolute percentage error for intermittent demand forecasts, Int. J. Forecast. 32 (2016) 669–679, https://doi.org/10.1016/i.ijforecast 2015.12.003.

[51] R. Mantena, V. Tilson, X. Zheng, Literature survey: mathematical models in the

analysis of durable goods with emphasis on information systems and operations management issues, Decis. Support. Syst. 53 (2012) 331–344, https://doi.org/10. 1016/i.dss.2012.01.012

Duarte Dinis is a PhD student at the Center for Management Studies of Instituto Superior Técnico (CEG-IST). University of Lisbon, under the supervision of Prof. Ana Barbosa Póvoa and Prof. Ângelo Palos Teixeira. He holds a Master's degree in Mechanical Engineering with a specialization in aircraft maintenance. He has worked as a Project Manager in the naval sector and as a Maintenance Planner in aircraft maintenance. His research interests focus on the application of artificial intelligence and predictive ana lytics methods to real industrial problems.

Ângelo Palos Teixeira is Associate Professor at Instituto Superior Técnico (IST), University of Lisbon (UL). He has received his PhD degree in Naval Architecture and Marine Engineering by the Technical University of Lisbon in 2007 and the Master degree by the Faculty of Engineering of Glasgow University. He is member of the Executive Board of the research Centre for Marine Technology and Ocean Engineering (CENTEC) of IST and Principal Investigator of the research group on Safety and Logistics of Maritime Transportation of CENTEC. He is also Deputy Coordinator of the Master Degree in Naval Architecture and Ocean Engineering of IST. His main scientific areas of research are related to uncertainty modelling, risk assessment and management, maritime safety and trafic models, and reliability of marine structures, subsea systems and ofshore wind turbines.

Ana Barbosa-Póvoa is Full Professor of Operations and Logistics at the Department of Management and Engineering of Instituto Superior Técnico (IST). University of Lisbon She holds a PhD from Imperial College of Science Technology and Medicine. Her research interests are on the areas of Operations and Supply Chain Management where she has been exploring the optimization of global systems accounting for economic, environmental and social concerns. Ana has published widely in these areas and supervised several Master and PhD students. She has been coordinating several scientific projects, some of them in close collaboration with industry.
