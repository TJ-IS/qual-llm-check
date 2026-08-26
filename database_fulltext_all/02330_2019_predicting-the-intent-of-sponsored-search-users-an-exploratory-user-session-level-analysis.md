---
otero_id: 2330
otero_key: "JWXFWGJM"
title: "Predicting the intent of sponsored search users: An exploratory user session-level analysis"
authors: "Il Im; Brian Kimball Dunn; Dong Il Lee; Dennis F. Galletta; Seok-Oh Jeong"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting the intent of sponsored search users: An exploratory user sessionlevel analysis

![](/api/attachments/JWXFWGJM/fulltext/images/a807b134a06191d2a44194172c89d0a97869c4e2fcecfea484f398a7e9b8bf0f.jpg)

Il Im<sup>a</sup>, Brian Kimball Dunn<sup>b</sup>, Dong Il Lee<sup>c,⁎</sup>, Dennis F. Galletta<sup>d</sup>, Seok-Oh Jeong

<sup>a</sup> School of Business, Yonsei University, 50 Yonsei-ro, Seodeamun-gu, Seoul, Republic of Korea

<sup>b</sup> Utah State University, Huntsman School of Business, Logan, UT, USA

<sup>c</sup> School of Business, Sejong University, 209, Neungdong-ro, Gwangjin-gu, Seoul, Republic of Korea

<sup>d</sup> Katz Graduate School of Business, 282 Mervis Hall, University of Pittsburgh, 15260, USA

<sup>e</sup> Department of Statistics, Hankuk University of Foreign Studies, Yong-In 17035, Republic of Korea

## A R T I C L E I N F O

Keywords: Sponsored search ad Conversion Search pattern Purchase funne Session analysis

## A B S T R A C T

Over time, an online user searching for information about an idea or product may enter multiple search engine queries, thus creating a keyword search pattern from which the user's intent may be inferred. Such inferences could lead a merchant to alter the messages or provide ofers to push the user toward a purchase decision once the user reaches the advertiser's website. Our research seeks to establish the relationship between these patterns as they occur during a user's search session and the user's purchase behavior. To test our hypotheses, we examine a unique dataset from a large Asian travel agency that includes over two million unique search engine queries and clicks as well as the same users' corresponding on-site behavior over a one-year period. We developed a typology for the coding of search queries used in determining the level of specificity and breadth as well as content type for each of the searches. Our analysis provides important findings regarding the relationship be tween search patterns and behavior.

## 1. Introduction

Website-owning firms invest considerable time and money into building and maintaining their sites. The efectiveness of these websites depends in part on the user's intent [1–3]. Therefore, knowing the user's intent upon arrival on the site could empower the website to better serve the customer to the site owner's advantage. However, knowing a user's intent is a dificult proposition that would necessitate some degree of programmed, algorithmic clairvoyance. Being able to make such inferences would enable websites to provide a tailored experience such as providing special ofers to those intending to make a purchase or facilitating more eficient information finding for those completing an information task. However, in most cases website owners have only limited information—referring site, browser, screen resolution, and IP address—from which to infer this intent.

One of the most popular tactics for attracting users to a website is sponsored search keyword advertising [4], in which advertisers pay a fee each time a user clicks their ad and comes to their site. These ads are based on specific search queries. Companies spend considerable money on search keyword advertising, with \$26.1 billion spent during the first six months of 2017 in the US alone [5]. In the case of users clicking on these ads, the user arrives at the advertiser's website with an additional piece of potentially useful information: the search term that generated the link to the website. This additional information may be useful to enable websites to infer the intent of the user upon arrival at the website.

In this study, sponsored search advertisement data from an online travel agency were collected for about a year and analyzed to answer the questions above. These data comprise over two million observations, each representing a user's search query and corresponding click on the advertiser's ad. This very large dataset allows us also to see sequences of searches and clicks conducted by the same user, thus facilitating the discernment of discrete search sessions, during which the user sought to complete a specific task. Further, the data encompass a wide variety of search parameters used and represent users arriving on the travel agency's website with a variety of intents.

Prior to analyzing our data, we first categorized the data included in the query-click dyads based on the content of the query. A novel typology was developed for this study that enabled us to view search query clicks in terms of both the breadth and specificity of the keyword terms used. Further, acknowledging that a user's intent may be better expressed over the course of multiple queries and clicks, we introduce a new unit of analysis to the sponsored search literature, the user search session, which refers to all the query-click dyads that can be ascribed to a single user intent (e.g., a user's intent to book a trip to New Zealand, a user finding prices for tour packages to San Francisco).

In this study, we first establish basic hypotheses regarding the im plications of the depth (specificity) and breadth (number of categories referenced) of search sessions. These are then tested to determine their ability to predict user intent—specifically given the sales context of our data, this intent is represented in terms of the user's location within the purchase funnel. We find that, in fact, patterns do arise that can aid in predicting a user's location within the purchase funnel. We then build on these analyses by exploring the potential for categorizing search sessions as a potential means for algorithmically determining user in tent upon arrival.

## 2. Background

## 2.1. The sponsored search context

Given its centrality to this research, we ofer here a brief overview of sponsored search advertising, particularly as it applies to the websiteowning firm (i.e., the advertiser). Use of a search engine (e.g., Google) is typified by a user conducting a search by entering one or more key words, terms that the user chooses to describe the content sought. The set of keywords taken together (e.g., “high definition projector”, “flights to Hong Kong”) form the parameters of a search query. Once the user has entered the query, the search engine accesses its data and algorithmically determines the sites most likely to deliver the soughtafter content. These links are presented to the user on a search results page.

Looking at this process from the advertiser's point of view adds additional terms and metrics. Organizations will measure success of their keyword advertisements against a campaign objective of which direct sales and lead generation are among the most commonly pursued [6]. Sales can be measured through actual sales transacted through the website as a result of a click and, similarly, leads can be measured through actual contact information submitted to the company (a user submitting a loan application for instance or a corporate customer submitting an information request to a potential vendor). Both a completed sale and a generated lead can be considered forms of customer conversion. These conversions can be used to form another metric, conversion rate, or the ratio of conversions to clicks.

## 2.2. Search-related research

Much of the research conducted on sponsored search has come from the technical or economic modeling perspective. Such studies have researched topics including the relationship between an advertisement's rank and click-through rate and conversion rate [7], auction ineficiencies [8], potential auction equilibria [9], auction simplification mechanisms [10], possible welfare distribution efects of alternative search engine policies [11], and efects of a regulated sponsored search market on possible adverse selection [12]. While this stream of research has provided useful insight into the underlying mechanisms of sponsored search and suggests important implications in particular for the search engines themselves, it does not enable the owner to discern user intent.

For a website-owning advertiser trving to understand the user's intent so as to optimize the on-site experience for that user, it becomes important to identify the correct unit of analysis. Examining a single search query in isolation limits the potential information available; a sequence or collection of search queries made by a user may be both attainable and useful in predicting the user's intent. On the other hand, attempting to view all of a given user's queries over an extended period of time may add considerable noise and complexity if the user searches with diferent intents across that period. To address these concerns, we introduce the idea of the search session, a sequence of search query-click dyads related to a single task and conducted by a user over a confined period of time; operationalization of this will be discussed later in this paper.

This concept of multiple searches being part of the same overall session has been intimated by earlier research. Using log files, Rutz and Bucklin [13] studied behavior within search engines and found evi dence of a potential “spillover efect”, in which users who begin with one category of search terms move to other categories, for example starting with a generic term (e.g., “sports car”) and moving to a brandspecific term (e.g., “BMW Z4”). Other research has also noted an evolution in users' search queries (e.g., [14,15]). These studies, however, have not investigated the ability of accumulated search queries to predict a user's intent once the user arrives at a given website.

## 2.3. Information search and user intent

Information search “is a process in which a person seeks data or knowledge about a problem, situation, or artifact” ([15], p.91). A great deal of user activity on the Internet can be construed as acts of information search. For website owners to identify potential user intents, we thus reference the literature on information search. As our data collection context is that of an online retailer, we pay particular attention to past work regarding the purchase funnel and decisionmaking.

The purchase funnel is a framework studied primarily in the marketing discipline; its intent is to typify stages in a consumer's purchasing process. The purchase funnel concept is represented by a number of competing, though not necessarily contradictory, conceptualizations with various numbers of stages. In one of the earliest of these, Lewis [16] viewed the consumer purchase process as consisting of four stages: attention (the consumer becomes aware of a product), interest (the consumer acquires an initial interest), desire (the consumer wants the product), and action (the consumer purchases the product). These stages are funnel-like in that the consumer initially considers a large number of possibilities, then, over time, narrows these and eventually selects and purchases the one determined to best suit the individual. The funnel itself implies that there should be optimal behaviors for firms in guiding consumers in each stage of the funnel.

While later conceptualizations have included somewhat diferent stages, they have generally followed a similar, funnel-like progression. Lavidge and Steiner [17] suggest a process comprised of six stages: awareness, knowledge, liking, preference, conviction, and purchase. O'Brien [18] developed another similar model, consisting of four stages (awareness, attitude, intention, purchase). Ives and Learmonth [19] took a more comprehensive approach in a model with four stages (that extend beyond the purchase and further decompose into thirteen sub stages). Finally, several other researchers (e.g., [20–22]) have simpli fied the funnel to only two stages, a narrowing stage in which consumers consider a number of possibilities, and a purchase stage.

Conceptualizations similar to these have been developed within the broader context of decision making and problem solving. Simon [23] described the decision-making process in three phases: intelligence, design, and choice. Here, the intelligence phase refers to problem recognition and intelligence gathering, the design phase to the structuring of the problem and development of criteria to solve it, and the choice phase the selection of the alternative deemed most fitting. Evidence of the existence of these phases within the Web context has been estab lished [24].

An additional perspective on problem solving stages involves the idea of task structure, or the “degree to which the necessary inputs, operations on those inputs, and outputs are known and recognizable to the decision maker” ([15], p.92). From a task structure perspective, tasks with higher structure (e.g., buying a specific product) are less complex while those with lower structure (e.g., researching a solution to an ill-defined problem) are more complex [25]. Browne et al. [15] analyzed the decision-making process using two forms of task structure, low and high. Tasks with low structure are construed as potentially having multiple possible answers and a less clear approach to determining what those answers may be, while tasks with high structure tend to have single answers with a clear approach to resolution [26]. From this standpoint, the task structure itself may indicate the in dividual's stage in the decision-making process.

The overlap among these views on information search processes confirms an underlying premise. Learning about a product, searching a possibility maze to solve a problem, and considering a low structure task all require broad information and cognitive abstraction. Meanwhile, making a product purchase, identifying and executing a decision, and completing a high structure task reflect an already nar rowed set of possibilities. Thus, when predicting the intent of users arriving on websites, we propose that predicting this intent based on funnel location, problem solving stage, or task structure should all reflect similar relationships.

Here we need to clearly distinguish some terms used in this study: depth, breadth, and specificity. Depth refers to the level within a product hierarchy at which a user is searching for information. The top of a product hierarchy might therefore be a general product category such as washing machine or refrigerator. The next level down in this hierarchy might then be brands of the product such as GE, Whirlpool, and LG. The next level might be model number such as WM123 or G-457a. Thus, a user searching information about a product at the brand level reflects less depth than does a user searching for information at the model number level. Breadth refers to the diversity of search. For example, a user searching for information about four diferent refrigerator models is doing so with greater breadth than another researching two diferent models. Specificity refers to the extent of detail in information search. For example, if a user is searching for a refrigerator of a certain color, his/her search is more specific than other users searching for a refrigerator of any color.

Given our understanding of information search, website owners would expect individuals at the top of the purchase funnel (i.e., those who are early in the problem-solving process or working on a low structure task) to behave similarly to each other. These users need to identify broad possibility sets from which to narrow down possible products or answers as well as to attain the information needed to structure their decision-making. Therefore, the website owner should expect that the search session of a user at the top of the funnel (i.e., in the information-gathering stage) would be more likely to use a broader set of search terms, while someone closer to the purchase stage would use a narrower set of terms. Indeed, in the ofline context, Biehal and Chakravarti [27] found that consumers searching for information about a product purchase will, as they progress down the funnel, begin to search for information about ever more specific brands and products. Similarly, we expect that those who have a well-structured problem or who have already identified the product to purchase will search deeper using more specific terms (e.g., make and model of a product, a narrowly detailed question). These observations bring us to our two basic hypotheses:

Hypothesis 1. Users searching narrowly (lower breadth) will be more likely to purchase products than those searching broadly (higher breadth).

Hypothesis 2. Users searching more specifically (higher specificity) will be more likely to purchase products than those searching less specifically (lower specificity).

The purchase funnel concept suggests that users begin their pur chase journey by collecting information about numerous products; some of these users reach the bottom of the funnel (i.e., a purchase is transacted) while others do not progress beyond the top of the funnel (no purchase). Users who eventually make a purchase typically search increasingly narrowly and deeply as they progress down the funnel [27]. Conversely, those who do not purchase and remain near the top of the funnel would be less likely to narrow or deepen their searches.

Further, users may not complete both researching and purchasing within a single search session. Therefore, search patterns across search sessions are as important as characteristics of individual search sessions. If a user narrows or deepens search across search sessions, it is more likely that he/she has stronger and more focused intentions than one who stays at the same level [28]. On the other hand, if a user does not narrow or deepen the search, the person will not likely be ready to make a purchase. This leads to the following hypotheses.

Hypothesis 3. Search breadth and purchase propensity are negatively correlated.

H3a. Users searching more narrowly (lower breadth) in multiple search sessions will be more likely to purchase products than those searching more broadly (higher breadth) across sessions.

H3b. Users narrowing search breadth in the second session will be more likely to purchase products than those broadening search breadth in the second session.

Hypothesis 4. Search specificity and purchase propensity are positively correlated.

H4a. Users searching more specifically in multiple search sessions will be more likely to purchase products than those searching less specifically across sessions.

H4b. Users increasing search specificity in the second session will be more likely to purchase products than those decreasing search specificity in the second session.

## 3. Data

## 3.1. Data source

To investigate these hypotheses, data were acquired from a leading online travel agency in Asia (XYZ Travel hereafter), which conducts sponsored search advertising. Data acquired were based on advertisements placed through a single platform. From these advertising activities, XYZ Travel accumulates individual user search and click data, which can be matched to online sales results for each user. The raw data contains information about each user's sponsored search advertisement click that led the user to the XYZ Travel website. This includes the search query entered, the time of the query, the user's IP address, and user purchase data (i.e., whether the user purchased or not).<sup>1</sup> The dataset contains a total of 2,399,391 raw search cases collected during a one-year span; 172,671 cases were generated by users who made purchases, while 2,226,720 were generated by users who did not. The total number of unique keywords used was 11,221.

Each query in our data set is associated with an IP address and time. We used these IP addresses as a surrogate for a discrete user. Based on IP address and time for each query-click dyad, we aggregated queries into sessions (see Table 1). Based on IP address, the number of unique users in the data set is 1,176,115, of whom 80,840 made purchases. The mean number of query-click dyads per user was 2.13 for purchasing customers and 1.01 for non-purchasing customers.

Table 1  
Examples of query-click dyad sequences.

<table><tr><td>IP address</td><td>n of query-click dyads</td><td>Query-click 1</td><td>Query-click 2</td><td>Query-click 3</td><td>...</td><td>Query-click 15</td></tr><tr><td>158.xxx.xxx.xxx</td><td>2</td><td>Airplane ticket</td><td>Price comparison</td><td></td><td></td><td></td></tr><tr><td>210.xxx.xxx.xxx</td><td>15</td><td>Singapore Airtel</td><td>Guam Airtel</td><td>Airline reservation</td><td>...</td><td>Hong Kong travel</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>165.xxx.xxx.xxx</td><td>1</td><td>Tokyo travel</td><td></td><td></td><td></td><td></td></tr></table>

## 3.2. Session identification

Since the data were collected over the course of 12 months, it is assumed that some queries from the same IP address likely consisted of multiple search sessions. In other words, diferent sets of searches were conducted with diferent intents (e.g., a session in March may have been regarding a hotel booking in Australia, while a session in Apri may have regarded a tour package for central Europe). Given our selection of the search session as our unit of analysis, operationalizing thi concept is of great importance. A study by Göker and He [29] established 11 min as the optimal criterion for separating on-site search sessions. In other words, a gap of 11 min or more between searche indicates that the user has moved on to a new search-related task. By this approach, if the same user's search sequence experienced a break of 11 min or more (i.e., at least 11 min transpire between searches), then the next query represented to us a new search session.

To validate this approach, three graduate students were hired as search session coders and a sample of 5920 queries from 200 randomly selected IP addresses was used. These queries were time-stamped, allowing the coders to determine the time between queries. The coder were then asked to separate the sequences of queries into sessions based on the queries' content using a logical rationale. For instance, if three consecutive queries seemed to refer to a trip Hong Kong, then the fourth to a trip to Hawaii, then a session break could have been identified between the third and fourth queries. Further, if a sequence of search terms included an apparently related purchase, then the search session ended at the purchase, with the next query instigating a new search session. The inter-coder reliability among the three coders was 99.0%, 93.0%, and 93.6%, respectively.

The graduate students' coding was then compared against nine diferent candidate criteria to establish discrete sessions. These in cluded Göker and He's 11-minute criterion, a similar criterion using 24 h instead of 11 min, average of all time intervals for the given IP address, median of all intervals for the given IP address, mean absolute deviation (MAD) of all IP address intervals, mean interval plus two standard deviations, mean interval plus three standard deviations, median plus two MADs, and median plus three MADs.

Among these criteria, we found that the Göker and He criterion performed most reliably. This 11-minute criterion yielded the same results as those coded by the three coders in 68.9%, 71.0%, and 71.7% of cases respectively. The other candidate criteria performed significantly worse, with the highest reliability among them being 55.4%. We therefore adopted this ‘11-minute rule’ as our mechanism for identifying discrete sessions. Using 11 min as the criterion for session separation resulted in the identification of 1,823,539 discrete search sessions, of which 124,589 resulted in a purchase.

## 3.3. Keyword coding

Coding of keyword data presented one of the biggest challenges of this study. This coding is particularly critical as both search session and dimensions of these sessions were coded through this process. Without similar previous studies for guidance, the researchers employed a two-phase approach for keyword coding. In Phase 1, researchers determined a typology for query dimensions (e.g., “location specificity”). In Phase 2, queries were coded by multiple coders, aided by an automated process, according to the criteria developed through Phase 1.

The Phase 1 typology of query dimensions was developed based on a thorough review of random samples of query sequences. After establishing this initial typology, a sub-sample including 40 random users who purchased and 40 who did not purchase was selected from the dataset. This sub-sample was then coded by the researchers individually by hand to verify the validity and replicability of these categorizations. Discrepancies among coding results were discussed and dimensions refined based on these discussions. A second round of sample coding was then completed in a similar manner; researchers coded sample keywords and any disagreements or possible problems were discussed and the coding scheme modified accordingly. After completing an additional, third round of sample coding, the coding scheme was deemed final as agreement had been reached among the researchers using only the criteria set forth in the previous rounds. The dimensions included in the final scheme are shown in Table 2.

Although the terms identified through this process (and included in Table 2) are travel-specific, we expect similar typologies can be reasonably developed and applied for other search advertiser contexts. For example, for an online clothing retailer, location level could be replaced by product depth (e.g., jeans – men's jeans – Levi's men's jeans, etc.), type of airline by product brand or sub-brand, type of activity by main use of product (e.g., casual, formal, work-wear, etc.), and purpose of travel by purpose of purchase (e.g., for self-use, gift, etc.).

Table 2  
Query coding scheme and derived variables.  
```txt
Dimension Description
Location level 0 = N/A, 1 = region (e.g., Europe), 2 = country (e.g., Japan), 3 = city (e.g., Los Angeles), 4 = attraction (e.g., Phuket Beach, Disneyland)
Type of airline 0 = N/A, 1 = domestic airline, 2 = non-domestic airline
Type of activity 0 = N/A, 1 = packaged, 2 = semi-packaged (“Free”) travel, 3 = backpack travel, 4 = transportation only (e.g., airplane, train), 5 = lodging only
Purpose of travel 0 = N/A, 1 = business (e.g., conference, exhibition), 2 = active leisure (e.g., ski, golf), 3 = inactive leisure (e.g., beach, cruise)
Schedule 0 = N/A, 1 = includes a schedule-related term (e.g., “itinerary”)
Reservation 0 = N/A, 1 = includes a reservation-related term (e.g., “booking”)
Purchase 0 = N/A, 1 = includes a purchase-related term (e.g., “buy”)
Price-related 0 = N/A, 1 = includes a weaker price-related term (e.g., “price check”), 2 = includes a stronger price-related term (e.g., “discount”, “lowest price”)
Recommendation 0 = N/A, 1 = includes a recommendation-related term (e.g., “popular”)
Advertiser name 0 = N/A, 1 = includes “XYZ Travel”
Other specificity 0 = N/A, 1 = includes a specific term not captured in the above dimensions
Location depth Difference in location level between first and last queries in a session
Other depth Difference in details of non-location query terms between first and last queries in a session
Location breadth Diversity of queried locations in a session
Other breadth Diversity of queried non-location terms in a session
```

Phase two consisted of both a screening stage and a coding stage. In the screening stage, seven undergraduate research assistants were recruited as coders and asked to screen for and identify specific destina tions, airlines, and other terms frequently appearing in the search queries. Once completed, these terms were used in the coding stage.

During the coding stage, ten people coded queries using Web-based software developed by the researchers specifically for this purpose. A portion of the coding was completed automatically by a text analysis program, which identified commonly used query terms identified in the previous coding stage such as “New York”, “Shanghai”, “backpack” and “Delta”. Following the automatic coding, the remaining observations were then coded manually. For greater accuracy and to reduce sub jective bias, each query requiring manual coding was coded by two independent, randomly assigned coders, thus following the examples set in prior studies (e.g., [30,31]). Any discrepancies were identified and resolved by a third coder, often after discussion with the original coders.

## 3.4. Depth and breadth

## 3.4.1. Location depth and other depth

Testing the efects of specificity of search session queries requires us to define specificity within this data set using the dimensions coded. Here we identified location depth as one measure of specificity and other depth (referring to depth not related to location) as another. Location depth is determined here based on the location level coded as described above (0 = no location, 1 = region, 2 = country, 3 = city, 4 = attraction) of each query. The location depth of a search session was then measured as the mean location depth of all queries within that session.

The other depth measure of specificity captures the level of detail of non-location-related query terms within a search session. Several of the variables identified in Phase 1 and included in Table 2 are associated with search specificity, but are not location-related: type of airline, type of activity, purpose of travel, schedule, reservation, purchase, pricerelated, recommendation. and advertiser name. These variables were combined into a new variable, “other depth”, which we then applied to each query-click dyad and then each search session. Specifically, the number of these variables present for each query was counted as the other depth for the query. For instance, a query of “buy Lufthansa tickets at XYZ travel” would have received another depth score of three, one for a purchase-related term (e.g., “buy”), one for a named airline (e.g., “Lufthansa”), and one for the name of the advertiser (e.g., “XYZ travel”). The other depth value for a session was then calculated by averaging the values of all query-click dyads included in the session.

## 3.4.2. Breadth measurement

Breadth measures the diversity of terms used within a query; as a search session increases in the number of dimensions referenced, the breadth increases. For example, a session may include a query-click dyad for “Tokyo hotel” followed by one for “Tokyo subway”. In thi case, the second query increases the session's breadth since it adds an element (“subway”) belonging to the transportation categorization that was not part of the first query. Similar to our operationalization for depth, we sub-divided breadth measurements into location breadth and other breadth.

Location breadth measures the diversity of locations in a session; the more locations referenced in a session, the greater the location breadth. For instance, a search session that included query-click dyads of “Los Angeles hotel”, “Las Vegas hotel”, and “Hawaii hotel” would have a location breadth of three. Note that nested terms were not considered to add breadth so that a session that began with the term “Japan tours” would not see its location breadth increased by the inclusion of the query “Osaka tours”, since Osaka is nested within Japan.

Table 3  
Breadth and specificity test results, full data set. −2LL = 71,085 (p < 0.001), Nagelkerke R<sup>2</sup> = 0.124, AIC = 655,113.

<table><tr><td>Variable</td><td>B</td><td>SE</td><td>p-Value</td><td>Exp(B)</td><td>Supported?</td></tr><tr><td>Constant</td><td>-3.077</td><td>0.012</td><td>&lt; 0.001</td><td>0.046</td><td></td></tr><tr><td>Location breadth</td><td>-2.535</td><td>0.094</td><td>&lt; 0.001</td><td>0.079</td><td>H1 supported</td></tr><tr><td>Other breadth</td><td>-2.722</td><td>0.052</td><td>&lt; 0.001</td><td>0.066</td><td>H1 supported</td></tr><tr><td>Airline name</td><td>0.271</td><td>0.025</td><td>&lt; 0.001</td><td>1.311</td><td>H2 supported</td></tr><tr><td>Brand name</td><td>0.634</td><td>0.009</td><td>&lt; 0.001</td><td>1.885</td><td>H2 supported</td></tr><tr><td>Location depth</td><td>-0.139</td><td>0.003</td><td>&lt; 0.001</td><td>0.870</td><td>H2 not supported</td></tr><tr><td>Other depth</td><td>0.288</td><td>0.007</td><td>&lt; 0.001</td><td>1.334</td><td>H2 supported</td></tr><tr><td>Session duration</td><td>0.302</td><td>0.001</td><td>&lt; 0.001</td><td>1.353</td><td></td></tr></table>

Table 4  
Confusion matrix with cut-of = 0.0761, full data.

<table><tr><td rowspan="2"></td><td colspan="2">Predicted</td><td></td></tr><tr><td>No</td><td>Yes</td><td>% correct</td></tr><tr><td>Observed no</td><td>527,287</td><td>79,143</td><td>86.95% (specificity)</td></tr><tr><td>Observed yes</td><td>30,829</td><td>21,019</td><td>40.54% (sensitivity)</td></tr><tr><td>Overall</td><td>558,116</td><td>100,162</td><td>83.29% (accuracy)</td></tr></table>

For other breadth of a session, the number of specificity-related dimensions (type of airline, type of activity, purpose of travel, schedule, reservation, purchase, price-related terms, recommendation, and advertiser name) in the query that were present were counted, with thi count being used as the other breadth value for a query-click dyad. After the first query-click dyad of each session, whenever a new specific term is added (e.g. “Tokyo free travel” after “Tokyo airline ticket”), other breadth of the session was increased by 1.

## 4. Analysis

## 4.1. Breadth and specificity

Based on our basic hypotheses, H1 and H2, we expected that user intent could be inferred from attributes of the user's search sessions. Specifically, we hypothesized that attributes of the user's search session can be used to predict whether a user will make a purchase. Since the purchase is a binary variable (either the search session resulted in a purchase or it did not), we conducted a logistic regression analysis to test H1 and H2. As earlier research has found that time spent searching afected user behavior in the broader internet context [32], we also control for total session time in this model.² In order to check for multicollinearity, an OLS regression was carried out prior to the logit analysis [33]. The highest variable inflation factor (VIF) found was 2.47, indicating that no serious multi-collinearity is present. Descriptive statistics and a correlation matrix for referenced variables are omitted due to space limitations, but can be provided upon request. The logit regression results are summarized in Table 3 below and prediction ac curacy in Table 4.

Using the full data set, we found that broader searches (i.e., those less-focused on narrow topics) significantly relate to a lower probability of purchase (hence the odds ratios below 1). This is consistent for both location breadth and other breadth. We also found support for the relationship between other depth and purchasing. Other depth was significantly related to the user making a purchase. Further, both brand name and airline name significantly contributed to higher purchase probability. We note a negative but insignificant efect for location depth.

![](/api/attachments/JWXFWGJM/fulltext/images/7985d44828cef64749f2c4cc2a0d9c670685ceed7ba09c1f38bf52efea1d17ea.jpg)  
Fig. 1. ROC curve, testing set of full data. AUC = 0.6225.

The logistic regression model shown predicts the conditional probability of “Yes” (i.e., a customer purchase) given levels of search breadth and depth. We classify a subject (i.e., predict the purchase propensity of a subject) by applying a threshold, or cutof, to the subject's predicted probability. The ‘sensitivity’ is defined as the proportion of observed “Yes” outcomes classified correctly and the ‘specificity<sup>3</sup>’ is the proportion of observed “No” outcomes classified correctly. Since the cutof works on the trade-of between sensitivity and specificity, the choice of cutof is very important especially for an imbalanced dataset as ours, where a large majority of observations are classified as “No” (i.e., did not make a purchase).

We randomly split our dataset into a training set and a test set (50:50), trained the logistic regression model using the training set, and predicted the purchase probabilities for the test set. Then, we computed sensitivity and specificity for a moderate range of cutof and plot sensitivity versus 1-specificity so as to obtain the receiver operating characteristic (ROC) curve. A good classification rule would have the ROC curve attracted to the top-left corner of the plot with a large area under the curve (AUC). With cutof value = 0.0761, the model accu rately predicts actual purchases 40.54% of the time (sensitivity), and accurately predicts non-purchases 86.95% of the time (specificity), see Fig. 1 and Table 4. The cut-of value 0.0761 was suggested as the point that results in the longest distance from the point of (0,1), which corresponds to the top-left point on the ROC curve. A moderate AUC (=0.6225) supports the prediction power of the classifier based on the logistic regression model for this data set.

However, our prediction model does not perform well in terms of cost: precision = 20.99%, F1-score = 27.65%. This performance is commonly observed while analyzing imbalanced datasets such as ours. Fig. 2 illustrates the distribution of the predicted purchase probabilities, which suggests that the predictive power of our model may be very sensitive to the choice of cut-of value, not surprising given our use of logistic regression. As such, in order to improve prediction accuracy, we adopted a machine learning technique as described in Section 4.4 below.

One of the strengths of this data set is that it contains multiple query-click dyads from the same user within the timeframe necessary to be considered a “search session” based on our criteria explained earlier. We find, however, that the mean number of queries per session is 1.01—in other words, most sessions consist of only one query. What happens, however, when we consider only sessions with multiple queries? Do our hypotheses still hold? To examine this, we divided our data set appropriately and conducted a logistic regression analysis using exclusively search sessions with multiple query-click dyads.<sup>4</sup> The findings are in Tables 5 and 6 below.

We see, then, increased support for the importance of location depth. Airline name became insignificant with multiple-search sessions. However, for website owners who track users over multiple query-click dyads within a single search session, we continue to see the ability of both breadth and depth measures to predict funnel location.

## 4.2. Search session classification

We next analyzed the data to determine whether we could identify categorizable search session characteristics that provide meaningful insight into user intent, again focusing on funnel location. These characteristics included our previously discussed variables: depth (lo cation and other), breadth (location and other), and specificity (combined airline name and brand name). For specificity, we coded the session a 1 if it included either an airline name or a brand name (i.e., if either the airline name or brand name variables were a 1) or, otherwise, a 0. We also included session duration and number of query-click dyads. Because of the presence of the binary specificity variable, categories were identified using a two-step clustering analysis. This approach allowed us to use a mixture of variables (including our dichotomous variable for specificity) and provided a relatively rigorous approach in identifying a “stable” number of clusters. Through this approach, we identified six discernable search patterns (see Table 7 below).

We note here that, based on purchase behavior, two of these groups are clearly lower in the funnel than the other four. These lower-funnel groups, 1 and 2, appear to have a significant separation from the higher-funnel groups in terms of a few key criteria: query count, session duration, and breadth (although this is likely a function of these groups sessions including multiple queries). Thus, those sessions reflecting the lower funnel locations are those with multiple query-click dyads and

![](/api/attachments/JWXFWGJM/fulltext/images/6e5e35eb78edd084ff9ff40610af4d087ac393a222b359cbc8e6d6ec4e39940a.jpg)  
Predicted purchase probability  
Fig. 2. Actual purchases versus predicted purchase probabilities (full data, logistic regression model). The vertical dotted line in the figure is the cut-of value (0.0761).

Table 5  
Breadth and specificity test results, multiple query-click dyad sessions only.  
Table 8

<table><tr><td>Variable</td><td>B</td><td>SE</td><td>p</td><td>Exp(B)</td><td>Supported?</td></tr><tr><td>Constant</td><td>-3.506</td><td></td><td></td><td></td><td></td></tr><tr><td>Location breadth</td><td>-3.151</td><td>0.195</td><td>&lt; 0.001</td><td>0.043</td><td>H1 supported</td></tr><tr><td>Other breadth</td><td>-2.933</td><td>0.094</td><td>&lt; 0.001</td><td>0.053</td><td>H1 supported</td></tr><tr><td>Airline name</td><td>0.043</td><td>0.063</td><td>0.502</td><td>1.044</td><td>H2 not supported</td></tr><tr><td>Brand name</td><td>0.426</td><td>0.025</td><td>&lt; 0.001</td><td>1.531</td><td>H2 supported</td></tr><tr><td>Location depth</td><td>0.014</td><td>0.008</td><td>0.091</td><td>1.014</td><td>H2 weak support</td></tr><tr><td>Other depth</td><td>0.302</td><td>0.019</td><td>&lt; 0.001</td><td>1.352</td><td>H2 supported</td></tr><tr><td>Session duration</td><td>0.201</td><td>0.002</td><td>&lt; 0.001</td><td>1.222</td><td></td></tr></table>

Nagelkerke $R ^ { 2 } = 0 . 2 1 5 , ~ - 2 \mathrm { L L } = 7 6 , 9 5 1 ~ ( \mathrm { p } ~ < ~ 0 . 0 0 1 )$

Table 6  
Confusion matrix, multiple query sessions only.

<table><tr><td rowspan="2"></td><td colspan="2">Predicted</td><td></td></tr><tr><td>No</td><td>Yes</td><td>% correct</td></tr><tr><td>Observed no</td><td>117,877</td><td>916</td><td>99.23%</td></tr><tr><td>Observed yes</td><td>12,927</td><td>1652</td><td>11.33%</td></tr><tr><td>Overall</td><td>130,804</td><td>2568</td><td>89.62%</td></tr></table>

Table 7  
Classification of search session behavior.

<table><tr><td>Variable</td><td>1.</td><td>2.</td><td>3.</td><td>4.</td><td>5.</td><td>6.</td></tr><tr><td>Location breadth</td><td>0.00</td><td>0.42</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Other breadth</td><td>0.68</td><td>1.34</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Location depth</td><td>0.00</td><td>0.65</td><td>0.42</td><td>2.86</td><td>0.06</td><td>0.31</td></tr><tr><td>Other depth</td><td>1.42</td><td>1.03</td><td>2.00</td><td>1.00</td><td>1.00</td><td>1.47</td></tr><tr><td>Specificity</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>Query-click dyad count</td><td>2.94</td><td>2.21</td><td>1.00</td><td>1.01</td><td>1.00</td><td>1.05</td></tr><tr><td>Session duration</td><td>7.55</td><td>4.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td></tr><tr><td>n</td><td>98,703</td><td>22,241</td><td>421,019</td><td>327,901</td><td>300,626</td><td>147,399</td></tr><tr><td>% of sample</td><td>7.5%</td><td>1.7%</td><td>31.9%</td><td>24.9%</td><td>22.8%</td><td>11.2%</td></tr><tr><td>Purchase %</td><td>11.42%</td><td>13.75%</td><td>&lt; 0.01%</td><td>0.03%</td><td>&lt; 0.01%</td><td>0.09%</td></tr></table>

longer durations.

We then conducted an analysis of variance to determine whether these groups varied significantly in their ability to predict funnel location (by predicting purchase behavior) and found that there was a significant efect for group membership at the $\mathsf { p } < 0 . 0 5$ level for the six conditions, $\mathrm { F ( 5 , 1 3 1 7 8 8 6 ) } = 3 1 \mathrm { , } 6 8 1 \mathrm { . } 1 7 9 \mathrm { , ~ p ~ < ~ } 0 . 0 0 1$ . Post hoc comparisons using the Tukey HSD test indicate that the mean of purchases for Group 1 $( \overline { { { x } } } ~ = ~ 0 . 1 4 , ~ s = 0 . 3 4 4 )$ was significantly diferent from Groups 2 through 6. The mean of purchases for Group $2 \ : ( \overline { { x } } \ : = \ : 0 . 1 1$ $\mathbf { s } = 0 . 3 1 8 )$ was significantly diferent from Groups 3 through 6. See Table 8 for descriptive statistics; details of post hoc comparisons can be found in Table 9.

Descriptive statistics for between-subjects ANOVA.

<table><tr><td>Group</td><td>n</td><td>Mean</td><td>S.D.</td><td>S.E.</td></tr><tr><td>1</td><td>98,703</td><td>0.11</td><td>0.318</td><td>0.001</td></tr><tr><td>2</td><td>22,241</td><td>0.14</td><td>0.344</td><td>0.002</td></tr><tr><td>3</td><td>421,019</td><td>&lt; 0.01</td><td>0.002</td><td>&lt; 0.001</td></tr><tr><td>4</td><td>327,904</td><td>&lt; 0.01</td><td>0.018</td><td>&lt; 0.001</td></tr><tr><td>5</td><td>300,626</td><td>&lt; 0.01</td><td>0.002</td><td>&lt; 0.001</td></tr><tr><td>6</td><td>147,399</td><td>&lt; 0.01</td><td>0.030</td><td>&lt; 0.001</td></tr><tr><td>Total</td><td>1,317,892</td><td>0.01</td><td>0.105</td><td>&lt; 0.001</td></tr></table>

Table 9  
Group comparisons. Mean diference shown.

<table><tr><td></td><td>1.</td><td>2.</td><td>3.</td><td>4.</td><td>5.</td><td>6.</td></tr><tr><td>Group 1</td><td>-</td><td>-0.023**</td><td>0.114**</td><td>0.114**</td><td>0.114**</td><td>0.114**</td></tr><tr><td>Group 2</td><td>0.023**</td><td>-</td><td>0.137**</td><td>0.137**</td><td>0.137**</td><td>0.137**</td></tr><tr><td>Group 3</td><td>-0.114**</td><td>-0.137**</td><td>-</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>-0.001*</td></tr><tr><td>Group 4</td><td>-0.114**</td><td>-0.137**</td><td>&lt; 0.001</td><td>-</td><td>&lt; 0.001</td><td>-0.001</td></tr><tr><td>Group 5</td><td>-0.114**</td><td>-0.137**</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>-</td><td>-0.001*</td></tr><tr><td>Group 6</td><td>-0.114**</td><td>-0.137**</td><td>0.001*</td><td>0.001</td><td>0.001*</td><td>-</td></tr></table>

<sup>⁎</sup> Significant at $\alpha = 0 . 0 5 .$  
<sup>⁎⁎</sup> Significant at α = 0.01.

Both groups 1 and 2 are significantly more likely to purchase than groups 3 through 6, suggesting that website owners might reasonably and algorithmically determine user intent and, based on that intent, deliver optimized content

## 4.3. Analysis of compound sessions

It is possible that users do not complete their information search task within a single search session. Instead, users may search for information about products/services of interest through multiple sessions, which we term a compound session. To test if the patterns found in the previous analyses hold for these compound sessions as well, additional analyses have been conducted.

Table 10  
Breadth and specificity test results, compound session data set. $^ { - 2 \mathrm { L L } } = 5 2 , 3 7 6$ (p < 0.001), Nagelkerke R<sup>2</sup> = 0.253, AIC = 269,497.

<table><tr><td>Variable</td><td>B</td><td>SE</td><td>p-Value</td><td>Exp(B)</td><td>Supported?</td></tr><tr><td>Constant</td><td>-0.962</td><td>0.017</td><td>&lt; 0.001</td><td>0.382</td><td></td></tr><tr><td>Avg. location breadth</td><td>-0.854</td><td>0.230</td><td>&lt; 0.001</td><td>0.426</td><td>H3a supported</td></tr><tr><td>Δ(Location Breadth) &lt; 0</td><td>0.752</td><td>0.257</td><td>0.003</td><td>2.121</td><td>H3b not supported</td></tr><tr><td>Δ(Location Breadth) = 0</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>Δ(Location Breadth) &gt; 0</td><td>0.075</td><td>0.275</td><td>0.786</td><td>1.078</td><td></td></tr><tr><td>Avg. other breadth</td><td>-0.731</td><td>0.135</td><td>&lt; 0.001</td><td>0.481</td><td>H3a supported</td></tr><tr><td>Δ(Other Breadth) &lt; 0</td><td>0.627</td><td>0.151</td><td>&lt; 0.001</td><td>1.872</td><td>H3b supported</td></tr><tr><td>Δ(Other Breadth) = 0</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>Δ(Other Breadth) &gt; 0</td><td>-1.200</td><td>0.159</td><td>&lt; 0.001</td><td>0.301</td><td></td></tr><tr><td>Airline name</td><td>0.574</td><td>0.035</td><td>&lt; 0.001</td><td>1.775</td><td>H4a supported</td></tr><tr><td>Brand name</td><td>0.489</td><td>0.013</td><td>&lt; 0.001</td><td>1.631</td><td>H4a supported</td></tr><tr><td>Avg. location depth</td><td>-0.046</td><td>0.002</td><td>&lt; 0.001</td><td>0.955</td><td>H4a not supported</td></tr><tr><td>Δ(Location Depth) &lt; 0</td><td>-2.351</td><td>0.045</td><td>&lt; 0.001</td><td>0.095</td><td>H4b not supported</td></tr><tr><td>Δ(Location Depth) = 0</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>Δ(Location Depth) &gt; 0</td><td>-2.704</td><td>0.050</td><td>&lt; 0.001</td><td>0.067</td><td></td></tr><tr><td>Avg. other depth</td><td>0.094</td><td>0.005</td><td>&lt; 0.001</td><td>1.099</td><td>H4a supported</td></tr><tr><td>Δ(Other Depth) &lt; 0</td><td>-2.474</td><td>0.040</td><td>&lt; 0.001</td><td>0.094</td><td>H4b not supported</td></tr><tr><td>Δ(Other Depth) = 0</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>Δ(Other Depth) &gt; 0</td><td>-2.235</td><td>0.036</td><td>&lt; 0.001</td><td>0.107</td><td></td></tr><tr><td>Session duration</td><td>0.203</td><td>0.002</td><td>&lt; 0.001</td><td>1.225</td><td></td></tr></table>

To analyze compound sessions, our first step is to identify when multiple, related sessions occur. A heuristic approach was employed to identify a user's compound sessions. First, occurrences of consecutive sessions from the same IP address with an intervening interval of less than three days were identified. The three-day period was determined from the marketing literature, which indicates that consumers often defer their decisions for many reasons up to several days without any information searching during that time [34,35]. Second, if a purchase occurred in the first session, the next session was not considered to be part of the same compound session as the second session is highly unlikely to be a continuation of the first one. Finally, we analyzed the efect of shifts of search breadth and depth during a compound session period. First, we identified the compound session and then defined a new dummy variable that indicated an increase and/or decrease of search breadth and depth observed across multiple sessions within the compound session. We then fit a new logistic regression model with the new dummy variables together with an average of two consecutive search breadth and depth levels.

The summary of the fitted model for the compound session data is provided in Table 10. As in the single-session analysis, average location breadth across sessions is negatively related to purchase probability. The average of other breadth is also negatively related to purchase probability. In other words, the broader the searching (i.e., the more varied the subject matter of queries), the less likely the user is to purchase. This finding supports H3a.

Interestingly, the conversion probability is not significantly afected by the location breadth change, while the change in other breadth affects the conversion probability in such a way that a decrease/increase in the other breadth level during a compound session tends to increase/ decrease the conversion probability, which partially supports H3b. Also, we have a supporting result for the relationship between specifi city and conversion during a compound session.

Average location depth of sessions has a positive relationship with purchase propensity, supporting H4a. However, a change in the search depth tends to lower the conversion probability regardless of whether the change reflects an increase or decrease in depth. This is a surprising finding, as we expected that an increase in depth should signal a narrowing of options. However, this unexpected finding may be telling us that changes in depth in fact reflect that the customer is still considering diverse alternatives, thus suggesting that the customer is at the top of the funnel. Regardless, this finding does not support our last hypothesis, H4b (Table 10).

Table 11  
Confusion matrix with cut-of = 0.028, compound session data set.

<table><tr><td rowspan="2"></td><td colspan="2">Predicted</td><td></td></tr><tr><td>No</td><td>Yes</td><td>% correct</td></tr><tr><td>Observed no</td><td>65,366</td><td>31,936</td><td>67.18% (specificity)</td></tr><tr><td>Observed yes</td><td>14,132</td><td>24,014</td><td>62.95% (sensitivity)</td></tr><tr><td>Overall</td><td>79,498</td><td>55,950</td><td>65.99% (accuracy)</td></tr></table>

Table 11 shows the prediction accuracy of the classifier constructed by the new logistic regression model analyzing compound sessions only. The sensitivity (62.95%), specificity (67.18%), overall accuracy (65.99%) and AUC (0.694) in Fig. 3 all indicate acceptable performance from the classification rule. It is noticeable that, unlike in the full data analysis, the precision (42.92%) and hence F1-score (51.04%) are also of a moderate level. Fig. 4 shows the distribution of predicted purchase probabilities.

To check the validity of three-day criterion for compound session searches, we ran the same analysis with three other criteria: one day, one week, and one month. We found that these three criteria showed no significant diferences compared to the 3-day criterion used in this study.

## 4.4. Prediction with XGBoost

Based on the results in the previous section, we built a model to predict purchase propensities using the compound session dataset. For evaluating predicting power, we randomly split the compound session data into training (50%) and test (50%) data sub-sets. For the prediction algorithm, we chose the extreme gradient boosting (XGBoost), a state-of-the-art machine learning algorithm that uses an optimized library of gradient boosting. Utilizing core computations, parallelization, cache optimization, and distributed computing, it creates highly eficient and flexible tree-based learning algorithms.

The explanatory variables used in the previous logistic regression model for compound session data analysis were reused for training our XGBoost machine. Unlike the logistic classification, we do not have to take any efort to determine a cut-of value for ensemble machines. The value of 0.5 was used as the cut-of for the predicted purchase probabilities. Also, XGBoost takes care of potential class imbalance problems by controlling the balance of positive and negative weights.

![](/api/attachments/JWXFWGJM/fulltext/images/da633964093817dd6507b8f847e4486de45bc1b930e1c60f035a7bfec7a20a29.jpg)  
Fig. 3. ROC curve, compound session data set. AUC = 0.694.

![](/api/attachments/JWXFWGJM/fulltext/images/56d94bd97c5588d9b0d0fe8cf464fb517db45404e5b4514b05feb008c70e999f.jpg)  
Predicted purchase probability  
Fig. 4. Actual purchases versus predicted purchase probabilities (compound session data, logistic regression model). The vertical dotted line in the figure is the cutof value (0.3177).

Table 12  
Prediction performance of XGBoost for compound session data.

<table><tr><td></td><td>Accuracy</td><td>Specificity</td><td>Sensitivity (recall)</td><td>Precision</td><td>F1-score</td></tr><tr><td>Test set</td><td>0.6060</td><td>0.5119</td><td>0.8462</td><td>0.4046</td><td>0.5475</td></tr></table>

Table 12 summarizes the performance of the trained XGBoost machine. There is a substantial improvement in sensitivity compared with those from the logistic regression model, although the other measures are at a moderate level. Fig. 5 supports choosing a cut-of of 0.5 for the predicted probabilities, although we still observe many false positive cases (see Fig. 5).

## 4.5. Hypothesis summary

A summary of the hypothesis test results is provided in Table 13. In the table, “Partially supported” means that the hypothesis was supported with some variables (e.g., ‘Other depth’) while it was not supported with other variables (e.g., ‘Location depth’).

## 5. Discussion

## 5.1. Results and implications

As demonstrated in our basic hypotheses (H1 and H2), user intent can indeed be inferred based on characteristics of the user's arrival on a website. Those who arrive having searched for less broad and more specific terms can be expected to more likely be pursuing a low-funnel, high-structure task such as making a purchase, while those who have searched for broader and less specific terms are more likely pursuing a low-structure task.

Interestingly, there are nuances to this. As we saw, not every measure of specificity was significant in predicting funnel location. In the full data set, location depth was insignificant, but was only weakly significant in the sample with only sessions including multiple queryclick dyads. Further, while airline name was significant in the full data set, it was insignificant in the multiple query-click dyad sessions sample. From this, we suggest that while specificity matters, not all types of specificity matter in all cases. From a website owner's perspective, this implies an important need to test various levels and kinds of specificity to determine which are important in predicting low-funnel locations for website visitors. In the case of a consumer electronics manufacturer, for instance, they may find that increased specificity in terms of the company's model numbers is meaningful, but specificity in terms of product features is not.

![](/api/attachments/JWXFWGJM/fulltext/images/36fe8a62d3a993cdacb948b0b726ddd0f55da5ecc4f9b14d5bd60f3a00caa3cb.jpg)  
Predicted purchase probabilities  
Fig. 5. Actual purchases versus predicted purchase probabilities (compound session data, XGBoost)

On the other hand, we found that both measures of breadth, location and other, signal a user who is further up in the purchase cycle. This was found to be the case in all subsets of the data. As users' queryclick dyads became broader and less focused, entailing multiple keyword types (e.g., a destination and a type of transportation, a lodging type and an activity), the more likely they were to be earlier in the funnel. Given that we found this to be true for both forms of breadth and in all cases, we suggest that practitioners may be able to assume that broader queries, regardless of the variety of keyword categories from which they draw, can generally predict early-funnel user intent and therefore low likelihood of purchase.

Further, our user classifications show that user sessions can be segmented into categories that significantly relate to probability of purchase and, thus, to a position further down in the funnel. The cri teria from such a categorization exercise could be used to tailor website experiences to the predicted user intent based on search session query information delivered electronically to the website for the arriving visitor. For instance, those users whose intent is algorithmically determined to be more probably late-funnel might be directed to a landing page that is more geared toward sales messaging in order to better facilitate the completion of a transaction. Those users who are earlier in the funnel, on the other hand, may be given an experience aimed at guiding them toward a later funnel stage with special ofers or perhaps a better experience with navigation featuring stronger information scent [36] and that can guide such users toward later stages of the funnel.

Further, as mentioned, sponsored search campaigns represent large marketing investments. Websites themselves can be very resource-intensive to design, build, and maintain. Understanding the user's intent upon arrival can help website owners optimize that user's experience, for instance by focusing on helping the user complete a high-structure task eficiently or in presenting more information in an accessible way to help users with a low-structure task to begin the information win nowing process. This study represents a first attempt at discerning user intent based on information passed to the website upon arrival. It may be that other arrival types (e.g., those coming from a search engine, those coming via direct URL entry, etc.) can further strengthen the ability of website-owning firms to infer intent.

We also found that the vast majority of searches do not result in latefunnel activities. This preponderance brings to the fore the question of the ability of companies to place a value on such searches in order to place appropriate bids through sponsored search and to evaluate expenditures against user behavior. Further, while these users may not be in the late-funnel purchasing mode, it may be useful to understand how early in the funnel they might be. If a firm understands that a user is still determining whether a product is needed, it may be beneficial to communicate with that user in a diferent way than would be most appropriate for a user who has already decided that the product is needed and is now comparing models against one another. Diving even more granularly into specific qualities of search session queries may shed further light on the intent of users and, thus, enable website owners to estimate more accurately the funnel positions of website visitors. This may be a useful avenue for future research.

Table 13 Hypothesis test results.

<table><tr><td colspan="3">Hypotheses</td><td>Test results</td></tr><tr><td>H1</td><td></td><td>Users searching narrowly will be more likely to purchase products than those searching broadly.</td><td>Supported</td></tr><tr><td>H2</td><td></td><td>Users searching more specifically will be more likely to purchase products than those searching less specifically.</td><td>Partially supported</td></tr><tr><td rowspan="2">H3 (breadth)</td><td>H3a</td><td>Users searching more narrowly in multiple search sessions will be more likely to purchase products than those searching broadly across sessions.</td><td>Supported</td></tr><tr><td>H3b</td><td>Users narrowing search breadth in the second session will be more likely to purchase products than those broadening search breadth in the second session.</td><td>Partially supported</td></tr><tr><td rowspan="2">H4 (depth)</td><td>H4a</td><td>Users searching more specifically in multiple search sessions will be more likely to purchase products than those searching broadly across sessions.</td><td>Supported</td></tr><tr><td>H4b</td><td>Users increasing search specificity in the second session will be more likely to purchase products than those decreasing search specificity in the second session.</td><td>Not supported</td></tr></table>

Our compound session analysis shows that the efects of average breadth and depth throughout sessions are similar to those of single sessions. However, for users engaging in compound sessions with a website, the change in search breadth across the sessions seems to be a more significant indicator of purchase than the change in depth. We speculate that customers who change depth of search are still in an earlier stage of the funnel, and once they arrive at later stage, they are less likely to change the depth. This needs more research to provide better understanding about users' online purchase behaviors.

## 5.2. Limitations

We acknowledge several limitations to our findings. First, while the study builds on theory in several respects (our conceptualizations of user intent and the user search session, for instance), the analysis of the data is largely atheoretical. We follow in this a body of IS research that uses the data itself to inform research [32]. While this approach en abled us to make discoveries regarding the usefulness of breadth and specificity, we acknowledge that without the support of a greater body of established theory, generalizability of our findings may not be entirely reasonable.

Relatedly, our dataset comes from a specific advertiser (an Asian travel agency). While we do not expect that customers from other regions of the world or customers of other product types would difer significantly in their behavior and would thus invalidate our findings with regard to predicting user intent, it may be useful to replicate this study in other contexts to verify that this is the case. Further, while our dimensions of specificity included details such as “airline name” and depth was specific to “location”, we feel that these concepts would have cognates in other industries. We note that identifying such cognates would be an important step in applying our findings to other contexts and data sets.

We also note that this study uses as its unit of analysis not the individual, but rather the user search session made up of one or more query-click dyads. This decision was made so as to isolate the user's information seeking and purchase process for the purchase of a single item. Looking at a user's activities among various discrete sessions would potentially capture multiple buying processes (e.g., Process A to book a trip to Fiji, Process B to find airfares for relatives coming from California, Process C to book an all-inclusive leisure tour to Hong Kong). However, by taking this approach and basing sessions as we did on time gaps between searches, we may have inadvertently separated individual search processes. While this may have thereby reduced predictive power of the analysis, we feel this was nevertheless a conservative approach since it would have only served to decrease the likelihood of finding significant results. Future researchers may wish to explore additional alternative means of identifying discrete sessions in order to increase the predictive power.

Similarly, in our coding of data, we considered unique IP addresses to indicate unique individuals. This may not always be the case, for instance if the same IP address is shared by multiple work associates at the same ofice or multiple members of the same household. On the other hand, using this approach allows us to use ecologically valid field data such as the dataset used here and still make inferences regarding individual user behaviors. Further, from the point of view of practitioners hoping to gain insight into their users, IP addresses may be the best data available to them as well with which to identify unique users. Finally, as noted, we believe that this represents taking a conservative approach in identifying unique users. Cases wherein the same IP address actually represents multiple distinct users are a potential source of noise and would only reduce, rather than increase, predictive power. Nevertheless, future researchers may wish to find approaches to better isolate individual users, perhaps through collecting cookie data, using intercept surveys, or conducting laboratory experiments.

Predictions within this analysis make an assumption that all users coming by way of a search engine are seeking to complete a task. It is possible that some intents cannot be so construed. While one may argue that even a hedonic purpose remains a “task” when it involves using an online search engine, it may be useful for future researchers to study hedonic searches in isolation as has been done in other areas of the information systems literature.

We also note that what we capture is specifically limited to characteristics of the user's search and data captured once the user lands on the company's website. Given the nature of the data, we were unable to capture other online searches that did not result in a click leading to this particular travel agency let alone other information gathering attempts that may have happened online or of. We are also unaware of other behaviors or transactions that users may have taken as a result of their searches (e.g., purchasing similar travel through another website, making an ofline purchase at a physical travel agency, talking to coworkers about their decision options). That said, the focus of this study is to understand what an online advertiser can glean from the limited information available through a user who clicks through on a search advertisement. Further research that captures other search behaviors along with those undertaken at a search engine as well as transactions that take place through various channels would be a useful future addition to this stream of research.

Finally, while this research remains an important first step in predicting user intent upon arrival on a website, it does so only within the specific context of a user arriving via search engine. The field would benefit from research and discoveries regarding arrival through other means and mechanisms.

## 5.3. Conclusion

This research contributes to the literature by introducing a typology for search query keywords as well as the concept of the user search session in the sponsored search context. We further introduced the use of the purchase funnel as a means of describing user intent and showed the parallels between this approach and the concepts of problem solving [23] and task structure [26]. These can be particularly helpful in fostering further research into the meanings and implications of user search terms as well as enabling future researchers to isolate purchase and task processes.

Further, we showed how a dataset can be used to track user search processes across multiple searches. From this, we showed not only that search term breadth and specificity matter, but also contributed the idea that diferent types of specificity may matter diferently or not at all. We also made a contribution by showing that, indeed, a user's intent can be inferred based on information related to the user's means of arrival. This possibility of inferring user intent upon arrival can be of great use for website owners seeking to improve the success of their websites by adjusting user experience based on such inferred intent.

## References

[1] L. Deng, M.S. Poole, Afect in web interfaces: a study of the impacts of web page visual complexity and order, MIS Ouarterly 34 (2010) 711–730

[2] P.B. Lowry, J. Gaskin, G. Moody, Proposing the multi-motive information systems continuance model (MösC) to better explain end-user system evaluations and con: tinuance intentions, Journal of the Association for Information Systems 16 (2015) 515-579.

[3] S. Nadkarni, R. Gupta, A task-based model of perceived website complexity, MIS Ouarterly 31 (2007) 501–524

[4] A. Nosshi, A. Saad, M.B. Senousy, New trends and challenges of internet marketing Asia Pacific Journal of Information Systems 25 (2015) 337–355.

[5] PwC, IAB Internet Advertising Revenue Report, Interactive Advertising Bureau (IAB), (2017).

[6] Econsultancy.com, State of Search Marketing Report, (2017).

[7] A. Ghose, S. Yang, An empirical analysis of search engine advertising: sponsored search in electronic markets, Management Science 55 (2009) 1605–1622.

[8] B. Edelman, M. Ostroysky, Strategic bidder behavior in sponsored search auctions Decision Support Systems 43 (2007) 192–198.

[9] B. Edelman, M. Ostrovsky, M. Schwarz, Internet advertising and the generalized second-price auction: selling billions of dollars worth of kevwords, American

Economic Review 97 (2007) 242–259.

[10] P. Milgrom, Simplified mechanisms with an application to sponsored-search auc tions. Games and Economic Behavior 70 (2010)

[11] S. Yao, C.F. Mela, A dynamic model of sponsored search advertising, Marketing Science 30 (2010) 447–468

[12] A. Animesh, V. Ramachandran, S. Viswanathan, Quality uncertainty and performance of online sponsored search markets: an empirical investigation, Information Systems Research 21 (2010) 190–201.

[13] O.J. Rutz, R.E. Bucklin, From generic to branded: a model of spillover in paid search advertising, Journal of Marketing Research 48 (2011) 87–102.

[14] R.D. Blackwell, P.W. Miniard, J.F. Engel, Consumer Behavior, 10th ed., Thompson, South-Western, 2006.

[15] G.J. Browne, M.G. Pitts, J.C. Wetherbe, Cognitive stopping rules for terminating information search in online tasks, MIS Quarterly 31 (2007) 89–104.

[16] E.S.E. Lewis, Catch-line and Argument, The Book-keeper, (1903), p. 124.

[17] R.J. Lavidge, G.A. Steiner, A model for predictive measurements of advertising efectiveness, Journal of Marketing 25 (1961) 59–62.

[18] O'Brien, Stages of consumer decision making, Journal of Marketing Research 8 (1971) 282–289.

[19] B. Ives, G. Learmonth, The information system as a competitive weapon, Communications of the ACM 27 (1984) 1193–1201.

[20] R.L. Andrews, T.C. Srinivasan, Studying consideration efects in empirical choice models using scanner panel data, Journal of Marketing Research 32 (1995) 30–41.

[21] D.H. Gensch, A two stage disaggregate attribute choice model, Marketing Science 6 (1987) 223–231.

[22] T.J. Gilbride, G.M. Allenby, A choice model with coniunctive, disiunctive and compensatory screening rules, Marketing Science 23 (2004) 391–406.

[23] H.A. Simon, The New Science of Management Decision, Harper & Brothers, New York, NY, 1960.

[24] R. Kohli, S. Devaraj, M.A. Mahmood, Understanding determinants of online con sumer satisfaction: a decision process perspective, Journal of Management Information Systems 21 (2004) 115–136.

[25] K. Byström, K. Järvelin, Task complexity afects information seeking and use, Information Processing and Management 31 (1995) 191–213.

[26] D.J. Campbell, Task complexity: a review and analysis, Academy of Management Review 13 (1988) 40–52.

[27] G.J. Biehal, D. Chakravarti, Information accessibility as a moderator of consumer choice, Journal of Consumer Research 10 (1983) 1–14.

[28] I. Im, J. Jun, W. Oh, S.-O. Jeong, Deal-seeking versus brand-seeking: search beha viors and purchase propensities in sponsored search platforms, MIS Quarterly 40 (2016) 187–204.

[29] A.S. Göker, D. He, Analysing web search logs to determine session boundaries for user-oriented learning, Lecture Notes in Computer Science 1892 (2000) 319–322.

[30] M.-C. Boudreau, D. Gefen, D.W. Straub, Validation in information systems research: a state-of-the-art assessment, MIS Quarterly 25 (2001) 1–16.

[31] P. Shrivastava, Rigor and practical usefulness of research in strategic management, Strategic Management Journal 8 (1987)

[32] E.J. Johnson, W.W. Moe, P.S. Fader, S. Bellman, G.L. Lohse, On the depth and dynamics of search behaviour, Management Science 50 (2004) 299–308.

[33] S.W. Menard, Applied Logistic Regression, 2nd ed., SAGE, Thousand Oaks, CA,

2002.

[34] S.M. Broniarczyk, J.G. Grifin, Decision dificulty in the age of consumer empowerment, Journal of Consumer Psychology 24 (2014) 608–625.

[35] N.T. Thai, U. Yuksel, Too many destinations to visit: tourists' dilemma? Annals of Tourism Research 62 (2017) 38–53

[36] S.K. Card, P. Pirolli, M.V.D. Wege, R.W. Reeder, P.K. Schraedley, J. Boshart, Information scent as a driver of web behavior graphs: Results of a protocol analysis method for web usability, SIGHCI Conference on Human Factors in Computing Systems, ACM, Seattle, WA, 2001, pp. 498–505.

Il Im is a professor of Information Systems at Yonsei University. He received his Ph.D from Marshall School of Business, University of Southern California. Before joining Yonsei faculty, he taught at College of Computing Sciences, New Jersey Institute of Technology. His research areas include recommendation systems, technology adoption, and impacts of smart IT on human behaviors. He has published his work in MISQ, Information & Management, ACM Transactions on Information Systems, Technovation, etc.

Brian Kimball Dunn is an assistant professor of management information systems at the Huntsman School of Business at Utah State University. After a 10-year career in industry in e-commerce and online marketing. he received his PhD in information systems from the University of Pittsburgh. His research interests include the effects of human-computer interaction on brand-related outcomes and user behavior within digital content platforms. His work has been published at Information Systems Research, European Journal of Information Systems, AIS Transactions on HCI, and other venues

Dong Il Lee is a professor of Marketing at School of Business at Seiong University. He received his Ph.D. from School of Business. Seoul National University. He has published in Journal of Business Research, Journal of Global Academy of Marketing Science, International Journal of Electronic Customer Relationship Management about e-Commerce, buzz difusion, and online consumer behaviors. His research areas include trust building of e-Commerce, online advertising management, online consumer's path analysis, and online buzz difusion.

Dennis F. Galletta is an AIS Fellow, a LEO awardee, Fryrear Faculty Fellow and Professor at the University of Pittsburgh, where he serves as Doctoral Director for the Katz Graduate School of Business, He has published in JMIS, MISO. ISR. MgtSci. EJIS, JAIS, etc., and has served on editorial boards such as IMIS. MISO. ISR, and JAIS. He won a “Developmenta Editor Award" at the MIS Ouarterly in 2006 and a Provost's Mentorship Award in 2016 He was program co-chair for ICIS 2005 and AMCIS 2003, chaired the first AMCIS in 1995, and co-chaired ICIS 2011. He served as AIS President, ICIS Treasurer, AIS Council Member, and Editor-in-Chief of AISWorld. He is a founding co-Editor in Chief of AIS Transactions on HCI from 2008-present. He taught IS courses on the Fall 1999 Semester at Sea vovage and established the concept of Special Interest Groups in AIS in 2000

Seok-Oh Jeong is a professor of Statistics at Hankuk University of Foreign Studies. He received his Ph.D. from Seoul National University in 2002. His research interests include large scale inference, statistical learning, causal inference, and neuroimaging.
