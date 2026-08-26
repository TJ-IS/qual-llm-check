---
otero_id: 4260
otero_key: "BDEGGNFK"
title: "More than Words in Medical Question-and-Answer Sites: A Content-Context Congruence Perspective"
authors: "Chih-Hung Peng; Dezhi Yin; Han Zhang"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0923"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.238.7.40] On: 13 May 2020, At: 22:58 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/BDEGGNFK/fulltext/images/5f3c70074589117bd446c943b6d716df17c1f2623cc29817d961082766cdb7ce.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# More than Words in Medical Question-and-Answer Sites: A Content-Context Congruence Perspective

Chih-Hung Peng, Dezhi Yin, Han Zhang

Chih-Hung Peng, Dezhi Yin, Han Zhang (2020) More than Words in Medical Question-and-Answer Sites: A Content-Context Congruence Perspective. Information Systems Research

Published online in Articles in Advance 05 May 2020

https://doi.org/10.1287/isre.2020.0923

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# More than Words in Medical Question-and-Answer Sites: A Content-Context Congruence Perspective

Chih-Hung Peng,<sup>a</sup> Dezhi Yin,<sup>b</sup> Han Zhang

<sup>a</sup> College of Commerce, National Chengchi University, Taipei 11605, Taiwan; <sup>b</sup> Muma College of Business, University of South Florida, Tampa, Florida 33620; <sup>c</sup> Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30308 Contact: chpeng@nccu.edu.tw, https://orcid.org/0000-0002-7101-7999 (C-HP); dezhiyin@usf.edu, https://orcid.org/0000-0003-1107-3232 (DY); han.zhang@scheller.gatech.edu, https://orcid.org/0000-0002-6258-2486 (HZ)

Received: Revised: August 28, 2017; Octob Accepted: Published Online in Articles in Advance: May 5,2020

https://doi.org/10.1287/isre.2020.0923

Copyright:

Abstract. Given the popularity and prevalence of medical question-and-answer (Q&A) services, it is increasingly important to understand what constitutes a helpful answer in the medical domain. Prior studies on user-generated content have examined the independent impacts of content and source characteristics on reader perception of the content's value. In the setting of medical Q&A sites, we propose a novel content-context congruence perspective with a focus on the role of congruence between an answer’s content and the answer’s contextual cues. Specifically, we identify two types of contextual cues critical in this unique setting—the language attributes (i.e., concreteness and emotional intensity) of the question’s content, and the acuteness of the disease to which the question is related. Building on the priming literature and construal-level theory, we hypothesize that an answer will be perceived as more helpful if the language attributes of the answer’s content are congruent with those of the preceding question, and if they are congruent with the disease’s acuteness. Analyses of a unique data set from WebMD Answers provide empirical evidence for our theoretical model. This research deepens our understanding of readers value judgment of online medical information, demonstrates the importance of considering the congruence of content with contextual cues, and opens up exciting opportunities for future research to explore the role of content-context congruence in all varieties of usergenerated content. Our findings also provide direct practical implications for knowledge contributors and Q&A sites.

History: Rajiv Kohli, Senior Editor; Sam Ransbotham, Associate Editor. Funding: This work was partially supported by the Ministry of Science and Technology of Taiwan [Grant MOST 108-2410-H-004-227-MY2] and by E.SUN Bank. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2020.0923.

Keywords: medical Q&A • answer helpfulness • user-generated content • content-context congruence • fit • concreteness emotional intensity • construal level

## Introduction

As the internet enables people to easily access health information (Erdem and Harrison-Walker 2006, Kivits 2006), the general public increasingly turns to the internet to seek help and advice over health concerns, medical questions, and doctors’ suggestions (Agarwal et al. 2010, Fichman et al. 2011). According to the “The Great American Search for Healthcare Information” survey of 1700 American adults, 73% obtained health-related information from the internet (Weber Shandwick 2018). In another nationally representative survey of over 1300 U.S. teens and young adults (14–22 years old), 87% reported that they had searched online for health information (Rideout and Fox 2018). People seek online health information primarily because of their health conditions or illnesses, and they most often go to websites about specific health conditions (Cornejo 2018). In fact, more and more patients rely on the internet as their first source to acquire knowledge about their own health conditions before pursuing a professional diagnosis (Tan and Goonawardene 2017). There is no doubt that the internet and constantly evolving social technologies are transforming the healthcare industry as well as the way people seek health information and knowledge.

The most popular online resources for health-related information include WebMD, Facebook, YouTube, and Twitter (Stricker 2014). As the most accessed website for health information, WebMD provides a questionand-answer (Q&A) platform, wherein people can search for answers and ask questions (Harper et al. 2009). Although most people believe the medical information they obtain online (e.g., from medical Q&A sites) is trustworthy and of good quality (Taylor 2011), this is not always the case (Silberg et al. 1997, McLeod 1998). Because the health information that people find online has measurable impacts on their health-related decisions (Lawhon 2016), a deeper understanding of people’s value judgment of online medical information is especially critical for patients, medical institutions, and society at large.

In this study, we examine what constitutes a helpful answer on medical Q&A sites. An important feature of many Q&A sites is a helpfulness voting system that relies on “wisdom of the crowd” to gauge the perceived value of information provided in an answer. To reduce information overload and highlight more valuable content (Jones et al. 2004), many Q&A sites allow readers to cast votes on the helpfulness of answers and display helpful answers more prominently. When future readers decide which content to read, they also rely heavily on the judgment of others, such as helpfulness evaluation of the content (Otterbacher et al. 2011). Thus, a better understanding of the factors influencing answer helpfulness can assist future readers with finding helpful information more easily and motivate contributors to create more useful information. This understanding is even more critical in the medical domain, as the medical answers that readers deem more valuable should be incorporated more into their health-related decisions and have critical implications for their lives.

In the medical setting, we define the helpfulness of an answer to a medical question as the extent to which the answer is perceived to facilitate readers health-related judgment and decisions (Mudamb and Schuff 2010, Yin et al. 2014). Answer helpfulness reflects information diagnosticity, as the answer can provide diagnostic value across multiple stages of readers decision-making process (Mudambi and Schuff 2010). Prior studies on perceived value of answers in Q&A sites have examined the impact of answer characteristics, among which the most frequently studied is answer length or the total amount of information contained in an answer (Shah and Pomerantz 2010, Edelman 2012). In addition, existing research in the Q&A setting has studied the role of various contextual cues—influential characteristics of environmental signals that surround the focal content (Murnane et al. 1999). Note that contextual cues are signals from the content’s environment, not characteristics of the content. Studies have examined how a reader’s value assessment of an answer could be shaped by the question’s features (Harper et al. 2008, Shah and Pomerantz 2010, Zhang and Wang 2016), source characteristics (Edelman 2012, Lou et al. 2013, Oh and Worrall 2013), and the type of Q&A sites (Chen et al. 2010, Jeon et al. 2010, Fichman 2011).

Our research deviates from earlier work in two important ways. First, we situate our study in the setting of medical Q&A sites and highlight the critical role of two unique types of contextual cues—the language attributes of a question and the acuteness of the disease associated with the question. These cues are similar to a product’s characteristics (such as its average rating and product type) in the online review setting because they are all signals from the environment surrounding the target of users’ value judgment (i.e., answers and reviews, respectively). However, the question and the disease are two unique aspects of medical Q&A sites that are not present in other types of user-generated content. These two types of contextual cues are also highly relevant for the judgment of answer helpfulness in medical Q&A sites, as an answer in this unique setting is always a response addressing a particular question and a particular disease. Second, despite significant progress made toward understanding the impacts of content characteristics and contextual cues on a reader’s value assessment of an answer, the role of content-context congruence is relatively unexplored.<sup>1</sup> However, some emerging studies in user-generated content have revealed that readers’ evaluation of content helpfulness is not context-free because contextual cues can shape readers’ beliefs and mindsets (Huang et al 2013, Yin et al. 2016). Drawing on the priming literature and construal-level theory (Winkielman and Cacioppo 2001, Trope and Liberman 2011), we propose that question-answer congruences and diseaseanswer congruences can increase a reader’s perceived helpfulness of the answer. An empirical analysis of data collected from WebMD Answers provides evidence for our predictions.

This research demonstrates the critical role of contentcontext congruence in the helpfulness evaluation of answers in medical Q&A sites and makes two key contributions. First, this research complements and extends recent findings in other settings that value judgment of content is not context-free (Yin et al. 2016). Although it is intuitive to assume that perceived helpfulness of certain content is determined primarily by the content itself, we propose and find evidence for a more nuanced perspective emphasizing the importance of congruence between content and contextual cues. This content-context congruence perspective extends the proposals of value-from-fit from goal pursuit (Higgins 2000) and truth-from-fit from lie detection (Hansen and Wanke¨ 2010) to reader evaluation of user-generated content, suggesting that readers also derive value from the congruence of content features with their context.<sup>2</sup> Although our hypotheses are situated in the specific setting of medical Q&A sites, the broader content-context congruence perspective can be applied to other types of Q&A sites and all types of user-generated content. Thus, this paper opens up exciting opportunities for future research to explore the role of interplay between content and context in readers’ judgment and decision making.

Second, we take advantage of the unique nature of the medical Q&A sites and identify two types of relevant and prominent contextual cues in this setting. In particular, our theoretical framework and findings highlight the critical role of diseases and deepen our understanding of readers’ value judgment of medical answers that can have life-changing consequences. Given the huge presence and undisputable significance of medical Q&A sites in people’s daily lives, we believe our findings have strong practical implications.

## Literature Review

User-generated content (UGC) refers to content that is created by members of the general public and distributed over the internet (Daugherty et al. 2008, Krumm et al. 2008), such as consumer reviews on e-commerce sites and answers on Q&A sites. Prior literature on the antecedents of perceived UGC diagnosticity has examined both content and contextual cues. In the setting of consumer reviews, which has received the most academic attention (see Cheung and Thadani 2012 for a literature review), a large body of studies examined how a review’s content characteristics, such as length, readability, and emotional expression, can influence the perceived helpfulness of the review (Mudambi and Schuff 2010; Yin et al. 2014, 2017). In addition, some studies investigated the effect of contextual cues, such as source and product characteristics (Forman et al. 2008, Mudambi and Schuff 2010, Cheung et al. 2012).

As the popularity of online Q&A sites grows, researchers have become increasingly interested in the perceived value of answers (Shah and Pomerantz 2010, Lou et al. 2013, Oh and Worrall 2013). The literature on Q&A has also investigated the effect of content and contextual cues. Some studies focused on the characteristics of an answer, such as answer length (Shah and Pomerantz 2010, Edelman 2012), emotional support (Kim and Oh 2009), and politeness (Lee et al. 2019). Other studies examined the contextual cues available from the question, source, and even Q&A sites. Question-level factors that have been studied include question length (Shah and Pomerantz 2010, Zhang and Wang 2016), topic (e.g., technology, business, and entertainment) (Harper et al. 2008), and the number of answers to the question (Shah and Pomerantz 2010). Source characteristics include the answer contributor’s expertise (Edelman 2012, Oh and Worrall 2013), experience (Shah and Pomerantz 2010, Oh and Worrall 2013), reputation (Chen et al. 2010), and motivation (Lou et al. 2013). The type of Q&A sites has also been examined as a contextual cue (Harper et al. 2008, Chen et al. 2010, Jeon et al. 2010, Fichman 2011). Online Appendix A reviews the studies conducted in the Q&A setting and summarizes the examined antecedents of the perceived value of answers.

Despite the ample UGC research into content and contextual cues, limited attention has been paid to the interaction between them or how their interplay affects reader perception of content diagnosticity (Cheung and Thadani 2012). Notably, a few emerging studies in online reviews suggest that the impact of review content on review helpfulness is not context-free, but is instead dependent on contextual cues, such as the average rating or type of product (Huang et al. 2013, Yin et al. 2016). Inspired by value-from-fit proposal in goal pursuit (Higgins 2000) and task-technology fit theory (Goodhue and Thompson 1995), we apply the fit perspective to medical Q&A sites and argue that answer content may be perceived to be more helpful if its characteristics are congruent with the contextual cues available from the unique setting.

## Theory and Hypotheses Development Congruence

The concept of congruence is receiving more attention in various academic disciplines, and a growing stream of research has demonstrated the importance of congruence between an entity and its contextual cues (Edwards 2008). For example, in goal pursuit, people experience regulatory fit when the manner of their engagement in an activity (e.g., eager or vigilant) fits their goal orientation or interests regarding that activity at the moment (e.g., promotion or prevention) (Higgins 2005). This regulatory fit can increase value judgments and evaluations, such as consumers’ perceived value of their choices (Avnet and Higgins 2006). Similarly, task-technology fit theory posits that information technology is more likely to be used and positively influence individual performance when the technology’s capabilities match the tasks that the user must perform (Goodhue and Thompson 1995).

In this paper, we apply the notion of fit or congruence to user-generated content and argue that content-context congruence plays an indispensable role in readers’ value evaluations. When people read and evaluate a piece of content, information contained in the content is the focus of their attention. At the same time, they are also exposed to contextual cues—defined as information that is present in the content’s environment but is peripheral to the focus of attention (Murnane et al. 1999). In the setting of medical Q&A sites, we propose that the congruence of an answer’s content characteristics with contextual cues from the question and the disease topic can influence reader perception of answer helpfulness.

In the following, we introduce two characteristics of answer content: language concreteness and emotional intensity. Furthermore, we identify two classes of contextual cues unique in medical Q&A sites: concreteness and emotional intensity expressed in the content of a question, and the acuteness of a disease. We finally develop and propose our hypotheses regarding question-answer congruences and diseaseanswer congruences.<sup>3</sup> Our theoretical framework is illustrated in Figure 1.

## Language Concreteness and Emotional Intensity

Answer contributors can write an answer in different ways (i.e., making use of different words) while expressing the same idea. In addition to the substantive content of a message (i.e., what is being conveyed), the attributes of its language can also influence the audience (Bradac et al. 1979, Miller et al. 2007). Even when the substantive content of two messages is similar, variation in the use of specific words may lead readers to perceive the messages in different ways, which can influence their evaluation of the messages (Berry et al. 1997). In this paper, we focus on two aspects of language used in the content of answers: one cognitive and the other emotional.

First, a cognitive aspect of language is its concreteness level, as answers on medical Q&A sites can be framed in either a concrete or abstract manner when addressing the same question and conveying a similar meaning. We define language concreteness as the extent to which words provide descriptive, specific, and vivid information about an object or situation (Hansen and Wanke¨ 2010). For example, “a stethoscope” and “a medical device” can be used to describe the same equipment in our setting, but the former is more concrete and less abstract than the latter. Compared with abstract language, concrete language is better recalled (Tse and Altarriba 2009), judged as more truthful (Hansen and Wanke¨ 2010), and is more persuasive in shaping attitudes and behaviors (Larrimore et al. 2011). In user-generated content, the concreteness of words used in online reviews increases consumers’ evaluation of reviews helpfulness (Li et al. 2013). We expect language concreteness to also play a role in readers’ helpfulness evaluation of answers on Q&A sites.

In addition to the cognitive aspect of the content, answer contributors may also express their feelings to varying degrees. We define emotions in our setting as subjective feelings expressed by the content contributor, and we define emotional intensity as the percentage of expressed emotions in the content, following the existing literature (Fujita et al. 1991, Kahn et al. 2007). Emotional expressions are prevalent in user-generated content. Although emotions are typically not part of the substantive content, they can have critical implications for reader value perception of the content. For example, the intensity of expressed emotions in an online review presents a prominent signal for readers to make sense of the review (Jensen et al. 2013), and it can influence reader perception of review helpfulness in sophisticated manners (Yin et al. 2017). On community-based social Q&A sites where users form a community and support each other, emotional support is an important selection criterion for best answers (Kim et al. 2007, Kim and Oh 2009). Similarly, on Q&A sites primarily used for knowledge exchange, answer contributors can express emotions at different intensity levels. Next, we develop hypotheses about the impact of congruence in content characteristics between a question and its answer on reader evaluation of that answer’s helpfulness.

Figure 1. Theoretical Framework  
![](/api/attachments/BDEGGNFK/fulltext/images/a7185f9d45a751caffd9ba2f0b488bc9f564ad23d5c6c089a568b550775557d7.jpg)

## Question-Answer Congruences

Contextual cues present within the questions can shape reader evaluation of answers (Harper et al. 2008, Shah and Pomerantz 2010). After users input keywords to search for answers to a question on a Q&A site, they typically see a list of previously asked questions. When they click on a specific question, that question is universally displayed on top of the page followed by answers to that question. Readers are very likely to first read the question and judge its relevance to their inquiry before reading the answers. In the setting of online reviews, consumers would observe a product’s average rating and other summary rating statistics before reading individual reviews, and empirical evidence suggests that their evaluation of an individual review’s helpfulness is shaped by the contextual cues, such as the product’s average rating (Yin et al. 2016). It is reasonable to expect the same to occur on Q&A sites, whereby a reader’s evaluation of an individual answer’s helpfulness can be shaped by contextual cues, such as the language attributes of the question’s content.

Whereas answer content may vary in language concreteness and emotional intensity, question content can also vary in regard to these language attributes. In our first two hypotheses, we argue that question-answer congruences could contribute to the perceived value of the answer. A probable reason for this effect is that priming facilitates processing and enhances fluency (Winkielman et al. 2012). Fluency is broadly defined as an individual’s subjective experience of the ease with which he or she processes information (Oppenheimer 2008). Fluency arises from a wide variety of factors, such as font clarity, visual contrast, and repeated exposure (Alter and Oppenheimer 2009). Most relevant to our purposes, fluency can arise from a priming effect of the question’s content characteristics. Specifically, the observation of a stimulus (called the prime) can reduce reaction time to subsequently encountered related concepts, because the prime activates related concepts in memory, and this preactivation leads to faster identification (Collins and Loftus 1975). In particular, prior exposure to certain stimuli has been found to enhance fluency of matching stimuli when compared with nonmatching stimuli at a later time (Winkielman and Cacioppo 2001).

The way in which a question is written might prime readers and lead them to be more fluent with answers having matching content characteristics. Reading ques tions associated with concrete thinking can activate one’s concrete mindset and predispose the individua to concrete words in the memory (Freitas et al. 2004, Wakslak and Trope 2009). When readers are primed by a concrete question and put into a concrete mindset, they should find concrete answers easier to process than abstract answers, and vice versa. Similarly, the mere observation of emotionally laden stimuli (i.e., affect primes) can elicit emotions in the observers by preactivating emotion-related words and concepts in their memory (Chartrand et al. 2006). When readers are primed by an emotion-laden question, they should find emotional answers more fluent than nonemotional answers, and vice versa.

Moreover, fluency is typically associated with positive evaluations (Winkielman et al. 2012). The ease of processing indicates the likelihood of an external stimulus being good or bad. In fact, fluency is usually a learned and readily available heuristic for identifying better choices (Gigerenzer 2007). A wide range of studies have provided evidence that fluency obtained through various means (such as repetition and priming) enhances liking, even for an initially neutral stimulus (see Reber et al. 2004 for a comprehensive review). Physiological evidence also shows that flu ency triggers stronger activity over the “smiling” region of the brain (Winkielman and Cacioppo 2001). Applied to our setting, answers that readers find more fluent should be evaluated more positively. Taken together, we propose that the congruence in language concreteness or emotional intensity between a question and its answer—namely, the question-answer concreteness congruence and question-answer emotion congruence—can enhance the perceived helpfulness of the answer.

Hypothesis 1. The congruence in language concreteness between an answer and its question is positively related to the perceived helpfulness of the answer.

Hypothesis 2. The congruence in emotional intensity between an answer and its question is positively related to the perceived helpfulness of the answer.

## Disease-Answer Congruences

Our next set of hypotheses argue that disease-answer congruences can also contribute to the perceived value of the answer. In addition to question characteristics, the unique setting of medical Q&A sites creates another prominent contextual cue. A distinctive aspect of various diseases is that they differ in treatment duration. Diseases are typically classified into acute diseases that last a limited period of time and chronic diseases that are lengthy in duration (Perrin et al. 1993,

Murrow and Oglesby 1996). Because disease topics that users inquire about on medical Q&A sites vary significantly in terms of urgency and duration, the acute nature of a disease could influence users’ mindset as they seek medical information and advice (Holman and Lorig 2004).

In this paper, we define disease acuteness as the extent to which a disease is urgent and short-term in nature (Parkes and Jewell 2001, Zochling et al. 2006). Because acute diseases can be cured in a short time, readers consulting questions related to an acute disease tend to think about how to treat it in a timely manner. On the other hand, chronic diseases are typically long-lasting conditions; thus, readers concerned with a chronic disease tend to reflect on how to deal with its long-term consequences, which may be unclear until sometime in the distant future. Notably, disease acuteness reflects temporal distance, defined as the perception of some event being close to or far away from the reference point of the present (Maglio et al. 2013).

According to construal-level theory, temporal distance has direct implications on the level of mental construal—the extent to which people’s thinking about an event is at a concrete or abstract level (Liberman and Trope 1998, Trope and Liberman 2003). As temporal distance of an event increases, the thinking of the event would be more abstract in people’s minds (Trope and Liberman 2010). This is because high-level abstract mental representations are more likely than low-level concrete mental representations to remain unchanged as people get closer to the events in the distant future (Trope and Liberman 2011). For example, contacting a friend is more abstract than sending that friend a WhatsApp message. If this action happens in the distant future (e.g., in a year), then people are more likely to think about contacting the friend because this abstract notion is more stable over time than sending the WhatsApp message; in fact, the platform of WhatsApp might not be available when one is trying to contact the friend in a year’s time (e.g., Yahoo Messenger was discontinued). As a result, it is more useful for people to think about distant events with a more abstract (and thus stable) mindset, and to think about urgent events with a more concrete mindset. On medical Q&A sites, readers of an answer addressing an acute (or chronic) disease should be predisposed to think about the disease in a concrete (or abstract) manner.

Because the differences in temporal distance of events can lead to mindsets at different construal levels, greater congruence between temporal distance and the concreteness level of information in a message can make the message more persuasive and, thus, more diagnostic (Kim et al. 2009). This effect can be explained using the same fluency arguments from before: when temporal distance (and the corresponding activated mental construal of a person’s mindset—thinking at a concrete or abstract level) is congruent with the concreteness of information, the person tends to experience increased fluency, which in turn leads to a more positive evaluation of the information (Reber and Schwarz 1999, Oppenheimer 2006). For example, a number of experimental studies in message-framing literature find compelling evidence that higher congruence between a message’s concreteness level and the psychological distance (such as temporal distance, social distance, etc.) inherent in the decision-making context can positively influence attitudes and behaviors (White et al. 2011, Freling et al. 2014).

The aforementioned reasoning suggests that the congruence between disease acuteness and information concreteness can increase perceived helpful ness of the information, whereas the concreteness level of a message can manifest in different ways. First, the concreteness level of words used in the message is the most straightforward reflection of that message’s concreteness level. The use of more concrete words indicates a more concrete message, whereas the use of more abstract words indicates a more abstract message. In the medical setting, when readers encounter answer information with a concreteness leve that matches disease acuteness (for example, a concrete answer to a question on an acute disease, or an abstract answer to a question on a chronic disease), they are likely to experience greater fluency (Reber et al. 2004) and perceive the answer to be more helpful. In contrast, when readers encounter answer information with concreteness that does not match disease acuteness they are less likely to experience fluency and thus may perceive the answer to be less helpful. Therefore, the congruence between disease acuteness and the answer’s concreteness level should positively influence readers’ perceived helpfulness of the answer, and we propose the following hypothesis regarding this congruence (hereafter, disease-answer concreteness congruence).

Hypothesis 3. The congruence between an answer’s concrete level and disease acuteness is positively related to the perceived helpfulness of the answer.

Second, a message’s concreteness level can manifest in the intensity of expressed emotions. Although emotionally charged words are distinct from either concrete or abstract words (Altarriba et al. 1999, Altarriba and Bauer 2004), experimental studies have provided evidence that emotional words are more vivid than neutral or nonemotional words (Dewhurst and Parry 2000, Kensinger and Corkin 2003). Survey data also supported that emotionally charged words are rated as more concrete and vivid (Campos 1989). Thus, even if the concreteness level of words used in substantive content is held constant, more intense expressions of emotion should result in a more concrete answer. Extending the same reasoning from construallevel theory to our setting, readers are likely to experience greater fluency when they encounter answers with an emotional intensity that matches disease acuteness (for example, an emotional answer responding to a question on an acute disease, or a nonemotional answer responding to a question on a chronic disease). The positive experience of fluency can result in a more positive evaluation of the answer. In contrast, readers are less likely to experience fluency when the answer’s emotional intensity does not match disease acuteness (for example, an emotional answer addressing a question on a chronic disease, or a nonemotional answer addressing a question on an acute disease). This reduced fluency should lead readers to rate the answer as less helpful. Therefore, we propose the following hypothesis regarding the congruence between disease acuteness and answer emotional intensity (hereafter, disease-answer emotion congruence).

Hypothesis 4. The congruence between an answer’s emotional intensity and disease acuteness is positively related to the perceived helpfulness of the answer.

To summarize, we have presented a theoretical framework in this section that focuses on the critical role of congruence between unique contextual cues (i.e., language attributes of the question and acuteness of diseases) and language attributes of answer content in the setting of medical Q&A sites. Based on the priming literature and construal-level theory (Winkielman and Cacioppo 2001, Trope and Liberman 2011), we hypothesize that question-answer congruences and disease-answer congruences can positively influence the perceived value of answers.

## Method and Results

To test these hypotheses, we collected and analyzed a unique data set from WebMD Answers. According to Comscore’s Media Metrix report (Comscore 2013), WebMD.com is the leading healthcare portal, with over 50 million unique visitors per month. As one of its provided services, WebMD Answers allows users to ask medical questions under a range of diverse categories, such as bipolar disorder, high blood pressure, pregnancy, and others. Because medical questions are classified into diverse disease topics, data from WebMD Answers enable us to quantify the key independent variables and are ideal for testing the proposed hypotheses. In January 2018, we collected the content of all 26,318 questions and their answers, categorized under 99 common disease topics that WebMD Answers organized for users to explore. We collected 35,098 answers in total, 16,802 of which (over 46%) had received at least one vote. We also collected data on 3022 distinct authors who provided the answers.

## Measures

The dependent variable is answer helpfulness (helpfulness). For each answer from WebMD Answers, we collected the following data in addition to the answer content: the number of “helpful” votes and the number of total votes (that is, the total number of users who voted either “yes” or “no” to the question, “Was this helpful?”). Following prior literature (Mudambi and Schuff 2010, Yin et al. 2014), we measured helpfulness at the answer level using the ratio of the number of helpful votes to the total number of votes for an answer.

The independent variables of interest are four cogni tive and emotional congruence variables—two of these are factors measuring congruence between a question and its answer (question-answer concreteness congruence and question-answer emotion congruence), whereas the other two are factors measuring congruence between the acuteness of disease topic discussed in the question and the answer (disease-answer concreteness congruence and disease-answer emotion congruence). Before we can quantify these congruence variables, we need to measure the concreteness and emotiona intensity of each question and answer and the acuteness of the relevant disease.

First, to measure content concreteness, we relied on the dictionary of concreteness ratings of nearly 40,000 generally known English words and expressions obtained through internet crowdsourcing (Brysbaert et al. 2014). The dictionary provides the ratings of these words and expressions on a five-point scale ranging from abstract to concrete. We adopted this dictionary in our study because (1) it is specifically designed for measuring language concreteness, (2) its reliability and validity have been demonstrated by its creators, and (3) it has been used to quantify language concreteness in the medical setting (Cousins et al. 2018) as well as in online reviews (Ransbotham et al. 2019). Notably, this dictionary includes words from the med ical domain. For example, “disinfection” has a concreteness rating of 2.67, whereas “aorta” has a concreteness rating of 4.61. To calculate the average concreteness of an answer, we divided the sum of concreteness ratings of words in the answer by the total number of words in the answer. We calculated the average concreteness of a question in a similar way.

Second, we used Linguistic Inquiry and Word Count (LIWC) software to compute the emotional intensity of each question and answer. Pennebaker et al. (2007) developed a psychometrically validated dictionary composed of over 4,000 words and word stems assigned to multiple categories. This tool has been widely adopted in various fields (Tausczik and Pennebaker 2010) and extensively validated (Pennebaker and Francis 1996, Pennebaker et al. 2007). Most relevant for our purposes, this dictionary includes a list of words that indicate positive or negative emotions. LIWC has been found to be a valid tool for measuring emotional discourse (Kahn et al. 2007, Bantum and Owen 2009), and it is increasingly used by information systems and marketing scholars to quantify emotional expression in various types of user-generated content (Schweidel and Moe 2014, Yin et al. 2014, Ransbotham et al. 2019). Following common practice and suggestions from the LIWC inventors (Pennebaker et al. 2007), we measured emotional intensity by calculating the number of emotional words (identified by the LIWC dictionary) divided by the total number of words.

Third, we measured the acuteness of each disease topic through the professional evaluations obtained from family physicians. WebMD Answers categorized the questions and their answers under 99 common disease topics. We recruited three American family physicians and instructed them to independently rate the acuteness of 99 health topics listed by WebMD Answers. Specifically, each physician read the definitions for acute and chronic diseases and then evaluated each disease along a five-point Likert scale (1 = always chronic, 2 = often chronic, 3 = sometimes chronic and sometimes acute, 4 = often acute, 5 = always acute).<sup>4</sup> In order to assess the reliability of this measure, we calculated Cohen’s kappa among the three physicians for each disease (Cohen 1960). The average index was 0.54, suggesting moderate agreement among the physicians (McHugh 2012).<sup>5</sup> As a result, we aggregated these ratings for each disease and used the mean values as a measure for disease acuteness.

Finally, we measured the four congruence variables through the commonly used difference score approach (David et al. 1989, Keller 1994, Oh and Pinsonneault 2007, Tilcsik 2014). This approach is deemed appropriate for examining congruence concepts when congruence is defined theoretically as a match between two component variables that are independent of the outcome variable (supposedly predicted by the congruence) (Venkatraman 1989). Under this circumstance, the difference score measurement provides a variety of advantages over other approaches (including residuals, interactions, and split-sample analyses): it reduces the measurement error and interpretation problems associated with residuals from regression equations; alleviates the multicollinearity concern from the use of interaction terms; and addresses the problems of restricted range, reduced sample size, and interpretation of congruence magnitude that occur in a split-sample analysis (Venkatraman 1989, Keller 1994). Therefore, we applied the difference score approach in the present study, as content concreteness, emotional intensity, and disease acuteness are all independent from the helpfulness of answer content at the theoretical level.

For each congruence variable, we first standardized both components making up the congruence because some component variables (e.g., answer emotional intensity and disease acuteness) were measured along different scales. Then, we calculated the absolute dif ference between these two standardized component variables. To ease interpretation, we multiplied the absolute difference by <sup>−</sup>1 to create the measure for the congruence variables: a higher value of the congruence variable indicates greater congruence between its two components. We used this same procedure to operationalize the two question-answer congruence variables and the two disease-answer congruence variables. As an example, disease-answer concreteness congruence was measured as the extent to which the concreteness level of the answer’s content matches the acuteness of the disease topic associated with the question.

We also included a series of control variables to account for the influence of source, answer, and question characteristics. First, source characteristics have been found to contribute to information helpfulness (Forman et al. 2008, Cheung et al. 2012). For the Q&A setting, we controlled for author expertise, which is a dummy variable indicating whether the contributor of an answer is an expert (e.g., MD, which stands for “doctor of medicine”). We also accounted for author credibility, operationalized as the total number of helpful votes an author had received divided by the total number of questions that author had answered.

Next, we controlled for characteristics of answer content that may influence its information helpful ness. First, the amount of information was measured by answer length and defined as the number of words in an answer (answer length). Second, the difficulty of reading an answer (answer reading difficulty) has direct implications for its perceived helpfulness (Korfiatis et al. 2012). Thus, we calculated the Coleman-Liau index as a proxy for reading difficulty, which is an estimate of the U.S. grade level that a student would need to read and understand a text sample (DuBay 2004). Third, because of a potential relationship between total votes and content helpfulness (Mudambi and Schuff 2010), we included the total number of votes an answer received (answer total votes) as a control. Fourth, an older answer may have had more time to accumulate more helpful votes. Thus, we also controlled for the number of days (answer days) since the answer was posted. Fifth, we controlled for an answer’s concreteness (answer concreteness) and emotional intensity (answer emotional intensity) that might directly impact answer helpfulness. Sixth, the first few answers to a question are likely to receive more votes than later answers on the page, so we controlled for the sequence of a focal answer (answer sequence).

Finally, we included a dummy variable to indicate whether there are any other answers marked as helpful (other helpful answers): 1 if yes, 0 otherwise.

We also included relevant control variables at the question level. We accounted for the generality of the question by counting the number of keywords identified by WebMD for a specific question (question keywords). A question with more keywords is considered a more general question because it can be answered from more perspectives, potentially increasing the difficulty of creating helpful answers. We also included the number of words in each question (question length) in the models.

Finally, we used disease-level fixed effects to control for disease topic heterogeneity. These fixed effects are algebraically equivalent to including a dummy for every disease in our sample, and so they enabled us to control for differences in the average helpfulness of answers across diseases. Moreover, we controlled for the temporal trend in answers. It is likely that helpful ratings change as a Q&A website matures. Therefore, we included month-year pair dummies and the dummies for the days of a week. Table 1 reports the descriptive statistics for the variables in our analysis, and Table 2 reports the correlations.

## Data Analysis and Results

The dependent variable, the ratio of the number of helpful votes over the total number of votes for an answer, is bounded between 0 and 1. Given that a bounded dependent variable leads to inconsistent parameter estimates using ordinary least squares (OLS), we used the two-limited Tobit model (Greene 2003, Kennedy 2008). This model has been widely used in diverse disciplines, including marketing, strategy, finance, management, and information systems (Luo and Homburg 2007, Barthélemy 2008, Sosa 2009 Ferreira et al. 2010, Mudambi and Schuff 2010).

Table 3 presents the results of the main regressions used to test our hypotheses. We standardized all continuous independent variables to ease the comparison of effect sizes. We first entered the control variables in Model 1 (baseline model) and then added the four congruence variables in Model 2. We conducted the likelihood ratio (LR) test to compare Model 2 with Model 1 and found that the addition of the four congruence variables improves the model fit significantly $( p < 0 . 0 0 1 )$ ). Furthermore, to assess any potential multicollinearity, we calculated variance inflation factor (VIF) scores for all independent and control variables in Model 2. The scores were all below the rule-of-thumb value of 10 (Kennedy 2008), indicating that multicollinearity was not a concern.

Hypotheses 1 and 2 propose a positive effect of the congruence in concreteness and emotional intensity between a question and its answer on the perceived helpfulness of that answer. In Model 2 of Table 3, question-answer concreteness congruence was positively related to helpfulness $( \beta = 0 . 0 0 3 , \bar { p } < 0 . 0 1 )$ , and questionanswer emotion congruence was positively related to helpfulness $( \beta = 0 . 0 \dot { 0 } 3 , p < 0 . 0 5 )$ . Controlling for other factors, an answer whose concreteness or emotional intensity is more similar to that of its corresponding question is expected to be more helpful. Therefore, the first two hypotheses are supported.

Hypotheses 3 and 4 propose a positive effect of the congruence between disease acuteness and an answer’s concreteness or emotional intensity on the perceived helpfulness of the answer. In Model 2 of Table 3, disease-answer concreteness congruence was positively related to helpfulness $( \beta = 0 . 0 \dot { 0 } 6 , p < 0 . 0 1 )$ and disease-answer emotion congruence was positively related to helpfulness $( \beta = 0 . 0 0 4 , p < 0 . 0 1 )$ . Controlling for other factors, an answer with a higher level of congruence between its concreteness or emotional intensity and the acuteness of its corresponding disease topic is expected to be more helpful. Therefore, the last two hypotheses are supported.<sup>6</sup>

Table 1. Descriptive Statistics

<table><tr><td></td><td>Mean</td><td>SD</td><td>Min</td><td>Median</td><td>Max</td></tr><tr><td>1. Helpfulness</td><td>0.59</td><td>0.17</td><td>0.03</td><td>0.55</td><td>1.00</td></tr><tr><td>2. Question-answer concreteness congruence</td><td>-1.32</td><td>1.20</td><td>-12.76</td><td>-1.06</td><td>0.00</td></tr><tr><td>3. Question-answer emotion congruence</td><td>-1.33</td><td>1.29</td><td>-23.23</td><td>-1.02</td><td>0.00</td></tr><tr><td>4. Disease-answer concreteness congruence</td><td>-1.25</td><td>1.11</td><td>-12.03</td><td>-1.05</td><td>0.00</td></tr><tr><td>5. Disease-answer emotion congruence</td><td>-1.35</td><td>1.02</td><td>-24.04</td><td>-1.20</td><td>0.00</td></tr><tr><td>6. Author expertise</td><td>0.21</td><td>0.41</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>7. Author credibility</td><td>28.85</td><td>134.38</td><td>0.00</td><td>12.34</td><td>8,812.00</td></tr><tr><td>8. Answer length</td><td>95.48</td><td>97.67</td><td>1.00</td><td>64.00</td><td>853.00</td></tr><tr><td>9. Answer reading difficulty</td><td>10.68</td><td>5.15</td><td>-16.10</td><td>10.20</td><td>137.00</td></tr><tr><td>10. Answer total votes</td><td>48.11</td><td>424.33</td><td>1.00</td><td>12.00</td><td>23,698.00</td></tr><tr><td>11. Answer days</td><td>1,874.20</td><td>868.78</td><td>187.00</td><td>1,701.00</td><td>4,956.00</td></tr><tr><td>12. Answer concreteness</td><td>2.21</td><td>0.31</td><td>0.00</td><td>2.23</td><td>4.89</td></tr><tr><td>13. Answer emotional intensity</td><td>5.60</td><td>4.81</td><td>0.00</td><td>5.00</td><td>100.00</td></tr><tr><td>14. Answer sequence</td><td>1.38</td><td>1.44</td><td>1.00</td><td>1.00</td><td>24.00</td></tr><tr><td>15. Other helpful answers</td><td>0.30</td><td>0.46</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>16. Question keywords</td><td>3.00</td><td>1.52</td><td>1.00</td><td>3.00</td><td>5.00</td></tr><tr><td>17. Question length</td><td>31.97</td><td>36.49</td><td>0.00</td><td>15.00</td><td>112.00</td></tr></table>

Note. Max, maximum; Min, minimum; SD, standard deviation.

Table 2. Correlations

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td></tr><tr><td>1. Helpfulness</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Question-answer concreteness congruence</td><td>0.11</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Question-answer emotion congruence</td><td>0.14</td><td>0.12</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Disease-answer concreteness congruence</td><td>0.10</td><td>0.61</td><td>0.11</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Disease-answer emotion congruence</td><td>0.06</td><td>0.11</td><td>0.34</td><td>0.24</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Author expertise</td><td>0.10</td><td>0.08</td><td>0.01</td><td>0.08</td><td>-0.06</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. Author credibility</td><td>0.06</td><td>0.01</td><td>0.05</td><td>0.01</td><td>0.00</td><td>0.04</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8. Answer length</td><td>0.26</td><td>0.14</td><td>0.17</td><td>0.16</td><td>0.16</td><td>-0.01</td><td>0.11</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9. Answer reading difficulty</td><td>0.12</td><td>-0.12</td><td>0.05</td><td>-0.13</td><td>0.02</td><td>0.06</td><td>0.04</td><td>0.10</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10. Answer total votes</td><td>0.06</td><td>0.00</td><td>0.03</td><td>0.00</td><td>-0.01</td><td>0.01</td><td>0.55</td><td>0.08</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11. Answer days</td><td>0.29</td><td>0.15</td><td>0.26</td><td>0.11</td><td>0.09</td><td>-0.01</td><td>0.08</td><td>0.27</td><td>0.31</td><td>0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12. Answer concreteness</td><td>0.04</td><td>0.48</td><td>0.02</td><td>0.45</td><td>-0.02</td><td>0.07</td><td>-0.01</td><td>-0.02</td><td>-0.16</td><td>0.00</td><td>0.03</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13. Answer emotional intensity</td><td>-0.04</td><td>0.04</td><td>-0.12</td><td>0.06</td><td>0.00</td><td>-0.13</td><td>-0.03</td><td>-0.06</td><td>0.00</td><td>-0.02</td><td>-0.09</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>14. Answer sequence</td><td>-0.01</td><td>-0.09</td><td>-0.04</td><td>-0.07</td><td>-0.03</td><td>-0.12</td><td>0.02</td><td>-0.05</td><td>-0.03</td><td>0.02</td><td>-0.14</td><td>-0.01</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>15. Other helpful answers</td><td>-0.06</td><td>-0.11</td><td>-0.09</td><td>-0.07</td><td>-0.02</td><td>-0.16</td><td>0.02</td><td>-0.09</td><td>-0.06</td><td>0.06</td><td>-0.21</td><td>-0.02</td><td>0.03</td><td>0.41</td><td>1.00</td><td></td><td></td></tr><tr><td>16. Question keywords</td><td>-0.23</td><td>-0.07</td><td>-0.28</td><td>-0.04</td><td>-0.05</td><td>0.02</td><td>-0.05</td><td>-0.15</td><td>-0.23</td><td>-0.03</td><td>-0.48</td><td>0.00</td><td>0.05</td><td>0.06</td><td>0.14</td><td>1.00</td><td></td></tr><tr><td>17. Question length</td><td>-0.21</td><td>-0.06</td><td>-0.27</td><td>-0.04</td><td>-0.01</td><td>-0.05</td><td>-0.04</td><td>-0.10</td><td>-0.23</td><td>-0.01</td><td>-0.50</td><td>-0.04</td><td>0.07</td><td>0.06</td><td>0.16</td><td>0.69</td><td>1.00</td></tr></table>

As robustness checks, we conducted a number of additional tests (see Online Appendix B) to address the following potential issues: a sample selection bias, the interdependence of answers within the same topic, the bounded nature of our ratio-based dependent variable, extreme values of our dependent variable when the total number of helpfulness votes is small, and endogeneity caused by reverse causality or omitted variables. All our results still hold when using alternative models in these robustness checks.

## General Discussions

Situated in the critical and unique setting of medical Q&A sites, we supplement an emerging stream of research studying factors that influence the perceived helpfulness of user-generated content (Mudambi and Schuff 2010, Jensen et al. 2013, Yin et al. 2014) and explore what constitutes a helpful answer to a medical question. Focusing on two unique types of contextual cues—the language attributes of the question and the acuteness level of the associated disease—we propose a content-context congruence perspective: an answer that is congruent with its question or disease will be rated by readers as more helpful. An empirical analysis of data from WebMD Answers provides evidence for our proposed theoretical framework. At a broader level, the results illustrate the important role of content-context congruence in studying the perceived value of usergenerated content and demonstrate its important implications for both theory and practice.

## Theoretical Implications

This paper offers a number of theoretical contributions. First and foremost, this study proposes a congruence perspective in explaining users’ value perception of user-generated content. Although previous studies on antecedents of information helpfulness generally assumed that content needs to be written in a certain way or placed in a certain context in order to be considered helpful, emerging evidence in online reviews suggests that contextual cues can influence the beliefs and mindsets of consumers as they read and make sense of the reviews (Yin et al. 2016, Huang et al. 2018). Building on and going beyond recent studies that found “context matters,” we advance a congruence perspective inspired by fit theories in organizational behavior, individual goal pursuit, and individual performance in information technology use. In organi zations, an employee whose individual needs, values, and goals are congruent with the organization’s culture, values, and norms (namely, person-organization fit) performs better and has higher job satisfaction (Hoffman and Woehr 2006). When people pursue a goal, a regulatory fit between the way they engage in an activity and their goal orientation increases their perceived value of the activity (Higgins 2005). In the use of information systems, a task-technology fit between the technology’s capabilities and the associated tasks increases technology adoption and individual performance (Goodhue and Thompson 1995). All of these theories share the perspective that the congruence between someone or something and its environment leads to positive outcomes.

Table 3. Tobit Regressions

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td>Author expertise</td><td>0.043***(0.004)</td><td>0.041***(0.004)</td></tr><tr><td>Author credibility</td><td>-0.001(0.001)</td><td>-0.001(0.001)</td></tr><tr><td>Answer length</td><td>0.026***(0.001)</td><td>0.024***(0.001)</td></tr><tr><td>Answer reading difficulty</td><td>0.004***(0.001)</td><td>0.006***(0.001)</td></tr><tr><td>Answer total votes</td><td>0.002(0.001)</td><td>0.002(0.001)</td></tr><tr><td>Answer days</td><td>0.049(0.139)</td><td>0.038(0.138)</td></tr><tr><td>Answer concreteness</td><td>0.004***(0.001)</td><td>0.0001(0.001)</td></tr><tr><td>Answer emotional intensity</td><td>0.003***(0.001)</td><td>0.003**(0.001)</td></tr><tr><td>Answer sequence</td><td>0.006***(0.001)</td><td>0.006***(0.001)</td></tr><tr><td>Other helpful answers</td><td>0.002*(0.001)</td><td>0.002**(0.001)</td></tr><tr><td>Question keywords</td><td>-0.019***(0.002)</td><td>-0.019***(0.002)</td></tr><tr><td>Question length</td><td>-0.001(0.002)</td><td>-0.001(0.002)</td></tr><tr><td>Question-answer concreteness congruence</td><td></td><td>0.003***(0.001)</td></tr><tr><td>Question-answer emotion congruence</td><td></td><td>0.003**(0.001)</td></tr><tr><td>Disease-answer concreteness congruence</td><td></td><td>0.006***(0.001)</td></tr><tr><td>Disease-answer emotion congruence</td><td></td><td>0.004***(0.001)</td></tr><tr><td>Constant</td><td>0.481(0.412)</td><td>0.511(0.411)</td></tr><tr><td>N</td><td>16,726</td><td>16,726</td></tr><tr><td>Log likelihood</td><td>5,519.81</td><td>5,558.64</td></tr><tr><td>p-value, LR test</td><td></td><td>0.000</td></tr></table>

Notes. All continuous independent variables are standardized. Disease topic dummies, days of week dummies, and month-year dummies are included. Standard errors are in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Adapting this perspective to UGC, we derive a congruence-focused theoretical framework based on the priming literature and construal-level theory. Specifically, we argue and find empirical evidence that a greater congruence between content and contextual cues can lead readers to perceive the content as more helpful. In addition to the independent impacts of content characteristics and contextual cues revealed in the UGC literature, the level of congruence between content and context may also play a nontrivial role. For example, concrete information may not always be desirable; rather, its impact can be determined by its congruence with environmental cues, such as those that prime people’s concrete (versus abstract) thinking or activate their concrete (versus abstract) mindsets. Although question and disease characteristics in our setting are very different types of contextual cues compared with a product’s average rating or product type in online reviews, they are all fundamentally environmental signals around the target of users value assessment. Our proposed hypotheses involve characteristics of questions and diseases that may not be applicable in other settings, but our proposed congruence perspective has broader appeals and can be extended to other types of user-generated content, such as online reviews. For example, a match between review content and product type may contribute to perceived value of online reviews (Huang et al. 2013). Our findings highlight the importance of taking this more nuanced congruence perspective when studying the perceived value of user-generated content, and they open up exciting new avenues for future research in this area.

Second, our disease-related findings illustrate the nontrivial role of event timing in influencing readers thinking and their subsequent evaluation of UGC Studies in online word-of-mouth provided evidence that the temporal distance of events (e.g., authoring a review, consuming a product) and other psychologica distances (such as spatial distance and social distance) can jointly affect consumer evaluation and preferences (Zhao and Xie 2011, Huang et al. 2016). Our work complements and extends these earlier studies by demonstrating that the temporal distance of events and user-generated content can also jointly influence readers’ value judgment of the content. This study also illustrates the possibility of applying construallevel theory in online, interpersonal settings where multiple parties (such as content contributors and readers) are involved. Construal-level theory was originally developed to explain how people mentally construe their own personal events that will occur in their near or distant future (Liberman and Trope 1998), and its applications have started to appear in the information systems field over recent years (Ho et al. 2015). This paper extends its application from intrapersonal to interpersonal situations wherein readers make sense of online information produced by others. Although the majority of evidence for construal-level theory comes from laboratory experiments (Trope and

Liberman 2010), this paper is also among the first to provide empirical evidence for the theory based on an analysis of a large-scale archival data set (Huang et al. 2016).

Third, we explore readers’ value evaluation of online health information from medical Q&A sites, a knowledge-focused form of user-generated content that has critical implications for people’s health-related decisions and lives. The majority of studies examining the perceived diagnosticity of content were carried out in the setting of online word-of-mouth (Chevalier and Mayzlin 2006, Mudambi and Schuff 2010, Willemsen et al. 2011). However, critical aspects of online reviews, such as ratings that indicate reviewers’ opinions about a product or service, are not relevant on Q&A websites where the focus is on the effective exchange of information and knowledge. In addition, a product’s average rating represents a critical contextual cue that may influence consumers initial beliefs and their interpretation of reviews (Yin et al. 2016), but this cue is again not relevant on Q&A sites. We argue that the unique nature of medica Q&A sites warrants its own examination. Answers from medical Q&A sites are posted to address specific medical questions and specific diseases that vary in their acuteness. Our findings indicate that these unique contextual cues significantly influence the way that prospective readers make sense of and evaluate answers written in certain ways. For example, our questionrelated hypotheses and findings suggest that questions are an integral part of Q&A sites, and they should not be overlooked in explaining readers’ value judgment of answers. Thus, we not only add to a growing literature examining factors that drive the perceived helpfulness of user contributions, but also contribute to a better understanding of knowledge evaluation—how to identify and promote more helpful answers—in the medical setting.

## Practical Implications

This research offers useful insights for medical sites that intend to educate and help patients looking for answers to their health-related inquiries. Perceived value of online health information is critical because it determines the extent to which the information is incorporated into people’s health decisions and influences health outcomes. Creators of websites providing medical information should be aware that in the healthcare domain, diseases or health conditions are a primary reason for people to search online information in the first place (Cornejo 2018), and they also represent a prominent contextual cue that can shape readers’ thinking and mindsets. Whereas different diseases are necessary in organizing the vast quantity of medical information and advice available online, our findings extend the significance of disease categories from information organization to information evaluation. If the acuteness of two disease categories is very different, then the experience of crafting or selecting the most helpful information for one category of diseases might not be directly applicable for the other category.

This study also offers practical insights for content contributors. Content contributors have a basic human need for competence (Deci and Ryan 2000). Such need is most likely to be satisfied when their contributions are valued and perceived as helpful. Most contributors probably hold the simplistic assumption that answers written in a certain way (e.g., longer, more concrete, etc.) are more valuable. They are typically not aware of the subtle role of contextual cues in prospective readers’ value judgments. Our findings suggest that such awareness is critical for content contributors. For example, concrete information is typically considered more credible and valuable than abstract information (Hansen and Wanke¨ 2010), but the reverse might occur if the question is written in an abstract or nonemotional manner or if the disease is chronic. The mere realization that readers interested in different medical questions may differ in their thinking and mindsets can go a long way in guiding contributors’ writing efforts.

Our findings also have valuable implications for the design of Q&A sites. Content is essential for a Q&A website; if readers perceive the content from the site to be useful for their decision making, they will “stick” to the site longer. Thus, most user-generated content platforms offer guidelines for content contributors in order to guide their writing in ways more conducive to being helpful. These guidelines almost universally promote certain characteristics of content without regard to context, such as providing more details, avoiding being emotional, etc. As an example, guidelines such as “provide details and be specific” may prompt contributors to write more concrete answers regardless of whether the question is written concretely or abstractly, or whether the disease is acute or chronic. Instead of prescribing a simplistic formula centered around characteristics of the “ideal” content, Q&A sites are advised to educate content contributors about the pitfalls of following simple formulas and the diversity of readers looking for answers to different questions. For example, the awareness of “readers interested in chronic diseases are different from those interested in acute diseases” can help contributors reduce their natural tendency to create more concrete answers when they strive to write more valuable answers.

In addition, the helpfulness rating of answers is the primary means by which Q&A sites determine the value of different answers in order to highlight more helpful or the most helpful ones. However, the accumulation of helpfulness votes takes considerable time after an answer is posted. Our work offers useful insights for Q&A sites attempting to develop ways of estimating and predicting, a priori, the extent to which an answer will be perceived as helpful by future readers. In addition to content characteristics most frequently associated with information helpfulness, such as the length of content, our results suggest that the congruence between content and its unique contextual cues should also be taken into consideration in the estimation and prediction of answer helpfulness. Readily available software and dictionaries such as those used in this work can help automate the measurement of content-context congruence and the prediction of answer helpfulness.

## Limitations and Future Directions

A number of exciting opportunities present themselves for future studies. First, it would be valuable for further investigation to explore the mechanisms underlying the impact of content-context congruence on perceived information helpfulness. When readers make sense of certain content, their beliefs and mindsets play a critical role in their helpfulness evaluation of the content (Yin et al. 2016). However, a limitation of this research is the lack of data on readers and voters, which inhibits the possibility of investigating the mechanisms. Our empirical study is also limited in the establishment of causality. Although our hypotheses are described in associational terms, the logic behind them implies that congruence between content and its contextual cues causes greater perceived helpfulness of answers. Although the crosssectional nature of our data makes it challenging to directly examine this causal influence, we conducted various robustness checks (including an analysis using the instrument variable approach) that effectively alleviate concerns of endogeneity. Future research should explore both the underlying mechanisms and causal relationships using complementary methodologies, such as surveys and experiments.

Second, whereas our theoretical framework focuses on the congruence between content characteristics and contextual cues unique in the medical Q&A setting, content-context congruence may play similar roles in other settings of user-generated content involving different types of contextual cues. In online reviews, for example, product type is a prominent contextual cue, and consumers may have a certain expectation for emotional expression in the reviews, depending on the nature of the product (such as hedonic versus utilitarian products). Thus, it stands to reason that a review in which emotional intensity is congruent with product type may be evaluated more favorably. Future research should explore the generalizability of our proposed theoretical framework in other kinds of user-generated content.

Third, our paper examines the consequences of content-context congruence—how this congruence influences readers’ perceived value of answers. It would also be fascinating to explore the sources of content-context congruence. For example, the con creteness level or emotional intensity of content in a question may prime not only readers but also some answer contributors. More studies are needed to uncover the source of congruence as well as the types of contributors who are more likely to write congruent answers.

Fourth, we focus on two content characteristics— language concreteness and emotional intensity—as the basis for our question-answer congruence and disease-answer congruence variables. We selected these variables because they are theory-driven, have been demonstrated as critical in users’ evaluation of information diagnosticity, and can yield meaningful theoretical implications. However, a question and an answer can be congruent in other aspects (e.g., emotional valence), and future research can explore whether sim ilarity in these other aspects can also contribute to answer helpfulness.

Fifth, this research focuses on disease acuteness—one dimension of psychological distance (i.e., temporal distance)—in our latter two hypotheses and archival data analysis. In addition to the temporal dimension, other dimensions of psychological distance (such as spatial distance or social distance) may also play important roles in a variety of user-generated content settings. For example, regarding online reviews, some platforms such as Amazon reveal the geographical locations of reviewers (Forman et al. 2008), which may influence how a consumer evaluates concrete versus abstract reviews, depending on his or her spatial distance from the reviewers. In order to fully understand the role of psychological distance, more studies are needed to explore the effects of its other dimensions and how different dimensions interact to influence user judgment (Zhao and Xie 2011, Huang et al. 2018).

## Conclusion

Complementing the emerging interest in the role of contextual cues in reader helpfulness assessment of certain content, we propose a content-context congruence perspective in order to explain the perceived value of answers on medical Q&A sites. Our research provides real-world evidence that answer content is evaluated as more helpful if it is congruent with the contextual cues unique to medical Q&A sites. We believe that this work extends our current understanding of the interplay between content and context in user-generated content, and we look forward to future research exploring the role of different kinds of content-context congruence in various user-generated content settings.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their constructive guidance during the review process. The authors are grateful to Sabyasachi Mitra and Chih-Ping Wei for their insightful feedback on earlier versions of this paper.

## Endnotes

<sup>1</sup> For brevity, we use “content-context congruence” to refer to the congruence between content characteristics and contextual cues. Note that “content” in content-context congruence means content characteristics or language attributes, not substantive content or wha is being conveyed.

<sup>2</sup> We consider the terms “congruence” and “fit” as interchangeable, and we use “congruence” throughout the paper.

<sup>3</sup> The outcome variable in our research is perceived helpfulness of an answer. Thus, we selected answer-related congruence variables as our independent variables, including question-answer congruences and disease-answer congruences. On the other hand, question-disease congruences might be more relevant for predicting question-level outcome variables, such as intention to read answers after seeing a question (which would be outside the scope of this research).

<sup>4</sup> Among the 99 disease topics, 83 topics were rated by all of the physicians, whereas the rest were rated by one or two physicians. As a robustness check, we conducted the same analyses excluding the observations from disease topics that were rated by only one or two physicians, and we found that the results did not qualitatively differ. To be comprehensive, we report results with answers from all 99 disease topics in the main text.

<sup>5</sup> Our results were robust to using a three-point Likert scale (i.e., collapsing points 1 and 2 to represent “chronic,” and collapsing 4 and 5 to represent “acute”; the average index of Cohen’s kappa was 0.63 in this case, suggesting substantial agreement among the physicians).

<sup>6</sup> Because our congruence variables are composite indices, it may not be reasonable to directly interpret their coefficients. On the other hand, we can compare the effect sizes of congruence variables with other variables known to influence information helpfulness. Fo example, the intensity of emotions expressed in UGC has been revealed to play an important role in readers’ perception of the content (Jensen et al. 2013), and it is also a critical component comprising two of our congruence variables. As shown in Model 2 of Table 3, the effect sizes of the two emotion-related congruence variables (i.e., question-answer emotion congruence and disease-answer emotion congruence) are comparable with the effect sizes of answer emotional intensity.

## References

Agarwal R, Gao G, DesRoches C, Jha AK (2010) Research commentary— The digital transformation of healthcare: Current status and the road ahead. Inform. Systems Res. 21(4):796–809.

Altarriba J, Bauer LM (2004) The distinctiveness of emotion concepts: A comparison between emotion, abstract, and concrete words Amer. J. Psych. 117(3):389–410.

Altarriba J, Bauer LM, Benvenuto C (1999) Concreteness, context availability, and imageability ratings and word associations for abstract, concrete, and emotion words. Behav. Res. Methods In struments Comput, 31(4):578–602

Alter AL, Oppenheimer DM (2009) Uniting the tribes of fluency to form a metacognitive nation. Personality Soc. Psych. Rev. 13(3): 219–235.

Avnet T, Higgins ET (2006) How regulatory fit affects value in consumer choices and opinions. J. Marketing Res. 43(1):1–10.

Bantum EOC, Owen JE (2009) Evaluating the validity of computerized content analysis programs for identification of emotional expression in cancer narratives. Psych. Assessment 21(1):79–88.

Barthélemy J (2008) Opportunism, knowledge, and the performance of franchise chains. Strategic Management J. 29(13):1451–1463.

Berry DS, Pennebaker JW, Mueller JS, Hiller WS (1997) Linguistic bases of social perception. Personality Soc. Psych. Bull. 23(5): 526–537.

Bradac JJ, Bowers JW, Courtright JA (1979) Three language variables in communication research: Intensity, immediacy, and diversity. Human Comm. Res. 5(3):257–269.

Brysbaert M, Warriner AB, Kuperman V (2014) Concreteness ratings for 40 thousand generally known English word lemmas. Behav. Res. Methods 46(3):904–911.

Campos A (1989) Emotional values of words: Relations with concreteness and vividness of imagery. Perceptual Motor Skill 69(2):495–498.

Chartrand TL, van Baaren RB, Bargh JA (2006) Linking automatic evaluation to mood and information processing style: Consequences for experienced affect, impression formation, and stereotyping. J. Experiment. Psych. General 135(1):70–77.

Chen Y, Ho T-H, Kim Y-M (2010) Knowledge market design: A field experiment at Google Answers. J. Public Econom. Theory 12(4): 641–664.

Cheung CMK, Thadani DR (2012) The impact of electronic word-ofmouth communication: A literature analysis and integrative model. Decision Support Systems 54(1):461–470.

Cheung CM-Y, Sia C-L, Kuan KKY (2012) Is this review believable? A study of factors affecting the credibility of online consumer reviews from an elm perspective. J. Assoc. Inform. Systems 13(8): 618–635.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Cohen J (1960) A coefficient of agreement for nominal scales. Ed. Psych. Measurement 20(1):37–46.

Collins AM, Loftus EF (1975) A spreading-activation theory of se mantic processing. Psych. Rev. 82(6):407–428.

Comscore (2013) Comscore Media Metrix ranks top 50 U.S. web properties for February 2013. Accessed April 28, 2013, http:// www.comscore.com/Insights/Press\_Releases/2013/3/comScore \_Media\_Metrix\_Ranks\_Top\_50\_U.S.\_Web\_Properties\_fo February 2013

Cornejo C (2018) Social life of health information. Accessed July 16, 2019, https://www.wegohealth.com/2018/02/05/social-life-of -health-information/.

Cousins KAQ, Ash S, Olm CA, Grossman M (2018) Longitudinal changes in semantic concreteness in semantic variant primar progressive aphasia (SVPPA). eNeuro 5(6):e0197–0118.

Daugherty T, Eastin MS, Bright L (2008) Exploring consumer moti vations for creating user-generated content. J. Interactive Adver tising 8(2):16–25.

David FR, Pearce JA, Randolph WA (1989) Linking technology and structure to enhance group performance. J. Appl. Psych. 74(2): 233–241.

Deci EL, Ryan RM (2000) The “what” and “why” of goal pursuits: Human needs and the self-determination of behavior. Psych Inquiry 11(4):227–268

Dewhurst SA, Parry LA (2000) Emotionality, distinctiveness, and recollective experience. Eur. J. Cognitive Psych. 12(4):541–551.

DuBay WH (2004) The principles of readability. Impact Information, accessed February 16, 2020, http://www.impact-information .com/impactinfo/readability02.pdf.

Edelman B (2012) Earnings and ratings at Google Answers. Econom Inquiry 50(2):309–320

Edwards JR (2008) Person–environment fit in organizations: An assessment of theoretical progress. Acad. Management Ann. 2(1): 167–230.

Erdem SA, Harrison-Walker LJ (2006) The role of the internet in physician–patient relationships: The issue of trust. Bus. Horizons 49(5):387–393.

Ferreira MA, Massa M, Matos P (2010) Shareholders at the gate? Institutional investors and cross-border mergers and acquisitions. Rev. Financial Stud. 23(2):601–644.

Fichman P (2011) A comparative assessment of answer quality on four question answering sites. J. Inform. Sci. 37(5):476–486.

Fichman RG, Kohli R, Krishnan R (2011) Editorial overview—The role of information systems in healthcare: Current research and future trends. Inform. Systems Res. 22(3):419–428.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Freitas AL, Gollwitzer P, Trope Y (2004) The influence of abstract and concrete mindsets on anticipating and guiding others self-regulatory efforts. J. Experiment. Soc. Psych. 40(6):739–752.

Freling TH, Vincent LH, Henard DH (2014) When not to accentuate the positive: Re-examining valence effects in attribute framing. Organ. Behav. Human Decision Processes 124(2):95–109.

Fujita F, Diener E, Sandvik E (1991) Gender differences in negative affect and well-being: The case for emotional intensity. J. Per sonality Soc. Psych. 61(3):427–434.

Gigerenzer G (2007) Gut Feelings: The Intelligence of the Unconsciou (Viking Press, New York).

Goodhue DL, Thompson RL (1995) Task-technology fit and indi vidual performance. MIS Quart. 19(2):213–236.

Greene WH (2003) Econometric Analysis (Prentice Hall, Upper Saddle River, NJ).

Hansen J, Wanke M (2010) Truth from language and truth from¨ fit: The impact of linguistic concreteness and level of construal on subjective truth. Personality Soc. Psychol. Bull. 36(11):1576–1588.

Harper FM, Moy D, Konstan JA (2009) Facts or friends? Distinguishing informational and conversational questions in social Q&A sites. Proc. SIGCHI Conf. Human Factors Comput. (Association for Computing Machinery, New York), 759–768.

Harper FM, Raban D, Rafaeli S, Konstan JA (2008) Predictors of answer quality in online Q&A sites. Proc. SIGCHI Conf. Human Factors Comput. (Association for Computing Machinery, New York), 865–874.

Higgins ET (2000) Making a good decision: Value from fit. Amer. Psych. 55(11):1217–1230.

Higgins ET (2005) Value from regulatory fit. Current Directions Psych. Sci. 14(4):209–213.

Ho CKY, Ke W, Liu H (2015) Choice decision of e-learning system: Implications from construal level theory. Inform. Management 52(2):160–169.

Hoffman BJ, Woehr DJ (2006) A quantitative review of the relationship between person–organization fit and behavioral outcomes. J. Vocational Behav. 68(3):389–399.

Holman H, Lorig K (2004) Patient self-management: A key to effectiveness and efficiency in care of chronic disease. Public Health Rep. 119(3):239–243.

Huang L, Tan C-H, Ke W, Wei K-K (2013) Comprehension and assessment of product reviews: A review-product congruity prop osition. J. Management Inform. Systems 30(3):311–343.

Huang L, Tan CH, Ke W, Wei KK (2018) Helpfulness of online review content: The moderating effects of temporal and social cues. J. Assoc. Inform. Systems 19(6):503–522.

Huang N, Burtch G, Hong Y, Polman E (2016) Effects of multiple psychological distances on construal and consumer evaluation: A field study of online reviews. J. Consumer Psych. 26(4):474–482.

Jensen ML, Averbeck JM, Zhang Z, Wright KB (2013) Credibility of anonymous online product reviews: A language expectancy perspective. J. Management Inform. Systems 30(1):293–324.

Jeon GY, Kim Y-M, Chen Y (2010) Re-examining price as a predictor of answer quality in an online Q&A site. Proc. SIGCHI Conf. Human Factors Comput. (Association for Computing Machinery, New York), 325–328.

Jones Q, Ravid G, Rafaeli S (2004) Information overload and the message dynamics of online interaction spaces: A theoretical model and empirical exploration. Inform. Systems Res. 15(2):194–210.

Kahn JH, Tobin RM, Massey AE, Anderson JA (2007) Measuring emotional expression with the linguistic inquiry and word count. Amer. J. Psych. 120(2):263–286.

Keller RT (1994) Technology-information processing fit and the performance of R&D project groups: A test of contingency theory. Acad. Management J. 37(1):167–179.

Kennedy P (2008) A Guide to Econometrics, 6th ed. (Wiley-Blackwell, Cambridge, MA)

Kensinger EA, Corkin S (2003) Memory enhancement for emotional words: Are emotional words more vividly remembered than neutral words? Memory Cognition 31(8):1169–1180.

Kim S, Oh S (2009) Users’ relevance criteria for evaluating answers in a social Q&A site. J. Amer. Soc. Inform. Sci. Tech. 60(4):716–727.

Kim H, Rao AR, Lee AY (2009) It’s time to vote: The effect of matching message orientation and temporal frame on political persuasion. J. Consumer Res. 35(6):877–889

Kim S, Oh JS, Oh S (2007) Best-answer selection criteria in a socia Q&A site from the user-oriented relevance perspective. Proc. 70th Annual Meeting Amer. Inform. Sci. Tech. (American Society fo Information Science and Technology, Silver Springs, MD), 1–15.

Kivits J (2006) Informed patients and the internet: A mediated con text for consultations with health professionals. J. Health Psych 11(2):269–282.

Korfiatis N, Garc´ıa-Bariocanal E, Sanchez-Alonso S (2012) Evaluating´ content quality and helpfulness of online product reviews: The interplay of review helpfulness vs. review content. Electronic Commerce Res. Appl. 11(3):205–217.

Krumm J, Davies N, Narayanaswami C (2008) User-generated con tent. IEEE Pervasive Comput. 7(4):10–11.

Larrimore L, Jiang L, Larrimore J, Markowitz D, Gorski S (2011) Peer to peer lending: The relationship between language features, trustworthiness, and persuasion success. J. Appl. Comm. Res. 39(1):19–37.

Lawhon L (2016) New health union survey reveals importance of online health communities. Accessed July 16, 2019, https:/ health-union.com/news/online-health-experience-survey/.

Lee S-Y, Rui H, Whinston AB (2019) Is best answer really the best answer? The politeness bias. MIS Quart. 43(2):579–600.

Li M, Huang L, Tan C-H, Wei K-K (2013) Helpfulness of online product reviews as seen by consumers: Source and content fea tures. Internat. J. Electronic Commerce 17(4):101–136.

Liberman N, Trope Y (1998) The role of feasibility and desirability considerations in near and distant future decisions: A test of temporal construal theory. J. Personality Soc. Psych. 75(1):5–18

Lou J, Fang Y, Lim KH, Peng JZ (2013) Contributing high quantity and quality knowledge to online Q&A communities. J. Amer. Soc. Inform. Sci. Techn. 64(2):356–371

Luo X, Homburg C (2007) Neglected outcomes of customer satis faction. J. Marketing 71(2):133–149.

Maglio SJ, Trope Y, Liberman N (2013) The common currency of psychological distance. Current Directions Psych. Sci. 22(4): 278–282.

McHugh ML (2012) Interrater reliability: The kappa statistic. Bio chemia Medica (Zagreb). 22(3):276–282

McLeod SD (1998) The quality of medical information on the internet: A new public health concern. Arch. Ophthalmology 116(12): 1663–1665.

Miller CH, Lane LT, Deatrick LM, Young AM, Potts KA (2007) Psychological reactance and promotional health messages: The effects of controlling language, lexical concreteness, and the restoration of freedom. Human Comm. Res. 33(2):219–240.

Mudambi SM, Schuff D (2010) What makes a helpful online review? A study of customer reviews on Amazon.com. MIS Quart. 34(1): 185–200.

Murnane K, Phelps MP, Malmberg K (1999) Context-dependent recognition memory: The ice theory. J. Experiment. Psych. Gen eral 128(4):403–415.

Murrow EJ, Oglesby FM (1996) Acute and chronic illness: Similarities, differences and challenges. Orthopaedic Nursing 15(5):47–51.

Oh S, Worrall A (2013) Health answer quality evaluation by librarians, nurses, and users in social Q&A. Library Inform. Sci. Res. 35(4):288–298.

Oh W, Pinsonneault A (2007) On the assessment of the strategic value of information technologies: Conceptual and analytical approaches. MIS Quart. 31(2):239–265.

Oppenheimer DM (2006) Consequences of erudite vernacular utilized irrespective of necessity: Problems with using long words needlessly. Appl. Cognitive Psych. 20(2):139–156.

Oppenheimer DM (2008) The secret life of fluency. Trends Cognitive Sci. 12(6):237–241.

Otterbacher J, Hemphill L, Dekker E (2011) Helpful to you is useful to me: The use and interpretation of social voting. Proc. Amer. Soc. Inform. Sci. Tech. 48(1):1–10.

Parkes M, Jewell DP (2001) The management of severe Crohn’s disease. Alimentary Pharmacology Therapeutics 15(5):563–573.

Pennebaker JW, Francis ME (1996) Cognitive, emotional, and lan guage processes in disclosure. Cognition Emotion 10(6):601–626.

Pennebaker JW, Booth RJ, Francis ME (2007) Linguistic Inquiry and Word Count (Liwc2007) (LIWC, Austin, TX).

Perrin EC, Newacheck P, Pless IB, Drotar D, Gortmaker SL, Leventhal J, Perrin JM, Stein REK, Walker DK, Weitzman M (1993) Issues involved in the definition and classification of chronic health conditions. Pediatrics 91(4):787–793.

Ransbotham S, Lurie NH, Liu H (2019) Creation and consumption of mobile word of mouth: How are mobile reviews different? Marketing Sci. 38(5):733–912.

Reber R, Schwarz N (1999) Effects of perceptual fluency on judg ments of truth. Consciousness Cognition 8(3):338–342.

Reber R, Schwarz N, Winkielman P (2004) Processing fluency and aesthetic pleasure: Is beauty in the perceiver’s processing experience? Personality Soc. Psych. Rev. 8(4):364–382.

Rideout V, Fox S (2018) Digital health practices, social media use, and mental well-being among teens and young adults in the U.S. Accessed July 16, 2019, https://www.hopelab.org/reports/pdf/ a-national-survey-by-hopelab-and-well-being-trust-2018.pdf.

Schweidel DA, Moe WW (2014) Listening in on social media: A joint model of sentiment and venue format choice. J. Marketing Res. 51(4):387–402.

Shah C, Pomerantz J 2010. Evaluating and predicting answer quality in community QA. Proc. 33rd Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (Association for Computing Machen ery, New York), 411–418.

Silberg WM, Lundberg GD, Musacchio RA (1997) Assessing, controlling, and assuring the quality of medical information on the internet: Caveant lector et viewor—Let the reader and viewer beware. JAMA 277(15):1244–1245.

Sosa ML (2009) Application-specific R&D capabilities and the advantage of incumbents: Evidence from the anticancer drug market. Management Sci. 55(8):1409–1422.

Stricker P 2014. Social media: An emerging communication modal ity. Accessed July 16, 2019, http://www.naylornetwork.com cmsatoday/articles/index-v2.asp?aid=296436&issueID=30171.

Tan SS-L, Goonawardene N (2017) Internet health information seeking and the patient-physician relationship: A systematic review. J. Medical Internet Res. 19(1):e9.

Tausczik YR, Pennebaker JW (2010) The psychological meaning of words: LIWC and computerized text analysis methods. J. Lan guage Soc. Psych. 29(1):24–54.

Taylor H (2011) The Growing Influence and Use of Health Care Information Obtained Online (Harris Insights & Analytics, Rochester, NY)

Tilcsik A (2014) Imprint–environment fit and performance: How organizational munificence at the time of hire affects subsequen job performance. Admin. Sci. Quart. 59(4):639–668.

Trope Y, Liberman N (2003) Temporal construal. Psych. Rev. 110(3): 403–421.

Trope Y, Liberman N (2010) Construal-level theory of psychological distance. Psych. Rev. 117(2):440–463.

Trope Y, Liberman N (2011) Construal level theory. Lange PAMV, Kruglanski AW, Higgins ET, eds. Handbook of Theories of Social Psychology (SAGE Publications, Thousand Oaks, CA), 118–134.

Tse C-S, Altarriba J (2009) The word concreteness effect occurs for positive, but not negative, emotion words in immediate serial recall. British J. Psych. 100(1):91–109.

Venkatraman N (1989) The concept of fit in strategy research: Toward verbal and statistical correspondence. Acad. Management Rev. 14(3):423–444.

Wakslak C, Trope Y (2009) The effect of construal level on subjective probability estimates. Psych. Sci. 20(1):52–58.

Weber Shandwick (2018) The great American search for healthcare information. Accessed February 16, 2020, https://www .webershandwick.com/wp-content/uploads/2018/11/Healthcare -Info-Search-Report.pdf

White K, MacDonnell R, Dahl DW (2011) It’s the mind-set that matters: The role of construal level and message framing in influencing consumer efficacy and conservation behaviors. J. Marketing Res. 48(3):472–485.

Willemsen LM, Neijens PC, Bronner F, de Ridder JA (2011) “Highly recommended!” The content characteristics and perceived use fulness of online consumer reviews. J. Comput.-Mediated Comm 17(1):19–38.

Winkielman P, Cacioppo JT (2001) Mind at ease puts a smile on the face: Psychophysiological evidence that processing facilitation elicits positive affect. J. Personality Soc. Psych. 81(6):989–1000.

Winkielman P, Huber DE, Kavanagh L, Schwarz N (2012) Fluency of consistency: When thoughts fit nicely and flow smoothly. Gawronski B, Strack F, eds. Cognitive Consistency: A Fundamental Principle in Social Cognition (Guilford Press, New York), 89–111.

Yin D, Bond SD, Zhang H (2014) Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quart. 38(2):539–560

Yin D, Bond SD, Zhang H (2017) Keep your cool or let it out: Nonlinear effects of expressed arousal on perceptions of consumer reviews. J. Marketing Res. 54(3):447–463.

Yin D, Mitra S, Zhang H (2016) When do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth. Inform. Systems Res. 27(1):131–144.

Zhang Y, Wang P (2016) Interactions and user-perceived helpfulness in diet information social questions & answers. Health Inform. Libraries J. 33(4):295–307.

Zhao M, Xie J (2011) Effects of social and temporal distance on consumers’ responses to peer recommendations. J. Marketing Res. 48(3):486–496.

Zochling J, Grill E, Scheuringer M, Liman W, Stucki G, Braun J (2006) Identification of health problems in patients with acute inflammatory arthritis, using the international classification of functioning, disability and health (ICF). Clinical Experiment. Rheumatology 24(3):239–246.
