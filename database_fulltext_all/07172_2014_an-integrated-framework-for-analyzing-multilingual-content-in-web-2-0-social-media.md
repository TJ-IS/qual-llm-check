---
otero_id: 7172
otero_key: "BEBKV5HJ"
title: "An integrated framework for analyzing multilingual content in Web 2.0 social media"
authors: "Yan Dang; Yulei Zhang; Paul Jen-Hwa Hu; Susan A. Brown; Yungchang Ku; Jau-Hwang Wang; Hsinchun Chen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.02.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated framework for analyzing multilingual content in Web 2.0 social media

Yan Dang <sup>a,</sup>⁎, Yulei Zhang <sup>a</sup>, Paul Jen-Hwa Hu <sup>b</sup>, Susan A. Brown <sup>c</sup>, Yungchang Ku <sup>d</sup>, Jau-Hwang Wang <sup>d</sup>, Hsinchun Chen <sup>c</sup>

<sup>a</sup> Computer Information Systems, The W. A. Franke College of Business, Northern Arizona University, Flagstaff, AZ 86011, United States

<sup>b</sup> Department of Operations and Information Systems, David Eccles School of Business, University of Utah, Salt Lake City, UT 84112, United States

<sup>c</sup> Department of Management Information Systems, Eller College of Management, University of Arizona, Tucson, AZ 85721, United States

<sup>d</sup> Computer Center, Central Police University, Taiwan

## a r t i c l e i n f o

Article history: Received 29 December 2012 Received in revised form 29 December 2013 Accepted 19 February 2014 Available online 26 February 2014

Keywords: Social media Web portal User evaluation

## a b s t r a c t

The growth of Web 2.0 has produced enormous amounts of user-generated content that contains important information about individuals' attitudes, perceptions, and opinions toward products, social events, and political issues. The volume of such content is increasing exponentially, making its search, analysis, and use more dif<sup>fi</sup>cult and thus favoring advanced tools that aid in information search and processing. We propose an integrated framework that offers an infrastructure necessary for accessing, integrating, and analyzing multilingual user-generated content from different social media sites. Building on this framework, we develop the Dark Web Forum Portal (DWFP) that supports the gathering and analyses of social media content concerning security. Our evaluation results show that users supported by DWFP complete tasks better and faster than those using the benchmark forum. Participants consider DWFP to be better in terms of system quality, usefulness, ease of use, satisfaction and intention to use.

© 2014 Elsevier B.V. All rights reserved

## 1. Introduction

The phenomenal growth of Web 2.0 has produced enormous amounts of user-generated content available in various online forums, blogs, and social media sites [30]. Such content contains information about individuals' attitudes, perceptions, and opinions toward various products, services, social events, and political issues [30]. The opinionrich content enables new knowledge discovery in different domains such as healthcare, education, politics, and security. For example, in security informatics area, the Web has become an essential communication media for international extremist groups who are increasingly using the Internet to promulgate their agendas. Due to the high anonymity, easy access, and huge audience of social media sites (e.g., Web forums), international extremist groups often use them to promote violence and distribute propaganda materials. Thus, collecting and analyzing related information from social media sites can be of great importance and interest to security analysts. However, the sheer volume of user-generated content is increasing exponentially, making effective search, analysis, and decision making more dif<sup>fi</sup>cult [14] for people who are interested in this type of rich data source such as computer and information researchers, security informatics researchers, social scientists, government agencies, and the general public. To address these challenges, advanced, automated tools would provide an effective response. As Kim et al. [34] pointed out, searching and analyzing social media content is tedious and time-consuming. However, inadequate search of social media content produces incomplete information that in turn can mislead the decision making by individuals or organizations alike [20].

Several challenges remain in developing automated search and analysis support tools. For example, gathering and integrating usergenerated content, normally semi-structured or unstructured, across different social media sites, is challenging [22,29,32]. The lack of common formats in user-generated content is also problematic; compared with other online resources, such as news or scienti<sup>fi</sup>c article repositories, user-generated content often lacks a consistent structural organization. Consequently, when searching for relevant content regarding a particular topic or event, such as posted comments representative of mainstream opinions, people often need to visit multiple social media sites to browse and integrate related content with primitive support, if any. Popular social media sites normally vary in their organization or structure, which further constrains the use of a single access procedure to gather content across sites.

Language introduces another dimension of complexity; the content available in many social media sites is usually created in different languages. According to the Internet World Statistics, more than 70% of Internet users are non-English speaking (http://www.

internetworldstats.com/stats7.htm). As a result, effective search and analysis support must properly address issues surrounding multilingual, user-generated content. Most existing search techniques and analytical tools offer limited utilities for gathering and integrating content created in different languages, partially because they are designed for speci<sup>fi</sup>c grammatical structures or document organization formats [32]. To support enhanced decision making, automated tools should allow people to collect, store, and analyze voluminous usergenerated content in different languages, offer desirable <sup>fl</sup>exibility and nearly real-time access, and provide adequate result presentation designs [12].

To address the abovementioned challenges, this study makes contributions by proposing and developing an integrated, architectural framework that provides an infrastructure necessary for accessing, integrating, and analyzing multilingual user-generated content from various social media sites. The framework adopts a modular, multi-layered architecture and offers advanced functionalities for content integration, search, and multilingual translation. This study also contributes to security informatics research and practice by developing an integrated forum portal system (called Dark Web Forum Portal) based on the proposed system framework. The system offers an effective search and analysis support on volumes of user-generated content obtained from different, highly visible, multilingual Web forums of concern to homeland security. The system could be of great importance and interest to computer and information researchers, security informatics researchers, social scientists, government agencies, and the general public.

We conduct an experiment to evaluate this forum portal system. Our evaluation focuses on user task performance measured by accuracy and time ef<sup>fi</sup>ciency, system quality, ease of use, usefulness, satisfaction, and intention to use, and includes user-generated content from two highpro<sup>fi</sup>le security-oriented forums for comparative purposes. A total of 78 senior students from the National Central Police University, Taiwan voluntarily participated in the experiment. According to our experimental results, participants supported by DWFP can complete tasks better and faster than those using the benchmark forum, consider DWFP better in system quality, usefulness, and ease of use, and exhibit greater satisfaction with and intention to use the system.

Following the design science guidelines [27], we adopt the system build-and-evaluate cycle in this study. We <sup>fi</sup>rst provide description on how the IT artifact was developed to address the challenges in social media data in Section 2, representing the system “build” part of the cycle. We then evaluate the IT artifact via a quantitative study as presented in Section 3, which is the system “evaluate” part of the cycle. Speci<sup>fi</sup>cally, in Section 2, we <sup>fi</sup>rst provide a background overview and highlight several key challenges in searching, integrating, and analyzing multilingual content from multiple social media sites (Section 2.1), and then describe in detail about the development of the proposed framework and the forum portal system for security informatics that aim at addressing the identi<sup>fi</sup>ed challenges (Section 2.2). In addition to system development, a systematic and rigorous evaluation of the system is also crucial to design science research as suggested by the design science guidelines [27]. Therefore, we present the system evaluation in detail in Section 3. We describe the evaluation study in Section 3.1, and discuss the data analysis results in Section 3.2. After that, in Section 4, we discuss the study's contributions and limitations, and point out several future research directions. We conclude the paper with a summary in Section 5.

## 2. Designing the IT artifact DWFP

## 2.1. Background overview

The community-oriented, highly interactive socialization and communication capability of Web 2.0 has fostered an exponential growth of user-generated content [37]. While this content contains enormous volumes of individuals' attitudes and opinions about various topics, the content across platforms often differs in structure, format, and language. In this section, we provide an overview of user-generated content and highlight several challenges fundamental to the search and analysis of user-generated content.

## 2.1.1. Overview about user-generated content

User-generated content means the content created and posted on online social media sites by general Internet users [30]. Web 2.0 enables the creation of a large amount of user-generated content by allowing general Internet users to interact and collaborate with each other on social media sites (such as Web forums, blogs, Twitter, and Facebook). This is a huge difference compared with Web 1.0 when general Internet users could only passively view the content provided by major online publishers and webmasters. Previous research that aims at developing Web portals for different areas has mainly focused on collecting and using Web 1.0 content as data sources for the portals, such as EBizPort [35], Nano Mapper [16], MPEG-7 in Moving Image Collections portal [2], and FedStats Web portal [4]. Web 1.0 resources support information (document) publishing and dissemination, typically controlled and managed by the providers. Thus, the content available in these resources normally follows a particular structure; for example, a digital library of scienti<sup>fi</sup>c articles uses a consistent format to organize key <sup>fi</sup>elds of an article, such as title, journal or conference, authors, abstract, and citations.

While Web 1.0 resources provide “read-only” content in speci<sup>fi</sup>c structural formats and consistent displays, Web 2.0 resources are mostly generated by a community that creates and consumes the content, often in unstructured formats [28,37]. Social networking, a prominent feature of Web 2.0, enables greater information exchange, opinion sharing, and discussion among individuals on a global scale [37], thus resulting in vast amounts of user-generated content. According to Chen [11], the voluminous, dynamic nature of social media data are valuable because they allow us to tap into the “wisdom of the crowd,” thus enhancing decision-making. However, the user-generated content available in social media sites, created in different languages and rapidly disseminated without consistent structure, represents challenges for effective search and analysis.

## 2.1.2. Challenges with user-generated content

2.1.2.1. Content integration across different social media sites. Most usergenerated content lacks structure. According to Roberts [39], approximately 95% of the 1.2 zettabytes of data available in the digital universe are unstructured, with about 70% generated by users in social media. Overall, existing tools offer limited support for accessing the unstructured content available in social media sites and presenting it with displays appropriate for users [22,29,32]. As Kawamura [32] comments, integrating social media data represents a critical challenge in Web 2.0.

Central to integrating user-generated content is providing an adequate structure to user-generated content for easy search and access without destroying its richness, such as an opinion issued about an event, who said what, how different people viewed an incident, and how their views change over time. Terman [43] analyzed the integration of social media data related to business and identi<sup>fi</sup>ed the volume and lack of structure as two critical challenges. The absence of a de<sup>fi</sup>ned data model that speci<sup>fi</sup>es data <sup>fi</sup>elds and types in social media data also creates dif<sup>fi</sup>culty in populating and storing user-generated content in databases [43].

Efforts have been taken to integrate social media data, typically toward one or several given users or events rather than integrating across all or most users and events. For example, Wang et al. [46] proposed an ontology-based, user-centric approach to keep track of an individual's friends and their activities by integrating social media data from different social networking sites. With their approach, people can merge their friends' accounts in multiple social networking sites to obtain a comprehensive understanding of their activities. Bojārs et al. [8] applied semantic Web technology to develop an approach capable of incorporating semantic information into user-generated content to better understand online communities, with a focus on capturing and analyzing the content that an individual has contributed in different sites. Becker et al. [5] proposed a method to identify key events discussed by Internet users and integrate the associated user-generated content about a given event across various social media sites. While interesting and providing considerable value, these studies are limited in addressing the data integration challenge central to effective search and analysis of usergenerated content. Toward that end, a consistent structure (format) is necessary for developing automated, <sup>fl</sup>exible techniques that allow search of and access to user-generated content in different sites and provide a mechanism for extracting important content in an intuitive and timely manner.

2.1.2.2. The multilingual issue in user-generated content. The Web embraces more than 1000 languages [15]. Not surprisingly, non-Englishspeaking users have outnumbered their English-speaking counterparts since 2000 and the differential seems to be growing over time [23]. A substantial portion of user-generated content is created in languages other than English, which makes automatic translation appealing. Qin et al. [38] incorporate cross-language information retrieval techniques in Web portal developments by constructing a domain-speci<sup>fi</sup>c bilingual lexicon. Talvensaari et al. [42] perform graded relevance assessments to improve corpus-based, cross-language information retrieval for locating relevant content. However, few previous studies have developed or integrated a real-time translation component for social media data in different languages.

A review of existing translation methods indicates that dictionarybased, corpus-based, and machine translation-based approaches have been used [1,48]. Table 1 presents the key criteria for each approach [1,48]. Common machine translation-based tools include Google Translation (http://translate.google.com/), Babel Fish (http://babel<sup>fi</sup>sh. altavista.com), and FreeTranslation.com (http://www.freetranslation. com). Among them, Google Translation is widely used for various online translation services and has shown stable, effective, and time-ef<sup>fi</sup>cient performance.

## 2.2. System framework and Dark Web Forum Portal

As abovementioned, several challenges associated with usergenerated content from multiple social media sites are identi<sup>fi</sup>ed, including the sheer volume, lack of structure, and multilingual issue. To address those challenges, we propose an integrated system framework to support effective search and analysis of user-generated content, representing the problem solving process in design science research [27].

As shown in Fig. 1, the framework consists of three layers — a database layer, a logical control layer, and a presentation layer. In each layer, we implement and leverage advanced functions to address the gathering, integration, and search of multilingual user-generated content. Speci<sup>fi</sup>cally, three major functions, including data integration support, search support, and multilingual translation support, are created in order to address the challenges highlighted in Section 2. In the following, we describe each layer and the key functions it offers.

Key criteria for different translation approaches [1,48].

<table><tr><td>Approach</td><td>Key criteria</td></tr><tr><td>Dictionary-based</td><td>Construct a bilingual dictionary (generic or domain-specific);Translation is done through dictionary look-ups.</td></tr><tr><td>Corpus-based</td><td>Builds a statistical translation model from a large training set;Require no dictionaries between two languages;Better fit domains in which dictionaries do not exist or are difficult to create.</td></tr><tr><td>Translation-based</td><td>Employ machine translation techniques for automatic translation;Require no additional training;Relatively easy to incorporate into an integrated system.</td></tr></table>

## 2.2.1. Database layer

The database layer deals with issues pertinent to content collection and parsing. Timely access and gathering of user-generated content in social media is critical, demanding tailored collection and update procedures. Thus, to collect the content available at a social media site, both complete spidering and incremental spidering are utilized. Complete spidering is applied to an online forum the <sup>fi</sup>rst time the forum is included in the resource pool (i.e., collecting all postings of the forum). Then, incremental spidering is performed on the forum to gather new postings at a speci<sup>fi</sup>ed time interval. In this way, the spidering process can achieve greater time and computational processing ef<sup>fi</sup>ciency.

For incremental spidering, we implement algorithms to identify and collect postings generated after the last spidering of a given social media site. Different techniques are created and tailored to the respective social media sites. Once new threads and postings are collected using incremental spidering, detailed data <sup>fi</sup>elds (such as posting title, main posting body, author, posting date/time) are extracted from the raw HTML Web pages (i.e., collated user-generated content) and stored in a database that follows a uni<sup>fi</sup>ed database design to accommodate different data sources. Building on the data collection, parsing, and archive foundation, we then implement data integration functionality at the database layer.

## 2.2.2. Logic control layer

In this layer, we create speci<sup>fi</sup>c functions to enable search and multilingual translation support. For the search support, keyword-based functions are developed; for the multilingual translation support, the machine translation-based technique is adopted. This layer serves as middleware that connects the presentation layer and the database layer.

In our prototype implementation, the search support function allows users to search postings from each social media site, using keyword(s) that appear in different data <sup>fi</sup>elds (e.g., message/thread title, message body, author name, post date). Users can use logical operations such as “AND” or “OR” in conjunction with keywords to obtain postings appropriate to their needs or interests. In addition to searching content from a particular site, our system also allows users to search content across multiple sites. To enhance consistency and the user experience, we adopted a uni<sup>fi</sup>ed search interface design and implemented search functionality across different social media sites. In addition, full-text indexing is employed in order to improve the ef<sup>fi</sup>ciency of searching in full message bodies.

The multilingual translation support function is developed by using Google Translation API (http://code.google.com/apis/ajaxlanguage documentation/#Translation), which offers effective machine translationbased services in many domains. We chose Google Translation API because it is a widely used tool for online translation services and has been shown to be stable, fast, and effective in translation performance. In addition, the use of Google Translation API is free of charge and easy to access and implements in an integrated system that runs Java-based applications. The multilingual translation support function performs translations in a real-time manner. The user can launch it when conducting searches and when browsing the search results. After that, the content to be translated will be sent to the translation server with the translated messages returning back and displaying on the client browser in seconds.

## 2.2.3. Presentation layer

Information visualization is important for system development, as better visualization can help enhance users' performance and overall system assessments [40]. Information visualization seeks to present search or analysis results in an effective and ef<sup>fi</sup>cient manner [7]. The presentation layer of the proposed system framework provides consistent user interfaces with desirable functionality. We used JavaServer Pages (JSP) technology to develop display pages for presenting search and analysis results to users. For non-English forums, we present results in both the original language and English, using a double-column table format (i.e., a column for each language and a row for the same posting). To further support users regarding multilingual content, (e.g., when a user performs a keyword search in non-English forums), our system allows them to submit search terms in English, even though the focal social media site (forum) uses a different language (e.g., Arabic or French). In this case, our system will return the search results that match both the submitted English terms and the translated terms (in Arabic or French). In our presentation interfaces, keywords are highlighted in the search results in both languages.

![](/api/attachments/BEBKV5HJ/fulltext/images/8cdc7df0f6c9e1b2d5356fc80f7ddfb421d935d54c415fb0cf225ac5afb2567d.jpg)  
Fig. 1. System framework architecture.

## 2.2.4. Dark Web Forum Portal

We build on the proposed framework to develop Dark Web Forum Portal (DWFP), a forum portal system that could contribute to security informatics research and practice [47]. The portal currently contains user-generated content from 29 highly visible forums of concern to homeland security, with more than thirteen million postings contributed by 340,000 individuals. Among them, seventeen forums are in Arabic, seven in English, three in French, and two each in both German and Russian.

We chose security informatics as an illustration primarily because of the growing attention and concern at both national and international levels. DWFP aims to support individuals and government agencies in comprehending and <sup>fi</sup>nding relevant content in social media sites in an effective and ef<sup>fi</sup>cient manner. This is done by providing automated support in data gathering and integration of heterogeneous content from different forums, storing data in a structured database, and producing timely analysis reports or alerts. For displaying the search and analysis results of the multilingual content, we use a two-column display format, with one column showing the original postings and the other column displaying the translations. Such display format allows users to view the content in the original language and the target language simultaneously. Fig. 2 shows a screenshot of particular search (using keywords Iraq OR bomb) and multilingual translation support functions provided by DWFP.

## 3. Evaluation of the IT artifact DWFP

In the previous section, we presented the system development in detail. As suggested in the design science guidelines, a systematic and rigorous evaluation is also crucial to design science research [27]. Thus, in this section, we discuss the evaluation of the system. We <sup>fi</sup>rst present a set of hypotheses that are used to guide the system evaluation (in the aspects of accuracy, ef<sup>fi</sup>ciency, system quality, ease of use, usefulness, satisfaction and intention to use). We then describe in detail about the evaluation study and the data analysis results, respectively.

![](/api/attachments/BEBKV5HJ/fulltext/images/6e533b03ae54aab13ddd9a0ef22bedff96117599c1b725f207e8c5b6bf71f3d0.jpg)  
Fig. 2. A screenshot of DWFP search and multilingual translation support.

User performance is an important indicator of the success of an information system [18,19], as it can re<sup>fl</sup>ect system's pragmatic bene<sup>fi</sup>ts and values. Accuracy is central to user performance [9] and thus represents a common evaluation measure in various domains [21]. In addition, one goal of information systems is to enable people to complete their tasks better and faster [33]. Task performance can be measured by time ef<sup>fi</sup>ciency, representing another important evaluation dimension [3]. DWFP encompasses functions that can better support the search and analysis of multilingual content from multiple sites. Therefore, we hypothesize:

H-1. Participants achieve higher accuracy in task performance when using DWFP than using the benchmark.

H-2. Participants achieve higher time ef<sup>fi</sup>ciency in task performance when using DWFP to complete tasks than using the benchmark.

System quality is a critical measure of information system success [19]. According to McKinney et al. [36], the quality of a Web-based information system can be measured by the user's perception of the system's performance. DWFP is developed to address challenges of usergenerated content by providing data integration support and embedded translation function. Thus, we hypothesize:

H-3. Participants perceive DWFP of higher system quality as compared with the benchmark.

Ease of use and usefulness are two widely-used measures to assess information systems. Ease of use refers to a person's perception that his or her use of the system is relatively free of effort [44]. Perceived usefulness refers to the degree to which a person considers that the use of an information system can enhance his or her performance [44]. Because DWFP is designed to better support users' searching and analyzing content available on different multilingual social media sites, we hypothesize:

## H-4. Users perceive DWFP easier to use than the benchmark.

## H-5. Users perceive DWFP more useful than the benchmark.

User satisfaction is essential for assessing the success of an information system [18,19]. Prior research suggests perceived usefulness and ease of use impact user satisfaction [e.g., 10, 31]. In addition, ease of use and usefulness [17,44] as well as attitude (i.e., satisfaction) [10,31] can also in<sup>fl</sup>uence users' intention to use an information system. Given that DWFP has been designed with ease of use and usefulness in mind, we hypothesize:

H-6. Participants exhibit higher satisfaction with DWFP than with the benchmark.

H-7. Participants show greater intention to use DWFP than the benchmark.

## 3.1. Evaluation study

## 3.1.1. Experimental design

We employed a one-repeated factor design, with “system” being the repeated factor (i.e., DWFP versus a benchmark containing two Web forums augmented with Google Translate, http://translate.google.com/). Our experiment focuses on examining user task performance (measured by accuracy and time ef<sup>fi</sup>ciency), system quality, usefulness, ease of use, user satisfaction, and intention to use. The benchmark includes two Web forums, one in Arabic and the other in English. During the experiment, each user conducts four search tasks. Among them, two tasks are about searching information in an Arabic data source (i.e., the social media content from this data source is in Arabic), and the other two tasks for an English data source (i.e., the social media content from this data source is in English). When working on the tasks, users are asked to use both DWFP and a related benchmark. For the two Arabic tasks, the benchmark is the Arabic forum where the data source is collected augmented with Google Translate. Similarly, for the two English tasks, the benchmark is the English forum where the data source is collected augmented with Google Translate. Choice of the benchmark forums was made based on the fact that they are important online discussion sites that are known to the security informatics community, included as data sources in DWFP, and provide search functions similar to those of DWFP. To mitigate the carryover effects, we randomized the sequence of the systems that participants used in the experiment.

## 3.1.2. Participants

We targeted senior students studying at the National Central Police University in Taiwan. These students will be assigned law-enforcement and security jobs upon graduation and therefore are potential, nearterm, users of DWFP. With the assistance of university administrators and instructors teaching these senior students, we recruited students to take part in our study. All participation was voluntary and did not affect students' grades or classroom performance assessments.

## 3.1.3. Experimental tasks and flow

Each participant used both DWFP and the benchmark to complete four tasks. For each participant, the order of the systems that he/she used was randomly assigned. With the assistance of three security informatics experts, we constructed different scenarios, from which we developed four experimental tasks: two searching for content from the “Alokab” forum postings (in Arabic) and two seeking content from the “Islamic Awakening” forum postings (in English). The tasks are listed in Appendix A.

Each participant used DWFP or the benchmark to complete these tasks, and then was asked to complete a questionnaire soliciting his or her assessments of system quality, usefulness, ease of use, satisfaction, and intention to use. Participants then used the other option (benchmark or DWFP) to repeat these tasks and then completed the questionnaire. That is, some participants used DWFP and then used the benchmark and others used the benchmark and then DWFP. To further reduce potential sequencing effects, we randomized the order in which the tasks were presented to each participant.

## 3.1.4. Measurement

We measured user task performance in terms of effectiveness and ef<sup>fi</sup>ciency. Speci<sup>fi</sup>cally, we assessed task performance effectiveness by accuracy, which refers to the degree to which the participant can use a forum to complete a task correctly [35]. We allowed partial accuracy by considering the portion of the correct answer in each task in relation to the complete, correct answer. Three security informatics experts helped provide the complete and correct answer to each task. Task accuracy for each participant was determined by checking against those complete and correct answers provided by the experts. We assessed task performance ef<sup>fi</sup>ciency by examining the amount of time a participant needed to complete a task. We used previously validated perception-based scales for system quality, ease of use, usefulness, user satisfaction, and intention to use (see Appendix B). System quality embraces the dimensions fundamental to the quality of an information system [18,19]. We adopted the Questionnaire for User Interaction Satisfaction (QUIS 7.0, http://lap.umd.edu/quis/) developed by Chin et al. [13], a multi-faceted scale consisting of items speci<sup>fi</sup>c to users' assessments of their interactions with a system in terms of overall reactions, screen factors, terminology and system information, learning, and system capabilities [26]. We adapted items from Davis [17] to measure perceived usefulness and perceived ease of use, with minor wording changes appropriate for our participants and context. We measured user satisfaction and intention to use with items from Bhattacherjee [6] and Davis [17]. All the measurement items employed a seven-point Likert scale, with 7 being “strongly agree,” 4 being “neutral,” and 1 being “strongly disagree.” Since the mother language of all participants is Chinese, all experimental tasks and measurement items were presented to them in Chinese. We used the translation and back translation method [25] to ensure proper translation of all the task descriptions and measurement items used in the experiment, with the assistance of two professional translators knowledgeable about the security domain, but unaware of the study's objectives.

## 3.1.5. Benchmark

To the best of our knowledge, DWFP is the <sup>fi</sup>rst Web portal that integrates user-generated content from multiple forums and offers advanced search and analysis functions for security informatics. Thus, there are no comparable portals readily available for evaluations. With the assistance of three security informatics experts, we identi<sup>fi</sup>ed two forums that are important to the domain and are included in the DWFP data sources. Each forum, augmented by an online translation function, can provide multilingual content search and analysis support similar to that of DWFP for a given data collection. Therefore, our benchmark includes two forums (“Alokab” and “Islamic Awakening”) combined with Web-based Google Translate service (http://translate.google.com). When using the benchmark to complete the experimental tasks, the subjects used the forum “Alokab” combined with Web-based Google Translate service to complete the two tasks about searching for Arabic content and the forum “Islamic Awakening” combined with Web-based Google Translate service for the other two tasks about searching for English content. Both forums “Alokab” and “Islamic Awakening” provide keyword-based search functionality similar to that of DWFP. In addition, the translation components in both DWFP and the benchmark are based on Google Translate. DWFP implements Google Translation API for multilingual translations, and the two forums in the benchmark are combined with Web-based Google Translate service for the experiment. Furthermore, the two forums in the benchmark are part of the 29 forums from which DWFP gathered the user-generated content. Overall, a participant could access the same content and comparable functions in the experiment when using DWFP or the benchmark to complete the experimental tasks.

## 3.2. Data analyses and results

A total of 78 students participated in the study, 67 males and 11 females. Both Arabic and English were foreign languages to the participants, whose mother language is Chinese. In Table 2, we summarize participant demographics. On average, participants had more than 10 years of experience using computers; approximately half of them were trained to be police of<sup>fi</sup>cers and the remaining to be security specialists. The participants had limited ability to read or write in English, and none of them could read or write in Arabic.

## Table 2

Table 4  
Summary of important characteristics of participants.

<table><tr><td>Characteristic</td><td>Participants</td></tr><tr><td>Gender</td><td>Male: 67; female: 11</td></tr><tr><td>Age</td><td>Mean: 25.01; standard deviation: 6.67</td></tr><tr><td>Years of using computer</td><td>Mean: 9.86; standard deviation: 3.16</td></tr><tr><td>Training focus</td><td>Police officers: 41; security analysts: 37</td></tr><tr><td>General computer skilla</td><td>Mean: 4.08; standard deviation: 1.11</td></tr><tr><td>English abilityb</td><td>Mean: 3.85; standard deviation: 1.25</td></tr><tr><td>Arabic abilityb</td><td>Mean: 1; standard deviation: 0</td></tr></table>

<sup>a</sup> Computer skill rating scale ranges from 1 to 7, with 1 being very unskilled and 7 being very skilled.  
<sup>b</sup> Language ability rating scale ranges from 1 to 7, with 1 being “can neither read nor write” and 7 being “can read and write very <sup>fl</sup>uently”

Table 3  
Summary of data analysis results — means and standard deviations

<table><tr><td rowspan="2">Measure</td><td colspan="2">DWFP</td><td colspan="2">Benchmarks</td></tr><tr><td>Mean</td><td>Std dev</td><td>Mean</td><td>Std dev</td></tr><tr><td>Task performance accuracy</td><td>61.86%</td><td>28.34%</td><td>43.30%</td><td>25.77%</td></tr><tr><td>Task performance time efficiency</td><td>2.33</td><td>1.06</td><td>3.19</td><td>1.67</td></tr><tr><td>System quality: Overall reactions</td><td>4.53</td><td>1.05</td><td>3.34</td><td>1.22</td></tr><tr><td>System quality: Screen</td><td>4.72</td><td>1.10</td><td>3.58</td><td>1.28</td></tr><tr><td>System quality: Terminology/system information</td><td>4.56</td><td>0.90</td><td>3.82</td><td>1.05</td></tr><tr><td>System quality: Learning</td><td>4.48</td><td>1.14</td><td>3.51</td><td>1.28</td></tr><tr><td>System quality: System capabilities</td><td>4.79</td><td>0.74</td><td>3.83</td><td>1.09</td></tr><tr><td>Perceived ease of use</td><td>4.79</td><td>1.20</td><td>3.37</td><td>1.42</td></tr><tr><td>Perceived usefulness</td><td>4.86</td><td>1.13</td><td>3.60</td><td>1.45</td></tr><tr><td>User satisfaction</td><td>4.60</td><td>1.14</td><td>3.31</td><td>1.45</td></tr><tr><td>Intention to use</td><td>4.73</td><td>1.29</td><td>3.20</td><td>1.33</td></tr></table>

## 3.2.1. Hypothesis testing results

In Table 3, we summarize the means and standard deviations of the measurements. As a group, participants achieved 61.86% accuracy in task performance when using DWFP and 43.40% accuracy when using the benchmark forums. On average, the participants needed 2.33 min to complete a task when using DWFP and 3.19 min when using the benchmark forums. Participants perceived DWFP more positively than the benchmark forums, ranging from 4.48 to 4.86 versus 3.20 to 3.83 on the seven-point Likert scale.

To test our hypotheses, we performed one-tailed t-tests with the experimental data. As summarized in Table 4, the data support all the hypotheses, with p b 0.0001. The support of our hypotheses can be attributed to DWFP's advanced search functionality, integrated usergenerated content, consistent presentation displays, and the embedded multilingual translation support. Speci<sup>fi</sup>cally, participants perceived DWFP to be signi<sup>fi</sup>cantly better than the benchmark in all the measurements we examined; they were able to complete tasks more accurately and faster when supported by DWFP than by the benchmark forum. Overall, participants considered DWFP to be better than the benchmark in terms of system quality, ease of use, and usefulness that lead to a perception of higher satisfaction and intention to use [10,17,31,44]. Our experimental results consistently show that participants are more satis<sup>fi</sup>ed with DWFP than with the benchmark and show greater intention to use DWFP in the near future.

## 4. Discussion

Web 2.0 social media has been providing an exponential growth of user-generated content. As a new type of data that is different from other formal data sources such as news, reports, and scienti<sup>fi</sup>c articles, user-generated content contains rich volumes of individuals' attitudes and options on various topics. Such opinion-rich content can be of great importance and interest to different people such as managers, government of<sup>fi</sup>cers, and researchers. However, several key challenges exist in searching for and analyzing information from user-generated content. First, most user-generated content from Web 2.0 social media sites lacks a common structural organization. Data format could vary a lot among and even within social media sites. This makes data access and gathering across sites dif<sup>fi</sup>cult. Second, multilingual issue becomes another challenge for searching and analyzing user-generated content. The majority of the user-generated content created over the Internet is not English. Thus, providing automated and timely translation support to help understand user-generated content in different languages is important.

Hypothesis testing results.

<table><tr><td>Hypothesis</td><td>Measure</td><td>p-value</td><td>Result</td></tr><tr><td>H-1</td><td>Task performance accuracy</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-2</td><td>Task performance time efficiency</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-3A</td><td>System quality: Overall reactions</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-3B</td><td>System quality: Screen</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-3C</td><td>System quality: Terminology/system information</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-3D</td><td>System quality: Learning</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-3E</td><td>System quality: System capabilities</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-4</td><td>Ease of use</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-5</td><td>Usefulness</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-6</td><td>Satisfaction</td><td>&lt;.0001</td><td>Supported</td></tr><tr><td>H-7</td><td>Intention to use</td><td>&lt;.0001</td><td>Supported</td></tr></table>

To make good use of user-generated content and address the abovementioned challenges, a framework is needed for integration, organization, search support, and visual display. Toward that end, we contribute to extant literature by advancing the search and analysis support of multilingual, user-generated content across various social media sites. The proposed framework follows an integrated approach that offers desirable data integration, search support, and automatic multilingual translation of semi-structured or unstructured user-generated content available in various sites, hereby addressing the challenges associated with multilingual, user-generated content in social media sites.

Second, we also contribute to security informatics research by developing an integrated portal with advanced data integration functionality supported by complete and incremental spidering that obtains the volumes of user-generated content available on different social media sites in a timely and ef<sup>fi</sup>cient manner, and effective content parsing for organizing and storing the accessed content according to a de<sup>fi</sup>ned structure. We adopt a uni<sup>fi</sup>ed data representation design to provide consistent displays of original content or search results. Individuals and organizations can conduct keyword-based search of user-generated content across all data sources; they can also search across different data <sup>fi</sup>elds using multiple keywords. We employ full-text indexing to improve the ef<sup>fi</sup>ciency of searching in different data <sup>fi</sup>elds such as message title, posting date, and full message body. The automatic multilingual translation function allows users to understand multilingual content in a real-time manner. Users can specify a search term in a chosen language to search content in other languages across different sites. The search results are displayed in both the language of the source content and a language of the user's choice through automated translation support. Our framework development emphasizes usefulness and ease of use, which are closely related to users' information processing and mental model [41] critical to cognitive <sup>fi</sup>t [45], and task-technology <sup>fi</sup>t [24].

In addition, our study contributes to existing security informatics practice by implementing Dark Web Forum Portal (DWFP), which currently contains user-generated content available in 29 high-pro<sup>fi</sup>le forums concerning homeland security. It has more than 13 million postings by 340,000 individuals, in Arabic, English, French, German, and Russian. We design consistent representation formats to display relevant content from different forums, and implement advanced search functionalities and automated multilingual translation support in DWFP. In addition, we perform a user evaluation study to assess the effectiveness of DWFP. Our study involves voluntary participants who represent potential users of DWFP. Our evaluation includes multiple measures fundamental to the effectiveness of DWFP, as revealed by the existing system adoption and success literature. Overall, our results are favorable, suggesting that people supported by DWFP can complete their tasks faster and better than using the benchmark; they consider DWFP to be of high system quality, and usefulness and easy to use. Participants were satis<sup>fi</sup>ed with DWFP and had favorable intention toward using it.

This study also follows the design science research guidelines set forth by Hevner et al. [27] through the system build-and-evaluate cycle. Speci<sup>fi</sup>cally, DWFP represents the IT artifact instantiated using advanced data integration, search support, and multilingual translation function (i.e., the “design as an artifact” guideline). To examine and demonstrate desirable system ef<sup>fi</sup>cacy and utility, we conduct the evaluation study using representative tasks, comparable benchmark, appropriate study design, and previously validated measurement instruments (i.e., the “design evaluation” guideline). By doing so, we contribute to extant research on social media analytics and security informatics by providing a real-world portal system that enables users to search and understand multilingual content from various social media sites (i.e., the “research contribution” guideline). We construct DWFP relevant to security informatics analysts and researchers (i.e., the “problem relevance” guideline). The implementation of DWFP encompasses advanced data integration, search support, and multilingual translation techniques (i.e., the “research rigor” guideline). Our system design and implementation proactively solicit from security informatics experts as well as general users' essential evaluative feedback for improved system design, functionality, and utilities (i.e., the “design as a search process” guideline). Furthermore, we conduct an evaluation study and communicate our empirical results to demonstrate and convey the utility of DWFP (i.e., the “communications of research” guideline).

Our evaluation results have several implications for researchers and practitioners interested in analyzing content available in social media data. For example, our results illustrate that the use of an integrated por tal could better support the search and analysis of user-generated content across social media sites in an effective and ef<sup>fi</sup>cient manner. Without such integrated portals, users who would like to search and analyze information on a topic of interest (such as computer and informa tion researchers, security informatics researchers, social scientists, government agencies, and the general public) from user-generated content typically need to browse different sites, which can be ineffective, time-consuming, and tedious. By accessing integrated content with adequate structures and systematic presentations, users can identify essential information and scrutinize interesting patterns from the vast amounts of social media data available. Our study also reinforces the importance of data integration (such as adopting a consistent database design), search support, and information representation for organizing and displaying social media data. A well-organized, consistent database design is indispensable for the very <sup>fi</sup>rst data collection and integration step as well as subsequent search and analysis support. This is because adopting a consistent database design across user-generated content from various social media sites could lead to the increase in ef<sup>fi</sup>ciency of information search and analysis, as the latter two functions need to access the database to obtain and display related information to the user. Presenting search results with intuitive displays is crucial to users' comprehension and analysis. Thus, advanced portal systems that target user-generated content in various forums and social media sites must address the associated structure and the volume challenges properly. Furthermore, translation support is crucial for social media portals and has to provide users with the necessary translation between languages in a <sup>fl</sup>exible and near real-time fashion. Toward that end, ou evaluation results indicate the effectiveness of a two-column display format for search result presentation, allowing users to view the original postings and the translated ones simultaneously. Translations should proceed in a near real-time manner; for example, postings should be sent to the translation server (e.g., Google Translations API server) immediately after a user clicks on the translation function, then the trans lations are transmitted back to the portal for display, without storing the translations in the database for performance reasons. In addition, the vast amount of data available in social media sites makes the combined use of complete and incremental spidering appealing. When a social media site is included for data collection, the use of incremental spidering is advantageous in keeping the data collection up-to-date without excessive maintenance efforts.

The proposed system framework also has some limitations that can be addressed in future research. First, the framework targets the semi-structured and un-structured and the multilingual aspects of user-generated content in social media, with a focus on ef<sup>fi</sup>cient and effective access and search support. However, such content has additional characteristics that also deserve our attention. For example, people use social media sites to communicate with others by sharing personal information or exchanging opinions. As such, social network analysis becomes important and can be applied to discover important interactions (communication) patterns among active users of a social media site. Future research therefore should extend the proposed framework by providing additional social network analysis functionality, beyond the reported data integration, search and translation support. Multimedia content represent another important extension. People often share pictures, audio or video <sup>fi</sup>les in social media sites; the multimedia content may contain important information about people and their preferences, opinions, tastes, or behaviors. This study targets text-based user-generated content; therefore, the proposed framework needs to be extended to incorporate multimedia data (such as sounds, pictures, videos) for integrated portals for user-generated content from different social media sites. Continued research is also needed to enrich the current analysis functionalities, such as sentiment analysis, automatic summarization, and user interactive visualization.

## 5. Conclusion

To provide effective support for searching and analyzing usergenerated content that lacks structure and is created in different languages, we propose an integrated framework and use it to develop a forum portal (i.e., DWFP) for the security informatics domain. The proposed framework enables convenient access to the integrated, unstructured user-generated content available in various sources and offers advanced capabilities in data integration, search support, and automatic multilingual translation. This framework is generic and can be applied to build portals in different domains. Our evaluation results demonstrate that DWFP enables people to search and analyze content across different forums and languages more ef<sup>fi</sup>ciently and effectively than several prevalent forum portals. Overall, people evaluate the Dark Web portal higher than the benchmark in term of system quality, usefulness, ease of use, satisfaction, and intention to use it in the near future.

## Acknowledgments

This work is partially supported by the NSF Computer and Network Systems (CNS) Program, (CNS-0709338), September 2007 3–August 2010 and HDTRA1-09-1-0058, July 2009–July 2012. Any opinions, <sup>fi</sup>ndings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily re<sup>fl</sup>ect the views of the National Science Foundation or DOD.

## Appendix A. Experimental tasks used in the study

Q1: Please <sup>fi</sup>nd one forum message from the Arabic forum “Alokab” that has the keyword Al-Qaeda.

Q2: Please <sup>fi</sup>nd one forum message from the Arabic forum “Alokab” that has the keyword Hamas.

Q3: Please <sup>fi</sup>nd one forum thread from the English forum “Islamic Awakening” that has the keyword “bomb” in its title.

Q4: Please <sup>fi</sup>nd one forum message from the English forum “Islamic Awakening” that has the keyword “terrorist” and was posted by the forum user named Daniel.

## Appendix B. Listing of the measurement items used in the study

System quality: Adapted from Chin et al. [13]

A—Overall reactions

QUISA1 Overall, I feel the Dark Web Forum Portal: terrible/wonderfu

QUISA2 Overall, I feel the Dark Web Forum Portal: frustrating/satisfying

QUISA3 Overall, I feel the Dark Web Forum Portal: dull/stimulating

QUISA4 Overall, I feel the Dark Web Forum Portal: dif<sup>fi</sup>cult/easy

QUISA5 Overall, I feel the Dark Web Forum Portal: inadequate power/ adequate power

QUISA6 Overall, I feel the Dark Web Forum Portal: rigid/<sup>fl</sup>exible

## B—Screen

QUISB1 Overall, I feel: Characters on the computer screen (hard to read/easy to read)

QUISB2 Overall, I feel: Highlighting on the screen simpli<sup>fi</sup>es task (not at all/very much)

QUISB3 Overall, I feel: Organization of information on screen (confusing very clear)

QUISB4 Overall, I feel: Sequence of screens (confusing/very clear)

C—Terminology/system information

QUISC1 Overall, I feel: Use of terms throughout system (inconsistent/ consistent)

QUISC2 Overall, I feel: Computer terminology is related to the task you are doing (never/always)

QUISC3 Overall, I feel: Position of messages on screen (inconsistent consistent)

QUISC4 Overall, I feel: Messages on screen which prompt user for input (confusing/clear)

QUISC5 Overall, I feel: Computer keeps you informed about what it is doing (never/always)

QUISC6 Overall, I feel: Error messages (unhelpful/helpful)

## D—Learning

QUISD1 Overall, I feel: Learning to operate the system (dif<sup>fi</sup>cult/easy)

QUISD2 Overall, I feel: Exploring new features by trial and error (dif<sup>fi</sup>cult/easy)

QUISD3 Overall, I feel: Remembering the operations of using the system to <sup>fi</sup>nish tasks is (dif<sup>fi</sup>cult/easy)

QUISD4 Overall, I feel: Tasks can be performed in a straight-forward manner (never/always)

QUISD5 Overall, I feel: Help messages on the screen (unhelpful/helpful)

QUISD6 Overall, I feel: Supplemental reference materials (confusing/clear)

## E—System capabilities

QUISE1 Overall, I feel: System speed (too slow/fast enough)

QUISE2 Overall, I feel: System reliability (unreliable/reliable)

QUISE3 Overall, I feel: Correcting your mistakes (dif<sup>fi</sup>cult/easy)

QUISE4 Overall, I feel: Experienced and inexperienced users' needs are taken into consideration (never/always).

Ease of use: Adapted from Davis [17]

EOU1 I would <sup>fi</sup>nd it easy to use Dark Web Forum Portal to search for forum messages.

EOU2 Learning to use Dark Web Forum Portal to search for forum messages would be easy for me.

EOU3 It would be easy for me to become skillful at using Dark Web Forum Portal to search for forum messages.

Perceived usefulness: Adapted from Davis [17]

PU1 Using Dark Web Forum Portal would help me more quickly to search for forum messages.

PU2 Using Dark Web Forum Portal would be useful to help me search for forum messages.

PU3 Using Dark Web Forum Portal would enhance my effectiveness in searching for forum messages.

Satisfaction: Adapted from Bhattacherjee [6]

SAT1 Overall, my use of Dark Web Forum Portal has left me feeling: Very dissatis<sup>fi</sup>ed/very satis<sup>fi</sup>ed.

SAT2 Overall, my use of Dark Web Forum Portal has left me feeling: Very displeased/very pleased.

SAT3 Overall, my use of Dark Web Forum Portal has left me feeling: Very frustrated/very contented.

SAT4 Overall, my use of Dark Web Forum Portal has left me feeling: Very terrible/very delighted.

Intention to use: Adapted from Bhattacherjee [6]

IU1 If given the opportunity, I would use Dark Web Forum Portal to search for forum messages in future.

IU2 I intend to use Dark Web Forum Portal rather than use any alternative means to search for forum messages in future.

IU3 If I could, I would like to avoid using Dark Web Forum Portal to search for forum messages in future.

## References

[1] M. Abusalah, J. Tait, M. Oakes, Literature review of cross language information retrieval, World Academy of Science, Engineering and Technology 4 (2005) 175–177.

[2] G. Agnew, D. Kniesner, M.B. Weber, Integrating MPEG-7 into the moving image collections portal, Journal of the American Society for Information Science and Technology 58 (9) (2007) 1357–1363.

[3] M. Avital, D. Te'eni, From generative <sup>fi</sup>t to generative capacity: exploring an emerging dimension of information systems design and task performance, Information Systems Journal 19 (4) (2009) 345–367.

[4] T.T. Avrahami, L. Yau, L. Si, J. Callan, The FedLemur Project: federated search in the real world, Journal of the American Society for Information Science and Technology 57 (3) (2006) 347–358.

[5] H. Becker, M. Naaman, L. Gravano, Learning similarity metrics for event identi<sup>fi</sup>- cation in social media, the 2010 ACM International Conference on Web Search and Data Mining (WSDM)ACM Press, New York City, New York, USA, 2010, pp. 291–300.

[6] A. Bhattacherjee, Understanding information systems continuance: an expectation– con<sup>fi</sup>rmation model, MIS Quarterly 25 (3) (2001) 351–370.

[7] R.M. Bittmann, R. Gelbard, Visualization of multi-algorithm clustering for better economic decisions — the case of car pricing, Decision Support Systems 47 (1) (2009) 42–50.

[8] U. Bojārs, J.G. Breslin, A. Finn, S. Decker, Using the Semantic Web for linking and reusing data across Web 2.0 communities, Journal of Web Semantics 6 (1) (2008) 21–28.

[9] W. Boucsein, Psychophysiological investigation of stress induced by temporal factors in human-computer interaction in: M. Frese E. Ulich W. Dzida (Eds.) Psychological Issues of Human Computer Interaction, Elsevier, Amsterdam, 1987, pp. 153–181.

[10] S.A. Brown, V. Venkatesh, A comparison of competing models and an extension of the model of adoption of technology in the household: an investigation of household adoption of personal computers, MIS Quarterly 29 (3) (2005) 399–426.

[11] H. Chen, AI, E-government, and politics 2.0, IEEE Intelligent Systems 24 (5) (2009) 64-86

[12] H. Chen, Building a social media digital library: collection, management, and analytics in: C. Xing E. Crestani A. Rauber (Eds.) The 13th International Conference on Asia-Paci<sup>fi</sup>c Digital Libraries (ICADL)Springer, Beijing, China, 2011, p. 2.

[13] J.P. Chin, V.A. Diehl, K.L. Norman, Development of an instrument measuring user satisfaction of the human–computer interface, Proceedings of SIGCHI '88ACM/SIGCHI, New York, 1988, pp. 213-218.

[14] M.D. Choudhury, S. Counts, M. Czerwinski, Identifying relevant social media content: leveraging information diversity and user cognition, The 22nd ACM Conference on Hypertext and HypermediaACM Press, Eindhoven, Netherlands, 2011, pp. 161–170.

[15] D. Crystal, Weaving a web of linguistic diversity, Guardian Weekly, 2001, (http:// www.guardian.co.uk/GWeekly/Story/0,3939,427939,00.html (Retrieved January 18.2012))

[16] Y. Dang, Y. Zhang, P.J.-H. Hu, S.A. Brown, H. Chen, Knowledge mapping for rapidly evolving domains: a design science approach, Decision Support Systems 50 (2) (2011) 415–427.

[17] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 319–340.

[18] W.H. DeLone, E.R. McLean, Information systems success: the quest for the depen dent variable, Information Systems Research 3 (1) (1992) 60–95.

[19] W.H. DeLone, E.R. McLean, The DeLone and McLean model of information systems success: a ten-year update, Journal of Management Information Systems 19 (4) (2003) 9–30.

[20] M. Diga, T. Kelleher, Social media use, perceptions of decision-making power, and public relations roles, Public Relations Review 35 (4) (2009) 440–442.

[21] J. Forster, E.T. Higgins, A.T. Bianco, Speed/accuracy decisions in task performance: built-in trade-off or separate strategic concerns? Organizational Behavior and Human Decision Processes 90 (1) (2003) 148–164

[22] I.A. Gelman, N. Wu, Combining structured and unstructured information sources for a study of data quality: a case study of Zillow.com, The 44th Hawaii International Conference on System Sciences (HICSS), IEEE Press, Kauai, HI, 2011. 1530–1605.

[23] Global Reach, Evolution of online populations, http://global-reach.biz/globstats/ evol.html 2004 (Retrieved February 18, 2011).

[24] D.L. Goodhue, R.L. Thompson, Task-technology <sup>fi</sup>t and individual performance, MIS Quarterly 19 (2) (1995) 213–236.

[25] J.A. Harkness, A. Villar, B. Edwards, J.A. Harkness, J.A. Harkness, M. Braun, B. Edwards, T.P. Johnson L. Lyberg P.P. Mohler, B.-E. Pennell TW. Smith Translation, adaptation and design, Survey Methods in Multinational, Multicultural and Multiregional Contexts, John Wiley & Sons, Hoboken, NJ, 2010.

[26] B. Harper, L. Slaughter, K. Norman, Questionnaire administration via the WWW: a validation and reliability study for a user satisfaction questionnaire, WebNet 97, Association for the Advancement of Computing in Education, (Toronto, Canada), 1997.

[27] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[28] L. Holcomb, C. Beal, Using Web 2.0 to support learning in the social studies context: our journey from Web 1.0 to Web 2.0 and beyond, in: I.G.e. al. (Ed.), Society for Information Technology & Teacher Education International Conference, AACE, Chesapeake, VA, 2009, pp. 3898–3900.

[29] G.J.F. Jones, Integrating Social Media with Existing Knowledge and Information for Crisis response, in: The 3rd Workshop on Social Web Search and Mining (SWSM 2011): Analysis of User Generated Content Under Crisis at SIGIR 2011, ACM Press, Beijing, China, 2011.

[30] A.M. Kaplan, M. Haenlein, Users of the world, unite! The challenges and opportunities of Social Media, Business Horizons 53 (1) (2010) 59–68.

[31] E. Karahanna, D.W. Straub, N.L. Chervany, Information technology adoption across time: a cross-sectional comparison of pre-adoption and post-adoption beliefs, MIS Quarterly 23 (2) (1999) 183–213.

[32] R. Kawamura, Social media's impact on BI starts with web data services, http:// kapowsoftware.com/blog/index.php/social-media-impact-on-bi-starts-with-webdata-services 2010 (Retrieved January 18, 2012).

[33] D. Kelly, Methods for evaluating interactive information retrieval systems with users, Foundations and Trends in Information Retrieval 3 (1–2) (2009) 1–224

[34] W. Kim, O.-R. Jeong, S.-W. Lee, On social Web sites, Information Systems 35 (2) (2010) 215–236.

[35] B. Marshall, D. McDonald, H. Chen, W. Chung, EBizPort: collecting and analyzing business intelligence information, Journal of the American Society for Information Science and Technology 55 (10) (2004) 873–891.

[36] V. McKinney, K. Yoon, F.M. Zahedi, The measurement of web-customer satisfaction: an expectation and discon<sup>fi</sup>rmation approach, Information Systems Research 13 (3) (2002) 296–315.

[37] T. O'Reilly, What is Web 2.0? Design patterns and business models for the next generation of software, http://www.oreillynet.com/pub/a/oreilly/tim/news/2005/09 30/what-is-web-20.html 2005.

[38] J. Qin, Y. Zhou, M. Chau, H. Chen, Multilingual web retrieval: an experiment in English–Chinese business intelligence, Journal of the American Society for Informa tion Science and Technology 57 (5) (2006) 671–683.

[39] J. Roberts, We have the data — now what??!! A few examples of social media analytics, http://www.collectiveintellect.com/blog/we-have-the-data-now-what-afew-examples-of-social-media-analytics 2011 (Retrieved February 18, 2011).

[40] B. Shneiderman, The eyes have it: a task by data type taxonomy for information visualizations, In Proceedings of the IEEE Symposium on Visual LanguagesIEEE Computer Society Press, Washington, 1996.

[41] J. Sweller, Cognitive load during problem solving: effects on learning, Cognitive Science 12 (2) (1988) 257–285.

[42] T. Talvensaari, M. Juhola, J. Laurikkala, K. Järvelin, Corpus-based cross-language information retrieval in retrieval of highly relevant documents, Journal of the American Society for Information Science and Technology 58 (3) (2007) 322–334.

[43] E. Terman, Five top challenges of integrating social media data with business applications. Enterprise Applications Guest Opinion 2011 (http://www.ctoedge.com/ content/<sup>fi</sup>ve-top-challenges-integrating-social-media-data-business-applications Retrieved January 18. 2012).

[44] V. Venkatesh, M.G. Morris, G.B. Davis. E.D. Davis, User acceptance of information technology: towards a uni<sup>fi</sup>ed view, MIS Quarterly 27 (3) (2003) 425–478.

[45] I. Vessey, D. Galletta, Cognitive <sup>fi</sup>t: an empirical study of information acquisition, Information Systems Research 2 (1) (1991) 63–84.

[46] Y. Wang, J. Zhang, J. Vassileva, A user-centric approach for social data integration and recommendation, The 3rd International Conference on Human-Centric Computing (HumanCom)IEEE Press, Cebu, Philippines, 2010, pp. 1–8.

[47] Y. Zhang, S. Zeng, C.-N. Huang, L. Fan, X. Yu, Y. Dang, C.A. Larson, D. Denning, N. Roberts, H. Chen, Developing a Dark Web Collection and infrastructure for computational and social sciences, IEEE International Conference on Intelligence and Security InformaticsIEEE Press, Vancouver, BC, Canada, 2010, pp. 59–64.

[48] Y. Zhou, J. Qin, H. Chen, J.F. Nunamaker, Multilingual web retrieval: an experiment on a multilingual business intelligence portal, Proceedings of the 38th Annual Hawaii International Conference on System Sciences (HICSS'2005), 2005.

Yan Dang is an assistant professor of computer information systems in the W.A. Franke College of Business at Northern Arizona University. She received her Ph.D. in management information systems from the University of Arizona. Her research interests include the implementation and adoption of information technology, knowledge-based systems and knowledge management, human cognition and decision making, and human computer interaction. Her research has been published in Decision Support Systems, Journal of Management Information Systems, Journal of the American Society for Information Science and Technology, IEEE Intelligent Systems, IEEE Transactions on Systems, Man, and Cybernetics, Part A, and other journals.

Yulei Zhang is an assistant professor of computer information systems in the W.A. Franke College of Business at Northern Arizona University. He received his Ph D. in management information systems from the University of Arizona. His research interests include social computing and social media analytics, text and Web mining, knowledge management, and information technology adoption. His research has been published in Decision Support Systems, Journal of Management Information Systems, Journal of the American Society for Information Science and Technology, IEEE Intelligent Systems, IEEE Transactions on Systems, Man, and Cybernetics, Part A, and other journals.

Paul Jen-Hwa Hu is a Professor and David Eccles Faculty Fellow at the David Eccles School of Business, the University of Utah. He has a Ph.D. in Management Information Systems from the University of Arizona. His current research interests include healthcare information systems and management, technology implementation management, electronic commerce, digital government, human–computer interaction, and knowledge management. He has published papers in Decision Support Systems, Information Systems Research, Journal of Management Information Systems, Decision Sciences, Communications of the ACM, IEEE Transactions on Systems, Man and Cybernetics, etc.

Susan A. Brown is an associate professor of Management Information Systems in the University of Arizona's Eller College of Management. She received her Ph.D. from the University of Minnesota. Her research interests include technology implementation, individual adoption, computer-mediated communication, technology-mediated learning, and related topics. Her research has been published in Decision Support Systems, MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the AIS, Organizational Behavior and Human Decision Processes, and others.

Yungchang Ku is currently a doctoral student in Information Management at Yuan Ze University, Taiwan. He is also an Associate Technical Specialist in the Department of Academic Affairs at Central Police University, Taiwan. He received his master's degree in Information Management from National Central University, Taiwan. His research interests include Web mining and social media analytics.

Jau-Hwang Wang is a professor in the Department of Information Management at Central Police University, Taiwan. He received his Ph.D. in computer science from the University of Minnesota, Minneapolis. His research interests include data mining for law enforcement applications, computer crime investigation and computer forensics, and law enforcement information systems. He has authored/co-authored more than 70 papers published in international/domestic conferences and referred journals.

Hsinchun Chen is a McClelland professor of Information Systems and the Director of the Arti<sup>fi</sup>cial Intelligence Lab at the University of Arizona. He received his Ph.D. in information systems from New York University. He has authored or edited 18 books, 17 book chapters, and more than 180 Science Citation Index journal articles covering digital library, intelligence analysis, biomedical informatics, data/text/Web mining, knowledge management, and Web computing. He serves on 10 editorial boards and has been an adviser for the U.S. National Science Foundation, U.S. Department of Justice, U.S. National Library of Medicine, U.S. Department of Defense, U.S. Department of Homeland Security, and other international research programs. He received the IEEE Computer Society 2006 Technical Achievement award. He is a fellow of IEEE and the American Association for the Advancement of Science (AAAS).
