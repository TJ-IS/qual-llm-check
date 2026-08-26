---
otero_id: 16260
otero_key: "R5EMZVUN"
title: "Temporal Effects of Repeated Recognition and Lack of Recognition on Online Community Contributions"
authors: "Samadrita Bhattacharyya; Shankhadeep Banerjee; Indranil Bose; Atreyi Kankanhalli"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2020.1759341"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Temporal Effects of Repeated Recognition and Lack of Recognition on Online Community Contributions

Samadrita Bhattacharyya , Shankhadeep Banerjee , Indranil Bose & Atreyi Kankanhalli

To cite this article: Samadrita Bhattacharyya , Shankhadeep Banerjee , Indranil Bose & Atreyi Kankanhalli (2020) Temporal Effects of Repeated Recognition and Lack of Recognition on Online Community Contributions, Journal of Management Information Systems, 37:2, 536-562, DOI: 10.1080/07421222.2020.1759341

To link to this article: https://doi.org/10.1080/07421222.2020.1759341

![](/api/attachments/R5EMZVUN/fulltext/images/2327dd10cbb041a82d7fe06e654d7832fc1824f872bae60dea1ff147afc0f133.jpg)

View supplementary material

![](/api/attachments/R5EMZVUN/fulltext/images/f4c90dec07c20e142d31cbb2edde56fd86a9338b6b89aed05b1197bc26cc63a2.jpg)

Published online: 16 Jun 2020.

![](/api/attachments/R5EMZVUN/fulltext/images/dc4c31729ded50e1d9a06088e9ba2bb5c0700bc96e11bdeccee3b512386b8590.jpg)

Submit your article to this journal

![](/api/attachments/R5EMZVUN/fulltext/images/6dcc11a4978863f3e09ca05b4c5410cb54de11501cbe20b3ca9553d3e59078e5.jpg)

Article views: 19

![](/api/attachments/R5EMZVUN/fulltext/images/664fc6bcde911c8e63ef4722b3fc474e2e851132b471f71133ff1d6995a426ea.jpg)

View related articles

![](/api/attachments/R5EMZVUN/fulltext/images/7a466a9e5cca2fbb0b7db7a4aceb45b365c01afed8bd791eb54b91a9c77bf309.jpg)

View Crossmark data

Check for updates

# Temporal E<sup>f</sup>ects of Repeated Recognition and Lack of Recognition on Online Community Contributions

Samadrita Bhattacharyya<sup>a</sup>, Shankhadeep Banerjee<sup>a</sup>, Indranil Bose<sup>a</sup>, and Atreyi Kankanhalli<sup>b</sup>

<sup>a</sup>Management Information Systems, Indian Institute of Management Calcutta, Joka, Kolkata, India; <sup>b</sup>Department of Information Systems and Analytics, National University of Singapore, Singapore

## ABSTRACT

A reason for online communities to confer recognition (e.g., badges) on members is to acknowledge and encourage contributions. Yet, it is unclear whether such recognition or lack of it changes members’ contribution behaviors over time. While anticipated recognition has been found to motivate members’ contributions, past <sup>fi</sup>ndings are limited regarding members’ post-recognition behaviors. Especially, the impact of multiple recognitions over time remains unexplored. Also, the contribution behavior of deserving, yet unrecognized members lacks investigation, which can help uncover the negative side e<sup>f</sup>ects of recognition systems. Motivated by these gaps in understanding, we build on reinforcement theory to propose a positive role of <sup>fi</sup>rsttime recognition as a social reinforcer of contribution behavior, while repeated recognition is hypothesized to su<sup>f</sup>er from reinforcer satiation. However, for deserving, yet unrecognized members we propose a decrease in contributions due to recognition inequity. Using quasiexperiments on 81,393 reviewers of one of the largest online business review sites, Yelp.com, we <sup>fi</sup>nd empirical support for our hypotheses, with contribution e<sup>f</sup>ort and quantity as outcomes. Additional analysis with contribution quality as outcome shows di<sup>f</sup>ering relationships for repeatedly recognized versus deserving, unrecognized members. Other than its research contributions, this study provides practical insights for designing e<sup>f</sup>ective recognition systems for online communities.

## KEYWORDS

Online communities; online reviews; online contributions; community contribution; community recognition; quasiexperiment; reinforcement theory; reinforcer satiation; recognition inequity; temporal e<sup>f</sup>ects

## Introduction

Online communities for sharing customer reviews of businesses, products, and services have become sought-after destinations for consumers seeking information to make purchase decisions and choices. For instance, Yelp — a popular online community site for sharing local business (e.g., restaurant) reviews — contained 184 million reviews as of March 2019, with 167 million average monthly unique consumers across devices.<sup>1</sup>

Online reviews act as an in<sup>fl</sup>uential source of information for consumers’ decisionmaking, with 78% of consumers reported as trusting online reviews as much as personal recommendations.<sup>2</sup> However, online review sites <sup>fi</sup>nd it challenging to sustain contributions of reviews over time, given the voluntary nature of contribution [8]. Thus, online reviews are typically under-provisioned. To address this issue, most online community sites aim to incentivize contributors through monetary rewards (e.g., money, gift coupons) or recognition (e.g., badges, ranks) [38], where recognition refers to the public appreciation of individuals’ e<sup>f</sup>orts through non-monetary rewards [7, 52]. Particularly, recognition is widely employed to encourage member contribution since it is less costly to provide than monetary rewards, and is considered a signi<sup>fi</sup>cant motivator for online contributions [45, 77]. For example, travel review site TripAdvisor provides various levels of badges (starting from “New Reviewer” to “Top Contributor”), and business review site Yelp provides the “Elite” badge to recognize reviewers who are role models in terms of their contributions. Yet, there is limited understanding of the e<sup>f</sup>ectiveness of recognition in promoting review contributions, which is a critical question for review site managers as well as researchers in this area.

In this regard, early surveys of individuals’ contribution motivations reported that contribution of reviews or word-of-mouth is driven by intrinsic factors, such as altruism and self-enhancement [72], as well as rewards and recognition [35]. Other than these self-reported surveys, which may su<sup>f</sup>er from bias, a number of studies have used experiments to examine the e<sup>fi</sup>cacy of monetary rewards for stimulating online review contribution [10, 25, 42, 70]. Prior research has also assessed the e<sup>f</sup>ectiveness of other ways to stimulate review contributions, such as using social norms [8] or appeals for altruism [62]. However, despite the prevalence of research on the impact of recognition in other online communities (e.g., [23, 26, 45, 49]), there are limited studies (e.g., [65, 66]) examining the impact of recognition on contribution behavior in online review communities. Our literature review (see the next section for the full review) uncovered two key gaps in our understanding of the e<sup>f</sup>ects of recognition on contributing online reviews. First, prior research has primarily investigated the impact of one-time recognition and looked at its short-term e<sup>f</sup>ects (e.g., [65]). However, in reality, members may contribute to a community for several years and may receive multiple recognitions at di<sup>f</sup>erent points of time in their tenure. Thus, it is valuable to examine the changes in contribution behavior not just for <sup>fi</sup>rst-time recognition, but also for multiple recognitions across time. Second, prior literature has focused on the contribution behavior of members who were recognized but shows a lack of study of those who do not receive recognition even if they made substantial contributions to the community. Such occurrences can potentially inhibit contributions and harm the community in the long run. Thus, it is important to understand the contribution behavior of deserving yet unrecognized members. Hence, the objective of this paper is to investigate the temporal e<sup>f</sup>ects of <sup>fi</sup>rst-time recognition, repeated recognition, and lack of recognition on contribution behavior in online review communities.

To address our research objective, we use reinforcement theory [63] as our overarching theoretical lens to propose a positive e<sup>f</sup>ect of <sup>fi</sup>rst-time recognition on contribution behavior, and the concept of satiation in reinforcement [29] to hypothesize a decline in contribution behavior for members who receive repeated recognition. We also propose a decline in contribution for the deserving yet unrecognized community members based on the concept of inequity [1] in recognition. We used quasi-experiments [11] on 81,393 reviewers’ data collected from Yelp.com, one of the largest local business review communities with an annual Elite recognition system, to show empirical support for our hypotheses, with contribution e<sup>f</sup>ort and quantity as outcomes.

Our results show a signi<sup>fi</sup>cant increase in both contribution e<sup>f</sup>ort and quantity for <sup>fi</sup>rsttime recognized reviewers, followed by a declining trend in both outcomes on repeated reception of the Elite badge in subsequent years. For the deserving yet unrecognized reviewers, we observed reductions in contribution e<sup>f</sup>ort and quantity. In terms of research contributions, this study presents a novel attempt at utilizing reinforcement and equity theories and related concepts to holistically explain the contribution behavior of both recognized and unrecognized deserving members over multiple periods of recognition. It also advances the online review and online community literature by explicating the temporal e<sup>f</sup>ects of multiple recognitions on the contribution behaviors of recognized and unrecognized members. In terms of practical implications, the insights from our <sup>fi</sup>ndings can be of value to designers and managers of online review communities. This underlines the need for careful design and implementation of recognition systems to account for the e<sup>f</sup>ects on recognized as well as deserving unrecognized members over time.

## Prior Research on the Impact of Recognition on Online Contributions

Our review reveals a number of studies on the relationship between monetary rewards and/or recognition with member contribution in online communities (e.g., [13, 14, 37, 40, 41, 44, 49, 73]), including online review communities (e.g., [35, 65, 71]). A summary of relevant literature is presented in Table 1. A signi<sup>fi</sup>cant portion of this literature has focused on examining the drivers of members’ participation or contribution, including anticipated rewards and recognition. Expectation of rewards and recognition was found to be a key predictor of member participation in various online communities [13, 37, 58, 73]. Recognition is sought in order to ful<sup>fi</sup>ll members’ need to signal expertise and gain social status or reputation in online communities [35, 45]. Accordingly, community members increased content sharing on websites [40, 49] in order to gain recognition. Thus, this literature has predominantly concentrated on the “pre-recognition” phase and found that the expectation of recognition enhances contribution behavior.

Comparatively, there has been much less research investigating members’ contribution behavior in the “post-recognition” phase. Here, some studies reported that members’ recognition resulted in improved contribution outcomes [33, 46]. However, a few studies found mixed e<sup>f</sup>ects on members’ contribution, for example, positive impact on contribution quantity, but negative impact on quality [65], positive impact on quality but not on quantity [78], positive impact on quantity for users with low or medium level of motivation, but no e<sup>f</sup>ect for users in high motivation state [16], and negative e<sup>f</sup>ect on contribution e<sup>f</sup>ort [32]. Furthermore, several studies were mainly empirical in nature [28, 33, 46] (largely atheoretical), and some had methodological limitations, for example, used hypothetical manipulations and survey measures for outcomes [28] or correlation analysis [65]. Overall, the e<sup>f</sup>ect of receiving recognition in online communities is an important but understudied area and requires delving deeper into the post-recognition phenomenon. Speci<sup>fi</sup>cally, we identi<sup>fi</sup>ed two key gaps in this area.

First, there is limited research on the temporal changes in members’ contribution behavior under the in<sup>fl</sup>uence of multiple recognitions, a more realistic situation than onetime recognition. Temporal changes in users’ motives (e.g., fun motives) and their e<sup>f</sup>ects on users’ contribution behavior (e.g., editing activities on Wikipedia) have been examined in prior studies (e.g., [6]). However, the temporal changes in contribution behavior due to multiple recognitions have rarely been investigated. Mostly, prior studies employed

Table 1. Summary of related literature on relationship between recognition and contribution behavior in online communities.

experiments [28, 33], quasi-experiments [46], or other designs (e.g., regression discontinuity and di<sup>f</sup>erence-in-di<sup>f</sup>erence [78] and simple correlations [65] to examine the onetime e<sup>f</sup>ects of badges or other reputation indicators). In the rare case of studying the e<sup>f</sup>ects of multiple recognitions [26], the changes over time in contribution behavior (e.g., quantity, e<sup>f</sup>ort, or quality) were not examined, but the member’s retention rate was measured instead. Based on reinforcement literature [53], the impact of receiving recognition for the <sup>fi</sup>rst-time should di<sup>f</sup>er from that of multiple receptions, but this has not been theorized and tested empirically. Our study aims to advance research in this area by examining temporal changes in members’ contribution behavior under the in<sup>fl</sup>uence of repeated recognition in online review communities.

Second, prior research is lacking in another important aspect of employing recognition systems in online review communities (i.e., possible demotivation of members who did not receive recognition despite having made signi<sup>fi</sup>cant contributions). Such occurrences can hurt the community in the long term by potentially inhibiting contributions. We aim to address this gap by identifying and comparing samples of recognized versus deserving yet unrecognized members to understand how their contribution behaviors vary over time for multiple recognitions or their lack thereof.

## Conceptual Background

In this section, we explicate the theoretical foundations of our study. Speci<sup>fi</sup>cally, we build on reinforcement theory [67] as our overarching theoretical lens, as recognition is considered as a social reinforcer, similar to approval and praise [63, 69]. Within this theory, we draw on the concept of reinforcer satiation to explain the e<sup>f</sup>ect of repeated recognition. We complement this using equity theory [1] to explain the behavior of deserving yet unrecognized members.

## Reinforcement Theory, Social Reinforcers, and Reinforcer Satiation

Reinforcement theory, a popular theory of motivation, provides guidelines to control and modify human behavior [63]. Historically rooted in the concept of operant conditioning [67], reinforcement theory has been applied to management practices for decades [51]. The central tenet of the theory is that human behavior is a function of its contingent consequences [63, 69]. Positive or desirable consequences strengthen the behavior and increase its subsequent frequency, whereas negative or undesirable consequences dissuade the behavior and decrease its frequency of occurrence [69]. Stimuli that are applied to increase desired behavior are known as positive reinforcers (e.g., money, praise, promotion), while dissuading stimuli are referred to as negative reinforcers (e.g., penalty, criticism) [63].

Stajkovic and Luthans [69] identify three types of positive reinforcers that can in<sup>fl</sup>uence individuals’ behavior, that is, monetary rewards (e.g., salary, bonus), feedback (e.g., role clari<sup>fi</sup>cation), and social reinforcers (e.g., approval, praise, recognition). Relevant to this study, we consider recognition from the review site (e.g., a badge) as a social reinforcer that we expect to positively in<sup>fl</sup>uence members’ contribution behavior in the community. Recognition, conferred publicly and selectively to recipients, symbolically represents status or reputation within the community, and also fosters trust within the community by signaling the members’ expertise and credibility [20]. Additionally, recognition (also sometimes referred to as award) fundamentally di<sup>f</sup>ers from monetary rewards and is valued di<sup>f</sup>erently by recipients [27].

Reinforcement theory suggests that the e<sup>fi</sup>cacy of reinforcers varies depending on several factors, such as schedules of reinforcement, frequency of administration, and changing importance of the reinforcer [63]. To explain how online community members’ contribution behaviors change under repeated recognition, we need to understand how the e<sup>f</sup>ect of social reinforcers may vary with repeated application. In this regard, prior research suggests that the strength of reinforcement on individuals’ behavior diminishes with repeated occurrence of the reinforcer [53, 76]. This condition is known as reinforcer satiation. Satiation occurs when the reinforcer is no longer motivating, as its value diminishes due to overexposure. Thus, recurrent application of the same social reinforcer may not lead to a perpetual increase in behavior. Rather, it has been observed that social reinforcers (e.g., approval, recognition) when presented repeatedly or for a prolonged time, tend to lose their e<sup>f</sup>ectiveness [22, 29]. Additionally, the application of the reinforcer (i.e., recognition in our case) should be perceived as fair by the recipient in order to be e<sup>f</sup>ective, as per equity theory.

## Equity Theory and Recognition Inequity

Adams’ equity theory is a widely accepted motivational theory that explains human behavior [1, 2], where equity is de<sup>fi</sup>ned as the degree of fairness. The basic premise of this theory is that individuals expect to be treated with fairness and impartiality by others [12]. Individuals engage in a task with an expectation of equity between the inputs that they contribute to the task (e.g., e<sup>f</sup>ort, skills, enthusiasm) and the outcomes they receive (e.g., salary, rewards, and recognition) [1]. In other words, they expect to be rewarded commensurate with the e<sup>f</sup>orts they put in for the task. The fairness is typically judged against the perceived inputs and outcomes of others for the same or similar task. In the context of our study, members of an online review community would expect to be recognized if their contributions are similar to the contributions of other members who have received the recognition (e.g., badge).

Conversely, individuals become demotivated in relation to both the task and the evaluation environment if they perceive inequity between their inputs and received outcomes [1, 2]. Dissatis<sup>fi</sup>ed individuals respond to this perceived unfairness by reducing their e<sup>f</sup>orts, leading to a decline in their performance. Several studies in organizational settings have reported <sup>fi</sup>ndings that are consistent with equity theory (i.e., have shown a negative in<sup>fl</sup>uence of perceived inequity on employees’ motivation and task performance) [61, 74]. Studies that have applied equity theory in online community settings have primarily used it to establish various drivers of contribution behavior (e.g., online justice perceptions [18], reciprocity [24], perceived community equity [47], and helping the service provider [79]). Thus, we explore the negative in<sup>fl</sup>uence of inequity in recognition on online community members’ contribution behavior, which has not been examined.

## Hypotheses Development

As per our research objectives, we develop hypotheses to explain the e<sup>f</sup>ects of <sup>fi</sup>rst-time and repeated recognition on the contribution behavior of members of online review communities over time. We also propose hypotheses regarding the e<sup>f</sup>ects of nonrecognition on the contribution behavior of deserving members. As per reinforcement theory, we assess contribution behavior mainly by its strength and frequency of occurrence. Strength corresponds to the contribution efort (assessed as review length), while frequency corresponds to the contribution quantity (assessed as review count) per time period. Both these aspects have been employed in the prior literature to assess online review contributions, as they are considered desirable for increasing the value of review sites to consumers [8, 70]. Furthermore, contribution e<sup>f</sup>ort is likely to be particularly important for review sites, where the e<sup>f</sup>ort put in by contributors to describe their experience with a business, product, or service, is of value as compared to having speci<sup>fi</sup>c expertise or domain knowledge that is required in other contribution sites (e.g., programming, or Q&A sites). While the two concepts (e<sup>f</sup>ort and quantity) appear related, they are conceptually di<sup>f</sup>erent. It is conceivable for reviewers to write frequent but short reviews, thus increasing the contribution quantity, with the same or even decreasing amount of contribution e<sup>f</sup>ort. Hence, it is important to examine both e<sup>f</sup>ort and quantity as contribution outcomes.

## Recognition as Social Reinforcer

Recognition refers to public appreciation for individuals’ e<sup>f</sup>orts in the form of nonmonetary rewards [7, 52]. In the context of our study, it is de<sup>fi</sup>ned as the appreciation in the form of non-monetary reward (e.g., badge) provided to a member for his/her contributions to the online review community. It serves as a public acknowledgement of the recipient’s status or merits in the community. Studies on online communities show that the expectation of achieving status or recognition is a motivator for community participation [45, 77]. Similarly, in online review communities, members indicated that they participate with an expectation of gaining recognition and status within the community [35, 65]. Thus, expected recognition is seen as a motivator for members’ contribution in online communities (i.e., in the pre-recognition phase).

Given the value of recognition to individuals, reinforcement literature acknowledges it as an important positive social reinforcer [69]. Thus, recognition (e.g., badge) is used by online review communities as a positive reinforcer to make members contribute to the community. Accordingly, prior studies found that badges or awards positively in<sup>fl</sup>uence individuals’ contributions to online communities in the post-recognition phase [33, 46]. Hence, based on reinforcement theory [63] we expect that recognition (e.g., conferment of badge) will act as a positive social reinforcer in online review communities and increase members’ contribution behavior, both in terms of strength (e<sup>f</sup>ort) and frequency (quantity per time period). This is particularly true for <sup>fi</sup>rst-time recognition, as receiving recognition for the <sup>fi</sup>rst time involves a sudden improvement in the status of the member [26] and the resultant bene<sup>fi</sup>ts, such as increased self-esteem [45]. This leads us to hypothesize:

Hypothesis 1a (H1a): Contribution efort (per time period) after first recognition will be higher than that before recognition.

Hypothesis 1b (H1b): Contribution quantity (per time period) after first recognition will be higher than that before recognition.

## Satiation on Repeated Recognition

Prior research has observed that the e<sup>f</sup>ect of recognition (or awards) on individuals motivation and behavior in the workplace is usually short-lived [55]. The diminishing e<sup>f</sup>ect of recognition could be intuitively linked to the idea that the same status or recognition loses its appeal if provided multiple times [3]. This could be theoretically explained by the concept of reinforcer satiation, which occurs in case of repeated administration of social reinforcers over a period of time. Satiation implies a sustained availability of a reinforcer, su<sup>fi</sup>cient to e<sup>f</sup>ect a decrease in the behaviors for it [29]. Satiation could be explained from the viewpoint of habituation in which people become used to a stimulus that is presented repeatedly or for a long period of time, whereby the responsiveness to the stimulus decreases [53].

Accordingly, in the context of our study, we expect that the social reinforcement provided by the recognition of contributors (e.g., through badges) will be prone to satiation, and members would value the recognition less on multiple receptions over time [3]. The satiation e<sup>f</sup>ect could be even more prominent in the case of longer duration of exposure to recognition [53] in communities such as Yelp where members are allowed to hold on to their status for an entire year. Thus, in comparison to the contribution behavior seen after receiving the <sup>fi</sup>rst-time recognition, we expect the contribution behavior (both in terms of strength and frequency) to decrease in the long run after repeated receptions of the recognition. Hence, we propose the following:

Hypothesis 2a (H2a): Contribution efort (per time period) after repeated recognition will be lower than that after first recognition.

Hypothesis 2b (H2b): Contribution quantity (per time period) after repeated recognition will be lower than that after first recognition.

## Non-reception of Recognition

Receiving community recognition is a major expectation of members when spending their time and e<sup>f</sup>ort in contributing reviews in an online community [35]. Members who do not receive recognition despite contributing actively in the community would perceive unfairness or inequity in the system, due to the imbalance between their e<sup>f</sup>orts and the received bene<sup>fi</sup>ts [1]. This perception would be further enhanced if they <sup>fi</sup>nd other members being recognized with similar or possibly even lower levels of contribution. Equity theory suggests that such perception of inequity will lead the dissatis<sup>fi</sup>ed members to reduce their contribution [1]. Accordingly, several studies have reported a negative in<sup>fl</sup>uence of perceived inequity on individuals’ motivation and task performance [61, 74]. Some individuals may even consider non-reception of the expected reward to be equivalent to punishment and may get completely dissuaded from further pursuing the task [43]. Hence, in the context of our study, we expect that deserving, yet unrecognized community members would reduce their subsequent contribution e<sup>f</sup>ort and quantity on nonreception of recognition. Thus, we posit the following:

Hypothesis 3a (H3a): Contribution efort (per time period) of deserving members after nonrecognition will be lower than that before non-recognition.

Hypothesis 3b (H3b): Contribution quantity (per time period) of deserving members after non-recognition will be lower than that before non-recognition.

## Research Methodology

## Data and Context

For our investigation, we chose Yelp as the target online review community. Yelp is the largest online community hosting reviews on local businesses worldwide, and has been increasingly receiving attention in academic research (e.g., [36, 50]). It implements a recognition system where at the beginning of each year the Yelp Elite Council acknowledges a set of nominated contributors (called the Yelp Elite Squad) by conferring them with the prestigious Elite badge, which lasts until the end of that calendar year. The nomination of contributors can be made by the member themselves (self-nomination), by another member, or by the local community manager. Also, at the end of each year, all existing Elites are automatically re-nominated for consideration for the following year’s badge.

The selection of Elites is performed based on the subjective judgment of the Yelp Elite Council, which considers various aspects of the nominee’s activities as presented on their website<sup>4</sup>: “The Yelp Elite Squad is our way of recognizing people who are active in the Yelp community and role models on and of the site. Elite-worthiness is based on a number of things, including well-written reviews, high-quality tips, a detailed personal profile, an active voting and complimenting record, and a history of playing well with others.” As the system of Elite selection depends on the Council’s discretion, and community members are not given speci<sup>fi</sup>c objective criteria that they need to meet in order to receive the badge, it may be perceived as an “as-if random” process for the active members. In fact, it is possible that among members who made similar contributions some may receive the Elite badge and others may not. This makes Yelp a suitable site to examine both the e<sup>f</sup>ects of multiple recognitions over time, as well as the non-recognition of “deserving” contributors, as per our research objective.

Our dataset from Yelp (originally created for the Yelp dataset challenge)<sup>7</sup> contains 5 million reviews of more than 180,000 local businesses, based out of 10 metropolitan areas across the United States and Europe, contributed by 1.3 million reviewers who visited local businesses and reviewed them between 2014 and 2017. We extracted yearwise data for members on total number of reviews written, average votes received (helpful, cool, and funny), average length of reviews, total number of tips provided, and the total number of likes received on the tips. These parameters convey yearly information about reviewer contribution patterns and may also be considered by Yelp as desirable. Since our dataset contains reviews on businesses from 10 metropolitan areas, it is possible that for a member, some reviews pertaining to the businesses located in cities other than these areas are excluded. Hence, for the purpose of our analysis, we selected only those members (count: 503,486) who had at least 70% of their total contributions available in the dataset. That way, we had at least 200 members who received repeated recognition in 2015–2017 (higher thresholds yielded fewer repeat members). Also, to ensure a set of members that were comparable in terms of experience on the site in 2014 (base year selected for our study), we considered only those who joined the platform between the years 2012 and 2014, and had at least one review in 2014. This allowed us to identify 81,393 reviewers including both recognized and unrecognized reviewers.

## Contribution Outcome Measures

The dependent variables used in our study are contribution quantity and contribution e<sup>f</sup>ort. We measured contribution quantity using the normalized values of review count for the member in that year, similar to prior studies (e.g., [17]). To assess contribution efort, we used the product of normalized review count and normalized value of average review length for the member in that year. In prior research, e<sup>f</sup>ort has been de<sup>fi</sup>ned as the amount of time spent on a task [9, 54]. The combined measure of review count and average review length (i.e., total number of words written) can indicate the amount of time spent by a member towards contributing reviews and, hence, is a good proxy for his/her contribution e<sup>f</sup>ort [8].

Normalization of each variable (review count and average review length) was done with respect to its population mean for that year. We used normalized values of outcome variables instead of absolute values to take care of the e<sup>f</sup>ect of any extraneous and unaccounted factors on the dependent variables. For example, the variable review count can show a sudden surge in a particular year for all the reviewers (irrespective of their status), and this may be triggered by exogenous factors, such as a change in the userinterface of the website or launch of its mobile application, boosting its usability. Comparing the normalized values over years not only alleviates the issue of unaccounted yearly <sup>fl</sup>uctuations, but also provides a comparison between the values of the outcomes for the individual member with respect to the average contribution of the community for the particular year.

## Research Design

To examine the e<sup>f</sup>ect of receiving or not receiving the annual Elite recognition, we identi<sup>fi</sup>ed and compared the values of members’ contribution behavior (i.e., contribution e<sup>f</sup>ort and quantity, across years). As the interventions had occurred beforehand and were beyond the control of the researchers, a quasi-experimental study with ex-post facto design was considered to be the most appropriate methodology to test the hypothesized relationships [11]. Ex-post facto analysis takes a similar approach to true experiments conducted in controlled laboratory settings, but it relaxes the random assignment criterion to a certain extent since it is an after-the-fact research design. In ex-post facto analysis, for groups that exhibit di<sup>f</sup>erences in observed outcomes after the interventions, the researchers attribute the di<sup>f</sup>erences to intervening factors retrospectively [39]. In our study, we conducted 3 within-subject quasi-experiments with 3 separate groups to test H1, H2, and H3. For each group, the comparison of contribution behavior between pre- and postintervention periods was performed using paired t-tests, a commonly used statistical method for within-subject comparison of means. Additionally, to improve the robustness of our results, we conducted Durbin-Wu-Hausman tests of endogeneity (also known as augmented regression model) to help us establish the e<sup>f</sup>ect of recognition on contribution outcomes after controlling for confounding and unaccounted factors [19, 34].

## Identi<sup>fi</sup>cation Strategy

For the study, we needed to identify three groups to test the three sets of hypotheses. Our <sup>fi</sup>rst group was created to test whether receiving recognition acts as a positive social reinforcer and leads to an increase in contribution behavior. From our processed sample of 81,393 members who joined Yelp in 2012–2014, we selected all those who had received their <sup>fi</sup>rst annual Elite recognition in 2015. The <sup>fi</sup>nal subset after cleaning and <sup>fi</sup>ltering consisted of 375 reviewers, which was named the “recognized” group. H1a and H1b were tested by comparing the change in contribution behavior of this group between 2014 and 2015.

Our second group was created to test whether receiving recognition repeatedly leads to a decline in contribution behavior, as proposed using the concept of reinforcer satiation. This group is a subset of the recognized group and comprises reviewers who were conferred the title repeatedly for three consecutive years (2015, 2016, and 2017). The group consisted of 220 reviewers and was categorized as the “repeatedly recognized” group. Using this group, H2a and H2b were tested by comparing the change in their contribution behavior between in 2015 and 2017.

To address the third set of hypotheses developed using the concept of inequity, we needed to identify Yelp members who were deserving of Elite recognition but were not recognized. The only ex-post facto way to do so would be to use matching techniques to <sup>fi</sup>nd unrecognized members in the data who were signi<sup>fi</sup>cantly similar to the recognized members in the pre-recognition period. Thus, we selected members who had experience on Yelp comparable to our <sup>fi</sup>rst group (the recognized group), and closely matched them on key aspects of contribution behavior in 2014. Based on the available data, we used the following 5 contribution parameters for our matching: review count, average review votes, average review length, tip count, and average tip likes. The dataset did not include information on members’ voting and complimenting activities. However, since Yelp does not disclose the exact criteria for selection of Elite members and there is subjectivity in the stated criteria, to validate the matching parameters we conducted a separate analysis to verify their predictive power in classifying Elite members. Various classi<sup>fi</sup>cation models i.e., decision tree, C&R tree, neural network, and C5.0, were employed using the Elite status of 2015 as the target variable and contribution parameters of 2014 as predictor variables.

To enhance the generalizability of the results, we partitioned the entire dataset into training and test sets in a 70:30 ratio, where the models were trained using the training set and evaluated using the test set. The models were further tested for a di<sup>f</sup>erent partitioning ratio (60:40). Moreover, 3-fold and 10-fold cross-validation techniques were used in the case of the C5.0 classi<sup>fi</sup>er for further increasing generalizability of the results. We obtained a very high value of prediction accuracy (\~85–90%), which established the importance of these contribution parameters in the Elite selection process (see Table A.1 of Appendix A). This implies that members who are similar on these parameters should have equal probability of being selected as Elite members by Yelp, thus legitimizing their use as matching parameters.

Next, we performed a 1:1 matching between our recognized (<sup>fi</sup>rst) group of 375 reviewers and the pool of unrecognized reviewers based on the 5 contribution parameters using the optimal matching algorithm, which applies the network <sup>fl</sup>ow methodology outlined in Rosenbaum [64]. The matching resulted in the third group of our study consisting of 375 reviewers. These were the reviewers who were similar to the recognized group in all 5 contribution parameters in 2014, yet did not get recognition in 2015. We call them the “deserving unrecognized” group. Using this group, H3a and H3b were tested by comparing their change in contribution behavior between 2014 and 2015.

Table A.2 in Appendix A shows the descriptive statistics of contribution parameters for all three groups. To verify the e<sup>f</sup>ective matching, we also carried out t-tests (Table A.3 of Appendix A) to compare the matched groups (i.e., recognized versus deserving unrecognized), which revealed that there was no signi<sup>fi</sup>cant di<sup>f</sup>erence between the two groups on any of the parameters. Furthermore, another set of t-tests showed that our recognized group was signi<sup>fi</sup>cantly better than a set of randomly selected community members in terms of all the parameters (Table A.4 of Appendix A). These tests indicate that the deserving unrecognized group closely resembled the recognized group in 2014 and were much better reviewers than any other randomly selected group.

## Analysis and Results

## Results for Hypotheses 1a and 1b

In order to test the <sup>fi</sup>rst set of hypotheses we analyzed the members of the recognized group to ascertain whether their contribution e<sup>f</sup>ort (H1a) and quantity (H2b) increased after receiving the Elite badge. For this purpose, we compared contribution e<sup>f</sup>ort and quantity for the year immediately after the <sup>fi</sup>rst intervention (i.e., 2015) with that of the preintervention year (i.e., 2014). A pairwise comparison of means (paired t-test) for the recognized group members showed that the contribution efort signi<sup>fi</sup>cantly increased in 2015 following the <sup>fi</sup>rst reception of Elite recognition $( \mathrm { M } _ { 2 0 1 5 } = 6 8 . 3 3 )$ as compared to 2014 $( \mathrm { M } _ { 2 0 1 4 } = 3 4 . 1 4 )$ $\mathrm { { p } < 0 . 0 0 1 }$ . Also, contribution quantity of the recognized group members signi<sup>fi</sup>cantly increased in 2015 $( \mathrm { M } _ { 2 0 1 5 } = 4 1 . 0 7 )$ as compared to 2014 $( \mathbf { M } _ { 2 0 1 4 } = 2 7 . 9 2 )$ , p < 0.001. Since the value of the dependent variables was normalized against the overall population mean, the results imply that both the contribution e<sup>f</sup>ort and quantity increased for the recognized group as compared to the average population, thus supporting both H1a and H1b. Table 2 shows the change in both contribution outcomes for recognized members. Figure 1 graphically depicts the change in contribution behavior for recognized members.

Contribution behavior of recognized and deserving unrecognized members.

<table><tr><td></td><td>Normalized Mean Pre-Recognition Year (2014)</td><td>Normalized Mean Post-Recognition Year (2015)</td><td>Difference in Means</td></tr><tr><td colspan="4">Recognized Members (N = 375)</td></tr><tr><td>Contribution Effort</td><td>34.14</td><td>68.33</td><td>34.19***</td></tr><tr><td>Contribution Quantity</td><td>27.92</td><td>41.07</td><td>13.15***</td></tr><tr><td colspan="4">Deserving Unrecognized Members (N = 375)</td></tr><tr><td>Contribution Effort</td><td>29.43</td><td>9.40</td><td>-20.03***</td></tr><tr><td>Contribution Quantity</td><td>25.01</td><td>6.82</td><td>-18.19***</td></tr></table>

Notes: \*\*\* p < 0.001.

![](/api/attachments/R5EMZVUN/fulltext/images/24a0435ed59369898a55f0c4e9f3f6f3f43656a98ffbc14407934f9b247cba60.jpg)  
Contribution behavior of recognized members.

## Results for H2a and H2b

The e<sup>f</sup>ect of repeated recognition on contribution e<sup>f</sup>ort (H2a) and quantity (H2b) was investigated by analyzing the behavior of the repeatedly recognized group members for the years 2015, 2016, and 2017, in all of which the Elite badge recognition was awarded to them. We observed a signi<sup>fi</sup>cant drop in contribution efort for this group in 2016 after receiving recognition for the second time $( \mathrm { M } _ { 2 0 1 6 } = 5 0 . 3 6 )$ as compared to 2015 when they <sup>fi</sup>rst received the recognition $( \mathrm { M } _ { 2 0 1 5 } = 8 4 . 7 5 )$ . The e<sup>f</sup>ort further declined with the third reception of recognition in 2017 $( \mathbf { M } _ { 2 0 1 7 } = 3 3 . 2 0 )$ . A paired t-test comparing means of 2015 and 2017 con<sup>fi</sup>rmed that with repeated reception of the badge (in 2015, 2016, and 2017) members reduced their contribution e<sup>f</sup>ort, thus supporting H2a $( \mathtt { p } < 0 . 0 0 1 )$ . Similarly, contribution quantity declined with repeated recognition as well. A pairwise comparison of means showed a signi<sup>fi</sup>cant decline in the contribution quantity for this group in 2017 after three receptions of recognition $( \mathrm { M } _ { 2 0 1 7 } = 1 8 . 0 7 )$ as compared to 2015 $( \mathrm { M } _ { 2 0 1 5 } = 4 9 . 6 0 )$ thus supporting H2b as well $( \mathtt { p } < 0 . 0 0 1 )$ . Table 3 presents the results for the repeatedly

## Results for Hypotheses 3a and 3b

Next, we evaluated the change in contribution e<sup>f</sup>ort (H3a) and quantity (H3b) for the deserving unrecognized group members (selected using optimal matching, as described before) to test the hypothesized negative e<sup>f</sup>ect of non-reception of recognition. A pairwise comparison of means displayed a signi<sup>fi</sup>cant decline in contribution efort $( \mathtt { p } \ < \ 0 . 0 0 1 )$ in 2015 $( \mathbf { M } _ { 2 0 1 5 } ~ = ~ 9 . 4 0 )$ from the pre-intervention year of 2014 $( \mathrm { M } _ { 2 0 1 4 } = 2 9 . 4 3 )$ for the deserving unrecognized group. Hence, H3a is supported. Contribution quantity also su<sup>f</sup>ered a signi<sup>fi</sup>cant $( \mathtt { p } \ < \ 0 . 0 0 1 )$ decline in 2015 $( \mathrm { M } _ { 2 0 1 5 } = 6 . 8 2 )$ in comparison to 2014 $( \mathbf { M } _ { 2 0 1 4 } = 2 5 . 0 1 )$ , thus supporting H3b. The change in contribution behavior for deserving unrecognized members is presented in Table 2 and Figure 3.

Contribution behavior of repeatedly recognized members.

<table><tr><td></td><td>Normalized Mean Pre-Recognition Year (2014)</td><td>Normalized Mean Post-Recognition Year (2015) A</td><td>Normalized Mean Post-Repeated-Recognition Year (2016) B</td><td>Normalized Mean Post-Repeated-Recognition Year (2017) C</td><td>Difference in Means (C-A)</td></tr><tr><td colspan="6">Repeatedly Recognized (N = 220)</td></tr><tr><td>Contribution Effort</td><td>35.80</td><td>84.75</td><td>50.36</td><td>33.20</td><td>-51.55***</td></tr><tr><td>Contribution Quantity</td><td>28.74</td><td>49.60</td><td>28.01</td><td>18.07</td><td>-31.53***</td></tr></table>

Notes: \*\*\* p < 0.001.

![](/api/attachments/R5EMZVUN/fulltext/images/b63b9ff94b4979f2b9d1e728f404ff36ba90cc2ba38ea0c7a82d0810803e5754.jpg)  
Contribution behavior of repeatedly recognized members.

## Robustness Checks and Additional Analyses

## Endogeneity Test

We used ex-post facto analysis for this quasi-experimental study; hence, there is a possibility of unaccounted endogeneity inducing erroneous results. Therefore, as a robustness test, we checked for endogeneity using the Durbin-Wu-Hausman test (augmented regression test) [19, 34]. This test investigated whether members’ contribution behavior in a given year t is in<sup>fl</sup>uenced by reception/non-reception of recognition, denoted by Elite (t), even in the presence of possible confounding factors and other unaccounted factors. Elite (t) being the endogenous variable in our context, a possible confounding variable would be the contribution behavior of the previous year (t-1), which could a<sup>f</sup>ect both contribution behavior (t) and Elite (t). For this analysis, we considered the case of receiving the Elite badge at t = 2015, captured by the binary variable Elite (2015), which is set to 1 for members who received recognition at the beginning of 2015 and 0 otherwise. Thus, the core regression equations for contribution e<sup>f</sup>ort and quantity are:<sup>9</sup>

![](/api/attachments/R5EMZVUN/fulltext/images/f05eb7e39c67113335dbf0b66db42d626b3dff75a04f938dafff25f528b8ac5f.jpg)  
Contribution behavior of deserving unrecognized members.

$$
\begin{array}{c} \text { Contribution   effort(2015) = a_{0} + b_{0} Elite(2015) + b_{1} Contribution   effort(2014)} \\ + \varepsilon \end{array}\tag{1.1}
$$

$$
\begin{array}{r l} \text {Contribution quantity (2015)} & = a _ {0} + b _ {0} \text {Elite (2015)} \\ & + b _ {1} \text {Contribution quantity (2014)} + \varepsilon \end{array}\tag{1.2}
$$

In the first stage of the Durbin-Wu-Hausman test, all signi<sup>fi</sup>cant<sup>10</sup> contribution parameters (review count, average review votes, average review length) of the previous year 2014 were used as explanatory variables for a regression model to predict Elite (2015). The residual generated from this regression analysis Elite2015\_res captured all the unaccounted factors used to predict Elite (2015).

$$
E l i t e (2 0 1 5) = C o n t r i b u t i o n p a r a m e t e r s (2 0 1 4) + E l i t e 2 0 1 5 \_ {r} e s\tag{1.3}
$$

In the second stage of the test, we augmented the regression Equations 1.1 and 1.2 by adding Elite2015\_res from Equation 1.3 as an additional explanatory factor. Thus, the generalized augmented regression equations included both known confounding factors as well as unaccounted factors, and can be framed as:

$$
\begin{array}{r l} \text { Contribution   effort } (2 0 1 5) & = a _ {0} + b _ {0} \text { Elite } (2 0 1 5) + b _ {1} \text { Contribution   effort } (2 0 1 4) \\ & \quad + b _ {2} \text { Elite } 2 0 1 5 \_ r e s + \varepsilon \end{array}
$$

$$
\begin{array}{r l} \text {   Contribution   quantity   (2015)   } & = a _ {0} + b _ {0} \text {   Elite   (2015)   } + b _ {1} \text {   Contribution   quantity   (2014)   } \\ & \quad + b _ {2} \text {   Elite   2015\_res   } + \varepsilon \end{array}
$$

The interpretation of the results of the augmented regressions would be: a) if $b _ { 2 }$ is signi<sup>fi</sup>cant, then we fail the test and there is unaccounted endogeneity in the model which merits further analysis; b) if $b _ { 2 }$ is not signi<sup>fi</sup>cant and even $b _ { O }$ is not signi<sup>fi</sup>cant then we fail to establish the in<sup>fl</sup>uence of recognition on contribution behavior; and c) if $b _ { 2 }$ is not signi<sup>fi</sup>cant and $b _ { O }$ is signi<sup>fi</sup>cant (and positive), then we pass the test and can support the claim that receiving the Elite recognition in 2015 did indeed improve the contribution outcomes.

The detailed results of each stage of the Durbin-Wu-Hausman test are included in Appendix B. The coe<sup>fi</sup>cient of residual Elite2015\_res was found to be insigni<sup>fi</sup>cant for both contribution e<sup>f</sup>ort $( \mathfrak { p } = 0 . 4 9 )$ in Table B.2 of Appendix B, and contribution quantity $( \mathtt { p } \ = \ 0 . 6 3 )$ in Table B.3 of Appendix B. This suggests that there is no unaccounted endogeneity in our model. Also, the coe<sup>fi</sup>cient of Elite (2015) was found to be positive and signi<sup>fi</sup>cant $( \mathtt { p } < 0 . 0 0 1 )$ for both contribution e<sup>f</sup>ort and contribution quantity in Appendix B, Tables B.2 and B.3, respectively, thus supporting the impact of recognition on contribution behaviors and passing this endogeneity test.

## Contribution Quality as Outcome

As part of the additional analyses, we also investigated another aspect of contribution behavior i.e., contribution quality, as is done in a number of studies (e.g., [15, 49, 60]). Prior studies have adopted either an objective view of quality (i.e., the information meets the requirements of particular activities) [57, 75], or a subjective view (i.e., the information meets the user’s expectations) [5]. In the context of online reviews, studies have typically preferred the subjective view and have widely used helpfulness/usefulness votes as the proxy for review quality [30, 56, 59]. Accordingly, we used “average number of votes received per review” for the member, normalized over the population mean for assessing contribution quality in the respective years.

The e<sup>f</sup>ect of first-time recognition on contribution quality was examined using the 375 members of the recognized group. A pairwise comparison of means revealed that on receiving the Elite badge at the beginning of 2015, contribution quality $( \mathbf { M } _ { 2 0 1 5 } = 2 . 3 8 )$ increased signi<sup>fi</sup>cantly $( \mathtt { p } < 0 . 0 0 1 )$ as compared to the pre-intervention year $\begin{array} { r l } {  { ( \mathbf { M } _ { 2 0 1 4 } = } } & { { } } \end{array}$ 1.29). The e<sup>f</sup>ect of repeated recognition tested on the second group revealed that on reception of Elite badges in 2015, 2016, and 2017, contribution quality kept on increasing in each year $( \mathrm { M } _ { 2 0 1 4 } = 1 . 3 2 $ $\mathrm { M } _ { 2 0 1 5 } = 2 . 5 8$ $\mathrm { M } _ { 2 0 1 6 } = 5 . 4 0$ , and $\mathrm { M } _ { 2 0 1 7 } = 7 . 1 2 )$ . Table C.1 (Appendix C) shows the results for contribution quality for <sup>fi</sup>rst-time recognized members, while Table C.2 shows the e<sup>f</sup>ect of repeated recognition on contribution quality. Figure C.1 (Appendix C) graphs the change in contribution quality across years for repeatedly recognized members, while Figure C.2 shows the same for deserving unrecognized ones.

The e<sup>f</sup>ect of non-reception of recognition on contribution quality was studied by analyzing the deserving unrecognized group. A pairwise comparison of means of contribution quality showed that its value did not signi<sup>fi</sup>cantly change with non-reception of recognition in 2015 $( \mathrm { M } _ { 2 0 1 4 } \ = \ 1 . 1 6 .$ $\mathrm { M } _ { 2 0 1 5 } ~ = ~ 0 . 9 9 ;$ p = 0.06). Thus, we observe that contribution quality does not change signi<sup>fi</sup>cantly for the deserving, yet unrecognized reviewers. Table C.1 of Appendix C shows these results.

From the aforementioned results, the pattern that emerged for contribution quality di<sup>f</sup>ered from that for contribution e<sup>f</sup>ort and contribution quantity (see Tables C.4 and C.5 in Appendix C). Contribution quality increased for the recognized group and kept on increasing with repeated recognition for 3 years, unlike contribution e<sup>f</sup>ort and contribution quantity where an early satiation of recognition was observed. A possible explanation for the continual increase in quality can be attributed to the learning e<sup>f</sup>ect, which posits that individuals become more e<sup>fi</sup>cient and/or e<sup>f</sup>ective in performing any task after repeating it several times [4]. Individuals who are more experienced in writing reviews are more likely to produce higher quality content. Indeed, prior studies have shown an association between the number of reviews written by a reviewer and the average helpfulness votes received [48, 59]. Our empirical analysis (presented in Table C.3 of Appendix C) shows signi<sup>fi</sup>cant impacts of both learning e<sup>f</sup>ect and recognition on contribution quality.

Another explanation for contribution quality increasing with repeated recognition is that (unlike for contribution e<sup>f</sup>ort and quantity) there is likely a reputational e<sup>f</sup>ect of the Elite badge that draws readers to the reviews of these recognized members and increases the number of votes they receive. In other words, Elite badge holders’ reputation could increase the helpfulness of their reviews, as seen through votes [78]. Overall, both the learning and reputational e<sup>f</sup>ects could outweigh the recognition satiation e<sup>f</sup>ects, resulting in a net increase in contribution quality for repeated recognition. However, contribution quality did not change signi<sup>fi</sup>cantly for the deserving unrecognized group. This could be because the learning (positive) e<sup>f</sup>ect could be compensated by the non-recognition (negative) e<sup>f</sup>ect for this group.

## E<sup>f</sup>ects of Receiving/Not-Receiving Recognition in Di<sup>f</sup>erent Temporal Orders

Last, we present additional analyses on the contribution behavior of members who received recognition (or did not) in various temporal orders<sup>11</sup> other than the main orders that we hypothesized. Although the small sample size in some of these scenarios calls for caution in making reliable statistical claims, analyzing the patterns (using paired t-tests at p < 0.05) provided interesting insights and supplemented our main results on the e<sup>f</sup>ects of reception (R) and non-reception (NR) of recognition i.e., the Elite badge in this case. As per the logic for H1a and H1b, we expected a positive e<sup>f</sup>ect of <sup>fi</sup>rst-time recognition on contribution e<sup>f</sup>ort and quantity for the relevant scenarios (a, b, c, d). The satiation e<sup>f</sup>ect of repeated recognition (as per the logic for H2a,b) was expected for scenario b, while the decline of contribution outcomes on non-reception of recognition (as per the logic for H3a,b) was expected for all the scenarios. The results for these analyses are presented in Table D.1 of Appendix D. Graphs of the contribution trajectories for each scenario are shown in Figure 4 and discussed in the following sections.

(a) R, NR, NR (N =10): We examined members who received recognition only once in 2015, but not in subsequent periods, even when worthy (i.e., similar to our repeatedly recognized group) in 2015. We observed that their contribution behavior (in terms of e<sup>f</sup>ort and quantity) increased signi<sup>fi</sup>cantly after receiving recognition in 2015. However, it decreased signi<sup>fi</sup>cantly in 2016, and further reduced in 2017, owing to non-reception of recognition.

(b) NR, R, R (N =165): Next, we investigated members who did not receive recognition in 2015, but received it in the subsequent periods (2016 and 2017). Results showed that both their contribution e<sup>f</sup>ort and quantity decreased signi<sup>fi</sup>cantly after not receiving recognition in 2015. On receiving recognition in 2016 both outcomes increased, however, on further reception in 2017 both outcomes reduced again, indicating satiation in recognition.

(c) R, NR, R (N = 9): We also looked into the contribution behavior of members who received recognition in alternate years (i.e., those who were awarded recognition in 2015 and 2017, but not in 2016). Their contribution e<sup>f</sup>ort and quantity increased after receiving recognition in 2015, reduced on non-reception of recognition in 2016, and again rose in 2017 on recognition.

(d) NR, R, NR (N = 36): For the members who did not receive recognition in alternate years, we observed that contribution e<sup>f</sup>ort and quantity decreased signi<sup>fi</sup>cantly after not receiving recognition in 2015. On receiving recognition in 2016 it increased, and again decreased on non-reception of recognition in 2017.

(e) NR, NR, NR (N = 440): Finally, we studied the contribution behavior of members who were deserving in 2014 but did not receive recognition during any of the following 3 years. We observed that contribution e<sup>f</sup>ort and quantity decreased signi<sup>fi</sup>cantly after not receiving recognition in 2015. On further non-reception in 2016 and 2017, their contribution outcomes decreased further. Interestingly, the e<sup>f</sup>ect of repeated non-recognition also dampened across years (i.e., the amount of decline in contribution e<sup>f</sup>ort and quantity decreased with each denial of recognition over the years). While this could potentially be an indication of inequity satiation, we are unable to test it because the members in this group where not deserving anymore when their contributions declined considerably after the <sup>fi</sup>rst non-recognition. However, this question would be useful to explore in future with suitable data.

![](/api/attachments/R5EMZVUN/fulltext/images/239e8b38746c29ce43559d8fb1f0b6e4cddfbb9b4266a402679535408f374488.jpg)  
R, NR, R

![](/api/attachments/R5EMZVUN/fulltext/images/0b990a97c94b338ceb720b873ac6a079a849f1ab2a5227c2aae5e911148f4a02.jpg)

![](/api/attachments/R5EMZVUN/fulltext/images/c6edc624df77395edc03cba7d3e14cd38e1934bbd80acc982ddc71fe48ec8269.jpg)

![](/api/attachments/R5EMZVUN/fulltext/images/b957853daad9043a9da2b3a07f8afdf5d4e4364303c39d27fdc937be15baa36d.jpg)

NR, NR, NR  
![](/api/attachments/R5EMZVUN/fulltext/images/7a7e47b7dca2916b5229dcad94701b0ec4dc1c7ccf6471b6776dd7d84355b32f.jpg)  
Contribution behavior for receiving (R) or not-receiving (NR) recognition in di<sup>f</sup>erent orders.

Observing the trajectories for all the scenarios above, we <sup>fi</sup>nd commonalities in their patterns. In each case, contribution behavior, in terms of e<sup>f</sup>ort and quantity, increased after receiving recognition and decreased after non-recognition. The <sup>fi</sup>ndings corroborate with our hypotheses regarding the contribution behaviors of recognized and deserving unrecognized groups. Also, we note that the e<sup>f</sup>ect of receiving recognition for the second time (refer to the cases NR, R, R and R, NR, R) was less than the e<sup>f</sup>ect of receiving it for the <sup>fi</sup>rst time. The results provide support for our satiation argument for multiple recognitions. Interestingly, we also found a similar satiation e<sup>f</sup>ect for non-recognition (i.e., the in<sup>fl</sup>uence of repeated non-recognition also dampened across years).

## Discussion and Implications

Recognition is often employed to stimulate contributions in online review communities [65]. Yet, there are several gaps in our understanding of the e<sup>f</sup>ectiveness of recognition for this purpose, including the negative side e<sup>f</sup>ects of this mechanism. Motivated thus, we theorize and test the e<sup>f</sup>ect of recognition in in<sup>fl</sup>uencing contribution behaviors of members for repeated versus <sup>fi</sup>rst-time recognition, as well as for the e<sup>f</sup>ect of nonrecognition for deserving members. We build on reinforcement theory [51, 69] to propose a positive role of <sup>fi</sup>rst-time recognition as a social reinforcer of contribution behavior, while repeated recognition is hypothesized to su<sup>f</sup>er from reinforcer satiation. However, for deserving yet unrecognized members we propose a decrease in contribution due to inequity in recognition. Using quasi-experiments on members of one of the largest online business review sites, Yelp.com, we <sup>fi</sup>nd empirical support for our hypotheses, with contribution e<sup>f</sup>ort and quantity as outcomes. From a post-hoc analysis, we <sup>fi</sup>nd that contribution quality displays an increasing trajectory for recognized reviewers, and a nearconstant level for deserving, yet unrecognized members. In other words, contribution quality behaves distinctly from contribution e<sup>f</sup>ort and quantity, and does not exhibit the negative e<sup>f</sup>ects for unrecognized members.

## Research Contributions

This paper o<sup>f</sup>ers several important research contributions. First, it advances the growing body of literature on member contribution in online communities, in general, and online review communities, in particular. Existing literature on online review communities extensively discusses the e<sup>f</sup>ect of monetary rewards on contribution behavior [10, 25, 44, 70], with relatively less focus on alternative sources of reward. This study contributes towards addressing this imbalance by drawing attention to the role of recognition as a means of stimulating online contributions.

Second, to the best of our knowledge, this work is an initial attempt to investigate the e<sup>f</sup>ect of repeated conferment of community recognition on members’ contribution behavior. Largely, existing research has not considered the time-varying e<sup>f</sup>ect of repeated administration of recognition on member contributions. Although Garnefeld et al. [28] explored the short-term and long-term e<sup>f</sup>ects of rewards (monetary and normative), their study was restricted to a single reception of the reward and the dependent variables (shortterm and long-term posting intentions) were measured through a survey of members. Furthermore, Gallus [26] studied the e<sup>f</sup>ects of multiple rounds of rewards on Wikipedia, but examined the retention rate of newcomers as the outcome. Thus, our study advances extant research by demonstrating the diminishing e<sup>f</sup>ect of repeated recognition on contribution e<sup>f</sup>ort and quantity in online communities.

Third, we report on multiple aspects of online review contribution behavior (quantity, e<sup>f</sup>ort, and quality) in a single study. Prior studies have often used contribution quantity as the sole measure of contribution [33, 46, 71], while some used only quality (e.g., [15]), which doesn’t o<sup>f</sup>er understanding regarding the impact on other aspects. Also, our use of contribution e<sup>f</sup>ort (product of number of reviews and average review length), captures the time and energy spent in writing reviews, which is seldom addressed in the literature [8]. As mentioned earlier, contribution e<sup>f</sup>ort is likely to be important for review sites, where the e<sup>f</sup>ort put in by contributors to describe their experience with a business, product, or service, is of particular value as compared to having speci<sup>fi</sup>c domain knowledge that is required in other contribution sites (e.g., programming, or Q&A sites). Our additional analysis on contribution quality also reveals interesting insights. While previous studies have pointed out di<sup>f</sup>erences in the antecedents of contribution quantity and quality [8, 49, 60], our study highlights the di<sup>f</sup>erences in these two outcomes by demonstrating their di<sup>f</sup>erent trajectories for repeated recognition and non-recognition.

Fourth, past research has typically considered the behavioral outcomes of the individuals who receive rewards and recognition and tended to overlook the remaining members of the community [65]. This study draws attention to that segment of community members who are worthy contributors yet did not get their due recognition. We observe that such non-recognition tends to harm their contribution behavior.

Finally, we add to the literature on reinforcement theory and equity theory in the context of online contributions. Traditionally, reinforcement theory has been used in organizational settings to study the impact of reinforcers (e.g., monetary incentives, social recognition, and performance feedback) on employees’ task performance [68, 69]. With the exception of a few studies (e.g., [21]) where it has been used to understand the role of knowledge validation on employees’ contribution to organizational knowledge repositories, this theory has rarely been utilized to examine individuals’ online contribution behavior. We extend its application to online communities which, unlike organizations, are non-hierarchical in nature and typically depend on voluntary contribution. In our study the theory is used to explicate community members’ online contribution behavior under the in<sup>fl</sup>uence of recognition (e.g., badges, titles) as a reinforcer.

We also extend the literature pertaining to the use of equity theory in online contributions. Previous studies that have employed this theory to examine online community contributions (e.g., [18, 24, 47, 79]) have not considered non-recognition as the basis of inequity. Also, the <sup>fi</sup>ndings of these studies were based on participants’ self-reported contribution behavior captured through surveys and not on their actual contribution behavior. In our study, using quasi-experiments, we identify the negative e<sup>f</sup>ects of inequity in recognition on community members’ actual contribution behavior. Furthermore, we introduce the concept of social reinforcer satiation, which has been earlier used to study the e<sup>f</sup>ect of verbal approval and assent [29, 53], to the context of virtual badges and titles. Satiation can thus be considered an important aspect of members’ response to rewards and recognition in online communities.

## Practical Implications

This paper presents several insights for online community managers and developers of online review sites, especially in designing and implementing recognition systems for their platforms. First, since we <sup>fi</sup>nd that recognition can boost contributions (at least in the short-term), online community managers could employ recognition as an e<sup>f</sup>ective mechanism to drive contribution. Recognition imposes less <sup>fi</sup>nancial cost on the platform as compared to monetary rewards, such as token money or gift coupons, and thus could be used as a lower-cost alternative [31].

Second, since the e<sup>f</sup>ect of recognition tends to decrease with multiple applications, granting the same recognition repeatedly may not su<sup>fi</sup>ce for sustained increase in contribution e<sup>f</sup>ort and quantity. Even for contribution quality, the e<sup>f</sup>ectiveness reduces with repeated recognition. To address this issue, community administrators may experiment with various types of recognition, e.g., di<sup>f</sup>erent levels of badges, or di<sup>f</sup>erent titles, to see if they can sustain the positive reinforcement. For example, TripAdvisor uses di<sup>f</sup>erent levels of badges (New reviewer, Reviewer, Senior reviewer, Top contributor, etc.) based on the number of reviews contributed.

Third, the case of deserving yet unrecognized members serves as a word of caution for site administrators when designing recognition systems. Since worthy members lose their motivation to contribute further when they are left unrecognized, online communities must have robust mechanisms in place for minimizing the cases of false negatives. An automated system for recognizing members may avoid the case of unwanted demotivation by making the recognition process more objective, thereby reducing the chance of nonrecognition of deserving members. Furthermore, online communities should have a grievance redressal system that can pacify the disgruntled members in case they perceive inequity in the recognition mechanism. For example, Stack Over<sup>fl</sup>ow, a popular online Q&A community for programmers, provides a support forum (Meta Stack Over<sup>fl</sup>ow), where community moderators can address the queries related to contributors’ reputation points and badges. Yelp and other online communities could also consider introducing a similar system in their support forum that would address the issues regarding any perceived unfairness in their recognition system.

Fourth, our <sup>fi</sup>ndings show that the e<sup>f</sup>ect of recognition depends on the entire history of members’ contribution and recognition. Thus, designing a system to track the trajectories of members while providing recognition, instead of limiting to the immediate history of contribution, could be bene<sup>fi</sup>cial. Also, we observe that members behave in a theoretically predictable manner for various recognition and non-recognition scenarios. Hence, predictive models could be built to estimate the consequence of providing or withholding recognition, which can guide community managers.

Last, our <sup>fi</sup>ndings indicate that while recognition increases contribution outcomes, satiation and non-recognition can lead to decrease in contribution outcomes. Depending on the distribution of recognition and its consequences, it is possible for the overall contribution outcomes of the entire community to increase or decrease. Since the goals of community managers are related to improving overall community outcomes, an optimization model could be implemented taking as inputs the predicted contributions of all members, and provide the most optimal recognition distributions that maximize the community outcomes.

## Limitations and Future Research

This study is subject to certain limitations, which o<sup>f</sup>er opportunities for future research. First, the <sup>fi</sup>ndings are based on data from a single community, an online review site (Yelp.

com). To test the generalizability of our <sup>fi</sup>ndings, similar research could be carried out for other sites (e.g., online Q&A forums, collaborative sites such as Wikipedia, combined e-commerce and review sites such as Amazon, and user-generated content sites, in general). Second, the <sup>fi</sup>ndings of this study are limited to recognition systems that employ a single type of badge. Thus, further investigation may be performed on other communities, which employ a variety of badges. Third, this study shows the association between members’ community status and contribution behaviors. However, the underlying psychological mechanisms of the community members could be explored further. While we explain the observed phenomena using appropriate theory,<sup>12</sup> in-depth interviews with community members can further strengthen the conceptual foundation of the research.

Fourth, the methodological approach of quasi-experiment has its limitations. Quasiexperiments are observational studies where the researchers are unable to manipulate the stimuli or provide random assignment of groups. This restricts the claim of causal linkage between recognition and contribution behavior. To strengthen the causal claim, future research may use <sup>fi</sup>eld experiments. Fifth, the dataset we used had details about members and reviews on local businesses in 10 metropolitan areas, which may somewhat limit the generalizability of the study. Although this covers a much larger number of cities (16005 unique postal codes) within these 10 areas, a variety of businesses, and many reviews and reviewers, we must generalize our results with caution. This limitation could be addressed for this speci<sup>fi</sup>c website if access is provided to data from all the cities where Yelp operates.

## Conclusion

Many online review communities incentivize reviewers through recognition systems, the e<sup>f</sup>ectiveness of which has not been comprehensively scrutinized. In this paper, we study the e<sup>f</sup>ect of repeated administrations of community recognition on contribution behavior in online review communities. We <sup>fi</sup>nd that recognition acts as a positive social reinforcer and leads to an increase in contribution e<sup>f</sup>ort and quantity. However, on repeated recognition, reinforcer satiation comes into play, resulting in a decrease in contribution behavior. Furthermore, consistent with the equity theory, we <sup>fi</sup>nd that deserving contributors when left unrecognized are demotivated and display a signi<sup>fi</sup>cant decline in contribution behavior. Additional analysis on contribution quality revealed that it increases for repeatedly recognized members, but interestingly does not decrease for unrecognized members. The <sup>fi</sup>ndings and insights shared in this paper o<sup>f</sup>er important research and practical implications. Developers and managers of online review communities could use the insights to e<sup>f</sup>ectively design their recognition systems to elicit more and better reviews. With the increased reliance on electronic word-of-mouth and online reviews, this study serves as a basis for future research in this area.

## Notes

1. https://www.yelp.com/factsheet

2. https://www.brightlocal.com/learn/local-consumer-review-survey/

3. Anecdotal evidence from postings on sites such as Yelp suggest that a number of members perceive they should have received Elite status based on their contributions, but did not do so. e.g., https://www.yelp.com/topic/san-jose-how-to-become-an-elite-yelper

4. https://www.yelp-support.com/article/What-is-Yelps-Elite-Squad?l=en\_US

5. Tips are usually single-topic nuggets of information regarding local businesses shared by Yelpers. In Yelp, reviews are expected to be more detailed, with the aim of sharing one’s opinion or feedback, whereas tips are one/two-liners and focus on some speci<sup>fi</sup>c information about the business that could be of help to potential customers.

6. Anecdotal evidence for this issue can be found in various comments from Yelpers on di<sup>f</sup>erent community sites e.g., https://www.yelp.com/topic/san-jose-how-to-become-an-elite-yelper

7. https://www.yelp.com/dataset/challenge

8. We did a baseline comparison to ensure that the decline in contribution e<sup>f</sup>ort and quantity for the repeatedly recognized group is signi<sup>fi</sup>cant as compared to a natural decline in contribution behaviour over time for members in online communities in general. We found that the declining slope from 2015-2017 for the repeatedly recognized group (di<sup>f</sup>erence in e<sup>f</sup>ort: -51.55; di<sup>f</sup>erence in quantity: -31.53) did not change signi<sup>fi</sup>cantly (became di<sup>f</sup>erence in e<sup>f</sup>ort: -50.05; di<sup>f</sup>erence in quantity: -30.70) even after accounting for the baseline decline in contribution behavior for the full sample in the same period. Thus, our results for H2a and H2b are robust, even with the baseline comparison.

9. Please note that the coe<sup>fi</sup>cients a0, b0, b1, b2 are just provided for representation purpose. We do not intend to imply that the coe<sup>fi</sup>cients would be the same for each equation.

10. Prior to conducting the Durbin-Wu-Hausman test, we ran a logistic regression to check whether all 5 matching parameters/variables in year 2014 signi<sup>fi</sup>cantly contributed to predicting Elite status in 2015. The results showed that the review-related variables were signi<sup>fi</sup>cant predictors of Elite status, while the tips-related variables were not.

11. There are two other possible scenarios that we did not report here. First, for the R, R, NR condition, the sample size was too small (N=2) and hence not included. Second, for the NR, NR, R condition, the results were materially the same as for any of the <sup>fi</sup>rst-time recognition conditions. Finally, the R, R, R condition is already included in our main hypotheses, H2a and H2b.

12. To validate our proposed theoretical explanations, we carried out a small-scale survey of Yelp reviewers (12 respondents) with a few open-ended questions about their reaction to multiple recognitions and to lack of recognition. The responses largely agreed with our explanations.

## Acknowledgement

The research was supported in part by a Category I research grant from the Indian Institute of Management Calcutta with the work order number RP:ITRRLROCC/3809/2019-20.

## References

1. Adams, J.S. Toward an understanding of inequity. Journal of Abnormal and Social Psychology, 67, (1963), 422–436.

2. Adams, J.S. Inequity in social exchange. Advances in Experimental Social Psychology, 2, (1965), 267–299.

3. Ambrose, M.L.; and Kulik, C.T. Old friends, new faces: Motivation research in the 1990s. Journal of Management, 25, 3 (1999), 231–292.

4. Anzai, Y.; and Simon, H.A. The theory of learning by doing. Psychological Review, 86, 2 (1979), 124–140.

5. Arazy, O.; Nov, O.; Patterson, R.; and Yeo, L. Information quality in Wikipedia: the e<sup>f</sup>ects of group composition and task con<sup>fl</sup>ict. Journal of Management Information Systems, 27, 4 (2011), 71–98.

6. Balestra, M.; Zalmanson, L.; Cheshire, C.; Arazy, O.; and Nov, O. It was fun, but did it last?: The dynamic interplay between fun motives and contributors’ activity in peer production. In Proceedings of the ACM on Human-Computer Interaction. 2017, p. 21.

7. Brun, J.P.; and Dugas, N. An analysis of employee recognition: Perspectives on human resources practices. The International Journal of Human Resource Management, 19, (2008), 716–730.

8. Burtch, G.; Hong, Y.; Bapna, R.; and Griskevicius, V. Stimulating online reviews by combining <sup>fi</sup>nancial incentives and social norms. Management Science, 64, 5 (2018), 2065–2082.

9. Butler, B.; Sproull, L.; Kiesler, S.; and Kraut, R. Community e<sup>f</sup>ort in online groups: who does the work and why. Leadership at a Distance: Research in Technologically Supported Work, 1, (2002), 171–194.

10. Cabral, L.; and Li, L. A dollar for your thoughts: feedback-conditional rebates on eBay. Management Science, 61, 9 (2015), 2052–2063.

11. Campbell, D.T.; and Riecken, H.W. Quasi-experimental design. International Encyclopedia of the Social Sciences, 5, (1968), 259–263.

12. Carrell, M. Equity theory. In F.M. Moghaddam (ed.), The SAGE Encyclopedia of Political Behavior. Thousand Oaks: SAGE, 2017, pp. 258–261.

13. Chan, C.M.L.; Bhandar, M.; Oh, L.-B.; and Chan, H.-C. Recognition and participation in a virtual community. In Proceedings of the 37th Annual Hawaii International Conference on System Sciences. 2004, pp. 1–10.

14. Chen, H.; Hu, Y.J.; and Huang, S. Monetary incentive and stock opinions on social media. Journal of Management Information Systems, 36, 2 (2019), 391–417.

15. Chen, J.; Xu, H.; and Whinston, A.B. Moderated online communities and quality of user-generated content. Journal of Management Information Systems, 28, 2 (2011), 237–268.

16. Chen, W.; Wei, X.; and Zhu, K. Engaging voluntary contributions in online communities: a hidden Markov model. MIS Quarterly, 42, 1 (2017), 83–100.

17. Chiu, C.-M.; Hsu, M.-H.; and Wang, E.T.G. Understanding knowledge sharing in virtual communities: an integration of social capital and social cognitive theories. Decision Support Systems, 42, 3 (2006), 1872–1888.

18. Chou, E.Y.; Lin, C.Y.; and Huang, H.C. Fairness and devotion go far: integrating online justice and value co-creation in virtual communities. International Journal of Information Management, 36, 1 (2016), 60–72.

19. Davidson, R.; and MacKinnon, J.G. Estimation and Inference in Econometrics. Oxford: Oxford University Press, 1993.

20. Dellarocas, C. Online reputation systems: how to design one that does what you need. MIT Sloan Management Review, 51, 3 (2010), 33.

21. Durcikova, A.; and Gray, P. How knowledge validation processes a<sup>f</sup>ect knowledge contribution. Journal of Management Information Systems, 25, 4 (2009), 81–108.

22. Erickson, M.T. E<sup>f</sup>ects of social deprivation and satiation on verbal conditioning in children. Journal of Comparative and Physiological Psychology, 55, 6 (1962), 953–957.

23. Fahey, R.; Vasconcelos, A.C.; and Ellis, D. The impact of rewards within communities of practice: a study of the SAP online global community. Knowledge Management Research & Practice, 5, 3 (2007), 186–198.

24. Feng, Y.; and Ye, H.J. Why do you return the favor in online knowledge communities? A study of the motivations of reciprocity. Computers in Human Behavior, 63, (2016), 342–349.

25. Fradkin, A.; Grewal, E.; Holtz, D.; and Pearson, M. Bias and reciprocity in online reviews: evidence from <sup>fi</sup>eld experiments on Airbnb. In Proceedings of the Sixteenth ACM Conference on Economics and Computation. New York, 2015, pp. 641–641.

26. Gallus, J. Fostering public good contributions with symbolic awards: a large-scale natural <sup>fi</sup>eld experiment at Wikipedia. Management Science, 63, 12 (2017), 3999–4015.

27. Gallus, J.; and Frey, B.S. Awards: a strategic management perspective. Strategic Management Journal, 37, 8 (2016), 1699–1714.

28. Garnefeld, I.; Iseke, A.; and Krebs, A. Explicit incentives in online communities: boon or bane? International Journal of Electronic Commerce, 17, 1 (2012), 11–38.

29. Gewirtz, J.L.; and Baer, D.M. Deprivation and satiation of social reinforcers as drive conditions. Journal of Abnormal and Social Psychology, 57, 2 (1958), 165–172.

30. Ghose, A.; and Ipeirotis, P.G. Designing ranking systems for consumer reviews: the impact of review subjectivity on product sales and review quality. In Proceedings of the 16th Annual Workshop on Information Technology and Systems. 2006, pp. 303–310.

31. Gneezy, U.; Meier, S.; and Rey-Biel, P. When and why incentives (don’t) work to modify behavior. Journal of Economic Perspectives, 25, 4 (2011), 191–210.

32. Goes, P.B.; Guo, C.; and Lin, M. Do incentive hierarchies induce user e<sup>f</sup>ort? Evidence from an online knowledge exchange. Information Systems Research, 27, 3 (2016), 497–516.

33. Hamari, J. Do badges increase user activity? a <sup>fi</sup>eld experiment on the e<sup>f</sup>ects of gami<sup>fi</sup>cation. Computers in Human Behavior, 71, (2017), 469–478.

34. Hausman, J.A. Speci<sup>fi</sup>cation tests in Econometrics. Econometrica, 46, 6 (1978), 1251–1271.

35. Hennig-Thurau, T.; Gwinner, K.P.; Walsh, G.; and Gremler, D.D. Electronic word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate themselves on the Internet? Journal of Interactive Marketing, 18, 1 (2004), 38–52.

36. Hicks, A.; Comp, S.; Horovitz, J.; Hovarter, M.; Miki, M.; and Bevan, J.L. Why people use Yelp.com: an exploration of uses and grati<sup>fi</sup>cations. Computers in Human Behavior, 28, 6 (2012), 2274–2279.

37. Hsu, M.H.; Ju, T.L.; Yen, C.H.; and Chang, C.M. Knowledge sharing behavior in virtual communities: the relationship between trust, self-e<sup>fi</sup>cacy, and outcome expectations. International Journal of Human Computer Studies, 65, 2 (2007), 153–169.

38. Jin, J.; Li, Y.; Zhong, X.; and Zhai, L. Why users contribute knowledge to online communities: an empirical study of an online social Q&A community. Information & Management, 52, 7 (2015), 840–849.

39. Johnson, B. Toward a new classi<sup>fi</sup>cation of nonexperimental quantitative research. Educational Researcher, 30, 2 (2001), 3–13.

40. Kankanhalli, A.; Tan, B.C.; and Wei, K.K. Contributing knowledge to electronic knowledge repositories: an empirical investigation. MIS Quarterly, 29, 1 (2005), 113–143.

41. Khansa, L.; Ma, X.; Liginlal, D.; and Kim, S.S. Understanding members’ active participation in online Question-and-Answer communities: a theory and empirical analysis. Journal of Management Information Systems, 32, 2 (2015), 162–203.

42. Khern-am-nuai, W.; Kannan, K.; and Ghasemkhani, H. Extrinsic versus intrinsic rewards for contributing reviews in an online platform. Information Systems Research, 29, 4 (2018), 871–892.

43. Kohn, A. Why incentive plans cannot work. Harvard Business Review, 1993, 54–63.

44. Kuang, L.; Huang, N.; Hong, Y.; and Yan, Z. Spillover e<sup>f</sup>ects of <sup>fi</sup>nancial incentives on non-incentivized user engagement: evidence from an online knowledge exchange platform. Journal of Management Information Systems, 36, 1 (2019), 289–320.

45. Lampel, J.; and Bhalla, A. The role of status seeking in online communities: giving the gift of experience. Journal of Computer-Mediated Communication, 12, 2 (2007), 100–121.

46. Li, Z.; Huang, K.; and Cavusoglu, H. Quantifying the impact of badges on user engagement in online Q&A communities. In Proceedings of Thirty Third International Conference on Information Systems. Orlando, 2012, pp. 1–10.

47. Liu, L.; Yin, C.; and Yang, J. Understanding user intention to share information in online social shopping communities: the moderating e<sup>f</sup>ect of community equity. In Pacific Asia Conference on Information Systems. Chengdu, China, 2014, p. 323.

48. Liu, Z.; and Park, S. What makes a useful online review? Implication for travel product websites. Tourism Management, 47, (2015), 140–151.

49. Lou, J.; Fang, Y.; Lim, K.H.; and Peng, J.Z. Contributing high quantity and quality knowledge to online Q&A communities. Journal of the American Society for Information Science and Technology, 64, 2 (2013), 356–371.

50. Luca, M.; and Zervas, G. Fake it till you make it: reputation, competition, and Yelp review fraud. Management Science, 62, 12 (2016), 3412–3427.

51. Luthans, F.; and Kreitner, R. Organizational Behavior Modification and Beyond. Scott Foresman & Co.:, 1985.

52. McAdams, J.L. Nonmonetary rewards: cash equivalents and tangible awards. In L.A. Berger and D.R. Berger (eds.), The Compensation Handbook: A State-of-the-art Guide to Compensation Strategy and Design. New York: McGraw-Hill, 1999, pp. 241–260.

53. McSweeney, F.K. Dynamic changes in reinforcer e<sup>f</sup>ectiveness: satiation and habituation have di<sup>f</sup>erent implications for theory and practice. Behavior Analyst, 27, 2 (2004), 171–188.

54. Naylor, J.; Pritchard, R.; and Ilgen, D. A Theory of Behavior in Organizations. New York: Academic Press, 2013.

55. Neckermann, S.; Cueni, R.; and Frey, B.S. Awards at work. Labour Economics, 31, (2014), 205–217.

56. Ngo-Ye, T.L.; and Sinha, A.P. The in<sup>fl</sup>uence of reviewer engagement characteristics on online review helpfulness: a text regression model. Decision Support Systems, 61, 1 (2014), 47–58.

57. Nov, O.; Arazy, O.; and Anderson, D. Scientists@Home: what drives the quantity and quality of online citizen science participation? PLoS ONE, 9, 4 (2014), e90375.

58. Okoli, C.; and Oh, W. Investigating recognition-based performance in an open content community: a social capital perspective. Information & Management, 44, 3 (2007), 240–252.

59. Otterbacher, J. “Helpfulness” in online communities: a measure of message quality. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. Boston: ACM, 2009, pp. 1–10.

60. Phang, C.W.; Kankanhalli, A.; and Huang, L. Drivers of quantity and quality of participation in online policy deliberation forums. Journal of Management Information Systems, 31, 3 (2014), 172–212.

61. Pritchard, R.D.; Dunnette, M.D.; and Gorgenson, D.O. E<sup>f</sup>ects of perceptions of equity and inequity on worker performance and satisfaction. Journal of Applied Psychology, 56, 1 (1972), 75–94.

62. Reimer, T.; and Benkenstein, M. Altruistic eWOM marketing: more than an alternative to monetary incentives. Journal of Retailing and Consumer Services, 31, (2016), 323–333.

63. Richardson, K.M. Reinforcement theory. In E.H. Kessler (ed.), Encyclopedia of Management Theory. Thousand Oaks: SAGE, 2013, pp. 655–660.

64. Rosenbaum, P.R. Optimal matching for observational studies. Journal of the American Statistical Association, 84, 408 (1989), 1024–1032.

65. Schuckert, M.; Liu, X.; and Law, R. Stars, votes, and badges: how online badges a<sup>f</sup>ect hotel reviewers. Journal of Travel and Tourism Marketing, 33, 4 (2016), 440–452.

66. Shen, W.; Hu, Y. (J.); and Ulmer, J.R. Competing for attention: an empirical study of online reviewers’ strategic behavior. MIS Quarterly, 39, 3 (2015), 683–696.

67. Skinner, B.F. Science and Human Behavior. Simon and Schuster, New York, 1953.

68. Stajkovic, A.D.; and Luthans, F. Di<sup>f</sup>erential e<sup>f</sup>ects of incentive motivators on work performance. Academy of Management Journal, 44, 3 (2001), 580–590.

69. Stajkovic, A.D.; and Luthans, F. Behavioral management and task performance in organizations: conceptual background, meta-analysis, and test of alternative models. Personnel Psychology, 56, 1 (2003), 155–194.

70. Stephen, A.; Bart, Y.; Plessis, D.; and Goncalves, D. Does paying for online product reviews pay o<sup>f</sup>? The e<sup>f</sup>ects of monetary incentives on content creators and consumers. Advances in Consumer Research, 40, (2012), 228–231.

71. Sun, Y.; Dong, X.; and McIntyre, S. Motivation of user-generated content: social connectedness moderates the e<sup>f</sup>ects of monetary rewards. Marketing Science, 36, 3 (2017), 329–337.

72. Sundaram, D.S.; Mitra, K.; and Webster, C. Word-of-mouth communications: a motivational analysis. Advances in Consumer Research, 25, (1998), 527–531.

73. Tang, Q.; Gu, B.; and Whinston, A.B. Content contribution for revenue sharing and reputation in social media: a dynamic structural model. Journal of Management Information Systems, 29, 2 (2012), 41–76.

74. Tyagi, P.K. Inequities in organizations, salesperson motivation and job satisfaction. International Journal of Research in Marketing, 7, 2–3 (1990), 135–148.

75. Velichety, S.; Ram, S.; and Bockstedt, J. Quality assessment of peer-produced content in knowledge repositories using development and coordination activities. Journal of Management Information Systems, 36, 2 (2019), 478–512.

76. Warren, V.L.; and Cairns, R.B. Social reinforcement satiation: an outcome of frequency or ambiguity? Journal of Experimental Child Psychology, 13, 2 (1972), 249–260.

77. Wasko, M.M.; and Faraj, S. Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS Quarterly, 29, 1 (2005), 35–57.

78. Wei, X.; Chen, W.; and Zhu, K. Motivating user contributions in online knowledge communities: virtual rewards and reputation. In Proceedings of the 48th Hawaii International Conference on System Sciences. IEEE, 2015, pp. 3760–3769.

79. Yoo, K.H.; and Gretzel, U. What motivates consumers to write online travel reviews? Information Technology & Tourism, 10, 4 (2008), 283–295.

## About the Authors

<sup>Samadrita</sup> <sup>Bhattacharyya</sup> (samadritab14@iimcal.ac.in) is a doctoral student of Management Information Systems at the Indian Institute of Management Calcutta. She holds an M.Tech in VLSI Design from Indian Institute of Engineering Science and Technology, Shibpur. Her research interests include social commerce, online reviews, social networks, business analytics, optimization, and algorithms. Her research articles have appeared in Decision Support Systems, Information & Management, and the proceedings of Australasian Conference on Information Systems, Hawaii International Conference on System Sciences, and IEEE.

<sup>Shankhadeep</sup> <sup>Banerjee</sup> (shankhadeepb15@iimcal.ac.in) is a doctoral student of Management Information Systems at the Indian Institute of Management Calcutta. He holds an MBA from that school. His research focus on the human related to crowdfunding, online reviews, virtual communities, e-tailing, and other contemporary technologies. He has extensive practitioner experience working at top technology <sup>fi</sup>rms, including Microsoft, Amazon, and eBay. His publications have appeared in Decision Support Systems, Information & Management, and the proceedings of International Conference on Information Systems and Australasian Conference on Information Systems.

<sup>Indranil</sup> <sup>Bose</sup> (bose@iimcal.ac.in; corresponding author) is Professor of Management Information Systems at the Indian Institute of Management Calcutta. He holds a Ph.D. from Purdue University. His research interests focus on business analytics, digital transformation, information security, and management of innovation. His publications have appeared in MIS Quarterly, Communications of the ACM, Decision Support Systems, Information & Management, European Journal of Operational Research, Communications of the AIS, Journal of Organizational Computing and Electronic Commerce, among others. He serves as Senior Editor of Decision Support Systems and as Associate Editor of Communications of the AIS, Journal of the AIS, and Information & Management.

<sup>Atreyi Kankanhalli</sup> (atreyi@comp.nus.edu.sg) is Provost's Chair Professor and Deputy Head in the Department of Information Systems and Analytics at the National University of Singapore (NUS). She is the Coordinator of the Service Systems Innovation Research Laboratory at NUS. She has been a visiting scholar at UC Berkeley, London School of Economics and Political Science, and ESSEC Business School. Her research interests are in the areas of online communities and digital collaboration, and digital innovation and transformation (particularly in public and healthcare sectors). Her publications have appeared in premium journals such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, and Research Policy, among others. She has received several awards and is serving or has served on the board of MIS Quarterly and Information Systems Research.
