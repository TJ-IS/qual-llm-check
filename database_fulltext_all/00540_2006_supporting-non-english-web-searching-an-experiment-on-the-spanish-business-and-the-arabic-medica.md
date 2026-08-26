---
otero_id: 540
otero_key: "HSCWWUSH"
title: "Supporting non-English Web searching: An experiment on the Spanish business and the Arabic medical intelligence portals"
authors: "Wingyan Chung; Alfonso Bonillas; Guanpi Lai; Wei Xi; Hsinchun Chen"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.02.015"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Supporting non-English Web searching: An experiment on the Spanish business and the Arabic medical intelligence portals

Wingyan Chung <sup>a,⁎</sup>, Alfonso Bonillas <sup>b,1</sup>, Guanpi Lai <sup>b,1</sup>, Wei Xi <sup>b,1</sup>, Hsinchun Chen <sup>b,1</sup>

<sup>a</sup> Department of Information and Decision Sciences, College of Business Administration, The University of Texas at El Paso, 500 W. University Avenue, El Paso, TX 79968, USA

<sup>b</sup> Artificial Intelligence Lab, Department of Management Information Systems, The University of Arizona, 1130 East Helen Street, McClelland Hall 430, Tucson, AZ 85721, USA

Received 3 March 2005; received in revised form 19 February 2006; accepted 22 February 2006 Available online 27 June 2006

## Abstract

Although non-English-speaking online populations are growing rapidly, support for searching non-English Web content is much weaker than for English content. Prior research has implicitly assumed English to be the primary language used on the Web, but this is not the case for many non-English-speaking regions. This research proposes a language-independent approach that uses meta-searching, statistical language processing, summarization, categorization, and visualization techniques to build high-quality domain-specific collections and to support searching and browsing of non-English information. Based on this approach, we developed SBizPort and AMedPort for the Spanish business and Arabic medical domains respectively. Experimental results showed that the portals achieved significantly better search accuracy, information quality, and overall satisfaction than benchmark search engines. Subjects strongly favored the portals' search and browse functionality and user interface. This research thus contributes to developing and validating a useful approach to non-English Web searching and providing an example of supporting decision-making in non-English Web domains.

Keywords: Internet; Web; Searching; Browsing; Business intelligence; Medical intelligence; Spanish; Arabic; Non-English Web searching; Web portal; Mutual information; Summarization; Categorization; Visualization; Kohonen self-organizing map

## 1. Introduction

The Internet has gained popularity worldwide and is estimated to continue to grow as access to Web content in different languages increases. A report published in

September 2004 shows that the majority (64.8%) of the world's online population consists of non-English speakers [13]. Moreover, that population was estimated to grow significantly in the near future to 820 million while the size of English-speaking online population was predicted to remain at 300 million [12]. For instance, there are more than 3.5 million Internet users in the Arab world [1] where the growth of Arabic Web content is estimated to double every year [28]. The Spanish-speaking online population has exceeded 9 millions and Latin America is estimated to have the fastest growing population in the world in the coming decades [2].

These statistics suggest a growing need for better support for Web searching in some non-English languages that individuals and organizations use on a daily basis. Non-English-speaking Internet users use their native language to search for useful information, and such searching typically happens across different regions where the language is used, as is the case for members of multinational organizations (MNOs) that have operations in multiple regions using the same language. These MNOs increasingly rely on the Internet when seeking information. An example might be searching for opportunities to expand a business in Latin America. A medical institution in an Arab region may need to discover efficient ways to collect, analyze, and disseminate massive information about different regions in the Middle East and North Africa.

Despite growing needs for non-English Web searching, most existing technologies have been developed for English-speaking users and fail to address the needs of non-English Web searching. Current search engines in Spanish and Arabic, for example, lack search and analysis capabilities. In particular, these search engines lack highquality collections to support searching across different regions. Better approaches to overcoming these problems would provide system developers with insights to enhance non-English Web searching. To address the needs, we propose in this paper a language-independent approach to building intelligent portals in non-English languages. Our goal was to develop and validate the approach to non-English Web searching. Based on the approach, we developed two Web search portals for the Spanish business and Arabic medical domains. We empirically studied the way these portals support decision-making and the related issues using native Spanish and Arab subjects.

The rest of the paper is structured as follows. Section 2 surveys previous research in non-English Web searching and search support in different languages. Section 3 presents a language-independent approach to supporting non-English Web searching and the two Web portals developed using the approach. Section 4 describes the methodology for evaluating the portals. Section 5 reports and discusses the findings. Section 6 concludes the paper and discusses future directions.

## 2. Literature review

Since the inception of the Internet, English has been the dominant language for communication on the Web. Prior research about Web searching has assumed implicitly that technologies are developed for Englishspeaking users. However, as more non-English-speaking users have adopted Internet technologies, other languages have gained popularity. It therefore is useful to review previous research in information seeking on the Web in a multilingual world. In particular, we also review developments of Web search technologies for the Spanishspeaking and Arabic-speaking regions.

## 2.1. Information seeking on the Web

Researchers who have studied information seeking on the Web have described the process of information seeking as consisting of various stages of problem identification, problem definition, problem resolution, and solution presentation [39]. Variations of this process model can be found in the literature [18,22,35].

Two major information-seeking activities are searching and browsing. Prior research has considered searching to include behaviors ranging from goal directed information searching, where the user has a specific target in mind, to more serendipitous or exploratory information browsing when no specific goal is present besides the intention to explore the information repository [35]. In directed searching, the user first decomposes his goal into smaller problems, then expresses his needs as concepts and higher level semantics, formulates queries using such supports as Boolean query languages and syntax directed editors, and finally evaluates the results by serial search or systematic sampling. In exploratory browsing, the user first transforms his general information need into a problem. He then (1) articulates that need as search terms or hyperlinks that appear on the system interface; (2) searches using the terms or explores the hyperlinks using such browse supports as automatic summarization, clustering and visualization tools, and Web directories; and (3) finally evaluates the results by scanning through them.

## 2.1.1. Support for Web searching and browsing

To support Web searching and browsing, various types of information technologies have been proposed. Metasearching has been found to be a promising method [4] to alleviate biases of search results from different search engines [26] by sending queries to multiple search engines and collating the set of top-ranked results from each engine. In addition, post-retrieval analysis provides added value to results returned by search engines. Previews and overviews of retrieved Web pages are important elements in post-retrieval analysis. A preview is extracted from, and acts as a surrogate for, a single object of interest [14]. Document summarization techniques provide previews of individual Web pages in the form of indicative summaries [10], query-biased summaries [36], or generic summaries [25]. An overview is constructed from and represents a collection of objects of interest [14]. Document categorization techniques such as the self-organizing map algorithm [17] have been used to categorize and search Web pages [5]. Document visualization techniques also have been used to amplify human cognition in browsing Internet search results [20,23]. Despite the potential advantages of meta-searching and information previews and overviews, they rarely have been applied to non-English search engines. One such application is the CBizPort that helps users to search, browse, categorize, and summarize Chinese business information [7] but does not contain a domain-specific collection and lacks useful functionality such as visualization.

## 2.1.2. Information quality

Information quality, a multifaceted concept, is considered to be an important aspect of evaluating the quality of a Web site [21] and is one that has been explored by Wang and Strong [38], who evaluated information quality using a set of 16 dimensions that were tested in [33]. These dimensions were for the most part used in evaluating the quality of information of organizations or companies, not the quality of information obtained from search engines. Although Marsico and Levialdi [24] have developed a Web site evaluation methodology that considers a site's information quality, their methodology was designed for evaluating general Web sites (e.g., travel information Web sites) and does not consider the special requirements of non-English Web searching.

There have been studies on cross-regional use of Chinese search engines (e.g., [7]), but because Chinese is mainly used in three geographically close regions (mainland China, Hong Kong, and Taiwan), its regional characteristics are less apparent than those of Spanish and Arabic, which are used across continents and widelyseparated regions. Unfortunately, no attempts have been made to study the cross-regional impacts of Spanish and Arabic search engines, evaluation of which could improve understanding of optimal design of search engines and portals.

## 2.2. Search engines for Spanish-speaking and Arabicspeaking regions

As more non-English-speaking people use the Internet to search and browse information, major search engines have attempted to expand their services for non-English speakers. Regional search engines that provide more localized searching have begun to emerge. In addition to English, these search engines typically accept queries in a user's native language and return pages from the regions being served. A survey of major search engines in Spanish and Arabic, two widely-used languages that are gaining popularity on the Web, follows.

## 2.2.1. Spanish search engines

Major search engines have been developed for Spanish, the second most popular language in the United States and the primary language for Spain and some 22 Latin American countries. Terra (http://www.terra.com/) offers its services to more than 3.1 million Internet users in Europe and the Americas. A Gallup poll in 2002 reported Terra to be the most popular search engine in Spain; Wanadoo (http://www.wanadoo.com/), a subsidiary of France Telecom, was rated second [11]. Currently, Terra serves more than 3 million Internet users in Spain, Latin America, the United States, and many European countries. Supporting Web searching in English and French as well as Spanish, Wanadoo is currently the leading Internet service provider in France and the United Kingdom with 9.3 million customers in June 2004.

Spanish search engines serving Latin America include Yahoo Español, Ahijuna, Auyantepui, Quepasa, Bacan, and Conexcol. Yahoo Español (Spain, http://espanol. yahoo.com/), the Spanish version of Yahoo, provides a human-compiled Web directory developed by about 150 editors who categorized over one million listed sites. YahooES also supplements its results with those from Inktomi and Google. Inktomi matches also appear to users after all YahooES matches have first been shown. Established in 1995, BIWE (Buscador en Internet para la web en Español, http://www.biwe.com/) is one of the earliest search engines for searching Spanish information on the Web. BIWE supports searching of news, products, images, and other information and provides a variety of services including a Web directory, email, entertainment, and market information for Hispanics. Headquartered in the United States, Quepasa (http://www.quepasa.com/) was launched in 1997 and is a bilingual Web portal (Spanish and English) serving Hispanic populations in the United States and Latin America. It uses proprietary Web search technologies to reduce the number of irrelevant results by utilizing terms most frequently used and documents most frequently viewed [32]. Quepasa also offers other services such as news, email, online radio, chat, online translation, forums, and Web hosting.

The following Spanish search engines primarily serve their own or adjacent regions. Launched in 1998, Ahijuna (Argentina, http://www.ahijuna.com.ar/) provides searching services of Argentina Web sites and other Spanish Web sites. It contains a Web directory with 14 categories having a total of 7578 hyperlinks. Based in

Venezuela, Auyantepui (http://www.auyantepui.com/) provides a searchable Web directory of Spanish sites. It grew from 14 categories listing 117 Web sites in 1996 to 550 categories with over 18,000 Web sites in 2002. Launched in 1998, Conexcol (Colombia, http://www. conexcol.com/) provides a searchable Web directory containing 14 categories having 400 subcategories and 13,214 Web sites' URLs. With more than 150,000 unique visitors per month, it is one of the top four most visited sites in Colombia. Bacan (Ecuador, http://www. bacan.com/), a major search engine in Ecuador, began its operations in 1996. It provides services such as news, email, online chat, entertainment, and shopping guides.

Every month Bacan has 80,000 individual visitors and generates over 2 millions hits. Ascinsa Internet (http:// www.ascinsa.com/) is widely-used in Peru and contains Web sites from Latin American countries and the United States. It provides services such as Internet access, email, Web page design, domain registration, Web hosting, among others. It also contains a directory listed by countries and then by domains.

Table 1 summarizes the content and functionality of major Spanish search engines. Although different types of information are provided, these search engines typically present results as a long textual list and lack post-retrieval analysis capabilities. Moreover, except for some large portals such as Yahoo Español, BIWE, and Terra, most Spanish search engines serve a few regions rather than an entire Spanish speaking community.

Comparing major Spanish search engines

<table><tr><td>Content</td><td colspan="2">Spain</td><td colspan="9">Latin America</td></tr><tr><td>Web pages and news on</td><td>Terra (Spain)</td><td>Wanadoo (France)</td><td>Auyantepui (Venezuela)</td><td>Ascinsa (Peru)</td><td>Conexcol (Colombia)</td><td>Bacan (Ecuador)</td><td>Quepasa (Mexico and U.S.)</td><td>YahooES (Spain)</td><td>Ahijuna (Argentina)</td><td>BIWE (Spain)</td><td></td></tr><tr><td>IT</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Business</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Government</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Financial</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Medical</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Other Latin American countries</td><td></td><td></td><td></td><td>√</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td></tr><tr><td>General</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Size of collection</td><td>Very good</td><td>Very good</td><td>Fair</td><td>Good</td><td>Good</td><td>Fair</td><td>Very good</td><td>Very good</td><td>Fair</td><td>Very good</td><td></td></tr><tr><td>Functionality</td><td>Terra (Spain)</td><td>Wanadoo (France)</td><td>Auyantepui (Venezuela)</td><td>Ascinsa (Peru)</td><td>Conexcol (Colombia)</td><td>Bacan (Ecuador)</td><td>Quepasa (Mexico and U.S.)</td><td>YahooES (Spain)</td><td>Ahijuna (Argentina)</td><td>BIWE (Spain)</td><td></td></tr><tr><td>Links to related resources</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Membership services</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Newsgroup search</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Web directory</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Search for Web sites</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Search stock prices</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td></tr><tr><td>Filtering for adult content</td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Online translation tool</td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Search for news</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Multimedia search (image, music, software, etc)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>User interface</td><td>Very good</td><td>Very good</td><td>Fair</td><td>Fair</td><td>Fair</td><td>Good</td><td>Very good</td><td>Very good</td><td>Fair</td><td>Very good</td><td></td></tr></table>

## 2.2.2. Arabic search engines

Arabic is spoken by more than 284 million people in about 22 countries. Although Arabic is the fifth most frequently spoken language in the world, the Arabic Web is still in its infancy, constituting less than 1% of the total Web content and having a low 2.2% penetration rate [1]. The cross-regional use of Arabic and the exponential growth of Arabic Web [28] nevertheless have highlighted the necessity of providing better Web searching and browsing.

Four major search engines offer the Arab World comprehensive services and extensive content coverage. Ajeeb (http://www.ajeeb.com/) is a bilingual Web portal (English/Arabic) launched in 2000 by Sakhr Software Company. Its database contains over one million searchable Arabic Web pages, which can be translated to English using the online version of Sakhr's machinetranslation software. In addition, Ajeeb has a multilingual dictionary and is known for its large Web directory, “Dalil Ajeeb,” which the company claims is the world's largest online Arabic directory. Ajeeb has launched Johaina, an automatic tool that gathers news from many Middle Eastern and worldwide news agencies. Using Sakhr's “IDRISI” search engine Johaina gathers mainly Middle East related news and categorizes them into primary and secondary topic categories. Albawaba.com (http://www. albawaba.com/) is a consumer portal offering comprehensive services including news, sports, entertainment, e-mail, and online chatting. The portal supports searching for both Arabic and English pages and the results are classified according to language and relevancy. Albawaba also provides meta-searching of other search engines (Google, Yahoo, Excite, Alltheweb, Dogpile) and a comprehensive directory of all Arab countries. Launched in 2000, UAE-based Albahhar (http://www.albahhar. com/) provides a wide range of online services such as searching, news, online chatting, and entertainment. The portal searches its 1.25 million Arabic Web pages and provides Arabic speakers a wide range of other online services like news, chat, and entertainment. Based in New Hampshire, Ayna (http://www.ayna.com/) is a Web portal providing an Arabic Web directory, an Arabic search engine, and other services such as a bilingual (English Arabic) email system, chat, greeting cards, personal homepage hosting, and personal commercial classifieds. In July 2001, Ayna had over 700,000 registered users and provided access to more than 25 million pages per month. Due to Ayna's popularity, Alexa Research ranks it among the top three leading Web sites in the Arab World.

Table 2  
Comparing major Arabic search engines

<table><tr><td>Content</td><td>Ajeeb</td><td>Albawaba</td><td>Albahhar</td><td>Ayna</td></tr><tr><td>Business</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Government</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Financial</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Medical</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>General</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Size of collection</td><td>Very good</td><td>Good</td><td>Very good</td><td>Very good</td></tr><tr><td>Functionality</td><td>Ajeeb</td><td>Albawaba</td><td>Albahar</td><td>Ayna</td></tr><tr><td>Encoding conversion (utf8-CP1256)</td><td></td><td></td><td></td><td>√</td></tr><tr><td>Links to related resources</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Membership services</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Web directory</td><td>Very good</td><td>Very good</td><td>Fair</td><td>Good</td></tr><tr><td>Search for Web sites</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Search by time period</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Search for news</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Languages of the search database</td><td>English/Arabic</td><td>English/Arabic</td><td>English/Arabic</td><td>English/Arabic</td></tr><tr><td>Cross-regional search support</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>User interface</td><td>Very good</td><td>Very good</td><td>Good</td><td>Good</td></tr><tr><td>System reliability</td><td>Fair</td><td>Fair</td><td>Poor</td><td>Very good</td></tr></table>

Table 2 compares the content and functionality of the Arabic search engines mentioned above. Despite their rich content and comprehensive services, Arabic search engines lack post-retrieval capability and their contents tend to be general, offering limited resources to serve domain-specific needs. They also fall short of supporting advanced search and browse functions. For example, none of them supports categorization or visualization of search results.

## 2.3. Summary

Because existing search engines in Spanish and Arabic typically lack analysis capabilities, they limit users' ability to understand retrieved results. The collections searched by these search engines are often regionspecific, so they do not provide a comprehensive understanding of the environment where they are operating. Major English search engines such as Google provide searching of non-English resources but fall short of covering domain- and region-specific information. There is a need for better approaches to overcoming these problems and to providing high-quality information to multinational organization users. We therefore propose a language-independent approach to address the following questions:

1. How can a language-independent approach support Web searching in non-English languages that are widely used across different regions?

2. How well do portals developed by the approach perform in comparison with existing search engines, in terms of accuracy, precision, recall, and user satisfaction?

3. When comparing with existing search engines, what is the information quality of the portals developed by the approach?

## 3. A language-independent approach

In this section, we describe a language-independent approach to supporting non-English Web searching. The approach uses meta-searching, statistical language processing, summarization, categorization, and visualization techniques to build high-quality domain-specific collections and to support searching and browsing of non-English information on the Web. Specifically, we used the approach to build two Web portals providing domainspecific collections for non-English Web searching and post-retrieval analysis for the Spanish business and Arabic medical domains. Because the implementation of the approach requires no (or minimal) customization to the portals' languages, it allows system developers to easily adapt the development to new languages and domains.

## 3.1. The SBizPort and AMedPort

The chosen domains of the two portals, Spanish Business Intelligence Portal (SBizPort) and Arabic Medical Intelligence Portal (AMedPort), represent important segments of the Web of interest to individual users and multinational organizations. Given the growing Spanish-speaking populations in the United States, Spain, and Latin America, businesses actively expand their opportunities by seeking information on the Web. Meanwhile, the growing Arabic online population and medical professionals seek a comprehensive, one-stop Web portal through which to communicate medical information among different Arab regions. The SBizPort and AMedPort were developed to address these growing needs. In addition to providing relevant information, the portals support intelligence gathering and analysis, where intelligence is defined as the product of acquisition, interpretation, collation, assessment, and exploitation of information in the respective domains [6]. The intelligence is presented in the forms of collated search results obtained from various high-quality information sources, Web page summaries, categorized search results, and visual maps showing clusters of Web pages. Table 3 provides topical coverage details of the two portals, screen shots of which are shown in Figs. 1 and 2.

## 3.2. Steps in the approach

Our approach consists of five major steps, which are described in the context of building SBizPort and AMedPort.

Table 3  
Topical coverage details of the two portals

<table><tr><td>Topics</td><td>SBizPort</td><td>AMedPort</td></tr><tr><td>Scenario</td><td>The user searches for Spanish Web pages about electronic commerce.</td><td>The user searches for Arabic medical information about excretion.</td></tr><tr><td>Search page</td><td>The query “electronic commerce” is used (Fig. 1(a)).</td><td>The query “excretion” is used (Fig. 2(a)).</td></tr><tr><td>Result page</td><td>Approximately 40 results from 4 meta-searchers (top 10 from each) are displayed (Fig. 1(b)).</td><td>Approximately 30 results from 4 meta-searchers (top 10 or fewer from each) are displayed (Fig. 2(b)).Examples of the results include “middle ear infection” and “skin symptoms of diabetes.”</td></tr><tr><td>Categorizer</td><td>The categorizer groups retrieved Web pages into 20 folders, among which are labeled “customs agent,” “electronic commerce,” and “foreign commerce” (Fig. 1(c)).</td><td>Examples of categories include “children’s education” and “sports.”The user selects the seventh category titled “special education,” within which he browses 2 Web pages about “questions and answers” (Fig. 2(c)).</td></tr><tr><td>Summarizer</td><td>The summarizer provides a 3-sentence summary of the circled result that contains information on an e-commerce event held in 2000 in Caracas, Venezuela (Fig. 1(d)).</td><td>The 3-sentence summary is listed on the left while the original page about petrochemical information is displayed on the right (Fig. 2(d)).</td></tr><tr><td>Visualizer</td><td>The SOM visualizer categorizes about 40 Web pages onto 2 regions labeled “foreign commerce” and “international commerce” and displays hyperlinks on the right (Fig. 1(e)).</td><td>The SOM visualizer categorizes about 30 Web pages onto 6 regions and displays hyperlinks on the right (Fig. 2(e)). Examples of the regions include “special education” and “sports.”</td></tr></table>

![](/api/attachments/HSCWWUSH/fulltext/images/e6aecc51af0db08ef81e159b66c8394a7f06f9c3a4e5e6311dd4c222cf849480.jpg)  
Fig. 1. Screen shots of SBizPort.

## 3.2.1. Collection building and searching

Figs. 1(a), 1(b), 2(a), and 2(b) show the search and result pages of the two portals. On the search page, a user can input keywords and choose whether to search, organize, or visualize the results. The user can input multiple keywords separated by line breaks and can choose among a number of carefully selected information sources from the Spanish or Arab regions by checking the boxes. The result page lists search results according to the information sources selected by the user.

![](/api/attachments/HSCWWUSH/fulltext/images/b5811df77689a47f22371c7b61040ee0b08682f2e2d4e1e66828600bef2c0214.jpg)  
Fig. 2. Screen shots of AMedPort.

To provide high-quality information, we manually analyzed the existing information sources in the two domains. For the Spanish business domain, key business categories such as e-commerce, international business, and competitive intelligence were searched to obtain seed URLs (translated into English), that were used for domain spidering/collecting of Web pages. More than 183 seed URLs were obtained. A Web crawler then followed these URLs to collect pages automatically. The pages were then automatically indexed and stored in our database. In addition to domain spidering, we performed meta-spidering of six major search engines (Yahoo ES, Ahijuna, Conexcol, Ambdirecto, Auyantepui, and Teoma) using queries translated from English queries that previously had been used to build an English business intelligence search portal [23]. We chose these search engines because of their rich Spanish business content. The Spanish business collection obtained from this method contained more than 476,084 Web pages covering more than 22 countries.

Similarly, our Arabic medical collection was built by using 105 seed URLs collected from seven major search engines (Google, Yahoo, AlltheWeb, Ajeeb, ArabVista, AltaVista, and DMOZ) and by meta-spidering these URLs using keywords from an Arabic medical glossary [16]. The results are then filtered depending on their number and quality. The resulting Arabic medical collection contained more than 220,000 Web pages covering more than 22 countries.

Apart from searching its own database, the SBizPort supports meta-searching two domain-specific databases (SBizPort collection and AMBDirecto) and six Spanish general search engines (Yahoo Español, Terra, Ahijuna, Auyantepui, Bacan, and Ascinsa). The AMedPort supports meta-searching three domain-specific databases (AMedPort, Sehha.com, and ArabMedmag.com) and three Arabic general search engines (Ba7th.com, ArabVista.com, and Ayna). These meta-search engines were chosen because of their rich content and domainspecific coverage. A virtual keyboard provided for AMedPort facilitates input (see Fig. 2(a)).

## 3.2.2. Summarizer

The SBizPort and AMedPort summarizers were modified from an English summarizer that uses sentenceselection heuristics to rank text segments [25]. These heuristics strive to reduce redundancy of information in a query-based summary [3]. The summarization takes place in three main steps: (1) sentence evaluation, (2) segmentation or topic identification and (3) segment ranking and extraction. First, a Web page to be summarized is fetched from the remote server and parsed to extract its full text. All sentences are extracted by identifying punctuation serving as periods. Important information such as presence of cue phrases (e.g., “therefore,” “in summary” in the respective languages), sentence lengths and positions are also extracted for ranking the sentences. Second, we use the Text-Tiling algorithm [15] to analyze the Web page and determine topic boundaries. A Jaccard similarity function is used to compare the similarity of different blocks of sentences. Third, we rank document segments identified in the previous step according to the ranking scores obtained in the first step and key sentences are extracted as summary. The summarizer can summarize Web pages flexibly, using three or five sentences. Users can invoke it by clicking the number of sentences for summarization under each result. Then, a new window is activated (shown in Figs. 1(d) and 2(d)), that displays the summary and the original Web page.

## 3.2.3. Categorizer

The SBizPort and AMedPort categorizers organize the Web pages (related to the query shown on top) into 20 (or fewer) folders labeled by the key phrases appearing most frequently in the page summaries or titles (see Figs. 1(c) and 2(c)). Each categorizer relies on a phrase lexicon in the relevant language to extract phrases from Web page summaries obtained from meta-searching or searching our collections. To create the lexicons, we collected a large number of Web pages in the two domains. From each collection of pages, we extracted meaningful phrases by using the mutual information approach, a statistical method that identifies significant patterns as meaningful phrases from a large amount of text in any language [30]. The approach is an iterative process of identifying significant lexical patterns by examining the frequencies of word co-occurrences in a large amount of text.

The mutual information (MI) algorithm is used in the approach to compute how frequently a pattern appears in the corpus, relative to its sub-patterns. Based on the algorithm, the MI of a pattern $c \left( \mathrm { M I } _ { c } \right)$ can be found by

$$
\mathrm{MI} _ {c} = \frac {f _ {c}}{f _ {\mathrm{left}} + f _ {\mathrm{right}} - f _ {c}}
$$

where f stands for the frequency of a set of words. Intuitively, $\mathrm { M I } _ { c }$ represents the probability of cooccurrence of pattern c, relative to its left sub-pattern and right sub-pattern. Phrases with high MI are likely to be extracted and used in automatic indexing. For example, if the Spanish phrase “gerencia del conocimiento” (knowledge management) appears in the corpus 100 times, the left sub-pattern (gerencia del) appears 110 times and the right sub-pattern (del conocimiento) appears 105 times, then the mutual information (MI) for the pattern “gerencia del conocimiento” is 100 / (110 + 105−100)= 0.87. In addition, we employed an updateable PAT-tree data structure developed in [30] that supports online frequency update after removing extracted patterns to facilitate subsequent extraction. Repetitive removal of sub-patterns therefore is not necessary. In addition, we used a stop word list and manual filtering to refine the results obtained.

Using the approach, we extracted 19,417 phrases from the SBizPort collection and 68,079 phrases from the AMedPort collection. The categorizer then uses these phrases to categorize the Web pages nonexclusively (see Figs. 1(c) and 2(c)).

## 3.2.4. Visualizer

The resulting portals also support visualization of Web pages retrieved using a Kohonen self-organizing map (SOM) algorithm [17] to categorize and place Web pages onto a two-dimensional jigsaw map [23] (see Figs. 1(e) and 2(e)). SOM is a neural networks algorithm that has been used in image processing and pattern recognition applications. When applied to automatic categorization and visualization of Web pages, SOM assigns similar pages to adjacent regions with each region labeled by the most frequently occurring phrases extracted by the mutual information approach described. The larger the size of a region on the map, the more the Web pages are assigned to it. Users can click on a region to see a list of pages on the right and can open pages by clicking the link-embedded titles.

## 3.2.5. Web directory

In addition, each of our portals provides a Web directory of the resources in its specific domain. Organized in a hierarchical manner, the directory was built from a combination of human identification and meta-searching. The Spanish business directory contains 295 categories and the Arabic medical directory contains 232 categories. Both have a depth of 5 levels.

## 3.3. Enhancements of the approach

We believe that the proposed approach offers benefits and new enhancements in five aspects: (1) New integration of existing techniques: Although some of the techniques used in the approach have been studied in prior work, we have not found a comprehensive approach that addresses the problem of information quality on the Web and the need for Web searching in languages used in widely separated geographic regions (e.g., Spanish and Arabic). By integrating human analysis with existing techniques for text processing, our approach was developed to alleviate information overload in searching and browsing Web content in non-English languages. For example, we have customized the Kohonen self-organizing map algorithm to the Spanish business and Arabic medical domains to support dynamic visualization of Web pages. This integration of visualization technique has been enhanced from our previous work [6,23] by considering languages (Spanish and Arabic) used widely in a multitude of geographic regions and by applying the technique to non-English domains. To our knowledge, there has been no previous attempt to integrate the technique into an application similar to the portals described here. (2) Collection building: Previous work on building Web collections typically focuses on English content due to the more abundant resources available. To deal with the challenge of supporting non-English Web searching, our proposed approach was used to build non-English Web collections encompassing wide arrays of geographic regions and content providers. For example, the SBiz-Port collection was built from spidering more than 183 Spanish business Web sites located in such regions as Argentina, Bolivia, Central America, Chile, Colombia, Ecuador, Spain, Mexico, Paraguay, Peru, Uruguay, and Venezuela. The AMedPort collection covered Web resources obtained from such regions as Saudi Arabia, Bahrain, Lebanon, Tunisia, Kuwait, Egypt, United Arab Emirates, Switzerland, United Kingdom, USA, Russia, and Canada. While existing search engines in those regions mainly provide regional services, the SBizPort and AMedPort collections respectively serve the entire communities that use Spanish and Arabic in Web searching. The collections also represent new advances over the English business collection built in [23] and the lack of its own Web collection in [6]. (3) Language processing: To extract meaningful phases as input for the categorizer and visualizer, we used the mutual information technique that considered the co-occurrence of terms in a large corpus (see Section 3.2.3). Because the approach used the probabilities of the terms appearing in the corpus rather than their linguistic patterns as the criterion for extraction, the technique was statistics-based and hence different from linguistic techniques used in previous research (e.g., [23]). Comparing with our previous work [6] (in which the system only served three closely-located geographic regions (China, Taiwan, and Hong Kong)), we have enhanced the performance of this technique by using a large number of Web pages from different regions as our corpus and by testing the technique in the two chosen languages. (4) User interface customization: The user interface interfaces of SBizPort and AMedPort were specially designed to bring about the industry features and to address the language-specific needs. For example, AMedPort provides a virtual keyboard to

Table 4

assist in the input of the right-to-left Arabic language. The images in SBizPort user interface are related to major industries in Latin America. (5) Application domains: This research has extended to domains such as Arabic medicine and Spanish business that are less explored in prior work. As the online populations in these two languages will grow significantly (see Section 1), this work thus helps system developers to easily customize their development to the particular language they consider. We believe that our approach can help multinational organizations to search effectively for non-English information on the Web.

## 4. Evaluation methodology

In this section, we describe our methodology for evaluating the usability of the Web portals developed by our approach. Our evaluation objectives are: (1) to study how the Web portals developed by our approach can assist searching and browsing of specialized domains on the Web; (2) to compare our portals with existing search engines in order to understand the effectiveness and efficiency of our portals; and (3) to evaluate the information quality and user satisfaction achieved by using our portals.

To achieve objective (1), we invited human subjects to use our portals to search and browse the Spanish business or Arabic medical domains, two specialized domains that do not have as much coverage on the Web as their English counterparts. To achieve objective (2), we selected BIWE and Ayna as benchmarks against which to compare SBizPort and AMedPort because of their comprehensive coverage and functionality. BIWE (http://www.biwe.com/) is a major Spanish search engine providing information for the Spanish-speaking community. It also has a detailed Web directory for users to browse topics in which they are interested. Compared with other Spanish search engines, BIWE's services are more comprehensive and target more closely to Hispanics. As one of the most visited Arab Internet hubs, Ayna (http://www.ayna.com/) serves Arabicspeaking people of the Middle East and North Africa. Unlike many Arabic search engines, Ayna is more stable and reliable that serves as a good benchmark to support a fair comparison with AMedPort. To achieve objective (3), we asked subjects to provide subjective rating and comments on information quality and user satisfaction.

## 4.1. Experimental design

We designed scenario-based search and browse tasks consistent with Text Retrieval Conference standards [37] to evaluate the performance of our Web portals. For example, a scenario for testing SBizPort was “America Online (AOL) in Latin America,” where a search task was “When was AOL Latin America launched in the United States?” and a browse task was “Find the URLs of financial portals where you can find stock quotes on America Online.” In a scenario for testing AMedPort “Prevention and treatment of cancer,” a search task was “Give the name of one vitamin that helps to prevent cancer,” and a browse task was “Find articles about healthy diet and cancer prevention.” To further validate the relevance of tasks, before conducting the actual experiment we did a pilot test with three subjects for each portal.

We recruited 19 Spanish students and 11 Arab students as volunteer subjects to evaluate the performance of the SBizPort and AMedPort. In each one-hour experiment, we introduced two systems (our portal and the benchmark system) to a subject and randomly assigned different scenarios to evaluate the systems. Each scenario contained two search tasks and one browse task. To test the impact of the domain-specific collection, we asked the subjects not to use the collection in the first task when using our portal but to use it in the second task. In the third task, we asked the subjects to use the SOM visualizer when using our portal and to use the available browse tools (e.g., hyperlinks, Web directory) when using the benchmark search engine (see Table 4). Although we did not impose any time limit on completing the tasks, we found that each subject spent an average of three minutes to finish a search task and eight minutes to finish a browse task. The order in which the systems were used was randomly assigned to avoid bias due to sequence of use.

After using a system, a subject filled in a post-session questionnaire about his ratings and comments on the system. The experimenter recorded all verbal comments or behavioral observations that were later analyzed using protocol analysis [9]. Upon finishing the study, each subject also filled in a post-study questionnaire to rate each system in terms of information quality and overall satisfaction and to provide additional feedback.

A summary of the experimental setup

<table><tr><td>System</td><td>Scenario</td><td>Task</td><td>Task type</td></tr><tr><td rowspan="2">1</td><td rowspan="2">First</td><td>1 and 2</td><td>Search</td></tr><tr><td>3</td><td>Browse</td></tr><tr><td rowspan="2">2</td><td rowspan="2">Second</td><td>4 and 5</td><td>Search</td></tr><tr><td>6</td><td>Browse</td></tr></table>

The systems and scenarios were randomly assigned to subjects.

The questionnaire was developed based on the user satisfaction measures used in [8,19]. We asked the subjects to rate their satisfaction on each system along a seven-point Likert scale.

To measure information quality, we modified the 16-dimension construct developed in [38] by dropping the “security” dimension which is not relevant because the information provided by the systems is already public. To accommodate the different levels of importance in the remaining 15 dimensions, we invited two experts to provide ratings on the relative importance of different dimensions in the two domains (see Table 5). The Spanish business expert is a senior executive of a management consulting company in Mexico. Being a native Spanish speaker, he had 24 years of experience in business development, raising capital, negotiations, finance, and strategic planning. He also had worked as the Vice President of Business Development for the Gallup Organization in Mexico. The Arabic medical expert is an Arab microbiology Ph.D. student at a major research university in the United States. These experts provided answers that we used to judge subjects' performances in the tasks.

The subjects also provided demographic information, which was kept confidential in accordance with the Institutional Review Board Guidebook [31].

## 4.2. Hypothesis testing

Because the Web portals developed by our approach encompassed Web resources from different Spanish or Arab regions, we believed that they would provide richer content and higher usability than those of benchmark systems. Users could thus find relevant results more quickly from our portals. With respect to the two domains, we tested the following five sets of hypotheses, none of which had been explored in previous research.

H1. Using a domain-specific collection in SBizPort/ AMedPort enables users to achieve higher effectiveness and efficiency than performing search tasks without its support.

H2. SBizPort/AMedPort enables users to achieve higher effectiveness and efficiency than relying on benchmark search engines for searching.

H3. The use of SOM visualizer in SBizPort/AMedPort enables users to achieve higher effectiveness and efficiency than using benchmark search engines to perform browse tasks.

H4. SBizPort/AMedPort users achieve a higher overall satisfaction than users of a benchmark search engine.

Table 5  
Definitions of 15 dimensions of information quality and expert ratings

<table><tr><td rowspan="2">Dimension</td><td rowspan="2">Definition</td><td colspan="2">Expert ratinga</td></tr><tr><td>Spanish</td><td>Arab</td></tr><tr><td colspan="4">Presentation quality and clarity</td></tr><tr><td>Accessibility</td><td>The extent to which information is available, or easily and quickly retrievable</td><td>3</td><td>3</td></tr><tr><td>Concise representation</td><td>The extent to which information is compactly represented</td><td>3</td><td>3</td></tr><tr><td>Consistent representation</td><td>The extent to which information is presented in the same format</td><td>3</td><td>3</td></tr><tr><td>Ease of manipulation</td><td>The extent to which information is easy to manipulate and apply to different tasks</td><td>3</td><td>2</td></tr><tr><td>Interpretability</td><td>The extent to which information is in appropriate languages, symbols, and units, and the definitions are clear</td><td>2</td><td>3</td></tr><tr><td colspan="4">Coverage and reliability</td></tr><tr><td>Appropriate amount of information</td><td>The extent to which the volume of information is appropriate for the task at hand</td><td>2</td><td>3</td></tr><tr><td>Believability</td><td>The extent to which information is regarded as true and credible</td><td>2</td><td>2</td></tr><tr><td>Completeness</td><td>The extent to which information is not missing and is of sufficient breadth and depth for the task at hand</td><td>3</td><td>3</td></tr><tr><td>Free-of-error</td><td>The extent to which information is correct and reliable</td><td>2</td><td>3</td></tr><tr><td>Objectivity</td><td>The extent to which information is unbiased, unprejudiced, and impartial</td><td>2</td><td>3</td></tr><tr><td colspan="4">Usability and analysis quality</td></tr><tr><td>Relevancy</td><td>The extent to which information is applicable and helpful for the task at hand</td><td>3</td><td>3</td></tr><tr><td>Reputation</td><td>The extent to which information is highly regarded in terms of its source or content</td><td>3</td><td>3</td></tr><tr><td>Timeliness</td><td>The extent to which information is sufficiently up-to-date for the task at hand</td><td>3</td><td>3</td></tr><tr><td>Understandability</td><td>The extent to which information is easily comprehended</td><td>3</td><td>2</td></tr><tr><td>Value-added</td><td>The extent to which information is beneficial and provides advantages from its use</td><td>3</td><td>3</td></tr></table>

Expert rating: 3 = extremely important, 2 = very important, 1 = important.

H5. SBizPort/AMedPort provides higher information quality than a benchmark search engine.

To test H1, we compared the performances of using (task 2) and not using (task 1) our domain-specific collections. To test H2, we compared the search performances of our portal and the benchmark search engine. To test H3, we compared browse performances of using our portal's SOM visualizer and the benchmark search engine's browse support tools. Because a previous research [7] has conducted a focused evaluation on the use of summarizer and categorizer to support Web searching and browsing, we did not repeat the evaluation of these tools here. To test H4 and H5, we compared subjects' ratings on the aforementioned aspects. As each subject was asked to perform similar tasks using the two systems, we used a one-factor repeated-measures design, which gives greater precision than designs that employ only between-subjects factors [27].

## 4.3. Performance measure

We recorded the time the subject spent on each task to measure the efficiency of using a system. We also measured the effectiveness of using a system by the following formulae:

$$
\text { Accuracy } = \frac {\text { Number   of   correctly   answered   parts }}{\text { Total   number   of   parts }}
$$

$$
\text { Precision } = \frac {\text { Number   of   relevant   URLs   identified   by   the   subject }}{\text { Number   of   all   URLs   identified   by   the   subject }}
$$

$$
\text { Recall } = \frac {\text { Number   of   relevant   URLs   identified   by   the   subject }}{\text { Number   of   relevant   URLs   identified   by   the   expert }}
$$

$$
F \text {   value   } = \frac {2 \times \text { Recall } \times \text { Precision }}{\text { Recall } + \text { Precision }}
$$

Accuracy reflects how well a system finds correct answers for search tasks. To measure the browse task performance, we used precision, recall, and F value. Precision reflected how well the portal helped users find relevant results and avoid irrelevant results. Recall reflected how well the portal helped users find all the relevant results that had been identified by experts. F value was used to balance recall and precision simultaneously [34], reflecting the performances achieved by the expert and by subjects.

## 5. Experimental results and discussions

In this section, we report and discuss the results of our user evaluation study. Table 6 summarizes the means and standard deviations of various performance measures. Table 7 shows the p-values and results of testing various hypotheses. Table 8 summarizes subjects' demographic profiles.

## 5.1. SBizPort performance

## 5.1.1. Search performance

Using SBizPort's domain-specific collection achieved higher mean accuracy and lower mean efficiency than not using it. However, the differences were not significant. The figures show that employing our domain-specific collection resulted in performance comparable to that achieved by using all the meta-search engines in combination, suggesting the comprehensive nature of our collection. We nevertheless believe that the SBizPort collection should be further enhanced to provide more comprehensive results in a shorter time, so H1 was not confirmed.

Comparing our portal with the benchmark search engine, we found that the mean accuracy of SBizPort was significantly higher than that of BIWE, while there was no significant difference between the efficiencies achieved by the two systems. We believe that SBizPort's ability to provide comprehensive, high-quality information from many sources helped users get accurate results. However, the efficiency of SBizPort was not significantly better than that of BIWE. Because SBizPort is a research prototype, it lacks the professional operations of BIWE. Therefore, H2 was partially confirmed.

## 5.1.2. Browse performance

We found that SBizPort achieved a higher mean precision, recall, and F value than BIWE. However, only the difference in F value was significant at a 5% alpha-error level and the difference in recall was significant at a 6% alpha-error level. The results show that SBizPort's browse support tools and SOM visualizer could enable users to find more relevant results than BIWE. However, there is still room for improvements in terms of efficiency and precision. Therefore, H3 was partially confirmed.

## 5.1.3. User ratings and comments

Subjects rated SBizPort more favorably than BIWE in terms of information quality and overall satisfaction (see Table 6). The mean differences between the two systems' ratings ranged from 0.6 to 1.5 and were all significant at a 5% alpha-error level. Subjects were very satisfied with SBizPort. We believe that several aspects of SBizPort contributed to its good performance: the high-quality meta-searchers and domain-specific collection used in SBizPort, the useful browse support tools, and the comprehensive content coverage. H4 and H5 were confirmed.

Means and standard deviations of different measures

<table><tr><td rowspan="2" colspan="3">Measure</td><td colspan="2">SBizPort</td><td colspan="2">BIWE</td><td colspan="2">AMedPort</td><td colspan="2">Ayna</td></tr><tr><td> $Mean^a$ </td><td>S.D.</td><td> $Mean^a$ </td><td>S.D.</td><td> $Mean^a$ </td><td>S.D.</td><td> $Mean^a$ </td><td>S.D.</td></tr><tr><td rowspan="2">Task 1</td><td rowspan="2"> $Search\ performance^b$ </td><td> $Accuracy^c$ </td><td>0.87</td><td>0.33</td><td>0.55</td><td>0.50</td><td>0.64</td><td>0.50</td><td>0.23</td><td>0.41</td></tr><tr><td> $Efficiency^d$ </td><td>131</td><td>43</td><td>149</td><td>48</td><td>141</td><td>45</td><td>146</td><td>37</td></tr><tr><td rowspan="2">Task 2</td><td rowspan="2"> $Search\ performance^b$ </td><td>Accuracy</td><td>0.95</td><td>0.23</td><td>0.55</td><td>0.50</td><td>0.50</td><td>0.50</td><td>0.18</td><td>0.40</td></tr><tr><td> $Efficiency^d$ </td><td>134</td><td>59</td><td>151</td><td>37</td><td>141</td><td>45</td><td>174</td><td>19</td></tr><tr><td rowspan="4">Task 3</td><td rowspan="4"> $Browse\ performance^e$ </td><td>Precision</td><td>0.87</td><td>0.29</td><td>0.86</td><td>0.34</td><td>0.43</td><td>0.37</td><td>0.27</td><td>0.41</td></tr><tr><td>Recall</td><td>0.21</td><td>0.14</td><td>0.13</td><td>0.085</td><td>0.26</td><td>0.21</td><td>0.12</td><td>0.18</td></tr><tr><td>F value</td><td>0.78</td><td>0.38</td><td>0.48</td><td>0.49</td><td>0.24</td><td>0.23</td><td>0.11</td><td>0.21</td></tr><tr><td> $Efficiency^d$ </td><td>288</td><td>63</td><td>285</td><td>24</td><td>289</td><td>26</td><td>300</td><td>24</td></tr><tr><td colspan="3">Information quality (overall)</td><td>2.1</td><td>0.66</td><td>2.9</td><td>1.07</td><td>2.6</td><td>1.1</td><td>4.7</td><td>1.0</td></tr><tr><td colspan="3">– Presentation quality and clarity</td><td>2.3</td><td>0.78</td><td>2.9</td><td>1.3</td><td>2.4</td><td>1.0</td><td>4.5</td><td>1.2</td></tr><tr><td colspan="3">– Coverage and reliability</td><td>2.2</td><td>0.63</td><td>3.0</td><td>1.1</td><td>2.9</td><td>1.3</td><td>5.0</td><td>0.87</td></tr><tr><td colspan="3">– Usability and analysis quality</td><td>1.98</td><td>0.76</td><td>2.9</td><td>1.1</td><td>2.4</td><td>1.2</td><td>4.6</td><td>1.2</td></tr><tr><td colspan="3">Overall satisfaction</td><td>1.8</td><td>0.76</td><td>3.1</td><td>1.7</td><td>2.2</td><td>1.3</td><td>4.9</td><td>1.8</td></tr></table>

<sup>a</sup> The range of rating is from 1 to 7, with 1 being the best.  
<sup>b</sup> When using our portals, the subjects were asked not to use our domain-specific collection in task 1 but used it in task 2.  
<sup>c</sup> In task 1, the “SBizPort” or “AMedPort” column refers to using domain-specific collection and the right column (“Benchmark”) refers to not using domain-specific collection.  
<sup>d</sup> Efficiency was measured by the time (in seconds) used.  
<sup>e</sup> In task 3, the subjects were asked to use the SOM visualizer when using our portals and could use all available browse tools when using the benchmark search engines

The subjects provided many positive comments on SBizPort's search and browse capabilities. Twelve subjects agreed that SBizPort was very useful for searching Spanish business information. For instance, subject #s10 said that SBizPort “is very useful for searching,” and “(the information) is clear.” Subject #s1 said “For specific topics (SBizPort) gave out specific results, making the searches better than other search engines.” The subjects also liked the browse support tools provided by SBizPort. A majority of seventeen subjects commented positively on it. For example, subject #s6 said that SBizPort was “really nice to have different functions and have a catalog.” Subject #s18 said that the browse tools “made it easy to view retrieved data.” Regarding the search performance, fifteen subjects commented that SBizPort did a good job or has a greater variety than the benchmark search engine. For example, subject #s7 said: “(SBizPort) gives lots of pages related to what I look for from different countries.” Subject #s10 said “(SBizPort) looks with more information and (is) able to provide in detail.” However, five subjects complained about the low speed of the system, especially when retrieving information from many meta-searchers.

On the other hand, the subjects were unhappy with BIWE's lack of relevance and clarity in searching and browsing. For example, subject #s7 said that BIWE “gives irrelevant pages (of) other countries I'm not interested in.” Subject #s9 said that it was “timeconsuming” to use BIWE. Moreover, most users did not like the presence of pop-up advertisements when using BIWE. Nevertheless, six subjects said that BIWE was useful for searching Spanish business information. Three subjects commented that the system was easy to use and fast.

p-values of testing various hypotheses (alpha error\* = 0.05)

<table><tr><td colspan="2">Comparison</td><td colspan="2">SBizPort vs. BIWE</td><td colspan="2">AMedPort vs. Ayna</td><td rowspan="2">Result</td></tr><tr><td>Hypothesis</td><td>Measure</td><td>Effectiveness</td><td> $Efficiency^a$ </td><td>Effectiveness</td><td> $Efficiency^a$ </td></tr><tr><td>H1</td><td>Accuracy</td><td>0.42</td><td>0.85</td><td>0.54</td><td>0.83</td><td>Not confirmed</td></tr><tr><td>H2</td><td>Accuracy</td><td>0.002*</td><td>0.30</td><td>0.046*</td><td>0.011*</td><td>Partially confirmed</td></tr><tr><td>H3</td><td>Precision</td><td>0.89</td><td>0.84</td><td>0.22</td><td>0.31</td><td>Partially confirmed</td></tr><tr><td></td><td>Recall</td><td>0.06</td><td></td><td>0.09</td><td></td><td></td></tr><tr><td></td><td>F value</td><td>0.035*</td><td></td><td>0.07</td><td></td><td></td></tr><tr><td>H4</td><td>Satisfaction</td><td>0.005*</td><td></td><td>0.000*</td><td></td><td>Confirmed</td></tr><tr><td>H5</td><td>Information quality (overall)</td><td>0.009*</td><td></td><td>0.000*</td><td></td><td>Confirmed</td></tr></table>

<sup>a</sup> Efficiency was measured by the time (in seconds) used.  
⁎ p valuesV0.05.

Table 8  
Subjects' demographic profile

<table><tr><td>Demographic information</td><td>Spanish subjects (total: 19)</td><td>Arab subjects (total: 11)</td></tr><tr><td>Country of origin</td><td>Mexico (12), USA (3), Panama (1), Puerto Rico (1), Colombia (1), Peru (1)</td><td>Lebanon (7), Morocco (1), Iraq (1), Mauritania (1), Jordan (1)</td></tr><tr><td>Education</td><td>Undergraduate (13), bachelor earned (2), master earned (3), doctorate earned (1)</td><td>Undergraduate (3), associate degree (1), bachelor earned (2), master earned (5)</td></tr><tr><td>Age range</td><td>18–25 (14), 26–30 (2), 31–35 (2), 41–50 (1)</td><td>18–25 (6), 26–30 (3), 36–40 (1), 41–50 (1)</td></tr><tr><td>Gender</td><td>Female (10), male (9)</td><td>Female (3), male (8)</td></tr><tr><td>Hours of using computer per week</td><td>&lt;5 (1), 5–10 (2), 10–15 (1), 15–20 (3), 20–25 (9), 30–35 (1), &gt;40 (2)</td><td>5–10 (1), 10–15 (3), 15–20 (1), 20–25 (2), 25–30 (1), 30–35 (1), &gt;40 (2)</td></tr></table>

## 5.2. AMedPort performance

## 5.2.1. Search performance

Using AMedPort's collection resulted in higher mean accuracy and efficiency than not using it. However, similarly to SBizPort, the differences were not significant. We believe that the AMedPort collection should be improved to provide more comprehensive results to users in a shorter time. H1 was not confirmed.

Comparing our portal with the benchmark search engine, we found that the mean accuracy and efficiency of AMedPort were significantly higher than those of Ayna. We believe that, like SBizPort, AMedPort provided comprehensive, high-quality information from many sources and helped users find correct results in a shorter time. H2 was confirmed.

## 5.2.2. Browse performance

Contrary to our expectation, AMedPort achieved performance comparable to that of Ayna, as shown by insignificant differences in precision, recall, and F value. Yet, at 7% and 10% alpha-error levels, AMedPort achieved better F value and recall respectively. So AMedPort needs further fine-tuning to be able to achieve a better performance. H3 was not confirmed.

## 5.2.3. User ratings and comments

Similarly to SBizPort, AMedPort received significantly better ratings than the benchmark search engine in terms of information quality and overall satisfaction. The mean differences ranged from 2.1 to 2.8 and were all significant at a 5% alpha-error level. We believe that AMedPort's good performance can be attributed to its high-quality meta-searchers and domain-specific collection and its useful browse support tools. H4 and H5 were confirmed.

Subjects' verbal comments show better satisfaction with AMedPort than with Ayna. Nine (out of eleven) subjects said that AMedPort was useful or provides more topics and information. For instance, subject #a7 said AMedPort was “helpful in cross-referencing information from specific to general.” Subject #a5 said AMedPort was “very useful because it does meta-searching.” Subject #a2 said the AMedPort was “very easy to use for Arabs.” In contrast, Ayna received many negative comments from subjects because of its lack of relevant results and confusing interface. For example, subject #a2 said that Ayna was “very clumsy, disorganized, (and) very brief.” Subject #a8 said she “couldn't easily access it” and subject #a9 said Ayna was “hard to use.”

## 5.3. Discussion

The encouraging results from our experiment demonstrate that the proposed approach is useful to support non-English Web searching and browsing. Although we applied the approach to building two portals in different domains and languages, the experimental results are surprisingly similar. We believe that this was because similar procedures were used to develop the portals and ensured high information quality, comprehensiveness in content coverage, useful functionality, and user-friendly interface. These important components help users who need to search for information from widely scattered regions in a language used by a multitude of countries and places. The results may also imply applicability of the proposed approach to building portals in other domains and languages. Given that the Internet will likely become more and more internationalized [29], the proposed approach is expected to benefit a wide range of domains and users.

Looking more closely into the findings, we observed that the performance differences between the two Arabic search engines are generally larger than those between the two Spanish search engines. This may be due to the relatively weaker Internet development in Arabic-speaking regions. However, as Arabic gains importance on the Internet, we expect the demand for better searching and browsing will grow significantly. Meanwhile, the performance of existing Spanish search engines is expected to lag behind the rapidly-growing Hispanic and Latino populations. Our proposed approach may possibly fill some of the needs.

Compared with previous research (such as [7,23]), our experimental findings provide insights to non-English Web searching in languages that are used in widelyseparated regions. New empirical findings and developments are provided in this work. For example, this research is the first attempt to use and to empirically study the SOM visualizer in supporting non-English Web searching. The Web collections provided by SBizPort and AMedPort are also much larger and contain more diverse regional information than the one developed in [23]. Meta-searching and post-retrieval analysis are new applications in Spanish and Arabic. While major languages like English and Chinese will still be important on the Web, the notion of “multilingual Web” is expected to draw attention from practitioners and researchers in the future. And this research will likely shed light on some system development and decision support issues for non-English Web searching.

## 6. Conclusions and future directions

As non-English speakers increasingly use the Web to seek information, there is a need for better support of searching the Web across different regions. However, support for Internet searching in non-English speaking regions is much weaker than in English-speaking regions. This research proposes a language-independent approach to building Web search portals to support non-English Web searching. Based on the approach, we developed two portals, SBizPort and AMedPort, for the Spanish business and Arabic medical domains, respectively. Experimental results show that the two portals significantly outperformed the benchmark search engines in terms of search accuracy and user ratings on information quality and overall satisfaction. The two portals also achieved precision and recall comparable to those of benchmark search engines. Subjects much preferred our portals to the benchmark search engines in many types of usage. We therefore conclude that the proposed approach is useful in supporting non-English Web searching. This research thus contributes to developing and validating a useful approach to non-English Web searching and providing an example of supporting Web searching in different non-English domains.

This study was limited in several ways. Our two research prototype portals have speed and stability that are not as good as those of commercial search engines like the chosen benchmarks. Several subjects complained about the slow responses of our systems. We also have been limited by the scarcity of prior work on non-English Web searching, which has prevented a more comprehensive review of a topic that possibly would offer better criteria for designing our approach. As for the user study, we had difficulty in recruiting native speakers as our subjects. Future work should consider expanding the sample size to establish a higher statistical confidence in the experimental results.

We are pursuing several directions to extend our research. As the notion of a “multilingual Web” continues to draw attentions, we are developing scalable techniques to collect and analyze information in different languages meaningfully to relate diverse content to produce intelligence. For instance, multinational corporations (MNCs) typically provide Web site information in different languages. Analyzing MNC's relationships with their multinational stakeholders could help provide a holistic picture of how they stand in the international arena. Other domains that we will explore include Spanish medical and Arabic business domains. The resulting business intelligence from stakeholders will serve to guide global development strategies. Another challenging area is the digital archiving of multilingual data from heterogeneous sources — often scattered in different regions. We will investigate techniques and methods to facilitate such a process and better support non-English Web searching. Furthermore, we will develop and validate new visualization techniques to support browsing and comprehending massive multilingual information on the Web.

## Acknowledgments

This research was partly supported by funding from the National Science Foundation Knowledge Discovery and Dissemination (KDD) program #9983304, June 2003–March 2004 and October 2003–March 2004 and from the University Research Institute Grant Program of the University of Texas at El Paso. We are grateful to our project members and the experts and the student subjects who participated in the user study.

## References

[1] R. Abbi, Internet in the Arab world, UNESCO Observatory on the Information Society 3 (2002).

[2] P. Caramelli, The current and future rapid growth of older people in Latin America: implications in psychogeriatrics (keynote presentation), Proceedings of the Eleventh International Congress, International Psychogeriatric Association, Chicago, IL, 2003.

[3] J. Carbonell, J. Goldstein, The use of MMR: diversity-based reranking for reordering documents and producing summaries,

Proceedings of the 21st Annual International ACM-SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Melbourne, Australia, 1998, pp. 335–336.

[4] H. Chen, H. Fan, M. Chau, D. Zeng, MetaSpider: meta-searching and categorization on the web, Journal of the American Society for Information Science and Technology 52 (13) (2001) 1134–1147.

[5] H. Chen, A. Houston, R. Sewell, B. Schatz, Internet browsing and searching: user evaluation of category map and concept space techniques, Journal of the American Society for Information Science, Special Issue on AI Techniques for Emerging Information Systems Applications 49 (7) (1998) 582–603.

[6] W. Chung, H. Chen, J.F. Nunamaker, A visual framework for knowledge discovery on the Web: an empirical study on business intelligence exploration, Journal of Management Information Systems 21 (4) (2005) 57–84.

[7] W. Chung, Y. Zhang, Z. Huang, G. Wang, T.-H. Ong, H. Chen, Internet searching and browsing in a multilingual world: an experiment on the Chinese Business Intelligence Portal (CBiz-Port), Journal of the American Society for Information Science and Technology 55 (9) (2004) 818–831.

[8] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 319–340.

[9] K.A. Ericsson, H.A. Simon, Protocol Analysis: Verbal Reports as Data, MIT Press, Cambridge, MA, 1993.

[10] T. Firmin, M.J. Chrzanowski, An Evaluation of Automatic Text Summarization Systems, The MIT Press, Cambridge, 1999.

[11] Gallup, Encuesta Sobre Portales 2002, http://aui.es/estadi/gallup/ gallup\_portales\_2002.htm, 2002.

[12] Global Reach, Evolution of non-English online populations, http://global-reach.biz/globstats/evol.html, 2004.

[13] Global Reach, Global internet statistics (by language), http://www.glreach.com/globstats/, 2004.

[14] S. Greene, G. Marchionini, C. Plaisant, B. Shneiderman, Previews and overviews in digital libraries: designing surrogates to support visual information seeking, Journal of the American Society for Information Science 51 (4) (2000) 380–393.

[15] M.A. Hearst, Multi-paragraph segmentation of expository text, Proceedings of the 32nd Annual Meeting of the Association for Computational Linguistics, Morgan Kaufmann Publishers, Las Cruces, New Mexico, 1994, pp. 9–16.

[16] Y.K. Hitti, Hitti's Medical Dictionary English–Arabic, Librairie du Liban, Beirut, 1972.

[17] T. Kohonen, Self-Organizing Maps, Springer-Verlag, Berlin, 1995.

[18] C. Kuhlthau, Longitudinal case studies of the information search process of users in libraries, Library and Information Science Research 10 (3) (1998) 257–304.

[19] J.R. Lewis, IBM computer usability satisfaction questionnaires: psychometric evaluation and instructions for use, International Journal of Human–Computer Interaction 7 (1) (1995) 57–78.

[20] X. Lin, Map displays for information retrieval, Journal of the American Society for Information Science 48 (1) (1997) 40–54.

[21] E. Loiacono, WebQual™: a web site quality instrument, Proceedings of International Conference on Information Systems (ICIS) Doctoral Consortium, (Charlotte, NC, USA), 2002.

[22] G. Marchionini, Information Seeking in Electronic Environments, Cambridge University Press, New York, 1995.

[23] B. Marshall, D. McDonald, H. Chen, W. Chung, EBizPort: collecting and analyzing business intelligence information, Journal of the American Society for Information Science and Technology 55 (10) (2004) 873–891.

[24] M.D. Marsico, S. Levialdi, Evaluating web sites: exploiting user's expectations, International Journal of Human–Computer Studies 60 (3) (2004) 381–416.

[25] D. McDonald, H. Chen, Using sentence selection heuristics to rank text segments in TXTRACTOR, Proceedings of the Second ACM/IEEE–CS Joint Conference on Digital Libraries, ACM/ IEEE–CS, Portland, OR, USA, 2002, pp. 28–35.

[26] A. Mowshowitz, A. Kawaguchi, Bias on the web, Communications of the ACM 45 (9) (2002) 56–60.

[27] J. Myers, A. Well, Research Design and Statistical Analysis, Lawrence Erlbaum Associates, Publishers, Hillsdale, NJ, USA, 1995.

[28] L. Norton, The Expanding Universe: Internet Adoption in the Arab Region, World Markets Research Centre, 2001, p. 3.

[29] E.T. O'Neill, B.F. Lavoie, R. Bennett, Trends in the evolution of the public web 1998–2002, Digital Library Magazine 9 (4) (2003).

[30] T.-H. Ong, H. Chen, Updateable PAT-array approach for Chinese key phrase extraction using mutual information: a linguistic foundation for knowledge management, Proceedings of the Second Asian Digital Library Conference, Taipei, Taiwan, 1999, pp. 63–84.

[31] R.L. Penslar, Institutional Review Board Guidebook, Office for Human Research Protection, U.S. Department of Health and Human Services, http://ohrp.osophs.dhhs.gov/irb/irb\_guidebook. htm, 2001.

[32] J. Peterson, Quepasa Announces Agreement to Acquire Vayala Corporation Hispanic PR Wire–Business Wire, Phoenix, 2002.

[33] L.L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Communications of the ACM 45 (4) (2002) 211–218.

[34] W.M.J. Shaw, R. Burgin, P. Howell, Performance standards and evaluations in information retrieval test collections: cluster-based retrieval models, Information Processing and Management 33 (1) (1997) 1–14.

[35] A.G. Sutcliffe, M. Ennis, Towards a cognitive theory of information retrieval, Interacting with Computers (Special Edition on HCI and Information Retrieval) 10 (1998) 321–351.

[36] A. Tombros, M. Sanderson, Advantages of query biased summaries in information retrieval, Proceedings of the 21st Annual International ACM-SIGIR Conference on Research and Development in Information Retrieval, (Melbourne, Australia), ACM Press, 1998, pp. 2–10.

[37] E. Voorhees, D. Harman, Overview of the sixth text retrieval conference (TREC-6), NIST Special Publication 500-240: The Sixth Text Retrieval Conference (TREC-6), National Institute of Standards and Technology, Gaithersburg, MD, USA, 1997.

[38] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5–34.

[39] T.D. Wilson, Models of information behavior research, Journal of Documentation 55 (3) (1999) 249–270.

![](/api/attachments/HSCWWUSH/fulltext/images/932474ef422ed40a340ec3a5c7c32993135975d2e3fc601a4c4c43bb6da580ca.jpg)  
Wingyan Chung is Assistant Professor of CIS in the Department of Information and Decision Sciences at The University of Texas at El Paso. He received his Ph.D. in Management Information Systems from The University of Arizona, and M.S. in information and technology management and BBA in business administration from The Chinese University of Hong Kong. His research interests include knowledge man agement, Web analysis and mining, data

![](/api/attachments/HSCWWUSH/fulltext/images/ab025f9139453f6c1b9a8052336b8f83176abeb86dfd18cb879ce237b51d2507.jpg)

Wei Xi received her masters degree in Management Information Systems from the University of Arizona in 2004 and her B.A. in English from Xi'an Foreign Languages University, China (1995). She joined AI lab in Spring 2003. Her areas of interest include Web programming and database management. Contact her at duoduoxi@gmail.com.

and text mining, information visualization, and human-computer interaction. He has published in leading journals such as Communications of the ACM, Journal of Management Information Systems, IEEE Computer, International Journal of Human-Computer Studies, and Decision Support Systems. Contact him at wchung@utep.edu.

![](/api/attachments/HSCWWUSH/fulltext/images/a665c2ed0521ff3d42f908f42238146af6bfb545d20fa61c047aa40b87184fb3.jpg)  
Alfonso A. Bonillas received his B.S. in Systems Engineering at the University of Arizona. His main interests are Web devel opment, systems optimization, programming, and database management. Contact him at artunso@yahoo.com.

![](/api/attachments/HSCWWUSH/fulltext/images/d263b1a257e6b111b0b11a5a3994f06fd8c5c65a53dc719a3c0bb9ac1559cfb5.jpg)

Guanpi (Greg) Lai is a doctoral student in the Systems and Industrial Engineering (SIE) Department at the University of Arizona. He received his B.S. in Computer Science from Tsinghua University, China and M.S. in Industrial Engineering from the University of Arizona. His research interests include embedded systems’ tasks scheduling, intelli gent control (automobile, home automation), data mining, and data visualization. Contact him at guanpi@email.arizona.edu.

![](/api/attachments/HSCWWUSH/fulltext/images/b61770b9e5b023a5b05624406d6467ba414c52cc401db17cc0013552c02dd3c4.jpg)

Hsinchun Chen is McClelland Professor of MIS at the Eller College of the University of Arizona and Andersen Consulting Professor of the Year (1999). He received the Ph.D. degree in Information Systems from New York University in 1989, MBA in Finance from SUNY-Buffalo in 1985, and BS in Management Science from the National Chiao-Tung University in Taiwan. He is author/editor of 10 books and more than 130 journal articles covering intelligence

analysis, biomedical informatics, data/text/Web mining, digital library, knowledge management, and Web computing. Contact him at hchen@eller.arizona.edu.
