---
otero_id: 16370
otero_key: "5HEVVJM8"
title: "Factors influencing effective use of big data: A research framework"
authors: "Feliks P. Sejahtera Surbakti; Wei Wang; Marta Indulska; Shazia Sadiq"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.02.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Factors influencing efective use of big data: A research framework

Feliks P. Sejahtera Surbakti<sup>a,c,⁎</sup>, Wei Wang<sup>a</sup>, Marta Indulska<sup>b</sup>, Shazia Sadiq<sup>a</sup>

<sup>a</sup> School of Information Technology and Electrical Engineering, The University of Queensland, St Lucia, QLD 4072, Australia

<sup>b</sup> UQ Business School, The University of Queensland, St Lucia, QLD 4072, Australia

<sup>c</sup> Industrial Engineering Department, Atma Jaya Indonesia Catholic University, Jakarta 12930, Indonesia

## A R T I C L E I N F O

Keywords: Big data Efective use Factors Framework

## A B S T R A C T

Information systems (IS) research has explored “efective use” in a variety of contexts. However, it is yet to specifically consider it in the context of the unique characteristics of big data. Yet, organizations have a high appetite for big data, and there is growing evidence that investments in big data solutions do not always lead to the derivation of intended value. Accordingly, there is a need for rigorous academic guidance on what factors enable efective use of big data. With this paper, we aim to guide IS researchers such that the expansion of the body of knowledge on the efective use of big data can proceed in a structured and systematic manner and can subsequently lead to empirically driven guidance for organizations. Namely, with this paper, we cast a wide net to understand and consolidate from literature the potential factors that can influence the efective use of big data, so they may be further studied. To do so, we first conduct a systematic literature review. Our review identifies 41 factors, which we categorize into 7 themes, namely data quality; data privacy and security and governance; perceived organizational benefit; process management; people aspects; systems, tools, and technologies; and organizational aspects. To explore the existence of these themes in practice, we then analyze 45 published case studies that document insights into how specific companies use big data successfully. Finally, we propose a framework for the study of efective use of big data as a basis for future research. Our contributions aim to guide researchers in establishing the relevance and relationships within the identified themes and factors and are a step toward developing a deeper understanding of efective use of big data.

## 1. Introduction

Efective use is defined in Information Systems (IS) research as the use of a system in a way that increases achievement of goals [1]. A substantial amount of research has investigated this concept [2–5]. For example, Burton-Jones and Grange [1] proposed a theory of the efective use of IS. The theory builds on factors that flow from representation theory but recognizes also that many other factors could drive efective use (e.g., intention to use and organization culture). Similarly, the Technology Acceptance Model (TAM) [6] adapted social-psycholo gical/behavioral theory and introduced perceived ease of use and perceived usefulness factors as antecedents of IS efectiveness. The Unified Theory of Acceptance and Use of Technology (UTAUT) [7] was developed on the basis of social cognitive theory [8] and difusion of in novations theory [9].

While it is clear that efective use has been well studied and theorized from an IS perspective, it has not received much attention in the specific big data context. Yet, efective use of big data is said to have the potential to transform economies and deliver a new wave of growth [10]. At the same time, studies indicate that while most organizations collect vast volumes of data, they do not necessarily utilize that data effectively [11]. Indeed, recent studies indicate that most big data in: itiatives fail to deliver on their expectations and that the failure is often not because of technological issues but because of problems associated with organizational aspects, particularly those related to lack of appropriate planning [12] and poor management of the socio-technical complexity of big data projects [13].

Compared to traditional data held in IS. we note that big data have diferent characteristics – the so-called “V”s – such as volume, velocity, variety, and veracity [14]. Consequently, it requires diferent technologies, methods of analysis, and skills for discovering useful information and insights. Although historically each of the Vs has been tackled to varying levels of success, it is their collective impact that presents a unique set of challenges quite distinct from previous IS research.

Several challenges appear when organizations attempt to implement such complex big data projects and shifts in approaches to generation of insight from data can be observed. Decision support systems in organizations have shifted from being model-driven to data-driven [15]. In model-driven decision support systems, users and analysts interacted primarily with a predefined (mathematical) model and explored its results. Such approaches have been successful in helping to solve welldefined and structured problems (for example what-if-analysis). In data-driven approaches, users (data scientists) interact primarily with the data. This approach promises to solve unstructured, exploratory, and so-called “wicked” problems by identifying relations or patterns in data to gain insights and foresights for decision making. However, given the complexity of the methods, and the size of the data on which they are applied, there are understandably some socio-technical issues within organizations that can become barriers in adopting a data-driven approach to decision making [16,17]. According to IBM [18], 1 out of 3 business leaders does not trust the information they use for decision making. Indeed, one of big data characteristics is veracity, which relates to a lack of data quality, which might influence the credibility of generated insights. Furthermore, there is a belief that a machine cannot replace the instinct and capability of humans [19]. Such resistance and barriers may result in widening of the business-technology divide – an enduring problem that has been the target of years of research in IS – and hence need to be revisited in the specific context of big data initiatives.

While a theory of efective use should provide guidance in such a context, the Theory of Efective Use (TEU) [1] was developed on the basis of traditional IS, which may not accommodate the specific characteristics of big data. Accordingly, and aligned with the thinking of Alvesson and Sandberg [20], we consider a wide range of perspectives to develop a new framework that guides future research in its ex ploration of the efective use of big data. We do so by first taking stock of the prior and current literature on efective use specifically in the big data context. We broaden our literature search to include prior studies on IS/IT efective use and synthesize our findings into key themes on which we then develop a research framework to facilitate the sys tematic study of factors related to efective use of big data.

Our study, therefore, employs a systematic literature review (SLR) method applied to extant IS research, as well as emerging studies in the contemporary big data context. We aim to answer the following three core questions to enable the development of our framework:

What factors are identified in literature relating to the efective use of big data?

What traditional efective use of IS factors might be relevant in the big data context?

• What factors are evident from successful practical implementations of big data projects?

Based on our review, we identify and describe 7 themes that have the potential to influence efective use of big data and conduct a descriptive evaluation of these themes by analyzing 45 published case studies that document successful uses of big data. On the basis of these validated themes, we then propose and describe our framework, which provides directions for future research on efective use of big data, with an ultimate goal to develop a theory of efective use in the big data context.

Our paper is structured as follows. In the next section, we report on the current body of knowledge as it relates to big data, efective use of IS, and efective use of big data. We then explain our method to un dertake the identification of factors and their subsequent thematic analysis and discuss the outcomes of the study in the result section. Finally, we propose a framework for studying efective use of big data and explore how research can proceed on this topic. We conclude the paper with a summary of our contributions and discussion of related limitations.

## 2. Background and related work

The big data phenomenon, which emerged in approximately 2011, is a consequence of over five decades of advancements in data management technology. Starting in the 1960s, the IMS hierarchical model [21] and the CODASYL network model [22] shaped the design of the early commercial databases such as SABRE [23], which was used by IBM to help American Airlines manage reservations data. In the early 1970s, Codd proposed the relational model [24], which pioneered one of the biggest success stories in data management. Relational database management systems (RDBMSs) such as System R [25] and Ingres [26] and, more recently, RDBMSs such as Oracle, DB2, and SQL Server became a commercial success, and Structured Query Language (SQL) became the standard query language in the 1980s.

With the advancement of database systems, new technologies for Data Warehousing for Business Intelligence (BI) systems started to emerge in the 1990s [27]. The architecture of such systems consists of the data warehouse component, or “taking data in” [28], and includes all the challenges of extraction, transforming, and loading (ETL) into the multidimensional data warehouse models [29]; as well as a BI component, which focuses on “taking data out” from the data ware house [28], using analysis methods such as OLAP (online analysis and processing) [30], and data mining to discover insights that support decision making. Most BI systems provide support tools such as dashboards, scoreboards, reports, as well as interactive visualizations for business performance management such as customer relationship management, sales management, profitability analysis, and monthly reporting [27].

The era of big data comes with the prevalence of search engines, social networks, e-commerce websites, smartphones, and the internet of things [27] and is characterized by the so-called “V”s of volume, variety, velocity, and veracity [14]. It is estimated that the amount of data stored in the world's IT systems is doubling about every two years, and enterprises have responsibility for about 85% of that data, much of which is unstructured and does not reside in relational database systems [31]. The database research community has a long history of contributing to query performance for large data [32–34] and data stream processing [35–37] that address volume and velocity issues. More recently, scale-out architectures have been developed to store vast amounts of data. To handle velocity of the data, cloud infrastructures that allow bursting for additional computation power have been developed for real-time data analysis. Despite these technological ad vances, the methods, system architectures, and techniques that were used successfully in the past are no longer suitable or suficient [38] in the big data era, and organizations continue to face challenges in using big data efectively.

In addition to managing and efectively utilizing big data tools and systems, organizations also struggle to recruit and retain big data professionals, or data scientists [16,17]. The need for big data has driven up demand for big data experts (as well as their salaries) while the supply is in shortage. To deal with this pressure, organizations are increasing their budgets, their recruitment and retention eforts, ofering more training opportunities to current staf to develop the required talent, and buying analytics solutions that are designed for users who are not data science experts [39].

In the presence of above-mentioned challenges that have surfaced with the emergence of big data, identifying and understanding the factors that enable or prohibit the efective use of big data is an important and multifaceted problem that requires attention. Below, we present an outline of prior work thus far that has contributed to the understanding of efective use in the more traditional IS setting, as well as in the new big data setting.

## 2.1. Efective use of information systems

A substantial number of prior studies have focused on developing models and theory relating to the use and efective use of IS and technology. The TAM is one such well-tested model of information technology use [40]. It is based on two theories – theory of reasoned action and the expectancy-value model. It suggests that IS usage i determined by two major variables: perceived usefulness and perceived ease of use. The model was further enhanced with the development of the UTAUT [7], which posits that usage behavior is influenced by several factors, including performance expectancy, efort expectancy, social influence, facilitating conditions, gender, age, experience, and voluntariness of use [7]. TAM and UTAUT are considered to be the underpinning theories of information technology use in IS research.

However, to achieve designed objectives or goals, systems must be used efectively, not just used. TEU [1] is a natural progression from studying use, as in TAM and UTAUT, to the study of efective use. TEU is founded on representation theory [1]. It proposes two levels of effective use, namely the nature and the drivers of efective use. Adap tation actions and learning actions are identified as the major antecedents (drivers) of efective use, [41] extended TEU in the context of BI systems, by studying the impact of enterprise architecture maturity stages on efective use. While these studies shed light on efective use of IS in a conventional enterprise setting, they do not consider big data specifically and the unique challenges related to the so-called big data “Vs.” Therefore, we argue that the body of knowledge on the efective use of IS needs to be revisited in the context of big data.

## 2.2. Efective use of big data

Despite the diferent context and diferent characteristics of big data, there is a paucity of research on the efective use of big data. In the big data context, [42] conducted a study to explore whether data quality levels were suficient for intended use. Accordingly, they proposed a model to assess the level of quality in use of big data [42]. To the best of our knowledge [42] is the latest attempt to develop TEU further, particularly to shed light on the efect of data quality on the efective use of big data. A few other studies have explored the efective use of big data in various application settings. For example, efective use of big data has been studied in ambulatory care [43] and neonatal intensive care unit [44]. The use of big data for supply chain management has also been investigated [45]. Moreover, several articles forecast future challenges and trends related to the use of big data, emphasizing the importance of exploiting its benefits [46–49].

In a study of big data value realization, [50] presented an integrated model on big data uses and consequences in organizations. They identify six tensions related to realizing value from big data in organizations and propose two socio-technical attributes, namely portability and interconnectivity, that influence value realization. The study also highlights that the majority of current research is conceptual, rather than empirical, in nature, spanning three levels of analysis: supra-organizational level, organizational level, and workplace level. In doing so, [50] called for further empirical research on what capabilities are needed and their interaction within three levels of analysis to sup porting organization on realizing value from big data. Furthermore, while there is much optimism in relation to big data, [50] stated that the existence of tensions on how organizations realize value from big data suggests a need for deep thinking.

In terms of ofering a specific and operationalized definition of big data analytics capability, [51] presented an extensive list, classification, and definition. The study proposes six research themes: resource orchestration of big data analytics, decoupling big data analytics cap ability from big data enabled capabilities, bounded rationality of big data analytics, turning big data analytics insights into action, trust of top managers in big data analytics insights, and business value measurement.

These studies provide several insights into various aspects of big data use, which further motivate the need to identify and study the factors that impact the efective use of big data. This gap in the body of knowledge is an impediment to the success of projects involving new and large datasets. Such factors may stem from technology, human sources, and organizational capabilities and from the data itself. Thus, developing a comprehensive model of the efective use of big data requires substantial theoretical development, which, in turn, requires the identification of factors, respective measures, and relationships. We aim to contribute toward this goal by proposing a research agenda based on a research framework that narrows down the factor search space for researchers and identifies themes that have the potential to impact ef fective use of big data.

## 3. Approach

Our study follows an SLR approach to ensure synthesis of all relevant prior work to enable the development of the efective use of big data research framework. An SLR is an appropriate approach in our study because it ofers a methodical way to identify, evaluate, and interpret the available studies conducted on a topic, research question, or a phenomenon of interest [52]. It difers from ordinary literature surveys in its formal planning and methodical execution. It is, therefore, an appropriate mechanism for summarizing existing research, identifying gaps in the existing literature, and providing background for positioning new research [52]. In other words, the SLR approach facilitates our mapping and assessment of scientific literature on efective use of big data and leads to a synthesis of findings, which provide the foundation for our research framework.

We conducted our SLR in accordance with the principles recommended by Tranfield et al. [53] and applied the three main steps of planning, execution, and reporting as outlined below.

## 3.1. Planning

At the beginning of the research, we determined the need for a review of potential factors influencing effective use of big data. We conducted an extensive search using Google Scholar, Elsevier's Scopus, IEEE Xplore Digital Library, Web of Science, ACM, ABI/INFORM, EBSCO, JSTOR, and ScienceDirect. Our search indicated that no previous reviews were published on factors related to efective use of big data. Next, we defined an SLR protocol to describe the plan for the review. An SLR protocol specifies in advance the process of identifying relevant research. how the identified research is filtered. the search strategy, exclusion criteria, and the method of synthesis. A comprehensive, unbiased search is one of the fundamental diference between a traditional narrative review and a systematic review [53].

Our SLR began with the selection of bibliographic databases that are most relevant for IS and information and communication technology literature reviews according to Schryen [54], namely IEEE Xplore Digital Library, Scopus, Web of Science, ACM, ABI/INFORM, EBSCO, JSTOR, and ScienceDirect. Next, we identified the keywords and search terms, as relevant to our study. To ensure that all the performed searches were consistent and comparable for each database, we used selected keywords and expressions. The generic search string with a combination of keywords to answer the research question was defined as follows: “big data” AND (“efective use” OR “impact” OR “success” OR “outcome” OR “quality use”) AND (factor OR determinant OR measure\* OR driver OR attribute OR theme OR indicator OR enabler).

To minimize researcher bias during the selection of articles, we defined two levels of inclusion/exclusion criteria, which were applied on the results of the searches. The first set of criteria ensured that we only considered articles written in English and only those where fulltext was available. A second set of exclusion criteria was applied after reading the article titles, abstracts, and keywords, to select relevant articles to be analyzed. An article was identified as relevant if a characteristic of efective use of big data was discussed or mentioned. We consider a characteristic in a broad sense, which includes, factor, measure, or enabler [55]. Furthermore, we included articles that focused on organizational level factors and excluded the ones that solely focused on computing or technical aspects (e.g., software tools and algorithms).

To ensure a broad range of the article sources, we did not limit the articles to just journals and conferences but also extended to other content, e.g., white paper and business magazines. However, as [56] suggested, the use of other articles, i.e., business magazines, newspapers, etc., was restricted to factual information because of low theoretical background in nonacademic articles. We did not define a time span of interest for the identification of relevant articles as we were driven by specific keywords rather than a time-based analysis.

## 3.2. Execution

Conducting the review begins with the identification of study quality assessment, data extraction, and data synthesis. Using search terms mentioned earlier, our search resulted in 5647 articles across the diferent databases – with 249 articles from IEEE Xplore Digital Library, 1243 articles from Scopus, 411 articles from Web of Science, 174 ar ticles from ACM Digital Library, 2696 articles from ABI/INFORM, 173 articles from EBSCO, 585 articles from JSTOR, and 116 articles from ScienceDirect. The selection process began by eliminating articles that met the exclusion criteria. The first author conducted this review, se parating those articles that did and did not match the exclusion criteria. Through this manual process, 5501 articles were removed from the initial set of 5647 articles. Most of the removed articles were technical in nature and related to software/algorithm development or applications, e.g., the big data bootstrap [57], visual analytics for big data [58] and Ibis: interposed big-data i/o scheduler [59], where the use of words such as “factor” or “measure” did not match the context of our study. This step resulted in 146 articles remaining as relevant – 4 from IEEE Xplore Digital Library, 30 from Scopus, 11 from Web of Science, 3 from ACM Digital Library, 62 from ABI/INFORM, 9 from EBSCO, 17 from JSTOR, and 10 from ScienceDirect. An additional 8 articles were re moved because of the duplication of search results across the databases, resulting in 134. We refer to this set of data as the big data set of literature in our paper.

In addition to this approach, we also followed the guidelines of Webster and Watson [60] and reviewed papers cited by the 134 relevant articles. In this second search stage, we considered it also critical to review success factors of traditional IT initiatives and IS success models as they may ofer useful insights for identifying factors that influence efective use of big data. We checked all references from the 134 relevant articles by reading the article titles and reviewing the abstract and full article if needed. Through this process, an additional 72 articles were identified, resulting in a total of 206 articles. We refer to the 72 articles as the IS set of literature in our paper (which is specific to IS/IT success model research only). The stages of the study selection process are summarized in Fig. 1.

Before the data extraction and data synthesis phase, [53] suggested to consider a quality assessment of the articles for conducting a reliable SLR. Quality assessment refers to the appraisal of a study's internal validity and the degree to which its design, conduct, and analysis have minimized biases or errors [53]. We did not wish to introduce a bias by judging articles that had already been published through a peer-review process. Accordingly, we justified the inclusion of articles through the quality assurance processes of peer reviewed journals and conferences. We also made sure that no two studies were included that were based on the same data; had this situation occurred, data of the later study should be used [52]]

The 206 articles were then coded with a dedicated coding protocol. Data coding was performed using a spreadsheet. Excel was used to create a matrix, where the rows represented articles and columns represented factors. The columns (factors) were populated as they were identified. The first author conducted the initial coding through iterative coding of relevant factors influencing efective use of big data of each identified article. The first step was to identify the factors from each study, using the author's original terms. The factors identified could be from the mention of measurement items, actual factors, enablers, implicit text, a use case, and other similar aspects. Because we did not have an a priori list of factors, all possible factors from each study were coded. The results were represented as a matrix mapping of factors to the 206 articles. To ensure those factors were all indeed present, valid, and nothing has been missed, the second author and an independent coder were engaged. The second author selected the articles using stratified random sampling method, 5% of 206 articles (7 from the 134 big data articles and 4 from the 72 traditional IS/IT literature were selected and coded). Afterward, we employed an independent coder and followed the same step as the second author using stratified random sampling method, i.e., 5% of 206 articles were selected excluding the ones that had already been checked by the second author (7 from the 134 big data articles and 4 from the 72 traditional IS/IT literature). The level of percentage agreement between the three coders was 76%, indicating acceptable inter-rater agreement [61]. Subsequently, all researchers worked together to refine the result. Through the above process, we identified a total of 41 factors.

![](/api/attachments/5HEVVJM8/fulltext/images/e29f29a983ba3dcfe4d7750ef133e7e841ed4ecf466c0e478e59d5df68311705.jpg)  
Fig. 1. Stages of the study selection process (adapted from [51]).

## 3.3. Reporting

In our review, we used thematic analysis and descriptive evaluation as the methods of data synthesis and subsequent reporting of the research findings. To make further descriptions more manageable, we aggregated the 41 factors into a smaller number of broader categories (themes). We used content analysis to categorize the factors into themes [61], following the core steps of the following: selecting the unit of analysis, creating categories, and establishing themes [62]. Two coders independently categorized factors into themes following specific guidelines: The themes must reflect the purpose of the research, be exhaustive, and mutually exclusive, which means placement of factors in one theme must be independent of the other themes. The first coder created 9 themes, whereas the second coder produced 7 themes. Therefore, a total of 16 themes were individually created at this stage (with overlap). Afterward, all authors discussed the 16 themes and developed a parsimonious consensus. Through this process, 7 major themes were identified. Reliability analysis was conducted by independent coders to determine whether the themes of 41 factors would be placed into the same themes. Two researchers independently assigned the factors to one of the 7 themes. Each factor could only be placed in one theme. The independent ratings were evaluated using Cohen's kappa, with a result of 92.04%, indicating high inter-rater agreement [61]. Lastly, 100% consensus through discussions was reached among researchers and we classified 41 factors into 7 themes.

While our themes of factors were identified from mostly academic literature, we were motivated to explore to what extent these themes are evident in successful big data projects in practice. To this end, we conducted a descriptive evaluation of our 7 themes. According to [63], a descriptive evaluation is possible where an existing knowledge base is available to build a convincing argument. Accordingly, we analyzed 45 case studies published in “Big Data in Practice: How 45 Successful Com panies Used Big Data Analytics to Deliver Extraordinary Results” [64]. The book presents a unique and in-depth insight into how specific companies use big data. We analyzed these case studies on the basis of our 7 themes of factors.

A coding scheme based on the 7 themes and underlying factors was developed to analyze each case study. The coding scheme consisted of nodes for the 7 themes that were previously identified from the SLR. The text was reviewed and coded by the researchers. NVivo 11 [65] was used to systematically code the published case studies and relate them to our earlier identified themes and their underlying factors. The 45 case studies were loaded into NVivo as documents, and parent nodes (themes) and child nodes (factors) were set up based on results from our SLR. Several iterations of coding were conducted by the first author, with two of the co-authors reviewing the results of the mapping.

## 4. Results

We identified 41 factors through our SLR. Subsequently, we clustered the factors into 7 themes, namely data quality; data privacy and security and governance; perceived organizational benefit; process management; people aspects; organizational aspects; and systems, tools, and technologies. In this section, we first present the summary of findings for the predominant themes in big data (134 articles) and IS literature (72 articles), the distribution of articles by field of literature and the distribution of articles by publication year. We then provide a discussion of each theme. The lists of papers included in the SLR are provided in Appendix A.

Our analysis showed that previous studies identified (implicitly or explicitly) success factors of big data use in various contexts (countries, industries, organizations, and projects) and through various methods (qualitative, quantitative, and mixed). Although some articles proposed common factors, such as top management support, data quality, and system quality, there is no consolidation of this work. Our study addresses this gap and provides a set of factors and themes built from a significant literature base.

As our analysis of literature was based on articles specifically dis cussing big data and expanded to include traditional IS literature focused on IS/IT success factors, we identify, as a result, a set of efective use factors that may apply to both sets of literature because we consider that some traditional IS factors of effective use may also be relevant in the big data context. Before embarking on a detailed description of each theme, we summarize our findings concerning big data-specific themes and themes based on IS/IT literature into the four categories shown in Table 1, based on how frequently they occurred. Our quantifications in Table 1 also indicate the total number of articles that were identified within a particular theme.

In summary, data privacy and security and governance are considered as prominent in big data discussions in the context of efective use, with less focus in IS/IT success models’ literature. On the contrary, the perceived organizational benefit theme has received more attention in IS literature. People aspects, systems, tools and techniques, data quality, and organizational aspects themes have received much attention of researchers regarding IS/IT success models and big data as well. Meanwhile, process management theme has not received much attention in either field. Fig. B1 presents the distribution of articles by field of literature (see Appendix B).

Fig. B2 shows the distribution of articles by publication year. Given that the big data phenomena emerged in approximately 2011, we have split the analysis into two-time windows – one before and one after (and including) 2014. Interestingly, the data privacy and security and governance theme has increased significantly, from 7 to 41 articles; growth of over 70% post 2014 period. In contrast, the perceived organizational benefit theme is the only theme with a downward trend, decreasing by around 23%. The other 5 themes show a slight rise. Process management, data quality, people aspects, organizational aspects and systems, tools and technologies increased by approximately 35%, 28%, 24%, 20%, and 10%, respectively.

In the following, we present a discussion of the 7 themes identified through our SLR and, thus, present the first consolidated view of factors that may potentially influence the efective use of big data. The explanation of themes is structured as follows: First a brief definition of each theme is given, followed by a discussion of the theoretical relevance or empirical evidence presented in reviewed literature. The presentation of themes is ordered based on the highest number of publications related specifically to big data.

## 4.1. Organizational aspects

The organizational aspects theme is concerned with the setting of the organization that may influence efective use of big data and encompass all factors that support or afect efective use of big data at organization level. This theme consists of 13 factors: organizational cultural competence, talent management, change management, strategy alignment, project management, performance management, organizational structure and size, interdepartmental collaboration, communication, top management support, environmental efect, clear goals, and focus on innovation. The theme was repeatedly mentioned in big data-related articles, including discussions of specific factors and measurement items. In our set of 206 articles, 95 discussed organizational aspects. Of these, 64 articles were from big data related articles and 31 articles were from our specific IS literature set of articles. Fig. B3 shows the number of articles that discussed or mentioned factors underlying this theme. Specifically, 47 articles discussed top management support, the most mentioned factor in this theme. Organizational cultural competence was discussed in 37 articles. This factor includes topics related to data-driven decision making [66] (BD\_21), business orientation [67] (BD\_73), and customer orientation [68] (BD\_51). Project management, talent management, and interdepartmental collaboration were another three factors that were repeatedly mentioned among ar ticle coded in this theme. The remainder of factors – change management, strategy alignment, focus on innovation, environmental efects, organizational structure and size. communication. clear goals and performance management – received less attention. The relatively lower focus on these factors, however, should not undermine the importance of their role in efective use of big data.

In Table 2. we present a representative description of each factor from a representative source article. While some factors were identified in multiple articles, we select the most representative definition or description that best explains the meaning behind each factor. We also note that in some cases factors were not yet formally defined in the big data context. In such cases, we quote the well-established definition from the IS literature in Table 2. Definitions or descriptions from big data literature are denoted by an asterisk (\*) in the table.

In our study of the relevant papers within the big data literature, we noted that the majority of the big data papers mention and analyze data-oriented culture as part of the cultural competence factor and highlight its importance for big data initiative success in an organization. Some authors also posit an innovation culture as an essential aspect of organizational cultural competence for big data success [69,70] (BD\_99; BD\_98). In addition to a focus on culture and innovation, prior research explored interdepartmental collaboration. Close collaboration, specifically between the IT department and other business departments, such as HR, finance, and manufacturing, features in [71] (BD\_72). Similarly collaboration and communication with data actors that are external to the organization has been considered [72] (BD\_96). In terms of setting clear goals, there appears to be an underlying debate in the literature that not every form of a big data initiative needs clear goals – see, for example, according to [73] (BD\_94), where the need for clear goals is questioned as a restriction to data-driven discovery of insights.

Table 1  
Most/least studied themes in big data (BD) and information systems (IS) literature.

<table><tr><td></td><td>Big data (BD) literature (134 articles)</td><td>Information systems (IS) literature (72 articles)</td></tr><tr><td>Most studied</td><td>- The organizational aspects theme is the most studied, with 64 articles of the total 95 big data and IS literature articles relevant to this theme coming from literature specific to big data- The systems, tools, and technologies theme is the second largest theme, with 61 of the 96 relevant articles to this theme coming from literature specific to big data- The people aspects theme is discussed specifically in 82 articles, 60 of which are big data specific- The data privacy and security and governance theme is almost exclusively made up of big data specific articles, with 47 of the 48 relevant articles coming from literature specific to big data- The data quality theme is dominated by big data literature based on 44 out of 61 articles relevant to the data quality theme</td><td>- The perceived organizational benefit theme is most studied in IS literature and is discussed in 33 out of 57 big data and IS literature articles relevant to this theme- The organizational aspects theme is next with 31 out of 95 articles relevant to this theme coming from the IS literature set of articles- The people aspects theme is the third most studied in the IS literature set, with 22 out of 82 relevant articles from the BD and IS literature sets of articles- The data quality theme is the fourth most studied in IS literature, 17 out of 61 articles relevant to this theme are coming from IS literature- The systems, tools, and technologies theme is the fifth most studied in IS literature, 33 out of 96 relevant articles to this theme coming from IS literature</td></tr><tr><td>Least studied</td><td>- The perceived organizational benefit theme is the least studied, with 24 big data specific articles focusing on this theme out of total 57 articles- The process management theme is the second least mentioned, with 33 big data-specific articles out of a total of 43 articles</td><td>- The data privacy and security and governance theme in IS literature has not received much attention, only 1 out of 48 articles specific to this theme coming from IS literature- The process management theme has the second smallest number of articles, 10 IS literature specific articles out of 43 articles</td></tr></table>

## 4.2. Systems, tools, and technologies

The systems, tools, and technologies theme refers to the availability of technological support for big data initiatives [74] (BD\_74). Topics related to this theme have received significant attention from researchers in the big data community, as indicated by the theme being the second biggest theme based on the number of big data articles that discuss efective use. Out of 206 articles, 96 discussed systems, tools, and technologies, 61 of which were found within the big data literature. This theme consists of 3 factors, namely system quality, IT infrastructure, and vendor support. Fig. B4 shows the number of articles that

Table 2  
The definition of factors of the organizational aspects theme.

<table><tr><td>Factor</td><td>Definition/references</td></tr><tr><td>Organizational cultural competence</td><td>“A pattern of behaviors and practices by a group of people (in a department, line of business or enterprise) who shared a belief that having, understanding, and using certain kinds of data play a critical role in the success of their business” * (BD_51)BD_21; BD_27; BD_37; BD_51; BD_58; BD_66; BD_72; BD_73; BD_75; BD_76; BD_78; BD_79; BD_83; BD_93; BD_98; BD_99; BD_100; BD_104; BD_107; BD_108; BD_115; BD_116; BD_117; BD_118; BD_119; BD_120; BD_121; BD_122; BD_127; BD_130; BD_131; IS_12; IS_62; IS_63; IS_65; IS_67; IS_72</td></tr><tr><td>Talent management</td><td>“The necessity of providing the organization with the right people (such as data scientists) who are prepared to work with huge sets of data” * (BD_79)BD_12; BD_72; BD_79; BD_83; BD_99; BD_118; BD_121; IS_15; IS_25; IS_33; IS_42; IS_61; IS_64; IS_67</td></tr><tr><td>Change management program</td><td>“The planning, coordinating, organizing, and directing of the processes through which change is implemented, while leadership is aimed at the motivation and influence employees” * (BD_72)BD_72; BD_73; BD_81; BD_82; BD_92; BD_96; BD_116; BD_121; IS_63</td></tr><tr><td>Strategic alignment</td><td>“The degree to which big data is central to the strategy, evidence-based decision making is considered the standard at all levels of the organization” * (BD_86)BD_72; BD_77; BD_86; BD_116; BD_121; BD_128; IS_55; IS_56; IS_66</td></tr><tr><td>Project management</td><td>The application of process, methods, knowledge, skills, and experience to achieve the objectives of big data initiatives * (BD_21)BD_1; BD_10; BD_18; BD_21; BD_93; BD_96; BD_116; BD_121; BD_131; IS_14; IS_15; IS_17; IS_25; IS_26; IS_27; IS_29; IS_30; IS_32; IS_63; IS_64</td></tr><tr><td>Performance management</td><td>The range of activities engaged in by an organization to enhance the performance of a target person or group, to improving organizational effectiveness * BD_114BD_110; BD_113; BD_114; BD_116; BD_121</td></tr><tr><td>Organizational structure and size</td><td>“The formal configuration between individuals and groups regarding the allocation of tasks, responsibilities, and authority within the organization and the number of employees of the firm” * (BD_72)BD_72; BD_93; BD_121; BD_130; IS_59; IS_60; IS_71</td></tr><tr><td>Interdepartmental collaboration</td><td>“An affective and volitional process where departments work together, with mutual understanding, common vision, and shared resources to achieve collective goals” * (BD_5)BD_5; BD_17; BD_18; BD_21; BD_60; BD_72; BD_74; BD_91; BD_112; BD_121; BD_131; IS_15; IS_27; IS_29</td></tr><tr><td>Communication</td><td>“One&#x27;s ability to talk and share information with other actors and stakeholders with no regard to institutionally imposed boundaries” * (BD_96)BD_96; BD_121; BD_131; IS_63; IS_68; IS_72</td></tr><tr><td>Top management support</td><td>“The extent to which top managers in the organization provide direction, authority, and resources during and after the acquisitions of IT systems” * (BD_77)BD_1; BD_2; BD_5; BD_21; BD_23; BD_35; BD_37; BD_39; BD_51; BD_54; BD_62; BD_72; BD_73; BD_77; BD_81; BD_82; BD_88; BD_92; BD_96; BD_98; BD_104; BD_113; BD_115; BD_119; BD_121; BD_122; BD_123; IS_14; IS_15; IS_17; IS_19; IS_25; IS_26; IS_27; IS_28; IS_29; IS_41; IS_42; IS_43; IS_59; IS_61; IS_62; IS_63; IS_64; IS_67; IS_70; IS_72</td></tr><tr><td>Environmental effect</td><td>“The degree of business competition pressure effects the organization” * (BD_92)BD_78; BD_92; BD_104; BD_120; BD_123; IS_60; IS_66</td></tr><tr><td>Clear goals</td><td>Well-established business goals that easy to understand by all people in organization * (BD_94)BD_72; BD_94; BD_96; BD_121; BD_126</td></tr><tr><td>Focus on innovation</td><td>“The degree to which the organization looking to develop and exploit new applications of big data technology” * (BD_93)BD_73; BD_93; BD_96; BD_98; BD_100; BD_119; BD_125; IS_62; IS_71</td></tr></table>

Table 3  
The definition of factors of the systems, tools, and technologies theme.

<table><tr><td>Factor</td><td>Definition/references</td></tr><tr><td>System quality</td><td>“The quality of technical aspects of analytics platform, which are firm specific and develop over time” * (BD_6)BD_1; BD_5; BD_6; BD_8; BD_9; BD_10; BD_11; BD_73; BD_75; BD_76; BD_78; BD_96; IS_4; IS_5; IS_8; IS_10; IS_13; IS_14; IS_16; IS_17; IS_18; IS_21; IS_31; IS_33; IS_39; IS_41; IS_44; IS_45; IS_46; IS_47; IS_48; IS_49; IS_53; IS_58; IS_72</td></tr><tr><td>IT infrastructure</td><td>“The foundation for enterprise technologies, applications, and services that is comprised data, network, and processing architectures” * (BD_74)BD_1; BD_2; BD_4; BD_5; BD_8; BD_9; BD_11; BD_12; BD_13; BD_20; BD_21; BD_23; BD_24; BD_27; BD_28; BD_31; BD_32; BD_33; BD_34; BD_35; BD_36; BD_37; BD_38; BD_40; BD_41; BD_4; BD_46; BD_51; BD_53; BD_55; BD_56; BD_58; BD_61; BD_63; BD_65; BD_66; BD_67; BD_68; BD_69; BD_70; BD_74; BD_78; BD_84; BD_85; BD_89; BD_92; BD_99; BD_115; BD_116; BD_118; BD_121; BD_129; BD_133; IS_2; IS_14; IS_15; IS_21; IS_33; IS_52; IS_54; IS_56; IS_63; IS_67; IS_70; IS_72</td></tr><tr><td>Vendor support</td><td>“The level of technical support offered by the vendor for implementing and using a technology-based solution” (IS_64)BD_10; BD_104; IS_15; IS_41; IS_60; IS_61; IS_64; IS_65; IS_67; IS_70</td></tr></table>

Table 4  
The definition of factors of the people aspects theme.

<table><tr><td>Factor</td><td>Definition/references</td></tr><tr><td>People&#x27;s knowledge and skills</td><td>&quot;The availability of staff with the required knowledge, skillset, and competencies&quot; * (BD_81)BD_2; BD_8; BD_13; BD_17; BD_28; BD_43; BD_64; BD_65; BD_69; BD_72; BD_74; BD_76; BD_77; BD_78; BD_79; BD_81; BD_82; BD_86; BD_89; BD_95; BD_96; BD_99; BD_101; BD_103; BD_109; BD_111; BD_113; BD_114; BD_115; BD_116; BD_118; BD_119; BD_120; BD_121; BD_122; BD_134; IS_11; IS_15; IS_19; IS_28; IS_30; IS_33; IS_60; IS_61; IS_63; IS_71</td></tr><tr><td>Trust</td><td>&quot;The overall trust the users have in the BI system in general and information provided by the BI system in particular&quot; * (BD_91)BD_91; IS_46; IS_54</td></tr><tr><td>Champions</td><td>&quot;A person or some people within the organization who actively supports and promotes the project&quot; (IS_15)BD_23; BD_51; BD_96; IS_15; IS_17; IS_25; IS_26; IS_60; IS_63</td></tr><tr><td>Employee engagement</td><td>Personnel commitment and contribution in big data initiatives * (BD_40)BD_5; BD_19; BD_27; BD_35; BD_37; BD_40; BD_45; BD_47; BD_48; BD_52; BD_59; BD_61; BD_63; BD_66; BD_67; BD_77; BD_104; IS_11; IS_15</td></tr><tr><td>User participation</td><td>User involvement in the implementation of Business Intelligence Systems * (BD_73)BD_68; BD_73; BD_93; IS_1; IS_14; IS_15; IS_43; IS_60; IS_64</td></tr><tr><td>Individual Characteristic</td><td>&quot;The age, computer literacy, education, prior experience, attitude, computer self-efficacy, and computer anxiety&quot; * BD_73BD_73; IS_39; IS_48; IS_53</td></tr></table>

discussed or made mention of these factors while the definition of each factor within the theme is provided in Table 3. IT infrastructure is the most discussed topic in this theme and is dominated by big data articles. Systems quality and vendor support follow, respectively, but are dominated by articles from our IS literature set.

System quality has been identified as a factor influencing big data implementation success through literature review [75] (BD\_78) and empirical studies [76] (BD\_6). In one study, system quality, adopted from the IS success model literature [77] (IS\_5), as well as system accessibility, reliability, integration, adaptability, and response time were identified as key measurements to increase business value in a big data environment [76] (BD\_6). To support efective use of big data, systems need to be reliable, flexible to new demands or conditions, efective in integrating data from diferent datasets, readily accessible to users, and must provide data in a timely fashion while protecting private in formation [78] (BD\_28).

IT infrastructure has been evidenced through SLR [79] (BD\_121) and case study [80] (BD\_116) research. Big data initiatives require appropriate tools and technologies to help organizations to integrate, analyze, visualize, and consume the growing deluge of big data [81] (BD\_5). Similarly, [82] (BD\_8) argued that organizations should be equipped with IT applications that ofer various decision-making tools, simulation tools, what-if analysis tools, statistical tools, and other tools that enable the organizations to examine trends and find the best course of action for a given situation. There is an indication of the need for flexibility with IT infrastructure as well, with [13] (BD\_1) arguing that it is important to be able to easily adjust to use case requirements given the diversity of IT needs in big data projects. In addition, the use of robust platforms to handle multiple sources of data, especially unstructured data, is indicated in prior research as a factor of high importance for efective use of big data [82] (BD\_8). The research indicates that data platforms should evolve to provide specific support for big data and embrace all formats of big data, not just relational big data.

Meanwhile, vendor support has been discussed in the big data literature in the manufacturing industry context [83] (BD\_104). The study highlights technological integration with vendors and importance of periodic audits. Overall, it is clear that a technology-savvy organization is a prerequisite to achieving the objectives of big data initiatives [13] (BD\_1), and understanding the business strategy and choosing the adequate tools and technologies is one of the key success factors in big data projects [13] (BD\_1).

## 4.3. People aspects

The people aspects theme concerns the extent to which employees need and receive assistance in big data initiatives. Out of our 206 articles, 82 discussed factors related to people aspects, including 60 from the literature on big data. This theme consists of 6 factors, namely people's knowledge and skills, trust, champions, employee engagement, user participation, and individual characteristics. Fig. B5 shows the number of articles that discussed or made mention of related factors in our datasets, while the definition of each factor can be found in Table 4.

The majority of articles have focused on people's knowledge and skills, with employee engagement being the second most frequent factor, followed by user participation, champions, and individual characteristics. A variety of research methods have been used in big data literature to identify and study factors relating to this theme. Research methods have ranged from literature review, case studies, surveys, through to interviews. According to prior research, people's knowledge and skills (analytical, technical, and interpretation of analytical results) are critical factors in big data projects [13,67,84] (BD\_1; BD\_73; BD\_64). In one study, researchers found that some companies have created specific units within their organizational structure, with a focus on big data analytics. Through a social content strategy and integration, they have been able to derive value from big data [85] (BD\_70). However, many do not have the required talent in place to derive insights from big data [78,86] (BD\_28; BD\_14). We note that while these topics have been discussed in the big data context, their measurement items derive mostly from IS literature. The IS literature is fertile with relevant factors and measures that have not yet had much attention in the big data space. For example, people support, cham pions, user participation, and their related measurement items (from [87] (IS\_15)) are potential factors related to efective use of big data.

The existence of champions has been emphasized as an important factor in big data initiatives (for example see [10] (BD\_23) and [72] (BD\_96)), with their primary role of ensuring that big data project is seen as a number-one priority in the organization, which is also tasked with ensuring the organization is able to provide the necessary resources to support such projects. Focusing on trust, prior case study and survey research [88] (BD\_91) found that efective use of BI systems is influenced by user trust. The researchers found that people are more likely to trust the system if they have been, and are, continuously involved in system development rather than confronted with systems that have been built independently. Furthermore, through multiple case studies in manufacturing firms, [89] (BD\_77) found that efective big data analytics utilization is also linked to the level of employee en gagement in big data initiatives. In addition to these factors, other case study research has shown that among many individual characteristics such as age, education, computer literacy, etc., personal innovativeness and readiness for change are the most important factors for efective use BI systems [67] (BD\_73). The researchers also argued, along similar lines to [87] (IS\_15), that user participation is an important determinant for intensity of use of BI systems.

## 4.4. Data privacy, security and governance

The data privacy, security and data governance theme feature factors that have been studied extensively in big data context, through a variety of research methods, including SLR, case study, survey, or interview-based research. The theme consists of two factors, namely data privacy and security and data governance. Out of our 206 selected articles, 48 examined data privacy and security and governance, 47 of which were from big data literature. Fig. B6 shows the number of articles that discussed or made mention of related factors, while the de finition of each factor can be found in Table 5.

Of the two factors, data privacy and security theme has received most attention in big data related research. Data privacy and security theme focuses on approaches that address the challenge of secure management of distributed data and data sharing, including data that may contain personally identifiable information [90] (BD\_62). Several studies, in various contexts, found that data privacy and security theme is one of the most crucial factors that can afect the success of big data projects – for example, in the healthcare domain [91,92] (BD\_132; BD\_95), in facility management [93] (BD\_114), and a variety of other industries [71,82,94] (BD\_72; BD\_8; BD\_30). Privacy and security have become a serious concern, and there is a general consensus that traditional security and privacy mechanisms are inadequate for the variety of use cases expected from big data use. Researchers have noted data privacy and security issue as an urgent matter [86,95] (BD\_14; BD\_13). Some of the security challenges have also been identified in the context of data platform use. As there is substantial use of third-party services and (cloud based) infrastructures to host important data or to perform critical operations, the risks are increased. In [94] (BD\_30), poor security and privacy enforcement practices of big data platforms are cited as the main obstacle for the adoption of big data use within organizations. Furthermore, [96] (BD\_65) suggested that privacy issues may cause private/public resistance, which represents a threat for efective big data implementation in organizations.

Big data governance tackles the regulation, management decision making, and procedures over data. It is the entirety of decision rights and responsibilities regarding the management of big data. According to [90] (BD\_62), organizations need to have dependable controls and unambiguous laws, as well as internal policies and guidelines relating to the efective use of big data. These include, but are not limited to, nontransactional data. Data governance was highlighted by some researchers as an important factor for afecting big data projects success, for example [97,98] (BD\_20; BD\_37). Similarly, [99] (BD\_90) stated that implementing big data governance plays an important role in big data adoption, and that successful implementation of data governance is based on a restricted amount of process, procedures and mandated roles and responsibilities. Further, [100] indicated that good data governance will enable the creation of a taxonomy of metadata that represents and distinguishes mission-critical data from less critical data. At the strategic level, a successful data governance process should span the entire spectrum from obtaining data to its use and ensure that big data eforts are undertaken in alignment with business strategy [100].

## 4.5. Data quality

Data quality refers to the fitness of data for an intended purpose [101] (BD\_3). Out of our 206 articles, 61 discussed data quality, including 44 articles from the big data article set. Through our literature review, we identified 7 related factors, namely data quality and information quality, data completeness, data currency, data access, data fitness, data accuracy, and data consistency. We distinguish here between data quality as a general factor and factors that that are related to a specific data quality dimension (e.g., data accuracy or data consistency). We do so on the basis of the level of discussion in related literature. Articles that focused on data quality, without making mention of specific data quality dimensions, were mapped against the general data quality factor. For example, 13 big data articles discuss data quality and information quality as factors that relate to efective use of big data but do not specifically mention or discuss any underlying data quality dimensions, such as data access, data completeness, etc. Fig. B7 shows the number of articles that discuss or make mention of related factors in data quality theme based on big data and IS literature. The definition of each factor can be found in Table 6.

Data quality has been investigated by several researchers in big data context. Data quality is repeatedly cited as a success factor for big data projects [71,79,102] (BD\_72; BD\_121; BD\_63). It has been examined extensively through a variety of ways, including conceptual studies, literature reviews, case studies, survey, and interview-based methods. It has also been studied in a variety of contexts – for example, in healthcare [103] (BD\_42), smart cities [104] (BD\_43), various industries [105] (BD\_57), and in the public sector [102] (BD\_63). Data quality has, of course, also been thoroughly investigated in IS literature. The diference between the traditional approach to data quality and big data quality is that the former approach promises oversight and control over the input, while in the latter the consideration is focused on how data can positively afect the outcome [106] (BD\_11). In our reviewed literature, we found that the terms data quality and information quality were often used interchangeably and frequently shared the same factors (e.g., completeness, accuracy, format, and currency). Some research does, however, diferentiate between data quality and information quality [107] (BD\_3). It defines “data quality” factors are capable of being assessed at the time the data are collected, while “information quality” factors are those that can only be assessed when the data are used, which is an important distinction in the big data use context.

The definition of factors of the data privacy and security and governance theme.

<table><tr><td>Factor</td><td>Definition/references</td></tr><tr><td>Data privacy and security</td><td>“The ways in which organization addressed the challenge of providing effective approaches for secure management of distributed data and data sharing, including those that may contain personally identifiable information (PII)” * (BD_62)BD_1; BD_2; BD_6; BD_8; BD_9; BD_10; BD_13; BD_14; BD_19; BD_23; BD_26; BD_29; BD_30; BD_40; BD_59; BD_62; BD_64; BD_65; BD_66; BD_72; BD_81; BD_82; BD_86; BD_93; BD_95; BD_114; BD_117; BD_120; BD_121; BD_126; BD_127; BD_132; IS_35</td></tr><tr><td>Data governance</td><td>“The entirety of decision rights and responsibilities regarding the management of big data” * (BD_62)BD_7; BD_8; BD_9; BD_11; BD_16; BD_24; BD_27; BD_33; BD_37; BD_44; BD_50; BD_58; BD_62; BD_64; BD_71; BD_86; BD_90; BD_91; BD_109</td></tr></table>

Table 6  
The definition of factors of data quality theme.

<table><tr><td>Factor</td><td>Definition/references</td></tr><tr><td>Data quality and information quality</td><td>“Data quality&#x27; factors are capable of being assessed at the time the data are collected, on the other hand, the &#x27;information quality&#x27; factors are not assessable until the data are used” * (BD_8)BD_8; BD_11; BD_14; BD_15; BD_40; BD_42; BD_50; BD_60; BD_63; BD_65; BD_72; BD_82; BD_116; IS_4; IS_5; IS_8; IS_10; IS_13; IS_15; IS_17; IS_18; IS_22; IS_33; IS_39; IS_44; IS_45; IS_46; IS_47; IS_48</td></tr><tr><td>Data completeness</td><td>“The availability of sufficient contextual information that the data content is not liable to be misinterpreted” * (BD_3)BD_3; BD_6; BD_22; BD_29; BD_57; BD_80</td></tr><tr><td>Data currency</td><td>“The extent to which the information is up to date” * (BD_6)BD_4; BD_6; BD_22; BD_29; IS_16; IS_21; IS_31</td></tr><tr><td>Data access</td><td>“The ability to make data available and can be retrieved from various data resources” * (BD_5)BD_1; BD_2; BD_5; BD_18; BD_20; BD_23; BD_24; BD_27; BD_68; BD_77; BD_84; BD_87; BD_120; IS_16; IS_21</td></tr><tr><td>Data relevance</td><td>“The capacity of the data to meet&#x27;s big data initiatives need” * (BD_73)BD_3; BD_73; BD_78; BD_80; BD_81; BD_83; BD_94; IS_5; IS_21; IS_69</td></tr><tr><td>Data accuracy</td><td>“A high degree of correspondence of the data content with the real-world phenomenon that it is intended to represent, typically measured by a confidence interval, such as ‘±1’ degree Celsius” * (BD_3)BD_3; BD_6; IS_31; IS_38</td></tr><tr><td>Data consistency</td><td>“The validity and integrity of data representing real-world entities” * (BD_57)BD_3; BD_6; BD_22; BD_57; BD_70; BD_121</td></tr></table>

The factors relating to specific data quality dimensions have been studied within big data literature in a variety of ways and with varying degrees of emphasis. According to [105] (BD\_57), data completeness i a central factor of data quality, a vital condition of a firm's IT infrastructure, and a key asset necessary to attain long-term competitive advantage. Data completeness is a useful factor to measure quantitatively the completeness of big data sets within a selected domain to evaluate validity of the analytical data [108] (BD\_29). Another specific data quality factor is currency. Currency reflects when the data item was captured or was last authenticated, or the period over which an average was computed [107] (BD\_3). This factor is relevant to volatile data items in organizations, such as transactional data. Data currency is important because continuous flow of information helps managers make real-time decisions [76] (BD\_6). Data access is another critical data quality factor in big data context. [81] (BD\_5) pointed out that the challenge of big data phenomena is how to handle massive amounts of data generated from a variety of data sources. Data access also become an important factor in the big data context because organizations in creasingly need to integrate information from multiple sources [10] (BD\_23). Accuracy of information has also been highlighted in big data literature, as big data deals with “dirty data” from multiple sources, which need to be organized and processed [76] (BD\_6).

Given that the volume of data can be substantial in big data projects, the relevance of the data to meet users’ needs has been studied in a number of big data articles. Gopalkrishnan et al. [73] (BD\_94) stated that a question that organizations should ask when looking at potential application of big data is whether the available data is relevant given the goal of the big data project. Data relevance is also highlighted as an important factor in the context of business IS to ensure deep structural usage [67] (BD\_73). Lastly, data consistency is considered to be a central factor because it relates to keeping data uniform as they move across the network and are shared by various applications and systems within or between organizations [105] (BD\_57). Strong positive interrelationships have been identified by prior research [105] (BD\_57) between corporate capability of data quality (for example relating to data consistency and data completeness) and compensating experience in data usage.

## 4.6. Process management

The process management theme refers to organizational ability to take action on data while focusing on restructuring business and IT process [74] (BD\_74). Out of our 206 articles, 43 discussed process management, with 33 being big data specific. This theme consists of 3 factors, namely process orientation, IT business process integration, and data management. Fig. B8 shows the number of articles that discussed or made mention of these related factors, and the definition of each factor can be found in Table 7. Data management is the most prominent factor discussed in this theme, followed by IT business process integration, and process orientation. These factors have been studied in the big data context through numerous approaches, including conceptual studies, literature review, multiple case study, survey, and interview-based research.

The process orientation factor relates to how significantly an organization is focused on restructuring business and IT processes to leverage big data opportunities. In practice, many organizations do not structure their processes in ways that optimize the use of big data to make better decisions and facilitate more informed action [74] (BD\_74). Researchers have argued that organizations should move beyond being data-centric and shift to process centric use of big data analytics [109] (BD\_17). In [109] (BD\_17), a theoretical model is developed to study if a business process afords enhanced visibility of big data analytics.

Table 7  
The definition of factors of the process management theme.

<table><tr><td>Factor</td><td>Definition/references</td></tr><tr><td>Process orientation</td><td>&quot;The management of work and budget around end-to-end processes instead of functional units&quot; * (BD_17)BD_17; BD_76; BD_89; BD_106; IS_55; IS_65; IS_66; IS_69; IS_72</td></tr><tr><td>IT business process integration</td><td>&quot;An organizational ability to adapt existing business and IT processes to continually augment their effectiveness and efficiency as well as to leverage the capabilities of emerging information technologies&quot; * (BD_74)BD_4; BD_43; BD_63; BD_66; BD_72; BD_74; BD_77; BD_83; BD_99; BD_103; BD_105; BD_114; BD_120; IS_15; IS_33; IS_41; IS_61; IS_67</td></tr><tr><td>Data management</td><td>&quot;The data management tasks include data governance, data development, data architecture management, data quality, database operations, data security, data warehousing, and business intelligence as well as document management&quot; * (BD_78)BD_72; BD_75; BD_76; BD_77; BD_78; BD_79; BD_81; BD_83; BD_84; BD_87; BD_97; BD_102; BD_103; BD_106; BD_111; BD_113; BD_115; BD_117; BD_118; BD_119; BD_120; BD_121; BD_132; IS_59; IS_64; IS_66; IS_72</td></tr></table>

Other researchers, for example [74], have argued that IT business process integration is a key data analytic capability in organization because of the need to integrate infrastructure, tools, and technologies with business processes to realize value from big data. Some studies [110,111] (BD\_77; BD\_72) have found that IT resources contribute to business value and influence the overall organization performance. Consistent with such previous research, IT business process integration enables organizations to process raw data into useful insights. According to [74] (BD\_74), IT business process integration can be measured by how significant the consistency levels are between application portfolios and business processes. They argue that business process integration is a key mechanism for successful big data analytics.

Furthermore, [112] (BD\_111) posited that the impact of big data on business performance relies on a data management strategy and its execution. They recommend that organizations should re-evaluate their data management strategy and operations to better exploit value from big data.

## 4.7. Perceived organizational benefit

The perceived organizational benefit theme refers to the advance ment of an economic proposition that may not necessarily be measured directly in monetary terms [82] (BD\_8). Of our 206 articles, 57 discussed identifiable business value, of which 24 articles were big data related. The theme consists of 7 factors, namely perceived value, perceived risk, perceived usefulness, perceived ease of use, intention to use, perceived observability, and cost-benefit analysis. Perceived value is the most prominent factor in this theme, based on frequency, followed by cost–benefit analysis, and perceived usefulness. We found that perceived ease of use, perceived usefulness, and intention to use are heavily discussed in the IS literature – these factors are the main factors in the study of efective use of IS. Fig. B9 shows the number of articles that discussed or mentioned the factors related to this theme. The definition of each factor can be found in Table 8. These various factors have been researched through a variety of approaches in the big data context, including SLR [79] (BD\_121), multiple case study [13,113] (BD\_1; BD\_7), surveys [114,115] (BD\_119; BD\_120), and interviewbased methods [82] (BD\_8).

Perceived value of big data analytics use is seen as being most important to understand in highly dynamic environments because big data analytics is expected to increase an organization's capacity to exploit insights from big data [116] (BD\_92). Positive perceived value can influence the efective use of big data [13] (BD\_1). It is related to perceived risk, with the relevant perceived risks consisting of financial, time, security, and general risks [117,118] (IS\_11; IS\_34). A study of the factors influencing adoption of big data [119] (BD\_12) found that perceived risk is a critical factor for predicting the adoption of big data. This is because monetary losses can occur, caused by the increase in the cost of capital and operation as well as loss of time because of unfamiliarity with the installation and usage of big data systems.

Perceived usefulness, a well-established IS construct, has been confirmed to be a significant influence on BI systems use [88] (BD\_91). Perceived ease of use has also been examined in the context of BI system use in organizations through a mixed method investigation [88] (BD\_91) in German-speaking countries (German, Austria, Switzerland, and Liechtenstein). Using survey method, [115] (BD\_75) revealed that successful usage of big data is positively associated with the intention to use of big data. Similarly, using a survey of the telecommunications industry in Malaysia, [114] (BD\_88) found that the greater the perceived observability of BI, the more likely that BI will be successfully deployed.

Finally, [13] (BD\_1) conducted case studies and found that costbenefit analysis has to be implemented to determine to what degree the well-defined business goals are realized by the big data project. Costbenefit factors also should be considered to justify the feasibility of big data initiatives. The components of the costs associated include the adoption big data technologies, maintenance these technologies, and training employees.

## 5. Descriptive evaluation

We recognize the need to validate the themes and, as a first step, we conduct a descriptive evaluation following [63], as described in Section 3. In this evaluation, we use 45 case studies of companies who successfully used big data. These published case studies serve as an insight into which themes and underlying factors afecting efective use of big data have practical significance. To distil this insight, we coded the case studies using the 41 factors, which then automatically mapped into the 7 themes. Fig. B10 presents the number of case studies that indicate the presence of the earlier identified 7 themes.

Our analysis of the case studies found evidence for all of identified themes in practice. Most case studies discussed data privacy, security and governance together with systems, tools and technologies as the themes influencing efective use of big data – they were mentioned in 15 case studies each. For example, in Disney, data privacy and security are discussed as a significant consideration. Organizational aspects theme is the third highest, followed by the people aspects theme. The themes are mentioned in 11 and 10 cases. For instance, LinkedIn's KPIs include revenue and number of members, both of which continue to rise year on year. The rise is attributed to LinkedIn restructuring their data science team so that the decision sciences aspect (which develops the LinkedIn features that generate data for analysis) is now part of en gineering. As such, data science is more integrated than ever at LinkedIn, with analysts becoming more closely aligned with company functions [64]. Interestingly, the data quality theme, which was prominent both in traditional IS literature and specifically in big data effective use literature, is mentioned in only 2 cases. We posit that this might be the case because the focus on successful cases may mean that organizations with poor quality data are not represented – a point that requires further study.

The definition of factors of the perceived organizational benefit theme.

<table><tr><td>Factor</td><td>Definition/references</td></tr><tr><td>Perceived value</td><td>“Identifiable value for the business is delivered from the project” * (BD_1)BD_1; BD_7; BD_8; BD_12; BD_16; BD_20; BD_23; BD_47; BD_71; BD_78; BD_85; BD_88; BD_91; BD_92; BD_124; IS_5; IS_8; IS_9; IS_11; IS_15; IS_16; IS_17; IS_20; IS_23; IS_24; IS_33; IS_34; IS_50; IS_71</td></tr><tr><td>Perceived risk</td><td>“The perception on the possibility of yielding unexpected outcome with undesirable consequences of big data application” * (BD_47)BD_3; BD_12; BD_47; BD_72; IS_11; IS_34</td></tr><tr><td>Perceived usefulness</td><td>“The users’ perception of how the BI system contributes to their daily work and task fulfillment” * (BD_91)BD_10; BD_91; IS_11; IS_16; IS_23; IS_24; IS_34; IS_35; IS_36; IS_37; IS_47; IS_52; IS_57; IS_58</td></tr><tr><td>Perceived ease of use</td><td>“The user&#x27;s perception of how easy it is to work with the Business Intelligence system and to access its functionality” * (BD_91)BD_10; BD_12; BD_25; BD_91; IS_2; IS_3; IS_5; IS_6; IS_14; IS_16; IS_18; IS_21; IS_23; IS_24; IS_34; IS_35; IS_36; IS_37; IS_52; IS_57; IS_58</td></tr><tr><td>Intention to use</td><td>“The first-time adoption intention of big data technology in an organization” * (BD_75)BD_75; IS_6; IS_7; IS_10; IS_11; IS_14; IS_37; IS_51; IS_53</td></tr><tr><td>Perceived observability</td><td>“How visible the results are after a BI system is used” * (BD_88)BD_84; BD_88; IS_35; IS_36; IS_51</td></tr><tr><td>Cost–benefit analysis</td><td>“The technique that is used to determine the best big data technology from a set of alternatives” * (BD_94)BD_1; BD_8; BD_9; BD_71; BD_77; BD_94; BD_99; BD_117; BD_121; IS_15; IS_19; IS_20; IS_47; IS_61</td></tr></table>

![](/api/attachments/5HEVVJM8/fulltext/images/630b3c69d64d3d407ebac80806ea7db7b71b585b5d3e168ad63a09ea9fe5351e.jpg)  
Fig. 2. Framework of efective use of big data.

Our findings from the descriptive analysis indicate that some of the themes appear to have a significant impact in terms of efective use of big data in current big data practices, i.e., data privacy, security and governance, systems, tools and technologies, organizational aspects, and people aspects. However, the factors within the themes of data quality, process management, and perceived organizational benefit have received less attention in practice.

Our analysis of the published case studies also uncovered a factor that was not initially identified through our literature review, namely “Partnerships,” which is distinct from the vendor support factor in systems, tools, and technologies theme. We anticipate that this factor may fit into the theme for organizational aspects but further investigation is required. Nevertheless, partnership is not a new factor and it is well known in practice and management theory. It is common nowadays that organizations maintain both competition and coopera tion [120]. Many organizations collaborate together to reduce their cost [121,122]. However, in big data use context, there is a need to reduce time to value [11]. As indicated by [64], the period of time between a request for a specific business goal and the initial delivery of the value requested can be achieved through partnerships.

There are 6 organizations using big data successfully that specifi cally indicated partnership as a factor that contributes to their efective use of big data (noted in the cases of Pendleton & Son Butchers, US

Olympic Women's Cycling Team, Milton Keynes, Dickey's Barbecue Pit, IBM Watson and Twitter). The factor is specifically focused on estab lishing partnerships and seemingly enables companies that are datarich to work with companies that have advanced analytic capabilities. Through the partnership, the involved organizations can create something more valuable than either of them could alone. For small businesses as Pendleton & Son Butchers, with limited resources and power, a partnership with a Big-Data-as-a-service (BDAAS) provider, who had experience of working with smaller businesses, was crucial to success as it removed the need to invest in new systems and staf with data ex perience and also reduced time to value [64].

## 6. Research framework and agenda

By conducting an SLR and documenting what is known to date, we were able to identify prominent areas of research that are of high relevance to the phenomenon of study, that is efective use of big data. On the basis of our earlier introduced themes, their underlying factors, and their potential impact on efective use of big data, we develop a framework that provides a starting point for future research to achieve a more nuanced understanding of efective use of big data. We aim for a parsimonious framework that accomplishes a desired level of explanation with as few categories as possible. Accordingly, we classify our themes into 3 categories namely motivational, operational and supporting mechanisms, and develop related propositions to inform a research agenda and highlight areas of research that warrant further study to develop requisite knowledge on efective use of big data. We posit that efective use is the ultimate objective of big data use, im pacted by the three categories of themes, and can hence be measured by the value realization (commercial or social good) construct. The framework is presented in Fig. 2.

The motivational category in our research framework refers to the theme that focuses on the reason for engaging in big data use in an organization. We argue that the perceived organizational benefit theme is one that arouses and sustains the desire of an organization to use big data efectively, which can be reflected by its constituent factors, such as perceived value, perceived risk, perceived usefulness, perceived ease of use, intention to use, perceived observability, and cost-benefit analysis. Factors related to perceived organizational benefit will pro vide the necessary motivation for the organization to undertake a big data project. The influence of this category is supported by our litera ture review, for example, [13] stated that organizations need to focus on generating return on investment (ROI) and conducting cost-benefit analysis before big data projects kick-of. Grounded in our analysis of the literature, we propose the following proposition:

Proposition 1. Efective use of big data is influenced by perceived organizational benefit

The operational category includes the themes that may directly influence efective use of big data. The operational category comprises of three themes: process management; data security, privacy and governance; and data quality that are, in turn, reflected by respective factors (see Sections 4.4–4.6). We argue that operational excellence would allow an organization to successfully execute a big data project and achieve efective use through value realization of big data. This is supported by our literature review, for example, according to [123], a clear data governance function is critical to ensure a meaningful use of the data. Based on our analysis of the literature, we propose the following proposition:

Proposition 2. Efective use of big data is influenced by process management; data privacy, security and governance; and data quality.

The third category of our framework is supporting mechanisms. Supporting mechanisms accompany and ensure the functioning of the various factors within the operational category and indirectly or directly may contribute to value realization of big data use. It consists of 3 themes: people aspects, organizational aspects and systems, and tools and technologies, which are reflected by their underlying factors (see Sections 4.1–4.3). Our literature review provides evidence of the influence of this category on efective use of big data. For example, [124] argued that top management support, IT infrastructure, and organiza tional culture change are essential to any big data project's success. Based on our analysis of the literature, we propose the following proposition:

Proposition 3. Efective use of big data is influenced by people aspects, organizational aspects and systems, and tools and techniques.

We note that to adequately explore these propositions, the following research questions also need to be answered.

What is the relative importance of the factors in each theme in af fecting efective use of big data?

The results of our review show that some factors have been extensively studied, some have been moderately studied, and others have been overlooked in the big data research context. For example, there is a paucity of research that is narrowly focused on explaining the perceived ease of use in the big data context [88], yet this factor has been studied extensively in IS literature [125–127]. Yet, it is evident that understanding ease of use (perceived and actual) in the big data context may hold several new challenges, given the unique characteristics and settings of big data projects. Despite the varied extent of research focus on the factors, we cannot conclude that extensively studied factors are more important than the understudied factors in influencing the efective use of big data. It is, therefore, desirable to empirically explore and establish which factors are important and what is their relative importance in influ encing the efective use of big data. The importance of factors may also be case-dependent [113] and cannot be generalized across sectors or industries. Furthermore, it may also depend on the maturity of big data use in the organization, that is whether they are in the stage of nascent, early, corporate, or mature adoption [100].

What are appropriate measurement items for factors influencing the efective use of big data?

Deficiencies of current measures for the factors need to be studied to enable a better understanding of efective use of big data. While some measures exist, and others could be adapted (for example those from IS literature), new measures may need to be developed and tested. For example, user participation has been discussed in three papers within big data use context [49,67,128]; however, none of these articles have indicated what measures are appropriate and if they are likely to difer in the big data context. Researchers rely on the established measurement items for their consistent reliability; thus, when the context changes (e.g., from IS use to big data use) but the measurement instruments remain the same, validity is doubtful [129]. This primary research step should be supported by further empirical studies to discover specific measurement items of factors influencing efective use of big data and to test if the new measurement instruments satisfy validity criteria.

• What other factors may afect efective use of big data?

Future research should also follow an exploratory empirical route to identify any yet unknown factors that are necessary for efective use of big data. For example, data quality is a multidimensional concept [130] and among current studies there is no comprehensive research about which known data quality dimensions (such as accuracy, completeness, etc.) are more important for efective use of big data. Nor is there an indication of whether new dimensions of data quality in the big data context (such as minimum size of the data) may need to be considered. This opens new research avenues in this still emerging topic and can lead to new findings on critical dimensions or factors of big data quality.

In addition to the three propositions, we also observed interrelationships between the categories. Organizations invest in systems, tools, and technologies, recruit and train people to work well in the big data ecosystem, and provide supporting working environment and organization culture if they see and believe in the benefit of big data utilization. Similarly, for the opposite direction, the supporting mechanisms of people aspects, organizational aspects, and systems, tools, and technologies help enable the perceived organizational benefit of big data. For example, if the organizations have the right tools, for instance, interactive visualization, they will be able to articulate their value proposition better. This implies the following:

Proposition 4. There is an interrelationship between the motivational factors and factors relating to support mechanisms.

In similar vein, organizations execute process management, create data security, privacy and governance mechanisms, and maintain data quality if they get benefit from big data usage, and benefit drives further investment in operations. For instance, [131] indicated that as the value of big data becomes more apparent, big data governance will gain further importance as an organization's support system that focuses on leveraging enterprise-wide big data resources to realize value from big data. We, therefore, state the following exploratory proposition:

Proposition 5. There is an interrelationship between motivational and operational factors.

We postulate support mechanisms, which include people aspects, organizational aspects, and systems, tools, and technologies, serve as a facilitator for the operational factors, to promote process management, to actualize good data governance, and to create good data quality. Meanwhile, support mechanism-related factors are also afected by operational ones. For example, [98] argued that the people, organiza tion, and technologies are afected by contextual factors such as big data governance. The following is, therefore, proposed:

Proposition 6. There is an interrelationship between the operational factors and factors relating to support mechanisms.

Following Propositions 3–6, we highlight some additional questions that require consideration to adequately explore these propositions.

What are the interrelationships between the identified themes and their underlying factors?

Further research is needed to study the relevance and interrelationships between identified themes and their underlying factors, and their impact on efective use of big data, as has been done, for example, by [38]. In [38], researchers found that data security and privacy afects process management and, in turn, impacts on value realization of big data. Our proposed framework aims to guide researchers in what should be studied but thus far outlines only high-level relationships between the categories of themes based on prior work. While this is a starting point, a finer granularity perspective, at the factor and theme level, is required to develop a deeper understanding of efective use of big data and provide guidance for organizations such that value of big data can be realized. Efective use has been studied and theorized by [1] in the context of IS on the basis of representation theory. However, what efective use means and how to measure this phenomenon in the specific context of big data is insight that is currently lacking, as is evidenced by our literature review. Our research framework and its constituent themes and factors present a starting point for pursuing these questions. However, we also argue that further study of these foundational questions is worthwhile to conduct and may lead to developing a new middle range theory of efective use in big data context, as well as testing the applicability of existing theories in the big data context. Therefore, we propose the following research question.

What does efective use as a conceptual variable represent and how to measure efective use in big data context?

Our research findings also contribute to extending the integrated model of big data value realization by [50]. In their model, the authors consider process management, organizational aspects and supra-organizational aspects. Process management refers to in ductive and deductive approaches in big data analytics and algorithmic and human-based intelligence. Organizational aspects are considered to incorporate centralized and decentralized big data capability structures, big data-driven business model improvement, and innovation. Finally, the supra-organizational aspect reflects controlled and open access to big data and minimizing and neglecting the social risks of big data value realization. Our framework extends these considerations to include data privacy, security, governance and data quality as other important aspects. Specifically, we present process management, data privacy, security and governance and data quality as prominent themes in efective use of big data, as part of the operational category, which implies they are vital themes to generate value to the organization. We agree with [69,71,92,102,132,133], which identified data quality as a critical factor for big data initiative success. We also argue, on the basis of [92,123,131,134,135], that data privacy and security and governance are essential for efective use big data. The themes in this category are particularly novel and extend findings from prior research (see [50,51]). Furthermore, whereas, prior studies have contributed several important findings, we argue that the assembly of the three categories of themes, and their respective factors, and measurements enables our framework to provide the most com prehensive avenue for positioning the future study of efective use of big data.

We note that the framework is intended for use at organizational level; however, we acknowledge that organizations are part of a big data ecosystem that involves other actors, such as government/public organizations, entrepreneurs, and researchers [136]. For example: governments create new regulations, policies, and standards in privacy and security management; public organizations can share their data; entrepreneurs can be partners in value co-creation and ideation; and education institutions provide capable data scientists. Our framework can be referenced by big data actors as the basis for collaboration in the wider stakeholder community, which, in turn, is a necessary prelude to developing and ofering better products and services with the organization.

## 7. Concluding discussion

Big data is a complex phenomenon, and understanding the technical, organizational, and human factors that contribute to its efective use are key to provide organizations with guidance for improved outcomes from their big data projects. This study is the first comprehensive attempt to explore factors that may influence efective use of big data, summarized in a research framework. This research has synthesized previous studies relating to factors on the efective use of big data using an SLR method [64]. We identified 41 factors and used thematic analysis to arrive at 7 main themes of factors, namely organizational aspects; systems, tools, and techniques; people aspects; data privacy and security and governance; data quality; process management and perceived organizational benefit. These themes and the underlying factors should be considered further to comprehensively study efective use of big data. We further clustered these themes into 3 categories, namely support mechanisms, operational, and motivational. Based on the review, we have proposed a research framework and ensuing research agenda that provides a comprehensive avenue for positioning the study of efective use of big data.

The results of this study are supported by previous literature on big data analytics capability that defined big data analytics capability as “the ability of data actors to efectively deploy technology and talent to capture, store, and analyze data toward value creation, business change, and societal change” [136]. According to [136], big data analytics cap ability consists of technology and infrastructure, technical and management skills, organization learning, and data-driven culture. Further, [51] have identified a number of themes such as big data analytics resource orchestration, trust of top managers in big data analytics in sights, and business value measurement, which have informed a number of themes in the supporting mechanisms and motivational ca tegory of our research framework.

Our study is not without limitations. First, the proposed framework is intended for use at the organizational level; however, we acknowledge that big data ecosystems involve other actors that are not specifically addressed by this study. Second, the use of secondary data sources is a limitation, including the use of published case studies. Last, as with all literature review studies, it includes human judgment during the review and coding process. We have mitigated these through the use of a multicoder approach.

In our concluding note, we encourage researchers to apply sophisticated methodological approaches to strong build evidence of factors, and relationships between them, to study efective use of big data. Such research will ultimately lead to the development of a theory of efective use of big data. Substantive theory-building eforts are required to ensure an adequate consideration of the complex problem represented by big data.

## Acknowledgement

The authors gratefully acknowledge the LPDP (Indonesia Endowment Fund for Education) for supporting this research with a PhD scholarship grant to the first author.

## Appendix A. Supplementary data

Supplementary material related to this article can be found, in the online version, at https://doi.org/10.1016/j.im.2019.02.001.

## References

[1] A. Burton-Jones, C. Grange, From use to efective use: a representation theor

perspective, Inf. Syst. Res. 24 (3) (2012) 632–658.

[2] M.-C. Boudreau, L. Seligman, Quality of use of a complex technology: a learning based model, Contemp. Issues End User Comput. 17 (248) (2006) 1–22.

[3] C. LeRouge, A.R. Hevner, R.W. Collins, It's more than just use: an exploration of telemedicine use quality, Decision Support Syst. 43 (4) (2007) 1287–1304.

[4] R. Agarwal, C.M. Angst, C.M. DesRoches, M.A. Fischer, Technological viewpoints (frames) about electronic prescribing in physician practices, J. Am. Med. Inform. Assoc. 17 (4) (2010) 425–431.

[5] P.A. Pavlou, A. Dimoka, T.J. Housel, Efective use of collaborative IT tools: nature, antecedents, and consequences, Hawaii International Conference on System Sciences, IEEE, 2008, pp. 40–52

[6] P. Legris, J. Ingham, P. Collerette, Why do people use information technology? A critical review of the technology acceptance model, Inform. Manage. 40 (3) (2003) 191–204.

[7] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a unified view, MIS Q. (2003) 425–478.

[8] D. Compeau, C.A. Higgins, S. Huf, Social cognitive theory and individual reac tions to computing technology: a longitudinal study, MIS Q. (1999) 145–158.

[9] G. Premkumar, K. Ramamurthy, S. Nilakanta, Implementation of electronic data interchange: an innovation difusion perspective, JMIS 11 (2) (1994) 157–186.

[10] J. Manyika, et al., Big Data: The Next Frontier for Innovation, Competition, and Productivity, (2017) Available: http://www.mckinsey.com/insights/mgi/ research/technology\_and\_innovation/big\_data\_the\_next\_frontier\_for\_innovation (accessed on: 4 August).

[11] S. LaValle, E. Lesser, R. Shockley, M.S. Hopkins, N. Kruschwitz, Big data, analytics and the path from insights to value, MIT Sloan Manage. Rey. 21 (2) (2013) 20–31

[12] B. Marr, Where big data projects fail, Forbes (2015) Available: http://www.forbes. com/sites/bernardmarr/2015/03/17/where-big-data-projects-fail/# 24de1890264e (accessed on 17.3.2015).

[13] J. Gao, A. Koronios, S. Selle, Towards a process view on critical success factors in big data analytics projects, AMCIS (2015) 1–14.

[14] A. De Mauro, M. Greco, M. Grimaldi, What is big data? A consensual definition and a review of key research topics, AIP Conf. Proc. 1644 (1) (2015) 97–104.

[15] D.J. Power, R. Sharda, F. Burstein, Decision Support Systems, Wiley Online Library, 2015.

[16] A. McAfee, E. Bryniolfsson, Big data: the management revolution, Hary. Bus. Rey. 90 (10) (2012) 60–68.

[17] T.H. Davenport, D. Patil, Data scientist, Harv. Bus. Rev. 90 (5) (2012) 70–76.

[18] S. LaValle, Business Analytics and Optimization for the Intelligent Enterprise, IBM Institute for Business Value. 2009.

[19] M. Chui, J. Manyika, M. Miremadi, Where machines could replace humans—and where they can’t (yet), Digital McKinsey 7 (2017) Available: http://www. mckinsey.com/business-functions/digital-mckinsey/our-insights/ (accessed on: August 20).

[20] M. Alvesson, J. Sandberg, Generating research questions through problematiza tion, Acad. Manage. Rev. 36 (2) (2011) 247–271.

[21] S. Banerjee, B.P. Carlin, A.E. Gelfand, Hierarchical Modeling and Analysis for Spatial Data, Chapman and Hall/CRC, 2004.

[22] C. Batini, S. Ceri, S.B. Navathe, Conceptual Database Design: An Entity-Relationship Approach, Benjamin/Cummings Redwood City, CA, 1992.

[23] R. Ramakrishnan, J. Gehrke, Database Management Systems. McGraw Hill. 2000

[24] E.F. Codd. A relational model of data for large shared data banks. CACM 13 (6) (1970) 377–387.

[25] M.M. Astrahan, et al., System R: relational approach to database management, ACM Trans. Database Syst. 1.(2) (1976) 97–137.

[26] M. Stonebraker, G. Held, E. Wong, P. Kreps, The design and implementation of INGRES, ACM Trans. Database Syst. 1 (3) (1976) 189–222.

[27] H.J. Watson, B.H. Wixom, The current state of business intelligence, Computer 40 (September) (2007) 96–99.

[28] H. Chen, R.H. Chiang, V.C. Storey, Business intelligence and analytics: from big data to big impact, MIS O. 2012 (2012) 1165–1188.

[29] P. Vassiliadis, A survey of extract–transform–load technology, Int. J. Data Warehous, Min, 5 (2009) 1–27.

[30] S. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, ACM Sigmod Record 26 (1997) 65–74.

[31] IDC, The Digital Universe of Opportunities: Rich Data and the Increasing Value of the Internet of Things, (2017) Available: https://www.emc.com/leadership/ digital-universe/2014view/index.htm (accessed on: July 12).

[32] D. Abadi, S. Madden, M. Ferreira, Integrating compression and execution in column-oriented database systems, Proceedings of the 2006 ACM SIGMOD International Conference on Management of Data, ACM, 2006, pp. 671–682.

[33] H. Wang, K. Zheng, X. Zhou, S. Sadiq, SharkDB: an in-memory storage system for massive trajectory data, Proceedings of the 2015 ACM SIGMOD International Conference on Management of Data, ACM, 2015, pp. 1099–1104.

[34] G. Candea, N. Polyzotis, R. Vingralek, Predictable performance and high query concurrency for data analytics. Int. J. Very Large Data Bases 20 (2) (2011) 227-248.

[35] D. Jiang, G. Chen, B.C. Ooi, K.-L. Tan, S. Wu, epiC: an extensible and scalable system for processing big data, Proc. VLDB Endowment 7 (7) (2014) 541–552.

[36] D.J. Abadi, et al., Aurora: a new model and architecture for data stream management, Int. J. Very Large Data Bases 12 (2) (2003) 120–139.

[37] B. Babcock, S. Babu, M. Datar, R. Motwani, J. Widom, Models and issues in data stream systems, Proceedings of the Twenty-first ACM SIGMOD-SIGACT-SIGART Symposium on Principles of Database Systems, ACM, 2002, pp. 1–16.

[38] A. Siddiqa, et al., A survey of big data management: taxonomy and state-of-the-art, J. Netw. Comput. Appl. 71 (2016) 151–166.

[39] Datamation, Big Data Challenges, (2017) Available: https://www.datamation. com/big-data/big-data-challenges.html (accessed on: August 23).

[40] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Manage. Sci. 35 (8) (1989) 982–1003.

[41] T.V.H. Trieu, Extending the theory of efective use: the impact of enterprise architecture maturity stages on the efective use of business intelligence systems, International Conference on Information Systems (ICIS 2013): Reshaping Society Through Information Systems Design, vol. 2 (2013) 1649–1659.

[42] J. Merino, I. Caballero, B. Rivas, M. Serrano, M. Piattini, A data quality in use model for big data, Fut. Gener. Comput. Syst. 63 (2016) 123–130.

[43] J.H. Thorpe, E.A. Gray, Big data and ambulatory care: breaking down legal barriers to support efective use, J. Ambul. Care Manage. 38 (1) (2015) 29–38.

[44] T. Vijayalakshmi, V. Kumar, J. Gokulraj, A. Malathy, Efective use of bigdata and social media in – neonatal intensive care unit, Int. J. Eng. Res. Technol. 4 (2015) 442–444.

[45] B.T. Hazen, C.A. Boone, J.D. Ezell, L.A. Jones-Farmer, Data quality for data sci ence, predictive analytics, and big data in supply chain management: an introduction to the problem and suggestions for research and applications, Int. J. Prod, Econ, 154 (2014) 72–80.

[46] M.D. Assunçaoa, R.N. Calheirosb, S. Bianchia, M.A. Nettoa, R. Buyyab, Big Data Computing and Clouds: Challenges, Solutions, and Future Directions, Technical Report CLOUDS-TR-2013-1, University of Melbourne: Cloud Computing and Distributed Systems Laboratory, 2013.

[47] K. Kambatla, G. Kollias, V. Kumar, A. Grama, Trends in big data analytics, J. Parallel Distrib. Comput. 74 (7) (2014) 2561–2573.

[48] C.P. Chen, C.-Y. Zhang, Data-intensive applications, challenges, techniques and technologies: a survey on big data. Inform, Sci, 275 (2014) 314–347.

[49] V. Huser, J.J. Cimino, Impending challenges for the use of big data, Int. J. Radiat. Oncol. Biol. Phys. 95 (3) (2016) 890–894.

[50] W.A. Günther, M.H.R. Mehrizi, M. Huysman, F. Feldberg, Debating big data: a literature review on realizing value from big data, J. Strateg. Inform. Syst. (2017) 191-209.

[51] P. Mikalef, I.O. Pappas, J. Krogstie, M. Giannakos, Big data analytics capabilities: a systematic literature review and research agenda, Inform. Syst. e-Bus. Manage. (2017) 1–32.

[52] B. Kitchenham, Procedures for Performing Systematic Reviews, vol. 33, no. 2004, Keele University, Keele, UK, 2004, pp. 1–26.

[53] D. Tranfield, D. Denyer, P. Smart, Towards a methodology for developing evidence-informed management knowledge by means of systematic review. Br. J Manage, 14 (3) (2003) 207–222

[54] G. Schryen, Writing qualitative IS literature reviews – guidelines for synthesis, interpretation and guidance of research, Commun. AIS 37 (12) (2015) 286–325

[55] C. Okoli, K. Schabram, A guide to conducting a systematic literature review of information systems research, Sprouts: Working Pap. Inform. Syst. 10 (26) (2010) 10–26.

[56] Y. Levy, T.J. Ellis, A systems approach to conduct an efective literature review in support of information systems research, Inform. Sci.: Int. J. Emerg. Transdiscipl. 9 (1) (2006) 181–212.

[57] A. Kleiner, A. Talwalkar, P. Sarkar, M. Jordan, The big data bootstrap, International Conference on Machine Learning (2012) 1759–1766.

[58] K. Cook, et al., VAST challenge 2012: visual analytics for big data, 2012 IEEE Conference on Visual Analytics Science and Technology (VAST), IEEE, 2012, pp. 251-255

[59] Y. Xu. M. Zhao. Ibis: interposed big-data i/o scheduler. Proceedings of the 25th ACM International Symposium on High-Performance Parallel and Distributed Computing, ACM, 2016, pp. 111–122.

[60] J. Webster, R.T. Watson, Analyzing the past to prepare for the future: writing a literature review, MIS Q. 26 (2) (2002) xiii–xxiii.

[61] S. Stemler, An overview of content analysis, Pract. Assess. Res. Eval. 7 (17) (2001) 137-146

[62] J.Y. Cho, E.-H. Lee, Reducing confusion about grounded theory and qualitative content analysis: similarities and differences, Qualitat, Rep. 19 (32) (2014) 1–20

[63] A.R. Hevner, A three cycle view of design science research, Scand. J. Inform. Syst. 19 (2007) 87–92.

[64] B. Marr, Big Data in Practice: How 45 Successful Companies used Big Data Analytics to Deliver Extraordinary Results, John Wiley & Sons, 2016.

[65] M.B. Miles, A.M. Huberman, Oualitative Data Analysis: An Expanded Sourcebook Sage Publications, Thousand Oaks, CA, 1994.

[66] D. Dutta, I. Bose, Managing a big data project: the case of ramco cements limited, Int. J. Prod. Econ. 165 (2015) 293–306.

[67] T. Grublješič, J. Jaklič, Conceptualization of the business intelligence extended us model, J. Comput. Inform. Syst. 55 (3) (2015) 72–82

[68] D. Kiron, R. Shockley, Creating business value with analytics, MIT Sloan Manage. Rev. 53 (1) (2011) 57–71.

[69] A. Marshall, S. Mueck, R. Shockley, How leading organizations use big data and analytics to innovate, Strategy Leadership 43 (5) (2015) 32–39.

[70] Bradford, Leaders, strugglers and strivers. Big data's role in driving innovation, Strateg, Direct, 32 (3) (2016) 1–3.

[71] P. Cato, P. Gölzer, W. Demmelhuber, An investigation into the implementation factors affecting the success of big data systems. 2015 11th International Conference on Innovations in Information Technology (IIT), IEEE, 2015, pp. 134-139

[72] D. Hawley, Implementing business analytics within the supply chain: success and fault factors, Electron. J. Inform. Syst. Eval. 19 (2) (2016) 112–121.

[73] V. Gopalkrishnan, D. Steier, H. Lewis, J. Guszcza, Big data, big business: bridging the gap, Proceedings of the 1st International Workshop on Big Data, Streams and

Heterogeneous Source Mining: Algorithms, Systems, Programming Models and Applications, ACM, 2012, pp. 7–11.

[74] G. Shuradze, H.-T. Wagner, Towards a conceptualization of data analytics capabilities, 2016 49th Hawaii International Conference on System Sciences (HICSS), IEEE, 2016, pp. 5052–5064.

[75] C. Adrian, R. Abdullah, R. Atan, Y.Y. Jusoh, Factors influencing to the im plementation success of big data analytics: a systematic literature review, 2017 International Conference on Research and Innovation in Information Systems (ICRIIS), IEEE, 2017, pp. 1–6.

[76] S. Ji-fan Ren, S. Fosso Wamba, S. Akter, R. Dubey, S.J. Childe, Modelling qualit dynamics, business value and firm performance in a big data analytics environment, Int. J. Prod. Res. (2016) 1–16.

[77] W.H. Delone, E.R. McLean, The DeLone and McLean model of information systems success: a ten-year update, JMIS 19 (4) (2003) 9–30.

[78] X. Zhu, B. Song, Y. Ni, Y. Ren, R. Li, Big data—from raw data to big data, Business Trends in the Digital Era, Springer, 2016, pp. 1–22.

[79] J.S. Saltz, I. Shamshurin, Big data team process methodologies: a literature review and the identification of key factors for a project's success, 2016 IEEE International Conference on Big Data (Big Data), IEEE, 2016, pp. 2872–2879.

[80] L. Muller, M. Hart, Updating business intelligence and analytics maturity model for new developments, International Conference on Decision Support System Technology, Springer, 2016, pp. 137–151.

[81] S.F. Wamba, S. Akter, A. Edwards, G. Chopin, D. Gnanzou, How ‘big data’ can make big impact: findings from a systematic review and a longitudinal case study, Int. J. Prod. Econ. 165 (2015) 234–246

[82] P. Russom, Managing big data, TDWI Best Practices Report, TDWI Research, 2013, pp. 1–40.

[83] R. Dubey, A. Gunasekaran, S.J. Childe, S.F. Wamba, T. Papadopoulos, The impact of big data on world-class sustainable manufacturing, Int. J. Adv. Manuf. Technol. 84 (1–4) (2016) 631–645.

[84] U. Sivarajah, M.M. Kamal, Z. Irani, V. Weerakkody, Critical analysis of big data challenges and analytical methods, J. Bus. Res. 70 (2017) 263–286.

[85] S. Parise, B. Iyer, D. Vesset, Four strategies to capture and create value from big data, Ivey Bus. J. 76 (4) (2012) 1–5.

[86] L.L. Segarra, et al., A framework for boosting revenue incorporating big data, J. Innoy, Manage, 4 (1) (2016) 39–68.

[87] B.H. Wixom, H.J. Watson, An empirical investigation of the factors afecting data warehousing success, MIS Q. (2001) 17–41.

[88] S. Bischoff, S. Aier, M.K. Haki, R. Winter, Understanding continuous use of business intelligence systems: a mixed methods investigation, J. Inform. Technol. Theory Appl. 16 (2) (2015) 5–37.

[89] A. Popovič, R. Hackney, R. Tassabehji, M. Castelli, The impact of big data analytics on firms’ high value business performance, Inform. Syst. Front. 20 (2) (2018) 209–222.

[90] B. Dorr, et al., The NIST IAD data science research program, Proceedings of the International Conference on Data Science and Advanced Analytics (DSAA). JEEE 2015, pp. 1–10.

[91] S. Zillner, H. Oberkampf, C. Bretschneider, A. Zaveri, W. Faix, S. Neururer, Towards a technology roadmap for big data applications in the healthcare domain, 2014 IEEE International Conference on Information Reuse and Integration (IRI), JEEE, 2014. pp. 291–296.

[92] M.-K. Kim, J.-H. Park, Identifying and prioritizing critical factors for promoting the implementation and usage of big data in healthcare. Inform. Dey. 33 (3) (2017) 257–269.

[93] M. Mawed, A. Al-Hajj, Using big data to improve the performance management: a case study from the UAE FM industry. Facilities 35 (13–14) (2017) 746–765.

[94] P. Colombo, E. Ferrari, Privacy aware access control for big data: a research roadmap. Big Data Res, 2 (4) (2015) 145–154.

[95] F. Fogelman-Soulié, W. Lu, Implementing big data analytics projects in business, Big Data Analysis: New Algorithms for a New Society, Springer, 2016, pp. 141-158.

[96] M. Ahmadi, P. Dileepan, K.K. Wheatley, A SWOT analysis of big data, J. Educ. Bus. (2016) 1–6.

[97] EY, Ernst, Young (Eds.), Big Data: Changing the Way Business Compete and Operate, 2014.

[98] A. Abbasi, S. Sarker, R.H. Chiang, Big data research in information systems: toward an inclusive research agenda, J. Assoc. Inform. Syst. 17 (2) (2016) 1–32.

[99] P. Brous, M. Janssen, D. Schraven, J. Spiegeler, B.C. Duzgun, Factors influencing adoption of IoT for data-driven decision making in asset management organizations, 2nd International Conference on Internet of Things, Big Data and Security (2017) 90–97.

[100] M. Comuzzi, A. Patel, How organisations leverage big data: a maturity model, Ind. Manage. Dat Syst. 116 (8) (2016) 1468–1492.

[101] J.M. Juran, Basic concepts, Quality Control Handb. (1974) 2.

[102] M. Janssen, H. van der Voort, A. Wahyudi, Factors influencing big data decision making quality, J. Bus, Res, 70 (2017) 338–345

[103], S.R. Sukumar. R. Natarajan. R.K. Ferrell. Ouality of big data in health care, Int, J Health Care Oual, Assur, 28 (6) (2015) 621–634.

[104] E. Al Nuaimi, H. Al Neyadi, N. Mohamed, J. Al-Jaroodi, Applications of big data to smart cities. J. Internet Sery. Appl. 6 (1) (2015) 1–15

[105] O. Kwon, N. Lee, B. Shin, Data quality management, data usage experience and acquisition intention of big data analytics, Int. J. Inform. Manage. 34 (3) (2014) 387-394.

[106] D. Loshin, Understanding Big Data Quality for Maximum Information Usability, White Paper, SASA Institute Inc., 2014.

[107] R. Clarke, Big data, big risks, Inform. Syst. J. 26 (1) (2016) 77–90.

[108] J. Gao, C. Xie, C. Tao, big data validation and quality assurance – issues, chal lenges, and needs, IEEE Symposium on Service-Oriented System Engineering (SOSE) (2016) 433–441.

[109] E. Graupner, M. Berner, A. Maedche, H. Jegadeesan, Business intelligence and analytics for processes – a visibility requirements evaluation, MKWI 2014 (2014) 26–38.

[110] A. Barua, P. Konana, A.B. Whinston, F. Yin, An empirical investigation of net enabled business value, MIS Q. 28 (4) (2004) 585–620.

[111] J.G. Mooney, V. Gurbaxani, K.L. Kraemer, A process oriented framework for as sessing the business value of information technology, ACM SIGMIS Database: DATABASE Adv. Inform. Syst. 27 (2) (1996) 68–81.

[112] L. Kung, H.-J. Kung, A. Jones-Farmer, Y. Wang, Managing big data for firm performance: a configurational approach, Twenty-first Americas Conference on Information Systems, Puerto Rico, 2015, pp. 1–9.

[113] O. Ylijoki, J. Porras, Conceptualizing big data: analysis of case studies, Intell. Syst. Account. Finan. Manage, 23 (4) (2016) 295–310.

[114] A. Ahmad, R. Ahmad, K.F. Hashim, Innovation traits for business intelligence succesful deployment, J. Theor. Appl. Inform. Technol. 89 (1) (2016) 96–107.

[115] S. Verma, The adoption of big data services by manufacturing firms: an empirical investigation in India, J. Inform. Syst. Technol. Manage. 14 (1) (2017) 39–68.

[116] D.Q. Chen, D.S. Preston, M. Swink, How the use of big data analytics afects value creation in supply chain management, JMIS 32 (4) (2015) 4–39.

[117] S. Seol, H. Lee, H. Zo, Exploring factors afecting the adoption of mobile ofice in business: an integration of TPB with perceived value. Int. J. Mobile Commun. 14 (1) (2016) 1–25.

[118] M.S. Featherman, P.A. Paylou, Predicting e-services adoption: a perceived risk facets perspective, Int. J. Hum.-Comput. Stud. 59 (4) (2003) 451–474.

[119] K.W.K. Soon, C.A. Lee, P. Boursier, A Study of the determinants afecting adoption of big data using integrated technology acceptance model (TAM) and difusion of innovation (DOI) in Malaysia, IJABER 14 (2016) 17–47.

[120] J. Coleman, Competition and cooperation, Ethics 98 (1) (1987) 76–90.

[121] C.K. Prahalad, V. Ramaswamy, Co-creation experiences: the next practice in value creation, J. Interactive Market. 18 (3) (2004) 5–14.

[122] E.B.-N. Sanders, P.J. Stappers, Co-creation and the new landscapes of design, Codesign 4 (1) (2008) 5–18.

[123] H.U. Buhl, M. Röglinger, F. Moser, J. Heidemann, Big data, Bus. Inform. Syst. Eng. 5 (2) (2013) 65–69.

[124] M. Halaweh, A.E. Massry, Conceptual model for successful implementation of big data in organizations. J. Int. Technol. Inform. Manage, 24 (2) (2015) 20–34

[125] E.D. Davis. Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Q. (1989) 319–340.

[126] K.R. Larsen, A taxonomy of antecedents of information systems success: variable analysis studies, JMIS 20 (2) (2003) 169–246.

[127] B. Shin, An exploratory investigation of system success factors in data warehousing, J. Assoc. Inform. Syst. 4 (1) (2003) 141–170.

[128] B.M. Félix, E. Tavares, N.W.F. Cavalcante, Critical success factors for big dat adoption in the virtual retail: magazine Luiza case study, Rev. Bras. Gest. Negócios 20 (1) (2018) 112–126.

[129] M.-C. Boudreau, D. Gefen, D.W. Straub, Validation in information systems re search: a state-of-the-art assessment, MIS Q. (2001) 1–16.

[130] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological founda tions, CACM 39 (11) (1996) 86–95.

[131] Y. Wang, L. Kung, C. Ting, T.A. Byrd. Bevond a technical perspective: understanding big data capabilities in health care. 2015 48th Hawaji Internationa Conference on System Sciences (HICSS). JEEE. 2015, pp. 3044–3053

[132] N.R. Sanders, How to use big data to drive your supply chain, Calif. Manage. Rev. 58 (3) (2016) 26–48.

[133] B. Farah, A value based big data maturity model, J. Manage. Policy Pract. 18 (1) (2017).11–18

[134] M. Halaweh, A. El Massry, A synergetic model for implementing big data in organizations: an empirical study, Inform. Resour. Manage. J. 30 (1) (2017) 48–64.

[135] B. Klievink, B.-J. Romjin, S. Cunningham, H. de Brujin, Big data in the public sector: uncertainties and readiness, Inform, Syst. Front. 19 (2) (2017) 267–283

[136] I.O. Pappas, P. Mikalef, M.N. Giannakos, J. Krogstie, G. Lekakos, Big data and business analytics ecosystems: paving the way towards digital transformation and sustainable societies, Inform. Syst. e-Bus. Manage. August (2018).

Feliks Prasepta Sejahtera is full-time lecturer and researcher at Atma Java Catholic University of Indonesia, a private university in Jakarta. He is the holder of a PhD scholarship from the Indonesian Government (LPDP) and is currently a PhD student at the School of Information Technology and Electrical Engineering, the University of Queensland.

Wei Wang is post-doctoral fellow at UQ Business School at the University of Queensland. His research interests include business process management, business process modeling, and business rule modeling. Specifically, his main contributions have been in the area of business rule representation, as well as methodological contributions to process model quality studies.

Marta Indulska is professor and leader of the Business Information Systems discipline at the UQ Business School, the University of Queensland. She has published more than 100 fully refereed articles in internationally recognized journals and conferences and has contributed several chapters to published books. Her research has been funded through several competitive grants, including ARC Discovery. Marta has also worked with several organizations in the retail, consulting, and nonprofit sectors to provide guidance on a

variety information technology topics.

Shazia Sadiq is professor at the School of Information Technology and Electrical Engineering, the University of Queensland. Her main research interests include innovative solutions for Business Information Systems that span several areas includin business process management, governance, risk and compliance, and information quality and use. She has published more than 100 peer-reviewed publications in high-ranking journals such as Information Systems Journal, VLDBJ, TKDE, as well as major conferences, such as SIGMOD, ICDE, ER, BPM, ICIS, and CAiSE. She has attracted in excess of \$3.5 million from the Australian Research Council and Industry in the past 10 years.
