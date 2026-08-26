---
otero_id: 3802
otero_key: "YFEFUGAU"
title: "An empirical analysis of users’ privacy disclosure behaviors on social network sites"
authors: "Kai Li; Zhangxi Lin; Xiaowen Wang"
year: "2015"
journal: "Information & Management"
doi: "10.1016/j.im.2015.07.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: An Empirical Analysis of Users’ Privacy Disclosure Behaviors on Social Network Sites

Author: Kai Li Zhangxi Lin Xiaowen Wang

![](/api/attachments/YFEFUGAU/fulltext/images/0ef677e2a4ce79c5608b495ac88f0a3bddc90ed152b2fc8b9f4fbbd71cbbbedb.jpg)

PII: S0378-7206(15)00074-9

DOI: http://dx.doi.org/doi:10.1016/j.im.2015.07.006

Reference: INFMAN 2827

To appear in: INFMAN

Received date: 15-9-2014

Revised date: 27-6-2015

Accepted date: 9-7-2015

Please cite this article as: K. Li, Z. Lin, X. Wang, An Empirical Analysis of Users Privacy Disclosure Behaviors on Social Network Sites, Information and Management (2015), http://dx.doi.org/10.1016/j.im.2015.07.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## Highlights

We investigate the associations between some predictors and privacy disclosure behaviors.

Males and females have significantly differentiated privacy disclosure patterns.

Age has negative and significant relationships with disclosing breadth, and disclosing depth.

Neither SNS experience nor social network size significantly affects privacy disclosure patterns.

Blog number always has positive associations with privacy disclosure patterns.

# An Empirical Analysis of Users' Privacy Disclosure Behaviors on Social Network Sites

Kai Li<sup>a</sup>, Zhangxi Lin<sup>b</sup>, Xiaowen Wang

a. Business school, Nankai University, likai@nankai.edu.cn

b. Center for Advanced Analytics and Business Intelligence, Texas Tech University, zhangxi.lin@ttu.edu

c. School of Economics, Nankai University, wangxw@nankai.edu.cn

Abstract: Users' privacy on social network sites is one of the most important and urgent issues in both industry and academic fields. This paper is intended to investigate the effect of users' demographics, social network site experience, personal social network size, and blogging productivity on privacy disclosure behaviors by analyzing the data collected from social network sites. Based on two privacy sensitivity levels of disclosed information, the textual information of a user's blog postings can be converted into a 4-tuple to represent their privacy disclosure patterns, containing disclosing breadth and depth, and frequencies of high and low sensitive disclosures. The collections of a user's privacy disclosure patterns in social network sites can well reflect the user's privacy disclosure behaviors. Applying the general linear modeling approach to the blogging data converted with the coding scheme, we find that males and females have significantly differentiated privacy disclosure patterns in the dimensions of disclosing breadth and depth. In addition, age has negative and significant relationships with disclosing breadth, disclosing depth, and high sensitive disclosure. We also find that none of social network site experience, personal social network size, and blog length is significantly related to users' privacy disclosure patterns, while blog number always has positive associations with privacy disclosure patterns.

Keywords: privacy disclosure, social media, social network sites, generalized linear model

## 1. Introduction

Social media are a group of Internet and mobile based applications build on Web 2.0 technologies in which people can create, share, or exchange user-generated contents. Nowadays, they are becoming increasingly important in our daily life and have received substantial attentions (Parameswaran and Whinston, 2007). Social media rely on the Internet and mobile technologies to provide interactive platforms for information dissemination, content generation, and interactive communications (Wang et al., 2013). An array of Internet and mobile based applications define the way social media functions. Examples include weblogs, microblogs, online forums, wikis, podcasts, life streams, social bookmarks, Web communities, social networking, and avatar-based virtual reality (Zeng et al., 2010; Abrahams et al., 2013; Fan and Gordon, 2014). Based on these applications, social network sites (SNS) have gained tremendous momentum and have revolutionized the way individuals build and maintain interpersonal relationships (Abrahams et al., 2012; Zhou et al., 2014).

#

Since people are incorporating SNS as a part of their routine activities to interact with each other, the number of SNS users has grown exponentially in recent years. Every minute, terabytes of user-generated contents are posted by millions of users on various social network sites, such as LinkedIn, Facebook, Twitter, QQ, etc. In this way, SNS, underpinned by social media, become versatile resources for both industry and academia people to study the enriched and dynamic data contributed by a wide-range of users in the social network (Litt, 2013).

In the past decade, research on SNS are more about adoption and usage of SNS (Zhou and Li, 2014; Lin et al., 2014) and management of social relationships on SNS (Ellison et al., 2007). Limited work has covered the topic of privacy disclosure on SNS. In fact, privacy disclosure on SNS is becoming one of the most important and active research issues in the information system area (Joinson & Paine, 2007), because user-contributed contents poured into various SNS result in major concerns on misuse of this big data. Meanwhile, the Web2.0 era demands data openness for all kinds of innovative online businesses, meaning more privacy information disclosures. This would essentially help reduce the uncertainty of interactions, legitimate the access to a person in an online group, and eventually promote the online businesses (Taddei and Contena, 2013; Metzger, 2006).

Personal information exchange between people on social network sites allows these people to maintain relationships with friends, develop new friendships, and find support and information (Taddei and Contena, 2013). In another aspect, privacy disclosure on SNS has its negative side, such as privacy information stolen, trafficking, and privacy invasion. Gross and Acquisti (2005) found that users effectively place themselves at a greater risk for cyber and physical stalking, identity theft, and surveillance when they disclose personal information on SNS. In this way, concerning these negative effects of privacy disclosure has major influences in users' adoption and routine use of SNS (Zhou and Li, 2014). Therefore, this paper is intended to examine the predictability of privacy disclosure behaviors on SNS in terms of privacy sensitivity levels of information to be disclosed (in short, we will use "sensitivity levels of information" implying the context of privacy). We will check the differences between users' high sensitive information disclosing and low sensitive information disclosing in terms of SNS structure and mechanism. These are particularly important questions for SNS service providers in industry, and hence answering these questions would be a great help to interface design and privacy policy of SNS.

Our study contributes to the literature by focusing on the predictors of SNS privacy disclosure. Communication Privacy Management theory is introduced as a framework to clarify the influence of users' gender, age, social network site experience, personal social network size, and blogging productivity to their privacy disclosure behaviors. Specifically, privacy disclosure is divided into two dimensions: breadth and depth. High sensitive disclosure and low sensitive disclosure are also distinguished in the study. We collected the practical data from one of the most popular social network sites to test the models. The results clarified various predictors of SNS privacy disclosure and offered insights into the social implications of SNS.

The rest of paper is structured as follows. Related literature about privacy disclosure on social network sites are reviewed to provide the theoretical background and foundation for our study in Section 2. We describe research methodology of this paper in Section 3, including data, variables, and models. Empirical results are presented in Section 4. Finally, we conclude the paper and suggest future research directions.

## 2. Literature Review

## 2.1 Privacy Disclosure on Social Network Sites

Information privacy has been considered as one of the most important "ethical issues of the information age" (Mason, 1986; Smith, 1994; Smith et al., 1996). As a philosophical, psychological, sociological, and legal concept, it has been studied extensively from different perspectives in multiple disciplines in most spheres of the social sciences (Smith et al., 2011). Generally, it refers to an individual's control over the release of information about themselves (Belanger et al., 2002; Belanger and Crossler, 2011), including its collection, unauthorized use, improper access, and errors (Smith et al., 1996). Researchers from different areas view it as different concepts. In the IS domain, privacy is usually studied based on two definitions. The first one is the control-based definition of privacy offered by Westin (1967), in which, privacy was explained as the "claim of individuals, groups, or institutions to determine for themselves when, how, and to what extent information about them is communicated to others". This kind of control refers to the limiting of vulnerability during information transactions (Margulis, 2003). The second one is the commodity-based definition (Davies, 1997), which argues that privacy can be traded and marketed, and is subject to the economic principles of cost–benefit analysis and trade-off (Smith et al., 2011). The commodity-based definition now is the underlying assumption in many studies and theories in IS.

Recently, privacy disclosure has become an important phenomenon, particularly on online social network sites (Joinson & Paine, 2007). However, most literature about privacy in IS focuses on privacy concern. Dimensions, predictors, outcomes, and measurement of privacy concern have been discussed and developed (Smith et al., 2011; Hong and Thong 2013). That could be one of the reasons why recent articles have still noted the importance of information privacy in the IS literature and the need for additional empirical studies (Pavlou, 2011, Smith et al., 2011; Schwaig, 2013).

Privacy disclosure is generally referred to as the self-disclosure of personal information privacy. Self-disclosure is a concept from sociology which refers to the process of people communicating about themselves with other persons (Wheeless & Grotz, 1976). Intimacy and sensitivity appear to be particularly critical to information self-disclosure in previous studies in social psychology. Self-disclosure is considered as an important building block for intimacy. Therefore, degree of intimacy is used to define categories of disclosed information (Altman and Taylor, 1973). Information sensitivity must also be considered in the discussion of personal disclosure. Previous privacy studies found that consumers' willingness to disclose personal information depends on the sensitivity of this information (Malhotra et al., 2004). While intimacy is related more to an intrinsic risk, sensitivity is related more to an extrinsic risk, such as monetary loss (Norberg and Dholakia, 2004). Altman and Taylor (1973) concluded that there are two dimensions to self-disclosure: breadth and depth. Both are crucial in developing a fully intimate relationship. It is easier for breadth to be expanded first in a relationship due to its more accessible features; it

#

consists of outer layers of personality and everyday lives, such as occupations and preferences. Depth is more difficult to reach, given its inner location; it includes more sensitive memories and traits that we might try to hide from most people. This is why we reveal ourselves most thoroughly and discuss the widest range of topics with our spouses and loved ones (Tolstedt and Stokes, 1984). Right now the most popular theory to explain users' privacy disclosure is privacy calculus model drawn on the exchange theory (Laufer and Wolfe, 1977; Stone and Stone, 1990). Individuals are willing to disclose personal information in exchange for some social benefits (Culnan and Armstrong, 1999; Dinev Hart, 2006). Therefore, an individual's decision to disclose information privacy on social media becomes a rational choice. As personalized services become more popular on social media platforms (Kobsa, 2007), personalization-privacy paradox issue is discussed based on privacy calculus in different contexts from online web (Awad and Krishnan, 2006) to mobile (Xu et al., 2011; Sutanto et al., 2013).

While it is beneficial for people to disclose different kinds of information on social network sites, accompanying such disclosures is risky, which incurs the major concerns among scholars, privacy advocators, and the media (Bélanger and Crossler, 2011; Hong and Thong, 2013). In the prior literature, the proposed privacy paradox implies that individuals who perceive high benefit and low risk will have more intention to disclose privacy. However, some researchers found that people do not always act rationally in their privacy disclosure (Acquisti and Grossklags, 2003). Sometimes high perceived privacy risk and low intention to disclose information still result in relatively higher levels of actual information disclosure (Norberg et al., 2007). This implies us to cross out the "trade-off" thinking of intention based on perceived benefit and perceived risk.

On a social network site, privacy disclosure is regarded not only to the amount of personal information that an Internet user decides to release to others (Joinson & Paine, 2007), but also to the ease with which a user can be identified as a real person (Gandey, 2000). SNS like a stage where people can manipulate information, choosing what to disclose and what to hide (Taddei and Contena, 2013). Therefore, in this study we treated privacy disclosure as individuals' privacy boundary management issue, and tried to find more explanatory factors and elements in people's considerations in privacy disclosure. Besides, most existing studies in privacy disclosure in the information system area actually discussed and tested the intention of disclosure. Surveys and questionnaires are used to collect subjective data. This type of research can only reach the disclosure intention rather than practical disclosure behaviors. We use practical data collected from social network platforms to study the associations of users' demographics, social network site experience, personal social network size and blogging productivity with privacy disclosure behaviors, and is aimed at extending the existing theoretical findings.

## 2.2 Communication Privacy Management Theory

Communication privacy management (CPM) theory, also known as communication boundary management theory, is a theory about how people make decisions about revealing and concealing private information. It was firstly developed based on the dialectical conception of privacy in social penetration theory, where privacy is considered as a process of opening and closing a boundary to others (Petronio, 1991). CPM theory suggests that individuals maintain and coordinate privacy boundaries with various communication partners, where private boundaries ar

#

the division between private information and public information (Petronio, 2002). Boundary management is considered as a rule-based process. When people disclose private information, they depend on a rule-based management system to control the level of accessibility.

Privacy rules of this rule-based management system are developed with criteria implemented to decide if and how information will be shared (Petronio, 2007). CPM theory general classifies those criteria as core criteria and catalyst criteria. Core criteria mainly cover gender and cultural elements, while catalyst criteria involve contextual and motivational elements.

## 2.2.1 Core Criteria in SNS context

## 1) Gender

Society and cultures have evolved with a certain set of expectations on two genders (Chakraborty et al., 2013). These expectations elicit different kinds of responses from women and men that result in different social behaviors (Chakraborty et al., 2013). We argue this kind of social behaviors includes people's privacy disclosure behavior. CPM theory also suggests that to differ socialization processes and cultural expectations, the behaviors of men and women are differentiated in how they delineate their boundaries and how they understand privacy and disclosure practices (Petronio, 2002).

Dindia and Allen (1992) suggested that women tend to disclose more than men in the psychology field. In the study of the associations between gender and disclosure, females were found to be less privacy protective in the online scenario (Sheehan, 1999), and this was confirmed in recent research on correlations between gender and privacy-related measures on SNS (Hoy & Milne, 2010).

## 2) Age

Regarding SNS adoption, while young people are the primary users, more and more people in other age groups joined the SNS user population and the aging effect is fading. In 2013, 78% of 30 –49 year olds, 60% of 50–64 year olds, and 43% of adults over the age of 65 were reported as social media users (Brenner & Smith, 2013). As more old people become SNS users, it is more necessary to investigate the association between age and privacy issues on SNS.

Based on Petronio's theory, when people are getting older, their metaphorical privacy boundaries may expand or contract in different life stages (Petronio, 2002). From children to adults, boundaries expand with information as people develop new relationships and take on more life responsibilities. However, the boundaries begin to contract for the elders, as they count more on privacy concerns (Litt, 2013). Bryce and Klang (2009) claimed that users, particularly young people, tend to less concern about their online privacy issue, since they have insufficient awareness of the complexities of technology, and lack of understanding of legal protections. However, other studies suggested that many young people, even though they were concerned about their online privacy and aware of associated risks, but routinely disclosed personal information in their online interactions (Livingstone, 2008; Bryce and Klang, 2009). More studies found that teens and younger adults might actually be stricter in their general online privacy behaviors than older adults (Park, 2011). There seems to be conflicting evidences on how younger and older adults manage privacy when online. Thus, this paper is to clarify the associations between age and privacy disclosure, by analyzing different partitions of data to compare the privacy behaviors of people in different age groups.

## 2.2.2 Catalyst Criteria in SNS context

## 1) Social network experience and personal social network size

In the SNS context, social network experience and social network size are two important but rarely mentioned elements in the previous literature. Experience is the knowledge or mastery of an event or subject gained through involvement in or exposure to it, which can be applied to subsequent operations (Lacity and Willcocks, 1998). Previous research has empirically demonstrated a positive relationship between prior experience and acceptance of microcomputer technology (Nelson and Cheney, 1997) and identified prior experience as a predictor of technology usage (Igbaria et al., 1995; Igbaria et al., 1996; Kettinger and Grover 1997; Thompson et al., 1994). The association between online experience and individuals' privacy strategies was also found (Park, 2011). Lewis et al. (2008) found that students who use Facebook more frequently are more likely to adjust their profiles’ visibility to private. Litt (2013) also proved that individuals with more social network site experiences will engage with more technological privacy tools on social network sites. Therefore, we consider social network experience as a catalyst criterion in SNS context.

In this study, we argue that social network experience and social network size are catalyst criteria in SNS situation. In CPM theory, motivational criterion is a very important category of catalyst criterion. CPM theory suggests that owners of information can form certain bonds that lead to disclosure (Petronio, 2002). This kind of motivation for sharing can include reciprocity or self-clarification. If one of your friends has disclosed a great deal to you, out of reciprocity, you might be motivated to disclose to him. Higher social network experience means higher frequency logging into the SNS account and longer time staying in the log-in status. These will result in more opportunities to see friends' great deals. Larger personal social network size means more friends on SNS, which also brings a higher probability of forming bonds. Here we argue that there is a positive association between personal social network size and privacy disclosure behaviors.

## 2) Blogging productivity

Recently the social media posting has attracted research attentions in the information systems field, with topics such as hotspot predicting (Li and Wu, 2010) and knowledge mining (Abrahams et al., 2012; Wang et al., 2013). It is important to clarify the association between privacy disclosure and the frequency and length of blogs, which are defined as blogging productivity. We argue that blogging productivity can also be considered as a kind of catalyst criteria in CPM theory. In the SNS context, the more blogging contents that people post, the more privacy information they could disclose. Moreover, the attributes of blog postings are operable elements for SNS providers to predict users' privacy disclosure.

## 3. Research Methodology

## 3.1 Data

The data used in this paper is collected in September 2013 from http://www.renren.com, the largest and most popular social network site in China operated by Renren Inc. The dataset contains 1,216 users' gender, age, account rating, number of friends, and posted blogs, as most of these variables have been directly or indirectly associated with the use of Internet and social network sites in former literature (Bonfadelli, 2002; Litt, 2013). There are slightly more females (50.9%) than males (49.1%) among subjects in the dataset. User ages range from 14 to 63 years old.

## 3.2 Measures

1) Social network experience, personal social network size, and blogging productivity

Social network experience. In this research, account rating is used to measure social network experience. It refers to the activity level of users' account on the social network sites, in terms of the frequency logging into the SNS account, the total time staying in the log-in status, and the completion of specific operations on the platforms. Account rating can motivate users' activeness by offering more functions and privileges on the platform in accordance with their account ratings. Therefore, account rating on social network sites reflects not only a measurement for social network site experience, but also user activeness and proficiency in a social network. We argue that users with high account rating have more positive attitudes on social network sites. Such positive attitudes stem from individuals' habit or predisposition which have been found as important antecedents of people's privacy concern and behavioral intention (Li, 2014). Besides, users who use social network sites more frequently are also more likely to know how to avoid privacy revelation (Litt, 2013).

Personal social network size. Number of friends is the direct measurement of a users' personal social network size. The reason why users disclose their information on social network sites is their intention to share or transmit information to their friends. Users with larger social networks are more likely forthcoming and open with their personal information on these sites. We argue that users who have more friends on social network sites have more motivations to disclose their personal information.

Blogging productivity. A user's blogging productivity is reflected by the quantity of blog postings they produced, which can be any combinations of photos, event comments, personal announcement, public testimonials, diary, idealized persona, etc. We measure a user's blog productivity in two variables, the number of blogs a user posted on a social network (denoted as blog number hereafter), and the average blog length (denoted as blog length hereafter) measured by the average size (byte) of all text in blogs a user posted on a social network site.

## 2) Dependent variables

Privacy disclosure is used as the dependent variable in this empirical analysis, which is in fact a group of privacy disclosure indicators, namely privacy disclosure pattern, measured in multiple dimensions. The collection of privacy disclosure patterns extracted from a user's blog postings can well reflect user's privacy disclosure behaviors.

We define the privacy disclosure pattern in three progressive steps. We firstly define the measurements of privacy sensitivity levels, then the scope of privacy disclosure based on the privacy sensitivity levels, and lastly the privacy disclosure composition with the frequencies of high/low sensitivity of disclosed information in a user's blog postings. In this way, a user's privacy disclosure pattern can be represented in the scope of privacy disclosure and privacy disclosure composition. A SNS user's privacy disclosure pattern is an aggregation of all his/her blog postings.

A. Previous privacy studies have found that consumer willingness to disclose personal information depends on the sensitivity of this information (Nowak and Phelps, 1995; Milne, 1997; Phelps et al., 2000; Sheehan and Hoy, 2000; Malhotra et al., 2004). In the previous studies, financial data and medical information are known to be considered by users as more sensitive information, while lifestyle characteristics and shopping habits are viewed less sensitive (Nowak and Phelps, 1995; Phelps et al., 2000; Sheehan and Hoy, 2000; Malhotra et al., 2004). As sensitivity of privacy information is hard to be quantitatively evaluated, we classify the privacy of information, which is embedded in users' blog postings, into two levels, 1 or 2, in terms of privacy sensitivity from low to high as follows:

(1) hobbies, interests, and dining/shopping preference;

(2) birthday/age, gender, occupation, email address, Instant messaging tools account (e.g. QQ, MSN), and cell phone number, name, ID number, and financial information (e.g. income, credit/debit card number, Alipay account<sup>1</sup>).

The first level of information is low sensitive, and the second level is high sensitive.

B. We also measure the scope of privacy disclosure in two dimensions, breadth and depth, following the former literature (Altman and Taylor, 1973; Norberg and Dholakia, 2004). In the traditional theory, the breadth of a disclosure is defined as the range of topics discussed by two individuals, and the depth of the disclosure is defined as the degree that the information revealed is private or personal. This paper denotes disclosing breadth (DB) as the range of topics contained in a user's posted blogs on social network sites, measured by the frequency of privacy information that appears in a user's blogs. Similarly, we denote disclosing depth (DD) as the highest sensitivity level of privacy information disclosed in a user's posted blogs, coded with 1 or 2 according to the sensitivity levels of privacy information in the above defined two levels.

C. The privacy disclosure composition consists of two elements, low sensitive disclosure (LSD) and high sensitive disclosure (HSD). LSD is measured as the frequency of low sensitive privacy information that appears in a user's blog postings, while HSD is measured by the frequency of disclosing high sensitive privacy information. LSD and HSD can jointly reflect a user's privacy disclosure tendency.

Based on the above setting, privacy information in each blog posting can be measured in a 4-tuple (DB, DD, LSD, HSD) to reflect a user's privacy disclosure pattern in the posting. Here is an example showing the application of the above coding scheme for the privacy disclosure pattern of a blog posting:

Morning swimming is so great! I love swimming! Just now I finished 3000 meters! My whole body feels full of power....I decide to order my favorite chicken pizza to treat myself....BTW, my QQ was stolen, I applied a new one (21287432). Q me, guys!

From this example, we can obtain a 4-tuple of privacy disclosure pattern of the posting: (DB, DD, LSD, HSD)  (3,2,2,1) . Table 1 lists the summary statistics from all coded blog postings by 1,216 users.

Table 1. Summary statistics of all variables (N=1216)

<table><tr><td>Variable</td><td>Mean</td><td>Std.D</td><td>Min.</td><td>Max.</td></tr><tr><td>Gender</td><td>0.49</td><td>0.5</td><td>0</td><td>1</td></tr><tr><td>Age</td><td>25.71</td><td>8.61</td><td>14</td><td>63</td></tr><tr><td>Account rating (AR)</td><td>22.82</td><td>5.21</td><td>4</td><td>34</td></tr><tr><td>Friend Number(FN)</td><td>187.69</td><td>124.96</td><td>7</td><td>453</td></tr><tr><td>Blog Number(BN)</td><td>128.37</td><td>50.82</td><td>1</td><td>377</td></tr><tr><td>Blog Length(BL)</td><td>87.44</td><td>37.23</td><td>4</td><td>209.73</td></tr><tr><td>Disclosing Breadth(DB)</td><td>21.39</td><td>13.87</td><td>0</td><td>91</td></tr><tr><td>Disclosing Depth(DD)</td><td>1.51</td><td>0.50</td><td>1</td><td>2</td></tr><tr><td>High Sensitive Disclosure(HSD)</td><td>2.42</td><td>7.31</td><td>0</td><td>31</td></tr><tr><td>Low Sensitive Disclosure(LSD)</td><td>18.77</td><td>11.34</td><td>0</td><td>69</td></tr></table>

Table 2 is the correlation matrix for all variables.

Table 2. Correlation analysis of all variables (N=1216)

<table><tr><td></td><td>Gender</td><td>Age</td><td>AR</td><td>FN</td><td>BN</td><td>BL</td><td>DB</td><td>DD</td><td>HSD</td><td>LSD</td></tr><tr><td>Gender</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Age</td><td>0.02</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AR</td><td>-0.17</td><td>0.22</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FN</td><td>0.09</td><td>-0.21</td><td>0.37***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BN</td><td>-0.11</td><td>-0.04</td><td>0.42***</td><td>0.39***</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BL</td><td>-0.03</td><td>0.08</td><td>0.12</td><td>0.22</td><td>-0.04</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>DB</td><td>-0.37***</td><td>-0.20*</td><td>0.11***</td><td>0.40</td><td>0.78***</td><td>0.06</td><td>1</td><td></td><td></td><td></td></tr><tr><td>DD</td><td>0.18</td><td>-0.09</td><td>0.16***</td><td>0.19*</td><td>0.19**</td><td>0.10</td><td>0.35***</td><td>1</td><td></td><td></td></tr><tr><td>HSD</td><td>0.01</td><td>-0.02</td><td>0.15</td><td>0.08</td><td>0.24</td><td>0.00</td><td>0.37**</td><td>0.29*</td><td>1</td><td></td></tr><tr><td>LSD</td><td>-0.30***</td><td>-0.08*</td><td>0.10***</td><td>0.19</td><td>0.53***</td><td>0.05</td><td>0.77***</td><td>0.50***</td><td>0.59***</td><td>1</td></tr></table>

Note: \*: p<0.1(2-tailed); \*\*: p<0.05(2-tailed); \*\*\*: p<0.01(2-tailed).

## 3.2 Generalized Linear Models of Privacy Disclosure

We constructed generalized linear models (GLM) to analyze the data. A GLM model consolidates several other statistical models to improve the predictive performance, which include linear regression, logistic regression, Poisson regression and so on (Nelder and Wedderburn, 1972). An iteratively reweighted least squares method is used for maximum likelihood estimation of the model parameters. First, we built basic models with four privacy disclosure variables and all independent variables.

$$
\text {   Model   1   to   4:   } \log E (Y) = \beta_ {1} G e n d e r + \beta_ {2} A g e + \beta_ {3} A R + \beta_ {4} F N + \beta_ {5} B N + \beta_ {6} B L + \text { intercept   }
$$

In Model 1 to Model 4, E(Y) in turn represents the expected value of disclosing breadth, disclosing depth, high sensitive disclosure, and low sensitive disclosure respectively. Coefficients $\beta _ { i }$ represent the log-transformed rate of privacy disclosure variables associated with the increase of each independent variable. After the basic models are tested, the dataset is stratified by sex and age to investigate the differences among different groups of users. Model 5 to 8 are used to test the different effects of independent variables on privacy disclosure between female users and male users, and model 9 to 12 are used for comparing the different effects among users of different age.

$$
\text {   Model   5   to   8:   } \log E (Y) = \beta_ {1} A g e + \beta_ {2} A R + \beta_ {3} F N + \beta_ {4} B N + \beta_ {5} B L + \text { intercept   }
$$

Model 9 to 12: log $E ( Y ) = \beta _ { \mathrm { l } } G e n d e r + \beta _ { \mathrm { 2 } } A R + \beta _ { \mathrm { 3 } } F N + \beta _ { \mathrm { 4 } } B N + \beta _ { \mathrm { 5 } } B L + \mathrm { i n t e r c e p t }$

Similarly, E(Y) in turn represents the expected value of disclosing breadth, disclosing depth, high sensitive disclosure, and low sensitive disclosure in Model 5 to Model 8 and in Model 9 to 12 respectively.

## 4. Empirical Results

## 4.1 Basic model

All three groups of GLM models are implemented and run with SAS version 9.1. Table 3 lists the coefficients of Model 1 to 4. The coefficient of Gender in Model 1 is negatively significant, indicating that male users have 18.1% lower Disclosing Breadth than female users. Similarly, the coefficient of $A g e$ in Model 1 indicates that an increase in the age of users by one year is associated with a decrease in the Disclosing Breadth of 4.3%. These results imply that female and younger users are associated with higher privacy disclosing frequency. The coefficients of Account rating and Friend Number are not significant, which suggests no significant associations between social network site experience and privacy disclosing breadth, and between personal social network size privacy disclosing breadth. However, the coefficient of Blog Number in Model 1 is positive and significant, indicating that an increase in the Blog Number by one unit increases Disclosing Breadth by 0.6%.

In Model 2, the coefficient of Gender is also negative and significant, indicating that female users are more likely to disclose privacy in both breadth and depth dimensions. Male users have 19.7% lower Disclosing Depth than female users. We also find a significant relationship between Age and Disclosing Depth, such that the older the user is, the lower the Disclosing Depth is. An increase in the age by one year decreases Disclosing Depth by 2.6%. Further, the coefficient of Blog Number in Model 2 is also positive and significant, indicating that a unit increase in Blog Number is associated with a 0.9% increase in the Disclosing Depth. Account rating, Friend Number and Blog Length are all reported no significant related to Disclosing Depth.

In Model 3, only the coefficient of Blog Number is significant, suggesting a unit increase in Blog Number is associated with a 0.8% increase in High Sensitive Disclosing. This implies that users who are likely to post more blogs on social network sites might disclose more high sensitive information. The results in Model 4 are a little similar to Model 1. Specifically, we find negative and significant coefficients on Gender (-0.168) and Age(-0.041), a positive and significant coefficient (0.006) on Blog Number. Other coefficient estimates on Account rating, Friend Number, and Blog Length are not significant.

Table.3 coefficient estimates on privacy disclosure

<table><tr><td rowspan="2"></td><td colspan="4">Coefficient</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td>Gender</td><td>-0.181***</td><td>-0.197***</td><td>-0.105</td><td>-0.168***</td></tr><tr><td>Age</td><td>-0.043**</td><td>-0.026**</td><td>-0.013</td><td>-0.041**</td></tr><tr><td>AR</td><td>0.069</td><td>0.011</td><td>0.052</td><td>0.057</td></tr><tr><td>FN</td><td>0.004</td><td>0.003</td><td>0.014</td><td>0.004</td></tr><tr><td>BN</td><td>0.006***</td><td>0.009*</td><td>0.008**</td><td>0.006***</td></tr><tr><td>BL</td><td>0.015</td><td>0.020</td><td>-0.002</td><td>0.013</td></tr></table>

Note: \*: p<0.1(2-tailed); \*\*: p<0.05(2-tailed); \*\*\*: p<0.01(2-tailed).

## 4.2 Detailed analysis on disclosing breadth

The data is jointly stratified by gender and age to compare the difference among different groups of users. The detailed analysis results are listed in Table 4. When we use male dataset to test Model 5, the coefficient of Age is negative and significant, suggesting that an increase in the age of male users by one year is associated with a decrease in the Disclosing Breadth of 4.8%. Neither Account rating nor Friend Number is reported being significantly related to Disclosing Breadth. We find a significant relationship between Blog Number and Disclosing Breadth. The coefficient is positive, indicating that the more blogs male users post, the higher Disclosing Breadth they have. Specifically, a unit increase in the number of blogs is associated with a 0.8% increase in the Disclosing Breadth. In contrast, the coefficient of Blog Number is not significant. The difference of using female dataset to test Model 5 is reflected on the coefficients of Age and Friend Number. Firstly, the absolute coefficient of Age is reported larger (-0.051). This implies that female users disclosing breadth has a greater decrease than male users, as people are getting older. Secondly, the coefficient of Friend Number becomes significant, showing that an increase in the number of friends by one is associated with a 0.6% increase in the Disclosing Breadth of female users. This implies that personal social network size has a positive impact on privacy disclosing breadth in female users but no significant impact in male users. Blog Number is also reported a positive and significant coefficient (0.9%).

When younger adults dataset (age<=24) is used to test Model 9, the coefficient of Gender is negative and significant, suggesting that male users have (20.6%) lower Disclosing Breadth than female users. Account rating, Friend Number and Blog Length are all reported being no significantly related to Disclosing Breadth. When we used middle adults (25<age<39) dataset to test Model 9, the results are similar with a slightly change on coefficients of Gender (-0.201) and Blog Length (0.022). The difference appears in older adults (age>=40) dataset. Firstly, the absolute coefficient of Gender is smaller (-0.186), indicating that gender difference of Disclosing Breadth becomes smaller in older people. The coefficient of Account Rating is significant, showing that an increase of Account rating by one unit is associated with an increase of Disclosing Breadth by 7.3%. In addition, the coefficient of Friend Number also becomes significant, showing that an increase in the number of friends by one is associated with a 0.6% increase in the Disclosing Breadth of older users.

Table.4 coefficient estimates for users' privacy disclosure breadth(DB)

<table><tr><td rowspan="2"></td><td colspan="3">Model 5</td><td colspan="2">Model 9</td></tr><tr><td>Male(N=597)</td><td>Female(N=619)</td><td>&lt;24(N=515)</td><td>25-39(N=592)</td><td>&gt;40(N=109)</td></tr><tr><td>Gender</td><td>-</td><td>-</td><td>-0.206***</td><td>-0.201***</td><td>-0.186**</td></tr><tr><td>Age</td><td>-0.048**</td><td>-0.051**</td><td>-</td><td>-</td><td>-</td></tr><tr><td>AR</td><td>0.069</td><td>0.076</td><td>0.070</td><td>0.070</td><td>0.073**</td></tr><tr><td>FN</td><td>0.005</td><td>0.006**</td><td>0.005</td><td>0.005</td><td>0.006*</td></tr><tr><td>BN</td><td>0.008***</td><td>0.009***</td><td>0.009***</td><td>0.009***</td><td>0.004***</td></tr><tr><td>BL</td><td>0.022</td><td>0.021</td><td>0.021</td><td>0.022</td><td>0.022</td></tr></table>

Note: \*: p<0.1(2-tailed); \*\*: p<0.05(2-tailed); \*\*\*: p<0.01(2-tailed).

## 4.3 Detailed analysis on disclosing depth

The coefficient estimates for users' privacy disclosing depth is listed in Table 5. Specifically, when we use male dataset to test Model 6, the coefficient of Age is negative and significant, showing that an increase in the age of male users by one year is associated with a decrease in the privacy Disclosing Depth of 1.7%. Neither Account rating nor Friend Number is reported significant associated with Disclosing Depth. A significant relationship is found between Blog Number and Disclosing Depth. The coefficient is positive, which implies that the more blogs male users post, the higher disclosing depth they have. Specifically, one unit increase in the number of blogs is associated with a 0.7% increase in the Disclosing Depth. In contrast, the coefficient of Blog Number is still not significant. The difference of using female dataset to test Model 6 is reflected on the coefficients of Age, Friend Number and Blog Number. Firstly, the absolute coefficients of both Age and Friend Number are reported larger (-0.034, 0.005). This implies that Age and Blog number have more strong impacts on Disclosing Depth in female users. Secondly, the coefficient of Friend Number becomes significant, showing that an increase in the number of friends by one is associated with a 0.5% increase in the Disclosing Breadth of female users.

When younger adults dataset (age<=24) is used to test Model 10, the coefficient of Gender is negative and significant, suggesting that male users have (24.6%) lower Disclosing Depth than female users. Account rating, Friend Number and Blog Length are all reported being no significantly related to Disclosing Depth. When we used middle adults (25<age<39) dataset to test Model 10, the results are similar with a slightly change on coefficient of Gender(-0.195). The absolute coefficient of Gender is smaller, indicating that the gender difference on Disclosing Depth becomes smaller. When we use older adults (age>=40) dataset to run Model 10, the coefficient of Gender is not significant any longer. The coefficient of Account Rating is positive and significant, showing that an increase of Account rating by one unit is associated with an increase of Disclosing Breadth by 2.7%. In addition, the coefficient of Friend Number is also significant, showing that an increase in the Friend Number by one friend is associated with a 0.5% increase in the Disclosing Breadth of older users. The significant coefficients of other variables are not found.

Table.5 coefficient estimates for users' privacy disclosing depth(DD)

<table><tr><td rowspan="2"></td><td colspan="3">Model 6</td><td colspan="2">Model 10</td></tr><tr><td>Male(N=597)</td><td>Female(N=619)</td><td>&lt;24(N=515)</td><td>25-39(N=592)</td><td>&gt;40(N=109)</td></tr><tr><td>Gender</td><td>-</td><td>-</td><td>-0.246***</td><td>-0.195***</td><td>-0.136</td></tr><tr><td>Age</td><td>-0.017*</td><td>-0.034**</td><td>-</td><td>-</td><td>-</td></tr><tr><td>AR</td><td>0.009</td><td>0.012</td><td>0.009</td><td>0.008</td><td>0.027**</td></tr><tr><td>FN</td><td>0.003</td><td>0.005**</td><td>0.004</td><td>0.004</td><td>0.005*</td></tr><tr><td>BN</td><td>0.007*</td><td>0.010*</td><td>0.007*</td><td>0.007*</td><td>0.010</td></tr><tr><td>BL</td><td>0.015</td><td>0.016</td><td>0.015</td><td>0.014</td><td>0.020</td></tr></table>

Note: \*: p<0.1(2-tailed); \*\*: p<0.05(2-tailed); \*\*\*: p<0.01(2-tailed).

## 4.4 Detailed analysis on high sensitive disclosure

The coefficient estimates for users' high sensitive disclosure is listed in Table 6. When we use male dataset to test Model 7, only the coefficient of Blog Number is significant, suggesting a unit increase in Blog Number is associated with a 0.8% increase in High Sensitive Disclosing. This implies that users who are likely to post more blogs on social network sites might disclose more high sensitive information. When we use female dataset to test Model 7, the results are similar with a little increase in coefficient of Blog Number (0.009). When younger adults dataset (age<=24) is used to test Model 11, only the coefficient of Blog Number is significant. The positive coefficient implies that Blog Number increases High Sensitive Disclosing by 0.8% in younger adults. Almost the same results are reported when we use middle adults dataset (24<age<40) to test Model 11. No significant coefficients are found in model testing when older adults dataset (age>=40) are analyzed.

Table.6 coefficient estimates for users' high sensitive disclosure (HSD)

<table><tr><td rowspan="2"></td><td colspan="3">Model 7</td><td colspan="2">Model 11</td></tr><tr><td>Male(N=597)</td><td>Female(N=619)</td><td>&lt;24(N=515)</td><td>25-39(N=592)</td><td>&gt;40(N=109)</td></tr><tr><td>Gender</td><td>-</td><td>-</td><td>-0.101</td><td>-0.107</td><td>-0.093</td></tr><tr><td>Age</td><td>-0.014</td><td>-0.017</td><td>-</td><td>-</td><td>-</td></tr><tr><td>AR</td><td>0.042</td><td>0.041</td><td>0.039</td><td>0.041</td><td>0.045</td></tr><tr><td>FN</td><td>0.009</td><td>0.014</td><td>0.015</td><td>0.009</td><td>0.005</td></tr><tr><td>BN</td><td>0.008*</td><td>0.009*</td><td>0.010*</td><td>0.009*</td><td>0.006</td></tr><tr><td>BL</td><td>-0.002</td><td>-0.002</td><td>-0.002</td><td>-0.002</td><td>-0.002</td></tr></table>

Note: \*: p<0.1(2-tailed); \*\*: p<0.05(2-tailed); \*\*\*: p<0.01(2-tailed).

## 4.5 Detailed analysis on low sensitive disclosure

The coefficient estimates for users' low sensitive disclosure are listed in Table 7. When we use male dataset to test Model 8, the coefficient of Age is negative and significant (-0.038). We also find a significant relationship between Blog Number and Low Sensitive Disclosure. The coefficient is positive (0.006). The difference of using female dataset to test Model 8 is reflected on the coefficients of Age. The absolute coefficient of Age is reported larger (-0.045). In addition, the coefficient of Friend Number becomes significant (0.5%). When younger adults dataset (age<=24) is used to test Model 12, the coefficient of Gender is negative and significant, suggesting that male users have (16.5%) lower Low Sensitive Disclosure than female users. The coefficient of Blog Number is always positive and significant. When we used middle adults (25<age<39) dataset to test Model 12, the results are similar with a slightly change on coefficients of Gender (-0.163) and Blog Length(0.013). The difference also appears in older adults (age>=40) dataset. Firstly, the absolute coefficient of Gender is smaller (-0.152), indicating that gender difference of Low Sensitive Disclosure becomes smaller in older people. The coefficient of Account rating is significant, showing that an increase of Account rating by one unit is associated with an increase of Low Sensitive Disclosure by 7.1%. The coefficient of Friend Number also becomes significant, showing that an increase in the number of friends by one is associated with a 0.5% increase in the Low Sensitive Disclosure of older users.

Table.7 coefficient estimates for users' low sensitive disclosure (LSD)

<table><tr><td rowspan="2"></td><td colspan="3">Model 8</td><td colspan="2">Model 12</td></tr><tr><td>Male(N=597)</td><td>Female(N=619)</td><td>&lt;24(N=515)</td><td>25-39(N=592)</td><td>&gt;40(N=109)</td></tr><tr><td>Gender</td><td>-</td><td>-</td><td>-0.165***</td><td>-0.163***</td><td>-0.152**</td></tr><tr><td>Age</td><td>-0.038**</td><td>-0.045**</td><td>-</td><td>-</td><td>-</td></tr><tr><td>AR</td><td>0.060</td><td>0.071</td><td>0.056</td><td>0.062</td><td>0.071**</td></tr><tr><td>FN</td><td>0.004</td><td>0.005**</td><td>0.004</td><td>0.004</td><td>0.005*</td></tr><tr><td>BN</td><td>0.006***</td><td>0.006***</td><td>0.006***</td><td>0.006***</td><td>0.004***</td></tr><tr><td>BL</td><td>0.013</td><td>0.012</td><td>0.012</td><td>0.013</td><td>0.013</td></tr></table>

Note: \*: p<0.1(2-tailed); \*\*: p<0.05(2-tailed); \*\*\*: p<0.01(2-tailed).

#

## 5. Discussion

Previous studies suggest that female users are more likely to disclose personal information (Hoy & Milne, 2010; Litt, 2013). This hypothesis has been reexamined in this study. In more details, our results indicate that female users not only disclose privacy information more frequently, but also do this with more sensitive information than male users. In traditional interpersonal and face-to-face contexts, women tend to self-disclose more than men to achieve more intimacy in relationships (Altman, 1973; Petronio, 2002). This rule is also applicable in the SNS context. Our results further show that gender does influence low sensitive disclosure, but has no significant effect on high sensitive disclosure. We also find gender difference on privacy disclosure decreases with regard to the age of users. Gender difference on disclosing depth is even found insignificant in older users.

Our results show that age has a negative association with privacy disclosure in both breadth and depth dimensions. We believe that as people get older, they tend to disclose less sensitive information. In addition, the frequency of disclosing on SNS also becomes less. It is basically consistent with previous studies based on information boundary theory (Litt, 2013). After specific models are tested in users of different genders, age has relatively stronger impacts on privacy disclosure in female users than in male users. Comparing with men, age brings more significant changes in women's mind and psychology (Chakraborty et al., 2013). We think this includes privacy disclosure on SNS. Like gender, age is found no significant association with low sensitive disclosure neither.

Account rating does not affect privacy disclosure significantly in the basic model 1 to 4. However, our results suggest that account rating has significant impacts on disclosing breadth, disclosing depth, and low sensitive disclosure among older users. Among younger people, account rating on social network sites has no significant effect on privacy disclosure, because they have a relatively high account rating. The account rating of older users is relatively lower than younger users. Older users' account rating much more truly reflects the time they spent on posting, modifying, and reading blogs. This might well explain why account rating is reported having significant impacts on disclosing breadth, disclosing depth, and low sensitive disclosure among older adults.

Personal social network size has been identified as a factor that affects users' information disclosure. In this study, the effects are only significant in female users and older users. In former literature, female were found more careful in adding strangers as new friends and also more likely to manage their friends than males on social network sites (Litt, 2013). In this way, we expect the higher quality of female users' social network than that of male users. Therefore, female users personal social network size on social networks should be more reflective to their social communication needs, which motivates them to disclose more information on social network sites. Similarly, older users hardly add strangers as their friends on social network sites (Chakraborty et al., 2013). Just like female users, their social network size truly reflects of their social communication needs. Blog number is always reported having positive associations with privacy disclosure. It is intuitive because posting more blogs on social network sites means more privacy information might be disclosed. Interestingly, there is no significant association between blog length and privacy disclosure. In reality, neither too short nor too long blog postings might not contain much privacy information. Short blogs (microblog) usually contain a few words. Long blogs probably are reproduced from other people's articles or blogs. We guess that a convex relationship might exist between blog length and privacy disclosure.

From the perspective of all variables' effects, there are few differences between disclosing breadth (Model 1) and disclosing depth (Model 2). However, if we compare low sensitive disclosure (Model 3) with high sensitive disclosure (Model 4), the results are quite different. While Gender, Age and Blog Number are all significantly related to Low Sensitive Disclosure, only Blog Number has a significant associate with High Sensitive Disclosure. This implies us that people act quite differently according to different levels of information sensitivity when they are facing a privacy disclosure decision. Information sensitivity actually plays a more important role on peoples information disclosure (Malhotra et al., 2004; Bansal et al., 2010). Additionally, the results related to low sensitive disclosure in model 3 are almost no significant in this study. It seems like that users do not care much about less sensitive information like hobbies, preference. We believe this is related to certain culture, since the research data is collected in China. China has a relatively collectivist culture (Su, 2013), which affects people's boundary. Some less sensitive information might not be considered as privacy and habitually shared with other people in the country versus other individualist cultures such as America or Europe.

## 6. Implications for theory and practice

From a theoretical perspective, the findings of this study have a number of implications for researchers:

Firstly, Some core criteria in CPM theory which were tested in previous research (Dindia and Allen, 1992) in traditional face-to-face communication contexts have been reexamined in this study. Our results, consistent with previous findings, indicate gender differences and age have their strong links with privacy disclosure patterns in the SNS context. Furthermore, some new criteria under the SNS context such as social network experience and personal social network size have been introduced and tested.

Secondly, previous research about privacy disclosure has focused more on intention and willingness to a designated action (Xu et al., 2012). People's intentions lead to their behaviors but are not the actual behaviors. Sometimes high intentions result in low levels of behaviors, while low intentions might cause highly active behaviors. These have been found in many previous IS studies (Norberg et al., 2007). In this study, practical data collected from a real social network site helps us study privacy disclosure behaviors, which can be identified by analyzing privacy disclosure patterns. This paper contributes theoretically by quantifying the scope of privacy disclosure into disclosing breadth and depth, and distinguishing high sensitive disclosure and low sensitive disclosure in the empirical analysis according the frequencies of high/low sensitivity of disclosed information. Specification and classification of privacy disclosure help us to investigate in more detail about users' privacy disclosure on social network sites.

From a managerial perspective, the findings of this study provide meaningful implications for SNS providers:

Firstly, the GLM models in this study clarify the associations between several predictors and users' privacy disclosure patterns. This implies that SNS providers can build their own forecasting models for users' privacy disclosure behaviors. Forecasting models can be embedded to help SNS providers to design more effective privacy management tools on their social network sites.

Secondly, detailed empirical tests among different populations have been finished in this paper. This can help SNS providers to formulate different kinds of alerts and business rules for diversified groups of users.

## 7. Conclusion

Since social media are characterized by vast volumes of user-contributed contents, navigating these contents is a significant research challenge (Abrahams et al., 2013). In this paper, we examine the different impacts of demographics, social network site experience, personal social network size, and blogging productivity on users' privacy disclosure patterns on social networking sites. Two dimensions of privacy disclosure scope, breadth and depth, are defined in the study. From the perspective of information sensitivity, low sensitive disclosure, and high sensitive disclosure are also distinguished. Data is stratified based on age and gender in the empirical analysis to compare the differentiated effects on different groups of users. Twelve generalized linear models in three groups are tested with several important findings.

We find there are significant gender differences on both disclosing breadth and depth. Female users are more likely to disclose privacy information than male on social network sites. Like many previous studies (Litt, 2013), age has a negative impact on privacy disclosure in this study. Significant effects are found on both disclosing breadth and depth. Neither social network site experience nor personal social network size is tested significantly related to users' privacy disclosure in basic models. But in some certain groups of users like female and older users, significant relationships can be supported.

Several limits are detectable in this study. First of all, the categories of privacy information are still under debate. Some kinds of personal information that are mentioned in literature were not identified and coded into privacy disclosure variables, such as attitude, location, medications, social issue opinions and so on(Norberg and Dholakia, 2004; Norberg et al. 2007). The data used in the empirical study are collected from one social network sites. We did not use data from other social network sites to do further robustness test.

While this study introduces gender, age, social network experience, personal social network size, blog number and blog length into the analysis model of users' privacy disclosure, future research will need to consider more factors and elements to explain why people disclose privacy information on social network sites. Technological skill, like privacy tool use (Litt, 2012), and social skills, like self-monitoring ability (Child & Agyeman-Budu, 2010) can all be involved in future study. According to CPM theory, culture is a very important privacy rule criterion. Disclosure depends on the norms for privacy and openness in a given culture (Petronio, 1991). Therefore, cross-culture study is also quite essential in the future.

## Acknowledgement

The authors are very grateful to the associate editor, guest editor and two anonymous reviewers for their constructive advice. This study is partially supported by the National Science Foundation of China(71302017).

## References

[1] A.S. Abrahams, J. Jiao, G. A. Wang, W. Fan, Vehicle defect discovery from social media, Decision Support Systems. (54) (1) (2012) 87-97.

[2] A.S. Abrahams, J. Jiao, W. Fan, G. A. Wang, Z. Zhang, What is buzzing in the blizzard of buzz: automotive component isolation in social media postings, Decision Support Systems. (55) (4) (2013) 871-882.

[3] A. Acquisti, J. Grossklags, Losses, Gains, Hyperbolic Discounting: An Experimental Approach to Information Security Attitudes and Behavior. In: Proceedings of the 2nd Annual Workshop on Economics and Information Security, UCBerkeley, Berkeley, CA, 2003.

[4] I. Altman, D. A. Taylor, Social penetration: The development of interpersonal relationships. New York: Holt, Rinehart & Winston, 1973.

[5] N.F. Awad, M.S. Krishnan, The personalization privacy paradox: an empirical evaluation of information transparency and the willingness to be profiled online for personalization, MIS Quarterly. (30) (1) (2006) 13-28.

[6] G. Bansal, F. M. Zahedi, & D. Gefen, The impact of personal dispositions on information sensitivity, privacy concern and trust in disclosing health information online, Decision Support Systems. (49) (2) (2010) 138-150.

[7] F. Bélanger, R.E. Crossler, Privacy in the digital age: a review of information privacy research in information systems, MIS Quarterly. (35) (2011) 1017-1041.

[8] F. Bélanger, J.S. Hiller, W.J. Smith, Trust worthiness in electronic commerce: the role of privacy, security, and site attributes, Journal of Strategic Information Systems. (11) (2002) 245-270.

[9] H. Bonfadelli, The Internet and knowledge gaps: A theoretical and empirical investigation, European Journal of Communication. (17) (2002) 65-84.J. Brenner, A. Smith, 72% of online adults are social networking site users. <http://www.pewinternet.org/\~/media//Files/Reports/2013/PIP\_Social\_networking\_sites\_upd ate.pdf> (Accessed 9.10.13).

[10] J. Bryce, M. Klang, Young people, disclosure of personal information and online privacy: Control, choice and consequences, Information security technical report. (14) (2009) 160-166.

[11] R. Chakraborty, C. Vishik, H. R. Rao, Privacy preserving actions of older adults on social media: Exploring the behavior of opting out of information sharing, Decision Support Systems. (55) (2013) 948-956.

[12] J.T. Child, & E.A. Agyeman-Budu, Blogging privacy management rule development: The impact of self-monitoring skills,concern for appropriateness, and blogging frequency, Computers in Human Behavior. (26) (5) (2010) 957-963.

[13] L. F. Cranor, Internet Privacy, Communications of the ACM. (42) (2) (1999) 28-31.

[14] M.J. Culnan, P.K. Armstrong, Information privacy concerns, procedural fairness, and impersonal trust: an empirical investigation, Organization Science. (10) (1) (1999) 104-115.

[15] S. G. Davies, Re-engineering the right to privacy: how privacy has been transformed from a right to a commodity, in technology and privacy: the new landscape, P. E. Agre and M. Rotenberg (eds.), Cambridge, MA: MIT Press, 1997, 143-165.

[16] K. Dindia, M. Allen, Sex differences in self-disclosure: Ameta-analysis. Psychological Bulletin. (112) (1) (1992) 106-124.

[17] T. Dinev, P. Hart, An extended privacy calculus model for e-commerce transactions, Information Systems Research. (17) (2006) 61-80.

[18] N.B. Ellison, C. Steinfield, C. Lampe, The benefits of Facebook ‘‘friends’’: social capital and college students’ use of online social network sites, J. Comput. - Mediat. Commun. (12) (2007) 1143–1168.

[19] W. Fan, M.D. Gordon, The power of social media analytics, Communications of the ACM. (57) (6), (2014) 74-81.

[20] H. Jr. Gandey, Exploring identity and identification in cyberspace, Notre Dame Journal of Law, Ethics and Public Policy. (14) (2000) 1085-1111.

[21] R. Gross, A. Acquisti, Information revelation and privacy in online social networks, Proceedings of the 2005 ACM workshop on Privacy in the electronic society. ACM, (2005) 71-80.

[22] W. Hong, J.Y. L. Thong, Internet privacy concerns: an integrated conceptualization and four empirical studies, MIS Quarterly. (37) (1) (2013) 275-298.

[23] M.G. Hoy, G. Milne, Gender differences in privacy-related measures for young adult Facebook users. Journal of Interactive Advertising. (10) (2) (2010) 22-45.

[24] M. Igbaria, T. Guimaraes, G.B. Davis, Testing the Determinants of Microcomputer Usage via a Structural Equation Model, Journal of Management Information Systems. (11) (4) (1995) 87-114.

[25] M. Igbaria, S. Parasuraman, J.J. Baroudi, A Motivational Model of Microcomputer Usage, Journal of Management Information Systems. (13) (1) (1996) 127-143.

[26] N. Joinson, C. B. Paine, Self-disclosure, privacy and the Internet, In A. Joinson, K. McKenna, S.M. Jourard, Self-Disclosure: An Experimental Analysis of the Transparent Self. Wiley, New York, 1971.

[27] W.J. Kettinger, V. Grover, the Use of Computer-Mediated Communication in an Organizational Context, Decision Sciences. (28) (3) (1997) 513-555.

[28] A. Kobsa, Privacy-Enhanced Personalization, Communications of the ACM. (50) (8) (2007) 24-33.

[29] M. C. Lacity, L. P.Willcocks, An empirical investigation of information technology sourcing practices: Lessons from experience, MIS Quarterly. (22) (3) (1998) 363-408.

[30] R.S. Laufer, M. Wolfe, Privacy as a concept and a social issue: a multidimensional development theory, Journal of Social Issues. (33) (3) (1977) 23-42.

[31] K. Lewis, J. Kaufman, & N. Christakis, The taste for privacy:An analysis of college student privacy settings in an online social network, Journal of Computer-Mediated Communication. (14) (2008) 79-100.

[32] Y. Li, The impact of disposition to privacy, website reputation and website familiarity on information privacy concerns, Decision Support Systems. (57) (1) (2014) 343-354.

[33] N. Li, D.D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support Systems. (48) (2) (2010) 354-368.

[34] H. Lin, W. Fan, P. Chau, Determinants of users' continuance of social networking sites: A self-regulation perspective, Information and Management. (51) (5) (2014) 595-603.

[35] E. Litt, Understanding social network site users’ privacy tool use, Computers in Human Behavior. (29) (2013) 1649-1656.

[36] S. Livingstone, Taking risky opportunities in the creation of youthful content creation: teenagers’ use of social networking sites for intimacy, privacy and self-expression, New Media and Society (10) (3) (2008) 393-411.

[37] N.K. Malhotra, S.S. Kim, J. Agarwal, Internet Users' Information Privacy Concerns (IUIPC): the construct, the scale, and a causal model, Information Systems Research. (15) (4) (2004) 336-355.

[38] S.T. Margulis, On the status and contribution of Westin's and Altman's theories of privacy, Journal of Social Issues. (59) (2) (2003) 411-429.

[39] R. O. Mason, Four Ethical Issues of the Information Age, MIS Quarterly. (10) (1) (1986) 4-12.

[40] M. J. Metzger, Effects of diet, vendor, and consumer characteristics on website trust and disclosure, Communication Research. (33) (3) (2006) 155-179.

[41] G.R. Milne, Consumer participation in mailing lists: a field experiment, Journal of Public Policy & Marketing. (16) (2) (1997) 298-309.

[42] J.A. Nelder, R.W.M. Wedderburn, Generalized linear models, Journal of the Royal Statistical Society Series A (General). (135) (1972) 370-384.

[43] R.R. Nelson, P.H. Cheney, Training End Users: An Exploratory Study, MIS Quarterly. (11)(4) (1997) 547-559.

[44] P. A. Norberg, R.R. Dholakia, Customization, information provision and choice: what are we willing to give up for personal service? Telematics and Informatics. (21) (2) (2004) 143-155.

[45] P. A. Norberg, D.R. Horne, D.A. Horne, The privacy paradox: personal information disclosure intentions versus behaviors, The Journal of Consumer Affairs. (41) (2007) 100-126.

[46] G.J. Nowak, J. Phelps, Direct marketing and the use of individual-level consumer information: determining how and when ‘privacy’ matters, Journal of Direct Marketing. (9) (3) (1995) 46-60.

[47] M. Parameswaran, A.B. Whinston, Research issues in social computing, Journal of the Association for Information Systems. 8 (6) (2007) 336-350.

[48] Y.J. Park, Digital literacy and privacy behavior online, Communication Research. (40) (2) (2011) 215-236.

[49] P.A. Pavlou, State of the information privacy literature: where are we now and where should we go? MIS Quarterly. (35) (4) (2011) 977-988.

[50] S. Petronio, Boundaries of privacy: Dialectics of disclosure. Albany, NY: State University of New York Press, 2002.

[51] S. Petronio, Communication boundary management: A theoretical model of managing disclosure of private information between married couples, Communication Theory. (1) (1991) 311-335.

[52] S. Petronio, Translational Research Endeavors and the Practices of Communication Privacy Management, Journal of Applied Communication Research. (35) (2007) 218-222.

[53] J. E. Phelps, G. Nowak, E. Ferrell, Privacy Concerns and Consumer Willingness to Provide

Personal Information, Journal of Public Policy and Marketing. (19) (1) (2000) 27-41.

[54] K.S. Schwaig, A.H. Segars, V. Grover, K.D. Fiedler, A model of consumers' perceptions of the invasion of information privacy Information & Management. (50) (2013) 1-12.

[55] K.B. Sheehan, An investigation of gender differences in online privacy concerns and resultant behaviors, Journal of Interactive Marketing. (13) (4) (1999) 24-38.

[56] K.B. Sheehan, M.G. Hoy, Dimensions of privacy concern among online consumers, Journal of Public Policy & Marketing. (19) (1) (2000) 62-73.

[57] H. J. Smith, Managing Privacy: Information Technology and Corporate America, Chapel Hill, NC: University of North Carolina Press, 1994.

[58] H.J. Smith, T. Dinev, H. Xu, Information privacy research: an interdisciplinary review, MIS Quarterly. (35) (4) (2011) 989–1015.

[59] H.J. Smith, S.J. Milberg, S.J. Burke, Information privacy: measuring individuals' concerns about organizational practices, MIS Quarterly. (20) (2) (1996) 167-196.

[60] E.F. Stone, D.L. Stone, Privacy in organizations: theoretical issues, research findings, and protection mechanisms, Research in Personnel and Human Resources Management. (8) (1990) 349-411, K. M. Rowland and G. R. Ferris (Eds.), JAI Press, Greenwich, CT.

[61] N, Su. Internationalization strategies of Chinese IT service suppliers, MIS Quarterly. (37) (1) (2013) 175-200.

[62] J.Sutanto, E. Palme, C.Tan, C.W. Phang. Addressing the personalization–privacy paradox: an empirical assessment from a field experiment on smartphone users, MIS Quarterly. (37) (4) (2013) 1141-1164.

[63] S. Taddei, B. Contena. Privacy, trust and control: Which relationships with online self-disclosure? Computers in Human Behavior. (29) (3) (2013) 821-826.

[64] R.L. Thompson, C.A. Higgins, J.M. Howell, Influence of Experience on Personal Computer Utilization: Testing a Conceptual Model, Journal of Management Information Systems. (11) (1) (1994) 167-187.

[65] B.E. Tolstedt, J.P. Stokes, Self-disclosure, Intimacy, and the Depenetration Process, Journal of Personality and Social Psychology. (46) (1) (1984) 84-90.

[66] G. A. Wang, J. Jiao, A. S. Abrahams, W. Fan, Z. Zhang, ExpertRank: A topic-aware expert finding algorithm for online knowledge communities, Decision Support Systems. (54) (3) (2013) 1442-1451.

[67] A.F. Westin, Privacy and Freedom, Athenaeum, New York, 1967.L. R. Wheeless, J. Grotz, Conceptualization and measurement of reported self-disclosure. Human Communication Research. (2) (4) (1976) 338-346.

[68] H. Xu, X.R. Luo, J.M. Carroll, M.B. Rosson, The personalization privacy paradox: an exploratory study of decision making process for location-aware marketing, Decision Support Systems. (51) (1) (2011) 42-52.

[69] D. Zeng, H. Chen, R. Lusch, S.H. Li, Social media analytics and intelligence, IEEE Intelligent Systems. (November/December) (2010) 13-16.

[70] T. Zhou, H. Li, Understanding mobile SNS continuance usage in China from the perspectives of social influence and privacy concern, Computers in Human Behavior. (37) (1) (2014) 283-289.

[71] M. Zhou, L. Lei, J. Wang, G. A. Wang, W. Fan, Social media adoption and corporate disclosure, Journal of Information Systems, forthcoming, 2014.
