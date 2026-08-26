---
otero_id: 20040
otero_key: "EUJB8GAR"
title: "Exploring the effect of digital CSR communication on firm performance: A deep learning approach"
authors: "Shuihua Han; Zhenyuan Liu; Ziyue Deng; Shivam Gupta; Patrick Mikalef"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.114047"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring the effect of digital CSR communication on firm performance: A deep learning approach

![](/api/attachments/EUJB8GAR/fulltext/images/2b02ae8ab0d93d8a1b084a3c320ce1b8164295437e5837c7463f628ca9e367d6.jpg)

Shuihua Han <sup>a</sup>, Zhenyuan Liu <sup>a</sup>, Ziyue Deng <sup>a</sup>, Shivam Gupta <sup>b</sup>, Patrick Mikalef <sup>c,d,\*</sup>

<sup>a</sup> Department of Management Science, School of Management, Xiamen University, Xiamen, China

<sup>b</sup> Department of Information Systems, Supply Chain Management & Decision Support, NEOMA Business School, Reims, France

<sup>c</sup> Department of Computer Science, Faculty of Information Technology and Electrical Engineering, Norwegian University of Science and Technology, Norway

<sup>d</sup> Department of Technology Management, SINTEF Digital, Trondheim, Norway

## A R T I C L E I N F O

Keywords: Deep learning Natural language processing Digital CSR communication Stakeholder engagement Firm performance Agenda-setting theory

## A B S T R A C T

This study proposes a novel research framework to examine the effect of digital CSR communications on financial performance while incorporating deep learning techniques to identify firms’ CSR communications on social media. Particularly, this research aims to quantify firms’ efforts in digital CSR communications by employing cutting-edge deep learning-based natural language processing (NLP) models to detect CSR-related tweets on social media. Utilizing a unique dataset of 65 Chinese public companies in the manufacturing sector between 2015 and 2019, we detected 64,769 long-form tweets posted on WeChat to acquire both digital CSR commu nications and stakeholder engagement data. Combining financial and secondary data of sample firms, this research reveals the positive but time-lagged influence of digital CSR communications on firms’ financial per formance, primarily through the lens of agenda-setting theory. We also find that stakeholder engagement plays an essential bridging role in the relationship above, while CSR ratings surprisingly hamper such a positive effect.

## 1. Introduction

The prevalence of social media has changed how firms communicate corporate social responsibility (CSR) with their stakeholders and the public [1–3], granting both challenges and opportunities for firms to launch communication management. Conventionally, companies tend to disclose CSR initiatives, practices, and achievements in annual report forms [4]. However, stakeholders (i.e., customers, shareholders, in vestors, and suppliers) and the public often express their skepticism regarding the authenticity of contents in one-way communication when there are scarce timely inquiries and interactions. Meanwhile, social media platforms allocate a crucial channel for business organizations to proactively disseminate their CSR agendas to the broader audience [1] and obtain feedback and suggestions through stakeholder engagement online, such as likes, reposts, and comments. Okazaki, et al. [5] identi fied such an interactive communication process as digital CSR commu nication, wherein firms can dynamically implement and evaluate their CSR communication strategies to gain trust from and then align interests among stakeholders and the public.

So what kinds of business value does digital CSR communication bring to firms? Pioneering scholars vigorously explored the business values of digital CSR communication in specific terms of customer loy alty, corporate reputation, product purchase intention, and product sales [6–9]. However, only a few studies shed light on digital CSR communications’ effect on financial performance. When generating CSR-related tweets on social media, firms would like to collaborate with their primary stakeholders and the public to set and implement their CSR conceptualizations, initiatives, and practices, as the interactive nature of social media enables firms to yield broad attention and abundant resources [10,11]. On the other hand, the business valuegenerating process of digital CSR communications takes a while, given that diverse social media stakeholder groups may have varying attitudes towards the same CSR activity [12].

Nevertheless, researchers may fail to grasp the interactive process of digital CSR communications from longitudinal studies, primarily as the detecting and processing of unstructured textual data is both timeconsuming and labor-intensive. In particular, most of the extant studies in CSR communication adopted manual coding strategy or lexicon-based methods to detect relevant tweets on social media [5,13,14]. Even though these studies usually sample short-form texts from Twitter or Weibo, it is still time- and labor-consuming to identify CSR-related tweets considering the multiple dimensions of CSR itself [15], and adds much more burdens in data processing procedure when tapping into long-form texts from platforms like Facebook and WeChat. In this vein, the existing research in digital CSR communication desires handy tools for dealing with large volumes of unstructured textual data on social media.

The blossoming of Artificial Intelligence (AI) poses promisingly prescriptive and cognitive solutions to addressing the research gap in examining the business values of digital CSR communication. AI tech nology, especially deep learning-based natural language processing (NLP) techniques, achieves superior performance in textual cognition’s accuracy and efficiency [16–18]. Prior studies have harnessed such AI to pursue various business research objectives in the context of social media [19–24]. However, to the best of our knowledge, there exists no literature leveraging deep learning approaches to detect digital CSR communications and investigating its effects on firms’ financial perfor mance. Therefore, we aim to propose a novel research framework integrating deep learning techniques for exploring the relationship be tween digital CSR communications and firm performance.

Drawing upon agenda-setting theory, we hypothesize that digital CSR communications contribute to firms’ financial performance due to the agenda-setting effect. Meanwhile, we also aim to uncover the role of stakeholder engagement on social media in the relationship between digital CSR communications and financial performance. To accomplish the research objectives above, we collected social media (i.e., WeChat) and secondary financial data of 65 of the Top 500 Chinese A-share listed manufacturing companies from 2015 to 2019. Then, we utilized tweets data with long text forms to train the cutting-edge deep learning models (i.e., CNN, BiLSTM, BiGRU) to detect CSR communications. After acquiring the deep learning model with the best detection performance, we applied it to categorizing sample firms’ digital CSR communications from 64,769 long-form tweets and calculating relevant stakeholder en gagements. We further incorporated these quantified data into the econometric analysis models. Finally, we run the econometric model with fixed effects as well as mediating and moderating analysis models to address research questions, gaining insights regarding the business value of firms’ digital CSR communications.

This study responds to the current call that profoundly interprets the influence of business strategies on firm performance through the utili zation of AI-based prescriptive and cognitive analytics [25]. In digital CSR communication, we developed an innovative and practical frame work for unleashing the power of deep learning-based NLP techniques in detecting firms’ CSR-related tweets on social media. Then, we found that digital CSR communications positively influence firms’ financial per formance, but such an effect is time-lagged and can be surprisingly dampened by firms’ CSR performance. Meanwhile, stakeholder engagement on social media plays an essential but partial mediating role in the relationship between digital CSR communications and financial performance. These findings methodologically and practically allow managers to make informed decisions on their design, delivery, and management of digital CSR communications for boosting both stake holder engagement and business performance, which have been high lighted by Korschun and Du [2], Schniederjans, et al. [26] and Benitez, et al. [9].

## 2. Literature review and hypothesis development

## 2.1. Digital CSR communication and its business value-generating process

Crane and Glozer [3] defined corporate social responsibility (CSR) communication as firm-initiated disclosure of CSR efforts through different channels. Further, Schoeneborn, et al. [27] provided a forma tive perspective to regard CSR-related communications and practices as talk and walk, respectively. This view dissects the walking-to-talk, talking-to-walk, and t(w)alking relationships between communications and practices, wherein CSR communications are no longer a firm’s cheap talk but constitute and influence CSR practices. In this sense, CSR communications occupy the driving seat in the value-generating process of firms’ CSR strategies in a long ride. Indeed, while conjoining business operations and stakeholder interactions with social and environmental issues, Podnar [28] contended that the business value of CSR commu nication hinges on stakeholder expectations and CSR strategies so that it can provide authentic and transparent information on a company’s economic, social, and environmental concerns through interacting with stakeholders [29]. In this view, CSR communication facilitates business organizations to broadcast their social initiatives, encourage stake holders to share opinions and obtain information about the activities of other participants in the CSR field [9].

With the upswing of social media, its powerful and interactive communication advantage forges a critical platform for firms to imple ment CSR communications, the process of which is defined as digital CSR communication in this study [5]. Du and Vieira Jr. [30] argued that the intensive interactivity of social media boosts the effectiveness of digital CSR communications, given that social media in-timely contrives firms’ CSR vision, endeavors, and practices. Meanwhile, firms can also yield CSR-related feedback and participation from broad social media users including stakeholders and the public, who would easily spread firms’ communication messages through their own social networks. Following this seminal research, more recent studies have revealed the paths where digital CSR communication generates various outcomes.

A wealth of empirical studies have indicated that stakeholder engagement is an indispensable bridge to achieving the business value of CSR communications, especially in the era of social media [15,31]. Representing word-of-mouth, trust and organizational attractiveness, and stakeholder engagement in digital CSR communications brings firms abundant resources and social capital that contribute to firm performance [11]. Yang and Basile [10] went further by identifying stakeholder engagement as the logical starting point for improving corporate value through digital CSR communications. Moreover, prior studies also saw the destructive effects of stakeholder engagement in digital CSR communication when firms failed to manage such engage ment well. For instance, Eberle, et al. [32] found the adverse effect of users’ negative comments in social media much stronger than the pos itive ones. Saxton, et al. [14] further manifested that stakeholder engagement, particularly in the tone of praising, questioning, or criti cizing CSR, determines the business value of CSR communication. They also found that a company’s response to stakeholders on social media positively correlates with stakeholders’ connective power while nega tively correlates with the company’s. In sum, stakeholder engagement works as an essential part in the dynamic value-generating process of digital CSR communication. Nevertheless, only a few of existing studies examined the mediating role of stakeholder engagement while exploring the effects of CSR communication on firm performance.

In the meantime, flourishing research demonstrated multiple busi ness outcomes of digital CSR communication. Recent studies have shown that digital CSR communication can boost brand loyalty and equity, company reputation, product purchase intention, and organi zational attractiveness [11,13,32–40]. For instance, Eberle, et al. [32] suggested that CSR communications can significantly enhance consumer recognition and improve firm performance. Focusing on asset manage ment companies, Sciarelli, et al. [39] revealed that the sufficient disclosure of corporate social performance (CSP) via the internet and social media is positively associated with economic performance. Underpinned by survey results, Gupta, et al. [34] expounded that banks CSR communication on social media can positively influence consumer loyalty and purchase intention through brand admiration. Fig. 1 illus trates discussions from prior studies regarding the business valuegenerating process of digital CSR communication.

However, only a few of studies shed light on the effect of digital CSR communications on financial performance, most of which preferred financial indicators measuring market reactions (i.e., Tobin’s Q and stock prices) rather than firms’ returns. In Fig. 1, we highlighted such research gaps by adding question marks on the business benefitsfinancial performance linkage arrow and financial indicators part. This perspective is crucial, given that digital CSR communications represent an essential channel for companies to utilize social media to implement stakeholder management and align their interests with the expectations of stakeholders and the public [26]. One possible explanation is that the effect of digital CSR communications on financial performance could be gradual rather than abrupt, especially considering the tendency of twalking. Hence, we can only capture such an effect more concisely through a longitudinal investigation. In the following subsection, we will leverage agenda-setting theory to delve into the relationship be tween digital CSR communications and financial performance in the long run, and then propose relevant research hypotheses.

![](/api/attachments/EUJB8GAR/fulltext/images/4366e7c569fb3d6d565e497ad74c4a70e1216f2fa4237da3e1e7501b7fd0dbb8.jpg)  
Fig. 1. The business value-generating process of digital CSR communications.

## 2.2. Hypotheses developments

Drawing on agenda-setting theory in mass communication, this research explores the effects of digital CSR communication on firms financial performance, wherein stakeholder engagement functions as an essential bridging role. Agenda-setting theory posits that media, firm coverage, and public attention can enlighten the importance of social issues and objectives [38], which consists of two main layers [41,42]. The first layer of agenda-setting theory is media agenda, which refers to media and corporate coverage of an issue or event that can affect the public perception of its importance. The second layer is the public agenda which delineates the effect of public attention and evaluation on such issues or events.

Agenda-setting theory offers theoretical, analytical tools for studies investigating the influence of CSR communications on firm perfor mance. As the first layer of agenda-setting theory, firm-initiated CSRrelated communications deliver firms’ attention and efforts to imple ment their social responsibility, representing stakeholder orientation while taking stakeholders’ rather than only shareholders’ interests into their decision-making processes. For instance, Takeshita [43] analyzed companies who have set public agendas on websites that can manifest their unswerving efforts in practicing CSR and then discovered the positive role of driving community attention in enhancing companies environmental performance. Based on the evidence of global companies, Lee [44] demonstrated that the higher media covers the importance of CSR, the better corporate reputation can yield. Therefore, the more digital CSR communications a firm launches, the broader stakeholder orientation it will hold.

In the era of social media, it is indispensable to test the agendasetting effect in decentralized discourse and networked online plat forms, considering social media plays the same role of messagedelivering as counterparts in traditional media [45]. By using social media to communicate CSR-related initiatives, conceptualizations, and practices, firms can set their agendas without being monitored or modified by traditional media. Additionally, social media is more resourceful regarding communication speed and interactivity. With such endeavors, firms can engage with diverse stakeholders to magnify their CSR efforts and obtain online feedback, support, and trust in an inter active manner. Stakeholders thereby will trust and reward companies for being honest and legitimate, which will be a process to boost busi ness performance ultimately. In this sense, primary stakeholder groups are prone to support the business operations of such stakeholderoriented firms, as more talented employees could be retained, cus tomers improve their purchase intentions and suppliers work much more closely and stably [46]. All this evidence can enhance firms competitive advantages, and bring them financial improvements. However, it is noticeable that such agenda-setting effects could usually be time-lagged [41], as improving financial performance through digital CSR communication could be in the gradual rather than abrupt manner. Therefore, we propose the first hypothesis regarding the effects of digital CSR communications on firms’ financial performance as follows:

## H1. A firm’s digital CSR communications have significantly positive but time-lagged effects on its financial performance.

In the process of digital CSR communications, stakeholders can engage with core firms in online interactions, including views, likes, retweets, and comments [47]. Stakeholders express their satisfaction to companies’ social media tweets through simple “likes”, which could help companies establish initial relationships with and then cultivate more profound recognition and trust from their customers, suppliers, employees, and others. Besides, retweets could also create contagious diffusion, enabling companies to connect with more entities in stake holders’ social networks and pursue higher and more diverse networks [14]. Further, comments represent a much deeper involvement in CSR communications and even co-create firms’ CSR initiatives and projects by providing extensive suggestions. In this sense, Besiou, et al. [31] claimed that stakeholder engagement is the key to achieving agendabuilding and -melding, forming the second layer of agenda-setting ef fect via the public agenda. In light of such a proposition, Castillo, et al. [48] revealed a positive relationship between CSR communications and stakeholder engagement.

Moreover, Korschun and Du [2] indicate that stakeholder engage ment functions as the intermediate outcome between CSR communica tions and business values, confirming such engagement could help firms acquire valuable resources for performance enhancement. Although firm-initiated digital CSR communications can deliver firms’ concern and practice of sharing environmental, social, and economic messages on social media, it is only through such engagement that firms’ initia tives can meet stakeholders’ and the public’s expectations and forge sustainable competitiveness [2,5]. Following this argument, a wealth of previous studies have shown that stakeholder satisfaction enhances corporate financial performance, wherein customer satisfaction leads to more purchases while investor satisfaction leads to more capital re sources. Also, higher stakeholder engagement can promote word-ofmouth communication and invigorate firms’ financial performance [49].

Investigating the comprehensive process of digital CSR communi cation in China, Kim [50] identified the mediating role of stakeholder engagement on social media in the relationship between CSR commu nications and corporate reputation. However, there is still limited research empirically investigating the role of stakeholder engagement in mediating the effects of digital CSR communications on firms’ financial performance. Therefore, we propose the second hypothesis in this study to explore the role of stakeholder engagement in the digital CSR com munication–Performance relationship as follows:

H2. Stakeholder engagement plays a significantly positive role in mediating the effect of digital CSR communications on financial performance.

In the wake of more companies disclosing and implementing CSR initiatives and practices, many third-party agencies rate firms’ perfor mance in CSR across various sectors. Such CSR ratings reflect listed companies’ environmental, social, and economic achievements and are often of greater interest to stakeholders as these ratings assess firms’ CSR performance from a third-party perspective. For example, Miller, et al. [51] found that companies that win positive CSR ratings also achieve higher financial performance, which brings companies with external CSR assessments of higher credibility and transparency, less skepticism, and enhanced consumer trust in the organizations. Moreover, for those firms in highly controversial industries with low CSR ratings particu larly, it is crucial to clarify the genuine relationship between digital CSR communications and firm performance. This questioning and criticism of the stakeholder community on social media can potentially exert a fatal influence on firms regarding reputation risks and market shares, which will ultimately be reflected in the firm’s financial performance [52,53].

Thus, external CSR ratings can increase the credibility of a com pany’s CSR practices as well as its CSR communications. Based on the evidence above, we argue that third-party CSR ratings positively mod erate the relationship between digital CSR communications and finan cial performance. Specifically, digital CSR communications of companies with higher external CSR ratings would have much greater financial performance. Therefore, we propose the following hypothesis:

H3. CSR ratings positively moderate the effects of digital CSR com munications on financial performance.

Fig. 2 illustrates the conceptual framework wherein we leverage agenda-setting theory to explore the mechanism of the value-generating process of digital CSR communications.

![](/api/attachments/EUJB8GAR/fulltext/images/29ba1b4ae5d34354265a0ea2fe3d1a8531bd8cb37f74622e867b584f14fc47e3.jpg)  
Fig. 2. Conceptual framework.

## 3. Research methods

## 3.1. Approaches to detecting digital CSR communications

To explore the effect of digital CSR communications on firm per formance longitudinally, the first and foremost step is to precisely and efficiently detect CSR-related tweets on social media extensively. Extant studies in this field utilize manual detection and/or lexicon-based methods to detect and quantify firms’ CSR communication tweets on social media. Table 1 summarizes more recent relevant studies, wherein sample firm details, social media platforms, tweets numbers, observa tion period, and the specific detection strategy are presented.

However, these existing methods are either labor-intensive to iden tify targets over time or yield low detection accuracy. For instance, managers and researchers adopting the manual detection method have to invest massive resources and time to acquire accurate results, espe cially when confronted with both multiple attributes of CSR and the overwhelming volume of data on social media. Meanwhile, CSR com munications often integrate with firms’ marketing, innovation, and operations practices rather than being an isolated behavior [56], which poses a formidable challenge to training detection employees with impaired cognition.

The prevalence of lexicon-based methods improves efficiency in detecting CSR communications while at the cost of losing accuracy. These methods usually utilize keyword matching and/or calculate tex tual similarity extent to identify CSR communications, the accuracy of which depends on the scale, quality, and coverage of dictionaries and corpora [22]. When processing longitudinal textual data, these ap proaches may suffer from low accuracy and efficiency due to the changes in textual features, considering the diverse and flexible ex pressions of CSR-related topics on social media. At the same time, lexicon-based methods can not further provide valuable and meaningful insights regards the dynamics of CSR communications, especially when organizations plan to evaluate and design effective digital CSR com munications through listening to, capturing, and understanding ongoing public discussions regards social and environmental concerns.

On the other hand, the thriving artificial intelligence (AI) technologies in natural language processing (NLP) meet researchers’ and managers urgent needs in effectively and efficiently identifying CSR-related tweets on social media. In particular, supervised NLP-based deep learning techniques could conduct textual detection and analysis based on contextual semantics and automatically detect whether a tweet belongs to CSR communications [57], which addresses the limitations of lexicon based methods. At the same time, with only a relatively resource input in the annotation and labeling process to train the algorithm can re searchers and managers acquire an automated detection and surveillance system of CSR communications. However, to the best of our knowledge, there exits no literature employing this cutting-edge technique to detect and identify CSR communications. More recently, Du, et al. [58] articu lated that AI-based analytics has great potential to open avenues for quantitative research and business practices in CSR fields. Therefore, this study tries to answer their call by leveraging deep learning approaches to detect, analyze and quantify firms’ digital CSR communications and then investigate their effects from a longitudinal perspective.

## 3.2. Research framework

Fig. 3 depicts the research framework proposed in this study. Spe cifically, drawing upon the methods in identifying CSR-related tweets on social media from prior studies, we develop an analytical framework integrating deep learning-based NLP models to detect and process tex tual information and then empirically examine the effectiveness and efficiency of these models in predicting firms’ digital CSR communica tions. In particular, we trained three potential deep learning models (i. e., Convolutional Neural Networks (CNN), Bidirectional Long Short-Term Memory (BiLSTM), and Bidirectional Gate Recurrent Unit (BiGRU)) for conducting the textual detection tasks. Then we applied a matrix of accuracy indicators to measure these models’ detection per formance. Ultimately, we also incorporate econometric analysis into the framework to further explore the effects of digital CSR communications on firms’ financial performance, wherein CSR textual information quantified through the most accurate deep learning model as well as supplemented with other secondary data at the firm level are working as input variables.

Table 1  
Extant studies investigating the effects of digital CSR communications.

<table><tr><td>Authors</td><td>Samples</td><td>Social media Platform</td><td>Tweets Number</td><td>Observation Period</td><td>Detection Strategy</td></tr><tr><td>Saxton, et al. [14]</td><td>42 out of Fortune 200 firms</td><td>Twitter</td><td>34,097</td><td>2013</td><td>Manual Detection</td></tr><tr><td>Vogler and Eisenegger [13]</td><td>68 Swiss companies</td><td>Facebook</td><td>33,772</td><td>From January 2011 to December 2017</td><td>Keywords Matching</td></tr><tr><td>Jiang and Park [54]</td><td>71 out of Top 100 Best Corporate Citizens companies</td><td>Twitter</td><td>22,951</td><td>From January to December 2019</td><td>Keywords Matching</td></tr><tr><td>Jakob, et al. [36]</td><td>58 out of 500 Fortune most successful companies of 2017</td><td>Facebook</td><td>67,189</td><td>From 2004 to June 2018</td><td>Keywords Matching</td></tr><tr><td>Yang and Basile [10]</td><td>82 out of Top 100 Global Brands</td><td>Facebook</td><td>19,508</td><td>From January to December 2017</td><td>Social Media Analytics (CSR-related tags)</td></tr><tr><td>Mickelsson, et al. [55]</td><td>3 high-profile fashion brands</td><td>Twitter</td><td>57,414</td><td>From 2018 to 2020</td><td>LDA Topic Modeling</td></tr></table>

![](/api/attachments/EUJB8GAR/fulltext/images/b17c12220884b5966fb0b6bc30f2fbeb1ebe62ecc348008d3f9388bc5752a050.jpg)  
Fig. 3. Research framework.

It is noticeable that our proposed research framework can be applied and adapted in future studies investigating broader business values of digital CSR communications with the overwhelming amount of social media tweets. Apart from this, business research and practices in scru tinizing companies’ social media behaviors almost share a similar analytical framework. Therefore, our research framework could also advise studies and practices in expansive fields, such as innovation, marketing, and operations management in social media.

## 3.3. Data collection and processing

In this study, our sample firms contain 65 of the Top 500 Chinese A share listed companies<sup>1</sup> in the manufacturing sector from 2015 to 2019, all of which have been implementing digital CSR communications on the WeChat Subscription Platform through their official accounts. First, Chinese A-share listed manufacturing enterprises need to incorporate CSR communications into their social media strategies, as these com panies are more likely to inflict pollution, excessive consumption of resources, and other irresponsible behavior [30]. Second, we chose the WeChat Subscription Platform (WSP) as the communication channel on social media, as WSP has advantages of providing both detailed tweets with long-form texts and a much more massive user base for companies to engage with [59,60]. Therefore, we conducted a thorough manual identification and found that 65 of the Top 500 Chinese A-share listed companies opened official accounts on WSP. Finally, we set the obser vation period from 2015, given that WSP was launched in November 2014. We also closed the observation period before 2019 to eschew the complex impact of COVID-19 on the financial performance of manufacturing enterprises.

In November 2021, we obtained unstructured textual data and sec ondary data of sample firms through multiple sources. Specifically, we employed a combination of crawler approaches to acquire the tweets of the sample firms posted on their WSP official accounts and obtained a total of 64,769 long-form tweets. We plan to apply deep learning-based natural language processing (NLP) models to identify the tweets that can be categorized into digital CSR communications and then yield stake holder engagement data from relevant CSR tweets. Moreover, we utilized the stock codes of sample firms to match and obtain secondary data via China Stock Market & Accounting Research Database (CSMAR), including financial performance indicators and control variables. Finally, we obtained the CSR ratings of sample firms in the observation period from the Hexun CSR rating database.

## 3.4. Leveraging deep learning techniques to detect digital CSR communications

## 3.4.1. Digital CSR communications annotation and identification strategy

Statistical and machine learning-based NLP models have been widely used in business analytics [17,61–65]. For example, Liu, et al. [66] manually marked 5000 pieces of random sample data for training NLP models and then utilized the trained model to predict 500,000 pieces of data for investigating the effects of social media marketing on customer engagement. Vogler and Eisenegger [13] constructed CSR-related keyword searching and matching solutions to identify CSR tweets to explore CSR communications’ effects on a firm’s reputation. Beyond the CSR context, Fan, et al. [22] used deep learning techniques to identify and extract the side effects of medicine in social media. However, to the best of our knowledge, no existing research applies deep learning-based NLP techniques to detect digital CSR communications. One possible explanation is due to the various dimensions of CSR, which may incur excessive burdens and challenges for identifying CSR semantics in long form tweets.

Carroll [67] built a pyramid to delineate the economic, legal, ethical, and philanthropic dimensions of CSR, and more recent studies divide CSR into three main dimensions, including environmental, social, and economic levels, which is deemed as the “triple bottom line” of enter prises’ sustainable operations [68]. Table 2 enumerates the key themes related to the above three dimensions of CSR communications, which stem from the disclosed annual CSR of eight sample enterprises and the CSR information evaluation system of SynTao Green Finance in Chinese contexts.<sup>2</sup>

After establishing the annotation criteria above, we randomly selected 20% out of the total sample tweets for manual annotation. Specifically, we assigned values of 1 and 0 to categorize all tweets into relevant and irrelevant tweets of CSR communications, respectively. In June 2023, three postgraduates who majored in Accounting and Finance were hired as research assistants to complete the annotation task of 12,646 tweets, wherein 10,331 tweets related to CSR communications and 2315 irrelevant ones were identified. Then, we used these manually detected tweets as the training and test set to train the deep learning models and compare their detection accuracy. Particularly, the data selected by stratified sampling and manual detection was divided into training set (7586 tweets), verification set (2530 tweets), and test set (2530 tweets) as per the ratio of 6:2:2.

Traditionally, most text tokenization in Chinese contexts uses the Jieba tokenization package to pre-process the words or phrases tokeni zations. However, the pre-trained linguistic analysis model launched by Google is more widely used to process the tokenization of various texts [69], and the results are much better than Jieba tokenization method. In this sense, we selected BERT Tokenizer for text pre-processing, which adopts BERT text embedding as input to train the text tokenization model and split the text into a sequence of strings. Finally, regarding the binary classification method, we apply Accuracy indicators to measure the overall prediction accuracy of detection models.

## 3.4.2. Deep learning-based detection models

We utilized a series of deep learning-based NLP models to conduct textual detection tasks, as these models can automatically complete the construction of attribute values in the detection process. We first adopted the original TextCNN model proposed by Kim [70], which first maps the texts into vectors, then captures the local semantics within the text through many filters [25]. After that, the TextCNN model can capture the most important textual features and then put them into the full connection layers, wherein the probability distribution of the labels can be obtained. Kashgari<sup>3</sup> optimized the original TextCNN by expanding it into Convolutional Neural Network (CNN) model that can better process long-form text types.

Stemming from Recurrent Neural Networks (RNN), Long Short Term Memory (LSTM) is an improved RNN that ensures the retention of important text feature values by adding Forget Gate and Input Gate. Two independent LSTM constructs the structural model of BiLSTM neural network, wherein sequence features can be captured by extracting two LSTM neural networks with positive and reverse sequences. One essential characteristic of BiLSTM is that the features obtained at t include both past and future information. Previous studies confirmed that the efficiency of applying BiLSTM model in conducting textual detection tasks had been notably improved [22,24]. Therefore, we also integrate BiLSTM model into the textual detection tasks.

Gate Recurrent Unit (GRU) model is another RNN frequently used for textual detection. To address the gradient descent issue in long-term memory and back propagation [71], GRU is equipped with higher training efficiency than LSTM. Specifically, GRU model consists of Up date Gate and Reset Gate. The former controls the extent to which the state information at the previous time is brought into the current state, while the latter controls the extent to which the state information at the previous time is overlooked. This study selected the BiGRU model to carry out text detection, wherein text information can be encoded in two orientations after inputting.

## 3.5. Variable measurements

Digital CSR communications: This is a numeric variable DCSRC that we utilized the natural logarithm of identified and detected digital CSR communication tweets. Specifically, we manually labeled and applied the most accurate deep learning-based NLP model to detect sample firms’ CSR-related tweets on their WeChat official accounts, with the former accounting for 20% and the latter for 80% of the whole 64,769 long-form tweets. After that, we aggregated detected CSR-relevant tweets into the yearly data to construct DCSRC.

Stakeholder engagement: We construct the numeric variable of SEave by taking the natural logarithm of the average number of reads, likes, retweets, and comments embedded in the sample companies digital CSR communication tweets as the proxy for stakeholder engagement. Previous literature on stakeholder or customer engage ment suggested that different social media interactions represent different engagement levels. For example, reads represent the con sumption of corporate digital communication, likes to stand for support, and retweets and comments refer to the contribution and co-creation in firm communications. In light of this situation, we followed the approach of Dearden, et al. [72] and Liu, et al. [66] to average the four types mentioned above of stakeholder engagement. Specifically, we averaged all four engagement data of sample firms’ each CSR-related tweets and then aggregated them into the yearly data to build SEave.

CSR ratings: This study operationalizes CSRra by Hexun annual CSR ratings of Chinese listed companies. According to the annual reports of listed companies, Hexun rates the annual CSR performance of listed companies through five systematic evaluation indicators, $\mathrm { i . e . , }$ , share holder responsibility, employee responsibility, the rights and liabilities of clients and customers, environmental responsibility, and social re sponsibility. Existing studies taking the Chinese context into account also referred to such CSR ratings to evaluate companies’ ability to perform CSR [73]. Further, we followed previous studies to percentile CSR ratings as the proxy CSRra. Specifically, we ranked the obtained

Table 2  
Labeling criteria for identifying CSR communication tweets.

<table><tr><td>CSR dimensions</td><td>Classifications</td><td>Relevant themes in WeChat tweet contents</td></tr><tr><td rowspan="3">Environmental</td><td>Environmental management</td><td>Environmental management system, Staff environmental consciousness, Energy and water conservation policy, Green procurement policy</td></tr><tr><td>Environmental disclosure</td><td>Energy consumption, Energy efficiency, Water consumption, Greenhouse gas emissions, Low carbon, Clean technology, Green building</td></tr><tr><td>environmental events</td><td>Water pollution, Air pollution, Solid waste pollution</td></tr><tr><td rowspan="8">Social</td><td>Employee management</td><td>Labor policy, Anti-forced labor, Anti-discrimination, Female employees, Employee training, Health and safety</td></tr><tr><td>Supply chain management</td><td>Supply chain responsibility management, Supervision system, Compliance and efficiency, Sunshine procurement, Joint innovation</td></tr><tr><td>Customer management</td><td>Customer satisfaction management, Customer information confidentiality, Dispute handling, and Technological innovation to improve customer satisfaction</td></tr><tr><td>Community management</td><td>Community communication, Health and care, Rural revitalization</td></tr><tr><td>Product management</td><td>Fair trade products, Safety and quality</td></tr><tr><td>Charity and donation</td><td>Corporate foundation, Donation, Philanthropy efforts</td></tr><tr><td>National Strategy</td><td>Support the real economy, Poverty alleviation, Contribute to national strategies</td></tr><tr><td>Negative social events</td><td>Negative events of employees, supply chain, customers, and products</td></tr><tr><td rowspan="3">Economic</td><td>Corporate governance</td><td>Information disclosure, Board independence, Executive compensation, Board diversity, Party building, Investor communication (profit, internal control, risk management)</td></tr><tr><td>Negative corporate governance events</td><td>Business ethics, Negative corporate governance events</td></tr><tr><td>Corporate governance</td><td>Information disclosure, Board independence, Executive compensation, Board diversity, Party building, Investor communication (profit, internal control, risk management)</td></tr></table>

CSR ratings, then accessed the sample companies’ percentile ranking in the observation years.

Financial performance: In this study, we selected yearly Returns on Equity (ROE) to measure sample companies’ financial performance. Previous studies on financial performance usually select TOBIN’S Q as the proxy for financial performance. However, the most empirical set tings of these studies were set in developed economies with more mature market structures. In one of the most emerging economic markets in the world, Chinese listed firms have the characteristics of high turnover of stocks and volatile prices due to the lower capital market effectiveness, which may undermine the role of TOBIN’S Q as an indicator to measure companies’ actual financial performance. We thereby utilized yearly ROE to measure corporate financial performance, which can provide more objective and genuine information regards actual firm performance.

Control variables: This study employed firm age, firm size, growth rate, solvency ratios, and financial leverage ratios as control variables. All these variables have been incorporated in previous studies as factors affecting firms’ financial performance, specifically through resource availability, growth, and financial sustainability.

Table 3 specifies variable names, measurements and data sources in this study.

## 3.6. Econometric analysis

To testify the research hypotheses proposed in Section 2.2, we build a set of panel data econometric regression models as follows:

$$
\begin{array}{r l} \text { Roe } _ {i, t} & = \beta_ {0} + \beta_ {1} \text { DCSRC } _ {i, t - 1} + \beta_ {2} \text { CSRra } _ {i, t} + \beta_ {3} \text { Age } _ {i, t} + \beta_ {4} \text { Ta } _ {i, t} + \beta_ {5} \text { Growth } _ {i, t} \\ & \quad + \beta_ {6} \text { Rla } _ {i, t} + \beta_ {7} \text { Lev } _ {i, t} + \mu_ {i} + \lambda_ {t} + \varepsilon_ {i, t} \end{array}\tag{1}
$$

$$
\begin{array}{r l} S E a v e _ {i, t} & = \alpha_ {0} + \alpha_ {1} \mathrm{DCSRC} _ {i, t - 1} + \alpha_ {2} \mathrm{CSRra} _ {i, t} + \alpha_ {3} \mathrm{Age} _ {i, t} + \alpha_ {4} \mathrm{Ta} _ {i, t} + \alpha_ {5} \text { Growth } _ {i, t} \\ & \quad + \alpha_ {6} \mathrm{Rla} _ {i, t} + \alpha_ {7} \mathrm{Lev} _ {i, t} + \mu_ {i} + \lambda_ {t} + \varepsilon_ {i, t} \end{array}\tag{2}
$$

$$
\begin{array}{r l} R o e _ {i, t} & = \gamma_ {0} + \gamma_ {1} D C S R C _ {i, t - 1} + \gamma_ {2} S E a v e _ {i, t - 1} + \gamma_ {3} \mathrm{CSRra} _ {i, t} + \gamma_ {4} \mathrm{Age} _ {i, t} + \gamma_ {5} \mathrm{Ta} _ {i, t} \\ & + \gamma_ {6} \text { Growth } _ {i, t} + \gamma_ {7} \mathrm{Rla} _ {i, t} + \gamma_ {8} \text { Lev } _ {i, t} + \mu_ {i} + \lambda_ {t} + \varepsilon_ {i, t} \end{array}\tag{3}
$$

Both individual and time-fixed effects are controlled in the models above. Function 1 aims to test the effect of digital CSR communications on financial performance, wherein we lag the digital CSR communica tions variable by one period according to the possible time-lagged agenda-setting effect. Therefore, we expect the coefficient $\beta _ { 1 }$ to be significantly positive. As to Function $^ { 2 , }$ we focus on the contribution of digital CSR communications to stakeholder engagement, and we, therefore, expect the coefficient $\alpha _ { 1 }$ to be significantly positive as well. In Function 3, we regress both digital CSR communications and stake holder engagement on financial performance to examine the possible mediating effect of stakeholder engagement on the relationship between digital CSR communications and financial performance. In this sense, we expect both coefficients of $\gamma _ { 1 }$ and $\gamma _ { 2 }$ to be significantly positive at the same time. Meanwhile, stakeholder engagement can be testified as a partial mediator when $\gamma _ { 1 }$ is smaller than $\beta _ { 1 } ;$ it will also suggest that stakeholder engagement is a full mediator when the coefficient $\gamma _ { 1 }$ be comes insignificant.

Table 3  
Variable definitions and measurements.

<table><tr><td>Variables</td><td>Measurements</td><td>Data sources</td></tr><tr><td colspan="3">Dependent variable</td></tr><tr><td>ROE</td><td>Firms&#x27; yearly returns on equity.</td><td>CSMAR</td></tr><tr><td colspan="3">Independent variable</td></tr><tr><td>DCSRC</td><td>The logarithmic forms of firms&#x27; digital CSR communication tweets detected by NLP-based deep learning models, aggregated at yearly level.</td><td>WeChat Subscription Platforms</td></tr><tr><td>SEave</td><td>The logarithmic forms of average stakeholder engagement in firms&#x27; each digital CSR communications, aggregated at yearly level.</td><td>WeChat Subscription Platforms</td></tr><tr><td>CSRra</td><td>The percentile position of sample firms&#x27; CSR ratings from the third-party agency (i.e., Hexun).</td><td>Hexun CSR ratings</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Age</td><td>The logarithmic forms of a firm&#x27;s ages.</td><td>CSMAR</td></tr><tr><td>Ta</td><td>The logarithmic forms of total assets of sample firms.</td><td>CSMAR</td></tr><tr><td>Growth</td><td>A firm&#x27;s revenue growth in year t is divided by its revenue growth in year t-1.</td><td>CSMAR</td></tr><tr><td>Rla</td><td>A firm&#x27;s total liabilities are divided by its total assets.</td><td>CSMAR</td></tr><tr><td>Lev</td><td>A firm&#x27;s sum up of net profits, income tax expenses, and financial expenses divided by the total of net profits and income tax expenses.</td><td>CSMAR</td></tr></table>

To test the moderating effect of CSR ratings, we construct the following regression equation based on panel data:

$$
\begin{array}{r l} R o e _ {i, t} & = \theta_ {0} + \theta_ {1} \mathrm{DCSRC} _ {i, t - 1} + \theta_ {2} \mathrm{CSRra} _ {i, t - 1} + \theta_ {3} \mathrm{CSRra} _ {i, t - 1} * \mathrm{DCSRC} _ {i, t - 1} \\ & \quad + \theta_ {4} \mathrm{Age} _ {i, t} + \theta_ {5} \mathrm{Ta} _ {i, t} + \theta_ {6} \text { Growth } _ {i, t} + \theta_ {7} \mathrm{Rla} _ {i, t} + \theta_ {8} \text { Lev } _ {i, t} + \mu_ {i} + \lambda_ {i} + \varepsilon_ {i, t} \end{array}\tag{4}
$$

In Function 4, we incorporate the interaction item between digital CSR communications and CSR ratings and regress it on corporate financial performance. The positive coefficient of interaction item can support Hypothesis 3 that CSR ratings enhance the influence of digital CSR communications on corporate financial performance. We run all the regression models above on Stata 16 with xtreg function.

## 4. Analysis and results

## 4.1. The detection results of digital CSR communications

Three deep learning-based NLP models, i.e., CNN, BiLSTM, and BiGRU models, were introduced to complete the digital CSR communi cations detection task. Meanwhile, to validate these deep learning models, we also follow extant methods identified from prior relevant studies (i.e., manual detection, keywords matching, and LDA topic modeling) to compare detection accuracy.<sup>4</sup> Further, we also conducted the segmented detection tasks according to multiple CSR dimensions (i. e., environmental, social, and economic dimensions), which could help us to understand the detection performance among different methods explicitly.

Table 4 shows the results of comparative performance analyses among manual detection, lexicon-based methods, and deep learning models. We took manual detection as the baseline results, given that most relevant studies adopted this strategy to detect digital CSR com munications. According to the results in Table $^ { 4 , }$ deep learning models outperformed both manual detection and lexicon-based methods across the training set, test set, and each CSR dimension except the social one. One possible explanation could be the abundant content of social-related CSR communications. Further, CNN achieved the most accurate detec tion performance compared to BiLSTM and BiGRU.

The primary motivation driving us to utilize deep learning is the time-consuming and labor-intensive process of manually detecting CSR communication tweets. Considering 64,769 collected long-text form tweets in this study, it may take several weeks and even months to identify relevant CSR ones. With the merit of deep learning techniques, we captured the improvements in detection accuracy in the model training process, presented in Table 5. Setting the manual detection accuracy as baseline results, we can yield almost equal accuracy when only detecting 1500 tweets for training the deep learning models.

Meanwhile, to verify the reliability of predicting digital CSR com munications through deep learning applications, we followed Vogler and Eisenegger [13] to randomly extract 1000 pieces of manually labeled data, and then re-predicted these data via CNN model. The result of such a validation process obtained 0.8965 in Precision and 0.9015 in Recall. Hence, we followed the previous studies to adopt a deep learning based NLP model with the best accuracy performance $( \mathrm { i . e . , }$ , the CNN model) to conduct the textual detection tasks of the remaining 80% of texts $( \mathrm { i . e . , }$ 48,751 tweets). By doing ${ \bf { s o } } ,$ we can acquire digital CSR communications and stakeholder engagement data.

## 4.2. Econometric analysis results

Table 6 presents the descriptive statistics of the variables and their correlations before being put into the regression models.

Table 7 reports the empirical results of the main regression results based on the panel data econometric analysis model. According to the empirical results of Model 1 in the second column, we find that the oneperiod lagged digital CSR communications exerted significant positive effects over ROE (coefficient $= 0 . 1 4 4 , \mathrm { p } < 0 . 0 5 )$ , supporting H1 pro posed in this study. Model 2 shows that digital CSR communication can positively influence stakeholder engagement $( { \mathrm { c o e f f i c i e n t } } = 0 . 0 7 6 , p <$ 0.01).

The results of Model 3 manifest that stakeholder engagement with a one-period lag significantly contributes to firms’ financial performance $( \mathrm { c o e f f i c i e n t } = 0 . 0 5 2 , \mathrm { p } < 0 . 0 1 )$ . It verifies that stakeholders’ perceptions and engagement can substantially benefit the firm. Meanwhile, digital CSR communications with a one-period lag can significantly and posi tively boost financial performance (coefficient $= 0 . 0 1 0 , p < 0 . 1 )$ . On the other hand, this coefficient is smaller than the counterpart of stake holder engagement, supporting H2 proposed in this study that stake holder engagement is an essential and partial mediator for achieving the positive effects of digital CSR communications on firms’ financial performance.

Model 4 aims to verify the moderating effect of CSR ratings on the CSR communications and financial performance relationship. Our empirical analysis results indicate the notable positive effect of lagged digital CSR on financial performance (coefficient $= 0 . 0 1 5 , \mathrm { p } < 0 . 0 5 )$ , whereas the coefficient of DCSRC \*CSRra was significantly negative, suggesting that CSR ratings hamper the positive effect of digital CSR communications on financial performance. In this sense, there was an inhibitory moderating effect of CSR ratings in the contribution of digital CSR communication to financial performance; therefore, H4 cannot be supported.

## 4.3. Robustness check

We also perform a robustness check on the dependent, moderating, and mediating variables. First, we replaced ROE with Returns on Assets (ROA) to measure firms’ financial performance. Second, we replaced the percentage ranking of CSR rating with the ABCD levels rating provided by Hexun. Table 8 outlines the results of the robustness check. Of all the results shown in Table $^ { 8 , }$ no significant differences exist between ROA and ROE as the proxies for firms’ financial performance. Therefore, findings regarding the effects of digital CSR on financial performance as well as the mediating role of stakeholder engagement are still robust. Secondly, the empirical results remained consistent with the previous research findings when we changed the measurement of CSR ratings, wherein CSR ratings inhibited the contribution of digital CSR to finan cial performance. In order to address the endogeneity issue inherent in our analytical process, we adopted Propensity Score Matching (PSM) and used the instrument variable of the average industrial stakeholder engagement to replace the sampled firms. The regression results are consistent with our main model, ensuring the positive but time-lagged effects of digital CSR communication on financial performance (coeffi cient $= 0 . 0 0 6 ^ { * } , p < 0 . 1 )$ ) and the potential mediator of stakeholder engagement in the digital CSR communication–Performance relation ship $( \mathrm { c o e f f i c i e n t } = 0 . 0 1 2 ^ { * } , \mathrm { p } < 0 . 1 )$ ).

Table 4  
The results of comparative detection performance analyses.

<table><tr><td>Method</td><td>Training Set</td><td colspan="3">Test Set</td><td colspan="3">Test Set on CSR Dimensions</td><td colspan="3">Comparative Improvement on Test Set over Baseline Method</td></tr><tr><td></td><td></td><td colspan="3"></td><td>Environmental</td><td>Economic</td><td>Social</td><td></td><td></td><td></td></tr><tr><td></td><td>Accuracy</td><td>Accuracy</td><td>Accuracy (Macro)</td><td>Accuracy (Weighted)</td><td>Accuracy</td><td>Accuracy</td><td>Accuracy</td><td>Accuracy</td><td>Accuracy (Macro)</td><td>Accuracy (Weighted)</td></tr><tr><td>Baseline</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Manual Detection</td><td>0.880</td><td>0.870</td><td>0.850</td><td>0.900</td><td>0.730</td><td>0.830</td><td>0.950</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Lexicon-Based</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Keywords Matching</td><td>0.480</td><td>0.510</td><td>0.490</td><td>0.530</td><td>0.330</td><td>0.500</td><td>0.630</td><td>-0.400</td><td>-0.36</td><td>-0.370</td></tr><tr><td>LDA Topic Model</td><td>0.653</td><td>0.557</td><td>0.683</td><td>0.680</td><td>0.653</td><td>0.887</td><td>0.770</td><td>-0.227</td><td>-0.167</td><td>-0.220</td></tr><tr><td>Deep Learning</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BiGRU Model</td><td>0.904</td><td>0.900</td><td>0.937</td><td>0.907</td><td>0.835</td><td>0.844</td><td>0.853</td><td>0.084</td><td>0.087</td><td>0.007</td></tr><tr><td>BiLSTM Model</td><td>0.970</td><td>0.925</td><td>0.925</td><td>0.926</td><td>0.794</td><td>0.900</td><td>0.862</td><td>0.09</td><td>0.075</td><td>0.026</td></tr><tr><td>CNN Model</td><td>0.982</td><td>0.931</td><td>0.941</td><td>0.932</td><td>0.863</td><td>0.944</td><td>0.866</td><td>0.102</td><td>0.091</td><td>0.032</td></tr></table>

Table 5  
The improvements of detection accuracy in training deep learning models.

<table><tr><td rowspan="2"></td><td colspan="5">Percentiles of Manually Detected CSR Posts</td></tr><tr><td>1% (104 tweets)</td><td>5% (517 tweets)</td><td>10% (1034 tweets)</td><td>15% (1550 tweets)</td><td>20% (2100 tweets)</td></tr><tr><td colspan="6">Baseline:</td></tr><tr><td>Manual Detection Accuracy</td><td>0.880</td><td>0.880</td><td>0.880</td><td>0.880</td><td>0.880</td></tr><tr><td colspan="6">Deep Learning Models</td></tr><tr><td>CNN Detection Accuracy</td><td>0.294</td><td>0.778</td><td>0.883</td><td>0.938</td><td>0.982</td></tr><tr><td>BiLSTM Detection Accuracy</td><td>0.213</td><td>0.653</td><td>0.808</td><td>0.901</td><td>0.970</td></tr><tr><td>BiGRU Detection Accuracy</td><td>0.217</td><td>0.557</td><td>0.779</td><td>0.883</td><td>0.904</td></tr></table>

We also followed Hong and Paylou [74] to conduct Bootstrap and Sobel tests to testify the mediation analysis of stakeholder engagement in the effects of digital CSR communications on financial performance. The results are shown in Table 9. The results of Sobel test indicate that the mediating effect was notably positive and was not zero. Meanwhile. the upper and lower limits of Bootstrap (within a 95% confidence in terval) are 0.0018 and 0.0102, respectively, neither of which contains zero. In this sense, the mediation analysis results demonstrate that stakeholder engagement partially mediated the positive effect of digital CSR communications on financial performance.

## 5. Discussion

## 5.1. Theoretical implications

First, drawing upon agenda-setting theory, this study examined the effect of digital CSR communication on firms’ financial performance from the communication process perspective. Specifically, we found that firm-initiated digital CSR communications have positive but time-lagged effects on firms’ financial performance, and stakeholder engagement partially mediates such effects. Compared with traditional mass media, Feezell [75] and Oh, et al. [76] asserted that social media may also generate agenda-setting effects, through which stakeholders and the public could capture issue salience and interactively provide feedback. In digital CSR communication, firms can leverage social media platforms to not only broadcast but also yield stakeholders’ expectations and opinions regarding CSR initiatives and practices [1,2,27,56]. Such an interactive communication process could co-create CSR agendas, gain ing attention, social capital, and resources to improve firm performance [77,78]. Although Vogler and Eisenegger [13] found that CSR agendas set by news media instead of social media contribute to corporate reputation, we revealed that the positive agenda-setting effects could be time-lagged through the longitudinal investigation [41,43,45]. These findings answer whether social media is an effective channel for setting CSR agendas. Also, we enlighten future studies on how to employ agenda-setting theory to explore multiple business value-generating processes of digital CSR communications.

Second, through the second layer of agenda-setting theory, we also testified the mediating role of stakeholder engagement in the relation ship between digital CSR communication and financial performance. Besiou, et al. [31] asserted that the merit of the agenda-setting effect not only resides in how companies shape public perceptions but, more importantly, will help companies attract proper stakeholders to achieve the essential objectives. Okazaki, et al. [78] accentuated the mediating role of stakeholder engagement in understanding CSR economic con sequences. However, Kim [11] did not identify such a significant effect of stakeholder engagement that mediates the process of CSR commu nication, wherein corporate reputation works as the outcome. Following his perspective to unpack the value-generating process of CSR commu nications, we utilized the field data sourced from WeChat to recognize the essential role of stakeholder engagement in the DCSRC–Performance link. Noticeably, Our results demonstrate that stakeholder engagement functions as a partial instead of a full mediator. One possible explanation could be the mismatch caused by stakeholder heterogeneity in digital CSR communication [55,79]. In this sense, future studies could delve into the essential role of stakeholder engagement in the valuegenerating process of digital CSR communications, especially taking heterogeneity into consideration.

Table 6  
Variable descriptive statistics and correlations matrix.

<table><tr><td>Variables</td><td>Means</td><td>Standard deviations</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1. Roe</td><td>0.101</td><td>0.131</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. SEave</td><td>11.597</td><td>3.965</td><td>0.115**</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. DCSRC</td><td>3.847</td><td>1.959</td><td>0.073</td><td>0.424***</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. CSRra</td><td>0.5</td><td>0.288</td><td>0.466***</td><td>0.057</td><td>0.028</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Age</td><td>2.636</td><td>0.543</td><td>-0.191***</td><td>0.091*</td><td>0.102*</td><td>-0.183***</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>6. Ta</td><td>23.67</td><td>1.152</td><td>-0.017</td><td>0.269***</td><td>0.261***</td><td>-0.041</td><td>0.308***</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>7. Growth</td><td>0.535</td><td>3.575</td><td>0.454***</td><td>0.086</td><td>0.059</td><td>0.111**</td><td>-0.057</td><td>0.000</td><td>1.000</td><td></td><td></td></tr><tr><td>8. Rla</td><td>0.494</td><td>0.18</td><td>-0.371***</td><td>0.026</td><td>0.064</td><td>-0.381***</td><td>0.438***</td><td>0.456***</td><td>-0.054</td><td>1.000</td><td></td></tr><tr><td>9. Lev</td><td>0.085</td><td>0.16</td><td>-0.117**</td><td>0.027</td><td>-0.017</td><td>-0.097*</td><td>0.162***</td><td>0.471***</td><td>0.042</td><td>0.281***</td><td>1.000</td></tr></table>

Note: \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

Table 7  
The results of main regression models

<table><tr><td rowspan="3"></td><td>Model 1</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td>H1</td><td>H1</td><td>H2</td><td>H2</td><td>H3</td></tr><tr><td>ROE</td><td>ROE</td><td>SEave</td><td>ROE</td><td>ROE</td></tr><tr><td> $\text{DCSRC}_t$ </td><td>0.006(1.00)</td><td></td><td></td><td></td><td></td></tr><tr><td> $\text{DCSRC}_{t-1}$ </td><td></td><td>0.144**(2.55)</td><td>0.076***(2.98)</td><td>0.010*(1.82)</td><td>0.015**(2.76)</td></tr><tr><td> $\text{SEave}_{t-1}$ </td><td></td><td></td><td></td><td>0.052**(2.24)</td><td></td></tr><tr><td> $\text{CSRra}_t$ </td><td>0.129***(3.97)</td><td>0.093**(2.05)</td><td>0.041(0.38)</td><td>0.091**(1.98)</td><td>0.145***(5.31)</td></tr><tr><td> $\text{DCSRC}_{t-1}*\text{CSRra}_t$ </td><td></td><td></td><td></td><td></td><td>-0.016**(-2.62)</td></tr><tr><td> $\text{Age}_t$ </td><td>-0.073(-1.65)</td><td>0.015(0.15)</td><td>-0.53(-0.13)</td><td>0.177(0.18)</td><td>0.112***(3.53)</td></tr><tr><td> $\text{Ta}_t$ </td><td>0.030(0.81)</td><td>0.175(1.42)</td><td>0.011(0.07)</td><td>0.174(1.40)</td><td>0.226**(2.03)</td></tr><tr><td> $\text{Growth}_t$ </td><td>0.014***(3.87)</td><td>0.128***(3.47)</td><td>-0.005(-0.99)</td><td>0.131***(3.53)</td><td>0.014***(3.92)</td></tr><tr><td> $\text{Rla}_t$ </td><td>-0.406**(-3.49)</td><td>-0.482**(-2.17)</td><td>0.167(0.55)</td><td>-0.491**(-2.20)</td><td>-0.568***(-2.79)</td></tr><tr><td> $\text{Lev}_t$ </td><td>0.025**(0.43)</td><td>0.057(1.20)</td><td>-0.566**(-2.42)</td><td>0.872*(1.67)</td><td>0.041(0.83)</td></tr><tr><td>Constant</td><td>-0.325(-0.39)</td><td>-3.927(-1.34)</td><td>0.450(0.13)</td><td>-3.951(-1.32)</td><td>-6.830(-2.86)</td></tr><tr><td>Firm fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>325</td><td>325</td><td>325</td><td>325</td><td>325</td></tr><tr><td> $R^2(\text{Within})$ </td><td>0.4556</td><td>0.3499</td><td>0.3491</td><td>0.3598</td><td>0.4606</td></tr></table>

Note: \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01. t statistics in parentheses.

Table 8  
The results of robustness check.

<table><tr><td rowspan="2"></td><td>Model 3</td><td>Model 4</td><td>Model 3</td><td>Model 4</td></tr><tr><td>ROA</td><td>ROA</td><td>ROE</td><td>ROE</td></tr><tr><td> $\text{DCSRC}_{t-1}$ </td><td>0.004*(1.77)</td><td></td><td>0.011**(1.93)</td><td></td></tr><tr><td> $\text{SEave}_{t-1}$ </td><td>0.016*(1.93)</td><td></td><td>0.048*(1.84)</td><td></td></tr><tr><td> $\text{CSRra\_ABCD}_{t-1}$ </td><td>0.041***(3.04)</td><td>0.056***(4.82)</td><td>0.092**(2.27)</td><td>0.150***(5.21)</td></tr><tr><td> $\text{DCSRC}_{t-1}*\text{CSRra\_ABCD}_{t-1}$ </td><td></td><td>-0.005**(-2.54)</td><td></td><td>-0.002***(-2.61)</td></tr><tr><td>Growth</td><td>0.004***(4.58)</td><td>0.004***(4.35)</td><td>0.113**(3.49)</td><td>0.014***(4.46)</td></tr><tr><td>Ta</td><td>0.059**(2.16)</td><td>0.017(1.38)</td><td>0.173(1.37)</td><td>0.036(0.88)</td></tr><tr><td>Rla</td><td>-0.244***(-3.58)</td><td>-0.234***(-4.88)</td><td>-0.485(-2.41)</td><td>-0.438***(-3.81)</td></tr><tr><td>Age</td><td>0.031**(2.09)</td><td>-0.011(-0.89)</td><td></td><td></td></tr><tr><td>Lev</td><td>0.026(1.53)</td><td>0.005(0.2)</td><td></td><td></td></tr><tr><td>Constant</td><td>-1.683**(-2.63)</td><td>-0.251(-0.88)</td><td>-3.733(-1.39)</td><td>-0.561(-0.77)</td></tr><tr><td>Firm fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>325</td><td>325</td><td>325</td><td>325</td></tr><tr><td> $R^2$ (Within)</td><td>0.4685</td><td>0.5185</td><td>0.3602</td><td>0.4588</td></tr></table>

Note: \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01. t statistics in parentheses.

Table 9  
The results of the mediation analysis.

<table><tr><td></td><td>Coefficients</td><td>Standard Error</td><td>Z-value</td><td>P-value</td><td>Upper limits</td><td>Lower limits</td></tr><tr><td>Sobel test</td><td>0.009</td><td>0.005</td><td>1.712</td><td>0.086</td><td></td><td></td></tr><tr><td>Bootstrap</td><td>0.024</td><td>0.0084</td><td>2.83</td><td>0.005</td><td>0.0018</td><td>0.0102</td></tr></table>

Third, this study identified that CSR ratings work as a significant boundary condition but negatively moderating the digital CSR com munication–Performance relationship. Previous studies contended that CSR ratings from third-party agencies could represent firms’ CSR per formance and strengthen the positive effect of CSR communication in a moderating manner [10]. However, our study revealed that CSR ratings hindered the positive effects of digital CSR communications on firms financial performance. In other words, the contribution of digital CSR communication to financial performance was more substantial fo companies with lower CSR ratings than those with higher ones. This finding indicates that firms with low CSR ratings from a third party can rely more on digital CSR communications when heading for superior firm performance, resonating with Du and Vieira Jr. [30] accentuating the necessity of digital CSR communications for organizations in controversial industries. This finding also aligns with Castillo, et al. [48] that firms with low CSR ratings can increase their organizational attractiveness by enhancing their digital CSR communications. In this vein, we enriched the empirical evidence from China to demonstrate that firms with low CSR ratings can enhance their financial performance by vigorously engaging in digital CSR communications.

Fourth, this research proposed cutting-edge deep learning-based NLP techniques to identify digital CSR communications, the business value of which was further probed through the combination with econometric analysis. In the wake of the prosperity and popularity of digital CSR communications, a myriad of researchers have devoted attention to exploring its business value via various methods. However, most of the extant literature on the recognition of digital CSR communications still adopts either manual detection [49] or lexicon-based detection solutions [13], both of which are either time-consuming or achieve low accuracy. In this sense, we applied the deep learning-based NLP approach to detect and identify digital CSR communication tweets with a large volume of textual data on social media, facilitating future research to improve their analytical efficiency in digital CSR communications. Moreover, after quantifying unstructured textual data through deep learning techniques, we embraced econometric analysis to shed light on the effects of digital CSR communications on firm performance. Without such a combination of deep learning and econometric analysis techniques, we could not testify the above findings from a longitudinal investigation. We also proposed an explicit research framework encouraging scholars to utilize AI-based analytics to improve interpretative capabilities for optimizing firms’ decision-making process and business performance [25], espe cially in interpreting multiple topic dimensions, comment emotions, and substantial outcomes in digital CSR communications.

## 5.2. Managerial implications

First, our results suggest that firms’ efforts in digital CSR commu nications could be paid off via improved financial performance, but such a value-generating process has a significantly time-lagged characteristic. Based on these results, managers and practitioners should be confident but patient about launching digital CSR communications. For example, managers should improve firms’ social media presence, especially when conducting CSR communications. Moreover, we also identified that stakeholder engagement is essential for achieving the business value of digital CSR communications. In this sense, firms can appoint managers dedicated to collecting and analyzing stakeholder engagement behav iors. For instance, managers can listen to initiatives and calls from the market side and then apply valuable information to their new product development processes to meet social and environmental expectations. Also, when confronted with stakeholders and public questioning, man agers can utilize digital CSR communications to reduce CSR information asymmetry by answering their internal philanthropic initiatives and practices. Hence, strategically implementing digital CSR communica tions can interactively set firms’ CSR agenda and align their interest with stakeholders and the public.

Second, the boundary condition (i.e., CSR ratings) on the positive relationship between digital CSR communications and financial per formance could also bring firms practical inspiration. Specifically, dig ital CSR communications can equip firms with an effective management instrument to realize business values. Especially for firms with lower CSR performance, implementing CSR communications on social media can redeem these firms’ reputations and re-gaining trust from stake holders and the public. After receiving unexpected CSR ratings from the third party, managers need to improve communication frequencies as well as content richness to engage with more stakeholders when grasping the opportunity of digital CSR communications. Third, man agers can also apply the deep learning-based NLP models in identifying the attributes and contents of their own and competitors’ CSR commu nications and further correctly evaluate the business returns of their CSR communications. In doing so, the methodology applied in this study provides these companies with handy tools to monitor the effectiveness of their communication and improve the marginal returns.

## 6. Conclusion and future scope of research

This study applied a deep learning approach to detect 65 listed manufacturing companies’ potential digital CSR communications on one of China’s most prevailing social media platforms (i.e., the WeChat Subscription Platform). Drawing upon agenda-setting theory, we investigated the business value of digital CSR communications and un covered the following findings: 1) digital CSR communications exert a significantly positive but time-lagged influence on financial perfor mance; 2) stakeholder engagement plays an essential but partial medi ating role in the relationship between digital CSR communications and financial performance; 3) however, CSR ratings from third-party agency hinder such an effect. Regarding the research methodology in this study, we adopted the combination of a deep learning approach and econo metric analysis to enhance the prescriptive and cognitive analytics models in the field of CSR research, responding to the call for demon strating the notable merit of AI analytics in quantitative CSR research in a more explicit manner [58].

Akin to previous studies, this study inevitably has a few limitation that need to be addressed by future studies. Firstly, our sample firms are all from Chinese listed companies in A-share markets, which are mature and well-managed. Hence, future research can delve into small and medium enterprise samples and further scrutinize CSR communications business value [80]. Second, we merely focused on one social media platform in China to solicit and detect potential digital CSR communi cation tweets. However, more recent studies collected data from multiple social media platforms [81], which helps to improve the generality of research findings. Future research could enrich the collection chan nels of textual data to validate our findings. Third, there also exist limitations in the variable constructions and data processing. For instance, we only quantified the frequency of detected CSR-related tweets instead of testing the effect of tweet length. Also, we used the average method to construct stakeholder engagement instead of dis secting and exploring its various dimensions. We also noticed that im ages and videos are important forms of communication during our manual labeling of digital CSR communications. Future research can also extend the applications of this state-of-the-art approach by leveraging deep learning techniques to process image and video data in the field of CSR communications.

## CRediT authorship contribution statement

Shuihua Han: Conceptualization, Methodology, Writing – original draft. Zhenyuan Liu: Data curation, Writing – original draft. Ziyue Deng: Writing – original draft, Investigation. Shivam Gupta: Supervi sion, Writing – review & editing. Patrick Mikalef: Writing – review & editing.

## Declaration of Competing Interest

The authors declare the following financial interests/personal re lationships which may be considered as potential competing interests:

Shuihua Han reports financial support was provided by National Natural Science Foundation of China.

## Data availability

The data that has been used is confidential.

## Acknowledgement

This study is partially supported by National Natural Science Foun dation of China under Grant No.71671152 for Prof. Shuihua Han (first author).

## References

[1] S.C. Chu, H.T. Chen, C. Gan, Consumers’ engagement with corporate social responsibility (CSR) communication in social media: evidence from China and the United States, J. Bus, Res, 110 (2020) 260–271.

[2] D. Korschun, S. Du, How virtual corporate social responsibility dialogs generate value: a framework and propositions, J. Bus, Res, 66 (9) (2013) 1494–1504.

[3] A. Crane, S. Glozer, Researching corporate social responsibility communication: themes, opportunities and challenges, J. Manag, Stud. 53 (7) (2016) 1223–1252

[4] S. Ren, M. Huang, D. Liu, J. Yan, Understanding the impact of mandatory CSR disclosure on green innovation: evidence from Chinese listed firms, Br. J. Manag. 00 (2022) 1–19

[5] S. Okazaki, K. Plangger, D. West, H.D. Men´endez, Exploring digital corporate social responsibility communications on twitter, J. Bus. Res. 117 (2020) 675–682.

[6] K. Hutter, J. Hautz, S. Dennhardt, J. Füller, The impact of user interactions in social media on brand awareness and purchase intention: the case of MINI on Facebook. J. Prod. Brand. Manag. 22 (5) (2013) 342–351.

[7] C. Diikmans, P. Kerkhof, C.J. Beukeboom, A stage to engage: social media use and

[8] X. Luo, S. Du. Exploring the relationship between corporate social responsibility and firm innovation, Mark, Lett, 26 (4) (2015) 703–714.

[9] J. Benitez, L. Ruiz, A. Castillo, J. Llorens, How corporate social responsibility activities influence employer reputation: the role of social media capability, Decis. Support. Syst. 129 (2020) 1–11. Art. no. 113223.

[10] J. Yang, K. Basile, Communicating corporate social responsibility: external stakeholder involvement, productivity and firm performance, J. Bus. Ethics 178 (2) (2022) 501–517

[11] S. Kim, The process model of corporate social responsibility (CSR) communication: CSR communication and its relationship with Consumers’ CSR knowledge, trust, and corporate reputation perception, J. Bus. Ethics 154 (4) (2019) 1143–1159.

[12] H. Wang, M. Jia, Z. Zhang, Good deeds done in silence: stakeholder management and quiet giving by Chinese firms, Organ. Sci. 32 (3) (2021) 649–674.

[13] D. Vogler, M. Eisenegger, CSR communication, corporate reputation, and the role of the news media as an agenda-setter in the digital age, Bus. Soc. 60 (8) (2021) 1957–1986.

[14] G.D. Saxton, L. Gomez, Z. Ngoh, Y.P. Lin, S. Dietrich, Do CSR messages resonate? Examining public reactions to Firms’ CSR efforts on social media, J. Bus. Ethics 155 (2) (2019) 359–377.

[15] P. Gomez-Carrasco, ´ E. Guillamon-Saorín, ´ B. García Osma, Stakeholders versus firm communication in social media: the case of twitter and corporate social

[16] M. Mustak, J. Salminen, L. Pl´e, J. Wirtz, Artificial intelligence in marketing: topic modeling, scientometric analysis, and research agenda, J. Bus. Res. 124 (2021) 389-404.

[17] E.W.T. Ngai, Y. Wu, Machine learning in marketing: a literature review, conceptual framework, and research agenda, J. Bus. Res. 145 (2022) 35–48

[18] J.J. Zhu, Y.C. Chang, C.H. Ku, S.Y. Li, C.J. Chen, Online critical review classification in response strategy and service provider rating: algorithms from heuristic processing, sentiment analysis to deep learning, J. Bus. Res. 129 (2021) 860–877.

[19] R. Kumar, S. Mukherjee, T.M. Choi, L. Dhamotharan, Mining voices from selfexpressed messages on social-media: diagnostics of mental distress during COVID 19, Decis. Support. Syst. 162 (2022) 1–13. Art. no. 113792.

[20] K. Li, C. Zhou, X.R. Luo, J. Benitez, Q. Liao, Impact of information timeliness and richness on public engagement on social media during COVID-19 pandemic: an empirical investigation based on NLP and machine learning, Decis. Support. Syst. 162 (2022) 1–13, Art, no. 113752

[21] S. Vamosi, T. Reutterer, M. Platzer, A deep recurrent neural network approach to learn sequence similarities for user-identification, Decis. Support. Syst. 155 (2022) 1–12. Art. no. 113718.

[22] B. Fan, W. Fan, C. Smith, H. Garner, Adverse drug event detection and extraction from open data: A deep learning approach, Inf. Process. Manag. 57 (1) (2020)

[23] T. Yang, et al., Fine-grained depression analysis based on Chinese micro-blog reviews, Inf. Process. Manag, 58 (6) (2021) 1–18. Arte. no. 102681.

[24] M. Zhang, B. Fan, N. Zhang, W. Wang, W. Fan, Mining product innovation ideas from online reviews, Inf. Process. Manag. 58 (1) (2021) 1–12. Art. no. 102389.

[25] B. Kim, J. Park, J. Suh, Transparency and accountability in AI decision support: explaining and visualizing convolutional neural networks for text information, Decis. Support. Syst. 134 (2020) 1–11. Art. no. 113302.

[26] D. Schniederjans, E.S. Cao, M. Schniederjans, Enhancing financial performance with social media: an impression management perspective, Decis. Support. Syst. 55 (4) (2013) 911–918.

[27] D. Schoeneborn, M. Morsing, A. Crane, Formative perspectives on the relation between CSR communication and CSR practices: pathways for walking, talking, and T(w)alking, Bus. Soc. 59 (1) (2020) 5–33.

[28] K. Podnar, Guest editorial: communicating corporate social responsibility, J. Mark. Commun. 14 (2) (2008) 75–81.

[29] M. Morsing, M. Schultz, K.U. Nielsen, The ’Catch 22′ of communicating CSR: findings from a Danish study, J. Mark. Commun. 14 (2) (2008) 97–111.

[30] S. Du, E.T. Vieira Jr., Striving for legitimacy through corporate social responsibility: insights from oil companies, J. Bus. Ethics 110 (4) (2012) 413–427.

[311 M. Besiou. M.L. Hunter. LN. van Wassenhove. A web of watchdogs: stakeholder media networks and agenda-setting in response to corporate initiatives, J. Bus. Ethics 118 (4) (2013) 709–729.

[32] D. Eberle. G. Berens. T. Li. The impact of interactive corporate social responsibility communication on corporate reputation. J. Bus. Ethics 118 (4) (2013) 731–746.

[33] L. Dalla-Pria. I. Rodríguez-de-Dios, CSR communication on social media: the impact of source and framing on message credibility. corporate reputation and WOM, Corp. Commun. 27 (3) (2022) 543–557

[34] S. Gupta, N. Nawaz, A. Tripathi, S. Muneer, N. Ahmad, Using social media as a medium for CSR communication. to induce consumer-brand relationship in the banking sector of a developing economy, Sustainability (Switzerland) 13 (7) (2021) 1–16. Art. no. 3700.

[35] Z. He, S. Liu, B.H. Ferns, C.C. Countryman, Pride or empathy? Exploring effective CSR communication strategies on social media, Int. J. Contemp. Hosp. Manag. 34 (8) (2022) 2989–3007.

[36] E.A. Jakob. H. Steinmetz, M.C. Wehner, C. Engelhardt. R. Kabst. Like it or not: when corporate social responsibility does not attract potential applicants, J. Bus Ethics 178 (1) (2022) 105–127.

[37] L. Ma, J.M. Bentley, Can strategic message framing mitigate the negative effects of skeptical comments against corporate-social-responsibility communication on social networking sites? Public Relat. Rev. 48 (4) (2022). Art. no. 102222.

[38] F. Naatu, S.A. Nyarko, Z.H. Munim, I. Alon, Crowd-out effect on consumers attitude towards corporate social responsibility communication, Technol. Forecast. Soc.

[39] M. Sciarelli, M. Tani, G. Landi, L. Turriziani, CSR perception and financial performance: evidences from Italian and UK asset management companies, Corp. Soc. Responsib. Environ. Manag. 27 (2) (2020) 841–851

[40] J. Yang, K. Basile, O. Letourneau, The impact of social media platform selection on effectively communicating about corporate social responsibility, J. Mark. Commun, 26 (1) (2020) 65–87.

[41] M.A. Islam, C. Deegan, Media pressures and corporate disclosure of socia responsibility performance information: a study of two global clothing and sports retail companies, Account. Bus. Res. 40 (2) (2010) 131–148.

[42] T.G.L.A. Van Der Meer, R. Vliegenthart, The consequences of being on the agenda: the effect of media and public attention on firms’ stock market performance, Communications 43 (1) (2018) 5–24

[43] T. Takeshita, Current critical problems in agenda-setting research. Int. J. Publio

[44] S.Y. Lee. How can companies succeed in forming CSR reputation? Corp. Commun

[45] L.V. Huang, T.E.D. Yeo, Tweeting #leaders: social media communication and retweetability of fortune 1000 chief executive officers on twitter. Internet Res. 28 (1) (2018) 123–142

[46] C. Flammer, A. Kacperczyk, The impact of stakeholder orientation on innovation evidence from a natural experiment, Manag. Sci. 62 (7) (2016) 1982–2001

[47] F. de Oliveira Santini, W.J. Ladeira, D.C. Pinto, M.M. Herter, C.H. Sampaio, B. J. Babin, Customer engagement in social media: a framework and meta-analysis, J. Acad. Mark. Sci. 48 (6) (2020) 1211–1228.

[48] A. Castillo, J. Benitez, J. Llorens, X.R. Luo, Social media-driven customer engagement and movie performance: theory and empirical evidence, Decis. Support. Syst. 145 (2021) 1–11. Art. no. 113516.

[49] S. Chung, A. Animesh, K. Han, A. Pinsonneault, Financial returns to firms’ communication actions on firm-initiated social media: Evidence from facebook business pages, Inf. Syst. Res. 31 (1) (Mar 2020) 258–285.

[50] S. Kim, The process of CSR communication—culture-specific or universal? Focusing on mainland China and Hong Kong consumers, Int. J. Bus. Commun. 59 (1) (2022) 56–82.

[51] S.R. Miller, L. Eden, D. Li, CSR reputation and firm performance: a dynamic approach, J. Bus. Ethics 163 (3) (2020) 619–636.

[52] Y. Zhang, F. Yang, Corporate social responsibility disclosure: Responding to investors’ criticism on social media, Int. J. Environ. Res. Public Health 18 (14) (2021) 1–27. Art. no. 7396.

[53] P.A. Ardiana, Stakeholder engagement in sustainability reporting: evidence of reputation risk management in large Australian companies, Aust. Account. Rey. 29 (4) (2019) 726–747.

[54] Y.N. Jiang, H. Park, Mapping networks in corporate social responsibility communication on social media: A new approach to exploring the influence of communication tactics on public responses, Public Relat. Rev. 48 (1) (2022). Art. no. 102143.

[55] J. Mickelsson, J.J.G.M. van Haren, J.G.A.M. Lemmink, Wrinkles in a CSR story: mismatched agendas in fast fashion service brands’ CSR reputation, J. Serv. Manag. 34 (2) (2023) 256–273.

[56] N. Verk, U. Golob, K. Podnar, A dynamic review of the emergence of corporate social responsibility communication, J. Bus. Ethics 168 (3) (2021) 491–515.

[57] C.E.H. Chua, V.C. Storey, X. Li, M. Kaul, Developing insights from social media using semantic lexical chains to mine short text structures, Decis. Support. Syst. 127 (2019) 1–10, Art, no, 113142

[58] S. Du, A. El Akremi, M. Jia, Quantitative research on corporate socia responsibility: a quest for relevance and rigor in a quickly evolving, turbulent world, J. Bus. Ethics (2022). https://doi.org/10.1007/s10551-022-05297-6.

[59] X. Chen, J. Ma, J. Wei, S. Yang, The role of perceived integration in WeChat usages for seeking information and sharing comments: A social capital perspective, Inf. Manag. 58 (1) (2021) 1–9. Art. no. 103280.

[60] Y. Zhou, Y. Yu, X. Chen, X. Zhou, Guanxi or justice? An empirical study of WeChat voting, J. Bus. Ethics 164 (1) (2020) 201–225.

[61] A. Yucel, A. Dag, A. Oztekin, M. Carpenter, A novel text analytic methodology for

[62] J. Evermann, J.R. Rehse, P. Fettke, Predicting process behaviour using deep learning, Decis, Support, Syst. 100 (2017) 129–140.

[63] S. Feuerriegel, J. Gordon, Long-term stock index forecasting based on text mining of regulatory disclosures, Decis. Support. Syst. 112 (2018) 88–97.

[64] A. Iovine, F. Narducci, G. Semeraro, Conversational recommender systems and natural language: a study through the ConveRSE framework, Decis. Support. Syst.

[65] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decis. Support. Syst. 104 (2017) 38–48.

[66] X. Liu, H. Shin, A.C. Burns, Examining the impact of luxury brand’s social media marketing on customer engagement: using big data analytics and natural language processing, J. Bus, Res, 125 (2021) 815–826.

[67] A.B. Carroll, The pyramid of corporate social responsibility: toward the moral management of organizational stakeholders, Bus. Horizons 34 (4) (1991) 39–48.

[69] J. Deylin, M.-W. Chang, K. Lee, K. J. a. p. a. Toutanova, "Bert: Pre-training of deep bidirectional transformers for language understanding," arXiv Preprint, 2018.

[70] Y. Kim, Convolutional neural networks for sentence classification, in: EMNLP 2014–2014 Conference on Empirical Methods in Natural Language Processing, Proceedings of the Conference, 2014, pp. 1746–1751, https://doi.org/10.3115/ v1/d14-1181 [Online]. Available: https://www.scopus.com/inward/record.uri? eid=2-s2.0-84961376850&doi=10.3115%2fv1%2fd14 1181&partnerID=40&md5=38be18f19001ceea9ee8cacdc60d2e3c.

[71] D. Tang, B. Qin, T. Liu, Document modeling with gated recurrent neural network for sentiment classification, in: Conference Proceedings - EMNLP 2015: Conference on Empirical Methods in Natural Language Processing. 2015. pp. 1422–1432

https://doi.org/10.18653/v1/d15-1167 [Online]. Available: https://www.scopus. com/inward/record.uri?eid=2-s2.0-84959928037&doi=10.18653%2fv1%2fd15- 1167&partnerID=40&md5=9b5eeb454db36f7e6b54fd9a55a3362c.

[72] K. Dearden, B. Crookston, H. Madanat, J. West, M. Penny, S. Cueto, What difference can fathers make? Early paternal absence compromises Peruvian children’s growth, Mater. Child Nutrition 9 (1) (2013) 143–154.

[73] K. Lee, W.Y. Oh, N. Kim, Social Media for Socially Responsible Firms: analysis of fortune 500’s twitter profiles and their CSR/CSIR ratings, J. Bus. Ethics 118 (4) (2013) 791–806.

[74] Y. Hong, P.A. Pavlou, Product fit uncertainty in online markets: nature, effects, and antecedents, Inf. Syst. Res. 25 (2) (2014) 328–344

[75] J.T. Feezell, Agenda setting through social media: the importance of incidenta news exposure and social filtering in the digital era, Polit. Res. Q. 71 (2) (2018) 482–494.

[76] H. Oh, K.Y. Goh, T.Q. Phan, Are you what you tweet? The impact of sentiment on digital news consumption and social media sharing, Inf. Syst. Res. 34 (1) (2023) 111-136.

[77] G. Manetti, M. Bellucci, The use of social media for engaging stakeholders in sustainability reporting, Account. Audit. Account. J. 29 (6) (2016) 985–1011.

[78] S. Okazaki, K. Plangger, T. Roulet, H.D. Men´endez, Assessing stakeholder network engagement, Eur. J. Mark. 55 (5) (2020) 1359–1384.

[79] C. Han, M. Yang, A. Piterou, Do news media and citizens have the same agenda on COVID-19? An empirical comparison of twitter posts, Technol. Forecast. Soc. Chang. 169 (2021). Art. no. 120849.

[80] K. Wenke, F.B. Zapkau, C. Schwens, Too small to do it all? A meta-analysis on the relative relationships of exploration, exploitation, and ambidexterity with SME performance, J. Bus. Res. 132 (2021) 653–665.

[81] Y.Y. Wang, C. Guo, A. Susarla, V. Sambamurthy, Online to offline: the impact of social media on offline sales in the automobile industry, Inf. Syst. Res. 32 (2) (2021) 582–604.

Shuihua Han, PhD. is a Professor of information systems at the School of Management, Xiamen University, China. He received his Ph.D. from Huazhong University of Science and Technology in China. His research on supply chain optimation, multiple channel man agement, and Big data analysis in Business has been published in journals such as Euro pean Journal of Operational Research, Annals of Operations Research, Decision Support Systems.

Zhenyuan Liu is a PhD candidate of information systems at the School of Management, Xiamen University, China.

Ziyue Deng is a PhD candidate of information systems at the School of Management, Xiamen University, China.

Shivam Gupta PhD. is a Professor at NEOMA Business School. France with a demonstrated history of working in the higher education industry. Skilled in Statistics, Cloud Computing, Big Data Analytics, Artificial Intelligence and Sustainability. Strong education professional with a Doctor of Philosophy (PhD) focussed in Cloud Computing and Operations Man agement from Indian Institute of Technology (IIT) Kanpur. Followed by PhD, postdoctoral research was pursued at Freie Universit¨at Berlin and SUSTech, China. He has completed HDR from University of Montpellier, France. He has published several research papers in reputed journals and has been the recipient of the International Young Scientist Award by the National Natural Science Foundation of China (NSFC) in 2017 and winner of the 2017 Emerald South Asia LIS award.

Patrick Mikalef is a Professor in Data Science and Information Systems at the Department of Computer Science. In the past, he has been a Marie Skłodowska-Curie post-doctoral research fellow working on the research project “Competitive Advantage for the Datadriven Enterprise” (CADENT). He received his B.Sc. in Informatics from the Ionian Uni versity, his M.Sc. in Business Informatics for Utrecht University, and his Ph.D. in IT Strategy from the Ionian University. His research interests focus the on strategic use of information systems and IT-business value in turbulent environments. He has published work in international conferences and peer-reviewed journals including the Journal of Business Research, British Journal of Management, Information and Management, In dustrial Management & Data Systems, and Information Systems and e-Business Management.
