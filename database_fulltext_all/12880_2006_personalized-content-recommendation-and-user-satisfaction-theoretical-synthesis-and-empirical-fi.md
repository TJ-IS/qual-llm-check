---
otero_id: 12880
otero_key: "PEFCEYKE"
title: "Personalized Content Recommendation and User Satisfaction: Theoretical Synthesis and Empirical Findings"
authors: "Ting-Peng Liang; Hung-Jen Lai; Yi-Cheng Ku"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222230303"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Personalized Content Recommendation and User Satisfaction: Theoretical Synthesis and Empirical Findings

TING-PENG LIANG, HUNG-JEN LAI, AND YI-CHENG KU

TING-PENG LIANG is National Chair Professor in Information Systems and Director of the Electronic Commerce Research Center of National Sun Yat-sen University in Taiwan. He received his Ph.D. from the Wharton School of the University of Pennsylvania. Prior to joining his current university in 1993, he taught at the University of Illinois and Purdue University. At National Sun Yat-sen University, he has served as the Dean of the College of Management (1994–97) and University Provost (1999–2002). His research has been published in Journal of Management Information Systems, MIS Quarterly, Management Science, Operations Research, Decision Support Systems, Information and Management, and many other academic journals. Professor Liang’s primary research interests include electronic commerce, knowledge management, intelligent systems, and strategic applications of information systems. He has served on the editorial boards of several journals, including Decision Support Systems, International Journal of Electronic Commerce, Industrial Management and Data Systems, and Electronic Commerce Research and Applications, among others. He is a fellow of the AIS and a member of ACM, INFORMS, and IEEE Computer Society.

HUNG-JEN LAI is an Assistant Professor in the Department of Information Management at the Naval Academy, R.O.C., Kaohsiung, Taiwan. He received his Ph.D. from National Sun Yat-sen University. He is a recipient of the Outstanding Teacher Award from the Naval Academy, R.O.C. His master’s thesis received the Long-Term Thesis Award from Acer Company. Professor Lai’s research interests include electronic commerce, knowledge management, intelligent systems, and medical information systems. His works have been published in several proceedings such as Hawaii International Conference on System Sciences and journals such as Information & Management.

YI-CHENG KU is an Assistant Professor in the Department of Computer Science and Information Management, Providence University, Taiwan. He received his Ph.D. in Information Management from National Sun Yat-sen University. His research interests include recommendation systems, innovation adoption and diffusion, and knowledge management. His papers have been published in Decision Support Systems, Electronic Commerce Research, and various conference proceedings.

ABSTRACT: Personalized services are increasingly popular in the Internet world. This study identifies theories related to the use of personalized content services and their effect on user satisfaction. Three major theories have been identified—information overload, uses and gratifications, and user involvement. The information overload theory implies that user satisfaction increases when the recommended content fits user interests (i.e., the recommendation accuracy increases). The uses and gratifications theory indicates that motivations for information access affect user satisfaction. The user involvement theory implies that users prefer content recommended by a process in which they have explicit involvement. In this research, a research model was proposed to integrate these theories and two experiments were conducted to examine the theoretical relationships. Our findings indicate that information overload and uses and gratifications are two major theories for explaining user satisfaction with personalized services. Personalized services can reduce information overload and, hence, increase user satisfaction, but their effects may be moderated by the motivation for information access. The effect is stronger for users whose motivation is in searching for a specific target. This implies that content recommendation would be more useful for knowledge management systems, where users are often looking for specific knowledge, rather than for general purpose Web sites, whose customers often come for scanning. Explicit user involvement in the personalization process may affect a user’s perception of customization, but has no significant effect on overall satisfaction.

KEY WORDS AND PHRASES: content recommendation, personalization, recommendation systems, user satisfaction.

THE RAPID PROPAGATION OF THE INTERNET, along with the evolution of information technologies (IT), has changed the way firms are adapting to changing customer needs. For physical products (e.g., computers and televisions), mass customization and fast response to dynamic market needs have become critical to remaining competitive. For digital products (e.g., news services and other Internet content providers [ICPs]), personalized services that provide tailored content to different clients, based on their interests, become feasible and necessary. The large amount of transactional data, collected from the use of Internet-enabled information systems, allows a company to understand customer needs and integrate the discovered knowledge into its product design and marketing plans. Existing literature has proved that customized sellers can charge more for customized products (e.g., [13]).

The Internet is an excellent platform for content providers to tailor their products based on customer preference. This is particularly true for online news services and knowledge management. For Internet news Web sites, most readers are only interested in certain types of news among the large number of reports. Some may be interested in political news, while others are interested in stock market movements. Therefore, providing news reports that meet a reader’s interests can save time and effort. As a result, personalized services have been adopted by many news Web sites, including crayon.net and Google News. Similarly, it would be useful if a personalized recommendation system could find relevant documents in the knowledge repository for users when they use a knowledge management system to solve a specific problem.

Although it is intuitive that personalization could add value to content providers, existing literature has not provided adequate theoretical and empirical evidence to tell whether the user really likes personalized services. Therefore, it would be useful to gain insight into issues related to the use of these services, such as the effect of personalized services on user satisfaction and factors that affect the satisfaction with these services.

In this paper, we review theories relevant to personalized services, build a research model, and evaluate the role of different theories empirically. The first theory is effort-based, which focuses on the principles of least effort and information overload. The second theory is motivation-based, which argues that the effect of personalization on user satisfaction is affected by individual motivation. The third theory is process-oriented, which argues that user satisfaction is affected by the design of a personalization process and, more specifically, the effect of user involvement in the process. These theories are synthesized to build a research model and are evaluated in two experiments. The results indicate that the design of a personalized service should focus on reducing information overload, although all theories can explain the effect of personalized news services on user satisfaction.

## Personalization and Recommendation Systems

A PANEL ON PERSONALIZATION AND DATA MINING defined personalization as “a process of collecting and using personal information to uniquely tailor products, content and services to an individual” [47, p. 116]. The Personalization Consortium offered the following definition in 2003: “personalization is the use of technology and customer information to tailor electronic commerce interactions between a business and each individual customer. Using information either previously obtained or provided in real time about the customer, the exchange between the parties is altered to fit that customer’s stated needs, as well as needs perceived by the business based on the available customer information” (excerpt from [1, p. 83]).

Due to the complexity of profiling customers, and the increased popularity of the Internet, proper use of IT is critical for personalization. An information system that provides content or product information to meet the needs of a particular customer is called a recommendation system or recommender system. Research and practical applications of the recommendation system have been widely reported (e.g., [3, 6, 29, 43]).

The kernel of a recommendation system is the mechanism that identifies user preferences and assesses the relative importance of a candidate item for recommendation, based on the likelihood that it will match the user’s preference. Because the process needs to select a limited number of candidate items from a large information repository, the technique is called information retrieval or information filtering.

Recommendation mechanisms may be classified by the features used to determine user preferences, and the methods used for data collection. Features used for analyzing user preferences may include attributes of the product (attribute-based filtering) or the behavior of the user (collaborative filtering). In attribute-based filtering, if the attribute is selected from the content (e.g., key words), it is called content-based filtering. If the attribute is related to the demographic information of the user, it is called demographic-based filtering.

Two methods also exist for collecting user preference data—implicit and explicit [33, 51]. The explicit method asks the user to express preferences or choices explicitly and uses this feedback to build a user profile and make recommendations accordingly. It has been adopted by many online news or other content providers. For example, the reader is asked to indicate the interest level from one to ten, after viewing a report. That information is then used to build a user profile for future recommendations [32]. Although this approach can capture user preferences immediately, the user may refuse to provide the input due to privacy or other concerns. The implicit method, in contrast, lets the system monitor the user’s browsing behavior (capturing keystrokes and hyperlinks) and infers user preferences from the collected browsing data. Previous literature has found that the implicit method performs as well as the explicit method in capturing user preferences [26, 51].

Although many previous studies have reported applications of recommendation systems, few of them have investigated whether personalized services can really improve user satisfaction, or why user satisfaction is increased. In order to take full advantage of personalization technology, we need to have a better understanding of how users respond to this service and its theoretical foundation.

## Theories Related to Personalized Content Services

A FEW THEORIES ARE AVAILABLE FOR UNDERSTANDING the need for information personalization and its effect on user satisfaction. For instance, Case [10] outlined five major psychological and social theories related to information seeking—principle of least effort, uses and gratifications, sense making, media use as social action, and play theory. Another theory that supports information customization is information overload [18]. These theories fall into two general categories—effort for usage (e.g., least effort and information overload) and user motivation for accessing the information (uses and gratifications, sense making, social action, and play theory). In addition, previous research in information systems has found user involvement to be a key factor that affects the attitude toward system use. Hence, it is natural to believe that user involvement in the process of creating personalized content affects user satisfaction.

## Effort-Based Theories

## Principle of Least Effort

Zipf’s principle of least effort states that each individual will adopt a course of action that will involve the least average work from the person. His theory is supported by evidence from various studies of language usage [53]. The principle of least effort predicts that information seekers will minimize the effort required to obtain information, even if it means accepting a lower quality or quantity of information. Allen [2] investigated 19 research and development engineers and found that they operated on a least effort basis when selecting information channels. Rosenberg [37] found patterns similar to those observed by Allen [2] in industrial personnel. From the theory, it is evident that accurate content recommendation, which reduces the effort needed by a user to search for relevant information, can increase user satisfaction.

## Information Overload

An alternative to the least effort theory is information overload, which means users are given more information than they can handle within a given time frame. That is, the user would prefer to remove some information in order to reduce the necessary effort for finding the target. Information overload affects decision making in two ways. Due to sheer volume, users are unable to locate what they need most, often making them overlook what they consider critical [20]. Users also fail to use the relevant information at hand, or known to be available, leading to the inefficient use of decision-making time [15, 49].

Many factors may cause information overload. Ho and Tang [21] argued that three factors cause information overload—information quantity, information quality, and information format. Grise and Gallupe [18] used the number of ideas, topic domain, idea diversity, and time to measure information overload. They found that individuals in high-load conditions were less satisfied when using electronic meeting systems.

IT is useful in alleviating information overload. For example, Berghel [7] outlined five ways to deal with information overload—search engines, information agency, information customization, brand identification, and information push. Ho and Tang [21] proposed the use of infomediary models to reduce information overload. Chung et al. [11] found that the use of knowledge maps could reduce information overload on Web browsing. From the above literature, we can conclude that personalized services can increase user satisfaction by reducing information overload, if such services can provide accurate recommendation, thus leading to the following proposition:

Proposition 1: User satisfaction increases when the information load is reduced by accurate personalized content recommendation.

## Motivation-Based Theories

Another set of theories interprets user behavior in using information media by analyzing users’ intrinsic motivations. These include uses and gratifications, media use as social action, sense making, and play theory.

## Uses and Gratifications

First noted by Elihu Katz in 1959, the uses and gratifications theory states that media audiences access information with a certain purpose and play an active role in selecting the source and the information they would like to access [8, 23]. This theory has been found useful in explaining the behavior of people using many new communication technologies. Sample studies include videocassette recorders by Levy [27], videotex by Atwater et al. [4], cable television by Heeter and Greenberg [19], political computer bulletin boards by Garramone et al. [17], video recorders by Rubin and Bantz [39], remote control devices by Perse and Ferguson [35], and political news on the Web by Kaye and Johnson [24]. While the uses and gratifications approach has traditionally been applied to the mass media, this theory is also useful in analyzing the goal-directed behavior of Web users [28].

## Media Use as Social Action

Media use as social action (MUSA), proposed by Renckstorf and McQuail [36] (also known as Renckstorf’s social action model [31]), is an extension of the uses and gratifications theory. It differentiates the purpose of media use into three categories: social uses of media (context-directed, such as facilitating communication and relaxation), instrumental uses (goal-directed rational behavior, such as deciding on which house to buy), and the intrinsic use of media for entertainment (emotion directed, such as becoming a fan of a football team). Bosman and Renckstorf [9] argued that the information-seeking behavior was linked to one’s motivations for media use. In other words, users with different motivations may have different patterns of information seeking. In information systems literature, the use of executive information systems was found to have different organizational effects in two different usage modes—scanning and target search [48]. Therefore, we may anticipate that personalized services may have different effects for scanning and target search.

## Sense Making

The main argument of sense making is that “information is not something that exists apart from human behavior and activity” [12, p. 63]. Rather, information is “created at a specific moment in time-space by one or more humans” [12, p. 63]. Sense making sees “information as something that is constructed internally in order to address discontinuities in life” [12, p. 63]. In other words, users have certain purposes in mind when they seek information. The theory suggests that, unless the content provided makes reasonable sense (or meets their expectation), the audience will not use it. It is more related to the instrumental use of media.

## Play and Entertainment Theories

Play theory argues that entertainment value is the most important need for media use. Stephenson [45] developed research on the premise that humans manipulate their intake of entertainment and information to serve their emotional needs. At the heart of the theory is that humans not only tend to seek pleasure and avoid pain but they also mix work with play. It is difficult to say where “information” stops and where “entertainment” begins [10, 52]. Toms [46] found support for a curiosity- or playdriven interpretation of reading electronic news. This theory supports the intrinsic (emotional) use of media.

If we consider the Internet to be a medium, then the above literature leads to the following proposition:

Proposition 2: User satisfaction with personalized content services differs for users with different motivations.

## Process-Oriented Theory: User Participation and Involvement

Another dimension related to personalization is the degree of user involvement in the process of constructing their interest profiles. Based on the user involvement theory, the user’s participation in the process may increase user satisfaction.

Beginning in the early 1960s, the practitioner and researcher have argued that user participation is critical in the development and implementation of information systems [22]. A design approach that reflects the emphasis on user involvement (called participative design) was popular at that time. Barki and Hartwick [5] later differentiated user participation as a series of activities or behaviors performed by the potential users, and user involvement as a subjective psychological state, reflecting the importance and personal relevance that a user attaches to a given system.

Because a personalized content recommendation system is also an information system, we posit that a recommendation mechanism that requires explicit user feedback in the process is likely to have a higher user satisfaction than those that do not require explicit feedbacks, which leads to the following proposition:

Proposition 3: User satisfaction will be higher for recommendation systems that use explicit user feedback for personalization than for systems that do not require explicit user feedback.

A framework that combines the three theories is illustrated in Figure 1. Because content recommendation has to obtain user browsing information first, it is difficult to examine the user involvement effect together with the other two effects. Therefore, the empirical testing of the model was done in two experiments. The first one compared the effect of different recommendation methods and the second one tested the effects of information overload and user motivation.

## The First Experiment

## Task Domain

THE PARTICULAR DOMAIN USED FOR THE EXPERIMENT was Internet news, which has become a popular application in content provision. The traditional way of having an editor in chief to judge which items are of high enough interest and importance for placement in the headlines, with others put under different categories, is changing in online news. The Los Angeles Times, London Times, CRAYON, and Tango have adopted collaborative recommendation systems to provide customized online news. Many such trials have been reported in the past decade. For example, Mock and

![](/api/attachments/PEFCEYKE/fulltext/images/cf57641c32d713e80b4b6e5df1eeccef79e1026eefe67a6640301309b6883d5d.jpg)  
Figure 1. Theoretical Research Framework

Vemuri [32] use the Intelligent News Filtering Organization System (INFOS) to seek user input and reorganize the order in which news is presented, thus reducing readers’ search load. Konstan et al. [25] proposed GroupLens, which summarized feedback from previous users to help a current user decide to review or not review a report. Sakagami and Kamba [40] developed ANATAGONOMY, which used an implicit approach to infer users’ preferences from their previous browsing behaviors (e.g., scrolling and enlarging windows) to produce personalized Web news. Many Web sites offer personalized news services, such as crayon.net and Google’s new Google News site. Therefore, online news service is an appropriate domain for studying content recommendation.

The first experiment was designed to answer two questions:

1. Do personalized recommendation methods capture the reading interest of the users to make accurate recommendation and increase user satisfaction? and

2. Do users prefer having direct input in the process of generating personalized content?

## Experimental Systems

Two personalization methods (explicit and implicit) were adopted to examine whether user feedback plays a role in user satisfaction. They were then compared with the traditional headline news approach (HLA) to examine the effect of reducing information overload. The explicit approach analyzes user interests based on key words and the interest ratings reported by the user after reading a particular article (called the self-reporting approach [SRI]). The implicit time-based approach (TBA) analyzes user interests, based on user reading interests as measured by the key words of the article and the length of time a user spent reading the article (details of the recommendation mechanisms can be found in Lai et al. [26]). TBA does not require the users to feedback their interest ratings after viewing a report.

Three news Web sites were designed for this experiment. The HLA system copied the regular headline news from www.chinatimes.com.tw (a popular news Web site in Taiwan, with millions of viewers every day). The home page showed the titles of the headline news chosen by the editor and 13 news categories (such as sports, stocks, etc.). The screen layout of the SRI and TBA systems was the same as the HLA system, except that the headline news was replaced by the news reports selected by the recommendation algorithms for each individual reader. When a user logged into the SRI or TBA system, the computer assessed the user’s viewing interests based on historical data and then composed a personalized headline news area that replaced the headline news compiled by the editor. Reports not selected for recommendation by the algorithm remained in their respective categories.

## Research Hypotheses

Based on the framework in Figure 1, recommendation accuracy and user satisfaction were the two main dependent variables. Recommendation accuracy measures the ability of the personalized method to capture audience interest, and user satisfaction measures the audience acceptance of the recommendation. The independent variables were different personalization methods. Two hypotheses are posited as follows:

Hypothesis 1 (Effect of Personalization Services): Personalized systems (TBA and SRI) perform better than the nonpersonalized HLA.

Hypothesis 2 (Effect of User Involvement in Personalization): SRI, which requires user feedback in the personalization process, will lead to higher user satisfaction than TBA, which does not require user feedback.

## Experimental Design and Procedures

Ninety-six volunteers were recruited and divided into two groups: one viewed HLA and SRI (Group I), and the other viewed HLA and TBA (Group II). Subjects were asked to participate in the experiment for four days. Nine subjects dropped out during the process, which left 87 effective subjects, with 43 in Group I and 44 in Group II.

Subjects in both groups were asked to view HLA for the first two days and fill out a satisfaction questionnaire after the second day. On the third and fourth days, users in Group I viewed SRI and those in Group II viewed TBA. After finishing on the fourth day, they all filled out questionnaires again to indicate their satisfaction with the experimental system. Subjects in Group I had to indicate their interests in the report on a seven-point scale (the higher the better) after each viewing, while the subjects in Group II did not have to do so. The average number of news items was 255 per day, distributed into 13 categories, with an average of 44 items included in the headline news chosen by the editors in the HLA approach.

## Instruments and Measurement

In the experimental process, both objective and subjective data were collected for analysis. Objective data were recommendation accuracy and user background; subjective data were user satisfaction with the experimental Web sites.

## Recommendation Accuracy

Two indices common for measuring the accuracy of a recommendation method were used—precision and recall [41, 42]. Precision measures the portion of recommended news that is relevant (i.e., number of recommended and read/number of recommended), and recall measures the portion of relevant news that is recommended (number of recommended and read/total number read).

## User Satisfaction

The instrument for measuring user satisfaction included four dimensions—information content, personalized services, user interface, and system value. Satisfaction with information content was measured using three questions adapted from Doll and Torkzadeh [14]:

1. whether the system finds the news that the user wants to view,

2. whether the system filters out the news that the user does not want, and

3. whether the system captures the right category (the one that is of interest to the user).

User satisfaction with personalized services was measured using three questions adapted from the customized service portion of SERVQUAL [34]:

1. whether the system pays attention to the user needs,

2. whether the system captures the user’s interests, and

3. whether the system provides adaptive services.

User satisfaction with the user interface was measured by four questions adapted from Doll and Torkzadeh [14]:

1. whether the system is easy to use,

2. whether the system is friendly,

3. whether the interface is properly formatted, and

4. whether the presentation is clear.

Questions about the value of the system included:

1. whether the system is useful, and

2. whether the system finds interesting news efficiently.

Table 1 summarizes the measurement dimensions and items.

A question designed to assess the overall satisfaction of the user was also included. All answers were on a seven-point Likert scale, with 1 being least agreed and 7 being most agreed.

The reliability data (Cronbach’s alpha) show that the instruments are acceptable because their alpha values are higher than 0.6. Results from the factor analysis show that the construction validity holds (see Appendix Tables A1 and A2).

Table 1. Dimensions for Measuring User Satisfaction

<table><tr><td>Information content</td><td>Customized service</td><td>User interface</td><td>System value</td></tr><tr><td>Find the wantedFilter out the unwantedCapture the right category</td><td>Attention to user needsCapture interestsAdaptive service</td><td>Easy to useFriendlyProperly formattedClear presentation</td><td>UsefulEfficient</td></tr></table>

## User Background Factors as Control Variables

Questions were also designed to collect user background information. Ten questions (including which news categories they like, experience in using the Internet, and frequency of accessing online news) were asked to see whether user satisfaction differed in different user groups. The results indicate that these background factors had no significant effect on user satisfaction.

## Experimental Results

The system recorded the number of news reports shown to a subject (NNS), the number of news reports viewed by the subject (NRR), and the number of news reports recommended and accepted by the subjects (NRA). Precision is calculated as NRA/NNS and recall is calculated as NRA/NRR. The results are shown in Appendix Table A3.

As the data indicate, the traditional headline (HLA) system presented 41 news items to all subjects on the home page, whereas the explicit SRI and implicit TBA systems recommended an average of 17.77 and 17.61 news items to each subject, respectively. The personalized systems were more selective than the headline news approach, but had a higher number of items read by the subject (NRA). The explicit SRI approach had the highest precision and user satisfaction, whereas the implicit TBA approach gave the highest recall.

## Effect of Personalization

The effect of personalization was examined by comparing the performance differences between systems with personalized services (SRI and TBA) and the traditional system (HLA). Because all subjects used the HLA system and either SRI or TBA, the paired t-test was used to compare the effects of SRI and TBA with the benchmark HLA. The results indicate that the accuracy in identifying user interests, as measured by precision and recall, was significantly higher for SRI and TBA than for HLA, but the difference between SRI and TBA was not statistically significant. Therefore, we can conclude that both recommendation methods outperform the traditional headline approach. Tables 2 and 3 indicate that user satisfaction is also significantly higher for SRI and TBA than for HLA. Therefore, H1 is supported: personalization can lead to higher user satisfaction.

Table 2. Results of Paired t-Test on User Satisfaction

<table><tr><td rowspan="2"></td><td colspan="2">Mean</td><td rowspan="2">Difference</td><td rowspan="2">t-value</td><td rowspan="2">Significance</td></tr><tr><td>SRI</td><td>HLA</td></tr><tr><td>Content</td><td>5.8488</td><td>5.2558</td><td>0.5930***</td><td>4.379</td><td>0.000</td></tr><tr><td>Customization</td><td>5.7558</td><td>4.6628</td><td>1.0930***</td><td>7.474</td><td>0.000</td></tr><tr><td>Interface</td><td>5.6802</td><td>5.4244</td><td>0.2558***</td><td>2.632</td><td>0.012</td></tr><tr><td>Value</td><td>5.9767</td><td>5.3488</td><td>0.6279***</td><td>3.699</td><td>0.001</td></tr><tr><td>Overall</td><td>5.8605</td><td>5.2558</td><td>0.6047***</td><td>6.800</td><td>0.000</td></tr><tr><td colspan="6">*** denotes p&lt;0.01.</td></tr></table>

## Effect of User Involvement

The second hypothesis deals with the difference between SRI, which requires user feedback for building user profile and TBA, which automatically constructs user profiles from their browsing behavior. Comparing the user satisfaction data of SRI and TBA in Tables 2 and 3, we find that most differences are not statistically significant, except the user’s feeling of system customization $( t = 2 . 0 0 4 , p < 0 . 0 5 )$ . This may be because SRI explicitly required the user to provide feedback after reading news and, hence, enabled the subject to feel that the outcome was more customized. Therefore, H2 is not fully supported and we conclude that both recommendation methods perform equally well. That is, user involvement in the recommendation generation process is not critical to overall user satisfaction with the system.

## Major Findings and Limitations

The findings from the first experiment indicate that personalized systems can indeed capture user preference and increase user satisfaction through recommending relevant news to the reader accurately. User motivation has some effects on user satisfaction, but feedback from the user may not be essential for building a user profile, because user interest ratings improve neither recommendation accuracy nor overall user satisfaction. Although the findings support the two hypotheses, the experiment has certain limitations.

First, the subject consistently viewed the personalized system after viewing the HLA system. This was due to the nature of the process, that is, the implicit recommendation method needs prior browsing of data, which makes it difficult to swap the sequence, so the order effect between personalized system and the benchmark HLA may exist in the experimental process. Second, subjects were given more news items (41) to read in the HLA system than in the other two recommendation systems (fewer than 20). This may have caused unexpected bias due to unequal information load when using different systems. Because SRI and TBA had the same performance in both recommendation accuracy and user satisfaction in the first experiment, we removed TBA and conducted a second experiment to test the effect of information overload and user motivations (i.e., P1 and P2 in Figure 1).

Table 3. Results of Paired t-Test on User Satisfaction

<table><tr><td rowspan="2"></td><td colspan="2">Mean</td><td rowspan="2">Difference</td><td rowspan="2">t-value</td><td rowspan="2">Significance</td></tr><tr><td>TBA</td><td>HLA</td></tr><tr><td>Content</td><td>5.6250</td><td>5.3068</td><td>0.3182*</td><td>1.956</td><td>0.057</td></tr><tr><td>Customization</td><td>5.4091</td><td>4.5682</td><td>0.8409***</td><td>4.650</td><td>0.000</td></tr><tr><td>Interface</td><td>5.5739</td><td>5.3125</td><td>0.2614**</td><td>2.168</td><td>0.036</td></tr><tr><td>Value</td><td>5.5455</td><td>5.4773</td><td>0.0678</td><td>0.380</td><td>0.706</td></tr><tr><td>Overall</td><td>5.7727</td><td>5.3409</td><td>0.4318***</td><td>3.772</td><td>0.000</td></tr></table>

\* denotes p < 0.10; \*\*\* denotes p < 0.01.

## The Second Experiment

## Research Framework and Hypotheses

INFORMATION OVERLOAD MAY BE CAUSED BY the number and precision (which shows the hit rate of recommended items matching user interests) of items recommended to a reader [18, 21]. We used a 2×2 factorial design: headline news versus personalized news and 40 versus 20 recommended items. In order to control the learning effect, the sequence of accessing personalized services and the number of news items were randomized. The revised research framework is illustrated in Figure 2. Three hypotheses are posited:

Hypothesis 3 (Effect of Information Amount): User satisfaction is higher for systems that recommend fewer items to the user.

Hypothesis 4 (Effect of Recommendation Accuracy): User satisfaction is higher when the accuracy of hitting user interests increases.

Hypothesis 5 (Effect of Individual Motivations): (a) The effect of personalized services on user satisfaction is affected by different motivations for information access. (b) The accuracy of capturing user interests by a personalized system is affected by different user motivations for information access.

## Experimental Design and Procedures

A total of 88 volunteers were recruited to participate in the experiment. Each subject was randomly allocated to one of the four settings in Appendix Table B1. We used the same news Web site (www.chinatimes.com) as in the first experiment. Because SRI and TBA showed equivalent performance in the first experiment, only SRI was used as the experimental system for making personalized news recommendations. Each subject viewed the news in one day and provided his or her interest ratings for building interest profiles. The system then recommended relevant news to the user in the following four days.

![](/api/attachments/PEFCEYKE/fulltext/images/3c3418e369609e553fc1f6cdb5a7bcae0322e150a44411ac3a13782e826066be.jpg)  
Figure 2. Framework for the Second Experiment

The experimental procedures were similar to the first one, including:

1. Filling out questionnaires about the background and motivations for reading online news, and then choosing news categories of interest to them (e.g., political or entertainment).

2. Performing experiment tasks. For example, the subject assigned to Setting 1 (40 RE) would see 40 news items generated by the recommendation system (RE) from the news on Day 1, choose those of interest to him or her, and fill out the evaluation form. After completing that task, the user moved to the next one, which in this case would be viewing 40 items chosen from the headline news (40 HL).

3. Continuing until completing all eight assignments in the setting.

## Instrument and Measurements

The questionnaires include three major modules—background, motivations, and user satisfaction. User background information includes his or her demographic information and Internet experience. A questionnaire was designed to include 17 items for measuring user motivations: (1) search news easily, (2) like to use computers, (3) like to use Internet, (4) obtain new information, (5) learn new knowledge, (6) need for work or study, (7) fun to read news, (8) read news as a hobby, (9) let me feel relaxed, (10) gain topics for chatting, (11) social interaction with friends, (12) join news group for discussion, (13) avoid lonely feeling, (14) release pressure from work or study, (15) surf Internet without purpose, (16) pass time, (17) have nothing else to do. We used precision for recommendation accuracy, which had the same effect as recall in our previous experiment. Because the previous four dimensions of user satisfaction were highly correlated, measurement of user satisfaction focused on the overall satisfaction.

## Experimental Results

Among the 88 volunteers, five of them did not complete the whole experiment, which results in a valid sample size of 83. The subjects were 73 percent male, 65 percent between ages 21 and 30, 56 percent with a bachelor’s degree, 37.4 percent with at least four years of work experience, 38 percent reading online news daily, and 91 percent with at least four years of Internet experience.

These demographic variables had no significant effect on either recommendation accuracy or user satisfaction. That is, the subject background was reasonably controlled. Appendix Table B2 shows the descriptive statistics at different experimental settings.

A factor analysis on the 17 motivation questions results in five factors, which are named as escape and passing time (Q13–17, eigenvalue = 3.427), social interaction (Q10–12, eigenvalue = 2.253), using IT (Q1–3, eigenvalue = 2.246), gaining information (Q5–6, eigenvalue = 1.883), and entertainment (Q7–8, eigenvalue = 1.749). The resulting user satisfaction levels, under different contingencies, are shown in Appendix Table B3.

The result on user motivation is consistent with prior literature, such as Rubin [38], who found five common motivations in studying the uses of television—information, entertainment, escape, habitual passing of time, and companionship. Kaye and Johnson [24] found four primary motivations for connecting to online political news—guidance, information seeking/surveillance, entertainment, and social utility. Ferguson and Perse [16] identified five motivations in using the World Wide Web—entertainment, passing time, relaxation/escape, social interaction, and information.

From the means in Table B3, we can find that the recommendation system generated significantly higher precision (0.51 versus 0.38 for HLA; F = 60.1, p < 0.001) and higher user satisfaction levels (4.758 versus 4.056; F = 27.38, p < 0.001). In other words, the personalized system adopted in the experiment was significantly better than the headline news approach in capturing user interests and increasing user satisfaction.

## Effect of Recommendation Accuracy

Table 4 shows the results from multivariate analysis of variance (MANOVA). The main effects of the personalized service (RE), and the interaction effect between the personalized service and the number of items (NO) presented to the subject, are statistically significant. User motivations and the main effect of usage sequence (i.e., whether the subject took HLA-SRI or SRI-HLA) are only marginally significant (p < 0.10). These results indicate that personalized systems made a very significant contribution toward user satisfaction. Hence, H4 is supported: personalized systems, which make more accurate content recommendations, result in higher user satisfaction.

<table><tr><td>Source</td><td>Type III sum of squares</td><td>Degrees of freedom</td><td>Mean square</td><td>F</td><td>Significance</td></tr><tr><td>News NO</td><td>1.273</td><td>1</td><td>1.273</td><td>1.289</td><td>0.260</td></tr><tr><td>MOTIVA</td><td>6.191</td><td>4</td><td>1.548</td><td>2.398</td><td>0.057*</td></tr><tr><td>NO * MOTIVA</td><td>3.544</td><td>4</td><td>.886</td><td>.898</td><td>0.470</td></tr><tr><td>RE</td><td>40.801</td><td>1</td><td>40.801</td><td>27.383</td><td>0.000***</td></tr><tr><td>RE * MOTIVA</td><td>4.227</td><td>4</td><td>1.057</td><td>.709</td><td>0.588</td></tr><tr><td>SEQ</td><td>1.916</td><td>1</td><td>1.916</td><td>3.490</td><td>0.065*</td></tr><tr><td>SEQ * MOTIVA</td><td>.558</td><td>4</td><td>.139</td><td>.254</td><td>0.906</td></tr><tr><td>NO * RE</td><td>8.615</td><td>1</td><td>8.615</td><td>4.635</td><td>0.034**</td></tr><tr><td>NO * RE * MOTIVA</td><td>5.643</td><td>4</td><td>1.411</td><td>.759</td><td>0.555</td></tr><tr><td>NO * SEQ</td><td>3.469</td><td>1</td><td>3.469</td><td>1.073</td><td>0.304</td></tr><tr><td>NO * SEQ * MOTIVA</td><td>8.811</td><td>4</td><td>2.203</td><td>.681</td><td>0.607</td></tr><tr><td>RE * SEQ</td><td>4.063</td><td>1</td><td>4.063</td><td>2.109</td><td>0.150</td></tr><tr><td>RE * SEQ * MOTIVA</td><td>6.345</td><td>4</td><td>1.586</td><td>.823</td><td>0.514</td></tr><tr><td>NO * RE * SEQ</td><td>5.116</td><td>1</td><td>5.116</td><td>.897</td><td>0.347</td></tr><tr><td>NO * RE * SEQ * MOTIVA</td><td>32.709</td><td>4</td><td>8.177</td><td>1.433</td><td>0.231</td></tr><tr><td colspan="6">*p&lt;0.10 (near significant); **p&lt;0.05; ***p&lt;0.01.</td></tr></table>

<sub>ffects</sub> <sub>of</sub> <sub>Different</sub> <sub>F</sub><sup>actors</sup> <sup>on</sup> <sup>User</sup> <sup>Sa</sup>

## Effect of Information Amount

From the data in Table B3, we find that the effect of personalized services increased rapidly when the number of news items presented to the user was reduced from 40 to 20. Hence, H3 is supported: increasing the number of items presented to the user will reduce user satisfaction, due to a higher information load.

Regarding the order effect, the sequence of reading headline news before personalized news (HL-RE, mean = 4.483) has a slightly higher user satisfaction than that of reading personalized news before headline news (RE-HL, mean = 4.331). The difference is small and marginally significant (p = 0.065 in Table 4). This implies that the gain in user satisfaction from adding personalized services to a nonpersonalized content provider is stronger than offering personalized services itself.

## Effect of User Motivation

The main effect of user motivation in Table 4 is marginally significant, which supports H5a. We further ran the data with the partial least squares (PLS) program on number of items shown, accuracy, user motivations, and satisfaction to see the relative influences of different factors. The result, as shown in Figure 3, indicates the following:

1. Recommending more items to the reader has a negative effect on user satisfaction (beta = –0.280), whereas making more accurate recommendations has a positive effect on user satisfaction (beta = 0.598). The motivation of loving IT shows a significant positive effect on user satisfaction, but its coefficient is small (0.088). H5a is partially supported: user satisfaction is affected by certain motivations for information seeking.

2. The recommendation accuracy is also affected by two particular user motivations—social interaction and gaining information. Social interaction has a positive effect, while gaining information has a negative effect. In other words, we see some support for the uses and gratifications theory in personalized content service. Hence, H5b is partially supported: the accuracy of personalized services differs when users have different motivations.

## Effect of Two Usage Modes

Because previous literature in information systems argues that two usage modes (scanning and target search) have different effects on executive performance [48] and Figure 3 indicates that social interaction (which tends to cover a broader set of interests) and gaining information (which tends to be more focused) have different effects on recommendation accuracy, we intend to investigate further whether these two modes have effects in online news. The user motivation measures were reclassified into two categories. The results from a factor analysis, as shown in Table B4, indicate that F1 includes reasons that do not have a particular focus (can be named scanning) while F2 includes those that have a specific purpose (can be named target search). Those items not on the table are removed.

![](/api/attachments/PEFCEYKE/fulltext/images/17b5cd082366dcd4083589be5be8a507d05c4427a05ea597009c770e389d0069.jpg)  
Figure 3. Result from the PLS Analysis  
\* indicates significance at the 0.05 level; \*\*\* indicates significance at the 0.001 level.

With these two usage modes, we used moderated regression analysis (MRA) to analyze the moderating effects [30, 44]. In applying MRA for a single predictor variable (i.e., precision as measured by the hit rate, HR), it is necessary to examine three regression equations for equality of the regression coefficients [50]. The criterion variable is user satisfaction (SAT). The moderator variable is represented by MOT. The equations to be examined are:

$$
\mathrm{SAT} = a + b _ {1} \mathrm{HR}\tag{1}
$$

$$
\mathrm{SAT} = a + b _ {1} \mathrm{HR} + b _ {2} \mathrm{MOT}\tag{2}
$$

$$
\mathrm{SAT} = a + b _ {1} \mathrm{HR} + b _ {2} \mathrm{MOT} + b _ {3} \mathrm{HR} \times \mathrm{MOT}\tag{3}
$$

For MOT to be a “pure moderator” variable, Equations (1) and (2) should not be different, but should be different from Equation (3). The results from a moderated regression analysis (shown in Table B5) indicate that the moderating effects of two different motivations exist at the significance level of 0.072, lower than the regular 0.05 level, but acceptable at the marginal 0.10 level. The regression lines of two different motivations are shown in Figure 4. That is, user satisfaction with a personalized system is more sensitive to the recommendation accuracy when the user has a certain target in mind (target search).

## Discussion and Conclusions

## Summary of Findings

PERSONALIZED SERVICES HAVE BECOME increasingly popular for ICPs. Well-known players, such as Google, have also begun to offer this function on their news Web sites. In this paper, we have reviewed several theories relating to personalized information services and conducted two experiments to evaluate these theories. Major findings include the following:

![](/api/attachments/PEFCEYKE/fulltext/images/91f34ff487c0b05f45103d03f2f5cb0b8bb307e88631d4d670833b6abfc3a173.jpg)  
Figure 4. Graphical Illustration of the Moderation Effect

1. Personalized services can indeed increase user satisfaction through accurate recommendation of relevant contents.

2. Information overload: A major theory that can interpret the value of personalized content services is information overload. We have found that both the number of items recommended to the user and the recommendation accuracy, as measured by the number of recommended items accepted by the user, had significant effects on the satisfaction of the user.

3. The uses and gratification theory: User satisfaction with personalized services differs significantly for users with different motivations. The satisfaction is higher when the motivation is social interaction, and is lower when the motivation is escape or entertainment.

4. The effect of recommendation accuracy on user satisfaction is moderated by different information usage modes. The effect is more sensitive to recommendation accuracy for users who have a specific information target in mind (target search) than for users who have no specific purpose when viewing online news (scanning).

5. The role of user feedback in personalized services is not significant, though the user involvement theory suggests that having user involvement can increase user satisfaction. This may be due to the fact that providing feedback requires more effort and hence offsets the effect of user involvement.

## Implications and Limitations

The above findings provide interesting implications for adopting personalized services in the future. From the theoretical point of view, we have integrated different theories relevant to providing personalized content services and empirically investigated their relative explaining capabilities in online news services. Our results indicate that reducing information overload is the most important concern for users in seeking information and that personalized recommendation can perform well when users use the media to seek specific information. The uses and gratifications theory, popular in the mass communication domain, is applicable to Internet-based information-seeking behavior. User feedback in the personalization process contributes insignificantly in both recommendation accuracy and user satisfaction. Therefore, algorithms that do not need user feedback may be more useful in implementing personalized content recommendation systems.

For practitioners, the following recommendations are useful. First, for a content provider (including knowledge management systems), the ability of the recommendation system to identify user interests correctly and make proper recommendations is critical to the success of the system. Second, personalized recommendations may not be suitable for all content providers. For Web sites whose users primarily intend to find specific information, personalized services will be more useful than the Web sites whose users come for escape or entertainment.

Due to resources and other constraints, the research is not without limitations. First, the experiments were conducted in laboratory environments, which are substantially different from the real-world information-seeking context. Therefore, more work needs to be done in order to know whether the results hold true in the real world. Second, online news is a popular domain, but the daily update nature of news reports is very unique. We are not sure whether findings in online news will hold in other domains. Finally, the recommendation method adopted in the research was content-based filtering. We are not sure whether collaborative filtering would result in the same findings. The comparison between content-based filtering and collaborative filtering in different domains may also be worth investigation in the future.

Acknowledgments: Earlier versions of the paper were presented at the Hawaii International Conference on System Sciences 2002, workshops at University of Queensland, University of Hong Kong, Hong Kong University of Science and Technology, City University of Hong Kong, and National Taiwan University. The authors thank Mohan Tanniru for his comments and assistance in the process of revising the paper and appreciate responses from reviewers and workshop participants on various versions of the paper. The project was partially funded by the MOE Program for Promoting Academic Excellence of Universities, under Grant No. 91-H-FA08–1-4 and National Science Council Grant No. NSC92–2416-H-110–006-CC3.

## REFERENCES

1. Adomavicius, G., and Tuzhilin, A. Personalization technologies: A process-oriented perspective. Communications of the ACM, 48, 10 (2005), 83–90.

2. Allen, T.J. Managing the Flow of Information. Cambridge, MA: MIT Press, 1977.

3. Ansari, A.; Essegaier, S.; and Kohli, R. Internet recommendation systems. Journal of Marketing Research, 37, 3 (August 2000), 363–375.

4. Atwater, T.; Heeter, C.; and Brown, N. Foreshadowing the electronic publishing age: First exposure to Viewtron. Journalism Quarterly, 62, 4 (1985), 807–815.

5. Barki, H., and Hartwick, J. Rethinking the concept of user involvement. MIS Quarterly, 13, 1 (1989), 53–63.

6. Bauer, T., and Leake, D. Using document access sequences to recommend customized information. IEEE Intelligent Systems, 17, 6 (2002), 27–33.

7. Berghel, H. Cyberspace 2000: Dealing with information overload. Communications of the ACM, 40, 2 (1997), 19–24.

8. Blumler, J.G. The role of theory in uses and gratifications studies. Communication Research, 6, 1 (January 1979), 9–36.

9. Bosman, J., and Renckstorf, K. Information needs: Problems, interests, and consumption. In K. Renckstorf (ed.), Media Use as Social Action: European Approach to Audience Studies. London: John Libbey, 1996, pp. 43–52.

10. Case, D.O. Looking for Information: A Survey of Research on Information Seeking, Needs, and Behavior. San Diego, CA: Academic Press, 2002.

11. Chung, W.; Chen, H.; and Nunamaker, J.A. Visual framework for knowledge discovery on the Web: An empirical study of business intelligence exploration. Journal of Management Information Systems, 21, 4 (Spring 2005), 57–84.

12. Dervin, B. From the mind’s eye of the user: The sense-making qualitative–quantitative methodology. In J.D. Glazier and R.R. Powell (eds.), Qualitative Research in Information Management. Englewood, CO: Libraries Unlimited, 1992, pp. 61–84.

13. Dewan, R.; Jing, B.; and Seidmann, A. Adoption of Internet-based product customization and pricing strategies. Journal of Management Information Systems, 17, 2 (Fall 2000), 9–28.

14. Doll, W.J., and Torkzadeh, G. The measurement of end-user computing satisfaction. MIS Quarterly, 12, 2 (June 1988), 259–274.

15. Farhoomand, A.F., and Drury, D.H. Managing information overload. Communications of the ACM, 45, 10 (October 2002), 127–131.

16. Ferguson, D., and Perse, E. The World Wide Web as a functional alternative to television. Journal of Broadcasting and Electronic Media, 44, 2 (2000), 155–174.

17. Garramone, G.M.; Harris, A.C.; and Anderson, R. Uses of political computer bulletin boards. Journal of Broadcasting and Electronic Media, 30, 3 (1986), 325–339.

18. Grise, M., and Gallupe, B. Information overload: Addressing the productivity paradox in face-to-face electronic meeting. Journal of Management Information Systems, 16, 3 (Winter 1999–2000), 157–185.

19. Heeter, C., and Greenberg, B. Cable and program choice. In D. Zillmann and J. Bryant (eds.), Selective Exposure to Communication. Hillsdale, NJ: Lawrence Erlbaum, 1985, pp. 203–224.

20. Herbig, P., and Kramer, H. The effect of information overload on the innovation choice process: Innovation overload. Journal of Consumer Market, 11, 2 (June 1994), 45–54.

21. Ho, J., and Tang, K. Towards an optimal resolution to information overload: An infomediary approach. In S. Ellis, T. Rodden, and I. Zigurs (eds.), Proceedings of the 2001 International ACM SIGGROUP Conference on Supporting Group Work. Boulder, CO: ACM Press, 2001, pp. 91–96.

22. Ives, B., and Olson, M. User involvement and MIS success: A review of the literature. Management Science, 30, 5 (1984), 586–603.

23. Katz, E.; Blumler, J.G.; and Gurevitch, M. Utilization of mass communication by individual. In J.G. Blumler and E. Katz (eds.), The Use of Communications. Beverly Hills, CA: Sage, 1974, pp. 19–32.

24. Kaye, B.K., and Johnson, T.J. Online and in the know: Uses and gratifications of the Web for political information. Journal of Broadcasting and Electronic Media, 46, 1 (2002), 54–72.

25. Konstan, J.A.; Miller, B.N.; Maltz, D.; Herlocker, J.L.; Gordon, L.R.; and Riedl, J. GroupLens: Applying collaborative filtering to Usenet news. Communications of the ACM, 40, 3 (March 1997), 77–87.

26. Lai, H.J.; Liang, T.P.; and Ku, Y.C. Customized Internet news services based on customer profiles. In N. Sadeh (ed.), Proceedings of the Fifth International Conference on Electronic Commerce. New York: ACM Press, 2003, pp. 225–229.

27. Levy, M.R. Home video recorders: A user survey. Journal of Communication, 30, 4 (Fall 1980), 23–27.

28. Lin, C.A., and Jeffres, L. Predicting adoption of multimedia cable services. Journalism Quarterly, 75 (1998), 251–275.

29. Linden, G.; Smith, B.; and York, J. Amazon.com recommendations: Item-to-item collaborative filtering. IEEE Intelligent Systems, 7, 1 (2003), 76–80.

30. McKeen, J.D.; Guimaraes, T.; and Wetherbe, J.C. The relationship between user participation and user satisfaction: An investigation of four contingency factors. MIS Quarterly, 18, 4 (1994), 427–451.

31. McQuail, D., and Windahl, S. Communication Models for the Study of Mass Communication, 2d ed. New York: Longman, 1993.

32. Mock, K., and Vemuri, V. Information filtering via hill climbing, Wordnet, and index patterns. Information Processing and Management, 33, 5 (1997), 633–644.

33. Orad, D., and Kim, J. Implicit feedback for recommender systems. AAAI Technical Report WS-98-08: Workshop on Recommender Systems. American Association for Artificial Intelligence, Menlo Park, CA, 1998.

34. Parasuraman, A.; Zeithaml, V.A.; and Berry, L.L. SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. Journal of Retailing, 64, 1 (1988), 12–40.

35. Perse, E.M., and Ferguson, D.A. The impact of the newer television technologies on television satisfaction. Journalism Quarterly, 70, 4 (1993), 843–853.

36. Renckstorf, K., and McQuail, D. Social action perspectives in mass communication research: An introduction. In K. Renckstorf (ed.), Media Use as Social Action: European Approach to Audience Studies. London: John Libbey, 1996, pp. 1–17.

37. Rosenberg, V. Factors affecting the preferences of industrial personnel for information gathering methods. Information Storage and Retrieval, 3, 3 (1967), 119–127.

38. Rubin, A.M. Television uses and gratifications: The interaction of viewing patterns and motivations. Journal of Broadcasting, 27, 1 (1983), 37–51.

39. Rubin, A.M., and Bantz, C.R. Uses and gratifications of videocassette recorders. In J.L. Salvaggio and J. Bryant (eds.), Media Use in the Information Age, Emerging Patterns of Adoption and Consumer Use. Hillsdale, NJ: Lawrence Erlbaum, 1989, pp. 181–195.

40. Sakagami, H., and Kamba, T. Learning personal preferences on online newspaper articles from user behaviors. Computer Networks and ISDN Systems, 29, 8 (1997), 1447– 1455.

41. Salton, G. Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Computer. Reading, MA: Addison-Wesley, 1989.

42. Saracevic, T., and Kantor, P. A study in information seeking and retrieving, II: Users, questions and effectiveness. Journal of the American Society for Information Science, 39, 3 (1998), 177–196.

43. Schafer, J.B.; Konstan, J.; and Riedl, J. Recommender systems in e-commerce. In M.P. Wellman (ed.), Proceedings of the First ACM Conference on Electronic Commerce. New York: ACM Press, 1999, pp. 158–166.

44. Sharma, S.; Durand, R.M.; and Gurarie, O. Identification and analysis of moderator variables. Journal of Marketing Research, 18, 3 (August 1981), 231–300.

45. Stephenson, W. The Play Theory of Mass Communication. Chicago: University of Chicago Press, 1967.

46. Toms, E.G. What motivates the browser? In T.D. Watson and D.K. Allen (eds.), Information Behavior: Proceedings of the Second International Conference on Research in Information Needs, Seeking, and Use in Different Contexts. London: Taylor Graham, 1999, pp. 191–208.

47. Tuzhilin, A. Report on the KDD2000 panel personalization and data mining: Exploring the synergies. SIGKDD Explorations, 2, 2 (December 2001), 115–116.

48. Vandenbosch, B., and Huff, S.L. Searching and scanning: How executives obtain information from executive information systems. MIS Quarterly, 21, 1 (1997), 81–107.

49. Wilson, P. Unused relevant information in research and development. Journal of American Society of Information Science, 46, 1 (1995), 45–51.

50. Zedeck, S. Problems with the use of “moderator” variables. Psychological Bulletin, 76, 4 (October 1971), 295–310.

51. Zhang, B., and Seo, Y. Personalized Web-document filtering using reinforcement learning. Applied Artificial Intelligence, 15, 7 (2001), 665–685.

52. Zillman, D., and Bryant, J. Entertainment as media effect. In J. Bryant and D. Zillman (eds.), Media Effects: Advances in Theory and Research. Hillsdale, NJ: Lawrence Erlbaum, 1994, pp. 437–462.

53. Zipf, G. Human Behavior and the Principle of Least Effort: An Introduction to Human Ecology. New York: Addison-Wesley, 1949.

## Appendix A. Descriptive Data for Experiment 1

<table><tr><td colspan="2">Table A1. Reliability Data</td></tr><tr><td>Dimension</td><td>Cronbach&#x27;s α</td></tr><tr><td>Information content</td><td>0.7018</td></tr><tr><td>Customized services</td><td>0.7714</td></tr><tr><td>User interface</td><td>0.8861</td></tr><tr><td>System value</td><td>0.6792</td></tr></table>

Table A2. Factor Loadings of Constructs

<table><tr><td>Items</td><td>User interface</td><td>Content</td><td>System value</td><td>Customization</td></tr><tr><td>Ease of use</td><td>0.8593</td><td></td><td></td><td></td></tr><tr><td>Friendliness</td><td>0.8498</td><td></td><td></td><td></td></tr><tr><td>Proper format</td><td>0.8343</td><td></td><td></td><td></td></tr><tr><td>Clear presentation</td><td>0.7393</td><td></td><td></td><td></td></tr><tr><td>Find wanted</td><td></td><td>0.8137</td><td></td><td></td></tr><tr><td>Remove unwanted</td><td></td><td>0.8087</td><td></td><td></td></tr><tr><td>Right category</td><td></td><td>0.7073</td><td></td><td>0.3627</td></tr><tr><td>Useful</td><td></td><td></td><td>0.8390</td><td></td></tr><tr><td>Efficient</td><td></td><td>0.4033</td><td>0.7223</td><td></td></tr><tr><td>Capture interests</td><td></td><td></td><td>0.3711</td><td>0.7448</td></tr><tr><td>Adaptive service</td><td></td><td>0.4013</td><td></td><td>0.6675</td></tr><tr><td>Personal attention</td><td></td><td>0.4759</td><td>0.3006</td><td>0.5125</td></tr><tr><td colspan="5">Notes: Loading values below 0.3 are not shown. Figures in boldface are in the same factor.</td></tr></table>

Table A3. Browsing Statistics of the Subject

<table><tr><td rowspan="2"></td><td colspan="2">HLA</td><td colspan="2">SRI</td><td colspan="2">TBA</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>NNS</td><td>41</td><td>0</td><td>17.77</td><td>7.42</td><td>17.61</td><td>5.97</td></tr><tr><td>NRR</td><td>14.02</td><td>6.32</td><td>14.53</td><td>5.99</td><td>14.34</td><td>5.21</td></tr><tr><td>NRA</td><td>2.16</td><td>2.49</td><td>6.33</td><td>3.51</td><td>6.27</td><td>3.55</td></tr><tr><td>Precision</td><td>0.0532</td><td>0.0609</td><td>0.3943</td><td>0.2340</td><td>0.3787</td><td>0.2051</td></tr><tr><td>Recall</td><td>0.1710</td><td>0.2119</td><td>0.4539</td><td>0.2304</td><td>0.4573</td><td>0.2354</td></tr><tr><td>Satisfaction</td><td>5.256</td><td>0.6580</td><td>5.861</td><td>0.5151</td><td>5.773</td><td>0.7108</td></tr></table>

## Appendix B. Descriptive Data for Experiment 2

Table B1. Settings of the Second Experiment

<table><tr><td>Settings</td><td colspan="2">Day 1</td><td colspan="2">Day 2</td><td colspan="2">Day 3</td><td colspan="2">Day 4</td></tr><tr><td>1</td><td>40 RE</td><td>40 HL</td><td>40 HL</td><td>40 RE</td><td>20 RE</td><td>20 HL</td><td>20 HL</td><td>20 RE</td></tr><tr><td>2</td><td>40 HL</td><td>40 RE</td><td>40 RE</td><td>40 HL</td><td>20 HL</td><td>20 RE</td><td>20 RE</td><td>20 HL</td></tr><tr><td>3</td><td>20 RE</td><td>20 HL</td><td>20 HL</td><td>20 RE</td><td>40 RE</td><td>40 HL</td><td>40 HL</td><td>40 RE</td></tr><tr><td>4</td><td>20 HL</td><td>20 RE</td><td>20 RE</td><td>20 HL</td><td>40 HL</td><td>40 RE</td><td>40 RE</td><td>40 HL</td></tr></table>

Notes: 20 and 40 are the number of items shown to the subject; RE = personalized services, HL = headline news. 20 RE means the personalized system recommends 20 news items to the subject.

Table B2. Mean and Standard Deviation of User Satisfaction

<table><tr><td>Settings</td><td colspan="2">Day 1</td><td colspan="2">Day 2</td><td colspan="2">Day 3</td><td colspan="2">Day 4</td></tr><tr><td>G1</td><td>4.52(1.21)</td><td>3.76(1.48)</td><td>4.00(1.41)</td><td>4.86(1.11)</td><td>5.10(1.18)</td><td>4.67(1.62)</td><td>4.38(1.28)</td><td>5.33(1.20)</td></tr><tr><td>G2</td><td>3.95(1.32)</td><td>4.65(1.69)</td><td>4.60(1.27)</td><td>4.20(1.47)</td><td>4.25(1.41)</td><td>4.70(1.49)</td><td>5.05(1.32)</td><td>4.25(1.77)</td></tr><tr><td>G3</td><td>4.10(1.74)</td><td>3.20(1.77)</td><td>4.00(1.49)</td><td>5.25(1.25)</td><td>4.75(1.16)</td><td>4.45(1.19)</td><td>4.00(1.49)</td><td>4.95(1.15)</td></tr><tr><td>G4</td><td>4.00(1.45)</td><td>4.95(1.46)</td><td>4.77(1.11)</td><td>3.68(1.32)</td><td>4.14(1.70)</td><td>4.45(1.70)</td><td>4.18(1.10)</td><td>4.23(1.41)</td></tr><tr><td colspan="9">Note: Numbers in parentheses are standard deviations.</td></tr></table>

Table B3. Satisfaction Levels Under Different Experimental Contingencies

<table><tr><td colspan="2">Construct</td><td colspan="2">Satisfaction level</td></tr><tr><td>Variable</td><td>Value</td><td>Mean</td><td>Standard deviation</td></tr><tr><td rowspan="2">Personalized services</td><td>Recommendation</td><td>4.758</td><td>0.096</td></tr><tr><td>Headline</td><td>4.056</td><td>0.124</td></tr><tr><td rowspan="2">Number of items</td><td>40</td><td>4.345</td><td>0.097</td></tr><tr><td>20</td><td>4.469</td><td>0.110</td></tr><tr><td rowspan="4">Personalized services * number of items</td><td>RE 40</td><td>4.616</td><td>0.104</td></tr><tr><td>RE 20</td><td>4.901</td><td>0.126</td></tr><tr><td>HL 40</td><td>4.074</td><td>0.134</td></tr><tr><td>HL 20</td><td>4.037</td><td>0.148</td></tr><tr><td rowspan="2">Sequence</td><td>RE-HL</td><td>4.331</td><td>0.094</td></tr><tr><td>HL-RE</td><td>4.483</td><td>0.101</td></tr><tr><td rowspan="5">Motivation</td><td>Escape</td><td>4.147</td><td>0.195</td></tr><tr><td>Social</td><td>4.868</td><td>0.189</td></tr><tr><td>Using IT</td><td>4.523</td><td>0.201</td></tr><tr><td>Information</td><td>4.338</td><td>0.195</td></tr><tr><td>Entertainment</td><td>4.158</td><td>0.207</td></tr></table>

Table B4. Two Motivations from Factor Analysis

<table><tr><td rowspan="2">Items</td><td colspan="2">Final factor structure</td></tr><tr><td>F1</td><td>F2</td></tr><tr><td>Do not know what else to do</td><td>0.878</td><td>-0.242</td></tr><tr><td>Passing time</td><td>0.856</td><td>-0.156</td></tr><tr><td>Avoid lonely feeling</td><td>0.771</td><td>6.031E-03</td></tr><tr><td>Forget pressure from work or study</td><td>0.764</td><td>6.573E-02</td></tr><tr><td>Surf the Internet without purpose</td><td>0.747</td><td>-2.854E-02</td></tr><tr><td>Let me feel relaxed</td><td>0.566</td><td>0.246</td></tr><tr><td>Obtain new information</td><td>-4.275E-02</td><td>0.818</td></tr><tr><td>Learn new knowledge</td><td>-0.162</td><td>0.745</td></tr><tr><td>Need for work or study</td><td>1.034E-02</td><td>0.667</td></tr><tr><td>Search news easily</td><td>0.106</td><td>0.614</td></tr><tr><td>Eigenvalue</td><td>3.598</td><td>2.195</td></tr><tr><td>Proportion</td><td>0.360</td><td>0.220</td></tr><tr><td>Cumulative</td><td>0.360</td><td>0.579</td></tr><tr><td colspan="3">Notes: Extraction method: principal component analysis; rotation method: varimax with Kaiser normalization.</td></tr></table>

<sub>Results</sub> <sub>from</sub> <sub>the</sub> M<sup>oderated</sup> <sup>Regression</sup>

<table><tr><td>Hypothesis</td><td>Regression equations (significance for individual regression coefficients)</td><td>F-value (significance)</td><td>Adjusted  $R^2$ </td><td>Result</td></tr><tr><td>H1</td><td>US = 2.833 + 3.524 HR (0.000)</td><td>375.940 (0.000)</td><td>0.361</td><td>HR has a significant positive relationship with US</td></tr><tr><td rowspan="2">H2</td><td>US = 2.799 + 3.524 HR + 0.072 MOT (0.422)</td><td>188.193 (0.000)</td><td>0.361</td><td>Motivation is a pure moderator</td></tr><tr><td>US = 2.959 + 3.166HR -0.223MOT + 0.656 HR x MOT (0.072)</td><td>128.881 (0.000)</td><td>0.363</td><td></td></tr></table>
