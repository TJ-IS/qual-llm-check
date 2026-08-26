---
otero_id: 11476
otero_key: "39V2JH9F"
title: "Applying behavioral economics in predictive analytics for B2B churn: Findings from service quality data"
authors: "Arash Barfar; Balaji Padmanabhan; Alan Hevner"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.06.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Applying behavioral economics in predictive analytics for B2B churn: Findings from service quality data

Arash Barfar, Balaji Padmanabhan, Alan Hevner

ELSEVIER Decision Support Systems

![](/api/attachments/39V2JH9F/fulltext/images/f2629b6e8dd7a3a1ea914ef5324b86a3d9bbff1f61b4845ac18829b50b7bb268.jpg)

PII: S0167-9236(17)30118-5

DOI: doi: 10.1016/j.dss.2017.06.006

Reference: DECSUP 12857

To appear in: Decision Support Systems

Received date: 15 November 2016

Revised date: 17 June 2017

Accepted date: 26 June 2017

Please cite this article as: Arash Barfar, Balaji Padmanabhan, Alan Hevner , Applying behavioral economics in predictive analytics for B2B churn: Findings from service quality data, Decision Support Systems (2017), doi: 10.1016/j.dss.2017.06.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

Arash Barfar Information Systems Department College of Business University of Nevada at Reno

Balaji Padmanabhan & Alan Hevner Information Systems & Decision Sciences Department Muma College of Business, University of South Florida 4202 E. Fowler Avenue, Tampa, FL 33620

Abstract: Motivated by the long-standing debate on rationality in behavioral economics and the potential of theory-driven predictive analytics, this paper examines the link between service quality and B2B churn. Using longitudinal B2B transactional data with service quality indicators provided by a large company, we present evidence that both rationality and bounded-rationality assumptions play significant roles in predicting organizational decisions on churn. Specifically, variables that relate to the assumed rationality of organizations appear to provide accurate predictions while, at the same time, variables that capture boundedly rational decision rules appear to play a role through “somatic states” that make organizations more sensitive to the rational variables. In addition to presenting a novel approach for predicting organizational decisions on churn, this paper offers theoretical and managerial insights as well as opportunities for future research at the intersection of behavioral economics and predictive analytics for decisionmaking.

Keywords: organizational decision analytics, B2B service operations, churn, service quality, decision-making, rationality, bounded rationality, heuristics, adaptive toolbox, somatic states

# APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

Abstract: Motivated by the long-standing debate on rationality in behavioral economics and the potential of theory-driven predictive analytics, this paper examines the link between service quality and B2B churn. Using longitudinal B2B transactional data with service quality indicators provided by a large company, we present evidence that both rationality and bounded-rationality assumptions play significant roles in predicting organizational decisions on churn. Specifically, variables that relate to the assumed rationality of organizations appear to provide accurate predictions while, at the same time, variables that capture boundedly rational decision rules appear to play a role through “somatic states” that make organizations more sensitive to the rational variables. In addition to presenting a novel approach for predicting organizational decisions on churn, this paper offers theoretical and managerial insights as well as opportunities for future research at the intersection of behavioral economics and predictive analytics for decisionmaking.

Keywords: organizational decision analytics, B2B service operations, churn, service quality, decision-making, rationality, bounded rationality, heuristics, adaptive toolbox, somatic states

## APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

## 1. INTRODUCTION

Service organizations are highly invested in maintaining strong relationships with their customer base, both individual customers (B2C) and business entities (B2B). Loyalty in B2B service operations is particularly important since B2B interactions are perhaps fewer but provide greater numbers of transactions and more revenue per transaction (Rauyruen & Miller 2007). To understand the role that service quality plays in B2B loyalty, we analyze a rich longitudinal service quality database from a large company. The database covers two years of weekly service transactions for nearly 100,000 Small and Medium Enterprises (SMEs) as service customers. These SMEs may be viewed as active processors of service quality, which constantly analyze their service records and decide whether to stop or continue their business with the service company (Koufteros et al. 2014). Using this fine-grained and longitudinal B service quality data to examine the role that service quality plays in B2B churn provides the applied context of this research.

The methodological context of this research is informed by two stimulating research streams. The field of behavioral economics has the potential to fuel new streams of interdisciplinary Information Systems (IS) research (Goes 2013). At the same time, the recent explosion of interest in predictive analytics has highlighted the potential of leveraging massive fine-grained behavioral data that are becoming available (Martens et al. 2016). This paper is one of the first that brings these two areas together in the context of an important decision support context (i.e. managing customer churn).

Our approach involves designing rational and boundedly rational measures of service pain assessment, which relate to the neoclassical and behavioral perspectives on the rationality assumption in organizational decision making. Do levels of service pain affect the SME’s decision on churn? Can different perspectives on the rationality assumption help us design different service pain evaluation variables that capture such effects and, subsequently, predict organizational decisions on churn? This paper takes up these broad questions and examines both explanation and prediction (Shmueli 2010). That is, we investigate (i) if the service pain evaluation variables are associated with SMEs’ decisions to churn and (ii) whether such variables help generate accurate predictions.

Using a finely-granular service database to construct theoretical features also presents important technical challenges in the design of an ETL (Extract-Transform-Load) system. ETL processing can absorb up to 70 percent of data warehousing resources (Kimball & Caserta 2004). Hence, ETL design is vitally important in feature engineering with large databases. Our ETL focus allows the effective transformation of thousands of an SME’s service records in multiple tables into one predictive record. While this paper does not discuss the technical details of the ETL system employed in this research, we believe such feature engineering and ETL design deserve greater consideration as a separate step in theory-driven predictive modeling (Shmueli & Koppius 2011).

This paper offers the following contributions. First, we demonstrate how behavioral economics ideas can be integrated into predictive analytics to develop a decision support system for B2B churn prediction. Second, we examine the effect of service quality on B2B churn in a non-contractual setting. The study’s third contribution concerns the long-standing debate on rationality in economics. Our results corroborate Friedman’s (1953) perspective on the role of simplifying assumptions (e.g. omniscient rationality) in predicting firm’s behavior. Specifically, the rational measures of service quality assessment help yield accurate predictions about organizational decisions on churn. On the other hand, there are boundedly rational decision rules that appear to exacerbate the impact of the rational service quality measures on SMEs’ decisions to churn; a finding that is in line with the somatic marker hypothesis in neuroeconomics.

## 2. BACKGROUND

## 2.1. Behavioral Economics and Organizational Decision Making

Current thinking on the drivers of organizational decisions reflects two economic viewpoints. In the more traditional view, neoclassical economics assumes that organizations are rational, omniscient, and with no limitations on computational capacities and time (Rieskamp et al. 2006). In contrast, behavioral economics views organizational decision making through the lens of bounded rationality. That is, satisficing administrators might employ heuristics in information processing, which could further make their decisions susceptible to different biases and short on substantive rationality (Simon 1997). In fact, previous decision support systems research (George et al. 2000) has shown that such biases are indeed strong.

Despite their fundamentally different perspectives on rationality, both schools agree that the ultimate test of a theory is its prediction accuracy against observed behavior (Friedman 1953; Simon 1987). Neoclassical economists insist on the need for simplifying assumptions (e.g. rationality) in achieving accurate predictions (Friedman 1953), whereas behavioral economists ponder if more realistic assumptions (e.g. bounded rationality) can also contribute to predictive power (Simon 1987; Camerer & Loewenstein 2004). Regarding organizational decision making, behavioral economists ask if “there are important, empirically verified, aggregate predictions that follow from the theory of perfect rationality but that do not follow from behavioral theories of rationality” Simon (1979, p. 496). Yet, predictive accuracy of utility and heuristic models is rarely investigated in behavioral operations (Katsikopoulos & Gigerenzer 2013).

Our analyses are based on the premise that administrative decision-making involves a combination of both intuitive and analytical skills (Simon 1997), hence our decision models ideally include both rational and boundedly rational predictors. This is also in accordance with Kuhn’s (1961) perspective on scientific practice; i.e. we involve the two competing theories in building predictive models to see if the theoretical service pain evaluation variables help predict B2B churn.

We close this brief review on the behavioral-neoclassical tension with a note on the rationality assumption. Neoclassical economics does not insist that an individual firm behaves rationally (Friedman 1978). Rather, it views the (not so realistic) rationality assumption as a means of achieving accurate predictions about a group of firms in uncontrolled settings (Friedman 1953). This perspective has recently received attention in business research; i.e. research should be judged based on objective criteria such as predictive accuracy rather than relatively subjective criteria such as realism of assumptions (Shugan 2009).

## 2.2. Predictive Analytics and Churn

Churn is a major problem in predictive analytics and has attracted considerable attention in several fields, including telecommunications (e.g. Tsai & Lu 2009; Verbeke et al. 2012), energy (Moeyersoms & Martens 2015), financial services (e.g. Van den Poel & Lariviere 2004; Glady et al. 2009; Nie et al. 2011), electronic commerce (e.g. Yu et al. 2011), retail markets (e.g. Buckinx & Van den Poel 2005), subscription services (Burez & Van den Poel 2007), donations (Fader et al. 2010), and human resources (i.e. employees) (Saradhi & Palshikar 2011). Almana et al. (2014) and Vafeiadis et al. (2015) provide recent surveys and comparisons of machine learning techniques used in churn prediction.

This paper contributes to the churn literature from three perspectives. First, the majority of churn studies are conducted in contractual settings; i.e. the timing of defection is clear. Yet, a significant segment of the service industry operates in non-contractual settings, where customers can silently respond to competitors’ loud overtures. Previous churn studies in non-contractual settings mostly predict customer behavior in a predetermined prediction period (e.g. Fader et al. 2010; Rust et al. 2011; Jahromi et al. 2014). Nonetheless, the timing of defection is of the utmost importance, particularly if the service company plans to exercise a retention program following specific series of service failures that precede churn.

Second, the majority of churn studies incorporate RFM (Recency, Frequency, and Monetary Value) based factors, demographics, and surveys as the main predictors (Buckinx & Van den Poel 2005, for limitations of RFM based churn models see Lee et al. 2011). The few studies that use service quality attributes as predictors (e.g. Padmanabhan et al. 2011) have taken a purely inductive approach. In contrast, this paper employs theoretical service quality variables as the main predictors for churn.

Third, the majority of churn studies concern B2C settings. The few studies that focus on B2B churn are not similar to the present study from the above two perspectives. Bolton et al. (2006) study B2B churn in a contractual setting with the data of 143 firms, where “average engineer work-minutes per contract” is the quality metric. In this paper, however, we investigate two years of several weekly service quality indices for nearly 100,000 SMEs. Jahromi et al. (2014) and Chen et al. (2014) study B2B churn in non-contractual settings. In contrast to these studies, in this paper we apply theory-driven predictive analytics and demonstrate that the service quality variables are relevant and can predict SMEs’ decisions on churn.

## 3. THE SERVICE DATABASE: SERVICE PAIN AND EPISODES

The B2B service database in this study is comprised of nine large data tables. The service transactions table includes the number of service units that each SME has received in each week within a two-year period;

i.e. <SME\_ID, Date, Units>. In the two-year service period, several hundred million units of service were delivered to the customers. With nearly 100,000 SMEs, each with 105 weeks of provided service, the service transactions table has nearly ten million records.

The service company has defined a set of eight Service Quality Indexes (SQIs). Each SQI corresponds to a specific type of service failure (e.g. a one-day delay in fulfilment) that an SME might experience with one unit of service. Table 1 shows the total relative frequency of service failures related to each SQI. Note that except for $S Q I _ { 1 }$ , less than 1% of the service units delivered in the two-year window were subject to different types of service failures. Nevertheless, we investigate if such infrequent service failures can explain/predict churn.

## Table 1: SQIs Service Failure Percentage

<table><tr><td>SQI</td><td> $SQI_1$ </td><td> $SQI_2$ </td><td> $SQI_3$ </td><td> $SQI_4$ </td><td> $SQI_5$ </td><td> $SQI_6$ </td><td> $SQI_7$ </td><td> $SQI_8$ </td></tr><tr><td>Incident per Service Unit</td><td>1.21%</td><td>0.33%</td><td>0.08%</td><td>0.02%</td><td>0.03%</td><td>0.01%</td><td>0.00%</td><td>0.06%</td></tr></table>

For every SME in every week we observe how many units of provided service were subject to a specific type of failure. In addition to the eight SQIs, a domain expert in the company provided a holistic SQI which is a weighted linear combination of the individual SQIs which we also use in the study.

The SQIs conceptually correspond to the absence of different service “hygiene” attributes (Naumann & Jackson 1999), which are expected as inherent parts of service (e.g. being on-time). Thus, the SQIs pertain to different measures of momentary pain stimulus (denoted by $p _ { t } )$ in behavioral economics (e.g. Ariely 1998). Besides $p _ { t } ,$ since an SME receives instant utility from the fulfilled service units, we normalize the weekly $p _ { t }$ related to each SQI with the number of provided service units in that week; i.e. proportional momentary pain, denoted by $\bar { p _ { t } }$ . Specifically, $\bar { p _ { t } }$ is the number of service units suffered from a specific SQI failure, divided by the total number of provided service units in a week.

As SMEs make transactions with the company their service pain/utility profiles become continually updated, hypothetically by $p _ { t }$ or $\bar { p _ { t } }$ corresponding to different SQIs. We hypothesize that SMEs are actively evaluating their service pain/utility profiles, and based on those evaluations they decide to churn or stay loyal to the service company (Bentham 1789; Jevons 1888). To predict their decisions on churn, should we assume that SMEs practice a rational model of service evaluation, where they make decisions based on the actual experienced service pain/utility (e.g. temporal average), or should we realistically assume that they abide by boundedly rational administrators who rely on judgment heuristics?

To answer this question, we first need to define a ‘service episode’; i.e. a bounded time interval defined by its instant service utilities and pains (Kahneman 2000). Unless the SME’s loyalty age is less than two years (i.e. the database time span), we assume that its service episode starts with the beginning of our service database. In the case of churners, the end of the SME’s service episode naturally coincides with the timing of its defection. Due to the non-contractual setting of this study, ‘defection’ corresponds to significant inactivity that lasts until the end of the database two-year window. Considering the large number of SMEs (i.e. nearly 100,000) and since non-contractual data are not labeled, we employed the following timeintensive two-step process to identify churners and their churn dates. This process took over two months to complete, but resulted in customer churn identifications accepted by the company as accurate.

1. We first form a pool of potential churners including thousands of SMEs whose service unit time-series satisfy the following two conditions: (i) There is a point in time where the moving average of the number of service units drops by at least 80%, and (ii) The slope of the first order regression line on the service unit time-series is less than -0.05. The two cutoffs (i.e. 80% and -0.05) were selected after a sensitivity analysis; the combination carries a low rate of false negatives after validating random samples of candidates with an expert analyst in the service company.

2. For the several thousands of potential churners in the pool we individually plot their service unit timeseries; i.e. number of weekly service units against time (e.g. Figure 1). We then manually examine the time-series plots to select the churners and register their churn dates. Further, every one of the plots identified as churn, and a sample that were not, were verified by the service company expert.

In the above process, a few thousand SMEs were selected as churners and the timings of their defections were registered. Of the churners, we focus on those with at least six months of service transactions to ensure enough data for the analyses. Each identified churner has its specific service episode with respect to the episode’s timings and content. The episode’s content in this study concerns (i) weekly service units as instant service utilities and (2) eight different types of weekly service pains. This paper is one the first churn studies in non-contractual settings where each churner has a specific churn date, compared to a predefined prediction period (Fader et al. 2010; Rust et al. 2011; Jahromi et al. 2014). This is important when service companies plan to exercise a retention program following specific series of failures that precede churn.

![](/api/attachments/39V2JH9F/fulltext/images/e39ae3cea91c4118dd256454f4b28bf0b9c0b1e48d8df365049284807c4eb357.jpg)  
Figure 1: An identified churner

## 4. BOUNDEDLY RATIONAL CHURN DECISION RULES

In accordance with the Principle of Utility (Bentham 1789), we suspect that the level of service pain an SME experiences can be used to predict its future decision on churn. In this section we draw on behavioral economics to suggest decision rules that an SME might apply to decide whether to churn. We then consider these as features which can be examined using descriptive and predictive analytics for churn.

Rational models of information processing suggest that a service episode is evaluated based on its actual experienced service pain and utility, which is the temporal average of the episode’s instant pains. Behavioral economics, however, posits that individuals are guided by their memories of pain, and not the actual experienced pain (Kahneman et al. 1997). Such remembered pain is liable to biases, and hence is a fallible estimate of the actual experienced pain; i.e. a memory-experience gap (Miron-Shatz et al. 2009).

The snapshot model in behavioral economics (Fredrickson & Kahneman 1993) explains the retrospective evaluation of temporally extended experiences (e.g. service episodes). Individuals assess their experience episodes by constructing a snapshot of the episode’s representative moments and evaluating that snapshot’s utility (Kahneman et al. 2003). In a similar vein, we posit that SMEs continuously update their service snapshots based on their streaming experience with the company (Fredrickson & Kahneman 1993).

# ACCEPTED MANUSCRIPT

We propose boundedly rational churn decision rules based on the representativeness and availability heuristics which are the focus of the of the heuristics and biases research program (Tversky & Kahneman 1974; Kahneman & Frederick 2002). Every churn decision rule can be exercised with each of the eight SQIs. For exposition, we illustrate a real example from the service database that is consistent with each decision rule. That is, the data behave as if an SME employed the decision rule and churned. While not suggesting causality, we seek such examples in the database for two reasons. First, such ples help the reader see the potential impacts of such decision rules on B2B churn. Second, any decis n rule should have concrete examples in the database to be considered in the study. Not seeing any example may suggest that the decision rule is never employed and should not be part of the study.

## 4.1. Representativeness Decision Rules for Churn

A prominent heuristic for judging pain episodes is the peak-end rule (Fredrickson & Kahneman 1993); i.e. the past episode is evaluated based on its maximum instant pain along with the instant pain close to the end— as the two representatives for all the episode’s instant pains. For example, among a group of patients that have undergone a painful operation, those with less total pain and more end pain evaluated the whole procedure more painful than those with more total pain and less end pain (Redelmeier & Kahneman 1996).

The original peak-end rule is merely an average of the peak pain and the end pain, hence the timing of the peak pain is not considered in the subsequent evaluation. This may not be important in less-than-onehour episodes (e.g. Redelmeier & Kahneman 1996); however, we suspect the timing of the peak pain might play a significant role in evaluating long service episodes. In a similar vein, some studies highlight the role of instant pains trends (Ariely & Carmon 2003), where a sequence of increasing pains is retrospectively judged worse than a sequence of decreasing ones, although both sequences carry the same total pain. That is, pushing the peak pain to the end can change the slope significantly, whereas the peak-end average stays as before. Accordingly, we propose separate decision rules based on the peak pain and the end pain.

The first and simplest decision rule (DR1) is solely based on the existence of service pain. That is, the SME will churn if the recent pain is greater than zero, regardless of its magnitude. Figure 2 depicts a churn in the database that can be attributed to the application of this rule; i.e. the SME decides to churn following the first incident of a specific SQI failure. The time-series show that on 5/31/2010, one of the eight units of provided service was subject to a specific type of failure, and the company subsequently churned.

![](/api/attachments/39V2JH9F/fulltext/images/3338eb93b18c1392be5086b65425231013b398cadabb860ff37d410ea9f87842.jpg)

![](/api/attachments/39V2JH9F/fulltext/images/8baa9932b022588988563a4d595feb98233c1ac262c81ef36bdc8adfd1494586.jpg)  
Figure 2: Application of DR1; (a) a specific SQI (b) service units

To act upon a churn decision rule, an SME needs some time to complete a switch to another service addition to the six-week action window, we examine the application of these decision rules with four-week and eight-week action windows. With a six-week action window DR1 can be formulated as:

$$
\exists t \in [ T - 5, T ] \colon p _ {t} \succ 0;
$$

DR1 also has a more rational manifestation, where the SME’s tolerance for service failure grows with the number of service units (i.e. extensional target evaluation). Behavioral economics posits that the logical rule of judgment is extensional (Kahneman & Frederick 2002); however, no such strict statement can be made in B2B services. It is not clear whether an SME’s potential insensitivity to service volume is an unconscious effect or a deliberate strategy. One reason is that SMEs, compared to individuals, are more likely to have logged information about the service volume, hence the extensional target attribute is not low in accessibility. Moreover, here both sensitivity and insensitivity to service scope are backed by apt explanations: An SME may not take its broad service scope into account, expecting no service pain at all since it is paying for each unit of service. Some may even push this further, expecting that broader service scopes deserve special care from the service company and subsequently less service pain. We refer to this hypothetical phenomenon as righteous neglect of scope since it can be endorsed by analytic reasoning. At the other extreme, an SME may appreciate the probability and admits that as the service scope expands the probability of service failures grows—leading to the sensitivity to service scope. For the same reasons, in addition to the $\mathrm { S Q } [ \mathrm { s } ^ { \prime }$ instant proportional pain $\left( \hat p _ { t } \right)$ we will test all of the suggested decision rules with instant pain $( p _ { t } ) ;$ i.e. without considering the instant service utility that the SME receives.

The decision rule for the extensional target evaluation of the end service pain (DR2) is proposed in a way that satisfies monotonicity (Ariely & Lewenstein 2000). Monotonicity holds if each service unit adds to the failure tolerance threshold an amount that depends on the previous service utility and failure that the SME has already experienced. Thus, DR2 states that the SME will churn if the updated average of service pains (after the recent failure) is greater than the average prior to the recent service failure. This condition holds iff the average of the recent instant pains is greater than the average prior to the recent failures.

To illustrate, suppose that throughout the past course of service transactions where 1000 units of service were provided, the SME has experienced ten units of failure. In the present month, the number of service units is 101 and the SME has experienced one unit of service failure. In the case of extensional service pain evaluation, one unit of pain is commensurate with 101 service units, compared to the past proportional pain (i.e. 10/1000). The SME may even appreciate this as a sign of improvement in service quality.

DR2: churn in week ?? if $\frac { \sum _ { t = T - 5 } ^ { T } p _ { t } } { \sum _ { t = T - 5 } ^ { T } u _ { t } } > \frac { \sum _ { t = 1 } ^ { T - 6 } p _ { t } } { \sum _ { t = 1 } ^ { T - 6 } u _ { t } }$ ; where $u _ { t }$ is the service volume in week ??.

![](/api/attachments/39V2JH9F/fulltext/images/f1c7487e53ee71e54c3398d510713015dc862b6635f0890086d015826565933e.jpg)

![](/api/attachments/39V2JH9F/fulltext/images/80eeaa3f46a587b172e11327e6a7bc395798747f42ac133e1bad9dc4c076fd8f.jpg)  
Figure 3: Application of DR2; (a) a specific SQI (b) service units

In Figure 3, for example, the service pain in the red area could push an SME with a sense of probability to churn, although it is not worse than the pain the SME experienced before. The reason is that the average pain in the red area is worse than the previous average pain (gray area); i.e. a regression in service quality.

# ACCEPTED MANUSCRIPT

The last decision rule in this section concerns the peak aspect of the peak-end rule, where an SME might take the maximum instant (proportional) service pain as a representative for the whole service episode. DR3 addresses an SME that will churn if the recent pain is greater than any pain it has experienced before. Figure 4 depicts a churn in the database that can be attributed to the application of DR3 with $p _ { t }$ .

$$
{ } _ { t = T - 5 } ^ { T } M a x ( p _ { t } ) \succ { } _ { t = 1 } ^ { T - 6 } M a x ( p _ { t } )
$$

![](/api/attachments/39V2JH9F/fulltext/images/d39a1b2ff37c3b649f80a0a81cf79015dd336eaf10df851a068231f54b0a732b.jpg)

![](/api/attachments/39V2JH9F/fulltext/images/fa20feb1280302301fbbcbb4f743a957b845ca0f78039abd1e6eb5407e0acbe9.jpg)  
Figure 4: Application of DR3; (a) a specific SQI (b) service units

## 4.2. Availability Decision Rules for Churn

In accordance with attribution theory, we suggest that the SME’s judgment about the frequency of service failures plays an important role in its decision on churn. Frequent service failures eventually turn into a stable attribution of the service company, which pertains to the application of a judgment heuristic known as the availability heuristic. An incident is estimated as frequent if it is available; i.e. it can be easily brought to mind (Tversky & Kahneman 1973). In this vein, clinical research has shown that the recalled pain frequency is often overestimated if the pain is recent (Van Den Brink et al. 2001; Shiffman et al. 2008).

In service operations, the broad decision rule that stems from the availability heuristic is equivalent to DR1. If the most recent service pain is greater than zero, the service failure that caused pain will be also conceived as frequent; an impression that can lead the SME to churn in accordance with attribution theory. As noted earlier, DR1 covers both prototypical and extensional target evaluation. Here we present a version of this decision rule for the extensional target evaluation of failures frequency with two different measures.

# ACCEPTED MANUSCRIPT

The first measure (??) for service failures frequency is temporal; i.e. the number of weeks that include at least one incident of related service failure divided by the number of weeks that include at least one service unit $( f = \frac { | \{ t | \forall t p _ { t } > 0 \} | } { | \{ t | \forall t u _ { t } > 0 \} | } )$ . Following the same logic presented for DR2, the decision rule for extensional target evaluation of temporal frequency states that an SME will churn if the recent temporal frequency of service failures is greater than what it was before. Figure 5 depicts a churn after two consecutive failures.

$$
{ } _ { t = T - 5 } ^ { T } f \succ { } _ { t = 1 } ^ { T - 6 } f
$$

![](/api/attachments/39V2JH9F/fulltext/images/cb395a3f9ffa2849fe664d8a357b7e924f9e403f38c6aad69bb4505eae187621.jpg)

![](/api/attachments/39V2JH9F/fulltext/images/7ae4e3db4143802c011fc9444d8e55c5015c6afdf89c88d2a5811b69c5d8ad94.jpg)  
Figure 5: Application of DR4; (a) a specific SQI (b) service units

The second measure (??) for service failures frequency is incidental, which is the number of related service failures divided by the number of weeks that include at least one service unit; $F = { \frac { \sum p _ { t } } { | \{ t | \forall t u _ { t } \succ 0 \} | } }$

$$
{ } _ { t = T - 5 } ^ { T } F \succ { } _ { t = 1 } ^ { T - 6 } F
$$

![](/api/attachments/39V2JH9F/fulltext/images/262faf2dde9ab695a3ebbaf0c9aa4969438aa3b54b8768800ddb288bf09cb02d.jpg)

![](/api/attachments/39V2JH9F/fulltext/images/f6b6df8ba679a16d50b8ca15d65310d157d7777758f537310ffdaaeb8268c02d.jpg)  
Figure 6: Application of DR5; (a) specific SQI (b) service units

Figure 6 depicts a churn incident that can be attributed to the application of the availability heuristic with the incidental measure.

Table 2 summarizes the five decision rules, and their possible applications with different SQIs.

Table 2: Summary of Decision Rules and their Applications

<table><tr><td>Rule</td><td>Description</td><td>Can be applied with...*</td></tr><tr><td>DR1</td><td>Churn if the recent pain is greater than zero, regardless of its magnitude.</td><td>Eight SQIs&#x27;  $p_t$  and the holistic SQIs&#x27;  $p_t$ </td></tr><tr><td>DR2</td><td>Churn if the updated average of service pains (updated after the most recent failure) is greater than the average prior to the recent service failure.</td><td>Eight SQIs&#x27;  $p_t$  and  $\bar{p}_t$ , along with the holistic SQIs&#x27;  $p_t$ ,  $\bar{p}_t$ , and  $pi_t$ </td></tr><tr><td>DR3</td><td>Churn if the recent pain is greater than any pain that has been experienced before.</td><td>Eight SQIs&#x27;  $p_t$  and  $\bar{p}_t$ , along with the holistic SQIs&#x27;  $p_t$ ,  $\bar{p}_t$ , and  $pi_t$ </td></tr><tr><td>DR4</td><td>Churn if the recent temporal frequency of service failures is greater than what it was before.</td><td>Eight SQIs&#x27;  $p_t$  and the holistic SQIs&#x27;  $p_t$ </td></tr><tr><td>DR5</td><td>Churn if the recent incidental frequency of service failures is greater than what it was before.</td><td>Eight SQIs&#x27;  $p_t$  and the holistic SQIs&#x27;  $p_t$ </td></tr></table>

$ ^ * p _ { t } \colon$ Instant pain  
$\bar { p _ { t } } \mathrm { : }$ Instant proportional pain $( \frac { p _ { t } } { u } )$  
$p i _ { t } \colon$ overall number of service failures in a specific week regardless of the SQI types.

## 4.3. Somatic Markers and Boundedly Rational Decision Rules

Organizational decision making involves a combination of both intuitive and analytical skills, where administrative emotions steer analytical actions to particular goals in the organization (Simon 1997). This is in line with the dual-system of cognitive processes in psychology (Kahneman & Frederick 2002). That is, System 2 (reasoning) concurrently monitors the quality of the quick proposals made by System 1 (intuition) and subsequently endorses, corrects, or overrides them. Accordingly, the suggested boundedly rational churn decision rules may also draw the SME’s attention to the rational measures of service quality.

The somatic marker hypothesis in neuroeconomics (Damasio 2005; Bechara & Damasio 2005) can partly explain the hypothesized synergy between rational and boundedly rational assessments of service quality. A heuristic (e.g. peak service pain) can cause a somatic state that “functions as an alarm bell” and “operates not only as a marker for the value of what it represented, but also as a booster for continued working memory and attention” (Damasio 2005, p. 174). Likewise, the decision rule’s biasing nature might cause a somatic state that draws the SME’s attention to service quality, and subsequently calls for judgment, which might be carried out using the rational measures of quality assessment.

## 5. ANALYSES AND RESULTS

We examine the large service database to see if rational and boundedly rational decision rules help the service company explain and predict an SME’s churn. We use one-third of the churners to build the descriptive dataset and the remaining two-thirds for the explanatory/predictive analyses.

# ACCEPTED MANUSCRIPT

Each identified churner has a specific service episode; i.e. a churner’s service episode ends with a specific churn date. For the non-churners however, we select the service episodes in both descriptive and predictive datasets based on the service episodes of the dataset’s churners. For every churner in the descriptive dataset (base rate: 1/9), for example, we randomly select nine non-churners (that have not been selected by the ETL yet) whose initial service episodes are longer than the churner’s. For these nine nonchurners, the ETL selects the service episodes’ ending and beginning in a way that (i) The ending coincides with the corresponding churner’s and (ii) The length is equal to the corresponding churner’s, based on which the ETL adjusts the beginning. Such matched sampling is used to control in part for common events in the environment that might impact all SMEs.

## 5.1. Descriptive Analysis

The aims of the study’s descriptive analysis are twofold. First, it intrinsically covers the two essential steps in building predictive models (Shmueli & Koppius 2011); i.e. exploratory analysis and choice of variables. We have defined five churn decision rules in Section 4 each of which can be calculated with $p _ { t }$ or $\bar { p _ { t } }$ of eight SQIs. The descriptive analysis helps decide which application measures, of which decision rules, with regard to which SQIs can be potential predictors for organizational churn.

Second, the study’s descriptive analysis aims to address the view in behavioral economics that rejects positivism and the elements of statistical significance such as $p \mathrm { . }$ value and lack of fit (Hosseini 2003; Ziliak & McCloskey 2008). Thus, in the descriptive analysis we refrain from rushing into the tests of statistical significance; we first investigate any descriptive evidence of the application of churn decision rules.

The descriptive ETL is designed to extract the three measures from the descriptive dataset. These measures in part address the application of the suggested decision rules in churn:

Measure 1- Percentage of churners that immediately follow the firing of a decision rule compared to nonchurners (for whom the condition of the relevant decision rule holds in the last six weeks of their matched service episodes),

Measure 2- Percentage of churners for whom the decision rule fired at least once compared to non-churners (for whom the condition of the relevant decision rule holds at least once in their matched episodes),

# ACCEPTED MANUSCRIPT

Measure 3- Alarm frequency of a decision rule for churners compared to non-churners. Alarm frequency is the number of times that the necessary condition of a decision rule holds in a service episode. Specifically, it concerns the number of times that a specific decision rule has fired, or set off a service quality alarm in a service episode, on which an SME could have acted and churned.

These measures help examine the importance of the representativeness and availability decision rules in B2B churn as defined in Section 4, through benchmarking the evidence of their application by churners against non-churners. Measure 1 is computed based on the last six weeks of the service episodes; hence the churn dates play a significant role in the first measure. To address the concern about any inherent inaccuracy of the churn dates, the ETL computes Measures 2 and 3 that capture the relative importance of the decision rules with respect to the entire service episode, and not just its end.

We end the descriptive analysis with a comparison between the actual service pain that the churners and non-churners experienced in their service episodes; i.e. a rational measure of service pain assessment.

## 5.1.1. Boundedly Rational Churn Decision Rules

To investigate any evidence of the application of the churn decision rules, the ETL analyzes the information extracted based on the temporal locus of a six-week sliding window. For each SME, starting from the $2 5 ^ { \mathrm { t h } }$ week of its specific service episode, the ETL first extracts the necessary information for all decision rules with respect to all SQIs, and then examines if the conditions for a specific decision rule hold. Having registered the analysis results for the current temporal locus of the sliding window, the ETL moves the sliding window ahead for one week, updates the relevant information, and repeats the process until it reaches the end of the SME’s specific episode. The first 24 weeks of each service episode are left as the initial benchmark for the extensional decision rules (e.g. DS2). In addition to the six-week sliding window, the ETL in this section has been executed with four-week and eight-week sliding windows. The results are not significantly different than the ones reported with the six-week sliding window.

For each SQI, in addition to its relevant instant pains $( p _ { t } )$ , we conduct the same analysis with instant proportional pains $( \hat { p } _ { t } )$ to examine their application with extensional target evaluation. Furthermore, the same analysis is conducted for $p i _ { t }$ , which is inherent to the holistic SQI, and addresses the overall number of service failures in a specific week regardless of the SQI types. To illustrate, suppose that in a specific week, there is one service failure of $S Q I _ { 1 }$ , one failure of $S Q I _ { 2 }$ , and no failures of the rest of SQIs. Here, $p i _ { t }$ is equal to 2, whereas $p _ { t }$ corresponding to the holistic SQI is sum of the weights of $S Q I _ { 1 }$ and $S Q I _ { 2 }$ that has been suggested by a domain expert.

The pseudo-code in Figure 7 illustrates the significant ETL programming involved in this process. Note that there are four loops in the pseudo code; 100,000 SMEs, each with nearly 100 weeks, five different decision rules, and nine different SQIs (including the holistic one).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For each SME,
    Fetch the SME's service episode; i.e.  $[w_{start}, w_{end}]$ ,
    Set  $[w_{start}, w_{start+23}]$  as the base,
    For each  $w_i$  in  $[w_{start+24}, w_{end-5}]$ ,
    For each decision rule  $DR_j$ ,
    For each  $SQI_k$ ,
    Check to see if the conditions of  $DR_j^*$  with  $SQI_k(p_t)$  holds within  $[w_i, w_{i+5}]$ ,
    Check to see if the conditions of  $DR_j$  with  $SQI_k(\bar{p}_t)$  holds within  $[w_i, w_{i+5}]$ ,
    EndFor,
    EndFor,
    EndFor,
EndFor,

*For conditions of different decision rules see section 4.1
</div>

Figure 7: Psuedo code for extracting pain assessment variables

Table 3 presents the data for Measure 1, showing a comparison between the percentage of churners who immediately followed the decision rule and churned, and the same percentage for non-churners. To compute this measure, the ETL extracts the percentage of non-churners for whom the condition of the relevant decision rule holds in the last six weeks of their matched service episodes. Note that DR2 and DR3 can be calculated with $p _ { t }$ and $\bar { p _ { t } }$ , hence each of their cells has two entries.

Table 3: Relative importance of decision rules for churners compared to non-churners (Measure 1)

<table><tr><td rowspan="2"></td><td colspan="2"> $SQI_1$ </td><td colspan="2"> $SQI_2$ </td><td colspan="2"> $SQI_3$ </td><td colspan="2"> $SQI_4$ </td><td colspan="2"> $SQI_5$ </td><td colspan="2"> $SQI_6$ </td><td colspan="2"> $SQI_7$ </td><td colspan="2"> $SQI_8$ </td><td colspan="3">Holistic SQI</td></tr><tr><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_\bar{t}$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $pi_t$ </td></tr><tr><td>DR1</td><td colspan="2">0.93</td><td colspan="2">0.97</td><td colspan="2">0.82</td><td colspan="2">0.83</td><td colspan="2">1.00</td><td colspan="2">1.16</td><td colspan="2">1.00</td><td colspan="2">1.08</td><td colspan="3">0.98</td></tr><tr><td>DR2</td><td>1.09</td><td>1.15</td><td>1.08</td><td>1.14</td><td>0.85</td><td>0.9</td><td>0.86</td><td>0.86</td><td>1.06</td><td>1.08</td><td>1.17</td><td>1.17</td><td>1.00</td><td>1.00</td><td>1.13</td><td>1.13</td><td>1.06</td><td>1.19</td><td>1.14</td></tr><tr><td>DR3</td><td>0.93</td><td>1.32</td><td>1.12</td><td>1.37</td><td>0.92</td><td>1.05</td><td>0.68</td><td>0.73</td><td>1.05</td><td>1.22</td><td>1.08</td><td>1.16</td><td>1.00</td><td>1.00</td><td>1.18</td><td>1.13</td><td>0.96</td><td>1.16</td><td>1.00</td></tr><tr><td>DR4</td><td colspan="2">0.84</td><td colspan="2">0.95</td><td colspan="2">0.82</td><td colspan="2">0.79</td><td colspan="2">1.02</td><td colspan="2">1.17</td><td colspan="2">1.00</td><td colspan="2">1.11</td><td colspan="3">0.91</td></tr><tr><td>DR5</td><td colspan="2">0.87</td><td colspan="2">0.96</td><td colspan="2">0.80</td><td colspan="2">0.79</td><td colspan="2">1.04</td><td colspan="2">1.17</td><td colspan="2">1.00</td><td colspan="2">1.07</td><td colspan="3">0.88</td></tr></table>

The three bold statistics in Table 3 indicate the existence of proportional peak pain in the last six weeks

prior to churn. These statistics address a relatively rational version of the peak pain decision rules since they are practiced with the $\mathrm { S Q I s } ^ { \prime } \ \bar { p _ { t } }$ , which also considers the received utility. For example, while the condition for $[ \mathrm { D R } 3 , S Q I _ { 1 } ( \bar { p } _ { t } ) ]$ holds 32% more in the last six weeks of the churners’ episodes than for the non-churners’, the same decision rule (practiced with $S Q I _ { 1 } ( p _ { t } ) )$ has an opposite trajectory (i.e. 0.93).

Nonetheless, the bold statistics in Table 3 do not necessarily imply a causal relationship between the decision rules and churn. Consider for example the bold statistic in $[ \mathrm { D R } 3 , S Q I _ { 2 } ( \bar { p } _ { t } ) ]$ . In this case, 10.4% of churners experienced the peak proportional pain in their last six weeks prior to churn, while this number is 7.6% for the non-churners (i.e. $\frac { 1 0 . 4 \% } { 7 . 6 \% } = 1 . 3 7 )$ . However, nearly half of the churners in the numerator did not follow the same decision rule more than four times within their service episodes. That is, the same decision rule had fired but they did not churn subsequently.

Table 4: Relative importance of decision rules for churners compared to non-churners (Measure 2)

<table><tr><td rowspan="2"></td><td colspan="2"> $SQI_1$ </td><td colspan="2"> $SQI_2$ </td><td colspan="2"> $SQI_3$ </td><td colspan="2"> $SQI_4$ </td><td colspan="2"> $SQI_5$ </td><td colspan="2"> $SQI_6$ </td><td colspan="2"> $SQI_7$ </td><td colspan="2"> $SQI_8$ </td><td colspan="3">Holistic SQI</td></tr><tr><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_\bar{t}$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $pi_t$ </td></tr><tr><td>DR1</td><td colspan="2">1.00</td><td colspan="2">1.02</td><td colspan="2">0.96</td><td colspan="2">0.98</td><td colspan="2">1.07</td><td colspan="2">1.20</td><td colspan="2">1.22</td><td colspan="2">1.06</td><td colspan="3">1.01</td></tr><tr><td>DR2</td><td>1.01</td><td>1.02</td><td>1.20</td><td>1.29</td><td>0.96</td><td>0.96</td><td>0.98</td><td>0.98</td><td>1.08</td><td>1.07</td><td>1.21</td><td>1.21</td><td>1.23</td><td>1.24</td><td>1.06</td><td>1.04</td><td>1.03</td><td>1.04</td><td>1.03</td></tr><tr><td>DR3</td><td>0.93</td><td>1.00</td><td>1.04</td><td>1.09</td><td>0.96</td><td>1.01</td><td>0.97</td><td>1.00</td><td>1.04</td><td>1.08</td><td>1.23</td><td>1.25</td><td>1.12</td><td>1.22</td><td>1.48</td><td>1.30</td><td>0.97</td><td>1.02</td><td>0.94</td></tr><tr><td>DR4</td><td colspan="2">0.98</td><td colspan="2">1.02</td><td colspan="2">0.96</td><td colspan="2">0.98</td><td colspan="2">1.06</td><td colspan="2">1.21</td><td colspan="2">1.23</td><td colspan="2">1.05</td><td colspan="3">0.99</td></tr><tr><td>DR5</td><td colspan="2">0.99</td><td colspan="2">1.02</td><td colspan="2">0.96</td><td colspan="2">0.99</td><td colspan="2">1.07</td><td colspan="2">1.21</td><td colspan="2">1.23</td><td colspan="2">1.06</td><td colspan="3">1.00</td></tr></table>

Table 4 indicates a comparison between the percentage of churners for whom the condition of the decision rule holds at least once in their entire service episodes, and the same percentage for non-churners (i.e. Measure 2). Measure 2 does not depend on the churn dates; it counts the cases where an SME followed a decision rule with some delay. Table 4 shows that the percentage of churners and non-churners that could follow a decision rule is not practically different. Only for $\left[ \mathrm { D R 3 } , S Q I _ { 8 } \left( p _ { t } \right) \right]$ does the difference of 48% stand out.

Table 5: Relative importance of decision rules for churners compared to non-churners (Measure 3)

<table><tr><td rowspan="2"></td><td colspan="2"> $SQI_1$ </td><td colspan="2"> $SQI_2$ </td><td colspan="2"> $SQI_3$ </td><td colspan="2"> $SQI_4$ </td><td colspan="2"> $SQI_5$ </td><td colspan="2"> $SQI_6$ </td><td colspan="2"> $SQI_7$ </td><td colspan="2"> $SQI_8$ </td><td colspan="3">Holistic SQI</td></tr><tr><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_\bar{t}$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $p_t$ </td><td> $\overline{p}_t$ </td><td> $pi_t$ </td></tr><tr><td>DR1</td><td colspan="2">0.97</td><td colspan="2">1.02</td><td colspan="2">0.96</td><td colspan="2">1.03</td><td colspan="2">1.10</td><td colspan="2">1.20</td><td colspan="2">1.30</td><td colspan="2">1.05</td><td colspan="3">0.99</td></tr><tr><td>DR2</td><td>1.00</td><td>1.04</td><td>1.00</td><td>1.00</td><td>0.95</td><td>0.95</td><td>0.99</td><td>1.00</td><td>1.10</td><td>1.10</td><td>1.20</td><td>1.20</td><td>1.30</td><td>1.30</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>DR3</td><td>0.94</td><td>1.06</td><td>1.10</td><td>1.10</td><td>0.95</td><td>0.99</td><td>0.92</td><td>0.93</td><td>1.00</td><td>1.10</td><td>1.10</td><td>1.10</td><td>1.00</td><td>1.20</td><td>1.00</td><td>0.97</td><td>0.95</td><td>1.00</td><td>0.95</td></tr><tr><td>DR4</td><td colspan="2">0.94</td><td colspan="2">1.00</td><td colspan="2">0.92</td><td colspan="2">0.99</td><td colspan="2">1.10</td><td colspan="2">1.19</td><td colspan="2">1.31</td><td colspan="2">1.03</td><td colspan="3">0.96</td></tr><tr><td>DR5</td><td colspan="2">0.94</td><td colspan="2">1.00</td><td colspan="2">0.94</td><td colspan="2">1.00</td><td colspan="2">1.11</td><td colspan="2">1.19</td><td colspan="2">1.31</td><td colspan="2">1.03</td><td colspan="3">0.96</td></tr></table>

Measure 3 indicates if a specific alarm was set off more for churners than for non-churners. Specifically, it provides a comparison between the average number of times that a decision rule’s condition holds in the entire service episode of a typical churner and that average for a typical non-churner.

## 5.1.2. Rational Assessment of Service Pain

Given that the service episodes in the analysis are of different lengths, we pick the temporal average of proportional service pain (??) as a normative measure of the actual experienced service pain/utility; i.e. for each SME with a T-week service episode, $\begin{array} { r } { \sigma = \frac { \sum _ { 1 } ^ { T } \bar { p _ { t } } } { T } } \end{array}$

Table 6 shows that for all SQIs the mean of ?? for the churners is greater than for the non-churners; suggesting that the churners in the descriptive dataset have experienced more total service pain than the non-churners. This indicates lower actual service quality for the churners throughout their service episodes. Consider the $S Q I _ { 1 }$ column: for a typical non-churner in the descriptive dataset, in every week on average, 1.49% of the service units suffered from the $S Q I _ { 1 }$ failure, whereas this ratio is 1.65% for the churners. Note that the holistic percentages are large due to the weights the service company expert assigned to each SQI. Table 6: Temporal average of proportional service pain

<table><tr><td></td><td> $SQI_1$ </td><td> $SQI_2$ </td><td> $SQI_3$ </td><td> $SQI_4$ </td><td> $SQI_5$ </td><td> $SQI_6$ </td><td> $SQI_7$ </td><td> $SQI_8$ </td><td>Holistic SQI</td></tr><tr><td>Non-churners</td><td>1.49%</td><td>0.50%</td><td>0.16%</td><td>0.83%</td><td>0.06%</td><td>0.50%</td><td>0.013%</td><td>0.71%</td><td>83.45%</td></tr><tr><td>Churners</td><td>1.65%</td><td>0.61%</td><td>0.19%</td><td>0.84%</td><td>0.07%</td><td>0.59%</td><td>0.017%</td><td>0.77%</td><td>94.48%</td></tr></table>

Table 6 pertains to the rational models of information processing in neoclassical economics; hence we can examine its statistical significance. To investigate whether the mean of ?? is significantly greater for the churners than for the non-churners, we conduct Analyses of Variance on ?? with regard to each SQI. We first conduct an omnibus MANOVA. It is determined that significant differences exist between the two groups at any level of α since (p-value≺10-4). Although the number of service units and service episodes’ lengths are both embedded in ??, we still include them as the covariances in our analyses.

Regarding the relevant assumptions, ANCOVA is robust with respect to the normality assumption for large samples. We conduct the Levene’s test to verify the homogeneity of variances of ?? for the churners and the non-churners. Except for the first two SQIs, the Levene’s null hypothesis is not rejected at α equals to 0.01—satisfying the corresponding assumption for seven SQIs. Among these SQIs, only the service failures related to $S Q I _ { 4 }$ and $S Q I _ { 7 }$ do not cause more significant pain for the churners; i.e. the actual service pain differences are highly significant for the rest of SQIs.

## 5.2. Explaining and Predicting B2B Churn with Service Quality

This section describes both explanatory and predictive modeling (for differences see Shmueli 2010). We investigate (i) if the service pain evaluation variables can explain SMEs’ decisions to churn, and (ii) if such theoretical predictors help predict churn. It is important to note that we approach the above questions (i.e. explanation and prediction) separately. We apply logistic regression models, which are widely used in classification trees as the second most common technique for churn detection (Neslin et al. 2006). To ensure robustness, we examine both explanation and prediction through ten iterations of random stratified subsampling.

## 5.2.1. Construction of Variables

The ETL system uses the remaining two-thirds of the SMEs and their specific episodes to generate the dataset for explanatory and predictive modeling (Table 7). SME\_ID is the primary key in the dataset. The target variable is a churn label, addressing the SME’s observed behavior on defection. The service pain assessment variables are computed based on each SME’s specific episode. The controls include Age (age of SME’s relationship with the service company), and a set of firmographics.

Table 7: An observation in the dataset for explanatory and predictive modeling

<table><tr><td rowspan="4">SME_ID</td><td rowspan="4">Churn (0/1)</td><td rowspan="2">Control Variables</td><td colspan="3">Service Pain Assessment Variables</td></tr><tr><td>Rational Service Assessment Variables</td><td colspan="2">Heuristic Service Assessment Variables</td></tr><tr><td>Age,  $F_1$ ,  $F_2$ ,  $F_3$ </td><td> $R_1$  ...  $R_9$ </td><td> $H_1$  ...  $H_{26}$ </td><td> $H_{27}$ ,  $H_{28}$ ,  $H_{29}$ </td></tr><tr><td>•Relationship Age, 11 years on average.•Firm demographics.</td><td>•Based on the SME’s whole episode.•  $R_i$ : Temporal average ( $\sigma$ ) of service pain/utility for  $SQI_i$ </td><td>•Based on the SME’s whole service episode.•See Appendix A.</td><td>• Based on the last six weeks of the SME’s service episode.•See Appendix A.</td></tr></table>

We draw on the descriptive analysis in Section 5.1 to select the theoretical variables. The churners in the descriptive dataset have experienced more actual service pain with regard to all SQIs (Table 6), hence the ETL computes nine R(ational) service pain assessment variables $( R _ { i : 1  9 } )$ . In Table 7, $R _ { i }$ is the temporal average of the proportional pain $( \frac { \sum _ { 1 } ^ { T } \bar { p _ { t } } } { T } )$ related to $S Q I _ { i } ,$ , which the SME has experienced in its specific episode. $R _ { 9 }$ concerns the holistic SQI. The ETL also computes 29 H(euristic) variables $( H _ { j : 1 \to 2 9 } )$ which concern the application of different decision rules with different SQIs. Appendix A explains these variables in detail.

# ACCEPTED MANUSCRIPT

## 5.2.2. Explaining Organization Churn with Service Pain Assessment Variables

We have drawn on the theories in behavioral economics to design variables that capture different forms of B2B service quality evaluation. The ultimate goal of these variables is to help generate accurate predictions about organizational churn. Nonetheless, since these variables are deeply rooted in theory, we first test the related hypotheses through explanatory modeling (Shmueli 2010). Specifically, explanatory modeling allows us to test if the related hypotheses for the effects of service pain or somatic states on churn hold.

In this section, accordingly, we investigate if the suggested service pain assessment variables can explain SMEs’ decisions to churn. To ensure consistency and robustness, we examine the effects of theoretical variables on churn through ten iterations of random stratified subsampling. In each iteration, we examine the statistical significance of the model using the randomly selected two-thirds of the dataset. To assess the predictive power of the explanatory models (Shmueli 2010), in each round we score the remaining one-third of the dataset (i.e. test stratum) with the explanatory logit models.

To account for multicollinearity, which could interfere with inference (Shmueli 2010), in every iteration we consider a ‘0.1’ cutoff as the tolerance threshold (Hair et al. 2010). All R(ational) variables $( R _ { i : 1  8 } )$ are highly tolerant in all iterations; their tolerance values are mostly in the ranges of 0.9 and 0.7. $R _ { 9 }$ is naturally intolerant since it concerns a linear combination of the eight SQIs. Among the H(euristic) variables, $H _ { 2 7 } , H _ { 2 8 }$ and $H _ { 2 9 }$ , which are computed based on the last six weeks of the SME’s episode, are highly tolerant throughout all iterations; their tolerance values are greater than 0.9. Among the first 26 H(euristic) variables, which are computed based on the SME’s whole episode, only $H _ { 1 3 }$ and $H _ { 1 4 }$ are moderately tolerant.

The rational essence of the tolerant H(euristic) variables deserves attention. $H _ { 1 3 }$ and $H _ { 1 4 }$ address the extensional target evaluation of the last service pain related to SQI2, which is a logical rule (Kahneman & Frederick 2002). Similarly, $H _ { 2 7 } , H _ { 2 8 } ,$ and $H _ { 2 9 }$ concern the existence of proportional peak pain in the last six weeks of the episode, thereby carrying a sense of utility and probability in the peak pain.

Besides the variables that pass the tolerance filter, we include three interaction terms between $H _ { 2 7 } , H _ { 2 8 } , H _ { 2 9 }$ and their corresponding R(ational) pain assessment variables. This addresses the hypothesized role of heuristics as attentional mechanisms (i.e. the somatic marker hypothesis). To illustrate, since $H _ { 2 7 }$ concerns the existence of the proportional peak $S Q I _ { 1 }$ pain in the last six weeks of the SME’s episode, we include ${ } ^ { \circ } H _ { 2 7 } \ast R _ { 1 } { } ^ { \prime }$ in the model. We hypothesize that the peak pain $( H _ { 2 7 } { = } 1 )$ could realize/exacerbate the effect of the rational assessment of the relevant pain $( R _ { 1 } )$ on the odds of churn.

Table 8 summarizes the statistically significant variables, their significance level, and their effects on SME’s age of business relationship with the service company stays highly significant, with a negative effect on the odds of churn. Holding other variables fixed, the odds of churn decreases by 3.7% for every oneyear increase in the business relationship age. In a similar vein, an Analysis of Variance shows that the average relationship age is significantly less for churners. This highlights the importance of a wellestablished inter-organizational relationship in B2B operations.

Table 8: Explanatory models

<table><tr><td></td><td>Control Variables</td><td>Rational Assessment Variables</td><td>Heuristic Variables</td><td>Somatic Marker Hypothesis</td><td>AUC on Test Stratum</td></tr><tr><td>1</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2***,+R6*,+R8***</td><td>+H13***</td><td>+H27*R1**,+H29*R5**</td><td>0.6563</td></tr><tr><td>2</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2***,+R6**,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5**</td><td>0.6542</td></tr><tr><td>3</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2***,+R6*,+R8***</td><td>+H13***,+H28**</td><td>+H27*R1***</td><td>0.6524</td></tr><tr><td>4</td><td>-Age***,F1***,F3***</td><td>+R1**,+R2***,+R6**,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5*</td><td>0.6504</td></tr><tr><td>5</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2*,+R6*,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2***</td><td>0.6431</td></tr><tr><td>6</td><td>-Age***,F1***,F2*,F3***</td><td>+R1***,+R2***,+R6**,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2*</td><td>0.6574</td></tr><tr><td>7</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2***,+R6**,+R8***</td><td>+H13***</td><td>+H27*R1***</td><td>0.6568</td></tr><tr><td>8</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2**,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2*,+H29*R5*</td><td>0.6639</td></tr><tr><td>9</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2***,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2***,+H29*R5***</td><td>0.6586</td></tr><tr><td>10</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2*,+R6*,+R8***</td><td>+H13***</td><td>+H27*R1**,+H28*R2**</td><td>0.6591</td></tr></table>

The theoretical variables in the explanatory models are found to increase the odds of churn, corroborating the hypothesized effects of the perceived service pain on SMEs’ decisions to churn. To illustrate, holding other variables fixed, one percent increase in the temporal average of $S Q I _ { 1 }$ proportional pain $( \mathrm { i } . { \mathsf { e } } . \ R _ { 1 } )$ will increase the odds of churn by 7.25%. Furthermore, proportional peak pain is found to either realize or exacerbate the effect of rational pain assessment on churn (e.g. $^ { c } H _ { 2 7 } * R _ { 1 } { } ^ { , } )$ , providing evidence for the hypothesized somatic states in organizational decision making. Proportional peak pain $( H _ { 2 7 } )$ could cause a somatic state in SMEs and calls for a decision on loyalty, which can be made using the related R(ational) measures of service quality $( R _ { 1 } )$

# ACCEPTED MANUSCRIPT

The use of expert opinion as part of the churn detection process calls for verification of the results’ robustness with respect to the labeled churners. We conduct a sensitivity analysis by continuously removing a random 5% of churners from a training stratum and investigating any change in the variables significance after each removal. Table 9 shows that while $R _ { 1 }$ loses its significance after removing 35% of the labeled churners, all other variables carry their significance until the removal of 50% of the labeled churners— showing the robustness of the explanatory models against an important human element in the study.

## 5.2.3. Predicting Organizational Churn with Service Pain Assessment Variables

Table 9: Sensitivity analysis

<table><tr><td colspan="2">Control Variables</td><td>Rational Service Pain Assessment Variables</td><td>Boundedly Rational Service Pain Assessment Variables</td><td>Somatic Marker Hypothesis</td></tr><tr><td>-5%</td><td>-Age***,F1***,F3***</td><td>+R1***,+R2***,+R6***,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5**</td></tr><tr><td>-10%</td><td>-Age***,F1***,F3***</td><td>+R1**,+R2***,+R6***,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5***</td></tr><tr><td>-15%</td><td>-Age***,F1***,F3***</td><td>+R1**,+R2***,+R6***,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5***</td></tr><tr><td>-20%</td><td>-Age***,F1***,F3***</td><td>+R1**,+R2***,+R6***,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5***</td></tr><tr><td>-25%</td><td>-Age***,F1***,F3***</td><td>+R1*,+R2***,+R6***,+R8***</td><td>+H13***</td><td>+H27*R1***,+H28*R2*,+H29*R5***</td></tr><tr><td>-30%</td><td>-Age***,F1***,F3***</td><td>+R1*,+R2***,+R6***,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5***</td></tr><tr><td>-35%</td><td>-Age***,F1***,F3***</td><td>R±,+R2***,+R6***,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5**</td></tr><tr><td>-40%</td><td>-Age***,F1***,F3***</td><td>R±,+R2***,+R6***,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5**</td></tr><tr><td>-45%</td><td>-Age***,F1***,F3***</td><td>R±,+R2***,+R6***,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5**</td></tr><tr><td>-50%</td><td>-Age***,F1***,F3***</td><td>R±,+R2***,+R6***,+R8**</td><td>+H13***</td><td>+H27*R1***,+H28*R2**,+H29*R5*</td></tr><tr><td colspan="5">***Significant at α=0.001, **Significant at α=0.01, *Significant at α=0.05. Significance of the coefficients is based on Wald χ2tests.</td></tr></table>

contribution to the predictive accuracy. Note that we apply the stepwise selection to the whole pool of control, rational, and boundedly rational variables; checking for multicollinearity is not necessary for predictive purposes (Shmueli 2010). The sequence of the predictors entering the logit model is determined by their contributions to the Area Under the ROC Curve (AUC), which is computed against a validation set. In each iteration, specifically, we randomly select two thirds of data set for training and validation, and the remaining one third for test. Table 10 shows the sequence of the predictors entering the model in each iteration and the AUC of the final model on the test stratum. ROC curves address the tradeoff between the model’s true positive and false positive rates at different thresholds (Provost & Fawcett 2013), and Area under ROC curve has been shown to stand out from the rest of accuracy measures (Culver et al. 2006), especially in cases of unbalanced datasets. We supplement our predictive modeling with classification trees as the second most common technique for churn detection (Neslin et al. 2006).

Table 10: Stepwise selection of predictors

<table><tr><td rowspan="2"></td><td colspan="8">Predictors Added in Each Step</td><td colspan="2">AUC on Test Stratum</td></tr><tr><td> $1^{st}$ </td><td> $2^{nd}$ </td><td> $3^{rd}$ </td><td> $4^{th}$ </td><td> $5^{th}$ </td><td> $6^{th}$ </td><td> $7^{th}$ </td><td> $8^{th}$ </td><td>Logit</td><td>Tree</td></tr><tr><td>1</td><td>Age</td><td> $F_3$ </td><td> $H_{13}$ </td><td> $F_1$ </td><td> $R_2$ </td><td> $R_6$ </td><td></td><td></td><td>0.6513</td><td>0.630</td></tr><tr><td>2</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $H_{13}$ </td><td> $R_1$ </td><td> $R_2$ </td><td> $H_{25}$ </td><td></td><td>0.6484</td><td>0.639</td></tr><tr><td>3</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $R_1$ </td><td> $H_{13}$ </td><td> $R_8$ </td><td> $R_2$ </td><td></td><td>0.6479</td><td>0.630</td></tr><tr><td>4</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $H_{13}$ </td><td> $R_2$ </td><td> $R_8$ </td><td> $R_6$ </td><td> $H_{25}$ </td><td>0.6425</td><td>0.625</td></tr><tr><td>5</td><td>Age</td><td> $F_3$ </td><td> $H_{13}$ </td><td> $R_1$ </td><td> $R_8$ </td><td> $F_1$ </td><td> $R_2$ </td><td> $H_{27}$ </td><td>0.6429</td><td>0.623</td></tr><tr><td>6</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $H_{13}$ </td><td> $R_2$ </td><td> $H_{25}$ </td><td> $R_1$ </td><td></td><td>0.6500</td><td>0.633</td></tr><tr><td>7</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $H_{13}$ </td><td> $R_1$ </td><td> $R_8$ </td><td> $R_6$ </td><td></td><td>0.6530</td><td>0.635</td></tr><tr><td>8</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $H_{13}$ </td><td> $R_6$ </td><td></td><td></td><td></td><td>0.6505</td><td>0.633</td></tr><tr><td>9</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $R_2$ </td><td> $R_8$ </td><td></td><td></td><td></td><td>0.6494</td><td>0.637</td></tr><tr><td>10</td><td>Age</td><td> $F_3$ </td><td> $F_1$ </td><td> $H_{13}$ </td><td> $R_2$ </td><td> $R_8$ </td><td></td><td></td><td>0.6504</td><td>0.622</td></tr></table>

Table 10 shows that the first two variables entering the logit models throughout the iterations are controls. Similarly, the contributions to the AUCs indicate that Age is the principal variable in terms of accuracy, highlighting the importance of having a long-term relationship with the service provider in B2B operations. The marginal contribution of the service pain variables beyond Age might be explained by a data limitation; i.e. the pain assessment variables are extracted from a two-year service database. Note that the business relationship age of an average SME with the service company is nearly 11 years. Perhaps other variables could help predict the churn of SMEs with a long-term relationship with the service company.

To examine further the predictive value of the service pain assessment variables, we repeat the above stepwise selection process with solely new customers; i.e. the SMEs with the relationship age of two years or less (for which our database has complete data). These new customers are the ones with which firms do not yet have deep relationships, making them particularly important for analytics-driven operational methods. Table 11 shows that for new customers, the principal predictors in all iterations are the theoretical service pain assessment variables. Modest AUC scores (greater than 0.6) have worthwhile implications in the context of B2C churn (Provost & Fawcett 2013). Modest AUC scores, especially those delivered by parsimonious service quality models, deserve even more attention in the B2B operations (fewer customers, more transactions). Figure 8 depicts a tree trained with the new customers. The numbers in the leaves represent percentage of churners.

Table 11: Churn models for new customers

<table><tr><td rowspan="2"></td><td colspan="4">Predictors Added in Each Step</td><td rowspan="2">AUC on Test Stratum</td></tr><tr><td> $1^{st}$ </td><td> $2^{nd}$ </td><td> $3^{rd}$ </td><td> $4^{th}$ </td></tr><tr><td>1</td><td> $H_{13}$ </td><td> $R_6$ </td><td> $R_8$ </td><td></td><td>0.6221</td></tr><tr><td>2</td><td> $H_{13}$ </td><td> $R_8$ </td><td> $R_6$ </td><td></td><td>0.6004</td></tr><tr><td>3</td><td> $H_{13}$ </td><td> $R_8$ </td><td> $R_1$ </td><td></td><td>0.5900</td></tr><tr><td>4</td><td> $H_{13}$ </td><td> $R_8$ </td><td> $H_{26}$ </td><td> $H_{25}$ </td><td>0.6074</td></tr><tr><td>5</td><td> $R_2$ </td><td> $R_6$ </td><td> $H_{13}$ </td><td> $H_{25}$ </td><td>0.5853</td></tr><tr><td>6</td><td> $R_1$ </td><td> $H_{13}$ </td><td> $H_{29}$ </td><td></td><td>0.6390</td></tr><tr><td>7</td><td> $R_1$ </td><td> $F_1$ </td><td> $H_{26}$ </td><td></td><td>0.6243</td></tr><tr><td>8</td><td> $R_1$ </td><td> $R_8$ </td><td> $H_{13}$ </td><td></td><td>0.5949</td></tr><tr><td>9</td><td> $R_2$ </td><td> $R_8$ </td><td> $R_9$ </td><td></td><td>0.6197</td></tr><tr><td>10</td><td> $R_1$ </td><td> $F_1$ </td><td> $H_{13}$ </td><td></td><td>0.6795</td></tr></table>

## 6. CONCLUSIONS AND FUTURE WORK

Figure 8: Churn tree for new customers  
![](/api/attachments/39V2JH9F/fulltext/images/db8b0a33826b957460317c3ca07c4e35090dbd2203d5a6cc41835cd82359ebe6.jpg)

In this paper we have shown how behavioral economics can inspire feature engineering and help build parsimonious models for an important business problem using theory-driven predictive analytics. Our analyses corroborate the role of the rationality assumption in explaining/ predicting the future behavior of organizations (Friedman 1953; Simon 1979). Besides shedding new light on the rationality debate, the results have important implications for B2B service operations. Our findings suggest that the service company should keep the total service pain low. This is an important finding in B2B operations where the prior conception is that firms do not follow a rational model of service quality assessment in making decisions about service renewals (Bolton et al. 2006). Concomitantly, the service provider should monitor every service failure and be alert to the extensional service evaluation heuristic, which can cause a somatic state for the SME—making it more sensitive to the past total service pain.

## 6.1. Implications for Behavioral Organizational Economics

Behavioral economics views administrative decision-making as a combination of both intuitive and analytical skills (Simon 1997). Accordingly, our feature engineering designed both rational and boundedly rational measures of service pain assessment. The rational measure of pain assessment is simply the temporal average of service pain. The boundedly rational service pain assessment measures are different variants of the two most comprehensive heuristics; i.e. representativeness and availability heuristics (Tversky & Kahneman 1974). These measures also include more rational variants of the heuristic decision rules, which appreciate utility and probability (i.e. extensional target evaluation).

Regarding the analytical service pain evaluation techniques, both descriptive and predictive analyses suggest that the average behavior of SMEs as a group is as if they are rational (Friedman 1953). In particular, the rational measures of service pain evaluation help explain and predict the SMEs’ decisions on churn. Individual SMEs might practice different boundedly rational decision rules; however, it is their assumed rationality that helps explain and predict their future behavior (Friedman 1953, 1978). This finding is also endorsed by Friedman (1953) and Shugan (2009); i.e. the theory’s fruitfulness is evaluated by its predictive accuracy, not by its assumptions realism. Nonetheless, our findings should not characterize the SMEs as wholly rational. What we demonstrate with our analyses is that, overall, the SMEs’ assumed rationality appears to contribute to our models’ statistical and practical significance. This is also consistent with the findings in experimental economics that concur with neoclassical predictions (e.g. List 2004).

Regarding the heuristic service pain evaluation techniques, our findings are consistent with the somatic marker hypothesis in neuroeconomics (Bechara & Damasio 2005). The biasing nature of intuitive decision rules might cause a somatic state which draws the SME’s attention to the service quality issues and calls for judgment, which might be carried out in a relatively rational way. In this vein, while the proportional peak pain draws the SME’s attention to the corresponding service issue, the SME’s information systems may play the role of a working memory that is necessary for coherent analytical reasoning after the somatic marker operates. Being in a somatic state caused by the peak pain, the organization carries out the subsequent evaluation more sensitively. It should be noted, however, that all the intuitive service evaluation measures in the models pertain to extensional target evaluation. That is, they appreciate the service utility and probability, and hence are viewed as logical rules of judgment (Kahneman & Frederick 2002).

The highlighted role of the rationality assumption in our findings can be explained from the behavioral organizational economics standpoint. First, it can be argued that the neoclassical organizational decisionmaking is a special case of bounded rationality (Sontheimer 2006); individuals’ decisions are satisficing and not optimizing due to the limitations on information, analytical processing capacity, and time. Thus, individuals may make optimizing decisions in a situation void of these limitations. For example, the service quality information might be logged by the SME’s information systems. Accordingly, the necessary information is not low in accessibility, and hence waives the need to employ any intuitive heuristic.

Moreover, the analytical processing capacity of a potential group of decision makers in an SME outperforms an individual’s (Oliva & Watson 2009). Lastly, it can be assumed that the SME spends enough that could ultimately affect the SME’s end customers. Each of these speculations deserves subtler investigation that could be undertaken by qualitative studies, which is beyond the scope of this paper.

## 6.2. Implications for Predictive Analytics and Churn

The hybrid deductive-inductive approach to building predictive models for churn makes this research one of the first B2B churn studies where service quality is shown to be an important determinant for customer attrition—especially for those with whom the service provider has not yet established a deep business relationship. This is an important finding for B2B operations, where the number of potential service providers is less than in B2C—making the ‘quality-churn’ connection more difficult to build on. Interestingly, the few B2B churn studies that consider service quality features (e.g. Chen et al. 2014) do not find them among the top ranked predictors. However, the high quality and longitudinal nature of the data used in this study present a compelling case for the importance of service quality in B2B operations.

Furthermore, this paper takes a unique approach to discovering churners and pinpointing their churn dates in a non-contractual environment. This makes the present paper one of the first non-contractual churn studies where subjects have different prediction periods, compared to predetermined prediction periods.

## 6.3. Future work

Future research directions for this research direction concern both behavioral and technical research. A behavioral research direction is on boundedly rational decision rules and their implementation. Behavioral researchers can suggest testing new heuristic decision rules in organizational decision-making. This is especially important considering the highlighted role of somatic states caused by boundedly rational decision rules.

# ACCEPTED MANUSCRIPT

As consumer behavior data are becoming available, technical researchers can employ new algorithms to investigate and apply different ideas in behavioral economics. A future research direction for the present study is if we can strengthen the predictive power by applying the notion of heuristics orchestration from the Fast and Frugal heuristics research (Gigerenzer & Selten 2002). Specifically, is it possible that an SME follows one (or several) boundedly rational decision rules orchestrated on a combination of SQIs? Here, orchestration mechanisms in behavioral economics, and introduce their application in theory-driven predictive analytics.

In conclusion, we have identified the potential in bringing ideas from behavioral economics into predictive analytics in problems where extensive behavioral data is available, such as in IS and Marketing studies that exploit big data and algorithms to derive insights into user behavior. Our work here, using theory-driven predictive analytics and feature engineering, is one approach that we demonstrate to be potentially promising.

## REFERENCES

Almana, A. M., Aksoy, M. S., & Alzahrani, R. (2014). A survey on data mining techniques in customer churn analysis for telecom industry. Journal of Engineering Research and Applications, 4(5), 165-171.

Ariely, D. (1998). Combining experiences over time: The effects of duration, intensity changes and online measurements on retrospective pain evaluations. J. of Behavioral Decision Making, 11(1), 19-45.

Ariely, D., & Carmon, Z. (2003). Summary assessment of experiences: The whole is different from the sum of its parts. Russell Sage Foundation.

Ariely, D., & Loewenstein, G. (2000). When does duration matter in judgment and decision making? Journal of Experimental Psychology: General, 129(4), 508.

Bechara, A., & Damasio, A. R. (2005). The somatic marker hypothesis: A neural theory of economic decision. Games and economic behavior, 52(2), 336-372.

Bentham, Jeremy (1789). The principles of morals and legislation. Dover Publications.

Bolton, R. N., Lemon, K. N., & Bramlett, M. D. (2006). The effect of service experiences over time on a supplier's retention of business customers. Management Science, 52(12), 1811-1823.

Buckinx, W., & Van den Poel, D. (2005). Customer base analysis: partial defection of behaviorally loyal clients in a noncontractual FMCG retail setting. European J. of Operational Research, 164(1), 252-268.

Burez, J., & Van den Poel, D. (2007). CRM at a pay-TV company: Using analytical models to reduce customer attrition by targeted marketing for subscription services. Expert Systems with Applications, 32(2), 277-288.

Camerer, C. F., & Loewenstein, G. (2004). Behavioral economics: Past, present, future. Advances in behavioral economics, 3.

Chen, K., Hu, Y. H., & Hsieh, Y. C. (2014). Predicting customer churn from valuable B2B customers in the logistics industry: a case study. Information Systems and e-Business Management, 1-20.

Culver, M., Kun, D., & Scott, S. (2006, December). Active learning to maximize area under the ROC curve. In Data Mining, 2006. ICDM'06. Sixth International Conference on (pp. 149-158). IEEE.

Damasio, A. (1994, 2005). Descartes' error: Emotion, reason, and the human brain. Putnam Publishing, Penguin Books.

Fader, P., Hardie, B. & Shang, J. (2010). Customer-base analysis in a discrete-time non-contractual setting. Marketing Science, 29(6), 1086-1108.

Fredrickson, B. L., & Kahneman, D. (1993). Duration neglect in retrospective evaluations of affective episodes. Journal of personality and social psychology,65(1), 45.

Friedman, M. (1953). The methodology of positive economics. Essays in positive economics. University of Chicago Press, 3-43.

Friedman, M. (1978). Whitman’s Interview with Milton Friedman. Economically speaking. PBS stations.

George, J. F., Duffy, K., & Ahuja, M. (2000). Countering the anchoring and adjustment bias with decision support systems. Decision Support Systems, 29(2), 195-206.

Gigerenzer, G, & Selten, R (2002). Rethinking rationality. Bounded rationality: The adaptive toolbox, 1-12.

Glady, N., Baesens, B., & Croux, C. (2009). Modeling churn using customer lifetime value. European Journal of Operational Research, 197(1), 402-411.

Goes, P. B. (2013). Editor's comments: information systems research and behavioral economics. MIS quarterly, 37(3), iii-viii.

Hair Jr, J. F., Black, W. C., Babin, B. J., & Anderson, R. E., 2010. Multivariate data analysis. 7<sup>th</sup> Edition.

Hosseini, H. (2003). The arrival of behavioral economics: from Michigan, or the Carnegie School in the 1950s and the early 1960s? Journal of Socio-Economics, 32(4), 391-409.

Jahromi, A. T., Stakhovych, S., & Ewing, M. (2014). Managing B2B customer churn, retention and profitability. Industrial Marketing Management, 43(7), 1258-1268.

Jevons, W. S. (1871). The theory of political economy. Reprinted by Palgrave Macmillan 2013.

Kahneman, D. (2000). Evaluation by moments: Past and future. Choices, values, and frames, 693-708.

Kahneman, D., Diener, E., & Schwarz, N. (2003). Well-being: The foundations of hedonic psychology. Russell Sage Foundation Publications.

Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. Heuristics and biases: The psychology of intuitive judgment, 49-81.

Kahneman, D., Fredrickson, B. L., Schreiber, C. A., & Redelmeier, D. A. (1993). When more pain is preferred to less: Adding a better end. Psychological Science, 4(6), 401-405.

Kahneman, D., & Tversky, A. (Eds.). (2000). Choices, values, and frames. Cambridge University Press.

Kahneman, D., Wakker, P. P., & Sarin, R. (1997). Back to Bentham? Explorations of experienced utility. The Quarterly Journal of Economics, 112(2), 375-406.

Katsikopoulos, K. & Gigerenzer, G. (2013). Behavioral operations management: A blind spot and a research program. Journal of Supply Chain Management, 49(1), 3-7.

Kimball, R., & Caserta, J. (2004). The data warehouse ETL toolkit. John Wiley & Sons.

Koufteros, X., Droge, C., Heim, G., Massad, N., & Vickery, S. K. (2014). Encounter Satisfaction in Etailing: Are the Relationships of Order Fulfillment Service Quality with its Antecedents and Consequences Moderated by Historical Satisfaction? Decision Sciences, 45(1), 5-48.

Kuhn, T. S. (1961). The function of measurement in modern physical science. Isis, 161-193.

Lee, H., Lee, Y., Cho, H., Im, K., & Kim, Y. S. (2011). Mining churning behaviors and developing retention strategies based on a partial least squares model. Decision Support Systems, 52(1), 207-216.

Lemmens, A., & Gupta, S. (2013). Managing churn to maximize profits. Harvard Business School.

Martens, D., Provost, F., Clark, J., & Junqué de Fortuny, E. (2016). Mining massive fine-grained behavior data to improve predictive analytics. MIS Quarterly, 40(4), 1-20.

Martens, D., Vanthienen, J., Verbeke, W., & Baesens, B. (2011). Performance of classification models from a user perspective. Decision Support Systems, 51(4), 782-793.

Miron-Shatz, T., Stone, A., & Kahneman, D. (2009). Memories of yesterday’s emotions: Does the valence of experience affect the memory-experience gap? Emotion, 9(6), 885.

Moeyersoms, J., & Martens, D. (2015). Including high-cardinality attributes in predictive models: A case study in churn prediction in the energy sector. Decision Support Systems, 72, 72-81.

Naumann, E., & Jackson Jr, D. W. (1999). One more time: how do you satisfy customers? Business Horizons, 42(3), 71-76.

Neslin, S. A., Gupta, S., Kamakura, W., Lu, J., & Mason, C. H. (2006). Defection detection: Measuring and understanding the predictive accuracy of customer churn models. Journal of marketing research, 43(2).

Nie, G., Rowe, W., Zhang, L., Tian, Y., & Shi, Y. (2011). Credit card churn forecasting by logistic regression and decision tree. Expert Systems with Applications, 38(12), 15273-15285.

Oliva, R., & Watson, N. (2009). Managing functional biases in organizational forecasts: A case study of consensus forecasting in supply chain planning. Production and Operations Management, 18(2), 138- 151.

Padmanabhan, B., Hevner, A., Cuenco, M. & Shi, C. (2011). From information to operations: Service quality and customer retention. ACM Transactions on Management Information Systems, 2(4).

Provost, F. & Fawcett, T. (2013). Data Science for Business. O’Reilly.

Rauyruen, P., & Miller, K. E. (2007). Relationship quality as a predictor of B2B customer loyalty. Journal of business research, 60(1), 21-31.

Redelmeier, D. A., & Kahneman, D. (1996). Patients' memories of painful medical treatments: real-time and retrospective evaluations of two minimally invasive procedures. Pain, 66(1), 3-8.

Rieskamp, J., Hertwig, R., & Todd, P. M. (2006). Bounded rationality. Handbook of Contemporary Behavioral Economics, Armonk, NY: ME Sharpe, 218-236.

Rust, R., Kumar, V. & Venkatesan, R. (2011). Will the frog change into a prince? Predicting future customer profitability. International Journal of Research in Marketing, 28(4), 281-294.

Saradhi, V. V., & Palshikar, G. K. (2011). Employee churn prediction. Expert Systems with Applications, 38(3), 1999-2006.

Shmueli, G. (2010). To explain or to predict? Statistical science, 25(3), 289-310.

Shmueli, G., & Koppius, O. R. (2011). Predictive analytics in information systems research. MIS Quarterly, 35(3), 553-572.

Shiffman, S., Stone, A. A., & Hufford, M. R. (2008). Ecological momentary assessment. Annu. Rev. Clin. Psychol., 4, 1-32.

Shugan, S. M. (2009). Commentary-Relevancy Is Robust Prediction, Not Alleged Realism. Marketing Science, 28(5), 991-998.

Simon, H. A. (1979). Rational decision making in business organizations. The American economic review, 69(4), 493-513.

Simon, H. A. (1987). Behavioural economics. The new Palgrave: A dictionary of economics, 1, 221-24. Simon, H. (1997a). Administrative Behavior. 4<sup>th</sup> Edition, Free Press.

Sontheimer, K. (2006). Behavioral versus neoclassical economics. Handbook of Contemporary Behavioral Economics: Foundations and Developments, 237.

Tsai, C. F., & Lu, Y. H. (2009). Customer churn prediction by hybrid neural networks. Expert Systems with Applications, 36(10), 12547-12553.

Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. Cognitive psychology, 5(2), 207-232.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124-1131.

Vafeiadis, T., Diamantaras, K. I., Sarigiannidis, G., & Chatzisavvas, K. C. (2015). A comparison of machine learning techniques for customer churn prediction. Simulation Modelling Practice & Theory, 55, 1-9.

Van den Brink, M., Bandell‐ Hoekstra, E. N. G., & Abu‐ Saad, H. H. (2001). The occurrence of recall bias in pediatric headache: a comparison of questionnaire and diary data. Headache: The Journal of Head and Face Pain, 41(1), 11-20.

Van den Poel, D., & Lariviere, B. (2004). Customer attrition analysis for financial services using proportional hazard models. European Journal of Operational Research, 157(1), 196-217.

Verbeke, W., Dejaeger, K., Martens, D., Hur, J., & Baesens, B. (2012). New insights into churn prediction in the telecommunication sector: A profit driven data mining approach. European Journal of Operational Research, 218(1), 211-229.

Wiersema, F. (2013). The B2B Agenda: The current state of B2B marketing and a look ahead. Industrial Marketing Management 42, 470–488.

Yu, X., Guo, S., Guo, J., & Huang, X. (2011). An extended support vector machine forecasting framework for customer churn in e-commerce. Expert Systems with Applications, 38(3), 1425-1430.

Ziliak, S. T., & McCloskey, D. N. (2008). The cult of statistical significance: How the standard error costs us jobs, justice and lives. University of Michigan Press.

## APPENDIX A

The first 26 H(euristic) variables are constructed based on Table 4, since Measure 2 has resulted in more potentially significant statistics than Measure 3. To illustrate, the decision rules whose Measure 2 is equal or greater than 1.2 also cover all such important heuristics per Measure 3. If a specific [DR, SQI] has two statistics (one for $p _ { t }$ and one for $\bar { p } _ { t } )$ both exceeding 1.2, we pick the greater as the representative; except for [DR<sub>3</sub>, SQI<sub>8</sub>], for which we include two variables as they are the only measures greater than 1.3.

# ACCEPTED MANUSCRIPT

The predictive ETL computes two predictors for each of these cells in Table 4; one for Measure 2 and one for Measure 3 (Section 4.1). The first predictor represents the number of times where the conditions for the relevant decision rule held in the SME’s service episode (denoted by an odd index, e.g. $H _ { 1 } )$ , and the second predictor represents a binary flag showing whether that condition held at least once in the SME’s service episode (denoted by an even index, e.g. $H _ { 2 } )$ . The last three decision rules (i.e. $H _ { 2 7 }$ , $H _ { 2 8 }$ , and $H _ { 2 9 } )$ are binary flags that address the highlighted cells in Table 3 (Measure 1) whose statistics are greater than 1.2. To illustrate, $H _ { 2 7 }$ is equal to one if the last proportional pain related to $S Q I _ { 1 }$ has not been experienced by the SME before; i.e. the $S Q I _ { 1 }$ peak pain decision rule holds at the end of the SME’s service episode.

For each SME, the variables are extracted based on that specific SME’s:  
Table A1. Heuristic Decision Rule Variables

<table><tr><td colspan="2">Variable</td><td colspan="2">Heuristic Decision Rule</td></tr><tr><td rowspan="26">Whole Episode</td><td rowspan="8">Availability Heuristics</td><td> $H_1$ </td><td>Number of times that the availability heuristic (incidental frequency) holds with respect to SQI6.</td></tr><tr><td> $H_2$ </td><td>Has the condition for the availability heuristic (incidental frequency) held with respect to SQI6 at least once?</td></tr><tr><td> $H_3$ </td><td>Number of times that the availability heuristic (temporal frequency) holds with respect to SQI6.</td></tr><tr><td> $H_4$ </td><td>Has the condition for the availability heuristic (temporal frequency) held with respect to SQI6 at least once?</td></tr><tr><td> $H_5$ </td><td>Number of times that the availability heuristic (incidental frequency) holds with respect to SQI7.</td></tr><tr><td> $H_6$ </td><td>Has the condition for the availability heuristic (incidental frequency) held with respect to SQI7 at least once?</td></tr><tr><td> $H_7$ </td><td>Number of times that the availability heuristic (temporal frequency) holds with respect to SQI7.</td></tr><tr><td> $H_8$ </td><td>Has the condition for the availability heuristic (temporal frequency) held with respect to SQI7 at least once?</td></tr><tr><td rowspan="18">Representativeness Heuristics</td><td> $H_9$ </td><td>Number of times that the end pain heuristic holds with respect to SQI6.</td></tr><tr><td> $H_{10}$ </td><td>Has the condition for the end pain heuristic held with respect to SQI6 at least once?</td></tr><tr><td> $H_{11}$ </td><td>Number of times that the end pain heuristic holds with respect to SQI7.</td></tr><tr><td> $H_{12}$ </td><td>Has the condition for the end pain heuristic held with respect to SQI7 at least once?</td></tr><tr><td> $H_{13}$ </td><td>Number of times that the extensional end pain heuristic (with  $\bar{p}_t$ ) holds with respect to SQI2.</td></tr><tr><td> $H_{14}$ </td><td>Has the condition for the extensional end pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI2 at least once?</td></tr><tr><td> $H_{15}$ </td><td>Number of times that the extensional end pain heuristic (with  $\bar{p}_t$ ) holds with respect to SQI6.</td></tr><tr><td> $H_{16}$ </td><td>Has the condition for the extensional end pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI6 at least once?</td></tr><tr><td> $H_{17}$ </td><td>Number of times that the extensional end pain heuristic (with  $\bar{p}_t$ ) holds with respect to SQI7.</td></tr><tr><td> $H_{18}$ </td><td>Has the condition for the extensional end pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI7 at least once?</td></tr><tr><td> $H_{19}$ </td><td>Number of times that the peak pain heuristic (with  $\bar{p}_t$ ) holds with respect to SQI6.</td></tr><tr><td> $H_{20}$ </td><td>Has the condition for the peak pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI6 at least once?</td></tr><tr><td> $H_{21}$ </td><td>Number of times that the peak pain heuristic (with  $\bar{p}_t$ ) holds with respect to SQI7.</td></tr><tr><td> $H_{22}$ </td><td>Has the condition for the peak pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI7 at least once?</td></tr><tr><td> $H_{23}$ </td><td>Number of times that the peak pain heuristic (with  $p_t$ ) holds with respect to SQI8.</td></tr><tr><td> $H_{24}$ </td><td>Has the condition for the peak pain heuristic (with  $p_t$ ) held with respect to SQI8 at least once?</td></tr><tr><td> $H_{25}$ </td><td>Number of times that the peak pain heuristic (with  $\bar{p}_t$ ) holds with respect to SQI8.</td></tr><tr><td> $H_{26}$ </td><td>Has the condition for the peak pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI8 at least once?</td></tr><tr><td rowspan="3">Last 6 weeks</td><td rowspan="3">*</td><td> $H_{27}$ </td><td>Has the condition for the peak pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI1 at the end of the episode?</td></tr><tr><td> $H_{28}$ </td><td>Has the condition for the peak pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI2 at the end of the episode?</td></tr><tr><td> $H_{29}$ </td><td>Has the condition for the peak pain heuristic (with  $\bar{p}_t$ ) held with respect to SQI5 at the end of the episode?</td></tr></table>

\* Representativeness Heuristics

# APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

## Highlights

 The paper presents an approach that integrates behavioral economics and predictive analytics in a B2B churn modeling context.

 We present evidence that both rationality and bounded-rationality assumptions play significant roles in predicting organizational decisions on churn.

Unlike many studies at the individual level we do not find strong evidence for human decision making biases or heuristics at play here at the organization level.
