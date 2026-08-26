---
otero_id: 26537
otero_key: "YC8QJGMC"
title: "Extrinsic versus Intrinsic Rewards for Contributing Reviews in an Online Platform"
authors: "Warut Khern-am-nuai; Karthik Kannan; Hossein Ghasemkhani"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0750"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/YC8QJGMC/fulltext/images/74faf716b9e1316d9ddc6050c9b8ea784329c7e4bd1bed1af6daf19413eaa36b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Extrinsic versus Intrinsic Rewards for Contributing Reviews in an Online Platform

Warut Khern-am-nuai, Karthik Kannan, Hossein Ghasemkhan

To cite this article: Warut Khern-am-nuai, Karthik Kannan, Hossein Ghasemkhani (2018) Extrinsic versus Intrinsic Rewards for Contributing Reviews in an Online Platform. Information Systems Research

Published online in Articles in Advance 05 Nov 2018

https://doi.org/10.1287/isre.2017.0750

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Extrinsic versus Intrinsic Rewards for Contributing Reviews in an Online Platform

Warut Khern-am-nuai,<sup>a</sup> Karthik Kannan,<sup>b</sup> Hossein Ghasemkhani<sup>b</sup>

<sup>a</sup> Desautels Faculty of Management, McGill University, Montréal, Québec H3A 1G5, Canada; <sup>b</sup> Krannert School of Management, Purdue University, West Lafayette, Indiana 47907

Contact: warut.khern-am-nuai@mcgill.ca, http://orcid.org/0000-0002-9861-0717 (WK-a-n); kkarthik@purdue.edu (KK); hossein@purdue.edu (HG)

Received: July 22, 2015 Revised: August 12, 2016; May 16, 2017 Accepted: August 21, 2017 Published Online in Articles in Advance: November 5, 2018

https://doi.org/10.1287/isre.2017.075

Copyright: © 2018 INFORMS

Abstract. Firms have considered various forms of incentives for writing reviews, including the use of extrinsic rewards to attract reviewers. Building on this literature, we study the implications of monetary incentives on online reviews in the context of a natural experiment, where one review platform suddenly began ofering monetary incentives for writing reviews. We refer to this as the treated platform. Along with data from Amazon.com and using the diference-in-diferences approach, we compare the quantity and quality of reviews before and after rewards were introduced in the treated platform. We find that reviews are significantly more positive but that the quality decreases. Taking advantage of the panel data, we also evaluate the efect of rewards on existing reviewers. We find that their level of participation after monetary incentives decreases but not their quality of participation. Last, even though the platform enjoys an increase in the number of new reviewers, disproportionately more reviews appear to be written for highly rated products.

History: Ritu Agarwal, Senior Editor; Param Singh, Associate Editor.

Funding: The authors gratefully acknowledge financial support from the National Science Foundation through [NSF CMMI grant 1400050].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0750.

Keywords: natural experiment • online reviews • monetary incentives • diference-in-diferences • electronic commerce

## 1. Introduction

The usefulness of an online review platform critically depends on the ability to accurately capture user experience. Yet, previous literature has shown that online reviews mainly capture extreme rather than moderate opinions (Chevalier and Mayzlin 2006, Liu 2006). One possible explanation is the under-reporting bias, where customers with moderate views on the product are less likely to provide reviews, while highly satisfied or highly dissatisfied customers write reviews to brag or moan (Hu et al. 2009). A natural way of overcoming the problem is to ofer rewards so as to attract reviewers who would otherwise not contribute. Historically, product manufacturers (or service providers) such as car rental agencies and hotels, and review platform owners such as Best Buy and TripAdvisor have ofered monetary incentives to attract reviewers. In this paper, we study the implications of monetary rewards ofered by review platform owners.

The question we seek to address in this paper is relevant as using monetary rewards to draw reviewers to review platforms has recently become a common practice. Yet little analysis has been done thus far on the implications of such rewards in the context of online reviews. Note that if a product manufacturer provides incentives to reviewers, it is intuitive to expect this to result in a positive bias in reviews (McQueeney 2016). In addition, Chen and Xie (2005) show that the manufacturer has an incentive to induce such behavior.<sup>1</sup> However, when the review platform ofers incentives, the outcome may not be as apparent. Specifically, it is not clear whether the incentives simply reduce the participation cost and thus allow the platform to capture the true perceptions of the population or whether they induce bias such as warm glow or indirect reciprocity that again will not lead to capturing true perceptions. In addition, writing reviews is an inherently intrinsically-motivated task. Prior research has shown that when behavior is primarily driven by intrinsic motivation, introducing extrinsic rewards could lead to weaker engagement (e.g., Kreps 1997, Deci et al. 1999).

The interactions between intrinsic and extrinsic motivations difer depending on the context and the incentive mechanism design. For example, prior information systems (IS) research has considered participation in discussion forums and knowledge management systems, and has identified conflicting results (e.g., Liu et al. 2014, Hsieh et al. 2010). One of the factors that decides the outcome in the discussion forum context is whether rewards are designed to be based on the quality of the answers. It is unclear if the insights from studies on discussion forums carry over to the review platform structure. In the review context, platforms use three diferent approaches on monetary incentives. The first is used by platforms such as Amazon, which generally does not provide explicit incentives to write reviews. The second approach is performancebased: For example, at some point, Epinions provided rewards based on the quality of the reviews written. Although this approach seems attractive, it is rarely implemented in practice due to the operational dificulties. The third approach is to provide rewards simply based on the number of reviews written. This recent incentive mechanism has become a common practice among review platforms such as Best Buy, Rakuten, and Kmart that ofer extrinsic rewards in exchange for reviews. In our study, we focus on this third type of mechanism, since our objective is to formally analyze how this widely adopted incentive structure changes the nature of the reviews and the level of participation and engagement of the intrinsically motivated reviewers.

In this paper, we take advantage of an exogenous change in a certain review platform, and use a natural experiment research design. On April 13, 2013, an online review platform, henceforth the treated platform, introduced a program to encourage reviewers by giving them monetary rewards for eligible reviews submitted. Based on our discussions with the platform, no other major changes that could afect reviewer behavior were introduced around that time. Moreover, the change only afected the treated platform and the reviews on it. Also, to our knowledge, the change was not announced in advance to the users: This gives us a clear point in time when the treatment was initiated. Dunning (2012, p. 3) defines a natural experiment as an observational setting where causes are randomly, or as good as randomly, assigned among some set of units. Consistent with that definition, this setting is a perfect candidate for a natural experiment research design. To study the efect of the treatment, we also need a valid control group that is not exposed to the treatment. We chose Amazon.com as the control platform, since it has one of the largest and most reputable review platforms, and it did not have a monetary incentive program before or after the treatment.

We match products in the treated platform with those in the control platform and use the diferencein-diferences (DID) approach to compare reviews in the two platforms before and after treatment. We find that after monetary incentives are introduced, reviews on the treated platform are significantly more positive while the quality drastically decreases. Our findings imply that monetary incentives are not simply reducing the costs of review writing; indirect reciprocity induced by the monetary rewards seems to be an important factor driving reviewer behavior. We followed up on the initial analysis by examining how existing reviewers in the treated platform, who may be considered intrinsically motivated, behave as a consequence of the rewards. We find that even though existing reviewers write reviews less often, they do not appear to reduce the depth and quality of their reviews, as there was no statistically significant difference in the review length and helpfulness before and after the incentives. From the platform’s standpoint, even though the platform enjoys an increase in the number of new reviewers who registered and contributed to the platform after monetary incentives, it sufers from review concentration bias, since reviews after the incentives are disproportionately written for highly rated products. Moreover, most of the low-rated products receive higher star ratings. As a result, the distribution of star ratings becomes more skewed to the positive extremity, implying that platform-level bias exacerbates with the introduction of monetary incentives.

In Section 2, we review the literature related to our study, and in Section 3 we develop our hypotheses. Section 4 discusses the data used for the empirical analysis. In Section 5, we introduce the empirical strategy used in our study and present a discussion of the results of our econometric analysis of product reviews and review platforms. In Section 6, we summarize the implications of our study and present the conclusions of our research and its limitations, along with potential directions for future research.

## 2. Literature Review

A wide array of studies on review systems is available not only in the IS domain but also in psychology, economics, computer science, and marketing. This domain also relates to prior works on traditional wordof-mouth efects (e.g., Bansal and Voyer 2000, Grewal et al. 2003). However, online reviews have been recognized as diferent in that they have a distinct set of features that traditional word-of-mouth lacks. First, online reviews are available for an indefinite period of time. Second, the platform owner can control which reviews to display. Third, online review systems typically allow readers to search and filter reviews they want to read. In the specific context of online reviews, we first seek to understand the importance and impact of diferent review elements and characteristics on review systems by surveying the literature that studies the impact of online review elements on consumer behavior.

## 2.1. Impact of Review Elements on Consumer Behavior

In this section, we discuss a few papers that are most relevant to our analysis. See Rosario et al. (2016) for a more comprehensive review of the previous literature.

Star ratings and number of reviews are two of the main review elements that we consider. Prior literature has shown that the two measures afect product sales and consumers’ buying intention. Using an experiment, Park and Kim (2009) showed that the number of reviews significantly impacts purchase intention, especially when consumers are unfamiliar with the product. Similarly, Chevalier and Mayzlin (2006) used online book reviews on Amazon and Barnes and Noble to show that the diferences in sales ranks of books between the two websites are due to the diferences in review volumes and prices. Luca (2011) used data from Yelp.com to demonstrate that the increase in star ratings can boost restaurant revenues. Moe and Trusov (2011) showed that previous ratings afect a reviewer’s judgment and, therefore, have an indirect impact on future product sales. Moreover, Chintagunta et al. (2010) leveraged online reviews and movie box ofice performance data to show that the average star rating also afects product sales.

Simply considering star ratings may not be suficient according to the prior literature. Pavlou and Dimoka (2006) found on eBay that extreme seller feedback has a significant efect on seller credibility. By contrast, Eisend (2006) argued that moderate reviews enhance product credibility and brand favorability by providing pros and cons of the product. Mudambi and Schuf (2010) reconciled these contradicting results by explaining that the efect of extreme reviews is moderated by the product type to which the reviews belong. They also showed that review length is another important element, and so we consider that review element as well. The review length was also found to be important in Pan and Zhang (2011).

Recent research has further investigated this issue by focusing on textual features of the reviews. Schlosser (2011) used content analysis and experiments to evaluate the efect of adding a pros and cons section on the helpfulness and persuasiveness of reviews. In addition, text mining has been shown to be a useful tool to enhance econometric analysis in studying the impact of reviews on sales (Ghose and Ipeirotis 2011). Furthermore, Archak et al. (2011) used text mining to include review text in their consumer choice model. They showed that textual data can be used to infer consumer preferences and to forecast sales. In light of these results, we also consider the textual content for our analysis. Next, we review the literature that focuses on understanding how and why people write reviews. This helps us further our understanding of the impact of monetary incentives on online reviews.

## 2.2. Review Generation Process

Here we discuss three substreams related to the study of the review generation process. The first relates to review characteristics and the bias in online review platforms. Marlin et al. (2007) conducted a user study in the context of online movie ratings and concluded that user preferences afect their choice of whether to rate. Additionally, Marlin and Zemel (2009) showed that the ratings generated in such circumstances violated the missing-at-random assumption. Similarly, Hu et al. (2006) conducted an experiment in the context of online reviews and proposed the brag-and-moan model, in which they argued that users with extreme preferences are more likely to write reviews. Li and Hitt (2008) has shown that this self-selection bias is helpful for retailers. They also observed that the valence of ratings has a downward trend and attributed this to the fact that earlier buyers may have significantly diferent preferences from later buyers. As later buyers read reviews from earlier buyers who do not share the same taste, the level of dissatisfac tion increases over time. Godes and Silva (2012) also focused on the downward trending valence but ofered a diferent explanation. They argued that the total number of reviews increases over time, so the later the buyers arrive, the more reviews they face, and the more their ability to thoroughly assess all reviews decreases. Therefore, later buyers are more likely to make an erroneous purchase, be dissatisfied, and end up writing negative reviews. Lee et al. (2015) studied the efect of social interactions on review generation and provided empirical evidence for imitation in sequentially generated online movie ratings. Gao et al. (2015) were among the first to study the relationship between online ratings and the opinion of the population, including ofline consumers. In the health care context, they found that lower quality physicians are less likely to be rated online and that although online ratings are correlated with population opinions, they are usually exaggerated.

The second substream of research examines fraud and review manipulation. Recent empirical studies have found evidence of fake reviews in several contexts such as restaurant reviews (Luca and Zervas 2016) and hotel reviews (Mayzlin et al. 2014). Lappas et al. (2016) showed that manipulating online hotel reviews has a significant efect on changing product visibility. Yoo and Gretzel (2009) found that there are diferences in the language structure between deceptive and truthful hotel reviews, but based on the structure alone, it is difficult to diferentiate between them. On the other hand, in the retail context, Anderson and Magruder (2012) posited that, even though retailers have incentives to fake reviews so as to increase their own ratings, there is no evidence suggesting they do so.

The third substream analyzes reviewer motivations. Dellarocas and Narayan (2006) showed the similarities of a population’s propensity to engage in ofline and online word-of-mouth. Hennig-Thurau et al. (2004)

surveyed participants on a German web-based customer opinion platform and found that the main factors motivating reviewers are the desire for social interaction and economic incentives, the concern for other consumers, and the opportunity to reach selfactualization. Goes et al. (2014) used data from epionions.com to empirically study how reviewers’ social network structure impacts reviewing behavior. They showed that popular reviewers tend to write more and their reviews tend to be more positive. On the other hand, Cheema and Kaikati (2010) argued that reviewers are less likely to write positive reviews because they are driven by incentives such as the need for uniqueness. Dellarocas et al. (2010) showed that users are more likely to post reviews for niche products. Meanwhile, Shen et al. (2015) demonstrated that reviewers behaved strategically to gain attention and that, as a result, the platform ends up with a diverse set of reviews. This competition was also observed in the context of user-generated content in the enterprise information technology (IT) (Huang et al. 2015). Given that intrinsic and extrinsic rewards can play an important role in the review generation process, we next examine prior works that study the impact of monetary incentives in related contexts.

## 2.3. The Impact of Monetary Incentives

For decades, the use of monetary incentives in general has been controversial. Kohn (1999) provides an excellent survey of prior studies that examined the impact of monetary incentives in areas such as psychology and economics. Studies in IS literature have also investigated the efect of monetary incentives in diferent contexts, and the empirical results are mixed. For example, in the crowdsourcing context, Liu et al. (2014) found that the quality of the tasks performed is higher when the incentives are higher in the Taskcn platform. However, Hsieh et al. (2010) and Chen et al. (2010b) used data from Google Answers to conclude otherwise. They found that financial incentives lead to higher volume and longer answers but that the incentives barely afect the quality of the answers. These contradictory results as to the impact of monetary incentives on task quality also extend to the context of online reviews. Stephen et al. (2012) conducted a laboratory experiment to study the impact of monetary incentives on reviewer behavior. They found that reviewers who are paid to write are likely to produce more useful content. On the other hand, Wang et al. (2012) performed a laboratory experiment on Amazon Mechanical Turk and found no significant diference in the quality of paid and unpaid reviews. Note that it is hard to capture intrinsic motivation in a laboratory setting, which is a key factor driving behavior in review platforms. Therefore, one has to be careful when extrapolating results from lab experiments. As we discuss later, our results from a naturally occurring experiment appear to be significantly diferent from their findings.

In summary, our work is related to the existing literature on online reviews, specifically on the review generation process. Prior works have discussed several factors that intrinsically motivate people to write reviews, such as the need for uniqueness and attention. Meanwhile, there are a few works with mixed findings that use laboratory experiments to examine the efect of extrinsic rewards on the quantity and quality of reviews. Furthermore, previous studies in related contexts such as crowdsourcing show conflicting results that may not apply to review platforms because of the structural diferences between the environments. Given that there is virtually no empirical evidence to show the implications of the practice of using monetary incentives to attract reviewers, our study aims to fill this gap by examining how monetary incentives afect the review components that have been shown to be of consequence to consumer behavior, the impact of such incentives on intrinsically motivated reviewers, and the implications of using monetary incentives for the review platform. To our knowledge, our work is the first to empirically investigate the impact of economic incentives, particularly monetary rewards, on an online review platform. This research is also particularly important for practitioners as the use of monetary incentives in online review platforms has become common among online retailers.

## 3. Hypothesis Development

In this section, we develop our research hypotheses related to the impact of monetary incentives on online reviews and the review platform. Because previous literature that studied online reviews primarily examined them at the content-level (e.g., Chevalier and Mayzlin 2006, Luca 2011) and the platform-level (e.g., Hu et al. 2009), we also separate our hypotheses development and analyses into those two levels. Our content-level hypotheses examine how monetary incentives afect review-level characteristics. The platformlevel hypotheses and analyses investigate the efect of monetary incentives on the aggregated platform-level parameters. We present a summarized framework of our research hypotheses in Figure 1.

Before developing our research hypotheses, we highlight a few specific details relevant to our empirical study. First, the retailer, who is the platform owner, provides monetary incentives on the review platform. Note that the owner of the review platform does not directly manufacture any of the products. Hence, it generally does not favor one product over another: Arguably the platform’s main objective is to provide meaningful, impartial, high-quality, useful reviews to consumers. Second, online review platforms typically tend to impose restrictions on reviews posted, for example, a minimum number of words to ensure the reviews are meaningful. Similar restrictions are imposed on several online review platforms such as Best Buy, Kmart, and Rakuten. Our analysis evaluates the changes in review elements and characteristics in response to the monetary incentive program conditional on all such requirements remaining the same. Third, monetary rewards ofered by the platform are solely based on the number of reviews contributed by reviewers as long as those reviews meet the requirements (in this case, they must be at least 50 characters long). The example platforms mentioned earlier also follow this policy.

Figure 1. The Framework of Our Hypotheses  
![](/api/attachments/YC8QJGMC/fulltext/images/ddb33a588666daddfee56c1efd072d1611ccac6920302e04fb15da29bedc9bd9.jpg)

## 3.1. Content-Level Hypotheses

We first focus on review-level characteristics, and investigate how the introduction of monetary incentives impacts them. Because the total number of reviews can obviously and intuitively be expected to increase because of monetary incentives, we are primarily interested in how monetary incentives afect review quality and valence.

3.1.1. Review Quality. Review quality typically represents the efort exerted by the reviewers, since better quality reviews require more time and efort. Writing reviews without receiving monetary rewards is similar to contributing to a public good (Bolton et al. 2004, Chen et al. 2010a) and contributions to a public good are largely driven by intrinsic motivation (Li et al. 2012). We develop our hypotheses about the interaction between intrinsic and extrinsic motivations using two related conceptual backgrounds, i.e., rationality and reciprocity.

Recall that monetary rewards from the platform are based on the number of reviews posted, and not on review quality. Hence, once the minimum length requirement to get the reward is met, the marginal financial payof of exerting more efort and writing additional details goes to zero. If new reviewers are mainly rational utility maximizers driven by extrinsic rewards, they exert minimal efort and write short reviews just to satisfy the requirements. In addition, extrinsic rewards can undermine intrinsic motivation due to the motivation crowding-out efect, a phenomenon wherein extrinsic rewards negatively afect intrinsic motivation (Kreps 1997). This unintended impact of monetary incentives has been extensively researched by psychologists and behavioral economists in contexts such as labor productivity and creativity (e.g., Kohn 1999). In our context, if this efect of monetary rewards is dominant, reviewers would end up exerting less efort and writing lower quality reviews.

On the other hand, it is possible that recipients of monetary rewards may develop a sense of gratitude toward the platform (Wood et al. 2011). The reward could invoke a strong sense of direct reciprocity (May 1987) and encourage reviewers to spend more efort in writing reviews (i.e., write reviews with better quality) to show their appreciation. A number of existing studies have found a positive relationship between monetary incentives and contribution quality. For instance, Stephen et al. (2012) concluded in their laboratory experiment study that paid reviewers tend to write higher quality reviews. Based on the above discussion, the impact of monetary rewards on review quality is not obvious. Therefore, we motivate this hypothesis as an open empirical question:

Hypothesis 1A (H1A). Review quality decreases after monetary incentives.

Hypothesis 1B (H1B). Review quality increases after monetary incentives.

3.1.2. Review Valence. Review valence captures reviewers’ experience of the product. However, external environmental factors can afect the transformation process between experiencing the product and writing a review. In that regard, we consider the efect that monetary incentives may have on such a transformation process through two possible avenues in the development of this hypothesis.

First, since it is generally acknowledged in the literature that reciprocity afects perception (e.g., Jiang et al. 2013), it is likely that reciprocity afects the transformation process, and eventually impacts review valence as well. We first consider indirect reciprocity, which is the mechanism whereby the recipient of an altruistic act who experiences gratitude is motivated to be more generous toward parties other than the giver (Nowak and Roch 2007). Such “pay-it-forward” behavior is observed in prior experimental and empirical studies. For example, Greiner and Levati (2005) found that indirect reciprocity enables mutual cooperation in social interactions. Baker and Bulkley (2014) found that the more help an organization member receives, the more likely that member is to help others. With indirect reciprocity, reviewers who receive monetary incentives from the review platform are expected to be more lenient toward the products they review. As a consequence, we expect to see a more positive average review valence. In addition, we consider direct reciprocity, i.e., gratitude that reviewers feel toward the platform for the reward (May 1987). As it is common knowledge that higher star ratings would increase product sales (Luca 2011), it is possible that reviewers receiving a reward would try to reciprocate by issuing high star ratings with the intention to help improve product sales, and as a result, help the platform. Therefore, the predicted efect of direct reciprocity is similar to that of indirect reciprocity, and both should result in more positive average review valence.

Second, the rewards could also afect the type of users who write reviews on the platform. Specifically, it is likely that monetary incentives bring another group of reviewers (who would otherwise not write reviews) to the platform. This group of users may not have fully experienced the product, but may still write reviews to get the rewards. Therefore, their reviews are not completely truthful. The literature on lying behavior has shown that liars tend to avoid creating costs for other parties when they benefit from their lies (e.g., Erat and Gneezy 2012). Similarly, reviewers who are writing reviews just to get the rewards without having adequate knowledge of the product would likely tend to write more positive reviews as their behavior amounts to telling white lies.

As we invoked reciprocity earlier, note that the direct reciprocity can also have the opposite efect. For example, direct reciprocity could drive reviewers to reward the platform by putting in more time and efort and writing more honest reviews. If this is the case, review valence may not be positively impacted by monetary incentives as discussed earlier. Furthermore, it is also plausible that the monetary incentives can bring in other types of reviewers in a diferent way. For instance, before monetary incentives, platform reviews were likely to follow the brag-and-moan model (Hu et al. 2009). Essentially, writing reviews is costly and the benefits are higher if the experience with the product is highly positive or negative. As a result, most reviews on the platform are extreme. Also, the distribution of reviews is J-shaped meaning that the volume of reviews with a 5-star rating outweighs the volume of reviews with a 1-star rating. With monetary incentives, it is plausible that the reward lowers the cost of writing reviews in general. Thus, more moderate reviewers (who would otherwise not contribute) would begin to write reviews on the platform. In this case, the average valence could become more positive or more negative.

In summary, as we cannot categorically predict the impact of monetary incentives on review valence based on existing theories, we motivate this hypothesis as an open empirical question:

Hypothesis 2A (H2A). Review valence becomes more positive after monetary incentives.

Hypothesis 2B (H2B). Review valence becomes more negative after monetary incentives.

## 3.2. Platform-Level Hypotheses

In this section, we examine how the introduction of monetary incentives afects the review platform, specifically, how it afects existing reviewer behavior, the number of new reviewers, and the bias in selecting the product to review.

3.2.1. Behavior of Existing Reviewers. Existing reviewers are users who contributed reviews to the platform before the introduction of incentives. As discussed when developing our first hypothesis, writing online reviews is akin to contributing to a public good and contributions to a public good tend to be driven by intrinsic motivation. In that regard, the existing reviewers may be viewed as driven solely by intrinsic motivation. However, monetary incentives have been shown to create unintended negative efects when interacting with intrinsic motivation (e.g., Kohn 1999, Bénabou and Tirole 2006). Mellström and Johannesson (2008) empirically found that monetary rewards could actually undermine the contribution level of volunteers in the context of blood donation. This negative efect is especially relevant in contexts where intrinsic motivation is the primary driver of behavior (Gneezy et al. 2011). In the context of online review platforms, reviewers spend time and efort in writing reviews, so naturally, both the quantity and quality of reviews are functions of reviewers’ efort level. Therefore, drawing comparisons with previous literature in other contexts, we hypothesize that monetary incentives will have a negative efect on existing reviewer participation. We test this hypothesis by investigating the efect of incentives on the quantity and quality of reviews. Formally,

Hypothesis 3 (H3). Existing reviewers reduce their efort level after monetary incentives.

3.2.2. Number of New Reviewers. The next interesting question is whether monetary incentives could persuade new reviewers to join and contribute. Note that users are heterogeneous in their contribution costs and in how they derive utility from contributing. It is reasonable to assume that on average, and ceteris paribus, users who were not contributing reviews before monetary incentives have lower levels of intrinsic motivation compared with existing reviewers. Some of these users have suficiently low entry costs that they could be encouraged to start contributing by the monetary incentives. On the other hand, the crowdingout efect (Titmuss 1970) could reduce the number of new reviewers, since the introduction of rewards could negatively impact their intrinsic motivation, and as a result, dissuade some users from joining the platform. Therefore, it is an empirical question whether the monetary incentives help incentivize new reviewers to join or reduce the number of new reviewers. Formally, we have the following two competing hypotheses:

Hypothesis 4A (H4A). The total number of new reviewers increases after monetary incentives.

Hypothesis 4B (H4B). The total number of new reviewers decreases after monetary incentives.

3.2.3. Bias in Selecting Products to Review. Hu et al. (2009) note that biases in review platforms may be due to purchasing (more positively reviewed products are purchased more often and therefore have a higher chance of receiving reviews) or under-reporting (reviewers find the “entry cost” for writing reviews to be too high and thus do not write reviews unless they are extremely negative or positive about their experience). As mentioned earlier, we mainly focus on how review generation is afected as a consequence of monetary incentives. Understanding bias is important for practitioners because they can invest in practices to alleviate such biases.

We hypothesize that after the introduction of monetary rewards, reviewers are more likely to choose highly rated products to review for the following reasons. First, as we argued in the development of H2A, indirect reciprocity likely induces reviewers to write more positive reviews. The theory of information cascade claims that users who choose not to conform to the majority assessment are more likely to sufer from cognitive stress (Kuran and Sunstein 1999). Therefore, to reduce that cognitive stress, reviewers choose to review products that are already highly rated. Second, relatedly, cognitive stress increases when more people express their opinion (Lee et al. 2015). Because monetary incentives increase the review volume, we expect the conformity efect to also be stronger. Third, previous literature has shown that less experienced reviewers tend to follow the crowd more than experienced reviewers (Moe and Schweidel 2012). Because we expect an increase in the number of new reviewers as discussed earlier, overall, we expect that reviewers will conform more with the crowd. Fourth, when writing positive reviews, users who are strictly rational utility maximizers can minimize their efort by choosing highly rated products and borrowing product specifications and characteristics already mentioned in the existing reviews. Therefore,

Hypothesis 5 (H5). Reviews are concentrated more toward highly rated products after monetary incentives.

## 4. Research Context and Data

To test the research hypotheses, we collected data from two online retailers. In this section, we provide information about the study context and details on the platforms we study.

## 4.1. The Treated Platform

Our main platform of interest is a large American retailer with billions of dollars in annual revenues with brick-and-mortar and online operations. Although it has subsidiaries that operate in other North American countries, we gathered our data from one of its e-commerce websites that primarily serves customers in the United States. On April 13, 2013, this platform introduced a monetary reward program to incentivize reviewers (no extrinsic rewards were ofered by the platform before April 2013). According to the incentive program, reviewers receive 25 loyalty points for every review they submit. Reviews must be at least 50 characters, a requirement that also existed before introduction of the incentive program. A reviewer can be rewarded for up to eight reviews per year, earning a maximum of 200 loyalty points. Note that no restrictions are placed on the number of personas a reviewer can use for writing reviews. Also, reviewers are allowed to review products that they did not purchase on the platform. The points earned can be exchanged for certificates that can be used toward instore or online purchases of products and services (certificates could not be used to buy gift cards). A reviewer needs 250 points for a \$5 certificate with additional certificates issued only in 250 point increments.<sup>2</sup> The certificates, including those issued to other personas, could be combined when purchasing products before August 2013. Afterward, only multiple certificates issued to the same persona can be combined. This incentive structure (issuing rewards based on level of participation) was a common practice among review platforms in 2013. For example, Rakuten ofered 100 points (valued at \$1) for each review posted by a verified purchaser. Another example is Kmart, which ofered 500 points (valued at \$0.50) for every review that met their minimum length requirement. The decision of the treated platform to introduce a new incentive mechanism provides us with an ideal setting for a natural experiment design.

As to the product type, we chose the video games category for the following reasons. First, video games are very good examples of experience goods that fit our research interest. Features of search goods can easily be observed before purchase. On the other hand, it is hard to evaluate the features of experience goods before purchase (Nelson 1970, Tirole 1988). Therefore, reviews of experience goods are generally more important and have greater impact. Second, the life cycle of video games is reasonably long, so we can observe reviews of video games of diferent qualities without significant censoring issues. This is not the case for some other products such as laptops, which typically have short life cycles, and reviews of obsolete models are not available. Third, practically all video games have a unique identifier that can be used to quickly identify them across diferent platforms. Fourth, many empirical papers have studied video games as their product category of choice (e.g., Zhu and Zhang 2010, Nair 2007).

We started collecting data in August 2013. We began by acquiring a list of available products in the video games category on the treated platform. For each product, we then collected product details and all of the information about the product reviews. As we explain in Section 4.2, we also collected reviews from a control platform for the corresponding products. We eliminated products that were invalid (such as products wrongly classified as video games) and those listed multiple times (e.g., digital download and preowned versions of the same product). We also discarded anonymous reviews (which accounted for only around 1.3% of the original sample). In the end, we had 6,316 reviews written by 5,242 users for 963 products. Note that of those 963 products, 804 were released before the beginning of the time window of our study (January 1, 2013) to which 4,035 of the reviews belong.

## 4.2. The Control Platform

We collected data on the same set of products from another review platform to serve as the control group for our analysis. We examined several e-commerce websites as candidates, including click-only retailers (such as Amazon.com and Newegg.com) and clickand-mortar retailers (such as Walmart.com). The most important requirement was that the platform not ofer any direct monetary rewards for writing reviews over the time frame of our study.<sup>3</sup> We found that Amazon.com not only had the largest set of products but also the largest number of reviews. In addition, Amazon reviews are widely used by customers as a reputable source of information, and many previous papers have used review data from Amazon to study various problems related to online reviews and electronic word-ofmouth (e.g., Chevalier and Mayzlin 2006, Shen et al. 2015). Furthermore, Amazon’s review platform is stable and consistent, making it an ideal candidate as a control group. Figure 2 shows the distribution of star ratings of reviews on Amazon.com for reviews posted between January and March 2013 (the first time frame of our analysis), and between May and July 2013 (the second time frame of our analysis). The distributions look almost identical. We also performed the chi-square goodness of fit test to compare the two distributions. The p-value for the test was 0.12, so we found no statistically meaningful diference between pre-treatment and post-treatment distributions.

We collected review data from Amazon.com for the time of our study, January to July 2013. In total, 37,672 reviews from 28,342 reviewers were collected for the same 963 products as those on the treated platform; 26,823 of these reviews were written for the 804 products that were released before January 1, 2013. The summary statistics of the review elements and characteristics are presented in Table 1. The statistics are calculated separately for the treated platform and control platform, and for both time periods. “Before” corresponds to the time period before monetary incentives, while “After” corresponds to the time period afterward. Additional summary tables that summarize the descriptive statistics for other variables that will be used in the analysis are provided in Online Appendix B.

Figure 2. The Distribution of Star Ratings of Reviews on Amazon.com in Two Time Frames  
![](/api/attachments/YC8QJGMC/fulltext/images/a3029a7e82ef7e6f3497385d432bf33fa74c7053eade54d76874f78ce03fcadf.jpg)

![](/api/attachments/YC8QJGMC/fulltext/images/914816da09fdc899a1dc5949a81eee421f71019088a935943924076763a26e1f.jpg)

Table 1. Summary Statistics of Review Elements (Cross-Sectional, per Product)

<table><tr><td rowspan="3"></td><td colspan="6">Treated platform</td><td colspan="6">Control platform</td></tr><tr><td colspan="3">Before</td><td colspan="3">After</td><td colspan="3">Before</td><td colspan="3">After</td></tr><tr><td>Mean</td><td>S.D.</td><td>N</td><td>Mean</td><td>S.D.</td><td>N</td><td>Mean</td><td>S.D.</td><td>N</td><td>Mean</td><td>S.D.</td><td>N</td></tr><tr><td>Total number of reviews</td><td>1.4</td><td>5.0</td><td>804</td><td>3.6</td><td>8.5</td><td>804</td><td>21.5</td><td>4.2</td><td>804</td><td>11.9</td><td>18.7</td><td>804</td></tr><tr><td>Average title length (in words)</td><td>4.5</td><td>1.8</td><td>256</td><td>4.0</td><td>1.4</td><td>405</td><td>3.5</td><td>1.2</td><td>723</td><td>3.7</td><td>1.9</td><td>671</td></tr><tr><td>Average content length (in words)</td><td>51.3</td><td>57.2</td><td>256</td><td>33.2</td><td>17.4</td><td>405</td><td>61.6</td><td>56.1</td><td>723</td><td>67.2</td><td>55.8</td><td>671</td></tr><tr><td>Average star ratings</td><td>4.3</td><td>0.8</td><td>256</td><td>4.3</td><td>0.7</td><td>405</td><td>4.2</td><td>0.7</td><td>723</td><td>4.2</td><td>0.8</td><td>671</td></tr></table>

## 5. Empirical Analysis and Results

In this section, we discuss our empirical models, present the results of our analyses, and discuss our findings. We organize our analyses and present the findings based on the modeling approaches we use. Therefore, the sequence of models will not exactly follow that of Section 3. At the end of this section, we present Table 13 to summarize our findings on the research hypotheses. In addition, we use DID as our identification strategy in many of the analyses below, one of the assumptions of which is that treatment and control groups follow the same pre-treatment trend. To test the validity of this assumption, we use the Augmented Dickey–Fuller (ADF) test of stationarity between the two pre-treatment data sets (i.e., the data from the treated and control platforms between January and March 2013). The results of the tests for all measures are provided in Table 14, after we introduce and study these measures.

## 5.1. Content-Level Analyses

We start our analysis at the content level where we empirically examine the impact of monetary incentives on review quality and valence. We use four diferent measures to evaluate changes in review quality. Our first measure is review length (i.e., word count). It has been shown that word count outperforms more complex methods in evaluating the quality of Wikipedia articles (Blumenstock 2008). Furthermore, in the specific context of online reviews, Mudambi and Schuf (2010) found a positive connection between review length and review quality. Our second measure of review quality is the helpfulness score that is provided by other users. The helpfulness score is widely used in the literature to measure review quality (e.g., Ghose and Ipeirotis 2006, Chen et al. 2008). In addition to these two numerical measures, we study the changes in textual features of reviews. We first use readability analysis as an alternative method of measuring review quality. The readability index has been shown to be a reliable indicator of online review quality (e.g., Korfiatis et al. 2008, Li et al. 2016). Last, we study the change in the information content of review text. Specifically, we measure the change in frequency of feature-related discussions in reviews posted before and after monetary incentives.

For review valence, we use two diferent variables that are widely used in the literature. Following Chintagunta et al. (2010), our first measure is the star rating associated with online reviews. As highlighted in Section 2.1, star ratings capture a quantified summary of review details and customer experience within one dimension (a number between 1 and 5). In addition to the star ratings, we examine the textual content of the reviews and use sentiment analysis to investigate changes in the sentiment of the reviews.

5.1.1. Review Length and Star Ratings. For this analysis, we set up our data as a panel data set such that each observation corresponds to a review. As discussed previously, the monetary incentive program was introduced in the middle of April 2013. Hence, to study the impact of the treatment, we compare diferent measures of interest on the treated platform against the control platform before and after the treatment. To ensure that we are not measuring only the immediate treatment efects, we drop the data for April 2013 and compare three months before and after the month of treatment (April). As a result, our data set covers reviews from January 1 to March 31, 2013 (before treatment) and May 1 to July 31, 2013 (after treatment). The unit of time is defined to be semimonthly, so we have a total of 12 time periods, i.e., six periods before and six after the treatment. For the product set, we first conduct our analysis on reviews of products released before the beginning of the time window of our study to ensure that all reviews are displayed on the review platform in the pre-treatment period for as long as they are displayed in the post-treatment period (i.e., the panel is balanced). In total, there are 2,916 reviews of 804 products on the treated platform that meet this criterion. As a robustness test, we later included all 963 products in the data set and found that the results are consistent.

Drawing inferences about the efect of an exogenous event solely based on the analysis of data from the treated platform could present identification issues.

Product characteristics could impact review elements. For example, the release of an update for some video games after treatment could afect user experience and result in changes in reviews. If we only use data from the treated platform, we might mistakenly attribute such factors to the treatment. Therefore, as discussed in Section 4.2, we leverage data from another review platform as the control group during the same time period, and use the DID approach as our identification strategy. The DID technique has been widely used in IS literature to account for potential identification issues similar to those we described earlier (e.g., Hosanagar et al. 2013, Chan and Ghose 2013).

To control for product-level characteristics, we matched products across two review platforms using a 2-stage matching practice. First, we used an automated script to match products based on their names and gaming platforms. Only products with exactly the same name and gaming platform are matched at this stage. Then as a second step, we performed a manual screening to match the rest of the products. This way, we can include product, time, and platform fixed efects in our DID regression framework. The analysis is performed at the review-level with the following model specification:

$$
D V _ {i t p} = \alpha_ {i} + \delta_ {t} + \zeta_ {p} + \beta \mathbf {X} _ {i t p} + \gamma M _ {t p} + \epsilon_ {i t p}.\tag{1}
$$

In Equation (1), $D V _ { i t p }$ is the dependent variable of interest, $\alpha _ { i }$ captures product fixed efects, $\delta _ { t }$ captures time fixed efects, and $\zeta _ { p }$ captures platform fixed efects. Meanwhile, $M _ { t p }$ is a dummy variable that takes the value 1 if the review is written on the treated platform in the post-treatment period (after the introduction of the monetary incentives) and 0 otherwise; $\mathbf { X } _ { i t p }$ is a set of control variables.

The results of three DID models for title word count, content word count, and star ratings are presented in Table 2. Star rating is used to measure review valence, while title and content review word count are proxies for review quality. The number of new products represents the number of new video games released on the relevant platform in a given time period. The release of new products might afect how much attention, time, and efort users dedicate to writing reviews for existing products. Alexa rank is the global website rank provided by Alexa.com for the relevant platform at the end of each time period. This time-varying control captures potential shocks to the popularity of platforms that might afect user involvement. Other potential confounding factors that are unchanging at the levels of platforms, products or time are captured by the fixed efects. Note that we apply the natural logarithm to star ratings, title word count, and review word count since the distributions of these variables are right-skewed.

The findings suggest that monetary incentives resulted in a significant decrease in the word count of the title and review content, which supports H1A. Monetary incentives appear to have a significant influence on the rational side of reviewers on average for an efort-intensive task such as writing reviews. Hence, reviewers spend less efort and write shorter reviews, since additional efort beyond the required minimal level does not earn them additional rewards. In addition, the incentive program significantly increases the star ratings of reviews. This finding supports H2A and provides evidence that the efect of indirect reciprocity (Nowak and Roch 2007) is prominent in our context. As reviewers receive monetary incentives from the platform, they act more generously toward products they review and issue higher ratings. Also, it appears that, on average, the impact of direct reciprocity does not contradict the indirect reciprocity efect. In other words, reviewers who wish to show their gratitude to the review platform also seem to be doing so by giving higher star ratings. To ensure robustness, we consider alternative specifications such as including reviews of all 963 products and defining alternative time periods such as February to June 2013. Results from all these alternative specifications are qualitatively similar.

Table 2. Results from the Regression Analysis Using the Diference-in-Diferences Approach

<table><tr><td></td><td>log(title word count)</td><td>log(content word count)</td><td>log(star ratings)</td></tr><tr><td> $M_{tp}$ </td><td>-0.120***(0.027)</td><td>-0.241***(0.036)</td><td>0.058***(0.019)</td></tr><tr><td>Number of new products</td><td>-0.002*(0.001)</td><td>-0.001(0.001)</td><td>-0.001**(0.001)</td></tr><tr><td>Alexa rank</td><td>-0.001(0.001)</td><td>0.001(0.001)</td><td>0.001**(0.001)</td></tr><tr><td>Constant</td><td>1.081***(0.015)</td><td>3.783***(0.023)</td><td>1.437***(0.010)</td></tr><tr><td>Product fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Platform fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>26,548</td><td>26,548</td><td>26,548</td></tr><tr><td>Adjusted R-squared</td><td>0.011</td><td>0.033</td><td>0.003</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by product. <sup>∗</sup>p < 0.1; <sup>∗∗</sup>p < 0.05; <sup>∗∗∗</sup>p < 0.01.

5.1.2. Review Helpfulness Score. In Section 5.1.1, we studied review length as a proxy for review quality. Here, we examine the change in the helpfulness score of the reviews to further investigate the efect of monetary incentives on review quality. For every review posted on the treated platform, there is a question at the bottom of the review asking if the review is helpful. Helpfulness score is a non-negative number showing the total number of helpful votes the review has received (so it can only increase over time). No additional information (such as the history or trend of the score) is provided. Therefore, ceteris paribus, older reviews (i.e., reviews posted earlier) are likely to have higher review helpfulness scores compared with more recent reviews because they have had more time to get helpfulness votes. Note that reviews written after the treatment are by definition more recent. ${ \mathrm { S o } } ,$ to ensure a fair comparison, we need to define the helpfulness measure for reviews written before and after the monetary incentives over a consistent and equal time frame.

For this analysis, we re-collected review helpfulness scores for the reviews in our data set in February 2015. Some products were no longer available in February 2015 on the treated platform, so we discarded those product reviews. After removing those observations, we had 2,151 reviews from 272 products. For each review, we determined the change in the review helpfulness score between August 2013 and January 2015. This measure is directly comparable across all reviews in our data set, regardless of when they were written. Unlike our analysis on review length and star rating, review helpfulness is unlikely to be afected by confounding time-varying factors. For example, an external shock that could change the helpfulness of a particular review over time is unlikely. Therefore, we are in a position to use the following specification to analyze the impact of monetary incentives on the change in the review helpfulness score for review j for product i:

$$
\begin{array}{c} \text {ChangeInHelpfulnessScore} _ {i j} \\ = \alpha_ {i} + \beta \text {ReviewAge} _ {i j} + \gamma M _ {i j} + \epsilon_ {i j}, \end{array}\tag{2}
$$

where $\alpha _ { i }$ captures product fixed efects and Review $A g e _ { i j }$ is the age of review j in months on July 31, 2013. Although our dependent variable measures the change in helpfulness during a fixed period, there could still be some diferences between reviews due to diferences in when they were written. Review $\boldsymbol { \mathrm { i } } g \boldsymbol { e } _ { i j }$ controls for such potential residual diferences. Meanwhile, $M _ { i j }$ is a dummy variable that takes the value 1 if review j is posted after the introduction of monetary incentives and 0 otherwise.

Table 3 reports the results from the analysis. The increase in review helpfulness score is significantly lower for reviews posted after monetary incentives compared with reviews posted before. The size of the diference is relatively large, since the increase in review helpfulness score is generally small (0.16 on average). This result indicates that reviews posted after monetary incentives are not only shorter (as reported in 5.1.1) but also less helpful in the eyes of customers, which further supports H1A. This is consistent with the finding in previous literature that review length and helpfulness scores tend to be correlated for experience goods (Mudambi and Schuf 2010). Note also that the estimated relationship between review age and changes in review helpfulness score is negative, indicating that older reviews are less likely to receive additional helpfulness votes. This behavior is consistent with the treated platform’s review system which, by default, sorts reviews by age from newest to oldest in ascending order.

Table 3. Changes in Review Helpfulness Score

<table><tr><td></td><td>Change in helpfulness score</td></tr><tr><td> $M_{ij}$ </td><td>-0.173***(0.051)</td></tr><tr><td>Review age</td><td>-0.049***(0.012)</td></tr><tr><td>Constant</td><td>0.319***(0.085)</td></tr><tr><td>Product fixed effects</td><td>Yes</td></tr><tr><td>N</td><td>2,151</td></tr><tr><td>Adjusted R-squared</td><td>0.387</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by product.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

As a robustness check, we also considered including reviews of products that were released after the start of our period of analysis. After including them, the data set consists of 3,340 reviews from 339 products. The results are qualitatively similar.

5.1.3. Textual Feature Analysis. Thus far, we have focused on the changes in quantitative review measurements such as star rating, helpfulness score, and word count. However, the value of online reviews is not limited to such quantitative measurements. Previous literature has established that textual features of online reviews are also important, and contain information in addition to quantitative measures (e.g., Pavlou and Dimoka 2006, Archak et al. 2011). Hence, in this section, we investigate our research hypotheses by analyzing review contents using several textual analysis techniques. These analyses help us learn about the content of reviews and investigate the robustness of our earlier findings. Particularly, we conducted a sentiment analysis to investigate changes in review valence, a readability analysis to provide an alternative measurement of the changes in review quality, and a topic modeling to analyze the diferences in review content between the two time frames. Note that the analyses in this section were conducted on the reviews from the same data set used in our main analyses in Section 5.1.1.

Readability Analysis and Sentiment Analysis. We start our analysis of textual content by calculating the Gunning–Fog (GF) index (Gunning 1969) to measure the readability of reviews and examine the changes in the value of the index before and after monetary incentives. The GF index estimates the years of education readers need to understand the text the first time they read it. This index has been widely used in the IS literature to calculate readability scores, especially for online reviews (e.g., Goes et al. 2014, Yin et al. 2016). In addition, previous literature has established that higher GF index values (i.e., more complex text) are usually associated with higher review quality as perceived by consumers (e.g., Korfiatis et al. 2008, Li et al. 2016). The formula used to calculate the index is as follows; “complex words” are defined as those with three or more syllables

Gunning–Fog Index

$$
\begin{array}{l} = 0. 4 \times \left[ \frac {\text { Number   of   Words }}{\text { Number   of   Sentences }} \right. \\ \left. + \left(\frac {\text { Number   of   Complex   Words }}{\text { Number   of   Words }} \times 1 0 0\right) \right]. \end{array}\tag{3}
$$

We then measured the sentiments of reviews posted before and after monetary incentives and across the treated and control platforms. We examined positive and negative sentiments of review content as they reflect the objectivity of reviews (Lu et al. 2013). We used the Harvard General Inquirer<sup>4</sup> to perform sentiment analysis. The Harvard General Inquirer is a lexiconbased content analysis tool that is widely used to extract the tone and sentiment of textual content such as financial reports (e.g., Loughran and McDonald 2011), news stories (e.g., Tetlock et al. 2008), and review text (e.g., Shen et al. 2015). We adopted an approach similar to that used by Shen et al. (2015) to analyze the sentiment of review text by using the frequency of positive and negative words in each review to measure the sentiment of that review.

After calculating the GF index, the percentage of positive words, and the percentage of negative words for each review, we then performed the DID test using a regression framework with the same specification presented in Equation (1). Results are reported in Table 4.

Regression estimates imply that the GF index significantly decreased after the monetary incentive program was introduced. In other words, the reviews posted after the treatment were on average less complicated than those posted before. Our results from Sections 5.1.1 and 5.1.2 indicated that reviews posted after monetary incentives are of lower quality (shorter and less helpful); the results from the analysis of changes in the GF index further corroborate those findings. Our results are therefore consistent with the previous literature that studies the connection between readability score and review quality (e.g., Korfiatis et al. 2008, Li et al. 2016). Therefore, H1A is further supported.

Results from the sentiment analysis in the third and fourth columns in Table 4 indicate that monetary incentives increase positive review sentiment (although the statistical power is weak), and significantly reduce negative sentiment. These results further validate our earlier findings in Section 5.1.1 that monetary incentives induce reviewers to be more generous toward the products and hence reviews are more positive. This provides further support for H2A, implying that indirect reciprocity is a strong factor in the presence of monetary incentives in this context.

Topic Modeling. Analyzing the sentiment and readability of review text, we found that users are writing simpler and more positive reviews after the introduction of monetary incentives. In this section, we study whether the information content of review text changes post treatment. To do so, we take advantage of the topic modeling approach. Topic modeling is an unsupervised learning algorithm for discovering the main themes of unstructured documents and generating a predefined number of topics (Blei 2012). Topics are estimated as latent constructs and the number of topics must be fixed before estimation. Topic modeling has been recently used by IS researchers to identify topics from textual content (e.g., Singh et al. 2014, Shi et al. 2015).

Table 4. Results from the Textual Feature

<table><tr><td></td><td>Gunning-Fog index</td><td>Percentage of positive words</td><td>Percentage of negative words</td></tr><tr><td> $M_{tp}$ </td><td>-0.464***(0.135)</td><td>0.422*(0.253)</td><td>-0.418***(0.141)</td></tr><tr><td>Number of new products</td><td>0.016***(0.005)</td><td>-0.020**(0.008)</td><td>0.007(0.004)</td></tr><tr><td>Alexa rank</td><td>0.001(0.005)</td><td>0.002(0.010)</td><td>0.004(0.006)</td></tr><tr><td>Constant</td><td>7.677***(0.081)</td><td>8.699***(0.149)</td><td>2.355***(0.081)</td></tr><tr><td>Product fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Platform fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>26,548</td><td>26,548</td><td>26,548</td></tr><tr><td>Adjusted R-squared</td><td>0.006</td><td>0.009</td><td>0.001</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by product. <sup>∗</sup>p < 0.1; <sup>∗∗</sup>p < 0.05; <sup>∗∗∗</sup>p < 0.01.

We used the topicmodels package in R (Grün and Hornik 2011) to analyze review text on treated and control platforms pre- and post-treatment. The package uses Gibbs sampling to estimate the distribution of terms over topics and the distribution of topics over reviews given an a priori fixed number of topics. We ran the model with two, three, four, and five topics, and inspected the distribution of terms. We found that the choice of two topics provided the most meaningfully and intuitively separated distribution.<sup>5</sup> In the first identified topic, the terms “great,” “love,” “fun,” “good,” and “enjoy” are the top five terms. So this topic likely represents the quality of the game and user experience. The top five terms for the second topic are “make,” “character,” “story,” “player,” and “level.” So the second topic is clearly related to the features of the video games. In other words, the second topic includes likely useful information, while the first topic relays information akin to that summarized in the star rating. For the number of topics greater than two, the topics are not easy to distinguish, define, and label (i.e., other topics appear to be essentially a combination of the first two topics). In addition, we used four goodness of fit metrics to ensure the validity of our choice. The metrics proposed by Cao et al. (2009) and Deveaud et al. (2014) suggest that the optimal number of topics is two. The metrics proposed by Grifiths and Steyvers (2004) and Arun et al. (2010), on the other hand, suggest that the optimal number is much larger. Given the intuitively meaningful distribution of words we achieve by choosing two topics, and the conflicting suggestions from these two other metrics, we proceeded with the choice of two topics. More details on this are provided in Online Appendix C.

We are interested in the impact of monetary incentive on the informativeness of reviews, or how much information about product features is included in the reviews. Therefore, we set up a DID regression model where the dependent variable is the probability that a review is related to the second topic (video games features). The right-hand side (RHS) variables are similar to those in our main model in Equation (1). The results are presented in Table 5. Evidently, the treatment efect $M _ { t p }$ is negative and statistically significant. It suggests that the treatment is associated with a decrease of about 0.8% in the discussion of the second topic in the reviews, further supporting our H1A.

It appears that after monetary rewards were introduced, users shared more about their feelings toward the product rather than discussing product features in their reviews. To test the robustness of our finding, we followed a second approach and constructed

Table 5. Regression Results from the Topic Modeling Analysis

<table><tr><td></td><td>Textual topic</td></tr><tr><td> $M_{tp}$ </td><td>-0.008** (0.003)</td></tr><tr><td>Number of new products</td><td>0.001 (0.001)</td></tr><tr><td>Alexa rank</td><td>0.001* (0.001)</td></tr><tr><td>Constant</td><td>0.494*** (0.002)</td></tr><tr><td>Product fixed effects</td><td>Yes</td></tr><tr><td>Platform fixed effects</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td></tr><tr><td>N</td><td>26,548</td></tr><tr><td>Adjusted R-squared</td><td>0.002</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by product.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Bayesian credible intervals using the Gibbs draws. The results show that the decrease in the prevalence of topic 2 (product features) is statistically significant at p-value < 0.01 (99% credible interval is <sup>(</sup>0.004, 0.009<sup>)</sup>).

## 5.2. Platform-Level Analysis

In Section 5.1, we focused on the impact of monetary incentives on reviews. In this section, we investigate the impact of monetary incentives at the platform level. Specifically, we are interested in the changes in existing reviewer behavior due to monetary incentives, how the incentives impact the number of new reviewers, and the implications of monetary incentives for review diversity on the platform. Note that we investigate the change in existing reviewers’ efort by measuring the change in their participation level and the quality of their reviews. We use the number of reviews written as a proxy for participation level, and the length and helpfulness score of the reviews as proxies for review quality.

5.2.1. Existing Reviewer Behavior. In this section, we are interested in the change in existing reviewers’ behavior due to the introduction of monetary incentives. We investigate two review elements, i.e., total number of reviews and the length of the reviews posted by existing reviewers, as these two elements are directly related to the efort level that reviewers contribute to the review platform. For the analyses in this section, we set up the data set at the reviewer level (i.e., each observation is a reviewer). Also, to be consistent with our previous analyses, the period of study covers the sixmonth period between January to March 2013 and May to July 2013, and the unit of time is half a month. Note that we restrict our attention to only active reviewers who wrote at least one review on the treated platform between January 1, 2013 and March 31, 2013 before the introduction of the monetary rewards. In total, 1,259 reviews from 1,071 reviewers were included in the data set.

In the analysis, the independent variable of interest is a dummy variable $M _ { t }$ that takes value 1 if monetary incentives are available at time period t and 0 otherwise. As for control variables, we consider the number of new products released on the treated platform in each time period as a time-varying factor. In addition, one might argue that the decrease in the number of reviews may just reflect a time trend. For example, people might write reviews less often over time. Therefore, we include a time trend as another control variable. We represent the vector of control variables as $\mathbf { X } _ { k t }$

First, as our outcome variables (i.e., the number of reviews, the average title word count of reviews, and the average content word count of reviews posted by existing reviewers in each time period) are power-law distributed, we apply natural logarithm transformation to them.<sup>6</sup> Then, we check for serial correlation in our outcome variables using the method proposed by Wooldridge (2010). We find that none of our dependent variables sufer from autocorrelation. Therefore, we use a fixed-efects panel data model to estimate the efect of monetary incentives on the number of reviews, the average title word count, and the average content word count. For reviewer k at time t, our model specification is as follows:

$$
D V _ {k t} = c + \beta \mathbf {X} _ {k t} + \gamma M _ {t} + \nu_ {k} + \epsilon_ {k t}.\tag{4}
$$

Table 6 reports results from the fixed-efects model. We find that the efect of monetary incentives on the existing reviewers’ efort is twofold. First, monetary incentives reduce the level of participation of existing reviewers, inducing them to write significantly less often.<sup>7</sup> However, once they commit to writing reviews, the quality of participation is not afected by monetary incentives. Hence, the length of reviews posted after monetary incentives by existing reviewers is not statistically diferent from reviews posted before. As a result, our H3 is partially supported. Second, we find that the time trend has a positive efect on the number of reviews although the magnitude of the efect is small. Therefore, it appears that existing reviewers on the treated platform tend to write more reviews over time. Moreover, the number of new products available to the platform has a negative impact on the number of reviews, suggesting a substitution efect. As a result, an increase in the number of new products is associated with a small decrease in the number of reviews posted.

Table 7. Changes in Review Helpfulness Score for Existing Reviewers

<table><tr><td></td><td>Change in helpfulness score</td></tr><tr><td> $M_{ij}$ </td><td>0.098 (0.140)</td></tr><tr><td>Review age</td><td>-0.006 (0.018)</td></tr><tr><td>Constant</td><td>3.045*** (0.318)</td></tr><tr><td>Product fixed effects</td><td>Yes</td></tr><tr><td>N</td><td>764</td></tr><tr><td>Adjusted R-squared</td><td>0.634</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by product.  
<sup>∗</sup>p < 0.1; <sup>∗∗</sup>p < 0.05; <sup>∗∗∗</sup>p < 0.01.

As we observe that the length of reviews posted by existing reviewers does not change before and after incentives, we next examine the change in the review helpfulness score as another measure of review quality. We use the same specification used in Section 5.1.2, but restrict our attention to reviews posted by existing reviewers. The results in Table 7 show no significant diference in the change of review helpfulness scores for reviews posted by existing reviewers in the presence of monetary incentives. Hence, it appears that monetary incentives reduce the level of participation of existing reviewers but not the quality of participation, providing only partial support for H3.

Next, to ensure that our findings are robust, we considered several alternative specifications. First, we changed the definition of an “active reviewer” by instead considering reviewers who write at least once on the treated platform in the eight- and 12-month period before monetary incentives. Second, we changed the time period from semimonthly to monthly. We found the results to be qualitatively similar. In addition, as in our main analysis, we considered using the DID approach to cross-validate our findings. However, note that we could directly identify and match products between the platforms using their names in our analysis of star ratings and review length. Meanwhile, the analysis here is done at the reviewer-level. As we do not have users’ personal information to do a similar matching across the platforms, we instead use propensity score matching (PSM). We match users by scores constructed through the standard logit function based on observable characteristics of the users. PSM has been widely used in the literature (e.g., Smith and Telang 2009, Rishika et al. 2013). In our case, the observable based on which we matched the users is the number of reviews before monetary incentives (i.e., a vector of semimonthly observations of reviews written) for the analysis of number of reviews and the average title word count and average content word count of reviews written before monetary incentives for the analysis of review length. Additional details about the PSM are provided in Online Appendix A. After all users are matched, we use a specification that is similar to Equation (1). Note that data from the control platform consists of 23,057 reviews from 20,886 reviewers. The results, shown in Table $^ { 8 , }$ are consistent with those from the fixed-efects model.

Table 6. Results of the Fixed-Efects Analysis of Existing Reviewers Behavior

<table><tr><td></td><td>log(number of reviews)</td><td>log(title word count)</td><td>log(content word count)</td></tr><tr><td> $M_t$ </td><td>-0.201***(0.006)</td><td>-0.208(0.231)</td><td>0.134(0.231)</td></tr><tr><td>Number of new products</td><td>-0.007***(0.001)</td><td>0.013**(0.007)</td><td>-0.003(0.011)</td></tr><tr><td>Time trend</td><td>0.005***(0.001)</td><td>0.018(0.030)</td><td>0.030(0.036)</td></tr><tr><td>Constant</td><td>0.215***(0.006)</td><td>1.161***(0.088)</td><td>3.393***(0.134)</td></tr><tr><td>Reviewer fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>12,852</td><td>1,121</td><td>1,121</td></tr><tr><td>Adjusted R-squared</td><td>0.125</td><td>0.108</td><td>0.071</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by reviewer.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

5.2.2. New Reviewers. Here, we study whether monetary incentives can bring more reviewers to the treated platform. Therefore, we reconstruct our data set to be a platform-level time series data set with semimonthly time periods. Each observation is the number of new reviewers who post their first review on the treated platform in that time period. In total, we have 3,794 new reviewers who joined the treated platform between January 1 to March 31 and May 1 to July 31, 2013.

We analyze the data by leveraging the Autoregressive-Moving-Average (ARMA) model to study the impact of monetary incentives on the number of new reviewers. In our ARMA<sup>(</sup>p, q<sup>)</sup> model, the order of the autoregressive part is p and the order of the moving average part is q. We use the Akaike information criterion (AIC), and the Bayesian information criterion (BIC) as our model selection criteria, and find that optimal values for p and q are 1 and 2, respectively. Hence, we use ARMA(1,2) as the main model for this analysis, which takes the following form:

Table 9. The Impact of Monetary Incentives on the Number of New Reviewers

<table><tr><td></td><td>ARMA(1,2)</td></tr><tr><td> $M_t$ </td><td>277.24*** (54.29)</td></tr><tr><td>Constant</td><td>173.89*** (39.49)</td></tr><tr><td>ar (L1)</td><td>-0.70 (0.59)</td></tr><tr><td>ma (L2)</td><td>-1.00** (0.44)</td></tr><tr><td>N</td><td>12</td></tr></table>

p < 0.1; p < 0.05; p < 0.01.

$$
\text { NewReviewers } _ {t} = c + M _ {t} + \varphi \text { NewReviewer } _ {t - 1} + \sum_ {i = 1} ^ {2} \theta_ {i} \varepsilon_ {t - i},\tag{5}
$$

where NewReviewers is the number of new reviewers in each time period, and $M _ { t }$ is a dummy variable that is 1 if monetary incentives are ofered in period t and 0 otherwise.

The result, presented in Table 9, indicates that monetary incentives appear to be significantly efective in terms of attracting new reviewers to join the platform. Therefore, H4A is supported. To ensure the robustness of the finding, we considered alternative models such as a Vector Autoregression (VAR) model and an Autoregressive-Moving-Average model with exogenous inputs (ARMAX) that includes other timevarying factors such as the number of new products available to the platform in each time period. In addition, we conducted a DID analysis using the number of new reviewers on Amazon as a control platform. We found that the results from all alternative approaches are qualitatively similar.

5.2.3. Bias in Selecting Product to Write Review. In this section, we are interested in understanding the bias in the way reviewers select products to review changes. Specifically, we study the implications of monetary incentives on how reviews are distributed. We first formally demonstrate that the reviews are written for a less diverse group of products after the treatment. The second analysis builds on the first test to demonstrate the nature of the bias using a regression model, showing that reviews are written disproportionately more for products with higher star ratings. Subsequently, toward the end of the section, we discuss the implications of the bias.

Table 8. Results of the Diference-in-Diferences Analysis of Existing Reviewers Behavior

<table><tr><td></td><td>log(number of reviews)</td><td>log(title word count)</td><td>log(content word count)</td></tr><tr><td> $M_{tp}$ </td><td>-0.048***(0.004)</td><td>0.051 (0.242)</td><td>0.142 (0.283)</td></tr><tr><td>Number of new products</td><td>-0.002* (0.001)</td><td>0.037 (0.033)</td><td>-0.047 (0.046)</td></tr><tr><td>Constant</td><td>0.047***(0.009)</td><td>1.284***(0.432)</td><td>4.869***(0.555)</td></tr><tr><td>Reviewer fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Platform fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>29,988</td><td>2,302</td><td>2,302</td></tr><tr><td>Adjusted R-squared</td><td>0.231</td><td>0.086</td><td>0.125</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by reviewer.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

First, we define “ex ante average star rating” as the average star rating that a reviewer observes before writing a review. Second, we calculate the number of reviews written for diferent levels of ex ante average star ratings, and then determine the cumulative distribution of reviews across the ex ante average star ratings. Third, we construct a curve similar to the Lorenz curve, plotting the cumulative number of reviews written against the sorted ex ante average star ratings (Gastwirth 1971). We derive the Gini coeficient by dividing the area between the Lorenz curve and the 45<sup>◦</sup> line by the total area under the $4 5 ^ { \circ }$ line. This value ranges from 0 (the least concentration and the highest diversity) to 1 (the highest concentration and the least diversity). Gini coeficient is widely used to study diversity (e.g., Brynjolfsson et al. 2011, Hosanagar et al. 2013). In testing H5, we evaluate whether there is a statistically significant diference in the Gini coeficient before and after monetary incentives. To do this, we adopt the permutation test technique (Good 2005), which has also been used by Lee and Hosanagar (2014) to measure the impact of recommender systems on sales diversity. We perform a two-sided permutation test with 10,000 iterations to get the p-value with up to four decimal places.

Figure 3 shows the curves for the two platforms; the corresponding Gini coeficients are reported in Table 10. The left panel in Figure 3 is for the treated platform, while the right panel is for the control platform. The solid lines on both plots represent the Lorenz curve of reviews posted between January and March 2013 (pre-treatment), while the dashed lines represent the curves for reviews posted between May and July of 2013 (post-treatment). Note that the diference between the Gini coeficients for the control platform is not statistically significant. Therefore, it is unlikely that a global systematic change was present that could afect the product reviews on the control platform during the treatment period. As products available in the treated and control platforms are almost identical, we can assume that the same should be true for the treated platform. Now, note that the diference between the Gini coeficients for the treated platform is statistically significant. It implies that, on the treated platform, reviews concentrate more on a few groups of products after the introduction of monetary incentives. We also calculated the diference in Gini coeficients derived from reviews posted on the treated platform between January to March 2012 and May to July 2012, and found that the diference is not statistically significant. A similar finding is observed for the control platform in 2012. So the change in the diversity of reviews on the treated platform could be attributed to the introduction of monetary incentives.

Table 10. The Diferences in Gini Coeficient

<table><tr><td></td><td>Jan-Mar</td><td>May-July</td><td>Differences</td></tr><tr><td>Treated platform</td><td>0.6493</td><td>0.7566</td><td>0.1073** (0.0192)</td></tr><tr><td>Control platform</td><td>0.6812</td><td>0.7196</td><td>0.0384 (0.3321)</td></tr></table>

Note. p-values are reported in parentheses.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

We established that review concentration bias significantly increases after monetary incentives. Next, we characterize the nature of this bias. Generally, reviews are written more for products with higher ex ante star ratings on treated and control platforms, which is consistent with previous literature (e.g., Hu et al. 2009). So, we are interested in formally testing whether reviews written after the monetary incentives are even more concentrated toward the highly rated products. To do so, we use a DID regression model to examine the impact of monetary incentives on how the selection process is afected by the ex ante average star ratings. Therefore, we can account for potential product, time, and platform-level confounders. We leveraged the main data set used in Section 5.1.1, which consists of reviews from treated and control platforms. We constructed the observations at the product level $( \mathrm { i . e . , }$ each observation is a product), while the time period remained semimonthly. For each observation, we calculated the cumulative average star ratings of the product in the previous time periods as our main explanatory variable of interest. Our model specification is as follows:

Figure 3. The Lorenz Curve of Reviews on the Treated and Control Platform Post-Treatment  
![](/api/attachments/YC8QJGMC/fulltext/images/ca869ba6738410c88ddc48222036a74f7080615c07cb3ae95743541b07656f92.jpg)

![](/api/attachments/YC8QJGMC/fulltext/images/d49f3aa1a692883d91822c5a5fe53730c74c194d7c7a9dc009d45eed2bd41f99.jpg)

$$
\begin{array}{r l} & {N u m R e v i e w _ {i t p}} \\ & {\quad = \alpha_ {i} + \delta_ {t} + \zeta_ {p} + \beta \mathbf {X} _ {i t p} + \gamma_ {1} E x A n t e S t a r _ {i t p} \times M _ {t p}} \\ & {\qquad + \gamma_ {2} E x A n t e S t a r _ {i t p} \times P l a t f o r m _ {p}} \\ & {\qquad + \gamma_ {3} E x A n t e S t a r _ {i t p} \times A f t e r _ {t}} \\ & {\qquad + \gamma_ {4} E x A n t e S t a r _ {i t p} + \gamma_ {5} M _ {t p} + \epsilon_ {i t p}.} \end{array}\tag{6}
$$

Here, NumReview $^ { \prime } i t p$ is the total number of reviews for product i at time t on platform $p . \alpha _ { i }$ captures product fixed efects, $\delta _ { t }$ captures time fixed efects, and $\zeta _ { p }$ captures platform fixed efects. Meanwhile, $\mathbf { X } _ { i t p }$ is a vector of control variables. $E x A n t e S t a r _ { i t p }$ is the cumulative average star ratings for product i on platform p at the beginning of time period $t . ~ M _ { t p }$ is a dummy variable that takes the value 1 if the observation is on the treated platform after the introduction of the monetary incentives and 0 otherwise. ${ \mathbf { } } A f t e r _ { t }$ is a dummy variable that takes the value 1 if time period t is after the introduction of monetary incentives. $P l a t f o r m _ { p }$ is a dummy variable that takes the value 1 if p is the treated platform. Regression estimates in Table 11 show that after the monetary incentive program was introduced, previously highly rated products received significantly more reviews, supporting our H5. Surprisingly, the efect of $M _ { t p }$ is negative and significant, suggesting that fewer reviews are written after the treatment. However, together with the interaction term, $E x A n t e S t a r _ { i t p } \times M _ { t p } ,$ the net efect of $M _ { t p }$ on the number of reviews written for products with existing ratings greater than $2 \ ( \mathrm { i . e . } ,$ the majority of reviews) is positive.

The next question, after selecting to review highly rated products, is: What ratings do the reviewers give? Using three months of data after the introduction of monetary incentives, Table 12 shows that average rating changes are larger when ex ante averages are lower. Note that the efect in the first row is expected to be nonnegative since reviewers cannot issue ratings lower than 1, while the efect in the last row is naturally nonpositive because reviewers cannot issue star ratings higher than 5.

Table 11. The Impact of Previous Star Ratings on the Total Number of Reviews

<table><tr><td></td><td>Total number of reviews</td></tr><tr><td> $ExAnteStar_{itp} \times M_{tp}$ </td><td>0.770*** (0.137)</td></tr><tr><td> $ExAnteStar_{itp} \times Platform_p$ </td><td>-2.195*** (0.273)</td></tr><tr><td> $ExAnteStar_{itp} \times After_t$ </td><td>-0.637*** (0.137)</td></tr><tr><td> $ExAnteStar_{itp}$ </td><td>2.017*** (0.303)</td></tr><tr><td> $M_{tp}$ </td><td>-0.971** (0.496)</td></tr><tr><td>Number of new products</td><td>-0.149*** (0.014)</td></tr><tr><td>Alexa rank</td><td>0.043*** (0.004)</td></tr><tr><td>Constant</td><td>-1.782*** (1.165)</td></tr><tr><td>Product fixed effects</td><td>Yes</td></tr><tr><td>Platform fixed effects</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td></tr><tr><td>N</td><td>19,428</td></tr><tr><td>Adjusted R-squared</td><td>0.209</td></tr></table>

Note. Standard errors in parentheses are robust and clustered by product.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

The aforementioned results raise some interesting questions about modeling the review generation process. Consider the brag-and-moan model in Hu et al. (2006) which assumes that reviewers gain more utility from writing extreme reviews. However, they assume that the “entry costs” they face are independent of whether reviewer’s experience is positive or negative. Our results indicate that such costs may not be symmetric. In other words, the costs appear to be diferent when reviewer experience is positive versus negative. Such a characterization is reminiscent of the Prospect theory (Kahneman and Tversky 1979).

Overall, our findings indicate that although the monetary incentive program can induce more reviewers to contribute to the platform and that the total number of reviews increases, it appears to create a bias of a diferent kind. First, reviews are more concentrated toward highly rated products compared with reviews posted before monetary incentives. Second, reviewers significantly deviate from previous star ratings in a positive manner for products with low and medium ratings, while deviating negatively for highly rated products (note, however, that the magnitude of this deviation is very small). As a result, the platform sees an influx of reviews with 4 and 5 star ratings, while reviews with 1 and 2 star ratings almost disappear. In other words, the distribution of star ratings appears to shift from bimodal to unimodal as seen in Figure 4. On a related point, it also appears that monetary incentives indeed interact with reviewers’ intrinsic motivation and that the incentives do not simply reduce the cost of writing reviews.

Table 12. Change in the Star Rating

<table><tr><td>Range of ex ante average star ratings</td><td>Average change of the given star ratings from the ex ante average</td><td>Number of observations</td></tr><tr><td>[1,2)</td><td>3.3333*** (0.3333)</td><td>12</td></tr><tr><td>[2,3)</td><td>0.7524*** (0.1957)</td><td>33</td></tr><tr><td>[3,4)</td><td>0.5135*** (0.0442)</td><td>397</td></tr><tr><td>[4,5]</td><td>-0.0435*** (0.0122)</td><td>2,847</td></tr></table>

p < 0.1; p < 0.05; p < 0.01.

Figure 4. The Distribution of Star Ratings in the Treated Platform Before and After Monetary Incentives  
![](/api/attachments/YC8QJGMC/fulltext/images/85bd526019ade1ec29c68ddb997b93c574cd7907facbb181dcdef357b680abd1.jpg)

To recap, we presented analyses using several measures to test our hypotheses in Section 5. Table 13 summarizes our hypotheses, measures, and results. Overall, we find that monetary incentives decrease review quality while review valence becomes more positive. For existing reviewers, the incentives reduce their level of participation while the quality of participation does not significantly change. Last, the platform enjoys an increase in the number of new reviewers who register and contribute to the review platform. However, reviews after monetary incentives are concentrated much more toward highly rated products.

As mentioned at the beginning of this section, one of the underlying assumptions in a DID analysis is that treatment and control groups should follow the similar pre-treatment trend. To investigate whether this assumption holds in our analyses, we use the ADF test of stationarity between the two pre-treatment data sets of treated and control platforms. Here, we invoke the stationarity definition, which states that for stationary time-series data, the underlying data generation process has a constant mean and variance over time. To operationalize this test for the measures used in our DID analyses, we calculated the diferences in the value of the measures between the treated and control platforms on a semimonthly basis. Then, we performed the ADF test to check for the stationarity of these diferences. The ADF test of all parameters rejects the null hypothesis of a unit root, indicating that the diferences between the two platforms are stationary. Table 14 reports the results of the ADF tests.

![](/api/attachments/YC8QJGMC/fulltext/images/45703c13802817719a2e2c87b0d0296daeb1b1283e08dbf2b6e6ce41ad1673ec.jpg)

Last, throughout the paper, we mentioned several analyses that were conducted based on alternative specifications to ensure the robustness of our results. Table 15 summarizes the robustness tests conducted in the paper. The results of the tests are qualitatively similar to our main results. Details of these tests are provided in Online Appendix D.

## 6. Conclusion

Many review platforms provide monetary incentives to attract reviewers. These incentives are provided to help reviewers overcome the cost of writing reviews, and thereby aid the platforms in obtaining reviews that are more representative of the diverse experiences of the user population. However, extrinsic rewards may have unintended consequences in a context where intrinsic motivation is paramount. Such issues could negatively afect the platforms and exacerbate existing biases. We studied this problem by taking advantage of a naturally occurring experiment. We also obtained data on another platform with no monetary incentives to serve as the control group. We focused on the reviews of experience goods and used video games review data in our analysis.<sup>8</sup>

Table 13. Summary of Results of the Hypothesis Tests

<table><tr><td>Hypothesis</td><td>Hypothesized characteristics</td><td>Measures</td><td>Results</td></tr><tr><td>1</td><td>Review quality</td><td>Length of reviewsReview helpfulness scoreReadability score (Gunning-Fog index)Frequency of feature-related discussions</td><td>H1A supportedH1B not supported</td></tr><tr><td>2</td><td>Review valence</td><td>Average star ratingsPercentage of positive wordsPercentage of negative words</td><td>H2A supportedH2B not supported</td></tr><tr><td>3</td><td>Existing reviewer behavior</td><td>Number of reviewsLength of reviewsReview helpfulness score</td><td>H3 partially supported</td></tr><tr><td>4</td><td>Number of new reviewers</td><td>Number of new reviewers</td><td>H4A supportedH4B not supported</td></tr><tr><td>5</td><td>Bias in selecting product to write review</td><td>Gini coefficientNumber of reviews posted based on ex ante star ratings</td><td>H5 supported</td></tr></table>

Table 14. Results of the Augmented Dickey–Fuller Test of Stationarity

<table><tr><td></td><td>Z(t) from Augmented Dickey-Fuller test</td></tr><tr><td>Total number of reviews</td><td>-10.710***</td></tr><tr><td>Average content word count</td><td>-5.051***</td></tr><tr><td>Average title word count</td><td>-1.788*</td></tr><tr><td>Average star ratings</td><td>-4.190**</td></tr><tr><td>Gunning-Fog index</td><td>-5.392***</td></tr><tr><td>Percentage of positive word count</td><td>-4.076**</td></tr><tr><td>Percentage of negative word count</td><td>-2.795**</td></tr><tr><td>Percentage of topic 1</td><td>-3.480**</td></tr></table>

<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Through our analysis, we find that by paying reviewers to write reviews, the review platform enjoys more participation at the cost of inflated star ratings and lower quality reviews. As review platforms are likely concerned about the quality of their reviews, using monetary incentives, at least the way they are commonly designed, might not align with that objective. We also evaluated the efect of incentives on the behavior of the existing reviewers. We find that monetary incentives result in a decrease in their level of participation, but the quality of participation does not significantly change. This finding is particularly important as it highlights the diference in behavior of two groups of users (i.e., existing reviewers and new reviewers). Last, we find that as a result of the monetary incentives, reviewers’ bias in selecting products is aggravated and reviews are even more concentrated toward products that are already highly rated. Our analyses appear to indicate that the traditionally used “brag-and-moan” model for consumer behavior should be revisited to account for the asymmetric cost of writing reviews based on the current star ratings of the products.

Our paper contributes to the existing body of knowledge on the efect of incentives on the review generation process. For example, we empirically demonstrate that while monetary incentives make intrinsicallymotivated reviewers contribute less often, there is no significant efect on the quality of their contributions. We also find that concentration bias in selecting products to review increases after monetary incentives. These findings are particularly important given that many companies are pursuing similar incentive models. Our findings could also be used to draw insights on similar incentive designs for other related contexts such as crowdsourcing platforms. However, our analysis is not without limitations. For example, we consider only the reward structure that pays reviewers based on the number of reviews written, which is the design commonly adopted by review platforms. A diferent reward structure may generate a diferent outcome: If the rewards are based on the length or popularity of the reviews, the results may be diferent. Studying such alternative mechanism designs is an interesting avenue for future research. Particularly, field experiments or laboratory experiments could be used to investigate other mechanism designs. Another avenue for future research is to study the direct efect of incentives on sales. Also, as prior literature has demonstrated the differences between online reviews of search goods and experience goods, another future research avenue could be to explore whether the efect of monetary incentives is similar for the reviews of search goods.

Table 15. List of Our Robustness Tests

<table><tr><td>Section</td><td>Description</td></tr><tr><td>5.1.1</td><td>Our main analysis is based on reviews of products released before the beginning of the time window of our study. As a robustness test, we include all products in the data set.</td></tr><tr><td>5.1.1</td><td>Our main analysis is based on the data from January to July 2013. Here, we perform the analysis using data from February to June 2013 instead.</td></tr><tr><td>5.1.2</td><td>Similar to the first robustness test, the analysis of the review helpfulness score is based on reviews of products released before the start of our analysis period. As a robustness test, we include reviews of products released afterward.</td></tr><tr><td>5.1.3</td><td>In the analysis of the topic modeling, we set up a difference-in-differences regression model where the dependent variable is the probability that a review is related to the product feature. To test the robustness of our finding, we constructed Bayesian credible intervals using the Gibbs draws instead.</td></tr><tr><td>5.2.1</td><td>In our analysis of existing reviewer behavior, we defined an “existing reviewer” as a reviewer who wrote at least one review on the treated platform during the four-month period before the introduction of monetary incentives. For robustness check, we considered reviewers who wrote at least once in the eight-month and 12-month period before monetary incentives.</td></tr><tr><td>5.2.1</td><td>In our analysis of existing reviewer behavior, the unit of time for our analysis is semimonthly. Here, we redefine each time period to be a month.</td></tr><tr><td>5.2.2</td><td>The analysis of the number of new reviewers is based on the Autoregressive-Moving-Average (ARMA) model. To ensure the robustness of the finding, we use a Vector Autoregression (VAR) model and an Autoregressive-Moving-Average model with exogenous inputs (ARMAX) that include the number of new products as a time-varying factor.</td></tr><tr><td>5.2.2</td><td>As mentioned above, the analysis of the number of new reviewers is based on the ARMA model. In another robustness test, we also conducted a difference-in-differences analysis using the number of reviewers on Amazon as a control platform.</td></tr></table>

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their constructive comments throughout the review process. The authors also thank participants at the 2014 Big Ten Information Systems Research Symposium, the ICIS Doctoral Consortium 2015, and participants in research seminars at the University of Illinois Urbana–Champaign, Indiana University, University of Texas at Austin, and Texas A&M University for their helpful feedback and discussions.

## Endnotes

<sup>1</sup> Some efort has been made to curb incentives for reviews from the product manufacturer or service provider. For instance, the Ofice of Fair Trading, which is the United Kingdom consumer protection agency, has issued an oficial statement against the use of monetary incentives. The statement emerged from an incident involving a highend English hotel, “The Cove,” which was ofering a future discount to guests who posted a review on TripAdvisor. We acknowledge that the policy might be aimed at the quid pro quo arrangement between the hotel and the guests.

<sup>2</sup> At the time the incentive program was introduced, there were avenues other than posting reviews to earn loyalty points. For example, users could visit any of the treated platform’s physical stores in the United States and check in using its smartphone app to receive 10 points. In addition, users could participate in the platform’s social polls, which were a part of its Facebook application, and receive 10 points for each answer.

<sup>3</sup> Amazon has a program called Vine in which top reviewers receive products from the sellers so that they can be among the first to write reviews of those products. None of the reviews in our data set was written as a part of the Vine program.

<sup>4</sup> The information about the tool is available at http://www.wjh .harvard.edu/<sup>\~</sup>inquirer/.

<sup>5</sup> Details of topic modeling estimation and results are available from the authors on request.

<sup>6</sup> Because the number of reviews can be 0, we use log(1 <sup>+</sup> number of reviews).

<sup>7</sup> One may argue that our observation is because existing reviewers may be creating new accounts to write reviews to obtain more rewards given the restriction of rewards for a maximum of 8 reviews per year. We evaluated the number of reviews each existing reviewer submitted after the incentive program, and found that none of the 1,071 existing reviewers reached that limit.

<sup>8</sup> To investigate the generalizability of our findings, we also analyzed reviews of another category of experience goods, movie DVDs, and confirmed that the primary results are qualitatively similar.

## References

Anderson M, Magruder J (2012) Learning from the crowd: Regression discontinuity estimates of the efects of an online review database. Econom. J. 122(563):957–989.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Arun R, Suresh V, Madhavan CV, Murthy MN (2010) On finding the natural number of topics with latent Dirichlet allocation: Some observations. Zaki MJ, Yu JX, Ravindran B, Pudi V, eds. Advances in Knowledge Discovery and Data Mining, Lecture Notes Artificial Intelligence, Vol. 6118 (Springer, Berlin), 391–402.

Baker WE, Bulkley N (2014) Paying it forward vs. rewarding reputation: Mechanisms of generalized reciprocity. Organ. Sci. 25(5): 1493–1510.

Bansal HS, Voyer PA (2000) Word-of-mouth processes within a services purchase decision context. J. Service Res. 3(2):166–177.

Bénabou R, Tirole J (2006) Incentives and prosocial behavior. Amer. Econom. Rev. 96(5):1652–1678.

Blei DM (2012) Probabilistic topic models. Comm. ACM 55(4):77–84.

Blumenstock JE (2008) Size matters: Word count as a measure of quality on Wikipedia. Proc. 17th Internat. Conf. World Wide Web (ACM, New York), 1095–1096.

Bolton GE, Katok E, Ockenfels A (2004) How efective are electronic reputation mechanisms? An experimental investigation. Management Sci. 50(11):1587–1602.

Brynjolfsson E, Hu Y, Simester D (2011) Goodbye pareto principle, hello long tail: The efect of search costs on the concentration of product sales. Management Sci. 57(8):1373–1386.

Cao J, Xia T, Li J, Zhang Y, Tang S (2009) A density-based method for adaptive LDA model selection. Neurocomputing 72(7):1775–1781.

Chan J, Ghose A (2013) Internets dirty secret: Assessing the impact of online intermediaries on HIV transmission. MIS Quart. 38(4):955–976.

Cheema A, Kaikati AM (2010) The efect of need for uniqueness on word of mouth. J. Marketing Res. 47(3):553–563.

Chen P-Y, Dhanasobhon S, Smith MD (2008) All reviews are not created equal: The disaggregate impact of reviews and reviewers at amazon.com. Working paper, Arizona State University, Tempe, http://ssrn.com/abstract<sup></sup>918083.

Chen Y, Xie J (2005) Third-party product review and firm marketing strategy. Marketing Sci. 24(2):218–240.

Chen Y, Ho T-H, Kim Y-M (2010b) Knowledge market design: A field experiment at Google answers. J. Public Econom. Theory 12(4):641–664.

Chen Y, Harper FM, Konstan J, Li XS (2010a) Social comparisons and contributions to online communities: A field experiment on Movielens. Amer. Econom. Rev. 100(4):1358–1398.

Chevalier JA, Mayzlin D (2006) The efect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Gopinath S, Venkataraman S (2010) The efects of online user reviews on movie box ofice performance: Accounting for sequential rollout and aggregation across local markets. Marketing Sci. 29(5):944–957.

Deci EL, Koestner R, Ryan RM (1999) A meta-analytic review of experiments examining the efects of extrinsic rewards on intrinsic motivation. Psych. Bull. 125(6):627–668.

Dellarocas C, Narayan R (2006) A statistical measure of a populations propensity to engage in post-purchase online word-of-mouth. Statist. Sci. 21(2):277–285.

Dellarocas C, Gao G, Narayan R (2010) Are consumers more likely to contribute online reviews for hit or niche products? J. Management Inform. Systems 27(2):127–158.

Deveaud R, SanJuan E, Bellot P (2014) Accurate and efective latent concept modeling for ad hoc information retrieval. Document numérique 17(1):61–84.

Dunning T (2012) Natural Experiments in the Social Sciences: A Design-Based Approach (Cambridge University Press, Cambridge, UK).

Eisend M (2006) Two-sided advertising: A meta-analysis. Internat. J. Res. Marketing 23(2):187–198.

Erat S, Gneezy U (2012) White lies. Management Sci. 58(4):723–733.

Gao GG, Greenwood BN, Agarwal R, Jefrey S (2015) Vocal minority and silent majority: How do online ratings reflect population perceptions of quality? MIS Quart. 39(3):565–589.

Gastwirth JL (1971) A general definition of the Lorenz curve. Econometrica 39(6):1037–1039.

Ghose A, Ipeirotis PG (2006) Designing ranking systems for consumer reviews: The impact of review subjectivity on product sales and review quality. Proc. 16th Annual Workshop Inform. Tech. Systems (ACM, New York), 303–310.

Ghose A, Ipeirotis PG (2011) Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Trans. Knowledge Data Engrg. 23(10): 1498–1512.

Gneezy U, Meier S, Rey-Biel P (2011) When and why incentives (don’t) work to modify behavior. J. Econom. Perspect. 25(4): 191–209.

Godes D, Silva J (2012) Sequential and temporal dynamics of online opinion. Marketing Sci. 31(3):448–473.

Goes PB, Lin M, Au Yeung C-M (2014) Popularity efect in usergenerated content: Evidence from online product reviews. Inform. Systems Res. 25(2):222–238.

Good PI (2005) Permutation, Parametric, and Bootstrap Tests of Hypotheses (Springer, New York).

Greiner B, Levati MV (2005) Indirect reciprocity in cyclical networks: An experimental study. J. Econom. Psych. 26(5):711–731.

Grewal R, Cline TW, Davies A (2003) Early-entrant advantage, wordof-mouth communication, brand similarity, and the consumer decision-making process. J. Consumer Psych. 13(3):187–197.

Grifiths TL, Steyvers M (2004) Finding scientific topics. Proc. Natl. Acad. Sci. 101 (suppl 1):5228–5235.

Grün B, Hornik K (2011) Topicmodels: An r package for fitting topic models. J. Statist. Software 40(13):1–30.

Gunning R (1969) The fog index after twenty years. J. Bus. Comm. 6(2):3–13.

Hennig-Thurau T, Gwinner KP, Walsh G, Gremler DD (2004) Electronic word-of-mouth via consumer-opinion platforms: What motivates consumers to articulate themselves on the Internet? J. Interactive Marketing 18(1):38–52.

Hosanagar K, Fleder D, Lee D, Buja A (2013) Will the global village fracture into tribes? Recommender systems and their efects on consumer fragmentation. Management Sci. 60(4):805–823.

Hsieh G, Kraut RE, Hudson SE (2010) Why pay?: Exploring how financial incentives are used for question and answer. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 305–314.

Hu N, Pavlou PA, Zhang J (2006) Can online reviews reveal a product’s true quality?: Empirical findings and analytical modeling of online word-of-mouth communication. Proc. 7th ACM Conf. Electronic Commerce (ACM, New York), 324–330.

Hu N, Zhang J, Pavlou PA (2009) Overcoming the j-shaped distribution of product reviews. Comm. ACM 52(10):144–147.

Huang Y, Singh PV, Ghose A (2015) A structural model of employee behavioral dynamics in enterprise social media. Management Sci. 61(12):2825–2844.

Jiang LC, Bazarova NN, Hancock JT (2013) From perception to behavior: Disclosure reciprocity and the intensification of intimacy in computer-mediated communication. Comm. Res. 40(1):125–143.

Kahneman D, Tversky A (1979) Prospect theory: An analysis of decision under risk. Econometrica 47(2):263–291.

Kohn A (1999) Punished by Rewards: The Trouble with Gold Stars, Incentive Plans, A’s, Praise, and Other Bribes (Houghton Miflin, Boston).

Korfiatis N, Rodríguez D, Sicilia M-A (2008) The impact of readability on the usefulness of online product reviews: A case study on an online bookstore. Lytras MD, Carroll JM, Damiani E, Tennyson RD, eds. Emerging Technologies and Information Systems for the Knowledge Society, WSKS 2008, Lecture Notes Comput. Sci., Vol. 5288 (Springer, Berlin Heidelberg), 423–432.

Kreps DM (1997) Intrinsic motivation and extrinsic incentives. Amer. Econom. Rev. 87(2):359–364.

Kuran T, Sunstein CR (1999) Availability cascades and risk regulation. Stanford Law Rev. 51(4):683–768.

Lappas T, Sabnis G, Valkanas G (2016) The impact of fake reviews on online visibility: A vulnerability assessment of the hotel industry. Inform. Systems Res. 27(4):940–961.

Lee D, Hosanagar K (2014) Impact of recommender systems on sales volume and diversity. Internat. Conf. Inform. Systems 2014 (AIS, Atlanta, GA).

Lee Y-J, Hosanagar K, Tan Y (2015) Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Sci. 61(9):2241–2258.

Li H, Zhang Z, Janakiraman R, Meng F (2016) How review sentiment and readability afect online peer evaluation votes?—An examination combining reviewers social identity and social network. ttra Annual Internat. Conf. Proc. 2016.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Li Z, Huang K-W, Cavusoglu H (2012) Quantifying the impact of badges on user engagement in online Q&A communities. Internat. Conf. Inform. Systems 2012 (TTRA, Whitehall, MI).

Liu TX, Yang J, Adamic LA, Chen Y (2014) Crowdsourcing with all-pay auctions: A field experiment on taskcn. Management Sci. 60(8):2020–2037.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box ofice revenue. J. Marketing 70(3):74–89.

Loughran T, McDonald B (2011) When is a liability not a liability? Textual analysis, dictionaries, and 10-ks. J. Finance 66(1):35–65.

Lu Y, Jerath K, Singh PV (2013) The emergence of opinion leaders in a networked online community: A dyadic model with time dynamics and a heuristic for fast estimation. Management Sci. 59(8):1783–1799.

Luca M (2011) Reviews, reputation, and revenue: The case of Yelp.com. Working paper, Harvard Business School, https:// www.hbs.edu/faculty/Pages/item.aspx?num<sup></sup>41233.

Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Sci. 62(12):3412–3427.

Marlin B, Zemel RS, Roweis S, Slaney M (2007) Collaborative filtering and the missing at random assumption. 23rd Conf. Uncertainty Artificial Intelligence (AUAI Press, Arlington, VA), 267–275.

Marlin BM, Zemel RS (2009) Collaborative prediction and ranking with non-random missing data. Proc. Third ACM Conf. Recommender Systems (ACM, New York), 5–12.

May RM (1987) More evolution of cooperation. Nature 327(6117): 15–17.

Mayzlin D, Dover Y, Chevalier J (2014) Promotional reviews: An empirical investigation of online review manipulation. Amer. Econom. Rev. 104(8):2421–2455.

McQueeney R (2016) Can Amazon (AMZN) fix its incentivized reviews problem? Accessed March 20, 2017, http://finance .yahoo.com/news/amazon-amzn-fix-incentivized-reviews-165804949 .html.

Mellström C, Johannesson M (2008) Crowding out in blood donation: Was Titmuss right? J. Eur. Econom. Assoc. 6(4):845–863.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Moe WW, Trusov M (2011) The value of social dynamics in online product ratings forums. J. Marketing Res. 48(3):444–456.

Mudambi SM, Schuf D (2010) What makes a helpful online review? A study of customer reviews on Amazon.com. MIS Quart. 34(1):185–200.

Nair H (2007) Intertemporal price discrimination with forwardlooking consumers: Application to the U.S. market for console video-games. Quant. Marketing Econom. 5(3):239–292.

Nelson P (1970) Information and consumer behavior. J. Political Econom. 78(2):311–329.

Nowak MA, Roch S (2007) Upstream reciprocity and the evolution of gratitude. Proc. Roy. Soc. B: Biol. Sci. 274(1610):605–610.

Pan Y, Zhang JQ (2011) Born unequal: A study of the helpfulness of user-generated product reviews. J. Retailing 87(4):598–612.

Park D-H, Kim S (2009) The efects of consumer knowledge on message processing of electronic word-of-mouth via online consumer reviews. Electronic Commerce Res. Appl. 7(4):399–410.

Pavlou PA, Dimoka A (2006) The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller diferentiation. Inform. Systems Res. 17(4):392–414.

Rishika R, Kumar A, Janakiraman R, Bezawada R (2013) The efect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Inform. Systems Res. 24(1):108–127.

Rosario AB, Sotgiu F, De Valck K, Bĳmolt TH (2016) The efect of electronic word of mouth on sales: A meta-analytic review of platform, product, and metric factors. J. Marketing Res. 53(3): 297–318.

Schlosser AE (2011) Can including pros and cons increase the helpfulness and persuasiveness of online reviews? The interactive efects of ratings and arguments. J. Consumer Psych. 21(3): 226–239.

Shen W, Hu YJ, Rees J (2015) Competing for attention: An empirical study of online reviewers strategic behaviors. MIS Quart. 39(3):683–696.

Shi Z, Lee GM, Whinston AB (2015) Towards a better measure of business proximity: Topic modeling for industry intelligence. MIS Quart. 40(4):1035–1056.

Singh PV, Sahoo N, Mukhopadhyay T (2014) How to attract and retain readers in enterprise blogging? Inform. Systems Res. 25(1): 35–52.

Smith MD, Telang R (2009) Competing with free: The impact of movie broadcasts on DVD sales and Internet piracy 1. MIS Quart. 33(2):321–338.

Stephen AT, Yakov B, Du Plessis C, Goncalves D (2012) Does paying for online product reviews pay of? The efects of monetary incentives on consumers product evaluations. Working paper, INSEAD, Fontainebleau, France.

Tetlock PC, Saar-Tsechansky M, Macskassy S (2008) More than words: Quantifying language to measure firms’ fundamentals. J. Finance 63(3):1437–1467.

Tirole J (1988) The Theory of Industrial Organization (MIT Press, Cambridge, MA).

Titmuss RM (1970) The Gift Relationship (New Press, New York).

Wang J, Ghose A, Ipeirotis P (2012) Bonus, disclosure, and choice: What motivates the creation of high-quality paid reviews? Internat. Conf. Inform. Systems 2012 (AIS, Atlanta, GA).

Wood AM, Brown GD, Maltby J (2011) Thanks, but I’m used to better: A relative rank model of gratitude. Emotion 11(1):175–180.

Wooldridge JM (2010) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA).

Yin D, Mitra S, Zhang H (2016) Research note: When do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth. Inform. Systems Res. 27(1):131–144.

Yoo KH, Gretzel U (2009) Comparison of deceptive and truthful travel reviews. Höpken W, Gretzel U, Law R, eds. Information and Communication Technologies in Tourism 2009 (Springer, Vienna), 37–47.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
