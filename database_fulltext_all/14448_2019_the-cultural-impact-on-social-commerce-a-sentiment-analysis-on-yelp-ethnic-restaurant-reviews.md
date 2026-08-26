---
otero_id: 14448
otero_key: "VPCFCKG2"
title: "The cultural impact on social commerce: A sentiment analysis on Yelp ethnic restaurant reviews"
authors: "Makoto Nakayama; Yun Wan"
year: "2019"
journal: "Information & Management"
doi: "10.1016/j.im.2018.09.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: The cultural impact on social commerce: a sentiment analysis on Yelp ethnic restaurant reviews

Authors: Makoto Nakayama, Yun Wan

![](/api/attachments/VPCFCKG2/fulltext/images/3c7f87d552597b57383b14c0b39e64d2522971cbaf8316234e5c726c2baa624d.jpg)

PII: S0378-7206(17)30622-5

DOI: https://doi.org/10.1016/j.im.2018.09.004

Reference: INFMAN 3104

To appear in: INFMAN

Received date: 15-7-2017

Revised date: 22-8-2018

Accepted date: 4-9-2018

Please cite this article as: Nakayama M, Wan Y, The cultural impact on social commerce: a sentiment analysis on Yelp ethnic restaurant reviews, Information and amp; Management (2018), https://doi.org/10.1016/j.im.2018.09.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# The cultural impact on social commerce: a sentiment analysis on Yelp ethnic restaurant reviews

Makoto Nakayama

College of Computing and Digital Media

DePaul University

mnakayama@cdm.depaul.edu

Phone: 312-362-5088

Fax: 312-362-6116

Yun Wan

Department of Computer Science

University of Houston, Victoria

WanY@uhv.edu

Phone: 281-275-8807

Fax: 361-580-5507

## ABSTRACT

In social commerce, ethnic culture plays an important role in the content and quality perception of customer reviews. This study examined Japanese restaurant reviews in English at Yelp.com and those in Japanese at Yelp.co.jp from a cross-cultural perspective. Using bilingual text mining software, we demonstrate that Japanese customers have significantly different sentiment distribution patterns on four basic attributes of dining experience (food quality, service, ambiance, and price fairness) than Western customers. These findings shed insights on how review contents and ratings may vary between local and foreign customers at multi-national social commerce platforms. Our findings fill a research gap of cultural influence in social commerce.

Keywords: Online restaurant review; cross-cultural difference; aspect importance; restaurant valuation; helpfulness votes

## Abstract

In social commerce, ethnic culture plays an important role in the content and quality perception of customer reviews. This study examines Japanese restaurant reviews in English language at yelp.com and those in Japanese language at yelp.co.jp from a cross-cultural perspective. Using bilingual text mining software, we demonstrate that Japanese customers have significantly different sentiment distribution

#

patterns on four basic attributes of dining experience (food quality, service, ambiance, and price fairness) compared with Western customers. These findings provide insights on how review content and ratings may vary between local and foreign customers at multinational social commerce platforms. Our findings fill a research gap of cultural influence in social commerce.

## 1 Introduction

We frequently observe challenges in cross-cultural service replication, provision, and consumption. In 1983, on a business trip to Italy, Howard Schultz found that Italian coffee bars were not just supplying coffee but “camaraderie” or a social corner for neighbors. This inspired him, and he vowed to replicate such an experience in the United States. He eventually transformed Starbucks from a small coffee bean reseller into a worldwide social, cultural, and business icon [1]. Thirty years later, however, most Italians still do not consider Starbucks remotely comparable to their native counterpart.<sup>1</sup> Schultz realizes he still has a long way to go to completely replicate that authentic Italian experience. In another instance, Americanized Asian restaurants are not considered authentic by native Asian customers, such as the case of Chop Suey [2]. Recipes modified to local taste preferences are an example of confluences of food, service, and restaurant ambiance between the origin and adapter.

The present-day consumerism and sharing economy may mitigate the above challenges. For example, the popularity of social commerce allows consumers with different cultural backgrounds to share their preferences and experiences on the same platform or through the same medium on the Internet. Reviews posted on online shopping portals (e.g., Amazon) or traveling portals (e.g., TripAdvisor and Yelp) provide businesses with useful insights. As a result, a consumer in Europe or Asia could purchase an item from Amazon based on the recommendation of previous buyers in North America. A Western traveler could use rating guidance from Yelp to find a fine local restaurant in Japan. Millennials from China could travel with the confidence that Airbnb would help them find a bed in which to sleep, no matter where they went.

In this paper, we demonstrate that there is still a shortfall in this social commerce cornucopia [3,4]. The culture has an impact on social commerce even when we can smooth out information asymmetry by sharing or exchanging our experience online. Specifically, through bilingual text analysis of 76,704 Western and 56,159 Japanese Yelp reviews on 10 popular Japanese food entrée items, we found that customers with different cultural backgrounds (Western vs. Japanese) have different sentiments and standards of rating regarding the food, service, ambiance, and price fairness of Japanese restaurant services. Such differences in sentiment indicate that a popular Japanese restaurant favored by Japanese customers may not necessarily receive the same preference by visiting Western customers. Even for a Japanese restaurant favored by both Western and Japanese customers, their specific preferences are likely different.

Such cultural impact can be easily validated in other service sectors as well as online shopping. Thus, all stakeholders in social media-facilitated social commerce, including customers, product/service providers, and platform/info brokerage operators, have to assess correctly the cultural influence when using social commerce platforms or engaging in social commerce initiatives.

#

For the remainder of the paper, we present the theoretical background and hypotheses of this study and then describe our research method and findings. We conclude with a discussion on the implications of culture-induced differences in sentiment on social commerce in general.

## 2 Theoretical background and hypotheses

## 2.1 Social commerce

Internet, social commerce is a relatively new online platform that allows consumers to share information, experience, and commentary about products and services [5–7]. Compared with traditional electronic commerce, in which the Internet only serves as a commerce transaction channel, the benefit of social commerce is aptly summarized in The Wisdom of Crowds by James Surowiecki, who contends that collectively intelligent solutions based on the principles of opinion diversity, participant independence, decentralization, and aggregation are always better [8].

In 2005, Yahoo launched its “Yahoo Shoposphere” platform and its “Pick List” function, thus enabling users to share their product reviews with each other. Its accompanying social network, Yahoo 360, integrated this function to allow users to connect with other reviewers [9,10]. Although this is arguably the first social commerce example [10], there were other e-commerce portals that provided similar types of social commerce functions earlier than that. For example, Amazon, TripAdvisor, and Yelp have provided similar product, service, and destination review functions since 1995 [11]. These review features were later integrated with social networking functions within the portals for those websites, and so customers could not only post comments but also interact. Other social commerce sites such as Facebook started with social networking functions and then integrated commercial activities within their services [10]. Still, others integrated these two functions from the very beginning. For example, eBay.com started its auction services and community ratings at about the same time, which enabled its business to grow exponentially [12].

Research on social commerce has been active since 2005 [7], and studies have explored in the fields of marketing, electronic commerce, and information systems. While most focus on user behaviors, such as social shopping, social networking websites, and social gaming, a few focus on social commerce website design and enterprise strategies. These studies found that user participation is the most important factor for social commerce platform success [13,14]. Additionally, active user participation in social commerce, such as contributing content and building relationships, are critical to social commerce growth [15].

This study focuses on cultural impacts on online reviews. Such reviews are a major type of content contributed by users in social commerce. While there are studies related to cultural impacts on purchase intention in social commerce, only a few explored the cultural impacts on reviews or other user contributed content. For example, Pavlou and Chai [16] find cultural differences influencing the proposed e-commerce adoption model and moderating its key relationships between trust, attitude, perceived behavior control, and transaction intentions by surveying approximately 1500 Chinese and US consumers. Ng [17] suggests that the market penetration of social commerce is more likely to succeed in East Asia than in Latin America, after investigating the moderating effect of culture on social commerce adoption and the mediating effect of trust in facilitating social commerce transaction. Van Slyke et al. [18] report that national culture does influence intentions to purchase online, and the influence of culture is also mediated by e-commerce beliefs.

#

## 2.2 eWOM and online reviews

An online review is considered an electronic version of word-of-mouth (WOM), or eWOM [19]. In traditional markets, WOM is mainly used by consumers to obtain product or service information in addition to other channels like marketers or experts [20]. Because the WOM information comes from family, relatives, and friends and is less influenced by sellers or manufacturers, it is considered more credible and trustworthy [21]. Dichter [22] was one of the earliest scholars to identify four critical motivations for individual WOM behavior: perceived product-involvement, self-involvement (gratification of emotional needs from the product), other involvement (a need to give something to the person receiving the WOM transmission), and message involvement (talk that is stimulated by the way the product is presented in media). This observation was developed further by Sundaram et al. [23] into four positive and four negative motives: altruism, product involvement, self-enhancement, and helping the company, and negative WOM altruism, anxiety reduction, vengeance, and advice seeking. These motives have a strong connection with consumers’ cultural backgrounds.

Because cultural background directly influences an individual’s value framework, it could influence consumers’ sentiments toward their product or service experience or eWOM in social commerce. Previous studies have found that cultural background affects consumers’ decision-making and shopping behavior [24–26]. However, few studies have investigated how consumers with different cultural backgrounds, especially national culture, create, search, and use eWOM information such as online reviews. Among these studies, Chu and Choi [27] found that national culture played a significant factor in affecting consumers’ engagement in eWOM on social networking sites in the United States and China. Lai et al. [28] noted that Amazon reviews on the U.S. site are more likely to express the author’s own opinions on products and contain more recommendations to others than Chinese reviews on Amazon’s Chinese website. They also found Chinese and American customer reviews focused on different aspects of the products. These studies are still limited in their exploration of cultural influence in socia commerce by linking cultural difference details and review sentiments. There is no in-depth analysis of cultural impact on review sentiments across culture, which plays a critical role in facilitating social commerce in different nations’ cultural environments—the focus of this study.

## 2.3 Cultural impacts

Culture at the national, organizational, or unit level exerts a subtle yet powerful influence on individuals behavior, including their perspective as reflected in the reviews [27,29]. There are many definitions of culture, and we adopt a value-oriented definition in this study [30]. This approach defines culture by how it is reflected in the values people express, and it asserts that such values are formed and shaped by the group to which one belongs – the group here could be a team, a company, or a nation. The cultural impacts could be observed in both product- and service-oriented social commerce platforms.

The product-oriented social commerce is global in nature, and the cultural impacts are most frequently observed in international expansions. In the past 20 years, successful online or traditional retailers are continuously expanding beyond developed countries into developing ones, especially countries such as China and India, with promising new waves of consumerism. eWOM plays an important role in such expansion efforts in terms of facilitating cross-border transactions. The expansion efforts in this domain are either successfully localized or quickly eliminated due to failure in acculturation and intense competition. Recent research comparing product reviews across cultures found noticeable differences in average helpfulness ratio and review variance for reviewers in different countries, and it is critical for

companies to understand such differences and better meet the needs of consumers with different cultural backgrounds [31].

Compared with product-oriented social commerce, eWOM on service-oriented social commerce includes equal or greater levels of cultural impacts. Take the example of online ethnic restaurant reviews, the unit of analysis in this study, which are a conjunctive digital asset of hospitability and tourism-related social commerce. There are both networking and economic motivations in hospitability and tourism social commerce [32]. However, different cultural backgrounds can induce different networking and economic motivations. Culture is reflected in the values people expressed in their motivations, and such values are formed and shaped by the ethnic group to which they belong [30]. Consequently, cultural background exerts a subtle yet powerful influence on peoples’ behavior, including their perspective reflected in the eWOM. It is almost self-evident that customers’ eWOM on restaurants are full of culturally induced tastes, preferences, and likes/dislikes. Studies on hospitality business provide insights into cultural differences such as service sensitivity [33,34] and environmental “hygiene issues” [35]. Even internationally franchised fast-food restaurants like McDonalds are still reflections of American culture.

However, because most social commerce platforms such as Yelp and TripAdvisor use the same standard and practice to organize eWOM, like online reviews and ratings, we could easily interpret a rating with reference to our own cultural background instead of realizing that they may express different sentiments and emphases in their eWOM. To address this potential mismatch and analyze the interactions between cultural background and review sentiments, we first adopted Hofstede’s national culture framework.

According to Hofstede’s framework and its later development [29,36,37], we could use six dimensions to characterize national cultures: power distance (PDI), individualism vs. collectivism (IDV), masculinity vs. femininity (MAS), uncertainty avoidance (UAI), long-term orientation vs. short-term orientation (LTO and STO), and indulgence vs. restraint (IND). In Hofstede’s framework, each dimension for a nation is surveyed and then represented with an index, ranging from 1 to 120. For example, the IDV dimension, which indicates the degree to which people in a society are integrated into groups, can be surveyed by examining to what extent people’s self-image in society is defined in terms of “I” or “we.” As a result, the higher end of this dimension represents nations with a preference for a loosely knit social framework or individualism, such as the United States (91) and most other western societies, whereas the lower end of this dimension represents nations with a preference toward collectivism, such as China (20) and Japan (46).

Hofstede’s framework has been widely adopted as a standard to compare different national cultures. In this study, we adopted this framework as the basis to analyze cross-cultural impact on social commerce. In Hofstede’s national culture comparison, we use the United States and Japan as two representatives of the Western and Eastern cultures. Their respective six-dimension index also has major differences, especially in individualism, UAI, and LTO:

$$
(\text {Source: www.hofstede - insights.com / models / national - culture / })
$$

Because culture-induced impacts and misunderstandings in eWOM would most likely happen along those opposing cultural dimensions, it is important to review the definition and implication of individualism, UAI, and LTO here.

Individualism, the low end of this dimension index, is defined as “a preference for a loosely-knit social framework in which individuals are expected to take care of only themselves and their immediate families.” By contrast, the high end of this dimension index, collectivism, refers to “a preference for a tightly-knit framework in society in which individuals can expect their relatives or members of a particular in-group to look after them in exchange for unquestioning loyalty” [36].

The UAI dimension indicates the extent to which the members of a society feel uncomfortable with uncertainty and ambiguity. It could be evaluated with questions like should we try to control the future or just let it happen? Nations with high UAI, such as Japan, are usually intolerant of unorthodox behavior and ideas [36].

The LTO dimension indicates to what extent a society maintains links with its own past while dealing with the challenges of the present and the future. Those cultures with a high index score in this dimension encourage thrift in spending and efforts in modern education as a way to prepare for the future [38].

In addition to Hofstede’s cultural framework, we also need to review two other distinctive cultural characteristics between Eastern and Western countries. The first is the shame vs. guilt worldview [39], or its extended version, the shame, fear, and guilt worldview [40]. Eastern cultures, especially those of China, Japan, and Korea, have a shame-driven social norm, and their citizens’ behavior is largely shaped by what is considered as appropriate by the group or the society, which is quite different from the Western guilt-driven social norm, which is largely shaped by Christian moral discipline. Individuals do what they consider to be appropriate according to the scripture [39]. Food culture is the second distinctive cultural characteristic of Eastern countries related to the hospitality and restaurant industries. The food culture of far Eastern countries is heavily influenced by Confucius, who in the “Analects of Confucius” emphasized the importance of sophisticated food preparation and elegance in food presentation. He stated that one cannot prepare and refine one’s food too much (食不厌精，脍不 厌细). This is in sharp contrast to Western food cultures, such as the British fish-and-chips or American McDonalds, which emphasize simplicity and standardization. These two cultural distinctions are important to our understanding of restaurant reviews.

Next, we hypothesize cultural discrepancies on positive and negative sentiments in online ethnic restaurant reviews between Western and Japanese cultures. We then further compare the cross-culture sentiment differences in reviews that have been voted as helpful in both categories.

## 2.4 Review sentiments

In this section, we examine how restaurant reviews vary between the two cultures based on (a) sentiment orientation, and (b) four basic aspects of restaurant reviews.

Sentiment orientation. Review sentiment has two categories: positive and negative sentiments. Different distributions of such sentiment in online reviews directly affect their perceived trustworthiness among consumers. For example, negative reviews have a greater influence on trust than positive reviews with the presence of a large number of positive reviews [41]. Consumer perceived helpfulness of reviews strongly interacts with review sentiments [42]. In many social commerce platforms, online reviews are displayed based on their sentiment classifications. For example, Amazon explicitly groups customer reviews into favorable (positive sentiment) and critical (negative sentiment) categories.

#

Four basic aspects of restaurant reviews. For a restaurant customer, his or her dining experience can be reviewed in at least four aspects: food quality, service, ambiance, and price fairness [35,43,44]. 1) Food quality refers to a diner’s experience over the cuisine, i.e., the taste, texture, freshness, and presentation style of the food; 2) service refers to the service experienced by the customer in a restaurant, i.e., the reception by the waiter/waitress; 3) ambiance refers to the image or atmosphere of a restaurant; and 4) price fairness refers to whether a customer feels that the overall dining experience they received was worth the money they paid. There is evidence that the above four aspects are relatively stable with time in restaurant reviews. For example, Pantelidis [45] conducted content analyses of online reviews on full-service restaurants in London from 2005 to 2007 and 2008 to 2009. He found the frequencies of topics mentioned relating to customer satisfaction did not change much, which included food (96% and 98%), service (73% and 92%), ambiance (51% and 53%), price (27% and 29%), menu (27% and 27%), and restaurant interior design/décor (8% and 10%).

Online restaurant reviews are an important form of eWOM and help to attract new customers. It was found that the number of reviews a restaurant receives significantly increases the number of visits to the restaurant’s webpage, and higher amounts of page visits correlate with an increased number of positive remarks on food quality, service, and ambiance [46]. This is confirmed by Jeong and Jang [35], who observe that positive experience in service increases the customer desire to share such experience with others. They also found that pleasant experience with restaurant ambiance makes customers likely to invite others to have the same opportunity, and that when customers share their positive experiences of service and food quality, the restaurant becomes more popular and successful.

Similar to motivations behind the decisions to leave a review for other products or service categories, most restaurant diners only want to write a review when they have strong positive or negative sentiments. Such sentiments are very likely related to and influenced by their cultural background when the review objective is an ethnic restaurant, more so than other factors such as education level, neighborhood diversity, or even weather (e.g., temperature and precipitation) [47].

Now, we develop our analysis of cultural impact on review sentiment by following Hofstede’s cultural dimension framework.

Food quality. The most important aspect of any dining experience is food quality [48,49]. A customer who is motivated to write a restaurant review most likely experienced a strong sentiment toward the food quality at the restaurant, regardless of their cultural background. However, there might be a comparative difference in their sentiment emphasis across three other aspects. Japanese culture is traditionally influenced by Confucian food philosophy, rooted in “attitudes toward food as a yardstick to measure a person’s character or moral aptitude” [50], and has a natural emphasis on quality, especially in terms of preparation, presentation, and dining methods. Japan adopted this philosophy in its culinary culture, in such forms as the tea ceremony [51]. In addition, Japanese culture has a higher LTO index and lower indulgence index, and so it is more utilitarian-oriented than Western culture. Hence, we hypothesize that Japanese customers are likely to have more sentiments (positive or negative) on food quality than service, ambiance, or price fairness compared with Western customers.

Service quality. The higher PDI and high collectivism characteristics of Japanese culture indicate a more hierarchical and group-minded society. These characteristics emphasize that each member has a corresponding position in society and expected contribution. In such a cultural environment, quality service by a restaurant is expected and taken for granted, deserving no special mention or compliment.

#

This is in contrast to lower PDI and high individualism in Western culture, which emphasizes individual contribution. Quality service by a member of staff at a restaurant is often appreciated and mentioned. For instance, a review of cross-cultural customer service studies [52] reports that Western customers have a higher need to express dissatisfaction and a greater desire to seek practical recovery after poor service than Eastern customers. In addition, Japanese culture has one of the highest masculinity indexes; a very high masculinity combined with milder collectivism fosters a deeply competitive environment, thus resulting in a drive for excellence and perfection in material services such as restaurants according to Hofstede [53]. Hence, Eastern customers expect the service in Japanese restaurants to be maintained at a high level, thereby leading to less overall complaints in reviews. Thus, we hypothesize that Japanese customers are likely to have fewer sentiments in their reviews on services compared with Western customers.

Ambiance. A diners’ cultural background could influence their perception of the ambiance, or atmosphere, of a restaurant. For example, Ha and Jang [54] found that restaurant ambiance plays a moderate role in customer satisfaction and loyalty-building for Korean restaurants in the United States, together with service quality. Another study found that authentic ambiance in Chinese restaurants in the United States could significantly influence both positive and negative customer sentiments [35]. Although we expect Japanese and Western customers to have similar positive sentiments on better ambiance, their negative sentiments may be different due to the culture of shame within Japanese society [39]. Cleanliness is of importance in Japanese culture [55], and losing face or having a bad image in public is considered shameful. This means a restaurant with bad ambiance may evoke a stronger negative sentiment from Japanese diners. Thus, we hypothesize that Japanese customers are likely to have more negative sentiments in critical reviews on ambiance than Western customers.

Price fairness. The high UAI and LTO characteristics of Japanese culture have an important impact on customers’ sense of price fairness of restaurant reviews. Japanese are on the high end of LTO because of thriftiness and being more likely to save for the future. As a result, Japanese diners might be more sensitive than Western customers to price fairness, as the latter are on the lower end of this dimension, regarding the kind of price fairness that they save. We see the same tendency among eastern consumers. A cross-cultural study on the fast food experiences of Korean and Filipino college students found that both groups view menu prices as the most important attribute [56]. On the other hand, Westerners are sensitive to price for its worth. As an example, a study by [57] reports that US hotel customers perceive the practice of variable pricing to be fairer than Korean customers. Mattila and Patterson [58] frame such a difference as distributive vs. interactional justice. Thus, we hypothesize that Japanese customers are likely to have more positive sentiment in favorable reviews but less negative sentiment in critical reviews on price fairness than Western customers.

In summary, regarding restaurant reviews by Japanese vs. Western customers, we hypothesize that

H1: For favorable reviews, Japanese reviewers respond more positively to food quality and price fairness, while Westerners lean more toward service and ambiance.

H2: For critical reviews, Japanese reviewers respond more negatively to food quality and ambiance, while Westerners lean more toward service and price fairness.

We could extend previous discussions to helpful reviews, which are voted on by customers. A consumer’s cultural background influences not only their review, but also their perception of other

#

reviews’ helpfulness, which has equal influence on customers using the same social commerce platform. We expect that the difference between Japanese and U.S. customers’ reviews should be consistent with their perception of review helpfulness.

On the other hand, there is a natural expected difference between a reviewer and a reader. The former is more concerned with expressing his or her strong sentiments regarding one or more aspects of a restaurant experience, whereas the latter expects or appreciates a more comprehensive description of such experience, instead of just one or two aspects. Thus, those lengthier reviews that covered more aspects of a restaurant would generally be considered more comprehensive and more helpful regardless of national and cultural background [59].

Thus, we have formulated the following hypotheses regarding review helpfulness:

H3: For favorable reviews, Japanese customers consider those with more positive sentiment on food quality and price fairness to be helpful, while Westerners consider those on service and ambiance to be more helpful.

H4: For critical reviews, Japanese customers consider those with more sentiment on food quality and ambiance to be more helpful, while Westerners consider those on service and price fairness to be more helpful.

Figure 1 summarizes the overall model of our four hypotheses. A key relative difference between Western and Japanese cultures lies in the emphasis on service. The model also captures relative differences on how customers in the two cultures focus on the price and ambiance aspects.

Next, we explain our research method and data collection to validate the above hypotheses.

## 3 Method

## 3.1 The data set and preparation

Launched in 2004 by two former PayPal employees, Yelp is one of the leading online tourism social commerce portals. It hosts a website as well as mobile platform for restaurant customers to share their dining experience, to socialize with each other. Yelp expanded into Europe and Asia in 2010 and has 135 million monthly visitors and 95 million reviews as of 2016. It has a market capitalization of \$3.4 billion as of 2017.

Because Yelp is the leading restaurant review platform in the world, it has a relatively comprehensive data set of online reviews contributed by customers from different countries. In this study, we used two data sets. The first came from Yelp’s Data Challenge 2016, which mainly consists of reviews from customers who visited Japanese restaurants in Phoenix and Las Vegas, as well as other cities in North America and Europe. The United States is a country of high ethnic diversity, especially in large cities (e.g., New York and Los Angeles) on the East and West Coasts.<sup>2</sup> Using reviews from less culturally diverse cities minimizes the influence of Asian culture in the Western data set. Figure 3 shows the locations of 250 Japanese restaurants in our data set for the Las Vegas area.

#

To compare the cultural impact, we obtained a second data set from Yelp Japan, which contains restaurant reviews from Tokyo and Osaka. We collected 76,704 reviews from Yelp in the English language and 56,159 from Yelp’s Japanese site in the Japanese language, all of which were collected from under the “Japanese restaurant” business category as classified by Yelp.

However, a restaurant listed under the Japanese restaurant category on Yelp does not necessarily mean the restaurant is Japanese only. In fact, 42% of Japanese restaurants in the United States are cross-listed as Chinese restaurants, and approximately 20% of Korean restaurants are cross-listed as Japanese restaurants on Yelp. This rendered the direct comparison of Japanese restaurant reviews unlikely to be accurate, i.e., a review created by a Chinese customer for a Chinese dish offered by a Chinese restaurant co-listed as a Japanese restaurant on Yelp could be included as a review of a Japanese restaurant if we used the review for sentiment analysis directly.

Considering this reality, we decided to use an indirect method for comparison. We chose the top 10 most popular Japanese entrée items (bento, curry rice, fried rice, gyoza, miso soup, ramen, soba, sushi, tempura, and udon) within the Yelp reviews from these two data sets. We used the association between these 10 entrée items and customer sentiments on review subject focuses (i.e., food, service, ambiance, and price fairness) as the proxy for the association between Japanese restaurants and review sentiments. This “condensed” review data set would not completely eliminate cross-listed Chinese or Korean restaurant reviews, but it would give us a smaller yet much “purer” review of Japanese restaurants.

## 3.2 Analytical tool and procedure

Japanese and English are two distinctive languages. The former uses three scripts, namely kanji (of Chinese origin), hirakana, and katakana [58,59], whereas the latter uses a uniform spelling through one alphabet. Because translating reviews from one language to another could result in losing many details in the process, the best way to preserve sentiments in reviews in both languages is to analyze reviews in their original language with the same method or software technology.

The content analytics technology developed by IBM, Watson Explorer Content Analytics 11.0 (hereafter, WCA), has such a capability. It uses a language analytical technology called TAKMI (Text Analysis and Knowledge Mining) with an accurate sentiment detector [61,62]. WCA uses a document processor based on the Unstructured Information Management Architecture (UIMA) standard and can analyze content in different languages including English and Japanese [62]. Thus, in this study, we used WCA for our sentiment textual analyses.

Because each review has multiple business classification tags, we selected reviews that have a “Japanese restaurant” tag and contain one of the top 10 Japanese entrée items as our criteria. For favorable (positive sentiment) and critical (negative sentiment) reviews, we chose reviews with a star rating of 4 or 5 and 1 or 2, respectively. Helpful reviews are those that received at least one helpfulness vote.

Difference in review counts would be an issue if we relied solely on the frequency of each phrase. For instance, a positive sentiment phrase such as “flavorful broth” may appear 20 times in 100 Japanese language reviews and in 200 English language reviews when those reviews specifically address “ramen” at a Japanese restaurant. To overcome this problem, we extracted the top 50 sentiment expressions by their degree of association with each entrée item. We measured the association between an entrée item and a review aspect by using correlation, as defined by the degree of uniqueness of term frequency

#

in the current document compared with other documents [62]. Suppose that 50% of all reviews mention “sushi.” The phrase “service is great” is seen together with the term “sushi” in some reviews, and the question is how often those two, “sushi” and “service is great,” appear together. Of all the uses of “service is great,” 50% appear in those reviews referring to “sushi” in Country X and 25% in Country Y. In that case, the correlations between “sushi” and “service is great” are 1 (=50%/50%) for Country X and 0.5 (=25%/50%) for Country Y. Using this metric, we can compare how strongly phrases and terms are related to an entrée item even when review counts vary between two data sets. WCA can extract both sentiment phrases and their correlation with each entrée item [64-65].

Once we determined these sentiment phrases, we categorized each sentiment phrase into one of the aspects of restaurant services: food quality, service, ambiance, and price fairness. For those sentiments not related to any of them (such as “I like it”), we categorized it as “other.” The “other” sentiment phrases are often uncategorizable due to their use of pronouns, passive voice (e.g., “it was great”), or ambiguous referent targets. Hence, we listed nouns that correlate highly with those “other” sentiment phrases so that we could estimate the sentiment shares for the “other” phrase category accordingly. For instance, the sentiment share of “service” phrases is 20% whereas that of the “other” is 32%. However, 25% of this 32% relates to the “service” nouns. Thus, the adjusted “service” share is 28%, or 20% plus 25% of 8%. Once adjusted shares are determined, we compare the average shares among the 10 entrée items to evaluate the hypotheses. To categorize the sentiment phrases and nouns, four bilingual speakers and one English speaker (with Japanese translation) independently categorized each phrase (e.g., “it was delicious,” is categorized into “food quality”; “the restaurant is small” is categorized into “ambiance”). When they disagreed, two rounds of discussions took place to reconcile disagreements. On average, 2.9% of phrases and 9.6% of nouns correlated with the phrases had one dissent. Those for two dissents were 0.1% and 0.3% for phrases and nouns. A majority rule was used for those cases.

## 4 Results

## 4.1 Cultural influence on review sentiments

The data analysis indicated that there were explicit differences in both positive and negative sentiment emphases on all four aspects of reviews between Western (mainly U.S.) and Eastern (Japanese) customers (Table 2). Specifically, when Japanese customers post a favorable review, the sentiments among the four aspects, in decreasing order of importance, are food quality, price fairness, ambiance, and service, whereas Western customers prioritize a different order of food quality, service, ambiance, and price fairness. For critical reviews, Japanese reviewers emphasize the negative sentiments on four aspects in decreasing order of importance as food quality, ambiance, service, and price fairness, whereas Western customers have an order of food quality, service, price fairness, and ambiance.

We used a histogram (Figure 4) to visualize the difference between these two cultures and could clearly identify that Japanese diners place more positive sentiment emphasis on food quality (36.7% vs. 29.3%) and price fairness (19.3% vs. 4.5%) at Japanese restaurants than Western diners in their favorable reviews. By contrast, the Western customers have more positive sentiment emphasis on service (25% vs. 3.5%) and ambiance (10.9% vs. 5.9%) than Japanese diners. Hence, H1 is fully supported.

For critical reviews, Japanese diners place more negative sentiment emphasis on ambiance (3.4% vs. 0.3%), whereas Western diners place more negative sentiment emphasis on service (17.5% vs. 2.3%) and price fairness (9.5% vs. 1.7%) than Japanese diners. The results also show that Western customers have

#

slightly more negative sentiment emphasis (33.1% vs. 27.7%) on food quality than Japanese customers, which is not expected in H2. Hence, H2 is partially supported.

## 4.2 Cultural influence on perception of review helpfulness

As mentioned previously, the sentiments expressed in reviews are influenced by a reviewer’s cultural background. This also influences the perception of review helpfulness for customers who vote on reviews, which, in turn, would affect how a customer using Yelp’s reviews chooses a local restaurant. The data analysis on review helpfulness found generally consistent and explicit differences between Japanese and Western customers on what they considered helpful reviews in favorable and critical categories (Table 3).

## †: The numbers are sentiment shares

When viewing favorable reviews, Japanese customers consider those reviews with positive sentiment on food quality, price fairness, ambiance, and service (in decreasing order of importance) to be helpful. On the other hand, Western customers consider food quality and service to be equally important, and ambiance is second in priority while price fairness is least important. When using critical reviews, Japanese customers’ order of importance switched between price fairness and ambiance. They consider negative sentiment on ambiance to be more helpful than price fairness. Western customers order of importance also switched between ambiance and price fairness – they perceive sentiments about price fairness to be more helpful than ambiance in critical reviews. Figure 5 represents of how sentiment shares vary across the two cultures and review valence.

When comparing Japanese and Western customers, we found more sentiments on service by Western customers in both favorable and critical reviews, which is generally consistent with reviewer sentiment patterns identified in H1 and H2. Further, Japanese customers displayed more positive sentiments on food quality, and Western customers had more negative sentiments on price fairness in their perception of review helpfulness, which is also consistent with patterns identified in H2.

We identified two gaps, the first of which is on ambiance. Japanese customers show slightly more positive sentiments (favorable reviews) on ambiance than Western customers. We also found that Japanese customers have more negative sentiments (critical reviews) on food quality, which is consistent with H4 but not consistent with our actual findings in review sentiment on food quality in H2. Thus, H3 is partially supported, whereas H4 is fully supported.

## 5 Discussion

## 5.1 Cultural impacts on social commerce

In management literature, there are considerable studies on cultural challenges by multinational corporations, from efforts of acculturation to hosting culture by such corporations to remain competitive in a foreign market [65,66]. The cultural impacts on marketing and IT have also been explored by researchers in their respective disciplines [67–69]. However, there is relatively little research that explores the cultural impacts on social commerce, essentially a blending of marketing, IT, and management, either due to a lack of interest by researchers or because it is considered less important. This research gap has prompted new research trends, such as smart tourism, a major application domain of social commerce [70].

#

This study provides one example of how national culture could influence social commerce in a critical way. As demonstrated in the analysis, restaurant diners from two distinctive cultural backgrounds may emphasize different elements of their dining experience in their reviews even though their restaurant ratings are the same. Specifically, the sentiment shares on food quality and price fairness are 7.4% and 14.8% higher for Japanese reviews than for their Western counterparts, respectively. At the same time, sentiment shares of service and ambiance are 21.5% and 5% higher for Western customers than for their Japanese counterparts, respectively. These combined results indicate that the Japanese are more sensitive regarding food quality and price fairness than their Western counterparts, a phenomenon caused not only by a belief in the superiority of domestic products due to the country/culture-of-origin effect [71] but also the competitiveness of restaurant businesses within the Japanese market.

Such differences indicate that a Western tourist visiting Tokyo may find a highly-rated sushi restaurant is, upon visiting, not as perfect as indicated on Yelp, simply because he or she has more expectations about service and ambiance whereas a Japanese reviewer may have rated their experience more based on food quality and price fairness. For example, there are quite a few complaints from American diners on Yelp about Sukiyabashi Jiro, a Japanese restaurant featured in David Gelb’s 2011 documentary, Jiro Dreams of Sushi, and which is considered the best restaurant in the country. The complaints mainly related to two aspects: the small restaurant space (ambiance) and the relatively cold attitude of chefs (service) in the restaurant, who serve sushi to customers directly.

## 5.2 Sharing economy and cultural influence

If cultural influence on review is already complex enough, the perception of helpful reviews further increases the complexity. Voting for helpfulness is becoming a de facto standard practice by social commerce practitioners to find quality reviews [72].

This study demonstrated that how consumers vote on review helpfulness reflects their cultural differences. In our second analysis section, Western customers command a 19% higher sentiment share regarding service than their Japanese counterparts in their perception of helpful reviews, regardless of the reviews being positive or negative. This service emphasis is consistent with previous analysis on review creation. It could be explained by the greater expressiveness tendency toward service quality in Western culture [33,73] and confirmed by previous studies on cross-cultural differences in service expectations at Asian ethnic restaurants [74,75]. By contrast, Japanese reviews rarely discuss service quality, nor do Japanese customers perceive reviews on service quality as helpful.

However, the discrepancy between what is important in reviews and the perception of review helpfulness is more interesting. As we mentioned previously, Japanese reviewers place less emphasis on ambiance in favorable reviews. However, because of the shame culture [39], losing face or having a bad image in public is considered shameful. Thus, a positive review regarding ambiance could help a restaurant to avoid losing face, and this may be considered more helpful for Japanese diners, which explains the inconsistency we observed between H1 and H3 on ambiance. This explanation is even more reasonable when considering the sudden difference between Japanese and Western reviewers on the sentiment emphasis of ambiance (3.4% vs. 0.3%) and perceived helpfulness of a review’s sentiment emphasis on ambiance (15.8% vs. 0.3%).

Complexities like those given above have a direct impact on promoting the sharing economy across national boundaries. The sharing economy is built upon various social commerce platforms such as Uber

#

and Airbnb. These platforms all depend on user reviews to facilitate or complete a transaction, and such transactions are increasingly international. Thus, understanding the cultural impact on reviews and perception of reviews is critical to platform expansion and further business growth.

## 5.3 Future research

There are at least two immediate future research directions based on our study. We borrowed four restaurant service attributes from existing hospitability literature [35,43,44] and classified review sentiments based on them. However, there were more than 30% (or one third) of sentiments that could not be clearly related to any of these attributes. Performing a text mining analysis on these sentiments may reveal interesting and important insights. Further, a follow-up study on the impact of culture [30], subculture [76], and micro-culture [67] on social commerce would help us to utilize online reviews and other user-generated content better, especially in smart tourism [70]. For example, we could use big data analytics to identify proactively unique culture-induced review sentiments and rating behavior or bias across different nations. We could then present these patterns to customers with different cultural backgrounds to encourage them to use ratings and reviews appropriately.

## 6 Conclusion

This study demonstrated that national culture plays an important role in shaping customer reviews as well as their perception of what is considered a quality review. When it comes to contributing to Japanese ethnic restaurant reviews, we found that Japanese reviewers place more overall emphasis on food quality, more positive sentiment on price fairness, and more negative sentiment on ambiance than Western reviewers. The perception of review helpfulness by customers is also influenced by national culture. We found Japanese customers consider those reviews with more sentiment on food quality to be more helpful. They also consider reviews with more positive sentiment on ambiance and price fairness and more negative sentiment on ambiance to be more helpful than American customers do. These findings could be explained by Hofstede’s six dimensions of national culture theory [37,77] combined with the shame, guilt, and fear cultural dimension worldviews [39,40]. A more integrated and sophisticated theory should be developed to help social commerce practitioners and researchers accommodate cultural impacts.

Online reviews are the most valuable digital assets of e-commerce portals and an integral component of social commerce platforms. Our findings contributed to filling a gap in the extant research by looking at cultural influence within social commerce.

## 7 References

[1] H. Schultz, Pour your heart into it: How Starbucks built a company one cup at a time, Hachette UK, 2012.

[2] H. Liu, Chop Suey as imagined authentic Chinese food: the culinary identity of Chinese restaurants in the United States, J. Transnatl. Am. Stud. 1 (2009).

[3] N. Yaraghi, S. Ravi, The current and future state of the sharing economy, (2017).

[4] G. Zervas, D. Proserpio, J.W. Byers, The rise of the sharing economy: Estimating the impact of Airbnb on the hotel industry, J. Mark. Res. (2014).

[5] R.G. Curty, P. Zhang, Social commerce: Looking back and forward, Proc. Assoc. Inf. Sci. Technol.

48 (2011) 1–10.

[6] T.-P. Liang, E. Turban, Introduction to the special issue social commerce: a research framework for social commerce, Int. J. Electron. Commer. 16 (2011) 5–14.

[7] C. Baethge, J. Klier, M. Klier, Social commerce—state-of-the-art and future research directions, Electron. Mark. 26 (2016) 269–290. doi:10.1007/s12525-016-0225-2.

[8] J. Surowiecki, The wisdom of crowds, Anchor, 2005.

[9] Y. Research, Social Commerce via the Shoposphere & Pick Lists, (2005). http://www.ysearchblog.com/2005/11/14/social-commerce-via-the-shoposphere-pick-lists/ (accessed January 1, 2017).

[10] C. Wang, P. Zhang, The evolution of social commerce: The people, management, technology, and information dimensions., CAIS. 31 (2012) 5.

[11] M. Luca, Reviews, reputation, and revenue: The case of Yelp. com, (2016).

[12] A. Cohen, The perfect store: Inside eBay, Back Bay Books, 2003.

[13] A. Chen, Y. Lu, P.Y.K. Chau, S. Gupta, Classifying, measuring, and predicting users’ overall active behavior on social networking sites, J. Manag. Inf. Syst. 31 (2014) 213–253.

[14] L. V Casaló, C. Flavián, M. Guinalíu, Antecedents and consequences of consumer participation in on-line communities: The case of the travel sector, Int. J. Electron. Commer. 15 (2010) 137–167.

[15] P.J. Bateman, P.H. Gray, B.S. Butler, Research note—the impact of community commitment on participation in online communities, Inf. Syst. Res. 22 (2011) 841–854.

[16] P.A. Pavlou, L. Chai, What drives electronic commerce across cultures? Across-cultural empirical investigation of the theory of planned behavior., J. Electron. Commer. Res. 3 (2002) 240–253.

[17] C.S.-P. Ng, Intention to purchase on social commerce websites across cultures: A cross-regional study, Inf. Manag. 50 (2013) 609–620.

[18] C. Van Slyke, H. Lou, F. Belanger, V. Sridhar, The influence of culture on consumer-oriented electronic commerce adoption, J. Electron. Commer. Res. 11 (2010) 30.

[19] Y. Chen, J. Xie, Online Consumer Review: Word-of-Mouth as a New Element of Marketing Communication Mix, Manage. Sci. 54 (2008) 477–491. doi:10.1287/mnsc.1070.0810.

[20] J.J. Brown, P.H. Reingen, Social ties and word-of-mouth referral behavior, J. Consum. Res. 14 (1987) 350–362.

[21] P.M. HERR, F.R. KARDES, J. KIM\*, Effects of word of mouth and product attribute information on persuasion: An accessibilty-diagnosticity perspective, J. Consum. Res. 17 (1991) 454–462. doi:10.1016/j.jcps.2014.05.002.

[22] E. Dichter, How word-of-mouth advertising works, Harv. Bus. Rev. 44 (1966) 147–160.

[23] D.S. Sundaram, K. Mitra, C. Webster, Word-of-mouth communications: A motivational analysis,

ACR North Am. Adv. (1998).

[24] M. De Mooij, Consumer behavior and culture: Consequences for global marketing and advertising, Sage, 2010.

[25] J.J. Kacen, J.A. Lee, The influence of culture on consumer impulsive buying behavior, J. Consum. Psychol. 12 (2002) 163–176.

[26] D.J. McCort, N.K. Malhotra, Culture and consumer behavior: toward an understanding of crosscultural consumer behavior in international marketing, J. Int. Consum. Mark. 6 (1993) 91–127.

[27] S.-C. Chu, S.M. Choi, Electronic word-of-mouth in social networking sites: A cross-cultural study of the United States and China, J. Glob. Mark. 24 (2011) 263–281.

[28] J. Lai, P. He, H.-M. Chou, L. Zhou, Impact of national culture on online consumer review behavior, (2013).

[29] G. Hofstede, Organizations and cultures: Software of the mind, McGrawHill, 1991.

[30] E.H. Schein, Organisational culture and leadership: A dynamic view, San Fr. (1985).

[31] C. Danescu-Niculescu-Mizil, G. Kossinets, J. Kleinberg, L. Lee, How opinions are received by online communities: a case study on amazon. com helpfulness votes, in: Proc. 18th Int. Conf. World Wide Web, ACM, 2009: pp. 141–150.

[32] A.M. French, X.R. Luo, R. Bose, Toward a holistic understanding of continued use of social networking tourism: A mixed-methods approach, Inf. Manag. (2016).

[33] M. Laroche, L.C. Ueltschy, S. Abe, M. Cleveland, P.P. Yannopoulos, Service quality perceptions and customer satisfaction: evaluating the role of culture, J. Int. Mark. 12 (2004) 58–85.

[34] H. Liu, L. Lin, Food, Culinary Identity, and Transnational Culture: Chinese Restaurant Business in Southern California, J. Asian Am. Stud. 12 (2009) 135–162. doi:10.1353/jaas.0.0039.

[35] E. Jeong, S. Jang, Restaurant experiences triggering positive electronic word-of-mouth ( eWOM ) motivations, Int. J. Hosp. Manag. 30 (2011) 356–366. doi:10.1016/j.ijhm.2010.08.005.

[36] G.H. Hofstede, Culture’s Consequences: International Differences in Work-related Values/cG. H. Hofstede, sage, 1982.

[37] M. Minkov, G. Hofstede, Hofstede’s fifth dimension: New evidence from the World Values Survey, J. Cross. Cult. Psychol. 43 (2012) 3–14.

[38] G. Hofstede, M. Minkov, Long-versus short-term orientation: new perspectives, Asia Pacific Bus. Rev. 16 (2010) 493–504.

[39] R. Benedict, The chrysanthemum and the sword: Patterns of Japanese culture, Houghton Mifflin Harcourt, 1967.

[40] T. Challies, Shame, Fear, Guilt, (n.d.). https://www.challies.com/articles/shame-fear-guilt/ (accessed December 1, 2017).

[41] S. Ba, P.A. Pavlou, Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior, MIS Q. (2002) 243–268.

[42] Y. Wan, M. Nakayama, The Reliability of Online Review Helpfulness, J. Electron. Commer. Res. 15 (2014) 179–189.

[43] J. Ha, S.C. (Shawn) Jang, Perceived values, satisfaction, and behavioral intentions: The role of familiarity in Korean restaurants, Int. J. Hosp. Manag. 29 (2010) 2–13. doi:10.1016/j.ijhm.2009.03.009.

[44] K. Ryu, H. Lee, W. Gon Kim, The influence of the quality of the physical environment, food, and service on restaurant image, customer perceived value, customer satisfaction, and behavioral intentions, Int. J. Contemp. Hosp. Manag. 24 (2012) 200–223. doi:10.1108/09596111211206141.

[45] I.S. Pantelidis, Electronic Meal Experience: A Content Analysis of Online Restaurant Comments, Cornell Hosp. Q. 51 (2010) 483–491. doi:10.1177/1938965510378574.

[46] Z. Zhang, Q. Ye, R. Law, Y. Li, The impact of e-word-of-mouth on the online popularity of restaurants: A comparison of consumer reviews and editor reviews, Int. J. Hosp. Manag. 29 (2010) 694–700. doi:10.1016/j.ijhm.2010.02.002.

[47] S. Bakhshi, P. Kanuparthy, E. Gilbert, Demographics, weather and online reviews: A Study of Restaurant Recommendations, Proc. 23rd Int. Conf. World Wide Web - WWW ’14. (2014) 443– 454. doi:10.1145/2566486.2568021.

[48] Y. Liu, S.S. Jang, Perceptions of Chinese restaurants in the US: what affects customer satisfaction and behavioral intentions?, Int. J. Hosp. Manag. 28 (2009) 338–348.

[49] Y. Namkung, S. Jang, Are highly satisfied restaurant customers really different? A quality perception perspective, Int. J. Contemp. Hosp. Manag. 20 (2008) 142–155.

[50] R. Sterckx, Food and Philosophy in Early China, in: R. Sterckx (Ed.), Of Tripod and Palate, Palgrave Macmillan US, New York, 2005: pp. 34–61. doi:10.1057/9781403979278\_3.

[51] T. Jiang, On the Historical Evolution of Japanese Tea Culture, Philos. Soc. Sci. 35 (2005) 170–172. https://philpapers.org/rec/JIAOTH (accessed April 6, 2018).

[52] J. Zhang, S.E. Beatty, G. Walsh, Review and future directions of cross-cultural consumer services research, J. Bus. Res. 61 (2008) 211–224.

[53] G. Hofstede, Japanese culture, (n.d.). https://www.hofstede-insights.com/countrycomparison/japan/ (accessed January 12, 2017).

[54] J. Ha, S.C. (Shawn) Jang, Effects of service quality and food quality: The moderating role of atmospherics in an ethnic restaurant segment, Int. J. Hosp. Manag. 29 (2010) 520–529. doi:10.1016/j.ijhm.2009.12.005.

[55] E. Tai, Rethinking Culture, National Culture, and Japanese Culture, Japanese Lang. Lit. 37 (2003) 1. doi:10.2307/3594873.

[56] S.-H. Baek, S. Ham, I.-S. Yang, A cross-cultural comparison of fast food restaurant selection

criteria between Korean and Filipino college students, Int. J. Hosp. Manag. 25 (2006) 683–698.

[57] S. Choi, A.S. Mattila, The role of disclosure in variable hotel pricing: A cross-cultural comparison of customers’ fairness perceptions, Cornell Hotel Restaur. Adm. Q. 47 (2006) 27–35. doi:10.1177/0010880405281681.

[58] A.S. Mattila, P.G. Patterson, Service Recovery and Fairness Perceptions in Collectivist and Individualist Contexts, J. Serv. Res. 6 (2004) 336–346. doi:10.1177/1094670503262947.

[59] S.M. Mudambi, D. Schuff, What Makes a Helpful Online Review ? A Study of Customer Reviews on Amazon.com, MIS Q. 34 (2010) 185–200.

[60] C.K. Leong, K. Tamaoka, Cognitive Processing of Chinese characters, words, sentences and Japanese kanji and kana: An introduction, in: C.K. Leong, K. Tamaoka (Eds.), Cogn. Process. Chinese Japanese Lang., Springer Netherlands, Dordrecht, 1998: pp. 1–10. doi:10.1007/978-94- 015-9161-4\_1.

[61] T. Nasukawa, T. Nagano, Text analysis and knowledge mining system, IBM Syst. J. 40 (2001) 967– 984.

[62] W.-D.J. Zhu, B. Foyle, D. Gagné, V. Gupta, J. Magdalen, A.S. Mundi, T. Nasukawa, M. Paulis, J. Singer, M. Triska, IBM Watson Content Analytics: Discovering Actionable Insight from Your Content, IBM Redbooks, 2014.

[63] M. Nakayama, Y. Wan, Is culture of origin associated with more expressions? An analysis of Yelp reviews on Japanese restaurants, Tour. Manag. 66 (2018) 329–338. doi:10.1016/j.tourman.2017.10.019.

[64] M. Nakayama, H. Kanayama, T. Nasukawa, Cross-cultural comparisons of review aspect importance, in: Int. Conf. Internet Stud., 2015: pp. 1–7.

[65] T. Kostova, K. Roth, Adoption of an organizational practice by subsidiaries of multinational corporations: Institutional and relational effects, Acad. Manag. J. 45 (2002) 215–233.

[66] M. Mendenhall, G. Oddou, The dimensions of expatriate acculturation: A review, Acad. Manag. Rev. 10 (1985) 39–47.

[67] J.E.M. Steenkamp, The role of national culture in international marketing research, Int. Mark. Rev. 18 (2001) 30–44. doi:10.1108/02651330110381970.

[68] D.E. Leidner, T. Kayworth, Review: a review of culture in information systems research: toward a theory of information technology culture conflict, MIS Q. 30 (2006) 357–399. doi:Article.

[69] K. Lim, A. O’Cass, Consumer brand classifications: an assessment of culture-of-origin versus country-of-origin, J. Prod. Brand Manag. 10 (2001) 120–136. doi:10.1108/10610420110388672.

[70] C. Koo, J. Park, J.-N. Lee, Smart Tourism: Traveler, Business, and Organizational Perspectives, (2017).

[71] Z. Gürhan-Canli, D. Maheswaran, Cultural Variations in Country of Origin Effects, J. Mark. Res. 37 (2000) 309–317. doi:10.1509/jmkr.37.3.309.18778.

[72] Y. Pan, J.Q. Zhang, Born Unequal: A Study of the Helpfulness of User-Generated Product Reviews, J. Retail. 87 (2011) 598–612.

[73] B. Stauss, P. Mang, “Culture shocks” in inter-cultural service encounters?, J. Serv. Mark. 13 (1999) 329–346.

[74] R.T. George, Dining Chinese: A Consumer Subgroup Comparison, J. Restaur. Foodserv. Mark. 4 (2001) 67–86.

[75] J. Ha, S. Jang, Effects of service quality and food quality: The moderating role of atmospherics in an ethnic restaurant segment, Int. J. Hosp. Manag. 29 (2010) 520–529. doi:http://dx.doi.org/10.1016/j.ijhm.2009.12.005.

[76] J.W. Schouten, J.H. McAlexander, Subcultures of Consumption: An Ethnography of the New Bikers, J. Consum. Res. 22 (1995) 43–61. doi:10.1086/209434.

[77] G. Hofstede, Culture’s consequences: International differences in work-related values, Sage, London, 1980.

Author Biographies

![](/api/attachments/VPCFCKG2/fulltext/images/0d4d8a826c763a907a35ff3738d7f257c5e1d6e907212b8a431de052e6a2cb9f.jpg)

Makoto Nakayama is Associate Professor at College of Computing and Digital Media (CDM) in DePaul University. Makoto holds a Ph.D. from University of California, Los Angeles and an MBA from University of Texas at Austin. Prior to moving into academe, he served as a software engineer on operating systems, a corporate business planning staff member focusing on technologies, and a product marketing manager on NetWare products. His research interests include online consumer behaviors, text analyses on online consumer reviews, and business intelligence. His papers appeared in Information & Management, Journal of Information Technology, Electronic Markets, and proceedings of international conferences.

![](/api/attachments/VPCFCKG2/fulltext/images/1f8708a7cf33404af7f83d6a76a67c51c3ce39c473f98535badd02d2785af09b.jpg)

Yun Wan is Professor of Computer Information System, and Directors of Graduate Computer Information Systems (MS-CIS) Program and undergraduate BAAS Program at School of Arts and Sciences in University of Houston-Victoria. Dr. Wan’s primary research interests are electronic commerce and the Internet. He also studies artificial intelligence, decision support systems, knowledge management, enterprise systems Integration, and intelligent agent design. He serves as Editorial Board member for International Journal of Information Systems in the Service Sector (IJISSS) and Journal of Electronic Commerce in Organizations (JECO). He is a columnist for Communications of the China Computer Federation (CCCF) since 2013. Wan received his Ph.D. in MIS from University of Illinois at Chicago, B.E. in Software Engineering, B.S. in Economic Management from University of Science and Technology of China.

![](/api/attachments/VPCFCKG2/fulltext/images/6f567263fc6ec0c528766ed111f56cd87a6da77b5f754c604b1f1eab1e8d72ed.jpg)  
Figure 1: Summary of hypotheses

![](/api/attachments/VPCFCKG2/fulltext/images/1495e6717cd30fa720d9ba37f4a85e3b49d084c7d6ed543fac45e9c4f602611e.jpg)

![](/api/attachments/VPCFCKG2/fulltext/images/bb40bd15ee3463ed931d2609d5505c71344bc6c64755ab37d51a4f40f1b512b8.jpg)  
Figure 2: Yelp main site (left, in English language) and Japanese site (right, in Japanese language)

![](/api/attachments/VPCFCKG2/fulltext/images/72fb385ad8ec996bd1611e32481c2cee9442614cb61581dd890411265f67cd44.jpg)

![](/api/attachments/VPCFCKG2/fulltext/images/57e6e0de643863b7f7ef0340c05c90b8d4ef3d48ef3e68b63fadca2aca560aa3.jpg)  
Figure 3: Yelp search first page (left) and locations of the 250 Japanese restaurants in the Las Vegas area (right)

![](/api/attachments/VPCFCKG2/fulltext/images/efd98a7ebefda134684e8f94529ad2dbc363040a69f9ceeca0b28303146bb7a0.jpg)  
Figure 4: Sentiment shares in favorable and critical reviews in Japanese and Western cultures

Review sentiment in helpful reviews  
![](/api/attachments/VPCFCKG2/fulltext/images/d67d13fa0f44fb5c9e36488ec945c65ce9ac9aed3cdada34345a055419e75dcc.jpg)  
Figure 5: Sentiment shares in helpful reviews in Japanese and Western cultures

Table 1: Hofstede Culture Index comparison between Western (United States) and Eastern (Japan) nations

<table><tr><td></td><td>PDI</td><td>IDV</td><td>MAS</td><td>UAI</td><td>LTO</td><td>IND</td></tr><tr><td>Eastern(Japan)</td><td>54</td><td>46</td><td>95</td><td>92</td><td>88</td><td>42</td></tr><tr><td>Western(United States)</td><td>40</td><td>91</td><td>62</td><td>46</td><td>26</td><td>68</td></tr></table>

Table 2: Review sentiment share comparison between Japanese and Western cultures

<table><tr><td rowspan="2"></td><td colspan="2">Positive sentiment – favorable reviews (4-5 stars)</td><td colspan="2">Negative sentiment – critical reviews (1-2 stars)</td></tr><tr><td>Japan</td><td>West</td><td>Japan</td><td>West</td></tr><tr><td>food quality</td><td>36.7%</td><td>29.3%</td><td>27.7%</td><td>33.1%</td></tr><tr><td>service</td><td>3.5%</td><td>25%</td><td>2.3%</td><td>17.5%</td></tr><tr><td>ambiance</td><td>5.9%</td><td>10.9%</td><td>3.4%</td><td>0.3%</td></tr><tr><td>price fairness</td><td>19.3%</td><td>4.5%</td><td>1.7%</td><td>9.5%</td></tr><tr><td>others</td><td>34.6%</td><td>30.4%</td><td>64.9%</td><td>39.6%</td></tr></table>

Table 3: Review helpfulness comparison between Japanese and Western cultures

<table><tr><td rowspan="2"></td><td colspan="2">Helpful favorable reviews (4-5 stars)</td><td colspan="2">Helpful critical reviews (1-2 stars)</td></tr><tr><td>Japan</td><td>West</td><td>Japan</td><td>West</td></tr><tr><td>food quality</td><td>37.9%†</td><td>22.2%</td><td>37.6%</td><td>20.3%</td></tr><tr><td>service</td><td>2.8%</td><td>21.9%</td><td>1.3%</td><td>20.3%</td></tr><tr><td>ambiance</td><td>10.2%</td><td>9.3%</td><td>15.8%</td><td>0.3%</td></tr><tr><td>price fairness</td><td>11.8%</td><td>3.8%</td><td>3.4%</td><td>12.7%</td></tr><tr><td>others</td><td>37.3%</td><td>42.8%</td><td>41.8%</td><td>46.4%</td></tr></table>
