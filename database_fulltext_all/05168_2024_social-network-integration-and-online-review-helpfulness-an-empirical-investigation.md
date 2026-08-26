---
otero_id: 5168
otero_key: "BD729JA7"
title: "Social Network Integration and Online Review Helpfulness: An Empirical Investigation"
authors: "Zheyuan Pu; Shengli Li; Jiaxuan Wu; Yipeng Liu"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00891"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Social Network Integration and Online Review Helpfulness: An Empirical Investigation

Zheyuan Pu, puzheyuan@pku.edu.cn

Shengli Li , lishengli@pku.edu.cn

Jiaxuan Wu , wujiaxuan@pku.edu.cn

Yipeng Liu , yliu@niu.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Social Network Integration and Online Review Helpfulness: An Empirical Investigation

Zheyuan Pu,<sup>1</sup> Shengli Li,<sup>2</sup> Jiaxuan Wu,<sup>3</sup> Yipeng Liu<sup>4</sup>

<sup>1</sup>Department of Information Management, Peking University, China, puzheyuan@pku.edu.cn <sup>2</sup>Department of Information Management, Peking University, China, lishengli@pku.edu.cn <sup>3</sup>Department of Information Management, Peking University, China, wujiaxuan@pku.edu.cn <sup>4</sup>Department of Operations Management & Information Systems, Northern Illinois University, USA, yliu@niu.edu

## Abstract

While the proliferation of online reviews greatly facilitates consumers’ online purchasing decisions, it also introduces the challenge of information overload. Many review websites have adopted voting systems to help consumers identify helpful reviews. This study contributes to the existing research by examining the impact of social network integration (SNI), an emerging social media feature on online review platforms, on the perceived helpfulness of these reviews. Drawing on data collected on a leading Chinese online review platform, our research reveals a positive impact of SNI on online review helpfulness. Additionally, we demonstrate that the impact of SNI on online review helpfulness can be moderated by different reviewer-related factors. Specifically, the effect of SNI is strengthened by higher reviewer expertise and the establishment of more follower ties and weakened by the amount of peer recognition received by the reviewer. To address the endogeneity issues arising from the reviewers’ self-selection process of SNI, we employed several identification strategies and confirmed the robustness of our results. Furthermore, our analyses of the underlying mechanisms reveal that SNI primarily enhances review helpfulness by motivating reviewers to invest greater effort in generating review content.

Keywords: Online Reviews, Social Network Integration, Review Helpfulness, Electronic Word-of-Mouth

Traci Carte was the accepting senior editor. This research article was submitted on July 22, 2022 and underwent three revisions. Shengli Li is the corresponding author.

## 1 Introduction

Online reviews have become important information sources that assist consumers in making purchasing decisions. As a prominent form of user-generated content (UGC), online reviews have been shown to wield significant influence over sales (Chen et al., 2021; Forman et al., 2008; Ren et al., 2017; Zhou & Duan, 2016). However, the sheer volume of customer reviews on online platforms like Yelp and TripAdvisor has given rise to the challenge of information overload (Malik & Hussain, 2018). To address this issue, many online review websites have introduced systems for users to vote on the helpfulness of reviews, aiding readers in their purchasing decisions (Mudambi & Schuff, 2010). Prior research has shown that online reviews with more helpful votes have a greater impact on consumer purchasing intentions (Kwok & Xie, 2016; Wan, 2015). Consequently, understanding the factors that contribute to online review helpfulness is crucial to all stakeholders, including consumers, businesses, and review websites.

![](/api/attachments/BD729JA7/fulltext/images/3a97379c47f0efe22caa27a56884040b39cf4a150f80af473bfa0362ec825e9d.jpg)  
Figure 1. Examples of SNI from Tripadvisor.com (Left) and Yelp.com (Right)

The influencing factors of online review helpfulness have attracted great attention from academics, with existing studies predominantly focusing on review characteristics (e.g., review length, rating valence, review sentiment) and reviewer attributes (e.g., reviewer expertise, reviewer identity disclosure, and reviewer reputation). More recently, researchers have begun to investigate the rapid integration of social network features on review websites and their impact on review helpfulness. These studies have revealed that social network-related variables, such as centrality measures of the focal reviewer (Meo et al., 2017) and the average degree of centrality of the reviewer’s friends (Bilal et al., 2021), have positive effects on review helpfulness.

A relatively recent addition to online review websites is the social network integration (SNI) feature (Huang et al., 2017). SNI allows users to link their review website accounts with popular social networking platforms like Facebook, Google, and Twitter (as illustrated in Figure 1). Typically, SNI offers users the convenience of registering (and authenticating) themselves using their existing social networking accounts and sharing their reviews posted on review websites with these integrated social networking platforms. Although SNI streamlines account registration, login, and the review-sharing process, it also compromises reviewers’ anonymity to some extent, as their identity information on the connected social networking account can be accessed through the online review platform (Huang et al., 2017). Previous research has also revealed that SNI can impact the process of creating online reviews by, for example, influencing reviewers’ linguistic styles (Fredheim et al., 2015; Huang et al., 2017).

This study examines whether reviewers’ choice of SNI influences the perceived helpfulness of their reviews. SNI can influence review helpfulness either positively or negatively. We draw on the information adoption model and propose that SNI has a positive impact on review helpfulness through both improving review quality and enhancing the credibility of the review source (Sussman & Siegal, 2003; Cheng et al., 2021). Specifically, adopting SNI tends to motivate reviewers to produce higher-quality reviews due to the increased visibility of their identity information on the integrated social networking site and the potential impacts on their social image (Huang et al., 2017). In addition, the disclosure of reviewers’ identity information through SNI also aids consumers in verifying the source credibility of reviews, making these reviews more credible and trustworthy (Kusumasondjaja et al., 2012).

However, previous studies have also illustrated the inhibition effect of reduced anonymity: individuals tend to be more hesitant to self-disclose and typically exhibit lower autonomy in less anonymous situations (Huang et al., 2017; Pu et al., 2020; Suler, 2004). In the context of SNI, reviewers might hesitate to fully express their genuine opinions due to the reduced anonymity (Fredheim et al., 2015; Huang et al., 2017). Consequently, these reviews might be perceived as less helpful since they do not convey reviewers’ genuine feelings.

In summary, whether the positive effects of SNI stemming from improved review quality and source credibility outweigh the negative impacts of reduced anonymity is an intriguing issue. Drawing on a dataset collected from a leading Chinese online review platform, this study estimates the effects of SNI on the perceived helpfulness of online reviews. Next, we examine the moderating effects of various reviewerrelated factors on the main effects. Our findings reveal that reviewers’ choice of SNI significantly enhances the perceived helpfulness of their online reviews. Additionally, this effect is positively moderated by reviewer expertise and the number of follower ties but is negatively moderated by the level of peer recognition received by the reviewer. We conducted robustness tests to further validate our results and employed various identification strategies, such as the matching technique, instrumental variable method, and the Heckman-type two-stage model, to address the endogeneity issue arising from reviewers’ self-selection of SNI. Lastly, we present additional findings on the plausible underlying mechanisms through which SNI positively impacts online review helpfulness.

## 2 Literature Review

## 2.1 Online Review Helpfulness and Its Influencing Factors

Online customer reviews, comprising open-ended user comments and numerical star ratings, can be defined as peer-generated evaluations of products or services posted online (Mudambi & Schuff, 2010). The primary purpose of online reviews is to facilitate the decisionmaking process of other consumers when making purchases (Baek et al., 2012; Mudambi & Schuff, 2010). As a distinct and significant form of UGC, online reviews exert substantial influence on consumer behavior and commercial success and have sparked keen interest among scholars from various research fields, including information systems (Forman et al., 2008; Hong et al., 2016; Huang et al., 2018; Kuan et al., 2015) and marketing (Chintagunta et al., 2010; He et al., 2022). Substantial attention has been devoted to examining online review helpfulness and its influencing factors (Mudambi & Schuff, 2020; Yin et al., 2016), driven by the exponential growth of online reviews and the need to help consumers discern which reviews are more useful. Online review helpfulness is often measured by the number of helpful votes a review receives from fellow readers (Chua & Banerjee, 2014) and can be defined as the extent to which consumers perceive a review as useful in helping them evaluate products or services and make informed purchasing decisions (Liu & Park, 2015; Mudambi & Schuff, 2020; Racherla & Friske, 2012).

Previous work on the influencing factors of online review helpfulness has often centered on review characteristics and reviewer attributes, examining the impact of star ratings and various aspects of review content on review helpfulness, including review characteristics such as rating inconsistency (Baek et al., 2012; Lee et al., 2021), rating extremity (Chua & Banerjee, 2014; Hong et al., 2016; Kuan et al., 2015), review length (Baek et al., 2012; Mudambi & Schuff, 2010), review images (Wu et al., 2020), and review sentiment (Baek et al., 2012; Wang et al., 2020), all of which have demonstrated significant influence on online review helpfulness. Regarding reviewer attributes, prior studies have indicated that reviewer expertise and reputation (Baek et al., 2012; Wang et al., 2020; Zhu et al., 2014), reviewer identity disclosure (Karimi & Wang, 2017; Liu & Park, 2015), and reviewers’ network centrality (Bilal et al., 2021; Meo et al., 2017) also contribute to the helpfulness of their online reviews.

## 2.2 Influence of Social Networking Features on Online Reviews

In recent years, online review platforms have integrated social networking features into their website design to encourage social interactions among users and promote user engagement (Goes et al., 2014; Wang et al., 2018). Multiple studies have found that social networking features have a significant impact on the generation of online reviews through social influence. For instance, socializing features allowing users to follow or connect with others not only make it more likely that reviewers’ ratings will be influenced by their friends’ ratings (Lee et al., 2015; Wang et al., 2018) but they also affect the quantity and quality of their subsequent reviews (Ke et al., 2020). In addition, since the follower-followee relationship forms a social network among reviewers, several studies have further examined the influence of social ties on online review helpfulness (e.g., Bilal et al., 2021; Meo et al., 2017). However, these studies have mainly focused on predicting review helpfulness rather than providing explanatory insights into the relationships between social ties and online review helpfulness.

Another emerging social networking feature is SNI, which has been found to significantly influence the online behaviors of platform users, such as their commenting activity on online news websites (Cho & Kwon, 2015; Fredheim et al., 2015; Suh et al., 2018). Despite its significance and prevalence, there is limited literature exploring the impact of SNI in the context of online product reviews. One notable exception is Huang et al. (2017), which investigated the effects of SNI on online review generation. This research revealed that SNI can affect online reviews in two ways: Allowing users to integrate their Facebook connections into the review platform motivates them to produce more reviews; however, SNI also leads to a decrease in the use of cognitive language and negative expressions, resulting in reviews that are more conforming and less straightforward (Huang et al., 2017). However, clear empirical evidence on whether SNI enhances or reduces the perceived helpfulness of online reviews is still lacking.

This study extends previous research by further investigating how consumers perceive the helpfulness of reviews authored by reviewers who chose to adopt SNI. We contribute to the literature in three ways: First, our study establishes the positive influence of SNI on online review helpfulness. Second, we investigate how this impact of SNI on review helpfulness varies in the presence of various reviewer attributes. Third, we take an additional step by investigating the underlying mechanism through which SNI exerts its impact. Our findings demonstrate that SNI enhances online review helpfulness by motivating reviewers to invest more effort into the review generation process.

## 3 Conceptual Framework and Hypothesis Development

In this section, we formulate several hypotheses and test them empirically. Our first hypothesis pertains to the main effects of SNI on perceived online review helpfulness (H1). We then identify several reviewerrelated factors and examine how these factors moderate the relationship between SNI and online review helpfulness. These reviewer-related factors include reviewer expertise (H2), recognition received by the focal reviewer from peers (H3), and social ties formed around the focal reviewer (H4). Figure 2 depicts the conceptual model of this study.

## 3.1 Effects of SNI on Online Review Helpfulness

The information adoption model proposed by Sussman and Siegal (2003) suggests that argument quality and information source credibility directly influence perceived information usefulness. Accordingly, we argue that the reduced anonymity of reviewers owing to SNI adoption may enhance perceived review helpfulness through two possible underlying mechanisms. As discussed above, SNI enables reviewers to share their reviews on an integrated social media platform, thereby exposing their reviews to their friends. Additionally, by adopting SNI, reviewers give the review platform permission to display reviewers’ profile images and nicknames from the integrated social media platform, making these reviewers more recognizable by other users by providing more personally identifiable information, compared to reviewers not adopting SNI. Thus, these features of SNI effectively reduce the anonymity of reviewers (Cho & Kwon, 2015). Under the first plausible underlying mechanism, the reduction of reviewers anonymity increases social presence (Huang et al., 2017), which motivates reviewers to invest more effort when creating online reviews and results in higher review quality (Omernick & Sood, 2013; Pu et al., 2020; Qiu & Kumar, 2017). Previous literature has also shown that users tend to contribute to public goods in social media because of social effects (Zhang & Zhu, 2011). Therefore, reviewers adopting SNI are likely to provide higher-quality reviews to benefit their friends on the integrated social media platform, which enhances their social image and reputation (Huang et al., 2017; Qiu & Kumar, 2017; Zhang & Zhu, 2011).

The second plausible underlying mechanism concerns source credibility. Given the growing challenges posed by manipulated online reviews (Filieri et al., 2018; Luca & Zervas, 2016), SNI can alleviate this issue by enhancing the credibility of the review source. Owing to the reduced anonymity of reviewers, SNI can assist readers in verifying the origin of reviews by offering additional information cues through social media (e.g., shared reviews or reviewers’ profile images and nicknames on social media platforms), thereby making the information source more trustworthy. Indeed, prior research has shown that reducing the content creator’s anonymity directly contributes to users’ perceived source credibility in social media (Chesney & Su, 2010). Furthermore, it is a costly endeavor to fake a reviewer’s account (and thus the reviews) linked to a social media platform. Therefore, observing a symbol indicating SNI adoption on a review platform should alleviate review readers’ concerns regarding the authenticity of the review.

However, SNI may also have a negative impact on online review helpfulness through a countervailing mechanism—the inhibition effect of reduced anonymity. As previously mentioned, adopting SNI decreases reviewers’ anonymity. Prior research suggests that individuals tend to exhibit lower autonomy and feel more hesitant to self-disclose in less anonymous online situations (Huang et al., 2017; Pu et al., 2020; Suler, 2004) because anonymity allows people to separate their online actions from their reallife identities, making them less concerned about the potential negative consequences arising from their online behavior (Suler, 2004). As a result, reviewers adopting SNI may be less willing to write reviews based on their genuine consumption experience (Cho et al., 2012; Dyussembayeva et al., 2020), increasing the likelihood that their reviews will be perceived as less helpful since they may not accurately reflect their honest and uncensored opinions about the product or service under review (Huang et al, 2017).

![](/api/attachments/BD729JA7/fulltext/images/0ff69af2f1b041c6f56cf0a0e2a9e98cb82f57e5b89534807f6cfad11f088583.jpg)  
Figure 2. Conceptual Model

In summary, the impact of SNI on online review helpfulness depends on whether the positive effects of enhanced review quality and source credibility outweigh the negative effects related to the reduced perception of genuine opinions. Note that it is generally challenging for readers to determine whether a review reflects the reviewer’s genuine opinions due to information asymmetry between reviewers and review readers. However, high review quality can be directly observed by readers, while enhanced credibility can be assessed through certain information cues. Consequently, we believe that it is unlikely that the negative impacts of SNI will outweigh the positive effects, leading us to hypothesize:

H1: Online reviews generated by reviewers with SNI will be perceived as more helpful than those posted by reviewers without SNI.

## 3.2 Moderating Role of Reviewer-Related Factors

As previously discussed, the positive impact of SNI on the perceived helpfulness of online reviews manifests through two potential pathways: enhanced review quality and improved source credibility. Therefore, the anticipated positive effect of SNI may vary depending on the specific reviewer’s content creation ability and their desire to enhance their online image. In this subsection, we identify several reviewer-related factors, including reviewer expertise, peer recognition, and social ties, and propose that the effect of SNI is likely to be moderated by these factors.

## 3.2.1 Reviewer Expertise

Expertise can be defined as “the extent to which the resource is perceived as being capable of providing correct information” (Bristor, 1990). Reviewer expertise is associated with reviewers’ platform experience and their knowledge of online review generation, which has been extensively studied as a key factor affecting the perceived helpfulness of online reviews (Hlee, 2020; Liu & Park, 2015; Racherla & Friske, 2012; Zhu et al., 2014). We now examine the moderating role of reviewer expertise in the relationship between SNI and review helpfulness.

In general, greater expertise in a specific field corresponds to increased practice and experience in that area (Ericsson et al., 1993). Consequently, it is reasonable to assume that reviewers with more experience in writing reviews will be better equipped to produce high-quality content (Zhu et al., 2014). For instance, experienced reviewers often exhibit higher levels of elaboration and engagement, enabling them to provide valuable and informative details about the product or service under review (Hlee, 2020). As a result, the additional time and effort invested by reviewers with higher levels of expertise in writing reviews on the platform can yield more substantial improvements in the quality of their online reviews, compared to those with lower levels of expertise. Therefore, we hypothesize that since SNI motivates reviewers to expend greater effort during the review generation process, the impact of SNI on online review helpfulness is likely to be stronger among reviewers with greater expertise.

Furthermore, reviewer expertise may also strengthen the positive impact of SNI on perceived review helpfulness via the mechanism of enhanced review source credibility. The prevalence of fake reviews in recent years has made consumers increasingly skeptical toward online reviews (He et al., 2022; Luca & Zervas, 2016). In particular, Filieri et al. (2018) found that consumers are aware that service providers collaborate with high-level reviewers to post promotional reviews to boost their ratings or rankings on third-party platforms, underscoring the urgent need for such reviewers to bolster the perceived credibility of their online reviews. Therefore, compared to less experienced reviewers, SNI is likely to be more advantageous for reviewers with higher expertise seeking to enhance the perceived source credibility of their reviews. Consequently, the influence of SNI through the enhancement of review source credibility is expected to be more pronounced for reviewers with higher expertise. Building on these premises, we propose the following hypothesis:

H2: Reviewer expertise positively moderates the relationship between SNI and online review helpfulness.

## 3.2.2 Peer Recognition

Peer recognition is a testament to a user’s valuable contributions as acknowledged by their community peers (Forman et al., 2008; Jabr et al., 2014). Previous studies have shown that receiving recognition from peers motivates users to more actively engage in content contribution (Burtch et al., 2022; Guan et al., 2018). Therefore, it can be inferred that reviewers who have received more peer recognition are likely to be more motivated to contribute content on review websites. In parallel, we posit that SNI can influence user behavior on online platforms by encouraging individuals to enhance their content creation efforts. This encouragement stems from the desire to bolster their social image and reputation within the network. This mechanism suggests that SNI could influence online review helpfulness by motivating reviewers to put more effort into their contributions. However, previous studies offer a refined understanding, with Chen et al. (2017) revealing that the motivation derived from seeking to improve one’s social image may not significantly increase content contribution among those who are already highly motivated, such as users with extensive peer recognition.

Further complicating this dynamic is the concept of inertia. Achieving peer recognition might lead content creators to become complacent, relying on strategies that have led to past success rather than innovating or enhancing their contributions (Burtch et al., 2022). This inertia could be detrimental in the context of online review platforms, where the novelty and uniqueness of content critically influence its perceived usefulness to consumers, especially in an environment saturated with competing reviews (Zhang et al., 2023). Therefore, even if SNI motivates highly recognized reviewers to intensify their content creation efforts, the effectiveness of these efforts in improving review helpfulness may be undermined by a lack of novelty in their contributions. Based on these arguments, we propose the following hypothesis:

H3: Peer recognition negatively moderates the relationship between SNI and online review helpfulness.

## 3.2.3 Social Ties

Social ties among platform users can be categorized into two types: follower ties (or incoming ties) and followee ties (or outgoing ties), based on their direction relative to the focal user (Rishika & Ramaprasad, 2019). Both types of social ties have been widely employed to predict online review helpfulness in previous studies (Cheng & Ho, 2015; Racherla & Friske, 2012; Zhu et al., 2014). In contrast to these studies, our focus is on exploring how these two types of social ties moderate the impact of a novel social networking feature, SNI, on the perceived helpfulness of online reviews.

Previous research suggests that the establishment of follower ties plays a crucial role in bolstering users motivation to shape their online image. This motivation, in turn, drives users to expend greater effort, resulting in higher-quality contributions (Qiu & Kumar, 2017). In our specific context, gaining more follower ties translates to a larger audience and heightened expectations from this audience. Consequently, reviewers with more followers are incentivized to invest more effort in writing their reviews. This heightened effort stems from the enhanced social presence and reduced anonymity associated with SNI, as maintaining a favorable social image becomes more important. This phenomenon reinforces the impact of SNI on the perceived helpfulness of reviews, particularly for reviewers with a significant number of follower ties. Furthermore, previous research has shown that as reviewers gain popularity among their peers, their reviews tend to exhibit greater objectivity (Goes et al., 2014). This enhanced objectivity can help mitigate the potential negative impact of SNI by reducing the influence of decreased anonymity on how readers perceive the authenticity of expressions in reviews (Lee & Koo, 2012). However, it is worth noting that reviewers with a large number of followers may also face heightened scrutiny regarding the authenticity of their reviews. The prevalence of promotional and fake reviews has made it common for service providers to collaborate with opinion leaders with a substantial number of followers to promote their products or services. For instance, restaurants often provide free meal coupons to prominent reviewers (those with many followers) in exchange for favorable reviews, thereby diminishing the credibility of such reviews (Luca & Zervas, 2016; Mayzlin et al., 2014). Consequently, displaying an SNI-adoption symbol will result in a more prominent and beneficial boost in review source credibility for these reviewers. Based on this, we believe that the number of follower ties will amplify the effects of SNI on online review helpfulness.

Meanwhile, followee ties bring fresh perspectives and novel information from other community members, reducing uncertainty about community norms and facilitating social learning from the strengths of others (Rishika & Ramaprasad, 2019; Wang & Wang, 2020). Reviewers with more followee ties will thus be better equipped to generate high-quality reviews, given their exposure to diverse viewpoints and information sources. As a result, the increased effort induced by SNI adoption will become more effective in enhancing review quality for reviewers with a higher number of followee ties. This reinforces the main effects of SNI on review helpfulness. In light of these considerations, we propose the following hypotheses concerning the moderating effects of these two types of social ties:

H4a: The number of follower ties positively moderates the relationship between SNI and online review helpfulness.

H4b: The number of followee ties positively moderates the relationship between SNI and online review helpfulness.

## 4 Research Methodology

## 4.1 Data Collection

We collected data from Qunar.com, the world’s largest Chinese online travel website. Similar to Tripadvisor.com in the United States, this platform allows users to share reviews on their hotel experiences and vote on the helpfulness of other users’ reviews.

Most importantly, Qunar.com offers users the option to integrate with major Chinese social networking websites (i.e., SNI), such as Sina Weibo, Baidu.com, Renren.com, etc. It is important to note that this integration is an opt-in feature on Qunar.com. When users choose SNI, their default login method becomes their social networking account. Upon opting to use SNI, the reviewer allows Qunar.com to use the user’s nickname, profile image, and social network information from the integrated social networking platform and to automatically share the user’s review on the integrated platform. Also, a symbol below the user’s profile image and nickname is activated, indicating that the user has selected the SNI option. Qunar.com also rates each reviewer in terms of reviewwriting experience—given by Levels 1-7, with Level 7 indicating the most expertise. Figure 3 provides a screenshot of SNI on Qunar.com.

We developed a web crawler to collect online reviews for all hotels in the city of Beijing posted on Qunar.com between November 2017 and November 2020, yielding a dataset of 2,489,626 reviews associated with 10,459 hotels. All data was collected in December 2020. Some reviews on Qunar.com were submitted by anonymous users, and characteristics related to those reviewers were unavailable. In addition, star ratings for some hotels were also unavailable, making it impossible to control for their service quality. We thus deleted these reviews, leaving 426,927 reviews for further analysis. Table 1 shows the operationalization of variables. Specifically, our dependent variable is measured by the number of helpful votes received by each review. The independent variable, SNI\_or\_not, indicates whether the reviewer has opted to use the SNI feature. The moderators include reviewer expertise (ExpLevel), peer recognition (HelpOthers), follower ties (Followers), and followee ties (Followees). Reviewer expertise is measured using each reviewer’s platform level. Peer recognition, follower ties, and followee ties are measured using the logarithmic form of each reviewer’s cumulative helpful votes, followers, and followees, respectively.

![](/api/attachments/BD729JA7/fulltext/images/d3b4f07c5fd3008eb6f494b1ebba527b2830617028ed06852a694503c8d38f38.jpg)  
Figure 3. An Example of SNI on Qunar.com

Table 1. Operationalization of Variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td colspan="2">Dependent variable</td></tr><tr><td>HelpfulVotes</td><td>The number of helpful votes received by a review</td></tr><tr><td colspan="2">Independent variable</td></tr><tr><td>SNI_or_not</td><td>Whether a reviewer chose to adopt SNI or not; a value of 1 indicates the reviewer adopted SNI</td></tr><tr><td colspan="2">Moderating variables</td></tr><tr><td>ExpLevel</td><td>Reviewer level of expertise awarded by the platform, with integer values from 1 to 7 (7 indicating greatest expertise)</td></tr><tr><td>HelpOthers</td><td>Logarithmic form of cumulative helpful votes a reviewer received from other users</td></tr><tr><td>Followees</td><td>Logarithmic form of the number of users a reviewer follows</td></tr><tr><td>Followers</td><td>Logarithmic form of the number of users following a reviewer</td></tr><tr><td colspan="2">Control variables</td></tr><tr><td>Duration</td><td>Exposure duration of the review (elapsed days from the date when the review was posted to the date of data collection)</td></tr><tr><td>ReviewValence</td><td>The star rating given by the reviewer</td></tr><tr><td>Pageview</td><td>The number of times a review was browsed</td></tr><tr><td>ReplyNum</td><td>The number of replies a review received</td></tr><tr><td>HotelStar</td><td>Four levels, from 2 to 5</td></tr><tr><td>ReviewNum</td><td>Logarithmic form of the number of online reviews a hotel has</td></tr></table>

## 4.2 Model Specification

To test our hypotheses, we estimated the following regression models specified by Equations (1) to (3):

Model 1 contains only control variables:

$$
H e l p f u l V o t e s = \beta_ {0} + \theta C o n t r o l s + \varepsilon\tag{1}
$$

Model 2 includes the independent variable “whether a reviewer chose SNI or not” and control variables:

$$
\begin{array}{r} H e l p f u l V o t e s = \beta_ {0} + \beta_ {1} S N I \_ o r \_ n o t \\ + \theta C o n t r o l s + \varepsilon \end{array}\tag{2}
$$

Model 3 adds reviewer-related factors and interaction terms to Model 2:

$$
\begin{array}{l} H e l p f u l V o t e = \beta_ {0} + \beta_ {1} S N I \_ o r \_ n o t \\ \qquad + \beta_ {2} E x p L e v e l \\ \qquad + \beta_ {3} H e l p O t h e r s \\ \qquad + \beta_ {4} F o l l o w e r s \\ \qquad + \beta_ {5} F o l l o w e e s \\ \qquad + \beta_ {6} S N I \_ o r \_ n o t * E x p L e v e l \\ \qquad + \beta_ {7} S N I \_ o r \_ n o t \\ \qquad * H e l p O t h e r s \\ \qquad + \beta_ {8} S N I \_ o r \_ n o t \\ \qquad * F o l l o w e r s \\ \qquad + \beta_ {9} S N I \_ o r \_ n o t \\ \qquad * F o l l o w e e s + \theta C o n t r o l s \\ \qquad + \varepsilon \end{array}\tag{3}
$$

The control variables in our study include the exposure duration of an online review (Duration), the review’s rating valence (ReviewValence), the review’s page view (Pageview), the number of replies the review received (ReplyNum), the hotel star-rating level (HotelStar), and the logarithmic form of the review volume for the hotel (ReviewNum). Previous research has shown that review valence significantly affects the number of helpful votes received by reviews (Kuan et al., 2015). Regarding replies to online reviews, both user and manager replies have been found to contribute to online review helpfulness (Moro & Esmerado, 2020; Ou & Chua, 2021). Furthermore, hotels with higher star ratings are typically associated with better service quality, which may positively impact review helpfulness (Filieri et al., 2020). Lastly, review volume serves as an indicator of a hotel’s popularity and may also exert an impact on online review helpfulness (Karimi & Wang, 2017).

We chose the negative binomial regression model for our main analysis because HelpfulVotes, a count variable, exhibited significant overdispersion (Ver Hoef & Boveng, 2007), as demonstrated by its variance (0.121) being significantly larger than its mean (0.060). This decision is further supported by the results of likelihoodratio tests across all regressions, which indicated significant over-dispersion (p < 0.01). Recognizing that a reviewer may contribute multiple hotel reviews and that such reviews are likely to share correlated characteristics, we clustered the standard errors at the reviewer level. Table 2 and Table 3 present the descriptive statistics and the correlation coefficients of all variables, respectively. We also checked the variance inflation factors (VIFs) for all independent variables and determined that multicollinearity was not a concern.

Table 2. Descriptive Statistics

<table><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Review level</td></tr><tr><td>HelpfulVotes</td><td>426,927</td><td>0.060</td><td>0.348</td><td>0</td><td>26</td></tr><tr><td>Duration</td><td>426,927</td><td>585.922</td><td>308.377</td><td>0</td><td>1168</td></tr><tr><td>ReviewValence</td><td>426,927</td><td>4.523</td><td>0.981</td><td>1</td><td>5</td></tr><tr><td>Pageview</td><td>426,927</td><td>10.400</td><td>19.281</td><td>0</td><td>1828</td></tr><tr><td>ReplyNum</td><td>426,927</td><td>0.617</td><td>0.719</td><td>0</td><td>242</td></tr><tr><td colspan="6">Reviewer level</td></tr><tr><td>SNI_or_not</td><td>426,927</td><td>0.075</td><td>0.264</td><td>0</td><td>1</td></tr><tr><td>ExpLevel</td><td>426,927</td><td>1.638</td><td>0.963</td><td>1</td><td>7</td></tr><tr><td>HelpOthers</td><td>426,927</td><td>0.376</td><td>0.672</td><td>0</td><td>7.731</td></tr><tr><td>Followers</td><td>426,927</td><td>0.004</td><td>0.089</td><td>0</td><td>6.363</td></tr><tr><td>Followees</td><td>426,927</td><td>0.002</td><td>0.074</td><td>0</td><td>5.778</td></tr><tr><td colspan="6">Hotel level</td></tr><tr><td>HotelStar</td><td>426,927</td><td>3.047</td><td>1.029</td><td>2</td><td>5</td></tr><tr><td>ReviewNum</td><td>426,927</td><td>7.147</td><td>0.968</td><td>0.693</td><td>9.417</td></tr></table>

Table 3. Correlation Matrix of Variables

<table><tr><td>Variables</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td></tr><tr><td>(1) HelpfulVotes</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) SNI_or_not</td><td>0.02*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) ExpLevel</td><td>0.03*</td><td>0.27*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) HelpOthers</td><td>0.25*</td><td>0.18*</td><td>0.63*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5) Followers</td><td>0.06*</td><td>0.08*</td><td>0.13*</td><td>0.20*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6) Followees</td><td>0.05*</td><td>0.09*</td><td>0.10*</td><td>0.15*</td><td>0.70*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(7) Duration</td><td>0.09*</td><td>0.06*</td><td>0.02*</td><td>0.09*</td><td>0.02*</td><td>0.01*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(8) ReviewValence</td><td>-0.11*</td><td>-0.01*</td><td>-0.02*</td><td>-0.06*</td><td>-0.01*</td><td>-0.00</td><td>-0.07*</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>(9) Pageview</td><td>0.21*</td><td>0.04*</td><td>0.07*</td><td>0.12*</td><td>0.09*</td><td>0.08*</td><td>0.32*</td><td>-0.04*</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>(10) ReplyNum</td><td>0.04*</td><td>0.00</td><td>-0.01*</td><td>0.00</td><td>0.01*</td><td>0.01*</td><td>-0.03*</td><td>0.05*</td><td>0.04*</td><td>1.00</td><td></td><td></td></tr><tr><td>(11) HotelStar</td><td>0.06*</td><td>0.03*</td><td>0.06*</td><td>0.11*</td><td>0.02*</td><td>0.01*</td><td>0.02*</td><td>0.11*</td><td>0.02*</td><td>-0.04*</td><td>1.00</td><td></td></tr><tr><td>(12) ReviewNum</td><td>0.02*</td><td>0.01*</td><td>-0.01*</td><td>0.03*</td><td>0.00*</td><td>-0.00</td><td>0.06*</td><td>0.15*</td><td>-0.02*</td><td>0.07*</td><td>0.50*</td><td>1.00</td></tr><tr><td colspan="13">Note: *p&lt; 0.05</td></tr></table>

## 5 Main Results

## 5.1 Results of Hypothesis Testing

Table 4 presents the regression results. The estimation of Model 1 indicates that the exposure duration, hotel level, number of replies for a review, review page view, and review volume of the hotel were all positively associated with online review helpfulness. In contrast, review valence was negatively related to online review helpfulness. The coefficient of SNI\_or\_not in Model 2 is significantly positive $( { \hat { \beta } } _ { 1 } =$ $0 . 1 1 0 , p < 0 . 0 1 \rangle$ ), indicating that reviews written by reviewers who opted for SNI received more helpful votes. Regarding effect size, reviews from those who opted for SNI received, on average, 11.6% more helpful votes compared to those from reviewers who did not opt for SNI. Thus, H1 is supported.

Model 3 shows how SNI interacts with reviewer-related factors. First, the coefficient of SNI\_or\_not × ExpLevel is significantly positive $( ~ \hat { \beta } _ { 6 } ~ = ~ 0 . 4 8 3 , ~ p ~ < ~ 0 . 0 1 )$ indicating that the positive influence of SNI on online review helpfulness was stronger for reviewers with higher expertise. Thus, H2 is supported. Second, the coefficient of SNI\_or\_not × HelpOthers is negative $( \hat { \beta } _ { 7 }$ $= - 0 . 9 0 3 , p < 0 . 0 1 )$ , suggesting that the impact of SNI on review helpfulness was weakened by increased recognition from peers on online review websites, confirming H3. The coefficients of SNI\_or\_not × Followers and SNI\_or\_not × Followees are 0.770 (p < 0.01) and -0.314 (p > 0.1), respectively. Therefore, a higher number of follower ties strengthened the effect of SNI on online review helpfulness, while the number of followee ties did not exhibit a significant moderating effect; thus H4a is supported and H4b is not supported. One plausible explanation for the insignificant moderating role of followee ties is as follows: While we anticipate that more followee ties offer richer and diversified information sources, which in turn should help improve the focal reviewer’s review generation skills, following more reviewers may also lead to information overload due to the conflicting information posted by others (Wei et al., 2021). This could weaken the positive social learning effects of followee ties, resulting in an insignificant moderation effect.

Table 4. Results of Negative Binomial Regression Analysis

<table><tr><td rowspan="2"></td><td colspan="3">DV: HelpfulVotes</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>SNI_or_not</td><td></td><td>0.110***(0.031)</td><td>0.053(0.062)</td></tr><tr><td>ExpLevel</td><td></td><td></td><td>-1.064***(0.016)</td></tr><tr><td>HelpOthers</td><td></td><td></td><td>2.121***(0.017)</td></tr><tr><td>Followers</td><td></td><td></td><td>-1.467***(0.197)</td></tr><tr><td>Followees</td><td></td><td></td><td>0.388(0.325)</td></tr><tr><td>SNI_or_not × ExpLevel</td><td></td><td></td><td>0.483***(0.037)</td></tr><tr><td>SNI_or_not × HelpOthers</td><td></td><td></td><td>-0.903***(0.040)</td></tr><tr><td>SNI_or_not × Followers</td><td></td><td></td><td>0.770***(0.214)</td></tr><tr><td>SNI_or_not × Followees</td><td></td><td></td><td>-0.314(0.332)</td></tr><tr><td>Duration</td><td>0.001***(0.000)</td><td>0.001***(0.000)</td><td>0.001***(0.000)</td></tr><tr><td>ReviewValence</td><td>-0.431***(0.006)</td><td>-0.431***(0.006)</td><td>-0.308***(0.006)</td></tr><tr><td>Pageview</td><td>0.022***(0.000)</td><td>0.022***(0.000)</td><td>0.013***(0.000)</td></tr><tr><td>ReplyNum</td><td>0.197***(0.021)</td><td>0.197***(0.021)</td><td>0.155***(0.032)</td></tr><tr><td>HotelStar</td><td>0.302***(0.009)</td><td>0.300***(0.009)</td><td>0.200***(0.009)</td></tr><tr><td>ReviewNum</td><td>0.137***(0.011)</td><td>0.137***(0.011)</td><td>0.085***(0.010)</td></tr><tr><td>Constant</td><td>-4.171***(0.072)</td><td>-4.179***(0.073)</td><td>-3.555***(0.069)</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.0957</td><td>0.0958</td><td>0.2349</td></tr><tr><td>Observations</td><td>426,927</td><td>426,927</td><td>426,927</td></tr><tr><td colspan="4">Note: *p&lt;0.1; **p&lt;0.05; ***p&lt;0.01, cluster-robust standard errors are in parentheses</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01, cluster-robust standard errors are in parentheses

## 5.2 Robustness Checks

## 5.2.1 Alternative Estimation Methodology

A substantial proportion of the reviews (approximately 95.2%) in our dataset did not receive any helpful votes, suggesting that our dependent variable may have had an excessive number of zero values. As a remedy, we adopted the zero-inflated negative binomial regression method to reexamine our hypotheses. Additionally, we performed an OLS estimation to serve as an alternative robustness check. The results from these estimations, detailed in Table 5, are qualitatively consistent with the negative binomial regression analysis.

## 5.2.2 Addressing the Endogeneity Issue Caused by Reviewers’ Self-Selection of SNI

There may have been a potential bias in our estimation coming from the self-selection process of the key independent variable ??????\_????\_??????. It is possible that the number of helpful votes a review receives depends on unobservable factors that could also influence the reviewer’s decision to adopt SNI. For instance, reviewers with a stronger motivation to build a reputation on the review website might be more inclined to adopt SNI. These reviewers, driven by the same motivation, might also tend to produce higher-quality reviews. Consequently, our estimation of SNI’s effects could have been subject to bias unless we addressed this potential endogeneity issue (Clougherty et al., 2015). To alleviate such concerns, we utilized several identification strategies to test the robustness of our previous analysis.

First, we employed the propensity score matching (PSM) approach to control for the self-selection problem on observable factors. PSM, originally developed for the evaluation of labor market policies (Dehejia & Wahba, 1999), has become a widely utilized empirical method across various research fields. In this study, we began by considering a set of variables that could be associated with reviewers’ SNI adoption and estimated the propensity score of choosing to use SNI using the logit model. We then applied the nearestneighbor matching strategy to assign a matched review for each review in the treatment group (reviews posted by reviewers who chose SNI). Finally, we conducted a negative binomial regression on the matched sample. In calculating the propensity score, we included several covariates, such as the number of follower ties and followee ties of a reviewer (FollowerNum and FolloweeNum), the reviewer’s level of expertise (ExpLevel), the number of historical helpful votes received by the reviewer from peers (HelpOthersNum), the star rating of the hotel (HotelStar), the average review rating of the hotel (AvgRating), and the exposure duration of the review (Duration). Table 6 presents the regression results of the logit model and shows that all covariates are significantly related to the choice of SNI. Table 7 shows that the biases of all covariates decreased to below 10% after PSM. The results of the negative binomial regression analysis using the matched samples are presented in the first column of Table 8. Notably, the estimated coefficient of SNI remains significantly positive, indicating that our findings remain robust after controlling for potential observable confounders.

Second, we exploited the instrumental variable method using two-stage least squares (2SLS) estimation to further address endogeneity concerns. Specifically, we chose the number of followees who adopted SNI and the proportion of followees who adopted SNI as the instrument variables for two primary reasons. First, we anticipated that reviewers who follow more users who have adopted SNI are more likely to adopt SNI themselves due to social influence. Second, the choices of adopting SNI made by a reviewer’s followees are unlikely to directly affect the review helpfulness of the focal reviewer. The Cragg-Donald Wald F-statistic of the first-stage regression was 1340.545, indicating that the weak instrument variable was not a concern. Further, we conducted the Hansen’s J of overidentifying restrictions to ensure the validity of our instruments (Hansen, 1982). The test statistics (J statistic = 2.112, p = 0.146) did not reject the null hypothesis that the instruments are valid, thus confirming the legitimacy of our instruments. The results of the second-stage regression are presented in the second column of Table 8, which shows that the positive impact of SNI remains robust.

Table 5. Results of Alternative Estimation Methodology

<table><tr><td rowspan="2"></td><td colspan="3">Zero-inflated negative binomial regression (DV: HelpfulVotes)</td><td colspan="3">OLS regression (DV: HelpfulVotes)</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>SNI_or_not</td><td></td><td>0.109*** (0.031)</td><td>0.065 (0.062)</td><td></td><td>0.012*** (0.003)</td><td>-0.009 (0.010)</td></tr><tr><td>ExpLevel</td><td></td><td></td><td>-1.084*** (0.016)</td><td></td><td></td><td>-0.073*** (0.002)</td></tr><tr><td>HelpOthers</td><td></td><td></td><td>2.170*** (0.020)</td><td></td><td></td><td>0.181*** (0.003)</td></tr><tr><td>Followers</td><td></td><td></td><td>-1.576*** (0.189)</td><td></td><td></td><td>-0.056* (0.033)</td></tr><tr><td>Followees</td><td></td><td></td><td>0.464 (0.355)</td><td></td><td></td><td>0.051 (0.038)</td></tr><tr><td>SNI_or_not × ExpLevel</td><td></td><td></td><td>0.506*** (0.037)</td><td></td><td></td><td>0.024*** (0.006)</td></tr><tr><td>SNI_or_not × HelpOthers</td><td></td><td></td><td>-0.957*** (0.041)</td><td></td><td></td><td>-0.067*** (0.009)</td></tr><tr><td>SNI_or_not × Followers</td><td></td><td></td><td>0.847*** (0.206)</td><td></td><td></td><td>0.189*** (0.059)</td></tr><tr><td>SNI_or_not × Followees</td><td></td><td></td><td>-0.378 (0.361)</td><td></td><td></td><td>0.004 (0.056)</td></tr><tr><td>Duration</td><td>0.001*** (0.000)</td><td>0.001*** (0.000)</td><td>0.001*** (0.000)</td><td>0.000*** (0.000)</td><td>0.000*** (0.000)</td><td>-0.000 (0.000)</td></tr><tr><td>ReviewValence</td><td>-0.432*** (0.006)</td><td>-0.432*** (0.006)</td><td>-0.295*** (0.006)</td><td>-0.039*** (0.001)</td><td>-0.039*** (0.001)</td><td>-0.033*** (0.001)</td></tr><tr><td>Pageview</td><td>0.022*** (0.000)</td><td>0.022*** (0.000)</td><td>0.012*** (0.000)</td><td>0.004*** (0.000)</td><td>0.004*** (0.000)</td><td>0.004*** (0.000)</td></tr><tr><td>ReplyNum</td><td>0.216*** (0.016)</td><td>0.216*** (0.016)</td><td>0.186*** (0.014)</td><td>0.012*** (0.004)</td><td>0.012*** (0.004)</td><td>0.012*** (0.004)</td></tr><tr><td>HotelStar</td><td>0.302*** (0.009)</td><td>0.301*** (0.009)</td><td>0.193*** (0.009)</td><td>0.019*** (0.001)</td><td>0.019*** (0.001)</td><td>0.012*** (0.001)</td></tr><tr><td>ReviewNum</td><td>0.136*** (0.011)</td><td>0.137*** (0.011)</td><td>0.079*** (0.010)</td><td>0.012*** (0.001)</td><td>0.012*** (0.001)</td><td>0.010*** (0.001)</td></tr><tr><td>Constant</td><td>-4.121*** (0.074)</td><td>-4.130*** (0.074)</td><td>-3.273*** (0.073)</td><td>0.037*** (0.006)</td><td>0.036*** (0.006)</td><td>0.111*** (0.006)</td></tr><tr><td>Observations</td><td>426,927</td><td>426,927</td><td>426,927</td><td>426,927</td><td>426,927</td><td>426,927</td></tr><tr><td colspan="7">Note: *p&lt;0.1; **p&lt;0.05; ***p&lt;0.01, cluster-robust standard errors are in parentheses</td></tr></table>

Table 6. Logit Regression During Calculating Propensity Scores

<table><tr><td></td><td>DV: SNI_or_not</td></tr><tr><td>FollowerNum</td><td>-0.032***(0.005)</td></tr><tr><td>FolloweeNum</td><td>0.107***(0.014)</td></tr><tr><td>ExpLevel</td><td>0.763***(0.005)</td></tr><tr><td>HelpOthersNum</td><td>0.002***(0.001)</td></tr><tr><td>HotelStar</td><td>0.047***(0.006)</td></tr><tr><td>AvgRating</td><td>0.103***(0.028)</td></tr><tr><td>Duration</td><td>0.001***(0.000)</td></tr><tr><td>Constant</td><td>-5.038***(0.123)</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.1104</td></tr><tr><td>Observations</td><td>426,927</td></tr><tr><td colspan="2">Note: *p&lt;0.1; **p&lt;0.05; ***p&lt;0.01</td></tr></table>

Table 7. Comparison of Biases Before and After Propensity Score Matching

<table><tr><td rowspan="3"></td><td colspan="3">Before Matching</td><td colspan="3">After Matching</td></tr><tr><td colspan="2">Mean</td><td rowspan="2">Bias (%)</td><td colspan="2">Mean</td><td rowspan="2">Bias (%)</td></tr><tr><td>Treated</td><td>Control</td><td>Treated</td><td>Control</td></tr><tr><td>FollowerNum</td><td>0.286</td><td>0.015</td><td>5.5</td><td>0.052</td><td>0.066</td><td>-0.3</td></tr><tr><td>FolloweeNum</td><td>0.211</td><td>0.003</td><td>6.0</td><td>0.025</td><td>0.025</td><td>-0.0</td></tr><tr><td>ExpLevel</td><td>2.539</td><td>1.565</td><td>92.2</td><td>2.512</td><td>2.509</td><td>0.3</td></tr><tr><td>HelpOthersNum</td><td>5.225</td><td>0.986</td><td>14.4</td><td>3.032</td><td>2.627</td><td>1.4</td></tr><tr><td>HotelStar</td><td>3.161</td><td>3.038</td><td>11.9</td><td>3.160</td><td>3.144</td><td>1.5</td></tr><tr><td>AvgRating</td><td>4.502</td><td>4.503</td><td>-0.5</td><td>4.501</td><td>4.505</td><td>-1.5</td></tr><tr><td>Duration</td><td>646.9</td><td>581.0</td><td>21.5</td><td>645.8</td><td>652.8</td><td>-2.3</td></tr></table>

Table 8. Regression Results After Correcting for Self-Selection Bias

<table><tr><td rowspan="2"></td><td colspan="3">DV: HelpfulVotes</td></tr><tr><td>(1) PSM</td><td>(2) 2SLS</td><td>(3) Heckman</td></tr><tr><td>SNI_or_not</td><td>0.176***(0.041)</td><td>0.800***(0.141)</td><td>0.751***(0.024)</td></tr><tr><td>Duration</td><td>0.001***(0.000)</td><td>-0.000***(0.000)</td><td>-0.000***(0.000)</td></tr><tr><td>ReviewValence</td><td>-0.396***(0.018)</td><td>-0.038***(0.001)</td><td>-0.038***(0.001)</td></tr><tr><td>Pageview</td><td>0.022***(0.001)</td><td>0.004***(0.000)</td><td>0.004***(0.000)</td></tr><tr><td>ReplyNum</td><td>0.196***(0.042)</td><td>0.012***(0.004)</td><td>0.012***(0.001)</td></tr><tr><td>HotelStar</td><td>0.302***(0.023)</td><td>0.011***(0.002)</td><td>0.011***(0.001)</td></tr><tr><td>ReviewNum</td><td>0.125***(0.028)</td><td>0.016***(0.001)</td><td>0.016***(0.001)</td></tr><tr><td>Constant</td><td>-4.129***(0.182)</td><td>-0.012(0.011)</td><td>-0.009*(0.005)</td></tr><tr><td>Lambda (IMR)</td><td>-</td><td>-</td><td>-0.365***(0.012)</td></tr><tr><td>Observations</td><td>63,890</td><td>426,927</td><td>426,927</td></tr><tr><td colspan="4">Note: *p&lt;0.1; **p&lt;0.05; ***p&lt;0.01, cluster-robust standard errors are in parentheses (except for the Heckman model).</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01, cluster-robust standard errors are in parentheses (except for the Heckman model)

Next, we employed the Heckman two-stage model as an additional approach to address endogeneity (Heckman, 1979). This econometric technique has been widely utilized in the fields of economics and management to tackle the self-selection issue (Clougherty et al., 2015). In the first stage, we estimated a probit model on whether a reviewer adopted SNI in order to obtain an adjustment term, namely the inverse Mills ratio (IMR). In the second stage, IMR was added to the regression to correct for the self-selection bias. We note that the first stage must contain at least one variable Z that is not present in the second stage—namely, the exclusion restriction variable. In this case, we used the number of followees who adopted SNI and the proportion of followees who adopted SNI as the exclusion restriction variables and reestimated Model 2 following the twostep procedure. The results of the second-stage regression are provided in the third column of Table 8. The coefficient of IMR (lambda) is significant, indicating the presence of a self-selection bias. Most importantly, the coefficient of SNI remains significantly positive, reaffirming the robustness of our results.

## 5.3 Discussion of Mechanisms

## 5.3.1 Observational Data Analysis

As previously discussed in Section 3.1, two possible underlying mechanisms could explain the positive effect of reviewers’ adoption of SNI on the perceived helpfulness of their online reviews: the increased time and effort invested during the review generation process and the enhanced credibility of the review source. In this section, we begin by investigating which of these two mechanisms is more likely to be responsible for improving the perceived helpfulness of online reviews.

To examine the first mechanism, we constructed two variables to measure the effort invested by reviewers in review generation. These variables include the length of each review in logarithmic form (Length) and the number of pictures included in each review (PictureNum). Longer reviews and those with more pictures typically require greater effort from reviewers and are commonly utilized in the literature as indicators of reviewers’ effort in writing reviews (Liu et al., 2019; Rohde et al., 2022). We then employed a regressionbased procedure of the parallel multimediator model (Hayes, 2017) to estimate the mediating effects of these two variables. This estimation procedure involved two steps. The first step included two equations, namely Equation (4) and Equation (5) that specified the influence of SNI on the two mediators, respectively. The second step included one equation, Equation (6), which outlined the influence of SNI and mediators on online review helpfulness.

$$
\begin{array}{c} L e n g t h = \alpha_ {1 0} + \alpha_ {1 1} S N I _ {-} o r _ {-} n o t + \theta C o n t r o l s \\ + \varepsilon \end{array}\tag{4}
$$

$$
P i c t u r e N u m = \alpha_ {2 0} + \alpha_ {2 1} S N I _ {-} o r _ {-} n o t
$$

$$
+ \theta C o n t r o l s + \varepsilon\tag{5}
$$

$$
\begin{array}{r} H e l p f u l V o t e s = \alpha_ {3 0} + \alpha_ {3 1} S N I _ {-} o r _ {-} n o t \\ + \alpha_ {3 2} L e n g t h \\ + \alpha_ {3 3} P i c t u r e N u m \\ + \theta C o n t r o l s + \varepsilon \end{array}\tag{6}
$$

Table 9 shows the regression results of Equations (4) to (6). The estimated coefficients $\hat { \alpha } _ { 1 1 }$ and $\hat { \alpha } _ { 2 1 }$ are both significantly positive, indicating a positive effect of SNI on review length and the number of review pictures, respectively. Estimated coefficients $\hat { \alpha } _ { 3 2 }$ and $\hat { \alpha } _ { 3 3 }$ in Equation (6) are also significant and positive, indicating that both review length and the number of review pictures had a positive effect on review helpfulness, which is consistent with previous research (Mudambi & Schuff, 2010; Wu et al., 2020). The mediation effects of review length and review pictures can then be estimated by $\hat { \alpha } _ { 1 1 } \times \hat { \alpha } _ { 3 2 }$ and $\hat { \alpha } _ { 2 1 } \times \hat { \alpha } _ { 3 3 }$ respectively. We conducted a bootstrap analysis (5000 samples) to obtain the standard errors and confidence intervals of the two estimators. The analysis revealed that the mediation effect of review length equals 0.0008 (95% confidence interval is [0.0006, 0.0010]), and the mediation effect of review pictures is 0.0093 (95% confidence interval is [0.0082, 0.0104]). Consequently, both mediation effects differ significantly from zero, indicating that the first mechanism is in effect. This reinforces our earlier argument that SNI improves perceived online review helpfulness by increasing the effort invested by reviewers during the review generation process.

Table 9. Estimation of the Mediation Effects

<table><tr><td></td><td>Equation (4)DV: Length</td><td>Equation (5)DV: PictureNum</td><td>Equation (6)DV: HelpfulVotes</td></tr><tr><td>SNI_or_not</td><td>0.062***(0.011)</td><td>0.132***(0.010)</td><td>0.002(0.003)</td></tr><tr><td>Length</td><td>-</td><td>-</td><td>0.013***(0.000)</td></tr><tr><td>PictureNum</td><td>-</td><td>-</td><td>0.071***(0.002)</td></tr><tr><td>Control variables</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.2046</td><td>0.0491</td><td>0.1144</td></tr><tr><td>Observations</td><td>426,927</td><td>426,927</td><td>426,927</td></tr><tr><td colspan="4">Note: *p&lt;0.1; **p&lt;0.05; ***p&lt;0.01, cluster-robust standard errors are in parentheses</td></tr></table>

Table 10. Examining the Moderating Role of Rating Deviation

<table><tr><td></td><td>DV: HelpfulVotes</td></tr><tr><td>SNI_or_not</td><td>0.076(0.049)</td></tr><tr><td>IfLargeGap</td><td>-0.298***(0.020)</td></tr><tr><td>SNI_or_not × IfLargeGap</td><td>0.064(0.062)</td></tr><tr><td>Control variables</td><td>Yes</td></tr><tr><td>Constant</td><td>Yes</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.0972</td></tr><tr><td>Observations</td><td>426,927</td></tr><tr><td colspan="2">Note: * p &lt; 0.1; ** p &lt; 0.05; *** p &lt; 0.01, cluster-robust standard errors are in parentheses</td></tr></table>

To examine the second mechanism, we investigated whether SNI could improve consumers’ perceived review helpfulness by enhancing the review source credibility. First, if this mechanism is valid, SNI should have a more pronounced impact on reviews facing greater credibility challenges. Consequently, we examined the moderating role of rating deviation in the relationship between reviewers’ choice of SNI and online review helpfulness. Reviewers who give review ratings that deviate from the average rating are more likely to have their trustworthiness questioned (Filieri, 2016; Lee et al., 2021). It is therefore reasonable to hypothesize that the effect of SNI is more pronounced for reviews exhibiting larger rating deviations, as the presence of SNI may alleviate consumers’ concerns about the credibility of such reviews.

However, the results shown in Table 10 reveal that even though a larger rating deviation (measured by the dummy variable IfLargeGap) negatively influenced review helpfulness, the coefficient of the moderation term is not significant. Second, after controlling for review length and the number of review pictures, the mediation analysis results in Table 9 show that the influence of SNI on review helpfulness is no longer significant. This suggests that SNI primarily affects perceived online review helpfulness through changes in review content. In summary, neither set of results provides support for the mechanism of enhanced review source credibility. We identified two plausible explanations for this lack of support: First, the symbol indicating the reviewer’s SNI adoption status was not displayed next to the online review on the review page. Instead, it could only be seen on the reviewer’s profile page. This limited visibility and accessibility could have contributed to the insignificance of this mechanism. Second, the adoption rate of SNI among reviewers in our research context was relatively low (7.5%), suggesting that many users may not have fully understand what SNI was and therefore may have disregarded the signal it conveyed.

## 5.3.2 Evidence from an Online Experiment

The above analysis, based on observational data, shows that the positive impact of SNI on online review helpfulness is primarily attributed to enhanced reviewer effort during the review generation process, rather than the increased review source credibility due to displaying the SNI-adoption symbol. In this section, we present the results of an online experiment designed to provide further insights into the underlying mechanism behind this enhanced reviewer effort. In addition, we investigate whether there is a negative mechanism at play, stemming from the inhibition effect of reduced anonymity. This experiment was conducted on Prolific, a popular crowdsourcing platform that facilitates a multitude of experimental studies across diverse research fields (e.g., Palan & Schitter, 2018; Peer et al., 2017).

We recruited 120 individuals (46 female) from the Prolific platform and compensated each participant with £1 (equivalent to approximately \$1.26). The objective of this experiment was to examine whether users’ review generation behavior would vary with or without SNI adoption. Participants were randomly assigned to either the SNI group (the treatment group) or the anonymity group (the control group). Before proceeding with the manipulation and review contribution process, we provided participants with the option to exit the survey if they were uncomfortable providing their social media alias nickname. Following this, we introduced ourselves as a hotel review platform seeking reviews from users worldwide. Participants in both groups were tasked with writing an online review based on a recent hotel stay.

After reading the provided instructions, participants were asked to provide the name and address of a hotel at which they recently stayed and to rate their overall satisfaction with this hotel on a scale from 1 to 5 stars. Subsequently, participants assigned to the SNI group were asked to provide the alias nickname associated with one of their social media accounts (such as Twitter, Instagram, Facebook, etc.). <sup>1</sup> They were informed that we would display their social media alias nickname along with the corresponding social media platform’s icon next to the online review they contributed. In contrast, participants assigned to the anonymity group were instructed to provide a random nickname, with an explanation that their chosen nicknames would also be displayed alongside their hotel reviews on our website. Following this, participants from both groups were tasked with writing a review of the hotel. Upon completing the review, we clarified the experiment’s objectives and asked participants to respond to a series of follow-up questions based on their authentic experiences. Adapted from previous research (Wang et al., 2017), these followup questions were designed to measure the authenticity of participants’ self-disclosure genuineness during the review-generating process. The questionnaire included three items: “I may lie about my accommodation experience,” “My review is a completely accurate reflection of what I really thought of the hotel,” and “I feel completely sincere when I reveal my accommodation experience and feelings.” Participants were asked to rate their responses on a scale from 1 (strongly disagree) to 7 (strongly agree) to convey their genuine thoughts.

Finally, we analyzed whether there were differences in the review generation effort and self-disclosure genuineness between the two groups of participants. Those participants who failed to provide sufficient information for us to identify the hotel and those in the treatment group who did not provide complete information about their associated social media accounts were excluded, leaving us with 107 participants (55 in the treatment group). To assess the effort invested by participants during the review generation process, we calculated the word count and character count for each review. Subsequently, we applied a natural logarithmic transformation to these two variables to address their left skewness and enhance result interpretation. Participants’ self-disclosure genuineness during the review generation was calculated by averaging their ratings of the three items (with the first item being reverse-coded). The results of t-test revealed that the mean value of the logarithmic character count (LogLen) in the treatment group was significantly higher than that in the control group $( M _ { S N I } =$ 5.488 vs. $M _ { A n o n y m i t y } = 5 . 2 7 3 ; t = - 2 . 0 5 3 , p < 0 . 0 5 )$ Similarly, for the logarithmic word count (LogWords), the mean value in the treatment group was also significantly higher than that in the control group $( M _ { S N I } = 3 . 7 3 0$ vs. $M _ { A n o n y m i t y } = 3 . 5 2 1 ; t = - 1 . 9 4 1 , p < 0 . 1 0 )$ . However, there was no significant difference in the mean values of participants’ self-rating of disclosure genuineness (Genuineness) between the two groups $( M _ { S N I } = 6 . 1 7 0$ vs. $M _ { A n o n y m i t y } = 6 . 0 0 6 ; t = - 0 . 9 9 3 , p > 0 . 1 0 ) .$

We also conducted multivariate linear regression analyses, where we regressed the outcome variables on whether the participant belonged to the treatment group (SNI\_or\_not) while controlling for a series of other variables. Specifically, we included the participant’s age (Age), gender (IfMale), whether the participant speaks English as their native language (IfNative), the participant’s satisfaction rating of the hotel (Rating), and the hotel’s star rating (Star) as control variables to account for potential confounders. The results of the regression analysis are presented in Table 11 and are consistent with our t-test analysis. In particular, the coefficients of SNI\_or\_not in Columns 1 and 2 indicate that, in comparison to participants in the control group, reviews contributed by participants in the treatment group contained, on average, 22.4% more characters $( \beta = 0 . 2 2 4 , p < 0 . 0 5 )$ and 22.3% more words $( \beta = 0 . 2 2 3 , p < 0 . 0 5 )$ . Nevertheless, the coefficient of SNI\_or\_not in Column 3 is not significant $( \beta = 0 . 1 4 7 , p > 0 . 1 )$ , thus providing no evidence of SNI’s influence on the genuineness of opinions in online review generation. These results once again support the underlying mechanism of SNI enhancing reviewers’ efforts in review generation. However, the countervailing mechanism of reduced anonymity and opinion genuineness in review generation is not supported.

Table 11. Multiple Regression Results

<table><tr><td></td><td>(1) LogLen</td><td>(2) LogWords</td><td>(3) Genuineness</td></tr><tr><td>SNI_or_not</td><td>0.224**(0.109)</td><td>0.223**(0.112)</td><td>0.147(0.166)</td></tr><tr><td>Age</td><td>-0.004(0.005)</td><td>0.004(0.005)</td><td>0.001(0.007)</td></tr><tr><td>IfMale</td><td>0.011(0.108)</td><td>-0.029(0.112)</td><td>-0.340**(0.166)</td></tr><tr><td>IfNative</td><td>-0.014(0.117)</td><td>0.011(0.120)</td><td>0.340*(0.178)</td></tr><tr><td>Rating</td><td>-0.033(0.065)</td><td>-0.037(0.067)</td><td>0.107(0.098)</td></tr><tr><td>Star</td><td>0.099*(0.059)</td><td>0.105*(0.061)</td><td>-0.069(0.090)</td></tr><tr><td>Constant</td><td>4.927***(0.359)</td><td>3.195***(0.370)</td><td>5.844***(0.548)</td></tr><tr><td> $R^2$ </td><td>0.077</td><td>0.075</td><td>0.104</td></tr><tr><td>Observations</td><td>107</td><td>107</td><td>107</td></tr><tr><td colspan="4">Note: *p&lt;0.1; **p&lt;0.05; ***p&lt;0.01</td></tr></table>

## 6 Discussion

## 6.1 Theoretical Implications

The findings of this study offer several noteworthy theoretical implications. First, our research extends the existing literature on online review helpfulness by examining the contributing role of SNI, a social networking feature that has been widely adopted by online review platforms. Previous research has primarily focused on examining SNI’s effects on the quantity and linguistic styles of reviewers’ subsequent reviews (Huang et al., 2017), leaving the question of whether and how SNI influences review readers’ perceived review helpfulness largely unexplored. Based on the framework of the information adoption model (Sussman & Siegal, 2003), our study proposes that reviewers’ choice of SNI may enhance online review helpfulness through two possible mechanisms: enhancing review quality and improving review source credibility. Our initial findings confirm a positive impact of SNI on online review helpfulness. Moreover, our analysis of the underlying mechanisms reveals that SNI primarily affects perceived review helpfulness by increasing the effort invested by reviewers during the review creation process, which is consistent with prior research (Huang et al., 2017; Pu et al., 2020). In addition, our study shows that reviewer-related factors, including reviewer level, peer recognition, and follower ties, significantly moderate this relationship by influencing the amount and efficacy of the enhanced effort invested by reviewers.

Second, this study contributes to the literature by enhancing our comprehension of how SNI influences UGC production. Previous research has indicated that choosing SNI leads to more civilized and deliberative comments on news websites (Cho & Kwon, 2015; Suh et al., 2018). In addition, the implementation of SNI by online review platforms has been shown to significantly increase the use of affective language while decreasing cognitive and negative expressions in subsequent review texts (Huang et al., 2017). Nevertheless, prior research has not directly investigated how readers perceive content generated by users who choose to adopt SNI. Leveraging the unique feature of review helpfulness voting systems on online review platforms, this study empirically demonstrates that reviews authored by SNI-adopting reviewers are deemed to be more helpful by readers. Although earlier research has implied that SNI may influence perceived review quality through differences in the linguistic style of the review text, this study offers an alternative perspective by analyzing the mechanism through which SNI impacts review helpfulness; namely, we focus specifically on the amount of effort expended by reviewers—a crucial factor for review readers in assessing the helpfulness of online reviews (Yin et al., 2014). Through a series of mechanism tests, we show that the positive effects of SNI on online review helpfulness mainly work through enhancing the amount of effort reviewers devote to review generation (reflected by review length and the number of pictures included in the review). This finding is in line with prior research, which suggests that reducing content creators anonymity positively affects the effort invested in subsequent content generation (Fredheim et al., 2015; Pu et al., 2020).

## 6.2 Practical Implications

Our findings also have important practical implications. First, our results suggest that enabling SNI on online review platforms can enhance the perceived usefulness of online reviews by motivating reviewers to invest more effort in their review generation. To maximize the signaling effects of SNI in helping consumers identify helpful reviews, review platforms should consider making the symbol indicating reviewers’ SNI-adoption status more apparent to users. However, online review platforms should also exercise caution in promoting SNI, as its influence on online review helpfulness varies across different reviewers. For instance, adopting SNI may be very beneficial for reviewers with higher platform expertise and more follower ties. In contrast, SNI may not have much of an impact on reviewers who have already received significant peer recognition.

Second, although for the majority of reviewers, adopting SNI can be an effective strategy to motivate them to invest more effort into creating reviews and enhance the perceived helpfulness of their subsequent contributions, reviewers who intend to adopt SNI should also keep in mind that the positive effect of SNI can vary depending on their content creation ability and their desire to enhance the online image. Specifically, adopting SNI is more beneficial for reviewers who possess higher expertise and more follower ties on the platform because of their higher capability and motivation concerning review contributions. However, for reviewers who have gained substantial peer recognition, it is important that they remain open-minded and creative to avoid complacency and the production of less valuable content, which could undermine the positive effects of SNI on perceived review helpfulness.

## 6.3 Limitations and Future Directions

Our study acknowledges several limitations that offer avenues for further research. First, our dataset was collected from a premier online review platform in China and confined to the city of Beijing. Recognizing the influence of cultural norms and practices on online consumer behavior, future research could enhance the robustness of our conclusions by testing our hypotheses on diverse review platforms and in various cities worldwide. Additionally, our analysis was limited by the lack of time-stamped data for helpful votes on reviews, which restricted our ability to construct panel data. Future studies could address this gap by employing alternative research methodologies, such as conducting field experiments on review platforms, which could enable the collection of panel data to allow for a more nuanced understanding of the factors influencing the perceived helpfulness of online reviews.

## 7 Conclusion

As social networking features continue to gain prominence across a wide range of online websites, social network integration (SNI) has emerged as a popular feature on online review platforms. However, the relationship between SNI and online review helpfulness has not been empirically tested. In this study, we leveraged a dataset collected from a leading Chinese online review platform to investigate not only the effects of SNI on review helpfulness but also how these effects are moderated by different reviewerrelated factors.

Our findings show that when reviewers choose SNI, their reviews are perceived to be more helpful. Moreover, the positive influence of SNI can be strengthened by higher levels of expertise among reviewers and the establishment of more follower ties; it can be weakened by the amount of peer recognition previously received by the reviewer. Our analyses of the underlying mechanisms reveal that SNI primarily enhances review helpfulness by motivating reviewers to invest greater effort in generating review content. This research offers a fresh perspective on understanding how the proliferation of social media features on review websites influences the perceived helpfulness of reviews. The practical implications of our results extend to stakeholders such as review websites, businesses, and reviewers themselves, providing valuable insights for enhancing the quality and impact of online reviews.

## Acknowledgments

We thank the editors and referees for their constructive suggestions and comments throughout the revision process. This work was supported by the National Natural Science Foundation of China (71972004).

## References

Baek, H., Ahn, J. H., & Choi, Y. (2012). Helpfulness of online consumer reviews: Readers’ objectives and review cues. International Journal of Electronic Commerce, 17(2), 99- 126.

Bilal, M., Marjani, M., Hashem, I. A., Malik, N., Lali, M. I., & Gani, A. (2021). Profiling reviewers’ social network strength and predicting the “helpfulness” of online customer reviews. Electronic Commerce Research and Applications, 45, Article 101026.

Bristor, J. (1990). Exhanced explanations of word of mouth communications; the power of relations. Research in Consumer Behavior, 4, 51-83.

Burtch, G., He, Q., Hong, Y., & Lee, D. (2022). How do peer awards motivate creative content? Experimental evidence from Reddit. Management Science, 68(5), 3488-3506.

Chen, H., Duan, W., & Zhou, W. (2021). When products receive reviews across platforms: Studying the platform concentration of electronic word-of-mouth. Information & Management, 58, Article 103532.

Chen, W., Wei, X., & Zhu, K. (2017). Engaging voluntary contributions in online communities: A hidden Markov model. MIS Quarterly, 42(1), 83-100.

Cheng, X., Gu, Y., Hua Y., & Luo, X. (2021). The paradox of word-of-mouth in social commerce: Exploring the juxtaposed impacts of source credibility and information quality on SWOM spreading. Information & Management, 58, Article 103505.

Cheng, Y. H., & Ho, H. Y. (2015). Social influence’s impact on reader perceptions of online reviews. Journal of Business Research, 68(4), 883-887.

Chesney, T., & Su, D. K. (2010). The impact of anonymity on weblog credibility. International Journal of Human-Computer Studies, 68(10), 710-718.

Chintagunta, P. K., Gopinath, S., & Venkataraman, S. (2010). The effects of online user reviews on movie box office performance: Accounting for sequential rollout and aggregation across local markets. Marketing Science, 29(5), 944- 957.

Cho, D., & Kwon, K. H. (2015). The impacts of identity verification and disclosure of social

cues on flaming in online user comments. Computers in Human Behavior, 51, 363-372.

Cho, D., Kim, S., & Acquisti, A. (2012). Empirical analysis of online anonymity and user behaviors: the impact of real name policy. Proceedings of the 45th Hawaii International Conference on System Sciences (pp. 3041- 3050).

Chua, A. Y. K., & Banerjee, S. (2014). Understanding review helpfulness as a function of reviewer reputation, review rating, and review depth. Journal of the Association for Information Science and Technology, 66(2), 354-362.

Clougherty, J. A., Duso, T., & Muck, J. (2015). Correcting for self-selection based endogeneity in management research: Review, recommendations and simulations. Organizational Research Methods, 19(2), 286-347.

Dehejia, R. H., & Wahba, S. (1999). Causal effects in nonexperimental studies: Reevaluating the evaluation of training programs. Journal of the American Statistical Association, 94(448), 1053-1062.

Dyussembayeva, S., Viglia, G., Nieto-Garcia, M., & Invernizzi, A. C. (2020). It makes me feel vulnerable! The impact of public selfdisclosure on online complaint behavior. International Journal of Hospitality Management, 88, Article 102512.

Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. Psychological Review, 100(3), 363-346.

Filieri, R. (2016). What makes an online consumer review trustworthy? Annals of Tourism Research, 58, 46-64.

Filieri, R., Galati, F., & Raguseo, E. (2020). The impact of service attributes and category on eWOM helpfulness: An investigation of extremely negative and positive ratings using latent semantic analytics and regression analysis. Computers in Human Behavior, 114, Article 106527.

Filieri, R., Hofacker, C. F., & Alguezaui, S. (2018). What makes information in online consumer reviews diagnostic over time? The role of review relevancy, factuality, currency, source credibility and ranking score. Computers in Human Behavior, 80, 122-131.

Forman, C., Ghose, A., & Wiesenfeld, B. (2008). Examining the relationship between reviews and sales: The role of reviewer identity

disclosure in electronic markets. Information Systems Research, 19(3), 291-313.

Fredheim, R., Moore, A., & Naughton, J. (2015). Anonymity and online commenting: The broken windows effect and the end of driveby commenting. Proceedings of the ACM Web Science Conference.

Goes, P. B., Lin, M., & Au Yeung, C. M. (2014). “Popularity effect” in user-generated content: Evidence from online product reviews. Information Systems Research, 25(2), 222- 238.

Guan, T., Wang, L., Jin, J., & Song, X. (2018). Knowledge contribution behavior in online Q&A communities: An empirical investigation. Computers in Human Behavior, 81, 137-147.

Hansen, L. P. (1982). Large sample properties of generalized method of moments estimators. Econometrica: Journal of the Econometric Society, 50(4), 1029-1054.

Hayes, A. F. (2017). Introduction to mediation, moderation, and conditional process analysis: A regression-based approach. Guilford.

He, S., Hollenbeck, B., & Proserpio, D. (2022). The market for fake reviews. Marketing Science, 41(5), 896-921.

Heckman, J. J. (1979). Sample selection bias as a specification error. Econometrica, 47(1), 153.

Hlee, S. (2020). How reviewer level affects review helpfulness and reviewing behavior across hotel classifications: The case of Seoul in Korea. Industrial Management & Data Systems, 121(6), 1191-1215.

Hong, Y., Huang, N., Burtch, G., & Li, C. (2016). Culture, conformity, and emotional suppression in online reviews. Journal of the Association for Information Systems, 17(11), 737-758.

Huang, L., Tan, C. H., Ke, W., & Wei, K. K. (2018). Helpfulness of online review content: The moderating effects of temporal and social cues. Journal of the Association for Information Systems, 19(6), 503-522.

Huang, N., Burtch, G., Gu, B., Hong, Y., Liang, C., Wang, K., Fu, D., & Yang, B. (2019). Motivating user-generated content with performance feedback: Evidence from randomized field experiments. Management Science, 65(1), 327-345.

Huang, N., Hong, Y., & Burtch, G. (2017). Social network integration and user content generation: Evidence from natural experiments. MIS Quarterly, 41(4), 1035- 1058.

Jabr, W., Mookerjee, R., Tan, Y., & Mookerjee, V. S. (2014). Leveraging philanthropic behavior for customer support: The case of user support forums. MIS Quarterly, 38(1), 187- 208.

Karimi, S., & Wang, F. (2017). Online review helpfulness: Impact of reviewer profile image. Decision Support Systems, 96, 39-48.

Ke, Z., Liu, D., & Brass, D. J. (2020). Do online friends bring out the best in us? The effect of friend contributions on online review provision. Information Systems Research, 31(4), 1322- 1336.

Kontaxis, G., Polychronakis, M., & Markatos, E. P. (2012). Minimizing information disclosure to third parties in social login platforms. International Journal of Information Security, 11, 321-332.

Kuan, K., Hui, K.-L., Prasarnphanich, P., & Lai, H.-Y. (2015). What makes a review voted? An empirical investigation of review voting in online review systems. Journal of the Association for Information Systems, 16(1), 48-71.

Kusumasondjaja, S., Shanka, T., & Marchegiani, C. (2012). Credibility of online reviews and initial trust. Journal of Vacation Marketing, 18(3), 185-195.

Kwok, L., & Xie, K. L. (2016). Factors contributing to the helpfulness of online hotel reviews. International Journal of Contemporary Hospitality Management, 28(10), 2156-2177.

Lee, K. T., & Koo, D. M. (2012). Effects of attribute and valence of e-WOM on message adoption: Moderating roles of subjective knowledge and regulatory focus. Computers in Human Behavior, 28(5), 1974-1984.

Lee, S., Lee, S., & Baek, H. (2021). Does the dispersion of online review ratings affect review helpfulness? Computers in Human Behavior, 117, Article 106670.

Lee, Y.-J., Hosanagar, K., & Tan, Y. (2015). Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Science, 61(9), 2241-2258.

Liu, X., Zhang, Z., Law, R., & Zhang, Z. (2019). Posting reviews on OTAs: Motives, rewards

and effort. Tourism Management, 70, 230- 237.

Liu, Z., & Park, S. (2015). What makes a useful online review? Implication for travel product websites. Tourism Management, 47, 140-151.

Luca, M., & Zervas, G. (2016). Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Science, 62(12), 3412- 3427.

Malik, M. S. I., & Hussain, A. (2018). An analysis of review content and reviewer variables that contribute to review helpfulness. Information Processing & Management, 54(1), 88-104.

Mayzlin, D., Dover, Y., & Chevalier, J. (2014). Promotional reviews: An empirical investigation of online review manipulation. American Economic Review, 104(8), 2421- 2455.

Meo, P. D., Musial-Gabrys, K., Rosaci, D., Sarnè, G. M., & Aroyo, L. (2017). Using centrality measures to predict helpfulness-based reputation in trust networks. ACM Transactions on Internet Technology, 17(1), 1-20.

Moro, S., & Esmerado, J. (2020). An integrated model to explain online review helpfulness in hospitality. Journal of Hospitality and Tourism Technology, 12(2), 239-253.

Mudambi, S. M., & Schuff,.D. (2010). Research note: What makes a helpful online review? A study of customer reviews on Amazon.com. MIS Quarterly, 34(1), 185-200.

Omernick, E., & Sood, S. O. (2013). The impact of anonymity in online communities. Proceedings of the International Conference on Social Computing (pp. 526-535).

Ou, Y., & Chua, A. (2021). An investigation of factors that contribute to movie review helpfulness in China. Proceedings of the International MultiConference of Engineers and Computer Scientists.

Palan, S., & Schitter, C. (2018). Prolific.ac—A subject pool for online experiments. Journal of Behavioral and Experimental Finance, 17, 22-27.

Peer, E., Brandimarte, L., Samat, S., & Acquisti, A. (2017). Beyond the Turk: Alternative platforms for crowdsourcing behavioral research. Journal of Experimental Social Psychology, 70, 153-163.

Pu, J., Chen, Y., Qiu, L., & Cheng, H. K. (2020). Does identity disclosure help or hurt user content

generation? Social presence, inhibition, and displacement effects. Information Systems Research, 31(2), 297-322.

Qiu, L., & Kumar, S. (2017). Understanding voluntary knowledge provision and content contribution through a social-media-based prediction market: A field experiment. Information Systems Research, 28(3), 529- 546.

Racherla, P., & Friske, W. (2012). Perceived ‘usefulness’ of online consumer reviews: An exploratory investigation across three services categories. Electronic Commerce Research and Applications, 11(6), 548-559.

Ren, J., Yeoh, W., Shan Ee, M., & Popovič, A. (2017). Online consumer reviews and sales: Examining the chicken-egg relationships. Journal of the Association for Information Science and Technology, 69(3), 449-460.

Rishika, R., & Ramaprasad, J. (2019). The effects of asymmetric social ties, structural embeddedness, and tie strength on online content contribution behavior. Management Science, 65(7), 3398-3422.

Rohde, C., Kupfer, A., & Zimmermann, S. (2022). Explaining reviewing effort: Existing reviews as potential driver. Electronic Markets, 1-17.

Suh, K. S., Lee, S., Suh, E. K., Lee, H., & Lee, J. (2018). Online comment moderation policies for deliberative discussion-seed comments and identifiability. Journal of the Association for Information Systems, 19(3), 182-208.

Suler, J. (2004). The online disinhibition effect. Cyberpsychology & Behavior, 7(3), 321-326.

Sussman, S. W., & Siegal, W. S. (2003). Informational influence in organizations: An integrated approach to knowledge adoption. Information Systems Research, 14(1), 47-65.

Ver Hoef, J. M., & Boveng, P. L. (2007). Quasi-Poisson vs. negative binomial regression: How should we model overdispersed count data? Ecology, 88(11), 2766-2772.

Wan, Y. (2015). The Matthew effect in social commerce. Electronic Markets, 25(4), 313- 324.

Wang, C., Zhang, X., & Hann, I.-H. (2018). Socially nudged: A quasi-experimental study of friends’ social influence in online product ratings. Information Systems Research, 29(3), 641-655.

Wang, L., Yan, J., Lin, J., & Cui, W. (2017). Let the users tell the truth: Self-disclosure intention

and self-disclosure honesty in mobile social networking. International Journal of Information Management, 37(1), 1428-1440.

Wang, S., & Wang, F. (2020). Network prominence and e-store performance in social marketplace: A nuanced typology and empirical evidence. Electronic Commerce Research and Applications, 43, Article 100991.

Wang, Y., Wang, J., Yao, T., & Li, M. (2020). What makes peer review helpfulness evaluation in online review communities? An empirical research based on persuasion effect. Online Information Review, 44(6), 1267-1286.

Wei, Z., Xiao, M., & Rong, R. (2021). Network size and content generation on social media platforms. Production and Operations Management, 30(5), 1406-1426.

Wu, R., Wu, H. H., & Wang, C. L. (2020). Why is a picture “worth a thousand words”? Pictures as information in perceived helpfulness of online reviews. International Journal of Consumer Studies, 45(3), 364-378.

Yin, D., Bond, S. D., & Zhang, H. (2014). Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quarterly, 38(2), 539-560.

Yin, D., Mitra, S., & Zhang, H. (2016). Research note—When do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth. Information Systems Research, 27(1), 131- 144.

Zhang, X., & Zhu, F. (2011). Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. American Economic Review, 101(4), 1601-1615.

Zhang, X., Zhang, X., Liang, S., Yang, Y., & Law, R. (2023). Infusing new insights: How do review novelty and inconsistency shape the usefulness of online travel reviews? Tourism Management, 96, Article 104703.

Zhou, W., & Duan, W. (2016). Do professional reviews affect online user choices through user reviews? An empirical study. Journal of Management Information Systems, 33(1), 202-228.

Zhu, L., Yin, G., & He, W. (2014). Is this opinion leader’s review useful? Peripheral cues for online review helpfulness. Journal of Electronic Commerce Research, 15(4), 267- 280.

## About the Authors

Zheyuan Pu is a PhD candidate in the Department of Information Management at Peking University. His current research focus is user-generated content and AI-generated content in virtual communities. He has published works in the proceedings of the Pacific Asia Conference on Information Systems, the Americas Conference on Information Systems, etc.

Shengli Li is an associate professor in the Department of Information Management at Peking University. He received his PhD in information systems from the University of Florida in 2013. Dr. Li’s research interests focus on information systems, electronic commerce, and social media. His research has been published in several journals, including MIS Quarterly, Production and Operations Management, Journal of Management Information Systems, Information & Management, and Decision Support Systems.

Jiaxuan Wu received her master’s degree in management from the Department of Information Management at Peking University. Her main research interests include social media and electronic commerce.

Yipeng Liu serves as the Dean’s Outstanding Associate Professor within the Department of Operations Management and Information Systems (OM&IS) at Northern Illinois University. He earned his PhD in information systems from the University of Florida in 2009. Dr. Liu’s research primarily focuses on the economic modeling of information systems. He employs both analytical modeling and empirical methods to explore the economic and social complexities present in business and organizational contexts. His work has been published in leading information systems journals, such as MIS Quarterly, Information Systems Research, Production and Operations Management, Journal of the Association for Information Systems, and Journal of Management Information Systems. (ORCiD: https://orcid.org/0000-0001-7645-4883)
