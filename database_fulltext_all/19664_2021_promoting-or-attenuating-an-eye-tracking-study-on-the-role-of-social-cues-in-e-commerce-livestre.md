---
otero_id: 19664
otero_key: "U6JQ945K"
title: "Promoting or attenuating? An eye-tracking study on the role of social cues in e-commerce livestreaming"
authors: "Mengqi Fei; Huizhong Tan; Xixian Peng; Qiuzhen Wang; Lei Wang"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113466"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Promoting or attenuating? An eye-tracking study on the role of social cues in e-commerce livestreaming

Decision Support Systems

Mengqi Fei, Huizhong Tan, Xixian Peng, Qiuzhen Wang, Lei Wang

![](/api/attachments/U6JQ945K/fulltext/images/84b98df72f2a60465da2654b39002a11d653270bc4a43aa276b714ac33ea156e.jpg)

PII: S0167-9236(20)30221-9

DOI: https://doi.org/10.1016/j.dss.2020.113466

Reference: DECSUP 113466

To appear in: Decision Support Systems

Received date: 24 November 2019

Revised date: 26 November 2020

Accepted date: 26 November 2020

Please cite this article as: M. Fei, H. Tan, X. Peng, et al., Promoting or attenuating? An eye-tracking study on the role of social cues in e-commerce livestreaming, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113466

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# Promoting or attenuating? An eye-tracking study on the role of social cues in e-commerce livestreaming

Mengqi Fei<sup>a,b</sup>, Huizhong Tan<sup>a,b</sup>, Xixian Peng<sup>a,b</sup>, Qiuzhen Wang<sup>a,b,\*</sup>, Lei Wang<sup>a,b</sup>

<sup>a</sup> Department of Data Science and Engineering Management, School of Management, Zhejiang University, Hangzhou, PR China

<sup>b</sup> Neuromanagement Lab, Zhejiang University, Hangzhou, PR China

Corresponding author. Email: wqz@zju.edu.cn; Tel: +86 0571 88206827. Postal Address:

School of Management, Zhejiang University, 866 Yuhangtang Road, 310058, Hangzhou,

Zhejiang Province, China.

Mengqi Fei is a Ph.D. candidate in Information Systems at Zhejiang University. Her present research interests are e-commerce decision making and NeuroIS.

Huizhong Tan is a Ph.D. candidate in Decision Neuroscience at Zhejiang University. Her main ion making.

Xixian Peng is an Assistant Professor of Information Systems at Zhejiang University. His interests broadly include Human-Computer Interface (HCI), Mobile Advertising, and NeuroIS. His research has appeared in journals such as Information Systems Research, Journal of the Association for Information Science and Technology, Computers in Human Behavior, etc. and leading international IS conferences

Qiuzhen Wang is a Professor of Information Systems at Zhejiang University. Her present research interests are online consumer behavior and Human-Computer Interface (HCI) design in e-commerce. She has published in Decision Support Systems, Information and Management, International Journal of Information Management, Electronic Commerce Research, Journal of Business Research and other academic journals.

Lei Wang is a Professor of Decision Neuroscience at Zhejiang University. Her primary research interests include consumer decision-making, financial e-commerce, mobile payment. She has published in Frontiers in Psychology, PLOS ONE, Electronic Commerce Research, Psychology & Marketing and other academic journals.

Declarations of interest: none.

# Promoting or attenuating? An eye-tracking study on the role of social cues in e-commerce livestreaming

Mengqi Fei<sup>a,b</sup>, Huizhong Tan<sup>a,b</sup>, Xixian Peng<sup>a,b</sup>, Qiuzhen Wang<sup>a,b,\*</sup> , Lei Wang<sup>a,b</sup>

<sup>a</sup> Department of Data Science and Engineering Management, School of Management, Zhejiang

University, Hangzhou, PR China

<sup>b</sup> Neuromanagement Lab, Zhejiang University, Hangzhou, PR China

Abstract: Unlike general e-business, e-commerce livestreaming innovatively enables anchors to use instant social functions to communicate with viewers and present products in more vivid ways. However, little research has been done to understand the effects of social cues in a two-phase research framework to examine how two widely used social cues (i.e., herding message and interaction text) can affect viewers’ attention allocation procedure and purchase intention when watching e-commerce livestreaming. We also propose that anchor characteristics (i.e., attractiveness) may moderate the effects of social cues. To examine the above effects, we conduct a within-subject eye-tracking experiment. Using generalized linear mixed-effects models, we find that both herding message and interaction text can capture exogenous attention. In terms of endogenous attention to the product and anchor, interaction text shows a negative distracting effect, whereas herding message shows a positive spillover effect, negatively moderated by anchor attractiveness. Moreover, endogenous attention is positively related to purchase intention, while the effect of exogenous attention is relatively more complex, involving the competing mechanisms of the distracting effect and social influence. Theoretical and practical implications are discussed.

Keywords: social cues; e-commerce livestreaming; selective attention; purchase intention

## 1. Introduction

With the development of Internet techniques and mounting engagement in online shopping among consumers, business innovations in the e-commerce market are continuously emerging. Product presentation on e-commerce platforms has shifted from simple textual and graphical descriptions to formats with more vivid consumption content [1], such as livestreaming. E-commerce livestreaming is a type of audiovisual live broadcasting over the Internet in which anchors (also known as livestreamers) vividly demonstrate intricate products to attract and retain the viewer’s attention. Most livestreaming platforms provide a live chat interface alongside the video, which allows viewers to communicate with anchors in real time. To date, using livestreaming to boost sales has become an important strategy among most large e-commerce platforms worldwide (e.g., Taobao, JD, and Amazon). For instance, Taobao Live, established in 2016, engaged more than 400 million users in 2019. The gross merchandise volume of Taobao Live has exceeded 200 billion yuan<sup>1</sup>. Given the rapid growth of livestreaming, scholars from various domains, including Information Systems (IS), are engaging in increasingly focused discussions on viewer engagement techniques. For example, social functions (e.g., Danmaku), viewers’ characteristics (e.g., curiosity, tendency to comment), and anchors’ attributes (e.g., attractiveness, perceived friendship) have been found to be important contributing factors to viewers’ watching engagement [1–4]. Although prior studies have offered some insightful findings on how to engage livestreaming viewers, there remain some limitations.

First, the previous literature has consistently shown that social interactivity plays a critical positively influence consumers’ perceived engagement and enticement [1] and purchase intention [5]. Compared with general e-commerce modes, livestreaming is differentiated through its affordance of more effective social functions that allow anchors to capture the audience’s attention by delivering product information and interacting with viewers in real time, thu rendering the effects of social cues in livestreaming more complex. Specifically, selective attention theory suggests that there are both endogenous attention and exogenous attention [6] Endogenous attention, referring to voluntary or top-down attention as a result of a subjective effort, is goal-driven and directly relates to focal targets [7]. In e-commerce livestreaming anchors are indispensable sources of product information and thus closely connected with consumers’ goals of watching livestreaming and purchasing attributes and communication styles play important roles in attracting attention by vering product information ention to both the product and the anchor should also be regarded as endogenous attention in the context of e-commerce livestreaming. In contrast, exogenous n, referring to the involuntary or bottom-up attention attracted by a suddenly occurring attention triggered by distracting cues [7,8], including social cues, such as herding message and interaction text that suddenly appear on the screen during e-commerce livestreaming. Previous findings regarding the positive effects of social cues on decision making [9–12] might support the conjecture that greater interactiv perception through the use of social cues can induce more endogenous attention to focal stimuli. However, the appearance of social cues in e-commerce livestreaming occurs in real time and is sudden (for example, flickering messages at the left corner, as shown in Fig. 2A). Thus, socia cues might also be treated as distractors to viewers that cause endogenous attention with uncertain effects. As such, previous literature might not have adequately accounted for the complex effects of social cues on both endogenous attention and exogenous attention in the context of e-commerce livestreaming.

In addition, viewers are exposed to an abundance of information cues, and they usuall motivating purchase) [13]. For instance, when processing social cues that suddenly appear, the anchor and product remain in the viewer’s sight range, and the viewer’s gaze may move among these elements. Therefore, the effects of social cues on attention, especially goal-driven/endogenous attention, should not only be studied in isolation but should also consider the joint effects of other information [14], such as anchor characteristics. However, previous findings on the interaction between different cues can hardly be applied in the current research context. Indeed, much of the previous literature has focused on the interaction effect on self-reported psychological processes, such as quality perception and trust [15–17], while limited effort has been dedicated to examining the cognitive process of attention allocation. Moreover, the previous findings have been mixed. According to cue consistency theory, multiple cues can synergistically interact with each other to influence decision-making procedures [15,16], while the attenuating interaction effect between different cues has also been observed in previous literature [17]. In e-commerce livestreaming, information cues are displayed in a real-time pattern with a vividly animated format. Therefore, the interaction effect between social cues and anchor characteristics on endogenous attention needs to be further explored.

Finally, we take one step further by examining how endogenous attention and exogenous behavioral responses, most studies have held the mechanisms with exclusive visual cueing experimental tasks, suggesting that endogenous attention and exogenous attention compete with each other for control over cognition through different mechanisms [7,18–20]. As such, exogenous attention to social cues may distract endogenous attention from the product and anchor, thus negatively affecting purchase intention. However, several studies have observed the opposite effect: attention to peripheral social cues, such as purchase history records, could increase purchase intention because of the herding effect [9,21–23]. In other words, exogenous attention induced by social cues may have a positive spillover effect that influences consumer responses, providing another possible mechanism. However, the two influencing attention mechanisms remain underexplored in the e-commerce livestreaming context.

Taken together, these research gaps drive this paper to investigate the following research questions: How do social cues (i.e., herding message and interaction text) influence consumers endogenous attention and exogenous attention allocation while watching e-commerce livestreaming? How does anchor attractiveness moderate the effects of social cues on endogenous attention? How do consumers’ endogenous attention and exogenous attention influence their purchase intention?

To answer these questions, we develop a theoretical framework based on the stimulus-organism-response (S-O-R) theory [29–32]. Specifically, we focus on the effects of two widely used social cues (i.e., herding message and interaction text) in e-commerce livestreaming and one key anchor characteristic (i.e., attractiveness) on visual attention and subsequent experiment in which the frequency of the herding message and the number of words comprising the interaction text are observed as the independent variables, anchor attractiveness level is manipulated as the moderating variable, attention obtained through eye movement data, and self-reported purchase intention are considered the dependent variables. Our findings contribute to the livestreaming literature by exploring how livestreaming’s distinguishing features—social cues that appear suddenly and in real time—influence viewers’ attention allocation, while also considering the moderating role of anchor attractiveness. This study also contributes to the literature on selective attention with the exploration of different influencing mechanisms of endogenous attention and exogenous attention. Practically, this study provides valuable suggestions for various stakeholders, such as platform providers, e-commerce marketers, and interface designers, about how to use different cues to attract viewers’ attention.

This paper is structured as follows. In Section 2, we review the relevant literature and formulate our theoretical framework and hypotheses. In Sections 3 and 4, we introduce the details of the eye-tracking experiment and analysis results. In Section 5, we conclude our findings by discussing the implications, limitations, and future directions.

## 2. Theories and Hypotheses

To understand how consumers process social cues and form their purchase intention while watching e-commerce livestreaming, we build a two-phase research conceptual model (Fig. 1) based on S-O-R theory. S-O-R theory was initially proposed in the field of environmental psychology [24] and has been extensively applied to study online retailing [25,26]. Its central idea is that informational and environmental cues act as stimuli that influence individuals cognitive and emotional processing, in turn influencing their behavioral responses. Numerous empirical studies in the areas of e-commerce and human-computer interaction have demonstrated the applicability and suitability of S-O-R theory in explaining how individuals’ cognitive responses to various information stimuli can influence their final behavioral intentions

## [27–31].

![](/api/attachments/U6JQ945K/fulltext/images/1b1f1db053d25fb53f68618ce7291e1736daf20d1fbcd9463ea268039969dc0c.jpg)  
Fig. 1. The research conceptual model.

The social cues in e-commerce livestreaming videos act as the ―stimulus‖ to consumers, including herding message and interaction text. We consider visual attention the ―organism‖, which includes endogenous attention and exogenous attention based on selective attention theory [6,7]. Endogenous attention refers to consumers’ goal-driven attention. The product and ancho are the key factors that directly and closely relate to consumers’ goals of watching livestreaming and purchasing. Thus, the endogenous areas of interest (ENAOI) consist of the product and the anchor. Exogenous attention refers to stimulus-driven attention directed at the two flickering social cues in the corner of the interface (see Fig. 2A; EXAOI, the exogenous areas of interes consisting of two subareas—the herding message area, HAOI, and the interaction text area,

TAOI). Finally, purchase intention toward the promoted products in the livestreaming videos is studied as a ―response‖. Specifically, we propose that social cues have effects on both consumers’ endogenous attention and exogenous attention and discuss the interaction effects of anchor attractiveness with social cues on endogenous attention, as well as how endogenous attention and exogenous attention influence final purchase intention.

## 2.1. Attentional capture, distraction, and spillover effects of social cues

Previous research has consistently indicated the power of social influence; people are easily attracted by various social cues and follow others’ behaviors or demonstrate herding behaviors [23,32,33]. Consequently, the influence of social cues is an important research focus in various areas, including e-commerce [10,34–36]. For example, social cues such as word of mouth and sales [10,36–38] have been shown to significantly influence consumers’ information processing, distinct social cues: herding message and interaction text. The former reflects information about other viewers’ instant purchasing behaviors, flickering on the screen occasionally; the latter is interaction text about other viewers’ comments and questions, scrolling in the left-hand corner (see Fig. 2).

Different cues have varying effects on the human attention allocation procedure, which involves both exogenous attention capture and endogenous attention transfer [39,40]. Exogenous attentional capture is a bottom-up process in which salient stimuli automatically capture viewers attention [18,41], whereas endogenous attention transfer occurs as a top-down process in which the content or the cognition process of a stimulus promotes the redirection of attention to the focal target [40]. Herein, we propose that the two kinds of social cues in e-commerce and transfer effects on the allocation of endogenous attention and exogenous attention.

Regarding attentional capture [42], flickering social cues can act as salient distractors that attract attention. Previous literature has revealed that social cues, such as other buyers’ opinions, can quickly draw consumers’ attention, even when important product-related information is presented [14]. Moreover, the appearance of the two kinds of social cues accompanies animations like flickering and scrolling, which have also been shown to promote the effect of attracting attention [43]. Herein, increasing frequency and number of social cues (i.e., herding message pops up more frequently or interaction text consists of more words) should both capture a significant amount of the viewers’ attention to the areas in question. Thus, we propose the following hypotheses.

H1a: Frequency of herding message is positively related to attention to the HAOI.

H2a: Number of words comprising interaction text is positively related to attention to the TAOI. Concerning the roles of social cues on endogenous attention to the product and anchor, there may be both a negative distraction effect and a positive spillover effect. Specifically, due to limited attention resources, the more attention that is captured by social cues, the less attention that is allocated to the focal areas of product and anchor. Meanwhile, if social cues are highly relevant to a certain goal, endogenous attention contain explicit positive social information buyi the product. This kind of information involves a strong social influence n con ume formation processing [11,38] to positively affect their attitudes and perceived socia resence [3,12,44]. Thus, when herding messages about co-viewe instant purchase pop up frequently, the positive social effect may lead to an endogenous transfer of atte to the product and anchor areas, causing in turn a stronger positive spillover effect of the herding message compared to the distraction effect on endogenous attention. In contrast, the interaction text in the experiment, which mainly consists of neutral words, did not involve any positive or negative attitudes of co-viewers toward the products presented in the videos. Thus, this indicates that more interaction text, irrelevant to the consumers’ own goals, may only distract viewers’ attention away from the product and anchor [8,45]. Hence, we propose the following hypotheses.

H1b: Frequency of herding message is positively related to attention to the ENAOI. H2b: Number of words comprising interaction text is negatively related to attention to the ENAOI.

## 2.2. Moderating role of anchor attractiveness

Given that consumers are exposed to and process various information cues simultaneously (HCI) studies have consistently demonstrated the important role of human faces in capturing visual attention [46–48]. Similarly, in e-commerce livestreaming, anchors are vital to produc anchors—anchor attractiveness—which refers to the degree to which an anchor’s features are considered attractive attractive appearances but also through how they interact with the viewers, such as presenting product information professionally. Thus, unlike notions of attractiveness in the traditional e-commerce context, which only focus on human appearance [49–51], we refer to the literature on media and advertising to consider anchor attractiveness from various facets; specifically, we not only consider the anchors’ physical appearance but also the attractiveness of their voices [52]

and their professionalism [53,54].

There are usually two perspectives on the interaction effect of multiple cues. When cues are equally important, some studies have observed a positive interaction between multiple consistent cues regarding perceptions and evaluations [15,16]. This view is consistent with cue consistency theory, suggesting that different information cues can synergize with each other to influence ve shown the opposite finding that a negative interaction can exist when these cues have different priorities or degrees of informativeness [10,17,56]. Specifically, the original effect of a certain cue on perception can be attenuated when other cues more informative or are of higher priority. For instance, extrinsic social cues (e.g., deals) influence on consumer evaluation and behaviora intention when intrinsi ) are presented [10]. This view is congruent with the perspective of cue diagnosticity, which holds that cues with higher diagnosticity, such as sales level, could suppress the effect of less diagnostic cues, such as stock level [57]. Because all of the important product information is delivered and presented by the anchor in an e-commerce livestreaming, an anchor’s characteristics play an important part in determining whether livestreaming can effectively drive the sales of promoted products [4]. As such, an anchor’s attractiveness should be of greater priority in attracting viewers’ attention than other information such as social cues. An anchor with high attractiveness can immediately capture more attention and would thus prompt viewers to respond more favorably to the information conveyed by the anchor, rather than the social cues generated by their co-viewers. In other words, the effects of social cues on attention would become less significant. However, an anchor with less attractiveness may might be low diagnostic and insufficient in providing product-related information to viewers. As a result, viewers are more likely to rely on social cues, and the effects of such cues on attention will be more salient. In addition, considering attention allocation among different elements, once an element (i.e., the anchor area) is selected and fixated upon, only its features influence the attention engagement generated (i.e., endogenous attention), while other elements (such as social cues) no longer play an important role [39]. Therefore, once high anchor may be attenuated. Hence, we propose the following hypotheses.

H3a/b: Anchor attractiveness negatively interacts with the effect of (a) herding message /(b) interaction text on attention to the ENAOI.

## 2.3. Effects of endogenous attention and exogenous attention

When considering both endogenous attention to the product and anchor and exogenous attention to social cues, it is crucial to determine their relationship. The extant literature on selective attention has argued that endogenous attention and exogenous attention compete with each other for attention control [18,19] and thus negatively associate with each other [20,42,58]. Specifically, as a distractor, exogenous attention has a negative competition effect on endogenous attention [7,18], and endogenous attention inhibits exogenous attention through voluntary control [42,58]. This effect has also been supported by the under-additive relationship between stimulus-driven and goal-driven attentional capture in eye movement data in previous research [20]. Similarly, in the context of e-commerce livestreaming, we propose a competing relationship under the following hypotheses.

H4a: Attention to the HAOI is negatively related to attention to the ENAOI.

H4b: Attention to the TAOI is negatively related to attention to the ENAOI.

Now that we know that there are both endogenous attention and exogenous pathways in final intention. In this study, we focus on purchase intention, which is defined as an individual’s willingness to click the product detail link for subsequent purchases after watching the livestreaming video. Previous literature has indicated that attention paid to products can predict intention and preferences [59,60], in which longer attention to a product usually indicates greater interest in it [13]. For example, attended products are more likely to be chosen than neglected products [59–61]. Accordingly, more endogenous attention indicates greater interest in the product and the anchor, which is information related directly to the purchase task, in that a viewer’s purchase intention will be promoted. Thus, we propose the following hypothesis regarding the effects of endogenous attention.

H5: Attention to the ENAOI is positively related to purchase intention.

Regarding the effects of exogenous attention on purchase intention, there are two different theoretical perspectives: the negative distraction effect and positive social influence. On the one hand, due to the competing relationship between endogenous attention and exogenous attention mentioned previously [7,18], exogenous attention to social cues can distract the effect of endogenous attention on the product and anchor areas. In this way, both attention to the herding message and the interaction text are likely to have negative distraction effects on the final purchase intention through the negative relationship with endogenous attention. On the other hand, attention to the herding message may also have a positive effect on purchase intention; as the studies on social influence have indicated, consumers tend to refer to the purchase behavior of other consumers [22,32,33], and positive social cues can promote consumers’ attitudes, beliefs, and purchases [12,34,35]. Moreover, several eye-tracking studies have found that attention to purchase history records [9] or positive peripheral cues [21] is positively related to consumers purchase intention. Thus, more attention to the herding message may also cause a stronger herding influence and improve viewers’ attitudes toward the product and anchor, which may in turn strengthen purchase intention. Unlike the herding message, which directly relates to purchase behavior, most of the interaction text is less relevant to viewers when they are considering whether to buy the product. In this case, attention to the interaction text area should only show a negative influence on purchase intention by grabbing attention resources from the product and anchor areas. Hence, we propose the competing hypotheses involving both the positive and negative effects of attention to the HAOI and one hypothesis to convey only the negative effect of attention to the TAOI:

H6: Attention to the HAOI is (a) positively or (b) negatively related to purchase intention.

H7: Attention to the TAOI is negatively related to purchase intention.

## 3. Research Methods

## 3.1. Experiment design

This study adopted a within-subject eye-tracking experiment to examine the proposed hypotheses. Subjects were asked to watch 12 real-world e-commerce livestreaming videos from Taobao Live with varying frequencies and numbers of social cues (considered the observed independent variables) and different levels of anchor attractiveness (considered the manipulated moderating variable). Subjects’ attention data were automatically recorded by the eye-tracking technique, and their purchase intention data were obtained by self-reported intention.

## 3.2. Materials

We captured real-word e-commerce livestreaming videos on Taobao Live as the experimental stimuli. Taobao Live is one of the largest e-commerce livestreaming platforms. Its main interface is shown in Fig. 2A. In the central area of Taobao Live videos, an anchor is trying to promote sales by vividly introducing detailed information about the products. The small area at the top presents the basic information, including the livestreaming room ID, shop name, number of viewers, etc. The left-hand corner of the screen presents social cues, including flickering messages that show co-viewers’ purchase behaviors instantly, such as ―XXX is on the way to buy‖, and scrolling text of co-viewers’ real-time comments, which usually involve questions about the product or requests addressed to the anchor like ―Please show us the back of the T-shirt‖. At the bottom of the screen is the interaction input window, consisting of a shopping bag with hyperlinks for the products, an input box for viewers to communicate with the anchor, a sharing button, and a ―like‖ button.

![](/api/attachments/U6JQ945K/fulltext/images/f5b314a92edff1ada5e7a5b57d27223b536049a544ace14cd80679bb389184d5.jpg)  
Fig. 2. The e-commerce livestreaming interface: A) the elements in the original screen; B) the AOIs (areas of interest) in the stimulus screen.

There were three main criteria to obtain our final stimulus pool. First, the anchors in the e-commerce livestreaming videos should vary in attractiveness. To accomplish this goal, we randomly captured the livestreaming videos from different anchors (four males and four females) on Taobao Live and conducted a pretest to select suitable anchors. In the pretest, 41 subjects were asked to evaluate the attractiveness of the anchors from three aspects: appearance, voice characteristics, and professional skills (i.e., their expressive ability, product understanding, and ability to explain) on a 7-point Likert scale (1 = very low, 7 = very high). Wilcoxon’s statistics showed that there were significant differences between the anchors with the highest and lowest attractiveness for both male anchors (low = 4.584, high = 4.880, Z = -2.140, p = 0.032) and female anchors (low = 4.244, high = 4.949, Z = -5.104, p < 0.001). Thus, the two male and two female anchors with the highest and lowest attractiveness were selected. Second, the appearance of social cues should vary across different videos. We randomly recorded more than 30 livestreaming videos<sup>2</sup> from the four anchors selected in step 1, and among them, we carefully pre-edited the videos by cutting them to the same duration of 40 seconds. Then, we calculated the appearance of social cues by the frequency of the herding message and the number of words varying social cues for each anchor. Finally, we obtained 12 videos (four anchors with three videos for each) as the raw experimental stimuli with a varying frequency of herding messages (mean = 9.92, min = 2, max = 17, standard deviation = 5.564) and a varying number of words guaranteeing that all 12 videos included the same important content, including trying on clothes, showing details about the clothes, and sharing matching tips. Moreover, sensitive livestreaming information, such as the room ID and anchor name, and other interference elements in the videos were removed.

## 3.3. Subjects

The subjects were recruited from a university in southern China and were paid 20 to 30 yuan for their participation. A total of 66 subjects with rich online shopping experience (i.e., shopping online more than once per month) participated in our experiment. Among them, eight subjects’ data were excluded from the data analysis since they did not pass the information recall test or their eye-blinking frequencies were too high to track valid eye movement data. As such, the data analysis was completed with data from 58 valid subjects (28 females, 30 males; mean age = 22.47).

## 3.4. Apparatus

The apparatus was a set consisting of an SMI ETG eye tracker and analysis equipment, an eight-inch tablet PC, an adjustable holder, and an external keypad in the laboratory. While participating in the experiment, subjects wore nonintrusive eye-tracking glasses to watch th e-commerce livestreaming videos presented on the tablet display (approximately 60 cm from the eyes) and used the keypad to complete the experimental tasks. Eye movement data were automatically tracked with a sample rate of 120 Hz. BeGaze 3.0 software was used to preprocess the eye movement data. The fixation floor time was set at 100 milliseconds.

## 3.5. Procedure

After entering the eye-tracking lab, the subjects were asked to read and sign an informed consent form, on which they were also informed that their task was to watch Taobao Live and select appropriate clothes for their male and female friends. Then, the subjects were introduced to equipment. The experiment started only after the subjects fully understood the experimental procedure. First, the subjects were asked to evaluate their initial preference for 12 pieces of clothing based on a basic description and pictures. Then, they watched the 12 corresponding Taobao Live videos and answered binary decision questions on whether they were willing to click purchases. To eliminate possible learning effects, the video were shown in a random order across four anchors for each subject. As they watched the videos, the subjects’ eye movements were automatically recorded by the eye tracker after they passed th calibration test in each trial. Finally, a post-experiment questionnaire was distributed that asked for the subjects’ evaluations of the anchors’ attractiveness and their attitudes toward e-commerce livestreaming, as well as a recall test about the stimulus video details. The full experiment lasted approximately 20 minutes per subject.

## 3.6. Measures

Independent variables. We have two independent variables in this study. First, herding message is a continuous variable measured by the total frequency of the herding messages that pop up during each livestreaming stimulus video. Second, interaction text is a continuous variable measured by the total number of words comprising the scrolling interaction text in each variables (the descriptive statistics were mentioned in Section 3.2), they were standardized for the subsequent data analysis.

Moderating variable. We consider anchor attractiveness as a moderator, which is manipulated at low and high levels.

Dependent variables. Attention, as one of our main variables, is measured from the eye movement data. As two key entific metrics for ascertaining the engagement of attention and cognitive process, the fixation time and count are chosen as the primary measurements [13,59]. Based on our research objectives, we divided the e-commerce livestreaming interface into different AOIs and focused on attention to the ENAOI (i.e., the areas of product and anchor face)<sup>3</sup> and attention to the two types of EXAOI (i.e., the area of herding message, HAOI, and the area of interaction text, TAOI), as displayed in Fig. 2B. Due to the varying sizes of different AOIs and the variance among different subjects’ eye-movement data [27,62], we adopted the relative fixation percentage data<sup>4</sup> instead of using absolute values directly. Specifically, we performed normalization at two levels—area size and subject—by calculating the fixation percentage in a certain AOI to account for the whole screen [43,46], dividing it by the AOI coverage percentage [14] and then standardizing it across subjects. Purchase intention is considered anothe dependent variable comprising subjects’ behavioral response. It is a binary measure reflecting whether the subjects chose to click on the product details link for subsequent purchases.

Control variables: We included the anchors’ and subjects’ gender, subjects’ age, and perceived initial preference for the products (on a 7-point Likert scale) as control variables in the data analysis.

## 4. Data Analysis and Results

## 4.1. Manipulation check of anchor attractiveness

In the post-experiment questionnaire, each subject rated the attractiveness of the four anchors in terms of their appearance, voice, and professionalism using a 7-point Likert scale (1 = very low, 7 = very high). Wilcoxon’s statistics based on negative ranks showed that there were significant differences in the average scores of the three dimensions of attractiveness between high and low attractiveness for both the male and female anchors (male: low = 3.293, high = 4.690, $Z = - 6 . 0 3 6$ $\mathrm { { p } < 0 . 0 0 1 }$ ; female: low $= \therefore \Im \Re$ $\mathrm { { h i g h } } = 4 . 3 2 8$ $Z = - 5 . 5 3 4$ $\mathsf { p } < 0 . 0 0 1 )$ ), suggesting that our manipulation of anchor attractiveness was successful.

## 4.2. Analysis strategy

The main dataset (total 58 × 12 = 696 records) consisted of repeated-measurement data with a 4 (two male and two femal anchors with high and low attractiveness) × 3 (three differen livestreaming videos per anchor) within-subject design. The generalized linear mixed-effects model (GLMM) [63] with subjects as random effects is suitable for our dataset because it can handle overdispersion and complicated repeat measures better than ANOVA or other linear models [64,65]. Thus, we adopted GLMM considering repeated measures using SPSS 22.0 software to analyze the within-effects of social cues. Also, we used multilevel SEM with Mplus

8.3 software to check the robustness. The results by multilevel SEM showed no significant difference from the results by GLMM, as shown in the supplementary materials. Therefore, this paper only reports the results by GLMM.

## 4.3. Descriptive results

Attention: Table 1 provides the descriptive statistics of attention to each AOI. Subjects mainly attended to the ENAOI while they were occasionally $\pmb { \mathrm { 2 ^ { + + r } } } \mathbf { \dot { a } _ { - } } ^ { + } \mathbf { \dot { = } } \mathbf { 1 }$ by the HAOI and TAOI.

Purchase intention: There were 381 (54.7%) trials that showed a ―0‖ value, indicating that the subject refused to view the product details for further purchase, and 315 (45.3%) trials that showed a ―1‖ value, indicating that the subject chose to view product details.

## Table 1

Descriptive statistics for attention.

<table><tr><td>AOI</td><td>%Trials (percent)</td><td>Average fixation time (ms)</td><td>Average fixation counts</td></tr><tr><td>ENAOI</td><td>100.00</td><td>26737.55</td><td>43.79</td></tr><tr><td>HAOI</td><td>60.92</td><td>561.80</td><td>1.68</td></tr><tr><td>TAOI</td><td>78.02</td><td>1542.27</td><td>4.59</td></tr></table>

Notes: ENAOI = the endogenous areas of interest including the product and anchor areas; HAOI = the herding message area of interest; TAOI = the interaction text area of interest. ―%Trials‖ indicates the percentage of trials during which the AOI was visited. The fixation time and count

data are the original fixation data before normalization and standardization.

## 4.4. Effects of social cues on selective attention

Table 2 displays the results regarding the effects of two different social cues and anchor attractiveness on relative attention allocation. Since the GLMM results of the fixation count and the fixation time are similar, and both of them are effective measurements of attention [43,46,59], for relative fixation count are shown in the supplementary $\therefore \mathrm { a } \mathrm { a } _ { \mathrm { c } } \mathrm { \acute { \Omega } } _ { \mathrm { d l s } } )$

Relative attention to HAOI: Herding message has a significantly positive effect $( \mathsf { b } = 0 . 1 3 9$ $\mathsf { p } < 0 . 0 0 1 )$ when control variables are $\mathbf { n } ^ { c } \cdot \mathbf { 1 } \mathbf { i }$ cluded (Model 1), while the effect becomes not supporting H1a.

Relative attention $\mathbf { t } { \boldsymbol { r } } , \mathbf { \bar { \mu } } _ { \mathbf { x } } . \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda }$ Interaction text has a marginally significant effect $( \mathbf { b } = 0 . 0 6 0$ $\mathsf { p } = 0 . 0 7 0 )$ when control variables are not included (Model 3), maintaining significance $( { \bf b } =$ $0 . 0 8 0 , \mathfrak { p } = 0 . 0 1 9 )$ with control variables included (Model 4). Thus, H2a is partially supported.

Relative attention to ENAOI: Herding message has a significantly positive influence $( { \bf b } =$ $0 . 1 4 8 , \mathrm { ~ p ~ < ~ } 0 . 0 0 1 \rangle$ ), while interaction text has a significantly negative influence $( \mathsf { b } = - 0 . 2 0 9 , \mathsf { p } <$ 0.001), as shown in Model 5, and the effects remain consistent with control variables included, as shown in Model 8, supporting H1b and H2b. Considering the moderating effects in Model 6, the interaction term of anchor attractiveness and herding message is significantly negative (b = -0.236, $\mathsf { p } < 0 . 0 0 1 )$ , while the interaction term of anchor attractiveness and interaction text is not significant (b = 0.118, p = 0.147). Hence, H3a is supported, while H3b is not supported. To have a clear understanding of the significant interaction effect of herding message and anchor attractiveness, we split the data into two based on the level of anchor attractiveness, and we conducted two GLMM analyses separately. The results showed that the effect of the herding message on relative attention to the ENAOI is $\mathrm { s . \thinspace { \sigma } . \ i i f }$ icantly positive in the case of low anchor attractiveness (b = 0.249, $\mathsf { p } < 0 . 0 0 1 )$ but insignificant in the case of high anchor attractiveness (b $= 0 . 0 1 4$ , p = 0.788). In addition, both relative attention to the HAOI (b = -0.221, $\mathrm { p } < 0 . 0 0 1 )$ ) and the TAOI (b = -0.214, $\mathrm { p } < 0 . 0 \mathrm { t } ^ { \cdot 1 }$ have significantly negative relationships with relative attention to the ENAOI, as shown in Model 8, supporting H4a and H4b.

## Table 2

Effects of social cues on relative attention to the HAOI, TAOI, and ENAOI.

<table><tr><td colspan="3">Dependent variable: HAOI</td><td colspan="3">TAOI</td><td colspan="3">ENAOI</td></tr><tr><td>Regressor</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td><td>Model 6</td><td>Model 7</td><td>Model 8</td></tr><tr><td colspan="9">Journal Pre-proof</td></tr><tr><td>HM</td><td>0.139***</td><td>0.245</td><td></td><td></td><td>0.148***</td><td>0.249***</td><td>0.263***</td><td>0.613**</td></tr><tr><td></td><td>(0.035)</td><td>(0.159)</td><td></td><td></td><td>(0.035)</td><td>(0.047)</td><td>(0.045)</td><td>(0.189)</td></tr><tr><td>IT</td><td></td><td></td><td>0.060</td><td>0.080*</td><td>-0.209***</td><td>-0.263***</td><td>-0.197***</td><td>-0.203***</td></tr><tr><td></td><td></td><td></td><td>(0.033)</td><td>(0.034)</td><td>(0.035)</td><td>(0.041)</td><td>(0.040)</td><td>(0.040)</td></tr><tr><td>AA</td><td></td><td></td><td></td><td></td><td></td><td>0.118</td><td>0.105</td><td>0.072</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>(0.068)</td><td>(0.065)</td><td>(0.079)</td></tr><tr><td>HM × AA</td><td></td><td></td><td></td><td></td><td></td><td>-0.236**</td><td>-0.269***</td><td>-0.192*</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>(0.071)</td><td>(0.068)</td><td>(0.077)</td></tr><tr><td>IT × AA</td><td></td><td></td><td></td><td></td><td></td><td>0.118</td><td>0.014</td><td>-0.054</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>(0.081)</td><td>(0.078)</td><td>(0.086)</td></tr><tr><td>HAOI</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.215***</td><td>-0.221***</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>(0.036)</td><td>(0.036)</td></tr><tr><td>TAOI</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.214***</td><td>-0.214***</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>(0.037)</td><td>(0.037)</td></tr><tr><td>Controls</td><td></td><td>Included</td><td></td><td>Included</td><td></td><td></td><td></td><td>Included</td></tr><tr><td>Intercept</td><td>-0.000</td><td>0.325</td><td>0.000</td><td>0.154</td><td>-0.000</td><td>-0.048</td><td>-0.039</td><td>0.008</td></tr></table>

<table><tr><td colspan="8">Journal Pre-proof</td></tr><tr><td>(0.707)</td><td>(0.965)</td><td>(0.713)</td><td>(1.090)</td><td>(0.696)</td><td>(0.694)</td><td>(0.644)</td><td>(0.888)</td></tr></table>

## Model summary statistics

<table><tr><td>AICc</td><td>1945.844</td><td>1953.337</td><td>1891.749</td><td>1897.680</td><td>1910.702</td><td>1905.976</td><td>1832.708</td><td>1836.581</td></tr><tr><td>BIC</td><td>1959.436</td><td>1966.912</td><td>1905.341</td><td>1911.255</td><td>1924.290</td><td>1919.551</td><td>1846.275</td><td>1850.129</td></tr><tr><td>N</td><td>696</td><td>696</td><td>696</td><td>696</td><td>696</td><td>696</td><td>696</td><td>696</td></tr></table>

Notes: (1) The dependent variables of the relative fixation time of each AOI (ENAOI, the product and anchor areas; HAOI, the herding message area; TAOI, the interaction text area) follow a normal distribution. The main independent variables are the herding message (HM), interaction text (IT), and anchor attractiveness (AA), the last of which is a binary variable with the reference value of low attractiveness level. (2) The number in the first row of every cell is the coefficient of the fixed effect. The standard error of each coefficient is displayed in parentheses. Significance levels \*\*\* at 0.001, \*\* at 0.01, and \* at 0.05. ―AICc‖ is the Akaike information criterion with a small sample correction, and ―BIC‖ is the Bayesian information criterion. (3) Control variables: anchor gender, subject’s initial preference for the product, subject gender, and subject age. $\mathrm { \vec { S i } } _ { \mathcal { S } ^ { \bot } }$ ificant effects of control variables $( \mathtt { p } < 0 . 0 5$ only): subject gender (male vs. female)  HAOI (b = -0.242, p = 0.031), anchor gender (male vs. female) TAOI (b = 0.184, $\mathtt { p } = 0 . 0 0 8 )$ , and subject’s initial preference for the product  ENAOI (b = 0.080, p = 0.029).

## 4.5. Effects of selective attention on purchase intention

Purchase intention is a binary variable reflecting whether subjects decide to view product details for further purchases. Thus, GLMM with a logit link was adopted to examine the effect of relative attention on purchase intention. The estimated fixed coefficients and summary statistics are displayed in Table 3. As shown in Model 10, which includes the control variables, the overal prediction accuracy when taking 0.5 as the threshold level is 62.5%, indicating that the model performs well in predicting the effect of relative attention on purchase intention. Specifically, both relative attention to the ENAOI (B = 0.402, $\begin{array} { r } { \mathbf { p } < 0 . 0 0 1 , } \end{array}$ ) and HAOI (B = 0.286, p = 0.002) have significantly positive effects on purchase intention, supporting H5 and H6a. The effect of relative attention to TAOI on purchase intention is not significant (B = 0.091, p = 0.298). Therefore, H7 is not supported.

## Table 3

Effects of relative attention on purchase intention.

<table><tr><td>Dependent variable: Purchase intention</td><td colspan="2">Model 9</td><td colspan="2">Model 10</td></tr><tr><td>Regressors</td><td>B</td><td>Exp(B)</td><td>B</td><td>Exp(B)</td></tr><tr><td rowspan="2">ENAOI</td><td>0.346***</td><td>1.414</td><td>0.402***</td><td>1.495</td></tr><tr><td>(0.087)</td><td></td><td>(0.091)</td><td></td></tr><tr><td rowspan="2">HAOI</td><td>0.207*</td><td>1.230</td><td>0.286**</td><td>1.331</td></tr><tr><td>(0.084)</td><td></td><td>(0.090)</td><td></td></tr><tr><td rowspan="2">TAOI</td><td>0.100</td><td>1.105</td><td>0.091</td><td>1.095</td></tr><tr><td>(0.084)</td><td></td><td>(0.087)</td><td></td></tr><tr><td>Controls</td><td></td><td></td><td>Included</td><td></td></tr><tr><td colspan="5">Journal Pre-proof</td></tr><tr><td>Intercept</td><td>-0.196</td><td>0.822</td><td>-1.480</td><td>0.228</td></tr><tr><td></td><td>(1.713)</td><td></td><td>(1.909)</td><td></td></tr><tr><td colspan="5">Model summary statistics</td></tr><tr><td>AICc</td><td colspan="2">2983.766</td><td colspan="2">3046.283</td></tr><tr><td>BIC</td><td colspan="2">2997.350</td><td colspan="2">3059.849</td></tr><tr><td>-2 Log pseudo likelihood</td><td colspan="2">2977.731</td><td colspan="2">3040.248</td></tr><tr><td>N</td><td colspan="2">96</td><td colspan="2">696</td></tr></table>

Notes: (1) The dependent variable of the purchase intention follows a binomial probability distribution. The independent variables are the relative fixation time of each AOI (ENAOI, the product and anchor areas; HAOI, the herding message area; TAOI, the interaction text area). (2) The number in the first row of every cell is the coefficient of the fixed effect. The standard error of each coefficient is displayed in parentheses. Significance levels \*\*\* at 0.001, \*\* at 0.01, and \* at 0.05. ―Exp(B)‖ indicates the odds ratio. $^ { 6 6 } \mathrm { A L C c } ^ { 5 9 }$ is the Akaike information $^ { 6 6 } \mathrm { B I C } ^ { 5 }$ is the Bayesian information criterion. (3) Control variables: anchor gender, subject’s initial preference for the product, subject gender, and subject age. Significant effects of control variables $\mathrm { ( p < 0 . 0 5 \ o n l y ) }$ : anchor gender (male vs. female)  purchase intention $( \boldsymbol { \mathrm { b } } = 0 . 5 9 3 , \boldsymbol { \mathrm { p } } < 0 . 0 0 1 )$ ), and subject’s initial preference for the product  purchase intention $( \mathbf { b } = 0 . 4 0 7 , \mathbf { p } < 0 . 0 0 1 )$

## 5. Discussion

## 5.1. Findings

Based on the S-O-R framework, the current research proposes a model to understand the role of social cues (i.e., herding message and interaction text) in the context of e-commerce livestreaming. Through a within-subject eye-tracking experiment, we examine the proposed model. The results of hypothesis testing are summarized in Table 4.

First, consistent with the previous findings on attention capture by salient stimuli [41,43], the two kinds of social cues can each attract exogenous attention. Specifically, we find that the increased appearance of a herding message and the use of interaction text can attract more attention from viewers to the corresponding areas. However, rding message and interaction text play different roles in influencing viewers’ endogenous attention to the focal areas of the product and anchor. The herding message has a positive spillover effect on endogenous attention because of social influence. That is, people may be eager to pay attention to the products that many others are buying at the same time [9–12]. In contrast, interaction text is only treated as a distractor; that is, increasing number of interaction text words leads to less endogenous attention [8,45].

Second, in contrast to the synergistic relationship between multiple cues regarding perceptions [15,16], we find that anchor attractiveness attenuates the positive effect of herding message on endogenous attention. Instead of promoting each other, herding message plays a significant role in affecting endogenous attention only in the case of low anchor attractiveness. This is because, compared to herding message, anchor characteristics are subconsciously prioritized by viewers when watching e-commerce livestreaming. As such, our finding supports the attenuating perspective [10,17,39], rather than the synergistic view, regarding how differen cues in e-commerce livestreaming jointly influence viewers’ attention allocation. However, the interaction text seems to be a less relevant product cue and a robust distractor for endogenous attention, suggesting that it might not be interrupted by the different levels of anchor endogenous attention.

Finally, the different mechanisms underlying how endogenous attention and exogenous attention influence purchase intention are revealed in this study. Not surprisingly, viewers purchase intention increases with more attention allocated to the product and anchor, which provides evidence of the predictive effectiveness of attention on intention [59–61]. However, the effects of exogenous attention to herding message and interaction text are complicated. On the one hand, we find that both of them compete with endogenous attention [7,20,58], as indicated by the significantly negative associations with endogenous attention. Additionally, we observe that exogenous attention to the herding message has a positive effect on purchase intention: th viewers’ herding mindset compels them to buy a product that others are actively purchasing. This positive social influence of herding message [9,12,21] overwhelms the negative distracting effec [20,42,58]. However, since the interaction text is less relevant to product information, its attention engagement might not affect consumers’ cognitive processing of the products and further influence purchase intention.

## Table 4

Results of hypotheses testing.

Proposed hypotheses Results H1a Herding message  (+) attention to the HAOI. Partially supported H2a Interaction text  (+) attention to the TAOI. Partially supported H1b Herding message  (+) attention to the ENAOI. Supported H2b Interaction text  (-) attention to the ENAOI. Supported H3a Anchor attractiveness H3b Anchor attractiveness × interaction text  (-) attention to the ENAOI. Not supported H4a Attention to the HAOI  (-) attention to the ENAOI. Supported H4b Attention to the TAOI  (-) attention to the ENAOI. Supported H5 Attention to the ENAOI  (+) purchase intention. Supported H6a/b Attention to the HAOI  (+ or -) purchase intention. H6a was supported

Notes: ENAOI = the endogenous areas of interest including the product and anchor areas; HAOI = the herding message area of interest; TAOI = the interaction text area of interest.

## 5.2. Implications

This study provides important theoretical insights. First, we focus on a rather novel interface feature in e-commerce livestreaming—the social cue—thereby contributing to HCI research [22,26,37]. Social cues are regarded as essential factors in various e-commerce contexts [34,35,37], yet little has been accomplished to their effects in an e-commerce livestreaming setting. Based on the S-O-R theory, we build a theoretical framework to explore how the two kinds of social cues (i.e., herding message and interaction text) influence viewers cognitive processes and behavioral intention. More importantly, we employ real-time eye movement data to discover the proposed underlying cognitive mechanisms. In doing so, we reveal the capture, distraction, and spillover effects of social cues on exogenous and endogenous attention. As a result, the current research contributes to the HCI and e-commerce literature by providing an exploratory theoretical framework to understand the role of social cues in e-commerce livestreaming, as well as the underlying mechanisms.

Second, our investigation of the interaction effects between social and anchor cues on attention deepens understanding of how different informational cues jointly influence the cognitive process during the viewing of e-commerce livestreaming. We illustrate the negative interaction between herding message and anchor attractiveness on endogenous attention with eye-tracking evidence, consistent with the previous finding of attenuating interaction between different cues on perception [10,17,39]. Moreover, we enrich the implications tied to anchor attractiveness [49,50] in e-commerce livestreaming by drawing from media and advertising studies [52–54] to better account for its role in audiovisual stimuli. Overall, our investigation on the moderating role of anchor attractiveness not only extends related findings on informational cues into the context of e-commerce livestreaming but also further highlights the importance of human features in the media area.

Third, this study offers some insightful findings in terms of how attention influences human attention and exogenous attention in the simplified visual cue context [20,42,58]. Our research is grounded in a real-life decision context, which involves a more complicated cognitive process. Accordingly, our investigation on the effects of endogenous attention and exogenous attention has integrated related findings from diverse theoretical views. Specifically, our findings of the negative relationship between exogenous and endogenous attention support the view of selective attention [7,20,58]; the positive effect of endogenous attention on purchase intention also supports the previous findings of the predictive effectiveness of attentional engagement [59–61]; finally, the positive effect of attention to a herding message on purchase intention reveals the two possible influencing routes of exogenous attention on human response: indirect distraction effect through endogenous attention and direct positive social influence. Taken together, this study provides a systematic and comprehensive understanding of attention’s complicated role in determining behavioral response.

This study also has implications for managerial practice. As an emerging e-business, e-commerce livestreaming platforms should provide a well-designed interface to facilitate viewers’ processing of product information, ultimately converting viewers into buyers. Meanwhile, many platforms tend to add increasing elements to their e-commerce livestreaming interfaces. However, most of these design elements are introduced without reference to any scientific research that confirms their effectiveness. Our findings suggest that platform providers should exercise careful consideration when integrating various social functions into e-commerce livestreaming. Based on our findings, the use of herding message can be increased to some degree, as it can attract more attention to the product and anchor. Conversely, the use of interaction text should be reduced due to its negative distraction effects. In other words, designers should aim to simplify the user interface to decrease the attentional distraction effects by unimportant elements. In addition, although it might seem like an obvious choice for platforms to employ more attractive anchors, the tradeoff between different cues utilization should be undertaken cautiously when considering using social cues simultaneously. Specifically, our findings suggest that marketers should focus more on using herding message in cases of anchors with low attractiveness, compared to those with high attractiveness, given the negative interaction between social cues and the anchor cue.

## 5.3. Limitations and future directions

This study has several limitations. First, given that clothing is the most common product on Taobao Live and that college students are the most typical viewers on the platform, our experiment only considered these settings. Future studies should consider more product types and broader sample groups to generalize the findings and increase external validity. Second, although there remain other aspects that could be accounted for, such as the complexity of the background in the livestreaming video. Future studies are encouraged to explore the effects of these alternative elements. Third, in this experiment, social cues were not perfectly manipulated but natively captured. This issue can be addressed in future research by establishing a strict laboratory environment and using advanced video editing technology. Moreover, in addition to our focus on the effect of selective attention on purchase intention, future investigations can incorporate other mechanisms that influence consumers’ responses in e-commerce livestreaming, including, for instance, the emotional or cognitive changes captured by other neurophysiological tools such as electroencephalography (EEG) and functional magnetic resonance imaging (fMRI). Acknowledgments: The authors thank Professor Qing Xu for her valuable advice on an early version of this paper. Funding: This work was supported by the National Natural Science Foundation of China [grant numbers 71672170, 72002193, 71871199] and the Fundamental

## References

[1] C. Yi, Z.J. Jiang, I. Benbasat, Enticing and engaging consumers via online product presentations: The effects of restricted interaction design, J. Manag. Inf. Syst. 31 (2015) 213–242.

[2] J. Zhou, J. Zhou, Y. Ding, H. Wang, The magic of danmaku: A social interaction perspective of gift sending on live streaming platforms, Electron. Commer. Res. Appl. 34 (2019) 1–9.

[3] T. Ang, S. Wei, N.A. Anaza, Livestreaming vs pre-recorded: How social viewing strategies impact consumers’ viewing experiences and behavioral intentions, Eur. J. Mark. 52 (2018) 2075–2104

[4] F. Hou, Z. Guan, B. Li, A.Y.L. Chong, Factors influencing people’s continuous watching intention and consumption intention in live streaming: Evidence from China, Internet Res. 30 (2020)

141–163.

[5] Z. Jiang, J. Chan, B.C.Y. Tan, W.S. Chua, Effects of interactivity on website involvement and purchase Intention, J. Assoc. Inf. Syst. 11 (2010) 34–59.

[6] M.I. Posner, Orienting of attention, Q. J. Exp. Psychol. 32 (1980) 3–25

[7] S. Yantis, Goal-directed and stimulus-driven determinants of attentional control, Atten. Perform. 18 (2000) 71–103.

[8] J.T. Serences, S. Yantis, Spatially selective representations of voluntary and stimulus-driven attentional priority in human occipital, parietal, and frontal cortex, Cereb. Cortex. 17 (2007) 284–293.

[9] Q. Ye, Z. Cheng, B. Fang, Learning from other buyers: The effect of purchase history records in online marketplaces, Decis. Support Syst. 56 (2013) 502–512.

[10] M. Kukar-Kinney, L. Xia, The effectiveness of number of deals purchased in influencing consumers’ response to daily deal promotions: A cue utilization approach, J. Bus. Res. 79 (2017) 189–197.

[11] K. Windels, J. Heo, Y. Jeong, L. Porter, A.-R. Jung, R. Wang, My friend likes this brand: Do ads with social context attract more attention on social networking sites?, Comput. Human Behav. 84 (2018) 420–429.

[12] M.K.O. Lee, N. Shi, C.M.K. Cheung, K.H. Lim, C.L. Sia, Consumer’s decision to shop online: The

moderating role of positive informational social influence, Inf. Manag. 48 (2011) 185–191.

[13] R.J.K. Jacob, K.S. Karn, Eye tracking in human-computer interaction and usability research, in: The

Mind’s Eye: Cognitive and Applied Aspects of Eye Movement Research, Elsevier Inc., 2003: pp.

531–553.

[14] E. Maslowska, C.M. Segijn, K.A. Vakeel, V. Viswanathan, How consumers attend to online

reviews: An eye-tracking and network analysis approach, Int. J. Advert. 39 (2020) 282–306.

[15] A.D. Miyazaki, D. Grewal, R.C. Goodstein, The effect of multiple extrinsic cues on quality

perceptions: A matter of consistency, J. Consum. Res. 32 (2005) 146–153.

[16] Y. Xu, S. Cai, H.W. Kim, Cue consistency and page value perception: Implications for web-based catalog design, Inf. Manag. 50 (2013) 33–42.

[17] X. Hu, G. Wu, Y. Wu, H. Zhang, The effects of Web assurance seals on consumers’ initial trust in

an online vendor: A functional perspective, Decis. Support Syst. 48 (2010) 407–418.

[18] J.T. Serences, S. Shomstein, A.B. Leber, X. Golay, H.E. Egeth, S. Yantis, Coordination of

voluntary and stimulus-driven attentional control in human cortex, Psychol. Sci. 16 (2005)

114–122.

[19] L. Busse, S. Katzner, S. Treue, Temporal dynamics of neuronal modulation during exogenous and

endogenous shifts of visual attention in macaque area MT, Proc. Natl. Acad. Sci. U. S. A. 105 (2008)

16380–16385.

[20] D. Schreij, S.A. Los, J. Theeuwes, J.T. Enns, C.N.L. Olivers, The interaction between

stimulus-driven and goal-driven orienting as revealed by eye movements, J. Exp. Psychol. Hum.

Percept. Perform. 40 (2014) 378–390.

[21]S.F. Yang, An eye-tracking study of the Elaboration Likelihood Model in online shopping, Electron.

Commer. Res. Appl. 14 (2015) 233–240.

[22] Q. Liu, S. Huang, L. Zhang, The influence of information cascades on online purchase behaviors of

search and experience products, Electron. Commer. Res. 16 (2016) 553–580.

[23] R.M. Raafat, N. Chater, C. Frith, Herding in humans, Trends Cogn. Sci. 13 (2009) 420–428.

[24] A. Mehrabian, J.A. Russell, An Approach to Environmental Psychology, MIT Press,

Cambridge,MA, 1974.

[25] J.C. Wang, C.H. Chang, How online social ties and product-related risks influence purchase

intentions: A Facebook experiment, Electron. Commer. Res. Appl. 12 (2013) 337–346.

[26] Y. Liu, H. Li, F. Hu, Website attributes in urging online impulse purchase: An empirical

investigation on consumer perceptions, Decis. Support Syst. 55 (2013) 829–837.

[27] M. Cortinas, R. Cabeza, R. Chocarro, A. Villanueva, Attention to online channels across the path to

purchase: An eye-tracking study, Electron. Commer. Res. Appl. 36 (2019) 0–1.

[28] H. Zhang, Y. Lu, S. Gupta, L. Zhao, What motivates customers to participate in social commerce? The impact of technological environments and virtual customer experiences, Inf. Manag. 51 (2014) 1017–1030.

[29] S. Kamboj, B. Sarmah, S. Gupta, Y. Dwivedi, Examining branding co-creation in brand communities on social media: Applying the paradigm of Stimulus-Organism-Response, Int. J. Inf. Manage. 39 (2018) 169–185.

[30] T. Friedrich, S. Schlauderer, S. Overhage, The impact of social commerce feature richness on website stickiness through cognitive and affective factors: An experimental study, Electron. Commer. Res. Appl. 36 (2019).

[31] X. Hu, Q. Huang, X. Zhong, R.M. Davison, D. Zhao, The influence of peer characteristics and technical features of a social shopping website on a consumer’s purchase intention, Int. J. Inf. Manage. 36 (2016) 1218–1230.

[32] R.B. Cialdini, N.J. Goldstein, Social influence: Compliance and conformity, Annu. Rev. Psychol. 55 (2004) 591–621.

[33] C.H. Chou, Y.S. Wang, T.I. Tang, Exploring the determinants of knowledge adoption in virtual communities: A social influence perspective, Int. J. Inf. Manage. 35 (2015) 364–376.

[34] T. Hennig-Thurau, G. Walsh, Electronic word-of-mouth: Motives for and consequences of reading

customer articulations on the internet, Int. J. Electron. Commer. 8 (2003) 51–74.

[35] K. Zhao, A.C. Stylianou, Y. Zheng, Sources and impacts of social influence from online anonymous

user reviews, Inf. Manag. 55 (2018) 16–30.

[36] Q. Wang, L. Meng, M. Liu, Q. Wang, Q. Ma, How do social-based cues influence consumers

online purchase decisions? An event-related potential study, Electron. Commer. Res. 16 (2016)

1–26.

[37] J. Lee, D.H. Park, I. Han, The effect of negative online consumer reviews on product attitude: An

information processing view, Electron. Commer. Res. Appl. 7 (2008) 341–352.

[38] T. Daugherty, E. Hoffman, eWOM and the importance of capturing consumer attention within

social media, J. Mark. Commun. 20 (2014) 1-2,82-102.

[39] R. Pieters, M. Wedel, J. Zhang, Optimal feature advertising design under competitive clutter,

Manage. Sci. 53 (2007) 1815–1828.

[40] R. Pieters, M. Wedel, Attention capture and transfer in advertising: Brand, pictorial, and text-size

effects, J. Mark. 68 (2004) 36–50.

[41]R.W. Remington, J.C. Johnston, S. Yantis, Involuntary attentional capture by abrupt onsets, Percept.

Psychophys. 51 (1992) 279–290.

[42]C.L. Folk, R.W. Remington, Bottom-up priming of top-down attentional control settings, Vis. Cogn. 16 (2008) 215–231.

[43] M.Y.M. Cheung, W. Hong, J.Y.L. Thong, Effects of animation on attentional resources of online

consumers, J. Assoc. Inf. Syst. 18 (2017) 605–632.

[44] J. Fang, L. Chen, C. Wen, V.R. Prybutok, Co-viewing experience in video websites: The effect of social presence on e-Loyalty, Int. J. Electron. Commer. 22 (2018) 446–476.

[45] H.J. Müller, P.M.A. Rabbitt, Reflexive and voluntary orienting of visual attention: Time course of

activation and resistance to interruption, J. Exp. Psychol. Hum. Percept. Perform. 15 (1989)

315–330.

[46] D. Cyr, M. Head, H. Larios, B. Pan, Exploring human images in website design: A multi-method approach, MIS Q. 33 (2009) 539–566.

[47]S. Djamasbi, M. Siegel, T. Tullis, Generation Y, web design, and eye tracking, Int. J. Hum. Comput. Stud. 68 (2010) 307–323.

[48] Q. Wang, Y. Yang, Q. Wang, Q. Ma, The effect of human image in B2C website design: An

eye-tracking study, Enterp. Inf. Syst. 8 (2014) 582–605.

[49] C. Valuch, L.S. Pflüger, B. Wallner, B. Laeng, U. Ansorge, Using eye tracking to test for individual differences in attention to attractive faces, Front. Psychol. 6 (2015).

[51]J. Sui, C.H. Liu, Can beauty be ignored? Effects of facial attractiveness on covert attention, Psychon. Bull. Rev. 16 (2009) 276–281.

[50] K. Nakamura, H. Kawabata, Attractive faces temporally modulate visual attention, Front. Psychol. 5 (2014).

[52] L. Bruckert, P. Bestelmeyer, M. Latinus, J. Rouger, I. Charest, G.A. Rousselet, H. Kawahara, P.

Belin, Vocal attractiveness increases by averaging, Curr. Biol. 20 (2010) 116–120.

[53] R. Ohanian, Construction and validation of a scale to measure celebrity endorsers’ perceived expertise, trustworthiness, and attractiveness, J. Advert. 19 (1990) 39–52.

[54] O. Maathuis, J. Rodenburg, D. Sikkel, Credibility, emotion or reason?, Corp. Reput. Rev. 6 (2004) 333–345.

[55] D. Maheswaran, S. Chaiken, Promoting systematic processing in low-motivation settings: Effect of incongruent information on processing and judgment, J. Pers. Soc. Psychol. 61 (1991) 13–25.

[56] W.B. Dodds, K.B. Monroe, D. Grewal, Effects of price, brand, and store information on buyers product evaluations, J. Mark. Res. 28 (1991) 307.

[57] Y. He, H. Oppewal, See how much we’ve sold already! Effects of displaying sales and stock level

information on consumers’ online product choices, J. Retail. 94 (2018) 45–57.

[58] A.B. Chica, J. Lupiáñez, Effects of endogenous and exogenous attention on visual processing: An

Inhibition of Return study, Brain Res. 1278 (2009) 75–85.

[59] I. Krajbich, C. Armel, A. Rangel, Visual fixations and the computation and comparison of value in

simple choice, Nat. Neurosci. 13 (2010) 1292–1298.

[60] R. Pieters, L. Warlop, Visual attention during brand choice: The impact of time pressure and task

motivation, Int. J. Res. Mark. 16 (1999) 1–16.

[61] C. Janiszewski, A. Kuo, N.T. Tavassoli, The influence of selective attention and inattention to

products on subsequent choice, J. Consum. Res. 39 (2013) 1258–1274.

[62] J. Zhang, M. Wedel, R. Pieters, Sales effects of attention to feature advertisements: A Bayesian

mediation analysis, J. Mark. Res. 46 (2009) 669–681.

[63] C.J. Anderson, J. Verkuilen, T.R. Johnson, Applied Generalized Linear Mixed Models: Continuous

and Discrete Data. For the Social and Behavioral Sciences, Springer, New York, 2010.

[64] G. Molenberghs, G. Verbeke, C.G.B. Demétrio, A.M.C. Vieira, A family of generalized linear

models for repeated measures with normal and conjugate random effects, Stat. Sci. 25 (2010)

325–347.

[65] T.F. Jaeger, Categorical data analysis: Away from ANOVAs (transformation or not) and towards

logit mixed models, J. Mem. Lang. 59 (2008) 434–446.

## Credit Author Statement

Mengqi Fei: Conceptualization, Methodology, and Writing - Original Draft. Huizhong Tan:

Software, Investigation, and Data Curation. Xixian Peng: Methodology, Supervision, and

Writing - review & editing. Qiuzhen Wang: Conceptualization, Supervision, and Writing -

Review & Editing. Lei Wang: Supervision and Funding acquisition.

## Highlights

 The eye-tracking study explores role of social cues in e-commerce livestreaming.

 Social cues have capture, distraction and spillover effects on attention.

 Anchor attractiveness attenuates the effects of social cues on attention.

 Endogenous and exogenous attention have different effects on purchase intention.

 Exogenous attention has both negative distraction and positive social influence.
