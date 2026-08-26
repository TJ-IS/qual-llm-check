---
otero_id: 20046
otero_key: "U5KKBXC5"
title: "Impact of the COVID-19 pandemic on the stock market and investor online word of mouth"
authors: "Xiaorui Zhu; Shaobo Li; Karthik Srinivasan; Michael T. Lash"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.114074"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of the COVID-19 pandemic on the stock market and investor online word of mouth

![](/api/attachments/U5KKBXC5/fulltext/images/36de4796db7d3c9a24f376bd50660ad6c990b0177f6a6953d38f703d1a2c3212.jpg)

Xiaorui Zhu <sup>a</sup>, Shaobo Li <sup>b</sup>, Karthik Srinivasan <sup>b</sup>, Michael T. Lash <sup>b,</sup>

<sup>a</sup> Towson University, College of Business and Economics, 8000 York Road, Towson, MD 21252, United States of America <sup>b</sup> University of Kansas, School of Business, 1654 Naismith Dr, Lawrence, KS 66045, United States of America

## A R T I C L E I N F O

Keywords: Stock market Sentiment Prediction COVID-19 Pandemic Social media analytics Text mining

## A B S T R A C T

Investor sentiment based on social media Word-of-Mouth (WoM) has been shown to be predictive of stock returns under normal market conditions. However, the COVID-19 pandemic has brought unprecedented impact and uncertainty to the stock market. In this paper, we examine the predictability of social media-based WoM on dav-ahead US stock market returns across three phases of the pandemic: pre-COVID. peak-COVID. and recovery. We collect over 24 million stock-related tweets from Twitter across these three periods and employ text-mining methods for feature engineering. We focus on two channels of WoM information, aggregate sentiments, and disaggregated topics, representing investors’ overall opinions and discussion patterns about the stock market. We find that, in contrast to normal market conditions, the investor sentiment indices are not significant in predicting market returns during the peak-COVID and recovery periods, while for the pre-COVID period, our findings are consistent with prior studies. To explore the effect of disaggregated latent topics, we propose an ensemble feature selection approach that identifies relevant topics for each of the three periods. We find that adding topic in formation significantly improves model prediction during the peak-COVID period. Our findings imply that during a global socio-economic disruption and the subsequent recovery, the landscape of financial markets, examined through the lens of social media-based WoM, is different than during normal market conditions. Our findings also suggest that investors who primarily trade on sentiment may wish to leverage machine learning techniques to identify latent topic information, subsequently incorporating such information into their trading decisionmaking.

## 1. Introduction

With traditional market indicators, lagging market behavior, and millions of individuals’ collective wealth on the line, it is imperative to study the underlying drivers of erratic market behavior experienced during disasters like COVID-19. While a nation’s economic indicators and market performance may be expected to be closely related under normal conditions, US stock index movements during COVID-19 have been contrary to the expectations of most economic analysts throughout the pandemic and onward [1]. Fig. 1 shows that the S&P 500 index began dropping towards the end of February 2020 as the coronavirus outbreak worsened worldwide, falling by over 30% in mid-March. However, the index rebounded immediately after the Federal Reserve announced steps to provide trillions of dollars to support the economy. As the pandemic continued, the index surpassed previous market highs. Meanwhile, the weekly economic index (WEI), an aggregate measure consisting of ten economic indicators, including the Rasmussen Con sumer Index and new unemployment insurance claims, temporally tracked with, yet proceeded, S&P 500 performance.

Understanding the drivers of market behavior under such conditions will allow decision-makers to mitigate financial risk. To such an end, one of the early studies to examine financial markets during COVID-19 [1] showed that the wild volatility of stock prices was primarily driven by fluctuations in risk aversion or sentiment rather than the economic state based on a theoretical model. Many past studies have documented how various investor sentiments influence the stock market [2–9]. Yet, few studies have investigated how such communication channels contribute to volatile market movement during global disasters such as COVID-19. A popular source for investor sentiment analysis is online social media platforms, such as Twitter, on which large-scale and high-velocity posts provide a wealth of information reflecting investor WoM [3,6]. To provide some cursory indications that social media-based WoM channels may provide insight into the COVID-19 stock market phenomenon, we plot the frequency of Twitter tweets mentioning either the phrase “stock market” or one of the S&P 500 ticker symbols in Fig. 1. We observe that the volume of daily tweets began increasing prior to the index’s disas trous dip and abrupt recovery. The average volume from 01/21/ 2020–12/11/2020, perhaps the most volatile period, is 1.756 times more than before the outbreak of COVID-19.<sup>1</sup> With this cursory obser vation in mind and motivated by past work, our study aims to examine the effects of social media WoM on the stock market during this volatile period. Our empirical findings may provide financial decision-makers with actionable insights for managing future disasters. To outline the gaps we intend to fill, we discuss past works on investor sentiments and financial markets during the COVID-19 pandemic subsequently.

![](/api/attachments/U5KKBXC5/fulltext/images/8b02739f9126f0e9a0d7afc86b5b57b9613164efc6a654b77609d60b23d6b9e7.jpg)  
Fig. 1. S&P 500 index, WEI, and stock market tweet count from 04/05/2019 to 07/09/2021.

## 1.1. Related works on COVID-19 and financial markets

A few studies in finance and information systems have explored the stock market during COVID-19. Ramelli and Wagner [10] studied crosssectional stock return responses during the early stages of the pandemic. Their findings indicate that investors anticipate the effects of COVID-19 to be amplified by financial channels, such as the involvement of global trading, cash holding and leverage, and conference calls. Chatterjee and French [11] explored a Twitter-based uncertainty index and its effect on the stock market before and during COVID-19. While based on social media platforms, their uncertainty index is not a measure of investor sentiment. A theoretical model presented by John and Li [12] suggests that investors make perceptual errors in sentiment trading, and they find that only COVID and market-induced sentiment, using Google search data as a proxy, significantly affect the realized volatility of stock indices. Unlike their approach that uses proxies, our study directly measures investor sentiment via Twitter WoM. Baig et al. [13] find that negative global sentiment has a significant effect on market liquidity and volatility under COVID-19. However, they use general news-oriented sentiment instead of social media-based investor sentiment. In addi tion, their empirical results are based on a 3-month period from January to April 2020, only covering the initial stages of the pandemic. These works primarily focus on the effects of the pandemic on stock volatility, while our study directly examines the effects on stock returns. A few other studies have also explored the international stock market [14–16]. Nevertheless, few studies have explored the channel of online social media and its impact on the stock market during the pandemic, while this channel has been well studied under a normal stock market, which we briefly review in the next subsection. Furthermore, these past studies only investigate the phenomenon during the very early stages of the event, leaving large portions of the pandemic and its recovery unexplored.

## 1.2. Related work on social media and financial markets

It is well known that social media WoM significantly influences general consumer behavior [17]. With this generality in mind, a growing body of literature has also explored the association between social media WoM and the stock market. To mention a few, Bollen et al. [3] demonstrated that public mood derived from high volume daily tweets on Twitter is predictive of the Dow Jones Industry Average index (DJIA). Other than Twitter, studies also analyzed messages from a stock-broker blogging platform called StockTwits.com. For instance, Pineiro-Chousa˜ et al. [4] studied how the message sentiment affects Chicago Board Options Exchange Market Volatility Index (VIX). Deng et al. [6] exam ined the interaction between sentiment and the stock market through the lens of bidirectional causality. Yu et al. [18] examined and compared the sentiment effects from social media and conventional media on short-term stock returns and found that social media sentiment has a stronger relationship with firm stock performance. To examine if social media sentiment has a time-varying effect on stock return, Ho et al. [19] employed a Bayesian Dynamic Linear Model and empirically confirmed the dynamic relationship based on the US stock market from 2009 to 2012.

Most of these works show that WoM information strongly influences stock market movement, but their results are primarily derived under “normal” market conditions. In contrast, Ge et al. [20] investigated the effects of emotions in social media during the 2015 Chinese stock market crash, finding that negative sentiment surrounding the crash creates a negative reinforcement loop – i.e., negative sentiment causes the market to crash further, which causes more negative sentiment. This work, however, does not directly examine the effects on stock returns; instead, they investigate the impact on a three-level market cognition which is an aggregate measure of market movement. Furthermore, the market crash due to the pandemic can be unique and different from crashes due to other reasons. To summarize, despite a large body of work on this topic, few of them are undertaken in response to a disaster of a scale and scope akin to the COVID-19 pandemic, and it is worth reassessing the rela tionship between online WoM and the stock market under such an un precedented circumstance.

## 1.3. Our study

With the research gaps in the preceding two subsections in mind, we assess the impact of COVID-19 on stock market returns through the lens of two important WoM derivatives, sentiment analysis and topic modeling, both of which have been widely adopted as popular machine learning tools for broad applications in decision support systems [21–23]. More specifically, we attempt to answer the following essential yet unanswered questions: (1) Should we expect social media-derived sentiment to play a different role in predicting the stock market under normal and volatile market conditions, e.g., before and during the outbreak of COVID-19? (2) Beyond sentiments, do specific topics dis cussed on social media help predict stock returns? (3) If so, are stock returns driven by different latent topics under different market environments?

Our empirical analysis focuses on the US stock market from April 2019 to July 2021. To assess the impact of COVID-19, we divide our sample into three distinct periods – “pre-COVID” (04/01/2019–01/20/ 2020), “peak-COVID” (01/21/2020–12/11/2020), and “recovery” (12/ 12/2020–07/22/2021), where the two cutoff dates, 01/20/2020 and 12/11/2020, are the dates on which two remarkable events took place: CDC confirmation of the first U.S. COVID-19 case (01/20/2020) and FDA Emergency Use Authorization (EUA) of the Pfizer-BioNTech COVID-19 vaccine (12/11/2020).<sup>2,3</sup>

To obtain social media-based investor WoM, we extracted 23.9 million tweets with the phrase “stock market" or one of the S&P 500 ticker symbols posted during these periods. Using text mining tech niques, we converted the massive and unstructured raw tweets into structured textual information, namely, investor sentiment and latent topics, representing two layers of social media WoM. We adopt two well documented investor sentiment indices, Bullishness and Agreement [2,5,24] (more details provided in Section 3). The sentiment indices can be regarded as aggregate information reflecting overall investor senti ment. On the other hand, the latent topics derived from Latent Dirichlet Allocation (LDA) modeling [25] can be considered a type of dis aggregated information that captures the pattern of investors’ discussion on social media.

By controlling for various market and economic factors, the effects of social media-based investor WoM, quantified via sentiment and topic distribution measures, can be tested across our defined periods of in terest (pre, peak, and recovery). In our empirical analysis, we first examine the effects of investor sentiment on stock returns and how these effects differ across the three phases of the pandemic. We then incor porate the disaggregated topic information to examine if it carries additional predictive power on stock returns and whether these “topics' differ across different periods. We summarize our findings as follows.

First, we find that, only under normal market circumstances, i.e., the pre-COVID period, are both social media-based investor sentiment indices, “Bullishness” and “Agreement,” statistically significant in pre dicting market return (e.g., S&P500 return) of the following trading day. The predictivity of both sentiment indices disappears during both peak COVID and recovery periods. In addition, we also find that the commonly used non-social-media-based sentiment indices, the one-year individual investor confidence index and institutional investor confi dence index, have the same dynamics as the social media-based senti ment indices in terms of statistical significance. However, the socia media-based sentiment indices are more predictive than these two non-social-media-based sentiment indices. Second, incorporating the latent topic information (the disaggregated investor WoM) adds sub stantial explanatory and predictive power across all periods, with the most prominent effects observed during the peak-COVID period and least during the recovery period. Using a novel ensemble-based feature selection procedure, we also find that the top 10 selected latent topics have little overlap across the three distinct sample periods. These find ings are in line with our main hypotheses (detailed in Section 2), fo which we conjecture that the reduced explanatory and predictive power of the sentiment indices is attributable to noisy and unreliable social exchanges, while the significant predictivity of latent topics is possibly due to the relevance and condensed nature of topic information.

Our study contributes to the current literature through the following dimensions. First, we expand the emerging literature on COVID-19 by exploring the association between social media WoM and stock returns. Despite a growing body of literature, to the best of our knowledge, no study has yet examined the effect of social media-based investor WoM on the stock market return and how the arrival of COVID-19 moderates such effects. Our study examines social media-based investor sentiment, a traditional channel of WoM, as well as disaggregated WoM informa tion (i.e., latent topics), and their effects on day-ahead stock market returns. Unlike many existing studies that only focused on a short time window during early COVID-19, our analysis is based on a substantially more protracted period, including the post-peak recovery period, and each of our three subsamples covers at least seven months, providing a sufficient number of observations for day-ahead stock return analysis. The natural division of the sample into pre-COVID, peak-COVID, and recovery facilitates our investigations on the moderating effects of COVID-19 and if such effects persist beyond the peak-COVID period. To our knowledge, we are the first to conduct such a comparative analysis to examine the impact of COVID-19 on the association between social media WoM and stock market returns.

Second, with respect to decision support systems literature, our empirical findings and our theoretical development give new insights into investors’ short-term trading strategies. Specifically, social mediabased investor sentiments, in general, tend to be less predictive during the global pandemic when market conditions are highly uncertain, and social exchanges are noisy and unreliable. In contrast, disaggregated information (topics) extracted from social media platforms carry non negligible predictive and explanatory power of day-ahead stock market returns. The effect of such disaggregated social media WoM is found to be most significant during the peak-COVID period. Therefore, when the market is highly volatile, investors who primarily trade on sentiment should leverage machine learning techniques, such as our proposed ensemble feature selection procedure, to further identify relevant topics in addition to aggregated sentiment indices.

In the next section, we present our research hypotheses. In Section 3, we provide details of data collection and feature engineering, including the LDA model. Sections 4 and 5 detail the methods and empirical results of the analyses of investor sentiment and latent topics, respectively. Finally, we conclude the paper by providing further discussions and implications.

## 2. Hypothesis development

Before introducing our hypotheses, we describe a conceptual model shown in Fig. 2. In this model, investors’ behaviors (box 4) are collec tively influenced by multiple types of information belonging to one of three categories: (1) market-related information, (2) micro- and mac roeconomic information, and (3) massive WoM information from social exchanges. Market-related information includes some of the most conventional metrics for trading, such as historical returns, volatilities, and other metrics directly induced by historical stock prices (box 5). Since our study focuses on daily market returns, e.g., the S&P500 index, we consider lagged returns and volatilities of the index by following the standard stock return forecasting models [9,26,27]. The economic data include interest-rate related variables such as risk-free rate, inflation, term spread and default spread, and the weekly economic index (WED). a composite index of several macroeconomic variables (more details are given in Section 3). These variables are also commonly used in stock return forecasting models found in the literature. Both types of infor mation are controlled for, because they are publicly available and can be quickly disseminated through both traditional news media and social media platforms (box 3). We do not consider traditional news media because the news coverage is often posted on social media by news media accounts or shared by individual users. We filter the information posted on social media (e.g., tweets) to be stock market relevant with the following two categories: general market chatter that mentions the “stock market” and stock-specific chatter that explicitly tags one of the S&P 500 ticker symbols. The chatters (3-a) form the bases to measure social media-based investor WoM (3-b) in two dimensions: investors overall sentiment as an aggregated measure and various specific topics as a disaggregated WoM measure.

![](/api/attachments/U5KKBXC5/fulltext/images/c15d8453b80b55af0c7b975e5ba32642034e61174aa4c2416d69a858f5dfd9e8.jpg)  
Fig. 2. A conceptual model: interactions between social media WoM and the stock market.

It has been well recognized that WoM communication plays a vital role in influencing consumers’ attitudes and decisions in brand and product purchases [17]. Indeed, a comprehensive review conducted by Cheung and Thadani [28] demonstrates that electronic WoM functions as a form of social influence that affects consumer purchases. Positive WoM leads to increased purchase behavior, while negative WoM leads to purchase aversion. Furthermore, they find that increased WoM volume positively correlates with purchase intention. In the stock market, both retail and institutional investors’ behaviors can be similarly influenced by WoM [29]. Shiller [30] wrote, “…Word-of-mouth transmission of ideas appears to be an important contributor to day-to-day or hour-to-hour stock market fluctuations” (pp. 180).

Most existing works on WoM and the stock market, as well as the present study, are driven by behavioral finance theories, mainly arguing that irrational investors trade on their beliefs [31–34], thus creating market inefficiencies. This contrasts the efficient market hypothesis (EMH) [35], which states that asset pricing reflects all currently avail able information related to the asset. The EMH implies that finding “undervalued” stocks is impossible as all available information is quickly spread and incorporated into the securities’ prices. However, a fundamental assumption of EMH is that market participants are rational, which often does not hold in practice. Black [31] first introduced the term noise trading, following which Shleifer and Summer [36] proposed the noise trader approach as an alternative to EMH. The noise trader approach imposes a more realistic assumption, namely, “some investors are not fully rational and their demand for risky assets is affected by their beliefs or sentiments that are not fully justified by fundamental news.” To explain the sentiment effects, in the study done by Jiao et al. [37], the precise interaction between WoM signaling on social media and lead-lag association with stock returns is attributable primarily to the five basic investor characteristics, namely the “echo chambers” effect, over confidence, conservatism, rational inattention, and confirmation bias, which all can be amplified especially under a volatile market.

Indeed, with the strike of the global pandemic, the irrationality in the stock market has undoubtedly increased, leading to a surge of noise trading, which is known to induce market volatility. It is estimated that the brokerage industry added about 10 million new clients in 2020.<sup>4</sup> Robinhood, a fintech trading app, saw three times its average customer trading volume in March 2020 compared to 2019.<sup>5</sup> Google Trends shows that “stock trading” keyword searches in the US in mid-March 2020 appeared more than five times the 2019 average.<sup>6</sup> Such a record surge of new retail investors is likely due to the low commission fees, market bottom, and stay-home orders amid COVID-19. Most of these new retail investors have very limited trading experience and they only focus on short-term returns. Instead, they heavily rely on social media platforms, such as Twitter, Discord, and Reddit, to exchange information,<sup>7</sup> which results in higher volume yet highly contaminated WoM information being disseminated on social media platforms.

This shift in investor behavior could further amplify irrational noise trading behavior across the whole market. The question is whether the noise trader approach is still suitable under such unprecedented market conditions. More specifically, our study addresses the following ques tion: across different market conditions during the pandemic, does social media-based investor sentiment, or more generally the social media WoM, explain and predict the stock returns differently? To this end, we propose our first hypothesis, which we express in two parts:

H1a. Social media-based investor sentiment provides little explanatory and predictive power when the market is highly volatile (i.e., during the peak COVID period).

H1b. Social media-based investor sentiment will remain weak during the recovery period.

Social media-based investor sentiment is an aggregated measure of investor WoM. One justification for H1 is that when WoM information is highly divergent, aggregated measures also exhibit high variance, which in turn can reduce the association with stock market movement. In addition, H1 also ties to the adaptive market hypothesis (AMH) [38], which reconciles the market’s inefficiencies from the perspective of evolutionary principles. While AMH argues that market inefficiency drives investors to learn, adapt, and trade on information, this process may fail in a highly uncertain and volatile market. A possible reason is that there is likely an increased behavioral bias under such circum stances due to overconfidence, overreaction, and herding.

Consequently, investors who trade on sentiment may no longer benefit from it; hence the effects of sentiment information are reduced. Further, some existing findings are also in line with H1. In particular, Chung et al. [39] examined the predictive power of a non-social mediabased investor sentiment [8] on cross-sectional stock returns across different economic states. They showed that it is generally insignificant during a recession, while in an economic expansion state, sentiment has significant and robust predictive power on stock returns. Along similar lines, Ge et al. [20] investigated the effects of emotions in social media on the Chinese stock market during the 2015 market crash. They found that market cognitions in both in-crash and post-crash periods are similarly affected by the high arousal of emotions. Under our context, similarly, we suspect that the social media-based sentiment may have similar effects in both peak-COVID and recovery periods.

While H1 states that the overall sentiment carries little effect on the stock market during the peak-COVID and recovery periods, in subse quent hypotheses, we examine whether disaggregated WoM informa tion, measured via latent topics, is predictive to market returns before and during the pandemic. We posit the following two hypotheses:

H2. The inclusion of disaggregated topic input features adds significant explanatory and predictive power to existing stock return models during normal and volatile market conditions.

H3. The top-N predictive topics derived from social media WoM differ during normal, peak, and recovery periods of the COVID-19 pandemic.

The rationale behind H2 and H3 is that latent topics, representing disaggregated WoM information, have their narratives, each reflecting a different but specific dimension of WoM. Investors often discuss issues and topics specific to temporally varying market situations, hence the most prevalent conversational topics in online WoM can be different before and during a global crisis like the COVID-19 pandemic. The discussion distribution over topics at a particular point in time may be linked to market sentiment, uncertainty, future investment strategies, etc. Therefore, once the topics relevant to different market conditions are selected based on their association with stock returns, they can add additional information not captured by the aggregate sentiment indices to stock return forecasting models.

Relatively few past studies have explored the effect of disaggregated WoM measures, such as latent topics, on the stock market [40,41]. To mention a few, Ke et al. [41] constructed a sentiment score from news articles in “Dow Jones Newswires” to predict stock return using topic modeling. Similarly, Glasserman et al. [40] compared different LDA models used to select news topics to explain stock returns. Gjerstad et al. [42] examined the effects of former US President Donald Trump’s tweets on financial markets through topic modeling. Our study further expands this literature by not only examining the predictive power of latent topics on the US stock market, but also how the latent topics change across different phases of the COVID-19 pandemic. Latent topics have been derived in other contexts, however. For instance, Aziz et al. [43] applied topic modeling to over 5000 finance research articles from 1990 to 2018, providing a comprehensive overview of how topics have evolved in finance research. Huan et al. [44] examined intermediary analyst information roles by adopting topic modeling to extract textual information from analysts’ reports following companies’ quarterly earnings conference calls. Ibrahim and Wang [45] applied latent topic modeling to capture the structure of WoM in the online retail section.

We conclude this section by illustrating the empirical models we develop to investigate our hypotheses. As shown in Fig. 3, the three boxes on the left-hand side are three different sets of predictors. These are mapped onto our response variable of interest, day-ahead S&P500 index returns, via our predictive model. Our three hypotheses are then tested separately by controlling for the conventional predictors. Finally, to examine the moderating effect of COVID-19 using, we fit and compare models across three time periods: pre-COVID, peak COVID, and recovery.

## 3. Data and feature engineering

To investigate the impact of COVID-19 on U.S. stock market pricing, we fuse data from several sources to derive a variety of factors for in clusion in our empirical models. Our data sources include Twitter, Yahoo! Finance, and the St. Louis Federal Reserve Bank website.

## 3.1. Online WoM data and features

Using two criteria, we obtain stock market-related tweets (i.e., short 140-character messages) from the microblogging social media platform Twitter. First, if a tweet mentions the “stock market” specifically, it is included in our “general market chatter” corpus. Second, if a tweet explicitly tags one of the S&P 500 ticker symbols, it is included in our “stock-specific chatter” corpus. We discuss the use and fusion of these two corpora shortly. These tweets are collected from 04/01/2019 to 07/ 22/2021, thus spanning our defined pre-COVID, peak-COVID, and re covery periods.

We apply several text-based pre-processing techniques to both Twitter corpora, including the conversion of all text to lower-case, the removal of URLs, usernames, hashtags, punctuation, and repeating characters (e.g., “hellooooo” is converted to “hello”), as well as stem ming using the Porter stemmer. Each tweet is then represented as a collection of processed unigram tokens from which we derive sentiment scores and topic distributions, which are then aggregated to a daily level of temporal granularity. Table 1 summarizes our processed stock market Twitter corpus.

To derive sentiment scores for each tweet, we employ VADER [46], a well-known rule-based technique for obtaining social mediafocused sentiment scores. The method works in conjunction with a va riety of lexicons to provide negative, neutral, and positive sentiment scores for each social media post. We aggregate the scores by day d and corpus c ∈ {general market chatter, general market chatter ∪ stock− specific chatter}. Note that we derive sentiment scores for general market chatter only and the union of general market chatter and stockspecific chatter since these two sets coincide with our hypotheses. Average daily sentiment values are derived as follows:

$$
\left[ n e g _ {d} ^ {c}, \mathsf {n e u t} _ {d} ^ {c}, p o s _ {d} ^ {c} \right] = \frac {1}{\left| T w e e t s _ {d} ^ {c} \right|} \sum_ {t \in T w e e t s _ {d} ^ {c}} V A D E R (t).\tag{1}
$$

## 3.2. Investor bullishness and agreement

To measure social media-based investor overall sentiment, we borrow two popular finance notions, Bullishness and Agreement, following prior studies [2,5,24]. The two indices are constructed by aggregating the positive and negative sentiment measures we obtained previously. The Bullishness index measures the amount of surplus pos itivity expressed through tweets on a given day. Bullishness is defined as:

$$
B u l l i s h n e s s _ {d} ^ {c} = \ln \left(\frac {1 + p o s _ {d} ^ {c}}{1 + n e g _ {d} ^ {c}}\right).\tag{2}
$$

Agreement index measures the degree to which the tweets express the same type of sentiment on a given day (i.e., how much the various tweets agree). We express this measure as:

![](/api/attachments/U5KKBXC5/fulltext/images/c711ba2f27b9c52ebbc62cc0e488dafe8c3de6ab576dbac731fe7dd4427debac.jpg)  
Fig. 3. Illustration of the empirical model of our study.

Table 1  
Descriptive statistics of our processed stock market Twitter corpora.

<table><tr><td>Corpus</td><td>Measure/Period</td><td>Total</td><td>Daily Avg</td></tr><tr><td rowspan="3">General Market Chatter</td><td>Tweets (04/01/2019–07/22/2021)</td><td>6,399,877</td><td>7591</td></tr><tr><td>Terms</td><td>116,827,965</td><td>138,585.96</td></tr><tr><td>Unique Terms</td><td>1,331,546</td><td>-</td></tr><tr><td rowspan="3">Stock-specific Chatter</td><td>Tweets (04/01/2019–07/22/2021)</td><td>18,203,243</td><td>21,593.41</td></tr><tr><td>Terms</td><td>328,374,929</td><td>389,531.35</td></tr><tr><td>Unique Terms</td><td> $2,000,000^a$ </td><td>-</td></tr><tr><td rowspan="3">General + Stock-specific</td><td>Period: Pre-COVID</td><td>5,289,835</td><td>17,931.64</td></tr><tr><td>Period: Peak-COVID</td><td>10,263,705</td><td>31,483.75</td></tr><tr><td>Period: Recovery</td><td>7,391,439</td><td>34,539.43</td></tr></table>

<sup>a</sup> We parameterized the model to retain the 2,000,000 most common unique terms to ensure more reasonable computation times were maintained.

$$
\text { Agreement } _ {d} ^ {c} = 1 - \sqrt {1 - \left(\frac {\text { pos } _ {d} ^ {c} - \text { neg } _ {d} ^ {c}}{\text { pos } _ {d} ^ {c} + \text { neg } _ {d} ^ {c}}\right) ^ {2}}.\tag{3}
$$

In the context of predicting market returns, these two metrics have direct ties to investor’s trading behavior, so they can better reflect investor sentiment than raw negative and positive sentiment scores. Our proposed indices differ from those in [2,5,24] in that we use aggregated sentiment scores rather than threshold-categorized positive/negative tweets and positive/negative counts. Our approach, therefore, promises to be more distinguishing and organic since it does not rely on param eterized cutoff values to dictate whether a tweet is positive or negative.

## 3.3. Disaggregated online WoM topic distributions

To investigate H2 and H3, we derive topics for each tweet using Latent Dirichlet Allocation (LDA) [25], an unsupervised topic learning technique. LDA views a document (in this case, a tweet) as a random mixture of latent topics, each of which is characterized by a distribution over corpus terms. The process of discovering these topics involves maximizing (a) the expectation of the posterior distribution of corpu terms over K topics and (b) the distribution of K topics over corpus documents, where K is a user-specified value indicating the number of topics one would like the process to discover. Once the K topics are discovered, the LDA model can be used to obtain a distribution over topics for any tweet. Therefore, we derive an LDA model from both general market and stock-specific chatter tweets, subsequently obtain ing a topic distribution for each tweet using this model. We then aggregate the tweet distributions by day d and average over this aggregation:

$$
\operatorname{topic} _ {d} ^ {k} = \frac {1}{| T w e e t s _ {d} |} \sum_ {t \in T w e e t s _ {d}} [ L D A (t) ] _ {k}: k = 1, \dots , K\tag{4}
$$

To define an appropriate value for K, we construct LDA models for $\pmb { K } = \pmb { 2 0 } , \pmb { 3 0 } , \pmb { 4 0 } , \pmb { 5 0 } , \pmb { 6 0 } , \pmb { 7 0 }$ , calculating and plotting the average coherence [47] of each and selecting K at the inflection (elbow) point. We find that the inflection point occurs at $\pmb { K } = 4 \mathbf { 0 } . ^ { 8 }$ We, therefore, fix K = 40 to discover 40 latent topics capturing the general discussions on Twitter related to market performance [48,49].

## 3.4. Macroeconomic and market data

We control for various macroeconomic features that have been documented as having predictive power in predicting market returns [50,51]. We include term structure premium (Term), defined as the dif ference between 10-year Treasury notes and 3-month bill yield, default spread (DEF), defined as the Moody’s BAA corporate bond minus the vield of AAA corporate bond. short-term risk-free rate (Rate) using 3- month Treasury Bills, and the breakeven inflation rate (Inflation), which represents a measure of what the expected inflation will be in the next five years. We obtained these from the St. Louis Federal Reserve Bank. In addition, we add the Weekly Economic Index (WEI) to capture information from other real economic activities, such as consumer behavior, the labor market, and production [52]. In particular, the WEI is extracted from ten indicators of real economic activity by using principal component analysis (PCA) [53]. To control for investor sentiment outside of Twitter, we also include macroeconomic-focused sentiment measures—the one-year individual investor confidence index (LIndi\_Conf) and institutional investor confidence index (LInst\_ Conf) of the United States stock market [54]. Furthermore, we control for the valuation of the stock market using the log cyclically adjusted price-earnings ratio (LCAPE) [30]. We also include an auto-regressive term of the previous trading day’s return to explain the potential se rial correlation. Additionally, market volatility, a main factor in deter mining risk premiums, is also included. The return is based on the closing price, and volatility is defined as the standard deviation of the returns in the previous 30 trading days [30].

## 4. Investor sentiment and market predictability

## 4.1. Empirical models

Our empirical analysis focuses on the one-day-ahead prediction of the S&P500 index return using ordinary least squares (OLS) regression. Denote $R e t u r n _ { d }$ to be the S&P500 index return of the current trading day and Return as that of the previous trading day. Let X be the vector of predictors containing the macroeconomic variables and the two nonsocial-media-based sentiment indices, LIndi\_Conf and LInst\_Conf, described in Section 3.4. We devise two OLS models to investigate our hypothesis (H1) as follows:

$$
\text { Return } _ {d} = \alpha + \beta_ {3} ^ {*} \text { Return } _ {d - 1} + \beta_ {4} ^ {*} \text { Volatility } _ {d - 1} + \boldsymbol {\gamma} ^ {T} \boldsymbol {X} _ {d - 1} + \epsilon_ {d};\tag{5}
$$

$$
\begin{array}{l} R e t u r n _ {d} = \alpha + \beta_ {1} ^ {*} B u l l i s h n e s s _ {d - 1} + \beta_ {2} ^ {*} A g r e e m e n t _ {d - 1} + \beta_ {3} ^ {*} R e t u r n _ {d - 1} \\ \qquad + \beta_ {4} ^ {*} V o l a t i l i t y _ {d - 1} + \boldsymbol {\gamma} ^ {T} \boldsymbol {X} _ {d - 1} + \epsilon_ {d}. \end{array}\tag{6}
$$

The first model (Eq. 5) represents a conventional market-predicting model using the previous day’s market movement and macroeconomic metrics, while Model (6) updates (5) by including our WoM sentiment indices. We would like to emphasize that though various supervised learning methods can be used to train a predictive model, we use an OLS model due to its superior interpretability and suitability of pursuing our research aim of explaining the predictivity of a phenomenon rather than enhancing overall prediction performance.

## 4.2. Empirical results

We fit Models (5) and (6) for each of the three sample periods, respectively. In Table 2 we report coefficient estimates, adjusted R squared and F-statistics. The Newey-West standard error [55] with lag $= 5$ is shown in parenthesis under the coefficient estimates, and the statistical significance levels are indicated by the stars.

Based on columns 4–6 of Table $^ { 2 , }$ we find that by controlling for the market and macroeconomic variables, both Bullishness and Agreement are statistically significant at the $\alpha = 0 . 0 1$ significance level during the pre-COVID period. However, during the peak-COVID period these covariates are no longer statistically significant (H1a). The effects of Bullishness and Agreement remain insignificant during the recovery period (H1b). The values of the adjusted $\mathrm { R } ^ { 2 }$ also support this finding. Specifically, the addition of Bullishness and Agreement only adds pre dictive power when market conditions are normal—the adjusted $\mathtt { R } ^ { 2 }$ is more than double (increased from 0.044 (column 1) to 0.089 (column 4)) for the pre-COVID period. During the peak-COVID period, however, the adjusted $\mathrm { R } ^ { 2 }$ shows a negligible decrease (from 0.195 to 0.192). Although the adjusted R<sup>2</sup> $\mathrm { R } ^ { 2 }$ increases during the recovery period (comparing column 3 vs 6), the increase is much less pronounced compared to the pre-COVID period.

We also find that non-social-media-based sentiments (LIndi\_Conf, LInst\_Conf) are significant only in the pre-COVID period, but not in the other two when market conditions are anomalous. This is consistent with the pattern of our social media-based sentiment. This finding further confirms the widely documented evidence that investor senti ment is predictive of stock returns under normal market conditions. On the other hand, the empirical evidence showing the insignificance of these sentiment measures suggests that the effect and predictivity of investor sentiment may heavily depend on market conditions. Similar findings have been documented by Chung et al. [39], which show that the predictive power of investor sentiment is generally insignificant during a recession. Our findings provide the first empirical evidence that the predictivity of investor sentiment is weak and insignificant after the strike of the COVID-19 pandemic.

In addition to the model estimation results for each of the three pandemic phases, we further investigate how investor sentiment effect dynamically change over the entire sample. We adopt a rolling window

approach to repeatedly estimate Model (6) by rolling forward a single day at a time and showing the coefficient estimates of the sentiment indices Bullishness and Agreement. We set the length of the rolling window to 84, which is the number of trading days in a four-month period.<sup>9</sup>

Fig. 4 depicts the change of the estimated coefficients for Bullishness (green, top) and Agreement (blue, bottom), along with the 95% confi dence interval of each. Clearly, both coefficient estimates have greater degrees of fluctuation and much wider confidence intervals during peak COVID-19 than before. Noticeable fluctuations begin around February 25th, when the CDC warned that the COVID-19 outbreak was on course to be formally declared as a pandemic. Such empirical evidence further supports our intuition behind H1 as discussed in Section 2. While the confidence interval of the Agreement coefficient becomes narrower in late 2020 and beyond, the coefficient of Bullishness remains highly variable. Although the coefficients of both sentiment indices are not significant during peak-COVID and recovery periods, the change of their confidence intervals suggests that Bullishness is noisier even after entering the recovery period, while Agreement becomes more consistent.

## 4.3. Market predictability under different conditions

Our empirical models also allow us to investigate market predict ability under different conditions. To proceed, we examine the adjusted $\mathrm { R } ^ { 2 } { \mathrm { : } }$ , which can be used as an indicator of in-sample predictive power. The adjusted $\mathrm { R } ^ { 2 \cdot } s ,$ shown in Table 2, are 0.195 and 0.192 during the peak-COVID period, compared with 0.044 (or 0.062) and 0.089 (or 0.072) during the pre-COVID (or recovery) period. This finding suggests that overall market predictability is much higher during the highly volatile peak-COVID period than in other periods. This counterintuitive finding may be largely attributable to the increased predictivity of the one-day lagged return, as indicated by its estimated coefficients shown in Table 2. A possible explanation is market overreaction following a big event.

Finally, as a robustness check, we look into several alternative cut-off dates for the three periods. We find that the results are both qualitative and quantitatively similar to those reported in Table 2 for all alternative cut-off dates explored.<sup>10</sup>

## 5. Investor discussion and market predictability

Before examining the effects of the disaggregated latent topics on stock market returns and how such effects differ across different market conditions, we first identify the within-period relevant topics from a broader pool of topic information extracted from the raw tweets.

## 5.1. Identifying relevant topics – Ensemble feature selection

The LDA model extracted a pool of 40 different topics discussed across the general and stock-specific tweets. However, we conjecture that not all topics are relevant predictors of stock returns for each period. Rather, the chatter may reflect the spillover effect from the stock market. With this conjecture in mind, it is essential to identify relevant topics bearing the predictive and explanatory power of market returns.

To identify such topics, we propose an ensemble feature selection approach by considering various established feature selection tech niques in the statistics and machine learning literature. One advantage of ensemble learning is that it improves model reliability and robustness by overcoming the potential biases of adopting a single model. For our proposed feature selection ensemble, we apply each feature selection method to our adopted linear regression framework, with the 40 derived topics as predictors to be selected, controlling for all other variables from our prior sentiment analysis (see Table 2). We then adopt a voting strategy to rank the topics according to their selection frequency. Table 3 summarizes the feature selection methods we employed. All the methods are implemented with available R packages and are also specified in Table 3.

Table 2  
Coefficient estimates of Models (5) and (6) for pre-, peak-COVID, and recovery periods.

<table><tr><td rowspan="2"></td><td colspan="3">Without twitter sentiment</td><td colspan="3">With twitter sentiment</td></tr><tr><td>Pre-COVID(1)</td><td>Peak-COVID(2)</td><td>Recovery(3)</td><td>Pre-COVID(4)</td><td>Peak-COVID(5)</td><td>Recovery(6)</td></tr><tr><td>Constant</td><td>-0.215*(0.121)</td><td>-0.806**(0.408)</td><td>-0.288(0.388)</td><td>-0.260**(0.123)</td><td>-0.711*(0.410)</td><td>-0.289(0.394)</td></tr><tr><td>Bullishness</td><td></td><td></td><td></td><td>-0.013***(0.003)</td><td>0.003(0.013)</td><td>-0.027(0.034)</td></tr><tr><td>Agreement</td><td></td><td></td><td></td><td>0.211***(0.046)</td><td>0.125(0.182)</td><td>0.168(0.254)</td></tr><tr><td>LInst_Conf</td><td>0.094**(0.042)</td><td>-0.015(0.050)</td><td>-0.027(0.055)</td><td>0.089**(0.041)</td><td>-0.009(0.052)</td><td>-0.022(0.053)</td></tr><tr><td>LIndi_Conf</td><td>-0.040*(0.022)</td><td>0.156(0.106)</td><td>-0.005(0.022)</td><td>-0.040*(0.022)</td><td>0.135(0.105)</td><td>-0.006(0.022)</td></tr><tr><td>Return</td><td>-0.121**(0.061)</td><td>-0.461***(0.127)</td><td>-0.201***(0.057)</td><td>-0.068(0.059)</td><td>-0.470***(0.123)</td><td>-0.164**(0.080)</td></tr><tr><td>Volatility</td><td>0.750**(0.341)</td><td>-0.248(0.286)</td><td>2.405***(0.636)</td><td>0.809**(0.329)</td><td>-0.309(0.281)</td><td>2.109***(0.739)</td></tr><tr><td>Rate</td><td>-0.012**(0.006)</td><td>0.017(0.013)</td><td>0.125**(0.064)</td><td>-0.010*(0.006)</td><td>0.016(0.013)</td><td>0.117*(0.068)</td></tr><tr><td>DEF</td><td>0.007(0.011)</td><td>0.054***(0.016)</td><td>0.033*(0.020)</td><td>0.010(0.012)</td><td>0.057***(0.017)</td><td>0.039**(0.019)</td></tr><tr><td>TERM</td><td>-0.009(0.008)</td><td>0.015(0.020)</td><td>-0.0004(0.009)</td><td>-0.005(0.008)</td><td>0.012(0.020)</td><td>0.004(0.010)</td></tr><tr><td>Inflation</td><td>0.003(0.012)</td><td>0.012(0.013)</td><td>0.002(0.011)</td><td>-0.001(0.012)</td><td>0.010(0.013)</td><td>-0.001(0.011)</td></tr><tr><td>WEI</td><td>0.004**(0.002)</td><td>0.001(0.001)</td><td>0.0005(0.0004)</td><td>0.002(0.002)</td><td>0.001(0.001)</td><td>0.0004(0.0004)</td></tr><tr><td>LCAPE</td><td>-0.006(0.043)</td><td>0.037(0.091)</td><td>0.103*(0.055)</td><td>0.015(0.045)</td><td>0.027(0.092)</td><td>0.100(0.061)</td></tr><tr><td>N (obs.)</td><td>201</td><td>225</td><td>152</td><td>201</td><td>225</td><td>152</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.044</td><td>0.195</td><td>0.062</td><td>0.089</td><td>0.192</td><td>0.072</td></tr><tr><td>F Statistic</td><td>1.930**</td><td>6.422***</td><td>1.990**</td><td>2.632***</td><td>5.445***</td><td>1.970**</td></tr></table>

Note: \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

![](/api/attachments/U5KKBXC5/fulltext/images/c9082da997eac78ac7298f456ffc93230af6aa6ba0dacef19a80b6661c4cc5ae.jpg)

![](/api/attachments/U5KKBXC5/fulltext/images/6a5da012297c33e2e158e2533318d575efd57969a7d1c1bc8fa70c78a53cc3aa.jpg)  
Fig. 4. Change in coefficient estimates of Bullishness and Agreement based on Model (3) using a rolling-window approach.

Table 3  
Description of adopted feature selection methods.

<table><tr><td>Method and R package</td><td>Description</td></tr><tr><td>Stepwise [56];R function step()</td><td>Iteratively adding and removing one predictor at a time in OLS estimation. Stops when certain statistics (e.g., AIC or BIC) reach to minimum. In our analysis, we use both AIC and BIC, respectively, as two alternatives. AIC and BIC are defined as:  $AIC = -2log(L) + 2p$ ;  $BIC = -2log(L) + plog(n)$ , where L is likelihood, p is the number of predictors and n is sample size. In general, BIC encourages simpler model (less variables) than AIC.</td></tr><tr><td>Lasso [57];R package: glmnet [58]</td><td>Minimizes residual sum squares subject to the sum of absolute value of coefficients being less than a constant. It estimates the coefficients and selects variables simultaneously by shrinking some coefficient estimates to exactly 0. Specifically, the Lasso estimator is of the form $\widehat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta}} \frac{1}{n} \sum_{i=1}^{n} \left( Y_i - x_i^T \boldsymbol{\beta} \right)^2 + \lambda \| \boldsymbol{\beta} \|_1$ ,where  $\lambda$  is a tuning parameter that controls the shrinkage level, and  $\| \boldsymbol{\beta} \|_1$  is the  $L_1$  norm of coefficient vector  $\boldsymbol{\beta}$ . The choice of  $\lambda$  is usually determined by cross-validation.</td></tr><tr><td>Elastic Net [59];R package: glmnet [58]</td><td>Derived based on Lasso, elastic net incorporates an additional penalty term,  $L_2$ -penalty, to overcome issues such as multicollinearity. The objective function of elastic net is $\widehat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta}} \frac{1}{n} \sum_{i=1}^{n} \left( Y_i - x_i^T \boldsymbol{\beta} \right)^2 + \lambda_1 \| \boldsymbol{\beta} \|_1 + \lambda_2 \| \boldsymbol{\beta} \|_2$ .</td></tr><tr><td>Adaptive Lasso [60];R package: glmnet [58]</td><td>Motivated by Lasso estimator, adaptive lasso incorporates a weight for each coefficient in the penalty function, i.e.,  $p_\lambda \left( \beta_j \right) = \lambda w_j | \beta_j |$ . The weight is often chosen as  $w_j = \left| \widetilde{\beta}_j \right|^ {-1}$ , where  $\widetilde{\beta}_j$  denote an initial estimate of  $\beta_j$ , e.g., OLS estimate. Adaptive Lasso enjoys the oracle property, that is, the estimator performs as well as if the true underlying model were given in advance.</td></tr><tr><td>SCAD [61];R package: ncvreg [62]</td><td>Instead of the  $L_1$ -penalty in Lasso, SCAD uses a nonconcave penalty function, namely, smoothly clipped absolute deviation penalty. This penalty function is bounded from above to reduce bias, and the estimates enjoys the oracle property. The SCAD penalty function is defined by its first order derivative $p'_\lambda(\boldsymbol{\beta}) = \lambda \left\{ I(\boldsymbol{\beta} \leq \lambda) + \frac{(a\lambda - \boldsymbol{\beta})_+}{(a-1)\lambda} I(\boldsymbol{\beta} > \lambda) \right\}$ ,where  $\lambda$  is the shrinkage tuning parameter and a is a positive constant that is usually set to 3.7.</td></tr><tr><td>MCP [63];R package: ncvreg [62]</td><td>Similar to SCAD, MCP uses a nonconcave penalty function, namely, minimax concave penalty. This penalty introduces even less bias for the penalized estimates. The MCP penalty function is defined as  $p(\boldsymbol{\beta}) = \lambda | \boldsymbol{\beta}| - \frac{\boldsymbol{\beta}^2}{2a}$  if  $|\boldsymbol{\beta}| \leq a\lambda$ , and  $p(\boldsymbol{\beta}) = \frac{a\lambda^2}{2}$  otherwise. The hyperparameter a is usually set to 3.</td></tr><tr><td>LAD-Lasso [64];R package: rqPen [65]</td><td>Achieves robust variable selection as the  $L_1$ -penalty is combined with the absolute loss. LAD-Lasso estimator is $\widehat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta}} \frac{1}{n} \sum_{i=1}^{n} |Y_i - x_i^T \boldsymbol{\beta}| + \lambda \| \boldsymbol{\beta} \|_1$ .</td></tr><tr><td>SPSP-Lasso [66]R package: SPSP [67]</td><td>SPSP-Lasso partitions the entire solution paths of Lasso method for a wide range of tuning parameter  $\lambda$ . This partitioning algorithm identifies the “relevant” and “irrelevant” sets of covariates.</td></tr></table>

Except for the stepwise method, all other feature selection methods fall into the category of penalized methods in which the estimators are expressed as:

$$
\widehat {\boldsymbol {\beta}} = \underset {\boldsymbol {\beta}} {\operatorname{argmin}} \frac {1}{n} \sum_ {i = 1} ^ {n} L \left(Y _ {i} - \boldsymbol {x} _ {i} ^ {T} \boldsymbol {\beta}\right) + p _ {\lambda} (\boldsymbol {\beta}),
$$

where $\beta$ is the vector of coefficients that need to be estimated, $\boldsymbol { L } ( \boldsymbol { u } )$ is an arbitrary loss function, typically squared loss, $\mathrm { i . e . , } L ( u ) = u ^ { 2 } . $ , and $p _ { \lambda } ( \pmb { \beta } )$ is a penalty function that penalizes the model coefficients such that insignificant features are shrunk to 0 and are thus dropped. The tuning parameter λ of the penalty function, often called the shrinkage param eter, controls model sparsity. The optimal value of λ can be determined through data-driven approaches such as cross-validation. To reduce the sampling variability of cross-validation, we repeat each method 100 times and then aggregate the selection results. Specifically, denote $T P _ { i , j } ^ { ( l ) } = 1$ if topic i is selected by method j in the lth run, and 0 otherwise. For each topic i we then compute the quantity $\begin{array} { r } { S _ { i } = \frac { 1 } { 1 0 0 } \sum _ { l = 1 } ^ { 1 0 0 } \sum _ { j = 1 } ^ { 9 } T P _ { i , j } ^ { ( l ) } , } \end{array}$ which determines the ranking of topic i for $i = 1 , . . . , 4 0$ . The larger the $S _ { i ; }$ the higher topic i is ranked as a candidate market returns predictor.

Fig. 5 shows the top ten ranked topics for each sample period. Clearly, there are few overlapping topic labels over the three periods. Interestingly, the selected topics are more consistent across different methods in the peak-COVID period when compared to the other two periods. For example, topic 39 is consistently selected by 7 out of 9 methods, and topics 27, 40, and 35 are selected by >5 methods. We further find that the adopted feature selection methods tend to select more topics during the peak-COVID period than the other two sample periods: the average number of selected topics is 3.6 in the peak-COVID period, compared to 2.2 (pre-COVID) and 0.7 (recovery). This finding is consistent with the “votes” depicted in Fig. 5, suggesting that the topics of investor’s discussion may provide much stronger signals and higher predictive power during the most volatile market period relative to the other two periods.

On the other hand, the recovery period topic information provides the weakest signal. For instance, the most ensemble-voted topic (topic 31) has only two votes from the nine methods with the rest receiving 1 or fewer. This may imply that the topic information in the recovery period is strongly disseminated and dispersed. A possible explanation is that, with the “new norm” in place, previously overlooked social media-based investment information is quickly cooling to have little impact on the stock market. This is also consistent with our previous findings shown in Table 2, where the predictability of investor sentiment during the re covery period is even lower than that in the pre-COVID period. With these findings in mind, we formally examine the composition of each topic selected, as well as the explanatory and predictive power of this disaggregated WoM information on the stock market in the next section, using empirical models similar to those specified in Section 4.1.

## 5.2. Latent topic predictivity

We first examine the composition of the selected topics in order to better understand the online WoM discussion patterns surrounding the stock market across our defined periods of study. We focus on the top 5 selected topics for each sample period (Fig. 5), displaying each in terms of the top identifying keywords, shown left to right, highest to lowest in Table 4. For convenience and ease in interpretation we also assign a label to each topic.

We notice that the within-period terms describing each topic are fairly unique to each period. Pre-COVID period terms center around

![](/api/attachments/U5KKBXC5/fulltext/images/c1ea084deb566dbf58c500bb1018ec285586c525c3cb09f60b237d6f6aaebc2f.jpg)

![](/api/attachments/U5KKBXC5/fulltext/images/f767dab1d352a1ddbf7690c5d7ebd7250b9443810b04b7bf3ef28b53eb2892c7.jpg)

![](/api/attachments/U5KKBXC5/fulltext/images/e941084126100eee2cc5bc973dfd790679b2ae14e82d7047ca0738c26ffa7189.jpg)  
Fig. 5. Top 10 most selected topics from ensemble feature selection for each sample period.

Table 4  
Top keywords of the five highest-ranked latent topics as shown in Fig. 5.

<table><tr><td>Period</td><td>Top Index</td><td>Label</td><td>Description</td></tr><tr><td rowspan="6">Pre-COVID</td><td>19</td><td>Short-term Options</td><td>call, week, put, next, see, today, last, day, back, look</td></tr><tr><td>29</td><td>Technical Analysis</td><td>high, day, best, low, sinc, close, new, worst, later, avg</td></tr><tr><td>13</td><td>Tech Stocks</td><td>amzn, aapl, tsla, fb, spi, msft, nvda, amd, nflx, qqq&#x27;</td></tr><tr><td>11</td><td>Trending Stocks</td><td>atus, via, amp, vra, project, futu, thank, sofi, ge, list</td></tr><tr><td>3</td><td>Long-term Purchase Analysis</td><td>buy, \xe2\x80\x9c, \xe2\x80\x9d, rate, hold, analyst, upgrad, research, travel, receiv</td></tr><tr><td>39</td><td>Recs and Analysis</td><td>1, 2, 3, 5, 4, 10, top, 6, 7, 8</td></tr><tr><td rowspan="5">Peak-COVID</td><td>27</td><td>Stocks and Vaccine</td><td>dow, us, vaccin, point, stock, market, china, bntx, street, byd</td></tr><tr><td>40</td><td>Growth Investing</td><td>compani, growth, amp, tech, data, product, year, strength, potenti, busi</td></tr><tr><td>35</td><td>Casino Stocks</td><td>tel, mgm, plan, czr, opti, \xf0\x9f\x94\xa5, xspa, gmbI, aex, wynn</td></tr><tr><td>15</td><td>News</td><td>amp, peopl, media, us, luna, say, job, social, care, stock</td></tr><tr><td>31</td><td>Options Trading</td><td>option, maxpain, expir, max, disney, di, oi, nqf, gem, log</td></tr><tr><td rowspan="4">Recovery</td><td>21</td><td>Banks and Options</td><td>ba, pt., 500, optionsflow, jpm, sampp, \xf0\x9f\x93\x88, cat, previous, usd</td></tr><tr><td>13</td><td>Tech Stocks</td><td>amzn, aapl, tsla, fb, spi, msft, nvda, amd, flx, qqq</td></tr><tr><td>5</td><td>Meme Stocks</td><td>amc, nio, gme, penn, aal, spce, wkh, mrna, nok, sndl</td></tr><tr><td>11</td><td>Trending Stocks</td><td>atus, via, amp, vra, project, futu, thank, sofi, ge, list</td></tr></table>

Table 5  
Assessing improvement with topic information.

<table><tr><td></td><td>Pre-COVID</td><td>Peak-COVID</td><td>Recovery</td></tr><tr><td colspan="4">Adjusted  $R^2$ </td></tr><tr><td>With topics</td><td>0.131</td><td>0.262</td><td>0.100</td></tr><tr><td>Without topics</td><td>0.089</td><td>0.192</td><td>0.072</td></tr><tr><td colspan="4">AIC</td></tr><tr><td>With topics</td><td>-1407.5</td><td>-1109.7</td><td>-1023.5</td></tr><tr><td>Without topics</td><td>-1402.6</td><td>-1094.0</td><td>-1023.1</td></tr><tr><td colspan="4">Likelihood Ratio Test</td></tr><tr><td>Chisq</td><td>14.889</td><td>25.779</td><td>10.365</td></tr><tr><td>p-value</td><td>0.011</td><td>&lt;0.001</td><td>0.066</td></tr></table>

option-related content, technical analysis (topics 19, 29, and 3), and a variety of stocks (topics 13 and 11), which is what we might expect during normal market conditions. During peak-COVID, however, the market-indicative topics of conversation shifted. Topic 39 is particularly enigmatic. These tweets predominantly consist of recommended stocks (e.g., Top 10 lists) and analysis of specific stocks (e.g., stock X is down by Y%).<sup>11</sup> This may suggest that individuals paid closer attention to this type of information during highly volatile markets. It may also be attributable to the tremendous increase in less-experienced retail investors who heavily rely on social media-based trading information. Additionally, topic 15 suggests that investors are more responsive to news events, with topic 27 further suggesting that vaccine speculation and discussion as being a particularly relevant and important type of news/discussion. Finally, casino-focused stocks (topic 35) are also indicative of returns during this period. Since these companies rely on foot-traffic, they may represent a proxy for investor concerns sur rounding general consumer mobility, which in turn affects the market as a whole.

The relevant topics during the recovery period are completely different from those of the peak-COVID period, but partially overlap with those of the pre-COVID period (topics 11 and 13). This overlap gives credence to the recovery narrative, suggesting a partial reversion to this earlier period. The non-overlapping topics (topics 5, 21, 31) focus on specific stocks (topic 5) and options (topics 21 and 31). Topics 21 and 31 further suggest a partial reversion to pre-COVID conditions since it centers on a particular financial instrument (options), which overlaps with the content of some of the topics of the pre-COVID period.

To quantify the explanatory and predictive power of topic informa tion, we follow the empirical models discussed in Section 4.1.<sup>12</sup> Specifically, for each sample period, we fit the following model

$$
\begin{array}{l} R e t u r n _ {d} = \alpha + \beta_ {1} ^ {*} B u l l i s h n e s s _ {d - 1} + \beta_ {2} ^ {*} A g r e e m e n t _ {d - 1} + \beta_ {3} ^ {*} R e t u r n _ {d - 1} \\ \quad + \beta_ {4} ^ {*} V o l a t i l i t y _ {d - 1} + \boldsymbol {\gamma} ^ {T} \boldsymbol {X} _ {d - 1} + \boldsymbol {\eta} ^ {T} \boldsymbol {Z} _ {d - 1} + \epsilon_ {d}, \end{array}\tag{7}
$$

where Z denote the vector of the top 5 selected topics for each period as the additional predictors.<sup>13</sup>

We assess the additional explanatory and predictive power carried by the top five latent topics by comparing several statistics between Models (7) and (6) for each sample period. In Table $^ { 5 , }$ both the adjusted $\mathrm { R } ^ { 2 }$ and AIC values indicate that the inclusion of topic information im proves the model fitting. The peak-COVID period shows the biggest improvement and the recovery period the lowest; the AIC in particular changes little during the recovery period. To further confirm this, we conduct the likelihood ratio test; the bottom of Table 5 shows the results. Clearly, the inclusion of topic information adds the most explanatory and predictive power for the peak-COVID period, with a p-value smaller than 0.001. In contrast, the effects of topic information in the recovery period are not statistically significant at the 0.05 significance level.

## 6. Discussion and conclusions

The onset of COVID-19 created unprecedented stock market vola tility. Among a variety of factors, our study focuses on social media WoM and analyzes the association between stock market performance, $\mathrm { i . e . , }$ S&P500 index return, and both aggregate (e.g., sentiment) and dis aggregated $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } _ { }$ , latent topics) information derived from millions of tweets across three disparate periods, pre-COVID, peak-COVID, and re covery. By controlling for traditional micro- and macroeconomic vari ables, we contrast the effects of online WoM between the three phases of the pandemic. Our empirical results show that for both peak-COVID and recovery periods, two sentiment indices, Bullishness and Agreement, are less predictive of day-ahead market returns than during normal (pre-COVID) market conditions. Our empirical findings also show that the day-ahead predictive model has a higher adjusted $\mathrm { R } ^ { 2 }$ during the peak COVID period when market conditions are more volatile than in the other two periods, which is possibly attributable to market overreaction, as suggested by the statistically significant negative effect of the previ ous day’s market return.

Building upon these findings, we examine the predictive and explanatory power of disaggregated information represented by latent topics, which capture investors’ discussion patterns. We introduce an ensemble feature selection procedure that consists of nine popular feature selection methods to uncover the most predictive topics in each period. We find little overlap between the predictive topics in each period. With an addition of the top 5 selected topics for each phase of the pandemic, our predictive model gains a substantial improvement for the peak-COVID period as measured by several statistics. At the same time, it is weakest and insignificant during the recovery period.

Our study makes several contributions to decision support systems literature. As mentioned in our literature review, past decision-focused works $[ 3 , 4 , 6 , 1 8 , 1 9 ]$ have examined and forecasted financial markets through various text-focused lenses. These works emphasize aiding in vestment decisions through such sources but do so during stable market conditions. On the other hand, this work examines and predicts financial markets before, during, and in the aftermath of a maior socioeconomic disaster. Thus, we can contribute to this broader literature by showing the market indicators driving investment decisions during such an event through the lens of readily accessible social media data. Our work im plies that investors may need an enhanced decision-making system to detect and alter the prediction models under different market condi tions. Investment decision-makers may therefore use our findings if similar conditions arise in the future.

Our analysis informs firms, financial investors, and policymakers in the following ways. First, since Bullishness and Agreement only add predictive power when market conditions are normal, individuals and institutions are advised to exclude social media sentiment from their market forecasting models during times of economic upheavals such as global pandemics. Secondly, they can expect changes in the market explainability of traditional indicators during a pandemic. Therefore, market forecasting models should be continuously fine-tuned as the disruption unfolds. Our topic-focused analysis shows that retail in vestors pay closer attention to specific stocks during times of uncer tainty, suggesting a ‘herd mentality’ effect. Close attention should be paid to emerging topics such as vaccinations, lockdowns, and foot traffic-dependent businesses, such as casinos, as these immediately impact the short-term market conditions, which are expected. Finally, during a major disruption, market analysts should take advantage of extrinsic signals, such as topic information in social media, to optimize the utility of their forecasting models.

Admittedly, our study has some limitations and potential for future work. First, while our study focused on stock market returns, it may also be interesting to investigate other key metrics such as volatility and trading volume, as in [2]. Alternative measures of sentiment may also provide additional insights should they be investigated in future work. Next, latent topic extraction is a notoriously imprecise method category. While we perform several robustness, the generalizability of this meth odology can still be viewed as a limitation. Alternate approaches to LDA may therefore also be explored in future work, though they are known to suffer from similar shortcomings. Finally, instead of exploring causality, our study focuses on examining the predictive and explanatory power of social media WoM on market movement. Future work can build upon our research by developing quasi-causal methods to identify specific causal relationships.

## CRediT authorship contribution statement

Xiaorui Zhu: Conceptualization, Methodology, Software, Formal analysis, Investigation, Resources, Data curation, Writing – original draft, Writing – review & editing, Visualization. Shaobo Li: Conceptu alization, Methodology, Software, Formal analysis, Investigation, Re sources, Data curation, Visualization, Writing – original draft, Writing – review & editing. Karthik Srinivasan: Conceptualization, Methodol ogy, Writing – original draft, Writing – review & editing. Michael T. Lash: Conceptualization, Methodology, Software, Formal analysis, Investigation, Resources, Data curation, Visualization, Project adminis tration, Writing – original draft, Writing – review & editing.

## Declaration of Competing Interest

There are no competing interests or funding to report.

## Data availability

Data will be made available on request.

## References

[1] J. Cox, D.L. Greenwald, S.C. Ludvigson, What Explains the COVID-19 Stock Market? National Bureau of Economic Research (NBER), 2020, pp. 1–36.

[2] W. Antweiler, M.Z. Frank, Is all that talk just noise? The information content of internet stock message boards, J. Financ. 59 (2004) 1259–1294, https://doi.org 10.1111/i.1540-6261.2004.00662.x

[3] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, J. Comput. Sci. 2 (2011). https://doi.org/10.1016/i.iocs.2010.12.007.

[4] J. Piñeiro-Chousa, M. Vizcaíno-González, A.M. Pérez-Pico. Influence of social media over the Stock market, Psychol. Mark. 34 (2017) 101–108, https://doi,org 10.1002/mar 20976

[5] Y. Xu, Z. Liu, J. Zhao, C. Su, Weibo sentiments and stock return: a time-frequency view, PLoS One 12 (2017) https://doi org/10.1371/iournal pone 0180723

[6] S. Deng, Z. Huang, A.P. Sinha, H. Zhao, The interaction between microblog sentiment and stock returns: an empirical examination, MIS Q. 42 (2018), https:// doi.org/10.25300/MISQ/2018/14268.

[7] H. Nguyen, R. Calantone, R. Krishnan, Influence of social media emotional word of mouth on institutional investors’ decisions and firm value, Manag. Sci. 66 (2020), https://doi.org/10.1287/mnsc.2018.3226.

[8] M. Baker, J. Wurgler, Investor sentiment and the cross-section of stock returns, J. Financ. 61 (2006). https://doi.org/10.1111/i,1540-6261.2006.00885.x.

[9] D. Huang, F. Jiang, J. Tu, G. Zhou, Investor sentiment aligned: a powerful predictor of stock returns, Rev. Financ. Stud. 28 (2015) 791–837, https://doi.org/10.1093/ rfs/hhu080.

[10] S. Ramelli, A.F. Wagner, Feverish stock price reactions to COVID-19, Rev. Corp. Financ. Stud. 9 (2020), https://doi.org/10.1093/rcfs/cfaa012.

[11] U. Chatterjee, J.J. French, A note on tweeting and equity markets before and during the Covid-19 pandemic, Financ. Res. Lett. 46 (2022), https://doi.org/ 10.1016/j.frl.2021.102224.

[12] K. John, J. Li, COVID-19, volatility dynamics, and sentiment trading, J. Bank. Financ. 133 (2021), https://doi.org/10.1016/i.ibankfin.2021.106162.

[13] A.S. Baig, H.A. Butt, O. Haroon, S.A.R. Rizvi, Deaths, panic, lockdowns and US equity markets: the case of COVID-19 pandemic, Financ. Res. Lett. 38 (2021), https://doi.org/10.1016/j.frl.2020.101701.

[14] A. Gupta, C. Shaju, Pratibha, Kamal, a study of the international Stock market behavior during COVID-19 pandemic using a driven iterated function system, Comput. Econ. (2021), https://doi.org/10.1007/s10614-021-10199-2.

[15] R. Chaudhary, P. Bakhshi, H. Gupta, Volatility in international Stock markets: an empirical study during COVID-19, J. Risk Financ. Manag. 13 (2020), https://doi. org/10.3390/jrfm13090208.

[16] Y. Liu, Y. Wei, Q. Wang, Y. Liu, International stock market risk contagion during the COVID-19 pandemic, Financ. Res. Lett. 45 (2022), https://doi.org/10.1016/j. frl.2021.102145.

[17] M. Trusov, R.E. Bucklin, K. Pauwels, Effects of word-of-mouth versus traditional marketing: findings from an internet social networking site, J. Mark. 73 (2009), https://doi.org/10.1509/jmkg.73.5.90.

[18] Y. Yu, W. Duan, Q. Cao, The impact of social and conventional media on firm equity value: a sentiment analysis approach, Decis. Support. Syst. 55 (2013) 919–926. https://doi.org/10.1016/LDSS.2012.12.028.

[19] C.S. Ho, P. Damien, B. Gu, P. Konana, The time-varying nature of social media sentiments in modeling stock returns, Decis. Support. Syst. 101 (2017) 69–81, https://doi.org/10.1016/J.DSS.2017.06.001.

[20] Y. Ge, J. Qiu, Z. Liu, W. Gu, L. Xu, Beyond negative and positive: exploring the effects of emotions in social media during the stock market crash, Inf. Process. Manag. 57 (2020). https://doi.org/10.1016/i.ipm.2020.102218.

[21] D. Slof, F. Frasincar, V. Matsiiako, A competing risks model based on latent Dirichlet allocation for predicting churn reasons. Decis, Support. Syst. 146 (2021). https://doi.org/10.1016/i.dss.2021.113541.

[22] K.R. Larsen, D.E. Monarchi, D.S. Hovorka, C.N. Bailey, Analyzing unstructured text data: using latent categorization to identify intellectual communities in information systems, Decis. Support. Syst. 45 (2008), https://doi.org/10.1016/j. dss.2008.02.009.

[23] W. Fan, M.D. Gordon, The power of social media analytics, Commun, ACM 57 (2014), https://doi.org/10.1145/2602574

[24] T.O. Sprenger, A. Tumasjan, P.G. Sandner, I.M. Welpe, Tweets and trades: the information content of stock microblogs, Eur. Financ. Manag. 20 (2014) 926–957, https://doi.org/10.1111/i.1468-036X.2013.12007.x.

[25] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, J. Mach. Learn. Res. 3 (2003) 993–1022. http://dl.acm.org/citation.cfm?id=944919.944937.

[26] D.E. Rapach, J.K. Strauss, G. Zhou, Out-of-sample equity premium prediction: combination forecasts and links to the real economy, Rev. Financ. Stud. 23 (2010), https://doi.org/10.1093/rfs/hhp063.

[27] I. Welch, A. Goyal, A comprehensive look at the empirical performance of equity premium prediction, Rev. Financ. Stud. 21 (2008), https://doi.org/10.1093/rfs/ hhm014.

[28] C.M.K. Cheung, D.R. Thadani, The impact of electronic word-of-mouth communication: a literature analysis and integrative model, Decis. Support. Syst. 54 (2012), https://doi.org/10.1016/j.dss.2012.06.008.

[29] H. Hong, J.D. Kubik, J.C. Stein, Thy neighbor’s portfolio: word-of-mouth effects in the holdings and trades of money managers, J. Financ. 60 (2005), https://doi.org 10.1111/i.1540-6261.2005.00817.x.

[30] R.J. Shiller, Irrational Exuberance, Princeton University Press, 2016, https://doi. org/10.1515/9781400865536

[311. E. Black, Noise, J Financ, 41 (1986) 528–543. https://doi,org/10.1111/J.1540 6261.1986.TB04513.X.

[32] B.S.J. Grossman, J.E. Stiglitz, On the impossibility of informationally efficient, Am. Econ, Rev, 70 (1980).

[33] S. Grossman, On the efficiency of competitive Stock markets where trades have diverse information, J. Financ. 31 (1976) 573–585, https://doi.org/10.1111/ i.1540-6261.1976.tb01907.x.

[34] D. Kahneman, A. Tversky, Prospect theory: An analysis of decision under risk, in: Experiments in Environmental Economics, 1979, pp. 263–292, https://doi.org/ 10.2307/1914185

[35] E.F. Fama, Efficient capital markets: a review of theory and empirical work. J. Financ. 25. (1970). https://doi org/10.2307/2325486

[36] A. Shleifer, L.H. Summers, The noise trader approach to finance, J. Econ. Perspect. 4 (1990). https://doi,org/10.1257/iep.4.2.19.

[37] P. Jiao, A. Veiga, A. Walther, Social media, news media and the stock market, J. Econ. Behav. Organ. 176 (2020) 63–90, https://doi.org/10.1016/j. jebo.2020.03.002.

[38] A.W. Lo, The adaptive markets hypothesis, J. Portf. Manag. 30 (2004), https://doi. org/10.3905/jpm.2004.442611.

[39] S.L. Chung, C.H. Hung, C.Y. Yeh, When does investor sentiment predict stock returns? J. Empir. Financ. 19 (2012) https://doi.org/10.1016/j. jempfin.2012.01.002.

[40] P. Glasserman, K. Krstovski, P. Laliberte, H. Mamaysky, Choosing news topics to explain stock market returns, in: ICAIF 2020 - 1st ACM International Conference on AI in Finance, 2020, https://doi.org/10.1145/3383455.3422557.

[41] Z. Ke, B.T. Kelly, D. Xiu, Predicting returns with text data, SSRN Electron. J. (2019), https://doi.org/10.2139/ssrn.3489226

[42] P. Gjerstad, P.F. Meyn, P. Molnar, ´ T.D. Næss, Do president Trump’s tweets affect financial markets? Decis. Support. Syst. 147 (2021) https://doi.org/10.1016/j. dss.2021.113577.

[43] S. Aziz, M. Dowling, H. Hammami, A. Piepenbrink, Machine learning in finance: a topic modeling approach, Eur. Financ. Manag. (2021), https://doi.org/10.1111/ eufm.12326.

[44] A.H. Huang, R. Lehavy, A.Y. Zang, R. Zheng, Analyst information discovery and interpretation roles: a topic modeling approach, Manag, Sci. 64 (2018) 2833–2855 https://doi.org/10.1287/mnsc.2017.2751.

[45] N.F. Ibrahim, X. Wang, A text analytics approach for online retailing service improvement: evidence from twitter, Decis. Support. Syst. 121 (2019), https://doi. org/10.1016/j.dss.2019.03.002

[46] C. Hutto, E. Gilbert, Vader: A parsimonious rule-based model for sentiment analysis of social media text, in: Proceedings of the Eighth International AAAI Conference on Web and Social Media, 2014, p. 18.

[47] M. Roder, ¨ A. Both, A. Hinneburg, Exploring the space of topic coherence measures, in: WSDM 2015 - Proceedings of the 8th ACM International Conference on Web Search and Data Mining. 2015. https://doi.org/10.1145/2684822.2685324

[48] T.H. Nguyen, K. Shirai, Topic modeling based sentiment analysis on social media for stock market prediction, in: ACL-IJCNLP 2015 - 53rd Annual Meeting of the Association for Computational Linguistics and the Zth International Joint Conference on Natural Language Processing of the Asian Federation of Natura Language Processing, Proceedings of the Conference, 2015, https://doi.org/ 10.3115/v1/p15-1131

[49] J. Si, A. Mukherjee, B. Liu, Q. Li, H. Li, X. Deng, Exploiting topic based twitte sentiment for stock prediction, in: ACL 2013 - 51st Annual Meeting of the Association for Computational Linguistics, Proceedings of the Conference, 2013

[50] F. Jiang, J. Lee, X. Martin, G. Zhou, Manager sentiment and stock returns, J. Financ. Econ. 132 (2019) 126–149, https://doi.org/10.1016/j. ifineco.2018.10.001

[51] L. Sun, M. Najand, J. Shen, Stock return predictability and investor sentiment: a high-frequency perspective, J. Bank. Financ. 73 (2016) 147–164. https://doi,org 10.1016/i ibankfin 2016.09.010

[52] D. Lewis, K. Mertens, J.H. Stock, U.S. Economic Activity During the Early Weeks of the The SARS-COV-2 Outbreak, National Bureau of Economic Research (NBER), 2020, pp. 1–16.

[53] J.H. Stock, M.W. Watson, Forecasting using principal components from a large number of predictors, J. Am. Stat. Assoc. 97 (2002) 1167–1179, https://doi.org/ 10.1198/016214502388618960

[54] R.J. Shiller, Measuring bubble expectations and investor confidence, J. Psychol Financ, Markets 1 (2000).

[55] K.D. West, Discussion of Lazarus, Lewis, Stock, and Watson, “HAR inference: recommendations for practice,”, J. Bus. Econ. Stat. 36 (2018) 560–562, https:// doi.org/10.1080/07350015.2018.1505627.

[56] R.R. Hocking, A biometrics invited paper. The analysis and selection of variables in linear regression, Biometrics. 32 (1976), https://doi.org/10.2307/2529336.

[57] R. Tibshirani, Regression selection and shrinkage via the lasso, J. R. Stat, Soc. B 58 (1996) 267–288

[58] J. Friedman, T. Hastie, R. Tibshirani, Regularization paths for generalized linear models via coordinate descent, J. Stat. Softw. 33 (2010), https://doi.org 10.18637/iss.v033.i01

[59] H. Zou, T. Hastie, Regularization and variable selection via the elastic-net, J. R.

[60] H. Zou, The adaptive lasso and its Oracle properties, J. Am. Stat. Assoc. 101 (2006) 1418-1429.

[61] J. Fan, R. Li, Variable selection via nonconcave penalized likelihood and its oracle properties, J. Am. Stat. Assoc. 96 (2001), https://doi.org/10.1198/ 016214501753382273.

[62] P. Breheny, J. Huang, Coordinate descent algorithms for nonconvex penalized regression, with applications to biological feature selection, Ann. Appl. Stat. 5 (2011), https://doi.org/10.1214/10-AOAS388.

[63] C.H. Zhang, Nearly unbiased variable selection under minimax concave penalty, Ann. Stat, 38 (2010). https://doi,org/10.1214/09-AOS729

[64] H. Wang, G. Li, G. Jiang, Robust regression shrinkage and consistent variable selection through the LAD-lasso, J. Bus. Econ. Stat. 25 (2007), https://doi.org 10.1198/073500106000000251

[65] B. Sherwood, A. Maidman, rqPen: PenalizedOuantile Regression, 2020

[66] Y. Liu, P. Wang, Selection by partitioning the solution paths, Electron. J. Stat. 12 (2018). https://doi org/10.1214/18-EJS1434

[67] X. Rui, Y. Lui, P. Wang, SPSP: Selection by Partitioning the Solution Path, 2022.

Xiaorui Zhu is an assistant professor of business analytics in the College of Business and Economics at Towson University. Xiaorui obtained his Ph.D. in Business Analytics from th

Lindner College of Business, the University of Cincinnati in 2022. His research interests include high-dimensional statistical inference, machine learning, risk management, finance, and creativity in open online learning.

Shaobo Li is an Assistant Professor of Business Analytics in the School of Business, University of Kansas. His research has appeared in top business and statistics journals such as Marketing Science and Journal of the American Statistical Association. He earned PhD of Business Administration from University of Cincinnati.

Karthik Srinivasan is an assistant professor of business analytics in the school of business at University of Kansas. Karthik got his PhD in Management Information Systems from th Eller College of Management, University of Arizona in 2019. His research interests are in health analytics, machine learning interpretability, and statistical machine learning.

Michael T. Lash is an assistant professor in the Business Analytics Area at the University of Kansas School of Business. He received his PhD in Computer Science from the University of Iowa in 2018. His research interests are broadly in the areas of data mining, machine learning, and business analytics, focusing particularly on decision-making in these areas. His work has appeared in a variety of peer-reviewed journals including the Journal of Management Information Systems (JMIS), Expert Systems with Applications (ESWA), and the International Journal of Data Mining and Bioinformatics (IJDMB), among others, as well as rigorously peer-reviewed conferences including the SIAM International Conference on Data Mining (SDM), the IEEE International Conference on Health Informatics (ICHI), and the IEEE International Conference on Bioinformatics and Biomedicine (BIBM).
