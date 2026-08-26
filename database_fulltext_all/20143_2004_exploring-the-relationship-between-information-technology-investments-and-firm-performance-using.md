---
otero_id: 20143
otero_key: "ANVR752M"
title: "Exploring the relationship between information technology investments and firm performance using regression splines analysis"
authors: "Kweku-Muata Osei-Bryson; Myung Ko"
year: "2004"
journal: "Information & Management"
doi: "10.1016/j.im.2003.09.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring the relationship between information technology investments and firm performance using regression splines analysis

Kweku-Muata Osei-Bryson<sup>a,\*</sup>, Myung Ko<sup>b,1</sup>

<sup>a</sup>Department of Information Systems and The Information Systems Research Institute,

Virginia Commonwealth University, Richmond, VA 23284, USA

<sup>b</sup>Department of Information Systems, College of Business, The University of Texas at San Antonio, San Antonio, TX 78249, USA

Received 14 April 2002; received in revised form 13 June 2003; accepted 2 September 2003

Available online 17 December 2003

## Abstract

Identifying the business value of information technology (IT) investments has been a major concern of managers and researchers. Various studies have addressed this issue but have provided contradictory results. Here, we explore the relationship between IT investments and firm performance using a relatively new technique, multivariate adaptive regression splines (MARS), and attempt to answer two questions: (1) do investments in IT have a positive impact on organizational productivity? and (2) for a given level of investment, what portion of the total should be invested in IT to maximize organizational productivity? Our results suggest that depending on the conditions that applied, an unbiased observer could either conclude that investments in IT has a positive statistically significant effect on productivity, or that there is a ‘productivity’ paradox. This suggests that the relationship between IT investments and organizational performance is much more complex than that found in some other studies. Our results could also provide guidance to managers who are responsible for determining the allocation of organizational resources.

<sup>#</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: IT investments; Productivity; Productivity paradox; Regression splines; Multivariate adaptive regression splines (MARS); Data mining

## 1. Introduction

For most of the past half-century, modern organiza tions have been increasing their investments in information technology (IT) (e.g. [5,13,28]), primarily because of the belief that IT has a significant positive impact on organizational performance. Many managers and researchers have been interested in determining the validity of this belief, and various studies have been conducted. Some previous ones have attempted to examine the contribution of IT to output but have failed to show any evidence of IT’s impact on productivity in spite of the increased IT investment [18], and so the ‘‘IT productivity paradox’’ has been an issue debated by IS researchers for the past decade [2,3,11,12,21]. Various explanations have been offered for the productivity paradox including mismeasurement of outputs and inputs, time lags due to learning and adjustment, redistribution of profits, mismanagement of IT and inappropriateness of traditional productivity measures. Some have made the claim that inconsistent findings from IT productivity research are also due to lack of adequate data [29,30]. However, other studies suggest that IT does have a positive impact on organizational productivity [8,20,26,27]. Given these inconsistent results, we are left to wonder: what is the truth?

Here, we took another look at understanding the relationship between IT investments and organizational performance. We examined two questions:

\- Do investments in the IT stock have a positive statistically significant impact on the value-added productivity measure?

\- Given that a fixed amount is available for investing in IT stock and non-IT labor, what is the optimal proportion that should be invested in the IT stock in order to maximize the value-added productivity measure?

The first question has been addressed by various researchers, and our contribution was to report on insights obtained by using a relatively new technique, multivariate adaptive regression splines (MARS) that offers richer analysis than some of the more traditional statistical techniques. Our motivation for addressing the second question was not simply to identify a specific numeric value but to gain a deeper understanding of the impact on productivity of using investments in IT as a substitute for those in non-IT labor.

## 2. Previous research

Several studies have examined the relationship between IT investments and productivity at the firm level but their findings have been inconsistent. Here, we briefly review previous empirical research on it. A summary is shown in Table 1.

In summary, while earlier studies have shown no relationship between IT investments and productivity at the firm level, some recent ones have shown evidence of a positive relationship. Most of these studies examined whether there was a productivity paradox.

## 3. Regression splines

Regression equations attempt to model the relationship between outcome and predictor variables using a single function (e.g. linear or log linear) of the predictor variables, describing the contribution of each predictor (independent) variable with a single coefficient. To capture any relevant non-linearity, higher order terms $( x ^ { 2 } .$ , etc.) may be introduced but their coefficients will be estimated using the data globally and thus, local features of the true function might not be captured [9]. On the other hand, a regression spline (RS) approach models the mean outcome as a piecewise polynomial, such as a piecewise continuous linear function (linear spline) or piecewise cubic function with continuous derivative of a predictor variable. A piecewise polynomial func tion f(x) can be obtained by dividing the range of each predictor variable into one or more intervals and representing the function f by a separate polynomial in each interval [10]. Thus, splines are described as piecewise polynomials whose segments have been joined together smoothly at the knots [6], where a knot is the end of one region of data and the beginning of another [23]. A regression spline function can be expressed as a linear combination of piecewise polynomial basis functions (BF) that are joined together smoothly at the knots and the coefficients of the basis function are estimated by minimizing the sum of square errors. Since this process is same as the estimation process of regression, this estimated spline is called a regression spline. Because the segmented nature of piecewise polynomials adjusts more effectively to local characteristics of a function or data, they provide more flexibility than polynomials. RS performs a polynomial fit in each region with constraints at the knots using the least squares criterion. Accordingly, ‘‘the parameters of the regression functions change from one region to another.’’ Appendix A provides an overview of multivariate adaptive regression splines.

Here, we explore the impact of IT investments on organizational productivity using MARS. It should be noted that both regression and regression splines can identify the order of importance of the independent variables in a predictive model, and estimate the value of the coefficient for each independent variable. However, if the impact of an independent variable on the dependent variable is conditional, then regression splines can identify such conditions while regression cannot. Thus, some questions cannot be answered using regression, since it does not provide means for exploring those questions. While most previous studies have examined the impact of IT investments on productivity, they have not identified conditions under which the impact of IT investments on productivity in terms of positive, negative, or non-existent. Regression splines can provide the means for exploring the research questions in greater depth than would have been possible using simple regression.

T<sub>a</sub>bl<sub>e</sub> 1 R<sub>esearc</sub>h <sub>summary</sub> <sub>o</sub>f IT i<sub>mpac</sub>t<sub>s</sub> <sub>on</sub> <sub>organ</sub>i<sub>za</sub>ti<sub>ona</sub>l <sub>pro</sub>d<sub>uc</sub>ti<sub>v</sub>it<sub>y</sub>

<table><tr><td>Study/year</td><td>Research method</td><td>Dataset/period</td><td>Measures</td><td>Results of IT impact</td></tr><tr><td>Weill [32]/1992</td><td>Hierarchical regression</td><td>33 valve manufacturing firms during 1982–1987</td><td>IT investment type (transactional, strategic, informational), financial measures (sales growth, return on assets, measures of labor productivity)</td><td>Transactional IT—positive relationship with performance strategic or informational IT—no relationship</td></tr><tr><td>Mahmood and Mann [19]/1993</td><td>Pearsonian correlation analysis and canonical correlation analysis</td><td>Computerworld&#x27;s list of “the 100 most effective users of information systems” for 1989</td><td>Organizational IT investment, strategic and economical performance measures</td><td>The individual IT measures are weakly related to individual performance variables. The combined IT measures are significantly related to the performance variables</td></tr><tr><td>Loveman [18]/1994</td><td>General production function employing regression analysis</td><td>60 manufacturing business units during 1978–1984</td><td>Material expenditure, non-IT purchased services expenditure, total labor compensation, non-IT capital, IT capital</td><td>No evidence of productivity gains from IT investments</td></tr><tr><td>Kivijarvi and Saarinen [14]/(1995)</td><td>Correlation and variance analyses</td><td>36 Finnish firms</td><td>Various dimensions of level of investments in IS, financial performance, state of information systems, user information satisfaction, and impact of an information systems</td><td>No direct relationship between IT investments and financial performance. However, IT investments improve performance in the long term</td></tr><tr><td>Lichtenberg [17]/1995</td><td>Regression analysis</td><td>Firms reported by Computerworld and InformationWeek during the period 1988–1991</td><td>IS budget, computer capital, non-computer capital, non-computer labor, IS labor</td><td>Computer capital and IS labor jointly contribute about 21% of output</td></tr><tr><td>Hitt and Brynjolfsson [11]/1996</td><td>Cobb-Douglas production function and the iterated seemingly unrelated regression (ISUR)</td><td>370 firms during 1988–1992</td><td>Variables in the dimensions of productivity, profitability, and consumer value</td><td>Increased productivity and consumer value but no impact on business profitability</td></tr><tr><td>Dewan and Min [5]/1997</td><td>Constant elasticity of substitution (CES) translog and translog production functions</td><td>370 firms during 1988–1992</td><td>IT substitutability for other inputs</td><td>IT capital is a substitute for capital and labor. Evidence of excess returns on IT capital relative to labor</td></tr><tr><td>Bharadwaj [1]/2000</td><td>Logistic regression analysis and the Wilcoxon rank sum test</td><td>All 56 firms that were ranked as IT leaders at least two of the four years from 1991 to 1994 by InformationWeek and 56 control sample firms</td><td>Various profitability measures and cost related ratios</td><td>The relationship between superior IT capability and firm performance is positive</td></tr><tr><td>Lee and Menon [15]/2000</td><td>Multivariate analysis of variance, cluster analysis</td><td>1064/1976–1994</td><td>IT capital, medical (non-IT) capital, IT labor, medical (non-IT) labor</td><td>The relationship between IT capital and productivity is positive. However, the relationship between IT labor and productivity is negative</td></tr><tr><td>Stratopoulos and Dehning [31]/2000</td><td>Wilkoxon signed rank test</td><td>71 companies from 1988 to 1997 and 71 control sample firms</td><td>Financial performance (ratios)</td><td>Successful investment in IT leads to superior financial performance</td></tr><tr><td>Shao and Lin [24–27]/2000–2002</td><td>Parametric econometric approach (Cobb-Douglas/translog production frontiers)</td><td>370 firms during 1988–1992</td><td>Capital, labor, IT investments</td><td>IT has a positive effect on technical efficiency and thus, it lead to the productivity growth</td></tr></table>

Table 2 Variable definitions [11]

<table><tr><td>Variable</td><td>Description</td><td>Source</td></tr><tr><td>Output</td><td>Gross sales deflated by output price</td><td>Compustat</td></tr><tr><td>Output price</td><td>Output deflator based on two-digit industry from BEA estimates of industry price deflators. If not available, sector level deflator for intermediate materials, supplies, and components</td><td>Bureau of Economic Analysis, 1993</td></tr><tr><td>IT capital</td><td>Market value of central processors plus value of PCs and terminals obtained from IDG survey. Deflated by computer price. Average value of PC determined as weighted average of PC price from Berndt and Griliches (1990) and value of PC from IBM. Resulting estimate is $2840 in 1990 dollars</td><td>IDG Survey</td></tr><tr><td>Computer price</td><td>Gordon&#x27;s deflator for computer systems—extrapolated to current period at same rate of price decline (-19.7% per year)</td><td>Gordon, 1993</td></tr><tr><td>IS labor</td><td>Labor portion of IS budget. Deflated by labor price</td><td>IDG Survey</td></tr><tr><td>Labor price</td><td>Price index for total compensation</td><td>Council of Economic Advisors, 1992</td></tr><tr><td>Value-added (V)</td><td>Output minus non-labor expense. Non-labor expense is calculated as total firm expenses (excluding interest, taxes, and depreciation) divided by output price less labor</td><td>Compustat</td></tr><tr><td>IT stock (T)</td><td>Calculated as IT capital plus three times IS labor</td><td>Calculation</td></tr><tr><td>Non-IT capital (K)</td><td>Deflated book value of capital less computer capital as calculated above</td><td>Compustat</td></tr><tr><td>Non-IT labor (L)</td><td>Available labor expenses or estimated labor expenses based on sector average labor costs times number of employees minus IS labor. Deflated by labor price</td><td>Compustat</td></tr><tr><td>Industry (IND)</td><td>Primary industry at the two-digit SIC level</td><td>Compustat</td></tr></table>

## 4. Regression splines analysis

## 4.1. Experimental data

We employed a popular dataset that has been used in some important studies on IT and productivity. We believe that using the same dataset promotes the comparability of our findings with previous studies without any bias. Variables included in this study are shown in Table 2. For detailed description of these variables, please see the study by Hitt and Brynjolfsson [11].

## 4.2. Experimental approach

We used the Multivariate Adaptive Regression Splines software, version 2.0 by Salford Systems [22].<sup>2</sup> Using the Cobb–Douglas production function as our theoretical model (see Appendix B), we generated an RS model that allows for only main-effects (i.e. it does not allow any interaction between the input variables). Two variables, year (YR) and industry (IND: using the two digit primary SIC level of US statistics or sector of the economy in which a firm operates) were included as categorical predictors. The variable, valueadded (V) was included as the target variable and non-IT labor (L), IT stock (T), and non-IT capital (K) were included as non-categorical predictors.

## 4.3. Results from the regression splines analysis

Table 3 provides important statistics of the dataset while Table 4 provides the order of importance of the input variables generated by MARS. Similar to the H&B regression models, in the RS model non-IT

Table 3 Sample statistics

<table><tr><td>Variable</td><td>Mean</td><td>S.D.</td><td>N</td></tr><tr><td> $\log_e T$ </td><td>4.911</td><td>1.164</td><td>1248</td></tr><tr><td> $\log_e L$ </td><td>6.839</td><td>1.116</td><td>1248</td></tr><tr><td> $\log_e K$ </td><td>8.065</td><td>1.473</td><td>1248</td></tr></table>

Table 4  
Importance of variables

<table><tr><td>Variable</td><td>Cost of omission</td><td>Importance</td></tr><tr><td> $\log_e L$ </td><td>0.158</td><td>100.000</td></tr><tr><td>IND</td><td>0.069</td><td>52.593</td></tr><tr><td> $\log_e K$ </td><td>0.049</td><td>33.623</td></tr><tr><td> $\log_e T$ </td><td>0.036</td><td>8.677</td></tr><tr><td>YR</td><td>0.035</td><td>0.000</td></tr></table>

labor, industry, non-IT capital, and the IT stock were selected as being the important predictor variables while year was not selected. The RS model had a $R ^ { 2 }$ value of 0.97, suggesting that it has a high predictive power.

The RS model involved 10 basis functions as described in Table 5. In our RS model, there was one knot for each of the non-categorical input variables. The knot for IT stock (T) was represented by $T _ { \mathrm { c v } } ,$ where $\log _ { \mathrm { e } } ( T _ { \mathrm { c v } } ) = 0 . 4 4 8$ (see BF15 in Table 5); the knot for non-IT labor (L) was represented by $L _ { \mathrm { c v } }$ where $\log _ { \mathrm { e } } ( L _ { \mathrm { c v } } ) = 5 . 8 0 1$ (see BF1 and BF2 in Table $5 ) ;$ and the knot for non-IT capital (K) was represented by $K _ { \mathrm { c v } } ,$ where log $\left( K _ { \mathrm { c v } } \right) = 5 . 5 3 5$ (see BF7 and BF8 in Table 5).

The log linear regression equation corresponding to our RS model can be expressed in terms of these basis functions as follows:

$$
\begin{array}{r l} \log_ {\mathrm{e}} V & = 5. 4 0 2 + 0. 7 6 1 \times \mathrm{BF} 1 - 0. 4 5 6 \times \mathrm{BF} 2 \\ & + 0. 5 1 5 \times \mathrm{BF} 3 + 0. 1 6 9 \times \mathrm{BF} 5 + 0. 1 8 9 \\ & \times \mathrm{BF} 7 - 0. 3 5 3 \times \mathrm{BF} 8 + 0. 4 4 8 \times \mathrm{BF} 9 \\ & + 0. 3 5 8 \times \mathrm{BF} 1 1 - 0. 1 6 7 \times \mathrm{BF} 1 3 + 0. 0 4 8 \\ & \times \mathrm{BF} 1 5 \end{array}
$$

Table 5  
Regression spline model from MARS

<table><tr><td colspan="2">Basis function</td><td>Coefficient</td><td>Variable</td><td>Knot (log value)</td></tr><tr><td>0</td><td></td><td>5.402</td><td></td><td></td></tr><tr><td>1</td><td>BF1 = max (0,  $\log_e L - 5.801$ )</td><td>0.761</td><td> $\log_e L$ </td><td>5.801</td></tr><tr><td>2</td><td>BF2 = max (0, 5.801 -  $\log_e L$ )</td><td>-0.456</td><td> $\log_e L$ </td><td>5.801</td></tr><tr><td>3</td><td>BF3 = (IND = 13 or IND = 21 or IND = 29 or IND = 48 or IND = 49 or IND = 58 or IND = 60 or IND = 61 or IND = 62 or IND = 78 or IND = 79)</td><td>0.515</td><td>IND</td><td>0.000</td></tr><tr><td>5</td><td>BF5 = (IND = 10 or IND = 12 or IND = 13 or IND = 14 or IND = 20 or IND = 24 or IND = 26 or IND = 27 or IND = 28 or IND = 29 or IND = 36 or IND = 39 or IND = 40 or IND = 44 or IND = 49 or IND = 50 or IND = 51 or IND = 52 or IND = 53 or IND = 56 or IND = 59 or IND = 60 or IND = 62 or IND = 75 or IND = 78 or IND = 79 or IND = 87)</td><td>0.169</td><td>IND</td><td>0.000</td></tr><tr><td>7</td><td>BF7 = max (0,  $\log_e K - 5.535$ )</td><td>0.189</td><td> $\log_e K$ </td><td>5.535</td></tr><tr><td>8</td><td>BF8 = max (0, 5.535 -  $\log_e K$ )</td><td>-0.353</td><td> $\log_e K$ </td><td>5.535</td></tr><tr><td>9</td><td>BF9 = (IND = 10 or IND = 14 or IND = 15 or IND = 16 or IND = 20 or IND = 21 or IND = 22 or IND = 23 or IND = 25 or IND = 27 or IND = 28 or IND = 30 or IND = 31 or IND = 32 or IND = 33 or IND = 34 or IND = 35 or IND = 37 or IND = 38 or IND = 39 or IND = 47 or IND = 50 or IND = 51 or IND = 52 or IND = 54 or IND = 56 or IND = 59 or IND = 60 or IND = 61 or IND = 62 or IND = 75 or IND = 78 or IND = 79 or IND = 80 or IND = 87)</td><td>0.448</td><td>IND</td><td>0.000</td></tr><tr><td>11</td><td>BF11 = (IND = 23 or IND = 24 or IND = 26 or IND = 31 or IND = 36 or IND = 39 or IND = 40 or IND = 42 or IND = 44 or IND = 45 or IND = 48 or IND = 50 or IND = 53 or IND = 60 or IND = 62 or IND = 78 or IND = 87)</td><td>0.358</td><td>IND</td><td>0.000</td></tr><tr><td>13</td><td>BF13 = (IND = 10 or IND = 12 or IND = 14 or IND = 23 or IND = 26 or IND = 31 or IND = 33 or IND = 39 or IND = 40 or IND = 44 or IND = 45 or IND = 48 or IND = 50 or IND = 52 or IND = 60 or IND = 61 or IND = 79 or IND = 87)</td><td>-0.167</td><td>IND</td><td>0.000</td></tr><tr><td>15</td><td>BF15 = max (0,  $\log_e T - 0.448$ )</td><td>0.048</td><td> $\log_e T$ </td><td>0.448</td></tr></table>

Table 6  
Regression spline model by region

<table><tr><td>Region</td><td>IT stock  $\log_e T$ </td><td>Non-IT labor: $\log_e L$ </td><td>Non-IT capital: $\log_e K$ </td><td>Production function</td></tr><tr><td>1</td><td> $T \leq T_{\text{cv}}$ </td><td> $L \leq L_{\text{cv}}$ </td><td> $K \leq K_{\text{cv}}$ </td><td> $\gamma L^{0.456}K^{0.353}_{e^{-(0.456\times 5.801)} \times e^{-(0.353\times 5.535)}}$ </td></tr><tr><td>2</td><td></td><td></td><td> $K > K_{\text{cv}}$ </td><td> $\gamma L^{0.456}K^{0.189}_{e^{-(0.456\times 5.801)} \times e^{-(0.189\times 5.535)}}$ </td></tr><tr><td>3</td><td></td><td> $L > L_{\text{cv}}$ </td><td> $K \leq K_{\text{cv}}$ </td><td> $\gamma L^{0.761}K^{0.353}_{e^{-(0.761\times 5.801)} \times e^{-(0.353\times 5.535)}}$ </td></tr><tr><td>4</td><td></td><td></td><td> $K > K_{\text{cv}}$ </td><td> $\gamma L^{0.761}K^{0.189}_{e^{-(0.761\times 5.801)} \times e^{-(0.189\times 5.535)}}$ </td></tr><tr><td>5</td><td> $T > T_{\text{cv}}$ </td><td> $L \leq L_{\text{cv}}$ </td><td> $K \leq K_{\text{cv}}$ </td><td> $\gamma T^{0.048}L^{0.761}K^{0.353}_{e^{-(0.048\times 0.448)} \times e^{-(0.761\times 5.801)} \times e^{-(0.353\times 5.535)}}$ </td></tr><tr><td>6</td><td></td><td></td><td> $K > K_{\text{cv}}$ </td><td> $\gamma T^{0.048}L^{0.761}K^{0.189}_{e^{-(0.048\times 0.448)} \times e^{-(0.761\times 5.801)} \times e^{-(0.189\times 5.535)}}$ </td></tr><tr><td>7</td><td></td><td> $L > L_{\text{cv}}$ </td><td> $K \leq K_{\text{cv}}$ </td><td> $\gamma T^{0.048}L^{0.456}K^{0.353}_{e^{-(0.048\times 0.448)} \times e^{-(0.456\times 5.801)} \times e^{-(0.353\times 5.535)}}$ </td></tr><tr><td>8</td><td></td><td></td><td> $K > K_{\text{cv}}$ </td><td> $\gamma T^{0.048}L^{0.456}K^{0.189}_{e^{-(0.048\times 0.448)} \times e^{-(0.456\times 5.801)} \times e^{-(0.189\times 5.535)}}$ </td></tr></table>

g ¼ ðe<sup>5:402</sup>Þðe<sup>0:515BF3</sup>e<sup>0:169BF5</sup>e<sup>0:448BF9</sup>e<sup>0:358BF11</sup>e<sup>0:167BF13</sup>Þ.

Given that there is one knot for each of the noncategorical input variables, it follows that there are eight different regions, each with its own production function to explain the relationship between the IT stock, non-IT labor, and non-IT labor input variables and the value-added output variable (see Table 6).

## 5. Comparison of results: regression and MARS analyses

We next compared our results from the RS model with those from the regression equation models of Hitt and Brynjolfsson. While both approaches provided interpretable models with high predictive power (i.e. $R ^ { 2 } \stackrel { - } { = } 0 . 9 7$ for RS and for most of the regression models), we believe that our analysis provided additional insights that were not identified in previous studies. The responses to our two main research questions were:

## 5.1. Question 1

Does investment in the IT stock have a positive statistically significant impact on productivity?

## 5.1.1. Hitt and Brynjolfsson study answer

\- IT has a positive statistically impact on productivity since $\beta _ { \mathrm { T } } > 0$ (see Table 7).

\- Non-IT labor (L), non-IT capital (K) and industry (IND) also have a positive statistically significant impact on productivity.

## 5.1.2. Our study answer

\- On average, IT stock (T) had a positive statistically significant impact on the firm performance measure value-added (V) only when it exceeded its knot $T _ { \mathrm { c v } }$ (i.e. log $\left( T _ { \mathrm { c v } } \right) = 0 . 4 4 8 )$ . This was the interpretation of basis function BF15 (max(0, log<sub>e</sub> $T \mathrm { ~ - ~ } 0 . 4 4 8 ) )$ of Table 5 and its coefficient value 0.048. Thus for those situations where, even after additional investment in the IT stock, the total IT stock investments is still below $T _ { \mathrm { c v } }$ there would appear to be a ‘productivity paradox as there was no improvement in value-added.

\- Non-IT labor (L), non-IT capital (K) and industry (IND) also had a positive statistically significant impact on productivity.

\- Non-IT labor (L) had a greater potential for impacting productivity than the IT stock (see Fig. 1).

Results of H&B regression analyses [11]

<table><tr><td rowspan="2">Variable</td><td colspan="4">Parameter estimates</td></tr><tr><td>OLS</td><td>ISUR</td><td>OLS on 2SLS</td><td>2SLS</td></tr><tr><td>IT stock  $\beta_{T}$ </td><td>0.0883* (0.0118)</td><td>0.0897* (0.00920)</td><td>0.0696* (0.00940)</td><td>0.0479* (0.0219)</td></tr><tr><td>Non-IT capital  $\beta_{K}$ </td><td>0.212* (0.0125)</td><td>0.225* (0.00864)</td><td>0.181* (0.0159)</td><td>0.128* (0.0269)</td></tr><tr><td>Non-IT labor  $\beta_{L}$ </td><td>0.663* (0.0231)</td><td>0.630* (0.0112)</td><td>0.725* (0.0216)</td><td>0.812* (0.0415)</td></tr><tr><td>Production function: V</td><td> $\gamma T^{0.0883} L^{0.663} K^{0.212}$ </td><td> $\gamma T^{0.0897} L^{0.630} K^{0.225}$ </td><td> $\gamma T^{0.0696} L^{0.725} K^{0.181}$ </td><td> $\gamma T^{0.0479} L^{0.812} K^{0.128}$ </td></tr><tr><td> $R^{2}$ </td><td>0.97</td><td>0.94–0.95</td><td>0.97</td><td>0.97</td></tr></table>

$\gamma \colon$ impact from industry, intercept.  
p < 0.05

## 5.1.3. Summary of responses

Both models suggested that investments in the IT stock (T) can have a positive statistically significant impact on productivity (V). Our findings differed in two ways: (1) the RS model suggested that the response to this question was conditioned based on the investments in non-IT labor, while the response of each H&B regression models was unconditioned; (2) the RS model suggested that the average impact of investments in the IT stock was not uniform and may be even marginal or non-existent under certain conditions while the H&B models suggested a uni form average impact.

## 5.2. Question 2

Assuming non-IT capital is fixed, and given a fixed amount (i.e. $A _ { ( T + L ) } )$ is available for investment in the IT stock and non-IT labor, what is the optimal proportion (i.e. $\rho _ { T } )$ of this amount that should be invested in the IT stock so as to maximize productivity (i.e. value-added)?

![](/api/attachments/ANVR752M/fulltext/images/5b3953cca486be2751db41549cddf1cf2adaf603fd19dd103bfbc941b8787e11.jpg)  
Non-IT Labor Impact Non-IT Capital Impact IT Stock Impact  
Fig. 1. Regression splines model with no interaction: separate impact of each variable.

In answering these questions we used the fact that $\rho _ { T } = \beta _ { T } / ( \beta _ { T } + \beta _ { T } )$ is on the boundary of the relevant region (see Appendix C).

## 5.2.1. Hitt and Brynjolfsson study answer

\- Productivity was a concave function of $\rho _ { T }$ and as such there was an optimal proportion. If the additional investments in the IT stock resulted in the IT stock proportion exceeding its optimal value then there would be a reduction in productivity which could lead to the conclusion that there was a ‘productivity paradox’ while the real problem was that there was a sub-optimal allocation of resources with respect to IT stock and non-IT labor. In Table 8, we reported the value of $\rho _ { T }$ for each of the H&B regression models. For each model the optimal proportion for the IT stock was relatively low, suggesting that most of the investment should be in non-IT labor and not IT stock.

\- The value of $\rho _ { T }$ was the same for all values of $A _ { ( T + L ) }$ . To the extent that the value of $A _ { ( T + L ) }$ was related to company size, this result suggested the optimal proportion of $A _ { ( T + L ) }$ that should be invested in the IT stock was independent of the company size (Fig. 2).

Table 8  
Optimal IT stock proportions for Hitt and Brynjolfsson models

<table><tr><td rowspan="2">Variable</td><td colspan="4">Parameter estimates</td></tr><tr><td>OLS</td><td>ISUR</td><td>OLS on 2SLS</td><td>2SLS</td></tr><tr><td>IT stock ( $\beta_T$ )</td><td>0.0883</td><td>0.0897</td><td>0.0696</td><td>0.0479</td></tr><tr><td>Non-IT labor ( $\beta_L$ )</td><td>0.663</td><td>0.630</td><td>0.725</td><td>0.812</td></tr><tr><td> $\rho_T$ </td><td>0.1175</td><td>0.1246</td><td>0.0876</td><td>0.0557</td></tr></table>

## 5.2.2. Our study answer

\- Productivity was again a concave function of $\rho _ { T }$ (see Fig. 3) and as such, for a given value of $A _ { ( T + L ) }$ there was a corresponding optimal proportion. For each $A _ { ( T + L ) }$ the optimal proportion for the IT stock was relatively low (see Tables 9 and 10). The implication of this is that, while investment in the IT stock may increase value-added, beyond a certain point if the additional investment in the IT stock is accompanied by a corresponding reduction in the investment in non-IT labor, then there could be a reduction in productivity.

![](/api/attachments/ANVR752M/fulltext/images/b37b5d9632bb0ed4e1ea16d924a28169bb6794aaaad6fe650af22e34460619eb.jpg)  
Fig. 2. H&B model—combined impact of IT stock and non-IT labor.

![](/api/attachments/ANVR752M/fulltext/images/061c0705cea4cd28ab1843e5d3f978c6c5ef1d7232fc6c6ed0e96c4dd16e61b6.jpg)  
Fig. 3. Regression splines with no interaction model—combined multiplier for IT stock and non-IT labor.

\- Unlike the H&B models for which there was a single value of $\rho _ { T }$ that was applicable for all values of $A _ { ( T + L ) } ,$ that for this RS model the value of $\rho _ { T }$ varied with the value of $A _ { ( T + L ) }$ . Fig. 3 displays this graphically. To the extent that the value of $A _ { ( T + L ) }$ was related to company size, this result suggested that the optimal proportion that should be invested in the IT stock was dependent on the company size.

## 5.2.3. Summary of responses

Both models suggested that, beyond a certain point, substituting IT investments for investments in non-IT labor was counter productive, and that the optimal proportion was a relatively low value; this suggestion runs counter to one of the major reasons for increased investments in the IT stock and the general belief that ‘‘more is better.’’ These results could also provide another explanation for the apparent occurrence of the productivity paradox. If two companies invest the same amount in non-IT capital, and the same total amount $A _ { ( T + L ) }$ in the IT stock and non-IT labor, when one company invests the optimal IT stock proportion while the other invests more than the optimal then the second company would have a lower value-added amount than the first, even though it invested more in IT stock. While the H&B models suggested that the optimal proportion was independent of company size (as measured in the total amount available for investments in the IT stock and non-IT labor), the RS model suggested that the optimal proportion may depend on company size.

Optimal IT stock proportion for regions

<table><tr><td>Region</td><td> $\beta_T$ </td><td> $\beta_L$ </td><td> $\rho_T$ </td><td></td></tr><tr><td> $T \leq T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>0.000</td><td>0.456</td><td>Min $\{\beta_T / (\beta_T + \beta_L), T_{\text{cv}} / A_{(T+L)}\}$ </td><td>0.000</td></tr><tr><td> $T \leq T_{\text{cv}}; L > L_{\text{cv}}$ </td><td>0.000</td><td>0.761</td><td>Min $\{\beta_T / (\beta_T + \beta_L), T_{\text{cv}} / A_{(T+L)}\}$ </td><td>0.000</td></tr><tr><td> $T > T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>0.048</td><td>0.456</td><td>Max $\{\beta_T / (\beta_T + \beta_L), T_{\text{cv}} / A_{(T+L)}\}$ </td><td>Max $\{0.095, T_{\text{cv}} / A_{(T+L)}\}$ </td></tr><tr><td> $T > T_{\text{cv}}; L > L_{\text{cv}}$ </td><td>0.048</td><td>0.761</td><td>Max $\{\beta_T / (\beta_T + \beta_L), T_{\text{cv}} / A_{(T+L)}\}$ </td><td>Max $\{0.059, T_{\text{cv}} / A_{(T+L)}\}$ </td></tr></table>

Table 10  
Optimal IT stock proportion for cases

<table><tr><td rowspan="2">Case</td><td colspan="3">Possible regions</td></tr><tr><td>Properties</td><td> $\rho_T$ </td><td>Combined impact</td></tr><tr><td> $A_{(T+L)} \leq T_{\text{cv}}$ </td><td> $T \leq T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>0.000</td><td> $A_{(T+L)}^{0.456}$  $e^{-(0.456 \times 5.801)}$ </td></tr><tr><td> $T_{\text{cv}} < A_{(T+L)} \leq L_{\text{cv}}$ </td><td> $T \leq T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>0.000</td><td> $A_{(T+L)}^{0.456}$  $e^{-(0.456 \times 5.801)}$ </td></tr><tr><td> $\Rightarrow T_{\text{cv}}/A_{(T+L)} \geq (T_{\text{cv}}/L_{\text{cv}})$  $\Rightarrow T_{\text{cv}}/A_{(T+L)} \geq 0.005$ </td><td> $T > T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>Max{0.095,  $T_{\text{cv}}/A_{(T+L)}$ }</td><td> $\rho_T^{0.048}(1 - \rho_T)^{0.456}$  $A_{(T+L)}^{(0.048 + 0.456)}$  $e^{-(0.048 \times 0.448)}e^{-(0.456 \times 5.801)}$ </td></tr><tr><td> $L_{\text{cv}} < A_{(T+L)} \leq T_{\text{cv}} + L_{\text{cv}}$ </td><td> $T \leq T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>0.000</td><td> $A_{(T+L)}^{0.456}$  $e^{-(0.456 \times 5.801)}$ </td></tr><tr><td> $\Rightarrow T_{\text{cv}}/A_{(T+ L)} < (T_{\text{cv}}/L_{\text{cv}})$  $\Rightarrow T_{\text{cv}}/A_{(T+L)} < 0.005$ </td><td> $T \leq T_{\text{cv}}; L > L_{\text{cv}}$ </td><td>0.000</td><td> $A_{(T+L)}^{0.761}$  $e^{-(0.761 \times 5.801)}$ </td></tr><tr><td></td><td> $T > T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>0.095Max{0.095,  $T_{\text{cv}}/A_{(T+L)}$ }</td><td> $\rho_T^{0.048}(1 - \rho_T)^{0.456}$  $A_{(T+L)}^{(0.048 + 0.456)}$  $e^{-(0.048 \times 0.448)}e^{-( 0.456 \times 5.801)}$ </td></tr><tr><td> $A_{(T+L)} > T_{\text{cv}} + L_{\text{cv}}$ </td><td> $T \leq T_{\text{cv}}; L > L_{\text{cv}}$ </td><td>0.000</td><td> $A_{(T+L)}^{0.761}$  $e^{-(0.761 \times 5.801)}$ </td></tr><tr><td> $\Rightarrow T_{\text{cv}}/A_{(T+L)} < (T_{\text{cv}}/(T_{\text{cv}} + L_{\text{cv}}))$  $\Rightarrow T_{\text{cv}}/A_{(T+L)} < 0.005$ </td><td> $T > T_{\text{cv}}; L \leq L_{\text{cv}}$ </td><td>0.095Max{0.095,  $T_{\text{cv}}/A_{(T+L)}$ }</td><td> $\rho_T^{0.048}(1 - \rho_T)^{0.456}$  $A_{(T+L)}^{(0.048+0.456)}$  $e^{-(0.048 \times 0.448)}e^{-(0.456 \times 5.801)}$ </td></tr><tr><td></td><td> $T > T_{\text{cv}}; L > L_{\text{cv}}$ </td><td>0.059Max{0.059,  $T_{\text{cv}}/A_{(T+L)}$ }</td><td> $\rho_T^{0.048}(1 - \rho_T)^{0.761}$  $A_{(T+L)}^{(0.048 + 0.761)}$  $e^{-(0.048 \times 0.448)}e^{-(0.761 \times 5.801)}$ </td></tr></table>

For given value of $A _ { ( T + L ) }$ , the corresponding $\rho _ { T }$ is the $\rho _ { T }$ of the relevant possible region that provides the largest value of the combined impact for T and L for all relevant possible regions.

## 6. Discussion and conclusion

Our study suggests that investments in the IT stock has a positive statistically significant impact on productivity only when it exceeds a threshold value, but below this there is no positive statistically significant impact. More important than its specific value is the implication that, in general, investments in the IT stock has to surpass some minimum value before it can be expected to have a statistically significant impact on productivity.

In summary the exploration of our research questions using RS analysis suggests that depending on the conditions that applied, an unbiased observer could either conclude that investments in IT has a positive statistically significant impact on productivity, or that there is a ‘productivity’ paradox. The results thus suggest that the relationship is much more complex than that exposed in some other studies. However, these results have not contradicted the results of other studies but rather made a contribution to increasing the IS community’s understanding of the complex relationships between investments in IT and organizational performance.

It should be noted that, although our dataset has been used in several important studies on the relationship between IT investments and productivity, it has some limitations, which could affect the generalizability of our results. First, some items in the dataset are estimated while some are self-reported. Second, what is accounted for as IT investments may not be the same for all organizations. Third, data were collected on IT spending but not IT utilization and it is likely that the relationship between the two is not the same for all organizations [16]. However, researchers have been able to obtain models with strong predictive power as measured by the $R ^ { 2 }$ values. Thus previous researchers reported that their overall results were not affected by such issues. Also that our dataset covers the period 1988–1992, and it is possible that the thresholds obtained from this dataset might be different than the corresponding ones for a more recent period. An interesting question is whether the corresponding thresholds and basis function coefficients for more recent periods is higher or lower than for the 1988–1992 period, given the reduction in prices for computer hardware and software and changes in non-IT labor productivity.

## Acknowledgements

We are grateful to Professors Erik Brynjolfsson and Lorin Hitt for kindly sharing their dataset with us, thus facilitating this study.

## Appendix A. Multivariate adaptive regression splines

Multivariate adaptive regression splines approach was motivated by adaptive regression spline [9] and the recursive partitioning regression (RPR) approach. Although RPR is commonly used for multivariate function approximation, it is discontinuous at the region boundaries. Thus, MARS improved this disadvantage of RPR while it retained the adaptability of RPR [7]. MARS is highly adaptive and automatically selects locations and degree of knots. It builds a model in a two-phase process, using a forward stepwise regression selection and backwards-stepwise deletion strategy. In the first phase, MARS builds an overfitted model by adding basis functions. In the second phase, basis functions that have the least contribution to the model are deleted where removal causes the smallest increase in residual squared error and the model is optimized [10,23]. Therefore, the function obtained using the MARS approach can be described as the form:

$$
Y = \beta_ {0} + \sum_ {k = 1} ^ {K} \beta_ {k} h _ {k} (\boldsymbol {x})
$$

where $\beta _ { 0 }$ is the coefficient of the constant basis function, $\beta _ { k } ( k = 1 , \ldots , K )$ are the coefficients of the basis functions, K is the number of basis functions in the model, $h _ { k } ( { \pmb x } )$ are product of spline basis functions, i.e. $h _ { k } ( \pmb { x } ) = h _ { k } ( x _ { 1 } , \dots x _ { q } ) = \varPi _ { i j } f _ { i j } ( x _ { i } )$ where $x _ { 1 } , . . . . x _ { q }$ are the independent variables, $f _ { i j }$ is a spline basis function for the ith independent variable $x _ { i }$ at jth knot. MARS uses the basis functions in pairs of the form $( x - t ) .$ <sub>þ</sub> and $( t - x ) _ { + }$ , where t is the knot. The $" + "$ represents positive part, thus, $( x - t ) _ { + }$ means $( x - t )$ if $x > t$ or 0 if otherwise and $( t - x ) _ { + }$ means (t  x) if $x < t$ or 0 if otherwise [9,10]. MARS provides ANOVA decomposition, which identifies the relative contributions of each of the predictor variables and the interactions between variables, and handles missing values [7]. Accordingly, the MARS approach provides highly flexible and easily interpretable models [4].

In this paper, we use MARS and let the data to find the knot points, the main-effect (no interaction), and the description of the relevant basis functions.

## Appendix B. Theoretical production function

Our MARS based analysis involves the use of a Cobb–Douglas production function that has been previously used in many important studies on IT and productivity (e.g. [5,11,17,18,24]). This production function assumes that a firm uses various inputs (e.g. IT stock (T), non-computer capital (K), and non-IT labor (L)) to produce outputs (e.g. value-added (V)). Given this assumption the relevant Cobb–Douglas function can be expressed as:

$$
V = e ^ {\beta_ {0}} T ^ {\beta_ {T}} K ^ {\beta_ {K}} L ^ {\beta_ {L}}
$$

where the parameters $\beta _ { T } , \ \beta _ { K } ,$ , and $\beta _ { L }$ indicate the impact of the relevant input variable (i.e. T, K, L) on the output variable V, and represents the impact of other factors including industry. It is well known the equation above can be expressed in terms of the following log linear equation, the parameters of which can be estimated using linear regression:

$$
\log_ {\mathrm{e}} V = \beta_ {0} + \beta_ {T} \log_ {\mathrm{e}} T + \beta_ {K} \log_ {\mathrm{e}} K + \beta_ {L} \log_ {\mathrm{e}} L
$$

Similar to other studies, we also include both industry and year as input categorical variables.

## Appendix C. Determination of optimal proportion $\pmb { \rho _ { T } }$

Assuming that non-IT capital (K) is fixed and that a fixed amount $A _ { ( T + L ) }$ is available for investments in the IT stock and non-IT labor. Let $\rho _ { T }$ be the maximum proportion that of this total amount that should be invested in the IT stock in order to maximize productivity then $T = \rho _ { T } A _ { ( T + L ) }$ and $L = { \left( 1 - \rho _ { T } \right) } A _ { ( T + L ) }$ which implies that $V = { ( \rho _ { T } A _ { ( T + L ) } ) ^ { \beta _ { T } } } K ^ { \beta _ { K } } ( ( 1 - \rho _ { T } ) ^ { - }$ $A _ { ( T + L ) } ) ^ { \beta _ { L } } = \rho _ { T } ^ { \beta _ { T } } ( 1 - \rho _ { T } ) \beta _ { L } K ^ { \beta _ { K } } A _ { ( T + L ) } ^ { ( \beta T + \beta L ) }$ . For the case where the value of the optimal proportion is unconstrained (e.g. regression model), $\rho _ { T }$ provides the solution to the equation $( \mathrm { d } V / \mathrm { d } \rho _ { T } ) = 0$ . Since $( \mathrm { d } V / \mathrm { d } \rho _ { T } ) = ( - \beta _ { L } \rho _ { T } ^ { \beta _ { T } } ( 1 - \rho _ { T } ) ^ { ( \beta _ { L } - 1 ) } + \dot { \beta } _ { T } \rho _ { T } ^ { ( \beta _ { T } - 1 ) } ) ( 1 -$ $\rho _ { T } ) ^ { \beta _ { L } } K ^ { \beta _ { K } } A _ { ( T + L ) } ^ { ( \beta T + \beta L ) }$ it follows that $\rho _ { T } = \beta _ { T } / ( \beta _ { T } + \beta _ { L } )$ for the case where the optimal proportion is unconstrained. For the case where the value of the optimal proportion is constrained (e.g. regression splines models), the point $\beta _ { T } / ( \beta _ { T } + \beta _ { L } )$ could be infeasible in which case the optimal proportion would be on the boundary of the relevant region.

## References

[1] A. Bharadwaj, A resource-based perspective on information technology capability and firm performance: an empirical investigation, MIS Quarterly 24 (1), 2000, pp. 169–196.

[2] E. Brynjolfsson, The productivity paradox of information technology, Communications of the ACM 36 (12), 1993, pp. 66–76.

[3] E. Brynjolfsson, L.M. Hitt, Paradox lost? Firm-level evidence on the returns to information systems spending, Management Science 42 (4), 1996, pp. 541–558.

[4] D.G.T. Dennison, B.K. Mallick, A.F.M. Smith, Bayesian MARS, 1997.

[5] S. Dewan, C.K. Min, The substitution of information technology for other factors of production: a firm level analysis, Management Science 43 (12), 1997, pp. 1660– 1675.

[6] R.L. Eubank, in: D.B. Owen, R.G. Cornell, A.M. Kshirsagar, W.J. Kennedy, E.G. Schilling (Eds.), Spline Smoothing and Nonparametric Regression, Marcel Dekker, New York, 1988.

[7] J.H. Friedman, Multivariate adaptive regression splines (with discussion), The Annals of Statistics 19 (1), 1991, pp. 1–141.

[8] R. Garretson, Greenspan hails technology spending, Info-World 21 (21), 1999, pp. 32.

[9] T.J. Hastie, R.J. Tibshirani, Generalized Additive Models, Chapman & Hall, London, 1990.

[10] T.J. Hastie, R.J. Tibshirani, J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Springer-Verlag, New York, 2001.

[11] L.M. Hitt, E. Brynjolfsson, Productivity, business profitability, and consumer surplus: three different measures of information technology value, MIS Quarterly 20 (2), 1996, pp. 121–142.

[12] J. Jurison, Reevaluating productivity measures, Information Systems Management (1997) 30–34.

[13] W.R. King, IT-enhanced productivity and profitability, Information Systems Management (1998) 64–66.

[14] H. Kivijarvi, T. Saarinen, Investment in information systems and the financial performance of the firm, Information and Management 28, 1995, pp. 143–163.

[15] B. Lee, N. Menon, Information technology value through different normative lenses, Journal of Management Information Systems 16 (4), 2000, pp. 99–119.

[16] C. Lee, Modeling the business value of information technology, Information and Management 39, 2001, pp. 191–210.

[17] F. Lichtenberg, The output contributions of computer equipment and personnel: a firm-level analysis, Journal of Economic Innovation and New Technologies 3 (4), 1995, pp. 201–217.

[18] G.W. Loveman, An assessment of the productivity impact of information technologies, in: T.J. Allen, M.S. Scott Morton (Eds.), Information Technology and the Corporation of the 1990s: Research Studies, Oxford University Press, Oxford, 1994, pp. 84–110.

[19] M. Mahmood, G.J. Mann, Measuring the organizational impact of information technology investment: an exploratory study, Journal of Management Information Systems 10 (1), 1993, pp. 97–122.

[20] M.K. McGee, Its official: IT adds up, Information Week (2000) 42.

[21] A. Rai, R. Patnayakuni, N. Patnayakuni, Technology investment and business performance, Communications of the ACM 40 (7), 1997, pp. 89–97.

[22] Salford Systems, MARS for Windows, Version 2.0, 2000.

[23] Salford Systems, MARS User Guide, San Diego, CA, 1999.

[24] B. Shao, Investigating the value of information technology in productive efficiency: an analytic and empirical study, Ph.D. dissertation, State University of New York, Buffalo, 2000.

[25] B. Shao, W. Lin, Technical efficiency analysis of information technology investments: a two-stage empirical investigation, Information and Management 39, 2002, pp. 391–401.

[26] B. Shao, W. Lin, Examining the determinants of productive efficiency with IT as a production factor, Journal of Computer Information Systems 41 (1), 2000, pp. 25–30.

[27] B. Shao, W. Lin, Measuring the value of information technology in technical efficiency with stochastic production frontiers, Information and Software Technology 43, 2001, pp. 447–456.

[28] W. Shu, Will the new economy emerge as information technology pays off? Journal of Association for Information Systems 2 (1), 2001, pp. 1–23.

[29] S. Sircar, J.L. Turnbow, B. Bordoloi, The impact of information technology investments on firm performance: a review of the literature, Journal of Engineering Valuation and Cost Analysis 1, 1998, pp. 171–181.

[30] S. Sircar, J.L. Turnbow, B. Bordoloi, A framework for assessing the relationship between information technology investments and firm performance, Journal of Management Information Systems 16 (4), 2000, pp. 69–97.

[31] T. Stratopoulos, B. Dehning, Does successful investment in information technology solve the productivity paradox? Information and Management 38, 2000, pp. 103–117.

[32] P. Weill, The relationship between investment in information technology and firm performance: a study of the valve manufacturing sector, Information Systems Research 3 (4), 1992, pp. 307–333.

![](/api/attachments/ANVR752M/fulltext/images/613a89ab049c89c7f9fd1aea803b5ad589e7132fb3c3bce4539022e0ea7dccb4.jpg)  
Kweku-Muata Osei-Bryson is professor of information systems at Virginia Commonwealth University since Fall 1998. Previously he was professor of

information systems and decision analysis in the School of Business at Howard University, Washington, DC, USA. He has also worked as an information systems practitioner in both industry and government. He does research in various areas including: data mining, expert systems, decision support systems, group support systems, information systems outsourcing, multi-criteria decision analysis. His papers have been published in various journals including: IEEE Transactions on Knowledge & Data Engineering, Data & Knowledge Engineering, Information & Software Technology, Decision Support Systems, Information Processing and Management, Computers & Operations Research, European Journal of Operational Research, Journal of the Operational Research Society, Journal of the Association for Information Systems, Journal of Multi-Criteria Decision Analysis, Applications of Management Science. Currently he serves an associate editor of the INFORMS Journal on Computing, and is a member of the editorial board of the Computers & Operations Research journal.

![](/api/attachments/ANVR752M/fulltext/images/f3829d6243748386be5f4d89a5b323777cf4f948ad10d2009fd3c58ce85b4fdc.jpg)

Myung S. Ko is currently an assistant professor in the Department of Information Systems at the College of Business, University of Texas at San Antonio. Dr. Ko received her PhD in information systems from the Virginia Commonwealth University. She holds MA in accounting. Her research interests include impact of IT on organizations, business value of IT, data mining, and accounting information systems.
