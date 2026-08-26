---
otero_id: 18600
otero_key: "MWSNHDYZ"
title: "Choosing a software cost estimation model for your organization: A case study"
authors: "Jainendra K. Navlakha"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90027-f"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Choosing a Software Cost Estimation Model for Your Organization: A Case Study

Jainendra K. Navlakha

School of Computer Science, Florida International University, Miami, FL 33199, USA

In the last decade or so, many software cost estimation models have been developed. These differ substantially from each other, particularly with respect to the inputs required and their outputs. For a software manager, the problem of selecting a particular model, or a combination of models that can be applied to an individual organization, is not at all trivial. This paper describes our efforts to solve this problem for two organizations who had collected data on past development efforts. Statistical correlations between the actual and the estimated efforts calculated by using different cost estimation models were obtained. Regression analysis revealed that the cost model that is used by the organizations is not ideal for their environment. Statistical tests show that the results obtained are indeed statistically significant. The methodology used to perform the case study is applied to predict the development effort for a project, and the result is quite impressive.

Keywords: Software Cost Estimation, Estimation Models, Statistical Correlation, Linear Regression, Statistical Significance.

![](/api/attachments/MWSNHDYZ/fulltext/images/5cb2e618d2275cbcd7d0bc01481d24b48a531738fe1e0dfb4fdea60106f7ce09.jpg)

Jai Navlakha received his Ph.D. from Case Western Reserve University in December 1977. Currently, he is the Professor and Director of the School of Computer Science at Florida International University. He was a member of the delegation of computer software specialists to PRC in 1983, an IEEE Distinguished lecturer to South America in 1984, and Distinguished Visitor of IEEE Computer Society in 1985–86. He has published widely in the areas of software metrics, A/I and expert systems, and neural networks.

## 1. Introduction

In the early days of computing, software costs represented a small percentage (generally less than 20%) of the overall costs of a computer-based system. Thus sizable error in estimates of software cost had relatively little impact on the success of a project. Today, however, the scenario is completely different, because software costs represent almost 80% of the system cost [5].

One estimate [12] puts the cost of all aspects of computing in the USA in 1990 to be 12.5% of the Gross National Product. As software costs form a major component of the total cost of most computer-based systems being developed today, this makes software one of the most cost intensive activities in the USA. Similar figures are valid for the industrialized nations of the world. As a result, a large estimation error in the projected cost of software development can make a very significant difference between profit and loss. The financial success of a project can depend on the ability of the software manager to estimate the cost of software development accurately, prior to the start of the project.

Software cost and effort estimation will never be an exact science. Too many variables – human, technical, environmental, political – can affect the ultimate cost of software and the effort needed to develop it. However, software project estimation can be transformed from a black art into a series of systematic steps that provide estimates with an acceptable degree of risk.

Here, we define and classify cost estimation models used to estimate various attributes of software. These models differ significantly with respect to the inputs they require and the outputs they produce. We then describe an experiment conducted to emphasize the necessity of customizing a software cost estimation model for an individual environment and summarize the results of the statistical analysis. Our recommendations to a software manager on how to choose a model in an environment are finally discussed.

## 2. Classification of Software Cost Estimation Models

Pressman [13] defines an estimation model for computer software as one that uses empirically derived formulae to predict data that are a required part of the software planning step. As the empirical data that support most models are derived from a limited set of projects, no estimation model is appropriate for all classes of software and in all development environments.

Resource models, which include software cost estimation models, consist of one or more empirically derived equations that predict effort, project duration, or other pertinent project data. In general, modeling a process is an attempt to explain what is going on in that process by making assumptions about the underlying process and simplifying the environment by removing extraneous and less relevant factors. Resource modeling can be used, among other ways, for initial prediction; i.e., given what we know or can guess about a project, modeling can help predict the effort, cost, staffing pattern, computer time, etc. required to produce the product. The main need is to discover the relationships between a set of characteristics that we know or can estimate and the resource elements of concern.

Basili [2] categorized these models into three main classes: static single-variable models, static multivariable models, and dynamic multivariable models.

## (a) Static Single-Variable Models

These models take on the form:

$$
\text { resource } = c * (\text { estimated   characteristic }) ^ {d},
$$

where the resource could be effort, project duration, staff size, or lines of software documentation. Constants c and d are determined from regression analysis applied to historical data. The first version of the Walston and Felix model [18] (called the IBM model in this paper) falls into this category. The effort equation in the IBM model is:

$$
\text { Effort } = (5. 2) * (\mathrm{KDSI}) ^ {0. 9 1} \text {   staff - months },
$$

where, KDSI refers to thousands of delivered source instructions. Boehm's Constructive Cost model [3] (called the COCOMO model) is a collection of hierarchically developed models. The first of these, called the Basic COCOMO model, belongs to this category. The effort equation in that model is given as:

$$
\text { Effort } = a * (\text { KDSI }) * \exp (b),
$$

where a and b are constants for an individual organization.

## (b) Static Multivariable Models

A resource estimation model that is based on several parameters and calculates a single resource value is called a static multivariable model. Some of these models start with a baseline equation based on historical data and adjust the initial estimate by a set of variables which attempts to incorporate the effects of important product and process attributes. Other models in this category start with a baseline equation that involves more than one variable.

A typical model in this category takes on the form:

$$
\text { resource } = c _ {1} * e _ {1} + c _ {2} * e _ {2} + c _ {3} * e _ {3} + \dots ,
$$

where, $e_{i}$ is the ith software characteristic and $c_{i}$ is the empirically derived constant for that characteristic. Boehm's Intermediate COCOMO model is a good example of static multivariable model that computes software development effort as a function of program size and a set of “cost drivers” that includes subjective assessment of product, hardware, personnel, and project attributes.

## (c) Dynamic Multivariable Models

These models project resource requirements as a function of time. If the model is derived empirically, then the resources are defined in a series of time steps that allocate some percentage of effort (or other resources) to each step of the software engineering process. A theoretical approach to dynamic multivariable modeling hypothesizes a continuous “resource expenditure curve” [2] and, from it, derives equations that model the behaviour of the resource. Examples of software cost estimation models that fall into this category include Putnam’s SLIM model [14], Jensen's SEER model [8] and RCA's PRICE-S model [6].

## 3. Differing Features of Cost Estimation Models

As already discussed, there have been several efforts towards the development of software cost estimation models. The most popular ones include Boehm's COCOMO model, Putnam's SLIM model, RCA's PRICES model, Jensen's SEER model and Grumman's SOFCOST model. All are commercially available and many software industries are using them for their cost estimations. Other cost models include: IBM's Wolverton model, the Doty model, the SDC model and so on. Boehm [4] gives a good short summary of all these models.

Major variations between these models are seen in the form of the inputs required and their outputs. For example, COCOMO inputs include ratings of attributes related to product, computer, personnel and project along with an estimate of total delivered source instructions (DSI); PRICE-S requires project magnitude in the form of equivalent executable assembly language statements, project application area, the level of new design and code, experience and skill levels of project members, hardware constraints, customer specification and reliability requirements, and development environment conditions; SLIM requires an estimate of development time, DSI and some indication of the level of technology usage in the development environment (which may be calculated by the model, also).

The outputs produced by these models also differ substantially from one another. All the models provide an estimate of the development effort and therefore the development cost. COCOMO provides a breakdown of this cost, based on individual subsystem tasks; it also gives the estimated productivity of the software development. PRICE-S gives the detailed schedule summary on a monthly basis and the costs incurred as the development progresses. It also provides risk projections based on variations in the estimated size, the development schedule or index of application area. A monthly progress summary showing the distribution of effort and associated costs throughout the performance of the development project is also part of its output. SLIM provides a region of feasible solutions for the project, so that the manager can choose a particular one based on such criteria as minimum cost, minimum development time, minimum difficulty, or the effort/time tradeoff function applicable to that project.

The list of required inputs and outputs produced by various models are not exhaustive. Clearly, these cost estimating models are quite different from each other. Each considers a different set of software characteristics as its parameters and ignores or makes assumptions about others. Therefore, not all are applicable for all classes of software and in all development environments. In fact, Mohanty [10] has shown that the results of using different models on the same project can give cost estimates which are an order of magnitude different. Indeed, it is quite possible that, for a particular organization, no one model may capture all the idiosyncracies of its software development environment. In that case, some combination of more than one model may be required for accurate estimation.

To study the suitability of using a particular cost estimation model (or some combination of several) in a software development environment, we conducted an experiment using some commercially developed project data.

It must be pointed out that much work related to validation of software cost estimation models $[9]$ , portability of cost estimation models $[1]$ , software sizing $[17]$ , etc. has been reported in the literature. In our analysis, we assume that the models are valid and the estimates are accurate.

## 4. Description of the Experiment

For this experiment, seven cost estimation models were used. COCOMO is a series of hierarchically developed models that operate in three modes - organic, semidetached, and embedded. We used the Intermediate COCOMO model in all three modes to provide greater accuracy than the basic model, and because it is more suitable for cost estimations in more detailed stages of software product development. The three modes were used because we were not sure what were the software development modes for the individual projects. The other four models employed in this experiment are: Putnam's SLIM, Jensen's SEER,

Table 1  
A Portion of Actual Data.

<table><tr><td>Project Number</td><td>Delivered Source Instructions</td><td>Actual Effort (Man-years)</td><td>Development Time (years)</td></tr><tr><td>1</td><td>80,000</td><td>10</td><td>3</td></tr><tr><td>2</td><td>102,548</td><td>26.61</td><td>2.667</td></tr><tr><td>3</td><td>47,124</td><td>7.4</td><td>1.5</td></tr><tr><td>4</td><td>74,300</td><td>11.25</td><td>2.33</td></tr><tr><td>5</td><td>104,327</td><td>29.86</td><td>3.667</td></tr><tr><td>6</td><td>56,401</td><td>13.834</td><td>1.392</td></tr><tr><td>7</td><td>46,147</td><td>12.776</td><td>1.275</td></tr></table>

Doty, and the IBM model. Thus, with respect to the classification of resource models, we considered two static single-variable models (Doty and IBM), three static multivariable models (three modes of Intermediate COCOMO) and two dynamic multivariable models (SLIM and SEER).

In this experiment, we collected data for seven software projects from two software development organizations. All these projects fall under the category of software systems and tools. Typical projects were, rehosting an image analysis system from PDP-11 to VAX (considerable software had to be written), acquiring satellite data from an external link located thousands of miles away for charting maps, computer graphics package as a development aid, and a genaralized tester system for various scientific projects. Table 1 shows part of the actual data collected for these seven projects.

It should be noted that, in the actual circumstances, the models are used prior to the start of software development and thus the input values are e.g., estimated DSI, estimated development time, etc. The purpose of this study is to determine which model (or combination of models) is appropriate for cost estimation in a particular environment. We assume that the estimations are quite accurate and thus we can substitute them by the actual DSI and actual development time in the models. The importance of this study is that if the initial estimates of DSI and development time are good, then the results of this experiment are valid. This approach, studying some software principles after the fact, in order to learn more about their characteristics, is not new. Researchers in other software engineering areas, like software complexity measures, have used it successfully in the past.

In addition to collecting the data shown in Table 1, we also interviewed the software managers and/or coordinators of the seven projects to obtain their ratings of personnel, product, computer, and project attributes that are required by the COCOMO model, as well as some other related but different attributes used by the Jensen model. It was also found that the organizations used the Intermediate COCOMO model in semidetached mode for their cost and effort estimations. A brief summary of how the development efforts were calculated or obtained, is now given.

## COCOMO Effort

At Florida International University, we have the commercially available implementation of COCOMO model developed by Wang Institute. Knowing DSI and the ratings of all fifteen COCOMO attributes for all seven projects, we determined the values of the Intermediate COCOMO efforts for all three modes – organic, semidetached and embedded.

## SLIM Effort

To determine the value of the SLIM effort, in addition to the estimates of DSI and the development time, one needs to know the value of the technology coefficient ( $C_{k}$ ) for the development of a project. Typical values for the technology coefficient are $C_{k}=2000$ for a poor software development environment (poor documentation and reviews, no methodology, a batch execution mode), $C_{k}=8000$ for a good development environment (methodology in place, interactive execution mode, adequate documentation and reviews), and $C_{k}=11000$ for an excellent environment (automated tools and techniques). We used the method described by Putnam [15] to determine the value of $C_{k}$ for individual projects. Table 2 shows the values of the technology coefficients for all 7 projects. Knowing $C_{k}$ , the development effort is computed as

Table 2  
$C_{k}$ and f for 7 Software Projects.

<table><tr><td>Project Number</td><td> $C_k$ </td><td>f</td></tr><tr><td>1</td><td>6,765</td><td>1.8575</td></tr><tr><td>2</td><td>6,765</td><td>2.6756</td></tr><tr><td>3</td><td>10,946</td><td>2.025</td></tr><tr><td>4</td><td>8,362</td><td>1.2946</td></tr><tr><td>5</td><td>4,181</td><td>2.6692</td></tr><tr><td>6</td><td>10,946</td><td>3.2585</td></tr><tr><td>7</td><td>10,946</td><td>1.4876</td></tr></table>

$$
\text { SLIM   effort } = 0. 4 * \left(\mathrm{DSI} / \mathrm{C} _ {\mathrm{k}}\right) ^ {3} / \left(\mathrm{t} _ {\mathrm{d}}\right) ^ {4},
$$

where, $t_d =$ development time.

## Jensen Effort

In the absence of the availability of Jensen's SEER model, we used SLIM's $C_{k}$ to substitute for the basic technology constant ( $C_{tb}$ ) of this model. This is not as outrageous as it appears, because fundamentally, this model is a combination of the COCOMO and SLIM models. So, for the purposes of this experiment, let $C_{tb} = C_{k}$ . Knowing the ratings of relevant attributes, we get

$$
C _ {t e} = C _ {k} / f,
$$

where, $C_{te}$ is the effective technology coefficient and f is the product of 13 cost driver attributes of the Jensen model [16]. Then, Jensen effort is defined as

$$
J e n s e n E f f o r t = 0. 4 * \left(D S I / C _ {t e}\right) ^ {1. 2} * (D) ^ {0. 4},
$$

where, D is the difficulty = (est. effort/0.4)/(t\_d)^3. Table 2 shows the values of Jensen's cost driver product f for all 7 projects.

## Doty Effort

This is a static single-variable model where the resource development effort depends only on the count of delivered source instructions.

$$
\begin{array}{l} \text {Doty   effort = (5.29 / 12)(KDSI)} ^ {1. 0 6 7} \text {man - years,} \\ \text {where, KDSI = DSI / 1000.} \end{array}
$$

## IBM Effort

The simplest version of the IBM model relies solely on DSI to calculate the effort.

$$
\text { IBM   effort } = (5. 2 / 1 2) (\text { KDSI }) ^ {0. 9 1} \text {   man - years. }
$$

It should be noted that the Doty and IBM models are, in fact, the same model customized to different environments, by adjusting the values of the coefficient and exponent.

## 5. Results of the Case Study

Table 3 summarizes all the actual and estimated efforts. The sample correlations among these efforts are given in Table 4. Observe that the correlation between the actual effort and the SLIM effort is 0.9945 and that between the actual and the Jensen effort is 0.963. These correlations were substantially better than our expectations. Note that the correlations of actual effort with efforts derived by other models range from 0.73 to 0.825.

As expected, the correlation between the Doty and IBM models is very high; the correlation among all three modes of Intermediate COCOMO model is also very high. The Jensen model estimate is highly correlated with the SLIM model estimate, as the Jensen model is a combination of SLIM and COCOMO models. The correlation between the COCOMO and Jensen model estimates is lower than expected. Reading the last line of Table 4, it seems that the behavior of the COCOMO model is quite different from that of other models.

Table 3  
Actual and Estimated Efforts (Man-Years).

<table><tr><td>Proj. No.</td><td>COCOMO organic</td><td>COCOMO semi-detached</td><td>COCOMO embedded</td><td>SLIM</td><td>Jensen</td><td>Doty</td><td>IBM</td><td>Actual effort</td></tr><tr><td>1</td><td>13.65</td><td>17.76</td><td>24.02</td><td>8.167</td><td>15.80</td><td>47.28</td><td>23.37</td><td>10.0</td></tr><tr><td>2</td><td>30.98</td><td>40.14</td><td>54.22</td><td>27.42</td><td>56.12</td><td>61.63</td><td>29.29</td><td>26.61</td></tr><tr><td>3</td><td>11.62</td><td>14.23</td><td>18.05</td><td>6.305</td><td>10.62</td><td>26.88</td><td>14.44</td><td>7.4</td></tr><tr><td>4</td><td>31.24</td><td>39.97</td><td>53.17</td><td>9.521</td><td>10.32</td><td>43.70</td><td>21.85</td><td>11.25</td></tr><tr><td>5</td><td>48.93</td><td>64.16</td><td>87.72</td><td>34.26</td><td>72.75</td><td>62.77</td><td>29.76</td><td>29.86</td></tr><tr><td>6</td><td>38.70</td><td>48.47</td><td>62.92</td><td>14.57</td><td>32.76</td><td>32.56</td><td>17.00</td><td>13.83</td></tr><tr><td>7</td><td>11.11</td><td>13.60</td><td>17.23</td><td>11.34</td><td>10.82</td><td>26.29</td><td>14.16</td><td>12.78</td></tr></table>

Table 4  
Sample Correlations Among Effort Values.

<table><tr><td></td><td>ccm-org</td><td>ccm-sem</td><td>ccm-emb</td><td>SLIM</td><td>Jensen</td><td>Doty</td><td>IBM</td><td>Actual</td></tr><tr><td>ccm-org</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ccm-sem</td><td>0.9992</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ccm-emb</td><td>0.9967</td><td>0.9991</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SLIM</td><td>0.7677</td><td>0.7835</td><td>0.7998</td><td>1.0</td><td></td><td></td><td></td><td></td></tr><tr><td>Jensen</td><td>0.7914</td><td>0.8053</td><td>0.8195</td><td>0.9798</td><td>1.0</td><td></td><td></td><td></td></tr><tr><td>Doty</td><td>0.6210</td><td>0.6470</td><td>0.6739</td><td>0.7999</td><td>0.8005</td><td>1.0</td><td></td><td></td></tr><tr><td>IBM</td><td>0.6209</td><td>0.6469</td><td>0.6736</td><td>0.7920</td><td>0.7934</td><td>0.9999</td><td>1.0</td><td></td></tr><tr><td>Actual</td><td>0.7308</td><td>0.7479</td><td>0.7656</td><td>0.9945</td><td>0.9631</td><td>0.8252</td><td>0.8174</td><td>1.0</td></tr></table>

Next we performed a stepwise regression analysis with the actual effort as the dependent variable and various estimated efforts as independent variables. Although the model estimates entering the analysis are based on the same projects, this is quite appropriate, because each looks and analyzes different aspects of the software development process. As expected after seeing the correlations, the regression required only one step and the variable that entered the regression was the SLIM effort. The predicted effort equation is given by

Development effort = 3.08 + 0.808 \* SLIM effort.

The value of the F-ratio (Mean square of regression divided by mean square of error) was equal to 449.88 indicating the result to be significant at better than 99% significance level. That is, the probability of getting this result by chance is less than 1%.

Thus it appears from this sample that the two organizations are better off using the SLIM model estimates than using the estimates derived from the semidetached mode of the Intermediate COCOMO model.

To ascertain that the residual cost estimation data is normally distributed, we performed the Shapiro-Wilk normality test [7] on the residuals (actual effort - estimated effort by regression) and found that the approximate Shapiro-Wilk coefficient is 0.907, indicating that the probability of getting this or lower value is 0.35, which is quite high. So there is no evidence to indicate that the residuals are not normally distributed.

Jensen model estimates are also very close to the actual. In fact, if SLIM effort is not considered in the regression, then the predicted effort is given by

effort = 6.10 + 0.33 \* Jensen effort.

Finally, to test the methodology with respect to its prediction capabilities, we took out the largest (maximum DSI) of the seven projects (project number 5) and regressed the actual effort against estimated efforts for the remaining six. The regression equation was found to be:

$$
\text { effort } = 2. 3 8 + 0. 8 7 * \text {   SLIM   effort.   }
$$

Using this equation to determine the predicted effort for project number 5, we get

$$
\text { effort } = 2. 3 8 + 0. 8 7 * 3 4. 2 6 = 3 2 \text {   man - years. }
$$

This estimation is within 8.3% of the actual development effort for that project. The result is fairly impressive.

## 6. Recommendations

There are a number of resource models available today that can help software managers plan a new project by predicting the effort and schedule requirements over the duration of the project. Since these models consider different attributes of software as the dependent variables and produce a variety of outputs, it is difficult to choose a particular one for application in an individual environment. It is not uncommon to find software developers using a particular cost estimation model in their environment when statistics reveal that some other model may be more appropriate. This was indeed the case in our study involving seven software development projects from two organizations. The organizations were using the Intermediate COCOMO model in semidetached mode, whereas the statistics revealed that it would have been more appropriate for them to use the SLIM model. In our case, the statistical analysis suggested the use of one model for these organizations. It is quite possible that for different types of software products, the correct answer would be to use a combination of models rather than a particular one.

It is recommended that before choosing a software cost estimation model for analysis and/or prediction, software managers should perform some statistical experiments to ascertain the validity of using that model in their development environment. At the least, they must look at the inherent assumptions of individual models and match them against their development environments to justify their selection.

This study included well defined and well specified software systems. It remains to be seen whether this type of experimentation and prediction is valid for business, military, or other kinds of software.

## References

[1] T.K. Abdel-Hamid and S.E. Madnick: "On the portability of quantitative software estimation models", Information and Management, Aug 1987, 1–10.

[2] V.R. Basili: “Resource models”, in: Tutorial on models and metrics for software management and engineering – (ed.) V.R. Basili, IEEE Computer Society Press, 1980, 4–9.

[3] B.W. Boehm: "Software engineering economics", Prentice Hall, Inglewood Cliffs, N.J., 1981.

[4] B.W. Boehm: "Software Engineering Economics", IEEE Trans. on Software Engineering, Jan 1984, 4-21.

[5] R.E. Fairley: “Software engineering concepts”, McGraw Hill Book Company, 1985.

[6] F.R. Freiman and R.E. Park: "PRICE software model - Version 3: An overview", Proceedings of the workshop on Quantitative software models, 1979, 32-41.

[7] G.J. Hahn and S. Shapiro: "Statistical models in Engineering", John Wiley and Sons, 1967.

[8] R.W. Jensen: "An improved macrolevel software development resource estimation model", Proceedings of the 5th IPSA Conf., April 1983, 88–92.

[9] C.F. Kemerer: “An empirical validation of software cost estimation models”, Communications of the ACM, 1987, 416–429.

[10] S.N. Mohanty: “Software cost estimation: Present and future”, Software Practice and Experience, 1981, 103–121.

[11] F. Mosteller and R.E.K. Rourke: "Sturdy statistics", Addison Wesley, 1973.

[12] News in Perspective, Datamation, Sep. 1980, 124.

[13] R.S. Pressman: "Software engineering - A practitioner's approach", McGraw-Hill, Inc., New York, 1987.

[14] L.H. Putnam: "A general empirical solution to the macro software sizing and estimation problem", IEEE Trans. on Software Engineering, July 1978, 345–361.

[15] L.H. Putnam: “A very simple software cost estimating system”, Tech. Report, Quantitative Software Management, Inc., 1981.

[16] User's manual of SEER - Software development schedule and cost estimation system, Hughes Aircraft Company, 1983.

[17] J.M. Verner and G. Tate: "A model for software sizing", Journal of Systems and Software, 1987, 173–177.

[18] C. Walston and C. Felix: “A method of programming measurement and estimation”, IBM Systems J., 1977, 54–73.
