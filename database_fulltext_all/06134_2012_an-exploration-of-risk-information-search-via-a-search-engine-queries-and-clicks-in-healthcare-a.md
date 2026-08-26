---
otero_id: 6134
otero_key: "B4Q53PAU"
title: "An exploration of risk information search via a search engine: Queries and clicks in healthcare and information security"
authors: "Jingguo Wang; Nan Xiao; H. Raghav Rao"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.09.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An exploration of risk information search via a search engine: Queries and clicks in healthcare and information security

Jingguo Wang <sup>a,</sup>⁎, Nan Xiao <sup>b</sup>, H. Raghav Rao <sup>b,c,</sup>⁎⁎

<sup>a</sup> Information Systems and Operations Management, College of Business, the University of Texas at Arlington, United States

<sup>b</sup> Management Science and Systems, School of Management, State University of New York at Buffalo, United States

<sup>c</sup> WCU Visiting Prof, SSME Department, Sogang University, Seoul, South Korea

## a r t i c l e i n f o

Article history: Received 28 April 2011 Received in revised form 8 September 2011 Accepted 18 September 2011 Available online 25 September 2011

Keywords: Search engine Information foraging Search log Session length Query click rate Markov Chain Monte Carlo simulation

## a b s t r a c t

The general public is increasingly using search engines to seek information on risks and threats. Based on a search log from a large search engine, spanning three months, this study explores user patterns of query submission and subsequent clicks in sessions, for two important risk related topics, healthcare and information security, and compares them to other randomly sampled sessions. We investigate two session-level metrics re<sup>fl</sup>ecting users' interactivity with a search engine: session length and query click rate. Drawing from information foraging theory, we <sup>fi</sup>nd that session length can be characterized well by the Inverse Gaussian distribution. Among three types of sessions on different topics (healthcare, information security, and other randomly sampled sessions), we <sup>fi</sup>nd that healthcare sessions have the most queries and the highest query click rate, and information security sessions have the lowest query click rate. In addition, sessions initiated by the users with greater search engine activity level tend to have more queries and higher query click rates. Among three types of sessions, search engine activity level shows the strongest effect on query click rate for information security sessions and weakest for healthcare sessions. We discuss theoretical and practical implications of the study.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Nearly all problem solving and decision making relies on information search [71]. The growth of the Internet and the World Wide Web has provided easier access to information. One of the bene<sup>fi</sup>ts that the Internet offers is the quantity and quality of individually customized information available with minimal effort and cost, the information that facilitates better decision making and makes the decision-making process more ef-<sup>fi</sup>cient. The arrival of search engines such as Google, Yahoo!, Bing, and AOL has signi<sup>fi</sup>cantly changed the way to forage for information. Millions of searchers regularly use modern search engines to <sup>fi</sup>nd information on the Web for topics ranging from news to healthcare. Recent <sup>fi</sup>ndings from Pew Internet show that almost half of all Internet users submit queries to and click on the results from search engines on a typical day [25].

One research stream in the area of information search focuses on user behavior of seeking for risk information. It attempts to understand how users seek for information related to some threats or hazards. Risk information seeking can be considered as part of individuals' reaction to uncertain risk and affects their consequent protection and mitigation actions [31, 68, 90]. Searching for healthcare information [29, 30, 80] and information security information [85] are two such examples that draw attention from the research community. Compared with searches on other topics, users' search for healthcare and information security are generally considered to be protection-motivated with the purpose to assess, mitigate, or prevent some threat or risk that might directly affect or enhance one's wellbeing or computer assets [18, 28, 73, 86]. An understanding of risk information search could help promote the dissemination of risk information, raise the awareness of risk, and mitigate the impact of hazards. By exploring these two topics, we can better understand how users' information foraging behaviors might change in the context of different types of risks or hazards in their decisions ranging from making purchases of information security artifacts to <sup>fi</sup>nalizing treatment options for healthcare issues.

Using a search engine in pursuit of a search task, a user formulates and reformulates a series of queries. A search session can be de<sup>fi</sup>ned from a contextual viewpoint as a series of interactions among a searcher, a Web system, and the content provided by that system within a speci<sup>fi</sup>c period toward addressing a single information need [38]. During a search session, the user may take several actions including submitting a query, viewing results pages, clicking on URLs, viewing Web documents, and returning to the Web search engine for query reformulation. In a broad sense, the click is a searcher's or seeker's point of “meaningful connection with another person or with the world around” the seeker [10]. The goal for the user in a search session is to locate relevant information that addresses an information need [38].

Many researchers have analyzed search sessions with the goal of using the information about users' activities to improve the performance of Web search engines [38, 55, 74, 89]. The session level is considered to be the key for measuring the performance of search engines and understanding user behavior [38]. There are two main behavioral indicators re<sup>fl</sup>ecting users' interactivity with a search engine: (a) session length (i.e., the number of unique queries submitted by a searcher in a search session) and (b) query click rate (i.e., the average number of clicks per query in a search session), that are often explored. Session length and query click rate re<sup>fl</sup>ect the extent to which a user revises his query and interacts with the search engine for a task. However most prior investigations on these two indicators are descriptive in nature (see Table 1).

Guided by theories in information seeking, we explore (1) the extent to which users submit unique queries in a search session (2) how user search patterns in terms of session length and query click rate may change with search topics (information security, healthcare information, and other topics) and users' search engine activity level (i.e., users' tendency on a typical day to engage in searches with a search engine to <sup>fi</sup>nd answers [16, 17]). We <sup>fi</sup>rst draw from information foraging theory and employ the Inverse Gaussian (IG) distribution to characterize the number of queries per search session. As information seeking behavior can be considered as a function of task characteristics and individual characteristics [45], we propose that users' search pattern (in terms of session length and query click rate) is affected by search topics, users' search engine activity level, and their interaction. In order to test these suppositions, we model the mean parameter of an Inverse Gaussian distribution as the function of search topics, users' search engine activity level, and their interaction. We model the number of clicks in a session following a conditional Poisson distribution given session length, search topics, users' search engine activity level, and their interactions. We test our hypotheses using a search log from a large search engine, spanning three months, for empirical validation. The search log allows us to better understand user search behavior without subjecting users to controlled lab experiments [89].

The contribution of our study is four fold. First, grounded in theories of information seeking, we <sup>fi</sup>nd that Inverse Gaussian (IG) distribution provides a strong <sup>fi</sup>t to the distribution of session length. Second, we quantitatively explore how a seeker's search behavior varies across search topics using a real-life search log. Most prior studies have either descriptively analyzed the popular search topics or terms [14, 37, 74, 78]; see, also, http://www.google.com/trends), or qualitatively compared the search behavior across different topics [6, 53, 79]. Our research also contributes to risk information seeking literature. We demonstrate the differences between the search for information security and healthcare while prior literature (e.g., Ng et. al. [52]) considers both searches are similar in the sense that they are protection-motivated. Third, search engine activity level is an important user characteristic that can be observed based on users' historical behavior and further used to pro<sup>fi</sup>le users. However, the question of how search engine activity level impacts search behavior in terms of session length and query click rate, for a given topic, is an open question that has not been explored before. We <sup>fi</sup>nd users' search engine activity level is an important factor in<sup>fl</sup>uencing user search behavior (in terms of session length and query click rate). Fourth we illustrate that there is an interaction effect between search engine activity level and search topics.

We organize this paper as follows. Section 2 reviews related literatures and introduces our research hypotheses. Section 3 describes the search log used in the study. Section 4 develops our modeling approach and presents analysis results. Section 5 discusses the implications of the research and concludes the paper.

Table 1 Prior studies on session interactions.

<table><tr><td>Ref.</td><td>Log used</td><td>Session length</td><td>Query click rate</td></tr><tr><td>[69]</td><td>AltaVista search engine from August 1998 to 13 September 1998</td><td>The average number of queries per session is 2.02.1 query (77.6%), 2 queries (13.5%),3 queries (4.4%), &gt;3 queries (4.5%)</td><td>N/A</td></tr><tr><td>[34]</td><td>Summary of multiple search engines including Fireball July 1998, Excite on March 10, 1997, and Alta Vista from 2 August to 13 September 1998</td><td>Average number of queries per user session for Excite:1 query (67%), 2 queries (19%),3 queries (7%), 4 queries (3%), more than 4 queries (4%)Average number of queries per user session for Alta Vista:1 query (77.6%), 2 queries (13.5%),3 queries (4.4%), more than 3 queries (4.5%)</td><td>Fireball: 59.51% sessions have 10 or less clicks, 40.47% sessions have &gt;10 clicks;Excite: 58% sessions have 10 or less clicks, 42% sessions have &gt;10 clicks;Alta Vista: 85.2% sessions have 10 or less clicks, 14.8% sessions have &gt;10 clicks</td></tr><tr><td>[75]</td><td>Excite search engine on 16 September 1997</td><td>Average number of queries per user session is 4.86Median number of queries per user session is 8Average number of unique queries per user session is 2.52Median number of unique queries per user session is 4</td><td>N/A</td></tr><tr><td>[75]</td><td>Excite search engine on 16 September 1997 and 20 December 1999.</td><td>Average number of queries per user session in 1997: 1 query (48.4%)2 queries 20.8%; 3+ queries 30.8%Year of 1999: 1 query 60.4%2 queries 19.8%; 3+ queries 19.8%</td><td>N/A</td></tr><tr><td>[74]</td><td>Excite search engine in September 1997, December 1999, and May 2001</td><td>Average number of queries per user session in 1997:1 query (48.4%), 2 queries (60.4%), 3+ queries (55.4%);Average number of queries per user session in 1999:1 query (20.8%), 2 queries (19.8%), 3+ queries (19.3%);2001:1 query (30.8%),2 queries(19.8%), 3+ queries (25.3%);</td><td>N/A</td></tr><tr><td>[73]</td><td>Excite Web search engine collected in May 2001; FAST search engine Web queries submitted on February 6, 2001</td><td>Average number of queries per user session for Excite:1 query (55.4%), 2 queries (19.3%), 3+ queries (25.3%)Average number of queries per user session for FAST:1 query (53%), 2 queries (18.9%), 3+ queries (29%)</td><td>Click rate of Excite is 1.7 and click rate of FAST search engine is 2.2</td></tr><tr><td>[13]</td><td>Search engine of the Utah state government web site from March 1, 2003 to August 15, 2003</td><td>Mean number of queries per session 1.73Median number of queries per session 1Mean number of unique queries per session 1.25Median number of unique queries per session 1</td><td>Average query click rate is 0.56</td></tr><tr><td>[35]</td><td>AlltheWeb.com on 6 February 2001 and 28 May 2002 submitted by European users</td><td>Average number of queries per user session in 2001:1query (53%), 2 queries (18%), 3+ queries (29%)Average number of queries per user session in 2002:1 query (59%), 2 queries(16%), 3+ queries 25%</td><td>Average number of clicks per session is 8.2</td></tr><tr><td>[35]</td><td>AltaVista search engine from 1998 and on September 8,2002</td><td>Average number of queries per user session in 1998:1 query (77.6%), 2 queries (13.5%), 3+ queries (6.9%)Average number of queries per user session in 2002:1 query (47.6%), 2 queries (20.4%), 3+ queries (32.0%)</td><td>N/A</td></tr><tr><td>[54]</td><td>NAVER search engine from 5 January to 11 January 2003</td><td>Average number of queries per session is 1.8 queries with a standard derivation of 2.03</td><td>N/A</td></tr></table>

## 2. Related literature and background theory

## 2.1. Related literature

Previous studies have utilized different levels of granularity to analyze Web search activities and understand the usage of information retrieval systems. Some studies have investigated popular search terms and their frequency of use based on the search logs from various information retrieval systems in different time periods [13, 14, 75]. Some have examined how the frequency of some search terms are affected by temporal and environmental factors [23, 78, 85]. Others have investigated the characteristics of search sessions, where a session comprises one or more consecutive queries and subsequent clicks on the hyperlinks delivered by search engines to the browser [38, 55, 74, 89]. Table 1 summarizes a subset of <sup>fi</sup>ndings on session length and query click rate. While these studies are mostly descriptive in nature, they often lack explanations regarding the extent to which users submit queries in a search session, and what factors might in<sup>fl</sup>uence users' extent of query submission and their resultant clicking behavior.

## 2.2. Background theory and hypotheses

Prior research in information seeking has argued that search behavior is a function of search task and individual characteristics [44]. Browne et al. [12] <sup>fi</sup>nd that when performing online search, individuals utilize a number of stopping rules to terminate search, and that the stopping rule used depends on the type of task performed. Search topic (or domain) has been an important element in understanding online search behavior [53]. Bhavnani [6] <sup>fi</sup>nds the existence of domain speci<sup>fi</sup>c search knowledge. Based on the questionnaires and transaction logs collected from forty-eight participants in a search experiment, Toms et al. [79] <sup>fi</sup>nd users' search behavior for consumer healthcare, shopping, travel and general search are signi<sup>fi</sup>cantly different in terms of their ef<sup>fi</sup>ciency, effectiveness, satisfaction, and search strategy/process. In this study we extend the above literature to propose that users' search patterns (in terms of session length and query click rate) are affected by search topics, users' search engine activity level, and their interaction.

## 2.2.1. Search topics: information security and healthcare

Healthcare and information security are two risk related topics most frequently searched via a search engine [74]. Both information security and healthcare searches may be considered as seeking for speci<sup>fi</sup>c riskrelated information to assess and prevent threats. According to protection motivation theory [65], when people perceive risks, they start threat appraisal and coping appraisal to evaluate the threats and their ability to deal with them. Information seeking occurs during both processes – in threat appraisal, users search for threat characteristics such as the severity and likelihood; in coping appraisal, users search for methods related to control, prevent, and mitigate the threat as well as improving their ability to carry out these methods [51]. Both healthcare and security information are bene<sup>fi</sup>cial to the respective information seekers. Online healthcare information may improve healthcare outcomes, enhance patient–physician communication, and reduce patient's cost. Information security related information can be used to protect a computer or recover a computer from virus af<sup>fl</sup>ictions, and help to understand the characteristics of security threats and determine whether a particular threat is relevant or not. Additionally, healthcare or information security-related search is a precursor to protective behavior. In the domain of search for healthcare information, it has been shown that the act of exploring for illness information can reduce users' anxiety, increase feelings of self-ef<sup>fi</sup>cacy, improve the effectiveness of protection [90], and trigger exercise self-care [18]. In the domain of search for information security, Wang et al. [85] <sup>fi</sup>nd that network attacks of current day and one day prior, lead to signi<sup>fi</sup>cantly more searches on information security. Therefore, information seeking is an important element for both healthcare protection and information security protective behavior [51, 72]. In a recent article, Ng et al. [52] argue that there is a similarity between preventive healthcare behaviors and protective security behavior. Both involve practicing preventive and protective behavior to avert unwanted situations. Theoretical frameworks such as health belief theory, protection motivation theory, and fear appeal theory are often used in both healthcare behavior [49, 60, 87, 88] and information security behavior [1, 41, 47, 52, 85].

While healthcare and information security-related information have their similarities, the efforts of actively seeking these two different types of information differ. Sutrop [77] has discussed two different discourses: the discourse of hope and the discourse of threat. Projects dealing with medical and health care fall into the category of discourse of hope – people search for information that can help result in better diagnostics or treatment. Projects regarding security threats have been identi<sup>fi</sup>ed as belonging to the discourse of threat. People search for information to mitigate and combat the harmful effects of threats, be it identity theft or denial of service. The discourse of hope and the discourse of threat are different and will cause a differential impact on search patterns. Besides, users may be more motivated to search for healthcare than for information security by submitting more queries and clicking more results, because healthcare information may be perceived more important given that it could have an impact on one's health status rather than physical assets (e.g., computers). In addition, when searching for healthcare related information, users tend to seek opinions from different sources on the same issue, because some healthcare information on the Internet maybe inaccurate, incomplete, and sometimes misleading [23]. Users including experts have dif<sup>fi</sup>culties in evaluating the quality of the information and most websites fail to establish their reliabilities [71]. To piece the information together and form a comprehensive understanding, the information seekers have to retrieve more information (i.e., submitting more queries and clicking on more results) [8].

Table 2 summarizes our discussion on the similarities and differences between information security search and healthcare information search. Based on the above discussion, we propose that:

H1(a). Users submit more queries in a healthcare related session than in an information security related session.

H1(b). Users have a higher click rate in a healthcare related session than in an information security related session.

## 2.2.2. Search engine activity level

Search engines enable users to quickly locate relevant information from Internet with the almost instantaneous availability of billions of web pages. A greater activity level implies that a user more frequently turns to Internet and search engines to <sup>fi</sup>nd answers for questions [25]. The usage frequency increases a user's familiarity, knowledge and experience with search engines, and increases his knowledge capital – knowledge about how to search [61]. Compared to less active users, more active users would have more experience with search engines, may be more familiar with how search engines work, and consequently know how to formulate proper queries to re<sup>fl</sup>ect their search intentions. Previous studies <sup>fi</sup>nd that queries submitted by users with more experience contain fewer errors than those by less experienced users [32]. Conversely, the low ability of formulating “good” queries and high probability to make errors could lead less active users less satis<sup>fi</sup>ed with the results returned by the search engine thus resulting in lower search motivations [45]. They could therefore have less search enjoyment for a task [9] or even a negative attitude [82]. Thus, a user with high search engine activity level may have a lower search cost [48] and the utility of continuing search could be higher. Therefore we argue that users with high search engine activity level may be able to check out more sources and indulge in more extensive search than those with low search engine activity levels, having more queries for a particular task and higher query click rate. We propose that:

Table 2  
Similarities and differences between information security search and healthcare information search.

<table><tr><td></td><td>Information security search</td><td>Health information search</td></tr><tr><td colspan="3">Similarities</td></tr><tr><td>Theoretical foundation</td><td colspan="2">Protection motivation theory, fear appeal, health belief theory</td></tr><tr><td>Information seeker&#x27;s knowledge base</td><td colspan="2">Most information seekers lack knowledge in this field. They rely on professionals (e.g., systems administrators and physicians) or Internet for related information</td></tr><tr><td>Information seeks&#x27; motivation</td><td colspan="2">Risk prevention or mitigation</td></tr><tr><td>Information process</td><td colspan="2">Threat appraisal and coping appraisal</td></tr><tr><td>The nature of information looked for</td><td colspan="2">Basic information on risk prevention, evaluation, and recovery</td></tr><tr><td>Impact on information searches</td><td colspan="2">Take remedy action or change behaviors (e.g., install firewalls or quit smoking)</td></tr><tr><td colspan="3">Differences</td></tr><tr><td>Objects to protect</td><td>Information assets</td><td>Human health well-being</td></tr><tr><td>Discourses</td><td>Discourse of threat</td><td>Discourse of hope</td></tr><tr><td>Diversity of information needed</td><td>Less diverse</td><td>More diverse</td></tr></table>

H2 (a). Users with a higher search engine activity level submit more numbers of queries in a session.

H2 (b). Users with a higher search engine activity level have a higher click rate in a session.

2.2.3. The interaction between search domain and search engine activity level

Marketing literature reveals that consumer information acquisition is based on product characteristics and individual differences [43, 50, 63]. As far back as 1923, it had been discovered that different extents of consumer information search exist for different types of products across different consumers (e.g., convenience goods, shopping goods and specialty goods) [20]. Consumers are willing to exert more information search effort when the product to be purchased is of personal importance. In a similar vein, on the one hand, we are looking at healthcare protection behavior that is more focused on individual well-being and on the other hand we are looking at cyber threats that are focused on computers and information – that pertain to physical assets. The above statement focuses on the topic of search for healthcare related sessions vs. information security related sessions. In addition, individual differences between information seekers exist in terms of their familiarity with search engines and this would have an impact on search within the particular domain. Greater search engine activity implies higher knowledge capital [61]. We argue that those with higher knowledge capital (regarding search) would also be more aware of the information security world and more likely to be familiar with computer technology in general because both topics belong to similar disciplines and hence would be able to bring their past experience to bear in extending the search to <sup>fi</sup>nd mechanisms to reduce threats. The knowledge also would facilitate interpretation of new external information on computer technology and information security in particular. Therefore, the knowledge and skills accumulated in previous searches are more likely to be applied in the search of information security and play a more important role during the search process. In contrast, the domain of search and the domain of healthcare are quite different, and the search for healthcare is more likely to be affected by users' health literacy. The knowledge capital regarding search may have less impact in facilitating healthcare related information seeking sessions and in facilitating interpretation of new external information regarding healthcare. Therefore, we propose the interaction effect between search domains and search en gine activity level as follows:

H3 (a). The impact of users' search engine activity level on the numbers of queries in healthcare related sessions is less than in information security related sessions.

H3 (b). The impact of users' search engine activity level on the click rate in healthcare related sessions is less than in information security related sessions.

## 3. Data

We use a search log from AOL Research [55]. The search log includes about 658,000 users over a three-month period from March 01 to May 31, 2006. It covers almost 1.5% of the May search users at AOL according to ComScore Media Metrix. The log has about 20 million search records, and includes around 1/3 of 1% of the total searches conducted through the AOL network over that period. The search log only includes U.S. searches conducted by the users who accessed the Internet through AOL client software. Each entry in the log includes a user ID number, the query submitted by the user, the time at which the query was submitted, and the domain portion of the clicked URL if the user clicked on a search result. Based on whether or not there is a URL in a log entry, we know each entry in the log represents one of two types of events: a query that was followed by a click through on a result item, or a query that was not followed by any click-through. If a user clicked on more than one result in the list returned from a single query, there will be more than one entry in the log with the same query, the same timestamp, and the domain name of the URL clicked. If a user requested “next page" of results for a query, there would be a subsequent identical query with the same timestamp.

Following prior studies [3, 5, 36, 89], we identify sessions using a cutoff value: Two temporally adjacent queries belong to the same session if the time between them is less than the cutoff value; otherwise, the two queries belong to two adjacent sessions. A challenge here is to determine a proper cutoff value. Jansen and Spink [36] and He et al. [3] report that the average search engine session is about 15 min. Baeza-Yates et al. [5] uses 15 min as the cutoff value to de<sup>fi</sup>ne a session. Based on these studies, we use 15 min as our cutoff value; that is, if a user submitted a query 15 min or longer after another query, he or she started a new session.

For the purpose of our analysis, we randomly sampled 2000 sessions related to information security, 2000 sessions related to healthcare, and 2000 randomly sampled sessions related to topics other than these two (these sessions are termed as general search in the paper). The topic of a search session is identi<sup>fi</sup>ed through keyword matching. We selected ten popular keywords for healthcare and information security each that have the least domain ambiguity and also provide suf<sup>fi</sup>cient number of sessions to sample from. The ten popular keywords we use to identify information security related search are: Spyware, Hack, Antivirus, Adware, Identity Theft, Software Virus, Firewall, Computer/Software Virus, Malware, Phishing, regardless of case. These keywords are generated based on the CSI/FBI computer crime and security survey [28, 64] and suggestions from information security professionals. The ten popular keywords of healthcare are obtained from a press release on consumer usage of online healthcare information resources by comScore [19]: Pregnancy, Cancer, Flu, Fitness, Blood Pressure, Rash, Nutrition, Weight Loss, Diabetes, Depression. We summarize the descriptive statistics of the number of queries and clicks in a search session in Table 3.

## 4. Modeling approach and empirical analysis

## 4.1. Modeling the number of queries in a search session

Information foraging theory [57, 59] investigates how strategies and technologies for information seeking, gathering, and consumption are adapted to the <sup>fl</sup>ux of information in the environment. The optimization approach to foraging, originated in ecological studies of search behavior and prey selection among animals. Pirolli and Card [58] apply foraging theory to human activities involving information search, and consider that information foragers will adapt their search to make optimal use of their knowledge resources by comparing the expected value of the information resource to the expected cost of accessing and extracting the relevant information. In order for an information seeker to move from his current state of being to a new state there must be some incentive in the form of net gain. Along this line, Huberman et al. [33] explores the regularities in World Wide Web sur<sup>fi</sup>ng, and shows that Inverse Gaussian (IG) distribution provides a good prediction to the number of pages requested in a website visitation. In this study, we use the Inverse Gaussian distribution to predict the number of queries that users submit per search session. Different from [33], our study extends the theory into a new domain – that of online information search behavior via a search engine and attempts to understand how the Inverse Gaussian distribution can be utilized to help predict the number of queries a user will submit in a search session at an aggregate level.<sup>1</sup>

We consider that users have question(s) in mind, and then seek information to address those questions using a search engine. We view users as rational and adaptive decision makers [62, 66]. When faced with an information seeking problem, they adopt strategies that are optimal based upon their perception of the decision environments. The optimality of a user's search strategy is re<sup>fl</sup>ected in his trade-off between the expected bene<sup>fi</sup>t and the expected cost of search [76,21]. A user sequentially formulates and submits queries to a search engine in order to <sup>fi</sup>nd the relevant information that he needs. The user formulates and reformulates the queries based on his experience and knowledge [32], familiarity with the topic [42], as well as information scent (i.e., cues related to the desired outcome) [56].

Let $Q = \{ 1 , 2 , . . . , T \}$ be a set of different queries that the user formulates during the search. The user faces uncertainty about the utility of each query. The utility of a query is de<sup>fi</sup>ned on how well the query ful<sup>fi</sup>lls the user's information needs, and how much the user spends (for example, physical search cost, cognitive effort) to solicit valuable information from the result list [39]. The user learns about the utility of a query by examining the results returned by the search engine. After the examination, uncertainty regarding the query is removed, and the utility of the query is revealed. We use ${ { z } _ { \mathrm { t } } } ^ { * }$ to denote the utility of the tth query. The query utility in a search session may be low or high. We assume the utility of query t to be stochastically related to that of the previous query t−1, i.e.,

$$
z _ {t} ^ {*} = z _ {(t - 1)} ^ {*} + \delta_ {t}, t = 1, 2, 3,... \delta_ {t} \sim N (\iota , \kappa^ {2})\tag{1}
$$

where $\delta _ { t } ( t = 1 , 2 , . . , T )$ are query utility increments following a normal distribution with mean ι and variance $\kappa ^ { 2 } ,$ . We expect that $\iota { < } 0$ because the utility brought by new queries could be diminishing on average [57]. The increments $\delta _ { t }$ are independent and stationary. t takes integer values representing the sequential no of queries, and ${ z _ { t } } ^ { * }$ is a continuous random variable re<sup>fl</sup>ecting the utility of the tth query. An initial utility ${ z _ { 0 } } ^ { * }$ is available to the user, representing the alternative opportunity that he may have to obtain information from channels other than the search engine. We normalize ${ z _ { 0 } } ^ { * }$ to zero and assume that there exists at least one query for which the expected utility of the query is greater than zero, so that it is worthwhile to search.

After each query, the user must decide whether or not to engage in further search. If he decides to stop searching, he has the information learned so far. Should he wish to continue searching, he selects (or formulates) the next query to be searched. The optimal sequential decision rule should tell him at each stage whether or not to continue search (i.e., the optimal stopping rule) and, if the decision is to continue search, which query to search next (i.e., the optimal selection rule). Let $F _ { t } ( z _ { t } ^ { * } )$ denote the information utility the user is expected to gain if he continues searching after submitted tth query, and we have:

Descriptive Statistics of the number of queries in a search session

<table><tr><td></td><td colspan="2">Pooled</td><td colspan="2">General</td><td colspan="2">Information security</td><td colspan="2">Healthcare</td></tr><tr><td></td><td>Query</td><td>Click</td><td>Query</td><td>Click</td><td>Query</td><td>Click</td><td>Query</td><td>Click</td></tr><tr><td>Mean</td><td>2.33</td><td>2.10</td><td>1.87</td><td>1.59</td><td>2.19</td><td>1.39</td><td>2.93</td><td>3.31</td></tr><tr><td>Median</td><td>1.00</td><td>1.00</td><td>1</td><td>1</td><td>1</td><td>0</td><td>2</td><td>2</td></tr><tr><td>Variance</td><td>6.76</td><td>12.39</td><td>3.07</td><td>6.01</td><td>5.76</td><td>10.22</td><td>10.88</td><td>18.73</td></tr><tr><td>Skewness</td><td>5.67</td><td>4.49</td><td>3.68</td><td>3.99</td><td>6.14</td><td>6.00</td><td>5.07</td><td>3.64</td></tr><tr><td>Kurtosis</td><td>64.44</td><td>32.45</td><td>20.12</td><td>28.85</td><td>69.58</td><td>51.98</td><td>49.99</td><td>21.25</td></tr><tr><td>Minimum</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Maximum</td><td>57</td><td>51</td><td>21</td><td>34</td><td>45</td><td>42</td><td>57</td><td>51</td></tr></table>

$$
F _ {t} (z _ {t} ^ {*}) = \max \Bigl \{0, \frac {1}{1 + r} E \bigl [ U _ {t + 1} (z _ {t + 1} ^ {*}) | z _ {t} ^ {*} ] \Bigr \} U _ {t + 1} (z _ {t + 1} ^ {*}) = z _ {t + 1} ^ {*} + F _ {t + 1} (z _ {t + 1} ^ {*})\tag{2}
$$

where r is a discount rate, ${ z _ { t + 1 } } ^ { * } { = } { z _ { t } } ^ { * } + \delta _ { t + 1 } ,$ , and $E ( \bullet )$ is the expected value taken with respect to the utility increment $\delta _ { t + 1 } .$ . Suppose that the user stops searching after the Tth query. Then we have $F _ { T } ( z _ { T } ^ { * } ) { = } 0$ . In other words, the user exits a search after T queries if and only if $E [ U _ { T + 1 }$ $( z _ { T + 1 } { } ^ { * } ) | z _ { T } { } ^ { * } ] = 0 .$

When r is greater than zero (which is reasonably assumed given that vast information over the Internet), there exists a <sup>fi</sup>xed threshold, τ, which could be suf<sup>fi</sup>ciently negative such that it is optimal to continue when ${ z _ { t } } ^ { * } > \tau ,$ and optimal to stop when ${ z _ { t } } ^ { * } { \le } \tau [ 2 2 ]$ . Though here we have a random walk which is discrete in “time” (the number of queries) but with continuous increments, Wald and Lee[84] shows that this form of stopping problem converges to the result for Brownian motion. Thus the question regarding when the user stops searching is similar to the question when an investor exercises an investment option for a project whose price changes following a Brownian motion [22]. An optimal exercise point for the price can be derived by using a dynamic programming procedure, and the investor may exercise his option when the price of the project reaches its optimal exercise point. Along the same vein this also holds for search. A threshold exists for query utility, and the user could stop searching when the utility of the current query reaches the threshold τ where $F _ { t } ( \tau ) = 0 . \ [ 3 3 ]$ and [33] present similar arguments on when to stop requesting new pages for a web site visitation.

The problem of when to exercise an option (or when to stop searching) is known as the <sup>fi</sup>rst passage time problem in Brownian motion: the time taken to <sup>fi</sup>rst cross a threshold value, b, given that the Brownian motion starts at a certain point, $T { = } \operatorname* { i n f } \{ t { : } z _ { t } { ^ { * } } = \tau \}$ Since it is a stochastic process and there are many possible paths to reach the threshold, the solution is to <sup>fi</sup>nd the distribution of time T. Note that here we measure the “time” (or length of path) in terms of the number of queries submitted, but not the time duration spent on a session or a query. It is well known (see, e.g., [26, 67, 81], that the <sup>fi</sup>rst passage time to the threshold $\tau , T ,$ converges to the Inverse Gaussian (IG) distribution given the <sup>fi</sup>nite variance $( \kappa ^ { 2 } )$ of $\delta _ { t } .$ Its probability density function is:

$$
f (T) = \sqrt {\frac {\lambda}{2 \pi T ^ {3}}} \exp \left[ \frac {- \lambda (T - \mu) ^ {2}}{2 \mu^ {2} T} \right]\tag{3}
$$

where TN0 and the distribution has a mean of $\mu$ and a variance of $\mu ^ { 3 } / \Lambda , \mu { > } 0$ and $\lambda > 0$ . The parameters μ and λ have the following interpretations: $\begin{array} { r } { \mu = \frac { b } { \nu } , \lambda = \frac { \hat { b } ^ { 2 } } { \kappa ^ { 2 } } . } \end{array}$ IG distribution is an asymmetric, heavytailed distribution. Its probability density is always positively skewed and the excess kurtosis is always positive. As λ tends to in<sup>fi</sup>nity, the inverse Gaussian distribution becomes more like a normal (Gaussian) distribution.

If we allow the mean number of queries in session varies for session to session, we can rewrite Eq. (3):

$$
f \left(T _ {i j}\right) = \sqrt {\frac {\lambda_ {j}}{2 \pi T _ {i j} ^ {3}}} \exp \left[ \frac {- \lambda_ {j} \left(T _ {i j} - \mu_ {i j}\right) ^ {2}}{2 \mu_ {i j} ^ {2} T _ {i j}} \right]\tag{4}
$$

where $T _ { i j }$ is the number of queries in the jth $( j = 1 , 2 , . . . , 2 0 0 0 )$ session searching for topic $i ( i = 1 , 2 , 3 )$ in our sample, $\mu _ { i j }$ is the expected number of queries of the session, and $\lambda _ { j }$ is topic-speci<sup>fi</sup>c to capture topic heteroscedasticity. To test the effects of search topic and search engine activity level, we can model $\mu _ { i j } .$

$$
\log \left(\mu_ {i j}\right) = a _ {i 1} + a _ {i 2} q _ {i j} + \varepsilon_ {i j}, \varepsilon_ {i j} \sim \text { normal } (0, \sigma_ {\varepsilon j})\tag{5}
$$

where i=1,2,3 representing the search on general topics, information security, and healthcare, and we have topic-speci<sup>fi</sup>c coef<sup>fi</sup>cients $a _ { i 1 } , a _ { i 2 }$ in our regression. $q _ { i j }$ is the search activity level of the user initiated the session, and $\varepsilon _ { i j }$ is an error term to capture unobserved heterogeneity normally distributed with mean zero and topic-speci<sup>fi</sup>c standard deviation $\sigma _ { \varepsilon j } .$ We use the log form of $\mu _ { i j }$ as the dependent variable to ensure its positivity. The coef<sup>fi</sup>cients $a _ { i 1 }$ , a , λ and $\sigma _ { \varepsilon j } ( i = 1 , 2 , 3 )$ are to be estimated.

4.2. Modeling the relationship between the number of clicks and the number queries

For a given number of queries $T _ { i j }$ in a session, we consider that the number of clicks follows a Poisson distribution:

$$
f \left(y _ {i j} \mid T _ {i j}\right) = \frac {e ^ {- \beta_ {i j} T _ {i j}} \left(\beta_ {i j} T _ {i j}\right) ^ {y _ {i j}}}{y _ {i j} !}\tag{6}
$$

where $y _ { i j }$ is the number of clicks given the number of queries submitted in a search session $\left( T _ { i j } \right)$ , and $\beta _ { i j }$ is query click rate on a query in a search session.

To test the effects of search topic and search engine activity level, we model query click rate $\beta _ { i j } \left( \mathrm { i . e . } \right.$ , the click rate of $j \mathrm { t h } ( j = 1 , 2 , . . . , 2 0 0 0 )$ session in the sample for topic $( i = 1 , 2 , 3 )$ as a function:

$$
\log \left(\beta_ {i j}\right) = b _ {i 1} + b _ {i 2} q _ {i j} + v _ {i j}, v _ {i j} \sim \text { normal } \left(0, \sigma_ {v j}\right)\tag{7}
$$

Again, $\nu _ { i j }$ is an error term to capture unobserved heterogeneity normally distributed with mean zero and topic-speci<sup>fi</sup>c standard deviation $\sigma _ { \nu j } .$ We use the log form of $\dot { \rho } _ { i j }$ as the dependent variable to ensure its positivity. The topic-speci<sup>fi</sup>c coef<sup>fi</sup>cients $b _ { i 1 } ,$ , b and $\sigma _ { v j } ( i = 1 , 2 , 3 )$ ) are to be estimated.

## 4.3. Modeling a user's search engine activity level

We measure a user's search engine activity level as the probability that he engages in at least one search in a typical day using the search engine. We regard such search engine activity level as a latent variable and incorporate a Bayesian shrinkage method to estimate its expected value based on the observed behavior of each user. This approach was used in [40] to measure the level of consumers' shopping activity. We consider the number of days a user uses the search engine for search as a zero-truncated binomial process considering that the search log only includes those users who initiated at least one search. Let q be a user's search engine activity level to user a search engine in a typical day. In the search log for N days (the days between the <sup>fi</sup>rst query and the last query in the log he or she submitted), the probability that a user had n active days among these N days is as follows:

$$
P (n | N, q) = \frac {\binom {N} {n} q ^ {n} (1 - q) ^ {(N - n)}}{1 - (1 - q) ^ {N}}\tag{8}
$$

We assume q to be distributed across the population according to a beta distribution with parameters k and m to allow for heterogeneity in the search engine activity level of users.

Note: One alternative measure we could use is the proportion of days for which the user was using the search engine and for which the user submitted queries. However, because not all users are present in equal amounts of time in our three-month search log, such a measure is likely to misrepresent one's latent and true tendencies in search. For example, a user who was observed in the log for only one day (for example, on April 15 2006) and was also active on this day would be represented by this measure as 1 (or every day in the three month), even if this individual's true activity level is signi<sup>fi</sup>cantly less frequent (say every 50 days). Because we are only able to observe a small sample of some users' lifetime behavior, such a measure based on limited history may not be able to re<sup>fl</sup>ect a user's latent and true tendency.

## 4.4. Estimation method

We estimate the models using Markov Chain Monte Carlo (MCMC) methods to obtain a distribution for each model parameter. We use uninformative but proper priors and hyperpriors. Particularly, we specify λ in Eq. (4) as gamma (1,1), $a _ { i } ( i = 1 , 2 , 3 , 4 )$ in Eq. (5) and $b _ { i } ( i = 1 , 2 , 3 , 4 )$ in Eq. (7) as normal (0,100), and k and m of the beta distribution of q in Eq. (8) as gamma (1,1). Following standard practices, we simulate multiple chains. Each chain has 12,000 iterations, and the <sup>fi</sup>rst 6000 are discarded as an initial burn-in. We monitor and plot the traces of each model parameters for all chains to con<sup>fi</sup>rm the adequacy of convergence of the model. All plots show convergence. The Gelman–Rubin convergence statistic [11] also demonstrates evidence of suf<sup>fi</sup>cient convergence.

## 4.5. Analysis results

To validate Eq. (3) on the distribution of the number of queries in a search session, we estimate μ and λ in Eq. (3) using method of moments for the pooled data, where $\hat { \mu } = E ( X )$ and $\begin{array} { r } { \dot { \hat { \lambda } } = \frac { E \breve { ( X ) } ^ { 3 } } { V ( X ) } } \end{array}$ . E(X) denotes the mean of queries (or clicks) in a session, and V(X) the variance of queries (or clicks). Fig. 1(a) plot the estimated and the empirical cumulative distribution functions for queries and clicks of three samples. To examine the quality of the <sup>fi</sup>t, we <sup>fi</sup>rst analyze quantile–quantile (q–q) plots. Fig. 1(b) provides a q–q plot for the <sup>fi</sup>t. We also regress the observed values on the <sup>fi</sup>tted value, and the variance of the observed value explained by the <sup>fi</sup>tted value, R<sup>2</sup>, are 95.5%. Both analyses con<sup>fi</sup>rm the strong <sup>fi</sup>t of the theoretical distribution to the empirical data.

We test an alternative proposition to con<sup>fi</sup>rm the model: users conduct independent Bernoulli trials to make a stopping decision after each query. This leads to a geometric distribution of the number of queries in a session. It is poorly <sup>fi</sup>tted to the data as we can see from the q–q plot in Fig. 1(b). Hence this alternative proposition is not supported.

In Tables 4b,4c, 5b,5c, and 6, we present the estimated coef<sup>fi</sup>cients, along with the standard deviations and 95% con<sup>fi</sup>dence intervals calculated from MCMC simulations for information security search as well as healthcare search. In addition, we also estimate the coef<sup>fi</sup>- cients for the general search case, as a benchmark, in Tables 4a and 5a.

By comparing the estimated coef<sup>fi</sup>cients for constant term $a _ { i 1 }$ $( i = 1 , 2 , 3 )$ between different topics (Table 7a), we see that both $a _ { 3 1 }$ are signi<sup>fi</sup>cantly larger than $a _ { 1 1 }$ and $a _ { 2 1 }$ , indicating that users are likely to submit more queries in a search session related to healthcare than to information security and other topics. Thus, H1(a) is supported. We also <sup>fi</sup>nd that $b _ { 3 1 }$ is signi<sup>fi</sup>cantly larger than $b _ { 1 1 }$ and $b _ { 2 1 }$ (Table 7b). The results suggest compared with searches on information security and other topics, users are more likely to click on the results returned by a query on healthcare. Thus, H1(b) is supported. In addition, searches on information security has the smallest query click rate compared with healthcare and other topics, evidenced by that $b _ { 2 1 }$ is signi<sup>fi</sup>cantly smaller than other two coef<sup>fi</sup>cients.

Our results in (Tables 4a, 4b, 4c) also show all a $( i = 1 , 2 , 3 )$ are significantly positive, suggesting that users with greater search activity are likely to submit more queries in a search session. Thus, H2 (a) is supported. We also <sup>fi</sup>nd from (Tables 5a, 5b, 5c), that all b $( i = 1 , 2 , 3 )$ are signi<sup>fi</sup>cantly positive, suggesting that users with greater search engine activity have higher query click rates. Thus, H2(b) is supported. By comparing $a _ { i 2 } \left( i = 1 , 2 , 3 \right)$ , we <sup>fi</sup>nd that the effect of q on the expected number of queries in a search session is stronger for information security signi<sup>fi</sup>- cantly than general sessions , but not than healthcare (Table 8a). Therefore H3a is not supported. By comparing $b _ { i 2 } ( i = 1 , 2 , 3 )$ , we <sup>fi</sup>nd the effect of q on query click rate varying across topics: it is strongest for information security, and weakest for healthcare (Table 8b). Thus H3b are supported.

Fig. 2 plots the relationship between search engine activity and session behavior for different topics. The bottom part of the <sup>fi</sup>gure is a histogram representing the distribution of users based on their level of search engine activity. In the middle part of the <sup>fi</sup>gure, the solid line indicates the mean of predicted numbers of queries in a session at each activity level, q, and the dotted lines indicate the 95% con-<sup>fi</sup>dence bounds. In the upper part of the <sup>fi</sup>gure, the solid line indicates the mean of predicted query click rate in a session at each activity

a. Empirical and Fitted CDF of the Number of Queries  
![](/api/attachments/B4Q53PAU/fulltext/images/9912867185d37eacf3e330c706feda7928d847a627057f8b19c29db77d118304.jpg)

b. Q-Q Plot for the Fit of Query Distribution  
![](/api/attachments/B4Q53PAU/fulltext/images/0a4ece93abfd2b61dddeb0f5fafddd3f6608d4c2a0b08d97b55abf19c350de85.jpg)  
Fig. 1. The cumulative distribution functions (CDFs) and q–q plots of the distribution of queries in a search session. a. Empirical and <sup>fi</sup>tted CDF of the number of queries. b. q–q plot for the <sup>fi</sup>t of query distribution.

Table 4a  
Regression on mean query number in a session (Eqs. (4) and (5)) for general search.

<table><tr><td>Parameter</td><td>Mean</td><td>Std Dev</td><td>2.50%</td><td>25%</td><td>50%</td><td>75%</td><td>97.50%</td></tr><tr><td> $a_{11}$  (constant)</td><td>0.42</td><td>0.03</td><td>0.36</td><td>0.40</td><td>0.42</td><td>0.43</td><td>0.48</td></tr><tr><td> $a_{12}$  (q)</td><td>0.18</td><td>0.06</td><td>0.05</td><td>0.14</td><td>0.18</td><td>0.22</td><td>0.29</td></tr><tr><td> $\lambda_1$ </td><td>9.60</td><td>0.59</td><td>8.42</td><td>9.22</td><td>9.58</td><td>9.99</td><td>10.76</td></tr><tr><td> $\sigma_{\varepsilon 1}$ </td><td>0.40</td><td>0.01</td><td>0.38</td><td>0.39</td><td>0.40</td><td>0.41</td><td>0.43</td></tr></table>

## Table 4b

Regression on mean query number in a session (Eqs. 4 and 5) for information security search.

<table><tr><td>Parameter</td><td>Mean</td><td>Std dev</td><td>2.50%</td><td>25%</td><td>50%</td><td>75%</td><td>97.50%</td></tr><tr><td> $a_{21}$  (constant)</td><td>0.43</td><td>0.03</td><td>0.38</td><td>0.41</td><td>0.43</td><td>0.45</td><td>0.50</td></tr><tr><td> $a_{22}$  ( $q$ )</td><td>0.52</td><td>0.08</td><td>0.34</td><td>0.46</td><td>0.52</td><td>0.57</td><td>0.68</td></tr><tr><td> $\lambda_2$ </td><td>8.44</td><td>0.51</td><td>7.43</td><td>8.08</td><td>8.47</td><td>8.79</td><td>9.40</td></tr><tr><td> $\sigma_{e2}$ </td><td>0.42</td><td>0.02</td><td>0.39</td><td>0.41</td><td>0.42</td><td>0.43</td><td>0.45</td></tr></table>

Regression on mean query number in a session (Eqs. (4) and (5)) for healthcare search.

<table><tr><td>Parameter</td><td>Mean</td><td>Std dev</td><td>2.50%</td><td>25%</td><td>50%</td><td>75%</td><td>97.50%</td></tr><tr><td> $a_{31}$  (constant)</td><td>0.77</td><td>0.04</td><td>0.69</td><td>0.74</td><td>0.77</td><td>0.80</td><td>0.85</td></tr><tr><td> $a_{32}$  ( $q$ )</td><td>0.34</td><td>0.09</td><td>0.17</td><td>0.28</td><td>0.34</td><td>0.40</td><td>0.50</td></tr><tr><td> $\lambda_3$ </td><td>6.88</td><td>0.49</td><td>5.97</td><td>6.55</td><td>6.87</td><td>7.20</td><td>7.86</td></tr><tr><td> $\sigma_{e3}$ </td><td>0.50</td><td>0.02</td><td>0.46</td><td>0.49</td><td>0.50</td><td>0.52</td><td>0.54</td></tr></table>

level, q, and the dotted lines indicate the 95% con<sup>fi</sup>dence bounds. We can see that overall the number of queries/clicks submitted in a session increase as user search engine activity increases. We also see that the effect of search engine activity level on session length and query click rate for different search topics is different.

## 4.6. Robustness checking

To examine whether the results are affected by the method used in session identi<sup>fi</sup>cation, we use two additional methods to identify sessions: 20 min cutoff value and 30 min cutoff value as a criterion for new sessions separately [2]. We did not see signi<sup>fi</sup>cant change of the results. Since it is possible that users may switch the search topics (for example, sports, entertainment, <sup>fi</sup>nance) in a search session, we manually examined the search content of the 2000 sessions related to information security and healthcare following content analysis procedures. After we discarded about 20% of the sessions which crossed multiple topics, we did not <sup>fi</sup>nd the change of the results signi<sup>fi</sup>cant either.

## 5. Discussion and conclusion

Based on a search log from a large search engine, spanning three months, we verify the validity of inverse Gaussian distribution to predict the number of queries and clicks in a search session and show that it provides a strong <sup>fi</sup>t to the data. We also <sup>fi</sup>nd that session length and click rate varies with search topics (information security vs. healthcare) and a user's search engine activity level (i.e., tendency to use a search engine on a typical day).

Our data analysis also compares information security search and healthcare information search with other randomly sampled sessions. Although the risk information search differs from general search significantly, the difference is not the same across these two risk categories. General search has lower number of queries and query click rate per session than healthcare search as we expect. But its number of queries is not signi<sup>fi</sup>cantly different with information security search. Also, general search even has a higher click rate than information security search. Our results reveal that users perceive different risks between information security threats and healthcare hazards, which in turn affect their search behavior. While they search more information on healthcare, when compared with general search, individuals do not show stronger information needs for information security.

Regression on query click rate in a session (Eqs. 6 and 7) for general search

<table><tr><td>Parameter</td><td>Mean</td><td>Std dev</td><td>2.50%</td><td>25%</td><td>50%</td><td>75%</td><td>97.50%</td></tr><tr><td> $b_{11}$  (constant)</td><td>-0.88</td><td>0.07</td><td>-1.01</td><td>-0.92</td><td>-0.88</td><td>-0.83</td><td>-0.73</td></tr><tr><td> $b_{12}$  ( $q$ )</td><td>1.00</td><td>0.13</td><td>0.73</td><td>0.91</td><td>1.00</td><td>1.10</td><td>1.29</td></tr><tr><td> $\sigma_{v1}$ </td><td>0.81</td><td>0.03</td><td>0.76</td><td>0.80</td><td>0.81</td><td>0.83</td><td>0.88</td></tr></table>

Regression on query click rate in a session (Eqs. 6 and 7) for information security search

<table><tr><td>Parameter</td><td>Mean</td><td>Std dev</td><td>2.50%</td><td>25%</td><td>50%</td><td>75%</td><td>97.50%</td></tr><tr><td> $b_{21}$  (constant)</td><td>-1.63</td><td>0.08</td><td>-1.79</td><td>-1.68</td><td>-1.62</td><td>-1.57</td><td>-1.48</td></tr><tr><td> $b_{22}$  ( $q$ )</td><td>1.54</td><td>0.15</td><td>1.25</td><td>1.44</td><td>1.55</td><td>1.63</td><td>1.83</td></tr><tr><td> $\sigma_{v2}$ </td><td>0.94</td><td>0.04</td><td>0.86</td><td>0.91</td><td>0.94</td><td>0.96</td><td>1.01</td></tr></table>

Regression on query click rate in a session (Eqs. 6 and 7) for healthcare search.

<table><tr><td>Parameter</td><td>Mean</td><td>Std Dev</td><td>2.50%</td><td>25%</td><td>50%</td><td>75%</td><td>97.50%</td></tr><tr><td> $b_{31}$  (constant)</td><td>-0.28</td><td>0.05</td><td>-0.37</td><td>-0.31</td><td>-0.28</td><td>-0.25</td><td>-0.18</td></tr><tr><td> $b_{32}$  ( $q$ )</td><td>0.59</td><td>0.10</td><td>0.40</td><td>0.54</td><td>0.60</td><td>0.66</td><td>0.78</td></tr><tr><td> $\sigma_{\nu/3}$ </td><td>0.69</td><td>0.02</td><td>0.65</td><td>0.67</td><td>0.69</td><td>0.70</td><td>0.72</td></tr></table>

## 5.1. Theoretical implications

We <sup>fi</sup>nd that users tend to submit more queries and have higher click rate in a session for healthcare than for information security and other topics. And query click rate of an information security session is the lowest. As we mentioned earlier, compared with the searches on other topics, users' search for healthcare and information security are generally protection motivated with the purpose to assess, mitigate, or prevent some hazard or risk that might directly affect or enhance one's well-being or computer assets [85]. Both topics include an element of vulnerability [41]. Of course while healthcare protection behavior is more focused on the individual well-being, cyber threats are focused on computers that pertain to physical assets. Individuals search for information regarding healthcare so that they can have better diagnostics or treatment (the discourse of hope). And in the case of information security, people search for information to mitigate and combat the harmful effects of threats, be it identity theft or denial of service (the discourse of threat). Therefore in both cases of fear appeals messages, information seekers are more motivated to search for healthcare than for information security related information.

Our results also indicate that users with greater search engine activity level tend to submit more queries in a search session and have a higher query click rate. Active users' increased experience with a search engine may allow them to formulate more questions and help them evaluate responses to questions, as the increased experience reduces the cognitive cost of searching information. Besides, active users may have more knowledge capital, i.e., possess more knowledge on how search engines work and have skills of query formulation to re<sup>fl</sup>ect their intention. Increased experience in information search will guide users to select strategies that may lead to more successful results [4]. The search results returned may be more relevant and have higher utility. Also, experienced individuals are more likely to search for alternative sources for information and be less reliant on the topics [86]. And they could have more queries and higher query click rate in a session.

Estimated parameters for the beta distribution of search engine activity level (q).

<table><tr><td>Parameter</td><td>Mean</td><td>Std Dev</td><td>2.50%</td><td>25%</td><td>50%</td><td>75%</td><td>97.50%</td></tr><tr><td>k</td><td>1.62</td><td>0.03</td><td>1.57</td><td>1.60</td><td>1.62</td><td>1.64</td><td>1.68</td></tr><tr><td>m</td><td>2.30</td><td>0.05</td><td>2.22</td><td>2.27</td><td>2.30</td><td>2.33</td><td>2.40</td></tr></table>

T-statistics on the difference between regression coef<sup>fi</sup>cients of constant term $( a _ { i 1 } ,$ i = 1,2,3).

<table><tr><td colspan="4">Regression on mean query number in a session</td></tr><tr><td></td><td>General  $a_{11}$ </td><td>Information security  $a_{21}$ </td><td>Healthcare  $a_{31}$ </td></tr><tr><td>General  $a_{11}$ </td><td>-</td><td>-0.41</td><td>-7.06**</td></tr><tr><td>Information security  $a_{21}$ </td><td>-</td><td>-</td><td>-6.54**</td></tr><tr><td>Healthcare  $a_{31}$ </td><td>-</td><td>-</td><td>-</td></tr></table>

T-statistics on the difference between regression coef<sup>fi</sup>cients of constant terms $( b _ { i 1 } ,$ $i = 1 , 2 , 3 )$

<table><tr><td colspan="4">Regression on query click rate in a session</td></tr><tr><td></td><td>General  $b_{11}$ </td><td>Information security  $b_{21}$ </td><td>Healthcare  $b_{31}$ </td></tr><tr><td>General  $b_{11}$ </td><td>-</td><td>7.11**</td><td>-7.09**</td></tr><tr><td>Information security  $b_{21}$ </td><td>-</td><td>-</td><td>-14.40**</td></tr><tr><td>Healthcare  $b_{31}$ </td><td>-</td><td>-</td><td>-</td></tr></table>

\* Signi<sup>fi</sup>cant at 0.05, \*\* signi<sup>fi</sup>cant at 0.01.

Finally, we <sup>fi</sup>nd that the effects of search engine activity level on query click rate are strong for information security, but weak for healthcare. As argued above, higher knowledge capital has more of an impact on information security search because of the commonality of the domain in contrast to healthcare search. The knowledge would facilitate interpretation of new external information that is garnered through search more for information security than for healthcare. It is quite likely that greater knowledge capital (resulting from greater search engine activity) helps in identifying speci<sup>fi</sup>c and purposeful goals for which information acquisition is necessary and this may be more so in the case of information security related search than for healthcare. An alternate conjecture is that it is entirely possible that greater knowledge capital regarding search results in more knowledge regarding the risks of information security as compared to healthcare risk. In the arena of healthcare risk, information seekers are prone to optimism bias [3] and therefore feel the risks of health security is less in their case, resulting in less information search in the case of health security than computer security. These will have to be studied in future research.

T-statistics on the difference between regression coef<sup>fi</sup>cients of search engine activity level (q) $( a _ { i 2 } , i = 1 , 2 , 3 )$ .

<table><tr><td colspan="4">Regression on mean query number in a session</td></tr><tr><td></td><td>General  $a_{12}$ </td><td>Information security  $a_{22}$ </td><td>Healthcare  $a_{32}$ </td></tr><tr><td>General  $a_{12}$ </td><td>-</td><td> $-3.37^{**}$ </td><td> $-1.53$ </td></tr><tr><td>Information security  $a_{22}$ </td><td>-</td><td>-</td><td> $1.52$ </td></tr><tr><td>Healthcare  $a_{32}$ </td><td>-</td><td>-</td><td>-</td></tr></table>

T-statistics on the difference between regression coef<sup>fi</sup>cients of activity level (q) (b , i = 1,2,3).

<table><tr><td colspan="4">Regression on query click rate in a session</td></tr><tr><td></td><td>General  $b_{12}$ </td><td>Information security  $b_{22}$ </td><td>Healthcare  $b_{32}$ </td></tr><tr><td>General  $b_{12}$ </td><td>-</td><td> $-2.65^{**}$ </td><td> $2.51^{**}$ </td></tr><tr><td>Information security  $b_{22}$ </td><td>-</td><td>-</td><td> $5.28^{**}$ </td></tr><tr><td>Healthcare  $b_{32}$ </td><td>-</td><td>-</td><td>-</td></tr></table>

\* Signi<sup>fi</sup>cant at 0.05, \*\* signi<sup>fi</sup>cant at 0.01

Information Security

Healthcare

General

![](/api/attachments/B4Q53PAU/fulltext/images/64e947433b4485e99cea362ff10c139f70d20407de0f164020085deebdfa2f99.jpg)  
Fig. 2. Effects of search engine activity level: number of users (bottom), estimated mean number of queries in a session (middle, with 95% con<sup>fi</sup>dence bounds in dotted lines), and estimated mean query click rate in a session (top, with 95% con<sup>fi</sup>dence bounds in dotted lines)

Our study also contributes to information security literature which has been using theories stemmed from healthcare literature to explain individuals' reaction to information security threats. While perceived risks could impact peoples' search behavior, our study suggests that the magnitude of the impact varies and it depends on the topics searched and users' search engine usage. Therefore, IS researcher should pay attention to the context and contingencies when applying healthcare literature to information security studies.

## 5.2. Practical implications

Our study has implications to both speci<sup>fi</sup>c risk information search and search engine design in general. One implication of the study for the design of search engines related to risk information search is that the designers should differentiate different topics when suggesting relevant queries and listing the most relevant results (This has been proposed in the design of ranking search results and has already started happening in the arena of search engines for mobile devices). Our results show that search pattern for different risk information varies. For healthcare, users tend to submit more queries and have a higher a click rate. But for information security users tends to submit more and click less. Thus, when returning the results, search engines could maximize the diversity of the results matching the query for healthcare search and expose users to different opinions. For information security, search engines should pursuit the accuracy of the information listed with limited expected interaction.

Our second implication for the design of search engines is that the designers may pro<sup>fi</sup>le users based on their search engine activity level (i.e., tendency to use a search engine in a typical day). Users' search engine activity level may be inferred based on their observed frequency of search engine visitations as shown in our study. From our results we can see that higher search engine activity level leads to more search at the session level. Further, search engine activity level exerts different impact on the search for different topics. Users with different search engine activity level may have different information needs and search strategies. Thus for search engines it is important to understand the behavioral difference between active users and less active users to maximize their interactivity with search engines for different search topics. While search engines could observe more activity from active users in their transaction logs, proper weights should be assigned to less active users when analyzing user behavior so that the behavior of less active users will not be overshadowed by that of active users. It may be also important for search engines to quest for what hinders the less active users' search.

Our third implication for the design of search engines is that search engines should always strive to reduce the cognitive cost of search in order to maximize users' interactivity. Search engines may consider providing an alternative way to organize result pages which show less but categorized links in order to reduce users' information load and facilitate them to locate their desired results. Search engines may provide services and tools to better <sup>fi</sup>t users' speci<sup>fi</sup>c needs and the searched topics. Procedural search knowledge [7] may be implemented to help novice users and guide users through the search retrieving comprehensive information for such topics as healthcare.

Finally, our model for session length and query click rate can be used to compare the interactivity of different search algorithms and technologies. New search engine techniques have been developed to help users quickly locate relevant resources. Those techniques include but are not limited to clustering the search results by topics [46,83], personalizing the search results based on user preference and behavioral history [12, 15], and topic speci<sup>fi</sup>c search engines focusing on a speci<sup>fi</sup>c domain of information (e.g., MEDLINE, ZoomInfo, CMedPort [91]). The effectiveness of those techniques and designs may be compared by analyzing session lengths and query click rate that users have when using these technologies and designs and searching for the same topic.

## 5.3. Future research and conclusion

There are a number of possible directions that can be explored in future studies. First, we used 2006 search engine log in this study. As search engine technology and the number of online resources change rapidly, users' search pattern may change as well. Future research can test our hypotheses using more recent data. However, previous studies have found users' healthcare information search and information security search is relatively constant and predictable in terms of queries submitted and search volume [27, 85]. Second, we identify the topics of search sessions by using ten keywords from various sources. A larger set of keywords for topic identi<sup>fi</sup>cation purposes could be used in future studies. Third, the frequency of search for different topics in the total population may vary. In this study we do not incorporate this aspect. The effects of such variations on user search behavior may be explored in future. Besides user characteristics as we have discussed above, topic-related characteristics over the Internet (for example, availability/dispersion of the facts in different topics, information quality of different topics) may also affect user search behavior, and consequently result in different session length for different topics. These factors need to be further studied using <sup>fi</sup>eld experiments. In addition, it may also be interesting to explore learning effects that spill over across multiple sessions by tracing user search behavior in a period. Fourth, an experienced user may reach target pages by ‘right clicking’ on the search results, and this kind of right-clicking might have increased further in the recent times due to the introduction of browsers with tabs. Right-clicking and using of tabs may affect users' search pattern. However, based on the search log that we have access to, we cannot differentiate between these two actions. How right-clicking and using of tabs affects search patterns needs to be explored in future. Finally, huge amount of search engine data are collected and stored by search engine providers. While the analysis of search engine data could be used to improve the accuracy of search engine algorithm and the understanding of users' behavior, it also raises concerns on information privacy. Future research could examine how the use of search engine data could bene<sup>fi</sup>t users while protecting their privacy.

To summarize, our study explores the impact of search topics and search engine activity level on session length and query click rate, with a real-life search engine log. We discover that Inverse Gaussian distribution provides a good characterization of the distribution of session lengths, and search topic and search engine activity level are important factors in<sup>fl</sup>uencing search pattern in terms of session length and query click rate. We discuss the theoretical implications of the study for information search behavior and practical implications for search engine design.

## Acknowledgements

The authors thank Dr. Bernardo Huberman and anonymous referees for their comments that have greatly improved the paper. We thank the editor-in-chief for his encouragement. The work of the <sup>fi</sup>rst author has been supported by summer research grant from UT Arlington College of Business. The research of the third (correspondent) author has been funded in part by NSF under grant 0916612 and by Sogang Business School's World Class University Project (R31-20002) funded by the Korea Research Foundation. The usual disclaimer applies.

## References

[1] C.L. Anderson, R. Agarwal, Practicing safe computing: a multimethod empirical examination of home computer. User Security Behavioral Intentions, MIS Quart 34 (3) (2010).

[2] M. Arlitt, Characterizing Web user sessions, ACM SIGMETRICS Performance Evaluation Review 28 (2) (2000).

[3] D.A. Armor, S.E. Taylor, When predictions fail: the dilemma of unrealistic optimism, in: T. Gilovich, D. Grif<sup>fi</sup>n, D. Kahneman (Eds.), Heuristics and biases: The psychology of intuitive judgment (Cambridge, Cambridge University Press, UK, 2002.

[4] A. Aula, K. Nordhausen, Modelling successful performance in Web searching, Journal of The American Society For Information Science And Technology 57 (2006).

[5] R. Baeza-Yates, C. Hurtado, M. Mendoza, G. Dupret, Modeling user search behavior, the Third Latin American Web Congress, 2005, Washington,.

[6] S.K. Bhavnani, Domain-speci<sup>fi</sup>c search strategies for the effective retrieval of healthcare and shopping information, in CHI 2002, Minneapolis, Minnesota, 2002

[7] S.K. Bhavnani, C.K. Bichakjian, T.M. Johnson, R.J. Little, F.A. Peck, J.L. Schwartz, V.J. Strecher, Strategy hubs: domain portals to help <sup>fi</sup>nd comprehensive information Journal of The American Society For Information Science And Technology 57 (1) (2006).

[8] S.K. Bhavnani, F.A. Peck, Scatter matters: regularities and implications for the scatter of healthcare information on theWeb, Journal of the American Society for Information Science and Technology 61 (4) (2010).

[9] P.H. Bloch, D.L. Sherrell, N.M. Ridgway, Consumer search: an extended framework, Journal of Consumer Research 13 (June) (1986).

[10] O. Brafman, R. Brafman, Click: The Magic of Instant Connections, Broadway Business, New York, 2010.

[11] S. Brooks, A. Gelman, Alternative methods for monitoring convergence of iterative simulations, Journal of Computational and Graphical Statistics 7 (1998).

[12] G.J. Browne, M.G. Pitts, J.C. Wetherbe, Cognitive stopping rules for terminating information search in online tasks, MIS Quarterly 31 (1) (2007).

[13] M. Chau, X. Fang, O.R.L. Sheng, Analysis of the query logs of a website search engine, Journal of The American Society For Information Science And Technology 56 (13) (2005).

[14] M. Chau, X. Fang, O.R.L. Sheng, What are people searching on government websites? Communications of the ACM 50 (4) (2007).

[15] D.-Y. Choi, Personalized local Internet in the location-based mobile web search, Decision Support Systems 43 (2007)

[16] H. Choi, H. Varian, Predicting Initial Claims for Unemployment Bene<sup>fi</sup>ts, Google Inc, 2009.

[17] H. Choi and H. Varian, Predicting the Present with Google Trends. Google Research Blog http://googleresearch.blogspot.com/2009/04/predicting-present-with-googletrends.html. Available at SSRN: http://ssrn.com/abstract=1659302 (April 2, 2009)

[18] P.H.B. Chou, A.V. Wister, From cues to action: information seeking and exercise self-care among older adults managing chronic illness, Canadian Journal on Aging 24 (4) (2005).

[19] Comscore, Online Health Information Category Grows 12 Percent in Q1 2007 Versus Last Year to More Than 55 Million Visitors per Month, comScore Networks (May 21 2007).

[20] M. Copeland, Relation of consumers' buying habits to marketing methods, Harvard Business Review 1 (3) (1923).

[21] A.R. Dennis, N.J. Taylor, Information foraging on the web: the effects of “acceptable” Internet delays on multi-page information search behavior, Decision Support Systems 42 (2006).

[22] A.K. Dixit, R.S. Pindyck, Investment Under Uncertainty, Princeton University Press, Princeton NJ, 1994.

[23] M. Ettredge, J. Gerdes, G. Karuga, Using web-based search data to predict macroeconomic statistics, Communications of the ACM 48 (1) (2005).

[24] G. Eysenbach, J. Powell, O. Kuss, E.-R. Sa, Empirical studies assessing the quality of health information for consumers on the World Wide Web: a systematic review Journal of the American Medical Association 287 (20) (2002)

[25] D. Fallows, Search Engine Use, Pew Internet & American Life Project, Washington, D.C., 2008

[26] J.L. Folks, R.S. Chhikara, The Inverse Gaussian Distribution and its Statistical Application - A Review, J. R. Statist. Soc. B 40 (3) (1978).

[27] J. Ginsberg, M.H. Mohebbi, R.S. Patel, L. Brammer, M.S. Smolinski, L. Brilliant, Detecting in<sup>fl</sup>uenza epidemics using search engine query data, Nature 457 (19) (2008).

[28] L.A. Gordon, M.P. Loeb, W. Lucyshyn, R. Richardson, CSI/FBI Computer Crime and Security Survey, Computer Security Institute, 2006.

[29] R. Grif<sup>fi</sup>n, S. Dunwoody, K. Neuwirth, Proposed model of the relationship of risk information seeking and processing to the development of preventive behaviors\* 1, Environmental Research 80 (2) (1999).

[30] R. Grif<sup>fi</sup>n, K. Neuwirth, S. Dunwoody, J. Giese, Information suf<sup>fi</sup>ciency and risk communication, Media Psychology 6 (1) (2004).

[31] R.J. Grif<sup>fi</sup>n, S. Dunwoody, K. Neuwirth, Proposed model of the relationship of risk information seeking and processing to the development of preventive behaviors, Environmental Research Section A 80 (1999).

[32] C. Holscher, G. Strube, Web search behavior of Internet experts and newbies, Computer Networks 33 (2000).

[33] B. Huberman, P. Pirolli, J. Pitkow, R. Lukose, Strong regularities in world wide web sur<sup>fi</sup>ng, Science 280 (1998).

[34] B. Jansen, U. Pooch, A review of web searching studies and a framework for future research, Journal of the American Society for Information Science and Technology 52 (3) (2001).

[54] S. Park, J.H. Lee, H.J. Bae, End user searching: a Web log analysis of NAVER, a Korean Web search engine, Library and Information Science Research 27 (2) (2005).

[35] B. Jansen, A. Spink, An analysis of Web searching by European AlltheWeb. com users, Information Processing and Management 41 (2) (2005).

[36] B.J. Jansen, A. Spink, An analysis of Web information seeking and use: Documents retrieved versus documents viewed, the 4th International Conference on Internet Computing, 2003.

[37] B.J. Jansen, A. Spink, How are we searching the World Wide Web? A comparison of nine search engine transaction logs, Information Processing and Management 42 (2006) (2006).

[38] B.J. Jansen, A. Spink, C. Blakely, S. Koshman, De<sup>fi</sup>ning a Session on Web Search Engines, Journal of The American Society For Information Science And Technology 58 (6) (2007).

[39] E.J. Johnson, S. Bellman, G.L. Lohse, Cognitive lock-in and the power law of practice, Journal of Marketing 67 (April) (2003).

[40] E.J. Johnson, W.W. Moe, P.S. Fader, S. Bellman, G.L. Lohse, On the depth and dynamics of online search behavior, Management Science 50 (3) (2004).

[41] A.C. Johnston, M. Warkentin, Fear appeals and information security behaviors: an empirical study, MIS Quarterly 34 (1) (2010).

[42] D. Kelly, C. Cool, The Effects of Topic Familiarity on Information Search Behavior, in the 2nd ACM/IEEE-CS joint conference on Digital libraries, Portland, Oregon, 2002.

[43] L.R. Klein, G.T. Ford, Consumer search for information in the digital age: an empirical study of prepurchase search for automobiles, Journal of Interactive Marketing 17 (3) (2003).

[44] S.A. Knight, A. Spink, Toward a Web search information behavior model, Information Science and Knowledge Management 14 (2008).

[45] S. Kulviwat, C. Guo, N. Engchanil, Determinants of online information search: a critical review and assessment, Internet Research 14 (3) (2004).

[46] N. Kumar, K.R. Lang, Do search terms matter for online consumers? The interplay between search engine query speci<sup>fi</sup>cation and topical organization, Decision Support Systems 44 (2007).

[47] H. Liang, Y. Xue, Avoidance of information technology threats: a theoretical perspective, MIS Quarterly 33 (1) (2009).

[48] M. Limayem, S. Hirt, C. Cheung, How habit limits the predictive power of intention: the case of information systems continuance, MIS Quarterly 31 (4) (2007).

[49] S. Milne, P. Sheeran, S. Orbell, Prediction and intervention in health related behavior: a meta analytic review of protection motivation theory, Journal of Applied Social Psychology 30 (1) (2000).

[50] S. Moorthy, B.T. Ratchford, D. Talukdar, Consumer information search revisited: theory and empirical analysis, Journal of Consumer Research 23 (4) (1997).

[51] K. Neuwirth S. Dunwoody, R.I. Griffin, Protection motivation and risk communication, Risk Analysis 20 (5) (2000).

[52] B.-Y. Ng, A. Kankanhalli, Y.C. Xu, Studying users' computer security behavior: a health belief perspective, Decision Support Systems 46 (4) (2009).

[53] S. Oyama, T. Kokubo, T. Ishida, Domain-speci<sup>fi</sup>c web search with keyword spices, IEEE Transactions on Knowledge and Data Engineering 16 (1) (2004).

[55] G. Pass, A. Chowdhury, C. Torgeson, A Picture of Search, the First International Conference on Scalable Information Systems (INFOSCALE '06) (Hong Kong, 2006.

[56] P. Pirolli, Computational Models of Information Scent-<sup>fl</sup>owing in a Very Large Browsabble Text Collection, CHI 1997 Conference on Human Factors in Computing Systems 1997 (Atlanta GA

[57] P. Pirolli, Information Foraging Theory: Adaptive Interaction with Information, Oxford University Press, New York, 2007

[58] P. Pirolli, S. Card, Information foraging in information access environments, Conference on Human Factors in Computing Systems, 1995, (Denver, Colorado, United States.

[59] P. Pirolli, S. Card, Information Foraging, Psychological Review 106 (4) (1999).

[60] S. Prentice-Dunn, R.W. Rogers, Protection motivation theory and preventive health: beyond the health belief model, Health Education Research 1 (3) (1986).

[61] S. Putrevu, B.T. Ratchford, A model of search behavior with an application to grocery shopping, Journal of Retailing 73 (4) (1997).

[62] H. Raiffa, Decision Analysis, Reading, MA, Addison-Wesley, 1968.

[63] B.T. Ratchford, Cost–bene<sup>fi</sup>t models for explaining consumer choice and information seeking behavior, Management Science 28 (2) (1982).

[64] R. Richardson, CSI Computer Crime and Security Survey, Computer Security Insti tute, 2007.

[65] R. Rogers, Cognitive and physiological processes in fear appeals and attitude change: A revised theory of protection motivation, in: J. Cacioppo, R. Petty (Eds.), Social psychophysiology, Guilford, 1983.

[66] L.J. Savage, The Foundations of Statistics, , 1954 (New York, Dover,.

[67] V. Seshadri, The Inverse Gaussian Distribution: A Case Study in Exponential Families Oxford Science Publications New York 1993

[68] D.J. Severtson, L.C. Baumann, R.L. Brown, Applying a health behavior theory to explore the in<sup>fl</sup>uence of information and experience on arsenic risk representations, policy beliefs, and protective behavior, Risk Analysis 26 (2) (2006).

[69] C. Silverstein, M. Henzinger, H. Marais, M. Moricz, Analysis of a very large web search engine query log, SIGIR Forum 32 (1) (1999).

[70] H.A. Simon, The Science of the Arti<sup>fi</sup>cial, MA, MIT Press, Cambridge, 1981

[71] M.D. Slater, D.E. Zimmerman, Descriptions of web sites in search listings: a potential obstacle to informed choice of health information, American Journal of Public Health 93 (8) (2003).

[72] V.K. Smith, W.H. Desvousges, J.W. Payne, Do risk information programs promote mitigating behavior? Journal of Risk and Uncertainty 10 (1995)

[73] A. Spink, B. Jansen, D. Wolfram, T. Saracevic, From e-sex to e-commerce: Web search changes, Computer 35 (3) (2002).

[74] A. Spink, B.J. Jansen, Web Search: Public Searching of the Web, Springer, Dordrecht, 2004.

[75] A. Spink, D. Wolfram, M. Jansen, T. Saracevic, Searching the web: the public and their queries, Journal of the American Society for Information Science and Technology 52 (3) (2001).

[76] G.J. Stigler, The economics of information, Journal of Political Economy 72 (1961).

[77] M. Sutrop, Ethical Issues in Governing Biometric Technologies, in: A. Kumar, D. Zhang (Eds.), Ethics and Policy of Biomentrics, Springer, 2010.

[78] B. Tancer, Click: What Millions of People Are Doing Online and Why it Matters, NY, Hyperion, New York, 2008.

[79] tpdelE.G. Toms, L. Freund, R. Kopak, J.C. Bartlett, The Effect of Task Domain on Search, the 2003 conference of the Centre for Advanced Studies on Collaborative research, 2003.

[80] M. Turner, R. Rimal, D. Morrison, H. Kim, The role of anxiety in seeking and retaining risk information: testing the risk perception attitude framework in two studies, Human Communication Research 32 (2) (2006)

[81] M.C.K. Tweedie, Statistical properties of inverse Gaussian distributions. I, Annals of Mathematical Statistics 28 (2) (1957).

[82] S. Venkatsubramanyan, T.R. Hill, An empirical investigation into the effects of web search characteristics on decisions associated with impression formation, Information Systems Frontiers 12 (2010)

[83] S. Venkatsubramanyan, J. Perez-Carballo, Techniques for organizing and presenting search results: a survey, Journal of Information Science and Technology 4 (2) (2007).

[84] A. Wald, On cumulative sums of random variables, Annals of Mathematical Statistics 15 (3) (1944).

[85] J. Wang, N. Xiao, H.R. Rao, Drivers of information security search behavior: an investigation of network attacks and vulnerability disclosures, ACM Transactions on Management Information Systems 1 (1) (2010).

[86] M.R. Ward, M.J. Lee, Internet shopping, consumer search and product branding, The Journal of Product and Brand Management 9 (1) (1999).

[87] N.D. Weinstein, Testing four competing theories of health-protective behavior, Health Psychology 12 (4) (1993).

[88] K. Witte, M. Allen, A meta-analysis of fear appeals: implications for effective public health campaigns, Health Education & Behavior 27 (5) (2000).

[89] D. Wolfram, P. Wang, J. Zhang, Identifying Web search session patterns using cluster analysis: a comparison of three search environments, Journal of The American Society For Information Science And Technology 60 (5) (2009).

[90] M.L. Ybarra, M. Sumanb, Help seeking behavior and the Internet: a national survey, International Journal of Medical Informatics 75 (1) (2006).

[91] Y. Zhou, J. Qin, H. Chen, CMedPort: an integrated approach to facilitating Chinese medical information seeking, Decision Support Systems 42 (2006)

Jingguo Wang is an Assistant Professor of Information Systems. He graduated from SUNY-Buffalo. His work has been published in Information Systems Research, Journal of Management Information Systems, ACM Transactions, IEEE Transactions, European Journal of Operational Research, Decision Support Systems, among others, and received best paper awards at AMCIS and the International Conference on Internet Monitoring and Protection. His current research interests are in the areas of cybercrime and information security, information search, and decision making.

Nan Xiao is a Ph.D. candidate in the Department of Management Science and Systems at University at Buffalo. His research interests include information security and healthcare information systems. His work has been published at ACM Transactions on Management Information Systems and Decision Support Systems and was presented at national and international conferences such as International Conference on Information Systems (ICIS) and Americas Conference on Information Systems(AMCIS)

H. R. Rao (MIS, SUNY @Buffalo) graduated from Purdue. He has edited four books including “Information Assurance in Financial Services (Idea Group, 2007)”. He has authored or co-authored more than 150 technical papers, and has received best paper and best paper runner up awards at AMCIS, ICIS and ISR. He has received research funding from NSF and DoD. He was a Fulbright fellow in 2004. He is the recipient of the 2007 SUNY Chancellor's award for excellence. He is currently SUNY Distinguished Service Professor of MIS at UB and WCU Visiting Professor of SSME at Sogang University, S. Korea.
