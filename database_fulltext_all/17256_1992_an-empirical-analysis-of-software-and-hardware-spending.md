---
otero_id: 17256
otero_key: "G5U5JBVF"
title: "An empirical analysis of software and hardware spending"
authors: "Vijay Gurbaxani; Haim Mendelson"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90033-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An empirical analysis of software and hardware spending

Vijay Gurbaxani \*

Graduate School of Management, University of California, Irvine, Irvine, CA 92717, USA

Haim Mendelson \*

Graduate School of Business, Stanford University, Stanford, CA 94305, USA

The growth in information systems budgets and in their primary components, hardware and software effort, are analyzed empirically. It is demonstrated that while a large component of the growth is due to technology related factors, these expenditures, and in particular, hardware spending, are sensitive to the growth rate of the economy and fluctuate around the technology-driven growth path due to general business conditions. The validity of the popular belief that software effort (including both software-development and maintenance) represents a growing proportion of information systems expenditures is tested versus the competing view that software effort and hardware expenditures consume relatively constant budget shares. It is shown that after controlling for macroeconomic effects, hardware and software expenditures grow exponentially at the same rate. The analysis also suggests that in the aggregate, it is primarily the hardware outlays that adjust in response to unexpected business conditions.

Keywords: Information systems spending, Budgets, Software spending, Hardware spending, Information systems costs, Demand for computing.

Vijay Gurbaxani is Associate Professor of Information Systems and Computer Science at the Graduate School of Management at the University of California, Irvine. His primary research interests are in the application of microeconomics to the study of managerial issues in the information systems context. A major focus of his research is the analysis of investment decisions in information technology and their impact on corporate information systems budgets. He is also studying the diffusion of information technology and its impact on organizations and markets. He is the author of the book, Managing Information Systems Costs, and has published articles in several journals including Communications of the ACM, Information Systems Research and the IEEE Transactions on Software Engineering. Dr. Gurbaxani received his M.S. and Ph.D. degrees from the William E. Simon School of Business Administration at the University of Rochester. He also holds an M.S. in Mathematics and Computer Science from the Indian Institute of Technology, Bombay.

\* We would like to thank the anonymous referees for their many constructive suggestions. Partial financial support by the IBM Program of Support for Education in the Management of Information Systems is gratefully acknowledged.

## 1. Introduction

Information systems (IS) spending has grown rapidly in the last two decades. As these expenditures continue to grow, it is increasingly important for both user organizations and the computer industry to develop an understanding of the factors that determine this growth. Due to the rapid pace of technological change and the relative youth of the field, the management of information systems is particularly difficult, and understanding the complexities of providing information services is not always straightforward. Since the pattern and rate of growth of IS budgets are directly related to the underlying techniques for the production of information services, the analysis of budget data can provide considerable insights into the nature of this process. These insights can assist IS managers in decision-making, budget justification and control. The trends in IS spending also have obvious importance for the software and hardware industries and for policy-makers and planners within industry and government who must evaluate the success of previous initiatives and the targets of future investments.

The importance of understanding the growth in IS spending is evidenced by the attention paid to this issue in the managerial literature. For many years, leading periodicals such as Datamation, EDP/IR and Computer Decisions have expended considerable resources to conduct and publish annual spending surveys. The trends governing the growth of IS budgets are also the subject of numerous studies in the academic MIS literature (see, for example, [1], [17], [18], [23], [25], [29], [30], [35]). Studies have focussed on the growth pattern of the overall budget as well as on its allocation to input factors. Given the scale of investments in information technology and its importance, one might expect that the behavior of IS budgets is well understood. In fact, there are considerable differences in opinion among IS professionals about the nature of growth of these expenditures.

![](/api/attachments/G5U5JBVF/fulltext/images/351febdf49ae90f5be6c0c0d53068876255c0cc163d61353dd9f7098ee5e26ad.jpg)  
Fig. 1. The S-shaped budget-proportion curve.

An important issue regarding IS budget trends is the behavior of the relative shares of software versus hardware expenditures. This issue has commanded significant attention (e.g., [2]–[5], [10], [13], [14], [17], Datamation, EDP/IR, Computer Decisions). The popular belief is that software effort, including both software-development and maintenance, represents an increasing proportion of IS expenditures – an assertion which is often depicted in the form of an S-shaped budget-proportion curve such as fig. 1. This curve demonstrates a significant increase in the software-development and maintenance portions of the IS budget over time, and a corresponding decline in the share of hardware. Fig. 1 is “probably the bestknown figure in computer literature of recent years" [31, p. 20]. $^{1}$

The prediction that software effort will consume an ever-increasing share of IS expenditures seems reasonable given the nature of the underlying cost trends (cf. Schaeffer [35], and has had considerable impact on the prevailing views of IS management. According to Boehm [8], “this relationship has done more than anything else to focus management attention and resources in improving the software process.” Indeed, this curve has been a major factor in the decision to launch the multimillion dollar U.S. Department of Defense Software Initiative [6], [11]. Given its importance, it is surprising that the prediction encapsulated by Fig. 1 (which is a hypothesis rather than an empirical statement) has never been subjected to rigorous statistical testing.

Frank [14] has challenged the validity of fig. 1, labeling it a “myth” and stating that, in fact, the budget shares of hardware and software have remained relatively constant over time. The resulting debate has attracted significant attention and has not been settled to date. While there have been a number of claims and counter-claims about the composition of IS budgets, the popular view has remained consistent with fig. 1 (cf. [9], [20], [35]). The issue is still open, however, since no studies to date have conducted a formal statistical analysis of the trends governing IS budget shares.

The implications of the two hypothesized patterns of software budget behavior are notably different. The shape of the budget-proportion curve reflects the degree to which IS managers have successfully contained software costs (in the aggregate), primarily through the substitution of hardware for software effort. A budget-proportion curve that is not steadily increasing over time would be consistent with the notion that significant progress has been accomplished by the industry, and that the substitution of hardware for software effort has been effective in reducing software outlays. In contrast, an S-shaped curve would imply that there are insufficient opportunities for such substitution (or that in spite of all its efforts, the industry has been unable to take advantage of such opportunities). The conclusion from the former case is that the industry is doing well and should continue along its current development path. Moreover, this result suggests that we should expect the continued balanced growth of both the hardware and software-development industries. The latter case leads to a more pessimistic assessment, both in terms of the industry's failure to realize gains from hardware-software substitution and in terms of the forecast it provides for the hardware industry: it implies that the growth in hardware sales will be hindered by the lack of progress in software-development technology.

Further, since industry norms are often used as benchmarks for evaluating the performance of IS managers, an understanding of the industry-wide budget trend is important. Consider, for example, an installation which exhibits an S-shaped budget-proportion curve such as fig. 1. If the aggregate budget trend is similarly shaped, the IS manager can justifiably argue that his or her performance is simply a reflection of the prevailing industry trends rather than managerial failure to contain software costs. If however, the industry benchmark is a flat budget-proportion curve, an installation characterized by an S-shaped curve should be carefully scrutinized to see if it is taking advantage of all available substitution opportunities. While specific circumstances could perhaps justify such behavior, a significant deviation from the industry norm should raise concerns that could result in corrective action. Similar comments apply to the sensitivity of IS spending to general business conditions: knowledge of the general trend provides a useful benchmark for evaluation and control.

A related issue which has received considerable attention in the literature is the pattern of growth of overall IS spending. Nolan [29], [30] argued that IS budgets grew according to an S-curve (or a series of S-curves). Lucas and Sutton [25] rejected this claim and demonstrated empirically, using data on counties in California, that the pattern of growth was more closely consistent with a linear or exponential model. More recently, Gurbaxani and Mendelson [18] have proposed an integrative model which suggests that the growth of IS budgets is influenced both by the effects of the diffusion of innovation and by the effects of the declining prices. This model predicts that the growth in overall IS spending can be modeled as a price-adjusted S-curve, where a constant-elasticity demand curve leading to an exponential growth pattern is shifted over time and the temporal shifts follow an S-curve. They find that the pattern of IS spending growth in the United States for the period 1960 to 1987 is well described by such a price-adjusted S-curve. Their analysis reveals that diffusion effects dominated spending growth in the initial years of computing, while current growth is more nearly consistent with an exponential model.

The two models have considerably different predictions of the nature of maturity in the IS environment. The Nolan predictions $[29]$ , $[30]$ , consistent with the traditional diffusion models, suggest that maturity will be characterized by virtually no growth in IS spending, with new demand being primarily due to replacement. On the other hand, an exponential model predicts a steady annual rate of growth, where the decreasing costs fuel demand as it becomes increasingly cost effective to automate an ever increasing number of tasks. Clearly, these predictions have very different implications for the planning decisions of users and vendors.

The aim of this paper is to develop an understanding of the nature of the provision of information services through an empirical analysis of IS spending data. Spending patterns reflect the choice of techniques for the production of information services. It is therefore useful to determine budget trends and to analyze the relationships between IS spending decisions and the underlying factors that drive the spending growth process. We focus on the influence of price on the pattern and rate of growth of the overall budget and its major components, hardware and software effort. We also analyze how the level of expenditures in information technology is affected by general business conditions.

This paper builds in part on the theoretical models developed in Gurbaxani and Mendelson [17] and on the empirical analysis in Gurbaxani and Mendelson [18]. Gurbaxani and Mendelson [18] estimated the behavioral pattern of aggregate IS expenditures. Gurbaxani and Mendelson [17] demonstrated theoretically that under certain assumptions about the characteristics of the production function for information services, the optimal allocation of IS budgets would result in constant budget shares of these two inputs and provided some preliminary supporting evidence. Drawing on these results, the current analysis determines the pattern of growth of IS expenditures and provides a rigorous empirical examination of the factor shares of hardware and software effort. We explicitly test the hypothesis that (after controlling for macroeconomic effects) the budget shares of hardware and software-development remain constant over time. This represents (to our knowledge) the first time that this hypothesis will have been formally tested.

We find that the empirical procedure is not as straightforward as one might initially expect. First, the test procedure must explicitly allow for the possibility of dependence between the software and hardware expenditures. Moreover, the analysis must also take into account the impact of general business conditions on information technology investments. The observation that many types of capital investment are positively correlated with the growth rate of the economy suggests that macroeconomic factors must be controlled for. In particular, it is likely that investments in hardware, which are capital investments, are more sensitive to general economic conditions than software spending, which is usually expensed. Given our focus on the relative growth rates of hardware and software spending, it is important to determine the relationship between macroeconomic factors and investments in hardware and software effort and incorporate it in the analysis.

The empirical analysis of IS budgets presented in this paper consists of (i) studying the time-series behavior of IS expenditures for the period 1976–1984, and (ii) analyzing the allocation of these expenditures to hardware and software effort. In what follows, section 2 presents our data sources and provides a preliminary analysis of the data. A more detailed analysis including tests of the robustness of our results is in section 3. Our concluding remarks are in section 4. The appendix provides the details of the econometric techniques applied in the estimations.

## 2. Data and preliminary analysis

The importance of IS budgets has resulted in several efforts to collect IS user spending data. However, only a few of these efforts provide consistent time-series data which enable the analysis of budget trends, and even fewer provide data on the allocation of IS expenditures between budget components. The most consistent source of IS budget data is the International Data Corporation (IDC), a respected source of statistics on the computer industry. $^{2}$ IDC maintains an online database that records information on a large number of installations, which represent over 80 percent of the general purpose computers in the United States. This database provides them with an unparalleled ability to monitor computing trends in user organizations. In fact, the Bureau of Economic Analysis uses IDC data in computing its annual dataset on industry capital investment. IDC publishes an annual report on IS spending in the United States in a publication called Electronic Data Processing / Industry Report. $^{3}$ The data analyzed in this study are therefore based on this source.

IDC has conducted an annual IS budget survey of user organizations in the United States for several years. The number of organizations surveyed in any year ranges between 125 and 350.

All sectors of the economy are included in the sample. $^{4}$ The user organizations surveyed are carefully selected so as to be a statistically representative sample of the total user population. The questionnaire used in the survey asks IS executives to report actual expenses for the previous and current years and estimated spending in the subsequent year. Survey respondents are asked to provide spending data by line-item or by major spending categories if the more detailed information is unavailable. The expenditure categories include systems hardware, data entry and data communications equipment, software, services, communications line charges, personnel, supplies, and overhead expenses. $^{5}$ IDC provides definitions of each line item to ensure consistency in the reporting across the set of user organizations. In addition, IDC attempts to ensure the consistency of their results between years. IDC also cross-checks the results of the budget surveys with those of other IDC studies. It should be noted though, that IDC sometimes revises its estimates as more accurate data become available, reflecting some of the difficulty in compiling such a dataset. The results are published as annual aggregate expenditures for the set of user organizations in the United States. A secondary source is Phister [34], which includes the most comprehensive collection of statistics on the IS industry. This book has been compiled from a variety of sources, including a significant contribution from the IDC data.

We used as much of the IDC data as possible, using Phister's [34] data for verification purposes. The longest period of time for which the available data categories are comparable between years is 1976–1984. Prior to 1976, IDC used several different categorizations of expenses, reflecting perhaps the rapid changes in computer technology. Since 1984, IDC has reduced the scope of its survey and now only reports the budget shares of the various categories. Therefore, our analysis examines the annual data for the nine year period from 1976 to 1984.

The empirical analysis performed on this data consists of studying the composition of IS budgets and their time-series behavior, and testing the hypothesis of constant budget shares over time. The hardware cost category (H) is taken to include expenditures on systems hardware, data entry and data communications. The software effort category (S) is computed as the sum of the costs of outside software and services and software personnel costs, capturing both software-development and maintenance. While IDC does not indicate the percentage of personnel costs attributable to software, Frank [14] estimated this percentage as having been constant at around 50 percent. This is also borne out by IDC's data and is consistent with Phister's [34] annual estimates, which indicate that software personnel costs as a percentage of total personnel costs average 50.34 percent. Thus, we compute software personnel costs as one-half of the total personnel cost. All dollar figures have been divided by the GNP implicit price deflator for the corresponding years, yielding real (inflation-adjusted) budget data. All spending figures are quoted in 1972 dollars.

Table 1 presents summary statistics for the variables studied. As can be seen from the table, when the sum of hardware and software expenses is considered, hardware consumes on average around 57 percent of the budget and the rest is consumed by software expenditures. It is also seen that hardware expenses have consumed on average

Table 1  
Summary statistics for the budget data.

<table><tr><td colspan="2">Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>S</td><td>Software (in thousands of 1972 dollars)</td><td>9254</td><td>1974</td></tr><tr><td>H</td><td>Hardware (in thousands of 1972 dollars)</td><td>12226</td><td>2789</td></tr><tr><td>B</td><td>Total Budget (in thousands of 1972 dollars)</td><td>32320</td><td>6754</td></tr><tr><td> $S/(S + H)$ </td><td></td><td>0.43</td><td>0.015</td></tr><tr><td> $H/(S + H)$ </td><td></td><td>0.57</td><td>0.015</td></tr><tr><td> $S/B$ </td><td></td><td>0.29</td><td>0.0036</td></tr><tr><td> $H/B$ </td><td></td><td>0.38</td><td>0.0187</td></tr></table>

38 percent of the total budget, and software expenses account on average for 29 percent of the total budget.

An examination of the data indicates that both software and hardware expenses have grown rapidly. Software expenses grew from 6.8 billion deflated dollars $^{6}$ in 1976 to 12.5 billion deflated dollars in 1984. Hardware expenses increased from 9.4 billion deflated dollars in 1976 to 17.8 billion in 1984. The mean share of software in the sum of software and hardware expenses is 43 percent and its standard deviation is 0.015. The mean share of software effort in the total IS budget is 29 percent and its standard deviation is 0.0036, while the mean hardware budget share is 38 percent with a standard deviation of 0.0187. The small variation around the means indicates the relative constancy of the budget shares of these two inputs. Note that the standard deviation of the hardware budget share is roughly five times larger than that of software. This point is addressed later.

We now study the behavior of IS budgets and their components over time. Since budget patterns are an outcome of the underlying demand for information services, we begin by examining the factors that are likely to affect this demand from both the theoretical and empirical perspectives. The quantity of information services demanded is determined by balancing their benefits against their costs. The trends related to the demand side were studied by Gurbaxani and Mendelson [18], and those pertaining to the cost side are presented in Mendelson [28]. On the demand side, it was found that the growth of information technology can be classified into two periods: a transient learning phase followed by a steady-state or mature growth phase. The steady-state period is also characterized by significant growth, which is driven primarily by the cost trends. Further, our findings [18] show that our sample period is substantially within the steady-state growth period.

Information technology cost trends have been examined in detail by Mendelson [28]. In the case of hardware, Mendelson [28] concludes that hardware costs (per unit of performance) decline exponentially over time. For example, the cost of computing power (in real dollars per MIPS) declines by 20 percent per year in real terms. The exponential decline is evidenced by almost perfect correlations between the logarithm of the real cost per unit of performance and time. Thus, time may serve as a proxy for the logarithm of price. In contrast to the case of hardware, software-development costs have declined much more slowly. Some studies have estimated an exponential decline at annual rates of 3 to 5 percent while yet others suggest that these costs perhaps did not decline at all (see [28], [34]).

An important determinant of the growth rates of software and hardware spending is the degree of substitution between these two inputs. When hardware can be substituted for software-development effort, the increased use of cheaper hardware also lowers the costs of software-development, resulting in an increase in the demand for both software and hardware. Clearly, higher degrees of substitution will result in greater increases in the demand for information services. To demonstrate how such substitution between hardware and software-development effort can take place under the prevailing cost trends, we present a simple example. Let the value of information services at time t be represented by the Cobb–Douglas function, $W(s_{t}, h_{t}) = A s_{t}^{\alpha} h_{t}^{\beta}$ , where $s_{t}$ and $h_{t}$ are the quantities of hardware and software inputs in period t, and let the per-unit costs of hardware and software-development in period t be $c_{ht}$ and $c_{st}$ respectively. Assume that the costs of hardware and software-development decline exponentially over time, i.e., $c_{ht} = c_{h0} \cdot \lambda_{h}^{t}$ and $c_{st} = c_{s0} \cdot \lambda_{s}^{t}$ , with the hardware costs declining faster than the software-development costs: $\lambda_{h} < \lambda_{s}$ (the case $\lambda_{s} = 1$ corresponds to no decline in software-development costs). $^{7}$

The firm's optimization problem in period $t$ is then

$$
\underset {s _ {t}, h _ {t}} {\operatorname{Max}} \left\{W (s _ {t}, h _ {t}) - c _ {s t} \cdot s _ {t} - c _ {h t} \cdot h _ {t} \right\}\tag{1}
$$

with the first-order conditions

$$
\alpha \cdot W = s _ {t} \cdot c _ {s t} \quad \text { and }\tag{2}
$$

$$
\beta \cdot W = h _ {t} \cdot c _ {h t}.\tag{3}
$$

By taking the ratio of equations (2) and (3), we obtain that the ratio of total spending on hardware, $h_{t} \cdot c_{ht}$ , to software-development spending, $s_{t} \cdot c_{st}$ is a time-independent constant: despite the faster decline in the unit cost of hardware, $c_{ht}$ , the quantity of hardware $h_{t}$ increases to make up for the price decline, resulting in a constant ratio of hardware to software-development spending.

![](/api/attachments/G5U5JBVF/fulltext/images/9210a99b24ae44eabcc60cd0d86f2285adf95d758a964188a7377accf10ee2bd.jpg)  
Fig. 2. The effects of hardware-software substitution.

To see how this effect obtains in more concrete terms, consider the following numerical example. We consider ten years over which hardware costs decline by 20 percent a year (i.e., $\lambda_h = 0.8$ ) and software costs remain constant ( $\lambda_s = 1$ ), $^8$ and assume $c_{h0} = 1$ , $c_{s0} = 1$ , $A = 1$ , $\alpha = 0.3$ and $\beta = 0.4$ . Solving (2)-(3), we obtain $s_t = 0.0265 \cdot 1.3465^t$ with $h_t = 1.33 \cdot 1.25^t \cdot s_t$ . Note that the quantities of hardware and software as well as the spending on both increase exponentially over time. This is a general result for the Cobb-Douglas production function and exponential costs. Fig. 2 shows the behavior of the ratio of software to hardware input quantities, $s_t / h_t$ , and the corresponding budget ratio, $(c_{st} \cdot s_t) / (c_{ht} \cdot h_t)$ . While the budget-proportion curve is flat at $0.75 (= \alpha / \beta)$ , the ratio $s_t / h_t$ declines over time, showing the effects of hardware-software substitution.

The example demonstrates that when hardware is substitutable for software effort, the optimal strategy for the production of information services is to take advantage of the rapidly decreasing costs of hardware by making the IS environment progressively more hardware intensive. This is manifested in the behavior of the ratio of software to hardware input quantities, $s_{t}/h_{t}$ . In general, the optimal values of the ratio of hardware to software and the implied budget shares depend on the degree of substitution between the two inputs. In the example above, the optimal quantity ratio adjusts at a rate that results in the budget shares of hardware and software effort being constant over time. Moreover, while the quantity ratio shifts in favor of hardware, the decreasing hardware costs also result in an increase in the demand for software. In fact, in response to the cost trends, the quantities of software and hardware as well as their respective budgets both increase exponentially.

We distinguish between two sets of factors that influence IS spending, technology-driven factors and macroeconomic factors (general business conditions). We call the pattern of growth in IS spending due to information technology factors alone (excluding the macroeconomic factors) the technology-driven growth path. Of course, IS spending is also driven by the economy as a whole: when the economy is growing, the growth rate of IS investments is likely to be higher than when the economy is slowing. Indeed, most forms of capital spending are highly correlated with the growth rate of the economy, suggesting that hardware investments in particular are affected by changes in general business conditions. A measure of the state of the economy should therefore also be incorporated in the analysis. One widely used measure of the business cycle is the growth rate of the GNP, and we incorporate this variable in our estimations.

We hypothesize that the technology-driven pattern of growth of IS budgets and its components is exponential. $^{9}$ Moreover, IS investments are also affected by general business conditions, implying that the observed values of IS budgets and their components will fluctuate around the technology-driven growth path in a manner that depends on the business cycle, as measured by the growth rate of GNP. The resulting regression models for the four categories of IS spending, software expenses, hardware expenses, the sum of software and hardware expenses, and the total IS budget are given by

$$
\log (S _ {T}) = \alpha_ {s} + \beta_ {s} \cdot T + \psi_ {s} \cdot G + \epsilon_ {s T},
$$

$$
T = 1, 2, \dots , N,\tag{4}
$$

$$
\log \left(H _ {T}\right) = \alpha_ {h} + \beta_ {h} \cdot T + \psi_ {h} \cdot G + \epsilon_ {h T},
$$

$$
T = 1, 2, \dots , N,\tag{5}
$$

$$
\log (S \& H _ {T}) = \alpha_ {s h} + \beta_ {s h} \cdot T + \psi_ {s h} \cdot G + \epsilon_ {s h T},
$$

$$
T = 1, 2, \dots , N,\tag{6}
$$

$$
\log (B _ {T}) = \alpha_ {b} + \beta_ {b} \cdot T + \psi_ {b} \cdot G + \epsilon_ {b T},
$$

$$
T = 1, 2, \dots , N,\tag{7}
$$

where $S_{T}$ , $H_{T}$ , $S\&H_{T}$ , and $B_{T}$ are the software, hardware, sum of software and hardware, and the total budgets respectively in period T. The net effect of the technology related factors on the growth rates of IS budgets and their component categories is captured by the coefficients of the time variable, $\alpha_{s}$ , $\beta_{s}$ , $\alpha_{h}$ , $\beta_{h}$ , $\alpha_{sh}$ , $\beta_{sh}$ , $\alpha_{b}$ and $\beta_{b}$ , in the four equations above. The variable G is the growth rate of the GNP, and its effect is measured by the coefficients $\psi_{s}$ , $\psi_{h}$ , $\psi_{sh}$ and $\psi_{b}$ , and the $\epsilon$ 's are the error terms.

Before proceeding with our results, it is useful to examine the limitations of our analysis due to the length of the time-series. Given our small sample size, we cannot appeal to the central limit theorem (implying asymptotic normality) in our statistical tests. Rather, we employ the standard tests for small samples that apply when the error terms are normally distributed. To justify this procedure, we tested whether the error terms that result from our regression equations are normally distributed. We employ the Kolmogorov–Smirnov test (see [33]) to test the above hypothesis. The test statistic, D, is defined as the greatest absolute difference between the hypothesized cumulative density function and the sample cumulative density function. We calculated the test statistic D for the error terms in each of equations (4)–(7). Its value was 0.14 for the software equation, 0.11 in the hardware equation, 0.15 in the software and hardware budget equation and 0.14 in the total budget equation. The critical value of the statistic for our case at the 95 percent level is 0.27. Thus, we do not reject the null hypothesis that the error terms are normally distributed. In fact, we cannot reject the hypothesis even at the 80 percent level. This result allows the use of the test procedures employed in our analysis.

The results of the regressions are summarized in table 2. The fit is of consistently high quality as can be seen from the $R^{2}$ terms. To account for the number of degrees of freedom, table 2 also presents the adjusted $R^{2}$ values, which substantially exceed 99 percent. In all cases, the coefficients of the time variable and the constant term are statistically significant at the 99 percent level. In general, the growth patterns of the IS budget and its components are consistent with the exponential growth hypothesis. $^{10}$ The estimates of the coefficient of time in the regressions for software and hardware are 0.0777 for software and 0.0775 for hardware, corresponding to an annual budget increase of 8.08 percent for software and 8.06 percent for hardware. The coefficient of the growth rate of GNP is statistically different from zero in all cases other than the software regression.

In all four cases, the hypothesis of positive first-order serial correlation between the residuals can be rejected at the 1 percent level of significance, consistent with the assumed independence between years of both hardware and software investments. When G is excluded as an independent variable, the analogous estimations reveal the existence of first-order serial correlation in all cases except the software regression. Thus, in the aggregate the only detectable serial correlation is that due to the GNP growth variable; once GNP is included as an explanatory variable in the estimations, these autocorrelations vanish.

Table 2  
Summary of trend regressions (t-statistics in parentheses)

<table><tr><td>Dependent variable</td><td>Constant coefficient</td><td>Time coefficient</td><td>GNP growth rate coefficient</td><td> $R^2$ </td><td>Adjusted  $R^2$ </td><td>SSR</td><td>SEE</td><td>D-W</td></tr><tr><td>(4) log(S)</td><td>8.717 **(791.71)</td><td>0.0777 **(47.04)</td><td>0.255(1.64)</td><td>0.997</td><td>0.996</td><td>0.00094</td><td>0.012</td><td>1.09</td></tr><tr><td>(5) log(H)</td><td>8.947 **(234.85)</td><td>0.0775 **(13.57)</td><td>1.88 *(3.52)</td><td>0.969</td><td>0.958</td><td>0.011</td><td>0.043</td><td>2.16</td></tr><tr><td>(6) log(S&amp;H)</td><td>9.53 **(410.60)</td><td>0.0776 **(22.30)</td><td>1.18 *(3.62)</td><td>0.988</td><td>0.984</td><td>0.004</td><td>0.026</td><td>1.91</td></tr><tr><td>(7) log(B)</td><td>9.971 **(807.21)</td><td>0.0755 **(40.79)</td><td>0.530 *(3.05)</td><td>0.996</td><td>0.995</td><td>0.001</td><td>0.014</td><td>1.08</td></tr></table>

\*\* Significant at the 99 percent level.  
\* Significant at the 95 percent level.  
N = 9.

The results of the regression analysis confirm that investments in information technology are sensitive to overall business conditions. Interestingly, as depicted by the magnitude and significance of the coefficient of G, the hardware component of the budget is much more responsive to economy-wide changes than is the software budget. Since hardware purchases are usually accounted for as a capital investment, this result is consistent with the observed positive correlation between most forms of capital spending and the rate of growth of the economy. Software costs, on the other hand, are accounted for mainly by personnel and are therefore difficult to adjust in the short term in response to changing business conditions. The observed pattern of spending suggests that while the growth rate of investments in information technology fluctuates with general business conditions, it is primarily the hardware component of the budget that is adjusted in response to economy-wide changes.

Our results show that IS budget growth is affected both by information technology related factors, such as prices and technological development, and by macroeconomic factors represented by the GNP growth rate. Theories from the IS area typically predict the pattern of growth due to IS-related factors, which we have called the technology-driven growth path. This pattern is modified, however, by economy-wide fluctuations, measured by the rate of growth of GNP. The regression results indicate that the rate of growth of IS expenditures is positively correlated with the growth rate of GNP. This result indicates that the allocation of IS expenditures to hardware and software should be interpreted in light of this trend. Next, we examine the hypothesis of constant budget shares taking this factor into account.

## 3. The constancy of budget shares

The trends in the factor shares of hardware and software in information systems spending are key indicators of the nature of the production of information services. A continuously increasing share of software effort in the information systems budget over time is consistent with the notion that the production of information services is becoming increasingly labor-intensive, with software development being a bottleneck that severely constrains its growth. On the other hand, the constancy of the factor shares of hardware and software effort would support the notion that the two are substitutable input factors, implying that information systems managers have successfully held down software costs through the effective use of additional hardware. In this section, we formally test which of these two alternatives prevails. Specifically, we test whether the ratio of software expenditures to hardware expenditures remains constant over time after accounting for the macroeconomic effects. While the closeness in the magnitude of the coefficients of the time variable in the hardware and software estimations of the previous section seems to support the constancy of budget shares, this analysis has ignored the dependence between software and hardware expenditures.

We reconsider the two regression equations

$$
\begin{array}{c} \log (S _ {T}) = \alpha_ {s} + \beta_ {s} \cdot T + \psi_ {s} \cdot G + \epsilon_ {s T}, \\ T = 1, 2, \dots , N, \end{array}\tag{4}
$$

$$
\log (H _ {T}) = \alpha_ {h} + \beta_ {h} \cdot T + \psi_ {h} \cdot G + \epsilon_ {h T},
$$

$$
T = 1, 2, \dots , N.\tag{5}
$$

The null hypothesis of identical technology-driven growth rates can be stated as

$$
H _ {0} \colon \beta_ {s} = \beta_ {h},\tag{8}
$$

and the alternative hypothesis is

$$
H _ {a} \colon \beta_ {s} \neq \beta_ {h}.\tag{9}
$$

In principle, we could use the simple regression estimates of section 2 to test whether $\beta_{s} = \beta_{h}$ . Using these estimates, $\hat{\beta}_{s} = 0.0777$ with a standard error of 0.0017, whereas $\hat{\beta}_{h} = 0.0775$ with a standard error of 0.0057. Viewing (4) and (5) as being drawn from two independent samples, we cannot reject $H_{0}$ : $\beta_{s} = \beta_{h}$ since the two estimates are within two standard errors of one another. This test procedure assumes, however, that the error terms from the two budget equations, $\epsilon_{sT}$ and $\epsilon_{hT}$ , are independent, whereas it stands to reason that there is strong dependence between the software and hardware budgets in any given year. This is because systems implementation typically involves joint software and hardware expenditures, hardware acquisition decisions directly affect software decisions and vice versa, $^{11}$ and firm-specific conditions affect both budget components. This gives rise to dependence between the budget residuals of (4) and (5), which must be accounted for in the model specification. Further analysis is therefore necessary to test the hypothesis that the budget shares of hardware and software, adjusted for the business cycle, are indeed constant over time. A more realistic model, then, would postulate (4)-(5) with

$$
E \left[ \epsilon_ {s T} \cdot \epsilon_ {h T} \right] = [ \Omega ] = \left[ \begin{array}{c c} \sigma_ {s s} & \sigma_ {s h} \\ \sigma_ {s h} & \sigma_ {h h} \end{array} \right],\tag{10}
$$

where $[\Omega]$ is a general $2 \times 2$ variance-covariance matrix between software and hardware expenditures. $^{12}$

We applied Zellner's [36] Seemingly Unrelated Regression (SUR) model to estimate equation (10) as follows (see appendix A for details). First, the individual time-series regressions (4) and (5) are estimated, as before. The resulting variance-covariance matrix of the residuals is used as an estimate of the variance-covariance matrix $\Omega$ . Using this matrix, we run the two regressions together using Generalized Least Squares (which is appropriate when the error terms are not independent), and then test the hypothesis of equal budget shares using the Chi-square statistic $\lambda$ discussed in appendix A.

The use of the SUR model achieves two objectives. First, the Ordinary Least Squares (OLS) estimates of the variances are biased due to the violation of the assumption of independence between the budget-component residuals in any given year. As a result, the hypothesis of constant technology-driven budget shares cannot be properly tested using OLS. Second, the correlations between the residuals provide more information which adds statistical power to the model. Thus, the SUR method improves the specification and allows us to better estimate the variances and associated test-statistics, since pooling the two equations increases the informativeness and effective size of the data-set.

Following this approach, we obtained the SUR equations

$$
\begin{array}{r l} \log (S _ {T}) & = 8. 7 1 7 + 0. 0 7 7 7 \cdot T + 0. 2 5 5 \cdot G, \\ & \quad (9 6 9. 6 5) (5 7. 6 2) \quad (2. 0 2) \\ R ^ {2} & = 0. 9 9 7, D - W = 1. 0 9 \text { and } \end{array}\tag{4a}
$$

$$
\begin{array}{c} \log (H _ {T}) = 8. 9 4 7 + 0 0 7 7 5 \cdot T + 1. 8 8 \cdot G, \\ (2 8 7. 6 3) (1 6. 6 2) (4. 3 1) \\ R ^ {2} = 0. 9 6 9, D - W = 2. 1 6. \end{array}\tag{5a}
$$

The SUR procedure leads to the same point estimates for the coefficients as OLS since the explanatory variables in both regression equations are the same (cf. [22]). However, the variance estimates and t-statistics – which are crucial to our test – are quite different. Specifically, the SUR procedure increases the resulting t-statistics. In the case of software, the t-value for the time variable is now 57.62 compared to 47.04 before, while the corresponding statistic for hardware is 16.62 compared to 13.57 before.

To test the hypothesis of constant technology-driven budget shares, we impose the additional constraint $\beta_{s} = \beta_{h}$ , which equates the coefficients of the two time variables. In the standard case, an F-test would be performed on the residual variances of the restricted and unrestricted regressions. The dependence between the residuals of the hardware and software variables in the same year calls for a more sophisticated test procedure which is described in appendix A. Under the null hypothesis that $\beta_{s} = \beta_{h}$ , the resulting test statistic $\lambda$ defined by equation (A-9) follows a $\chi^{2}$ distribution with one degree of freedom. In the case at hand, the test-statistic $\lambda$ equals 0.0015, implying that the null hypothesis $H_{0}$ of identical coefficients, $\beta_{s}$ and $\beta_{h}$ , cannot be rejected at any reasonable level of significance. This result demonstrates that the theoretical assertion of constant technology-driven budget shares is indeed supported by the empirical evidence.

We now re-estimate models (4a) and (5a) under the restriction $\beta_{s}=\beta_{h}$ . The resulting (restricted) SUR equations are

$$
\log (S _ {T}) = 8. 7 1 7 + 0. 0 7 7 7 \cdot T + 0. 2 5 5 \cdot G,
$$

$$
R ^ {2} = 0. 9 9 7, D - W = 1. 0 9 \text { and }\tag{4b}
$$

$$
\log \left(H _ {T}\right) = 8. 9 4 7 + 0. 0 7 7 7 \cdot T + 1. 8 9 \cdot G,
$$

$$
R ^ {2} = 0. 9 6 9, D - W = 2. 1 6.\tag{5b}
$$

In the restricted case, $\hat{\beta}_{h}$ has increased in value slightly to 0.0777 while the other coefficients are basically unchanged.

We also examined the variance-covariance matrix $\Omega$ which demonstrates the mutual dependence of the software and hardware expenditures as well as the magnitudes of the residual variances. The estimate of $\Omega$ produced by our final SUR model (4b)-(5b) was

$$
\Omega = 1 0 ^ {- 3} \cdot \left[ \begin{array}{l l} 0. 1 0 5 & 0. 1 0 2 \\ 0. 1 0 2 & 1. 2 5 9 \end{array} \right]
$$

with a correlation coefficient of 0.281 between the software and hardware residuals. The residual variance of the hardware budget is more than 10 times higher than that of the software budget – a pattern which is disguised by the raw variances in table 1. This demonstrates that IS budgets may be adjusted in response to unexpected business conditions primarily through their hardware components, whereas the long-term trend is such that both components move together.

This phenomenon is consistent with the nature of the IS environment. While software investments are usually accompanied by corresponding investments in hardware, it is often easier to react to unexpected changes through adjustments to the hardware budget for several reasons. First, a large component of software expenses is personnel costs, which cannot be adjusted easily in the short term. Additionally, the software budget can require an extensive planning stage and long periods of development time, all of which contribute to its relative inflexibility. Further, a significant proportion of this resource is consumed by maintenance tasks that can be crucial to the ongoing operations of the enterprise. On the other hand, it is significantly easier and quicker to adjust the level of investment in hardware. For example, hardware purchases can be delayed more easily in the event of a sudden budget shortfall. $^{13}$ All of this implies that hardware expenditures will display greater variations in the short run, while in the long run, it would be expected that both investments move together.

Our results on the constancy of the technology-driven budget shares have used an exponential model of growth, following the theoretical derivation in Gurbaxani and Mendelson [17] and the empirical results in Gurbaxani and Mendelson [18] which show that in recent years, most of the growth in IS budgets is due to the price effect. Given the exponential growth in the magnitude of both budget components, the hypothesis of the constancy of the technology-driven budget shares is equivalent to a hypothesis of equal coefficients of the logarithm of the time variable after controlling for the economy-wide effects. Next, we examine a more robust form of our test, which does not assume exponential growth.

Consider the variable $LRATIO_{t}=\log(H_{t}/S_{t})$ , which is defined as the logarithm of the ratio of the hardware budget to the software budget. The technology-driven values of $LRATIO_{t}$ are obtained by regressing it on the GNP growth rate, $G_{t}$ , and taking the residuals, $\epsilon_{t}$ , from the estimation equation

$$
L R A T I O _ {t} = \alpha_ {t} + \beta_ {t} \cdot G _ {t} + \epsilon_ {t}.\tag{11}
$$

If the technology-driven values of the budget shares are constant after controlling for economy-wide effects, then $\epsilon_{t}$ will be independent of time, t. On the other hand, if there is a time pattern in the budget ratio, then $\epsilon_{t}$ will be some function of t. We thus analyzed the residuals from the regression equation (11) to examine the existence of such time patterns. Testing for randomness of the residuals enables us to examine the constancy of the technology-driven budget shares without requiring the assumption of exponential budget growth.

Estimating equation (11), we obtained

$$
\begin{array}{r l} L R A T I O & = 0. 2 3 + 1. 6 3 \cdot G, \\ & (1 2. 4) \quad (3. 5 0) \\ R ^ {2} & = 0. 6 3 6, D - W = 2. 4 1 \end{array}\tag{12}
$$

with the residuals from (12) shown in fig. 3. As one would expect, the coefficient of G is positive, reflecting the fact that the hardware component of the budget is more responsive than the software component to GNP growth: larger GNP growth rates result in larger hardware spending without a corresponding increase in software outlays. Similarly, lower growth rates of the GNP are associated with lower values of the budget ratio. The Durbin–Watson statistic is 2.41, consistent with no first-order correlation among the residuals. While this result suggests that the residuals in adjacent periods are independent, further analysis is necessary to investigate the possibility of time dependence among the residuals from the above regression.

Fig. 3 presents a graphical depiction of the residuals plotted against time. A visual examination reveals that there is no apparent time pattern in the residuals. We confirm this observation through the use of a Runs Test [33], which tests for the randomness of a set of observations. This test involves counting the number of “runs” of like values (those that are either above or below the median of the set of observations). In this case, there are seven runs in the sequence of observations. The lower and upper values of the run statistic at the 5 percent level of significance are 3 and 9. Thus, we cannot reject the hypothesis that the process which generates the residual sequence is a random process.

To further confirm our findings, we also ran regressions of the residuals (RES) against time (T), the square of time (T2), and the two variables together. The resulting equations were

![](/api/attachments/G5U5JBVF/fulltext/images/a9d6f651411611c80e42bc553e8b86c4d964e7ad46197a60e69e2efd8c616553.jpg)  
Fig. 3. A plot of the residuals from equation 12.

$$
\begin{array}{r l} & R E S = 0. 0 0 0 8 - 0. 0 0 0 1 6 \cdot T, \\ & (0. 0 2 9) (- 0 0 3 2) \\ & R ^ {2} = 0. 0 0 0 1 5, D - W = 2. 4 1, \end{array}\tag{13}
$$

$$
\begin{array}{r l} R E S & = - 0. 0 0 2 8 + 0. 0 0 0 0 0 9 \cdot T 2, \\ & (- 0. 0 1 4) \quad (0. 1 8) \end{array}
$$

$$
R ^ {2} = 0. 0 0 4, D - W = 2. 4 2 \text { and }\tag{14}
$$

$$
\begin{array}{c} R E S = 0. 0 3 9 9 - 0. 0 2 1 5 \cdot T + 0. 0 2 1 \cdot T 2, \\ (0. 8 0 9) (- 0. 9 4 8) (0. 9 6 5) \\ R ^ {2} = 0. 1 3, D - W = 2. 7 5. \end{array}\tag{15}
$$

In all three cases, the $R^{2}$ of these regressions was very low, and the coefficient of the time variables was statistically equal to zero, consistent with the absence of a time pattern in the residuals.

We have shown that there is no apparent pattern of time-dependence in the residuals obtained from regressing the logarithm of the ratio of the hardware budget to the software budget on the growth rate of the GNP. Since this procedure is not contingent on the assumption of an exponential growth pattern, these results strengthen our finding that the budget shares do not follow any detectable trend.

The analysis in this section has revealed some interesting insights into the nature of the IS activity in organizations. It demonstrated that managers exploit the decreasing costs of hardware to reduce the software' effort through substitution. It also showed that the variance of the hardware budget is significantly higher than that of software expenditures, as can be expected from the nature of the two inputs. Most importantly, the analysis showed that the dominant underlying trend is for hardware and software expenditures to grow together over time at the same rate.

## 4. Concluding remarks

Budgets are a powerful management tool both as the quantitative expression of a plan and as a mechanism for controlling its execution. In the IS context, the rapid advances in the technology and the relative newness of the field have significantly increased the complexity of the management process, making an understanding of the underlying factors that drive these budgets important. This importance is underscored by the attention paid to budgets in textbooks for professional managers [35] and entire books on the subject [32]. These authors argue that every IS manager must be aware of the prevailing trends so as to be able to evaluate the cost-effectiveness of alternative methods and to allocate their resources effectively. More so than in many other fields, IS managers are in need of norms to assist them in decision-making, budget justification and control.

This research has utilized an econometric analysis of secondary data to provide a variety of insights into the nature of investments in information technology. $^{14}$ First, the results confirm that the recent growth of IS expenditures is well described by an exponential model, consistent with the results of Lucas and Sutton [25] and Gurbaxani and Mendelson [18]. Second, the results also demonstrate that the technology-driven rates of growth of both the hardware and software components of the budget are attributable to the declining costs of computing and are equal. Moreover, information technology investments are also responsive to the growth rate of the economy. In particular, hardware investments are strongly positively correlated with the growth rate of GNP and the rate of growth of hardware expenditures fluctuates around the technology-driven growth path in a manner that depends on the business cycle.

Our results strike at one of the most widely-used assumptions about IS budget behavior – that the relative share of software costs increases steadily over time according to an 5-curve, as in fig. 1. This curve has been cited numerous times in the literature to support the claim that software is a bottleneck which hampers the growth of IS use. Moreover, the results also show that the competing hypothesis of constant budget shares of hardware and software must also be modified to include the impact of the business cycle in addition to the price effect.

The trends in the budget shares of software and hardware support the notion that the production of information services has become increasingly hardware-intensive. Since the hardware budget share did not shrink despite the decline in hardware costs, the implication is that hardware capacity has grown faster over time than software effort, reflecting the substitution of hardware for software effort. A key question is how such substitution is implemented in the IS environment. While this may not be immediately apparent, a little reflection makes this quite clear. Substitution opportunities exist in both the development and operating environments. In the development environment, the provision of programmer productivity tools facilitates the substitution of hardware for software. While these tools can result in an increase in output per unit of programmer effort, they are typically hardware intensive and the gains in productivity are achieved at the cost of significant additional hardware. In the operating environment, this substitution can be achieved through the provision of additional target hardware capacity, which relaxes the hardware constraints on a system and reduces software effort. We briefly discuss each of the major forms of substitution in the IS environment. $^{15}$

The primary means by which hardware-software substitution has been effected is through the use of tools that decrease software effort but which are hardware-intensive. The development of high-level languages, followed by higher-level and problem-oriented languages and their subsequent popularity are such examples. The use of such languages allows gains in programmer productivity at the cost of an increase in the consumption of hardware resources [7]. The increasing use of Computer Aided Systems Engineering (CASE) tools such as design aids, program debuggers and application generators also reduces the design and programming effort while requiring significantly more hardware [24].

The growing popularity of database management systems and 4GL's are other examples of this trend [12]. The implementation of user-oriented relational systems requires a significant increase in hardware support compared to the earlier network or hierarchical systems. For example, a sample system implemented on IBM's hierarchical DBMS, IMS, had a throughput of up to 80 transactions per second on an IBM 3081, whereas the corresponding implementation on the relational DB2 could achieve a rate of only 16 transactions per second [21]. $^{16}$ Thus, the flexibility of the relational approach, which ultimately results in reduced software-development effort, requires an increase in the hardware outlay – a clear case of substitution. Another well known example is the development of OS/2 and other graphics-based operating systems for personal computers. This operating system is significantly more hardware-intensive than MS/DOS. For example, OS/2 requires a number of megabytes of memory and an advanced microprocessor, whereas DOS requires only a low level PC and consumes about 128K of memory. On the other hand, advanced operating systems provide many additional features that reduce programmer effort including, for example, multitasking, graphical user interfaces and a high level of integration. In summary, investments in software tools have been instrumental in reducing software effort. However, these gains have been made at the cost of significant increases in hardware capacity. As the costs of hardware continue to decrease, we should expect to see a continuation of this trend.

Another example of substitution between hardware capacity and software effort is the use of excess capacity in both the software-development and operations phases of the system life cycle. It is well known that the longer the response time in the software-development environment, the higher the effort required to develop any given system [4]. For a given workload, response time can be reduced by acquiring excess hardware capacity [27]. The result is that an increase in the hardware outlay (in the form of excess capacity) reduces the software-development effort. The software-development effort can also be reduced by relaxing capacity constraints in the target environment [4] – again resulting in the substitution of hardware capacity for software effort. Instead of expending programming resources to develop compact code that fits within the constraints of limited target hardware, it may now be more effective to provide additional hardware, thereby relaxing the hardware constraints and reducing the software effort.

This research also demonstrates the dependence of investments in information technology on general business conditions. In particular, it shows that investments in hardware are strongly positively correlated with the growth rate of GNP. That is, when the economy is growing, firms increase the level of their hardware investments. Correspondingly, when the economy is slowing, firms respond by reducing the level of their hardware investments.

The analysis provides several additional insights into the nature of the IS environment. It shows that while IS environments have become increasingly hardware-intensive as IS managers substitute hardware for software effort, both inputs are used in increasing quantities over time. That is, hardware and software are net complements in production and the dominant underlying trend is for the levels of investment in them to grow together. Yet, the research indicates that IS managers respond to unexpected business conditions primarily by adjusting their hardware investment schedules. This suggests that while the hardware industry will experience significant growth over the long term, it must be prepared to deal adequately with short-run fluctuations in the demand for its products.

## Appendix A

Use of the seemingly unrelated regression model in the analysis of budget components

The analysis of the budget-component equations (1)-(2) must take into account their mutual dependence, reflected in the variance-covariance matrix of the residuals, $\Omega$ . To estimate the matrix $n$ , we applied Zellner's [36] Seemingly Unrelated Regression (SUR) method. Under this method, one first estimates equations (1) and (2) separately, using Ordinary Least Squares. The Ordinary Least Squares estimates are used to compute the residuals $\{\epsilon_{sT}, \epsilon_{hT}\}$ , and the variance-covariance matrix $\Omega$ is estimated by

$$
[ \Omega ] = \left[ \begin{array}{c c} \hat {\sigma} _ {s s} & \hat {\sigma} _ {s h} \\ \hat {\sigma} _ {s h} & \hat {\sigma} _ {h h} \end{array} \right], \text { where }\tag{A-1}
$$

$$
\hat {\sigma} _ {s s} = \frac {1}{N} \sum_ {T = 1} ^ {N} \left[ \hat {\epsilon} _ {s T} \right] ^ {2},\tag{A-2}
$$

$$
\hat {\sigma} _ {h h} = \frac {1}{N} \sum_ {T = 1} ^ {N} \left[ \hat {\epsilon} _ {h T} \right] ^ {2} \text { and }\tag{A-3}
$$

$$
\hat {\sigma} _ {s h} = \frac {1}{N} \sum_ {T = 1} ^ {N} \left[ \hat {\epsilon} _ {s T} \cdot \hat {\epsilon} _ {h T} \right].\tag{A-4}
$$

The Generalized Least Squares (GLS) procedure can now be completed using the estimated variance-covariance matrix, $\Phi = \Omega \otimes I$ (where $\otimes$ denotes the Kronecker product). The GLS estimators are now given by

$$
\underline {{{{\hat {\beta}}}}} = \left[ X ^ {\prime} \hat {\Phi} ^ {- 1} X \right] ^ {- 1} X ^ {\prime} \hat {\Phi} ^ {- 1} \underline {{{{y}}}}, \text { where }\tag{A-5}
$$

$$
\underline {{{{\hat {\beta}}}}} = \left[ \begin{array}{l} \hat {\beta} _ {s} \\ \hat {\beta} _ {h} \end{array} \right], X = \left[ \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 1 & 2 & 0 & 0 \\ 1 & 3 & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & N & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 2 \\ \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 1 & N \end{array} \right] \text {and}\tag{A-6}
$$

$$
\underline {{{{y}}}} = \left[ \begin{array}{c} \log (S _ {1}) \\ \log (S _ {2}) \\ \vdots \\ \log (S _ {N}) \\ \log (H _ {1}) \\ \log (H _ {2}) \\ \vdots \\ \log (H _ {N}) \end{array} \right].\tag{A-7}
$$

The variance-covariance matrix of the estimated coefficient vector $\hat{\beta}$ is given by

$$
\operatorname{Var} \left(\underline {{{\hat {\beta}}}}\right) = \left(X ^ {- 1} \hat {\Phi} ^ {- 1} X\right) ^ {- 1}.\tag{A-8}
$$

As is well known (cf. [22]), when the explanatory variables are the same in both equations, the GLS estimator (A-5) coincides with the Ordinary Least Squares Coefficients of equations (1) and (2), but the variances given by (A-8) are different.

## Testing the hypothesis of constant budget shares

To test the hypothesis of constant budget shares, we have to impose the additional restriction $\beta_{s} = \beta_{h}$ which equates the coefficients of the time variable in the two regression equations. The hypothesis $\beta_{s} = \beta_{h}$ is a special case of a linear restriction of the form $R\beta = \theta$ on the regression coefficients. The test has to be performed with care due to the dependence between the residuals across equa-

tions. The test statistic is

$$
\lambda = (2 T - 2) \cdot \frac {\left(\underline {{r}} - R \underline {{\hat {\beta}}}\right) ^ {\prime} \left(R \hat {C} R ^ {\prime}\right) - 1 \left(\underline {{r}} - R \underline {{\hat {\beta}}}\right)}{\left(\underline {{y}} - X \underline {{\hat {\beta}}}\right) ^ {\prime} \left(\hat {\Omega} ^ {- 1} \otimes I\right) \left(\underline {{y}} - X \underline {{\hat {\beta}}}\right)},
$$

where

(A-9)

$$
\hat {C} = \left[ X ^ {\prime} \left(\hat {\Omega} ^ {- 1} \otimes I\right) X ^ {- 1} \right].\tag{A-10}
$$

Under the null hypothesis, the test statistic $\lambda$ follows a $\chi^{2}$ distribution with degrees of freedom equal to the number of linear restrictions in $R\beta = r$ .

## References

[1] I. Benbasat, A.S. Dexter, D.H. Drury, and R.C. Goldstein, A Critique of the Stage Hypothesis: Theory and Empirical Evidence, Communications of the ACM, May 1984, Vol. 27, pp. 476–485.

[2] B.W. Boehm, Software and Its Impact: A Quantitative Assessment, Datamation, May 1973.

[3] B.W. Boehm, Software Engineering, IEEE Transactions on Computers, Vol. C-25, No. 12, December 1976, pp. 1226–41.

[4] B.W. Boehm, Software Engineering Economics, Prentice-Hall, 1981.

[5] B.W. Boehm, Open Channel, Computer, March 1983, pp. 78–81.

[6] B.W. Boehm, Software Engineering Economics, IEEE Transactions on Software Engineering, Vol. SE-10, No. 1, January 1983, pp. 4–21.

[7] B.W. Boehm, Understanding and Controlling Software Costs, Information Processing 86, pp. 703–714, North-Holland, 1986.

[8] B.W. Boehm, Industrial Metrics Top-10 List, IEEE Software, September 1987, p. 84.

[9] E.J. Chikofsky and B.L. Rubenstein, CASE: Reliability Engineering for Information Systems, IEEE Software, March 1988, pp. 11–16.

[10] H.G. Cragon, Open Channel, Computer, December 1982, pp. 100–101.

[11] L.E. Druffel, Strategy for DoD Software Initiative, RADC, DACS, Griffiss AFB, NY, October 1982.

[12] H. Fosdick, Productivity in a Database Environment, Datamation, August 1982, pp. 109–112.

[13] W.I. Frank, The Ten Great Myths of Software, Computerworld, 1978.

[14] W.I. Frank, Critical Issues in Software, John Wiley, 1982.

[15] W.I. Frank, The History of Myth No. 1, Datamation, May 1983, pp. 252–256.

[16] V. Gurbaxani, Managing Information Systems Costs: An Economic Analysis of Hardware-Software Tradeoffs, ICIT Press, June 1990.

[17] V. Gurbaxani and H. Mendelson, Software and Hardware in Data Processing Budgets, IEEE Transactions on Software Engineering, Vol. 13, No. 9, September 1987, pp. 1010–1017.

[18] V. Gurbaxani and H. Mendelson, An Integrative Model of Information Systems Spending Growth, Information Systems Research, March 1990, pp. 23–46, 1990.

[19] V. Gurbaxani and H. Mendelson, The Use of Secondary Analysis in MIS Research, Survey Research in MIS, Harvard Business School Press, 1991.

[20] H.W. Hartman, Hardware Doesn't Matter, Software Magazine, June 1988, p. 10.

[21] International Data Corporation, Vendors, Users Seek to Manage the Database Management Revolution, EDP/IR, August 1985, Vol. 21, No. 7, pp. 1–4.

[22] G.G. Judge, R.C. Hill, W. Griffiths, H. Lutkepohl and T. Lee, Introduction to the Theory and Practice of Econometrics, Wiley and Sons, NY, 1982.

[23] J.L. King and K.L. Kraemer, Evolution and Organizational Information Systems: An Assessment of Nolan's Stage Model, Communications of the ACM, Vol. 27, 1984, pp. 466–475.

[24] D. Kull, To Raise Productivity, Work Smarter, Not Harder, Computer Decisions, 1984, pp. 164–189.

[25] H.C. Lucas and J.A. Sutton, The Stage Hypothesis S-Curve: Some Contradictory Evidence, Communications of the ACM, Vol. 20, 1977, pp. 254–259.

[26] M.M. Lehman, Laws and Conservation in Large Program Evolution, Proceedings, IEEE/PINY Workshop on Quantitative Software Models, October 1979, pp. 42–55.

[27] H. Mendelson, Pricing Computer Services: Queueing Effects, Communications of the ACM, Vol. 28, 1985, pp. 312–321.

[28] H. Mendelson, The Economics of Information Systems Management, Prentice Hall, forthcoming, 1990.

[29] R.L. Nolan, Managing the Computer Resource: A Stage Hypothesis, Communications of the ACM, No. 16, 1973, pp. 399–405.

[30] R.L. Nolan, Managing the Crisis in Information Systems, Harvard Business Review, March/April 1979, pp. 115–126.

[31] OECD, Software: An Emerging Industry, ICCP series No. 9, 1985.

[32] W.E. Perry, Data Processing Budgets, Prentice-Hall, Englewood Cliffs, N.J., 1985.

[33] R. Pfaffenberger and J. Patterson, Statistical Methods, Richard D. Irwin, Homewood, IL, 1977.

[34] M. Phister, Jr., Data Processing Technology and Economics, Santa Monica Publishing Company and Digital Press, 1979.

[35] H. Schaeffer, Data Center Operations, Prentice Hall, Englewood Cliffs, N.J., 1987.

[36] A. Zellner, An Efficient Method of Estimating Seemingly Unrelated Regressions and Tests of Aggregation Bias, Journal of the American Statistical Association, Vol. 57, 1962, pp. 348–368.
