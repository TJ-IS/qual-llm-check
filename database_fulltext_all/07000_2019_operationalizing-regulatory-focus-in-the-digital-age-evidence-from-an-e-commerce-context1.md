---
otero_id: 7000
otero_key: "TMYVF8QN"
title: "Operationalizing Regulatory Focus in the Digital Age: Evidence from an E-Commerce Context1"
authors: "Ji Wu; Liqiang Huang; J. Leon Zhao"
year: "2019"
journal: "MIS Quarterly"
doi: "10.25300/misq/2019/14420"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# OPERATIONALIZING REGULATORY FOCUS IN THE DIGITAL AGE: EVIDENCE FROM AN E-COMMERCE CONTEXT<sup>1</sup>

Ji Wu Business School, Sun Yat-sen University, Guangzhou, CHINA {wugide@gmail.com}

Liqiang Huang School of Management, Zhejiang University, Hangzhou, CHINA {huanglq@zju.edu.cn}

J. Leon Zhao College of Business, City University of Hong Kong, Hong Kong, CHINA {jlzhao@cityu.edu.hk}

Regulatory focus theory (RFT) has been regarded as an important theory for understanding customer behavior in e-commerce; however, there is a significant gap between theoretical analysis with RFT and its practical applications. In particular, there is little research on how to identify the chronic regulatory focus of customers; as such, it is difficult to apply RFT in e-commerce operations. To fill this research gap, we propose an innovative method to operationalize customer regulatory focus from the affective dimension, leading to operationalized regulatory focus (ORF). In this regard, our study spearheads a new avenue of research on how social theories can be operationalized and applied in e-commerce operations. We first identify customers’ chronic regulatory focus (i.e., promotion focus or prevention focus) based on online review data using text mining, leading to an innovative method we refer to as “regulatory focus discovery.” Then, we validate the computed results on regulatory focus by surveying corresponding customers included in the same dataset. Finally, we evaluate the applicability of ORF via an econometric analysis. In this article, we demonstrate that it is possible to compute regulatory focus of specific customers for the purpose of assessing their purchasing tendency. The theoretical and practical implications of ORF are discussed.

Keywords: Regulatory focus theory, operationalization, regulatory focus discovery, design science; electronic commerce, sentiment analysis

## Introduction

Regulatory focus theory (RFT) was developed to explain the relationship between people’s regulatory focus (RF) and the way in which they go about achieving their goals. The central thesis of the theory is that RF (promotion focus versus prevention focus) influences individual behavior in such areas as information selection, information processing, product choice, and emotion (Kirmani et al. 2007; Lee et al. 2010). A variety of academic areas, such as psychology (Lee et al. 2000), management (Rhee et al. 2014), and economics, (Florack et al. 2013) have studied this theory and demonstrated these relationships. For instance, Zhao and Pechmann (2007, Table 1, p. 675) suggest, in the case of anti-smoking, that a piece of advertising framed with either promotion-focus or preventionfocus is more persuasive to consumers with the corresponding focus. In another case, Yoon et al. (2012) demonstrate that people with different RF present different patterns in selective information processing. Specifically, positive information, in comparison to negative information,<sup>2</sup> is more likely to be relied on by promotion-focused individuals.

Previous studies of RFT have mainly used two methods, survey and experiment, to capture people’s RF as found in a comprehensive review by Haws et al. (2010). Although rich knowledge has been gained from studies based on surveys and experiments, it has limited appeal to business practitioners, because it is almost impossible for online platforms to manipulate consumer RF or to conduct surveys among a large number of consumers in digital age applications (e.g., web advertising). Furthermore, surveys and experiments cannot be used to take advantage of secondary data in the assessment of customer RF. With the availability of large amounts of secondary data in e-commerce, innovative research is thus necessary and possible to fill this research gap.

In this paper, we advocate a novel approach to operationalize customer RF in the digital age. The rapid development of information technologies, such as e-commerce and cloud computing, has enabled online platforms to track customer behavior (Hashem et al. 2015; Xu et al. 2014), which provides an unprecedented opportunity to observe and understand customers from rich secondary data. In particular, these new information technologies have made it possible to study customers’ RF with e-commerce data logs. Consequently, the time is ripe for management researchers to operationalize a long-standing construct (i.e., RF), thus contributing to computational social science. In the context of this study, “operationalization” stems from design science research (Gregor and Hevner 2013; Hevner et al. 2004) and includes two cohesive and complementary parts: (1) development of a new IT artifact to compute customers’ chronic RF based on the affective dimension of RFT and (2) evaluation of operationalized regulatory focus (ORF) in practice.

This study makes an important contribution: the operationalization of RF. Following the paradigm of computational social science, we set out to operationalize customers’ chronic RF via text mining, leading to an innovative method we refer to as regulatory focus discovery, the core foundation of ORF. In other words, our research modernizes the utility of RFT for the digital age. In addition, this study also contributes to the design science literature by not only providing a rigorous analytic model to evaluate a new method, but also adding a new piece of “invention” work, which is limited in current research as suggested in Gregor and Hevner (2013). Our approach is innovative because we utilize a new technical means to enrich an existing behavioral theory, thus making a well-known social science theory more meaningful and more applicable in real-world business settings.

The rest of this paper is organized as follows. First, the theoretical background is introduced. Next, we operationalize RF by developing an innovative method and validating ORF via a field survey. The applicability of ORF to complete the operationalization process is then evaluated. Finally, we discuss our main findings.

## Regulatory Focus Theory

RFT was originally developed to theorize two types of regulatory orientation—promotion focus and prevention focus—and various relevant behavior (Higgins 1997, 1998, 2000). A promotion focus reflects an individual’s concern with accomplishments, hopes, and aspirations, with more emphasis on gaining positive outcomes and minimizing missed opportunities; conversely, a prevention focus reflects an individual’s concern with avoidance, responsibility, and safety, favoring absence of negative outcomes and stressing minimization of errors (Aaker and Lee 2006). Further, an individual’s RF can be considered either situational or chronic (Haws et al. 2010). In situational cases, RF is temporary and can be activated by situational factors, such as promotion versus prevention framing (Yeo and Park 2006). Researchers typically consider chronic RF to be a personality trait that is stable over a relatively long period (Gamache et al. 2015). Existing studies suggest that effects of RF are manifested in two dimensions, cognitive and affective, as outlined in the following subsections.

## RFT and Decision Making

Effects of RF can be observed in all stages of decisionmaking processes, such as information searching, information processing, and choice. Previous studies have shown that, in early stages of decision making, an individual’s RF serves as a filter of information in case of multiple pieces of incoming information (e.g., Chernev 2004; Pham and Chang 2010). That means people primarily select information matching their RF. Generally, people with a promotion focus tend to pay more attention to positive information that emphasizes the presence or absence of gain-related outcomes, while, conversely, people with a prevention focus tend to have a higher sensitivity to negative information that emphasizes the presence or absence of loss-related outcomes (Keller 2008). These consistent findings have been reinforced by a metaanalysis, which again reveals that RF contributes to selective information processing (see Hart et al. 2009). In information processing, it is also noted that individuals’ RF can influence the perceived salience of different components in a piece of information (Lee et al. 2010). Specifically, a promotionfocused individual is more likely to focus on positive signals, which increase the impact of positive aspects. In contrast, negative signals are more likely to be emphasized by a prevention-focused individual, thus exaggerating negative aspects of the information. In addition to the evidence from general behavioral studies, neuroscientific evidence from fMRI experiments suggests that individuals pay greater attention to negative stimuli under a prevention focus and to positive stimuli under a promotion focus (Cunningham et al. 2005).

Individuals’ RF also influence their product choice. In particular, Florack et al. (2013) demonstrated that individuals’ RF plays a dominant role in shaping their preferences and product choices. For example, strong anti-theft features tend to be more attractive than innovative features to a preventionfocused buyer, while the reverse is true to a promotionfocused buyer. A focal piece of information (e.g., advertising) can be framed differently and thus affect product choices of customers with different RF. Lee and Aaker (2004), for instance, found that promotion-focused customers are more likely to be persuaded by appeals that are framed in terms of gains, while prevention-focused customers are more likely to be persuaded by appeals framed in terms of losses. This is confirmed by Jain et al. (2007), who found that prevention-focused and promotion-focused customers respond differently to information with negative versus positive framing (i.e., the attributes of product A are better than those of B versus the attributes of product B are worse than those of A).

In summary, the various studies above, although focusing on different stages of decision making, all imply that a “fit” is preferable between an individual’s RF and the relevant information such as product attributes, consistently confirming the important role that individuals’ RF play in decision making (Higgins 2000). In addition to decision making, RFT also suggests that individuals’ RF can influence their emotions, as discussed next.

## RFT and Emotions

The principle of RFT prompts scholars to consider individuals’ emotions when they face different outcomes. Research on relationships between RF and emotions evolved from the work of Higgins et al. (1997) and has found that individuals with different RF demonstrated emotional differences in their evaluation of both positive and negative situations. Specifically, when there is a positive outcome, strong positive emotions (such as happiness or satisfaction) are more likely to be expressed by a promotion-focused individual; conversely, relatively weak positive emotions (such as calmness or relaxation) are more likely to be expressed by a preventionfocused individual. A negative outcome tends to induce weak negative emotions (like disappointment or discouragement) from a promotion-focused individual, but strong negative emotions (such as tension or unease) from a preventionfocused individual.

In a later study, Brockner and Higgins (2001) theorized that individuals’ RF influences the nature and magnitude of their emotional experience; specifically, emotions of promotionfocused individuals vary along a cheerful–dejected emotional spectrum, while emotions of prevention-focused individuals vary along a quiescent–agitated emotional spectrum. Brockner and Higgins also theorized that RF and related emotions can be manifested in several theories such as person– organization fit, expectancy-valence theory, and goal-setting theory. In an empirical study, Crowe and Higgins (1997) used a mood questionnaire (containing a series of items for measuring both positive and negative emotional dimensions) to measure respondents’ promotion- or prevention-focused orientation. In a field environment, Yen et al. (2011) further testified to the close relationship between individuals’ RF and their emotional experiences and showed that the positive emotions of promotion-focused individuals are more intense when there is a positive outcome. In contrast, the negative emotions of prevention-focused individuals are generally more intense when there is a negative outcome (Arnold et al. 2014). In a subsequent study, Liu and Brockner (2015) found that when people’s RF tendency is congruent with the event they are experiencing, more intense emotions tend to appear.

## Opportunities and Challenges in RFT Applications

Past investigations of RFT relied mainly upon conventional empirical research methods such as surveys, interviews, and experiments. The value of these existing research methods in the exploration of the explanatory power of RFT has been widely recognized, leading to a considerable amount of new knowledge. However, technology development and business innovations have raised new opportunities and challenges for the application of this theory in business in the digital age. For instance, in the e-commerce context, although it is useful and important to understand whether customers are promotion-focused or prevention-focused in order to improve personalized recommendation systems or targeted marketing (Luo et al. 2014; Xu et al. 2014), it is difficult to use surveys, experiments, or interviews to identify customers’ RF. On the other hand, interactive e-commerce has resulted in a large amount of customer data, which opens the door for the identification of customer RF from various types of secondary data. To address this research gap, this study makes a pioneering attempt to operationalize RF in the digital era.

## Operationalization of Regulatory Focus

In this section, we describe how to operationalize customers’ chronic RF. Since “nothing is so practical as a good theory” (Van de Ven 1989), we operationalize consumers’ RF according to the central thesis of RFT. We explore customer RF via the affective dimension rather than the cognitive dimension for the following reasons: (1) as suggested by Cunningham et al. (2005), determining customer RF from the cognitive dimension requires log data for the whole cognitive process, which is often not available in companies, and (2) the affective dimension can reveal sufficiently individuals’ social and psychological world (Pennebaker et al. 2003; Vaish et al. 2008).

## Theory and Data

## Theoretical Foundation

As mentioned in the previous section, RFT suggests that customers with different RF can experience different intensities of positive or negative emotions such as pleasure or pain (Werth and Foerster 2007). Specifically, when outcomes are satisfactory, promotion-focused customers express stronger positive emotions like happiness; in comparison, preventionfocused customers would express relatively weaker positive emotions like quiescence (Arnold et al. 2014; Higgins 1998). Conversely, when outcomes are not satisfactory, promotionfocused customers would have relatively weaker negative emotions like disappointment in contrast to stronger negative emotions like anxiety by prevention-focused customers (Higgins 1997; Liu and Brockner 2015). In summary, promotion- and prevention-focused customers tend to have positive and negative sentiment biases in their emotional evaluations; these sentiment biases are stable over time and consistent across contexts (Vaish et al. 2008). This provides an opportunity for sentiment analysis to capture customers’ chronic RF (Norris et al. 2011); we refer to this unique text mining procedure as RF discovery.

The theoretical guidelines above inspired us to develop the RF discovery method when taking advantage of online product reviews. Online reviews offer a good business context to perform the detection of customer RF for the following reasons. First, in an online shopping context, outcome perceptions are prominently reflected in online product reviews, because they are the most direct manifestation of customers satisfied and dissatisfied emotions (Yin et al. 2014). Second, online review literature suggested that review features, such as customer expressions, could be used to detect customer traits (Li and Hitt 2008). Third, scholars such as Gamache et al. (2015) have suggested that behavioral data such as product reviews are particularly suitable for the longitudinal study of customers’ chronic RF because they provide a non-instructed and consistent form of emotional expression for evaluation across products. This product review data provides a stability that “cannot be captured through surveys or interviews because of the lack of availability of informants over long periods of time and the inherent risks of retrospective bias” (Eggers and Kaplan 2009, p. 468). In summary, these three principles point out that it is possible to identify customers RF from sentiment biases in online product reviews.

## Data

We collected data from an e-commerce company that designs, produces, and sells apparel in an Asian market. Their apparel is moderately priced and attracts many customers to repurchase frequently. The company’s products are all private label products that are not sold by other retailers. The company has a proprietary e-commerce platform to solely sell its own products while enabling customers to make purchases and post reviews. In addition, a firm-sponsored online brand community (OBC) with a series of features and discussion boards, such as new product announcements and individual diaries, was built in order to facilitate customer interaction. Furthermore, there is a link to the brand community website on the homepage of the e-commerce platform. Registered customers can log into both the e-commerce and brand community websites with the same account, which provides the opportunity for us to track customers’ transaction records, product reviews, and community log data, simultaneously.

We collected data in December 2012. The firm provided us with a registration database of customers on its e-commerce platform and OBC along with demographic details and con tact information, a transaction database of more than 10,000 customers for the period of May 2011 to December 2012, and another database containing information on products, product reviews, and customers who produced the product reviews. Overall, there are more than 2,300 customers who generated about 12,800 reviews on 1,276 products during the time period. Taking customers who have generated online reviews as the sample and using our RF discovery method, we identitified these reviewers’ chronic RF (i.e., the ORF) in the first round of data analysis. This rich dataset also enabled us to validate the application of the ORF in studying customer purchase behavior by triangulating customers’ online reviews, community participation records, and e-commerce transaction records.

![](/api/attachments/TMYVF8QN/fulltext/images/37c6a125ba5f3cc21f49f5fedf7de7698064c3263c97c699b7cd4d555c2a61ee.jpg)  
Figure 1. Flow Chart of RF Discovery

## Operationalizing RF

As an effective tool for automatically detecting the intensity of emotional expressions (Abbasi et al. 2008; Chen 2011), a method of sentiment strength analysis was used to extract customer emotional patterns. Compared with preventionfocused customers, promotion-focused ones tend to have stronger positive sentiment or weaker negative sentiment when products satisfy or dissatisfy them. Thus, we say that promotion-focused customers have positive sentimentstrength bias. In contrast, prevention-focused customers tend to have weaker positive sentiment or stronger negative sentiment when products satisfy or dissatisfy them, and thus we say that prevention-focused customers have negative sentiment-strength bias. Figure 1 plots a flow chart of RF discovery that describes in detail how we mine customers’ chronic RF from online product reviews.

From our product review dataset, we built three complete bipartite networks: a customer-review network, a reviewproduct network, and a customer-product network. These networks enabled us to capture emotional patterns in product reviews and individual sentiment-strength biases in the product evaluations. Online product reviews were first analyzed with the SentiStrength algorithm (Thelwall et al. 2011), which is a well-known lexical approach that has proved to be an efficient tool for assessing emotive sentiment in short texts and has been widely applied in various contexts (Stieglitz and Dang-Xuan 2013). We adopted and customized the SentiStrength algorithm to our sentiment analysis not only because SentiStrength is designed to be one of the most suitable methods in mining users’ emotions (Thelwall et al. 2011), but also because SentiStrength provides better robustness and generality (Xie et al. 2014). In addition, Senti-Strength mines both positive and negative sentiment for each review simultaneously while other algorithms simply classify each review into either positive or negative sentiment as a whole (Thelwall et al. 2011).

In our study, we customized SentiStrength for use in Mandarin texts by pre-processing each review and developing a sentiment lexicon (detail is provided in Appendix A). We also refined the SentiStrength algorithm by developing two word lists —a booster word list and a negating word list—and incorporating them into SentiStrength as rules. The booster word list contains 97 words that boost or reduce the emotional impact of subsequent words, and the negative word list contains 36 words that invert subsequent emotion words. Based on the sentiment lexicons and the defined rules, the Senti-Strength algorithm classified texts according to both positive emotion strength (on a scale of 1 to 5) and negative emotion strength (on a scale of -1 to -5). However, before we utilized the customized SentiStrength algorithm, we had to assess its accuracy. We determined this by applying it to a set of texts that had been coded by humans and comparing the Senti-Strength scores with the human scores (Appendix B provides the details). The results indicated that the classification accuracy of the customized SentiStrength algorithm reached 81.3%. In addition to classification accuracy, the macroaverage of the sentiment analysis for both positive and negative classes in our test sample were 0.736 and 0.771, respectively. The accuracy and macro-average measures indicated that the SentiStrength algorithm performed well and did not suffer from the trivial classifier issue. Moreover, we also compared our SentiStrength algorithm with the support vector machine (SVM) based method (see Appendix C for details). The results showed that the customized SentiStrength method performed better than SVM and allowed us to extract both positive and negative sentiment strength from the online reviews with good confidence. For an online product review $r _ { i j }$ of produc ${ \cdot } p _ { j }$ generated by customer $c _ { i } ,$ we captured positive sentiment strength, $S S R _ { i j } ^ { + } ( 1 \leq S S R _ { i j } ^ { + } \leq 5 )$ and negative sentiment strength, $S S R _ { i j } ^ { - } ( - 5 \ \stackrel { \cdot } { \le } \ S S R _ { i j } ^ { - } \ \le \ \stackrel { \cdot } { - } 1 )$

Next, we detected sentiment-strength biases (both positive and negative) of customers in their reviews. RFT theorizes that promotion-focused individuals tend to have a positive sentiment-strength bias in their product evaluation and prevention-focused individuals tend to have a negative sentiment-strength bias (Gross and John 2003; Higgins et al. 1997). In order to capture such sentiment-strength biases, we calculated the overall sentiment strength of a product based on the review-product network. We adopted the mechanism proposed by Liu (2012) on product review aggregation and computed the sentiment strength of the product according to the following equations:

$$
S S P _ {j} ^ {+} = \frac {\sum_ {i = 1} ^ {m} S S R _ {i j} ^ {+}}{m}\tag{1}
$$

$$
S S P _ {j} ^ {-} = \frac {\sum_ {i = 1} ^ {m} S S R _ {i j} ^ {-}}{m}\tag{2}
$$

where $S S P _ { j } ^ { + }$ (SSP<sup>-</sup>) is the overall positive (negative) sentiment-strength of the produc $. p _ { j } .$ The variable is the number of online reviews of the product. We computed the sentiment strength of the product by using the aggregate-andaverage approach suggested by Liu and considered that such an approach is appropriate for sentiment aggregation for both theoretical and empirical reasons. Theoretically, previous research has demonstrated that individual sentiment strength in product reviews is stable (Basiri et al. 2014). Empirically, we tested the stability of sentiment strength in online reviews by analyzing whether sentiment strength in online review is influenced by negativity bias, which suggests that online reviews follow a declining trend over time. Following the guidelines of Godes and Silva (2012), we checked the sequential and temporal dynamics of sentiment strength in the online reviews (the results are reported in Appendix D). The results indicate that sentiment strength in online reviews is not influenced by sequences of reviews or by the time at which reviews are posted.

After obtaining the sentiment strength of the products, we determined the sentiment-strength biases that customers exhibited in their product reviews, and classified customers as promotion-focused or prevention-focused by using the procedure shown in Figure 2. We calculated the sentiment-strength bias of each review and formalized it as 1 (positive), 0 (neutral), or -1 (negative). Then, we delineated a voting scheme to classify each customer as promotion-focused or preventionfocused on the condition of achieving a majority vote (i.e., more than half) amongst the sentiment-strength customer biases. We chose the majority voting scheme for several reasons. First, a majority voting scheme is developed from the expected behavior of the consensus (Lam and Suen 1997), which classifies customers based on their consistent behavior on emotional evaluations suggested by the RFT (Werth and Foerster 2007). Therefore, the majority voting scheme has a conceptual justification with the RFT. Second, studies have shown that the majority voting scheme is accurate and less sensitive to outliers (Zheng and Padmanabhan 2007), has a low computational complexity (Chelmis and Prasanna 2013), and can ensure algorithm convergence quickly (Das and Chen 2007). These advantages of majority voting scheme enable the application of our RF discovery method in e-commerce. Moreover, in line with previous studies (Das and Chen 2007), we took half as the threshold value in order to eliminate datasnooping bias and keep our sample size (Appendix E provides additional analyses on variation of threshold value). Consequently, only when more than half of both positive and negative sentiment-strength biases were consistent in the positive direction would the customer be classified as a promotionfocused individual. Similarly, if more than half of both positive and negative sentiment-strength biases were consistent in the negative direction, the customer was classified as a prevention-focused individual. However, if the above situations of consistency did not occur, the consumer was not classified.

Some reviews selected from the sample data are used to further clarify how chronic RF can be reflected in product evaluation. Figure 3 presents two examples. Graph (a) shows the positive and negative sentiment strength patterns of a customer (ID = 39514) and the corresponding products with the specific comments. This graph shows that both positive (the dashed line) and negative (the dotted line) sentiment strength embedded in reviews are consistently lower than that

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For each $c_i \in C$ ($C$ is a set of customers)

$SSB_i^+ = 0, SSB_i^- = 0$

For each $r_{ij} \in c_i (r_{ij}$ is an online review generated by $c_i$)

if $SSR_{ij}^+ - SSP_j^+ &gt; 0, SSB_i^+ = SSB_i^+ + 1$

else if $SSR_{ij}^+ - SSP_j^+ = 0, SSB_i^+ = SSB_i^+$

else if $SSR_{ij}^+ - SSP_j^+ &lt; 0, SSB_i^+ = SSB_i^+ - 1$

if $SSR_{ij}^- - SSP_j^- &gt; 0, SSB_i^- = SSB_i^- + 1$

else if $SSR_{ij}^- - SSP_j^- = 0, SSB_i^- = SSB_i^-$

else if $SSR_{ij}^- - SSP_j^- &lt; 0, SSB_i^- = SSB_i^- - 1$

if $SSB_i^+ &gt; 0 \land SSB_i^- &gt; 0, c_i$ is classified as promotion-focused

else if $SSB_i^+ &lt; 0 \land SSB_i^- &lt; 0, c_i$ is classified as prevention-focused
</div>

## Figure 2 Voting Scheme for Classification

![](/api/attachments/TMYVF8QN/fulltext/images/19fdaf9d0310eb78e81bdd396e21274f839c44355d5daa7f99713d35ee0fc432.jpg)  
Figure 3. Two Examples

of the products evaluated by all customers (the peaks of the horizontal line), respectively, suggesting that the focal customer has a negative sentiment-strength bias in his/her emotions. Thus, the customer is likely to be prevention-focused. Graph (b) shows the sentiment-strength patterns in the product reviews of another customer (ID = 44665) who is likely to be promotion-focused.

## Field Survey Assessment

In this section, we describe a field survey to demonstrate whether our RF discovery method accurately identified individuals’ RF. We first classified the 2,301 customers who were offered a reward (about 5 USD) if they completed the questionnaire successfully.

![](/api/attachments/TMYVF8QN/fulltext/images/00818729acb8dc91e52cee20408c25f27aabedd86c19e32f5ac9b38ed074d4c0.jpg)  
(b)  
had posted online reviews based on the RF discovery method and then randomly selected 300 customers from each group (i.e., promotion- versus prevention-focused). As mentioned earlier, the dataset allowed us to track customers and their contact information for academic purposes. We sent questionnaires to them in order to verify whether our classification is valid. We adopted the RF measurement questionnaire developed by Haws et al. (2010), which has 10 measurement items: 5 promotion focus and 5 for prevention focus. Each question was answered on a seven-point Likert scale (from strongly disagree to strongly agree). As the respondents were native speakers of Mandarin, the questionnaire was translated from English to Mandarin (Van de Vijver and Leung 1997). In order to increase their incentive to engage, the respondents

In all, 141 responses were received. After removing incomplete questionnaires and questionnaires with demographic mismatch issues, 124 valid questionnaires remained. Regarding demographics, 78.6% of the respondents were female, 53.7% were between 26 and 35 years old, over 42.5% had a university degree or other higher education, and 93.2% purchased online frequently (more than three times a year). We also checked whether the 124 survey respondents suffer from selection bias issue. To fulfill this purpose, we first compared demographics of the survey respondents with the non-survey customers in our sample. Both t-test and U-test suggested that there are no demographic differences between the survey respondents and non-surveyed customers. In addition, we also compared online review activities of the survey respondents with those of reviewers outside survey and we did not observe significant differences (see Appendix F for details). Then, to test the reliability and correlation of the measurement scores, the responses were averaged to calculate separate promotion and prevention scores (Louro et al. 2005). Both the RF promotion scale and the RF prevention scale were reliable $( \alpha _ { p r o m o t i o n } = 0 . 6 3 , \alpha _ { p r e v e n t i o n } = 0 . 7 2 )$ and uncorrelated r = 0.01).

Before revealing whether the survey results matched those of our RF discovery method, we tested whether there is a tight relationship between customers’ RF from the survey and their sentiment biases from text mining. The analysis in Appendix G shows the relationship. We took the classification results from the field survey as the “ground truth” to measure the performance of RF discovery, including the precision and recall of promotion- and prevention-focused outcomes, respectively. We followed the pattern recognition literature stream, and defined precision as the proportion of retrieved instances (from text analysis) that are correct (according to survey), and defined recall as the proportion of the correct instances (according to the survey) that are retrieved (by text analysis) (Anderson and Simester 2014). A group of 66 promotion-focused customers was identified by RF discovery; 55 of these were also identified as being promotion-focused by survey, and the total number of promotion-focused customers in the survey sample was 63. Thus, the precision and recall of the promotion-focused class were 83.3% and 87.3%, respectively. A group of 58 prevention-focused customers was identified by RF discovery, 50 of whom were also identified as prevention-focused by the survey method, and the total number of prevention-focused customers in the survey sample was 61. Thus, the precision and recall of the prevention-focused class were 86.2% and 82.0%, respectively.

We also checked the robustness of our classification result. In particular, we examined how the classification accuracy changed as the volume of online reviews increases. Figures 4 and 5 present the distribution of number of reviews for each customer and the performance of our classification method, respectively. Figure 4 shows that the number of customers decreases with the increasing number of product reviews. As shown in Figure 5, we observed that the more reviews used in the analysis, the better the performance would be. The result also shows that performance is still reliable to customers with only a few reviews. There are at least three reasons for this robustness of result. First, in our RF discovery method, customers with a few reviews are analyzed in comparison with other customers who have purchased the same products and, therefore, ORF is a comparative computational outcome based on many reviews, even for customers with a single review. Second, previous studies have demonstrated that individual sentiment bias is stable (Pennebaker et al. 2003) and can be accurately captured by a few comments based on sentiment analysis (Basiri et al. 2014). The stability of sentiment bias and the good performance of our customized SentiStrength method reinforce the credibility of classification on the basis of a small number of reviews. Third, the evalua tion space model suggests that positive and negative senti ment biases can coexist and are relatively independent (Norris et al. 2011). Thus, we used both positive and negative sentiment bias in each review to detect RF, and such design enables us to understand customers’ emotional tendency effi ciently even for those who only give a few reviews. In summary, our survey study indicates that the classification accuracy of our method reaches 84.7% and our approach is quite stable across customers who generate various amounts of reviews. By using the classification approach based on text analysis, the RF discovery method can distinguish promotionfocused customers from prevention-focused customers with high reliability.

## Discussion

Sentiment analysis techniques, which always involve high complexity and uncertainty (Abbasi et al. 2008), cannot support mining text for individuals’ sentiments with perfect accuracy (Chen et al. 2012). According to the literature (Thelwall et al. 2011), an accuracy that is higher than 85% should be considered excellent. Therefore, we have obtained an acceptable accuracy in the sentiment analysis outcome of our RF discovery method.

It is also possible that certain complexities in the survey responses may also affect our classification accuracy. As previously mentioned, although RF can be chronic, it can also be situational. That is, when we were conducting our field survey, a responder might be measured as prevention-focused even if he/she was chronically promotion-focused, because of the influence of situational factors at that specific time period. As has been discussed in previous studies such as Benbasat (1989), field surveys are affected by the issue of internal validity due to the control problem; that is, it is relatively difficult for researchers to control possible interruption factors that potentially influence the results. Despite this methodological disadvantage and potential response bias, our findings showed a relatively good result. In addition, the RF discovery method we develop can be used to further evaluate ORF in the e-commerce context as presented next.

![](/api/attachments/TMYVF8QN/fulltext/images/0b0742096da281c8dc4d82ca14a408fc45227310b762f11a78a985d0097d6594.jpg)  
(a)

![](/api/attachments/TMYVF8QN/fulltext/images/ebbf20f546f2b31f85a6e991228e958fec7d4972424f6647ad78966f3d2f4fe6.jpg)  
(b)

Figure 4. The Distribution of Number of Reviews per Customer  
![](/api/attachments/TMYVF8QN/fulltext/images/6805d6c1a65f0c5117c3f0ba311f85a53c0e457a2d35666349374d16b679ae27.jpg)  
Figure 5. Performance of RF Discovery

![](/api/attachments/TMYVF8QN/fulltext/images/d758a658e42a6f592c351d7b359a8a1716ecf2c96e4c80f92accf227b1f2b17e.jpg)  
(b)

## Evaluation of ORF

Development and evaluation are considered two complementary parts of design science research surrounding IT artifacts (see Gregor and Hevner 2013, pp. 342-352; Hevner et al. 2004, pp. 86-87). After developing and demonstrating ORF, we sought to evaluate ORF as an IT artifact. Hevner et al. (2004) suggest that an IT artifact must be evaluated effectively, enabling its implementation and application in an appropriate domain. In particular, we evaluate ORF by applying it in the domain of consumer purchase behavior in OBC as detailed next.

## Hypothesis Development

An OBC is a virtual community comprising customers, companies, and the relationships between them (Muniz and O’Guinn 2001). Recent studies have attempted to identify the relationship between OBC participation and customer purchase behavior and generated mixed findings. Several studies showed that OBC participation can intensify the customerfirm relationship (Rishika et al. 2013), increase the likelihood of customer purchase (Adjei et al. 2010), and have a positive impact on customers’ purchase expenditure (Goh et al. 2013). The authors of these studies argued that participation in a firm’s OBC can improve customer purchase via information sharing and communication. OBCs offer important sources of product information (Muniz and O’Guinn 2001), and information sharing and communication in OBCs reduce uncertainties about the quality of products and customer services provided by firms. According to uncertainty reduction theory (Berger 1987), a reduction in uncertainty levels strengthens the relationship between customer and firm. Therefore, an OBC member, who has less uncertainty about a firm and its products, is more likely to purchase (Adjei et al. 2010). Also, Goh et al. (2013) demonstrated that diverse types of customer communication in an OBC have distinct effects on increasing customers’ purchase expenditure.

In contrast, other studies indicated that OBC participation can have negative consequences for firms. Participation in OBCs may expose customers to more information about a broader array of related products and thus increase the likelihood that they will buy products from rival firms (Thompson and Sinha 2008). Moreover, Algesheimer et al. (2010) indicated that “customer community marketing programs may not have the potential of increasing behaviors of participants and might even decrease these behaviors post participation” (p. 767). They suggested that OBC participation has educational effects on customers: OBC members can learn much from information sharing and customer interaction and become more conservative in their spending. The contradictory findings in the literature motivate an interesting research question as discussed next.

According to RFT, we conjecture that customers’ RF could explain the inconsistent findings above to some extent. In an OBC, customers rely on their RF as a filter to select relevant information because OBCs offer an overwhelming amount of information (Florack et al. 2013; Pham and Chang 2010; Wang and Lee 2006). In particular, promotion-focused individuals are more concerned about positive information because such information signals satisfactory experiences and thus presents opportunities to attain positive outcomes. In contrast, prevention-focused individuals are more concerned about negative information which emphasizes safety and loss avoidance. Further, when a piece of information includes both promotion-oriented positive and prevention-oriented negative elements, promotion-focused customers are more sensitive to the positive elements, while prevention-focused customers are more sensitive to the negative elements (Yoon et al. 2012). This principle of information selection bias leads us to conjecture that the increasing availability of information in a brand community may have different impacts on promotion- and prevention-focused customers. More formally, we have the following hypothesis:

Proposition: The effect of participation in a customer brand community on purchase behavior is contingent on the customer’s RF; specifically, OBC participation has a positive impact on the purchase frequency of promotion-focused customers but a negative impact on the purchase frequency of prevention-focused customers.

## Econometric Model Specification and Results

To test our hypothesis, we matched the community participation records, transaction records, and online reviews of customers using their unique IDs. We filtered the relevant data in our analysis according to the following criteria:

(1) Customers who made purchases must also be members of the brand community. In addition, these members had to register during the period May 2011 to June 2012 in order to have sufficient observations and data to reliably estimate model parameters. Our approach is in line with the work of Rishika et al. (2013).

(2) Customers who made purchases must also have posted online product reviews to ensure the applicability of RF discovery in ORF. Finally, 484 samples were included in our econometric validation model. Among them, 248 were classified as promotion-focused and 225 as prevention-focused by using our approach, leaving 11 customers unclassified.

## Econometric Issues

In order to estimate the causal effects of OBC participation on customer purchase frequency conditional on customers’ RF, four econometric issues must be addressed: (1) self-selection bias, (2) reverse causality, (3) social network endogeneity, and (4) unobserved customer heterogeneity. First, selfselection bias can arise because customers who participate in the OBC may exhibit characteristics that differ systematically from nonparticipants, and this systematic difference might also determine customer purchase behavior. The estimates of the outcome variable (purchase frequency) may become biased and inconsistent if self-selection bias is not corrected (Heckman 1979). To resolve this problem, we utilized propensity score matching (PSM) combined with the difference-in-differences (DID) technique, suggested by Huang et al. (2012). In PSM, we included customers’ observed characteristics to construct a sample of nonparticipants who display the same characteristics as participants in the OBC. We then conducted a DID analysis to estimate the impact of OBC participation based on the resulting matched sample. Second, another endogeneity concern is the potential reverse causality problem: high value customers who have high purchase frequency might be more likely to join the firmsponsored OBC. As a check, we tested whether customer purchase behavior before participation could foretell their OBC participation. We conducted several analyses to rule out reverse causality.

In addition, the customers’ social network and their purchase behavior seem to be correlated, regardless of whether there is a causal influence since a peer effect in the social network can affect a customer’s behavior. In line with studies on the social network effect (Iyengar et al. 2011), we controlled for social network endogeneity by including a variable indicating the purchase behavior of neighboring customers. Finally, customers generally differ in terms of their propensities and preferences in buying products of a specific brand. While some customers tend to make frequent purchases of products from a certain brand online, others buy few products online and obtain more from physical stores. We accounted for this phenomenon by incorporating both observed and unobserved user heterogeneity into our model. We address the details of these four econometric issues in the following sections.

## The Main Equation

PSM is used to construct treatment and control groups of customers who resemble each other in all observed characteristics. The major difference between these two groups is that the customers in the treatment group participate in the OBC while those in the control group do not (see Appendix H for details on PSM procedure and results). Having obtained a control group of customers, we then proceeded to estimate the impact of OBC participation conditional on ORF with a DID estimator. The DID was estimated from the following individual purchase equation, using data on the treatment and control customers:

$$
\begin{array}{l} \log \left(P u r F r e q _ {i, j, i}\right) = \beta_ {0} + \beta_ {1} T r e a t e d _ {i j} + \beta_ {2} O B C P a r t _ {i j, t} \\ \quad + \beta_ {3} T r e a t e d _ {i j} \times O B C P a r t _ {i j, t} + \beta_ {4} T r e a t e d _ {i j} \times O B C P a r t _ {i j, t} \\ \times R e g u F o c u s _ {i j} + \beta_ {5} N e i g h b o r P u r F r e q _ {- i j, t} \\ \quad + \beta_ {6} S a l e s I n t e n s i t y _ {i j, t} + \beta_ {7} \log \left(\text { Price } _ {i j, t}\right) + \beta_ {7} T r a n F e e _ {i j, t} \\ \quad + \mu_ {i j} + \theta_ {t} + \varepsilon_ {i j, t} \end{array}\tag{3}
$$

where I denotes a matched pair of customers, j denotes a treatment-group or a control-group customer, and t denotes the time period. The dependent variable is the monthly purchase frequency of a treatment/control customer $( P u r F r e q _ { i j , t } ) .$ In line with previous studies (Rishika et al. 2013), we log transferred the purchase frequency variable in the model. $\it { T r e a t e d } _ { i j }$ is the treatment dummy variable that takes the value 1 if the customer j in a matched pair I belongs to the treatment group, and 0 otherwise. $O B C P a r t _ { i j , t }$ is a dummy variable indicating whether month t is in the post-participation period; $R e g u F o c u s _ { i j }$ is a dummy variable that equals 1 if the customer is promotion-focused and 0 if the customer is preventionfocused.

Several control variables were included in the estimation. To account for the social network effect, we included the $N e i g h b o r P u r F r e q _ { - i j , t }$ variable to reduce the endogeneity bias; this measures the average purchase frequency of a customer’s neighbors (people living in the same district) in a time period. We also took into account the “sale intensity” of a customer $( S a l e I n t e n s i t y _ { i j , t } ) .$ , that is, the proportion of products a customer buys on sales in a given time period. To control for the effects of marketing-mix activities, we included the variable $P r i c e _ { i j , t }$ (which measures the average price a customer pays for all of his/her products in period t) and the variable $T r a n F e e _ { i j , t }$ (which measures the average shipping fees a customer pays for the products in period t). We took the logarithm of the price variable to control for its right-skewed nature. In addition, to account for unobserved user heterogeneity, we included user fixed-effects $( \mu _ { i j } )$ . Finally, θ is a time-period dummy and $\mathcal { E } _ { i j , t }$ is the user- and time-specific error term. Table 1 shows the descriptive statistics of all variables.

## Main Analytical Results

Table 2 shows estimations of a series of alternative models using the DID technique. Model 1 is the basic DID model without any control variables. In Model 2, we included behavioral variables as controls, and Model 3 is an augmented version of Model 2 that includes customer-specific fixed effects and time-specific effects. Model 4 includes the threeway interaction effect among the treatment variable, customer OBC participation, and their RF. Table 2 provides substantial evidence that adding the RF increases prediction validity for purchase frequency. In particular, analysis of covariance test was performed to compare Model 4, which includes the RF and its interaction term, with its nested counterpart in Model 3. The partial F-test (5.41, p < 0.01) showed that Model 4 achieved significant improvement in explanatory power for purchase frequency over Model 3.

<table><tr><td rowspan="3">Variables</td><td colspan="4">Nonparticipation Group</td><td colspan="4">Participation Group</td></tr><tr><td colspan="2">Promotion Focus</td><td colspan="2">Prevention Focus</td><td colspan="2">Promotion Focus</td><td colspan="2">Prevention Focus</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>PurFreq</td><td>2.539</td><td>3.302</td><td>2.541</td><td>2.659</td><td>3.029</td><td>4.964</td><td>2.668</td><td>2.249</td></tr><tr><td>PurExpe</td><td>340.011</td><td>318.352</td><td>346.877</td><td>354.227</td><td>386.962</td><td>323.973</td><td>351.164</td><td>344.099</td></tr><tr><td>SaleIntensity</td><td>0.237</td><td>0.346</td><td>0.227</td><td>0.348</td><td>0.259</td><td>0.355</td><td>0.284</td><td>0.376</td></tr><tr><td>Price</td><td>159.67</td><td>159.82</td><td>181.71</td><td>260.38</td><td>160.09</td><td>150.77</td><td>144.99</td><td>148.38</td></tr><tr><td>TranFee</td><td>2.870</td><td>4.229</td><td>2.915</td><td>4.218</td><td>2.362</td><td>3.793</td><td>3.507</td><td>4.768</td></tr><tr><td>NeighborPurFreq</td><td>2.317</td><td>1.047</td><td>2.359</td><td>1.025</td><td>2.368</td><td>1.232</td><td>2.421</td><td>2.145</td></tr><tr><td>ReviewIntensity</td><td>0.316</td><td>0.424</td><td>0.300</td><td>0.414</td><td>0.337</td><td>0.437</td><td>0.320</td><td>0.381</td></tr><tr><td>AddressDisclosed</td><td>0.992</td><td>0.084</td><td>0.988</td><td>0.105</td><td>0.998</td><td>0.038</td><td>0.990</td><td>0.095</td></tr><tr><td>PhoneDisclosed</td><td>0.425</td><td>0.492</td><td>0.410</td><td>0.494</td><td>0.563</td><td>0.496</td><td>0.504</td><td>0.501</td></tr><tr><td>MSNDisclosed</td><td>0.176</td><td>0.381</td><td>0.109</td><td>0.312</td><td>0.207</td><td>0.405</td><td>0.203</td><td>0.401</td></tr><tr><td>Female</td><td>0.737</td><td>0.440</td><td>0.814</td><td>0.389</td><td>0.768</td><td>0.431</td><td>0.798</td><td>0.401</td></tr><tr><td>Age</td><td>33.084</td><td>4.214</td><td>34.219</td><td>4.367</td><td>32.674</td><td>2.955</td><td>33.001</td><td>3.115</td></tr><tr><td>Income</td><td>2.110</td><td>1.274</td><td>1.995</td><td>1.267</td><td>2.042</td><td>1.234</td><td>2.115</td><td>1.321</td></tr><tr><td>Urban</td><td>0.186</td><td>0.399</td><td>0.167</td><td>0.374</td><td>0.177</td><td>0.382</td><td>0.224</td><td>0.417</td></tr><tr><td>South</td><td>0.785</td><td>0.411</td><td>0.827</td><td>0.378</td><td>0.812</td><td>0.390</td><td>0.766</td><td>0.423</td></tr></table>

<table><tr><td>Variables</td><td>Model (1)No Controls</td><td>Model (2)Controls</td><td>Model (3)Controls, FE, TE</td><td>Model (4)Three-WayDifference</td></tr><tr><td>Treated</td><td>0.025(0.045)</td><td>0.056(0.045)</td><td>0.026(0.044)</td><td>0.024(0.045)</td></tr><tr><td>OBCPart</td><td>0.061*(0.035)</td><td>0.083**(0.035)</td><td>0.022(0.037)</td><td>0.017(0.037)</td></tr><tr><td>Treated × OBCPart</td><td>0.179***(0.053)</td><td>0.205***(0.053)</td><td>0.191***(0.053)</td><td>0.113*(0.067)</td></tr><tr><td>ReguFocus</td><td>0.021(0.027)</td><td>0.033(0.027)</td><td></td><td></td></tr><tr><td>Treated × OBCPart × ReguFocus</td><td></td><td></td><td></td><td>0.170***(0.055)</td></tr><tr><td>NeighborPurFreq</td><td></td><td>0.173***(0.030)</td><td>0.078**(0.038)</td><td>0.079**(0.038)</td></tr><tr><td>SaleIntensity</td><td></td><td>0.379***(0.038)</td><td>0.399***(0.039)</td><td>0.404***(0.040)</td></tr><tr><td>ln(Price)</td><td></td><td>-0.048***(0.018)</td><td>-0.077***(0.019)</td><td>-0.077***(0.019)</td></tr><tr><td>Transfer</td><td></td><td>-0.004(0.003)</td><td>-0.006*(0.003)</td><td>-0.005(0.003)</td></tr><tr><td>Intercept</td><td>0.651***(0.033)</td><td>0.227***(0.105)</td><td>-0.135(0.261)</td><td>-0.072(0.262)</td></tr><tr><td>User fixed effects</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-specific dummies</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.010</td><td>0.055</td><td>0.084</td><td>0.088</td></tr></table>

Notes: Standard errors in parentheses; FE = customer fixed specific effects; TE = time-specific effects. \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01.

<table><tr><td rowspan="2">Variables</td><td colspan="2">Model (5) Subsample: Prevention Focus</td><td colspan="2">Model (6) Subsample: Promotion Focus</td></tr><tr><td>Coefficient</td><td>SD</td><td>Coefficient</td><td>SD</td></tr><tr><td>Treated</td><td>0.215***</td><td>0.079</td><td>0.132**</td><td>0.054</td></tr><tr><td>OBCPart</td><td>0.093</td><td>0.069</td><td>0.007</td><td>0.044</td></tr><tr><td>Treated × OBCPart</td><td>-0.114</td><td>0.098</td><td>0.312***</td><td>0.063</td></tr><tr><td>NeighborPurFreq</td><td>0.024</td><td>0.078</td><td>0.090**</td><td>0.044</td></tr><tr><td>SaleIntensity</td><td>0.465***</td><td>0.075</td><td>0.377***</td><td>0.048</td></tr><tr><td>ln(Price)</td><td>-0.091***</td><td>0.035</td><td>-0.071***</td><td>0.023</td></tr><tr><td>TranFee</td><td>0.001</td><td>0.006</td><td>-0.008*</td><td>0.004</td></tr><tr><td>Intercept</td><td>-0.222</td><td>0.585</td><td>-0.068</td><td>0.293</td></tr><tr><td>User fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Time-specific dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>R2</td><td colspan="2">0.113</td><td colspan="2">0.095</td></tr></table>

Notes: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01.

We found that the parameter corresponding to the treatment effect of OBC participation (Treated × OBCPart) is consistently positive and significant across Models 1, 2, and 3. This finding implies that joining a firm-sponsored OBC positively influences customer value in terms of purchase frequency. We also found positive and statistically significant social network effects and sale effects on customer purchase behavior. This indicates that an increase in the purchase frequency of neighborhoods or sale offerings is associated with an increase in a customer’s product purchases. Moreover, we found that there are negative and statistically significant relationships between payment (i.e., price and shipping fees) and product purchases. Furthermore, in order to study how an individual’s RF moderates the effect of OBC participation, we included the three-way interaction term (Treated × OBCPart × ReguFocus) in Model 4. The coefficient of the three-way interaction term is positive and significant, indicating that a customer’s RF moderates the effect of OBC participation and the impact of customer participation in a firm-sponsored OBC is higher for customers with a promotion focus than customers with a prevention focus.

Next, we investigated how ORF influences the effect of OBC participation. We divided the sample dataset into two subsamples, one consisting of prevention-focused customers and the other of promotion-focused ones. We then conducted a DID analysis for each customer segment to distinguish the impact of OBC participation at the segment level. Table 3 shows the estimated results. Interestingly, we found a positive and significant OBC participation effect on promotionfocused customers (the coefficient estimate is 0.312). However, we also found a negative but not statistically significant coefficient of the treatment effect of OBC participation on prevention-focused customers (the coefficient estimate is -0.114). This implies that participation in a firm-sponsored OBC does not affect the purchase frequency of preventionfocused customers. In other words, OBC participation influences only promotion-focused customers about their customer purchase frequency. In addition, our results indicate that there are asymmetric social network effects on promotionfocused customers and prevention-focused customers. Specifically, we found a positive and statistically significant social network effect on purchase behavior of promotion-focused customers (the coefficient estimate is 0.090) and a nonsignificant social network effect on that of prevention-focused customers. These findings imply that the purchase behavior of promotion-focused customers is more likely to be influenced by their neighborhood than that of prevention-focused ones.

## Robustness Checks

## Instrumental Variable Specification

We used an instrumental variable specification to rule out self-selection bias as an instrumental variable is generally used to address potential endogeneity issues in econometric models when treatment (i.e., OBC participation in our context) is correlated with the error term (Heckman 1997). The instrumental variable taken into consideration should meet exclusion restriction and relevance assumptions: It must be uncorrelated with the dependent variable (i.e., purchase frequency) but correlated with the treatment variables (i.e., OBC participation). In our study, we used users’ review intensity in a given time period (ReviewIntensity<sub>it</sub>) as an instrumental variable. We defined review intensity as the ratio of the total number of product reviews posted by a customer during a given time period divided by the number of products which the focal customer purchased during the same period. This conceptualization derives from the study by Dellarocas and Narayan (2006), where they developed a density metric with a similar definition.

We conjecture that the review intensity should satisfy the relevance assumption because the literature shows that individuals’ propensity to either post reviews or engage in an OBC is governed by the same factors (Berger 2014). In addition, scholars have also pointed out that customers’ review propensity, as one of their traits, is not related to their purchase frequency (Arnold et al. 2014). Hence, we expect the review intensity to be exogenous. We further provide relevant statistics to show validity of the instrument in Appendix I. The results from our instrumental variable specification (Table I1 in Appendix I) are consistent with the results obtained from the DID method, indicating significant robustness.

## Inclusion of Additional Variables and Alternative Matching Algorithm

We checked the validity of our results via inclusion of two additional variables and an alternative matching algorithm in the PSM procedure. The two additional variables are as follows: one is a dummy variable indicating whether a customer validated his/her email address when registering on the business website (EmailValidated), and the other is a categorical variable indicating whether the customer lived in the east, middle, or west of the country (EasMidWes). These two variables may be related to a customer’s propensity to participate in a firm-sponsored OBC. For example, customers who validated their accounts were more likely to trust the firm and tended to engage in its OBC. Table J1 in Appendix J shows the results of a logit model with additional variables. Apart from using additional variables, we also employed an alternative matching method called the kernel-matching algorithm in our PSM procedure. Table J2 shows the main results of this additional effort. There is no significant difference revealed in comparison with the results presented earlier in subsection “Main Analytical Results.”

## Purchase Expenditure and Subsample Analysis

We checked the validity of our results by documenting the moderating effect of ORF on the relationship between OBC participation and the consumer’s total purchase expenditure in a period $( P u r E x p e _ { i j , t } )$ . The descriptive statistic of purchase expenditure is shown in Table 1, whose values suggest that the impact of OBC participation on customers’ purchase expenditure is influenced by RF. We utilized Equation (2) with purchase expenditure $( P u r E x p e _ { i j , t } )$ as the dependent variable and conducted DID analysis for each segment to distinguish the influence of OBC participation on purchase expenditure for promotion- and prevention-focused customers. The results are reported in Table K1 and Table K2, respectively, in Appendix K. Based on Table K1, we also compared Model 18 with Model 17 to assess the effect of incorporating the RF and its interaction term. An analysis of covariance test rejected Model 17 in favor of Model 18 at a significant level for purchase expenditure (the partial F-test = 3.15, p < 0.05). We also found that all the results pertaining to the effect of OBC participation using total purchase expenditure as the dependent variable are substantively similar to the results presented earlier in subsection “Main Analytical Results.”

To account for measurement error caused by potential misclassification in ORF, we also checked the robustness of our results with a subsample. As mentioned in the earlier “Discussion” subsection, the performance of sentiment analysis and ORF classification is very good, but not perfect. If we incorporate misclassified ORF into the econometric model, it may cause measurement errors. To account for such measurement errors, we tested DID models with the subsample that consisted of customers who were accurately matched. The results are shown in Table K3. We found that our results are substantially consistent with those in Tables 2 and 3.

## Inclusion of Customer Satisfaction

Previous studies have suggested that customers’ satisfaction is an important factor in purchase behavior (e.g., Conlon et al. 2001; De et al. 2013). In order to tease out a possible alternative explanation of customer satisfaction, we performed additional analysis. Recall that our data was collected from a company that produced private label apparel and sold via its own e-commerce platform. Our analysis is simplified by the fact that this platform was only used to sell its own products (i.e., apparel). Similar to studies such as Bolton and Lemon (1999) and Scherer et al. (2015), we developed the variable DeltaPurchase to represent customer satisfaction. This variable reflects the changes in customer’s purchase behavior, a decrease in a customer’s purchase frequency indicates dissatisfaction (Nitzan and Libai 2011; Scherer et al. 2015). To avoid scale differences among customers and bias caused by fluctuations in purchase frequency over time, we measured DeltaPurchase to denote the current month’s purchase frequency as a proportion of the average purchase frequency in the three preceding months (mean = 0.873, SD = 0.294). We then included the DeltaPurchase variable in our main analysis. The results are reported in Table L1 in Appendix L. We found that customer satisfaction has a positive and significant (p < 0.01) impact on purchase frequency. Importantly, we found that the main relationships among the key variables remain the same.

## Ruling Out Reverse Causality

We tested for possible reverse causality by investigating the link from customer purchase frequency to OBC participation, while controlling for customer characteristics. First, as an initial check, we illustrated the average purchase frequency of the treatment and control groups before their OBC participation (Panel A of Table M1 in Appendix M). The descriptive statistics clearly suggest that there is no significant difference in purchase frequency between the treatment and control groups before OBC participation (p > 0.1). This is evidence that customers’ purchase behavior is not correlated with their OBC participation decisions. Second, we tested whether customer purchase behavior (before engaging in the OBC) foretells OBC participation. We did so by estimating a probit regression to assess the probability of being an OBC member. The result (Column 2 of Panel B in Table M1) indicates that customer purchase frequency is a relatively poor predictor of OBC participation (p > 0.1). Furthermore, following Wies and Moorman’s (2015) approach for testing the potential reverse causality, we identified customers that only have a low probability (0.4 or lower) of participating in the OBC but are members nevertheless. We built a dummy variable UPART (unanticipated participation) that is equal to 1 if a customer I unexpectedly participates in the OBC at time t, and 0 otherwise. We regressed the variable customer purchase frequency on UPART. We found that the parameter corresponding to the effect of customer purchase frequency is not significant (Column 3 of Panel B in Table M1), suggesting that high purchase frequency does not induce customer participation in the OBC. The results replicated with a cutoff of 0.5 and 0.3 (Columns 4 and 5 of Panel B in Table M1), respectively. Hence, there is no evidence that customer purchase has reverse causality of participation in OBC.

## General Discussion

This study reveals that chronic RF can be identified from secondary data in the digital age. We first classified a sample of customers as being either promotion-focused or preventionfocused, via a text mining method we refer to as RF discovery. Through a field survey, we then demonstrated the accuracy of our method. Further, through econometric analysis, we found that promotion-focused customers purchased more frequently after they joined OBC but did not find that the purchase frequency of prevention-focused customers decreased significantly after joining OBC. The potential reasons are as follows. First, as we learn from RFT, preventionfocused customers are more sensitive to negative information, indicating that information of this kind has an exaggerated bias effect on them (Keller 2012). However, our in-depth analysis showed that most of the information in OBC relating to product appraisals is relatively positive, thus significantly alleviating the effect of negative bias among preventionfocused customers. We collected 1,500 discussion threads concerning products posted on the brand community website and analyzed their sentiment, among which we found that 85.52% of the discussion threads are positive, 11.15% of them are neutral, and only 3.33% are negative. Second, the specific research context may also result in the unexpected results. Specifically, since the given company does not sell premiumbranded apparel, it is understandable that customer involvement is not very pronounced so that the bias effect of negative information decreases. In other words, the effect of negative information bias on customers’ information processing or decision making is more significant when customers are highly involved in product evaluation. Next, we elaborate on the implications and limitations of our study as well as future research directions.

## Theoretical Contributions

The operationalization of RFT is the main contribution of this study, which has several significant theoretical implications as follows. First, we develop an innovative method to operationalize customer RF based on text mining we refer to as RF discovery. Our study stresses the enhancement of a wellknown theory by operationalizing it in an e-commerce context, leading to the new approach that serves both research and business purposes. In particular, past studies examining RFT generally gathered data on subjective responses by manipulating people’s RF using scenarios (e.g., Yoon et al. 2012) or measuring their RF using various psychological scales, as found in a comprehensive review by Haws et al. (2010). These methods are difficult to apply in the digital age, such as in the e-commerce context (Luo et al. 2014; Xu et al. 2014). Our study has strong theoretical implications because it expands the applicability of a well-known social science theory by means of data science.

Second, we believe that this study is a particular instance of design science research according to the seminal work by

Hevner et al. (2004). Our work enhances the variety of design research models by integrating behavioral science and data science tightly into a unique IT artifact, which may be described as a theory-driven invention study. By tight integration, we mean that, on one hand, RFT as a behavioral theory directs the RF discovery method and, on the other hand, the RF discovery method elevates the application scope of RFT. We hope that this unique invention study will inspire more efforts in the future to integrate behavioral science and design science. Consequently, our study does have theoretical implications from the design angle of research.

Third, the successful identification of an instrumental variable contributes to the application domain of econometric analysis to social media research. We were able to validate that review intensity is a good instrumental variable in the context of OBC that is embedded in an e-commerce platform operated by a single firm. Our empirical analyses demonstrated that review intensity is correlated with OBC participation but uncorrelated with customer purchase patterns as detailed in the “Instrumental Variable Specification” subsection; our modeling and testing efforts follow the theoretical guidance of instrumental variable identification (e.g., Ichimura and Taber 2001; Suarez et al. 2013). This contribution has instrumental value to future studies in social media and e-commerce.

## Practical Implications

Although a considerable number of studies (e.g., Lee and Aaker 2004), have revealed the significant effects of customer RF on their behavior, these studies have mainly relied on surveys to identify customers as either promotion- or prevention-focused. Compared with survey methods, our approach has several advantages in practical applications. First, our approach can be scaled up to extremely large numbers of customers because our RF discovery method can detect directly individual RF based on customer behavioral data as opposed to relying on customer surveys, which are difficult to scale up. For example, Amazon<sup>3</sup> had 310 million active customers in the first quarter of 2016. Supposing only 20% of customers post reviews,<sup>4</sup> we could detect RF for around 62 million customers using our ORF approach, which is impossible to do by means of surveys. To boost customer contribution, researchers such as Bateman et al. (2011) and Goes et al. (2014) proposed a series of interesting strategies to effectively stimulate customers to leave more product comments in online community. In addition, a survey reported by BrightLocal in 2017<sup>5</sup> revealed that the ratio of customers who were willing to leave reviews reached as high as 68%. These relevant findings from consumer survey and academic research further strengthen the value of ORF. Second, the RF discovery method we develop allows companies to identify RF of a large number of customers efficiently while removing tedious tasks for questionnaire handling in traditional survey approaches. Consequently, our RF discovery method has the advantage of reducing costs and delays, thus providing management a more cost-effective instrument to understand customers with data science. Third, another important advantage of our approach is that ORF typically operates outside of individuals’ awareness and control; thus, individuals are not burdened to provide accurate self-awareness of their RF. Further, using surveys to study customer RF may suffer from inherent risks of retrospective bias (Gamache et al. 2015). Our approach, which is an implicit and indirect method, bypasses this bias problem (Uhlmann et al. 2012).

The identification of customers’ RF has significant practical impacts for effective marketing. For instance, Jain et al. (2007) demonstrated that the promotion- and preventionfocused participants in their study react differently to negative versus positive framing in brand advertising. In light of this, an e-commerce company could send promotion-focused customers more sales information that emphasizes a product’s positive aspects; conversely, for prevention-focused customers, the firm could use framing that focuses on how its product avoids the disadvantages of rivals’ products. Our study provides an effective way to automatically identify customers as promotion- or prevention-focused; this method could help firms classify their customers into these different categories, which would help improve firm performance under an appropriate marketing strategy.

Moreover, this study has practical implications for OBCs. Our study shows that firm-sponsored OBCs do play a significant role in influencing customer value. They can be used by firms not only to disseminate product information rapidly and cocreate value with customers, but also to improve company profit by enhancing purchase frequency. Therefore, firms should try to initiate OBCs strategically and encourage customers to engage with them. However, OBCs are not a silver bullet. Our results suggest that participation in OBCs does not affect, or may even have a negative impact on, the purchase frequency of prevention-focused customers. Therefore, managers need to understand that not all customers will have the same response to their marketing efforts. To deal with this issue, firms should segment customers when implementing OBC marketing strategies and target promotionfocused customers who tend to purchase more frequently after joining an OBC.

## Limitations and Future Research Directions

Some caveats of this study must be noted. First, during the identification of the customers’ RF by the RF discovery method we develop, nearly one in eight individuals are misclassified. As discussed earlier, the shortcomings of the sentiment analysis technique itself and the potential response bias in the field environment (caused by contextual factors) are possible reasons. Thus, we call for future studies in a similar vein but in a controlled lab environment to see if a better result is possible. In addition, we acknowledge that although it is a rare case, the RF discovery method is not effective with classifying customers who have posted only one or two reviews for a defective product while all other customers received good ones for the same type of product.

Second, our approach is shown to be effective with classifying customers who leave comments. As data science studies always need input data for analysis, such data requirements limit their application boundary. Moreover, as mentioned in the “Theoretical Contributions” section, individuals’ RF can differ in cognitive and affective dimensions. Instead of focusing on product reviews and individual emotional evaluation, future research can extend this study by exploring the possibility of identifying RF via the cognitive dimension (Higgins 2000; Kirmani et al. 2007; Lee et al. 2010).

Third, scholars argue that theory can be of different types; for example, it may be a theory for explaining, for predicting, or for explaining and predicting (Gregor 2006). Although this study extends the application of RFT via data science, we use the explanatory model in the analysis (Shmueli 2010), while leaving room for exploration on whether the RFT can be both explanatory and predictive through the building of predictive analytical models (Shmueli and Koppius 2011).

Fourth, although we have successfully validated the ORF approach by using an econometric model, marketing-oriented research questions, such as when or how the effect of customers’ RF can be most manifested in their purchase decisions, are under explored in this study as our focus in this paper is mainly on information systems issues. Future research can be done to extend ORF applications to marketing science research by joint efforts between information systems researchers and marketing researchers.

## Concluding Remarks

The digital era has brought unprecedented opportunities to researchers on data-centric studies. With big data, social science theories that are developed from surveys or experiments can now be extended to real-world online settings. By taking advantage of plentiful data and with the support of data analytics, this paper has developed an innovative method to operationalize regulatory focus and utilize the operationalized regulatory focus to study customer purchase behavior in the e-commerce context. In addition to contributing to regulatory focus theory, this study has also exemplified how researchers can take advantage of secondary data in their research and how to bridge between survey data and secondary data, which is increasingly required of researchers in this ever expanding digital age.

## Acknowledgments

The authors gratefully acknowledge the numerous invaluable comments and suggestions from the senior editor, associate editor, and four anonymous reviewers. This work is partially supported by research grants from National Natural Science Foundation of China (No. 71601190; No. 71771196; No. 71401154; No. 71471157; No. 71821002), research grants from Research Grants Council of Hong Kong (CityU 11504515; CityU 11508517), and strategic research grant (7004778) from City University of Hong Kong.

## References

Aaker, J. L., and Lee, A. Y. 2006. “Understanding Regulatory Fit,” Journal of Marketing Research (43:1), pp. 15-19.

Abbasi, A., Chen, H., and Salem, A. 2008. “Sentiment Analysis in Multiple Languages: Feature Selection for Opinion Classification in Web Forums,” ACM Transactions on Information Systems (26:3), pp. 1-34.

Adjei, M. T., Noble, S. M., and Noble, C. H. 2010. “The Influence of C2C Communications in Online Brand Communities on Customer Purchase Behavior,” Journal of the Academy of Marketing Science (38:5), pp. 634-653.

Algesheimer, R., Borle, S., Dholakia, U. M., and Singh, S. S. 2010. “The Impact of Customer Community Participation on Customer Behaviors: An Empirical Investigation,” Marketing Science (29:4), pp. 756-769.

Anderson, E. T., and Simester, D. I. 2014. “Reviews Without a Purchase: Low Ratings, Loyal Customers, and Deception,” Journal of Marketing Research (51:3), pp. 249-269.

Arnold, M. J., Reynolds, K. E., Jones, M. A., Tugut, M., and Gabler, C. B. 2014. “Regulatory Focus Intensity and Evaluations of Retail Experiences,” Psychology & Marketing (31:11), pp. 958-975.

Basiri, M. E., Ghasem-Aghaee, N., and Naghsh-Nilchi, A. R. 2014. “Exploiting Reviewers’ Comment Histories for Sentiment Analysis,” Journal of Information Science (40:3), pp. 313-328.

Bateman, P. J., Gray, P. H., and Butler, B. S. 2011. “Research Note-the Impact of Community Commitment on Participation in Online Communities,” Information Systems Research (22:4), pp. 841-854.

Benbasat, I. 1989. “Laboratory Experiments in Information Systems Studies with a Focus on Individuals: A Critical Appraisal,” in The Information Systems Research Challenge: Experimental Research Methods, I. Benbasat (ed.), Boston: Harvard Business School, pp. 33-47.

Berger, C. R. 1987. “Communicating under Uncertainty,” in Interpersonal Processes: New Directions in Communication Research, M. E. Roloff, G. R. Miller, M. E. Roloff, and G. R. Miller (eds.), Thousand Oaks, CA: SAGE Publications, pp. 39-62.

Berger, J. 2014. “Word of Mouth and Interpersonal Communication: A Review and Directions for Future Research,” Journal of Consumer Psychology (24:4), pp. 586-607.

Bolton, R. N., and Lemon, K. N. 1999. “A Dynamic Model of Customers’ Usage of Services: Usage as an Antecedent and Consequence of Satisfaction,” Journal of Marketing Research (36:2), pp. 171-186.

Brockner, J., and Higgins, E. T. 2001. “Regulatory Focus Theory: Implications for the Study of Emotions at Work,” Organizational Behavior and Human Decision Processes (86:1), pp. 35-66.

Chelmis, C., and Prasanna, V. K. 2013. “Social Link Prediction in Online Social Tagging Systems,” ACM Transactions on Information Systems (31:4), pp. 1-27.

Chen, H. 2011. “Sentiment Analysis,” in Dark Web: Exploring and Data Mining the Dark Side of the Web, New York: Springer Science & Business Media.

Chen, H., Chiang, R. H. L., and Storey, V. C. 2012. “Business Intelligence and Analytics: From Big Data to Big Impact,” MIS Quarterly (36:4), pp. 1165-1188.

Chernev, A. 2004. “Global Orientation and Consumer Preference for the Status Quo,” Journal of Consumer Research (30:3), pp. 557-565.

Conlon, E., Devaraj, S., and Matta, K. F. 2001. “The Relationship between Initial Quality Perceptions and Maintenance Behavior: The Case of the Automotive Industry,” Management Science (47:9), pp. 1191-1202.

Crowe, E., and Higgins, E. T. 1997. “Regulatory Focus and Strategic Inclinations: Promotion and Prevention in Decision-Making,” Organizational Behavior and Human Decision Processes (69:2), pp. 117-132.

Cunningham, W. A., Raye, C. L., and Johnson, M. K. 2005. “Neural Correlates of Evaluation Associated with Promotion and Prevention Regulatory Focus,” Cognitive, Affective, & Behavioral Neuroscience (5:2), pp. 202-211.

Das, S. R., and Chen, M. Y. 2007. “Yahoo! for Amazon: Sentiment Extraction from Small Talk on the Web,” Management Science (53:9), pp. 1375-1388.

De, P., Hu, Y., and Rahman, M. S. 2013. “Product-Oriented Web Technologies and Product Returns: An Exploratory Study,” Information Systems Research (24:4), pp. 998-1010.

Dellarocas, C., and Narayan, R. 2006. “A Statistical Measure of a Population’s Propensity to Engage in Post-Purchase Online Word-of-Mouth,” Statistical Science (21:2), pp. 277-285.

Eggers, J. P., and Kaplan, S. 2009. “Cognition and Renewal: Comparing CEO and Organizational Effects on Incumbent Adaptation to Technical Change,” Organization Science (20:2), pp. 461-477.

Florack, A., Keller, J., and Palau, J. 2013. “Regulatory Focus in Economic Contexts,” Journal of Economic Psychology (38), pp. 127-137.

Gamache, D. L., McNamara, G., Manner, M. J., and Johnson, R. E. 2015. “Motivated to Acquire? The Impact of CEO Regulatory Focus on Firm Acquisitions,” Academy of Management Journal (58:4), pp. 1261-1282.

Godes, D., and Silva, J. C. 2012. “Sequential and Temporal Dynamics of Online Opinion,” Marketing Science (31:3), pp. 448-473.

Goes, P. B., Lin, M., and Au Yeung, C.-M. 2014. “‘Popularity Effect’ in User-Generated Content: Evidence from Online Product Reviews,” Information Systems Research (25:2), pp. 222-238.

Goh, K.-Y., Heng, C.-S., and Lin, Z. 2013. “Social Media Brand Community and Consumer Behavior: Quantifying the Relative Impact of User- and Marketer-Generated Content,” Information Systems Research (24:1), pp. 88-107.

Gregor, S. 2006. “The Nature of Theory in Information Systems,” MIS Quarterly (30:3), pp. 611-642.

Gregor, S., and Hevner, A. R. 2013. “Positioning and Presenting Design Science Research for Maximum Impact,” MIS Quarterly (37:2), pp. 337-355.

Gross, J. J., and John, O. P. 2003. “Individual Differences in Two Emotion Regulation Processes: Implications for Affect, Relationships, and Well-Being,” Journal of Personality and Social Psychology (85:2), pp. 348-362.

Hart, W., Albarracín, D., Eagly, A. H., Brechan, I., Lindberg, M. J., and Merrill, L. 2009. “Feeling Validated Versus Being Correct: A Meta-Analysis of Selective Exposure to Information,” Psychological Bulletin (135:4), pp. 555-588.

Hashem, I. A. T., Yaqoob, I., Anuar, N. B., Mokhtar, S., Gani, A., and Khan, S. U. 2015. “The Rise of ‘Big Data’ on Cloud Computing: Review and Open Research Issues,” Information Systems (47), pp. 98-115.

Haws, K. L., Dholakia, U. M., and Bearden, W. O. 2010. “An Assessment of Chronic Regulatory Focus Measures,” Journal of Marketing Research (47:5), pp. 967-982.

Heckman, J. 1979. “Sample Selection Bias as a Specification Error,” Econometrica (47:1), pp. 153-161.

Heckman, J. 1997. “Instrumental Variables: A Study of Implicit Behavioral Assumptions Used in Making Program Evaluations,” Journal of Human Resources (32:3), pp. 441-462.

Hevner, A. R., March, S. T., Park, J., and Ram, S. 2004. “Design Science in Information Systems Research,” MIS Quarterly (28:1), pp. 75-105.

Higgins, E. T. 1997. “Beyond Pleasure and Pain,” American Psychologist (52:12), p. 1280.

Higgins, E. T. 1998. “Promotion and Prevention: Regulatory Focus as a Motivational Principle,” Advances in Experimental Social Psychology (30), pp. 1-46.

Higgins, E. T. 2000. “Making a Good Decision: Value from Fit,” American Psychologist (55:11), pp. 1217-1230.

Higgins, E. T., Shah, J., and Friedman, R. 1997. “Emotional Responses to Goal Attainment: Strength of Regulatory Focus as Moderator,” Journal of Personality and Social Psychology (72:3). pp. 515-525.

Huang, Q., Nijs, V. R., Hansen, K., and Anderson, E. T. 2012. “Wal-Mart’s Impact on Supplier Profits,” Journal of Marketing Research (49:2), pp. 131-143.

Ichimura, H., and Taber, C. 2001. “Propensity-Score Matching with Instrumental Variables,” American Economic Review (91:2), pp. 119-124.

Iyengar, R., Van den Bulte, C., and Valente, T. W. 2011. “Opinion Leadership and Social Contagion in New Product Diffusion,” Marketing Science (30:2), pp. 195-212.

Jain, S. P., Lindsey, C., Agrawal, N., and Maheswaran, D. 2007. “For Better or for Worse? Valenced Comparative Frames and Regulatory Focus,” Journal of Consumer Research (34:1), pp. 57-65.

Keller, J. 2008. “On the Development of Regulatory Focus: The Role of Parenting Styles,” European Journal of Social Psychology (38:2), pp. 354-364.

Keller, J. 2012. “Differential Gender and Ethnic Differences in Math Performance: A Self-Regulatory Perspective,” Journal of Psychology (220:3), pp. 164-171.

Kirmani, A., and Zhu, R. 2007. “Vigilant against Manipulation: The Effect of Regulatory Focus on the Use of Persuasion Knowledge,” Journal of Marketing Research (44:4), pp. 688-701.

Lam, L., and Suen, S. Y. 1997. “Application of Majority Voting to Pattern Recognition: An Analysis of Its Behavior and Performance,” IEEE Transactions on Systems, Man, and Cybernetics– Part A: Systems and Humans (27:5), pp. 553-568.

Lee, A. Y., and Aaker, J. L. 2004. “Bringing the Frame into Focus: The Influence of Regulatory Fit on Processing Fluency and Persuasion,” Journal of Personality and Social Psychology (86:2), pp. 205-218.

Lee, A. Y., Aaker, J. L., and Gardner, W. L. 2000. “The Pleasures and Pains of Distinct Self-Construals: The Role of Interdependence in Regulatory Focus,” Journal of Personality and Social Psychology (78:6), pp. 1122-1134.

Lee, A. Y., Keller, P. A., and Sternthal, B. 2010. “Value from Regulatory Construal Fit: The Persuasive Impact of Fit between Consumer Goals and Message Concreteness,” Journal of Consumer Research (36:5), pp. 735-747.

Li, X., and Hitt, L. M. 2008. “Self-Selection and Information Role of Online Product Reviews,” Information Systems Research (19:4), pp. 456-474.

Liu, B. 2012. Sentiment Analysis and Opinion Mining: Synthesis Lectures on Human Language Technologies, Morgan & Claypool Publishers.

Liu, Z., and Brockner, J. 2015. “The Interactive Effect of Positive Inequity and Regulatory Focus on Work Performance,” Journal of Experimental Social Psychology (57), pp. 111-116.

Louro, M. J. S., Pieters, R., and Zeelenberg, M., 2005. “Negative Returns on Positive Emotions: The Influence of Pride and Self-

Regulatory Goals on Repurchase Decisions,” Journal of Consumer Research (31:4), pp. 833-840.

Luo, X., Andrews, M., Fang, Z., and Phang, C. W. 2014. “Mobile Targeting,” Management Science (60:7), pp. 1738-1756.

Muniz Jr., A. M., and O’Guinn, T. C. 2001. “Brand Community,” Journal of Consumer Research (27:4), pp. 412-432.

Nitzan, I., and Libai, B. 2011. “Social Effects on Customer Retention,” Journal of Marketing (75:6), pp. 24-38.

Norris, C. J., Larsen, J. T., Crawford, L. E., and Cacioppo, J. T. 2011. “Better (or Worse) for Some Than Others: Individual Differences in the Positivity Offset and Negativity Bias,” Journal of Research in Personality (45:1), pp. 100-111.

Pennebaker, J. W., Mehl, M. R., and Niederhoffer, K. G. 2003. “Psychological Aspects of Natural Language Use: Our Words, Our Selves,” Annual Review of Psychology (54:1), pp. 547-577.

Pham, M. T., and Chang, H. 2010. “Regulatory Focus, Regulatory Fit, and the Search and Consideration of Choice Alternatives,” Journal of Consumer Research (37:4), pp. 626-640.

Rhee, E., and Fiss, P. 2014. “Framing Controversial Actions: Regulatory Focus, Source Credibility, and Stock Market Reaction to Poison Pill Adoption,” Academy of Management Journal (57:6), pp. 1734-1758.

Rishika, R., Janakiraman, R., Kumar, A., and Bezawada, R. 2013. “The Effect of Customers’ Social Media Participation on Customer Visit Frequency and Profitability: An Empirical Investigation,” Information Systems Research (24:1), pp. 108-127.

Scherer, A., Wünderlich, N. V., and Von Wangenheim, F. 2015. “The Value of Self-Service: Long-Term Effects of Technology-Based Self-Service Usage on Customer Retention,” MIS Quarterly (39:1), pp. 177-200.

Shmueli, G. 2010. “To Explain or to Predict?,” Statistical Science (25:3), pp. 289-310.

Shmueli, G., and Koppius, O. R. 2011. “Predictive Analytics in Information Systems Research,” MIS Quarterly (35:3), pp. 553-572.

Stieglitz, S., and Dang-Xuan, L. 2013. “Emotions and Information Diffusion in Social Media: Sentiment of Microblogs and Sharing Behavior,” Journal of Management Information Systems (29:4), pp. 217-247.

Suarez, F. F., Cusumano, M. A., and Kahl, S. J. 2013. “Services and the Business Models of Product Firms: An Empirical Analysis of the Software Industry,” Management Science (59:2), pp. 420-435.

Thelwall, M., Buckley, K., Paltoglou, G., Cai, D., and Kappas, A. 2011. “Sentiment in Short Strength Detection Informal Text,” Journal of the American Society for Information Science and Technology (61:12), pp. 2544-2558.

Thompson, S. A., and Sinha, R. K. 2008. “Brand Communities and New Product Adoption: The Influence and Limits of Oppositional Loyalty,” Journal of Marketing (72:6), pp. 65-80.

Uhlmann, E. L., Leavitt, K., Menges, J. I., Koopman, J., Howe, M., and Johnson, R. E. 2012. “Getting Explicit About the Implicit: A Taxonomy of Implicit Measures and Guide for Their Use in Organizational Research,” Organizational Research Methods (15:4), pp. 553-601.

Vaish, A., Grossmann, T., and Woodward, A. 2008. “Not All Emotions Are Created Equal: The Negativity Bias in Social-

Emotional Development,” Psychological Bulletin (134:3), pp. 383-403.

Van de Ven, A. H. 1989. “Nothing Is Quite So Practical as a Good Theory,” Academy of Management Review (14:4), pp. 486-489.

Van de Vijver, F. J. R., and Leung, K. 1997. Methods and Data Analysis for Cross-Cultural Research, Thousand Oaks, CAL: SAGE Publications, Inc.

Wang, J., and Lee, A. Y. 2006. “The Role of Regulatory Focus in Preference Construction,” Journal of Marketing Research (43:1), pp. 28-31.

Werth, L., and Foerster, J. 2007. “How Regulatory Focus Influences Consumer Behavior,” European Journal of Social Psychology (37:1), pp. 33-51.

Wies, S., and Moorman, C. 2015. “Going Public: How Stock Market Listing Changes Firm Innovation Behavior,” Journal of Marketing Research (52:5), pp. 694-709.

Xie, Y., Chen, Z., Zhang, K., Cheng, Y., Honbo, D. K., Agrawal, A., and Choudhary, A. N. 2014. “Muses: Multilingual Sentiment Elicitation System for Social Media Data,” IEEE Intelligent Systems (29:4), pp. 34-42.

Xu, J., Benbasat, I., and Cenfetelli, R. T. 2014. “The Nature and Consequences of Trade-Off Transparency in the Context of Recommendation Agents,” MIS Quarterly (38:2), pp. 379-406.

Yen, C. L., Chao, S. H., and Lin, C. Y. 2011. “Field Testing of Regulatory Focus Theory,” Journal of Applied Social Psychology (41:6), pp. 1565-1581.

Yeo, J., and Park, J. 2006. “Effects of Parent-Extension Similarity and Self Regulatory Focus on Evaluations of Brand Extensions,” Journal of Consumer Psychology (16:3), pp. 272-282.

Yin, D., Bond, S. D., and Zhang, H. 2014. “Anxious or Angry: Effects of Discrete Emotions on the Perceived Helpfulness of Online Reviews,” MIS Quarterly (38:2), pp. 539-560.

Yoon, Y., Sarial-Abi, G., and Gürhan-Canli, Z. 2012. “Effect of Regulatory Focus on Selective Information Processing,” Journal of Consumer Research (39:1), pp. 93-110.

Zhao, G., and Pechmann, C. 2007. “The Impact of Regulatory Focus on Adolescents’ Response to Anti-Smoking Advertising Campaigns,” Journal of Marketing Research (44:4), pp. 671-687.

Zheng, Z., and Padmanabhan, B. 2007. “Constructing Ensembles from Data Envelopment Analysis,” INFORMS Journal on Computing (19:4), pp. 486-496.

## About the Authors

Ji Wu is an associate professor in the Business School at Sun Yatsen University. His research interests focus on electronic commerce, healthcare information technology, and big data analytics. His work has appeared in Information & Management and International Journal of Electronic Commerce, among others.

Liqiang Huang is an associate professor of Information Systems at Zhejiang University. His research interests include digital commerce, consumer behavior, and cloud computing. His work has appeared Journal of Management Information Systems and Journal of the Association for Information Systems, and others.

J. Leon Zhao is Chair Professor of Information Systems, College of Business at the City University of Hong Kong. His research is on information technology and management with a current focus on financial technology and financial services, blockchain technology and applications, business analytics, and information security. His research has appeared in such journals as Management Science, MIS Quarterly, Information Systems Research, INFORMS Journal on Computing, IEEE Transactions, and ACM Transactions.

# OPERATIONALIZING REGULATORY FOCUS IN THEDIGITAL AGE: EVIDENCE FROM ANE-COMMERCE CONTEXT

Ji Wu Business School, Sun Yat-sen University, Guangzhou, CHINA {wugide@gmail.com}

Liqiang Huang

School of Management, Zhejiang University, Hangzhou, CHINA {huanglq@zju.edu.cn}

J. Leon Zhao

College of Business, City University of Hong Kong, Hong Kong, CHINA {jlzhao@cityu.edu.hk}

## Appendix A

## Develop a Sentiment Lexicon

We preprocessed the reviews using the Institute of Computing Technology of the Chinese Academy of Sciences’ system to decompose them into words and phrases. The sentiment lexicon was developed in two steps. First, we selected words and phrases from the reviews, which were also entries in the Chinese Network Sentiment Dictionary and the NTU Sentiment Dictionary. In this way, we collected 167 positive emotion words and 102 negative emotion words. Second, we coded each positive (negative) emotion word and assigned a sentiment strength with values ranging from 2 (-2) to 5 (-5)<sup>1</sup>. After a 30-word (15 positive emotion words and 15 negative emotion words) trial run and performance check of its capability of ensuring consistent perceptions of the words’ sentiment strength, two professional coders examined every word in our lexicon (the training words excluded) and independently assigned them sentiment values. We used Krippendorff’s R (the ordinal version of Cohen’s kappa agreement test) to ensure inter-coder reliability. The reliability coefficients for both the positive and negative emotion words were greater than 0.7 (Archak et al. 2011), suggesting a reasonably high level of consistency across the two coders. After they completed the independent coding, the two coders discussed the discrepancies in order to reach a mutually agreed coding for all words.

## Appendix B

## The Performance of the Customized SentiStrength Algorithm

In this step, three coders were given verbal instruction and training with 100 product reviews. After verifying that the coders had a consistent perspective on the sentiments in the data, they were asked to code 1,000 online reviews independently based on the degree of positive and negative emotions contained in the reviews. The Krippendorff’s R was taken as the inter-coder reliability statistic. Using the numerical difference in the emotion scores as weights, the reliability values were 0.725 for positive and 0.693 for negative sentiment, indicating adequate agreement. We used the majority rule to resolve disagreements among the coders. The customized SentiStrength algorithm was then tested on the same set of 1,000 online reviews that had been classified by the three coders. It is worth noting that our SentiStrength algorithm uses a directory of sentiment words with associated strength measures. During the development of the customized SentiStrength algorithm, we initially obtained sentiment word strengths based on human judgments. In order to optimize the default manual word strengths, we also used a training algorithm (i.e., supervised learning) to fine-tune the sentiment word strengths. The training algorithm started with the baseline human-allocated word strengths for the predefined list and then checked each word strength to see whether an increase or decrease of 1 would improve classification accuracy for the set of 1,000 reviews that had been classified manually (i.e., the training data). The algorithm repeated until all words were checked without making any changes.

## Appendix C

## Comparison between Customized SentiStrength and SVM

Applied approaches for sentiment analysis can be classified into two categories: machine learning and semantic approach. In our main analysis, we adopted the customized SentiStrength algorithm, which is a semantic approach, to perform sentiment classification of online reviews. In the following, we introduce how the machine learning approach is performed, and present a comparison of the performance of machine learning and semantic approaches.

The machine learning approach aims to train a sentiment classifier using a labeled corpus. A general framework of sentiment analysis based on machine learning consists of four major phases: data preprocessing, text representation, classification, and evaluation. First, Chinese text processing needs an additional segmentation to break up the text into words (Zeng et al. 2011). For this purpose, we adopted the ICTCLAS system developed by the Institute of Computing Technology of the Chinese Academy of Sciences (http://english.ict.cas.cn/) to generate the segmentation of our online product reviews. After calculating the number of function words and the number of punctuation marks in each review, we deleted stop words and punctuation marks from our text.

In the text representation phase, a vector space model was used for text representation. This model helped to address three issues: feature selection, feature dimension reduction, and feature weight calculation. In feature selection, we considered all four types of features referred to by previous scholars (e.g., Abbasi et al. 2008). They are semantic features (e.g., the number of positive/negative sentiment words obtained based on predefined lexicons), stylistic features (e.g., the number of words, the average number of words in sentences), syntactic features (e.g., the number of punctuation marks, the number of function words), and content-specific features (e.g., words [unigrams], word n-grams [n = 2,3]). We obtained 6,094 features from the online product review dataset. Considering the strategy of selecting high-frequency words having a greater impact on sentiment classification (Pang et al. 2002), we used aggressive initial low-frequency feature reduction and removed all contentspecific features that occurred less than three times in the data. This process left us with 2,233 features. Finally, in order to build a vector space model for text representation, we used the Boolean method to calculate feature weight because the sentiment types seem to be basically determined when some key features occur (Yao et al. 2011, pp. 315-322).

In the classification phase, we adopted a support vector machine (SVM) as the machine learning algorithm for our robustness check, because this method is considered one of the most effective tools for sentiment classification (Abbasi et al. 2008; Pang et al. 2002). Accordingly, we employed SVMTorch, which deals directly with multi-class classification problems to conduct experiments (http://bengio.abracadoudou.com SVMTorch.html). Based on the 1,000 manually labeled online reviews, tenfold cross-validation was used to train and test the SVM classifier. To evaluate the performance of the sentiment analysis approach on the basis of machine learning, we used two most widely used criteria, namely, macro-average and accuracy (Ghamrawi and McCallum 2005; Thelwall et al. 2011). Macro-average was utilized to measure the performance of positive and negative classes respectively, while accuracy was used to evaluate the overall performance of sentiment classification. The empirical results indicated that the macro-average of the sentiment analysis approach based on machine learning reached 0.739 and 0.687 for negative and positive class, respectively. Accuracy reached 75.51%.

This comparison of the performance of machine learning and semantic approaches shows that the customized SentiStrength algorithm is more accurate than the SVM. The result is consistent with previous findings, which show that semantic sentiment analysis can obtain impressive accuracy when it is equipped with a high-quality lexicon (Thelwall et al. 2011; Waila et al. 2012). Accordingly, the customized SentiStrength algorithm is a good choice for this work.

## Appendix D

## Checking the Negativity Bias in Sentiment Strength of Online Reviews

Our comprehensive review of the extant literature shows that negativity bias (Godes and Silva 2012; Li and Hitt 2008; Moe and Schweidel 2012) is an important factor that must be considered in studying online reviews. With regard to negativity bias, both temporal and sequential effects are considered. Li and Hitt (2008) used time as their primary variable and examined negativity bias in the temporal process of review ratings, while Wu and Huberman (2008) looked into the sequential position of the reviews (i.e., how many reviews have already been submitted at time t) to uncover the negativity bias. Further, Godes and Silva (2012) integrated these two studies and investigated both the temporal process and sequential effects of online review ratings. Following Godes and Silva, we developed two variables: Time, which indicates how much time has elapsed since the first review, and Sequence, which indicates the position of the review in the sequence of reviews for a specifi product. Figure D1 presents the data aggregated across reviews for each value of Time and Sequence. The figure shows that sentiment reflected in online reviews is stable and there is no negativity bias.

![](/api/attachments/TMYVF8QN/fulltext/images/597c7a2fe946fa7d381fbad3e8586c804f714d8ad8aa7b4c89edcfda8a4adb36.jpg)  
Figure D1. A “Model-Free” View of the Data

![](/api/attachments/TMYVF8QN/fulltext/images/183df202ef75533f5961256f711cc1d5d2be0c3e3b547e64ed24e7bc259cd04a.jpg)

We also used a multivariate approach to double check the robustness of the findings. Specifically, we estimated models in which the dependent variable was the sentiment strength (SenStr)—positive sentiment strength (PosSenStr) and negative sentiment strength (NegSenStr)—that was assigned by a reviewer i to an item of product j. The independent variables of interest are Time aiSequencend . We controlled individual-level reviewer heterogeneity by forming a reviewer-level average sentiment strength. The variable RevAvgSen (including PosAvgSen and NegAvgSen) is the average sentiment strength of a customer’s reviews on all items. We also controlled customer purchase and review tenure. A consumer’s purchase tenure is measured as the difference, in months, between the date of review and the date of his/her first purchase, and a consumer’s review tenure refers to the period between first and last review. The variable Year2012 indicates whether the review is generated in 2012. Table D1 shows the descriptive statistics of the variables. Given the discrete and ordered nature of our dependent variable, we specified the models using the ordered logit model:

$$
\begin{array}{r l} S e n S t r _ {i j} = \kappa I (\pi_ {\kappa - 1} & \\ & <   \beta_ {1} R e v A v g S e n _ {1} + \beta_ {2} T i m e _ {i j} + \beta_ {3} S e q u e n c e _ {i j} + \beta_ {4} T e n u r e _ {i j} \\ & + \beta_ {5} Y e a r 2 0 1 2 _ {i j} + \delta_ {j} + _ {i j} \leq \pi_ {\kappa}) \end{array}
$$

where κ denotes the realized value of a sentiment strength ${ \mathfrak { o f } } \kappa \in [ 1 , K ]$ , being the highest sentiment strength allowed; $\pi _ { 1 }$ through $\pi _ { \kappa }$ are cut-off parameters to help identify the intervals; $l ( \cdot )$ is the indicator function, which equals one if @ is true and zero otherwise; $\delta _ { j }$ is the fixed effect of product $; j ;$ and $\varepsilon _ { i j }$ is the error term. Table D2 shows the estimation results.

<table><tr><td colspan="5">Table D1. Descriptive Statistics of Variables for Negativity Bias Analysis</td></tr><tr><td>Variables</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>Review positive sentiment strength ( $SSR_{ijt}^{+}$ )</td><td>3.725</td><td>1.272</td><td>1.000</td><td>5.000</td></tr><tr><td>Review negative sentiment strength ( $SSR_{ijt}^{-}$ )</td><td>-2.129</td><td>0.637</td><td>-5.000</td><td>-1.000</td></tr><tr><td>Time (days since first review)</td><td>94.661</td><td>119.832</td><td>1.000</td><td>595.000</td></tr><tr><td>Sequence (sequential position of reviews)</td><td>41.106</td><td>91.169</td><td>1.000</td><td>619.000</td></tr><tr><td>Purchase tenure (months since first purchase)</td><td>3.212</td><td>2.197</td><td>0.000</td><td>16.000</td></tr><tr><td>Review tenure (months since first review)</td><td>2.5100</td><td>2.066</td><td>0.000</td><td>16.000</td></tr><tr><td>Reviewer positive sentiment strength ( $PosAvgSen_{i}$ )</td><td>3.699</td><td>1.054</td><td>1.000</td><td>5.000</td></tr><tr><td>Reviewer negative sentiment strength ( $NegAvgSen_{i}$ )</td><td>-2.115</td><td>0.461</td><td>-5.000</td><td>-1.000</td></tr></table>

The results in Table D2 show that the coefficients of the variables Time and Sequence are not significant, which indicates that there is no negativity bias in the sentiment of the product reviews in our dataset. This result is consistent with the finding of Vaish et al. (2008), which indicates that individuals’ sentiment in online reviews is stable.

<table><tr><td colspan="5">Table D2. Empirical Results for Sentiment Bias Analysis</td></tr><tr><td rowspan="2">Variable</td><td colspan="2">Positive Sentiment Strength</td><td colspan="2">Negative Sentiment Strength</td></tr><tr><td>Coefficient</td><td>SD</td><td>Coefficient</td><td>SD</td></tr><tr><td>PosAvgSen</td><td>2.733E-01***</td><td>9.073E-02</td><td></td><td></td></tr><tr><td>NegAvgSen</td><td></td><td></td><td>4.843E-01***</td><td>2.423E-01</td></tr><tr><td>Time</td><td>-1.922E-04</td><td>7.742E-04</td><td>1.022E-04</td><td>1.525E-04</td></tr><tr><td>Sequence</td><td>1.346E-04</td><td>2.285E-04</td><td>-1.966E-03</td><td>1.614E-03</td></tr><tr><td>Purchase tenure</td><td>-1.172-02</td><td>9.961E-03</td><td>4.014E-03</td><td>6.003E-02</td></tr><tr><td>Review tenure</td><td>3.507E-02</td><td>1.399E-02</td><td>-6.465E-02</td><td>6.368E-02</td></tr><tr><td>Year 2012</td><td>-3.334E-01***</td><td>9.849E-02</td><td>-7.476E-01*</td><td>4.481E-01</td></tr><tr><td>Customer-fixed</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Product-fixed</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Pseudo-R2</td><td colspan="2">2.261E-01</td><td colspan="2">3.516E-01</td></tr></table>

Notes: \*\*\*p < 0.01, \*p < 0.1

## Appendix E

## The Choice of Threshold Value in the Voting Scheme

We conducted additional analyses in which we improved the threshold of voting scheme gradually. High threshold value might lead to the fact that a majority is not obtained for a customer (i.e., the customer is not classified). We applied the voting scheme in three-ways - one, where customers with no majority are treated as “promotion focused”, reported as type of “vote-pro” in the subsequent figure, and two, where such customers are treated as “prevention focused”, reported as type of “vote-pre” in the subsequent figure, and three, where such customers are discarded, reported as “vote-dis” in the subsequent figure. We took classification results obtained from field survey as gold standard and calculated classification accuracy by changing the threshold value of voting scheme. The results are reported in Figure E1. As observed from the figure, high threshold value improves classification accuracy for the classified customers but degrade the overall classification performance because of its shrank size of the classified sample

In order to prevent degradation due to its shrank size of the classified sample, we employed a state-of-the-art supervised machine learning algorithm, SVM, to classify the customers with no-majority votes, using customers’ demographics (e.g., age) and their sentiment biases in product reviews (e.g., average positive sentiment-strength bias) as features. The subsample of customers who had obtained class label was used to train the SVM algorithm. The results are reported in Table E1. As observed from the table, the overall classification accuracy for the combined method is slightly higher than 85%. In sum, we found the approach of combining the voting scheme with high threshold and SVM algorithm had better performance. However, this combination approach imposes a round of supervised learning phase, which would unnecessarily increase the complexity of our method. In our field survey section, we show that, despite its simplicity, the original majority voting scheme is effective in producing high quality RF classification.

![](/api/attachments/TMYVF8QN/fulltext/images/2add23e2c06cefb2331ffda90a6eec21664b8e4ba3eaca5646efb275a35d3a52.jpg)

Figure E1. Classification Accuracy Versus Threshold Value

<table><tr><td colspan="5">Table E1. The Performance of Combined Method Versus Varying Threshold Value of the Voting Scheme</td></tr><tr><td rowspan="2"></td><td colspan="4">Threshold Value of the Voting Scheme</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Classification Accuracy</td><td>0.863</td><td>0.879</td><td>0.887</td><td>0.871</td></tr></table>

## Appendix F

## Survey Respondents and Selection Bias

Table F1 summarizes the mean value of customer demographics and the average volume of online review activity for non-survey customers and survey respondents. The third column of Table F1 shows the ratio between non-survey customers and survey respondents. We used t-test and Mann-Whitney U-test to compare survey respondents with non-survey customers.

The descriptive statistics in Panel A of Table F1 suggest that demographics (i.e., age, gender, income, urban, and south) of survey respondents are similar to that of non-survey customers. Both t-test and U-test suggest that there are no demographic differences between survey respondents and non-survey customers. Second, we compare online review activity of survey respondents with online review activity of reviewers outside the survey. The results are reported in Panel B of Table F1. We do not observe a significant difference in the average volume of product reviews between the two groups.

Moreover, we use Figure F1 and Figure F2 to show the box plots and histograms of customer characteristic distributions for the two groups: the survey respondents and the non-survey customers. All of the plots reveal that the distributions for survey respondents and for non-survey customers are similar, which further provide evidences that the 124 respondents to our survey do not suffer from biases to selection.

Table F1. Comparing Customer Characteristics of Non-Survey Customers and Survey Respondents

<table><tr><td>Variable</td><td>Non-Survey Mean</td><td>Survey Mean</td><td>Ratio</td><td>t-Test</td><td>U-test</td></tr><tr><td colspan="6">Panel A: Customer Demographics</td></tr><tr><td>Female</td><td>0.768</td><td>0.779</td><td>0.986</td><td>-0.393</td><td>-0.393</td></tr><tr><td>Age</td><td>32.784</td><td>33.000</td><td>0.993</td><td>-0.764</td><td>-0.672</td></tr><tr><td>Income</td><td>2.141</td><td>2.111</td><td>1.014</td><td>0.347</td><td>0.598</td></tr><tr><td>Urban</td><td>0.196</td><td>0.172</td><td>1.133</td><td>0.816</td><td>0.816</td></tr><tr><td>South</td><td>0.781</td><td>0.793</td><td>0.985</td><td>-0.426</td><td>-0.426</td></tr><tr><td colspan="6">Panel B: Customer Review Behavior</td></tr><tr><td>Number of product reviews</td><td>6.637</td><td>7.120</td><td>0.932</td><td>-0.874</td><td>0.893</td></tr></table>

![](/api/attachments/TMYVF8QN/fulltext/images/856618b8214bc912492de7229389f7d04a6fdd17de03067301d0333b1c870d05.jpg)  
(a)

![](/api/attachments/TMYVF8QN/fulltext/images/2ad37a865376a201cc8f55d95d671899e244deefff4836d2063a376a5811d76d.jpg)  
(b)

![](/api/attachments/TMYVF8QN/fulltext/images/e43e0f6da7b937bd0af3eb70e430670d9f31a74d6a2ffd2e6bf6885b2712a960.jpg)  
(a)

![](/api/attachments/TMYVF8QN/fulltext/images/e57e2aeae2beccb7318ebed3cfd20a0c0dc12a46b5fa3f826fca41258b523088.jpg)  
(b)

![](/api/attachments/TMYVF8QN/fulltext/images/7274c6e52686d2f584c7ba2b5cd446619e2f16293d790bca7b9ce55214238afd.jpg)  
(c)

![](/api/attachments/TMYVF8QN/fulltext/images/5f2c6208e4bcfa2c03003042a87111a5d30b52ceaa60d7a434c7f58d13cf6a6f.jpg)  
(d)

(2) We used the procedure proposed by Higgins et al. (1997) to classify the survey respondents into either having a chronic promotion focus or a chronic prevention focus according to the median between their average RF promotion and RF prevention scores. Again, as expected, the chronic promotion-focused group had a higher average positive sentiment bias than the chronic prevention-focused group (mean = 0.15 versus mean = -0.53; t = -3.3, p < 0.01). Similarly, the chronic prevention-focused group had a higher average negative sentiment bias than the chronic promotion-focused group ( mean = 0.13 versus mean = -0.16; t = 2.85, p < 0.01).

## Appendix H

## Propensity Score Matching

We conducted a PSM analysis first by modeling the customers’ community participation decision. We identified a set of exogenous variables as covariates: (1) gender (Female ); (2) age (Age ); (3) a zip code-level estimate of the level of household income (Income ); (4) whether a customer disclosed his/her home address when he/she registered (AddressDisclosed ); (5) whether a customer disclosed his/her telephone number when he/she registered (PhoneDisclosed ); (6) whether a customer disclosed his/her MSN number (MSNDisclosed ) when he/she registered; (7) whether a customer lived in an urban area (Urban ); (8) whether a customer lived in the south of the country (South ); (9) review intensity before participation (ReviewIntensity ), which is measured as the ratio of the number of online product reviews posted by a customer in a certain time period to the number of products bought by the customer in the same time period; and (10) RF. We expected a customer’s community participation to be related to gender, age, income level, and location (Muniz and O’Guinn 2001), because the focal firm is a clothing retailer that mainly sells stylish apparel. We also expected a user, who has made a decision to take part in the OBC, to be affected by concerns over data privacy (Goh et al. 2013). Further, we expected that a customer’s propensity to express his/her opinions on products (ReviewIntensity ) and RF would influence his/her decision to engage in the community. We also examined whether there is a relationship between RF and community participation. The results shown in Table H1 suggest that the community participation behavior of promotionfocused customers differs significantly from that of prevention-focused customers, and that promotion-focused customers are more likely to engage in OBCs than prevention-focused customers.

<table><tr><td colspan="5">Table H1. RF and Community Participation</td></tr><tr><td></td><td>Prevention (Mean)</td><td>Promotion (Mean)</td><td>U-test p-value</td><td>t-test p-value</td></tr><tr><td>Community participation</td><td>0.491</td><td>0.552</td><td>3.097***</td><td>3.100***</td></tr></table>

Note: \*\*\*p < 0.01

With these exogenous variables, we calculated the probability of a customer participating in the OBC with a logistic model formulation. Table H2 shows the estimated logit model. We then performed matching with the optimal pair-matching algorithm. Each treated customer was matched with the most similar non-treated customer (non-participant). We also tested the balancing property of the propensity score to see if the underlying assumptions of the PSM process held. We checked whether the covariates in the logit model differ between the treatment and control observations. The results are reported in Table H3. As seen in the table, the variables used for the PSM were not significantly different across the two groups of customers’ post matching, implying statistical balance. To test whether the common support condition was met, we plotted the propensity score distributions pre- and post-matching of the two groups. Figure H1 describes the kernel density function of the propensity scores of the participation and non-participation groups. It shows that the common support condition is met. As a result of the above procedure, we were able to satisfactorily match treatment customers to a set of control customers, all of whom were included in model estimation next.

<table><tr><td colspan="3">Table H2. Results of Estimated Logit Model</td></tr><tr><td>Variable</td><td>Parameter</td><td>Std. Error</td></tr><tr><td>Female</td><td>0.235***</td><td>0.085</td></tr><tr><td>Age</td><td>-0.044***</td><td>0.013</td></tr><tr><td>Income.2</td><td>0.034</td><td>0.108</td></tr><tr><td>Income.3</td><td>-0.261***</td><td>0.082</td></tr><tr><td>Income.4</td><td>-0.238**</td><td>0.096</td></tr><tr><td>AddressDisclosed</td><td>0.534</td><td>0.498</td></tr><tr><td>PhoneDisclosed</td><td>0.567***</td><td>0.081</td></tr><tr><td>MSNDisclosed</td><td>-0.015</td><td>0.105</td></tr><tr><td>Urban</td><td>0.128*</td><td>0.075</td></tr><tr><td>South</td><td>-0.045</td><td>0.067</td></tr><tr><td>ReviewIntensity</td><td>0.045**</td><td>0.021</td></tr><tr><td>ReguFocus</td><td>0.222***</td><td>0.080</td></tr><tr><td>Constant</td><td>0.457</td><td>0.664</td></tr><tr><td>Pseudo-R2</td><td colspan="2">0.205</td></tr></table>

Notes: $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star \star } p < 0 . 0 1$ . The variable Income is a category variable, and we use Income.2, Income.3, and Income.4 to indicate the different categories of customer income.

Table H3. Summary of Statistics and Covariate Comparison after Matching

<table><tr><td>Variable</td><td>Treatment Group Mean</td><td>Control Group Men</td><td>Mean Difference</td><td>t-test p-value</td></tr><tr><td>Female</td><td>0.800</td><td>0.805</td><td>-0.005</td><td>0.708</td></tr><tr><td>Age</td><td>32.805</td><td>32.880</td><td>-0.075</td><td>0.467</td></tr><tr><td>Income.2</td><td>0.147</td><td>0.140</td><td>0.007</td><td>0.560</td></tr><tr><td>Income.3</td><td>0.096</td><td>0.099</td><td>-0.003</td><td>0.754</td></tr><tr><td>Income.4</td><td>0.236</td><td>0.226</td><td>0.010</td><td>0.508</td></tr><tr><td>AddressDisclosed</td><td>0.996</td><td>0.998</td><td>-0.002</td><td>0.479</td></tr><tr><td>PhoneDisclosed</td><td>0.565</td><td>0.571</td><td>-0.006</td><td>0.793</td></tr><tr><td>MSNDisclosed</td><td>0.216</td><td>0.227</td><td>-0.011</td><td>0.446</td></tr><tr><td>Urban</td><td>0.184</td><td>0.194</td><td>-0.010</td><td>0.506</td></tr><tr><td>South</td><td>0.807</td><td>0.828</td><td>-0.021</td><td>0.135</td></tr><tr><td>ReviewIntensity</td><td>0.310</td><td>0.305</td><td>0.005</td><td>0.755</td></tr><tr><td>ReguFocus</td><td>0.682</td><td>0.667</td><td>0.015</td><td>0.349</td></tr></table>

![](/api/attachments/TMYVF8QN/fulltext/images/9a5e4518450d88c7f24ea5931db6fd5d5607f5b716effb91c8212fca2d187270.jpg)

![](/api/attachments/TMYVF8QN/fulltext/images/26e6bf2eb266c28b0f8e64e7783a08d6951278d473d23fd6b0adae2005635652.jpg)  
(b)  
Figure H1. Kernel Density of Participation and Non-Participation Group

## Appendix I

## Instrumental Variable Specification

In order to theorize the relationships between the instrumental variable (i.e., review intensity) and OBC participation, our review of the literature shows that the main factors that determine people’s propensity to post reviews are self-enhancement (Angelis et al. 2012), information acquisition (Berger 2014), social interaction (Hennig-Thurau et al. 2004), and altruism (Dellarocas and Narayan 2006). Meanwhile, similar factors such as social identity (Bagozzi and Dholakia 2006), information motive (Chang et al. 2013), and relational capital (Casaló et al. 2010) are considered to have the most influence on individuals’ propensity to engage in a brand community. Accordingly, we could learn that individuals’ propensity to either post reviews or engage in a brand community shares the same factors, like social interaction motive, information motive, and self-efficacy motive. Accordingly, evidence is prominent in deducing the correlations between review intensity and OBC participation (relevance assumption).

In addition, scholars have also pointed out that customers’ review propensity, as one of their traits, is not related to their purchase frequency. For instance, Hennig-Thurau et al. (2004) demonstrated empirically that customers’ propensity to post reviews is not influenced by the frequency of product experience. Moreover, in the study of Arnold et al. (2014), the authors have uncovered that customers often generate a number of reviews even if they did not purchase products. Empirically, we found a strong positive relationship between the variable of OBC participation (OBCPart) and review intensity, with an F-statistic value of 17.22. Thus, the review intensity variable satisfies the basic requirement for the instrumental variable to be relevant (Bound et al. 1995). Moreover, according to Stock and Yogo (2005), the weak identification test also indicates that the review intensity is not a weak instrument. Next, we tested the exclusion restriction of our instrumental variable. It seems that this instrument meets the exclusion restriction because it is difficult to think of a direct channel by which review intensity can affect purchase frequency. We tested this assumption by regressing purchase frequency on the review intensity variable and other controls. We found that the coefficient of the estimated review intensity variable is non-significant (the coefficient of the estimate is 0.074, p > 0.1). This indicates that the review intensity variable satisfies the exogeneity requirement of the instrumental variable in our setup (Angrist and Krueger 1999). To summarize, the review intensity is considered a suitable instrumental variable in our study.

The results of our instrument specification are presented in Table I1. Considering the endogenous variable issue, we reported our results incrementally from Model 7 to Model 8. We also divided the sample data set into two subsamples (one group with customers of promotion focus and the other with customers of prevention focus). We then conducted IV estimation for each subsample. The Model 9 column show the result of the IV specification for the prevention-focused customers, and the Model 10 column shows the result of the IV specification for the promotion-focused customers. That is, the results from our IV specification are consistent with the results obtained from DID method, indicating that they are robust.

<table><tr><td colspan="5">Table I1. Instrumental Variable Specification</td></tr><tr><td>Variables</td><td>Model (7)IV for OBCPart</td><td>Model (8)IV for OBCPart,Interaction</td><td>Model (9)IV for OBCPart,Prevention Focus</td><td>Model (10)IV for OBCPart,Promotion Focus</td></tr><tr><td>OBCPart</td><td>0.542**(0.257)</td><td>0.112(0.191)</td><td>-0.333(1.629)</td><td>1.178**(0.506)</td></tr><tr><td>OBCPart × ReguFocus</td><td></td><td>0.095**(0.039)</td><td></td><td></td></tr><tr><td>NeighborPurFreq</td><td>0.0165*(0.009)</td><td>0.012(0.011)</td><td>0.021(0.043)</td><td>0.034*(0.020)</td></tr><tr><td>PromIntensity</td><td>0.295***(0.032)</td><td>0.396***(0.040)</td><td>0.263**(0.121)</td><td>0.321***(0.070)</td></tr><tr><td>log(Price)</td><td>-0.097***(0.017)</td><td>-0.076***(0.019)</td><td>-0.138**(0.064)</td><td>-0.120***(0.036)</td></tr><tr><td>TranFee</td><td>-0.009***(0.002)</td><td>-0.005*(0.002)</td><td>-0.012*(0.0073)</td><td>-0.005(0.006)</td></tr><tr><td>Intercept</td><td>0.438(0.281)</td><td>-0.159(0.231)</td><td>-0.107(1.635)</td><td>0.370(0.402)</td></tr><tr><td>User fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-specific dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Standard errors are in parentheses. \*p < .1, \*\*p < 0.05, \*\*\*p < 0.01.

## Appendix J

Inclusion of Additional Variables and Alternative Matching Algorithm

<table><tr><td colspan="3">Table J1. Results of Estimated Logit Model with Additional Variables</td></tr><tr><td>Variable</td><td>Parameter</td><td>Std. Error</td></tr><tr><td>Female</td><td>0.234***</td><td>0.086</td></tr><tr><td>Age</td><td>-0.044***</td><td>0.013</td></tr><tr><td>Income.2</td><td>-0.058</td><td>0.115</td></tr><tr><td>Income.3</td><td>-0.289**</td><td>0.140</td></tr><tr><td>Income.4</td><td>-0.212**</td><td>0.108</td></tr><tr><td>AddressDisclosed</td><td>0.329</td><td>0.500</td></tr><tr><td>PhoneDisclosed</td><td>0.423***</td><td>0.084</td></tr><tr><td>MSNDisclosed</td><td>-0.009</td><td>0.107</td></tr><tr><td>Urban</td><td>0.145*</td><td>0.083</td></tr><tr><td>South</td><td>-0.072</td><td>0.097</td></tr><tr><td>ReviewIntensity</td><td>0.051**</td><td>0.023</td></tr><tr><td>ReguFocus</td><td>0.204**</td><td>0.082</td></tr><tr><td>EamilValidated</td><td>0.695***</td><td>0.074</td></tr><tr><td>EasMidWes.2</td><td>0.234**</td><td>0.115</td></tr><tr><td>EasMidWes.3</td><td>0.138</td><td>0.162</td></tr><tr><td>Constant</td><td>0.500</td><td>0.669</td></tr><tr><td>Pseudo-R²</td><td colspan="2">0.235</td></tr></table>

Notes: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01. The variable EasMidWes is a category variable.

<table><tr><td>Variables</td><td>Model (11)</td><td>Model (12) Interaction</td><td>Model (13) Prevention Focus</td><td>Model (14) Promotion Focus</td></tr><tr><td>Treated</td><td>0.048(0.045)</td><td>0.047(0.045)</td><td>0.183**(0.079)</td><td>0.157***(0.055)</td></tr><tr><td>OBCPart</td><td>0.041(0.037)</td><td>0.037(0.037)</td><td>0.127*(0.069)</td><td>0.013(0.044)</td></tr><tr><td>Treated × OBCPart</td><td>0.206***(0.053)</td><td>0.081(0.068)</td><td>-0.096(0.098)</td><td>0.329***(0.063)</td></tr><tr><td>Treated × OBCPart × ReguFocus</td><td></td><td>0.162***(0.055)</td><td></td><td></td></tr><tr><td>NeighborPurFreq</td><td>0.069*(0.038)</td><td>0.071*(0.038)</td><td>0.0569(0.078)</td><td>0.083*(0.044)</td></tr><tr><td>PromIntensity</td><td>0.396***(0.040)</td><td>0.400***(0.039)</td><td>0.443***(0.074)</td><td>0.379***(0.047)</td></tr><tr><td>ln(Price)</td><td>-0.075***(0.019)</td><td>-0.075***(0.019)</td><td>-0.075**(0.035)</td><td>-0.072***(0.023)</td></tr><tr><td>TranFee</td><td>-0.005(0.003)</td><td>-0.004(0.003)</td><td>-0.003(0.006)</td><td>-0.007*(0.004)</td></tr><tr><td>Intercept</td><td>-0.114(0.260)</td><td>-0.055(0.261)</td><td>-0.302(0.585)</td><td>-0.086(0.293)</td></tr><tr><td>User fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-specific dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.092</td><td>0.094</td><td>0.134</td><td>0.105</td></tr></table>

Notes: Standard errors in parentheses. \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01

## Appendix K

Purchase Expenditure and Subsample Analysis

<table><tr><td colspan="5">Table K1. OBC Participation and Customer Purchase Expenditure</td></tr><tr><td>Variables</td><td>Model (15)No controls</td><td>Model (16)Controls</td><td>Model (17)Controls, FE, TE</td><td>Model (18)Three-WayDifference</td></tr><tr><td>Treated</td><td>0.105(0.066)</td><td>0.047(0.045)</td><td>0.013(0.044)</td><td>0.012(0.044)</td></tr><tr><td>OBC Part</td><td>0.020(0.052)</td><td>0.085**(0.035)</td><td>0.022(0.037)</td><td>0.018(0.038)</td></tr><tr><td>Treated × OBCPart</td><td>0.255***(0.079)</td><td>0.198***(0.053)</td><td>0.183***(0.053)</td><td>0.097*(0.057)</td></tr><tr><td>ReguFocus</td><td>0.071*(0.039)</td><td>0.029(0.027)</td><td></td><td></td></tr><tr><td>Treated × OBCPart × ReguFocus</td><td></td><td></td><td></td><td>0.124***(0.054)</td></tr><tr><td>NeighborPurFreq</td><td></td><td>0.157***(0.030)</td><td>0.059(0.038)</td><td>0.060(0.038)</td></tr><tr><td>PromIntensity</td><td></td><td>0.375***(0.038)</td><td>0.397***(0.040)</td><td>0.401***(0.039)</td></tr><tr><td>In(Price)</td><td></td><td>1.029***(0.018)</td><td>1.061***(0.019)</td><td>1.062***(0.019)</td></tr><tr><td>TranFee</td><td></td><td>-0.004(0.003)</td><td>-0.006*(0.003)</td><td>-0.005(0.003)</td></tr><tr><td>Intercept</td><td>5.372***(0.048)</td><td>0.323***(0.104)</td><td>-0.064(0.258)</td><td>-0.019(0.259)</td></tr><tr><td>User fixed effects</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-specific dummies</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.108</td><td>0.539</td><td>0.634</td><td>0.655</td></tr></table>

Notes: Standard errors in parentheses. $^ { \star } p < 0 . 1 ; ^ { \star \star } p < 0 . 0 5 ; ^ { \star \star \star } p < 0 . 0 1$

Table K2. Impacts of OBC Participation on Purchase Expenditure Varying with RF

<table><tr><td>Variables</td><td colspan="2">Model (19) Subsample: Prevention Focus</td><td colspan="2">Model (20) Subsample: Promotion Focus</td></tr><tr><td></td><td>Coefficient</td><td>SD</td><td>Coefficient</td><td>SD</td></tr><tr><td>Treated</td><td>0.192***</td><td>0.079</td><td>0.103*</td><td>0.053</td></tr><tr><td>OBCPart</td><td>0.087</td><td>0.069</td><td>0.005</td><td>0.043</td></tr><tr><td>Treatment ×OBCPart</td><td>-0.063</td><td>0.098</td><td>0.278***</td><td>0.063</td></tr><tr><td>NeighborPurFreq</td><td>-0.009</td><td>0.075</td><td>0.077*</td><td>0.044</td></tr><tr><td>PromIntensity</td><td>0.478***</td><td>0.074</td><td>0.369***</td><td>0.047</td></tr><tr><td>ln(Price)</td><td>1.087***</td><td>0.035</td><td>1.051***</td><td>0.023</td></tr><tr><td>TranFee</td><td>-0.001</td><td>0.006</td><td>-0.007*</td><td>0.003</td></tr><tr><td>Intercept</td><td>-0.201</td><td>0.582</td><td>-0.003</td><td>0.291</td></tr><tr><td>User fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Time-specific dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>R2</td><td colspan="2">0.605</td><td colspan="2">0.541</td></tr></table>

Notes: Standard errors in parentheses; \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

<table><tr><td colspan="4">Table K3. Impact of OBC Participation on Customer Purchase Frequency with Subsample</td></tr><tr><td>Variables</td><td>Model (21) Did</td><td>Model (22) Prevention Focus</td><td>Model (23) Promotion Focus</td></tr><tr><td>Treated</td><td>0.088(0.205)</td><td>0.243(0.397)</td><td>0.210(0.246)</td></tr><tr><td>OBCPart</td><td>0.145(0.157)</td><td>0.044(0.289)</td><td>0.240(0.188)</td></tr><tr><td>Treated ×OBCPart</td><td>0.057(0.298)</td><td>-0.387(0.497)</td><td>0.515**(0.236)</td></tr><tr><td>Treated × OBCPart × ReguFocus</td><td>0.313*(0.164)</td><td></td><td></td></tr><tr><td>NeighborPurFreq</td><td>0.437***(0.137)</td><td>-0.119(0.337)</td><td>0.587***(0.144)</td></tr><tr><td>PromIntensity</td><td>0.529***(0.179)</td><td>0.852*(0.475)</td><td>0.536***(0.189)</td></tr><tr><td>In(Price)</td><td>-0.150*(0.084)</td><td>-0.344*(0.186)</td><td>-0.103(0.095)</td></tr><tr><td>TranFee</td><td>-0.001(0.012)</td><td>0.006(0.025)</td><td>-0.001(0.015)</td></tr><tr><td>Intercept</td><td>-0.269(0.486)</td><td>-0.966(1.037)</td><td>-0.323(0.532)</td></tr><tr><td>User fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-specific dummies</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R2^2$ </td><td>0.120</td><td>0.174</td><td>0.193</td></tr></table>

Notes: Standard errors in parentheses. \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

## Appendix L

Inclusion of Customer Satisfaction

<table><tr><td colspan="5">Table L1. Robustness Check of OBC Participation with Delta Purchase</td></tr><tr><td>Variables</td><td>Model (24)</td><td>Model (25) Interaction</td><td>Model (26) Prevention Focus</td><td>Model (27) Promotion Focus</td></tr><tr><td>Treated</td><td>0.023(0.037)</td><td>0.024(0.037)</td><td>0.147**(0.068)</td><td>0.125***(0.045)</td></tr><tr><td>OBCPart</td><td>0.015(0.031)</td><td>0.017(0.031)</td><td>0.023(0.059)</td><td>0.037(0.036)</td></tr><tr><td>Treated × OBCPart</td><td>0.118***(0.044)</td><td>0.095*(0.056)</td><td>-0.038(0.084)</td><td>0.175***(0.053)</td></tr><tr><td>Treated × OBCPart × ReguFocus</td><td></td><td>0.108**(0.046)</td><td></td><td></td></tr><tr><td>DeltaPurchase</td><td>0.994***(0.268)</td><td>0.992***(0.268)</td><td>1.003**(0.507)</td><td>0.987***(0.305)</td></tr><tr><td>NeighborPurFreq</td><td>0.061*(0.032)</td><td>0.061*(0.032)</td><td>0.056(0.066)</td><td>0.061*(0.036)</td></tr><tr><td>PromIntensity</td><td>0.320***(0.035)</td><td>0.322***(0.033)</td><td>0.456***(0.064)</td><td>0.266***(0.039)</td></tr><tr><td>In(Price)</td><td>-0.074***(0.021)</td><td>-0.071***(0.029)</td><td>-0.058*(0.030)</td><td>-0.032***(0.019)</td></tr><tr><td>TranFee</td><td>-0.004(0.003)</td><td>-0.003(0.003)</td><td>-0.003(0.005)</td><td>-0.007**(0.003)</td></tr><tr><td>Intercept</td><td>-0.105(0.220)</td><td>-0.102(0.221)</td><td>-0.935(0.501)</td><td>-0.103(0.246)</td></tr><tr><td>User fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-specific dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.132</td><td>0.135</td><td>0.138</td><td>0.137</td></tr></table>

Notes: Standard errors in parentheses. \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

## Appendix M

## Ruling Out Reverse Causality

<table><tr><td colspan="5">Table M1. The Impact of Purchase Frequency on OBC Participation</td></tr><tr><td colspan="5">Panel A: Average Purchase Frequency Before Participation for Treatment and Control Groups</td></tr><tr><td>Variable</td><td>Treatment Group</td><td>Control Group</td><td>Difference</td><td>t-Test</td></tr><tr><td></td><td>2.282</td><td>2.203</td><td>0.079</td><td>1.286</td></tr><tr><td colspan="5">Panel B: The Impact of Purchase Frequency on Community Participation</td></tr><tr><td>Variable</td><td>First-Step Results</td><td>Cutoff Point = 0.5</td><td>Cutoff Point = 0.4</td><td>Cutoff Point = 0.3</td></tr><tr><td>PriorPurFreq</td><td>0.007(0.009)</td><td>0.014(0.012)</td><td>0.012(0.017)</td><td>0.049(0.051)</td></tr></table>

## References

Abbasi, A., Chen, H., and Salem, A. 2008. “Sentiment Analysis in Multiple Languages: Feature Selection for Opinion Classification in Web Forums,” ACM Transactions on Information Systems (26:3), pp. 1-34.

Angelis, M. D., Bonezzi, A., Peluso, A. M., Rucker, D. D., and Costabile, M. 2012. “On Braggarts and Gossips: A Self-Enhancement Account of Word-of-Mouth Generation and Transmission,” Journal of Marketing Research (49:4), pp. 551-563.

Angrist, J. D., and Krueger, A. B. 1999. “Empirical Strategies in Labor Economics,” in Handbook of Labor Economics, D. C. O. Ashenfelter (ed.), Amsterdam: Elsevier B.V., pp. 1277-1366.

Archak, N., Ghose, A., and Ipeirotis, P. G. 2011. “Deriving the Pricing Power of Product Features by Mining Consumer Reviews,” Management Science (57:8), pp. 1485-1509.

Arnold, M. J., Reynolds, K. E., Jones, M. A., Tugut, M., and Gabler, C. B. 2014. “Regulatory Focus Intensity and Evaluations of Retail Experiences,” Psychology & Marketing (31:11), pp. 958-975.

Bagozzi, R. P., and Dholakia, U. M. 2006. “Antecedents and Purchase Consequences of Customer Participation in Small Group Brand Communities,” International Journal of Research in Marketing (23:1), pp. 45-61.

Berger, J. 2014. “Word of Mouth and Interpersonal Communication: A Review and Directions for Future Research,” Journal of Consumer Psychology (24:4), pp. 586-607.

Bound, J., Jaeger, D. A., and Baker, R. M. 1995. “Problems with Instrumental Variables Estimation When the Correlation between the Instruments and the Endogenous Explanatory Variable Is Weak,” Journal of the American Statistical Association (90:430), pp. 443-450.

Casaló, L. V., Flavián, C., and Guinalíu, M. 2010. “Antecedents and Consequences of Consumer Participation in on-Line Communities: The Case of the Travel Sector,” International Journal of Electronic Commerce (15:2), pp. 137-167.

Chang, A., Hsieh, S. H., and Lin, F. 2013. “Personality Traits That Lead Members of Online Brand Communities to Participate in Information Sending and Receiving,” International Journal of Electronic Commerce (17:3), pp. 37-62.

Dellarocas, C. 2006. “Strategic Manipulation of Internet Opinion Forums: Implications for Consumers and Firms,” Management Science (52:10), pp. 1577-1593.

Ghamrawi, N., and McCallum, A. 2005. “Collective Multi-Label Classification,” in Proceedings of the 14<sup>th</sup> ACM International Conference on Information and Knowledge Management, pp. 195-200.

Godes, D., and Silva, J. C. 2012. “Sequential and Temporal Dynamics of Online Opinion,” Marketing Science (31:3), pp. 448-473.

Goh, K.-Y., Heng, C.-S., and Lin, Z. 2013. “Social Media Brand Community and Consumer Behavior: Quantifying the Relative Impact of User- and Marketer-Generated Content,” Information Systems Research (24:1), pp. 88-107.

Higgins, E. T., Shah, J., and Friedman, R. 1997. “Emotional Responses to Goal Attainment: Strength of Regulatory Focus as Moderator,” Journal of Personality and Social Psychology (72:3). pp. 515-525.

Hennig-Thurau, T., Gwinner, K. P., Walsh, G., and Gremler, D. D. 2004. “Electronic Word-of-Mouth Via Consumer Opinion Platforms: What Motivates Consumers to Articulate Themselves on the Internet?,” Journal of Interactive Marketing (18:1), pp. 38-52.

Li, X., and Hitt, L. M. 2008. “Self-Selection and Information Role of Online Product Reviews,” Information Systems Research (19:4), pp. 456-474.

Moe, W. W., and Schweidel, D. A. 2012. “Online Product Opinions: Incidence, Evaluation, and Evolution,” Marketing Science (31:3), pp. 372-386.

Muniz Jr., A. M., and O’Guinn, T. C. 2001. “Brand Community,” Journal of Consumer Research (27:4), pp. 412-432.

Pang, B., Lee, L., and Vaithyanathan, S. 2002. “Thumbs Up? Sentiment Classification Using Machine Learning Techniques,” in Proceedings of the ACL-02 Conference on Empirical Methods in Natural Language Processing (Volume 10), Association for Computational Linguistics, pp. 79-86.

Stock, J. H., and Yogo, M. 2005. “Testing for Weak Instruments in Linear Iv Regression,” in Identification and Inference for Econometric Models: Essays in Honor of Thomas Rothenberg, D. W. K. Andrews and J. H. Stock (eds.), Cambridge, UK: Cambridge University Press, pp. 80-120.

Thelwall, M., Buckley, K., Paltoglou, G., Cai, D., and Kappas, A. 2011. “Sentiment Strength Detection in Short Informal Text,” Journal of the American Society for Information Science and Technology (61:12), pp. 2544-2558.

Vaish, A., Grossmann, T., and Woodward, A. 2008. “Not All Emotions Are Created Equal: The Negativity Bias in Social-Emotional Development,” Psychological Bulletin (134:3), pp. 383-403.

Waila, P., Singh, V., and Singh, M. 2012. “Evaluating Machine Learning and Unsupervised Semantic Orientation Approaches for Sentiment Analysis of Textual Reviews,” in Proceedings of the 2012 IEEE International Computational Intelligence & Computing Research.

Wu, F., and Huberman, B. A. 2008. “How Public Opinion Forms,” in Proceedings of the International Workshop on Internet and Network Economics, New York: Springer, pp. 334-341.

Yao, J., Wang, H., and Yin, P. 2011. “Sentiment Feature Identification from Chinese Online Reviews: Analyzing and Improving Supervised Machine Learning,” in International Journal of Web Engineering and Technology (7:4), pp. 381-398.

Zeng, D., Wei, D., Chau, M., and Wang, F. 2011. “Domain-Specific Chinese Word Segmentation Using Suffix Tree and Mutual Information,” Information Systems Frontiers (13:1), pp. 115-125.
