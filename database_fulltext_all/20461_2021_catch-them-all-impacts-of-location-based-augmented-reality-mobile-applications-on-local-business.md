---
otero_id: 20461
otero_key: "3P3JBJG7"
title: "Catch them all: Impacts of location-based augmented reality mobile applications on local businesses"
authors: "Yuan Zhang; Jie Zhang"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103550"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Catch them all: Impacts of location-based augmented reality mobile applications on local businesses

![](/api/attachments/3P3JBJG7/fulltext/images/853f095038df64cdf97de6e0af69067c5d4dbf46a946ee8c0c589abbc4c626ee.jpg)

Yuan Zhang <sup>a</sup>, Jie Zhang \*,b

<sup>a</sup> David D. Reh School of Business Clarkson University, Potsdam, NY 13699, United States

<sup>b</sup> College of Business Administration, PO Box 19437, University of Texas at Arlington, Arlington, TX 76019, United States

## A R T I C L E I N F O

Keywords: Location-based technologies Augmented reality Mobile applications Online reputation Spillover effect Agglomeration effect Difference-in-difference

## A B S T R A C T

Mobile applications implemented with location-based and augmented reality (LBAR) technologies have become a new trend. They alter the app usage patterns, expand their mobility areas, and shape their daily lives. Consequently, local businesses may experience spillover effects in terms of store visits and online reputation. Anecdotal evidence is mixed regarding whether businesses gain from the LBAR apps. There is limited research on how the penetration of LBAR apps impacts local businesses and the potential economic value. To fill the gap in the research literature, we leverage a natural experiment involving the launch of an LBAR mobile app to examine its business impacts on the online reputation of nearby restaurants. We find that, in general, restaurants near the app portals do gain indirect benefits from the entry of the LBAR application in improving their online reputation. This spillover benefit of LBAR applications changes over time, and its internalization depends on the restaurant features, location, and the agglomeration of surrounding businesses. This paper provides useful theoretical and practical insights into the business impacts of LBAR technologies.

## 1. Introduction

In recent years, mobile applications implemented with both Location-based (LB) and Augmented Reality (AR) technologies, such as Ingress, Harry Potter Wizards Unite, and Minecraft Earth have gained widespread popularity with billions of users. LB technologies utilize geographic data to provide geographically personalized services and information to the users. They gradually shape users’ daily lives by encouraging users to explore new places in vicinity areas, enriching their daily activities, and even stimulating their online behaviors on social media [32,33]. For example, Foursquare and Yelp facilitate their users to discover and explore interesting places in local areas and popularize the idea of checking in and sharing locations on social media. On the other hand, AR technology is formally described as "the visual alignment of virtual content with real-world contexts" by Rauschenabel et al. [34], or as "a medium in which digital information is overlaid on the physical world that is in both spatial and temporal registration with the physical world, and that is interactive in time" by Craig [[11], p. 20] and Steffen et al. [39]. For example, in the Pokemon GO app, AR technology projects virtual AR content (e.g., Pokemon and Pokeballs) as an augmented graphic layer on the real-world context, e.g., the dining table in a local restaurant (Fig. 1a); and an AR eyewear displays virtual AR content on the glasses, laying over users’ real-world views through the glasses (Fig. 1b).

The geographically distributed AR content in the LBAR applications significantly expands the physical movement areas of users. Virtual portals in the app provide supporting tools and useful features that attract the users to hang around the physical app portals in the real world, which are mapped to the virtual app portals by geographic coordinates.

As the users of an LBAR app explore new places through the attrac tions of AR content and/or app portals and share their findings on social media, businesses located in the surrounding areas may gain indirect benefits after the app’s entry in the forms of more store visits, business opportunities, and online reputation. Editorial and consultant reports [13,15] have encouraged business owners and practitioners who happen to be located near app portals to take advantage of the benefits from the LBAR apps’ spillover effect through proximity marketing and brand campaigns. However, the penetration of the LBAR apps cannot guar antee positive impacts on local businesses. For instance, Filloon [16] and Zhu [48] cast doubt on the indirect benefits of Pokemon GO, the most popular LBAR app launched in 2016. They reported that not all restaurants close to the physical app portals experience more offline visits nor online awareness and that some players "came in (to the restaurant) but did not get anything to eat or drink." Thus, according to the above anecdotal evidence from news, industry reports, and edito rials, the influence of LBAR apps on local businesses can be a windfall (unexpected benefits) or a scourge (unexpected withdraws). Most of these industry analyses were based on a limited number of contextual cases, a small size of data samples, and/or short-time-frames. These findings might not saliently be representative or generalizable and most of these findings are based on case studies or association analysis in which robustness, causality, and generalization might be compromised and less rigorous. We still need to conduct rigorous research to examine such unexpected consequences of the LBAR technologies. LBAR appli cations such as Google glasses, Facebook’s LBS AR, and Spatial Augmented Reality systems represent the trend of technology’s business application, which calls for a thorough study. However, there is a dearth of research that provides comprehensive quantitative examination regarding the consequences and potential business impacts of LBAR apps. In this study, by building rigorous and comprehensive empirical analyses based on the theoretical foundations from AR and LBS litera ture, we attempt to examine and explain the unexpected business im pacts of LBAR applications systematically.

![](/api/attachments/3P3JBJG7/fulltext/images/ce1de0623539ec0a1fb6fcd7f145d3d6bbd670043ca80bccf54415989daa4e92.jpg)

![](/api/attachments/3P3JBJG7/fulltext/images/1a673f548629c7a5b44edf74350ae850f5a2ad5a438084a719d7a6a73acf1ab6.jpg)  
a  
b  
Fig. 1. a. Pokemon GO’s Spawn Screen. b. An AR Eye Glasses View.

Driven by the above gap in the literature, this study aims to examine whether and how the entry of an LBAR mobile app impacts local busi ness. More specifically, we study the spillover effect of the LBAR mobile app Pokemon GO on local restaurants’ online reputations. We formalize our objective into the following research questions: (1) How does the entry of the LBAR app impact restaurants’ business performance in the form of online reputation metrics? In other words, what are the dynamic effects of the entry of the LBAR app on the online reputation of restau rants near physical app portals? (2) How is the relationship between the entry of the LBAR app and restaurants’ online reputation moderated by restaurant and market-level characteristics? We use online reputation metrics as the proxies of restaurants’ business performance for the following two reasons: First, several studies [8,27,28,32,42] have revealed that online reputation, in the form of review and rating, significantly positively influences and can predict business performance. For example, Luca [27] showed that a one-star increase in Yelp rating leads to a 5-9% increase in restaurant revenue. Second, online reviews are frequently generated and immediately disclosed. Therefore, they can better capture the popular trends about the customer traffic as well as the sentiment and can provide timely signals about the changes in market demand. Therefore, when the real traffic and revenue data are not accessible, we can use online reputation metrics to measure res taurants’ performance.

To address the above questions, we first build a panel dataset by merging the mobile app’s geographic data, download data, Google Trend index, restaurant profiles and characteristics, and restaurant re view data. Then we conduct a set of comprehensive empirical analyses to examine the spillover effect of the LBAR app from various perspec tives. After treating the restaurant samples by propensity scores matching, we use a difference-in-difference (DID) analysis approach to estimate the DID coefficients on each restaurant’s review volume and rating. We consider restaurants near physical app portals as the treat ment group, and restaurants without a portal nearby as the control group, and then compare the DID effects in both the short and the long time frames. Furthermore, we perform a series of additional analyses: we examine both the short and long term DID effects on additional reputation metrics, the treatment intensity of the treatment through a polynomial regression on the distance of the restaurant to its closest portal, and the internalization of the LBAR’s spillover effect based on restaurant and market-level characteristics, for example, chain or non chain type and the local restaurant agglomeration level through Difference-in-Difference-in-Difference (DDD) analyses. We also conduct a series of robustness validations to rule out the potential self-selection threat, check the potential falsification and the reverse causality issues, test the parallel assumption of DID estimation, restore the validity of the control group, and address other potential confounding concerns.

This study makes the following contributions to the extant literature. First, it fills the gap in the literature about the influence and value of AR and LBAR technologies. It contributes to the LB and AR literature by examining the spillover effect and quantifying the economic value of LBAR applications through rich empirical findings. Second, the current study extends AR and LBAR literature by validating the spillover effect on review rating through reasoning AR feature’s influences on users. We observe that the internalization of the spillover effect varies with the restaurants’ and market characteristics. Additionally, our findings indicate that the impacts of the LB application are strengthened with a larger number of local competitors and are negatively associated with geographical distance. Third, our results can be used to estimate the economic impact of the spillover effect due to the LBAR app’s entry, shedding light on the business decisions of local business owners and the monetization strategies of LBAR app developers.

The rest of this paper is organized as follows. In Section 2, we review the related literature, summarize the context mechanism, and propose the hypotheses. Section 3 describes data sources, data processing and a summary of statistics, and introduces the identification strategy. We present our model and findings in Section 4 and provide a series of additional analyses in Section 5. Section 6 includes robustness tests and validation checks. The theoretical and managerial implications are explained in Section 7. Finally, we conclude the paper with limitations and future research.

## 2. Context, literature, and hypotheses development

The LBAR app is a state-of-art fusion application equipped with both LB and AR technologies. Currently, there is a dearth of research in the Information System field on conceptual theories or business impacts of such apps. To build valid reasoning and propose logical hypotheses, we first introduce our research context. Next, we summarize and review the related AR and LBS literature, respectively. Then, by applying the pre vious AR and LBS literature to our research context, we propose our hypotheses regarding the impacts of LBAR technologies on local businesses.

## 2.1. Research context

To examine the spillover effect of LBAR applications on local busi nesses, we choose Pokemon GO, a highly popular LBAR mobile game at its inception as our research context. Players follow the virtual reality map to explore vicinity areas and capture Pokemon using one-time-use virtual items, which can be restocked at physical app portals for free or through in-app purchases. The portals, named PokeStops, are real lo cations of interest predetermined by the developer, distributed in the real world, and mapped with the same virtual world coordinates. Players move into proximity of PokeStops to collect virtual items and to lure Pokemon. Players can only collect free virtual items near PokeStops. Because each restocking session supplies only a limited quantity of the virtual items and takes few minutes to "cool down", players usually linger at the PokeStop, exploring its vicinity areas in order to stock sufficient virtual items. Besides, PokeStops have a significantly higher Pokemon spawn rate than at other places<sup>1</sup>; also the players can only drop a "Lure Module" (a virtual item designed to increase Pokemon ac tivity) in the surrounding area of a PokeStop. Thus, players are also attracted by PokeStops to "lure" more and rarer Pokemon.

## 2.2. The AR literature

By integrating layers of virtual information and virtual contents into users’ perception of the real world [33,39], augmented reality tech nologies can enable spatial, social, or real-time interactions between users and the environment or among users, and can provide users an enriched. immersive, and interactive experience. Nowadays. AR tech nologies have been implemented as wearable devices such as Google glasses, and have been widely applied in such business areas as e-com: merce, tourism and sightseeing, live broadcasting, and online education. The literature on business impacts of AR technologies consists mainly of several conceptual studies [4,5,20] and surveys ([33,34,39]; Yuan and Wu 2008). Rauschnabel et al. [34] and Kunkel et al. [20] proposed that AR app usage leads to users’ positive perceived emotional gratification due to perceived augmentation quality in addition to the utilitarian and hedonic benefits; thus, the AR app can improve a user’s awareness, favorability, and consideration of the brands reflected and projected by the AR app. Bigham [4] and Bulearca and Tamarjan [5] claimed that AR technologies could improve customer satisfaction by enhancing perceived experience value. Yuan and Wu [46] reiterated that AR technologies could improve customers’ entire experience throughout the purchase stages. Steffen and colleagues [39] pointed out that AR and VR technologies could facilitate additional related information to users and reduce physical risks and resource costs when they immerse in the joint of the virtual and physical world. Liu et al. [25], Peukert et al. [30], and Yang and Xiong [44] in their lab experiments and survey arrived at similar conclusions that AR technologies, which allow richer sensory and interactive experiences by facilitating experiential information, could increase the hedonic value of related products and reduce users perceived uncertainty and perceived risks in product evaluation before purchase. These studies suggest that the adoption and use of AR tech nologies can generally enhance the positive aspects of the physical world, specifically boosting consumers’ brand awareness and purchase intentions. However, empirical evidence is lacking regarding the outcome and direct consequences of the penetration of AR technologies on business performance. Moreover, it remains unclear whether the unintentional adoption of AR technologies can have indirect benefits on other agents in the interactive joint of the virtual and physical envi ronment. Our study can fill in the much-needed gap by examining the AR technologies’ business impacts based on a natural experiment of the entry of an LBAR mobile app.

## 2.3. The LB and LBAR literature

Location-based technologies (LBT) have largely been adopted by mobile marketing [14,40]. The literature has documented the business and social impacts of LBT applications mainly in the following two ways:

First, LBT are found to have significant impacts on users’ daily ac tivities [9]; therefore, they support and improve the efficiency of prox imity marketing strategies such as locational targeting promotions [1,7, 14]. By surveying different app users, Cousins and Varshney [9] showed that mobile advertising through LBT increases users’ mobility and has a timely influence on users’ purchase intentions. However, we still do not know the potential impacts of LB apps on local businesses. Through randomized field experiments and surveying focal retailers, Fang et al. [14] showed that given the real-time and location-sensitive features, LB technologies can leverage the advantages of geo-marketing, and thus are widely adopted by businesses as a novel marketing tool. Through field experiments, Chan et al. [7], Fang et al. [14], and Andrews et al. [1] also demonstrated that LB technologies are an effective promotion tool due to their immediate and accumulated impacts on product sales. By con structing and estimating a structural model through data from an online restaurant review platform, Qiu et al. [32] studied the check-in records of LB social network users and found that LB technologies can diversify discovery of the users’ and their friends’ restaurant and can consequently improve their observational learning outcome. Most of the LB literature investigated the firm usage of LB technologies for their own marketing purposes but did not focus on unintended and indirect ben efits of the individual use of LB apps on neighboring businesses. More over, though most of the literature on LB technologies has shown that LB technologies have a positive and effective impact on the business impact. A mixed finding revealed by Filloon [16] and Zhu [48] sug gested that not all local business managers can rip the benefits of such LB apps. This paper intends to verify the specific business impacts of an LB mobile app and uncover the mechanism through comprehensive empirical evidence.

Second, LBT apps with other technologies like AR can directly in fluence consumer behaviors and, subsequently, the performance of local businesses. Through a large-scale interview of Pokemon GO players in different locations, Colley et al. [10] reported how the game changed players’ movement patterns: about 60% of respondents visited at least one new location within a 3 km vicinity area, and about 10% players moved beyond 3 km while playing Pokemon GO. These authors also demonstrated very heterogeneous types of newly-explored locations adjacent to PokeStops and Gyms, including city landmark buildings, parks, libraries, universities, museums, stores, and restaurants. More importantly, 46% of interviewees reported that they had a consumption or dining experience at nearby venues due to Pokemon GO-related ac tivities. Zach and Tussyadiah [47]’s study on Pokemon GO players in the US also supported the respondent reports, i.e., besides improving players’ daily functions and psychosocial functions, Pokemon GO can enhance players’ sense of community, mobility, and physical activity, as well as the unplanned consumption in retail (11% of respondents), restaurants (29%), services (13%), and travel (17%). The above litera ture summarizes rich first-hand evidence that the LBAR apps enlarge users’ mobility in nearby business areas and induce their unplanned consumption behaviors. However, there is a lack of research about how users’ adoption of the LBAR app influences local businesses. The above research gaps call for a comprehensive examination of LBAR applica tions’ influence on local business. Motivated thus, we will explain and justify how the entry and penetration of an LBAR application shape the performance of local restaurants.

![](/api/attachments/3P3JBJG7/fulltext/images/9866bc15f79b4a24cce063f35ff90c7ef5f6c133068fed34beeebe9c0cb929b0.jpg)  
Fig. 2. Illustration of the spillover mechanism.

![](/api/attachments/3P3JBJG7/fulltext/images/154d7fede1e713c66df6f4db2d7dff1e1a294b13e611e25b25b6d10269f40291.jpg)  
Fig. 3. Zoom-in effect of players gathered at a PokeStop (near Santa Monica Pier in August 2016).

## 2.4. The spillover mechanism and hypotheses development

Based on the above literature and our research setting, we illustrate the mechanism regarding Pokemon GO’s spillover effect on local busi ness in Fig. 2. PokeStops (represented by the statue in Fig. 2) are usually landmarks, statues, or arts that convey historical, cultural, and educa tional values<sup>2</sup>. PokeStops attract players to move towards their vicinity areas by providing free in-game items, which are essential for players. During a PokeStop’s "cooling down" time, players tend to stay within a walking distance to the PokeStop for the next round of restocking; meanwhile, players may explore new locations in the vicinity area and linger there (Fig. 3) [10].

The app design increases player’s awareness of surrounding busi nesses and locations by encouraging movement and visits to/lingering behaviors in new locations. The players’ lingering behaviors and exploration can result in new foot traffic and potential business oppor tunities to nearby restaurants as well as a new dining experience for the players themselves. In other words, the app design can increase users likelihood to visit those businesses [10,47]. Consequently, according to the economic patronage effect in Liu et al. [23] and Duan et al. [12], players post reviews on social media. Based on the above mechanism, we expect that there exists a significant spillover effect on the online reputation of the local restaurants that have a PokeStop nearby due to the entry of Pokemon GO.

To sum up the spillover effect mechanism, related literature, and the important functions of PokeStops, we expect that PokeStops have a higher likelihood of attracting players to linger around through LB technologies. When players play at PokeStop areas, LB technologies can further encourage movement, visits, and exploration to new locations, thus increasing user awareness of surrounding businesses. This discovery process can increase users’ likelihood of visiting businesses in the vicinity area. Hence, businesses such as restaurants located close to PokeStops are expected to bring indirect benefits in the form of new traffics. In turn, users can post their experiences through reviews on social media. We expect to observe a larger review volume of those restaurants close to PokeStops. Combining the above literature of LB/ LBAR technologies and summarizing the above reasoning, we propose Hypothesis 1.

Hypothesis 1: The entry of the LBAR application can significantly increase the review volume of a restaurant with portals nearby.

Under our research context, when the app users explore the vicinity areas with their mobile devices through LBS technologies, AR technolo gies first scan and project the real-world environment, add layers of vir tual contents (e.g., portals and items), and display the "augmented reality" on the users’ mobile devices [11]. The augmented contents, which mix the virtual elements and real restaurant scenes, improve the awareness, favorability, and consideration of the reflected brands (e.g., restaurants) through the users’ perceived emotional gratification, especially the he donic benefits [34]. In other words, AR technologies can improve a user’s perceived augmented view of reality (e.g., the real restaurant), and in crease the positive attitude of the restaurant that appears on the AR camera mode. Specifically, while playing the Pokemon GO app and dining in a restaurant, players have a joint immersive experience, which sets virtual game contents and interior/exterior of the restaurants in the same scene. Due to the emotion spillover effect explicated in Yegiyan [45] and the gratification halo in Rauschnabel et al. [34], the hedonic benefits players gain from AR, and the other features of the app can have a positive emotional spillover to the surroundings, such as the restaurant, increasing customers’ evaluation of the restaurants. In addition, given the unique attraction of PokeStops (catching free virtual items and a higher likelihood of catching more and rarer Pokemon near PokeStops), players are more inclined to play around PokeStops, where they also gain more hedonic benefits induced by AR technologies. Furthermore, local restaurants have a higher propensity to benefit from app users/customers’ gratification halo [34] when the restaurants are located close to a PokeStop.

Therefore, having portals nearby can be considered as an added feature of a local business such as a restaurant. Susskind and Chan [38] and Xiang et al. [41] reported that diversified services and hospitality features could have a positive predictive relationship on users’ evalua tion like Yelp rating. Thus, we can consider the portals predetermined by the LBAR application as a positive external feature of a restaurant and expect that proximity to portals can have a positive association with users’ evaluation of the restaurant in terms of review ratings.

Hypothesis 2: The entry of the LBAR application can significantly improve the rating of a restaurant with portals nearby.

Table 1  
Descriptive statistics of the key variables and controls.

<table><tr><td>Variables</td><td>Min</td><td>Max</td><td>Mean</td><td>S.E</td></tr><tr><td>Review volume</td><td>0</td><td>108</td><td>3.58</td><td>0.22</td></tr><tr><td>Rating</td><td>1</td><td>5</td><td>3.81</td><td>0.01</td></tr><tr><td>Checkin volume</td><td>0</td><td>38</td><td>0.99</td><td>0.07</td></tr><tr><td>Competition</td><td>0</td><td>5.42</td><td>3.53</td><td>5.36</td></tr><tr><td>Density</td><td>0</td><td>5.65</td><td>3.30</td><td>0.47</td></tr><tr><td>Distance (m)</td><td>0</td><td>389.33</td><td>34.94</td><td>39.55</td></tr><tr><td>Game Downloads (Million)</td><td>0</td><td>103.44</td><td>22.76</td><td>40.24</td></tr><tr><td>Google Trend index</td><td>0</td><td>263</td><td>34.65</td><td>0.59</td></tr></table>

Table 2  
Probit regression of receiving treatment.

<table><tr><td>Variables</td><td>Coef.</td><td>Std. Err.</td></tr><tr><td>Price level $</td><td>0.345</td><td>0.240</td></tr><tr><td>Price level $$</td><td>0.894***</td><td>0.239</td></tr><tr><td>Price level $$$</td><td>-0.966***</td><td>0.255</td></tr><tr><td>Competition</td><td>-0.007***</td><td>0.001</td></tr><tr><td>Chain</td><td>0.214***</td><td>0.047</td></tr><tr><td>Overall rating</td><td>-0.099</td><td>0.075</td></tr><tr><td>Total volume</td><td>0.001</td><td>0.001</td></tr><tr><td>American</td><td>-0.324***</td><td>0.058</td></tr><tr><td>Chinese</td><td>0.976***</td><td>0.153</td></tr><tr><td>Japanese</td><td>0.565***</td><td>0.108</td></tr><tr><td>Korean</td><td>0.136</td><td>0.138</td></tr><tr><td>Indian</td><td>2.480***</td><td>0.304</td></tr><tr><td>Other Asian fusion</td><td>1.528***</td><td>0.112</td></tr><tr><td>French</td><td>0.013</td><td>0.024</td></tr><tr><td>Italian</td><td>0.529***</td><td>0.084</td></tr><tr><td>Other European</td><td>0.487***</td><td>0.138</td></tr><tr><td>Mexican</td><td>0.444***</td><td>0.073</td></tr><tr><td>Other Latin American</td><td>-0.068</td><td>0.102</td></tr><tr><td>Mediterranean</td><td>0.144</td><td>0.147</td></tr><tr><td>Bakeries and dessert</td><td>-0.090</td><td>0.097</td></tr><tr><td>Bars, beers, wine and liquor</td><td>0.302***</td><td>0.056</td></tr><tr><td>Breakfast and brunch</td><td>0.891***</td><td>0.085</td></tr><tr><td>Coffee &amp; tea</td><td>0.931***</td><td>0.132</td></tr><tr><td>Deli</td><td>-0.495***</td><td>0.146</td></tr><tr><td>Fast food</td><td>0.843***</td><td>0.063</td></tr><tr><td>Juice &amp; frozen desserts</td><td>0.329*</td><td>0.192</td></tr><tr><td>Vegan &amp; vegetarian</td><td>0.006</td><td>0.096</td></tr><tr><td>Other Cuisines and services</td><td>0.553***</td><td>0.141</td></tr><tr><td>Crime report volume</td><td>0.831</td><td>0.472</td></tr><tr><td>Weather</td><td>7.941***</td><td>2.306</td></tr></table>

## 3. Identification strategy and data processing

## 3.1. Data

We built a rich dataset by merging data from various sources: the Pokemon GO geographic data through PogoDev API, restaurant profiles and reviews from Yelp, the app downloads data from Prior Data, and Google Trend index of "Pokemon GO." The data were merged by geocoordinates and date. We also develop new locational attributes such as geo-distance between a restaurant and PokeStops, and PokeStop density around a restaurant.

Following the literature ([19,43], and [21]), we conducted the an alyses on a monthly level. As validation, we also ran the analyses on a weekly level controlling seasonal volatility in Section 6.6. The official launch date of Pokemon GO was July 6, 2016. However, due to the large user base of Pokemon series games across different game platforms, and the prominent popularity during the global beta test since March 2016 prior to the US beta test, Pokemon GO had gained a large number of test users since the US beta test at the end of May 2016. Considering the potential influence of the beta versions, we chose June 2016 as the entry month.

## 3.1.1. Pokemon GO geographic data and Pokemon GO app store data

The Pokemon GO geographic data include the IDs and geocoordinates of PokeStops and gyms in the Dallas-Fort Worth area of Texas.<sup>3</sup> This dataset is collected from Niantic via a third-party API PGOAPI provided by PogoDev. More specifically, we first use the opensource tool www.PokemonGOmap.info to visually select all PokeStops and gyms located in the Dallas-Forth Worth (DFW) area on a Google map. Then via the PGOAPI repository, we downloaded the geocoordinates of PokeStops and Gyms, based on which we determined the locational variables such as PokeStop Density, Competition among restaurants, and Distance to nearest PokeStop for each restaurant based on the general form of the Haversine formula<sup>4</sup>, which calculates the distance using longitude and latitude of the two locations

$$
h a v \left(\frac {d}{r}\right) = h a v (\phi_ {2} - \phi_ {1}) + \cos (\phi_ {1}) * c o s t (\phi_ {2}) * h a v (\lambda_ {2} - \lambda_ {1}),\tag{1}
$$

where hay denotes the Haversine function: hay $\begin{array} { l l l } { \left( \theta \right) = s i n ^ { 2 } \bigg ( \frac { \theta } { 2 } \bigg ) } & { = \frac { 1 - c o s ( \theta ) } { 2 } ; } \end{array}$ d is the distance between two locations, r is the radius of the earth (3,959 miles or 6,371 kilometers); $\phi _ { 1 }$ and $\phi _ { 2 }$ are the latitudes of locations 1 and $^ { 2 , }$ respectively; and $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are the longitudes of locations 1 and $^ { 2 , }$ respectively.

Moreover, we collected the Pokemon GO App’s monthly downloads (denoted as Gamedownloads) from the mobile app market intelligence provider Priori Data and the Google trend index (GoogleTrend) of the key word "Pokemon GO" from https://trends.google.com as the macro-level control variables for the game popularity trend.

## 3.1.2. Restaurants’ business information and reviews from yelp

We chose to focus on restaurants in the Dallas-Fort Worth area of Texas. We obtained an exhaustive list of restaurants by a default organic search by location at Yelp.com. Through Yelp API, we collected the restaurants’ profiles and reviews with dates, ratings<sup>5</sup>, and review texts from Yelp.com. We calculated each restaurant’s monthly rating by averaging the daily newly-posted review ratings per month after excluding the missing observation. We summed up the newly-posted reviews for each restaurant per month as the monthly review volume. Restaurant attributes extracted from business information include restaurant name, address, zip code, price level, cuisine text tags, overall ratings, and total review volume. Review attributes include posting date, rating, check-ins, Yelper ID, and Yelper characteristics.

We manually examined each restaurant and assigned a Chain dummy according to the official definitions of chain restaurants<sup>6</sup>. To capture a restaurant’s CuisinesType, we first classified the customer reported tags of all restaurants to extract 135 unique phrases with the NLP application spaCy, then cluster them into 21 cuisine categories based on Jaccard similarity, and manually label each category by the main cuisine type of the phrase group, such as "American," "Chinese," and "Italian" (See Table 2). Based on the address and zip code of each restaurant, we collected its location city from the database provided by the website of federalgovernmentzipcodes.us and generated a City dummy vector to control the city level fixed effect. The list included 36 cities such as Dallas and Garland. Through the Google Map API, we obtain each res taurant’s geo-coordinates by its address, through which we can calcu lated such control variables as Competition among restaurants, Distance to the nearest PokeStop, and PokeStop Density for each restaurant via the Haversine formula. We calculate the Distance as the distance between a restaurant and any other one and measure the Competition variable by the count of restaurants within a radius of 46 meters<sup>7</sup>. We calculated the distances between a restaurant and each of the adjacent PokeStops and then sorted to obtain the shortest distance, denoted as Distance to the nearest PokeStop. Since players may walk around the plaza to interact with other PokeStops, we controlled the PokeStop Density, which mea sures the count of PokeStops within a radius of 46 meters.

We used the search filter "PokeStop Nearby"<sup>8</sup> as provided by the Yelp website and mobile app after the launch of Pokemon GO. The validity of this filter is justified with a regression discontinuity design using Dis tance to nearest PokeStop as the forcing variable in Section 6.5. We used this filter to download the URLs of restaurants with PokeStops nearby as the treatment group, and the rest of the restaurants without PokeStops nearby as the control group. The parallel trend assumption validated through the relative time approach in Section 4.1 ensures that in the absence of Pokemon GO, the difference between the treatment group and the control group does not vary over time.

## 3.2. Descriptive statistics

After data cleaning, there were a total of 59,999 reviews for 1,215 restaurants from January to December 2016. 77.5% of the restaurants have at least one PokeStop nearby. Table 1 provides the summary of statistics.

## 3.3. Propensity score matching

To address potential endogeneity concerns of a restaurant’s assign ment to the treatment group, we conducted propensity score matching (PSM) before the DID estimation, as suggested by Li [21] and Xu et al. [43]. Besides the test of the parallel assumption through the relative time approach, regression-discontinuity for the condition validation, and context reasoning for the treatment and un-treatment condition, PSM is another classic and one of the most popular approaches to address the possible occurrence of self-selection bias and potential falsification concerns [6]. When we compared the difference between individuals' outcomes with and without the treatment condition. we cannot observe the outcomes for the same entity at the same time. The selection concern could be inflamed if treated, and non-treated entities have differences even when the treatment is not entered. By including entity-level characteristic variables that have no association with the treatment condition, we can estimate the PSM score and match pairs of treated and untreated entities [37]. Therefore, the matched pairs of treated and untreated entities are comparable to each other and are similar in all relevant pre-treatment characteristics. Subsequently, the outcome differences between the treated and the control groups can be attributed to the treatment- "having PokeStop(s) nearby," and the con cerned endogeneity caused by different pre-treatment characteristics of treated and control groups can be excluded. The PSM procedure ensures that the matched pairs of treated and control restaurants have a similar probability of receiving the treatment (having a PokeStop nearby). Therefore, all the processed observations are comparable, so that we can eliminate the self-selection bias and endogeneity concern. Matched observations can improve the propensity that our estimation meets the parallel trend assumption, which is a counterfactual condition that if there were no Pokemon GO entry or PokeStops, restaurants in the treated and the control groups would have identical time trends in terms of reputation metrics. In other words, if the estimated DID coefficients are significant, they are caused by the treatment conditions, not by alternative factors. The parallel trend assumption is formally tested through dynamic DID estimations (a relative time approach) in Section 4.1.

The objective of PSM is to find matching pairs of treated (a restaurant with a PokeStop nearby) and control (one without) restaurants before the entry of Pokemon GO. Then we dropped the unmatched observations and kept the matched ones for DID estimation. Smith and Todd [37] and Caliendo and Kopeinig [6] highlighted the need to include observable entity-level pre-treatment characteristic variables that have no associ ation with the treatment condition to estimate the propensity score between the treated and the control groups. Thus, observable restaurant characteristics are chosen as pre-treatment covariates, including a res taurant’s overall rating, total review volume, chain or non-chain cate gory, cuisine type, price level, and local competition. Additionally, we incorporated location-level pre-treatment covariates, including crime mobility. Next, we estimated the probability of a restaurant receiving the treatment as the function of the above six covariates through a probit regression (results in Table 2). Nineteen covariates are significantly associated with a restaurant’s receiving the treatment on the 0.05 sig nificance level. Accordingly, we obtained the predictive propensity score for both control and treated restaurants.

To avoid the potential confounding concern caused by the entity order, we first randomly sorted the dataset. Then, we matched the treatment and control groups based on their predicted propensity scores, using the above probit model (Table 2). We adopted the Nearest Neighbor (NN) matching algorithm with replacement following meth odology by Rishika et al. [35] and Li [21]. According to Marco and Sabine [6], one of the advantages of this algorithm is that it ensures high matching quality and can reduce matching bias when the propensity scores of the treatment and control groups are not close. As recom mended by Smith and Todd [37], we imposed the matching with a caliper (0.05), which is the tolerance level on the maximum propensity score distance. By doing so, we could avoid bad matches when the dis tance between the treated and control restaurants is large. A high tolerance level can ensure that the obtained matches have a high level of propensity similarity and high matching quality. The PSM yields 273 pairs of matched restaurants. To balance the size of the control and treatment groups, we keep an equal number of treated restaurants that have the closest propensity scores to their untreated counterpart. We end up with 546 restaurants in our analyses.

To evaluate the matching quality, we run t-tests on the means of matched treated and control restaurants. The results in Table 3 suggest that after matching, at a 0.05 significance level, a control restaurant and a treated one have the same propensity of receiving treatment. There after, the current matched control and treatment groups are comparable, and the balance matched observations allow us to use the restaurants without PokeStops nearby as the benchmark to examine the impact of the entry of Pokemon GO through a DID analysis.

Table 3  
t-test result on the matching.

<table><tr><td>Mean treated</td><td>Mean control</td><td>Mean diff.</td><td>t-stat.</td></tr><tr><td>0.346</td><td>0.346</td><td>0.001</td><td>0.10</td></tr><tr><td>0.608</td><td>0.604</td><td>0.004</td><td>0.50</td></tr><tr><td>0.040</td><td>0.044</td><td>-0.004</td><td>-1.31</td></tr><tr><td>40.820</td><td>42.256</td><td>-1.436</td><td>-1.71</td></tr><tr><td>0.405</td><td>0.404</td><td>0.001</td><td>0.16</td></tr><tr><td>3.780</td><td>3.796</td><td>-0.016</td><td>-1.62</td></tr><tr><td>179.840</td><td>184.180</td><td>-4.340</td><td>-1.49</td></tr><tr><td>0.275</td><td>0.286</td><td>-0.011</td><td>-1.61</td></tr><tr><td>0.044</td><td>0.042</td><td>0.001</td><td>0.45</td></tr><tr><td>0.074</td><td>0.070</td><td>0.004</td><td>1.13</td></tr><tr><td>0.028</td><td>0.029</td><td>-0.001</td><td>-0.37</td></tr><tr><td>0.003</td><td>0.003</td><td>0.000</td><td>0.56</td></tr><tr><td>0.101</td><td>0.098</td><td>0.003</td><td>0.72</td></tr><tr><td>0.026</td><td>0.025</td><td>0.000</td><td>0.10</td></tr><tr><td>0.098</td><td>0.099</td><td>-0.001</td><td>-0.15</td></tr><tr><td>0.034</td><td>0.032</td><td>0.002</td><td>0.60</td></tr><tr><td>0.158</td><td>0.157</td><td>0.000</td><td>0.04</td></tr><tr><td>0.042</td><td>0.043</td><td>0.000</td><td>-0.15</td></tr><tr><td>0.033</td><td>0.031</td><td>0.002</td><td>0.70</td></tr><tr><td>0.056</td><td>0.057</td><td>-0.001</td><td>-0.27</td></tr><tr><td>0.256</td><td>0.253</td><td>0.004</td><td>0.56</td></tr><tr><td>0.105</td><td>0.102</td><td>0.002</td><td>0.50</td></tr><tr><td>0.045</td><td>0.043</td><td>0.003</td><td>0.90</td></tr><tr><td>0.021</td><td>0.022</td><td>-0.001</td><td>-0.43</td></tr><tr><td>0.222</td><td>0.226</td><td>-0.004</td><td>-0.63</td></tr><tr><td>0.019</td><td>0.018</td><td>0.001</td><td>0.46</td></tr><tr><td>0.057</td><td>0.057</td><td>0.000</td><td>0.00</td></tr><tr><td>0.033</td><td>0.031</td><td>0.002</td><td>0.79</td></tr><tr><td>0.874</td><td>0.873</td><td>0.001</td><td>0.08</td></tr><tr><td>6.847</td><td>7.156-</td><td>-0.283</td><td>0.91</td></tr></table>

## 4. Empirical analyses

## 4.1. Models

In order to comprehensively capture the causal impacts of the entry of Pokemon GO on the online reputation of restaurants with PokeStops nearby, we adopted (1) the Difference-in-Difference (DID) models to estimate different fixed-time frame effects and (2) the Relative time approach to estimate the dynamic long-term effects in our main analysis. Specifically, we examined the changes of restaurants’ reputation metrics with PokeStops nearby before and after the launch of Pokemon GO, relative to those of restaurants without PokeStops nearby across the same fixed-time frames and at the same period. For more results and robustness checks, we adopted additional models and conducted further analyses as described in Sections 5 and 6, e.g., DDD, polynomial regression, and reversal regression.

## • Fixed-Time-Frame DID Effects

Inspired by Angrist and Pischke (2008) and Imbens and Wooldridge [19], we have the following main econometric estimation models:

$$
\text { Volume } _ {i, t} = \alpha_ {0} ^ {V} + \alpha_ {1} ^ {V} P K G _ {i} + \alpha_ {2} ^ {V} d _ {t} + \beta^ {V} (P K G _ {i} * d _ {t}) + \Theta^ {V} R _ {i} + \Psi^ {V} X _ {t} + \varepsilon_ {i, t} ^ {V}\tag{2}
$$

$$
\text { Rating } _ {i, t} = \alpha_ {0} ^ {R} + \alpha_ {1} ^ {R} P K G _ {i} + \alpha_ {2} ^ {R} d _ {t} + \beta^ {R} (P K G _ {i} * d _ {t}) + \Theta^ {R} R _ {i} + \Psi^ {R} X _ {t} + \varepsilon_ {i, t} ^ {R}\tag{3}
$$

We use online reputation metrics review volume $( V o l u m e _ { i , t } )$ and rating $\left( R a t \dot { m } g _ { i , t } \right)$ as proxies for the foot traffic and user evaluation, respectively, of the restaurant i at period t (Hu et al. 2017, [27,29]). In addition to these two metrics, customers’ social check-ins are shown to have sig nificant impacts on their peers’ restaurant awareness, discovery, and selection [32]. Thus, check-in volume (Checkin ) can also be a business performance indicator. Due to the generalizability concerns regarding these metrics, we examine the impacts of entry of the LBAR app on restaurants’ check-in volume in Section 5.1.

In Eqs. (2) and $( 3 ) , P K G _ { i }$ denotes the treatment dummy: $P K G _ { i } - 1$ when restaurant i is located near PokeStops, and 0 otherwise. $d _ { t }$ is the time switch dummy: $d _ { t } = 1$ when it is after June 2016, and $d _ { t } = 0$ otherwise. $R _ { i }$ is the vector of the observable restaurant time-invariant characteristics: $\begin{array} { r l } { R _ { i } = } & { { } ( D e n s i t y _ { i } } \end{array}$ Competition , Distance , PriceLevel , CuisinesType , City , Chain ). PriceLevel is a price level category vector, including four price level dummies $P _ { 1 } , P _ { 2 } , P _ { 3 }$ , and $P _ { 4 } ,$ which represent the restaurant’s price levels \$ (under \$10), \$\$ (\$11 to \$30), \$\$\$ (\$31 to \$60), and \$\$\$\$ (above \$61), respectively.<sup>11</sup> X is the vector of macrolevel time-variant controls, including Google Trend monthly index (GoogleTrend ), representing Pokemon GO’s general popularity, and Pokemon GO’s monthly downloads (Gamedownloads ). $\varepsilon _ { i , t }$ is the resid ual. We take natural log for the dependent variables, Density , Distance , and Gamedownloads to remove the scale effects.

The two DID coefficients $\beta ^ { V }$ and $\beta ^ { R }$ estimate the average effects of the entry of Pokemon GO on the treated restaurants’ review volume and rating, respectively. They are of key research interest. Because the game effect may be saliently different between a short-term window and a long-term one, we conduct the DID estimations in both terms. Given June 2016 as the treatment launch time, we symmetrically select three months prior to and post this launch time (March to September 2016) as the short-term fixed window, and select January to December 2016 as the long-term fixed window.

## • Dynamic Long-Term Effects- Relative Time Approach

The PSM-DID can saliently diminish the pre-treatment heterogeneity and the potential self-selection concerns and can demonstrate the im pacts of having PokeStop(s) nearby after the entry of the LBAR app on restaurants’ online reputation through different fixed-time frame DID effects. However, we still need to formally validate the parallel assumption of the DID estimation by further solidifying the estimation robustness. Specifically, we need to compare the significance of the DID effects for each period before and after the entry of the treatment. Autor [3] and Gong et al. [18] reported that if all DID coefficients before the entry of the treatment are non-significant and at least one DID coeffi cient is significant after the entry of the treatments, the parallel trend assumption holds true, and there is no pre-treatment heterogeneity threat. Moreover, each period’s DID effects demonstrate how the treatment effects dynamically vary across the long term. To achieve the above two objectives, we estimate the dynamic DID coefficients for each period through the relative time approach, as recommended by the majority of econometrics and IS literature. The explanation and model details are furnished below:

The primary benefit of the relative time approach is attributed to its validity to prove the parallel trend assumption by estimating the DID coefficients with significance level for each period, which can both reveal the changing patterns of the treatment across the long term and further guarantee that the counterfactual treatment group and the control group have the same time trends. If the assumption holds, there is no pre-treatment heterogeneity in trends between the control and the treatment groups. In other words, if the parallel trend assumption holds, without the entry of Pokemon GO, there is no difference in terms of the changes of online reputation metrics between the treated and control restaurants. Meeting this assumption can eliminate the potential threats caused by self-selection bias $[ 7 , 8 , 1 7 ]$ . A rigorous and widely adopted method to verify the parallel trend assumption [24,26] and to examine the validity of the DID estimation ([3] and [31]) is the relative time approach. Typical relative time estimation is conducted by reforming the general form of DID model and rewriting the time-fixed effects into an additional set of time dummies to measure the distance between the current time and the time when treatments are initiated. In our research

p < 0.1

Table 4  
Fixed-time frame did estimation results for full model.

<table><tr><td rowspan="2">Variable (s)</td><td colspan="2">Review volume</td><td colspan="2">Review rating</td></tr><tr><td>Short-frame</td><td>Long-frame</td><td>Short-frame</td><td>Long-frame</td></tr><tr><td>Diff-in-Diff</td><td>0.065** (0.033)</td><td>0.025 (0.026)</td><td>0.057*** (0.013)</td><td>0.080*** (0.016)</td></tr><tr><td>Price level $</td><td>-0.038 (0.035)</td><td>-0.117* (0.067)</td><td>-0.019 (0.015)</td><td>0.007 (0.044)</td></tr><tr><td>Price level $$</td><td>-0.039 (0.034)</td><td>-0.126* (0.067)</td><td>-0.011 (0.015)</td><td>0.0120 (0.044)</td></tr><tr><td>Price level $$$</td><td>0.067 (0.071)</td><td>0.011 (0.014)</td><td>0.086** (0.039)</td><td>0.009 (0.047)</td></tr><tr><td>Competition</td><td>0.011* (0.006)</td><td>0.016*** (0.005)</td><td>0.001 (0.001)</td><td>0.002 (0.003)</td></tr><tr><td>Density</td><td>0.002 (0.009)</td><td>0.010 (0.008)</td><td>0.002 (0.002)</td><td>0.002 (0.005)</td></tr><tr><td>Distance</td><td>-0.005 (0.011)</td><td>-0.011* (0.006)</td><td>-0.002 (0.002)</td><td>-0.009* (0.006)</td></tr><tr><td>Game download</td><td>0.045*** (0.015)</td><td>0.046*** (0.015)</td><td>0.004 (0.003)</td><td>0.037*** (0.009)</td></tr><tr><td>Chain</td><td>0.021 (0.014)</td><td>-0.025** (0.011)</td><td>0.005 (0.004)</td><td>0.008 (0.007)</td></tr><tr><td>Google trend</td><td>0.001 (0.001)</td><td>0.007** (0.004)</td><td>0.002** (0.001)</td><td>0.006*** (0.003)</td></tr><tr><td>R-square</td><td>0.52</td><td>0.51</td><td>0.61</td><td>0.62</td></tr></table>

Note: Standard errors in parentheses.  
p < 0.05  
会会☆p < 0.01

setting, the Pokemon GO entry time is the same for all restaurants. We can rewrite the time treatment interaction for each period to estimate the dynamic DID effects based on the relative distances to the treatment entry time without having to generate the entity-specific relative dis tance dummies. More specifically, our strategy is, first, to include in teractions between the time fixed effect and the treatment dummy for the four pre-treatment months (January to April) ahead of the game entry month and then to remove the interaction for the last pre-treatment month (May) given the dummy variable trap. Second, we rewrite the interactions related to May, the month before the treatment, which serves as the baseline. Thus, if our online reputation metrics satisfy the parallel trend assumption, the pre-DID coefficients (January to May) would all be insignificant, while at least some of the post-DID coefficients (July to December) would be significant. According to Autor [3] and Pischke [31], the distinctive advantage of this method is that the interaction terms after treatment are shown in a dynamic way, which illustrates how the DID effects change over time. Specifically, the above method is to expand our main models (2) and (3) into generalized expressions and form the interaction such that:

According to Autor [3] and Gong et al. [18], the subscripts j and k are the chronicle time distances. $\beta _ { j }$ describes the treatment’s lag effect—effects before the event. Accordingly, $\beta _ { k }$ depicts the treatment’s lead effect—effects after the event. If the parallel trend assumption holds, all lags $( \beta _ { j } )$ should be insignificant. Meanwhile, all or partial leads $( \beta _ { k } )$ should be significant. The dynamic DID coefficients of each period across the long term are summarized in Table 5.

## 4.2. Findings

The DID estimation results in both the short and the long fixed-time frames are reported in Table $^ { 4 , }$ which can provide us with a broad pic ture that having PokeStop(s) nearby after the entry of the LBAR app positively affects restaurants’ online reputation in terms of review vol ume and rating. The short-frame results validate the hypotheses that Pokemon GO positively impacts local restaurants in terms of their online reputation. They suggest that after the launch of Pokemon GO, being close to PokeStops consequently improves the restaurant’s online review volume by 6.5% $( p < 0 . 0 5 )$ , and the average rating by $5 . 7 \% ( p < 0 . 0 1 )$ in the short term. In the long frame, only the DID coefficient of review rating is significantly improved by $8 \% ( p < 0 . 0 1 )$ , but the positive short frame DID effect on review volume diminishes to a non-significant level.

$$
\text { Volume } _ {i, t} = \sum_ {j} \beta_ {j} ^ {V} * \text { PriorPKG } _ {i, t} (j) + \delta^ {V} * \text { PKG } _ {i, t} + \sum_ {k} \beta_ {k} ^ {V} * \text { PostPKG } _ {i, t} (k) + \theta^ {V} R _ {i} + \psi^ {V} X _ {i, t} + \varepsilon_ {i, t} ^ {V}
$$

The dynamic long-term effect results for both reputation metrics are summarized in Table $^ { 5 , }$ which demonstrates the more detailed dynamic temporal effects of being closed to PokeStop(s) after the entry, and can further confirm the accumulative findings of the fixed-time frame analysis. Recalling the two objectives of the relative time approach, first, all lag coefficients (the coefficients for all the pre-treatment periods) are insignificant and most of the lead coefficients (the coefficients for all the post-treatment periods) are significant. Thus, the parallel trend assumption is verified, and the pre-treatment heterogeneity and poten tial self-selection concerns can be eliminated. Second, to examine the dynamic temporal DID effects across the long term, we observe that for the treated restaurants, the significant review volume increments sus tain for about four months after the entry of the LBAR app, and the significant review rating increments start from the entry time and sus tain for at least six months after the entry. More specifically, for res taurants located nearby a PokeStop(s), four months after the app’s entry, restaurants on average gain 1.57 times faster growth in review volume

(4)

$$
\text { Rating } _ {i, t} = \sum_ {j} \beta_ {j} ^ {R} * \text { PriorPKG } _ {i, t} (j) + \delta^ {R} * \text { PKG } _ {i, t} + \sum_ {k} \beta_ {k} ^ {R} * \text { PostPKG } _ {i, t} (k) + \theta^ {R} R _ {i} + \psi^ {R} X _ {i, t} + \varepsilon_ {i, t} ^ {R}\tag{5}
$$

Table 5  
Dynamic effects of relative time approach DID estimation.

<table><tr><td></td><td>Volume</td><td>Rating</td></tr><tr><td>5 Month prior</td><td>0.051 (0.032)</td><td>0.013 (0.009)</td></tr><tr><td>4 Month prior</td><td>0.014 (0.023)</td><td>0.012 (0.009)</td></tr><tr><td>3 Month prior</td><td>-0.025 (0.023)</td><td>0.008 (0.009)</td></tr><tr><td>2 Month prior</td><td>-0.011 (0.023)</td><td>0.013 (0.009)</td></tr><tr><td>1 Month prior</td><td>-0.007 (0.031)</td><td>0.015 (0.012)</td></tr><tr><td>Current</td><td>0.088 (0.029)</td><td>0.029*** (0.010)</td></tr><tr><td>1 Month post</td><td>0.066*** (0.023)</td><td>0.092*** (0.009)</td></tr><tr><td>2 Month post</td><td>0.085*** (0.028)</td><td>0.071*** (0.009)</td></tr><tr><td>3 Month post</td><td>0.039* (0.023)</td><td>0.016*** (0.008)</td></tr><tr><td>4 Month post</td><td>0.036** (0.018)</td><td>0.011*** (0.007)</td></tr><tr><td>5 Month post</td><td>0.024 (0.016)</td><td>0.057*** (0.006)</td></tr><tr><td>6 Month post</td><td>0.005 (0.021)</td><td>0.015*** (0.009)</td></tr><tr><td>Price level $</td><td>-0.121* (0.066)</td><td>0.011 (0.039)</td></tr><tr><td>Price level $$</td><td>-0.125* (0.067)</td><td>0.0121 (0.044)</td></tr><tr><td>Price level $$$</td><td>0.011 (0.011)</td><td>0.012 (0.049)</td></tr><tr><td>Competition</td><td>0.019*** (0.005)</td><td>0.003 (0.003)</td></tr><tr><td>Density</td><td>0.012 (0.007)</td><td>0.001 (0.003)</td></tr><tr><td>Distance</td><td>-0.021* (0.005)</td><td>-0.011* (0.004)</td></tr><tr><td>Game Download</td><td>0.045*** (0.015)</td><td>0.037*** (0.007)</td></tr><tr><td>Chain</td><td>-0.027** (0.013)</td><td>0.009 (0.007)</td></tr><tr><td>Google Trend</td><td>0.009** (0.004)</td><td>0.007*** (0.003)</td></tr><tr><td>R-square</td><td>0.49</td><td>0.57</td></tr></table>

Note: Standard errors in parentheses.  
<sup>\*</sup> p < 0.1  
p < 0.05  
$\begin{array} { r } { p < 0 . 0 1 . } \end{array}$

than the current growth. For treated restaurants, at least six months after the entry of the LBAR app, restaurants on average gain 8.04 times faster growth in rating.

In summary, based on the findings of both the fixed-time-frame DID analysis and the dynamic Relative Time Approach DID analysis, the launch of Pokemon GO significantly enhances restaurants’ online rating in both time frames and review volume in the short run in our research setting. Thus, both H1 and H2 are supported. Based on the AR marketing theory, as an LBAR app, Pokemon GO can have spillover effects on the local businesses that appear in the AR views during users’ gameplay. This positive spillover effect enhances the value of those restaurants located in the proximity of PokeStops. Thus, as a positive and desirable attribute, "PokeStop nearby" contributes to customers’ perceived quality of a restaurant and thus improves their evaluations in terms of online ratings. The improvement in the ratings of the treated restaurants vali dates H1, and justifies and extends the current AR literature [5,34]

The significant short-term boost of treated restaurants’ review vol ume supports H2. This impact tapers after about four months post entry and diminishes to a non-significance level. This faster worn-out volume DID can be explained by the platform design. Since a customer can only post one review per restaurant but can update the existing review and rating over time on the Yelp website, the review volume of a restaurant reflects the number of new customers but not repeated ones. Since its entry, Pokemon GO has become extremely popular rapidly, resulting in a significant increase in the number of players who move around and explore nearby areas hunting Pokemon. This LBAR app changes the users’ online and offline social and physical activities within a very short time frame. When they find interesting landmarks or landscape and experience dining services from restaurants in the vicinity of PokeStops, these players may become customers and post their experiences on so cial media, which increase the review volume of the restaurants. How ever, as the phenomenal popularity of Pokemon GO dies down quickly, the monthly US downloads dropped from the peak of 103.4 million to 2.7 million by December 2016. Resultantly, the long-term review vol ume increment becomes insignificant due to the decrease of new traffic

Based on the above results, we can estimate the economic signifi cance of the spillover effect of the entry of LBAR applications in terms of restaurants’ revenue. The DID results in Table 4 suggest that Pokemon GO’s entry increases the ratings of treated restaurants by 5.7% in the short term and 8.0% in the long term. Table 1 shows that the average rating of the restaurants in our sample is 3.81 stars. According to Luca [27], a one-star increase in a restaurant’s Yelp rating results in a 9% increase in its revenue. Combining these, we can roughly estimate the entry of Pokemon GO increases the monthly revenue of a PokeStop nearby restaurant by $1 . 9 6 \% ( = 3 . 8 1 \ast 5 . 7 \% ^ { \ast } 9 \% )$ in the short term, and by 2.75% $( = 3 . 8 1 \times 8 . 0 \% \ast 9 \% )$ in the long term. Since the PokeStops are exogenously chosen by Niantic during our research period, the geo-location of a restaurant near a PokeStop is expected to increase its revenue with no additional marketing expenses.

Table 6  
DID estimation on checkin volume results for full model.

<table><tr><td>Variable(s)</td><td>Short-term</td><td>Long-term</td></tr><tr><td>Diff-in-Diff</td><td>0.028 (0.068)</td><td>0.015** (0.009)</td></tr><tr><td>Price level $</td><td>0.164** (0.073)</td><td>-0.001 (0.012)</td></tr><tr><td>Price level $$</td><td>0.342*** (0.072)</td><td>0.011 (0.013)</td></tr><tr><td>Price level $$$</td><td>-0.074 (0.185)</td><td>0.002 (0.003)</td></tr><tr><td>Competition</td><td>-0.001* (0.001)</td><td>0.002 (0.005)</td></tr><tr><td>Density</td><td>0.002*** (0.001)</td><td>-0.008 (0.006)</td></tr><tr><td>Distance</td><td>-0.011 (0.008)</td><td>-0.037*** (0.009)</td></tr><tr><td>Game Download</td><td>0.002*** (0.001)</td><td>0.023*** (0.008)</td></tr><tr><td>Chain</td><td>-0.052 (0.04)</td><td>-0.003*** (0.001)</td></tr><tr><td>Google trend</td><td>0.001* (0.001)</td><td>0.01** (0.004)</td></tr><tr><td>R-square</td><td>0.64</td><td>0.62</td></tr></table>

Note: Standard errors in parentheses.  
\*p < 0.1.  
\*\*p < 0.05.  
\*\*\*p < 0.01.

## 5. Additional analyses

To cross-validate our main results and also to identify richer patterns, we conduct additional analyses: (1) we check the impact of the entry of the LBAR app on another performance indicator, Checkin volume, of the treated restaurants (Section 5.1); (2) to verify the mechanism proposed in Section 2.1, we inspect the treatment intensity from a geographical perspective by replacing the DID interaction term with the polynomial terms of the distance between a restaurant and its closest PokeStop and conducting a polynomial regression (Section 5.2); (3) to further examine how the internalization of the spillover effect, we conduct the Difference in Difference in Difference (DDD) analyses by incorporating more inter action terms (e.g., the competition level (Section 5.3), and the chain/ non-chain dummy (Section 5.4) and the treatment condition).

## 5.1. The DID analysis on check-ins

Yelp allows its users to "check in" by sharing their location infor mation on social media when visiting a restaurant. By using the check-in feature, the customers broadcast to their followers on Yelp that they are at that restaurant. Accordingly, check-ins may increase the awareness of the restaurant through observational learning and peer influence. Check-ins may not directly measure a restaurant’s online reputation; however, it is a critical metric that business owners value [32]. We consider the volume of check-ins as another business performance in dicator and conduct a DID estimation for both the short and long terms to examine the impacts of Pokemon GO on the treated and control res taurants (Eq. 6).

$$
\text { Checkin } _ {i, t} = \alpha_ {0} ^ {C} + \alpha_ {1} ^ {C} P K G _ {i} + \alpha_ {2} ^ {C} d _ {t} + \beta^ {C} (P K G _ {i} * d _ {t}) + \Theta^ {C} R _ {i} + \Psi^ {C} X _ {i, t} + \varepsilon_ {i, t} ^ {C}\tag{6}
$$

We estimate the above models and show the results in Table 6.

After the entry of Pokemon GO, the check-in volume of treated res taurants insignificantly increases in the short term, and the increment accumulates to a significant level of 1.5% $( p < 0 . 0 5 )$ in the long term. On Yelp, a user can check in to the same restaurant multiple times, unlike

Table 7  
Results of treatment intensity identity- polynomial regression.

<table><tr><td></td><td>Review volume</td><td>Rating</td></tr><tr><td>Distance</td><td>-2.203*** (0.515)</td><td>-0.151** (0.06)</td></tr><tr><td> $Distance^2$ </td><td>-0.268*** (0.076)</td><td>-0.099** (0.039)</td></tr><tr><td>Price level $</td><td>-7.923** (4.038)</td><td>-0.017 (0.014)</td></tr><tr><td>Price level $$</td><td>-6.174* (3.678)</td><td>-0.039*** (0.013)</td></tr><tr><td>Price level $$$</td><td>-5.361** (2.114)</td><td>0.0823** (0.035)</td></tr><tr><td>Competition</td><td>0.301*** (0.0692)</td><td>0.045*** (0.009)</td></tr><tr><td>Density</td><td>0.237*** (0.057)</td><td>0.037*** (0.008)</td></tr><tr><td>Game download</td><td>0.02346 (0.023)</td><td>0.021 (0.096)</td></tr><tr><td>Google trend</td><td>0.011*** (0.007)</td><td>0.036 (0.295)</td></tr><tr><td>Chain</td><td>-6.429** (3.07)</td><td>-0.011* (0.005)</td></tr><tr><td>R-square</td><td>0.61</td><td>0.51</td></tr></table>

Note: Standard errors in parentheses.

$$
^ {*} p <   0. 1.
$$

$$
^ {* *} p <   0. 0 5.
$$

$$
p <   0. 0 1.
$$

Table 8  
Summary of DDD estimation results of competition.

<table><tr><td>Reputation metrics</td><td>DD</td><td>Competition</td><td>Competition x DID</td></tr><tr><td>Volume</td><td>0.024 (0.027)</td><td>0.003** (0.001)</td><td>0.002*** (0.001)</td></tr><tr><td>Rating</td><td>0.078*** (0.017)</td><td>0.001* (0.001)</td><td>0.002* (0.001)</td></tr><tr><td>Check-in</td><td>0.011** (0.005)</td><td>-0.001* (0.001)</td><td>0.001* (0.001)</td></tr></table>

Note: DDD Coef. Standard errors in parentheses.

$$
p <   0. 0 1.
$$

posting reviews. Thus check-in volume can reflect the traffic of both new and repeat customers to a restaurant. While review volume result (Table 3) suggests that the entry of Pokemon GO causes an immediate increase in new traffic to restaurants in proximity to PokeStops. Even though that effect tapers off with the cooling down of the app downloads in the long run, the check-in result shows that Pokemon GO can still cause a significant increase of repeated visits of the app users in the long term.

## 5.2. Treatment intensity analysis - polynomial regression with the distance variable

In the previous analyses, the treatment condition of a restaurant depends on whether it has a PokeStop nearby. However, it remains unclear if the treatment effects increase or decrease for a business that is located closer to or further away from PokeStops. To examine whether and how the treatment intensity shapes the effect size, more specifically to examine if the geographical distance plays a primary role in deter mining the effect size of PokeStops on local businesses, we run the following polynomial regression on review volume and review rating, including both the control and the treated entities for the long term by entering the distance to the closet PokeStop and its square term as in dicators of treatment intensity. Distance is defined as the distance of restaurant i to the nearest PokeStop as in given in Eq. (1).

$$
\text { Volume } _ {i, t} = \alpha_ {0} ^ {V} + \alpha_ {1} ^ {V} \text { Distance } _ {i} + \alpha_ {2} ^ {V} \text { Distance } _ {i} ^ {2} + \Theta^ {V} R _ {i} + \Psi^ {V} X _ {i, t} + \varepsilon_ {i, t} ^ {V}\tag{7}
$$

$$
\text { Rating } _ {i, t} = \alpha_ {0} ^ {R} + \alpha_ {1} ^ {R} \text { Distance } _ {i} + \alpha_ {2} ^ {R} \text { Distance } _ {i} ^ {2} + \Theta^ {R} R _ {i} + \Psi^ {R} X _ {i, t} + \varepsilon_ {i, t} ^ {R}.\tag{8}
$$

The results of the polynomial regression are summarized in Table 7. We find that two treatment intensity indicators, the distance, and the area size are significantly and negatively associated with both review volume and rating. More specifically, a 1% distance closer to the closest PokeStop can increase the restaurant’s review volume by 2.20% $( p <$ 0.01), and increase the review rating by $0 . 1 5 \% ( p < 0 . 0 5 )$ . In addition, the significant and negative coefficients of the $D i s t a n c e ^ { 2 }$ term suggest

Table 9  
Summary of DDD estimation results of chain/non-chain.

<table><tr><td>Reputation metrics</td><td>DD</td><td>Chain</td><td>Chain x DID</td></tr><tr><td>Volume</td><td>0.040 (0.023)</td><td>-0.005* (0.003)</td><td>-0.012*(0.007)</td></tr><tr><td>Rating</td><td>0.076*** (0.014)</td><td>-0.001 (0.002)</td><td>0.003 (0.005)</td></tr><tr><td>Check-in</td><td>0.012** (0.005)</td><td>-0.002** (0.001)</td><td>-0.007** (0.003)</td></tr></table>

Note: DDD Coef. Standard errors in parentheses.

$$
^ {*} p <   0. 1.
$$

$$
p <   0. 0 1.
$$

that the spillover effect of the LBAR app on reputation metrics di minishes with the distance to PokeStops at an increasing rate.

Thus, the geographical distance has a significant direct relationship with the reputation of local businesses. This finding strengthens our hypotheses and corroborates our proposed spillover mechanism. App users are attracted by PokeStops in order to interact with them for the many useful features. From there, they wander around and linger in the adjacent shops and restaurants as new traffic. The result also implies that being closer to a PokeStop (a decrease in distance to PokeStops) is an attractive attribute of restaurants and contributes to the spillover effect at an increasing rate.

## 5.3. The moderation effect of restaurants’ agglomeration level

To further examine whether a restaurant is surrounded by a large number of competitors strengthens or suppresses the treatment density after the entry of Pokemon GO, we incorporate the Competition metric with the interaction terms to re-run the DID estimation for the long-term frame. We summarize the results in Table 8.

The results show that the competition level of a restaurant is posi tively associated with its review volume. Furthermore, geographic concentration or agglomeration of restaurants can strengthen the spill over effect of Pokemon GO on restaurants’ online reputations. Poke Stops attract the Pokemon GO app users to gather around, which creates the patronage effect for the nearby businesses [23]. Among the restau rants close to PokeStops, those located in a higher concentrated area will attract more visitors due to the agglomeration effect (e.g., more dining choices). Such visitors become potential customers and may generate a greater number of reviews. In addition, restaurants that can thrive in a high-level competitive business environment provide certain unique features and experiences. The virtual contents in the LBAR app can augment customers’ real experiences, improve the variety of services and features of the treated restaurants, thereby enhancing the cus tomers’ restaurant evaluations.

## 5.4. The moderation effect of restaurants’ chain/non-chain property

About 40% of the restaurants in our sample are chain stores. To examine whether this property of restaurants moderates the treatment density after the entry of Pokemon GO, we add a dummy variable for the chain restaurant with its interaction terms to re-run the DID estimation for the long-term frame.

Results given in Table 9 show that chain restaurants benefit less from the spillover benefits from the entry of the LBAR application. For chain restaurants, such as McDonald’s and Chipotle, customers were already aware of the brands and formed perceived expectations and evaluations prior to visiting the stores. In contrast, for non-chain restaurants, the spillover benefits of the LBAR app can substitute the branding effect to a certain degree by promoting awareness, consideration and favorability to the app users. Thus, independent or non-chain restaurants will benefit more from the LBAR app.

Table 10  
Reverse regression, rating on DID.

<table><tr><td>Diff-in-Diff</td><td>Without lag term</td><td>With lag term</td></tr><tr><td>Rating</td><td>-0.006 (0.005)</td><td>-0.006 (0.005)</td></tr><tr><td>Rating_AR1</td><td>-</td><td>-0.007 (0.005)</td></tr><tr><td>Price level $</td><td>-0.005 (0.127)</td><td>-0.015 (0.127)</td></tr><tr><td>Price level $$</td><td>-0.003 (0.127)</td><td>-0.013 (0.127)</td></tr><tr><td>Price level $$$</td><td>-0.017 (0.135)</td><td>-0.024 (0.135)</td></tr><tr><td>Competition</td><td>-0.001 (0.001)</td><td>-0.001 (0.001)</td></tr><tr><td>Density</td><td>0.001 (0.001)</td><td>0.001 (0.001)</td></tr><tr><td>Distance</td><td>-0.001 (0.001)</td><td>0.001 (0.001)</td></tr><tr><td>Game Download</td><td>0.001*** (0.001)</td><td>0.002 (0.001)</td></tr><tr><td>Google Trend</td><td>0.001*** (0.001)</td><td>0.001 (0.001)</td></tr></table>

Note: Standard errors in parentheses.

$$
^ {*} \mathrm{p} <   0. 1
$$

$$
^ {* *} \mathrm{p} <   0. 0 5
$$

$$
p <   0. 0 1
$$

## 6. Robustness validations

To validate the above findings, we discuss the potential issues and conduct a series of robustness tests. First, to rule out the potential selfselection and endogeneity issues, we conduct extensive research by prudently scrutinizing the official documents regarding the selection of PokeStops (Section 6.1). Second, in order to remove the reversal cau sality concern, we run a falsification test by regressing reputation met rics back on the DID indicators (Section 6.2). In Section 6.3, we check the potential confounding issues. In Section 6.4, we design a regression discontinuity model for the control group validation. Finally, we vali date our DID estimation results at a different time-frequency in Section 6.5.

## 6.1. Endogeneity concern of PokeStops

The potential self-selection bias could jeopardize the randomness of the treatment and threaten the validity of the DID estimation results. However, according to the official game website and the online com munities of the app developers<sup>12</sup>, during our research period restaurant owners could not nominate their stores into PokeStops. In the 1st gen eration Pokemon GO, all PokeStops and gyms are imported from the portal database of Ingress, which is a previously launched AR mobile game by Niantic<sup>13</sup>. PokeStops or Ingress Portals are crowdsourced and are generally considered interesting locations by the public. Yet, players cannot create new portals or PokeStops in the game<sup>14</sup>. Instead, all portal candidates must be submitted to Niantic through an application process. Nonetheless, Niantic suspended the application process from September 2015 to September 2017<sup>15</sup>. During our research period (Jan-Dec 2016), there are no new PokeStops, thus restaurant owners have no opportunity to self-select their locations to become PokeStops. Additionally, all PokeStops’ location is fixed at least during our research time frame.

Second, we search all related official documents to examine whether any features of PokeStops or portals can potentially cause the alternative

Table 11  
Reverse regression, volume on DID

<table><tr><td>Diff-in-Diff</td><td>Without lag term</td><td>With lag term</td></tr><tr><td>Volume</td><td>0.009 (0.006)</td><td>0.008 (0.006)</td></tr><tr><td>Volume_AR1</td><td>-</td><td>-0.005 (0.009)</td></tr><tr><td>Price level $</td><td>-0.001 (0.127)</td><td>-0.006 (0.127)</td></tr><tr><td>Price level $$</td><td>0.003 (0.127)</td><td>-0.001 (0.127)</td></tr><tr><td>Price level $$$</td><td>-0.012 (0.135)</td><td>-0.014 (0.135)</td></tr><tr><td>Competition</td><td>-0.001 (0.001)</td><td>-0.001 (0.001)</td></tr><tr><td>Density</td><td>0.001 (0.001)</td><td>0.001 (0.001)</td></tr><tr><td>Distance</td><td>-0.001 (0.001)</td><td>-0.001 (0.001)</td></tr><tr><td>Game Download</td><td>0.002*** (0.001)</td><td>0.002 (0.001)</td></tr><tr><td>Google trend</td><td>0.001*** (0.001)</td><td>0.001 (0.001)</td></tr></table>

Note: Standard errors in parentheses.  
\*p < 0.1.  
\*\*p < 0.05.

$$
p <   0. 0 1.
$$

difference between the treated and control restaurants. The PokeStop nomination submission guidelines<sup>16</sup> by Niantic state that PokeStops or portals aim to help players explore, discover, and enjoy vicinity areas. Eligible nominations include locations with historical, educational, or cultural value and significance, with pieces of art or unique architecture and locations like hyper-local spots or described as a "hidden gem," such as tourist or adventurous attractions, public parks, libraries, or trans portation hubs. Niantic also mentions locations that are ineligible to be PokeStops or portals include but are not limited to schools, private properties, temporary and mobile locations, cemeteries, indoors, generic business locations, and natural landscapes. Based on the above official selection criteria, restaurant owners can hardly turn their business lo cations into PokeStops and cannot intervene in the treatment conditions in our research setting. Thus the locations of PokeStops are completely exogenous in the current research, and the endogeneity concern about PokeStops’ selection is ruled out.

## 6.2. Falsification test through reverse regression

To validate the DID estimation results, to formally remove the reversal causality concerns, and to invalidate the claim that online reputation metrics of businesses presiding in that location determine the presence of PokeStop in that area, we first perform the following reverse regression by regressing reputation metrics back on the DID indicators:

$$
D I D _ {i, t} = \gamma_ {0} ^ {V} + \gamma_ {1} ^ {V} \text { Volume } _ {i, t} + \gamma_ {2} ^ {V} R _ {i} + \Psi^ {V} X _ {i, t} + \varepsilon_ {i, t} ^ {V}\tag{9}
$$

$$
D I D _ {i, t} = \gamma_ {0} ^ {R} + \gamma_ {1} ^ {R} R a t i n g _ {i, t} + \gamma_ {2} ^ {R} R _ {i} + \Psi^ {R} X _ {i, t} + \varepsilon_ {i, t} ^ {R}\tag{10}
$$

where $D I D = P K G _ { i } * d _ { t }$

Next, we incorporate the first-order lag term of online reputation metrics Volume $t { - } 1$ and Rating in the above regressions. The results, summarized in Tables 10 and 11, show that neither the reputation metrics nor their lag terms are significantly associated with the DID effects. Thus, the results support that online reputation metrics do not reversely predict restaurants’ treatment conditions, or the DID effects. The reversal causality concern is ruled out.

## 6.3. Confounding check

## • Yelp Filter

Another potential threat might be caused by Yelp’s promoting action—the launch of the "PokeStop nearby" filter after Pokemon GO’s

p < 0.05.

Table 12  
Regression discontinuity regression results.

<table><tr><td></td><td>Review volume</td><td>Review rating</td></tr><tr><td> $I(Distance_{i} \leq c)$ </td><td>0.419 *** (0.134)</td><td>0.048** (0.027)</td></tr><tr><td> $Distance_{i} \leq c$ </td><td>0.017* (0.010)</td><td>0.014** (0.007)</td></tr><tr><td> $(Distance_{i} \leq c) * I(Distance_{i} \leq c)$ </td><td>0.077 (0.067)</td><td>0.046 (0.076)</td></tr><tr><td>Price level $</td><td>-0.379** (0.193)</td><td>0.052 (0.067)</td></tr><tr><td>Price level $$</td><td>-0.352* (0.189)</td><td>0.087 (0.067)</td></tr><tr><td>Price level $$$</td><td>0.395** (0.219)</td><td>0.097 (0.070)</td></tr><tr><td>Competition</td><td>0.025 (0.026)</td><td>-0.012 (0.017)</td></tr><tr><td>Density</td><td>0.062 (0.044)</td><td>0.026 (0.019)</td></tr><tr><td>Game Download</td><td>0.137* (0.083)</td><td>0.020 (0.031)</td></tr><tr><td>Chain</td><td>-0.075 (0.05)</td><td>-0.022** (0.012)</td></tr><tr><td>Google trend</td><td>0.002* (0.001)</td><td>0.002* (0.001)</td></tr><tr><td>Entity level VCE cluster</td><td>Yes</td><td>Yes</td></tr></table>

Note: Standard errors in parentheses.  
p < 0.1.

$$
p <   0. 0 1.
$$

official launch. This potential confounding effect might affect the Yelp reviews of those restaurants that are close to PokeStops. If Yelp’s action influences the treatment group significantly, the DID estimation could be upwards biased. In order to examine and eliminate the confounding threat to our estimation results, we consider the launch of the Yelp filter as the treatment switch and operate the DID estimation on the reputa tion metrics. More specifically, through weekly data after the same propensity score matching process, we examine the changes of review volume and review rating before and after the launch of Yelp’s filter between restaurants with PokeStops nearby with those without Poke Stops nearby. Yelp.com launched the "PokeStop nearby" filter and pos ted an announcement on their official blog on July 15, 2016. Thus, we choose the third week of July as the switch time. We consider the first

Table 13  
Summary of weekly estimation results (Restaurant cuisines factor, city location dummy, and holiday dummy are included).

<table><tr><td>Reputation metrics</td><td>Short-term</td><td>Long-term</td></tr><tr><td>Volume</td><td>0.030** (0.012)</td><td>0.020 (0.02)</td></tr><tr><td>Rating</td><td>0.022*** (0.006)</td><td>0.115*** (0.019)</td></tr></table>

Note: DD Coef. Standard errors in parentheses.

$$
p <   0. 0 5.
$$

$$
p <   0. 0 1.
$$

coefficient of review volume is 0.44 (Std. Err. = 0.331, $\pmb { p = 0 . 1 8 4 } )$ and the coefficient of rating is 0.019 (Std. Err. = 0.054, p = 0.725). Both DID coefficients are non-significant. Therefore, our results are free of the potential effect due to the summer seasonal influence, and our estima tion is unbiased.

## 6.4. Control group validation through regression discontinuity

We have used the Yelp filter to assign restaurants into the treated and control groups in our previous analyses. To justify the validity of the control group, we adopt the Regression Discontinuity (RD) design and use the geo-distance between restaurants and the nearest PokeStop as the forcing variable. According to Anderson and Magruder [2], the cutoff value c is determined by the intersection of kernel density dis tance distributions of filtered treated and control groups as:

where $I ( D i s t a n c e _ { i } \leq c )$ is an indicator function, which equals 1, sug gesting that restaurant i is determined as a treatment entity when Distance ≤ c; and equals 0 (restaurant i as a control entity) otherwise.

$$
\text { Volume } _ {i, t} = \alpha_ {0} ^ {V} + \beta^ {V} * I (\text { Distance } _ {i} \leq c) + \alpha_ {1} ^ {V} * (c - \text { Distance } _ {i}) + \alpha_ {2} ^ {V} * (c - \text { Distance } _ {i}) * I (\text { Distance } _ {i} \geq c) + \Theta^ {V} R _ {i} + \Psi^ {V} X _ {i, t}\tag{11}
$$

$$
\text { Volume } _ {i, t} = \alpha_ {0} ^ {R} + \beta^ {R} * I (\text { Distance } _ {i} \leq c) + \alpha_ {1} ^ {R} * (c - \text { Distance } _ {i}) + \alpha_ {2} ^ {R} * (c - \text { Distance } _ {i}) * I (\text { Distance } _ {i} \geq c) + \Theta^ {V} R _ {i} + \Psi^ {V} X _ {i, t}\tag{12}
$$

two weeks of July as the pre-period and the second two weeks as the post-period. The DID coefficient of review volume is 0.063 (Std. Err. = $0 . 1 2 9 , p = 0 . 6 2 5 )$ and the coefficient of rating is 0.003 (Std. Err. = 0.067, $\pmb { p = 0 . 9 6 4 } )$ . Both DID coefficients given by Yelp’s reaction after Pokemon GO’s launch are non-significant. Therefore, our results are free of the potential effect due to the launch of the Yelp filter.

## • Seasonal Influence

Another threat might be caused by seasonal influence such that during summer time (May to September), people might be more likely to do outdoor activities, which could inflate the DID effects. To examine and eliminate the confounding threat to our estimation results, we consider the summer months as the switch time and operate the DID estimation on the reputation metrics. More specifically, through monthly data after the same propensity score matching process, we examine the changes of review volume and review rating before and after summertime (March to September) between restaurants with PokeStops nearby with those without PokeStops nearby. The DID

The indicator function intervenes in the discontinuity in each dependent variable. The coefficien $\boldsymbol { \beta } ^ { V }$ or $\beta ^ { R }$ estimates the causal effect of having a PokeStop nearby, or more specifically, having a shorter "distance to the nearest PokeStop" than the cutoff. As suggested by Li [22], we include vectors of restaurant characteristics and macro-level control covariates, including (Density, Competition , PriceLevel , Chain , GameDownloads , GoogleTrend ). The RD regression results are reported in Table 12.

The results show that being close to a PokeStop can significantly improve the restaurant’s review volume and rating by 41.9% $( p < 0 . 0 1 )$ and 4.8% $( p < 0 . 0 5 )$ , respectively. These results are consistent with our DID estimation. Since the design of RD can guarantee local randomi zation of the treated and control restaurants near the cutoff line, the consistent results verify the control validity in the previous DID and DDD analyses.

## 6.5. Validation through a weekly frequency

For robustness, we also validate our DID estimation results at a different time frequency, i.e., on a weekly level. Because holidays may confound the estimation results, we incorporate the time fixed effect and a holiday dummy<sup>17</sup> in the weekly data DID estimation on both review volume and rating. The primary results are reported in Table 13, and the full results are in Appendix A.

The results are consistent with our previous results based on monthly data in Table 3. More specifically, after the entry of Pokemon GO, the review volume and rating of the treated restaurants increase by 2.1% (p < 0.01) and 3% $( p < 0 . 0 1 )$ , respectively in the short term. The long-term review rating increases by 11.9% (p < 0.01) and the review volume does not show a significant increase in the long term.

## 7. Implications

## 7.1. Theoretical implications

The theoretical assessments and empirical findings in this paper advance our understanding of the business impacts of AR, LB, and LBAR technologies. Through surveys and interviews, current AR literature [5, 34] conceptually reasoned how the adoption and use of AR technologie can improve users’ perceived emotional gratification and brand awareness, favorability, and consideration, and can improve customers entire experience throughout the purchase stages. However, in addition to user self-reported intentions and perceptions, very few studies have examined the impacts of AR on users and businesses through directly measuring users’ brand evaluations as empirical evidence. In this sense, our study is pioneer research to examine the business impacts of AR technologies by providing direct, rich, and detailed empirical evidence to its positive influence on users' brand evaluation in terms of review valence. We find that the LBAR app can improve users’ ratings of local restaurants. That is, the virtual content generated by the LBAR app can add value to users’ experiences at a business, which is discovered through the app or while using it. Moreover, our research extends the AR marketing studies by examining the spillover effect of AR applications on consumers’ evaluations of local businesses. Our finding uncovers the potential business value and positive externality of the LBAR app to local businesses.

LB literature studied how LB technologies impact users’ daily ac tivities; however, very few studies focus on the potential impacts of LB apps on local businesses. Moreover, most LB literature only focuses on firms’ applying the LB technologies for their own marketing purposes, but did not study the unintended and indirect benefits of the individual use of LB apps on neighboring businesses. To meet these two research gaps, we validate the LB technologies’ effectiveness in improving local businesses through the following perspectives:

First, we examine the LB applications’ spillover effect on locationrelated businesses and find that the entry of the LBAR app benefits restaurants near the physical app portals by improving their online reputation in both the short and long terms. We explain the LBAR’s spillover effect on review volume through a spillover mechanism: the LBAR app can increase users’ awareness of surrounding businesses by encouraging movement and visits to new locations and lingering be haviors, which can result in new foot traffic and potential business op portunities to nearby restaurants as well as new dining experiences to the users. Hence, the LBAR app can increase users’ likelihood of visiting nearby businesses, and in turn, post reviews on social media.

Second, to understand and explain the inconsistency between LB literature and practical cases as well as the mixed findings from industry reports ([16] and [48]) regarding the LB technologies’ proximity mar keting efficiency, we investigate the internalization of the spillover ef fect for heterogeneous restaurants. Through a series of empirical analyses, our study reveals the internalization of the LBAR app’s spill over effect on restaurants based on different factors (e.g., restaurant agglomeration level in vicinity area, Google trend, and the chain/non-chain feature of restaurants). Specifically, we show the spillover effect of the LBAR app on a restaurant is strengthened when it is surrounded by an agglomeration of restaurants and diminishes with the geographical distance from the portals at an increasing rate. Addi tionally, treated local businesses that are not affiliated with a chain group will benefit more from the entry of the LBAR app.

At last, based on the quantitative effects of the LBAR app on reviews of businesses near app portals, we can estimate the economic impact of the spillover effect on local businesses due to the LBAR app, which provides unique contributions to the LBAR literature on the business applications and values of the LBAR apps.

To sum up, our findings provide new evidence and tangible measure of the economic value of LBAR technologies, which extend the current LB and LBAR literature.

## 7.2. Managerial implications for local businesses

Our findings suggest that PokeStop nearby can be considered as an attraction to users and validated as a positive feature of restaurants. In addition to the empirical results from our previous formal analyses (Sections 4–6), we also conduct text analyses of the Yelp reviews for more direct evidence. By parsing the review texts of the restaurants, we find that reviews with the keywords "Pokemon" or "PokeStops" have a higher proportion in 4 and 5-star ratings (Appendix B).

Moreover, our findings show that the entry of this application can generally improve the online ratings of local businesses in both the long and short terms. As shown in Section 4.2. we estimate that the entry of Pokemon GO results in around a 1.96% increase in the monthly revenue of a PokeStop nearby restaurant in the short term, and a 2.75% incre ment in the long term. Thus those local business owners have the incentive of paying to become or be close to a PokeStop, which also creates a monetizing opportunity for the app developers. Thus, we suggest that the app developer open its platform to local businesses as sponsors for mutual benefits. Not until December 2019, almost three years after our research period, did Niantic officially launched a spon sorship program and opened it to local small businesses<sup>18</sup>. The spon sorship cost is US\$30 or US\$60 per month per stop for the basic and premium levels, respectively. Local businesses can use our estimated economic benefits or apply our model to their scenarios to directly compare the benefit and cost of participating in the sponsorship program from Niantic or other LBAR developers in the future.

Our findings also suggest that the spillover benefits of location-based mobile applications cannot benefit all businesses equally. Instead, the findings suggest that locations and other characteristics affect the spillover effect of LBAR apps. There demonstrate strong distance and agglomeration effects; that is, businesses located closer to PokeStops, or stores surrounded by a large number of competitors benefit more from the entry of Pokemon GO. Our results also show that non-chain res taurants are more positively associated with the spillover effect on on line reputation metrics.

## 7.3. Managerial implications for app developer

Our study has demonstrated the pronounced econometric signifi cance of traffic and business opportunities brought by PokeStops during the time frame of this research. However, Niantic could not start working with some big-chains and marketing sponsored locations (aka "branded PokeStops") in the United States until early 2017, when Pokemon GO’s second generation was released. Till now, only Sprint and Starbucks but no individual small businesses successfully sponsored to become new PokeStops. Our study shows that Pokemon GO can generally improve restaurants’ online reputation and especially for non chain restaurants. Individual small local businesses have a higher motive to become PokeStops through sponsorship and to cooperate with Niantic. Though now Niantic has not adopted any form of monetization, in an interview by Brazil Globo<sup>19</sup>, Niantic’s strategic VP is considering a cost-per-visit model by charging business partners at certain locations US\$0.5 per visitor attracted by the game. A total of 89% of the restau rants in our full sample are non-chain (independent) restaurants. Ac cording to our analysis, around 70% of these non-chain restaurants benefit from the entry of Pokemon GO. If the developer cooperates with small non-chain businesses as well. the shared revenue for Niantic will be substantial. Therefore, we recommend Niantic to further open the PokeStops application and work with more diversified and heteroge neous restaurants rather than limiting the sponsorship program only to big chains. Echoing our recommendation based on the analyses with the data of three years ago, Niantic opened its sponsorship program to local small businesses in December 2019<sup>20</sup>.

![](/api/attachments/3P3JBJG7/fulltext/images/f3af478c1121c2063dbe0f59f102f88e9a987f2f82e87bf6d19eea97e9f5f64b.jpg)  
Figure B1. a. Positive Review Sample, b. Negative Review Sample.

## 8. Conclusion

This paper validates and extends the AR and LB literature in the marketing and IS fields. We provide a comprehensive empirical analysis regarding the spillover effect of LBAR application on local businesses. Pokemon GO, as the most successful LBAR mobile application, indeed provides positive externality to local businesses, especially to those that are closer to app portals, in high agglomeration geo-locations or nonchain restaurants. There are two directions for future studies. First, if sales or traffic data are available, LBAR apps’ direct impact on local businesses can be examined. Second, more LBAR apps have also been launched. Future studies can continuously collect more data to verify whether and how LBAR technological convergence mobile apps and local business would influence each other as an ecosystem in a longer time frame.

## Author statement

We would like to submit the enclosed manuscript, “Catch Them All: Impacts of Location-Based Augmented Reality Mobile Applications on Local Businesses,” for consideration of publication as a research article in Information & Management. The nominees for reviewers have no conflict of interest with any of the authors of the paper being submitted. The authors declare that they have no known competing financial in terests or personal relationships that could have appeared to influence the work reported in this paper. This paper (or closely related research) has not been published or accepted for publication. It is not under consideration at another journal either.

![](/api/attachments/3P3JBJG7/fulltext/images/6daf1bc6b80a9ce32e12df153ea88c5e430bf0d9fed0575dc82a433c910ec7d0.jpg)

![](/api/attachments/3P3JBJG7/fulltext/images/96f2f6a50b14e62a99edeecd6de63288501b7b5861041dcb3f04a5530fc1611a.jpg)  
Figure B2. a. With Pokemon GO Related Keywords, b. Without Pokemon GO Related Keywords.

Please feel free to contact me if you have any questions regarding this submission. Thank you very much for your consideration.

Yuan Zhang

David D. Reh School of Business Clarkson University Jie Zhang College of Business Administration University of Texas at Arlington

## Appendix A. The Full DID Estimation Based on Weekly Data

Table A. The Full DID Estimation Results Based on Weekly Data (Restaurant cuisines factor city location dummy are included)

<table><tr><td>Variable(s)</td><td>Review Volume Short-term</td><td>Long-term</td><td>Review Rating Short-term</td><td>Long-term</td></tr><tr><td>Diff-in-Diff</td><td>0.030** (0.012)</td><td>0.020 (0.02)</td><td>0.022*** (0.006)</td><td>0.115*** (0.019)</td></tr><tr><td>p1</td><td>-0.082*** (0.014)</td><td>-0.035 (0.023)</td><td>-0.004 (0.007)</td><td>0.002 (0.01)</td></tr><tr><td>p2</td><td>-0.029** (0.013)</td><td>-0.018 (0.023)</td><td>-0.002 (0.006)</td><td>-0.009 (0.01)</td></tr><tr><td>p3</td><td>0.081*** (0.028)</td><td>0.116** (0.049)</td><td>0.029* (0.015)</td><td>0.014 (0.021)</td></tr><tr><td>Competition</td><td>0.003*** (0.001)</td><td>0.010*** (0.004)</td><td>0.001 (0.001)</td><td>0.002 (0.002)</td></tr><tr><td>Density</td><td>0.018* (0.010)</td><td>0.011* (0.006)</td><td>0.003 (0.002)</td><td>0.001 (0.003)</td></tr><tr><td>Distance</td><td>-0.003*** (0.001)</td><td>-0.021*** (0.008)</td><td>-0.001 (0.001)</td><td>-0.005*** (0.002)</td></tr><tr><td>Game Download</td><td>0.001 (0.001)</td><td>0.002*** (0.001)</td><td>0.002* (0.001)</td><td>0.002** (0.001)</td></tr><tr><td>Chain</td><td>-0.009*** (0.005)</td><td>-0.023 (0.009)</td><td>-0.004 (0.003)</td><td>-0.022*** (0.004)</td></tr><tr><td>Google Trend</td><td>0.001 (0.001)</td><td>0.001 (0.001)</td><td>0.002* (0.001)</td><td>0.004** (0.001)</td></tr><tr><td>R-square</td><td>0.49</td><td>0.63</td><td>0.69</td><td>0.69</td></tr></table>

Note: Standard errors in parentheses.  
\*p < 0.1.  
\*\*p < 0.05.  
\*\*\*p < 0.01.

## Appendix B. Validation from Customer Perceptive, Text Analyses of Yelp Reviews

To further explore how Pokemon GO affects restaurants' online reputation, we run a text analysis in this session. We parse all review texts with the keywords “Pokemon” or “PokeStop” between July and August 2016 along with individual rating and customers’ information on Yelp. There are 40 reviews (0.278% of all reviews) from these two months in our sample, using “Pokemon GO” as a keyword. Thirty-eight of them are from the treatment group– restaurants with PokeStops nearby and two reviews are from the control group - restaurants without PokeStops nearby, In July, in the treatment group, the frequency of “Pokemon” is 19, and the frequency of “PokeStop” is 11. In August, in the treatment group, the frequency of “Pokemon” is 13, and the frequency of “PokeStop” is 9. In July, in the control group, the frequency of “Pokemon” is one, and the frequency of “PokeStop” is 1. In August, in the control group, the frequency of “Pokemon” is 0, and the frequency of “PokeStop” is 0.

We manually read each of the identified reviews and found that most of these reviews were about sharing information related to Pokemon species or PokeStops in nearby areas. From a customer’s perspective, review texts show three patterns regarding Pokemon GO’s impact on restaurants’ online reputations.

First, PokeStops can draw the players’ attention and lead players to visit nearby restaurants. Few yelpers point out that for restaurants that serve similar cuisine, those with PokeStops nearby will be highly preferred.

Second, for the yelpers who play Pokemon GO, having PokeStops nearby is shown as a positive attribute to them (an example in Fig. B1a), and these yelpers usually leave higher ratings and sentiment scores. Besides being stated as an experience enhancement, being close to PokeStops or being inhabited by rare Pokemon also improves customers’ experiences and utilities while waiting for seats or services and prevents negative emotions during waiting.

Third, ways of how restaurant owners take advantage of the game and restaurant’s attitudes to players affect customer ratings and sentiments. Several of the restaurants provide Pokemon GO-related check-in promotional offers or special menus, and customers leave feedbacks on Yelp regarding their dinging and playing experience. For customers, given average food and service quality, Pokemon GO is considered a plus for “not-bad” restaurants. However, there are also negative reviews (an example in Fig. B1 b) with low-rating in texts in the parsed texts. Few owners might consider Pokemon GO an annoying fad. Nevertheless, restaurant managers and servers’ bad manners and attitudes to customers who love Pokemon GO could hurt customers’ feelings and restaurants’ online reputation.

Meanwhile, we observe no text that shows a crowded atmosphere due to the Pokemon GO heat decreases yelper’s rating and sentiment, either. In Fig. B2 a, we have an overall view of the different rating proportions of parsed Pokemon GO-related texts. Generally, the impact of Pokemon GO on yelpers’ attitudes to restaurants is positive, and as we expect in the previous session, Pokemon GO is verified to be an attractive feature to restaurants. Accordingly, we parse the texts of reviews without keywords like “Pokemon GO” and “PokeStop” and summarizing their rating distribution in the pie chart Fig. B2 b. By comparing the two figures, we observe an evident difference between the two text samples’ rating distribution. The 5-point rating proportion of the sample without keywords is 18% less than that of the sample with keywords. The 1-point, 2-point, and 3-point rating proportions of the sample without keywords are larger than their counterparts of the sample with keywords by 5%, 8%, and 7%, respectively. The 4-point rating proportion of the sample without keywords is slightly lower than that of the sample with keywords.

Figure B2. The contrast of Rating Distributions of Reviews with and without Pokemon GO Related Keywords

Further, we compare the means of two samples. The mean rating of the sample with Pokemon GO-related keywords is significantly higher (p = 0.035) than that of the sample without those keywords. This salient difference further validates our expectation that Pokemon GO is an attractive feature for both restaurants and customers by enhancing restaurant differentiation and improving customers’ dining experience and perceived quality.

## References

[1] M. Andrews, X. Luo, Z. Fang, A. Ghose, Mobile ad effectiveness: hyper-contextual targeting with crowdedness, Mark. Sci. 35 (2) (2016) 218–233.

[2] M. Anderson, J. Magruder, Learning from the crowd: Regression discontinuity estimates of the effects of an online review database, Econ. J. 122 (563) (2012) 957-989.

[3] D.H. Autor, Outsourcing at will: the contribution of unjust dismissal doctrine to the growth of employment outsourcing, J. Labor Econ. 21 (1) (2003) 1–42.

[4] L. Bigham, Experiential marketing, New Consumer Research, Jack Morton Worldwide New York 2005

[5] M. Bulearca, D. Tamarjan, Augmented reality: a sustainable marketing tool, Glob. Bus. Manag. Res. 2 (2010) 237–252.

[6] M. Caliendo, S. Kopeinig, Some practical guidance for the implementation of propensity score matching, J. Econ. Surv. 22 (1) (2008) 31–72.

[7] J. Chan, A. Ghose, R. Seamans, The internet and hate crime: offline spillovers from online access, MIS Q. 40 (2) (2016) 381–403.

[8] W. Chen, B. Gu, Q. Ye, K.X. Zhu, Measuring and managing the externality of managerial responses to online customer reviews, Inf. Syst. Res. 30 (1) (2019) 81–96.

[9] K. Cousins. U. Varshney. A product location framework for mobile commerce environment. in: ACM. 2001, pp. 43–48

[10] A. Colley, J. Thebault-Spieker, A. Lin, D. Degraen, B. Fischman, J. Hakkil¨ ¨a, K. Kuehl, V. Nisi, N.J. Nunes, N. Wenig, D. Wenig, B. Hecht, J. Schoning, ¨ The geography of Pokemon GO: beneficial and problematic effects on places and movement, in: ACM, 2017, pp. 1179–1192.

[111 A.B. Craig. Understanding augmented reality: Concepts and applications. Newnes (2013).

[12] W. Duan, B. Gu, A.B. Whinston, The dynamics of online word-of-mouth and product sales—An empirical investigation of the movie industry, J. Retail. 84 (2) (2008) 233–242.

[13] W. Fulton, Pok´emon GO is going to make restaurants and bars tons of money, Thrillist (2016).

[14] Z. Fang, B. Gu, X. Luo, Y. Xu, Contemporaneous and delayed sales impact of location-based mobile promotions, Inf. Syst. Res, 26 (3) (2015) 552–564.

[15] A. Friedenthal. How Pokémon GO and augmented reality marketing can drive vour sales, Softw. Adv. (2016).

[16] W. Filloon, How restaurants are dealing with Pok´emon GO Mania, Eater (2016)

[17] Q. Gao, M. Lin, D.J. Wu, More than just money: educational impact of online charitable crowdfunding, Inf. Syst. Res. 32 (1) (2021) 53–71.

[18] J. Gong, B.N. Greenwood, Y. Song, Uber might buy me a Mercedes Benz: an empirical investigation of the sharing economy and durable goods purchase, Available at, SSRN 2971072 (2017).

[19] G.W. Imbens, J.M. Wooldridge, Recent developments in the econometrics of program evaluation, J. Econ. Lit. 47 (1) (2009) 5–86.

[20] N. Kunkel, S. Soechtig, J. Miniman, C. Stauch, Augmented and virtual reality go to work: seeing business through a different lens. Tech. Trends (2016).

[21] X. Li. Could deal promotion improve merchants’ online reputations? The moderating role of prior reviews, J. Manag. Inf, Syst, 33 (1) (2016) 171–201

[22] X. Li, Impact of average rating on social media endorsement: The moderating role of rating dispersion and discount threshold Inf, Syst, Res, 29 (3) (2018) 739–754

[23] A.X. Liu, J.-B.EM Steenkamp, J. Zhang, Agglomeration as a driver of the volume of electronic word of mouth in the restaurant industry, J. Mark. Res. 55 (4) (2018) 507–523.

[24] Q. Liu, Y. Lu, Firm investment and exporting: evidence from China’s value-added tax reform, J. Int. Econ. 97 (2) (2015) 392–403.

[25] Y. Liu, Z. Jiang, H.C. Chan, Touching products virtually: facilitating consumer mental imagery with gesture control and visual presentation, J. Manag. Inf. Syst. 36 (3) (2019) 823–854.

[26] Y. Lu, Z. Tao, L. Zhu, Identifying FDI spillovers, J. Int. Econ. 107 (2017) 75–90

[27] M Luca, Reviews, reputation, and revenue: the case of Yelp.com. Working paper, Harvard Business School, 2016

[28] X. Luo, J. Zhang, W. Duan, Social media and firm equity value, Inf. Syst. Res. 24 (1)

[29] W W. Moe, D.A. Schweidel. Online product opinions: Incidence, evaluation, and evolution, Mark, Sci, 31 (3) (2012) 372–386.

[30] C. Peukert, J. Pfeiffer, M. Meißner, T. Pfeiffer, C. Weinhardt, Shopping in virtual reality stores: The influence of immersion on system adoption, J. Manage. Inf. Syst. 36 (3) (2019) 755–788

[31] J.-S. Pischke, Labor market institutions, wages, and investment: review and implications, CESifo Econ. Stud. 51 (1) (2005) 47–75.

[32] L. Qiu, Z. Shi, A.B. Whinston, Learning from your friends’ check-ins: an empirical study of location-based social networks, Inf. Syst. Res. 29 (4) (2018) 1044–1061.

[33] P.A. Rauschnabel, A. Rossmann, M. Claudia tom Dieck, An adoption framework for mobile augmented reality games: the case of Pok´emon Go, Comput. Hum. Behav. 76 (2017) 276–286.

[34] P.A. Rauschnabel. R. Felix. C. Hinsch. Augmented reality marketing: how mobile AR-apps can improve brands through inspiration. J. Retail. Consum. Sery. 49 (2019) 43–53.

[35] R. Rishika, A. Kumar. R. Janakiraman, R. Bezawada, The effect of customers' social media participation on customer visit frequency and profitability: an empirica investigation, Inf. Syst. Res. 24 (1) (2013) 108–127.

[36] J.L, Schafer, Multiple imputations: a primer, Stat, Methods Med, Res, 8 (1) (1999 3–15.

[37] J.A. Smith, P.E. Todd, Does matching overcome Lalonde’s critique of nonexperimental estimators? J. Econom. 125 (1-2) (2005) 305–353.

[38] A.M. Susskind, E.K. Chan, How restaurant features affect check averages: a study of the toronto restaurant market, Cornell Hotel Restaur. Adm. Q. 41 (6) (2000) 56-63.

[39] J.H. Steffen, E.G. James, O.M. Thomas, L.J. Jeffrey, I. Wolman, Framework of affordances for virtual reality and augmented reality, J. Manage. Inf. Syst. 36 (3) (2019) 683–729.

[40] C. Ververidis, G. Polyzos, Mobile marketing using a location based service, in: Proceedings of the First International Conference on Mobile Business, Athens, Greece, 2002, pp. 1–12.

[41] Z. Xiang, Q. Du, Y. Ma, W. Fan, A comparative analysis of major online review platforms: Implications for social media analytics in hospitality and tourism, Tourism Manage, 58 (2017) 51–65

[42] K.L. Xie, Z. Zhang, Z. Zhang, The business value of online consumer reviews and management response to hotel performance, Int. J. Hosp. Manag. 43 (2014) 1–12.

[43] K. Xu, J. Chan, A. Ghose, S.P. Han, Battle of the channels: The impact of tablets on

[44] S. Yang, G. Xiong, Try It On! contingency effects of virtual fitting rooms, J. Manag. Inf, Syst, 36 (3) (2019) 789–822.

[45] N.S. Yegiyan, Explicating the emotion spillover effect, J. Media Psychol. 27 (3) (2015).134–145

## Y. Zhang and J. Zhang

[46] Y.-H. Yuan, Erin, and Chihkang “Kenny Wu. "Relationships among experiential marketing, experiential value, and customer satisfaction, J. Hosp. Tourism Res. 32 (3) (2008) 387–410.

[47] F.J. Zach, I.P. Tussyadiah, To catch them all—the (un)intended consequences of Pokemon go on mobility, consumption, and wellbeing. Information and Communication Technologies in Tourism 2017, Springer, Cham, 2017, p. 21.

[48] Y. Zhu, 5 Brilliant Ways Restaurants are using Pok´emon GO to Level Up Sales, Forbes, 2016.

Yuan Zhang is an Assistant professor at the David D. Reh School of Business at Clarkson University. She received her Ph. D in MIS from the University of Texas at Arlington in Spring 2020. Her research interests include user-generated-contents, augmented and vir tual reality, live streaming platforms and social media, video games, and blockchain. He works have been accepted and published by peer-reviewed conferences, including CIST, HICSS, POMS, WISE, and others.

Jie Zhang is currently Daniel Himarios Endowed Chair Professor of Information Systems in the College of Business at the University of Texas at Arlington. She received her Ph.D. ir computer information systems from the University of Rochester. She employs analytical and empirical techniques to closely examine issues in advanced and business applications of information technologies, for example, trend and business impacts of social media, web advertising, consumer online behaviors, online channel selection and pricing strategies, software licensing policies, and business alliances. Her research appears in MIS Quarterly, Journal of Economics and Management Strategies, Information Systems Research, Journal of Management Information Systems, Decision Support Systems, among others. She has received grants and awards recognizing her research impacts.
