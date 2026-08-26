---
otero_id: 11230
otero_key: "8XHPTG9W"
title: "Giving context to accounting numbers: The role of news coverage"
authors: "Kuo-Tay Chen; Hsin-Min Lu; Tsai-Jyh Chen; Shu-Hsing Li; Jian-Shuen Lian; Hsinchun Chen"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.025"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Giving context to accounting numbers: The role of news coverage

Kuo-Tay Chen <sup>a</sup>, Hsin-Min Lu <sup>b</sup>, Tsai-Jyh Chen <sup>c</sup>, Shu-Hsing Li <sup>a,d,</sup>⁎, Jian-Shuen Lian <sup>a</sup>, Hsinchun Chen <sup>e</sup>

<sup>a</sup> Department of Accounting, National Taiwan University, Taipei, Taiwan

<sup>b</sup> Department of Information Management, National Taiwan University, Taipei, Taiwan

<sup>c</sup> Department of Risk Management and Insurance, National Chengchi University, Taipei, Taiwan

<sup>d</sup> Department of Accounting, Tunghai University, Taichung, Taiwan

<sup>e</sup> Management Information Systems Department, The University of Arizona, Tucson, Arizona, USA

## a r t i c l e i n f o

Available online 20 August 2010

Keywords: Earnings response coef<sup>fi</sup>cient (ERC) Event study News coverage effect Information content of earnings

## a b s t r a c t

Accounting numbers such as earnings per share are an important information source that conveys the value of <sup>fi</sup>rms. Previous studies on the return-earnings relation have con<sup>fi</sup>rmed that stock prices react to the information content in accounting numbers. However, other information sources such as <sup>fi</sup>nancial news may also contain value-relevant information and affect investors' reaction to earnings announcements. We quantify news coverage about S&P 500 companies in the Wall Street Journal (WSJ) before earnings announcements and model its interaction with the return-earnings relation, Our empirical results show that news coverage decreases the information content of unexpected earnings and thus leads to a lower earnings response coef<sup>fi</sup>cient (ERC) for <sup>fi</sup>rms with higher news coverage. Statistically signi<sup>fi</sup>cant interaction between news coverage and unexpected earnings was observed. News coverage does not impact cumulated abnormal returns directly. We further document that this <sup>fi</sup>nding is not driven by <sup>fi</sup>rm size. The results suggest that <sup>fi</sup>nancial news may play an important role in conveying value-related information to the markets.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Accounting numbers are an important means for management to communicate <sup>fi</sup>rm performance to outside investors. Through regularized <sup>fi</sup>nancial statements, investors receive creditable and useful <sup>fi</sup>rm-speci<sup>fi</sup>c information, which helps them better evaluate the true value of <sup>fi</sup>rms. High quality accounting numbers not only reduce the information asymmetry between managers and outside investors, but also facilitate sound investment decisions and the ef<sup>fi</sup>ciency of security markets.

The usefulness of accounting numbers has been an important issue for accounting researchers and general investors. Using the earnings response coef<sup>fi</sup>cient (ERC) to measure the magnitude of the relationship between stock returns and earnings, previous studies have concluded that the ERC is signi<sup>fi</sup>cantly positive [25] and numerical earnings information indeed conveys value-relevant information to the markets. The empirical results suggest that a favorable earnings surprise induces positive abnormal stock returns, while an unfavorable earnings surprise induces negative abnormal stock returns.

Accounting numbers, nonetheless, are not the only source of information conveying the fundamental value of <sup>fi</sup>rms. Other sources, such as <sup>fi</sup>nancial news, trade association publications, and reports issued by analysts and brokerage houses may also contain useful information. These alternative information sources often provide timely updates between earnings announcements and may play an important role in shaping investors' beliefs. The magnitude of the ERC, as a result, may be in<sup>fl</sup>uenced by these information sources.

While highly circulated <sup>fi</sup>nancial news has been shown to impact short-term market returns [32], few studies have investigated how <sup>fi</sup>nancial news impacts the return-earnings relation. Tetlock et al. [33] quanti<sup>fi</sup>ed sentiment in news articles by counting words associated with negative outlooks. Their empirical results showed that the fraction of negative words in <sup>fi</sup>rm-speci<sup>fi</sup>c news stories forecasts low <sup>fi</sup>rm earnings. Previous studies on ERCs have identi<sup>fi</sup>ed four important determinates: earnings persistency, <sup>fi</sup>rm risk, <sup>fi</sup>rm growth, and interest rate [7,13,25]. However, these studies have not examined the interaction between the information content of earnings and news articles.

Given the limitations of previous studies, our research aims at investigating how <sup>fi</sup>nancial news coverage impacts the returnearnings relation. To the best of our knowledge, this is the <sup>fi</sup>rst study that documents how <sup>fi</sup>nancial news coverage affects investors' reactions to accounting earnings. We used the Wall Street Journal (WSJ) as the representative source of <sup>fi</sup>nancial news and collected news articles discussing S&P 500 companies from August 1999 to February 2007. Our collection contains 283,457 news articles and spans more than seven years. This testbed provides a solid ground for statistical inference. Firm-level news coverage computed from our news collection facilitates our investigations on the interaction between <sup>fi</sup>nancial news coverage and return-earnings relation.

The remainder of the paper is organized as follows. Section 2 provides a review of related literature followed by the discussion of the research objectives and hypotheses in Section 3. In Section 4, we describe our data sources and empirical models. The main <sup>fi</sup>ndings of the study are presented in Section 5. Section 6 discusses the managerial implications of our results. We conclude with a summary and future research directions in Section 7.

## 2. Literature review

The seminal works of Ball and Brown [2] and Beaver [5] spawned the study of the information content of accounting numbers. Researchers study a wide range of topics via the return-earnings relation and the event study framework [14,25]. In this section we <sup>fi</sup>rst summarize the earnings response coef<sup>fi</sup>cient research and then focus on two major aspects that are directly relevant to this study: lagged performance information in accounting earnings and asymmetry in the return-earnings relation.

## 2.1. Earnings response coefficient

The information content of accounting numbers can be measured by the extent to which security prices change in response to the announcement of <sup>fi</sup>nancial statements. One of the most commonly used measures is the Earnings Response Coef<sup>fi</sup>cient, ERC. Speci<sup>fi</sup>cally, an ERC is estimated using the following model:

$$
C A R _ {\mathrm{it}} = a + b U E _ {\mathrm{it}} + e _ {\mathrm{it}}
$$

where $\mathsf { e } _ { \mathrm { i t } }$ is white noise and $\mathrm { C A R } _ { \mathrm { i t } }$ (Cumulated Abnormal Return; CAR) is the measure of risk-adjusted return for security i cumulated over an event window around the earnings announcement at time t. The ERC literature often adopts Fama and French three-factor model [15], which incorporates excess market returns (market returns minus risk-free interest rates), small minus large <sup>fi</sup>rm returns (SML), and high minus low book-to-market <sup>fi</sup>rm returns (HML) as main risk factors. Expected returns can be computed after the loadings of risk factors are estimated using historical data. Abnormal returns are the difference between actual stock returns and their expected returns computed with the three-factor model. It is a common practice to accumulate the abnormal returns over a period of time to capture the market reaction to earnings events.

$\mathrm { U E } _ { \mathrm { i t } }$ is the unexpected earnings divided by security price at time t. Unexpected earnings capture the earnings variation that has not yet been incorporated into the investors' belief. There are two approaches commonly used to compute unexpected earnings. The <sup>fi</sup>rst approach estimates expected earnings based on a time series model. The second approach uses analysts' forecasts as a proxy for market expectation. Empirical evidence suggests that analysts' forecasts are a better proxy for market expectation of earnings [27].

The estimated value of coef<sup>fi</sup>cient b is the ERC. While there is consensus that the ERC is signi<sup>fi</sup>cantly positive [25], the magnitude of the ERC may vary across <sup>fi</sup>rms. Collins and Kothari [7] suggested that the information environment, which can be broadly de<sup>fi</sup>ned to include all sources of information relevant to <sup>fi</sup>rm value assessment, is an important determinant of ERCs. Their study, nonetheless, did not directly measure the information environment but instead looked at other determinants such as earnings persistency, <sup>fi</sup>rm risk, <sup>fi</sup>rm growth, and interest rates. Other studies that looked at the economic determinants of ERCs have identi<sup>fi</sup>ed various characteristics that affect ERCs. Notable determinants include: <sup>fi</sup>rm size [8,13], capital structure [11], earnings persistence [24], earnings quality [10,16], and similarity of investor expectations [1].

## 2.2. Lagged performance information in accounting earnings

Accounting earnings measurement emphasizes transaction-based revenue recognition. As a result, a large portion of the information embedded in earnings is historical in nature. Security prices, on the other hand, re<sup>fl</sup>ect both current earnings as well as future earnings information that are available to the market [26]. As a result, valuerelevant information in accounting earnings may have been incorporated into stock prices before earnings announcements are issued. Only a small portion of the earnings information content can be captured by measuring the stock price reaction around earnings events. The “price lead earnings” viewpoint [6] provides a compelling explanation of why estimated earnings response coef<sup>fi</sup>cients are small in comparison to theoretical predictions [25].

The “price lead earnings” viewpoint has been veri<sup>fi</sup>ed by empirical studies that expand the return-earnings measurement window [12], include leading period return [22,26], and include future earnings and future returns [9]. However, most of these studies failed to explore other information sources that may have contained future earnings information. Financial news is one such information source [29,30]. Before being of<sup>fi</sup>cially announced, information related to a <sup>fi</sup>rm's earnings is sometimes disclosed through various news reports. Investors could incorporate the information into their determination of reasonable security prices. The return-earnings relation can be better modeled if relevant information from <sup>fi</sup>nancial news could be captured.

## 2.3. Asymmetry in the return-earnings relation

Previous studies have documented that security markets react to positive and negative earnings surprises differently. Positive earnings surprises were found to be associated with larger price responses [20,28]. One possible reason is that widely adopted accounting conservatism recognizes probable losses as they are discovered but defers revenue until it is veri<sup>fi</sup>ed [19]. This practice increases the speed that accounting numbers re<sup>fl</sup>ect economic losses compared to economic gains. Timely recognition of economic losses leads to lower autocorrelations of negative shocks in earnings time series. The consequence is that accounting losses during the current period are less likely to signal future losses while accounting gains are more likely to signal future gains. This time series property is often referred to as the lower persistency of accounting losses relative to accounting gains [4]. Lower persistency is known to decrease ERCs [24].

Studies on <sup>fi</sup>rm disclosure activities point out that <sup>fi</sup>rm management is motivated to disclose bad news earlier in fear of litigation risk [18]. This explanation suggests that information about a forthcoming negative earnings surprise may have been released earlier, which leads to lower ERC when the bad earnings are of<sup>fi</sup>cially announced. The asymmetry in the return-earnings relation should be controlled in the empirical study so that valid results could be obtained.

## 3. Hypotheses development

In this study, we aim to investigate the role of <sup>fi</sup>nancial news coverage in determining the ERC. Financial news contains timely updates on <sup>fi</sup>rm value. The “price lead earnings” viewpoint suggests that investors would have incorporated the information from <sup>fi</sup>nancial news into stock prices before the earnings announcements. The information content of earnings announcements, as a result, is reduced by news coverage. In other words, we expect a negative relationship between news coverage and ERCs:

H1. Firms with higher news coverage before their earnings announcements are associated with lower ERCs.

Fig. 1 schematically shows the hypothesized relationships in the research model. Measured by the ERC, the thick horizontal arrow indicates the relationship between unexpected earnings and cumulated abnormal returns. Hypothesis H1 asserts that news coverage moderates this relationship; higher news coverage reduces the ERC.

![](/api/attachments/8XHPTG9W/fulltext/images/a5d9c04e59b4cc117c139896e7bd5ee660a539b00ab2dc36079db82c834f44ca.jpg)  
Fig. 1. Research model. Control variables: return momentum, size, book-to-market ratio, and share turnover.

## 4. Research methodology

## 4.1. Research testbed

We used articles from the WSJ to develop our research testbed. News articles from August 1999 through February 2007 were collected from the ProQuest database. We retrieved 283,457 news articles in total for the 91-month period and developed a system for automatic analysis of <sup>fi</sup>rm news coverage. We focused on S&P 500 companies because <sup>fi</sup>nancial news tends to cover large <sup>fi</sup>rms. The monthly S&P 500 companies list was obtained from the Center for Research on Security Prices (CRSP) database.

Daily stock prices were obtained from CRSP and analysts' forecasts were retrieved from the Institutional Brokers' Estimate System (IBES). While accounting numbers are publicly available from the EDGAR system [17], the data are not in a consistent format across <sup>fi</sup>rms or time period. We instead downloaded accounting numbers from the Compustat North American Annual and Quarterly database, which contained the same numerical data but in a structured format.

## 4.2. Firm-based news coverage analysis

We conducted <sup>fi</sup>rm-based news coverage analysis by creating a system that automatically extracts and standardizes <sup>fi</sup>rm names. We de<sup>fi</sup>ned that a <sup>fi</sup>rm received news coverage in a news article if the <sup>fi</sup>rm's name was mentioned at least once in the article. One news article may be associated with zero, one, or more <sup>fi</sup>rms. Our procedure implicitly assumes that all <sup>fi</sup>rms mentioned in a news article are equally important.

Fig. 2 presents the system design for <sup>fi</sup>rm-based news coverage analysis. Our system performs named entity recognition and standardizes the recognized company names by consulting the “stocknames” table in the CRSP monthly stock price dataset (SM). Standardized <sup>fi</sup>rm IDs (PERMCO) are then attached to matched entities.

The design of our <sup>fi</sup>rm name matching process follows a tight-toloose approach. Each recognized named entity goes through a threestage matching process. The <sup>fi</sup>rst stage matches the full named entity string against the <sup>fi</sup>rm names in the stocknames table. Since the company names in the stocknames table do not contain punctuation, all punctuation marks in the original named entity string are replaced with white spaces. Extra white spaces (two or more consecutive white spaces) are removed. The process stops if the named entity string matches with an entry in the stocknames table.

In the second stage, the named entity string is gradually truncated when matching against <sup>fi</sup>rm names in the stocknames table. Each time the last word in the named entity string is removed if the previous string does not match with any entries. A match is obtained if the truncated named entity string is identical to the beginning part of a <sup>fi</sup>rm name in the stocknames table. The process stops if the truncated named entity string matches with an entry or the truncated string contains fewer than 2 words.

The third stage handles possible complications that involve acronyms. If part of a company name is an acronym, the company names in stocknames table often contain additional white spaces (e.g., “U S AIRWAY GROUP INC”). We address this issue by detecting acronyms in the recognized named entity and inserting additional white space between characters of an acronym before the matching process.

To investigate the interaction between news coverage and returnearnings relation, the news frequency before earnings announcements was computed. We computed news frequency for each earnings announcement event using a [−20, −1] trading day window relative to the earnings announcement date. This twentytrading day window, which is roughly equal to one month, allows most <sup>fi</sup>rms to have news coverage before earnings announcements and facilitates the subsequent statistical inference. Using trading day instead of calendar day can mitigate coverage variations caused by trading holidays.

## 4.3. Empirical model specification

The basic abnormal return/unexpected earnings speci<sup>fi</sup>cation was used as a baseline model to evaluate all subsequent modi<sup>fi</sup>cations [8]. The regression model takes the following form:

$$
\begin{array}{r l} C A R _ {\mathrm{it}, [ 0, z ]} = & a + b _ {1} U E _ {\mathrm{it}} + b _ {2} D u e _ {\mathrm{it}} U E _ {\mathrm{it}} + g _ {1} F F a l p h a _ {\mathrm{it}} + g _ {2} \log (S i z e _ {\mathrm{it}}) \\ & + g _ {3} \log (B M _ {\mathrm{it}}) + g _ {4} \log (S T u r n o v e r _ {\mathrm{it}}) + h _ {1} F F a l p h a _ {\mathrm{it}} U E _ {\mathrm{it}} \\ & + h _ {2} \log (S i z e _ {\mathrm{it}}) U E _ {\mathrm{it}} + h _ {3} \log (B M _ {\mathrm{it}}) U E _ {\mathrm{it}} \\ & + h _ {4} \log (S T u r n o v e r _ {\mathrm{it}}) U E _ {\mathrm{it}} + e _ {\mathrm{it}} \end{array} \tag {1}\tag{1}
$$

where $\mathrm { D u e } _ { \mathrm { i t } }$ is 1 if $\mathrm { U E } _ { \mathrm { i t } }$ is positive and 0 if $\mathrm { U E } _ { \mathrm { i t } }$ is negative. $\mathsf { C A R } _ { \mathrm { i t , \left[ 0 , 2 \right] } }$ is the cumulated abnormal return of <sup>fi</sup>rm i over the trading day window [0, 2] relative to an earnings announcement day t. The three-trading day window captures the immediate response of earnings announcements [28]. While a longer event window may increase the magnitude of ERC, the effects of other events during a longer window may interfere with the change of stock prices and bias the results [25].

We adopted the Fama–French three-factor model to control for common risk factors [15]. The values of the three risk factors (excess market return, SML and HML) were downloaded from Dr. Kenny French's website (http://mba.tuck.dartmouth.edu/pages/faculty/ken. french/index.html). For each earnings event, the regression coef<sup>fi</sup>- cients estimated over the trading day window $[ - 2 5 2 , - 2 1 ]$ relative to an earnings announcement day were used to compute abnormal returns during the [0, 2] window. The sum of the abnormal returns during the [0, 2] event window is our dependent variable. Excluding 20 trading days before earnings announcements avoided the confounding of the estimated coef<sup>fi</sup>cient with earnings announcements. The last term $\mathsf { e } _ { \mathrm { i t } }$ is white noise.

![](/api/attachments/8XHPTG9W/fulltext/images/b05c3c87a479fc63975754d0e4a23d191d9d0aa322df471b6021856aa7ea98f4.jpg)  
Fig. 2. System design for <sup>fi</sup>rm-based news coverage analysis.

The covariate $\mathrm { U E } _ { \mathrm { i t } }$ is the unexpected earnings computed based on the difference between the realized earnings and analysts' forecasts, divided by the stock price of <sup>fi</sup>rm i at day t. Both the realized earnings per share (EPS) and analysts' forecast were obtained from the IBES database. We retrieved the analyst's most recent monthly mean forecast before earnings announcements. $\mathrm { F F a l p h a _ { i t } }$ is the estimated intercept in the Fama–French three-factor model used to compute abnormal returns. This variable is used to control the return momentum effect [23]. Other independent variables, including $\log ( \mathrm { S i z e _ { i t } ) , \log ( B M _ { i t } ) }$ and $\mathrm { l o g ( S T u r n o v e r _ { i t } ) }$ , are control variables for <sup>fi</sup>rms' market value at time t, book-to-market ratio at time t, and share turnover rate during the reporting quarter associated with time t. Firm size $( \log ( \mathrm { { S i z e } _ { \mathrm { { i t } } } ) } )$ has been shown to in<sup>fl</sup>uence the ERC [28]. Book-to-market ratio $\left( \mathrm { l o g ( B M _ { i t } ) } \right)$ is related to future growth of a <sup>fi</sup>rm. A lower book-to-market ratio signals higher growth and vice-versa [31]. Previous studies reported that growth <sup>fi</sup>rms tend to have higher ERCs [28]. All interaction terms between control variables and $\mathrm { U E } _ { \mathrm { i t } }$ are included to capture the potential moderating effect of control variables.

Note that by rearranging Eq. (1), it implies that the ERC of <sup>fi</sup>rm i at time t is $\mathsf { b } _ { 1 } + \mathsf { b } _ { 2 } \mathsf { D u e } _ { \mathrm { i t } } + \mathsf { h } _ { 1 }$ FFalpha +h log $\mathrm { ( S i z e _ { i t } ) + h _ { 3 } l o g ( B M _ { i t } ) + }$ $\mathrm { h } _ { 4 } \mathrm { l o g ( S T u r n o v e r _ { i t } ) }$ . That is, the ERC is a function of the sign of unexpected earnings as well as other control variables. Coef<sup>fi</sup>cient b is the ERC of a <sup>fi</sup>rm with zero FFalpha , log $\mathrm { ( { } S i z e _ { i t } ) }$ , log $\mathrm { [ B M _ { i t } ) }$ , and log $( { \mathrm { S T u r n o v e r } } _ { \mathrm { i t } } )$ when unexpected earnings are negative. Coef<sup>fi</sup>cient $\mathsf { b } _ { 2 }$ captures the difference in the ERC between positive and negative earnings surprises. Coef<sup>fi</sup>cient $\mathrm { h } _ { \mathrm { j } } ~ ( \mathrm { j } = 1 , 2 , 3 , 4 )$ captures the effect of control variables on the ERC. For example, h can be interpreted as the change of the ERC when $\mathrm { F F a l p h a _ { i t } }$ increases by one.

Hypothesis H1 predicts that <sup>fi</sup>rms with higher news coverage before earnings announcements are associated with a lower ERC. This hypothesis can be tested by including two terms that capture news coverage and the interaction between news coverage and an earnings surprise:

$$
\begin{array}{r l} C A R _ {\mathrm{it}, [ 0, 2 ]} = & a + b _ {1} U E _ {\mathrm{it}} + b _ {2} D u e _ {\mathrm{it}} U E _ {\mathrm{it}} + c _ {1} N e w s F r e q u e n c y _ {\mathrm{it}} \\ & + c _ {2} N e w s F r e q u e n c y _ {\mathrm{it}} U E _ {\mathrm{it}} + g _ {1} F F a l p h a _ {\mathrm{it}} + g _ {2} \log (S i z e _ {\mathrm{it}}) \\ & + g _ {3} \log (B M _ {\mathrm{it}}) + g _ {4} \log (S T u r n o v e r _ {\mathrm{it}}) + h _ {1} F F a l p h a _ {\mathrm{it}} U E _ {\mathrm{it}} \\ & + H _ {2} \log (S i z e _ {\mathrm{it}}) U E _ {\mathrm{it}} + h _ {3} \log (B M _ {\mathrm{it}}) U E _ {\mathrm{it}} \\ & + h _ {4} \log (S T u r n o v e r _ {\mathrm{it}}) U E _ {\mathrm{it}} + e _ {\mathrm{it}} \end{array} \tag {2}
$$

where NewsFrequency is the number of news articles that have mentioned <sup>fi</sup>rm i during the trading day window $[ - 2 0 , - 1 ]$ relative to the earnings announcement date t. We computed NewsFrequency via the output of our <sup>fi</sup>rm-based news coverage analysis system. While our goal is to test the interaction between news coverage and unexpected earnings, NewsFrequency is also included following the framework for testing moderator effects [3].

By adding news coverage into the empirical model, the ERC of <sup>fi</sup>rm i at time t becomes $\mathsf { b } _ { 1 } + \mathsf { b } _ { 2 } \mathsf { D u e } _ { \mathrm { i t } } + \mathsf { c } _ { 2 }$ NewsFrequenc $\mathrm { { y } _ { \mathrm { { i t } } } + \mathrm { { h } _ { 1 } \mathrm { { F F a l p h a } _ { \mathrm { { i t } } } + } } }$ h log(Size )+h log(BM )+h log(STurnover ). The magnitude of ${ \sf C } _ { 2 }$ can be interpreted as the change in the ERC if <sup>fi</sup>rm i is covered in one additional news article during the 20 trading-day pre-announcement window. Hypothesis H1 predicts that ${ \sf C } _ { 2 }$ is negative.

## 5. Empirical results

We estimated Eqs. (1) and $( 2 )$ via ordinary least square regression. The upper and lower 1% of $U E _ { i t }$ and $\mathsf { C A R } _ { \mathrm { i t , \left[ 0 , 2 \right] } }$ were winsorized (i.e., extreme values were replaced with the 1% or 99% percentile values) to guard against outliers. The upper 1% of NewsFrequen ${ \mathrm { C y } } _ { \mathrm { i t } }$ was also winsorized. Winsorizing selected variables prevents the potential negative effects of extreme values when conducting regression analysis. Our main results would remain qualitatively the same if unwinsorized data were used. The <sup>fi</sup>nal sample consists of 11,201 <sup>fi</sup>rm-quarter observations. Descriptive statistics of variables for Eqs. (1) and (2) are summarized in Table 1. The average cumulated abnormal return $\left( \mathrm { C A R } _ { \mathrm { i t , \left[ 0 , 2 \right] } } \right)$ during the [0, 2] trading day window relative to earnings announcements is 0.00370 but is not signi<sup>fi</sup>cantly different from zero. The average of unexpected earnings is quite small (0.00046) with a relative large dispersion (std. $\mathsf { d e v . } { = } 0 . 0 0 2 7 5 )$ even after winsorization. The mean of NewsFrequency indicates that on average each S&P 500 company is mentioned in 5.971 news articles during the 20 trading days before earnings announcements. Market value $\mathrm { ( S i z e _ { i t } ) }$ , book-to-market ratio $\left( \mathrm { B M } _ { \mathrm { i t } } \right)$ and share turnover (STurnover ) were transformed using the logarithm function to correct their skewed distributions.

In our sample, 33% of <sup>fi</sup>rm-quarters did not have news coverage. The estimation results may therefore be driven by <sup>fi</sup>rm-quarters with and without news coverage instead of by the level of news coverage. To guard against this potential problem, we also report the estimation results using a subsample that contains <sup>fi</sup>rm-quarters with news coverage during the 20-trading-day window before earnings announcement. There were 7539 <sup>fi</sup>rm-quarters in this subsample.

Table 2 presents the summary statistics in the subsample with news coverage. The average o $\mathrm { C A R } _ { \mathrm { i t , [ 0 , 2 ] } }$ and $\mathrm { U E } _ { \mathrm { i t } }$ is lower compared to the whole sample. The difference, nonetheless, is small compared to their standard deviations. The means and standard deviations of control variables are similar to those in the full sample. It is not surprising to see that the mean of NewsFrequency increases from 5.917 to 8.790.

## 5.1. Baseline models

Table 3 reports the estimation results of the baseline model (Eq. (1)). The <sup>fi</sup>rst two columns of Table 3 list a simpli<sup>fi</sup>ed version of Eq. (1) that excludes the interaction terms between unexpected earnings and control variables. The result shows that the ERC is 4.51 and is signi<sup>fi</sup>cantly positive. The result is consistent with previous studies on ERCs [8,26]. The estimated coef<sup>fi</sup>cient of $\mathrm { U E } _ { \mathrm { i t } }$ is smaller using the with-news sample. Before moving to the results of the more complicated model, we note that this pattern is consistent with our intuition that <sup>fi</sup>rms with news coverage have smaller ERCs. Two control variables, FFalpha and log $\mathrm { ( S i z e _ { i t } ) }$ , are signi<sup>fi</sup>cant, indicating a systematic variation of cumulated abnormal returns with respect to momentum and <sup>fi</sup>rm size.

Table 1  
Descriptive statistics of all <sup>fi</sup>rm-quarters.

<table><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Median</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td> $\text{CAR}_{\text{it},[0,2]}$ </td><td>11,201</td><td>0.00370</td><td>0.00315</td><td>0.05890</td><td>-0.17951</td><td>0.17239</td></tr><tr><td> $\text{UE}_{\text{it}}$ </td><td>11,201</td><td>0.00046</td><td>0.00033</td><td>0.00275</td><td>-0.01360</td><td>0.01057</td></tr><tr><td> $\text{NewsFrequency}_{\text{it}}$ </td><td>11,201</td><td>5.917</td><td>1.000</td><td>14.026</td><td>0.000</td><td>93.000</td></tr><tr><td> $\text{FFalpha}_{\text{it}}$ </td><td>11,201</td><td>0.00028</td><td>0.00023</td><td>0.00134</td><td>-0.00767</td><td>0.01200</td></tr><tr><td> $\log(\text{Size}_{\text{it}})$ </td><td>11,201</td><td>23.053</td><td>22.963</td><td>1.186</td><td>16.633</td><td>27.128</td></tr><tr><td> $\log(\text{BM}_{\text{it}})$ </td><td>11,201</td><td>-1.118</td><td>-1.049</td><td>0.760</td><td>-8.047</td><td>2.066</td></tr><tr><td> $\log(\text{STurnover}_{\text{it}})$ </td><td>11,201</td><td>-0.986</td><td>-1.073</td><td>0.638</td><td>-2.986</td><td>2.369</td></tr></table>

Table 3  
Table 2  
Descriptive statistics of <sup>fi</sup>rm-quarters with news coverage.

<table><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Median</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td> $CAR_{it,[0,2]}$ </td><td>7539</td><td>0.00270</td><td>0.00235</td><td>0.05892</td><td>-0.17951</td><td>0.17239</td></tr><tr><td> $UE_{it}$ </td><td>7539</td><td>0.00044</td><td>0.00032</td><td>0.00290</td><td>-0.01360</td><td>0.01057</td></tr><tr><td> $NewsFrequency_{it}$ </td><td>7539</td><td>8.790</td><td>3.000</td><td>16.341</td><td>1.000</td><td>93.000</td></tr><tr><td> $FFalpha_{it}$ </td><td>7539</td><td>0.00027</td><td>0.00023</td><td>0.00135</td><td>-0.00767</td><td>0.01200</td></tr><tr><td> $log(Size_{it})$ </td><td>7539</td><td>23.311</td><td>23.211</td><td>1.219</td><td>16.633</td><td>27.128</td></tr><tr><td> $log(BM_{it})$ </td><td>7539</td><td>-1.128</td><td>-1.054</td><td>0.777</td><td>-8.047</td><td>1.474</td></tr><tr><td> $log(STurnover_{it})$ </td><td>7539</td><td>-1.003</td><td>-1.095</td><td>0.635</td><td>-2.986</td><td>1.597</td></tr></table>

The last two columns of Table 3 report the estimation results using all covariates in Eq. (1). Consistent with previous studies on asymmetry in the return-earnings relation [20,28], the coef<sup>fi</sup>cient of $\mathsf { D u e } _ { \mathrm { i t } } \mathrm { U E } _ { \mathrm { i t } }$ is signi<sup>fi</sup>cantly positive, which indicates that positive unexpected earnings are associated with larger ERCs compared to negative unexpected earnings. The estimated coef<sup>fi</sup>cient of $\mathrm { l o g ( B M _ { i t } ) }$ $\mathrm { U E } _ { \mathrm { i t } }$ is signi<sup>fi</sup>cantly negative ( 2.26). As discussed before, a lower book-to-market ratio signals higher growth and vice-versa [31]. The signi<sup>fi</sup>cant coef<sup>fi</sup>cient is consistent with previous studies that document higher ERCs for growth <sup>fi</sup>rms [28]. Firm size has also been identi<sup>fi</sup>ed to be a determinant of ERCs. The estimated coef<sup>fi</sup>cient of $\mathsf { l o g } ( \mathsf { S i z e } _ { \mathrm { i t } } ) \mathsf { U E } _ { \mathrm { i t } } ,$ nonetheless, is not signi<sup>fi</sup>cant, while the sign of the coef<sup>fi</sup>cient is consistent with previous studies [28]. The estimated coef<sup>fi</sup>cient of $\mathsf { l o g ( S T u r n o v e r _ { i t } ) U E _ { i t } }$ is signi<sup>fi</sup>cant using the full sample but shows insigni<sup>fi</sup>cant results when the subsample was used. $\mathrm { F F a l p h a _ { i t } U E _ { i t } }$ is not signi<sup>fi</sup>cant in our baseline model.

## 5.2. The effect of news coverage

Table 4 reports the estimation results of Eq. (2). As listed in the last two columns, our main concern is the interaction between news coverage and unexpected earnings $\left( \mathrm { N e w s F r e q u e n c y _ { i t } U E _ { i t } } \right)$ . The estimated coef<sup>fi</sup>cient of NewsFrequen $\mathsf { J } _ { \mathrm { i t } } \mathrm { U E } _ { \mathrm { i t } }$ is signi<sup>fi</sup>cantly negative. The estimation result suggests that, other things being equal, the ERC decreases −0.064 if a <sup>fi</sup>rm appears in one additional news article. A lower ERC indicates smaller market reactions given the same unexpected earnings and other <sup>fi</sup>rm characteristics. Our empirical result supports hypothesis H1, which predicts a negative coef<sup>fi</sup>cient for NewsFrequenc $\mathrm { \Delta y _ { i t } U E _ { i t } . }$ It is interesting to note that the estimated coef<sup>fi</sup>cient for news coverage (NewsFrequency ) is not signi<sup>fi</sup>cant. It means that NewsFrequency does not in<sup>fl</sup>uence CAR directly; the in<sup>fl</sup>uence is through moderating the return-earnings relation.

Regression results of the baseline model.

<table><tr><td rowspan="2"></td><td colspan="2">Baseline: Eq. (1)(omit interaction)</td><td colspan="2">Baseline: Eq. (1)(full model)</td></tr><tr><td>Full sample</td><td>With news</td><td>Full sample</td><td>With news</td></tr><tr><td>Intercept</td><td>0.052***</td><td>0.043***</td><td>0.042***</td><td>0.035**</td></tr><tr><td> $UE_{it}$ </td><td>4.51***</td><td>4.18***</td><td>8.76**</td><td>7.50</td></tr><tr><td> $Due_{it}UE_{it}$ </td><td></td><td></td><td>1.046***</td><td>1.054***</td></tr><tr><td> $FFalpha_{it}$ </td><td>-3.48***</td><td>-4.04***</td><td>-3.32***</td><td>-3.89***</td></tr><tr><td> $log(Size_{it})$ </td><td>-0.0022***</td><td>-0.0018***</td><td>-0.0019***</td><td>-0.0016***</td></tr><tr><td> $log(BM_{it})$ </td><td>-0.00061</td><td>0.000073</td><td>-0.00056</td><td>-0.00012</td></tr><tr><td> $log(STurnover_{\downarrow it})$ </td><td>-0.00076</td><td>-0.0014</td><td>-0.0012</td><td>-0.0023**</td></tr><tr><td> $FFalpha_{it}UE_{it}$ </td><td></td><td></td><td>23.55</td><td>142.60</td></tr><tr><td> $log(Size_{it})UE_{it}$ </td><td></td><td></td><td>-0.30</td><td>-0.23</td></tr><tr><td> $log(BM_{it})UE_{it}$ </td><td></td><td></td><td>-2.26***</td><td>-1.87***</td></tr><tr><td> $log(STurnover_{\downarrow it})UE_{it}$ </td><td></td><td></td><td>-0.84***</td><td>-0.35</td></tr><tr><td>Adj. R-square</td><td>0.049</td><td>0.049</td><td>0.057</td><td>0.056</td></tr></table>

<sup>⁎⁎⁎,</sup> <sup>⁎⁎,</sup> <sup>⁎</sup> indicate statistical signi<sup>fi</sup>cance at the 0.01 0.05 and 0.1 levels respectively.

Table 4  
The effect of news coverage on ERC.

<table><tr><td rowspan="2"></td><td colspan="2">News coverage: Eq. (2)(omit interaction)</td><td colspan="2">News coverage: Eq. (2)(full model)</td></tr><tr><td>Full sample</td><td>With news</td><td>Full sample</td><td>With news</td></tr><tr><td>Intercept</td><td>0.043***</td><td>0.038**</td><td>0.049***</td><td>0.043***</td></tr><tr><td> $UE_{it}$ </td><td>8.82**</td><td>7.69</td><td>-3.40</td><td>-6.87</td></tr><tr><td> $Due_{it}UE_{it}$ </td><td>1.040***</td><td>1.040***</td><td>1.11***</td><td>1.12***</td></tr><tr><td> $NewsFrequency_{it}$ </td><td>0.0000081</td><td>0.000019</td><td>0.000062</td><td>0.000070</td></tr><tr><td> $NewsFrequency_{it}UE_{it}$ </td><td></td><td></td><td>-0.064***</td><td>-0.065***</td></tr><tr><td> $FFalpha_{it}$ </td><td>-3.31***</td><td>-3.88***</td><td>-3.27***</td><td>-3.84***</td></tr><tr><td> $log(Size_{it})$ </td><td>-0.0019***</td><td>-0.0017**</td><td>-0.0022***</td><td>-0.0020***</td></tr><tr><td> $log(BM_{it})$ </td><td>-0.00057</td><td>-0.00016</td><td>-0.00078</td><td>-0.00034</td></tr><tr><td> $log(STurnover_{it})$ </td><td>-0.0012</td><td>-0.0023**</td><td>-0.0015</td><td>-0.0026**</td></tr><tr><td> $FFalpha_{it}UE_{it}$ </td><td>23.48</td><td>142.40</td><td>-32.16</td><td>85.16</td></tr><tr><td> $log(Size_{it})UE_{it}$ </td><td>-0.30</td><td>-0.24</td><td>0.29</td><td>0.46*</td></tr><tr><td> $log(BM_{it})UE_{it}$ </td><td>-2.26***</td><td>-1.87***</td><td>-1.97***</td><td>-1.56***</td></tr><tr><td> $log(STurnover_{it})UE_{it}$ </td><td>-0.84***</td><td>-0.35</td><td>-0.53*</td><td>0.054</td></tr><tr><td>Adj. R-square</td><td>0.056</td><td>0.055</td><td>0.059</td><td>0.058</td></tr></table>

$^ { * * * } , ^ { * * * } , ^ { * }$ indicate statistical signi<sup>fi</sup>cance at the 0.01 0.05 and 0.1 levels respectively.

Given the empirical support for the interaction between news coverage and unexpected earnings, it is important to know whether the signi<sup>fi</sup>cant result is driven by <sup>fi</sup>rm size. As reported in the <sup>fi</sup>rst two columns of Table 4, the estimated coef<sup>fi</sup>cient of $\log ( \mathrm { S i z e _ { i t } ) U E _ { i t } }$ is negative when the interaction between news coverage and unexpected earnings $\left( \mathrm { N e w s F r e q u e n c y _ { i t } U E _ { i t } } \right)$ is excluded. The estimated coef<sup>fi</sup>cient of $\log ( \mathrm { S i z e _ { i t } ) U E _ { i t } }$ becomes positive when NewsFrequency UE is included in the empirical model. Moreover, NewsFrequency UE is signi<sup>fi</sup>cant at a 99% con<sup>fi</sup>dence level across both samples while log $\mathrm { ' { S i z e } _ { i t } ) U E _ { i t } }$ is only signi<sup>fi</sup>cant at a 90% con<sup>fi</sup>dence level in the “with news” subsample. The results suggest that the interaction between news coverage and unexpected earnings is not a size effect despite relatively high correlation between the size of a <sup>fi</sup>rm and its news coverage (correlation coef<sup>fi</sup>cient=0.468; p-value b0.01). Previous studies have documented lower ERCs for larger <sup>fi</sup>rms [8,13], but the lower ERCs may have been affected or caused by news coverage that was omitted in the empirical models.

## 6. Discussion

Our empirical results have several important implications for managers and investors. First, if managers prefer higher CARs around earnings events, then only when the unexpected earnings are negative should managers release information regarding forthcoming earnings during the pre-announcement period. The reason can be explained by taking expectation to Eq. (2) and differentiating with respect to NewsFrequency :

$$
\frac {\partial \mathrm{E} \left(C A R _ {\mathrm{it} , [ 0 , 2 ]}\right)}{\partial N e w s F r e q u e n c y _ {\mathrm{it}}} = c _ {1} + c _ {1} U E _ {\mathrm{it}} \equiv N N _ {\mathrm{it}}
$$

where $\mathsf { N N } _ { \mathrm { i t } }$ is the expected change of $\mathsf { C A R } _ { \mathrm { i t , [ 0 , 2 ] } }$ given one additional news coverage. From Table 4 the estimated values for ${ \sf C } _ { 1 }$ and ${ \sf C } _ { 2 }$ are 0.000062 and −0.064. Since ${ \mathsf { c } } _ { 1 } \mathrm { i } s$ not signi<sup>fi</sup>cantly different from zero, it is omitted in this analysis (i.e., setting $\mathsf C _ { 1 } = 0 )$ . Substituting the estimated value of $\boldsymbol { \mathsf { c } } _ { 2 }$ back to the above equation gives $\mathsf { N N } _ { \mathrm { i t } } { = } - 0 . 0 6 4 \mathsf { U E } _ { \mathrm { i t } } .$ . In other words, the marginal effect of additional news coverage on expected change of CAR is positive only if the unexpected earnings are negative. Having more news coverage before positive unexpected earnings actually hurts expected CAR. Given that <sup>fi</sup>rm management prefers higher CAR, the results suggest that the management should not release news if a positive earnings surprise is expected.

Second, if investors want to pro<sup>fi</sup>t from the price movement around earnings announcements, they should avoid <sup>fi</sup>rms with a high level of news coverage. Financial instruments such as call, put, and straddle options [21] can be used to pro<sup>fi</sup>t from signi<sup>fi</sup>cant stock price movements. While the investment strategies may vary depending on available information and investors' belief, stock prices need to move signi<sup>fi</sup>cantly in the expected direction in order to offset the costs associated with these <sup>fi</sup>nancial instruments and pro<sup>fi</sup>t from the investment strategies. Given the fact that news coverage reduces the ERC, investors should avoid <sup>fi</sup>rms with high news coverage if they are betting on large stock price movements.

Finally, our empirical results are based on news coverage computed from the WSJ. The WSJ is a mainstream newspaper that reaches a broad range of readers. Other news sources may reach a different group of readers and have different impacts on stock prices. For instance, newswires are usually subscribed by institutional investors and delivers <sup>fi</sup>rm-speci<sup>fi</sup>c information with small delay. While it may be dif<sup>fi</sup>cult for small <sup>fi</sup>rms to be covered by the WSJ, it is relatively easy for the management to transmit news through newswire. Similar effects may be achieved through newswires.

## 7. Conclusions and future research directions

This study investigates the in<sup>fl</sup>uence of news coverage on the ERC, which measures the information content of earnings. We collected news articles in the Wall Street Journal from August 1999 through February 2007 to construct measures for news coverage on S&P 500 companies. Combined with data from classical <sup>fi</sup>nancial databases such as IBES, Compustat and CRSP, we were able to study the effect of news coverage on earnings surprise.

Our empirical results indicate that news coverage has a signi<sup>fi</sup>- cantly negative effect on the ERC; higher news coverage decreases the information content of earnings and reduces market responses to unexpected earnings. While news coverage is correlated with <sup>fi</sup>rm size, the empirical evidences suggest that our <sup>fi</sup>ndings are not a size effect. In addition, news coverage is not subsumed by book-to-market ratio, share turnover rate, and return momentum.

Our study highlights the importance of <sup>fi</sup>nancial news in conveying value-related information to the markets. We plan to include more information sources such as newswires, blogs and forum discussions to further investigate the interaction and relative importance of different sources. We are also interested in studying the interaction between news sentiment and return-earnings relations. Sophisticated <sup>fi</sup>rm-based sentiment measures may reveal the underlying relationship among various textual information sources and how investors interpret the sentiment under the context of <sup>fi</sup>rm valuation.

## Acknowledgements

This work was supported in part by the US National Science Foundation under grant CNS-0709338 and the National Science Council of Taiwan (NSC97-2410-H002-125-MY3). Any opinions, <sup>fi</sup>ndings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily re<sup>fl</sup>ect the views of the National Science Foundation.

## References

[1] J.S. Abarbanell, W.N. Lanen, R.E. Verrecchia, Analysts' forecasts as proxies for investor beliefs in empirical research, Journal of Accounting and Economics 20 (1) (1995).31-60

[2] R. Ball, P. Brown, An empirical evaluation of accounting income numbers, Journal of Accounting Research 6 (2) (1968) 159–178

[3] R.M. Baron, D.A. Kenny, The moderator–mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations, Journal of Personality and Social Psychology 51 (6) (1986) 1173–1182.

[4] S. Basu, The conservatism principle and the asymmetric timeliness of earnings, Journal of Accounting & Economics 24 (1) (1997) 3–37.

[5] W.H. Beaver, The information content of annual earnings announcements, Journal of Accounting Research 6 (1968) 67–92.

[6] W. Beaver, R. Lambert, D. Morse, The information content of security prices, Journal of Accounting and Economics 2 (1) (1980) 3–28.

[7] D.W. Collins, S.P. Kothari, An analysis of intertemporal and cross-sectional determinants of earnings response coef<sup>fi</sup>cients, Journal of Accounting and Economics 11 (2–3) (1989) 143–181.

[8] D.W. Collins, S.P. Kothari, J.D. Rayburn, Firm size and the information content of prices with respect to earnings, Journal of Accounting and Economics 9 (2) (1987) 111–138.

[9] D.W. Collins, S.P. Kothari, J. Shanken, R.G. Sloan, Lack of timeliness and noise as explanations for the low contemporaneuos return-earnings association, Journal of Accounting and Economics 18 (3) (1994) 289–324.

[10] P.M. Dechow, I.D. Dichev, The quality of accruals and earnings: the role of accrual estimation errors, The Accounting Review 77 (2002) 35–59.

[11] D.S. Dhaliwal, L.E.E. Kyung Test, The association between unexpected earnings and abnormal security returns in the presence of <sup>fi</sup>nancial leverage, Contemporary Accounting Research 8 (1991) 20–41.

[12] P.D. Easton, T.S. Harris, J.A. Ohlson, Aggregate accounting earnings can explain most of security returns: the case of long return intervals, Journal of Accounting and Economics 15 (2–3) (1992) 119–142.

[13] P.D. Easton, M.E. Zmijewski, Cross-sectional variation in the stock market response to accounting earnings announcements, Journal of Accounting and Economics 11 (2–3) (1989) 117–141.

[14] E.F. Fama, L. Fisher, M.C. Jensen, R. Roll, The adjustment of stock prices to new information, International Economic Review 10 (1) (1969) 1–21.

[15] E.F. Fama, K.R. French, Common risk factors in the returns on stocks and bonds, Journal of Financial Economics 33 (1) (1993) 3–56.

[16] J. Francis, R. LaFond, P.M. Olsson, K. Schipper, Costs of equity and earnings attributes, Accounting Review 79 (2004) 967–1010.

[17] J. Gerdes, EDGAR-Analyzer: automating the analysis of corporate data contained in the SEC's EDGAR database, Decision Support Systems 35 (1) (2003) 7–29.

[18] J.R. Graham, C.R. Harvey, S. Rajgopal, The economic implications of corporate <sup>fi</sup>nancial reporting, Journal of Accounting & Economics 40 (1–3) (2005) 3–73.

[19] W.T. Harrison, C.T. Horngren, Financial Accounting, 5th edPrentice Hall, 2003.

[20] C. Hayn, The information content of losses, Journal of Accounting & Economics 20 (2) (1995) 125–153.

[21] J.C. Hull, S. Basu, Options, Futures, and Other Derivatives, 7th edPearson, 2010.

[22] R. Jacobson, D. Aaker, Myopic management behavior with ef<sup>fi</sup>cient, but imperfect, <sup>fi</sup>nancial markets — a comparison of information asymmetries in the United States and Japan, Journal of Accounting & Economics 16 (4) (1993) 383–405.

[23] N. Jegadeesh, S. Titman, Returns to buying winners and selling losers: implications for stock market ef<sup>fi</sup>ciency, The Journal of Finance 48 (1) (1993) 65–91.

[24] R. Kormendi, R. Lipe, Earnings innovations, earnings persistence, and stock returns, The Journal of Business 60 (3) (1987) 323.

[25] S.P. Kothari, Capital markets research in accounting, Journal of Accounting & Economics 31 (1-3)(2001) 105–231.

[26] S.P. Kothari, R.G. Sloan, Information in prices about future earnings: implications for earnings response coef<sup>fi</sup>cients, Journal of Accounting and Economics 15 (2–3) (1992) 143–171.

[27] J. Livnat, R.R. Mendenhall, Comparing the post earnings announcement drift for surprises calculated from analyst and time series forecasts, Journal of Accounting Research 44 (1) (2006) 177–205.

[28] T.J. Lopez, L. Rees, The effect of beating and missing analysts' forecasts in the information content of unexpected earnings, Journal of Accounting, Auditing & Finance 17 (2002) 155–184.

[29] Z. Ma, O.R.L. Sheng, G. Pant, Discovering company revenue relations from news: a network approach, Decision Support Systems 47 (4) (2009) 408–414.

[30] J. Muntermann, Towards ubiquitous information supply for individual investors: a decision support system design, Decision Support Systems 47 (2) (2009) 82–92.

[31] D. Skinner, R. Sloan, Earnings surprises, growth expectations, and stock returns or don't let an earnings torpedo sink your portfolio, Review of Accounting Studies 7 (2) (2002) 289–312.

[32] P.C. Tetlock, Giving content to investor sentiment: the role of media in the stock market, Journal of Finance 62 (3) (2007) 1139–1168.

[33] P.C. Tetlock, M. Saar-Tsechansky, S. Macskassy, More than words: quantifying language to measure <sup>fi</sup>rms' fundamentals, Journal of Finance 63 (3) (2008) 1437–1467.

![](/api/attachments/8XHPTG9W/fulltext/images/f6ef22763c7aec567f6daf9e84534f1507a74b06b21030097b014f0df6500ea5.jpg)  
Kuo-Tay Chen is an associate professor in the Department of Accounting at National Taiwan University. He received a Ph.D. degree in Management Information Systems from the University of Texas at Austin. His current research interests focus on applications of data mining, and text mining, to accounting and finance, information systems auditing, and applications of social network analysis to supply chain management and corporate governance. He has published in International Journal of Accounting Studies (Taiwan), Journal of Contemporary Accounting (Taiwan), Taiwan Accounting Review, Data & Knowledge Engineering.

![](/api/attachments/8XHPTG9W/fulltext/images/7d02cb0f365184ee54f59e7cc06700a24f9c3beacf2c62eb9d5164f788791110.jpg)

Hsin-Min Lu received the bachelor's degree in business administration and MA degree in economics from the National Taiwan University, and the PhD degree in information systems from the University of Arizona. He is an Assistant Professor in the Department of Information Management at the National Taiwan University. His research interests include data mining, text mining, and applied econometrics.

![](/api/attachments/8XHPTG9W/fulltext/images/622cce20775234596eedae77ca3c5004e33a2a272b60f586986c5b8582db68f8.jpg)

Jian-Shuen Lian received his bachelor's degree in Accounting from the National Taiwan University, Taipei, in 1995, and master degree in Information Science from the University of Pittsburgh, PA, in 2000. Now he is an Accounting PHD candidate at the National Taiwan University, Taipei.

![](/api/attachments/8XHPTG9W/fulltext/images/90d10a3777cac87ec7de3d7e41fa0097ebb32bb7fc22a2564a5ea54660a01ef8.jpg)

Tsai-Jyh Chen is a professor of risk management and insurance at the National Chengchi University (NCCU). She received her Ph.D. from the Wharton School, University of Pennsylvania. She was the chairman of the Department of Risk Management and Insurance and the director of the Graduate Institute of Insurance at the NCCU. Currently she serves as the director of English Taught Program in the commerce college of NCCU and the chapter advisor of International Honor Society Beta Gamma Sigma — NCCU Chapter, She has also provided services for the governmental and professional organizations. Dr. Chen has authored and translated several books and published many articles in academic and professional journals. She is the associate editor of the Insurance Issues and Practices (Taiwan Insurance Institute).

![](/api/attachments/8XHPTG9W/fulltext/images/8b8514600b8bcfce8b1cab3c077859dfdbe4ea18002cbc91adb35d28b5826dc0.jpg)

![](/api/attachments/8XHPTG9W/fulltext/images/cd7bb8050108e7ced728ba7348d5d8eff7c49814782ebea4b46dc0a98d53189b.jpg)

Shu-Hsing Li received the bachelor's degree in business administration from National Chengchi University in Taiwan, and the PhD degree in accounting from New York University. He is now Professor of Accounting at National Taiwan University, and Chair Professor of Accounting at Tunghai University. He has also taught at Rutgers University and the University of Hawaii at Manoa. His academic publications have appeared in the Accounting Review, Journal of Accounting, Auditing and Finance, European Journal of Operational Research, Review of Quantitative Finance and Accounting, IEEE Intelligent Systems, and other scholarly journals. He is currently the Editor of NTU Management Review, and the Director of Enterprise Risk

Management and Business Intelligence Research Center at National Taiwan University. He is the leading scholar in Taiwan working on the transfer pricing for multinational companies.

Hsinchun Chen received the BS degree from the National Chiao-Tung University in Taiwan, the MBA degree from the State University of New York at Buffalo, and the PhD degree in information systems from New York University. He is a McClelland professor of management information systems at the University of Arizona. He has served as a scientific counselor/advisor of the US National Library of Medicine, the Academia Sinica (Taiwan), and the National Library of China (China). He is a fellow of the IEEE and the AAAS. He received the IEEE Computer Society 2006 Technical Achievement Award. He was ranked #8 in publication productivity in information systems (CAIS 2005) and #1 in Digital Library research (IP&M 2005) in two bibliometric studies. His COPLINK system, which has been quoted as a national model for public safety information sharing and analysis, has been adopted in more than 550 law enforcement and intelligence agencies in 20 states.
