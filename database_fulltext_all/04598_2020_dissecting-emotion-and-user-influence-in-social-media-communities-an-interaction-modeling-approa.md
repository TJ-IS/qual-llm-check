---
otero_id: 4598
otero_key: "WCVC793J"
title: "Dissecting emotion and user influence in social media communities: An interaction modeling approach"
authors: "Wingyan Chung; Daniel Zeng"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2018.09.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Dissecting Emotion and User Influence in Social Media Communities: An Interaction Modeling Approach

Authors: Wingyan Chung, Daniel Zeng

![](/api/attachments/WCVC793J/fulltext/images/82d4684cbec8472bb405c1ef5c1d4907e9ab1994b5dda178fa6bd8da64cfb4b8.jpg)

PII: S0378-7206(17)30922-9

DOI: https://doi.org/10.1016/j.im.2018.09.008

Reference: INFMAN 3108

To appear in: INFMAN

Received date: 16-10-2017

Revised date: 5-9-2018

Accepted date: 9-9-2018

Please cite this article as: Chung W, Zeng D, Dissecting Emotion and User Influence in Social Media Communities: An Interaction Modeling Approach, Information and amp; Management (2018), https://doi.org/10.1016/j.im.2018.09.008

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Dissecting Emotion and User Influence in Social Media Communities: An Interaction Modeling Approach

Wingyan Chung <sup>1</sup> and Daniel Zeng <sup>2,</sup> <sup>3</sup>

<sup>1</sup> Institute for Simulation and Training, University of Central Florida

Address: 3100 Technology Parkway, Orlando, Florida, 32826, U.S.A.

Email: wchung@ucf.edu; Tel.: +1 (407) 882 1300; Fax: +1 (407) 882 1335.

<sup>2</sup> Department of Management Information Systems, Eller College of Management,

The University of Arizona.

Address: 1130 E. Helen St., Tucson, AZ 85721, U.S.A.

Email: zeng@email.arizona.edu; Tel.: +1 (520) 621-4614; Fax: +1 (520) 621-2433.

<sup>3</sup> State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China.

## Abstract

Human emotion expressed in social media plays an increasingly important role in shaping policies and decisions. However, the process by which emotion produces influence in online social media networks is relatively unknown. Previous works focus largely on sentiment classification and polarity identification but do not adequately consider the way emotion affects user influence. This research developed a novel framework, a theory-based model, and a proofof-concept system for dissecting emotion and user influence in social media networks. The system models emotion-triggered influence and facilitates analysis of emotion-influence

#

causality in the context of U.S. border security (using 5,327,813 tweets posted by 1,303,477 users). Motivated by a theory of emotion spread, the model was integrated in an influencecomputation method, called the interaction modeling (IM) approach, which was compared with a benchmark using a user centrality (UC) approach based on social positions. IM was found to have identified influential users who are more broadly related to U.S. cultural issues. Influential users tended to express intense emotions of fear, anger, disgust, and sadness. The emotion trust distinguishes influential users from others, whereas anger and fear contributed significantly to causing user influence. The research contributes to incorporating human emotion into the datainformation-knowledge-wisdom model of knowledge management and to providing new information systems artifacts and new causality findings for emotion-influence analysis.

Keywords: emotion; network analysis; sentiment analysis; social media analytics; emotion extraction; influence modeling; causal modeling; social computing; border security.

## Dissecting Emotion and User Influence in Social Media Communities:

## 1. INTRODUCTION

Understanding emotional drivers often bears strategic importance in business decision and public policy development (Straker et al. 2016). Social media, a growing online platform for sharing opinions and ideas, provides many opportunities for decision makers to understand public emotion (Tettegah 2016). On the basis of emotion expressed in social media discussions, policy makers may understand public concerns about security issues (Choudhury et al. 2014); marketers may create sales agendas to promote products and services (Laurenson 2017; Pappas et al. 2017); and cybersecurity experts may obtain intelligence about malicious attacks, identity thefts, and other cybercrimes (Tayouri 2016).

#

One important task of leaders and managers is to monitor sentiment and emotion of their constituents to understand their behavior and trends. The task maps into four phases of the famous “data-information-knowledge-wisdom” (DIKW) model (and its variants) (Ackoff 1989; Briggs et al. 2002). Data are raw symbols represented in social media messages; information is created when the data are processed to provide meaning (e.g., a product and customer emotion); knowledge is discovered when the messages are used by people in a certain context (e.g., feedback about a product); wisdom is manifested by actions taken by decision makers using the knowledge in response to emotion expressed in the social media messages (e.g., changing a product feature based on public anger, reinforcing a marketing strategy in response to aggregate joyous emotion).

Related to the task of understanding online behavior, research in emotion has been conducted extensively in the field of psychology (Darwin 1872; Plutchik 1980; Scherer 2005; Scherer et al. 2014) and more recently in artificial intelligence (AI) (Teng et al. 2007; Wiebe et al. 2005) and social media analytics (SMA) (Chung 2016; Chung et al. 2018; Guellil et al. 2015; Rosso et al. 2016). Psychological theories have been developed to explicate emotion types and categories. For example, personalization theory and complexity theory have been studied in personalized online shopping environments (Pappas et al. 2016; Pappas et al. 2017). Research in AI and SMA develops technologies and resources to help automate part of the tasks of emotion recognition and analysis (Fan et al. 2014; Zeng et al. 2010). The growing volume, velocity, and variety of social media have allowed unprecedented expression of human emotion on a large scale. However, existing approaches on examining emotion do not sufficiently incorporate knowledge about psychological processes and do not study all components and levels of the phenomenon of emotion using modern methodology and recent techniques (see (Scherer et al.

2014), p. 315). In particular, how to gauge the changing emotion of the constituents of an online community over time challenges both researchers and decision makers. Furthermore, existing research uses questionnaires and Likert scales to capture emotion from respondents in an experimental setting. The number of participants and the information collected both limit the analysis of emotion (e.g., (Pappas et al. 2016; Pappas et al. 2017) tested their models using input from 723 respondents in the e-commerce market of one country). How emotion expressed in a large social media community (that may span different geographic locations and long time periods) should be modeled and analyzed to reveal their influence presents new challenges to researchers and managers.

The aforementioned challenges call for a unique type of emotion analytics in which the internal states of humans are extracted and analyzed from written messages (or other media) to provide answers for intelligence analysis. For example, by analyzing the content and linkage information in social media, decision makers and leaders could possibly obtain useful answers to questions such as, Who are the most influential leaders in the social media community? How are different types of emotion changing over time as new events emerge? How does users’ emotion change the emotion of other users in the community? What are the network relationships among participants of social media discussion?

Existing research in social media analytics and text mining represents media content as streams of textual entities, numerical indices, and relationship linkages (Rosso et al. 2016). Typical analysis tasks include sentiment classification, topic modeling, and network analysis. Despite prior research in human cognitive processes (Norman 1995), human emotion in social computing environment has not been studied widely. There is a lack of understanding of the

hidden network of interpersonal motivations that influence collective decision-making in social media community (Cebrian et al. 2016).

This paper describes a novel framework for emotion analytics using social media content The research developed a novel framework, a theory-based model, and an automated system to extract emotion expressed in social media and analyze user influence. Intelligence in the form of user emotion, posting behavior, relationship between users, and temporal trends is extracted from social media content. The system analyzes text and linkages in social media posts to determine the intensity of emotion types and user relationships. A 4-year-long collection of social media posts was used to track temporal changes of user behavior and message content. The collection contains more than 5,327,813 messages posted by more than 1,303,477 users who expressed opinions and discussed issues on U.S. border security. The raw data were processed to reveal intensity of different types of emotion expressed in the social media posts. Motivated by a theory of emotion spread, a dynamic influence model was developed and integrated in an influencecomputation method, called the interaction modeling (IM) approach, which was compared with a benchmark using a user centrality (UC) approach based on social positions. The two approaches were implemented in an automated system, whose effectiveness was evaluated in identifying influential users, attributing user influence with intensity of emotion, identifying causality between emotion and user influence, and supporting visualization of user networks. Findings of the study indicate a strong applicability of the framework to analyzing emotion and influence in large social media communities.

This research should make three contributions. First, it enriches the DIKW model by connecting academic literature of several fields: MIS, AI, psychology, and human information

#

processing. The enriched model should help to guide systems design, development, and evaluation by incorporating human emotion into the components of the model. Second, the research develops new information systems (IS) artifacts on characterizing temporal changes of emotion in a large community of online users. The framework, the system developed based on it, and its relevant methods implement the enriched DIKW model in the context of SMA. The new developments should expand the capability of modeling and analyzing emotion to test existing theories and to build new theories. Third, new empirical findings of examining different types of emotion and user influence should shed light on aggregate behavior of the respective online communities. The results have implications for domains where understanding the emotion of constituents is important for decision-making. Examples of these domains are public policy informatics, human-centric cybersecurity, e-commerce, and health informatics. Businesses may benefit from better understanding of consumers and their temporal behavior.

The rest of the paper is structured as follows. Section 2 surveys existing works in social computing, emotion and sentiment analyses, and studying influence in social media. Section 3 presents a framework for dissecting emotion in social media and describes its components. Section 4 reports the results of an empirical study and discusses implications. Section 5 concludes the paper and discusses future directions.

## 2. LITERATURE REVIEW

The analysis of emotion in social media relates to social computing, SMA, and human information processing. This literature review used two different databases to search for relevant articles: Compendex/INSPEC and PsycINFO. By querying the terms “social media” and “emotion” in the abstracts and “Social media” in the keyword field, with a time span from 2011

#

to 2016, the search returned 632 results and 56 results, respectively, from Compendex/INSPEC and PsycINFO. The Compendex/INSPEC results were further narrowed down to 116 items by adding the term “influence,” which reduced the large volume of results. In addition, the related terms “sentiment analysis,” “expert identification,” “computational rhetoric,” “digital rhetoric” were searched on Google Scholar (http://scholar.google.com/) to provide a more comprehensive coverage. The retrieved articles address how emotion is expressed in an online environment, how the expression of emotion online affects decision-making, how influence is characterized in these expressions, and what relevant technologies are available.

## 2.1 Social Computing and Human Information Processing

Social computing has become a central theme across various information and communication technology (ICT) fields (Wang et al. 2007), drawing attention not only from technologists and researchers but also from political analysts, business strategists, and government agencies, among others. Putting power in individuals and communities mediated by social software (Schuler 1994), social computing facilitates social studies and human social dynamics and is concerned with the intersection of social behavior and computational systems (Wang et al. 2007; Wikipedia 2016). Human activities and emotion have been characterized using various models to design and develop ICT in social context.

Human information processing has been studied for more than three decades, spanning the areas of information seeking, business, and, more recently, military intelligence analysis (Norman 1995; Olson et al. 1990). Human cognitive processes include personal cognitive style; emotion; social interaction effects; and non-conscious aspects of attitudes, interests, and opinions. Prior research has examined these factors in the context of consumption (Han et al. 2007; Petty et al. 1986; Sherry 1991) and investing (Aspara et al. 2011; Cheng 2010; Statman et al. 2008) and offers insights into what motivates certain human decisions and what the appeals presented by these factors are. Another stream of research relates to processing rhetoric arguments. Computational rhetoric examines the algorithmic processes involved in argumentation and discourse processing, thus creating and interpreting arguments and modeling 2013). The main task is to pass some judgmental value (e.g., good or bad) from one object (e.g., a certain political stance) of a discourse to another (e.g., a politician who holds that stance). Digital rhetoric, a closely related area to computational rhetoric, has also been studied by humanity researchers and helps to explain how traditional rhetorical strategies of persuasion function and how they are configured in digital spaces (Zappen 2005). Despite these prior studies, human emotion in social computing environments has been studied only in recent years. The field of SMA represents some of the efforts to apply ICT to understanding human emotion.

## 2.2 Application of Social Media Analytics to Understanding Emotion

Social media analytics (SMA) is a rich set of tools and technologies applied to security informatics (Benjamin et al. 2014; Zeng et al. 2010). Traditional domains in which SMA is used include business intelligence, online product review analysis, and security informatics (Chen et al. 2012; Chung 2014; Chung et al. 2012). Applications of SMA to understanding emotion have been increasing in recent years. Among these applications, sentiment analysis and emotion extraction are important tools for understanding large amounts of social media data.

## 2.2.1 Sentiment Analysis

A “sentiment” is a positive or a negative view, attitude, emotion, or appraisal about an entity or an aspect of the entity from an opinion holder ((Liu 2011), p.,463). Emotions are human subjective feelings and thoughts ((Liu 2011), p.466) and have been studied in psychology,

##

philosophy, and sociology (Darwin 1872; Plutchik 1980; Scherer 2005; Scherer 2009; Stieglitz et al. 2013; Tettegah 2016). Sentiment analysis is the task of finding the opinions of authors about specific entities such as products and services (Feldman 2013). Some of the seminal publications in sentiment analysis are (Liu 2011; Liu 2015; Pang et al. 2008). Lexicon-based sentiment analysis has shown promise in recent research (Nielsen 2011). For instance, researchers have developed a specialized lexicon to support sentiment classification (Mohammad et al. 2013). The lexicon contains more than 13,000 entries of term-category, in which a term may belong to one or more of the eight emotion categories (anger, anticipation, disgust, fear, joy, sadness, surprise, and trust) (Plutchik 1980). Using the Harvard IV-4, SentiWordNet 3.0, and SenticNet 3.0 dictionaries, Xie et al. incorporated sentiment information into user-generated tags to assist in personalized search in social media (Xie et al. 2016). Their framework considers user attributes, resources (social media content), and search queries and maps user-generated tags to sentiment spaces, which consist of emotion categories specified in the selected dictionaries. Based on the six Ekman emotion categories, Mohammad and Kiritchenko created a corpus of emotion-labeled tweets using tweet hashtags and used the corpus to classify emotion and personality types automatically from Facebook posts (Mohammad et al. 2015). These linguistic resources have also been used in sentiment polarity determination. For example, Saif et al. developed a lexiconbased approach for capturing contextual semantic of words and for classifying sentiment polarity of tweets and high-level entities (Saif et al. 2016). Fersini et al. examines the use of adjectives and expressive signals to classify tweet sentiment and found only adjectives to play a key role in the classification (Fersini et al. 2016). A systematic review of social media research on public health reveals diverse applications to the study of Ebola outbreak (Fung et al. 2016). Many of

these studies used keyword counting and manual categorization to find user emotions and sentiment.

## 2.2.2 Emotion Extraction

Development of sentiment analysis necessitates the formalization of emotion representation in digital media. Emotion extraction is an important task to automate deeper understanding of text than simple keyword matching. Affective models that encompass the expressive aims of social media are useful in guiding the development of intelligent technologies to understand human emotions (Rosso et al. 2016). The World Wide Web Consortium (W3C) created the Emotion Markup Language (EmotionML) to specify human emotion for use in manual annotation and automatic recognition of emotion-related states (Baggia et al. 2014). It extends the WordNet-Affect, which assigns affective labels to English words (Strapparava et al. 2004). Onyx, a semantic vocabulary of emotions developed using linked open data, extends from EmotionML and WordNet-Affect by supporting additional features such as database querying and annotation (Sánchez-Rada et al. 2016).

Some of these linguistic resources are used to support SMA. For instance, Rangel and Rosso developed EmoGraph for modeling emotion in Spanish text using graph-based features (Rangel et al. 2016). Volkova and Bachrach developed machine learning models to classify emotion from tweets and correlated between user socio-demographic traits (e.g., income, age, gender, education, and family status) and the number of tweets they posted (Volkova et al. 2015). They also used emotion and opinion distribution to classify user demographics, finding some stereotypical results (e.g., female users are more emotional and opinionated than male users). Scharl et al. developed an intelligent web portal that aggregates news and social media coverage on a TV program (Scharl et al. 2016). The portal provides an interactive dashboard with trend charts and visual analytics and computes positive and negative sentiments on actors and plot elements. Celli et al. correlated personality types and communication styles of Twitter users with the mood of the news articles they shared (Celli et al. 2016). They performed automatic classification using as features the best predictors of positive and negative moods. The work also highlights the importance of studying influence in social media networks.

## 2.3 Studying Influence in Social Media

In recent years, online social networks have facilitated diffusion of social influence at a massive scale (Bond et al. 2012). Traditionally, social network analysis examines network dynamics and actor influence on a small scale (Wasserman et al. 1994). Advances in information technologies enable new capabilities of network analysis, such as identifying opinion leaders in discussion forums (Song et al. 2007), finding expertise in networks (Wang et al. 2013; Zhang et al. 2007), analyzing business stakeholder networks (Chung et al. 2009), and visualizing networked relationships of businesses (Chung et al. 2005) and infectious disease transmission (Zeng et al. 2011).

The proliferation of social media has made them a hub of information generation and diffusion. One important problem is to characterize and identify influentials, which can be defined as users who change the opinions or emotions of others in a large scale. Previous work quantifies user influence based on various structural measures, such as in/out-degree, betweenness, PageRank, and diffusion (Banerjee et al. 2013; Jackson 2008). The idea is based on social linkages developed in human interaction that facilitate spread of emotion. These linkages play a critical role in large communities by facilitating exchange of information and confirmation of authoritative and influential positions. However, they have not been examined widely in social media communities.

Recent works also attempt to model the spread of human behavior in social networks (Bond et al. 2012; Kane et al. 2014; Liang et al. 2015; Schreck et al. 2013). Emotion entrainment, which accounts for the synchronous convergence of human emotions, has been examined in neuroscience (Bastiaansen et al. 2011) and human social networks (Kramer et al. decision-making is relatively unknown. Examples include public policy decisions and infectious disease control scenarios, among others. Although previous methods provide quantitative analysis for social interactions, they often require explicit causal knowledge that is scarce in most scenarios.

## 2.4 Summary

In summary, previous works focus largely on the classification of emotion types or sentiment polarity identification but rarely examine both emotion and actor influence (see Table 1). There is a lack of consideration of how emotion affects user influence in a social media community. Furthermore, the hidden network of interpersonal motivations that influence collective decision-making in a social media community is not widely explored (Cebrian et al. 2016).

This research attempted to dissect emotion types in a longitudinal manner to support analysis of emotion on a temporal scale. To our knowledge, this work is the first to examine the relationship between emotion types and user influence and to examine the process by which different emotion types shape user influence in social media.

Table 1. Summary of Literature on Studying Emotion and Influence in Social Media

<table><tr><td></td><td></td><td>Targets of Study</td></tr></table>

##

<table><tr><td>Study (in chronological order of publication)</td><td>Major Topics</td><td>Sentiment Polarity</td><td>Emotion Category</td><td>Actor Influence</td></tr><tr><td>Strapparava &amp; Valitutti (Strapparava et al. 2004)</td><td>Extending WordNet to incorporate lexical representation of affective knowledge</td><td></td><td>√</td><td></td></tr><tr><td>Wiebe et al. (Wiebe et al. 2005)</td><td>Building a lexicon for emotion and sentiment identification</td><td>√</td><td>√</td><td></td></tr><tr><td>Teng et al. (Teng et al. 2007)</td><td>Classifying emotion types using Rough-Set theory and Support Vector Machines</td><td></td><td>√</td><td></td></tr><tr><td>Song et al. (Song et al. 2007)</td><td>Identifying opinion leaders using an influence rank score computed by novel contribution to network</td><td></td><td></td><td>√</td></tr><tr><td>Zhang et al. (Zhang et al. 2007)</td><td>Identifying experts by building simulation rules that govern user interactions and replicated structural characteristics</td><td></td><td></td><td>√</td></tr><tr><td>Bond et al. (Bond et al. 2012)</td><td>Testing randomized trial of political mobilization messages to examine online peer influence</td><td></td><td></td><td>√</td></tr><tr><td>Mohammad &amp; Turney (Mohammad et al. 2013)</td><td>Developing a word-emotion association lexicon</td><td>√</td><td>√</td><td></td></tr><tr><td>Baggia et al. (Baggia et al. 2014)</td><td>Developing an emotion markup language (similar to XML)</td><td>√</td><td>√</td><td></td></tr><tr><td>Mohammad &amp; Kiritchenko (Mohammad et al. 2015)</td><td>Detecting emotion categories using hashtags</td><td>√</td><td>√</td><td></td></tr><tr><td>Xie et al. (Xie et al. 2016)</td><td>Collaborative tagging of user profiles for personalized search</td><td>√</td><td>√</td><td></td></tr><tr><td>Saif et al. (Saif et al. 2016)</td><td>Sentiment polarity classification using a lexicon-based approach</td><td>√</td><td></td><td></td></tr><tr><td>Fersini et al. (Fersini et al. 2016)</td><td>Polarity detection using natural language, emoticon, and expressive lengthening</td><td>√</td><td></td><td></td></tr><tr><td>Liang et al. (Liang et al. 2015)</td><td>Characterizing online social influence using social network analysis and information theoretic approaches</td><td></td><td></td><td>√</td></tr><tr><td>Sánchez-Rada &amp; Iglesias (Sánchez-Rada et al. 2016)</td><td>Developing a common vocabulary to represent emotion</td><td></td><td>√</td><td></td></tr><tr><td>Celli et al. (Celli et al. 2016)</td><td>Predicting sentiment polarity using personality, communication style, and Twitter metadata</td><td>√</td><td></td><td>√</td></tr></table>

## 3. A FRAMEWORK FOR DISSECTING EMOTION IN SOCIAL MEDIA

This section describes a framework for dissecting emotion in social media. A model was built and tested using a theory of human emotion-spreading to understand the way emotion affects user influence. The components and the design rationale are described in the following sections.

## 3.1 Framework Components

As shown in Figure 1, the framework consists of various steps of data collection, cleaning, filtering, and analysis. Input sources for the framework include social media data, a specialized lexicon for emotion extraction and sentiment analysis, an algorithm to compute emotion indices, and program modules for performing network analysis and visualization.

![](/api/attachments/WCVC793J/fulltext/images/35dad068ca6f342349736ab05e81ef67f74105d9dfa2a5dba541b30033be49f7.jpg)  
Figure 1. A framework for dissecting emotion in social media

## 3.2 System Development

Based on the framework, we developed the BOrder Security Social Emotion Tracker (BOSSET), an IS that extracts emotion from tweets related to U.S. border security and models user influence based on user positions in network and on behavioral impact on the community. BOSSET implements the steps of the framework in the context of border security discussion on Twitter.com, a major social media website where users post short messages called “tweets” on issues they are interested in. Each tweet consists of no more than 140 alphanumeric characters. The BOSSET system and its emotion extraction and strength computation were developed based on design science research guidelines (Hevner et al. 2004), which include producing a design as an artifact, solving important and relevant business/social problems, demonstrating utility and quality through evaluation, contributing to SMA, and presenting the research to both technologyoriented and management-oriented audiences. Design was treated as a search process to discover an effective solution to our problem and tested alternatives against the requirements and constraints.

#

## 3.3 Data Collection and Processing

The system collected the tweets related to the U.S. border security discussion. We constructed carefully a list of queries by reviewing recent literature published on the topic (Bush et al. 2009; Gans et al. 2012; LeMay 2004; U.S. Commission on Immigration Reform 1994). Filtering and collection testing helped to reduce the original 14 queries to eight domain-specific “immigration debate,” “immigration policy,” “immigration reform,” “US border security,” and “US immigration.” We developed a tweet crawler that collects tweet postings automatically between May 2013 and June 2017. As of June 28, 2017, the dataset consists of 5,327,813 tweets posted by 1,303,477 unique users. In this study, we focused on the executive actions announced by President Obama in November 2014 to grant legal status to millions of undocumented immigrants (Dwyer 2014; Meckler et al. 2014). We selected a subset of the data consisting of 189,012 tweets posted by 105,304 users between November 1 and November 30 of 2014. That month also set the records for the highest numbers of tweets and user activities ever observed during the entire timespan of the data collection. From the users whose tweets were collected in November 2014, we randomly selected a sample of 5,000 users for further examination of the emotion extracted from the tweets and of emotion entrainment.

## 3.4 Emotion Extraction

To extract emotion from each tweet, we computed values of indices in eight emotional categories defined in (Plutchik 1980) (anger, disgust, fear, sadness, surprise, anticipation, joy, and trust). Each index represents the emotional intensity of a tweet. We used the emotion lexicon developed in (Mohammad et al. 2013) to identify emotional words that appear in the tweets. The lexicon contains 13,901 word-emotion entries tagged by more than 2,216 human users who completed a total of 38,726 tagging assignments. Each word was assigned a sentiment polarity (positive (+1) or negative (-1)) and is categorized into one (or more) of the eight emotional categories. Equation (1) shows the computation of the score of emotion j (ranging from 1 to 8) of tweet i, which contains $n _ { i }$ words. Equation (2) shows the computation of sentiment score of tweet i.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$M_{ij} = \frac{\sum\limits_{k=1}^{n_i}W_{ik}}{n_i}\qquad \forall i\in\{1\ldots N\},\forall j\in\{1\ldots M\}$ …(1)

$S_i = \frac{\sum\limits_{k=1}^{n_i}V_{ik}}{n_i}\qquad \forall i\in\{1\ldots N\}$ …(2)

where

$M_{ij} = \text{Score of emotion } j \text{ of Tweet } i$ $S_i = \text{Sentiment score of Tweet } i$ $n_i = \text{Number of words in Tweet } i$ $M = \text{Number of different emotion categories}$ $N = \text{Total number of tweets being considered}$ $W_{ik} = \left\{ \begin{array}{ll}1 &amp; \text{if word}(k)\text{ of Tweet } i \text{ is in category } j,\text{ where } k\in\{1\ldots n_i\}\\ 0 &amp; \text{otherwise} \end{array} \right.$ $V_{ik} = \left\{ \begin{array}{ll}1 &amp; \text{if sentiment of word}(k)\text{ of Tweet } i \text{ is positive}\\ -1 &amp; \text{if sentiment of word}(k)\text{ of Tweet } i \text{ is negative}\\ 0 &amp; \text{otherwise} \end{array} \right.$
</div>

Because the lexicon and algorithm were not tested on our data collection, there was a potential problem that the emotions expressed in the data may not be correctly captured. In addition, implicit emotions (e.g., sarcasm) not expressed in lexicon words may not be obtained correctly. To establish that the eight emotions were correctly inferred by using our algorithm, we invited two independent raters to manually tag the social media messages (tweets) and then computed the reliability measures of the emotion extraction. One rater is male and had earned a master’s degree in computer science from a U.S. public university. The other rater is a female and had earned a master’s degree in educational psychology from another U.S. public university. Each rater was asked to rate 13 to 21 tweets for each of the eight emotions, thereby rating a total of 141 tweets. For each tweet, the rater was asked to indicate whether it contains the specified emotion. Only the date, time, and content of the tweets were presented to the raters. These tweets were selected from all the collected data such that for a given emotion group, the score of the

specific emotion of each tweet is in a range (from 0.3 to 0.95) higher than that of the other seven emotions (ranging from 0 to 0.1). Then, in each group of tweets belonging to one emotion type, we inserted tweets randomly from other emotion groups so that a rater had to judge whether each tweet contained the specified emotion type.

Table 2. Reliability Measures Among Two Independent Raters and the Algorithm

<table><tr><td>Reliability Measure</td><td>Rater A – Rater B</td><td>Rater A – Algorithm</td><td>Rater B – Algorithm</td></tr><tr><td>Inter-rater Agreement</td><td>80.1%</td><td>78.7%</td><td>71.6%</td></tr><tr><td>Cohen’s kappa</td><td>60%</td><td>53.4%</td><td>41.7%</td></tr></table>

Upon getting the ratings, we computed two types of reliability measures: inter-rater agreement ratio and Cohen’s kappa, which were chosen to balance between interpretability and rater guessing (Cohen 1960; McHugh 2012). The results are shown in Error! Reference source not found.. “Algorithm” refers to the tagging obtained by using our algorithm; Rater A and Rater B refer to tagging done by the two independent raters mentioned above. The results indicate moderate to strong levels of agreement (McHugh 2012) in different pairwise combinations of raters and algorithm. According to the results, we believe that the algorithm has an acceptable reliability for correctly categorizing the collected tweets into the eight emotion types.

## 3.5 Dynamic Influence Modeling

Dynamic influence of human emotion is the socialization of feelings among people who interact with each other. Prior research indicates that human emotion can spread dramatically through online social networks (Bond et al. 2012). For example, online shoppers’ positive emotions were found to have a moderating effect on the relationship between persuasion and intention to purchase in an e-commerce environment (Pappas et al. 2017). However, the process of online social influence is not well understood. To examine how this process takes place in a

#

large-scale social media network and how emotion evolves dynamically, we developed an Interaction Modeling (IM) approach to detect causal relationships and to identify influential users on the basis of the theory of emotion entrainment (Clayton et al. 2005). This theory suggests that human emotion rhythmically converges through social interactions.

Based on the theory, we developed a model for representing influence propagation based on dynamics of emotion in a social media community. In the model, we consider users who can highly entrain others as influential. We represent the time series of the emotion scores (Equation (1) described above) of two users x and y with two Markov processes $X = x _ { \mathrm { t } }$ and $Y = { y _ { \mathrm { t } } }$ . Then, the entrainment strength from x to y is given by Equation (3).

$$
E n (\mathrm{X} \rightarrow \mathrm{Y}) = H \left(x _ {t + 1} \mid \mathbf {x} _ {t} ^ {m}\right) - H \left(x _ {t + 1} \mid \mathbf {x} _ {t} ^ {m}, \mathbf {y} _ {t} ^ {n}\right)\tag{... (3}
$$

where, $\mathbf { x } _ { t } ^ { m } = \left( x _ { t } , . . . , x _ { t - m + 1 } \right) , \quad \mathbf { y } _ { t } ^ { n } = \left( y _ { t } , . . . , y _ { t - n + 1 } \right)$ , while m and n are the orders of each of the Markov processes; and $x _ { t } = \sum _ { i = 1 } ^ { 8 } M ( x ) _ { i , t } \atop { \bf { a n d } } ^ { y _ { t } } = \sum _ { i = 1 } ^ { 8 } M ( y ) _ { i , t }$ that represent aggregation of the eight emotions M(.) of a user $( x \mathrm { o r } y )$ at time t. H(\*) calculates the entropy of the probability distribution enclosed. In our experiments, we set the Markov orders $\scriptstyle { m = n = 3 }$ . According to our empirical analysis, this order is adequately high, and a higher order increases computational cost without presenting much quantitative differences. Equation (3) can be estimated based on Simpson’s rule (Kaw et al. 2008) with a computational complexity of $O ( N l o g ( N ) )$ , which we find acceptable for entrainment analysis on large-scale datasets. One limitation of using Equation (3) to infer influence is that it is not possible to eliminate contemporaneous sentiment expressed by two users due to co-incidence but not due to one influencing the other. However, such unrelated coincidence of contemporaneous emotion is balanced out when a large number of users’ sentiment scores are taken into account in the computation. Using Equation (4), we measured the influence of each user x based on how other users entrain toward him.

$$
I (x) = \sum_ {x \neq y} E n (y \rightarrow x)\tag{... (4}
$$

The model is built into our proposed IM approach to examine the dynamics of average emotion on user influence. We compared the IM approach with a User Centrality (UC) approach, which is our selected benchmark approach that uses the betweenness centrality metric to measure connectivity in a social network (Freeman 1977), as calculated in Equation (5).

Betweenness Centrality of User i in Network g

$$
C e _ {i} ^ {B} (g) = \sum_ {k \neq j: i \notin \{k, j \}} \frac {P _ {i} (k j)}{P (k j)}\tag{... (5}
$$

where

g = An undirected, unweighted network of participants represented as an

adjacency matrix

$g _ { i j } = { \left\{ \begin{array} { l l } { 1 } \\ { 0 } \end{array} \right. }$ if node i links with node j otherwise

n = Number of nodes in g

Ni(g) = Neighborhood of node i (set of nodes that i is linked to)

$P _ { i } ( k j )$ = Number of geodesics (shortest paths) between node k and node j

$P ( k j )$ = Total number of geodesics (shortest paths) between node k and node j

Herein, a social network was constructed by identifying links between pairs of users (A and B). A link exists between two users when User A sends a tweet targeted to User B, or User A retweets another tweet written by User B, or User A modifies and then sends out a tweet written by User B. These actions were identified in the tweets’ content directly.

While other measures of centrality are available (Jackson 2008), the betweenness centrality score identifies the extent to which a user serves as a bridge in a highly polarized discussion that relies heavily on the ability to find compromises and common grounds in participants with diverse viewpoints. In other words, network location (an external characteristic)

is the premise of the UC approach in gauging influence. By contrast, the IM approach uses dynamics of emotion (a characteristic internal to users) in evaluating influence.

## 3.6 Causal Modeling and Network Visualization

Two approaches can be used to validate the accuracy of the influence model: causal modeling and network visualization. Network visualization allows quick human evaluation of the relationships between a selected target user and other users connected to this user. The users and their links may be illustrated specifically in the network to indicate relationship types and strengths. Despite the power and aesthetic effect, a visualization approach is limited by human cognitive capacity in handling large volumes of data. Causal modeling, a statistical approach to analyzing relationship, may alleviate the situation and provides scientific evidence of relationship between an influence measure and measures of different emotion types. Granger developed a popular method for determining whether a time series is useful in forecasting another time series (Granger 1969). Subsequent developments defined linear dependence and feedback for multiple time series (Geweke 1982). Sugihara et al. developed a method called convergent cross-mapping (CCM) and applied it to identifying causal networks for policy and management recommendations on ecological systems (Sugihara et al. 2012). The method can distinguish causality from correlation, but its applicability to identifying causality between emotion and user influence in social media community is unknown. To fill the gap, we propose to apply the method to our data and to compare causality of different emotion types in relation to the influence measure.

## 4. EMPIRICAL FINDINGS

In this section, we present empirical findings of using the BOSSET system to examine emotion and influence of Twitter users who posted on U.S. border security issues in November

2014 (see Section 3.3 for details about data collection). The goal of the study is twofold: (1) to validate the proposed framework and its associated methods for emotion analysis in social media and (2) to provide empirical findings of analyzing emotion, sentiment, and influence in the U.S. immigration and border security discussion.

## 4.1 Emotion and Sentiment Scores

We analyzed the changes in emotion and sentiment scores during the 3 months leading to President Obama’s executive action on U.S. immigration policy (from September 2014 to November 2014). This period witnessed one of the highest levels of online activities over the data collection timespan of 2013-2017. In particular, 38,761 messages were collected on November 20, 2014 (Figure 2), the day on which the executive action was announced through a prime-time speech delivered by the President (Figure 3) (Dwyer 2014), and 37,223 messages were collected the next day (November 21, 2014). These numbers are higher than those of most other days.

![](/api/attachments/WCVC793J/fulltext/images/3796f7e5779ed5ad81650c8e24b25c7a783b4857061e948267a0d01a7a143e00.jpg)  
Figure 2. Changes in message count from 9/1/2014 to 11/30/2014

#

Changes in sentiment scores and emotion scores are shown in Figure 4 to Figure 6. The sentiment score remained mostly negative before the announcement of the executive action but turned positive dramatically on approaching and shortly after the announcement (Figure 4). The emotion scores of anger, disgust, fear, and sadness decreased significantly before the markedly, whereas the scores of disgust, fear, and sadness continued to decline below those in September and October 2014. The emotion scores of anticipation, joy, surprise, and trust (Figure 6) also show strong fluctuations during the period, thus indicating a declining trust and soaring surprise after the announcement.

![](/api/attachments/WCVC793J/fulltext/images/511017728139b134ef7584a73aa4f60a4e85dd9aca1e54627507df474fc7def6.jpg)  
Figure 3. President Obama’s announcement of executive action on US immigration policy (Dwyer 2014)

![](/api/attachments/WCVC793J/fulltext/images/d8254fe281bca6a0fec41944ce309244eb1471ededdf987cbe2f2ce0822bb907.jpg)  
Figure 4. Changes in sentiment score from 9/1/2014 to 11/30/2014 (vertical dashed line indicates the date 11/20/2014 when the President announced his executive order)

![](/api/attachments/WCVC793J/fulltext/images/3d27c540c353bc56aa879b8f23cc048ff6d5cdcf85b292084be22f3bd4cec77d.jpg)  
Figure 5. Changes in emotion scores (anger, disgust, fear, and sadness) from 9/1/2014 to 11/30/2014 (vertical dashed line indicates announcement of the President’s executive order)

![](/api/attachments/WCVC793J/fulltext/images/d8359d3e9abe69d88bc2086bd21fcd9f35d107aa8bde0365add62c19cbc55fd3.jpg)  
Figure 6. Changes in emotion scores (anticipation, joy, surprise, and trust) from 9/1/2014 to 11/30/2014 (vertical dashed line indicates announcement of the President’s executive order)

## 4.2 Dynamic Influence Modeling

This section reports findings of comparing top influential users using two approaches (IM and the UC described in Section 3.5) and describes relative strengths of different emotion types.

## 4.2.1 Comparison of Approaches

Our analysis of the socialization of feelings among people shows that a small number of users were able to influence a large number of people in the community, thus producing a significant emotion entrainment effect (“influence” is defined as a change in emotion or opinion as expressed by Equations (1-4)). When compared with the UC approach, the IM approach produces significantly different top-ranked users. Table 3 lists these top 10 most influential users (in the online social network dated 11/30/2014) identified by the two methods. The top users identified by the UC approach are shown on the top part of the table. Several of the listed users are outspoken leaders in U.S. immigration and border security issues, whereas others are journalists or political activists. For example, Daniel John Sobieski identified himself as a freelance writer for various news agencies and expressed strong opinions on the immigration policy proposed by President Obama. FAIR (Federation for American Immigration Reform) is immigration.

Table 3. Top 10 Most Influential Users Identified by Two Methods  
User Centrality Approach

<table><tr><td>User Name</td><td>URL</td><td>UC Score</td><td>Follower Count</td><td>Friend Count</td><td>Retweet Count</td></tr><tr><td>Daniel John Sobieski</td><td>https://twitter.com/gerfingerpoken</td><td>154195466.7</td><td>57081</td><td>26377</td><td>56</td></tr><tr><td>FAIR</td><td>https://twitter.com/FAIRImmigration</td><td>39167930.26</td><td>107474</td><td>1310</td><td>77</td></tr><tr><td>Michael Johns</td><td>https://twitter.com/michaeljohns</td><td>38841336.06</td><td>140065</td><td>92530</td><td>6</td></tr><tr><td>Mickey Kaus</td><td>https://twitter.com/kausmickey</td><td>36675556.34</td><td>36602</td><td>6345</td><td>296</td></tr><tr><td>daveweigel</td><td>https://twitter.com/daveweigel</td><td>25970773.17</td><td>312935</td><td>10050</td><td>21</td></tr><tr><td>Greg Sargent</td><td>https://twitter.com/ThePlumLineGS</td><td>24310903.04</td><td>152439</td><td>3756</td><td>27</td></tr><tr><td>Jeremy W. Peters</td><td>https://twitter.com/jwpetersNYT</td><td>20473270.35</td><td>16555</td><td>502</td><td>1</td></tr><tr><td>Matthew Kolken</td><td>https://twitter.com/mkolken</td><td>19565648.53</td><td>9945</td><td>4603</td><td>359</td></tr><tr><td>Julia Preston</td><td>https://twitter.com/JuliaPrestonNYT</td><td>19552440.3</td><td>8602</td><td>998</td><td>0</td></tr><tr><td>Michael Deacon</td><td>https://twitter.com/MichaelPDeacon</td><td>16906061.8</td><td>15139</td><td>2090</td><td>3</td></tr></table>

Interaction Modeling Approach

<table><tr><td>User Name</td><td>URL</td><td>IM Score</td><td>Follower Count</td><td>Friend Count</td><td>Retweet Count</td></tr><tr><td>ladybug</td><td>https://twitter.com/ellis_texas</td><td>94.55</td><td>1386</td><td>407</td><td>86</td></tr><tr><td>Sheepdog Report</td><td>https://twitter.com/SHEEPDOGREPORT</td><td>91.21</td><td>6627</td><td>6397</td><td>14</td></tr><tr><td>CONEXION</td><td>https://twitter.com/CONEX360</td><td>90.71</td><td>1344</td><td>1163</td><td>0</td></tr><tr><td>Marty Barrack</td><td>https://twitter.com/ahebrewcatholic</td><td>90.49</td><td>3668</td><td>3577</td><td>3</td></tr><tr><td>Stellasasha?</td><td>https://twitter.com/Stellasasha1</td><td>88.97</td><td>17490</td><td>13526</td><td>84</td></tr><tr><td>Les Wenzel</td><td>https://twitter.com/ldubindubc</td><td>88.66</td><td>1375</td><td>1639</td><td>67</td></tr><tr><td>Mike Robbins</td><td>https://twitter.com/MikeRobbinsUSA</td><td>88.03</td><td>2281</td><td>3299</td><td>83</td></tr><tr><td>Ted Skibinski</td><td>https://twitter.com/TedSkibinski</td><td>87.69</td><td>2784</td><td>3110</td><td>86</td></tr><tr><td>Ken</td><td>https://twitter.com/kckshrugged</td><td>86.99</td><td>223</td><td>335</td><td>280</td></tr><tr><td>Dave Ganteaume</td><td>https://twitter.com/DGanteaume</td><td>86.91</td><td>3312</td><td>3704</td><td>35</td></tr></table>

The top users identified by the IM method are shown on the lower part of Table 3. These are generally outspoken individuals who posted many tweets and had many followers. Some of them had significant ties to the Latino and other communities. For example, CONEXION lists itself as related to Latino entrepreneurs, and others affiliated themselves with specific religions. Compared with the users identified by the UC method, these users are less connected to politics and mass media but more broadly related to cultural and religious issues of concern to the U.S. society. These observations were based on messages published on the users’ Twitter accounts.

Additional qualitative analyses (such as interviews and interpretive studies) are needed to examine the user profiles.

## 4.2.2 Distribution of Emotion Ratios

To study quantitatively the strengths of different types of emotion in contributing to the results of the IM approach, we analyzed the distribution of emotion strengths and calculated the emotion ratios. The emotion ratio $R ( e _ { j } ) _ { k }$ for the j th emotion $e _ { j }$ in the k users with the highest influence scores (calculated by the IM method) is computed as

$$
R \left(e _ {j}\right) _ {k} = \frac {\sum_ {i = 1} ^ {k} e _ {i j}}{\sum_ {i = 1} ^ {k} \sum_ {j = 1} ^ {m} e _ {i j}}, \quad j = 1, \dots , m; k = 1, \dots , n\tag{... (6}
$$

where, $e _ { i j }$ is the sum of the j th emotion scores (among m (= 8) categories defined in (Plutchik 1980)) of the tweets written by the i th user (where i ranges from 1 to k). Intuitively, $R ( e _ { j } ) _ { k }$ characterizes the emotion distribution over the top k users. If $R ( e _ { j } )$ varies significantly as k increases (as more less-influential users are involved in the calculation of the ratio), the j th emotion is considered to be a critical factor for distinguishing influential users from other users.

![](/api/attachments/WCVC793J/fulltext/images/eca81c9aa27cbc6934d986da3504553aa9077fd09ae1a8394dc038f1b27719af.jpg)  
Figure 7. Relative strengths of eight emotion types

Figure 7 illustrates the changes in emotion ratios in the selected users ordered by decreasing influence scores. There are several emerging trends. First, influential users are more likely to be those high in emotions related to fear, disgust, anger, and sadness and have relatively lower ratios of trust, joy, anticipation, and surprise than lower rank users. Much of the influence appears to originate from the top 50 users. This observation is in line with the “rich-gets-richer effect” in which leaders who have strong influence tend to entrain dramatically more users’ emotion than others. Second, fear was the most dominant emotion (with the highest ratio) in the posted tweets while surprise was the least dominant emotion (with the lowest ratio). Third, the ratio for trust increases dramatically as users’ ranks change from 1 to n (= 5000). This means the relative amount of trust expressed in social media increasingly distinguishes influential users from less influential users, i.e., expressing less trust in social media is associated with higher user influence in the community. This may be due to the use of more criticism in their messages that decreased trust scores. Fourth, several series (e.g., surprise, trust) in the figure have precipitous fluctuations in emotion ratios for highly ranked users (left side of the figure), thus showing instability in the relative strength of the emotion being considered (compared with other emotions). This may be due to many opposing media that simultaneously influence the community’s diverse emotions. The step-change shown on the right side of several series (around rank 4,800) may also reflect sudden introduction of media content or events (e.g., publication of political scandals, resignation of key figures).

## 4.3 Network Visualization

Visualization of the entrainment network provides further information about the connectivity of top influential users, revealing why (instead of how much) the users attain top influence from the community. In the visualization, we examined the structure of selected users’ entrainment patterns that affect the influence of each user. The influence networks of twitter users named “Daniel John Sobieski,” “SHEEPDOG REPORT,” and “ANNA RAND” are shown in Figure 8 Figure 10, respectively. All nodes are labeled by the names of users who entrain toward the specified user (central node labeled yellow). Blue nodes have above-average entrainment strengths while white nodes have below-average strengths. The arrow on an edge indicates the entrainment direction and the thickness of an edge represents entrainment strength.

We first explored two users who had the highest centrality score (see Table 3). The ratios of users entraining toward these two users with above-average strengths are, respectively, 41.53% and 42.86%. These similarly high ratios suggest that influential users are likely to be entrained by others with a similar degree of entrainment. To test this hypothesis, we further compared the second most influential user “SHEEPDOG REPORT” found by the second method (see Table 3) and the second least influential user “ANNA RAND”

(https://twitter.com/OBAMA\_CZAR) (found by the second method but not listed in Table 3). These two users tweeted similar numbers of messages (46.6K vs. 52.1K), yet had totally different influence in discussing immigration and border security in the community. The ratios of users with above-average entrainment strengths are 57.93% for “SHEEPDOG REPORT” and 32.00% for “ANNA RAND” (note the relatively sparse edges compared with the other networks shown). This result supports our hypothesis that entrainment strengths among influential users are similar to each other. The findings provide strong implications for decision makers to identify influential users or leader groups in a social media community and for users who aspire to become leaders in their communities.

![](/api/attachments/WCVC793J/fulltext/images/4127047fdb4f56927eed3a29b73f0af81882faaff86fd75b604d89fd96859594.jpg)  
Figure 8. Influence Network of “Daniel John Sobieski”

![](/api/attachments/WCVC793J/fulltext/images/9f253363088d21f7e855aee79853c5086cd61869099c3cf34b7b985be6477ccf.jpg)

Figure 9. Influence Network of “SHEEPDOG REPORT”  
![](/api/attachments/WCVC793J/fulltext/images/d5159eb56c78bb4778b90d3d4a837bac189ba6b04b3acbeb70f3eb5bd9e62695.jpg)  
Figure 10. Influence Network of “ANNA RAND”

## 4.4 Causal Modeling

In addition to network visualization, we used CCM (Sugihara et al. 2012) to model the causal relationship between emotion types and user influence computed by the IM approach. CCM is a statistical test for assessing the cause-and-effect relationship between two time series variables that have synergistic effects. In ecology, CCM has been used to show that the apparent

##

correlation between sardine and anchovy in the California current is due to shared climate forcing and not direct interaction (Sugihara et al. 2012). However, the application of CCM in ecology did not examine social influence (e.g., of a pack leader). In our application of CCM, we assume that the users’ social influence and the emotion reflected from their messages belong to the same dynamical system that changes with time. This is because the users mutually influence each other within the same temporal period and context that form the environment of their interaction. Different from previous research on CCM that examined data of physical entities only (McCracken et al. 2014; Sugihara et al. 2012), our research considers temporal occurrence of human influence and emotion in a social media community. We postulate that the large amount of data on human behavior would enable observation of macroscopic behavior in the community. To our knowledge, such observation has not been examined in detail in prior research. In addition, applications of CCM beyond the field of ecology are not widely available (Sugihara et al. 2012).

Data series of each user’s influence score and his/her scores of the eight emotion categories (averaged over all the users’ posted messages) were used to compute the Pearson correlations and the CCM correlations, which are tabulated in Table 4 and Table 5, respectively. In Table 4, the Pearson correlation indicates the extent to which a column variable and a row variable move together, with a range between -1 and +1 and without distinguishing direction of influence (thus filling only half of the table’s cells). A positive value means that the variables move in the same direction, while a negative value indicates movement in opposite directions. The values shown in the table indicate that all the emotion categories correlate positively with each other with different extent of correlation. The absolute magnitude of Pearson correlation indicates the degree to which two variables move to the same extent.

Table 4. Pearson Correlations Between User Influence Score and User Emotion

<table><tr><td></td><td>Anger</td><td>Anticipation</td><td>Disgust</td><td>Fear</td><td>Joy</td><td>Sadness</td><td>Surprise</td><td>Trust</td></tr><tr><td>Inf_Score</td><td>0.03</td><td>0.03</td><td>0.20</td><td>0.06</td><td>0.06</td><td>0.20</td><td>0.02</td><td>0.05</td></tr><tr><td>Anger</td><td></td><td>0.14</td><td>0.29</td><td>0.99**</td><td>0.18</td><td>0.29</td><td>0.97**</td><td>0.17</td></tr><tr><td>Anticipation</td><td></td><td></td><td>0.43</td><td>0.09</td><td>0.89**</td><td>0.50**</td><td>0.09</td><td>0.87**</td></tr><tr><td>Disgust</td><td></td><td></td><td></td><td>0.34</td><td>0.57**</td><td>0.96**</td><td>0.05</td><td>0.50**</td></tr><tr><td>Fear</td><td></td><td></td><td></td><td></td><td>0.13</td><td>0.33</td><td>0.94**</td><td>0.11</td></tr><tr><td>Joy</td><td></td><td></td><td></td><td></td><td></td><td>0.64**</td><td>0.10</td><td>0.88**</td></tr><tr><td>Sadness</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.06</td><td>0.58**</td></tr><tr><td>Surprise</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.09</td></tr></table>

Strong correlations ( 0.5) are shown with \*\*; weak correlations ( 0.3) are shown in light gray.

Table 5. CCM Correlations Between the User Influence Score and User Emotion

<table><tr><td></td><td>Inf_Score</td><td>Anger</td><td>Anticipation</td><td>Disgust</td><td>Fear</td><td>Joy</td><td>Sadness</td><td>Surprise</td><td>Trust</td></tr><tr><td>Inf_Score</td><td>-</td><td>0.00</td><td>-0.01</td><td>0.08</td><td>0.01</td><td>0.01</td><td>0.09</td><td>0.00</td><td>-0.01</td></tr><tr><td>Anger</td><td>0.16</td><td>-</td><td>0.24</td><td>0.89**</td><td>0.47</td><td>0.37</td><td>0.90**</td><td>0.36</td><td>0.30</td></tr><tr><td>Anticipation</td><td>0.05</td><td>0.02</td><td>-</td><td>0.29</td><td>0.03</td><td>0.60**</td><td>0.36</td><td>0.00</td><td>0.56**</td></tr><tr><td>Disgust</td><td>0.19</td><td>0.07</td><td>0.21</td><td>-</td><td>0.09</td><td>0.36</td><td>0.95**</td><td>0.00</td><td>0.27</td></tr><tr><td>Fear</td><td>0.19</td><td>0.47</td><td>0.08</td><td>0.85**</td><td>-</td><td>0.14</td><td>0.81**</td><td>0.11</td><td>0.11</td></tr><tr><td>Joy</td><td>0.09</td><td>0.03</td><td>0.61**</td><td>0.46</td><td>0.04</td><td>-</td><td>0.56**</td><td>0.00</td><td>0.51**</td></tr><tr><td>Sadness</td><td>0.17</td><td>0.14</td><td>0.22</td><td>0.95**</td><td>0.18</td><td>0.40</td><td>-</td><td>0.01</td><td>0.29</td></tr><tr><td>Surprise</td><td>0.06</td><td>0.29</td><td>0.29</td><td>0.33</td><td>0.17</td><td>0.38</td><td>0.42</td><td>-</td><td>0.29</td></tr><tr><td>Trust</td><td>0.03</td><td>0.03</td><td>0.65**</td><td>0.36</td><td>0.04</td><td>0.51**</td><td>0.43</td><td>0.00</td><td>-</td></tr></table>

Strong correlations ( 0.5) are shown with \*\*; weak correlations ( 0.3) are shown in light gray.

In Table 5, each cell shows a CCM correlation of using the row variable to cross-map the column variable. CCM uses points with the most similar histories to an independent variable X<sub>j</sub> (e.g., emotion j’s score) to estimate the dependent variable Y (e.g., user influence) (McCracken et al. 2014). The CCM correlation is the Pearson correlation coefficient between Y and $\hat { Y } | M _ { X }$ (an estimate of Y using its CCM with X, see (S1-S3) in (Sugihara et al. 2012)). Using a procedure for simplex prediction as performed in dynamic modeling and CCM (Ye et al. 2016), we determined an embedding dimension of E=2 and tau parameter of =1 for state space reconstruction using all the data points of 5,000 top-ranked users’ influence scores. Unlike Pearson Correlation, CCM correlation is an asymmetric measure of two variables’ correlation. The results in Table 5 show that some CCM correlations are high in both directions (e.g., between Disgust and Sadness and between Trust and Anticipation), while some CCM correlations are high only on one side (e.g.,

#

between Fear and Disgust and between Anger and Disgust). These differences prompted us to examine causal contribution of different emotion types on user influence scores.

To study the causality between emotion types and user influence, we examined convergence in cross-map predictability by computing the CCM correlation as a function of the sample size (a.k.a. library size, L), where L ranges from 10 to 75 (in increments of 5) and each sample contains 300 randomly selected users. The results are plotted in Figure 11, which shows eight charts representing CCM correlation between user influence scores and the scores of eight emotion types. The red line in each chart indicates the CCM correlation (C<sub>YX</sub>) of user influence score (Y) cross-mapping an emotion score (X<sub>j</sub>). The blue line in each chart indicates the CCM correlation (C<sub>XY</sub>) of an emotion score (X<sub>j</sub>) cross-mapping user influence score (Y). According to (McCracken et al. 2014; Sugihara et al. 2012), a negative difference of the two CCM correlations ( = C<sub>YX</sub> – C<sub>XY</sub>) indicates that X<sub>j</sub> “CCM causes” Y. All the charts in Figure 11 show negative differences (i.e., blue lines above red lines), meaning that all the emotion scores “CCM cause” (with different extents) user influence. The CCM causality is strongest for the emotions anger and fear, as indicated by the wide margins between blue and red lines in the respective charts. As library sizes increase, CCM correlations increase generally with decreasing rates, thus demonstrating convergence of cross-map prediction. In addition, the charts show that the values of C<sub>XY</sub> for anger, fear, joy, and surprise are consistently higher than their respective Pearson correlations (plotted as gray dashed lines) across different L (beyond 40). The results highlight that these emotion types possess stronger correlations with user influence than their linear correlations. The causal modeling identified the positive nonlinear driving force of these emotion types on user influence.

![](/api/attachments/WCVC793J/fulltext/images/c9f8b0e8f2e5d46c083b567ad0824724ab1bdaf8c6b8d79ce6dedc15110e364d.jpg)  
Figure 11. Plots of CCM correlation and library size (between emotion types and user influence score)

## 4.5 Implications for Researchers and Managers

The findings of this research provide several important implications for understanding interpersonal motivations and emotion in social computing environments, for intelligence gathering and decision support, and for methodology development for SMA.

First, the framework supports new emotion analytics by building a novel analysis understanding of internal characteristics such as user emotion. The analysis pipeline enables longitudinal analysis of emotion on a temporal scale, as shown in Figure 2, and Figure 4 to Figure 6 summarize important statistical measures for tracking changes in messages, sentiment, and aggregate emotion over the study period. The representation of different emotion categories and the computation of user influence reveal intelligence from deeper human emotion and connection rather than only from textual content. The BOSSET system instantiates the framework and facilitates the task of situational understanding of online human behavior based on sentiment and emotion. These IS artifacts serve to enrich the DIKW model and its component phases. Given that collective emotion of social media communities is a key driving force of many decisions in business and policy making, the framework, the IM approach, and the BOSSET system fill a gap in existing research and practice.

Second, dynamic influence modeling of human emotion and user influence demonstrates the potential value of the proposed method to identify influential users and to distinguish relative effects of emotion categories on user influence. The computation of influence scores using the IM and UC methods illustrates diverse views of influence revealed by these methods and allows decision makers to adapt the methods to their needs.

Third, the analyses of sentiment and emotion data can enhance capabilities of online surveillance and monitoring, as demonstrated in the fine-grained computation of intensity of emotion categories and user influence scores. These capabilities have enhanced understanding of human behavior in social media communities beyond simple sentiment polarity classification in prior research (see Section 2.2).

Fourth, the visualization of user influence network and causality analysis confirmed validity of the approach. The strong causality between certain emotion categories (anger and fear) and user influence mean that they are most effective in driving influence in social media communities. On the other hand, social media users could be vulnerable to being manipulated by other users who maliciously spread messages that emphasize anger and fear. Therefore, being able to monitor emotion intensity and emotion’s impact on a social media community can potentially help to identify malicious usage.

## 5. CONCLUSION

The widespread use of social media in individuals’ lives and organizational management has provided many opportunities for examining human emotion and its effect on aggregate online influence. However, the process by which emotion produces influence in large-scale online social media networks is relatively unknown.

## 5.1 Summary of Findings

This research developed a novel framework for dissecting emotion and examining user influence in online social media networks. The framework enables collection, influence modeling, and visualization of human emotion expressed in social media messages. Motivated by a theory of emotion spread, a dynamic influence model was developed and integrated in an influence-computation method, called the IM approach, which was compared with a benchmark using a UC approach based on social positions. A proof-of-concept system named BOrder Security Social Emotion Tracker (BOSSET) incorporated the two approaches to extract information of emotion from social media messages and to compute user influence scores.

The novelty of the framework includes different emotion categories and their relationship with user influence, computation of influence scores using the IM and UC approaches, analysis of emotion spreading in online community, and unique modeling of causality between emotion and user influence. The BOSSET system incorporates components of the framework to perform analyses, summarization, and visualization of 5,327,813 tweets posted by 1,303,477 unique users who discussed U.S. borders security issues. Empirical findings of the system reveal significant fluctuations of emotion scores over the period of study. Comparison of two methods for modeling dynamic user influence (IM and UC) showed that IM identified opinion leaders who have broad connections to politics, mass media, cultural, and religious issues that are tied to the topic of U.S. border security and immigration. Analysis of distribution of emotion ratios showed that the emotions fear, disgust, anger, and sadness distinguish influential users from less influential ones. The results of network visualization and CCM validated the accuracy of the influence model by enabling observation of macroscopic online behavior and by identifying causality between emotion types and user influence.

## 5.2 Contributions and Limitations

This research should contribute to advancing the fields of SMA, providing new IS artifacts, and to enriching the DIKW model. The new IS artifacts include a novel framework for dissecting emotion and user influence in social media communities, an information system named BOSSET for tracking emotion and influence in U.S. border security social media discussion, and the IM approach that models dynamic user influence based on the psychological theory. The research provides new empirical findings on CCM causality whose application was traditionally restricted to the field of ecology. The causal modeling highlighted several emotion types with strong CCM causality and identified the respective nonlinear driving force on user influence. The results have strong implications on SMA, business analytics, public policy informatics, and social and behavioral research. The developed framework and IS artifacts can enrich knowledge discovery and wisdom manifestation of the DIKW model by providing suitable guidance and analysis results of emotion and user influence in social media.

This research has several limitations. There is a lack of prior study of human emotion in social computing environment. Thus, the identification of relevant works and techniques was a nontrivial task in this research before the technical infrastructure was built. While the data are available in a large volume, the resources available to collect and handle the data were limited. For example, dynamic influence modeling required intensive computation. Processing speed and retrieval efficiency of the system limited the scale of the computation. In addition, despite being a promising approach, CCM causality was not studied widely beyond the field of ecology. Relevant prior work is very limited.

## 5.3 Future Directions

The research can be extended in several directions. First, the methods used to extract emotion may be extended to develop dynamic lexicons that adapt to new vocabulary and expressions that constantly appear in social media. These methods may use machine learning and natural language processing techniques to identify relevant terms and to relate them to human emotion. For example, Abraham et al. developed an integrated framework for discovering products defects from social media (Abrahams et al. 2015). Second, the IM technique may be extended to incorporate prior evidence and contextual factors into computation of user influence.

#

The evidence and factors may include individuals’ attributes and assumptions, environmental preferences toward users, and seasonal factors that favor certain users. An example of such application is in computing user influence in social-network-based crowdsensing applications (Liu et al. 2018). Third, additional data with a longer time span (e.g., 5 to 10 years) may be collected to enable discovery of trends and fluctuation in public emotion, network relationships, and causal changes. The new findings can provide new insights into temporal movements of participants’ behavior, which can be correlated with other social and economic factors to provide a deeper explanation of empirical observations. The resulting models and techniques could have general applicability in different fields.

## Acknowledgments

The first author was supported in part by the U.S. Defense Advanced Research Projects Agency (under contract no. FA8650-18-C-7824) and by Florida Center for Cybersecurity (under award no. 2108-1106-00-G) and the second author was supported in part by the National Natural Science Foundation of China under Grant No. 71621002 and the Chinese Academy of Sciences under Grant ZDRW-XH-2017-3. Any opinions, findings, and conclusions or recommendations expressed in this paper are those of the authors and do not necessarily reflect the views of the funding agencies.

## 6. REFERENCES

Abrahams, A. S., Fan, W. G., Wang, G. A., Zhang, Z. J., and Jiao, J. 2015. "An Integrated Text Analytic Framework for Product Defect Discovery," Production and Operations Management (24:6) Jun, pp. 975-990.

Ackoff, R. L. 1989. "From data to wisdom," Journal of Applied Systems Analysis (16), pp. 3-9.

Aspara, J., and Tikkanen, H. 2011. "Individuals’ Affect-Based Motivations to Invest in Stocks: Beyond Expected Financial Returns and Risks," Journal of Behavioral Finance (12:2), pp. 78- 89.

Baggia, P., Pelachaud, C., Peter, C., and Zovato, E. 2014. "Emotion Markup Language (EmotionML) 1.0," https://www.w3.org/TR/2014/REC-emotionml-20140522/.

Banerjee, A., Chandrasekhar, A. G., Duflo, E., and Jackson, M. O. 2013. "The Diffusion of Microfinance," Science (341:6144) 2013-07-26 00:00:00.

Bastiaansen, J., Thioux, M., and Keysers, C. 2011. "Evidence for mirror systems in emotions," Philosophical Transactions of The Royal Society B (364), pp. 2391-2404.

Benjamin, V., Chung, W., Abbasi, A., Chuang, J., Larson, C. A., and Chen, H. 2014. "Evaluating Text Visualization for Authorship Analysis," Security Informatics (3:10).

Bond, R. M., Fariss, C. J., Jones, J. J., Kramer, A. D. I., Marlow, C., and Settle, J. E. 2012. "A 61- million-person experiment in social influence and political mobilization," Nature (489:7415), pp. 295-298.

Briggs, R. O., Vreede, G.-J. D., Nunamaker, J. F., and Sprague, R. 2002. "Special Issue: decisionmaking and a hierarchy of understanding," Journal of Management Information Systems (18:4), pp. 5-10.

Bush, J., McLarty III, T. F., and Alden, E. H. 2009. U.S. immigration policy, Council on Foreign Relations: New York.

Cebrian, M., Rahwan, I., and Pentland, A. 2016. "Beyond Viral," Communications of the ACM (59:4) Apr, pp. 36-39.

Celli, F., Ghosh, A., Alam, F., and Riccardi, G. 2016. "In the mood for sharing contents: Emotions, personality and interaction styles in the diffusion of news," Information Processing & Management (52:1) 1//, pp. 93-98.

Chen, H., Chiang, R., and Storey, V. 2012. "Business Intelligence and Analytics," MIS Quarterly (36:4), pp. 1165-1188.

Cheng, P. Y. K. 2010. "Improving Financial Decision Making With Unconscious Thought: A Transcendent Model," Journal of Behavioral Finance (11:2).

Choudhury, M. D., Monroy-Hernández, A., and Mark, G. 2014. ""Narco" emotions: affect and desensitization in social media during the mexican drug war," in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Association for Computing Machinery.

Chung, W. 2014. "BizPro: Extracting and Categorizing Business Intelligence Factors from Textual News Articles," International Journal of Information Management (34:2), pp. 272-284.

Chung, W. 2016. "Social Media Analytics: Security and Privacy Issues," Journal of Informaiton Privacy and Security (12:3), pp. 105-106.

Chung, W., Chen, H., and Nunamaker, J. F. 2005. "A visual framework for knowledge discovery on the Web: An empirical study on business intelligence exploration," Journal of Management Information Systems (21:4), pp. 57-84.

Chung, W., Chen, H., and Reid, E. 2009. "Business stakeholder analyzer: An experiment of classifying stakeholders on the Web," Journal of the American Society for Information Science and Technology (60:1), pp. 59-74.

Chung, W., and Tseng, T.-L. 2012. "Discovering business intelligence from online product reviews: A rule-induction framework," Expert Systems with Applications (39:15), pp. 11870- 11879.

Chung, W., and Zeng, D. 2018. "Social-Media-Based Policy Informatics: Cases on Cybersecurity and Public Health Informatics," in Policy Analytics, Modelling, and Informatics, G.-G. J., P. T. and L.-R. L. (eds.), Springer, Cham.

Clayton, M., Sager, R., and Will, U. 2005. "In time with the music: the concept of entrainment and its significance for ethnomusicology," European Meetings in Ethnomusicology (11), pp. 1-82.

Cohen, J. 1960. "A coefficient of agreement for nominal scales," Educational and Psychological Measurement (20), pp. 27-46.

Darwin, C. 1872. The Expression of Emotion in Man and Animals, John Murray: London, UK.

Dwyer, D. 2014. "President Obama Offers Legal Status to Millions of Undocumented Immigrants," 11-20-2014 (available at http://abcnews.go.com/Politics/president-obama-offerlegal-status-millions-undocumented-immigrants/story?id=27063573).

Fan, W., and Gordon, M. D. 2014. "The Power of Social Media Analytics," Communications of the ACM (57:6), pp. 74-81.

Feldman, R. 2013. "Techniques and applications for sentiment analysis," Communications of the ACM (56:4), pp. 82-89.

Fersini, E., Messina, E., and Pozzi, F. A. 2016. "Expressive signals in social media languages to improve polarity detection," Information Processing & Management (52:1) 1//, pp. 20-35.

Freeman, L. C. 1977. "A set of measures of centrality based on betweenness," Sociometry (40:1), pp. 35-41.

Fung, I. C.-H., Duke, C. H., Finch, K. C., Snook, K. R., Tseng, P.-L., Hernandez, A. C., Gambhir, M., Fu, K.-W., and Tse, Z. T. H. 2016. "Ebola virus disease and social media: A systematic review," American Journal of Infection Control ((forthcoming)).

Gans, J., Replogle, E. M., and Tichenor, D. J. (eds.) Debates on U.S. Immigration. Sage Publications, Inc.2012.

Geweke, J. 1982. "Measurement of Linear-Dependence and Feedback between Multiple Time-Series," Journal of the American Statistical Association (77:378), pp. 304-313.

Granger, C. W. J. 1969. "Investigating Causal Relations by Econometric Models and Cross-Spectral Methods," Econometrica (37:3), pp. 414-&.

Grasso, F. 2002. "Towards computational rhetoric," Informal Logic (22:3), pp. 195-204.

Guellil, I., and Boukhalfa, K. 2015. "Social big data mining: A survey focused on opinion mining and sentiments analysis," in Programming and Systems (ISPS), 2015 12th International Symposium on, pp. 1-10.

Han, S., Lerner, J., and Keltner, D. 2007. "Feelings and consumer decision making: the appraisaltendency framework," Journal of Consumer Psychology (17:3), pp. 158-168.

Hevner, A. R., March, S. T., Park, J., and Ram, S. 2004. "Design science in information systems research," Management Information Systems Quarterly (28:1), pp. 75-105.

Jackson, M. O. 2008. Social and Economic Networks, Princeton University Press: Princeton, NJ.

Kane, G. C., Alavi, M., Labianca, G. J., and Borgatti, S. P. 2014. "What's different about social media networks? A framework and research agenda," MIS Quarterly (38:1), pp. 275-304.

Kaw, A., and Kalu, E. 2008. Numerical Methods with Applications, (1st. ed.) www.autarkaw.com.

Kramer, A. D., Guillory, J. E., and Hancock, J. T. 2014. "Experimental evidence of massive-scale emotional contagion through social networks," Proceedings of the National Academy of Sciences (111:29), pp. 8788-8790.

Laurenson, L. 2017. "Social Media Platforms Can Be Built Around Quality, Not Scale," Harvard Business Review).

LeMay, M. C. 2004. U.S. immigration: A reference handbook, ABC-CLIO: Santa Barbara, Calif.

Liang, Y., Zheng, X., Zeng, D. D., Zhou, X., Leischow, S. J., and Chung, W. 2015. "Characterizing Social Interaction in Tobacco-Oriented Social Networks: An Empirical Analysis," Nature Scientific Reports (5).

Liu, B. 2011. "Opinion Mining and Sentiment Analysis," Web Data Mining: Exploring Hyperlinks, Contents, and Usage Data, Second Edition), pp. 459-526.

Liu, B. 2015. "Sentiment Analysis: Mining Opinions, Sentiments, and Emotions," Sentiment Analysis: Mining Opinions, Sentiments, and Emotions), pp. 1-367.

Liu, J., Shen, H., Narman, H. S., Chung, W., and Lin, Z. 2018. "A Survey of Mobile Crowdsensing Techniques: A Critical Component for The Internet of Things," ACM Trans. Cyber-Phys. Syst. (2:3), pp. 1-26.

Mani, I. 2013. "Computational modeling of narrative," in Synthesis lectures on human language technologies,, Morgan & Claypool,: San Rafael, Calif. (1537 Fourth Street, San Rafael, CA 94901 USA), pp. 1 online resource (xvii, 124 p.).

McCracken, J. M., and Weigel, R. S. 2014. "Convergent cross-mapping and pairwise asymmetric inference," Physical Review E (90:6) Dec 1.

McHugh, M. L. 2012. "Interrater reliability: the kappa statistic," Biochem Med (Zagreb) (22:3), pp. 276-282.

Meckler, L., Nelson, C. M., and Morath, E. 2014. "Obama to Protect 4 Million-Plus Immigrants From Deportation," 11-20-2014 (available at http://www.wsj.com/articles/president-obamaannounces-moves-to-overhaul-immigration-1416502101).

Mohammad, S. M., and Kiritchenko, S. 2015. "Using hashtags to capture fine emotion categories from tweets," Computational Intelligence (31:2), pp. 301-326.

Mohammad, S. M., and Turney, P. D. 2013. "Crowdsourcing a Word-Emotion Association Lexicon," Computational Intelligence (29:3), pp. 436-465.

Nielsen, F. Å. 2011. "A new ANEW: Evaluation of a word list for sentiment analysis in microblogs," in arXiv:1103.2903 [cs.IR]: https://arxiv.org/abs/1103.2903.

Norman, D. A. 1995. "Introduction to human-computer interaction," in Readings in Human-Computer Interaction: Toward the Year 2000 (2nd edition), R. M. Baecker, W. Buxton, S. Greenberg and J. Grudin (eds.), Morgan Kaufmann: San Francisco, CA, pp. 1-3.

Olson, J., and Olson, G. 1990. "The growth of cognitive modeling in human-computer interaction since GOMS," Human-Computer Interaction (5), pp. 221-265.

Pang, B., and Lee, L. 2008. "Opinion Mining and Sentiment Analysis," Foundations and Trends® in Information Retrieval (2:1–2), pp. 1-135.

Pappas, I. O., Kourouthanassis, P. E., Giannakos, M. N., and Chrissikopoulos, V. 2016. "Explaining online shopping behavior with fsQCA: The role of cognitive and affective perceptions," Journal of Business Research (69:2) Feb, pp. 794-803.

Pappas, I. O., Kourouthanassis, P. E., Giannakos, M. N., and Chrissikopoulos, V. 2017. "Sense and sensibility in personalized e-commerce: How emotions rebalance the purchase intentions of persuaded customers," Psychology & Marketing (34:10) Oct, pp. 972-986.

Petty, R., and Cacioppo, J. 1986. "The Elaboration Likelihood Model of Persuasion," in Advances in Experimental Social Psychology, L. Berkowitz (ed.), Academic Press: New York, pp. 123- 205.

Plutchik, R. 1980. "A general psychoevolutionary theory of emotion," Emotion: Theory, research, and experience (1:3), pp. 3-33.

Rangel, F., and Rosso, P. 2016. "On the impact of emotions on author profiling," Information Processing & Management (52:1) 1//, pp. 73-92.

Rosso, P., Bosco, C., Damiano, R., Patti, V., and Cambria, E. 2016. "Emotion and sentiment in social and expressive media: Introduction to the special issue," Information Processing & Management (52:1) 1//, pp. 1-4.

Saif, H., He, Y., Fernandez, M., and Alani, H. 2016. "Contextual semantics for sentiment analysis of Twitter," Information Processing & Management (52:1) 1//, pp. 5-19.

Sánchez-Rada, J. F., and Iglesias, C. A. 2016. "Onyx: A Linked Data approach to emotion representation," Information Processing & Management (52:1) 1//, pp. 99-114.

Scharl, A., Hubmann-Haidvogel, A., Jones, A., Fischl, D., Kamolov, R., Weichselbraun, A., and Rafelsberger, W. 2016. "Analyzing the public discourse on works of fiction – Detection and visualization of emotion in online coverage about HBO’s Game of Thrones," Information Processing & Management (52:1) 1//, pp. 129-138.

Scherer, K. R. 2005. "What are emotions? And how can they be measured?," Social Science Information Sur Les Sciences Sociales (44:4) Dec, pp. 695-729.

Scherer, K. R. 2009. "The dynamic architecture of emotion: Evidence for the component process model," Cognition and Emotion (23:7) 2009/11/01, pp. 1307-1351.

Scherer, K. R., and Ekman, P. (eds.) Approaches to emotion. Psychology Press2014.

Schreck, T., and Keim, D. 2013. "Visual analysis of social media data," IEEE Computer (46:5), pp. 68-75.

Schuler, D. 1994. "Social Computing," Communications of the ACM (37:1) Jan, pp. 29-29.

Sherry, J. 1991. "Postmodern Alternatives: The Interpretive Turn in Consumer Research," Handbook of Consumer Behavior), pp. 548-591.

Song, X., Chi, Y., Hino, K., and Tseng, B. 2007. "Identifying opinion leaders in the blogosphere," in Proceedings of the sixteenth ACM conference on Conference on information and knowledge management, ACM pp. 971-974.

Statman, M., Fisher, K. L., and Anginer, D. 2008. "Affect in a behavioral asset pricing model," Financial Analysts Journal (64), pp. 20-29.

Stieglitz, S., and Dang-Xuan, L. 2013. "Emotions and Information Diffusion in Social Media-Sentiment of Microblogs and Sharing Behavior," Journal of Management Information Systems (29:4) Spr, pp. 217-247.

Straker, K., and Wrigley, C. 2016. "Designing an emotional strategy: Strengthening digital channel engagements," Business Horizons (59:3) May-Jun, pp. 339-346.

Strapparava, C., and Valitutti, A. 2004. "Wordnet-affect: an affective extension of wordnet," in Proceedings of the 4th International Conference on Language Resources and Evaluation, Lisbon, Portugal.

Sugihara, G., May, R., Ye, H., Hsieh, C. H., Deyle, E., Fogarty, M., and Munch, S. 2012. "Detecting Causality in Complex Ecosystems," Science (338:6106) Oct 26, pp. 496-500.

Tayouri, D. 2016. "Social media as an intelligence goldmine," Cyber Security Review:Spring), pp. 27-30.

Teng, Z., Ren, F., and Kuriowa, S. 2007. "Emotion Recognition from Text Based on the Rough Set Theory and the Support Vector Machines," in 2007 International Conference of the Natural Language Processing and Knowledge Engineering, IEEE Computer Society, Beijing, China, pp. 36 – 41.

Tettegah, S. (ed.) Emotions, Technology, and Social Media. Elsevier2016.

U.S. Commission on Immigration Reform 1994. U.S. immigration policy - Restoring credibility: A report to Congress, U.S. Commission on Immigration Reform: Washington, DC (1825 Connecticut Ave., NW, Suite 511, Washington 20009).

Volkova, S., and Bachrach, Y. 2015. "On Predicting Sociodemographic Traits and Emotions from Communications in Social Networks and Their Implications to Online Self-Disclosure," Cyberpsychology, Behavior, and Social Networking (18:12) 2015/12/01, pp. 726-736.

Wang, F.-Y., Carley, K. M., Zeng, D., and Mao, W. 2007. "Social Computing: From Social Informatics to Social Intelligence," IEEE Intelligent Systems (22:2), pp. 79-83.

Wang, G. A., Jiao, J., Abrahams, A. S., Fan, W. G., and Zhang, Z. J. 2013. "ExpertRank: A topicaware expert finding algorithm for online knowledge communities," Decision Support Systems (54:3) Feb, pp. 1442-1451.

Wasserman, S., and Faust, K. 1994. Social Network Analysis: methods and applications, Cambridge University Press.

Wiebe, J., Wilson, T., and Cardie, C. 2005. "Annotating expressions of opinions and emotions in language," Language Resources and Evalution (formerly Computers and the Humanities) (1:2), pp. 1-54.

Wikipedia 2016. "Social Computing," https://en.wikipedia.org/wiki/Social\_computing.

Xie, H., Li, X., Wang, T., Lau, R. Y. K., Wong, T.-L., Chen, L., Wang, F. L., and Li, Q. 2016. "Incorporating sentiment into tag-based user profiles and resource profiles for personalized search in folksonomy," Information Processing & Management (52:1) 1//, pp. 61-72.

Ye, H., Clark, A., Deyle, E., and Sugihara, G. 2016. "rEDM: an R package for Empirical Dynamic Modeling and Convergent Cross-Mapping," https://cran.rproject.org/web/packages/rEDM/vignettes/rEDM\_tutorial.html.

Zappen, J. P. 2005. "Digital Rhetoric: Toward an Integrated Theory," Technical Communication Quarterly (14:3) 2005/07/01, pp. 319-325.

Zeng, D., Chen, H., Castillo-Chavez, C., Lober, W. B., and Thurmond, M. 2011. Infectious Disease Informatics and Biosurveillance, Springer.

Zeng, D., Chen, H., Lusch, R., and Li, S.-H. 2010. "Social Media Analytics and Intelligence," IEEE Intelligent Systems (25:6), pp. 13-16.

Zhang, J., Ackerman, M. S., and Adamic, L. 2007. "Expertise networks in online communities: structure and algorithms," in Proceedings of the 16th international conference on World Wide Web, ACM New York, NY, USA, Banff, Alberta, Canada, pp. 221 - 230.

#

## Author Biography

Wingyan Chung, Ph.D. is an associate professor in the Institute for Simulation and Training (IST) at University of Central Florida (UCF). Dr. Chung's scholarly interests and expertise include social media analytics, business intelligence, cybersecurity, data and text mining, Web analytics, knowledge management, information visualization, and human-computer interaction. He has published over 100 refereed articles in such journals and conferences as Scientific Reports, Journal of Management Information Systems, Communications of the ACM, IEEE Computer, Decision Support Systems, Journal of the Association for Information Science and Technology, and International Conference on Information Systems. He is ranked among the Top 20 academic authors globally in Business Intelligence and Analytics. He has received over 7 million US dollars in research funding from the National Science Foundation, Department of Defense, Department of Homeland Security, Intel Corporation, and Florida Center for Cybersecurity, among others.

Daniel Dajun Zeng, Ph.D. is Gentile Family Professor in the Department of Management Information Systems at the University of Arizona. Dr. Zeng's research interests include intelligence and security informatics, spatial-temporal data analysis, infectious disease informatics, social computing, recommender systems, software agents, and applied operations research and game theory. He has published more than 300 peer-reviewed articles and received more than US\$28 million research support. An IEEE fellow, he served as the Editor in Chief of IEEE Intelligent Systems and is President of IEEE ITS Society (2016-2017).
