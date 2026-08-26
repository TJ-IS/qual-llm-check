---
otero_id: 4640
otero_key: "JUXZ52Y6"
title: "How mood affects the stock market: Empirical evidence from microblogs"
authors: "Yuan Sun; Xuan Liu; Guangyue Chen; Yunhong Hao; Zuopeng (Justin) Zhang"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103181"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# How mood a<sup>f</sup>ects the stock market: Empirical evidence from microblogs

Yuan Sun<sup>a,b</sup>, Xuan Liu<sup>a,⁎</sup>, Guangyue Chen<sup>c</sup>, Yunhong Hao<sup>a</sup>, Zuopeng (Justin) Zhang

<sup>a</sup> School of Business Administration, Zhejiang Gongshang University, No.18, Xuezheng St., Zhejiang Gongshang University, Xiasha University Town, Hangzhou, Zhejiang People’s Republic of China

<sup>b</sup> Zheshang Research Institute of Zhejiang Gongshang University, 149 JiaoGong road, Hangzhou, Zhejiang, People’s Republic of China

<sup>c</sup> School of Management, Fudan University, No. 220 Handan Road, Yangpu District, Shanghai, People’s Republic of China

<sup>d</sup> Coggin College of Business, University of North Florida, Jacksonville, FL, 32224, USA

## A R T I C L E I N F O

Keywords: Text mining Microblog Sentiment analysis Stock return

## A B S T R A C T

Examining 22,504 tweets extracted from Sina Weibo, a microblog site, we identify two clusters of microblog users and study how they in<sup>fl</sup>uence the stock market. Our research contributes the following signi<sup>fi</sup>cant <sup>fi</sup>ndings to the existing literature. First, we discover that there exists an inverse U-shaped curve between stock return and the attention of both news media and investors. Second, we verify that news media attention plays a positive moderating e<sup>f</sup>ect in the relationship between investor attention and the stock return. Finally, we <sup>fi</sup>nd that social interaction could positively moderate the e<sup>f</sup>ect of news media’s and investor’s sentiments on stock return.

## 1. Introduction

A capital market is e<sup>fi</sup>cient when stock prices fully re<sup>fl</sup>ect all available information circulated in the market. In <sup>fi</sup>nancial markets characterized by imperfect information, social media can be used as a major instrument to disseminate information to the public. Currently, many companies are taking advantage of social media to improve information transparency and build up their brand image [1]. As one of the major forms of social media in China, microblogs have been increasingly used by people to express and exchange their opinions and feelings. Microblog data can be a useful and timely source for users and organizations to extract valuable information about sentiment and opinions on various topics [2]. For instance, a microblog article entitled “Wanda Real Estate Debt Was Miserably Battered Today” posted at 10:10 a.m. on June 22, 2017, was quickly spread on the Internet. At 10:18 a.m., the microblog account “Mr. Visiting Shan” maliciously added the words political risk to the title of the article. At 10:30 a.m., Wanda’s stock price began to plummet. This example poses some in teresting questions. For instance, will the information disseminated on social media always a<sup>f</sup>ect the emotional and psychological responses of social media users, thereby a<sup>f</sup>ecting their <sup>fi</sup>nancial decisions? To answer such question, sentiment analysis can be an e<sup>f</sup>ective approach to investigating microblog feeds to derive insights and provide new perspectives. A similar approach has been applied in a recent study on the Chinese <sup>fi</sup>nancial market [3].

Recent years have witnessed an increasing number of studies on social media that employ methodologies such as opinion mining to extract and process unstructured data from social media [4–7]. Scholars have begun to explore the relationship between social media and the stock market [8]. focusing on two main issues: effects of attention and sharing of moods.

Studies concentrating on the e<sup>f</sup>ects of attention assume that people usually have limited information-processing capacity and, consequently, make decisions under time pressure [9]. According to the attention theory, the speed of information di<sup>f</sup>usion is associated with the level of attention. Rapid information di<sup>f</sup>usion allows people to receive relevant information immediately and take instantaneous trading ac tions [10]. Within this framework, recent studies have shifted their focuses on media attention [11,12] and investor attention [13,10]. With regard to media attention, the news media plays a vital role in the process of determining which issues will receive low or high levels of public attention. Investor attention could also a<sup>f</sup>ect stock market return [14–16].

Social media is used by people not only to share their opinions but also to convey their moods. From a behavioral <sup>fi</sup>nance perspective, researchers have shown that the stock market can be driven by the emotions of market participants. Moreover, some sentiment measures, such as investor and consumer surveys, have been proposed to forecast share returns [17–20].

Although prior studies have recognized the impact of social media on the stock market and explored their relationships from some perspectives, they are still subject to the following limitations. First, in most studies, each microblog message is weighed equally. However, certain microblog users (e.g., government news, news media, and <sup>fi</sup>- nancial analysts) may have more in<sup>fl</sup>uence on the stock market than regular microblog users [8]. Second, although prior research has em phasized the in<sup>fl</sup>uence of investor attention [14,15] as well as media attention [21–23] on stock returns, very few studies have conceptually and empirically studied the joint role of these two types of attention and their combined e<sup>f</sup>ect on stock returns. Third, prior research mostly assumes the neutrality of news media. However, in reality, news media cannot be absolutely objective because it is inevitable for journalists of the news media to attach subjective opinions to their reports [22]. Our paper attempts to <sup>fi</sup>ll the research gap by addressing these limitations.

Speci<sup>fi</sup>cally, we explore the relationship between microblog mood and the stock market. First, we classify all the microblog accounts into several clusters and select the following two as our research object: individual investors and the news media. Second, we develop an em pirical model and formulate corresponding hypotheses to investigate the moderating e<sup>f</sup>ects of the two types of attention. Examining the model and hypotheses, we investigate how news media coverage in-<sup>fl</sup>uences investors’ attention, a<sup>f</sup>ecting their trade decisions. Third, in our sentiment analysis, we incorporate the in<sup>fl</sup>uence of sentiment from news media reports on the stock market. Finally, we study how emo tional contagion contributes to the interactions among microblog users, ultimately in<sup>fl</sup>uencing the stock market. People tend to transfer their emotion as a result of facial, vocal, and postural feedback; such phenomenon is recognized as emotional contagion in social science [24], which enables people to experience the same emotion without being aware of the transfer [42]. Social media such as Twitter and Weibo typically supports the following three types of user interactions: repost, praise, and comment [25], with which mood levels can be easily in-<sup>fl</sup>uenced by other people. Focusing on this feature, we study how the interactions among microblog users facilitated by emotional contagion strengthen the e<sup>f</sup>ects of sentiment of investors and news media on the stock market.

Our research makes the following three major contributions to the existing literature. First, our paper is the <sup>fi</sup>rst to validate how di<sup>f</sup>erent types of microblogging users a<sup>f</sup>ect the stock market based on the classi<sup>fi</sup>cation of their various identities from the perspective of the stakeholder theory. Second, our study examines the role of social media in the Chinese <sup>fi</sup>nancial market using the two dimensions of attention and sentiment. Third, our paper contributes to the emotional contagion literature by exploring the interactions among microblog users, char acterized by the unique features of microblogs.

The rest of this paper is organized as follows. The next section provides the theoretical background of the study. Section 3 proposes the research hypotheses. Section 4 introduces the methodology, including model speci<sup>fi</sup>cation and data collection, processing, and measurement. Section 5 presents our empirical results. Section 6 summarizes our <sup>fi</sup>ndings and implications and highlights the directions for future research.

## 2. Literature Review

## 2.1. Attention and the stock market

The E<sup>fi</sup>cient Market Hypothesis assumes that investors are rational and the market is e<sup>f</sup>ective, which implies that share prices re<sup>fl</sup>ect all information [26]. This assumption requires that investors allocate enough attention to their assets. However, investors have limited atten tion, as it is a scarce resource [27]. Therefore, people make most of their decisions under time pressure, which will result in biased invest ment decisions [9].

Attention measurement is a di<sup>fi</sup>cult task. The traditional proxy variables of investor attention usually include price limit [28], trading volume [29], advertise expenditure [30,31], and media reports [32]. However, stock return can be in<sup>fl</sup>uenced by other factors that are not directly related to investor attention. For instance, a news article in the Wall Street Journal does not guarantee that investors will pay attention to it unless they actually read it [33]. Da, Engelberg and Gao [33] proposed a new direct measure of investor attention using aggregate search frequency in Google. They consider the search behavior as a revealed attention measure, for instance, if you search for a stock in Google, you are undoubtedly paying attention to it. However, we consider that users who search for stocks are not necessarily investors because there may exist many other types of users. For example, some people may just search for a stock to <sup>fi</sup>nish a report or <sup>fi</sup>nd a <sup>fi</sup>gure, so they may not pay attention to the stock like investors. Therefore, using the search frequency as a measure of attention is not rigorous enough.

In this paper, we propose a di<sup>f</sup>erent measurement to overcome the limitation. Speci<sup>fi</sup>cally, we classify the potential investor groups from a large number of Weibo users. We believe that the comments or investment strategies about particular stocks published by investors on Weibo indicate that they have paid attention to the stocks. On the basis of this rationale, we measure an investor’s attention by the number of microblogs that he(she) has posted. Similarly, we use the number of reports on a stock published by the news media as a measure of media attention.

## 2.2. Emotion and financial market

The foundation of traditional <sup>fi</sup>nance is associated with the modern portfolio theory [34] and the E<sup>fi</sup>cient Market Hypothesis [35]. The E<sup>fi</sup>cient Market Hypothesis argues that the price of any asset must immediately incorporate all available information and can be regarded as an optimal estimate of true investment value at all times [36]. Behavioral finance is the psychological study of market participants and their interactions with the <sup>fi</sup>nancial markets, where market participants may be either individual households or organizations [37–39].

According to the behavioral <sup>fi</sup>nance theory, researchers have shown that the emotions of market participants will have a strong in<sup>fl</sup>uence on the stock market. The role that investor sentiment plays in asset pricing has shown its great importance in <sup>fi</sup>nancial economics. Various investor sentiment proxies have been proposed to investigate the contemporaneous correlations between investor sentiment and marketwide variables [40]. In numerous recent studies, mood levels have been used as a proxy for investor sentiment [41–43,40]. According to these <sup>fi</sup>ndings, mood states can spread among Internet users through textbased communication. In our study, we develop a sentiment index to capture the sentiment of investors and news media. Our goal is to categorize a tweet into a three-dimensional daily time series of mood levels, namely, positive, neutral, or negative. Based on Antweiler and Frank [44], we establish a daily mood index for both investors and news media.

## 2.3. Emotional contagion and social interaction

Emotional contagion has been de<sup>fi</sup>ned as the phenomenon that “when people are in a certain mood, whether elation or depression, that mood is often communicated to others. When we are talking to someone who is depressed it may make us feel depressed, whereas if we talk to someone who is feeling self-con<sup>fi</sup>dent and buoyant we are likely to feel good about ourselves” [45]. Emotional states can be transferred to others through emotional contagion, leading people to experience the same emotion without being aware of the transfer [42]. As a result of emotional contagion, selection and in<sup>fl</sup>uence processes are proposed to explain the following phenomenon [46]: people befriend others who are similar to them [47] or they become more similar to their friends over time. Therefore, to some extent, emotional contagion can enhance social interaction.

Social interaction refers to as the interdependence of individuals, under which the preferences, beliefs, and budget constraints of a person engaging in both social and economic behavior are directly in<sup>fl</sup>uenced by the characteristics and choices of other people [48]. Xia, Lei, Jiliang and Huan [2] showed that social interaction can help sentiment analysis by proposing a sociological approach to handle noisy and short texts for sentiment classi<sup>fi</sup>cation. Kramer, Guillory and Hancock [42] conducted an experiment with people who used Facebook, and the results showed that emotion expressed by others on Facebook a<sup>f</sup>ected our own mood, producing experimental evidence for massive-scale contagion through social interaction. Manski [49] divided social interaction into endogenous interaction and situational interaction. Hong, Kubik and Stein [50] studied how individuals obtained information through social interaction to in<sup>fl</sup>uence individual ownership behavio decisions.

Di<sup>f</sup>erent from traditional media texts, microblog texts are noisy, short, and embedded with social relations [2]. Sina Weibo provides three types of user interactions (repost, praise, and comment) that allow users to form threaded conversations around a single message [25]. Thus, microblog users’ mood levels can be easily in<sup>fl</sup>uenced by other people. In this paper, we consider the social interactions of Weibo users when exploring the relationship between mood levels and stock returns.

## 3. Hypotheses

## 3.1. Relationship between attention and stock return

An increasing amount of research has focused on the media’s e<sup>f</sup>ect on the stock market because the news media provides constant information to the public. The media e<sup>f</sup>ect is referred to as a phenomenon that stocks with no or low mass media coverage earn higher re turns than those with high coverage, even after controlling for well known risk factors [11]. Given the influence of the news media. the empirical conclusion in most of the literature is that media coverage of listed companies will promote either people’s preference for stock investment or increased stock prices. For instance, Chen, Goldstein and Jiang [51] showed that media attention on the capital market was mainly re<sup>fl</sup>ected in stock prices.

Investor attention is the premise and objective condition of market reaction. However, limitations of time and professional skills make investor attention a scarce resource [52]. Dellavigna and Pollet [14] compared investors’ response to earnings announcements on Friday when their inattention was more likely, with the response on other weekdays. Their results supported the existence of post-earnings announcement drift based on an under-reaction to information caused by limited attention. Aouadi, Arouri and Teulon [53] found that Google search volume was a reliable proxy for investor attention. Interestingly, they showed that investor attention was strongly correlated to trading volume and was a signi<sup>fi</sup>cant determinant of stock market illiquidity and volatility. Thus, social media works as an attention-allocation mechanism in the modern world, in which social media can attract the maximum attention from investors.

Current research shows that stocks with media coverage or investor attention will lead to attention-driven buying [54] and overtrading. “Attention-driven buying behavior” means that the attention of market participants is easily a<sup>f</sup>ected by the media, thus forming “excessive attention” [55], so market participants will buy more attention-grabbing stocks. This excessive attention will cause an overreaction to new information and an overestimation of stock value in the short term [56], and a long-term reversal of subsequent earnings, which is called “over-attention underperformance” [57]. This paper attempts to examine whether the impact of attention on stock market returns gra dually disappears after concentration increases to a certain degree, which is consistent with the “over-attention underperformance hypothesis.” Therefore, the following hypotheses are established:

H1a. There is an inverse U-shaped curve between news media attention

and stock returns.

H1b. There is an inverse U-shaped curve between investor attention and stock returns.

As mentioned above, increased media attention has a direct in<sup>fl</sup>u ence on stock returns because the dissemination of news media in formation will reduce information asymmetry among the public [58]. At the same time, the direct impact of investor attention on stock returns is a result of “over-attention underperformance” [57]. Firms frequently publish mandatory news announcements, and the business press reports <sup>fi</sup>rm-speci<sup>fi</sup>c news and events through the news media [59]. When a <sup>fi</sup>rm is recognized by investors from a mass media report, the reactions of di<sup>f</sup>erent types of investors to that media coverage will be re<sup>fl</sup>ected in both trading decisions and stock prices [60]. However, much more attention should be paid to whether and how attention mechanisms moderate with each other in response to the stock market. There is likely to be a mechanism in which media coverage changes investors’ trade decisions by a<sup>f</sup>ecting their attention. Zhang, Wan and Fu [22] used a security market experiment to measure investor attention and found that the amount of media coverage was positively related to investor attention, con<sup>fi</sup>rming that media reports in<sup>fl</sup>uenced investor behavior as an attention allocation mechanism. Thus, we de velop another hypothesis as follows：

H1c. News media attention plays a positive moderating role in the relationship between investor attention and the stock return.

## 3.2. Relationship between sentiment and stock return

An emotion is a kind of feeling directing one toward anything intuitively appraised as good or away from anything intuitively appraised as bad. Elster [61] de<sup>fi</sup>ned emotion as a physiological state of arousal triggered by a belief. A large body of literature shows that a person’s emotional state may in<sup>fl</sup>uence his(her) <sup>fi</sup>nancial decision making [62]. Lo and Repin [63] studied the physiological characteristics of profes sional stock traders and found that emotion can a<sup>f</sup>ect a trader’s ability to survive in the <sup>fi</sup>nancial market. If an individual is in a good mood because of recent life experience, it will help him/her take a positive outlook to the task at his/her hand. The evidence also indicated that good moods resulting from morning sunshine led to higher stock returns [64].

Tetlock [65] used daily content from the Wall Street Journal and found that high media pessimism predicted downward pressure on market prices followed by a reversion to fundamentals, and unusually high or low pessimism predicted high market trading volume. Wu and Lin [59] conducted a textual analysis of news content and found that positive news generated positive abnormal returns and negative news caused negative abnormal returns. Walker [66] found that there was a signi<sup>fi</sup>cant relationship between the total number of housing market articles published in the Financial Times and the return premium of companies involved in the housing market. Thus, it is reasonable to assume that public sentiment can a<sup>f</sup>ect stock market values.

Di<sup>f</sup>erent sentiment measures have been proposed to forecast share returns, such as investor and consumer surveys [17–19], trading volume, or market volatility [67]. In this study, we use mood levels as a proxy for investor sentiment [68,43,69]. Categorizing the emotional color of a tweet into a three-dimensional daily time series of mood levels, including positive, neutral, or negative, we develop a daily mood index for both investors and the news media based on Antweiler and Frank [44] The formula for the daily mood index is given in Section 4.1. Hence, we establish the following two hypotheses:

H2a. An increased daily mood index in the news media will have a positive e<sup>f</sup>ect on stock returns.

H2b. An increased daily mood index among investors will have a positive e<sup>f</sup>ect on stock returns.

Table 1

## 3.3. Moderating role of social interaction

Emotional states can be transferred to other people through emotional contagion, resulting in they experiencing the same emotion without knowing the transfer [42]. Studies have found evidence for social interaction based on emotional contagion. For instance, Neumann and Strack [70] showed that mood contagion can be conceived of as a mechanism with which feelings are transferred between persons who listen to each other. Emotional contagion can enhance social in teraction. However, social interaction has also been considered as a critical factor of social media information and a potentially important tool for mobilizing people. Wang, Wang, Li, Zheng and Zhao [71] found that users of the Sina microblog could comment on or reply to any publicly released tweet. Even if users did not pay attention to the publisher, user interaction behavior would not be a<sup>f</sup>ected, and a stronger social connection would still be established.

In China, Sina Weibo provides users with the platforms to interact with friends and followers. There are three types of user interactions in Sina Weibo: repost, praise, and comment [22]. A user can post a new tweet, mention another user in a tweet, or comment on an existing tweet. A Sina Weibo user can comment on or reply freely to any published microblog, which means that Weibo supports a speci<sup>fi</sup>c kind of social interaction [25]. Wang, Chen, Wang, Wang, Yang, Li, Zheng and Zhao [25] found that users who made comments on a tweet were often friends with the original tweeter, and they usually built a strong social link.

In this paper, we also focus on the social interactions of Weibo users when exploring the relationship between mood levels and stock returns. In particular, we extend previous research of Nofer and Hinz [43] by including the total number of reposts, comments, and praises per tweet in the analysis. Therefore, the following hypotheses are proposed:

H3a. Social interaction plays a positive moderating role in the relationship between the news media mood index and the stock return.

H3b. Social interaction plays a positive moderating role in the relationship between the investor mood index and the stock return.

## 4. Methodology and data

This section introduces our research model and methods for data collection, processing, and measurement. Beginning with a summary of our attention and mood measurement, we develop di<sup>f</sup>erent empirical models to determine whether microblog attention or mood will a<sup>f</sup>ect stock returns. Additionally, we demonstrate our data-gathering process by explaining how we collect historical capital data and why microblogs are chosen over other Chinese social media. Using di<sup>f</sup>erent combinations of data as the input, we show how the methods of identity classi<sup>fi</sup>cation and sentiment analysis were employed to extract public mood states from microblog feeds.

## 4.1. Measurement

Prior research has proposed di<sup>f</sup>erent theories of attention, but it remains di<sup>fi</sup>cult to directly measure attention. Di<sup>f</sup>erent kinds of indirect proxies have been used in recent studies to measure investor attention, such as advertising expense [72–74], media coverage [55,11], extreme returns [32], trading volume [32], and the Baidu Index [21,75]. In this paper, we develop a new measurement of at tention based on the rationale that the comments or investment stra tegies about particular stocks published by investors on Weibo indicate that they have paid attention to the stocks. Based on this reasoning, we measure an investor’s attention by the number of microblogs that he (she) has posted. Similarly, we use the number of reports on a stock published by the news media to measure media attention.

Recent studies have analyzed the e<sup>f</sup>ect of microblog participants sentiment on stock returns. However, they have not investigated the di<sup>f</sup>erence between positive and negative sentiment, which play totally di<sup>f</sup>erent roles with regard to their in<sup>fl</sup>uences on human behavior [76]. Based on the study of Antweiler and Frank [44] we develop a daily mood index for both investors and the news media. Speci<sup>fi</sup>cally, we denote M <sup>positive</sup> as the number of tweets related to “positive” mood and M <sup>negative</sup> <sub>t</sub> as that related to “negative” mood. Therefore, the DMI (daily mood index) is calculated as follows:

$$
D M I = L n \big [ (1 + M _ {t} ^ {p o s i t i v e}) / (1 + M _ {\mathrm{t}} ^ {n e g a t i v e}) \big ].\tag{5}
$$

A positive value of the DMI indicates that an overall positive signal is delivered on that day. Moreover, the larger the value, the more positive the sentiment is delivered by the tweets. In contrast, a negative value of the DMI implies that an overall negative signal is delivered on that day.

The intraday stock return is calculated using the following formula:

$$
R E T U R N _ {\mathrm{it}} = L n (P R I C E _ {i t}) - L n (P R I C E _ {i, t - 1})\tag{6}
$$

where $P R I C E _ { i t }$ is the closing price of a stock i on a given day t and $P R I C E _ { i t - 1 }$ is the closing price on the given day before ( 1t − ). In addition, we add the number of forwarding, comments, and likes for each tweet on each day and then multiply it by the daily mood index. The result is de<sup>fi</sup>ned as social interaction [77].

Finally, we control for numerous variables. First, we consider the stock market factors, such as trade volume and currency value; after taking the logarithm, we use the data obtained from the CSMAR (China Stock Market and Accounting Research) database. Second, by considering company features, we control for leverage, earnings per share, the book-to-market value ratio, and Tobin’s Q [21]. Table 1 summarizes the descriptions of our variables.

## 4.2. Model specification

The purpose of our study is to investigate the relationship between stock return and investor attention. We use the number of tweets published by investors and news media as a proxy for attention. Thus, we develop the following equations to test hypotheses H1a, H1b, and H1c:

$$
R E T U R N _ {i t} = \alpha_ {i} + \beta_ {1} A T T E N T I O N
$$

$$
+ \beta_ {2} A T T E N T I O N ^ {2} + \beta_ {3} C U R R E N C Y V A L + \beta_ {4} T R A V O L
$$

$$
+ \beta_ {5} B O O K T M A R K E T + \beta_ {6} R E T U R N T O T A + \beta_ {7} L E V E R A G E
$$

$$
+ \beta_ {8} R E T U R N T O N A + \beta_ {9} T O B I N Q + \beta_ {1 0} E A R N I N G S + \varepsilon_ {i t},\tag{1}
$$

Variables de<sup>fi</sup>nition.

<table><tr><td>Variables</td><td>Definition</td></tr><tr><td colspan="2">Controls</td></tr><tr><td>TRAVOL</td><td>The daily trade volume per stock</td></tr><tr><td>CURRENCYVAL</td><td>The daily stock currency value per stock</td></tr><tr><td>BOOKTMARKET</td><td>Book to market ratio monthly per stock</td></tr><tr><td>RETURNOTA</td><td>Return on total assets monthly per stock</td></tr><tr><td>LEVERAGE</td><td>Total liabilities to total assets monthly per stock</td></tr><tr><td>RETURNONA</td><td>Return on net assets monthly per stock</td></tr><tr><td>EARNINGS</td><td>Earnings per share monthly per stock</td></tr><tr><td>TOBINQ</td><td>The ratio between a physical asset&#x27;s market value and its replacement value monthly per stock</td></tr><tr><td colspan="2">Study Variables</td></tr><tr><td>RETURN</td><td>The daily return per stock</td></tr><tr><td>ATTENTION</td><td>The number of tweets released by each investor or media each day</td></tr><tr><td>DMI</td><td>The sentiment delivered by per tweet, see above formula</td></tr><tr><td>INTERACTION</td><td>The sum of forwarding, likes, and comments per tweet</td></tr></table>

$$
\begin{array}{r l} R E T U R N _ {i t} = \alpha_ {i} + \beta_ {1} A T T E N T I O N + \beta_ {2} N E W S M E D I A \times I N V E S T O R \\ & + \beta_ {3} C U R R E N C Y V A L + \beta_ {4} T R A V O L + \beta_ {5} B O O K T M A R K E T \\ & + \beta_ {6} R E T U R N T O T A + \beta_ {7} L E V E R A G E + \beta_ {8} R E T U R N T O N A \\ & + \beta_ {9} T O B I N Q + \beta_ {1 0} E A R N I N G S + \varepsilon_ {i t} \end{array} \tag {2}
$$

Di<sup>f</sup>erent sentiment measures have been proposed to forecast share returns, such as investor and consumer surveys [17,18,7], trading vo lume, and market volatility [67]. Using mood levels as a proxy for investor sentiment, we study the relationship between sentiment and stock return with the following regression model to verify hypotheses H2a and H2b:

$$
\begin{array}{r l} R E T U R N _ {i t} & = \alpha_ {i} + \beta_ {1} D M I + \beta_ {2} C U R R E N C Y V A L + \beta_ {3} T R A V O L \\ & \quad + \beta_ {4} B O O K T M A R K E T + \beta_ {5} R E T U R N T O T A L A \\ & \quad + \beta_ {6} L E V E R A G E + \beta_ {7} R E T U R N T O T A L A + \beta_ {8} T O B I N Q \\ & \quad + \beta_ {9} E A R N I N G S + \varepsilon_ {i t} \end{array}\tag{3}
$$

As we have explained in Section 3, interactions with others have a strong in<sup>fl</sup>uence on people, leading to a shared emotion or social mood. Collectively shared opinions and beliefs shape individuals’ decision and aggregate them into social trends, fashion, and actions [78]. Sina Weibo provides users with platforms to interact with friends and followers, so users’ mood levels can be easily in<sup>fl</sup>uenced by other people. Therefore, we further our research by considering the moderating e<sup>f</sup>ect of social interaction. In particular, we calculate social interaction by totaling the number of forwards, comments, and likes for each tweet on a daily basis and then multiplying it with the daily mood index. Taking social interaction as a moderating variable, we establish the following model to verify hypotheses H3a and H3b:

$$
\begin{array}{r l} R E T U R N _ {i} & = \alpha_ {i} + \beta_ {1} D M I + \beta_ {2} D M I \times I N T E R A C T I O N \\ & + \beta_ {3} C U R R E N C Y V A L + \beta_ {4} T R A V O L + \beta_ {5} B O O K T M A R K E T \\ & + \beta_ {6} R E T U R N T O T A + \beta_ {7} L E V E R A + \beta_ {8} R E T U R N T O N A \\ & + \beta_ {9} T O B I N Q + \beta_ {1 0} E A R N I N G S + \varepsilon_ {i t} \end{array} \tag {4}
$$

## 4.3. Sample and data

Since Twitter was blocked in China in 2009, several Chinese media companies launching similar services have rapidly gained popularity. Sina Weibo, launched on August 14, 2009, is the largest microblog platform in China with more than 100 million messages posted each day. By the third quarter of 2015, Sina Weibo had 222 million sub scribers and 100 million daily users. Sina Weibo enables users to post short tweets or messages that are displayed on a user’s Weibo page. As each character in Chinese represents a whole word, the content of Chinese tweets is richer than what can be communicated through 140 characters in English. In addition to posting short messages and sharing pictures, Weibo users can upload videos, play games, and communicate through private instant messaging [79].

Sina Weibo provides a platform for us to investigate the relationship between user groups with di<sup>f</sup>erent identities based on users’ attention, mood levels, and social interaction from a stakeholder’s perspective. Moreover, with Sina Weibo’s advanced search capability, we can customize our data by searching for a more speci<sup>fi</sup>c expression in combination with topic keywords, date, types of document, and source of document. For instance, we can input our keywords (the real estate company’s short name) and de<sup>fi</sup>ne the time span. In a few seconds, the web will display all the required data.

## 4.3.1. Data collection

In many parts of the developed world, the real estate industry has become a symbol of wealth creation that can foster the local economy. Real estate companies are important sectors of the economy that invest large amounts of capital and signi<sup>fi</sup>cant proportions of the workforce. Realtors hold the view that information about properties belongs only to their <sup>fi</sup>rm or its network [80]. However, this poses a problem owing to the lack of information transparency. Social media has played a dominant role in the information society. In China, there are many social media platforms for people to express their opinions, such as Sina Weibo, Wechat, Renren (which is more like Facebook), Stock BBS, and so on. Microblogs have advantages over other social media platforms. First, they attract attention from both adults and young people. Second, many <sup>fi</sup>nancial reviewers, well-known economists, and stock market commentators have microblog accounts [81]. Therefore, we collected data in the following ways.

<sup>Web data.</sup> To extract data from Weibo, we designed and customized the method of website crawling based on an existing data crawling approach. In this study, we used “Octopus Collector”<sup>1</sup> software to capture massive Weibo data. A microblog contains 7 parts: “microblog\_content,” “microblog\_author,” “author\_id,” “microblog\_time,” “comment\_count,” “repost\_count,” and “praise\_count,” all of which are needed for our research. The experiments veri<sup>fi</sup>ed the e<sup>fi</sup>ciency of our web crawling method and the accuracy of our page classi<sup>fi</sup>cations. Overall, we extracted 22,504 tweets from Sina Weibo from Octobe 2015 to December 2015.

<sup>Stock data.</sup> For these <sup>fi</sup>rms, we obtained <sup>fi</sup>nancial data from the CSMAR database for the period from October 2015 to December 2015, which allowed us to empirically investigate market behavior for those three months. We deleted stocks with invalid samples that do not truly represent the name of the business, stocks about which fewer than 5 people tweeted during the three months, and stocks for which no company-related tweets were published by either investors or the news media.

In our time span, there was some missing data because of the stock market closing on a national holiday or other speci<sup>fi</sup>c reasons. Thus, we applied imputation methods for missing value. If the missing data were for one day, then we used the following formula [82]:

$$
X = 1 / 2 (x _ {t} - x _ {t - 1}),\tag{7}
$$

where x represents all valid variables and t represents time series.

If the data was missing for several consecutive days, then the above formula was unsuitable. Based on Zhou, Zhang, Li and Yang [82] the following method was applied to make up the balance between the <sup>fi</sup>xed time interval of the time series data and the panel data:

$$
X = R a n d o m ^ {*} (x _ {a} - x _ {b}) + x _ {b}\tag{8}
$$

We used the random method to return a random number between 0 and 1, where $x _ { b }$ is the last value and $x _ { a }$ is the <sup>fi</sup>rst value between the time intervals. If there was missing data for three months, we directly removed the sample stock.

## 4.3.2. Identity classification

A microblog account can be considered either subjective or objective. Subjective microblog accounts normally belong to individual users with di<sup>f</sup>erent backgrounds, jobs, and genders, whereas objective microblog accounts mainly include the news microblog media, such as “Sina Finance,” “Sina sports,” “Beijing News,” and so on [81]. Our research weighs microblog opinions based on users’ in<sup>fl</sup>uence on stock returns. In particular, we focus on two groups of users (individual investors and news media) from seven categories because these two groups account for the largest proportion of our original sample and the users from these two groups have a great impact on stock price. We <sup>fi</sup>nd that “individual investors” tend to pay close attention to the stock market with respect to the following features, such as stock price movement, stock recommendation, and earning announcement. “News media” was easy to be categorized based on their Weibo titles, for in stance, “Sina Real Estate,” “Live News,” “24 h News,” and “Guiyang Leju.” At the beginning, we applied an exploration-based method to collect users’ data from Weibo. The heuristic rule evaluated if a user had published messages with keywords containing a company’s abbreviation such as “Wanke,” “Greenland Group,” and “Poly Real Estate.” After obtaining the tweets, we performed propagation to obtain more users’ data. Two research assistants then helped to determine whether the collected users could fall into one of the two groups. If there were inconsistent results about classi<sup>fi</sup>cation, the assistants would discuss the results to reach a <sup>fi</sup>nal conclusion. Overall, we collected 8099 tweets for “individual investors” and 2313 tweets for “news media.”

## 4.3.3. Sentiment analysis

With the collected users’ tweets, we conducted a sentiment analysis for the two types of users. Substantial research exists in the <sup>fi</sup>eld of emotion analysis, among which many systems have been implemented to automatically detect sentiment in texts [83,84]. The major solutions to emotion analysis include the emotional knowledge-based method and the feature-based classi<sup>fi</sup>cation method. The emotional knowledge based method aims to create the emotion dictionary or <sup>fi</sup>eld emotion lexicon and then determine the polarity of text using a combination of emotional words [85,83,86]. The method based on feature classi<sup>fi</sup>cation primarily uses machine learning to conduct feature extraction and make judgments [83].

In this paper, we used the API (Application Programming Interface) provided by the Chinese Tencent NLP platform<sup>2</sup> to conduct microblog content text processing and sentiment analysis. Our goal was to classify a tweet as being either “positive,” “negative,” or “neutral” by applying the sentiment classi<sup>fi</sup>cation to all the Weibo messages in the two clus ters. Detailed principles of emotion analysis are divided into the following three parts.

4.3.3.1. Construction of corpus. To date, Tencent NLP has been collecting texts from more than 20 sites, including e-commerce, news, <sup>fi</sup>lm, music, APP, and other categories, with a cumulative number of 400 million tagged materials and approximately 2,000,000 new annotations per day.

4.3.3.2. Polar words mining. Tencent NLP will dig out certain words or phrases from the document that can represent positive and negative polarities. The construction of the polar vocabulary database can be divided into the following two steps.

1) Text preprocessing. As there is too much noise in the text pre processing corpus, we must preprocess the text before mining polar words. This preprocessing includes the participle, denoising, best matching, and other related technologies. The participle uses the par ticiple system of the Tencent TE199. Denoising must remove unrelated information in the document, such as “@jjhuang,” HTML labels, along with words that do not have a classi<sup>fi</sup>cation meaning, for instance, pronouns such as “the”, “ah”, “I”, and so on.

2) Selection of polar words. After text preprocessing, Tencent Wen

Chi uses the TF-IDF method to select certain words as polar words for training models. Tencent NLP has excavated more than 0.12 million polarity words, and through arti<sup>fi</sup>cial veri<sup>fi</sup>cation of more than 0.8 million of those words, approximately 100 polar words are excavated from the corpus each day.

4.3.3.3. Polar words judgment. The task of polarity judgment is to determine the positive, negative, or neutral polarity of the corpus, which is a complex three-classi<sup>fi</sup>cation problem. To simplify the problem, Tencent NLP <sup>fi</sup>rst makes a subjective-or-objective judgment on the corpus; the objective corpus is a neutral one, and the subjective corpus is then either positive or negative. For the purpose of classi<sup>fi</sup>er selection, Tencent NLP adopts the Support Vector Machine (SVM) model<sup>3</sup> for subjective and objective judgments. In terms of the polar judgment, both the Naive Bayesian Model<sup>4</sup> and the Support Vector Machine model are used.

## 5. Empirical analyses

Having described our sample data collection and preprocessing processes, we next shift our focus to the empirical analysis to test our hypotheses. In this section, we <sup>fi</sup>rst summarize the descriptive statistics to identify the basic features of variables, report the correlations between various variables, and then test the validity of our hypothesis based on proposed empirical models. Finally, we conduct a further robustness check to ensure the reliability of the research results.

## 5.1. Descriptive statistics

We report the descriptive statistics of key variables, including the mean, observations, and standard deviation for our <sup>fi</sup>nal sample (Appendix A, Table A1). After deleting invalid samples, we obtain 1371 observations of investors and 712 observations of news media. The mean of DMI is positive for both investors and news media, which in dicates that positive sentiment predominates. The maximum and mean of attention for investors are larger than those for news media. To avoid the multicollinearity problem among variables, we analyze the explained variables and the explanatory variables using the variance in <sup>fl</sup>ation factor (VIF) [87]. VIF quanti<sup>fi</sup>es the severity of multicollinearity in an ordinary least squares (OLS) regression analysis. It measures how much the variance (the square of the estimate's standard deviation) of an estimated regression coe<sup>fi</sup>cient will change because of collinearity. The larger the VIF value, the higher degree is the collinearity. The empirical judgment method shows that when 0 < VIF < 10, there is no multiple collinearity. Our results demonstrate that the maximum VIF is 8.52, which is less than 10, implying that our variables do not have a serious multicollinearity problem.

Moreover, we provide the correlation analysis of all variables, which is shown in Appendix A, Table A2. As shown in the table, for either investors or the news media, there is a positive correlation between attention and stock return. In addition, the correlation also be comes positive between Daily Mood Index and return.

Fig. 1 demonstrates that individual investors tend to be more sensible. In particular, they exhibit more positive sentiments than negative moods. This <sup>fi</sup>nding is compatible with those reported in previous studies that extract sentiment from Internet messages. For instance, Rao and Srivastava [88] studied stock and commodity discussions on Twitter and found that 67.14% of tweets were positive. The phenom enon in which positive words are used more often than negative words is known as the “Pollyanna e<sup>f</sup>ect” in the literature [89].

(a) Investors  
![](/api/attachments/JUXZ52Y6/fulltext/images/acbea692371cadd72307b85acfda8f5c073e634d2a430e69e78ba6ca45d3a407.jpg)  
Fig. 1. Distribution of mood levels.

In contrast, the news media is always neutral. Objectivity and au thenticity are the basic characteristics of the media because it is widely open for public communication. News media should be consistent with the objective facts to the greatest extent possible when releasing tweets so that the subjective sense of those tweets can be eliminated. There are typically two sides to every story; if news reports show only one side of views, media reports will be biased and may mislead the audience, hence damaging the authenticity of the media. However, it is impossible for the news media to be completely objective because journalists will inevitably introduce subjective factors. Although the positive and negative emotions of the news media may be relatively insigni<sup>fi</sup>cant, they can still a<sup>f</sup>ect the stock market; therefore, it is ne cessary to consider the mood of the news media.

## 5.2. Empirical results

We use OLS to examine our empirical models of H1, H2, and H3 and show the results in the following subsections.

## 5.2.1. Relationship between attention and the stock return

Examining linear relationships, we <sup>fi</sup>nd a positive relationship between attention and the stock return for both investors and the news media (see Table B1). However, the relationship between stock returns and attention could be nonlinear. To better address this nonlinear ef fect, we add attention-squared to investigate whether this kind of relationship is re<sup>fl</sup>ected in the U-shaped curve.

Table B1 in Appendix B shows that the coe<sup>fi</sup>cient of the attention square $( \beta = - 0 . 2 1 , \rho < 0 . 0 5 )$ is negative and investor attention-squared has a signi<sup>fi</sup>cant impact on stock return. Our result indicates that there is an inverse U-shaped curve between attention and stock return. Furthermore, this shows that the impact of news media attention on stock returns gradually disappears, after that attention increases to a certain degree. This implies that stocks with no or low social media coverage earn higher returns than those with high coverage even after well-known risk factors are controlled for [11]. There is also evidence from Zhang, Wan and Fu [90] who took all IPO <sup>fi</sup>rms as their research sample and found that short-term media reports between the <sup>fi</sup>ling date and the listing date positively correlate with IPO underpricing and <sup>fi</sup>rstday turnover. However, the long-term media reports released one year before the <sup>fi</sup>ling date signi<sup>fi</sup>cantly positively correlate with IPO underpricing, but not to the <sup>fi</sup>rst-day turnover.

With regard to investor attention, the statistical signi<sup>fi</sup>cance $( \beta =$ $- 0 . 2 6 , \mathbf { p } \ < \ 0 . 0 0 1 )$ suggests the inverted U-shaped relationship between attention and stock return, which is consistent with the over-attention underperformance hypothesis. In summary, the stock return is signi<sup>fi</sup>cantly and positively related to attention but is signi<sup>fi</sup>cantly and negatively associated with the square of attention, which supports our Hypotheses 1a and 1b.

(b) News media  
![](/api/attachments/JUXZ52Y6/fulltext/images/cf08760eaae28cc764c243048a7aaa7d08a7da7c99c0a9d8260ce6966a9fa160.jpg)

With regard to the moderating e<sup>f</sup>ect in H1c, our <sup>fi</sup>ndings indicate that interaction of the two types of attention on stock returns is positive and signi<sup>fi</sup>cant $( \beta = 0 . 1 6 , \ p < 0 . 0 5 )$ . The results indicate that media attention exerts a moderating e<sup>f</sup>ect on investor attention to in<sup>fl</sup>uence the stock return, in other words, media coverage that focuses on speci<sup>fi</sup>c stocks can magnify the e<sup>f</sup>ect of investor attention. The study further strengthens the evidence that an investor’s attention and investment behavior caused by the news media information transmission have a direct impact on stock returns. Therefore, we can accept Hypothesis 1c.

## 5.2.2. Relationship between mood and stock return

We further explore whether sentiment on Sina Weibo is related to stock return (see Table B2 in Appendix B). We <sup>fi</sup>nd that both news media’s DMI $( \beta = 0 . 1 2 , \mathrm { ~ p ~ < ~ } 0 . 0 0 1 )$ and investors’ DMI $( \beta = 0 . 0 5 ,$ $\mathsf { p } < 0 . 0 0 1 )$ have a signi<sup>fi</sup>cant positive relation to intraday stock return, indicating that positive sentiment is associated with higher stock prices. This result is consistent with evidence from psychology research, which proves that positive sentiment causes investors to trade more as they attempt to sustain a positive outcome. For instance, Siganos, Vagenas-Nanos and Verwijmeren [91] examined the relation between daily sentiment and trading behavior in 20 international markets using Facebook’s Gross National Happiness Index and found that sentiment has a positive contemporaneous relation to stock returns. Therefore, we can accept Hypotheses 2a and 2b.

## 5.2.3. Relationship between sentiment and social interaction

To investigate whether social interaction will enhance DMI e<sup>f</sup>ects on the stock return, we consider the moderating e<sup>f</sup>ect of the social interactions of Weibo users (see Table B2 in Appendix B). We <sup>fi</sup>nd that social interactions positively promote both news media $( \beta = 0 . 0 8 ,$ $\mathsf { p } < 0 . 0 0 1 )$ and investors $( \beta = 0 . 0 4 , \mathrm { ~ p ~ < ~ } 0 . 0 1 )$ on the relationship between the mood index and stock return. Our results show that the mood contagion can be considered as a mechanism with which a<sup>f</sup>ective feelings are transferred between persons who listen to each other [70]. Thus, we can accept Hypothesis 3, which indicates that social interaction plays a positive moderating role in the relationship between mood index and the stock market return.

## 5.3. Robustness check

Finally, we perform a robustness test on the research results. First, we change the explained variable by considering the abnormal return, which is calculated as follows (see Table C1 in Appendix C): $A B N O R M A L R E T U R N _ { i t } = S T O C K R E T U R N _ { i t } - M A R K E T R E T U R N _ { i t } .$

(9)

Second, we <sup>fi</sup>nd that both news media’s DMI and investors’ DMI have a signi<sup>fi</sup>cant positive relation to intraday stock return, indicating that positive sentiment is associated with higher stock prices. To eval uate this result, we examine the relationship between stock returns and the positive mood of investors and the news media.

As shown in Table C2 in Appendix C, positive sentiments have a signi<sup>fi</sup>cant impact on stock returns, which is consistent with Hypothesis 2. This could indicate that these results have been accepted by the robustness tests, proving stability and reliability. There is no substantial change in the main test and robustness test results, implying that our study’s conclusion is robust.

## 6. Discussion

## 6.1. Major findings

This paper investigates the relationship between Sina Weibo and stock returns. Microblog users play an important role in the dissemination of organization information. Among di<sup>f</sup>erent categories of users, we select investors and news media for our study. We develop our research models based on the two dimensions of attention and emotion and investigate the impact of social media on the stock market from a stakeholder perspective. Our <sup>fi</sup>ndings are set forth below.

First, we model the attention for both investor and news media and examine the nonlinear relationship between attention and stock returns. Our results con<sup>fi</sup>rm an inverse U-shaped curve between stock returns and the attention of both investors and the news media, thus supporting the over-attention underperformance hypothesis. In addition, we demonstrate the positive moderating role of the news media in strengthening the relationship between investor attention and the stock return.

Second, we <sup>fi</sup>nd that the stock market can be in<sup>fl</sup>uenced by the emotions of market participants (most of whom are investors). Our research also incorporates the sentiment of news media because media journalists will inevitably mix in their personal opinions in their reports. We show that both news media’s DMI and investors’ DMI have a signi<sup>fi</sup>cant positive relationship with intraday stock return, indicating that positive sentiment is associated with higher stock prices. Our result aligns with the <sup>fi</sup>nding from the psychology literature that shows the e<sup>f</sup>ect of positive sentiment on more trading from investors.

Finally, we extend previous research by including the interaction variable in the analysis. Considering the social interaction of Internet users, our results verify that social interaction has a positive moderating e<sup>f</sup>ect on reinforcing the relationship between mood index and the stock return. In practice, Sina Weibo provides users with the platforms to interact with their friends and followers; hence, their mood levels can be easily in<sup>fl</sup>uenced by other people.

## 6.2. Theoretical implications

This study has several theoretical implications. First, we study how users with di<sup>f</sup>erent identities in<sup>fl</sup>uence the stock return from a stakeholder perspective. Previous studies mostly focus on the impact of in vestors or news media on the stock market from a single perspective [92,11,93,94,91]. They have not considered the di<sup>f</sup>erent opinions expressed by users on the same social media platform. Microblog users play an important role in transmitting organizational information; information disseminators are not limited to investors or the press. Other groups are also important to organizations, as there exist di<sup>f</sup>erent relationships between such groups and organizations [81,8]. Therefore, the stakeholder theory provides a new perspective for our research [95].

Second, we establish and test the hypothesis to verify an inverse U shaped curve between news media attention and stock return. Prior studies show that stocks with news media coverage or investor attention will lead to attention-driven buying [54,23]. However, they only focus on the importance of either investor attention [14,15] or news media attention [21–23] for stock returns. Very little research exists on the joint e<sup>f</sup>ect of di<sup>f</sup>erent types of attention on stock returns. In addition, previous empirical results mostly indicate a linear correlation between attention and the stock return [15,16]. The “attention-driven buying behavior” means that the attention of market participants is easily a<sup>f</sup>ected by the media, resulting in “excessive attention” [55]. Such attention will cause overreaction to new information and overestimation of stock value in the short-term [56] and long-term reversals of subsequent earnings, which is called “over-attention underperformance” phenomenon [57]. Our <sup>fi</sup>nding contributes to a better understanding of such phenomenon.

Third, we <sup>fi</sup>nd that both investors’ and the news media’s Daily Mood Index have a signi<sup>fi</sup>cant positive relation to intraday stock return. Additionally, it is reasonable to consider the impact of news media on the stock return but not that of investors. Based on the behavioral <sup>fi</sup>- nance theory, researchers have shown that the stock market can be driven by the emotions of market participants [61,78]. The role that investor sentiment plays in asset pricing has shown its great importance in <sup>fi</sup>nancial economics [65,96,43,97]. Moreover, researchers have been less concerned about the social interactions between Internet users when showing the relationship between mood levels and stock returns [48]. People tend to transfer emotions as a result of facial, vocal, and postural feedback, which the social science has recognized as emotional contagion [24,70]. As one of the most in<sup>fl</sup>uential microblogs in China, Sina Weibo provides users platforms to interact with friends and followers [8] through three types of user interactions: repost, praise, and comment [25]. Collecting and studying users’ data from Sina Weibo, we develop daily mood index for both investors and the news media and explore their in<sup>fl</sup>uence on stock return. In particular, our study focuses on emotional contagion and investigates how it contributes to interactions and enhances the e<sup>f</sup>ects of investor and news media sentiment on the stock return. Our results show that social interaction plays a positive moderating e<sup>f</sup>ect in the relationship between mood index and the stock return, thus indicating that social interaction on social media can a<sup>f</sup>ect people’s sentiments or behavior. Our <sup>fi</sup>ndings contribute to a better understanding of the relationship between social media and the stock return by considering the theory of emotion contagion in sentiment analysis.

## 7. Conclusions

## 7.1. Managerial implications

This study also has several managerial implications for both organizations and the stock market. By classifying microblog users into seven categories, we <sup>fi</sup>nd that both investors and the news media have a great impact on the stock returns.

There are many stakeholders involved in an organization, including shareholders, employees, customers, suppliers, and political groups [95]. It is necessary to consider stakeholder analysis in con<sup>fl</sup>ict resolution, project management, and business administration. Managers should identify which groups are most likely to be in<sup>fl</sup>uenced by a proposed action so as to prioritize groups according to their impacts on the action [98]. In reality, companies are more focused on shareholders, ignoring the interests of other stakeholders when making business decisions. Only when convening the general meeting can the enterprises receive feedback on the investment project, and there is usually very little of such type of feedback information obtained and transferred in a short time. The emergence of social media signi<sup>fi</sup>cantly facilitates the amount, speed, and range of information transmission [99,79]. People use these social platforms to write, share, comment, discuss, interact, and communicate [6]. Our <sup>fi</sup>ndings suggest that the prominent characteristics of microblogs have made them the center for collecting public opinions. They have extended the ways for the public to express their opinions, resulting in a new platform for public participation [100,25]. Therefore, we suggest that enterprises should pay more attention to the information released by their users and understand their thoughts in a timely fashion through social media, for example, delivering positive news about a company to the public will enhance the company’s image. Social media not only has provided a channel for communication between companies and the public but also has created a platform for establishing companies’ reputation and brand [101]. In the long term, social media will have an impact on a company’s performance.

Stock market regulators should pay more attention to the impact of social media information on the stock market and prevent companies or individuals from using the Internet to illegally manipulate the stock market. For example, a person might maliciously release adverse information about a company by distorting or exaggerating facts, which could mislead investors in their investment decisions. Moreover, insiders’ information disclosed through Weibo or other social media outlets will have a great impact on the stock market [102]. Therefore, the relevant regulators should take measures to reduce the negative impacts of social media on the stock market. First, establishing relevant laws and regulations can be an e<sup>f</sup>ective way to regulate the behavior of the news media. Second, regulators should strengthen the self-dis cipline of the media industry and guide the appropriate direction of the development of the media.

## 7.2. Limitations and future research

Despite our signi<sup>fi</sup>cant <sup>fi</sup>ndings, this research still has some limita tions that require more future work. First, we only focus on the Chinese real-estate stock market, which is limited in its sample size. Further research should increase the sample size to further corroborate the hypotheses. Second, we believe that the e<sup>f</sup>ect on intraday stock returns (i.e., the lagging e<sup>f</sup>ects of the stock market) should also be taken into account to produce a more accurate result [91]. Third, we select only two most active groups as our research object: investors and news media. Other users could also be taken into account [17]. Therefore, we can further discuss the impact of di<sup>f</sup>erent users on organizations or the stock market.

Future research could focus on important topics from a new shareholder’s perspective [6] and investigate related information about an organization and the stock market. We expect to discover hot topics for shareholders based on Social Network Analysis. Moreover, future papers can study the social interactions underlying the Hot-topic Network Graph. By constructing the Hot-topic Network Graph, we can measure social interactions from the perspective of the social network so that the abstract interactions can be transformed into a vivid interactive network. Moreover, based on the social network, this kind of social interaction can also be quanti<sup>fi</sup>ed. We can calculate network metrics, such as centrality and density, which can be achieved by UCINET<sup>5</sup> . We can add these network indicators into the equation and construct the Stakeholder-Stock Market model to more speci<sup>fi</sup>cally discuss either the impact of each kind of users on the stock of the enterprise or which kind of users has the greatest impact on the stock market. Thus, companies could be aware of such users and discuss their impact on the stock market. This approach would provide a new perspective for future research.

## Acknowledgments

This work was supported by grants from the National Natural Science Foundation of China (71772162), Natural Science Foundation of Zhejiang Province (LQ19G020004), Contemporary Business and Trade Research Center, and the Collaborative Innovation Center of Contemporary Business and Trade Circulation System Construction of Zhejiang Gongshang University (16YXYP01), Key Project of National Social Science foundation of China (19AGL015), Major Project of Key Research Institute of Humanities and Social Sciences of the Ministry of Education (17JJD790019), Special Funds Project for Promoting the Level of Running Local Colleges and Universities in Zhejiang Province (Interdisciplinary Innovation Team Building of Internet and Management Change) and the Zhejiang Provincial Scienti<sup>fi</sup>c and Technological Innovation activities for Xin Miao Talents Program (ID: 2017R408025). This research is the achievement of New Key Specialized Think Tank of Zhejiang Province (Zheshang Research Institute).

## Appendix A. Supplementary data

Supplementary material related to this article can be found, in the online version, at doi:https://doi.org/10.1016/j.im.2019.103181.

## References

[1] L.Y.N. Tang, Y.M. Zhang, F. Dai, Y.J. Yoon, Y.Q. Song, Sentiment analysis for the construction industry: a case study of weibo in China, Proceedings of the Asce International Workshop on Computing in Civil Engineering (2017) 270–281, https://doiorg/10.1061/9780784480823.033

[2] H. Xia, T. Lei, T. Jiliang, L. Huan, Exploiting social relations for sentiment analysis in microblogging, Proceedings of the The 6th ACM International Conference on Web Search and Data Mining (2013) 537–546, https://doi.org/10.1145/2433396. 2433465.

[3] S. Zhang, Sentiment analysis of chinese micro-blogs based on emoticons and emotional words, Comput.Sci. 36 (s3) (2012) 146–148, https://doi.org/10.3969/j. issn.1002-137X.2012.z3.041.

[4] S.M. Kim, E. Hovy, Extracting opinions, opinion holders, and topics expressed in online news media text. Proceedings of the The Workshop on Sentiment and Subiectivity in Text (2006) 1–8. https://doi,org/10.3115/1654641.1654642

[5] T. Ma, X. Wan, Opinion target extraction in Chinese news comments, Proceedings of the The 23rd International Conference on Computational Linguistics: Posters (2010) 782–790.

[6] X. Zhou, X. Wan, J. Xiao, Cminer: opinion extraction and summarization for chi nese microblogs, IEEE Trans. Knowl. Data Eng. 28 (7) (2016) 1650–1663, https:/ doi.org/10.1109/TKDE.2016.2541148.

[7] K. Zhao, A.C. Stylianoua, Y. Zheng, Sources and impacts of social in<sup>fl</sup>uence from online anonymous user reviews, Inf. Manag. 55 (1) (2018) 16–30, https://doi.org 10.1016/i.im.2017.03.006

[8] S. Deng, Z. Huang, A.P. Sinha, H. Zhao, The interaction between microblog sentiment and stock return: an empirical examination, MISO 42 (3) (2018) 895–918 https://doi.org/10.25300/MISO/2018/14268.

[9] X. Gabaix, D. Laibson, G. Moloche, S.E. Weinberg, The Allocation of Attention: Theory and Evidence, (2003), pp. 1–45 https://mpra.ub.uni-muenchen.de/ 47339/.

[10] C.M.A. Leung, Attention, search, and information di<sup>f</sup>usion : study of stock network dynamics and returns, J. Appl. Geophy. 105 (5) (2014) 147 158 http://hdl. handle.net/2152/25993.

[11] L. Fang, J. Peress, Media coverage and the cross section of stock returns, J. Finance 64 (5) (2009) 2023 2052 http://s3.amazonaws.com/zanran\_storage/faculty. insead.edu/ContentPages/460090162,pdf

[12] M. Gentzkow, J.M. Shapiro, What drives media slant? Evidence from us daily newspapers, Econometrica 78 (2010) 35–71 https://www.mendeley.com/ research-papers/drives-media-slant/

[13] K. Hou, W. Xiong, L. Peng, A tale of two anomalies: the implication of investor attention for price and earnings momentum, SSRN 45 (2008) 416–418, https:// doi.org/10.2139/ssrn.890875.

[14] S. Dellavigna, J.M. Pollet, Investor inattention and friday earnings announcements, J. Finance 64 (2) (2009) 709–749, https://doi.org/10.1111/j.1540-6261. 2009.01447.x.

[15] J. Li, J. Yu, Investor attention, psychological anchors, and stock return predict ability, J. Financi. Econ. 104 (2) (2010) 401–419, https://doi.org/10.1016/j. ifineco.2011.04.003

[16] N. Vozlyublennaia, Investor attention, index performance, and return predict ability, J. Bank. Financ. 41 (1) (2014) 17–35, https://doi.org/10.1016/j.jbank<sup>fi</sup>n. 2013.12.010

[17] M. Lemmon, Consumer con<sup>fi</sup>dence and asset prices: some empirical evidence, Rev. Financi, Stud. 19 (4) (2006) 1499–1529, https://doi,org/10.1093/rfs/hhi038

[18] L.X. Qiu, I. Welch, Investor sentiment measures, SSRN 117 (35) (2006) 367–377, https://doi.org/10.2139/ssrn.589641.

[19] S. Akhtar, R. Fa<sup>f</sup>, B. Oliver, A. Subrahmanyam, Reprint of: stock salience and th asymmetric market e<sup>f</sup>ect of consumer sentiment news, J. Bank. Financ. 36 (12) (2012) 3289–3301, https://doi.org/10.1016/j.jbank<sup>fi</sup>n.2012.07.019.

[20] B. Hernández-Ortega, Don’t believe strangers: online consumer reviews and the role of social psychological distance, Inf. Manag. 55 (1) (2018) 31–50, https://doi. org/10.1016/j.im.2017.03.007.

[21] Y.L. Rao, D.F. Peng, D.C. Cheng, Does media attention cause abnormal return?- Evidence from china’s stock market, Syst. Eng. Theory. Pract. 30 (2) (2010) 287–297 http://www.wanfangdata.com.cn/details/detail.do?\_type=perio&id= xtgcllysj201002014.

[22] Y. Zhang, D. Wan, L. Fu, An experimental study on how media reports a<sup>f</sup>ect in vestment behavior based on investor attention, Syst. Eng. (10) (2012) 19–27 http://qikan.cqvip.com/article/detail.aspx?id=44191894&from=zk\_search.

[23] S. Legge, L. Schmid, Media attention and betting markets, Eur. Econ. Rev. 87 (2016) 304–333, https://doi.org/10.1016/j.euroecorev.2016.06.001.

[24] E. Hatfreld, J.T. Cacioppo, R.L. Rapson, Emotional contagion, Curr. Dir. Psychol. Sci. 2 (3) (1993) 96–99, https://doi.org/10.1111/1467-8721.ep10770953.

[25] T. Wang, Y. Chen, Y. Wang, B. Wang, G. Yang, X. Li, H. Zheng, B.Y. Zhao, The power of comments: fostering social interactions in microblog networks, Front. Comput. Sci. China (5) (2016) 1–19, https://doi.org/10.1007/s11704-016- 5198-y.

[26] E.F. Fama, E<sup>fi</sup>cient capital markets: a review of theory and empirical work, J. Finance 25 (2) (1970) 383 417 https://www.jstor.org/stable/2325486.

[27] D. Kahneman, Attention and E<sup>f</sup>ort NJ, Englewood Cli<sup>f</sup>s, Prentice-Hall, 1973https://www.jstor.org/stable/1421603.

[28] M. Seasholes, G. Wu, Predictable behavior, pro<sup>fi</sup>ts, and attention, J. Empir. Financ. 14 (5) (2007) 590–610, https://doi.org/10.1016/j.jemp<sup>fi</sup>n.2007.03.002.

[29] L. Peng, W. Xiong, T. Bollerslev, Investor attention and time-varying comovements, Eur. Financi. Manag. 13 (3) (2007) 394–422, https://doi.org/10.1111/j. 1468-036X.2007.00366.x.

[30] T.J. Chemmanur, A. Yan, Advertising, Attention, and Stock Returns, SSRN: woking paper, 2009, https://ssrn.com/abstract=1340605.

[31] D. Lou, Maximizing Short-term Stock Prices Through Advertising, SSRN working paper, 2010, https://ssrn.com/abstract=1571947.

[32] B.M. Barber, T. Odean, All that glitters: the e<sup>f</sup>ect of attention and news on the buying behavior of individual and institutional investors, Rev. Econ. Stud. 21 (2) (2008) 785–818, https://doi.org/10.1093/rfs/hhm079.

[33] Z. Da, J. Engelberg, P. Gao, In search of attention, J. Finance 66 (5) (2011) 1461–1499, https://doi.org/10.1111/j.1540-6261.2011.01679.x.

[34] H. Markowitz, Portfolio selection, J. Finance 7 (1) (1952) 77–91 http://10.1111/j 1540-6261.1952.tb01525.x

[35] F.E. F, E<sup>fi</sup>cient capital markets: a review of theory and empirical work, J. Finance 25 (2) (1970) 383–417 https://www.istor.org/stable/2325486

[36] B.G. Malkiel, Expectations, bond prices, and the term structure of interest rates, Q.J. Econ. 76 (2) (1962) 197–218 http://10.2307/1880816.

[37] W.F.M.D. Bondt, Y.G. Muradoglu, H. Shefrin, S.K. Staikouras, Behavioral <sup>fi</sup>nance: Quo vadis? J. Appl. Financ. 18 (2) (2008) 7–21.

[38] M. Statman, K.L. Fisher, D. Anginer, A<sup>f</sup>ect in a behavioral asset-pricing model, Financ, Anal, J. 64 (2) (2008) 20–29 http://10.2139/ssrn,1094070.

[39] M. Virigineni, M.B. Rao, Contemporary developments in behavioral <sup>fi</sup>nance, Int. J. Econ. Financ. Iss. 7 (1) (2017) 448–459 http://econiournals.com/index.php/jiefi article/view/3809/pdf

[40] Y. Zhang, Y. Zhang, D. Shen, W. Zhang, Investor sentiment and stock returns: evidence from provincial tv audience rating in china, Phys. A 466 (2017) 288 294.

[41] K. Garris, J. Guillory, S.S. Sundar, Does interactivity serve the public interest?: the role of political blogs in deliberative democracy, Int. J. Intera. Commun. Syst. Tech. 1 (1) (2011) 1–18.

[42] A.D.I. Kramer, J.E. Guillory, J.T. Hancock, Experimental evidence of massive-scal emotional contagion through social networks, Proc. Natl. Acad. Sci. U.S.A. 111 (24) (2014) 8788 8790, https://doi.org/10.1073/pnas.1320040111.

[43] M. Nofer, O. Hinz, Using twitter to predict the stock market, Bus. Inf. Syst. Eng. 57 (4) (2015) 1–14. https://doi,org/10.1007/s12599-015-0390-4.

[44] W. Antweiler, M.Z. Frank, Is all that talk just noise? The information content of internet stock message boards, J. Finance 59 (3) (2004) 1259 1294 https://www. jstor.org/stable/3694736.

[45] E. Hat<sup>fi</sup>eld, J. Cacioppo, R. Rapson, Emotional contagion, Curr. Dir. Psychol. Sci. 2 (3) (1993) 96 99, https://doi.org/10.1111/1467-8721.ep10770953.

[46] K. Lewis, M. Gonzalez, J. Kaufman, Social selection and peer in<sup>fl</sup>uence in an onlin social network, Proc. Natl. Acad. Sci. U.S.A. 109 (1) (2012) 68–72, https://doi. org/10.1073/pnas.1109739109.

[47] M. Mcpherson, L. Smithlovin, J.M. Cook, Birds of a feather: homophily in social networks, Annu. Rev. Soc. 27 (1) (2001) 415–444, https://doi.org/10.1146/ annurev.soc.27.1.415.

[48] S.N. Durlauf, Y.M. Joannides, Social interactions, Annu, Rev. Econom, 2 (1) (2010 451–478. https://doi.org/10.1146/annurev.economics.050708.143312.

[49] C.F. Manski, Economic analysis of social interactions, J. Econ. Perspect. 14 (3) (2000).115–136. https://doi,org/10.1257/iep.14.3.115

[50] H. Hong, J.D. Kubik, J.C. Stein, Thy neighbor’s portfolio: word-of-mouth e<sup>f</sup>ects in the holdings and trades of money managers, J. Finance 60 (6) (2005) 2801–2824, https://doi.org/10.1111/i.1540-6261.2005.00817.x

[51] Q. Chen, I. Goldstein, W. Jiang, Price informativeness and investment sensitivity to stock price, Rev. Financi. Stud. 20 (3) (2007) 619–650, https://doi.org/10. 1093/rfs/hhl024.

[52] D. Kahneman, Attention and e<sup>f</sup>ort, Am. J. Psychol. 88 (2) (1975) 339–340,

https://doi.org/10.2307/1421603.

[53] A. Aouadi, M. Arouri, F. Teulon, Investor attention and stock market activity: evidence from france, Econ. Model. 35 (3) (2013) 674 681, https://doi.org/10 1016/i.econmod.2013.08.034.

[54] P. Klibano<sup>f</sup>, O. Lamont, T.A. Wizman, Investor reaction to salient news in closed end country funds, J. Finance 53 (2) (1998) 673–699, https://doi.org/10.1111 0022-1082.265570.

[55] W.S. Chan, Stock price reaction to news and no-news: drift and reversal after headlines, J. Financi. Econ. 70 (2) (2003) 223–260, https://doi.org/10.1016/ S0304-405X(03)00146-6.

[56] K. Daniel, D. Hirshleifer, A. Subrahmanyam, Investor psychology and securit under- and overreactions, J. Finance 53 (6) (1998) 1839–1885 http://www. kentdaniel.net/papers/published/jf98.pdf.

[57] H. Hong, J.C. Stein, A uni<sup>fi</sup>ed theory of underreaction, momentum trading, and overreaction in asset markets, J. Finance 54 (6) (1999) 2143–2184, https://doi. org/10.1111/0022-1082.00184.

[58] B.J. Bushee, J.E. Core, W. Guay, S.J.W. Hamm, The role of the business press as an information intermediary, J. Account. Res. 48 (1) (2010) 1–19, https://doi.org 10.1111/i.1475-679X.2009.00357.x

[59] C.H. Wu, C.J. Lin, The impact of media coverage on investor trading behavior and stock returns, Pac-Basin. Financi. J. 43 (C) (2017) 151–172, https://doi.org/10. 1016/j.pac<sup>fi</sup>n.2017.04.001.

[60] R.C. Merton, A simple model of capital market equilibrium with incomplete information, J. Finance 42 (3) (1987) 483–510, https://doi.org/10.1111/j.1540- 6261.1987.tb04565.x.

[61] J. Elster, Emotions and economic theory, J. Econ. Lit. 36 (1) (1998) 47 74 http:/ www.jstor.org/stable/2564951.

[62] B.E. Hermalin, A.M. Isen, The E<sup>f</sup>ect of A<sup>f</sup>ect on Economic and Strategic Decision Making, USC CLEO Research Paper No. C01-5, 2000, https://doi.org/10.2139 ssrn.200295.

[63] A.W. Lo, D.V. Repin, The psychophysiology of real-time <sup>fi</sup>nancial risk processing, J. Cogn. Neurosci. 14 (3) (2002) 323–339, https://doi.org/10.1162/ 089892902317361877.

[64] D. Hirshleifer, T. Shumway, Good day sunshine: stock returns and the weather, J. Finance 58 (3) (2003) 1009–1032, https://doi.org/10.1111/1540-6261.00556.

[65] P.C. Tetlock, Giving content to investor sentiment: the role of media in the stock market, J. Finance 62 (3) (2007) 1139 1168, https://doi.org/10.1111/j.1540- 6261.2007.01232.x.

[66] C.B. Walker. The direction of media influence: real-estate news and the stock market, J. Behav. Exp. Finance 10 (2016) 20–31, https://doi.org/10.1016/j.jbef. 2016.02.001.

[67] R.E. Whaley, The investor fear gauge, J. Portf. Manage. 26 (3) (2000) 12–17, https://doi.org/10.3905/jpm.2000.319728.

[68] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, J. Comput. Sci. 2.(1) (2011)1–8. https://doi,org/10.1016/i.jocs.2010.12.007

[69] W. Zhang, X. Li, D. Shen, A. Teglio, Daily happiness and stock returns: some international evidence, Physica A 460 (2016) 201–209, https://doi.org/10.1016/j. physa.2016.05.026.

[70] R. Neumann, F. Strack, Mood contagion": the automatic transfer of mood between persons, J. Pers. Soc. Psychol. 79 (2) (2000) 211–223, https://doi.org/10.1037/ 0022-3514.79.2.211.

[71] T. Wang, G. Wang, X. Li, H. Zheng, B.Y. Zhao, Characterizing and detecting malicious crowdsourcing, Proceedings of the The ACM SIGCOMM 2013 Conference on SIGCOMM (2013) 537–538. https://doi.org/10.1145/2534169. 2491719.

[72] G. Grullon, G. Kanatas, J.P. Weston, Advertising, breadth of ownership, and li quidity, SSRN 17 (2) (2004) 439–461, https://doi.org/10.1093/rfs/hhg039.

[73] Y. Zhang, M.F. Wiersema, Stock market reaction to ceo certi<sup>fi</sup>cation: the signaling role of ceo background, S.M.J. 30 (7) (2009) 693–710, https://doi.org/10.1002/ smj.772.

[74] L. Dong, Attracting investor attention through advertising, Rev. Financ. Stud. 27 (6) (2014) 1797 1829, https://doi.org/10.1093/rfs/hhu019.

[75] X. Fan, Y. Yuan, X. Zhuang, X. Jin, Long memory of abnormal investor attention and the cross-correlations between abnormal investor attention and trading vo lume, volatility respectively, Physica A 469 (1) (2017) 323 333, https://doi.org 10.1016/j.physa.2016.11.009.

[76] X. Luo, J. Zhang, W. Duan, Social media and <sup>fi</sup>rm equity value, Inf. Syst. Res. 24 (1) (2013) 146 163, https://doi.org/10.1287/isre.1120.0462.

[77] W. Zhang, Research on Investor Sentiment and Stock Market Performance Based on Micro-blog Text Mining, Diss, Shandong University, 2015, http://www. wanfangdata com cn/details/detail do? type =degree&id=Y2791635

[78] J.R. Nofsinger, Social mood and <sup>fi</sup>nancial economics, J. Behav. Financ. 6 (3) (2005) 144 160, https://doi.org/10.1207/s15427579jpfm0603\_4.

[79] L. Zhang, I. Pentina, Motivations and usage patterns of weibo, Cyberpsychol. Behav. Soc. Netw. 15 (6) (2012) 312 317, https://doi.org/10.1089/cyber.2011 0615.

[80] M. Kummerow, J.C. Lun, Information and communication technology in the rea estate industry: productivity, industry structure and market e<sup>fi</sup>ciency, Telecommun. Policy 29 (2–3) (2005) 173–190, https://doi.org/10.1016/j.telpol. 2004.12,003

[81] D. Guang, Z. Xuan, Z. Tian, F. Yang, Predicting stock using microblog moods, Chin. Commun. (8) (2016) 244–257 http://www.wanfangdata.com.cn/details/detail. do? type=perio&id =zgtx201608024.

[82] P. Zhou, Y. Zhang, X. Li, L. Yang, A study on the measurement of investor’s attention based on micro-blog information-empirical data from chinese stock market. Econ. Probl. (2) (2015) 159–166 http://www.wanfangdata.com.cn

details/detail.do?\_type=perio&id=jjwtts201502026.

[83] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up?: Sentiment classi<sup>fi</sup>cation using machine learning techniques, Proceedings of the Conference on Empirica Methods in Natural Language Processing (2002) 79–86, https://doi.org/10.3115/ 1118693.1118704.

[84] L.A. Adamic, N. Glance, The political blogosphere and the 2004 us election: divided they blog, Proceedings of the The 3rd International Workshop on Link Discovery (2005) 36–43, https://doi.org/10.1145/1134271.1134277.

[85] P.D. Turney, Thumbs up or thumbs down?: Semantic orientation applied to unsupervised classi<sup>fi</sup>cation of reviews, Proceedings of the The 40th Annual Meeting on Association for Computational Linguistics (2001) 417–424, https://doi.org/10. 3115/1073083.1073153

[86] H. Kanayama, T. Nasukawa, Fully automatic lexicon expansion for domainoriented sentiment analysis, Proceedings of the Proceedings of the 2006 Conferenc on Empirical Methods in Natural Language Processing Sydney, (2006), pp. 355–363.

[87] M.H. Kutner, C.J. Nachtsheim, J. Neter, Applied Linear Regression Models, 5th ed., McGraw-Hill Irwin, 2004, http://www.lavoisier.fr/livre/notice.asp?id= OOLWRRA333ROWQ.

[88] T. Rao, S. Srivastava, Analyzing Stock Market Movements Using Twitter Sentimen Analysis, Washington, USA (2012), pp. 119–123 https://dl.acm.org/citation.cfm? id=2456923.

[89] J. Boucher, C.E. Osgood, The pollyanna hypothesis, J. Verbal Learning Verba Behav. 8 (1) (1969) 1–8, https://doi.org/10.1016/S0022-5371(69)80002-2.

[90] Y. Zhang, D. Wan, L. Fu, Media coverage and ipo performance: information asymmetry or investor sentiment? - based on gem listed companies, Secu. Mark, Hera. (1) (2012) 70 77 http://www.szse.cn/main/<sup>fi</sup>les/2012/01/20 410036823709.pdf.

[91] A. Siganos, E. Vagenas-Nanos, P. Verwijmeren, Facebook’s daily sentiment and international stock markets, J. Econ. Behav. Organ. 107 (2014) 730–743, https:/ doi.org/10.1016/j.jebo.2014.06.004.

[92] S.R. Das, M.Y. Chen, Yahoo! For amazon: sentiment extraction from small talk on the web, Manag. Sci. 53 (9) (2007) 1375 1388.

[93] T. Nguyen, D. Phung, B. Adams, S. Venkatesh, Event extraction using behaviors of sentiment signals and burst structure in social media, Knowl. Imf. Syst. 37 (2) (2013) 279 304, https://doi.org/10.1007/s10115-012-0494-9.

[94] H. Sebastian, K. Christian, Z. Bernhard, Beyond fundamentals: investor sentiment and exchange rate forecasting, Eur. Financ. Manag. 19 (3) (2013) 558–578, https://doi.org/10.1111/j.1468-036X.2010.00593.x.

[95] T. Donaldson, L.E. Preston, The stakeholder theory of the corporation: concepts, evidence, and implications, Acad. Manage. Rev. 20 (1) (1995) 65–91 https://10. 2307/258887.

[96] L. Barbosa, J. Feng, Robust sentiment detection on twitter from biased and noisy data, ProCeedings of the International Conference on Computational Linguistics (2010) 36–44.

[97] R. Pandarachalil, S. Sendhilkumar, G.S. Mahalakshmi, Twitter sentiment analysis for large-scale data: an unsupervised approach, Cogn. Comput. 7 (2) (2015) 254–262.

[98] A.A. Elias, R.Y. Cavana, L.S. Jackson, Stakeholder analysis for r&d project management, R&D. Manag. 32 (4) (2002) 301–310 https://10.1111/1467-9310. 00262.

[99] T. Correa, A. WillardHinsley, H.G. Zúñiga, Who interacts on the web?: The

intersection of users’ personality and social media use, Comput Hum Behav. 26 (2) 247-253. https://doi.org/10.1016/j.chb.2009.09.003.

[100] J.J. Jussilaa, H. Kärkkäinena, H. Aramo-Immonenb, Social media utilization in business-to-business relationships of technology industry <sup>fi</sup>rms, Comput. Hum. Behav. 30 (2014) 606–613. https://doi.org/10.1016/i.chb.2013.07.047

[101] P. Aula, Social media, reputation risk and ambient publicity management, Strat. Leader. 38 (6) (2010) 43–49 https://10.1108/10878571011088069.

[102] R.L. Hagerman, J.P. Healy, The impact of sec-required disclosure and insidertrading regulations on the bid/ask spreads in the over-the-counter market, J. Acc. Pub. Poli. 11 (3) (1992) 233–243, https://doi.org/10.1016/0278-4254(92) 90009-M.

Yuan Sun is professor at Zhejiang Gongshang University, China. His main research interests include IT/IS usage, IT/IS Innovation, enterprise systems, performance evaluations, IS success, and online social network. He is also interested in various research methodologies. His research has been published in various journals, such as Information & Management, International Journal of Information Management, Journal of Enterprise Information Management, Enterprise Information Systems, Electronic Markets, Computers in Human Behavior, Computers in Industry, Computers & Education, Journal of Computer Information Systems, and various conference proceedings. Prof. Sun is currently serving as a Senior Editor for Information Technology & People, an Associate Editor for Journal of Electronic Commerce Research and Journal of Global Information Management. He is a member of the council of CNAIS

Xuan Liu is lecturer at Zhejiang Gongshang University, China. Her main research interests include social media, online social network, and user-generated content. Her research has been published in various journals, such as Corporate Social Responsibility and Environmental Management, Robotica, European Journal of International Management, Journal of Pacific Rim Psychology, and various conference proceedings.

Guangyue Chen is a master student at Fudan University, China. Her main research interests include corporate governance, accounting theory, and social media. Her research has been published in some journals and conference proceedings.

Yunhong Hao is professor at Zhejiang Gongshang University, China. His main research interests include corporate governance, accounting theory, and social media. His research has been published in various journals, such as Corporate Social Responsibility and Environmental Management, International Journal of Information Management, International Journal of Environmental Science and Technology.

Zuopeng (Justin) Zhang is a faculty member at the Coggin College of Business, University of North Florida. He was previously associate professor of Management, Information Systems, and Analytics at State University of New York, Plattsburgh. He received his Ph.D. degree in Business Administration with specialization in Management Science and Information Systems from Pennsylvania State University, University Park. His research interests include economics of information systems, knowledge management, electronic business, business process management, information security, and social net working. He is the editor-in-chief of the Journal of Global Information Management, an ABET program evaluator, and an JEEE senior member
