---
otero_id: 15646
otero_key: "3A88HCAW"
title: "Does the interplay between the personality traits of CEOs and CFOs influence corporate mergers and acquisitions intensity? An econometric analysis with machine learning-based constructs"
authors: "Qiping Wang; Raymond Y.K. Lau; Kai Yang"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113424"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Does the interplay between the personality traits of CEOs and CFOs influence corporate mergers and acquisitions intensity? An econometric analysis with machine learning-based constructs

Qiping Wang <sup>\*</sup>, Raymond Y.K. Lau , Kai Yang

Department of Information Systems, College of Business, City University of Hong Kong, Hong Kong Special Administrative Region

## A R T I C L E I N F O

Keywords: Mergers and acquisitions Econometric analysis Personality mining Machine learning Corporate finance

## A B S T R A C T

Although the upper echelons theory posits that senior executives’ personal characteristics influence firm per formance, very few studies have examined the impact of the interplay between CEO and CFO characteristics on corporate activities. To fill this research gap, we propose an econometric analysis model to examine the interplay between the personality traits of CEOs and CFOs and corporate mergers and acquisitions (M&A) intensity. In particular, our econometric analysis model is empowered by novel personality constructs extracted using a stateof-the-art machine learning-based personality detector that automatically mines CEO/CFO personality traits from firms’ earnings call transcripts. Based on historical M&A data of S&P 1500 firms, our econometric analysis reveals that the “openness” personality trait of CEOs is positively associated with corporate M&A intensity, while CEOs’ “consciousness” and “neuroticism” personality traits are negatively associated with corporate M&A in tensity. Moreover, the impacts of CEOs’ “openness” and “consciousness” personality traits on corporate M&A intensity are more pronounced when CFOs have similar personality traits to those of CEOs.

## 1. Introduction

The upper echelons (UE) theory suggests that the unobservable psychological characteristics of senior executives, along with their observable demographic characteristics, profoundly influence corporate strategic choices and performance [1,2]. Although the existing literature on corporate strategy reveals relationships between chief executive of ficers’ (CEOs’) psychological characteristics and corporate strategic behaviors [3,4], very few studies have examined the impact of CEO personality traits on M&A activities $[ 5 , 6 ]$ . Indeed, CEOs’ personality traits directly influence how they filter, interpret, and respond to envi ronmental stimuli, and thereby affect their strategic business choices [7]. Despite the growing interest in identifying the determinants of M&A success by the Information Systems (IS) research community [8–10], a study focused on the relationship between senior executives’ personality attributes and M&A activities is missing in the existing IS literature.

Although the CEO of a firm is the most critical actor in formulating corporate strategies, s/he often jointly makes strategic decisions with other top executives [1]. Chief financial officers (CFOs), who are the closest working partners of CEOs, tend to interact with CEOs throughout various strategic decision-making processes [11–13] such as corporate

M&As [12]. In particular, CFOs interact with CEOs at every stage of an M&A process, including drawing up a transaction plan before an M&A deal, negotiating with an M&A target, and improving the operational efficiency during the M&A integration phase [14]. Accordingly, how CFOs interact with CEOs often determines the ultimate M&A activities.

Indeed, the relationships between CEOs and CFOs have been found to be crucial for the success of M&As, and these relationships influence corporate financial performance [12]. One determinant of a good CEO-CFO partnership is a CEO-CFO personality matching that facilitates effective collaborative decision making [15]. An emerging body of research has examined how CEO-CFO relationships, such as the matching of language style in CEO-CFO social interactions, facilitate corporate activities [13]. Moreover, the relationships between CEO-CFO overconfidence and corporate tax-avoidance activities have come under scrutiny [11]. However, a study about the interplay between the per sonality traits of CEOs and CFOs and the impact of this interplay on corporate M&A intensity is missing in the existing literature. A firm’s M&A intensity is measured in terms of the number and accumulative values of M&A transactions in a financial year [13].

Nevertheless, a major challenge of studying the impact of senior executives’ personality traits on corporate performance is that it is extremely difficult to elicit such data on a large scale. Previous studies on executives’ personality traits were predominantly conducted based on intrusive, time-consuming, and costly surveying methods [3,4], which seriously limited the scope and external validity of such studies. Although some researchers have applied dictionary-based methods (e.g., LIWC and MRC database) to elicit executives’ personal particulars [16] or have inferred CEOs’ characteristics based on their profiles [6], the accuracy of these methods is questionable [17].

With the recent advances in data science and machine learning (ML), a deep learning model has been developed to effectively mine in dividuals’ personality traits based on their textual comments, and the model has been shown to significantly outperform other automated personality mining methods [17]. Empowered by such a state-of-the-art ML method, we apply it to automatically extract the personality traits of CEOs and CFOs based on 15,013 earnings call transcripts from 290 S&P 1500 firms. We then propose an econometric analysis model empowered by these novel personality constructs to study the interplay between CEOs and CFOs’ personality traits and corporate M&A intensity. Indeed, recent studies have confirmed that it is possible to extract executives personality traits from comments recorded in earnings call transcripts and then use these personality traits to analyze various business phe nomenon phenomena [5,13].

Previous studies show that the degree to which senior executives exhibit the personality traits of consciousness, openness, and neuroti cism, as defined in the big five personality model [18], influences corporate performance [3,4]. As such, this study first focuses on the impact of CEOs’ personality traits—specifically consciousness, open ness, and neuroticism—on M&A intensity. We then study how the interplay between these three personality traits in CEOs and CFOs might influence corporate M&A intensity.

The main contributions of our research are twofold. First, grounded in the UE theory, we propose an econometric analysis model empowered by novel ML-based personality constructs to examine the impact of CEOs’ personality traits on corporate M&A intensity. Second, we develop an econometric analysis model to study the impact of the interplay between the personality traits of CEOs and CFOs on corporate M&A intensity. To the best of our knowledge, this is the first successful econometric analysis empowered by ML-based personality constructs to empirically examine the interplay between the personality traits of CEOs and CFOs and their impact on corporate M&A intensity. The managerial implication of our research is that corporate decision makers can utilize our empirical findings to make more informed decisions regarding a variety of matters, including M&A target selection, corporate hiring, and institutional financial investment.

## 2. Theoretical foundations and hypothesis development

## 2.1. Literature review

## 2.1.1. CEO/CFO personality traits and M&As

As a major corporate strategy, M&A has received growing attention from the IS research community in recent years [8–10]. Extensive research has highlighted the relationships between various executive characteristics, such as personality traits [6,19,20], age [16], gender [21], tenure [22], experience [23], and compensation [24], and M&A activities. For executive personality, existing studies have looked at limited aspects of personality traits, such as CEO hubris [20], over confidence [6], and narcissism [19]. For example, Malmendier and Tate [6] examined the impact of CEO confidence on merger decisions. The study found that overconfident CEOs are more likely to engage in ac quisitions and undertake low-value mergers than non-overconfident CEOs. In another instance, Mathew and Hambrick [20] investigated the impact of CEO hubris on the acquisition premium for large size ac quisitions. The study revealed that CEO hubris is positively related to the premiums paid for acquisitions, and greater CEO hubris and acquisition premiums subsequently lead to greater shareholder losses. Aktas, Bodt,

Bollaert and Roll [19] argued that narcissistic CEOs are more likely to initiate an acquisition, negotiate faster, and complete the transaction. However, CEOs with these personality taxonomies tend to be over ambitious and make abrupt business decisions [25].

In reality, CEOs’ personalities are more diversified than the above mentioned traits. A more comprehensive taxonomy for describing in dividuals’ personality traits [26] is the big five personality model [27], which classifies personality attributes into five dimensions: extraversion (energetic, outgoing), neuroticism (emotional, sensitive), agreeableness (friendly, cooperative), conscientiousness (responsible, organized), and openness to experience (curious, imaginative). The big five personality model has gone beyond the field of psychology, and it has been widely used in the business field [4,28]. For example, Nadkarni and Herrmann [4] successfully adopted the big five personality taxonomy to explore the relationships between CEO personality, strategic flexibility, and performance. Accordingly, we employ the big five personality model to measure senior executives’ personality traits in our study.

Very few studies have examined the relationships between CEOs personality traits and M&A activities. One exception is a small scale empirical study examining the relationship between one single person ality dimension of CEO and M&A activities [5]. Consequently, there are still many outstanding research questions related to CEO personality and M&A activities.

## 2.1.2. CEO-CFO partnership

Researchers have begun to pay more attention to the issue of CEO-CFO partnerships in recent studies. How a CFO interacts with the CEO plays a critical role in a firm’s strategic decision making, such as M&As [13] and tax avoidance [11]. For example, CEOs and CFOs can have intensive social interactions when their language styles match [13]. High CEO-CFO language style matching can also result in firms initiating more M&A activities while receiving lower announcement returns. Furthermore, firms with overconfident CEOs and CFOs are more likely to engage in tax-avoidance activities than those with other combinations of CEO-CFO overconfidence [11]. Though previous studies have exam ined the impacts of CEO-CFO partnerships on business activities, they have not analyzed the impact of the interplay between CEO-CFO per sonality traits on M&A intensity. Accordingly, our study tries to fill this research gap by investigating the relationships between the interplay and dynamism of CEO-CFO personality traits and M&A intensity.

## 2.1.3. Personality mining

With the growing need for automatically mining individuals’ per sonality traits from large-scale data, some dictionary-based approaches, such as Linguistic Inquiry and Word Count (LIWC) and MRC Psycho linguistic databases, have emerged to automatically derive and evaluate personality linguistic cues in a more efficient way [29,30]. Proyer and Brauer [31] employed LIWC analysis to examine adult playfulness (one type of personality trait) from university students’ self-descriptions. Moreover, some ML methods, such as Support Vector Machine (SVM), Multinomial Naïve Bayes (MNB), and K-Nearest Neighbors (KNN), are being applied to detect personality using the bag-of-words model [32].

Recently, some deep learning-based methods, such as a convolu tional neural network (CNN) model [33], have emerged to detect in dividuals’ personality traits based on semantic features captured in social media posts. One step further, Yang and Lau [17] developed an attention-based deep learning model that can leverage both semantic and syntactic features embedded in text to identify individuals’ per sonalities [17]. Syntactical features are also critical linguistic cues that reflect one’s personality [34]. In sum, prior studies show evidence that ML methods, particularly deep learning methods, outperform dictionary-based personality mining approaches because deep learning methods can model complex relations between mass inputs and output classes. Accordingly, following [17], this study adopts the state-of-theart attention-based deep learning model to detect CEOs’/CFOs’ per sonalities from earnings call transcripts.

## 2.2. Hypothesis development

## 2.2.1. CEO conscientiousness and M&A intensity

Conscientiousness shows a tendency for self-discipline and an orientation for control and achievement against external expectations [35]. Individuals with high conscientiousness are self-disciplined, deliberate, cautious, and well organized [36], and they have a low tolerance for ambiguity [37]. CEO conscientiousness is positively correlated to legalism in the top management team (TMT) [26] and negatively correlated to corporate strategic flexibility [4] and the initi ation of strategic changes [3]. The legal (following rules) concern makes conscientious CEOs more prone to rely on “dependable, tried-and-true strategies” [4]. Consequently, conscientious CEOs may welcome known strategies, whereas they reject new and challenging strategies that deviate from their experience. Such a narrow vision may inhibit them from initiating strategic changes such as M&A investments. Moreover, CEOs with achievement orientation have a strong need to take control and responsibility for strategic behaviors [4]. This attribute may inhibit innovation and creative potential among employees.

A high intensity (frequency and transaction values) of M&A typically requires considerable deviations from previous M&A activities, and it entails reconstructing the organization [38]. Therefore, to initiate M&A activities, CEOs should be bold, risk-tolerant, and stand outside the established rules and regulations. However, conscientious CEOs depend on tried-and-true strategies and legalism, which makes them reluctant to pursue risky M&A activities. Accordingly, we establish the following hypothesis:

Hypothesis 1. CEO conscientiousness is negatively related to a firm’s M&A intensity.

## 2.2.2. CEO openness to experience and M&A intensity

Individuals who are open to experience are imaginative, curious, intelligent, broad-minded, and original [39]. Open individuals embrace novel experiences, engage in divergent thinking, vigorously search outside information, and find more innovative solutions to various problems [40–42]. Open CEOs tend to form a broad vision by consid ering multiple strategic avenues. With a higher level of openness, CEOs can quickly identify outside information that deviates from the existing mind-set, and they can better recognize and seize alternative strategic opportunities [4,43]. Moreover, prior studies have documented that CEO openness is positively related to strategic flexibility [4] and the initiation of strategic changes [3].

M&A is usually accompanied by a tremendous amount of outside information and radical changes, both of employees and the organiza tion itself. Open CEOs are more prone to embrace and enjoy these changes. Their receptivity to divergent and new information enables them to notice strategic changes and identify corresponding strategies in a timelier manner than CEOs who are not open. Therefore, we propose the following hypothesis:

Hypothesis 2. CEO openness to experience is positively related to a firm’s M&A intensity.

## 2.2.3. CEO neuroticism and M&A intensity

Neuroticism reflects one’s tendency to experience negative emotions such as depression, anger, and anxiety [44]. Neurotic individuals are less emotionally stable when facing new situations [45] and more vulnerable to stress [46]. They tend to generate negative emotional re actions toward even ordinary events and remain in bad moods for a long time. Additionally, neuroticism constitutes pessimism, self-doubt, and worry [47]. CEOs with a high score in neuroticism are more likely to hold pessimistic attitudes toward corporate strategies. The aforementioned neurotic attributes inhibit CEOs from thinking clearly, making wise decisions, and coping with stress. Furthermore, neurotic CEOs perceive higher risks in decision making [3,4]. Conversely, emotionally stable individuals are more likely to experience positive emotions such as joy, happiness, and anticipation, resulting in an enhanced ability to bear risks and address difficult issues [3]. Emotionally stable CEOs are better at decision making in dynamic and unpredictable situations [28].

Based on the above logic, we argue that CEO neuroticism is likely to lower firm M&A intensity. As neurotic CEOs experience negative emo tions toward new situations, they may also perceive higher risks and more difficulties with regard to target firms than emotionally stable CEOs. The perceived difficulties and risks will discourage them from pursuing risky and uncertain investments such as M&As. Therefore, we propose the following hypothesis:

Hypothesis 3. CEO neuroticism is negatively related to a firm’s M&A intensity.

## 2.2.4. Moderating effect of CFO personality similarity with CEO

Similarity is a critical factor in relationship development [48]. The False Consensus Effect, a psychological theory, suggests that individuals tend to trust, favor, or overestimate others who share similar opinions, beliefs, values, and personality traits [49]. “Similar kinds of people are likely to have similar kinds of personalities, are likely to do similar kinds of things, and are likely to behave in similar ways” [50]. This finding is further supported by [51], which finds that people tend to resort to interpersonal similarity, based on the big five model, for better decision making. Conversely, drawing on the cognitive consistency theory, dif ferences between two parties result in aversion and avoidance [52]. The personality differences in the CEO-CFO subgroup reflect their cognitive conflicts, which can lead to poor communication, reluctance to ex change information, and other functional and dysfunctional conflicts within a firm [53]. Hence, CFOs who have a similar personality with CEOs are less likely to disagree with CEOs and more likely to ingratiate themselves with regard to CEO decision making within the TMT. With the endorsement of CFOs, CEOs have more confidence in initiating or inhibiting M&A decisions.

Hypothesis 4. The relationships specified in H1, H2, and H3 are more pronounced when a CFO’s personality traits are similar to that of a CEO.

## 3. Data and methodology

## 3.1. Data construction

The data collection for this research began with accessing earnings call transcripts of S&P Composite 1500 listed firms from Seeking Alpha. Seeking Alpha is a crowd-sourced financial content provider that pub licizes publicly available historical firm disclosures, including quarterly earnings call transcripts. We downloaded 15,013 earnings call tran scripts from 2005 to 2017. We collected M&A data, executive data, corporate financial data, and stock return data from Thomson One, Execucomp, COMPUSTAT, and CRSP, respectively. After removing the samples that contained null values, our final sample contained 1633 firm-year observations and 750 CEO-CFO pairs from 290 S&P 1500 firms across 12 industries (details depicted in Table A.1 of Appendix).

A typical earnings transcript is composed of a prepared comment section and an improvisational Q&A section. In the comment section, CEOs and CFOs might polish their speeches beforehand, thus making it challenging to mine their real personalities. In contrast, CEOs’/CFOs speech in a Q&A section better reflects their real personalities as it is more difficult to script this type of speech [54]. Accordingly, following

## Q. Wang et al.

## Table 1

Correlations of personality scores generated by the adopted detector and surveys.

<table><tr><td></td><td>CON</td><td>OPN</td><td>NEU</td><td>EXT</td><td>AGR</td></tr><tr><td colspan="6">Panel A: Pearson correlation</td></tr><tr><td>Correlation</td><td>0.607***</td><td>0.602***</td><td>0.776***</td><td>0.608***</td><td>0.649***</td></tr><tr><td>#Obs.</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td></tr><tr><td colspan="6">Panel B: Intraclass correlation</td></tr><tr><td>Correlation</td><td>0.775***</td><td>0.769***</td><td>0.851***</td><td>0.771***</td><td>0.754***</td></tr><tr><td>#Obs.</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td></tr></table>

Notes: NEU: Neuroticism; CON: Consciousness; OPN: Openness to Experience; EXT: Extroversion; AGR: Agreeableness. Standard errors are reported in paren thesis; $^ { * } , \ ^ { * * } ,$ , and \*\*\* indicate significant difference at the 10%, 5%, and 1% levels, respectively.

[5,13], we mine the personality traits of CEOs and CFOs based solely on the Q&A section of the earnings transcripts.

## 3.2. Measures of variables

## 3.2.1. CEO/CFO personality detection

We measure CEO/CFO personality based on the big five personality framework [27]. As stated above, in addition to semantic features, syntactical features also contain important linguistic cues that reflect an individual’s personality [55]. However, traditional ML methods can only capture semantic features, and they cannot effectively detect im plicit syntactical features. Yang and Lau [17] developed an attentionbased deep learning model to mine senior executives’ personality traits based on big social media data. According to their experimental results, the personality detector significantly outperforms other state-ofthe-art personality classifiers, including Neural Networks (NB), KNN, and CNN. Accordingly, we adopt this deep learning-based personality detector to mine the personality traits of CEOs and CFOs.

3.2.1.1. Validity of the adopted personality detection method. The per sonality detector proposed by Yang and Lau [17] was trained on the myPersonality [56] and the Essays [57] datasets. Although the attention-based personality detector has been empirically tested to be effective across different data sets [17], we further verify its validity based on a new empirical experiment. In particular, our experiment involved 53 randomly selected subjects who were postgraduate students from various disciplines. Each subject was first asked to write an essay of over 150 words to describe herself. Then, each subject was asked to fill scores identified by the personality detector and those obtained via the big five questionnaires [58]. The Pearson correlation is a widely adopted statistic that measures the degree of the linear relationship between two variables. The results reported in Panel A of Table 1 show that all the coefficients of the big five personality traits are above the 0.4 threshold for strong correlation [60]. Therefore, the personality scores predicted by the personality detector have significant and strong correlations with the ground-truth values. Our experiment confirms the accuracy and reliability of the adopted personality detector. Moreover, we conduct an intraclass correlation analysis to further examine the reliability of the adopted personality detector. The intraclass correlation coefficient, a coefficient capturing both degree of correlation and agreement between two variables, is considered to be a more reliable measure than the Pearson correlation coefficient [61]. The results reported in Panel B of Table 1 show that all the coefficients of the five personality traits are above the 0.75 threshold for good reliability [61]. In sum, our experi mental results confirm the validity and reliability of the adopted per sonality detector.

## 3.2.2. Dependent variables

## M&A intensity

We use M&A frequency and value of M&A transactions as the proxie of M&A intensity [13]. M&A frequency is calculated as the total number of M&A deals announced in a year that are subsequently completed [13,18]. The value of M&A transactions is measured as the logarithm of the accumulated transaction value of M&A deals in a year [13]. Firms with no M&A deals in a year are labeled as “0” for both the M&A fre quency and the value of M&As.

## 3.2.3. Moderators

CFO personality similarity

We use two methods to measure CFO personality similarity with the CEO. First, we assign a score of “1” if the CFO has the same main per sonality type as the CEO (e.g., the dimension of openness is highest across the five personality traits for both CEO and CFO), and “0” otherwise. Second, we measure CFO personality similarity as a dummy variable, where “1” is above the average of CEO-CFO personality simi larity, and “0” otherwise. CEO-CFO personality similarity is measured by the following function:

$$
\begin{array}{r l} & \text {CEO - CFO Personality Similarity = cos(CEO Personality, CFO Personality)} \\ & = \frac {\text {CEO EXT} \times \text {CFO EXT} + \text {CEO NEU} \times \text {CFO NEU} + \text {CEO CON} \times \text {CFO CON} + \text {CEO OPN} \times \text {CFO OPN} + \text {CEO AGR} \times \text {CFO AGR}}{\sqrt {\left(\text {CEO EXT} ^ {2} + \text {CEO NEU} ^ {2} + \text {CEO CON} ^ {2} + \text {CEO OPN} ^ {2} + \text {CEO AGR} ^ {2}\right)} \times \sqrt {\left(\text {CFO EXT} ^ {2} + \text {CFO NEU} ^ {2} + \text {CFO CON} ^ {2} + \text {CFO OPN} ^ {2} + \text {CFO AGR} ^ {2}\right)}} \end{array}
$$

out the 60-item NEO five-factor inventorv-3 questionnaire to elicit her personality traits [58]. For each questionnaire, we calculated a subject’s personality score across five dimensions based on the 60-item NEO fivefactor inventory-3 and then mapped each five-dimension personality score to the corresponding essay completed by the subject in the first section. From these questionnaires, we only obtained 47 valid responses. Then, we applied the adopted personality detector to detect each sub ject’s personality scores based on the essay composed in this experiment. The distributions of these subjects’ personality scores are depicted in Table A.2 of the Appendix.

Following the methodology adopted in [59], we conducted a Pearson correlation analysis to examine the correlations between the personality

## 3.2.4. Control variables

To test our hypotheses, we create an array of control variables, including firm-level and executive-level variable as well as two other personality traits (i.e., agreeableness and extraversion). For firm-level factors, we control for the following variables: firm size [62], marketto-book ratio [21], return on assets (ROA) [63], leverage [55], and liquidity [64]. We measure firm size as the logarithm of the acquirer’s total assets. We compute the book-to-market ratio as the acquirer market value of equity over the book value of equity. We control firm perfor mance using the return on assets (ROA) by taking the net income ratio to total assets. Leverage is measured as total liabilities divided by total shareholder equity, which is used to measure how much potential borrowed capital can be leveraged to increase the returns of certain investments. Liquidity reflects the ease of changing assets to cash and is calculated as the ratio of total current assets to total current liabilities.

Table 2  
Descriptive statistics for firm-level variables (N = 1633).

<table><tr><td>Variable</td><td>Mean</td><td>SD</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>1. M&amp;A frequency</td><td>0.36</td><td>0.63</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Log (value of M&amp;As)</td><td>0.74</td><td>1.24</td><td>0.86</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. CEO NEU</td><td>0.36</td><td>0.11</td><td>-0.03</td><td>-0.03</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. CEO CON</td><td>0.42</td><td>0.13</td><td>-0.05</td><td>-0.04</td><td>0.08</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. CEO OPN</td><td>0.78</td><td>0.09</td><td>0.02</td><td>0.00</td><td>-0.05</td><td>-0.21</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. CEO EXT</td><td>0.59</td><td>0.07</td><td>-0.11</td><td>-0.11</td><td>0.24</td><td>-0.16</td><td>0.44</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. CEO AGR</td><td>0.52</td><td>0.06</td><td>0.09</td><td>0.06</td><td>0.12</td><td>-0.06</td><td>-0.04</td><td>-0.11</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>8. CFO personality similarity</td><td>0.70</td><td>0.46</td><td>-0.04</td><td>-0.02</td><td>0.03</td><td>0.09</td><td>0.10</td><td>0.14</td><td>0.14</td><td>1</td><td></td><td></td><td></td></tr><tr><td>9. CEO-CFO turnover</td><td>0.21</td><td>0.41</td><td>0.05</td><td>0.04</td><td>0.00</td><td>0.02</td><td>-0.03</td><td>-0.02</td><td>-0.02</td><td>-0.01</td><td>1</td><td></td><td></td></tr><tr><td>10. Log (CEO-CFO age difference)</td><td>0.84</td><td>0.35</td><td>0.02</td><td>0.00</td><td>0.01</td><td>-0.01</td><td>-0.05</td><td>0.01</td><td>-0.04</td><td>0.00</td><td>-0.05</td><td>1</td><td></td></tr><tr><td>11. CEO-CFO same gender</td><td>0.87</td><td>0.34</td><td>0.04</td><td>0.04</td><td>0.07</td><td>0.02</td><td>-0.06</td><td>-0.03</td><td>0.02</td><td>0.03</td><td>0.04</td><td>-0.03</td><td>1</td></tr><tr><td>12. Log (CEO-CFO tenure overlap)</td><td>0.62</td><td>0.26</td><td>-0.03</td><td>-0.02</td><td>0.05</td><td>0.08</td><td>-0.01</td><td>-0.05</td><td>-0.01</td><td>0.03</td><td>-0.09</td><td>0.03</td><td>0.02</td></tr><tr><td>13. Log (CEO tenure)</td><td>0.88</td><td>0.32</td><td>0.01</td><td>-0.01</td><td>0.07</td><td>0.15</td><td>-0.05</td><td>-0.10</td><td>0.00</td><td>-0.03</td><td>-0.05</td><td>0.21</td><td>0.02</td></tr><tr><td>14. CEO Gender</td><td>0.98</td><td>0.15</td><td>0.01</td><td>0.03</td><td>-0.01</td><td>0.01</td><td>-0.11</td><td>-0.08</td><td>0.07</td><td>0.03</td><td>0.00</td><td>0.02</td><td>0.26</td></tr><tr><td>15. Log (CEO Age)</td><td>1.75</td><td>0.05</td><td>-0.02</td><td>-0.03</td><td>0.11</td><td>0.17</td><td>-0.03</td><td>-0.01</td><td>0.01</td><td>0.04</td><td>0.00</td><td>0.33</td><td>0.08</td></tr><tr><td>16. Log (CEO Compensation)</td><td>6.47</td><td>8.80</td><td>0.04</td><td>0.09</td><td>-0.09</td><td>-0.06</td><td>0.04</td><td>-0.01</td><td>-0.01</td><td>0.03</td><td>0.00</td><td>0.03</td><td>-0.04</td></tr><tr><td>17. CEO Turnover</td><td>0.09</td><td>0.29</td><td>0.07</td><td>0.05</td><td>-0.01</td><td>-0.01</td><td>0.03</td><td>0.02</td><td>-0.02</td><td>0.02</td><td>0.63</td><td>0.00</td><td>0.05</td></tr><tr><td>18. Log (Firm Size)</td><td>3.45</td><td>0.75</td><td>0.09</td><td>0.14</td><td>0.11</td><td>0.21</td><td>0.02</td><td>0.13</td><td>-0.06</td><td>0.09</td><td>0.06</td><td>-0.02</td><td>0.01</td></tr><tr><td>19. Market-to-book Ratio</td><td>3.89</td><td>36.86</td><td>-0.02</td><td>-0.01</td><td>0.00</td><td>-0.02</td><td>0.09</td><td>0.04</td><td>-0.04</td><td>0.00</td><td>0.04</td><td>0.02</td><td>0.01</td></tr><tr><td>20. ROA</td><td>0.02</td><td>0.14</td><td>0.04</td><td>0.08</td><td>0.01</td><td>-0.03</td><td>0.02</td><td>-0.02</td><td>-0.01</td><td>-0.01</td><td>-0.03</td><td>-0.02</td><td>-0.05</td></tr><tr><td>21. Leverage</td><td>0.24</td><td>0.24</td><td>-0.01</td><td>0.02</td><td>-0.07</td><td>0.01</td><td>0.00</td><td>0.07</td><td>-0.10</td><td>0.01</td><td>0.03</td><td>0.05</td><td>0.02</td></tr><tr><td>22. Liquidity</td><td>2.37</td><td>2.36</td><td>0.00</td><td>0.01</td><td>-0.15</td><td>-0.21</td><td>-0.07</td><td>-0.33</td><td>0.12</td><td>-0.06</td><td>-0.01</td><td>0.00</td><td>0.00</td></tr><tr><td>Variable</td><td>Mean</td><td>SD</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td></tr><tr><td>12. Log (CEO-CFO tenure overlap)</td><td>0.62</td><td>0.26</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13. Log (CEO tenure)</td><td>0.88</td><td>0.32</td><td>0.51</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>14. CEO gender</td><td>0.98</td><td>0.15</td><td>0.03</td><td>0.07</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15. Log (CEO age)</td><td>1.75</td><td>0.05</td><td>0.28</td><td>0.40</td><td>0.05</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16. Log (CEO compensation)</td><td>6.47</td><td>8.80</td><td>-0.02</td><td>0.05</td><td>0.01</td><td>0.03</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17. CEO turnover</td><td>0.09</td><td>0.29</td><td>-0.02</td><td>-0.04</td><td>0.00</td><td>0.07</td><td>0.01</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18. Log (firm size)</td><td>3.45</td><td>0.75</td><td>-0.02</td><td>0.04</td><td>0.01</td><td>0.14</td><td>0.39</td><td>0.04</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>19. Market-to-book ratio</td><td>3.89</td><td>36.86</td><td>0.03</td><td>0.06</td><td>0.00</td><td>0.04</td><td>0.04</td><td>0.06</td><td>-0.01</td><td>1</td><td></td><td></td><td></td></tr><tr><td>20. ROA</td><td>0.02</td><td>0.14</td><td>0.00</td><td>0.03</td><td>-0.01</td><td>0.00</td><td>0.12</td><td>-0.04</td><td>0.16</td><td>0.01</td><td>1</td><td></td><td></td></tr><tr><td>21. Leverage</td><td>0.24</td><td>0.24</td><td>-0.07</td><td>-0.05</td><td>0.04</td><td>0.07</td><td>0.18</td><td>0.04</td><td>0.17</td><td>0.03</td><td>-0.04</td><td>1</td><td></td></tr><tr><td>22. Liquidity</td><td>2.37</td><td>2.36</td><td>0.00</td><td>-0.04</td><td>0.06</td><td>-0.05</td><td>-0.05</td><td>-0.01</td><td>-0.42</td><td>0.02</td><td>0.00</td><td>-0.16</td><td>1</td></tr></table>

Notes: NEU: Neuroticism; CON: Consciousness; OPN: Openness to Experience; EXT: Extroversion; AGR: Agreeableness.

At the executive level, we first control for CEO-related variables, including CEO age [16], gender [21], tenure [22], compensation [24], and turnover, because these factors can significantly affect firms’ M&A activities. CEO age is measured by the logarithm of a CEO’s age in a year. CEO gender receives $^ { \ast } \mathbf { 1 } ^ { \ast }$ if the CEO is a male and $\mathbf { \vec { \Delta } } ^ { 6 } \mathbf { 0 } ^ { 3 }$ if the CEO is a fe male. CEO tenure is computed as the logarithm of the years since the focal CEO begins his tenure. CEO compensation is defined as the loga rithm of the focal CEO’s total compensation (in millions USD) in a year. CEO turnover is a dummy variable, where 1 indicates that the CEO is dismissed in a year, and 0 otherwise. Second, considering that CEO-CFO demographic similarity can affect the interactions of CEO/CFO person alities, which may, in turn, affect our dependent variables, we also control for four CEO-CFO dvadic-level variables, including CEO-CFO tenure overlap, same gender, age difference, and turnover [13]. CEO-CFO tenure overlap is computed as the logarithm of shared tenure be tween CEO and CFO in the focal firm. CEO-CFO same gender is a dummy variable that is captured as 1 if CEO and CFO are in the same gender, and 0 otherwise. CEO-CFO age difference is calculated as the logarithm of the difference between CEO age and CFO age plus one. CEO-CFO turnover is a dummy variable that indicates 1 if the CEO or CFO of the focal firm is dismissed in a given year. Table 2 reports the descriptive statistics of the related variables.

## 3.3. The econometric model specification

For the relationship between CEO personality and M&A frequency, the dependent variable, M&A frequency, is a count measure with non negative integer values, many of which are equal to 0. It may violate a linear regression model's critical assumption in which the error term follows a normal distribution. To address this issue, we estimate a Poisson regression, a generalized linear regression model that allows us to count activities [18]. Poisson regression assumes that the logarithm of the dependent variable can be linearly modeled by a combination of unknown parameters. The model is shown as follow:

$$
\begin{array}{r l} M \& A f r e q u e n c y _ {i, t} = & P o i s s o n \left(\beta_ {0} + \beta_ {1} C E O C o n s c i o u s n e s s _ {i, t - 1} + C E O O p e n n e s s _ {i, t - 1} \right. \\ & \left. + \beta_ {3} C E O N e u r o t i c i s m _ {i, t - 1} + \delta X + \alpha_ {i} + \gamma_ {t} + \varepsilon_ {i, t}\right) \end{array}\tag{1}
$$

where M & A frequency is calculated as the number of M&As announced by firm i in year t that are subsequently completed. The in dependent variables are CEO consciousness, CEO openness, and CEO neuroticism. X contains a range of control variables (measured in year t-1), including CEO agreeableness, extraversion, CEO age, CEO gender, CEO tenure, CEO compensation, CEO turnover, firm size, market-to-book ratio, ROA, leverage, and liquidity. α and $\gamma _ { t }$ denote firm-fixed and year-fixed effects, respectively. $\varepsilon _ { i , \mathrm { ~ \scriptsize ~ i ~ } }$ is an error term.

For the impact of CEO personality on the value of M&A transactions, the dependent variable, value of M&As, is a continuous variable. Thus, we conduct an OLS model as follow:

$$
\begin{array}{r l} \text { Value   of } M \& A s _ {i, t} = & O L S \left(\beta_ {0} + \beta_ {1} C E O \text { Consciousness } _ {i, t - 1} + \beta_ {2} C E O \text { Openness } _ {i, t - 1} \right. \\ & \left. + \beta_ {3} C E O \text { Neuroticism } _ {i, t - 1} + \delta X + \alpha_ {t} + \gamma_ {t} + \varepsilon_ {i, t}\right) \end{array}\tag{2}
$$

where Value of M & $A s _ { i , }$ is measured by the accumulated transaction value of M&A deals of firm i in year t. The other variables in Eq. (2) are the same as those in Eq. (1).

The moderating effect of CEO-CFO personality similarity is modeled by the following equation:

$$
\begin{array}{l} M \& A f r e q u e n c y _ {i, t} (o r V a l u e s o f M \& A _ {i, t}) = P o i s s o n (o r O L S) (\beta_ {0} + \beta_ {1} C E O C o n s c i o u s n e s s _ {i, t - 1} * C F O P e r s o n a l i t y S i m i l a r i t y \\ \quad + \beta_ {2} C E O O p e n n e s s _ {i, t - 1} * C F O P e r s o n a l i t y S i m i l a r i t y + \beta_ {3} C E O N e u r o t i c i s m _ {i, t - 1} * C F O P e r s o n a l i t y S i m i l a r i t y \\ \quad + \beta_ {4} C F O P e r s o n a l i t y S i m i l a r i t y + \delta X + \alpha_ {i} + \gamma_ {t} + + \varepsilon_ {i, t}) \end{array}\tag{3}
$$

where CFO personality similarity is a dummy variable that equals “1” if the CFO has the same main personality type as the CEO or CFO person ality similarity is above the average score of cosine similarity between the CEO personality and the CFO personality, and $\mathbf { \vec { \Delta } } ^ { 6 } 0 ^ { 3 } \mathbf { \vec { \Delta } }$ otherwise.

## 4. Empirical results

## 4.1. Main results of H1 to H4

In H1, H2, and H3, we propose that CEO conscientiousness and neuroticism are negatively associated with M&A frequency and value, while CEO openness has a positive association. Table 3 reports the corresponding results. Columns 1 and 4 are baselines. Column 2 of Table 3 reports the result of the Poisson regression for M&A frequency. The coefficient estimate of CEO consciousness is negative and statistically significant, thus supporting H1. It equals − 0.308 (p < 0.01), suggesting that one unit increase in CEO consciousness will lead to a 30.8% decrease in the number of M&As. The coefficient estimate of CEO openness is positive and statistically significant, thereby supporting H2. It equals 0.168 $( p < 0 . 0 1 )$ , suggesting that one unit increase in CEO openness will give rise to a 16.8% increase in the number of M&As. The coefficient estimate of CEO neuroticism is negative and statistically significant (β = − 0.166, p < 0.01), supporting H3. Column 5 of Table 3 reports the result for the value of M&As. The coefficient estimates of CEO consciousness and CEO neuroticism are negative and statistically significant $( \beta = - \ 0 . 1 8 0 , p < 0 . 0 1 ; \beta = - \ 0 . 1 0 2 , \ p < 0 . 0 1 )$ , thereby supporting H1 and H3, respectively. Similarly, the coefficient estimate of CEO openness is positive and statistically significant $( \beta = 0 . 0 5 9 , \rho <$ 0.01), supporting H2.

Table 4 is used to test the moderating effects of CFO personality

Table 3 Results H1, H2, and H3.

<table><tr><td rowspan="3">Variable</td><td colspan="3">M&amp;A frequency (Poisson model)</td><td colspan="3">Value of M&amp;As (OLS model)</td></tr><tr><td>Baseline</td><td>Predicted</td><td>Corrected</td><td>Baseline</td><td>Predicted</td><td>Corrected</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>CEO CON</td><td></td><td>-0.308*** (0.054)</td><td>-0.521*** (0.061)</td><td></td><td>-0.180*** (0.038)</td><td>-0.294*** (0.042)</td></tr><tr><td>CEO OPN</td><td></td><td>0.168*** (0.047)</td><td>0.241*** (0.062)</td><td></td><td>0.059* (0.031)</td><td>0.072* (0.048)</td></tr><tr><td>CEO NEU</td><td></td><td>-0.166*** (0.047)</td><td>-0.283*** (0.067)</td><td></td><td>-0.102*** (0.033)</td><td>-0.17*** (0.053)</td></tr><tr><td>CEO EXT</td><td>-0.054 (0.042)</td><td>0.003 (0.046)</td><td>0.042 (0.066)</td><td>-0.041 (0.031)</td><td>-0.007 (0.033)</td><td>0.008 (0.055)</td></tr><tr><td>CEO AGR</td><td>0.026 (0.042)</td><td>0.114 (0.049)</td><td>0.122 (0.073)</td><td>-0.003 (0.031)</td><td>0.052 (0.034)</td><td>0.105 (0.068)</td></tr><tr><td>CEO tenure</td><td>0.054 (0.046)</td><td>0.048 (0.047)</td><td>0.046 (0.047)</td><td>0.016 (0.033)</td><td>0.008 (0.033)</td><td>0.004 (0.033)</td></tr><tr><td>CEO turnover</td><td>0.117*** (0.036)</td><td>0.118*** (0.036)</td><td>0.117*** (0.039)</td><td>0.064** (0.030)</td><td>0.062** (0.030)</td><td>0.061* (0.031)</td></tr><tr><td>CEO gender</td><td>0.024 (0.045)</td><td>0.028 (0.045)</td><td>-0.004 (0.062)</td><td>0.036 (0.031)</td><td>0.028 (0.030)</td><td>0.026 (0.029)</td></tr><tr><td>CEO age</td><td>-0.085* (0.046)</td><td>-0.072 (0.048)</td><td>-0.060 (0.050)</td><td>-0.067** (0.034)</td><td>-0.055 (0.034)</td><td>-0.046 (0.031)</td></tr><tr><td>CEO compensation</td><td>-0.008 (0.044)</td><td>-0.042 (0.051)</td><td>-0.069 (0.059)</td><td>0.020 (0.034)</td><td>0.002 (0.034)</td><td>-0.012 (0.037)</td></tr><tr><td>Firm size</td><td>0.191*** (0.050)</td><td>0.213*** (0.052)</td><td>0.224*** (0.057)</td><td>0.210 *** (0.037)</td><td>0.230*** (0.038)</td><td>0.245*** (0.044)</td></tr><tr><td>Market-to-book ratio</td><td>-0.071 (0.067)</td><td>-0.062 (0.065)</td><td>-0.061 (0.079)</td><td>-0.020 (0.030)</td><td>-0.014 (0.030)</td><td>-0.012 (0.066)</td></tr><tr><td>ROA</td><td>0.056 (0.045)</td><td>0.040 (0.046)</td><td>0.027 (0.062)</td><td>0.060* (0.031)</td><td>0.050 (0.034)</td><td>0.044 (0.035)</td></tr><tr><td>Leverage</td><td>-0.043 (0.046)</td><td>-0.011 (0.048)</td><td>0.009 (0.049)</td><td>0.006 (0.032)</td><td>0.017 (0.031)</td><td>0.020 (0.030)</td></tr><tr><td>Liquidity</td><td>0.061 (0.044)</td><td>-0.060 (0.054)</td><td>-0.139** (0.061)</td><td>0.095*** (0.034)</td><td>0.027 (0.036)</td><td>-0.013 (0.037)</td></tr><tr><td>Constant</td><td>-1.058*** (0.043)</td><td>-1.109 *** (0.045)</td><td>-1.139 (0.052)</td><td>0.739*** (0.030)</td><td>0.739*** (0.030)</td><td>0.739*** (0.028)</td></tr><tr><td>Firm fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>#Obs.</td><td>1633</td><td>1633</td><td>1633</td><td>1633</td><td>1633</td><td>1633</td></tr><tr><td>Pseudo - R2</td><td>0.084</td><td>0.137</td><td>0.142</td><td></td><td></td><td></td></tr><tr><td>Adj. R2</td><td></td><td></td><td></td><td>0.110</td><td>0.148</td><td>0.159</td></tr><tr><td> $\chi^2$ </td><td>35.80***</td><td>94.22***</td><td>101.55***</td><td></td><td></td><td></td></tr></table>

Note: Column 1 and column 3, labeled as “Baseline”, report controls; column 2 and column 4, labeled as “Predicted”, report estimated coefficients obtained using predicted personality traits by the adopted personality detector; column 3 and column 6, labeled as “Corrected”, report corrected estimates through the application of the SIMEX method. Standard errors are reported in parenthesis; \*, \*\*, and \*\*\* indicate significant difference at the 10%, 5%, and 1% levels, respectively.

Table 4  
Moderating effects of CFO personality similarity.

<table><tr><td rowspan="2">Variable</td><td>M&amp;A frequency</td><td>Value of M&amp;As</td><td>M&amp;A frequency</td><td>Value of M&amp;As</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>CEO CON</td><td>-0.432***(0.072)</td><td>-0.303***(0.048)</td><td>-0.273***(0.056)</td><td>-0.164***(0.039)</td></tr><tr><td>CEO OPN</td><td>0.295***(0.074)</td><td>0.130***(0.048)</td><td>0.207***(0.047)</td><td>0.096***(0.033)</td></tr><tr><td>CEO NEU</td><td>-0.182**(0.079)</td><td>-0.090*(0.055)</td><td>0.161**(0.061)</td><td>0.017 (0.074)</td></tr><tr><td>CFO personality Similarity (Mean)</td><td>0.437 (0.444)</td><td>0.135 (0.304)</td><td></td><td></td></tr><tr><td>CFO personality Similarity (Mean) × CEO CON</td><td>-0.922**(0.385)</td><td>-0.550**(0.252)</td><td></td><td></td></tr><tr><td>CFO personality Similarity (Mean) × CEO OPN</td><td>0.456***(0.142)</td><td>0.451***(0.096)</td><td></td><td></td></tr><tr><td>CFO personality Similarity (Mean) × CEO NEU</td><td>0.0790 (0.163)</td><td>-0.027 (0.113)</td><td></td><td></td></tr><tr><td>CFO personality Similarity (Main type)</td><td></td><td></td><td>0.104 (0.149)</td><td>0.047 (0.099)</td></tr><tr><td>CFO personality Similarity (Main type) × CEO CON</td><td></td><td></td><td>-0.296*(0.045)</td><td>-0.206*(0.034)</td></tr><tr><td>CFO personality Similarity (Main type) × CEO OPN</td><td></td><td></td><td>-0.128***(0.046)</td><td>-0.074**(0.034)</td></tr><tr><td>CFO personality Similarity (Main) × CEO NEU</td><td></td><td></td><td>-0.304*(0.171)</td><td>-0.200 (0.115)</td></tr><tr><td>CEO EXT</td><td>0.000 (0.046)</td><td>-0.013 (0.033)</td><td>0.015 (0.047)</td><td>-0.004 (0.033)</td></tr><tr><td>CEO AGR</td><td>0.014 (0.049)</td><td>0.039 (0.035)</td><td>0.112**(0.049)</td><td>0.048 (0.035)</td></tr><tr><td>CEO-CFO turnover</td><td>0.013 (0.054)</td><td>0.012 (0.039)</td><td>0.013 (0.054)</td><td>0.009 (0.039)</td></tr><tr><td>CEO-CFO age difference</td><td>0.059 (0.046)</td><td>0.027 (0.032)</td><td>0.077*(0.046)</td><td>0.037 (0.032)</td></tr><tr><td>CEO-CFO same gender</td><td>0.094**(0.047)</td><td>0.065**(0.031)</td><td>0.093**(0.047)</td><td>0.059*(0.031)</td></tr><tr><td>CEO-CFO tenure overlap</td><td>-0.031 (0.049)</td><td>0.016 (0.035)</td><td>-0.032 (0.049)</td><td>0.010 (0.035)</td></tr><tr><td>CEO tenure</td><td>0.060 (0.052)</td><td>-0.003 (0.037)</td><td>0.059 (0.052)</td><td>0.000 (0.038)</td></tr><tr><td>CEO turnover</td><td>0.106**(0.050)</td><td>0.053 (0.038)</td><td>0.110**(0.050)</td><td>0.057 (0.039)</td></tr><tr><td>CEO gender</td><td>-0.021(0.047)</td><td>0.011 (0.031)</td><td>-0.015 (0.047)</td><td>0.016 (0.031)</td></tr><tr><td>CEO age</td><td>-0.092*(0.050)</td><td>-0.067*(0.035)</td><td>-0.105**(0.050)</td><td>-0.076**(0.035)</td></tr><tr><td>CEO compensation</td><td>-0.039 (0.050)</td><td>-0.002 (0.034)</td><td>-0.033 (0.052)</td><td>0.004 (0.034)</td></tr><tr><td>Firm size</td><td>0.205***(0.052)</td><td>0.233***(0.037)</td><td>0.225***(0.052)</td><td>0.244***(0.038)</td></tr><tr><td>Market-to-book ratio</td><td>-0.074 (0.063)</td><td>-0.025 (0.030)</td><td>-0.069 (0.065)</td><td>-0.017 (0.030)</td></tr><tr><td>ROA</td><td>0.032 (0.047)</td><td>0.040 (0.030)</td><td>0.039 (0.046)</td><td>0.047 (0.031)</td></tr><tr><td>Leverage</td><td>-0.018 (0.048)</td><td>0.004 (0.031)</td><td>-0.019 (0.048)</td><td>0.015 (0.031)</td></tr><tr><td>Liquidity</td><td>-0.045 (0.054)</td><td>0.041 (0.036)</td><td>-0.059 (0.054)</td><td>0.026 (0.036)</td></tr><tr><td>Constant</td><td>-1.131***(0.045)</td><td>0.739***(0.030)</td><td>-1.123***(0.045)</td><td>0.739 (0.030)</td></tr><tr><td>Firm fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>#Obs.</td><td>1633</td><td>1633</td><td>1633</td><td>1633</td></tr><tr><td>Pseudo - R2</td><td>0.139</td><td></td><td>0.122</td><td></td></tr><tr><td>Adj.R2</td><td></td><td>0.154</td><td></td><td>0.152</td></tr><tr><td>χ2</td><td>119.96***</td><td></td><td>114.47***</td><td></td></tr></table>

Note: Standard errors are reported in parenthesis; \*, \*\*, and \*\*\* indicate significant difference at the 10%, 5%, and 1% levels, respectively.

similarity (H4). Columns 1 and 2 of Table 4 report the results when CFO personality similarity is based on the cosine similarity between CEO-CFO big five personality traits. In column 1, the coefficient estimate of CEO CON × CFO Personality Similarity is negative and statistically significant $( \beta = - \ 0 . 9 2 2 , p < 0 . 0 5 )$ , indicating that the negative effect of CEO consciousness on M&A frequency is stronger when a CFO has a similar personality as the CEO (see Fig. 1a). The coefficient estimate of CEO OPN × CFO Personality Similarity is positive and statistically sig nificant $( \beta = 0 . 4 5 6 , p < 0 . 0 1 )$ , indicating that the positive effect of CEO openness on M&A frequency is more substantial when a CFO has a similar personality as the CEO (See Fig. 1b). The coefficient estimate on CEO NEU × CFO Personality Similarity is positive but not significant, indicating that the negative effect of CEO neuroticism on M&A fre quency is not significantly affected by a similar CFO. A possible un derlying reason is that the proportion of neurotic CEOs is lowest (0.31%) among all the personality components and the possibility of CFOs hav ing a similar personality is even lower, thus leading to the insignificance of CFO personality similarity on the relationship between CEO neurot icism and M&A intensity. In column $^ { 2 , }$ the dependent variable is the value of M&As, and we observe similar results. Columns 3 and 4 of Table 4 report the moderating results when CFO personality similarity is measured by whether the CEO and CFO share the same main type of personality across five dimensions. The empirical findings yield consistent results with those presented in columns 1 and 2. Therefore. H4 is partially supported.

## 4.2. Pairwise interplay of CEO-CFO personality traits

In this subsection, we go beyond our previous findings regarding H4 and show the results capturing the effect of CEO-CFO pairwise person ality traits on M&A intensity. Table 5 presents the corresponding results. In particular, the results reported in columns 1 and 2 show that a CEO-CFO dyad characterized by high consciousness (high CON (CEO) × high CON (CFO)) has a more negative influence on M&A frequency (β = − $0 . 7 2 3 , p < 0 . 0 1 )$ and transaction values $( \beta = - \ 0 . 4 3 6 , \ p < 0 . 0 1 )$ than a dyad characterized by low consciousness (low CON (CEO) × low CON (CFO)). Our results are consistent with the findings of prior literature in that conscientious executives are shown more rely on “dependable, tried-and-true strategies”, and tend to reject new and challenging stra tegies that deviate from their experience [4]. Similarly, our study also reveals that a pair with high neuroticism (high NEU (CEO) × high NEU (CFO)) is more negatively associated with both M&A frequency and transaction values than a pair with low neuroticism (low NEU (CEO) × low NEU (CFO))

Moreover, our finding adheres to prior literature showing that a high level of neuroticism is correlated to negative behaviors [65]. As for CEO-CFO pairwise personality on openness, we find that executives with a high level of openness are more likely to increase M&A intensity than a pair with a low level of openness. Considering the effect on M&A fre quency, combinations of high OPN (CEO) × high OPN (CFO) (β = 0.156, $p < 0 . 0 5 )$ , high OPN (CEO) × low OPN (CFO) (β = 0.133, p < 0.1), and low OPN (CEO) × high OPN (CFO) $( \beta = 0 . 1 4 4 , \ p < 0 . 0 5 )$ have stronger positive correlations with the number of M&As than the combination of low OPN (CEO) × low OPN (CFO) $( \beta = 0 . 0 9 4 , p > 0 . 1 )$ . Our empirical results support prior literature that executives with a higher level of openness can quickly identify outside information that deviates from existing mindsets, and so they better recognize and seize alternative strategic opportunities [4,43]. In summary, these results illustrate the effects of pairwise combinations of CEO-CFO personality traits on M&A intensity.

![](/api/attachments/3A88HCAW/fulltext/images/ce5f06858bc710bed3cf6351acede5cc66a77fc5483aff323e298e07657c2f75.jpg)

![](/api/attachments/3A88HCAW/fulltext/images/2ffbb0acb70d1f0520bf753068aba6d4db725d11221e149ce9de739c2d62440a.jpg)

![](/api/attachments/3A88HCAW/fulltext/images/efbde86b4208e57f419ed151c3909d0a5c79cb5fcd18373eb94b03c25a8101f9.jpg)

![](/api/attachments/3A88HCAW/fulltext/images/8667d32343909b555628a0b66b032b93a47cb933fdd15eb390f40627c6ea67b4.jpg)  
Fig. 1. Moderating effect of CFO personality similarity.

## 5. Robustness tests

## 5.1. Controlling for data mining errors

As data mining methods may not be perfect, our adopted personality detector inevitably causes a predictive error. This predictive error is then transmitted to our econometric models and is manifested as a measure ment error [66]. To mitigate such bias, we introduce the simulation extrapolation method (SIMEX) [67], which has an advantage in cor recting the measurement errors caused by data mining methods. This method is best for a situation in which the sample data is labeled, and thus the measurement error variance in a continuous variable can be calculated or is known. However, it can also be generalized to situations where data is unlabeled [66]. In our case, because the earnings call dataset is unlabeled, it is difficult to compute the exact error variance generated by the adopted personality detector. Farnadi, Zoghbi, Moens and Cock [68] provided experimental evidence that ML-based person ality detectors are effective across different domains. According to published experimental results [17] and the validation experiment re ported in this paper, we once again show that the adopted personality detector is effective across different domains and data sets. Since the adopted personality detector produced a higher predictive error in the benchmark Essays corpus [17] than that produced in the validation experiment reported in this paper, we adopt the predictive error asso ciated with personality detection against the Essays corpus in our SIMEX

computation.

Comparing the predicted values of personality traits with the ground-truth values in the Essays corpus, we obtain a $5 \times 5$ covariance matrix of the predictor error of the personality detector. After that, we follow a two-stage SIMEX correction. In the first simulation stage, we select a fixed set of values $\{ \lambda _ { 1 , } \lambda _ { 2 } , . . . , \lambda _ { 1 6 3 3 } \}$ }. Then, we generate a set of independent variables $\left\{ \widehat { X } \left( \lambda _ { 1 } \right) , \widehat { X } \left( \lambda _ { 2 } \right) , . . . , \widehat { X } \left( \lambda _ { 1 6 3 3 } \right) \right\}$ that contain mea surement errors. Taking one of the independent variables, consciousness (abbreviation: CON), as an example, we simulate the impact of mea surement error in CON with CON<sup>̂</sup> $\left( \lambda _ { k } \right) = C O N + e \left( \lambda _ { k } \right)$ , where $e { \sim } N ( 0 , \sigma _ { e } ^ { 2 } )$ and e (λ ) has a variance of $( 1 + \lambda _ { k } ) \sigma _ { e } ^ { 2 } ( \mathbf { k } \in \{ 1 , 2 , . . . , 1 6 3 3 \} )$ . In the second extrapolation stage, a parameter model, θ (λ), is estimated and extrap olated to the level (θ (− 1)), where measurement error reduces to 0. Extrapolation plots are reported in Fig. 2, and corrected results are re ported in columns 3 and 6 of Table 3. The results show that the econometric models are well corrected through the application of the SIMEX method.

## 5.2. Controlling for endogeneity

Our study could easily be subject to the endogeneity problem due to the reverse casualty and unobserved omitted variables. One common concern is that the board of directors may purposefully select CEOs with particular personalities to fulfill their M&A needs. CEO selection research demonstrates that a CEO may be chosen or selected by a firm whose strategy fits the CEO’s personality [69]. As a result, CEOs whose personalities are conducive to the firms’ strategies are more likely to be hired, while incompatible CEOs are more likely to be rejected. To address the endogeneity issue caused by reverse casualty, we employ dynamic panel models [70]. Specifically, the lagged values of our dependent variables (i.e., M&A Frequency<sub>i,t-1</sub>, M&A Frequency<sub>i,t-2</sub>, Value of $M \mathcal { k } A s _ { i , t - 1 } ,$ Value of $M \mathcal { E } A s _ { i , t - 2 } )$ are introduced to the regression models in the main analysis.

Another concern is the endogeneity caused by unobserved omitted variables. First, an acquirer firm’s M&A experience may affect the re lationships between CEO personality and M&A intensity. To alleviate this concern, we follow the measure developed by Cuypers, Cuypers and Martin [71] and calculate an acquirer’s M&A experience as the logarithm of one plus the total number of M&A deals that the firm completed during the 10 vears prior to the focal M&A. In addition, as high-tech firms account for the largest number of the 290 public firms and 584 M&A deals in our sample, this may possibly cause disproportionate ef fects of CEO/CFO personality matching on M&A intensity between high tech and non-high-tech firms. Therefore, we address this issue by adding a new control variable, High Tech, which is a dummy variable that equals “1” if the firm is from the high technology industry, and 0 otherwise. Columns 1 and 2 of Table 6 report the corresponding results of the incorporation of M&A Frequency , M&A Frequency , Value of M&A $T r a n s a c t i o n _ { i , t - l } ,$ , Value of M&A Transaction , M&A experience, and High Tech. It can be seen that our focal variables of interest are still qualita tively significant after the introduction of these variables. Collectively, these findings alleviate the concerns on reverse causality and unob served omitted variables that may change our main results.

Table 5  
Pairwise combinations of CEO-CFO personality traits.

<table><tr><td>Variable</td><td>M&amp;A frequency(1)</td><td>Value of M&amp;As(2)</td><td>M&amp;A frequency(3)</td><td>Value of M&amp;As(4)</td><td>M&amp;A frequency(5)</td><td>Value of M&amp;As(6)</td></tr><tr><td>High CON (CEO)×High CON (CFO)</td><td>-0.723***(0.103)</td><td>-0.436***(0.069)</td><td></td><td></td><td></td><td></td></tr><tr><td>High CON (CEO)×Low CON (CFO)</td><td>-0.505***(0.085)</td><td>-0.407***(0.059)</td><td></td><td></td><td></td><td></td></tr><tr><td>Low CON (CEO)×High CON (CFO)</td><td>-0.685***(0.092)</td><td>-0.278***(0.060)</td><td></td><td></td><td></td><td></td></tr><tr><td>Low CON (CEO)×Low CON (CFO)</td><td>-0.486***(0.081)</td><td>-0.314***(0.056)</td><td></td><td></td><td></td><td></td></tr><tr><td>High OPN (CEO)×High OPN (CFO)</td><td></td><td></td><td></td><td></td><td>0.156**(0.042)</td><td>0.127**(0.042)</td></tr><tr><td>High OPN (CEO)×Low OPN (CFO)</td><td></td><td></td><td></td><td></td><td>0.133*(0.042)</td><td>0.128(0.044)</td></tr><tr><td>Low OPN (CEO)×High OPN (CFO)</td><td></td><td></td><td></td><td></td><td>0.144**(0.037)</td><td>0.114**(0.042)</td></tr><tr><td>Low OPN (CEO)×Low OPN (CFO)</td><td></td><td></td><td></td><td></td><td>0.094(0.057)</td><td>0.082(0.044)</td></tr><tr><td>High NEU (CEO)×High NEU (CFO)</td><td></td><td></td><td>-0.290***(0.092)</td><td>-0.213***(0.061)</td><td></td><td></td></tr><tr><td>High NEU (CEO)×Low NEU (CFO)</td><td></td><td></td><td>-0.194***(0.073)</td><td>-0.128*(0.050)</td><td></td><td></td></tr><tr><td>Low NEU (CEO)×High NEU (CFO)</td><td></td><td></td><td>-0.071(0.070)</td><td>-0.065(0.050)</td><td></td><td></td></tr><tr><td>Low NEU (CEO)×Low NEU (CFO)</td><td></td><td></td><td>-0.209**(0.082)</td><td>-0.150***(0.056)</td><td></td><td></td></tr><tr><td>CEO CON</td><td></td><td></td><td>-0.327***(0.054)</td><td>-0.189***(0.038)</td><td>-0.341***(0.054)</td><td>-0.204***(0.039)</td></tr><tr><td>CEO OPN</td><td>0.189**(0.047)</td><td>0.081***(0.031)</td><td>0.163***(0.047)</td><td>0.066**(0.031)</td><td></td><td></td></tr><tr><td>CEO NEU</td><td>-0.128**(0.051)</td><td>-0.075**(0.034)</td><td></td><td></td><td>-0.156***(0.051)</td><td>-0.099*(0.036)</td></tr><tr><td>CFO CON</td><td></td><td></td><td>0.073(0.050)</td><td>0.028(0.037)</td><td>0.044(0.055)</td><td>0.014(0.041)</td></tr><tr><td>CFO OPN</td><td>0.115(0.045)</td><td>-0.102(0.033)</td><td>-0.068(0.044)</td><td>-0.074**(0.033)</td><td></td><td></td></tr><tr><td>CFO NEU</td><td>-0.093*(0.054)</td><td>-0.085**(0.037)</td><td></td><td></td><td>0.004(0.052)</td><td>-0.017(0.036)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Firm fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>#Obs.</td><td>1633</td><td>1633</td><td>1633</td><td>1633</td><td>1633</td><td>1633</td></tr><tr><td>Pseudo -  $R^2$ </td><td>0.150</td><td></td><td>0.142</td><td></td><td>0.136</td><td></td></tr><tr><td>Adj.  $R^2$ </td><td></td><td>0.165</td><td></td><td>0.151</td><td></td><td>0.147</td></tr><tr><td> $\chi^2$ </td><td>126.51***</td><td></td><td>105.49***</td><td></td><td>90.63***</td><td></td></tr></table>

Note: Standard errors are reported in parenthesis; \*, \*\*, and \*\*\* indicate significant difference at the 10%, 5%, and 1% levels, respectively.

## 5.3. CEO tenure starts after CFO tenure

It is also possible that CEOs may select CFOs who have similar per sonalities such that these CFOs can ingratiate themselves with CEOs in terms of strategic decision making, which may lead to biased results. To rule out such concern, we retest our hypotheses using a subsample in which CEOs take tenure later than CFOs. Under this condition, it is unlikely that CEOs would select CFOs with similar personalities in advance. The results reported in columns 3–6 of Table 6 demonstrate that the moderating effect of CFO personality similarity with CEO is still statistically significant.

## 5.4. Executives’ comments of less than 2000 words

Someone may argue that the personalities of CEOs and CFOs who speak fewer words during earnings conferences are more difficult to accurately predict with our adopted personality detector. To mitigate this concern, we remove any senior executive who contributes less than 2000 words during the Q&A section of an earnings call transcript. Accordingly, we test the robustness of our main findings by remeasuring CEO personality based on this sub dataset. Unreported empirical results yield consistent findings with those in the main analysis.

## 6. Summary and managerial implications

## 6.1. Concluding remarks

This study proposes an econometric analysis model empowered by novel machine learning-based personality constructs to empirically examine the impact of the interplay between senior executives’ per sonality traits on corporate M&A intensity. In particular, our empirical results show that CEO openness is positively and significantly associated with corporate M&A intensity (e.g., the frequency and amount of M&A deals), while CEO consciousness and neuroticism are negatively asso ciated with corporate M&A intensity. Moreover, the effects of CEO consciousness, openness, and neuroticism on M&A intensity become stronger when CFOs have similar personality traits as those of CEOs. We further study the dyadic combinations of CEO-CFO specific personality characteristics. Our empirical results reveal that the CEO-CFO pairs with high openness, low consciousness, or low neuroticism undertake more M&A deals than those with low openness, high consciousness, and high neuroticism. In sum, the proposed econometric model leads to novel findings regarding how the interplay between the personality traits of

![](/api/attachments/3A88HCAW/fulltext/images/9bbda49e6687eff2f9ad63dc6907b3f5f0a3add996aa5030fbc39e23dacd0c2d.jpg)  
(a) CEO Conciousness on M&A Frequency

![](/api/attachments/3A88HCAW/fulltext/images/6629c77e567978e3b1cf978873ae2f278777feb196626c2fe4d1e75fb4902626.jpg)  
(b) CEO Conciousness on Value of M&As

![](/api/attachments/3A88HCAW/fulltext/images/3f24fc45e04164819e8bcae1543d09d530ff664a44e239d1d28b27d9c6921fd9.jpg)  
(c) CEO Openness on M&A Frequency

![](/api/attachments/3A88HCAW/fulltext/images/67569859b7fecb22fceb6c45e00800b492f548fa0ad654835439965c658e27db.jpg)  
(d) CEO Openness on Value of M&As

![](/api/attachments/3A88HCAW/fulltext/images/3ac9f70ebb7fade485dec1803d6e64d3b43c63044da08502901760a2c3f31ec1.jpg)  
(e) CEO Neuroticism on M&A Frequency

![](/api/attachments/3A88HCAW/fulltext/images/573c29213c3c0e821e0be92f2e3081333bb166eaecc9c217eb07ab621c800edf.jpg)  
(f) CEO Neuroticism on Value of M&As  
Fig. 2. SIMEX simulation extrapolation.

CEOs and CFOs may strengthen or attenuate corporate M&A activities.

## 6.2. Theoretical contributions and managerial implications

This study makes several theoretical contributions to existing liter ature. First, we propose an econometric analysis model empowered by novel ML-based personality constructs to examine the impact of CEO personality traits on corporate M&A intensity. Second, while previous research studied the relationships between the personal characteristics of CEOs, such as tenure [22] or overconfidence [6], and corporate M&A activities, the joint influence of CEOs and CFOs on corporate M&A in tensity is not reported in existing literature. Accordingly, we extend the existing IS literature [8–10] by studying the impact of personality sim ilarity between CEOs and CFOs, and the dyadic combinations of CEO-CFO personality traits on corporate M&A activities. To the best of our knowledge, this is the first successful econometric analysis empowered by ML-based personality constructs to empirically examine the interplay between the personality traits of CEOs and CFOs and to explore their impact on corporate M&A intensity.

Table 6 Robustness tests.

<table><tr><td>Variable</td><td>M&amp;A frequency(1)</td><td>Value of M&amp;As(2)</td><td>M&amp;A frequency(3)</td><td>Value of M&amp;As(4)</td><td>M&amp;A frequency(5)</td><td>Value of M&amp;As(6)</td></tr><tr><td>CEO NEU</td><td>-0.148***(0.054)</td><td>-0.071***(0.035)</td><td>0.001 (0.161)</td><td>0.024 (0.105)</td><td>0.174 (0.186)</td><td>0.124 (0.131)</td></tr><tr><td>CEO CON</td><td>-0.289***(0.056)</td><td>-0.148***(0.039)</td><td>-0.373***(0.132)</td><td>-0.346***(0.089)</td><td>-0.238**(0.104)</td><td>-0.185***(0.070)</td></tr><tr><td>CEO OPN</td><td>0.152***(0.046)</td><td>0.051*(0.030)</td><td>0.482***(0.165)</td><td>0.223**(0.096)</td><td>0.227**(0.092)</td><td>0.176 (0.059)</td></tr><tr><td>M &amp; A frequency-1</td><td>0.158***(0.033)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M &amp; A frequency-2</td><td>0.186***(0.039)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Value of M &amp; As-1</td><td></td><td>0.121***(0.031)</td><td></td><td></td><td></td><td></td></tr><tr><td>Value of M &amp; As-2</td><td></td><td>0.171***(0.033)</td><td></td><td></td><td></td><td></td></tr><tr><td>M&amp;A experience</td><td>0.194***(0.053)</td><td>-0.092**(0.037)</td><td></td><td></td><td></td><td></td></tr><tr><td>High tech</td><td>0.056 (0.048)</td><td>0.063*(0.034)</td><td></td><td></td><td></td><td></td></tr><tr><td>CFO personality similarity(Mean)</td><td></td><td></td><td>1.388 (0.107)</td><td>0.793 (0.122)</td><td></td><td></td></tr><tr><td>CFO personality similarity(Mean) × CEO NEU</td><td></td><td></td><td>-0.057 (0.113)</td><td>-0.235 (0.105)</td><td></td><td></td></tr><tr><td>CFO personality similarity(Mean) × CEO CON</td><td></td><td></td><td>-1.856**(0.122)</td><td>-1.183***(0.109)</td><td></td><td></td></tr><tr><td>CFO personality similarity(Mean) × CEO OPN</td><td></td><td></td><td>0.473*(0.262)</td><td>0.537***(0.537)</td><td></td><td></td></tr><tr><td>CFO personality similarity(Main type)</td><td></td><td></td><td></td><td></td><td>0.18 (0.116)</td><td>0.190 (0.127)</td></tr><tr><td>CFO personality similarity(Main type) × CEO NEU</td><td></td><td></td><td></td><td></td><td>-0.400 (0.129)</td><td>-0.010 (0.138)</td></tr><tr><td>CFO personality similarity(Main type) × CEO CON</td><td></td><td></td><td></td><td></td><td>-0.160**(0.087)</td><td>-0.381*(0.060)</td></tr><tr><td>CFO personality similarity(Main type) × CEO OPN</td><td></td><td></td><td></td><td></td><td>0.172**(0.085)</td><td>0.136**(0.062)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Firm fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>#Obs.</td><td>1633</td><td>1633</td><td>500</td><td>500</td><td>500</td><td>500</td></tr><tr><td>Pseudo - R2</td><td>0.125</td><td></td><td>0.137</td><td></td><td>0.147</td><td></td></tr><tr><td>Adj. R2</td><td></td><td>0.132</td><td></td><td>0.159</td><td></td><td>0.161</td></tr><tr><td>χ2</td><td>154.87 ***</td><td></td><td>40.93***</td><td></td><td>53.82***</td><td></td></tr></table>

Note: Standard errors are reported in parenthesis; $^ { * } , ^ { * * } ,$ , and \*\*\* indicate significant difference at the 10%, 5%, and 1% levels, respectively.

Table A.2  
Subjects’ personality score distributions in our validation experiment.

<table><tr><td>Personality trait</td><td>Obs.</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Panel A: Self-report personality scores in the validation experiment</td></tr><tr><td>Consciousness</td><td>47</td><td>0.568</td><td>0.112</td><td>0.333</td><td>0.833</td></tr><tr><td>Openness</td><td>47</td><td>0.571</td><td>0.130</td><td>0.150</td><td>0.800</td></tr><tr><td>Neuroticism</td><td>47</td><td>0.560</td><td>0.084</td><td>0.400</td><td>0.783</td></tr><tr><td>Extroversion</td><td>47</td><td>0.592</td><td>0.085</td><td>0.350</td><td>0.717</td></tr><tr><td>Agreeableness</td><td>47</td><td>0.526</td><td>0.115</td><td>0.133</td><td>0.667</td></tr><tr><td colspan="6">Panel B: Personality scores detected by the adopted personality detector in the validation experiment</td></tr><tr><td>Consciousness</td><td>47</td><td>0.495</td><td>0.200</td><td>0.109</td><td>0.931</td></tr><tr><td>Openness</td><td>47</td><td>0.588</td><td>0.225</td><td>0.107</td><td>0.945</td></tr><tr><td>Neuroticism</td><td>47</td><td>0.501</td><td>0.131</td><td>0.303</td><td>0.828</td></tr><tr><td>Extroversion</td><td>47</td><td>0.563</td><td>0.130</td><td>0.227</td><td>0.808</td></tr><tr><td>Agreeableness</td><td>47</td><td>0.532</td><td>0.210</td><td>0.077</td><td>0.892</td></tr></table>

The managerial implications of our research are as follows. First, corporate decision makers of the acquirer firms can apply the proposed model to extract and analyze the personality traits of senior executives at the target firms, and thereby, they can better formulate appropriate M&A strategies given the specific characteristics of their counterparts. Second, our research facilitates corporate human resource management in general and corporate hiring in particular. By mining and analyzing the personality traits of a firm’s board of management, appropriate corporate hiring strategies could be developed for recruiting senior ex ecutives whose personality traits can supplement those of other mem bers residing in the board of management. Finally, institutional investors can apply the proposed model to mine and analyze the per sonality traits of the senior executives of the target firms, and hence make more informed financial investment decisions by considering the strengths and weaknesses of the TMT of the investment targets.

## 6.3. Limitations and future research directions

Our study has several limitations. First, this study examines the ef fects of CEO and CFO psychological orientations (i.e., personality) and their impact on corporate M&A intensity. Future study could exploit the effect of CEO-CFO behavioral integration on corporate strategic decision making. Second, this study investigates CEO-CFO personality similarity in terms in the context of M&As, while CEO-CFO personality difference might also strengthen each other in other business contexts. Future research may also explore the roles of CEO-CFO personality difference in other contexts. Third, this study focuses on the CEO-CFO dyad. Future research may investigate the impact of other kinds of executive dyads, such as the CEO and chief technology officer (CTO). Finally, although the adopted personality detection method can automatically mine ex ecutives’ personality traits from earnings call transcripts, it may contain measurement errors. Hence, future research will incorporate personality mining from multiple data sources (e.g., online social media) such that the results of personality mining can be cross-checked and corrected.

## Acknowledgement

Our research work was partly supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (Projects: CityU 11525716), the NSFC Basic Research Program (Project

No. 71671155), and the CityU Shenzhen Research Institute.

Appendix A

Table A.1  
The demographics of the 290 S&P 1500 firms used in this study.

<table><tr><td>Industry</td><td>Number of firms</td><td>Number of M&amp;As (2005–2017)</td></tr><tr><td>High technology</td><td>100</td><td>217</td></tr><tr><td>Healthcare</td><td>52</td><td>98</td></tr><tr><td>Financials</td><td>48</td><td>83</td></tr><tr><td>Media and entertainment</td><td>21</td><td>46</td></tr><tr><td>Consumer products and services</td><td>16</td><td>38</td></tr><tr><td>Telecommunications</td><td>15</td><td>30</td></tr><tr><td>Retail</td><td>13</td><td>19</td></tr><tr><td>Industrials</td><td>10</td><td>30</td></tr><tr><td>Consumer staples</td><td>5</td><td>3</td></tr><tr><td>Materials</td><td>4</td><td>5</td></tr><tr><td>Energy and power</td><td>4</td><td>12</td></tr><tr><td>Real estate</td><td>2</td><td>3</td></tr><tr><td>Total</td><td>290</td><td>584</td></tr></table>

## References

[1] D.C. Hambrick, P.A. Mason, Upper echelons: the organization as a reflection of its top managers, Acad. Manag. Rev. 9 (2) (1984) 193–206.

[2] R. Reuber, Management experience and management expertise, Decis. Support. Syst. 21 (2) (1997) 51–60.

[3] P. Herrmann, S. Nadkarni, Managing strategic change: the duality of CEO personality, Strateg, Manag, J. 35 (9) (2014) 1318–1342.

[4] S. Nadkarni, P. Herrmann, CEO personality, strategic flexibility, and firm performance: the case of the indian business process outsourcing industry, Acad. Manag. J. 53 (5) (2010) 1050–1073.

[5] S. Malhotra, T.H. Reus. P. Zhu. E.M. Roelofsen. The acquisitive nature of extraverted CEOs, Adm. Sci. Q. 63 (2) (2017) 370–408.

[6] U. Malmendier, G. Tate, Who makes acquisitions? CEO overconfidence and the market's reaction, J. Financ. Econ. 89 (1) (2008) 20–43

[7] N.J. Hiller, D.C. Hambrick, Conceptualizing executive hubris: the role of (hyper-) core self-evaluations in strategic decision-making, Strateg. Manag. J. 26 (4) (2005)

[8] R.Y.K. Lau, S.S.Y. Liao, K.F. Wong, D.K.W. Chiu, Web 2.0 environmental scanning and adaptive decision support for business mergers and acquisitions, MIS O. 36 (4) (2012).1239–1268

[9] K. Pal, O. Palmer, A decision-support system for business acquisitions, Decis. Support. Syst. 27 (4) (2000) 411–429.

[10] H. Tanriverdi, V.B. Uysal, Cross-business information technology integration and acquirer value creation in corporate mergers and acquisitions, Inf. Syst. Res. 22 (4) (2010) 703–720.

[11] T.-S. Hsieh, Z. Wang, S. Demirkan, Overconfidence and tax avoidance: the role of CEO and CFO interaction, J. Account. Public Policy 37 (3) (2018) 241–253.

[12] S. Sainani, How do CFOs matter? Evidence from M&A, in: FMA Annual Meeting 2018, 2018. URL, http://www.fmaconferences.org/SanDiego/Blinds/1500432.pdf

[13] W. Shi, Y. Zhang, R.E. Hoskisson, Examination of CEO–CFO social interaction through language style matching: outcomes for the CFO and the organization, Acad, Manag, J. 62 (2) (2019) 383–414

[14] C. Kirkland, The Role of a CFO in M&A. https://www.axial.net/forum/the-role-of -a-cfo-in-ma/. 2015 (Accessed 19 March 2020).

[15] E. Zehnder, The Evolving Role of the CFO: The CEO’s Key Business Partner. http://www.egonzehnder.com/leadership-insights/the-evolving-role-of-the-cfo the-ceos-kev-business-partner.html. 2008

[16] S. Yim, The acquisitiveness of vouth: CEO age and acquisition behavior, J. Financ Econ. 108 (1) (2013) 250–273.

[17] K. Yang, R. Lau, Detecting senior executives’ personalities for predicting corporate behaviors: an attention-based deep learning approach, in: The Fortieth International Conference on Information Systems, (Munich, Germany), 2019. https

[18] A. Nadolska, H.G. Barkema, Good learners: how top management teams affect the success and frequency of acquisitions. Strateg, Manag, J. 35 (10) (2014) 1483-1507.

[19] N. Aktas, E.D. Bodt, H. Bollaert, R. Roll, CEO narcissism and the takeover process: from private initiation to deal completion, J. Financ. Quant. Anal. 51 (1) (2016)

[20] L.A.H. Mathew, D.C. Hambrick, Explaining the premiums paid for large

[21] J. Huang, D.J. Kisgen, Gender and corporate finance: are male executives overconfident relative to female executives? J. Financ. Econ. 108 (3) (2013) 822-839.

[22] B. Zhou, S. Dutta, P. Zhu, CEO tenure and mergers and acquisitions, Finance Res. Lett. 34 (2019), https://doi.org/10.1016/j.frl.2019.08.025.

[23] Q. Huang, F. Jiang, E. Lie, K. Yang, The role of investment banker directors in M&a, J. Financ. Econ. 112 (2) (2014) 269–286.

[24] Y. Grinstein, P. Hribar, CEO compensation and incentives: evidence from M&A bonuses, J. Financ. Econ. 73 (1) (2004) 119–143.

[25] E. Sadler-Smith, V. Akstinaite, G. Robinson, T. Wray, Hubristic leadership: a review, Leadership 13 (5) (2016) 525–548.

[26] R.S. Peterson. D.B. Smith. P.V. Martorana. P.D. Owens. The impact of chief executive officer personality on top management team dynamics: one mechanism by which leadership affects organizational performance, J. Appl. Psychol. 88 (5) (2003) 795–808.

[27] R.R. McCrae, P.T. Costa, Validation of the five-factor model of personality acros instruments and observers, J. Pers. Soc. Psychol. 52 (1) (1987) 81–90.

[28] A.H.B. De Hoogh, D.N. Den Hartog, P.L. Koopman, Linking the Big Five-Factors of personality to charismatic and transactional leadership; perceived dynamic work environment as a moderator, J. Organ. Behav. 26 (7) (2005) 839–865.

[29] F. Iacobelli, A.J. Gill, S. Nowson, J. Oberlander, Large scale personality classification of bloggers, in: S. D’Mello, A. Graesser, B. Schuller, J.-C. Martin (Eds.), Affective Computing and Intelligent Interaction, Springer, Berlin, Heidelberg, 2011, pp. 568–577.

[30] M. Wilson, et al., Behav. Res. Methods Instr. Comput. 20 (1) (1988) 6–10.

[31] R.T. Proyer, K. Brauer, Exploring adult playfulness: examining the accuracy of personality judgments at zero-acquaintance and an LIWC analysis of textual information, J Res. Pers, 73 (2018) 12–20

[32] B.Y. Pratama, R. Sarno, Personality classification based on Twitter text using Naive Baves. KNN and SVM. in: 2015 International Conference on Data and Software Engineering (ICoDSE), 2015, pp. 170–174.

[33] N. Majumder, S. Poria, A. Gelbukh, E. Cambria, Deep learning-based document modeling for personality detection from text, IEEE Intell. Syst. 32 (2) (2017) 74–79.

[34] M. Bertrand, S. Mullainathan, Enjoying the quiet life? Corporate governance and

[35] T.A. Judge, J.E. Bono, R. Ilies, M.W. Gerhardt, Personality and leadership: a qualitative and quantitative review, J. Appl. Psychol. 87 (4) (2002).

[36] J.E. Bono, T.A. Judge. Personality and transformational and transactiona leadership: a meta-analysis, J. Appl, Psychol. 89 (5) (2004) 901–910.

[37] R. McCrae, P. Costa, The five factor theory of personality, in: J.S. Wiggins (Ed.), The Five Factor Model of Personality: Theoretical Perspective. The Guilford Press New York, NY. 1996, pp. 139–153.

[38] S. Finkelstein, D.C. Hambrick, Top-management-team tenure and organizationa outcomes: the moderating role of managerial discretion, Adm, Sci, O. 35 (3) (1990) 484-503.

[39] M.R. Barrick, M.K. Mount. The big five personality dimensions and job performance: a meta-analysis, Pers. Psychol. 44 (1) (1991) 1–26.

[40] R.R. McCrae, Openness to experience: expanding the boundaries of factor V. Eur. J

[41] P E Tetlock Accountability and complexity of thought J. Pers, Soc Psychol 45 (1) (1983) 74–83.

[42] P.E. Tetlock, Cognitive style and political belief systems in the British House of commons, J. Pers. Soc. Psychol. 46 (2) (1984) 365–375.

[43] S. Shane, N. Nicolaou, L. Cherkas, T. Spector, Genetics, the Big Five, and the tendency to be self-employed, J. Appl. Psychol. 95 (6) (2010) 1154–1162.

[44] B.E. Jeronimus. H. Riese, R. Sanderman. J. Ormel. Mutual reinforcement betweer neuroticism and life experiences: a five-wave, 16-year study to test reciprocal causation, J. Pers, Soc, Psychol, 107 (4) (2014) 751–764

## Q. Wang et al.

[45] R.R. McCrae, P.T. Costa, Personality trait structure as a human universal, Am. Psychol. 52 (5) (1997) 509–516.

[46] C.J. Norris, J.T. Larsen, J.T. Cacioppo, Neuroticism is associated with larger and more prolonged electrodermal responses to emotionally evocative pictures, Psychophysiology 44 (5) (2007) 823–826.

[47] M. Scheier, C. Carver, M. Bridges, Distinguishing optimism from neuroticism (and trait anxiety, self-mastery, and self-esteem): a reevaluation of the life orientation test, J. Pers, Soc. Psychol, 67 (6) (1994) 1063–1078.

[48] A.J. Bahns, C.S. Crandall, O. Gillath, K.J. Preacher, Similarity in relationships as niche construction: choice, stability, and influence within dyads in a free choice environment, J. Pers. Soc. Psychol. 112 (2) (2017) 329–355.

[49] L. Ross, D. Greene, P. House, The “false consensus effect”: an egocentric bias in social perception and attribution processes, J. Exp. Soc. Psychol. 13 (3) (1977) 279–301.

[50] B. Schneider, The people make the place, Pers. Psychol. 40 (3) (1987) 437–453.

[51] P. Adamopoulos, A. Ghose, V. Todri, The impact of user personality traits on word of mouth: text-mining social media platforms, Inf. Syst. Res. 29 (3) (2018) 612–640.

[52] R. Singh, S.Y. Ho, Attitudes and attraction: a new test of the attraction, repulsion and similarity-dissimilarity asymmetry hypotheses, Br. J. Soc. Psychol. 39 (2) (2000) 197–211.

[53] R.M. Bowen, S.J. Jollineau, S.C. Lyon, S. Malhotra, P. Zhu, CEO-CFO Personality Differences and Audit Fees: The Price of Conflict?, Unpublished results, 2019, https://doi.org/10.2139/ssrn.3473963.

[54] D. Matsumoto, M. Pronk, E. Roelofsen, What makes conference calls useful? The information content of managers’ presentations and analysts’ discussion sessions, Account. Rev. 86 (4) (2011) 1383–1414.

[55] M.T. Billett, T.-H.D. King, D.C. Mauer, Bondholder wealth effects in mergers and acquisitions: new evidence from the 1980s and 1990s, J. Financ. 59 (1) (2004) 107–135.

[56] F. Celli, B. Lepri, J.-I. Biel, D. Gatica-Perez, G. Riccardi, Workshop on Computational Personality Recognition (Shared Task), in the Workshop on Computational Personality Recognition, Orlando, Florida, USA. https://www.aaai. org/ocs/index.php/ICWSM/ICWSM13/paper/do wnload/6190/6306, 2014.

[57] F.C. Mairesse, M.A. Walker, M.R. Mehl, R.K. Moore, Using linguistic cues for the automatic recognition of personality in conversation and text, J. Artif. Intel. Res. (30) (2007) 457–500.

[58] P.T. Costa Jr., R.R. McCrae, The five-factor model and the NEO inventories, in: J. N. Butcher (Ed.), Oxford Handbook of Personality Assessment, Oxford University Press, New York, NY, US, 2009, pp. 299–322.

[59] J. Benesty, J. Chen, Y. Huang, I. Cohen, Pearson correlation coefficient, in: Processing, Springer. Berlin. Heidelberg, 2009, pp. 1–4.

[60] S. Glen, Correlation Coefficient: Simple Definition, Formula, Easy Steps. https ://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-for mula/, 2020 (accessed on 4 April 2020).

[61] T.K. Koo, M.Y. Li, A guideline of selecting and reporting Intraclass correlation coefficients for reliability research, J. Chiropr. Med. 15 (2) (2016) 155–163.

[62] S.B. Moeller, F.P. Schlingemann, R.M. Stulz, Firm size and the gains from acquisitions, J. Financ. Econ. 73 (2) (2004) 201–228.

[63] W.B. Carper, Corporate acquisitions and shareholder wealth: a review and exploratory analysis, J. Manag. 16 (4) (1990) 807–823.

[64] R.L. Smith, J.-H. Kim, The combined effects of free cash flow and financial slack on bidder and target stock returns, J. Bus. 67 (2) (1994) 281–310.

[65] B.R. Karney, T.N. Bradbury, Neuroticism, marital interaction, and the trajectory of marital satisfaction, J. Pers. Soc. Psychol. 72 (5) (1997) 1075–1092.

[66] M. Yang, G. Adomavicius, G. Burtch, Y. Ren, Mind the gap: accounting for measurement error and misclassification in variables generated via data mining, Inf. Syst. Res. 29 (1) (2018) 4–24.

[67] J.R. Cook, L.A. Stefanski, Simulation-extrapolation estimation in parametric measurement error models, J. Am. Stat. Assoc. 89 (428) (1994) 1314–1328.

[68] G. Farnadi, S. Zoghbi, M.-F. Moens, M.D. Cock, Recognising personality traits using Facebook status updates, in: The Seventh International AAAI Conference on Weblogs and Social Media, 2013. https://www.aaai.org/ocs/index.php/ICWSM/ ICWSM13/paper/viewFile/6245/6309.

[69] J.D. Westphal, E.J. Zajac, Who shall govern? CEO/board power, demographic similarity, and new director selection, Admin. Sci. Q. 40 (1) (1995) 60–83.

[70] R. Blundell, S. Bond, Initial conditions and moment restrictions in dynamic pane

[71] I.R.P. Cuypers, Y. Cuypers, X. Martin, When the target may know better: effects of experience and information asymmetries on value from mergers and acquisitions, Strateg. Manag. J. 38 (3) (2017) 609–625.

Qiping Wang (qipinwang2-c@my.cityu.edu.hk) received the Ph.D. degree in the Department of Information Systems from City University of Hong Kong, and the M.Phil. degree in Business Administration from Shanghai Jiao Tong University, China. Her research interests include Social Media Analytics and AI for Fintech. Her works has been published in IEEE Consumer Electronics Magazine and the International Conference on Information Systems(ICIS)

Raymond Y.K. Lau (raylau@cityu.edu.hk) is an Associate Professor in the Department of Information Systems at City University of Hong Kong. He is the author of over two hundred refereed international journals and conference papers. His research work has been pub lished in renowned journals such as IEEE Transactions on Knowledge and Data Engi neering, IEEE Intelligent Systems, IEEE Internet Computing, INFORMS POM, etc. His research interests include Big Data Analytics, Fintech, and AI for Business. He is a senior member of the IEEE and the ACM, respectively.

Kai Yang (kayang6-c@my.cityu.edu.hk) received the Ph.D. degree in the Department of Information Systems from City University of Hong Kong, and the Bachelor and the Master degrees in the Department of Software Engineering from the South China University of Technology, China. His research interests include Social Media Analytics, Data Mining, Artificial Intelligence, and Fintech. His works have been published in Neurocomputing, International Conference on Computational Linguistics (COLING) and the International Conference on Information Systems (ICIS).
