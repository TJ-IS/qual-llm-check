---
otero_id: 5858
otero_key: "JXTHW8U6"
title: "Nonlinear time series analysis on the offer behaviors observed in an electricity market"
authors: "HyungSeon Oh; Robert J. Thomas"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.01.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Nonlinear time series analysis on the offer behaviors observed in an electricity market

HyungSeon Oh <sup>a,</sup>⁎, Robert J. Thomas

<sup>a</sup> Strategic Energy Analysis Center, National Renewable Energy Laboratory, Golden, CO 80401, United States

<sup>b</sup> School of Electrical and Computer Engineering, Cornell University, 428 Phillips Hall, Ithaca, NY 14853, United States

## a r t i c l e i n f o

Article history: Received 29 April 2009 Received in revised form 19 January 2010 Accepted 20 January 2010 Available online 25 January 2010

Keywords: Hurst exponent Nonlinear dynamics Chaos Offer behavior Locational marginal price (LMP)

## a b s t r a c t

In electricity markets where supply and demand drives the price for the purchase and sale of electricity, generating <sup>fi</sup>rms change capacity for various reasons including load level, policy, and varying market conditions. These types of <sup>fl</sup>uctuating production patterns can result in the reduction of market ef<sup>fi</sup>ciency. In an inef<sup>fi</sup>cient market, where the price for electricity exceeds marginal cost, the locational marginal price (LMP) is often used to measure market ef<sup>fi</sup>ciency. Stochastically driven changes in the market are captured by this approach, however, these random changes (frequently observed in ef<sup>fi</sup>cient markets as well) do not affect market ef<sup>fi</sup>ciency in the long run. Conversely, a slow, consistent change is not captured by the snapshot approach and affects the ef<sup>fi</sup>ciency signi<sup>fi</sup>cantly. Therefore, it is necessary to construct an algorithm that captures only consistent changes that truly affect market ef<sup>fi</sup>ciency. Fractal analysis can characterize a price behavior in the electricity markets because the price exhibits a self-similarity.<sup>1</sup> Once a system undergoes a change, the fractal dimension of the system re<sup>fl</sup>ects the change. In this paper, an approach using nonlinear time series analysis is proposed and tested on actual offer behavior observed in the electricity markets in the United States.

© 2010 Published by Elsevier B.V.

## 1. Introduction

Independent system operators (ISOs) monitor the electricity market using locational marginal pricing (LMP) in a snap-shot approach to provide them with a quick look at the market to determine market ef<sup>fi</sup>ciency [1,5,11,13,16,20,21]. Only when anomalous market behavior is observed do ISOs take further investigative action. Such an action may include examining the offers from the generators under investigation directly [2,8,12,17,26]. But, according to the Federal Energy Regulatory Commission (FERC) [25], an ef<sup>fi</sup>cient market review “…should include an evaluation of market prices of ISO/RTO-administered products (e.g. real-time and day-ahead markets, locational marginal prices, and ancillary services) and speci<sup>fi</sup>- cally determine the extent to which the prices re<sup>fl</sup>ect competitive outcomes…” This means that, in addition to LMP information, ISOs must also factor in correct and up-to-date information (i.e., fuel costs and current economic situations) in order to properly determine market ef<sup>fi</sup>ciency. If these factors are not considered in the decision to take further investigative action, market participants could claim that the information used by ISOs to assess the market was incorrect and thereby <sup>fl</sup>awed. Another problem associated with the snap-shot approach is that non-strategic withholding by generating <sup>fi</sup>rms can occur as a result of stochastic loads and market speculation and cause prices to spike [17]. These innocent stochastic price spikes, possibly due to errors in load forecasting or network constraints, are captured by the snap-shot approach and may falsely represent the state of the market. Furthermore, this real-time method cannot capture slowly varying offer behavior trends that may have occurred before the price spikes were observed. These are clearly shortcomings of this snapshot type approach. To properly monitor the electricity markets, a tool must be used that can monitor a slow, consistent change without being affected by sporadic, inconsistent activity.

Fig. 1 illustrates how a <sup>fi</sup>rm reacts to information transmitted through a price signal. The top graph in Fig. 1 shows data <sup>fl</sup>ow in an electricity market. Firms submit offers to ISOs based on information such as demand forecast and historical market clearing data. Then the ISOs collect the offers, clear the markets, and publish the results. The bottom graph in Fig. 2 illustrates the translation of the market operation in the framework of a signal processing. An observer sends an input signal to the system and receives an output signal (i.e., a <sup>fi</sup>rm submits offers and then receives market clearing results).

Auction and bidding strategies in game theory are closely related to the deregulated electricity market. In game theory, the most commonly discussed type of equilibrium for this market is Nash equilibrium [3,23]. However, game theory is not practical for such a complicated system as the deregulated electricity market because of the multi-dimensional strategic space and the uncertainty associated with the market. For a real market it is not even clear if the system moves toward any equilibrium state at all. Depending on the initial condition sensitivity, the system exhibits aperiodic behavior and its trajectory does not settle down to <sup>fi</sup>xed points, periodic orbits, or quasi-periodic orbits as time diverges. As a result, it is not possible to perform a long-term prediction. This type of behavior is called chaotic behavior [9,22], which is a term describing aperiodic, long-term behavior in a deterministic system.

![](/api/attachments/JXTHW8U6/fulltext/images/0fbb12db6e8582c19ed60060569d071e2b62ce2891328bf11072688cf90039b1.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/01d1e04fe37c219f460fa4f687d7c0b392f655005f7e35526fdcbfa5d199de16.jpg)  
Fig. 1. Electricity market as a signal processing where input and output signals are offer and dispatch result and demand forecast, respectively

![](/api/attachments/JXTHW8U6/fulltext/images/ca489769f18f6a67136b7f2fd364aebca0a722d21bca488708a8459f28eeea2a.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/7cb98e4475c16f96aae2146f2221c78cf6d4f55216f651a5a05d8bec2b3ace5a.jpg)  
Fig. 2. LMPs of various generators from New York independent system operator.

![](/api/attachments/JXTHW8U6/fulltext/images/70600d42ffececf3ad8473b9447d53e2471fdcb495e7dd76ff8b372367058c8e.jpg)  
Fig. 3. Schematic diagram showing how to calculate C(ε) for a <sup>fl</sup>ow. Some neighboring points lying on dynamically uncorrelated parts of the data exist for point A, but point B has only direct images and pre-images of B resulting in dimension of 1. To avoid the incorrect calculation of C(ε) for estimating dimension, all neighbors over time where |i−j| is less than $n _ { \mathrm { m i n } }$ need to be ignored.

Stock price trajectory is often modeled as chaotic behavior or “fractal” due to its self-similarity [19]. Self-similarity implies that every part of the object is a reduced version of the whole. A fractal exists in a non-integer dimensional space, and therefore, dimension is the minimum number of independent variables to describe a fractal. Two different fractals may have an identical value of dimension, but two fractals with different values of dimension are guaranteed to be different. In other words, the value of dimension serves as a signature of a change in the system state.

Deterministic chaos provides a striking explanation for irregular behavior and anomalies in systems that do not appear to be inherently stochastic [23]. The Hurst exponent is used for describing a stock market, but a <sup>fi</sup>lter process is necessary to reduce error as a result of various sources of error involved in the stock market [6]. The process can introduce bias to the stock price data. Similar to the stock market [19], the electricity market exhibits nonlinear behavior due to the highly apparent nonlinear relationship between offers submitted by suppliers and the market clearing price. Different from a stock market, electricity markets have highly ordered structure, and thus, no <sup>fi</sup>lter process is necessary for characterizing market based on the values of the parameters. Therefore, the value is not sensitive to the stochastic changes, which makes the value of dimension an ideal candidate for market monitoring.

Market clearing price is a good measure to use when analyzing a change in the market state. Fig. 2 shows several LMPs observed in the New York ISO over a one-month period during the summer of 2003 [15]. Due to the hot weather, demands for electricity increased causing generating <sup>fi</sup>rms to demand higher prices and realize higher pro<sup>fi</sup>ts. Consequently, market speculators changed their strategies early in the summer to take advantage of the upcoming changing state of the market. The locational marginal price is set by offers made by price setting <sup>fi</sup>rms, therefore, it is a good indicator of possible changes in strategies from <sup>fi</sup>rms located at a particular bus. Fig. 2 shows numerous relatively high price spikes for two different buses over a short period of time. Consequently, the market monitoring used by ISOs would detect abnormal offer behaviors for both buses, which in turn would call for further inspection. The average price of both buses during the summer almost doubled compared to those in early June, indicating changes in both buses during this time period. In this study, the dimension of LMP is proposed and tested for market monitoring.

Section 2 describes the theoretical background and develops a metric to test the behavior of market participants. The metric developed in Section 2 is applied to real-time LMP data from all of the deregulated electricity markets in the United States: NY ISO, PJM

![](/api/attachments/JXTHW8U6/fulltext/images/4d5b5a9d5d8fb40b8cdde29e8c31d2ff87b27d3d9a2908446b9661aa32c319b5.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/f1b55ff31e3ad42ba6c0c11303f15a265c38754b218d0b02ba97ca1e145a23b7.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/c4946a7677d6629f3063abe6b1a3bf4b3cc28ad0d41e881adaa29b1fc6459f30.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/e45eb9b8a13d86e497b734ae63ba918b2795a75906b8d6c22ab9389ca9832b19.jpg)  
Fig. 4. Correlation integral for the market clearing price data obtained from the simulation with 500 periods

ISO, NE ISO, Midwest ISO, and CA ISO, and the results are presented in Section 3. For CA ISO, the LMP's from the day-ahead market were used because the real-time prices were not available at this time. Section 4 presents the conclusions from this study.

## 2. Nonlinear time series analysis

As stated previously, self-similarity is a characteristic that describes a chaotic behavior or fractal; whereas, dimension is a signature of a change in the fractal. Various dimensions can be de<sup>fi</sup>ned for describing fractals [22]. In practical applications where the geometric object has to be reconstructed from a <sup>fi</sup>nite sample of data points with errors, correlation dimension is most widely used [22]. As a system evolves, one can obtain a set of many points $\{ x _ { i } , i { = } 1 , . . . , n \}$ on a phase space. The dimension of experimentally measured data can be evaluated with the knowledge of nonlinear dynamics. However, the measured quantity is not a phase space object, but a time series that is a sequence of scalar measurements of some quantity. In this study, the measurable scalar quantity used is the market clearing price and it is necessary to convert the observations into state vectors by reconstructing a phase space.

It is important that components in one vector must be statistically independent to each other. One way to solve this problem is through the method of delay [7]. Take for example a sequence of measurements $s _ { n } ; s _ { n } = s [ x ( n \Delta t ) ] + \delta _ { n }$ where $s _ { n }$ is nth observation with noise of $\delta _ { n }$ measured at every Δt. It allows a delay reconstruction to form an m dimensional vector r by using s; $r _ { n } { = } \left( s _ { n - ( m - 1 ) \nu } , s _ { n - ( m - 2 ) \nu } , . . . , s _ { n - \nu } , \right.$ $s _ { n } )$ where ν stands for number of samples in a reconstructed space. The term of delay time, τ, refers to the time difference in a number of samples between adjacent components of the delayed vectors. In general, the $\tt a t t r a c t o r ^ { 2 }$ formed by the vector $r _ { n } " s$ is equivalent to the attractor in the unknown space. In other words, the original system is on the vector $r _ { n } " s$ space if the embedded dimension,<sup>3</sup> m, is suf<sup>fi</sup>ciently large enough for components in one vector to be independent with each other [7]. The equivalency is guaranteed when m is larger than twice the number of the actual degrees of freedom $^ 4 d _ { \mathrm { e m } } > 2 \bar { d }$ where $d _ { \mathrm { e m } }$ stands for an embedded dimension. Therefore, embedded dimensionality is not a problem as long as the vectors are reconstructed in a dimension greater than twice the “true” attractor. Wolf et al. suggests estimating delay time and embedded dimension in the following way [24]:

![](/api/attachments/JXTHW8U6/fulltext/images/de02358f2cce9cdb26f8070429b80221a05c5807d8c919282fff0d1d5afc8d78.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/343379c5882d8dcd0602b837c79d2c09e34d5b4b6c79654a585718f83c23692b.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/d9492bfb821ac81ad264fffb350b904c098028ce6b595ce3055459766429bd0e.jpg)  
Fig. 5. Correlation dimension for various price data obtained from n-period simulation type of market participants. Change in the precision of demand forecast or other changes can be captured by statistical tools. Therefore, given the results of other analyses, it is possible to tell if the strategies of market participants have been changed

![](/api/attachments/JXTHW8U6/fulltext/images/04296db80dfe9ad35e8d9f551d1c31034fd927ba86b996fb71e5b0338b9db0c1.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/81fcb6cda0a0226a72d91eb8f86bc615dfdf9f54ebcdca2eeb2b9000abd8355c.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/c1c65544d57a4c1be07d354a18b71cd080d40f364166ba9a2decf8e119bca6e2.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/0efe63a83f8bb32fac85d2a962edffedb336f0d2c8a3e1aa6b847eb590736dbc.jpg)  
Fig. 6. The change in systems that agents York-Warbasse and Cornell faced during June 2003. While the system of Cornell did not change signi<sup>fi</sup>cantly, that of York-Warbasse evolved.

![](/api/attachments/JXTHW8U6/fulltext/images/98486cf7e2a3a3c06abe886513b3e49b802585e5ccd1acf177d9d1db42b5711d.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/6f3b43adcaa849f9868a0dc31fb97c69f200b4197fd934a23dc07cfacc883f21.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/0f7cda4f9a334caf982d1c7559092379d9737c23749a8ab413f188e819b977c1.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/3e6a8ca25b9d56786595848706f8388ef559c67738ccfa5cddd020a266b65d43.jpg)  
Fig. 7. The change in systems that agents FLUVANNA and ORCHARD faced in the PJM ISO during June 2009. While the system of ORCHARD did not change signi<sup>fi</sup>cantly, that of FLUVANNA evolved.

$$
m \times \tau = Q\tag{1}
$$

where Q stands for mean orbital period, which is the situation where the pairs entering the sum are not statistically independent (see Fig. 3).

A reasonable approach to choosing Q, is to look at where the time the autocorrelation function decays to 1/e [7]. In this study, correlation dimension<sup>5</sup> of a fractal can be evaluated by using the following equation:

$$
C (\varepsilon) \equiv \frac {2}{N (N - 1)} \sum_ {i = 1} ^ {N} \sum_ {j = i + n _ {\min}} ^ {N} H \left(\varepsilon - | | x _ {i} - x _ {j} |\right) \propto \varepsilon^ {d} \rightarrow d = \left[ \frac {\partial \log C (\varepsilon)}{\partial \log \varepsilon} \right]\tag{2}
$$

where ε is the distance variable in an ε-neighborhood used in $C ( \varepsilon ) ; n _ { \mathrm { m i n } }$ is the minimum number of measurement satisfying $n _ { \mathrm { m i n } } = t _ { \mathrm { m i n } } / \Delta t ;$ t<sub>min</sub> and Δt represent autocorrelation time and time delay of measurement, respectively.

![](/api/attachments/JXTHW8U6/fulltext/images/93974ee6486291523c215638f1f95336b038038e9a19582af05165fced3b30db.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/76a4b501775679829164a0d4c77bec7f66d31e84865dfc5fbb8d440af7a7a572.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/598315634f0e45d297c77c8efa9bae857bbd510b730d3f8b6aea54e09e437b72.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/da7087f2c356c5b7f5146f884ae40498d4372173da3253b90af8aa66cb33e910.jpg)  
Fig. 8. The change in systems that agents LDRIDGEFLD153XLD and LDPINEHRST132 faced in the New England ISO during June 2009. While the system of LDPINEHRST132 did not change signi<sup>fi</sup>cantly, that of LDRIDGEFLD153XLD evolved.

To evaluate the value of dimension d, C(ε) and ε is plotted in log–log scale for various embedded dimensions as shown in Fig. 4, and Eq. (2) is used. If Eq. (2) is valid over the entire range of ε, there should be a straight line of slope d. However, the power law only holds over an intermediate range of ε. The curve saturates at large ε because the balls with radius of ε surround the whole attractor and, therefore, the number of neighborhoods within ε cannot grow any further. On the other hand, the balls with extremely small radius ε contains x only and the power law holds only in the intermediate scaling region. Data that existed only in the intermediate region were chosen for evaluating dimension.

Fig. 5 illustrates fractal dimension obtained as a function of the embedded dimension and the true dimension was determined at approximately two. Therefore, an embedded dimension of <sup>fi</sup>ve should indicate a true dimension, but Fig. 5 shows that the true dimension at the embedded dimension is approximately two. The value of dimension depends on the accuracy of the demand forecast and other market conditions, such as the offer behavior of market participants. The change in demand can change the status of market, and as a result, the LMP changes.

A  
![](/api/attachments/JXTHW8U6/fulltext/images/51e6f0d2b55b524e11a084308ac0f8e369b9602b24fc3217c85ed4d6082d6552.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/262574914f59e4daaa1ed2317ba3500137c8c420d79400a5014aaa62328cf1b0.jpg)

B  
![](/api/attachments/JXTHW8U6/fulltext/images/a20c25366275f1f246ac3144f3ed5976b8fc43caa86fcf2cac14f3b155d5cfa2.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/a64c349156bacfcdf599325efec4a0306d007297c7736880840083786728eb7a.jpg)  
Fig. 9. The change in systems that agents WECDFTR13N1 and CONSALCONHYDR faced in the Midwest ISO during June 2009. While the system of CONSALCONHYDR did not change signi<sup>fi</sup>cantly, that of WECDFTR13N1 evolved.  
B  
A

## 3. Results and discussion

Fig. 2 shows LMP data obtained from the New York ISO [15]: York-Warbasse and Cornell. In the summer months, some <sup>fi</sup>rms changed their strategies to maximize their pro<sup>fi</sup>ts by increasing the market clearing price. This change in strategy should have consequently resulted in a change to the system dimension. As Fig. 6 shows, the value of the dimension at the York-Warbasse location changed during the period, but the Cornell location did not suggest that location could be a big factor in the dissimilar reactions to the same change.

York-Warbasse is located in New York City, which is a frequently congested area during the summer. When an area is congested and somewhat isolated from the rest of the system, it is often dif<sup>fi</sup>cult to <sup>fi</sup>nd another source of electric power. When <sup>fi</sup>rms face uncompetitive environments, the increase in price returns high pro<sup>fi</sup>ts. So, when <sup>fi</sup>rms near York-Warbasse changed their offer strategies during the summer months, the York-Warbasse location was faced with operating in an uncompetitive market. Whereas Cornell, which is in central New York and rarely experiences congestion, continued to operate in a competitive market. In a competitive market, increases in offer prices may result in a signi<sup>fi</sup>cantly high probability of not being dispatched. Therefore, it is rational for <sup>fi</sup>rms, such as Cornell, that operate in a competitive market not to increase their offers resulting in unchanged market conditions.

Based on the value of dimension suggested in this study, only York-Warbasse needs further inspection which differs greatly from what the results would be if a snap-shot approach was used. Additionally, the method described here also does not require that assumptions be made on fuel prices, which could prevent market participants from claiming inaccurate information was used in determining the outcome.

Figs. 7–10 illustrate the results of applying the nonlinear tool on the LMP data obtained from PJM ISO [18], NE ISO [14], Midwest ISO [10], and CA ISO [4], respectively. Because CA ISO does not provide the real-time pricing on its web site, the LMP data from the day-ahead market was used for this analysis. In general, the LMPs where the changes in the dimension were observed were higher than those where the dimension stayed unchanged.

![](/api/attachments/JXTHW8U6/fulltext/images/0da2a04f48d8c9f512392afae18847b3c3d10f278a4e6c0508fc63e513572dd4.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/e5ad20e0ab91ab5121f790a461ce4906efc3827586ef37abef81cf661a078747.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/aecef953a874ef5c7446cc77e8284717bdcf0859eab02801ebc4ca7e2ba1eac6.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/5f2203b1ef6f58bed563a7e53420175100040e6754ed47972e078794d5e0df9a.jpg)  
Fig. 10. The change in systems that agents COVEL06\_6\_N001 and BRRNDAA\_6\_N001 faced in the California ISO during June 2009. While the system of BRRNDAA\_6\_N001 did not change signi<sup>fi</sup>cantly, that of COVEL06\_6\_N001 evolved.

## 4. Conclusions

Market clearing price for electric power follows aperiodic procedure, which is a fractal. Dimension is a character that unequivocally identi<sup>fi</sup>es a fractal. The value of dimension is evaluated without any assumptions and the change in value of dimension is a signature of the change in state. The sets of data suggest this nonlinear dynamic method proposed in this paper can show the exercise of market power.

## References

[1] F. Alvarado, Controlling power systems with price signals, Journal of Decision Support System (2005) 495–504.

[2] A.G. Bakirtzis, N.P. Ziogos, A.C. Tellidou, G.A. Bakirtzis, Electricity producer offering strategies in day-ahead energy market with step-wise offers, IEEE T PES 22 (2007) 1804–1818.

[3] C.A. Berry, B.F. Hobbs, W.A. Meroney, R.P. O'Neill, W.R. Stewart, Analyzing strategic bidding behavior in transmission networks, Game Theory Application in Electricity Markets, 99TP-136-0, IEEE PES Winter Meeting, 1999, pp. 7–32.

[4] California ISO, Locational Marginal Prices (LMP), DAM Available from http://oasis. caiso.com/mrtu-oasis/?doframe=true&serverurl=http%3a%2f%2ffrptp09%2eoa% 2ecaiso%2ecom%3a8000&volume=0ASIS

[5] California ISO, Market Monitoring Overview, 2005 Available from http://www. caiso.com/docs/2005/10/17/2005101719583822310.html.

[6] H.E. Hurst, Long-term storage of reservoirs, Transactions of the American Society of Civil Engineers (1951) 116.

[7] H. Kantz, T. Schreiber, Nonlinear Time Series Analysis, Cambridge Univ. Press, Cambridge, 1999.

[8] D.-N. Liu, Y.-G. Wu, X.-L. Jiang, G.-Y. He, H.-Q. Zhang, Key performance indices to monitor bidding behaviors in electricity market. Power Systems Conference and Exposition, 2006, pp. 1156–1161.

[9] E.N. Lorenz, Deterministic nonperiodic <sup>fl</sup>ow, Journal of Atmospheric Sciences 20 (1963) 130.

[10] Midwest ISO, Real-Time LMPs, 2009 Available from http://www.midwestmarket. org/home/Market%20Reports/index.php?type=rt\_lmp&theMonth=200906.

[11] T. Mount, Market power and price volatility in restructured markets for electricity Journal of Decision Support System (2001) 311–325.

[12] T. Mount, H.-N. Oh, On the First Price Spike in Summer, Proc. of 37th Annual Hawaiian International Conference on System Science (HICSS), 2004.

[13] New England ISO, Market Monitoring Reports and Presentations, Available from http://www.iso-ne.com/markets/mktmonmit/rpts/index.html

[14] New England ISO, Historical Data, Available from http://www.iso-ne.com/ markets/hst\_rpts/hstRpts.do?category=Hourly.

[15] New York ISO, Market Data Exchange, Available from http://www.nyiso.com public/market\_data/pricing\_data.jsp.

[16] New York ISO, Market Monitoring, Market Monitoring Policies, Available from http://www.nyiso.com/public/services/market\_monitoring/policies.jsp

[17] H. Oh, R.J. Thomas, B.C. Leiseutre, T.D. Mount, A method for classifying offer strategies observed in an electricity market, Journal of Decision Support System (2004) 449–460.

[18] Pennsylvania-New Jersey-Maryland ISO, Daily Real-Time LMP Files, Available from http://www.isomou.com/markets-and-operations/energy/real-time/lmp.aspx.

[19] E. Peter, Chaos and Order in the Capital Markets A New View of Cycles, Prices, and Market Volatility John Wiley & Sons Inc, New York, 1991

[20] PJM Market Monitoring Unit, Activities of Market Monitoring Unit 2006, Available from http://www.pjm.com/markets/market-monitor/downloads/mmureports/20070122-mmu-activities-report pdf

[21] Potomac Economics, 2007 State of the Market Report for the Midwest ISO, Available from. http://www.midwestmarket.org/publish/Document/24743- f\_11ad9f8f05b\_-7b890a48324a/2007%20MISO%20SOM%20Report\_Final%20Text. pdf?action=download&\_property=Attachment.

[22] S.H. Strogatz, Nonlinear Dynamics and Chaos, Westerview, Cambridge, 2000.

[23] J.D. Weber, T.J. Overbye, A two-level optimization problem for analysis of market bidding strategies, Power Engineering Society Summer Meeting, IEEE, vol. 2, 1999, pp. 682–687.

[24] A. Wolf, J.B. Swift, H.L. Swinney, J.A. Vastano, Determining Lyapunov exponents from a time series Physica 16D (1985) 285-317.

[25] P. Wood, N.M. Brownell, J.T. Kelliheer, S.G. Kelly, Policy Statement on Market Monitoring Units, Docket No. PL05-1-000, 2005.

[26] Z. Yang, Y. Song, R. Cao, G. Tang, Analysis on bidding strategy of power provider by game theory, Power System Technology (2006) 22–26.

![](/api/attachments/JXTHW8U6/fulltext/images/64d95e7ce73fc0cafcd209a1ce417a6ad443f7f2fb02e284ccadde5bccb4d80e.jpg)

![](/api/attachments/JXTHW8U6/fulltext/images/06c11a1d95d4bc8100dec5d8707f40948fe32459e16823076a1d985f945c4054.jpg)

HyungSeon Oh is an engineer at the National Renewable Energy Laboratory. He received his Ph.D. in electrical and computer engineering from Cornell University in 2005 and specializes in power system planning, renewable energy, smart grids, storage devices, computer simulation and nonlinear dynamics.

Robert J. Thomas currently holds the position of Professor Emeritus of Electrical and Computer Engineering at Cornell University. He has had assignments with the U.S. Department of Energy Of<sup>fi</sup>ce of Electric Energy Systems (EES) in Washington, DC and the National Science Foundation as the <sup>fi</sup>rst Program Director for the Power Systems Program in the Engineering Directorate's Division of Electrical Systems Engineering (ESE). He is the author of over 100 technical papers, and two book chapters. He has been a member of the IEEE United States Activity Board's Energy Policy Committee since 1991 and was the committee's Chair from 1997 to 1998. He was a member of the IEEE Technology Policy Council, has served as the IEEE-USA Vice President for Technology Policy,

and has been a member of several university, government and industry advisory Boards or Panels. He has published in the areas of transient control and voltage collapse problems as well as technical, economic and institutional impacts of restructuring. He is the founding Director of the 13 university member National Science Foundation Center, PSerc (Power Systems Engineering Research Center). He is currently an Advisor to the DOE Assistant Secretary for Electricity Delivery and Energy Reliability and he currently serves as one of 30 inaugural members of the U.S. Department of Energy Secretary’s Electricity Advisory Committee (EAC). He has received 5 teaching awards and the IEEE Centennial and Millennium medals. He is a member of Tau Beta Pi, Eta Kappa Nu, Sigma Xi, ASEE and a Life Fellow of the IEEE.
