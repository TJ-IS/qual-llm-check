---
otero_id: 11278
otero_key: "B9RM62W4"
title: "Towards ubiquitous information supply for individual investors: A decision support system design"
authors: "Jan Muntermann"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards ubiquitous information supply for individual investors: A decision support system design

Jan Muntermann ⁎

Faculty of Economics and Business Administration, Goethe-University Frankfurt, 60323 Frankfurt, Germany

a r t i c l e i n f o

Article history: Received 23 October 2007 Received in revised form 13 January 2009 Accepted 25 January 2009 Available online 1 February 2009

Keywords: Financial decision support Ubiquitous information provisioning Design science

## a b s t r a c t

This paper introduces an IT artifact called MoFiN DSS that comprises hard- and software components that provide the basis for a prototype of a <sup>fi</sup>nancial decision support system (DSS) to support individual investors reacting to unforeseen market events. We have derived our motivation for building such a system design from behaviora <sup>fi</sup>nance research. Analyses of the behavior of individual investors provide evidence that this segment does react more signi<sup>fi</sup>cantly to any public news published compared to institutional investors. On the other hand, the analyses show that they react signi<sup>fi</sup>cantly slower than their institutional counterparts. Since empirical intraday event study analyses show that capital markets react promptly to new information and that excess returns decrease over a speci<sup>fi</sup>c period of time, individual investors miss signi<sup>fi</sup>cant trading opportunities due to their current strategies of information research. We address the problem that this market segment is not able to continuously observe diverse information channels and to assess all the new information available. Our prototype decision support system continuously observes company announcements and forecasts their potential impact on the corresponding stock price. After identifying those events for which signi<sup>fi</sup>cant market reactions can be expected, wireless push-based message services provide the technical basis for prompt and location-independent information supply. Based on a novel simulation-based evaluation methodology we have developed, we demonstrate and quantify the advantages that the developed system provides to the individua investors.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction and motivation

In the last years, the banking industry and especially the brokerage sector has faced dramatic changes due the impact of new information and communication technologies available. These changes have affected intra-organizational processes as well as communication structures and customer services [14,25,42]. This ongoing change has been addressed by various empirical studies evaluating its impact including productivity gains or cost savings achieved [12,38,49].

In the retail banking sector, online banking and brokerage services are one success story how the adoption of information and communication technology can on the one hand positively affect business pro<sup>fi</sup>tability and on the other hand provide signi<sup>fi</sup>cant relative advantage to customers [55]. In this paper, we focus on the retail brokerage market segment, where customers, i.e. individual investors rely in particular on prompt information supply. The supply of corresponding Internet resources and web-based transaction services has addressed these needs in recent years. However, individual investors are still not playing on the same level playing <sup>fi</sup>eld with their institutional counterparts since they are not able to observe current developments all the time, i.e. they don't have ubiquitous information and market access. This results in behavior patterns that clearly separate individual investors from institutional ones.

Compared to the institutional investors, the individual investors are much more attention-driven, i.e. they are more likely to react to new public information available [4] such as newly published company announcements [23]. As a result, higher trading volumes of individual investors can be observed on a relative basis in such cases [8].

While the trading behavior of individual investors seems largely affected by news being published by companies or by the news, their information supply is mainly pull-driven and stochastic, i.e. they receive their information from classic information channels such as Internet or TV and only when these channels are currently available. This way of information search has signi<sup>fi</sup>cant impact on how the individual investors trade on the <sup>fi</sup>nancial markets.

The empirical observations of Dey and Radhakrishna [16] for example provide evidence that individual investors react with a signi<sup>fi</sup>cant delay to new information available and therefore miss opportunities that institutional investors do exploit since they react promptly. These opportunities have been observed and quanti<sup>fi</sup>ed by several intraday event studies that analyze the impact of newly disseminated information on <sup>fi</sup>nancial markets [6,19]. There is strong evidence here that <sup>fi</sup>nancial markets react promptly to newly published information and that the signi<sup>fi</sup>cance of abnormal excess market returns is declining within the course of time [40,50].

In this paper, we address this discrepancy of the described behavior of individual investors who react on newly and publicly published information such a company announcements more signi<sup>fi</sup>cantly (in terms of increased trading volume) but also more slowly than the institutional ones. The trading opportunities they miss due to their current strategies of information research is addressed in this paper with a prototype DSS that has been developed on basis of the design science research paradigm [34]. We used this framework and have developed an IT artifact (Mobile Financial Noti<sup>fi</sup>cation Decision Support System — MoFiN DSS) that comprises both hard- and software components representing our prototype system. MoFiN DSS addresses the problem domain described and collects, processes, and provides information in a way to support individual investors reacting faster to new information published by companies and to focus on most relevant events. Providing anytime and anywhere access to relevant <sup>fi</sup>nancial information opens up a window of opportunity for private investors. This is addressed by using wireless communication technologies that provide the technological basis to increase the level of ubiquitous information supply. We call this approach “towards ubiquitous information supply” in the following.

The remainder of the paper is organized as follows: Section 2 (Research approach) presents an introduction to the design science research paradigm and provides theoretical foundations for our approach. Then, Section 3 introduces the IT artifact (MoFiN DSS) we have developed. MoFiN DSS provides time-critical information and decision support via wireless communication channels and devices. The application of mobile communication and information technologies have been well recognized in this research <sup>fi</sup>eld since they can provide a new technological basis for existing information problems and for exploring new opportunities in data management and information provisioning [33].

First, we econometrically develop forecasting models that are used for (1) identifying those company announcements for which signi<sup>fi</sup>cant effects can be expected on the capital markets and for (2) estimating the period of time for which abnormal price effects can be expected (price effect duration). The forecasting models are based on quantitative metrics that we adapt from empirical <sup>fi</sup>nancial research and which are usually used to measure and analyze the ef<sup>fi</sup>ciency of how capital markets react to new information available (so-called event studies) [9].

Then, we present the hardware infrastructure we have set up, which provides access to the data sources and communication channels needed to implement the desired functionality. By installing and connecting a GSM/GPRS gateway to our infrastructure, we are able to manage seamless information processes from classic Internet to wireless communication networks.

The software component of MoFiN DSS is a server application, which manages the entire data collection, processing and the communication process on the basis of the installed infrastructure.

Since utility and the value provided by a developed IT artifact is the central research objective of any design science research [34], we present and apply a novel simulation-based evaluation methodology in Section 4. The evaluation approach addresses the business value of IT provided by the IT artifact on the basis of increased consumer surplus [10]. The simulation-based approach addresses ex ante evaluations that are needed for IT artifact evaluations being naturally not yet adopted by the market, i.e. when no product-related empirical data, such as user behavior or transaction data, is observable.

Finally, Section 5 summarizes our contribution and presents some of the limitations of this work motivating future research.

## 2. Research approach

This research is based on the design science research paradigm that Simon [58] described in his widely cited book “The sciences of the arti<sup>fi</sup>cial” as a science that addresses arti<sup>fi</sup>cial artifacts and whose foundation is coming from both computer and management sciences. Design science research is utility-centric where identi<sup>fi</sup>ed practical problems are addressed with novel system designs in order to provide suitable solutions [45].

Typical design science research approaches address relevant and so far unsolved problem <sup>fi</sup>elds were they contribute with the design, development, and evaluation of innovative IT artifacts [21]. There is a wide range of how the term ‘IT artifact’ is de<sup>fi</sup>ned in information systems (IS) research. In this paper, we follow the de<sup>fi</sup>nition of Srinivasan et al. [59] who de<sup>fi</sup>ne the IT artifact as a “…combined hardware and software system that is designed and implemented within an organizational context and whose purpose is to collect, organize, and store data, and transform it into information needed …”. This de<sup>fi</sup>nition widely corresponds to the term “IT artifact instantiation” which March and Smith [34] de<sup>fi</sup>ne as system architectures, system designs or software prototypes that are designed in order to demonstrate the feasibility and applicability of developed models and methods.

In addition to the developing process in which a new artifact is designed, design science research demands for an evaluation process, which evaluates the artifact in a rigorous way. This evaluation can help to improve the artifact design by achieving a better understanding of the problem and the artifact's contribution to its solution [35]. The value of design science research has been well recognized [3,47], and especially in the discussion about missing relevance in IS research, IT artifacts and design science can play an important role [1,28]. In general, its research output can provide valuable contributions to the applicable knowledge for IS research including its foundations (e.g. knowledge derived from the artifact designed) and methodologies (such as evaluation criteria and methodologies) [21]. In this paper, we contribute in both ways. First, Section 3 presents the IT artifact we have developed in order to address the problem <sup>fi</sup>eld described. Second, we have developed and applied novel evaluation criteria and a simulation-based evaluation methodology (Section 4) providing the basis for an evaluation of the developed IT artifact. Since the developed artifact or a corresponding product is not available on the market yet (i.e. there exist no observations of investors' behavior), such an ex ante evaluation approach needs to be applied.

## 3. Design of a mobile <sup>fi</sup>nancial noti<sup>fi</sup>cation decision support system IT artifact (MoFiN DSS)

## 3.1. System characteristics and functionalities

Motivated by the current behavior of individual investors, the developed IT artifact aims at (1) reducing the reaction time of individual investors to unforeseen but relevant events that can have signi<sup>fi</sup>cant effects on stock prices and (2) to provide decision support when identifying those events for which considerable price reactions can be expected. To further describe the prototype DSS we have developed, we use Power's DSS classi<sup>fi</sup>cation framework [52,53].

According to this framework, almost every DSS can be described by four dimensions:

1. Targeted users (intra- vs. inter-organizational)

2. Enabling technology (e.g. web-based)

3. Purpose (e.g. task-speci<sup>fi</sup>c or general-purpose)

4. Dominant component driver (e.g. model- vs. data-driven).

Our system design represents an intra-organizational system where individual investors represent the target user group of the system design. In recent years, many such customer decision support systems (CDSS) have been introduced by online banks and online brokers providing access to information recourses [36,46]. One the one hand side, these services represent a cost-ef<sup>fi</sup>cient alternative within the communication channel mix in order to retain and build new relationships with customers [30]. On the other hand, today's customers of retail banks and brokers demand for useful <sup>fi</sup>nancial and decision support systems that are usually provided on retail banking and brokerage websites [26,62]. In contrast, mobile <sup>fi</sup>nancial information services are still in its infancy although they have been predicted to become one essential driver of successful mobile commerce [20,32]. Whereas around 40% of today's mobile device users believe in possible advantages provided by mobile banking and stock trading services [61], the diffusion of mobile banking services has not met expectations yet [56].

Usefulness and relative advantage were identi<sup>fi</sup>ed as major success factors for the customers' willingness to adopt mobile banking services [37,29,31]. However, most mobile <sup>fi</sup>nancial services being available today are adapted versions of established online banking services addressing the same application scenarios such as providing access to stock quotes or calculating currency conversion [32]. Consequently, these services fail to provide signi<sup>fi</sup>cant relative advantage compared to the existing electronic banking services.

The system functionalities of the MoFiN DSS IT artifact aim at bridging this gap by proactively providing time-critical information and to provide further decision support in these situations.

The <sup>fi</sup>rst objective is addressed with an infrastructure design that enables wireless data processing to a personal mobile device of an investor. Therefore, mobile devices and messaging services provide the enabling technology that provide <sup>fl</sup>exible information supply and decision support on the basis of wireless communication technologies. In decision support system research, the potential of mobile services has been well recognized since they can provide ubiquitous access to information and decision support tools [43,57]. These potentials have been explored for different application domains such as location-based DSS [7,44] or eHealth DSS [48]. Using wireless technologies to support security-relevant processes and the ubiquitous environment raise security and privacy questions. Typical security requirements comprise accountability, availability, con<sup>fi</sup>dentiality, and integrity. These issues have been addressed in [41], in which a SIM-based security token is proposed to secure con<sup>fi</sup>dential mobile information and transaction services.

The system design is further characterized by task-speci<sup>fi</sup>city because it is designed to support individual investors during tasks being well-described and that repeat repetitively (system purpose). On the other hand, <sup>fi</sup>nancial DDS typically address problems in dynamic, complex, and unstructured situations [22]. An investment decision process that should be supported in a ubiquitous environment is similarly unstructured due to the general complexity of capital markets. Like in most other practical decision-support application domains, the addressed problem is consequently semi-structured featuring both structured and unstructured elements [18,60].

The described decision situation is supported by forecasting models (component driver) for estimating the magnitude and duration of the stock price reaction following newly published company announcements. These forecasting models make the developed decision support system concept model-driven [53] and are being presented in the following section.

## 3.2. Decision support forecasting models

Becoming a central part of the MoFiN DSS IT Artifact, the <sup>fi</sup>rst forecasting model should provide the functionality to identify relevant company announcements for which signi<sup>fi</sup>cant price reactions of the corresponding stock can be expected. The development of the forecasting models is based on an empirical dataset that comprises 425 company announcements (called events i in the following) that were published and collected between 2003-08-01 and 2005-07-31. Furthermore, corresponding intraday stock and CDAX index prices p (at price <sup>fi</sup>xing t on a one-minute basis) were collected for the same period. All data stems from primary data sources (e.g. Frankfurt Stock Exchange Xetra), and was processed automatically in order to avoid errors from manual processing and as a necessity for processing voluminous intraday security price series.

The intraday price series were recorded exact to the minute on the basis of tick-by tick transaction prices. If, within the interval of one minute, more than one transaction (and the corresponding price) has been observed, the last price of the one minute interval is used. The resulting minute-by-minute intraday prices (which we call price fixings in the following) provide the basis for the following calculations.

With the aim of identifying relevant events, the forecasting model is based on post-event abnormal returns that describe the abnormality of intraday stock price returns that follow the publication of an announcement.

The way of calculating these metrics stems from <sup>fi</sup>nancial research, more precisely from event study analysis. Event studies explore the semi-strong form of the ef<sup>fi</sup>cient market hypothesis after which security prices adjust ef<sup>fi</sup>ciently to new information available [17]. By analyzing security price adjustments following unforeseen market events, event studies aim to detect excess returns on the market [39]. Since the forecasting model should detect events that will cause such excess returns, we have chosen this methodical approach for calculating appropriate metrics representing the basis for the forecasting model.

Following the approach of Carter and Soo [11] and Muntermann and Güttler [40], we <sup>fi</sup>rst calculate a mean absolute abnormal return MAAR for each event and prior to the event day. Here, stock returns (<sup>fi</sup>rst logarithmic term) are <sup>fi</sup>rst adjusted by a general market trend (second logarithmic term for returns of the general CDAX market index). Then, an average for the absolute subtraction term is calculated for all price <sup>fi</sup>xings that were observed during an estimation window.

Since the model needs to be implemented and applied real-time when a company announcement has been observed, we decided to make use this simple procedure to calculate abnormal returns. Empirical analyses provide evidence that more complex procedures (such as a market model) do not perform signi<sup>fi</sup>cantly better than simple procedures (such as mean adjusted returns) when modeling abnormal price behavior on the basis of intraday data [2].

Since we aim at developing a forecasting model featuring low false positive rates (i.e. identi<sup>fi</sup>ed announcements should be relevant in terms of a market reaction), we propose a conservative model that adjusts stock returns by both a market trend and a return mean.

We use 10 days prior to the event date but excluded the day prior to the event day which might be affected by insider trading or anticipation effects. This approach complies with the standard event study methodology approach to calculate return adjustments [51]. The limitation of 10 days results from the maximum length of intraday prices series that can be requested from the stock exchanges and from the fact that other data providers (such as CRSP) provide daily price data only. However, each calculation of MAAR is based on up to 11,880 price <sup>fi</sup>xings (for both stock and index: 9 days 11 h 60 min) depending on the number of price <sup>fi</sup>xings available.

$$
M A A R _ {i} = 1 / T \sum_ {t = 1} ^ {T} \left| \ln \left(\frac {P _ {i , t}}{P _ {i , t - 1}}\right) - \ln \left(\frac {P _ {C D A X , t}}{P _ {C D A X , t - 1}}\right) \right|.
$$

These MAAR can be interpreted as momentum of the affected stock and measures the average abnormal price behavior of this stock when the corresponding company has not published any announcements. If a stock generally shows a more volatile price behavior, this will increase the MAAR value calculated. In the following, the MAAR values are taken to exclude any price effects that result from high asset volatilities. Using these MAAR , so-called corrected absolute abnormal returns $C A A R _ { i , t }$ are calculated for the stock price quotes following the event.

$$
C A A R _ {i, t} = \left| \ln \left(\frac {P _ {i , t}}{P _ {i , t - 1}}\right) - \ln \left(\frac {P _ {C D A X , t}}{P _ {C D A X , t - 1}}\right) \right| - M A A R _ {i}.
$$

Table 2  
Table 1  
Variables for event relevance forecasting.

<table><tr><td>Dependent variable</td><td>Variable description</td></tr><tr><td> $\mathop{\sum }\limits_{{t = 3}}^{{10}}{CAAR}_{i,t}$ </td><td>Corrected absolute abnormal return cumulated over the third to tenth price fixing (subsequent to the event) of the stock affected by event i following the event date.</td></tr><tr><td>Independent variables</td><td>Variable description</td></tr><tr><td> ${CAAR}_{i,1}$  and  ${CAAR}_{i,2}$ </td><td>Corrected absolute abnormal return of the first (and second) price fixing (subsequent to the event) of the stock affected by event i following the event date.</td></tr></table>

This metric provides the basis for the forecasting model that is built in the following by an OLS regression based on a time series model, i.e. it assumes that observations of earlier variable values can be used to forecast following values by discovering a pattern (such as trends or seasonality) that might exist in the historical observations.

Therefore, the <sup>fi</sup>rst two CAARs being calculated subsequent to an event observed are used as predictors in order to forecast following excess returns. The intraday event study presented by Muntermann and Güttler [40] provides evidence that excess returns can be expected for the <sup>fi</sup>rst ten price <sup>fi</sup>xings (also on a one-minute basis) following the observed event type. Therefore, a CAAR cumulated over the third to tenth price <sup>fi</sup>xing is chosen as dependent variable. Table 1 summarizes these model variables.

In the following, a multiple linear OLS regression was conducted in order to estimate the parameters of a forecasting model that can be used for price effect forecasts.

Effectiveness evaluation of developed DSS and their underlying models is considered as a central aspect of DSS research [27,54]. Therefore, we used only 200 of the observed events to develop the forecasting model. The remaining 225 events are used later for evaluating the developed IT artifact in order to analyze how its usage will improve decision quality of personal investors being supported by the system.

Regression results (Table 2) show that the developed forecasting model can account for 36.5% (R<sup>2</sup>) of the variation of the dependent variable to be forecasted.

The models F-value of 53.835 (p-valueb0.1%) corroborates that the OLS regression has generated a forecasting model featuring signi<sup>fi</sup>cant predictive power.

As a result of the OLS regression, the price effect forecasting model is given as:

$$
F \left(\sum_ {t = 3} ^ {1 0} C A A R _ {i, t}\right) = 0. 0 1 3 + 0. 5 3 1 \cdot C A A R _ {i, 1} + 1. 3 6 6 \cdot C A A R _ {i, 2}.
$$

As a typical time series model, the two abnormal price effects following the event $( C A A R _ { i , 1 }$ and $C A A R _ { i , 2 } )$ have a signi<sup>fi</sup>cant positive impact on the subsequent abnormal price behavior, i.e. the forecasting objective. The Durbin/Watson test statistic does not provide any evidence for serial correlation in the residuals of the regression.

Price effect forecasting model regression results.

<table><tr><td colspan="6">Model summary</td></tr><tr><td>R</td><td> $R^2$ </td><td>Adj.  $R^2$ </td><td>Durbin-W. st.</td><td>F-value</td><td>Significance</td></tr><tr><td>0.604(a)</td><td>0.365</td><td>0.359</td><td>1.803</td><td>53.835</td><td>&lt;0.001(a)</td></tr><tr><td colspan="6">Coefficients(b)</td></tr><tr><td rowspan="2"></td><td colspan="2">Unstandardized coefficients</td><td colspan="2">Standardized coefficients</td><td></td></tr><tr><td>βj-value</td><td>Std. error</td><td>Beta</td><td>t-value</td><td>Significance</td></tr><tr><td>(Constant)</td><td>0.013</td><td>0.005</td><td></td><td>2.561</td><td>0.011</td></tr><tr><td> $CAAR_{i,1}$ </td><td>0.531</td><td>0.077</td><td>0.406</td><td>6.870</td><td>&lt;0.001</td></tr><tr><td> $CAAR_{i,2}$ </td><td>1.366</td><td>0.209</td><td>0.386</td><td>6.531</td><td>&lt;0.001</td></tr></table>

(a) Predictors: (Constant), CAAR , CAAR .  
(b) Dependent variable: $\sum _ { t = 3 } ^ { 1 0 } C A A R _ { i , t } .$

Table 3  
Variables for price effect duration forecasting.

<table><tr><td>Dependent variable</td><td>Variable description</td></tr><tr><td> $\Delta t_{i,3,10}$ </td><td>Price effect duration measured in minutes, in which the third to tenth price fixings of the stock affected by event i can be observed following the event date.</td></tr><tr><td>Independent variables</td><td>Variable description</td></tr><tr><td> $\Delta t_{i,1,2}$ </td><td>Period of time measured in minutes, in which the first two price fixings of the stock affected by event i can be observed following the event date.</td></tr><tr><td> $TVol_{i,1,2}$ </td><td>Sum of the trading volume measured in number of stocks traded (in 1000 stocks) during the two first price fixings following the event date.</td></tr><tr><td>#Analystsi</td><td>Number of analysts covering the company that has published the announcements.</td></tr></table>

In order to identify relevant events, this function can be used for providing decision support to individual investors. In case of an event observed, corrected absolute abnormal returns will automatically be calculated for the <sup>fi</sup>rst two price <sup>fi</sup>xings following the event date and then used as input factors for the forecasting model. If the forecasted price effect exceeds the effect that can be observed on average (we observed a mean of approx. 2.47%), an event will be treated as relevant and will trigger a noti<sup>fi</sup>cation process.

A second forecasting model addresses the price effect duration, i.e. period of time within which an investor has to react to be able to pro<sup>fi</sup>t from excess market returns following the event observed. Therefore, its dependant variable is de<sup>fi</sup>ned as the period of time which corresponds to the third to tenth price <sup>fi</sup>xing following the event date. In contrast to the price effect forecasting model being solely based on a time series model approach, the price effect duration model uses further explanatory variables. Dependent and independent variables are listed and further explained in the following Table 3.

We calculated $\Delta t _ { i , 3 , 1 0 }$ and $\Delta t _ { i , 1 , 2 }$ for the forecasting dataset and collected the trading volumes and analyst coverage. Again, a multiple linear OLS regression was conducted to estimate the model parameters. Table 4 shows results for this regression including model the model summary and parameter details.

With an F-value of 30.054 (p-valueb0.1%) the models provides signi<sup>fi</sup>cant predictive power. Using the β -values for the predictors, the price effect duration forecasting model is given as:

$$
F \left(\Delta t _ {i, 3, 1 0}\right) = 3 6. 7 0 + 0. 0 8 2 \cdot \Delta t _ {i, 1, 2} - 0. 0 1 8 \cdot T V o l _ {i, 1, 2} - 0. 6 8 1 \cdot \# A n a l y s t s _ {i}.
$$

The forecasting model states that the price effect duration will be increased by the period after which the two <sup>fi</sup>rst price <sup>fi</sup>xings (following the event) can be observed. Furthermore, the duration decreases when high trading volumes $( T V o l _ { i , 1 , 2 } )$ can be observed and when there is a higher number of analysts covering the corresponding company, i.e. more market participants observe this company and react to the event. The Durbin/Watson test statistic indicates only very weak positive autocorrelation which we tolerate because it is not a pure time series regression.

Price effect duration forecasting model regression results

<table><tr><td colspan="6">Model summary</td></tr><tr><td>R</td><td> $R^{2}$ </td><td>Adj.  $R^{2}$ </td><td>Durbin-W. st.</td><td>F-value</td><td>Significance</td></tr><tr><td>0.561(a)</td><td>0.315</td><td>0.305</td><td>1.457</td><td>30.054</td><td>&lt;0.001(a)</td></tr><tr><td colspan="6">Coefficients(b)</td></tr><tr><td rowspan="2"></td><td colspan="2">Unstandardized coefficients</td><td colspan="3">Standardized coefficients</td></tr><tr><td> $\beta_{j}$ -value</td><td>Std. error</td><td>Beta</td><td>t-value</td><td>Significance</td></tr><tr><td>(Constant)</td><td>36.700</td><td>1.377</td><td></td><td>26.650</td><td>&lt;0.001</td></tr><tr><td> $\Delta t_{i,1,2}$ </td><td>0.082</td><td>0.045</td><td>0.110</td><td>1.815</td><td>0.071</td></tr><tr><td> $TVol_{i,1,2}$ </td><td>-0.018</td><td>0.006</td><td>-0.190</td><td>-3.149</td><td>0.002</td></tr><tr><td>#Analysts $_{i}$ </td><td>-0.681</td><td>0.088</td><td>-0.474</td><td>-7.783</td><td>&lt;0.001</td></tr></table>

(a) Predictors: (Constant), Δt , TVol , #Analysts .  
(b) Dependent variable: Δt<sub>i,3,10</sub>.

![](/api/attachments/B9RM62W4/fulltext/images/38766a4ab428e43140d1d7c331fe1dc6a8b5a60164a7513d38c2b4906801ed36.jpg)  
Fig. 1. Example of the price adjustment process.

We expect that investors reacting quicker to relevant information will generally be able higher pro<sup>fi</sup>ts on average (This is explored in Section 4 evaluation the bene<sup>fi</sup>ts of timelier information supply provided by the system design). Therefore, the forecasts are used in order to prevent reacting to any events where stock prices should already fully re<sup>fl</sup>ect the new information available.

The entire price adjustment process is further illustrated in Fig. 1 showing an example of a price adjustment process.

On the basis of $C A A R _ { i , 1 }$ and $C A A R _ { i , 2 }$ that were calculated for the example event, the price effect forecasting model estimates a signi<sup>fi</sup>cant corrected absolute abnormal return of 3.22% cumulated over the third to tenth price <sup>fi</sup>xing. As shown in Fig. 1, the effective price effect that can be observed is even higher with more than 5%. For the corresponding price effect duration $\Delta t _ { i , 3 , 1 0 } ,$ the price effect duration model forecasted a period of 12.88 min given the input values for the variables $\Delta t _ { i , 1 , 2 } , T V o l _ { i , 1 , 2 } ,$ and #Analysts .

Since the estimated price effect is signi<sup>fi</sup>cantly higher than the noti<sup>fi</sup>cation threshold (i.e. the price effect that can be observed on average), this will trigger a noti<sup>fi</sup>cation. An investor will receive a noti<sup>fi</sup>cation two minutes subsequent to the event (plus a short period that is needed to deliver the message via the wireless network). If the investor makes a prompt and correct investment decision (i.e. to buy the stock since the stock price will rise), there is a chance to realize an intraday pro<sup>fi</sup>t of 7.36%. This pro<sup>fi</sup>t results from a stock price increase of 120.50 € to 129.37 € that has been observed for this example for the remaining trading day.

Both forecasting models provide a functional basis of the decision support system which is introduced in the following section.

## 3.3. IT artifact design

Following the IT artifact de<sup>fi</sup>nition of Srinivasan et al. [59] the developed IT artifact MoFiN DSS comprises both hard- and software components. These components process and analyze data from different data sources in a way to provide ubiquitous decision support to private investors. Decision support is provided proactively to the investor in case of a relevant company announcement has been published and observed by the system. After processing the information within a client/server infrastructure, it is sent wireless via a mobile push services to a personal mobile device of the investor. Fig. 2 illustrates the hardware setup providing the system's infrastructural basis.

The two servers on the left hand side of Fig. 2 (News Feed Server and Stock Prices Server) provide the input data including company announcements being published and the intraday quotes of affected stocks. These data sources are aggregated and made accessible via XML (eXtensible Markup Language) web services by a Financial Information Server that is operated and provided by the Interactive Data Managed Solutions AG.

The MoFiN DSS Application Server (running the server software component that is presented in the following) receives required data from the Financial Information Server, which provides dynamically generated XML documents. When MoFiN DSS Application Server has identi<sup>fi</sup>ed a company announcement for which signi<sup>fi</sup>cant excess returns are forecasted, it will initiate a mobile push message to be sent via the GSM Push Gateway Server to which a GSM/GPRS class 10 modem is connected (Multitech MultiModem GPRS). The GSM/GPRS modem is accessed via Now SMS/MMS Gateway and the entire communication is based on HTTP protocol over a standard TCP/IP Internet connection. In the current installation setup, sending mobile messages via the GSM network does account for most of the latency within the entire data transmission process (see Fig. 2), especially when sending MMS (which includes graphical information) that is uploaded via a GPRS connection. Whereas SMS and WAP Push messages are sent within a few seconds, sending MMS can take up to \~20 s on our infrastructure. However, this could signi<sup>fi</sup>cantly be reduced by replacing this component with a professional push gateway installation.

![](/api/attachments/B9RM62W4/fulltext/images/e5e54702fcd006a59fa43179729676a1e4a515b530e33f7d204816a12ee49455.jpg)  
Fig. 2. MoFiN DSS hardware infrastructure.

After initiating a message to be sent, a mobile push message (e.g. based on the Short Message Service SMS, Multimedia Service Message MMS or Wireless Application Protocol (WAP) Push) is sent wireless to the Mobile Device of the individual investor who is then able to react promptly to the information provided. This can be done via mobile transaction services that were introduced by online banks and brokers in recent years.

In addition to these hardware components, the MoFiN DSS IT artifact has a server software component (Fig. 3) that manages the described data processing. Fig. 2 depicts the graphical user interface of this server software and shows the observation and evaluation status of events that were currently observed. A list of the events, i.e. the observed company announcements, can be found in the top left-hand side providing date, time, and initiator of the announcements. Below, the announcement content can be displayed by selecting an announcement from the list above. The two dialogues on the right hand side show results of the event evaluation process using the forecasting models developed in the previous section. A critical value of the cumulated corrected absolute abnormal return (CCAAR) above which events a treated as relevant can be de<sup>fi</sup>ned on the Noti<sup>fi</sup>cation Setting tab not visible here. Here, we have chosen the CCAAR which we observed on average. Below this, the chart graphically illustrates the observed abnormal behavior (solid line) and the forecasted abnormal behavior (dashed line) of the stock price effect following the announcements date. In the depicted case, the observed event has been identi<sup>fi</sup>ed as an event being relevant and worth notifying the investor. This means, that a signi<sup>fi</sup>cant abnormal price behavior, i.e.

high positive or negative market return can be expected for the affected stock, which are worth considering a buy or sell decision.

MoFiN DSS will then initiate a mobile message to be sent wireless to the investor's mobile device. Depending on the user's preferences and device functionality, the system is able to send text messages, multimedia messages including graphical information or WAP Push messages, which feature further meta information such as an expiration date for messages that became outdated.

The screenshots presented in Fig. 4 were taken from a standard Nokia 3650 mobile phone and show an exemplary multimedia (MMS) message including textual and graphical information regarding the event observed by the system. Obviously, most of the underlying system complexity can be hidden from the user and only the most relevant information is presented. This is essential since the user has to decide whether or not and how to react to this information provided within a short period of time. Otherwise, the user will miss the window of opportunity since stock market prices will fully re<sup>fl</sup>ect the information shortly. If the user decides to react to the company announcement, existing mobile brokerage services come into play, which are offered by retail banks and online brokers since several years.

After presenting the IT artifact we have developed, we come to the question, whether or not timelier information supply and the decision support provided really open up new opportunities for individual investors. There are several studies that provide evidence that new information technology being available to investors does not necessarily provide opportunities or even lead to less investment success.

![](/api/attachments/B9RM62W4/fulltext/images/339d783bbd4bbdac9b37a3aff638f70b76a901b38aa88b621a2756105b124e38.jpg)  
Fig. 3. The user interface of the MoFiN DSS software component.

![](/api/attachments/B9RM62W4/fulltext/images/764a6537a090cc23dbb4a620af90ae2d6c6d266c54c1b49d73819a4a10405edd.jpg)

![](/api/attachments/B9RM62W4/fulltext/images/9cbe0061e8a9ceeb32980088a4346ea402059cac9b74de347dd4d7e4d255dfc7.jpg)  
Fig. 4. Push message content on a mobile device (Nokia 3650).

Barber and Odean [5] observe and analyze the trading behavior of individual investors who switched from phone-based to online banking. The empirical results provide evidence that better and timelier information supply do not automatically leads to increased performance since traders seem motivated by overcon<sup>fi</sup>dence.

On the other hand, Dey and Radhakrishna [16] have explored intraday trading volume reactions to earnings announcements, being an event type similar to the ones observed and processed MoFiN DSS. Their results provide evidence that individual investors react with a signi<sup>fi</sup>cant delay to new information available, and therefore they miss the opportunities of realizing excess returns that intraday event studies have documented in the past [19,40,50].

## 4. Empirical artifact evaluation

The evaluation of the MoFiN DDS IT artifact is performed by a simulation approach that assesses the value provided to potential customers of a corresponding decision support system. After introducing theoretical foundations in Section 4.1, Section 4.2 introduces evaluation hypotheses that address the positive value provided by the artifact's functionalities. The simulation-based evaluation utilizes different empirical datasets being presented in Section 4.3. With the goal of evaluating the formulated evaluation hypotheses, Section 4.4 illustrates how the simulation-based methodology is working and how it has been applied. Finally, Section 4.5 presents and summarizes the empirical results.

## 4.1. Theoretical foundation and evaluation criteria

The evaluation approach presented and applied in the following addresses the IT business value provided the developed decision support system. Developing and choosing appropriate IT business value evaluation methodologies play an important role in the academic and professional <sup>fi</sup>eld. Since there exist different dimensions how to measure business value, no universal evaluation approach exists. In contrast, the question of IT value provided can theoretically be decomposed into three different questions and corresponding evaluation frameworks [24]:

5. Do investments in IT increase productivity (derived from theory of production)?

6. Do investments in IT improve business performance (derived from theory of competitive strategy)?

7. Do investments in IT create value for consumers (derived from theory of the consumer)?

Depending on the evaluation problem addressed it is essential to choose a suitable evaluation framework, in order to develop or apply an appropriate evaluation methodology. Furthermore, quantitative methodologies demand for measurable evaluation metrics.

In the following, we present a simulation-based evaluation approach, which addresses the value provided to consumers, in particular to potential customers of novel <sup>fi</sup>nancial IT services. Compared to many previous frameworks, the simulation-based evaluation methodology allow an ex ante evaluation of an IT investment, which is essentially for the evaluation of IT artifact developed. The approach therefore assesses the potential value provided [15].

In our evaluation, we address two different dimensions of how the IT artifact contributes to customers' surplus. These comprise (1) the reduction of investors' reaction time and (2) the decision support provided. These two contributions provide the basis for evaluation hypotheses presented in the following.

## 4.2. Evaluation hypotheses

In order to evaluate the artifact's positive impact on customers surplus we formulate two hypotheses addressing the potential increase of pro<sup>fi</sup>tability per transaction.

H1. Reduction of the investors' reaction time leads to transactions being signi<sup>fi</sup>cantly more pro<sup>fi</sup>table on average.

H2. Concentrating on those events identi<sup>fi</sup>ed by the MoFiN DSS IT artifact leads to transactions being signi<sup>fi</sup>cantly more pro<sup>fi</sup>table on average.

These two evaluation hypotheses are addressed in the following by a simulation-based evaluation approach that should provide statistical signi<sup>fi</sup>cance and monetary valuation regarding the customers' surplus provided.

## 4.3. Empirical dataset

The simulation approach makes use of the dataset that was introduced in the forecasting model development section. This data input provides an empirical basis to ensure realistic simulation results. The original dataset of 425 company announcements and the corresponding intraday price series (called sample s in the following) provides the basis for addressing the question whether or not reduced reaction time of investors will result in higher market returns, i.e. can lead to transactions being more pro<sup>fi</sup>table to the investor on average (H1).

Since parts (200 company announcements and the corresponding stock price series) of the original dataset were used as information dataset for building the forecasting models, this data can not be used for evaluating the decision support provided. Consequently, only the remaining 225 announcements and the corresponding intraday stock price series (sub-sample ss1) were used for addressing H2.

Table 5 Paired-differences parameters and paired t-test statistics for comparing realizable return populations |R | calculated for sample s and different delay levels $d \ ( I _ { s } = 4 2 5 )$

<table><tr><td rowspan="2"></td><td colspan="8">Paired differences delay levels (d1,d2) in minutes</td></tr><tr><td>(105,120)</td><td>(90,105)</td><td>(75,90)</td><td>(60,75)</td><td>(45,60)</td><td>(30,45)</td><td>(15,30)</td><td>(0,15)</td></tr><tr><td>Mean in %</td><td>0.14</td><td>0.28</td><td>0.19</td><td>0.34</td><td>0.34</td><td>0.32</td><td>0.48</td><td>2.77</td></tr><tr><td>t-value</td><td>1.62*</td><td>3.21**</td><td>1.55+</td><td>1.92*</td><td>2.95**</td><td>2.77**</td><td>2.92**</td><td>4.37**</td></tr></table>

⁎⁎, ⁎ and <sup>+</sup> indicate signi<sup>fi</sup>cance at the 1%, 5% and 10% level respectively.

From this dataset, a second sub-sample ss2 was created in order to assess the quality of the decision support provided. Therefore, ss2 contains those 86 company announcements (and the corresponding stock price series) that were classi<sup>fi</sup>ed as relevant by the decision support component of MoFiN DSS, i.e. the corresponding forecasting model estimated a price effect lying above the effect that can be observed on average. The announcements in sub-sample ss2 therefore represent a collection of events about whose occurrence an investor would be noti<sup>fi</sup>ed when using MoFiN DDS since the price effect forecasting model has tagged these events as relevant.

The evaluation should provide evidence to the questions whether or not a reduced reaction time (H1) and the decision support provided (H2) leads to transactions being more pro<sup>fi</sup>table to the investor on average. On the basis of the three (sub-)samples created, the simulation setup will address these questions.

## 4.4. Simulation setup

The simulation setup covers potential transactions performed by investors incorporating the impact of reduced reaction time (due to timelier information supply) and decision support. Consequently, an experimental evaluation approach is chosen that simulates the impact of the IT artifact on the basis of arti<sup>fi</sup>cial and historical data (i.e. the (sub-)sample created) [21].

The simulation is based on the calculation of different performance metrics. These comprise realizable returns and mean realizable yield taking different behavior of investors such as different delay levels into account. A delay level d describes be period of time (in minutes) after which the investor reacts following an announcement date. Such an event i will cause stock prices p rise or fall.

Realizable returns are de<sup>fi</sup>ned as:

$$
\left| r _ {i, d} \right| = \left| \frac {p _ {i , t _ {c}} - p _ {i , t _ {d}}}{p _ {i , t _ {c}}} \right|
$$

where $t _ { c }$ is de<sup>fi</sup>ned as close of trading at the event date and $t _ { d }$ is the timestamp d minutes subsequent to the event date. Realizable returns values are simulated for different events i (depending on the used (sub-)sample) and delay levels d so that their population of values provides a basis for statistical test procedures.

First, and in order to address evaluation hypothesis H1, a realizable return population |R |is calculated using sample s, i.e. each event of the 425 (I<sub>s</sub>) events and the delay levels $d = ( 1 2 0 , 1 1 5 , . . . , 0 )$ minutes.

Second, and in order to address evaluation hypothesis H2, realizable returns $\mathsf { R } _ { d }$ populations are calculated for the two subsamples ss1 and ss2 and each delay level $d ,$ whereas sub-sample ss1 comprises 225 (I ) events and sub-sample ss2 comprises 86 $\left( I _ { s s 2 } \right)$ events.

After having generated these further two $\mathsf { R } _ { d }$ populations, it is possible to address evaluation hypothesis H2 by statistically comparing parameters of these sub-samples using appropriate statistical test procedures. All these generated $\mathsf { R } _ { d }$ populations provide the basis for following statistical test procedures.

A second evaluation metric mean realizable yield is defined, which can be used for quantifying trading pro<sup>fi</sup>ts that can be realized by investors per transaction. Investors' behavior is parameterized by the delay level d and the trading volume v an investor will trade following an event observed.

$$
\overline {{y _ {v , d}}} = \underbrace {1 / I _ {s s 1} \sum_ {i = 1} ^ {I _ {s s 1}} \left[ \left| v \cdot \frac {p _ {i , t _ {c}} - p _ {i , t _ {d}}}{p _ {i , t _ {c}}} \right| - c _ {i} \right]} _ {\text { relevant   events   (ss2)}} - \underbrace {1 / I _ {s s 2} \sum_ {i = 1} ^ {I _ {s s 2}} \left[ \left| v \cdot \frac {p _ {i , t _ {c}} - p _ {i , t _ {d}}}{p _ {i , t _ {c}}} \right| - c _ {i} \right]} _ {\text { all   events   (ss1)}}
$$

with:

$$
c _ {i} = \left\{ \begin{array}{l l} c _ {M i n} & v <   v _ {M i n} \\ c _ {F i} + c _ {v} \cdot v & v _ {M i n} <   v <   v _ {M a x} \\ c _ {M a x} & v > v _ {M a x} \end{array} \right.
$$

lower bound trading costs

upper bound trading costs:

On the basis of the evaluation metrics de<sup>fi</sup>ned, and the empirical dataset of the two sub-samples ss1 and ss2, $\overline { { y } } _ { v , d }$ values are simulated for the parameter values $d = ( 1 2 0 , 1 0 5 , . . . , 0 )$ and $\nu = ( 5 0 , 1 0 0 ,$ 1000). Trading cost parameter values $c _ { F i }$ (<sup>fi</sup>xed costs), c (variable costs), $c _ { M i n }$ (minimum costs), and $c _ { M a x }$ (maximum costs) were taken from comdirect bank AG [13], one of the largest online brokers in Germany. Their cost function and trading fee structure is comparable to those of other online brokerage service providers such as E⁎TRADE or Schwab Investor Services.

The simulation runs generate populations |R | of realizable returns for all events (sample s), all events of the evaluation dataset (subsample ss1), and those events that have been identi<sup>fi</sup>ed as relevant (subsample ss2) including all variations of delay levels $d = ( 1 2 0 , 1 0 5 , . . . , 0 ) ,$ i.e. 27 |R | populations in total. These populations are used in the following for statistically proving and assessing the bene<sup>fi</sup>ts the IT artifact provides to potential customers of MoFiN DSS.

Furthermore, a matrix of mean realizable yields $\overline { { y _ { \nu , d } } }$ is generated, which provides the basis for quantifying the value MoFiN DSS provides.

## 4.5. Simulation results

On the basis of the generated $| \mathsf { R } _ { d } |$ populations, statistical tests were conducted in order to prove if investors can signi<sup>fi</sup>cantly bene<sup>fi</sup>t when being supported with MoFiN DSS, i.e. from shorter delay levels d (Table 5 with $| \mathsf { R } _ { d } |$ populations calculated on the basis of sample s) and the decision support (Table 6 with $| \mathsf { R } _ { d } |$ populations calculated on the basis of sub-samples ss1 and ss2) provided.

First, we address evaluation hypothesis H1 and evaluate the potential advantage of shorter delay levels by comparing |r | populations at two sequential delay levels $( d 1 , d 2 ) = ( 1 0 5 , 1 2 0 ) , ( 9 0 , 1 0 5 ) , \ldots , ( 0 , 1 5 )$ . The corresponding hypotheses address the question whether or not each delay level reduction (d2 to d1; e.g. a reduction from 120 min to 105 min) leads to signi<sup>fi</sup>cant higher realizable return means.

With the objective of exploring potential differences between the two |R | populations (at different delay levels), paired t-test statistics have been applied [63]. The test addresses the hypothesis that mean difference between paired observations (i.e. the values of at different

## Table 6

|R | population parameters and unequal variances t-test statistic for comparing realizable returns of unsupported (sub-sample ss1) vs. supported (sub-sample ss2) decision-making.

<table><tr><td rowspan="2"></td><td colspan="9">Delay level d in minutes</td></tr><tr><td>120</td><td>105</td><td>90</td><td>75</td><td>60</td><td>45</td><td>30</td><td>15</td><td>0</td></tr><tr><td rowspan="2">Mean in %</td><td colspan="9"> $|r_{i,d}|$  population for sub-samples ss1 ( $I_{ss1} = 225$ )</td></tr><tr><td>1.20</td><td>1.26</td><td>1.33</td><td>1.43</td><td>1.58</td><td>1.72</td><td>1.81</td><td>1.94</td><td>2.48</td></tr><tr><td rowspan="2">Mean in %</td><td colspan="9"> $|r_{i,d}|$  population for sub-samples ss2 ( $I_{ss2} = 86$ )</td></tr><tr><td>2.71</td><td>2.84</td><td>3.51</td><td>3.65</td><td>3.66</td><td>3.72</td><td>3.67</td><td>4.83</td><td>9.24</td></tr><tr><td>t-value</td><td>2.20*</td><td>2.30*</td><td>2.97**</td><td>3.11**</td><td>3.05**</td><td>2.85**</td><td>2.68**</td><td>2.76**</td><td>1.71*</td></tr></table>

⁎⁎ and ⁎ indicate signi<sup>fi</sup>cance at the 1% and 5% level respectively

Simulated mean realizable yields per trade (in €) with $d = ( 1 2 0 , 1 0 5 , . . . , 0 )$ and $\nu = ( 5 0 ,$ 100, …, 1000).

<table><tr><td rowspan="2">v in €.</td><td colspan="9">Delay level d in minutes</td></tr><tr><td>120</td><td>105</td><td>90</td><td>75</td><td>60</td><td>45</td><td>30</td><td>15</td><td>0</td></tr><tr><td>50</td><td>-3.76</td><td>-3.71</td><td>-3.44</td><td>-3.40</td><td>-3.42</td><td>-3.42</td><td>-3.46</td><td>-3.00</td><td>-1.22</td></tr><tr><td>100</td><td>-2.84</td><td>-2.75</td><td>-2.20</td><td>-2.12</td><td>-2.17</td><td>-2.17</td><td>-2.25</td><td>-1.33</td><td>2.23</td></tr><tr><td>150</td><td>-1.93</td><td>-1.78</td><td>-0.96</td><td>-0.84</td><td>-0.92</td><td>-0.91</td><td>-1.04</td><td>0.34</td><td>5.68</td></tr><tr><td>200</td><td>-1.01</td><td>-0.82</td><td>0.27</td><td>0.44</td><td>0.33</td><td>0.34</td><td>0.18</td><td>2.02</td><td>9.13</td></tr><tr><td>250</td><td>-0.10</td><td>0.15</td><td>1.51</td><td>1.71</td><td>1.59</td><td>1.59</td><td>1.39</td><td>3.69</td><td>12.58</td></tr><tr><td>300</td><td>0.82</td><td>1.11</td><td>2.75</td><td>2.99</td><td>2.84</td><td>2.85</td><td>2.60</td><td>5.36</td><td>16.03</td></tr><tr><td>350</td><td>1.73</td><td>2.07</td><td>3.98</td><td>4.27</td><td>4.09</td><td>4.10</td><td>3.82</td><td>7.04</td><td>19.49</td></tr><tr><td>400</td><td>2.65</td><td>3.04</td><td>5.22</td><td>5.55</td><td>5.34</td><td>5.36</td><td>5.03</td><td>8.71</td><td>22.94</td></tr><tr><td>450</td><td>3.56</td><td>4.00</td><td>6.46</td><td>6.83</td><td>6.60</td><td>6.61</td><td>6.24</td><td>10.38</td><td>26.39</td></tr><tr><td>500</td><td>4.48</td><td>4.97</td><td>7.69</td><td>8.10</td><td>7.85</td><td>7.86</td><td>7.45</td><td>12.06</td><td>29.84</td></tr><tr><td>550</td><td>5.39</td><td>5.93</td><td>8.93</td><td>9.38</td><td>9.10</td><td>9.12</td><td>8.67</td><td>13.73</td><td>33.29</td></tr><tr><td>600</td><td>6.31</td><td>6.89</td><td>10.17</td><td>10.66</td><td>10.35</td><td>10.37</td><td>9.88</td><td>15.40</td><td>36.75</td></tr><tr><td>650</td><td>7.22</td><td>7.86</td><td>11.40</td><td>11.94</td><td>11.61</td><td>11.63</td><td>11.09</td><td>17.08</td><td>40.20</td></tr><tr><td>700</td><td>8.14</td><td>8.82</td><td>12.64</td><td>13.22</td><td>12.86</td><td>12.88</td><td>12.31</td><td>18.75</td><td>43.65</td></tr><tr><td>750</td><td>9.05</td><td>9.79</td><td>13.88</td><td>14.49</td><td>14.11</td><td>14.13</td><td>13.52</td><td>20.42</td><td>47.10</td></tr><tr><td>800</td><td>9.97</td><td>10.75</td><td>15.12</td><td>15.77</td><td>15.36</td><td>15.39</td><td>14.73</td><td>22.10</td><td>50.55</td></tr><tr><td>850</td><td>10.88</td><td>11.71</td><td>16.35</td><td>17.05</td><td>16.62</td><td>16.64</td><td>15.94</td><td>23.77</td><td>54.00</td></tr><tr><td>900</td><td>11.80</td><td>12.68</td><td>17.59</td><td>18.33</td><td>17.87</td><td>17.90</td><td>17.16</td><td>25.44</td><td>57.46</td></tr><tr><td>950</td><td>12.72</td><td>13.64</td><td>18.83</td><td>19.61</td><td>19.12</td><td>19.15</td><td>18.37</td><td>27.12</td><td>60.91</td></tr><tr><td>1000</td><td>13.63</td><td>14.61</td><td>20.06</td><td>20.88</td><td>20.37</td><td>20.40</td><td>19.58</td><td>28.79</td><td>64.36</td></tr></table>

delay levels) is larger than zero. Table 5 gives means of the paired difference and the test results for the paired t-tests.

The results presented in Table 5 con<sup>fi</sup>rm that shorter delay levels (from two hours following the announcement until a prompt reaction without any delay) allow higher realizable returns at different level of signi<sup>fi</sup>cance.

Therefore, we are able to corroborate H1 that the decrease of the investors' reaction time provided by the proposed IT artifact enables investors to perform transactions that are more pro<sup>fi</sup>table on average. In order to prevent an investor from reacting to an event with a delay when the market price has already fully adjusted, the artifact provides functionalities being based on the price effect duration forecasting model. This includes the forecasted price effect duration which can be provided to the investor and the calculation of expiration dates for messages delivered.

The second evaluation hypothesis H2 is addressed on the basis of the two $| \mathsf { R } _ { d } |$ populations that were generated by the simulation on the basis of sub-samples ss1 and ss2. An appropriate statistical hypothesis test procedure tests whether or not the mean of $\left| \mathsf { R } _ { d } \right|$ populations simulated on the basis of sub-sample ss2 (relevant events) is signi<sup>fi</sup>cantly larger than the $| \mathsf { R } _ { d } |$ mean simulated on the basis of sub-sample ss1. Therefore, a corresponding statistical test procedure is chosen that works with different population sizes and without the underlying assumption of equal population variances $s ^ { 2 } .$ For that reason, unequal variances t-test has been chosen as an appropriate test procedure [63]. The |R | population means for both sub-samples and <sup>fi</sup>nally, unequal variances t-test results are given by Table 6 for each delay level d.

The test results provide evidence that those events of sub-sample ss2 (identi<sup>fi</sup>ed as relevant by the system) result in signi<sup>fi</sup>cant higher realizable returns compared to sub-sample ss1 (all events of the testing set). These results corroborate evaluation hypothesis H2 that a concentration on those events identi<sup>fi</sup>ed by the MoFiN DSS IT artifact leads to transactions being signi<sup>fi</sup>cantly more pro<sup>fi</sup>table on average. This result holds for all delay levels d on high levels of signi<sup>fi</sup>cance, which underpins the <sup>fi</sup>ndings.

After statistically proving the relative advantages of the MoFiN DSS IT artifact on the basis of the simulated realizable return values, we explore these advantages on a quantitative monetary basis and by simulating a matrix of mean realizable yields. Taken possible trading behavior (i.e. different delay levels and trading volumes) and realistic trading costs into account, the mean realizable yields matrix illustrates the increase of realizable trading pro<sup>fi</sup>ts an investor can achieve when being supported with the MoFiN DSS IT artifact. This <sup>fi</sup>nding is illustrated in Table 7 providing an overview of the matrix values.

The cells in Table 7 can be interpreted easily, as they directly monetarily quantify average bene<sup>fi</sup>ts when focusing on events that were identi<sup>fi</sup>ed as relevant only. Here, at a delay level of for example 15 min subsequent to the event date and a trading volume of 1000 € leads to 28.79 € higher pro<sup>fi</sup>ts on average, i.e. more than 2.8% higher pro<sup>fi</sup>ts that can be realized on an event day. Due to trading costs involved, these bene<sup>fi</sup>ts decrease with lower trading volumes and consistently, there exits trading volumes for which the bene<sup>fi</sup>ts can not compensate trading costs. These trading combinations are highlighted in the upper left-hand table cells of Table 7 and in the left-hand area of the mountain chart in Fig. 5, which illustrates the empirical <sup>fi</sup>ndings.

The simulations results provide evidence that investors being supported by our IT artifact are enabled to focus on those events that make a relatively higher impact on stock prices than others. Therefore, individual investors being supported accordingly should be empowered to perform intraday transactions that are more pro<sup>fi</sup>table while reducing the number of unpro<sup>fi</sup>table transactions performed, where trading costs lie above the pro<sup>fi</sup>ts that can be realized on the event date. Therefore, the evaluation results demonstrated the window of opportunity the IT artifact opens up to its users.

![](/api/attachments/B9RM62W4/fulltext/images/4584592365325a0e7415ee28e315aff146ac0db93807b39ce8ee488127b6a19c.jpg)  
Fig. 5. Simulated mean realizable yields per trade (in €) with $d = ( 0 , 1 5 , . . . , 1 2 0 )$ and $\boldsymbol { \nu } = ( 5 0 , 1 0 0 , . . . , 1 0 0 0 )$

The evaluation has provided the basis for exploring the utility provided by the designed IT artifact — a central goal of design science research [58]. For this evaluation, we have de<sup>fi</sup>ned and developed novel validation criteria, evaluation metrics and a simulation-based evaluation methodology. All these contributions represent additions to the IS knowledge base since they add to the IS methodologies pool [21].

## 5. Summary and conclusion

In this paper, we developed an ITartifact (MoFiN DSS) that represents a prototype decision support system, which aims at providing timecritical information via wireless communication channels. Following a design science research approach, the developed IT artifact comprises hard- and software-components that together provide the functionalities required.

The motivation for this research has been derived from behavioral <sup>fi</sup>nance research, which provides insights into the details how individual investors react to new information being published during the day. The empirical observations provide evidence that such information effects the trading of individual investors more signi<sup>fi</sup>cantly than those of institutional ones in terms of trading volume impact. But at the same time, these studies reveal that the individual investors react signi<sup>fi</sup>cantly slower compared to their institutional counterparts. However, intraday event studies show that capital markets react promptly to new information available and that observable excess returns decrease signi<sup>fi</sup>cantly with time elapsed. Therefore, our prototype DSS addresses this discrepancy by providing location-independent information supply and decision support via mobile communication services as a step towards ubiquitous information supply for individual investors. Since this user group is not able to continuously observe diverse news services, MoFiN DSS monitors news feeds and assesses the relevance of any news being published in the course of a day. This assessment is based on forecasting models we have developed on the basis on a dataset that includes 425 company announcements and voluminous intraday price series of the stocks being affected. Our system design picks up current behavior and challenges that individual investors face today in order to enable them to (1) react quicker to the information they are currently reacting to and to (2) concentrate on those announcements for which most signi<sup>fi</sup>cant market reactions can be expected. Furthermore, by identifying these relevant events, the system is capable of keeping the level of intrusiveness to a dimension manageable. Since rigorous design science research should address the utility provided by the designed artifact, we empirically investigated the IT business value it provides by a novel simulation-based evaluation approach and evaluation metrics that address consumers' value. The simulation results provide evidence that individual investors being supported with MoFiN DSS can realize higher trading success on average given their current trading strategies.

The main research contributions of this work can be summarized as follows:

• Literature review of neighboring disciplines' research: The literature review of current <sup>fi</sup>nancial research output including behavioral <sup>fi</sup>nance and event study research, we have identi<sup>fi</sup>ed a research problem <sup>fi</sup>eld to which information systems and in particular decision support system research can provide an important contribution. Both, consumers and suppliers can gain from corresponding research that provides the basis for better investment decisions and the offering of novel information products. The <sup>fi</sup>ndings provide an important contribution to the relevance of the research objective presented.

• Forecasting models: In Section 2, the presented forecasting models assist investors to decide for which of the company announcements being published during the course of the day signi<sup>fi</sup>cant abnormal stock price behavior can be expected in the following. The forecasting models provide the functional basis for the developed IT artifact that should enable investors to concentrate on the most relevant events (in terms of their impact on the capital market) and to disregard outdated ones (where the stock prices already re<sup>fl</sup>ect the new information).

• Development of an IT artifact: The implemented MoFiN DSS IT artifact comprises hard- and software components that aim at improving the information supply for individual investors. On the basis of the developed forecasting models and the installed infrastructure setup, the IT artifact aims at supporting individual investors in typical situations where timely and selected information supply is essential. The designed ITartifact is an important research contribution of design science research output because foundational IT artifacts contribute to the IS knowledge base. It can, for example, provide the necessary input for future behavioral science research addressing the impact of better information supply on the investors' behavior.

• IT business value evaluation: The simulation-based evaluation methodology provides the basis for an ex ante evaluation of the designed IT artifact. In contrast to other traditional evaluation approaches were, it can be used for quantitatively assessing customers' value on product level for novel products and services, for which other empirical data such as a productivity or pro<sup>fi</sup>tability measures are not available yet. The developed evaluation methodology including the de<sup>fi</sup>ned evaluation metrics represent typical design science research contributions [21].

This study is conducted in the relatively new research domain of mobile CDSS and its underlying motivation has been derived interdisciplinary. Therefore, the limitations of this research provide the basis for a wide set of future research.

One limitation of this research addresses the forecasting models that have been developed in order to asses the impact of company announcements on stock prices. Although it has been demonstrated that they can provide signi<sup>fi</sup>cant value to investors, future research can explore forecasting models that include other event types (such as analyst reports) or forecasting methods (such as machine learning). The object-oriented design of MoFiN DSS is open to integrate new <sup>fi</sup>ndings this <sup>fi</sup>eld. In the future, we will focus on this and will set up an even more voluminous database. Furthermore, we will apply analysis methods from knowledge technologies.

The simulation-based evaluation approach provides a methodical basis for ex ante evaluations of newly created IT artifacts like MoFiN DSS. However, behavioral science oriented research that incorporate user feedback and usage patterns and its context also remains a topic of future research. Anytime and anywhere access to <sup>fi</sup>nancial information affords opportunities but at the same time it involves risks such as privacy breaches or security threats.

Furthermore, only explicit transaction costs are currently considered. Further non-transparent transaction cost components, such as market impact, delay costs, spreads and opportunity costs, are subject to further research.

These further research questions and directions show that research in CDSS in this <sup>fi</sup>eld is far from settled and that more interdisciplinary is needed. This also includes the different research paradigms such as behavioral and design science.

## References

[1] S. Alter,18 Reasons why IT-reliant work systems should replace “the ITartifact” as the core subject matter of the IS <sup>fi</sup>eld, Communications of the AIS 12 (23) (2003) 365–394.

[2] E. Aktas, Intraday stock returns and performance of a simple market model, Applied Financial Economics 18 (18) (2008) 1475–1480.

[3] Y.A. Au, Design science I: the role of design science in electronic commerce research, Communications of the AIS 7 (1) (2001).

[4] B.M. Barber. T. Odean. All that glitters: the effect of attention and news on the buving behavior of individual and institutional investors Review of Financial Studies 21 (2) (2008) 785–818

[5] B.M. Barber, T. Odean, Online investors: do the slow die <sup>fi</sup>rst? Review of Financial Studies 15 (2) (2002) 455–487.

[6] M.J. Barclay, R.H. Litzenberger, Announcement effects of new equity issues and the use of intraday price data, Journal of Financial Economics 21 (1) (1988) 71–99.

[7] R.C. Basole, R.O. Chao, Location-based mobile decision support systems and their effect on user performance, in: C. Bullen, E. Stohr (Eds.), Proceedings of the 10th American Conference on Information Systems, AIS, New York, NY, USA, 2004, pp. 2870–2874.

[8] N. Bhattacharya, Investors' trade size and trading responses around earnings announcements: an empirical investigation, Accounting Review 76 (2) (2001) 221–244.

[9] S.J. Brown, J.B. Warner, Measuring security price performance, Journal of Financial Economics 8 (3) (1980) 205–258.

[10] E. Brynjolfsson, Y. Hu, M.D. Smith, Consumer surplus in the digital economy: estimating the value of increased product variety at online booksellers, Management Science 49 (11) (2003) 1580–1596.

[11] M.E. Carter, B.S. Soo, The relevance of form 8-K reports, Journal of Accounting Research 37 (1) (1999) 119–132.

[12] A. Chowdhury, Information technology and productivity payoff in the banking industry: evidence from the emerging markets, Journal of International Development 15 (6) (2003) 693–708.

[13] Comdirect Bank, Preis- und Leistungsverzeichnis, http://www.comdirect.de static/pdf/corp0099.pdf, (01.04.2005).

[14] D.B. Crane, Z. Bodie, Form follows function: the transformation of banking, Harvard Business Review 74 (2) (1996) 109–117.

[15] M.J. Davern, R.J. Kauffman, Discovering potential and realizing value from information technology investments, Journal of Management Information Systems 16 (4) (2000) 121–143.

[16] M.K. Dey, B. Radhakrishna, Who trades around earnings announcements? Evidence from TORQ data, Journal of Business Finance und Accounting 34 (1–2) (2007) 269–291.

[17] E.F. Fama, L. Fisher, M.C. Jensen, R. Roll, The adjustment of stock prices to new information, International Economic Review 10 (1) (1969) 1–21.

[18] G.A. Gorry, M.S. Scott Morton, A framework for management information systems, Sloan Management Review 13 (1) (1971) 55–70.

[19] T.F. Gosnell, A.J. Keown, J.M. Pinkerton, The intraday speed of stock price adjustment to major dividend changes: bid–ask bounce and order <sup>fl</sup>ow imbalances, Journal of Banking & Finance 20 (2) (1996) 247–266.

[20] A. Herzberg, Payments and banking with mobile personal devices, Communications of the ACM 46 (5) (2003) 53–58.

[21] A.R. Hevner, S.T. March, J. Park, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[22] H.G. Heymann, R. Bloom, Decision Support Systems in Finance and Accounting, Quorum Books, New York, NY, USA, 1988.

[23] D. Hirshleifer, J.N. Myers, L.A. Myers and S.H. Teoh, Do individual investors drive post-earnings announcement drift? Direct evidence from personal trades, Working Paper (2003).

[24] L.M. Hitt, E. Brynjolfsson, Productivity, business pro<sup>fi</sup>tability, and consumer surplus: three different measures of information technology value, MIS Quarterly 20 (2) (1996) 121–142.

[25] C.P. Holland, A.G. Lockett, I.D. Blackman, The impact of globalisation and information technology on the strategy and pro<sup>fi</sup>tability of the banking industry, in: R.H. Sprague (Ed.), Proceedings of the 30th Hawaii International Conference on System Sciences, IEEE Computer Society, Los Alamitos, CA, USA, 1997, pp. 418–427.

[26] B. Howcroft, R. Hamilton, P. Hewer, Consumer attitude and the usage and adoption of home-based banking in the United Kingdom, International Journal of Bank Marketing 20 (3) (2002) 111–121.

[27] S. Kanungo, S. Sharma, P.K. Jain, Evaluation of a decision support system for credit management decisions, Decision Support Systems 30 (4) (2001) 419–436.

[28] N. Kock, P. Gray, R. Hoving, H. Klein, M.D. Myers, J. Rockart, IS research relevance revisited: subtle accomplishment, unful<sup>fi</sup>lled promise, or serial hypocrisy? Communications of the AIS 8 (23) (2002).

[29] M.S. Lee, P.J. McGoldrick, K.A. Keeling, J. Doherty, Using ZMET to explore barriers to the adoption of 3G mobile banking services, International Journal of Retail & Distribution Management 31 (6) (2003) 340–348.

[30] C.A. Looney, D. Chatterjee, Web-enabled transformation of the brokerage industry, Communications of the ACM 45 (8) (2002) 75–81.

[31] P. Luarn, H. Lin, Toward an understanding of the behavioral intention to use mobile banking, Computers in Human Behavior 21 (6) (2005) 873–891.

[32] N. Mallat, M. Rossi, V.K. Tuunainen, Mobile banking services, Communications of the ACM 47 (5) (2004) 42–46.

[33] S. March, A. Hevner, S. Ram, Research commentary: an agenda for information technology research in heterogeneous and distributed environments, Information Systems Research 11 (4) (2000) 327–341.

[34] S.T. March, G.F. Smith, Design and natural science research on information technology, Decision Support Systems 15 (4) (1995) 251–266.

[35] M.L. Markus, A. Majchrzak, L. Gasser, A design theory for systems that support emergent knowledge processes, MIS Quarterly 3 (26) (2002) 179–212.

[36] M.C. Martin, D.A. Bradbard, C. Peter, Customer decision support systems: online tools for consumer decision making, Journal of E-Business 1 (5) (2005).

[37] M. Mattila, Factors affecting the adoption of mobile banking services, Journal of Internet Banking and Commerce 8 (1) (2003).

[38] J.L. McKenney, R.O. Mason, D.G. Copeland, Bank of America: the crest and trough of technological leadership, MIS Quarterly 21 (3) (1997) 321–353.

[39] A. McWilliams, D. Siegel, Event studies in management research: theoretical and empirical issues, Academy of Management Journal 40 (3) (1997) 626–657.

[40] J. Muntermann, A. Güttler, Intraday stock price effects of ad hoc disclosures: the German case, Journal of International Financial Markets, Institutions and Money 17 (1) (2007) 1–24.

[41] J. Muntermann, H. Roßnagel, Security issues and capabilities of mobile brokerage services and infrastructures, Journal of Information System Security 2 (1) (2006) 27–43.

[42] C. Nehmzow, The internet will shake banking's medieval foundations, Journal of Internet Banking and Commerce 2 (2) (1997).

[43] E.W.T. Ngai, A. Gunasekaran, Mobile commerce: strategies, technologies, and applications, Decision Support Systems 43 (1) (2007) 1–2.

[44] E.W.T. Ngai, T.C.E. Cheng, S. Au, K. Lai, Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (1) (2007) 62–76.

[45] J.F. Nunamaker, M. Chen, T.D. Purdin, Systems development in information systems research, Journal of Management Information Systems 7 (3) (1991) 89–106.

[46] R.M. O'Keefe, T. McEachern, Web-based customer decision support systems, Communications of the ACM 41 (3) (1998) 71–78.

[47] W.J. Orlikowski, C.S. Iacono, Research commentary: desperately seeking the ‘IT’ in IT research — a call to theorizing the IT artifact, Information Systems Research 12 (2) (2001) 121–134.

[48] N. Padmanabhan, F. Burstein, L. Churilov, J. Wassertheil, B. Hornblower, N. Parker, A mobile emergency triage decision support system evaluation, in: R.H. Sprague (Ed.), Proceedings of the 36th Annual Hawaii International Conference on System Sciences, Computer Society Press, Los Alamitos, CA, USA, 2006, p. 96b

[49] D. Parsons, C.C. Gotlieb, M. Denny, Productivity and computers in Canadian banking, Journal of Productivity Analysis 4 (1) (1993) 95–113.

[50] J.M. Patell, M.A. Wolfson, The intraday speed of adjustment of stock prices to earnings and dividend announcements, Journal of Financial Economics 13 (2) (1984) 223–252.

[51] P.P. Peterson, Event studies: a review of issues and methodology, Quarterly Journal of Business and Economics 3 (28) (1989) 36–66.

[52] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Greenwood Publishing, Westport, CT, USA, 2002.

[53] D.J. Power, Specifying an expanded framework for classifying and describing decision support systems, Communications of the AIS 13 (2004) 158–166.

[54] F.C. Sainfort, D.H. Gustafson, K. Bosworth, R.P. Hawkins, Decision support systems effectiveness: conceptual framework and empirical evaluation, Organizational Behavior and Human Decision Processes 45 (2) (1990) 232–252.

[55] G. Shao, The diffusion of online banking: research trends from 1998 to 2006, Journal of Internet Banking and Commerce 12 (2) (2007) 1–13.

[56] S. Shen, S. Pittet, C. Milanesi, N. Ingelbrecht, T.J. Hart, K. Desai, T.H. Nguyen, M. Basso, Overview of Consumer Mobile Applications, Gartner Research, Stamford, CT, USA, 2006.

[57] J. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002) 111–126.

[58] H.A. Simon, The Sciences of the Arti<sup>fi</sup>cial, The MIT Press, Cambridge, MA, USA,1996.

[59] A. Srinivasan, S. March, C. Saunders, Information technology and organizational contexts: orienting our work along key dimensions, in: D. Avison, D. Galletta, J.I. DeGross (Eds.). Proceedings of the 26th International Conference on Information Systems, AIS, Las Vegas, NV, USA, 2005, pp. 991–1001.

[60] E. Turban, J.E. Aronson, T. Liang, Decision Support Systems and Intelligent Systems, Pearson Prentice Hall, Upper Saddle River, NJ, USA, 2005.

[61] N. van Veen, R. Reitsma, A. Carini, The European Mobile Landscape 2006: European Consumer Technology Adoption Study, Forrester Research, Cambridge, MA, USA, 2006.

[62] Y. Wang, Y. Wang, H. Lin, T. Tang, Determinants of user acceptance of internet banking: an empirical study, International Journal of Service Industry Management 14 (5) (2003) 501–519

[63] R.M. Weiers, Introduction to Business Statistics, Thomson Brooks/Cole, Belmont CA, USA, 2005.

![](/api/attachments/B9RM62W4/fulltext/images/932fea3244baade6a074dc8be31b3a743983bdcaaee9303b24952be6655a2917.jpg)  
Jan Muntermann is Assistant Professor of Information Systems and holds the E-Finance Lab endowed Chair of E-Finance and Securities Trading at Goethe-University Frankfurt. His research interests include design science, decision support systems and IT valuation, especially in the <sup>fi</sup>elds of E-Finance and Mobile Business. In these fields, he has published in journals and proceedings such as Journal of Electronic Commerce Research, Journal of International Financial Markets, Institutions and Money, Journal of Information System Security and ICIS. Jan holds a PhD from Frankfurt University and has been a Visiting Scholar at Microsoft Research (Cambridge) and London Business School
