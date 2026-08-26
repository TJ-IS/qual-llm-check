---
otero_id: 28390
otero_key: "26QF68QY"
title: "Strategic Content Generation and Monetization in Financial Social Media"
authors: "Ding Li; Khim-Yong Goh; Cheng-Suang Heng"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0482"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic Content Generation and Monetization in Financial Social Media

Ding Li,<sup>a</sup> Khim-Yong Goh,<sup>b,</sup>\* Cheng-Suang Heng<sup>b</sup>

<sup>a</sup> Business School, Nanjing University, Nanjing 210093, China; <sup>b</sup> School of Computing, National University of Singapore, Singapore 117418 \*Corresponding author

Contact: liding@nju.edu.cn, https://orcid.org/0000-0003-3297-9172 (DL); gohky@comp.nus.edu.sg,

https://orcid.org/0000-0002-9291-2386 (K-YG); hengcs@comp.nus.edu.sg, https://orcid.org/0000-0001-6609-401X (C-SH)

Received: August 23, 2022

Revised: August 17, 2023; January 7, 2024

Accepted: January 14, 2024

Published Online in Articles in Advance: February 20, 2024

https://doi.org/10.1287/isre.2022.0482

Copyright: © 2024 The Author(s)

Abstract. Financial social media platforms, which rely on social media analysts (SMAs) to contribute content to investors, have emerged as a crucial channel for investors to gain access to financial information and for SMAs to monetize their content. However, we still have a limited understanding of the factors that affect how content is generated and monetized in financial social media platforms. This study focuses on the novel role of investors preferences for free/paid content and its sentiment and investigates the extent to which SMAs exhibit strategic content generation and monetization behaviors by catering to and trading off the investors’ preferences. We also evaluate the underlying mechanisms and implications of such strategic behaviors. Utilizing a data set from a financial social media platform based in China, we propose a Bayesian empirical model to jointly analyze the investor’s demand and SMAs’ strategic supply of financial social media content. The model estimation results show that SMAs cater to investors’, especially paid subscribers’, preferences in their content generation such that their strategic behaviors account for 46.20% (24.50%) of the variation in SMAs’ generation decision for free (paid) content sentiment. In addition, an SMA is more likely to produce paid content when the expected free readership increases and is less likely to do so when the expected paid subscriptions increase, evidence that SMAs do balance the preferences of different investors when mone tizing content. We find that SMAs are strategic in acquiring readers via their content monetization decisions and retaining subscribers via their content generation decisions. Importantly, we uncover that the orientation of an SMA’s strategic catering behavior is driven by the audience composition effect. Our study provides new empirical evidence, associated theoretical explanations for the results, and a practical illustration of an approach to reduce the potential confirmation bias of investors who may favor information from some SMAs that are prone to strategic catering behaviors.

History: Eric Zheng, Senior Editor; Tianshu Sun, Associate Editor

Open Access Statement: This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. You are free to download this work and share with others but cannot change in any way or use commercially without permission, and you must attribute this work as “Information Systems Research. Copyright © 2024 The Author(s). https://doi.org/10.1287/ isre.2022.0482, used under a Creative Commons Attribution License: https://creativecommons.org licenses/by-nc-nd/4.0/.”

Funding: This research is partially supported by the National Research Foundation, Singapore [Project Grant A-0004920-02-00]

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0482.

Keywords: strategic behavior • content generation • content monetization • investor preference • financial social media • Bayesian estimation

## 1. Introduction

Social media has profoundly transformed the financial sectors (Luo et al. 2013, Zheludev et al. 2014, Arner et al. 2015). Specifically, to promote informational exchanges and to address the low financial literacy and behavioral biases of retail investors (Barberis and Thaler 2003), financial social media platforms have engaged social media analysts (SMAs) to contribute investment information to retail investors. Such platforms have gained tremendous popularity in recent years (Matsuyama and Wood 2022, Egan and Cetera 2023). For instance, Stock-Twits, a U.S.-based financial social media platform, garnered more than 15.4 million monthly visitors in 2022. In January 2021, r/wallstreetbets, a popular investmentrelated subreddit of the social news website Reddit, ini tiated the short squeeze of GameStop and caused its stock price to increase 30 times within a month, which resulted in large losses to hedge funds and short sellers.<sup>2</sup>

Despite the popularity and implications of social media intermediation on the financial industry, the literature on financial social media (Antweiler and Frank 2004, Sabherwal et al. 2008, Bollen et al. 2011) still lacks two key aspects that motivate this study.

The first research gap is the lack of a good understanding of SMAs’ content generation process. The current literature on financial social media has focused largely on the informational value of social media content in predicting stock market movements (Das and Chen 2007, Sabherwal et al. 2008, Luo et al. 2013, Chen et al. 2014), whereas the research on SMAs’ supply of financial social media content is still limited (Chen et al. 2019). Unlike traditional financial analysts who need to undergo professional training (e.g., CFAs) and whose reports need to follow strict guidelines,<sup>3</sup> SMAs are often grassroots analysts without qualifications or degrees,<sup>4</sup> and there are no clear guidelines or rules of conduct that regulate what SMAs can write. Thus, SMAs’ content generation process may be materially different from traditional analysts’ report-writing process (De Franco et al. 2009, Brown et al. 2015, Meng 2015, Huang et al. 2018) and thus demands more research. Unpacking SMAs content generation process is also of practical importance in terms of offering insights into regulating SMAs behaviors in this ever-growing and impactful realm of financial social media (Kogan et al. 2022).

The second research gap is the lack of a good understanding of SMAs’ content monetization strategy. This gap also exists in the larger user-generated content (UGC) and social media literatures. The focus of the extant literatures has been on examining the impact of the implementation of content monetization policies (Pauwels and Weiss 2008, Oh et al. 2016, Lambrecht and Misra 2017), where the monetization decisions are made by the platforms as part of the content pricing strategy. However, these related literatures have overlooked the fact that nowadays, content is generated primarily by various freelance or professional contributors (e.g., SMAs in our paper), and the monetization decisions are increasingly democratized to these contributors (e.g., in Youtube Premium Subscription, StockTwits Rooms, Zhihu Paid Consulting, etc.). This literature has thus shed little insight from a supply-side perspective on how and why content contributors may monetize content in a heterogeneous manner. We note that this gap is due primarily to the lack of actual monetization data of individual content contributors. Enabled by the novel data we have, we endeavor to fill this research gap to both advance the theoretical understanding of contributors’ decision-making process and offer practical insights into determining improved monetization strategies for content generation businesses.

To bridge the above two gaps in SMAs’ content generation and monetization process, we highlight two theoretical significances of our research objectives. The first theoretical significance involves a focus on the role of demand-side information in SMAs’ decisions and the emphasis on investor preferences. An important difference between traditional analysts and SMAs is the availability of demand-side information. That is, although traditional analysts often work inside the boundaries of a company (e.g., securities firms, investment banks) and disseminate their reports to investors unidirectionally, the interactive nature of financial social media has brought SMAs and investors unprecedentedly close, giving SMAs the opportunity to gain access to the investor preferences of their own audience base for their content (e.g., via comments, likes, changes in free readership, and paid subscriptions). The following question then arises: To what extent will SMAs exploit this opportunity and strategically generate and monetize content by catering to investor preferences? The finance literature about catering theory (Baker and Wurgler 2004a, b) has found that, driven by the catering incentives, firms, fund managers, and analysts strategically pay dividends (Baker and Wurgler 2004b), include more popular stocks in a portfolio (Ben-David et al. 2023), and issue more timely reports (Chiu et al. 2021) in exchange for higher stock prices, more investor attention, and better career outcomes. Similarly, driven by the incentive to boost performance metrics in financial social media (e.g., free readership, paid subscriptions), SMAs may thus engage in strategic content generation and monetization by catering to investor preferences for their content.

By simultaneously examining SMAs’ content generation and monetization decisions, this highlights the second theoretical significance of our work. Specifically, this allows us to zoom in on investor preferences for SMAs’ content and decompose them into (free) readers preferences and (paid) subscribers’ preferences. The content monetization literature has long established that content contributors (e.g., SMAs in financial social media platforms) may act upon various incentives or motivations (Tang et al. 2012, Zhao et al. 2016) for content generation, and as a form of extrinsic motivation, monetary incentives have been shown to crowd out intrinsic motivations for generating content (Becker et al. 2010, Hsieh et al. 2010, Mason and Watts 2010, Stephen et al. 2012, Wang et al. 2012, Liu et al. 2014, Liu and Feng 2015). However, less is known about the scenario when content contributors are given a chance to monetize content on their own, how they may trade off the (poten tially conflicting) investor preferences of free readers (relating to nonmonetary incentives) and paid subscribers (relating to monetary incentives) in both the content generation and monetization decisions.

Motivated by the above research gaps and significances, this paper aims to evaluate the extent of SMAs strategic behaviors in content generation and monetization by catering to and trading off investor preferences.

We then take a further step to examine the theoretical mechanisms that may underpin SMAs’ strategic behaviors. Lastly, we assess the practical implications and potential negative consequences of SMAs’ strategic behaviors on aggravating investors’ confirmation bias (Park et al. 2013). Overall, our research questions are thus as follows:

(1) How and to what extent do SMAs exhibit strategic content production behaviors by generating and monetizing content to cater to investor preferences in financial social media?

(2) How and to what extent do SMAs exhibit strategic content production behaviors by trading off the investor preferences of free readers and paid subscribers in the content generation and monetization of financial social media?

To answer our research questions, we obtained data from iMaibo, one of the leading financial social media platforms based in China. Our data contains detailed information about SMAs, including their attributes, financial social media content, (free) readership, (paid) subscription records, and user interactions, as well as China’s stock market performance. We then propose a joint model of content demand and supply following the nonrandom marketing-mix variable framework as the identification approach to address potential endogeneity biases (Bronnenberg and Mahajan 2001, Manchanda et al. 2004). Our proposed model accounts for investors’ (i.e., free readers’ and paid subscribers’) timevarying preferences for free/paid content and its sentiment and SMAs’ incorporation of these preferences into their content generation and monetization decisions. Our model also accounts for SMA heterogeneity (with a random coefficients specification).

Our empirical analysis uncovers important new findings. First, we find evidence that SMAs exhibit strategic behaviors in both content generation and monetization in catering to investor preferences for financial social media content. Specifically, SMAs would increase the (negative) sentiment of the content if paid subscribers preferences for (negative) sentiment grow. In addition, we show that SMAs’ strategic behaviors account for 46.20% (24.50%) of the variation in the SMAs’ content generation decision for free (paid) content sentiment. Second, our results reveal that SMAs do trade off the preferences of free readers and paid subscribers such that an SMA is more likely to produce paid content when the expected free readership increases and is less likely to do so when the expected subscriptions increase. Third, SMAs cater more to readers’ preferences in the content monetization decision but cater more to subscribers’ preferences in the content generation decision, implying that SMAs are strategic in acquiring readers via their content monetization decisions and retaining subscribers via their content generation decisions. Fourth, our evaluations of the underlying mechanism reveal that the composition of an SMA’s investor audience base governs the orientation of an SMA’s catering behavior.

Our study makes the following theoretical and practical contributions. First, our study is among the first to document how investor preferences influence SMAs strategic content generation. Second, we add to the existing content monetization and pricing literature by studying individual content contributors’ heteroge neous content monetization decisions on financial social media. Third, we advance the user-generated content literature by documenting the trade-off between free readership and paid subscriptions of content contribu tors when making decisions on content generation and monetization. Fourth, we contribute to the IS literature by evaluating the underlying mechanism for SMAs strategic content production behaviors in relation to the composition of an SMA’s audience base. Last, on the practical implications, we also illustrate an approach to identify the SMAs who may amplify the confirmation biases of investors such that platform managers and regulators alike can apply to improve the content quality of financial social media.

## 2. Literature Review

## 2.1. Financial Social Media

Social media has emerged as a prominent channel for retail investors to obtain investment information (Chen et al. 2014, Hu and Tripathi 2017, Kadous et al. 2019). Prior researchers have focused on assessing the informational value of the content on social media using stock- or firm-level analysis. For example, compared with financial analysts, social media channels often offe more accurate forecasts (Bagnoli et al. 1999, Clarkson et al. 2006) and more timely coverage of stock events (Shi et al. 2014). The sentiments extracted from the content on social media are an important construct in this literature, which can predict some stock market metrics (e.g., stock volatility, trade volume (Antweiler and Frank 2004), stock price, returns, and earnings surprises (Das and Chen 2007, Sabherwal et al. 2008, Luo et al. 2013, Chen et al. 2014). Recently, researchers have also started to investigate how social media content influences the investment decisions of retail investors (Kadous et al. 2019).

Critically, we find that the extant body of literature on financial social media has focused mainly on the impact of financial social media content (e.g., assessing the informational value of financial social media content). However, relatively little research effort has focused on supply-side decisions by SMAs, that is, for the generation and monetization of financial social media content. Chen et al. (2019), which examined how the introduc tion of monetary incentives affects the amount and quality of financial social media content, is a rare exception. Nonetheless, this prior study neither accounts for the role of investor preferences for the content nor considers the extent and nature of strategic content generation and monetization, all of which we address in this study.

Furthermore, we note that the finance literature on catering theory (Baker and Wurgler 2004b, Baker et al. 2009) has emphasized the importance of investor preferences for resulting in the strategic behaviors of firms, fund managers, and analysts. For instance, investor preference for dividends brings a stock price premium for dividend-paying firms, which motivates firms to pay dividends to investors (Baker and Wurgler 2004a, b). Investor preference for lower-priced stocks places a premium on firms with low share prices. Accordingly, firms may strategically split the shares to lower the nominal price of each stock share in order to increase the overall firm valuation (Baker et al. 2009). ETF (exchange-traded fund) managers attract investors attention by designing portfolios that cater to investors expectations of high future returns (e.g., by including popular stocks) (Ben-David et al. 2023). Analysts also cater to institutional investors’ attention by issuing more timely coverage of stocks, because the institutional investors may vote for the analysts to be “all-star” analysts (Chiu et al. 2021). An important distinction of SMAs from traditional analysts is that SMAs have the advantage of having close social interactions or connections with their own audience base, which makes it easy for SMAs to discern investor preferences for their content. By following the logic of catering theory to examine the novel role of investor preferences in shaping SMAs strategic behaviors, our study aims to advance the financial social media literature by providing a thorough understanding of SMAs’ dual processes of generating and monetizing content.

We next review the studies on content generation and monetization to position our study in the relevant literature. We present a list of relevant literature in Table A1 of the Online Appendix.

## 2.2. Content Generation

The literature has examined a spectrum of factors that may affect online content generation, including social network factors (e.g., network size (Qiu and Kumar 2017, Baek and Shore 2020, Wei et al. 2020), network structure factors (Lu et al. 2017, Bhattacharya et al. 2019)), distance factors (e.g., spatial distance, virtual distance (Hwang et al. 2015, Guo et al. 2020)), content platform policies (e.g., content sharing (Heimbach and Hinz 2018), privacy control (Cavusoglu et al. 2016)), cognitive factors (e.g., reciprocity (Zhao et al. 2016), reputation (Tang et al. 2012)), and monetary incentives (Becker et al. 2010, Hsieh et al. 2010, Mason and Watts 2010, Stephen et al. 2012, Tang et al. 2012, Wang et al. 2012, Liu et al. 2014, Liu and Feng 2015). There is another stream of literature studying strategic content generation. For instance, Shen et al. (2015) found that with a review ranking system, reviewers tend to avoid crowded review segments and post more differentiated reviews. Nguyen et al. (2021) showed that more experienced reviewers are inclined to post less extreme ratings. Goes et al. (2014) reported that as a reviewer becomes more popular, his or her reviews become more objective, negative, and varied.

Our study extends the literature on online content generation by investigating the extent to which SMAs engage in strategic content generation (and content monetization) by catering to and trading off investor preferences, a type of demand-side factor, which has been overlooked by prior studies.

## 2.3. Content Monetization

Content monetization is critical to the long-term sustainability of digital content businesses, including financial social media. Recently, there has been an emerging stream of research on paid content. In the paid content business, a portion of digital content is accessible only after the payment of a certain amount of fee (often on a subscription basis). Two topics have been examined in this literature. The first topic focuses on the design of paid content policies. Content platforms are recommended to charge lower prices when demand is higher (Lambrecht and Misra 2017) and pay greater attention to the quantity of free content (Aral and Dhillon 2020). The second topic examines the impact of the implementation of a paid content policy, such as the digital paywall by the New York Times (NYT). Researchers have found that the implementation of paid content policy leads to readership loss (Pauwels and Weiss 2008), a lon ger tail for the word-of-mouth (WOM) of news articles in social media (Oh et al. 2016), and a positive spillover on NYT’s offline businesses (Pattabhiramaiah et al. 2018).

This paper differs from the extant literature on content monetization in two ways. First, we study the indi vidual content contributor’s (i.e., SMAs’) heterogeneous decision to monetize content, in contrast to the current literature’s focus on a uniform platform-level implementation of content monetization policy. Our study adds a timely complement to the literature because although content contributors are increasingly given the discretion to monetize content, their motivations and actions to do so are still unknown. Second, content con tributors may act upon various motivations to generate content (see Section 2.2). However, the extant literature has not studied the motivations that drive a contributor’s decision to monetize content. Our study of SMAs’ strategic content monetization through catering to and trading off investor preferences fills this critical gap by examining the extent of SMAs’ tradeoff between monetary (relating to paid subscriber’s preferences) and nonmonetary motivations (relating to free readers’ preferences).

## 3. Methodology

## 3.1. Data Description

On our focal platform iMaibo, SMAs can publish both free and paid content in tweet form, similar to those on Twitter. Such content involves mainly investment analysis or advice (e.g., stock recommendations, asset allocations) for the Chinese stock market. Free content is accessible to all, whereas paid content is visible only to those who paid for subscriptions to specific SMAs. Investors can subscribe to SMAs’ paid content on a daily, monthly, or quarterly basis. We obtained detailed data associated with SMAs and market conditions from July 2014 to June 2016. In total, we have a panel of 531 SMAs across 51,466 daily observations.

We present the summary statistics of our data and the definition of variables or measures in Table 1. The average numbers of daily free readers and paid subscribers for these SMAs are 821.41 (s.d. � 2,244.02) and 37.0 (s.d. � 187.04), respectively. Each day on average, SMAs incidence or probability of producing paid content is 19%. More details of our data and additional summary statistics are elaborated in the Online Appendix.

## 3.2. Model-Free Evidence and Reduced-Form Analysis

In this paper, we focus on SMAs’ (negative) sentiment<sup>5</sup> levels of free and paid content as their focal content generation decision. We report model-free evidence and patterns in the data to motivate the setup of our econometric model. First, Figure 1 plots the average daily (negative) sentiment levels of the free and paid content of SMAs over time. We find that the (negative) sentiment of the paid content is mostly higher, that is, more negative than that of the free content, suggesting a significant difference in the content generation decisions for the free and paid content.

Second, we explore why SMAs generate sentiment differently for the free and paid content. A plausible explanation is that the stocks covered in the free and paid content have rather different investment potentials. Crucially, the stocks in the free and paid content may have different investment returns. To verify this, we run a simple regression by regressing the sentiment difference in an SMA’s free and paid content on a specific day (SentimentDiff ) on the difference in stock returns

Table 1. Summary Statistics (N � 51,466)

<table><tr><td>Category</td><td>Variable</td><td>Definition</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td rowspan="2">Demand</td><td>Reader</td><td>Readership, number of free readers for SMA  $i$  on day  $t$ </td><td>821.41</td><td>2,244.02</td><td>0.00</td><td>51,121.00</td></tr><tr><td>Subscriber</td><td>Subscription, number of paid  $subscribers^a$  for SMA  $i$  on day  $t$ </td><td>37.00</td><td>187.04</td><td>0.00</td><td>3,959.00</td></tr><tr><td rowspan="3">Supply</td><td>Monetize</td><td>Whether SMA  $i$  produced paid content on day  $t$ </td><td>0.19</td><td>0.39</td><td>0.00</td><td>1.00</td></tr><tr><td>FreeSentiment</td><td>Proportion of negative words in newly posted free content of SMA  $i$  on day  $t$  (Tetlock 2007, Tetlock et al. 2008)</td><td>0.27</td><td>0.16</td><td>0.00</td><td>1.00</td></tr><tr><td>PaidSentiment</td><td>Proportion of negative words in newly posted paid content of SMA  $i$  on day  $t$ </td><td>0.06</td><td>0.14</td><td>0.00</td><td>1.00</td></tr><tr><td rowspan="14">Controls or Moderators</td><td>Comment</td><td>No. of comments received by SMA  $i$  on day  $t$ </td><td>36.82</td><td>177.51</td><td>0.00</td><td>8,591.00</td></tr><tr><td>Like</td><td>No. of likes received by SMA  $i$  on day  $t$ </td><td>106.40</td><td>370.01</td><td>0.00</td><td>9,613.00</td></tr><tr><td>Follower</td><td>No. of followers of SMA  $i$  on day  $t$ </td><td>18,766.00</td><td>64,475.24</td><td>0.00</td><td>661,517.00</td></tr><tr><td>Tenure</td><td>No. of days since SMA  $i$  joined the iMaibo platform</td><td>271.60</td><td>226.80</td><td>1.00</td><td>1,204.00</td></tr><tr><td>isTradeDay</td><td>Whether day  $t$  is a stock trading day</td><td>0.88</td><td>0.32</td><td>0.00</td><td>1.00</td></tr><tr><td>TradeVolume</td><td>Trade volume of the Chinese stock market (in millions)</td><td>26,499.91</td><td>17,461.94</td><td>0.00</td><td>85,713.28</td></tr><tr><td>VIX</td><td>CBOE China ETF Volatility Index on day  $t$ </td><td>26.81</td><td>12.23</td><td>0.00</td><td>58.40</td></tr><tr><td> $StocksReturn^f$ </td><td>Return of stocks covered in free content of SMA  $i$  on day  $t$ </td><td>0.00004</td><td>0.02</td><td>-0.08</td><td>0.06</td></tr><tr><td> $StocksReturn^p$ </td><td>Return of stocks covered in paid content of SMA  $i$  on day  $t$ </td><td>-0.00064</td><td>0.10</td><td>-0.23</td><td>0.13</td></tr><tr><td>MarketReturnPrior1D</td><td>Return of the Chinese stock market in prior 1 day</td><td>0.003</td><td>0.05</td><td>-0.05</td><td>0.09</td></tr><tr><td>MarketReturnPrior1M</td><td>Return of the Chinese stock market in prior 1 month</td><td>0.014</td><td>0.11</td><td>-0.20</td><td>0.46</td></tr><tr><td>Price</td><td>Per-day price of SMA  $i$ &#x27;s subscription package</td><td>183.38</td><td>312.94</td><td>0.00</td><td>1,000.00</td></tr><tr><td>SubscriberReaderRatioLag</td><td>Ratio of SMA  $i$ &#x27;s no. of paid subscribers to that of free readers on day  $t-1$ </td><td>0.018</td><td>0.09</td><td>0.00</td><td>1.68</td></tr><tr><td>SubscriberFollowerRatioLag</td><td>Ratio of SMA  $i$ &#x27;s no. of paid subscribers to that of followers on day  $t-1$ </td><td>0.003</td><td>0.02</td><td>0.00</td><td>0.29</td></tr></table>

Figure 1. (Color online) Sentiment Levels of Free and Paid Content Over Time  
![](/api/attachments/26QF68QY/fulltext/images/9b750f1a99bf64825bcc7a9a8314d52b47d6a7fc6f4bba3cbf5ee9b7abbcb1a3.jpg)

for the stocks covered in the SMA’s free and paid content on the same day (ReturnDiff ) and from the previous day (ReturnDiffLag). The results in Table 2 show insignificant effects of ReturnDiff and ReturnDiffLag on SentimentDiff, suggesting that the differences in stock coverage cannot explain the sentiment differences in SMAs’ free and paid content.

Third, another explanation for why SMAs generate sentiment differently for the free and paid content is that free readers and paid subscribers exhibit different preferences for free and paid content. As such, SMAs strategically generate content sentiment in a way that caters to the different preferences of these readers and subscribers. To verify this, we run a simple regression by regressing the sentiment of free and paid content of an SMA on a specific day on the sentiment of the content receiving the most likes from the previous day (i.e., Free-SentimentMostLikedLag and PaidSentimentMostLikedLag, as proxies for investor preferences for sentiment) and show the results in Table 3. We find that the sentiment of the free (paid) content receiving the most likes from the prior day shows a significant positive relation with the sentiment of current free (paid) content. This finding suggests that investor preferences can explain the sentiment levels in SMAs’ content generation decisions for free and paid content sentiment. This reduced-form analysis provides suggestive evidence that SMAs may cater to investor preferences for content sentiment, which motivates our model setup in Section 3.3.

Table 2. Regression of Free/Paid Content Sentiment Difference on Stock Returns Difference

<table><tr><td>Variable</td><td>SentimentDiff</td></tr><tr><td>ReturnDiff</td><td>0.047(0.065)</td></tr><tr><td>ReturnDiffLag</td><td>0.061(0.044)</td></tr><tr><td> $R^2$ </td><td>0.322</td></tr></table>

Notes. Standard deviation in parentheses. \*Estimates significant at 90%; \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.

Table 3. Regression of Free/Paid Content Sentiment on Lagged Sentiment of Most Liked Content

<table><tr><td>Variable</td><td>FreeSentiment</td><td>PaidSentiment</td></tr><tr><td>Intercept</td><td>0.192***(0.011)</td><td>0.192***(0.017)</td></tr><tr><td>FreeSentimentMostLikedLag</td><td>0.160***(0.037)</td><td></td></tr><tr><td> $StocksReturn^f$ </td><td>-0.044(0.063)</td><td></td></tr><tr><td>PaidSentimentMostLikedLag</td><td></td><td>0.248***(0.049)</td></tr><tr><td> $StocksReturn^p$ </td><td></td><td>-0.271**(0.085)</td></tr><tr><td> $R^2$ </td><td>0.042</td><td>0.114</td></tr></table>

Notes. Standard deviation in parentheses. \*Estimates significant at 90%; \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.

Fourth, in our econometric model, we assume that investors have preferences for content sentiment,<sup>6</sup> and the preference may be time-varying. Investor preferences for sentiment represent their belief of the stock market orientations (Barberis et al. 1998, Park et al. 2013), that is, the expected or projected movement direction or trend (e.g., bullish or bearish) of stock prices. Given that the stock market conditions are volatile and always changing, investors’ own beliefs of the market orientations may be time-varying as well (Barron 1995, Benner and Ranganathan 2013, Giglio et al. 2021). Therefore, our above-mentioned assumption is conceptually reasonable. To bolster this claim, we present evidence to support our assumption. We plot the average daily sentiment of the free and paid content receiving the most likes for all SMAs (as proxies for investor preferences for sentiment) in Figure 2. We observe that the sentiment of the content receiving the most likes changes considerably from day to day. We further regress the sentiment of the content receiving the most likes on a specific day (i.e., FreeSentimentMostLiked and PaidSentimentMostLiked) on the corresponding sentiment from the previous day (i.e., FreeSentimentMostLikedLag and PaidSentimentMostLikedLag). Results in Table 4 reveal that the lagged sentiment terms do not have statistically significant effects. Hence, the sentiment of the content with the most likes is not serially correlated, implying that investor preferences for sentiment are indeed time varying.

Our model-free evidence validates our assumption that investors have time-varying preferences for content sentiment and supports our model setup that investor preferences for content enter into SMAs’ content generation decisions. Importantly, we note that reduced-form regression analyses using the preference proxies above (i.e., aggregate sentiment of the content receiving the most likes) do not allow us to distinguish between free readers’ and paid subscribers’ preferences for free and paid content (e.g., because paid subscribers have access to both free and paid content, they can have preferences for both types of content sentiment). Consequently, we resort to a structural econometric modeling approach that we elaborate on in Section 3.3.

Figure 2. (Color online) Sentiment Levels of the Most Liked Free and Paid Content Over Time  
![](/api/attachments/26QF68QY/fulltext/images/af605f03cbe0fb8f2e59a10f7d6ae14db268fcaaf387aef7e98cdef0742a15dd.jpg)

Table 4. Regression of Free/Paid Content Sentiment of Most Liked Content on Corresponding Lagged Terms

<table><tr><td>Variable</td><td>FreeSentimentMostLiked</td><td>PaidSentimentMostLiked</td></tr><tr><td>Intercept</td><td>0.227***(0.015)</td><td>0.258***(0.018)</td></tr><tr><td>FreeSentimentMostLikedLag</td><td>0.028(0.020)</td><td></td></tr><tr><td> $StocksReturn^f$ </td><td>0.122(0.091)</td><td></td></tr><tr><td>PaidSentimentMostLikedLag</td><td></td><td>0.002(0.013)</td></tr><tr><td> $StocksReturn^p$ </td><td></td><td>-0.284**(0.120)</td></tr><tr><td> $R^2$ </td><td>0.002</td><td>0.003</td></tr></table>

Notes. Standard deviation in parentheses. \*Estimates significant at 90%; \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.

## 3.3. Model Specification

We now propose a Bayesian model for our empirical analysis. This model needs to fulfill three functions: (1) capture the time-varying investor preferences, (2) capture SMAs’ strategic catering and trade-off of investor preferences in content generation and monetization decisions, and (3) handle the potential endogeneity biases in investor preferences and SMA responses. For the first function, we use a state-space model on the demand side (Lachaab et al. 2006, Sriram and Kalwani 2007, Zhao et al. 2009, Liu and Shankar 2015, Kim and Kumar 2018) to model the dynamic evolution of investor preferences. For the second and third functions, we employ the framework of nonrandom marketing-mix variables (Bronnenberg and Mahajan 2001, Manchanda et al. 2004). We thus have a joint model of content demand and supply for the financial social media and elaborate on it below.

3.3.1. Demand Side. On the demand side, we model the two major performance metrics (or incentives) of SMAs, namely the (free) readership and (paid) subscriptions. We link the two performance metrics with the sentiment levels of an SMA’s free and paid content, for which the model coefficients reveal investors’ (i.e., readers’ and subscribers’) preferences for the SMA’s content sentiment. Investor preferences for sentiment may be time-varying because of the changing market conditions and investment portfolios (which is verified by our model-free evidence in Section 3.2). We use the statespace model (also called the structural time series model) to model the time-varying investor preferences. It is widely used to model customers’ time-varying preferences (or responsiveness) for brands, marketing-mix variables, or other explanatory variables (Lachaab et al. 2006, Sriram and Kalwani 2007, Zhao et al. 2009, Liu and Shankar 2015, Kim and Kumar 2018, Song et al. 2019, Wang et al. 2021). In general, a state-space model consists of two sets of equations, with the observation equation specifying the relationship between observed behaviors and the time-varying parameters and the state equation specifying the evolution of time-varying parameters. In our paper, the observation equations specify free readership and paid subscriptions as functions of explanatory covariates and time-varying investor preferences. Furthermore, the state equations depict the dynamic nature of time-varying investor prefer ences in the observation equations.

## 3.3.1.1. Observation Equations.

$$
R e a d e r _ {i t} = \alpha_ {i 0} + \alpha_ {i t} ^ {f} F r e e S e n t i m e n t _ {i t} + \pmb {\rho} _ {i} ^ {r} C o n t r o l + \epsilon_ {i t} ^ {r}\tag{1}
$$

$$
\begin{array}{c} S u b s c r i b e r _ {i t} ^ {*} = \beta_ {i 0} + \beta_ {i t} ^ {f} F r e e S e n t i m e n t _ {i t} + \beta_ {i t} ^ {p} P a i d S e n t i m e n t _ {i t} \\ * 1 (M o n e t i z e _ {i t} = 1) + \boldsymbol {\rho} _ {i} ^ {s} C o n t r o l + \epsilon_ {i t} ^ {s} \end{array}\tag{2}
$$

$$
\left\{ \begin{array}{c l} S u b s c r i b e r _ {i t} ^ {*} = S u b s c r i b e r _ {i t} & \text { if } M o n e t i z e _ {i t} = 1 \\ S u b s c r i b e r _ {i t} ^ {*} \in [ S u b s c r i b e r _ {i t}, + \infty) & \text { if } M o n e t i z e _ {i t} = 0 \end{array} \right.\tag{3}
$$

We define two continuous variables, Reader and Sub-$s c r i b e r _ { i t } ,$ to measure the number of free readers<sup>7</sup> and paid subscribers SMA i has on day t. Subscriber<sub>it</sub> is the observed subscription of an SMA (including both nonexpired and new subscriptions). We use $S u \ ' { b s c r i b e r } _ { i t } ^ { * 8 }$ to denote the potential subscriptions of an SMA and relate it to the observed subscriptions, as shown in Equation $\left( 3 \right) . ^ { 9 }$ By augmenting the observed subscriptions in this wa ${ \mathrm { y } } , ^ { 1 0 }$ we can account for the number of subscriptions an SMA would have obtained if he or she were to produce paid content on that day.

Because we have three SMA behaviors (i.e., free content sentiment generation, paid content sentiment generation, and content monetization) and two types of investors $( \mathrm { i . e . , }$ free readers and paid subscribers), there are five investor preferences in our paper: (1) free readers’ preference for free content sentiment $( \mathrm { i . e . , } \alpha _ { i t } ^ { f } )$ , (2) free readers’ preference for free content (or expected readership, i.e., E(Reader )), (3) paid subscribers’ preference for free content sentiment $( \mathrm { i . e . , \it \beta _ { i t } ^ { f } } ) ,$ , (4) that for paid content sentiment $( \mathrm { i . e . , ~ } \beta _ { i t } ^ { p } ) , ^ { 1 1 }$ and (5) paid subscribers preference for monetized or paid content (or expected subscriptions, i.e., E(Subscriber )<sup>12</sup>).

For investor preferences for content monetization, conceptually, the expected readership $( E ( R e a d e r _ { i t } ) )$ and expected subscriptions $( E ( S u b s c r i b e r _ { i t } ) )$ measure the free readership and paid subscriptions an SMA is projected to get if an SMA decides to monetize his or her content. Thus, the expected readership and expected subscriptions capture the general consumption preferences of free readers and paid subscribers toward an SMA’s content.

For investor preferences for content generated, we examine the preferences for the sentimen $\mathrm { t } ^ { \mathrm { 7 3 } }$ of an SMA’s free and paid content (i.e., revealed by the effects of SMAs’ free and paid content sentiment on free readership and paid subscriptions). Thus, we take the sentiment of free and paid content as key content generation decisions of SMAs while accounting for factors such as prediction accuracy, diversity, and novelty of stocks.

We focus on investor preferences for sentiment<sup>14</sup> because our literature review reveals that sentiment is the most widely used construct for measuring the informational aspect of financial content (Das and Chen 2007, Tetlock et al. 2008, Loughran and McDonald 2011), especially for negative sentiment (Tetlock 2007). Importantly, sentiment is shown to be diagnostic and evaluative of the fundamentals of firms (Tetlock 2007) while projecting the future prospects of firms.<sup>15</sup> Sentiment is thus used widely to predict stock market performance (Tetlock 2007, Tetlock et al. 2008). Consistent with the literature, we regard the content sentiment generation decision of an SMA as the SMA’s assessment on the outlook of the stocks commented by him or her $( \mathrm { i . e . , }$ $F r e e S e n t i m e n t _ { i t } ,$ $P a i d S e n t i m e n t _ { i t } )$ . Importantly, the confirmation bias theory of behavioral finance (Park et al. 2013) proposes that investors tend to favor information that confirms or supports their prior beliefs. In other words, investors have their own beliefs about the outlook of the stock market, which may be different from $\mathrm { S M A s } ^ { \prime }$ . In our context, investors’ own beliefs or assessments can be captured by the investor preferences for the content sentiment $( \mathrm { i . e . , } \alpha _ { i t } ^ { f } , \beta _ { i t } ^ { f } ,$ , and $\beta _ { i t } ^ { p } )$ (Barberis et al. 1998, Park et al. 2013). Thus, because of investors’ prior beliefs, not all types of ${ \mathrm { S M A s } } ^ { \prime }$ content will be preferred or favored by investors equally; that is, investors may value more the content with specific sentiment that confirms their prior beliefs (Park et al. 2013). Because of the interactivity of social media, SMAs are able to learn about investor preferences via the correspondence between their content sentiment and their performance $( \mathrm { i . e . , } R e a d e r _ { i t }$ and Subscriber<sub>it</sub>) and engagement metrics $( \mathrm { e . g . } ,$ , Comment, Like).

Finally, we note that Control represents control variables for readership and subscriptions, whereas ${ \pmb \rho } _ { i } ^ { r }$ and $\pmb { \rho } _ { i } ^ { s }$ are the associated coefficients. We control for variables that may affect the observed free readership and paid subscriptions, including factors of prior performance $( \mathrm { e . g . }$ , readership and subscriptions in the prior period, $\mathrm { i . e . , }$ $R e a d e r _ { i t - 1 } ,$ $S u b s c r i b e r _ { i t - 1 } )$ , factors related to SMAs (e.g., numbers of followers, comments and likes received), stock market attributes (e.g., if it is a stock trading day, trade volume, volatility index, market returns in prior one day and prior one month), and factors related to content (e.g., prediction accuracy of free and paid content, diversity and novelty of stocks covered in free and paid content, price and amount of paid content).

## 3.3.1.2. State Equations.

$$
\alpha_ {i t} ^ {\bullet} = \delta_ {i} ^ {\alpha^ {\bullet}} \alpha_ {i t - 1} ^ {\bullet} + \delta_ {i} ^ {r e t u r n ^ {\alpha^ {\bullet}}} S t o c k s R e t u r n _ {t} ^ {\bullet} + S M A _ {i} ^ {\alpha^ {\bullet}} + \tau_ {t} ^ {\alpha^ {\bullet}} + \zeta_ {i t} ^ {\alpha^ {\bullet}}\tag{4}
$$

$$
\beta_ {i t} ^ {\bullet} = \delta_ {i} ^ {\beta^ {\bullet}} \beta_ {i t - 1} ^ {\bullet} + \delta_ {i} ^ {r e t u r n ^ {\beta^ {\bullet}}} S t o c k s R e t u r n _ {t} ^ {\bullet} + S M A _ {i} ^ {\beta^ {\bullet}} + \tau_ {t} ^ {\beta^ {\bullet}} + \zeta_ {i t} ^ {\beta^ {\bullet}}\tag{5}
$$

Investor preferences for sentiment $\left( \mathrm { i . e . , ~ } \alpha _ { i t } ^ { \bullet } \right.$ and $\beta _ { i t } ^ { \bullet 1 6 }$ in Equations (1) and (2)) are latent states,<sup>17</sup> as in the state- $\cdot ^ { 1 7 }$ space model literature (Kitagawa 1996). Equations (4) and (5) depict the evolution pattern of investor preferences, which is influenced by the values from the previous period $( \mathrm { i . e . } , \ \alpha _ { i t - 1 } ^ { \bullet }$ and $\dot { \beta } _ { i t - 1 } ^ { \bullet } ) .$ , returns of the stocks covered in SMA i’s free content $( \mathrm { i . e . }$ $S t o c k s R e t u r n _ { t } ^ { f } )$ and paid content $( \mathrm { i . e . }$ , StocksReturn<sup>p</sup>), SMA fixed effects $( \mathrm { i . e . , }$ $\mathsf { \bar { \Lambda } } _ { S M A _ { i } ^ { \alpha ^ { f } } , \ S M A _ { i } ^ { \beta ^ { f } } }$ , and $S M A _ { i } ^ { \beta ^ { p } } )$ , and time-specific trends $( \mathrm { i . e . , } \tau _ { t } ^ { \alpha ^ { f } } , \tau _ { t } ^ { \beta ^ { f } }$ , and $\tau _ { t } ^ { \beta ^ { p } } ) . \delta _ { i } ^ { \alpha ^ { \bullet } }$ and $\delta _ { i } ^ { \beta ^ { \bullet } }$ measure the carryover effects of respective preferences from the last period to the current one. If the carryover effect is not equal to 1, then the value of investor preference at period t is systematically different from that at period t-1. $\mathbf { \Delta } ^ { \star } \tau _ { t } ^ { \alpha ^ { f } } , \tau _ { t } ^ { \beta ^ { f } }$ , and $\tau _ { t } ^ { \beta ^ { p } }$ are modeled as time fixed effects. The inclusion of $\tau _ { t } ^ { \bullet }$ enables us to control for the scenario that market-level (e.g., stock market crash) or platform-level events $( \mathrm { e . g . }$ , a sudden inflow of investors) on a given day may affect the investor preferences for all of SMAs’ content systematically.

Similar to other state-space models, Equations (4) and (5) contain initial states, that is, $\alpha _ { i 0 } ^ { \bullet }$ and $\beta _ { i 0 } ^ { \bullet } ,$ , that denote investor preferences and time-specific trends at time $0 ,$ which is unobserved to us but can be estimated. By including and estimating initial states, we can control for the likely case that different SMAs face different initial conditions $( \mathrm { e . g . }$ ., SMAs join the platform at different time periods and with different groups of investors).

3.3.2. Supply Side. The main aim of the supply-side model is to capture the influence of time-varying investor preferences on SMAs’ content generation and monetization. To model an SMA’s content monetization decision, we use a discrete variable, Monet $\dot { z } e _ { i t } ,$ to denote an SMA’s decision to monetize content $( \mathrm { i . e . , }$ whether to produce paid content) on a given day.<sup>18</sup> Mone $i z e _ { i t }$ is then a function of a continuous latent variable Monetize<sup>∗</sup> , as follows:

$$
M o n e t i z e _ {i t} = \left\{ \begin{array}{l l} 1 & \text { if } M o n e t i z e _ {i t} ^ {*} > 0 \\ 0 & \text { if } M o n e t i z e _ {i t} ^ {*} \leq 0 \end{array} \right.\tag{6}
$$

$$
M o n e t i z e _ {i t} ^ {*} = \kappa_ {i 0} + \kappa_ {i 1} E (R e a d e r _ {i t}) + \kappa_ {i 2} E (S u b s c r i b e r _ {i t})
$$

$$
+ \eta_ {i} ^ {m} C o n t r o l + \pi_ {i t} ^ {m}\tag{7}
$$

We then specify SMAs’ content generation decisions for the sentiment of their free and paid content<sup>19</sup> as

$$
F r e e S e n t i m e n t _ {i t} = \gamma_ {i 0} + \gamma_ {i 1} \alpha_ {i t} ^ {f} + \gamma_ {i 2} \beta_ {i t} ^ {f} + \boldsymbol {\eta} _ {i} ^ {f} C o n t r o l + \pi_ {i t} ^ {f}\tag{8}
$$

$$
P a i d S e n t i m e n t _ {i t} \mid (M o n e t i z e _ {i t} = 1) = \lambda_ {i 0} + \lambda_ {i 1} \beta_ {i t} ^ {p} + \boldsymbol {\eta} _ {i} ^ {p} C o n t r o l + \pi_ {i t} ^ {p}\tag{9}
$$

The key feature of our supply-side model is that we include investor preference $\mathsf { \Omega } _ { 3 } ^ { 2 0 } \left( \mathrm { i . e . , } E ( R e a d e r _ { i t } ) \right.$ , E(Subscri-$b e r _ { i t } ) , \alpha _ { i t } ^ { f } , \beta _ { i t } ^ { f } ,$ , and $\boldsymbol { \beta } _ { i t } ^ { p } )$ as explanatory variables in SMAs content generation and monetization decisions. ${ \bf \Phi } ^ { 2 1 } { \bf \Phi } \gamma _ { i 0 }$ and $\lambda _ { i 0 }$ denote the extent of unbiased or independent opinion-expression of SMAs in generating free and paid content sentiments. $\kappa _ { i 1 } \left( \kappa _ { i 2 } \right)$ indicates the extent to which an SMA utilizes the information about expected readership (subscriptions) when monetizing content. $\gamma _ { i 1 } \left( \gamma _ { i 2 } \right)$ reveals the extent to which an SMA caters to the preferences of readers (subscribers) for free content sentiment when deciding on its value during content generation, whereas $\lambda _ { i 1 }$ gauges the extent of catering to subscribers preference for paid content sentiment when generating paid content. Thus, the sign and significance of coefficients κ<sub>i1</sub>, κ<sub>i2</sub>, $\gamma _ { i 1 } , \gamma _ { i 2 }$ , and $\lambda _ { i 1 }$ can uncover the extent to which SMAs are strategic in content generation and monetization.

By including investor preferences for content sentiment in an SMA’s content generation decisions, our model implies that the observed sentiment level of the SMA’s content may deviate from the price movement direction of the stocks covered. Moreover, the observed sentiment level may result from an SMA’s effort to cater to his or her audience’s preferences, because doing so might improve the $\mathrm { S M A } ^ { \prime } \mathrm { s }$ performance metrics $( \mathrm { e . g . , }$ increase readership or subscriptions). A potential negative consequence for investors to read such catered content is that investors’ confirmation bias may be aggravated. Therefore, investors’ prior (potentially biased) belief about stock market movements is not corrected by new information but instead reinforced by SMAs tailored content. We further explore this implication of SMAs’ strategic behaviors in Section 5.2.

Finally, we use Control to denote the control variables used in the supply-side equations, and $\pmb { \eta } _ { i } ^ { m } , \pmb { \eta } _ { i } ^ { f } ,$ , and $\pmb { \eta } _ { i } ^ { p }$ are the corresponding coefficients. We account for variables that may affect the content generation and monetization decisions, including factors of prior performance $( \mathrm { e . g . }$ , readership and subscriptions in the last period), factors related to SMAs (e.g., numbers of followers, comments, and likes received and the SMA’s tenure on the platform), and factors related to the stock market $( \mathrm { e . g . }$ ., whether it is a stock-trading day, trade volume, volatility index, returns of stocks covered, and market returns in prior one day and one month).

3.3.3. SMA Heterogeneity. Different SMAs may have different groups of investors to cater to, different backgrounds, different abilities, or different strategies for content generation and monetization. It is crucial to account for this heterogeneity across SMAs in our model specification. We achieve this using the random coefficients framework (Rossi and Allenby 2003). Specifically, $\alpha _ { i 0 } ^ { \bullet } , \beta _ { i 0 } ^ { \bullet } , \pmb { \rho } _ { i } ^ { \bullet } , \delta _ { i } ^ { \bullet } , S M A _ { i } ^ { \bullet } , \kappa _ { i \bullet } , \gamma _ { i \bullet } , \lambda _ { i \bullet } ,$ , and $\eta _ { i } ^ { \bullet }$ are SMA-specific parameters. We use $\phi _ { i }$ to denote these parameters, and with this model framework, we have

$$
\phi_ {i} = \bar {\phi} Z _ {i} + \theta_ {i}\tag{10}
$$

We include an intercept in $Z _ { i } \ ( { \mathrm { i . e . , } } Z _ { i } = [ 1 ] )$ . Therefore, $\bar { \phi }$ is the population-level means of individual parameters. In this way, we can account for the unobserved SMA heterogeneity. Lastly, $\epsilon _ { i t } ^ { \bullet } , \zeta _ { i t } ^ { \bullet } , \pi _ { i t } ^ { \bullet } ,$ , and $\theta _ { i }$ are normally distributed random errors such that $\epsilon _ { i t } ^ { \bullet } \sim M V N ( 0 , V )$ 1 $\zeta _ { i t } ^ { \bullet } \sim M V N ( 0 , W ) , \pi _ { i t } ^ { \bullet } \sim M V N ( 0 , \Omega ) , ^ { 2 2 }$ and $\theta _ { i } \sim M V N ( 0 , \Gamma )$ In summary, our key model variables and parameters are summarized in Table 5.

3.4. Identification Strategy and Model Estimation In our study, various sources of potential endogeneit bias can arise, such as SMAs’ content generation and monetization decisions being subject to their knowledge of investor preferences (which we evaluate in our research questions) and to unobserved influences $( \mathrm { e . g . , }$ omitted variables, self-selection), beyond the focal and control factors accounted for in our proposed model. If this is indeed the case, the investor preference parameters $\left( \mathrm { i . e . , } \alpha _ { i t } ^ { \bullet } \right.$ and $\beta _ { i t } ^ { \bullet } )$ and SMA response parameters $( \mathrm { i . e . , ~ } \kappa _ { i \bullet } , \gamma _ { i \bullet } ,$ and $\lambda _ { i \bullet } )$ are likely biased. To control for potential endogeneity bias, we propose to follow the framework of nonrandom marketing-mix variables (Bronnenberg and Mahajan 2001, Manchanda et al. 2004), which leverages the full likelihood of the data, the power of Bayesian inference, and data augmentation to account for any form or source of endogeneity through the violation of the independence between a model’s residual error term and the focal independent variables.

Table 5. Key Variables and Parameters in the Empirical Mode

<table><tr><td>Variable; parameter</td><td>Definition</td></tr><tr><td> $Subscriber_{it}^{*}$ </td><td>No. of potential subscriptions for SMA  $i$  on day  $t$ </td></tr><tr><td> $SMA_{i}^{\alpha^{f}}$ ,  $SMA_{i}^{\beta^{f}}$ ,  $SMA_{i}^{\beta^{p}}$ </td><td>SMA-specific fixed effects for investor preferences</td></tr><tr><td> $\tau_{t}^{\alpha^{f}}$ ,  $\tau_{t}^{\beta^{f}}$ ,  $\tau_{t}^{\beta^{p}}$ </td><td>Time-specific evolution trend for investor preferences</td></tr><tr><td> $E(Reader_{it}); \kappa_{i1}$ </td><td>Expected readership, measuring general content consumption preferences of free readers; SMA  $i$ &#x27;s degree of catering to free readers in content monetization</td></tr><tr><td> $E(Subscriber_{it}); \kappa_{i2}$ </td><td>Expected subscriptions, measuring general content consumption preferences of paid subscribers; SMA  $i$ &#x27;s degree of catering to paid subscribers in content monetization</td></tr><tr><td> $\alpha_{it}^{f}; \gamma_{i1}$ </td><td>Free readers&#x27; (time-varying) preference for free content sentiment parameter; SMA  $i$ &#x27;s degree of catering to free readers in free content generation</td></tr><tr><td> $\beta_{it}^{f}; \gamma_{i2}$ </td><td>Paid subscriber&#x27;s (time-varying) preference for free content sentiment parameter; SMA  $i$ &#x27;s degree of catering to paid subscribers in free content generation</td></tr><tr><td> $\beta_{it}^{p}; \lambda_{i1}$ </td><td>Paid subscriber&#x27;s (time-varying) preference for paid content sentiment parameter; SMA  $i$ &#x27;s degree of catering to paid subscribers in paid content generation</td></tr><tr><td> $\delta_{i}^{\bullet}$ </td><td>Carryover effects of investor preferences at time  $t-1$  to those at time  $t$ </td></tr></table>

We provide more discussion of this framework in the Online Appendix. The key idea of this framework is to explicitly account for the demand-side response parameters (e.g., investor preferences) in the supply-side decisions $( \mathrm { e . g . }$ , content generation and monetization decisions) and estimate the demand and supply sides jointly. This method of inference is fully Bayesian and does not rely on the existence of valid instruments and asymptotic approximations (Manchanda et al. 2004). This framework has been adopted by many prior studies to handle the strategic behaviors of firms and others, such as Musalem et al. (2008), Van Diepen et al. (2009), Li et al. (2011), Luo and Kumar (2013), Schweidel and Knox (2013), and Nair et al. (2017).

Our proposed model is estimated using the Bayesian approach. To complete the model, we use standard diffuse priors for all the model parameters. A hierarchical Bayesian approach is used to estimate the proposed model, which is a common approach to estimate the individual-specific model parameters (Rossi and Allenby 2003). A Markov Chain Monte Carlo (MCMC) procedure is developed to make draws from the full conditional distributions of the joint posterior distribution of the parameters (see the online Appendix). To estimate the timevarying parameters $( \alpha _ { i t } ^ { \bullet } , \beta _ { i t } ^ { \bullet } ) _ { i }$ , we use the forward filter and backward sampling (FFBS) method (see Kalman filtering techniques in Lindsten and Scho¨n 2013). Given the complexity of the model, we test the identification of the parameters on a simulated data set. Our simulation result, presented in the Online Appendix, shows that the proposed model can recover the true parameter values reasonably well. We run an MCMC chain with 20,000 iterations and use the last 5,000 iterations to compute the posterior means and standard deviations for the estimated model coefficients and the covariance matrices.

## 4. Empirical Analysis and Findings

The focus of this paper is to identify the extent of the strategic behaviors of SMAs such that SMAs may cater their content production decisions according to investors’ changing preferences. An important premise here is that investors have time-varying preferences for financial social media content. To ascertain this, we present relevant demand-side results<sup>23</sup> that can demonstrate the time-varying nature of investor preferences. We also discuss the difference between free readers’ and paid subscribers’ preferences<sup>24</sup> in the Online Appendix.

## 4.1. Identifying Strategic Behaviors in SMAs’ Content Generation and Monetization

4.1.1. Evaluating the Extent of Strategic Behaviors. The model estimation results are shown in Table 6. At the population level, we find evidence of significant strategic behaviors by SMAs. First, the expected free readership has a positive effect on the decision to monetize content (coefficient � 0.180, marginal effect � 0.008, p < 0.01). However, the expected paid subscriptions have a negative effect $\mathrm { ( c o e f f i c i e n t = - 0 . 4 8 4 }$ , marginal effect � $- 0 . 0 2 0 , p < 0 . 0 1 )$ ) on the content monetization decision. Thus, SMAs’ decision to monetize content is strategic; that is, they are more likely to monetize content (exclu sive to paid subscribers) when the expected free readership is increasing and when the expected paid subscriptions are declining. Monetizing content will hurt the interest of free readers because part of an SMA’s content will not be accessible to them because of the paywall. Interestingly, SMAs seem to monetize content in a way that brings more free readers instead of driving free readers away. Conversely, SMAs appear to decrease content monetization when expected paid sub scribers increase. In other words, SMAs appear to monetize content when the expected paid subscriptions decline. Thus, in general, SMAs’ monetization decisions do not aim to increase the number of subscribers but try to keep the number of subscribers from falling. Paid subscribers’ interest (e.g., wanting to consume more paid content) seems to be sacrificed to some extent in the monetization decision. SMAs’ differential treatment to free readers and paid subscribers suggests that SMAs are trading off the interests of free readers and paid subscribers in the monetization decision.

Table 6. Supply-Side Population-Level Estimates

<table><tr><td>Factor type</td><td>Variable</td><td>Monetize</td><td>FreeSentiment</td><td>PaidSentiment</td></tr><tr><td rowspan="5">Investor preferences</td><td> $E(Reader_{it})$ </td><td>0.180***(0.031)</td><td></td><td></td></tr><tr><td> $E(Subscriber_{it})$ </td><td>-0.484***(0.053)</td><td></td><td></td></tr><tr><td> $\alpha_{it}^{f}$ </td><td></td><td>-0.018***(0.006)</td><td></td></tr><tr><td> $\beta_{it}^{f}$ </td><td></td><td>0.090***(0.006)</td><td></td></tr><tr><td> $\beta_{it}^{p}$ </td><td></td><td></td><td>0.067***(0.023)</td></tr><tr><td rowspan="14">Control</td><td>Intercept</td><td>-2.042***(0.114)</td><td>0.354***(0.021)</td><td>0.271***(0.069)</td></tr><tr><td>ReaderLag</td><td>-0.077(0.044)</td><td>0.004(0.013)</td><td>-0.006(0.047)</td></tr><tr><td>SubscriberLag</td><td>0.739***a(0.059)</td><td>-0.016(0.023)</td><td>-0.020(0.051)</td></tr><tr><td>CommentLag</td><td>-0.024(0.0170)</td><td>5 e-04(0.014)</td><td>0.007(0.047)</td></tr><tr><td>LikeLag</td><td>-0.012(0.014)</td><td>-3 e-04(0.012)</td><td>0.004(0.045)</td></tr><tr><td>FollowerLag</td><td>-0.009(0.038)</td><td>-0.013(0.023)</td><td>0.010(0.066)</td></tr><tr><td>Tenure</td><td>-0.027***(0.011)</td><td>2 e-04(0.012)</td><td>-0.004(0.043)</td></tr><tr><td>isTradeDay</td><td>1.286***(0.169)</td><td>0.017(0.019)</td><td>-0.048(0.068)</td></tr><tr><td>TradeVolume</td><td>-8 e-04(0.012)</td><td>-4 e-04(0.011)</td><td>-0.002(0.036)</td></tr><tr><td>VIX</td><td>-0.004(0.013)</td><td>4 e-04(0.012)</td><td>0.006(0.045)</td></tr><tr><td>MarketReturnPrior1D</td><td>-0.028(0.147)</td><td>0.277***(0.098)</td><td>0.258**(0.144)</td></tr><tr><td>MarketReturnPrior1M</td><td>-1.309***(0.297)</td><td>0.070***(0.026)</td><td>0.044(0.073)</td></tr><tr><td> $StocksReturn^f$ </td><td></td><td>-0.020(0.105)</td><td></td></tr><tr><td> $StocksReturn^p$ </td><td></td><td></td><td>-0.260**(0.119)</td></tr></table>

Notes. Standard deviation in parentheses. Variables with a postfix of “Lag” are lagged by one day, that is, t�1. \*Estimates significant at 90% \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.  
<sup>a</sup>Note that SubscriberLag and E(Subscriber ) differ in the direction of the effect on content monetization. We want to use expected subscription to capture the trend or expected number of subscriptions an SMA can obtain if monetizing content. On the other hand, SubscriberLag captures the past performance of an SMA. For a subscription-maximizing SMA, it is possible that higher expected subscriptions will lead to a highe monetization probability. In that case, SubscriberLag and expected subscriptions may have effects in the same direction. However, for SMAs who also care about fostering a growing reader base, an increased expected subscription may not lead to a higher monetization probability Moreover, they may increase the monetization incidence only when the expected subscriptions start to decline to maintain a sizable subscribe base. Consequently, SubscriberLag and expected subscriptions would have different effects on the monetization decision. Our empirical result suggest that SMAs are not always maximizing the number of subscriptions, and SubscriberLag and expected subscriptions having different effects on an SMA’s monetization decision is what we observe here.

Second, we find that readers’ preference for free (negative) content sentiment negatively affects the (negative) sentiment level of free content (coefficient � �0.018, marginal effect � �0.001, p < 0.01), whereas subscribers preference for free (negative) content sentiment positively affects the (negative) sentiment level of free content (coefficient � 0.090, marginal effect � 0.004, p < 0.01). Therefore, SMAs do respond to both readers’ and subscribers’ preferences in deciding the (negative) sentiment level of free content. For readers’ preferences for free (negative) content sentiment, SMAs take a contrarian approach,<sup>25</sup> whereas for subscribers’ preferences, SMAs take a catering approach. It is thus evident that the SMAs trade off readers’ and subscribers’ preferences for content sentiment when generating free content.

Third, we find that subscribers’ preference for paid (negative) content sentiment positively affects the (negative) sentiment level of paid content (coefficient � 0.067, marginal effect � 0.003, p < 0.01). As such, the (negative) sentiment level of an SMA’s paid content generated depends on the paid subscribers’ preference for it. Overall, we find that SMAs cater to investor preferences (i.e., of subscribers) when generating both paid and free content’s sentiments.

To sum up, our results that investor preferences play important roles in SMAs’ content generation and monetization decisions are in accordance with the general predictions of the catering theory (Baker and Wurgler 2004b, Baker et al. 2009). Our study also yields more nuanced findings for the scenario where SMAs face two sets of investor preferences. We find that SMAs’ content monetization decisions are more in line with free readers’ preferences, whereas content generation decisions for sentiment level are more in line with paid subscribers’ preferences. Thus, when monetizing content, SMAs care more about the growth of readers, and when generating sentiment, SMAs value the preferences of subscribers. In summary, SMAs are strategic in acquiring readers via the content monetization decision and retaining subscribers via the content generation decision.

On the control factors, intriguingly, the effects of market returns from the prior one day (coefficient � 0.277, p < 0.01) and the prior one month (coefficient � 0.070, p < 0.01) are both positive and significant for the free (negative) content sentiment decision. In other words, when the market returns are higher (i.e., more positive), the generated sentiment will be more negative. This finding shows that, on average, SMAs are taking a contrarian approach to predict the stock market;<sup>26</sup> that is, if the prior market returns are increasing, then SMAs would predict the market to move in a downward direction. In addition, the effect of market returns from the prior day is stronger than that from the prior month, suggesting that SMAs tend to predict market movements based on more recent information (i.e., one day).

The above findings are drawn from the populationlevel parameters. The random coefficients framework we have employed permits us to further recover the individual SMA-level parameters. We provide a discussion of the individual-level parameter estimates in the Online Appendix. Furthermore, in Section 8 of the Online Appendix, we offer more analyses to discuss SMAs’ optimization strategies for free readership and paid subscriptions. Specifically, for 97.57% of observations, SMAs’ content generation and monetization decisions are consistent with neither the readership-optimizing strategies nor the subscription-maximizing strategies but are mainly strategic responses to the changes in the demand side (e.g., investor preferences). In addition, for those SMAs who engage in readership optimizing and subscription maximizing, we find that they first maximize or build up the free readership and then adopt monetization actions later on the acquired investor or readership base.

4.1.2. Robustness Checks. To ensure the robustness of our results, we conduct several further analyses. First, in our model, we use the framework of nonrandom marketing-mix variables to address the main endogene ity issue between SMAs’ content production decisions and investor preferences or unobserved influences. As a robustness check, we further include latent instrumental variables (LIV) in our model to correct for any remaining endogeneity bias (Ebbes et al. 2005, Zhang et al. 2009, Rutz and Trusov 2011, Saboo and Grewal 2013). The LIV method is a “frugal” IV approach, thereby not requiring observed IVs. The key idea here is to introduce a binomial variable, LIV, to decompose the endog enous variable (FreeSentiment, PaidSentiment) into two components: one that is correlated with the error term of the main equation and one that is not (Ebbes et al. 2005). Results in Column (1) of Table 7 show that the focal model coefficients are largely consistent with those of our main model in Table 6.

Second, producing free content is another supply side decision of SMAs. Because the focus of this paper is SMAs’ content generation and monetization decisions, as we mentioned in Footnote 18, we do not model this decision to avoid overcomplicating our empirical model. Here, we show that our results are robust to the potential sample selection bias as a result of not explicitly modeling the free content production decision. We employ the two-stage Heckman model estimation method to insert the inverse Mills ratio of the free content production decision into the current supply-side decisions. We find that the estimated model coefficients from this method, as shown in Column (2) of Table 7, are quite similar to those of our main results.

Third, to verify whether SMAs’ anticipated readership and subscription numbers could influence the sentiment level of free and paid content generated, we tested an alternative specification by adding the expected readership and subscriptions (i.e., E(Reader ), $E ( \bar { S } u b s c r i b e r _ { i t } ) )$ ) into the content generation decisions (i.e., FreeSentiment and PaidSentiment). We find no evidence of such effects in Column (3) of Table 7, whereas the focal model coefficients are again consistent with those of our main model.

Fourth, to rule out SMAs’ capacity constraint as an alternative explanation of our key findings (e.g., lack of time or writing resources to generate more paid content as subscriptions rise), we include in our supply-side model the average number of pieces of content authored by an SMA in the prior seven days to serve as a proxy for the content capacity of an SMA. This alternative explanation is largely ruled out because we see that the results in Column (4) of Table 7 remain stable and consistent with those in Table 6.

Fifth, we acknowledge that investors’ content consumption behaviors (and SMAs’ content production decisions) could be sensitive to investors’ risk preferences, besides the preference for content itself. We note that investors’ risk preferences refer to their tendency to avoid, be neutral to, or seek risk, which is tied to the volatility $( \mathrm { i . e . , }$ standard deviation) of a stock’s price (Roll 1984), whereas preferences for content sentiment are about the expected or projected movement direction or trend $( \mathrm { e . g . , }$ bullish or bearish) of a stock’s price. To control for the potential effect of investors’ risk preferences on their content consumption behaviors, we conduct another robustness check by including the volatility of the stocks (as measured by the average standard deviation of the stocks’ returns in the past one week) covered in an SMA’s free and paid content into the evolution of investors’ preferences for the free and paid content sentiment $( \mathrm { i . e . , }$ Equations (4) and (5)). Results in Column (5) of Table 7 show that the focal model coefficients are again consistent with those of our main model.

Table 7. Robustness Checks

<table><tr><td>Equation</td><td>Variable</td><td>(1) Latent IV</td><td>(2) Produce free content</td><td>(3) Alternative specification</td><td>(4) Capacity constraint</td><td>(5) Risk preference</td></tr><tr><td rowspan="3">Monetize</td><td> $E(Reader_{it})$ </td><td>0.103***(0.032)</td><td>0.137***(0.027)</td><td>0.099***(0.030)</td><td>0.116***(0.033)</td><td>0.099**(0.063)</td></tr><tr><td> $E(Subscriber_{it})$ </td><td>-0.282***(0.055)</td><td>-0.364***(0.052)</td><td>-0.325***(0.049)</td><td>-0.228***(0.081)</td><td>-0.179***(0.049)</td></tr><tr><td>InverseMillsRatio</td><td></td><td>-1.041***(0.166)</td><td></td><td></td><td></td></tr><tr><td rowspan="5">FreeSentiment</td><td> $E(Reader_{it})$ </td><td></td><td></td><td>0.007(0.007)</td><td></td><td></td></tr><tr><td> $E(Subscriber_{it})$ </td><td></td><td></td><td>-0.003(0.008)</td><td></td><td></td></tr><tr><td> $\alpha_{it}^{f}$ </td><td>-0.018***(0.006)</td><td>-0.017***(0.007)</td><td>-0.027***(0.007)</td><td>-0.018***(0.006)</td><td>-0.017**(0.006)</td></tr><tr><td> $\beta_{it}^{f}$ </td><td>0.092***(0.006)</td><td>0.093***(0.006)</td><td>0.098***(0.007)</td><td>0.092***(0.006)</td><td>0.090***(0.006)</td></tr><tr><td>InverseMillsRatio</td><td></td><td>0.053(0.091)</td><td></td><td></td><td></td></tr><tr><td rowspan="4">PaidSentiment</td><td> $E(Reader_{it})$ </td><td></td><td></td><td>0.005(0.024)</td><td></td><td></td></tr><tr><td> $E(Subscriber_{it})$ </td><td></td><td></td><td>-0.023(0.028)</td><td></td><td></td></tr><tr><td> $\beta_{it}^{p}$ </td><td>0.061***(0.022)</td><td>0.040*(0.023)</td><td>0.058***(0.025)</td><td>0.055***(0.021)</td><td>0.045**(0.023)</td></tr><tr><td>InverseMillsRatio</td><td></td><td>-0.183(0.179)</td><td></td><td></td><td></td></tr></table>

Notes. Standard deviation in parenthesis. For the sake of brevity, only the essential results are presented. \*Estimates significant at $9 0 \% ;$ \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.

## 4.2. Quantifying the Tradeoffs in Strategic Behaviors

In the prior section, we present evidence showing that SMAs are balancing the interests of free readers and paid subscribers in their content generation and monetization decisions. Here, to quantify the trade-offs in SMAs’ content generation and monetization, we interact expected readership with expected subscriptions and, likewise, free readers’ preference for free content sentiment with paid subscribers’ preference for free content sentiment in Equations (7) and (8).

From the results in Table 8, we find that the interaction effect of expected free readership and expected paid subscriptions is positive on the monetization decision $( \mathrm { c o e f f i c i e n t } = 0 . 0 7 7 , p < 0 . 0 1 )$ . Therefore, the effect of expected readership on the monetization decision becomes $0 . 1 0 4 + 0 . 0 7 7 \stackrel { . } { ^ { * } }$ E(Subscriber ), which depends on the strength of expected subscriptions (i.e., E(Subscriber )). Therefore, when expected subscriptions increase, the effect of expected readership also increases. In other words, when expected subscriptions increase, SMAs increase the catering to free readers in the monetization decision. However, the effect of expected subscriptions on the monetization decision is $- 0 . { \overset { - } { 4 } } 2 5 + 0 . 0 7 7 \cdots$ E(Read-$e r _ { i t } )$ . Thus, as expected readership increases, the negative effect of expected subscriptions on the monetization decision is attenuated. Thus, with a growing free readership, SMAs no longer need to sacrifice the interest of paid subscribers too much (i.e., low monetization probability will hurt the interest of subscribers) to cater to free readers in the monetization decision.

We also find that the interaction effect of readers’ preference and subscribers’ preference for free content sentiment in the sentiment decision for free content is negative (coefficient $= - 0 . 0 2 0 , p < 0 . 0 1 )$ ). The effect of readers’ preferences on the sentiment level of free content becomes $- 0 . 0 5 8 - 0 . 0 2 0 \ ^ { * } \beta _ { i t } ^ { f } ,$ depending on the strength of subscribers’ preferences for free content sentiment. Thus, as subscribers’ preferences increase, the original negative effect of readers’ preferences becomes even more negative, suggesting that SMAs will take an even stronger contrarian approach; that is, readers’ preferences are held in higher or more opposite disregard with respect to free content sentiment decisions. In contrast, the effect of subscribers’ preferences on the sentiment level of free content becomes $0 . 1 0 6 - 0 . 0 2 0 ~ ^ { * } \alpha _ { i t } ^ { f } ,$ depending on the strength of readers’ preferences for free content sentiment. Thus, this implies that as readers’ preferences increase, SMAs will cater less to subscribers’ preferences for free content sentiment.

Table 8. Strategic Behaviors and Tradeoff

<table><tr><td colspan="2">Monetize</td><td colspan="2">FreeSentiment</td><td colspan="2">PaidSentiment</td></tr><tr><td>Variable</td><td>Coefficient</td><td>Variable</td><td>Coefficient</td><td>Variable</td><td>Coefficient</td></tr><tr><td> $E(Reader_{it})$ </td><td>0.104***(0.052)</td><td> $\alpha^{f}_{it}$ </td><td>-0.058***(0.006)</td><td> $\beta^{p}_{it}$ </td><td>0.029***(0.011)</td></tr><tr><td> $E(Subscriber_{it})$ </td><td>-0.425***(0.102)</td><td> $\beta^{f}_{it}$ </td><td>0.106***(0.007)</td><td></td><td></td></tr><tr><td> $E(Reader_{it}) * E(Subscriber_{it})$ </td><td>0.077***(0.020)</td><td> $\alpha^{f}_{it} * \beta^{f}_{it}$ </td><td>-0.020***(0.006)</td><td></td><td></td></tr></table>

Notes. Standard deviation in parentheses. \*Estimates significant at 90%; \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.

Taken together, in both the content monetization decision and the generation decision for free content sentiment, we observe both a complementarity effect (i.e., positive moderation) and a substitution effect (i.e., negative moderation) in the moderating roles of paid subscribers’ and free readers’ preferences, respectively. First, the preferences of paid subscribers have a complementarity relationship with the effect of free readers’ preferences on monetization (i.e., positive effect is strengthened) and free content sentiment $( \mathrm { i . e . , }$ negative effect is accentuated). Second, and more interestingly, the preferences of free readers have a substitution relationship with the effect of paid subscribers’ preferences on monetization $( \mathrm { i . e . , }$ negative effect is weakened) and free content sentiment (i.e., positive effect is diminished), which demonstrates that SMAs are indeed balancing and trading off the preferences of free readers and paid subscribers. Thus, the sentiment of financial social media content is not a mere reflection or prediction of stock market movements, as shown in studies on the informative value of financial social media content (Das and Chen 2007, Sabherwal et al. 2008, Luo et al. 2013, Chen et al. 2014), but also a result of SMAs’ reaction to investor preferences. Further analysis shows that SMAs’ strategic behaviors (i.e., catering to and trading off investor preferences) explain 46.20% (24.50%) of the variance in SMAs’ free (paid) content sentiment decisions, whereas stock market conditions and prior performance of SMAs together explain 44.54% (75.29%). Therefore, SMAs exhibit more strategic behaviors in generating free content relative to paid content, which is understandable because free content is consumed by both free readers and paid subscribers, thus involving more strategic considerations.

## 4.3. Underlying Mechanism of SMAs’ Strategic Behaviors: Audience Composition Effect

Our main results suggest that SMAs cater to free readers and paid subscribers’ preferences differently in their content generation and monetization decisions. Although the catering theory (Baker and Wurgler 2004b, Baker et al. 2009) does not inform the situation where SMAs face multiple investor preferences, we provide a natural extension to the catering theory regarding the relative salience of catering incentives. That is, SMAs may increase the catering to readers’ preferences when readers’ preferences are more salient but also increase the catering to subscribers’ preferences when subscribers preferences are more salient. We then propose that the composition of an SMA’s investor audience base can regulate the direction of an SMA’s catering behaviors.

To test the mechanism, we construct a variable that reflects the change in the composition of an SMA’s audience. Specifically, we define SubscriberReaderRatioLag, which measures the ratio of the number of subscribers to that of readers on the previous day. A higher SubscriberReaderRatioLag suggests a higher proportion of subscribers in an SMA’s audience base. Hence, subscribers preferences will be more salient to the SMA. We interact this variable with investor preferences in the content generation and monetization equations below:

$$
\begin{array}{r l} M o n e t i z e _ {i t} ^ {*} = & \kappa_ {i 0} + \kappa_ {i 1} E (R e a d e r _ {i t}) + \kappa_ {i 2} E (S u b s c r i b e r _ {i t}) \\ & + \kappa_ {i 3} (E (R e a d e r _ {i t}) * S u b s c r i b e r R e a d e r R a t i o L a g _ {i t}) \\ & + \kappa_ {i 4} (E (S u b s c r i b e r _ {i t}) * S u b s c r i b e r R e a d e r R a t i o L a g _ {i t}) \\ & + \kappa_ {i 5} S u b s c r i b e r R e a d e r R a t i o L a g _ {i t} + \pmb {\eta} _ {i} ^ {m} C o n t r o l + \pi_ {i t} ^ {m} \end{array}\tag{11}
$$

$$
\begin{array}{r l} F r e e S e n t i m e n t _ {i t} = & \gamma_ {i 0} + \gamma_ {i 1} \alpha_ {i t} ^ {f} + \gamma_ {i 2} \beta_ {i t} ^ {f} \\ & + \gamma_ {i 3} (\alpha_ {i t} ^ {f} * S u b s c r i b e r R e a d e r R a t i o L a g _ {i t}) \\ & + \gamma_ {i 4} (\beta_ {i t} ^ {f} * S u b s c r i b e r R e a d e r R a t i o L a g _ {i t}) \\ & + \gamma_ {i 5} S u b s c r i b e r R e a d e r R a t i o L a g _ {i t} \\ & + \pmb {\eta} _ {i} ^ {f} C o n t r o l + \pi_ {i t} ^ {f} \end{array}\tag{12}
$$

Table 9. Strategic Behaviors and Audience Composition Effect (Part 1)

<table><tr><td colspan="2">Monetize</td><td colspan="2">FreeSentiment</td><td colspan="2">PaidSentiment</td></tr><tr><td>Variable</td><td>Coeff.</td><td>Variable</td><td>Coefficient</td><td>Variable</td><td>Coefficient</td></tr><tr><td> $E(Reader_{it})$ </td><td>0.069*(0.037)</td><td> $\alpha^{f}_{it}$ </td><td>-0.020**(0.008)</td><td> $\beta^{p}_{it}$ </td><td>0.059**(0.029)</td></tr><tr><td> $E(Subscriber_{it})$ </td><td>-0.293***(0.056)</td><td> $\beta^{f}_{it}$ </td><td>0.109***(0.008)</td><td> $\beta^{p}_{it}$ *SubscriberReaderRatioLag</td><td>-2 e-04(0.080)</td></tr><tr><td> $E(Reader_{it})$ *</td><td>-0.266**(0.129)</td><td> $\alpha^{f}_{it}$ *SubscriberReaderRatioLag</td><td>-0.009(0.042)</td><td>SubscriberReaderRatioLag</td><td>0.007(0.116)</td></tr><tr><td> $E(Subscriber_{it})$ *</td><td>0.360***(0.072)</td><td> $\beta^{f}_{it}$ * SubscriberReaderRatioLag</td><td>0.103**(0.057)</td><td></td><td></td></tr><tr><td>SubscriberReaderRatioLag</td><td>-0.098(0.095)</td><td>SubscriberReaderRatioLag</td><td>0.053(0.068)</td><td></td><td></td></tr></table>

Notes. Standard deviation in parentheses. \*Estimates significant at 90%; \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.

$$
P a i d S e n t i m e n t _ {i t} \mid (M o n e t i z e _ {i t} = 1) = \lambda_ {i 0} + \lambda_ {i 1} \beta_ {i t} ^ {p}
$$

$$
+ \lambda_ {i 2} (\beta_ {i t} ^ {p} * S u b s c r i b e r R e a d e r R a t i o L a g _ {i t})
$$

$$
+ \lambda_ {i 3} S u b s c r i b e r R e a d e r R a t i o L a g _ {i t} + \pmb {\eta} _ {i} ^ {p} C o n t r o l + \pi_ {i t} ^ {p}\tag{13}
$$

From the results in Table 9, we find that SubscriberReaderRatioLag negatively moderates the effect of expected readership on the content monetization decision but positively moderates the effect of the expected subscriptions on the monetization decision. SubscriberReaderRatioLag also positively moderates the effect of subscribers’ preferences for free content sentiment on the content generation decision of free content sentiment. Therefore, we find that SubscriberReaderRatioLag intensifies SMAs’ catering to paid subscribers in the free content generation decision but reduces the catering to free readers in the monetization decision when the audience ratio of subscribers is higher, thus supporting our argument on the relative salience of audience preferences.

As another test, we define SubscriberFollowerRatioLag, which measures the ratio of the number of subscribers to that of followers on the previous day. We then replace

SubscriberReaderRatioLag in Equations (11)�(13) with SubscriberFollowerRatioLag and re-estimate the model. From Table 10, we find that SubscriberFollowerRatioLag negatively moderates the effect of expected readership on the monetization decision and positively moderates the effect of subscribers’ preferences for free content sentiment on the content generation decision of free content sentiment. Taken together, we find that as the ratio of the number of subscribers to that of followers increases, SMAs reduce the catering to free readers in the monetization decision and accentuate the catering to paid subscribers in the free content generation decision, which is also in line with our proposed mechanism above.

## 5. Contributions and Implications 5.1. Theoretical Contributions

Our study makes the following theoretical contributions. First, to the best of our knowledge, our study is the first attempt to document how investor preferences (Guiso et al. 2018) influence SMAs’ strategic content generation in terms of content sentiment. The majority of prior literature on financial social media has focused only on assessing the informational value of social media content in predicting stock markets (Das and Chen 2007, Sabherwal et al. 2008, Luo et al. 2013, Chen et al. 2014) and thus has a limited understanding of how financial social media content is generated in the first place. We thus advance the literature on financial social media by investigating the supply or generation of financial social media content by SMAs. We find novel evidence that, unlike in the offline setting of traditional financial markets (Morris 2001), SMAs engage in a significant extent of strategic content generation by catering to the investor preferences of their audience base, especially those of paid subscribers in terms of their preferences for both free and paid content sentiment.

Table 10. Strategic Behaviors and Audience Composition Effect (Part 2)

<table><tr><td colspan="2">Monetize</td><td colspan="2">FreeSentiment</td><td colspan="2">PaidSentiment</td></tr><tr><td>Variable</td><td>Coefficient</td><td>Variable</td><td>Coefficient</td><td>Variable</td><td>Coeff.</td></tr><tr><td> $E(Reader_{it})$ </td><td>0.099***(0.037)</td><td> $\alpha^{f}_{it}$ </td><td>-0.017**(0.008)</td><td> $\beta^{p}_{it}$ </td><td>0.054*(0.028)</td></tr><tr><td> $E(Subscriber_{it})$ </td><td>-0.330***(0.055)</td><td> $\beta^{f}_{it}$ </td><td>0.100***(0.008)</td><td> $\beta^{p}_{it}$ *</td><td>-0.132</td></tr><tr><td> $E(Reader_{it})$ *</td><td>-0.940***(0.190)</td><td> $\alpha^{f}_{it}$ *</td><td>-0.035</td><td> $SubscriberFollowerRatioLag$ </td><td>-0.035(0.299)</td></tr><tr><td> $SubscriberFollowerRatioLag$ </td><td>(0.190)</td><td> $SubscriberFollowerRatioLag$ </td><td>(0.136)</td><td></td><td></td></tr><tr><td> $E(Subscriber_{it})$ *</td><td>0.317</td><td> $\beta^{f}_{it}$ *</td><td>0.209***</td><td></td><td></td></tr><tr><td> $SubscriberFollowerRatioLag$ </td><td>(0.265)</td><td> $SubscriberFollowerRatioLag$ </td><td>(0.075)</td><td></td><td></td></tr><tr><td> $SubscriberFollowerRatioLag$ </td><td>-0.550***(0.051)</td><td> $SubscriberFollowerRatioLag$ </td><td>0.534***(0.082)</td><td></td><td></td></tr></table>

Notes. Standard deviation in parentheses. \*Estimates significant at 90%; \*\*estimates significant at 95%; \*\*\*estimates significant at 99%.

Second, how financial social media is monetized and what factors drive the monetization decision have seldom been studied in the prior literature. Our investigation of SMAs’ content monetization decisions fills this gap. In addition, by studying individual content contributors heterogenous monetization decisions, this study adds a timely complement to the existing content monetization and pricing literature, which has focused only on platform-level uniform monetization actions (Pauwels and Weiss 2008, Oh et al. 2016, Lambrecht and Misra 2017) and has missed the current business practices where the monetization decision is increasingly democratized to individual content contributors’ discretion.

Third, our study further advances the user-generated content literature (Tang et al. 2012, Goes et al. 2014, Shen et al. 2015, Nguyen et al. 2021) by documenting the trade-off between free readership and paid subscriptions of content contributors when making decisions on content generation and monetization. Interestingly, our study finds that an SMA is more likely to produce paid content when expected readership increases and less likely to do so when expected subscriptions increase, which clearly shows that an SMA is balancing the interests of different groups of investors. Furthermore, we find that SMAs strategically trade off the content sentiment preferences of free readers and paid subscribers in the content generation decision for sentiment, with such reactions to investor preferences accounting for 46.20% (24.50%) of the variance in SMAs’ free (paid) content sentiment decision when generating content.

Last, our study contributes to the related IS literature (Chen et al. 2019) and the catering theory (Baker and Wurgler 2004b, Baker et al. 2009) by uncovering the underlying mechanism of SMAs’ strategic behaviors observed in financial social media. We provide an extension to the catering theory (Baker and Wurgler 2004b, Baker et al. 2009) by explaining SMAs’ catering behaviors when SMAs face multiple and potentially conflicting investor preferences. Our study underscores that the composition of an SMA’s audience base regulates the orientation of the SMA’s catering behaviors toward free readers or paid subscribers.

## 5.2. Managerial Implications: Reduction of Investors’ Confirmation Bias

We have established that SMAs indeed cater to investors’, especially subscribers’, preferences, when generating content on financial social media. The behavioral finance literature suggests that investors often fall prey to confirmation bias (Park et al. 2013),<sup>27</sup> which means that investors often seek opinions that confirm their prior investment beliefs. A potential negative consequence of SMAs’ catering behaviors is that it may aggravate investors’ confirmation biases. In this subsection, we illustrate an approach to identify the SMAs who are susceptible to exacerbating investors’ confirmation bias and assess the severity of the problem. With the list of such SMAs identified, platforms can consider appropriate actions to reduce investors’ confirmation bias, with the aim to also increase the quality of content produced.

First, we examine the relation between catering to investor preferences and the ability to predict the market. It is less of a concern if the SMAs, who are more likely to cater to the investors, can also predict the market accurately, because although their content is aligned with investor preferences, it is still of high informationa value. Here, we plot the SMA-level predictive accuracy (i.e., the extent to which an SMA’s buy/sell stock recommendation corresponds to an increase/decline in stock prices the next day) and the degree of strategic catering to subscribers’ preferences for free (negative) content sentiment $( \mathrm { i . e . , } \gamma _ { i 2 } )$ in Figure 3. We see a U-shaped relation between the predictive accuracy for the next day and the catering to subscribers’ preferences. Thus, SMAs with low and high predictive accuracy are both more likely to cater to subscribers’ preferences. This result is worrisome because it suggests that a group of SMAs with low predictive accuracy are engaging in strategic catering of content to their subscribers.

Second, we examine whether investor preferences for content sentiment can predict market returns accurately. If this is the case, then SMAs’ catering to investor preferences will be acceptable because what the investors prefer is where the market moves. Hence, we plot Figure 4 to show the relation between subscribers’ preferences for free (negative) content sentiment $( \mathrm { i . e . , ~ } \beta _ { i t } ^ { f } )$ and the market return for the next day. The slope of the fitted line is virtually flat. A further t-test shows a correlation of �0.007 (p value � 0.1328). Thus, SMAs’ catering to investor preferences will not bring valuable informational content to investors.

Third, the prior two exercises suggest that there exists a group of SMAs with low predictive accuracy but yet strategically caters much to investor preferences to produce content that unfortunately does not benefit them in actual investment outcomes. Therefore, this group of SMAs is highly susceptible to worsening the confirmation bias of investors. To identify this group of SMAs, we propose the following strategy. We categorize

Figure 3. (Color online) SMAs’ Catering to Subscribers’ Preferences for Free Content Sentiment vs. Predictive Accuracy  
![](/api/attachments/26QF68QY/fulltext/images/746b3f173bc5e424fad41499811e96ca39a2d9adafbb74a26e330fc3474da19e.jpg)

SMAs’ predictive accuracy and the extent of catering to subscribers’ preference for free content sentiment into high, medium, and low levels, respectively, which generates a 3 × 3 table, as shown in Table 11. Among the nine groups of SMAs, the SMAs with low predictive accuracy and a high extent of catering to subscribers preferences (bold-faced, top-right cell in Table 11) are the SMAs we aim to identify. There are 57 of them (10.73% of all SMAs). To assess how serious the problem is, we calculate the number of visitors (both free readers and paid subscribers), the visitors per SMA, the percentage of revenue captured, and the revenue per SMA by each group of SMAs in Table 11. We find that this group of problematic SMAs attracts 9.60% (i.e., the fifthhighest share) of the total visitors and captures 3.48% of the platform’s revenue.<sup>28</sup> We also find that for the group of SMAs with low predictive accuracy, it is those with moderate catering intensity that have the most visitors per SMA and the highest revenue per SMA. This result implies that for the SMAs with low predictive accuracy, catering behaviors can only help them attract visitors and subscribers to some extent and will work counterproductively (i.e., lose visitors and subscribers) if the catering intensity becomes too high. Financial social media platform operators are thus recommended to follow our approach to identify a similar group of SMAs and take suitable actions on this group of SMAs for the purpose of resolving concerns of aggravating the confirmation bias of retail investors.

## 6. Limitations and Future Direction

Although this study has highlighted several important findings, we acknowledge some limitations. First, we consider only textual content in our study, although a small number of images or pictures do exist in the data. Nevertheless, we think that the influence of images should be minimal because they are often posted together with texts for illustrative purposes. Second, our data come from a single financial social media platform. Caution should be taken when generalizing our findings to other platforms. Still, we are confident about the representativeness of our data given the large five millionuser base of iMaibo. Third, we do not observe the offline activities between SMAs and investors. Two policies of iMaibo, however, mitigate this concern: (1) private communications between SMAs and investors are not allowed; and (2) SMAs cannot disclose personal contact information on iMaibo. Thus, the impact of offline activities between SMAs and investors on investors’ content preferences or acquisition behaviors should be negligible. Fourth, we have shown that our results are robust to several endogeneity concerns and alternative specifications. Nevertheless, we do not claim to have addressed all sources of potential endogeneity biases and thus do not make absolute causal interpretation claims.

Figure 4. (Color online) Subscribers’ Preferences for Free Content Sentiment and Market Return for the Next Day  
![](/api/attachments/26QF68QY/fulltext/images/932d603d28b7ca172c09026776f28cf5708e6c0c7a421f2e82057d2875473a03.jpg)

Table 11. Categorization of SMAs’ Predictive Accuracy vs. Strategic Behaviors

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Catering to subscribers&#x27; preferences for free content sentiment</td></tr><tr><td>Low</td><td>Medium</td><td>High</td></tr><tr><td rowspan="6">Predictive accuracy</td><td rowspan="2">Low</td><td>23</td><td>97</td><td>57</td></tr><tr><td>(visitor: 2.62%, visitor per SMA: 2,083; revenue: 3.33%, revenue per SMA: 17,611)</td><td>(visitor: 15.10%, visitor per SMA: 11,988; revenue: 4.11%, revenue per SMA: 21,743)</td><td>(visitor: 9.60%, visitor per SMA: 7,642; revenue: 3.48%, revenue per SMA: 18,433)</td></tr><tr><td rowspan="2">Medium</td><td>64</td><td>27</td><td>85</td></tr><tr><td>(visitor: 11.20%, visitor per SMA: 8,934; revenue: 15.70%, revenue per SMA: 83,057)</td><td>(visitor: 2.67%, visitor per SMA: 2,130; revenue: 41.20%, revenue per SMA: 218,134)</td><td>(visitor: 29.70%, visitor per SMA: 23,630; revenue: 2.93%, revenue per SMA: 15,485)</td></tr><tr><td rowspan="2">High</td><td>90</td><td>52</td><td>36</td></tr><tr><td>(visitor: 21.20%, visitor per SMA: 16,843; revenue: 27.90%, revenue per SMA: 147,829)</td><td>(visitor: 5.80%, visitor per SMA: 4,619; revenue: 1.26%, revenue per SMA: 6,671)</td><td>(visitor: 2.19%, visitor per SMA: 1,745; revenue: 0.04%, revenue per SMA: 186)</td></tr></table>

Moving forward, our study points to avenues for future research. First, in this paper, we have explored the specific mechanism of catering incentives that may explain the nature of strategic content generation and monetization. Future research can study other potential mechanisms to further examine the nature and drivers of strategic content production in financial social media. Second, we propose a general modeling framework to study the supply-side strategic behaviors to respond to time-varying demand-side preferences. Future researchers can apply our model to other settings, such as how online marketers adjust digital marketing intervention strategies based on consumers changing preferences to different interventions. Third, this paper has focused on financial content generation in terms of content sentiment based on a simple albeit established method of assessing the proportion of negative words. Future research can examine other content attributes or measure sentiment based on other more advanced text-mining or sentiment analysis approaches.

## Acknowledgments

The authors thank the anonymous reviewers and seminar and workshop participants at the Chinese University of Hong Kong and National University of Singapore for their valuable comments and suggestions.

## Endnotes

<sup>1</sup> https://www.similarweb.com/website/stocktwits.com/.

<sup>2</sup> https://www.nytimes.com/2021/01/28/business/gamestopstock-market.html.

<sup>3</sup> https://www.cfainstitute.org/en/ethics-standards/codes/standardsof-practice-guidance/standards-of-practice-I-B.

<sup>4</sup> https://www.quantifiedstrategies.com/writing-for-seeking-alphaalternatives/.

<sup>5</sup> We measure sentiment using the proportion of negative words in the content by following Tetlock (2007) and Tetlock et al. (2008). Therefore, a higher value suggests more negative sentiment. We

note that the proportion of negative words in a sentence has been an established measurement for sentiment in the finance literature since the seminal work of Tetlock (2007) and Tetlock et al. (2008). Tetlock (2007) found that negative words have a much stronger correlation with stock returns than other words. This finding is also consistent with a large body of literature in psychology, which documents that negative information has more impact and is more thoroughly processed than positive information across a wide range of contexts (Baumeister et al. 2001, Rozin and Royzman 2001) Besides the theoretical soundness of this measurement, Footnote 14 also establishes the empirical importance of this measurement in our context.

<sup>6</sup> By assuming that investors have preferences for content sentiment, we do not imply that investors expect a fixed level of sentiment. On the contrary, investor preferences for sentiment may change over time. Through interactions with investors on financial social media, SMAs can arguably discern such investor preferences. Therefore, we aim to examine the extent to which SMAs cater to investor preferences for content sentiment and adjust their own content generation accordingly.

<sup>7</sup> Note that Reader does not include Subscriber ; that is, free readers are counted separately from paid subscribers.

<sup>8</sup> In Equation (2), 1() denotes the indicator function, such that Paid-Sentiment is only observable and has an effect when Monetize � 1.

<sup>9</sup> On iMaibo, when an SMA does not produce paid content on a day (Monetize � 0), there will be no subscription option for investors specific to the SMA (i.e., no new subscriptions). However, it is possible that there exist some willing investors who wish to pay for subscriptions on that day but cannot do so because the SMA chooses not to monetize content on that day. Hence, using observed subscriptions to infer expected subscriptions will produce a biased estimate. The potential subscriptions augment the observed ones if Monetiz $\begin{array} { r l r } { \mathrm { ~  ~ \rho ~ } _ { { } ^ { - i t } } } & { { } = } & { 0 , } \end{array}$ , enabling a more accurate estimate of model parameters.

<sup>10</sup> When Monetize<sub>it</sub> � 0, the potential subscriptions are no smaller than the observed subscriptions. As such, Subscriber<sup>∗</sup> will be treated as a truncated normal variable (bounded by Subscriber<sub>it</sub> and +∞) in the model estimation when no paid content is produced (Monetize � 0). When an SMA produces paid content (Monetiz $e _ { i t } = 1 )$ , the potential subscriptions are equal to the observed ones.

<sup>11</sup> Note that paid content is accessible only to paid subscribers. Thus, paid sentiment enters only Equation (2).

<sup>12</sup> To construct E(Reader<sub>it</sub>) and E(Subscriber<sub>it</sub>), we follow Albuquerque et al. (2012) and calculate the two quantities while estimating the model parameters.

<sup>13</sup> We account for the role of contemporaneous sentiment in Equations (1) and (2). However, we also use alternative specifications with lagged (by one period) sentiment and obtain qualitatively sim ilar results for investor preferences of sentiment on the demand side and SMAs’ responses to these sentiment preferences on the supply side.

<sup>14</sup> We acknowledge that sentiment is not the only important informational aspect of financial content. Our demand-side results (see Table A8 of the Online Appendix) find that diversity, novelty, and accuracy are largely insignificant in the readership and subscription equations. We also conducted an analysis by linking additional informational aspects $( \mathrm { e . g . }$ , novelty, diversity) to investors’ login and subscription decisions. We find that sentiment also has the strongest effect on such decisions (this result can be provided upon request). Overall, the empirical results suggest that sentiment is a more important content aspect than diversity, novelty, and accuracy that affects investor behaviors. Thus, SMAs need to pay more atten tion to the sentiment aspect than others.

<sup>15</sup> In this paper, we regard sentiment as the reflection of SMAs’ prediction about the market or stocks’ directions. Sentiment has two effects on investors’ behaviors: (1) Accuracy effect, which means the extent to which an SMA’s sentiment is consistent with the market direction. A perfectly rational investor is expected to read and/or subscribe more to the SMA whose content sentiment is more consistent with the market or stock directions. (2) Preference effect, which means the extent to which an SMA’s sentiment is consistent with investors’ existing beliefs. Investors may have their own beliefs (e.g., theory, judgment, or expectations) regarding where the market or a stock moves. The confirmation bias theory and empirical evidence (Kadous et al. 2019) show that investors prefer preferenceconsistent information, even at the expense of low accuracy. There fore, the content with preference-consistent sentiment may lead to higher readership and more subscriptions. In this study, we are interested in the preference effect. To account for the accuracy effect, we added the accuracy-related measures as control variables in Equations (1) and (2).

<sup>16</sup> To simplify our exposition of notations, we use • (dot) to concisely represent the variables of the same kind. For instance, $\beta _ { i t } ^ { \bullet }$ represents both $\beta _ { i t } ^ { f }$ and $\beta _ { i t } ^ { p } ; \tau _ { t } ^ { \bullet }$ represents both $\tau _ { t } ^ { \alpha ^ { \bullet } }$ and $\tau _ { t } ^ { \beta ^ { \bullet } }$ .

<sup>17</sup> Note that we assume investor preferences are heterogeneous across SMAs. We also expect that investor preferences for content are heterogeneous among investors as well. In our model, the investor preference for an SMA’s content is an SMA-level coefficient or variable $\left( \mathrm { i . e . , ~ } \alpha _ { i t } ^ { f } , \beta _ { i t } ^ { f } , \beta _ { i t } ^ { p } , \right.$ E(Reader ), and E(Subscribe $r _ { i t } ) )$ that measures the aggregate-level mean preferences of an SMA’s whole investor audience base. This aggregate measure accounts for the situation where investors have different preferences at the individual investor level. As such, the heterogeneous SMA-level investor preferences for content generation and monetization could result from the fact that different SMAs have different sets of investor bases and individual investors have heterogeneous preferences in each investor base.

<sup>18</sup> To keep our model specification parsimonious, we maintain that Monetiz $e _ { i t } = 1$ denotes an SMA producing paid content, but this does not preclude the SMA from generating free content. Likewise, $M o n e t i z e _ { i t } = 0$ denotes the case where the SMA either does not produce paid content or generates free content only on a given day. Because our emphasis is on content monetization, we focus on SMAs’ decisions for monetizing or producing paid content but not for generating free content.

<sup>19</sup> Note that SMAs’ paid content sentiment decision is conditional on Monetiz $_ { i t } = 1$ . In other words, an SMA needs to make a paid content sentiment decision only when he or she decides to monetize content.

<sup>20</sup> Investor preferences are contemporaneous here because much of SMAs’ content generation and monetization decisions are made in real time on financial social media in response to dynamic investor interactions and market factors. We also find that the model using contemporaneous investor preferences (DIC: 2986552; WAIC: 1909302) has a better model fit than that of the model using the lagged investor preferences (DIC: 3372256; WAIC: 2843997).

21 There are several channels through which SMAs can obtain the information about investor preferences. First, SMAs can observe the popular tweets or opinions by other SMAs on this platform or other social media platforms to infer information about investor prefer ences for content and its sentiment, Second, such information can be obtained via observing the variation in performance metrics such as free readership and paid subscriptions. After producing content, an SMA can observe the changes in the readership and subscriptions. An increase in readership or subscription suggests that the produced content is favored or positively received by investors. Third, through observing the content liked by investors and the number of likes for each piece of content, SMAs can infer the content and its sentiment preferred by investors. Fourth, through the comments from investors who leave their opinion or feedback for the content produced by SMAs, SMAs can draw inferences on the content and its sentiment preferred by investors as well.

<sup>22</sup> Note that we allow the error terms in the content monetization decision (π<sup>m</sup>) and content generation decisions $( \pi _ { i t } ^ { f }$ and $\pi _ { i t } ^ { p } )$ ) to be correlated, thus accounting for the interdependence between the supply-side decisions by an SMA.

<sup>23</sup> Because our main focus is on the supply-side results, we relegate the demand-side results to the Online Appendix.

<sup>24</sup> Free readers’ preferences and paid subscribers’ preferences are substantively different. Details can be found in the Online Appendix.

<sup>25</sup> Note that we measure content sentiment using the proportion of negative words (Tetlock 2007, Tetlock et al. 2008). Thus, the negative coefficient on readers’ preference for free (negative) content sentiment (coefficient � �0.018) means that when readers’ prefer ence for free (negative) content sentiment is higher (i.e., prefers sentiment that is more negative), the generated (negative) sentiment will be lower (i.e., sentiment is less negative). Hence, readers’ pref erence for free content (negative) sentiment and SMAs’ generated (negative) sentiment will move in the opposite direction. A possible explanation for SMAs’ contrarian approach toward free readers preferences for free (negative) content sentiment is that by saying things differently from readers’ own assessment of stocks, SMAs can add a dose of “surprise” into their content, which is easier to attract readers’ attention and spark discussions (Baldi and Itti 2010)

<sup>26</sup> Recall that we measure content sentiment using the proportion of negative words (Tetlock 2007, Tetlock et al. 2008). The positive coefficients for market returns (0.277 for the return from the prior one day and 0.070 for the return from the prior one month) suggest that when the market returns are higher (i.e., more positive), the generated (negative) sentiment will be higher, that is, more negative. In other words, market returns and SMAs’ generated (negative) sentiment for free content will move in the opposite direction. Hence, it is a contrarian approach.

27 The U.S. Securities and Exchange Commission (SEC) has constantly alerted the general public on the existence of content manip ulation in financial social media, such as rumors and fraud (SEC 2012, SEC 2014, SEC 2019). Catering to investor preferences may be another important yet intricate form of content manipulation.

<sup>28</sup> Revenue is calculated by the sum of all subscription fees accrued to each SMA. iMaibo has a 50/50-split revenue-sharing scheme with SMAs.

## References

Albuquerque P, Pavlidis P, Chatow U, Chen KY, Jamal Z (2012) Evaluating promotional activities in an online two-sided market of user-generated content. Marketing Sci. 31(3):406–432.

Antweiler W, Frank MZ (2004) Is all that talk just noise? The information content of internet stock message boards. J. Finance 59(3):1259–1294.

Aral S, Dhillon P (2020) Digital paywall design: Implications for con tent demand & subscriptions. Management Sci. 67(4):2381–2402.

Arner DW, Barberis J, Buckley RP (2015) The evolution of fintech: A new post-crisis paradigm. Geo. J. Int’l L. 47:1271–1319.

Baek J, Shore J (2020) Forum size and content contribution per per son: A field experiment. Management Sci. 66(12):5906–5924.

Bagnoli M, Beneish MD, Watts SG (1999) Whisper forecasts of quarterly earnings per share. J. Account. Econom. 28(1):27–50

Baker M, Wurgler J (2004a) Appearing and disappearing dividends: The link to catering incentives. J. Financial Econom. 73(2): 271–288.

Baker M, Wurgler J (2004b) A catering theory of dividends. J. Finance 59(3):1125–1165.

Baker M, Greenwood R, Wurgler J (2009) Catering through nominal share prices. J. Finance 64(6):2559–2590.

Baldi P, Itti L (2010) Of bits and wows: A Bayesian theory of sur prise with applications to attention. Neural Netw. 23(5):649–666.

Barberis N, Thaler R (2003) A survey of behavioral finance. Hand book of the Economics of Finance, vol. 1 (Elsevier, Amsterdam), 1053–1128.

Barberis N, Shleifer A, Vishny R (1998) A model of investor sentiment. J. Financial Econom. 49(3):307–343.

Barron OE (1995) Trading volume and belief revisions that differ among individual analysts. Account. Rev. 72(4):581–597.

Baumeister RF, Bratslavsky E, Finkenauer C, Vohs KD (2001) Bad is stronger than good. Rev. Gen. Psychol. 5(4):323–370.

Becker JU, Clement M, Schaedel U (2010) The impact of network size and financial incentives on adoption and participation in new online communities. J. Media Econom. 23(3):165–179.

Ben-David I, Franzoni F, Kim B, Moussawi R (2023) Competition for attention in the Etf space. Rev. Financial Stud. 36(3):987–1042.

Benner MJ, Ranganathan R (2013) Divergent reactions to convergent strategies: Investor beliefs and analyst reactions during technological change. Organ. Sci. 24(2):378–394.

Bhattacharya P, Phan TQ, Bai X, Airoldi EM (2019) A coevolution model of network structure and user behavior: The case of content generation in online social networks. Inf. Syst. Res. 30(1):117–132.

Bollen J, Mao H, Zeng X (2011) Twitter mood predicts the stock market. J. Comput. Sci. 2(1):1–8.

Bronnenberg BJ, Mahajan V (2001) Unobserved retailer behavior in multimarket data: Joint spatial dependence in market shares and promotion variables. Marketing Sci. 20(3):284–299.

Brown LD, Call AC, Clement MB, Sharp NY (2015) Inside the “black box” of sell-side financial analysts. J. Account. Res. 53(1):1–47.

Cavusoglu H, Phan TQ, Cavusoglu H, Airoldi EM (2016) Assessing the impact of granular privacy controls on content sharing and disclosure on Facebook. Inf. Syst. Res. 27(4):848–879.

Chen HL, Hu YJ, Huang S (2019) Monetary incentive and stock opi nions on social media. J. Manage. Inf. Syst. 36(2):391–417.

Chen H, De P, Hu YJ, Hwang B-H (2014) Wisdom of crowds: The value of stock opinions transmitted through social media. Rev. Financial Stud. 27(5):1367–1403.

Chiu PC, Lourie B, Nekrasov A, Teoh SH (2021) Cater to thy client: Analyst responsiveness to institutional investor attention. Management Sci. 67(12):7455–7471.

Clarkson PM, Joyce D, Tutticci I (2006) Market reaction to takeover rumour in Internet discussion sites. Account. Finance 46(1):31–52.

Das SR, Chen MY (2007) Yahoo! for Amazon: Sentiment extraction from small talk on the Web. Management Sci. 53(9):1375–1388.

De Franco G, Vasvari FP, Wittenberg-Moerman R (2009) The infor mational role of bond analysts. J. Account. Res. 47(5):1201–1248.

Ebbes P, Wedel M, Bo¨ckenholt U, Steerneman T (2005) Solving and testing for Regressor-error (in)dependence when no instrumental variables are available: With new evidence for the effect of education on income. Quant. Marketing Econom. 3(4):365–392.

Egan J, Cetera M (2023) Nearly 80% of young adults get financial advice from this surprising place. Forbes Advisor. Retrieved February 1, 2024, https://www.forbes.com/advisor/investing financial-advisor/adults-financial-advice-social-media/.

Giglio S, Maggiori M, Stroebel J, Utkus S (2021) The joint dynamics of investor beliefs and trading during the Covid-19 crash. Proc. Natl. Acad. Sci. USA 118(4):e2010316118.

Goes PB, Lin M, Au Yeung C-m (2014) “Popularity Effect” in usergenerated content: Evidence from online product reviews. Inform. Systems Res. 25(2):222–238.

Guiso L, Sapienza P, Zingales L (2018) Time varying risk aversion. J. Financial Econom. 128(3):403–421.

Guo C, Kim TH, Susarla A, Sambamurthy V (2020) Understanding con tent contribution behavior in a geosegmented mobile virtual community: The context of Waze. Inform. Systems Res. 31(4):1398–1420.

Heimbach I, Hinz O (2018) The impact of sharing mechanism design on content sharing in online social networks. Inform. Systems Res. 29(3):592–611.

Hsieh G, Kraut RE, Hudson SE (2010) Why pay? Exploring how financial incentives are used for question & answer. Proceeding of the SIGCHI Conference on Human Factors in Computing Systems (ACM, New York), 305–314.

Hu T, Tripathi A (2018) Is there a free lunch? Examining the value of free content on equity review platforms. Digital Transformation: Challenges and Opportunities: 16th Workshop on e-Business WeB 2017, Seoul, South Korea, December 10, 2017, Revised Selected Papers 16 (Springer International Publishing, Cham, Switzerland), 79–86.

Huang AH, Lehavy R, Zang AY, Zheng R (2018) Analyst information discovery and interpretation roles: A topic modeling approach. Management Sci. 64(6):2833–2855.

Hwang EH, Singh PV, Argote L (2015) Knowledge sharing in online communities: Learning to cross geographic and hierarchical boundaries. Organ. Sci. 26(6):1593–1611.

Kadous K, Mercer M, Zhou YD (2019) Do individual investors understand how social media advice influences their investment decision? Preprint, submitted June 17, http://dx.doi.org 10.2139/ssrn.2968407

Kim KH, Kumar V (2018) The relative influence of economic and relational direct marketing communications on buying behavior in business-to-business markets. J. Marketing Res. 55(1):48–68.

Kitagawa G (1996) Monte Carlo filter and smoother for non-Gaussian nonlinear state space models. J. Comput. Graph. Statist. 5(1):1–25.

Kogan S, Moskowitz TJ, Niessner M (2022) Social media and financial news manipulation. Rev. Finance 27(4):1229–1268.

Lachaab M, Ansari A, Jedidi K, Trabelsi A (2006) Modeling preference evolution in discrete choice models: A Bayesian state space approach. Quant. Marketing Econom. 4(1):57–81.

Lambrecht A, Misra K (2017) Fee or free: When should firms charge for online content? Management Sci. 63(4):1150–1165.

Li S, Sun B, Montgomery AL (2011) Cross-selling the right product to the right customer at the right time. J. Marketing Res. 48(4):683–700.

Lindsten F, Scho¨n TB (2013) Backward simulation methods for Monte Carlo statistical inference. Foundations and TrendsVR in Machine Learning 6(1):1–143.

Liu Y, Feng J (2015) Can Monetary Incentives Increase Ugc Contribution? (The Motivation and Competition Crowding Out, Fort Worth, TX).

Liu Y, Shankar V (2015) The dynamic impact of product-harm crises on brand preference and advertising effectiveness: An empirica analysis of the automobile industry. Management Sci. 61(10) 2514–2535.

Liu TX, Yang J, Adamic LA, Chen Y (2014) Crowdsourcing with allpay auctions: A field experiment on Taskcn. Management Sci. 60(8):2020–2037.

Loughran TIM, McDonald B (2011) When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. J. Finance 66(1):35–65.

Lu Y, Singh PV, Sun B (2017) Is a core-periphery network good for knowledge sharing? A structural model of endogenous network formation on a crowdsourced customer support forum. Management Inform. Syst. Q. 41(2):607–628.

Luo A, Kumar V (2013) Recovering hidden buyer–seller relationship states to measure the return on marketing investment in business-to-business markets. J. Marketing Res. 50(1):143–160.

Luo X, Zhang J, Duan W (2013) Social media and firm equity value Inform. Systems Res. 24(1):146–163.

Manchanda P, Rossi PE, Chintagunta PK (2004) Response modeling with nonrandom marketing-mix variables. J. Marketing Res. 41(4): 467–478.

Mason W, Watts DJ (2010) Financial incentives and the performance of crowds. SIGKDD Explor. 11(2):100–108.

Matsuyama A, Wood T (2022) The rising role of social media ‘finfluencers’. Deloitte. Retrieved February 1, 2024, https:// www.deloitte.com/au/en/Industries/financial-services/blogs/ rising-role-social-media-finfluencers.html.

Meng X (2015) Analyst reputation, communication, and information acquisition. J. Account. Res. 53(1):119–173.

Morris S (2001) Political correctness. J. Political Econom. 109(2): 231–265.

Musalem A, Bradlow ET, Raju JS (2008) Who’s got the coupon? Esti mating consumer preferences and coupon usage from aggre gate information. J. Marketing Res. 45(6):715–730.

Nair HS, Misra S, Hornbuckle WJ, Mishra R, Acharya A (2017) Big data and marketing analytics in gaming: Combining empirical models and field experimentation. Marketing Sci. 36(5):699–725.

Nguyen P, Wang X, Li X, Cotte J (2021) Reviewing experts’ restraint from extremes and its impact on service providers. J. Consumer Res. 47(5):654–674.

Oh H, Animesh A, Pinsonneault A (2016) Free vs. for-a-fee: The impact of a paywall on the pattern and effectiveness of word of-mouth via social media. Management Inform. System Q. 40(1): 31–56.

Park J, Konana P, Gu B, Kumar A, Raghunathan R (2013) Informa tion valuation and confirmation bias in virtual communities: Evidence from stock message boards. Inform. Systems Res. 24(4): 1050–1067.

Pattabhiramaiah A, Sriram S, Sridhar S (2018) Rising prices under declining preferences: The case of the US print newspaper industry. Marketing Sci. 37(1):97–122.

Pauwels K, Weiss A (2008) Moving from free to fee: How online firms market to change their business model successfully. J. Marketing 72(3):14–31

Qiu L, Kumar S (2017) Understanding voluntary knowledge provi sion and content contribution through a social-media-based prediction market: A field experiment. Inform. Systems Res. 28(3):529–546.

Roll R (1984) A simple implicit measure of the effective bid-ask spread in an efficient market. J. Finance 39(4):1127–1139.

Rossi PE, Allenby GM (2003) Bayesian statistics and marketing. Marketing Sci. 22(3):304–328.

Rozin P, Royzman EB (2001) Negativity bias, negativity dominance, and contagion. Pers. Soc. Psychol. Rev. 5(4):296–320.

Rutz OJ, Trusov M (2011) Zooming in on paid search ads-a consumer-level model calibrated on aggregated data. Marketing Sci. 30(5):789–800.

Sabherwal S, Sarkar SK, Zhang Y (2008) Online talk: Does it matter? Management Finance 34(6):423–436.

Saboo AR, Grewal R (2013) Stock market reactions to customer and competitor orientations: The case of initial public offerings. Marketing Sci. 32(1):70–88.

Schweidel DA, Knox G (2013) Incorporating direct marketing activity into latent attrition models. Marketing Sci. 32(3):471–487.

SEC (2012) Investment adviser use of social media. National Examination Risk Alert 2(1):1-7.

SEC (2014) Updated investor alert: Social media and investing – Avoiding fraud. U.S. Securities and Exchange Commission, Washington, DC.

SEC (2019) Investor bulletin: Social sentiment investing tools—Think twice before trading based on social media. U.S. Securities and Exchange Commission, Washington, DC.

Shen W, Hu YJ, Rees J (2015) Competing for attention: An empirical study of online reviewers’ strategic behavior. Manage. Inf. Syst Q. 39(3):683–696.

Shi Z, Rui H, Whinston AB (2014) Content sharing in a social broadcasting environment: Evidence from Twitter. Manage. Inf. Syst. Q. 38(1):123–142.

Song T, Huang J, Tan Y, Yu Y (2019) Using user-and marketergenerated content for box office revenue prediction: Differences between microblogging and third-party platforms. Inform. Sys tems Res. 30(1):191–203.

Sriram S, Kalwani MU (2007) Optimal advertising and promotion budgets in dynamic markets with brand equity as a mediating variable. Management Sci. 53(1):46–60.

Stephen A, Bart Y, Du Plessis C, Goncalves D (2012) Does paying for online product reviews pay off? The effects of monetary incentives on content creators and consumers. NA Adv. Consumer Res. 40:228–231.

Tang Q, Gu B, Whinston AB (2012) Content contribution for reve nue sharing and reputation in social media: A dynamic structural model. J. Management Inform. Syst. 29(2):41–75.

Tetlock PC (2007) Giving content to investor sentiment: The role of media in the stock market. J. Finance 62(3):1139–1168.

Tetlock PC, Saar-Tsechansky M, Macskassy S (2008) More than words: Quantifying language to measure firms’ fundamentals J. Finance 63(3):1437–1467.

Van Diepen M, Donkers B, Franses PH (2009) Dynamic and compet itive effects of direct mailings: A charitable giving application. J. Marketing Res. 46(1):120–133.

Wang J, Ghose A, Ipeirotis P (2012) Bonus, disclosure, and choice: What motivates the creation of high-quality paid reviews? Proceedings of the Thirty Third International Conference on Information Systems (ICIS 2012), 9 (Association for Information Systems, Atlanta).

Wang Y-Y, Guo C, Susarla A, Sambamurthy V (2021) Online to offline: The impact of social media on offline sales in the automobile industry. Inform. Systems Res. 32(2):582–604.

Wei Z, Xiao M, Rong R (2020) Network size and content generation on social media platforms. Production Oper. Management 30(5): 1406–1426.

Zhang J, Wedel M, Pieters R (2009) Sales effects of attention to feature advertisements: A Bayesian mediation analysis. J. Market ing Res. 46(5):669–681.

Zhao L, Detlor B, Connelly CE (2016) Sharing knowledge in social Q&A sites: The unintended consequences of extrinsic motivation. J. Management Inform. Syst. 33(1):70–100.

Zhao Y, Zhao Y, Song I (2009) Predicting new customers’ risk type in the credit card market. J. Marketing Res. 46(4):506–517.

Zheludev I, Smith R, Aste T (2014) When can social media lead financial markets? Sci. Rep. 4(1):1–12.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
