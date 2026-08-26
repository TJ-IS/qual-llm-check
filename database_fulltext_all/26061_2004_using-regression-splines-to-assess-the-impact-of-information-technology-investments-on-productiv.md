---
otero_id: 26061
otero_key: "CYHSB7GW"
title: "Using regression splines to assess the impact of information technology investments on productivity in the health care industry"
authors: "Myung Ko; Kweku‐Muata Osei‐Bryson"
year: "2004"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.2004.00160.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using regression splines to assess the impact of information technology investments on productivity in the health care industry

Myung Ko\* & Kweku-Muata Osei-Bryson<sup>†</sup>

\*Department of Information Systems, College of Business, The University of Texas at San Antonio, San Antonio, TX 78249, USA, email: Mko@utsa.edu, and <sup>†</sup>Department of Information Systems and The Information Systems Research Institute, Virginia Commonwealth University, Richmond, VA 23284, USA, email: Kweku.Muata@isy.vcu.edu

Abstract. This paper explores the impact of information technology (IT) investments on productivity using a new technique, multivariate adaptive regression splines (MARS). We believe that it provides additional insights on the nature of the impact of IT investments on productivity. The results from our study are compared with findings from a previous study that has also used the same data set. While the results of a previous study indicate that IT investments have a positive but uniform impact on productivity, our study suggests that the impact of IT on productivity is not uniform but is contingent on other complementary factors. Our findings describe that the complementary relationship exists between IT and non-IT related investments. Thus, improved organizational productivity cannot be expected from investment in IT alone but only together with non-IT investments. Our findings also point out that further investment may not necessarily bring on higher organizational productivity.

Keywords: information technology investments, productivity, regression, regression splines, data mining, MARS

## 1. INTRODUCTION

Substantiating the business value of information technology (IT) on organizational productivity has been a major concern of information system (IS) research. In 2002, Morgan Stanley reported that US companies wasted \$130 billion in the previous 2 years on technology (Ward, 2002). While organizations have increased investments in IT in order to improve organizationa performance, findings from earlier IT productivity studies have been inconclusive despite the fact that several recent firm-level empirical studies have found a positive relationship between IT investments and organizational performance.

A major objective of our study is to explore the impact of IT investment on productivity at the firm level using a new technique. Although many studies have investigated the impact of IT investment, our study provides different perspectives from previous studies in several ways. First, we take another look at the impact of IT investments on productivity using a relatively new data mining technique – multivariate adaptive regression splines (MARS)<sup>1</sup> – which we believe provides a highly interpretable and informative model. Most previous IT productivity studies have been conducted using approaches based on econometrics or data envelopment analysis. We believe our approach offers additional insights on the nature of the impact of IT investments on productivity. Second, our empirical study is based on one industry, specifically the health care industry, whereas the majority of previous studies are based on a mix of industries. Using a data set of one industry has the advantage of analysing one industry in-depth and also of reducing any confounding factors caused from a mix of industries. Last, findings from our study are compared with the results obtained from another study that used the same data set (Menon et al., 2000) in order to demonstrate additional insights obtained by using a different technique.

We believe that the results of our study advance IT productivity research by providing additional insights for understanding the complexity of IT productivity issues. While the results of a prior study indicate that IT investments have a positive but uniform impact on productivity, our findings suggest that this impact is not uniform but is contingent on other complementary factors.

The remainder of the paper is organized as follows. The next section provides a brief overview regarding previous research on the contribution of IT to productivity at the firm level. Section 3 describes IT developments in health care and Section 4 describes the data set and variables. Section 5 discusses the production function and Section 6 introduces the research methodology used in this study, a regression spline (RS) approach. Section 7 includes the empirical results and Section 8 discusses the conclusions and limitations of this paper.

## 2. OVERVIEW ON PREVIOUS RESEARCH

Many previous studies have examined the impact of IT investments on productivity at the firm level. Loveman (1994) used the Cobb-Douglas production function in his study but did not find any evidence of productivity increase from IT investment.

Some of the previous studies indicated mixed results. Weill (1992) found that transactiona IT investments had a positive impact on firm performance, whereas strategic IT or informational IT did not. Prasad & Harker (1997) found that IT labour produced high returns in productivity, whereas IT capital did not. Also, Lee & Menon (2000) found that IT capital was associated with increased productivity in the health care industry, whereas IT labour was not. Menon et al. (2000) found that non-IT labour demonstrated the highest positive impact on productivity in the health care industry. In their study, IT labour and medical IT capital contributed positively to productivity, while non-IT capital demonstrated a negative impact on productivity. Smith et al. (2000) used the data that were collected by the Medical Group Management Asso ciation and examined IS investments, medical service organization affiliations, and the numbe of physicians per clinic in order to measure health care performance, such as gross charges per physician, net revenue per physician, total operating cost per physician and operating margin. While the authors found that investment in IS is negatively associated with net revenue in the health care industry and negatively associated with operating cost among multi-specialty groups in 1995 and 1997, they did not ascertain any statistical significance for the financial performance measures in 1996.

On the other hand, some recent studies have found positive results. Lichtenberg (1995) found substantial ‘excess returns’ for both computer capital and IS labour. Lichtenberg claimed that marginal productivity of IS labour is six times as much as that of non-IT labour. Barua et al. (1995) proposed a process-oriented approach and empirically tested it using a two-stage analysis. They found that many significant IT impacts occur at the immediate level and can be traced to some IT impacts at higher-level performance variables. Brynjolfsson & Hitt (1996) examined the impact of IT on productivity, business profitability and consumer value. They found that IT spending has a positive impact on productivity and provided significant value for consumers. However, their analysis did not show any evidence of improvement in business profitability. Dewan & Min (1997) found that IT capital is a net substitute for both ordinary capital and labour. Francalanci & Galal (1998) examined the impact of IT investments and worker composition on the productivity of life insurance companies. The authors found that increases in IT investments are associated with productivity benefits when accompanied by changes in worker composition. Shao & Lin (2001) also found that the impact of IT investments on organizational productivity is positive. Mukhopadhyay et al. (1997) investigated the mail sorting process at 46 mail processing centres at the United States Postal Service. The authors found that IT has a positive impact on the mail sorting process. They also found that IT improves quality, which, in turn, increases total output. Devaraj & Kohli (2000) examined the relationship between IT investments and organizational profitability in the health care industry and found that IT investments have an impact on profitability after 3 months or more because of lag effects. They also found that IT investment improves the quality of products and services. Given that recent empirical studies on IT productivity have found that IT investments have a positive impact on organizational productivity, the following hypothesis is proposed:

H1: Investments in IT lead to increased productivity in health care organizations.

As we described earlier, all of the previous studies have found either a positive or a negative impact on organizational productivity, therefore the following related hypothesis is also proposed:

H2: The impact of IT investments on productivity in health care organizations is uniform

Table 1 includes the summary of the previous empirical firm-level studies for the impact of IT investment on productivity.

<table><tr><td colspan="4">Table 1. Summary of firm-level studies of the IT investment impact on organizational productivity</td></tr><tr><td>Study</td><td>Research method</td><td>Sample size/period</td><td>Findingss</td></tr><tr><td>Weill (1992)</td><td>Regression analysis</td><td>33/1982–87</td><td>Transactional IT: ↑Strategic or Informational IT: ↔</td></tr><tr><td>Loveman (1994)</td><td>Regression analysis</td><td>60/1978–84</td><td>Productivity: ↔</td></tr><tr><td>Lichtenberg (1995)</td><td>Regression analysis</td><td>Not reported/1988–91</td><td>Computer Capital, IS Labour and Productivity: ↑</td></tr><tr><td>Barua et al. (1995)</td><td>Regression analysis</td><td>60 strategic business units (SBU)/1979–83 with some from 1978 to 1984</td><td>Significant positive impacts of IT at the intermediate level in the organization.</td></tr><tr><td>Hitt &amp; Brynjolfsson (1996)</td><td>Ordinary least squares (OLS), the iterated seemingly unrelated regression (ISUR)</td><td>1109/1988–92</td><td>IT and Productivity: ↑IT and Consumer Value: ↑</td></tr><tr><td>Dewan &amp; Min (1997)</td><td>Non-linear least squares and OLS regressions</td><td>1131/1988–92</td><td>IT Capital is a substitute for both Capital and Labour.</td></tr><tr><td>Prasad &amp; Harker (1997)</td><td>Two-step OLS regression</td><td>47/1993–95</td><td>IT Labour and Productivity: ↑IT Capital and Productivity: ↔ or ↓</td></tr><tr><td>Mukhopadhyay et al. (1997)*</td><td>Stochastic production frontier</td><td>1794/over 3 years (39 accounting periods)</td><td>IT and Output: ↑IT and Quality: ↑</td></tr></table>

<table><tr><td>Francalanci &amp; Galal (1998)</td><td>Regression analysis</td><td>520/1986–95</td><td>IT (and changes in worker composition) and Productivity: ↑</td></tr><tr><td>Shao &amp; Lin (2001)</td><td>Stochastic production frontier/data envelopment analysis (DEA)</td><td>1115/1988–92</td><td>IT and Technical Efficiency: ↑ thus, IT and Productivity: ↑</td></tr><tr><td>Lee &amp; Menon (2000)</td><td>Multivariate analysis of variance, cluster analysis</td><td>1064/1976–94</td><td>IT Capital and Productivity: ↑IT Labour and Productivity: ↓</td></tr><tr><td>Menon et al. (2000)</td><td>The stochastic frontier</td><td>1064/1976–94</td><td>Between Non-IT Labour, IT Labour, IT Capital, Medical IT Capital and Productivity: ↑Non-IT Capital and Productivity: ↓</td></tr><tr><td>Devaraj &amp; Kohli (2000)</td><td>Field study/time series</td><td>Eight hospital/a recent 36 months (not specified)</td><td>IT and Profitability: ↑ (after 3 months or more)IT and Quality of Products and Services: ↑The effect of (BPR &amp; IT) and Profitability: ↑</td></tr><tr><td>Smith et al. (2000)</td><td>Ordinary least squares regressions</td><td>Varies (year to year and variable to variable – from 252 to 663)/1995–97</td><td>IT and Net Revenue:1995: ↓ 1996: ↔ 1997: ↓IT and Operating Cost:1995: ↓ 1996: ↔ 1997: ↓</td></tr></table>

\*Their analysis is at application level. BPR, Business Process Reengineering; ≠, positive relationship; , no effect; Ø, negative relationship.
´

## 3. IT DEVELOPMENTS IN HEALTH CARE

Rapid increases in health care costs have led to significant changes in the US health care system. In order to reduce the overall Medicare spending, federal legislation established a prospective payment system (PPS) in 1983. PPS utilizes Diagnosis Related Groups (DRGs), which provide a way to classify patients into categories and set a maximum amount that would be reimbursed for each category of Medicare patients. Before 1983, hospitals were reimbursed for the service performed on patients. However, this reimbursement scheme was changed after DRGs were implemented. Because the hospital would be paid the same for patients in the same category, hospitals were given an incentive to keep costs down by establishing more efficient operations (Sumner & Moreland, 1995).

Compared with other industries, the health care industry has been perceived as being slow in implementing IT (Raghupathi, 1997). However, this situation has been changing in recent years as investment in IT has increased continuously in the 1990s. The major reasons for this increase include the desire to improve the quality of patient care, the need to respond to government pressure to reduce costs, and the need to upgrade medical IS (Dash, 1997; Raghupathi, 1997; Smith et al., 2000; Bose, 2003).

The health care IS field can be categorized into administrative and clinical systems. Administrative IS are mainly used for administrative purposes such as processing claims transactions, profiling physicians and tracking health plan enrolment. Clinical IS are mainly used to improve the quality of health care and to increase the performance of health care providers (Anderson, 1997; Wholey et al., 2000; Bose, 2003). Recently, the health care industry has become aware that both administrative and clinical systems have to be integrated to effectively manage health care. Yet, developing clinical systems and integrating the two systems are challenging tasks (Grimson et al., 2000).

During the last several years, internet technology and web-enabled applications have changed the traditional structure of the health care industry. Thus, the new term ‘e-health’ relates to approaches for using these new technologies in order to achieve improved access, reduced costs and/or improved revenue and improved patient satisfaction (Bose, 2003). Using the internet, costs of health insurance claims can be reduced to less than \$1 per claim, compared with \$10 to \$15 using a paper-based claim process (Danzon & Furukawa 2001). Furthermore, ehealth can not only be used for cutting costs but also for improving the quality and effectiveness of health care. Using electronic medical record systems, health care providers can access the patient’s medical history and make clinical decisions quickly. This reduces errors and any duplication of care. On the other hand, because of the sensitive nature of medical information, protecting patients’ privacy and security is also a major challenge for the health care industry.

## 4. DESCRIPTION OF THE DATA SET

We used a data set that has been used previously in another study on the IT productivity in the health care industry (Menon et al., 2000). The data were collected by the Washington State

Department of Health, which includes all hospitals in the state of Washington except specialized hospitals such as psychiatric and substance abuse treatment centres. Thus, the data set only includes observations for general medical and surgical hospitals. This ensures that the sample is a highly homogeneous one (Menon & Lee, 2000). Overall, the data set consists of $1 1 3 0 ^ { 2 }$ observations from 63 different hospitals for the years 1975–94 and, thus, is an unbalanced panel. Each observation represents charges and costs incurred by each hospital per year.

The data set includes 83 financial cost centres that can be categorized into three major areas – revenue-generating accounts, ancillary accounts and non-revenue-generating accounts. The first category is revenue-generating accounts. This includes accounts that provide services to inpatients for room and board functions. Intensive care and acute care also belong to this category. The second category is ancillary accounts, which includes accounts that provide services to inpatients and outpatients; examples of these accounts are emergency room and radiology. The third category is non-revenue-generating accounts, which includes accounts that provide services only; examples of these accounts are accounting, purchasing and admitting. The data include all charges and costs, which were accumulated by the account number for each hospital for a period from 1975 to 1994. Charges represent the total amount billed for patient services, not considering any reimbursement. Costs represent expenses incurred for the period and they include salaries and wages, employee benefits, supplies, and rental and lease expenses.

For this data set the input production variables are IT Capital, Medical IT Capital, Non-IT Capital, IT Labour and Non-IT Labour. Table 2 provides descriptions of these variables as well as the output production variable, Adjusted Patient Days. It should be noted that given the dif ficulty in defining an output performance measure for the health care industry, Adjusted Patient Days has been offered as a useful proxy for hospital output in previous studies (Maclean & Mix, 1991; Menon et al., 2000).

## 5. THE PRODUCTION FUNCTION

The theory of production assumes that a firm uses various inputs to produce its outputs based on the rules specified by the firm’s production function (Henderson & Quandt, 1980). Many previous studies that have explored the contribution of IT investments to productivity have also used this theoretical base (e.g. Loveman, 1994; Hitt & Brynjolfsson, 1996; Dewan & Min, 1997; Shao, 2000). For this study the output (Q) is the hospital’s Adjusted Patient Days (see Table 2) and the input variables are Non-IT Capital (K), IT Capital (T), Medical IT Capital (M), Non-IT Labour (L) and IT Labour (S). Because we assume that a hospital’s Adjusted Patient Days (Q) depends on the use of Non-IT Capital (K), IT Capital (T), Medical IT Capital (M), Non-IT Labour (L) and IT Labour (S), our production function has the following form:

Table 2. Variable definitions

<table><tr><td>Variable</td><td>Description (or departmental account)</td></tr><tr><td>Adjusted Patient Days (Q)</td><td>Sum of Inpatient Days and Outpatient Days. Outpatient Days are derived by dividing outpatient revenue by inpatient revenue per day. Deflated by the Output Price (see below).</td></tr><tr><td>IT Capital (T)</td><td>Capital expenses incurred in administrative non-revenue-generating accounts such as Data Processing, Communications, Admitting, Patient Accounts, Central Services, Purchasing, Accounting, Medical Records, Personnel, Medical Library, Medical Staff and Utilization Management. Deflated by Price Deflator for Fixed Investment for IT from WEFA (1994).</td></tr><tr><td>Medical IT Capital (M)</td><td>Capital expenses incurred in ancillary accounts that use the equipment for diagnosing and therapeutics such MRI, CT Scanning Services, Surgical Services, Recovery Room, Anesthesiology, IV Therapy Services, Electrodiagnosis, Radiology-Diagnostic, Radiology-Therapeutic, Emergency Room, Nuclear Medicine, Electromyography, Lithotripsy, Organ Acquisitions, Outpatient Chemical Deposit. Deflated by Price Deflator for Fixed Investment for IT from WEFA (1994).</td></tr><tr><td>Non-IT Capital (K)</td><td>Capital expenses incurred in revenue-generating accounts such as Intensive/Coronary Care, Semi-Intensive Care, Acute Care, Physical Rehabilitation, Psychiatric, Nursery, Labouratory, Pharmacy, Home Care Services and any remaining accounts. Deflated by Price Deflator for Fixed Investment for Non-IT from WEFA (1994).</td></tr><tr><td>IT Labour (S)</td><td>Salaries and employee benefits charged to IT Capital accounts. Deflated by Labour Price (see below).</td></tr><tr><td>Non-IT Labour (L)</td><td>Salaries, employee benefits, and physicians&#x27; salaries charged to accounts other than IT Capital accounts. Deflated by Labour Price (see below).</td></tr><tr><td>Labour Price</td><td>Employment Price Index for health care services from Bureau of Labour Statistics (BLS) (1995).</td></tr><tr><td>Output Price</td><td>Consumer Price Index for health care services from WEFA (1994).</td></tr></table>

WEFA, Wharton Econometric Forecasting Associates; MRI, megnetic resonance imaging.  
Source: Menon et al. (2000) and Menon’s SAS Programme

$$
Q = f (K, T, M, L, S)\tag{1}
$$

While the simplest and most widely used production function is the Cobb-Douglas function, the Translog production function, which is a generalization of the Cobb-Douglas functional form, has also been used because it allows for the exploration of interactions between the input variables. By relaxing the constraints of the substitution assumptions and allowing no restriction on returns to scale, the Translog function is a more flexible functional form although it presents more parameters than Cobb-Douglas (Evans et al., 2000). In general, the Translog function has the following form:

$$
\log_ {\mathrm{e}} Q = \log_ {\mathrm{e}} \gamma_ {0} + \sum_ {i} \alpha_ {i} \log_ {\mathrm{e}} v _ {i} + ^ {1 / 2} \sum_ {i} \sum_ {j} \beta_ {i j} \log_ {\mathrm{e}} v _ {j} \log_ {\mathrm{e}} v _ {i}\tag{2}
$$

where $V _ { i } \dots . . \ V _ { n }$ are the firm’s inputs; and $\beta _ { i j } = \beta _ { j i }$ for all $i , j .$

In this study, our analysis is based on the Translog production function. However, we use RS analysis. an alternative technigue, which we believe offers additional valuable insights for understanding the complex relationships between IT investments and productivity in the health care industry.

The relevant Translog function that applies to our production function as shown in Equation (1) can be expressed as:

$$
\begin{array}{l} \log_ {e} Q = \gamma_ {0} + \alpha_ {K} \log_ {e} K + \alpha_ {T} \log_ {e} T + \alpha_ {M} \log_ {e} M + \alpha_ {L} \log_ {e} L + \alpha_ {S} \log_ {e} S + 1 / 2 \beta_ {K K} (\log_ {e} K) ^ {2} \\ \quad + 1 / 2 \beta_ {T T} (\log_ {e} T) ^ {2} + 1 / 2 \beta_ {M M} (\log_ {e} M) ^ {2} + 1 / 2 \beta_ {L L} (\log_ {e} L) ^ {2} + 1 / 2 \beta_ {S S} (\log_ {e} S) ^ {2} \\ \quad + \beta_ {K T} \log_ {e} K \log_ {e} T + \beta_ {K M} \log_ {e} K \log_ {e} M + \beta_ {K L} \log_ {e} K \log_ {e} L + \beta_ {K S} \log_ {e} K \log_ {e} S + \beta_ {T M} \log_ {e} T \log_ {e} M \\ \quad + \beta_ {T L} \log_ {e} T \log_ {e} L + \beta_ {T S} \log_ {e} T \log_ {e} S + \beta_ {M L} \log_ {e} M \log_ {e} L + \beta_ {M S} \log_ {e} M \log_ {e} S \\ \quad + \beta_ {L S} \log_ {e} L \log_ {e} S \end{array}\tag{3}
$$

## 6. OVERVIEW OF REGRESSION SPLINES

Compared with regression equations that attempt to model the relationship between the dependent and input variables using a single function (e.g. linear, log linear) of the input vari ables by describing the contribution of each predictor (independent) variable with a single coef ficient, an RS approach models the relationship using a piecewise polynomial function, such as piecewise continuous linear functions (linear splines) or piecewise cubic functions with con tinuous derivative of input variable (Hastie & Tibshirani, 1990).

In regression equations, higher order terms $( \mathsf { i } . \mathsf { e } . x ^ { 2 } , x ^ { 3 }$ , etc.) may be introduced to capture any relevant non-linearity, but the coefficients of these terms will be estimated using the data globally and, thus, local features of the true function might not be captured (Hastie & Tibshirani, 1990). On the other hand, in the RS approach, a piecewise polynomial function $f ( x )$ can be obtained by dividing the range of each input variable into one or more intervals and representing function ƒ by a separate polynomial in each interval (Hastie et al., 2001). Thus, splines are described as piecewise polynomials whose segments have been joined together smoothly at the knots (Eubank, 1988), where a knot specifies the end of one region of data and the beginning of another (Steinberg et al., 1999). An RS function can be expressed as a linear combination of piecewise polynomial basis functions (BF) that are joined together smoothly at the knots, and the coefficients of the basis function are estimated by minimizing the sum of square errors. Because this process is identical to the estimation process of regression, this estimated spline is called the ‘regression spline’. Because the segmented nature of piecewise polynomials adjusts more effectively to local characteristics of a function or data, they provide more flexibility than polynomials. RS performs a polynomial fit in each region with constraints at the knots by utilizing the least squares criterion. Accordingly, the parameters of the regression functions change from one region to another.

The MARS approach was motivated by adaptive RS (Hastie & Tibshirani, 1990) and the recursive partitioning regression (RPR) approach (Breiman et al., 1984). Although RPR is commonly used for multivariate function approximation, it is discontinuous at the region boundaries. MARS improved this disadvantage of RPR while retaining the adaptability of RPR (Friedman, 1991). MARS is highly adaptive and automatically selects locations and the degree of knots. It builds a model in a two-phase process, using a forward stepwise regression selection and backward stepwise deletion strategy. In the first phase, MARS builds an over-fitted model by adding basis functions. In the second phase, basis functions that have the least contribution to the model are deleted and the model is optimized (Steinberg et al., 1999). Therefore, the function obtained using the MARS approach can be described as the form:

$$
Y = \beta_ {0} + \sum_ {k = 1} ^ {K} \beta_ {k} h _ {k} (x)
$$

where $\beta _ { 0 }$ is the coefficient of the constant basis function, $\beta _ { k } ( i = 1 , \dots , \kappa )$ are the coefficients of the basis functions, K is the number of basis functions in the model, $h _ { k } ( x )$ are the products of spline basis functions, i.e. $h _ { k } ( \boldsymbol { x } ) = h _ { k } \left( x _ { 1 } , . . . , x _ { q } \right) = \Pi _ { i j } f _ { i j } ( x _ { i } )$ where $f _ { i j } ( x )$ is spline basis function. MARS uses the basis functions in pairs of the form $( x - t )$ and $( t - x )$ where t is the knot. The ‘+’ represents the positive part, thus $( x - t ) _ { + } = \mathsf { m a x } ( 0 , x - t )$ , i.e. $( x - t )$ if $x > t$ or 0. Also, (t $\boldsymbol { x } ) _ { + } = \mathrm { m a x } ( 0 , t - \boldsymbol { x } )$ , i.e. (t  x) if $x < t$ or 0 if otherwise (Hastie & Tibshirani, 1990; Hastie et al., 2001).

MARS provides decomposition, which identifies the relative contributions of each of the input variables and the interactions between these variables. It also handles missino values by constructing ‘surrogate variables’. First, MARS develops the best model possible using the observations without missing values. For each variable with missing values, MARS creates a sub-model based on a surrogate or surrogates. For example, MARS may develop a model based on income data. In addition, a sub-model based on education and age is created for use when the value from income is missing because the model indicated education and age are surrogate variables, which happen to represent the best predictors for income in this example. Thus, it can be observed that the higher correlation between the missing predictor and the other predictors, the smaller the loss of information because of the missing value (Friedman, 1991; Steinberg et al., 1999; Kuhnert et al., 2000; Hastie et al., 2001).

A MARS model can be generated allowing either no interaction between the input variables or permitting interactions between variables. MARS models that involve interactions between variables have a hierarchical, tree-like structure, with parent and child relationships between basis functions. Previous researchers have reported that prediction results using MARS are more accurate than artificial neural networks (De Veaux et al., 1993; Briand et al., 2000b; Abraham & Steinberg, 2001).

Although MARS has not been used in previous studies by other researchers on IT and productivity, this technique has been successfully applied in various fields including software engineering (e.g. Briand et al., 2000a,b), electrochemistry (e.g. Carey & Yee, 1992), geography (e.g. Abraham & Steinberg, 2001), communication (e.g. Ekman & Kubin, 1999), chemical studies (e.g. De Veaux et al., 1993; Nguyen-Cong et al., 1996), cancer research (e.g. Mallick et al., 1997), genetics (York & Eaves, 2001), engineering (e.g. Jin et al., 2000), geochemistry (e.g. Griffin et al., 1997), epidemiology (e.g. Kuhnert et al., 2000), finance (e.g. Abraham, 2002) and biological sciences (e.g. Prasad & Iverson, 2000).

## 7. EMPIRICAL RESULTS AND DISCUSSION

## 7.1. Results from this study

## 7.1.1. Description of the results

We used the MARS software (version 2.0) by Salford Systems (2000) to generate an RS model that allowed two-way interactions between the input variables. Setting the maximum basis function parameter to the default value of 15, the resulting model had an R-squared value of 0.91, suggesting that it had high predictive power. Table 3 describes the order of importance of the input variables to this model.

Table 4 describes the generated RS model, which consists of 11 basis functions and their coefficients. Some basis functions BF4 and BF12 do not have coefficients because they only exist as part of other basis functions (e.g. BF5, BF6, BF7 and BF13). If the sign of the coefficient of a basis function is the same as the sign of the variable in that basis function (e.g. BF1 and BF2), then the contribution of the given input variable in terms of that basis function is pos itive, whereas if the corresponding signs are different, then the contribution of a given input variable in terms of that basis function is negative (e.g. BF3 and BF5). Table 4 also identifies the knots for our input variables. The knots for Non-IT Labour (L) are represented by $L _ { c v 1 } , L _ { c v 2 }$ and $L _ { c v 3 }$ where $\mathsf { l o g } _ { \mathrm { e } } ( L _ { c v 1 } ) = 1 6 . 7 1 2 , \mathsf { l o g } _ { \mathrm { e } } ( L _ { c v 2 } ) = 1 5 . 3 4 1$ and l $0 9 _ { \mathrm { e } } ( L _ { c v 3 } ) = 1 3 . 4 7 3$ ; the knot for Non-IT Capital(K) is represented by $K _ { c v 1 }$ where log $_ { ( K _ { c v 1 } ) } = 1 2 . 2 4 0$ ; the knots for IT Labour (S) are represented by $S _ { c v 1 }$ and $S _ { c v 2 }$ where $\log _ { \mathrm { e } } ( S _ { c v 1 } ) = 1 2 . 9 8 6$ and $\mathsf { l o g } _ { \mathrm { e } } ( S _ { c v 2 } ) = 1 3 . 6 4 9 ;$ ; the knot for IT Capital (T) is represented by $T _ { c v 1 }$ where $\mathsf { l o g } _ { \mathrm { e } } ( T _ { c v 1 } ) = 1 4 . 2 7 6 ;$ ; and the knot for Medical IT Capita (M) is represented by $M _ { c v 1 }$ where $\mathsf { l o g } _ { \mathrm { e } } ( M _ { c v 1 } ) = 1 1 . 3 3 8$

Table 3. Relative importance of the input variable

<table><tr><td>Name of variable</td><td>Variable</td><td>Cost of omission</td><td>Importance</td></tr><tr><td>Non-IT Labour</td><td> $\log_eL$ </td><td>0.192</td><td>100.000</td></tr><tr><td>Non-IT Capital</td><td> $\log_eK$ </td><td>0.097</td><td>48.462</td></tr><tr><td>IT Labour</td><td> $\log_eS$ </td><td>0.078</td><td>28.881</td></tr><tr><td>IT Capital</td><td> $\log_eT$ </td><td>0.074</td><td>23.007</td></tr><tr><td>Medical IT Capital</td><td> $\log_eM$ </td><td>0.069</td><td>10.600</td></tr></table>

Table 4. The final model from MARS

<table><tr><td></td><td>Basis function</td><td>Coefficient</td><td>Variable</td><td>Parent</td><td>Knot</td></tr><tr><td>0</td><td></td><td>10.990</td><td></td><td></td><td></td></tr><tr><td>1</td><td>BF1 = max(0,  $\log_eL - 16.712$ )</td><td>1.391</td><td> $\log_eL$ </td><td></td><td>16.712</td></tr><tr><td>2</td><td>BF2 = max(0, 16.712 –  $\log_eL$ )</td><td>-1.256</td><td> $\log_eL$ </td><td></td><td>16.712</td></tr><tr><td>3</td><td>BF3 = max(0,  $\log_eK - 12.240$ )</td><td>-0.373</td><td> $\log_eK$ </td><td></td><td>12.240</td></tr><tr><td>4</td><td>BF4 = max(0, 12.240 –  $\log_eK$ )</td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>BF5 = max(0,  $\log_eL - 15.341$ * BF4</td><td>-1.277</td><td> $\log_eL$ </td><td> $\log_eK$ </td><td>15.341</td></tr><tr><td>6</td><td>BF6 = max(0, 15.341 –  $\log_eL$ * BF4</td><td>0.209</td><td> $\log_eL$ </td><td> $\log_eK$ </td><td>15.341</td></tr><tr><td>7</td><td>BF7 = max(0,  $\log_eS - 12.986$ * BF4</td><td>0.807</td><td> $\log_eS$ </td><td> $\log_eK$ </td><td>12.986</td></tr><tr><td>9</td><td>BF9 = max(0,  $\log_eT - 14.276$ )</td><td>0.206</td><td> $\log_eT$ </td><td></td><td>14.276</td></tr><tr><td>10</td><td>BF10 = max(0, 14.276 –  $\log_eT$ )</td><td>0.169</td><td> $\log_eT$ </td><td></td><td>14.276</td></tr><tr><td>11</td><td>BF11 = max(0,  $\log_eS - 13.649$ )</td><td>0.956</td><td> $\log_eS$ </td><td></td><td>13.649</td></tr><tr><td>12</td><td>BF12 = max(0, 13.649 –  $\log_eS$ )</td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td>BF13 = max(0,  $\log_eM - 11.338$ * BF12</td><td>1.112</td><td> $\log_eM$ </td><td> $\log_eS$ </td><td>11.338</td></tr><tr><td>15</td><td>BF15 = max(0,  $\log_eL - 13.473$ * BF11</td><td>-0.194</td><td> $\log_eL$ </td><td> $\log_eS$ </td><td>13.473</td></tr></table>

Given these basis functions and their coefficients described in Table 4, the regression equation can be expressed as follows:

$$
\begin{array}{r l} \log_ {e} Q & = 1 0. 9 9 0 + 1. 3 9 1 * B F 1 - 1. 2 5 6 * B F 2 - 0. 3 7 3 * B F 3 - 1. 2 7 7 * B F 5 + 0. 2 0 9 * B F 6 \\ & + 0. 8 0 7 * B F 7 + 0. 2 0 6 * B F 9 + 0. 1 6 9 * B F 1 0 + 0. 9 5 6 * B F 1 1 + 1. 1 1 2 * B F 1 3 \\ & - 0. 1 9 4 * B F 1 5 \end{array}
$$

## 7.1.2. Interpretation of the results

## 1) Investments in Non-IT Labour (L)

Investments in Non-IT Labour can have a positive impact on productivity, but the overall impact of the amount invested in Non-IT Labour on productivity is contingent on the amounts invested in Non-IT Labour (see BF1, BF2), Non-IT Capital (see BF5 and BF6) and IT Labour (see BF15). For example, if the amount invested in Non-IT Capital is below $K _ { c v 1 }$ , where $K _ { c v 1 } = 2 0 6 9 0 2$ , the impact on productivity is positive as long as the amount invested in Non-IT Labour is below $L _ { c v 2 } ,$ , where $L _ { c v 2 } = 4 5 9 7 \ 3 9 3$ . In this situation, if the amount invested in Non-IT Labour is above $L _ { c v 2 } ,$ , the impact on productivity is negative. Thus, for those cases where additional investments in Non-IT Labour make the total investments in Non-IT Labour above $L _ { c v 2 }$ there would appear to be a ‘productivity paradox’ because the overall productivity is decreasing as the investment is increasing (see Figure 1). Therefore, when limited Non-IT Assets are available, the use of too many doctors, nurses or lab technicians could actually result in a decrease in productivity.

![](/api/attachments/CYHSB7GW/fulltext/images/9be65424dda2840c180a281b83bc16b042fe6f297824a37798501716e53d3287.jpg)  
Figure 1. The impact of Non-IT Labour on productivity in actual amount when Non-IT Capital is fixed at ${ K _ { c v 1 - } } ^ { 3 }$ and IT Labour is fixed at $S _ { c v 1 } .$

$^ 3 K _ { c v 1 - }$ means that Non-IT Labour is less than $K _ { c v 1 }$ and $S _ { c v 1 - }$ means that IT Labour is less than $S _ { c v 1 }$

On the other hand, if the amount invested in Non-IT Capital is above $K _ { c v 1 } ,$ , the impact of Non-IT Labour on productivity is always positive. In this case, if the amount invested in IT Labour is above $S _ { c v 2 }$ , the impact is lower than when it is below $S _ { c v 2 }$ . Thus, as we explained earlier, the overall impact of the amount invested in Non-IT Labour on productivity is not uniform. They are also evidenced by the fact that coefficients for each of the basis functions that involve Non-IT Labour are different (i.e. BF1, BF2, BF5, BF6 and BF15).

## 2) Investments in Non-IT Capital (K)

The impact of investments in Non-IT Capital (K) varies with the amount invested. For the case where this amount exceeds the $K _ { c v 1 }$ , where $K _ { c v 1 } = 2 0 6 ~ 9 0 2$ , then the impact is negative. This is the interpretation of the basis function, BF3 and its coefficient. Because the sign of the coefficient of BF3 is different from the sign of the Non-IT Capital (K) in BF13, the contribution of Non-IT Capital is negative. For the case when the amount invested in Non-IT Capital is below $K _ { c v 1 }$ , the impact of investment in Non-IT Capital is more complex, occurring within the context of the interactions of Non-IT Capital with both Non-IT Labour and IT Labour. The interaction of Non-IT Capital and Non-IT Labour when $K < K _ { c v 1 }$ is described by the basis functions BF5 and BF6 and their corresponding coefficients (see below). The interaction of Non-IT Capital and IT Labour then $K < K _ { c v 1 }$ is described by the basis function BF7 and its corresponding coefficients (see below).

$$
\mathrm{BF} 5 = \max (0, \log_ {\mathrm{e}} L - 1 5. 3 4 1) * \max (0, 1 2. 2 4 0 - \log_ {\mathrm{e}} K); \quad \text { coefficient } = - 1. 2 7 7
$$

$$
\mathrm{BF6} = \max (0, 1 5. 3 4 1 - \log_ {\mathrm{e}} L) * \max (0, 1 2. 2 4 0 - \log_ {\mathrm{e}} K); \quad \text { coefficient } = 0. 2 0 9
$$

$$
\mathrm{BF} 7 = \max (0, \log_ {\mathrm{e}} S - 1 2. 9 8 6) * \max (0, 1 2. 2 4 0 - \log_ {\mathrm{e}} K); \quad \text { coefficient } = 0. 8 0 7
$$

Thus, the overall impact of the amount invested in Non-IT Capital on productivity is not uniform.

## 3) Investments in IT Capital (T)

Investments in IT Capital have a positive impact on productivity only if the amount invested in IT Capital is above $T _ { c v 1 }$ , where $T _ { c v 1 } = 8 4 6 6 1 4$ Because the sign of the coefficient of the basis function is the same as the sign of the variable (BF9), the contribution of a given variable is positive. This explains a situation in which the initial IT investments in a health care organization need to be leveraged in creating IT infrastructure. Thus, until a certain threshold $T _ { c v 1 }$ is reached, investments in IT do not have a positive impact on productivity. On the other hand, the amount invested in IT Capital has a negative impact on productivity if the amount invested in IT Capital is below $T _ { c v 1 }$ . Because the sign of the coefficient of the basis function BF10 is dif ferent from the sign of the variable, the contribution of the given variable is negative.

For those cases where additional investments in IT Capital make the total investments below the required level, $T _ { c v 1 }$ , there would appear to be a ‘productivity paradox’ because overall productivity is decreasing as the IT Capital investments are increasing. As we explained earlier, the overall impact on organizational productivity is not uniform because there are different coeffi cients for each of the basis functions that involve the IT Capital (i.e. BF9 and BF10).

## 4) Investments in IT Labour (S)

The overall impact of IT Labour investments on productivity is contingent on the amount invested in IT Labour (see BF11), as well as the amount invested in Non-IT Labour (see BF15), Non-IT Capital (see BF7) and Medical IT Capital (see BF13). For example, if the amount invested in Non-IT Capital is below $K _ { c v 1 }$ and the investments in IT Labour are above $S _ { c v 1 }$ , where $S _ { c v 1 } = 4 3 6 2 6 3$ , investments in IT Labour have a positive impact on productivity. Thus, when limited Non-IT Assets are available, investments in IT staff (i.e. automating processes or training) could increase the overall productivity. If the amount invested in Non-IT Capital is above $K _ { c v 1 }$ investments in IT Labour have a positive impact on productivity only if the amount invested in IT Labour is above $S _ { c v } ,$ , where $S _ { c v 2 } = 8 4 6 6 1 4$ . Thus, the overall impact on organizational productivity is not uniform because there are different coefficients for each of the basis functions that involve the IT Labour (i.e. BF7 and BF11).

For those cases where the additional investments in IT Labour would still make the tota investments in IT Labour below $S _ { c v 1 }$ [where $\log _ { \mathrm { e } } ( S _ { c v 1 } ) = 1 2 . 9 8 6 ]$ , the basis function BF13 [i.e. max(0, log M - 11.338)  max(0, $1 3 . 6 4 9 - \mathsf { l o g } _ { \mathrm { e } } S ) ]$ applies. In this situation, the impact of IT Labour occurs within the context of its interaction with Medical IT Capital.

## 5) Investments in Medical IT Capital (M)

The overall impact on productivity is not uniform because it is contingent on both the amount invested in Medical IT Capital and the amount invested in IT Labour (see BF13). For example, if the amount invested in IT Labour is below $S _ { c v 2 } .$ , where $S _ { c v 2 } = 8 4 6 6 1 4$ , and the investments in Medical IT Capital are above $M _ { c v 1 }$ , where $M _ { c v 1 } = 8 3 ~ 9 5 2$ , investments in Medical IT Capital have a positive impact on productivity. However, if the amount invested in IT Labour is above $S _ { c v 2 }$ , or if the amount invested in Medical IT Capital is below $M _ { c v 1 }$ , the amount invested in Medical IT Capital does not have any impact on productivity.

For those cases where total investments in Medical IT Capital are still below $M _ { c v 1 }$ after further investment in Medical IT Capital, a ‘productivity paradox’ would appear to exist because there would be no resulting improvement in productivity.

## 7.2. A limited comparative analysis of the results from two studies

In this section, we offer a limited comparison of our results with those obtained in a study by Menon et al. (2000). Our choice of this study was primarily based on the fact that this is the only study that used the same data set. However, we use their study in only a limited way because our study is based on a Translog function, which allows two-way interaction between variables, whereas their study uses a stochastic production frontier approach that did not allow two-way interaction between variables. We would like to compare the findings only to the extent that the previous study identified the importance of the same investment variables.

As shown in Table 5, the Menon et al. (2000) study indicates that Non-IT Labour has the highest positive impact on productivity, with Medical IT Capital, IT Capital and IT Labour also having positive impacts on productivity, while Non-IT Capital has a negative impact on productivity.

Table 5. Parameter estimates from stochastic production frontie

<table><tr><td>Variable</td><td>Parameter estimates</td><td>t-Statistics</td></tr><tr><td>Constant</td><td>5.2901</td><td>133.11</td></tr><tr><td>Non-IT Labour</td><td>0.8626</td><td>143.51</td></tr><tr><td>IT Labour</td><td>0.1804</td><td>118.89</td></tr><tr><td>Non-IT Capital</td><td>-0.0845</td><td>-36.68</td></tr><tr><td>Medical IT Capital</td><td>0.0608</td><td>49.15</td></tr><tr><td>IT Capital</td><td>0.0179</td><td>36.21</td></tr></table>

For all values, P < 0.0005.

The results of Menon et al. (2000) support our research hypotheses H1 and H2, indicating that IT investments in health care organizations have a positive impact on productivity. Thei results also suggest that the impact of IT investment is uniform.

The results of our study only partially support H1, indicating that the impact of IT investments on productivity is positive only under a certain condition, and that this impact is not uniform; thus, H2 is not supported. Depending on the amount invested in each category, the impact on productivity changes, and, thus, our findings are consistent with the contingency theory of organizations.

## 7.3. Contingency and complementarity theories and interpretation of the results

The underlying premise of the contingency theory of organizations is that organizational performance is based on the fit between relevant variables (Barua et al., 1996). The interaction approach of the theory predicts that the interaction between two variables explains perfor mance (Selto et al., 1995; Bergeron et al., 2001). Likewise, in the context of IT investments, the contingency theory suggests that interaction of IT and non-IT investments may explain the organizational productivity. Thus, the impact of IT investment on organizational productivity is contingent on one or more complementary factors such as whether investments in non-IT were also made. Complementarity theory assumes that doing (more of) one factor increases the returns to doing (more of) another complementary factor (Milgrom & Roberts, 1995; Barua et al., 1996). Applying complementarity theory to IT productivity research, our results describe that the complementary relationship exists between investments in IT and non-IT. Thus, the impact of IT investment on organizational productivity can be maximized when the complementary variables are considered together than when they are considered in isolation (Barua et al., 1996).

Our findings suggest that when making IT investment decisions, top managers should identify the complementary variables and consider investments in complementary variables, because the impact of IT investment on productivity is contingent on investment in these com plementary factors. Figure 2 displays an example of investment type and its complementary factor(s) in our study.

![](/api/attachments/CYHSB7GW/fulltext/images/7dc1f03a383d7c48eeb58b2be65c1848ef484a52fb0aec4eaa0bf2f881203857.jpg)  
Figure 2. Type of investment and its complementary factor(s).

## 8. CONCLUSIONS AND LIMITATIONS

While investments in IT have continuously increased, efforts in identifying the impact of IT investments on productivity at the firm level are still not very successful. In this study, we take another look at the IT productivity issue using a new technique, MARS, on a data set of the health care industry.

Our research contributes to IT productivity research in several ways. First of all, our study introduces a relatively new data mining technique, MARS, to IT productivity research. This technique provides the opportunity for rich analysis, including the exposing of insights on the relationship between IT investments and productivity that might not be offered by traditiona technigues such as regression and data envelopment analysis, Second, while previous studies indicate that IT investments have a positive but uniform impact on productivity, our study suggests that the impact of IT is not uniform, but contingent on other complementary variables, such as the amounts invested in IT Labour, IT Capital and Medical IT Capital, as well as the amount invested in Non-/T Labour and Non-/T Capital. Thus, our results support the contingency theory of organizations. Our findings provide clues for inconsistent results originating from previous studies. We believe that our results advance IT productivity research by providing additional insights for understanding the complexity of IT productivity issues.

Furthermore, in addition to insights offered by the interpretation of the relevant basis functions and their coefficients, the RS model offers the opportunity for conducting 'What-If' analysis. While it is true that there are limitations for the usefulness of formal and informal predictive models that are based on historical data, they are still often used in modern organizations. For example, the budgeting process in many health care organizations involves top-down budgeting, bottom-up budgeting, or a hybrid of these two approaches. In top-down budgeting, top management develops and approves the enterprise-wide budget even before project and department budgets are developed. Middle and lower level managers then break down these estimates into project and departmental budgets. The estimates in the enterprise-wide budget are based on the top managers’ judgement, experience and past budget data. With the bottomup approach, project and department budgets are developed before the enterprise-wide budget, and are combined into the enterprise-wide budget, which is then sent to top-management for approval. In both approaches, top-management has to make enterprise-wide budget decisions based on different scenarios in which investment amounts are aggregated at the organizational level and not at the project level. In such situations, ‘What-If’ analysis is conducted using formal or informal models. In those situations where the decision-makers consider information from the past to be relevant to the decision-making process, a predictive model such as the one derived in this paper might be considered to be a useful decision support resource. For example, let’s assume that an additional amount of \$12 703 024 is available for investment, and that the current investments in IT Labour, IT Capital, Medical IT Capital, Non-IT Capita and Non-IT Labour are \$2 773 863, \$88 986, \$487 920, \$197 452 and \$18 307 483 respectively. The decision facing the manager is how much should be invested in each area. Using the RS model, the manager could conduct ‘What-If’ analysis based on different scenarios (see Table 6a) and observe the predicted Adiusted Patient Davs (see Table 6b). The reader shoulo note that we began the study with numbers from an actual observation in the data set and cre ated various scenarios for the investment amount in this example using our RS model. Thus, we only want to emphasize that our model offers a formal approach for identifying scenarios under which additional investment in IT could have a positive or negative impact on productivity.

Table 6a. Percentage of new investment allocated to each variable

<table><tr><td>Scenario</td><td>IT Labour</td><td>IT Capital</td><td>Medical IT Capital</td><td>Non-IT Capital</td><td>Non-IT Labour</td></tr><tr><td>1</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>100</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>0</td><td>100</td><td>0</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>100</td></tr><tr><td>5</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>6</td><td>60</td><td>10</td><td>10</td><td>10</td><td>10</td></tr><tr><td>7</td><td>10</td><td>60</td><td>10</td><td>10</td><td>10</td></tr><tr><td>8</td><td>10</td><td>10</td><td>60</td><td>10</td><td>10</td></tr><tr><td>9</td><td>10</td><td>10</td><td>10</td><td>60</td><td>10</td></tr><tr><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>60</td></tr></table>

Table 6b. Proposed investments and the impact on productivity

<table><tr><td>Scenario</td><td>IT Labour</td><td>IT Capital</td><td>Medical IT Capital</td><td>Non-IT Capital</td><td>Non-IT Labour</td><td>Adjusted Patient Days</td></tr><tr><td>1</td><td>15 476 887</td><td>88 986</td><td>487 920</td><td>197 452</td><td>18 307 483</td><td>265 624</td></tr><tr><td>2</td><td>2 773 863</td><td>12 792 010</td><td>487 920</td><td>197 452</td><td>18 307 483</td><td>134 439</td></tr><tr><td>3</td><td>2 773 863</td><td>88 986</td><td>487 920</td><td>12 900 476</td><td>18 307 483</td><td>30 839</td></tr><tr><td>4</td><td>2 773 863</td><td>88 986</td><td>487 920</td><td>197 452</td><td>31 010 507</td><td>254 138</td></tr><tr><td>5</td><td>5 314 468</td><td>2 629 591</td><td>3 028 525</td><td>2 738 057</td><td>20 848 088</td><td>53 020</td></tr><tr><td>6</td><td>10 395 677</td><td>1 359 289</td><td>1 758 222</td><td>1 467 754</td><td>19 577 785</td><td>71 488</td></tr><tr><td>7</td><td>4 044 165</td><td>7 710 801</td><td>1 758 222</td><td>1 467 754</td><td>19 577 785</td><td>71 840</td></tr><tr><td>8</td><td>4 044 165</td><td>1 359 289</td><td>8 109 734</td><td>1 467 754</td><td>19 577 785</td><td>53 222</td></tr><tr><td>9</td><td>4 044 165</td><td>1 359 289</td><td>1 758 222</td><td>7 819 266</td><td>19 577 785</td><td>28 517</td></tr><tr><td>10</td><td>4 044 165</td><td>1 359 289</td><td>1 758 222</td><td>1 467 754</td><td>25 929 297</td><td>72 246</td></tr></table>

Our study includes several limitations. First, our findings are based on one industry – the health care industry. Thus, we do not want to emphasize the actual dollar amount of investments for each input variable but rather focus on the fact that there is a level of investment for each input variable that can impact productivity, Second. while studies such as ours that involve quantitative analyses based on the production function approach are often considered to be theoretically rigorous (Barua & Mukhopadhyay, 2000), such studies involve the assumption that IT investments have a direct impact on organizational performance. Thus, our study treats the relationship between IT investments and organizational performance as a ‘black box’. However, to fully understand the impact of IT investments on organizational performance, we need to focus on how IT investments are converted into IT assets, making an impact, and finally leading to improved organizational performance (Markus & Soh, 1993; Soh & Markus, 1995). Thus, some organizational contextual variables that moderate the impact of IT investment on organizational performance should be considered (Weill, 1992; Soh & Markus, 1995; Li & Ye, 1999; Teo et al., 2000; Hoogeveen & Oppelland, 2002). Third, as is common to empirical data sets, this data set also has some measurement issues. Because the data set is based on data collected in the state of Washington in the USA, it may not be a representative sample of all hospitals. Thus, the generalizability of the findings may be limited. Also, because the data set includes data for a 20-year period (i.e. 1975–94), it is possible that consistency in the collection of the data might not be the same over the years, although deflators are used to maintain compatibility. Another issue is the age of the data set. It is possible that additional insights might have been obtained from a more recent data set, permitting us to consider the impact of current technologies, such as electronic commerce and enterprise resource planning (ERP) systems on organizational productivity. In addition, the data set does not contain all variables that might be relevant to a study of this nature because Net Patient Revenue Per Admission or Patient Satisfaction could also be used. It should, however, be noted that despite these limitations we were able to obtain an explanatory model with high R-squared value.

Another important limitation of this study is the theoretical model on which it is based. While the Translog production function is more general than the Cobb-Douglas production function, it still limits the number of variables that can be involved in an interaction to two. Thus, if some of the complementary relationships involved more than two variables then those relationships would not have been identified. It should be noted, however, that complementary relationships involving more than two variables can be easily identified using RS analysis. While we could have tried to identify such relationships in this study, the result would have been a more complicated RS model whose corresponding theoretical model might not be well known.

For future research, we plan to perform another analysis using the same data set but include only years before DRG or only years after DRG because implementation of DRG in 1983 fundamentally changed how hospitals get reimbursed. While it would be beneficial to show the results of the data set after the implementation of the DRG, investigating the impact of IT investments from the implementation of the DRG was not the main objective of this paper. However, we hope to investigate the impact of the DRG implementation in future research. We also would like to explore some additional issues including: (1) the impact of newer forms of IT such as ERP systems and electronic commerce on productivity; (2) the effects of time lag of IT investments and its return; and (3) the identification of significant higher order complementary/ contingency relationships that involve two or more variables.

## 9. ACKNOWLEDGEMENTS

We are grateful to Professors Byungtae Lee and Nirup Menon for kindly sharing their data set and to Professor Menon for letting us use his SAS programme, thus facilitating this study. We also thank the anonymous referees for their valuable comments, which have contributed to improving the quality of the paper.

## REFERENCES

Abraham, A. (2002) Analysis of hybrid soft and hard computing techniques for Forex Monitoring Systems. World Congress on Computational Intelligence, May, pp. 1616– 1622.

Abraham, A. & Steinberg, D. (2001) Is neural network a reliable forecaster on earth? A MARS Query! In: International Work – Conference on Artificial and Natural Neural Networks, Jose, M. & Alberto, P. (eds), pp, 679– 686, Springer-Verlag, Germany, June.

Anderson, J.G. (1997) Clearing the way for physicians’ use of clinical information systems. Communications of the ACM, 40, 83–90.

Barua, A., Lee, C.H.S. & Whinston, A.B. (1996) The calculus of reengineering. Information Systems Research, 7, 409–428.

Barua, A., Kriebel, C. & Mukhopadhyay, T. (1995) Infor mation technologies and business value: an analytic and empirical investigation. Information Systems Research, 6, 3–23.

Barua, A. & Mukhopadhyay, T. (2000) Information technologies and business performance: past, present, and future. In: Framing the Domains of IT Management Projecting the Future Through the Past, Zmud, R. (ed.) Pinnaflex Education Resources, Inc., Cincinnati. OH USA.

Bergeron, F., Raymond, L. & Rivard, S. (2001) Fit in strategic information technology management research: an empirical comparison of perspectives. Omega, 29, 125–142.

Bose, B. (2003) Knowledge management-enabled health care management systems: capabilities, infrastructure, and decision-support. Expert Systems with Applications, 24, 59–71.

Breiman, L., Friedman, J.H., Olshen, R. & Stone, C. (1984) Classification and Regression Trees. Wadsworth International Group, Belmond, CA.

Briand, L.C., Freimut, B. & Vollei, F. (2000b) Using multiple adaptive regression splines to understand trends in inspection data and identify optimal inspection rates. International Software Engineering Research Network (ISERN), ISERN-00-07, Version 1.

Briand, L.C., Melo, W. & Wuest, J. (2000a) Assessing the applicability of fault-proneness models across object oriented software projects. International Software Engi neering Research Network (ISERN), ISERN-00-06, Ver sion 2.

Brynjolfsson, E. & Hitt, L.M. (1996) Paradox lost? Firm level evidence on the returns to information systems spending. Management Science, 42, 541–558.

Carey, W.P. & Yee, S.S. (1992) Calibration of nonlinea solid-state sensor arrays using multivariate regression techniques. Sensors and Actuators, 9, 113–122.

Danzon, P.M. & Furukawa, M.F. (2001) Health care: competition and productivity. In: The Economic Payoff from the Internet Revolution, Litan, R.E. & Rivlin, A.M. (eds), pp. 189–234. The Brookings Institution, Washington, DC, USA.

Dash, J. (1997) IT gets to the heart of health care. Soft ware Magazine, 17. 76–79.

De Veaux, R.D., Psichogios, D.C. & Ungar, L.H. (1993) A comparison of two nonparametric estimation schemes: MARS and neural networks. Computers Chemical Engi neering, 17, 819–837.

Devaraj, S. & Kohli, R. (2000) Information technology payoff in the health-care industry: a longitudinal study. Jour nal of Management Information Systems, 16, 41–67.

Dewan, S. & Min, C.-K. (1997) The substitution of informa tion technology for other factors of production: a firm level analysis. Management Science, 43, 1660–1675.

Ekman, T. & Kubin, G. (1999) Nonlinear prediction of mobile radio channels: measurements and MARS mode

designs. IEEE International Conference on Acoustics, Speech and Signal Processing, pp. 2667–2670.

Eubank, R. (1988) Spline Smoothing and Nonparametric Regression. Mercel Dekker, Inc., New York, NY, USA.

Evans, D., Green, C. & Murinde, V. (2000) The importance of human capital and financial development in economic growth: new evidence using the Translog production function. Finance and Development Research Programme Working Paper Series, Paper no. 22, November, pp. 1–31.

Francalanci, C. & Galal, H. (1998) Information technology and worker composition: determinants of productivity in the life insurance industry. MIS Quarterly, 22, 227-241.

Friedman, J.H. (1991) Multivariate adaptive regression splines. Annals of Statistics, 19, 1–141.

Griffin, W.L., Fisher, N.I., Friedman, J.H. & Ryan, C.G. (1997) Statistical technigue for the classification of chromites in diamond exploration samples. Journal of Geochemical Exploration. 59. 233–249

Grimson, J., Grimson, W. & Hasselbring, W. (2000) The system integration in health care. Communications of the ACM, 43, 49–55.

Hastie, T.J. & Tibshirani, R.J. (1990) Generalized Additive Model. Chapman & Hall, London.

Hastie, T.J., Tibshirani, R.J. & Friedman, J.H. (2001) The Elements of Statistical Learning: Data Mining, Inference, and Prediction. Springer-Verlag, New York.

Henderson, J. & Quandt, R. (1980) Microeconomic Theory: A Mathematical Approach. McGraw-Hill Book Company, New York, NY, USA.

Hitt, L.M. & Brynjolfsson, E. (1996) Productivity, business profitability, and consumer surplus: three different measures of information technology value. MIS Quarterly, 20, 121–142.

Hoogeveen, D. & Oppelland, H.J. (2002) A socio politica model of the relationship between IT investments and business performance. Proceedings of the 35th Hawai International Conference on System Sciences

Jin, R., Chen, W. & Simpson, T.W. (2000) Comparative Studies of Metamodeling Techniques Under Multiple Modeling Criteria, American Institute of Aeronautics and Astronautics. AIAA-2000-4801.

Kuhnert, P., Do, K.-A. & Mcclure, R. (2000) Combining non-parametric models with logistic regression: an appli cation to motor vehicle injury data. Computational Statistics and Data Analysis, 34, 371–386.

Lee, B. & Menon, N. (2000) information technology value through different normative lenses. Journal of Management Information Systems, 16, 99–119.

Li, M. & Ye, L.R. (1999) Information technology and firm performance: linking with environmental, strategic and managerial contexts. Information and Management, 35, 43–51.

Lichtenberg, F. (1995) The output contributions of computer equipment and personnel: a firm-level analysis. Journal of Economic Innovation and New Technology, 3, 201–207.

Loveman, G.W. (1994) An assessment of the productivity impact of information technologies. In: Information Technology and the Corporation of the 1990s: Research Studies, Allen. T.J. & Scott Morton, M.S. (eds), pp. 84– 110. MIT Press, Cambridge, MA, USA.

Maclean, M. & Mix, P. (1991) Measuring hospital productivity and output: the omission of outpatient services. Health Reports, 3, 229–244.

Mallick, B.K. Denison, D.G.T. & Smith, A.F.M. (1997) Bayesian Survival Analysis Using a MARS Model – Technical Report. Imperial College, London.

Markus, L. & Soh, C. (1993) Banking on information technology: converting IT spending into firm performance. In: Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Adyantage. Banker, R., Kaufmann. R. & Mahmood. M (eds), pp. 375–403. Idea Group Publishing, Harrisburg, PA, USA.

Menon, N. & Lee, B. (2000) Cost control and production performance enhancement by IT investment and regulation changes: evidence from the healthcare industry. Decision Support Systems, 30. 153–169

Menon, N., Lee, B. & Eldenburg, L. (2000) Productivity o information systems in the healthcare industry. Information Systems Research, 11, 83–92

Milgrom, P. & Roberts, J. (1995) Complementarities and fi strategy, structure, and organizational change in manu facturing. Journal of Accounting and Economics, 19, 179–208.

Mukhopadhyay, T., Surendra, R. & Srinivasan, K. (1997) Information technology impact on process output and quality. Management Science, 43, 1645–1659

Nguyen-Cong, V., Van Dang, G. & Rode, B.M. (1996) Using multivariate adaptive regression splines to OSAR studies of dihydroartemisinin derivatives. European Journal of Medical Chemistry, 31, 797– 803.

Prasad. A.M. & Iverson, L.R. (2000) Predictive vegetation mapping using a custom built model-chooser: compari son of regression tree analysis and multivariate adaptive regression splines. 4th International Conference on Integrating GIS and Environmental Modeling (GIS/EM4):

Problems, Prospects and Research Needs. Banff, Alberta, Canada.

Prasad, B. & Harker, P. (1997) Examining the contribution of information technology toward productivity and profitability in U.S. retail banking. Working Paper No. 97-09, Financial Institutions Center, The Wharton School. University of PennsyIvania, PA, USA.

Raghupathi, W. (1997) Health care information systems. Communications of the ACM, 40, 81–82.

Salford Systems (2000) MARS for Windows, Version 2.0.

Selto, F.H., Renner, C.J. & Young, S.M. (1995) Assessing the organizational fit of a just-in-time manufacturing system: testing selection, interaction and systems models of contingency theory. Accounting, Organizations and Society, 20, 665–684.

Shao, B. (2000) Investigating the value of information technology in productive efficiency: An analytic and empirical study. PhD thesis, State University of New York, Buffalo, NY, USA.

Shao, B. & Lin, W. (2001) Measuring the value of information technology in technical efficiency with stochastic production frontiers. Information and Software Technology, 43, 447–456.

Smith, H.L. & Bullers, W. Jr & Piland, N.F. (2000) Does information technology make a difference in healthcare organization performance? A multiyear study. Health Topics: Research and Perspectives on Healthcare 7813–22

Soh, C. & Markus, M.L. (1995) How IT creates business value: a process theory synthesis. Proceedings of the 16th International Conference on Information Systems, Amsterdam, The Netherlands, pp. 29–41.

Steinberg, D., Colla, P.L. & Martin, K. (1999) MARS User Guide, Salford Systems, San Diego, CA.

Sumner, A.T. & Moreland, C.C. (1995) The potential impact of diagnosis related group medical management on hospital utilization and profitability. Health Care Management Review, 20, 92–100.

Teo, T.S.H., Wong, P.K. & Chia, E.H. (2000) Information technology (IT) investment and the role of a firm: an exploratory study. International Journal of Information Management, 20, 269–286.

Ward. S. (2002) Companies sguander billions on Tech USA Today, 20 May 2002.

Weill. P. (1992) The relationship between investment in information technology and firm performance: a study of

the valve manufacturing sector. Information Systems Research, 3, 307–333.

Wholey, D.R., Padman, R., Hamer, R. & Schwartz, S. (2000) The diffusion of information technology among health maintenance organizations. Health Care Man agement Review, 25, 24–33.

York, T.P. & Eaves, L.J. (2001) Common disease analysis using multivariate adaptive regression splines (MARS): genetic analysis workshop 12 simulated sequence data. Genetic Epidemiology, 21, 649–654.

## Biographies

Myung S. Ko is currently an Assistant Professor in the Department of Information Systems at the College of Busi ness, University of Texas at San Antonio. Dr Ko received her PhD in Information Systems from the Virginia Commonwealth University. She holds MA in Accounting. He research interests include impact of IT on organizations, business value of IT, data mining and accounting information systems.

Kweku-Muata Osei-Bryson is Professor of Information Systems at Virginia Commonwealth University since Fall 1998. Previously he was Professor of Information Systems and Decision Analysis in the School of Business at Howard University. Washington. DC. USA. He has also worked as an Information Systems Practitioner in both industry and government. He does research in various areas including: Data Mining, Expert Systems, Decision Support Systems, Group Support Systems, Information Systems Outsourcing, Multi-Criteria Decision Analysis. His papers have been published in various journals including: IEEE Transactions on Knowledge & Data Engineering, Data & Knowledge Engineering, Information & Software Technology, Decision Support Systems, Information Processing and Management, Computers & Operations Research, European Journal of Operational Research, Journal of the Operational Research Society Journal of the Association for Information Systems, Journal of Multi-Criteria Decision Analysis. Applications of Management Science. Currently he serves an Associate Editor of the INFORMS Journal on Computing, and is a member of the Editorial Board of the Computers and Operations Research Journal.
