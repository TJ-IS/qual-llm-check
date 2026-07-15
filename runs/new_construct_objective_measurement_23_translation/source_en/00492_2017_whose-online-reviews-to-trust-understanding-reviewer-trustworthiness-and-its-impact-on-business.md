---
otero_id: 492
otero_key: "UHPKF9MA"
title: "Whose online reviews to trust? Understanding reviewer trustworthiness and its impact on business"
authors: "Shankhadeep Banerjee; Samadrita Bhattacharyya; Indranil Bose"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.01.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Whose online reviews to trust? Understanding reviewer trustworthiness and its impact on business

Shankhadeep Banerjee, Samadrita Bhattacharyya, Indranil Bose

Indian Institute of Management Calcutta, India

## a r t i c l e i n f o

Article history: Received 20 August 2016 Received in revised form 26 November 2016 Accepted 21 January 2017 Available online 27 January 2017

Keywords: Online reviews Predictive model Regression analysis Reviewer characteristics Trustworthiness Yelp Electronic word-of-mouth Online reviewers Online trust

## a b s t r a c t

Why do top movie reviewers receive invitations to exclusive screenings? Even popular technology bloggers get free new gadgets for reviewing. How much do these reviewers really matter for businesses? While the impact of online reviews on sales of products and services has been well established, not much literature is available on impact of reviewers for businesses. Source credibility theory expounds how a communication's persuasiveness is affected by the perceived credibility of its source. So, perceived trustworthiness of reviewers should influence acceptance of reviews, and consequently should have an indirect impact on sales. Using local business review data from Yelp.com, this paper successfully tests the premise that reviewer trustworthiness positively moderates the impact of review-based online reputation on business patronages. Given the importance of reviewer trustworthiness, the next logical question is – how to estimate and predict it, if no direct proxy is available? We propose a theoretical model with several reviewer characteristics (positivity, involvement, experience, reputation, competence, sociability) affecting reviewer trustworthiness, and find all factors to be significant using the robust regression method. Further, using these factors, a predictive classification of reviewers into high and low level of potential trustworthiness is done using logistic regression with nearly 83% accuracy. Our findings have several implications - firstly, businesses should focus on building a good review-based online reputation; secondly, they should encourage top trustworthy reviewers to review their products and services; and thirdly, trustworthy reviewers could be identified and ranked using reviewer characteristics.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

The Internet has transformed the way consumers can decide to purchase a product or avail services of a business. Before the advent of the Internet, consumers either trusted word-of-mouth from acquaintances, or just used information provided by the seller to make a buy/no-buy decision. However, a third option has been created with the proliferation of online review sites which offer easy access to electronic wordof-mouth (eWOM) from peer consumers. eWOM can be defined as “any positive or negative statement made by potential, actual, or former customers about a product or company, which is made available to a multitude of people and institutions via the Internet” [1]. A plethora of websites like Amazon, Yelp, Glassdoor, IMDB, etc. allow peer-evaluated reviews for products, local businesses, employers, movies, etc., respectively. Internet users routinely access online reviews to obtain product information before purchasing [2], and a significant portion of these consumers report that they are influenced by online reviews in their decision-making [3]. According to BrightLocal Local Consumer Review

Survey 2016 [4], 91% of US-based respondents have read online reviews to determine the quality of a local business. Thus, it can be expected that online reviews will have a significant impact on sales of products and services. This has been conclusively established multiple times in extant research on eWOM [5–7]. In the context of local businesses, the online reviewer communities have been found to add significantly to their revenues; for example, the average annual revenue from Yelp.com as reported by paid business accounts in a 2012 survey was US\$ 23,000 [8]. In certain categories like Home, the revenue was reported to be much higher at US\$ 54,000. Even opening a free business account on Yelp without any spending on advertising added an average annual revenue of US\$ 8000 to the local businesses. Other studies have directly linked Yelp ratings with revenue, such as a one-star increase in Yelp ratings was found to trigger 5–9% increase in revenue at restaurants [9]. So overall, it can be concluded that online reviewers do play an important role in influencing new customers in making purchase-related decisions.

While there is no doubt regarding the overall importance of online reviews and reviewer communities at large, at a micro level not all individual reviews can have equal impact on consumers for making purchase-related decisions. Using feedback mechanisms on reviews like helpfulness votes, it has been observed that some reviews are more accepted and appreciated by readers than others. Reviews which are considered more helpful have been found to have a greater influence on customers' purchase decisions in comparison to other reviews [10]. Research on eWOM has discovered several factors which have been found to significantly affect helpfulness or usefulness of a review. These include review length/depth (word count) and extremity (star rating) [11]; content and style [12]; readability [13]; reader's objectives [14]; subjectivity, informativeness, and linguistic correctness [15]; etc. However, one factor which gets comparatively lesser mention is the trustworthiness of a reviewer producing a review. In our daily lives, we value opinions of people we trust, much more than those of people we do not. Source credibility theory expounds how a communication's persuasiveness is affected by the perceived credibility of the source of communication. So, applying this theory in the context of eWOM, we can expect that acceptance of a review by a prospective customer should, to some extent, get affected by the perceived trust on the reviewer. Earlier studies have conceptualized product review helpfulness as a second-order formative construct manifested through perceived source credibility, and other content-related factors [16]. For instance, reviews that are written by self-described experts have been found to be more helpful than others [17]. Even just simple disclosure of identity information by reviewers in product reviews has been found to be positively associated with acceptance of reviews, subsequently followed by better sales [7]. Thus, there seems to be ample evidence pointing to the inherent need of eWOM readers to be able to know and trust the reviewers in order to accept their reviews. Since acceptance of a review can affect the decision of a customer either in favor of or against visiting a local business, overall patronages of the business should be indirectly affected by average trustworthiness of all reviewers reviewing it. While logically the argument holds well, we are not aware of any previous research till date which has validated the proposition for local businesses. Earlier attempts to test direct impact of top reviewers on product sales did not generate support for the proposed hypothesis owing to certain limitations of data [10]. Hence, for this paper we propose to take up this research question:

RQ1: Does overall trustworthiness of reviewers have any impact on the number of customers visiting the business being reviewed?

The managerial implication of investigating this question is that it may benefit businesses by helping them focus on identifying and targeting the most trustworthy reviewers, and encouraging them to review their products and services. This idea is very similar to the popular practice of top movie critics getting exclusive invitations to premier screenings for writing reviews, or technology companies sending new gadgets to technology bloggers for their expert public reviews. But what we are suggesting is to make the practice more widespread if the impact of reviewer trustworthiness on business patronages is found to be significant.

Assuming that reviewer trustworthiness is found to have an impact on business patronages, the next logical step will be to find a way to identify the trustworthy reviewers. Some online review sites like Yelp allows one to follow reviewers one perceives to be trustworthy, therefore the number of followers of a reviewer can be a good measure of reviewer trustworthiness. However, most websites do not offer such possibilities. In such cases, the only way will be to look into some of the available reviewer profile characteristics, and try to predict the level of trustworthiness. Xu [18] has found that these profile characteristics act as cues of source trustworthiness and play an important role in consumer decision making. An extension of source credibility theory by McCroskey and Jenson [19] identify five source characteristics which can affect credibility – competence, character, sociability, composure, and extroversion. However, this has never been applied in the context of online reviews till date. So we do not know if these dimensions hold true for faceless online reviewers about whom very little personal information is shared on review sites. With the objective of trying to develop a predictive model for reviewer trustworthiness using reviewer characteristics, the following research question is also proposed:

RQ2: Which reviewer characteristics determine the trustworthiness of a reviewer?

To find answers to the two research questions, a dataset from Yelp. com is used, which contains reviews by consumers for over 77K local businesses across multiple cities in four countries. The data includes attributes on reviewers, businesses, reviews, and check-ins (customer visiting a business), and hence is ideal for conducting this research. The number of check-ins is used as a proxy for business patronages, and average star ratings multiplied by review count is used as a proxy for online reputation of a business. We find that reviewer trustworthiness measured in terms of number of followers of reviewers, has a positive moderating effect on the relationship between online reputation and patronages of a business. This means that while better online reputation is associated with better patronages, the relationship can be further boosted if the reviewers are more trustworthy, as compared to if they are less so. Furthermore, we take help from McCroskey's research and published literature on eWOM to identify six reviewer attributes (competence, experience, sociability, reputation, involvement, and positivity) which could be hypothesized to influence trustworthiness in the context of a reviewer community. The proxy measures of these attributes are used as independent variables, and with trustworthiness as a dependent variable, a robust regression analysis is done to identify the significant factors. Finally, a logistic regression model is built to classify reviewers into ‘high’ or ‘low’ level of trustworthiness. Our results show a classification accuracy of nearly 83% implying that the model is a pretty good predictor of reviewer trustworthiness.

Overall, this paper makes relevant contributions to literature, being the first paper (to the best of our knowledge, till date) to establish a link between trustworthiness of reviewers and business patronages. It is also one of the few works to identify and empirically validate several reviewer characteristics which can influence trustworthiness. Furthermore, the predictive model developed in this paper can be customized and used by businesses to identify trustworthy reviewers when direct information about reviewers is unavailable. Even online review sites can use it to recommend most trustworthy reviewers and their reviews to the users. Apart from practical utility, the findings from this paper have significant managerial implications for businesses as well. Firstly, businesses can focus on building a good review-based online reputation; secondly, they can encourage top trustworthy reviewers to review their products and services; and thirdly, trustworthy reviewers can be identified and ranked using reviewer-related characteristics.

## 2. Literature review

Most of the eWOM literature has focused either on finding factors associated with helpfulness of reviews [15,16,20–24], or on discovering the impact of reviews on sales [7,15,25–28]. There are several studies which give importance to reviewers mostly in the context of influencing the helpfulness of reviews [15,17,18,28–32]. For the propositions related to how reviewers influence sales, mixed results have been found. One study [9] has shown a significant positive impact of reviewers certified as ‘Elite’ in Yelp on business sales whereas another study [10] has not found any significant impact of rankings of reviewers on the sales related ranks of products at Amazon.

However, there are only few studies speci c to reviewer trustworthiness. A study by Xu [18] adopts a 2 (number of trusted members: small, large) × 2 (profile picture: without, with) × 2 (review valence: negative, positive) between-participants experiment to explore how two personal profile characteristics, reputation cue and profile picture, influence cognitive trust and affective trust towards the reviewer and perceived review credibility respectively and in a combinatorial manner. The findings of the study have shown that reputation cue and profile picture cue contributes differently to users' affective trust and cognitive trust towards the reviewer. Reputation cue that is generated by the system, is found to influence both affective and cognitive dimensions of trust, whereas the self-generated cue of profile picture only impacts affective trust. Reputation cue has a direct influence on perceived review credibility, whereas the influence of profile picture on perceived review credibility is dependent on review valence.

But overall the area of reviewer trustworthiness is not widely studied. Hence, RQ1 is a good question to start a series of investigations on the same theme. Also, factors influencing reviewer trustworthiness are only implied in eWOM literature, mainly in the context of review credibility and usefulness. Liu and Park [33] have found that the reviewer's expertise and reputation influence the perceived value of a review. Ghose and Ipeirotis [15] have studied the impact of average helpfulness votes received per review and personal information disclosure on helpfulness of review. Otterbacher [34] has found that reviewer characteristics like the number of reviews posted by a reviewer and the number of helpful votes received by the reviewer on the whole, impacts the helpfulness vote of a review. Liu et al. [35] has discovered that reviewer expertise and writing style have an impact on review helpfulness. Ngo-Ye and Sinha [31] have employed a reviewer”'s RFM (Recency, Frequency, Monetary Value) dimensions to characterize reviewer engagement and found that inclusion of these dimensions helps improve prediction of online review helpfulness. Some reviewer characteristics that are found to impact sales (through decrease in perceived uncertainty of buyers) are reviewer quality and reviewer exposure [28]. Another key finding related to reviewers is that reviews written by a self-described expert are more helpful than those that are not [17]. Shen et al. [36] have empirically examined how online reviewers' behaviors are driven by the desire to gain attention and online reputation.

While there exist research that study one or more of reviewer characteristics impacting review helpfulness, we have not found any study that has tried to find the impact of reviewer characteristics on reviewer trustworthiness or credibility. This may be because most studies have treated reviewer trust as an implicit mechanism through which review helpfulness is affected by reviewer characteristics, and hence ‘trust’ is mentioned only when explaining the results. Another reason can be the absence of a good proxy to measure reviewer trustworthiness when conducting empirical analysis. The closest relevant work that can be found is by Ku et al. [30] which has attempted to discriminate reviewers with a high reputation from those with a low reputation on the basis of their web trust network and review behaviors in Epinions.com. Their results have indicated that trust intensity, average trust intensity of trustors, degree of review focus in the target category, and average product rating in the target category, have successfully discriminated reviewers into the two groups. Ku et al. have considered reviewer reputation to be the dependent variable and have classified it as high/low based on the number of helpfulness votes received; whereas trust intensity of a reviewer has been measured by his/her centrality in the community trust network. This independent factor is found to be positively associated with reputation. However, it can be argued that average review helpfulness votes is not a good measure for reputation, but rather is a better indicator of reviewer competence or expertise in writing reviews. Also, reputation can be based on external certification as well, like being branded as ‘Elite Reviewer’ in case of Yelp.com. So it can be considered to be an independent variable. Thus, both competence and reputation can be treated as independent variables affecting reviewer trustworthiness. This is the approach we adopt and measure reviewer trustworthiness on the basis of the number of followers he/she has gained, as the dependent variable, and treat reviewer characteristics as independent variables.

The key literature related to online reviewers is summarized in Table 1 and shows the various relationships that have been studied in this context. Our study intends to cover the research gaps by establishing the appropriate relationship between reviewer impression (more specifically trustworthiness) and sales (or patronages); and also between a variety of reviewer related attributes and trustworthiness.

## 3. Hypotheses development

Academicians often confuse between the concepts of trust and trustworthiness, and hence most of the trust literature does not mention trustworthiness, even though most of the work relates to that [39]. Trust can be defined as “the willingness of a party to be vulnerable to the actions of another party based on the expectation that the other will perform a particular action important to the trustor, irrespective of the ability to monitor or control that other party” [40]. Thus, trust can be treated as a three-part relation where person X trusts person Y to do action A [41]. So, if Y is not able to do A, then X may lose trust on Y in doing A anymore, but Y still may be considered trustworthy by X. However, if Y betrays X in some way, then X will not consider Y to be trustworthy anymore, and hence may not trust Y even for other activities. So, trustworthiness of a person refers to how much the person is ‘deserving of trust’. Which means that trustworthiness begets trust through a causal connection [41]. If we extend the argument a bit further, trustworthiness of a person can also be a causal factor in deciding how much to trust his/her opinions on some matter. This is similar to what the Source Credibility Theory (SCT), a well-established theory in communication, also talks about.

According to the SCT, the persuasiveness of a communication is determined in part by the perceived credibility of the source of communication [42], and trustworthiness is the most influential dimension of source credibility [43]. So, if X is trying to persuade Y to take action A, then whether Y feels persuaded enough to do A or not, will depend to some extent on how much trustworthy Y considers X. SCT has been experimentally established by Hovland and Weiss [42] by presenting identical content to subjects using sources they consider having ‘high trustworthiness’ and ‘low trustworthiness’. They have found that the immediate reaction to ‘fairness’ of presentation and ‘justifiability’ of conclusions drawn by the sources have significantly depended on the subject's initial opinion on the matter, and his evaluation of trustworthiness of source. Opinions among audience are found to have changed immediately after communication by a ‘high trustworthy’ source, than when presented by a ‘low trustworthy’ source. However, no difference is found in the factual information being learned from the communication. Thus, the SCT deals with the opinions being affected, and not factual information, based on the perceived trustworthiness of the source of communication. Multiple studies have adopted the SCT in areas of persuasive marketing, brand building, and design of logos and websites [44].

Summary of key literature on online reviewers.

<table><tr><td>Relationship studied</td><td>Key literature</td></tr><tr><td>Reviewer attributes → Review acceptance</td><td>Average helpfulness votes received per review and personal information disclosure [15], Engagement (recency, frequency, monetary value) [31], Historical rating distribution [32], Expertise and reputation [33], Number of reviews and total helpful votes [34], Expertise and writing style [35]</td></tr><tr><td>Reviewer attributes → Sales</td><td>Quality and exposure [28], Certified elite [9]</td></tr><tr><td>Reviewer attributes → Reviewer impression</td><td rowspan="2">Reputation cue and profile picture [18], Review quality and reviewer photos [29], Centrality in trust network [30], Helpfulness votes [5-7]</td></tr><tr><td>Review acceptance → Sales</td></tr><tr><td>Reviewer impression → Review acceptance</td><td>Credibility [14,16,37]</td></tr><tr><td>Reviewer impression → Sales</td><td>Top ranked [10]</td></tr><tr><td>Others</td><td>Reviewers&#x27; strategic behaviors [36], Impact of ranking systems on reviewer well-being and engagement [38]</td></tr></table>

In the online context, trust plays an important role for customers in making purchase decisions since there is an information asymmetry between transacting parties. Earlier research models focused mostly on customer perceptions of the business and website, as well as consumer characteristics as the predictors of online trust. However, with the rise of social media, use of customer reviews has become a significant determinant of how trust builds up online [45]. According to the BrightLocal Local Consumer Survey 2016 [4], 84% of people trust online reviews as much as a personal recommendation, and 90% form their opinion about a business by reading less than 10 reviews. Online reviews are mostly personal opinions about products and services by peer customers, since most of the factual information is already mentioned in the item description. Thus, the SCT can apply well in the context of online reviews. It can indicate whether a customer trusts the reviews posted by a reviewer, and whether that depends on the perceived trustworthiness of the reviewer. This highlights the importance of reviewer trustworthiness in the context of online reviews, since trust and acceptance of a review's recommendation can lead a customer towards either a buy or no-buy decision, hence influencing the sales of the product or service.

Impact of online customer reviews on sales is a well-researched area [2,5,7,25–27]. So it is logical to expect that the characteristics and perceptions of the sources of reviews should also have some impact on sales [9,10,28]. However, the association may not be a straightforward positive relationship, since just having reviews written by more popular and trustworthy reviewers may not necessarily lead to higher sales or to more customers visiting a business. This is because reviewers can be writing negative comments which should adversely affect customers' intent to visit. So, it is ultimately the rating and review content that will directly affect patronages and consequently, overall sales volumes. But reviews, either positive or negative, from more trustworthy sources should be better accepted as compared to less trustworthy sources. A lot of research has been done to establish the association between source credibility and attitude towards content [46,47]. So, the positive association between review-based online reputation of business and its patronages will become stronger if the level of trustworthiness of reviewers is higher. Accordingly, we propose the following two hypotheses to empirically test our arguments, specifically in the context of local business reviews:

H1a. Review-based online reputation of a business is positively associ ated with the patronages generated by the business.

H1b. Average perceived trustworthiness of reviewers reviewing a business positively moderates the association between online reputation and patronages of the business.

For identifying reviewer characteristics that can affect trustworthiness, along with eWOM literature, we resorted to the classic work of McCroskey and Jenson [19] which has expounded five dimensions of source credibility. The dimensions are competence, character, sociability, composure, and extroversion, of which the first three are found to be more significant. Each dimension is further broken down into certain values (e.g., character dimension has values kindness, sympathy, selflessness, and virtue). For theory building, we have used some of these dimensions and values that seem appropriate in the context of reviewers, along with other factors identified in literature on eWOM that are found to affect helpfulness of review through latent trust on source of reviews. Accordingly, six hypotheses have been proposed.

Positivity among leaders has been found to impact followers' perceived trust and evaluation of leader's effectiveness [48]. McCroskey's character dimension also pointed to kindness and sympathy leading to more source credibility. In the online review context, these findings imply that reviewers with a tendency towards posting more sympathetic review with positive polarity in rating businesses, will be more trusted by other users. This is also proposed and verified by Fang et al. [32] using TripAdvisor data. They have found that reviewers who posted more reviews stressing the positive aspects are more likely to receive helpful votes than an author who stressed the negative aspects. In terms of star ratings, a higher average can be considered more positive and sympathetic leading to an increase in trustworthiness. This leads to the following hypothesis:

H2a. Reviewer's positivity in rating businesses is positively associated with the perceived reviewer trustworthiness.

Otterbacher [34] has found that the number of reviews posted by a reviewer is positively associated with the number of helpfulness votes received for the review. Liu and Park [33] too hypothesized number of reviews as one of the factors impacting review usefulness. So, it can be expected that an increase in the number of reviews, which is a measure of reviewer involvement in reviewing products or services, will be associated with an increase in trustworthiness of the reviewer. Hence, the following hypothesis is proposed:

H2b. The amount of reviewer's involvement in reviewing businesses is positively associated with the perceived reviewer trustworthiness.

Expertise dimension of source credibility refers to perceiving the source as trained, experienced, authoritative, skilled, and informed [43]. So one of the important aspects of source credibility is experience in the area under consideration. People with more experience in a field are generally more trusted than inexperienced ones in matters pertaining to that field. In the context of online reviews, experience will refer to the time period for which a reviewer has been a member of the online review community. We can expect reviewers with more years of experience in using the review site, to be more trusted and have more followers among the community as compared to newbies. Thus, this leads to the following hypothesis:

H2c. Reviewer's experience in online review website is positively associated with the perceived reviewer trustworthiness.

Liu and Park [33] have found that reviewer reputation affects the perceived value of a review. Consumers may infer credibility of reviewer directly from his reputation as suggested by the website or other members of community [18]. One of the values in McCroskey's competence dimension is qualification, which in the context of online reviews will be certification of being a good reviewer by the online review site. Being certified as ‘Elite’ reviewer in Yelp can be a good indicator of a reviewer's competence. It will also enhance a reviewer's reputation in the community. A quantifiable measure of reputation can be the total number of years a reviewer has been certified as ‘Elite’. It will be logical to expect that more the reputation of a reviewer, more will be the perceived trust on the reviewer. Thus, we propose the following hypothesis:

H2d. Reviewer's reputation in online review website is positively associated with the perceived reviewer trustworthiness.

A more competent reviewer will be able to write more useful reviews. Thus competence of a reviewer can be measured using average votes received per review by the reviewer. A competent source having more value is usually considered to be more credible, according to McCroskey's research. Ghose and Ipeirotis [15] too consider average helpfulness votes received by reviewer as one of the possible reviewer characteristics that may affect review helpfulness. Hence, it can be expected that reviewer's competence in writing useful reviews may affect reviewer trustworthiness. Thus, the following hypothesis is proposed:

H2e. Reviewer's competence in writing useful reviews is positively associated with the perceived reviewer trustworthiness.

Sociability is one of the critical dimensions of source credibility according to McCroskey. One of the key values of sociability is friendliness.

In the context of social networks, friendliness can be quantified using the number of friends a person is connected to in the community. So this will imply that number of friends a reviewer has in the community will be positively associated with the credibility of the reviewer. Liu and Park [33] have used the number of friends as one of the variables and tested its effect on usefulness of reviews. So the following hypothesis is proposed:

H2f. Reviewer's sociability as perceived by other users of a review website is positively associated with the perceived reviewer trustworthiness.

A visual representation of the proposed model with all the hypotheses is presented in Fig. 1. Operationalization of constructs used in the hypotheses is provided in Table 2. Review length, commonly known to significantly influence the helpfulness of reviews [11], is being used as a control variable to isolate the influence of reviewer characteristics from review characteristics upon reviewer trustworthiness. Similarly, business category and location as business characteristics are introduced as control variables examining their possible impact on business patronages.

A possible concern regarding the operationalization of constructs could be on the use of number of followers to measure reviewer trustworthiness. While ‘trust’ might be a major factor in causing an online user to follow other members in a community, other factors like social exchange and profile attractiveness can also play a significant role. However, Yelp provides a special context in which the number of followers can be justified to be a good proxy for measuring reviewer trustworthiness. In Yelp, the identities of followers are not revealed to the reviewers, hence restricting the mutual exchange factor. Also, Yelp provides options to ‘friend’ each other to connect on a social basis, and ‘compliment’ others, to praise reviewers for their pictures, posts, etc.

Table 2  
Constructs and measuring variables.

<table><tr><td>Constructs</td><td>Measuring variables</td></tr><tr><td>Business patronages</td><td>Total number of check-ins</td></tr><tr><td>Review-based online reputation of business</td><td>Average business rating * Number of reviews</td></tr><tr><td>Trustworthiness of reviewer</td><td>Number of followers</td></tr><tr><td>Positivity</td><td>Average review rating</td></tr><tr><td>Involvement</td><td>Number of reviews written</td></tr><tr><td>Experience</td><td>Number of years in Yelp</td></tr><tr><td>Reputation</td><td>Number of years as ‘Elite’ reviewer</td></tr><tr><td>Competence</td><td>Average number of review helpfulness votes received per review</td></tr><tr><td>Sociability</td><td>Number of friends</td></tr></table>

These limit the profile attractiveness factor for following a reviewer. Given the fact that Yelp is primarily a utility-based community where members would like to get really credible reviews, following someone's reviews anonymously would mostly be an indication of trust on the reviewer and his/her opinions. Thus, we use followership in Yelp as an approximate measure of reviewer trustworthiness.

## 4. Data

A large dataset was collected from Yelp.com which has been made public as a part of the Yelp Dataset Challenge. The dataset had 2.2 million reviews of 77,000 local businesses in several cities from countries like Germany, UK, USA, and Canada. Data of about 525,000 users who visited the businesses and reviewed them were also available. The analysis required business level data to test hypotheses H1a and H1b. We used business level attributes, total check-ins, average rating, and number of reviews in our analysis. We also computed average number of followers of the reviewers of each business by combining business data and user data. Average number of followers of the reviewers of businesses was used as a measure of reviewer trustworthiness. Table 3 shows the descriptive statistics of the variables used. Initially we considered 77,445 observations for business level analysis. After cleaning the data by removing the outliers and missing values, we ended up with 53,902 records for our first level of analysis.

![](/api/attachments/UHPKF9MA/fulltext/images/3af1b369418f5b9f4ea7d2f577b68dbce763da398789066c49664f0b56abd4b8.jpg)  
Fig. 1. Theoretical model on reviewer trustworthiness

Table 3  
Descriptive statistics of the variables used for testing hypotheses H1a–H1b.

<table><tr><td>Variable</td><td>Range</td><td>Mean</td><td>SD</td></tr><tr><td>Average number of followers</td><td>0–68</td><td>7.39</td><td>9.58</td></tr><tr><td>Average business rating * Number of reviews</td><td>3–1252</td><td>114.06</td><td>173.81</td></tr><tr><td>Total number of check-ins</td><td>3–1860</td><td>101.74</td><td>191.89</td></tr></table>

To test the second part of our analysis, i.e., hypotheses H2a through H2f a user dataset with 552,339 initial observations was used. User attributes such as number of followers, number of friends, average review rating, number of reviews written, total votes per user, years of experience, and years of reputation were used for the analysis. Average length of reviews written by users was used as a control variable. After preprocessing the data set, i.e., removal of outliers and missing records, we ended up with 69,612 records. Table 4 shows the descriptive statistics of the sample data.

## 5. Analysis and results

In the first part of our analysis we tested the moderating effect of reviewer trustworthiness on the effect of online reputation of a business on its patronages. We used average number of followers of the reviewers who reviewed a business as a proxy of reviewer trustworthiness and total number of check-ins for a business as a proxy for patronages. To measure online reputation of a business we calculated the product of average business rating and the number of reviews a business (average business rating ∗ number of reviews) received over the years. We introduced an interaction variable, product of average number of followers and (average business rating ∗ number of reviews) to take into account the moderation effect [49]. We used a log transformation of the variables to adjust for skewness [50]. We also controlled for the effect of business category and location (city) by including dummy variables representing category and city in our model. The dummy variable City Code takes binary values 0 for Las Vegas and 1 for Phoenix. We considered Las Vegas and Phoenix in our analysis as these two cities appeared in the data set the most number of times. Also, the cities were located in different states of the US. The purpose was to check whether location of the business had any impact on its patronages. Two different business categories, ‘Restaurants’ and ‘Beauty and Spas’ were represented by the dummy variable Category Code. ‘Restaurants’ and ‘Beauty and Spas’ were the highest and the second highest most frequently appearing business categories in the data set. Also the type of these two businesses was significantly different and this helped us observe whether business category had any impact on patronages. After including the control variables in the analysis the data size became 7700. We also checked the correlation between the independent variables and found no significant multicollinearity among the variables [51].

Descriptive statistics of the variables used for testing hypotheses H2a–H2f.

<table><tr><td>Variable</td><td>Range</td><td>Mean</td><td>SD</td></tr><tr><td>Number of followers</td><td>1–23</td><td>2.042</td><td>1.934</td></tr><tr><td>Average review rating per user</td><td>1–5</td><td>3.816</td><td>0.587</td></tr><tr><td>Number of reviews written</td><td>3–284</td><td>45.026</td><td>46.541</td></tr><tr><td>Years of experience</td><td>1–12</td><td>5.214</td><td>2.084</td></tr><tr><td>Years of reputation</td><td>0–3</td><td>0.133</td><td>0.435</td></tr><tr><td>Average review votes per user</td><td>0–8.5</td><td>2.085</td><td>1.414</td></tr><tr><td>Number of friends</td><td>1–49</td><td>7.186</td><td>9.361</td></tr><tr><td>Average review length</td><td>1–58</td><td>23.114</td><td>13.130</td></tr></table>

Hypotheses H1a and H1b were tested using the first model. We used the following linear regression equations for the analysis.

Model 1:

Log of total checkins  β β Category code  β City code  ∈

Model 2:

Log of total checkins $= \beta _ { 0 } + \beta _ { 1 }$ Category code β City code β Log of

Average business rating  Number of reviews ∈

Model 3:

Log of total checkins

<sub>¼</sub> β<sub>0 þ</sub> β<sub>1</sub> Category code $+ \beta _ { 2 }$ City code

β Log of Average number of followers

1 ${ \mathrm { - } } \beta _ { 4 }$ Log of Average business rating Number of reviews

$+ \beta _ { 5 }$ Log of Average number of followers

Average business rating Number of reviews ∈

Model 1 incorporated only the control variables to account for the variation in our sample in terms of city and business category. Model 2 tested the main effect of online reputation on business patronages. Model 3 tested the moderating effect by introducing the interaction variable i.e., product of average number of followers and (average business rating ∗ number of reviews) [49]. Table 5 summarizes the results of the hypotheses testing for Models 1, 2 and 3.

The result supported hypothesis H1a where the relationship of review-based online reputation and patronages of business was found to be positive and significant. We observed a significant increase in the value of $R ^ { 2 }$ from Model 1 to Model 2 and Model 3. The coefficient of the interaction term was also positive and significant and thus supported hypothesis H1b. We obtained similar results using the cities Las Vegas and Edinburgh that were from different countries.

In the second part of our analysis we attempted to identify the reviewer characteristics which impacted reviewer trustworthiness. Number of followers of a reviewer was used as a measure of trustworthiness of that reviewer. The descriptive statistics of the data is provided in Table 4. It was observed that the standard deviation of the variables was smaller than their mean.

We also checked the distribution of the variables. All variables except Number of followers, Number of reviews and Number of friends were found to be normally distributed. These three variables (Number of followers, Number of reviews and Number of friends) had shown skewness to the right. To adjust for the non-conformance to normality we used log-transformation of these variables for our analysis [50]. Next we checked the correlation matrix to identify multicollinearity, if any, among the independent variables [51]. The correlation of the variables ranged from −1.52 to +0.348 and was not found to be significant enough to cause issues with regression analysis. However, to reassure that there was no evidence of multicollinearity, we checked the VIF [52] of the independent variables and found it to be below 10.

To analyse hypotheses H2a through H2f we used the following linear regression equations:

Model 4

Log of number of followers $= \beta _ { 0 } + \beta _ { 1 }$ Average review length $+ \in$

Results of hypotheses testing (H1a–H1b).

<table><tr><td>Dependent variable: Log of total number of check-ins</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Category code</td><td>1.391***</td><td>0.701***</td><td>0.553***</td></tr><tr><td>City code</td><td>0.389***</td><td>0.138***</td><td>0.085***</td></tr><tr><td>Log of Review based online reputation</td><td></td><td>0.899***</td><td>0.831***</td></tr><tr><td>Log of Reviewer trustworthiness</td><td></td><td></td><td>-0.027</td></tr><tr><td>Interaction effect: Log of Reviewer trustworthiness * Log of Review based online reputation</td><td></td><td></td><td>0.041***</td></tr><tr><td> $R^2$ </td><td>0.104</td><td>0.688</td><td>0.763</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.104</td><td>0.688</td><td>0.763</td></tr><tr><td>Hypothesis</td><td></td><td>H1a</td><td>H1b</td></tr><tr><td>Hypothesized relationship</td><td></td><td>Review-based online reputation → Patronages</td><td>Review-based Online reputation * Reviewer trustworthiness → Patronages</td></tr><tr><td>Results</td><td></td><td>Supported</td><td>Supported</td></tr></table>

⁎⁎⁎ Significant at the 0.001 level of significance.

## Model 5

Log of number of followers $\mathrm { \beta _ { 0 } + \beta _ { 1 } }$ Average review length

十 ${ \bf \nabla } \cdot \beta _ { 2 }$ Average review rating

\+ $\beta _ { 3 }$ Log of number of reviews written

$\beta _ { 4 }$ Years of experience

$\beta _ { 5 }$ Years of reputation

\+ $\mathrm { . \textmu \textmu \textmu \textmu } _ { \mathrm { 8 6 } }$ Average review vote per user

$+ \beta _ { 7 }$ Log of number of friends ∈

We used linear regression after checking for the underlying assumptions. We checked the scatter plots of the dependent variable with respect to all the independent variables to identify the patterns that had appeared to be linear in nature. We considered the average length of review for each user as a control variable in order to confirm that trustworthiness of a reviewer significantly depended on the reviewer characteristics, and was not biased by the length of the review that a reviewer wrote. Model 4 in this part of analysis took into account the control variables. Model 5 studied the main effect of the independent variables. We ran a robust regression model. Robust regression was used instead of the OLS regression to take care of heteroscedasticity, and error due to outliers and highly leveraged data points [53]. The model was found to be significant at the 0.001 level of significance. All the hypotheses were supported in our analysis. Tables 6 and 7 summarize the results obtained from hypotheses testing for Models 4 and 5. The linear regression model resulted in an adjusted $R ^ { 2 }$ value of 0.366, which conformed with the goodness of fit of the robust regression model. Fig. 2 shows the proposed model with final results.

The data size of the analysis being large (69,612 records) we had to re-confirm that the results of the regression analysis were due to correctness of the model, and not due to Type I error. To ensure that, we carried out the analysis using smaller sub-samples of the initial data set. We randomly selected around 50% of the data (30,000 records) and 25% of the data (15,000 records) and ran the regression analysis for both sub-samples. We found all hypotheses to be supported. Hypothesis H2c was supported at the 0.05 level of significance. All other hypotheses were found to be significant at the 0.001 level of significance.

Results of robust regression analysis (H2a–H2f).

<table><tr><td>Dependent variable: Log of number of followers</td><td>Model 4</td><td>Model 5</td></tr><tr><td>Average review length</td><td>-0.001***</td><td>0.001***</td></tr><tr><td>Average review rating per user</td><td></td><td>0.051***</td></tr><tr><td>Log of number of reviews written</td><td></td><td>0.228***</td></tr><tr><td>Years of experience</td><td></td><td>0.004***</td></tr><tr><td>Years of reputation</td><td></td><td>0.183***</td></tr><tr><td>Average review votes per user</td><td></td><td>0.084***</td></tr><tr><td>Log of number of friends</td><td></td><td>0.120***</td></tr><tr><td> $R^2$ </td><td>0.001</td><td>0.366</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.001</td><td>0.366</td></tr></table>

\*\*\* Significant at the 0.001 level of significance.

Finally to test the predictive capacity of our model, we predicted the trustworthiness of a reviewer based on his/her characteristics. We divided the user dataset into two subsets: high and low trustworthiness of users depending on the mean value of number of followers. The reviewers with followers more than the average number of followers were labeled as high trustworthy reviewers and users having followers less than the average number of followers were labeled as low trustworthy reviewers. For the purpose of classification, a robust logistic regression model was built using the significant factors identified in the proposed research model. Monte Carlo cross-validation was used to repeatedly (5 times) train and test the model by splitting the data each time into random sub-samples in a proportion of 80–20. Use of the robust logistic regression took care of heteroscedastic errors and presence of outliers in the data. We calculated the average of the accuracies for the 5 data samples that were created and found that the predictive model successfully classified 82.85% of the reviewers as high or low on trustworthiness based on the underlying factors. Table 8 shows the performance measure of the predictive Model I. We obtained similar results by using other machine learning techniques like neural network and C5.0 decision tree with overall accuracy of 83.59% and 83.1% respectively.

The Model I showed a high degree of specificity indicating that it had correctly classified more than 95% of less trustworthy reviewers. If a business aimed to target high trustworthy reviewers to write a review of that business it incurred some cost in terms of promotional expenses. Correctly classifying reviewers who had less followers had the potential to save businesses from making redundant expenses. Since the sensitivity of the model was 41.1% there was some probability of misclassifying high trustworthy reviewers. However, the overall predictability of the model was fund to be reasonably high (82.85%).

The sensitivity of the model was 41.1% which meant that more than 50% of actually high trustworthy reviewers would be incorrectly classified as low trustworthy. For businesses that wanted to identify as many trustworthy reviewers as possible to incentivize or encourage them to review their services, the required model should have a high value of sensitivity. We developed a cost-sensitive classification technique to address the issue, where we assigned higher penalty or cost for falsely classifying high trustworthy as low trustworthy reviewers. Model II in Table 8 showed that the performance measure of the classifier with differential mis-classification cost (Cost of false negative classification = 5 × Cost of false positive classification). The model had a sensitivity of 89.87%, which meant that the revised model was able to correctly identify more than 89% of high trustworthy reviewers.

Further, to check the robustness of the predictive model, we performed a cost-sensitive classification to predict top-10% trustworthy reviewers. The model displayed an overall accuracy of 83% and a sensitivity of 85.8%. Observations for Model III in Table 8 showed the performance measures for classifying top 10% reviewers.

Table 7  
Results for hypotheses testing (H2a–H2f).

<table><tr><td>Hypothesis</td><td>Hypothesized relationships</td><td>Coefficients</td><td>Results</td></tr><tr><td>H2a</td><td>Reviewer positivity → Reviewer trustworthiness</td><td>0.051***</td><td>All hypotheses are supported</td></tr><tr><td>H2b</td><td>Reviewer Involvement → Reviewer trustworthiness</td><td>0.228***</td><td></td></tr><tr><td>H2c</td><td>Reviewer experience → Reviewer trustworthiness</td><td>0.004***</td><td></td></tr><tr><td>H2d</td><td>Reviewer reputation → Reviewer trustworthiness</td><td>0.183***</td><td></td></tr><tr><td>H2e</td><td>Reviewer competence → &gt; Reviewer trustworthiness</td><td>0.084***</td><td></td></tr><tr><td>H2f</td><td>Reviewer sociability → Reviewer trustworthiness</td><td>0.120***</td><td></td></tr></table>

⁎⁎⁎ Significant at the 0.001 level of significance.

## 6. Discussion and implications

## 6.1. Theoretical implications

This paper makes several significant theoretical contributions. First, it establishes a direct positive influence of review-based online reputation of a business on its patronages, which should consequently affect sales. Earlier studies have either used the average ratings [5] or volume of ratings [6] received to find its impact on sales. However, we have created a new construct of review-based online reputation using product of average ratings and the total number of ratings. This we believe is a better measure since it takes into account the distortions created by businesses which have very few ratings. Also, most of the earlier studies have focused on online product sales, whereas we have focused on number of footfalls a local business has received.

Second, while some research works have proposed few reviewer characteristics (quality and exposure [27], elite certification [8], top ranked [9]) that can directly influence sales, this paper added a missing link to the models by introducing the perceived trustworthiness of reviewers based on their characteristics. We established reviewer trustworthiness as a significant factor in moderating the positive influence of review-based online reputation on patronages. This is a unique relationship which has not been verified before in eWOM research to the best of our knowledge.

Third, we introduced number of followers a reviewer had as a proxy to measure reviewer trustworthiness. While this has been done in the social network literature, it has hardly been used in eWOM literature except in some cases as a reputation cue [18]. This may be because most of the online review websites do not provide any functionality to anonymously follow a trusted reviewer for getting updates on his/her review posts. In fact, reviewer trustworthiness has been mostly treated as an implicit rather than an explicit factor in online review research.

Fourth, past research has mostly focused on identifying one or two reviewer characteristics that can affect review helpfulness like expertise and reputation [32], number of reviews and total helpful votes [33], expertise and writing style [34], engagement [30], historical rating distribution [31], etc. For the first time, to the best of our knowledge, a number of them have been used in an integrated manner to build a model of reviewer trustworthiness. All proposed characteristics (positivity, involvement, experience, reputation, competence, sociability) have been found to be significant, and can be reused by future researchers in extending not just eWOM literature, but also research on online communities.

![](/api/attachments/UHPKF9MA/fulltext/images/77628ddbab0e7e3e6aeaa9dbfc79f9ab28ab31c208790cd393725d7e4cb357b5.jpg)  
Fig. 2. Results of hypothesized relationships.

Table 8  
Performance measure of the predictive models.

<table><tr><td>Performance measure</td><td>Model I: Logistic regression</td><td>Model II: Cost-sensitive</td><td>Model III: Top 10% and cost-sensitive</td></tr><tr><td>Sensitivity</td><td>41.15%</td><td>89.87%</td><td>85.79%</td></tr><tr><td>Specificity</td><td>95.10%</td><td>66.23%</td><td>82.64%</td></tr><tr><td>False positive rate for true negative data</td><td>4.90%</td><td>33.77%</td><td>17.35%</td></tr><tr><td>False negative rate for true positive data</td><td>58.85%</td><td>10.13%</td><td>14.21%</td></tr><tr><td>False positive rate for classified positive</td><td>28.83%</td><td>56.07%</td><td>57.02%</td></tr><tr><td>False negative rate for classified negative</td><td>15.39%</td><td>4.23%</td><td>2.55%</td></tr><tr><td>Correctly classified</td><td>82.85%</td><td>71.9%</td><td>83.0%</td></tr></table>

Note: True positive data refers to high trustworthy reviewers  
True negative data refers to low trustworthy reviewers.

## 6.2. Managerial implications

The findings of this paper have several managerial implications as well. First, since we have found a significant positive influence of online reputation on patronages of local business, the managers can be advised to focus on increasing their number of customer reviews and to try their best to receive positive reviews. Earlier, businesses with online sales channels used to get affected by the reviews on their products, but now even brick-and-mortar businesses get affected due to reviews posted by their customers online.

Second, because of the positive moderating influence of reviewer trustworthiness on influence of online reputation on patronages, business managers may be advised to encourage top trustworthy reviewers to review their products and services. While increase in patronages is positively associated with good online reviews, it can be further boosted if reviewers have higher level of perceived trustworthiness. So the practice of inviting top online reviewers to visit and review businesses can be more popularized. The lure of getting free invitations can lead to more reviewers becoming active and quality conscious in review sites in order to gain trust of others.

Third, business managers can customize and use the predictive model presented in this paper to identify and rank reviewers based on their potential trustworthiness using reviewer characteristics available in the websites. This can be particularly useful for online review sites where users are not allowed to follow their trusted reviewers, thus eliminating the possibility of using the number of followers as a direct proxy to reviewer trustworthiness.

Fourth, the predictive model can also be used by the online review websites to rank reviewers and even display their reviews in decreasing order of reviewer trustworthiness. This can be particularly useful in case of new reviews posted with no helpfulness votes received to decide their display order. Also, the significant factors affecting reviewer trustworthiness can be shared with reviewers, so that they can get an easy understanding of steps to take in order to gain more followers.

## 6.3. Limitations and future research

There are some limitations to this research, which can be overcome in future research. First, we have used data only from one review site Yelp, which only includes local businesses. So it needs to be tested whether the findings are generalizable for other product review websites as well.

Second, we have used check-ins to a business posted by Yelp customers, when they visit the business, as a proxy for business patronages. While it is a good indicator based on actual physical presence of a customer at the business shop, it is still limited compared to the total number of footfalls in the business since most of the customers may not be checkingin their location on Yelp. This is why the mean of total check-ins across all businesses is just 148. Future researchers can try to get sales data of businesses from financial databases and verify this model.

Third, only a few of the possible control variables have been used in this study. For instance, when controlling for review characteristics, we have used length of review. However, future researchers can take some of the linguistic characteristics of reviews like sentiment, depth, bias, etc. into consideration. Similarly for business characteristics, apart from category and location, other control variables like size, age, etc. of a business can be used as control variables. An important variable that can be controlled in future studies is the online marketing expense of businesses, since that may have a positive influence on the number of check-ins. For instance, Yelp allows businesses to purchase self-service and full-service ads, with the latter having added advantages of removing competitor ads from business page, and have videographers from Yelp help produce professional videos. While it may be difficult to find out the exact advertising expenses of local businesses, the effort of marketing can be reflected by data on the sponsored ads posted by the businesses.

Fourth, more reviewer characteristics can be added to improve the predictive accuracy of the model. Some of the well-known trust inducing factors like presence of profile picture, etc. have not been considered. Even the network effect of friends has not been explored in depth. Future research can dig deeper into other reviewer characteristics. Other predictive techniques can also be used to build models either separately or in ensemble (e.g., decision tree combined with neural network) to further boost the accuracy.

Fifth, only a cross-sectional regression analysis could be performed with the data available to us. Hence, we do not know how business patronages get impacted over time by reviewer trustworthiness, or how reviewer characteristics vary in their influence on trustworthiness over time. Future researchers can use time-stamped data to conduct a panel data regression to uncover interesting results.

## 7. Conclusion

This paper puts focus on trustworthiness of reviewers as an important construct in eWOM literature. We have found reviewer trustworthiness to positively moderate the association between review-based online reputation and patronages of businesses. Furthermore, we have found reviewer trustworthiness to be positively associated with six reviewer characteristics like positivity, involvement, experience, reputation, competence, and sociability. Using these factors, we have developed a predictive model to classify reviewers into two groups based on high and low trustworthiness. This research makes significant theoretical contribution and can be used by businesses to estimate reviewer trustworthiness in order to target top reviewers to review their products or services.

## References

[1] T. Hennig-Thurau, K.P. Gwinner, G. Walsh, D.D. Gremler, Electronic word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate them selves on the Internet? Journal of Interactive Marketing 18 (2004) 38–52.

[2] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, Journal of Marketing 74 (2010) 133–148.

[3] X. Li, L. Hitt, Price effects in online product reviews: an analytical model and empirical analysis, MIS Quarterly 34 (2010) 809–831.

[4] BrightLocal, Local consumer review survey, https://www.brightlocal.com/learn/ local-consumer-review-survey/ 2016

[5] J. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (2006) 345–354

[6] W. Duan, B. Gu, A. Whinston, Do online reviews matter?—an empirical investigation of panel data, Decis. Support. Syst. 45 (2008) 1007–1016.

[7] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Information Systems Research 19 (2008) 291–313.

[8] S. DiGrande, D. Knox, K. Manfred, J. Rose, Unlocking the digital-marketing potential of small businesses, BCG perspectives, https://www.bcgperspectives.com/content/ articles/digital\_economy\_marketing\_sales\_unlocking\_digital\_marketing\_small\_ businesses/ 2013.

[9] M. Luca, Reviews, Reputation, and Revenue: The Case of Yelp.com, Harvard Business School NOM Unit Working Paper. 12–016, 2011 1–40.

[10] P. Chen, S. Dhanasobhon, M.D. Smith, All Reviews Are Not Created Equal: The Disaggregate Impact of Reviews and Reviewers at Amazon.com, Heinz College Research, 2008 1–32.

[11] S.M. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on Amazon com MIS Ouarterly 34 (2010) 185–200

[12] R. Schindler, B. Bickart, Perceived helpfulness of online consumer reviews: the role of message content and style, Journal of Consumer Behaviour 11 (2012) 234–243.

[13] N. Korfiatis, E. García-Bariocanal, S. Sánchez-Alonso, Evaluating content quality and helpfulness of online product reviews: the interplay of review helpfulness vs. review content, Electronic Commerce Research and Applications 11 (2012) 205–217.

[14] H. Baek, J. Ahn, Y. Choi, Helpfulness of online consumer reviews: readers' objectives and review cues, International Journal of Electronic Commerce 17 (2012) 99 126.

[15] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering 23 (2011) 1498–1512.

[16] M. Li, L. Huang, C. Tan, K. Wei, Helpfulness of online product reviews as seen by consumers: source and content features, International Journal of Electronic Commerce 17 (2013) 101–136.

[17] L. Connors, S.M. Mudambi, D. Schuff, Is it the review or the reviewer? A multi-method approach to determine the antecedents of online review helpfulness, Proceedings of the 44th Hawaii International Conference on System Sciences 2011, pp. 1–10.

[18] Q. Xu, Should I trust him? The effects of reviewer profile characteristics on eWOM credibility, Computers in Human Behavior 33 (2014) 136–144.

[19] J.C. McCroskey, T.A. Jenson, Image of mass media news sources, Journal of Broadcasting 19 (1975) 169–180.

[20] J. Devi, Estimating the helpfulness and economic impact of product reviews, Int. J. Innov. Res. Dev. 1 (2012) 232–236.

[21] P.F. Wu, In search of negativity bias: an empirical study of perceived helpfulness of online reviews, Psychology and Marketing 30 (2013) 971–984.

[22] P. Fei Wu, H. van der Heijden, N.T. Korfiatis, The influences of negativity and review quality on the helpfulness of online reviews, International Conference on Information Systems 2011, pp. 1–10.

[23] D. Yin, S.D. Bond, H. Zhang, Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews, MIS Quarterly 38 (2014) 539–560.

[24] M. Jensen, J. Averbeck, Z. Zhang, Credibility of anonymous online product reviews: a language expectancy perspective, Journal of Management Information Systems 30 (2013) 293–324.

[25] K. Floyd, R. Freling, S. Alhoqail, H. Cho, T. Freling, How online product reviews affect retail sales: a meta-analysis, Journal of Retailing 90 (2014) 217–232.

[26] P. De Maeyer, Impact of online consumer reviews on sales and price strategies: a review and directions for future research. The Journal of Product and Brand Management 21 (2012) 132–139.

[27] G. Cui, H.-K. Lui, X, Guo, The effect of online consumer reviews on new product sales. International Journal of Electronic Commerce 17 (2012) 39–57.

[28] N. Hu, L. Liu, J.J. Zhang, Do online reviews affect product sales? The role of reviewer characteristics and temporal effects, Information Technology and Management 9 (2008) 201–214.

[29] E. Lee, S. Shin, When do consumers buy online product reviews? Effects of review quality, product type, and reviewer's photo, Computers in Human Behavior 31 (2014) 356–366.

[30] Y.C. Ku, C.P. Wei, H.W. Hsiao, To whom should I listen? Finding reputable reviewers in opinion-sharing communities, Decis. Support. Syst. 53 (2012) 534–542.

[31] T.L. Ngo-Ye, A.P. Sinha, The influence of reviewer engagement characteristics on online review helpfulness: a text regression model, Decis. Support. Syst. 61 (2014) 47-58.

[32] B. Fang, Q. Ye, D. Kucukusta, R. Law, Analysis of the perceived value of online tourism reviews: influence of readability and reviewer characteristics, Tourism Management 52 (2016) 498–506.

[33] Z. Liu, S. Park, What makes a useful online review? Implication for travel product websites, Tourism Management 47 (2015) 140–151.

[34] J. Otterbacher, “Helpfulness” in online communities: a measure of message quality, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, Boston, Massachusetts, USA 2009, pp. 1–10.

[35] Y. Liu, X. Huang, A. An, X. Yu, Modeling and predicting the helpfulness of online reviews 2008 Fighth JFFE International Conference on Data Mining, JFFE 2008 pp. 443–452.

[36] W. Shen, Y. Jeffrey Hu, J. Rees Ulmer, Competing for attention: an empirical study of online reviewers' strategic behavior, MIS Ouarterly 39 (2015) 683–696.

[37] L. Zhu, G. Yin, W. He, Is this opinion leader's review useful? Peripheral cues for online review helpfulness L. Electron, Commer, Res, 15 (2014) 267–280.

[38] J. Mosteller, C. Mathwick, Reviewer online engagement: the role of rank, well-being, and market helping behavior, Journal of Consumer Marketing 31 (2014) 464–474 http://dx.doi.org/10.1108/JCM-05-2014-0974

[39] R. Hardin, Trustworthiness, Ethics 107 (1996) 26–42.

[40] R. Mayer, J. Davis, F. Schoorman, An integrative model of organizational trust, The Academy of Management Review 20 (1995) 709–734.

[41] R. Hardin, Trust and Trustworthiness, Russel Sage Foundation, New York, 2002.

[42] C. Hovland, W. Weiss, The influence of source credibility on communication effectiveness, Pub. Opin. Q. 15 (1951) 635–650.

[43] D. Berlo, J. Lemert, R. Mertz, Dimensions for evaluating the acceptability of message sources, Pub. Opin. Q. 33 (1969) 563–576.

[44] P.B. Lowry, D.W. Wilson, W.L. Haig, A picture is worth a thousand words: source credibility theory applied to logo and website design for heightened credibilit and consumer trust, International Journal of Human Computer Interaction 30 (2013) 63–93.

[45] S. Utz, P. Kerkhof, J. Van Den Bos, Consumers rule: how consumer reviews influence perceived trustworthiness of online stores, Electronic Commerce Research and Applications 11 (2012) 49–58.

[46] S. Chaiken, D. Maheswaran, Heuristic processing can bias systematic processing: effects of source credibility, argument ambiguity, and task importance on attitude judgment, Journal of Personality and Social Psychology 66 (1994) 460–473.

[47] M. Cheung, C. Luo, C. SIA, H. Chen, How do people evaluate electronic word-ofmouth? Informational and normative based determinants of perceived credibility of online consumer recommendations in China, PACIS 2007 Proceedings 2007, p. 18.

[48] S. Norman, B. Avolio, F. Luthans, The impact of positivity and transparency on trust in leaders and their perceived effectiveness, The Leadership Quarterly 21 (2010) 350–364.

[49] J. Jaccard, R. Turrisi, Interaction Effects in Multiple Regression - Vol. 72 (Quantitative Applications in the Social Sciences), SAGE Publications Inc., 2003

[50] A.C. Cameron, P.K. Trivedi, Regression Analysis of Count Data, Cambridge Universit Press, New York, 2013.

[51] T. Kumar, Multicollinearity in regression analysis, The Review of Economics and Statistics 57 (1975) 365–366.

[52] R.M. O'brien, A caution regarding rules of thumb for variance inflation factors, Quality and Quantity 41 (2007) 673–690.

[53] P. Rousseeuw, A. Leroy, Robust Regression and Outlier Detection (Wiley Series in Probability and Mathematical Statistics), Wiley, New York, 1987.

![](/api/attachments/UHPKF9MA/fulltext/images/a4ce692e22090210e984b91aa37ecc3386ffad5165643f6cb778ca4e53daf94e.jpg)

Shankhadeep Banerjee is a doctoral student of Management Information Systems at the Indian Institute of Management Calcutta. He holds B.Tech in Computer Science and Engineering from National Institute of Technology (Durgapur), PGDM/MBA from Indian Institute of Management Calcutta and IMP certi cate from NEOMA Business School, France. His research interests are in e-commerce, business analytics, social networks, and adoption of technology. He has prior IS research experience at Indian School of Business Hyderabad, where his research work on smart city maturity model received press coverage at national level. He also has extensive IS practitioner experience working at top technology firms like Microsoft, Amazon, and eBay.

![](/api/attachments/UHPKF9MA/fulltext/images/059b962fc22245b22dabb6f128fa6e7f8a719ed6f5e55cc239f245a0014dbba2.jpg)

Samadrita Bhattacharyya is a doctoral student of Management Information Systems at the Indian Institute of Manage ment Calcutta. She holds B.Tech in Electronics and Communication Engineering from West Bengal University of Technology and M.Tech in VISI Design from Indian Institute of Engineering Science and Technology, Shibpur (formerly Bengal Engineering and Science University, Shibpur). Her research interests include social networks, business analytics, optimization and algorithms, and VLSI design. Her research articles have appeared in conference proceedings of IEEE.

![](/api/attachments/UHPKF9MA/fulltext/images/bd509c435665ecdbd436a49ed403d240f26048949a5253ccb6002ea67018d3dc.jpg)

Indranil Bose is Professor of Management Information Systems at the Indian Institute of Management, Calcutta. He acts as Coordinator of IIMC Case Research Center. He holds a B.Tech. from the Indian Institute of Technology, MS from the University of Iowa, MS and Ph.D. from Purdue University. His research interests are in business analytics, telecommunications, information security, and supply chain management. His publications have appeared in Communications of the ACM, Communications of AIS, Computers and Operations Research, Decision Support Systems, Ergonomics, European Journal of Operational Research, Information & Management International Journal ofProduction Economics Journal of Organizational Computing and Electronic Com: merce, Journal of the American Society for Information Science and Technology, Operations Research Letters etc. He is listed in the International Who”'s Who of Professionals, Marquis Who”'s Who in the World, Marquis Who”'s Who in Asia, Marquis Who”'s Who in Science and Engineering, and Marquis Who”'s Who of Emerging Leaders 2007. He serves as Senior Editor of Decision Support Systems and as Associate Editor of Communications of AIS, Information & Management, Information Technology & Management and several other IS journals.
