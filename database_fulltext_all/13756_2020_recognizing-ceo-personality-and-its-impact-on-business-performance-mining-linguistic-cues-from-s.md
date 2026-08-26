---
otero_id: 13756
otero_key: "XQ2QUU2W"
title: "Recognizing CEO personality and its impact on business performance: Mining linguistic cues from social media"
authors: "Shichao Wang; Xi Chen"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103173"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Recognizing CEO personality and its impact on business performance: Mining linguistic cues from social media

Shichao Wang, Xi Chen\*\*

Zhejiang University, China

## A R T I C L E I N F O

Keywords: Upper echelons theory CEO personality Social media Business performance

## A B S T R A C T

Upper echelons theory suggests that CEO personality will influence organizational performance. However, dificulty in measuring CEO personality restrains related research. We capture linguistic cues CEOs leaving on social media and recognize their personality by text mining. To our knowledge, it is the first study introducing social media text mining approaches into the research stream that empirically inquires and extends upper echelons theory. Then, we investigate the CEO personality’s impact on both operational and financial performance. Results show that CEO Extraversion, Emotional Stability, and Agreeableness improve Cost Eficiency and Profitability, while CEO Conscientiousness reduces them. CEO Openness to Experience negatively influences Profitability, and all facets of CEO personality improve Employee Productivity except for CEO Conscientiousness. The contribution of our research is multi-sided: (1). methodologically, we introduce a text mining approach to measure CEO personality; (2). theoretically, we provide empirical evidence for upper echelons theory; (3). practically, our results help companies evaluate CEO candidates from a personality perspective.

## 1. Introduction

Before Satya Nadella became CEO of Microsoft in February 2014, the tech giant’s stock price had gone sideways for 14 years at the helm of Ballmer. Its business was being challenged by the trend of mobility and cloud service at that time. However, since Satya Nadella took over Microsoft, the share price has almost tripled and its market value is now over \$800 billion.<sup>1</sup> Although, without rigorous analysis, we cannot assert that the growth of Microsoft during the last 4 years is due to the change of CEO, analysts believe one of the important reasons is Satya Nadella’s strategic choice: moving away from proprietary phone hardware and operating systems and centered around subscription products.<sup>2</sup> Another example of a CEO’s impact on firm performance is from Ford’s CEO Alan Mullaly.<sup>3</sup> Besides evidence from industry, researchers in strategic management and organizational theory have already reached a consensus that leadership explains a non-trivial proportion of organizational performance variance [1]. As the leader of executives, a CEO often has a disproportionate, sometimes dominating, influence on his or her firm. Therefore, the choice of a chief executive oficer (CEO) is a crucial decision for an organization.

Concluded by upper echelons theory [2], it is the psychological and observable characteristics of a CEO that influence, through a threestage process, his or her decision and hence organizational performance. As one of the major psychological characteristics, CEO personality has been investigated by strategic management researchers to demonstrate its impact on organizational strategies and performance (e.g., [3,6]). However, extant research focuses more on special traits of personality, such as hubris [3,5] and narcissistic [6].<sup>4</sup> But from a comprehensive view, personality comprises multiple dimensions and all dimensions take effect simultaneously when a CEO makes decisions. So. we adopt Big Five model [7–9], which is the most accepted framework measuring personality, to capture every facet of CEO personality as well as its impact on organizational performance.

One main challenge that restrains researchers from investigating the impact of CEO personality comprehensively is the dificulty in obtaining data about CEOs’ personality. CEOs of public organizations tend to be unwilling to answer questionnaires about their personality [4], and responses may sufer from social desirability bias [10]. One pro mising and practical alternative approach is to use unobtrusive indicators. For instance, Chatterjee and Hambrick [6] leverage the prominence of a CEO’s photograph in company’s annual report, press releases, etc., to measure a CEO’s level of narcissism; Tang et al. [5] adopt a media-based measure of CEO hubris based on data collected from business press coverage. However, when we aim to measure personality in a comprehensive way, the mentioned kinds of unobtrusive measure failed because of the dificulty in manually defining an appropriate criterion to measure all facets of personality uniformly. Fortunately, this digital era provides us with the possibility to recognize CEOs’ personality automatically through data mining techniques utilizing the behavior CEOs generated on the Internet, which often leaks cues of personality. One of the sources of psychological cues is social media where people express themselves by posting status (e.g., Facebook and Twitter). Specifically, in this research, we crawl CEOs’ social media homepages to obtain their textual posts and then adopt a predictive model trained by Mairesse et al. [11] to automatically recognize CEOs’ personality using linguistic features extracted from text. This approach allows us to measure all five dimensions of CEO personality based on the same feature set. As we show in Pretest 1-3, the features we use to recognize personality are stable across scenarios (e.g. online or ofline), identities (e.g. CEO or normal user) and time.

On the performance side, extant research has studied the impact of executives’ characteristics on organizational strategic choices (e.g., [12]), organizational performance (e.g. [13]) and variation of organi zational performance (e.g. [6]). However, the performance indicators investigated are mostly finance-related. Venkatraman and Ramanujam [14] have already advocated adopting a broader conceptualization of the construct space of business performance in strategic management studies. They conclude that it will provide a more comprehensive operationalization of business performance if it is viewed from both financial and operational perspective. Besides, we are able to look into the influence path from CEO personality to financial performance if more detailed operational-level performance is included in analysis. Researchers also find that leaders can have diferent magnitude of im pact on diferent measures of performance (e.g. [15]). Therefore, in our research, we intend to investigate the overall impact of CEO personality on both financial and operational performance. Specifically, we choose three categories of business performance indicators-Cost Eficiency, Productivity and Profitability [16,17]. To our knowledge, we are the first research to investigate how each facet of CEO personality influ ences operational performance.

Our empirical model is built on a dataset combining CEOs’ personality scores with the business performance of corresponding firms during their tenure. To construct the dataset, we first find out CEOs of S &P 500 companies and then manually search their accounts on Facebook and Twitter. Finally, 71 CEOs’ social media accounts are found. After filtering out those CEOs who post rarely, 50 CEOs are left to the analysis stage. Corresponding business performance and control data are downloaded from the Compustat and ExecuComp database. Before econometric analysis, two pretests are conducted to validate the adopted predictive model is applicable in social media context and applicable to public figures like CEOs. We also do a correlation analysis (i.e., pretest 3) to verify the stable personality assumption, because personality scores are treated as constant over time in our model. Results of our regression models show that CEO Extraversion, Emotional Stability, and Agreeableness have a positive efect on Cost Eficiency, while Conscientiousness has a negative efect. For Productivity, results are complex but almost all facets of personality have a positive efect on Employee Productivity, except for Conscientiousness. Finally, CEO Extraversion, Emotional Stability, and Agreeableness positively influence firm Profitability, while Conscientiousness and Openness to Experience have a negative influ ence on it.

The contribution of our research is multi-sided: (1). methodologically, we introduce a text mining approach based on public data to measure executives’ personality, which may inspire researchers in related fields to make more innovative use of user digital footprint in this big data era; (2). theoretically, we contribute to the upper echelons perspective of an organization by empirically demonstrating what and how CEO personality afects business performance in a comprehensive way; (3). Practically, our research provides a basis for the board of directors to evaluate CEO candidates from a personality perspective.

## 2. Theoretical background

## 2.1. Whether and why CEO afects business performance

Lieberson and O’Connor [18] initiated a debate on whether leadership makes a diference to organizational performance in the 1970s˜1980s among researchers in strategic management and organizational theory. “Individualists” maintain that leaders have a significant and possibly great impact on the performance of the organizations they lead, but “contextualists” emphasize the constraints placed on leaders by situational factors [19]. Related studies in this period find that between about 5% and 20% of the variance in performance is due to CEO efects (in some cases explaining as much as 50%) [1,20,21]. After much debate, Thomas [1] concludes that the impact of leaders on differences between firms can be trivial because it will be determined largely by the characteristics of firms, but the impact of leaders within firms is crucial if we control the company-level influences. In other words, leadership does matter at least within firms. Meanwhile, researchers find that leaders can have much diferent magnitude of impact on diferent measures of performance (e.g. [15]), which is one of the reasons we adopt a broader conceptualization of the construct space of business performance.

But the rationale underlying the efect was not systematically un derstood until Hambrick and Mason set up upper echelons theory in 1984 [22,2]. The theory suggests that top managers’ psychological and observable attributes (e.g., age, education, career experience) will in fluence their strategic choices and organizational performance through a three-stage process—defining a field of vision, selective perception, and interpretation [2]. Upper echelons theory provides the theoretical basis for our research. Extant research within the framework of upper echelons theory can be classified into four categories: (1) Impact of executives’ characteristics on organizational choices, such as culture, strategy, structure (e.g. [5,6,23]); (2) Impact of executives’ characteristics on organizational performance mediated by organizational choice (e.g. [13]); (3) Impact of executives’ characteristics on organizational performance (e.g., [6,24,25]); (4) The moderating role played by contextual variables in the relationship of executives’ characteristics and organizational performance (e.g. [26,27]). Our study contributes to the third stream and extends it by considering operational performance in our analysis and introducing a novel measure of executives’ personality.

## 2.2. Personality traits and stability of personality

We adopt the Big Five model as the framework of personality traits. These five personality traits have been repeatedly obtained by applying factor analyses to various personality questionnaires [7–9]. Big Five model presents current orthodoxy in personality assessment and ofers a robust and comprehensive way of understanding personality diferences [28]. Using the Big Five model also caters to the recent calls to use comprehensive psychological frameworks to investigate the relationships between CEO personality and firm performance [13]. To be specific, Big Five model assesses personality in the following five dimensions [29,30]:

(1) Extraversion (talkative, sociable, assertive, energetic);

(2) Emotional Stability (calm, not neurotic, not easily upset,

unemotional);

(3) Agreeableness (good-natured, cooperative, friendly);

(4) Conscientiousness (orderly, responsible, dependable, self-dis ciplined);

(5) Openness to Experience (intellectual, imaginative, independent minded, insightful).

Studies about the stability of personality are also related to our research because we assume a CEO’s personality is stable over time. McCrae and Costa [31] suggest that an individual's personality at age 80 can be well predicted by his or her personality at age 30. McCrae and Costa [32] further review research about stability of personality and summarize four conclusions: (1) Mean levels of personality traits change with age, but reach stable after about age 30; (2) Individual diferences in personality traits are also essentially fixed by age 30; (3) Stability appears in all Big Five traits of personality; (4) Stability apply to almost everyone no matter what identity he or she is. Although a meta-analysis conducted by Ardelt [33] shows that literature fails to support personality stability theory, they still find that studies assessing any of Big Five personality traits tend to find higher personality stability. Besides, all the research we review about top managers’ personality and organizational performance treats personality as a stable disposition (e.g. [5,6]). Therefore, the assumption of stability of CEO personality in our study is theoretically reasonable.

## 2.3. Personality recognition

Traditional measures of Big Five personality are questionnairebased. Nadkarni and Herrmann [13] adopt a 60-item revised NEO Five-Factor Inventory [34] to measure personality in the framework of the Big Five model. The very brief measure of the Big-Five personality proposed by Gosling et al. [35] is also widely used because of its convenience. Some unobtrusive measures of personality are also proposed. For instance, Chatterjee and Hambrick [6] leverage a CEO’s prominence in the company’s press releases to measure a CEO’s level of narcissism, Malmendier and Tate [36] and Tang et al. [5] abstract news articles that mention focal CEOs and then count the total number of times they are described by terms suggesting confidence or conservatism to measure level of hubris.

In the last 20 years, with the purpose of automatic recognition of personality, researchers have been attempting to build a connection between psychological cues and personality (e.g., [11,37–41]). One proposition is mining linguistic cues to recognize personality. It has been proved that utterances convey a great deal of information about the speaker [37,42]. Word use has also been demonstrated as a stable individual diference with several modest but reliable correlations with personality [43].

Methods to extract linguistic features from text divide into two categories: closed-vocabulary methods and open-vocabulary methods. Closed-vocabulary approach starts with word categories (e.g., pronouns, inclusive words, social process, etc.) which have been predefined based on linguistic theory, and then counts the frequency of words in each category [44]. A typical study using closed-vocabulary approach is Mairesse et al. [11], who trains the model we use in this study. They extract linguistic features according to Linguistic Inquiry and Word Count (LIWC) dictionary and MRC Psycholinguistic database and then train predictive models for each Big Five personality trait based on these features. Results showed that the models perform well. In contrast, open-vocabulary methods do not rely on predefined word categories. They extract a comprehensive collection of linguistic features (e.g., single words, nonword symbols, multiword phrases and topics) from text being analyzed [40]. Because these linguistic features are not assigned a priori, this category of methods can accommodate unconventional language use and predict very well on text from same context [40,44]. But it also sufers from a problem of generality when models applied to corpus from a diferent context. On the contrary, closed-vocabulary methods, which are theory-based, will have higher generalizability across diferent contexts. Therefore, theoretically speaking, we think the model we adopt is more likely to be applicable to corpus from diferent contexts.

## 2.4. Social media use and personality

One of the fastest growing and most popular applications in this digital era is social media where individual users maintain their social connections and share their experiences or opinions online. There is already empirical evidence demonstrating that social media use is related to users’ personality. For example, Eftekhar et al. [39] investigate the link between Facebook users’ photo-related activities and the Big Five personality traits and find connections such as Neuroticism and Extraversion predict more photo uploads. Amichai-Hamburger and Vinitzky [45] find users’ personality correlates with various Facebook behaviors like taking part in groups, using private messages, sharing information, etc. Park et al [40] link posted status on Facebook to users personality using a regression model built on open-vocabulary linguistic features. Their results indicate that the linguistic cues on social media can also be mined to construct valid personality measures. Other examples are Golbeck et al. [46], Farnadi et al. [41], Sumner et al. [47], etc. Therefore, it is theoretically reasonable to extract CEOs’ personality from social media text posted by CEOs. Furthermore, we think the text from social media reflects CEOs’ utterance more efectively than text such as CEOs’ speeches or interviews because social media posts are less restricted for CEOs expressing themselves.

## 3. Methodology

## 3.1. Data

To construct our sample of CEOs, we first acquire the list of S&P 500 companies, and then visit the oficial website of each company. For those publicly owned companies, information about leadership will be displayed thoroughly and updated timely for the purpose of information disclosure to stakeholders. Information about leadership displayed on an oficial website typically consists of (1) Full name of leaders; (2) Leaders’ positions currently held in the company; (3) Leaders’ education and working experiences; (4) Leaders’ photographs. Thus, the CEO of a company will be easily recognized. We then search the combination of each CEO’s name and the corresponding company name on Facebook and Twitter. The keywords for a CEO include (1) company name and the CEO’s full name, (2) company name and the CEO’s last name, (3) company name and the CEO’s first name, (4) the CEO’s full name. Results are filtered by (1) comparing profile picture or photos uploaded to social media with the CEO’s photograph on company’s oficial website; (2) comparing education and/or work experiences disclosed on social media with oficially described education and/or work experiences. After this time-consuming manual process, 71 CEOs are found on Facebook or Twitter or both.

The next step is to crawl the text that CEOs posted on Facebook and Twitter. For Facebook, we use the Selenium module in Python to overcome the dynamic loading problem. For twitter, we utilize the REST APIs provided by twitter to request post data for each CEO. To make personality recognition reliable, we filter out CEOs who posted less than 200 words on social media. Finally, we have 50 CEOs from 50 distinct companies in our sample.

Yearly business performance and other industry-level, firm-level and individual-level control variables within a CEO’s tenure are all collected from Compustat and ExecuComp database. Combining CEOs’ personality scores with firm business performance, we finally have 40 CEOs and 218 firm-year observations in our sample. Note that 10 CEOs are omitted when combining dataset because of control data missing. We then filter out 8 observations whose focal year is earlier than 2000. Because the market may have changed significantly after 2000 and observations before 2000 are too sparse which may bias the estimation of time trend efect.

## 3.2. Measures

## 3.2.1. CEO personality

We measure personality comprehensively within the framework of Big Five model [7–9]. Mairesse et al. [11] train predictive models for recognition of all Big Five personality traits on both conversation and written text. They released their trained predictors online.<sup>5</sup> Along with the main package, predefined dictionaries needed for feature extraction are also provided. The two dictionaries used are: (1) Linguistic Inquiry and Word Count (LIWC) by Pennebaker and King [37], which extracts 88 linguistic features such as “anger words”, “inclusive words”, “family members”, etc., from text. (2) MRC Psycholinguistic database [69], which gives scores for words on 14 features such as “imagery of words”, “concreteness”, “frequency of use”, etc., based on statistics for over 150,000 words. The program first extracts linguistic features and computes score on each feature based on LIWC and MRC dictionary from text, then trained models are loaded to give scores between 1.0 to 7.0 (low to high) on all five traits of personality. Four predictive models are provided in the released package, i.e. (1) Linear Regression, (2) M5 Model Tree, (3) M5' Regression Tree and (4) Support Vector Machine with Linear Kernel (SMOreg). According to their experimental results, predictor based on support vector performs best in predicting self-re port personality from written text.<sup>6</sup> The SMOreg predictor also per forms well in the following Pretest 1 which validates the efectiveness of alternative predictors using an external dataset from online social media context. Therefore, we adopt the SMOreg predictor to obtain CEOs’ personality scores in our study.

3.2.1.1. Pretest 1. The predictors provided by Mairesse et al. [11] are trained on essays written by students in laboratory, while our corpus for CEO personality recognition is collected from social media platforms. Although we have theoretically argued that a predictor built on linguistic features extracted through a close-vocabulary approach is more likely to be general across context, we still need to empirically test whether the predictor we adopt performs well in the social media context.

We collect an external dataset which is a subsample from myPersonality project [48]. It includes 10,000 Facebook textual status updates from 250 users and their self-report Big Five personality scores and Facebook social media properties. myPersonality is a third-party application on Facebook, on which users can take a series of psychological tests and share results with their friends. The self-report personality scores are measured by the NEO-PI-R questionnaire [34], which gives scores on each Big Five personality trait range from 1 to 5. The descriptive statistics for the self-report personality scores in our external dataset are presented in Table 1.

To validate the efectiveness of the four alternative predictors, we first aggregate text to user level and then apply each predictor to every user’s text collection to get their predicted personality scores (users writing less than 200 words are omitted). For each model, the predicted personality scores are compared with corresponding self-report scores (both predicted and self-reported personality scores have been normalized to 0–1 before comparison). Mean Absolute Error (MAE) for personality scores predicted by each predictor is reported in Table 2.

Table 1  
Descriptive statistics for self-report personality scores in myPersonality dataset.

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td>Extraversion</td><td>150</td><td>3.2958</td><td>0.8642</td><td>1.35</td><td>5.00</td></tr><tr><td>Emotional Stability</td><td>150</td><td>2.5909</td><td>0.7443</td><td>1.35</td><td>4.75</td></tr><tr><td>Agreeableness</td><td>150</td><td>3.6158</td><td>0.6695</td><td>1.65</td><td>5.00</td></tr><tr><td>Conscientiousness</td><td>150</td><td>3.5140</td><td>0.7973</td><td>1.45</td><td>5.00</td></tr><tr><td>Openness to Experience</td><td>150</td><td>4.1186</td><td>0.6082</td><td>2.25</td><td>5.00</td></tr></table>

As is shown in Table 2, the best two predictors are P3 (M5' Regression Tree) and P4 (Support Vector Machine with Linear Kernel), both with MAE less than 0.17 averaged over all five personality traits. If transformed to the original scale from 1 to 7, the average MAE for P3 and P4 is about 1. Openness to Experience is the hardest trait to predict using online social media text. But the best two predictors still predict it with MAE less than 0.21, i.e. no more than 1.26 if scaled from 1 to 7. Just as Mairesse et al. [11] argued “…one needs to keep in mind the dificulty of the regression task over the binary classification task: it is the most fine-grained personality recognition problem, requiring the association of an exact scalar value with each individual”. Besides, the self-report personality scores in the myPersonality dataset may be biased from true scores because they are completed in a less rigorous and entertainment-oriented context. It may exaggerate the error of predictors trained on personality scores obtained in a rigorous laboratory setting. So, we think the performance of trained predictors, especially P3 and P4, on social media text is acceptable and it is reasonable to use these predictors to obtain CEOs’ personality scores from their social media textual posts.

3.2.1.2. Pretest 2. Another concern about the applicability of the adopted predictor in our research is that CEOs as public figures may be restricted by their special identity when expressing themselves on social media. Theoretically, we argue that the content or topic of textual posts may be restricted by their identity, but leaked linguistic features are hard to control so that will be stable. Empirically, we conduct a test to verify that our measurement is not afected by the factor that CEOs may hide their true personal traits because they are speaking on behalf of the firm, by testing the consistency of personality scores across diferent topics of text to show. The underlying logic of the test is that if the role as a CEO is influencing the writing of the CEO, then the personal traits detected from text of their writing of business-related content will be diferent from those detected from text of their writing of nonbusiness-related content. If CEOs’ personality can be consistently recognized across business-related and nonbusiness-related text, we may claim the stability of linguistic features and hence the applicability of the adopted predictor.

Specifically, we first clean our collected textual posts by removing stop words, numbers, punctuations and lemmatizing each word in the text. Then topic modeling is conducted using LDA algorithm [49] on all collected posts in order to reveal the latent topic of each textual post. Diferent settings are tested. It turns out that business-related topic and nonbusiness-related topic can be well defined with topic number 2 and using only noun and verb in the text to do LDA.<sup>7</sup> The top 20 keywords for each topic are listed in Table 3. We then apply the adopted personality predictor to recognize each CEO’s personality solely on business-related text or nonbusiness-related text. Correlation analysis shows that the two lists of CEOs’ personality scores are highly correlated with each other (Table 4), which provides evidence for the stability of linguistic features and the applicability of the adopted predictor to predict personality of public figures like CEOs.

Table 5  
Mean Absolute Error (MAE) for personality scores predicted by trained model on myPersonaliy dataset.

<table><tr><td>Personality Trait</td><td>MAE for P1</td><td>MAE for P2</td><td>MAE for P3</td><td>MAE for P4</td></tr><tr><td>Extraversion</td><td>0.184129</td><td>0.185173</td><td>0.175998</td><td>0.178191</td></tr><tr><td>Emotional Stability</td><td>0.176544</td><td>0.176544</td><td>0.168971</td><td>0.173057</td></tr><tr><td>Agreeableness</td><td>0.167434</td><td>0.137826</td><td>0.14033</td><td>0.134359</td></tr><tr><td>Conscientiousness</td><td>0.15512</td><td>0.154861</td><td>0.153512</td><td>0.156155</td></tr><tr><td>Openness to Experience</td><td>0.215145</td><td>0.215145</td><td>0.201245</td><td>0.206779</td></tr><tr><td>Average</td><td>0.179675</td><td>0.17391</td><td>0.168011</td><td>0.169708</td></tr></table>

Note: P1-P4 indicate the four alternative personality predictors

Table 3 LDA results.

<table><tr><td colspan="2">Topic 1: Nonbusiness-related</td><td colspan="2">Topic 2: Business-related</td></tr><tr><td>Top 20 Keywords</td><td>Weight</td><td>Top 20 Keywords</td><td>Weight</td></tr><tr><td>team</td><td>0.011</td><td>thanks</td><td>0.010</td></tr><tr><td>get</td><td>0.011</td><td>ceo</td><td>0.007</td></tr><tr><td>thanks</td><td>0.010</td><td>see</td><td>0.007</td></tr><tr><td>thank</td><td>0.010</td><td>business</td><td>0.007</td></tr><tr><td>help</td><td>0.009</td><td>customer</td><td>0.007</td></tr><tr><td>year</td><td>0.009</td><td>innovation</td><td>0.006</td></tr><tr><td>make</td><td>0.009</td><td>today</td><td>0.006</td></tr><tr><td>time</td><td>0.009</td><td>look</td><td>0.005</td></tr><tr><td>today</td><td>0.009</td><td>excite</td><td>0.005</td></tr><tr><td>work</td><td>0.008</td><td>tech</td><td>0.005</td></tr><tr><td>go</td><td>0.008</td><td>follow</td><td>0.005</td></tr><tr><td>day</td><td>0.008</td><td>share</td><td>0.004</td></tr><tr><td>people</td><td>0.007</td><td>congrat</td><td>0.004</td></tr><tr><td>world</td><td>0.006</td><td>thx</td><td>0.004</td></tr><tr><td>post</td><td>0.006</td><td>davos</td><td>0.004</td></tr><tr><td>see</td><td>0.006</td><td>book</td><td>0.004</td></tr><tr><td>look</td><td>0.005</td><td>meet</td><td>0.004</td></tr><tr><td>way</td><td>0.005</td><td>yahoo</td><td>0.004</td></tr><tr><td>need</td><td>0.005</td><td>technology</td><td>0.004</td></tr><tr><td>use</td><td>0.005</td><td>leader</td><td>0.004</td></tr></table>

Correlation of personality scores predicted on business-related posts and nonbusiness-related posts.

<table><tr><td>Personality Trait</td><td>Obs</td><td>Correlation</td></tr><tr><td>Extraversion</td><td>42</td><td>0.5170***</td></tr><tr><td>Emotional Stability</td><td>42</td><td>0.7540***</td></tr><tr><td>Agreeableness</td><td>42</td><td>0.4499***</td></tr><tr><td>Conscientiousness</td><td>42</td><td>0.4914***</td></tr><tr><td>Openness to Experience</td><td>42</td><td>0.6553***</td></tr><tr><td>Average</td><td></td><td>0.5531</td></tr></table>

\* $^ { \star \star } \mathrm { p } < 0 . 0 1 , ^ { \star \star } \mathrm { p } < 0 . 0 5 , ^ { \star } \mathrm { p } < 0 . 1 ,$

Another evidence will be given in the section of personality en dogeneity analysis, which proves that CEO personality traits will not be afected by firm performance. The underlying logic is that if CEOs’ utterance is afected by their identity as CEO, we can infer that firm performance will influence their utterance on social media because firms in diferent situation require diferent CEO public image. Hence, CEOs’ recognized personality based on linguistic features will be affected. However, the results of personality endogeneity analysis do not support the potential influence.

3.2.1.3. Pretest 3. Because all text posted by a CEO will firstly be aggregated to one text file for personality recognition, our measure of CEO personality is invariant, reflecting the view that personality is a relatively stable disposition. Although we have provided theoretical evidence in Section 2.2 that personality is relatively stable, especially it is measured within the framework of Big Five model, we further do an empirical test to support our assumption of personality stability.

Correlation coeficients between personality scores measured on $1 ^ { s t }$ half and 2<sup>nd</sup> half corpus.

<table><tr><td rowspan="2">Personality Trait</td><td colspan="2">Continuous 1 st and 2nd half</td><td colspan="2">Omit 5000 words between 1 st and 2nd half</td></tr><tr><td>Obs</td><td>Correlation</td><td>Obs</td><td>Correlation</td></tr><tr><td>Extraversion</td><td>46</td><td>0.5948***</td><td>15</td><td>0.6546***</td></tr><tr><td>Emotional Stability</td><td>46</td><td>0.6547***</td><td>15</td><td>0.9011***</td></tr><tr><td>Agreeableness</td><td>46</td><td>0.4836***</td><td>15</td><td>0.7050***</td></tr><tr><td>Conscientiousness</td><td>46</td><td>0.5364***</td><td>15</td><td>0.5712***</td></tr><tr><td>Openness to Experience</td><td>46</td><td>0.6845***</td><td>15</td><td>0.8543***</td></tr><tr><td>Average</td><td></td><td>0.5908</td><td></td><td>0.7372</td></tr></table>

\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

Specifically, corpus of each CEO is split into two parts with same number of words. The first part of corpus consists of early posted text and the second part is comprised by recent posted text (each part should meet the 200-word threshold). Then personality scores are predicted using predictor P4 based on solely first or second part of corpus. As shown in the left part of Table $^ { 5 , }$ we find that the personality scores measured on 1st and 2nd half corpus are highly correlated. However, CEO may post frequently in a short time, so it is likely that the first and second half both contain text posted within a short time span. To eliminate this potential bias, we further delete 5000 words in the middle of each CEO’s sequence of posts and then split text in the same way as above.<sup>8</sup> This procedure makes sure that at least 10 posts being omitted between the first and second half (the maximum length of a post in our sample is 478 words), so that the first and second half are much less likely to include text posted in a short time span. Result of correlation analysis is presented in the right part of Table 5, which still indicates personality scores are highly consistent over time. In conclusion, Pretest 3 presents solid evidence about the stability of linguistic features and hence predicted personality over time.

## 3.2.2. Business performance

Smith et al. [17] derive a set of performance metrics to study preoutsourcing firm characteristics. They group the firm performance metrics into six categories: cost eficiency, productivity, profitability, growth, cash management, and market ratios. Following Jiang et al. [16], we use three out of these six performance metrics categories: cost eficiency, productivity, and profitability. Specifically, business performance is measured as following. The definition of each item is from Compustat oficial document

## 3.2.2.1. Cost eficiency

(1) Overhead expense per unit of sales: Selling, general and administrative expenses (SG&A) / Sales. SG&A represents all commercial expenses of operation (such as, expenses not directly related to product production) incurred in the regular course of business pertaining to the securing of operating income. Units of SG&A and Sales are both millions of dollars.

(2) Operating expense per unit of sales: (Cost of goods sold + SG&A) /Sales. Cost of goods sold represents all expenses directly allocated by the company to production, such as material, labor, and overhead. The total operating costs for nonmanufacturing companies are considered as Cost of Goods Sold if a breakdown is not available. Unit of cost of goods sold is also millions of dollars.

Table 6  
Results for personality endogeneity analysis.

<table><tr><td rowspan="2">Variable</td><td colspan="5">Regression Models</td></tr><tr><td>Extraversion</td><td>Emotional Stability</td><td>Agreeableness</td><td>Conscientiousness</td><td>Openness to Experience</td></tr><tr><td> $Revenue_{t-1}$ </td><td>1.85e-06(1.87e-06)</td><td>2.24e-07(2.81e-06)</td><td>-5.53e-07(1.54e-06)</td><td>8.09e-07(1.40e-06)</td><td>-1.47e-06(2.15e-06)</td></tr><tr><td> $FirmAge_{t-1}$ </td><td>-0.00962**(0.00350)</td><td>-0.00412(0.00527)</td><td>0.000138(0.00288)</td><td>-0.00377(0.00263)</td><td>0.00403(0.00402)</td></tr><tr><td> $ROA_{t-1}$ </td><td>0.240(0.749)</td><td>-0.552(1.127)</td><td>0.671(0.616)</td><td>0.241(0.562)</td><td>0.718(0.861)</td></tr><tr><td> $Year_{t-1}$ </td><td>-0.00949(0.0144)</td><td>-0.0137(0.0216)</td><td>-0.00565(0.0118)</td><td>0.00294(0.0108)</td><td>0.00785(0.0165)</td></tr><tr><td> $ROAChange_t$ </td><td>2.395(2.086)</td><td>-1.027(3.140)</td><td>2.716(1.717)</td><td>2.171(1.567)</td><td>-1.247(2.398)</td></tr><tr><td> $IsChairman_t$ </td><td>-0.0490(0.186)</td><td>-0.0238(0.281)</td><td>-0.0392(0.153)</td><td>0.0525(0.140)</td><td>0.0423(0.214)</td></tr><tr><td> $PctSharesOwned_t$ </td><td>0.0308(0.0970)</td><td>-0.184(0.146)</td><td>0.107(0.0799)</td><td>0.0254(0.0729)</td><td>-0.143(0.112)</td></tr><tr><td> $Age_t$ </td><td>0.00348(0.00324)</td><td>-0.00465(0.00488)</td><td>0.00178(0.00267)</td><td>0.00179(0.00243)</td><td>0.00623(0.00372)</td></tr><tr><td> $IsOutsideHire$ </td><td>-0.00128(0.154)</td><td>0.293(0.232)</td><td>-0.158(0.127)</td><td>-0.0358(0.116)</td><td>0.118(0.177)</td></tr><tr><td>Constant</td><td>23.96(28.84)</td><td>31.60(43.42)</td><td>15.95(23.75)</td><td>-1.128(21.67)</td><td>-11.52(33.16)</td></tr><tr><td>Observations</td><td>39</td><td>39</td><td>39</td><td>39</td><td>39</td></tr><tr><td>Adj R-squared</td><td>0.1584</td><td>-0.0010</td><td>-0.0447</td><td>-0.1003</td><td>-0.0667</td></tr></table>

Standard errors in parentheses.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

## 3.2.2.2. Productivity

(1) Assets turnover: Sales/Assets. Assets represents current assets (cash, and other assets which, in the next 12 months, expect to be realized in cash or used in the production of revenue) plus net property, plant, and equipment (PPE) plus other noncurrent assets (including intangible assets, deferred charges, and investments and advances). Units of Sales and Assets are both millions of dollars.

(2) PPE turnover: Sales/Property, Plant, and Equipment (fixed assets). Units of Property, Plant, and Equipment is also millions of dollars

(3) Inventory turnover: Sales/Inventory. Inventory represents merchandise bought for resale and materials and supplies purchased for use in production of revenue. Units of Inventory is millions of dollars

(4) Employee productivity: Sales/Number of employees. It measures the eficiency of a company's use of its employees in generating sales revenue to the company.

## 3.2.2.3. Profitability

(1) Return on assets: Income Before Extraordinary expenses (IBE) / Assets. IBE represents the income of a company after all expenses, including special items, income taxes, and minority interest – but before provisions for common and/or preferred dividends. The units of IBE is millions of dollars.

(2) Net profit margin: Income Before Extraordinary expenses (IBE) / Sales.

We collect each item from the second year (t + 1) to the last year of a CEO’s tenure where t is the year CEO being appointed. If CEO is still in his position when we collected data, i.e. 2015, then we set the timeframe end to the year of 2015.

## 3.2.3. Control variables

Following Chatterjee and Hambrick [6], we control for potentially confounding factors at three levels: CEO level, firm level and industry level. It should be noticed that ${ \mathfrak { t } } + { \mathfrak { n } } \left( { \mathfrak { n } } \geq 1 \right)$ is the focal firm year.

(1) CEO controls: Because the tendency to engage in firm afairs may vary with age or tenure, we control CEO age and CEO tenure in year t + n–1.

(2) Firm controls: Because large and small firms may face diferent bureaucratic momentum and CEOs may have diferent strength of power in firms with diferent size, we control firm size (natural logarithm of revenues in year t + n–1). For the possibility that a given firm may have strategy or performance tendencies, we include, for each dependent variable, its value for the firm in the year prior to the start of the CEO’s tenure (i.e., year t – 1). We also include a binary indicator of whether the firm has a COO or president other than CEO in year t + n, to eliminate their impact on business performance.

(3) Industry controls: We control the industry’s central tendencies for each of our dependent variables by including the industry average (for all firms in the same industry, always excluding the focal firm) in each year (i.e., year t + n), for each dependent variable $\mathrm { ( B P I n d M e a n _ { t + n } ) } .$ . Chatterjee and Hambrick [6] also include industry sector dummy variable in their model. However, from our estimation results in Table 10, industry-level control variable $\mathbf { B P I n d M e a n } _ { \mathrm { t + n } }$ has trivial impact on our measure of business per formance, implying industry diference is not an important concern if we have controlled all the variables above. Therefore, we think the industry heterogeneity has been controlled if we have included industry average in our model. The reason that we don’t use industry dummy is that in our dataset, we have firms from 26 industry sectors (but only two industry sectors in [6]). We will lose a large number of degrees of freedom if we include 25 industry dummy variables, which will have a strong impact on the eficiency of estimation especially with a relatively small sample and cause identification problem.

(4) Personality endogeneity: Chatterjee and Hambrick [6] suggested CEO personality may be influenced by certain situations that request and/or allow them to demonstrate the tendency of some personality trait, therefore personality endogeneity should be controlled. Following their method, we regress our measure of all five CEO personality traits against a set of antecedent and contemporaneous variables. The antecedent variables, which captured key aspects of the CEO’s entry conditions, include firm revenues, firm age, ROA, calendar year at year t-1, ROA change between t and t-1. Contemporaneous variables are all measured at year t. They include the percentage of company stock owned by the CEO (PctSharesOwned ), CEO age and one dummy variable indicating if CEO is chairman of board. Besides, whether CEO is an outside hire, i.e. employed by the firm within a year prior to being CEO) is also included.

The results are presented in Table 6. Only CEO Extraversion is significantly afected by one independent variable, i.e. firm age. It indicates that our measure of CEO personality does not sufer from endogeneity problem. Therefore, we do not control the personality score predicted by the regression as Chatterjee and Hambrick [6] do in our main model. Another important insight from personality endogeneity analysis, just as we mentioned in Pretest 2, is the stability of CEOs linguistic features and hence the robustness of our measure of CEO personality.

We also control time trend efect using calendar year.

## 3.3. Model specification and estimation

Combining all the variables we discuss before in a linear specifica tion, we derive the following model for estimation,

$$
\begin{array}{r l} B P _ {t + n} = \alpha + \beta_ {1} B P _ {t - 1} + \beta_ {2} F i r m S i z e _ {t + n - 1} + \beta_ {3} H a s C o o O r P r e s _ {t + n} \\ & + \beta_ {4} P e r s o n a l i t y + \beta_ {5} C E O A g e _ {t + n - 1} + \beta_ {6} C E O T e n u r e _ {t + n - 1} + \beta_ {7} Y e a r \\ & + \beta_ {8} B P I n d M e a n _ {t + n} + \varepsilon \end{array}
$$

where BP stands for variables measuring business performance, and BPIndMean means industry average business performance excluding the focal firm. We also replace $B P I n d M e a n _ { t + n }$ with $B P I n d M e a n _ { t + n - 1 }$ (not excluding the focal firm) in the model so that it can be used for prediction, and the results are qualitatively same.

As for estimation, because the firms in our sample are not from a same industry or in same size thus may exist heterogeneity among them, we first test heteroscedasticity between groups using a Wald Test proposed by Greene [70]. We also test autocorrelation within groups using another Wald Test developed by Wooldridge [71]. The results, shown in Table 7, demonstrate that there are significant heteroscedasticity and AR1 autocorrelation in our panel data. Therefore, we fit our models using Generalized Least Squares (GLS) estimation for panel-data models and account for group-wise heteroscedasticity and panel-specific AR1 autocorrelation.

## 4. Results and discussion

Tables 8 and 9 present the descriptive statistics for CEOs’ person ality scores and other main variables, respectively. Table 10 presents

Results for the heteroscedasticity test and autocorrelation test.

<table><tr><td rowspan="2">Model for</td><td colspan="2">Wald Test for Groupwise Heteroskedasticity</td><td colspan="2">Wooldridge Test for Autocorrelation in Panel data</td></tr><tr><td>chi2(33)</td><td>P-value</td><td>F(1, 23)</td><td>P-value</td></tr><tr><td>SGA/Sales</td><td>6.7e+07***</td><td>0.0000</td><td>91.309***</td><td>0.0000</td></tr><tr><td>Opexp/Sales</td><td>2.5e+13***</td><td>0.0000</td><td>351.422***</td><td>0.0000</td></tr><tr><td>AssetsTurnover</td><td>2.0e+05***</td><td>0.0000</td><td>6.225**</td><td>0.0202</td></tr><tr><td>PPETurnover</td><td>1.7e+09***</td><td>0.0000</td><td>3.247*</td><td>0.0847</td></tr><tr><td>InventoryTurnover</td><td>7.4e+11***</td><td>0.0000</td><td>136.824***</td><td>0.0000</td></tr><tr><td>EmployeeProductivity</td><td>60276.56***</td><td>0.0000</td><td>5.290**</td><td>0.0309</td></tr><tr><td>ReturnOnAssets</td><td>95361.39***</td><td>0.0000</td><td>28.409***</td><td>0.0000</td></tr><tr><td>NetProfitMargin</td><td>8.7e+06***</td><td>0.0000</td><td>11.662***</td><td>0.0024</td></tr></table>

\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

Table 8  
Descriptive statistics for CEOs’ personality scores.

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td>Extraversion</td><td>50</td><td>4.79720</td><td>0.2090374</td><td>4.363735</td><td>5.131689</td></tr><tr><td>Emotional Stability</td><td>50</td><td>3.927338</td><td>0.2888846</td><td>3.502457</td><td>4.388147</td></tr><tr><td>Agreeableness</td><td>50</td><td>4.625817</td><td>0.2058804</td><td>4.170735</td><td>4.962068</td></tr><tr><td>Conscientiousness</td><td>50</td><td>4.709436</td><td>0.2169139</td><td>4.332998</td><td>4.893034</td></tr><tr><td>Openness to Experience</td><td>50</td><td>4.639837</td><td>0.2778897</td><td>4.253278</td><td>5.006913</td></tr></table>

estimation results.

As shown in Table 10, CEO Extraversion is positively related to Cost Eficiency.<sup>9</sup> One cluster of traits characterizing Extraversion includes sociability, gregariousness and talkativeness [50]. So, a feasible ex planation is that extraverted CEOs are more likely to build broad and diverse networks of social relationships because they tend to be initiative in social activities, adept in breaking ice with others and socially attractive by being humorous, launching topics and stimulating social interactions [511. The sociability of extraverted CEOs helps them mobilize others within their firms and outside the firms [13]. As a result, extraverted CEOs are accessible to more outer resources which are of benefit to reducing cost incurred to their own companies. A CEO’s high level of Extraversion also improves Employee Productivity. It can be a result of they being more talkative, warm, enthusiastic and opti mistic [30], which makes them more willing to communicate with emplovees and emplovees are tend to be encouraged by CEO's warmth enthusiasm and optimism. This proposition is also consistent with the argument of Bono and Judge [52] that extraverted leaders are expressive and articulate individuals who persuade, influence, and orga nize others. Besides. another cluster of traits characterizing Extraversion includes assertiveness and dominance [50]. It implies that more extraverted CEOs are more forceful and efective in communicating their decisions and opinions to employees [53], whose productivity also depends on the clarity of the order and the efficiency of communication with their leaders. The positive efects of CEO Extraversion on Cost Eficiency and Employee Productivity are two paths through which it raises firm Profitability. Nadkarni and Herrmann [13] has also demonstrated that strategic flexibility mediates the positive relationship between CEO extraversion and firm Profitability. Besides, we think another possible reason is that extraverted CEOs are optimistic and energetic [30], which helps them keep calm and make right decisions when faced with high stress. However, extraverted CEOs’ optimism may make them overestimate the market circumstance. Meanwhile extra verted CEOs are more ambitious [54] As a result they may invest superfluously in firm assets, which leads to low Assets Turnover and PPE Turnover. Following the same logic, we may expect a lower Inventory Turnover in a firm with extraverted CEO. but the empirical results showed there is no significant relationship between them. We think it is because inventory management is a more rational procedure with advanced ERP developed nowadavs. It is in conformity with the empirical results show in Table 3 that none of the personality traits has significant impact on Inventory Turnover.

As for Emotional Stability, the empirical results are more consistent and demonstrate that Emotional Stability is definitely a positive personality trait. From the perspective of individual-level performance, extant research has shown that neurotic individuals (low in Emotional Stability) are more likely to be worse job performers because they have more tendency to feel insecure or overly anxious or distracted from their work [55]. Therefore, Emotional Stability is an important individual performance predictor in all jobs including executive jobs and it is expected to relate to business performance [54]. In addition, low level of Emotional Stability is associated with low self-esteem and low

Table 9  
Descriptive statistics for dependent and control variables.

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td>SGA/Sales $_{t+n}$ </td><td>210</td><td>0.30483</td><td>0.22786</td><td>0</td><td>0.82325</td></tr><tr><td>Opexp/Sales $_{t+n}$ </td><td>210</td><td>0.70928</td><td>0.24324</td><td>0</td><td>0.98206</td></tr><tr><td>AssetsTurnover $_{t+n}$ </td><td>210</td><td>0.75618</td><td>0.57981</td><td>0.01874</td><td>2.91446</td></tr><tr><td>PPETurnover $_{t+n}$ </td><td>210</td><td>8.19745</td><td>7.98332</td><td>0.79789</td><td>61.3796</td></tr><tr><td>InventoryTurnover $_{t+n}$ </td><td>210</td><td>44.0887</td><td>221.839</td><td>0</td><td>2823.53</td></tr><tr><td>EmployeeProductivity $_{t+n}$ </td><td>210</td><td>421.03</td><td>275.517</td><td>106.211</td><td>2056.61</td></tr><tr><td>ReturnOnAssets $_{t+n}$ </td><td>210</td><td>0.06143</td><td>0.06096</td><td>-0.4272</td><td>0.23703</td></tr><tr><td>NetProfitMargin $_{t+n}$ </td><td>210</td><td>0.12024</td><td>0.15621</td><td>-0.8573</td><td>1.62874</td></tr><tr><td>RevenueLog $_{t-n-1}$ </td><td>210</td><td>9.16269</td><td>1.57077</td><td>5.73611</td><td>12.1059</td></tr><tr><td>HasCooOrPres $_{t+n}$ </td><td>210</td><td>0.33333</td><td>0.47253</td><td>0</td><td>1</td></tr><tr><td>CEOAge $_{t-n-1}$ </td><td>210</td><td>50.8048</td><td>5.9088</td><td>36</td><td>67</td></tr><tr><td>CEOTenure $_{t-n-1}$ </td><td>210</td><td>4.56667</td><td>4.63891</td><td>0</td><td>22</td></tr><tr><td>Year $_{t+n}$ </td><td>210</td><td>2010.24</td><td>3.64849</td><td>2000</td><td>2015</td></tr><tr><td>SGA/SalesIndMean $_{t+n}$ </td><td>210</td><td>1.54397</td><td>5.42559</td><td>0</td><td>74.0818</td></tr><tr><td>Opexp/SalesIndMean $_{t+n}$ </td><td>210</td><td>2.02954</td><td>5.44721</td><td>0</td><td>74.6947</td></tr><tr><td>AssetsTurnoverIndMean $_{t+n}$ </td><td>210</td><td>1.00624</td><td>0.52195</td><td>0</td><td>2.97539</td></tr><tr><td>PPETurnoverIndMean $_{t+N}$ </td><td>210</td><td>20.4027</td><td>17.7378</td><td>0</td><td>95.7275</td></tr><tr><td>InventoryTurnoverIndMean $_{t+n}$ </td><td>210</td><td>27.4995</td><td>81.6534</td><td>0</td><td>815.38</td></tr><tr><td>EmployeeProductivityIndMean $_{t+n}$ </td><td>210</td><td>318.144</td><td>205.634</td><td>0</td><td>2301.16</td></tr><tr><td>ReturnOnAssetsIndMean $_{t+n}$ </td><td>210</td><td>-1.424</td><td>5.25421</td><td>-49.107</td><td>0.28771</td></tr><tr><td>NetProfitMarginIndMean $_{t+n}$ </td><td>210</td><td>-6.1776</td><td>17.0984</td><td>-180.48</td><td>0.96317</td></tr></table>

self-eficacy [53]. Thus, these people are less likely to be perceived as good and strong leaders in most conditions [56,57] and it has been demonstrated by existing studies that most successful leaders are emotionally stable [58,59]. These are possible reasons accounting for the empirical results that neurotic CEOs do harms to every operational aspect of a company and the overall financial performance. Besides, since neurotic CEOs tend to be compulsive, defensive, and thin-skinned [50], they are relatively more dificult to establish social networks inside and outside their firms. As a result, they are less likely to utilize outer resources and maintain a collective atmosphere among employees, which lead to lower Cost Eficiency and Employee Productivity.

The empirical results for Agreeableness are almost same as that of Extraversion, which can be the result of they both being interpersonally oriented [60]. Agreeable individuals usually show personal warmth, a preference for cooperation over competition, and trust and acceptance of others [50]. Therefore, similar as extraverted CEOs, CEOs with high Agreeableness are more likely to have a broader social relationship within the firms and outside the firms. So, Cost Eficiency may be improved through their accessibility to outer resources. Agreeableness has also been thought to help members in group maintain a harmony relationship and reduce within-group conflict [61,62]. It will benefit Employee Productivity in addition to the more employee care provided by agreeable CEOs since they are personally warmer. The positive ef fects of CEO Agreeableness on Cost Eficiency and Employee Productivity are two ways it raises firm Profitability. Peterson et al. [28] has proposed another mechanism by which CEO Agreeableness afect performance, i.e. CEO Agreeableness will enhance TMT (Top Management Team) cohesion and decentralization. However, agreeableness can also cause passivity, in which CEOs act modest and avoid conflicts at all costs [13]. CEOs’ kindness and altruism may be “used” by others, such as suppliers, cooperative partner and other related companies. So, they are more likely to be persuaded to invest in unnecessary assets, resulting in lower PPE Turnover.

Table 10  
Estimation results main models.

<table><tr><td rowspan="2">Variable</td><td colspan="2">Cost Efficiency</td><td colspan="4">Productivity</td><td colspan="2">Profitability</td></tr><tr><td>SGA/Sales</td><td>Opexp/Sales</td><td>Assets Turnover</td><td>PPE Turnover</td><td>Inventory Turnover</td><td>Employee Productivity</td><td>Return on Assets</td><td>Net Profit Margin</td></tr><tr><td> $OP_{t-1}$ </td><td>0.926***(0.0326)</td><td>0.690***(0.0424)</td><td>1.023***(0.0473)</td><td>0.759***(0.0336)</td><td>0.797***(0.278)</td><td>1.091***(0.0166)</td><td>0.283***(0.0219)</td><td>0.808***(0.0383)</td></tr><tr><td> $FirmSize_{t-n-1}$ </td><td>0.00687**(0.00283)</td><td>0.000808(0.00347)</td><td>-0.0356***(0.00771)</td><td>-0.420***(0.107)</td><td>-5.278(10.26)</td><td>-3.430**(1.554)</td><td>-0.00341**(0.00157)</td><td>-0.00676*(0.00349)</td></tr><tr><td> $HasCooOrPres_{t+n}$ </td><td>-0.00485(0.00361)</td><td>0.0127(0.00879)</td><td>0.0474**(0.0227)</td><td>0.123(0.208)</td><td>1.478(8.367)</td><td>-13.70***(4.259)</td><td>-0.00413(0.00384)</td><td>-0.000133(0.00458)</td></tr><tr><td>Extraversion</td><td>-0.0687***(0.0160)</td><td>-0.104***(0.0211)</td><td>-0.161**(0.0692)</td><td>-2.620***(0.682)</td><td>-15.76(31.98)</td><td>25.14**(11.15)</td><td>0.0476***(0.00847)</td><td>0.0338*(0.0197)</td></tr><tr><td>EmotionalStability</td><td>-0.0260**(0.0115)</td><td>-0.0106(0.0170)</td><td>-0.00211(0.0298)</td><td>2.302***(0.543)</td><td>12.97(27.84)</td><td>64.00***(4.829)</td><td>0.0156**(0.00642)</td><td>0.0504***(0.0141)</td></tr><tr><td>Agreeableness</td><td>-0.103***(0.0262)</td><td>-0.129***(0.0348)</td><td>-0.123(0.0929)</td><td>-1.910**(0.972)</td><td>24.56(57.63)</td><td>32.87*(17.81)</td><td>0.0857***(0.0182)</td><td>0.0769*(0.0407)</td></tr><tr><td>Conscientiousness</td><td>0.128***(0.0221)</td><td>0.192***(0.0408)</td><td>0.327***(0.0837)</td><td>-0.0594(1.154)</td><td>10.68(45.06)</td><td>-0.475(15.76)</td><td>-0.139***(0.0168)</td><td>-0.117***(0.0234)</td></tr><tr><td>OpennessToExperience</td><td>0.0106(0.0130)</td><td>0.0152(0.0172)</td><td>-0.238***(0.0718)</td><td>0.545(0.637)</td><td>-5.786(33.62)</td><td>32.23***(9.195)</td><td>-0.0384***(0.00783)</td><td>-0.0472***(0.0176)</td></tr><tr><td> $CEOAge_{t-n-1}$ </td><td>-0.00492***(0.000777)</td><td>-0.00351***(0.00125)</td><td>0.00484(0.00383)</td><td>-0.00499(0.0423)</td><td>-0.735(2.239)</td><td>-0.705(0.690)</td><td>0.00322***(0.000402)</td><td>0.00451***(0.00116)</td></tr><tr><td> $CEOTenure_{t-n-1}$ </td><td>0.00674***(0.00117)</td><td>0.00584***(0.00197)</td><td>-0.0143***(0.00340)</td><td>-0.231***(0.0613)</td><td>-3.268(3.499)</td><td>8.954***(0.634)</td><td>-0.00419***(0.000698)</td><td>0.000603(0.00,136)</td></tr><tr><td>Year</td><td>7.52e-05(0.000993)</td><td>0.00414**(0.00162)</td><td>0.00269(0.00422)</td><td>0.113**(0.0538)</td><td>-0.168(3.065)</td><td>-0.321***(0.0774)</td><td>0.000303(0.000555)</td><td>-0.00493***(0.00181)</td></tr><tr><td> $OPIndMean_{t+n}$ </td><td>0.000217(0.000281)</td><td>5.69e-05(0.000238)</td><td>0.0126(0.0170)</td><td>0.00115(0.00602)</td><td>0.0541(0.0838)</td><td>-0.00857*(0.00455)</td><td>0.000578**(0.000281)</td><td>-0.000243(0.000148)</td></tr><tr><td>Constant</td><td>0.297(2.028)</td><td>-7.768**(3.274)</td><td>-4.399(8.437)</td><td>-210.9*(110.6)</td><td>320.2(6188)</td><td>0(0)</td><td>-0.518(1.097)</td><td>9.845***(3.717)</td></tr><tr><td>Observations</td><td>203</td><td>203</td><td>203</td><td>203</td><td>203</td><td>203</td><td>203</td><td>203</td></tr><tr><td>Number of Groups</td><td>33</td><td>33</td><td>33</td><td>33</td><td>33</td><td>33</td><td>33</td><td>33</td></tr></table>

Standard errors in parentheses.  
\* p < 0.  
\*\* p < 0.05.  
\*\*\* p < 0.01.

The most interesting and counter-intuitive empirical results come from the impacts of CEO Conscientiousness and Openness to Experience. Conscientiousness is defined as self-disciplined, organized, strong-willed, dependable and achievement-oriented, while Openness to Experience is defined as intellectual, curious, insightful, creative, unconventional and artistic [29,30]. Intuitively, these two traits should be “good” characteristics because they are associated with better per sonal performance and more efective leadership [53,55]. However, empirical results in our research show that their impacts on business performance indicators are mostly negative. Conscientious CEOs lead to low Cost Eficiency. Following the logic proposed above, a conceivable reason is that conscientious CEOs are very task-focused rather than relationship-focused [50]. In other words, they would rather realize a goal on their own than seek others for a favor. Thus, most cost in operation or production will be taken by their own company. Conscientious CEOs also avoid taking actions that deviate significantly from their past experience and they need concrete feedback on actions [53]. Consequently, they are not able to respond to market change immediately and cut of wrong strategies as soon as negative signs emerge [63,64]. These behaviors can incur low Cost Eficiency and Profitability of a firm. This argument is consistent with the opinion and result by Nadkarni and Herrmann [13], who theoretically argued and empirically showed that CEO conscientiousness is negatively related to firm financial performance and it’s mediated by the negative efect of CEO conscientiousness on firm strategic flexibility. However, on the other hand, since they tend to commit to established rules and routines, existing assets will be more fully utilized so that higher Assets Turnover achieved by more conscientious CEOs.

As for Openness to Experience, it is the only trait that has no sig nificant impact on Cost Eficiency. This result also follows the logic we proposed above, i.e. Openness to Experience is less related to interpersonal relationship or responsibility taking [60] so that CEO Openness to Experience is less likely to afect Cost Eficiency by determining how much outer resources they utilized or the extent to which they achieve goals on their own. The negative impact on Assets Turnover can be explained in the way just opposite to that we use to explain why conscientious CEOs improve Assets Turnover. Open CEOs have a strong need for change and are highly capable of adapting to new rules or perspectives [65]. So, they tend to change their strategy frequently, which may break the existing product and resource advantages of firms [26] and hence reducing the eficiency of assets usage. This is also one of the feasible reasons that CEO Openness to Experience leads to lower Profitability. Another reason is that they actively seek excitement and risks [53]. As a result, they are less likely to make rational decisions rely on past experience or lessons. It can be a double-edged sword: on the one hand, it enhances firm strategic flexibility [13]; on the other hand, it put firms into a situation facing larger risk of failure. Finally, CEO high in Openness to Experience would particularly reward intellectually flexible and open group members [66]. Therefore, employees led by open CEOs may be more intellectually flexible and open-minded [28] and have wider discretion and stronger motivation in solving problems in more eficient ways. It is one mechanism by which CEO Openness to Experience positively afects Employee Productivity as shown in our empirical results.

Generally speaking, Extraversion, Emotional Stability and Agreeableness seems to be “good” characteristics, while Conscientiousness and Openness to Experience tend to be “bad” characteristics. Results for CEO Conscientiousness and CEO Openness to Experience are most surprising and in fact, are contrary to findings of several extant papers (e.g. [13,54,67]). However, extant findings about the impact of CEO Personality on organizational performance are usually mediated by some other variables, such as strategic flexibility, firm culture, leadership, top management team integration. The impact of CEO personality on organizational performance may be exerted through various paths and the direction and/or magnitude of impact can difer with diferent path models. An example is given by Nadkarni and Herrmann [13] and O’Reilly III et al. [68]. Nadkarni and Herrmann [13] demonstrate CEO Conscientiousness has negative efect on firm performance when mediated by strategic flexibility, while O’Reilly III et al. [68] find a positive impact of CEO Conscientiousness on firm performance through being associated with firm cultures that are detail oriented. However, the aim of our research is to estimate the overall direction and magnitude of impact exerted by each CEO personality trait on business performance. Therefore, the results we give have in cluded influence of CEO personality through all potential paths, which should difer from the results through only one influence path. Besides, extant research mostly focuses on a relatively small number of in dustries and usually medium and small firms are considered because of the convenience to survey on CEO personality. But in our research, we do not need to ask CEOs to answer personality questionnaires since an unobtrusive predictor is applied and our sample is public firms from various industries. That is also an important reason why we have dif ferent or even contradictory results when compared to former research.

## 5. Conclusion and limitations

This research studies the impact of CEO personality on firm business performance in a comprehensive way. It answers two questions within the framework of upper echelons theory [2]: what dimensions of CEO personality afect firm business performance and in which direction.

To the best of our knowledge, this research is also the first one introducing a text mining approach to measure executives’ personality in the field of upper echelons theory. It is also the first time that CEOs’ social media behaviors are observed to recognize CEOs’ personality. These two novel approaches may inspire researchers in related fields to make more innovative use of user digital footprint in this big data era. To our knowledge, this is also the first research that studies how each facet of CEO personality influences operational performance.

However, some limitations still exist that can serve as future research directions. First, the sample size for our econometric analysis is relatively small, which may not be representative enough. In the future studies, researchers may obtain personality data for more CEOs through other initiative ways. Second, the predictor we adopted is from an initial work of applying machine learning to recognize personality. With rapid development of machine learning, more advanced models have been proposed.<sup>10</sup> We advocate that researchers disclosure their trained predictors to others and we may refer to these more advanced and accurate models in future studies. Third, the explanation about the results is not theoretically organized. This is a dificult work in that CEO personality can afect firm performance through various paths and the directions of impact on diferent paths may be contradictory with each other, just as we mentioned in discussion. But our research is aimed at demonstrating the existence and the direction of the overall efect. Future research can further investigate new paths CEO personality af fects organizational performance and try to synthesize all the potential paths in a theoretical framework to help management researchers and practitioners analyze the overall impact CEO personality may have on organizational performance.

## Funding

This work is supported by the National Natural Science Foundation of China (Nos. 91546107, 71821001 and 71372057), the Natural Science Foundation of Zhejiang Province (Nos. LR16G020001), and the Social Science Foundation of Zhejiang Province (Nos. 13ZJQN030YB).

## Acknowledgements

The authors are grateful to the Editor and reviewers for their invaluable and insightful comments that have greatly helped to improve this work.

## References

[1] Thomas, Alan Berkeley, Does leadership make a diference to organizational performance? Adm. Sci. Q. (1988) 388–400.

[2] Donald C. Hambrick, Phyllis A. Mason, Upper echelons: the organization as a reflection of its top managers, Acad. Manag. Rev. 9 (2) (1984) 193–206.

[3] Nathan J. Hiller, Donald C. Hambrick, Conceptualizing executive hubris: the role of (hyper) core self-evaluations in strategic decision-making, Strateg. Manage. J. 26 (4) (2005) 297–319.

[4] Donald C. Hambrick, Upper echelons theory: an update, Acad, Manag, Rey, 32 (2007) 334–343.

[5] Yi Tang, et al., How CEO hubris afects corporate social (ir) responsibility, Strateg. Manage. J. 36 (9) (2015) 1338–1357.

[6] Arijit Chatterjee, Donald C. Hambrick, It’s all about me: narcissistic chief executive oficers and their efects on company strategy and performance, Adm. Sci. Q. 52 (3) (2007) 351–386.

[7] Warren T. Norman, Toward an adequate taxonomy of personality attributes: re plicated factor structure in peer nomination personality ratings, J. Abnorm. Soc. Psychol. 66 (6) (1963) 574.

[8] Dean Peabody, Lewis R. Goldberg, Some determinants of factor structures from personality-trait descriptors, J. Pers, Soc, Psychol, 57 (3) (1989) 552

[9] Lewis R. Goldberg, An alternative “description of personality”: the big-five factor structure, J. Pers, Soc. Psychol. 59 (6) (1990) 1216

[10] Roger Tourangeau, Ting Yan, Sensitive questions in surveys, Psychol. Bull. 133 (5) (2007),859.

[11] François Mairesse, et al., Using linguistic cues for the automatic recognition of personality in conversation and text, J. Artif, Intell, Res, 30 (2007) 457–500.

[12] Mathew L.A. Hayward, Donald C. Hambrick, Explaining the premiums paid for large acquisitions: evidence of CEO hubris, Adm. Sci. Q. (1997) 103–127.

[13] Sucheta Nadkarni, P.O.L. Herrmann. CEO personality, strategic flexibility, and firm performance: the case of the Indian business process outsourcing industry, Acad. Manag. J. 53 (5) (2010) 1050–1073

[14] Natarian Venkatraman, Vasudevan Ramanuiam, Measurement of business performance in strategy research: a comparison of approaches, Acad. Manag. Rev. 11 (4) (1986) 801–814.

[15] Aldrich, Howard, Organizations and environments, Englewoods Cliffs, 1979.

[16] Bin Jiang, Gregory V. Frazier, Edmund L. Prater, Outsourcing effects on firms' operational performance: an empirical study, Int. J. Oper. Prod. Manage. 26 (12) (2006) 1280–1300.

[17] Michael Alan Smith, Sabyasachi Mitra, Sridhar Narasimhan, Information systems outsourcing: a study of pre-event firm characteristics, J. Manag. Inf. Syst. 15 (2) (1998) 61–93.

[18] Stanley Lieberson, James F. O’Connor, Leadership and organizational performance: a study of large corporations, Am. Sociol. Rev. (1972) 117–130.

[19] Jefrey Pfefer, Gerald R. Salancik, The External Control of Organizations: a Resource Dependence Approach. Harper and Row Publishers. NY. 1978

[20] Nan Weiner, Situational and leadership influences on organization performance, Acad. Manag. Proc. 1 (1978) Briarclif Manor, NY 10510: Academy of Management, 1978.

[21] Nan Weiner, Thomas A. Mahoney, A model of corporate performance as a function of environmental, organizational, and leadership influences, Acad. Manag. J. 24 (3) (1981) 453–470.

[22] Finkelstein, Sydney, and Donald Hambrick, "Strategic Leadership, West Educationa Publishing, St. Paul, 1996.

[23] Michael Jensen, Edward J. Zajac, Corporate elites and corporate strategy: how demographic preferences and structural position shape the scope of the firm,

Strateg. Manage. J. 25 (6) (2004) 507–524.

[24] David Hirshleifer, Angie Low, Siew Hong Teoh, Are overconfident CEOs better in novators? J. Finance 67 (4) (2012) 1457–1498.

[25] Anthony L. Iaquinto, James W. Fredrickson, Top management team agreement about the strategic decision process: A test of some of its determinants and con: sequences, Strateg. Manage. J. 18 (1) (1997) 63–75.

[26] Sucheta Nadkarni, Vadake K. Narayanan, Strategic schemas, strategic flexibility, and firm performance: the moderating role of industry clockspeed, Strateg. Manage. J. 28 (3) (2007) 243–270.

[27] Donald C. Hambrick, Eric Abrahamson, Assessing managerial discretion across industries: a multimethod approach, Acad. Manag. J. 38 (5) (1995) 1427–1441.

[28] Randall S. Peterson, et al., The impact of chief executive oficer personality on top management team dynamics: one mechanism by which leadership afects organizational performance, J. Appl. Psychol. 88 (5) (2003) 795.

[29] Oliver P. John, Sanjay Srivastava, The Big Five trait taxonomy: history, measurement, and theoretical perspectives, Handbook of personality: Theory and research2, (1999), pp. 102–138 1999.

[30] Paul T. Costa, Robert R. McCrae, The revised neo personality inventory (neo-pi-r), The SAGE Handbook of Personality Theory and Assessment 2.2, (2008), pp. 179–198.

[31] Robert R. McCrae, Paul T. Costa, Self-concept and the stability of personality: crosssectional comparisons of self-reports and ratings, J. Pers. Soc. Psychol. 43 (6) (1982) 1282.

[32] Robert R. McCrae, Paul T. Costa, The stability of personality: observations and evaluations, Curr. Dir. Psychol. Sci. 3 (6) (1994) 173–175.

[33] Ardelt, Monika, Still stable after all these years? Personality stability theory revisited, Soc. Psychol. Q. (2000) 392–405.

[34] Paul T. Costa Jr, Robert R. McCrae, Four ways five factors are basic, Pers. Individ. Dif, 13 (6) (1992) 653–665.

[35] Samuel D. Gosling, Peter J. Rentfrow, William B. Swann Jr, A very brief measure of the Big-Five personality domains, J. Res. Pers. 37 (6) (2003) 504–528.

[36] Ulrike Malmendier, Geofrey Tate, Who makes acquisitions? CEO overconfidence and the market’s reaction, J. financ. econ. 89 (1) (2008) 20–43.

[37] James W. Pennebaker, Laura A. King, Linguistic styles: language use as an individual diference, J. Pers. Soc. Psychol. 77 (6) (1999) 1296.

[38] Jacob B. Hirsh, Jordan B. Peterson, Personality and language use in self-narratives, J. Res. Pers. 43 (3) (2009) 524–527.

[39] Azar Eftekhar, Chris Fullwood, Neil Morris, Capturing personality from Facebook photos and photo-related activities: how much exposure do you need? Comput. Human Behav, 37 (2014).162-170

[40] Gregory Park, et al., Automatic personality assessment through social media lan guage, J. Pers. Soc. Psychol. 108 (6) (2015) 934.

[41] Golnoosh Farnadi, et al., Computational personality recognition in social media, User Model. Useradapt. Interact. 26 (2-3) (2016) 109–142.

[42] Matthias R. Mehl, Samuel D. Gosling, James W. Pennebaker, Personality in its natural habitat: Manifestations and implicit folk theories of personality in daily life, J. Pers, Soc. Psychol. 90 (5) (2006) 862

[43] Lisa A. Fast, David C. Funder, Personality as manifest in word use: correlations with self-report, acquaintance report, and behavior, J. Pers. Soc. Psychol. 94 (2) (2008) 334.

[44] H.Andrew Schwartz, et al., Personality, gender, and age in the language of socia media: the open-vocabulary approach, PLoS One 8 (9) (2013) e73791.

[45] Yair Amichai-Hamburger, Gideon Vinitzky, Social network use and personality, Comput, Human Behay, 26 (6) (2010) 1289–1295.

[46] Jennifer Golbeck, Cristina Robles, Karen Turner, Predicting personality with social media. CHI'11 Extended Abstracts on Human Factors in Computing Systems. ACM 2011.

[47] Chris Sumner, et al., Predicting dark triad personality traits from twitter usage and a linguistic analysis of tweets, Machine Learning and Applications (Icmla), 2012 11th International Conference on vol. 2. (2012)

[48] Fabio Celli, et al., Workshop on computational personality recognition (shared task). Proceedings of the Workshop on Computational Personality Recognition (2013).

[49] David M. Blei, Andrew Y. Ng, Michael I. Jordan, Latent dirichlet allocation, J. Mach Learn Res, 3 (January) (2003) 993–1022

[50] Robert R. McCrae, Paul T. Costa, Validation of the five-factor model of personality across instruments and observers, J. Pers. Soc. Psychol. 52 (1) (1987) 81.

[51] Robert J. House, Jane M. Howell, Personality and charismatic leadership, Leadersh. Q. 3 (2) (1992) 81–108.

[52] Joyce E. Bono, Timothy A. Judge, Personality and transformational and transac tional leadership: a meta-analysis, J. Appl. Psychol. 89 (5) (2004) 901.

[53] Timothy A. Judge, Joyce E. Bono, Remus Ilies, Megan W. Gerhardt, Personality and leadership: a qualitative and quantitative review, J. Appl. Psychol. 87 (4) (2002) 765.

[54] Amy E. Colbert, Murray R. Barrick, Bret H. Bradley, Personality and leadership composition in top management teams: implications for organizational effective ness, Pers, Psychol, 67 (2) (2014) 351–387.

[55] Murray R. Barrick, Michael K. Mount, Timothy A. Judge, The FFM personality dimensions and iob performance: meta-analysis of meta-analyses. Int. J. Sel. Assess. S (1/2) (2001) 9–30.

[56] Robert Hogan. Gordon J. Curphy. Jovce Hogan. What we know about leadership efectiveness and personality, Am. Psychol. 49 (6) (1994) 493.

[57] Robert J. House, Power and personality in complex organizations, Res. Organ. Behav. 10 (1988) 305–357.

[58] Bernard M. Bass, Ralph Melvin Stogdill, Bass & Stogdill’s Handbook of Leadership: Theory, Research, and Managerial Applications, Simon and Schuster, 1990.

[59] Murray R. Barrick, Greg L. Stewart, Mitchell J. Neubert, Michael K. Mount, Relating member ability and personality to work-team processes and team efectiveness, J. Appl. Psychol. 83 (3) (1998) 377.

[60] D. Scott Derue, Jennifer D. Nahrgang, N.E.D. Wellman, Stephen E. Humphrey, Trait and behavioral theories of leadership: an integration and meta-analytic test of their relative validity, Pers. Psychol. 64 (1) (2011) 7–52.

[61] William G. Graziano, Elizabeth C. Hair, John F. Finch, Competitiveness mediates the link between personality and group performance, J. Pers. Soc. Psychol. 73 (6) (1997) 1394.

[62] Michael K. Mount, Murray R. Barrick, Greg L. Stewart, Five-factor model of per sonality and performance in jobs involving interpersonal interactions, Hum Perform. 11 (2–3) (1998) 145–165.

[63] Kathleen M. Eisenhardt, Jefrey A. Martin, Dynamic capabilities: what are they? Strateg. Manage. J. 21 (10–11) (2000) 1105–1121.

[64] Katsuhiko Shimizu, Michael A. Hitt, Strategic flexibility: organizational preparedness to reverse inefective strategic decisions, Acad. Manag. Perspect. 18 (4) (2004) 44–59.

[65] Paul T. Costa, Robert R. McCrae, Personality in adulthood: a six-year longitudina study of self-reports and spouse ratings on the NEO Personality Inventory, J. Pers. Soc. Psychol. 54 (5) (1988) 853

[66] Robert R. McCrae, Paul T. Costa Jr, Personality trait structure as a human universal, Am. Psychol. 52 (5) (1997) 509.

[67] Yazmina Araujo-Cabrera, Miguel A. Suarez-Acosta, Teresa Aguiar-Quintana, Exploring the influence of CEO extraversion and openness to experience on firm performance: the mediating role of top management team behavioral integration, J.

Leadersh. Organizational Stud. 24 (2) (2017) 201–215.

[68] I.I.I. O’Reilly, A. Charles, et al., The promise and problems of organizational culture: CEO personality, culture, and firm performance, Group Organ. Manage. 39 (6) (2014) 595–625.

[69] M. Coltheart, The MRC psycholinguistic database, Q. J. Exp. Psychol. A 33.4 (1981) 497–505.

[70] W.H. Greene, Econometric analysis, Pearson Education India, 2003.

[71] M. Wooldridge Jefrey, Econometric analysis of cross section and panel data, MIT press, 2002.

Shichao Wang is currently a PhD candidate at School of Management, Zhejiang University. He received his Bachelor’s degree in Information Management and Information Systems from Nanjing University of Aeronautics and Astronautics. His research interests include data mining, social network, and online content marketing. H has published his works in the proceedings of conferences such as Information Resource Management.

Xi Chen is professor at School of Management, Zhejiang University. He is currently the head of the Department of Data Science and Management Engineering. He received his Ph.D. degree in information systems from the University of Hong Kong. His research interests focus on data mining, mobile commerce, social media, and online healthcare. He has published his works in journals such as Decision Support Systems, European Journal of Operational Research, Information and Management, Internet Research, and Electronic Commerce Research and Applications.
