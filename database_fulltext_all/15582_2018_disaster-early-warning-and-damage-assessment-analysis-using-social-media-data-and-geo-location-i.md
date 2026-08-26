---
otero_id: 15582
otero_key: "XSSW7FN3"
title: "Disaster early warning and damage assessment analysis using social media data and geo-location information"
authors: "Desheng Wu; Yiwen Cui"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.04.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Disaster early warning and damage assessment analysis using social media data and geo-location information

![](/api/attachments/XSSW7FN3/fulltext/images/91f08041fa35fc09d21ca7e2dd95e19749ad22acb595c75b4566c7a8fd940b8c.jpg)

Desheng Wu<sup>a,b,⁎</sup>, Yiwen Cui<sup>a</sup>

<sup>a</sup> School of Economics and Management, University of Chinese Academy of Sciences, Beijing 100190, China <sup>b</sup> Stockholm Business School, Stockholm University, SE-106 91 Stockholm, Sweden

## A R T I C L E I N F O

Keywords: Social media Geo-location information Hurricane Sandy Disaster early warning Disaster assessment

## A B S T R A C T

Societies are confronted with destructive natural disasters of increasing frequency. Social networks are playing an increasingly important role as early warning systems, aiding with rapid disaster assessment and post-disaster recovery. There is a need for both the public and disaster-relief agencies to better understand how social media can be utilized to assess and respond to natural disasters. However, existing research on the role of social media in society's response to natural disasters is neither holistic nor systematic. In this study. we conduct a hierarchical multiscale analysis based on multiple data resources, combining social media data, economic losses, and geoinformation. We verify the role played by social media before, during, and after a natural disaster. We investigate whether the combination of social media and geo-location information can contribute to a more e<sup>fi</sup>cient early warning system and help with disaster assessment. This paper draws attention to the fact that during a disaster, citizens turn to social media and the majority of tweets contain information about the hurricane and/or its impact with negative sentiment. We demonstrate that the severity of damage in one area is positively correlated with the intensity of disaster-related activity. Meanwhile, the coastal areas and areas with close proximity to Hurricane center tend to su<sup>f</sup>er from higher losses during a disaster. Our <sup>fi</sup>ndings explore the role played by social media from individuals in a<sup>f</sup>ected populations and how they respond to unfolding natural disasters. Results hold signi<sup>fi</sup>cance with regard to providing timely assistance for both o<sup>fi</sup>cial institutions and netizens.

## 1. Introduction

Natural disasters bring substantial capital losses as well as continuous and severe threats to society. As a result of natural processes, disasters cause a high number of fatalities; they a<sup>f</sup>ect a large portion of the population and incur substantial social impacts and huge economic losses. They may also lead to political instability sometimes [1–3]. To meet the needs of development, citizens are exploiting and irrationally utilizing natural resources which exacerbate the occurrence of natural disasters (such as earthquakes, hurricanes, and <sup>fl</sup>oods), directly and indirectly by changing the climate [4,5]. Timely response and assessment are needed in disaster management. Thus, developing tools for rapid natural disaster response and assessment [6–10] has become a topic of research to re<sup>fl</sup>ect emerging needs from the past few decades [11].

As countries face these needs, expanding applications of social media (such as Twitter, Inc. and Facebook, Inc.) are on the rise. Unlike other traditional ways, social media platforms gather an unprecedented scale of data and amount of information, recording public reactions through both virtual and physical words. This becomes an essential supplement for sociological research [12–14]. These platforms o<sup>f</sup>er possibilities to observe social responses in a timely and continuous manner, speculate on the implications of expressed social attitudes, and distinguish interactions on social media relating to signi<sup>fi</sup>cant events. It appears there is no comparison between social media and other traditional media. Opportunities to interpret data provided by social media are manifold, including those related to public opinion monitoring [15,16], relationship management [17–19], applications in medicine and health care [20–22] and social activities prediction, such as forecasting human behaviors in the stock market with social media sentiment index [23 26].

In recent years, owing to the signi<sup>fi</sup>cant potential of social media, applications of social media in disaster management have attracted much attention from both academic and practitioner circles. Particularly, social media is useful during emergency situations [27]. Twitter as one of the most active social media platforms, it allows its users to deliver short messages with no > 280 characters and to follow anyone he or she is interested in. Such mechanisms lead to a social network topology, with social and informational features o<sup>f</sup>ered by Twitter. Speci<sup>fi</sup>cally, its information network properties can facilitate and accelerate information di<sup>f</sup>usion while its social attributes allow free access to personal information including geo-location, social con nections, and personal emotions. The limitation of message length further promotes the rapid exchange of information. All these features have emerged to reveal Twitter as a research hotspot in the <sup>fi</sup>eld of emergency management.

Extant research on the use of Twitter in emergency management is diverse. Researchers study the features of social media in emergency information di<sup>f</sup>usion [28,29], news collections and dissemination, and emergency response and disaster relief [30–32]. Another branch mainly concentrates on Twitter content, such as analyses of the sentiment of emergency-related messages, crisis detection [33–35], and identifying messages from disaster areas [36–38]. Recently, some scholars have started to use social media (Twitter) to derive information about dis asters such as damage caused by disasters $[ 6 , 3 9 ]$ and correlations between tweet distributions and disaster phenomena (such as <sup>fl</sup>oods and earthquakes) [40–43]. But, the studies are still not comprehensive. For instance, Kryvasheyeu, Y. et al. <sup>fi</sup>nd positive correlation between per capita losses and Twitter activity [7]. However, sometimes a region being a<sup>f</sup>ected not such serious with little population is counted out high per-capita losses mistakenly. Apparently, the most concerning damage in disaster management should be the total damage losses rather than percapita losses. Besides, geo-information, as a vital factor in disaster assessment, is also overlooked.

In addition, understanding relations between social media and nat ural disasters remains limited, especially the combination of large text content and the context of natural disasters [39]. To achieve a comprehensive understanding of natural disasters, we adopt three essential notions of disaster in our study: social, crisis occasion, and systemic de pendency beyond one single event, which has been emphasized in Quarantelli's book [44]. Natural disasters, then, should be considered from multiple perspectives for a more holistic understanding [39,45], especially regarding the understanding of disasters within the frameworks of social time and social spaces. All in all, although scholars have already made it possible for relatively e<sup>fi</sup>cient emergency responses concerning this issue, studies in this area are still in the early stage.

In this paper, we develop a framework which combines data from multiple sources, including social media (Twitter) and geo-location (whether being coastal and the proximity to the hurricane center), with information on disaster losses. We then present a multi-dimensional analysis of a series of Twitter activity during Hurricane Sandy. We start our study from the national level and gradually narrow down to concrete resolutions of states and Zip Code Tabulation Areas (ZCTAs). First, we study how citizens react to a disaster using analyses of both social media volume and content. Second, we investigate reactions between severely and less-severely a<sup>f</sup>ected regions at the state level, then identify general features of the public behavior in response to an emergency event. This allows for the study of whether the combination of social media and geoinformation has an advantage in early warning. Finally, we combine information culled from disaster-related Twitter activity and geo-location features to analyze their correlations with the damage caused by Hurricane Sandy.

The rest of this paper is structured as follows: In the next section, we o<sup>f</sup>er background information on Hurricane Sandy, and then describe our data and their sources. The methods involved in this paper are il lustrated in Section 3. In Section 4, we present our results from the national, states, and ZCTAs dimensions, which are followed by a section that brie<sup>fl</sup>y concludes the paper by summarizing <sup>fi</sup>ndings and discussing the limitations.

## 2. Background and data

The natural disaster chosen for this study is Hurricane Sandy, which was the most destructive hurricane of 2012 and the third-costliest hurricane in American history [46]. It was a late-season tropical cyclone formed on October 22 from a typical wave in the western

Caribbean Sea. At <sup>fi</sup>rst, it moved slowly and continuously, growing in size before it strengthened and was upgraded to a Category 3 hurricane. It hit Cuba on October 25 and became disorganized after it left. It brie<sup>fl</sup>y weakened to a tropical storm and then re-strengthened into a hurricane. On October 29, Hurricane Sandy began to pummel America. One hour later, it was no longer a tropical storm but made its <sup>fi</sup>rst landfall in the continental United States at 23:00 near Brigantine, New Jersey, with wind speeds reaching 130 km/h [47]. As reported by the National Hurricane Center, Sandy a<sup>f</sup>ected 24 states in varying degree, destroyed or damaged 650,000 buildings and houses, left > 8.5 million people out of electric service (some outages lasted several weeks), and caused 157 direct or indirect fatalities. Economic losses amounted to more than \$70 billion in the United States alone [46,48].

Hurricane Sandy attracted extensive coverage from both traditional broadcasting media and online platforms. As such, this study is designed to utilize large data sets from both social media and disaster damage management records. One of the datasets was extracted from online social media data during Hurricane Sandy; the other one was obtained from damage losses data produced by the Federal Emergency Management Agency (FEMA).

## 2.1. Twitter data

Twitter is a free social network and micro-blogging service website that was established in 2006; it is now one of the most popular and active social platforms worldwide. Twitter allows its users to deliver short messages called tweets, using 280 words or less to share their moods, opinions, and comments or to create continual messages about their activities. This kind of information dissemination is called We Media, in which everyone may be involved in the spread of messages and participate in the free exchange of information. Consequently, users receive news and updates faster than traditional media. Alternative geo information may also be attached as long as users agree to start the Global Positioning System function of their devices, which in turn makes a spatial analysis of Twitter postings possible.

To conduct a comprehensive analysis, the tweeting time of our research data ranges from 8:00 a.m. on October 15, 2012 to 7:00 a.m. on November 12, 2012. This is chosen because it covers the period that begins with the formation and concludes with the dissipation of Hurricane Sandy. Our original dataset includes 52.25 million tweets posted by 13.75 million unique users (see Fig. 1). In the interest of studying Twitter from both context and spatiotemporal dimensions, however, the dataset is limited to 5.98 million tweets posted by 2.06 million users, owing to lack of geographical attributes in most of the tweets. We gather 0.5 million and 0.47 million tweets, respectively, originating from New York and New Jersey. In this paper, we set 23:30 on October 29 as the time datum with the number 0 to represent the moment Hurricane Sandy hit the United States. Correspondingly, the notation “-” represents the time preceding Sandy's landfall, while “+” means extending [49]. Positive emotional response ratio (ERR) is de <sup>fi</sup>ned and calculated as the number of positive sentiment-related tweets in an hour divided by the total number in the corresponding period. In a similar vein, negative ERR is also calculated. Positive sentiment-related tweets are those which express happy, glad, and/or passionate feelings while negative sentiment-related tweets are those which include expressions of depression, sadness, and/or hatred.

## 2.2. Hurricane damage losses data

The damage losses dataset was generated by FEMA's Enterprise Coordination & Information Management (ECIM) reporting team. It contains two sub-datasets (one for renters and the other for property owners). To facilitate calculation, we sum the damage of renters and owners as total damage. Other core data elements include the number of applicants, counties, zip codes, and measurements of the severity of damage. (see http://www.fema.gov/what-disaster-assistance).

![](/api/attachments/XSSW7FN3/fulltext/images/7da40616fbfb09d5aaebcc875ede099cbdc42f4d07673a5aba02fe8246e418f1.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/8b959d2a33e05629b3bea7325920f1abca46e3c5dbe505ce18c9d13a768a4d5e.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/e72642124b562fe183f1d2eb1540e83f0b86913722dfd14a7bebed495c7e98d8.jpg)  
Fig. 1. E<sup>f</sup>ect of di<sup>f</sup>erent levels of <sup>fi</sup>ltering and emotional response ration (ERR) changes during Hurricane Sandy. Histograms in (A) and (B) show the number of tweets over time in di<sup>f</sup>erent datasets. (C) illustrates the variation trend of positive and negative ERRs.

## 3. Methods

Our investigation focuses on the use of Twitter during an emergency event, especially how the public responds to a major disaster and which factors may contribute to building an early warning system. To answer those questions, the approaches of characterization still need to be settled.

## 3.1. Reverse geocoding

Dimensional coordination of data in social media as well as information on damage losses is necessary for exploring whether a correlation exists between postings on Twitter and factual data on disaste damage. Because of this, an approach is needed to reverse geo-in formation of tweets into identi<sup>fi</sup>able geographic information.

Geo-location is an essential feature of tweets, allowing for the discovery of user locations [50]. In recent years, studies of the geographic distribution of user behaviors by utilizing tweets' geo-locations have become an essential issue in the <sup>fi</sup>eld of social media [36]. Geo-information implies precise and clearly identifiable information that in cludes names of countries, states, and cities, as well as street addresses and intersections, which even can be narrowed further to highways and speci<sup>fi</sup>c places such as parks and schools. Therefore, it is not e<sup>f</sup>ective to merely use the geotags attached to tweets for determining accurate geolocation. Fig. 2 shows an example of extracted tweets. In it, the attributes “lat\_<sup>fi</sup>nal” and “lng\_<sup>fi</sup>nal” represent, respectively, the latitude and longitude of a user's location, while ‘geom’ indicates another expression of geo-location readable for Geographic Information System tools.

To obtain and rectify more precise geographic information, we used programming tools via the geocoding libraries Google Map API and OpenStreetMap to reverse Twitter geocode. Finally, we got user location attributes including country, state, county, and ZCTA number. This type of supplemental information not only contributes to those who have read the tweets but also helps governments and related institutions to conditionally and conveniently retrieve relevant messages related to emergency events.

## 3.2. Content analysis

## 3.2.1. Sentiment analysis

The objective of this part is to measure the emotion or mood expressed in each tweet and classify it as negative, neutral, or positive, which are then quanti<sup>fi</sup>ed by speci<sup>fi</sup>c <sup>fi</sup>gures. Twitter sentiment analysis has attracted signi<sup>fi</sup>cant public and research interest for several years, especially regarding its applications to the various stock markets, avenues of public opinion monitoring, and disaster warnings [36,51]. Patterns of emotional changes revealed in social media postings are thought to re<sup>fl</sup>ect the spatiotemporal mood variations of society. By analyzing the tweets posted during an event or disaster, governors could deduce and infer public attitudes and opinions and thus making appropriate decisions. At present, the primary methods of Twitter sentiment analysis are conducted by using sentiment lexicons [52,53] or adopting some machine learning methods, such as Naive Bayes, Maximum Entropy, and Support Vector Machine algorithms (SVM) [37,54,55]. In this paper, we utilized lexical resource SentiWordNet 3.0 to calculate a sentiment score for each tweet. A sample of the algorithm process is represented as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Import: Tweets set $T = \{t_1, t_2, t_3, L, t_n\}$, sentiment lexicon Dict, emoticons set Emotions.  
For each tweet $t_i$, the scoring formula $Scores(t_i)$ is:  
$Scores(t_i) = \sum_{w_{i,j} \in t_i} f(w_{i,j}, Dict) + \sum_{e_{i,j} \in t_i} \delta(e_{i,j}, Emotions)$  
Where $w_{i,j}$ and $e_{i,j}$ represent the word and emoticon in tweet $t_i$ respectively.  
$f(w_{i,j}, Dict) = Pos(w_{i,j}) - Neg(w_{i,j})$  
Each word $w_{i,j}$ in Dict has two numerical scores $Pos(w_{i,j})$ and $Neg(w_{i,j})$, which indicate the degree of positivity or negativity.  
$\delta(e_{i,j}, Emotions) = \begin{cases} Pos(e_{i,j}) &amp; \text{if } e_{i,j} \text{ represents positive in Emotions} \\ Neg(e_{i,j}) &amp; \text{if } e_{i,j} \text{ represents negative in Emotions} \end{cases}$  
Output: For each tweet, $Scores(t_i)$ is calculated, where $Scores(t_i) &gt; 0$ indicates positive emotional orientation and vice-versa.
</div>

![](/api/attachments/XSSW7FN3/fulltext/images/d30023c90b9e6d536c0bd3d6acbcb94bb86a5f6078200cdcbd911feb434ff0ea.jpg)  
Fig. 2. An example of the extracted tweets.

## 3.2.2. Top hashtags and keywords frequency analysis

Due to the insu<sup>fi</sup>ciency of contemporary sentiment analysis methods, some tweets will inevitably get assigned to the wrong class. “I love the hurricane Sandy!!!!!!” for example, is most likely a sarcastic expression being used to convey negative feelings, yet the computer would consider it as genuinely positive.

To overcome this problem, other text analysis methods are required here. Hashtag and keyword frequencies are critical in Twitter topic analysis. Hashtag plays an important role as a communication device in the analysis of Twitter topic and is always used for de<sup>fi</sup>ning daily hot topics [49,56]. Besides, previous works indicate that high-frequency keywords may also function well in the topic analysis as a supplementary information channel [57,58]. Kireyev, Palen, and Anderson [59] are pioneers who explored this method to analyze disaster-related messages. They discover that during a disaster the main topics are about information and emotion. Thus, we combined both principal methods (top hashtag and keywords frequency analysis) in selecting words of topics for this study. However, few studies have been devoted to this area as per our knowledge, that there hasn't been a universal criterion for partitioning the topics yet. Finally, we divided these words into <sup>fi</sup>ve categories following the works of Qu et al. and David et al. [7,60,61] (see Table 1). This was done knowing that the <sup>fi</sup>ve topics might reveal and explain potential roles of social media during a nat ural disaster, including information exchange, emotional expression, and appeals for actions.

After reverse geocoding and content analysis, we aggregated the selected tweets according to their locations and time stamps, and then proceeded to connect them with information on economic damage and losses. Comparison metrics include number of posted tweets, timestamps of tweets, the sum of active users, sentiments, and topics (in cluding identi<sup>fi</sup>cation of topic categories). At last, we conducted experiments from three dimensions whose results and implications are illustrated subsequently. Fig. 3 illustrates the proposed data processing and analysis framework.

## 4. Results

## 4.1. The Twitter nationwide analysis in response to Hurricane Sandy

To explore perspectives from the national level regarding the ways in which society responds to a disaster, data are reviewed with consideration for volume and content.

## 4.1.1. Volume of Twitter activity

Fig. 4 illustrates the volume, sentiment, and impact scope of Twitter activity (the number of ZCTAs involved) during Hurricane Sandy. Two patterns demonstrated by all messages and sum of sentiment index are shown in Fig. 4A. The red histogram shows total Twitter messages posted over time, while the blue one represents the total sentiment index (TSI) during Hurricane Sandy (each tweet has a sentimental score and it is summed as a general sentiment index). Fig. 4B shows the number of ZCTAs a<sup>f</sup>ected over the period.

Analyses indicate that the total numbers of Twitter messages and a<sup>f</sup>ected ZCTAs share the same variation trend: The curves <sup>fl</sup>uctuate steadily before the disaster, and then sharply increase to a peak value, followed by a sharp slump back to the average level. Geographically, this change tendency is similar almost everywhere except for the difference between dataset magnitudes. This means that the change tendency of the curves is similar in all places, whether discussing the nation as a whole or individual state such as New Jersey and New York. In addition to these results, TSI in Fig. 4A shows opposite change with the total of Twitter activity. Namely, TSI reaches the minimum value when the number of Twitter activity reaches its sharp peak.

## 4.1.2. Nationwide Twitter content analysis

Hurricanes typically bring enduring in<sup>fl</sup>uences to the daily lives of those it affects. Review of data from this study reveals that Twitter activity skyrockets with the arrival of Hurricane Sandy. Now, we turn to an examination of the content of social media during Hurricane Sandy.

Fig. 5A demonstrates that both positive and negative tweets increase in large increments, while the number of negative tweets has relatively signi<sup>fi</sup>cant growth. An alternative way to summarize the di<sup>f</sup>erence is shown in Fig. 5B, in which we de<sup>fi</sup>ne Positive and Negative D-values. Positive D-value represents the di<sup>f</sup>erence between the numbers of positive and negative tweets divided by the total, while Negative D-value is computed as the di<sup>f</sup>erence between negative and positive ones.

To direct illustrate Twitter contents produced by users during the disaster, we draw a tag cloud of high-frequency words in our dataset, as shown in Fig. 5C. Results show that words such as “hurricane,” “Sandy,” “weather,” “power,” “storm,” “gas,” and “New York” are relatively frequent. A possible reason why “Obama” and “Romney” are also included is that they were the two leading candidates in the presidential election, which was held one week after the hurricane. From another aspect, it seems that Twitter, as a social media platform, has become a favorite channel of communication and information exchange, and records everything happening around people thus to re<sup>fl</sup>ect the masses life patterns or rhythms [45], such as the presidential election and the major disaster Sandy.

Table 1  
Five topics of Twitter messages.

<table><tr><td>Topics</td><td>Description</td><td>Related words</td></tr><tr><td>Disaster-related</td><td>The most important role of Twitter during a disaster is information sharing and dissemination. When people use some words directly related to the disaster, which could attract people&#x27;s attention as an early warning.</td><td>“disaster,” “Franken-storm,” “hurricane,” “flood,” “destroy,” “Sandy,” “storm,” “tornado.”</td></tr><tr><td>Weather-related</td><td>Hurricanes are often accompanied by climate changes, being different from other kinds of natural disasters.</td><td>“cold,” “climate change,” “black out,” “climate.”</td></tr><tr><td>Emotion-related</td><td>Emotional support is important during and after a disaster. When undergoing a disaster, people naturally express their personal feelings and concerns, providing social and emotional support, comfort, and sympathy to others.</td><td>“panic,” “hope,” “terrifying,” “insane,” “scared,” “keep calm,” “scary,” “hungry,” “fuck,” “hate,” “horrible,” “pray for us,” “omg,” “god.”</td></tr><tr><td>Action-related</td><td>When a disaster happens, the government plays an irreplaceable role in disaster relief and support. This category includes the words that people are using to appeal to the government to tack action.</td><td>“government,” “MTA,” “FEMA,” “governor,” “red cross,” “federal,” “Cuomo,” “NY,” “NY,” “wall st,” “CNN.”</td></tr><tr><td>Situation-related</td><td>Situation updates and influence descriptions are important for early warnings and disaster assistance.</td><td>“power,” “no power,” “food,” “house,” “energy,” “hospital,” “airport,” “electric,” “electricity,” “cancelled,” “gas,” “blocked,” “emergency,” “life,” “warning,” “lost,” “help,” “need,” “keep safe,” “safe,” “stay home,” “stay safe,” “recovery,” “survived,” “dead,” “kill,” “dying,” “home,” “problem,” “move.”</td></tr></table>

![](/api/attachments/XSSW7FN3/fulltext/images/07584cf746b28947e03f37177b9a5dc7786bb572c0515805e049c017c3f9ae08.jpg)  
Fig. 3. The process of data processing and analysis.

![](/api/attachments/XSSW7FN3/fulltext/images/27de9b222d913d3e752aeafe607fcec4bf58f8ba58e7ca71b3d391da243a538a.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/efcef4b1647a665f7ad6396c044573621ee874cd024ecfea3819846dc7d8cd96.jpg)  
Fig. 4. Volume, sentiment and the impact scope of Twitter activity during Hurricane Sandy. The horizontal axis is an o<sup>f</sup>set representing the time of Hurricane Sand landfall. (A) shows numbers of Twitter activity and sentiment index over time and (B) represents the number of a<sup>f</sup>ected ZCTAs (with at last posted one disaster related message) over time. (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

Table 2  
![](/api/attachments/XSSW7FN3/fulltext/images/b1bf6cd1a9563bcd15c272bb3e2f4e54fb1e569c37e255f62df689c5c85068bb.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/4f4f81d2cdd266e33da4d4da43f54f141d4486e9276e4e12c27b441dea978dda.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/0bb6ec2349c3d4774f5f51bab24661923876b6890075aed9a0b0d11c44d2ca08.jpg)  
Fig. 5. Twitter content features. (A) and (B) show some features of positive and negative messages over time. (C) is a tag cloud of high-frequency words in this dataset, whose size represents the number of usage in di<sup>f</sup>erent tweets.

![](/api/attachments/XSSW7FN3/fulltext/images/c8947238f4b9a4c171deb75577466e6564668fd0a26d5effdb68343f81a40b46.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/afddf9d5a4c14b365ea2b8d4c5ad62464f33e9b5d1e435b7f0e03573ae936ce9.jpg)  
Fig. 6. The consistency between Twitter activity, <sup>fi</sup>ve topics and sentiment index in American. (A) and (B) represent the topics' trend over time, and the only di<sup>f</sup>erence is the horizontal axis.

Fig. 6 shows the general content topics distribution during Sandy. The topics and total activity curves share the same change tendency which steeply increases on the day the hurricane made landfall. They drop to a lower level afterward and then <sup>fl</sup>uctuate around the normal level. In addition, from Fig. 6, we can verify that the majority of contents being delivered are related to the disaster while other topics are lagging far behind in quantity. The sentiment of the whole nation reaches an extremely low level during this time. Results in Table 2 indicate that disasters, special situations, and emotionally-charged issues have a tremendously positive and signi<sup>fi</sup>cant correlation with Twitter activity, while the sentiment index has a negative correlation. We use Pearson's correlation coe<sup>fi</sup>cient to calculate the relationship between the two variables.

$$
p _ {(x, y)} = \frac {\operatorname{cov} (x , y)}{\sigma_ {x} \sigma_ {y}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {E (X ^ {2}) - E ^ {2} (X)} \sqrt {E (Y ^ {2}) - E ^ {2} (Y)}}
$$

## 4.2. Twitter activity analysis and early warning at the states level

The presence of hurricane activity may result in distinct patterns of performance displayed by users of social media. This study examines whether there will be any di<sup>f</sup>erences in response to a disaster of areas with di<sup>f</sup>erent levels of in<sup>fl</sup>uence. To create a uni<sup>fi</sup>ed standard of severely a<sup>f</sup>ected or less-severely a<sup>f</sup>ected regions, we conduct a statelevel examination of states which have declared a state of emergency.

## 4.2.1. Twitter activity in response to Hurricane Sandy at the state level

According to the report, Hurricane Sandy a<sup>f</sup>ected 24 states in varying degrees; this included most of the east coast from Florida to Maine. Devastating <sup>fl</sup>oods and severe damage were seen in New Jersey and New York. Figs. 7 and 8 present aspects of volume and sentiment considering the ways that citizens from di<sup>f</sup>erent regions respond to the disaster.

Two-dimensional (temporal and spatial) heat maps, normalized and non-normalized, are shown in Figs. 7 and 8. Twitter activity and average sentiment index of each state are calculated in intervals of 12 and 24 h, while normalized and non-normalized indices are calculated to reduce the impact of population among di<sup>f</sup>erent states. To specify, the non-normalized index considers all states as a whole and ignores the di<sup>f</sup>erences among them, while the normalized index is designed to only re<sup>fl</sup>ect changes within a single state. We use min-max method to cal culate normalized Twitter activity (sentiment index), showed as fol lows,

Pearson correlation coe<sup>fi</sup>cients among all messages, <sup>fi</sup>ve topics, and sentiments.

<table><tr><td></td><td>Disaster-related</td><td>Action-related</td><td>Situation-related</td><td>Emotion-related</td><td>Weather-related</td><td>Sentiment index</td></tr><tr><td>Twitter activity</td><td>0.980**</td><td>0.310**</td><td>0.989**</td><td>0.986**</td><td>0.873**</td><td>-0.889**</td></tr></table>

<sup>⁎⁎</sup> Signi<sup>fi</sup>cant at 0.01 level.

D  
D  
![](/api/attachments/XSSW7FN3/fulltext/images/3eb983956d3b2cadb4dd564b408a022244062b5d67dbffa24c57db7ba1d181df.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/fed2830a9b1eab5baaaed572920035c5b669db35f5da48efc5ec50957174b1fd.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/cfc6800acc71b178e6810e60c576a4841ed27337070b1b3732d4cd3ffd04ff36.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/48402f984e1523d892eb1ff4a42b13c824d7a4706c92efdf05dbe80129e534ce.jpg)  
Fig. 7. Summary of Twitter activity by time and location. Colors correspond to the levels of activity (red for a higher active degree, while blue for a lower), both (A) and (C) represent non-normalized, while (B) and (D) are normalized. (For interpretation of the references to color in this <sup>fi</sup>gure legend, the reader is referred to the web version of this article.)

$$
\mathrm{x} _ {i, t} ^ {*} = \frac {\mathrm{x} _ {i , t} - \min \{\mathrm{x} _ {i} \}}{\max \{\mathrm{x} _ {i} \} - \min \{\mathrm{x} _ {i} \}},
$$

where min{x } and max{x } represent the minimum and maximum variable x in the state i respectively, and $x _ { i , t }$ means the variable x at the time t in the state i.

![](/api/attachments/XSSW7FN3/fulltext/images/c6509b34939d302ecc2239c120c6f02a554cc5f3397f846bfe4543586ca2cbd1.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/eb25c052d66c74feb929fe39355980b3d302af368ed36f7b336b1ebf8c5e1e43.jpg)

The red areas in the heat map matrices indicate high levels of activity (or positive sentiment values), while the blue areas represent low levels (or negative sentiment values). (A) and (B) in Figs. 7 and 8 show that the vast majority of states with a higher level of activity and a lower sentiment value are those that have declared a state of emergency; these include Connecticut, New Jersey, New York, and Virginia. In addition, (B) and (D) reveal that Twitter activity becomes active with the arrival of Hurricane Sandy and peaks sharply over the next several

![](/api/attachments/XSSW7FN3/fulltext/images/0a3c25700774135f2686339b2b9a431d27ed70256b42e971a75b1f98a43486ed.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/dacb15491d0ee25f94801cb62f21e59cc5d72cc80837646d1978d0d2ab2440c2.jpg)  
Fig. 8. Summary of an average sentiment index by period and location. Colors correspond to the levels of the sentiment value (red for more positive, while blue for extremely negative). Same as $\mathrm { F i g . } 7 ,$ both (A) and (C) represent non-normalized, while (B) and (D) are normalized. (For interpretation of the references to color in this figure legend. the reader is referred to the web version of this article.)

![](/api/attachments/XSSW7FN3/fulltext/images/92aef6aabc6f30f6ecd0a8ceb652df0d229b21c9cd5f93cba1694e97d68b366b.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/d22ee78cd9002bd2005791d87e0e054f8b54459d462a8f0c1ce5ad86e604a07e.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/e64affcb359fb840b140a33181f47c3fc5b3f8ebe4a4cefc7895368712a0c853.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/9244a46199cc88d66098fadbdbf9c69c683e868ebafd2b8b0f4fbddeeee2eb41.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/96ab781bec92b027718c79eafea829c7b856f41e0157a408cf0bc6329a625b25.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/d55241d91f62a2fb2bec0a2de299fa3bd72f5c056b6412a2c4fded0c4b0d2ead.jpg)  
Fig. 9. Comparison of di<sup>f</sup>erent topic ratios and average sentiment index changes in severely and less severely regions.

hours for each state. Notably, Twitter activity in the two most damaged states (New York and New Jersey) reach their peaks when Sandy arrives and last for several days. Summarily, a<sup>f</sup>ected states show both higher activity and lower sentiment in social media than states which are not a<sup>f</sup>ected or less a<sup>f</sup>ected by the hurricane.

## 4.2.2. Topics of the Twitter activity

We identify a<sup>f</sup>ected and una<sup>f</sup>ected regions to explore di<sup>f</sup>erences among the topics of Twitter activity across various states. This is done to investigate the e<sup>f</sup>ects of early meteorological warnings on Twitter topics and activities. Division among the states, then, is decided ac cording to the declaration of a state of emergency [62–64]. Ultimately, ten states (Connecticut, Delaware, Maryland, Massachusetts, New Jersey, New York, North Carolina, Pennsylvania, Vermont, and Virginia) and the District of Columbia are categorized as severely a<sup>f</sup>ected areas while the rest are seen as less severely a<sup>f</sup>ected.

We de<sup>fi</sup>ne and calculate topic ratios and average sentiment index to study the content category distributions of the messages; this process is equivalent to utilizing the number of each topic-related tweets and sum of the sentiment index respectively divided by the sum of tweets in the same area. Fig. 9 shows that about <sup>fi</sup>ve days before Hurricane Sandy hit the US, the disaster ratio has a remarkable increase in severely a<sup>f</sup>ected areas (shown by a solid line), while the sentiment index ratio becomes negative. This is almost one day earlier than the <sup>fi</sup>rst state announcement of the state of emergency. Fig. 9A and B shows that before the disaster, residents in severely a<sup>f</sup>ected areas are concerned more about the disaster and have an apparently higher emotional catharsis (as with the expression of worries about the coming storm). However, when the hurricane arrives, people in several regions start to keep track of current events and are continuously updating their statuses, especially regarding what they are undergoing and the speci<sup>fi</sup>c impacts of the disaster. As for the overall sentiment tendency, a<sup>f</sup>ected areas have lower sentiment values than una<sup>f</sup>ected areas over the whole period.

The severity of damage may be inferred in advance at the state level based on characteristics of the information stream, such as the ratio of disaster-related messages and average sentimental index. These may help to build an integrated scienti<sup>fi</sup>c disaster early warning and assessment system. To valid whether they are e<sup>fi</sup>cient in disaster assessment, we conduct a series of studies at a <sup>fi</sup>ner spatial granularity.

![](/api/attachments/XSSW7FN3/fulltext/images/810ea3d0cf41de86aa9cf1f42ecfa06664b4dc7be72795d0890e75f9a81b9f8f.jpg)  
C

![](/api/attachments/XSSW7FN3/fulltext/images/62cce0e5cc244d822b47887b427d331e300d1a3a42e259f593668a7adc2613d7.jpg)

![](/api/attachments/XSSW7FN3/fulltext/images/71aee5297729292d6133b1a9a321e1bd901fcb963476ccb9ce89571f847711db.jpg)

D  
![](/api/attachments/XSSW7FN3/fulltext/images/b7b471fe894163fd21784833e3ed39058aefa0bc05904df5563872c069952c87.jpg)  
Fig. 10. The consistency between the Twitter activity, topics and sentiment index in New York and New Jersey.

## 4.3. Twitter activity analysis at ZCTA-level and disaster assessment

Since Sandy's damage was limited to several states, with particularly large losses in New York and New Jersey, the target is therefore narrowed down to those two states. Besides, owing to the limitations in data on damage losses and available Twitter records, we discard some ZCTAs without any Twitter messages or disaster losses data. In sum, we conduct a damage assessment analysis at a meticulous spatial granu larity, targeting New York and New Jersey (within ZCTA-levels) and using corresponding Twitter activity in the same boundaries.

## 4.3.1. Statistical analysis of Twitter activity in severely afected areas

We calculate the consistency between Twitter activity, topics, and sentiment index to understand how citizens of New York and New Jersey respond to the disaster (see Fig. 10). Table 3 shows detailed correlations between the variables above are similar to the indices at both the national and state levels. After having a basic understanding of

Twitter activity in both New York and New Jersey, then we turn to the assessment of disaster using Twitter activity.

## 4.3.2. Twitter activity and disaster assessment

Previous sections and related works [33] suggest that social media can provide an early warning e<sup>f</sup>ect during a disaster. In addition, geoinformation, as a vital factor in disaster assessment, is frequently overlooked and should be used to increase the accuracy of disaster assessment. Thus, we explore the correlations (see Fig. 11) between the total damage losses, Twitter activity, and geo-information (whether being coastal and the proximity to the hurricane center).

The intensity of Twitter activity: Estimation of disaster damage is the stock data after the disaster, while the sum of Twitter messages is the data <sup>fl</sup>ow that varies signi<sup>fi</sup>cantly during the disaster. Hence, we calculate the correlation on a daily accumulation basis to coordinate the data of damage losses and Twitter activity. We then build a dynamic framework to closely follow their correlations. More signi<sup>fi</sup>cant correlations are obtained when calculating the number of disaster-related messages, which indicate that the selected speci<sup>fi</sup>c topic is more conducive to disaster assessment than the whole information <sup>fl</sup>ow. The correlations are presented in Fig. 12 for several days covering the landfall. Results show that the correlation coe<sup>fi</sup>cient between the sum of the disaster-related messages and damage losses at ZCTA level

## Table 3

Pearson correlation coe<sup>fi</sup>cients among Twitter activity, <sup>fi</sup>ve topics, and sentiments in New York and New Jersey.

<table><tr><td></td><td>Disaster-related</td><td>Action-related</td><td>Situation-related</td><td>Emotion-related</td><td>Weather-related</td><td>Sentiment index</td></tr><tr><td>Twitter activity in New York</td><td>0.974**</td><td>0.563**</td><td>0.978**</td><td>0.984**</td><td>0.850**</td><td>-0.927**</td></tr><tr><td>Twitter activity in New Jersey</td><td>0.940**</td><td>0.476**</td><td>0.962**</td><td>0.988**</td><td>0.765**</td><td>-0.954**</td></tr></table>

![](/api/attachments/XSSW7FN3/fulltext/images/e3812a3a931a9cee814eb5f7fc89f12135e39b18091f895017cda1c56f7188e5.jpg)  
A

![](/api/attachments/XSSW7FN3/fulltext/images/ce1d9ab9f53a3fe362223a150e24d37f204d65c293292e0d7de35a91fcf938b9.jpg)  
B

Disaster-related Messages Average Sentiment Total Damage  
![](/api/attachments/XSSW7FN3/fulltext/images/66dc24126d7896bbce0eef9649691f6fcd3b7e472a4d16babd7b4923e460e58c.jpg)  
Fig, 11. Spatial distribution and correlations between the severity of the disaster-related activity, average sentiment index and total damage of the hurricane in New Jersey (A) and New York (B) at ZCTA level. Di<sup>f</sup>erent shades of color represent distinct degrees of the corresponding index, where deeper color represents highe level. Disaster-related activity and total damage follow a quasi-lognormal distribution, and a moderately strong positive correlation between disaster-related activity and damage is found in both New Jersey $( r = 0 . 3 6 7 , p = 2 . 0 3 \mathrm { E } - 4 3 )$ and New York $( r = 0 . 3 9 3 , p = 6 . 0 2 \mathrm { E } - 5 2 )$ at the <sup>fi</sup>ne-resolution ZCTA level. However, average sentiment index is underpowered in New Jersey $( r = { } - 0 . 0 3 5 , p = 0 . 4 3 4 )$ , while the <sup>fi</sup>gures in New York shows that the sentiment index has a signi<sup>fi</sup>cant negative correlation with total damage $( r = { } - 0 . 1 7 6 , p = 0 . 0 2 )$

![](/api/attachments/XSSW7FN3/fulltext/images/861baba7d1c34e188fc6491c15911c74e5402f758940f0fac248aa471ccb5226.jpg)  
Fig. 12. Trend of correlation coe<sup>fi</sup>cients in New Jersey and New York.

started to rise four days before the Hurricane Sandy landfall, then gradually increases with time.

Coastal or non-coastal region: Coastal <sup>fl</sup>ooding is a signi<sup>fi</sup>cant secondary threat during a hurricane and may cause serious damage [65]. Fig. 11 shows that the total damages reach a relatively high level when their locations are close to the coastline, which is consistent with what is empirically known about New York and New Jersey. Considering this, we divide ZCTAs into coastal and non-coastal regions in accordance with their geo-location, where correlation coe<sup>fi</sup>cients are found highly signi<sup>fi</sup>cant in both New Jersey $( r = 0 . 4 7 9 , p = 1 . 0 3 \mathrm { E } - 2 3 )$ and New York $( r = 0 . 6 0 8 , p = 3 . 2 3 \mathrm { E } - 5 1 )$ . This suggests that coastal areas are more likely to su<sup>f</sup>er from high losses than non-coastal ones.

Proximity to the hurricane center: Besides whether being coastal, the proximity to the hurricane center is another signi<sup>fi</sup>cant geo-information in disaster assessment. After evaluating the distance between each ZCTA and the center of Hurricane Sandy (refer to the landfall point), we compute the correlation between proximity and damage losses. Signi<sup>fi</sup>cant but negative correlation coe<sup>fi</sup>cients are discovered both in New Jersey $( r = - 0 . 1 3 2 )$ and New York $( r = - 0 . 5 2 0 )$ .

## 5. Conclusion and discussion

In this study, we have concluded that unexpected natural disasters leave their traces on social media. Society tends to turn to social media, which can re<sup>fl</sup>ect human life patterns and rhythms that are closely associated with the spatiotemporal distributions of disaster. Participation of government agencies and the interactions of commu nications o<sup>fi</sup>cials with citizens via social media platforms strengthen the importance of social media as an indicator of public awareness of a disaster in local areas, which is highly relevant to the in<sup>fl</sup>uence. Based on the connection between natural disasters and social media, we conduct a multi-dimensional analysis to explore their speci<sup>fi</sup>c correla tions.

We develop a data processing framework based on reverse geocoding, sentiment analysis, hashtag and high-frequency approaches to coordinate the multisource data and conduct a multidimensional ana lysis. We also de<sup>fi</sup>ne <sup>fi</sup>ve topics of information in this paper, which corresponded with the keywords in Table 1. The combination of the social media data and geo-information not only helps users who received the message but also contributes to the researchers from the government or o<sup>fi</sup>cial institutions for conditionally and conveniently retrieving relevant messages regarding an emergency.

Based on the framework above, we investigate the question of how people respond to a major disaster as expressed on Twitter and examine it at the national level. Results show that people are using social media for three major purposes during a disaster: emotional expression, situational updates, and disaster-related information exchanges, whose trends suggest a considerable simultaneous growth along with the rapid increase of Twitter messages. Signi<sup>fi</sup>cant correlation between Twitter activity and disaster-related topic strengthens our notion that Twitter, as a social media platform, has recorded all crucial events happening around people and reversely re<sup>fl</sup>ected the life patterns or rhythms of the public.

In addition, we conduct a comparative analysis at the state level to explore the questions of whether there are any di<sup>f</sup>erences in responses to a disaster between a<sup>f</sup>ected and una<sup>f</sup>ected areas, and whether the perceived disaster could be predicted in advance according to users' reactions in social media. We discover that levels of activity and sen timents are largely in<sup>fl</sup>uenced by whether individuals are being a<sup>f</sup>ected by Hurricane Sandy. Furthermore, the ratio of the disaster-related topic in severely a<sup>f</sup>ected areas increases four and a half days in advance of Hurricane Sandy making landfall, and almost one day earlier than the declaration of a state of emergency from the government. This contributes to arguments regarding the establishment of early warning systems for a<sup>f</sup>ected regions. Besides, sentiment index also has the leading e<sup>f</sup>ect as shown in Fig. 9.

Finally, we explore whether we could infer the severity of a disaster through the local information <sup>fl</sup>ow in social media and use it to build an integrated scienti<sup>fi</sup>c disaster early warning and assessment system. We get a similar conclusion with [7] that the intensity of disaster-related Twitter activity has a signi<sup>fi</sup>cant positive correlation coe<sup>fi</sup>cient with damage losses. The primary di<sup>f</sup>erence between our studies is that we focus on the total damage in one area while they calculate a per-capital loss. Additionally, we also <sup>fi</sup>nd that coastal regions tend to su<sup>f</sup>er from higher losses and whether being coastal is positively correlated with the damage losses at the 0.01 level. Meanwhile, distance to the hurricane center and the average sentiment index have signi<sup>fi</sup>cant negative correlation coe<sup>fi</sup>cients with damage losses, but the average sentiment index is sometimes underpowered. Moreover, when calculating the correlation between the proximity to hurricane center and damage losses, a slightly higher correlation is found in New York; possible reasons for this could be that New York state is a place where Hurricane Sandy neither directly landed on nor in<sup>fl</sup>uenced along the trace. Taking all those factors into consideration, the results have signi<sup>fi</sup>cance for both o<sup>fi</sup>cial institutions and public netizens, in potentially providing with timely assistance.

In summary, our study con<sup>fi</sup>rms the close connection between the severity of disaster-related activity in social media and the damage caused by Hurricane Sandy. Di<sup>f</sup>erent from previous works, we have conducted a more holistic study, not only studying early warning e<sup>f</sup>ects of social media at the state level but also combining Twitter characteristics and geo-information to explore their relationships to damage assessments. Due to a paucity of current methods in dividing topics, the accuracy of topic classi<sup>fi</sup>cation is limited. However, this leads it to become one part of our future research agenda.

## Acknowledgments

This work is supported by the Ministry of Science and Technology of the People's Republic of China under Grant 2016YFC0503606, by National Natural Science Foundation of China (NSFC) grant [grant nos. 71471055; 91546102], by a CAS Strategic Research and Decision Support System Development grant (Grant GHJ-ZLZX-2017-36), and by Chinese Academy of Sciences Frontier Scienti<sup>fi</sup>c Research Key Project under Grant No. QYZDB-SSW-SYS021, and Marianne and Marcu Wallenberg Foundation under Grant # MMW 2015.0007.

## References

[1] R. Mechler, Natural Disaster Risk Management and Financing Disaster Losses in Developing Countries, vol. 1, Verlag Versicherungswirtsch, 2004.

[2] M. Dilley, Natural Disaster Hotspots: A Global Risk Analysis, vol. 5, World Ban Publications, 2005.

[3] S. Cole, H. A, E. Werker, Do voters demand responsive governments? Evidence from Indian disaster relief, Journal of Development Economics 97 (2) (2012) 167–181.

[4] R.J. Haarsma, W. Hazeleger, C. Severijns, H. Vries, A. Sterl, R. Bintanja, ... H.W. Brink, More hurricanes to hit western Europe due to global warming Geophysical Research Letters 40 (9) (2013) 1783 1788

[5] J. Tollefson, Hurricane Sandy Spins up Climate Discussion, Nature News, 2012 (doi, 10).

[6] M. Erdik, K. Şeşetyan, M. Demircioğlu, U. Hancılar, C. Zül<sup>fi</sup>kar, Rapid earthquake loss assessment after damaging earthquakes, Soil Dynamics and Earthquake Engineering 31 (2) (2011) 247–266.

[7] Y. Kryvasheyeu, H. Chen, N. Obradovich, E. Moro, P. Van Hentenryck, J. Fowler, M. Cebrian, Rapid assessment of disaster damage using social media activity, Science Advances 2 (3) (2016) e1500779.

[8] P. Bergeijk, S. Lazzaroni, Macroeconomics of natural disasters: strengths and weaknesses of meta-analysis versus review of literature, Risk Analysis 35 (6) (2015) 1050–1072.

[9] S. Hallegatte, Modeling the role of inventories and heterogeneity in the assessment of the economic costs of natural disasters, Risk Analysis 34 (1) (2014) 152–167.

[10] L.N. Rickard, Z.J. Yang, J.P. Schuldt, G.M. Eosco, C.W. Scherer, R.A. Daziano, Sizing up a superstorm: exploring the role of recalled experience and attribution of re: sponsibility in judgments of future hurricane risk, Risk Analysis 37 (12) (2017) 2334-2349

[11] B. Nelson, Natural disasters: a calculated risk, Nature 495 (7440) (2013) 271–273.

[12] D. Lazer, A. Pentland, L. Adamic, S. Aral, A.L. Barabasi, D. Brewer, ... M. Gutmann, Life in the network: the coming age of computational social science, Science 323 (5915) (2010) 721–723

[13] J. You, Who are the science stars of Twitter? Science 345 (6203) (2014) 1440–1441.

[14] B.H. Erickson, Social network analysis: methods and applications, Historica Methods, 1997 (book reviews, June).

[15] M. McCombs, Setting the Agenda: The Mass Media and Public Opinion, John Wiley & Sons. 2013.

[16] C. Shirky, The political power of social media: technology, the public sphere, and political change, Foreign A<sup>f</sup>airs (2011) 28 41.

[17] C. Heller Baird, G. Parasnis, From social media to social customer relationship management, Strategy & Leadership 39 (5) (2011) 30 37.

[18] R.L. Briones, B. Kuch, B.F. Liu, Y. Jin, Keeping up with the digital age: how the American Red Cross uses social media to build relationships, Public Relation Review 37 (1) (2011) 37 43.

[19] L. Peel, D.B. Larremore, A. Clauset, The ground truth about metadata and com munity detection in networks, Science Advances 3 (5) (2017) e1602548.

[20] F.J. Grajales III, S. Sheps, K. Ho, H. Novak-Lauscher, G. Eysenbach, Social media: a review and tutorial of applications in medicine and health care, Journal of Medical Internet Research 16 (2) (2014) e13.

[21] W.-Y.S. Chou, Y.M. Hunt, E.B. Beckjord, R.P. Moser, B.W. Hesse, Social media use in the United States: implications for health communicationJournal of Medical Internet Research 11 (4) (2009) e48.

[22] B. Vyncke, T. Perko, B. Gorp, Information sources as explanatory variables for the Belgian health-related risk perception of the Fukushima nuclear accident, Risk Analysis 37 (3) (2017) 570–582.

[23] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 2 (2008).1–2). 1-135

[24] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, Journal of Computational Science 2 (1) (2011) 1–8.

[25] J. Hirschberg, C.D. Manning, Advances in natural language processing, Science 349 (6245) (2015) 261–266.

[26]J. Van Duick. The Culture of Connectivity: A Critical History of Social Media, Oxford University Press. 2013.

[27] R. Meyer, K. Broad, B. Orlove, N. Petrovic, Dynamic simulation as an approach to

understanding hurricane risk response: insights from the Stormview lab, Risk Analysis 33 (8) (2013) 1532 1552.

[28] C. Jiang, Y. Chen, K.J.R. Liu, Evolutionary dynamics of information di<sup>f</sup>usion over social networks, IEEE Transactions on Signal Processing 62 (17) (2014) 4573–4586.

[29] Y. Li, M. Qian, D. Jin, P. Hui, A.V. Vasilakos, Revealing the e<sup>fi</sup>ciency of information di<sup>f</sup>usion in online social networks of microblog, Information Sciences 293 (2015) 383–389.

[30] J. Yin, A. Lampert, M. Cameron, B. Robinson, R. Power, Using social media to enhance emergency situation awareness, IEEE Intelligent Systems 27 (6) (2012) 52–59.

[31] V.K. Neppalli, C. Caragea, A. Squicciarini, A. Tapia, S. Stehle, Sentiment analysis during Hurricane Sandy in emergency response, International Journal of Disaster Risk Reduction 21 (2017) 213–222

[32] Y. Kryvasheyeu, H. Chen, E. Moro, P. Van Hentenryck, M. Cebrian, Performance of social network sensors during Hurricane Sandv. PLoS One 10 (2) (2015) e0117288

[33] T. Sakaki, M. Okazaki, Y. Matsuo, Earthquake Shakes Twitter Users: Real-time Event Detection by Social Sensors. Paper Presented at the Proceedings of the 19th International Conference on World Wide Web. (2010)

[34] P.S. Earle, D.C. Bowden, M. Guy, Twitter earthquake detection: earthquake monitoring in a social world, Annals of Geophysics 54 (6) (2012).

[35] J. Bohannon, Twitter can predict hurricane damage as well as emergency agencies, Science (2016), http://dx.doi.org/10.1126/science.aaf4182 (Mar 11, 2016)

[36] R.P. Schumaker, A.T. Jarmoszko, C.S. Labedz, Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decision Support Systems 88 (2016) 76–84.

[37] N. Oscar, P.A. Fox, R. Croucher, R. Wernick, J. Keune, K. Hooker, Machine learning, sentiment analysis, and tweets: an examination of Alzheimer's disease stigma on Twitter, Journals of Gerontology. Series B, Psychological Sciences and Social Sciences 72 (5) (2017) 742 751.

[38] D. Pohl, A. Bouchachia, H. Hellwagner, Online indexing and clustering of social media data for emergency management, Neurocomputing 172 (C) (2016) 168 179.

[39] X. Guan, C. Chen, Using social media data to understand and assess disasters, Natural Hazards 74 (2) (2014) 837 850.

[40] B. Herfort, J.P. de Albuquerque, S.-J. Schelhorn, A. Zipf, Exploring the geographical relations between social media and <sup>fl</sup>ood phenomena to improve situational awareness, Connecting a Digital Europe Through Location and Place, Springer, 2014, pp. 55 71.

[41] J.P. De Albuquerque, B. Herfort, A. Brenning, A. Zipf, A geographic approach for combining social media and authoritative data towards identifying useful information for disaster management, International Journal of Geographical Information Science 29 (4) (2015) 667–689.

[42] Y. Lu, D. Yang, Information exchange in virtual communities under extreme disaster conditions, Decision Support Systems 50 (2) (2011) 529–538.

[43] A. Kongthon, C. Haruechaiyasak, J. Pailai, S. Kongyoung, The Role of Twitter During a Natural Disaster: Case Study of 2011 Thai Flood. Paper Presented at the Technology Management for Emerging Technologies (PICMET), 2012 Proceedings of PICMET'12, (2012).

[44] E.L. Quarantelli, What Is a Disaster?: A Dozen Perspectives on the Question, Routledge, 2005.

[45] C. Chen, D. Neal, M. Zhou, Understanding the evolution of a disaster—a Framework for Assessing Crisis in a System Environment (FACSE). Natural Hazards 65 (1) (2013) 407-422.

[46] M. Diakakis, G. Deligiannakis, K. Katsetsiadou, E. Lekkas, Hurricane Sandy mortality in the Caribbean and continental North America. Disaster Prevention and Management 24 (1) (2015) 132 148.

[47] E.S. Blake, T.B. Kimberlain, R.J. Berg, J. Cangialosi, J.L. Beven II, Tropical Cyclone Report: Hurricane Sandy, vol. 12, National Hurricane Center, 2013, pp. 1–10.

[48] E. Blake, J. Cangialosi, J. Beven, Tropical Cyclone Report Hurricane Sandy, National Hurricane Center Sandy, Miami, Florida, 2012 (2013).

[49] F. Morstatter, J. Pfe<sup>f</sup>er, H. Liu, K.M. Carley, Is the Sample Good Enough? Comparing Data From Twitter's Streaming API With Twitter's Firehose, (2013) (arXiv preprint arXiv:1306.5204).

[50] T. Nguyen, M.E. Larsen, B. O'Dea, D.T. Nguyen, J. Yearwood, D. Phung, ... H. Christensen, Kernel-based features for predicting population health indices from geocoded social media data, Decision Support Systems 102 (2017) 22–31.

[51] F.H. Khan, S. Bashir, U. Qamar, TOM: e opinion mining framework using hybrid classi<sup>fi</sup>cation scheme, Decision Support Systems 57 (2014) 245–257.

[52] S. Deng, A.P. Sinha, H. Zhao, Adapting sentiment lexicons to domain-speci<sup>fi</sup>c social media texts, Decision Support Systems 94 (2017) 65–76.

[54] W. Medhat, A. Hassan, H. Korashy, Sentiment analysis algorithms and applications: a survey, Ain Shams Engineering Journal 5 (4) (2014) 1093–1113

[55] G. Gautam, D. Yadav, Sentiment Analysis of Twitter Data Using Machine Learning Approaches and Semantic Analysis. Paper Presented at the Contemporary Computing (IC3), 2014 Seventh International Conference on, (2014)

[56] C. Xing, Y. Wang, J. Liu, Y. Huang, W.-Y. Ma, Hashtag-based Sub-event Discovery Using Mutually Generative LDA in Twitter. Paper Presented at the Proceedings of the Thirtieth AAAI Conference on Arti<sup>fi</sup>cial Intelligence, (2016).

[57] W. Xie, F. Zhu, J. Jiang, E.-P. Lim, K. Wang, Topicsketch: real-time bursty topic detection from twitter, IEEE Transactions on Knowledge and Data Engineering 28 (8) (2016) 2216–2229.

[58] F. Atefeh, W. Khreich, A survey of techniques for event detection in twitter, Computational Intelligence 31 (1) (2015) 132–164.

[59] K. Kireyev, L. Palen, K. Anderson, Applications of Topics Models to Analysis of Disaster-related Twitter Data. Paper Presented at the NIPS Workshop on Applications for Topic Models: Text and Beyond, (2009).

[60] Y. Qu, C. Huang, P. Zhang, J. Zhang, Microblogging After a Major Disaster in China: A Case Study of the 2010 Yushu Earthquake. Paper Presented at the Proceedings of the ACM 2011 Conference on Computer Supported Cooperative Work, (2011).

[61] C.C. David, J.C. Ong, E.F.T. Legara, Tweeting supertyphoon Haiyan: evolving functions of twitter during and after a disaster event, PLoS One 11 (3) (2016) e0150190.

[62] Perdue declares state of emergency before Sandy arrives, Retrieved 1st, February., 2018, from, 2012. http://www.wral.com/sandy-prompts-tropical-storm-watchesalong-nc-coast/11703675/, .

[63] Northeast in crosshairs of ‘superstorm’ Sandy, Retrieved 22th April, 2017 from, 2012. http://edition.cnn.com/2012/10/26/us/tropical-weather-sandy/index. html?hpt=hp\_t1, .

[64] Pres. Obama signs D.C. Emergency Declaration, From http://washington.cbslocal. com/2012/10/28/obama-signs-d-c-emergencv-declaration-due-to-sandv/

[65] M.E. Mousavi, J.L. Irish, A.E. Frey, F. Olivera, B.L. Edge, Global warming and hurricanes: the potential impact of hurricane intensification and sea level rise or coastal <sup>fl</sup>ooding, Climatic Change 104 (3) (2011) 575–597.

Desheng Wu is a Professor with Stockholm University, Stockholm, Sweden and a dis tinguished Professor with the University of Chinese Academy of Sciences, Beijing, China. His current research interests include risk analysis, performance evaluation, and decision support system. He has published over 100 journal papers that have appeared in such journals as Decision Sciences, Production and Operations Management, Risk Analysis, the European Journal of Operational Research, and the IEEE Transactions on Knowledge and Data Engineering. He has published <sup>fi</sup>ve books at Springer. He has served as an Editor/ Guest Editor/Chair for several journals/conferences. He has also edited the special issues include Human and Ecological Risk Assessment in 2009 and 2010, Production Planning and Control in 2009, Computers and Operations Research in 2010, the International Journal of Environment and Pollution in 2009, and Annals of Operations Research in 2010. Mr. Wu is a member of the Professional Risk Managers' International Association, Academic Advisory Committee, a Steering Committee Member and the Chair of the IEEE Analytics and Risk Committee.

Yiwen Cui is a PhD candidate at the University of Chinese Academy of Sciences, Beijing, China. Her research interests are data mining and data mining applications in risk management.
