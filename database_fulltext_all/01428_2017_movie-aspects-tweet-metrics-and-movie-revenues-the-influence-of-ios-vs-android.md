---
otero_id: 1428
otero_key: "P26BYSBU"
title: "Movie aspects, tweet metrics, and movie revenues: The influence of iOS vs. Android"
authors: "David Zimbra; Kumar R. Sarangee; Rupinder P. Jindal"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.08.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Movie aspects, tweet metrics, and movie revenues: The influence of iOS vs. Android

ELSEVIER Decision Support Systems

David Zimbra, Kumar R. Sarangee, Rupinder P. Jindal

![](/api/attachments/P26BYSBU/fulltext/images/c906dbb32a711cf06bb87ccd04e5c99d80029fda4ead0aeed9b24bfd727864eb.jpg)

PII: S0167-9236(17)30145-8

DOI: doi: 10.1016/j.dss.2017.08.002

Reference: DECSUP 12868

To appear in: Decision Support Systems

Received date: 5 December 2016

Revised date: 27 May 2017

Accepted date: 7 August 2017

Please cite this article as: David Zimbra, Kumar R. Sarangee, Rupinder P. Jindal , Movie aspects, tweet metrics, and movie revenues: The influence of iOS vs. Android, Decision Support Systems (2017), doi: 10.1016/j.dss.2017.08.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Movie Aspects, Tweet Metrics, and Movie Revenues: The Influence of iOS vs. Android

David Zimbra\*

Assistant Professor Department of Operations Management and Information Systems Leavey School of Business Santa Clara University 500 El Camino Real Santa Clara, CA 95053 (408) 554-2174 dzimbra@scu.edu

Kumar R. Sarangee

Associate Professor

Department of Marketing

Leavey School of Business

Santa Clara University

500 El Camino Real

Santa Clara, CA 95053

(408) 554-6953

ksarangee@scu.edu

Rupinder P. Jindal

Assistant Professor

Department of Marketing

Milgard School of Business

University of Washington Tacoma

1900 Commerce St.

Tacoma, WA 98402

(253) 692-5885

jindalrp@uw.edu

All authors contributed equally to the article

Movie Aspects, Tweet Metrics, and Movie Revenues: The Influence of iOS vs. Android

## Abstract

Microblogging word of mouth (MWOM) using Twitter has been found to impact the success of experiential products such as movies. However, the influence of the type of device or platform used for tweeting (iOS or Android) on the relationship between well-established tweet metrics – valence, volume, and time period of tweeting – and movie performance is not yet known. Furthermore, it is not known if users of these platforms differ in the aspects of movies they discuss and how that may influence tweet metrics. In this study, we investigated these gaps by analyzing more than four million tweets for 29 movies from both iOS and Android users and conducted a robustness check on another 8 movies. Results from mixed model estimations show that valence of tweets on Android before a movie’s release and volume of tweets on iOS after the release significantly influence the revenues of a movie. Results also show that mentions of director and script are more important in the case of Android users whereas mentions of production and music are more important in the case of iOS users. Finally, results show that it may be more productive for movie studios and advertisers to reach the more prolific Twitter users on Android but relatively newer Twitter use on iOS. These findings have significant implications for movie studios as well as mobile advertisers to target their promotions to these platform users accordingly.

Keywords: Word of mouth (WOM); Twitter; Mobile advertising; iOS vs. Android; Movies.

# ACCEPTED MANUSCRIPT

## 1. Introduction

It has been well documented that word of mouth (WOM), or the process of communicating information from person to person, plays a major role in consumers’ decision-making process (Hennig-Thurau et al., 2012; Godes and Mayzlin, 2004; Jansen et al., 2009). The power of WOM has been further magnified by the use of social media (Kaplan and Haenlein 2010, p.61). Social media are characterized by collaboration and community, and due to their ubiquitous online access keep people connected (Jansen et al. 2009). This has led to the emergence of electronic WOM (eWOM) which can be defined as “any positive or negative sentiment made by potential, actual, or former customers about a product or company, which is made available to a multitude of people and institutions via the Internet” (Hennig-Thurau et al. 2004, p.39).

A novel form of eWOM is microblogging word of mouth (MWOM) using web-based social communication services such as Twitter (Jansen et al., 2009). This is defined as “any brief statement made by a consumer about a commercial entity or offering that is broadcast in real time to some or all members of the sender’s social network through a specific web-based service” (Hennig-Thurau et al. 2015). Although many forms of MWOM exist, Twitter has been the most influential and popular microblogging site with immense impact on its users’ behavior and decision-making process. It has more than 300 million monthly active users and one billion unique monthly visits to sites with embedded tweets (Twitter, 2016). Around 200 million users post 400 million tweets a day (da Silva et al., 2014) making Twitter one of the largest and most dynamic datasets of user generated content.

Recognizing its pervasive adoption, academics have undertaken various research endeavors to better understand the impact of Twitter on consumer behavior. These endeavors have spanned various contexts such as its use by celebrities (Jin and Phua, 2014); for marketing and branding campaigns (Jansen et al., 2009); in politics and sports (Diakopoulos and Shamma, 2010); and other events that generate insecurity (Cheong and Lee, 2011). Another popular context for examining the impact of MWOM is movies (Rui et al., 2013; Liu, 2006; Duan et al., 2008) because WOM has been found to be critical for a movie’s staying power and its ultimate financial success (Elberse and Eliashberg, 2003). These investigations have

# ACCEPTED MANUSCRIPT

typically focused on the impact of important characteristics or metrics of WOM such as its volume (the total number of interactions), valence (that captures the overall nature of messages – positive, negative, or neutral) and the time period (pre- or post-consumption) on movie success. For example, Liu (2006) finds that higher volume of WOM activity about a movie leads to greater awareness of the movie leading to higher sales. Similarly, regarding valence, positive WOM implies a direct or indirect recommendation for product purchase whereas negative WOM indicates “product denigration, rumor and private complaining” (Liu, 2006, p. 76). Finally, time period indicates whether consumers have intentions or plans to purchase a product (pre-consumption) or have attitudes towards a product after experiencing it (post consumption) (Rui at a,2013). In the context of Twitter, volume is the number of total tweets; valence, the net sentiment in the tweets; and time period indicates which tweets were sent before watching a movie and which were sent afterwards. Despite this informative research, several crucial gaps still exist that we highlight below.

First, it is well known that users tweet using many kinds of electronic devices including mobile phones and tablets (da Silva et al., 2014); this has contributed to the spectacular growth of Twitter (McGee, 2012). In fact, 82 percent of Twitter’s active users tweet using mobile phones (Twitter, 2016). This merits further attention because companies can use this information not only to forecast future sales (Rui et al., 2013) but also for mobile advertising, which is a fast growing global business worth 100 billion U.S. dollars and is expected to account for more than half of all digital advertising spending in 2016 (Grewal et al., 2016). However, extant research has not sufficiently examined the conditioning influence of the type of electronic devices (or platforms) used for tweeting on the relationship of tweet metrics (such as volume, valence, and time period) with the success of experiential products such as movies. This is a significant gap because existing research has established differences in characteristics, perceptions, choices, and behaviors between users of different platforms such as iOS and Android (Benenson and Reinfelder, 2013; Benenson et al., 2013; Gronli et al., 2014; Liu et al., 2013; Felt et al., 2011; Chin et al., 2012; Gerpott et al., 2013).

It has also been shown that Twitter users post messages on a wide array of topics, unlike other forms of WOM such as blogs that are specifically tailored to particular topics (da Silva et al., 2014). However,

# ACCEPTED MANUSCRIPT

most studies, especially in the context of movies, have analyzed user posts at an aggregate level by combining and evaluating all tweets pertaining to a particular movie as a single unit (Liu, 2006; Duan et al., 2008; Hennig-Thurau et al., 2015; Rui et al., 2013). The content within the messages has not been utilized perhaps due to the complexity in analyzing multiple themes in a large number of individual messages. This second gap we examine is substantial because “aspect” analysis of Twitter posts can identify topics more frequently mentioned by users of different platforms. In fact, aspect-based analysis is considered one of three important levels of analysis of sentiments due to its finer grained capabilities (Liu, 2012). This can thus help movie producers and mobile advertisers design targeted promotions to customers based on their topical preferences and platforms of usage.

We address these gaps in the context of movies and look specifically at the two most popular platforms, iOS and Android, which comprise more than 79% of all existing devices (Li et al., 2013). First, we categorize tweets from users of these two platforms and analyze the tweets along various wellestablished WOM metrics such as volume, valence, and the time period of tweeting. Then, we examine the impact of these metrics on the daily revenue of movies. We thereby clarify the impact of tweeting platforms and tweet metrics on the usage of experiential new products. Next, we conduct an aspect analysis by uncovering the impact of various aspects or topics regarding a movie (such as actors, director, production, and music) about which the users of iOS and Android are more likely to tweet. This provides vital information for advertisers to devise appropriate mobile promotions which have been found to be an extremely effective communication medium (Goh et al., 2015).

To achieve these objectives, we conducted an empirical study where we used a total of more than four million tweets for 29 movies along with corresponding data obtained from sources such as Box Office Mojo<sup>1</sup> and Internet Movie Database (IMDb)<sup>2</sup>. We estimated mixed models to analyze the data, conducted robustness checks and our results shed light on these research gaps. Thus, our study contributes to various research domains such as WOM, social media, mobile advertising, consumer behavior, and movies.

# ACCEPTED MANUSCRIPT

The rest of the paper is organized as follows. First, we provide a review of relevant literature on twitter, movies, and devices based on which we identified the research gaps. Next, we introduce methods where we discuss data collection, study variables, estimation methods, and empirical results. Finally, we provide conclusions, implications, and limitations of our study and suggest future research directions.

## 2. Related Work

Twitter, launched in 2006, is a computer-mediated communication platform where users post short text-based status updates (a maximum of 140 characters in length) called tweets (Jin and Phua, 2014; da Silva et al., 2014). Tweets are frequently characterized by casual language along with slangs, abbreviations, acronyms, and emoticons and contain hashtags, user references, and embedded links to other websites comprising of additional referenced information (Ghiassi et al., 2013). The default setting for tweets is public which enables people to follow and read one another’s tweets without permission. Moreover, each user has a Twitter page which aggregates all their updates into a single list and displays these tweets on the user’s profile page (Jansen et al., 2009). Also, tweets can be delivered directly to a network of followers through instant messaging, Short Message Service (SMS), email, or other social networking platforms such as Facebook (Jansen et al., 2009). This is because the Twitter application program interface (API) permits the integration of Twitter with other web services and applications. Tweets often contain valuable information related to brand sentiments (Ghiassi et al., 2013) and user opinions on important business and social issues (Gleason, 2013).

Due to Twitter’s popularity, researchers from communication, information technology, media studies, and marketing have tried to understand its influence (Jin and Phua, 2014) using approaches such as sentiment analysis (Ghiassi et al., 2013) and social networking (Cha et al., 2010; Bakshy et al., 2011). Twitter has also been monitored in real time for major events (e.g., Iranian protests of 2009 and Japanese tsunami disaster of 2011), outbreak of news stories, reactions of users to events and indicators of business and society (Phelan et al., 2009; Bifet and Frank, 2010; Mathioudakis and Koudas, 2010; Petrovic et al., 2010; Naveed et al., 2011; Thelwall et al., 2011; Benhardus and Kalita, 2013; Hsieh et al., 2013), to alert/ update the general public in the absence of traditional news media (Grossman, 2009); to predict election outcomes through analysis of candidates’ tweets (O’Connor et al., 2010; Tumasjan et al., 2010; Bermingham and Smeaton, 2011; Chung and Mustafaraj, 2011; Wang et al., 2012; Mejova et al., 2013; Ringsquandl and Petkovic, 2013), and to forecast movements in stock market and other socioeconomic indicators (Bollen et al., 2011; Mittal and Goel, 2012).

Twitter has also gained attention for movies because of its impact on experiential media goods whose distribution strategy merits a hyped launch and whose “instant” success is critical (Hennig-Thurau et al., 2015). Specifically, the relationship between Twitter metrics (volume, valence, and time period) and movie performance is crucial. Asur and Huberman (2010) confirmed the impact of volume of pre-release tweets on opening weekend success, and later showed the impact of valence on the second weekend box office performance. Next, Wong, Sen and Chiang (2012) attempted to relate Twitter valence to total box office revenues taking into account only positive tweets in their analysis. Their results however indicated that tweets do “not necessarily translate into predictable box office” (p. 6) results. Then, a seminal paper by Rui, Liu and Whinston (2013) established significant effects for tweet volume and valence on weekly box office revenue. Specifically, positive tweets were associated with higher movie sales whereas negative tweets were associated with lower movie sales. They also found that the effect of tweets from users with more followers was significantly more influential than tweets from users with less followers, and that pre-consumption WOM had more impact than post-consumption WOM. A more recent study validated the “Twitter effect,” which suggests that MWOM through Twitter impacts product adoption through immediate dissemination of consumers’ post-purchase quality evaluations (Hennig-Thurau et al., 2015). They highlighted a negativity bias and shed more light on the mechanism of influence of Twitter on product adoption of active users, which is based on several idiosyncratic and distinguishing characteristics of MWOM.

However, several critical gaps still remain unresolved. Existing smartphone literature suggests that MWOM such as Twitter is communicated to network participants in real time often from smartphones, tablets, and other mobile devices (Hennig-Thurau et al., 2012; da Silva et al., 2014). Mobile devices are highly individualized and important personal communication tools (Bacile, Ye and Swilley, 2014) that enable ubiquitous access to digital information (Grewal et al., 2016). This real-time communication from various mobile devices combined with a wide network of receivers who access social media sites through such devices catalyzes the expeditious diffusion of Twitter. In fact, researchers posit that Twitter’s growth is strongly associated with the advent of mobile devices, which account for more than 60% of total tweets (McGee 2012). Hence, information related to the use of popular platforms such as iOS and Android and its influence on Twitter and product usage can be extremely useful to companies for both forecasting sales as well as targeting their advertising.

A key question here is why there should be a differential impact of Twitter usage on iOS vs. Android on movie performance. We postulate that this may be due to differences in characteristics, lifestyle choices, motivations, demographics, and behaviors among the users of these platforms which have been established by prior studies. For example, researchers have studied user attitudes and perceptions of issues such as privacy and security towards smart phones and found Android users to be more aware and better informed of risks than iPhone users who seemed to care less about such issues (Benenson and Reinfelder, 2013). Other studies have revealed differences in demographic characteristics across adopters of different platforms (Gerpott et al., 2013). For example, the effects of gender and age were confirmed in a study of iPhone users which showed its users to be younger males. More research has found out that brand-aware users and people interested in technology were more likely to have an iPhone whereas people more concerned about security and privacy related issues were more likely to have an Android phone (Benenson et al., 2013). A recent study revealed differences in smartphone choices of voters in the 2016 presidential election, with voters for Mr. Donald Trump preferring Samsung (which operates on Android) and voters for Mrs. Hillary Clinton preferring Apple (iOS) (Chinni, 2016). These studies highlight differences in the characteristics of users of iOS and Android who can develop their own sub-cultures with a particular vocabulary in this environment (da Silva et al., 2014) and therefore can influence the impact of Twitter on movies.

Researchers also acknowledge that Twitter, because of its simplicity and popularity, encourages its users to post messages on a myriad of topics (Rui et al., 2013). Consequently, tweets can help direct

# ACCEPTED MANUSCRIPT

marketing campaigns by sharing consumers’ opinions on different topics when discussing brands and products (Jansen et al., 2009). Recognizing this trend, academicians have studied how varied the topics of communication were between Starbucks and its users over Twitter (Jansen et al., 2009). This phenomenon of tweets addressing various topics is even more pronounced in the context of movies. For example, Rui et al. (2013) mention that on March 4, 2010, a day after the release of Alice in Wonderland, 15000 tweets were posted discussing different topics about the movie. Similarly, even a few months after the release of the movie Avatar, 13000 tweets were still discussing different topics pe ining to the movie. This enhances the case for conducting aspect analysis of tweets regarding movies to identity differences in topical patterns exhibited by users of iOS and Android.

In summary, we study the following two research questions (RQ) in this paper:

RQ1. What influence does the type of platform (iOS or Android) used for tweeting have on the relationship between tweet metrics and movie performance?

RQ2. Do users of these platforms (iOS or Android) differ in the aspects of movies they discuss and how that may influence tweet metrics?

Next, we describe in detail our empirical approach in answering these questions.

## 3. Data Collection and Characteristics

## 3.1. Data Collection

We collected tweets about newly-released movies from the Twitter streaming API using a customdeveloped system. Our collection centered around 9 movie release weekends, spanning multiple seasons including summer which is the most prolific time for new movie releases. We targeted all movies released on these 9 weekends for collection, provided (a) they were released nationwide throughout the U.S., and (b) this was their first release worldwide. This resulted in an initial list of 84 movies targeted for Twitter data collection. We developed a keyword list for each movie to identify tweets discussing the movie. These keywords consisted of linguistic variations of a movie title to account for various ways a movie may be referred to by Twitter users, including through the use of hashtags. We established strict conditions before considering a movie or a tweet for data collection. Only tweets that were specifically

related to the movie were collected. We ensured this by requiring each tweet to mention a movie title (through the use of one or more of the movie title-based keywords). We established a connection to the Twitter streaming API starting eight days before the release of the movie and kept it open until a week after the release weekend, to capture all available tweets posted during the period of analysis.

Next, we parsed the collected tweets, which entailed separating the various contents of the tweet, message body, user information, and other metadata. Particularly relevant for our study, this metadata contains the specific technology used to send the tweet (labeled as 'source' in the tweet metadata). We used the tweet identifiers in the metadata to remove any duplicate tweets. Tweets of all lengths were considered. To ensure that a sufficient number of tweets about each movie were available for our analysis, we established a data collection requirement. We required that at least 100 tweets per day were collected about a movie on average across the collection period for the movie to be evaluated further. Because only a small sample of all tweets created by Twitter users are available through the Twitter streaming API, 100 tweets per day though should translate into at least a few thousand actual tweets. This reduced the number of movies in our collection to 40. Daily movie revenue information (and values for other control variables) was unavailable for 11 of these, reducing our final collection to 29 movies. These 29 movies and the 9 release weekends are listed in Table 1. We have concealed their identities for privacy reasons.

As shown in Table 1, the movies in our data collection had an average of 139,955 tweets posted about them during the overall period of analysis. Movie 1 had the most tweets, with over 1.7 million, while seven other movies had more than 100,000 tweets each. Movie 29 with about two thousand tweets was the least tweeted movie. Movies 6 and 19 also had relatively low numbers of tweets.

## 3.2.Data Characteristics

## 3.2.1. Period Analysis

To evaluate Twitter activity across various periods of analysis (pre-release, release weekend, and post-release-weekend), we examined the volume of tweets posted in each period. We considered a period starting eight days before the release of the movie as pre-release; the first three days of the movie

## ACCEPTED MANUSCRIPT

Table 1  
Tweet collection and period analysis

<table><tr><td>Movie</td><td>Release Weekend</td><td>Number of total tweets during the collection period</td><td>Average number of daily tweets during pre-release period</td><td>Total pre-release tweets as % of total tweets</td><td>Average number of daily tweets during release weekend</td><td>Total release weekend tweets as % of total tweets</td><td>Average number of daily tweets during post-release-weekend period</td><td>Total post-release-weekend tweets as % of total tweets</td></tr><tr><td>Movie 1</td><td>8/30/2013</td><td>1,758,358</td><td>145,089</td><td>66</td><td>78,190</td><td>13</td><td>51,867</td><td>20</td></tr><tr><td>Movie 2</td><td>8/30/2013</td><td>170,030</td><td>14,819</td><td>69</td><td>10,441</td><td>18</td><td>2,878</td><td>11</td></tr><tr><td>Movie 3</td><td>8/30/2013</td><td>28,272</td><td>1,200</td><td>33</td><td>2,682</td><td>28</td><td>1,517</td><td>37</td></tr><tr><td>Movie 4</td><td>9/6/2013</td><td>218,032</td><td>7,356</td><td>26</td><td>28,714</td><td>39</td><td>10,434</td><td>33</td></tr><tr><td>Movie 5</td><td>9/6/2013</td><td>37,936</td><td>2,232</td><td>47</td><td>3,658</td><td>28</td><td>1,300</td><td>23</td></tr><tr><td>Movie 6</td><td>9/6/2013</td><td>3,897</td><td>190</td><td>39</td><td>505</td><td>38</td><td>123</td><td>22</td></tr><tr><td>Movie 7</td><td>9/13/2013</td><td>153,538</td><td>5,882</td><td>30</td><td>21,210</td><td>41</td><td>6,121</td><td>27</td></tr><tr><td>Movie 8</td><td>9/13/2013</td><td>144,590</td><td>9,549</td><td>52</td><td>4,485</td><td>9</td><td>7,819</td><td>37</td></tr><tr><td>Movie 9</td><td>9/20/2013</td><td>337,326</td><td>8,409</td><td>19</td><td>38,610</td><td>34</td><td>22,031</td><td>45</td></tr><tr><td>Movie 10</td><td>9/20/2013</td><td>53,546</td><td>1,897</td><td>28</td><td>10,897</td><td>61</td><td>810</td><td>10</td></tr><tr><td>Movie 11</td><td>9/20/2013</td><td>29,028</td><td>1,119</td><td>30</td><td>2,009</td><td>20</td><td>2,007</td><td>48</td></tr><tr><td>Movie 12</td><td>9/27/2013</td><td>42,195</td><td>1,464</td><td>27</td><td>5,360</td><td>38</td><td>2,057</td><td>34</td></tr><tr><td>Movie 13</td><td>9/27/2013</td><td>42,615</td><td>1,518</td><td>28</td><td>6,430</td><td>45</td><td>1,596</td><td>26</td></tr><tr><td>Movie 14</td><td>9/27/2013</td><td>66,450</td><td>1,372</td><td>16</td><td>8,540</td><td>38</td><td>4,264</td><td>44</td></tr><tr><td>Movie 15</td><td>3/7/2014</td><td>12,694</td><td>474</td><td>29</td><td>1,815</td><td>42</td><td>493</td><td>27</td></tr><tr><td>Movie 16</td><td>3/7/2014</td><td>26,081</td><td>1,145</td><td>35</td><td>1,433</td><td>16</td><td>1,802</td><td>48</td></tr><tr><td>Movie 17</td><td>3/14/2014</td><td>70,148</td><td>3,331</td><td>37</td><td>8,025</td><td>34</td><td>2,774</td><td>27</td></tr><tr><td>Movie 18</td><td>3/14/2014</td><td>106,990</td><td>3,376</td><td>25</td><td>21,268</td><td>59</td><td>2,310</td><td>15</td></tr><tr><td>Movie 19</td><td>3/14/2014</td><td>4,836</td><td>234</td><td>38</td><td>355</td><td>22</td><td>271</td><td>39</td></tr><tr><td>Movie 20</td><td>3/14/2014</td><td>43,326</td><td>3,679</td><td>67</td><td>3,489</td><td>24</td><td>488</td><td>7</td></tr><tr><td>Movie 21</td><td>5/9/2014</td><td>67,476</td><td>2,088</td><td>24</td><td>9,616</td><td>42</td><td>3,132</td><td>32</td></tr><tr><td>Movie 22</td><td>5/9/2014</td><td>13,128</td><td>567</td><td>34</td><td>864</td><td>19</td><td>857</td><td>45</td></tr><tr><td>Movie 23</td><td>5/9/2014</td><td>18,852</td><td>559</td><td>23</td><td>2,288</td><td>36</td><td>1,073</td><td>39</td></tr><tr><td>Movie 24</td><td>5/9/2014</td><td>23,076</td><td>715</td><td>24</td><td>2,216</td><td>28</td><td>1,529</td><td>46</td></tr><tr><td>Movie 25</td><td>5/9/2014</td><td>23,976</td><td>1,434</td><td>47</td><td>1,620</td><td>20</td><td>1,092</td><td>31</td></tr><tr><td>Movie 26</td><td>7/25/2014</td><td>483,903</td><td>19,139</td><td>31</td><td>55,761</td><td>34</td><td>23,357</td><td>33</td></tr><tr><td>Movie 27</td><td>7/25/2014</td><td>53,946</td><td>2,928</td><td>43</td><td>5,841</td><td>32</td><td>1,856</td><td>24</td></tr><tr><td>Movie 28</td><td>7/25/2014</td><td>22,095</td><td>479</td><td>17</td><td>1,383</td><td>18</td><td>2,016</td><td>63</td></tr><tr><td>Movie 29</td><td>7/25/2014</td><td>2,367</td><td>94</td><td>31</td><td>261</td><td>33</td><td>118</td><td>34</td></tr><tr><td>AVERAGE</td><td></td><td>139,955</td><td>8,356</td><td>47</td><td>11,654</td><td>24</td><td>5,448</td><td>27</td></tr></table>

screening (usually beginning on a Friday) as the release weekend, and up to a week after that as the postrelease-weekend period. The change in traffic from one period to another varies for different movies (Table 1). For several movies, the majority of Twitter discussions occurred in anticipation of their release. Movies 1, 2, and 20 each had more than two-thirds of their tweets posted during the pre-release period. These movies experienced a notable decline in the number of tweets during the release and post-release periods. In contrast, the majority of Twitter discussions about Movies 10 and 18 occurred during the release weekend (59% and 61%, respectively). Six movies had 45% or more of their total tweets in postrelease period, indicating sustained conversation about the movies.

## 3.2.2. Mobile Device User Analysis

Different segments of Twitter users may have distinctive preferences for movies. Moviegoers are traditionally categorized by age, gender, or other demographic information in assessing the potential popularity of a movie and likelihood of consumer purchase. In our research, we specifically examine the users of Android and iOS mobile devices and the views they express about movies on Twitter. The majority of tweets in our data were posted using mobile devices, and Android and iOS devices were by far the most popular. We leveraged the source information parsed from the tweet metadata to limit our analysis to tweets posted using the Twitter apps for the iPhone and iPad (for iOS users), and the Twitter apps for Android-based phones and tablets (for Android users).

The results of the Twitter mobile device user analysis are presented in Table 2. Tweets posted from iOS and Android accounted for, on average, about half of total tweets. Across the movies in our collection, more than twice as many tweets were posted from iOS compared with Android. Several movies had particularly skewed distributions. 58% and 61% of tweets about Movies 8 and 21, respectively, were posted on iOS, three times the number of tweets posted on Android.

## 3.2.3. Sentiment Analysis

To determine whether a tweet expressed positive or negative opinions regarding a movie, we performed sentiment analysis on its text. We utilized the Opinion Finder lexicon of positive and negative words (Wilson et al., 2005) which has been successfully applied in similar research (O'Connor et al.,

2010; Bollen et al., 2011; Chung and Mustafaraj, 2011; Zimbra et al., 2015). We scanned each tweet for occurrences of terms listed in the lexicon, incrementing the sentiment score for each positive word and decrementing the score for each negative word utilized in the tweet. The brief length of tweets limits the range of sentiment scores. Sentiment scores above zero indicate the expression of positive sentiment through the usage of more positive words, while scores below zero indicate the expression of negative sentiment through the usage of more negative words. Scores of zero indicate either equal number of positive and negative words or the expression of no sentiment.

The results of the Twitter sentiment analysis are presented in Table 2. Tweets about the movies in our collection were positive on average, with 0.58 more positive words used per tweet than negative. Several movies received particularly positive sentiment from Twitter users, including Movies 1, 6, and 22, with entiments about Movies 3, 4, 5, 7, and 17, with average sentiment score below 0.2. The average sentiments expressed in tweets from iOS and Android mobile device users were overall similar, with average sentiment scores of 0.65 and 0.63, respectively. However, iOS and Android users expressed distinctive sentiments regarding some movies. For example, iOS users were significantly more positive about Movies 6 and 29 than Android users.

We also examined the sentiments expressed over the three periods of analysis (pre-release, release weekend, and post-release-weekend), and evaluated how Twitter users' sentiments regarding the movies changed over time. We list the average sentiment scores of tweets posted within each period of analysis in Table 3, and compute the change in sentiment scores (sentiment slope) across the periods. Several movies received more positive sentiments during their opening weekend and following their release, including Movies 10, 14, and 21. Each of these movies had sentiment slopes greater than 0.11, indicating that opinions expressed by Twitter users improved over time, and that these movies may have exceeded viewers' pre-release expectations. The release of other movies was not received as well by Twitter users, with sentiment slopes less than 0.10, including Movies 1, 17, and 28. These movies with negative sentiment slopes may not have fulfilled the pre-release expectations of movie viewers, as they did not sustain the positive sentiments of Twitter users once released.

Table 2  
Twitter mobile device user analysis

<table><tr><td rowspan="2">Movie</td><td colspan="4">Volume</td><td colspan="2">Sentiment</td></tr><tr><td>Proportion of total tweets posted on iOS (%)</td><td>Proportion of total tweets posted on Android (%)</td><td>Proportion of total tweets posted on these two platforms (%)</td><td>Sentiment of tweets posted on iOS</td><td>Sentiment of tweets posted on Android</td><td>Overall sentiment of all tweets</td></tr><tr><td>Movie 1</td><td>35</td><td>18</td><td>53</td><td>1.04</td><td>1.00</td><td>0.91</td></tr><tr><td>Movie 2</td><td>29</td><td>13</td><td>42</td><td>0.31</td><td>0.35</td><td>0.37</td></tr><tr><td>Movie 3</td><td>37</td><td>19</td><td>56</td><td>0.19</td><td>0.10</td><td>0.15</td></tr><tr><td>Movie 4</td><td>19</td><td>16</td><td>35</td><td>0.25</td><td>0.18</td><td>0.19</td></tr><tr><td>Movie 5</td><td>19</td><td>7</td><td>26</td><td>0.16</td><td>0.07</td><td>0.15</td></tr><tr><td>Movie 6</td><td>14</td><td>1</td><td>15</td><td>1.00</td><td>0</td><td>1.40</td></tr><tr><td>Movie 7</td><td>39</td><td>17</td><td>56</td><td>0.05</td><td>0.11</td><td>0.08</td></tr><tr><td>Movie 8</td><td>58</td><td>18</td><td>76</td><td>0.24</td><td>0.34</td><td>0.32</td></tr><tr><td>Movie 9</td><td>36</td><td>13</td><td>49</td><td>0.34</td><td>0.26</td><td>0.22</td></tr><tr><td>Movie 10</td><td>40</td><td>19</td><td>59</td><td>0.25</td><td>0.18</td><td>0.21</td></tr><tr><td>Movie 11</td><td>45</td><td>19</td><td>64</td><td>0.31</td><td>0.32</td><td>0.31</td></tr><tr><td>Movie 12</td><td>26</td><td>13</td><td>39</td><td>0.23</td><td>0.18</td><td>0.31</td></tr><tr><td>Movie 13</td><td>28</td><td>17</td><td>45</td><td>0.61</td><td>0.50</td><td>0.71</td></tr><tr><td>Movie 14</td><td>40</td><td>14</td><td>54</td><td>0.64</td><td>0.67</td><td>0.65</td></tr><tr><td>Movie 15</td><td>35</td><td>16</td><td>51</td><td>0.38</td><td>0.18</td><td>0.41</td></tr><tr><td>Movie 16</td><td>17</td><td>7</td><td>26</td><td>0.30</td><td>0.40</td><td>0.37</td></tr><tr><td>Movie 17</td><td>30</td><td>18</td><td>48</td><td>0.37</td><td>0.36</td><td>0.18</td></tr><tr><td>Movie 18</td><td>30</td><td>16</td><td>46</td><td>0.63</td><td>0.36</td><td>0.48</td></tr><tr><td>Movie 19</td><td>37</td><td>14</td><td>51</td><td>0.38</td><td>0.07</td><td>0.26</td></tr><tr><td>Movie 20</td><td>25</td><td>23</td><td>48</td><td>0.65</td><td>0.29</td><td>0.40</td></tr><tr><td>Movie 21</td><td>61</td><td>17</td><td>78</td><td>0.47</td><td>0.50</td><td>0.48</td></tr><tr><td>Movie 22</td><td>39</td><td>13</td><td>52</td><td>0.91</td><td>0.72</td><td>0.82</td></tr><tr><td>Movie 23</td><td>38</td><td>10</td><td>48</td><td>0.84</td><td>0.92</td><td>0.70</td></tr><tr><td>Movie 24</td><td>28</td><td>6</td><td>34</td><td>0.45</td><td>0.46</td><td>0.37</td></tr><tr><td>Movie 25</td><td>19</td><td>11</td><td>30</td><td>0.37</td><td>0.33</td><td>0.52</td></tr><tr><td>Movie 26</td><td>31</td><td>18</td><td>49</td><td>0.36</td><td>0.31</td><td>0.42</td></tr><tr><td>Movie 27</td><td>33</td><td>11</td><td>44</td><td>0.51</td><td>0.51</td><td>0.36</td></tr><tr><td>Movie 28</td><td>46</td><td>28</td><td>74</td><td>0.25</td><td>0.31</td><td>0.27</td></tr><tr><td>Movie 29</td><td>26</td><td>9</td><td>35</td><td>0.91</td><td>0.53</td><td>0.63</td></tr><tr><td>AVERAGE</td><td>34</td><td>16</td><td>50</td><td>0.65</td><td>0.63</td><td>0.58</td></tr></table>

## 3.2.4. Movie Aspect Analysis

The volume of tweets has been shown in prior research to relate to box office performance (Rui et al., 2013). While it is informative to know the degree to which a movie is being discussed by Twitter users, the existing research does not reveal the specific aspects of the movie that prompted these tweets. In this study we performed aspect analysis to determine the specific aspects of the movie discussed in each tweet. Researchers have similarly sought more detailed information on the aspects related to Twitter discussions in other contexts such as brands (Kontopoulos et al., 2013).

Following the categorization used by the Academy Awards (i.e., Oscars), we defined seven aspect

## ACCEPTED MANUSCRIPT

Table 3  
Period-sentiment analysis

<table><tr><td>Movie</td><td>Sentiment of tweets during pre-release period</td><td>Sentiment of tweets during release weekend</td><td>Sentiment of tweets during post-release-weekend period</td><td>Sentiment Slope</td></tr><tr><td>Movie 1</td><td>1.12</td><td>0.72</td><td>0.37</td><td>-0.37</td></tr><tr><td>Movie 2</td><td>0.32</td><td>0.53</td><td>0.39</td><td>0.03</td></tr><tr><td>Movie 3</td><td>0.25</td><td>0.15</td><td>0.06</td><td>-0.09</td></tr><tr><td>Movie 4</td><td>0.21</td><td>0.22</td><td>0.13</td><td>-0.04</td></tr><tr><td>Movie 5</td><td>0.14</td><td>0.12</td><td>0.21</td><td>0.03</td></tr><tr><td>Movie 6</td><td>1.49</td><td>1.35</td><td>1.31</td><td>-0.08</td></tr><tr><td>Movie 7</td><td>0.05</td><td>0.09</td><td>0.09</td><td>0.01</td></tr><tr><td>Movie 8</td><td>0.27</td><td>0.66</td><td>0.32</td><td>0.02</td></tr><tr><td>Movie 9</td><td>0.10</td><td>0.25</td><td>0.25</td><td>0.07</td></tr><tr><td>Movie 10</td><td>0.18</td><td>0.20</td><td>0.40</td><td>0.11</td></tr><tr><td>Movie 11</td><td>0.29</td><td>0.32</td><td>0.33</td><td>0.02</td></tr><tr><td>Movie 12</td><td>0.28</td><td>0.31</td><td>0.33</td><td>0.02</td></tr><tr><td>Movie 13</td><td>0.83</td><td>0.65</td><td>0.68</td><td>-0.07</td></tr><tr><td>Movie 14</td><td>0.43</td><td>0.73</td><td>0.65</td><td>0.11</td></tr><tr><td>Movie 15</td><td>0.42</td><td>0.44</td><td>0.36</td><td>-0.03</td></tr><tr><td>Movie 16</td><td>0.40</td><td>0.45</td><td>0.32</td><td>-0.04</td></tr><tr><td>Movie 17</td><td>0.32</td><td>0.07</td><td>0.11</td><td>-0.10</td></tr><tr><td>Movie 18</td><td>0.44</td><td>0.46</td><td>0.60</td><td>0.07</td></tr><tr><td>Movie 19</td><td>0.40</td><td>-0.14</td><td>0.36</td><td>-0.01</td></tr><tr><td>Movie 20</td><td>0.43</td><td>0.34</td><td>0.38</td><td>-0.02</td></tr><tr><td>Movie 21</td><td>0.28</td><td>0.50</td><td>0.62</td><td>0.16</td></tr><tr><td>Movie 22</td><td>0.70</td><td>0.97</td><td>0.84</td><td>0.07</td></tr><tr><td>Movie 23</td><td>0.59</td><td>0.90</td><td>0.58</td><td>-0.01</td></tr><tr><td>Movie 24</td><td>0.32</td><td>0.53</td><td>0.30</td><td>-0.01</td></tr><tr><td>Movie 25</td><td>0.43</td><td>0.60</td><td>0.61</td><td>0.08</td></tr><tr><td>Movie 26</td><td>0.31</td><td>0.63</td><td>0.31</td><td>-0.01</td></tr><tr><td>Movie 27</td><td>0.35</td><td>0.26</td><td>0.5</td><td>0.07</td></tr><tr><td>Movie 28</td><td>0.48</td><td>0.58</td><td>0.13</td><td>-0.17</td></tr><tr><td>Movie 29</td><td>0.55</td><td>0.74</td><td>0.59</td><td>0.01</td></tr><tr><td>AVERAGE</td><td>0.42</td><td>0.47</td><td>0.41</td><td>-0.01</td></tr></table>

Note: Sentiment slope is the average change in sentiment from pre-release period to post-release-weekend period.

categories of a movie that a tweet may refer to: acting, directing, production, cinematography and special effects, writing and script, music and soundtrack, and the movie premiere and pre-release promotional activities. To perform aspect analysis, we defined comprehensive lists of terms that may be used in tweets to refer to these movie aspects. For each aspect category, we first developed a list of general terms describing the category. To supplement these general terms, we then developed lists of movie-specific terms for each movie which included the names and Twitter handles of the actors featured in a movie, the directors, and the production studios responsible for movie creation, production, and distribution. Once these aspect lexicons were developed, we scanned each tweet for usage of terms describing each movie aspect – if a term was mentioned, the tweet was considered as discussing that aspect category. If more

than one aspect category was mentioned in a single tweet, that tweet was counted towards all those categories. We examined the volume and sentiment of tweets in which the movie aspects were mentioned.

Four of the seven movie aspect categories prompted more Twitter discussion than the other three, so we present the percentages of tweets that discussed these aspects – acting, directing, music and the soundtrack, and movie premiere – and the associated sentiment scores in Table 4. Popular actors in several movies prompted much discussion from Twitter users. Movies 14, 19, 21, 22, 25, and 28 each had over 30% of tweets mentioning the actors in the movie. Movies 3, 14, 19, and 22 had relatively large percentages of tweets discussing the directing aspects too. They featured actor-directors and tweets that mentioned them contributed to both acting and directing aspect categories. Twitter users expressed particularly positive sentiments about the actors in Movies 5, 6, 8, and 11, each with average sentiment score over 1.0 among tweets discussing the acting aspect. Movies 21 and 28 scored particularly high on positive sentiment for their directors. There were many positive tweets about the music and soundtrack of Movie 1. Movie 12 had the highest percentage of tweets (13%) mentioning its music and soundtrack although the sentiments expressed by Twitter users about it were fairly neutral. A large volume of tweets associated with the premiere and pre-release promotional activities may indicate active marketing campaigns in anticipation of movie release. Movies 2, 20, and 25 each had more than 10% of their tweets discussing this aspect category. These tweets expressed fairly neutral sentiments overall, which may indicate informative pre-release announcements. Other movies such as Movies 6, 8, 17, and 18 had tweets discussing their premiere more positively than the movie’s overall sentiment. These results may indicate the expression of positive opinions by Twitter users in anticipation of movie’s release, which ultimately failed to fulfill their heightened expectations.

Our analysis also revealed the movie aspects frequently discussed by specific mobile device users. Across all movies in our collection, a higher proportion of the tweets from iOS users discussed the acting and directing aspects compared to Android users, while tweets from Android users were more likely to discuss the music and soundtrack and movie premiere aspects. For example, 41% of the tweets from iOS users on Movie 19 mentioned the acting aspect, compared to 15% of the tweets from Android users. 10% of the tweets from iOS users on Movie 18 discussed the directing aspect, compared to 5% of the Android user tweets. A higher proportion of the tweets from Android users mentioned the music and soundtrack aspect of Movie 12 (21%) than the tweets from iOS users (15%). 20% of the tweets from Android users on Movie 20 discussed the movie premiere aspect, compared to 7% of the tweets from iOS users.

Table 4  
Movie aspect analysis for select aspect categories

<table><tr><td rowspan="2">Movie</td><td colspan="2">Acting</td><td colspan="2">Directing</td><td colspan="2">Music</td><td colspan="2">Premiere</td></tr><tr><td>% of total tweets</td><td>Average sentiment</td><td>% of total tweets</td><td>Average sentiment</td><td>% of total tweets</td><td>Average sentiment</td><td>% of total tweets</td><td>Average sentiment</td></tr><tr><td>Movie 1</td><td>18</td><td>0.91</td><td>1</td><td>0.47</td><td>7</td><td>1.53</td><td>1</td><td>0.80</td></tr><tr><td>Movie 2</td><td>26</td><td>0.71</td><td>1</td><td>0.06</td><td>1</td><td>0.39</td><td>12</td><td>0.11</td></tr><tr><td>Movie 3</td><td>24</td><td>-0.22</td><td>60</td><td>0.18</td><td>1</td><td>0.5</td><td>2</td><td>0.11</td></tr><tr><td>Movie 4</td><td>5</td><td>0.67</td><td>1</td><td>0.15</td><td>1</td><td>0.77</td><td>2</td><td>0.26</td></tr><tr><td>Movie 5</td><td>1</td><td>1.15</td><td>1</td><td>0.38</td><td>1</td><td>-0.05</td><td>8</td><td>0.12</td></tr><tr><td>Movie 6</td><td>3</td><td>1.24</td><td>1</td><td>0</td><td>0</td><td>0</td><td>5</td><td>1.48</td></tr><tr><td>Movie 7</td><td>1</td><td>0.91</td><td>1</td><td>0.39</td><td>1</td><td>0.19</td><td>2</td><td>-0.24</td></tr><tr><td>Movie 8</td><td>10</td><td>1.10</td><td>1</td><td>0.48</td><td>1</td><td>0.34</td><td>1</td><td>1.16</td></tr><tr><td>Movie 9</td><td>6</td><td>0.68</td><td>1</td><td>0.46</td><td>1</td><td>0.05</td><td>3</td><td>0.37</td></tr><tr><td>Movie 10</td><td>6</td><td>0.58</td><td>1</td><td>0.13</td><td>1</td><td>0.26</td><td>1</td><td>0.17</td></tr><tr><td>Movie 11</td><td>2</td><td>1.09</td><td>1</td><td>2</td><td>1</td><td>0.51</td><td>1</td><td>1</td></tr><tr><td>Movie 12</td><td>1</td><td>0.76</td><td>0</td><td>0</td><td>13</td><td>0.09</td><td>4</td><td>0.05</td></tr><tr><td>Movie 13</td><td>10</td><td>0.80</td><td>4</td><td>1</td><td>1</td><td>0.71</td><td>2</td><td>0.5</td></tr><tr><td>Movie 14</td><td>31</td><td>0.88</td><td>30</td><td>0.87</td><td>1</td><td>0.87</td><td>1</td><td>0.59</td></tr><tr><td>Movie 15</td><td>3</td><td>0.53</td><td>1</td><td>0.31</td><td>1</td><td>0.8</td><td>3</td><td>0.46</td></tr><tr><td>Movie 16</td><td>1</td><td>0.71</td><td>1</td><td>0.87</td><td>1</td><td>0.09</td><td>2</td><td>0.53</td></tr><tr><td>Movie 17</td><td>27</td><td>0.40</td><td>1</td><td>0.66</td><td>1</td><td>1.18</td><td>5</td><td>0.73</td></tr><tr><td>Movie 18</td><td>20</td><td>0.71</td><td>6</td><td>0.97</td><td>1</td><td>1.11</td><td>5</td><td>0.87</td></tr><tr><td>Movie 19</td><td>32</td><td>0.77</td><td>30</td><td>0.69</td><td>0</td><td>0</td><td>2</td><td>1</td></tr><tr><td>Movie 20</td><td>8</td><td>0.76</td><td>19</td><td>0.32</td><td>4</td><td>0.5</td><td>17</td><td>0.16</td></tr><tr><td>Movie 21</td><td>30</td><td>0.62</td><td>2</td><td>1.14</td><td>1</td><td>0.47</td><td>1</td><td>0.89</td></tr><tr><td>Movie 22</td><td>45</td><td>0.78</td><td>43</td><td>0.76</td><td>4</td><td>0.81</td><td>3</td><td>0.46</td></tr><tr><td>Movie 23</td><td>26</td><td>0.96</td><td>2</td><td>0.94</td><td>1</td><td>0.94</td><td>3</td><td>0.80</td></tr><tr><td>Movie 24</td><td>4</td><td>0.27</td><td>4</td><td>0.48</td><td>1</td><td>1</td><td>5</td><td>0.44</td></tr><tr><td>Movie 25</td><td>35</td><td>0.37</td><td>1</td><td>4</td><td>3</td><td>0.83</td><td>17</td><td>0.15</td></tr><tr><td>Movie 26</td><td>14</td><td>0.64</td><td>1</td><td>0.26</td><td>1</td><td>0.72</td><td>3</td><td>0.35</td></tr><tr><td>Movie 27</td><td>3</td><td>0.82</td><td>1</td><td>0.25</td><td>1</td><td>0.68</td><td>1</td><td>0</td></tr><tr><td>Movie 28</td><td>86</td><td>0.24</td><td>1</td><td>1.33</td><td>1</td><td>0.37</td><td>1</td><td>0.63</td></tr><tr><td>Movie 29</td><td>26</td><td>0.92</td><td>6</td><td>0.64</td><td>1</td><td>4</td><td>8</td><td>0.31</td></tr><tr><td>AVERAGE</td><td>15</td><td>0.78</td><td>2</td><td>0.55</td><td>3</td><td>1.35</td><td>2</td><td>0.40</td></tr></table>

## 3.3. Model Variables

The variables used in model specification include movie revenues, volume and valence of tweets, proportion of tweets about each of the seven aspect categories, some relevant and established characteristics of each movie, and some aggregate characteristics of Twitter users.

Daily revenue of each movie is the daily gross collection (in millions of dollars) from all the theaters in the US where the movie is playing. Daily volume of tweets for each movie on each platform is the number of tweets about that movie sent from that platform each day. Total volume of pre-release tweets for each movie on each platform is the sum of all tweets for each movie on each platform in the prerelease period (starting eight days before the release of the movie).

Daily valence of tweets for each movie on each platform is calculated as follows: (a) first, we find the daily average of sentiment score for each movie on each platform (which is the net of difference between positive and negative words), (b) second, we add the number of negative and positive words in each tweet and find the daily average for each movie on each platform, and then (c) we divide the number in step (a) by the number in step (b). For example, if the average number of positive words in all tweets about a movie on iOS on a particular day was three while the average number of negative words was one then the valence would be 0.5 (i.e., (3–1) divided by (3+1)). A user who focuses on positive outcome tendencies does not necessarily ignore negative ones and vice versa; users tend to exhibit a relative preference for encoding potential outcomes with either a positive or a negative focus (Nenkov, Inman, and Hulland 2008). Thus, we combined the positive and negative outcome focus dimensions to create this relative valence construct.<sup>4</sup> Average valence of pre-release tweets on a platform is an arithmetic average of daily valence in the pre-release period.

Proportion of tweets about each aspect category of a movie on a particular platform was obtained by dividing the number of tweets about the focal aspect category for that movie on the focal platform by the total number of tweets about the focal aspect category for that movie every day. For example, if a movie had 2,000 total tweets about the director on a particular day and 500 of those tweets were on iOS then the proportion of tweets about the director for that movie on iOS for that day is 0.25.

We controlled for several movie characteristics that could arguably influence the volume and valence of tweets and the revenue a movie generates. Production budget (in million dollars) captures the total amount of money spent in producing the movie. Number of theaters is the total number of screens showing the movie each day. Both these variables also serve as a proxy for the promotional budget of the

# ACCEPTED MANUSCRIPT

movie because a movie produced with a big budget and showing in a larger number of theaters is likely to spend more on advertising and promotion. Competition captures the number of other movies released in the same weekend. Featured in IMDb is a binary variable that captures if the movie was featured in Internet Movie Database (IMDb), a website very popular with moviegoers. Star power is a binary variable that denotes whether the movie had famous stars playing a lead role. Average user grade is the movie rating on a scale of 1 to 10 as rated by the moviegoers. We collected data over multiple seasons to explore seasonal differences. Two binary variables denote if a movie was released in summer or spring – winter was considered the reference season.

Among Twitter user characteristics, user experience captures the number of years a user has been tweeting. Total tweets refer to each user’s total number of tweets during their entire membership of Twitter. Number of followers refers to each user’s followers on Twitter while the number of friends refers to each user’s friends on Twitter. For model estimation, averages of each of these four variables were calculated at relevant levels. Table 5 lists the descriptive statistics of all the variables.

Three movie characteristics were specified as random effects – genre, MPAA rating, and movie studio size. Each movie was categorized as belonging to one of the nine genres – action/adventure, science fiction, comedy, war, animation, mystery/thriller, documentary, drama, or 3-dimensional. Also, each movie was categorized as per Motion Picture Association of America’s (MPAA) rating. All movies in our dataset belong to one of the three categories – PG, PG-13, and R. To account for any potential influence of production studio’s resources we ranked studios into three categories – mini, intermediate, and major.

## 4. Results and Discussion

## 4.1. Models

We followed a two-stage estimation procedure. In the first stage, we studied the influence of tweets volume and valence from each platform on the daily revenue. In the second stage we studied potential antecedents of tweets’ daily volume and valence on each platform. Because we have data for each movie over multiple days we specified mixed models at each stage to account for any intra-movie correlations (Stroup 2013). The general notation for each mixed model in the study is:

Table 5  
Descriptive statistics

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>Daily revenue (in millions of dollars)a</td><td>281</td><td>2.62</td><td>3.79</td><td>0.01</td><td>20.23</td></tr><tr><td>Number of theatersa</td><td>504</td><td>1091.17</td><td>1427.92</td><td>0</td><td>4001</td></tr><tr><td>Competitiona</td><td>504</td><td>16.19</td><td>4.81</td><td>10</td><td>28</td></tr><tr><td>Production budget (millions)a,b</td><td>504</td><td>30.65</td><td>36.91</td><td>1</td><td>145</td></tr><tr><td>Star power (binary variable)b</td><td>504</td><td></td><td></td><td>0</td><td>1</td></tr><tr><td>Average user gradeb</td><td>504</td><td>6.35</td><td>0.97</td><td>4</td><td>8.10</td></tr><tr><td>Featured in IMDb (binary variable)b</td><td>504</td><td></td><td></td><td>0</td><td>1</td></tr><tr><td>Released in summer (binary variable)a</td><td>504</td><td></td><td></td><td>0</td><td>1</td></tr><tr><td>Released in spring (binary variable)a</td><td>504</td><td></td><td></td><td>0</td><td>1</td></tr><tr><td colspan="6">iOS</td></tr><tr><td>Total volume of pre-release tweets (000s)</td><td>86</td><td>24.96</td><td>82.65</td><td>0.08</td><td>451.50</td></tr><tr><td>Daily volume of tweets after release (000s)</td><td>273</td><td>2.55</td><td>5.01</td><td>11</td><td>36.20</td></tr><tr><td>Average valence of pre-release tweets</td><td>86</td><td>0.52</td><td>0.29</td><td>-0.01</td><td>1</td></tr><tr><td>Daily valence of tweets after release</td><td>267</td><td>0.45</td><td>0.30</td><td>-1</td><td>1</td></tr><tr><td>Proportion of tweets about actor(s)</td><td>504</td><td>0.25</td><td>0.24</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about director</td><td>504</td><td>0.19</td><td>0.27</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about production</td><td>504</td><td>0.08</td><td>0.22</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about cinematography</td><td>504</td><td>0.10</td><td>0.22</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about script</td><td>504</td><td>0.14</td><td>0.27</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about music</td><td>504</td><td>0.13</td><td>0.24</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about premiere</td><td>503</td><td>0.17</td><td>0.25</td><td>0</td><td>1</td></tr><tr><td>User – experience (years)</td><td>504</td><td>4.38</td><td>1.37</td><td>0</td><td>7.51</td></tr><tr><td>User – total tweets (000s)</td><td>504</td><td>10.50</td><td>7.63</td><td>0</td><td>77.52</td></tr><tr><td>User – number of followers (millions)</td><td>504</td><td>0.06</td><td>0.29</td><td>0</td><td>4.38</td></tr><tr><td>User – number of friends (millions)</td><td>504</td><td>0.01</td><td>0.08</td><td>0</td><td>0.17</td></tr><tr><td colspan="6">Android</td></tr><tr><td>Total volume of pre-release tweets (000s)</td><td>83</td><td>12.49</td><td>40.58</td><td>0.09</td><td>217.85</td></tr><tr><td>Daily volume of tweets after release (000s)</td><td>266</td><td>1.29</td><td>2.70</td><td>9</td><td>18.24</td></tr><tr><td>Average valence of pre-release tweets</td><td>83</td><td>0.46</td><td>0.26</td><td>0.04</td><td>1</td></tr><tr><td>Daily valence of tweets after release</td><td>257</td><td>0.45</td><td>0.42</td><td>-1</td><td>1</td></tr><tr><td>Proportion of tweets about actor(s)</td><td>504</td><td>0.12</td><td>0.15</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about director</td><td>504</td><td>0.07</td><td>0.14</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about production</td><td>504</td><td>0.03</td><td>0.12</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about cinematography</td><td>504</td><td>0.08</td><td>0.20</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about script</td><td>504</td><td>0.06</td><td>0.16</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about music</td><td>504</td><td>0.07</td><td>0.17</td><td>0</td><td>1</td></tr><tr><td>Proportion of tweets about premiere</td><td>502</td><td>0.09</td><td>0.19</td><td>0</td><td>1</td></tr><tr><td>User – experience (years)</td><td>504</td><td>3.86</td><td>1.56</td><td>0</td><td>8.16</td></tr><tr><td>User – total tweets (000s)</td><td>504</td><td>9.49</td><td>9.32</td><td>0</td><td>75.9</td></tr><tr><td>User – number of followers (millions)</td><td>504</td><td>0.05</td><td>0.06</td><td>0</td><td>1.36</td></tr><tr><td>User – number of friends (millions)</td><td>504</td><td>&lt;0.01</td><td>0.01</td><td>0</td><td>0.02</td></tr></table>

Notes: <sup>a</sup>Data collected from boxofficemojo.com; <sup>b</sup>data collected from imdb.com; all other data from tweets.

$$
\mathbf {y} = \mathbf {X} \boldsymbol {\beta} + \mathbf {Z} \gamma + \varepsilon\tag{1}
$$

where y is (n × 1) vector of the response variable, X is an $\left( \mathtt { n } \times \mathtt { p } \right)$ matrix of independent variables, β is a

(p × 1) parameter vector of fixed-effects, Z is an (n × r) design matrix for random effects,  is an (r × 1)

parameter vector of random effects normally distributed with mean 0 and variance G, and is (n × 1) random error vector normally distributed with mean 0 and variance R.

We modeled the variance of y $\mathbf { ( } \mathbf { V } = \mathbf { Z } \mathbf { G } \mathbf { Z } ^ { \prime } + \mathbf { R } )$ by setting up the random effects design matrix Z and by specifying covariance structures for G and R. In both stages, we specified the movie’s genre, its MPAA rating, and movie studio size as random effects and a variance-components covariance structure for both G and R (Stroup 2013). We used restricted maximum-likelihood to construct an objective function and maximized it over all unknown parameters (SAS 2013; Stroup 2013). The corresponding log-likelihood function is:

$$
l _ {\mathrm{R}} (\mathbf {G}, \mathbf {R}) = - \left(\frac {\mathrm{n} - \mathrm{p}}{2}\right) \log (2 \pi) - \frac {1}{2} \log | \mathbf {V} | - \frac {1}{2} \log \left| \mathbf {X} ^ {\prime} \mathbf {V} ^ {- 1} \mathbf {X} \right| - \frac {1}{2} \mathbf {r} ^ {\prime} \mathbf {V} ^ {- 1} \mathbf {r}\tag{2}
$$

where p = rank(X) and $\mathbf { r } = \mathbf { y } - \mathbf { X } ( \mathbf { X } ^ { \prime } \mathbf { V } ^ { - 1 } \mathbf { X } ) ^ { - } \mathbf { X } ^ { \prime } \mathbf { V } ^ { - 1 } \mathbf { y }$

We minimized this function using a ridge-stabilized Newton-Raphson algorithm. The estimation ran computation of $\widehat { \pmb { \beta } }$ and ${ \widehat { \gamma } } .$ These were used to determine new values of the score vector and the Hessian matrix and update the variance-covariance matrix. At convergence, parameters and random effects were estimated as

$$
\widehat {\boldsymbol {\beta}} = \left(\mathbf {X} ^ {\prime} \widehat {\mathbf {V}} ^ {- 1} \mathbf {X}\right) ^ {-} \mathbf {X} ^ {\prime} \widehat {\mathbf {V}} ^ {- 1} \mathbf {y}\tag{3}
$$

$$
\widehat {\boldsymbol {\gamma}} = \widehat {\mathbf {G}} \mathbf {Z} ^ {\prime} \widehat {\mathbf {V}} ^ {- 1} (\mathbf {y} - \mathbf {X} \widehat {\boldsymbol {\beta}})\tag{4}
$$

## 4.2. Estimation and Results of Stage 1 (Revenue) model

Dependent variable is the log transform of daily revenue. Key independent variables include the total volume and average valence of tweets originating on iOS and Android platforms in pre-release period as well as one-period lagged values of daily volume and daily valence of tweets on both the platforms during the release weekend and post-release-weekend. All these variables were grand-mean-centered. Other independent variables include the number of theaters, competition, production budget, star power, average user grade, and featured in IMDb. We also controlled for the season. We built the model incrementally and used Bayesian information criteria (BIC) to evaluate incremental nested models

# ACCEPTED MANUSCRIPT

(Stroup 2013). The results for the final model appear in Table 7.

We started with an intercept-only model. Next, we included random intercept effects to account for potential variation because of movie genre, MPAA rating, or studio size. The comparison of these two nested models indicates improvement in the model fit $( \Delta \mathrm { B I C } _ { ( 3 ) } = 8 2 , \mathrm { p } < 0 . 0 1 )$ ). Empirical best linear unbiased predictors (BLUP) for random effects indicate that action/adventure, science-fiction, and war movies have higher daily revenue while documentaries and dramas have lower daily revenue (see Table 6). Movies made by major studios also generate higher daily revenue. Next, we added all but our key independent variables to obtain model 1a (see Table 7). The comparison of these two nested models indicates significant improvement in model fit $( \Delta \mathrm { B I C } _ { ( 8 ) } = 2 5 0 , \mathrm { p } < 0 . 0 1 )$ . Finally, we added our key independent variables to obtain full model, model 1b. The comparison of these two nested models again indicates significant improvement in model fit $( \Delta \mathrm { B I C } _ { ( 8 ) } = 2 6 , \mathrm { p } < 0 . 0 1 )$

Results of the full model 1b show that average valence of pre-release tweets on Android have a

## Table 6

Results from random intercepts in all three mixed models

<table><tr><td rowspan="2">Effect</td><td colspan="3">Dependent variable</td></tr><tr><td>Daily revenue</td><td>Daily valence of pre-release Android tweets</td><td>Daily volume of iOS tweets after release</td></tr><tr><td> $Studio size^a$ </td><td></td><td></td><td></td></tr><tr><td>Mini</td><td></td><td></td><td></td></tr><tr><td>Intermediate</td><td></td><td></td><td>-*</td></tr><tr><td>Major</td><td>+*</td><td></td><td>+*</td></tr><tr><td> $Movie Genre^b$ </td><td></td><td></td><td></td></tr><tr><td>Action / Adventure</td><td>+**</td><td></td><td>+**</td></tr><tr><td>Science fiction</td><td>+*</td><td></td><td>-*</td></tr><tr><td>Comedy</td><td></td><td></td><td></td></tr><tr><td>War</td><td>+**</td><td></td><td>-**</td></tr><tr><td>Animation</td><td></td><td></td><td></td></tr><tr><td>Mystery / Thriller</td><td></td><td></td><td>+*</td></tr><tr><td>Documentary</td><td>-***</td><td>+***</td><td>+***</td></tr><tr><td>Drama</td><td>-***</td><td></td><td></td></tr><tr><td>3D</td><td></td><td></td><td></td></tr><tr><td> $MPAA rating^b$ </td><td></td><td></td><td></td></tr><tr><td>PG</td><td></td><td></td><td></td></tr><tr><td>PG 13</td><td></td><td></td><td>-*</td></tr><tr><td>R</td><td></td><td></td><td></td></tr></table>

\*p<0.10; \*\*p<0.05; \*\*\*p<0.01.  
Notes: <sup>a</sup>Data collected from boxofficemojo.com; <sup>b</sup>data collected from imdb.com.  
+ indicates positive association with dependent variable; − indicates negative association with dependent variable.

Table 7  
Results from mixed model for daily revenue (Model 1)

<table><tr><td rowspan="2">Variable</td><td colspan="2">Model 1a</td><td colspan="2">Model 1b</td></tr><tr><td>Estimate</td><td>SE</td><td>Estimate</td><td>SE</td></tr><tr><td>iOS</td><td></td><td></td><td></td><td></td></tr><tr><td>Pre-release tweets</td><td></td><td></td><td></td><td></td></tr><tr><td>Total volume of pre-release iOS tweets</td><td></td><td></td><td>-0.005</td><td>0.003</td></tr><tr><td>Average valence of pre-release iOS tweets</td><td></td><td></td><td>0.729</td><td>0.443</td></tr><tr><td>Tweets after release</td><td></td><td></td><td></td><td></td></tr><tr><td>Lagged daily volume of iOS tweets after release</td><td></td><td></td><td>0.077***</td><td>0.023</td></tr><tr><td>Lagged valence of daily iOS tweets after release</td><td></td><td></td><td>-0.031</td><td>0.338</td></tr><tr><td>Android</td><td></td><td></td><td></td><td></td></tr><tr><td>Pre-release tweets</td><td></td><td></td><td></td><td></td></tr><tr><td>Total volume of pre-release Android tweets</td><td></td><td></td><td>-0.030</td><td>0.039</td></tr><tr><td>Average valence of pre-release Android tweets</td><td></td><td></td><td>2.174**</td><td>1.030</td></tr><tr><td>Tweets after release</td><td></td><td></td><td></td><td></td></tr><tr><td>Lagged daily volume of Android tweets after release</td><td></td><td></td><td>-0.011</td><td>0.080</td></tr><tr><td>Lagged valence of daily Android tweets after release</td><td></td><td></td><td>-0.231</td><td>0.198</td></tr><tr><td>Covariates</td><td></td><td></td><td></td><td></td></tr><tr><td>Number of theaters playing the movie</td><td>0.001***</td><td>&lt;0.001</td><td>0.001***</td><td>&lt;0.001</td></tr><tr><td>Competition</td><td>0.017</td><td>0.019</td><td>0.019</td><td>0.021</td></tr><tr><td>Production budget</td><td>-0.004</td><td>0.004</td><td>-0.006</td><td>0.004</td></tr><tr><td>Star power</td><td>0.435**</td><td>0.232</td><td>0.560**</td><td>0.264</td></tr><tr><td>Average user rating</td><td>0.184**</td><td>0.087</td><td>0.249**</td><td>0.110</td></tr><tr><td>Featured in IMDb</td><td>-0.225</td><td>0.281</td><td>0.056</td><td>0.350</td></tr><tr><td>Movie released in summer</td><td>1.643***</td><td>0.267</td><td>1.702***</td><td>0.317</td></tr><tr><td>Movie released in spring</td><td>0.784***</td><td>0.227</td><td>0.835***</td><td>0.244</td></tr><tr><td>Intercept</td><td>-4.112**</td><td>0.686</td><td>-4.493**</td><td>0.898</td></tr><tr><td>BIC</td><td>856</td><td></td><td>830</td><td></td></tr><tr><td>ΔBIC</td><td></td><td></td><td>26***</td><td></td></tr></table>

\*p<0.10; \*\*p<0.05; \*\*\*p<0.01.

positive and negative words in tweets to the sum of positive and negative words. Thus, both the number of positive and negative words in each tweet as well as the difference between them affects the revenue. For example, if the average number of both positive and negative words in all pre-release tweets on Android is three, an increase of one positive word is associated with almost 36% increase in daily revenue during the first ten days of movie screening. Results also show that daily volume of tweets on iOS after movie’s release has a significant positive association with next day’s revenue. An increase of one unit (i.e., one thousand tweets) in daily tweets on iOS is associated with almost 8 percent increase in revenue next day during the first ten days of release.

Other factors having a positive association with daily revenue during the first ten days include the number of theaters (an additional theater is associated with about 1.4% increase in revenue), star power (an increase of 75% in revenue over a movie without star power), and average user grade (one unit increase is associated with about 28% increase in revenue). Also, movies released in summer make about four times more daily revenue while movies released in spring make more than twice as much daily revenue compared with movies released in winter.

## 4.3. Estimation and Results of Stage 2 models

Based on the results of stage 1 model, we specify two models in stage 2. The first model explains the daily valence of tweets on Android in pre-release period while the second model explains the daily volume of tweets on iOS after the movie’s release.<sup>5</sup>

## 4.3.1. Android Valence model

Dependent variable is the daily valence of tweets on Android during the pre-release period. Valence is a proportion measure and we need to take its logit transform before it can be employed as a dependent variable. Furthermore, daily valence varies in value from −1 to +1, i.e., for some movies daily valence was negative on some days. Because only positive values are suitable for logit transformation, we estimated a model only for positive daily valence values.<sup>6</sup> Key independent variables include the proportions of tweets on Android about each of the seven aspects – actors, director, production, cinematography, script, music, and premiere. Other independent variables include user experience, total tweets, number of followers, number of friends, production budget, and star power. We built this model incrementally too and used BIC to evaluate incremental nested models (Stroup 2013). The results for final model for valence appear in Table 8.

Similar to stage 1, we started with an intercept-only model. Next, we included random intercept effects to account for potential variation in valence because of movie genre, MPAA rating, or studio size.

Results from mixed models for (a) daily valence of pre-release tweets on Android (Model 2), and (b) daily volume of tweets on iOS after movie’s release (Model 3)

<table><tr><td rowspan="3">Variable</td><td colspan="4">Daily valence of pre-releasetweets on Android</td><td colspan="4">Daily volume of tweetson iOS after movie&#x27;s release</td></tr><tr><td colspan="2">Model 2a</td><td colspan="2">Model 2b</td><td colspan="2">Model 3a</td><td colspan="2">Model 3b</td></tr><tr><td>Estimate</td><td>SE</td><td>Estimate</td><td>SE</td><td>Estimate</td><td>SE</td><td>Estimate</td><td>SE</td></tr><tr><td>Tweet characteristics –Proportion of tweetson the platform about:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Actors</td><td></td><td></td><td>0.06</td><td>0.83</td><td></td><td></td><td>1760</td><td>1138</td></tr><tr><td>Director</td><td></td><td></td><td>1.71***</td><td>0.65</td><td></td><td></td><td>-995</td><td>840</td></tr><tr><td>Production</td><td></td><td></td><td>0.65</td><td>0.64</td><td></td><td></td><td>2233**</td><td>1042</td></tr><tr><td>Cinematography</td><td></td><td></td><td>-0.98**</td><td>0.44</td><td></td><td></td><td>724</td><td>1220</td></tr><tr><td>Script</td><td></td><td></td><td>1.59**</td><td>0.78</td><td></td><td></td><td>1244</td><td>867</td></tr><tr><td>Music</td><td></td><td></td><td>-0.70</td><td>0.64</td><td></td><td></td><td>2033**</td><td>920</td></tr><tr><td>Premiere</td><td></td><td></td><td>0.29</td><td>0.59</td><td></td><td></td><td>540</td><td>955</td></tr><tr><td>User characteristics</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Experience</td><td>-0.18</td><td>0.23</td><td>-0.24</td><td>0.22</td><td>-1.6***</td><td>.4</td><td>-1.3***</td><td>.4</td></tr><tr><td>Number of tweets</td><td>0.03*</td><td>0.02</td><td>0.03*</td><td>0.02</td><td>-1.7</td><td>42.9</td><td>1.7</td><td>42.1</td></tr><tr><td>Number of followers</td><td>28.79</td><td>30.51</td><td>49.93</td><td>31.01</td><td>-1038</td><td>3040</td><td>-591</td><td>2987</td></tr><tr><td>Number of friends</td><td>182.15</td><td>296.99</td><td>73.49</td><td>279.53</td><td>161738</td><td>156847</td><td>100788</td><td>152143</td></tr><tr><td>Covariates</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Production budget</td><td>&lt;-0.01</td><td>&lt;0.01</td><td>&lt;-0.01</td><td>&lt;0.01</td><td>76.9***</td><td>14.4</td><td>70.7***</td><td>13.9</td></tr><tr><td>Star power</td><td>-0.40</td><td>0.28</td><td>-0.20</td><td>0.28</td><td>-291</td><td>967</td><td>-916</td><td>913</td></tr><tr><td>Intercept</td><td>0.39</td><td>1.16</td><td>0.43</td><td>1.15</td><td>6283</td><td>3303</td><td>4773</td><td>3054</td></tr><tr><td>BIC</td><td>321</td><td></td><td>305</td><td></td><td>5271</td><td></td><td>5157</td><td></td></tr><tr><td>ΔBIC</td><td></td><td></td><td>16**</td><td></td><td></td><td></td><td>114***</td><td></td></tr></table>

\*p<0.10; \*\*p<0.05; \*\*\*p<0.01.

The comparison of these two nested models indicates a significant improvement in the model fit $( \Delta \mathrm { B I C } _ { ( 3 ) }$ $= 1 6 , p < 0 . 0 1 )$ . Empirical BLUP for random effects indicate that daily valence of pre-release tweets on Android is more positive for documentaries (see Table 6). Next, we added all but our key independent variables to obtain model 2a (see Table 8). The comparison of these two nested models however indicates insufficient improvement in model fit $( \Delta \mathrm { B I C } _ { ( 6 ) } = 7 , \mathrm { n . s . } )$ . Finally, we added our key independent variables to obtain full model, model 2b. The comparison of these two nested models does indicate significant improvement in the model fit $( \Delta \mathrm { B I C } _ { ( 7 ) } = 1 6 , \mathrm { p } < 0 . 0 5 )$

Results of the full model 2b show that daily valence of pre-release tweets on Android is positively associated with higher proportions of mentions of director and script but with lower proportion of mentions of cinematography. Dependent variable in this model is the logit transform of valence while aspects are in proportions, which makes interpretation of coefficients less straightforward. For example, 1% increase in mentions of director is associated with an increase of more than 450% increase in

positivity of valence. However, valence itself is the proportion of difference in positive and negative words to the sum of these words. For example, if the number of positive and negative words were 1 and 0.9 respectively (for a valence of about 0.05) it means the number of positive words would go up by about 0.82 (for a valence of about 0.29). Users who have tweeted more during their lifetime tend to generate more positive tweets on Android in the pre-release period – an increase of one thousand tweets is associated with an increase of 3% in positivity of valence.

## 4.3.2. iOS Volume model

Dependent variable is the daily volume of tweets on iOS after the movie has been released, i.e., during the release weekend and post-release-weekend period. For the purpose of uniformity, all independent variables are the same as in the Android valence model. However, here the proportions of tweets mentioning each of the seven aspects are based on iOS. We built this model incrementally and used BIC to evaluate incremental nested models. The results for the final model for volume appear in Table 8. Similar to previous models, we started with an intercept-only model. Next, we included random intercept effects to account for variation in the volume because of movie genre, MPAA rating, or studio size. The comparison of these two nested models indicates significant improvement in the model fit $( \Delta \mathrm { B I C } _ { ( 3 ) } = 4 7$ $\mathsf { p } < 0 . 0 1 ,$ ). Empirical BLUP for random effects indicate that action / adventure, mystery / thriller, and documentaries generate higher daily volume of tweets on iOS after movie’s release whereas sciencefiction and war movies generate lower daily volume (see Table 6). PG-13 movies generate lower volume too. Movies made by major studios generate higher volume while movies made by intermediate studios generate lower volume. Next, we added all but our key independent variables to obtain model 3a (see Table 8). The comparison of these two nested models indicates significant improvement in model fit $( \Delta \mathrm { B I C } _ { ( 6 ) } = 1 0 4 , \mathrm { p } < 0 . 0 1 )$ . Finally, we added our key independent variables to obtain full model, model 3b. The comparison of these two nested models again indicates significant improvement in model fit $( \Delta \mathrm { B I C } _ { ( 7 ) } = 1 1 4 , \mathrm { p } < 0 . 0 1 )$

Results of the full model 3b show daily volume on iOS after movie’s release is positively associated with higher proportions of mentions of production and music. Because aspects are in proportions, 1

percent increase in mentions of production is associated with an increase of 22 thousand tweets on iOS while 1 percent increase in mentions of music is associated with an increase of 20 thousand tweets on iOS after movie’s release. User experience surprisingly has a negative association – a year’s increase in experience is associated with a decrease of almost 1300 tweets every day after a movie has been released. Also movies made with higher production budget generate higher volume on iOS after the release. An tweets after movie’s release.

## 4.4. Robustness Checks

To check for the robustness of results we estimated several additional models. First, in this study we estimated random effects models to account for any potential correlations between multiple observations for each movie. However, one could argue that the predictor variable terms may not be uncorrelated in the data, which violates a key assumption of random effects models. Hence, we also estimated fixed effects models and found that the results stayed substantively similar. Second, in our revenue model (model 1) we used data for the first ten days after movie release. However, the release weekend has special significance in the movie business – it is believed that most of the movies collect a weekend also lays the ground for its performance later on. It is arguable if these models also hold for movie performance in the release weekend alone. Hence, we re-estimated the revenue model with data from the release weekend only – the results stayed substantively similar. Third, to account for users’ relative preference for encoding positive or negative outcomes we created the valence measure by dividing the sentiment score by the sum of both positive and negative words in each tweet. Prior research in this area has also used the sentiment score only (the numerator in our calculations) to capture valence of tweets. We re-estimated models 1 and 2 using sentiment score alone to capture the valence of tweets – the results were substantively similar. Also, in our Android valence model we had taken the logit transform of valence before estimation because it is a proportion variable. However, because it ranges from −1 to 1 we had to remove the observations with negative values before taking the logit transform. T

# ACCEPTED MANUSCRIPT

check for the robustness of results we estimated a simple GLM model which includes observations with both the positive and negative values of valence – the results indicated similar conclusions. Finally, we also conducted a test to see the predictive performance of the three models. For this purpose, we collected additional data on eight new movies. We used coefficients from the original models to predict the corresponding dependent variables in the new validation set of eight movies. We used several measures to compare the model fit between the two datasets. These measures include normalized root n square error (NRMSE), median absolute deviation (MAD), and symmetric mean absolute per ntage erro (SMAPE) (Armstrong and Collopy, 1992). As shown in Table 9, the results broadly validated the model specifications.

## Table 9

Results from cross-validation testing

<table><tr><td>Samplea</td><td>Normalized Root Mean Square Error (NRMSE)</td><td>Median Absolute Deviation (MAD)</td><td>Symmetric Mean Absolute Percentage Error (SMAPE)</td></tr><tr><td colspan="4">Daily Revenue model:</td></tr><tr><td>Training set (N = 252)</td><td>0.20</td><td>0.61</td><td>0.37</td></tr><tr><td>Validation set (N = 73)</td><td>0.25</td><td>0.80</td><td>0.44</td></tr><tr><td colspan="4">Daily pre-release Android tweets’ Valence model:</td></tr><tr><td>Training set (N = 108)</td><td>0.22</td><td>0.71</td><td>0.61</td></tr><tr><td>Validation set (N = 60)</td><td>0.22</td><td>0.98</td><td>0.81</td></tr><tr><td colspan="4">Daily post-release iOS tweets’ Volume model:</td></tr><tr><td>Training set (N = 272)</td><td>0.11</td><td>1502</td><td>0.60</td></tr><tr><td>Validation set (N = 93)</td><td>0.17</td><td>1696</td><td>0.71</td></tr></table>

Notes: N, the total number of observations in model estimation, =   . <sup>a</sup>Training set has data on 29 movies while validation set has data on 8 movies.

## 5. Conclusion and Implications

The primary objective of this research was to study the conditioning influence of the type of platform used for tweeting (iOS or Android) on the relationship between well-established tweet metrics (volume, valence, and time period of tweeting) and movie performance. Another goal was to uncover any differences between the aspects or topics of a movie about which users of iOS and Android are more likely to tweet about. For this purpose, we collected more than four million tweets for 29 movies and also collected corresponding data from several other sources such as boxofficemojo.com and Internet Movie Database (IMDb). We categorized the tweets based on whether they were sent from iOS or Android

devices and collected the volume and valence of tweets across three time periods – pre-release, the release weekend, and the post-release period of a movie. We performed sentiment analysis on tweets to determine whether they expressed positive, negative, or neutral opinions about the movie. Next, we performed aspect analysis to determine the specific aspects of the movie discussed in each tweet. We estimated mixed models to analyze the data, conducted robustness checks to validate the findings, and derived some interesting results that we summarize next.

Our findings strongly indicate that the average valence of pre-release tweets originating on Android has a significant positive association with daily revenues of movies. In contrast, the volume of daily tweets on iOS after movie’s release has a significant positive association with daily revenue of movies. These differences can be linked to the underlying differences among the users of iOS and Android along various characteristics including demographics, which are reflected in their choices, behaviors, sentiments, and opinions through tweets. These findings provide movie studios prescriptive guidance to focus their targeting and monitoring efforts on different platforms during difference phases of a movie’s lifecycle. They also need to be cognizant of which metrics to monitor from each platform, which is a significant contribution to extant literature on Twitter and movies.

Because only the average valence of pre-release Android tweets and the daily volume of post-release iOS tweets were statistically significant for movie revenues, we focused on them when conducting aspect analysis by platform. Our results show that the valence of pre-release tweets on Android is strongly associated with (a) higher proportions of mentions of director and script but (b) lower proportion of mentions of cinematography. Conversely, an interesting variation revealed by our results is that the volume of tweets on iOS after a movie’s release was strongly associated with higher proportions of mentions of production and music. Another nuanced distinction which our results brought forth was that more prolific users who have tweeted more on Android during their lifetime tend to generate more positive tweets in the pre-release period. In contrast, experienced users who have been Twitter members on iOS for a long time tend to generate lower tweet volume after release, which is counterintuitive but highlights the need to cultivate newer Twitter users on iOS.

# ACCEPTED MANUSCRIPT

These findings have significant implications for movie studios and mobile advertisers. If a firm wants to target both iOS and Android users, a “one size fits all” approach may be ineffective and it is advisable to tailor promotional strategy to users of each platform to maximize the impact. Specifically, to promote on Android, firms need to focus on the director and script of the movie but avoid cinematography. Movie studios could highlight these aspects while other advertisers could craft their messages around them such as by employing the director as a spokesperson and embedding their brand in the storyline. It is also useful to reach heavy Twitter users on Android, who have tweeted more in their lifetimes. In contrast, to promote on iOS, studios and advertisers need to focus on production and music and also attempt to reach newer Twitter users who might actually be more enthusiastic and generate higher volume. Our study is among the first to undertake such a fine-grained examination of the differences among iOS and Android users and how they impact consumption of experiential goods. This is rucial as the adoption of smartphones and other devices is leading to a meteoric growth in mobile advertising (Grewal et al., 2016) that can be effectively utilized by companies in their digital marketing strategies and tactics..

Our study has a few limitations that deserve mention. First, we used an integrated dataset based on a total of 29 movies. These movies do seem to be representative of the population as indicated by the broad range of production budget, star power, user grades, launch seasons, number of screens, genre, MPAA ratings, studio resources, volume and valence generated, and daily revenue generated. We also conducted a cross-validation check using a separate dataset of eight movies. Nonetheless, future research may replicate our models using a dataset composed of a larger number of movies. Second, some Twitter users may use more than one kind of device or platform. Our analysis does not account for this possibility. Third, although our approach to sentiment analysis is similar to that applied successfully in existing research, it did not account for context or sentiment expressions particular to movie-related discussions.

Finally, our study identifies promising areas of future academic research. First, to establish the generalizability of differences between Android and iOS users, future studies should consider other experiential products and services such as airlines and restaurants. Next, future research can develop more advanced sentiment analysis approaches, including those that utilize supervised machine learning. Further academic work can also develop alternative approaches to defining aspect lexicons, including using a team of annotators to build lexicons through review of samples of tweets. Finally, the impact of other devices or platforms used by mobile users can be assessed and compared with iOS and Android.

## References

Armstrong, J. S. & Collopy, F. (1992). Error measures for generalizing about forecasting methods: Empirical comparisons,” International Journal of Forecasting, 8 (June), 69–80.

Asur, S., & Huberman, B. A. (2010). Predicting the future with social media. In Web Intelligence and Intelligent Agent Technology (WI-IAT), 2010 IEEE/WIC/ACM International Conference on (Vol. 1, pp. 492-499).

Bacile, T. J., Ye, C., & Swilley, E. (2014). From firm-controlled to consumer-contributed: Consumer coproduction of personal media marketing communication. Journal of Interactive Marketing, 28(2), 117- 133.

Bakshy, E., Hofman, J., Mason, W., & Watts, D. (2011). Everyone’s an influencer: Quantifying influence on Twitter. In Proceeding of ACM WSDM conference Hong Kong. China.

Benenson, Z., & Reinfelder, L. (2013). Should the users be informed? On differences in risk perception between android and iphone users. In Symposium on Usable Privacy and Security (SOUPS) (pp. 1-2).

Benenson, Z., Gassmann, F., & Reinfelder, L. (2013,). Android and iOS users' differences concerning security and privacy. In CHI'13 Extended Abstracts on Human Factors in Computing Systems (pp. 817- 822). ACM.

Benhardus, J., & Kalita, J. (2013). Streaming trend detection in Twitter. International Journal on Web Based Communities, 9(1), 122–139.

Bermingham, A., & Smeaton, A. (2011). On using twitter to monitor political sentiment and predict election results. In Proceeding of IJCNLP conference, Chiang Mai, Thailand.

Bifet, A., & Frank, E. (2010). Sentiment knowledge discovery in Twitter streaming data. In Proceeding of 13th international conference on Discovery Science Conference (pp. 1–15).

Bollen, J., Mao, H., & Zeng, X. (2011). Twitter mood predicts the stock market. Journal of Computational Science, 2(1), 1–8.

Cha, M., Haddadi, H., Benevenuto, F., & Gummadi, K. (2010). Measuring user influence in Twitter: The million follower fallacy. In Proceeding of 4th AAAI conference on weblogs and social media, Washington DC, (pp. 10–17).

Cheong, M., & Lee, V. C. (2011). A microblogging-based approach to terrorism informatics: Exploration and chronicling civilian sentiment and response to terrorism events via Twitter. Information Systems Frontiers, 13(1), 45-59.

Chin, E., Felt, A. P., Sekar, V., & Wagner, D. (2012, July). Measuring user confidence in smartphone security and privacy. In Proceedings of the Eighth Symposium on Usable Privacy and Security (p. 1). ACM.

Chinni, D. (2016). Consumer Choices Reflected the Nation’s Political Divide. The Wall Street Journal, 29<sup>th</sup> November, 2016. Available at http://www.wsj.com/articles/consumer-choices-reflected-the-nationspolitical-divide-1480415404, [accessed on 29<sup>th</sup> November, 2016].

Chung, J., Mustafaraj, E. (2011). Can collective sentiment expressed on twitter predict political elections? In Proceedings of the twenty-fifth AAAI conference on artificial intelligence (pp. 1770–1771).

da Silva, N. F., Hruschka, E. R., & Hruschka, E. R. (2014). Tweet sentiment analysis with classifier ensembles. Decision Support Systems, 66, 170-179.

Diakopoulos, N. A., & Shamma, D. A. (2010). Characterizing debate performance via aggregated twitter sentiment. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 1195-1198). ACM.

Duan, W., Gu, B., & Whinston, A. B. (2008). The dynamics of online word-of-mouth and product sales— An empirical investigation of the movie industry. Journal of retailing, 84(2), 233-242.

Elberse, A., & Eliashberg, J. (2003). Demand and supply dynamics for sequentially released products in international markets: The case of motion pictures. Marketing Science, 22(3), 329-354.

Felt, A. P., Finifter, M., Chin, E., Hanna, S., & Wagner, D. (2011). A survey of mobile malware in the wild. In Proceedings of the 1st ACM workshop on Security and privacy in smartphones and mobile devices (pp. 3-14). ACM.

Gerpott, T. J., Thomas, S., & Weichert, M. (2013). Characteristics and mobile Internet use intensity of consumers with different types of advanced handsets: An exploratory empirical study of iPhone, Android and other web-enabled mobile users in Germany. Telecommunications Policy, 37(4), 357-371.

Ghiassi, M., Skinner, J., & Zimbra, D. (2013). Twitter brand sentiment analysis: A hybrid system using ngram analysis and dynamic artificial neural network. Expert Systems with applications, 40(16), 6266- 6282.

Gleason, B. (2013). # Occupy Wall Street: Exploring informal learning about a social movement on Twitter. American Behavioral Scientist, 0002764213479372.

Godes, D., & Mayzlin, D. (2004). Using online conversations to study word-of-mouth communication. Marketing science, 23(4), 545-560.

Goh, K. Y., Chu, J., & Wu, J. (2015). Mobile advertising: an empirical study of temporal and spatial differences in search behavior and advertising response. Journal of Interactive Marketing, 30, 34-45.

Grewal, D., Bart, Y., Spann, M., & Zubcsek, P. P. (2016). Mobile advertising: a framework and research agenda. Journal of Interactive Marketing, 34, 3-14.

Grønli, T. M., Hansen, J., Ghinea, G., & Younas, M. (2014). Mobile application platform heterogeneity: Android vs Windows Phone vs iOS vs Firefox OS. In 2014 IEEE 28th International Conference on Advanced Information Networking and Applications (pp. 635-641). IEEE.

Grossman, L. (2009). Iran protests: Twitter, the medium of the movement. Time Magazine, 17.

Hennig-Thurau, T., Gwinner, K. P., Walsh, G., & Gremler, D. D. (2004). Electronic word‐of‐mouth via consumer‐opinion platforms: What motivates consumers to articulate themselves on the Internet? Journal of interactive marketing, 18(1), 38-52.

Hennig-Thurau, T., Wiertz, C., & Feldhaus, F. (2012). Exploring the “Twitter Effect:” An investigation of the impact of microblogging word of mouth on consumers’ early adoption of new products. Available at SSRN, 2016548.

Hennig-Thurau, T., Wiertz, C., & Feldhaus, F. (2015). Does Twitter matter? The impact of microblogging word of mouth on consumers’ adoption of new movies. Journal of the Academy of Marketing Science, 43(3), 375-394.

Hsieh, C., Moghbel, C., Fang, J., & Cho, J. (2013). Experts vs. the crowd: examining popular news prediction performance on Twitter. In Proceedings of ACM KDD conference, Chicago, USA.

Jansen, B. J., Zhang, M., Sobel, K., & Chowdury, A. (2009). Twitter power: Tweets as electronic word of mouth. Journal of the American society for information science and technology, 60(11), 2169-2188.

Jin, S. A. A., & Phua, J. (2014). Following celebrities’ tweets about brands: The impact of Twitter-based electronic word-of-mouth on consumers’ source credibility perception, buying intention, and social identification with celebrities. Journal of Advertising, 43(2), 181-195.

Kaplan, A. M., & Haenlein, M. (2010). Users of the world, unite! The challenges and opportunities of Social Media. Business Horizons, 53(1), 59-68.

Kontopoulos, E., Berberidis, C., Dergiades, T., & Bassiliades, N. (2013). Ontology-Based Sentiment Analysis of Twitter Posts. Expert Systems with Applications.

Liu, B. Sentiment analysis and opinion mining: Synthesis lectures on human language technologies [M].[sl]: Morgan & Claypool Publishers, 2012: 1–167. Google Scholar.

Liu, Y. (2006). Word of mouth for movies: Its dynamics and impact on box office revenue. Journal of Marketing, 70(3), 74-89.

Liu, Y., Li, F., Guo, L., Shen, B., & Chen, S. (2013). A comparative study of android and iOS for accessing internet streaming services. In International Conference on Passive and Active Network Measurement (pp. 104-114). Springer Berlin Heidelberg.

Mathioudakis, M., & Koudas, N. (2010). Twitter Monitor: Trend detection over the twitter stream. In Proceeding of ACM SIGMOD conference (pp. 1155–1158).

McGee, M. (2012). Twitter: 60% of users access via mobile. Retrieved on January 22, 2013 from http://marketingland.com/twitter-60-percent-of-users-access-via-mobile-13626.

Mejova, Y., Srinivasan, P., & Boynton, B. (2013). GOP primary season on Twitter: ‘‘Popular’’ political sentiment in social media. In Proceedings of ACM WSDM conference, Rome, Italy.

Mittal, A. & Goel, A. (2012). Stock prediction using twitter sentiment analysis. Stanford University Working Paper.

Naveed, N., Gottron, T., Kunegis, J., & Alhadi, A. (2011). Bad news travel fast: A content-based analysis of interestingness on Twitter. In Proceeding of 3rd ACM WebSci conference, Koblenz, Germany.

O’Connor, B., Balasubramanyan, R., Routledge, B., & Smith, N. (2010). From tweets to polls: Linking text sentiment to public opinion time series. In Proceeding of 4<sup>th</sup> AAAI Conference on Weblogs and Social Media, Washington DC (pp. 122–129).

Petrovic, S., Osborne, M., & Lavrenko, V. (2010). Streaming first story detection with application to Twitter. In Proceeding of NAACL conference (pp. 181–189).

Phelan, O., McCarthy, K., & Smyth, B. (2009). Using Twitter to recommend real-time topical news. In Proceeding of ACM RecSys conference (pp. 385–388).

Ringsquandl, M. & Petkovic, D. (2013). Analyzing political sentiment on Twitter. In Proceedings of AAAI conference.

Rui, H., Liu, Y., & Whinston, A. (2013). Whose and what chatter matters? The effect of tweets on movie sales. Decision Support Systems, 55(4), 863-870.

SAS (2013), SAS/STAT 12.3 User’s Guide. Cary, NC: SAS Institute Inc.

Stroup, W. (2013). Generalized Linear Mixed Models. Boca Raton, FL: Chapman & Hall/CRC.

Thelwall, M., Buckley, K., & Paltoglou, G. (2011). Sentiment in Twitter events. Journal of the American Society for Information Science and Technology, 62(2), 406–418.

Tumasjan, A., Sprenger, T., Sandner, P., & Welpe, I. (2010). Predicting elections with Twitter: What 140 characters reveal about political sentiment. In Proceedings of the fourth international AAAI conference on Weblogs and social media (pp. 178– 185).

Twitter (2016). Twitter usage / Company facts. Available at https://about.twitter.com/company, accessed on 3<sup>rd</sup> October, 2016.

Wang, H., Can, D., Kazemzadeh, A., Bar, F., & Narayanan, S. (2012). A system for realtime twitter sentiment analysis of 2012 U.S. presidential election cycle. In Proceedings of ACL ACL conference, Jeju, Republic of Korea

Wilson, T., Hoffman, P., Somasundaran, S., Kessler, J., Wiebe, J., Choi, Y., Cardie, C., Riloff, E., & Patwardhan, S. (2005). OpinionFinder: A System for Subjectivity Analysis. Proceedings of Conference on Human Language Technology and Empirical Methods in Natural Language Processing 34-35.

Wong, F. M. F., Sen, S., & Chiang, M. (2012). Why watching movie tweets won't tell the whole story? In Proceedings of the 2012 ACM workshop on Workshop on online social networks (pp. 61-66). ACM.

Zimbra, D., Chen, H., & Lusch, R. (2015). Stakeholder Analyses of Firm-Related Web Forums: Applications in Stock Return Prediction. ACM Transactions on Management Information Systems 6 (1).
