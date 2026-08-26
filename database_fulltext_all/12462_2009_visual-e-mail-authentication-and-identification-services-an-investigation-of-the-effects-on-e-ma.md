---
otero_id: 12462
otero_key: "JX2BP4Q4"
title: "Visual e-mail authentication and identification services: An investigation of the effects on e-mail use"
authors: "Jingguo Wang; Rui Chen; Tejaswini Herath; H. Raghav Rao"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.06.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visual e-mail authentication and identi<sup>fi</sup>cation services: An investigation of the effects on e-mail use

Jingguo Wang <sup>a,</sup>⁎, Rui Chen <sup>b</sup>, Tejaswini Herath <sup>c</sup>, H. Raghav Rao

<sup>a</sup> Information Systems and Operations Management, College of Business, The University of Texas at Arlington, United States

<sup>b</sup> Information Systems and Operations Management, Miller College of Business, Ball State University, United States

<sup>c</sup> Finance, Operations, and Information Systems, Faculty of Business, Brock University, Canada

<sup>d</sup> Management Science and Systems School of Management, State University of New York at Buffalo, United States

## a r t i c l e i n f o

Article history: Received 4 August 2008 Received in revised form 4 June 2009 Accepted 14 June 2009 Available online 21 June 2009

Keywords: E-mail authentication and identi<sup>fi</sup>cation services Information processing Cognitive effort Decision aids Self-ef<sup>fi</sup>cacy

## a b s t r a c t

E-mail communication has become an essential part of business and individual communication. However, the increase of phishing, spam and other illegitimate e-mails poses severe threats to legitimate e-mail communications. It is therefore important to understand the impact of newly emerging visual e-mail authentication and identi<sup>fi</sup>cation services on shaping individuals' attitudes toward e-mail use. This study explores the research question in the context of a cost–bene<sup>fi</sup>t framework. We <sup>fi</sup>nd that the attitude toward e-mail use is affected positively by perceived e-mail bene<sup>fi</sup>ts and negatively by the cognitive effort expended in identifying relevant and authentic e-mails. Cognitive effort increases with both e-mail load and perceived e-mail risk, and decreases with perceived service usefulness whose effect becomes stronger for those with higher perceived e-mail risk. In addition, the relationship between perceived service usefulness and individuals' self-ef<sup>fi</sup>cacy in identifying authentic and relevant e-mails without technology support follows an inverted u-curve. Implications of the study are discussed.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

E-mail is an important vehicle for organizational and interpersonal communication. According to a Pew February–March 2007 survey [51], 91% of American internet users send or read e-mail. E-mail has, however, become a vector for malware and opened new horizons for crimes [16]. One such example is phishing which is a new form of deception that has appeared over the internet in recent years. The credible appearance of a phishing e-mail makes it hard for recipients to detect its legitimacy and authenticity [10,21,63]. The presence of fraudulent e-mails impacts consumer behavior. A Gartner survey con<sup>fi</sup>rms that “more than 80 percent of U.S. online consumers said their concerns about online attacks have affected their trust in e-mail from companies or individuals. Of these consumers, more than 85 percent delete suspect e-mail without opening it” [43]. Online promotions, giveaways, and other marketing practices have also become less attractive to users [32].

E-mail authentication and identi<sup>fi</sup>cation systems have emerged as new services designed to assist e-mail users in dealing better with these problems. Different from spam <sup>fi</sup>lters that classify e-mails into spam and non-spam using a junk-mail folder, e-mail authentication and identi<sup>fi</sup>cation systems use a trusted third party to promote con<sup>fi</sup>dence in electronic markets [19,44]. An e-mail authentication system veri<sup>fi</sup>es that a message actually originates from a legitimate source for the stated sender. Examples of such systems include DomainKeys by Yahoo! and Gmail, Goodmail Systems (www.goodmailsystems.com), and ICONIX (www.iconix.com). E-AUTHENTICATE<sup>®</sup> (note the company name has been disguised for the purpose of the study and to avoid con<sup>fl</sup>ict of interest), a recent start-up, has become a leading provider of visual e-mail authentication and identi<sup>fi</sup>cation solutions. In order to use the service, users install a piece of client software on their computers. Based on the list of legitimate domains (or the white list) maintained by the service provider, the client software automatically veri<sup>fi</sup>es the authenticity of e-mail senders in real time through the internet when the user checks his/her e-mails. If an email is veri<sup>fi</sup>ed as authentic, a check mark (or the sender's company logo) is shown in the inbox just beside the sender's address to indicate the authenticity of the e-mail. Users can quickly identify e-mails from legitimate senders simply by looking for the check mark next to a message.

E-mail use is a major facet of our professional and personal life, yet it remains an under-researched topic within the information systems discipline [64]. This study attempts to overcome this lacuna in two ways. First, we attempt to understand the factors affecting individuals' attitude toward e-mail use in the context of a cost–bene<sup>fi</sup>t framework given the recent increase in active deceptions (such as phishing) and the large number of irrelevant e-mails (such as spam). We <sup>fi</sup>nd that the attitude toward e-mail use is affected positively by perceived e-mail bene<sup>fi</sup>ts and negatively by the cognitive effort expended in identifying relevant and authentic e-mails. The expended cognitive effort increases with perceived e-mail risk and e-mail load. Second, we examine whether visual e-mail authentication and identi<sup>fi</sup>cation services are effective in assisting users in e-mail assessment. E-mail authentication and identi<sup>fi</sup>cation services are new artifacts developed to battle cyber threats posed through e-mail. Their effectiveness, however, has not yet been examined in prior research. We wonder whether such systems could extend the capabilities of e-mail users and guide them toward better strategies for identifying authentic and relevant e-mails [57]. Interestingly, we <sup>fi</sup>nd that the service indeed directly reduces individuals' cognitive effort in identifying authentic and relevant e-mails, with the effect more apparent for those with higher perceived risk. In addition, we <sup>fi</sup>nd that the relationship between perceived usefulness of the service and self-ef<sup>fi</sup>cacy in identifying e-mails follows an inverted u-curve with the individuals with a medium level of self-ef<sup>fi</sup>cacy perceiving the service as more useful than those with a low or high self-ef<sup>fi</sup>cacy.

In the following section, drawing upon theories on the cognitive process of decision making and decision support systems, we develop a model to understand (a) the factors that shape individuals' attitudes toward e-mail use and (b) the effects of visual e-mail authentication and identi<sup>fi</sup>cation services in assisting individuals in e-mail assessment. The subsequent section describes data collection procedures, survey instrument validation, and model testing using partial least square (PLS) regression. In the last section, we discuss the contributions of this paper.

## 2. Theoretical framework

In this section we lay out the theoretical framework of the research. Figs.1 and 2 summarize the proposed hypotheses as well as the nature of each relationship. Fig. 1 describes that an individual's attitude toward email use is affected positively by the perceived bene<sup>fi</sup>t of using e-mail and negatively by the cognitive effort expended in identifying relevant and authentic e-mails. Cognitive effort increases with both e-mail load and perceived e-mail risk, and decreases with the perceived usefulness of visual e-mail authentication and identi<sup>fi</sup>cation services. The relationship between perceived service usefulness and cognitive effort is positively moderated by e-mail load and perceived risk.

Further, we hypothesize that the relationship between an individual's perceived service usefulness and his/her self-ef<sup>fi</sup>cacy in identifying authentic and relevant e-mails without technology support follows an inverted u-curve (Fig. 2). We describe these hypotheses in more detail in the following subsections.

## 3. Hypotheses development

## 3.1. Attitude toward e-mail use

The theory of reasoned action (TRA) [3] and its later version, the theory of planned behavior (TPB) [1], is a stream of research in social psychology that suggests that an individual's attitude toward a speci<sup>fi</sup>c behavior predicts his/her behavioral intention, and behavioral intention predicts whether the individual will carry out the behavior. The theories provide a parsimonious framework to study the relationships among attitudes, behavioral intentions, and behavior. Researchers in information systems have tried to advance the theoretical speci<sup>fi</sup>cation by testing various predictors of attitude as well as behavioral intention. Examples of such studies include Davis [20] and Venkatesh et al. [62].

Our investigation follows the direction of this literature by specifying a model that focuses on one of the primary components of TRA and TPB models, namely attitude, as our dependent variable. An individual's attitude is his/her feelings of favorableness or unfavorableness toward performing the behavior. Attitude toward the use of a technology was used as a strong predictor for technology acceptance and adoption behavior [20,62]. In this study, we are interested in the attitude toward the general usage of e-mail. We attempt to gain a better understanding of the factors that shape an individual's attitude toward e-mail use in the context of a cost–bene<sup>fi</sup>t framework. We believe an individual's attitude toward e-mail use affects his/her behavioral intention to use it as a channel for communication and information seeking, which, in turn, affects his/ her behavior. Consequently, the effectiveness of e-mail as a promotion and communication channel for business entities will be affected. In other words, if users have unfavorable attitudes toward e-mail use, they will use e-mail less. The channel will also become less effective for promotion and communication because the users are less likely to open e-mails and the promotion e-mails will not reach their targets. Prior studies have shown a strong positive correlation between the attitude toward general e-mail use and the attitude toward e-mail advertisements [42]. Thus we consider that the individuals' attitudes toward e-mail use have implications for the effectiveness of e-mails as a channel for promotion and communication.

![](/api/attachments/JX2BP4Q4/fulltext/images/3e8a3d8820a6b7bf1e6f8b5cc02c98340c2988dc0e713f2a6e07377648450bcf.jpg)  
Fig. 1. Research model and proposed hypotheses.

![](/api/attachments/JX2BP4Q4/fulltext/images/6cf72d2ba811f5fa9e7fb39e3a6c4de4161860a423010cdc1de0f0a6a9c3e21f.jpg)  
Fig. 2. The proposed inverted u-curve between task self-ef<sup>fi</sup>cacy and perceived usefulness of a technology in a technology supported environment

Ajzen [2] asserts that the attitude toward a behavior is formed by the individual's beliefs about the consequences and outcomes of the behavior. An individual who believes that an action will lead to positive results will have a favorable attitude toward the behavior. The bene<sup>fi</sup>ts of using e-mail may include but are not limited to discounted price, time-based offers, new product information, and special events [24,41]. Thus we hypothesize:

H1. Perceived bene<sup>fi</sup>t of using e-mail positively affects attitude toward e-mail use.

## 3.2. Cognitive effort in identifying authentic and relevant e-mails

Perhaps the most-obvious impact of e-mail on our lives is that many of us now spend large amounts of time dealing with the messages we receive [64]. In general, an individual may have two possible courses of action when an e-mail arrives in his/her inbox: opening and reading the e-mail, or ignoring the e-mail (i.e., deleting the e-mail without reading it). When the individual opens and reads an e-mail, there are several possible consequences. In the best scenario, the individual receives some relevant and valuable information in the e-mail (for example, useful coupons, introduction to a new product, or learning about an upcoming event). In other instances, an individual may read a spam containing nothing valuable. In the worst case scenario, the individual may open an e-mail that is carrying malware and fall victim, an action likely to result in identity theft and <sup>fi</sup>nancial loss. By opening and reading the e-mail, at the very least, the individual has to spend time and effort reading and comprehending the e-mail. On the other hand, if to reduce the effort burden the individual chooses not to open the e-mail, he/she may possibly miss valuable information from the message. However, by not opening the e-mail the chance of falling victim to active deceptions is minimized. Thus a sequence of actions of opening and ignoring e-mails realizes the individual's bene<sup>fi</sup>ts of e-mail use.

Expectancy theory [61] holds that individuals behave in ways that maximize positive outcomes and minimize negative outcomes. In order to maximize the bene<sup>fi</sup>ts from e-mails and minimize the potential cost (or loss), individuals may apply an optimized amount of cognitive effort (or thinking cost) to identify authentic e-mails that are of interest (or that are relevant). Cognitive effort, a focal construct in decision making, measures the mental or cognitive aspect of effort expended to reach a decision.

Individuals adapt decision making strategies to speci<sup>fi</sup>c situations and environments to reach conclusions [50]. Decision making strategies are essentially a set of heuristic rules executed by processing information in a mental problem space where meaning is assigned to decision cues (such as the sender name and the message subject in an e-mail) and the relative value of each cue is determined [47]. Individuals choose a decision making strategy by maintaining a balance or making a tradeoff between their cognitive effort, which they wish to minimize, and expected accuracy, which they wish to maximize. The effort–accuracy tradeoff model of decision makers behavior has gained overwhelming support [37,50,58]. According to the concept of effort–accuracy tradeoff, decision makers attempt to make accurate choices [37,50]; and more effort is considered to lead to 0more accurate choices [39]. At the same time, decision makers prefer to minimize their own effort [25], as a consequence willing to accept imperfect accuracy [37].

As cognitive misers, individuals do not enjoy expending effort on decision making. Huppertz et al. [34] <sup>fi</sup>nd a negative relationship between decision effort and the satisfaction. Equity theory [49] has been used to provide explanations regarding the negative relationship between effort and satisfaction. Cardozo [11] also shows that consumers who spend more effort in decision making are less happy with their shopping experiences. Therefore, we hypothesize that:

H2. Cognitive effort in identifying authentic and relevant e-mails negatively affects attitude toward e-mail use.

Because of their limited information processing capacity [45], individuals presented with larger number of e-mails may have excessive information to process and comprehend. Further, information is often valuable only within certain time frames so that one can react to the situation it represents. While some e-mails need to be processed immediately (such as limited time offer that “requires immediate attention” and “instant action”), some others may require substantial amount of time to generate an appropriate response. All these scenarios create information overload for individuals [55]. The burden of heavy information load may affect the individual' ability to set priorities, and make prior information harder to recall [55], and thus it requires additional decision making effort [17].

Individuals apply heuristic rules to each e-mail to identify its relevance and authenticity. One of the problems is simply the number of e-mails that require attention [64]. The larger the number of e-mails received, the greater the cognitive effort that is needed to identify authentic and relevant e-mails. This increase in cognitive effort is due to the need for repeated application of heuristic rules to identify relevance and authenticity. Thus we hypothesize:

H3. An individual's e-mail load positively affects his/her cognitive effort in identifying authentic and relevant e-mails.

One may argue that as the number of e-mails increases, individuals can adjust their decision making strategies. In other words, given the time constraint and the increasing number of e-mails received on each day, an individual may alter his/her making decision strategies with less effort. For example, one may check a fewer number of cues in e-mail assessment [64]. Thus, the total effort devoted to daily e-mail processing would be roughly the same no matter how many e-mails are received, though the accuracy of the decision strategy may decrease. However, active deceptions using e-mail increase the risk of an incorrect decision.

With active e-mail deception, individuals face uncertainty regarding the information provided in e-mails. Successful phishers present highly credible e-mail (and web presence) to their targets, the presentation of which is so realistic that it convinces victims to provide sensitive information. Phishing e-mails manipulate recipients into forming inaccurate mental models of an online interaction [46]. Individuals who rely on simple cues, such as the logos on the message and authentic appearance of the message, can easily be deceived and consequently bear losses resulting from computer viruses, identity theft, and <sup>fi</sup>nancial losses [21]. Such individuals are vulnerable to phishing schemes as they do not have useful strategies for identifying phishing e-mails [23]. In order to detect attacks and minimize the chance of falling victim, individuals need to develop more complex decision rules and use a greater number of cues (such as misspelled words, the formation of sender address and mouse-over URLs, and the presence of an SSL padlock) which are often overlooked by naïve users [23]. Consequently e-mail assessment rules could become more complex with more routes introduced.

Several scams also use e-mail — these include advance-fee scams, lottery scams, auction scams, giveaway e-mail hoaxes, charity hoaxes, and e-card hoaxes. Since the risk of using e-mail is dif<sup>fi</sup>cult to capture as an objective reality, we adopt the notion of perceived risk which is widely used in ecommerce and marketing research. Perceived risk is de<sup>fi</sup>ned as the individual's subjective belief of suffering a loss in the pursuit of a desired outcome [8]. Individuals have personal beliefs regarding the inherent risks involved in every transaction based on the limited information available to them [22,66]. We hypothesize that when he/she has a higher perceived risk of using e-mail, the individual may adopt more complex decision making strategies to identify authentic and relevant e-mails in order to minimize his/her potential loss, and these decision making strategies in turn increase the individual's cognitive effort in email assessment.

H4. Perceived risk of using e-mail is positively related to cognitive effort in identifying authentic and relevant e-mails.

## 3.3. Role of visual e-mail authentication and identification services

One form of coping with highly complex decision environments is to use decision support systems which assist an individual (or a group) in choosing a course of action in non-routine situations that require judgment [38]. The motivating principle of decision support is that a computer-based system performs resource-intensive, but standardized, information processing tasks, thus freeing up some of the human decision processing capacity. The effectiveness of decision support systems has drawn considerable attention from researchers over the last three decades, and mixed results have been found. For a comprehensive review on the studies in decision support systems and their effectiveness, please refer to [27,48].

Recent studies indicate that anti-phishing tools and services are not very effective in protecting against phishing attacks. For instance, Wu et al. [65] reveal that the anti-phishing toolbar's warning messages are not very useful in deterring participants when the fraudulent web pages look highly convincing. Schechter et al. [54] <sup>fi</sup>nd that participants ignore HTTPS indicators and that site-authentication images are ineffective in preventing users from releasing their passwords and account numbers to fraudulent sites.

In this study we examine whether visual e-mail authentication and identi<sup>fi</sup>cation services can effectively help individuals in e-mail assessment. Visual e-mail authentication and identi<sup>fi</sup>cation services are designed to assist an individual in assessing e-mails for validation and authentication. The e-service automatically checks the authenticity of an e-mail when it is presented to the individual in his/her inbox. It assigns a check mark if the mail is authentic by checking the e-mail sender against the white list maintained by the service provider. For those e-mails having a check mark shown, the individual need not go through a number of cues to determine their authenticity. For those e-mails that have not been marked, the individual still need rely on his/her own effort to identify their authenticity. Contingent on the authenticity of an e-mail, the individual may further judge its relevance based on his/her own situation.

The e-service can be considered as a decision aid for e-mail assessment. It may provide enhanced capabilities for the individual; and in turn it may facilitate the activation and engagement of relevant psychological processes [4], alleviating individual cognitive effort in identifying authentic and relevant e-mails. Ceteris paribus, if a decision aid reduces the effort associated with employing a particular strategy relative to other strategies, an individual will be more inclined to employ that strategy [59]. Studies by Todd and Benbasat [59,60] show that decision aids reduce individuals' cognitive effort in decision making.

Perceived usefulness is a construct widely used in the technology acceptance model (see, e.g., [20]). In this study, we de<sup>fi</sup>ne perceived usefulness of the visual e-mail authentication and identi<sup>fi</sup>cation service as the degree to which individuals believe that the e-service will help them assess the authenticity of an e-mail. We postulate that the more an individual perceives the e-service as useful, the more likely he/she will utilize the check mark in his/her e-mail assessment. As a result, the individual can check a fewer number of cues in an e-mail for its authenticity, an action which saves cognitive effort. But if the e-service is perceived as less useful, the reliance on the check mark decreases and the individual may need to expend more effort in examining other e-mail cues to verify authenticity. Thus we hypothesize:

H5. Perceived usefulness of the e-service negatively affects cognitive effort in identifying authentic and relevant e-mails.

Perceived usefulness of the e-service may save more cognitive effort for an individual with a high e-mail load than for one with a low e-mail load. With the check mark, the e-service classi<sup>fi</sup>es e-mails in the inbox into two categories: e-mails with and without a check mark. For those e-mails with a check mark individuals do not need to worry about their authenticity. The classi<sup>fi</sup>cation may not provide much cognitive reduction for an individual with low e-mail load because the total number of e-mails that the individual receives is a handful. But for an individual with a high e-mail load, the classi<sup>fi</sup>cation may provide more cognitive saving because the number of e-mails that now need detailed examination for their authenticity may be just a small fraction of the total e-mail received. Thus, we hypothesize:

H6. An individual's e-mail load positively moderates the relationship between perceived usefulness of the e-service and cognitive effort in identifying authentic and relevant e-mails.

Perceived usefulness of the e-service may also result in different levels of cognitive saving for individuals with different levels of perceived e-mail risk. An individual with a high perceived risk may have a high degree of uncertainty regarding the authenticity of e-mails. Consequently, the individual may examine more cues in an e-mail to remove his/her uncertainty and assure his/herself about the decision than an individual with low perceived risk. With the e-service, individuals may not need to go through so many cues to verify the authenticity of an e-mail. Compared with those with a low perceived risk, individuals with a high perceived risk may bene<sup>fi</sup>t more by doing so. Thus, we hypothesize:

H7. Perceived risk of using e-mail positively moderates the relationship between perceived usefulness of the e-service and cognitive effort in identifying authentic and relevant e-mails.

3.4. Impact of e-mail identification self-efficacy on perceived usefulness of the e-service

Self-ef<sup>fi</sup>cacy refers to humans' beliefs about their ability to perform a task [6]. It in<sup>fl</sup>uences individual motivation to perform a given task [33]. Perceived usefulness re<sup>fl</sup>ects humans' beliefs about whether using a technology will help them perform their jobs better. It is a construct related to outcome judgment [20]. The relationship between self-ef<sup>fi</sup>cacy and perceived usefulness re<sup>fl</sup>ects the effects of selfef<sup>fi</sup>cacy on motivation as well as on outcome judgment [18,35]. We consider that there are two components that de<sup>fi</sup>ne an individual's self-ef<sup>fi</sup>cacy for a task in a computer (or technology) supported environment: computer (or technology) self-ef<sup>fi</sup>cacy, which is the individual's belief in his/her capability to use the technology [18], and task self-ef<sup>fi</sup>cacy, which is the individual's capability to accomplish the task without the support of technology. Computer self-ef<sup>fi</sup>cacy re<sup>fl</sup>ects individual perceptions about his/her ability to apply technology skills to a task (or broader tasks), while task self-ef<sup>fi</sup>cacy concerns individual perceptions about his/her ability to organize and execute a course of action required to attain designated types of performance for a task without the support of technology.

The in<sup>fl</sup>uence of computer self-ef<sup>fi</sup>cacy on perceived usefulness of a computer system or technology has been empirically examined, and mixed results have been found (See, e.g., [13,35,40]). However, the impact of task self-ef<sup>fi</sup>cacy on perceived usefulness of the system or technology which supports the accomplishment of a task has been barely examined. We de<sup>fi</sup>ne e-mail identi<sup>fi</sup>cation self-ef<sup>fi</sup>cacy as an individual's perceptions about his/her ability to identify authentic and relevant e-mails based on simple cues (such as “from” line and “subject” line of an e-mail). We argue that the relationship between e-mail identi<sup>fi</sup>cation self-ef<sup>fi</sup>cacy and perceived usefulness of the e-service follows an inverted u-curve, which can be understood from a perspective of economic incentives for using the e-service [5] as follows.

Perception of ef<sup>fi</sup>cacy to perform a required task is determined by an individual's interactions with and feedback from his/her environment [6]. Such perception affects how much effort the individual will expend on an activity, how long he/she will persevere when confronted with obstacles, and how resilient he/she will be in the face of adverse situations. A low sense of self-ef<sup>fi</sup>cacy leads to less effort, persistence, and resilience. Feelings of low self-ef<sup>fi</sup>cacy can lead an individual to choose an alternative he/she can handle or manage rather than the one that is “best” [56].

In the case of identifying authentic e-mails, low self-ef<sup>fi</sup>cacy could produce ill-conceived e-mail identi<sup>fi</sup>cation strategies. The cost of learning and incorporating the e-service into decision making strategies could be high [26]. Further, low self-ef<sup>fi</sup>cacy results in an insuf<sup>fi</sup>cient understanding of one's external environment and of computer technology. Individuals with low self-ef<sup>fi</sup>cacy may perceive low bene<sup>fi</sup>ts in using the e-service since they tend to underestimate the risks that exist in cyberspace. In other words, the cost of using the e-service may be higher than the bene<sup>fi</sup>t the e-service can bring for these individuals. Thus individuals with low self-ef<sup>fi</sup>cacy may not believe that the e-service will help them assess e-mails, and they will have a low perceived usefulness of the e-service. Individuals with an intermediate level of self-ef<sup>fi</sup>cacy are more aware of their external environment and of computer technology. However, they themselves do not have the ability to develop decision making strategies with a suf<sup>fi</sup>ciently low cognitive effort to identify benign or malicious e-mails. The e-service relieves their effort. Thus they may perceive the e-service as more useful. Individuals with a high level of self-ef<sup>fi</sup>cacy have the ability to develop low cost decision making strategies even without the support of the e-service. Though the cost of using the e-service may be low for them, the net value that the e-service brings may also be low. Consequently, these individuals may believe the e-service will not help them much in assessing the authenticity of e-mails. Thus we propose the following hypothesis (Fig. 2):

H8. The relationship between perceived e-mail identi<sup>fi</sup>cation selfef<sup>fi</sup>cacy and perceived usefulness of the e-service follows an inverted u-curve.

## 4. Research methodology and results

## 4.1. Measurement development

The research hypotheses were empirically tested using data collected through surveys. We constructed an initial set of items by analyzing the literature and re<sup>fl</sup>ecting on the proposed theory. Items for attitude toward e-mail use were adapted from Venkatesh et al. [62]. Items for perceived bene<sup>fi</sup>t of using e-mail were adapted from Ducoffe [24] and Madden [41]. Because there were no existing items that we were able to use to measure individuals' cognitive effort to identify authentic and relevant e-mails, we developed new items based on their de<sup>fi</sup>nitions described above, which are similar to those in Bechwati and Xia [9]. We measured e-mail load based on an individual's subjective perception of the amount of e-mails received per day based on Eppler and Mengis [28]. Items for perceived risk were adapted from Jarvenpaa et al. [36]. Items for perceived service usefulness were based on Davis [20] and Venkatesh et al. [62]. As there were no existing items for e-mail identi<sup>fi</sup>cation self-ef<sup>fi</sup>cacy, we developed items to capture one's judgment about his/her personal capabilities to perform the task ([7], p. 73). The questionnaire was pretested with a group of faculty members and Ph.D. students. One pilot test was administrated to 30 undergraduate students. Necessary changes were made following the pilot test. The <sup>fi</sup>nal version of the items is presented in Appendix A. All items used a 7-point Likert scale.

![](/api/attachments/JX2BP4Q4/fulltext/images/1235f8fc84cd6483c39076b90e154b65fc21f4760612772aacdf82f3aad1e1ac.jpg)  
Fig. 3. E-AUTHENTICATE plug-in client side.

Table 2  
Table 1  
Descriptive statistics, correlations, and average variance extracted (AVE).

<table><tr><td></td><td>Mean (STD)</td><td>Composite reliability</td><td>Cronbach&#x27;s alpha</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1. Attitude</td><td>5.23 (1.21)</td><td>0.88</td><td>0.72</td><td>0.88</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. E-mail benefit</td><td>4.63 (1.28)</td><td>0.92</td><td>0.88</td><td>0.35</td><td>0.86</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Cognitive effort</td><td>3.54 (1.35)</td><td>0.97</td><td>0.97</td><td>-0.30</td><td>-0.16</td><td>0.92</td><td></td><td></td><td></td></tr><tr><td>4. E-mail load</td><td>4.56 (1.41)</td><td>0.90</td><td>0.84</td><td>-0.02</td><td>-0.05</td><td>0.31</td><td>0.87</td><td></td><td></td></tr><tr><td>5. Usefulness</td><td>4.58 (1.32)</td><td>0.96</td><td>0.95</td><td>0.33</td><td>0.36</td><td>-0.09</td><td>0.04</td><td>0.93</td><td></td></tr><tr><td>6. Perceived risk</td><td>4.05 (1.25)</td><td>0.94</td><td>0.92</td><td>-0.08</td><td>0.07</td><td>0.09</td><td>-0.06</td><td>0.09</td><td>0.90</td></tr></table>

Note: The diagonal elements (in bold) represent the square root of AVE.

## 4.2. Survey administration

The study was carried out with undergraduates taking a course titled ‘Introduction to MIS’ at a major university in the northeastern US. The subjects were considered appropriate for the study due to their regular use of e-mail as a communication tool. Since this is a required course for all undergraduates majoring in business administration, the undergraduate students in this class were from a variety of business majors such as marketing, <sup>fi</sup>nance, accounting, HR, operations, and MIS. The fact that the respondents came from diverse backgrounds created an inbuilt heterogeneity. Moreover, since this is one of the <sup>fi</sup>rst IS courses that students have to take, the respondents did not have much exposure to formal IS. Thus they were less likely to have an in-depth understanding of phishing and spam e-mails. The invitations to participate the study were distributed to around 400 students, and participation was voluntary. Students who were willing to participate the study and also use supported e-mail programs (including Yahoo! Mail, Hotmail, Gmail, Earthlink, Outlook Express 6.0) were asked to install the client software of an e-mail authentication and identi<sup>fi</sup>cation service. The e-mail identi<sup>fi</sup>cation and authentication service that was chosen for the study is called E-AUTHENTICATE. E-AUTHENTICATE is a leading e-mail security service and it is free to online users. Users can download a software plugin from the E-AUTHENTICATE website and install it without fees or registration. A screen capture of the E-AUTHENTICATE plug-in at the client side is shown in Fig. 3. The vendor periodically updates the service, and the maintenance does not explicitly involve any user-side interactive activities. E-AUTHENTICATE can be viewed as a supplement to the existing security instruments such as spam <sup>fi</sup>lters: spam <sup>fi</sup>lters remove spam e-mails using a junk-mail folder, and the e-mail authentication and identi<sup>fi</sup>cation service veri<sup>fi</sup>es the true identities of e-mail senders which appear in the inbox using a checkmark.

Two surveys were administered. The <sup>fi</sup>rst survey collected demographic information about the participants at the beginning of the study before introducing the participants to the e-service. After the participants had used the software (e-service) for two months, the second survey was administrated. The second survey included all the items discussed above. Both surveys were conducted online. Extra credit was distributed to those students who used the software and <sup>fi</sup>nished both surveys. Those who did not want to do the survey were given the option of writing up a report on any cyber security issue of their choice for the credit. This resulted in 134 usable responses representing 68 females and 66 males. The average age of the respondents was 21.3 years, ranging from 19 to 50 years. On average the participants had been using computers for about 10 years. 60% respondents subscribed to listservs from which they received e-mails on a regular basis. When asked about online commerce activities for which records of transactions were sent through e-mail, 11.4% respondents mentioned that they participated very often, 67.4% participated sometimes, while 21.2% never participated. When asked about giving out their e-mail addresses to shopping or advertising avenue(s) from which information was sent on regular basis, 8.27% respondents had never done so, while 91.7% had occasionally or often done so. Regarding their level of skills on Internet and e-mail related activities, respondents indicated an average of 5.18 (with a standard deviation of 1.15) for e-mail and 5.50 (with a standard deviation of 1.04) for Internet on a 7-point Likert scale ranging from none to extensive.

Loading and cross-loadings.

<table><tr><td></td><td>Attitude</td><td>E-mail benefit</td><td>Cognitive effort</td><td>E-mail load</td><td>Usefulness</td><td>Perceived risk</td></tr><tr><td>Attitude1</td><td>0.87</td><td>0.25</td><td>-0.29</td><td>0.06</td><td>0.32</td><td>-0.05</td></tr><tr><td>Attitude2</td><td>0.90</td><td>0.37</td><td>-0.24</td><td>-0.08</td><td>0.28</td><td>-0.09</td></tr><tr><td>Benefit1</td><td>0.28</td><td>0.84</td><td>-0.12</td><td>0.04</td><td>0.22</td><td>-0.07</td></tr><tr><td>Benefit2</td><td>0.27</td><td>0.90</td><td>-0.17</td><td>-0.06</td><td>0.35</td><td>0.14</td></tr><tr><td>Benefit3</td><td>0.32</td><td>0.87</td><td>-0.13</td><td>-0.10</td><td>0.36</td><td>0.11</td></tr><tr><td>Benefit4</td><td>0.33</td><td>0.81</td><td>-0.13</td><td>-0.04</td><td>0.32</td><td>0.07</td></tr><tr><td>Effort1</td><td>-0.27</td><td>-0.12</td><td>0.91</td><td>0.31</td><td>-0.15</td><td>0.05</td></tr><tr><td>Effort2</td><td>-0.26</td><td>-0.17</td><td>0.92</td><td>0.21</td><td>-0.07</td><td>0.07</td></tr><tr><td>Effort3</td><td>-0.24</td><td>-0.14</td><td>0.93</td><td>0.24</td><td>-0.10</td><td>0.02</td></tr><tr><td>Effort4</td><td>-0.31</td><td>-0.18</td><td>0.94</td><td>0.31</td><td>-0.07</td><td>0.11</td></tr><tr><td>Effort5</td><td>-0.30</td><td>-0.19</td><td>0.92</td><td>0.29</td><td>-0.04</td><td>0.08</td></tr><tr><td>Effort6</td><td>-0.32</td><td>-0.15</td><td>0.93</td><td>0.31</td><td>-0.04</td><td>0.13</td></tr><tr><td>Effort7</td><td>-0.20</td><td>-0.10</td><td>0.89</td><td>0.30</td><td>-0.09</td><td>0.07</td></tr><tr><td>Load1</td><td>0.04</td><td>-0.01</td><td>0.27</td><td>0.90</td><td>0.07</td><td>-0.01</td></tr><tr><td>Load2</td><td>-0.09</td><td>-0.07</td><td>0.34</td><td>0.95</td><td>0.05</td><td>-0.03</td></tr><tr><td>Load3</td><td>0.04</td><td>-0.06</td><td>0.15</td><td>0.75</td><td>-0.05</td><td>-0.21</td></tr><tr><td>Usefulness1</td><td>0.34</td><td>0.40</td><td>-0.04</td><td>0.08</td><td>0.89</td><td>0.08</td></tr><tr><td>Usefulness2</td><td>0.30</td><td>0.28</td><td>-0.09</td><td>0.03</td><td>0.93</td><td>0.09</td></tr><tr><td>Usefulness3</td><td>0.31</td><td>0.37</td><td>-0.09</td><td>0.06</td><td>0.96</td><td>0.05</td></tr><tr><td>Usefulness4</td><td>0.30</td><td>0.34</td><td>-0.08</td><td>0.00</td><td>0.93</td><td>0.10</td></tr><tr><td>Risk1</td><td>-0.05</td><td>0.11</td><td>0.07</td><td>-0.02</td><td>0.11</td><td>0.87</td></tr><tr><td>Risk2</td><td>-0.01</td><td>0.06</td><td>0.02</td><td>-0.09</td><td>0.08</td><td>0.87</td></tr><tr><td>Risk3</td><td>-0.05</td><td>0.09</td><td>0.08</td><td>-0.09</td><td>0.07</td><td>0.91</td></tr><tr><td>Risk4</td><td>-0.14</td><td>0.03</td><td>0.10</td><td>-0.05</td><td>0.06</td><td>0.93</td></tr></table>

Data set in bold are signi<sup>fi</sup>cant at 0.01.

![](/api/attachments/JX2BP4Q4/fulltext/images/70da74e2c2806c3dd0341304a30a29df41aea7bf9ea561f395a544c73d757b66.jpg)  
Fig. 4. PLS results for the main effects.

## 4.3. Data analysis and results

We tested the measurement model and structural model using partial least squares (PLS). PLS provides the ability to model latent constructs even under conditions of non-normality and small- to medium-size samples [14]. It is best suited for testing complex relationships by avoiding inadmissible solutions and factor indeterminacy. The software employed was smartPLS 2.0 [53]. The bootstrap procedure was used to estimate the signi<sup>fi</sup>cance of the path coef<sup>fi</sup>cients.

## 4.3.1. Measurement validation

Analyses of the measurement model in PLS involve testing construct reliability, convergent validity, and discriminant validity [31]. The descriptive statistics for the constructs are shown in Table 1. The Cronbach's α for all constructs were at or above 0.72, and composite reliabilities were at or above 0.88. These results show that the constructs are internally consistent.

Convergent and discriminant validities were examined using the following four methods. First, the square root of the average variance extracted (AVE) of all constructs is much larger than all other crosscorrelations. Second, all AVEs are well above 0.50, suggesting that the constructs capture much higher construct-related variance than error variance. Third, the correlations among all constructs are very small, suggesting that all constructs are distinct from each other. Fourth, all items loaded highest on their intended constructs with all factor loadings greater than 0.75 (all t-values are signi<sup>fi</sup>cant)

![](/api/attachments/JX2BP4Q4/fulltext/images/70201eadaa8522222d63df0fc31f259328a8bf03c9669a7b77575aa663fea53a.jpg)  
Fig. 5. PLS results for the moderating effects

Model summary and parameter estimates.

<table><tr><td rowspan="2">Model</td><td colspan="2">Unstandardized coefficients</td><td>Standardized coefficients</td><td rowspan="2">t-statistics</td><td rowspan="2">Significance</td></tr><tr><td>b</td><td>Std. error</td><td>β</td></tr><tr><td>(Constant)</td><td>0.03</td><td>0.87</td><td></td><td>0.03</td><td>0.98</td></tr><tr><td>(Self-efficacy)</td><td>1.75</td><td>0.38</td><td>1.77</td><td>4.60</td><td>0.00</td></tr><tr><td> $(Self-efficacy)^2$ </td><td>-0.16</td><td>0.04</td><td>-1.54</td><td>-4.00</td><td>0.00</td></tr></table>

Dependent variable: perceived usefulness.  
Adjusted R<sup>2</sup> = 0.12. F-statistics = 15.88 (p b 0.01).

(Table 2). All these suggest adequate convergent and discriminant validities.

We also performed Harman's one factor test by including all items in a principal components analysis [52]. We did not see evidence of a common method bias as each factor explains roughly equal variance.

## 4.3.2. Testing the structural model

Following Carte and Russell [12], we <sup>fi</sup>rst ran the main effects model without including the interaction terms. Fig. 4 shows the standardized PLS path coef<sup>fi</sup>cients for the main effects model. In PLS, $R ^ { 2 }$ in the endogenous constructs indicates the explanatory power of the model. 19% of the variance in attitude toward e-mail use and 11% of the variance in cognitive effort were explained by the model. The model can be considered a satisfactory and substantive model because the percentages of variance explained were greater than 10% [29].

The results show that the attitude toward e-mail use is determined by the individual's perceived bene<sup>fi</sup>t and cognitive effort of using e-mail. Perceived bene<sup>fi</sup>t has a signi<sup>fi</sup>cant positive impact on attitude toward e-mail use $( \beta = 0 . 3 1 , p { < } 0 . 0 1 )$ , validating H1, and cognitive effort has a signi<sup>fi</sup>cant negative impact $( \beta = - 0 . 2 5 , p \small { < } 0 . 0 1 )$ supporting H2.

When analyzing the relationships between cognitive efforts and its antecedents, both perceived e-mail load $( \beta = 0 . 3 2 , p { < } 0 . 0 1 )$ and perceived risk $( \beta = 0 . 1 2 , ~ p { < } 0 . 0 5 )$ were found to have signi<sup>fi</sup>cant negative impact on cognitive effort, and perceived usefulness of the e-service $( \beta = - 0 . 1 1 , p < 0 . 0 5 )$ has signi<sup>fi</sup>cant negative impact. These results support H3, H4, and H5, respectively

We then tested the moderating effect of perceived e-mail load and perceived risk on the relationship between perceived usefulness and cognitive effort (H6 and H7). The interaction terms were modeled in PLS as products of each item belonging to the underlying scales after standardization as suggested by Chin et al. [15], and then the interaction terms were added to the main effects model in Fig. 4. The results are summarized in Fig. 5.

The coef<sup>fi</sup>cient of the interaction term between perceived usefulness and perceived e-mail load $( \beta = - 0 . 0 8 , \Delta R ^ { 2 } = 0 . 0 1 )$ with a t-statistics of 1.51 is not signi<sup>fi</sup>cant at the level of 0.05. We do not have suf<sup>fi</sup>cient evidence to support H6. The coef<sup>fi</sup>cient of the interaction term between perceived usefulness and perceived risk $( \beta = - 0 . 2 1 , \ \Delta R ^ { 2 } = 0 . 0 5 )$ is signi<sup>fi</sup>cant at the level of 0.01, supporting H7.

We also tested the moderating effect of perceived risk on the relationship between perceived usefulness and cognitive effort following Carte and Russell [12]. We examined whether the variance explained by the moderating effect is signi<sup>fi</sup>cant beyond the main effects using the following F-statistic:

$$
\begin{array}{l} F (d f _ {\text {interaction}} - d f _ {\text {main}}, N - d f _ {\text {interaction}} - 1) \\ = \frac {\Delta R ^ {2} / (d f _ {\text {interaction}} - d f _ {\text {main}})}{(1 - R _ {\text {interaction}} ^ {2}) / (N - d f _ {\text {interaction}} - 1)}. \end{array}
$$

The F-statistics for the moderating effect was $7 . 7 7 \ ( p { < } 0 . 0 1 )$ , thereby also supporting the signi<sup>fi</sup>cant role of the proposed moderating effect of perceived risk on the relationship between perceived usefulness and cognitive effort.

We further validated the moderating effect using Cohen' $; f ^ { 2 }$ which compares the $R ^ { 2 }$ value of the interaction effect over the main effect with the following equation [15]:

$$
f ^ {2} = (R _ {\text { interaction }} ^ {2} - R _ {\text { main }} ^ {2}) / (1 - R _ {\text { main }} ^ {2}).
$$

Cohen's $f ^ { 2 }$ for the interaction between perceived usefulness and perceived risk is 0.06, which shows a medium effect [15].

To summarize, the results validate the moderating role of perceived risk on the relationship between perceived usefulness of the e-service and cognitive effort (H7), but they fail to support the moderating role of e-mail load on the relationship between perceived usefulness and cognitive effort (H6).

E-mail identi<sup>fi</sup>cation self-ef<sup>fi</sup>cacy was measured by eight items as shown in Appendix A. The loading of all items were above 0.86. Both Cronbach's α and composition reliability for the construct are above 0.95. We <sup>fi</sup>tted a quadratic model relating perceived usefulness to e-mail identi<sup>fi</sup>cation self-ef<sup>fi</sup>cacy, that is:

$$
\text { perceived   usefulness } = \beta_ {1} + \beta_ {2} (\text { self - efficacy }) + \beta_ {3} (\text { self - efficacy }) ^ {2}.
$$

Table 3 presents the regression results. As expected, there is an inverted u-curve relationship between an individual's self-ef<sup>fi</sup>cacy and his/her perceived usefulness of the e-service, supporting H8.

## 5. Discussion

The primary goal of this paper is to develop and empirically test what affects individuals' attitudes toward e-mail use given the recent increase in active deceptions (such as phishing) and a large number of irrelevant e-mails (such as spam), and whether visual e-mail identi<sup>fi</sup>cation services are an effective way to assist users in e-mail processing.

## 5.1. Contribution to theory

The results of our study make important theoretical contributions to studies in e-mail and e-mail authentication services. First, our results show that individuals' attitudes toward e-mail use are affected positively by bene<sup>fi</sup>ts brought by using e-mail and negatively by cognitive effort in identifying relevant and authentic e-mails. Both e-mail load and perceived e-mail risk positively affect cognitive effort in e-mail assessment. Echoing prior <sup>fi</sup>ndings [30,32,43], our results indicate that active deceptions and irrelevant e-mails affect the effectiveness of e-mail as a promotion and communication channel for business entities partly because the cognitive effort now needed to identify relevant and authentic e-mails increases.

Second, as a decision aid, visual e-mail authentication and identi<sup>fi</sup>cation service directly reduces individuals' cognitive effort. Individuals with high perceived risk bene<sup>fi</sup>t more from using the e-service than those with low perceived risk. Our results suggest that visual e-mail authentication and identi<sup>fi</sup>cation services alter individuals' e-mail assessment strategies. The decision aid frees up some of decision processing capacity and saves cognitive effort in e-mail assessment. It is an effective way to improve individuals e-mail processing.

Interestingly, we <sup>fi</sup>nd that the relationship between an individual's perceived usefulness of the e-service and his/her self-ef<sup>fi</sup>cacy of identifying authentic and relevant e-mails without technology support can be represented by an inverted u-curve. Individuals with a medium level of self-ef<sup>fi</sup>cacy perceive the e-service as more useful than those with a low or high self-ef<sup>fi</sup>cacy. We can further explore the relationship between computer self-ef<sup>fi</sup>cacy and task self-ef<sup>fi</sup>cacy, and test the roles of these two factors in determining perceived usefulness of a technology. Such a study may explain the inconsistent <sup>fi</sup>ndings in the relationship between computer self-ef<sup>fi</sup>cacy and perceived usefulness of a computer system.

## 5.2. Implications for practice

E-mail has served as an effective and ef<sup>fi</sup>cient marketing channel for years; however, its sustainable advantage has increasingly been threatened by the presence of cyber security risks. To promote and continue the success of e-mail marketing in the long-run, our <sup>fi</sup>ndings point out a few directions for improved practice.

First, e-mail marketers should strive to increase the user perceptions about the values of commercial e-mails. Online consumers value e-mails that carry timely and accurate information on new products, sales, and coupons. Due to the fact that consumers vary in their purchase interest, they may appreciate and undervalue information in a different manner. Personalization systems have been increasingly used to model consumer pro<sup>fi</sup>les and purchasing behaviors. E-mail marketers may use these personalization systems to better understand the targeted customers and compose commercial e-mails that cater to the special interests of individual consumers or groups. For example, e-mails may highlight sales on outdoor products for a person who likes jogging.

Second, the involvement of e-mail marketers in combating cyber security threats is encouraged. On one hand, these marketers may help lower the consumers' Internet risk perceptions through patronage of safe computing workshops, webcasts, and other educational campaigns. On the other hand, e-mail marketers may partner with e-mail security vendors to develop new technical instruments that offer higher safety and security to the consumers. Evidenced by the case of E-AUTHENTICATE, online users bene<sup>fi</sup>t from e-mail security systems. They are likely to hold more positive attitudes toward commercial e-mails given better security systems in place. Thus it is bene<sup>fi</sup>cial for those <sup>fi</sup>rms that wish to use e-mail as a marketing channel to join the white list of the E-AUTHENTICATE service.

Further, in the context of the design of the E-AUTHENTICATE service we do not <sup>fi</sup>nd that there is a signi<sup>fi</sup>cant moderating effect of e-mail load on the relationship between perceived usefulness and cognitive effort though the sign of the interaction term is as expected. The tool does not result in signi<sup>fi</sup>cantly more cognitive reduction for those with high e-mail load than for those with a low e-mail load. One way that may bring more bene<sup>fi</sup>ts to those with high e-mail load is to mark e-mails with more categories instead of two. For example, we may maintain both a white list and a black list, and also utilize e-mail domains' reputation scores which are calculated based on e-mail behaviors of the domains (see, e.g., Sender Score by Return Path, Inc.; SenderBase Reputation Score by IronPort Systems, Inc; SenderIndex by Habeas Inc.). For those e-mails from a sender on the black list, we may show classes: “authentic, suspected bad”. For those senders on the white list, based on their reputation score, we may have classes of “authentic and with a good reputation”, “authentic but has a bad reputation”, and “authentic, but there's no reputation info available”. For the rest of the e-mails, we may have a class of “unauthentic, and no other indication is available to differentiate the message”. In such a way, each category would have relative small number of e-mails, and it may bring more bene<sup>fi</sup>ts for those with a high e-mail load.

## 5.3. Limitation and future research

In this study, we have investigated the formation of attitudes toward e-mail use and the effects of newly emerged visual e-mail authentication and identi<sup>fi</sup>cation services in the context of a cost– bene<sup>fi</sup>t framework. Following TRA and TPB model, future research should further empirically establish the relationship between the attitude toward e-mail use and the actual use of e-mail for information solicitation.

This study is a survey-based research using college students as research subjects and the <sup>fi</sup>ndings are subject to the homogenous group problem. Compared with the general population, college students might be more pro<sup>fi</sup>cient in using e-mail and combating cyber attacks such as phishing. Future research could employ more representative samples and examine populations other than university students (for example, general Internet/computer users) so that the external validity of the results can be improved. In addition, <sup>fi</sup>eld-observed data and behavioral logs could be utilized to overcome the limitation of survey-based method.

E-AUTHENTICATE utilizes domain keys to verify the identities of e-mails. Currently more than 1500 popular online vendors (e.g., news, retailing, bank <sup>fi</sup>rms) have registered their domain keys with this e-mail security service. The fact that E-AUTHENTICATE protects a subset of all the commercial e-mails might impact user perceptions of service usefulness and the strength of the relationships among theoretical variables. Future research could retest the research model with other e-mail security services.

The bene<sup>fi</sup>ts of e-mail use considered in this study are mainly provided by commercial e-mails. But the bene<sup>fi</sup>ts can also include increasing the communication with key family and friends and enhancing the connection to them [41], which are resulted by private e-mails. Cognitive effort considered in this study is the cost of processing all the e-mails. If the effort involved in only processing the commercial e-mails can be isolated, perhaps the effects of the e-service could be more salient.

Furthermore, the dependent variable considered in this study is one's attitude towards e-mail use. How individuals behave or deal with the e-mails, i.e., whether they open the e-mails that are not authenticated, and whether they respond to e-mails that are authenticated more positively, needs to be studied in the future. For the next step of the study, we will collect behavioral data through logs and observe the open rate of authenticated and unauthenticated e-mails to further evaluate the effectiveness of the e-mail authentication service.

This study has investigated the effects of e-mail authentication and identi<sup>fi</sup>cation services. However, what affects individuals' intention of adopting the service needs to be examined in a separate study. In order to use the e-service, the individual needs to install a piece of client software that allows access to his/her inbox which can be considered intrusive. We contemplate that individuals' privacy concerns are likely to affect his/her intention to use the software. Furthermore, the e-service is designed to be used by the general public rather than by organizational users. The use of such services is personal and voluntary rather than organizational and mandatory. The motives to adopt the e-service need to be further explored.

## Acknowledgements

The authors would like to thank K. Banjara and J. Wilbur for helping setup the study. The authors also thank the editor and the two referees for their comments, which have considerably improved the lucidity of this research. The research of the fourth author is also supported in part by NSF under grant #0809186.The usual disclaimer applies.

Appendix A. Questionnaire items

<table><tr><td colspan="2">Attitude Toward E-mail Use</td><td colspan="4">Good Idea</td><td colspan="3">Bad Idea</td></tr><tr><td rowspan="2">Attitude1</td><td rowspan="2">All things considered, using e-mail is:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="4">Extremely Bad</td><td colspan="3">Extremely Good</td></tr><tr><td>Attitude2</td><td>All things considered, using e-mail is:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="2">Perceived benefit of using e-mail</td><td colspan="4">Strongly Disagree</td><td colspan="3">Strongly Agree</td></tr><tr><td>Benefit1</td><td>E-mails provide me with the benefit of information about new products:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Benefit2</td><td>E-mails provide me with the benefit of special sales offerings:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Benefit3</td><td>E-mails provide me with the benefit of coupons or special discounts:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Benefit4</td><td>E-mails provide me with the benefit of information about different upcoming events:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="2">Cognitive Effort</td><td colspan="4">Strongly Disagree</td><td colspan="3">Strongly Agree</td></tr><tr><td>Effort1</td><td>Everyday, it takes me considerable effort to verify whether new e-mails are coming from authentic senders.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Effort2</td><td>I spend considerable amount of time daily to verify whether e-mails are coming from authentic senders.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Effort3</td><td>Everyday, I take considerable effort to verify whether incoming e-mails are forged or not.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Effort4</td><td>It takes me considerable amount of time everyday to verify whether the identities of incoming e-mails are real.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Effort5</td><td>Everyday, it takes considerable effort for me to be certain whether the new e-mails are genuine.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Effort6</td><td>Everyday, I take considerable effort to scan for the incoming e-mails that are relevant to me.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Effort7</td><td>It takes me considerable effort to screen for e-mails of interest everyday.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="2">E-mail Load</td><td colspan="4">Strongly Disagree</td><td colspan="3">Strongly Agree</td></tr><tr><td>Load1</td><td>I receive a considerable amount of e-mails every day.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Load2</td><td>I think the daily e-mail load I receive is high.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Load3</td><td>I think the daily e-mail load I receive is low.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="2">Perceived Usefulness of the e-Service</td><td colspan="4">Strongly Disagree</td><td colspan="3">Strongly Agree</td></tr><tr><td>Usefulness1</td><td>Using E-AUTHENTICATE service enables me to accomplish the task of e-mail authenticity check more quickly.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Usefulness2</td><td>Using E-AUTHENTICATE service helps improve identifying authentic e-mails.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Usefulness3</td><td>Using E-AUTHENTICATE service enhances my effectiveness of detecting authentic e-mails</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Usefulness4</td><td>Using E-AUTHENTICATE service gives me greater control over e-mail authenticity check.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="2">Perceived Risk</td><td colspan="4">Strongly Disagree</td><td colspan="3">Strongly Agree</td></tr><tr><td>Risk1</td><td>There is a high potential for loss involved by opening e-mails.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Risk2</td><td>Opening e-mail will lead to high potential for loss.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Risk3</td><td>There is considerable risk involved in potential consequence of opening e-mails.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Risk4</td><td>Opening e-mails will lead to considerable risks.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="2">E-mail Assessment Self-efficacy</td><td colspan="4">Strongly Disagree</td><td colspan="3">Strongly Agree</td></tr><tr><td>Efficacy1</td><td>It is easy for me to verify an e-mail as coming from authentic sender based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Efficacy2</td><td>I feel comfortable in my abilities to identify e-mails that may be forged based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Efficacy3</td><td>I feel confident in my abilities to identify e-mails that are authentic based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Efficacy4</td><td>I feel confident in my abilities to determine whether the identities of e-mails are real based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Efficacy5</td><td>I feel comfortable in my abilities to identify e-mails that may be useful to me based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Efficacy6</td><td>I feel confident in my abilities to identify e-mails that are relevant to me based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Efficacy7</td><td>I feel confident in my abilities to identify malicious e-mails, such as phishing e-mails, based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Efficacy8</td><td>I feel confident in my abilities to identify e-mails that are detrimental based on “from line” and “subject line”.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr></table>

## References

[1] I. Ajzen, Attitudes, Personality, and Behavior, Dorsey Press, Chicago, IL, 1988.

[2] I. Ajzen, The theory of planned behavior, Organizational Behavior and Human Decision Processes 50 (2) (1991).

[3] I. Ajzen, M. Fishbein, Understanding Attitudes and Predicting Social Behavior, Prentice-Hall, Englewood Cliffs, NJ, 1980.

[4] M. Alavi, D.E. Leidner, Research commentary: technology-mediated learning—a call for greater depth and breadth of research, Information Systems Research 12 (1) (2001).

[5] S. Ba, A.B. Whinston, H. Zhang, Building trust in online auction markets through an economic incentive mechanism, Decision Support Systems 35 (3) (2003).

[6] A. Bandura, Self-ef<sup>fi</sup>cacy: toward a unifying theory of behavioral change, Psychological Review 84 (2) (1977).

[7] A. Bandura, Self-ef<sup>fi</sup>cacy: the Exercise of Control, W. H. Freeman, New York, 1997.

[8] R.A. Bauer, Consumer behavior as risk taking, in: D.F. Cox (Ed.), Risk Taking and Information Handling in Consumer Behavior, Harvard University Press, Cambridge, MA, 1960.

[9] N.N. Bechwati, L. Xia, Do computers sweat? The impact of perceived effort of online decision aids on consumers' satisfaction with the decision process, Journal of Consumer Psychology 13 (1&2) (2003).

[10] I. Bose, A.C.M. Leung, Assessing anti-phishing preparedness: a study of online banks in Hong Kong, Decision Support Systems 45 (4) (2008).

[11] R.N. Cardozo, An experimental study of customer effort, expectation, and satisfaction, Journal of Marketing Research 2 (1965).

[12] T. Carte, C. Russell, In pursuit of moderation: nine common errors and their solutions, MIS Quarterly 27 (3) (2003).

[13] P.Y.K. Chau, In<sup>fl</sup>uence of computer attitude and self-ef<sup>fi</sup>cacy on IT usage behavior, Journal of End User Computing 13 (1) (2001).

[14] W.W. Chin, The partial least squares approach for structural equation modeling, in: G.A. Marcoulides (Ed.) Modem Methods for Business Research Lawrence Erlbaum Mahwah NI 1998

[15] W.W. Chin, B.L. Marcolin, P.R. Newsted, A partial least squares latent variable modeling approach for measuring interaction effects: results from a Monte Carlo simulation study and an electronic mail adoption study, Information Systems Research 14 (2) (2003).

[16] W. Chung, H. Chen, W. Chang, S. Chou, Fighting cybercrime: a review and the Taiwan experience, Decision Support Systems 41 (3) (2006).

[17] S. Cohen, Aftereffects of stress on human performance and social behavior: a review of research and theory. Psychological Bulletin 88 (1980).

[18] D.R. Compeau, C.A. Higgins, Computer self-ef<sup>fi</sup>cacy: development of a measure and initial test, MIS Ouarterly 19 (2) (1995)

[19] D. Crocker, Trust in Email Begins with Authentication, Messaging Anti-Abuse Working Group, 2008.

[20] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989).

[21] R. Dhamija, J.D. Tygar, M. Hearst, Why phishing works, Proceedings of Conference on Human Factors in Computing Systems (CHI2006) (Quebec, Canada), 2006

[22] G.R. Dowling, R. Staelin, A model of perceived risk and intended risk-handling activity, Journal of Consumer Research 21 (1) (1994).

[23] J.S. Downs, M.B. Holbrook, L.F. Cranor, Decision strategies and susceptibility to phishing, Proceedings of Symposium on Usable Privacy and Security (SOUPS), Pittsburgh, PA, USA, 2006.

[24] R.H. Ducoffe, Advertising value and advertising on the web, Journal of Advertising Research (1996) (No. September/October).

[25] H.J. Eihorn, R.M. Hogarth, Behavioral decision theory: processes of judgment and choice, Annual Review of Psychology 32 (1981).

[26] P.S. Ellen, W.O. Bearden, S. Sharma, Resistance to technological innovations: an examination of the role of self-ef<sup>fi</sup>cacy and performance satisfaction, Journal of the Academy of Marketing Science 19 (4) (1991).

[27] S.B. Eom, Mapping the intellectual structure of research in decision support systems through author cocitation analysis (1971–1993), Decision Support Systems 16 (4) (1996).

[28] M.J. Eppler, J. Mengis, The concept of information overload: a review of literature from organization science, accounting, marketing, MIS, and related disciplines, The Information Society 20 (2004).

[29] R.F. Falk, N.B. Miller, A Primer for Soft Modeling, University of Akron Press, Akron, OH, 1992.

[30] D. Fallows, Internet users and spam: what the attitudes and behavior of Internet users can tell us about <sup>fi</sup>ghting spam, Proceedings of First Conference on Email and Anti-Spam (CEAS) Mountain View, CA, 2004.

[31] C. Fornell, D.F. Larcker, Structural equation models with unobservable variables and measurement errors, Journal of Marketing Research 18 (1) (1981).

[32] FST, making email effective again, Financial Services Technology (US Edition), GDS Publishing, 2008.

[33] M.E. Gist, The in<sup>fl</sup>uence of training method on self-ef<sup>fi</sup>cacy and idea generation among managers, Personnel Psychology 42 (4) (1989).

[34] J.W. Huppertz, S.J. Arenson, R.H. Evans, An application of equity theory to buyer– seller exchange situations, Journal of Marketing Research 15 (2) (1978).

[35] M. Igbaria, J. Iivari, The effects of self-ef<sup>fi</sup>cacy on computer usage, Omega 23 (6) (1995).

[36] S.L. Jarvenpaa, N. Tractinsky, M. Vitale, Consumer trust in an Internet store, Information Technology and Management 1 (12) (1999).

[37] E.J. Johnson, J.W. Payne, Effort and accuracy in choice, Management Science 31 (4) (1985).

[38] G.M. Kasper, A theory of decision support system design for user calibration, Information Systems Research 7 (2) (1996).

[39] N.M. Klein, M.S. Yadav, Context effects on effort and accuracy in choice: an enquiry into adaptive decision making, Journal of Consumer Research 15 (4) (1989).

[40] D.A. Lopez, D.P. Manson, A study of individual computer self-ef<sup>fi</sup>cacy and perceived usefulness of the empowered desktop information system, Journal of Interdisciplinary Studies 10 (1997).

[41] M. Madden, America's Online Pursuits, Pew Internet & American Life Project, 2003.

[42] C.P. Maneesoonthorn, An Empirical Examination of the Effects of Permission, Interactivity, Vividness and Personalization on Consumer Attitudes toward E-Mail Marketing, University of Canterbury, 2006.

[43] T. McCall, R. Moss, Gartner Survey Shows Frequent Data Security Lapses and Increased Cyber Attacks Damage Consumer Trust in Online Commerce, Gartner Inc., Stamford, Conn, 2005.

[44] E. Messmer, Ebay's Paypal Uses E-Mail Authentication to Combat Fraud, Network World, 2008.

[45] G.A. Miller, The magic number seven, plus or minus two: some limits on our capacity for processing information, The Psychological Review 63 (2) (1956).

[46] R. Miller, M. Wu, Fighting phishing at the user interface, in: Lorrie Cranor, Simson Gar<sup>fi</sup>nkel (Eds.), Security and Usability: Designing Secure Systems that People can Use, O'Reilly Media, Portland, OR, 2005.

[47] A. Newell, H. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

[48] E. O'Donnell, J.S. David, How information systems in<sup>fl</sup>uence user decisions: a research framework and literature review, International Journal of Accounting Information Systems 1 (3) (2000).

[49] R.L. Oliver, J.E. Swan, Consumer perceptions of interpersonal equity and satisfaction in transaction: a <sup>fi</sup>eld survey approach, Journal of Marketing 53 (2) (1989).

[50] J.W. Payne, Contingent decision behavior, Psychological Bulletin 92 (2) (1982).

[51] Pew, February 15–March 7 2007 Tracking Survey, Pew Internet & American Life Project, 2007.

[52] P.M. Podsakoff, S.B. MacKenzie, J.-Y. Lee, N.P. Podsakoff, Common method biases in behavioral research: a critical review of the literature and recommended remedies, Journal of Applied Psychology 88 (5) (2003).

[53] C.M. Ringle, S. Wende, S. Will, Smartpls 2.0 (M3) Beta, http://www.smartpls.de, 2005.

[54] S.E. Schechter, R. Dhamija, A. Ozment, I. Fischer, The Emperor's new security indicators, Proceedings of the 2007 IEEE Symposium on Security and Privacy, IEEE, Oakland, California, 2007.

[55] A.G. Schick, L.A. Gordon, S. Haka, Information overload: a temporal approach, Accounting, Organizations and Society 15 (3) (1990).

[56] L.F. Seltzer, In<sup>fl</sup>uencing the ‘shape’ of resistance: an experimental exploration of paradoxical directives and psychological reactance, Basic and Applied Social Psychology 4 (1) (1983).

[57] M.S. Silver, Descriptive analysis for computer-based decision support, Operations Research 36 (6) (1998).

[58] P. Todd, I. Benbasat, Inducing compensatory information processing through decision aids that facilitate effort reduction: an experimental assessment, Journal of Behavioral Decision Making 13 (1) (2000).

[59] P.A. Todd, I. Benbasat, The in<sup>fl</sup>uence of decision aids on choice strategies under conditions of high cognitive load, 4IEEE Transactions on Systems, Man, and Cybernetics 24 (1994).

[60] P.A. Todd, I. Benbasat, The in<sup>fl</sup>uence of decision aids on choice strategies: an experimental analysis of the role of cognitive effort, Organizational Behavior and Human Decision Processes 60 (1) (1994).

[61] W. van Eerde, H. Thierry, Vroom's expectancy models and work-related criteria: a meta-analysis, Journal of Applied Psychology 81 (5) (1996).

[62] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a uni<sup>fi</sup>ed view, MIS Quarterly 27 (3) (2003).

[63] J. Wang, R. Chen, T. Herath, H.R. Rao, An exploration of the design features of phishing attacks, in: H.R. Rao, S. Upadhyaya (Eds.), Annals of Emerging Research in IA, Security and Privacy Services, Elsevier, New York, NY, 2009.

[64] R. Weber, The grim reaper: the curse of e-mail, MIS Quarterly 28 (3) (2004).

[65] M. Wu, R.C. Miller, S. Gar<sup>fi</sup>nkel, Do security toolbars actually prevent phishing attacks? Proceedings of Human Factors in Computing Systems (CHI 2006), (Quebec, Canada), 2006.

[66] H. Zhang, H. Li, Factors affecting payment choices in online auctions: a study of eBay traders, Decision Support Systems 42 (2) (2006).

Jingguo Wang is an Assistant Professor of Information Systems. He graduated from SUNY Buffalo. His work has been published in Information Systems Research, IEEE Transactions on Systems, Man, and Cybernetics (Part C), European Journal of Operational Research, Decision Support Systems, and other journals, and received best paper awards at AMCIS and the International Conference on Internet Monitoring and Protection. His current research interests are in the areas of cybercrime and information security, information search, and decision making

Rui Chen is an Assistant Professor of Information Systems, and earned his Ph.D. from SuNY Buffalo. His research interests are in the areas of information assurance emergency management, coordination and collaboration, and information technology outsourcing, Some of his publications have appeared in the Journal of the AIS. Communications of the ACM, Decision Support Systems, and other journals. He is also a Microsoft Certi<sup>fi</sup>ed System Administrator (MCSE) and Database Administrator (MCDBA).

Tejaswini Herath graduated from SUNY Buffalo and is an Assistant Professor of Information Systems at Brock University, Canada. Her research interests are in information assurance and include topics such as information security and privacy, diffusion of information assurance practices, economics of information security and risk management. Her work has been published in the Journal of Management Information Systems, Decision Support Systems, European Journal of Information Systems, Information Systems Management and International Journal of E-Government Research. In addition she has presented papers at leading conferences and contributed several book chapters.

H.R. Rao (MIS, SUNY at Buffalo) graduated from Purdue. He has edited four books including “Information Assurance in Financial Services (Idea Group, 2007)”. He has authored or co-authored more than 150 technical papers, and has received best paper and best paper runner up awards at AMCIS and ICIS. He has received research funding from NSF and DoD. He was a Fulbright fellow in 2004. He is the recipient of the 2007 SuNY Chancellor's award for excellence
