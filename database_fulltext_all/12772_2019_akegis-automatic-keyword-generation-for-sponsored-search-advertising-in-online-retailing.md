---
otero_id: 12772
otero_key: "YAWHN87X"
title: "AKEGIS: automatic keyword generation for sponsored search advertising in online retailing"
authors: "Michael Scholz; Christoph Brenner; Oliver Hinz"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.02.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# AKEGIS: automatic keyword generation for sponsored search advertising in online retailing

![](/api/attachments/YAWHN87X/fulltext/images/3fda57618128500c85f1f4d6c017d1a76438e67296028994c02a57b5ad13d2f9.jpg)

Michael Scholz<sup>a</sup>, Christoph Brenner<sup>b</sup>, Oliver Hinz<sup>b,\*</sup>

<sup>a</sup> University of Passau, Innstr. 43, Passau 94032, Germany

<sup>b</sup> University of Frankfurt, Campus Westend, Theodor-W.-Adorno Platz 4, Frankfurt am Main, 60323, Germany

## A R T I C L E I N F O

Keywords: Keyword generation Sponsored search advertising Empirical evaluation Diference-in-diference Conversion rate Customer journey

## A B S T R A C T

Sponsored search advertisers face several complex decisions when planning and implementing a new sponsored search advertising campaign. These decisions include the selection of keywords, the definition of landing pages, and the formulation of bidding strategies. Relatively low attention has been paid on supporting the selection of keywords in recent research and most studies on sponsored search advertising focus on the formulation of bidding strategies and strategies for budget planning. We present a novel approach for automatically generating sponsored search keywords that relies on the theory of consumer search behavior. Our approach uses an online store's internal search log to extract keywords used by consumers within their search process, because recent research has shown that especially consumers with a high conversion probability that exhibit goal-directed instead of exploratory search patterns use an online store's internal search engine. We empirically test our approach based on a store's internal search engine and identify the efects of this approach by comparing it to a state-of-the-art approach. Our analysis reveals that our approach substantially increased the number of profitable keywords, improved the store's conversion rate by approximately 41%, and decreased the average cost per click by more than 70%.

## 1. Introduction

Sponsored search advertising (SSA) has emerged as a new form of Internet advertising in the last decade and is the prevailing business model for generic search engines like Google or Bing. In 2017 search revenues totaled \$40.6 billion in the United States alone which represents 46% of total internet advertising revenue [26]. Consumers typically accept this kind of advertising and prefer it over other forms, such as banners, because providers deliver only ads that match the consumer's search requests. Advertisers thus spend a larger share of their advertising budgets on SSA. Advertisers usually bid at auctions for specific keywords and face in this process some complex decisions that largely afect the profitability of SSA campaigns [15]. First, advertisers need to determine the relevant keywords for which they want to place bids. Second, advertisers need to define for each keyword the page (i.e., landing page) to which search engine users will be directed when clicking on the advertiser's ad. Third, they need to set a budget for their SSA campaign. And fourth, they need to determine bids that will result in a high conversion rate and ultimately high profits or customer lifetime values.

Recent research has mainly focused on determining optimal bids [4,36,53,64], budget optimization [20,33,42,63], and the efects of diferent types of keywords on an advertiser's sponsored search performance [17,27,29,38,46]. Although researchers and practitioners provide evidence which types of keywords are rather profitable, the generation of concrete keywords is still one of the major challenges advertisers face [54]. The keywords should somehow relate to the ad. vertised goods and they should be used in queries by consumers who are likely to click on a sponsored link and ultimately make a purchase. In recent years, a limited number of studies, e.g., [31,55], proposed methods to automatically or semi-automatically expand an existing keyword set. All these methods need an initial keyword set and thus are not suitable to completely automatically generate sponsored search keywords. However, the automatic generation of keywords constitutes one of the most promising areas of SSA because nowadays the manual generation of typical campaigns with more than 10,000 keywords is time-consuming while the limitation to a few thousand keywords is certainly not optimal in terms of profits.

This manuscript aims to close this gap with an approach for automatic keyword generation. To come up with a theory-driven design, we review studies on consumer search and decision behavior and provide in initial empirical studies strong evidences that keywords used in onthe-store searches seem to be promising candidates for sponsored search advertising. Our approach for automatic keyword generation (AKEGIS) relies on these findings and automatically i) generates sponsored search keywords, ii) identifies landing pages, and iii) suggests keywords that should be paused for SSA. In an empirical investigation of two large-scaled online stores, we show that AKEGIS clearly outperforms manual experts (state-of-the-art approach) in generating keywords. It generates three times more profitable keywords, reduces the average cost per click and increases the online store's conversion rate.

## 2. Keyword generation

We briefly describe the process of sponsored search advertising from the perspective of an advertiser in this section and then review literature on generating keywords for sponsored search advertising.

## 2.1. Sponsored search advertising

Search engine or sponsored search advertising is an advertising form where advertisers can display text ads near the organic search results in generic search engines, such as Google or Bing. The position of the ads depends on the advertisers' bids for the keyword and on the advertiser's quality factor. For every search, the resulting position is determined in a continuous auction.

As a first step in the process of getting the ads online, the adver tiser carries out keyword research to determine for which searches conducted by a consumer an ad should be displayed. There are sev eral tools and approaches, such as Google Broad Match, available tha help advertisers expanding and refining their keyword set [2,5]. As a second step, the advertiser has to set up a campaign structure in which keywords have to be booked (several match types are possible, such as “exact match” or “broad match”), ad texts need to be written, landing pages for every ad within the campaign structure have to be defined, and bids must be determined. Existing studies, for example, investigate strategies for determining bids [66] or creating ads [22]. The third step is to activate all the campaigns, including the assign ment of a budget [63], and then these ads take part in the auctions to determine the position of the advertiser's ad per keyword searched by a user. To optimize the bids, there are many bid management tools and approaches available that are able to adjust the bids for every keyword several times per day depending on the performance data of the ad. In this field. much research has already been conducted [3,4,13,17,29,47,53,62,65,66]. The next step is the control ling and monitoring phase. Once the setup is completed and the ads are active, performance data needs to be checked to determine which keywords worked well in terms of the costs of the purchased trafic and the conversion behavior on the landing page and the website. Since SSA is a performance marketing channel, booked keywords or campaigns are measured against various success criteria. Keywords which e.g. generate many clicks but achieve only few conversion such as very generic keywords or also keywords for which the shop does not carry any products will be permanently down-bidded and thus do not generate any ads at some point. This can be the case if a retailer for example bids on keywords related to product categories they do not sell. Ayanso and Mokaya [7] provide an approach fo evaluating the efficiency of search advertiser profiles that helps to identify important efficiency measures that should be used to monitor SSA campaigns. Unprofitable keywords will be lowered in their bid, or – if necessary – paused or even deleted, and the process of keyword research starts again as an ongoing procedure because the search behavior of users could change, or new products could be available in the advertiser's online store.

Table 1  
Sources and approaches for keyword generation.

<table><tr><td>Source</td><td>Approach</td></tr><tr><td>Tools</td><td>Wordy, TermsNet, Google Keyword Planner, SEMRush</td></tr><tr><td>External websites</td><td>Crawling and Extraction</td></tr><tr><td>Own website</td><td>Product Feed Permutation, Crawling and Extraction</td></tr><tr><td>Manual</td><td>Brainstorming, Expertise</td></tr></table>

## 2.2. Existing approaches for keyword generation

A major challenge for advertising companies is the generation of the keywords for which they would like to be listed. Table 1 provides an overview about the main sources for keyword research and the related approaches. The main diference of the various approaches is the source of data used. On the one hand, own data such as product information or the attributes of products or services can be used as well as information texts or other website content. On the other hand, third party data or information can be used, like an analysis of a competitor website. Regardless of the source, there are many diferent approaches and tools which use diferent systematics and procedures. A simple practical approach widely used in the retail segment is the permutation of one's own product feed. The product attributes are combined to generate keywords. In this way, it is possible to generate a very large number of keywords. There are many free online tools [9,45,67] as this is a well and long known procedure [50]. However, the disadvantage is that this approach can create keywords that do not lead to clicks and conversions in real settings at the end of the day and therefore produce a massive overhead. Several online tools, such as Wordy or TermsNet [2,31], generate keywords for a given set by adding synonyms and morphological forms of the given keywords. In other words, these tools are able to find keywords that are semantically similar to given initial keywords. The most widely used tool Google Keyword Planner [19] allows to identify keywords for specific topics and gives further keyword suggestions. Google's auto-completion is used by both Ubersuggest [44] and Keyword Tool [34] which also uses the autocompletion of Youtube, Bing, Amazon and some other big websites to generate keywords. SEMRush [51] allows retailers to find out at which keywords ads other websites are displayed and thus enables a competitive analysis. Other Tools like WordStream [60] combine the approaches competitive analyses, topic research and semantic word relations.

Advertisers who do not use such tools to expand their keyword sets can make use of the broad match (or advanced match) methodology, a type of matching that search engines such as Google, Yahoo! or Bing ofer their advertisers [5]. Broad match automatically places bids for keywords that are semantically similar to those an advertiser has explicitly specified. If, for example, an advertiser wants to bid for the keyword “black shoes”, broad match is suitable to also place bids for misspelled keywords such as “black shoos” or “blak shoes” and for related keywords such as “dark shoes”. Related keywords often are perceived as slightly diferent by consumers, so that they expect to get other products when clicking on a sponsored link. This is, however, not possible if keywords are expanded using broad match. The two keywords “black shoes” and “dark shoes” in our example are booked for one and the same ad and finally forward users to one and the same landing page. In contrast to tools like Wordy or TermsNet, broad match is based on search queries at generic search engines like Google and seems to generate more relevant keywords for sponsored search advertisers.

Query logs of generic search engines also have been used in recent research to generate a set of relevant keywords [16]. The idea of such an approach is to start with a set of URLs relevant to a specific keyword and to identify those queries submitted to the generic search engine that have led to clicks on the URLs in the start set. Although this strategy will lead to keywords not related to those initially defined, there is no guarantee of finding keywords that are indeed relevant for a particular advertiser. Another approach proposes using query logs from generic search engines to compute co-occurrences between given and potential other keywords to expand an initial set of keywords [57].

Further approaches expand an initial keyword set by extracting keywords from the website of the advertiser [41,54,55], by semi-au tomatically extracting keywords from websites that are equal to the advertiser's website [61], by extracting keywords from web search results [10,11] or by extracting keywords from Twitter [56]. These approaches use and extend algorithms for query expansion [30] that have been developed in order to improve the quality of search engines.

Although some approaches have provided initial evidence that they can produce relevant sets of sponsored search keywords, all mentioned semi-automated approaches are subject to three major limitations: i) they require an initially defined set of relevant keywords or URLs, ii) they are not well suited for advertisers with a frequently changing product assortment and hence the need for a permanent and instantaneous generation of keywords, and iii) they are only partially based on empirical evidence for example regarding the amount of keywords generated and in particular with respect to performance measures, such as conversion rate and sales<sup>1</sup>.

## 3. AKEGIS – an automatic keyword generation approach

We propose our approach AKEGIS for automatic generation of sponsored search keywords in this section. We first review research on consumer search behavior and then provide empirical evidences that an online store's search engine log may provide a list of promising keyword candidates for SSA. In such logs the search behavior and the usage of keywords during the customer journey is stored for further analysis and optimization processes regarding the internal search quality. Usually most of the online shops today store this kind of information. Thereafter, we introduce the core algorithm of our proposed approach.

## 3.1. Theoretical foundation

The design of AKEGIS is based on a rather simple idea but it also deeply rooted in theory. Two requirements have to be fulfilled to make data from internal search engines promising for keyword generation in SSA. First, the right kind of customers need to be attracted through these keywords and second, the overlap between keywords used in generic and internal search engines must be suficiently large. We will test the two prerequisites by analyzing transactional data and by means of a laboratory experiment.

## 3.1.1. Conversion funnel

Advertisers attempt to make profits with SSA campaigns. If con sumers search for a certain keyword in a generic search engine, the search engine displays an appropriate ad if the keyword was booked by a company and this ad should attract consumers to click on it, visit the advertiser's online store and finally convert there to purchasers. Interestingly, keywords used by consumers with a high conversion probability have on average a low cost per click [22]. Therefore keywords used in SSA improving an online store's conversion rate thus are on average more profitable for the online store than keywords that do not improve the conversion rate. A keyword generation approach for SSA should hence generate keywords that are used by consumers in search engines with a high conversion probability.

Previous research has shown that consumers' search activities and conversion probabilities difer across consumers with diferent types of search behavior [40] and at diferent stages of the purchase process [29]. Research on ofline consumer behavior has identified two types of search behavior: goal-directed versus exploratory search [28]. This dichotomy has been found to also hold for online consumers [40,43,52]. Consumers who already have a specific purchase in mind or planning to make a specific purchase in the near future are interested in information for their purchase decision and hence search with goal-directed patterns. These consumers search for the actual price of a product, look for a specific brand or compare two or more products. Search patterns of goal-directed consumers focus on the goal of making a purchase decision. Goal-directed consumers thus directly benefit from information which helps them make a purchase decision whereas consumers exhibiting patterns of exploratory search rather benefit from the browsing experience [43]. Consequently, goal-directed consumers show higher conversion probabilities than exploratory consumers [40]. In terestingly, goal-directed consumers make significantly more often use of internal search engines of online stores [40]. The class of consumers who use an online store's internal search might hence be more likely to convert to purchasers.

We investigate the conversion rates of consumers using an online store's internal search and consumers not using the internal search based on a dataset for a large European online store. This investigation helps us to determine whether users of a store's internal search engine i) have a higher conversion probability than other users and ii) are more likely to consult a generic search engine (that ofers sponsored search results) before entering an online store. The focal online store ofers clothes, shoes, furniture, electronics, toys, and handyman products. Consumers can get access to products by searching for them with the internal search or by using the navigation menu. Our dataset includes the daily number of online store visitors and purchasers, separated by the usage of the store's internal search engine (83 days). Table 2 provides a description of the aggregated data.

The conversion rate of consumers who employed the online store's internal search is significantly higher than the conversion rate of all other consumers $( p < 0 . 0 0 1$ , tested with a binomial test). 7.46% of consumers who consulted the internal search converted to purchasers whereas only 1.52% of consumers who did not use the internal search finally purchased anything in the store. The conversion rate is usually between 2.5 and 3% in the investigated store, so that the diference of approximately 6 percentage points is really tremendous. Table 2 also shows that a significantly higher percentage of visitors who consulted the internal search engine than who did not, consulted a generic search engine before entering the store $( p < 0 . 0 0 1 )$ . Consumers who have a higher conversion probability hence are more likely to i) visit a generic search engine before entering an online store and ii) consult the online store's internal search engine. Keywords used at internal search engine are thus promising candidates for SSA campaigns on generic search engines.

## 3.1.2. Overlapping search behavior

Although these results are promising, it is unclear which keywords consumers who consult the internal search engine use in their queries at generic search engines. Because advertisers can easily extract keywords from their internal search engines, it is especially of interest if goal directed consumers who use an online store's internal search enter similar keywords there and at generic search engines. Based on previous research. the expectable results are not that clear:

On the one hand, consumers are querying for multiple retailers in their first search query of an online purchase process whereas they are focused on rather one retailer in the later search queries [12]. Keywords used for the first search query are furthermore more generic than the keywords used for later searches [12]. Because consumers consult a generic search engine rather before an online store's internal search engine [6], keywords entered in both types of search engines might vary. Keywords entered in the online store's internal search engine are likely to be more specific and rather product- than retailer-related.

On the other hand, research in psychology has shown that information that is most salient is likely to be overweighed by human decision makers [32,59]. This phenomenon is known as ‘focalism’ and has been demonstrated to influence a person‚s actions [18,48]. Attributes and characteristics the desired product should have can be con sidered as such information. Also, keywords entered in a generic search engine might be more salient to consumers when entering an online store right after consulting a generic search engine and using the online store's internal search. We hence can alternatively hypothesize that goal-directed consumers will enter rather similar keywords in a generic and in an online store search engine.

Table 2  
Descriptive data about online store visitors for 83 days.

<table><tr><td>Variable</td><td>No internal search</td><td>Internal search</td></tr><tr><td>Total number of store visitors</td><td>116.97 mill.</td><td>27.71 mill.</td></tr><tr><td>Average number of store visitors per day</td><td>1,409,325</td><td>333,840</td></tr><tr><td>Percentage of store visitors who consulted a generic search engine before entering the store</td><td>35.52%</td><td>42.95%</td></tr><tr><td>Average number of purchasers per day</td><td>21,419</td><td>24,908</td></tr><tr><td>Average conversion rate (CVR)</td><td>1.52</td><td>7.46</td></tr></table>

Which of the two contradicting efects dominates, is an empirical question that we aim to answer in an experiment. We therefore conduct a controlled laboratory experiment in which subjects must search for products for a person they personally know. The participants were requested to search with i) an online store's internal search engine for products in an all-purpose online store that ofers clothes, toys, furniture, electronic products and much more and ii) the generic search engine Google. We used two categories of products: ofice furniture and home multimedia products. We decided to use ofice furniture and home multimedia as the product categories because i) many products are available in these categories, ii) several keywords are possible when searching for products in these categories, iii) our participants (students) are familiar with ofice furniture and home multimedia products, and iv) ofice furniture can be rather considered as search goods whereas home multimedia products can be rather considered as ex perience goods [25]. Each participant either searched for i) ofice furniture with Google and home multimedia products within the online store or ii) for ofice furniture within the online store and for home multimedia products with Google. We used this between-subiects design to keep the sample size rather small while avoiding carry-over efects when using both search engines to search for the same product category. The participants were requested to suggest products for pur chase to ensure that they will use goal-directed search patterns. We did not investigate the search behavior of exploratory consumers in our experiment because there is strong evidence that consumers expressing exploratory patterns rarely consult internal search engines [40]. Forcing participants with an exploratory search behavior to use an internal search engine would thus create biased results. The participants searched for products without any time or budget restrictions. As soon as a participant has finished her search tasks, she completed a survey in which she had to list each furniture/multimedia product she recommends purchasing with its name and price.

We manipulated an existing typical online store for the experiment by disabling the navigation through categories and the filtering of products. More specifically, we implemented an individual CSS file that disabled several HTML elements for category navigation and filtering. The CSS file was loaded and executed before the browser rendered the websites so that the participants were not able to take notice of this manipulation. This approach ensures that the participants indeed employed the online store's internal search to fulfill their tasks. We invited 300 participants to take part in the experiment. In total, 97 undergraduate and graduate students from a public European university participated in the experiment. Invited persons who did not participate in the experiment almost always declined due to an inappropriate date of the experiment. Diferences in group sizes are due to random as signment of participants to the groups and the fact that not all participants successfully finished the search tasks. Each participant received 10 Euro for participation. The proportion of female participants is approximately equal across the experimental groups $( p > 0 . 6 )$ which indicates that the randomization worked as intended.

Participants who searched with the internal search engine for mulated slightly, but not significantly $( p _ { f u r n i t u r e } = 0 . 3 6 8 ,$ p = 0.123; tested with a one-sided t-tests for independent samples) more queries than participants who searched for the same product category with Google (generic search engine). Also, the number of distinct keywords used in the internal search engine is higher than the number of distinct keywords used in the generic search engine. These figures indicate that consumers use the internal search engine of an online store slightly diferent than a generic search engine. The number of products finally chosen by the participants does, however, not significantly difer between the two groups $( p _ { f u r n i t u r e } = 0 . 5 6 5 ,$ p = 0.811, tested with one-sided t-tests for independent samples).

In order to test whether the search queries entered in the internal search engine are similar to those entered in the generic search engine, we analyzed how many participants entered keywords in the internal search engine that were used as top keywords in Google (generic search engine). More specifically, we first extracted the top-n keywords entered in the generic search engine and then counted the number of participants who entered any of these top-n keywords in the internal search engine. As shown in Fig. 1, at least one of the top-5 keywords entered in Google for the furniture search was used 33 times as keyword by the 39 participants who used the internal search engine of an online store for the furniture search (black line in Fig. 1).

As a baseline, we compute the average frequency of n keywords entered in the online store's internal search engine (gray lines). Five diferent keywords were on average only ten times entered in the internal search engine (see Fig. 1). This allows us to compare the search frequency of an average keyword that prospective consumers enter in the internal search with the search frequency of top Google keywords. Top keywords extracted from the generic search engine Google are significantly $( p < 0 . 0 0 1$ , tested with a Mann-Whitney-U-test for independent samples) more frequently used for a search query in the internal search engine than an average keyword. We furthermore computed the similarity of the keywords entered in the internal search and the keywords entered in Google. Correlation values of 0.488 for furniture and 0.275 for multimedia show that not only the most popular keywords occur by random chance in both groups but that there is also a moderate similarity between all keywords use in the internal search engine and all keywords used in Google. The results of our laboratory experiment indicate that goal-directed consumers enter keywords in an online store's internal search that are often used in Google by goal directed consumers who already have a purchase in mind.

![](/api/attachments/YAWHN87X/fulltext/images/4e40747fa5e6c81e29687cc864941c9279148fd3fb5f1374df8b9e30c492905f.jpg)  
Fig. 1. Frequency of keywords entered in internal search engine.

## 3.2. Algorithm

AKEGIS is based on the empirical evidence that keywords used by visitors during their customer journey in an online store's internal search seem to be good predictors for valuable sponsored search key words. Furthermore, our approach uses an advertiser's internal search to define landing pages and to monitor and manage advertising keywords to build a comprehensive automatic system.

The keyword generation approach of AKEGIS is depicted in Algorithm 1. An initial set of keyword candidates K is filled with keywords from the internal search and also other sources, such as Thesauri. These keywords can be for example product names, product categories or even more generic keywords, which are related to the respective assortment. The keywords k ∈ K will be enriched with other keyword suggestions and the monthly Google search volume to prioritize key words and to remove keywords from K that are not searched or are only scarcely searched on Google. An internal search is than executed for each keyword k to examine the potential keyword's relevance for the advertiser's online store. Keyword k is booked into the advertiser's account if the number of internal search results l exceeds or equals a predefined threshold τ and if k is not included in the account so far. If l < τ the corresponding keyword k is paused if it is included in the adver tiser's SSA account.

Algorithm 1. Keyword Generation Algorithm example, every 24 h) by executing internal search requests and pausing those keywords leading to zero or fewer than τ results. Paused keywords should also be checked regularly and activated once the internal search delivers enough results.

We propose that parameter τ should be initially set to a rather high value and than lowered down until keywords are generated that are not profitable. The lower τ the more keywords will be booked in an advertiser's SSA account. However, keywords that lead to only a few internal search results are likely to be of interest only for a few con sumers.

In the next section, we empirically evaluate AKEGIS in cooperation with two online stores.

## 4. Empirical evaluation

We implemented the idea of automatically generating sponsored search keywords based on the search log of a store's internal search in cooperation with a large-scale online store and measured several SSA performance indicators before and after the implementation. We compare these performance indicators to those of a second and similar online store from the same company to capture any efects over time (like seasonality or trends). In the following, we describe the empirical setting, explain the data collection process, and then present the data analysis and results.

## 4.1. Setting

We analyzed the performance of SSA activities for two large-scale online stores managed by the same company. The company runs more than 100 online stores worldwide and has online sales of just under Euro 7 billion a year.

One online store implemented AKEGIS in the first half of our ob servation period (we call this online store A from now on). AKEGIS was implemented as described above with τ = 5, i.e., keyword candidates the lead to less than five results in store A’s internal search engine are either not booked or are paused. We use a second online store B from

```kotlin
procedure GENERATEKEYWORDS
    K ← getKeywordsFromInternalSearch()
    K ← K + getKeywordsFromOtherSources()
    for all k ∈ K do
    k ← enrich(k)
    l ← length(getResultsFromInternalSearch(k))
    p ← firstResultFromInternalSearch(k)
    if l >= τ then
    if accountContains(k) == False then
    book(k, p)
    else
    if accountContains(k) == True then
    pause(k)
```

The first page the advertiser's internal search returns for a particular keyword can be used as landing page for the corresponding keyword. This automatic process is highly eficient compared to static category landing pages, as these always need a manual setup. After implementing the new keywords with a starting bid and suitable advertising texts based on templates into the advertiser's SSA account, they are set as active and bid management software can be used to carry out necessary bid adjustments for the keywords in the following time.

To identify keywords that need to be paused due to product fluctuation, we propose checking all active keywords frequently (for the same company to control for diferences that are not attributed to AKEGIS (trend over time, company image, etc.). At the beginning of the test both shops and their Google Ads campaigns have been set up manually by the same division of the company and the same agency. Therefore, all match types were used within the campaigns and the accounts were structured the same way (product categories). With AKEGIS in shop A an alphabetical campaign structure has been in troduced and new keywords were booked as “exact match”. The campaigns of shop B were expanded according to the old structure and booking pattern.

![](/api/attachments/YAWHN87X/fulltext/images/bf00743463b16c306ac266adfc2de0d8d3095614f8c6ee5195a5d4a7b57c805b.jpg)

![](/api/attachments/YAWHN87X/fulltext/images/d9108d79e59df18f25b8478b2169e10ac2ffb57eeca3d74098dc4e5b8cfee70c.jpg)

![](/api/attachments/YAWHN87X/fulltext/images/63a4badf3146277fbad62712e328061b64d96f5cc0670a2ee79f75a8eea84eee.jpg)

![](/api/attachments/YAWHN87X/fulltext/images/f9350be074043904bbc8e68fc968d02c86ce63785247f3fa211f867ad7623af2.jpg)  
Fig. 2. Number of keywords, number of impressions per keyword, cost per click and conversion rate relative to $t = 0 .$

Moreover, both stores

ofer nearly the same products (mainly clothes for each gender, each age group and each size; approximately 90% overlap),

• were implemented with the same content management system,

use the same layout template,

use the same product categorization and product pictures, and

• run on the same server.

The company uses the same bid management software for both stores to place bids at Google AdWords for the keywords generated for store B or for store A. The parameters of the bid management software (e.g., for ad scheduling) were kept equal for the two online stores throughout the complete duration of the study. Bids were placed without any pre-defined budget but with a pre-defined return on investment rate. The bidding process should thus have no influence on the diferences between the two stores.

## 4.2. Measures

We use keywords as unit of analysis because a sponsored search auction is keyword specific. As AKEGIS automatically generates keywords, it is likely to extract more keywords than experts can do and according to our insights, we expect also improvements with respect to economic outcome measures. We measure the number of keywords used in sponsored search auctions per day relative to the number of keywords at t = 0. The company's bid management software places bids on Google AdWords for all active keywords. Depending on the bid, these keywords are then listed in the sponsored search results of Google users searching for one of the keywords. We counted the number of impressions per keyword (i.e., the number of times an ad of the online store is listed in the sponsored search results) for all keywords per day relative to the number of impressions per keyword at $t = 0 .$ We furthermore measure the costs per click and day relative to the costs at $t = 0 .$ Costs per click depend on the bid placed for a keyword and the bid (besides the quality factor of the target page) determines the position of an ad in the search result list which in turn influences the number of clicks significantly. The position finally directly influences the conversion rate [4] which we use as further measure in our investigation. Conversion rate and cost per click furthermore directly influence a store's profit from an SSA campaign. We again use conversion rates relative to the rates at t = 0.

## 4.3. Data

We collected data for 365 days. The company started introducing the AKEGIS approach in store A at t = 69. The introduction of AKEGIS lasted until t = 119. Thus, the pre-treatment phase was from t = 0 until t = 69 whereas the post-treatment phase started at $t = 1 2 0$ and ended at t = 364. For each online store and each day, we gathered the number of generated keywords, the number of impressions per keyword, the cost per click and the conversion rate relative to the values at t = 0<sup>2</sup>. The data in our dataset only were generated by active keywords. Fig. 2 illustrates the data with respect to diferent performance indicators.

Table 3 depicts the mean and standard deviation of our performance measures for store A before and after the introduction of AKEGIS. Note that all values are relative to the values at the first day of our data collection period. A comparison of the mean values with t-tests for independent samples indicates that AKEGIS improved the number of keywords, reduced the impressions per keyword, decreased the cost per click and increased the store's conversion rate significantly $( p < 0 . 0 1$ for all measures).

The results in Table 3 are valid only under the assumption of common trends in the pre- and post-treatment phase $( \mathrm { i . e . , }$ , before and after implementing AKEGIS). As seasonal trends and a changing product portfolio could theoretically have an influence on the performance in both phases, we compare the performance of store A with the performance of store B.

## 4.4. Pre-treatment trend

For a valid analysis, both stores need to show the same trend in terms of our defined measures before the intervention. We test for the common trend assumption by proofing the Granger causality of a measure for store B on the same measure for store A [21,39]. A test for Granger causality is only reliable if the variables are stationary. We use the Zivot-Andrews-Unit-Root test to check for stationary [68].

Table 3  
Performance before and after the implementation of AKEGIS.

<table><tr><td rowspan="2">Measure</td><td colspan="2">Pre-treatment</td><td colspan="2">Post-treatment</td><td rowspan="2">t value</td><td rowspan="2">p value</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td># keywords</td><td>1.618</td><td>0.378</td><td>5.255</td><td>0.739</td><td>55.511</td><td>&lt; 0.001</td></tr><tr><td>Impressions/Keyword</td><td>0.988</td><td>0.241</td><td>0.889</td><td>0.153</td><td>-3.221</td><td>0.002</td></tr><tr><td>Cost per click</td><td>2.514</td><td>0.413</td><td>1.025</td><td>0.153</td><td>-29.400</td><td>&lt; 0.001</td></tr><tr><td>Conversion rate</td><td>1.007</td><td>0.106</td><td>1.202</td><td>0.240</td><td>9.801</td><td>&lt; 0.001</td></tr></table>

Table 4  
Analysis of common pre-treatment trends.

<table><tr><td rowspan="2">Measure</td><td colspan="2">Stationary test</td><td colspan="2">Granger causality test</td></tr><tr><td>t value</td><td>p value</td><td>t value</td><td>p value</td></tr><tr><td># keywords</td><td>-4.526</td><td>0.001</td><td>5.246</td><td>0.003</td></tr><tr><td>Impressions/Keyword</td><td>-5.118</td><td>&lt; 0.001</td><td>4.150</td><td>0.010</td></tr><tr><td>Cost per click</td><td>-5.546</td><td>&lt; 0.001</td><td>5.098</td><td>0.003</td></tr><tr><td>Conversion rate</td><td>-7.320</td><td>&lt; 0.001</td><td>3.157</td><td>0.031</td></tr></table>

Table 4 shows that the time series of all four performance measures is stationary. Furthermore, Table 4 indicates that store B is a good predictor for the performance of store A in terms of the above defined measures. We hence can assume that both stores have a common trend with respect to their performance before the introduction of AKEGIS.

## 4.5. Analysis

We conduct diference-in-diference (DiD) estimations [8] with fixed store and time efects in order to investigate the efect of AKEGIS. This is the state-of-the-art approach to identify the efect of a treatment given to one of two groups [35,37,58]. We control for weekday efects and estimate the efect on the above defined performance measures PM with the following models.

$$
\begin{array}{r l} {P M _ {i, t}} & {= \beta_ {0} S t o r e A _ {i, t} \times A K E G I S _ {i, t} +} \\ & {\quad \sum_ {j = 1} ^ {6} \beta_ {j} W e e k d a y _ {i, t} + \gamma S t o r e _ {i} + \delta T i m e _ {t} + \epsilon_ {i, t}} \end{array}\tag{1}
$$

The efect of our proposed approach is captured by the coeficient $\beta _ { 0 } .$ Because all performance measures are given relative to the first day of our data collection period, $\beta _ { 0 }$ expresses the relative change of a performance measure after the introduction of AKEGIS.

## 4.6. Results

The results in Table 5 demonstrate that the average number of keywords for store A is on average three times higher after the in troduction of AKEGIS than the number of keywords that has been generated before introducing AKEGIS. This clearly shows that AKEGIS can create a very high number of keywords and substantially outperforms the capabilities of human.

Table 5  
Efect on the number of keywords.

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p value</td></tr><tr><td>Store A × AKEGIS</td><td>3.052</td><td>0.093</td><td>32.849</td><td>&lt; 0.001</td></tr><tr><td>Tuesday</td><td>-0.045</td><td>0.072</td><td>-0.623</td><td>0.533</td></tr><tr><td>Wednesday</td><td>-0.174</td><td>0.072</td><td>-2.413</td><td>0.016</td></tr><tr><td>Thursday</td><td>-0.273</td><td>0.072</td><td>-3.796</td><td>&lt; 0.001</td></tr><tr><td>Friday</td><td>-0.423</td><td>0.072</td><td>-5.883</td><td>&lt; 0.001</td></tr><tr><td>Saturday</td><td>-0.441</td><td>0.072</td><td>-6.143</td><td>&lt; 0.001</td></tr><tr><td>Sunday</td><td>0.002</td><td>0.072</td><td>0.025</td><td>0.980</td></tr><tr><td>DF</td><td></td><td></td><td>618</td><td></td></tr><tr><td>Adj.  $R^2$ </td><td></td><td></td><td>0.925</td><td></td></tr></table>

We can safely ascertain that AKEGIS leads to a higher number of advertising keywords compared to a manual approach. More specifically, fewer than 40,000 keywords were generated for A on average before implementing AKEGIS, and more than 126,000 after implementing AKEGIS.

Not only has the number of keywords significantly changed with the implementation of AKEGIS, but the keywords are also diferent. It is, however, questionable whether investing in such a large number of advertising keywords is profitable.

The company's bid management software places bids on Google AdWords for all keywords that are active in the company's Google AdWords account. Depending on the bid, these keywords are then listed in the sponsored search results of Google users searching for one of the keywords. Impressions are approximately three times higher after the introduction of AKEGIS. This is not surprising given that AKEGIS created approximately three times more keywords for online store A than before. In line with that, Table 6 indicates that the number of im pressions per keyword did not change significantly under AKEGIS.

A rather constant number of impressions per keyword over time indicates that the average position of the ads was also rather equal before and after the intervention. This is consistent with the fact that the bid management parameters have been kept constant for both stores.

However, Table 7 shows that AKEGIS significantly lowered the cost per click on average. Because both stores use the same bid management software, a lower cost per click indicates that AKEGIS generates cheaper keywords. Cheaper keywords are those that are rather specific and hence not very popular [46].

On top of that striking result, Fig. 2 shows that the conversion rate of store A is, on average, higher than the conversion rate of store B after the intervention. This is manifested by the results presented in Table 8. AKEGIS improves the conversion rate by 41.1% (p < 0.001).

AKEGIS hence generated advertising keywords that attracted more valuable consumers. This is in line with the outlined consumer search behavior. Consumers using an online store's internal search typically are rather goal-directed and have a higher conversion probability than store visitors who do not use the internal search.

Table 6  
Efect on the number of impressions per keyword.

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p value</td></tr><tr><td>Store A × AKEGIS</td><td>-0.021</td><td>0.028</td><td>-0.764</td><td>0.445</td></tr><tr><td>Tuesday</td><td>-0.020</td><td>0.022</td><td>-0.911</td><td>0.363</td></tr><tr><td>Wednesday</td><td>-0.054</td><td>0.022</td><td>-2.486</td><td>0.013</td></tr><tr><td>Thursday</td><td>-0.070</td><td>0.022</td><td>-3.242</td><td>0.001</td></tr><tr><td>Friday</td><td>-0.085</td><td>0.022</td><td>-3.948</td><td>&lt; 0.001</td></tr><tr><td>Saturday</td><td>-0.069</td><td>0.022</td><td>-3.208</td><td>0.001</td></tr><tr><td>Sunday</td><td>0.065</td><td>0.022</td><td>3.003</td><td>0.003</td></tr><tr><td>DF</td><td></td><td></td><td>618</td><td></td></tr><tr><td>Adj.  $R^2$ </td><td></td><td></td><td>0.166</td><td></td></tr></table>

Table 7  
Efect on cost per click.

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p value</td></tr><tr><td>Store A × AKEGIS</td><td>-0.736</td><td>0.047</td><td>-15.555</td><td>&lt; 0.001</td></tr><tr><td>Tuesday</td><td>0.043</td><td>0.037</td><td>1.179</td><td>0.239</td></tr><tr><td>Wednesday</td><td>0.114</td><td>0.037</td><td>3.086</td><td>0.002</td></tr><tr><td>Thursday</td><td>0.174</td><td>0.037</td><td>4.750</td><td>&lt; 0.001</td></tr><tr><td>Friday</td><td>0.248</td><td>0.037</td><td>6.769</td><td>&lt; 0.001</td></tr><tr><td>Saturday</td><td>0.244</td><td>0.037</td><td>6.664</td><td>&lt; 0.001</td></tr><tr><td>Sunday</td><td>-0.021</td><td>0.037</td><td>-0.578</td><td>0.563</td></tr><tr><td>DF</td><td></td><td></td><td>618</td><td></td></tr><tr><td>Adj.  $R^2$ </td><td></td><td></td><td>0.892</td><td></td></tr></table>

Table 8 Efect on conversion rate.

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p value</td></tr><tr><td>Store A × AKEGIS</td><td>0.411</td><td>0.032</td><td>13.017</td><td>&lt; 0.001</td></tr><tr><td>Tuesday</td><td>-0.003</td><td>0.024</td><td>-0.102</td><td>0.918</td></tr><tr><td>Wednesday</td><td>-0.022</td><td>0.025</td><td>-0.891</td><td>0.373</td></tr><tr><td>Thursday</td><td>-0.018</td><td>0.024</td><td>-0.739</td><td>0.460</td></tr><tr><td>Friday</td><td>-0.028</td><td>0.024</td><td>-1.135</td><td>0.257</td></tr><tr><td>Saturday</td><td>0.045</td><td>0.024</td><td>1.824</td><td>0.069</td></tr><tr><td>Sunday</td><td>0.095</td><td>0.024</td><td>3.883</td><td>&lt; 0.001</td></tr><tr><td>DF</td><td></td><td></td><td>618</td><td></td></tr><tr><td>Adj.  $R^{2}$ </td><td></td><td></td><td>0.535</td><td></td></tr></table>

The weekday efects show that SSA is most efective on weekend. Especially the conversion rate is highest on Saturday on Sunday $( p < 0 . 1 )$

In summary, the empirical investigation showed that the keywords generated with our AKEGIS approach are on average cheaper and attract more store visitors to become purchasers. Because the process of keyword generation can be completely automated with the use of an online store's internal search, the number of generated keywords could be significantly increased. Automatically generating sponsored search keywords is furthermore possible at less costs than manually generating keywords. AKEGIS thus facilitates the dis-intermediation of SSA experts.

In the next section, we examine the robustness of our findings.

## 5. Robustness checks

Diference-in-diference estimations compare two regions or periods of one group that are separated by a treatment intervention. A control group is contrasted with the treatment group to estimate the trend in the treatment group for the case in which the treatment has not been set. Diferences between the two regions or periods of the treatment group might also be the result of some pre-treatment trends. We conduct robustness checks to test for possible pre-treatment trends by es timating several models with placebo interventions. We follow the suggestion in [1] and [23] and systematically contrast multiple pretreatment interventions with the efect of the real treatment T. More specifically, we set “placebo” treatments at the following dates relative to the real treatment T: $T - 3 0 , T - 1 5 , T + 1 5 , T + 1 5 .$ . We then use the diference-in-diference estimation with fixed store and time efects to compute the efect of the interaction efect of store A and the introduction of AKEGIS on all of our performance measures. For example, if we set the placebo intervention to $T - 1 5 ,$ , we assume that AKEGIS would have been launched 15 days before its actual launch. The pretreatment phase is therefore 15 days shorter whereas the post-treatment phase is 15 days longer for the placebo intervention $T - 1 5$

The placebo intervention efects should be significantly lower than the efect of the true treatment on all dependent variables. Fig. 3 shows the coeficients of all placebo interventions as well as the real treatment on all dependent variables. Lower absolute coeficients for the number of keywords, the cost per click and the conversion rate indicate that the most significant change in respect to these performance measures indeed was triggered by the introduction of AKEGIS. We thus can assume that AKEGIS is responsible for the improvement of our performance measures.

Only the coeficients for the number of impressions per keyword indicate that there is no treatment efect. This is not surprising because our DiD analysis already revealed that the number of impressions per keyword is not significantly afected by the intervention.

## 6. Discussion

In this section, we discuss the implications of our study for researchers and online store managers. Furthermore, we discuss limitations of our study and provide avenues for further research.

## 6.1. Research implications

Our study contributes to recent research on SSA in various ways. First, we show that keywords used in an online store's internal search engine are promising candidates for SSA and that there are two reasons for it. First, internal search engines are mainly used by goal-directed consumers who are more likely to convert to purchasers and our analyses reveal that this efect is really large. 7.46% of consumers who consulted the internal search converted to purchasers whereas only 1.52% of consumers who did not use the internal search finally purchased anything in the store. The conversion rate is usually between 2.5 and 3% in the investigated store, so that the diference of approximately 6 percentage points is striking. This indicates that users of generic search engines who formulate queries with these keywords are very likely to be goal-oriented consumers.

![](/api/attachments/YAWHN87X/fulltext/images/b499c0fc7eff04fc01fceead1032d9a9fe64725a8c1f183627393a36eee4a674.jpg)

![](/api/attachments/YAWHN87X/fulltext/images/48cf914c001bdf3d5e94e0564c90f4d8af4cf1c6bd95ec028b7bdc6e7eb0bd84.jpg)

![](/api/attachments/YAWHN87X/fulltext/images/30ed5575c385e0671fbc23bbd76913e7585ff64f8ea62ee20c72705006cb9cd5.jpg)

![](/api/attachments/YAWHN87X/fulltext/images/7b04e6e8d07876993212c592d621462a6d555cd710d8c987402de73909cddb46.jpg)  
Fig. 3. Efect of placebo interventions and the real treatment.

Second, there is a large overlap between the keywords that goal oriented consumers – who are attractive targets for SSA – use at generic search engines and internal search engines. Our analyses suggest that keywords entered in a generic search engine might be more salient to consumers when entering an online store right after consulting a generic search engine. Research in psychology has shown that information that is most salient is likely to be overweighed by human decision makers [32,59] and such ‘focalism’ can influence a person's actions [18,48]. In our case this means that the behavior of at least goaloriented consumers is rather similar at generic and internal search engines due to this focalism. This makes data from internal search engines valuable for SSA. We use these insights to design a superior decision support system that can suggest high numbers of promising keywords using the data from the internal search engine.

We furthermore provide a rigorous evaluation procedure for evaluating the performance of decision support systems for SSA. We applied the evaluation procedure to compare the performance of our decision support system for SSA keywords to that of a state-of-the-art approach. The same evaluation procedure can also be used to investigate the efect of decision support systems for bidding strategies or budget optimization.

Moreover, we provide first evidence that the eficiency of SSA depends on the weekday. Cost per click are lowest on Sundays and highest on Fridays. Interestingly, the conversion rate is highest on Sundays and lowest on Fridays rendering Sundays especially important for sponsored search advertisers. Previous research revealed similar weekday efect by showing that limited attention among investors afects stock returns [14]. Due to inattention on certain weekdays or time of the day, com pared to other periods, the authors found evidence of a less immediate and more delayed response to new information. Similar efects have also been found in online auctions where [24] found, long-lasting unanticipated gaps between demand and supply over the course of the week and time of the day. The decrease of the SSA eficiency on Fridays might hence be a result of a similar mismatch that firms do not account for in their bidding behavior.

## 6.2. Managerial implications

Online store managers can use AKEGIS as decision support tool for SSA campaigns. AKEGIS is a simple and easy-to-implement approach. AKEGIS uses the first result page returned by an online store's search engine as landing page, it furthermore comes with the advantage that, in contrast to existing approaches for keyword set expansion, that landing pages do not have to be manually managed for sponsored search keywords. Existing software solutions for SSA management, such as Camato<sup>3</sup> or AdEngine<sup>4</sup>, support advertisers in managing landing pages, but they lack functionalities for completely automatically generating and evaluating keyword candidates. AKEGIS hence might complement existing software solutions. AKEGIS now (as of June 2018) creates a keyword set for store A that is ten times larger than the one used at the beginning of our study. More advertising generates more trafic, which increases the number of internal searches that can then be used to generate more keywords for SSA. Thus. AKEGIS starts a positive feedback loop. The success in store A was impressive, and the management decided to gradually integrate this technology into the other stores of the focal company. In addition to this it also has been transformed to a commercial product which manages ad-spend in a two-digit million range.

## 6.3. Limitations and future directions

Our study is subject to some limitations that provide avenues for future research. We could not test the performance of each single keyword in order to obtain further insights into how to identify a successful keyword. The high variance, especially in the conversion rate, indicates that AKEGIS generates many keywords that are not profitable. Analyzing these keywords and the clickstreams of consumers who have entered these keywords in a store's internal search might help to separate profitable from non-profitable keywords before booking these keywords in a sponsored search account. This should, however, not constitute a major problem because bidding systems take care of this problem and sort out non-profitable keywords after an exploration phase.

We compared AKEGIS to only one possible other approach of keyword generation. The success of manual keyword generation heavily depends on the skills and the used tools of the human decision makers and therefore the results have to be seen in this light. This benchmark approach is the state-of-the-art approach successfully used for more than 100 online stores of the company with whom we cooperated in our empirical investigation. These human decision makers are experts in the area of sponsored search and can fall back on several years of experience. Nevertheless, a precise empirical test regarding the number of newly booked keywords or the keywords generated by an expert or by another tool and their resulting performance values could be helpful in order to make a more precise structured impact assessment of AKEGIS compared to the individual keyword generation approaches. The overall improvement driven by AKEGIS is however so substantial that we expect that the main findings should also hold if we would have used other benchmarks that heavily rely on human expert input or if we would have used other companies that employ such experts as benchmark. However, it would be interesting to see how AKEGIS also performs against other automatic approaches (which are however very limited at this point of time, see Section 2.2).

Another shortcoming of AKEGIS parallels the problems that many recommender systems have that rely on consumer activity data. Insuficient amounts of data can lead to so called “cold start problems”. Such systems cannot provide recommendations unless multiple-item purchasing profiles for a number of consumers, or at least for the consumer currently using the system, are available [49]. AKEGIS needs enough data from internal search to be able to generate enough meaningful keywords. This is easier for heavily visited websites than for smaller companies with fewer visits and thus a lower number of search queries. It would thus be interesting to determine a minimum threshold of search data that are required for AKEGIS to unfold its superiority.

We assume that online stores should focus on consumers who already have a purchase in mind. Some consumers might, however, visit an online store to build knowledge about products for later purchases. These consumers rather do not consult an online store's search engine, visit only a few product sites but do consider the few product sites very intensively [40]. Sponsored search keywords that can attract such consumers might be extracted from product sites on which consumers spend very long time. As AKEGIS is not limited to internal search engines as source for sponsored search keyword candidates it can be easily extended to also extract keywords from product sites.

However, we need to acknowledge that AKEGIS is designed to increase short-term profitability. The empirical study provided suficient substantial evidence that the systems achieves convincing improvements over the state-of-the-art approach that this firm used to apply. However, the sponsored keywords might be too focused on conversions and these keywords are likely to ignore customers who are exploring and have not yet decided exactly what to buy. These latter customers may be important in the long term in order to build the company's brand and generate a steady flow of new customers at diferent stages of the conversion funnel. We therefore suggest conducting a second study that examines whether AKEGIS can also increase revenue and profit ability over a longer time horizon.

## 7. Conclusion

Existing research has characterized consumers who use an online store's internal search as rather goal-directed [40]. Goal-directed consumers show a higher conversion probability than exploratory con sumers. Keywords entered in an online store's internal search hence mainly are from consumers with a rather high conversion probability. This manuscript introduced a novel approach (AKEGIS) that allows for automatically generating keywords for sponsored search advertising based on the keywords of an online store's internal search. In contrast to existing approaches [5,31,54,55], AKEGIS does not need a set of manually formulated keywords as input. In a large-scale field study, we demonstrated that AKEGIS helps generate advertising keywords that reduce the cost per click and simultaneously improve an online store's conversion rate.

While previous research has mainly focused on bidding management, keyword set expansion and the efect of diferent types of key words on the performance of SSA campaigns, our results clearly in dicate that automatically creating and managing keyword sets can leverage largely untapped potential. Researchers and practitioners have not examined this area thoroughly and our manuscript aims to shed light on this potential.

## References

[1] A. Abadie, A. Diamond, J. Hainmueller, Synthetic control methods for comparative case studies: estimating the effect of California's Tobacco Control Program, Journa of the American Statistical Association 105 (490) (2010) 493–505

[2] V. Abhishek, K. Hosanagar, Keyword generation for search engine advertising using semantic similarity between terms. Proceedings of the 9th ACM International Conference on Electronic Commerce. 2007, pp. 89–94.

[3] V. Abhishek, K. Hosanagar, Optimal bidding in multi-item multislot sponsored search auctions, Operations Research 61 (4) (2013) 855–873.

[4] A. Agarwal, K. Hosanagar, M.D. Smith, Location, location, location: an analysis o profitability of position in online advertising markets, Journal of Marketing Research 48 (6) (2011) 1057–1073.

[5] W. Amaldoss, K. Jerath, A. Sayedi, Keyword management costs and “Broad Match” in sponsored search advertising, Marketing Science 35 (2) (2016) 259–274.

[6] E. Anderl, I. Becker, F. Von Wangenheim, J.H. Schumann, Mapping the customer journey: lessons learned from graph-based online attribution modeling. International Journal of Research in Marketing 33 (3) (2016) 457–474.

[7] A. Avanso, B. Mokava, Efficiency evaluation in search advertising, Decisior Sciences 44 (5) (2013) 877–913.

[8] M. Bertrand, E. Duflo, S. Mullainathan, How much should we trust diference-indiference estimates? Quarterly Journal of Economics 119 (1) (2004) 249–275.

[9] Beruf-ApS, A free tool for combining AdWords keywords, 2019, http://kombinator. org/.

[10] A.Z. Broder, P. Ciccolo, M. Fontoura, E. Gabrilovich, V. Josifovski, L. Riedel, Search advertising using web relevance feedback, Proceedings of the 17th ACM Conference on Information and Kowledge Management, 2008, pp. 1013–1022.

[11] A.Z. Broder, P. Ciccolo, E. Gabrilovich, V. Josifovski, D. Metzler, L. Riedel, J. Yuan, Online expansion of rare queries for sponsored search. Proceedings of the 18th ACM International Conference on World Wide Web, 2009, pp. 511–520.

[12] B.J. Bronnenberg, J.B. Kim, C.F. Mela, Zooming in on choice: how do consumers search for cameras online? Marketing Science 35 (5) (2016) 693–712

[13] T.Y. Chan, Y.-H. Park, Consumer search activities and the value of ad positions in sponsored search advertising, Marketing Science 34 (4) (2015) 606–623.

[14] S. DellaVigna, J.M. Pollet, Investor inattention and friday earnings announcements, Journal of Finance 64 (2) (2009) 709–749.

[15] B. Edelman, M. Ostroysky, Strategic bidder behavior in sponsored search auctions Decision support systems 43 (1) (2007) 192–198.

[16] A. Fuxman, P. Tsaparas, K. Achan, R. Agrawal, Using the wisdom of the crowds for keyword generation, Proceedings of the 17th ACM International Conference on World Wide Web. 2008, pp. 61–70.

[17] A. Ghose, S. Yang, An empirical analysis of search engine advertising: sponsored search in electronic markets, Management Science 55 (10) (2009) 1605–1622.

[18] D.T. Gilbert. T.D. Wilson, Prospection: experiencing the future, Science 317 (5843 (2007) 1351–1354

[19] Google, Keyword Research and Strategy with Keyword Planner - Google Ads, 2019 https://ads.google.com/intl/en\_en/home/tools/keyword-planner/.

[20] R. Gopal, X. Li. R. Sankaranaravanan, Online keyword based advertising: impact of ad impressions on own-channel and cross-channel click-through rates. Decision Support Systems 52 (1) (2011) 1–8

[21] C.W.J. Granger, Investigating causal relations by econometric models and cross-

[22] H. Haans, N. Raassens, R. van Hout, Search engine advertisements: the impact of advertising statements on click-through and conversion rates, Marketing Letters 24 (2) (2013) 151–163.

[23] I. Heimbach, O. Hinz, The impact of sharing mechanism design on content sharing in online social networks, Information Systems Research 29 (3) (2018) 592–611.

[24] O. Hinz, S. Hill, J.-Y. Kim, TV's dirty little secret: the negative efect of popular TV on online auction sales. MIS Quarterly 40 (3) (2016) 623–644.

[25] P. Huang, N.H. Lurie, S. Mitra, Searching for experience on the web: an empirica examination of consumer behavior for search and experience goods, Journal of marketing 73 (2) (2009) 55–69.

[26] IAB, IAB Internet Advertising Revenue Report 2018, https://www.iab.com/wpcontent/uploads/2018/05/IAB-2017-Full-Year-Internet-Advertising-Revenue-Report.REV\_.pdf.

[27] I. Im, J. Jun, W. Oh, S.-O. Jeong, Deal-seeking versus brand-seeking: search behaviors and purchase propensities in sponsored search platforms, MIS Quarterly 40 (1) (2016) 187–203.

[28] C. Janiszewski, The influence of display characteristics on visual exploratory search behavior, Journal of Consumer Research 25 (3) (1998) 290–301.

[29] K. Jerath, L. Ma, Y.-H. Park, Consumer click behavior at a search engine: the role of keyword popularity, Journal of Marketing Research 51 (4) (2014) 480–486.

[30] R. Jones, B. Rey, O. Madani, W. Greiner, Generating query substitutions, Proceedings of the 15th ACM International Conference on World Wide Web. 2006 pp. 387–396.

[31] A. Joshi, R. Motwani, Keyword generation for search engine advertising, Proceedings of the 6th IEEE International Conference on Data Mining, 2006, pp. 490–496.

[32] D. Kahneman, D.T. Miller, Norm theory: comparing reality to its alternatives. Psychological review 93 (2) (1986) 136

[33] C. Karande, A. Mehta, R. Srikant, Optimizing budget constrained spend in search advertising. Proceedings of the 6th ACM International Conference on Web Search and Data Mining, 2013, pp. 697–706.

[34] KeyTools, Keyword Tool - Google Keyword Planner Alternative For SEO (FREE), 2019, https://keywordtool.io/.

[35] A. Kumar, R. Telang, Does the web reduce customer service cost? Empirical evi dence from a call center, Information Systems Research 23 (3) (2012) 721–737

[36] D. Liu, J. Chen, Designing online auctions with past performance information, Decision Support Systems 42 (3) (2006) 1307–1320

[37] Q. Lu, Q. Ye, How hotel star rating moderates online word-of-mouth efect: a difference-in-diference approach, Proceedings of the IEEE International Conference on Management Science & Engineering, 2013, pp. 3–8.

[38] X. Lu, X. Zhao, Diferential efects of keyword selection in search engine advertising on direct and indirect sales, Journal of Management Information Systems 30 (4) (2014) 299–325.

[39] G. Mallapragada, R. Srinivasan, Innovativeness as an unintended outcome of franchising: insights from restaurant chains. Decision Sciences 48 (6) (2017 1164–1197.

[40] W.W. Moe, Buying, searching, or browsing: diferentiating between online shoppers using in-store navigational clickstream, Journal of Consumer Psychology 13 (1 & 2) (2003) 29–39.

[41] L. Mostafa, BidTerm Suggestion for Webpages, Proceedings of the IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining, 2012, pp. 1090–1094.

[42]. S. Muthukrishnan. M. Pál. Z. Svitkina. Stochastic models for budget optimization in search-based advertising, Algorithmica 58 (4) (2010) 1022–1044

[43] T.P. Novak, D.L. Hoffman. A. Duhachek, The influence of goal-directed and experiential activities on online flow experiences. Journal of Consumer Psychology 13 (1&2) (2003) 29–39.

[44] N. Patel, Ubersuggest's Free Keyword Tool, Generate More Suggestions, 2019, https://neilpatel.com/ubersuggest/

[45] A. Ronchi, Combine words for SEO, PPC and linkbuilding, 2019, http:// mergewords.com/

[46] O.J. Rutz, R.E. Bucklin, From generic to branded: a model of spillover in paid search advertising, Journal of Marketing Research 48 (1) (2011) 87–102.

[47] O.J. Rutz, R.E. Bucklin, G.P. Sonnier, A latent instrumental variables approach to modeling keyword conversion in paid search advertising, Journal of Marketing Research 49 (3) (2012) 306–319.

[48] D.A. Schkade, D. Kahneman, Does living in California make people happy? A focusing illusion in judgments of life satisfaction, Psychological Science 9 (5) (1998 340-346.

[49] M. Scholz, V. Dorner, M. Franz, O. Hinz, Measuring consumers' willingness to pay with utility-based recommendation systems, Decision Support Systems 72 (2015) 60–71.

[50] SearchEngineLand, PPC Magic: 3 Steps To Turning Hundreds Of Keywords Into Millions - Search Engine Land 2010, https://searchengineland.com/ppc-magic-3 steps-to-turning-hundreds-of-keywords-into-millions-41198.

[51] SEMRush, SEMrush - service for competitors research, shows organic and Ads keywords for any site or domain 2019, https://www.semrush.com/.

[52] S.N. Singh, N.P. Dalal, Web home pages as advertisements, Communications of the ACM 42 (8) (1999) 91–98

[53] B. Skiera, N.A. Nabout, PROSAD: a bidding decision support system for profit op timizing search engine advertising, Marketing Science 32 (2) (2013) 213–220.

[54] S. Thomaidou, K. Leymonis, M. Vazirgiannis, Digital Enterprise Design and Manag., Advances in Intelligent Systems and Computing, vol. 205, chap. GrammAds: Keyword and Ad Creative Generator for Online Advertising Campaigns, Springer, 2013 pp. 33–44.

[55] S. Thomaidou, M. Vazirgiannis, Multiword keyword recommendation system for Advances in Social Networks Analysis and Mining, 2011, pp. 423–427.

[56] D. Wang, Z. Li, G. Xie, M.-A. Kaafar, K. Salamatian, Adwords Management for

Third-parties in SEM: an Optimisation Model and the Potential of Twitter, 35th Annual EEE International Conference on Computer Communications, 2016.

[57] Y. Wei, Q. Wei, J. Zhang, From Query Log to Competitive Advertising: A Business Intelligence Method for Elaborating Consideration Set of Keywords, Proceedings of the IEEE International Conference on Management Science & Engineering, 2013, pp. 179–185.

[58] W. Wen, C. Forman, S.J.H. Graham, The impact of intellectual property rights en forcement on open source software project success, Information Systems Research 24 (4) (2013) 1131–1146.

[59] T.D. Wilson, T. Wheatley, J.M. Meyers, D.T. Gilbert, D. Axsom, Focalism: a source of durability bias in afective forecasting. Journal of personality and social psychology 78 (5) (2000) 821.

[60] WordStream, Free Keyword Tool WordStream 2019, https://www.wordstream. com/keywords.

[61] H. Wu, G. Qiu, X. He, Y. Shi, M. Qu, J. Shen, J. Bu, C. Chen, Advertising Keyword Generation Using Active Learning, Proceedings of the 18th ACM International Conference on World Wide Web, 2009, pp. 1095–1096.

[62] S. Yang, S. Lu, X. Lu, Modeling competition and its impact on paid-search advertising, Marketing Science 33 (1) (2014) 134–153.

[63] Y. Yang, J. Zhang, R. Qin, J. Li, F.-Y. Wang, W. Qi, A budget optimization framework for search advertisements across markets, IEEE Transactions on Systems, Man, and Cybernetics. Part A: Systems and Humans 42 (5) (2012) 1141–1151

[64] S. Yao, C.F. Mela, A dynamic model of sponsored search advertising, Marketing Science 30 (3) (2011) 447–468

[65] Y. Yuan, F.-Y. Wang, D. Zeng, Competitive analysis of bidding behavior on sponsored search advertising markets, IEEE Transactions on Computational Social Systems 4 (3) (2017) 179–190.

[66] Y. Yuan, D. Zeng, H. Zhao, L. Li, Analyzing positioning strategies in sponsored search auctions under CTR-based quality scoring, IEEE Transactions on Systems, Man, and Cybernetics. Part A: Systems and Humans 45 (4) (2015) 688–701.

[67] D. Zambonini, AdWord and SEO Keyword Permutation Builder, 2019, http://seo danzambonini.com/

[68] E. Zivot, D.W.K. Andrews, Further evidence on the great crash, the oil-price shock,

and the unit-root hypothesis, Journal of Business & Economic Statistics 10 (3) (1992) 251–270.

Michael Scholz (1981) studied information systems at the Martin-Luther-University Halle/Wittenberg and received his Ph.D. in December 2009 from the University of Passau He is now an assistant professor for information systems at the University of Passau. His research has been published in journals, such as European Journal of Operational Research (EJOR), Decision Support Systems (DSS), Journal of Statistical Software (JSS), Business & Information Systems Engineering (BISE) and in a number of proceedings (e.g., ICIS, ECIS).

Christoph Brenner (1981) studied business informatics at the University of Hamburg. After graduating, he worked for a start-up company and shortly afterwards founded an online marketing company. Christoph is a doctoral student at the Goethe University in Frankfurt.

Oliver Hinz (1974) studied at the TU Darmstadt Business Administration and Information Systems with main focus on Marketing, Software Engineering and Computer Graphics. After receiving his diploma (equiv, master degree) he worked several vears for the Dresdner Bank as a consultant for business logic. Oliver worked as a Research Assistant at the Chair of Electronic Commerce (2004–2007) and received his Ph.D. in October 2007 from Goethe University Frankfurt. He supported the E-Finance Lab as Assistant Professor for E-Finance & Electronic Markets from 2008 to 2011 and then joined the TU Darmstadt and headed the Chair of Information Systems | Electronic Markets until September 2017. Oliver is now Full Professor of Information Systems and Information Management at Goethe University Frankfurt. His research has been published in journals like Information Systems Research (ISR). Management Information Systems Ouarterly (MISQ), Journal of Marketing (JM), Journal of Management Information Systems (JMIS), Decision Support Systems (DSS), Business & Information Systems Engineering (BISE) and in a number of proceedings (e.g. ICIS, ECIS, PACIS). According to the German business journal “Handelsblatt” he belongs currently to the top researchers in the management disciplines in Germany.
