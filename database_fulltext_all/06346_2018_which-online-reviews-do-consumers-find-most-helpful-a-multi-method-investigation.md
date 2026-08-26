---
otero_id: 6346
otero_key: "B694HKQ6"
title: "Which online reviews do consumers find most helpful? A multi-method investigation"
authors: "Seyed Pouyan Eslami; Maryam Ghasemaghaei; Khaled Hassanein"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.06.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Which online reviews' do consumers find most helpful?: A multimethod investigation

![](/api/attachments/B694HKQ6/fulltext/images/1260ca90ab6e7212baca6c452b3740762f1ded838f4115f090afb0c2e590e282.jpg)

Seyed Pouyan Eslami, Maryam Ghasemaghaei, Khaled Hassanein

<table><tr><td>PII:</td><td>S0167-9236(18)30109-X</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.06.012</td></tr><tr><td>Reference:</td><td>DECSUP 12970</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>1 March 2018</td></tr><tr><td>Revised date:</td><td>7 June 2018</td></tr><tr><td>Accepted date:</td><td>29 June 2018</td></tr></table>

Please cite this article as: Seyed Pouyan Eslami, Maryam Ghasemaghaei, Khaled Hassanein , Which online reviews' do consumers find most helpful?: A multimethod investigation. Decsup (2018), doi:10.1016/j.dss.2018.06.012

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Which Online Reviews' Do Consumers Find Most Helpful?: A Multimethod Investigation

Seyed Pouyan Eslami eslamisp@mcmaster.ca DeGroote School of Business McMaster University Hamilton, Ontario, Canada

Dr. Maryam Ghasemaghaei

ghasemm@mcmaster.ca

DeGroote School of Business

McMaster University

Hamilton, Ontario, Canada

Dr. Khaled Hassanein

hassank@mcmaster.ca

DeGroote School of Business

McMaster University

Hamilton, Ontario, Canada

Corresponding author:

Dr. Maryam Ghasemaghaei

Phone: (905) 525-9140, ext 21721

Fax: (905) 521-8632

# Which Online Reviews’ Do Consumers Find Most Helpful?: A Multimethod Investigation

## Abstract

While there is some evidence that review length, review score, and argument frame can impact consumers’ perceptions regarding the helpfulness of online consumer reviews, studies have not yet identified the most appropriate levels of such factors in terms of maximizing perceived helpfulness of these reviews. Drawing on Negativity Bias and Cue-Summation theories, we propose a theoretical model that explains online reviews’ helpfulness based on specific characteristics of these reviews (i.e., length, score, argument frame). The model is empirically validated using two datasets of online consumer reviews related to products and services from Amazon.com and Insureye.com respectively. We also employ ANOVA analyses to reveal the levels of each of these characteristics that result in maximizing perceived helpfulness of online consumer reviews. Further, we employ an artificial neural network approach to predict the helpfulness of a given review based on its characteristics. Our findings reveal that the most helpful online consumer reviews are those that are associated with medium length, lower review scores, and negative or neutral argument frame. Our results also reveal that there is no major difference between the characteristics of the most helpful online consumer reviews related to products or services. Finally, our findings reveal that the most helpful factor in predicting the helpfulness of an online consumer review is the review length. Theoretical and practical contributions are outlined.

## Keywords:

Online consumer reviews, artificial neural network, sentiment analysis, review helpfulness, review length, review score

# ACCEPTED MANUSCRIPT

## 1. Introduction

Nowadays many consumers rely on available User-Generated Online Consumer Reviews (UGRs) as one of the most trusted sources of information to evaluate their various purchasing alternatives (Salehan and Kim 2016). As opposed to information provided by businesses or experts that could be either limited or biased, UGRs provide first-hand usage experience information about a particular product provided in these UGRs have the potential to enhance consumers’ ability to evaluate their purchasing alternatives, and to ultimately make wiser purchasing decisions (Chevalier and Mayzlin 2006; Kohli et al. 2004; Zhu and Zhang 2010).

Recent reports have shown that the number of available UGRs grows at an exponential rate (Chaudhari et al. 2013; Singh et al. 2017) recent report by Yelp, its users provide around 24000 new UGRs eve sit hrestha 2016). Although online in having more UGRs to attract more consumers to their websites (Chevalier and Mayzlin 2006; Ghasemaghaei et al. 2016; Srinivasan et al. 2002; Zhu and Zhang 2010), from a consumer perspective, it is hard to go through all the available UGRs before choosing the best purchasing option. In this regards, according to another report by BrightLocal (2016), about 85 percent of consumers read only ten UGRs before making their final purchasing decisions. This could result in their missing out on some potentially more helpful UGRs that appear later in the stack. Thus if more valuable UGRs could be presented earlier, it would improve the overall consumer experience.

As a result, measuring the proper value of an UGR becomes an important task not only for consumers, but also for online consumer review aggregators and online vendors (e.g., Amazon). From a consumers’ perspective it is important to come up with criteria to choose the most valuable UGRs to rely on (Pongpatipat and Liu-Thompkins 2016), and from online consumer review aggregators’ and online vendors’ perspective, it is important to be able to predict and showcase the most valuable UGRs for their customers to save them time and improve their overall satisfaction and loyalty (Minnema et al. 2016).

## ACCEPTED MANUSCRIPT

In measuring the value of a UGR, the most mentioned criteria in the current literature is perceived review helpfulness (Cao et al. 2011; Liu et al. 2008; Salehan and Kim 2016; Yin et al. 2013). Perceived review helpfulness indicates the degree to which an UGR contains an appropriate level of information to be considered as useful by consumers, who are contemplating to purchase the same product or service (Filieri 2015; Qiu et al. 2012). To evaluate the perceived review helpfulness, some information (Ghose and Ipeirotis 2011). It has been shown that numerical information, such as review scores, affects perceived review helpfulness by providing a codified assessment about the quality of a product or a service, whereas textual open-ended information enhances the perceived review helpfulness through offering more tacit knowledge about reviewers’ attitudes regarding their post-purchase usage experiences (Korfiatis et al. 2012). Consumers’ attitude that could be stated through positive, neutral, or negative statements with various degrees of infused emotions (Hu et al. 2014) is often referred to as sentiment polarity or what we call here as argument frame. is study, we extracted the argument frame expressed in each UGR by using a proposed two-stage sentiment analysis procedure.

Among all the factors identified as impacting review helpfulness (Hu et al. 2014; Mudambi and Schuff 2010; Qazi et al. 2016; Salehan and Kim 2016), review length is seen to be the key influencer (Salehan and Kim 2016; Zhang et al. 2014). In this regard, review length can be seen as a proxy to determine the available information in a UGR (Salehan and Kim 2016). Although argument frame and review score can significantly impact review helpfulness, they have not received sufficient attention from the research community.

To the best of our knowledge, to date no study has simultaneously investigated the impact of all the above factors (i.e., review length, argument frame, and review score) on review helpfulness. It is only when studying the impact of these factors together could their relative importance be assessed. Moreover, the mediated impact of review length on review helpfulness through argument frame and review score has not yet been studied. Considering the importance assigned to review length in terms of having a direct effect on review helpfulness, it is also important to understand whether, such effect could also be mediated through the argument frame and score of a review. Therefore, by drawing on Cue-Summation and Negativity Bias Theories, the first objective of this study is to propose a research model to investigate the impact of review length, argument frame, and review score on review helpfulness and the interrelations among these factors.

Moreover, no study to date has deeply investigated the characteristics of the most helpful UGR in and argument frame (i.e., positive, neutral, negative) for both products and services. Therefore, the second objective of this study is to investigate the most appropriate levels of review length, review score, and argument frame in terms of affecting consumers’ perceptions of review helpfulness.

Additionally, to be able to generalize our findings to both product-related and service-related datasets reflecting product-related and service-related UGRs. In so doing, we can understand if there are related UGRs. Furthermore, we can also understand to what extent the recommended levels of the above factors for maximizing review helpfulness vary between product-related and service-related UGRs. To this end, we use two UGR datasets reflecting product-related (1500 UGRs from Amazon.com) and service-related (830 UGRs from Insureye.com).

Furthermore, to date no study has investigated to what extent a UGR’s helpfulness can be predicted based on its characteristics (i.e., review text and score). The main focus of extant literature in this area has been mostly on finding the correlational relationships among the various factors affecting UGR helpfulness. Being able to predict the helpfulness of UGRs could help online aggregators (e.g., TripAdvisor) to serve their customers better by listing UGRs in order of helpfulness. Online vendors could also benefit from identifying the most helpful UGRs to ensure they provide an associated response for each especially in the case of critical UGRs. Therefore, the fourth objective of this study is to investigate to what extent review length, review score, and argument frame can be used to predict review helpfulness for both product and service UGRs.

# ACCEPTED MANUSCRIPT

To fulfill the above objectives, we have used a variety of research methods. The first objective was investigated by using a structural equation modeling technique, to be more precise Partial Least Square (PLS-SEM). Furthermore, the next two objectives were investigated by conducting a series of ANOVA analyses. Finally, an artificial neural network (ANN) approach was employed to address the fourth objective.

## 2. Theoretical background

## 2.1. Review helpfulness

Review helpfulness has been widely used to measure the perceived value of a UGR in enhancing consumers’ ability in evaluating the quality of a product/service (Cao et al. 2011; Liu et al. 2008; Mudambi and Schuff 2010; Salehan and Kim 2016; Yin et al. 2013). A helpful UGR has a potential to offer a greater value to consumers by providing appropriate information regarding the quality of product/service. Particularly, a helpful UGR has been defined as “a peer-generated product evaluation that facilitates the consumer’s purchase decision process” (Mudambi and Schuff 2010).

Current literature identifies various exogenous variables impacting a UGR’s helpfulness. For example, some studies have investigated the impact of review length on review helpfulness (Ghose and studies indicate that as longer UGRs contain more details, consumers find them to be more helpful. Moreover, some studies have investigated the impact of review scores on review helpfulness (Mudambi and Schuff 2010; Salehan and Kim 2016). These numerical reviewer scores, in many instances, are available in a Likert scale format, ranging from one to five, reflecting the positive, neutral, or negative evaluation of previous users of a product/service (Krosnick et al. 1993). The findings of these studies indicate that extreme numerical scores at both ends of the scale are perceived as being more helpful than moderate ones by consumers (Mudambi and Schuff 2010).

Studies have also found that sentiment polarity or what we refer to here as ‘argument frame’ could also impact a UGR’s helpfulness’ perceptions. Argument frame is defined as the consumers’ tone

## ACCEPTED MANUSCRIPT

reflected in the text of a UGR (Hu et al. 2014). These argument frames or polarities reflect the overall consumers’ emotions regarding their usage experiences of a particular product/service (Yin et al. 2013, 2016). Overall, these emotions can be classified into three distinct categories of positive, negative, or neutral. Recent studies indicate that these emotions can be transferred through computer-mediated communications (Harris and Paradice 2007). Thus, readers can detect the emotions of review writers (Salehan and Kim 2016). In regards to non-verbal cues such as emoticons, some recent studies indicate that the emoticons in UGRs sometime are more formative than the actual text in those UGRs as they graphically represent the emotional state of a UGR writer and UGR readers can grasp those emotions more specifically (Heerschop et al. 2011; Hogenboom et al. 2013, 2014; Jiang et al. 2015). These findings are in-line with the main promise of Rhetorical structure theory (RST) (Mann and Thompson 1988). RST focuses on the notion of coherence across a textual document. Relying on this notion, this theory argues that there should be a rhetorical relationship across different text spans (Mann and Thompson 1988). Therefore, according to RST, one can argue that the emotional state of the emoticons can be used as a substitute proxy to the argument frame of a UGR (Hogenboom et al. 2013). Anyhow, people who tend to use UGRs pay attention to the textual content of those UGRs (Salehan and Kim 2016). One of the most important factors influencing consumers’ perceptions regarding a UGR’s helpfulness is its argument frame. Current studies argue that users find negatively-framed UGRs to be more helpful than positivelyframed ones (Yin et al. 2016)

## 2.2. Cue-summation theory

Cue-Summation Theory (Severin 1967) explains how learning occurs through the lens of an individual’s information processing capability. The theory incorporates two main components – Cue and Summation. A cue refers to a snippet of information used by an individual in a learning process; and summation emphasizes the positive effect of employing multiple cues from one or more sources of information in this learning process.

# ACCEPTED MANUSCRIPT

According to this theory, effective learning is positively correlated to the number of cues available to and used by the decision maker. Accordingly, this theory argues that the number of cues (i.e., information snippets) in a given piece of information (e.g., a UGR) can be used as proxy to measure the effectiveness of a piece of information in helping an individual’s learning in a specific context (e.g., making eCommerce decisions) (Jiang and Benbasat 2007). Thus, it could be posited that an individual’s learning outcome is positively dependent on the number of available cues (Dwyer 1978; Miller 1957).

Accordingly, some scholars have used this theory in studying UGRs (Hsieh et al. 2012; Wang et al. 2011; Willemsen et al. 2011). For instance, Willmesen et al. (2011) have shown that UGRs containing a higher diversity of both positive and negative cues are more helpful than other UGRs which contain either one of those types of cues.

## 2.3. Negativity bias theory

Negativity Bias Theory (Kanouse and Hanson Jr 1987) implies that in the course of making decisions, individuals tend to weigh negative cues higher than positive or the neutral ones (Rozin and Royzman 2001; Sen and Lerman 2007). This higher tendency towards using negative cues can be demonstrated in the four distinct ways of higher negative potency, steeper negative gradients, higher potency refers to negative cues having a stronger impact on individuals than positive ones. Steeper negative gradients assert that the negativity of negative events grows faster in space and time than those of positive ones. Higher negativity dominance states that a combination of equally negative and positive cues results in more negative impressions. Finally, various negative differentiation states that negative cues produce more diverse individual responses than positive ones (Rozin and Rozyman 2001). According to negativity bias theory, individuals find negative cues to be more helpful in their decision making process than positive or neutral cues (Herr et al. 1991).

Accordingly, some scholars have used this theory in the context of studying UGRs (Lee and Youn 2009; Sen and Lerman 2007; Zhang et al. 2010). For instance, Zhang et al. (2010) have shown that

UGRs which contain negative cues have higher impact on consumers when considering the purchase of a product/service than those UGRs which contain either positive or neural cues.

## 3. Research model and hypotheses

The research model in Figure 1 is proposed to address the first research objective of this study. It integrates cue-summation and negativity bias theories to explain how review length, review score, and argument frame are associated with a UGR’s helpfulness.

![](/api/attachments/B694HKQ6/fulltext/images/42d34f91b6a6a2ca7950376922d06db89a3ab420235eeaa82499d8f01fd1b46e.jpg)  
Figure 1. Proposed research model

The content of a piece of information can be used as a proxy to evaluate its helpfulness for 2010). Since a UGR is also a source of information, its helpfulness is dependent on the amount of information available in its textual content (Park and Lee 2009b; Racherla and Friske 2012). In this regard, some studies have shown review length to be positively correlated to consumers’ perceived UGR helpfulness (Chevalier and Mayzlin 2006; Mudambi and Schuff 2010; Qazi et al. 2016; Racherla and Friske 2012; Salehan and Kim 2016). An explanation for this is that longer UGRs are likely to contain more cues than shorter ones (Qazi et al. 2016). Thus, it is expected that consumers will perceive longer UGRs as more helpful in making their purchasing decisions compared to shorter ones. Hence, we hypothesize that:

H1: The length of a UGR is positively associated with its perceived helpfulness.

# ACCEPTED MANUSCRIPT

UGRs are usually associated with an open-ended comment section plus an overall review score. While some recent studies have used the unstructured textual data in the comment section to predict review helpfulness (Hu et al. 2014), other studies have utilized the structured numerical information of the review score for this purpose (Mudambi and Schuff 2010). To analyze the textual data of a UGR, Schindler and Bickart (2012) have considered the two factors of content and style. In their work, content refers to the actual information which is available in a UGR, whereas, style refers to the choice of words used by a UGR writer to express her/his usage experience.

In order to analyze the writing style of UGRs, some studies have employed various sentiment analysis techniques to extract the sentiment polarities or argument frames embodied in those UGRs (Bai 2011; Brody and Elhadad 2010; Hu et al. 2014; Jo and Oh 2011; Li and Wu 2010; Maks and Vossen 2012; Salehan and Kim 2016; Ye et al. 2009). A UGR argument frame refers to the extent to which a UGR is positively, neutrally, or negatively framed (Salehan and Kim 2016). In this regard, generally a positively-framed UGR contains positive consumer’s feedback, while a negatively-framed UGR contains negative consumer’s feedback. Furthermore, a UGR with a neutral argument frame encompasses both positive and negative consumer’s feedback.

Extant literature argues that the argument frame of a UGR can be effectively transmitted via computer-mediated communication (Harris and Paradice 2007; Walther and D’Addario 2001) and can affect consumers’ perception regarding its helpfulness (Salehan and Kim 2016). In this regard, it has been found that consumers have considered negatively-framed UGRs to be more helpful compared to positively-framed ones (Hu et al. 2012; Mudambi and Schuff 2010). These findings are also in alignment with the main argument of negativity bias theory, in which people pay more attention to negative cues than positive ones. Hence, we hypothesize that:

H2. The argument frame of a UGR is negatively associated with its perceived helpfulness such that negatively framed UGRs are perceived to be more helpful compared to positively or neutrally framed ones.

# ACCEPTED MANUSCRIPT

Another factor influencing consumers’ perceptions regarding a UGR’s helpfulness is its review score. In general, the review score of a UGR (typically ranging from 1 to 5) reflects the overall assessment of a review writer regarding the quality of a product/service (Mudambi and Schuff 2010). In this regard, lower review scores indicate the negative assessment of a review writer about the quality of a product/service, whereas higher review scores represent their positive assessments of the same. According to negativity bias theory, individuals tend to weigh negative cues higher than positive or neutral ones. This implies that consumers will pay more attention to negative cues (Rozin and Royz 2001). In this regard, Salehan and Kim (2016) have found that consumers perceive UGRs with lower review scores to be more helpful. Hence, we hypothesize that:

H3. The review score of a UGR is negatively associated with its perceived helpfulness.

Negative experiences tend to have a longer impact on individuals than positive ones. Individuals who have had a negative experience generally form more resistant emotional states than those who have had positive ones (Ito et al. 1998). It has been shown that individuals who have had bad experiences tend to use stronger words and voice to describe their feelings (Baumeister et al. 2001). According to the theory of social sharing of emotions (Rimé 2009; Rimé et al. 1998), people who have had bad experiences are more willing to share their thoughts with others by providing longer and more negative comments. Moreover, Korfiatis et al. (2012) have found that review writers who have had negative experiences tend to write longer and more negatively phrased UGRs. Therefore, on the balance of these arguments, we hypothesize that:

H4: The length of a UGR is negatively associated with its argument frame.

A review score reflects a review writer’s product/service overall usage experience, such that a lower score indicates a bad experience, whereas a high review score reflects a good experience (Mudambi and Schuff 2010). As mentioned above, according to the theory of social sharing of emotions, individuals who have had bad experiences are more willing to share their thoughts with others (Rime 2009; Rime et al. 1998). Therefore, such review writers are expected to write longer UGRs. Moreover, Korfiatis et al.

(2012) have found that longer reviews are generally associated with lower review scores. Hence, we hypothesize that:

H5: The length of a UGR is negatively associated with its review score.

According to cognitive consistency theory (Osgood and Tannenbaum 1955), people prefer to have harmony and consistency between their thoughts and actions. This theory asserts that individuals are 1968). According to this theory, any inconsistency among these concepts will create tensions for individuals (Osgood and Tannenbaum 1955). Thus, individuals are motivated to reduce this tension by making coherent decisions over time (Newcomb 1968; Osgood and Tannenbaum 1955). Recent studies have acknowledged such a proposition. For example, Hogenboom et al. (2014) argue that the argument frame of a UGR can be used as a substitute proxy to the review score of the same UGR. Moreover, Ghasemaghaei et al. (2018) , have found that the argument frame of a UGR is the best predictor for the review score of the same UGR. Thus, it is expected that when a consumer is writing a UGR, he/she will provide a review score that is consistent with the argument frame that they have incorporated in that UGR. Hence, we hypothesize that:

H6. The argument frame of a UGR is positively associated with its review score.

## 4. Methodology

## 4.1. Data collection

In this study we obtained the open-ended textual content, review scores, and review helpfulness scores of online consumer reviews. The length of each UGR was calculated, using an R code, by counting the number of words available in its textual content. To analyze the result in a meaningful way, we categorized the UGRs into three different categories of short, medium, and long. To this end, the mean and the standard deviation of UGRs’ lengths’ distribution were calculated. Subsequently, those UGRs which placed one standard deviation bellow or above the mean were considered to be short or long, respectively, while the rest was considered to be of medium length. Finally, argument frame was analyzed based on our proposed sentiment mining algorithm, which is described in the next section.

To be able to generalize our findings to both product-related and service related UGRs, we obtained two different datasets – one from each domain. These datasets were collected from UGRs posted in the past five years that contained scores for UGR helpfulness. For product-related UGRs, we obtained a dataset with 1500 UGRs on digital cameras sold on Amazon.com (He and McAuley 2016; McAuley et al. 2015). For-service-related UGRs, we obtained a dataset with 830 UGRs from the Insureye.com website, a website containing UGRs regarding insurance services. Summary statistics of these datasets are shown in the below tables.

Table 1. Product-related dataset descriptive statistics (n = 1500)

<table><tr><td>Variable</td><td>Mean</td><td>Median</td><td>Standard Deviation</td></tr><tr><td>Length in words</td><td>89.94</td><td>35.00</td><td>153.52</td></tr><tr><td>Length</td><td>1.76</td><td>2.00</td><td>0.54</td></tr><tr><td>Argument Frame</td><td>0.07</td><td>0.00</td><td>0.86</td></tr><tr><td>Review Score</td><td>3.55</td><td>4.00</td><td>1.30</td></tr><tr><td>Review Helpfulness Score</td><td>0.72</td><td>1.00</td><td>0.45</td></tr></table>

Length: 1, 2, or 3, reflecting short, medium, or long UGRs respectively; Argument Frame: -1, 0, or 1: reflecting negatively-framed, neutrally-framed, or positively-framed UGRs respectively; Review Scores: 1, 2, 3, 4 or 5; Review Helpfulness: (0: not Helpful) or (1: Helpful).

Table 2. Service-related dataset descriptive statistics (n = 830)

<table><tr><td>Variable</td><td>Mean</td><td>Median</td><td>Standard Deviation</td></tr><tr><td>Length</td><td>103.64</td><td>64.00</td><td>121.47</td></tr><tr><td>Length</td><td>1.96</td><td>2.00</td><td>0.47</td></tr><tr><td>Argument frame</td><td>0.03</td><td>0.00</td><td>0.89</td></tr><tr><td>Review score</td><td>2.69</td><td>2.00</td><td>1.64</td></tr><tr><td>Review Helpfulness Score</td><td>0.76</td><td>1.00</td><td>0.43</td></tr></table>

Length: 1, 2, or 3, reflecting short, medium, or long UGRs respectively; Argument Frame: -1, 0, or 1: reflecting negatively-framed, neutrally-framed, or positively-framed UGRs respectively; Review Scores: 1, 2, 3, 4 or 5; Review Helpfulness: (0: not Helpful) or (1: Helpful).

## 4.2. Sentiment analysis

Sentiment analysis is a data mining approach used to analyze textual information to extract different types of polarities and emotions that exists in a piece of text. Sentiment analysis is an automated and effective method for information retrieval from unstructured text (Bai 2011; Brody and Elhadad 2010; Hu et al. 2014; Jo and Oh 2011; Li and Wu 2010; Maks and Vossen 2012; Salehan and Kim 2016;

# ACCEPTED MANUSCRIPT

Ye et al. 2009). By utilizing computational linguistics, natural language processing, and text mining techniques (Hogenboom et al. 2014), sentiment analysis transforms unstructured textual data into some predefined categories such as different polarities or emotions. Sentiment analysis has the following three main advantages: (i) gathering people’s opinions that are expressed in an unstructured textual format, (ii) converting a large set of unstructured textual data into some predefined fields, usable by other data mining and statistical analysis approaches, and (iii) aggregating people’s opinions to build predictive models regarding a particular subject (Yu et al. 2013). Although one should acknowledge the limitations of sentiment mining techniques, but reaching an accuracy level of at least 80% has encouraged many researchers to utilize sentiment mining in various fields such as information systems and marketing (Berger et al. 2010; Duan et al. 2008; Ghose and Ipeirotis 2011).

Advancement in machine learning techniques in information retrieval and natural language processing, and availability of unstructured data from various social media networks and consumer reviews’ websites have facilitated the widespread usage of sentiment analysis in identifying affect and emotional states that exists in UGRs (Das and Chen 2007; Yu et al. 2013).

There are different variations of sentiment analysis techniques. Each of these techniques varies on two main dimensions of: (1) the level of text analysis and (2) the algorithms employed for sentiment analysis (Collomb et al. 2014). Sentiment analysis based on the level of text analysis can be categorized into two main categories of document-based and feature-based sentiment analysis (Liu 2010). Documentbased sentiment analysis is used to determine the sentiment polarity of a given text. It has two different levels of analysis - word level and sentence level (Collomb et al. 2014). Featured-based sentiment analysis is generally used to extract the sentiment of a given segment of text towards a special feature of a product/service (Cambria et al. 2013).

Sentiment analysis can also be categorized based on the algorithm used for text analysis. There are three different categories of algorithms used for sentiment analysis: Lexicon based, machine learning, and rule-based (Collomb et al. 2014; Pang and Lee 2008). First, the Lexicon-based approach is suitable for calculating sentiment polarity of a segment of text such as a UGR using sentiment orientations of words or sentences in such a segment (Collomb et al. 2014; Taboada et al. 2008, 2011). In this approach, two different lexicons containing either negative or positive words/sentences are used to determine the sentiment polarity of a given text (Hogenboom et al. 2014); Second, the machine learning sentiment analysis techniques uses deep learning algorithms to determine the sentiment of a given text or classify it based on a given criteria (Pang and Lee 2004). Machine learning techniques are suitable for feature-based sentiment analysis (Go et al. 2009; Pang and Lee 2008). Finally, the rule-based techniques are similar to lexicon based approaches, with the one distinction that the level of textual classification is higher. Rulebased techniques are suitable for extracting different variations of emotions (e.g. joy, sadness, fear and etc.) out of a give text (Gilbert 2014; Heerschop et al. 2011; Hogenboom et al. 2013; Jiang et al. 2015).

Choosing a proper method for sentiment analysis depends on the need of analysis. In this study, we used a document based sentiment analysis method as our interest was to capture the overall sentiment polarity or argument frame in a given UGR. This was accomplished by using the sentiment analysis procedure outlined in Figure 2. Our procedure used an R code that leverages the sentiment library of CRAN<sup>1</sup>. This library has the ability to classify any written document based on its sentiment polarity into 3 different categories of positive, neutral, and negative with 6 different variations of emotions (e.g., anger, happiness, joy, etc.).

To cross validate the obtained results, we also used another sentiment analysis approach using an opinion lexicon (Hu and Liu 2004) as a dictionary to extract different reviews’ polarities of positive, neutral, or negative. In this approach, first we removed the stop words from each UGR. Stop words refer to the most common words of a language that does not have any significant importance, such as “a”, ”an”, ”the”. These words are usually filtered out to reduce the amount of unnecessary information (Rajaraman and Ullman 2011). Then, positive words were assigned a polarity of +1, neutral words were assigned a polarity of 0, and negative words were assigned a polarity of -1. The sentiment polarity of each UGR was then calculated based on the sum of the polarities of the remaining words (i.e., excluding stop words). At the final round of this procedure we compared the results of these two approaches. Our analysis showed a

# ACCEPTED MANUSCRIPT

94% similarity between the findings of these two methods. Thus, we opted to use the sentiments extracted using our first approach as it is sentence-based as opposed to word-based.

Finally, as our final round of cross validation, two of the authors independently read and assigned an argument frame for each UGR in a randomly chosen sample of 300 UGRs. We then computed Cohen’s kappa to assess the agreement between these raters. Our results revealed an inter-rater reliability of 0.89 which was significantly higher than the widely accepted 0.60 threshold (Landis and Koch 1977). We then compared the argument frames generated by our automated method to those generated by one of the coauthors. This comparison shown a 91% accuracy rate for our automated method which is higher than the typical 80% acceptable performance rate commonly reported for sentiment analysis algorithms (Cao et al. 2013; Yu et al. 2013).

Furthermore, after extracting review length, review score, and argument frames of our selected datasets of UGRs, we conducted a series of statistical analysis to satisfy our research objectives. To this end, our first objective was explored using PLS-SEM (Hair et al. 2011). We explored our second and third objectives using ANOVA analyses. Finally, our fourth research objective was addressed using an artificial neural network approach. Figure 2 illustrates our overall research methodology.

## ACCEPTED MANUSCRIPT

![](/api/attachments/B694HKQ6/fulltext/images/089fd414ca7e61342f11619f1b03f289d2a6f5748423b2979ac9d7593d676589.jpg)  
Figure 2. Research methodology

## 5. Data analysis and results

## 5.1. Hypotheses testing

To validate the research model of this study, illustrated in Figure 1, we utilized structural findings to both product-related and service-related UGRs, we ran PLS-SEM on both sets of data (Amazon.com and Insureye.com). We used PLS-SEM for three main reasons. First, unlike any first generation regression tools, PLS-SEM simultaneously assesses all the paths in the research model (Gefen et al. 2000). Second, it does not require any normal multivariate data distributional assumption (Chin 1998; Chin et al. 2003; Gefen et al. 2000). Finally, it minimizes the residual variance of endogenous variables of the research model (Chin 1998; Gefen et al. 2000).

As illustrated in Figures 3 and 4, and Table 3, all of the mentioned hypotheses were supported across both datasets. These findings completely satisfy our first objective and indicates that review length is positively correlated to review helpfulness, whereas, argument frame and review score are negatively correlated to review helpfulness.

![](/api/attachments/B694HKQ6/fulltext/images/1b05417b12245b1764e6a20bd660994932ef5cea27df84264f0ffa8806371637.jpg)  
Figure 3. Product-related dataset PLS-SEM results

![](/api/attachments/B694HKQ6/fulltext/images/2cd80401f851cac6cb43964be372de7ff42ce8c663615ba803059756a31c1e88.jpg)  
Figure 4. Service-related dataset PLS-SEM results

Table 3. Hypothesis testing results

<table><tr><td>Hypothesis</td><td>Hypothesized Relationship</td><td>Product Dataset</td><td>Service Dataset</td></tr><tr><td>H1</td><td>Review Length → Review Helpfulness</td><td>Supported</td><td>Supported</td></tr><tr><td>H2</td><td>Argument Frame → Review Helpfulness</td><td>Supported</td><td>Supported</td></tr><tr><td>H3</td><td>Review Score → Review Helpfulness</td><td>Supported</td><td>Supported</td></tr><tr><td>H4</td><td>Review Length → Argument Frame</td><td>Supported</td><td>Supported</td></tr><tr><td>H5</td><td>Review Length → Review Score</td><td>Supported</td><td>Supported</td></tr><tr><td>H6</td><td>Argument Frame → Review Score</td><td>Supported</td><td>Supported</td></tr></table>

These findings also address the first part of our third objective in which we explore to what extent the effects of review length, argument frame, and review score on review helpfulness are different between product-related and service-related UGRs. To this end, we need to compare the effect sizes of the hypothesized relationships in the two models of Figures 3 and 4. As shown in Figures 3 and 4, the effects of argument frame and review score on review helpfulness are similar across both product-related and service-related UGRs.

## 5.2. Understanding the most appropriate level of review length, review score, and argument frame of a helpful UGR

To address our second and third research objectives, we conducted a series of one-way ANOVA analyses. ANOVA analysis is mainly used to explore and compare the differences among different group means of the same independent variable. Particularly, we conducted a series of one-way ANOVA analyses and used Benferroni multiple comparison analysis, a type of ANOVA that is used when one wants to consider a set of simultaneous statistical inferences about an observed variable (Worsley 1982), to deeply understand how different levels of review length, argument frame, and review scores impact review helpfulness across both of our datasets (i.e., product and service related UGRs).

As shown in Table 4, and Figures 5 and 6, across both datasets longer reviews are generally found to be more helpful by UGR readers which is in line with H1. However as can be seen, interestingly medium length UGRs were found to be significantly more helpful compared to short length or long length ones. Compared to the short length UGRs, consumers find medium length UGRs’ to be significantly more as they provide more information regarding the product/service in question. Moreover, compared to longer UGRs, again medium length UGRs are found to be significantly more helpful. This could be due to the fact that as Information Processing Theory (Miller 1956) argues, people tend to have limited abilities to digest new information. Thus, each person has a limited ability to identify, assimilate, transform, and apply new knowledge (Bettman 1979; Payne and Bettman 2004). As such, although longer UGRs contain more information than medium ones, as people have limited information capacity, it is logical for them to find medium UGRs to be more helpful than longer ones.

![](/api/attachments/B694HKQ6/fulltext/images/0c07fa56334c7329c08a3eed7f1bdc76887aef33ff83197d79a6da21e821d421.jpg)  
Figure 5. Product-related ANOVA on length

![](/api/attachments/B694HKQ6/fulltext/images/334ae1812e424bf9182fc84f3eb137127faa7d615d26227098d78c4e471c9476.jpg)  
Figure 6. Service-related ANOVA on length

Table 4. One-way ANOVA results on review length and review helpfulness

<table><tr><td>Review Length</td><td>Multiple Comparison</td><td>Mean Difference</td><td>Sig.</td></tr><tr><td colspan="4">Product-Related Dataset</td></tr><tr><td rowspan="2">Short Length</td><td>Medium Length</td><td>-0.430*</td><td>0.000</td></tr><tr><td>Long Length</td><td>-0.16*</td><td>0.004</td></tr><tr><td>Medium Length</td><td>Long Length</td><td>0.27*</td><td>0.000</td></tr><tr><td colspan="4">Service-Related Dataset</td></tr><tr><td rowspan="2">Short Length</td><td>Medium Length</td><td>-0.77*</td><td>0.000</td></tr><tr><td>Long Length</td><td>-0.62*</td><td>0.000</td></tr><tr><td>Medium Length</td><td>Long Length</td><td>0.15*</td><td>0.001</td></tr></table>

\*. The mean difference is significant at the 0.05 level.

Further, as can be seen in Table 5, and Figures 7 and 8, in general across both of our datasets, negatively-framed UGRs are significantly more helpful compared to positively-framed UGRs. This could be due to the fact that, as has been stated earlier, according to negative bias theory, in general, people tend to weigh negative cues higher than positive or neutral ones (Rozin and Royzman 2001; Sen and Lerman 2007). Our results also indicate that neutral UGRs are still thought of as being helpful for services but not for products. This could be due to the fact that consumers are able to find a lot of information regarding the positive attributes of a product on their own (e.g., resolution of a particular phone camera) while such information is not readily available for them on services (e.g., food tasting at a particular restaurant). As such, they are more interested in negative UGRs for products or services but they can also benefit from reading neutral UGRs in the case of services containing both negative and positive information.

![](/api/attachments/B694HKQ6/fulltext/images/2397e4a73897d549efcaacfc907fdf3a15c6aba6b1349380a90aa96c161b9703.jpg)  
Figure 7. Product-related ANOVA on argument frame

![](/api/attachments/B694HKQ6/fulltext/images/64d41d9c4d4199664a2c38aba656c740e9aeb4cdd88abd4ae20b30bd4ae552a8.jpg)  
Figure 8. Service-related ANOVA on argument frame

Table 5. One-way ANOVA results on argument frame and review helpfulness

<table><tr><td>Argument Frame</td><td>Multiple Comparison</td><td>Mean Difference</td><td>Sig.</td></tr><tr><td colspan="4">Product-Related Dataset</td></tr><tr><td rowspan="2">Negatively-Framed</td><td>Neutrally-Framed</td><td>0.25*</td><td>0.000</td></tr><tr><td>Positively-Framed</td><td>0.26*</td><td>0.000</td></tr><tr><td>Neutrally-Framed</td><td>Positively-Framed</td><td>0.01</td><td>0.981</td></tr><tr><td colspan="4">Service-Related Dataset</td></tr><tr><td rowspan="2">Negatively-Framed</td><td>Neutrally-Framed</td><td>0.06</td><td>0.481</td></tr><tr><td>Positively-Framed</td><td>0.27*</td><td>0.000</td></tr><tr><td>Neutrally-Framed</td><td>Positively-Framed</td><td>0.22*</td><td>0.000</td></tr></table>

\*. The mean difference is significant at the 0.05 level.

Finally, as illustrated in Table 6, and Figures 9 and 10, in both of our datasets, in general, consumers find UGRs with lower review scores to be more helpful. As explained earlier, this could be due to the fact that individuals generally pay more attention to negative cues which is supported by negativity bias theory (Kanouse and Hanson Jr 1987).

![](/api/attachments/B694HKQ6/fulltext/images/ebd118d1f0e0ea7f9f2b6739267e25a63391e7dff0b9f37278dd70ccf85f85c2.jpg)  
Figure 9. Product-related ANOVA on review score

![](/api/attachments/B694HKQ6/fulltext/images/b4c18abdbf7088431b8d3af7e80a5af96abd1ac3a304159d72f2c5aa767da491.jpg)  
Figure 10. Service-related ANOVA on review score

Table 6. One-Way ANOVA results on review score and review helpfulness

<table><tr><td>Review Score</td><td>Multiple Comparison</td><td>Mean Difference</td><td>Sig.</td></tr><tr><td colspan="4">Product-Related Dataset</td></tr><tr><td rowspan="4">Review score 1</td><td>Review score 2</td><td>0.06</td><td>0.692</td></tr><tr><td>Review score 3</td><td>-0.02</td><td>0.983</td></tr><tr><td>Review score 4</td><td>0.11*</td><td>0.017</td></tr><tr><td>Review score 5</td><td>0.41*</td><td>0.000</td></tr><tr><td rowspan="3">Review score 2</td><td>Review score 3</td><td>-0.09</td><td>0.334</td></tr><tr><td>Review score 4</td><td>0.05</td><td>0.787</td></tr><tr><td>Review score 5</td><td>0.35*</td><td>0.000</td></tr><tr><td rowspan="2">Review score 3</td><td>Review score 4</td><td>0.13*</td><td>0.000</td></tr><tr><td>Review score 5</td><td>0.43*</td><td>0.000</td></tr><tr><td>Review score 4</td><td>Review score 5</td><td>0.30*</td><td>0.000</td></tr><tr><td colspan="4">Service-Related Dataset</td></tr><tr><td>Review score 1</td><td>Review score 2</td><td>0.12</td><td>1.000</td></tr><tr><td></td><td>Review score 3</td><td>0.29*</td><td>0.000</td></tr><tr><td></td><td>Review score 4</td><td>0.34*</td><td>0.000</td></tr><tr><td></td><td>Review score 5</td><td>0.32*</td><td>0.000</td></tr><tr><td>Review score 2</td><td>Review score 3</td><td>0.27*</td><td>0.000</td></tr><tr><td></td><td>Review score 4</td><td>0.33*</td><td>0.000</td></tr><tr><td></td><td>Review score 5</td><td>0.31*</td><td>0.000</td></tr><tr><td>Review score 3</td><td>Review score 4</td><td>0.05</td><td>1.000</td></tr><tr><td></td><td>Review score 5</td><td>0.03</td><td>1.000</td></tr><tr><td>Review score 4</td><td>Review score 5</td><td>-0.02</td><td>1.000</td></tr></table>

\*. The mean difference is significant at the 0.05 level.

## 5.3. Predicting the most helpful UGRs using an artificial neural network approach

So far we have figured out which UGRs are the most helpful to consumers based on the individual UGR characteristics (i.e., review length, review score, and argument frame). To increase the potential practical contributions of our study and to address our fourth research objective, we employed an ANN that considers all three characteristics of a UGR simultaneously to predict its helpfulness. The proposed ANN can be used as a tool to rank a given set of UGRs based on their predicted helpfulness.

ANN is a dynamic system consisting of a series of nodes, artificial neurons, connected by weighted links or synapses. ANNs are able to make linear/non-linear mappings from a set of inputs to desired output/s. Having a non-linear computational power, makes ANNs applicable for use in a variety of problems such as prediction and classification (Basheer and Hajmeer 2000)<sup>2</sup>. Among all different ANN architectures, multilayer perceptron networks is the prominent ANN architecture (Bischof et al. 1992), which has been used in this study.

The first step in employing an ANN is to choose an appropriate ANN architecture by identifying the number of inputs, outputs, number of hidden layers and neurons in each hidden layer. To predict frame of a UGR. Therefore, our input layer consisted of three neurons representing these three UGR characteristics, and the output layer consisted of one neuron representing review helpfulness. The rule of thumb for choosing an appropriate ANN architecture is to keep the architecture as simple as possible (Krimpenis et al. 2006). Therefore, we started with one hidden layer and it proved suffi ient. According to another rule of thumb, the number of neurons in a hidden layer in an ANN with a one hidden layer should be between the number of neurons in the input layer and output layer (Karsoliya 2012). Thus, 1, 2, or 3 neurons could be used in our hidden layer. To select the best ANN architecture, pre ction accuracy rate on the training or a validation set is the best benchmark. Our results showed that the ANN architecture that contains 2 neurons in its hidden layer is the best for our purposes. Two ANNs were trained for predicating UGR helpfulness (one for products and another for services). These ANNs were trained using a training set of 800 products’ UGRs and 440 services’ UGRs. Training was halted when performance ceased to improve on an independent validation sets consisting of 400 UGRs and 220 UGRs for products and services respectively. Finally, the performance of the trained ANNs was tested on a third independent set of data consisting of 300 products’ UGRs and 170 services’ UGRs. Table 7 summarises the performance of the trained ANNs for the training, validation and test sets, respectively. The performance on the independent test sets with accuracy rates above the minimum accepted range of 80% (Ghiasi et al. 2013) demonstrates the ability of our trained ANNs to accurately predict UGR helpfulness based on the three UGR characteristics used.

Table 7. Prediction accuracy levels

<table><tr><td>Prediction Accuracy Rate on Training Set</td><td>Prediction Accuracy Rate on Validation Set</td><td>Prediction Accuracy Rate on Testing Set</td></tr><tr><td colspan="3">Product-Related UGRs</td></tr><tr><td>84.1%</td><td>82.8 %</td><td>80.7 %</td></tr><tr><td colspan="3">Service-Related UGRs</td></tr><tr><td>90.7%</td><td>89.53 %</td><td>84.78 %</td></tr></table>

Using the proposed ANN, Figure 11 illustrates the prediction results in heat map format. Generally for both datasets, the most helpful UGRs are those that are associated with lower review scores, negative or neutral argument frame, and medium length. As shown in Figure 11, the least helpful UGRs are those with short length, high review score, and positively framed. These results are consistent with our initial ANOVA analyses findings.

<table><tr><td></td><td></td><td></td><td colspan="4">Product-Related UGRS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>AF Negative</td><td>AF Neutral</td><td>AF Positive</td><td>AF Negative</td><td>AF Neutral</td><td>AF Positive</td><td>AF Negative</td><td>AF Neutral</td><td>AF Positive</td><td></td><td></td></tr><tr><td>Review Score- 5</td><td></td><td></td><td></td><td></td><td></td><td></td><td>ND</td><td>ND</td><td>ND</td><td></td><td></td></tr><tr><td>Review Score- 4</td><td>ND</td><td>ND</td><td></td><td></td><td></td><td></td><td>ND</td><td></td><td>ND</td><td></td><td></td></tr><tr><td>Review Score- 3</td><td>ND</td><td>ND</td><td></td><td></td><td></td><td></td><td>ND</td><td>ND</td><td>ND</td><td></td><td></td></tr><tr><td>Review Score- 2</td><td>ND</td><td>ND</td><td></td><td></td><td></td><td></td><td></td><td></td><td>ND</td><td></td><td></td></tr><tr><td>Review Score- 1</td><td></td><td>ND</td><td></td><td></td><td></td><td></td><td></td><td></td><td>ND</td><td>Most Helpful</td><td></td></tr><tr><td></td><td>Short Length</td><td>Short Length</td><td>Short Length</td><td>Medium Length</td><td>Medium Length</td><td>Medium Length</td><td>Long Length</td><td>Long Length</td><td>Long Length</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Least Helpful</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td colspan="4">Service-Related UGRS</td><td></td><td></td><td></td><td></td><td>Least Unhelpful</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>AF Negative</td><td>AF Neutral</td><td>AF Positive</td><td>AF Negative</td><td>AF Neutral</td><td>AF Positive</td><td>AF Negative</td><td>AF Neutral</td><td>AF Positive</td><td></td><td></td></tr><tr><td>Review Score- 5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>ND</td><td>ND</td><td></td><td>Most Unhelpful</td></tr><tr><td>Review Score- 4</td><td>ND</td><td></td><td></td><td></td><td></td><td></td><td>ND</td><td>ND</td><td>ND</td><td></td><td></td></tr><tr><td>Review Score- 3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Review Score- 2</td><td></td><td></td><td>ND</td><td></td><td></td><td></td><td></td><td>ND</td><td></td><td></td><td></td></tr><tr><td>Review Score- 1</td><td></td><td>ND</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Short Length</td><td>Short Length</td><td>Short Length</td><td>Medium Length</td><td>Medium Length</td><td>Medium Length</td><td>Long Length</td><td>Long Length</td><td>Long Length</td><td></td><td></td></tr></table>

ND: No Data available in test datasets.

Figure 11. Proposed ANN's prediction results

Finally, we checked the prediction power of our input factors for the trained ANNs. As can be seen in Table 8, among our three input factors, across both datasets, review length is the strongest predictor of review helpfulness. This finding is consistent with our PLS results as well as with the extant literature in this area (Salehan and Kim 2016; Zhang et al. 2014).

Table 8. Prediction power of factors affecting an UGR's helpfulness

<table><tr><td rowspan="2">Predictor</td><td colspan="2">Helpfulness</td></tr><tr><td>Portion</td><td>Rank</td></tr><tr><td colspan="3">Product-Related UGRs</td></tr><tr><td>Review Length</td><td>0.49</td><td>1</td></tr><tr><td>Review Score</td><td>0.32</td><td>2</td></tr><tr><td>Argument Frame</td><td>0.19</td><td>3</td></tr><tr><td colspan="3">Service-Related UGRs</td></tr><tr><td>Review Length</td><td>0.69</td><td>1</td></tr><tr><td>Argument Frame</td><td>0.16</td><td>2</td></tr><tr><td>Review Score</td><td>0.15</td><td>3</td></tr></table>

## 6. Contributions, limitations, and future research

## 6.1. Contributions

This study investigated four main objectives: (1) investigate the impact of review length, argument frame, and review scores on review helpfulness and the interrelations among these factors; (2) investigate the most appropriate level of review length, review score, and argument frame in terms of affecting consumers’ perceptions of the review helpfulness; (3) investigate whether there is any difference in the characteristics of product-related and service-related UGRs; and (4) investigate to what extent review length, review score, and argument frame can predict review helpfulness. Our results have significant theoretical and practical contributions.

From a theoretical perspective, to the best of our knowledge this is the first study to investigate the effects of UGR length, argument frame, and score on review helpfulness and the interrelations among these factors. The results of this study address a gap in the current literature by identifying the characteristics of the most helpful UGRs among both product-related and service-related UGRs. Our PLS, ANOVA and ANN analyses reveal that generally there is consistency between the characteristics of the most helpful UGRs between product-related and service-related UGRs. Particularly, we find that the most helpful UGRs are those associated with lower review scores, negative or neutral argument frame, and medium length. Our results also reveal that, generally, longer UGRs are more helpful than shorter ones as potentially they contain more cues. Our multimethod investigation lends further credibility to our findings. Further, to the best of our knowledge, this study is the first to use artificial neural networks to predict the most helpful UGRs.

The results of this study also make some important practical contributions. Consumers can use the findings of this study to select the most appropriate UGRs to focus on before making their purchasing decisions (i.e., UGRs with lower scores, negative or neutral argument frame and medium length). Moreover, this study has some practical applicability for online consumer review aggregators and online vendors. Online consumer review aggregators (e.g., TripAdvisor) can use the propose ANN approach of this study to identify and rank the most helpful UGRs to highlight for their users Although, one might argue that consumers for some services such as hotels are looking for the most recent UGRs, for many other products or services, such as cameras or insurance services, the quality of a product/service will remain the same over the foreseeable time. Identifying the most helpful UGR, among a set of available UGRs, could potentially increase consumers’ trust in a review aggregator. Further, online vendors can use the proposed ANN approach to identify the most importa UGRs that require quick responses. Providing quick responses can reduce the damaging effects of negative UGRs that are highly read due to being deemed most helpful by potential customers. Moreover, this study shows an easy and a practical way of deploying sentiment analysis techniques for both online consumer review aggregators and online vendors. Both of these two groups, using sentiment analysis techniques, can easily identify their consumers attitude towards their products/services and enhance their brand perceptions among their own consumers by addressing the issues that matters to their consumers the most.

## 6.2. Limitations and future research

As with any other research, this study has some limitations. First, we mainly focused on high involvement products (i.e., digital cameras and insurance services), which require more thorough information processing. Future studies can use other sources of online consumer review data representing different industries or product types to assess the generalizability of our findings. The second limitation of this study exists in the capabilities of sentiment analysis. Although sentiment analysis techniques have been greatly improved to deal with different types of writing styles, the library we used for sentiment

## ACCEPTED MANUSCRIPT

analysis still had limitations in dealing with sarcastic writing. Another limitation of our employed sentiment analysis technique was in detecting the emoticons that could have probably existed in the selected UGRs. As stated earlier, current literature argues that emoticons in the textual document of UGRs can be seen as the substitute proxy for the argument frame of those UGRs. Some recent studies have tried to bridge this gap by adding the various emoticons into their lexicons. Thus, future studies in this area should utilize a more comprehensive library that incorporate different styles of writing and emoticons. The next potential limitation for this study could be in identifying fake UGRs. Although we have tried to make sure that the platforms we used contain only user generated online consumer reviews, it is still hard to ensure that our final datasets did not contain any fake UGRs. This is a general limitation with UGRs as opposed to being a specific limitation associated with this study. Finally, another potential limitation of this study exists in categorizing argument frames into three distinct categories of positive, negative, or neutral. A neutral argument in this study was one that contained a balance of both positive and negative argument frames. Another view, however, would define a neutral argument of being devoid of any positive or negative argument frames. A new class could be defined as a “mixed argument” UGR to capture the cases that incorporate a mix of negative and positive argument frames. Therefore, it would be interesting if future studies would explore the use of such a category in addition to the three we used.

## 7. Conclusion

The number of available UGRs is growing at an exponential rate. Based on the current literature, the best criterion for selecting a UGR to read is its perceived review helpfulness. Given the number of UGRs available on many websites, it is really hard for consumers, online UGR aggregators, or online vendors to go through all of them to find the most helpful ones to consumers in a timely manner. By illustrating the most important factors that affect perceived review helpfulness, this study provides novel insights to the current literature in this area. Further, our multimethod approach revealed the most appropriate levels of these factors to maximize perceived UGR helpfulness. The ANN approach introduced in this paper for predicting the helpfulness of a given UGR based on its characteristics is both novel and useful.

## References

Amblee, N., and Bui, T. 2007. “Freeware Downloads: An Empirical Investigation into the Impact of Expert and User Reviews on Demand for Digital Goods,” AMCIS 2007 Proceedings, p. 21.

Bai, X. 2011. “Predicting Consumer Sentiments from Online Text,” Decision Support Systems (50:4), pp. 732–742.

Basheer, I. A., and Hajmeer, M. 2000. “Artificial Neural Networks: Fundamentals, Computing, Design, and Application,” Journal of Microbiological Methods (43:1), pp. 3–31.

Baumeister, R. F., Bratslavsky, E., Finkenauer, C., and Vohs, K. D. 2001. “Bad Is Stronger than Good.,” Review of General Psychology (5:4), p. 323.

Berger, J., Sorensen, A. T., and Rasmussen, S. J. 2010. “Positive Effects of Negative Publicity: When Negative Reviews Increase Sales,” Marketing Science (29:5), pp. 815–827.

Bettman, J. R. 1979. “Memory Factors in Consumer Choice: A Review,” The Journal of Marketing, pp. 37–53.

Bischof, H., Schneider, W., and Pinz, A. J. 1992. “Multispectral Classification of Landsat-Images Using Neural Networks,” IEEE Transactions on Geoscience and Remote Sensing (30:3), pp. 482–490.

BrightLocal. 2016. “BrightLocal.” (https://www.brightlocal.com/learn/local-consumer-review-survey-2016/, accessed January 1, 2018).

Brody, S., and Elhadad, N. 2010. “An Unsupervised Aspect-Sentiment Model for Online Reviews,” in Human Language Technologies: The 2010 Annual Conference of the North American Chapter of the Association for Computational Linguistics, Association for Computational Linguistics, pp. 804–812.

Cambria, E., Schuller, B., Xia, Y., and Havasi, C. 2013. “New Avenues in Opinion Mining and Sentiment Analysis,” IEEE Intelligent Systems (28:2), pp. 15–21.

Cao, J., Wu, Z., Wang, Y., and Zhuang, Y. 2013. “Hybrid Collaborative Filtering Algorithm for Bidirectional Web Service Recommendation,” Knowledge and Information Systems (36:3), pp. 607–627.

Cao, Q., Duan, W., and Gan, Q. 2011. “Exploring Determinants of Voting for the ‘Helpfulness’ of Online User Reviews: A Text Mining Approach,” Decision Support Systems (50:2), pp. 511–521.

Chaudhari, D. D., Deshmukh, R. A., Bagwan, A. B., and Deshmukh, P. K. 2013. “Feature Based Approach for Review Mining Using Appraisal Words,” in Emerging Trends in Communication, Control, Signal Processing & Computing Applications (C2SPCA), 2013 International Conference On, IEEE, pp. 1–5.

Chevalier, J. A., and Mayzlin, D. 2006. “The Effect of Word of Mouth on Sales: Online Book Reviews,” Journal of Marketing Research (43:3), pp. 345–354.

Chin, W. W. 1998. “The Partial Least Squares Approach to Structural Equation Modeling,” Modern Methods for Business Research (295:2), pp. 295–336.

Chin, W. W., Marcolin, B. L., and Newsted, P. R. 2003. “A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study,” Information Systems Research (14:2), pp. 189–217.

Coakes, S. J., and Steed, L. 2009. SPSS: Analysis without Anguish Using SPSS Version 14.0 for Windows, John Wiley & Sons, Inc.

Collomb, A., Costea, C., Joyeux, D., Hasan, O., and Brunie, L. 2014. “A Study and Comparison of Sentiment Analysis Methods for Reputation Evaluation,” Rapport de Recherche RR-LIRIS-2014- 002.

Das, S. R., and Chen, M. Y. 2007. “Yahoo! For Amazon: Sentiment Extraction from Small Talk on the Web,” Management Science (53:9), pp. 1375–1388.

Duan, W., Gu, B., and Whinston, A. B. 2008. “Do Online Reviews Matter?—An Empirical Investigation of Panel Data,” Decision Support Systems (45:4), pp. 1007–1016.

Dwyer, F. M. 1978. Strategies for Improving Visual Learning: Instructor’s Manual, Learning Services.

Eastin, M. S. 2001. “Credibility Assessments of Online Health Information: The Effects of Source Expertise and Knowledge of Content,” Journal of Computer Mediated Communication (6:4), pp. 0–0.

Filieri, R. 2015. “What Makes Online Reviews Helpful? A Diagnosticity-Adoption Framework to Explain Informational and Normative Influences in e-WOM,” Journal of Business Research (68:6), pp. 1261–1270.

Gefen, D., Straub, D., and Boudreau, M.-C. 2000. “Structural Equation Modeling and Regression: Guidelines for Research Practice,” Communications of the Association for Information Systems (4:1), p. 7.

Ghasemaghaei, M., Eslami, S. P., Deal, K., and Hassanein, K. 2016. Consumers’ Attitude toward Insurance Companies: A Sentiment Analysis of Online Consumer Reviews.

Ghasemaghaei, M., Eslami, S. P., Deal, K., and Hassanein, K. 2018. “Reviews’ Length and Sentiment as Correlates of Online Reviews’ Ratings,” Internet Research (just-accepted), pp. 00–00.

Ghiasi, M. M., Bahadori, A., Zendehboudi, S., Jamili, A., and Rezaei-Gomari, S. 2013. “Novel Methods Predict Equilibrium Vapor Methanol Content during Gas Hydrate Inhibition,” Journal of Natural Gas Science and Engineering (15), pp. 69–75.

Ghose, A., and Ipeirotis, P. G. 2011. “Estimating the Helpfulness and Economic Impact of Product Reviews: Mining Text and Reviewer Characteristics,” IEEE Transactions on Knowledge and Data Engineering (23:10), pp. 1498–1512.

Gilbert, C. H. E. 2014. “Vader: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text,” in Eighth International Conference on Weblogs and Social Media (ICWSM-14). Available at (20/04/16) Http://Comp. Social. Gatech. Edu/Papers/Icwsm14. Vader. Hutto. Pdf.

Go, A., Bhayani, R., and Huang, L. 2009. “Twitter Sentiment Classification Using Distant Supervision,” CS224N Project Report, Stanford (1:12).

Gueorguieva, R., and Krystal, J. H. 2004. “Move over Anova: Progress in Analyzing Repeated-Measures Data Andits Reflection in Papers Published in the Archives of General Psychiatry,” Archives of General Psychiatry (61:3), pp. 310–317.

Hair, J. F., Ringle, C. M., and Sarstedt, M. 2011. “PLS-SEM: Indeed a Silver Bullet,” Journal of Marketing Theory and Practice (19:2), pp. 139–152.

Harris, R. B., and Paradice, D. 2007. “An Investigation of the Computer-Mediated Communication of Emotions,” Journal of Applied Sciences Research (3:12), pp. 2081–2090.

He, R., and McAuley, J. 2016. “VBPR: Visual Bayesian Personalized Ranking from Implicit Feedback.,” in AAAI, pp. 144–150.

Heerschop, B., Goossen, F., Hogenboom, A., Frasincar, F., Kaymak, U., and de Jong, F. 2011. “Polarity Analysis of Texts Using Discourse Structure,” in Proceedings of the 20th ACM International Conference on Information and Knowledge Management, ACM, pp. 1061–1070.

Herr, P. M., Kardes, F. R., and Kim, J. 1991. “Effects of Word-of-Mouth and Product-Attribute Information on Persuasion: An Accessibility-Diagnosticity Perspective,” Journal of Consumer Research (17:4), pp. 454–462.

Hoaglin, D. C., and Welsch, R. E. 1978. “The Hat Matrix in Regression and ANOVA,” The American Statistician (32:1), pp. 17–22.

Hogenboom, A., Bal, D., Frasincar, F., Bal, M., de Jong, F., and Kaymak, U. 2013. “Exploiting Emoticons in Sentiment Analysis,” in Proceedings of the 28th Annual ACM Symposium on Applied Computing, ACM, pp. 703–710.

Hogenboom, A., Heerschop, B., Frasincar, F., Kaymak, U., and de Jong, F. 2014. “Multi-Lingual Support for Lexicon-Based Sentiment Analysis Guided by Semantics,” Decision Support Systems (62), pp. 43–53.

Hsieh, J.-K., Hsieh, Y.-C., and Tang, Y.-C. 2012. “Exploring the Disseminating Behaviors of EWOM Marketing: Persuasion in Online Video,” Electronic Commerce Research (12:2), pp. 201–224.

Hu, M., and Liu, B. 2004. “Mining and Summarizing Customer Reviews,” in Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, pp. 168–177.

Hu, N., Bose, I., Koh, N. S., and Liu, L. 2012. “Manipulation of Online Reviews: An Analysis of Ratings, Readability, and Sentiments,” Decision Support Systems (52:3), pp. 674–684.

Hu, N., Koh, N. S., and Reddy, S. K. 2014. “Ratings Lead You to the Product, Reviews Help You Clinch It? The Mediating Role of Online Review Sentiments on Product Sales,” Decision Support Systems (57), pp. 42–53.

Ito, T. A., Larsen, J. T., Smith, N. K., and Cacioppo, J. T. 1998. “Negative Information Weighs More Heavily on the Brain: The Negativity Bias in Evaluative Categorizations.,” Journal of Personality and Social Psychology (75:4), p. 887.

Jiang, F., Liu, Y.-Q., Luan, H.-B., Sun, J.-S., Zhu, X., Zhang, M., and Ma, S.-P. 2015. “Microblog Sentiment Analysis with Emoticon Space Model,” Journal of Computer Science and Technology (30:5), pp. 1120–1129.

Jiang, Z., and Benbasat, I. 2007. “The Effects of Presentation Formats and Task Complexity on Online Consumers’ Product Understanding,” Mis Quarterly, pp. 475–500.

Jo, Y., and Oh, A. H. 2011. “Aspect and Sentiment Unification Model for Online Review Analysis,” in Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, ACM, pp. 815–824.

Kanouse, D. E., and Hanson Jr, L. R. 1987. “Negativity in Evaluations.,” in Preparation of This Paper Grew out of a Workshop on Attribution Theory Held at University of California, Los Angeles, Aug 1969., Lawrence Erlbaum Associates, Inc.

Karsoliya, S. 2012. “Approximating Number of Hidden Layer Neurons in Multiple Hidden Layer BPNN Architecture,” International Journal of Engineering Trends and Technology (3:6), pp. 714–717.

Kim, J.-O., and Kohout, F. J. 1975. “Analysis of Variance and Covariance: Subprograms ANOVA and ONEWAY,” Statistical Package for the Social Sciences (2), pp. 398–433.

Kim, M., Kim, J.-H., and Lennon, S. J. 2006. “Online Service Attributes Available on Apparel Retail Web Sites: An ES-QUAL Approach,” Managing Service Quality: An International Journal (16:1), pp. 51–77.

Kim, S.-M., and Hovy, E. 2006. “Automatic Identification of pro and Con Reasons in Online Reviews,” in Proceedings of the COLING/ACL on Main Conference Poster Sessions, Association for Computational Linguistics, pp. 483–490.

Kohli, R., Devaraj, S., and Mahmood, M. A. 2004. “Understanding Determinants of Online Consumer Satisfaction: A Decision Process Perspective,” Journal of Management Information Systems (21:1), pp. 115–136.

Korfiatis, N., GarcíA-Bariocanal, E., and SáNchez-Alonso, S. 2012. “Evaluating Content Quality and Helpfulness of Online Product Reviews: The Interplay of Review Helpfulness vs. Review Content,” Electronic Commerce Research and Applications (11:3), pp. 205–217.

Krimpenis, A., Benardos, P. G., Vosniakos, G.-C., and Koukouvitaki, A. 2006. “Simulation-Based Selection of Optimum Pressure Die-Casting Process Parameters Using Neural Nets and Genetic Algorithms,” The International Journal of Advanced Manufacturing Technology (27:5–6), pp. 509–517.

Krosnick, J. A., Boninger, D. S., Chuang, Y. C., Berent, M. K., and Carnot, C. G. 1993. “Attitude Strength: One Construct or Many Related Constructs?,” Journal of Personality and Social Psychology (65:6), p. 1132.

Landis, J. R., and Koch, G. G. 1977. “An Application of Hierarchical Kappa-Type Statistics in the Assessment of Majority Agreement among Multiple Observers,” Biometrics, pp. 363–374.

Lee, M., and Youn, S. 2009. “Electronic Word of Mouth (EWOM) How EWOM Platforms Influence Consumer Product Judgement,” International Journal of Advertising (28:3), pp. 473–499.

Li, N., and Wu, D. D. 2010. “Using Text Mining and Sentiment Analysis for Online Forums Hotspot Detection and Forecast,” Decision Support Systems (48:2), pp. 354–368.

## ACCEPTED MANUSCRIPT

Liu, B. 2010. “Sentiment Analysis and Subjectivity.,” Handbook of Natural Language Processing (2), pp. 627–666.

Liu, X., He, M., Gao, F., and Xie, P. 2008. “An Empirical Study of Online Shopping Customer Satisfaction in China: A Holistic Perspective,” International Journal of Retail & Distribution Management (36:11), pp. 919–940.

Maks, I., and Vossen, P. 2012. “A Lexicon Model for Deep Sentiment Analysis and Opinion Mining Applications,” Decision Support Systems (53:4), pp. 680–688.

Mann, W. C., and Thompson, S. A. 1988. “Rhetorical Structure Theory: Toward a Functional Theory of Text Organization,” Text-Interdisciplinary Journal for the Study of Discourse (8:3), pp. 243–281.

McAuley, J., Pandey, R., and Leskovec, J. 2015. “Inferring Networks of Substitutable and Complementary Products,” in Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, pp. 785–794.

Miller, G. A. 1956. “The Magical Number Seven, plus or Minus Two: Some Limits on Our Capacity for Processing Information.,” Psychological Review (63:2), p. 81.

Miller, N. E. 1957. “Graphic Communication and the Crisis in Education,” Audio Visual Communication Review, pp. 1–120.

Minnema, A., Bijmolt, T. H., Gensler, S., and Wiesel, T. 2016. “To Keep or Not to Keep: Effects of Online Customer Reviews on Product Returns,” Journal of Retailing (92:3), pp. 253–267.

Mudambi, S. M., and Schuff, D. 2010. What Makes a Helpful Review? A Study of Customer Reviews on Amazon. Com.

Newcomb, T. M. 1968. “Interpersonal Balance,” Theories of Cognitive Consistency: A Sourcebook, pp. 28–51.

Osgood, C. E., and Tannenbaum, P. H. 1955. “The Principle of Congruity in the Prediction of Attitude Change.,” Psychological Review (62:1), p. 42.

Pang, B., and Lee, L. 2004. “A Sentimental Education: Sentiment Analysis Using Subjectivity Summarization Based on Minimum Cuts,” in Proceedings of the 42nd Annual Meeting on Association for Computational Linguistics, Association for Computational Linguistics, p. 271.

Pang, B., and Lee, L. 2008. “Opinion Mining and Sentiment Analysis,” Foundations and Trends® in Information Retrieval (2:1–2), pp. 1–135.

Park, C., and Lee, T. M. 2009a. “Antecedents of Online Reviews’ Usage and Purchase Influence: An Empirical Comparison of US and Korean Consumers,” Journal of Interactive Marketing (23:4), pp. 332–340.

Park, C., and Lee, T. M. 2009b. “Information Direction, Website Reputation and EWOM Effect: A Moderating Role of Product Type,” Journal of Business Research (62:1), pp. 61–67.

Payne, J. W., and Bettman, J. R. 2004. “Walking with the Scarecrow: The Information-Processing Approach to Decision Research,” Blackwell Handbook of Judgment and Decision Making, pp. 110–132.

Pongpatipat, C., and Liu-Thompkins, Y. 2016. “Beyond Information: How Consumers Use Online Reviews to Manage Social Impressions,” in Let’s Get Engaged! Crossing the Threshold of Marketing’s Engagement Era, Springer, pp. 103–104.

Qazi, A., Syed, K. B. S., Raj, R. G., Cambria, E., Tahir, M., and Alghazzawi, D. 2016. “A Concept-Level Approach to the Analysis of Online Review Helpfulness,” Computers in Human Behavior (58), pp. 75–81.

Qiu, L., Pang, J., and Lim, K. H. 2012. “Effects of Conflicting Aggregated Rating on EWOM Review Credibility and Diagnosticity: The Moderating Role of Review Valence,” Decision Support Systems (54:1), pp. 631–643.

Racherla, P., and Friske, W. 2012. “Perceived ‘Usefulness’ of Online Consumer Reviews: An Exploratory Investigation across Three Services Categories,” Electronic Commerce Research and Applications (11:6), pp. 548–559.

Rajaraman, A., and Ullman, J. D. 2011. “Recommendation Systems,” Mining of Massive Datasets, pp. 307–341.

## ACCEPTED MANUSCRIPT

Reinhard, M.-A., and Sporer, S. L. 2010. “Content versus Source Cue Information as a Basis for Credibility Judgments,” Social Psychology.

Rimé, B. 2009. “Emotion Elicits the Social Sharing of Emotion: Theory and Empirical Review,” Emotion Review (1:1), pp. 60–85.

Rimé, B., Finkenauer, C., Luminet, O., Zech, E., and Philippot, P. 1998. “Social Sharing of Emotion: New Evidence and New Questions,” European Review of Social Psychology (9:1), pp. 145–189.

Rozin, P., and Royzman, E. B. 2001. “Negativity Bias, Negativity Dominance, and Contagion,” Personality and Social Psychology Review (5:4), pp. 296–320.

Salehan, M., and Kim, D. J. 2016. “Predicting the Performance of Online Consumer Reviews: A Sentiment Mining Approach to Big Data Analytics,” Decision Support Systems (81), pp. 30–40.

Schindler, R. M., and Bickart, B. 2012. “Perceived Helpfulness of Online Consumer Reviews: The Role of Message Content and Style,” Journal of Consumer Behaviour (11:3), pp. 234–243.

Sen, S., and Lerman, D. 2007. “Why Are You Telling Me This? An Examination into Negative Consumer Reviews on the Web,” Journal of Interactive Marketing (21:4), pp. 76–94.

Severin, W. 1967. “Another Look at Cue Summation,” AV Communication Review (15:3), pp. 233–245.

Shrestha , K. 2016. “50 Important Online Reviews Stats You Need to Know [Infographic].” 2016. Vendasta Blog, , August 29. (https://www.vendasta.com/blog/50-stats-you-need-to-know-aboutonline-reviews, accessed February 24, 2018).

Singh, J. P., Irani, S., Rana, N. P., Dwivedi, Y. K., Saumya, S., and Roy, P. K. 2017. “Predicting the ‘Helpfulness’ of Online Consumer Reviews,” Journal of Business Research (70), pp. 346–355.

Sokalr, R. R., and Rohlf, F. J. B. 1981. The Principles and Practice of Statistics in Biological Research, Freeman, WH.

Srinivasan, S. S., Anderson, R., and Ponnavolu, K. 2002. “Customer Loyalty in E-Commerce: An Exploration of Its Antecedents and Consequences,” Journal of Retailing (78:1), pp. 41–50.

Taboada, M., Brooke, J., Tofiloski, M., Voll, K., and Stede, M. 2011. “Lexicon-Based Methods for Sentiment Analysis,” Computational Linguistics (37:2), pp. 267–307.

Taboada, M., Voll, K., and Brooke, J. 2008. “Extracting Sentiment as a Function of Discourse Structure and Topicality,” Simon Fraser Univeristy School of Computing Science Technical Report.

Vasey, M. W., and Thayer, J. F. 1987. “The Continuing Problem of False Positives in Repeated Measures ANOVA in Psychophysiology: A Multivariate Solution,” Psychophysiology (24:4), pp. 479–486.

Walther, J. B., and D’Addario, K. P. 2001. “The Impacts of Emoticons on Message Interpretation in Computer-Mediated Communication,” Social Science Computer Review (19:3), pp. 324–347.

Wang, G., Liu, X., and Fan, W. 2011. A Knowledge Adoption Model Based Framework for Finding Helpful User-Generated Contents in Online Communities.

Willemsen, L. M., Neijens, P. C., Bronner, F., and De Ridder, J. A. 2011. “‘Highly Recommended!’ The Content Characteristics and Perceived Usefulness of Online Consumer Reviews,” Journal of Computer Mediated Communication (17:1), pp. 19–38.

Worsley, K. J. 1982. “An Improved Bonferroni Inequality and Applications,” Biometrika (69:2), pp. 297– 302.

Ye, Q., Law, R., and Gu, B. 2009. “The Impact of Online User Reviews on Hotel Room Sales,” International Journal of Hospitality Management (28:1), pp. 180–182.

Yin, D., Bond, S., and Zhang, H. 2013. Anxious or Angry? Effects of Discrete Emotions on the Perceived Helpfulness of Online Reviews.

Yin, D., Mitra, S., and Zhang, H. 2016. “Research Note—When Do Consumers Value Positive vs. Negative Reviews? An Empirical Investigation of Confirmation Bias in Online Word of Mouth,” Information Systems Research (27:1), pp. 131–144.

Yu, Y., Duan, W., and Cao, Q. 2013. “The Impact of Social and Conventional Media on Firm Equity Value: A Sentiment Analysis Approach,” Decision Support Systems (55:4), pp. 919–926.

Zhang, K. Z., Zhao, S. J., Cheung, C. M., and Lee, M. K. 2014. “Examining the Influence of Online Reviews on Consumers’ Decision-Making: A Heuristic–systematic Model,” Decision Support Systems (67), pp. 78–89.

Zhang, Z., Ye, Q., Law, R., and Li, Y. 2010. “The Impact of E-Word-of-Mouth on the Online Popularity of Restaurants: A Comparison of Consumer Reviews and Editor Reviews,” International Journal of Hospitality Management (29:4), pp. 694–700.

Zhu, F., and Zhang, X. 2010. “Impact of Online Consumer Reviews on Sales: The Moderating Role of Product and Consumer Characteristics,” Journal of Marketing (74:2), pp. 133–148.

# ACCEPTED MANUSCRIPT

## Author Biography

Seyed Pouyan Eslami is a Ph.D. candidate at the DeGroote School of Business, McMaster University. His research focuses on text analytics, social media analytics, and data analytics use in organizations. His most recent activities have resulted in 6 peer-reviewed articles in academic journals, and conference proceedings. His most recent article have published in Internet Research.

Maryam Ghasemaghaei is an Assistant Professor of Information Systems at DeGroote School of Business at McMaster University. Her research interests relate to technology adoption, and the use of data analytics in organizations. Her research activities have resulted in over 20 peer reviewed articles in academic journals, and conference proceedings such as MIS Quarterly, Information & Management, Decision Support Systems, Journal of Strategic Information Systems, Computers in Human Behavior, Journal of Computer Science, and Journal of Retailing and Consumer Services.

Khaled Hassanein is a Professor of Information Systems, Associate Dean (Graduate Studies & Research), and Director of the McMaster Digital Transformation Research Centre at the DeGroote School of Business, McMaster University. His main research interests lie in the areas of technology adoption, decision support systems including data analytics, and Neuro-Information Systems. His research activities have resulted in over 100 peer-reviewed articles in academic journals, and leading conference proceedings. He is a senior editor, associate editor or editorial board member with several Information Systems' journals. He is a joint holder of several U.S. patents, a senior member of the IEEE and a designated Professional Engineer in Ontario.

## Highlights

 Multimethod have been used including sentiment analysis, PLS-SEM, ANOVA, and ANN

 Helpful reviews have medium length, lower scores, and negative argument frame

 There is no difference between the most helpful reviews for products or services

 Most helpful factor in predicting the helpfulness of a consumer review is length
