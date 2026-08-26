---
otero_id: 12560
otero_key: "9DXJWFDR"
title: "Personalized local internet in the location-based mobile web search"
authors: "Dae-Young Choi"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Personalized local internet in the location-based mobile web search

Dae-Young Choi

Department of MIS, Yuhan College, Koean-dong, Sosa-ku, Puchon City, Kyongki-do, 422-749, South Korea

Available online 28 June 2005

## Abstract

In this paper, a new ubiquitous-GPS-Web-enabled mobile search mechanism is proposed. It is based on user’s physical location, distance from user’s physical location and user’s search intentions (i.e., keywords, preferences). The concept of perception index (PI) is used to handle fuzzy query in the ubiquitous-GPS-Web-enabled mobile search. Using fuzzy query, together with user’s physical location and distance from user’s physical location, the ubiquitous-GPS-Web-enabled mobile devices can receive more personalized and locally targeted search results. The proposed approach can be applied to enhance the power of mobile Web search. Consequently, it gives a mobile user the personalized local angle to make searching for local businesses on the Web, and contributes to a significant convenience in the location-based mobile Web searching (i.e., local Internet).

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Location-based mobile web search; Ubiquitous-GPS-web-enabled mobile search mechanism; Perception index; Fuzzy query; Personalized local internet

## 1. Introduction

In 1991, Mark Weiser described that ubiquitous computing (or pervasive computing) is the process of removing the computer out of user awareness and seamlessly integrating it into everyday life [25]. And recently, the rapid development of mobile devices, wireless technologies and low-cost, low-power multifunctional sensor nodes has enabled the realization of ubiquitous computing environments, which consist of numerous wearable, handheld, and embedded devices that work together to transform physical spaces into smart and interactive environments. Ubiquitous computing enhances the computing and communication capabilities of human by integrating embedded computers with various environments and daily lives. Thus, it makes computing and communication essentially autonomous and transparent to the users. In the ubiquitous computing environment, small ubiquitous chips are embedded into all sorts of things such as mobile phones, digital cameras, medicine bottles and so on. They communicate and cooperate with each other to control our living environment or to provide rich information services to us. The computer automatically recognizes the condition of the real world, and conducts various information processing and operation according to the condition. For example, if we attach an ultra small tag to a medicine bottle and move two bottles closely, they exchange information one another. If the combination of these medicines is not good, they automatically recognize this inadequate condition [19–21]. Mobile computing just has reactive context responding to discrete events, thus cannot make timely, context-sensitive decisions. In the meantime, ubiquitous computing requires systems and devices that perceive context in a proactive manner. Context awareness (or context sensitivity) is an application software system’s ability to sense and analyze context from various sources. It lets application software take different actions adaptively in different contexts [29]. Schilit [22] defines context awareness by categorizing context-aware applications as follows: (1) Proximate selection—a user interface technique where the objects located nearby are emphasized or otherwise made easier to choose. (2) Automatic contextual reconfiguration—a process of adding new components, removing existing components or altering the connections between components due to contexts changes. (3) Contextual information and commands—it can produce different results according to the context in which they are issued. (4) Context-triggered actions—simple IF–THEN rules used to specify how context-aware systems should be adapted. In a mobile distributed computing system, contexts are the location of the user, the identity of people and physical objects that are nearby the user, and the states of devices that the user interact with [22]. In this paper, we assume that an embedded ubiquitous chip in a ubiquitous-GPS-Webenabled mobile device deliver reminders when users are within a specified area, and these reminders are processed in a location-detection module in the ubiquitous-GPS-Web-enabled Web-severs. As a result, by using the embedded ubiquitous chips in mobile devices and Web-servers, location-triggered communication channels are established between clients (or mobile users) and the ubiquitous-GPS-Web-enabled Web-servers within a specified area. In this respect, we can achieve the proximate selection, and automatic location-based reconfiguration that a process of adding new components, removing existing components or altering the connections between components due to mobile user’s location changes, between mobile users and the ubiquitous-GPS-Web-enabled Web-servers within a specified area.

GPS [1,2,8,9,15,18,24], which stands for Global Positioning System, is able to show a user his/her exact position on the earth anytime, anywhere. GPS satellites, 24 in all, orbit at 11,000 nautical miles above the earth. The satellites transmit signals that can be detected by anyone with a GPS receiver. Using the receiver, a user can determine his/her location with great precision [37–41].

Mobile device is a small, portable computer that allows a user to store, organize, and access information. Mobile devices can include cell phones, Web phones, pagers, two-way pagers, PDAs (personal digital assistants), and Internet appliances. These mobile devices allow a user to communicate with others and get information anywhere, anytime by means of GPS, wireless telecommunication network (WTN), wireless sensor network (WSN), wireless modem, etc. Wireless technology converts e-business into mobile business (M-commerce). M-commerce can be defined as any transaction with a monetary value–either direct or indirect–that is conducted over a wireless telecommunication network. This will contribute to a significant growth in total global e-commerce revenue [4]. It allows one to connect to the Internet at any time from virtually any place and this can be used to conduct online transactions, market purchase, trade stocks, send e-mail, etc. Experts predict that the mobile device market will have 1.3 billion users and be worth an estimated by \$20 billion by 2005 [42]. As Internet-enabled mobile phones become available, the base of M-commerce customers will grow [23]. Mcommerce will result in increased convenience for customers. Wireless applications for sales and service professionals provide one of the largest opportunities for e-business.

The Web is an impressive success story in terms of both its available information and the growth rate of human users. It now penetrates most areas of our lives, and its success is based on its simplicity. Unfortunately, this simplicity could hamper further Web development [7]. Often, search engines will return too many results, but most will be uninteresting to the user. If a search tool can get geographical information or learn preferences or contexts from the user, this information can be used to improve the search or document-ranking process. For example, SuperPages (http://www.SuperPages.com) can help users to find <sup>d</sup>Italian restaurants within 1 mile radius from a specific address’ (U.S. yellow pages services). More specifically, if a user supply a search category, and

zip code or both a city and a state as part of user’s starting address, SuperPages gives a user search results by distance. Now, SuperPages provides wire less phone service and it brings online yellow pages on the road. In a similar sense, the <sup>d</sup>geo-targeting feature in new Inktomi Web Search 9 allows custo mers to select specific global regions they want to target [43]. These location-based searches are pro cessed based on crisp query with keywords. For ex ample, local search by keywords <sup>d</sup>Italian restaurants<sup>T</sup>, <sup>d</sup>1 mile<sup>T</sup>, <sup>d</sup>a specific address<sup>T</sup>. In February 2003, new technology was introduced to help businesses feed data on their physical location to Web search engines [44]. That data is stored in a tag on the business Web site and contains Geographic Information Systems (GIS) data such as the location’s latitude and longi tude. Search engines with their feelers out for regional data on Web pages can pick it up and deliver query results related to Web surfers’ location. In this ap proach, Web surfers’ location becomes part of the relevance of the query. For example, if a traveler is visiting San Francisco and types in <sup>d</sup>sushi<sup>T</sup> to the cell phone’s Web search service, the phone could call up restaurants relevant to the current location with the aid of such technology. Web search technology companies including FAST Search and Transfer and Google are working with wireless phone companies to power mobile search that can benefit from locally targeted results. In addition, wireless Internet devices are more often equipped with global positioning system (GPS) technology that can track the user’s physical where abouts [44]. Both parties want to localize Web search to make it more relevant and draw more regiona advertising dollars. These new technologies have attractive market potential for the wireless and hand held sectors, specifically for any company providing location-based services. Web pages tagged with geographical data will have the ability to be included within search engine results for goods and services sorted by location and proximity. Location tags (geographical data) in conjunction with relevant keywords will give the mobile user much better search results. Any business owner who relies upon a physical presence for their business such as banks, gas stations, restaurants, even coffee shops, will benefit from this service. Although location tags in conjunction with relevant keywords provide GPS and Web-enabled mobile devices with local angle to make searching for local businesses on the Web, it is still within the keyword-based local search as SuperPages [45] does. In addition, it has been defined which manage information only in a crisp way as existing commercial Web search engines do. That is, their query languages do not allow the expression of preferences or vagueness which could be desirable for the following reasons [13]:

<sup>!</sup> to control the size of the results;

<sup>!</sup> to express soft retrieval conditions;

<sup>!</sup> to produce a discriminated answer.

An advantage of fuzzy set-based modeling is that it is mainly qualitative in nature. Indeed, in many cases, it is enough to use an ordinal scale for the membership degrees. This also facilitates the elicitation of (user/ context dependent) membership functions for which it is enough, in practice, to identify the elements that totally belong and those which do not belong at all to the fuzzy set. Fuzzy set membership functions are convenient tools for modeling user’s preference profiles. Fuzzy queries are often motivated by the expression of preferences or tolerance and of relative levels of importance [6]. Compared to the existing crisp query (i.e., keyword-based query), fuzzy query provides a better representation of users’ preferences and the necessary information for rank-ordering the answers according to the degree to which they satisfy the query. The fuzzy query and the perceptual aspects of humans are explained in considerable details in [6,13,28,30,33,34]. In this paper, we propose a search mechanism for integrating user’s physical location, location-triggered communication channels (or location-awareness) between clients (or mobile users) and Web-servers within a specified area, and user’s search intentions including keywords, preferences, etc., in a ubiquitous-GPS-Web-enabled mobile search.

In Section 2, we propose a new ubiquitous-GPS-Web-enabled mobile search mechanism based on user’s physical location, location-awareness, and user’s search intentions including keywords, preferences, etc. In Section 3, query processing based on the proposed search mechanism is described. We summarize some features of the proposed search mechanism, and introduce a new type of personalization method in Web search engines and present a personalized search and ranking algorithm based on the proposed personalization method. In Section 4, we suggest some considerations for implementing the proposed search mechanism. In Section 5, we conclude the paper.

## 2. A ubiquitous-GPS-Web-enabled mobile search mechanism

Although the commercial Web search engines such as Yahoo !, Google, Lycos, etc. help Internet users get to rich information, they generally return too many Web pages irrelevant to user’s query. In addition, they do not properly handle fuzzy query. For example, if a traveler is visiting San Francisco and try to find <sup>d</sup>famous sushi<sup>T</sup> restaurants on the Web, he/she types a fuzzy query <sup>d</sup>famous sushi<sup>T</sup>. In this case, <sup>d</sup>famous<sup>T</sup> and <sup>d</sup>sushi<sup>T</sup> are generally processed as keywords in existing commercial Web search engines. As a result, search engines return many Web pages (or URLs) irrelevant to user’s query. For example, given a fuzzy query that finds <sup>d</sup>famous sushi<sup>T</sup>, Yahoo ! returns about 317,000 Web pages (or URLs) and Google returns about 165,000 Web pages (or URLs). Intuitively, we find that there are so many Web pages (or URLs) irrelevant to user’s query. It should be noted that fuzzy term <sup>d</sup>famous<sup>T</sup> is a constraint on the focal keyword <sup>d</sup>sushi<sup>T</sup> rather than an independent keyword. In other words, the fuzzy term <sup>d</sup>famous<sup>T</sup> plays the role of a constraint on the fuzzy query. Thus, using fuzzy term(s), Internet users can narrow thousands of hits to the few that users really want. In this respect, the fuzzy terms in a query provides helpful hints for targeting queries that users really want. However, existing commercial Web search engines tend to ignore the importance of fuzzy terms in a query. Large-scale Web search engines such as Yahoo !, Google, Lycos, effectively retrieve entire documents, but they are imprecise, and do not exploit and retrieve the semantic Web document content. We can not automatically extract such content from general documents yet [16].

The most important tool for information retrieval is the index—a collection of terms with pointers to places where information about documents can be found. The indices are used to [10]:

<sup>!</sup> provide a quick and easy access to data;

<sup>!</sup> save time and operations in editing, searching, inserting, deleting of data;

<sup>!</sup> correspond with the user’s view on the contents, reducing the effort needed to understand and use it;

<sup>!</sup> provide additional services while designing queries, analyzing the content of data, etc.

The development of effective indexing tools to aid in filtering is one of major classes of problems associated with Web search and retrieval. Removal of spurious information is a particularly challenging problem [12]. Search engines are the most popular tools that people use to locate information on the Web. A search engine works by traversing the Web via the hyperlinks that connect the Web pages, performing text analysis on the pages it has encountered, and indexing the pages based on the keywords they contain. A user seeking information from the Web would formulate his/her information goal in terms of a few keywords composing a query. A search engine, on receiving a query, would match the query against its document index (DI). All of the pages that match the user query will be selected into an answer set and be ranked according to how relevant the pages are with respect to the query. Relevancy here is usually based on the number of matching keywords that a page contains [11]. The DI generally consists of keywords that appear in the title of a page or in the text body. Based on the DI, the commercial Web search engine such as Yahoo !, Google, Lycos, etc. help users to retrieve information in the Internet. For example, SuperPages [45] can help users to find <sup>d</sup>Italian restaurants within 1 mile radius from a specific address’ (US yellow pages services) [14]. This location-based search is processed based on crisp query with keywords (i.e., <sup>d</sup>Italian restaurants<sup>T</sup>, <sup>d</sup>1 mile<sup>T</sup>, <sup>d</sup>a specific address<sup>T</sup>). For the wireless and hand-held sectors, in February 2003, new technology was introduced to help businesses feed data on their physical location to Web search engines [44]. That data is stored in a tag on the business Web site and contains Geographic Information Systems (GIS) data such as the location’s latitude and longitude. Although location tags in conjunction with relevant keywords provide GPS and Web-enabled mobile devices with a local angle to make searching for local businesses on the Web, i is still within the keyword-based local search as SuperPages [45] does (i.e., search by distance and keywords). For example, they can help a mobile user to find <sup>d</sup>sushi<sup>T</sup> restaurants from user’s physical location. Until now, however, they do not properly process fuzzy queries and the location-awareness (or automatic location-based reconfiguration) between clients (or mobile users) and Web-servers within a specified area. For example, they do not properly handle a fuzzy query that finds <sup>d</sup>famous sushi<sup>T</sup> restaurants from user’s physical location within a specified area. Consequently, they do not properly reflect user’s search intentions such as preferences, local search, etc. Moreover, they have problems as follows [11]:

<sup>!</sup> large answer set;

<sup>!</sup> low precision;

<sup>!</sup> ineffective for general-concept queries.

In order to handle the fuzzy query, we propose a perception index (PI). The remarkable human capability to perform a wide variety of physical and mental tasks without any measurements and any computations is derived from the brain’s crucial ability to manipulate perceptions—perceptions of distance, size, weight, color, speed, time, direction, force, number, truth, likelihood, and other characteristics of physical and mental objects. Familiar examples of the remarkable human capability are parking a car, driving in heavy traffic, playing golf, riding a bicycle, understanding speech, and summarizing a story [31,32]. In the computational theory of perceptions (CPT) [32,33], words play the role of labels of perceptions and, more generally, perceptions are expressed as propositions in a natural language. These perceptions are mainly manipulated based on fuzzy concepts. For processing a fuzzy query, the PI consists of attributes associated with a keyword restricted by fuzzy term(s) in a fuzzy query. In this respect, the restricted keyword is named as a focal keyword, whereas attribute(s) associated with the focal keyword is named as focal attribute(s). The PI can be mainly derived from the contents in the text body of a Web page or from the other sources of information with respect to a Web page. For example, the PI may be consisted of distance, size, weight, color, popularity, etc., on a keyword in the text body of a Web page. Using the PI, search engines can process fuzzy concepts (terms). Thus, if we integrate the DI used in existing commercial Web search engines with the proposed PI as in Table 1, search engines can handle fuzzy queries. For example, consider a fuzzy query that finds <sup>d</sup>famous sushi<sup>T</sup>. In this case, the fuzzy term <sup>d</sup>famous<sup>T</sup> is processed by using the PI, whereas keyword <sup>d</sup>sushi<sup>T</sup> is processed by using the DI.

Table 1  
An example of integrated index (DI + PI)

<table><tr><td>Document index (DI)</td><td>IPs</td><td colspan="3">Perception index (PI)</td><td>FPs (Results)</td></tr><tr><td>Keywords</td><td>URLs</td><td>Size</td><td>No. of visitors</td><td>...</td><td>Targeted URLs</td></tr></table>

IPs: Intermediate Pointers; FPs: Final Pointers; URLs: Uniform Resource Locators.

It should be noted that fuzzy term(s) may be regarded as a constraint on a fuzzy query. For example, consider a fuzzy query that finds <sup>d</sup>famous sushi<sup>T</sup>. In this case, the fuzzy term <sup>d</sup>famous<sup>T</sup> plays the role of a constraint on the fuzzy query. Thus, using fuzzy term(s), Internet users may narrow thousands of hits to the few that users really want. In this respect, the PI provides helpful hints for targeting queries that users really want.

The expressive power of conventional search engine query interfaces is relatively weak when restricted to keyword-based search [11,26]. At present, commercial Web search engines based on the DI (i.e., keyword-based search engines) present limitations in modeling perceptual aspects of humans. In addition, they generally return too many Web pages (or URLs) irrelevant to user’s query. Although much Web search engines have been developed, they do not properly handle the fuzzy terms representing human’s perception. In addition, they are unsuccessful in returning the targeted results. In order to tackle these problems, we integrate the DI used in existing commercial Web search engines with the proposed PI. For a ubiquitous-GPS-Web-enabled mobile search, we assume that mobile devices are equipped with GPS technology for user’s physical location and the embedded ubiquitous chips for location-awareness between clients and Web-servers within a specified area. The embedded ubiquitous chip in a ubiquitous-GPS-Web-enabled mobile device deliver reminders when users are within a specified area, and these reminders are processed in a location-detection module in the ubiquitous-GPS-Web-enabled Web-severs. As a result, location-triggered communication channels are established between clients and Web-servers within a specified area. In this respect, we can achieve the proximate selection, and automatic location-based reconfiguration due to mobile user’s location changes, between mobile users and the ubiquitous-GPS-Webenabled Web-servers within a specified area. For a ubiquitous-GPS-Web-enabled mobile search, given a fuzzy query, the proposed search mechanism processes the fuzzy query based on the integrated index (DI + PI), user’s physical location and distance from user’s physical location (or location-awareness for automatic location-based reconfiguration due to mobile user’s location changes) as shown in Fig. 1.

In Fig. 1, if we submit a query with only crisp terms (keyword-based query), for example, finds <sup>d</sup>sushi<sup>T</sup> restaurants from user’s physical location within a specified area, then by applying the DI, user’s physical location and location-awareness, this search engine performs an elimination-based approach to eliminate the URLs which are impossible to be the answers of the query. On the other hand, if we submit a fuzzy query, for example, finds <sup>d</sup>famous sushi restaurants from user’s physical location within a specified area, then by applying the integrated index (DI + PI), user’s physical location and location-awareness, more personalized search results are extracted. More specifically, the phase 2 evaluates the fuzzy terms and location-awareness in detail on the set of intermediate pointers (i.e., the candidate URLs), and then generates the final pointers (FPs) (i.e., targeted results) that user really wants. This search mechanism can be conceptually explained by SQL-like language as follows : SELECT\*FROM {a set of intermediate pointers that satisfies both keyword(s) in the DI and user’s physical location} [WHERE the value(s) of focal attribute(s) in the PI are satisfied by the user within a specified area]. We note that existing commercial Web search engines tend to ignore the importance of [WHERE] part. In this approach, the PI, the specified area (or distance) for location-awareness, and user’s physical location may be regarded as a constraint on the DI. Consequently, the proposed mechanism gives the mobile user more personalized and locally targeted search results.

![](/api/attachments/9DXJWFDR/fulltext/images/2d95b1bc37dc5b44674ebcd9b60b5e5babef35a5eb3d6221210dd9a98f352563.jpg)  
Fig. 1. A ubiquitous-GPS-Web-enabled mobile search mechanism based on the integrated index (DI + PI), location-awareness and user’s physical location.

## 3. Query processing based on the integrated index, user’s physical location and location-awareness

For the fuzzy query processing, we assume Web search engines have directory browser that can select user’s search intentions such as restaurant, health, autos, travel, etc. The directory browser highly reduces the degree of freedom on fuzzy terms. In other words, directory browser provides the higher possibility for a well-defined (restricted) condition. For example, given a travel-domain database, consider a fuzzy query that finds <sup>d</sup>popular national parks in the USA<sup>T</sup>. In this case, the fuzzy term <sup>d</sup>popular<sup>T</sup> is used to restrict <sup>d</sup>national parks<sup>T</sup>, not <sup>d</sup>music<sup>T</sup>, <sup>d</sup>entertainer<sup>T</sup>, etc. We note that $\cdot _ { \mathrm { i n } } ,$ and $\cdot _ { \mathrm { t h e } } ,$ in the above fuzzy query are examples of stop words ignored by search engines (see http://www.google.com). Now, we present how this search engine processes fuzzy queries. Let the set of <sup>d</sup>sushi<sup>T</sup> restaurants from user’s physical location within a specified area be $A = \{ A _ { 1 } , ~ A _ { 2 } , . ~ . ~ . , ~ A _ { 9 9 } , ~ A _ { 1 0 0 } \}$ and each $A _ { i } , \quad ( i = 1 $ 2, . . . , 100) has its own page title or URL.

Example 1. Consider a crisp query that finds <sup>d</sup>sushi restaurants from user’s physical location within a specified area $\left( \mathrm { Q } _ { 1 } \right)$ . In this case, the PI in Fig. 1 is not used. Thus, the integrated index is made as in Table 2.

We note that IPs and FPs are equal. Consequently, ubiquitous-GPS-Web-enabled mobile devices receive locally targeted search results based on the focal keyword <sup>d</sup>sushi<sup>T</sup> in the DI, user’s physical location and distance, within directory <sup>d</sup>restaurants<sup>T</sup>. As an example of applications, mobile phones could call up sushi restaurants relevant to the current location (i.e., search by distance and keyword) with the aid of ubiquitous-GPS-Web-enabled technology.

A snapshot of integrated index (DI + PI) after processing $\mathrm { Q } _ { 1 }$

<table><tr><td>Document index (DI)</td><td>IPs</td><td>Perception index (PI)</td><td></td><td>FPs (Results)</td></tr><tr><td rowspan="5">Sushi</td><td> $A_{1}$ </td><td>No. of visitors</td><td>...</td><td> $A_{1}$ </td></tr><tr><td> $A_{2}$ </td><td>No. of visitors</td><td>...</td><td> $A_{2}$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $A_{99}$ </td><td>No. of visitors</td><td>...</td><td> $A_{99}$ </td></tr><tr><td> $A_{100}^{+}$ Irrelevant URLs</td><td>No. of visitors</td><td>...</td><td> $A_{100}^{+}$ Irrelevant URLs</td></tr></table>

IPs: Intermediate Pointers; FPs: Final Pointers; URLs: Uniform Resource Locators.

![](/api/attachments/9DXJWFDR/fulltext/images/18f2ff4ef3a1c4610e9d3dc0b46472b25dd87504b6d53bc23cd309cd07e4fafb.jpg)  
Fig. 2. A membership function of <sup>d</sup>famous<sup>T</sup>.

Example 2. Consider a fuzzy query that finds <sup>d</sup>famous sushi<sup>T</sup> restaurants from user’s physical location within a specified area $( \mathbf { Q } _ { 2 } )$ . In this case, the DI and PI in Fig. 1 are used. The DI and PI may be as follows : DI = {sushi, . . . }, PI = {no. of visitors, . . . }. We note that a focal keyword <sup>d</sup>sushi<sup>T</sup> in the DI is restricted by a fuzzy term <sup>d</sup>famous<sup>T</sup>. In this case, the fuzzy term <sup>d</sup>famous<sup>T</sup> may be manipulated by the number of visitors (i.e., a focal attribute in the PI) per day, and represented by a membership function as in Fig. 2. For example, the proposed search mechanism finds <sup>d</sup>famous sushi<sup>T</sup> restaurants (i.e., <sup>d</sup>no. of visitors<sup>T</sup> per day 100) from user’s physical location within 2 miles. We assume that $\mathrm { Q } _ { 2 }$ is A<sub>F</sub>, $A _ { \mathrm { F } } \in \{ A _ { 1 } , A _ { 2 } , \dotsc ,$ $A _ { 9 9 } , A _ { 1 0 0 } \}$ , by using a-cut in Fig. 2. In this case, the integrated index is made as in Table 3. Consequently, ubiquitous-GPS-Web-enabled mobile devices receive more personalized and locally targeted search results $( A _ { \mathrm { F } } )$ based on the focal keyword <sup>d</sup>sushi<sup>T</sup> in the DI, the value of focal attribute <sup>d</sup>no. of visitor<sup>T</sup> in the PI, user’s physical location and distance, within directory <sup>d</sup>restaurants<sup>T</sup>.

A snapshot of integrated index (DI + PI) after processing $\mathrm { Q } _ { 2 }$

<table><tr><td>Document index (DI)</td><td>IPs</td><td colspan="2">Perception index (PI)</td><td>FPs (Results)</td></tr><tr><td>Sushi</td><td> $\{A_1, \dots, A_{100}\} +$ IrrelevantURLs</td><td>No. of visitors</td><td>...</td><td>URLs w.r.t  $\{A_F\}$ </td></tr></table>

Focal keyword: Sushi; Focal attribute: No. of visitors.

![](/api/attachments/9DXJWFDR/fulltext/images/d7509567c1b79dc3a2dbe017369d7e541b077da91b7d2c6b9e1fcc25a10c492b.jpg)  
Fig. 3. A membership function of <sup>d</sup>low-price<sup>T</sup>.

Example 3. Consider a fuzzy query that finds <sup>d</sup>lowprice sushi<sup>T</sup> restaurants from user’s physical location within a specified area $\left( \mathbf { Q } _ { 3 } \right)$ . In this case, the DI and PI in Fig. 1 are used. The DI and PI may be as follows : $\mathrm { D I } = \{ s u s h i , \ldots \} , \mathrm { P I } = \{ p r i c e , \ldots \} $ We note that a focal keyword <sup>d</sup>sushi<sup>T</sup> in the DI is restricted by a fuzzy term <sup>d</sup>low-price<sup>T</sup>. In this case, the fuzzy term <sup>d</sup>low-price<sup>T</sup> may be manipulated by the degree of price (i.e., a focal attribute in the PI), and represented by a membership function as in Fig. 3. For example, the proposed search mechanism finds <sup>d</sup>low-price sushi<sup>T</sup> restaurants (i.e., Sushi price V 8 in US\$) from user’s physical location within 2 miles. We assume that $\mathrm { Q } _ { 3 }$ is $A _ { \mathrm { L P } } , A _ { \mathrm { L P } } \in \{ A _ { 1 } , A _ { 2 } , . . . , A _ { 9 9 } , A _ { 1 0 0 } \}$ , by using a-cut in Fig. 3. In this case, the integrated index is made as in Table 4. Consequently, ubiquitous-GPS-Web-enabled mobile devices receive more personalized and locally targeted search results $\left( \boldsymbol { A } _ { \mathrm { L P } } \right)$ based on the focal keyword <sup>d</sup>sushi<sup>T</sup> in the DI, the value of focal attribute <sup>d</sup>price<sup>T</sup> in the PI, user’s physical location and distance, within directory <sup>d</sup>restaurants<sup>T</sup>.

Example 4. Consider a fuzzy query that finds <sup>d</sup>moderate-price hotel<sup>T</sup> from user’s physical location within a specified area $\mathrm { ( Q _ { 4 } ) }$ . In this case, the DI and PI in Fig. 1 are used. The DI and PI may be as follows :

A snapshot of integrated index (DI + PI) after processing $\mathrm { Q } _ { 3 }$

<table><tr><td>Document index (DI)</td><td>IPs</td><td>Perception index (PI)</td><td>FPs (Results)</td></tr><tr><td>Sushi</td><td> $\{A_{1},\dots,A_{100}\} +$  Irrelevant URLs</td><td>Price ...</td><td>URLs w.r.t  $\{A_{LP}\}$ </td></tr></table>

Focal keyword: Sushi; Focal attribute: Price.

${ \mathrm { D I } } = \{ h o t e l , . . . \} , { \mathrm { P I } } = \{ p r i c e , . . . \} $ . We note that a focal keyword <sup>d</sup>hotel<sup>T</sup> in the DI is restricted by a fuzzy term <sup>d</sup>moderate-price<sup>T</sup>. In this case, the fuzzy term <sup>d</sup>moderate-price<sup>T</sup> may be manipulated by the degree of price (i.e., a focal attribute in the PI), and represented by a membership function as in Fig. 4. For example, the proposed search mechanism finds <sup>d</sup>moderate-price hotel<sup>T</sup> (i.e., price = [60, 120] in US \$) from user’s physical location within 2 miles. We assume that $\mathrm { Q } _ { 4 }$ is ${ \cal A } _ { \mathrm { M P } } , { \cal A } _ { \mathrm { M P } } \in \{ { \cal A } _ { 1 } , ~ { \cal A } _ { 2 } , \ldots , ~ { \cal A } _ { 9 9 } ,$ $\boldsymbol { A } _ { 1 0 0 } \}$ , by using a-cut in Fig. 4. This query can be similarly handled as in Example 3.

Example 5. Consider a fuzzy query that finds <sup>d</sup>famous and low-price sushi<sup>T</sup> restaurants from user’s physical location within a specified area $( \mathbf { Q } _ { 5 } ) .$ . In this case, the DI and PI in Fig. 1 are used. The DI, PI and logical operator may be as follows : $\mathrm { D I } = \{ s u s h i , \ldots \} , \mathrm { P I } = \{ n o .$ of visitors, $p r i c e , \ldots \nmid$ , logical operator = {and}. We note that a focal keyword <sup>d</sup>sushi<sup>T</sup> in the DI is restricted by fuzzy terms <sup>d</sup>famous<sup>T</sup> and <sup>d</sup>low-price<sup>T</sup>. In this case, the fuzzy terms <sup>d</sup>famous<sup>T</sup> and <sup>d</sup>low-price<sup>T</sup> may be manipulated as in Figs. 2 and 3, respectively. For example, the proposed search mechanism finds <sup>d</sup>famous and low-price sushi<sup>T</sup> restaurants $( \mathrm { i . e . , ~ \hbar \Omega ^ { \mathrm { ~ } } n o }$ of visitors<sup>T</sup> per $\mathrm { d a y } \geq 1 0 0$ and Sushi priceV8 in US\$) from user’s physical location within 2 miles. Logical operators such as <sup>d</sup>or<sup>T</sup>, <sup>d</sup>not<sup>T</sup> can be similarly used for representing relationships among fuzzy terms. Then the query results with respect to $\mathrm { Q } _ { 5 }$ become $\{ A _ { \mathrm { F } } \} \cap \{ A _ { \mathrm { L P } } \}$ . For instance, let $A _ { \mathrm { F } }$ be a set $\left\{ A _ { 1 } , A _ { 2 } , A _ { 3 } \right\}$ and $A _ { \mathrm { L P } }$ be a set $\{ A _ { 1 } , A _ { 4 } , A _ { 5 } \}$ , then $\{ A _ { \mathrm { F } } \} \cap \{ A _ { \mathrm { L P } } \} = \{ A _ { 1 } \}$ . In this case, the integrated index is made as in Table 5. Consequently, ubiquitous-GPS-Web-enabled mobile devices receive more personalized and locally targeted search results $( \{ A _ { \mathrm { F } } \} \cap \{ A _ { \mathrm { L P } } \} )$ based on the focal keyword <sup>d</sup>sushi<sup>T</sup> in the DI, the values of focal attributes <sup>d</sup>no. of visitor<sup>T</sup> and <sup>d</sup>price<sup>T</sup> in the PI, user’s physical location and distance, within directory <sup>d</sup>restaurants<sup>T</sup>.

![](/api/attachments/9DXJWFDR/fulltext/images/d75b48a9d089fe1634fb509342ccb2cfa7aca45ede6450c5b2b9ed3e99bda64f.jpg)  
Fig. 4. A membership function of <sup>d</sup>moderate-price<sup>T</sup>.

A snapshot of integrated index (DI + PI) after processing $\mathrm { Q } _ { 5 }$

<table><tr><td>Document index (DI)</td><td>IPs</td><td>Perception index (PI)</td><td>FPs (Results)</td></tr><tr><td>Sushi</td><td> $\{A_1, \dots, A_{100}\} +$ IrrelevantURLs</td><td>No. of visitors Price</td><td>... URLs w.r.t $\{A_F\} \cap \{A_{LP}\}$ </td></tr></table>

Focal keyword: Sushi; Focal attributes: No. of visitors and price.

In a similar sense, logical operators such as $\cdot _ { \mathrm { o r } } ,$ , <sup>d</sup>not<sup>T</sup> can be manipulated.

## 3.1. Some features of the proposed search mechanism

The proposed search mechanism has the following features: First, the higher the a in a-cut $( 0 \leq \alpha \leq 1 )$ , the smaller the number of the targeted results. This property provides continual incremental result from the highest constraint $( \mathrm { i } . \mathrm { e } . , \ : \alpha = 1 )$ to the lowest constraint $( \mathrm { i } . \mathrm { e } . , \ : \alpha = 0 )$ . Consequently, we can achieve <sup>d</sup>interactive user control of the query processing<sup>T</sup> by adjusting the value of a. Second, even though the same integrated index (DI + PI) is given, different search results are returned by adjusting the value of a or by using different focal attributes in the PI or by user’s physical location or by distance. In the case of <sup>d</sup>using different focal attributes in the PI<sup>T</sup>, for example, consider a fuzzy query that finds <sup>d</sup>attractive $\operatorname { c a r } ^ { * }$ where <sup>d</sup>attractive<sup>T</sup> means <sup>d</sup>comfortable and fast<sup>T</sup>. In this case, for the fuzzy term <sup>d</sup>attractive<sup>T</sup>, people may use different focal attributes (i.e., size, speed, etc.) in the PI. In addition, different people may use different conceptual comprehension (fuzzy terms, membership functions, a-cut), with respect to the same situation. Thus, by reflecting user’s search intentions by means of fuzzy query and distance, search engine will return the targeted results that users really want. Third, clustering (i.e., grouping similar documents together to expedite information retrieval) is adaptively determined depending on the value of a or the selected focal attributes in the PI or user’s physical location or distance. Fourth, for comparing with commercial keyword-based Web search engines, the ratio [the number of FPs/the number of IPs] can be used as a measure of performance evaluation on the proposed mechanism.

We note that the number of IPs is the result of phase 1 and the number of FPs is the result of phase 2 in Fig. 1. The smaller the ratio, the better the filtering effect of the proposed mechanism. For example, in the case of fuzzy query $\mathrm { Q } _ { 2 } \mathrm { ( i . e . }$ , <sup>d</sup>famous sushi<sup>T</sup>) in Example 2,

(i) Yahoo: The proposed mechanism=317,000: A . In this case, the rati $\underline { { \scriptscriptstyle 1 } } = [ A _ { \mathrm { F } } / 3 1 7 , 0 0 0 ]$

$$
\begin{array}{l} \text {(ii) Google: The proposed mechanism = 165,000: A_{F}.} \\ \text { In this case,the ratio = [A_{F} /165,000].} \end{array}
$$

Yahoo and Google return search results of about 317,000 and 165,000 on the fuzzy query $\mathrm { Q } _ { 2 } ,$ respectively. It should be noted that commercial keywordbased Web search engines use only the phase 1 in Fig. 1. Fifth, using fuzzy query, together with user’s physical location and location-awareness for automatic location-based reconfiguration due to mobile user’s location changes, ubiquitous-GPS-Web-enabled mobile devices can receive more personalized and locally targeted search results. In summary, the proposed approach can be explained as in Fig. 5.

## 3.2. Personalized search and ranking

The Web is an impressive success story in terms of both its available information and the growth rate of human users. It now penetrates most areas of our lives, and its success is based on its simplicity. Unfortunately, this simplicity could hamper further Web development [7]. Often, search engines will return many results, but most will be uninteresting to the user. If a search tool can get geographical information or learn preferences or contexts from the user, this information can be used to improve the search or document-ranking process.

Internet users do not have to watch all the irrelevant noise. In this respect, personalization technology gives the user a more tailored site. It is the provision to the individual of tailored products, services, advertisements, or information relating to products or services. Personalization of Web pages can be accomplished in numerous ways. Some approaches require the user’s participation (typically through filling out a form or questionnaire). Other approaches operate behind the scenes, without depending on user input, for example, by using Web cookies for tracking what user likes to view or by analyzing Web server log for the access pattern and statistics, etc. An important problem relating to personalization concerns understanding how a machine can help an individual user via suggesting recommendations [3]. In this respect, we mainly present the perception personalization based on the PI in a ubiquitous-GPS-Webenabled mobile search.

![](/api/attachments/9DXJWFDR/fulltext/images/cdd06876737793bf62e8d41162b56f3680a3923be81d89c0f11ce61e2f11c2ee.jpg)  
Fig. 5. Personalized and targeted local search.

As described in Section 3.1, in the case of <sup>d</sup>using different focal attributes in the PI<sup>T</sup>, for example, consider a fuzzy query that finds <sup>d</sup>attractive car<sup>T</sup>, where <sup>d</sup>attractive<sup>T</sup> means <sup>d</sup>comfortable and fast<sup>T</sup>. In this case, for the fuzzy term <sup>d</sup>attractive<sup>T</sup>, people may use different focal attributes (i.e., size, speed, etc.) in the PI. In addition, different people may use different conceptual comprehension (fuzzy terms, membership functions, a-cut), with respect to the same situation. Thus, by using the PI, we can achieve perception personalization and Web search engines will return the personalized search results that users really want.

Ranking algorithm plays an important role in Web search engines. In existing Web search engines, however, detailed information regarding ranking algorithms used by major search engines is not publicly available. A simple means to measure the quality of a Web page, proposed by Carriere and

Kazman [5], is to count the number of pages with pointers to the page. Google is a representative Web search engine that uses link information. Its rankings are based, in part, on the number of other pages with pointers to the page. In November 1999, Northern Light introduced a new ranking system, which is also based, in part, on link data [35,36]. In other words, Google and Northern Light rank search results, in part, by popularity. In the meantime, HotLinks ranks search results based on the bookmarks of its registered users. In theory, more popular links indicate more relevant content, but if a user differs from the crowd, simply popularity-based ranking approaches dive deeply into other possibilities on the Web. Consequently, they often give users many Web pages irrelevant to user’s query. In addition, they often tend to return unranked random samples in response to user’s query. In order to tackle these problems, we introduce a new ranking algorithm based on the perception index (PI).

Zadeh [30] suggested we can represent linguistic quantifiers as fuzzy subsets of the unit interval. In this representation the membership grade of any proportion r <sup>a</sup> [0, 1], Q(r), is a measure of the compatibility of the proportion r with the linguistic quantifier we are representing by the fuzzy subset $Q .$ For example, if Q is the quantifier <sup>d</sup>most<sup>T</sup> then Q(0.9) represents the degree to which 0.9 satisfies the concept <sup>d</sup>most<sup>T</sup>. Yager [27,28] identified three classes of linguistic quantifiers that cover most of these used in natural language.

(i) A quantifier Q is said to be monotonically nondecreasing if $r _ { 1 } > r _ { 2 }$ then $Q ( r _ { 1 } ) { \geq } Q ( r _ { 2 } )$

(ii) A quantifier Q is said to be monotonically nonincreasing if $r _ { 1 } > r _ { 2 }$ then $Q ( r _ { 1 } ) { \le } Q ( r _ { 2 } )$

(iii) A quantifier $\boldsymbol { Q }$ is said to be unimodal if there exists two values $a \leq b$ both contained in the unit interval such that for $r { < } a , \varrho$ is monotonically nondecreasing, for $r > b$ , Q is monotonically nonincreasing, and for $r \in [ a , b ] , Q ( r ) = 1$ Fig. 6 shows prototypical examples of these quantifiers.

In a similar way, we can identify three classes of fuzzy terms that cover most of these used in natural language. For example, we have represented the fuzzy terms <sup>d</sup>famous<sup>T</sup> (monotonically nondecreasing), <sup>d</sup>lowprice<sup>T</sup> (monotonically nonincreasing), <sup>d</sup>moderateprice<sup>T</sup> (unimodal) (see Figs. 2–4). In this respect, we design a new ranking algorithm based on the PI.

## Algorithm 1. Ranking for one focal attribute

## (i) Monotonically nondecreasing case

The larger the value of focal attribute in the PI, the higher the rank retrieved documents for a given fuzzy query.

## (ii) Monotonically nonincreasing case

The larger the value of focal attribute in the PI, the lower the rank retrieved documents for a given fuzzy query.

## (iii) Unimodal case

If an interval of focal attribute determined by a-cut is $[ a _ { i } , b _ { i } ] .$ , and let $\beta$ denote the midpoint between $a _ { i }$ and $b _ { i } ,$ , then the degree of closeness (nearness) to $\beta$ can be used as a ranking criterion. In other words, the closer the $\beta ,$ , the higher the rank retrieved documents for a given fuzzy query.

Example 6. Consider a fuzzy query that finds <sup>d</sup>famous sushi<sup>T</sup> restaurants from user’s physical location within a specified area. In this case, the fuzzy term <sup>d</sup>famous<sup>T</sup> may be represented by a monotonically nondecreasing membership function (see Fig. 2). We assume that <sup>d</sup>famous sushi<sup>T</sup> restaurants from user’s physical location within a specified area are $A _ { \mathrm { F } }$ by using a-cut. Let the personalized and locally targeted search results $A _ { \mathrm { F } }$ be $\mathsf { \bar { \{ A _ { F } ^ { 1 } , \ { A _ { F } ^ { 2 } , \ldots , A _ { F } ^ { r } \} } } }$ taking values of focal attribute $( \mathrm { i . e . , ~ } \ \mathrm { n o . }$ of visitors) such as $\mathrm { V a l } ( A _ { \mathrm { F } } ^ { 1 } ) { \le } \mathrm { V a l } ( A _ { \mathrm { F } } ^ { 2 } ) { \le }$ $\cdot \cdot \cdot \leq \mathrm { V a l } ( A _ { \mathrm { F } } ^ { r } )$ , then the personalized and locally targeted search results $A _ { \mathrm { F } }$ are ranked as the following order: $A _ { \mathrm { F } } ^ { r } , . . . , A _ { \mathrm { F } } ^ { 2 } , A _ { \mathrm { F } } ^ { 1 }$

Example 7. Consider a fuzzy query that finds <sup>d</sup>lowprice sushi<sup>T</sup> restaurants from user’s physical location within a specified area. In this case, the fuzzy term <sup>d</sup>low-price<sup>T</sup> may be represented by a monotonically nonincreasing membership function (see Fig. 3). We assume that <sup>d</sup>low-price sushi<sup>T</sup> restaurants from user’s physical location within a specified area are $\boldsymbol { A } _ { \mathrm { L P } }$ by using a-cut. Let the personalized and locally targeted search results $A _ { \mathrm { L P } }$ be $\{ A _ { \mathrm { L P } } ^ { 1 } , \ A _ { \mathrm { L P } } ^ { 2 } , . . . , \ A _ { \mathrm { L P } } ^ { t ^ { - } } \}$ taking values of focal attribute $( \mathrm { i . e . }$ , price) such as $\mathrm { V a l } ( \mathcal { A } _ { \mathrm { L P } } ^ { 1 } ) { \le } \mathrm { V a l } ( \mathcal { A } _ { \mathrm { L P } } ^ { 2 } ) { \le } . . . { \le } \mathrm { V a l } ( \mathcal { A } _ { \mathrm { L P } } ^ { t } )$ , then the personalized and locally targeted search results $A _ { \mathrm { L P } }$ are ranked as the following order: $A _ { \mathrm { L P } } ^ { 1 } , \ A _ { \mathrm { L P } } ^ { 2 } , . . . , A _ { \mathrm { L P } } ^ { t } .$

Example 8. Consider a fuzzy query that finds <sup>d</sup>moderate-price hotels<sup>T</sup> from user’s physical location within a specified area. In this case, the fuzzy term <sup>d</sup>moderate-price<sup>T</sup> may be represented by a unimodal membership function (see Fig. 4). We assume that <sup>d</sup>moderate-price hotels<sup>T</sup> from user’s physical location within a specified area are $A _ { \mathrm { M P } }$ by using a-cut. Let an interval of focal attribute (i.e., price) determined by acut be $[ a _ { i } , b _ { i } ]$ , and let $\beta$ denote the midpoint between $a _ { i }$ and $b _ { i } ,$ and let the personalized and locally targeted search results $A _ { \mathrm { M P } }$ be $\{ A _ { \mathrm { M P } } ^ { 1 } , \ A _ { \mathrm { M P } } ^ { 2 } , \ldots , A _ { \mathrm { M P } } ^ { s } \}$ taking values of the focal attribute such as $\mathrm { V a l } ( A _ { \mathrm { M P } } ^ { 1 } )$ $\mathrm { V a l } ( A _ { \mathrm { M P } } ^ { 2 } ) , \dotsc , \ \mathrm { V a l } ( A _ { \mathrm { M P } } ^ { s } )$ . If the degree of closeness (nearness) to $\beta$ is the order $\mathrm { V a l } ( A _ { \mathrm { M P } } ^ { 1 } ) , \mathrm { V a l } ( A _ { \mathrm { M P } } ^ { 2 } ) , \dots ,$ $\mathrm { V a l } ( A _ { \mathrm { M P } } ^ { s } )$ , then the personalized and locally targeted search results $A _ { \mathrm { M P } }$ are ranked as the following order: $A _ { \mathrm { M P } } ^ { 1 } , A _ { \mathrm { M P } } ^ { 2 } , \ldots , A _ { \mathrm { M P } } ^ { s }$

![](/api/attachments/9DXJWFDR/fulltext/images/318627fd8ce997db3bd9d8171b3d8983757edced94ca0bb1be226e59e0e2a5f9.jpg)  
(i) Monotonically nondecreasing

![](/api/attachments/9DXJWFDR/fulltext/images/7a56531ed1d711b92d43c7af4e7dea20d08d9063f2e5d08515f0912fd8e1277e.jpg)

(ii) Monotonically nonincreasing  
Fig. 6. Three types of quantifiers.  
![](/api/attachments/9DXJWFDR/fulltext/images/e6fbc231d0254bf21e5568885a801a9273b0535ebf8362ca4e7a35f8ed2695eb.jpg)  
(iii) Unimodal

Algorithm 2. Ranking for multiple focal attributes

If we have multiple focal attributes (for instance, <sup>d</sup>no. of visitors<sup>T</sup> and <sup>d</sup>price<sup>T</sup>), weighting the importance of focal attributes should be considered. For the weighted case, assume that $\theta _ { 1 } , \ \theta _ { 2 } , \ldots , \ \theta _ { n }$ are ordinal weights. Then we refer to $\theta = ( \theta _ { 1 } , \ \theta _ { 2 } , \ldots ,$ $\theta _ { n } )$ as a weighting, where $\theta _ { i }$ is the weight of attribute i. Intuitively, the targeted results can be ranked according to the ordinal weights. For a respective focal attribute, the rank retrieved documents for a given fuzzy query can be determined based on the Algorithm 1.

Example 9. Consider a fuzzy query that finds <sup>d</sup>famous and low-price sushi<sup>T</sup> restaurants from user’s physical location within a specified area. In this case, the fuzzy terms <sup>d</sup>famous<sup>T</sup> and <sup>d</sup>low-price<sup>T</sup> may be represented by a monotonically nondecreasing membership function and a monotonically nonincreasing membership function, respectively. Using the results of Examples 6 and 7, if the weight of focal attribute <sup>d</sup>no. of visitors<sup>T</sup> is more important than the weight of focal attribute <sup>d</sup>price<sup>T</sup>, then the personalized and locally targeted search results are ranked as the following order: $A _ { \mathrm { F } } ^ { r } , \ldots , A _ { \mathrm { F } } ^ { 2 } , A _ { \mathrm { F } } ^ { 1 } , A _ { \mathrm { L P } } ^ { 1 } ,$ $A _ { \mathrm { L P } } ^ { 2 } , \ldots , A _ { \mathrm { L F } } ^ { \mathrm { t } }$ .

Now, if we apply Algorithms 1 and 2, the targeted search results can be displayed from the highest rank to the lowest rank. Although the existing ranking mechanisms for Web search engines also provide users with their own ranking algorithms based on popularity, bookmark, etc., their approaches look like the behind-the-scenes processing. In the proposed approach, user<sup>T</sup>s search intentions can be explicitly reflected by using the values of focal attributes in the PI. In this respect, we can explicitly describe how to rank the search results by means of the proposed algorithms. Consequently, the proposed algorithms provide a user with the personalized ranking based on user’s search intentions.

## 4. Some considerations for implementation

The work of Lidsky and Kwon [14] is an opinionated but informative resource on search engines. It describes 36 different search engines and rates them on specific details of their search capabilities. For instance, in one study, searches are divided into five categories : (1) simple searches; (2) custom searches; (3) directory searches; (4) current news searches; and (5) Web content. The five categories of search are evaluated in terms of power and ease of use. Variations in ratings sometimes differ substantially for a given search engine. In the meantime, they chose the respective best search engine according to five categories: (1) search indexes and directories; (2) people finders; (3) business finders; (4) usenet search; and (5) metasearch. The data indicate that as the number of people using the Internet and Web has grown, user types have diversified and search engine providers have begun to target more specific types of users and queries with specialized and tailored search tools. In this respect, for the fuzzy query processing, directory-based design requirement for managing Web sites is necessary because of the following reason: the present state of AI is not up to formulating a full commonsense database, but full commonsense knowledge is not necessary [17]. In this respect, for the fuzzy query processing, if we design a search engine based on <sup>d</sup>directory<sup>T</sup> concept (i.e., travel, health, recreation, etc.), the degree of freedom on fuzzy terms will be highly reduced. In other words, <sup>d</sup>directory<sup>T</sup> concept provides the higher possibility for a well-defined (restricted) condition. For example, given a travel-domain database, consider a fuzzy query that finds <sup>d</sup>popular national parks in the USA<sup>T</sup>. In this case, the fuzzy term <sup>d</sup>popular<sup>T</sup> is used to restrict <sup>d</sup>national parks<sup>T</sup>, not <sup>d</sup>music<sup>T</sup>, <sup>d</sup>entertainer<sup>T</sup>, etc. In the meantime, we need to consider the followings : (1) ease of use—for the fuzzy query on the Internet, the <sup>d</sup>ease of use<sup>T</sup> is important because Internet users are broad spectrum in terms of age, level of intelligence, etc. In this respect, user interface for phase 2 in Fig. 1 should provide Internet users with an easy user interface for specifying the fuzzy terms such as <sup>d</sup>famous<sup>T</sup>, <sup>d</sup>attractive<sup>T</sup>, etc.; (2) cultural differences—we need to reflect cultural differences in handling fuzzy terms. For instance, different people generally use different scales (i.e., feet, miles, meter, etc.) in handling fuzzy terms.

In Section 1, we assume that an embedded ubiquitous chip in a ubiquitous-GPS-Web-enabled mobile device deliver reminders when users are within a specified area, and these reminders are processed in a location-detection module in the ubiquitous-GPS-Web-enabled Web-severs. In order to implement the ubiquitous communication for location-awareness between a ubiquitous-GPS-Web-enabled mobile device and the ubiquitous-GPS-Web-enabled Web-severs within a specified area, ubiquitous sensor network (USN) is necessary as in Fig. 7.

## 5. Conclusions

The expressive power of conventional Web search engine query interfaces is relatively weak when restricted to keyword-based search (i.e., document index (DI)-based search). At present, the keyword based search engines present limitations in modeling perceptual aspects of humans. In addition, they are unsuccessful in returning the targeted results. In other words, they generally return too many Web pages (or URLs) irrelevant to user’s query. In this respect, we need a new tool to handle both the fuzzy query and the removal of spurious results. In order to tackle these problems, we introduce the perception index (PI). If we integrate the document index (DI) used in existing commercial Web search engines with the proposed PI, we can handle both crisp terms (keyword-based) and fuzzy terms (perception-based). It is a further step toward a human-friendly, natural language-based interface for Web searching. The proposed mechanism assists the user to reflect his/her perception in the process of query. As a consequence, Internet users can narrow thousands of hits to the few that users really want. In this respect, the PI provides a new tool for targeting queries that users really want. The use of PI also provides helpful hints for solving the problems of <sup>d</sup>large answer set<sup>T</sup>, <sup>d</sup>low precision<sup>T</sup>, <sup>d</sup>ineffective for general-concept queries<sup>T</sup> suffered by most search engines. An important problem relating to personalization concerns understanding how a machine can help an individual user via suggesting recommendations [3]. In this respect, we introduce the perception personalization based on the PI in a ubiquitous-GPS-Web-enabled mobile search, and present a personalized search and ranking algorithms based on the PI.

In this paper, a new ubiquitous-GPS-Web-enabled mobile search mechanism is proposed. It is based on user’s physical location, distance from user’s physical location (or location-awareness for automatic location-based reconfiguration due to mobile user’s location changes) and user’s search intentions (i.e., keywords, preferences, etc.) Using fuzzy query, together with user’s physical location and distance from user’s physical location, ubiquitous-GPS-Web-enabled mobile devices can receive more personalized and locally targeted search results. The proposed approach can be applied to enhance the power of mobile Web search. Consequently, it gives a mobile user the personalized local angle to make searching for local businesses on the Web, and contributes to a significant convenience in the location-based mobile Web searching (i.e., local Internet).

![](/api/attachments/9DXJWFDR/fulltext/images/bd9556f1593335a06faeab2661ce3e38de05622eb08cb485c662c4dae632df05.jpg)  
Fig. 7. Ubiquitous sensor network (USN).

## Acknowledgement

The author would like to thank the anonymous referees for their comments and suggestions which helped to improve this paper. He wishes to thank Prof. L.A. Zadeh, University of California, Berkeley, for his inspirational address on the perceptual aspects of humans in the BISC (Berkeley Initiative in Soft Computing) seminars and group meetings. This work was supported by Korea Research Foundation Grant (KRF-2004-013-D00040).

## References

[1] D.J. Abel, V.J. Gaede, K.L. Taylor, X. Zhou, SMART: towards spatial Internet marketplaces, Geoinformatica 3 (2) (1999) 141–164.

[2] N. Andrienko, G. Andrienko, Intelligent support for geographic data analysis and decision making in the web, Journal of Geographic Information and Decision Analysis 5 (2) (2001) 115– 128.

[3] N.J. Belkin, Helping people find what they don’t know, Communications of the ACM 43 (8) (2000) 58– 61.

[4] A. Boukerche, S.K. Das, Special issue on wireless and mobile computing and communications, Journal of Parallel and Distributed Computing 60 (4) (2000) 349– 352.

[5] J. Carriere, R. Kazman, WebQuery: searching and visualizing the web through connectivity, Proceedings of the Sixth Inter national Conference on the World wide Web, 1997.

[6] D. Dubois, H. Prade, F. Sedes, Fuzzy logic techniques in multimedia database querying: a preliminary investigation of the potentials, IEEE Transactions on Knowledge and Data Engineering 13 (3) (2001) 383– 392.

[7] D. Fensel, M.A. Musen, The semantic Web: a brain for humankind, IEEE Intelligent Systems (2001 (March/April)) 24–25.

[8] M.F. Goodchild, GIS and transportation: status and challenges, Geoinformatica 4 (2) (2000) 127–139.

[9] B. Huang, H. Lin, Design of a query language for accessing spatial analysis in the web environment, Geoinformatica 3 (2) (1999) 165–183.

[10] A. Juozapavicius, R.E. Blake, Indices and data structures in information systems, Informatica 10 (1) (1999) 71 – 88.

[11] B. Kao, J. Lee, C.Y. Ng, D. Cheung, Anchor point indexing in Web document retrieval, IEEE Transactions on SMC (Part C) 30 (3) (2000) 364– 373.

[12] M. Kobayashi, K. Takeda, Information retrieval on the web, ACM Computing Surveys 32 (2) (2000) 144– 173.

[13] D.H. Kraft, F.E. Petry, Fuzzy information systems: managing uncertainty in databases and information retrieval systems, Fuzzy Sets and Systems 90 (2) (1997) 183 – 191.

[14] D. Lidsky, R. Kwon, Searching the net, PC Magazine (1997 (Dec. 2)) 227– 258.

[15] A.V. Lotov, V.A. Bushenkov, A.V. Chernov, D.V. Gusev, G.K. Kamenev, Internet, GIS, and interactive decision maps, Journal of Geographic Information and Decision Analysis 1 (2) (1997) 118– 149.

[16] P. Martin, P.W. Eklund, Knowledge retrieval and the world wide web, IEEE Intelligent Systems (2000 (May/June)) 18 – 25.

[17] J. McCarthy, Phenomenal data mining, Communications of the ACM 43 (8) (2000) 75 – 79.

[18] B.E. Mennecke, Understanding the role of geographic information technologies in business: applications and research directions, Journal of Geographic Information and Decision Analysis 1 (1) (1997) 45– 69.

[19] K. Sakamura, N. Koshizuka, The eTRON wide-area distributed system architecture for e-commerce, IEEE MICRO 21 (6) (2001) 7 –13.

[20] K. Sakamura, N. Koshizuka, T-engine: the open real-time embedded systems platform, IEEE MICRO 22 (6) (2002).

[21] K. Sakamura, N. Koshizuka, T-engine: the open, real-time embedded systems platform for ubiquitous computing, Proc. of VLSI symposium, June 2003.

[22] B. Schilit, et al., Context-aware computing applications, Proc. of IEEE Workshop on Mobile Computing Systems and Applications, The IEEE Computer Society, Sta. Cruz, CA, 1994 (Dec.), pp. 85 – 90.

[23] H. Simon, Sinking your teeth into M-commerce, Intelligent Enterprise (2000 (Aug. 18)) 60– 63.

[24] T. Tezuka, R. Lee, Y. Kambayashi, H. Takakura, Models for conceptual geographical prepositions based on web resources, Journal of Geographic Information and Decision Analysis 5 (2) (2001) 83– 94.

[25] M. Weiser, The computer for the 21st century, Scientific American 265 (30) (1991) 94– 104.

[26] M. Williams, What makes rabbit run? Journal of Man-Machine Studies 2a (1) (1984) 333 – 352.

[27] R.R. Yager, On linguistic summaries of data, in: G. Piatetsky-Shapiro, B. Frawley (Eds.), Knowledge Discovery in Databases, MIT Press, 1991, pp. 347– 363.

[28] R.R. Yager, Database discovery using fuzzy sets, International Journal of Intelligence Systems 11 (1996) 691–712.

[29] S. Yau, et al., Reconfigurable context-sensitive middleware for pervasive computing, IEEE Pervasive Computing (2002) 33– 40.

[30] L.A. Zadeh, A computational approach to fuzzy quantifiers in natural language, Computer Mathematics and its Applications 9 (1983) 149–184.

[31] L.A. Zadeh, Toward a theory of fuzzy information granulation and its centrality in human reasoning and fuzzy logic, Fuzzy Sets and Systems 90 (2) (1997) 111– 127.

[32] L.A. Zadeh, From computing with numbers to computing with words—from manipulation of measurements to manipulation of perceptions, IEEE Transactions on Circuits and Systems 45 (1) (1999) 105– 119.

[33] L.A. Zadeh, A new direction in AI—toward a computational theory of perceptions, AI Magazine 22 (1) (2001) 73–84.

[34] L.A. Zadeh, From search engines to question-answering systems—the need for new tools, in advances in web intelligence, Proc. of AWIC 2003, Lecture Notes in Computer Science, vol. 2663, Springer-Verlag, 2003, pp. 15–17.

[35] http://www.searchenginewatch.com/sereport/99/11briefs.html.

[36] http://www.websearch.about.com/internet/webserch/library/ weekly/aa052199.htm.

[37] http://www.gpshome.ssc.nasa.gov.

[38] http://www.colorado.edu/geography/gcraft/notes/gps/gps<sup>\_</sup>f. html.

[39] http://www.gpsworld.com/gpsworld.

[40] http://www.aero.org/publications/GPSPRIMER.

[41] http://www.igscb.jpl.nasa.gov.

[42] http://www.utexas.edu/computer/pda.

[43] http://www.news.com.com/2100-1023-966536.html?tag= bplst.

[44] http://www.news.com.com/2100-1023-984722.html.

[45] http://www.SuperPages.com.

![](/api/attachments/9DXJWFDR/fulltext/images/1cbee11f4883cf93b14537d1705d360e5c4904b479a47ae97ebc497a8c9b32ad.jpg)

Dae-Young Choi is an associate professor in the Department of MIS at Yuhan College in Puchon City, South Korea. He received his BS, MS and PhD degrees in computer sciences from Sogang University, in 1985, 1992, and 1996, respectively. He was a research fellow at the Korea Institute for Defense Analyses (KIDA) from 1985 to 1990. He received postdoctoral fellowship from Korea Science and Engineering Foundation (KOSEF) in 2000.

He was with the BISC Group, Department of EECS, CS Division, University of California, Berkeley, as a visiting scholar, in 2001. He has been selected as a scholar to be sent abroad under the professor dispatching scheme by Korea Research Foundation (KRF) in 2004. He is with the Department of Computer Science and Engineering, University of Colorado at Denver as a visiting professor in 2004–2006. He has a national certificate of professional engineer for information processing systems. His research interests include mobile Web search engines, business intelligence, fuzzy systems, GDSS and personalized local Internet.
