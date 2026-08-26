---
otero_id: 21618
otero_key: "87VCZKMB"
title: "A marketing category management system: a decision support system using scanner data"
authors: "James J. Jiang; Gary Klein; Roger Alan Pick"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00053-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A marketing category management system: a decision support system using scanner data

James J. Jiang <sup>a,)</sup>, Gary Klein <sup>b</sup>, Roger Alan Pick <sup>c</sup>

College of Administration and Business, Louisiana Tech UniÕersity, P.O. Box 10318, Ruston, LA 71272-0046, USA <sup>b</sup> School of Business, The UniÕersity of Texas at Permian Basin, 4901 E. UniÕersity BlÕd., Odessa, TX 79762-0001, USA <sup>c</sup> Bloch School of Business and Public Administration, UniÕersity of Missouri-Kansas City, 5110 Cherry Street, Kansas City, MO 64110-2499, USA

Accepted 10 August 1998

## Abstract

Point-of-sale scanner data provides a unique opportunity for analyzing consumer package goods CPG trends and Ž . patterns. Decisions of ever-increasing complexity are made possible by the amount of data available. Unfortunately, the analysis of such voluminous data requires complex techniques and processing requirements not available to many marketing decision makers. In this paper, we describe a prototype system which allows users to manage the complex models and scanner data to make forecasts in an interactive fashion. A limited test of the prototype allowed users not familiar with the underlying models to develop product forecasts. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; Marketing management; Scanner data; BVAR forecasts

## 1. Introduction

Marketing decision-making in the consumer packaged goods CPG arena benefits from advances in Ž . the collection and compilation of electronic scanner data 2,4,15 . The key problem facing today’s CPG<sup>w</sup> <sup>x</sup> brand managers is not lack of data but a lack of systems that transform voluminous scanner data into decisions of strategic advantage 2,5,15,16 . For ex- <sup>w</sup> <sup>x</sup> ample, without new system assistance, the five staff-days spent analyzing bimonthly store audit data would increase to 5000 staff-days to analyze weekly-level scanner data 17 .<sup>w</sup> <sup>x</sup>

A review of the literature reveals that marketing models with scanner data appear unfamiliar to decision support systems DSS researchers 1,3,Ž . <sup>w</sup> 12,18,25,26 . Consequently, problems in scanner-<sup>x</sup> based system design receive little attention in the DSS literature. In addition, full scale applications require large capital investments in hardware and personnel. For this reason, current commercial systems solve isolated marketing problems, for example those focusing on pricing, feature and display effects <sup>w</sup> <sup>x</sup> 5,26 .

To help overcome these deficiencies, we propose a marketing category management system that permits CPG brand managers to exert frequent control on in-store pricing and promotion variables as well as on out of store variables such as advertising. This is termed a ‘level-two’ approach to solve today’s marketing scanner-data dilemma—too much data with too few marketing analysts. At level two, the system controls the marketing-mix variables in a given product category. This expands the more common ‘level-one’ approach of summary reports and exception reporting 2,19 .<sup>w</sup> <sup>x</sup>

We will begin with an introduction to singlesource systems, those systems containing multiple measurements of a single source. A later section introduces the prototype implementation in detail. Bayesian vector autoregression BVAR is the mod- Ž . eling approach on which the prototype system is based. An evaluation of the system’s ability to support user requests follows the system description. We will conclude by summarizing the study and describing future research directions.

## 2. The data: single-source systems

A single-source system is a database containing multiple measurements on single units of analysis, such as stores or households. The multiple measurements may include television viewing, advertising, in-store promotions, direct mail coupons, and scanned grocery purchases. The increasing popularity of single-source data is underscored by the fact that CPG firms spend about 1.3 billion dollars every year to purchase data from the two major data suppliers, Information Resources IRI and A.C. Nielsen.Ž .

Single-source data is collected at various stages in the product flow. Shipment data is collected on items from the factory to the warehouse, withdrawal data between the warehouse and retailer, consumer data at take-away time, and data about promotional activity. Five primary databases on which single-source data are accumulated: 1 a household database with con-Ž . sumer data; 2 a store database with sales and localŽ .

promotions; 3 a retail factors database with pricing, Ž . display and features; 4 a promotion factors databaseŽ . with coupons and sweepstakes; 5 and an advertis-Ž . ing database with active TV, print, and radio data. The power of a single-source system comes from a complex set of interactions among these five. Put simply, the system tracks what products are sold the Ž trade environment ; who bought these products the. Ž consumer environment ; and why these products were. bought the promotion environment 5 .Ž . <sup>w</sup> <sup>x</sup>

Table 1 presents an example framework which could represent a single-source dataset as a four dimensional Cartesian product. That is, a singlesource dataset CŽ . Ž . <sup>s</sup>Geographic level G <sup>=</sup>Product Ž . Ž . Ž . P <sup>=</sup> Time T <sup>=</sup> Measurements M . For example, one Cartesian product could be C1<sup>s</sup>Cincinnati metro-market area: at store level for Smith Groceries4  4  <sup>=</sup> All packaged beer products <sup>=</sup> Weekly data from 1995–1996.<sup>=</sup>Õolume, price, promotion, and display4. One can see how all the information is captured and how extensive the data quickly becomes.

IRI and Neilsen invest tremendous amounts of time and money to develop their single-source data management systems. Although an abundance of data sounds wonderful, the amount is usually too large for effective use. For example, for every single numeric value stored in a research database in 1979, at least 1420 were stored in 1989 10,15 . Currently, <sup>w</sup> <sup>x</sup> about two gigabytes of numeric values enter into IRI’s single-source systems every week 21 . The<sup>w</sup> <sup>x</sup> challenge facing the CPG industry is to efficiently and effectively analyze scanner data. In other words, in today’s competitive environment, CPG managers need automated systems to help analyze these data in support of decisions 15,20 .<sup>w</sup> <sup>x</sup>

Little 14,15 argues that brand managers should<sup>w</sup> <sup>x</sup> make their decisions through model-based DSSs to effectively use single-source data. His reasons are: Ž . 1 Brand managers’ information needs have shifted from traditional marketing status reports i.e., whatŽ are sales, price, and total revenue? to marketing. response reports i.e., what is price elasticity, adver-Ž tising response, promotional effectiveness . How-. ever, marketing response reports require complex models. 2 Marketing response output can help brandŽ . managers understand competitive interactions in a given product category. However, many existing models are hard to use, therefore, rarely applied in the marketing industry. 3 There is a shortage ofŽ . qualified marketing analysts in industry to help brand managers construct and use ‘good’ marketing models.

Table 1 Single-source dataset

<table><tr><td>(1) Geographic</td><td>(G): store, cluster of stores, metro-market, and national, etc. (individual Conditional forecast aggregate at geographic level)</td></tr><tr><td>(2) Product</td><td>(P): sku, brand, etc. (individual vs. aggregate at product category level)</td></tr><tr><td>(3) Time</td><td>(T): week, 2 weeks, month, and quarter, etc. (individual vs. aggregate at time horizon)</td></tr><tr><td>(4) Measurements</td><td>(M): price, volume, feature, and display, etc.</td></tr></table>

Curry 5 also argues that a model-based DSS <sup>w</sup> <sup>x</sup> offers bright long term prospects. His reasons include: 1 Contrary to the situation 10 years ago, Ž . managers are now accustomed to using models for specific problems; e.g., forecasting, product positioning, pricing. 2 Dozens of models have been devel-Ž . oped for key decision areas. The main challenge today is to use existing models productively rather than to develop new models. 3 Marketing planning Ž . typically involves multiple parts, each of which makes use of at least one model. 4 Models can findŽ . more consistent optimal solutions to problems than can expert systems.

## 3. The model: Bayesian vector autoregression

In order to choose a model for this system, we wanted to pick a model which matches the CPG situation. The CPG situation involves a large volume of data. Furthermore, that data involves numerous variables which interact with each other, and the data is a collection of time series. Marketers in the CPG arena, whether manufacturers or retailers, need to be able to make both conditional ‘What If?’ and un-Ž . conditional forecasts that account for competitive interactions among brands. The BVAR class of model meets all of these needs 6–8,24 .<sup>w</sup> <sup>x</sup>

In addition, the BVAR has capabilities and accuracy compared with other popular techniques. BVAR is able to provide forecasts of multiple data series where marketing activities of all players can be considered. Such a vector forecasting technique is critical to brand management. Previous studies have found BVAR to be an effective forecasting model. The use of BVAR in this precise context has been studied by Curry et al. 6,8 , Curry and Mathew 7 ,<sup>w</sup> <sup>x</sup> <sup>w x</sup> and Whiteman et al. 24 . Their conclusions state<sup>w</sup> <sup>x</sup>

Using POS scanner data, we establish that BVAR is a superior forecasting tool compared to Exponential Smoothing, univariate ARIMA, Box–Jenkins transfer function models, and MARMA. Because BVAR uses few degrees of freedom and is easy to identify, it satisfies the practical requirements of category management. Finally, using impulse response functions and conditional forecasts, we illustrate that BVAR provides important insights for the category manager. 6 , page 197<sup>ww</sup> <sup>x</sup> <sup>x</sup>

Other forecasting techniques capable of handling the data include the vector autoregression models Ž . VAR and the generalized autoregressive conditional heteroskedasticity GARCH models. Table 2Ž . is a comparison of the three methods for the dataset of this study. As can be seen, the BVAR outperforms these two techniques not previously considered. The results suggest that over-parameterization could be a problem for both the VAR and GARCH models. Especially since a large number of lags are the normal situation in the brand management applications.

Table 2  
Theil values for BVAR, VAR and GARCH models

<table><tr><td></td><td>Lag 2</td><td>Lag 3</td><td>Lag 4</td></tr><tr><td colspan="4">BVAR</td></tr><tr><td>Brand 1</td><td>6.01</td><td>6.67</td><td>8.67</td></tr><tr><td>Brand 2</td><td>3.71</td><td>4.11</td><td>6.91</td></tr><tr><td>Brand 3</td><td>7.17</td><td>7.08</td><td>6.36</td></tr><tr><td>Brand 4</td><td>3.49</td><td>3.09</td><td>3.39</td></tr><tr><td colspan="4">VAR</td></tr><tr><td>Brand 1</td><td>11.73</td><td>12.14</td><td>13.25</td></tr><tr><td>Brand 2</td><td>10.94</td><td>11.56</td><td>13.33</td></tr><tr><td>Brand 3</td><td>8.29</td><td>8.02</td><td>7.87</td></tr><tr><td>Brand 4</td><td>8.27</td><td>9.67</td><td>8.52</td></tr><tr><td colspan="4">GARCH</td></tr><tr><td>Brand 1</td><td>5.66</td><td>126.87</td><td>1345.87</td></tr><tr><td>Brand 2</td><td>2.44</td><td>234.61</td><td>2652.93</td></tr><tr><td>Brand 3</td><td>4.41</td><td>156.39</td><td>1623.99</td></tr><tr><td>Brand 4</td><td>4.74</td><td>149.57</td><td>1769.45</td></tr></table>

BVAR forecasts movements in an n-dimensional state vector. Mathematically, vector autoregression can be written:

$$
\boldsymbol {x} (w + l) = \mathbf {A} \boldsymbol {x} (w) + \mathbf {D} \boldsymbol {m} (w + l) + \boldsymbol {e} (w + l)
$$

where; $\textstyle { \boldsymbol { x } } ( { \boldsymbol { w } } )$ is an $N \times 1$ state vector for time period w, A is an $N \times N$ state transition matrix, $N = ( n \times$ $l ) + 1$ , n<sup>s</sup>number of time series variables in the system, l <sup>s</sup> number of lags, D is an $N \times q$ coefficient matrix, $\pmb { m } ( \boldsymbol { w } + 1 )$ is a $q \times 1$ vector of merchandising variables for time period $w + 1$ , eŽ . w <sup>q</sup> 1 is an $N \times 1$ white noise vector for time period $w + 1$ , and w is an index for time period.

Conceptually, the matrix A represents the ‘natural laws of motion’ influencing a category’s transition from one state to the next, and the matrix D captures the effects of merchandising variables. The state consists of variables which are out of the modeler’s direct control such as volume sales for each UPC and price and merchandising activities for other brands. The merchandising variables include items that the modeler can control in a deterministic way such as displays, features, coupon drops, and ownbrand prices.

The system’s dataset consists of n endogenous variables and q exogenous variables. All the relations in the model are linear. There is a total of $N \times q$ free coefficients in the model 9 . Since the<sup>w</sup> <sup>x</sup> $N \times q$ free coefficients are estimated using data, forecasts using unrestricted vector autoregression often suffer from over-parameterization of the model and, consequently, large out-of-sample forecast error. The Bayesian approach to estimation specifies ‘fuzzy’ restrictions on the coefficients rather than sharply including or dropping a given regressor 13 . <sup>w</sup> <sup>x</sup> Without reviewing the ‘fuzzy’ restrictions in detail, we outline the assumptions and principles of the Bayesian approach to VAR. For a detailed reviewŽ see Refs. 6,13 or Ref. 22 .<sup>w</sup> <sup>x</sup> <sup>w x</sup> .

Bayesian VAR uses Normal prior distributions with means of zero and small standard deviations for long lags 9 . This allows the system to estimate the<sup>w</sup> <sup>x</sup> coefficients using Theil’s mixed estimation technique 23 . The estimation process chooses a set of <sup>w</sup> <sup>x</sup> ‘hyperparameters’ for the prior distribution in the system. Identifying the ‘best’ BVAR model includes the following difficulties: a determining potential Ž .

variables, b placing prior distributions on coeffi-Ž . cients, and c the lack of clear guidance to evaluate Ž . the tremendous number of potential coefficients.

The system we propose eliminates many of the complex choices inherent in BVAR modeling. The prototype helps a user select variables by efficiently partitioning them into time series and deterministic variables. The system also helps simplify identification of the prior distribution by reducing the required number of hyperparameter specifications. Finally, the system helps a user digest the huge volume of estimation results generated from the existing system to find a prior distribution and set of variables that maximizes the model’s out of sample forecast accuracy.

This model-building activity is the first part of our DSS, which we call the model fitting subsystem. Using the model fitting system is a decision-making activity in which the decision-maker’s goal is to create the best possible model. The system assists in this by allowing the decision-maker to create a sequence of alternative models and examine their forecasting performance. We will go into this system in greater detail in Section 4.

The second part of the DSS is the model application subsystem. This subsystem uses the model built by the model selection subsystem. The user of this subsystem could be, but need not be, the same as the user of the model selection subsystem. The model application subsystem is the part of the DSS that actually assists in solving a business problem. Without any further modification, the model will answer unconditional questions such as: ‘What are expected baseline volumes, by week, for the next eight weeks? What are expected total revenues and market shares during the same time period?’ The model can also produce conditional forecasts to answer ‘what-if’ questions. For example, ‘If we lower the price of a given SKU by 10% two weeks in a row, what will our sales, market share, and total revenues be for each week for the 6 weeks that follow?’ The BVAR model application subsystem to answers these types of questions by generating forecasts conditioned upon fixed values for certain variables.

The objectives of the system, therefore, are to aid marketing analysts in generating high-quality forecasting models and to help brand managers generate and evaluate marketing strategies and policies. The

BVAR model-fitting and model-application sub-systems in the integrated DSS facilitate these services to the users.

## 4. A category management system

## 4.1. The conceptual model

Fig. 1 shows a conceptual model of the category management system. A defining element of a DSS is that the functionality derives from the interaction between the computer and decision maker. This particular system is designed for two different types of users: retailing managers and marketing analysts. A marketing analyst’s responsibility is to use data and analytical models to provide information for retailing managers’ decision needs. The model then provides forecasts for the model-application subsystem. Category managers use the model-application system to set up their marketing tactics, such as price-setting, featuring, and merchandising. The system allows them to input their tactics and make a forecast conditioned upon these specifications. Category managers can try a number of possibilities until they find a marketing plan with satisfactory forecast results.

![](/api/attachments/87VCZKMB/fulltext/images/6319551aba486ce531285252755fd208409c42795c10829d1b25b28a020f9a1e.jpg)  
Fig. 1. Conceptual model of the category management system.

The system supports brand managers as well as category managers. A brand manager for a manufacturer can only affect the marketing mix of the UPCs under his<sup>r</sup>her control. Their usage of the system would generally only be conditioned upon the smaller number of variables that they control, leaving the other variables outside their control to be forecast. If they wish to anticipate the impact of some action by the competition, this system will allow them to make forecasts conditioned upon that action.

The dataset used in the prototype system was sponsored by a major grocer and was collected by IRI. At the request of the sponsors, data was aggregated and the category disguised. This dataset retains 2 years of sales histories e.g., price, and volume , Ž . consolidated by 3 SKUs across all stores in a major U.S. metropolitan area, aggregated on a weekly basis. It also includes in-store and out-of-store causal data e.g., display, feature, advertising . In general,Ž . given the large number of items in a typical CPG category, item aggregation is almost always necessary 5,11 . Variables collected by IRI can be aggre-<sup>w</sup> <sup>x</sup> gated to the managers’ desired level of inquiry. Three logical candidates for aggregation are single store, store type, and metro-market 11 . We use data<sup>w</sup> <sup>x</sup> aggregated to the market level as requested by the sponsoring company. However, it is possible to implement the BVAR model using pooled store and individual store level data.

## 4.2. Model-fitting subsystem and interfaces

Fig. 2 shows the conceptual structure of the model-fitting subsystem. The following activities are controlled by the model-fitting subsystem:

1. Model specification: specifying the BVAR model.

2. Model generation: formatting user input for solution.

3. Model execution: controlling the actual running of the model.

4. Model output generation: generating the user reports.

5. Model storage: saving the calibrated category model into the model base.

The latter four functions are relatively straightforward involving common practices in model management. The first function, model specification, involves complex interaction with the marketing analyst. To illustrate the model generation process, Fig. 3 shows the proposed BVAR model creation decision process. Three major stages can be identified to construct a ‘best’ BVAR model for a particular product category.

![](/api/attachments/87VCZKMB/fulltext/images/74e761b604d8fb7e1a0891e2355b0b72d22cf6cd10b493b473913dae58391811.jpg)  
Fig. 2. Conceptual structure of the model-fitting system.

![](/api/attachments/87VCZKMB/fulltext/images/89af2ab7ef14deb7570f57b206ebbc2d30a0a5dbf99cb1b423e8617cadeaa202.jpg)  
Fig. 3. The proposed BVA model-fitting decision process.

## 4.2.1. Stage 1: specify time-series Õariables

In this stage, a user must select the forecast variables for a particular product category. The user can also update the existing variables in a category before parameters are estimated by the model-fitting system. The process of selecting or updating variables is interactive, and driven by menus and question-answering. When specifying a structure for time-series variables, the user first selects time-series variables to be forecast by the system. See Table 3.Ž . Then, for each continuous variable the user enters the number of time lagged values to include or allow a default value. Finally, the user specifies deterministic variables using a structure similar to that of the forecast variables. For each question, the system provides context-sensitive help messages. The fitting system also allows the user to update part of the specification without revising the entire model.

## 4.2.2. Stage 2: specifying a prior distribution

In this stage, the system requires input for four values: mean, weight, tightness, and decay. For greater support, each question has its own help message to guide users who are not familiar with these terms Appendix A . Furthermore, the system checksŽ . the specification for each parameter and automatically replaces any values that are out-of-range with default values. The user can review the existing specifications at any time and update these values on the screen.

Table 3  
Time series variable selection

<table><tr><td colspan="3">Stage (I): Question 1—selecting time series variables</td></tr><tr><td>S</td><td>TSUN1: Brand 1’s (Scotties)</td><td>Total volume sales</td></tr><tr><td>S</td><td>PRCD1: Brand 1’s (Scotties)</td><td>Store price on deal</td></tr><tr><td>S</td><td>TCOM1: Brand 1’s (Scotties)</td><td>Total TV commercial time</td></tr><tr><td></td><td>TSUN2: Brand 2’s (Kleenex)</td><td>Total volume sales</td></tr><tr><td>S</td><td>PRCD2: Brand 2’s (Kleenex)</td><td>Store price on deal</td></tr><tr><td>S</td><td>TCOM2: Brand 2’s (Kleenex)</td><td>Total TV commercial time</td></tr><tr><td></td><td>TSUN3: Brand 3’s (Puffs)</td><td>Total volume sales</td></tr><tr><td>S</td><td>PRCD3: Brand 3’s (Puffs)</td><td>Store price on deal</td></tr><tr><td>S</td><td>TCOM3: Brand 3’s (Puffs)</td><td>Total TV commercial time</td></tr><tr><td></td><td>HELP: Help screen!!!</td><td></td></tr></table>

Cursor´Move Up<sup>r</sup>Dn; Enter´Select.  
S indicates a selected variable.

Table 5  
Table 4  
In-sample fit report—Report I: Summary report of system equations

<table><tr><td rowspan="2">Equation no.</td><td rowspan="2">Dependent variables</td><td rowspan="2">Total observations</td><td colspan="2">R</td><td rowspan="2">Durbin Watson</td><td rowspan="2">Q statistic</td><td rowspan="2">Degree of freedom</td><td rowspan="2">Significance level</td></tr><tr><td>Unadjusted</td><td>Adjusted</td></tr><tr><td>1</td><td>TSUN1</td><td>112</td><td>0.79</td><td>0.74</td><td>2.13</td><td>39.32</td><td>104</td><td>0.12</td></tr><tr><td>2</td><td>PRCD1</td><td>112</td><td>0.65</td><td>0.61</td><td>2.14</td><td>49.96</td><td>104</td><td>0.01</td></tr><tr><td>3</td><td>PRCN1</td><td>112</td><td>0.77</td><td>0.74</td><td>2.20</td><td>20.16</td><td>104</td><td>0.91</td></tr><tr><td>4</td><td>PRCD2</td><td>112</td><td>0.67</td><td>0.64</td><td>2.05</td><td>20.03</td><td>104</td><td>0.92</td></tr><tr><td>5</td><td>PRCN2</td><td>112</td><td>0.78</td><td>0.75</td><td>2.06</td><td>25.67</td><td>104</td><td>0.69</td></tr><tr><td>6</td><td>PRCD3</td><td>112</td><td>0.62</td><td>0.58</td><td>1.95</td><td>19.92</td><td>104</td><td>0.92</td></tr><tr><td>7</td><td>PRCN3</td><td>112</td><td>0.79</td><td>0.74</td><td>1.93</td><td>34.61</td><td>104</td><td>0.26</td></tr></table>

The higher the value of R, the better the model fits the data ‘in-sample.  
The closer the Durbin Watson statistics is to 2, the better are forecasts.  
High significance for the Q-statistic indicates excessive residual autocorrelation.

## 4.2.3. Stage 3 Iterati( ) Õe improÕements : find candidate solutions

When the user decides that s<sup>r</sup>he wants a solution, the model generation system generates a BVAR model in Regression Analysis Time Series’ RATSŽ . format. Then the model execution system uses RATS time series modules to compute the results. RATS produces voluminous output; more than 100 pages for a category with only four products. The output generation system scans the output and produces a concise report for the user. Tables 4–6 show example reports of the in-sample fit, model structure, and out-of-sample forecasting ability of a user’s specified model. The model structure diagnosis report in Table 5 shows the relationships in the current model and allows the user to judge the model against experience and intuition. Once the user is satisfied with the specified model, the estimated model is stored in the model base for the model-application system. If the user is not satisfied with the model, s<sup>r</sup>he can revisit the variables and<sup>r</sup>or prior distribution. Model construction is an iterative process until the user is satisfied with the model’s out-of-sample forecast performance. Model generation, model computing, output generation, and model storage are transparent to the user.

Model structure diagnosis report—Report II: Model structure diagnosis

<table><tr><td colspan="5">Part (I):  $T-test^a$ </td></tr><tr><td>Variableb</td><td>Lag</td><td>Parameter</td><td>Standard error</td><td>T statistic</td></tr><tr><td>TSUN1</td><td>1</td><td>0.329</td><td>0.09</td><td>3.42</td></tr><tr><td>TSUN1</td><td>4</td><td>0.160</td><td>0.07</td><td>2.13</td></tr><tr><td>PRCD1</td><td>1</td><td>0.534</td><td>0.08</td><td>6.31</td></tr><tr><td>PRCD2</td><td>2</td><td>-0.161</td><td>0.07</td><td>-2.28</td></tr><tr><td>FEAT1</td><td>0</td><td>0.010</td><td>0.01</td><td>2.15</td></tr><tr><td>SUMMER</td><td>0</td><td>0.159</td><td>0.03</td><td>2.97</td></tr><tr><td>FALL</td><td>0</td><td>0.237</td><td>0.08</td><td>3.21</td></tr><tr><td colspan="5">Part (II):  $F-test^c$ </td></tr><tr><td colspan="3">Independent variable</td><td>F-test</td><td>Significance level</td></tr><tr><td colspan="3">TSUN1 (Scotties) (all previous weeks)</td><td>3.25</td><td>0.02</td></tr><tr><td colspan="3">PRCD1 (Scotties) (all previous weeks)</td><td>3.87</td><td>0.01</td></tr><tr><td colspan="3">PRCD2 (Kleenex) (all previous weeks)</td><td>3.11</td><td>0.05</td></tr></table>

<sup>a</sup> Equation no: 1; dependent variable: TSUN1 Scotties ; significant Ž . Ž . t<sup>G</sup>2.00 individual influence on TSUN1.  
<sup>b</sup>In your model, the dependent variable TSUN1 is highly related to the above variable s . Ž . Ž .  
<sup>c</sup> Dependent variable: TSUN1 Scotties current week ; influence total effects are significant Ž . Ž . $( F \geq 3 . 0 ) .$  
The F-test summarizes the T-tests shown in the previous section. TheŽ T-tests are ‘week specific’ while an F-test integrates over all weeks included in a model..

Table 6  
Output for Theil statistics—Report III: Out of sample forecasts

<table><tr><td>Weeks</td><td>Theil</td><td>Attention!</td></tr><tr><td>1</td><td>1.02</td><td>X</td></tr><tr><td>2</td><td>0.87</td><td></td></tr><tr><td>3</td><td>0.74</td><td></td></tr><tr><td>4</td><td>0.66</td><td></td></tr><tr><td>5</td><td>0.32</td><td></td></tr><tr><td>6</td><td>0.21</td><td></td></tr><tr><td>7</td><td>0.19</td><td></td></tr><tr><td>8</td><td>0.15</td><td></td></tr><tr><td>8 weeks Theil total =</td><td>4.16</td><td></td></tr></table>

Theil statistics for dependent variable: TSUN1 Scotties .Ž .  
Theil<sup>-</sup>1: Your model outperforms the Naive baseline model forŽ . this forecast period.  
Theil<sup>)</sup>1: Your model fails to outperform the Naive model for this forecast period.

## 4.3. Model-application subsystem and interface

Today, success in the PG business boils down to who can best predict the future 5,17 . Brand man-<sup>w</sup> <sup>x</sup> agers want to know what is going to happen to their business if they change their prices, promotional strategy or other elements of the marketing mix, either nationwide or market by market. The modelapplication system provides this kind of predictive ability. The model-application system transports the abstract model developed by the model-fitting system to the practical world of retailing or manufacturing.

Fig. 4 shows the conceptual structure of the prototype model-application system. The following activities are conducted by the system:

1. Marketing scenario specification: marketing conditions specified by users.

2. Model generation: format BVAR model for execution.

3. Model execution: forecasting the specified marketing conditions.

4. Output generation: Generating the reports to users

5. Scenario history maintenance: store the 16 most recent scenarios for later reference.

In the dialogue manager of Fig. 4, a brand manager specifies the marketing scenario that s<sup>r</sup>he wants to forecast. For example, if our competitors lower the price of their product 10% 2 weeks in a row, what will our sales, market share, and total revenues be for each week in the 8 weeks that follow? The user is allowed to specify any scenario by setting prices, features and displays for one or more brands in a category.

The requirements of specifying a marketing scenario are shown in Table 7. The user provides input via a form on screen. Any invalid inputs, such as typing a character instead of numeric key for a number are rejected by the system. In addition, the user can review previously attempted scenarios managed by the scenario history management system.

After the user has chosen a marketing scenario, the system generates a conditional forecast model based on the model developed. The conditional forecast model generation is controlled by the model generation system. The model execution system uses

![](/api/attachments/87VCZKMB/fulltext/images/6a6445fdb0089c9290c7bd8b270fae9e17c70548e839b3ee1374dadbb32ac4e2.jpg)  
Fig. 4. Conceptual structure of the model-application system.

Table 7 Marketing scenario input

<table><tr><td colspan="3">Conditional marketing scenario</td><td rowspan="2">Base period(Date: 3/10/97)</td></tr><tr><td></td><td>Week 1</td><td>Week 2</td></tr><tr><td>Price 1</td><td>0.69</td><td>0.69</td><td>0.49</td></tr><tr><td>Price 2</td><td>1.09</td><td>1.09</td><td>1.09</td></tr><tr><td>Price 3</td><td>1.29</td><td>1.39</td><td>1.19</td></tr><tr><td>Adv 1</td><td>10</td><td>10</td><td>155</td></tr><tr><td>Adv 2</td><td>17</td><td>25</td><td>17</td></tr><tr><td>Adv 3</td><td>100</td><td>150</td><td>35</td></tr><tr><td>M 1</td><td>OFF</td><td>OFF</td><td>ON</td></tr><tr><td>M 2</td><td>OFF</td><td>OFF</td><td>OFF</td></tr><tr><td>M 3</td><td>ON</td><td>ON</td><td>ON</td></tr></table>

Brand 1: Scotties.  
Brand 2: Kleenex.  
Brand 3: Puffs.

RATS to compute the conditional forecast results. An output generation system is used to digest the huge amount of printed output generated by RATS, and isolate certain statistics useful to the managers, such as market share. These algorithms and procedures are transparent to a user. Table 8 shows the sample 8-week forecast for one brand each brand inŽ a category has a similar report . Table 9 illustrates. how the system summarizes sales volume. A similar report is generated for total revenues.

## 5. Evaluation

Can marketing managers use the prototype system effectively? Twenty-one marketing managers were asked to use the prototype system to construct a BVAR model for a particular product category. All twenty-one successfully constructed the BVAR model. The mean quality of the specified BVAR model was 4.03 with a variance of 0.33. Model quality is measured by the out-of-sample forecasting ability of a user’s model Theil statistics. A Theil less than 8 indicates that a model performs better than a naive model defined as a function of predicted and actual values 23 . Smaller Theil values mean better<sup>w</sup> <sup>x</sup> forecasts.

Table 8  
Output for single brand forecast—Brand name: Brand 1 ScottiesŽ .

<table><tr><td></td><td>Week 1</td><td>Week 2</td><td>Week 3</td><td>Week 4</td><td></td></tr><tr><td colspan="6">Baseline forecast</td></tr><tr><td>Volume</td><td>228.57</td><td>237.30</td><td>238.86</td><td>237.96</td><td></td></tr><tr><td>Price</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.49</td><td></td></tr><tr><td>Total revenue</td><td>114.38</td><td>117.71</td><td>118.51</td><td>117.43</td><td></td></tr><tr><td>Market share</td><td>69</td><td>68</td><td>69</td><td>69</td><td></td></tr><tr><td colspan="6">Conditional forecast</td></tr><tr><td>Volume</td><td>168.45</td><td>187.83</td><td>233.87</td><td>240.86</td><td></td></tr><tr><td>Price</td><td>0.69</td><td>0.69</td><td>0.61</td><td>0.56</td><td></td></tr><tr><td>Total revenue</td><td>116.23</td><td>129.61</td><td>142.04</td><td>135.29</td><td></td></tr><tr><td>Market share</td><td>63</td><td>66</td><td>70</td><td>71</td><td></td></tr><tr><td></td><td>Week 5</td><td>Week 6</td><td>Week 7</td><td>Week 8</td><td>Total</td></tr><tr><td colspan="6">Baseline forecast</td></tr><tr><td>Volume</td><td>236.56</td><td>255.31</td><td>264.38</td><td>268.35</td><td>1967.5</td></tr><tr><td>Price</td><td>0.49</td><td>0.47</td><td>0.46</td><td>0.45</td><td>0.49</td></tr><tr><td>Total revenue</td><td>115.83</td><td>119.96</td><td>120.98</td><td>121.03</td><td>945.83</td></tr><tr><td>Market share</td><td>69</td><td>70</td><td>70</td><td>70</td><td>69</td></tr><tr><td colspan="6">Conditional forecast</td></tr><tr><td>Volume</td><td>233.19</td><td>250.16</td><td>257.83</td><td>260.98</td><td>1833.5</td></tr><tr><td>Price</td><td>0.54</td><td>0.57</td><td>0.49</td><td>0.48</td><td>0.58</td></tr><tr><td>Total revenue</td><td>125.37</td><td>126.73</td><td>125.95</td><td>125.09</td><td>1026.3</td></tr><tr><td>Market share</td><td>71</td><td>71</td><td>71</td><td>70</td><td>70</td></tr></table>

Table 9  
Sales volume summary report for the entire category

<table><tr><td>Week</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>8 weeks total</td></tr><tr><td>Brand</td><td>(97:5:18)</td><td>(97:5:25)</td><td>(97:6:1)</td><td>(97:6:1)</td><td>(97:6:15)</td><td>(97:6:22)</td><td>(97:6:29)</td><td>(97:7:5)</td><td></td></tr><tr><td>1</td><td>168.5</td><td>187.8</td><td>233.9</td><td>240.9</td><td>233.2</td><td>250.2</td><td>257.8</td><td>261.0</td><td>1833.2</td></tr><tr><td>2</td><td>73.3</td><td>73.4</td><td>75.7</td><td>75.1</td><td>73.4</td><td>79.0</td><td>82.3</td><td>84.3</td><td>616.5</td></tr><tr><td>3</td><td>22.0</td><td>20.6</td><td>20.7</td><td>20.5</td><td>19.8</td><td>22.0</td><td>23.4</td><td>24.0</td><td>172.9</td></tr></table>

Sales volume conditional forecasts Unit: 1000 .Ž .

The managers were able to use the system after less than an hour of training. None of them were statisticians; they could not have constructed, used, or interpreted BVAR models using RATS alone without this DSS to assist them. Managers were asked to measure the ease of use of the prototype system and their confidence in the constructed model. The mean responses were 8.24 out of 10 10— Ž extremely easy to use and 8.14 out of 10 extremely . Ž confident , respectively. Subjects with the aid of the. proposed system not only successfully constructed a BVAR model but also felt that the system is quite easy to use and are confident that they built a good model.

It is fair to say that system usage leads to successful model construction; each subject was successful. Stronger evidence of the system’s role in the process would be provided by comparing these results to cases where no support system were available or where some alternative systems were used. However, it is an extremely difficult task to find subjects who are familiar with BVAR modeling and are qualified to be subjects in such an experiment. Subjects in the present experiment were asked, ‘Can you write a BVAR model and run it in RATS environment?’ The answer was always ‘no.

## 6. Conclusions and future research

Checkout scanners generate a tremendous volume of marketing data for firms in the consumer packaged goods industry. These data create a new opportunity for brand managers to better understand their customers, to make better forecasts, and to better plan their tactics. However, the overwhelming amount of scanner data in conjunction with the complexity of marketing environments turns the CPG-brand manager’s dream into a nightmare. To overcome this nightmare, researchers argue the use of model-based DSS to automate data analysis. We report on a prototype Category Management DSS that introduces the use of BVAR model to practitioners.

The contributions of this system include the following.

Ž . 1 A system that is designed for category management. Current scanner-based DSSs can only either solve isolated marketing problems i.e., pricing Ž . or one brand in a given category at a time 5,26 .<sup>w</sup> <sup>x</sup>

Ž . 2 The system simplifies the usage of an econometric BVAR for scanner datasets. The model can digest the volume of scanner data and is able to effectively capture all marketing-mix variables in a product category. The prototype system simplifies the procedure of constructing a BVAR model and provides a user-friendly interface.

Ž . 3 Instead of adopting a traditional approach, the prototype system separated model management into two subsystems, modeling fitting and model application. This allows the DSS to be interactive to marketing analysts and marketing brand managers, separately. This allows brand managers, instead of asking them to construct analytical models, to focus on their business problems. Marketing analysts can use the model-fitting subsystem to automate model creation.

Ž . 4 The prototype system demonstrates an effective way to integrate an advanced RATS package into the marketing DSS. By implementing an output generating subsystem in model-fitting and model-applications subsystems, the prototype DSS reports only significant and relevant information to the users. The traditional volume of output generated by advanced time-series statistical systems are not presented to the users.

In order to completely automate the BVAR model fitting stage, future research on BVAR model fitting heuristics is encouraged. Instead of playing ‘what if marketing scenarios, a brand manager may seek an ‘optimal control’ solution that generates ‘next week’s’ marketing mix as a closed-loop feedback function of ‘this week’s’ market results. Optimal marketing algorithms based on BVAR modeling represent a promising direction for future research. The automation of other applications using BVAR, such as pricing and advertising strategies, provides challenges for DSS researchers 7,18,24 . <sup>w</sup> <sup>x</sup>

Another promising direction for future research would be to include more complex interactions among brands. For example, we could assume that other brand managers would have this tool or a similar one available to them. Then they would presumably run this same system to make forecasts conditioned upon their own actions and choose the best action that they are able to find. A better system would take this kind of activity into account and searching for a game-theoretic minimax solution.

IRI has developed a very complex single-source database management system for the marketing industry. However, an easy-to-query database interface should be designed in a DSS to provide the managers a way to specify a subset for their needs e.g., Ž a particular set of stores, products, or time periods .. The proposed single-source dataset framework of Table 1 could be used as the basis for designing such an interface to retrieve the data.

## Acknowledgements

The authors would like to thank the companies of Information Resources IRI for their support of thisŽ . research through the Integrated Research Center at the University of Cincinnati. Dr. Curry’s University Ž of Cincinnati comments on this project is highly. appreciated. Dr. Doan’s Estima Regression Analy- Ž . sis of Time Series software grant is also appreciated.

## Appendix A. Help screen for prior specification phase

Ž . 1 MEAN: 0.1 to 1.0 governs a variable’s own<sup>w</sup> <sup>x</sup> first-week lag in each equation. Setting MEAN at 1.0 centers the prior distribution on a model that assumes this week’s value will be identical to last week’s value except for random movements.

The MEAN index controls how much weight a variable’s own one-week lag has on its current level. ŽFor example, how much do last week’s sales influence this week’s sales..

A MEAN value of 0.0 indicates no CARRY-OVER effect from last week while a value of 1.0 means that on average last week’s level DETER-Ž . MINES this weeks level.

Remember that no matter what value you specify, the data can override your judgement. However, by setting MEAN at a low value 0.1 to 0.4 you areŽ . effectively demanding that carry-over effects—revealed by the data—be very large before they can impact results. Normally, MEAN is set to 1.0 because carry-over effects are typically important for most time series.

Ž . 2 OTHER’S WEIGHT: 0.1 to 1.0 controls how<sup>w</sup> <sup>x</sup> much weight one variable say price may have Ž . when affecting another variable say sales . Ž .

Note that the MEAN index controls a variable’s own first lag. Its value is typically higher than the values for WEIGHT which controls the impact of all other variables’ first lags.

If WEIGHT<sup>s</sup>0.0 your model is effectively a set of univariate autoregressions. That is, each variable is being predicted only its own past values. Setting WEIGHT<sup>s</sup>0.0, therefore, removes competitive interactions and marketing mix effects from the model.

Ž . 3 TIGHTNESS: 0.1 to 2.0 directly controls the<sup>w</sup> <sup>x</sup> standard deviation of your prior, that is, how much weight is given to each variable’s own lags other than week one.

Setting TIGHTNESS at a very small value, say 0.01 virtually eliminates the effects of 2nd, 3rd, and higher order lags even if you have specified such lags in your model.

Normal values for this parameters are in the range 0.1 to 0.4. Generally values in the range 0.8 to 1.2 are considered ‘loose’ and permit the data to override your judgement.

Ž . 4 DECAY: 0.1 to 1.0 summarizes how quickly<sup>w</sup> <sup>x</sup> carry-over effects from one week to the next dissi- Ž . pate. The higher the value the more quickly effects dissipate; e.g., the less successive weight put on each lag as you move back in time: last week, 2 weeks ago, 3 weeks ago, etc.

Normal values for this index are in the range 0.1<sup>w</sup> to 0.2 . The system default is 0.2. <sup>x</sup>

## References

<sup>w</sup> <sup>x</sup> 1 M.M. Abraham, L.M. Lodish, An implemented system for improving promotion productivity using store scanner data, Marketing Science 12 1993 248–269. Ž .

<sup>w</sup> <sup>x</sup> 2 R. Blattberg, Learning How the Market Works, Marketing Science Institute Conference, Cambridge, MA, Sep. 21–22, 1989.

<sup>w</sup> <sup>x</sup> 3 R. Blattberg, R. Briesch, E.J. Fox, How promotions work, Marketing Science 14 1995 122–132.Ž .

<sup>w</sup> <sup>x</sup> 4 D. Curry, Single-source systems: retail management present and future, Journal of Retailing 65 1989 1–20.Ž .

<sup>w</sup> <sup>x</sup> 5 D. Curry, The New Marketing Research Systems, Wiley, New York, 1993.

<sup>w</sup> <sup>x</sup> 6 D. Curry, S. Divakar, S. Mathur, C. Whiteman, BVAR as a category management tool: an illustration and comparison with alternative techniques, Journal of Forecasting 14 1995Ž . 181–199.

<sup>w</sup> <sup>x</sup> 7 D. Curry, G. Mathew, Optimal demand-side retail pricing for EDLP conditions, Working paper, the Center of Integrated Research Systems, The University of Cincinnati, April, 1997.

<sup>w</sup> <sup>x</sup> 8 D. Curry, G. Mathew, N.T. Bruvold, Store level scanner data and category management: modelling and estimation techniques, Working paper, The Center of Integrated Research Systems, The University of Cincinnati, July, 1996.

<sup>w</sup> <sup>x</sup>9 T. Doan, R.S. Litterman, C.A. Sims, Forecasting and conditional projection using realistic prior distribution, Econometric Review 3 1984 1–100.Ž .

<sup>w</sup> <sup>x</sup> 10 G. Eskin, Single Source Data: The U.S. Experience, presented to The Special Joint ARF<sup>r</sup>MRS Research Leaders Seminar, Boston, MA, July 24, 1989.

<sup>w</sup> <sup>x</sup> 11 E.W. Foekens, P.S. Leeflang, P.R. Wittink, A comparison and an exploration of the forecasting accuracy of nonlinear models at different levels of aggregation, Working Paper, Department of Economics, University of Groningen, Groningen, Netherlands, July, 1993.

<sup>w</sup> <sup>x</sup> 12 P.M. Guadagni, J.D. Little, A logit model of brand choice calibrated on scanner data, Marketing Science 3 1983 203–Ž . 238.

<sup>w</sup> <sup>x</sup> 13 R.S. Litterman, A Bayesian procedure for forecasting with vector autoregressions, Working paper, Massachusetts Institute of Technology, Department of Economics, Boston, MA, 1980.

<sup>w</sup> <sup>x</sup> 14 J.D.C. Little, Decision support systems for marketing managers, Journal of Marketing 43 1979 9–26.Ž .

<sup>w</sup> <sup>x</sup> 15 J.D.C. Little, New Opportunities in a Changing World—The 1990 Philip McCord Morse Lecture, ORSA<sup>r</sup>TIMS Joint National Meeting, Philadelphia, PA, Oct 29, 1990.

<sup>w</sup> <sup>x</sup> 16 J. McCann, Overview of marketing system past, present, and future, Marketing Science Institute Conference, Cambridge, MA, Sep 21–22, 1989.

<sup>w</sup> <sup>x</sup> 17 J. McCann, J.P. Gallagher, Expert Systems for Scanner Data Environments: The Marketing Workbench Laboratory Experience, Kluwer Academic Publishers, 1989.

<sup>w</sup> <sup>x</sup> 18 J.H. Pedrick, F.S. Zufryden, Evaluating the impact of advertising media plans: a model of consumer purchase dynamics

using single-source data, Marketing Science 10 1991 111– Ž . 130.

<sup>w</sup> <sup>x</sup> 19 B. Peters, ‘Brave new world’ of single source information, Marketing Research 2 1990 13–21.Ž .

<sup>w</sup> <sup>x</sup> 20 J.B. Rochester, D.P. Douglass, Building marketing information systems, I<sup>r</sup>S Analyzer 28 1990 .Ž .

<sup>w</sup> <sup>x</sup> 21 J. Schmitz, G. Armstrong, J. Little, Coverstory—automated news finding in marketing, Interfaces 20 1990 29–38.Ž .

<sup>w</sup> <sup>x</sup> 22 C.A. Sims, Macroeconomics and reality, Econometrica 48 Ž . 1980 1–48.

<sup>w</sup> <sup>x</sup> 23 H. Theil, Principles of Econometrics, Wiley, New York, 1971.

<sup>w</sup> <sup>x</sup> 24 C.H. Whiteman, C. Curry, S. Divakar, S. Mathur, Dynamically optimal pricing strategies for consumer packaged goods, Working paper, the Center of Integrated Research Systems, The University of Cincinnati, May, 1996.

<sup>w</sup> <sup>x</sup> 25 D.R. Wittink, J.C. Poter, S. Gupta, Dangers in using marketing-level data for determining promotion effects, Marketing Science Institute Report No.93-115, 1–40.

<sup>w</sup> <sup>x</sup> 26 M.J. Zenor, The profit benefits of category management, Journal of Marketing Research 31 1994 202–213.Ž .

![](/api/attachments/87VCZKMB/fulltext/images/0f5840778aa7d96d3d7f94513632d961ee3afb463667ad875ec40a53dafd182c.jpg)

Dr. James J. Jiang is an Associate Professor of Computer Information Systems at the College of Administration and Business, Louisiana Tech University. His PhD in Information Systems was awarded by the University of Cincinnat in 1992. He earned his MBA in Management Science and MS in Applied Mathematics degrees from Wright State University in 1988 and 1989, respectively. His research interests include system development and implementation

and marketing modeling-based systems. He has published more than 50 journal articles in these areas. He is a member of ACM, IEEE, and DSI.

![](/api/attachments/87VCZKMB/fulltext/images/bd457d7c2919003f9e9bb7e31aa3c0fa796b7061e583c2a850f59bd8c4955667.jpg)

Dr. Gary Klein is Couger Chair of Information Systems at the University of Colorado in Colorado Springs. He obtained his PhD in Management Science at Purdue University. Before that time, he served with Arthur Anderson in Kansas City and was director of the Information Systems department for a regional financial institution. He was previously on the faculty at the University of Arizona, Southern Methodist University and Louisiana Tech Univer-

sity. His specialties include information system development and mathematical modeling with 50 publications in these areas. In addition to being an active participant in international conferences, he has made professional presentations on Decision Support Systems in the US and Japan where he once served as a guest professor to Kwansei Gakuin University.

![](/api/attachments/87VCZKMB/fulltext/images/3596c8408686a402e01b9c53f5f1694e77bfbe6662ef15cc0bfe074a1e5c36db.jpg)

Roger Alan Pick is an Associate Professor of Management Information Systems at the Henry W. Bloch School of Business and Public Administration at the University of Missouri-Kansas City. He joined the faculty at the Bloch School in 1993. Besides UMKC, Dr. Pick has taught at Purdue University, the University of Wisconsin-Madison, the University of Cincinnati, and Louisiana Tech Unversity. His PhD in Management Science major in Systems Analysis andŽ

Computer Science, minor in Applied Economics was awarded by. Purdue University in 1984. His MS from Purdue and his BSŽ . Ž . from Oklahoma University degrees are in mathematics. Pick is a member of the ACM, DSI, IEEE and INFORMS. Dr. Pick’s research interests are in model management, decision support systems, marketing information systems, and in the economics of information technology. His research on these topics has resulted in scholarly articles appearing in Management Science, Communication of the ACM, Journal of Management Information Systems, Expert Systems, and other outlets. For more information, see his homepage at http:<sup>rr</sup>cctr.umkc.edu<sup>r</sup>user<sup>r</sup>rpick<sup>r</sup>
