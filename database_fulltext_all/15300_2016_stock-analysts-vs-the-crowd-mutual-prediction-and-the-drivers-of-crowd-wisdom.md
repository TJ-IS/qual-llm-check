---
otero_id: 15300
otero_key: "ES7E7BWK"
title: "Stock analysts vs. the crowd: Mutual prediction and the drivers of crowd wisdom"
authors: "Matthias Eickhoff; Jan Muntermann"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.03.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Stock analysts vs. the crowd: Mutual prediction and the drivers of crowd wisdom

Author: Matthias Eickhoff Jan Muntermann

![](/api/attachments/ES7E7BWK/fulltext/images/dd828ceaae976f33b486dcf372cb02d06a6bcdb02c407b982eaab015b860295f.jpg)

PII: S0378-7206(16)30031-3

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.03.008

Reference: INFMAN 2896

To appear in: INFMAN

Received date: 20-9-2015

Revised date: 22-2-2016

Accepted date: 22-3-2016

Please cite this article as: Matthias Eickhoff, Jan Muntermann, Stock analysts vs.the crowd: Mutual prediction and the drivers of crowd wisdom, Information and Management http://dx.doi.org/10.1016/j.im.2016.03.008

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Stock Analysts vs. the Crowd: Mutual Prediction and the Drivers of Crowd Wisdom

## Abstract:

We examine the drivers of crowd wisdom in the financial domain by relating analyst report and social media sentiment via Granger Causality (GC) testing based on wisdom of crowds (WoC) theory. Significance for a large number of the tested time series indicates that analyst reports and social media content are suitable for mutual prediction. We elaborate on the conditions under which crowd cognitive diversity matters and derive measures for them. Results suggest that WoC theory can partially explain the GC between the two media types and that both professional analysts and the crowd can outperform one another under favorable circumstances.

Keywords: Wisdom of Crowds; WoC; Sentiment Analysis; Stock Analysts; Social Media

# Stock Analysts versus the Crowd: Mutual Prediction and the Drivers of Crowd Wisdom

Matthias Eickhoff<sup>\*</sup>Matthias.Eickhoff@wiwi.uni-goettingen.de

University of Göttingen, Chair of Electronic Finance and Digital Markets, Platz der Göttinger Sieben 5, Göttingen, Germany

Tel.: 49 0551 39 20046, fax: 49 0 551 39 20041

Highlights

<sup>-</sup> Exploration of the drivers of crowd wisdom and their impact on prediction quality.

<sup>-</sup> Operationalization of measures based on constructs of crowd wisdom theory.

<sup>-</sup> Suggestion of future research avenues for crowd wisdom research.

<sup>-</sup> Recommendation of aggregation procedures for crowd-based platforms.

## Abstract

We examine the drivers of crowd wisdom in the financial domain by relating analyst report and social media sentiment via Granger causality (GC) testing based on the wisdom of crowds (WoC) theory. The significance of a large number of the tested time series indicates that analyst reports and social media content are suitable for mutua prediction. We elaborate on the conditions under which crowd cognitive diversity matters, and we derive related measures. The results suggest that the WoC theory can partially explain the GC between the two media types and that both professional analysts and the crowd can outperform one another under favorable circumstances.

Keywords: Wisdom of Crowds; WoC; Sentiment Analysis; Stock Analysts; Social Media

#

## Introduction

The impact of financial analyst reports has been subject to increasing scientific scrutiny. In particular, the herding behavior of financial analysts, that is, how some analysts seem to affect the opinion of others,<sup>44</sup> has been analyzed extensively.<sup>11,25,43</sup> The reaction of the capital market has also been analyzed. Traditional analyses have dealt with buy/hold/sell recommendations, from the Institutional Brokers’ Estimate System (I/B/E/S). More recently, researchers have been applying text-mining methods to analyst reports to automatically extract more information than previously available. The analysis of the entire report is desirable, as it may yield further information beyond the constrained categorization of the stock.<sup>44</sup> In contrast to prior studies, this study focuses on how the opinions of professional stock analysts, that is, individuals who are paid to provide regularly updated opinions about certain companies, relate to those of social media users. The study also analyzes whether the two related content types can be used to predict each other’s sentiment. Although studies have shown that social media content can be used to forecast stock returns similar to analyst recommendations, this does not necessarily imply that the prediction powers of the two mediums are inherently related. Such a relation is of interest because professional analysts have access to privileged information, as illustrated in section 2.

However, analysts also face a number of constraints that can influence their recommendations. These constraints include incentives to generate in-house brokerage volume<sup>27</sup> and the tendency to stick to established recommendations.<sup>11,43</sup> The average social media user does not face these constraints.

Therefore, such a relation could allow the incorporation of social media content in models traditionally using traditional stock analyst recommendations for predictive purposes. This incorporation could serve as a control variable for the analysts’ biases. Therefore, the aim of this research is to investigate the presence of such a relationship between content types in either direction. Social media and analyst report data regarding the 30 component companies of the Dow Jones Industrial Average (DJIA) index are collected from the year 2013. First, we perform sentiment analysis on analyst reports and social media data to establish time periods (quarterly and annual) and company combination Granger causality (GC) between social media and analyst sentiment. We then aim to determine reasons for different cases of GC direction. Afterthis section, the theoretical background of the analysis is introduced. Theoretical insight on the information value of analyst reports and the concept of wisdom of crowds (WoC) is compared in section 2, focusing on inefficiencies in analyst opinions likely to be mitigated by social media content. Based on these foundations, hypotheses are developed and tested. In section 3, methodologica foundations are introduced and comprise sample generation, GC, sentiment analysis, and variable operationalization related to WoC constructs. We then present our analysis and empirical results in section 4. Using binary response models, we provide evidence regarding which types of companies and public interest foster GC directions. This section also examines drivers of WoC in our social media sample by introducing variables for measuring WoC-related conditions proposed by Surowiecki.<sup>42</sup> The conclusion summarizes the results of the analysis and elaborates on their theoretical value for WoC and analyst research.

## Theoretical Background

This research aims at combining insights from research regarding the information value of analyst reports with the principle of social media user sentiment through the lens of crowd wisdom.

## Information value of analyst reports

Analyst reports have been researched, largely to answer the following question: How do stock analysts influence the stock market, and how do stock analysts arrive at their conclusions?

The former question addresses the information value of analyst reports and their recommendations (i.e., whether they can be used as a basis for supporting investment decisions). It is assumed that analysts have privileged access to relevant information about companies by thorough research or close relationships with these businesses. Therefore, they are viewed as information providers capable of improving information efficiency<sup>18</sup> and shortening the time between publication and incorporation of information into stock prices.<sup>15,26</sup> Answers to this question have been mixed. While earlier studies suggested that investments based on analyst recommendations can be profitable,<sup>3,46</sup> recent research doubts the impartiality of stock analysts.<sup>4,8</sup> These doubts motivate the second question (i.e., upon which information stock analysts base their recommendations).

Several studies have provided evidence for herding behavior among stock analysts. Herding behavior refers to the tendency to provide recommendations close to those of the consensus.<sup>44</sup> This behavior introduces a bias toward the status quo. Career concerns are largely responsible for this tendency.<sup>11</sup> Career concerns are especially relevant for younger analysts who fear termination if they make bold predictions and fail.<sup>25</sup> Groysberg et al.<sup>22</sup> found that compensation schemes are designed to increase brokerage and investment-banking revenues. Therefore, other data sources offering insight into companies are desirable. Social media content is widely available for a large number of companies, and social media users are no faced with the same repercussions or incentives as stock analysts. Thus, social media users might be able to provide less biased opinions about a company’s current state or future developments. Earlier research indicates that social media content (Twitter) can be used to predict stock returns.<sup>6</sup> The sentiment of social media users and stock analysts may be used in a similar manner.<sup>38</sup> The latter issue is of particular interest to this study, because deficiencies of stock analyst recommendations necessitate alternate data sources about companies. Social media content is a possible data source that is investigated in this paper.

Alternate sources of information can help mitigate known biases. Social media users should not be faced with the same problems as professional analysts and are unlikely to be punished if their opinions are wrong. The next section explores how models that currently rely solely on analyst opinions can be augmented.

Poetz and Schreier note that expert knowledge can lead to superior skills and problem solving within a given domain.<sup>40</sup> This assertion is supported by previous research.<sup>1,33</sup> However, this superiority is imited in its predictive accuracy of expert opinions.<sup>28</sup> While earlier sources mainly stem from psychology, crowddriven projects have increased due to advances in networking. A popular example of such a project is Wikipedia, which has been shown to be as accurate as the Encyclopedia Britannica.<sup>20</sup>

The efficient market hypothesis suggests that individual actors cannot outperform the market as the current price of a stock should incorporate all available information.<sup>14,36</sup> However, conventional market theory may not hold true in the context of crowd wisdom. Recent studies indicate that stock prediction communities, which are small special-purpose social networks, can achieve higher performance than the market in general [23].

## Wisdom of Crowds

The average social media user is not likely to have the finance background of stock analysts. Prior studies show that social media indicates mood and may assist in making stock market predictions.<sup>6,38</sup> Surowiecki describes this novel source of expertise as the WoC. The WoC theory proposes that large independent and heterogeneous groups can outperform smaller groups in their assessments even if the smaller group consists of subject matter experts. 42

Poetz and Schreier<sup>40</sup> define a crowd as "potentially large and diverse." Beyond these characteristics, no further assumptions will be made on the makeup of crowds.

In contrast to a crowd, our expert group can be described more clearly. According to Nofer and Hinz,<sup>37</sup> an expert is "a professional analyst from a bank or research company who has experience in his area of expertise: publishing share recommendations and predicting the stock market development." In order for crowd wisdom to emerge, a group should satisfy three key conditions: diversity, independence, and decentralization.<sup>42</sup> Aggregation of the crowd's diverse opinions is required to reach a consensus decision. 42 In contrast to authors of Wikipedia articles, social media users have no explicit intention to aggregate their collective sentiments. Their intent is to share their opinions with the community. The text-mining methods applied in this study shall serve as a humble substitute. This study investigates the extent to which groups lacking the intent to reach a common goal are not able to create a WoC effect easily.

#

Previous studies generally assume that these three conditions are satisfied. In this study, we derive measures for each condition and assess their influence on the crowds’ predictive power.

In order to confirm that these conditions are satisfied, we examine substantial social media data in each of these categories. Building on previous research, we develop measures to operationalize these conditions. We treat them as factors that may explain situations from which crowd wisdom actually arises.

## Diversity

The presence of group diversity is the central concept of the WoC theory. A group consisting of some informed and uninformed individuals will tend to outperform those consisting only of experts, even if experts are more informed than any member of the other group.<sup>42</sup> The argument for a positive effect of group diversity hinges on two separate effects.

First, diversity ensures that the group's opinion is based on sufficiently varying individual perceptions. Sorowiecki argues that “[diversity] expands a groups’ set of possible solutions and allows the group to conceptualize problems in novel ways.”<sup>42</sup> This argument does not refute expert opinion. Instead, Surowiecki suggests that exposing experts to less informed individuals challenges their opinions and forces them to make stronger arguments.

Second, larger and more diverse groups make voicing dissenting opinions easier. This reduced risk is due to the increased possibility of finding allies supporting a novel point of view. Even if a new opinion does not find support, the increased number of perspectives makes failing to convince the group more acceptable. Group diversity creates an atmosphere that is open to debate.

## Independence

Surowiecki<sup>42</sup> suggests independence is a counterweight for herding behavior (i.e., the tendency to conform to the opinion of others). This factor reduces the risk of information cascades<sup>42</sup> that threaten to override individual opinions over the group’s opinions. This threat results in the loss of added information value that dissenting opinions can offer. Independence reduces the correlation between individual opinions, reducing the risk of spreading erroneous judgment from one individual to the next. In addition, independent individuals contribute their own perspectives instead of conforming to predominant points of view.<sup>42</sup>

## Decentralization

A centralized group should face fewer problems coordinating and aggregating decisions. However, decentralization is critical for group diversity and independence. Decentralization also makes the group more permeable. This allows members familiar with particular problems to participate in discussions

#

when their expertise is needed. This ability is “at the heart of decentralization.”<sup>42</sup> However, the price of decentralization is increased communication and coordination costs and the possibility of redundancy. The increase in flexibility and the support decentralization offers may outweigh its cost.

The conditions under which crowd wisdom can arise are neither easily separated from one another nor directly observable. Therefore, a later section of this study translates these theoretical constructs into operational definitions, that is, into associated variables and their attributes that are observable and measurable.

## Hypotheses

Previous findings lead us to the conclusion that analyst recommendations may be biased because of the payment incentive structures in which professional analysts work. Social media users do not face these types of incentives. Social media and analyst recommendations may be viewed as supplementary sources of information about companies.

Alternatively, social media users may not have access to all relevant information available to stock analysts and have no coordinated way to aggregate their opinions. Thus, there may be no uniform answer to the question of whether professional analysts or social media users are quicker when incorporating new information into their opinion. This would also be the case if both groups are equally good at the task. Finally, this would be observed if there are situations or contexts in which either groups’ advantages outweigh the other groups. Against this background, hypothesis 1a is proposed:

Hypothesis 1a: There is no uniform direction of lead–lag between the two content types, and neither professional stock analysts nor social media users always shift their mean sentiment quicker than the other group.

However, their financial expertise and domain-specific training may enable professional analysts to develop superior information processing capabilities. Moreover, when analysts are able to communicate directly with corporations, they might be able to extract information that is of particular value to their analysis. Even if this information is made public immediately, others might not be able to gain insights from it. Against this background, hypothesis 1b is proposed:

Hypothesis 1b: Professional analysts are able to incorporate information into their assessment prior to social media users, therefore shifting their sentiment quicker when their expertise is relevant or they operate on superior information.

However, against the theoretical background of WoC research, we hypothesize the opposite, that is, that cases exist where (a) the information is not privileged and therefore accessible to social media users and (b) the user groups satisfy the three key conditions for crowd wisdom proposed by Surowiecki (2005) to

#

arise. The combination of decentralization, independence, and group diversity may enable social media users to arrive at conclusions that professional analysts either are unable to reach on their own or may take longer to process public information newly available. In example, an age-diverse group of users may be able to predict the impact of a product announcement, such as a new generation of smartphone, in a more timely fashion if the product will be used by consumers of all ages. This is because a single analyst lacks insight into what each age group expects from this type of product. A decentralized group may be able to judge a product announcement’s implication for different markets in a similar manner, if a sufficient number of users from each market is represented. A single analyst may lack the cultural insight necessary to understand how different communities will perceive the product. Finally, independence within the social media user group may improve the aggregate of social media users’ opinions by enabling them to utilize their own reasoning instead of following an established opinion. If one or more of these effects are present in related social media data, we should be able to see that social media users adjust their opinions more timely compared to individual analysts. Against this background, we propose hypothesis 1c:

Hypothesis 1c: Social media users’ mean sentiment changes faster than that of professional analysts if the discussed conditions for crowd wisdom are satisfied.

These conflicting theoretical considerations will be investigated in the analytical part of this paper. In addition, we examine the drivers of crowd wisdom in our social media sample. The aim of this analysis is to examine whether the WoC theory can help explain the situation in which a particular group of people possesses superior information processing capabilities. To this end, we derive measures for each of the three conditions and propose hypothesis 2:

Hypothesis 2: There is a positive relationship between the extent to which a group satisfies the conditions of crowd wisdom and the likelihood of a successful prediction of analyst opinion by social media users.

## Methodology

## Sample

Three datasets are used, each containing information about the companies included in the DIJA in 2013. Table 1 shows an overview of the data.

Each dataset is collected for the year 2013, starting 1 January and ending 31 December. The first dataset consists of analyst reports from the Thomson Reuters Advanced Analytics (TRAA) platform. After having extracted textual content, 9439 observations remained. The second dataset contains a broad selection of

#

social media content, including web logs, forums and product reviews. These data were obtained from the SDLs SM2 database, which is primarily intended for marketing. A maximum of 40,000 observations per quarter was requested from the database for each company, resulting in 3,814,839 observations (approximately 127,000 per company). A public news dataset was obtained from the Guardian open API, which contains 21,278 news articles from the same period. These articles are annotated with their respective news category, such as “financial,” "technology," or “environment.” Their daily median (i.e., the most common news category for a given firm on a specific day) will serve as a basis for the second stage of the analysis.

## Granger Causality

The question whether analysts or social media users react faster to new (exogenous) information will be analyzed via GC testing. This method is easily misunderstood because of its name. A GC test compares a model explaining a time series value using lagged values with one that adds lagged values of a second time series.<sup>30</sup> Thus, x is Granger causal to y if

$$
\sigma_ {M 2} ^ {2} (y _ {t + 1} | I _ {t}) <   \sigma_ {M 1} ^ {2} \left(y _ {t + 1} | I _ {t} - \overline {{x}} _ {t}\right),
$$

that is, the forecast error $\sigma ^ { 2 }$ is reduced by including the past values of x. No causal relationship is implied if GC is discovered. Asserting such a relationship purely on the basis of GC would be a post hoc fallacy.<sup>13</sup> Pearl does not classify GC as a causal, but as a statistical methodology.<sup>39</sup>

Three outcomes can occur for a GC test between a pair of time series. First, no GC relationship is observed. This outcome would entail that neither series could statistically improve the prediction of the other. Second, a GC relationship is observed in one direction. Third, a GC relationship is noted in both directions. For each company’s pair of social media and analyst reports, five different models are estimated per possible direction of the GC. One model for the entire year 2013 and four quarterly models are presented. Each follows the model specification with the null hypothesis that there is no GC (i.e., that M2 does not reduce the forecast error):

$$
M 1: Y _ {t} = \alpha + \sum_ {i = 1} ^ {n} \beta_ {i} Y _ {t - 1} + \epsilon_ {t}
$$

$$
M 2: Y _ {t} = \alpha + \sum_ {i = 1} ^ {n} \beta_ {i} Y _ {t - 1} + \sum_ {i = 1} ^ {n} \gamma_ {i} X _ {t - 1} + \epsilon_ {t}
$$

n refers to the number of lags included in each model and t to a specific period. If only a small number of lags are included in the selection of the lag-length parameter, a present relation between the time series is potentially missed. Including many lags can lead to spurious results. The selection of this critical

#

parameter is outlined in the section presenting our analysis and empirical results. With the establishment of the method, the question as to which insights can be gained by the following analysis can be answered. The aim is to analyze whether and under which circumstances analyst reports and social media sentiments may be used to predict one another. Regarding the first question, the following cases might occur as a result of GC testing between the two types of content:

Case 1 – GC exists, in both directions between the two types of content. This provides mixed evidence supporting WoC considerations and the importance of expert knowledge. Due to the nature of GC testing, such cases are expected and the two theoretical foundations are not mutually exclusive.

Case 2 – Social media content is found to GC analyst reports. This proves that events were not foreseen by domain experts and were incorporated into the public opinions of social media users in a a more timely manner. Such a relation could indicate that, besides the known herding behavior of analysts, they also follow public opinion about a given company.

Case 3 - Analyst reports are found to GC social media content. This confirms that, due to superior knowledge, analysts are able to assess situations before the crowd can arrive at a similar conclusion. As it is unlikely that social media users have direct access to analyst reports, the impact of such reports on the opinion of the crowd has to be by proxy. This proxy occurs via traditional media channels reporting on the professionals’ opinions or individual star users within a social community.

<sup>-</sup> Case 4 – No GC is found between the two types of media content. The contained information appears to be independent from one another. This result indicates that the two types of data are not interchangeable. Still, this does not contraindicate their predictive power with regard to other data, such as stock returns.

## Sentiment Analysis

Sentiment scores are calculated for each document as an input for our GC testing. This is performed with the General Inquirer (GI) software and “Positiv” and “Negativ” categories from the Harvard IV-4 dictionary.<sup>41</sup> The use of such dictionaries assumes that the contained words have a prior polarity<sup>45</sup> (e.g., the word "good," when considered without context, will be perceived as positive by most people). This prior polarity is used to assign words to a sentiment category. However, a word’s prior polarity will not always coincide with its contextual polarity (e.g., "fast" might be contained as a positive word in a dictionary for the automobile domain and a text might contain the phrase "it broke fast"). In the case of such violations, bias is introduced. The sentiment score for each document i of company j is consequently calculated using a positivity measure:

#

$$
\text { Positivity } _ {i, j} = \frac {\text { pos } _ {i , j}}{\text { pos } _ {i , j} + \text { neg } _ {i , j}}
$$

Unless the analyzed text contained ${ > } 5 0$ words, and a positivity score could be calculated, observations were dropped. This resulted in a 4% reduction of social media data. After sentiment scores for each document have been calculated, the resulting social media and analyst report sentiment time series need to be scaled to a common frequency. A higher common frequency seems desirable for providing a large number of observations to test for GC. The large number of social media data observations allowed the analyst report data to dictate the achievable frequency. The number of available reports ranges from 166 (General Electric) to 541 (Cisco). As expected, many such quarterly report releases are published. A higher frequency of daily aggregates of report sentiment is not supported by the available data. Consequently, daily means of the positivity measure are calculated for both analyst reports and social media content. Missing values in the report series are added by linear interpolation. Figure 1 illustrates notable aspects of the data.

The left plot in the figure shows that stock analysts seem to be much more cheerful than the average social media user. Prior research indicates that, instead of recommendations or accuracy, analyst compensation is partially determined by the investment banking’s business generated after a report.<sup>22</sup> Twedt and Rees argue that this effect might be diminished when considering the full content of a report instead of focusing on the buy/hold/sell recommendation or forecast measure.<sup>44</sup> Analysts seem to be hesitant to use negative language. A possible way of addressing the apparent domain-specific language of stock analysts would be to compile a sentiment dictionary specifically for the domain. Z-Scores of both time series are used to normalize the two series around a common level.<sup>6</sup> This is achieved by subtracting the mean $( \mu )$ of the observations from each data point (x) before dividing them by their standard deviation (<sup>σ</sup>), resulting in the centered series illustrated in Fig. 1 (right):

$$
Z = \frac {x - \mu}{\sigma}
$$

There are fewer analyst reports than social media observations. This results in more volatile time series for the reports. However, this should be of no immediate consequence for GC testing.

## WoC Measures

In order to examine social media data, we introduce a number of measures intended to operationalize each WoC condition described by Surowiecki.<sup>42</sup>

## Diversity

#

Diversity is a driver of team performance in many disciplines. Diversity cannot always be measured easily in social media observations. Therefore, we rely on two established dimensions of diversity, including age and gender. Lee and Farh<sup>34</sup> found a positive interaction between gender diversity and group self-efficacy outcomes. In addition, gender diversity in the boardroom has been shown to have a positive influence on firm performance.

We follow Blau’s definition of group heterogeneity<sup>5</sup> describing nonhierarchical (nominal, inherently unranked) distinctions within groups. This definition of heterogeneity stands in contrast to a hierarchy emphasizing inequality, such as income differences or the “glass ceiling.” We derive Blau indices for heterogeneity, which are calculated as one minus the sum of squared group fractions per measured category type<sup>5</sup>:

$$
B l a u I n d e x = 1 - \sum_ {i = 1} ^ {N} P r o p _ {i} ^ {2},
$$

Prop<sub>i</sub> refers to the fraction of a specific group in the total population, i describes individual categories regarding a property (e.g., male or female for a gender index), and N refers to the total number of categories for the property. The value range of these indices varies depending on the number of categories included in a property, but it is always bound between zero and one.<sup>32</sup> A perfectly homogeneous group would result in an index equal to zero (the sum is 1). A “perfectly diverse” (i.e., distributed evenly across the categories) group receives a score of 0.5 for a property with two categories. A larger value corresponds to a more diverse group. Such measures are widely used to capture group diversity in multiple disciplines. Similar measures are available across several disciplines, such as the Gini,<sup>21</sup> Gibbs–Martin,<sup>19</sup> and Herfindahl–Hirschman indices.<sup>24</sup> Gender composition measures the male to female ratio of the data.

## Decentralization

Decentralization has been studied in many different systems. Its role as a determinant of health-care system performance has been examined.<sup>7</sup> Furthermore, decentralization has been studied in the context of government performance.<sup>17</sup> Kim and Burton found decentralized groups to perform better regarding cost and time, whereas centralized groups achieved better quality.<sup>29</sup>

No common studies have tested decentralization as a condition for WoC. In this analysis, we construct a geospatial measure to determine whether the geographical concentration of the crowd influences their predictive power regarding analyst sentiment.

The data contains 1163 unique location annotations. We calculate the concentration measure among those locations. The Platform Concentration measure refers to the type of social media platform (e.g., blog, microblog, forum, or social network) using a Blau index.

#

An additional location measure contains the average distance between users posting about a specific company within a specific period. Depending on availability, location annotations in the data mostly refer to the country, state, or city level. We geocode those locations to longitude–latitude coordinates and calculate the average distance between posts for a given period and company. Distance is calculated as the path on the surface of a unit sphere (radius = 1) between two sets of coordinates and scaled up to kilometers with the factor 1:6371 (earth radius in kilometers).

## Independence

Independence is the most abstract of the three conditions proposed by Surowiecki.<sup>42</sup> Independence depends on a user-to-user relationship within the crowd that is not =directly observable. Common social networks and social media sites are not structured in hierarchical tiers, and the data used here do not include the structure of the social network. Independence is expected to be the most fleeting condition to test. We construct a measure of author tone to capture how assertive each social media text is written.

The Semantic Authority measure is calculated similar to a text sentiment, using the “Modalweak” and “Modalstrong” categories from the Louhgran and McDonald 10-K dictionary.<sup>35</sup> These modal categories contain words commonly used to increase or decrease the assertiveness of a statement. For example, “always” or “definitely” are included in the “Modalstrong” category, while “maybe” or “could” are examples of the “Modalweak” category. We calculate the measure for the ith document and the jth company as follows:

$$
\text { Authority } _ {i, j} = \frac {\text { ModStrong } _ {i , j} - \text { ModWeak } _ {i , j}}{\text { ModStrong } _ {i , j} + \text { ModWeak } _ {i , j}}
$$

The variable is a tonal measure for an author’s certainty. An authority figure uses more strong modal words than someone who is influenced by the opinion of others. We use this variable to measure social media users' certainty and not that of analysts.

## Analysis and Empirical Results

## Granger Causality

Statistical results of the analysis are presented in two steps. GC testing results are first developed and interpreted. Second, these results are used in an analysis of circumstances leading to a particular GC direction. Following Bollen et al., who evaluated model performance based on p-values of the additional M2 time series,<sup>6</sup> a lag-length selection method was used. This method was chosen because of the large number of models in the analysis. Models for each company (30) in the sample and direction of the GC (2) are estimated for quarterly subsets and the entire annual time span of 2013. Models from lag-length n = 1 to n = 15 days are estimated. This results in 30×2×15×5 = 4500 models. The two mediums might have an inherently different reaction speed to new information, resulting in a uniform-direction GC between the content types. The direction of GC may also depend on the type of information and company at hand. While the latter scenario corresponds to the hypotheses outlined in section 2.3, it is worth exploring the alternative. For each of the 15 lag lengths, the number of models with a significant relationship between the series pairs (i.e., those models with a p-value smaller than 10%) are reported here. If one of the two mediums is inherently faster than the other, higher numbers of GC going in one direction will be observed. Table 2 demonstrates these results. The first row shows models in which social media sentiment was used to augment analyst report sentiment. The second shows results of the opposite direction.

The number of lags resulting in the largest amount of significant models is identical in both prediction directions. Another sample (e.g., requiring another minimal text length or including minimal dictionary hit counts) may result in different optimal parameters for the two directions. There appears to be an actual maximum (i.e., both smaller and longer lag selections reduce the number of significant models). However, no strong imbalance between the two directions of GC is observed. This proves that the GC between the two mediums is driven by more circumstances than an inherent imbalance in reaction speed between the two mediums. A lag length of 10 periods creates the largest number of significant relationships. However, there is no indication that this number of lags is preferable for all series pairs, as other lag lengths produce a similar amount of significant models. Therefore, another set of models is estimated in which the laglength parameter is not chosen simultaneously for all models. Instead, the estimation is made individually for each of the 300 models. The aim is to minimize the p-value of the model. The results of this second selection of models are reported in Table 3.

The p-value-based lag-length selection procedure improves the number of significant models from 57 (19%) to 127 (42%). Of the 127 significant models, 68 (45.3%) predict analyst report sentiment by social media sentiment and 59 (39.3%) predict social media sentiment via analyst report sentiment. Both directions of prediction appear to be feasible. The preprocessing of input documents was performed similarly for both types of content and all companies. Improvements can be made by introducing a casespecific preprocessing logic. As the question of interest in this work is not case specific, an applied uniform logic seems sufficient. Given these results the question arises as to which situation leads to which kind of GC relationship (i.e., what kind of company is more prone to either direction of GC or what situation fosters this tendency).

## Drivers of Crowd Wisdom

We create binary response models to explore the drivers of crowd wisdom. The chance that a given set of circumstances leads to GC in either direction was estimated with a separate model for each direction.

We estimate one model for each direction of GC. There are two reasons why two models per situation are estimated. First, as Table 3 indicates, the two directions of GC are not mutually exclusive. Second, the Social model (M2) can serve as a benchmark for the WoC model. Therefore, a single binary encoding of the GC direction would omit cases where both directions are significant. Generalized linear models (GLMs) using log-link functions are estimated (Logit). For the “Analyst” model (M1), the dependent variable is 1 if the social media data were found to GC analyst reports in a given period and firm (i.e., if the p-value in Table 3 is <0.1). In the opposite case, the dependent variable in the “Social” model (M2) is 1. If the measured variables derived from the theoretical WoC constructs proposed by Surowiecki<sup>42</sup> help us understand the situation in which crowd wisdom emerges, M1 should be the better overall model. The theoretical argument for our measures only holds true in this direction. Consequently, M2 can serve as a benchmark for the results of M1. The independent variables included in these models are split into four groups. We provide a brief overview of the intention and composition of each group in the next section, before discussing the results for each of these categories.

## Discussion and Interpretation

WoC Measures: In this category, we group the main WoC measures of this study. The first five variables refer to the previously derived Blau index measures for age, geolocations, platform diversity, and author name diversity. Authority refers to the tonal authority measure. This variable is followed by the average age of social media users in a given period–company combination and age variance.

Platform diversity increases the likelihood of GC between the two types of content in either direction. The significant coefficient in the “Analyst ← Social” model supports the WoC theory. By contrast, the negative coefficient of age diversity in the same model contradicts the WoC theory, suggesting that any form of cognitive diversity improves the group consensus. An increase in the average age of users decreases their predictive capabilities. A slight depreciation of cognitive ability with age might be expected. However, this depreciation seems counterintuitive, as older users are expected to become more experienced in their assessments. The negative coefficient for authority suggests that users who are sure of their opinion decrease the quality of the group's mean sentiment. This is in line with the expectation of the WoC theory, which suggests that an independent crowd should perform better. The corresponding coefficient in the “Social ← Analyst” case suggests that certainty in social media posts decreases the likelihood of analysts predicting their sentiment.

Overall, the results of the WoC measures for the theoretical constructs described by Surowiecki<sup>42</sup> are promising. The model indicates that there is indeed a measurable connection between the makeup of the crowd and its ability to explain analyst opinion. Although it is difficult to compare results between different content domains, this is in line with previous WoC research, such as the efforts to explain the content quality of Wikipedia<sup>2</sup> or its comparable quality to classical encyclopedias.<sup>20</sup> Interestingly, this suggests that WoC can arise without a system specifically designed to allow the crowd to aggregate their opinion. Previous research highlights the importance of group coordination for content quality.<sup>31</sup> In our case, this aggregation only takes place after the fact using sentiment analysis. Examining how the support of the crowd’s coordination may improve their information processing capabilities is an interesting question for future research.

Industry Dummies: The main industry classification of a company may be of use when searching for companies for which GC is present between the two content types. We observe intuitive results in several industries. Both energy and industrial companies are unfavorable for the “Analyst ← Social” case, whereas consumer staples, diversified and financial companies, favor the “Social ← Analyst” case. The financial industry dummy deserves special attention: Although this industry does favor the “Social ← Analyst” case, no significant reduction of prediction quality in the “Analyst ← Social” case can be observed. Overall, the industry dummies confirm previous studies indicating that stock analysts’ recommendations do indeed carry inherent value.<sup>46</sup> At the same time, no significant support for any industry in the sample adds explanatory power to the crowd’s opinion.

Company Specific: We include revenue and operating income, research and development (R&D) budgets, issuer ratings and the (ultimate) number of subsidiaries of a given company. We observe a decrease in the capabilities of the crowd to predict analyst sentiment for companies with a higher number of subsidiaries. This might be because large multinational companies are too complex to be summarized by a single measure of crowd opinion. The crowd may have a positive opinion of one division of a firm, while expressing a negative one about another. The “Social ← Analyst” case demonstrates a positive effect of revenue, suggesting that expert opinion is more informative for larger companies. Another possible method of interpreting this result is to suggest that experts be more careful in their evaluation of larger companies. This would be an interesting question for future research, because all companies in the sample are comparatively large (in order to make sure there are enough social media posts and analyst reports).

A larger R&D budget also exhibits a similar effect. Company size overall has a negative effect on the comparative quality of the “Analyst ← Social” case possibly due to the aggregation of all crowd opinions to a single opinion. This weakness can be eliminated using topic-mining methods and calculating topicspecific sentiments in order to capture more nuances of the crowd’s opinion on different divisions of larger companies.

News Dummies: Using the Guardian API data mentioned in Table 1, the most common (median) news category for each period and company is extracted and introduced to the dummy coding models. We include the median news category to see whether specific types of novel information favor one of the two groups’ information processing capabilities. The results indicate that business news decreases the likelihood of analysts’ ability to predict social media users. This supports the known tendency of analysts opinions. Media network news decreases the predictive power of social media users. Many social media posts coinciding with this median news category may be concerned with product debates, rather than company evaluations. Only the environmental news dummy provides a significant increase in the likelihood of WoC. This finding seems intuitive if negative events, such as chemical spills, occur. Overall, the news categories provide intuitive results, suggesting that the chosen sentiment measure for the two content types indeed provides an adequate aggregation of the groups’ opinion.

## Controls

We aggregate three variables in this group. The first variable “URL Blau” serves as a verification of the diversity in URLs, rather than platform diversity. It can be used to assess the decentralization of the observations. We do not group this variable with the WoC measures because, in contrast to platform diversity, which is based on a curated field generated from our social media data, this measure is less certain to capture the diversity concept as proposed by the WoC theory. Interestingly, this measure exhibits a negative coefficient. This may be explained by an effect resulting from crowds being too diverse or decentralized, thus preventing crowd wisdom to emerge. This interesting finding can be explored in future research.

The second variable “COL Readability” is computed as the average Coleman–Liau Index for the social media posts in each period.<sup>12</sup> Such readability measures intend to rate the complexity of speech in a document and may serve as a proxy for author education. The positive coefficient indicates that more advanced syntax correlates with better crowd judgment.

The third variable “Authority Var.” computes the variance of our authority measure instead of its period mean. We choose to report it in the controls group because a variance measure is less distinguishable from a diversity measure than the mean specification. It is less compatible with the theoretical foundation of the analysis. However, as the two measures are not highly correlated and the variance measure adds power to the model, practitioners may be interested in including both specifications in their analyses. From the WoC theoretical standpoint of the study, this measure may be interpreted as a diversity, rather than an independence measure, the theoretical integration of which can be studied in future.

Altogether, the two models suggest that the WoC theory indeed provides useful constructs that can be operationalized to explain when the crowd can arrive at opinions prior to the availability of expert assessment. The following provides a brief overview of the results of both stages of our analysis regarding the initial hypotheses:

H1a (Situational direction of GC): The results indicate that this is indeed true; no uniform GC direction can be established between the two types of content.

H1b (Analyst expertise and privileged access matter): This hypothesis is supported by the negative coefficients in the industry dummies (analyst model) regarding energy and industrial companies. In addition, the positive coefficients in M2 for financials and consumer staples indicate that these types of companies require analyst expertise.

H1c (When relevant information is public and diverse, independent opinions can be aggregated, and the crowd has an advantage): This is supported by the positive coefficient of the environmental news category when analyst reports are predicted, as well as the negative coefficient of the sport news category in the opposite direction.

Thus, the analysis provides evidence for H1a and H1b, whereas evidence in support of H1c is sparse.

H2 (Satisfaction of WoC conditions should improve social media users’ opinion quality): Our results provide mixed evidence regarding this hypothesis. The hypothesis is supported by the positive effect of platform diversity. However, both age diversity measures show negative effects on the dependent variable. Gender diversity shows no significant effect.

## Implications

As discussed, our results add to the growing body of work suggesting that WoC as a phenomenon can be used to explain the sometimes surprising quality of the content created by large groups<sup>20,31</sup> as well as the value of stock opinions of social media users.<sup>10</sup> Our contribution to this body is twofold. First, the comparison to stock analysts allows us to benchmark the crowd wisdom against an expert group. The results of our GC analysis suggest that in some situations the crowd can add information in a more timely manner than experts,. Second, our analysis supports the WoC theory as proposed by Surowiecki.<sup>42</sup> Through the operationalization of the independence, decentralization, and diversity constructs, which

#

constitute the central pillars of the theory, the contribution of each condition to the WoC is examined. Furthermore, we examine the conditions beyond those proposed by WoC theory under which the crowd is wise. The results indicate that crowd wisdom exists, although it is highly dependent on the conditions described by the WoC theory and the degree to which particular subjects appeal to the crowd’s interest. This suggests that more constructs may be needed to fully explain when a crowd is wise than are included in the current WoC theory. Future research should focus on discovering additional determinants of crowd wisdom. Although sentiment as an aggregate measure for crowd opinion works in principle, the results suggest additionally that complex or conflicting topics, which may be especially prevalent for larger companies, may require more complex aggregation methods for the crowd’s diverse opinions.

We divide the practical implications of this research into implications for the financial sector and those for social media users and platforms. Within the financial sector, our results inform the customers of analysts about the conditions under which analyst research is especially valuable, but also when it may be wise to resort to social media monitoring tools to gauge the crowd’s opinion. The results also inform the customers how to aggregate the opinions of social media users. Similarly, stock analysts are informed of the circumstances under which it may be wise to listen to social media users’ opinions as an additiona source of information, but also when they are unlikely to provide valuable information.

In addition, the operationalization of WoC-related constructs can help companies refine their social media monitoring tools to better reflect the diverse opinion of the crowd. After companies, this should also be of interest to social media content aggregators who need to know the kind of data on social media users that interest their customers.

Finally, special-purpose social networks such as stock recommendation communities<sup>40</sup> and social lending communities<sup>16</sup> are fundamentally based on the assumption of crowd wisdom. The members of such communities expect these platforms to provide them with insights gained from this crowd wisdom. Our WoC theory-based results provide the administrators of such communities with evidence on the makeup of wise crowds. While such communities are unlikely to actively control the characteristics of the user group making up their community, our results may prove useful regarding the user selection for the samples of users that are chosen to compute their crowd-based recommendations.

## Limitations

This study has methodological and theoretical limitations, which warrant discussion. There is no reliable method of determining which portion of social media users are professional or “hobby” analysts. A more controlled experiment using a single social network would be an interesting avenue for future research. In addition, because of their herding tendency, analysts could exhibit some WoC effects. Reactions falling out of the n = 15 lag length included in the analysis may be missed. Large lag lengths can lead to spurious

#

correlations. This methodological trade-off has to be accepted. Using a larger and more diverse set of companies and multiyear samples could provide interesting results. The available data do not provide insight into the social hierarchy of social media users, which may provide a more suitable measure of independence as a precursor to WoC. Finally, the aggregation of social media users’ opinions to the singular sentiment measure sacrifices the diversity of opinions of the group. Other measures may well be more suited to capture this diversity. Beyond these methodological considerations, it is also important to keep in mind that the domain of company-specific opinions may not be comparable to other areas of WoC research. The reproduction of a similar analysis for a noneconomic domain could provide an interesting comparison.

## Conclusion

The aim of this research was to investigate a possible relation between the prediction power of stock analysts’ sentiment and that of "the crowd" (i.e., a large set of social media users). Earlier studies have identified inefficiencies in professional analysts’ decision processes. The WoC theory suggests that the crowd might be able to mitigate these problems.

GC testing between the two types of content showed statistically significant relations for a large number of cases in this sample. This finding indicates that the two types of content can be used to predict the other in many cases. However, evidence for the similar use of the two types of content is lacking. Similarly, no evidence is provided as to the contents' complementarity (keeping in mind the emerging issue of multicollinearity). The practical applications of such relationships include algorithmic trading, news reporting, and customer relations.

Logit models provide information on the circumstances under which social media content sentiment can be used to predict analyst reports, and vice versa.

There is mixed evidence supporting WoC theory. Platform diversity in the social media sample increases the crowd’s success, whereas age diversity decreases it. This finding might be mitigated by a larger sample. A larger sample introduces more variance in company type, spanning a significantly longer period. Evidence for the WoC theory is provided by cases in which social media users arrived at a (collective) opinion, before professional stock analysts were able to include environmental changes into their reports.

These results suggest that crowd wisdom can outperform experts if information is instantly available. However, the drivers of crowd wisdom might not be sufficiently explained by the current WoC theory.

Professional analysts seem to react quicker to technical issues, such as changes in financial situations. Therefore, this study supports the WoC theory (i.e., the general possibility of crowd wisdom), although the drivers of this wisdom have not been fully understood yet.

## References

[1] J.R. Anderson, Cognitive skills and their acquisition, Psychology Press, 1981.

[2] O. Arazy, W. Morgan, R. Patterson, Wisdom of the Crowds: Decentralized Knowledge Construction in Wikipedia, 16th Annu. Work. Inf. Technol. Syst. Pap. (2006).

[3] B. Barber, R. Lehavy, M. McNichols, B. Trueman, Can investors profit from the prophets? Security analyst recommendations and stock returns, J. Finance. 56 (2001) 531–563.

[4] R. Barniv, O.-K. Hope, M.J. Myring, W.B. Thomas, Do analysts practice what they preach and should investors listen? Effects of recent regulations, Account. Rev. 84 (2009) 1015–1039.

[5] P.M. Blau, Inequality and heterogeneity: A primitive theory of social structure, Free Press New York, 1977.

[6] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, J. Comput. Sci. 2 (2011) 1–8.

[7] T. Bossert, Analyzing the decentralization of health systems in developing countries: decision space, innovation and performance, Soc. Sci. Med. 47 (1998) 1513–1527.

[8] M.T. Bradshaw, Analyst information processing, financial regulation, and academic research, Account. Rev. 84 (2009) 1073–1083.

[9] K. Campbell, A. Mínguez-Vera, Gender Diversity in the Boardroom and Firm Financial Performance, J. Bus. Ethics. 83 (2007) 435–451.

[10] H. Chen, P. De, Y. (Jeffrey) Hu, B.-H. Hwang, Wisdom of Crowds: The Value of Stock Opinions Transmitted Through Social Media, Rev. Financ. Stud. 27 (2014) 1367–1403.

[11] M.B. Clement, S.Y. Tse, Financial analyst characteristics and herding behavior in forecasting, J. Finance. 60 (2005) 307–341.

[12] M. Coleman, T.L. Liau, A computer readability formula designed for machine scoring., J. Appl. Psychol. 60 (1975) 283.

[13] T.E. Damar, Attacking Faulty Reasoning: A Practical Guide to Fallacy-Free Arguments, Belmont, CA: Thomson Wadsworth, 2005.

[14] E. Dimson, M. Mussavian, A brief history of market efficiency, Eur. Financ. Manag. 4 (1998) 91– 103.

[15] P.T. Elgers, M.H. Lo, R.J. Pfeiffer, Delayed Security Price Adjustments to Financial Analysts’ Forecasts of Annual Earnings, Account. Rev. 76 (2001) 613–632.

[16] C.R. Everett, Group Membership, Relationship Banking and Loan Default Risk: The Case of Online Social Lending, SSRN Electron. J. 7 (2010).

[17] J.-P. Faguet, Decentralization and Local Government Performance: Improving Public Service Provision in Bolivia, Rev. Econ. Del Rosario. 3 (2000) 127–176.

[18] R. Frankel, S.P. Kothari, J. Weber, Determinants of the informativeness of analyst research, J. Account. Econ. 41 (2006) 29–54.

[19] J.P. Gibbs, W.T. Martin, Urbanization, Technology, and the Division of Labor: International Patterns on JSTOR, Am. Sociol. Rev. 27 (1962) 667–677.

[20] J. Giles, Internet encyclopaedias go head to head, Nature. 438 (2005) 900–901.

[21] C. Gini, Variabilit{à} e mutabilit{à}, Repr. Mem. Di Metodol. Stat. (Ed. Pizetti E, Salvemini, T). Rome Libr. Eredi Virgilio Veschi. 1 (1912).

[22] B. Groysberg, P.M. Healy, D.A. Maber, What Drives Sell-Side Analyst Compensation at High-Status Investment Banks?, J. Account. Res. 49 (2011) 969–1000.

[23] S. Hill, N. Ready-Campbell, Expert stock picker: the wisdom of (experts in) crowds, Int. J. Electron. Commer. 15 (2011) 73–102.

[24] A.O. Hirschman, The paternity of an index, Am. Econ. Rev. (1964) 761–762.

[25] H. Hong, J. Kubik, A. Solomon, Security Analysts’ Career Concerns and Herding of Earnings Forecasts, RAND J. Econ. 31 (2000) 121.

[26] H. Hong, T. Lim, J.C. Stein, Bad News Travels Slowly: Size, Analyst Coverage, and the Profitability of Momentum Strategies, J. Finance. 55 (2000) 265–295.

[27] P.J.. Irvine, Do analysts generate trade for their firms? Evidence from the Toronto stock exchange, J. Account. Econ. 30 (2000) 209–226.

[28] R. Johnston, B.F. McNeal, Statistical versus clinical prediction: Length of neuropsychiatric hospital stay., J. Abnorm. Psychol. 72 (1967) 335.

[29] J. Kim, R.M. Burton, The Effect of Task Uncertainty and Decentralization on Project Team Performance, Comput. Math. Organ. Theory. 8 (2002) 365–384.

[30] G. Kirchgässner, J. Wolters, U. Hassler, Introduction to modern time series analysis, Springer, 2012.

[31] A. Kittur, R.E. Kraut, Harnessing the wisdom of crowds in wikipedia, in: Proc. ACM 2008 Conf. Comput. Support. Coop. Work - CSCW ’08, ACM Press, New York, New York, USA, 2008: p. 37.

[32] J. Konrad, Alison M and Prasad, Pushkala and Pringle, Handbook of Workplace Diversity, Sage, London, 2006.

[33] J. Larkin, J. McDermott, D.P. Simon, H.A. Simon, Expert and novice performance in solving physics problems, Science (80-. ). 208 (1980) 1335–1342.

[34] C. Lee, J.-L. Farh, Joint Effects of Group Efficacy and Gender Diversity on Group Cohesion and Performance, Appl. Psychol. 53 (2004) 136–154.

[35] T. Loughran, B. McDonald, When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks, J. Finance. 66 (2011) 35–65.

[36] B.G. Malkiel, E.F. Fama, EFFICIENT CAPITAL MARKETS: A REVIEW OF THEORY AND EMPIRICAL WORK\*, J. Finance. 25 (1970) 383–417.

[37] M. Nofer, O. Hinz, Are crowds on the internet wiser than experts? The case of a stock prediction community, J. Bus. Econ. 84 (2014) 303–338.

[38] M. Nofer, O. Hinz, Using Twitter to Predict the Stock Market, Bus. Inf. Syst. Eng. 57 (2015) 229– 242.

[39] J. Pearl, Causality, Cambridge university press, 2009.

[40] M.K. Poetz, M. Schreier, The value of crowdsourcing: can users really compete with professionals in generating new product ideas?, J. Prod. Innov. Manag. 29 (2012) 245–256.

[41] P.J. Stone, D.C. Dunphy, M.S. Smith, D.M. Ogilive, The General Inquirer, The M.I.T. Press, Cambridge, Massachusetts, 1966.

[42] J. Surowiecki, The wisdom of crowds, Random House LLC, 2005.

[43] B. Trueman, Analyst Forecasts and Herding Behavior, Rev. Financ. Stud. 7 (1994) 97–124.

[44] B. Twedt, L. Rees, Reading between the lines: An empirical examination of qualitative attributes of financial analysts’ reports, J. Account. Public Policy. 31 (2012) 1–21.

[45] T. Wilson, J. Wiebe, P. Hoffmann, Recognizing contextual polarity in phrase-level sentiment analysis, in: Proc. Conf. Hum. Lang. Technol. Empir. Methods Nat. Lang. Process., 2005: pp. 347– 354.

[46] K.L. Womack, Do brokerage analysts’ recommendations have investment value?, J. Finance. 51 (1996) 137–167.

## Jan Muntermann:

Jan Muntermann holds the Chair of Electronic Finance and Digital Markets in the Faculty of Economic Sciences, University of Göttingen. His research interests include the design and analysis of information systems, business intelligence and analytics, IT governance and research methodology. He has published in journals such as Information Systems Research, Decision Support Systems, and European Journal of Information Systems.

## Matthias Eickhoff:

Matthias Eickhoff is a Ph.D. student at the Chair of Electronic Finance and Digital Markets in the Faculty of Economic Sciences, University of Göttingen. His research interests include the analysis of unstructured data, text mining and business intelligence in the financial domain. He holds a M.Sc. in Finance, Accounting and Taxes. His work has appeared in the proceedings of the conferences on Design Science Research in Information Systems and Technology and the Pacific Asian Conference on Information Systems.

## Figure Caption

Figure 1: Daily sentiment means (left) and z-scores (right) of daily sentiment means for Cisco. The gray line denotes social media and the black line analyst sentiment. The daily mean counts on the charts refer to the number of available daily data points prior to linear interpolation of missing values.

## Tables

Table 1: Observation counts for analyst report (TRAA), social media (SDL), and news (Guardian Open Platform) data.

<table><tr><td>Company Name</td><td>Analyst Reports</td><td>Social Media</td><td>Public News</td></tr><tr><td>3M</td><td>177</td><td>127,547</td><td>435</td></tr><tr><td>AT&amp;T</td><td>345</td><td>83,053</td><td>101</td></tr><tr><td>American Express</td><td>356</td><td>152,781</td><td>6889</td></tr><tr><td>Boeing</td><td>510</td><td>141,357</td><td>136</td></tr><tr><td>Caterpillar</td><td>362</td><td>133,019</td><td>78</td></tr><tr><td>Chevron</td><td>249</td><td>144,790</td><td>57</td></tr><tr><td>Cisco</td><td>541</td><td>152,742</td><td>81</td></tr><tr><td>Coca Cola</td><td>190</td><td>127,533</td><td>257</td></tr><tr><td>Disney</td><td>250</td><td>153,809</td><td>461</td></tr><tr><td>DuPont</td><td>272</td><td>148,654</td><td>44</td></tr><tr><td>Exxon</td><td>204</td><td>133,028</td><td>65</td></tr><tr><td>General Electric</td><td>166</td><td>140,357</td><td>7531</td></tr><tr><td>Goldman</td><td>232</td><td>142,807</td><td>293</td></tr><tr><td>Home Depot</td><td>253</td><td>144,170</td><td>3</td></tr><tr><td>IBM</td><td>337</td><td>146,425</td><td>135</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

<table><tr><td>Company Name</td><td>Analyst Reports</td><td>Social Media</td><td>Public News</td></tr><tr><td>Intel</td><td>525</td><td>147,317</td><td>157</td></tr><tr><td>JP Morgan</td><td>331</td><td>140,364</td><td>71</td></tr><tr><td>Johnson&amp;Johnson</td><td>361</td><td>141,091</td><td>1900</td></tr><tr><td>McDonald&#x27;s</td><td>375</td><td>142,714</td><td>109</td></tr><tr><td>Merck</td><td>397</td><td>140,500</td><td>27</td></tr><tr><td>Microsoft</td><td>464</td><td>156,697</td><td>759</td></tr><tr><td>Nike</td><td>236</td><td>129,887</td><td>241</td></tr><tr><td>Pfizer</td><td>252</td><td>142,273</td><td>49</td></tr><tr><td>Procter &amp; Gamble</td><td>264</td><td>111,625</td><td>458</td></tr><tr><td>Travelers</td><td>212</td><td>4,413</td><td>167</td></tr><tr><td>UnitedHealth</td><td>281</td><td>41,876</td><td>14</td></tr><tr><td>United Technology</td><td>268</td><td>44,247</td><td>1</td></tr><tr><td>Verizon</td><td>405</td><td>155,642</td><td>204</td></tr><tr><td>Visa</td><td>291</td><td>137,386</td><td>401</td></tr><tr><td>Walmart</td><td>333</td><td>106,735</td><td>154</td></tr><tr><td>Total</td><td>9,439</td><td>3,814,839</td><td>21,278</td></tr></table>

Table 2: Number of significant models in both prediction directions for social media and analyst report sentiment, n = 1–15. Maxima are highlighted.

<table><tr><td>n-lag</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>Analyst ← Social</td><td>21</td><td>20</td><td>13</td><td>18</td><td>19</td><td>17</td><td>23</td><td>20</td><td>20</td><td>30</td><td>27</td><td>29</td><td>29</td><td>26</td><td>24</td></tr><tr><td>Social ← Analyst</td><td>23</td><td>20</td><td>20</td><td>18</td><td>18</td><td>20</td><td>20</td><td>25</td><td>19</td><td>27</td><td>23</td><td>27</td><td>23</td><td>22</td><td>21</td></tr><tr><td>Sum</td><td>44</td><td>40</td><td>33</td><td>36</td><td>37</td><td>37</td><td>43</td><td>45</td><td>39</td><td>57</td><td>50</td><td>56</td><td>52</td><td>48</td><td>45</td></tr></table>

Table 3: p-values (three-digit rounding) of GC tests for quarterly subsamples and annual data. Optimal lag length for each individual time series pair based on lag lengths between 1 and 15 (p-values ≤ 10% are highlighted). The first row indicates the test direction (e.g., the Analyst heading indicates that reports are predicted via social media content). The sums refer to the number of significant models in columns and rows.

<table><tr><td rowspan="2">Company</td><td colspan="5">Analyst ←Social</td><td colspan="5">Social ← Analyst</td><td rowspan="2">Sum</td></tr><tr><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Annual</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Annual</td></tr><tr><td>3M</td><td>0.759</td><td>0.385</td><td>0.073</td><td>0.064</td><td>0.113</td><td>0.05</td><td>0.215</td><td>0.09</td><td>0.044</td><td>0.416</td><td>5</td></tr><tr><td>American Express</td><td>0.297</td><td>0.305</td><td>0.216</td><td>0.355</td><td>0.264</td><td>0.341</td><td>0.025</td><td>0.06</td><td>0.277</td><td>0.168</td><td>2</td></tr><tr><td>AT&amp;T</td><td>0.155</td><td>0.176</td><td>0.3</td><td>0.225</td><td>0.229</td><td>0.512</td><td>0.31</td><td>0.082</td><td>0.279</td><td>0.124</td><td>1</td></tr><tr><td>Boeing</td><td>0.066</td><td>0.176</td><td>0.423</td><td>0.269</td><td>0.312</td><td>0.008</td><td>0.195</td><td>0.082</td><td>0.24</td><td>0.012</td><td>4</td></tr><tr><td>Caterpillar</td><td>0.027</td><td>0.336</td><td>0.217</td><td>0.039</td><td>0.001</td><td>0.338</td><td>0.532</td><td>0.25</td><td>0.036</td><td>0.044</td><td>5</td></tr><tr><td>Chevron</td><td>0.096</td><td>0.239</td><td>0.116</td><td>0.046</td><td>0.109</td><td>0.103</td><td>0.331</td><td>0.006</td><td>0.133</td><td>0.381</td><td>3</td></tr><tr><td>Cisco</td><td>0.062</td><td>0.351</td><td>0.004</td><td>0.17</td><td>0.079</td><td>0.576</td><td>0.024</td><td>0.115</td><td>0.188</td><td>0.033</td><td>5</td></tr><tr><td>Coca Cola</td><td>0.233</td><td>0.065</td><td>0.045</td><td>0.062</td><td>0.079</td><td>0.031</td><td>0.001</td><td>0.745</td><td>0.194</td><td>0.125</td><td>6</td></tr><tr><td>Disney</td><td>0.005</td><td>0.107</td><td>0.216</td><td>0.167</td><td>0.23</td><td>0.195</td><td>0.019</td><td>0.145</td><td>0.164</td><td>0.017</td><td>3</td></tr><tr><td>DuPont</td><td>0.056</td><td>0.06</td><td>0.187</td><td>0.02</td><td>0.357</td><td>0.223</td><td>0.73</td><td>0.005</td><td>0.001</td><td>0.071</td><td>6</td></tr><tr><td>Exxon</td><td>0.013</td><td>0.059</td><td>0.161</td><td>0.257</td><td>0.021</td><td>0.062</td><td>0.051</td><td>0.162</td><td>0.036</td><td>0.147</td><td>6</td></tr><tr><td>General Electric</td><td>0</td><td>0.125</td><td>0.514</td><td>0.008</td><td>0.009</td><td>0</td><td>0.912</td><td>0.03</td><td>0.289</td><td>0.14</td><td>5</td></tr><tr><td>Goldman</td><td>0.124</td><td>0.023</td><td>0.018</td><td>0.622</td><td>0.112</td><td>0.735</td><td>0.133</td><td>0.306</td><td>0.052</td><td>0.493</td><td>3</td></tr><tr><td>Home Depot</td><td>0.068</td><td>0.151</td><td>0.21</td><td>0.285</td><td>0.101</td><td>0.06</td><td>0.699</td><td>0.042</td><td>0.05</td><td>0.028</td><td>5</td></tr><tr><td>IBM</td><td>0.007</td><td>0.007</td><td>0.454</td><td>0.013</td><td>0.111</td><td>0.24</td><td>0.241</td><td>0.007</td><td>0.035</td><td>0.288</td><td>5</td></tr><tr><td>Intel</td><td>0.016</td><td>0.075</td><td>0.234</td><td>0.56</td><td>0.683</td><td>0.117</td><td>0.01</td><td>0.11</td><td>0.059</td><td>0.227</td><td>4</td></tr><tr><td>Johnson&amp;Johnson</td><td>0.052</td><td>0.369</td><td>0.014</td><td>0.066</td><td>0.427</td><td>0.053</td><td>0.167</td><td>0.12</td><td>0.161</td><td>0.216</td><td>4</td></tr><tr><td>JP Morgan</td><td>0.02</td><td>0.242</td><td>0.029</td><td>0.046</td><td>0.403</td><td>0.013</td><td>0.724</td><td>0.153</td><td>0.011</td><td>0.032</td><td>6</td></tr><tr><td>McDonald's</td><td>0.009</td><td>0.118</td><td>0.095</td><td>0.079</td><td>0.065</td><td>0.048</td><td>0.477</td><td>0.012</td><td>0.484</td><td>0.452</td><td>6</td></tr><tr><td>Merck</td><td>0.459</td><td>0.184</td><td>0.041</td><td>0.658</td><td>0.771</td><td>0.576</td><td>0.329</td><td>0.002</td><td>0.698</td><td>0.475</td><td>2</td></tr><tr><td>Microsoft</td><td>0.347</td><td>0.212</td><td>0.218</td><td>0.106</td><td>0.012</td><td>0.568</td><td>0.239</td><td>0.446</td><td>0</td><td>0.462</td><td>2</td></tr><tr><td>Nike</td><td>0.035</td><td>0.019</td><td>0.014</td><td>0.001</td><td>0.056</td><td>0.213</td><td>0.522</td><td>0.174</td><td>0.245</td><td>0.67</td><td>5</td></tr><tr><td>Pfizer</td><td>0.025</td><td>0.13</td><td>0.037</td><td>0.032</td><td>0.007</td><td>0.025</td><td>0.162</td><td>0.16</td><td>0.707</td><td>0.039</td><td>6</td></tr><tr><td>Procter &amp; Gamble</td><td>0.174</td><td>0.254</td><td>0.147</td><td>0.018</td><td>0.071</td><td>0.295</td><td>0.078</td><td>0.001</td><td>0.101</td><td>0.056</td><td>5</td></tr><tr><td>Travelers</td><td>0.045</td><td>0.267</td><td>0.158</td><td>0.872</td><td>0.406</td><td>0.034</td><td>0.061</td><td>0.334</td><td>0.067</td><td>0.193</td><td>4</td></tr><tr><td>UnitedHealth</td><td>0.189</td><td>0.247</td><td>0.001</td><td>0.475</td><td>0.042</td><td>0.15</td><td>0.304</td><td>0.126</td><td>0.187</td><td>0.504</td><td>2</td></tr><tr><td>United Technology</td><td>0.168</td><td>0.139</td><td>0.028</td><td>0.324</td><td>0.205</td><td>0.447</td><td>0.051</td><td>0.097</td><td>0.005</td><td>0.019</td><td>5</td></tr><tr><td>Verizon</td><td>0.008</td><td>0.47</td><td>0.007</td><td>0.179</td><td>0.059</td><td>0.259</td><td>0.733</td><td>0.196</td><td>0.192</td><td>0.688</td><td>3</td></tr><tr><td>Visa</td><td>0.232</td><td>0.133</td><td>0.068</td><td>0.766</td><td>0.094</td><td>0.122</td><td>0.043</td><td>0.167</td><td>0.73</td><td>0.238</td><td>3</td></tr><tr><td>Walmart</td><td>0.127</td><td>0.092</td><td>0.014</td><td>0.585</td><td>0.052</td><td>0.282</td><td>0.023</td><td>0.027</td><td>0.238</td><td>0</td><td>6</td></tr><tr><td>Sum</td><td>18</td><td>8</td><td>15</td><td>13</td><td>14</td><td>11</td><td>11</td><td>14</td><td>12</td><td>11</td><td>127</td></tr></table>

Table 4: Analyst ← Social describes the case in which analyst reports are Granger-caused by social media content and vice versa. Quarterly data were used (i.e., 4 quarter times 30 companies equals No. Obs.). The dependent variable is given by a binary coding of the results in Table 3 (p ≤ 0.1 or not). All noncategorica variables are standardized.

<table><tr><td colspan="2" rowspan="2"></td><td colspan="3">M1: Analyst ← Social</td><td colspan="3">M2: Social ← Analyst</td></tr><tr><td>Estimate</td><td>Std. Error</td><td>Pr(&gt;|z|)</td><td>Estimate</td><td>Std. Error</td><td>Pr(&gt;|z|)</td></tr><tr><td rowspan="10">WoC Measures</td><td>(Intercept)</td><td>10.061</td><td>3.972</td><td>0.011</td><td>1.454</td><td>2.607</td><td>0.577</td></tr><tr><td>Age Blau</td><td>-1.097</td><td>0.768</td><td>0.153</td><td>0.729</td><td>0.612</td><td>0.234</td></tr><tr><td>Geo Blau</td><td>1.86</td><td>0.979</td><td>0.058</td><td>-0.28</td><td>0.566</td><td>0.621</td></tr><tr><td>Platform Blau</td><td>3.876</td><td>1.409</td><td>0.006</td><td>1.564</td><td>0.926</td><td>0.091</td></tr><tr><td>Name Blau</td><td>0.616</td><td>1.404</td><td>0.661</td><td>0.107</td><td>0.344</td><td>0.755</td></tr><tr><td>Authority</td><td>-5.815</td><td>1.702</td><td>0.001</td><td>-2.269</td><td>0.835</td><td>0.007</td></tr><tr><td>Avg. Age</td><td>-3.498</td><td>1.42</td><td>0.014</td><td>-0.359</td><td>0.633</td><td>0.57</td></tr><tr><td>Age Var.</td><td>0.809</td><td>0.706</td><td>0.252</td><td>-0.9</td><td>0.53</td><td>0.09</td></tr><tr><td>Avg. Distance</td><td>1.335</td><td>0.795</td><td>0.093</td><td>0.879</td><td>0.577</td><td>0.128</td></tr><tr><td>% Male</td><td>-0.816</td><td>0.968</td><td>0.399</td><td>-0.05</td><td>0.601</td><td>0.934</td></tr><tr><td rowspan="8">Industry Dummies</td><td>Consumer Staples</td><td>-5.699</td><td>3.326</td><td>0.087</td><td>3.701</td><td>2.492</td><td>0.138</td></tr><tr><td>Diversified</td><td>-2.983</td><td>2.352</td><td>0.205</td><td>3.607</td><td>1.887</td><td>0.056</td></tr><tr><td>Energy</td><td>-31.704</td><td>8.834</td><td>0</td><td>-0.144</td><td>4.693</td><td>0.975</td></tr><tr><td>Financial</td><td>-15.442</td><td>4.862</td><td>0.001</td><td>0.932</td><td>2.194</td><td>0.671</td></tr><tr><td>Health Care</td><td>-19.204</td><td>5.854</td><td>0.001</td><td>-4.154</td><td>3.073</td><td>0.177</td></tr><tr><td>Industrials</td><td>-13.796</td><td>4.386</td><td>0.002</td><td>0.028</td><td>2.625</td><td>0.991</td></tr><tr><td>Technology</td><td>-8.183</td><td>3.627</td><td>0.024</td><td>-3.014</td><td>3.061</td><td>0.325</td></tr><tr><td>Telco</td><td>10.23</td><td>6.422</td><td>0.111</td><td>4.557</td><td>4.141</td><td>0.271</td></tr><tr><td rowspan="5">Firm Specific</td><td>Revenue</td><td>-2.685</td><td>1.044</td><td>0.01</td><td>0.504</td><td>0.616</td><td>0.413</td></tr><tr><td>Operating Income</td><td>-1.613</td><td>1.729</td><td>0.351</td><td>-1.615</td><td>1.198</td><td>0.178</td></tr><tr><td>R&amp;D Budget</td><td>4.23</td><td>1.916</td><td>0.027</td><td>2.572</td><td>1.218</td><td>0.035</td></tr><tr><td>S&amp;P Long-term Rating</td><td>1.192</td><td>0.949</td><td>0.209</td><td>-0.231</td><td>0.607</td><td>0.704</td></tr><tr><td>No. Subsidiaries</td><td>-3.796</td><td>1.152</td><td>0.001</td><td>-0.898</td><td>0.668</td><td>0.179</td></tr><tr><td rowspan="2">News Dummies</td><td>Business</td><td>-2.6</td><td>3.192</td><td>0.415</td><td>-4.193</td><td>2.249</td><td>0.062</td></tr><tr><td>Allows Comments</td><td>-1.673</td><td>3.73</td><td>0.654</td><td>-0.551</td><td>2.631</td><td>0.834</td></tr><tr><td rowspan="9"></td><td>Environment</td><td>19.442</td><td>6.079</td><td>0.001</td><td>-0.841</td><td>3.545</td><td>0.812</td></tr><tr><td>Film</td><td>-5.445</td><td>4.05</td><td>0.179</td><td>-1.644</td><td>2.987</td><td>0.582</td></tr><tr><td>Football</td><td>-17.691</td><td>6.509</td><td>0.007</td><td>-6.156</td><td>3.973</td><td>0.121</td></tr><tr><td>Media-Network</td><td>-13.513</td><td>4.965</td><td>0.006</td><td>-2.171</td><td>3.196</td><td>0.497</td></tr><tr><td>Music</td><td>-14.777</td><td>1356.967</td><td>0.991</td><td>-0.413</td><td>3.553</td><td>0.908</td></tr><tr><td>Sport</td><td>-9.414</td><td>5.018</td><td>0.061</td><td>-5.405</td><td>3.24</td><td>0.095</td></tr><tr><td>Sustainability</td><td>-7.139</td><td>4.876</td><td>0.143</td><td>-6.152</td><td>3.449</td><td>0.074</td></tr><tr><td>Technology</td><td>-9.564</td><td>5.3</td><td>0.071</td><td>-2.774</td><td>3.745</td><td>0.459</td></tr><tr><td>World</td><td>-7.767</td><td>3.787</td><td>0.04</td><td>-3.435</td><td>2.589</td><td>0.185</td></tr><tr><td rowspan="3">Controls</td><td>URL Blau</td><td>-3.747</td><td>1.432</td><td>0.009</td><td>-1.163</td><td>0.849</td><td>0.171</td></tr><tr><td>COL Readability</td><td>1.778</td><td>0.899</td><td>0.048</td><td>0.528</td><td>0.504</td><td>0.295</td></tr><tr><td>Authority Var.</td><td>-7.494</td><td>2.259</td><td>0.001</td><td>-1.765</td><td>1.026</td><td>0.085</td></tr><tr><td rowspan="4">Model Summary</td><td>No. Obs.</td><td></td><td></td><td>120</td><td></td><td></td><td>120</td></tr><tr><td>AIC</td><td></td><td></td><td>168.45</td><td></td><td></td><td>196.82</td></tr><tr><td>Family</td><td></td><td></td><td>Binomial</td><td></td><td></td><td>Binomial</td></tr><tr><td>Link</td><td></td><td></td><td>Logit</td><td></td><td></td><td>Logit</td></tr></table>
