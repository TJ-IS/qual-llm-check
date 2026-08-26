---
otero_id: 1320
otero_key: "WDA39N3C"
title: "A longitudinal study of e-government maturity"
authors: "Amit Das; Harminder Singh; Damien Joseph"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2016.09.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A longitudinal study of e-government maturity

Amit Das<sup>a,</sup>\*, Harminder Singh<sup>b</sup>, Damien Joseph<sup>c</sup>

<sup>a</sup> College of Business & Economics, Qatar University, Doha, Qatar

<sup>b</sup> Faculty of Business and Law, Auckland University of Technology, Auckland, New Zealand

<sup>c</sup> Nanyang Business School, Nanyang Technological University, Singapore

## A R T I C L E I N F O

Article history: Received 15 September 2015 Received in revised form 28 June 2016 Accepted 29 September 2016 Available online xxx

Keywords: e-Government maturity ICT infrastructure Human capital index Governance Panel data analysis Mixed-effects models

## A B S T R A C T

We assembled a panel data set for the period 2002–2008 and <sup>fi</sup>tted a mixed-effects regression model to study how the maturity of e-Government around the globe was in<sup>fl</sup>uenced by changing levels of af<sup>fl</sup>uence, information communication technology (ICT) infrastructure, human capital, and governance. We found that e-Government matured faster with rising af<sup>fl</sup>uence (in terms of gross domestic product (GDP) per capita) and improvements in ICT infrastructure. Human capital and the quality of governance had no signi<sup>fi</sup>cant effect on e-Government maturity. The results suggest that a high level of e-Government maturity can be attained purely through investment in ICT infrastructure, without substantial changes to human capital or governance.

ã 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Though information technology applications in government are decades old, e-Government is a comparatively new phenomenon [48]. Traditional IT in government is inward looking and addresses mainly applications internal to government agencies. Conversely, e-government is outward looking and connects government agencies to external stakeholders such as citizens, businesses, and other government agencies. If the World Wide Web (web servers and browser clients communicating over the HTTP protocol) is viewed as a general purpose technology with the characteristics of pervasiveness, progressive improvement in cost performance, and support for innovation [12]; e-Government can be conceptualized as the application of this general purpose technology to the speci<sup>fi</sup>c domain of government. At its core, e-Government uses mostly the same building blocks as retail and business-to-business e-commerce, and faces many of the same technical challenges (e.g., availability, scalability, and security).

While the technology itself might be familiar, e-Government has proven hard to theorize [48]. Sitting at the cusp of public administration and information systems two multidisciplinary <sup>fi</sup>elds in search of their own dominant paradigms e-Government presents a challenge to native as well as imported theories [9]. Pre-2000 viewpoints of informatization and infocracy (transformation of government processes and structures through information technology) have been largely supplanted by more critical accounts of the reinforcement of existing power structures, over-government, and surveillance. Expectations of technologyled transformation persist, but are now tempered by organizational inertia and the recognition of diverging interests.

Against this backdrop, many past studies of e-Government can be categorized by their focus on the supply of and/or the demand for e-Government. Studies on the demand side investigate the uptake of e-Government services and the satisfaction of users – how e-Government affects citizens and <sup>fi</sup>rms [5,54]. Demand-side research on e-Government also examines the impacts of e-Government projects, such as the <sup>fi</sup>nancial and non<sup>fi</sup>nancial outcomes. The results from these studies <sup>fi</sup>nd e-Government to be positively associated with business competitiveness, national economic performance, and environmental protection [21,59– 61], and negatively with corruption [40].

Studies on the supply side examine obstacles e-Government projects face in achieving their goals [62,25] and the demands they place on the back-of<sup>fi</sup>ce functions of government agencies [1]. They also include measures of “e-readiness” as an enabler of e-Government development, such measures often including technological infrastructure, citizens’ skills, and political support. Large-scale empirical studies in this stream of research have explored how a variety of factors in<sup>fl</sup>uences the adoption of

A. Das et al. / Information & Management xxx (2016) xxx–xxx

e-Government around the globe. Factors found to have a signi<sup>fi</sup>cant effect include a country’s income (gross domestic product (GDP)), the muni<sup>fi</sup>cence of its macroeconomic environment, the quality of its information communication technology (ICT) infrastructure, the level of trust in the society, and the quality of its public institutions and civic life [4,20,58,59].

With the exception of I<sup>fi</sup>nedo (2011) [28], almost all the studies that have examined e-Government maturity so far use crosssectional data [58,59] or within-country analyses [33,50]. These studies provide useful information comparing e-Government activity in different countries at particular points in time. However, e-Government evolves over time, and the factors in<sup>fl</sup>uencing this evolution cannot be identi<sup>fi</sup>ed from cross-sectional studies. In particular, how does e-Government mature in a country as its af<sup>fl</sup>uence, ICT infrastructure, human capital, and governance evolve over time? Cross-sectional studies, which compare countries at one point in time, cannot answer this question.

Furthermore, the apparent relationship between the predictor and outcome variables estimated through cross-sectional analysis may not hold up in longitudinal analysis. A classic case, where the conclusion from cross-sectional analysis, is reversed by longitudinal examination, is described in Rosenthal and Rosnow (2013) [53] who cite [26] Hagenaars and Cobben’s (1978) study on the rate of religious nonaf<sup>fi</sup>liation among Dutch women over time. Crosssectional analysis of this data set erroneously suggests that Dutch women became more religious as they got older, when longitudinal analysis uncovers just the opposite, the confusion being caused by differences in religiosity across successive cohorts (later cohorts starting out more religious than earlier cohorts).

An additional concern with cross-sectional studies is the bias in coef<sup>fi</sup>cient estimates introduced by the misspeci<sup>fi</sup>cation of models, particularly the omission of potentially relevant predictors. Data permitting, one way to guard against omitted-variable bias is panel data analysis, where we regress period-to-period changes in the dependent variable on the changes in the independent variables. If the omitted variable (e.g., geography or culture) is time invariant for each country, its effect is captured in the intercepts of the regression model. The effect of omitted variables that change at the same rate for all countries is picked up by the slope on the time variable. Panel data analysis can thus be restricted to variables that change at different rates for different countries (GDP, ICT infrastructure, human capital, governance, etc.). Limiting the proliferation of independent variables addresses the width (number of countries) versus depth (number of variables) tradeoff [18] faced by most longitudinal studies; here we are able to retain 191 countries in our models, reducing the chances of sampling bias.

Driven by these twin concerns, stronger causal inference [17] and robustness to errors arising from model misspeci<sup>fi</sup>cation, we develop and use panel data to examine the drivers of e-Government maturity. Our research question is: how does the maturity of a country’s e-Government services change over time as it improves its income level, its ICT infrastructure, its human capital, and its governance institutions and processes? Our focus is not so much on comparing the state of e-Government maturity in different countries at a point time as on understanding why e-Government matures at different rates over time in different countries. Our mixed-effects statistical models allow countries to start at different levels of e-Government maturity at the start of the study window, and then experience different rates of growth over time (random components in intercept as well as slope estimates).

The next section presents in brief the conceptual arguments supporting our choice of variables that bear on e-Government maturity. Next, we describe our methodology and data, before presenting our results. We conclude with a short discussion of our <sup>fi</sup>ndings, possible limitations, and avenues for future research.

## 2. Conceptual model and hypotheses development

## 2.1. e-Government Maturity

e-Government maturity may be de<sup>fi</sup>ned as the extent to which a government has established an online presence [81]. The online presence of governments is realized through the features implemented in e-Government web sites such as free access to online publications, access to databases, and a variety of online services (free and paid). Well-developed e-Government sites use multimedia to supplement text in multiple languages, and allow access from a wide range of computing devices (such as tablets and smartphones). e-Government web sites must make it easy for users to voice their concerns and provide feedback, with special attention to disability access [31]. Finally, e-Government web sites must safeguard privacy and security even more closely than their commercial counterparts, and present their policies in these matters clearly for all users.

The demanding requirements laid out above for e-Government web sites cannot be met overnight, and e-Government maturity usually represents a continuum of developmental stages, from publishing information to supporting online transactions, with some having progressed further than others [83]. Previous research on e-Government has thus conceptualized maturity using an evolutionary approach [43,2]. In this view, e-government is seen to progress through a series of stages as a function of integration and complexity, or as a function of increasing levels of online activity and customer centricity. Such maturity models are useful because they guide practitioners, help the citizenry understand the trajectory of e-Government, and can be used as a communication tool to explain e-Government to third parties [36].

In this study, we seek to measure and explain e-Government maturity as demonstrated behavior, in contrast to other measures that assess the potential of a country to enact e-Government. A well-known example of the latter is the United Nation’s (UN’s) e-Government Readiness Index, which includes, among other components, the state of a nation’s telecommunication infrastructure and its level of human capital [72–76]. Other measures of e-Government potential include the World Economic Forum’s Networked Readiness Index [87–93], which covers about half to two-thirds of all countries in the world.

The UN and World Economic Forum indices indicate the capacity of a country to engage in e-Government programs, but do not explicitly address its current success in implementing them. Hence, we rely on the evaluation of e-Government web sites by West and his associates at the Inside Politics research center at Brown University. West and his associates examined >1500 government web sites from >190 nations in the summer of each year from 2002 to 2008 [78–84]. Details of the data collected by West are provided in a later section. With respect to stage theories of e-Government evolution, some of West’s criteria databases, security features, and support for digital signatures and credit card payments bear directly on the capability to deliver service transactions. As a result, our conceptualization of e-Government maturity is focused more on the provision of services than on political activity [36]. Given the wide variation among countries, transaction capability appears to be, in the time frame of the study, a common denominator on which e-Government can be compared across countries.

## 2.2. Determinants of e-Government maturity

The determinants of e-Government maturity examined in this study are national af<sup>fl</sup>uence (in terms of a country’s GDP per capita, adjusted for purchasing power parity), ICT infrastructure, human capital, and governance. These factors have been used extensively in previous studies [4,20,58,59,61] and shown to correlate positively with the development of e-Government internationally.

GDP: National af<sup>fl</sup>uence refers to a country’s overall level of wealth, as measured by its per capita GDP. Well-off countries might have spare resources (“slack” in organization theory terms) to invest in ICT systems to support government functions. By contrast, less developed countries must focus on maintaining and improving the traditional modes and channels of government. A positive relationship between af<sup>fl</sup>uence and e-Government has been found in previous research [20,61]. However, Azad et al. (2010) [4] did not <sup>fi</sup>nd a signi<sup>fi</sup>cant relationship between e-Government and GDP. They conjectured that many countries adopt e-Government only symbolically and do not progress beyond the creation of “Potemkin e-villages” [34]. Another reason for the lack of a relationship could be their use of a <sup>fi</sup>ve-stage measure of e-Government adoption, which was much coarser than the indices used in other studies.

We can argue that as countries become richer, they undertake more and more ambitious e-Government services, going beyond just the “essential” information systems such as broadcasts of government policies and directories of government services. Of course, the success of such services sets up a virtuous cycle of positive feedback justifying further investment in e-Government. Hence, our <sup>fi</sup>rst hypothesis is:

Hypothesis 1. Increase in a country’s GDP per capita is positively associated with an increase in e-Government maturity over time.

ICT Infrastructure: Given slack resources in the form of GDP per capita, ICT infrastructure the diffusion and use of information and communication technology in a country is expected to promote the maturity of e-Government. With the prices of computing equipment falling steadily, the limiting factor for ICT development in recent times appears to be the availability and affordability of telecommunication bandwidth. The extent of ICT development directly facilitates (or limits) the delivery of e-Government services to its citizenry [56,61] in terms of both reach and richness. Citizens in countries with higher levels of ICT penetration are also more likely to conduct their governmentrelated affairs online [58]. In related research, Fernández-i-Marín (2011) [24] used a Bayesian linear model to estimate the “critical” level of internet penetration in European countries above which e-Government applications become viable.

In addition to reach, development of national ICT infrastructures enables more complex services, such as those requiring more bandwidth (e.g., streaming video), or those supporting mobile devices (e.g., location-based services). Hence, we postulate:

Hypothesis 2. Improvements in a country’s ICT infrastructure are positively associated with an increase in e-Government maturity over time.

Human Capital: The human capital of a country re<sup>fl</sup>ects the extent to which the population is literate and has attained an adequate level of education. We operationalize literacy as the percentage of adult citizens who can read and write with understanding, and the overall level of education as the proportion of the school-going age population enrolled in primary, secondary, or tertiary educational institutions [58]. Other potential operationalizations of literacy (e.g., average expected years of schooling) and education (e.g., proportion of skilled professionals in the workforce) are not pursued here due to the lack of crosscountry data over time.

We suggest a twofold mechanism through which human capital can facilitate e-Government maturity. The primary impact of human capital arises from the demand it creates for e-Government services; such services are mostly useful to those who can to read, understand, and navigate software interfaces. A review by Jaeger (2006) [31] con<sup>fi</sup>rms the role of education in internet use. Similarly, Zhao et al. (2007) [94] conclude that the educated are better able to overcome ICT complexity to utilize e-Government services.

A more educated citizenry, aware of developments in neighboring countries and around the world, is more likely to demand e-Government. Berry and Berry (2014) [11] postulate “citizen pressure” as one of four forces behind policy change, and Lee et al. (2011) [44] found empirical support for citizen pressure (using the human capital index as one of its indicators) as a correlate of e-Government adoption in countries covered by the 2008 UN e-Government report.

A secondary effect of human capital on e-Government maturity may arise through the supply of skills in a nation’s workforce capable of rolling out sophisticated ICT applications. As we limit our measure of human capital to basic literacy (as opposed to highend ICT skills), we are not in a position to explore this effect of human capital on e-Government.

On the basis of the above reasoning, we cast our hypothesis about the role of human capital as follows:

Hypothesis 3. Increase in a country’s human capital is positively associated with an increase in e-Government maturity over time.

Governance: Governance refers to “the traditions and institutions by which authority is exercised in a country” [35]. As e-Government involves the embedding of digital technology in the social process of governing a country, we might expect that a nation’s e-Government maturity re<sup>fl</sup>ects how it is governed (Huang, 2007) [27]. Ciborra (2005) and Ciborra and Navarra (2003) [15,16] examine how weak governance (in terms of the accountability and transparency of incumbent governments) constrains the delivery of e-Government, with speci<sup>fi</sup>c reference to an aid-funded initiative in the Kingdom of Jordan.

At the technical level, e-Government does provide interested governments a way to engage citizens (for consultation, feedback, or dialogue) who might have earlier kept away from participation due to concerns about public visibility [56]. The implementation of e-Government also demands a certain level of government transparency because it requires the codi<sup>fi</sup>cation of business rules. In this way, responsibility for policy execution shifts from the discretion of street-level bureaucrats toward impartial “processors,” reducing the potential for arbitrary interpretation [52]. However, from an institutional perspective [49], only governments that seek to promote these values engagement and transparency are likely to pursue higher levels of maturity in e-Government. Governments that are unstable, corrupt, or do not enjoy the widespread mandate of their citizens, are unlikely to embrace e-Government beyond basic information publishing (mainly propaganda; [63].

Good governance, as manifested in the six dimensions of Kaufmann et al. (2010) [35] – voice and accountability, political stability and absence of violence, government effectiveness, regulatory quality, rule of law, and control of corruption is also often associated with the increasing professionalization of the civil service and closer links with the citizenry. The role of institutions on e-Government diffusion has been studied extensively, and their progress or regress has been clearly demonstrated (e.g. [32,85,34,23,39]. The expectation that e-Government deployment in a country will respond to the overarching structures and processes of governance in the country guides our <sup>fi</sup>nal hypothesis:

Hypothesis 4. Improvements in a country’s quality of governance are positively associated with an increase in e-Government maturity over time.

Fig. 1 depicts the conceptual model we test in this paper using mixed-effect regression analysis of panel data.

A. Das et al. / Information & Management xxx (2016) xxx–xxx

![](/api/attachments/WDA39N3C/fulltext/images/54db7f4f61d3663f9575cbcb9ce3c2673770ae6bd9d6b536b3d8d04c81780bdf.jpg)  
Fig. 1. Proposed Conceptual Model.

## 3. Method

## 3.1. Data and measures

Countries form the natural unit of analysis in this study. Accordingly, we assembled data for 191 countries using established sources of secondary data. The nature of our data sources for this study offers two important advantages. First, it enables replication, critique, and extension of our results using publicly (and freely) available data. Second, the broad coverage (including almost all countries in the world) assures that our <sup>fi</sup>ndings are truly generalizable and free from selection-related biases. The process of assembling the data set has been described below.

Our measure of e-Government Maturity is obtained from West (2002; 2003; 2004; 2005; 2006; 2007; 2008) [78–84]. Given our interpretation of e-Government maturity as demonstrated behaviors rather than just potential, we <sup>fi</sup>nd West’s measure the most thorough quantitative report available. West and his associates at the Inside Politics research center at Brown University examined >1500 government web sites from >190 countries in the summer of each year. Included among them were the web sites of the executive, legislative, and judicial branches of government, and the sites of cabinet of<sup>fi</sup>ces and key agencies serving important functions such as health, taxation, education, interior, economic development, administration, tourism, transportation, military, and business regulation. Websites for subnational units and local regional/municipal government units were not included in their study.

On the basis of a comprehensive examination of the characteristics of government web sites, West and his colleagues scored each country on a maximum of 100 points. These characteristics include:

1. online publications,

2. online databases

3. the use of audio and video

4. support for nonnative languages or foreign language translation

5. free access (as opposed to paid access, a negative feature)

6. commercial advertising (another negative feature)

7. access for the disabled

8. a privacy policy

9. security features

10. the presence and breadth of online services,

11. support for digital signatures and credit card payments,

12. an e-mail address for questions/concerns, comment forms,

13. provision of automatic e-mail updates,

14. website personalization, and

15. access from non-PC devices such as handheld computers [82].

Non-English web sites were translated by foreign language readers.

West’s measures of e-Government maturity are available for all years from 2002 to 2008. However, [79] introduced some changes to the methodology of measurement from 2002 to 2003, rendering the 2002 series dif<sup>fi</sup>cult to compare with the data for the remaining years. We model e-Government maturity as a 1-year lagged function of the independent variables: time, GDP per capita, infrastructure index, human capital index, and governance index, to capture the delay between changes in the independent variables and changes in e-Government maturity, improving the ability to evaluate causality. The 1-year lag also means that the discordant values of e-Government reported by West for the year 2002, though reported in the summary statistics, do not actually enter the estimation of our models, as we do not include the values of the independent variables from the previous year (2001) in our data set.

The time-series of per-capita PPP-adjusted GDP of different countries each year from 2002 to 2008 (in 2010 international dollars) were drawn from the archive of the World Economic Outlook databases stored at the web site http://www.imf.org external/ns/cs.aspx?id=28. We used the 2010 World Economic Outlook data series [29] to reduce the effect of changes in the de<sup>fi</sup>nition of the international dollar (also called the Geary-Khamis dollar) over the years.

Our measure for ICT Infrastructure is an index composed of three equally weighted components: Internet subscribers per 1000 people, broadband connections per 1000 people, and mobile subscriptions per 1000 people. This index re<sup>fl</sup>ects the range of technologies used to deliver most e-Government applications, and the relative scarcity of connectivity vis-à-vis standalone computing. The raw data are taken from the 2011 Yearbook of Statistics of the International Telecommunication Union (ITU), which contains the telecommunication/ICT indicators for the preceding 10-year period from 2001 to 2010 [30]. Because of the 1-year lag in our models, the last year from which infrastructure index is actually used for estimation is 2007; hence, we did not complete the manual computation of these indices for 2008. Our index corresponds reasonably well with the digital development (DigiDev) factor extracted by Cruz-Jesus et al. (2016) [18] from a variety of ICT-related measures, except for the exclusion of computer penetration from our index (we think that increasing use of mobile phones and tablets provide a viable alternative to traditional PCs and laptops for accessing e-Government applications).

Once again, we did not use the technology infrastructure index computed by UNPAN (2003; 2004; 2005; 2008; 2010) [72–76] because

it included (in the earlier years) components such as TV ownership and the density of <sup>fi</sup>xed-line telephones (both being somewhat distant from e-Government), and

the components of the UNPAN index and their relative weightages underwent material changes over the period of our study, compromising comparability across the years.

Our measure for Human Capital is similar to the “education index” described in the abovementioned UNPAN reports from 2003 to 2008, which in turn draw their data from the UNESCO. The human capital index is a combination of the adult literacy rate (de<sup>fi</sup>ned as the percentage of people aged >15 years who can read and write with understanding a short statement on their everyday life) and the combined gross enrolment ratio of primary, secondary, and tertiary schools in a country. The latter refers to the percentage of school-age population enrolled in any educational institution, and contributes one-third of the <sup>fi</sup>nal HCI measure, with the remaining two-thirds coming from the adult literacy rate. The human capital index ranges from zero to one.

According to our study, UNPAN shifted the basis of its education index from enrolment ratio to mean (and expected) years of schooling. Because of this change, our measure of human capital (two-thirds literacy and one-third gross enrolment ratio) had to be computed manually from the statistics provided in the annual Human Development Reports [65–71].

The time-series measures for Governance were developed by Kaufmann et al. [35]. These indicators are aggregated from >200 variables, collected from 25 separate data sources created by 18 different organizations, such as Freedom House, the Economist Intelligence Unit, and the U.S. State Department. Kaufmann et al. (2010) [35] de<sup>fi</sup>ne governance broadly as the traditions and institutions by which authority is exercised in a country; based on this de<sup>fi</sup>nition, they cluster its indicators into six dimensions using an unobserved component model. The dimensions of governance Kaufmann et al. (2010) [35] arrive at are: voice and accountability, political stability, government effectiveness, regulatory quality, rule of law, and control of corruption. Each year, across all countries, each of the six dimensions of governance is standardized, that is, normally distributed with a mean of zero and a standard deviation of one. Higher scores correspond to better governance, and virtually all scores fall between 2.5 and +2.5.

To improve the stability of estimation, we expressed GDP per capita in thousands of dollars, and rescaled (multiplied) the human capital and governance indices by a factor of 100 for inclusion in our regression model.

Table 1 shows the descriptive statistics for independent and dependent variables over the years.

Subsequently, we present the pairwise correlations among the independent variables (lagged by 1 year) and the dependent variable: The pairwise correlations in Table 2, among the independent variables, and between them and the dependent variable, are all positive and statistically signi<sup>fi</sup>cant.

## 3.2. Data analysis

Panel data aim to overcome one of the main weaknesses of cross-sectional studies: endogeneity originating from the omission of potentially relevant predictor variables, which can bias the estimates of both intercepts and slopes [86]. Panel data also reveal dynamic relationships between predictor and dependent variables as they unfold over time, which is not possible with cross-sectional data.

To make the most of the opportunity that panel data afford, we need to adopt an appropriate method of data analysis. Ordinary least square (OLS) regression is clearly inappropriate for the analysis of panel data. Each unit of observation (a country, in our case) contributes multiple observations to our data, but these observations are more likely to be correlated rather than independent (as assumed in OLS regression). Less obvious, but equally signi<sup>fi</sup>cant, is the fact that observations from a particular point in time (a year, in our case) might also be correlated, leading to further violation of OLS assumptions.

In our mixed linear model, we recognize the correlations among the e-Government maturity scores of the same country at different points in time. Individual-speci<sup>fi</sup>c, time-invariant, unobserved heterogeneity (e.g., geography or culture) is captured using these multiple data from each country (and likewise for each point in time, for which there are data from multiple countries). The <sup>fi</sup>xedeffects part of our model effectively incorporates proxies for individual country [17], giving up (n-1) degrees of freedom corresponding to the n units under observation. Computationally, we use an estimation procedure (restricted maximum-likelihood (REML) estimation) that explicitly accounts for the loss of these degrees of freedom while estimating the random effects without bias.

Mixed-effect models have a <sup>fi</sup>xed-effect component analogous to traditional regression [57]. The random-effects component gives structure to the error term remaining after <sup>fi</sup>tting the <sup>fi</sup>xed effects by admitting different intercepts (and slopes for regressor variables) for different units (countries, in our case). In this respect, mixed-effects models allow more <sup>fl</sup>exible modeling of panel data than repeated measure ANOVA; unlike ANOVA, they also allow the inclusion of time-varying covariates. Mixed-effect models are mathematically equivalent to hierarchical linear models (HLMs) and growth curve models (GCMs). All of these models stand in contrast to OLS regression by recognizing the within-unit correlations in panel data.

In a mixed-effect model, each country is allowed to have its own intercept and slope (over time) to re<sup>fl</sup>ect the reality that different countries start the period of study (2003–2007) at different initial levels of e-Government maturity, and also grow at different rates from these initial levels. Barr et al. (2013) [10] advise researchers to keep linear mixed models “maximal” in the sense of including all

Table 1  
Means and standard deviations (SD) of independent and dependent variables.

<table><tr><td rowspan="2">Year</td><td colspan="2">e-Gov index</td><td colspan="2">GDP per capita</td><td colspan="2">Infrastructure index</td><td colspan="2">Human capital index</td><td colspan="2">Governance index</td></tr><tr><td>Mean</td><td>Std. Error</td><td>Mean</td><td>Std. Error</td><td>Mean</td><td>Std. Error</td><td>Mean</td><td>Std. Error</td><td>Mean</td><td>Std. Error</td></tr><tr><td>2002</td><td>40.67</td><td>0.59</td><td>9.64</td><td>0.87</td><td>16.23</td><td>1.31</td><td>77.28</td><td>1.46</td><td>-2.91</td><td>6.91</td></tr><tr><td>2003</td><td>27.24</td><td>0.44</td><td>10.08</td><td>0.90</td><td>17.25</td><td>1.38</td><td>77.88</td><td>1.45</td><td>-2.54</td><td>6.90</td></tr><tr><td>2004</td><td>25.34</td><td>0.40</td><td>10.75</td><td>0.96</td><td>17.39</td><td>1.40</td><td>78.12</td><td>1.42</td><td>-3.20</td><td>6.91</td></tr><tr><td>2005</td><td>25.75</td><td>0.46</td><td>11.89</td><td>1.07</td><td>14.85</td><td>1.23</td><td>78.79</td><td>1.46</td><td>-2.83</td><td>7.20</td></tr><tr><td>2006</td><td>27.54</td><td>0.49</td><td>12.10</td><td>1.06</td><td>20.95</td><td>1.57</td><td>76.91</td><td>1.47</td><td>-4.62</td><td>6.82</td></tr><tr><td>2007</td><td>30.45</td><td>0.55</td><td>12.73</td><td>1.10</td><td>21.26</td><td>1.62</td><td>78.10</td><td>1.40</td><td>-6.19</td><td>6.78</td></tr><tr><td>2008</td><td>30.89</td><td>0.55</td><td>13.50</td><td>1.08</td><td colspan="2">Not available</td><td colspan="2">Not available</td><td>-7.05</td><td>6.59</td></tr></table>

Table 2  
Pairwise correlations.

<table><tr><td></td><td>e-Gov index</td><td>GDP per capita (lag 1)</td><td>Infrastructure index (lag 1)</td><td>Human capital index (lag 1)</td><td>Governance index (lag 1)</td></tr><tr><td>e-Gov index</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>GDP per capita (lag 1)</td><td> $0.510^{**}$ </td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Infrastructure index (lag 1)</td><td> $0.540^{**}$ </td><td> $0.829^{**}$ </td><td>1.000</td><td></td><td></td></tr><tr><td>Human capital index (lag 1)</td><td> $0.382^{**}$ </td><td> $0.539^{**}$ </td><td> $0.625^{**}$ </td><td>1.000</td><td></td></tr><tr><td>Governance index (lag 1)</td><td> $0.412^{**}$ </td><td> $0.753^{**}$ </td><td> $0.824^{**}$ </td><td> $0.559^{**}$ </td><td>1.000</td></tr></table>

Signi<sup>fi</sup>cant at 0.01 level.

Please cite this article in press as: A. Das, et al., A longitudinal study of e-government maturity, Inf. Manage. (2016), http://dx.doi.org/10.1016/j. im.2016.09.006

A. Das et al. / Information & Management xxx (2016) xxx–xxx

theoretically justi<sup>fi</sup>ed random effects. Accordingly, we also set the variance–covariance structure of the random effects intercept and slope to be the most general (unstructured).

In our random-intercept models, the level of the dependent variable egov for country i in year t is made up of the following components:

the <sup>fi</sup>xed intercept $\beta _ { 1 }$ for all units,

<sub></sub> the country-speci<sup>fi</sup>c random intercept $U _ { 1 i }$ for country $i ,$

the <sup>fi</sup>xed slope $\beta _ { j }$ (along the independent variable $x _ { j }$ for each country $i ) ,$ and

the random error $\varepsilon _ { i t }$ for country i in year t

where

$$
U _ {1 i} \sim N (0, \tau^ {2}) \text {   and   } \varepsilon_ {i t} \sim N (0, \sigma^ {2}).
$$

Allowing random variation in slopes (over time) across countries adds another component to $e g o v _ { i t }$

the random slope on time $U _ { 2 i }$ for each country i

with $U _ { 1 { \mathrm { : } } }$ <sub>i</sub>and $U _ { 2 i }$ distributed (multivariate) normally as $\binom { U _ { 1 i } } { U _ { 2 i } } \sim M V N \biggl ( \left( \begin{array} { l } { { 0 } } \\ { { 0 } } \end{array} \right) , \left( \begin{array} { l l } { { \tau _ { 1 1 } } } & { { \tau _ { 1 2 } } } \\ { { \tau _ { 2 1 } } } & { { \tau _ { 2 2 } } } \end{array} \right) \biggr )$

We start by examining the growth of e-Government maturity over time without regard to the effect of GDP per capita, infrastructure, human capital, or governance. We build a model of the <sup>fi</sup>xed effect of time and the random effect (intercept) of country.

1. Unconditional random-intercept model: For country i in year t

$$
e g o v _ {i t} | t i m e, U _ {1 i} = \beta_ {1} + \beta_ {2} t i m e _ {t} + U _ {1 i} + \varepsilon_ {i t}
$$

where

$$
U _ {1 i} \sim \mathrm{N} (0, \tau^ {2}) \text { and } \varepsilon_ {i t} \sim N (0, \sigma^ {2})\tag{1}
$$

Grouping the <sup>fi</sup>xed and random components of the intercept (1), may be rewritten as

$$
e g o v _ {i t} | t i m e, U _ {1 i} = \left(\beta_ {1} + U _ {1 i}\right) + \beta_ {2} t i m e _ {t} + \varepsilon_ {i t}
$$

The following coef<sup>fi</sup>cients were estimated by the REML method, which explicitly accounts for the degrees of freedom consumed in estimating the <sup>fi</sup>xed effects, thus providing unbiased estimates of the random effects. For this model, and for all other models, estimation was repeated with full (i.e., unrestricted) maximum likelihood estimation (MLE), which produces slightly biased estimates with tighter con<sup>fi</sup>dence intervals. All results remained the same, and the difference in coef<sup>fi</sup>cient estimates between the two procedures never exceeded 2% for signi<sup>fi</sup>cant coef<sup>fi</sup>cients. Such stability is expected for large sample sizes, and gives us greater con<sup>fi</sup>dence in our results.

Model 1 in Table 3 shows that the typical country’s e-Government maturity rises by 1.054 units each year. However, different countries begin the observation period at different levels of e-Government maturity, and this variation in starting points is re<sup>fl</sup>ected in the signi<sup>fi</sup>cant random-effect parameter which has a 95% con<sup>fi</sup>dence interval of (4.339, 5.471). We conclude that the majority of countries started the observation period with an e-Government maturity level of ${ 2 3 \pm 5 }$ points, thereafter increasing approximately 1% every year.

The inclusion of the theorized predictor variables GDP per capita, infrastructure, human capital, and governance, each lagged by a year leads to the formulation of our second model. Model 2 (see Table 4) retains the varying intercepts and the constant slope over time, adding coef<sup>fi</sup>cients for the predictors (covariates), all of which also vary over time.

2. Random-intercept model with time-varying covariates: For country i in year t

$$
\begin{array}{l} e g o v _ {i t} | g d p k, i n f r a, h u m c a p, g o v c e, t i m e, U _ {1 i} \\ \quad = \beta_ {1} + \beta_ {2} g d p k _ {i (t - 1)} + \beta_ {3} i n f r a _ {i (t - 1)} + \beta_ {4} h u m c a p _ {i (t - 1)} \\ \quad + \beta_ {5} g o v c e _ {i (t - 1)} + \beta_ {6} t i m e _ {t} + U _ {1 i} + \varepsilon_ {i t} \end{array}
$$

where

$$
U _ {1 i} \sim \mathrm{N} (0, \tau^ {2}) \text { and } \varepsilon_ {i t} \sim N (0, \sigma^ {2})\tag{2}
$$

Grouping the intercept terms together,

egov<sub>it</sub> gdpk; inf ra; humcap; govce; time; $U _ { 1 i }$

$$
\begin{array}{l} = (\beta_ {1} + U _ {1 i}) + \beta_ {2} g d p k _ {i (t - 1)} + \beta_ {3} i n f r a _ {i (t - 1)} + \beta_ {4} h u m c a p _ {i (t - 1)} \\ \quad + \beta_ {5} g o v c e _ {i (t - 1)} + \beta_ {6} t i m e _ {t} + \varepsilon_ {i t} \end{array}
$$

The following coef<sup>fi</sup>cients were estimated by the REML procedure.

Inclusion of the time-varying covariates reduces the slope of e-Government over time to 0.862, with additional positive contributions from GDP per capita $\left( _ { \beta 2 } = 0 . 1 2 9 \right)$ and infrastructure $\big ( _ { \beta 3 } = 0 . 0 9 3 \big )$ . In Model 2, the intercept of e-Government maturity (in 2003) varies in the 19 3 range for the majority of countries. Later, it increases by approximately 0.862 units every year. An extra unit of GDP per capita (measured in thousands of dollars) adds 0.129 units to e-Government maturity. A one point improvement in the (rescaled) infrastructure index yields an additional 0.093 units of e-Government maturity.

Not only can countries enter the observation period at different levels of e-Government maturity but they can also develop at different rates over time due to geographical and cultural factors (among others). Subsequently, we develop a pair of models where the slope of e-Government maturity over time is also allowed to

Unconditional random-intercept model.

<table><tr><td rowspan="2">Model 1</td><td colspan="2">Number of observations: 1142</td><td colspan="2">Group variable: nation</td><td colspan="2">Number of groups: 191</td></tr><tr><td colspan="6">Observations per group: minimum: 3, maximum: 6, average: 6</td></tr><tr><td rowspan="2">Log-restricted likelihood = -3562.236</td><td></td><td>Wald chi $^{2}$  (5)</td><td>173.75</td><td>Prob &gt; chi $^{2}$ </td><td>0.000</td><td></td></tr><tr><td>Coef.</td><td>Std. Err.</td><td>z</td><td>P &gt; |z|</td><td colspan="2">95% Confidence Interval</td></tr><tr><td>time</td><td>1.054</td><td>0.080</td><td>13.18</td><td>0.000**</td><td>0.897</td><td>1.211</td></tr><tr><td>intercept</td><td>22.902</td><td>0.522</td><td>43.89</td><td>0.000**</td><td>21.879</td><td>23.924</td></tr><tr><td>Random-effect parameters</td><td>Estimate</td><td>Std. Err.</td><td colspan="2">95% Confidence Interval</td><td></td><td></td></tr><tr><td>nation: Identity</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sd (intercept)</td><td>4.872</td><td>0.288</td><td>4.339</td><td>5.471</td><td></td><td></td></tr><tr><td>Sd (residual)</td><td>4.616</td><td>0.106</td><td>4.413</td><td>4.829</td><td></td><td></td></tr></table>

Signi<sup>fi</sup>cant at 0.01 level.

Please cite this article in press as: A. Das, et al., A longitudinal study of e-government maturity, Inf. Manage. (2016), http://dx.doi.org/10.1016/j. im.2016.09.006

A. Das et al. / Information & Management xxx (2016) xxx–xxx

Table 4  
Random-intercept model with time-varying covariates.

<table><tr><td rowspan="2">Model 2</td><td colspan="2">Number of observations: 1025</td><td colspan="2">Group variable: nation</td><td colspan="2">Number of groups: 177</td></tr><tr><td colspan="6">Observations per group: minimum: 1, maximum: 6, average: 5.8</td></tr><tr><td rowspan="2">Log-restricted likelihood = -3108.165</td><td></td><td>Wald chi $^{2}$  (5)</td><td>353.11</td><td>Prob &gt; chi $^{2}$ </td><td>0.0000</td><td></td></tr><tr><td>Coef.</td><td>Std. Err.</td><td>z</td><td>P &gt; |z|</td><td colspan="2">95% Confidence Interval</td></tr><tr><td>L1.gdpk</td><td>0.129</td><td>0.035</td><td>3.66</td><td>0.000**</td><td>0.060</td><td>0.198</td></tr><tr><td>L1.infra</td><td>0.093</td><td>0.025</td><td>3.73</td><td>0.000**</td><td>0.044</td><td>0.142</td></tr><tr><td>L1.humcap</td><td>0.022</td><td>0.018</td><td>1.22</td><td>0.224</td><td>-0.014</td><td>0.058</td></tr><tr><td>L1.govce</td><td>0.001</td><td>0.005</td><td>0.29</td><td>0.775</td><td>-0.009</td><td>0.012</td></tr><tr><td>time</td><td>0.862</td><td>0.084</td><td>10.21</td><td>0.000**</td><td>0.696</td><td>1.027</td></tr><tr><td>intercept</td><td>19.197</td><td>1.434</td><td>13.38</td><td>0.000**</td><td>16.386</td><td>22.009</td></tr><tr><td>Random-effect parameters</td><td>Estimate</td><td>Std. Err.</td><td colspan="2">95% Confidence Interval</td><td></td><td></td></tr><tr><td colspan="7">Nation: Identity</td></tr><tr><td>Sd (intercept)</td><td>3.174</td><td>0.233</td><td>2.749</td><td>3.666</td><td></td><td></td></tr><tr><td>Sd (residual)</td><td>4.403</td><td>0.107</td><td>4.198</td><td>4.618</td><td></td><td></td></tr></table>

Signi<sup>fi</sup>cant at 0.01 level.

Table 5  
Unconditional random-slope model.

<table><tr><td rowspan="2">Model 3</td><td colspan="3">Number of observations: 1142</td><td>Group variable: nation</td><td colspan="2">Number of groups: 191</td></tr><tr><td colspan="6">Observations per group: minimum: 3, maximum: 6, average: 6</td></tr><tr><td rowspan="2">Log-restricted likelihood = -3530.948</td><td></td><td>Wald chi $^{2}$  (5)</td><td>103.29</td><td>Prob &gt; chi $^{2}$ </td><td>0.0000</td><td></td></tr><tr><td>Coef.</td><td>Std. Err.</td><td>z</td><td>P&gt; |z|</td><td colspan="2">95% Confidence Interval</td></tr><tr><td>time</td><td>1.050</td><td>0.103</td><td>10.16</td><td>0.000**</td><td>0.848</td><td>1.253</td></tr><tr><td>intercept</td><td>22.914</td><td>0.494</td><td>46.34</td><td>0.000**</td><td>21.945</td><td>23.883</td></tr><tr><td>Random-effects parametersnation: Unstructured</td><td>Estimate</td><td>Std. Err.</td><td colspan="4">95% Confidence Interval</td></tr><tr><td>Sd (time)</td><td>1.011</td><td>0.107</td><td>0.822</td><td>1.244</td><td></td><td></td></tr><tr><td>Sd (intercept)</td><td>4.812</td><td>0.513</td><td>3.905</td><td>5.930</td><td></td><td></td></tr><tr><td>Corr (time, intercept)</td><td>-0.444</td><td>0.110</td><td>-0.633</td><td>-0.206</td><td></td><td></td></tr><tr><td>Sd (residual)</td><td>4.213</td><td>0.108</td><td>4.006</td><td>4.430</td><td></td><td></td></tr></table>

Signi<sup>fi</sup>cant at 0.01 level.

vary across countries (in addition to varying intercepts). Model 3 below (see Table 5) estimates the level and variability of intercepts and slopes over time without regard to the covariates GDP per capita, infrastructure, human capital, and governance.

3. Unconditional random-slope model (includes random intercepts): For country i in year t

$$
e g o v _ {i t} \mid t i m e, U _ {1 i}, U _ {2 i} = \beta_ {1} + \beta_ {2} t i m e _ {t} + U _ {1 i} + U _ {2 i} t i m e _ {t} + \varepsilon_ {i t}
$$

where

$$
\binom{U _ {1 i}}{U _ {2 i}} \sim M V N \bigg (\binom{0}{0}, \left( \begin{array}{c c} \tau_ {1 1} & \tau_ {1 2} \\ \tau_ {2 1} & \tau_ {2 2} \end{array} \right) \bigg) \text {   and   } \varepsilon_ {i t} \sim N (0, \sigma^ {2})\tag{3}
$$

Alternatively,

$$
e g o v _ {i t} | t i m e, U _ {1 i}, U _ {2 i} = (\beta_ {1} + U _ {1 i}) + \beta_ {2} t i m e _ {t} + U _ {2 i} t i m e _ {t} + \varepsilon_ {i t}
$$

or,

$$
e g o v _ {i t} | t i m e, U _ {1 i}, U _ {2 i} = \left(\beta_ {1} + U _ {1 i}\right) + \left(\beta_ {2} + U _ {2 i}\right) t i m e _ {t} + \varepsilon_ {i t}
$$

The following coef<sup>fi</sup>cients were estimated by REML:

Letting the slope vary over countries leads to the same average value of slope on time as earlier (1.05), with a standard deviation of 1.011 across countries. The average value of the intercept is 22.914, with a standard deviation of 4.812 points. The negative correlation of slope and intercept shows that the slope (on time) is lower for countries with higher intercepts. Countries that start at lower levels of e-Government maturity (with more headroom) improve faster.

Our <sup>fi</sup>nal model retains random intercepts and slopes (over time) while accounting for the contributions of the time-varying covariates GDP per capita, infrastructure, human capital, and governance.

4. Random-slope model with time-varying covariates: For country i in year t

$$
\begin{array}{l} e g o v _ {i t} | g d p k, i n f r a, h u m c a p, g o v c e, t i m e, U _ {1 i}, U _ {2 i} \\ \quad = \beta_ {1} + \beta_ {2} g d p k _ {i (t - 1)} + \beta_ {3} i n f r a _ {i (t - 1)} + \beta_ {4} h u m c a p _ {i (t - 1)} \\ \quad + \beta_ {5} g o v c e _ {i (t - 1)} + \beta_ {6} t i m e _ {t} + U _ {1 i} + U _ {2 i} t i m e _ {t} + \varepsilon_ {i t} \end{array}
$$

where

$$
\binom{U _ {1 i}}{U _ {2 i}} \sim M V N \bigg (\binom{0}{0}, \left( \begin{array}{c c} \tau_ {1 1} & \tau_ {1 2} \\ \tau_ {2 1} & \tau_ {2 2} \end{array} \right) \bigg) \text {   and   } \varepsilon_ {i t} \sim N (0, \sigma^ {2})\tag{4}
$$

Grouping similar terms,

$$
\begin{array}{l} e g o v _ {i t} | g d p k, i n f r a, h u m c a p, g o v c e, t i m e, U _ {1 i}, U _ {2 i} \\ \quad = (\beta_ {1} + U _ {1 i}) + \beta_ {2} g d p k _ {i (t - 1)} + \beta_ {3} i n f r a _ {i (t - 1)} + \beta_ {4} h u m c a p _ {i (t - 1)} \\ \quad + \beta_ {5} g o v c e _ {i (t - 1)} + (\beta_ {6} + U _ {2 i}) t i m e _ {t} + \varepsilon_ {i t} \end{array}
$$

The following coef<sup>fi</sup>cients were estimated for Model 4 by REML (Table 6):

Introduction of the time-varying covariates reduces the average slope to 0.865, with a standard deviation of 1.002 across countries. The average value of the intercept is 19.332, with a standard deviation of 4.629 points. The strong negative correlation of 0.745 between slope and intercept shows that e-Government maturity grows faster for countries with lower starting levels (of e-Government maturity).

A. Das et al. / Information & Management xxx (2016) xxx–xxx

Table 6  
Random-slope model with time-varying covariates.

<table><tr><td rowspan="2">Model 4</td><td colspan="3">Number of observations: 1025</td><td>Group variable: nation</td><td colspan="2">Number of groups: 177</td></tr><tr><td colspan="6">Observations per group: minimum: 1, maximum: 6, average: 5.8</td></tr><tr><td rowspan="2">Log-restricted likelihood = -3082.919</td><td></td><td>Wald chi $^{2}$  (5)</td><td>271.89</td><td>Prob &gt; chi $^{2}$ </td><td>0.000</td><td></td></tr><tr><td>Coef.</td><td>Std. Err.</td><td>z</td><td>P&gt; |z|</td><td colspan="2">95% Confidence Interval</td></tr><tr><td>L1.gdpk</td><td>0.124</td><td>0.036</td><td>3.45</td><td>0.001**</td><td>0.054</td><td>0.195</td></tr><tr><td>L1.infra</td><td>0.097</td><td>0.024</td><td>4.05</td><td>0.000**</td><td>0.050</td><td>0.144</td></tr><tr><td>L1.humcap</td><td>0.020</td><td>0.018</td><td>1.12</td><td>0.262</td><td>-0.015</td><td>0.055</td></tr><tr><td>L1.govce</td><td>0.000</td><td>0.005</td><td>0.06</td><td>0.949</td><td>-0.010</td><td>0.010</td></tr><tr><td>time</td><td>0.865</td><td>0.108</td><td>7.99</td><td>0.000**</td><td>0.653</td><td>1.077</td></tr><tr><td>intercept</td><td>19.332</td><td>1.415</td><td>13.66</td><td>0.000**</td><td>16.558</td><td>22.106</td></tr><tr><td>Random-effect parameters</td><td>Estimate</td><td>Std. Err.</td><td colspan="4">95% Confidence Interval</td></tr><tr><td>nation: Unstructured</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sd (time)</td><td>1.002</td><td>0.106</td><td>0.815</td><td>1.233</td><td></td><td></td></tr><tr><td>Sd (intercept)</td><td>4.629</td><td>0.512</td><td>3.727</td><td>5.750</td><td></td><td></td></tr><tr><td>Corr (time, intercept)</td><td>-0.745</td><td>0.059</td><td>-0.840</td><td>-0.606</td><td></td><td></td></tr><tr><td>Sd (residual)</td><td>3.979</td><td>0.108</td><td>3.772</td><td>4.198</td><td></td><td></td></tr></table>

<sup>\*\*</sup> Signi<sup>fi</sup>cant at 0.01 level.

## 4. Results

Table 7 presents the coef<sup>fi</sup>cient estimates from our four models side-by-side.

For both pairs of models, random intercept and random slopes, the addition of the time-varying covariates GDP per capita, infrastructure, human capital, and governance improves model <sup>fi</sup>t as indicated by the log likelihood and the size of the residuals. The regression coef<sup>fi</sup>cients of the <sup>fi</sup>rst two covariates, GDP and infrastructure, are statistically signi<sup>fi</sup>cant.

The Hausman test, $\chi ^ { 2 } ( 5 ) = 4 . 7 3 , p = 0 . 4 4 9 ,$ shows that the random-slope model with time-varying covariates is consistent with the random-intercept model (with time-varying covariates) while being more ef<sup>fi</sup>cient, with smaller residuals and tighter con<sup>fi</sup>dence intervals. The likelihood ratio (LR) test, x<sup>2</sup> 2 50:49; p 0:000, also shows that the random-slope model with time-varying covariates <sup>fi</sup>ts the data signi<sup>fi</sup>cantly better than the random-intercept model (with time-varying covariates) after accounting for the additional degrees of freedom consumed. REML allows LR tests to compare models with identical <sup>fi</sup>xed-effect components and nested random effects (true in our case).

We thus choose Model 4 with random slopes (and random intercepts) as the best-<sup>fi</sup>tting model for our data. Our preference for the random-slope model follows the advice of Barr et al. (2013) [10] to keep linear mixed models maximal in order to correctly capture the random-effect structure of the data. Maximal models have more “expressive power” to represent the random-effect structure present in the data. The column of coef<sup>fi</sup>cient estimates from this model is shaded in Table 7 above.

Table 8 below summarizes our main results (based on Model 4).

Most, but not all, countries improved in e-Government maturity over the period of our study, 2002–2008. There is signi<sup>fi</sup>cant heterogeneity among countries in both intercept (starting points) and slope (rate of change over time) in their achievement of e-Government maturity.

In the aggregate, the rate of growth is slower for countries already at high levels of e-Gov maturity (negative correlation between slope and intercept). This suggests that it is easier to establish a minimal level of e-Gov maturity, but harder to make progressive improvements.

Our results support Hypotheses 1 (Af<sup>fl</sup>uence) and 2 (ICT Infrastructure), but not Hypotheses 3 (Human Capital) and 4 (Governance). In other words, only GDP per capita and ICT infrastructure are signi<sup>fi</sup>cantly associated with rising e-Government maturity over time. This pattern of results suggests that GDP and ICT infrastructure may be suf<sup>fi</sup>cient conditions for e-Government maturity, as measured by West and associates. In other words, it might be possible for a country, willing and able to make investment in technological capabilities, to advance its e-Government maturity without necessarily rebuilding public sector processes as described by Andersen and Henrikson (2006) [2].

In agreement with other research on the topic, GDP per capita and the infrastructure index make signi<sup>fi</sup>cant positive contributions to e-Government maturity, but the contributions of the human capital and governance indices fail to reach statistical

Model comparison.

<table><tr><td rowspan="2">Variable</td><td colspan="2">Random intercept (no covariates)</td><td colspan="2">Random intercept (time-varying covariates)</td><td colspan="2">Random slope (no covariates)</td><td colspan="2">Random slope (time-varying covariates)</td></tr><tr><td>coeff</td><td>p-value</td><td>coeff</td><td>p-value</td><td>coeff</td><td>p-value</td><td>coeff</td><td>p-value</td></tr><tr><td>GDP per capita</td><td></td><td></td><td>0.129</td><td>0.000**</td><td></td><td></td><td>0.124</td><td>0.000**</td></tr><tr><td>infrastructure index</td><td></td><td></td><td>0.093</td><td>0.000**</td><td></td><td></td><td>0.097</td><td>0.000**</td></tr><tr><td>human capital index</td><td></td><td></td><td>0.022</td><td>0.224</td><td></td><td></td><td>0.020</td><td>0.262</td></tr><tr><td>governance index</td><td></td><td></td><td>0.001</td><td>0.775</td><td></td><td></td><td>0.000</td><td>0.949</td></tr><tr><td>time</td><td>1.054</td><td>0.000**</td><td>0.862</td><td>0.000**</td><td>1.050</td><td>0.000**</td><td>0.865</td><td>0.000**</td></tr><tr><td>intercept</td><td>22.902</td><td>0.000**</td><td>19.197</td><td>0.000**</td><td>22.914</td><td>0.000**</td><td>19.332</td><td>0.000**</td></tr><tr><td>Sd (slope on time)</td><td></td><td></td><td></td><td></td><td>1.011</td><td></td><td>1.002</td><td></td></tr><tr><td>Sd (intercept)</td><td>4.872</td><td></td><td>3.174</td><td></td><td>4.812</td><td></td><td>4.629</td><td></td></tr><tr><td>Corr (time, intercept)</td><td></td><td></td><td></td><td></td><td>-0.444</td><td></td><td>-0.745</td><td></td></tr><tr><td>Sd (residual)</td><td>4.616</td><td></td><td>4.403</td><td></td><td>4.213</td><td></td><td>3.977</td><td></td></tr><tr><td>Wald chi-square (5 df)</td><td>173.75</td><td></td><td>353.11</td><td></td><td>103.29</td><td></td><td>271.89</td><td></td></tr><tr><td>Log likelihood</td><td>-3562</td><td></td><td>-3108</td><td></td><td>-3531</td><td></td><td>-3083</td><td></td></tr></table>

Signi<sup>fi</sup>cant at 0.01 level.

Please cite this article in press as: A. Das, et al., A longitudinal study of e-government maturity, Inf. Manage. (2016), http://dx.doi.org/10.1016/j. im.2016.09.006

A. Das et al. / Information & Management xxx (2016) xxx–xxx

## Table 8

Summary of Results.

<table><tr><td>Variable</td><td>Coefficient</td><td>What it signifies</td></tr><tr><td>Intercept: fixed effect</td><td>19.332</td><td>Average level of West&#x27;s e-Government maturity measure for all countries in 2003 at zero levels of GDP per capita, infrastructure, human capital, and governance in the previous year</td></tr><tr><td>Intercept: random effect</td><td>4.629</td><td>Average variation in the intercept among countries</td></tr><tr><td>Time: fixed effect</td><td>0.865</td><td>On average, West&#x27;s e-Government maturity score for a country increases by 0.865 units every year</td></tr><tr><td>Time: random effect</td><td>1.002</td><td>Average variation in the slope among countries (some countries show negative slope)</td></tr><tr><td>GDP per capita</td><td>0.124</td><td>A $1000 increase in a country&#x27;s GDP per capita is associated with an increase of 0.124 in its e-Government maturity score</td></tr><tr><td>ICT Infrastructure</td><td>0.097</td><td>A 1-point increase in a country&#x27;s infrastructure score (scaled to 100) is associated with an increase of 0.097 in its e-Government maturity score</td></tr></table>

signi<sup>fi</sup>cance. Theory, as well as prior research based on crosssectional analysis, raised expectations that e-Government maturity would be in<sup>fl</sup>uenced signi<sup>fi</sup>cantly by human capital (an educated citizenry) and good governance (transparency, accountability, and effectiveness). That e-Government can develop, indeed <sup>fl</sup>ourish, without signi<sup>fi</sup>cant dependence on these two factors human capital and governance alerts us that the type of e-Government we are developing (and measuring) viewing the citizen predominantly as a consumer of government services is primarily an “infrastructure play.” In addition, the maturity of e-Government in a country does not signal higher levels of human capital or good governance. Proponents of e-Government as a vehicle for administrative reform are likely to be disappointed, but other research, notably Kraemer and King (1986; 2006) [37,38], has often argued that the ruling elites are likely to appropriate technology in their own interests to maintain the status quo. Of course, we must also acknowledge that our overall understanding of e-Government adoption (including the challenges and barriers) lags behind the research on supply-side issues (deployment of e-Government). Rana et al. (2013) [51] note that this imbalance of understanding is re<sup>fl</sup>ected in the number of studies: supply-side 53 vs. demand-side 18.

## 5. Discussion

We undertook this study to identify factors that are associated with e-Government maturity over time. To do so, we assembled a panel data set using established secondary data sources, and analyzed it with random-effect models. Table 9 below shows a comparison of our study with a few others that examine the antecedents of e-Government maturity.

Table 9 shows that only I<sup>fi</sup>nedo (2011) [28] and this paper have used panel data to investigate the antecedents of e-Government maturity. However, use of OLS regression to estimate the effect of predictor variables is problematic for reasons mentioned in the earlier section. Across all these studies, GDP and ICT infrastructure are the only consistent predictors of e-Government maturity. Human capital and governance are the two predictors that are often signi<sup>fi</sup>cant in cross-sectional analysis, and do not hold up under our more stringent longitudinal analysis. To reiterate, our results do not indicate that the e-Government maturity of a country goes up (or down) as its human capital and governance go up (or down).

We must note that our results are robust to increase the lag between GDP and e-Government maturity to 2 years (leaving other independent variables with 1-year lags). The rationale for trying a longer lag for GDP was that the delay between changes in GDP and its effect on e-Government maturity might be longer, thus the effect being potentially mediated by the other independent variables. On <sup>fi</sup>nding consistent results, we retained the results of our original model (all independent variables lagged by 1 year) as it fares better in terms of missing data; it is able to utilize one additional wave of panel data than the variant with a 2-year lag for

## Table 9

Comparison of Related Research.

<table><tr><td>Paper</td><td>Singh et al. [58]</td><td>Ifinedo [28]</td><td>Krishnan and Teo [39]</td><td>This paper (final model)</td></tr><tr><td>Design</td><td>Cross-sectional</td><td>Longitudinal</td><td>Cross-sectional</td><td>Longitudinal</td></tr><tr><td>Data</td><td>178 countries, year 2006</td><td>64 countries, years 2003, 2004, 2005, 2008, 2010</td><td>178 countries, year 2008</td><td>191 countries, years 2002 through 2008</td></tr><tr><td>Analysis technique</td><td>Path analysis</td><td>OLS regression</td><td>Moderated multiple regression, 2-year lag between DV and IVs</td><td>Random-slope model with time-varying covariates, 1-year lag between DV and IVs</td></tr><tr><td>Dependent variable</td><td>e-Gov maturity West [82]</td><td>Web measure+online service index (UNPAN [76])</td><td>Online service index (UNPAN [76])</td><td>e-Gov maturity [78] through 2008)</td></tr><tr><td colspan="5">Predictors</td></tr><tr><td>GDP</td><td>Positive, p&lt;0.01a</td><td>Positive, p=0.05</td><td>Positive, p&lt;0.01</td><td>Positive, p&lt;0.01</td></tr><tr><td>ICT infrastructure</td><td>Positive, p&lt;0.01</td><td>Positive, p=0.05</td><td>Positive, p&lt;0.01</td><td>Positive, p&lt;0.01</td></tr><tr><td>Human capital</td><td>Positive, p&lt;0.05</td><td>Positive, p&lt;0.01</td><td>Positive, p&lt;0.05</td><td>Not significant</td></tr><tr><td>Governance</td><td>Negative, p&lt;0.01b</td><td>Positive, p&lt;0.05c</td><td>Positive, p&lt;0.05d</td><td>Not significantb</td></tr><tr><td>Innovative capacity</td><td></td><td>Positive, p&lt;0.01</td><td></td><td></td></tr></table>

<sup>a</sup> Effects on ICT infra, human capital, and governance.  
<sup>b</sup> Composed of Voice and Accountability, Political Stability, Government Effectiveness, Regulatory Quality, Rule of Law, and Control of Corruption [35].  
<sup>c</sup> Signi<sup>fi</sup>cant variables: Rule of Law and Corruption Perceptions [64].  
<sup>d</sup> Signi<sup>fi</sup>cant variables: Political Stability, Government Effectiveness, and Rule of Law – main effects and interactions with ICT infrastructure.

A. Das et al. / Information & Management xxx (2016) xxx–xxx

GDP. More data (larger sample size) promise higher statistical power and more precise estimates.

The role of GDP has been acknowledged by almost all other researchers, except for Azad et al. (2010) [4] as noted earlier. Cruz-Jesus et al. (2016) [18], in fact, report a nonlinear effect of GDP, suggesting that its effect is greatest for poorer countries. Only after a certain level of af<sup>fl</sup>uence is reached do other variables start to have an effect on the maturity of e-Government. The strong link between af<sup>fl</sup>uence and e-Government maturity re<sup>fl</sup>ects the fact that developing e-Government services continues to be an expensive affair (despite the falling cost of computer hardware), allowing wealthier nations to still dominate most e-Government rankings [58]. The key role of GDP also raises some signi<sup>fi</sup>cant questions for the future of e-Government. As countries, such as some in Europe, embrace austerity in their <sup>fi</sup>scal policies, what will happen to their e-Government initiatives? As government expenditure decreases, will their e-Government maturity scores plateau and even decline?

Future research may be able to evaluate the particular elements of the ICT infrastructure (potentially involving mobile/wireless technology) that have greater impact on e-Government maturity. This could support the choice of ICT investments on a limited budget, potentially enabling poorer countries to spend their money wisely as they attempt to catch up with their more af<sup>fl</sup>uent counterparts.

With a large amount of data and careful statistical analysis, the lack of signi<sup>fi</sup>cance of either governance or human capital comes as a disappointment. The public administration literature is cautious about the potential of e-Government to transform the practice of government [6,19,38,47,48]. It now appears that, at least in the short term, we may be stuck with a “limited” form of e-Government (primarily transactional, focused on the citizen as a consumer of services) rather than all-out e-participation/edemocracy viewed as likely a few years ago [47,48]. The current form of e-Government is investment-intensive, but requires relatively little by way of citizen engagement or administrative reform.

If technology is viewed as a means of structuring relationships between governments and citizens, in terms of setting boundaries and accountability, then e-Government can be used as a badge to signal “good governance” to important parties [15]. One example is the use of e-Government by developing countries to showcase themselves as attractive destinations for foreign direct investment, in effect using e-Government maturity as a signal of governance. Although our results actually cast doubt on this line of reasoning inferring good governance from a relatively high level of e-Government maturity currently lacks a sound basis we still encourage governments to promote the adoption of e-Government by educating their citizens to better utilize available services, while the next generation of e-Government applications are developed [3]. If not anything else, familiarity with today’s e-Government applications (mostly focused on service delivery) might <sup>fl</sup>atten the learning curve for future applications potentially targeted at e-participation and electronic democracy.

## 5.1. Limitations

Technological advances have enabled new functionality on e-Government sites since the timeframe of the study, particularly in the area of mobile apps. Citizen awareness and utilization of e-Government services are also higher now than in the period studied. That said, there is no reason to believe that the structural relation between e-Government maturity and the predictors tested here GDP, ICT infrastructure, human capital, and governance have changed systematically since the 2002–2008 timeframe. Norris (2010b) [48] points out that a decade may seem like a long time in the evolution of technology, but is a relatively short time within which to expect changes in administrative practice. Speaking of the technology itself, the world wide web continues to be the general purpose technology [12] from which the tool set of e-Government is derived.

Some researchers have argued that e-Government rankings, such as the e-Government maturity measure used in this paper from West (2003; 2004; 2005; 2006; 2007; 2008) [79–84] may not accurately depict the performance of public administrators in terms of e-Government. Such rankings focus on the visible elements of e-Government (such as number of services delivered online), without exploring the extent to which governments have used technology to transform their internal operations or radically improve business processes [7,8]. These rankings also ignore equally important aspects of e-Government, such as organizational collaboration, adaptation, and a shift from bureaucracy to service orientation [2,13,22]. For example, if some administrations prioritize community links over service delivery, or emphasize local over national government interaction, their efforts may not be picked up by our maturity measure [55].

In the face of such criticism, new maturity models are being developed to incorporate additional dimensions beyond technology deployment, such as organizational integration and citizenship orientation [45,14,46]. As this study has relied on West’s e-Government measure as the dependent variable, it is perhaps most relevant for governments who expect to achieve substantive change in public service delivery by innovating with technology. We see value in extending our research with the newer measures being developed to encompass more aspects of e-Government.

## 5.2. Future research

Although all of our models are linear (in terms of the relation between independent and dependent variables), recent research has identi<sup>fi</sup>ed a nonlinear effect of GDP on e-Government [18]. Poorer countries experienced a bigger marginal contribution from GDP than the more af<sup>fl</sup>uent. Similar nonlinear effects may be postulated and tested for other independent variables as well.

Second, the current level of e-Government in a country might affect its future development in later years. The negative correlation between intercept and slope in the mixed-effect regression model means that countries entering the period of study with highly developed e-Government initiatives had less “headroom” to improve during the study period than countries that were at more rudimentary levels of e-Government at the start of the period. In other words, it is easier to achieve a minimal level of e-Government presence than it is to make progressive improvements. To examine this issue, we plan to include autoregressive parameters (lagged values of y) as predictors in our model to measure this effect.

Third, the lack of signi<sup>fi</sup>cance of governance in our model, alongside its theorized importance, indicates that it may be useful to examine broader measures of societal values, such as culture [44] or social capital, to capture aspects of society that fall outside our narrow de<sup>fi</sup>nition of governance. A similar point can be made about human capital. Its lack of signi<sup>fi</sup>cance suggests the need for a more direct measure of citizens’ education than basic literacy and school enrolment (e.g., computer literacy and ICT skills of citizens). Future studies could examine how e-Government is used by citizens from different educational backgrounds, and how the spread of tertiary (college) education in<sup>fl</sup>uences the supply of and demand for e-Government services.

Finally, this study, like most others on e-Government, has adopted a somewhat insular view in excluding external in<sup>fl</sup>uences on e-Government development. Recent studies such as Lakka et al.

(2013) [42] and Kromidha (2012) [41] argue that focusing solely on endogenous factors is limiting, and recommend examining the role of concepts such as external ICT trade and international e-Government development assistance (for an example, see [15]. In particular, if development assistance can help poorer nations to implement e-Government, donor and recipient nations can work out arrangements (potentially spanning the private and public sectors) that bene<sup>fi</sup>t both sides.

## 6. Conclusion

Existing large-scale empirical research on e-Government is dominated by cross-sectional analyses. This limits the applicability of the <sup>fi</sup>ndings of these studies and our con<sup>fi</sup>dence in them because of concerns over omitted variables, and the neglect of developmental processes. This paper attempts to overcome these methodological challenges by estimating a mixed-effects model on an international panel data set. Although the analysis can be enhanced further (as described in the Further Research section), our current <sup>fi</sup>ndings are generally supportive of the infrastructurefocused point of view: substantial differences in e-Government maturity exist among countries, and the countries that do better at e-Government are the ones that are richer and have built better ICT infrastructure. Human capital and governance, as operationalized here, does not have a signi<sup>fi</sup>cant effect on e-Government maturity. The lack of signi<sup>fi</sup>cant effects for these variables should be probed further with alternative measures of human capital (such as computer literacy and ICT skills of citizens) and governance (such as social capital). Future research might also uncover speci<sup>fi</sup>c technologies that support e-Government most effectively and investigate whether less well-off countries can leverage these technologies (or cheaper alternatives thereof) to leapfrog their more af<sup>fl</sup>uent peers. Finally, it is important to qualify our conclusions with the caveat that alternative measures of e-Government maturity might lead to different results and conclusions.

## References

[1l H. Almutairi. Electronic government return assessment by measuring information system usage, Electron, Gov, Int. I. 7 (1) (2010) 1–21.

[2] K.V. Andersen, H.Z. Henriksen, E-Government maturity models: extension of the layne and lee model, Gov. Inf. Q. 23 (2006) 236–248.

[3] A. Ayanso, D. Chatterjee, D.I. Cho, E-Government readiness index: a methodology and analysis, Gov. Inf. Q. 28 (2011) 522–532.

[4] B. Azad, S. Faraj, J.M. Goh, T. Feghali, What shapes global diffusion of egovernment: comparing the in<sup>fl</sup>uence of national governance institutions, J. Global Inf. Manage. 18 (2010) 85–104.

[5] M.A. Badri, K. Alshare, A path analytic model and measurement of the business value of e-Government: an international perspective, Int. J. Inf. Manage. 28 (2008) 524–535, doi:http://dx.doi.org/10.1016/j.ijinfomgt.2006.10.004.

[6] J.N. Baldwin, R. Gauld, S. Gold<sup>fi</sup>nch, What public servants really think of egovernment, Public Manage. Rev. 14 (2012) 105–127.

[7] F. Bannister, The Curse of the Benchmark: an Assessment of the Validity and Value of e-Government Comparisons, Int Rev, Adm. Sci 73 (2007) 171-188 doi:http://dx doi org/10.1177/0020852307077959

[8] F. Bannister, Deep e-Government, Adv. Manage. Inf. Syst. 17 (2010) 33–51.

[9] F. Bannister, R. Connolly, The great theory hunt: does e-government really have a problem? Gov. Inf. Q. 32 (2015) 1–11.

[10] D.J. Barr, R. Levy, C. Scheepers, H.J. Tily, Random effects structure for con<sup>fi</sup>rmatory hypothesis testing: keep it maximal, J. Memory Lang. 68 (2013) 255–278.

[11] F.S. Berry, W.D. Berry, Innovation and diffusion models in policy research, in: P. Sabatier C M Weible (Eds.) Theories of the Policy Process 3rd ed. Westview Colorado. 2014 pp. 307-362

[12] T.F. Bresnahan, M. Trajtenberg, General purpose technologies ‘Engines of growth’? J. Econom. 65 (1) (1995) 83–108.

[13] M.M. Brown, Understanding e-Government Bene<sup>fi</sup>ts: An Examination of Leading-Edge Local, Am. Rev. Public Adm. 37 (2007) 178–197, doi:http://dx. doi.org/10.1177/0275074006291635.

[14] D.J. Calista, J. Melitski, E-Government and e-Governance: converging constructs of public sector information and communications technologies, Public Adm. Q. (2007) 87–120.

[15] C. Ciborra, Interpreting e-Government and development: ef<sup>fi</sup>ciency, transparency or governance at a distance? Inf. Technol. People 18 (3) (2005) 260–279.

[16] C. Ciborra, D.D. Navarra, Good governance and development aid: risks and challenges of E-Government in Jordan, in: R. Montealegre, M. Korpela, A. Poulymenakou (Eds.), Proceedings of IFIP WG 8.2 WG 9.4, 2003 (Athens, Greece).

[17] J. Cohen, P. Cohen, S.G. West, L.S. Aiken, Applied Multiple Regression/ Correlation Analysis for the Behavioral Sciences, 3rd ed., Erlbaum, Hillsdale, N J, 2003.

[18] F. Cruz-Jesus, T. Oliveira, F. Bacao, Z. Irani, Assessing the pattern between economic and digital development of countries, Information Systems Frontiers (2016), doi:http://dx.doi.org/10.1007/s10796-016-9634-1 (forthcoming).

[19] J.N. Danziger, K.V. Andersen, Impacts of IT on politics and the public sector: methodological, epistemological, and substantive evidence from the golden age of transformation, Int. J. Public Adm. 25 (5) (2002) 591–627.

[20] A. Das, H. Singh, D. Joseph, A longitudinal study of E-Government maturity, PACIS Proc. (2011). http://aisel.aisnet.org/pacis2011/52.

[21] J. Das, C.E. DiRienzo, Is ethnic diversity good for the environment? a cross-Country analysis, The J. Environ. Dev. 19 (2010) 91–113, doi:http://dx.doi.org 10.1177/1070496509355274.

[22] S.S. Dawes, Stewardship and usefulness: policy principles for informationbased transparency, Gov. Inf. Q. 27 (4) (2010) 377–383.

[23] P. Dunleavy, Governance and state organization in the digital era, in: R. Mansell, C. Avgerou, D. Quah (Eds.), The Oxford Handbook of Information and Communication Technologies, Oxford University Press, New York, 2007, pp. 440-423.

[24] X. Fernández-i-Marín, The impact of e-Government promotion in europe: internet dependence and critical mass, Policy Internet 3 (4) (2011) 1–29.

[25] G. Goldkuhl, Innovation in a regulated environment? – legal barriers for e-Government development, Int. J. Public Inf. Syst. 2 (2009) 77–95.

[26] J.A. Hagenaars, N.P. Cobben, Age, cohort and period-General-Model for analysis of social-Change, Netherlands J. Soc. Sci. 14 (1) (1978) 59–91.

[27] Z.Y. Huang, A comprehensive analysis of US counties’ e-Government portals: development status and functionalities, Eur. J. Inf. Syst. 16 (2) (2007) 149–164.

[28] P. I<sup>fi</sup>nedo, Factors in<sup>fl</sup>uencing e-Government maturity in transition economies and developing countries: a longitudinal perspective, ACM SIGMIS Database 42 (4) (2011) 98–116.

[29] International Monetary Fund (IMF), World Economic Outlook (WEO): Recovery, Risk, and Rebalancing, International Monetary Fund (IMF), 2010 (Archive of past World Economic Outlook databases available at http://www. imf.org/external/ns/cs.aspx?id=28, accessed on 22.06.16).

[30] International Telecommunication Union (ITU), Yearbook of Statistics Telecommunication/ICT Indicators 2001–2011, 37th edition, International Telecommunication Union, 2011. (Current data available in World Telecommunication/ICT Indicators Database available at accessed on 22.06.16) http://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx.

[31] P.T. Jaeger, Assessing section 508 compliance on federal e-Government web sites: a multi-Method, user-Centered, evaluation of accessibility for persons with disabilities Gov, Inf, 0. 23 (2006) 169–190.

[32] E.C. Kamarck, J.S. Nye, Governance.com: Democracy in the Information Age, Brookings Institution Press. Washington DC, 2002

[33] G. Karokola, L. Yngstrom, Discussing E-Government maturity models for developing world-Security view, Proceedings of the Information Security South Africa Conference, 6–8 July 2009 81–98 (2009). (Available at: accessed on 28.09.15) http://icsa.cs.up.ac.za/issa/2009/Proceedings ISSA2009Proceedings.pdf#page=101.

[34] I. Katchanovski, T. La Porte, Cyberdemocracy or potemkin e-villages? electronic governments in OECD and post-communist countries, Int. J. Public Adm. 28 (7–8) (2005) 665–681.

[35] D. Kaufmann, A. Kraay, M. Mastruzzi, The Worldwide Governance Indicators: A Summary of Methodology, Data and Analytical Issues, World Bank Polic Research Working Paper No. 5430, 2010 (Available at http://papers.ssrn.com/ sol3/papers.cfm?abstract\_id=1682130, accessed on 22.06.16).

[36] D.Y. Kim, G. Grant, E-Government maturity model using the capability maturity model integration, J. Syst. Inf. Technol. 12 (3) (2010) 230–244

[37] K.L. Kraemer, J.L. King, Computing and public organizations, Public Adm. Rev. 46 (1986) 488–496 (Secial Issue).

[38] K. Kraemer, J.L. King, Information technology and administrative reform: will E-Government Be different? Int. J. Electron. Gov. Res. 2 (1) (2006) 1–20.

[39] S. Krishnan, T.S. Teo, Moderating effects of governance on information infrastructure and e-Government development, J. Am. Soc. Inf. Sci. Technol. 63 (10) (2012) 1929–1946

[40] S. Krishnan, T.S.H. Teo, V.K.G. Lim, Examining the relationships among egovernment maturity, corruption, economic prosperity and environmental degradation: a cross-country analysis, Inf. Manage. 50 (2013) 638–649.

[41] E. Kromidha, Strategic e-Government development and the role of benchmarking, Gov. Inf. Q. 29 (2012) 573–581.

[42] S. Lakka, T. Stamati, C. Michalakelis, D. Martakos, What drives eGovernment growth? An econometric analysis on the impacting factors, Int. J. Electron. Gov. 6 (2013) 20–36.

[43] K. Layne, J.W. Lee, Developing fully functional E-Government: a four stage model, Gov. Inf. Q. 18 (2) (2001) 122–136.

[44] C.P. Lee, K. Chang, F.S. Berry, Testing the development and diffusion of egovernment and e-democracy: a global perspective, Public Adm. Rev. 71 (3) (2011) 444–454.

[45] J. Lee,10 year retrospect on stage models of e-Government: a qualitative metasynthesis, Gov. Inf. Q. 27 (2010) 220–230.

[46] T. Obi, 2015 Waseda University-IAC International e-Government Ranking Survey, Research report of the Waseda University Institute of e-Government, 2015 (http://www.e-gov.waseda.ac.jp/pdf/2015\_Waseda\_IAC\_E-Government\_Press\_Release.pdf, Accessed 03.09.15).

[47] D.F. Norris, e-government . . . not e-governance . . . not e-democracy not now!: not ever? Proceedings of the 4th International Conference on Theory and Practice of Electronic Governance, AMC, 2010, pp. 339–346.

[48] D.F. Norris, E-Government 2020: Plus ça change, plus c'est la meme chose, Public Adm. Rev. 70 (suppl. 1) (2010) s180–s181.

[49] D.C. North, Institutions Institutional Change and Economic Performance, Cambridge University Press, 1990.

[50] E. Rakhmanov, The barriers affecting E-Government development in Uzbekistan, Proceedings of Fourth International Conference on Computer Sciences and Convergence Information Technology (2009) 1474–1480, doi: http://dx.doi.org/10.1109/ICCIT.2009.249.

[51] N.P. Rana, Y.K. Dwivedi, M.D. Williams, A meta-analysis of existing research on citizen adoption of e-Government, Inf. Syst. Frontiers 17 (2013) 547–563.

[52] C.G. Reddick, A two-Stage model of E-Government growth: theories and empirical evidence for U.S. cities, Gov. Inf. Q. 21 (2004) 51–64.

[53] R. Rosenthal, R.L. Rosnow, Beginning behavioral research: a conceptual primer, Pearson (2013) (7th edition).

[54] M. Scott, W. DeLone, W. Golden, Measuring eGovernment Success: a public value approach, Eur. J. Inf. Syst. 25 (2016) 187–208.

[55] P. Shackleton, J. Fisher, L. Dawson, E-Government services, in: H. Linger, J. Fisher, W.G. Wojtkowski, W. Wojtkowski, J. Zupancic, K. Vigo, J. Arnold (Eds.), Constructing the Infrastructure for the Knowledge Economy, Springer, US, 2014, pp. 581–592.

[56] M.A. Shareef, V. Kumar, U. Kumar, Y.K. Dwivedi, E-Government adoption model (GAM): differing service maturity levels, Gov. Inf. Q. 28 (2011) 17–35.

[57] J.D. Singer, J.B. Willett, Applied Longitudinal Data Analysis: Modeling Change and Event Occurrence, Oxford University Press, New York 2003

[58] H. Singh, A. Das, D. Joseph, Country-Level determinants of e-Government maturity, Commun. Assoc. Inf. Syst. 20 (2007) 632–648.

[59] S.C. Srivastava, T.S.H. Teo, What facilitates e-Government development? a cross-Country analysis, Electron. Gov. Int. J. 4 (2007) 365–378.

[60] S.C. Srivastava, T.S. Teo, “The relationship between e-Government and national competitiveness: the moderating in<sup>fl</sup>uence of environmental factors”, Commun. Assoc. Inf. Sys. 23 (1) (2008) 73–94.

[61] S.C. Srivastava, T.S.H. Teo, E-Government, e-Business, and national economic performance, Commun. Assoc. Inf. Sys. 26 (1) (2010) 267–286.

[62] M. Tate, D. Johnstone, J. Toland, R. Hynson, “How the current orthodoxy of local government is failing IT managers: an illustrative case study”, Electron. Gov. Int. L. 4 (4) (2007) 509–526

[63] C.J. Tolbert, K. Mossberger, The effects of e-Government on trust and con<sup>fi</sup>dence in government, Public Adm. Rev. 66 (3) (2006) 354–369.

[64] Transparency International, Transparency International, (2010) (Available at: http://www.transparency.org/cpi2010/results).

[65] United Nations Development Programme (UNDP), Human Development Report 2002: Deepening Democracy in a Fragmented World, United Nations Development Programme (UNDP), 2002 (All reports available at http://hdr. undp.org/en/global-reports, accessed 22.07.16).

[66] United Nations Development Programme (UNDP), Human Development Report 2003: Millennium Development Goals: A Compact Among Nations to End Human Poverty, United Nations Development Programme, 2003.

[67] United Nations Development Programme (UNDP), Human Development Report 2004: Cultural Liberty in Today’s Diverse World, United Nations Development Programme (UNDP), 2004.

[68] United Nations Development Programme (UNDP), Human Development Report 2005: International Cooperation at a Crossroads: Aid, Trade and Security in an Unequal World, United Nations Development Programme (UNDP), 2005.

[69] United Nations Development Programme (UNDP), Human Development Report 2006: Beyond Scarcity: Power, Poverty and the Global Water Crisis, United Nations Development Programme (UNDP), 2006.

[70] United Nations Development Programme (UNDP), Human Development Report 2007/8: Fighting Climate Change: Human Solidarity in a Divided World, United Nations Development Programme (UNDP), 2008.

[71] United Nations Development Programme (UNDP), Human Development Report 2009: Overcoming Barriers: Human Mobility and Development United Nations Development Programme (UNDP), 2009.

[72] United Nations Public Administration Network, Global e-Government Survey 2003: E-Government at the Crossroads, United Nations Public Administration Network, New York: United Nations. 2003

[73] United Nations Public Administration Network, Global e-Government Survey 2004: Towards Access for Opportunity, United Nations Public Administration Network, New York: United Nations, 2004.

[74] United Nations Public Administration Network, Global e-Government Survey 2005: From E-Government to E-Inclusion, United Nations Public Administration Network, New York: United Nations, 2005.

[75] United Nations Public Administration Network, Global e-Government Survey 2008: From E-Government to E-Inclusion, United Nations Public Administration Network New York: United Nations 2008.

[76] United Nations Public Administration Network, Global e-Government Survey 2010: Leveraging E-Government at a Time of Financial and Economic Crisis, United Nations Public Administration Network, New York: United Nations, 2010.

[78] D.M. West, Global E-Government 2002, (2002) (http://www.insidepolitics. org/egovt02int.pdf, Accessed 28.08.15).

[79] D.M. West, Global E-Government 2003, (2003) (http://www.insidepolitics. org/egovt03int.pdf, Accessed 28.08.15).

[80] D.M. West, Global E-Government 2004, (2004) (http://www.insidepolitics org/egovt04int.pdf, Accessed 28.08.15).

[81] D.M. West, Global E-Government 2005, (2005) (http://www.insidepolitics. org/egovt05int.pdf, Accessed 28.08.15).

[82] D.M. West, Global E-Government 2006, (2006) (http://www.insidepolitics. org/egovt06int.pdf, Accessed 28.08.15).

[83] D.M. West, Global E-Government 2007, (2007) (http://www.insidepolitics. org/egovt07int.pdf, Accessed 28.08.15).

[84] D.M. West, Improving Technology Utilization in Electronic Government Around the World, 2008, Brookings Institute, 2008. (Accessed 28.08.15) http:// www.brookings.edu/ /media/research/<sup>fi</sup>les/reports/2008/8/17-

[85] E.J. Wilson, The Information Revolution and Developing Countries, MIT Press, Cambridge, MA, 2004.

[86] J.M. Wooldridge, Econometric Analysis of Cross Section and Panel Data, MIT Press, Cambridge, MA, 2002.

[87] World Economic Forum, Global Information Technology Report 2003–2004: Towards an Equitable Information Society, World Economic Forum, Geneva, 2004.

[88] World Economic Forum, Global Information Technology Report 2004–2005: Ef<sup>fi</sup>ciency in an Increasingly Connected World, World Economic Forum, Geneva, 2005.

[89] World Economic Forum, Global Information Technology Report 2006–2007: Connecting to the Networked Economy, World Economic Forum, Geneva, 2007.

[90] World Economic Forum, Global Information Technology Report 2007–2008: Fostering Innovations Through Networked Readiness, World Economic Forum, Geneva. 2008

[91] World Economic Forum Global Information Technology Report 2008-2009 Mobility in a Networked World, World Economic Forum, Geneva, 2009.

[92] World Economic Forum, Global Information Technology Report 2009–2010: ICT for Sustainability World Economic Forum. Geneva 2010

[93] World Economic Forum, Global Information Technology Report 2010–2011: Transformations 2.0 World Economic Forum. Geneva. 2011

[94] H. Zhao, S. Kim, T. Suh, J. Du, Social institutional explanations of global internet diffusion: a cross-country analysis, J. Global Inf. Manage. 15 (2) (2007) 28–55, doi:http://dx.doi.org/10.4018/jgim.2007040102.

Amit Das (PhD, University of Minnesota) is an associate professor in the College of Business & Economics at Qatar University, where he teaches courses in e-Business, international business, project management, and organization theory.

Harminder Singh (PhD, Michigan State University) is a senior lecturer in the Faculty of Business & Law at the Auckland University of Technology, where he teaches courses in information systems strategy, governance, and business intelligence

Damien Joseph (PhD, Nanyang Technological University) is an associate professor in the Nanyang Business School, where he teaches courses in systems development, data management, and research methods.
