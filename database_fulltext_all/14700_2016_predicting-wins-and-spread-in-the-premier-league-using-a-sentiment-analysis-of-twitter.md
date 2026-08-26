---
otero_id: 14700
otero_key: "PHTP9H2X"
title: "Predicting wins and spread in the Premier League using a sentiment analysis of twitter"
authors: "Robert P. Schumaker; A. Tomasz Jarmoszko; Chester S. Labedz"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.05.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting wins and spread in the Premier League using a sentiment analysis of twitter

Robert P. Schumaker <sup>a</sup>, A. Tomasz Jarmoszko <sup>b</sup>, Chester S. Labedz Jr. <sup>c</sup>

<sup>a</sup> Computer Science Dept., University of Texas at Tyler, Tyler, TX 75799, USA

<sup>b</sup> Management Information Systems Dept., Central Connecticut State University, New Britain, CT 06050, USA

<sup>c</sup> Management & Organization Dept., Central Connecticut State University, New Britain, CT 06050, USA

## a r t i c l e i n f o

Article history: Received 11 January 2016 Received in revised form 30 May 2016 Accepted 31 May 2016 Available online xxxx

Keywords: Business intelligence Topic: Sentiment analysis Twitter Sports analytics English Premier League Crowdsourcing

## a b s t r a c t

Can the sentiment contained in tweets serve as a meaningful proxy to predict match outcomes and if so, can the magnitude of outcomes be predicted based on a degree of sentiment? To answer these questions we constructed the CentralSport system to gather tweets related to the twenty clubs of the English Premier League and analyze their sentiment content, not only to predict match outcomes, but also to use as a wagering decision system. From our analysis, tweet sentiment outperformed wagering on oddsfavorites, with higher payout returns (best \$2704.63 versus odds-only \$1887.88) but lower accuracy, a tradeoff from non-favorite wagering. This result may suggest a performance degradation that arises from conservatism in the odds-setting process, especially when three match results are possible outcomes. We found that leveraging a positive tweet sentiment surge over club average could net a payout of \$3011.20. Lastly, we found that as the magnitude of positive sentiment between two clubs increased, so too did the point spread; 0.42 goal difference for clubs with a slight positive edge versus 0.90 goal difference for an overwhelming difference in positive sentiment. In both these cases, the cultural expectancy of positive tweet dominance within the twitter-base may be realistic. These outcomes may suggest that professional odds-making excessively predicts non-positive match outcomes and tighter goal spreads. These results demonstrate the power of hidden information contained within tweet sentiment and has predictive implications on the design of automated wagering systems.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Predicting the outcomes of sporting events has a long and rich tradition. Since ancient times people have designed methods to divine natural and physical events. Today the urge to successfully predict still grips gamblers and academics alike. Prediction is no longer an art and probability is now considered a complex science. The most difficult aspect of prediction rests with identifying the relevant parameters and separating them from the noise of the event. Critical parameters are sometimes difficult to identify or measure, are constantly changing, or are not yet fully explored. The inability to correctly identify the most relevant parameters can sometimes lead to crippled systems relying on unimportant data or, worse, may create forecasts not based on sound science (e.g., basing predictions on the color of a uniform).

One way to simplify this problem of choosing and weighting parameters is to implement crowdsourcing as a forecasting tool. In James Surowiecki's seminal book, The Wisdom of Crowds [1], he made claim that large groups of individuals are better at making forecasts in conditions of uncertainty than are domain experts. This stems from collective intelligences, on the whole, being better able to properly sift through and analyze data than an individual. About the same time, another milestone book, Moneyball [2], popularized the use of statistics and sabermetric techniques (a quasi-scientific methodology of identifying relevant sports metrics, applying and refining them) in sports. Academic focus was not too far behind as the field of sports analytics gained popularity [3].

Twitter has been a boon to academic research with rich crowd-based datasets that can be easily collected and analyzed. Its data have been used to make predictions on phenomena as diverse as crime [4], the stock market [5], political elections [6], public opinion polls [7], public health [8] and movie sales [9]. The lure of twitter for academic research is two-fold. It provides a rich topical memory in the form of author-annotated hashtags, and provides a record of trends in public perception. Coupled together, academics can mine the twitterverse (i.e., universe of twitter data) and identify valuable insights.

Our research aims to demonstrate a crowdsourced system that can extract sentiment information from twitter to make match and point spread predictions in the English Premier League. Further, we analyze specific sentiment components such as tone and polarity, use them to calculate the degree changes in club-level sentiment and predict the magnitude of match goal differentials.

R.P. Schumaker et al. / Decision Support Systems xxx (2016) xxx–xxx

The rest of this paper is framed as follows. Section 2 provides an overview of literature concerning crowdsourcing, sentiment analysis and relevant studies. Section 3 presents our research questions. Section 4 introduces the CentralSport system and explains its various components. Section 5 sets up the Experimental design. Section 6 details the Experimental results and discussion. Finally Section 7 presents study conclusions and suggests further extensions of this stream of research.

## 2. Literature review

Crowdsourcing is a tool through which the average of crowd forecasts is used to predict future events [1]. In sports, this forecasting behavior generally equates to wagering on favorites and has been found to be a fairly accurate and reliable indicator of expectations. In a study of UFC fights, crowds were better able to predict wins (85.7%) than were bookies (67.6%) [10]. In a study of the wagering on matches in the Bundesliga (Germany's premier football league), crowds were found to be more accurate in their forecasts than bookies [11]. In a study of the FIFA World Cup 2006 tournament, crowds were also better able to predict winners than were pre-tournament rankings or random chance [12]. All three studies suggest that crowds were able to collectively make more accurate forecasts by weighting the data, not scientifically, but naïvely. Their decision-making contrasts with the weighting schemes designed by experts, which are driven by experience and previously seen patterns of data and profit generation. While crowdsourcing has demonstrated itself as an effective prediction tool, critics observe that some bettors may simply select the crowd favorite rather than evaluate the data independently [13]. This reinforcing behavior could lead to over-valuing the crowd favorite and can have an impact on accuracy. However, empirical evidence has shown that this typically encompasses a minority of wagering activity [13].

## 2.1. Odds-makers and wagering

Before two clubs take to the soccer playing field, or pitch, oddsmakers will set a betting line in an attempt to draw an equal currency amount of wagers on each club. By balancing the wagers, in effect the losing side of the wager pays the winning side minus the sportsbook's commission. Should the line become unbalanced, the sportsbooks are responsible for the difference and this imbalance may cause them a monetary loss. If one club is heavily favored, the sportsbook will increase odds on the less favored club to give bettors an incentive to wager longshots and rebalance the line.

One type of popular wagering system is the Moneyline. In this system, clubs with negative values are favored and clubs with high positive values are longshots. Odds and payouts are based on a unit of £100. For example, Arsenal and Swansea may have a Moneyline of −220 and +550 respectively. For the bettor on Arsenal (the favorite) they would need to wager £220 to win £100. For the Swansea bettor, they would wager £100 in a bid to win £550. The odds-makers attempt to gauge betting interest on the match and adjust the Moneyline to balance the monetary amounts wagered on both clubs.

Once odds are initially set, odds will move in response to the currency amount of wagers to continually balance the odds-makers match balance sheet. Because there are a variety of odds-makers with which to place wagers, the amount of currency wagering between clubs may differ between sportsbooks. This will lead to differences in odds between books. Typically the sportsbook with the more favorable odds will attract more wagering and will thus force their odds to return to market equilibrium.

<sup>1</sup> We use the terms odds-makers and sportsbooks interchangeably.

## 2.2. Social media and prediction

There has been much academic interest in using social media to make predictions. These predictions have crossed a diverse number of domains because of social media's rich crowd-based datasets that can be easily collected and analyzed. These areas have included crime, movie sales, politics, the stock market and sports. In a study of social media prediction and crime, twitter content was topically clustered into distinct discussion areas, correlated with the geo-location of the tweet and fed into a crime prediction model to demonstrate better predictive performance in 19 of 25 crime types [4]. Even though the tweeters were not making predictions themselves of crimes, their topics of discussion were a decent predictor.

In a study that correlated social media attention to movie sales, twitter content was found to be a good predictor [9]. In particular, positive twitter content was associated with higher movie sales whereas negative content was associated with lower movie sales. The authors also noted that tweets expressing an intention to watch a particular movie had the strongest predictive effect. In this case, tweeters were expressing their intention to watch or not watch a particular movie. This differs from the crime prediction study where the topics of the tweets themselves were used for prediction.

In US politics, twitter tweet counts and sentiment have been used to predict voter outcomes. In a study of the German Federal elections, Tumasjan et al. used a simple and easy to implement method of counting tweets that mention a candidate or political party [14]. Their reasoning was that tweets mentioning a candidate or party indicated their voting intention. This method was fairly accurate when applied against German federal elections with an error rate of 1.65%. When more complex methods were investigated such as using a sentiment analyzer to further determine voter intention, the results were not as precise [15]. Although the results are dependent upon the methods of how sentiment was captured and analyzed. It was further noted that sentiment polarity methods, at the time, were not sophisticated enough to recognize political language nuances, had poor performance and produced unacceptable errors [16].

Another political study investigated using a moving average of candidate, or elected official, tweet sentiment as a replacement to traditional polling services [7]. This work noted that natural language processing techniques achieved an 80% correlation.

In a study of the sentiment of financial news articles and the stock market, Schumaker et al. used the article sentiment as a method for predicting the magnitude of stock price movements immediately following article release [17]. Their work found that articles with a negative sentiment were easiest to predict, netting a 3.04% trading return using a simple trading engine.

Fans post tweets in order to express their personal feelings, most fundamentally (as we collected them) about the strengths, weaknesses and prospects of the team they follow and its next opponent. Admittedly, the tone and polarity of fans' tweets likely do not affect match results, except in cases in which extraordinary fan base sentiment might exceptionally motivate or demotivate a team. Fans' tweets by themselves are not likely to influence betting lines offered to bettors, which of course potentially includes those fans. Nonetheless, the tones and polarities of opponent fans' tweets may modestly affect initial betting line odds or later adjustments thereto, as we note elsewhere.

As tweets suggest the expected outcome on the field (i.e., the fulltime score line), the wisdom of crowds premise becomes more credible. Many thousands of fans, well versed through years as footballers themselves before advancing age and injuries transformed them into amateur pundits, bring considerable collective intelligence to sentiment crowdsourcing. This fan base is sufficiently diverse, decentralized through the reach of the Internet, able to be summarized and rabidly independent. In expressing their sentiments about real events on the turf pitch from odds-distorted results on the shadow field of wagering, fans' tweeted views contain useful raw information about future score lines.

In many of these studies, the act of tweeting was treated as an intention to act even though specific predictions were not solicited. The tweets themselves were used as predictive proxies. Putting this in terms of sports prediction from tweets, fans can choose to express their emotions towards their team as positive, negative or neutral (an intention to act), or choose not to tweet at all. This sentiment content can then be treated as an extra dimension of information.

## 2.3. Sentiment analysis

Investigating the role of sentiment as a predictor further, identifying fan or club-based sentiment could help in odds-setting or refinement. In sentiment analysis the focus is on analyzing direction-based text to determine tone (whether the author is positioning the text as objective/ factual or subjective/opinion-based) and polarity (whether the author's word choice is positive or negative) [18].

Sentiment analysis techniques have been well-studied in stock prediction [19,20] , online product sales [21] and corporate reputation [22]. One of the major findings was that negative sentiment was a better predictor of downward moves in firm value than were other sentimentbased techniques [23]. Further work identified positive and negative polarity in financial news to be consistent with human judgment [24] on firm performance [25–27].

To measure sentiment, one well-known and tested tool is OpinionFinder. This tool can identify sentence-level tone and polarity based on user-selected terms [28]. OpinionFinder was developed by Wiebe et al. based on a series of publications, such as the subjective sentence classifier [29,30], and the polarity classifier [31]. It performs well compared to the baseline MPQA Opinion Corpus, with an accuracy of 74%, subjective precision of 78.4%, subjective recall of 73.2% and a subjective F-measure of 75.7%, as compared to baseline MPQA's accuracy of 55.3%.

## 2.4. Sentiment analysis in sports

The use of twitter for prediction has become more popular among researchers. Schoen et al. posit that social media projects an impression “as a widely accepted and reliable source of data for predicting future outcomes [16].” Following up on this social media impression for prediction in sports, two studies have tackled using social media the prediction of outcomes of North American football games. Hong and Skiena [32] use Lydia – a text analytics system – to analyze four sources of online text streams: LiveJournal blogs, RSS blogs captured by Spinn3r, twitter and traditional news media. Using indicators of positive and negative sentiment within each message, the authors develop a measure of relative favorableness for teams which is then translated into a match prediction. They report the accuracy of their predictive method – when applied to 30 games between 2006 and 2009 – as 60%. Sinha et al. [33] undertake a study of the relationships between North American football games and tweets which mention the teams involved. The authors predict game outcomes for: 1) straight wins, 2) wins with/against the spread and 3) over-under point totals based on 10% of tweets exchanged during the 2010–2012 National Football League (NFL) seasons. Tweets were classified into weekly, pre-game and post-game categories and linked to specific teams via hashtags. Using logistic regression the authors determined prediction accuracy of 56%.

In European football (i.e., soccer), the most relevant studies are Godin et al. [34] and Radosavljevic et al. [35]. Although both studies aim to predict outcomes of English Premier League (EPL) games played during the 2013–2014 season, their methods differ. First, Godin et al. establish baseline predictive indicators of naïve predictions (home team always wins), expert predictions (BBC pundit views) and bookmaker predictions (the averaged odds of some 50 bookmakers). The three baseline methods lead to predictive accuracy of 51%, 60% and 67% respectively. Godin et al. then employ a variety of individual and combined methods including: two versions of statistical analysis, twitter volume, sentiment analysis, two versions of user prediction analysis, and combined methods of majority voting, early fusion and late fusion. Although they did not provide details of the number derivations, they claim predictive accuracy of 52% to 68%. It was also reported that a theoretical profit of 30% could have been realized in betting on EPL games during the second half of the 2013–2014 season.

Twitter is not the only possible source for input data for sentiment analysis. Radosavljevic et al. developed a method based on Poisson regression which used 83.1 billion posts in Tumblr to predict outcomes of the 2014 World Cup [35]. This method estimates the likelihood of win/draw/loss outcomes from vector elements that are based on the number of mentions of teams and players. The researchers trained their method on two years of international game data leading up to World Cup games. Application of their method to the World Cup resulted in a success rate of nearly 50% which is quite good for a three class problem like football.

## 2.5. Odds crowdsourcing versus sentiment crowdsourcing

The act of wagering on a match has the potential to influence odds movement. If enough actors in the domain engage in this activity, it can be considered a type of crowdsourcing where actors are collectively predicting match outcomes. Surowiecki describes how this collective intelligence works:

There are four key qualities that make a crowd smart. It needs to be diverse, so that people are bringing different pieces of information to the table. It needs to be decentralized, so that no one at the top is dictating the crowds answer. It needs a way of summarizing peoples opinions into one collective verdict. And the people in the crowd need to be independent, so that they pay attention mostly to their own information, and not worrying about what everyone around them thinks [1].

For odds movement, crowdsourcing easily fulfills two of the requirements: diversity of individuals and summarization of verdict. The second and fourth requirements, decentralization and paying attention to their own information, could be argued. While sportsbooks are not consolidated entities, their combined odds are generally on par with market equilibrium. We argue that it is not so much a matter of decentralization as it is market feedback that can lead to an arbitrage opportunity.

Taking this idea of market feedback further, the fourth part of Surowiecki's definition of crowd intelligence is being independent in decision-making and paying attention to their own information. While some bettors may behave in this manner, the public display of odds is meant to balance currency wagering and is not a true representation of crowd expectation. The reasons for wagering from a bettor's standpoint include luck and entertainment, desperation (e.g., wagering longshots) or wagering favorites in cases of laziness. Thus we cannot expect an odds-market to behave in a completely independent crowdsourced manner.

For sentiment of tweets, crowdsourcing fulfills all four of the requirements. Tweeters are a generally diversified group, linked by their interest in the EPL. It is decentralized from the standpoint that there is no centralized authority establishing sentiment or providing instant feedback. It can be used to summarize sentiment (i.e., the focus of this study) and it is mostly independent (although it could be argued that threaded discussion in twitter can ensue).

Given these arguments, we believe that crowdsourced sentiment may be a better predictor of match outcome than wager crowdsourcing.

## 2.6. Research gaps

Our review of the literature identified several opportunities not previously pursued, notably a lack of sentiment studies in football.

Although Godin et al. performed some research within this domain, we seek to extend the body of work to investigate both tone and polarity measures, and conduct a deeper investigation of wagering activity as an evaluative factor.

Another gap was that prior studies focused on a binary prediction of winners. We seek to leverage twitter sentiment and look for signals in the data such as the magnitude of polarity that may lead to predicting in-match goal differential. Our intent is to uncover sentiment information and apply it to match prediction in a novel and interesting way.

## 3. Research questions

These gaps in the literature led to the following research questions:

1. What signals exist in twitter data that may provide match predictions? Following Surowiecki's crowdsourcing approach, we believe that tweeters (i.e., tweet authors) are better able to make match predictions than bettors and are able to convey those predictions through the sentiment of their word choice. Tweets that are positive may be indicative of a favorable match outcome whereas negative tweets may reflect pessimism and predict a potential loss. We feel that the normalized aggregate view of this sentiment information for each club and match may have predictive value.

2. What role does sentiment magnitude have on successful match prediction?

Similarly we believe that a normalized imbalance of positive vs negative sentiments may help predict goal differential. We plan to investigate the magnitude of match sentiment versus the respective club averages. We reason that a significant surge or drop in matchlevel sentiment versus their club average may be a predictive signal of potential goal difference. It is further believed that a club with a normalized surge in positive tweets may win by a larger margin than one in which the difference is less. Conversely, a club with a surge in negative tweets may be expected to lose by a larger margin than one where the difference is less than average.

3. What is the impact of sentiment-based prediction on wagering returns?

From prior studies, accuracy and wagering profit have been observed to have an inverse relationship (i.e., high accuracy/low payout or low accuracy/high payout). Does the same hold true in the EPL, and if so, how are crowds able to identify longshot wins over odds-makers?

## 4. System design

To address our research questions, we built the CentralSport system as shown in Fig. 1.

The CentralSport system is a twitter collector and sentiment analysis tool that interfaces directly with twitter's streaming API and captures desired tweets in real-time based on the hashtag filter. Each tweet is composed of specific information, such as the twitter handle (i.e., chosen name of the tweet author a.k.a. tweeter), the date/time it was tweeted and the tweet content. This feed is stored in a database along with match results and betting lines at match start, for each match, as shown in Table 1.

Match results are obtained from ESPN.com and are manually entered into the system. Betting lines are acquired from OddsPortal. com which is an aggregation of 15 different sports books and follows the Moneyline wagering approach. Moneyline odds are unitless, meaning the monetary unit (e.g., dollar, pound, and euro) is irrelevant. We chose to use dollars for this research. Specific wagering details are further described in the Experimental design section.

Once collected, each tweet is analyzed using OpinionFinder to identify sentiment information. It categorizes tweets in two axes, tone and polarity. Tone evaluates whether a tweet is subjective or objective. OpinionFinder classifies each sentence within the tweet, and the designation of tone for the tweet follows the majority of the individual sentences. In cases of a tie or ambiguity, the tweet is marked tone neutral. Here are examples of tweet tone:

Objective: Andre Schurrle celebrates his first Premier League goal for Chelsea #cfc.

Subjective: Has someone just took the batteries out of our players???? Our players have just stopped functioning???? #mufc.

Polarity evaluates the positive or negative bias of a tweet. Like tone, polarity classifies each sentence and uses majority rules. Tweets can be marked polarity neutral in cases of ambiguity or a tie. Examples of tweet polarity include:

Negative: Supporting Newcastle is actually making me hate football #nufc.

Positive: Were delighted to confirm the signing of @R9Soldado from Valencia after successfully completing his medical. #thfc.

![](/api/attachments/PHTP9H2X/fulltext/images/291621cb1fbeb06e7ac902100adddada28476af4ff2744b2f3f3ee75fd8438dd.jpg)  
Fig. 1. The CentralSport system.

Please cite this article as: R.P. Schumaker, et al., Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.010

R.P. Schumaker et al. / Decision Support Systems xxx (2016) xxx–xxx

Table 1  
Sample match results and betting lines.

<table><tr><td>HomeClub</td><td>AwayClub</td><td>MatchStart</td><td>HomeScore</td><td>AwayScore</td><td>HomeOdds</td><td>DrawOdds</td><td>AwayOdds</td></tr><tr><td>#lfc</td><td>#nufc</td><td>2014-05-11 10:00:00.000</td><td>2</td><td>1</td><td>-556</td><td>706</td><td>1345</td></tr><tr><td>#mcfc</td><td>#whufc</td><td>2014-05-11 10:00:00.000</td><td>2</td><td>0</td><td>-588</td><td>760</td><td>1303</td></tr><tr><td>#ncfc</td><td>#afc</td><td>2014-05-11 10:00:00.000</td><td>0</td><td>2</td><td>396</td><td>300</td><td>-145</td></tr><tr><td>#saintsfc</td><td>#mufc</td><td>2014-05-11 10:00:00.000</td><td>1</td><td>1</td><td>175</td><td>273</td><td>141</td></tr><tr><td>#sufc</td><td>#swans</td><td>2014-05-11 10:00:00.000</td><td>1</td><td>3</td><td>13</td><td>244</td><td>225</td></tr></table>

For tweets with more than one hashtag, we elected to label it with the first club hashtag. We reason that if a tweet mentions two or more clubs, the tweeter may have intended more emphasis towards the first club mentioned. While not perfect, we felt this to be an adequate automation compromise for the large volume of tweets collected.

## 5. Experimental design

## 5.1. The experiment

For this study we used data from the final three months of the 2013– 2014 English Premier League season, February 16 through May 11, 2014. Tweets were gathered from the twitter streaming API using one team-specific hashtag per club, identified by a domain expert. While we recognize that using only one hashtag per club may be a study limitation compared to gathering an entire universe of club-related tweets, the volume of tweets gathered offsets the limitation.

During this period, 122 matches were played. For each match we used tweets for the ninety-six hours up to match start, consistent with Hong and Skiena's work. From these data we constructed a baseline model that used aggregated odds-only data from OddsPortal.com to predict outcomes, and eight sentiment models that describe the data based on the axes of tone and polarity. Fig. 2 depicts the sentiment models with an explanation to follow.

From this figure we develop eight models across the axes of tone and polarity; Model 1 — Subjective Negative tweets, Model 2 — Objective Negative, Model 3 — Subjective Positive, Model 4 — Objective Positive, Model 5 — All Subjective, Model 6 — All Objective, Model 7 — All Negative, and Model 8 — All Positive.

To address those tweets identified as either neutral tone or neutral polarity, we chose not to use them in the models. While it could be argued that neutral tone tweets should not have an impact on Models 7 and 8, All Negative and All Positive respectively, we felt that using identical data across all models would provide a more robust and equal comparison between models.

For our first research question, we test sentiment between clubs of unequal tweets by normalizing the sentiment model data versus tweets for the particular club and match, and used it for comparison purposes as shown in Eq. (1).

$$
\text { Max } \left(\frac {\Sigma (\text { Tweets } \mid \text { Model } _ {n} , \text { Club } _ {1} , \text { Match } _ {m})}{\Sigma (\text { Tweets } \mid \text { Club } _ {1} , \text { Match } _ {m})}, \frac {\Sigma (\text { Tweets } \mid \text { Model } _ {n} , \text { Club } _ {2} , \text { Match } _ {m})}{\Sigma (\text { Tweets } \mid \text { Club } _ {2} , \text { Match } _ {m})}\right)\tag{1}
$$

![](/api/attachments/PHTP9H2X/fulltext/images/509f5e53ab9c5b20fb6fb18b4fb1266952e250daac7c4621b33556d1bfc23f3b.jpg)  
Fig. 2. Sentiment models.

For models using negative polarity sentiment (Models 1, 2 and 7), we expect that the club with the higher match normalized value would lose, following the logic that negative sentiment indicates anxiety and a potential for loss. Whereas for all other sentiment models we expected the club with the highest value to win. Table 2 demonstrates how match normalization works using Model 8 — All Positive tweets.

From this table, the home club variable HNrmlz is the number of positive tweets for Manchester United (8503) in the ninety-six hours before match start, divided by the overall number of tweets for Man United (10,138) during the same period, excluding neutral categories. A similar calculation was performed for ANrmlz. Comparing the two values (0.8387 versus 0.6955 for Home and Away respectively), the Home team has greater subjective positive sentiment and is predicted to win the match.

For our second and third research questions, we use averaged clubbased sentiment, where the number of sentiment-based tweets for the match is compared against an average value for the club. This measure indicates if a surge or drop in sentiment is occurring for a particular match, which may indicate predictive value. We then analyze each match, comparing values using the formula in Eq. (2).

$$
M a x \left(\frac {\Sigma (T w e e t s \mid M o d e l _ {n} , C l u b _ {1} , M a t c h _ {m})}{\Sigma (T w e e t s \mid M o d e l _ {n} , C l u b _ {1}) / \Sigma (m \mid C l u b _ {1})}, \frac {\Sigma (T w e e t s \mid M o d e l _ {n} , C l u b _ {2} , M a t c h _ {m})}{\Sigma (T w e e t s \mid M o d e l _ {n} , C l u b _ {2}) / \Sigma (m \mid C l u b _ {2})}\right)\tag{2}
$$

We expect models with higher values for Models 1, 2 and 7, to lose. For all other sentiment models we expected the club with the highest value to win. As an example using Manchester United from earlier, we use the number of positive tweets in the ninety-six hours before match start (8503) and divide it by the average number of tweets for Model 8 — All Positive (8317.2) for a normalized value of 1.0223 versus Liverpool at 8.0314. These values indicate that both clubs were more positive in their tweets than average, however, Liverpool was 8× their typical positive sentiment and the model would predict them to win the match (Liverpool did win and it was an odds upset).

## 5.2. The collection

For the study period, 18,027,966 tweets were gathered. The average tweet length was 105.0 characters with a standard deviation of 34.9. Removing the neutral tone and polarity tweets and using tweets only within the ninety-six hours before match start left a dataset of 1,026,569 tweets as broken down by club and sentiment values in Table 3.

From this table, Manchester United, Liverpool, Chelsea, Arsenal and Manchester City had the most tweets, consistent with expectations based on club size and popularity. Clubs promoted to the 2013–2014 Premier League (i.e., Cardiff City, Crystal Palace and Hull City) had some of the fewest, but not the least, number of tweets.

This table indicates that the tone of tweets was mostly objective, 96.7% of tone. For polarity (e.g., whether the tweet is positive or negative), every club's tweeters were more positive (average 68.6%) than negative, expressing a mostly optimistic attitude. The most optimistic club tweeters followed Sunderland (79.4%), Southampton (72.8%) and Liverpool (71.8%). Looking at the optimistic club records (win-draw-loss), Sunderland was 4–2-7, Southampton 5–2-5 and Liverpool 10–1-1. It

Please cite this article as: R.P. Schumaker, et al., Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.010

R.P. Schumaker et al. / Decision Support Systems xxx (2016) xxx–xxx

Table 2  
Example of match normalization for Model 8 (All Positive).

<table><tr><td>HomeClub</td><td>AwayClub</td><td>Date</td><td>#Htweets</td><td>#Atweets</td><td>#HMod8</td><td>#AMod8</td><td>HNrmlz</td><td>ANrmlz</td></tr><tr><td>Man United</td><td>Liverpool</td><td>3/16/2014</td><td>10,138</td><td>5034</td><td>8503</td><td>3501</td><td>0.8387</td><td>0.6955</td></tr></table>

was interesting to note that it was not necessarily the clubs with the best records that had the highest fan optimism (as demonstrated by Sunderland). We speculate that the optimism/pessimism differences may be due to regional cultural differences. Although interesting, this was not the focus of our research.

## 5.3. The metrics

We evaluated the models on accuracy (i.e., how correct the models were versus actual results), payout (i.e., constructing a simple wagering algorithm to measure hypothetical payouts) and betting efficiency (i.e., the averaged payout per wager). Depending on the sentiment model to be tested, the relevant axes of tone (objective/subjective) and polarity (positive/negative) were used.

## 5.3.1. Accuracy

Accuracy is a measure of predicted match outcome versus actual outcome. Aggregating the average of the 122 matches for each model led to this measure. Based on the values of the normalized match data and the model, the system would select either the home or away club to win. If either the number of Home or Away tweets for the model was 0, then the match was not considered for that model. A Draw wager was considered, however, it was found that sentiment was unable to fully recognize a draw outcome and we chose to ignore this category. Even so, the performance returns from predicting just Home and Away match outcomes offset the need for Draw. Within our dataset, there were 6 draw occurrences.

## 5.3.2. Payout

Payout is a summed value of returns on hypothetical \$100 wagers made on predicted match outcomes for the 122 matches. For models using negative polarity sentiment (Models 1, 2 and 7), the wagering engine would bet on the club with the highest normalized value to lose. All other models bet on the club with the highest normalized value to win. Further, a third decision of No Bet was used if either the number of Home or Away tweets for the model was 0.

5.3.3. Wagering efficiency

Wagering efficiency is the aggregated wagering payout for all wagered matches divided by the number of matches wagered upon for each model. This value allows us to identify which models produce the best return with the least bankroll.

## 6. Experimental findings and discussion

## 6.1. What signals exist in twitter data

To answer our first research question, what signals exist in twitter data that may provide match predictions, we looked at the accuracy and payout of predictions. Table 4 presents the results.

The baseline odds-only approach was correct on 80 of the 122 matches in our study for an accuracy of 65.57% holding consistent with Godin et al.'s observation of 67%. None of the sentiment models outperformed baseline on accuracy and only two models (Model 1 — Subjective Negative and Model 6 — All Objective) were at or exceeded 50.0%. A careful reader will observe that Model 5 — All Subjective does not appear to reflect a weighted average of Model 1 — Subjective Negative and Model 3 — Subjective Positive, because the tweet limit threshold per match is exceeded for some matches in Model 5. The same applies to Model 6 — All Objective.

While the accuracy results are not attractive, accuracy only presents one facet of the results whereas the more interesting metrics to the gambler or betting house is payout and betting efficiency. Payout measures the hypothetical return on a \$100 wager for either the home or away club, with the exception of the No Bet category. Payout is the amount of return derived from wagering, minus the initial wager amount. The column Excess Return is the payout of the model minus Baseline. Positive Excess Return values indicate a return greater than Baseline. From the table, Baseline had a \$1887.88 payout. Seven of the eight sentiment models also exhibited a positive payout. Only Model 5 (All Subjective) with a \$195.54 payout loss did not. This is the result of fan sentiment skewing slightly towards longshot wagers, decreasing accuracy with the trade-off of better payouts.

Table 3  
Breakdown of club level sentiment.

<table><tr><td>Club Name</td><td>Hashtag</td><td># Tweets</td><td># Objective</td><td># Subjective</td><td># Positive</td><td># Negative</td></tr><tr><td>Arsenal</td><td>#afc</td><td>45,807</td><td>44,194</td><td>1613</td><td>29,176</td><td>16,631</td></tr><tr><td>Aston Villa</td><td>#avfc</td><td>9794</td><td>9442</td><td>352</td><td>6435</td><td>3359</td></tr><tr><td>Cardiff City</td><td>#cardiffcity</td><td>727</td><td>705</td><td>22</td><td>397</td><td>330</td></tr><tr><td>Chelsea</td><td>#cfc</td><td>70,912</td><td>69,008</td><td>1904</td><td>50,781</td><td>20,131</td></tr><tr><td>Crystal Palace</td><td>#cpfc</td><td>6603</td><td>6360</td><td>243</td><td>4615</td><td>1988</td></tr><tr><td>Everton</td><td>#efc</td><td>10,059</td><td>9791</td><td>268</td><td>6000</td><td>4059</td></tr><tr><td>Fulham</td><td>#ffc</td><td>3205</td><td>2748</td><td>457</td><td>2279</td><td>926</td></tr><tr><td>Hull City</td><td>#hcafc</td><td>2214</td><td>2126</td><td>88</td><td>1385</td><td>829</td></tr><tr><td>Liverpool</td><td>#lfc</td><td>86,636</td><td>83,419</td><td>3217</td><td>62,228</td><td>24,408</td></tr><tr><td>Manchester City</td><td>#mcfc</td><td>35,504</td><td>34,402</td><td>1102</td><td>22,185</td><td>13,319</td></tr><tr><td>Manchester United</td><td>#mufc</td><td>171,499</td><td>166,459</td><td>5040</td><td>121,310</td><td>50,189</td></tr><tr><td>Newcastle</td><td>#nufc</td><td>11,763</td><td>11,256</td><td>507</td><td>6421</td><td>5342</td></tr><tr><td>Norwich</td><td>#ncfc</td><td>4513</td><td>4319</td><td>194</td><td>2830</td><td>1683</td></tr><tr><td>Southampton</td><td>#saintsfc</td><td>4682</td><td>4596</td><td>86</td><td>3407</td><td>1275</td></tr><tr><td>Stoke City</td><td>#scfc</td><td>2491</td><td>2432</td><td>59</td><td>1589</td><td>902</td></tr><tr><td>Sunderland</td><td>#sufc</td><td>4620</td><td>4294</td><td>326</td><td>3668</td><td>952</td></tr><tr><td>Swansea</td><td>#swans</td><td>1601</td><td>1554</td><td>47</td><td>1052</td><td>549</td></tr><tr><td>Tottenham</td><td>#thfc</td><td>12,450</td><td>12,013</td><td>437</td><td>7219</td><td>5231</td></tr><tr><td>West Bromwich</td><td>#wbafc</td><td>366</td><td>338</td><td>28</td><td>228</td><td>138</td></tr><tr><td>West Ham</td><td>#whufc</td><td>3583</td><td>3448</td><td>135</td><td>2184</td><td>1399</td></tr></table>

Please cite this article as: R.P. Schumaker, et al., Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.010

Table 4  
Accuracy and payout results of models.

<table><tr><td></td><td>Correct</td><td>Incorrect</td><td>No Bet</td><td>Accuracy</td><td>Payout</td><td>Excess return</td></tr><tr><td>Baseline</td><td>80</td><td>42</td><td>0</td><td>65.57%</td><td>$1887.88</td><td></td></tr><tr><td>Model 1</td><td>52</td><td>51</td><td>19</td><td>50.49%</td><td>$1934.70</td><td>$46.82</td></tr><tr><td>Model 2</td><td>55</td><td>67</td><td>0</td><td>45.08%</td><td>$1946.53</td><td>$58.65</td></tr><tr><td>Model 3</td><td>41</td><td>61</td><td>20</td><td>40.20%</td><td>$823.38</td><td>($1064.50)</td></tr><tr><td>Model 4</td><td>58</td><td>64</td><td>0</td><td>47.54%</td><td>$2270.55</td><td>$382.67</td></tr><tr><td>Model 5</td><td>44</td><td>72</td><td>6</td><td>37.93%</td><td>($195.54)</td><td>($2083.42)</td></tr><tr><td>Model 6</td><td>61</td><td>61</td><td>0</td><td>50.00%</td><td>$2704.63</td><td>$816.75</td></tr><tr><td>Model 7</td><td>57</td><td>65</td><td>0</td><td>46.72%</td><td>$2614.53</td><td>$726.65</td></tr><tr><td>Model 8</td><td>55</td><td>67</td><td>0</td><td>45.08%</td><td>$1708.52</td><td>($179.36)</td></tr></table>

Further, models that incorporate some level of positive and subjective tweets (Model 3 – Subjective Positive, Model 5 — All Subjective and Model 8 — All Positive) had negative excess returns. The sentiment models with the best excess returns were Model 6 (All Objective) with an excess return of \$816.75 above baseline, Model 7 (All Negative) with \$726.65 and Model 4 (Objective Positive) with an excess return of \$382.67 over Baseline.

While the models that incorporated sentiment did not exhibit better prediction accuracy than the odds-only approach, two of the models that used subjective-only data reported negative excess returns versus the models that incorporated some form of objective data. This observation was unexpected and counter-intuitive at the surface. In prior sentiment work on financial news articles and their impact on stock price, researchers had found that subjective articles were better predictors of price movement than objective articles [17]. It was believed that the tone of the articles was influencing traders and consequently price. However, for this study, tweets of a subjective nature have a negative effect, and objective tweets are more meaningful predictors. We believe this to be the case for two reasons. First, tweets are more descriptive, a reflection of individual expression, and not prescriptive. In other words, tweets are generally not reporting previously unknown events that may impact play which may be the case for financial news sentiment. The second reason is noise in the medium. With financial news articles, there are fewer articles to apply to a longer event horizon (i.e., trading day). With sports-related tweets, there are many (sometimes thousands) more tweets to correspond to an event of a much more limited duration. As a consequence of the deluge of information (one could argue the quality of the information too) and shorter event duration, the noise from tweets would be greater and hence less influential (if at all) than would financial news articles.

## 6.2. What role does polarity magnitude have on match prediction?

To answer our second research question, what role does sentiment magnitude have on successful match prediction, we looked at the polarity models, Models 7 and 8, All Negative and All Positive tweets respectively. For the analysis we normalized data by dividing the number of tweets for each match by the average number of tweets for the model over the period of study. The normalized values tell us if there is a surge or drop in positive/negative sentiment, and by how much. Next, we compared the values between clubs for each match (e.g., Manchester United (1.0223) versus Liverpool (8.0314) is a difference of 7.0090 on Liverpool's behalf) and used these differences as sentiment magnitudes. A sliding threshold from 0 to 10 in 0.1 increments was introduced, where only sentiment magnitude differences greater than or equal to the threshold value was used for accuracy and payout calculations. Fig. 3 shows the accuracy and payout results of the models versus the sliding sentiment magnitude thresholds.

For a sliding threshold (sentiment magnitude) of zero, we wager on all matches (excluding No Bet). Whereas for sentiment magnitude of 1.0, we wager only on those matches where the difference in sentiment magnitude is at least 100% greater. Positive tweets at sentiment magnitude zero had an accuracy of 53.28% and payout of \$3011.20, versus negative polarity with 27.87% accuracy and \$315.17 payout. Model 8 (All Positive) had good accuracy results that improved to 75.00% on thresholds between 4.3 and 5.3 inclusively, on 12 matches, before declining. This same model also had sizeable payouts, peaking at \$3295.24 at 0.9 threshold on 52 matches, before declining. Model 7 (All Negative) had comparatively worse accuracy, peaking at 36.1% at 1.7 threshold on 36 matches, before descending to 0% accuracy at thresholds 4.3 and greater. Model 7 also exhibited worse payouts by comparison, maxing out at \$1215.03 at 1.7 threshold on 36 matches. From these data it would appear that positive sentiment was a better predictor of match outcomes. We believe that coupled with the fan optimism finding from earlier, positive sentiment may be the cultural expectancy for the English Premier League twitter-base, with the majority of tweeters from the UK. Looking into this further, we also note an excessive number of All Positive tweets (276,628) versus All Negative (132,906).

Next we examined if the sentiment magnitude was a predictor of match goal differential. It was expected that as sentiment magnitude increased between clubs it would have a similar increase on expected goals. Table 5 depicts the average of goals broken down by sentiment magnitude.

For both models, as the magnitude of sentiment difference between clubs increased, so too did the goal differential. However, Model 7 (All Negative) showed a contrarian relationship. As tweeters became more negative towards the club, the number of goals scored for that club increased leading to that club winning. We speculate that this is attributable to opposing club tweeters disparaging a stronger opponent. Looking deeper into the data, 76.9% of the negative sentiment magnitude greater than or equal to 2.0 was directed towards the oddsfavorite club. Seven times this phenomenon was observed against Liverpool, eight times against Manchester United, four times against Chelsea and one time by Chelsea against Liverpool, four times by Aston Villa, and two times by Cardiff City, Manchester City and Sunderland against stronger opponents. It would appear that it wasn't

![](/api/attachments/PHTP9H2X/fulltext/images/2998d154583a502fd23a4db6ca55343fbf7acecdc763c0c9cc909f4b8f535fff.jpg)

![](/api/attachments/PHTP9H2X/fulltext/images/87f959cfe73bd2696530e874bd50b9054aa6e55dd67e1be570be4403e8623870.jpg)  
Fig. 3. Accuracy and payout of Models 7 and 8 versus sentiment thresholds.

Please cite this article as: R.P. Schumaker, et al., Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.010

Table 5  
Models 7 and 8 average of goals versus sentiment magnitude.

<table><tr><td>Sentiment magnitude</td><td>Model 7</td><td>Model 8</td></tr><tr><td>0.0 ≥ x &lt; 1.0</td><td>+0.60</td><td>+0.42</td></tr><tr><td>1.0 ≥ x &lt; 2.0</td><td>+0.69</td><td>+1.07</td></tr><tr><td>x ≥ 2.0</td><td>+1.15</td><td>+0.90</td></tr></table>

the clubs' fans disparaging their own team, but rather spirited conversation from the weaker opponent.

Model 8 (All Positive) similarly showed an increase in goals, however, for sentiment magnitudes over 2.0× different, the average goals decreased (0.90). While still positive and consistent with expectations, this deviation could indicate an overconfidence in the club.

## 6.3. What is the impact of prediction on wagering returns?

To answer our third research question, what is the impact of sentiment-based prediction on wagering returns, we looked at balancing accuracy and payout with betting efficiency, which provides the average return per wager minus the initial bet.

In looking at the models, both Models 7 and 8 were profitably engaged in betting against favorites and longshot wagering. We define betting against the favorites as seeking a return between 1 and 2 times the wager, based on the odds (e.g., Moneyline odds between +100 and +199 inclusive). We further define longshot wagers as seeking a return of 2 or more times the wager (e.g., Moneyline odds of +200 or greater). While we recognize that some matches will have positive Moneyline odds for both clubs (e.g., meaning a wager either way would be against the favorites using our definition), we feel that breaking apart the wagering activity into these distinct buckets will provide additional insight as shown in Table 6.

From this table several interesting trends emerge. First, for wagering Mx Against, against the favorites across models (left-side of the table), the accuracy, payouts and betting efficiency values are fairly similar to Baseline on the same matches, with a slight edge to both Models 7 and 8. This would indicate a weak relationship between both all positive and all negative tweet sentiment and a better return on match prediction than following an odds-only approach (\$14.71 versus \$14.46 for Model 7 and \$15.32 versus \$15.07 for Model 8).

Second, in looking at Mx Against and Mx Longshots (left to right), we notice that accuracy decreases, and payouts increase, consistent with prior results. What is interesting is that Baseline did not follow the same pattern. For Baseline, both Accuracy and Payout increased. We theorize that this is a result of the three classes of outcomes: win, draw and loss. Because of the three outcomes, sometimes Moneyline wagering will show strong positive values for all classes (especially if clubs are evenly matched). Looking through the data this did appear to be the case and helps to explain the discrepancy.

Third, in wagering on just Mx Longshots (seeking returns 2 or more times the wager), Model 7 outperformed Baseline on payout and betting efficiency, but for Model 8, Baseline garnered the higher values. Returning to our earlier comment in the second research question, we speculate that this may indicate a sentiment overconfidence in the wagered clubs, especially given the strong positive sentiment that M8 Longshots portrays.

Table 6  
Results of wagering activity against favorites and longshots.

<table><tr><td>Model 7</td><td>Baseline</td><td>M7 against</td><td>Baseline</td><td>M7 longshots</td></tr><tr><td>Accuracy</td><td>50.00%</td><td>50.00%</td><td>65.45%</td><td>23.64%</td></tr><tr><td>Payout</td><td>$405.00</td><td>$412.00</td><td>$907.36</td><td>$1627.00</td></tr><tr><td>Bet Efficiency</td><td>$14.46</td><td>$14.71</td><td>$16.50</td><td>$29.58</td></tr><tr><td>Model 8</td><td>Baseline</td><td>M8 against</td><td>Baseline</td><td>M8 longshots</td></tr><tr><td>Accuracy</td><td>50.00%</td><td>50.00%</td><td>68.52%</td><td>22.22%</td></tr><tr><td>Payout</td><td>$422.00</td><td>$429.00</td><td>$1189.37</td><td>$1003.00</td></tr><tr><td>Bet Efficiency</td><td>$15.07</td><td>$15.32</td><td>$22.03</td><td>$18.57</td></tr></table>

From our observations it would appear that twitter sentiment can be effectively used to uncover arbitrage wagering opportunities.

## 7. Conclusions and future directions

From our study we found that crowdsourced sentiment can be a better predictor of match outcomes than crowdsourced odds. In looking at accuracy and payout, the crowdsourced odds-only (Baseline) approach had the highest accuracy versus the eight sentiment models tested. However, in terms of payout, five of the eight sentiment models had higher returns (Subjective Negative \$46.82, Objective Negative \$58.65, Objective Positive \$382.67, All Objective \$816.75 and All Negative \$726.65). The three models with returns less than Baseline were all clustered around Subjective Positive (Subjective Positive − \$1064.50, All Subjective −\$2083.42 and All Positive −\$179.36). Of the three, only All Subjective lost money, −\$195.54. We believe that crowdsourced sentiment was better at identifying longshot wagers as evidenced by five of the sentiment models. For the other three we found the subjective positiveness harmed the results and believe this to be a reaction to events and overconfidence in club performance, rather than rational prescriptive observation transcribed to tweet sentiment.

In looking specifically at the models of All Positive and All Negative sentiments and evaluating the surge/drop of match sentiment versus their club average, we found that this technique led to higher accuracy and payouts for the All Positive model (53.28% accuracy and \$3011.20 payout). Conversely, All Negative showed a marked decline in performance (27.87% accuracy and \$315.17 payout). This result indicates that positive surges (above average club levels) in tweet sentiment generally lead to better match predictability. Tweet authors recognize some factor in their clubs' performance and express it through tweet sentiment. While we expected a similar result with negative sentiment (e.g., recognize something wrong with the club and expect a loss), this was not the case. However, upon a deeper analysis it appears that tweeters from weaker clubs were purposefully injecting negative sentiment into the feeds of their stronger opponents.

Lastly, in examining All Positive and All Negative's wagering behavior against favorites and on longshots, both models exhibited a decrease in accuracy and increase in payouts when wagering on longshots. While the system sacrificed accuracy, it made up for it in payouts. All Negative increased payouts from \$412.00 to \$1627.00 and All Positive increased from \$429.00 to \$1003.00. When compared to the odds-only Baseline, All Negative outperformed Baseline in both payout and betting efficiency (betting efficiency of \$14.71 versus \$14.46 Baseline against the favorites and \$29.58 versus \$16.50 on longshots). All Positive showed a similar gain towards Baseline against the favorites (\$15.32 versus \$15.07) but not on longshots (\$18.57 versus \$22.03). This again was found to be the result of weaker opponents negatively tweeting against their stronger rivals.

There are many potential extensions to this research as the system we created could be ported to other sports domains. One such extension would be the inclusion of Draw categories. While we ignored this category in our study and still managed good results, future work should look into ways of algorithmically identifying Draws with good accuracy. Another extension would be to analyze tweets during a match or briefly thereafter. It might provide some additional insight into tweet author behavior based on goal differences such as more/less interest in matches with more/less goal differentials. A third extension would be to analyze tweets and performance in the first half of the season versus the second half. Sinha et al. discovered season-half differences in the NFL and perhaps similar differences exist in the Premiership. Fourth, an analysis of tweets and retweets may prove interesting in answering the question of what conditions lead to the most retweets? Lastly, it would be interesting to merge sentiment and social network theory to

Please cite this article as: R.P. Schumaker, et al., Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.010

identify the tweeters with the greatest say on setting the sentiment mood for a particular hashtag. It is quite clear that within this domain there are plenty of opportunities for further research.

## References

[1] J. Surowiecki, The Wisdom of Crowds, Doubleday, New York, 2004.

[2] M. Lewis, Moneyball: The Art of Winning an Unfair Game, WW Norton & Company, 2003.

[3] R.P. Schumaker, O.K. Solieman, H. Chen, Sports knowledge management and data mining, Annual Review of Information Science and Technology 44 (1) (2010) 115–157.

[4] M. Gerber, Predicting crime using twitter and kernel density estimation, Decision Support Systems 61 (2014) 115–125.

[5] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, Journal of Computational Science 2 (1) (2011) 1–8.

[6] D. Gayo-Avello, A meta-analysis of state-of-the-art electoral prediction from twitter data, Social Science Computer Review 31 (6) (2013) 649–679.

[7] B. O'Connor, et al., From tweets to polls: linking text sentiment to public opinion time series. The Fourth Annual International AAAI Conference on Weblogs and Social Media. Washington, DC, 2010.

[8] M.J. Paul, M. Dredze, You Are What you Tweet: Analyzing Twitter for Public Health. The Fifth Annual International AAAI Conference on Weblogs and Social Media. Barcelona, Spain, 2011.

[9] H. Rui, Y. Liu, A. Whinston, Whose and what chatter matters? The effect of tweets on movie sales, Decision Support Systems 55 (2013) 863–870.

[10] S. Wise, Testing the effectiveness of semi-predictive markets: are fight fans smarter than expert bookies? Collaborative Innovation Networks Conference. Savannah, GA., 2009.

[11] M. Spann, B. Skiera, Sports forecasting: a comparison of the forecast accuracy of prediction markets, betting odds and tipsters, Journal of Forecasting 28 (1) (2008) 55–72.

[12] S. Luckner, J. Schroder, C. Slamka, On the forecast accuracy of sports prediction markets, in: H. Gimpel, et al., (Eds.), Negotiation, Auctions, and Market Engineering, Springer, Berlin 2008, pp. 227–234

[13] L. Qiu, H. Rui, A. Whinston, A twitter-based prediction market: social network approach, International Conference on Information Systems (ICIS). Shanghai, China, 2011.

[14] A. Tumasjan, et al., Predicting elections with twitter: what 140 characters reveal about political sentiment, The Fourth Annual International AAAI Conference on Weblogs and Social Media, 10 2010, pp. 178–185.

[15] D. Gayo-Avello, Don't turn social media into another literary digest poll, Communications of the ACM 54 (10) (2011) 121–128.

[16] H. Schoen, et al., The power of prediction with social media, Internet Research 23 (5) (2013) 528–543.

[17] R.P. Schumaker, et al., Evaluating sentiment in nancial news articles, Decision Support Systems 53 (3) (2012) 458–464.

[18] J. Wiebe, et al., Learning subjective language, Computational Linguistics 30 (3) (2004) 277–308.

[19] S. Hill, N. Ready-Campbell, Expert stock picker: the wisdom of (experts in) crowds, International Journal of Electronic Commerce 15 (3) (2011) 73–101.

[20] R.P. Schumaker, H. Chen, Textual analysis of stock market prediction using breaking financial news: the AZFinText system, ACM Transactions on Information Systems 27 (2) (2009).

[21] H. Baek, J. Ahn, Y. Choi, Helpfulness of online consumer reviews: readers' objectives and review cues, International Journal of Electronic Commerce 17 (2) (2012) 99–126.

[22] T. Li, G. Berens, M. de Maertelaere, Corporate twitter channels: the impact of engagement and informedness on corporate reputation, International Journal of Electronic Commerce 18 (2) (2013) 97–125.

[23] P. Tetlock, Giving content to investor sentiment: the role of media in the stock market, The Journal of Finance 62 (3) (2007) 1139–1168.

[24] A. Devitt, K. Ahmad, Sentiment Polarity Identification in Financial News: a Cohesion-Based Approach, Prague, Czech Republic, Association of Computational Linguistics, 2007.

[25] S. Das, M. Chen, Yahoo! For Amazon: sentiment extraction from small talk on the web, Management Science 53 (9) (2007) 1375–1388.

[26] A. Davis, J. Piger, L. Sedor, Beyond the numbers: an analysis of optimistic and pessimistic language in earnings press releases, Technical Report, Federal Reserve Bank of St. Louis. 2006.

[27] A. Ghose, P. Ipeirotis, S. Arun, Opinion Mining Using Econometrics: a Case Study on Reputation Systems, Prague, Czech Republic, Association of Computational Linguistics, 2007.

[28] T. Wilson, et al., OpinionFinder: a system for subjectivity analysis, Human Language Technology Conference. Vancouver, Canada, 2005.

[29] E. Riloff, J. Wiebe, Learning extraction patterns for subjective expressions, Conferenc on Empirical Methods in Natural Language Processing. Sapporo, Japan, 2003.

[30] J. Wiebe, E. Riloff, Creating subjective and objective sentence classifiers from unannotated texts, Sixth International Conference on Intelligent Text Processing and Computational Linguistics. Mexico City, Mexico, 2005.

[31] T. Wilson, J. Wiebe, P. Hoffman, Recognizing contextual polarity in phrase-level sentiment analysis, Conference on Human Language Technology and Empirical Methods in Natural Language Processing. Vancouver, Canada, 2005.

[32] Y. Hong, S. Skiena, The wisdom of bookies? Sentiment analysis versus the NFL point spread, The Fourth Annual International AAAI Conference on Weblogs and Social Media. Washington, DC, 2010.

[33] S. Sinha, et al., Predicting the NFL using twitter, ECML/PKDD 2013 Workshop on Machine Learning and Data Mining for Sports Analytics, 2013.

[34] F. Godin, et al., Beating the bookmakers: leveraging statistics and twitter microposts for predicting soccer results. KDD Workshop on Large-Scale Sports Analytics. Sydney, Australia, 2014.

[35] V. Radosavljevic, et al., Large-scale World Cup 2014 outcome prediction based on Tumblr posts, KDD Workshop on Large-Scale Sports Analytics: Sydney, Australia, 2014.

![](/api/attachments/PHTP9H2X/fulltext/images/3b235d23da93055e38cbac87858fa0557192c40d7254d623c7a8c7171a841c7a.jpg)  
Dr. Robert P. Schumaker is an Associate Professor of Computer Science at the University of Texas at Tyler, Associate Editor of Decision Support Systems (DSS) journal and is a speaker through the ACM Distinguished Speakers Program. Dr. Schumaker is an accomplished researcher with over 30 publications and a g-index score of 26; measuring scientific productivity based on published articles and citations. His research deals with business analytics in the areas of textual/financial prediction, sentiment analysis and sport analytics.

![](/api/attachments/PHTP9H2X/fulltext/images/7f429590820d95c43b7b16d4b8c19b57815e9a789b4521c6a3b41b9055d13414.jpg)

Dr. Anrezi Tomasz Jarmoszko is an Associate Professor of Management Information Systems at Central Connecticut State University. His research includes Soviet and East European computing and sports analytics. He has also worked with Poland's Ministry of Post Telecommunications, the Hungarian Oil and Gas Co., and a five-year appointment as manager of strategy and planning at Polkomtel in Warsaw.

![](/api/attachments/PHTP9H2X/fulltext/images/d75f6d475366c242b900efd2b32d2bf6504f9abea8d2c047ddf7da8263e85c61.jpg)

Dr. Chester Labedz Jr. is an Associate Professor of Management and Organization at Central Connecticut State University. Management and Consulting. Chet puts more than twenty years of very diverse assignments to the service of his clients' human resources needs, the systemic analysis and development of their Total People Strategy, and identification and innovative support of their strategic change imperatives.

Please cite this article as: R.P. Schumaker, et al., Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.010
