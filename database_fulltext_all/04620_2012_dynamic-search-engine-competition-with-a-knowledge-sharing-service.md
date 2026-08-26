---
otero_id: 4620
otero_key: "HTCC5SWM"
title: "Dynamic search engine competition with a knowledge-sharing service"
authors: "Kihoon Kim; Edison T.S. Tse"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.10.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamic search engine competition with a knowledge-sharing service

Kihoon Kim <sup>a,</sup>⁎, Edison T.S. Tse <sup>b</sup>

<sup>a</sup> Korea University Business School, Republic of Korea

<sup>b</sup> Management Science and Engineering, Stanford University, United States

## a r t i c l e i n f o

Article history: Received 31 March 2010 Received in revised form 19 September 2011 Accepted 2 October 2011 Available online 7 October 2011

Keywords: Differential game Network economics Economics of IS Competitive impacts of IS Electronic commerce

## a b s t r a c t

This research investigates how an inferior search engine can impact its competition with a superior search engine by introducing a knowledge-sharing service. Speci<sup>fi</sup>cally, we model the dynamic competition between an inferior search engine with a knowledge-sharing service and a pure superior search engine. We show that the degree to which the knowledge-sharing service helps the inferior search engine to enlarge its market share increases as the amount of online content decreases and the complexity of searchers' questions increases. We also <sup>fi</sup>nd that the inferior search engine is generally advised to close its database of answers for more market share.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Ever since its <sup>fi</sup>rst appearance, Google has been a leading search engine in both the US and Europe; however, it has little market share in South Korea. According to a press release from comScore,<sup>1</sup> Google-related sites had a 63.1% market share in the US in October 2008 and a 79.2% share in Europe in July 2008.<sup>2</sup> In the South Korean search engine market, Google had less than a 2% market share in July 2007; the Korean portal Naver was the leader with a 77% market share.<sup>3</sup> Both Google and Naver also provide non-search services such as e-mail and news services, but their online users' choice of search engines can be primarily determined by the search capabilities of the search engines rather than by the other services [9,10]. If it is taken as a given that Google's search technology is superior to Naver's search technology, then this huge difference between Google's market shares in the US and Europe and that in South Korea raises a question: Why has Naver so strikingly dominated Google in the Korean search engine market?<sup>4</sup>

One answer lies in Naver's knowledge-sharing service called Knowledge-iN. Knowledge-iN enables its members to share their knowledge by freely asking and answering questions. A 2007 New York Times article indicates that Korean searchers generally visit Naver to search the Internet as well as its database of answers when they have questions.<sup>5</sup> Furthermore, Naver's Knowledge iN receives an average of 44,000 questions and 100,000 answers each day, which contributes to Naver's success as the world's <sup>fi</sup>fth-largest portal.<sup>6</sup> One reason for Naver's success is undoubtedly Naver's policy of keeping its database of answers closed to queries from other search engines. This policy effectively restricts Google's usefulness in the Korean market since Google cannot provide its users with any information from Naver's Knowledge-iN. Given that Korean Internet users generally want to search information in Korean, Naver's closed and large database of answers has attracted much traf<sup>fi</sup>c to Naver due to the fact that web content in Korean is limited.

In the US, Google's prime competitor Yahoo also has a successful knowledge-sharing service. But, unlike the situation with Naver, the presence of Yahoo's knowledge-sharing service has not stopped Google from obtaining a greater share of the US search engine market. Although Yahoo Answers had obtained 60 million users and 160 million answers worldwide one year after its launch in December 2005,<sup>7</sup> and it had a 74% market share in the US online knowledge-sharing market in

March 2008,<sup>8</sup> Google's market share in the US search engine market increased from 55.8% in January 2007 to 58.7% in February 2008.<sup>9</sup>

In contrast to Naver's closed-database policy, Yahoo keeps its database of answers open to outside search queries; in fact, its open-database policy induces a fraction of Google users to visit Yahoo Answers when their search results in Google show data from Yahoo Answers. Hence even when Google users intend to only visit Google for their search, they may continue to visit Yahoo through Yahoo Answers. By not restricting its database to its own searchers, Yahoo gains the bene<sup>fi</sup>t of indirectly promoting multihoming behavior of search customers. (In this context, multihoming refers to the searchers' tendency to visit multiple search engines.) At the same time, this open policy helps Google access more content (from Yahoo Answers) on the Internet.

To investigate how an additional knowledge-sharing service impacts the competitive edge of an inferior search engine, we dynamically model the competition between the inferior search engine with the knowledge-sharing service and a superior search engine without a knowledge-sharing service. Our dynamic model re<sup>fl</sup>ects the searchers' myopic attitude towards choosing a search engine based on its current search capability. Additionally, potential answerers can decide whether to join the knowledge-sharing service after reading posted questions and determining whether they are interested in them. Advertisers may choose a search engine by considering how many users currently use the service. These players' myopic tendencies are expected since the cost of changing their main search engine can be negligible.

Speci<sup>fi</sup>cally, we develop a differential game model that describes the competition between the inferior search engine with the knowledgesharing service and the superior search engine. This setting agrees well with the current market situations in the US and South Korea: Naver and Yahoo, which are inferior to Google, provide knowledgesharing services, but Google does not. In our differential game model, two competing search engines maximize their discounted pro<sup>fi</sup>ts over an in<sup>fi</sup>nite horizon; their main source of revenue is advertising (they have no membership fees) and they have periodic membership maintenance costs. The parameters we consider are the amount of web content, the policy of keeping the database of answers closed, the characteristics of the searchers' inquiries, and the effects of advertising on users. By <sup>fi</sup>nding an open-loop Nash equilibrium of the differential game between these two search engines, we investigate the conditions under which the inferior search engine with a knowledge-sharing service will outperform the superior pure search engine, as well as when the inferior search engine should keep its database of answers closed so it can obtain a greater market share.

We <sup>fi</sup>nd that the degree to which the knowledge-sharing service helps the inferior search engine compete better increases as the amount of online content decreases. In other words, when there is a small amount of online content, the inferior search engine generally wins over the superior search engine as a result of the former's knowledge-sharing service. However, when there is an abundant amount of online content, the superior search engine generally wins the game. Given the existence of a large amount of online content in English, and assuming that Google continues to provide better search results than Yahoo, we predict that Yahoo Answers will not help Yahoo attract more searchers as much as Naver's KnowledgeiN helps them in the Korean search engine market. In addition, the degree to which the inferior search engine can increase its market share by making a database of answers unavailable to outside queries also increases as the amount of online content decreases: our numerical analysis shows a 10–15% increase in the market share of the inferior search engine when online content is limited, but it shows only a

1–2% increase when online content is abundant. Therefore, in the US, Yahoo is unlikely to signi<sup>fi</sup>cantly increase its market share by closing its database of answers.

Our most important discovery is that the inferior search engine is advised to close its database of answers to obtain a greater market share if its search technology is not far behind that of the superior pure search engine. This implies that the degree to which an open database of answers helps the superior pure search engine attract searchers is larger than the degree to which it helps the inferior search engine do so. Thus, though Naver's closed policy may decrease the welfare of searchers,<sup>10</sup> Naver seems to have chosen the right strategy of defending its leading position in the South-Korean search engine market.

The rest of the paper proceeds as follows: Section 2 provides a review of the relevant literature on dynamic search engine competition. Section 3 introduces our differential game model, and Section 4 shows under what conditions and to what degree the search engine with low technology can bene<sup>fi</sup>t from its knowledge-sharing service. Finally, Section 5 summarizes the results and their strategic implications for practitioners.

## 2. Literature review

In this section, we provide a review of relevant literature on a dynamic two-sided-market price competition and a search engine competition. In this paper, we view a search engine as a two-sided<sup>11</sup> platform that connects searchers and information on the Internet. Because information on the Internet is made available by online content providers, a search engine indirectly connects searchers and online content providers. Thus, a larger number of online content providers attract more searchers and vice versa. In addition, we model the dynamic competition between two heterogeneous search engines: one is a pure search engine and the other is a search engine with an online knowledge-sharing service. The knowledge-sharing service of the latter search engine is also a two-sided platform: one side contains searchers and the other side contains answerers [5]. Thus, more answerers attract more questioners and vice versa. Because we model a dynamic competition between these heterogeneous two-sided platforms, previous work on both topics—dynamic two-sided market competition and search engine competition—provide the theoretical foundation for our paper.

Few dynamic two-sided-market price competition models exist [5,8,13]; to our knowledge, our model is the <sup>fi</sup>rst to investigate the dynamic competition between two heterogeneous search engines from a two-sided market point of view. [8] consider a price competition between two platforms; they <sup>fi</sup>nd that one platform will take all when potential members tend to join only one platform. To simulate the impact of the singlehoming tendency of members on competition, they employ an exogeneous parameter called the singlehoming index. In contrast, our model uses an endogenous singlehoming index that periodically updates the tendency of searchers to visit a single search engine according to the search engine's capability of answering the searchers' questions. We believe this endogeneous singlehoming index is designed to re<sup>fl</sup>ect a myopic decision of searchers of whether to visit multiple search engines based on the search engines' relative search capabilities. Given the endogeneous degree of singlehoming, our recommendation that an inferior search engine should close its database of answers for more market share partially agrees with their conclusion that a high degree of singlehoming leads to a single-platform-take-all situation: as the inferior search engine makes the database of answers proprietary, it has a higher degree of singlehoming in our model. [5] analyze the competition between two knowledge-sharing platforms,<sup>12</sup> discovering that a new knowledge-sharing platform is more likely to survive when the database of answers slowly becomes obsolete than when it rapidly becomes obsolete. Again, their model uses an exogeneous singlehoming index; our model employs an endogeneous index that changes as the capability of each search engine evolves over time. Additionally, their model assumes a database of answers is closed to search queries from other knowledge-sharing platforms; our model allows the search engine with a knowledge-sharing service to make its database of answers open, if it decides to do so.

Search engine competition literature has focused on whether incumbent search engines have the <sup>fi</sup>rst-mover advantage [3] and why many search engines coexist [1,11]. Gandal [3] uses the data before Google entered the search engine market, and he suggests that the <sup>fi</sup>rst-mover advantage of incumbent search engines has not been fully sustained over time. Our simulation results agree with this empirical investigation when the search engine market has large searchable online content; however, we show that when online content in a speci<sup>fi</sup>c language is limited, an incumbent search engine with a knowledge-sharing service will maintain its leading position if it makes its database of answers unavailable to a latecomer. [1] empirically <sup>fi</sup>nd that searchers needed to multihome because no search engine can provide all the relevant information for search queries. In accordance with their observation, we adjust the degree of searchers singlehoming according to the probability that a search engine will answer the searchers' questions. [11] provide a static model of competition between an incumbent search engine and a new search engine; they show that multiple search engines will coexist as long as no search engine is perfect. We model the dynamic competition between two heterogeneous search engines, and our simulation results agree well with their conclusion: neither search engine dies out in our simulation. In addition, some search engine literature considers how to improve search quality [2,6,7], but none of these researches deal with the impact of the addition of a knowledge-sharing service on the performance of a search engine. Our study shows a superior search engine may not win over an inferior search engine with a knowledge-sharing service when the latter limits searchable content.

Finally, [4] provide the static analysis of the heterogeneous search engine competition that our model simulates dynamically. They employ the notion of ful<sup>fi</sup>lled expectations equilibrium; with this notion, the searchers' expectations of the success of a knowledge-sharing service are realized. The equilibria of their model thus depend on the rational expectations of searchers, but our dynamic model is based on the myopic tendency of searchers to choose a better search engine during each time period. To a certain extent, their analytical results agree with our simulation results: an inferior search engine should close its database of answers to obtain a greater market share as long as its search technology is not greatly inferior to that of a superior search engine. On the other hand, when the amount of information on the Internet is very large, under their static setting, a somewhat inferior search engine can still win over a superior search engine by introducing a knowledge-sharing service. However, in our dynamic model, the inferior search engine will lose its market share leadership even it starts with a huge membership. In addition, we include some characteristics of the knowledge that searchers seek as factors that in<sup>fl</sup>uence the degree to which a knowledge-sharing service will increase the market share of the inferior search engine.

## 3. Differential game model

In this section, we introduce a differential game model that describes the competition between two search engines: search engine 1 has low technology and a knowledge-sharing service, and search engine 2 has high technology and does not have a knowledge-sharing service. In an open-loop equilibrium of the differential game, each search engine solves its own optimal control problem given the competing search engine's pre-committed advertising fees over time. To describe each search engine's optimal control problem, we present the evolution over time of the states involved in the competition: the membership of each search engine, the size of search engine 1's database of answers, the number of online content providers, and the amount of online content in a speci<sup>fi</sup>c language.

We <sup>fi</sup>rst describe the differential equations that describe the growth of each search engine when search engine 1 makes its database of answers unavailable to queries from search engine 2. When the database of answers is closed, search engine 2 can only index the online content available on the Internet. Thus, when the amount of content on the Internet is limited, search engine 1 can effectively limit the amount of information that search engine 2 can index by closing the database of answers.

## 3.1. When search engine 1's database of answers is closed

Searchers, answerer members, advertisers, and the database of answers are the four sides involved in the growth of search engine 1. Searchers can <sup>fi</sup>nd answers to their questions either by searching the Internet and the database of answers or by posting their questions, which are answered by some answerer members. Answerer members provide their time and knowledge to searchers in return for gaining not only a reputation as experts but potential consulting service opportunities. Advertisers prefer a search engine with a knowledge-sharing service with many searchers and answerer members. Finally, the database of pre-answered questions, if large, may lessen the role of answerer members signi<sup>fi</sup>cantly, weakening the cross-network externalities between searchers and answerer members. [5] describe in detail the crossnetwork externalities between these four sides.

Following [5], we place topics of searchers' questions into four different categories according to two parameters θ and η. θ∈[0,1] describes the degree of complexity of questions on topics, and η∈[0,1] is the rapidity with which the knowledge on topics becomes obsolete. They call η the “knowledge disuse rate.” The degrees of cross-network externalities between the four sides of search engine 1 are affected by these two parameters. For instance, as either θ or η increases, searchers <sup>fi</sup>nd it have more dif<sup>fi</sup>cult to get answers from online content; thus, they rely more on answerers than on existing web content in getting answers to their questions. Examples in each category are shown in Fig. 1, which is an excerpt from [5].

Before we proceed to describe in detail the dynamic growth of each search engine, we introduce the notations for states at time t used in our differential game:

• Q (t): the number of searchers who visit search engine i

• A (t): the number of answerer members of search engine 1's knowledge-sharing service<sup>13</sup>

• N (t): the number of advertisers who use search engine i

• K(t): the number of valuable (non-obsolete) answers on the search engine 1's database

• W(t): the number of online content providers (any entities which generate content on the Internet)

• I(t): the number of valuable (non-obsolete) online content, excluding the search engine 1's database of answers.

The relationships of these states are presented in Fig. 2.<sup>14</sup>

![](/api/attachments/HTCC5SWM/fulltext/images/463dbb1161e8dbe16959524d1d5a5a26d9751f4bd9a0d51707ffab3995bc5c13.jpg)  
Fig. 1. Four categories of topics according to the complexity of questions (θ) and the knowledge disuse rate (η).

We assume the instantaneous membership growth of each search engine during time dt is linear in the difference between the number of potential members and the number of current members [5,8,12]. That is, a fraction of the unful<sup>fi</sup>lled demand joins the search engine during time dt. The fraction is speci<sup>fi</sup>ed by a diffusion rate. For instance, the instantaneous change in the number of searchers who join search engine 1 is described by the following differential equation:

$$
\frac {d Q _ {1} (t)}{d t} = \alpha_ {1} \underbrace {\left\{\underbrace {D (A _ {1} (t) , N _ {1} (t) , I _ {1} (t))} _ {\text { Potential   demand   of   searchers   for   search   engine }} - Q _ {1} (t) \right\}} _ {\text { Unfulfilled   demand   of   searchers   for   search   engine   1   at   time   t }},\tag{1}
$$

where $\alpha _ { 1 }$ refers to a diffusion rate, which is the fraction of the unful-<sup>fi</sup>lled demand by which the growth of searchers of search engine 1 instantaneously changes. I (t) is the amount of online information accessed by search engine 1. The growth of the groups of answerers, advertisers, and online content providers is described by the same form of a differential equation: the growth instantaneously changes by the constant fraction of the unful<sup>fi</sup>lled demand.

Note that as Eq. (1) indicates, we do not assume any positive network effect between searchers. Searchers do not choose a particular search engine because other searchers use it. Instead, they tend to use a particular search engine if it provides satisfactory answers to their queries. Therefore, when the number of searchers of search engine 1 is small, if both the size of the group of answerers and the amount of online information are small, search engine 1 cannot prosper. Similarly, we do not assume any positive network effect within the groups of answerers and online content providers. Otherwise, both search engines 1 and 2 can grow easily and the degree of the competition between them becomes too weak to in<sup>fl</sup>uence their growth.

More searchers will visit search engine 1 if it has more answerer members, more search results, or less advertisement on its site. The growth of searchers who visit search engine 1 is expressed as follows<sup>15</sup>:

$$
\frac {d Q _ {1}}{d t} = \alpha_ {1} \left\{\underbrace {d \frac {b _ {q _ {1} a}}{\delta_ {1}} \sqrt {A _ {1}} + b _ {q _ {1} k} \delta_ {1} \sqrt {I _ {1}} \left(\frac {I _ {1}}{T I}\right) ^ {e _ {q _ {1}}} - d _ {q _ {1}} \sqrt {N _ {1}} \left(\frac {N _ {1}}{N _ {1} + N _ {2}}\right) ^ {e _ {q _ {1}}}} _ {\text { Number   of   potential   searchers   visiting   search   engine   1 }} - Q _ {1} \right\},\tag{2}
$$

where $\alpha _ { 1 } \in ( 0 , 1 ]$ is a diffusion parameter; $\delta _ { 1 }$ is de<sup>fi</sup>ned as $\frac { 1 } { 1 + \theta _ { 1 } }$ and indi-<sup>þ</sup>cates how effective the database of answers is in answering questions of searchers. Recall that $\theta _ { 1 }$ is the average complexity of questions asked on search engine 1. The parameter d represents the searchers' patience in waiting for answers from members of the knowledgesharing service, $b _ { q _ { 1 } a }$ and $b _ { q _ { 1 } k }$ are the degree of bene<sup>fi</sup>ts for searchers from answerer members and the database of answers, respectively, and $d _ { q _ { 1 } }$ refers to the degree of negative effects of advertising on searchers. The two expressions $\left( { \frac { I _ { 1 } } { T \cal { I } } } \right) ^ { e _ { q _ { 1 } } }$ and $\left( \frac { N _ { 1 } } { N _ { 1 } + N _ { 2 } } \right) ^ { e _ { q _ { 1 } } }$ adjust the number of potential searchers visiting search engine 1 by considering search engine 2's search technology and advertisers. I<sub>1</sub> is the amount of online content that search engine 1 can index: $I _ { 1 } = K + s _ { 1 } ( I - \lambda K )$ , and TI is the total amount of online content that either search engine 1 or search engine 2 can index: $T I = K + m a x \{ s _ { 1 } , s _ { 2 } \} ( I - \lambda K ) = K + s _ { 2 } ( I - \lambda K )$ $( \because s _ { 1 } < s _ { 2 }$ by the assumption). The parameters $s _ { 1 } \in [ 0 , 1 ]$ and $s _ { 2 } \in [ 0 , 1 ]$ represent the portions of web content that search engine 1 and 2 can index, respectively. $\lambda \in [ 0 , 1 ] ,$ as a portion of $K ,$ refers to the degree to which the database of search engine 1's knowledge-sharing service overlaps the available information on the Internet excluding that in the database. We assume this overlap portion decreases as questioncomplexity $\theta _ { 1 }$ increases: $\lambda { = } \lambda _ { 0 } \delta _ { 1 }$ , where $\lambda _ { 0 }$ is the overlap portion when $\theta _ { 1 }$ is zero; $e _ { q _ { 1 } }$ is the degree to which potential searchers of search engine 1 visit a single search engine: as this index increases, more searchers tend to use only one search engine. If this index is close to 1, the increase in search engine 2's search technology will lower $\frac { I _ { 1 } } { T I } ,$ decreasing the unful<sup>fi</sup>lled demand of searchers for search engine 1. We call $\frac { I _ { 1 } } { T I }$ search engine 1's information share. This information share is also affected by the size of the knowledge-sharing database: if K is large compared with I, search engine 1's information share will be large. Additionally, when $e _ { q _ { 1 } }$ is high, the negative effects of advertising on searchers' demand for search engine 1 decrease as $N _ { 2 }$ increases.<sup>16</sup>

As mentioned in the Literature Review, the singlehoming index $e _ { q _ { 1 } }$ is de<sup>fi</sup>ned as the probability that the competing search engine 2 will answer questions of searchers:

$$
e _ {q _ {1}} = \delta_ {2} \frac {I _ {2}}{M + I _ {2}},
$$

where $\begin{array} { r } { \delta _ { 2 } = \frac { 1 } { 1 + \theta _ { 2 } } } \end{array}$ is the general simplicity of questions asked on search engine $2 . I _ { 2 }$ <sup>þ</sup>is the amount of online content that search engine 2 can index: $I _ { 2 } = S _ { 2 } I .$ Recall that $\theta _ { 2 } \in [ 0 , 1 ]$ is the complexity of questions asked on search engine 2. MN0 is a large constant that speci<sup>fi</sup>es the size of information needed to answer the simplest questions with a 50% probability. The parameter $e _ { q _ { 1 } }$ endogenously increases as the competing search engine 2 becomes more competent in answering questions of searchers: as search engine 2 becomes more effective in answering questions, more potential searchers of search engine 1 may visit only search engine 2. Similarly, the singlehoming index $e _ { q _ { 2 } }$ of search engine 2 is de<sup>fi</sup>ned as the probability that search engine 1 will answer questions of searchers:

$$
e _ {q _ {2}} = \delta_ {1} \frac {I _ {1}}{M + I _ {1}}.
$$

By assigning this different singlehoming index to each search engine, we can appropriately adjust the potential demand of searchers for each search engine according to its time-varying capability in answering their questions.

More Answerer members join search engine 1's knowledgesharing service when search engine 1 has more searchers and less advertising. The dynamic growth of answerer members is expressed as follows:

![](/api/attachments/HTCC5SWM/fulltext/images/6fc3da38e86aa654dd9ad161994fa8aab236271b8b8d79e91a39c6e729ed199d.jpg)  
Fig. 2. Dynamics of search engines 1 and 2. Note: (+) and (−) represent positive and negative cross-group network effects

$$
\frac {d A _ {1}}{d t} = \beta_ {1} \left\{\underbrace {b _ {a _ {1}} \left(1 - \frac {\delta_ {1} I _ {1}}{M + I _ {1}}\right) \sqrt {Q _ {1}} - d _ {a _ {1}} \sqrt {N _ {1}}} _ {\text { number   of   potential   answerer   members   visiting   search   engine }} - A _ {1} \right\},\tag{3}
$$

where $\beta _ { 1 }$ is the diffusion parameter for answerer members; $b _ { a }$ is the degree of cross-network bene<sup>fi</sup>ts that answerer members receive from answering open questions posted. Note that the cross-network effect of searchers on answer members decreases as searchers are more likely to <sup>fi</sup>nd answers by searching the Internet including the database of answers. The parameter $d _ { a _ { 1 } }$ is the degree of negative cross-network effects of advertising on answerer members.

More advertisers join search engine 1 if it has more searchers and answerer members. The growth of advertisers who join search engine 1 is described as follows

$$
\frac {d N _ {1}}{d t} = \gamma_ {1} \left\{\underbrace {b _ {n _ {1}} \sqrt {Q _ {1} + A _ {1}} \left(\frac {Q _ {1} + A _ {1}}{Q _ {1} + A _ {1} + Q _ {2}}\right) ^ {e _ {n _ {1}}} \frac {R}{R + N _ {1}} - r _ {n _ {1}} p _ {n _ {1}} {} ^ {2} \left(1 - \frac {p _ {n _ {2}} - p _ {n _ {1}}}{p _ {n _ {1}}}\right)} _ {\text { number   of   potential   advertisers   using   search   engine   1 }} - N _ {1} \right\},\tag{4}
$$

where $\gamma _ { 1 }$ is the diffusion parameter for advertisers of search engine 1: $b _ { n _ { 1 } }$ is the degree of cross-network bene<sup>fi</sup>ts for advertisers from reaching searchers and answerer members; $e _ { n _ { 1 } } \in [ 0 , 1 ]$ is a singlehoming index for advertisers of search engine 1, and the term $\left( \frac { Q _ { 1 } + A _ { 1 } } { Q _ { 1 } + A _ { 1 } + Q _ { 2 } } \right)$ is search engine 1's ad-audience share. The larger $e _ { n _ { 1 } }$ is, the more the increase in $Q _ { 2 }$ decreases the unful<sup>fi</sup>lled demand of advertisers for search engine 1. The parameter $r _ { n _ { 1 } }$ refers to the sensitivity of advertisers to a periodic fee $p _ { n _ { 1 } }$ . This sensitivity decreases as the competing search engine 2 increases its adverting fee, which is re<sup>fl</sup>ected by expression $\left( 1 - \frac { p _ { n _ { 2 } } - p _ { n _ { 1 } } } { p _ { n _ { 1 } } } \right)$ . In addition, R is a large positive constant, and $\frac { R } { R + N _ { 1 } }$ implies the limited advertising space on search engine 1's website: the increase in advertising is presumed to decrease the chance that visitors to search engine 1 will see a particular advertisement.

New answers are added to the database of search engine 1's knowledge-sharing service when posted questions are answered by answerer members. The growth of the database of answers is expressed as follows:

$\frac { d K } { d t } = \left( 1 - \frac { \delta _ { 1 } I _ { 1 } } { M + I _ { 1 } } \right)$ : the probability that questions will be posted $\times \frac { A _ { 1 } } { L + A _ { 1 } }$ : the probability that answerer members will answer posted questions 5

$\times \sqrt { Q _ { 1 } }$ : the average number of queries during dt

$- \eta _ { 1 } K$ : the portion of the current database becoming obsolete during dt;

where $L { > } 0$ is a constant, which is the number of answerer members needed for these members to answer open questions with a 50% probability. Recall that the average knowledge disuse rate $\eta _ { 1 } \in [ 0 , 1 ]$ is the average rate at which online content including the answers of the database becomes obsolete.

Search engine 2's dynamics are similar to those of search engine 1, except that search engine 2 does not get its database of answers from a knowledge-sharing service. The dynamic growth of searchers who visit search engine 2 is similar to that of searchers visiting search engine 1, except for the lack of contributions from answerer members:

$$
\frac {d Q _ {2}}{d t} = \alpha_ {2} \left\{\underbrace {b _ {q _ {2}} \delta_ {2} \sqrt {I _ {2}} \left(\frac {I _ {2}}{T I}\right) ^ {e _ {q _ {2}}} - d _ {q _ {2}} \sqrt {N _ {2}} \left(\frac {N _ {2}}{N _ {1} + N _ {2}}\right) ^ {e _ {q _ {2}}}} _ {\text { number   of   potential   searchers   visiting   search   engine   2 }} - Q _ {2} \right\},\tag{6}
$$

where $\alpha _ { 2 } \in ( 0 , 1 ]$ is a diffusion parameter for searchers of search engine 2, and $b _ { q _ { \tilde { z } } }$ represents bene<sup>fi</sup>ts that searchers receive from using search engine $2 ; \ \delta _ { 2 } = \frac { 1 } { 1 + \theta _ { 2 } }$ is the average simplicity of questions: $\theta _ { 2 }$ <sup>þ</sup>is the average complexity of questions asked on search engine 2; $d _ { q _ { 2 } }$ is the degree of price sensitivity of search engine 2 advertisers. Note that $\frac { I _ { 2 } } { T I }$ is called search engine 2's information share.

We assume more online content providers exist when more searchers exist: as more people search the Internet to <sup>fi</sup>nd information, more people or organizations are willing to post some information on the Internet. The growth of online content providers is as follows:

$$
\frac {d W}{d t} = \beta_ {2} \left\{\underbrace {g _ {w} + b _ {w} \sqrt {Q _ {1} + Q _ {2}}} _ {\text { number   of   potential   online   content   providers }} - W \right\},\tag{7}
$$

where $\beta _ { 2 }$ is a diffusion parameter for online content providers; $g _ { w }$ is the minimum potential number of online content providers: the greater the number of Internet users who use a particular language is, the larger $g _ { w }$ is; $b _ { w }$ is the degree of bene<sup>fi</sup>ts that online content providers reap from searchers.

The growth of advertisers joining search engine 2 is the same as that of advertisers joining search engine 1, except that search engine 2 derives none of its growth from answerer members:

$$
\frac {d N _ {2}}{d t} = \gamma_ {2} \left\{\underbrace {b _ {n _ {2}} \sqrt {Q _ {2}} \left(\frac {Q _ {2}}{Q _ {1} + A _ {1} + Q _ {2}}\right) ^ {e _ {n _ {2}}} \frac {R}{R + N _ {2}} - r _ {n _ {2}} p _ {n _ {2}} {} ^ {2} \left(1 - \frac {p _ {n _ {1}} - p _ {n _ {2}}}{p _ {n _ {2}}}\right)} _ {\text { number   of   potential   advertisers   using   search   engine   2 }} - N _ {2} \right\},\tag{8}
$$

where $\gamma _ { 2 }$ is a diffusion parameter for advertisers of search engine $^ { 2 ; }$ $b _ { n _ { 2 } }$ is the parameter for bene<sup>fi</sup>ts that advertisers receive from reaching searchers, and $r _ { n _ { 2 } }$ refers to the degree of price sensitivity of advertisers of search engine $2 ; e _ { n _ { 2 } }$ is a singlehoming index for advertisers of search engine 2.

The amount of online content in a particular language changes as follows:

$$
\frac {d I}{d t} = p \sqrt {W} - \eta_ {2} I,\tag{9}
$$

where p refers to the degree of productivity of online content providers, and $\eta _ { 2 }$ is the average rate at which online content becomes obsolete. Recall that $\eta _ { 2 }$ is called the average knowledge disuse rate of search engine 2.

The revenues of search engines 1 and 2 come from their advertisers, which are assumed to be charged a periodic fee. Thus, given a periodic advertising fee, each search engine can increase its advertisement revenue by having more audiences, which attract more advertisers, as the advertiser-growth differential Eq. (4) indicates. Search engine 1 has both questioners and answerers ad its audiences for advertising, but search engine 2 has only questioners as its advertising audiences. Both search engines periodically incur the costs of maintaining their users (advertising audiences) and advertisers.

Given all these dynamics so far, search engine 1 solves

$$
\begin{array}{l} \max _ {p _ {n _ {1}}} \int_ {0} ^ {\infty} e ^ {- r t} \Big \{- c _ {q _ {1}} Q _ {1} (t) - c _ {a} A (t) + \Big (p _ {n _ {1}} - c _ {n _ {1}} \Big) N _ {1} (t) \Big \} d t \\ s. t. (2) ^ {\sim} (9) \\ Q _ {i} (0) _ {i} = q _ {i 0},   A (0) = a _ {0},   W (0) = w _ {0},   N _ {i} (0) = n _ {i 0},   K (0) = k _ {0}, \\ I (0) = i _ {0} \quad \text { for }    i = 1,   2, \end{array}
$$

and search engine 2 solves

$$
\begin{array}{l} \max _ {p _ {n _ {2}}} \int_ {0} ^ {\infty} e ^ {- r t} \Big \{- c _ {q _ {2}} Q _ {2} (t) + \Big (p _ {n _ {2}} - c _ {n _ {2}} \Big) N _ {2} (t) \Big \} d t \\ s. t. (2) ^ {\sim} (9) \\ \quad Q _ {i} (0) = q _ {i 0}, A (0) = a _ {0}, W (0) = w _ {0}, N _ {i} (0) = n _ {i 0}, K (0) = k _ {0}, \\ \quad I (0) = i _ {0} \quad \text { for } i = 1, 2. \end{array}
$$

$p _ { n _ { i } }$ represents a periodic fee that search engine i charges to advertisers. $c _ { q _ { i } }$ and $c _ { n _ { i } }$ are search engine i's periodic marginal costs of maintaining searchers and advertisers, respectively. $c _ { a }$ is the search engine 1's periodic marginal cost of maintaining its answerer members.

## 3.2. When search engine 1's database of answers is open

When search engine 1 opens its database of answers, search engine 1 helps search engine 2 index more information in return for attracting some searchers who intend to only visit search engine 2, but are indirectly led to search engine 1. Thus, the amount of information that search engine 2 can access increases, and the singlehoming tendency of potential searchers of search engine 1 decreases. All the other modeling details are the same as those when search engine 1 keeps its database of answers open.

When search engine 1 allows its database of answers to be searchable by search engine 2, the amount of online content (I ) that search engine 2 can index increases as follows:

$$
I _ {2} = s _ {2} I + s _ {2} (1 - \lambda) K = s _ {2} \{I + (1 - \lambda) K \}.
$$

Search engine 1 trades off the information stored in its database of answers for a reduction in the singlehoming tendency of its potential searchers: even when a searcher intends to only visit search engine 2, the searcher can visit search engine 1 if search engine 2 provides some answers from the database of search engine 1's knowledgesharing service. The degree to which the database attracts search engine 2 searchers to search engine 1 is assumed to decrease as the ratio of I to (1 λ)K increases. Thus, we decrease $e _ { q _ { 1 } }$ as follows:

$$
e _ {q _ {1}} = \delta_ {2} \frac {I _ {2}}{M + I _ {2}} \times \frac {I}{I + (1 - \lambda) K} = \delta_ {2} \underbrace {\frac {s _ {2} I}{M + s _ {2} I + s _ {2} (1 - \lambda) K}} _ {\text { decreases   as   K   increases }}.
$$

As a result, $\boldsymbol { e } _ { \boldsymbol { q } _ { 1 } }$ decreases as K increases when the database is open to queries from search engine 2.

The reduced singlehoming tendency of potential searchers of search engine 1 implies the increased number of its potential searchers, given the current amount of information that search engine 1 can access, as the search engine 1's searcher-growth differential Eq. (2) indicates. Therefore, when search engine 1 opens its database of answers to search engine 2, search engine 1 can increase its advertising revenue by having more searchers to its site, and correspondingly obtaining more advertisers. That is, the reduced singlehoming tendency of search engine 1 indirectly re<sup>fl</sup>ects search engine 1's additional advertising revenue by allowing searchers to visit search engine 1's knowledge base via a link from their search results at search engine 2.

We can combine two cases—when the database of answers is open and when it is closed—by using the indicator function, which shows the status of the database of answers:

$$
I _ {2} = s _ {2} I + 1 _ {\{o p e n \}} s _ {2} (1 - \lambda) K; e _ {q _ {1}} = \delta_ {2} \frac {s _ {2} I}{M + s _ {2} I + 1 _ {\{o p e n \}} s _ {2} (1 - \lambda) K}.
$$

1 is one when the database of answers is open; $1 _ { \{ o p e n \} }$ is zero when the database of answers is closed.

## 4. Analysis

In this section, we numerically solve for open-loop Nash equilibria of the differential game described in Section 3. Detailed procedures for <sup>fi</sup>nding an open-loop Nash equilibrium for an in<sup>fi</sup>nite-horizon differential game are described in [8]. By <sup>fi</sup>nding stabilized states of open-loop Nash equilibria for the differential game, we examine under what conditions an online knowledge-sharing service will help an inferior search engine to win over a superior pure search engine. Speci<sup>fi</sup>cally, we consider search engine competition in two markets differing in the amount of online content: online content is small for the Korean search engine market and large for the US search engine market. Table 1 shows the default parameter values for the simulation.

## 4.1. Benchmark: competition between two pure search engines

Before we analyze the competition between two heterogeneous search engines, we simulate the competition between two pure search engines: search engine 1 does not have a knowledge-sharing service. To perform the simulation, we use the following parameter values and initial conditions for search engine 1's dynamics: $d = 0 , \ \beta _ { 1 } = 0 , \ \eta _ { 1 } = 1 ; A$ $( 0 ) = 0 , \ : K ( 0 ) = 0 \ :$ . To investigate the impact search engine 1 has on the competition by having a knowledge-sharing service, we use the same initial conditions except A(0) and K(0) as Eqs. (10) and (11) that we employ when search engine 1 has a knowledge-sharing service:

Parameter values for the differential game simulation

<table><tr><td>Parameters</td><td>Values</td></tr><tr><td> $s_{1}, s_{2}$  (search technologies)</td><td>0.4, 0.7</td></tr><tr><td> $e_{n_{i}}$  (singlehoming index for advertisers)</td><td>0 (multihoming) for i = 1, 2</td></tr><tr><td>r (interest rate)</td><td>0.05</td></tr><tr><td> $\alpha_{i}, \beta_{i}, \gamma_{i}$  (diffusion parameters)</td><td>0.5, 0.5, 0.5 for i = 1, 2</td></tr><tr><td> $b_{q_{1}a}, b_{q_{1}k}, b_{a_{1}}, b_{n_{1}}$  (benefit parameters for search engine 1)</td><td>10, 10, 5, 2</td></tr><tr><td> $b_{q_{2}}, b_{w}, b_{n_{2}}$  (benefit parameters for search engine 2)</td><td>10, 5, 2</td></tr><tr><td> $r_{n_{i}}$  (price-sensitivity parameters)</td><td>1 for i = 1, 2</td></tr><tr><td> $d_{q_{1}}, d_{a_{1}}, d_{q_{2}}$  (advertisement-sensitivity parameters)</td><td>0, 0, 0</td></tr><tr><td> $c_{qi}, c_{a}, c_{ni}$  (per-period unit costs)</td><td>0.05, 0.05, 0.05 for i = 1, 2</td></tr><tr><td> $\theta_{i}$  (average complexity of questions)</td><td>0.1 (simple), 0.5 (complex)</td></tr><tr><td> $\eta_{i}$  (average rate of answers becoming obsolete)</td><td>0.005 (slow), 0.01 (fast)</td></tr><tr><td>d (searchers&#x27; patience to wait)</td><td>0.5</td></tr><tr><td> $\lambda_{0}$  (fraction of K overlapping I when questions are simple)</td><td>0.2</td></tr><tr><td>p (productivity of online content providers)</td><td>0.2</td></tr><tr><td>M, L (probability parameters)</td><td>500, 100</td></tr><tr><td>R (congestion parameter for advertising)</td><td>200</td></tr></table>

$$
\begin{array}{l} Q _ {1} (0) = 5 0 0, A (0) = 0, N _ {1} (0) = 2 0, K (0) = 0; \\ Q _ {2} (0) = 2 0, W (0) = 5 0 0, N _ {2} (0) = 5, I (0) = 1 0 0 0. \end{array}
$$

An inferior pure search engine tends to perform better as online content decreases. According to Table 2, which shows the results of the longterm competition between the two pure search engines, search engine 1's market share increases by 4–6% as the minimum number of potential content providers, ${ { g } _ { w } } ,$ decreases from 10,000 to 10. When online content is limited, searchers tend to multihome because even a superior search engine may not provide answers to their questions; the tendency for searchers to multihome increases their demand for search engine 1.

Table 2 also shows an inferior pure search engine tends to benefit more from introducing a knowledge-sharing service when online content is limited than it does when online content is abundant. When online content is limited, searchers are less like to <sup>fi</sup>nd answers to their questions, thus visiting search engine 1 to get the answers from answerer members and the database of answers. On the other hand, as online content increases, the degree to which search engine 1's market share by introducing a knowledge-sharing service diminishes. This simulation result accords with the empirical observation that Yahoo Answers contributes little to the market share of Yahoo in the US search engine market, in which online content is abundant. Moreover, when questions are complex and the knowledge disuse rate is high, the knowledgesharing service most helps the inferior search engine increase its market share: in Table 2, search engine 1's market share increases by 21% when online content is limited, questions are complex, and the knowledge disuse rate is relatively high $( \mathrm { e . g . } , g _ { w } = 1 0 , \theta = 0 . 5 , \mathrm { a n d } \eta = 0 . 0 1 )$

When online content is abundant, the inferior search engine is well advised to develop a knowledge-sharing service for complex and rapidly-changing topics. As the last column of Table 2 shows, search engine 1's market share increases by 10% after introducing a knowledgesharing service when questions are complex and the knowledge disuse rate is relatively high (e.g., θ=0.5 and η=0.01); however, search engine 1's market share increases only by 4% when questions are simple and the knowledge disuse rate is relatively low (e.g., θ=0.1 and η=0.005).

## 4.2. When online content providers are limited

In this subsection, we simulate the competition between search engine 1, an incumbent with an initially large market share, and search engine 2, a latecomer with an initially small market share, when online content providers are limited. We focus on the impact that search engine 1 has on the competition in terms of market share if it closes its database of answers. A practical example of such a case is Naver, which was an incumbent with a successful online knowledge-sharing service when technologically superior Google entered the Korean search engine market in 2006. To take search engine 1's large market share into account, We use the following initial conditions:

The long-term stabilized values for the states in the simulation when search engine 1 does not have a knowledge-sharing service.

<table><tr><td> $\theta$ </td><td> $\eta$ </td><td> $g_{w}$ </td><td> $Q_1$ </td><td> $N_1$ </td><td> $Q_2$ </td><td>W</td><td> $N_2$ </td><td>I</td><td> $\frac{Q_1}{Q_1+Q_2}$ </td><td> $\frac{Q_1}{Q_1+Q_2}$  with K-S</td></tr><tr><td>0.1</td><td>0.01</td><td>10</td><td>68</td><td>15</td><td>100</td><td>74</td><td>17</td><td>173</td><td>40%</td><td>58% (18%↑)</td></tr><tr><td>0.1</td><td>0.01</td><td>10,000</td><td>177</td><td>23</td><td>341</td><td>10,114</td><td>27</td><td>2011</td><td>34%</td><td>40% (6%↑)</td></tr><tr><td>0.1</td><td>0.01</td><td>60,000</td><td>258</td><td>24</td><td>533</td><td>60,141</td><td>32</td><td>4904</td><td>33%</td><td>36% (3%↑)</td></tr><tr><td>0.1</td><td>0.005</td><td>10</td><td>94</td><td>17</td><td>148</td><td>87</td><td>19</td><td>381</td><td>39%</td><td>56% (17%↑)</td></tr><tr><td>0.1</td><td>0.005</td><td>10,000</td><td>236</td><td>23</td><td>481</td><td>10,134</td><td>28</td><td>4004</td><td>33%</td><td>37% (4%↑)</td></tr><tr><td>0.1</td><td>0.005</td><td>60,000</td><td>354</td><td>24</td><td>753</td><td>60,166</td><td>32</td><td>9811</td><td>32%</td><td>34% (2%↑)</td></tr><tr><td>0.5</td><td>0.01</td><td>10</td><td>49</td><td>9</td><td>70</td><td>64</td><td>11</td><td>161</td><td>41%</td><td>62% (21%↑)</td></tr><tr><td>0.5</td><td>0.01</td><td>10,000</td><td>143</td><td>19</td><td>250</td><td>10,099</td><td>22</td><td>2009</td><td>36%</td><td>46% (10%↑)</td></tr><tr><td>0.5</td><td>0.01</td><td>60,000</td><td>213</td><td>19</td><td>391</td><td>60,123</td><td>24</td><td>4904</td><td>35%</td><td>41% (6%↑)</td></tr><tr><td>0.5</td><td>0.005</td><td>10</td><td>69</td><td>13</td><td>104</td><td>75</td><td>14</td><td>349</td><td>40%</td><td>59% (19%↑)</td></tr><tr><td>0.5</td><td>0.005</td><td>10,000</td><td>194</td><td>21</td><td>352</td><td>10,117</td><td>25</td><td>3999</td><td>36%</td><td>44% (8%↑)</td></tr><tr><td>0.5</td><td>0.005</td><td>60,000</td><td>295</td><td>22</td><td>552</td><td>60,146</td><td>28</td><td>9809</td><td>35%</td><td>40% (5%↑)</td></tr></table>

Note: The last column is added to show search engine 1's market share when it has a knowledge-sharing service, keeping the database of answers open.

Table 3 The long-term stabilized values for the states in the simulation when online content providers are limited $( g _ { w } = 1 0 )$

<table><tr><td> $\theta$ </td><td> $\eta$ </td><td>z</td><td> $Q_1$ </td><td>A</td><td> $N_1$ </td><td>K</td><td> $Q_2$ </td><td>W</td><td> $N_2$ </td><td>I</td><td> $\frac{Q_1}{Q_1+Q_2}$ </td></tr><tr><td>0.1</td><td>0.1</td><td>Open</td><td>87</td><td>44</td><td>14</td><td>27</td><td>46</td><td>67</td><td>9</td><td>16</td><td>65%</td></tr><tr><td>0.1</td><td>0.1</td><td>Closed</td><td>87</td><td>44</td><td>14</td><td>27</td><td>28</td><td>63</td><td>7</td><td>16</td><td>76%</td></tr><tr><td>0.1</td><td>0.01</td><td>Open</td><td>200</td><td>44</td><td>19</td><td>277</td><td>144</td><td>102</td><td>16</td><td>202</td><td>58%</td></tr><tr><td>0.1</td><td>0.01</td><td>Closed</td><td>199</td><td>44</td><td>19</td><td>277</td><td>72</td><td>92</td><td>11</td><td>192</td><td>73%</td></tr><tr><td>0.1</td><td>0.005</td><td>Open</td><td>246</td><td>39</td><td>21</td><td>453</td><td>193</td><td>114</td><td>18</td><td>428</td><td>56%</td></tr><tr><td>0.1</td><td>0.005</td><td>Closed</td><td>243</td><td>39</td><td>20</td><td>453</td><td>99</td><td>102</td><td>13</td><td>405</td><td>71%</td></tr><tr><td>0.1</td><td>0.001</td><td>Open</td><td>376</td><td>26</td><td>25</td><td>1114</td><td>397</td><td>149</td><td>24</td><td>2406</td><td>49%</td></tr><tr><td>0.1</td><td>0.001</td><td>Closed</td><td>357</td><td>26</td><td>24</td><td>1098</td><td>258</td><td>134</td><td>20</td><td>2281</td><td>58%</td></tr><tr><td>0.1</td><td>0.0001</td><td>Open</td><td>600</td><td>19</td><td>28</td><td>2908</td><td>754</td><td>194</td><td>32</td><td>9299</td><td>44%</td></tr><tr><td>0.1</td><td>0.0001</td><td>Closed</td><td>559</td><td>18</td><td>29</td><td>2828</td><td>540</td><td>175</td><td>28</td><td>8878</td><td>51%</td></tr><tr><td>0.5</td><td>0.1</td><td>Open</td><td>88</td><td>45</td><td>14</td><td>28</td><td>35</td><td>65</td><td>8</td><td>16</td><td>72%</td></tr><tr><td>0.5</td><td>0.1</td><td>Closed</td><td>88</td><td>45</td><td>14</td><td>28</td><td>21</td><td>62</td><td>6</td><td>15</td><td>81%</td></tr><tr><td>0.5</td><td>0.01</td><td>Open</td><td>178</td><td>47</td><td>19</td><td>309</td><td>111</td><td>95</td><td>14</td><td>195</td><td>62%</td></tr><tr><td>0.5</td><td>0.01</td><td>Closed</td><td>177</td><td>47</td><td>18</td><td>309</td><td>54</td><td>86</td><td>10</td><td>185</td><td>77%</td></tr><tr><td>0.5</td><td>0.005</td><td>Open</td><td>223</td><td>45</td><td>20</td><td>571</td><td>153</td><td>107</td><td>16</td><td>414</td><td>59%</td></tr><tr><td>0.5</td><td>0.005</td><td>Closed</td><td>221</td><td>45</td><td>20</td><td>569</td><td>73</td><td>95</td><td>12</td><td>391</td><td>75%</td></tr><tr><td>0.5</td><td>0.001</td><td>Open</td><td>414</td><td>42</td><td>26</td><td>2515</td><td>333</td><td>146</td><td>23</td><td>2381</td><td>55%</td></tr><tr><td>0.5</td><td>0.001</td><td>Closed</td><td>396</td><td>42</td><td>25</td><td>2447</td><td>157</td><td>127</td><td>17</td><td>2224</td><td>72%</td></tr><tr><td>0.5</td><td>0.0001</td><td>Open</td><td>801</td><td>50</td><td>34</td><td>10,656</td><td>677</td><td>202</td><td>31</td><td>10,131</td><td>54%</td></tr><tr><td>0.5</td><td>0.0001</td><td>Closed</td><td>750</td><td>48</td><td>32</td><td>10,224</td><td>309</td><td>172</td><td>23</td><td>9488</td><td>71%</td></tr></table>

$$
Q _ {1} (0) = 5 0 0, A (0) = 1 0 0, N _ {1} (0) = 2 0, K (0) = 2 0 0;\tag{10}
$$

$$
Q _ {2} (0) = 2 0, \quad W (0) = 5 0 0, N _ {2} (0) = 5, \quad I (0) = 1 0 0 0.\tag{11}
$$

Online content in a particular language tends to be limited when a relatively small number of online content providers exist.<sup>17</sup> For instance, compared to the US search engine market, in which most online searches are done in English, most searchers in South Korea use Korean for their web search. Obviously, the number of online content providers who upload content in Korean is much smaller than that of content providers who post content in English. Thus, online content in Korean is relatively smaller than that in English. To simulate the competition between search engine 1 and 2 when online content providers are limited, we use a minimum of 10 potential online content providers $( g _ { w } = 1 0 )$ ; in the next subsection, we increase the minimum number of potential online content providers from 10 to 1000 to 10,000 to simulate the competition as the number of online content providers increases.

When online content providers are limited, Search engine 1 can significantly increase its market share by making its database of answers unavailable to search queries from search engine 2 unless the associated knowledge disuse rate is very low. As Table 3 shows, the size of the database (K) is not small compared to that of online content (I) excluding the database; thus, search engine 1's market share increases by 10–15% by keeping its database of answers closed. Fig. 3 also depicts the growth trajectories of the two search engines, showing that the number of searchers visiting search engine 2 is much smaller when the database is closed than it is when the database is open. When searchable content is limited, no matter how superior search engine

Growth of Competing Search Engines (Open)  
![](/api/attachments/HTCC5SWM/fulltext/images/5509ed4566e2a5774572aea4fa07efa8909cd8a649f62ad2a190cebb5dc90660.jpg)

Growth of Competing Search Engines (Closed)  
![](/api/attachments/HTCC5SWM/fulltext/images/c0952ff55236a03043cbab46b6629093d981f9727021963b679c3ee4e3be0611.jpg)  
Fig. 3. The growth trajectories of search engines 1 and 2 when online content providers are limited. Note: $g _ { w } = 1 0 , \theta = 0 . 1$ , and η= 0.005.

2's technology is, it is unlikely to satisfy searchers. As a result, searchers of search engine 2 tend to visit search engine 1 (hence tend to multihome), and search engine 1 has no need to open its database of answers in exchange for an increase in multihoming of potential searchers. Note that when the associated knowledge disuse rate is very low (e.g., η=0.0001 in Table 3), online content eventually accumulates and the market share impact of search engine 1's making the database of answers inaccessible becomes relatively small.

In terms of market share, the initial leader search engine 1 will still be a leader unless questions are simple, the knowledge disuse rate is low, and its database of answers is open: in such a case, information on the Internet eventually accumulates and will be large compared to the database of answers. This result is illustrated by Table 3, which shows the simulation results of the competition: When questions are simple (θ=0.1); the average knowledge disuse rate is low $( \eta = 0 . 0 0 0 1 )$ ; and the database is open, search engine 1's market share is 44%. However, with the same question complexity and knowledge disuse rate, search engine 1 will still be a leader when it keeps its database of answers closed.

## 4.3. When online content providers are abundant

In this subsection, we simulate the competition between search engine 1 and 2 when online content providers are abundant. We again investigate the impact search engine 1 has on the market shares of search engine 1 and 2 by closing its database of answers, with the same initial conditions<sup>18</sup> speci<sup>fi</sup>ed by Eqs. (10) and (11) in the previous subsection. But, we increase the minimum number of potential online content providers $\left( { { g } _ { w } } \right)$ from 10 to 1000 to 10,000 to re<sup>fl</sup>ect a large number of online content providers, which generally implies a large amount of online content.

As more online content providers exist, search engine 1 is more likely to lose its leading position to search engine 2. Furthermore, search engine 1's closing its database of answers results in a small gain in its market share. As Tables 4 and 5 shows, search engine 1 will lose its leading position when online content providers are abundant (e.g., $g _ { w } = 1 0 0 0 0 )$ , and the degree to which search engine 1's market share increases by closing its database of answers also diminishes: the increase in its market share is only 1–2% when $g _ { w } = 1 0 0 0 0$ . This is because the size of the database of answers, $K ,$ is quite small compared to the size of online content, I. Fig. 4 shows that the almost same growth trajectories of search engine 1 and 2 are realized regardless of whether the database is closed or open. It stands to reason that when large online content is provided by a large number of online content providers, the search technology of a search engine becomes critical to its success. Therefore, search engine 1 with low technology and a small database of answers will <sup>fi</sup>nd it dif<sup>fi</sup>cult to compete with a pure search engine with high technology, regardless of whether the database is closed or open.

The long-term stabilized values for the states in the simulation when the amount of online content is not small (g =1000).

<table><tr><td> $\theta$ </td><td> $\eta$ </td><td>z</td><td> $Q_1$ </td><td>A</td><td> $N_1$ </td><td>K</td><td> $Q_2$ </td><td>W</td><td> $N_2$ </td><td>I</td><td> $\frac{Q_1}{Q_1+Q_2}$ </td></tr><tr><td>0.1</td><td>0.01</td><td>Open</td><td>210</td><td>40</td><td>22</td><td>231</td><td>212</td><td>1103</td><td>19</td><td>664</td><td>50%</td></tr><tr><td>0.1</td><td>0.01</td><td>Closed</td><td>207</td><td>40</td><td>22</td><td>228</td><td>167</td><td>1097</td><td>17</td><td>662</td><td>55%</td></tr><tr><td>0.1</td><td>0.005</td><td>Open</td><td>251</td><td>34</td><td>21</td><td>342</td><td>291</td><td>1116</td><td>22</td><td>1337</td><td>46%</td></tr><tr><td>0.1</td><td>0.005</td><td>Closed</td><td>244</td><td>33</td><td>21</td><td>336</td><td>238</td><td>1110</td><td>20</td><td>1333</td><td>51%</td></tr><tr><td>0.5</td><td>0.01</td><td>Open</td><td>193</td><td>45</td><td>20</td><td>285</td><td>161</td><td>1094</td><td>17</td><td>662</td><td>54%</td></tr><tr><td>0.5</td><td>0.01</td><td>Closed</td><td>190</td><td>45</td><td>19</td><td>282</td><td>123</td><td>1089</td><td>15</td><td>660</td><td>61%</td></tr><tr><td>0.5</td><td>0.005</td><td>Open</td><td>239</td><td>43</td><td>21</td><td>512</td><td>223</td><td>1108</td><td>19</td><td>1331</td><td>52%</td></tr><tr><td>0.5</td><td>0.005</td><td>Closed</td><td>233</td><td>42</td><td>21</td><td>504</td><td>170</td><td>1100</td><td>17</td><td>1327</td><td>58%</td></tr></table>

The long-term stabilized values for the states in the simulation when online content is abundant $( g _ { w } = 1 0 0 0 0 )$

<table><tr><td> $\theta$ </td><td> $\eta$ </td><td>z</td><td> $Q_1$ </td><td>A</td><td> $N_1$ </td><td>K</td><td> $Q_2$ </td><td>W</td><td> $N_2$ </td><td>I</td><td> $\frac{Q_1}{Q_1+Q_2}$ </td></tr><tr><td>0.1</td><td>0.01</td><td>Open</td><td>234</td><td>31</td><td>20</td><td>147</td><td>345</td><td>10,120</td><td>23</td><td>2012</td><td>40%</td></tr><tr><td>0.1</td><td>0.01</td><td>Closed</td><td>231</td><td>30</td><td>20</td><td>145</td><td>324</td><td>10,118</td><td>22</td><td>2011</td><td>42%</td></tr><tr><td>0.1</td><td>0.005</td><td>Open</td><td>289</td><td>24</td><td>22</td><td>194</td><td>485</td><td>10,139</td><td>26</td><td>4027</td><td>37%</td></tr><tr><td>0.1</td><td>0.005</td><td>Closed</td><td>286</td><td>24</td><td>22</td><td>192</td><td>463</td><td>10,137</td><td>26</td><td>4027</td><td>38%</td></tr><tr><td>0.5</td><td>0.01</td><td>Open</td><td>221</td><td>41</td><td>20</td><td>238</td><td>257</td><td>10,109</td><td>20</td><td>2010</td><td>46%</td></tr><tr><td>0.5</td><td>0.01</td><td>Closed</td><td>218</td><td>40</td><td>20</td><td>236</td><td>234</td><td>10,106</td><td>19</td><td>2010</td><td>48%</td></tr><tr><td>0.5</td><td>0.005</td><td>Open</td><td>282</td><td>39</td><td>22</td><td>439</td><td>362</td><td>10,127</td><td>23</td><td>4025</td><td>44%</td></tr><tr><td>0.5</td><td>0.005</td><td>Closed</td><td>277</td><td>38</td><td>22</td><td>433</td><td>330</td><td>10,123</td><td>22</td><td>4024</td><td>46%</td></tr></table>

Growth of Competing Search Engines (Closed)  
![](/api/attachments/HTCC5SWM/fulltext/images/f41717215385dbbc1f47c4409ea90f1329d98d5dee26140e5f6f0f3ac78cc0c5.jpg)

![](/api/attachments/HTCC5SWM/fulltext/images/08f83a8f3be0516e3178f6776b3a31bedaecb32dd7e1854ddfd4f096634e4f75.jpg)  
Fig. 4. The growth trajectories of search engines 1 and 2 when online content is abundant. Note: $g _ { w } = 1 0 0 0 0 , \theta = 0 . 1$ , and $\begin{array} { r } { \eta = 0 . 0 0 5 . } \end{array}$ The size of online content (I) and the number of online content providers (W) are omitted because they are too large compared to the other states.

Search engine 1 is advised to close its database of answers for more market share unless its search technology is far behind that of search engine 2. As Table 6 shows, when search engine 1's search technology is very low compared to that of search engine $2 \ ( \mathrm { e . g . } , \ s _ { 1 } = 0 . 1 $ and $s _ { 2 } = 0 . 7 )$ , search engine 1 may end up with a little more market share by opening its database of answers when online content is very abundant (e.g., $g _ { w } = 6 0 , 0 0 0$ , 70,000, and 100,000). On the other hand, when $g _ { w } = 6 0 , 0 0 0$ and s decreases to 0.5, search engine 1 still has a little more market share by closing its database of answers. Note that when online content providers are very abundant, the search engine 1's market share changes little by closing or opening its database of answers; search engine 1 is generally advised to close its database of answers for more market share regardless of the amount of online content.

can also increase its pro<sup>fi</sup>ts by closing its database of answers. The answer to this question depends on the degree to which advertisers tend to put their advertisements only on a single search engine: if they tend to more singlehome, search engine 1 is more likely to increase its profits with its closed database of answers.

In the previous two sections, we have shown that search engine 1 can generally increase its market share by closing its database of answers. The next question we may ask is whether search engine 1

Fig. 5 compares the instantaneous pro<sup>fi</sup>ts of search engine 1 when advertisers tend to multihome $( \mathrm { i . e . , ~ } e _ { n _ { 1 } } = e _ { n _ { 2 } } { = } 0 )$ and partially singlehome $( \mathrm { i . e . , } e _ { n _ { 1 } } = e _ { n _ { 2 } } = 0 . 5 )$ . When they multihome, search engine 1 has more instantaneous pro<sup>fi</sup>ts with its open database of answers; when they partially singlehome, search engine 1 has more profits with its closed database of answers. This is because as advertisers tend to compare the searchers' demands for search engine 1 and 2, they care more about the market share of search engine 1 than they do about the number of searchers visiting search engine 1.

## 4.4. The impact of closing a database of answers on profits

## 4.5. The impact of less-invasive advertising on the competition

In this subsection, we investigate whether the results of the previous two subsections will still hold when search engine 2 presents advertising in a less-invasive way than search engine 1 does. In the previous subsections, we assume that advertising has neither positive nor negative cross-group effects on members of search engines 1 and 2; $\begin{array} { r } { d _ { q _ { 1 } } = d _ { a } = d _ { q _ { 2 } } = 0 . } \end{array}$ . However, in practice, some search engines may present advertising according to searchers' interests: Google's searchbased advertising is less invasive than banner or pop-up advertising that Naver and Yahoo sometimes put on some portion of their websites.

The long-term stabilized values for the states in the simulation when search engine 1's search technology s is low.

<table><tr><td> $g_w$ </td><td> $s_1$ </td><td> $s_2$ </td><td>z</td><td> $Q_1$ </td><td>A</td><td> $N_1$ </td><td>K</td><td> $Q_2$ </td><td>W</td><td> $N_2$ </td><td>I</td><td> $Q_1/(Q_1+Q_2)$ </td></tr><tr><td>1000</td><td>0.1</td><td>0.7</td><td>Open</td><td>149</td><td>40</td><td>20</td><td>233</td><td>214</td><td>1095</td><td>19</td><td>662</td><td>41.087%</td></tr><tr><td>1000</td><td>0.1</td><td>0.7</td><td>Closed</td><td>142</td><td>40</td><td>20</td><td>227</td><td>174</td><td>1089</td><td>17</td><td>660</td><td>45.067%</td></tr><tr><td>10,000</td><td>0.1</td><td>0.7</td><td>Open</td><td>95</td><td>31</td><td>15</td><td>144</td><td>347</td><td>10,105</td><td>23</td><td>2011</td><td>21.415%</td></tr><tr><td>10,000</td><td>0.1</td><td>0.7</td><td>Closed</td><td>91</td><td>30</td><td>15</td><td>140</td><td>331</td><td>10,103</td><td>22</td><td>2010</td><td>21.589%</td></tr><tr><td>60,000</td><td>0.1</td><td>0.7</td><td>Open</td><td>79</td><td>23</td><td>14</td><td>85</td><td>535</td><td>60,124</td><td>27</td><td>4904</td><td>12.892%</td></tr><tr><td>60,000</td><td>0.1</td><td>0.7</td><td>Closed</td><td>78</td><td>23</td><td>14</td><td>84</td><td>527</td><td>60,123</td><td>27</td><td>4904</td><td>12.883%</td></tr><tr><td>60,000</td><td>0.1</td><td>0.5</td><td>Open</td><td>103</td><td>26</td><td>18</td><td>105</td><td>449</td><td>60,117</td><td>26</td><td>4904</td><td>18.609%</td></tr><tr><td>60,000</td><td>0.1</td><td>0.5</td><td>Closed</td><td>101</td><td>26</td><td>17</td><td>104</td><td>442</td><td>60,117</td><td>25</td><td>4904</td><td>18.658%</td></tr><tr><td>70,000</td><td>0.1</td><td>0.7</td><td>Open</td><td>79</td><td>22</td><td>14</td><td>81</td><td>555</td><td>70,126</td><td>28</td><td>5296</td><td>12.448%</td></tr><tr><td>70,000</td><td>0.1</td><td>0.7</td><td>Closed</td><td>78</td><td>22</td><td>14</td><td>80</td><td>548</td><td>70,125</td><td>28</td><td>5296</td><td>12.435%</td></tr><tr><td>100,000</td><td>0.1</td><td>0.7</td><td>Open</td><td>79</td><td>21</td><td>16</td><td>72</td><td>606</td><td>100,130</td><td>29</td><td>6329</td><td>11.504%</td></tr><tr><td>100,000</td><td>0.1</td><td>0.7</td><td>Closed</td><td>78</td><td>21</td><td>16</td><td>71</td><td>601</td><td>100,130</td><td>29</td><td>6329</td><td>11.489%</td></tr><tr><td>60,000</td><td>0.2</td><td>0.7</td><td>Open</td><td>142</td><td>23</td><td>19</td><td>85</td><td>534</td><td>60,130</td><td>28</td><td>4904</td><td>21.060%</td></tr><tr><td>60,000</td><td>0.2</td><td>0.7</td><td>Closed</td><td>141</td><td>23</td><td>19</td><td>84</td><td>526</td><td>60,129</td><td>27</td><td>4904</td><td>21.145%</td></tr><tr><td>60,000</td><td>0.3</td><td>0.7</td><td>Open</td><td>216</td><td>23</td><td>20</td><td>86</td><td>534</td><td>60,137</td><td>28</td><td>4905</td><td>28.778%</td></tr><tr><td>60,000</td><td>0.3</td><td>0.7</td><td>Closed</td><td>214</td><td>23</td><td>20</td><td>86</td><td>525</td><td>60,136</td><td>27</td><td>4904</td><td>28.964%</td></tr><tr><td>600,000</td><td>0.2</td><td>0.7</td><td>Open</td><td>194</td><td>15</td><td>20</td><td>39</td><td>947</td><td>600,170</td><td>35</td><td>15,494</td><td>17.038%</td></tr><tr><td>600,000</td><td>0.2</td><td>0.7</td><td>Closed</td><td>194</td><td>15</td><td>20</td><td>39</td><td>944</td><td>600,170</td><td>35</td><td>15,494</td><td>17.047</td></tr><tr><td>1,000,000</td><td>0.2</td><td>0.7</td><td>Open</td><td>214</td><td>14</td><td>21</td><td>34</td><td>1076</td><td>1,000,200</td><td>37</td><td>20,002</td><td>16.601</td></tr><tr><td>1,000,000</td><td>0.2</td><td>0.7</td><td>Closed</td><td>214</td><td>14</td><td>21</td><td>34</td><td>1074</td><td>1,000,200</td><td>37</td><td>20,002</td><td>16.608%</td></tr></table>

Note: θ=0.1 and η=0.01.

Table 7  
![](/api/attachments/HTCC5SWM/fulltext/images/dab796b334c30ad209ae35affbf73157434a7409a3de779d5af89787de4ea2c2.jpg)  
Fig. 5. Change in the instantaneous pro<sup>fi</sup>ts of search engine 1 as the degree to which advertisers singlehome increases. Note: θ=0.1 and η=0.005.

The previous results regarding the impact of search engine 1's closing its database of answers on its market share still hold when search engine 2's advertising has a positive effect, but search engine 1's advertising has a negative effect on their users. As Table 7 shows, search engine 1 can generally increase its market share by closing its database of answers, and the degree to which search engine 1 bene<sup>fi</sup>ts from closing its database of answers decreases in the amount of online content: the increase in its market share by making its database unavailable to search engine 2 is only 1–2% when online content providers are abundant. This simulation result implies that the outcome of the competition between search engine 1 and 2 will not signi<sup>fi</sup>cantly change when search engine 2 makes its advertising more informative to its searchers than search engine 1.

## 5. Conclusion

Our research is, up to our knowledge, the <sup>fi</sup>rst attempt to investigate the dynamic competition between two heterogeneous search engines: one is a low-technology search engine with an online knowledgesharing service and the other is a high-technology search engine without an online knowledge-sharing service. Our research is motivated by the question of Google's small market share in South Korea, where a local portal called Naver, which has a successful knowledge-sharing service, is dominant. Another motivation is the question of whether, given Google's dominant position in the US market, Yahoo can increase its market share by introducing an online knowledge-sharing service.

The long-term stabilized values for the states in the simulation with asymmetric advertising effects: negative for search engine 1 and positive for search engine 2.

<table><tr><td> $g_w$ </td><td> $\theta$ </td><td> $\eta$ </td><td>z</td><td> $Q_1$ </td><td>A</td><td> $N_1$ </td><td>K</td><td> $Q_2$ </td><td>W</td><td> $N_2$ </td><td>I</td><td> $\frac{Q_1}{Q_1+Q_2}$ </td></tr><tr><td>10</td><td>0.1</td><td>0.005</td><td>Open</td><td>233</td><td>35</td><td>20</td><td>415</td><td>193</td><td>113</td><td>18</td><td>425</td><td>55%</td></tr><tr><td>10</td><td>0.1</td><td>0.005</td><td>Closed</td><td>230</td><td>35</td><td>20</td><td>413</td><td>106</td><td>101</td><td>14</td><td>403</td><td>68%</td></tr><tr><td>10</td><td>0.5</td><td>0.01</td><td>Open</td><td>167</td><td>42</td><td>18</td><td>281</td><td>112</td><td>93</td><td>14</td><td>193</td><td>60%</td></tr><tr><td>10</td><td>0.5</td><td>0.01</td><td>Closed</td><td>166</td><td>42</td><td>18</td><td>281</td><td>59</td><td>85</td><td>10</td><td>184</td><td>74%</td></tr><tr><td>10,000</td><td>0.1</td><td>0.005</td><td>Open</td><td>279</td><td>19</td><td>22</td><td>160</td><td>488</td><td>10,139</td><td>26</td><td>4027</td><td>36%</td></tr><tr><td>10,000</td><td>0.1</td><td>0.005</td><td>Closed</td><td>276</td><td>19</td><td>22</td><td>159</td><td>469</td><td>10,137</td><td>26</td><td>4027</td><td>37%</td></tr><tr><td>10,000</td><td>0.5</td><td>0.01</td><td>Open</td><td>212</td><td>35</td><td>20</td><td>213</td><td>260</td><td>10,109</td><td>20</td><td>2010</td><td>45%</td></tr><tr><td>10,000</td><td>0.5</td><td>0.01</td><td>Closed</td><td>209</td><td>35</td><td>20</td><td>211</td><td>239</td><td>10,106</td><td>19</td><td>2010</td><td>47%</td></tr></table>

Note: $d _ { q _ { 1 } } = d _ { a } = 1 ; d _ { q _ { 2 } } = - 1 .$

Our study provides useful strategic guidelines for search engines to refer to when they or their competitors consider introducing an online knowledge-sharing service. Table 8 summarizes under what circumstances the knowledge-sharing service will help an inferior search engine to increase its market share and to keep its initial market share leadership. A search engine with inferior technology generally bene<sup>fi</sup>ts from introducing a knowledge-sharing service. The degree to which the knowledge-sharing service helps the inferior search engine compete better with a superior search engine decreases as more online content providers exist: if searchers are likely to <sup>fi</sup>nd answers to their questions by searching the online content, they generally do not visit the inferior engine to use its knowledge-sharing service. Thus, Google's main competitor Yahoo will not bene<sup>fi</sup>t significantly from its knowledge-sharing service Yahoo Answers. On the other hand, when online content providers are limited, searchers tend to multihome and are willing to ask questions online. Under these circumstances, the inferior search engine's database of answers will attract searchers. However, when question complexity is low and the associated knowledge changes very slowly, an inferior search engine may lose its (market share) leadership if it opens its database of answers to searchers visiting a competing superior search engine: when the associated knowledge changes slowly, the competing superior search engine can eventually access a relatively large amount of online content, which accumulates over time.

## Table 8

the impact of a knowledge-sharing service on the market share of an inferior search engine. Note: complexity refers to the average complexity of questions asked on a search engine site. Closed and Open on the <sup>fi</sup>rst line of the table mean that the database of answers is closed and open.

<table><tr><td>Online content providers</td><td>Complexity</td><td>Knowledge disuse rate</td><td>Degree of benefits</td><td>Market share leadership</td></tr><tr><td rowspan="4">Limited</td><td rowspan="2">Simple</td><td>Low</td><td>High</td><td>Keep (Closed); Lose (Open)</td></tr><tr><td>High</td><td>High</td><td>Keep</td></tr><tr><td rowspan="2">Complex</td><td>Low</td><td>High</td><td>Keep</td></tr><tr><td>High</td><td>Highest</td><td>Keep</td></tr><tr><td rowspan="4">Abundant</td><td rowspan="2">Simple</td><td>Low</td><td>Lowest</td><td>Lose</td></tr><tr><td>High</td><td>Low</td><td>Lose</td></tr><tr><td rowspan="2">Complex</td><td>Low</td><td>Medium</td><td>Lose</td></tr><tr><td>High</td><td>Medium</td><td>Lose</td></tr></table>

Table 9  
The strategy for an inferior search engine to increase its market share: close vs. open its database of answers.

<table><tr><td>Online content providers</td><td>Search quality difference</td><td>Close vs. open</td></tr><tr><td rowspan="2">Limited</td><td>Small</td><td>Close</td></tr><tr><td>Large</td><td>Close</td></tr><tr><td rowspan="2">Abundant</td><td>Small</td><td>Close</td></tr><tr><td>Large</td><td>Open</td></tr></table>

One critical question is whether the inferior search engine will increase its market share by keeping the database of answers inaccessible by the competing search engine. As Table 9 summarizes, when online content is limited, the inferior search engine should keep its database of answers closed to maximize its market share; when online content is abundant, the inferior search engine should keep its database of answers closed unless its search technology is far behind that of the superior search engine. We can also verify that the degree of a competitive edge that the closed database will provide for the inferior search engine increases as indexable online content decreases. The result shows that Naver, a leading portal in South Korea, has done the strategically correct thing in keeping its database of answers closed, thereby maintaining its dominant position.

Our model can be extended to include the case when the superior search engine introduces its own knowledge-sharing service. The results of our study <sup>fi</sup>rst suggest that when online content is abundant, the superior search engine does not need to introduce its knowledgesharing service: the superior search engine without a knowledgesharing service is already dominant over the inferior search engine with a knowledge-sharing service. When online content is small due to a small number of content providers or their low productivity in posting content on the Internet, the incumbent inferior search engine with a knowledge-sharing service is expected to keep its dominant position if its closed database of answers can be signi<sup>fi</sup>cantly large compared to online content. Searchers then tend to rely on the inferior search engine's database of answers to <sup>fi</sup>nd information; the superior search engine will have a hard time in attracting searchers.

## Acknowledgments

We thank Wugang Zhao, Yongkyun Na, Yenho Chung, and the anonymous referee for valuable comments. The research is partially supported by the SK research fund at Korea University Business School. We also acknowledge Kwanjeong Educational Foundation in South Korea for their partial <sup>fi</sup>nancial support for Kihoon Kim's doctoral study in Management Science and Engineering at Stanford University. An earlier version of this article was prepared as part of his Ph.D. thesis.

## References

[1] E. Bradlow, D. Schmittlein, The little engines that could: modeling the performance of world wide web portals, Marketing Science 19 (1999) 43–62.

[2] D. Choi, Enhancing the power of web search engines by means of fuzzy query, Decision Support Systems 35 (2003) 31–44.

[3] N. Gandal, The dynamics of competition in the internet search engine market, International Journal of Industrial Organization 19 (2001) 1103–1117.

[4] K. Kim, E. Tse, Search engine competition with a knowledge-sharing service, Working Paper, 2010.

[5] K. Kim, E. Tse, Dynamic competition strategy for online knowledge-sharing platforms, International Journal of Electronic Commerce 16 (1) (2011) 43–79.

[6] N. Kumar, K.R. Lang, Do search terms matter for online consumers? the interplay between search engine query speci<sup>fi</sup>cation and topical organization, Decision Support Systems 44 (2007) 159–174.

[7] F. Menczer, Complementing search engines with online web mining agents, Decision Support Systems 35 (2003) 195–212.

[8] M. Sun, E. Tse, When does the winner take all in two-sided markets? Review of Network Economics 6 (2007) 16–41.

[9] R. Telang, T. Mukhopadhyay, Drivers of web portal use, Electronic Commerce Research and Applications 4 (2005) 49–65.

[10] R. Telang, T. Mukhopadhyay, R.T. Wilcox, An Empirical Analysis of Internet Search Engine Choice, Working Paper, Carnegie Mellon University, 2001.

[11] R. Telang, U. Rajan, T. Mukhopadhyay, The market structure for internet search engines, Journal of Management Information Systems 21 (2004) 137–160.

[12] J. Xie, M. Sirbu, Price competition and compatibility in the presence of positive demand externalities, Management Science 41 (1995) 909–926.

[13] F. Zhu, M. Iansiti, Dynamics of platform competition: exploring the role of installed base, platform quality and consumer expectations, HBS Working Paper, 2007.

Kihoon Kim is an Assistant Professor of Logistics, Services, and Operations Management at Korea University Business School. His current research lies in platform competition in two-sided markets such as online knowledge-sharing and search engine markets. He received his Ph.D. from the department of Management Science and Engineering at Stanford University in 2009. Before he came to Stanford for his graduate study, he worked as a sup ply chain management consultant at Seoul of<sup>fi</sup>ce of PricewaterhouseCoopers Consulting

Edison Tse is Associate Professor and Director of Asia Center in the Department of Management Science of Engineering of Stanford University. He received his Ph.D. from MIT in Electrical Engineering and won the 1973 Donald P. Eckman Award for outstanding achievement in the <sup>fi</sup>eld of automatic control. He co-founded the Journal of Economic Dynamics and Control and has been a member of its Advisory Board. His current research in volves taking a system approach to problems in management, decision and policy.
