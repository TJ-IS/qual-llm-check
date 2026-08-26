---
otero_id: 5870
otero_key: "96JCKUGB"
title: "Location and time do matter: A long tail study of website requests"
authors: "Chetan Kumar; John B. Norris; Yi Sun"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.04.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Location and time do matter: A long tail study of website requests

Chetan Kumar <sup>a,</sup>⁎, John B. Norris <sup>b</sup>, Yi Sun <sup>a</sup>

<sup>a</sup> Department of Information Systems and Operations Management, College of Business Administration, California State University San Marcos 333 South Twin Oaks Valley Road, San Marcos, CA 92096, United States

<sup>b</sup> Krannert School of Management, Purdue University, 403 West State Street, West Lafayette, IN 47907, United States

## a r t i c l e i n f o

Article history: Received 16 October 2008 Received in revised form 15 April 2009 Accepted 17 April 2009 Available online 3 May 2009

Keywords: Website visitations Long tail model Request heterogeneity User location Time of access

## a b s t r a c t

There has been a tremendous growth in the amount and range of information available on the Internet. The users' requests for online information can be captured by a long tail model. A few popular websites enjoy a high number of visitations while the majority of the rest are less frequently requested. In this study we use real world data to investigate this phenomenon and show that both users' physical location and time of access affect the heterogeneity of website requests. The effect can partially be explained by differences in demographic characteristics at locations and diverse user browsing behavior in weekdays and weekends. These results can be used to design better online marketing strategies, af<sup>fi</sup>liate advertising models, and Internet caching algorithms with sensitivities to user location and time of access differences.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

There has been a tremendous growth in the amount and range of information available on the Internet. Cisco Systems report [10] forecasts that global Internet Protocol (IP) traf<sup>fi</sup>c will increase six folds between 2007 and 2012, from fewer than 7 exabytes per month in 2007 to 44 exabytes per month in 2012. ComScore Inc. [12] estimates that total global Internet users have surpassed 1 billion visitors in December 2008. The increase in Internet traf<sup>fi</sup>c is aided because making information available online is becoming relatively inexpensive, and as more people have Internet access demand for information increases. In addition, new format and content of Web 2.0 technologies such as video, social networking and collaboration applications prompted more interest in online deliveries. The trend of increasing Internet traf<sup>fi</sup>c is likely to continue [10,13].

The visitation of users to websites or online product purchase can be captured by a long tail model coined by Chris Anderson [2], shown in Fig. 1. Anderson [2] used this model to explain the success of Amazon book and Net<sup>fl</sup>ix DVD rental recommendations system to promote obscure products. Brynjolfsson et al. [7] had earlier noted this effect due to lower search costs in the digital economy. A few popular websites enjoy a high number of visitations. Interestingly there are also a large number of infrequently requested websites. The former is shown by the steep end of the curve, while the latter forms the tapering long tail.

Before the Internet age economic scale favored services that catered to a large amount of customers. For example, books that potentially attract more readers will be more likely published than those targeting niche markets [2]. However the inexpensive online medium and reduced intermediaries lowered the hurdle of entrance. Websites with potentially small audiences can also exist because of relatively inexpensive hosting costs for the information service provider. All sorts of information has a more equal chance to be present on the Internet and, with the assistance of ef<sup>fi</sup>cient search engines such as Google, to be found by users. In this study we investigate this phenomenon by using real world data and show how users' location and time of access (weekdays versus weekends) affects this long tail model.

Our results can be used to design better online marketing strategies, af<sup>fi</sup>liate advertising models, and Internet caching algorithms. According to Interactive Advertising Bureau Internet ad revenues grew to \$21 billion in 2007, up 25% over 2006. However as online advertising is still only 10% of all US ad spending it has considerable room to grow [3]. Internet based marketing, advertising, and content delivery is becoming increasingly important for businesses and institutions. Understanding patterns in user request behavior can provide guidelines for customizing advertising pricing for Internet portals such as Yahoo and Google. In addition they can be exploited for Internet caching algorithms to reduce user delays on the Internet. Therefore we believe this study contributes to an important area for Information Systems research.

The rest of this paper is organized as follows. We <sup>fi</sup>rst discuss literature related to online visitation and marketing, followed by a description of methodology of analysis. Next we present the model and data analysis. Finally we conclude with discussion and areas for future research.

![](/api/attachments/96JCKUGB/fulltext/images/3f890441d30aa7191b175faebbd1831a4ddb71442b931013f3887d05ba1573e5.jpg)  
Fig. 1. Long tail model (adapted from: http://en.wikipedia.org/wiki/The\_Long\_Tail).

## 2. Related literature and methodology

## 2.1. Literature review

Researchers have long been interested in client-side study of human behavior in the context of the Internet. Some focused on the demographics attributes of Internet users and how these attributes affect users' browsing behavior [19]. Hu et al. [17] suggested a model to predict users' gender and age from their web browsing behavior. Others studied the way that users navigate the Internet [9]. Tauscher and Greenberg [29] and Cockburn et al. [11] demonstrated that the probability of revisitation of a website is very high. Deborah [14] studied Internet searching habits and suggested that many users only use one or two search engines most of the time. Sen et al. [28] investigated the determinants of online search strategies and found that buyers' attitudes toward the price, their perception of online price dispersion, and their awareness of shopping agents affected their choice of online search strategy signi<sup>fi</sup>cantly. Breslau et al. [6], Almeida et al. [1l and Glassman [16], among others, modeled online visitations using the classical Zipf distribution [33] that relates object reques frequency to rank. In his in<sup>fl</sup>uential study Zipf [33] demonstrated an empirical law, that given some corpus of natural language such as English, the frequency of word occurrence is approximately inversely proportional to its rank in the frequency table. For example, in English “the” is the most frequently occurring word with about 7% of all occurrences. Following the Zipf distribution “of." which is the second ranked word, occurs about 3.5% of the time. More details of the Zipf distribution are provided in model and data analysis Section 3. Zipf [33] is among the set of power law distributions such as the well known Pareto distribution [25] which characterizes the “80–20”" rule where 20% of the population controls 80% of the wealth. Brynjolfsson et al. [8] have shown that Pareto distribution can be modi<sup>fi</sup>ed with regard to concentration of product sales on the Internet due to effect of search costs. Along these lines in our study we <sup>fi</sup>rst empirically demonstrate the long tail of website requests using the Zipf distribution [33]. Our study then goes beyond previous online visitation studies by focusing on the differences in user browsing behavior due to differing geographical locations and time of access. There are several reasons to warrant the study. Users from different areas have different demographic characteristics For example in certain regions in the United States (US) there are higher percentages of immigrant residents or high-skilled workers. Residents in these locations tend to have more diversi<sup>fi</sup>ed interests and the differences may exhibit in diversi<sup>fi</sup>ed visitations for online information. We also expect that time of access has an effect on diversity of website requests. For example, users may have different browsing behavior on weekdays versus weekends.

This knowledge can help business managers design better marketing strategies to allocate website advertising budget given observed patterns in user request behavior. It can also provide guidelines for customizing advertising pricing or af<sup>fi</sup>liate marketing models for Internet portals such as Yahoo and Google. There is growing interest in research on online marketing and content customization. Brynjolfsson et al. [8] compared Internet buying habits to of<sup>fl</sup>ine catalog purchases. Baye et al. [4] propose a model for pricing products and advertisements online. Sen [27] investigated the differences of search engine optimization and paid placements and proposed models that describe sellers' choice based on cost and consistence of rankings. Business community and academic researchers have also recognized the importance of customizing online content and marketing strategy based on users' preferences and their demographic attributes. Since total Internet advertising revenues is still only 10% of all US ad spending, it has considerable growth potential [3]. A signi<sup>fi</sup>cant area for improvement for Internet advertising is in customizing content to users. Luo and Seyedian [24] discuss the importance of contextual marketing in ecommerce based on different interests of users. Venkatesh and Agarwal [31] show how usability of website improves online purchase rate, and Bhatnagar and Papatla [5] demonstrate the bene<sup>fi</sup>ts of customizing online advertising according to user pro<sup>fi</sup>le. We expect that the result of our research can enhance current online marketing research.

Furthermore we can use the knowledge to develop more effective caching algorithms. Caching involves storing copies of objects in locations that are relatively close to the user thereby reducing access delays [13,21]. Popular caching algorithms include least recently used (LRU), least frequently used (LFU), and their numerous variations [13,26,32]. However, most existing caching mechanisms do not consider location or time of access differences of the end user. Our results may help develop caching methods with priority given to users' locations and their time of access to further reduce user delays.

## 2.2. Methodology and hypotheses

In this study we conduct an empirical investigation on the long tail characteristics of website requests at different proxy server locations and times of access. We use web trace data from the IRCache network that maintains proxy servers at nine cities in the US (www.ircache. net). Using this data our <sup>fi</sup>rst objective is to con<sup>fi</sup>rm the overall validity of using Zipf distribution to study long tail effects of online visitations. As discussed by Anderson [2], the adoption of the Internet as a distribution channel has lead to the existence of a long tail in infrequently requested goods and services in the digital medium. Past studies have used Zipf distribution to show relationship of web object rank to request frequency [1,6,16]. Our goal is to empirically demonstrate presence of the long tail effect of a large number of infrequently requested websites in addition to few very popular ones, using the Zipf distribution. Factors that contribute to presence of the long tail include reduced costs of hosting web content and the improved ability to search for niche information online [2,8].

Hypothesis 1. Long tail of website requests. There exists a long tail of large number of infrequently requested websites in addition to a few very popular websites.

We now consider differences in diversity of websites requests due to user's geographical location and time of access. This allows us to go beyond earlier studies by analyzing differences in long tail characteristics due to these two factors. The differences are measured by statistically testing variations in website request diversity. To examine location differences we focus on representative IRCache servers present in the four time zones of continental US: Silicon Valley at NASA Ames Research Center, California (Paci<sup>fi</sup>c time); Boulder, Colorado (Mountain time); Urbana-Champaign, Illinois (Central time); and New York, New York (Eastern time). We then perform statistical tests to con<sup>fi</sup>rm differences in website request heterogeneity across different locations. User location is an important factor to consider because different geographical areas in the US have varying demographic pro<sup>fi</sup>les [30]. This may result in differences in diversity of website requests at different locations.

Hypothesis 2. User location and diversity of website requests. The user's geographical location has an effect on the diversity of website requests.

Next we consider effect of time of access on diversity of website requests across locations. For this we partition the requests between weekdays and weekends. We then statistically test for differences in request behavior during weekdays and weekends at each location. We are interested to observe if users request diversi<sup>fi</sup>ed information sources at different times of access. At weekends users have more free time to explore personal interests and this may result in variations in website request behavior.

Hypothesis 3. User's time of access and diversity of website requests. The time of access of the user has an effect on the diversity of website requests at every location.

Note that we partition data between weekdays and weekends at each location in order to examine differences due to user time of access. Considering smaller time intervals such as hours or minutes at each location may result in a multicollinearity problem. This is because these two factors may be correlated and can contribute redundant information to the model [18]. For example, users' requests at different time intervals during a day may be affected by the demographic preferences at their locations' time zones. This effect is minimized if we partition data for each location only between weekday and weekend. In addition we avoid over counting differences in time of access by not pooling data from all locations. By determining user requests variations between weekdays and weekends online products and services may be accurately tailored to their preferences at those times. Alternative approaches that are focused at smaller time durations at one speci<sup>fi</sup>c time zone can later build on these results. In this study we expand on preliminary research of Kumar, Norris and Sun [22] by a comprehensive analysis of both location and time of access effects on website requests.

## 3. Model and data analysis

We use a variation of the classical Zipf distribution [33] to characterize the long tail behavior of website requests. Zipf's law in our setting may be stated as follows. The fraction of the time, f(R), that the Rth most popular website is requested is given by:

![](/api/attachments/96JCKUGB/fulltext/images/a60d0e1b7dcad0ae8333a81ebe5f9e0d314351a979d8a39e004adac3abeefc99.jpg)  
Fig. 2. Zipf distribution and characterizing exponent s.

Table 1 Log-linear regression for frequency of website requests onto rank of site for all servers and four locations.

<table><tr><td>Server locations</td><td> $\beta_0$ </td><td> $\beta_1$ </td><td> $R^2$ </td><td>M</td></tr><tr><td>All servers</td><td>18.333 (0.0031)</td><td>-1.365 (0.00024)</td><td>0.97</td><td>926,552</td></tr><tr><td>Silicon Valley</td><td>13.09279 (0.0051)</td><td>-1.131 (0.00046)</td><td>0.976</td><td>140,127</td></tr><tr><td>Boulder</td><td>14.973 (0.0048)</td><td>-1.276 (0.00043)</td><td>0.981</td><td>155,373</td></tr><tr><td>Urbana-Champaign</td><td>15.28 (0.0046)</td><td>-1.295 (0.00041)</td><td>0.983</td><td>159,879</td></tr><tr><td>New York</td><td>13.361 (0.0048)</td><td>-1.148 (0.00044)</td><td>0.978</td><td>145,306</td></tr></table>

The Standard Errors are in parentheses, M = total website requests.

$$
f (R) = \Omega / R ^ {s}\tag{1}
$$

where R is the rank of websites in terms of number of requests, s is the exponent characterizing the distribution, $\textstyle \Omega = 1 / { \left( \sum _ { n = 1 } ^ { N } 1 / n ^ { s } \right) }$ is a normalizing constant and N is the total number of requested websites. In his seminal study Zipf demonstrated that in the English language the frequency of word occurrence is approximately inversely proportional to its rank in the frequency table, with s value slightly greater than 1 [33]. Parameter s determines the relative impact that higher ranked objects have in the overall distribution as shown in Fig. 2. Note that the f(R) vs. rank R mapping captures the long tail behavior of relatively few sites being requested very frequently and a large number of infrequently requested websites. Some transformations allow us to connect and characterize both Zipf distribution and the long tail behavior using a log-linear model. Performing log transformation on Eq. (1) we obtain:

$$
\log [ f (R) ] = \log \Omega - s \log [ R ]\tag{2}
$$

Eq. (2) is analogous to <sup>fi</sup>tting a log-linear regression relationship between rank R of site and frequency of requests $f ( R )$ as follows:

$$
\ln [ f (R) ] = \beta_ {0} + \beta_ {1} \ln [ R ] + \varepsilon\tag{3}
$$

Parameter s of (2) is directly captured by coef<sup>fi</sup>cient $\beta _ { 1 }$ of $( 3 )$ , and s also indirectly contributes to logΩ and intercept $\beta _ { 0 }$ terms of the two expressions, respectively. The log-linear relationship (3) has been used successfully by economists to study distribution of income and wealth [23,25]. More recently Brynjolfsson et al. [8] have used it to show the effect of search costs on concentration of product sales. In our context $\beta _ { 0 }$ can be interpreted a measure of overall demand for unique websites at a server location, while $\beta _ { 1 }$ measures how quickly the share of total number of requests attributed to a particular website falls as site rank increases. A bene<sup>fi</sup>t of using expression (3) is that we can test if the differences in $\beta _ { 1 }$ for various locations or time periods are statistically signi<sup>fi</sup>cant.

## 3.1. Long tail of website requests (H1)

Our <sup>fi</sup>rst objective is to empirically demonstrate that there exists a long tail behavior of large number of infrequently requested websites in addition to a few very popular ones. For this we <sup>fi</sup>t a log-linear regression model for the comprehensive trace data of the IRCache network. The data was collected from 29 April to 30 June, 2004. It includes the URLs of requests, the request time, the format of object requested, unique identi<sup>fi</sup>ers for user IP address, and the elapsed times for serving requests. The comprehensive proxy trace of all nine IRCache server locations, referred as All Servers, includes 926,552 total website requests. Table 1 summarizes the regression results for All Servers, as well as for one IRCache location in each of the four US time zones: Silicon Valley (SV), Boulder (BO), Urbana-Champaign (UC), and New York (NY). The high $R ^ { 2 }$ value of 0.97 for All Servers indicates that there is a good <sup>fi</sup>t between frequency of website requests and rank of the websites. This is also demonstrated in Fig. 3 which shows a good linear <sup>fi</sup>t in a scatter plot between the two variables on a log–log scale. The approximate straight line in the <sup>fi</sup>gure, with slope $\beta _ { 1 } =$ −1.365, displays a Zipf distribution for frequency vs. rank for websites. This in turn con<sup>fi</sup>rms Hypothesis 1 that the long tail behavior for website requests does exist at proxy servers.

![](/api/attachments/96JCKUGB/fulltext/images/5c2fe8185a0070c463ba80383fe9feb50229bc63c00fb5d298e90853bcd2bd6c.jpg)  
Fig. 3. Frequency of requests vs. rank of sites for all servers.

The absolute value of $\dot { \rho } _ { 1 }$ coef<sup>fi</sup>cients corresponds to parameter s of the Zipf distribution. A smaller |β | indicates greater diversity in requests as websites with lower ranks retain a higher share of total requests. Conversely, larger $| \beta _ { 1 } |$ indicates more homogenous website requests with the most popular websites making up a higher proportion of total requests.

## 3.2. Effect of user location on diversity of website requests (H2)

Next we test if there are signi<sup>fi</sup>cant differences in the characteristics of websites requests depending on the locations of the proxy servers. Fig. 4 demonstrates that there is a good linear <sup>fi</sup>t for log (frequency of requests) vs. log(rank of sites) for the individual servers located in the four cities mentioned earlier. The high $R ^ { 2 }$ values of 0.976, 0.981, 0.983, and 0.978, respectively indicate long tail request behavior at each of the server locations (refer Table 1). We can use the $\beta _ { 1 }$ coef<sup>fi</sup>cients to statistically test for differences in heterogeneity of website requests. Utilizing a paired sample test, we measure if the difference in $\beta _ { 1 }$ coef<sup>fi</sup>cients for any two locations is signi<sup>fi</sup>cant. Table 2 shows difference in $\beta _ { 1 }$ corresponding to the pair of locations listed in each row and column. The t statistic for this difference is $( \beta _ { 1 j } - \beta _ { 1 j ^ { \prime } \neq j } ) / \sqrt { \mathrm { V a r } ( \beta _ { 1 j } - \beta _ { 1 j ^ { \prime } \neq j } ) }$ , where j denotes server location. Using this, we con<sup>fi</sup>rm the difference in $\beta _ { 1 }$ coef<sup>fi</sup>cients is signi<sup>fi</sup>cant $\scriptstyle \left( p < 0 . 0 0 1 \right)$ for all $^ 4 { \sf C } _ { 2 } = 6$ pairs of locations. This supports Hypothesis 2 that the geographical location has a signi<sup>fi</sup>cant effect on diversity of website requests.

![](/api/attachments/96JCKUGB/fulltext/images/e4d89c4718552c756e67970af905beccf37f54d5de429700665b2f2a5b497897.jpg)  
Urbana-Champaign (UC)

Table 2  
Difference i $\beta _ { 1 }$ coef<sup>fi</sup>cients for four locations.

<table><tr><td></td><td>Boulder</td><td>Urbana-Champaign</td><td>New York</td></tr><tr><td>Silicon Valley</td><td>0.144160*</td><td>0.164*</td><td>0.017*</td></tr><tr><td>Boulder</td><td>N/A</td><td>0.019*</td><td>-0.127*</td></tr><tr><td>Urbana-Champaign</td><td>N/A</td><td>N/A</td><td>-0.147*</td></tr></table>

⁎ Signi<sup>fi</sup>cantly different from zero, pb0.001.

![](/api/attachments/96JCKUGB/fulltext/images/fb095ef0e2d76f4b5fdc326496a4368e8d17d23b20b1265b03d622409fd2b6e2.jpg)

The distribution of $\beta _ { 1 }$ coef<sup>fi</sup>cients for the four server locations is shown in Fig. 5. It shows that users from different locations do have different interests in online access. We can use this for judging if some locations can be grouped together based on website request patterns. For example, Silicon Valley and New York locations display greater heterogeneity in user's choice of information than Boulder and Urbana-Champaign. This can be explained partially by the fact that the former two areas have higher percentages of international immigrants and high-skilled workers. We use data from the US Census Bureau [30] to con<sup>fi</sup>rm this. The US Census Bureau is a comprehensive source of data for the nation's demographic pro<sup>fi</sup>le and economy. For our purpose we focus on demographic data for the counties where the four IRCache servers are located. This provides us information on factors such as percentage of foreign born residents, diversity of spoken language, and per capita income. The US Census county data [30] was collected between 1999 and 2000 and is representative of the proxy trace data time period. Table 3 shows the demographic pro<sup>fi</sup>les of the counties where the servers are located. We observe that the percentage of foreign born residents is signi<sup>fi</sup>cantly greater for Silicon Valley and New York compared to Boulder and Urbana-Champaign. This is also true for language other than English spoken at home for the four locations. This diversity of population in the two coastal areas compared to both inland locations indeed manifests in greater heterogeneity of web site requests. This demonstrates why the distributions of $\beta _ { 1 }$ coef<sup>fi</sup>cients for Silicon Valley and New York are similar in Fig. 5. The same is true for Boulder and Urbana-Champaign. We also observe from Table 3 that the two coastal areas have a higher per capita income than the inland areas, though this difference is less pronounced than international immigrants. This may indicate to an extent that persons with higher paid jobs tend to have more diversi<sup>fi</sup>ed interests and browsing behavior.

![](/api/attachments/96JCKUGB/fulltext/images/abd1dc01d39a8dd6454d2bb2e341fd2e44f0350bc3099e599459d13d95c19785.jpg)

![](/api/attachments/96JCKUGB/fulltext/images/9ad86de30dc51c2518573d44a98994b5e652bfa2b1e8c868dd33431699da82d6.jpg)  
Fig. 4. Frequency of requests vs. rank of sites for four server locations.

![](/api/attachments/96JCKUGB/fulltext/images/bb22f439f7c1a98fd37c1a5c1e8c604861346df00e6b6fad65e002f3b6b3d8fd.jpg)  
Fig. 5. Distribution of $\beta _ { 1 }$ for four server locations.

## 3.3. Effect of user's time of access on diversity of website requests (H3)

Next we consider the effect of time of access for website requests. For that we partition the trace data to website requests on weekdays and weekends for each location. Table 4 summarizes the log-linear regression for frequency of website requests onto rank of site on weekday and weekend. The high $R ^ { 2 }$ value for all cases indicates that long tail behavior does exist on both weekdays and weekends. As before, we use the $\beta _ { 1 }$ coef<sup>fi</sup>cients in each case to statistically test for differences in heterogeneity of website requests. The t statistic for this difference is $( \beta _ { 1 \mathrm { w d } } - \beta _ { 1 \mathrm { w e } } ) / \sqrt { \mathsf { V a r } ( \beta _ { 1 \mathrm { w d } } - \beta _ { 1 \mathrm { w e } } ) } ,$ , where wd and we denote weekday and weekend, respectively. Using this, we con<sup>fi</sup>rm the difference in $\beta _ { 1 }$ coef<sup>fi</sup>cients between weekday and weekend is signi<sup>fi</sup>cant $\scriptstyle \left( p < 0 . 0 0 1 \right)$ ) for all four locations. This supports Hypothesis 3 that time of access does have a signi<sup>fi</sup>cant effect on diversity of website requests. This can also be compared in Fig. 6 that shows distribution of weekday and weekend coef<sup>fi</sup>cients, $\beta _ { \mathrm { 1 w d } }$ and $\beta _ { 1 \mathrm { w e } } ,$ , for each location. We observe that distributions are indeed different. In Table 4 we observe a trend that |β | coef<sup>fi</sup>cients on weekends are lower at each location compared to weekdays. This indicates that there is greater diversity of requests on weekends. We reason this could be because users have more free time to explore personal interests during weekends rather than focus on work requirements during weekdays. This allows them to access diversi<sup>fi</sup>ed information sources during weekends.

Demographic pro<sup>fi</sup>le for four locations.

<table><tr><td>Server locations (counties where servers are located)</td><td>Foreign born persons, percent, 2000</td><td>Language other than English spoken at home, percent age 5+, 2000</td><td>Per capita money income, 1999</td></tr><tr><td>Silicon Valley (Santa Clara)</td><td>34.1%</td><td>45.4%</td><td>$32,795</td></tr><tr><td>Boulder (Boulder)</td><td>9.4%</td><td>13.6%</td><td>$28,976</td></tr><tr><td>Urbana-Champaign (Champaign)</td><td>8.0%</td><td>11.8%</td><td>$19,708</td></tr><tr><td>New York (New York)</td><td>29.4%</td><td>41.9%</td><td>$42,922</td></tr></table>

Log-linear regression for frequency of website requests onto rank of site for four locations on weekday and weekend.

<table><tr><td>Server locations</td><td>Time of access</td><td> $\beta_0$ </td><td> $\beta_1$ </td><td> $R^2$ </td><td>M</td></tr><tr><td rowspan="3">Silicon Valley</td><td>Weekday</td><td>12.855 (0.0054)</td><td>-1.124 (0.0005)</td><td>0.976</td><td>122,490</td></tr><tr><td>Weekend</td><td>10.750 (0.0092)</td><td>-1.053 (0.00096)</td><td>0.969</td><td>37,421</td></tr><tr><td colspan="2">Difference in  $\beta_1$ </td><td>-0.0713*</td><td></td><td></td></tr><tr><td rowspan="3">Boulder</td><td>Weekday</td><td>14.653 (0.0051)</td><td>-1.263 (0.00047)</td><td>0.980</td><td>136,599</td></tr><tr><td>Weekend</td><td>12.679 (0.0079)</td><td>-1.201 (0.00081)</td><td>0.979</td><td>46,548</td></tr><tr><td colspan="2">Difference in  $\beta_1$ </td><td>-0.0618*</td><td></td><td></td></tr><tr><td rowspan="3">Urbana-Champaign</td><td>Weekday</td><td>14.918 (0.0048)</td><td>-1.28 (0.00044)</td><td>0.983</td><td>140,406</td></tr><tr><td>Weekend</td><td>13.350 (0.0072)</td><td>-1.264 (0.00073)</td><td>0.984</td><td>46,342</td></tr><tr><td colspan="2">Difference in  $\beta_1$ </td><td>-0.0156*</td><td></td><td></td></tr><tr><td rowspan="3">New York</td><td>Weekday</td><td>12.984 (0.0051)</td><td>-1.131 (0.00048)</td><td>0.977</td><td>125,551</td></tr><tr><td>Weekend</td><td>11.325 (0.0079)</td><td>-1.088 (0.00081)</td><td>0.976</td><td>43,328</td></tr><tr><td colspan="2">Difference in  $\beta_1$ </td><td>-0.0425*</td><td></td><td></td></tr></table>

The Standard Errors are in parentheses, M = total website requests.  
⁎ Signi<sup>fi</sup>cantly different from zero, $\scriptstyle p < 0 . 0 0 1 .$

These results are important on multiple levels. First, online marketing strategies may be segmented to better target users from different locations. For example, a marketing company for a niche product, such as an exotic oriental vase, may allocate more resources to locations with more diversi<sup>fi</sup>ed website visitations Another example is that, rather than promoting a set of products uniformly across all locations, Internet portal websites may choose to advertise obscure products more in heterogeneous regions while focusing on mainstream product in more homogeneous regions. Second, Internet portals can adjust pricing schedules based on different regions at which the advertisements are targeted. Currently the cost of pay-perclick ads primarily depends on the search engine and the level of competition for a particular key word or key phrase. It also includes factors such as the relevance of an ad's text and the quality of an advertiser's web page [15]. We propose that web search <sup>fi</sup>rms such as Google may adjust their pay-per-click advertising model to accommodate that some locations have greater af<sup>fi</sup>nity for niche websites than others. An application of our results to online advertising is as follows. The value of advertisements in online markets can depend on diversity of user interests. There are two cases how this may be incorporated, shown in Fig. 7. Case 1: depending on steepness of the long tail at a given location or time, difference in price $p _ { 1 }$ and $p _ { 2 }$ for advertising two products m and m may be higher in a less diversi<sup>fi</sup>ed market compared to corresponding prices $p _ { 1 } ^ { \prime }$ and p' in more diversi<sup>fi</sup>ed

![](/api/attachments/96JCKUGB/fulltext/images/42f6ff1ec7175ce8413d3fdfa7825bbee8ee0d22d01813fc0906bc81f2af3373.jpg)

![](/api/attachments/96JCKUGB/fulltext/images/e87b0365e31c1b82497d05739b848765c8364eaee8133f41d8ca7c65af04a77f.jpg)

![](/api/attachments/96JCKUGB/fulltext/images/4caaedcff744daf93c72ee90cea9811ea305d94f88456f7a68806a6072c12ff4.jpg)

![](/api/attachments/96JCKUGB/fulltext/images/abe98dce6d6c233c35cd5f36e283334f75af914f40d5d79361b3f8cc69122c8d.jpg)  
Fig. 6. Distribution o $\dot { \beta } _ { 1 }$ for four server locations on weekdays and weekends.

markets. For example, in Fig. 7 $, p _ { 1 } - p _ { 2 } > p _ { 1 } ^ { \prime } - p _ { 2 } ^ { \prime }$ . Case 2: for the same product being advertised in two markets, the more demanded product $m _ { 1 }$ may be priced higher $p _ { 1 }$ at less diversi<sup>fi</sup>ed market than $p _ { 1 } ^ { \prime }$ at more diversi<sup>fi</sup>ed market. On the other hand lower demand product m may be priced lower $p _ { 2 }$ at less diversi<sup>fi</sup>ed market and priced higher $p _ { 2 } ^ { \prime }$ at more diversi<sup>fi</sup>ed market. For example, in Fig. 7 $, p _ { 1 } > p _ { 1 } ^ { \prime }$ and $p _ { 2 } < p _ { 2 } ^ { \prime }$ . The same reasoning may also be used for customizing Internet advertisements and marketing strategies based on the characteristics of website visitations. This approach is an improvement over current cost-per-click advertising and other online marketing models on the Internet that do not effectively consider location and time of access differences of users.

![](/api/attachments/96JCKUGB/fulltext/images/0f4f9a8412794c02ef05830812959e9fa63d5ae4d4b03b6ffb6064d47a031303.jpg)

![](/api/attachments/96JCKUGB/fulltext/images/ccdffb9ed8d9a4c0ea7475b1b57c2439e0697666d7c783b5321371766dd58b06.jpg)  
Fig. 7. Internet advertisement pricing based on long tail characteristics.

Finally, our results may help to design better Internet caching algorithms that are aware of the difference in the users' request patterns based on their locations. An example is as follows. For website locations and time periods with greater diversity of website requests we assign closer to equal priorities for caching different objects. With lesser diversity of requests we assign greater priorities to objects that are more popular. This would be an improvement over current LRU based caching mechanisms, such as those used at IRCache network (www.ircache.net), that do not consider server locations and time of access differences [20].

## 4. Discussion and conclusions

The users' requests for online information can be captured by a long tail model. Our study con<sup>fi</sup>rmed this phenomenon using the Zipf distribution. However previous models do not consider the impact of location and time of access on the diversity of website requests. Therefore we examined the differences in user browsing habits due to location and time of access using an actual proxy trace data. Our tests con<sup>fi</sup>rm our hypotheses that server location and time of access indeed have an effect on the heterogeneity of website requests. This can partially be explained by differences in demographic characteristics at locations, due to differing proportions of international immigrants and high-skilled workers, and diverse browsing behavior between weekdays and weekends. Our results can be used for designing better online marketing strategies, af<sup>fi</sup>liate advertising models, and Internet caching algorithms with sensitivities to user location and time of access differences.

This study examines users' online request patterns using data from multiple proxy servers. We analyzed the data by server locations and time of access. There are several interesting research avenues to pursue in the future. In the subsequent study we plan to expand the analysis to include patterns in user IP addresses across multiple days and locations. In addition our paired comparison method for server locations opens up avenues for using other techniques such as a Tukey–Kramer ANOVA for multiple comparisons. However an ANOVA procedure requires additional assumptions regarding equality of variance across locations. An area of future research is to develop tests for differences both within and across locations. Another line of reasoning is to compare if the extent of difference in weekday and weekend $| \beta _ { 1 } |$ coef<sup>fi</sup>cients is in<sup>fl</sup>uenced by location or other demographic factors. For example, in Table 4 weekday vs. weekend difference in $\beta _ { 1 }$ for SV, BO, UC and NY are 0.0713, −0.0618, −0.0156 and −0.0425, respectively. While we have shown that the differences are statistically signi<sup>fi</sup>cant for a particular location, there may be some differences across locations. An area for research can be to develop a statistical measure for testing extent of time of access difference across locations and to provide a rationale for the same. Finally one can also examine alternative approaches that consider smaller time intervals, such as hours or minutes, focused on speci<sup>fi</sup>c time zones to extract more managerial implications from user browsing patterns.

To the best of our knowledge our research is the <sup>fi</sup>rst to analyze diversity of website requests based on user location and time of access. There is a signi<sup>fi</sup>cant potential to improve on online marketing, advertising, and content customization by better understanding patterns in user request behavior. In addition they can be exploited for Internet caching algorithms to reduce user delays due to increasing congestion. Therefore we believe that this study contributes to ecommerce research that is bene<sup>fi</sup>cial for users, technology providers, and businesses on the Internet.

## List of notations

$f ( R )$ fraction of time that Rth most popular website is requested

$R$ rank of websites in terms of number of requests

$s$ exponent characterizing Zipf distribution

$\varOmega$ normalizing constant for Zipf distribution

$N$ total number of requested websites (n=1 to N)

$\beta _ { 0 }$ coef<sup>fi</sup>cient of log-linear regression that measures overall demand for unique websites

$\beta _ { 1 }$ intercept of log-linear regression that measures how quickly the share of total number of requests attributed to a particular website falls as site rank increases

$\beta _ { 1 j }$ $\beta _ { 1 }$ coef<sup>fi</sup>cient for any location j

$\beta _ { \mathrm { 1 w d } }$ $\beta _ { 1 }$ coef<sup>fi</sup>cient for weekdays wd

$\beta _ { \mathrm { 1 w e } }$ $\beta _ { 1 }$ coef<sup>fi</sup>cient for weekends we

$R ^ { 2 }$ coef<sup>fi</sup>cient of determination measure of goodness of <sup>fi</sup>t of log-linear regression

## Acknowledgements

We thank the seminar participants of the 2008 INFORMS Annual Meeting and the 2007 Workshop on e-Business (WEB) for valuable comments on this study.

## References

[1] V. Almeida, A. Bestavros, M. Crovella, A. de Oliveira, Characterizing reference locality in the WWW, Proceedings of Fourth IEEE International Conference in Parallel and Distributed Information Systems, Miami Beach, Florida, USA, 1996, http://www.cs.bu.edu/groups/oceans/papers/Home.html.

[2] C. Anderson, The Long Tail: Why the Future of Business is Selling Less of More, Hyperion, 2006.

[3] Associated Press, Internet Ad Revenue Exceeds \$21B in 2007, February 25, 2008 http://www.usatoday.com/money/advertising/2008-02-25-online-ad-revenue\_N. htm. Accessed on April 20 2008

[4] M.R. Baye, J. Rupert, J. Gatti, P. Kattuman, J. Morgan, A dashboard for online pricing, California Management Review 50 (1) (2007) 202–216.

[5] A. Bhatnagar, P. Papatla, Identifying locations for targeted advertising on the internet, International Journal of Electronic Commerce 5 (3) (2001) 23–44.

[6] L. Breslau, P. Cao, F. Li, G. Phillips, S. Shenker, Web caching and Zipf-like distributions: evidence and implications, Proceedings of the Eighteenth Annual Joint Conference of the IEEE Computer and Communications Societies INFOCOM, 1999.

[7] E. Brynjolfsson, Y.J. Hu, D. Simester, Goodbye Pareto Principle, Hello Long Tail: The Effect of Search Costs on the Concentration of Product Sales, 2007 Available at SSRN: http://ssrn.com/abstract=953587.

[8] E. Brynjolfsson, Y.J. Hu, M. Smith, Consumer surplus in the digital economy: estimating the value of increased product variety, Management Science 49 (2003) 1580–1596.

[9] L. Catledge, J. Pitkow, Characterizing browsing strategies in the world wide web in computer systems and ISDN systems, Proceedings of the Third International World Wide Web Conference, Darmstadt, Germany, 1995, pp. 1065–1073.

[10] Cisco Systems Visual Networking Index Forecast Report, 2008 http://www.cisco. com/en/US/netsol/ns827/networking\_solutions\_sub\_solution.html#.

[11] A. Cockburn, B. McKenzie, M. JasonSmith, Pushing back: evaluating a new behaviour for the back and forward buttons in web browsers, International Journal of Human-Computer Studies 57 (2002) 397–414

[12] Comscore Inc. Report, Global Internet Audience Surpasses 1 billion Visitors, 2009 http://www.comscore.com/press/release.asp?press=2698. Accessed on Jan 23, 2009.

[13] A. Datta, K. Dutta, H. Thomas, D. VanderMeer, World wide wait: a study of internet scalability and cache-based approaches to alleviate it, Management Science 49 (10) (2003) 1425–1444.

[14] F. Deborah, Search Engine Users: Internet Searchers are Con<sup>fi</sup>dent, Satis<sup>fi</sup>ed and Trusting — But They are Also Unaware and Naïve, 2005 Available at: http://www. pewinternet.org/pdfs/PIP\_Searchengine\_users.pdf.

[15] B. Edelman, M. Ostrovsky, M. Schwarz, Internet advertising and the generalized second-price auction: selling billions of dollars worth of keywords, American Economic Review 97 (1) (2007) 242–259.

[16] S. Glassman, A caching relay for the world wide web, Proceedings of First International Conference on the World Wide Web, CERN, Geneva, Switzerland, 1994, http://www1.cern.ch/WWW94/PrelimProcs.html.

[17] J. Hu, H. Zeng, H. Li, C. Niu, Z. Chen, Demographic prediction based on user's browsing behavior. Proceedings of the 16th International Conference on World Wide Web. Banff, Alberta. Canada. 2007.

[18] R.A. Johnson, D.W. Wichern, Applied Multivariate Statistical Analysis, Prentice Hall, Englewood Cliffs, NJ, 2002

[19] C. Kehoe, J. Pitkow, Surveying the territory: GVU's <sup>fi</sup>ve WWW user surveys, The World Wide Web Journal 1 (1996) 77–84.

[20] C. Kumar, Performance evaluation for implementations of a network of proxy caches, Decision Support Systems 46 (2009) 492–500.

[21] C. Kumar, J.B. Norris, A new approach for a proxy-level web caching mechanism, Decision Support Systems, 46 (2008) 52–60.

[22] C. Kumar, J.B. Norris, Y. Sun, Location does matter: a long tail study of website requests, Proceedings of the Sixth International Workshop on e-Business (WEB), 2007.

[23] M.O. Lorenz, Methods of measuring the concentration of wealth, Publications of the American Statistical Association 9 (70) (1905) 209–219

[24] X. Luo, M. Seyedian, Contextual marketing and customer-orientation strategy for e-commerce: an empirical analysis, International Journal of Electronic Commerce 8 (2) (Winter 2003–4) 95–118.

[25] V. Pareto, Cours d'economie politique, in G.H. Bousquet and G. Busino, Eds., Oevres Completes de Vilfredo Pareto, 1, 1964 Librairie Droz, Geneva (1896 Originally published).

[26] S. Podlipnig, L. Boszormenyi, A survey of web cache replacement strategies, ACM Computing Surveys 35 (4) (2003) 374–398.

[27] R. Sen, Optimal search engine marketing (SEM) strategy, International Journal of Electronic Commerce 10 (1) (2005) 9–25.

[28] R. Sen, R. King, M. Shaw, Buyers' choice of online search strategy and its managerial implications, Journal of Management Information Systems 23 (1) (2006) 211–238.

[29] L. Tauscher, S. Greenberg, How people revisit web pages: empirical <sup>fi</sup>ndings and implications for the design of history systems, International Journal of Human-Computer Studies 47 (1997) 97–138 Special issue on World Wide Web Usability

[30] U.S. Census Bureau, State and County Facts, 2008 http://quickfacts.census.gov/ qfd/.

[31] V. Venkatesh, R. Agarwal, Turning visitors into customers: a usability-centric perspective on purchase behavior in electronic channels, Management Science 52 (3) (2006) 367–382.

[32] E.F. Watson, Y. Shi, Y. Chen, A user-access model-driven approach to proxy cache performance analysis, Decision Support Systems 25 (1999) 309–338.

[33] G.K. Zipf, Human Behavior and the Principle of Least Effort, Addison-Wesley, Cambridge MA 1949.

Chetan Kumar is an Assistant Professor in the Department of Information Systems and Operations Management at the College of Business Administration, California State University San Marcos. He received his PhD from the Krannert School of Management, Purdue University. His research interests include managing computer networks, electronic commerce, web analytics, peer-to-peer networks, caching, and IS strategy for <sup>fi</sup>rms. His research has been published in Decision Support Systems journal. He has presented his research at INFORMS, Workshop on e-Business (WEB), Workshop on Information Systems and Economics (WISE), ICIS Doctoral Consortium, and AMCIS Doctoral Consortium conferences.

John B. Norris received his PhD from the Quantitative Methods area at the Krannert School of Management, Purdue University. His research interests include web analytics, healthcare management, and decision support tools for student team assignment. His research has been published in Decision Support Systems journal. He has presented his research at AOM, DSI, INFORMS, and POMS conferences.

Yi Sun is an Assistant Professor of Information Systems at the College of Business Administration, California State University San Marcos. His degrees include BA degree from Foreign Affairs College in Beijing, China and PhD (Management Information Systems) from University of Florida. He has research interests in telecommunications, data mining and arti<sup>fi</sup>cial intelligence, electronic commerce, and applied operations research. He has published several articles in refereed journals such as Decision Support Systems and European Journal of Operational Research.
