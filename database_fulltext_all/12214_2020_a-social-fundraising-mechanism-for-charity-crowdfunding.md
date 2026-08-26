---
otero_id: 12214
otero_key: "5U2XWJRN"
title: "A social fundraising mechanism for charity crowdfunding"
authors: "Yung-Ming Li; Jhih-Dong Wu; Chin-Yu Hsieh; Jyh-Hwa Liou"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113170"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

## A social fundraising mechanism for charity crowdfunding

Yung-Ming Li, Jhih-Dong Wu, Chin-Yu Hsieh, Jyh-Hwa Liou

![](/api/attachments/5U2XWJRN/fulltext/images/4a310a366268fa43d719491a2ac50cf5bef8f097ffe8cc5dad46df3aec74a698.jpg)

PII: S0167-9236(19)30199-X

DOI: https://doi.org/10.1016/j.dss.2019.113170

Reference: DECSUP 113170

To appear in: Decision Support Systems

Received date: 22 March 2019

Revised date: 11 October 2019

Accepted date: 11 October 2019

Please cite this article as: Y.-M. Li, J.-D. Wu, C.-Y. Hsieh, et al., A social fundraising mechanism for charity crowdfunding, Decision Support Systems (2018), https://doi.org/ 10.1016/j.dss.2019.113170

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2018 Published by Elsevier.

# A Social Fundraising Mechanism for Charity Crowdfunding

Yung-Ming Li • Jhih-Dong Wu • Chin-Yu Hsieh • Jyh-Hwa Liou

Institute of Information Management, National Chiao Tung University, Hsinchu, 300, Taiwan yml@mail.nctu.edu.tw • azuma.iim03g@nctu.edu.tw • hsieh.chinyu@gmail.com • alioujh@gmail.com

## Abstract

In recent years, as the world has witnessed many social issues and environmental disasters, philanthropic giving has become widespread. Today, crowdfunding platforms have also become popular, and charities often use these to fundraise. However, they rarely utilize the power of social networking to assist a fundraiser in discovering potential donors, and this is especially true for small organizations and individuals. In this research, we propose a recommendation mechanism for social fundraising that analyzes the donor’s preferences, the relationship between the donor and fundraiser, and the characteristics of the fundraising dynamics to promote the spread of philanthropic fundraising. The proposed mechanism can effectively discover appropriate donors and relevant campaigns to expedite the fundraising process and improve its success rate.

Keywords: Crowdfunding, Philanthropy, Social networking, Social fundraising, Social recommendations

## 1 Introduction

In recent years, the world has seen many social issues and environmental disasters, some caused by anthropogenic impacts on the environment. It is often necessary to raise a vast amount of money to try to mitigate the suffering of the victims. In the past, fundraising campaigns were held on the ground, which could attract new supporters, communicate the idea or mission of the organization, and even maintain the relationships between current supporters [61]. However, unlike large organizations, it is not easy for small organizations or individuals to do this, due to insufficient resources and the effort and experience required. In addition, physical fundraising campaigns tend to be limited to a specific local place.

Recently, varieties of crowdfunding models have emerged, such as lending, equity, reward-based, and donation-based crowdfunding. Online social fundraising is a type of donation-based crowdfunding that utilizes the Internet to raise funds from enormous numbers of individuals giving small amounts of money, and to promote these fundraising activities through social networking activity. Social fundraising is gradually becoming an important funding channel for the younger generation, and this area is still growing [7, 16]. A number of popular platforms such as GlobalGiving, CrowdRise, and GoFundMe have emerged. CrowdRise is a popular fundraising platform for charitable and personal causes, and over 1.5 million charities use it to raise funds. DonorsChoose is a nonprofit crowdfunding platform for education that has a potential online charity market of \$30 billion a year, with the possibility of becoming \$70 billion [55].

To improve the success of social fundraising activities, platforms use gamification and rewards systems to induce users to participate in fundraising activities. For example, in the CrowdRise platform, users can earn CrowdRise Impact Points (CIPs), which represent the charitable donation process, such as raising money or donating to a fundraiser. CIPs can also be redeemed for items such as hoodies and tees. Although the current fundraising platforms provide new opportunities, most crowd-based fundraising activities still face problems with inefficiency. Charity fundraising platforms still lack an efficient way to discover potential donors. Even experienced fundraisers sometimes have difficulty in soliciting funds [13]. Thus, the issue of how to help fundraisers who lack experience in fundraising to overcome this difficulty has become important. It would be helpful to support fundraisers and charitable activities with recommendations of appropriate potential donors. Activities on social media provide plentiful clues that can be used to analyze personal preferences and social relationships [36, 43, 48, 50, 53,58], and these are key factors in finding relevant donors with suitable preferences and close relationships [34].

Most recent recommendation systems in crowdfunding were developed for reward-based campaigns [12, 54, 62, 63], which cannot be fittingly applicable to charity crowdfunding. The purpose of this research is to propose a social fundraising recommendation mechanism based on ways in which fundraisers can effectively discover suitable donors and take advantage of their experience in

(1) How can we help a fundraiser to reduce the experience requirements for fundraising and

Soliciting funds is not easy without experience. Although online fundraising minimizes the entry barriers to fundraisers, current platforms do not provide an effective approach to reduce the experience required of a fundraiser. Building a fundraising recommendation system is an excellent way to support fundraisers in targeting suitable donors, and can help donors to participate in charitable fundraising.

(2) How can we identify appropriate donors who are interested in the campaign, based on their behaviors?

In the past, it has not been easy to understand personal preference. However, nowadays, we can collect and analyze personal behaviors from social media and infer preferences from enormous amounts of social interaction data, such as comments, likes, shares of an article, or check-ins. We utilize the data of social activities and historical donation activities to infer the fundraising themes that potential donors prefer.

(3) How can we build trust between a potential donor and a fundraiser using the power of social media?

Fundraising from friends is generally easier than from strangers. A donor’s social relationship with fundraisers is an important factor in evaluating the willingness to be a donor. In the real world, it is difficult to observe the relationship between two persons, but with social networking data, this relationship can be examined and measured.

In this research, we utilize social networks to propose a charity fundraising recommendation mechanism that tries to match a fundraiser with potential donors by analyzing the major factors affecting user preferences and the social relationship between fundraisers and donors. The proposed mechanism provides effective evaluation and matching of both types of participants in social funding activities. We aim to assist a fundraiser in solicitation activities by reducing the entry barrier to donor discovery; at the same time, donors can discover a campaign they may be interested in more rapidly. problem via improvements to the fundraising process, such that fundraisers can more efficiently find potential donors, and donors can easily find suitable campaigns without time-consuming effort.

The remainder of the paper is structured as follows: Section 2 reviews the literature related to our research. The proposed mechanism is presented in Section 3. The experiments conducted on the proposed mechanism are discussed in Section 4. The results of the experiments and an evaluation are presented in Section 5. Finally, Section 6 concludes our research contributions and describes the

## 2 Related literature

## 2.1 Crowdfunding and philanthropic fundraising

Crowdfunding comes from the concept of crowdsourcing, which involves using the vast potential of contributors to obtain informational products or services via the Web [18]. Crowdfunding is defined as an entrepreneur or individual using the Internet to receive funding from a large crowd of individuals each providing small amounts [6]. Crowdfunding takes different forms, such as reward-based, equity-based, lending-based, and donation-based (charity-based) [31]. Reward-based crowdfunding allows funders as early customers to receive a reward or benefit for their backing. Equity-based crowdfunding is similar to the relationship of the entrepreneur-investor who receives equity stakes in return for his or her financial investment. Lending-based crowdfunding follows the relationship of debtor and lender with some rate of return. Reward, equity, and lending crowdfunding all include the idea of monetary exchange. In donation-based crowdfunding, supporters act as philanthropists who do not expect return [40].

The majority of recent crowdfunding studies focus on reward-based crowdfunding [12, 54, 62, 63]. In reward-based crowdfunding, the main motivation of a backer is the desire to collect a reward delivered [12]. The project characteristics of venture status and promised lead time affect the delivery performance [54]. Popular reward-based crowdfunding platforms such as Kickstarter adopt an all-or-nothing policy to enhance the success of project realization and delivery, which is not suitable to charity-based crowdfunding projects needing emergency support or seeking to resolve social issues. Many charity-based crowdfunding platforms, such as CrowdRise and GlobalGiving operate under the rule of keep-it-all. The donor’s motivations in charity-based crowdfunding include intrinsic motivations such as personal interest, beliefs, empathy, social influences, and social trust, as well as extrinsic motivations such as improving social problems and knowledge [4]. Donors’ intentions arise both from traditional empathy, but are also influenced by the credibility of the recipient (reputation of initiator, popularity of project, and project content quality) [33]. While recipients are not passively waiting for donations, but try to raise the popularity of their project through social media platforms.

The social aspects of charity-based crowdfunding are important and have been explored in several studies [4, 9, 21]. For example, analyzing behavioral events relating to donation recurrence and donation recurrence with data collected from Kiva.org, [67] found that donors’ profiles and motives, and social contact-teams have great impact on donation behavior. [21] also supported a positive association between donations to fundraisers and the richness of social interaction. A donor is more likely to trust a recipient if social media are used to solicit activities [41]. However, many nonprofit organizations have not made effective use of social media for fundraising due to limitations on resources [59, 60]. Recently, crowdfunding platforms have begun to facilitate mass participation in fundraising activities, and allow individuals to become fundraisers even with no fundraising experience. Nevertheless, existing social fundraising platforms lack an effective approach for disseminating campaigns, and provide only passive approaches to fundraisers, such as sending an e-mail or sharing a link [10]. In this research, analyzing the activities on social media and social fundraising platforms, we propose an integrated mechanism matching donors and fundraisers, which

can expedite the fundraising process.

## 2.2 Recommendation systems in crowdfunding

The major goal of recommendation systems is to analyze users’ behaviors to suggest suitable content (or items) to a specific user. Personalized recommendations can increase user satisfaction [44]. Recommendation systems can be classified into four types: content-based, collaborative filtering, association rule, and hybrid (a combination of content-based and collaborative filtering). Content-based recommendation systems infer a user’s preferences based on items purchased or previously used and recommend new items with some similarity [5, 45]. Collaborative filtering recommendation considers the similarity between a target user and a like-minded user. It uses the preferences of like-minded users to infer the target user’s preferences, which are not explicitly known [30, 42]. Association rule-based recommendation considers a sequence of items to predict the target user’s behavioral patterns [1, 32]. This approach straightforwardly mines the target user’s behavior; however, it has certain drawbacks, such as the extraction of non-interesting rules, large numbers of discovered rules, and performance issues [17, 51]. The hybrid recommendation approach makes predictions based on a weighted combination of content-based and collaborative filtering recommendation [8].

Recently, the majority of existing recommendation systems in crowdfunding are developed for decision support of reward-based campaigns [2, 19, 46]. For example, [46] recommends projects to a group of investors by incorporating a set of features, such as topical preference, geo-location, temporal information, and social network links measured by the interacting messages and link structure of investors on the Twitter platform. [2] compares different statistical and machine learning models for recommending potential investors from among Twitter users for specific projects, analyzing the number of Tweets, the number of followers, and project profile and status. [19] collects multi-data to build a recommendation module that includes campaign data from Kickstarter, user data from profile pages, and social data, but which merely includes the number of social media accounts or links for the creator’s social activity.

For reward based crowdfunding, project completion and the tangible reward are the concerns of a backer, which might not be aligned with the motivation of a charity donor. A donor selects a project with more consideration of the charity characteristics and social relationship with the fundraiser than the fundraising status of project. Furthermore, studies show that a donor is influenced by peers, such as family or friends, who consequently affect his or her decision to donate [39, 41]. Existing crowdfunding recommendation systems cannot satisfactorily support charity fundraising activities, due to a lack of detailed consideration of a donor’s social motivations [7, 52]. Our proposed recommendation system utilizes and integrates various types of activity information from social media and charity fundraising platforms to identify the motivations of donors and thus to discover appropriate donors from a set of people and recommending interesting campaigns to donors. With this support, fundraisers can more easily solicit fundraising activities and can therefore pay more attention to their primary philanthropic mission.

## 2.3 Social networking and relationships

A social network is a space that everyone can use to create, share, and exchange opinions through the Internet. Hence, social networks can disseminate information not only within a small social circle but also to a large network of people, due to the ‘small world’ phenomenon [23]. The first social networking website that can be identified was SixDegrees.com, named for the ‘six degrees of separation’, which was established in 1997 [15]. Following this, more successful social networking sites (e.g. LinkedIn, Facebook, and Twitter) were developed. Today, social media are popular and important channels from many perspectives, such as marketing, politics, and philanthropy [37, 41, 49].

In the social networking space, each person links or interacts with others, forming a huge graph of connections of different relationships. We can extract implicit information about personal details, social relationships, and social intelligence [58]. Triadic closure is an approach that aims to simplify a huge social network using three nodes, allowing us to understand and predict these networks [14, 35]. There are two distinct types of edge, which are based on the strength of a relationship. The first type involves strong ties, meaning the participants have a high level of trust in each other; in real-world terms, these are family or friend relationships. The other type involves weak ties, indicating a more distant relationship; these participants do not have a high level of trust, such as strangers or friends of friends [20]. The property of strong triadic closure states that if one user knows a second user who has a friend in common with both of them, the first user will eventually become a friend of this third user. “Mutual friends” therefore become a factor that can be used to measure the similarity of interests and the closeness of relationships. We can therefore expect that the more friends of a particular user are participating in an activity (e.g. donating to a charity), the more willing he/she will be to participate in the same activity.

Recently, with the widespread use of mobile devices, increasing numbers of people are using information from social media such as LinkedIn, Facebook, and Twitter to make decisions [65]. Social media form a novel communication channel for fundraising and can also maintain the relationships between donors within nonprofit organizations [24, 47]. The impact of social factors on reward-based crowdfunding was investigated in some works [38, 68]. As a donor’s giving for charity is not for the tangible reward from a completed project, he/she tends to select a fundraiser with a strong relationship. The social motivation of charity-based crowdfunding needs elaborated measurement [4, 21].

Most studies on crowdfunding are conducted by analyzing the Twitter data and corresponding reward-based projects’ profiles [2, 38]. However, due to the limitation of the Tweet dataset, social activities obtainable in these works are not comprehensive for a detailed analysis. Of the various types for decision support due to the numerous connections and relationships involved [26, 40]. Hence, our proposed recommendation mechanism uses the Facebook platform as its social media source. In the proposed mechanism, by analyzing the social activities and fundraising activities in Facebook and charity crowdfunding platforms, we infer a user’s preference, the relationship between a fundraiser and a donor, as well as the social influence from friends to enhance the performance of charity fundraising recommendations.

## 3 The system framework

We develop a social fundraising recommendation mechanism that can discover donors with higher willingness and trust through social networks and fundraising platforms. We aim to improve the efficiency of social fundraising, especially in terms of the discovery of donors. Furthermore, the proposed mechanism not only makes recommendations for fundraisers but also for donors; in other words, the proposed mechanism is designed to support both the donor in discovering campaigns and the fundraiser in discovering donors. Fig. 1 illustrates the processes in our proposed mechanism, and these can be described as follows:

![](/api/attachments/5U2XWJRN/fulltext/images/275b126e82292d785ed60ca726b62ae5b5b023a829708b2a3a9bc7fec764c263.jpg)  
Fig. 1. The processes in the proposed mechanism

(1) First, our proposed mechanism distinguishes between two types of users (i.e. fundraisers and donors). A fundraiser wants to discover potential donors, while a donor wants to find interesting campaigns. Both types of user can use the proposed mechanism for support in achieving their goals.

(2) We then collect and calculate the user’s preferences and his or her relationships in the social network. From the perspective of a fundraiser, we carry out relationship analysis based on the fundraiser’s social media profile and generat e a list of candidate donors by performing preference analysis. From the perspective of a donor, we carry out these analyses by following the reverse flows to generate a list of relevant campaigns.

(3) Next, we collect information about donations to campaigns from the fundraising platforms and calculate the frequency of campaign updates. The more interesting campaigns are provided to the requesting donor, and thus the fundraiser can discover more suitable donors.

(4) Finally, we consolidate the above analyses using appropriate weights to generate a list of top-k targets. We present a fundraiser with a list of donors, while a donor will receive a list of campaigns.

The system architecture is shown in Fig. 2.

![](/api/attachments/5U2XWJRN/fulltext/images/3c2a546488b2e46f771d22ced0b62f590f2aec3ec2709e9b4fa60ad4b2d6ad0a.jpg)  
Fig. 2. Framework of the proposed system

There are five main modules in our system, as follows:

(1) ThemeTree construction: We construct a hierarchical structure to classify the project, which is drawn from several different charity fundraising platforms. The classified results are used to identify the preferences of participants (fundraisers and donors) based on their social network profiles and the fundraising platforms.

(2) Formation of the execution plan: The proposed system provides bidirectional recommendations for donors and fundraisers. A social fundraising recommendation list (i.e. a donor or campaign list) is provided based on the role of the requesting user.

(3) Fundraising participants analysis module: In this module, we focus on calculating the fundraising preferences of the participants and their relationships. In donor preference analysis, we analyze the donor’s giving behavior and their individual preferences to identify the type of donor. We also infer the donor’s preferences from their activities on social media. Finally, we compute the donor-campaign similarity to select appropriate donors and relevant campaigns. In fundraiser-donor relationship analysis, we evaluate the fundraiser-donor relationship by computing their social interactions and social closeness.

(4) Fundraising campaign analysis module: In this module, we compute three measures for a given fundraising campaign. The campaign donation similarity represents the similarity between the target donor’s friends and the campaign donation list. The campaign donation interaction represents the interaction between the target donor and the campaign donation list. The campaign frequency indicates the intensity of a fundraiser’s intention to communicate with the donor.

(5) Fundraising recommendation engine module: In this module, we aggregate the results from the above analysis modules, and generate the list of top-k donors (campaigns) for the fundraiser (donor) according to the role of the requesting user.

## 3.1 ThemeTree construction

Tree structure can be effectively used to portray user preference. We built a ThemeTree to analyze the preference of a donor. The first step is to construct the ThemeTree, which is used to match the user’s preference with the campaign theme. The ThemeTree is a three-layer tree structure. The first layer is the root layer; the second contains the theme names, which are collected from charity fundraising platforms, GlobalGiving and CrowdRise; while the third contains the leaf nodes, which include the preference types classified using Facebook. Part of a ThemeTree is illustrated in Fig. 3.

![](/api/attachments/5U2XWJRN/fulltext/images/6c4156510a2daaa8f4a2bbf5bcb42f18f00aa5946f5e83908176745525e0c8b5.jpg)

Fig. 3. Part of a ThemeTree

## 3.2 Formation of the execution plan

We form a recommendation execution plan based on the user type. We use the parameter ???????????????? to represent whether the query is invoked by a fundraiser or a donor:

$$
u s e r t y p e = \left\{ \begin{array}{l l} F, & \text {if query is invoked by fundraiser;} \\ D, & \text {if query is invoked by donor.} \end{array} \right.\tag{1}
$$

The concept of the execution flow is described as follows.

$L i s t _ { 1 s t }$ contains the initial list of candidates generated from the relationship analysis, $M o d u l e _ { R e l a t i o n s h i p } ( F )$ or preference analysis $M o d u l e _ { P r e f e r e n c e } ( D )$ , where F represents the requesting fundraiser and D means the requesting donor. $L i s t _ { 1 s t }$ is a set of donors (fundraisers) if the user type is fundraiser (donor).

$$
L i s t _ {1 s t} = \left\{ \begin{array}{l l} M o d u l e _ {R e l a t i o n s h i p} (F) & \text { if   usertype   is   fundraiser } \\ M o d u l e _ {P r e f e r e n c e} (D) & \text { if   usertype   is   donor } \end{array} \right.\tag{2}
$$

Next, by analyzing the candidates generated in $L i s t _ { 1 s t }$ , we continue to generate the second list of candidates as follows:

$$
L i s t _ {2 n d} = \left\{ \begin{array}{l l} M o d u l e _ {P r e f e r e n c e} & \text {if usertype is fundraiser} \\ M o d u l e _ {R e l a t i o n s h i p} (F \in L i s t _ {1 s t}) & \text {if usertype is donor} \end{array} \right.\tag{3}
$$

Thus, two different types of candidate lists are generated in the different execution plans.

## 3.3 Fundraising participants analysis module

In this module, we identify donors (and fundraisers) with the most similarity and closeness, based on analyzing the donor’s preferences and calculating the fundraiser-donor relationship.

## 3.3.1 Donor preference analysis module

This module aims to understand a donor’s preferences. We analyze the behavioral trends of a particular donor and then compute his/her actual actions involving donations through social fundraising platforms. We also analyze related data about user preferences from social media.

???????????????????? $( d _ { i } , t h e m e )$ represents the overall preference of donor $d _ { i }$ towards a specific theme and individual behavior and is measured as:

$$
P r e f e r e n c e (d _ {i}, t h e m e) = G i v i n g T r e n d (d _ {i}, t h e m e) + D o n o r P r e f e r e n c e (d _ {i}, t h e m e)\tag{4}
$$

The value of ???????????????????? should be normalized; we utilize a min-max normalization approach, which is efficient and convenient to implement.

??????????????????????(?? , ??ℎ??????) represents the giving trend of donor $d _ { i }$ towards a specific ??ℎ??????, such as environment or education, and is calculated as follows:

$$
\begin{array}{r l} & G i v i n g T r e n d (d _ {i}, t h e m e) \\ & \qquad = T h e m e I n t e r a c t i o n (d _ {i}, t h e m e) * T h e m e P r e f e r e n c e (d _ {i}, t h e m e). \end{array}\tag{5}
$$

The donor $d _ { i } \mathrm { { ' } s }$ interactions related to a theme are measured based on the interacting activities: ??ℎ???????????????????????????? $( d _ { i } , t h e m e ) = S h a r e T i m e s ( d _ { i } , t h e m e ) + c o m m e n t T i m e s ( d _ { i } , t h e m e )$ (6) Where ??ℎ???????????????? $( d _ { i } , t h e m e ) \mathrm { i s }$ the number of times a donor $d _ { i }$ has shared a specific theme on the fundraising campaign page, and ???????????????????????? $( d _ { i } , t h e m e )$ is the number of times comments have been written by donor $d _ { i }$ on this ??ℎ??????.

Assume T is the set of all themes. The donor d ’s preference towards a theme is measured as: ??ℎ?????????????????????????? $( d _ { i } ,$ , ??ℎ??????)

$$
= \frac {\text { GivingTimes } (d _ {i} , \text { theme }) * \text { donationAmount } (d _ {i} , \text { theme })}{\sum_ {\text { theme } \in T} \text { GivingTimes } (d _ {i} , \text { theme }) * \text { donationAmount } (d _ {i} , \text { theme })}\tag{7}
$$

Where ?????????????????????? $( d _ { i } , t h e m e )$ represents the number of times that donor $d _ { i }$ has donated to a campaign with a specified ??ℎ??????; and ???????????????????????????? $( d _ { i } , t h e m e )$ is the total amount of donor $d _ { i } ^ { \prime } s$ donations to campaigns with a specified ??ℎ??????.

Next, the preference exhibited by donor $d _ { i }$ towards ??ℎ?????? on social media is measured as:

$$
\text { DonorPreference } (d _ {i}, \text { theme }) = \text { SocialPreference } (d _ {i}, \text { theme }) * \text { Similarity } (\overrightarrow {d _ {i}}, \overrightarrow {\text { theme }})\tag{8}
$$

where ???????????????????????????????? $( d _ { i } , t h e m e )$ represents the preference of donor $d _ { i }$ based on his/her activities on social media. We consider the following social activities: (1) check-ins: these reveal location-based service (LBS) data such as location, time, and what the user is doing; (2) likes: a user can use these to display the fact that they “like” someone’s opinion; (3) pages: on Facebook, a user can choose their preferred pages, and we can use these to infer his/her interests; (4) comments: a user can post comments related to specific themes on social media. Check-ins, comments, likes, and pages are used to infer a user’s preference. For example, [66] uses check-in data to infer a user’s preference and [11] predicts customer preference and measures customer engagement by analyzing likes, comments, shares, and interaction of a brand page.

In our experiments, we selected Facebook as our experimental platform, since it is the most suitable option for the non-profit field [26]. We therefore classified these four activities to match our ThemeTree:

$$
\begin{array}{r l} S o c i a l P r e f e r e n c e (d _ {i}, t h e m e) & \\ & = C h e c k I n \big (d _ {i}, t h e m e \big) + L i k e (d _ {i}, t h e m e) + P a g e s (d _ {i}, t h e m e) \\ & + C o m m e n t (d _ {i}, t h e m e) \end{array}\tag{9}
$$

Let $\overrightarrow { d _ { \imath } }$ denote the vector of a donor $d _ { i } \mathrm { : }$ ’s preference and ??<sup>⃗⃗⃗</sup>ℎ<sup>⃗⃗⃗</sup>??????<sup>⃗⃗⃗⃗⃗⃗⃗</sup> denote a vector of a ??ℎ?????? in the ThemeTree. The similarity between the preference of $d _ { i }$ and the ??ℎ?????? is measured using cosine similarity as follows:

$$
S i m i l a r i t y \big (\overrightarrow {d _ {\iota}}, \overrightarrow {t h e m e} \big) = \cos (\overrightarrow {d _ {\iota}}, \overrightarrow {t h e m e}) = \frac {\overrightarrow {d _ {\iota}} \cdot \overrightarrow {t h e m e}}{\| \overrightarrow {d _ {\iota}} \| \| \overrightarrow {t h e m e} \|}\tag{10}
$$

## 3.3.2 Fundraiser-donor relationship analysis module

In this module, we analyze the relationship between the donor and the fundraiser. The strength of the relationship can be reflected in the intensity of their common interaction activities. In this research, we consider four activities from social edia: (1) commenting: whether they have both written comments on the same post; (2) likes: whether they have both given likes to the same things; (3) tagging: whether they are both tagged in the same place or photo; and (4) pages: whether they are interested in the same pages. The intensity of the interaction between a donor $d _ { i }$ and a fundraiser $f _ { k }$ is measured as follows:

$$
I n t e r a c t i o n (d _ {i}, p _ {k}) = C o m m e n t (d _ {i}, f _ {k}) * L i k e (d _ {i}, f _ {k}) * T a g (d _ {i}, f _ {k}) * P a g e s (d _ {i}, f _ {k})\tag{11}
$$

We use the Jaccard similarity coefficient to compute the elements ?????????????? $( d _ { i } , f _ { k } )$ $L i k e ( d _ { i } , f _ { k } )$ $T a g ( d _ { i } , f _ { k } )$ , and $P a g e s ( d _ { i } , f _ { k } )$ as follows:

$$
J a c c a r d (A, B) = \frac {| A \cap B | + 1}{| A \cup B |} = \frac {| A \cap B | + 1}{| A | + | B | - | A \cap B |}\tag{12}
$$

If a given individual $d _ { i }$ can easily connect to many other people within a social network, he/she can affect many people; in other words, he/she can connect more easily with a fundraiser or a donor.

We define ??ℎ??????????????????ℎ $\left( { p _ { i } , p _ { j } } \right)$ as the shortest path between person $p _ { i }$ and person $p _ { j } .$ . In this research, a direct link between two persons is a friendship connection between them.

We measure the closeness centrality of a person $p _ { i }$ as follows:

$$
C l o s e n e s s (p _ {i}) = \frac {(N - 1)}{\sum_ {j = 0} ^ {N} s h o r t e s t P a t h (p _ {i} , p _ {j})}\tag{13}
$$

where N is the number of people in a social network and $i \neq j$

The relationship between donor $d _ { i }$ and fundraiser $f _ { k }$ is:

$$
R e l a t i o n s h i p (d _ {i}, f _ {k}) = I n t e r a c t i o n (d _ {i}, f _ {k}) \times \frac {\text {Closeness} (f _ {k})}{\text {shortestPath} (d _ {i} , f _ {k})}\tag{14}
$$

After computing the relationships between all users, we obtain a sorted list of candidates.

## 3.4 Fundraising campaign analysis module

In this module, we will evaluate the relationship between a specific donor and other donors selected in the same list. Using triadic closure, we know that if friends of a particular person donate to a specific campaign, he/she will be more willing to donate; the more of his/her friends that appear on the donation list, the higher the probability that this donor will be influenced by these friends who have donated. We define ??????????????(??) as the set of user u’s friends. ??????????????????????????(??) denotes a set of donors to a campaign $c .$ $u ^ { \prime } \mathrm { s }$ friends and the selected donors to campaign c is measured as follows:

$$
D F S i m (u, c) = \frac {| F r i e n d s (u) \cap D o n a t i o n D o n o r (c) |}{| D o n a t i o n D o n o r (c) |}\tag{15}
$$

This value is greater if more of user ??’s friends donate to campaign ??. User u will be influenced by his/her friends, and therefore has higher probability of donating to campaign ??. Individuals are likely to judge the quality of a charity based on their friends or other information such as donation histories [25, 57]. Since a donor on a donation list may not be a friend of a given user, we compute the intensity of the interactions between a candidate donor and other donors in the same donation list as follows:

$$
C D I n t e r a c t i o n (u, c) = \sum_ {d \in D o n a t i o n D o n o r (c)} I n t e r a c t i o n (u, d)\tag{16}
$$

A campaign with a higher rate of status updates will garner higher levels of attention from donors [3]. We measure the frequency of campaign updates as follows:

$$
C F r e q u e n c y (c) = \left\{ \begin{array}{l l} 0 & , i f N _ {U p d a t e} = 0 \\ \frac {N _ {U p d a t e} (c)}{D a t e _ {n e w e s t} (c) - D a t e _ {c r e a t e d} (c)} & , i f N _ {U p d a t e} = 1 \\ \frac {N _ {U p d a t e} (c)}{D a t e _ {n e w e s t} (c) - D a t e _ {o l d e s t} (c)} & , i f i f N _ {U p d a t e} > 1 \end{array} \right.\tag{17}
$$

where $N _ { U p d a t e } ( c )$ represents the number of update records in campaign c. $D a t e _ { o l d e s t } ( c )$ is the oldest date of updating, while $D a t e _ { n e w e s t } ( c )$ is the newest. $D a t e _ { c r e a t e d }$ is the date on which campaign ?? was created. We can then compute the merit of campaign c for user ?? as follows:

$$
\text { CampaignMerit } (u, c) = \left(D F S i m (u, c) + C D I n t e r a c t i o n (u, c)\right) \times (1 + C F r e q u e n c y (c))\tag{18}
$$

Note that the value of ??????????????????????????(??, ??) should be normalized.

## 3.5 Fundraising recommendation engine module

In this section, we evaluate participants and campaigns based on the role of the requesting user, a multiple-criteria decision analysis (MCDA) approach called TOPSIS (technique for order of preference by similarity to ideal solution) to decide whether or not items on the candidate list are accepted. Finally, we present different recommendation lists to users to match the role of the requesting user.

## 3.5.1 Computation of candidates

After obtaining the results from the above analysis modules, we generate a final list of candidates for further TOPSIS analysis. ???????????????????????? $_ { \dot { \boldsymbol { f } } i n a l }$ denotes the list of donors (campaigns) based on the results from the above three modules.

$$
C a n d i d a t e L i s t _ {f i n a l} = \{r _ {1}, r _ {2}, \dots , r _ {n} \}, \forall r _ {i} \in D o n o r, C a m p a i g n\tag{19}
$$

## 3.5.2 Suitability criteria aggregation

In this section, we use TOPSIS to evaluate the list of candidates, in order to produce a final list of recommended candidates. TOPSIS was originally developed in 1981 [28] and has since been further developed [27, 64]. The concept of TOPSIS is based on the shortest geometric distance from the positive ideal solution (PIS) and the longest geometric distance from the negative ideal solution (NIS).

First, we define a ???????????????? vector that contains the criteria for user preference $C r _ { P }$ , user relationship $C r _ { R }$ , and campaign merit $C r _ { C M }$

$$
C r i t e r i a = (C r _ {P}, C r _ {R}, C r _ {C M})\tag{20}
$$

Donors want to discover campaigns they are interested in, while fundraisers want to find donors to solicit for donations. $A l t e r n a t i v e _ { d s }$ represents the vector of campaigns for the donor scenario, and $A l t e r n a t i v e _ { f s }$ represents the vector of donors in the fundraiser scenario:

$$
A l t e r n a t i v e _ {d s} = (c _ {1}, c _ {2}, \dots , c _ {n})\tag{21}
$$

$$
A l t e r n a t i v e _ {f s} = (d _ {1}, d _ {2}, \dots , d _ {n})\tag{22}
$$

We also define a vector of the weights of criteria from users before applying our mechanism, or use the default weights of the criteria based on an average of those of other users. ?? represents the vector of the weights of criteria from questionnaires, and contains the weights of the user preference $w _ { P }$ , user relationship $w _ { R }$ , and campaign merit $w _ { C M }$

$$
W = (w _ {P}, w _ {R}, w _ {C M})\tag{23}
$$

$$
w h e r e w _ {P} + w _ {R} + w _ {C M} = 1
$$

Next, we perform TOPSIS to rank our alternatives. There are six steps in our mechanism.

Step 1: We create a decision matrix $D M _ { m n }$ which contains ?? criteria and ?? alternatives. $x _ { m n }$ represents the intersection of alternatives and criteria. In our mechanism, we have three criteria and N alternatives, and therefore define a set of ????????????????????????.

$$
D M _ {m n} = (x _ {m n}) _ {m \times n}\tag{24}
$$

$$
w h e r e m = | C r i t e r i a |, n = | A l t e r n a t i v e |
$$

Step 2: We normalize this from $D M _ { m n }$ and also normalize matrix ??.

$$
R = (r _ {i j}) _ {m \times n}
$$

$$
w h e r e r _ {i j} = \frac {x _ {i j}}{\sqrt {\sum_ {k = 1} ^ {m} x _ {i k} ^ {2}}}, i = 1, 2, \dots , m, j = 1, 2, \dots , n\tag{25}
$$

Step 3: We obtain a weighted normalized decision matrix $T \colon$ :

$$
\begin{array}{c} {T = (t _ {i j}) _ {m \times n} = (w _ {i} r _ {i j}) _ {m \times n}} \\ {\mathrm{where} i = 1, 2, \ldots , m, j = 1, 2, \ldots , n, w _ {i} \in W} \end{array}\tag{26}
$$

Step 4: We compute a positive ideal solution $S _ { i } ^ { + }$ and a negative ideal solution $S _ { i } ^ { - }$ . Our criteria both have a positive impact; in other words, a greater value means a more positive impact in our design. We maximize the best alternative and minimize the worst using Equations (27) and (28):

$$
S _ {i} ^ {+} = \left\{m a x (t _ {i j}) | j = 1, 2, \dots , n \right\} = (v _ {1} ^ {+}, v _ {2} ^ {+}, \dots , v _ {n} ^ {+})\tag{27}
$$

$$
S _ {i} ^ {-} = \left\{m i n (t _ {i j}) | j = 1, 2, \dots , n \right\} = (v _ {1} ^ {-}, v _ {2} ^ {-}, \dots , v _ {n} ^ {-})\tag{28}
$$

Step 5: We compute the distance between the (positive or negative) ideal solution and each alternative:

$$
A _ {j} ^ {+} = \sqrt {\sum_ {i = 1} ^ {n} \left(v _ {i j} - v _ {i} ^ {+}\right) ^ {2}} \text {where} i = 1, 2, \dots , m, j = 1, 2, \dots , n\tag{29}
$$

$$
v A _ {j} ^ {-} = \sqrt {\sum_ {i = 1} ^ {n} \left(v _ {i j} - v _ {i} ^ {-}\right) ^ {2}} \text {where} i = 1, 2, \dots , m, j = 1, 2, \dots , n\tag{30}
$$

Step 6: To find the shortest distance from the positive ideal solution and the longest distance from the negative ideal solution, we use Equation (31):

$$
C _ {j} = \frac {A _ {j} ^ {-}}{A _ {j} ^ {+} + A _ {j} ^ {-}}\tag{31}
$$

When the above steps are complete, we can sort $C _ { j }$ in descending order and organize these into a list of recommendations. In the next section, we use this approach to generate our results.

## 3.5.3 Formation of campaign/donor list

Finally, we produce a list of recommended candidates. In the fundraiser scenario, the fundraiser will receive a list of donors, consisting of two information components: (1) campaign information;

and (2) a list of candidate donors. The campaign information contains information such as the name of the campaign name, how much it has raised, and the time elapsed. The list of candidate donors provides the names of the donors, their photos from social media, their relationship with the fundraiser, their preferences, and their contact information. In the donor scenario, the donor will receive a list of candidate campaigns, consisting of the basic campaign information and the corresponding fundraiser information.

## 4 Experiments

We implemented and performed experiments to evaluate our proposed mechanism. Facebook was selected as the experimental platform as it is the most popular social network in the world. It had around 1.6 billion monthly active users (MAU) in December 2015. This abundance of social information can be utilized to conduct social relationship analysis. In addition, we used CrowdRise and GlobalGiving as our reference charity fundraising platforms. CrowdRise is one of the most famous fundraising platforms in the world, and uses a P2P fundraising model. According to USA Today news, the American Cancer Society has used CrowdRise to fundraise from the current another large crowdfunding platform for grassroots charitable projects, was founded in 2002. It has 517,000 donors, has facilitated 212 million dollars of donations and 14,000 projects in 165 countries [22]. GlobalGiving and CrowdRise offer 20 and 21 donation theme types, respectively. We therefore constructed a ThemeTree for our experiments based on these two fundraising platforms.

We created a website to execute and evaluate the proposed mechanism. At the front end, we used HTML5, CSS3, and JavaScript as our major programming languages, and used AngularJS, jQuery libraries, and Google Visualization API to display the recommendation lists. At the back end, we used PHP, MariaDB, and Facebook Graph API to collect social networking data.

## 4.1 Experimental processes

Our experiment was performed using the following four stages:

Stage 1: Build the experimental environment. In this stage, we built a web-based system for the proposed mechanism. After the system had been developed, we invited users to join our experiment, and encouraged them to disseminate our web-based service to their friends. Due to Facebook’s privacy policy, we required authorization from the users to collect and analyze personal and social information. We also asked users to fill in a weighting questionnaire, including the user’s preferences and relationships, and the context of the campaign. After the user had filled out the questionnaire, we used the results to calculate the TOPSIS weighted normalized decision matrix.

Stage 2: Develop the campaign information. The system provides an interface for users to create a campaign. The campaign information is as follows: (1) campaign name; (2) campaign theme; campaign donor list; (7) campaign story/content; and (8) campaign progress reports, including update

Stage 3: Execute the mechanism. Both fundraisers and donors were invited to use the proposed system. For fundraisers who wanted to discover donors to donate to their campaigns, we responded with a list of the most relevant donors; for a potential donor who wanted to discover campaigns that may be of interest, we replied with a list of the most appropriate campaigns.

Stage 4: Evaluate the mechanism. As the users interacted with the proposed mechanism, we tracked their behaviors (clicks and sharing) and solicited feedback (liking, satisfaction, and willingness) using questionnaires based on the recommendation results.

## 4.2 Data collection

In this section, we describe the data collection carried out during the experiment. In this process, we collected data on users and campaign information, and also constructed a ThemeTree.

## 4.2.1 User profile

We invited the users and their friends who were willing to join our experiment by the snowball sampling approach. In this experiment setting, the profile and size of the sampled participants were aligned with the studies on crowdfunding [12], [29]. We collected users’ personal and social information for the past 12 months. As shown in Table 1, these data included 4,735 posts, 2,093 check-ins, 9,910 tags, 154,592 likes, 15,084 comments, and 23,773 fan pages liked. A total of 117 users participated in the experiment, and each user had 466 friends on average. The distribution of gender was 63 males and 54 females, and the age range was 18 to 40 (64% aged 18–24; 30% aged 25–30, 6% aged 31–40).

Table 1 Summary of dataset.

<table><tr><td>Title</td><td>Value</td><td>Title</td><td>Value</td></tr><tr><td>Number of participants</td><td>117 users</td><td>Number of likes</td><td>154,592</td></tr><tr><td>Number of posts</td><td>4,735</td><td>Number of comments</td><td>15,084</td></tr><tr><td>Number of check-ins</td><td>2,093</td><td>Number of fan pages liked</td><td>23,773</td></tr><tr><td>Number of tags</td><td>9,910</td><td>Average number of friends per user</td><td>466</td></tr></table>

The statistics on user experience of online fundraising also show that 65% of users had no previous online giving experience. 35% of users had online giving experience as a fundraiser or a donor. 5% of users had been a fundraiser as well as a donor. Regarding the frequency of giving via an online platform, 26% of users had one to two times of giving experience and 6% of users had giving experiences for more than two times.

## 4.2.2 Campaign profile

Next, we describe the profiles of the campaigns considered in our experiment. By collecting and classifying related themes from CrowdRise and GlobalGiving, we obtained a list of 12 theme types, as sers to input their campaigns, which could either be ongoing campaigns in an actual fundr ising platform or campaigns that had not yet been announced. A total of 53 campaigns were included in the experiment. Information on the goals and status of these campaigns is shown in Tables 3 and 4. We used the ThemeTree to match the fundraising platform theme to the category on Facebook, which we used to infer users’ preferences.

Table 2 Themes of campaigns

## Themes

<table><tr><td>Accidents and Emergencies (2); Animals; Children (4); Civil Rights and Social Action (1); Education, Tuition, and PTAs (6); Environment (6); Health (7); Medical, Disease, and Disorders (4); Peace and Security (4); Poverty, Hunger, and Shelter (6); Volunteering (6); Women and Girls (4)</td></tr></table>

Table 3 Range of campaign goals

<table><tr><td>Goal#</td><td>C#</td><td>%</td></tr><tr><td>Goal not set</td><td>5</td><td>9%</td></tr><tr><td>1~ 10,000</td><td>27</td><td>51%</td></tr><tr><td>10,001~20,000</td><td>8</td><td>15%</td></tr><tr><td>20,001~30,000</td><td>4</td><td>8%</td></tr><tr><td>30,001~40,000</td><td>1</td><td>2%</td></tr><tr><td>40,001~</td><td>8</td><td>15%</td></tr><tr><td>Total</td><td>53</td><td>100%</td></tr></table>

Table 4 Percentage of campaign goal raised

<table><tr><td>Goal#</td><td>C#</td><td>%</td></tr><tr><td>Goal not set</td><td>5</td><td>9%</td></tr><tr><td>Just launched (0%)</td><td>1</td><td>2%</td></tr><tr><td>One-third of goal (33%)</td><td>14</td><td>26%</td></tr><tr><td>Two-thirds of goal (66%)</td><td>12</td><td>23%</td></tr><tr><td>Reached goal (100%)</td><td>11</td><td>21%</td></tr><tr><td>Exceeded goal (&gt;100%)</td><td>10</td><td>19%</td></tr><tr><td>Total</td><td>53</td><td>100%</td></tr></table>

## 4.3 Computation of measurements

## 4.3.1 Criteria

We evaluated performance according to two weight options as follows: (1) default weight (DW): we invited the initial users to fill out a criteria questionnaire, and used this as the default weight; (2) personal weight (PW): personal criteria weight if provided. The default weights for users who did not provide personal criteria weight were (user preference, user relationship, campaign context) = (0.346, 0.32, 0.334)

## 4.3.2 Suitability

In order to validate the effectiveness of our proposed mechanism in terms of providing suitable recommendations for users, we compared it with other benchmark approaches, as follows.

1. Random approach: This approach provides a random recommendation list to users with no computation or process involved.

2. Content-based approach: This is a recommendation approach based on past preference or product. This approach uses past history data to infer a recommendation for donor campaigns based on the donor’s preferences. Hence, we chose the components of donor preference and fundraising campaign as comparison.

3. Collaborative filtering approach (CF): This is a recommendation approach based on a similar user’s preference. This approach uses similar donors to infer a donor’s preferences. The system can discover donors with similarity and closeness to a given user, and recommend campaigns to the target donor based on these. We used the components of fundraiser-donor relationship and fundraising campaigns as a basis for comparison.

4. Social-based approach: This is a recommendation method based on social networking information. This approach utilizes data from the social network, including user preferences, relationships, and social influence. We considered the factors of donor preferences and the fundraiser-donor relationship for comparison.

5. Social fundraising recommendation approach (SFR; our proposed approach): This social fundraising recommendation approach is based on our proposed mechanism. This integrated mechanism can help fundraisers by providing a list of potential donors and also help donors by offering them interesting campaigns. In this approach, we considered a more comprehensive analysis of donor preference, fundraiser-donor relationship, and fundraising campaign analysis.

## 5 Results and evaluation

In order to evaluate our proposed recommendation mechanism, we gathered feedback from users after interacting with our recommendation mechanism. First, we analyzed the behaviors based on the like and share rates. Then, we evaluated the questionnaire using likeness, satisfaction, and willingness.

We evaluated the accuracy of our system by asking users to pick those items (donors or campaigns) that they found most suitable. We measured the accuracy of the recommendation mechanism using the equation described below, where $\emptyset _ { R e c o m m e n d e d I t e m s }$ represents the set of our recommended items produced by our mechanism and ∅<sub>????????????????????????????????∩??????????????????????????</sub> represents the set of recommended items that are most suitable

Then:

$$
\text {Accuracy} = \frac {| \emptyset_ {\text {RecommendedItems} \cap \text {SuitableItems}} |}{| \emptyset_ {\text {RecommendedItems}} |}\tag{32}
$$

Note the items to recommend are donors if the user is a fundraiser and the items are campaigns if the

user is a donor.

We compared the recommendation accuracies of our approach and other benchmark approaches. The donor recommendation accuracy (for a fundraiser) is shown as in Fig. 4 and the campaign recommendation accuracy (for a donor) is shown as in Fig. 5. The results of donor recommendation paired t-tests and the campaign recommendation paired t-tests are shown as in Table 5 and Table 6.

![](/api/attachments/5U2XWJRN/fulltext/images/7495921a90224b2c4c5557f64197291cd642f85a0dedf31ca6582909b20af04a.jpg)

![](/api/attachments/5U2XWJRN/fulltext/images/b73224d5fa97c8fdef2d9277a5ce559c3e8b9bad8b7b2772c489581414880d9a.jpg)  
Fig. 4. Donor recommendation accuracies of Fig. 5. Campaign recommendation accuracies of different approaches different approaches

Table 5 Verification results for the donor recommendation accuracies of different approaches

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>t</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="4">SFR</td><td>Random</td><td>.305</td><td>.324</td><td>.029</td><td>10.203</td><td>.000</td></tr><tr><td>Content-based</td><td>.182</td><td>.320</td><td>.029</td><td>6.181</td><td>.000</td></tr><tr><td>CF</td><td>.191</td><td>.314</td><td>.029</td><td>6.181</td><td>.000</td></tr><tr><td>Social-based</td><td>.182</td><td>.364</td><td>.032</td><td>5.702</td><td>.000</td></tr></table>

Table 6 Verification results for the campaign recommendation accuracies of different approaches

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>t</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="4">SFR</td><td>Random</td><td>.305</td><td>.355</td><td>.032</td><td>9.302</td><td>.000</td></tr><tr><td>Content-based</td><td>.200</td><td>.366</td><td>.033</td><td>5.899</td><td>.000</td></tr><tr><td>CF</td><td>.211</td><td>.394</td><td>.036</td><td>5.817</td><td>.000</td></tr><tr><td>Social-based</td><td>.263</td><td>.371</td><td>.034</td><td>7.655</td><td>.000</td></tr></table>

## 5.1 Evaluation of behaviors

We tracked the users’ behaviors by recording clicks on the ‘like’ and ‘share’ buttons in the proposed system.

## 5.1.1 Evaluation of like rate

When a donor received information about a soliciting campaign, our system provided a function

$$
L i k e R a t e = \frac {\emptyset A c t u a l C l i c k L i k e}{\emptyset S o l i c i t i n g}\tag{33}
$$

where ∅Soliciting represents the total number of potential campaigns, and ∅?????????????????????????????? is the total number of clicks from donors. The like rates generated for the various different recommendation approaches are shown in Fig. 6. It can be seen that our proposed mechanism obtained the highest like rate.

![](/api/attachments/5U2XWJRN/fulltext/images/6bf63a7c67f2d33f605c936ed6fa7ef171c47208b9c7a66ea7d1c3f4cbaa1cdc.jpg)  
Fig. 6. Like rates for all approaches

We also utilized a paired-samples t-test to verify the statistically significant differences between the approaches used. The results, based on a confidence interval of 95%, are shown in Table 7. We can verify that our proposed mechanism outperforms the other approaches.

Table 7 Statistical verification results for like rate

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="4">SFR</td><td>Random</td><td>.15504</td><td>.25479</td><td>.02193</td><td>7.070</td><td>.000</td></tr><tr><td>Content-based</td><td>.06096</td><td>.28758</td><td>.02475</td><td>2.463</td><td>.015</td></tr><tr><td>CF</td><td>.06393</td><td>.28413</td><td>.02445</td><td>2.614</td><td>.010</td></tr><tr><td>Social-based</td><td>.05637</td><td>.28983</td><td>.02494</td><td>2.260</td><td>.025</td></tr></table>

## 5.1.2 Evaluation of share rate

When a donor received a potential campaign, our system provided a function that can allow a donor to click ‘share’; our system will record this and share the campaign over Facebook. We calculated the share rate as follows:

$$
S h a r e R a t e = \frac {\emptyset A c t u a l C l i c k S h a r e}{\emptyset S o l i c i t i n g}\tag{34}
$$

where ∅Soliciting represents the total number of potential campaigns and ∅????????????????????????ℎ?????? is the total number of shares by donors. From Fig. 7, we can observe that our proposed approach is better than the others in terms of the sharing rate.

![](/api/attachments/5U2XWJRN/fulltext/images/efa60f342686356c8bbfe7b7bfa9f71ed03c8fac58d72a8b5ba582e79d505788.jpg)  
Fig. 7. Share rates for all approaches

We also utilized a paired-samples t-test to verify the statistically significant differences between the sharing rates of these different approaches, using a confidence interval of 95%, and the results are shown in Table 8. We demonstrated that our proposed mechanism is better than the other approaches.

Table 8 Statistical verification results for share rate

<table><tr><td>Paired Group</td><td>Mean</td><td>Std.</td><td>Std.</td><td>t</td><td>Sig.</td></tr><tr><td colspan="2"></td><td>Deviation</td><td>Error Mean</td><td colspan="2">(2-tailed)</td></tr><tr><td rowspan="4">SFR</td><td>Random</td><td>.12037</td><td>.32815</td><td>.02824</td><td>4.262</td></tr><tr><td>Content-based</td><td>.08244</td><td>.37441</td><td>.03222</td><td>2.558</td></tr><tr><td>CF</td><td>.07874</td><td>.38867</td><td>.03345</td><td>2.354</td></tr><tr><td>Social-based</td><td>.06296</td><td>.29745</td><td>.02560</td><td>2.459</td></tr></table>

## 5.2 Evaluation of perception

We evaluated our proposed recommendation mechanism using a feedback questionnaire. The questionnaire had a scale of scores from 1 to 5 (where a greater score indicates a more positive rating), and we asked users to answer the following questions:

 Question 1: How much do you like this campaign?

 Question 2: To what extent are you satisfied with the context of this campaign?

 Question 3: How willingly do you want to donate to this campaign?

Since we had two types of users (donors and fundraisers), we had two different scenarios for which users can fill out the questionnaire. For donors, we asked the users directly to fill out the questionnaire. For fundraisers, we provided the user with a link to contact the targeted donors, where the user could choose which donors to solicit. Finally, we asked these solicited donors to fill out the questionnaire.

## 5.2.1 The evaluation of liking

In Fig. 8, we show the results from users for the liking score for all solicited campaigns. All values are averaged for each approach. It can be seen that the random approach had the lowest score and our proposed approach achieved the highest.

![](/api/attachments/5U2XWJRN/fulltext/images/fcac08768f151e42bbcc330a161c0dfeafaffb739431208003acdf366d998084.jpg)  
Fig. 8. Liking score for potential campaigns

## 5.2.2 Evaluation of satisfaction

In Fig. 9, we show the results for the users’ satisfaction with the potential campaigns. All values are the average score for each approach. It can be seen that the random approach has the lowest score of all of the approaches and our proposed approach has the highest.

![](/api/attachments/5U2XWJRN/fulltext/images/29998ff1a23215b6238704e844a2b78e48c07ca4c46851be9ea86a6c0ebaa2cd.jpg)  
Fig. 9. Satisfaction with potential campaigns

## 5.2.3 Evaluation of willingness

In Fig. 10, we show the results for the donation willingness scores for users. All values are the average score for each approach. We can see that the random approach has the lowest score and the SFR approach again has the highest.

![](/api/attachments/5U2XWJRN/fulltext/images/a327027643bedde2b7e82c85c7e706f5cba0ffca5003755870660c71e344e77e.jpg)  
Fig. 10. Willingness to donate

## 6 Discussion and conclusion

We are living in a rapidly changing world with numerous social problems, and social fundraising is one solution for achieving philanthropic goals. Based on an analysis of social relationships, user preference information, and the footprints generated within charity fundraising platforms, we propose a social fundraising recommendation mechanism that can identify potential donors and assist fundraisers in soliciting donations. In addition, our proposed mechanism can also help donors to carry out donation activities by offering them interesting campaigns. Specifically, we analyze four key fundraising factors: the giving patterns of the donor, the preferences of the donor, the fundraiser-donor relationship, and the merit of the campaign. We then integrate these four key factors to generate a candidate list using the multi-criteria decision model TOPSIS, in order to determine the priority of the candidates on the recommendation list.

In our experiments, we evaluate the accuracy, like rate, share rate, liking, satisfaction, and willingness in order to verify the proposed mechanism. The results show that our proposed mechanism outperforms other benchmark approaches. The proposed recommendation mechanism can help a fundraiser to find suitable donors, while donors can use the proposed mechanism to find suitable campaigns. Our proposed mechanism can effectively improve the success rate of social fundraising.

## 6.1 Research contributions

This study makes several important contributions. From a system development perspective, we design an efficient and effective recommendation system for social fundraising. The experimental results show that our proposed system is able to improve the willingness of a donor to donate. Next, from a methodological perspective, we adopt the user’s preferences, relationships, and campaign context as TOPSIS criteria. Our proposed system combining these three criteria performs better than other benchmark approaches. From a practical perspective, although existing charity fundraising platforms (e.g. CrowdRise, GlobalGiving) offer many campaigns, they do not provide an effective mechanism to match fundraisers with donors. The proposed mechanism provides an effective assessment and match for two types of participants in social fundraising activities based on an analysis of social relationships, user preference information, and the footprints generated within charity fundraising platforms. Our mechanism can effectively match a donor with a fundraiser, which consequently improves the success rate of fundraising. By improving the fundraising process, charity fundraisers can effectively seek financial resources from the crowd to solve social problems, so that fundraisers can find potential donors more effectively, and donors can easily find suitable activities without spending time.

## 6.2 Managerial implications

In charity crowdfunding, donors give without the expectation of gaining a tangible reward from a project. A donor tends to provide giving to a charity project that is of high interest and has a strong relationship with the donor. The social networking factor therefore becomes more important in charity fundraising. The social activities on social media will significantly affect the success rate of fundraising. Especially, the main activities affecting user preferences, the social relationships between fundraisers and donors, as well as the social influence of friends’ behavior on the campaigns should be more elaborately managed. From a wider social view, our mechanism can support society in attempting to solve numerous social issues. Naturally, support from governments and foundations is important, but we can also utilize the power of crowds to solve a wide range of smaller social problems.

## 6.3 Limitations of this research

This study has several limitations. Firstly, when utilizing social networking information to enhance the accuracy of recommendations, we only use Facebook as a social media platform due to constraints on scale and resources. By analyzing and combining a greater range of activities from different social media platforms, the accuracy of recommendation could be further improved. Secondly, as the experiments are conducted by inviting the participants by the snowball sampling approach, instead of utilizing an existing dataset, the population size and distribution of sampled participants are limited by the experiment period. The performance should be further increased with population size and diversity. Thirdly, our recommendation system also suffers from the ‘cold start problem; if the system does not have sufficient information, the accuracy of the recommendations will be low. Fourthly, we know that social networks change the behavior of individuals in terms of making friends; however, these individuals still have offline relationships in the real world. Our system only captures online activities over social networks, and these offline activities are not considered. Some charitable fundraising may involve offline activities, which are not considered in the online space. In future, we may gather information on both online and offline activities, and include new types of human behavior. Finally, we mainly trace likes and sharing behavior in this research. Our system does not trace other behaviors, such as how long the user stays on a specific campaign page. In future, we may trace a great range of user activities and consider a wider variety of user behaviors.

## 6.4 Future work

Several related issues should be studied further. Firstly, our recommendation system focuses on financial issues. For some social problems, a charity may request donations of materials or even volunteers, since in addition to financial resources, the charity may need other types of resources. Thus, charity resource-raising is an important issue. Secondly, a report shows that nearly 14% of online transactions use mobile devices for donations [7]. Due to the particular characteristics of mobile devices, which are ubiquitous and easy to use, “impulse donating” may be easier to inspire. In the future, mobile platforms will become new, popular channels for giving. Thirdly, existing fundraising platforms mainly operate with a centralized structure. From a platform design perspective, a decentralized architecture based on social networks may be a good alternative approach to improve effectiveness. Finally, a further mechanism for enhancing social fundraising activities might consider incentive issues for giving, such as economic incentives (e.g. tax deductions) and social incentives (e.g. reputational credit).

## References

[1] Aggarwal, C.C., Procopiuc, C., & Yu, P.S. (2002). Finding localized associations in market basket data. IEEE Transactions on Knowledge and Data Engineering, 14(1), 51–62.

[2] An, J., Quercia, D., & Crowcroft, J. (2014). Recommending investors for crowdfunding projects. Proceedings of the 23rd International Conference on World Wide Web. Seoul, Korea, 261–270.

[3] Andreoni, J., & Rao, J.M. (2011). The power of asking: How communication affects selfishness, empathy, and altruism. Journal of Public Economics, 95(7), 513–520.

[4] Bagheri, A., Chitsazan, H., & Ebrahimi, A. (2019). Crowdfunding motivations: A focus on donors' perspectives. Technological Forecasting and Social Change, 146, 218–232.

[5] Belkin, N.J., & Croft, W.B. (1992). Information filtering and information retrieval: Two sides of the same coin? Communications of the ACM, 35(12), 29–38.

[6] Belleflamme, P., Lambert, T., & Schwienbacher, A. (2014). Crowdfunding: Tapping the right crowd. Journal of Business Venturing, 29(5), 585–609.

[7] Blackbaud (2016). Charitable Giving Report How Nonprofit Fundraising. https://www.blackbaud.com/nonprofit-resources/charitablegiving.

[8] Campos, L.M.D., Fernández, J.M.L., Huete, J.F., & Rueda, M.A.M. (2010). Combining content-based and collaborative recommendations: A hybrid approach based on Bayesian networks. International Journal of Approximate Reasoning, 51(7), 785–799.

[9] Choy, K., & Schlagwein, D. (2015). IT affordances and donor motivations in charitable crowdfunding: The "Earthship Kapita" case. European Conference on Information Systems (ECIS), Munster, Germany, 1–12.

[10] CrowdRise. How do I set up a campaign? https://support.crowdrise.com/hc/en-us/articles/203533514-How-do-I-set-up-a-campaign-.

[11] Cvijikj, P., I., & Michahelles, F. (2013). Online Engagement Factors on Facebook Brand Pages, Social Network Analysis and Mining, 3(4), 843–861.

[12] Du, Z., Li, M., & Wang, K. (2019). “The more options, the better?” Investigating the impact of the number of options on backers’ decisions in reward-based crowdfunding projects. Information & Management, 56(3), 429–444.

[13] Duronio, M.A., & Tempel, E.R. (1997). Fund raisers: Their career, stories, concerns, and accomplishments, Jossey-Bass Inc, San Francisco.

[14] Easley, D., & Kleinberg, J. Networks, crowds, and markets: Reasoning about a highly connected world. https://www.cs.cornell.edu/home/kleinber/networks-book/.

[15] Ellison, N.B. (2007). Social network sites: Definition, history, and scholarship. Journal of Computer-Mediated Communication, 13(1), 210–230.

[16] Flannery, H., & Harris, R. (2011). 2011 DonorCentrics™ internet and multichannel giving benchmarking report: Blackbaud. https://www.blackbaud.com/files/resources/downloads/WhitePaper\_MultiChannelGivingAnalysi s.pdf.

[17] García, E., Romero, C., Ventura, S., & Calders, T. (2007). Drawbacks and solutions of applying association rule mining in learning management systems. Proceedings of the International Workshop on Applying Data Mining in e-Learning, Crete, Greece, 1–10.

[18] Geiger, D., & Schader, M. (2014). Personalized task recommendation in crowdsourcing information systems — Current state of the art. Decision Support Systems, 65, 3–16.

[19] Gera, J., & Haur, H. (2018). A novel framework to improve the performance of crowdfunding platforms. ICT Express, 4(2), 55–62.

[20] Gilbert, E., & Karahalios, K. (2009). Predicting tie strength with social media. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Boston, MA, USA, 211–220.

[21] Gleasure, R. & Feller, J. (2016). Does Heart or Head Rule Donor Behaviors in Charitable Crowdfunding Markets?. International Journal of Electronic Commerce, 20(4), 499–524.

[22] GlobalGiving. (no date). GlobalGiving homepage, https://www.globalgiving.org/.

[23] Gurevitch, M. (no date). The social structure of acquaintanceship networks. Massachusetts Institute of Technology. http://hdl.handle.net/1721.1/11312.

[24] Habibi, M. R., Laroche, M., & Richard, M.O. (2014). Brand communities based in social media: How unique are they? Evidence from two exemplary brand communities. International Journal of Information Management, 34(2), 123–132.

[25] Harbaugh, W. T. (1998). The prestige motive for making charitable transfers. The American Economic Review, 88 (2) 277–282.

[26] Hong, Y., Hu, Y., & Burtch, G. (2015). How does social media affect contribution to public versus private goods in crowdfunding campaigns? International Conference on Information Systems.

[27] Hwang, C.L., Lai, Y.J., & Liu, T.-Y. (1993). A new approach for multiple objective decision making. Computers & Operations Research, 20(8), 889–899.

[28] Hwang, C.L., & Yoon, K. (1981). Methods for multiple attribute decision making. Multiple Attribute Decision Making, 186, 58–191.

[29] Kang, L., Jiang, Q., & HooTan, C. (2017). Remarkable advocates: An investigation of geographic distance and social capital for crowdfunding. Information & Management, 54(3), 336–348.

[30] Kim, H.N., Ji, A.T., Ha, I., & Jo, G.S. (2010). Collaborative filtering based on collaborative tagging for enhancing the quality of recommendation. Electronic Commerce Research and Applications, 9(1), 73–83.

[31] Kuppuswamy, V., & Bayus, B. (2013). Crowdfunding Creative Ideas: The Dynamics of Project Backers in Kickstarter. SSRN Electronic Journal, 1–42.

[32] Lee, K.C., & Lee, S. (2011). Interpreting the web-mining results by cognitive map and association rule approach. Information Processing & Management, 47(4), 482–490.

[33] Li, L., Suh, A., & Wagner, C. (2071). Donation Behavior in Online Micro Charities: An Investigation of Charitable Crowdfunding Projects, Proceedings of the 50th Hawaii International Conference on System Sciences, USA, 843–853.

[34] Li, Y. M., Chou, C. L., & Lin, L.F. (2014). A social recommender mechanism for location-based group commerce. Information Sciences, 274, 125–142.

[35] Liao, H. Y., Chen, K.Y., & Liu, D.R. (2015). Virtual friend recommendations in virtual worlds. Decision Support Systems, 69, 59–69.

[36] Liu, L., Cheung, C.M., & Lee, M.K. (2016). An empirical investigation of information sharing behavior on social commerce sites. International Journal of Information Management, 36(5), 686–699.

[37] Loader, B. D., & Mercea, D. (2011). Networking democracy? Social media innovations and participatory politics. Information, Communication & Society, 14(6), 757–769.

[38] Lu, C.C., Xie, S., Kong, X., & Yu, P.S. (2014). Inferring the impacts of social media on

crowdfunding. Proceedings of the 7th ACM International Conference on Web Search and Data Mining, New York, New York, USA, 573–582.

[39] Meer, J. (2011). Brother, can you spare a dime? Peer pressure in charitable solicitation. Journal of Public Economics, 95(7), 926–941.

[40] Mollick, E. (2014). The dynamics of crowdfunding: An exploratory study. Journal of Business Venturing, 29(1), 1–16.

[41] Nah, S., & Saxton, G.D. (2012). Modeling the adoption and use of social media by nonprofit organizations. New Media & Society. https://doi.org/10.1177/1461444812452411.

[42] Nakamura, A., & Abe, N. (1998). Collaborative filtering using weighted majority prediction algorithm. Proceedings of the Fifteenth International Conference on Machine Learning, San Francisco, CA, USA, 395–403.

[43] Otte, E., & Rousseau, R. (2002). Social network analysis: A powerful strategy, also for the information sciences. Journal of Information Science, 28(6), 441–453.

[44] Park, J.H. (2014). The effects of personalization on user continuance in social networking sites. Information Processing & Management, 50(3), 462–475.

[45] Pazzani, M.J., & Billsus, D. (2007). Content-based recommendation systems. The Adaptive Web, Springer, 325–341.

[46] Rakesh, V, Lee, W.C., & Reddy, C.K. (2016). Probabilistic Group Recommendation Model for Crowdfunding Domains. Proceedings of the Ninth ACM International Conference on Web Search and Data Mining. San Francisco, California, USA, 257–266.

[47] Roberson, B.G. (2015). Examining the relationship between trust, credibility, satisfaction, and loyalty among online donors. Walden University ScholarWorks. https://scholarworks.waldenu.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=2965&co ntext=dissertations.

[48] Saoud, Z., & Kechid, S. (2016). Integrating social profile to improve the source selection and the result merging process in distributed information retrieval. Information Sciences, 336, 115–128.

[49] Saravanakumar, M., & SuganthaLakshmi, T. (2012). Social media marketing. Life Science Journal, 9(4), 4444–4451.

[50] Shafiq, O., Alhajj, R., & Rokne, J.G. (2015). On personalizing Web search using social network analysis. Information Sciences, 314, 55–76.

[51] Sharma, N., & Verma, C.K. (2006). Association rule mining: An overview. GESTS International Transactions on Computer Science and Engineering, 22(1), 71–82.

[52] Song, A., Lee, H.I., Ko, M., & Lee, U. (2015). Every little helps: Understanding donor behavior in a crowdfunding platform for non-profits. Proceedings of the 33rd Annual ACM Conference Extended Abstracts on Human Factors in Computing Systems. Seoul, Republic of Korea, 1103– 1108.

[53] Townsend, L. (2014). How much has the ice bucket challenge achieved? BBC News Magazine. https://www.bbc.com/news/magazine-29013707.

[54] Tuo, G., Feng, Y., & Sarpong, S. (2019). A configurational model of reward-based crowdfunding project characteristics and operational approaches to delivery performance. Decision Support Systems, 120, 60–71.

[55] Tsotsis, A. (2014). Fred Wilson Leads \$23M Funding In CrowdRise, A ‘Charity Water’ For Everyone. TechCrunch Daily. https://techcrunch.com/2014/04/21/fred-wilson-leads-23m-funding-for-crowdrise-a-charity-wate r-for-everyone/.

[56] Ungar, L. (2016). Cancer society hopes crowdfunding attracts Millennial donors, USAToday. https://www.usatoday.com/story/money/2016/02/12/cancer-society-hopes-crowdfunding-brings-i n-millennial-donors/80247050/.

[57] Vesterlund, L. (2003). The informational value of sequential fundraising. Journal of Public Economics, 87(3), 627–657.

[58] Wang, F.Y., Carley, K.M., Zeng, D., & Mao, W. (2007). Social computing: From social informatics to social intelligence. IEEE Intelligent Systems, 22(2), 79–83.

[59] Waters, R.D. (2007). Nonprofit organizations' use of the internet: A content analysis of

communication trends on the internet sites of the philanthropy 400. Nonprofit Management and Leadership, 18(1), 59–76

[60] Waters, R.D., Burnett, E., Lamm, A., & Lucas, J. (2009). Engaging stakeholders through social networking: How nonprofit organizations are using Facebook. Public Relations Review, 35(2), 102–106.

[61] Webber, D. (2004). Understanding charity fundraising events. International Journal of Nonprofit and Voluntary Sector Marketing, 9(2), 122–134.

[62] Wessel, M., Adam, M., & Benlian, A., (2019). The impact of sold-out early birds on option selection in reward-based crowdfunding. Decision Support Systems, 117, 48–61.

[63] Xiao, S., & Yue, Q. (2018). Investors' inertia behavior and their repeated decision-making in online reward-based crowdfunding market. Decision Support Systems, 111, 101–112.

[64] Yoon, K. (1987). A reconciliation among discrete compromise solutions. Journal of the Operational Research Society, 38(3), 277–286.

[65] Zhang, J. (2015). Voluntary information disclosure on social media. Decision Support Systems, 73, 28–36.

[66] Zhang, J., D., & Chow, C., Y. (2015). CoRe: Exploiting the Personalized Influence of Two-dimensional Geographic Coordinates for Location Recommendations, Information Sciences, 29(1), 163–181.

[67] Zhao, H., Jin, B., Liu, Q., Ge, Y., Chen, E., Zhang, X., & Wu, T. (2019). Voice of Charity: Prospecting the Donation Recurrence & Donor Retention in Crowdfunding. IEEE Transactions on Knowledge and Data Engineering.

[68] Zheng, H., Li, D., Wu, J., & Xu, Y. (2014). The role of multidimensional social capital in crowdfunding: A comparative study in China and US. Information & Management, 51(4), 488– 496.

Yung-Ming Li is a Professor at the Institute of Information Management, National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ACM Transactions on Networking, INFORMS Journal on Computing, Production and Operations Management, Decision Sciences, International Journal of Electronic Commerce, Information and Management, Decision Support Systems, European Journal of Operational Research, International Conference on Information Systems (ICIS), Workshop on Information Technology and Systems (WITS), among others.

Jhih-Dong Wu received his M.S. degree from the Institute of Information Management, National Chiao Tung University in Taiwan and B.S. degree in Information Management from the National Yunlin University of Science and Technology, Taiwan. His research interests focus on social commerce and financial technology.

Chin-Yu Hsieh is a Ph.D. student at the Institute of Information Management, National Chiao Tung University in Taiwan. His research interests include artificial intelligence and electronic ecommerce.

Jyh-Hwa Liou received her Ph.D. student from the Institute of Information Management, National Chiao Tung University in Taiwan. She is with the faculty of Hsin Sheng College of Medical Care and Management in Taiwan. Her research interests include electronic commerce and business intelligence. Her research has appeared in Decision Support Systems.

## Highlights

 Crowdfunding platforms have become popular and charities often use these to fundraise.

 We propose a recommendation mechanism for social fundraising to promote the spread of philanthropic fundraising.

The proposed mechanism is built by analyzing the donor’s preferences, the relationship between the donor and fundraiser, and the characteristics of the fundraising dynamics.

The proposed mechanism can effectively discover appropriate donors and relevant campaigns to expedite the fundraising process.
