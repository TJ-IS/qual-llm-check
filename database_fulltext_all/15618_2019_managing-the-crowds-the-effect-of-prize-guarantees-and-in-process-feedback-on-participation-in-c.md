---
otero_id: 15618
otero_key: "NNUSRDKN"
title: "Managing the Crowds: The Effect of Prize Guarantees and In-Process Feedback on Participation in Crowdsourcing Contests1"
authors: "Lian Jian; Sha Yang; Sulin Ba; Li Lu; Li Crystal Jiang"
year: "2019"
journal: "MIS Quarterly"
doi: "10.25300/misq/2019/13649"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MANAGING THE CROWDS: THE EFFECT OF PRIZE GUARANTEES AND IN-PROCESS FEEDBACK ON PARTICIPATION IN CROWDSOURCING CONTESTS<sup>1</sup>

Lian Jian Annenberg School of Communication, University of Southern California, Los Angeles, CA 90089 U.S.A. {ljian@usc.edu}

Sha Yang Marshall School of Business, University of Southern California, Los Angeles, CA 90089 U.S.A. {shayang@marshall.usc.edu}

Sulin Ba School of Business, University of Connecticut, Storrs, CT 06268 U.S.A. {sulin.ba@uconn.edu}

Li Lu College of Business & Public Management, West Chester University, West Chester, PA 19383 U.S.A. {llu@wcupa.edu}

Li Crystal Jiang Department of Media and Communication, City University of Hong Kong, Hong Kong, CHINA {crystal.jiang@cityu.edu.hk}

Crowdsourcing contests are contests by which organizations tap into the wisdom of crowds by outsourcing tasks to large groups of people on the Internet. In an online environment often characterized by anonymity and lack of trust, there are inherent uncertainties for participants of such contests. This study focuses on crowdsourcing contests with winner-take-all prizes. During these contests, submissions are made sequentially and contest hosts can provide public in-process feedback to the submissions as soon as they are received. Drawing on the uncertainty literature, we examine how the use of prize guarantees (guaranteeing that a winner will be picked and paid) and in-process feedback (numeric ratings to individual designs and public textual comments during the contest) can help attract more submissions by influencing the various uncertainties faced by the contestants. We find that guaranteeing the prize increases submissions. The volume of in-process feedback (both numeric reviews and textual comments) has a positive effect on the number of submissions, and such an effect is bigger in contests without prize guarantees. In addition, providing highly positive or extremely negative feedback discourages overall future submissions, and the negative effect of highly positive feedback is mitigated in guaranteed contests.

Keywords: Crowdsourcing contest, feedback, prize guarantees, uncertainty, participation

## Introduction

In recent years, it has become popular for businesses to outsource tasks once performed in-house to participants on the Internet, a practice known as crowdsourcing (Howe 2008). Many crowdsourcing activities are organized as contests. While traditionally contests were a privilege of governments and large organizations, the advancement of information technology has reduced the cost of hosting contests, such that relatively smaller-scaled contests can be hosted on crowdsourcing platforms with just a few mouse clicks. These platforms are now routinely used by business for various tasks, including product innovation (Innocentive), graphic design (99designs), software development (TopCoder), and small jobs such as translation (Amazon Mechanical Turk, AMT). On these platforms, hundreds of contests are active at a time. As rewards of these contests are often nontrivial (a few hundred to a few thousand U.S. dollars), financial compensation is an important impetus for participation (Brabham 2010).

As contest hosts become relatively less known, anonymity, lack of trust, and lack of repeated interactions may limit the extent to which crowdsourcing succeeds. Due to the prevalence of incomplete contracting (payment is not guaranteed) and insufficient enforceability (evaluation of work quality is subjective), fraudulent employers (contest hosts) can collect work without paying the participants (Silberman et al. 2010). In a 2013 survey of AMT workers, for example, half of the respondents reported that their work was “regularly rejected unfairly or arbitrarily” (Irani and Silberman 2013). These workers feel exploited and unfairly treated due to payment rejections and low wage (Deng et al. 2016). Similarly, prizes in crowdsourcing contests, though clearly announced at the outset, may not always be awarded.<sup>2</sup> For example, on popular creative design crowdsourcing sites, participants have voiced their concerns by reporting suspicious contest hosts.<sup>3</sup> Clearly, there is a perception that some contest hosts are free-riders.

Another example of suspicious contest host was provided by “Wilnar” on May 26, 2014: “Just want to share this client who is stealing work from their contest which he did not choose as a winner. This is the link of the contest, [link omitted]…. Check the design of [design name omitted] and check the CH website [contest holder’s website omitted].”

In addition to such concerns of free-riding contest hosts (host behavioral uncertainty), participants in crowdsourcing contests also face task uncertainty (the difficulty in gaining a clear set of criteria for evaluating solution quality). For innovative or creative tasks in particular, the evaluation criteria are subjective and are entirely dependent on the contest host’s taste. And finally, in crowdsourcing contests, contestants also face competition uncertainty (the difficulty in assessing one’s own probability of beating other contestants).

This study focuses on these three sources of uncertainties and investigates how the use of prize guarantees (guaranteeing that a winner will be picked and paid) and in-process feedback (numeric reviews to individual designs and public textual comments during the contest) can affect these uncertainties and ultimately influence contest submissions. We find that guaranteeing the prize increases submissions. The volume of in-process feedback also positively influences participation, and this effect is stronger in contests without prize guarantees, where feedback can help in reducing host behavioral uncertainty. However, providing highly positive or extremely negative feedback discourages future submissions. Interestingly, the negative effect of highly positive feedback is mitigated in contests with guaranteed prizes, suggesting that participants are willing to accept more competition uncertainty in guaranteed contests.

The rest of the paper is organized as follows. In the following two sections, we review the literature on crowdsourcing contests and uncertainties in marketplaces. Next, we develop our hypotheses. The subsequent section describes our study site and dataset, followed by a description of the empirical model. We report the results and, finally, we present our conclusions.

## Literature Review

The growing body of research on crowdsourcing contests has studied contestant behaviors, including entry (Araujo 2013), effort (Huang et al. 2012), and submission timing (Bockstedt et al. 2016; Yang et al. 2010). From a contest host’s perspective, predictors of contest outcomes can be either static or time varying throughout the contest. Most studies have focused on the former, studying reward size (Huang et al. 2012), submission visibility (Boudreau and Lakhani 2013; Wooten and Ulrich 2015), contest duration (Yang et al. 2013), and task specificity (Walter and Back 2011). For the latter, a few have explored how participant count (Boudreau et al. 2011) and the existence of a high quality solution (Liu et al. 2014) can affect participation. From a system design perspective, some have proposed ways for improvement such as by recommending tasks to participants (Mo et al. 2018).

Closely relevant to our research, a small number of studies have examined the effect of in-process feedback provided by contest hosts on contest participation. While each study has its own focus, with regard to the effect of feedback on submission quantity, a few consistent findings among these studies are that positive feedback increases the receivers’ own follow-up submissions (Jiang et al. 2016; Wooten and Ulrich 2016), five-star ratings to others’ submissions reduce own submissions (Gross 2017; Jiang et al. 2016), and low ratings (one- or two-star) to others’ submissions encourage own submissions (Jiang et al. 2016).

Our study differs from these studies because we investigate the effects of both highly positive (four or five stars) and extremely negative (marked as “eliminated”) feedback on contest participation. More importantly, we investigate how these effects are moderated by prize guarantees, a variable treated as a control in prior studies (Gross 2017; Jiang et al. 2016).

## Uncertainty in Crowdsourcing Contests

Uncertainty refers to the extent to which the outcome of a future event cannot be accurately predicted based on current information (Pfeffer and Salancik 1978). In online markets, Pavlou et al. (2007) emphasize that it is the perceived uncertainty, not the objective uncertainty, that affects buyers’ purchasing intentions. As buyers tend to overestimate potential losses (Kahneman and Tversky 1979), they tend to associate perceived uncertainties with perceived risks (Chiles and McMackin 1996), resulting in a negative effect of perceived uncertainties on transaction activities (Dimoka et al. 2012; Hong and Pavlou 2014; Kim and Krishnan 2015).

Uncertainties in marketplaces either stem from the environment of the transaction (i.e., the circumstances of an exchange cannot be clearly specified ex ante) or the behaviors of the parties involved (the performance of the transacting parties cannot be easily evaluated ex post) (Willamson 1975, 1985, 1996). In online marketplaces, uncertainty is primarily reflected in the product involved (environment) and in the sellers’ opportunistic behaviors (e.g., not shipping the product; Pavlou et al. 2007) (behavioral). Following the same logic, in crowdsourcing contests, we identify three uncertainties—task uncertainty (environment), competition uncertainty (environment), and host behavioral uncertainty (behavioral)—which we discuss in detail below.

Task uncertainty is the uncertainty in the evaluation criteria of the task solutions. For certain tasks (e.g., programming), evaluating a solution is straightforward and the challenge is in locating the expertise (Terwiesch and Xu 2008). For creative or innovative tasks, however, the very problems being solved are often ill structured and they “become well structured problems only in the process of being prepared for the problem solvers” (Simon 1973, p. 186). Solving such problems typically involves first generating a few alternative solutions, testing them, and then iteratively revising until a good solution is reached (von Hippel and Tyre 1995).

Competition uncertainty is the uncertainty in one’s chance of winning the competition (Hong et al. 2016). It is particularly important in the contests we study because these contests are winner-take-all (single-prize): losers make efforts but receive no compensation. Game theoretical analyses of this type of contests (Konrad and Leininger 2007; Liu et al. 2014; Segev and Sela 2014) and prior empirical work (Gill and Prowse 2012; Hong et al. 2016; Jian et al. 2016; Liu et al. 2014) have identified a discouragement effect: a prior high quality entry discourages future submissions, as it reduces future participants’ perceived likelihood of winning.

Host behavioral uncertainty refers to the difficulty participants face in assessing whether their work will be evaluated and paid for fairly by the contest host. Behavioral uncertainty in markets is typically caused by information asymmetry— one party of the transaction simply has more transactionrelevant information than the other party (Ackerlof 1970)— and a lack of ex post monitoring and enforcement on opportunistic behaviors (Pavlou et al. 2007). Both factors are present in crowdsourcing contests. Compared to the participants, contest hosts have better information about the task as well as their own true types (intention to pay) ex ante. And ex post, there is limited means for participants to monitor and enforce contest host behavior.

## Hypotheses

We focus on the per-period submission quantity in a contest as our main measure of participation. Since every submission costs time and effort, and thus exposes the participant to risks and uncertainties, the per-period measure of the submission quantity is a real-time response to contest hosts’ choices including both the static features of the contest and their inprocess interactions with the participants. Prior studies have identified the number of submissions as an important performance metric for crowdsourcing contests (Terwiesch and Xu 2008), as it robustly predicts the quality of the best solutions (Girotra et al. 2010; Osborn 1953).

## Guarantee

For a contest host, guaranteeing a contest means prepaying the amount of the prize through an escrow service offered by the platform. Assuming that the platform is trustworthy, guaranteed prizes are nonrefundable and have to be allocated to the contest winners. Therefore, prize guarantees eliminate host behavioral uncertainty entirely. Since host behavioral uncertainty affects participation negatively, removing it should encourage participation. We hypothesize

H1 (main effect of guarantee): Guaranteed contests will receive more submissions than nonguaranteed contests.

## Volume of In-Process Feedback

In-process feedback provides a communication channel between the contest host and the participants, so that participants can receive intermediate opinions from the host and revise their submissions accordingly. As previously mentioned, because many creative or innovate tasks are ill defined up front, frequent iterations are an optimal way for reducing the task uncertainty. Lower task uncertainty can reduce participants’ perceived risk of investing effort in a wrong direction, thus reducing the expected cost of submission.

In addition to reducing task uncertainty, we argue that inprocess feedback can also help in reducing host behavioral uncertainty. In online transactions with strangers, nothing can guarantee the absence of opportunistic behaviors objectively. For a risk-conscious participant to engage in transactions with a contest host who does not offer a prize guarantee, all the participant can do is to use the observed current behaviors of the contest host to predict her future behavior, even though such a prediction can be subjective. Everything else being equal, compared to a contest host who is silent during the entire contest, a host who engages with her contestants regularly via in-process feedback can create a perception that she is behaving according to norms of practices on the platform, that is, to pay a winner at the end of the contest.<sup>4</sup>

In summary, because in-process feedback can reduce both task uncertainty and perceived host behavioral uncertainty, we expect it to increase submissions. In our study context we observe two kinds of in-process feedback: numeric reviews to individual submissions and textual comments. Because each numeric review is directed at a submission, it is the result of a trial test and provides valuable data for estimating the contest host’s tastes. We hypothesize

H2a (main effect of review volume): Higher cumulative numbers of reviews lead to more per-period submissions.

In addition, textual comments reveal richer information than do numerical reviews (Daft and Lengel 1986), even though they are typically not directed at any individual entry. Such general comments can provide guidance for participants by either narrowing their search space or pointing to promising directions. Because the cost of coming up with new solutions is reduced (Gross 2017), submissions are expected to increase. We hypothesize

H2b (main effect of comment volume): Higher cumulative numbers of comments lead to more perperiod submissions.

## Negative Reviews and Comments

In addition to feedback volume, the content of feedback can also affect contest outcome (Chevalier and Mayzlin 2006), especially if submissions (and their ratings) are publicly revealed (Segev and Sela 2014). Usually, contest hosts can provide ratings such as one to five stars. Additionally, some platforms even allow negative ratings by marking a submission as “eliminated” (see Table 1 for all possible reviews). Since these ratings are highly subjective, everything else being equal, a large number of eliminated submissions can indicate that the contest host has high standards, strong opinions, and is hard to please. Extremely negative reviews tend to get noticed by users and often have considerable influence (Chevalier and Mayzlin 2006). Therefore, we hypothesize

H3a (main effect of negative reviews): Higher cumulative numbers of negative reviews lead to fewer per-period submissions.

Similarly, public negative textual comments (such as “Please show some originality”) can also be discouraging, as they signal a contest host’s overall negativity toward the submissions received. We hypothesize the following:

H3b (main effect of negative comments): Higher cumulative numbers of negative comments lead to fewer per-period submissions.

## High Reviews and Comments

Providing high ratings to existing entries might reveal useful information about the contest host’s tastes, which can reduce task uncertainty and therefore increase submissions. In addition, giving high ratings also suggests that the host may not be overly picky, and it makes it harder for her to deny payment later by citing low quality of submission. Such a reduction in contest hosts’ behavioral uncertainty should also increase submissions. On the other hand, in crowdsourcing contests, unless one is the direct receiver of high ratings, high ratings to others’ submissions can deter own submission due to the discouragement effect (Jian et al. 2016; Segev and Sela 2014).

In our study context, the competition is intense: a runner-up receives nothing but in many cases would have spent an amount of effort similar to the winner. On the other hand, there are plenty of outside options if one decides to exit or not enter a contest already crowded with competition; hundreds of new contests are posted on the platform everyday. On balance, we expect that even though high ratings can reduce task uncertainty and host behavioral uncertainty to a certain extent, these reductions are secondary to the discouragement effect. We hypothesize

H4a (main effect of high reviews): Higher cumulative numbers of highly rated submissions lead to fewer per-period submissions.

Similarly, public textual comments that praise existing submissions excessively can also reduce submissions, due to the perceived high competition they signal. We hypothesize

H4b (main effect of high comments): Higher cumulative numbers of highly positive comments lead to fewer per-period submissions.

## Moderating Effects

In a guaranteed contest, the contestants face no host behavioral uncertainty. Therefore, the positive effect of in-process feedback in attracting submissions is limited to reducing task uncertainty. In contrast, in contests without guarantees, inprocess feedback also helps to reduce host behavioral uncertainty, as suggested by H2a and H2b. Therefore, we expect the positive effect of feedback volume to be weaker in guaranteed contests, and hypothesize

H5a (effect of review volume moderated): The positive effect of review volume in attracting submissions is weaker in guaranteed than in nonguaranteed contests.

H5b (effect of comment volume moderated): The positive effect of comment volume in attracting submissions is weaker in guaranteed than in nonguaranteed contests.

As we expect negative feedback to discourage submission because it may imply that the contest host has high standards (H3a and H3b), in guaranteed contests such an effect does not exist: a contest host cannot deny payment. Therefore, we expect the negative effect of negative ratings and comments to be weaker in guaranteed contests, and hypothesize

H6a (effect of negative ratings moderated): The negative effect of the cumulative number of negative ratings in attracting submissions is weaker in guaranteed than in non-guaranteed contests.

H6b (effect of negative comments moderated): The negative effect of the cumulative number of negative comments in attracting submissions is weaker in guaranteed than in non-guaranteed contests.

As suggested by H4a and H4b, highly positive reviews or textual comments indicate strong competition, which could discourage future submissions. Everything else being equal, we expect such a discouragement effect to be weaker in contests with prize guarantees, because the certainty of a reward being given can offset to a certain extent the reduced probability of winning due to intensified competition. If a contest is highly competitive and no guarantee is given, contestants presumably would have low incentive to participate. Therefore, we hypothesize

H7a (effect of high reviews moderated): The negative effect of the cumulative number of highly rated submissions on the number of per-period submissions attracted is weaker in guaranteed than in non-guaranteed contests.

H7b (effect of high comments moderated): The negative effect of the cumulative number of highly positive comments on the number of per-period submissions is weaker in guaranteed than in nonguaranteed contests.

## Study Context and Dataset

Founded in 2008 and a leading crowdsourcing platform, the site we study specializes in graphic designs such as logos and webpages.<sup>5</sup> Before a contest’s launch, a contest host specifies the task, the prize amount, the duration (typically seven days), and whether to guarantee the prize (i.e., depositing the full, nonrefundable amount of the prize into an escrow account). Upon contest completion, the amount will be transferred to the winner chosen by the contest host. The web interfaces as well as the timeline of a contest are described in Appendix A.

<table><tr><td colspan="3">Table 1. The Numerical Reviews and Their Interpretations</td></tr><tr><td>Rating</td><td>Meaning on the Site</td><td>Operationalization</td></tr><tr><td>Eliminated</td><td>Has no potential, not the right direction</td><td>Negative review</td></tr><tr><td>1</td><td>Has potential</td><td rowspan="3">Low positive (or neutral) review</td></tr><tr><td>2</td><td>Right direction</td></tr><tr><td>3</td><td>Good design</td></tr><tr><td>4</td><td>Great design</td><td rowspan="2">High review</td></tr><tr><td>5</td><td>Leading contender</td></tr><tr><td>Not Rated</td><td>The contest host has not rated it</td><td>No review</td></tr></table>

During a contest, a contest host can interact with her contestants mainly in two ways. First, she can provide reviews (ranging from 1 to 5, see Table 1) to the existing submissions. She can also rate submissions negatively by marking them as “eliminated.” Second, a contest host can post public textual comments, which are not attached to individual submissions.

With the site’s permission, we collected data on all the logo design contests posted between June 23 and July 5, 2011 (n $= 1 , 0 3 1 ) , ^ { 6 }$ with 322 (31%) contests guaranteed. Among the remaining 709 (69%), 242 (34%) did not pay. Most of the contest hosts (75%) were first-time hosts. For each contest, we recorded every 12 hours the number of submissions, the rating of each submission, and the comments posted. We also recorded static contest characteristics (i.e., prize and guarantee). For each contest host, we recorded the number of contests they had held and paid out, and the average percentage of submissions they had rated in the past.

## Model Specification

The empirical analyses contain two parts. First, to test H1 (main effect of guarantee), a cross-sectional model was employed to estimate the effect of Guarantee on Entries , the total number of entries received by contest i. Due to the potential selection biases in contest hosts’ choices to guarantee their prizes, we estimated the treatment effect of Guarantee using the following five methods: propensity score matching (PSM), nearest neighbor matching (NNM), regression adjustment (RA), inverse-probability weighting (IPW), and IPW regression adjustment (IPWRA). The predictors of Guarantee included characteristics of the contest host as well as decisions made by the host at the same time of determining prize guarantees (therefore might be correlated). The former included MeanReviewRate , the mean proportion of submissions rated in the past, and $P a y R a t e _ { i } ,$ the proportion of contests paid out in the past. The latter included Prize and FastTrack (whether the contest lasted for fewer than four days).

Second, to examine the effects of in-process feedback, a panel analysis was employed to predict the dependent variable (DV), NewEntries , a per-period measure of the number of entries submitted to contest i during period t. Since it is a count variable with overdispersion, we employ a negative binomial model. In Equation (1), for the sake of exposition, we present our model in a linear form while keeping in mind that the negative binomial model is nonlinear.

$$
\begin{array}{l} \text { NewEntries } _ {i, t} = \beta_ {0} + \beta_ {1} \log (\text { NegativeComments } _ {i, t - 1}) + \\ \beta_ {3} \log (\text { HighReview } _ {i, t - 1}) + \beta_ {4} \log (\text { NegativeComments } _ {i, t - 1}) + \\ \beta_ {5} \log (\text { CommentVolume } _ {i, t - 1}) + \beta_ {6} \log (\text { HighComments } _ {i, t - 1}) + (1) \\ \delta_ {1} \log (\text { Contestants } _ {i, t - 1}) + \delta_ {2} \log (\text { MedianSubmissions } _ {i, t - 1}) + \\ \delta_ {3} \log (\text { NewContests } _ {i, t}) + \alpha_ {t} C _ {i} + \omega_ {1} \text { Period } _ {t} + \omega_ {2} \text { Weekend } _ {i, t} + \varepsilon_ {i, t} \end{array}\tag{1}
$$

where the variables are defined in Table 2. $C _ { i }$ is a contestlevel dummy for the fixed effects, to account for idiosyncratic characteristics of the contest hosts and the contests. The independent variables (IV) on in-process feedback (i.e., $N e g a t i \nu e R e \nu i e w _ { i , t - 1 } .$ , Review $V o l u m e _ { i , t - 1 }$ 4 $H i g h R e \nu i e w _ { i , t - 1 } ,$

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td> $NegativeReview_{i,t-1}$ </td><td>Cumulative number of entries rated negatively (marked as “eliminated”) by the contest host as of period t-1 in contest i</td></tr><tr><td> $ReviewVolume_{i,t-1}$ </td><td>Cumulative number of entries rated (as eliminated or rated 1 ~ 5 stars) by the contest host as of period t-1 in contest i</td></tr><tr><td> $HighReview_{i,t-1}$ </td><td>Cumulative number of entries rated highly (either 4 or 5, out of 5 stars) by the contest host as of period t-1 in contest i</td></tr><tr><td> $NegativeComments_{i,t-1}$ </td><td>Cumulative number of negative comments posted by the contest host as of period t-1 in contest i</td></tr><tr><td> $CommentVolume_{i,t-1}$ </td><td>Cumulative number of comments posted by the contest host as of period t-1 in contest i</td></tr><tr><td> $HighComments_{i,t-1}$ </td><td>Cumulative number of highly positive comments posted by the contest host as of period t-1 in contest i</td></tr><tr><td> $Contestants_{i,t-1}$ </td><td>Cumulative number of contestants in contest i as of period t-1</td></tr><tr><td> $MedianSubmissions_{i,t-1}$ </td><td>Median number of submissions per contestant among all existing contestants in contest i as of period t-1</td></tr><tr><td> $NewContests_{i,t}$ </td><td>Number of contests posted on the site during period t for contest i</td></tr><tr><td> $Period_t$ </td><td>Dummy for period: last period,  $2^{nd}$  last,  $3^{rd}$  last ... $13^{th}$  last</td></tr><tr><td> $Weekend_{i,t}$ </td><td>Dummy variable indicating period t of contest i falls on a weekend</td></tr><tr><td> $Prize_i$ </td><td>The prize amount in U.S. $</td></tr><tr><td> $Guarantee_i$ </td><td>Dummy that equals one if contest i&#x27;s prize is guaranteed.</td></tr><tr><td> $MeanReviewRate_i$ </td><td>Mean percentage of entries rated in all previous contests held by the host of contest i*</td></tr><tr><td> $PayRate_i$ </td><td>The percentage of past contests paid by the contest host*</td></tr></table>

\*For first-time contest hosts, this value was set to zero.

$N e g a t i \nu e C o m m e n t s _ { i , t - 1 } ,$ $C o m m e n t V o l u m e _ { i , t - 1 } ,$ and $H i g h C o m m e n t s _ { i , t - 1 } )$ are cumulative counts by period t-1 and are log-transformed. They are lagged by one period because our hypotheses presuppose a decision-making process in which participants view the feedback provided by the contest host in the previous period before making submission decisions. For the content of feedback, only the negative and highly positive categories are included in the model, implying that the low positives and neutral comments are the omitted baselines.

Comments by contest hosts were human-coded into three categories: neutral, high, and negative. Neutral comments provide information about preferences of the contest host or the procedure of winner selection. High comments are those indicating that a winner has emerged $( \mathrm { e . g . }$ ., “Excellent work so far! We will have a difficult time deciding on a winner”). And last, negative comments are those that indicate a general dissatisfaction with the submissions (e.g., “If you do not have the guts to create something original, please do not try to impress me”). Two coders coded all of the 1,548 comments independently (Cohen’s Kappa 0.93) and agreed 97.16% of the time. Disagreements were resolved by a random tiebreaker.

For control variables, first, as $R e \nu i e w V o l u m e _ { i , t - 1 }$ is naturally correlated with the current participation level, we controlled for it using Contestants<sub>i,t-1</sub>, the number of contestants in contest i as of period $t { - } 1 . ^ { 7 }$ Second, contests might attract participants who tend to make different numbers of repeated submissions. To account for such variation, we controlled for the median<sup>8</sup> number of submissions per contestant as of period $t - 1 , M e d i a n S u b m i s s i o n s _ { i , t - 1 } .$ We also included the number of new contests posted on the site in period t of contest i, $N e w C o n t e s t s _ { i , t } ,$ to account for market competition. Third, we added a period dummy, $P e r i o d _ { t } ,$ to control for the time trend,<sup>9</sup> and a dummy, $W e e k e n d _ { i , t } ,$ to control for the difference between weekdays and weekends.

To examine the interaction effects between the six IVs and Guarantee , we add

$$
\beta_ {k} = \beta_ {k 0} + \beta_ {k 1} G u a r a n t e e _ {i}\tag{2}
$$

where $k = \left\{ 1 , . . . , 6 \right\}$ The descriptive statistics are reported in Table 3 and the correlations in Table 4. Due to a few fairly highly correlated variables, to check whether such correlations cause multicollinearity concerns, we ran a pooled OLS regression and obtained a maximum VIF of 8.62 among all simple and interaction terms, which is below the maximum acceptable level of 10.

## Results

## Treatment Effects of Guarantee

The results of the logistic regression used to predict treatment (Guarantee) are reported in Table 5. The estimated coefficients are sensible, showing that both PayRate and Prize have statistically significant positive effects. For the two matching methods (PSM and NNM), the ratio was 1:1 and was well balanced between the treated and the control on all four covariates.<sup>10</sup>

Since the decision to guarantee the prize is made by the individual contest host, not the platform, we believe that the average treatment effect on the treated (ATET) is more relevant to this study than the average treatment effect (ATE). Across all five methods, the ATET of Guarantee (reported in Table 6) was between 45.31 and 52.28, supporting H1 (positive effect of guarantee). These estimates suggest that for those contests with prize guarantees, the prize guarantee itself increased the number of submissions by about 50 on average.

## Effects of In-Process Feedback

The raw estimated coefficients are reported in Table 7. Hypotheses of main effects (H2a–H4b) will be tested based on the estimated coefficients in model (1). For the interaction effects (H5a–H7b), although model (2) provides coefficients of the interaction terms, due to the nonlinear nature of our empirical model, their actual marginal effects need to be evaluated at each data point and averaged across the entire sample before drawing correct inferences (Norton et al. 2004). Therefore, in Table 8, we report their average marginal effects (AME) when Guarantee = 1 (column 1), Guarantee = 0 (column 2), and their differences (column 3). Testing an interaction effect therefore amounts to checking the sign and statistical significance of the differences (column 3) in Table 8. Finally, we summarize all the results of hypothesis testing in Table 9.

H2a, effect of review volume, is supported; the coefficient of $L o g ( R e \nu i e w V o l u m e _ { i , t - 1 } )$ is positive and statistically significant $( \beta _ { 2 } = 0 . 1 1 , p < 0 . 0 0 1 )$ in model (1). Since Log(Review $V o l u m e _ { i , t - 1 } )$ is a log-transformed variable, the raw coefficients are elasticities: a 1% increase in $R e \nu i e w V o l u m e _ { i , t - 1 }$ leads to a 0.11% increase in $N e w E n t r i e s _ { i , t - 1 }$ Similarly, H2b is supported: the coefficient on Log(CommentVolume<sub>i,t-1</sub>) is positive and statistically significant $( \beta _ { 5 } = 0 . 2 1 , p < 0 . 0 0 1 )$

H3a and H3b, negative effects of negative reviews and comments, are both supported. In model (1), the coefficients on Log(NegativeReview ) (β = -0.06, p < 0.001) and Log(NegativeComment $s _ { i , t - 1 } ) \ ( \beta _ { 4 } = - 0 . 9 0 , p < 0 . 0 5 )$ are both negative and statistically significant.

H4a and H4b, negative effects of high reviews and comments, are both supported. In model (1), the coefficients on $L o g ( H i g h R e \nu i e w _ { i , t - 1 } ) \quad ( \beta _ { 3 } ~ = ~ - 0 . 2 9 , ~ p ~ < ~ 0 . 0 0 1 )$ and $L o g ( H i g h C o m m e n t s _ { i , t - 1 } ) \ ( \beta _ { 6 } = - 0 . 1 6 , p < 0 . 0 5 )$ are both negative and statistically significant.

H5a predicted that the positive effect of review volume would be weaker in guaranteed contests. It would be supported if the difference (column 3 in Table 8) were negative and statistically significant. Indeed, we find that the difference is -0.88 $( p < 0 . 0 5 )$ , which supports H5a. According to the AMEs reported in column 1 and 2, a 1% increase in Review $V o l u m e _ { i , t - 1 }$ leads to a 0.70% increase in NewEntries in guaranteed contests and a 1.58% increase in non-guaranteed contests. We further illustrate this interaction effect in panel (a) in Figure 1, which plots the AME of Log(Review $V o l u m e _ { i , t - 1 } )$ when Guarantee = 0 and 1 with all fixed effects set to zero. H5b, the negative interaction effect between $L o g ( C o m m e n t V o l u m e _ { i , t - 1 } )$ and Guarantee , is also supported: the difference between the AMEs of Log(CommentVolume ) in guaranteed and non-guaranteed contests is -3.15 (p < 0.05). The interaction effect is plotted in panel (b) in Figure 1.

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>Std. Dev.</td><td>Median</td><td>Min</td><td>Max</td></tr><tr><td> $NewEntries_{i,t}$ </td><td>13,665</td><td>6.35</td><td>14.28</td><td>2</td><td>0</td><td>1013</td></tr><tr><td> $NegativeReview_{i,t-1}$ </td><td>13,665</td><td>5.19</td><td>23.66</td><td>0</td><td>0</td><td>1048</td></tr><tr><td> $ReviewVolume_{i,t-1}$ </td><td>13,665</td><td>13.35</td><td>35.10</td><td>3</td><td>0</td><td>1129</td></tr><tr><td> $HighReview_{i,t-1}$ </td><td>13,665</td><td>1.74</td><td>4.70</td><td>0</td><td>0</td><td>96</td></tr><tr><td> $NegativeComments_{i,t-1}$ </td><td>13,665</td><td>0.003</td><td>0.07</td><td>0</td><td>0</td><td>2</td></tr><tr><td> $CommentVolume_{i,t-1}$ </td><td>13,665</td><td>0.60</td><td>1.52</td><td>0</td><td>0</td><td>17</td></tr><tr><td> $HighComments_{i,t-1}$ </td><td>13,665</td><td>0.16</td><td>0.72</td><td>0</td><td>0</td><td>14</td></tr><tr><td> $Contestants_{i,t-1}$ </td><td>13,665</td><td>7.08</td><td>13.07</td><td>4</td><td>0</td><td>424</td></tr><tr><td> $MedianSubmissions_{i,t-1}$ </td><td>13,665</td><td>1.74</td><td>1.45</td><td>1.5</td><td>0</td><td>24</td></tr><tr><td> $NewContests_{i,t}$ </td><td>13,665</td><td>32.90</td><td>25.33</td><td>31</td><td>0</td><td>94</td></tr><tr><td> $Prize_i$ </td><td>1,031</td><td>255.87</td><td>96.4</td><td>200</td><td>200</td><td>1744</td></tr><tr><td> $Guarantee_i$ </td><td>1,031</td><td>0.31</td><td>0.46</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $MeanReviewRate_i$ </td><td>1,031</td><td>16.5</td><td>33.03</td><td>0</td><td>0</td><td>100</td></tr><tr><td> $PayRate_i$ </td><td>1,031</td><td>0.17</td><td>0.36</td><td>0</td><td>0</td><td>1</td></tr></table>

Table 4. Correlations among All Variables

<table><tr><td colspan="2"></td><td>[1]</td><td>[2]</td><td>[3]</td><td>[4]</td><td>[5]</td><td>[6]</td><td>[7]</td><td>[8]</td><td>[9]</td><td>[10]</td><td>[11]</td><td>[12]</td><td>[13]</td><td>[14]</td></tr><tr><td>[1]</td><td> $NewEntries_{i,t}$ </td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[2]</td><td> $Log(NegativeReview_{i,t-1})$ </td><td>0.34</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[3]</td><td> $Log(ReviewVolume_{i,t-1})$ </td><td>0.39</td><td>0.68</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[4]</td><td> $Log(HighReview_{i,t-1})$ </td><td>0.28</td><td>0.42</td><td>0.7</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[5]</td><td> $Log(NegativeComments_{i,t-1})$ </td><td>0.02</td><td>0.06</td><td>0.05</td><td>0.07</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[6]</td><td> $Log(CommentVolume_{i,t-1})$ </td><td>0.12</td><td>0.25</td><td>0.38</td><td>0.36</td><td>0.12</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[7]</td><td> $Log(HighComments_{i,t-1})$ </td><td>0.05</td><td>0.14</td><td>0.23</td><td>0.25</td><td>0.04</td><td>0.66</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[8]</td><td> $Log(Contestants_{i,t-1})$ </td><td>0.43</td><td>0.55</td><td>0.78</td><td>0.51</td><td>0.04</td><td>0.31</td><td>0.17</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[9]</td><td> $Log(MedianSubmissions_{i,t-1})$ </td><td>0.15</td><td>0.31</td><td>0.54</td><td>0.39</td><td>0.02</td><td>0.28</td><td>0.18</td><td>0.57</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[10]</td><td> $Log(NewContests_{i,t})$ </td><td>-0.12</td><td>-0.19</td><td>-0.28</td><td>-0.22</td><td>0.00</td><td>-0.15</td><td>-0.1</td><td>-0.3</td><td>-0.23</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>[11]</td><td> $Log(Prize_i)$ </td><td>0.25</td><td>0.19</td><td>0.2</td><td>0.11</td><td>-0.01</td><td>-0.05</td><td>-0.06</td><td>0.27</td><td>0.02</td><td>0.02</td><td>1</td><td></td><td></td><td></td></tr><tr><td>[12]</td><td> $Guarantee_i$ </td><td>0.16</td><td>0.17</td><td>0.22</td><td>0.22</td><td>0.00</td><td>0.22</td><td>0.12</td><td>0.18</td><td>0.05</td><td>0.03</td><td>0.07</td><td>1</td><td></td><td></td></tr><tr><td>[13]</td><td> $PayRate_i$ </td><td>0.04</td><td>-0.03</td><td>0.08</td><td>0.05</td><td>-0.01</td><td>0.03</td><td>0.00</td><td>0.12</td><td>0.01</td><td>0.01</td><td>0.03</td><td>0.2</td><td>1</td><td></td></tr><tr><td>[14]</td><td> $MeanReviewRate_i$ </td><td>0.05</td><td>0.03</td><td>0.11</td><td>0.06</td><td>-0.01</td><td>0.00</td><td>-0.02</td><td>0.11</td><td>0.01</td><td>0.03</td><td>0.09</td><td>0.14</td><td>0.75</td><td>1</td></tr><tr><td>[15]</td><td> $Log(NewEntries_{i,t-1})$ </td><td>0.42</td><td>0.48</td><td>0.65</td><td>0.44</td><td>0.03</td><td>0.28</td><td>0.15</td><td>0.76</td><td>0.48</td><td>-0.19</td><td>0.27</td><td>0.22</td><td>0.08</td><td>0.09</td></tr></table>

Note: Correlation coefficients in bold indicates that they are statistically significant at the 5% level or higher.

Table 5. Results of Logistic Regression as Part of the Propensity Score Matching Process

<table><tr><td rowspan="2"></td><td colspan="2">Logistic Regression</td></tr><tr><td colspan="2">DV = Guaranteei</td></tr><tr><td>Prizei</td><td>0.002*</td><td>(0.001)</td></tr><tr><td>FastTracki</td><td>-0.073</td><td>(0.280)</td></tr><tr><td>PayRatei</td><td>1.292***</td><td>(0.283)</td></tr><tr><td>MeanReviewRatei</td><td>-0.002</td><td>(0.003)</td></tr><tr><td>Constant</td><td>-1.390***</td><td>(0.200)</td></tr><tr><td>Observations</td><td colspan="2">1,031</td></tr></table>

Standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

<table><tr><td colspan="3">Table 6. Estimates of Treatment Effects of Guarantee on total  $Entries_i$ </td></tr><tr><td></td><td>Estimated ATET</td><td>Observations</td></tr><tr><td>Propensity Score Matching (PSM)</td><td>47.12***(7.18)</td><td>644 treated and control</td></tr><tr><td>Nearest Neighbor Matching (NNM)</td><td>52.28***(6.63)</td><td>644 treated and control</td></tr><tr><td>Regression Adjustment (RA)</td><td>45.99***(6.50)</td><td>1,031</td></tr><tr><td>Inverse-Probability Weighting (IPW)</td><td>46.67***(6.41)</td><td>1,031</td></tr><tr><td>IPW Regression Adjustment (IPWRA)</td><td>45.31***(6.42)</td><td>1,031</td></tr></table>

Robust standard errors are in parentheses and for both PSM and NNM, robust Abadie-Imbens standard errors are reported. For both PSM and NNM, the matching ratio was 1:1. \*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

Table 7. Unconditional Negative Binomial Model with FE as Dummies Predicting the Number of New Submissions During Period t in Contest i

<table><tr><td rowspan="3"></td><td colspan="4">DV = NewEntriesi,t</td></tr><tr><td colspan="4">Unconditional Negative Binomial with FE as Dummies</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.06</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.08*</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.11*</td><td>(0.05)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-1.26</td><td>(0.80)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.29***</td><td>(0.08)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.33*</td><td>(0.14)</td></tr><tr><td>Log(Contestantsi,t-1) × Gua</td><td></td><td></td><td>0.16***</td><td>(0.05)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>-0.06***</td><td>(0.01)</td><td>-0.09***</td><td>(0.02)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.11***</td><td>(0.02)</td><td>0.14***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.29***</td><td>(0.02)</td><td>-0.36***</td><td>(0.03)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-0.90*</td><td>(0.40)</td><td>0.00</td><td>(0.81)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.21***</td><td>(0.04)</td><td>0.32***</td><td>(0.06)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.16*</td><td>(0.07)</td><td>-0.32***</td><td>(0.09)</td></tr><tr><td>Log(Contestantsi,t-1)</td><td>0.17***</td><td>(0.03)</td><td>0.09*</td><td>(0.04)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>-0.09*</td><td>(0.04)</td><td>-0.08</td><td>(0.04)</td></tr><tr><td>Log(NewContestsi,t)</td><td>0.01</td><td>(0.01)</td><td>0.01</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,01</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.67</td><td colspan="2">0.67</td></tr><tr><td>LL</td><td colspan="2">,602.99</td><td colspan="2">-32,580.53</td></tr><tr><td>AIC</td><td colspan="2">65,251.98</td><td colspan="2">65,207.07</td></tr><tr><td>BIC</td><td colspan="2">65,424.99</td><td colspan="2">65,380.09</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the over-dispersion parameter. “Gua” is a short for “Guarantee.” $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1 , ^ { \star \star } \mathsf { p } <$ $0 . 0 1 , { } ^ { \star } \mathsf { p } < 0 . 0 5$

Table 8. Average Marginal Effects of In-Process Feedback on NewEntries<sub>i,t</sub>

<table><tr><td rowspan="2"></td><td colspan="6">Average Marginal Effects of Feedback on NewEntriesi,t</td></tr><tr><td colspan="2">Guarantee = 1</td><td colspan="2">Guarantee = 0</td><td colspan="2">Difference</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>-0.33</td><td>(0.23)</td><td>-0.98**</td><td>(0.32)</td><td>0.64</td><td>(0.38)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.70</td><td>(0.43)</td><td>1.58***</td><td>(0.46)</td><td>-0.88*</td><td>(0.43)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-2.85***</td><td>(0.88)</td><td>-3.93***</td><td>(1.05)</td><td>1.09*</td><td>(0.54)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-14.52*</td><td>(6.73)</td><td>0.03</td><td>(8.90)</td><td>-14.55</td><td>(10.74)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.45</td><td>(0.66)</td><td>3.60**</td><td>(1.24)</td><td>-3.15*</td><td>(1.28)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>0.06</td><td>(1.20)</td><td>-3.58**</td><td>(1.25)</td><td>3.64*</td><td>(1.52)</td></tr></table>

Average marginal effects calculated as the mean marginal effects evaluated at the variables’ values in the sample. Standard errors derived with the delta-method are reported in parentheses. ${ } ^ { \star \star \star } p < 0 . 0 0 1 ,$ ${ } ^ { \star \star } p < 0 . 0 1 ,$ \*p < 0.05

<table><tr><td colspan="2">Table 9. Summary of Results of Hypothesis Testing</td></tr><tr><td>Hypotheses</td><td>Results</td></tr><tr><td>H1 (main effect of guarantee)</td><td>Supported</td></tr><tr><td>H2a (main effect of review volume)</td><td>Supported</td></tr><tr><td>H2b (main effect of comment volume)</td><td>Supported</td></tr><tr><td>H3a (main effect of negative reviews)</td><td>Supported</td></tr><tr><td>H3b (main effect of negative comments)</td><td>Supported</td></tr><tr><td>H4a (main effect of high reviews)</td><td>Supported</td></tr><tr><td>H4b (main effect of high comments)</td><td>Supported</td></tr><tr><td>H5a (effect of review volume moderated)</td><td>Supported</td></tr><tr><td>H5b (effect of comment volume moderated)</td><td>Supported</td></tr><tr><td>H6a (effect of negative reviews moderated)</td><td>No</td></tr><tr><td>H6b (effect of negative comments moderated)</td><td>No</td></tr><tr><td>H7a (effect of high reviews moderated)</td><td>Supported</td></tr><tr><td>H7b (effect of high comments moderated)</td><td>Supported</td></tr></table>

![](/api/attachments/NNUSRDKN/fulltext/images/62f7a3a26b3dd56358fcc79325c2766f4e865a98c70ee3f09997db0d5804177d.jpg)

![](/api/attachments/NNUSRDKN/fulltext/images/5105f7bd26c5c2da12693ccf74d801aad78c89d7d1af2b67be181b70d3543cc5.jpg)

![](/api/attachments/NNUSRDKN/fulltext/images/af945847eca4ce0733331a6e9296687f90d906140a5ea39f3f5650e6ee965c17.jpg)

![](/api/attachments/NNUSRDKN/fulltext/images/c54094ecf3caf4eebf67461cc1f400ef1dc7279fbba5e4692abe7f8eb42c6d61.jpg)  
Figure 1. The Average Marginal Effect of Log(ReviewVolume<sub>i,t-1</sub>), Log(HighReview<sub>i,t-1</sub>), Log(CommentVolume<sub>i,t-1</sub>), and Log(HighComments<sub>i,t-1</sub>) on NewEntries<sub>i,t</sub>

H6a and H6b predicted that negative reviews and comments would have weaker effects in guaranteed contests than in nonguaranteed ones. Neither is supported: the two differential effects (column 3 in Table 8) have the expected signs but are statistically nonsignificant.

Finally, H7a and H7b (effect of high reviews and high comments moderated) are supported. The AME of $L o g ( H i g h R e \nu i e w _ { i , t - 1 } ) , - 2 . 8 5 ( p < 0 . 0 0 1 )$ , is smaller in magnitude in guaranteed contests than in non-guaranteed contests, $- 3 . 9 3 \ ( p < 0 . 0 0 1 )$ Their difference, 1.09, is positive and statistically significant $( p < 0 . 0 5 )$ The interaction effect is illustrated in panel (c) of Figure 1. For H7b, although the AMEs are statistically nonsignificant, their difference, 3.64, is $( p < 0 . 0 5 )$ . Panel (d) in Figure 1 plots the interaction, which shows that in guaranteed contests, high comments have near zero effects but in non-guaranteed contests, the effect is negative.

## Instrumental Variables to Address Endogeneity Due to Time-Varying Effects

The fixed effects in our main model cannot account for timevarying endogenous factors. Therefore we take an instrumental variable approach to address this issue, by adopting a popularly used method which starts by identifying other similar observations and then takes the means of the same variables for these observations as instruments (Albuquerque and Bronnenberg 2009; Ducarroz et al. 2016). As noted by Gross (2017), although a contest host’s feedback provision behaviors can be endogenously affected by time-varying factors, in practice they mainly reflect the contest host’s “type (engaged or aloof)” (p. 445). We also believe that contest hosts follow different feedback styles. Some log on frequently and engage with the participants as much as possible while others like to leave the participants alone. With this assumption, if we can identify other contest hosts with a similar feedback style, the means of the same variables can be computed from these similar contests, to be used as instruments.

To identify contest hosts with similar review provision styles, in step 1, we created a variable called Delay, which measured the time it took (in periods) for the contest host to provide a rating for the first entry received in her contest. This first entry was chosen because it was submitted early in the contest, before potential time-varying external factors could influence the feedback provision behavior of the contest host. Each contest is matched with all other contests with the exact same Delay. In step 2, among all the contests matched in step 1, we took the N (= 30) nearest neighbors, with the distance measured by the sum of the absolute distances along the following six variables: Guarantee, Weekend, DayTime (dummy indicating day versus night time), HostExperience (whether the host is a first-timer), MeanReviewRate, and Prize.<sup>11</sup>

To generate the instrument variables for the three comment variables, in step 1, all contests with the same EverComment (a dummy variable indicating whether the contest host posted any comment at all throughout the entire contest) were identified. And in Step 2, the N (= 30) nearest neighbors were identified among the contests matched in step 1. To instrument for CommentVolume , the distance was measured by the sum of the absolute distances along the same six variables as above. To instrument for NegativeComments , a seventh variable, EverNegativeComment (whether the contest holder gave any negative comment throughout the contest) was added to compute the neighbor distance. Similarly, to instrument for HighComments , a seventh variable, EverHighComment (whether the contest holder gave any high comment throughout the contest) was added to compute the neighbor distance.<sup>12</sup> Every contest in our dataset found N matches.

To be valid instruments, our instrument variables (descriptive statistics in Table E1 in Appendix E) should first be correlated with the potentially endogenous variables. To verify this, we show that in the first stage regression (in Table E2 in Appendix E), most of the coefficients are highly statistically significant. Furthermore, since these instruments are derived from other contests, they should have no effect on the focal contest’s outcome other than through the potentially endogenous explanatory variables, satisfying the exclusion restriction.

Table 10 contains results of the second stage control function analyses. That is, the residuals in the first stage regressions are entered as control variables into an unconditional negative binomial model with fixed effects modeled as dummy variables (the same as our main model). Most hypotheses supported in the main model are still supported. Two hypotheses have lost support: H3a (main effect of negative reviews) and H3b (main effect of negative comments).

## Robustness Tests and Alternative Model Specifications

The first robustness test we conducted was to replace the cumulative independent variables with per-period measures. The results (in Appendix F) are qualitatively similar to our main results. We also explored the possibility that there could be a word-of-mouth effect (Duan et al. 2009) by including a lagged DV, NewEntries<sub>i,t-1</sub>. To address the autocorrelation and endogeneity introduced due to the inclusion of a lagged DV, we used the Arellano-Bond linear estimator and logtransformed the dependent variable. The results reported in Appendix G demonstrate that our main results are again robust to this alternative model specification.

Two additional alternative models were explored. First, an individual contestant-level analysis was conducted to verify our results obtained at the contest level. The results (in Appendix H) reveal that the majority of our main results are robust. Second, we reanalyzed our models by replacing the DV with Contestants , the number of newly joined contestants in period t. The results (in Appendix I) demonstrate that our main results are largely robust to this alternative DV.

## Discussion and Implications

We have examined the effects of payment guarantees and inprocess feedback on participation in crowdsourcing contests. We find that guaranteeing the prize, thereby eliminating contest host behavioral uncertainty, helps attract more submissions. In-process feedback, either in the form of numeric ratings or textual comments, increases the number of submissions. And this effect is significantly stronger in contests without prize guarantees. We interpret these results as demonstrating that in-process feedback can reduce both task uncertainty and contest host behavioral uncertainty and help attract submissions.

<table><tr><td colspan="5">Table 10. Results of Control-Function Estimation with Negative Binomial Model with Fixed Effects Modeled as Dummy Variables</td></tr><tr><td rowspan="3"></td><td colspan="4"> $DV = NewEntries_{i,t}$ </td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td> $Log(NegativeReview_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-1.81</td><td>(0.93)</td></tr><tr><td> $Log(ReviewVolume_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-0.48**</td><td>(0.17)</td></tr><tr><td> $Log(HighReview_{i,t-1}) \times Gua$ </td><td></td><td></td><td>3.88*</td><td>(1.62)</td></tr><tr><td> $Log(NegativeComments_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-8.12</td><td>(9.04)</td></tr><tr><td> $Log(CommentVolume_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-3.26**</td><td>(1.16)</td></tr><tr><td> $Log(HighComments_{i,t-1}) \times Gua$ </td><td></td><td></td><td>2.81**</td><td>(0.97)</td></tr><tr><td> $Log(Contestants_{i,t-1}) \times Gua$ </td><td></td><td></td><td>1.02**</td><td>(0.39)</td></tr><tr><td> $Log(NegativeReview_{i,t-1})$ </td><td>0.98</td><td>(0.61)</td><td>0.70</td><td>(0.74)</td></tr><tr><td> $Log(ReviewVolume_{i,t-1})$ </td><td>0.88***</td><td>(0.11)</td><td>0.92***</td><td>(0.13)</td></tr><tr><td> $Log(HighReview_{i,t-1})$ </td><td>-3.73***</td><td>(1.09)</td><td>-3.56**</td><td>(1.32)</td></tr><tr><td> $Log(NegativeComments_{i,t-1})$ </td><td>-4.01</td><td>(3.18)</td><td>5.32</td><td>(9.19)</td></tr><tr><td> $Log(CommentVolume_{i,t-1})$ </td><td>3.08***</td><td>(0.72)</td><td>2.86**</td><td>(0.92)</td></tr><tr><td> $Log(HighComments_{i,t-1})$ </td><td>-2.48***</td><td>(0.50)</td><td>-2.38**</td><td>(0.73)</td></tr><tr><td> $Log(Contestants_{i,t-1})$ </td><td>-0.51*</td><td>(0.22)</td><td>-0.54</td><td>(0.28)</td></tr><tr><td> $Log(MedianSubmn_{i,t-1})$ </td><td>0.10</td><td>(0.13)</td><td>0.04</td><td>(0.15)</td></tr><tr><td> $Log(NewContests_{i,t})$ </td><td>0.00</td><td>(0.01)</td><td>0.00</td><td>(0.02)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Residuals of first stage regression</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.63</td><td colspan="2">0.61</td></tr><tr><td>LL</td><td colspan="2">-32,356.74</td><td colspan="2">-32,252.79</td></tr><tr><td>AIC</td><td colspan="2">64,749.47</td><td colspan="2">64,547.57</td></tr><tr><td>BIC</td><td colspan="2">64,884.88</td><td colspan="2">64,705.55</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the over-dispersion parameter. \*\*\*p < 0.001, $\star \star _ { \mathsf { p } } < 0 . 0 1$ , \*p < 0.05.

Interestingly, our findings reveal that the content of in-process feedback can affect participation as well. We identify an overall negative effect of highly positive feedback (numeric reviews or textual comments), most likely because participants try to avoid competition. Moreover, we find that this negative effect is weaker in guaranteed contests. That is, with prize guarantees, participants tend to be less deterred by the level of competition they face. On the other hand, overly critical feedback also tends to discourage submissions. This can be because participants perceive that the contest host is hard to please and therefore unlikely to pay.

This study contributes to the crowdsourcing contest literature by highlighting the effect of feedback content on contest participation. While prior research has identified the negative effect of highly positive feedback, this study finds that their negative effects vary depending on whether the prize is guaranteed. Similarly, the effects of feedback volume also vary depending on prize guarantees.

As for practical implications, our results about the volume and content of in-process feedback indicate that contest hosts need to maintain regular communication with their participants. Contest hosts should also be cautious when providing highly positive or highly critical feedback, especially when their prizes are not guaranteed. We suggest that crowdsourcing platforms reconfirm with the contest hosts when such types of feedback are about to be sent.

Our study has a few limitations. First, effort was not observable but could have been a relevant variable for studying contestant choices under uncertainties. And second, the timing of submissions and feedback were not available on the site so we had to record it every 12 hours. The precision of this measure can be improved in future. Furthermore, in future work, the results of our study need to be verified on other crowdsourcing platforms with different types of tasks (e.g., programming), or exhibiting different web interface features or community characteristics.

## Acknowledgments

We would like to thank the three anonymous reviewers for their insightful comments that helped to improve the paper significantly.

## References

Ackerlof, G. A. 1970. “The Market for ‘Lemons’: Quality Uncertainty and the Market Mechanism." The Quarterly Journal of Economics (84:3), pp. 488-500.

Albuquerque, P., and Bronnenberg, B. J. 2009. “Estimating Demand heterogeneity Using Aggregated Data: An Application to the Frozen Pizza Catgory,” Marketing Science (28:2), pp. 356-372.

Araujo, R. M. 2013. “99designs: An Analysis of Creative Competition in Crowdsourced Design,” in Proceedings of the First AAAI Conference on Human Computation and Crowdsourcing, Palm Springs, CA, pp. 17-24.

Bockstedt, J., Druehl, C., and Mishra, A. 2016. “Heterogeneous Submission Behavior and Its Implications for Success in Innovation Contests with Public Submissions,” Production and Operations Management.

Boudreau, K. J., Lacetera, N., and Lakhani, K. R. 2011. “Incentives and Problem Uncertainty in Innovation Contests: An Empirical Analysis,” Management Science (57:5), pp. 843-863.

Boudreau, K. J., and Lakhani, K. 2013. “Cumulative Innovation and Open Disclosure of Intermediate Results: Evidence from a Policy Experiment in Bioinformatics,” Working Paper, Harvard Business School.

Brabham, D. C. 2010. “Moving the Crowd at Threadless,” Information, Communication & Society (13:8), pp. 1122-1145.

Chevalier, J. A., and Mayzlin, D. 2006. “The Effect of Word of Mouth on Sales: Online Book Reviews,” Journal of Marketing Research (43:3), pp. 345-354.

Chiles, T. H., and McMackin, J. F. 1996. “Integrating Variable Risk Preference, Trust, and Transaction Cost Economics,” Academy of Management Review (21:1), pp. 73-99.

Daft, R. L., and Lengel, R. H. 1986. “Organizational Information Requirements, Media Richness and Structural Design,” Management Science (32:5), pp. 554-571.

Deng, X., Joshi, K. D., and Galliers, R. D. 2016. “The Duality of Empowerment and Marginalization in Microtask Crowdsourcing: Giving Voice to the less Powerful Through Value Sensitive Design,” MIS Quarterly (40:2), pp. 279-302.

Dimoka, A., Hong, Y., and Pavlou, P. A. 2012. “On Product Uncertainty in Online Markets: Theory and Evidence,” MIS Quarterly (32:2), pp. 395-426.

Duan, W., Gu, B., and Whinston, A. 2009. “Informational Cascades and Software Adoption on the Internet: An Empirical Investigation,” MIS Quarterly (33:1), pp. 23-48.

Ducarroz, C., Yang, S., and Greenleaf, E. A. 2016. “Understanding the Impact of In-Process Promotional Messages: An Application to Online Auctions,” Journal of Marketing (80:2), pp. 80-100.

Gill, D., and Prowse, V. 2012. “A Structural Analysis of Disappointment Aversion in a Real Effort Competition,” American Economic Review (102:1), pp. 469-503.

Girotra, K., Terwiesch, C., and Ulrich, K. T. 2010. “Idea Generation and the Quality of the Best Idea,” Management Science (56:4), pp. 591-605.

Gross, D. P. 2017. “Performance Feedback in Competitive Product Development,” RAND Journal of Economics (48:2), pp. 438-466.

Hong, Y. K., and Pavlou, P. A. 2014. “Product Fit Uncertainty in Online Markets: Nature, Effects, and Antecedents,” Information Systems Research, (25:2), pp. 328-344.

Hong, Y., Wang, C., and Pavlou, P. A. 2016. “Comparing Open and Sealed Bid Auctions: Evidence from Online Labor Markets,” Information Systems Research (27:1), pp. 49-69.

Howe, J. 2008. Crowdsourcing: How the Power of the Crowd Is Driving the Future of Business, New York: Random House.

Huang, Y., Singh, P., and Mukhopadhyay, T. 2012. “How to Design Crowdsourcing Contest: A Structural Empirical Analysis,” paper presented at the Workshop on Information Systems and Economics, Orlando, FL.

Irani, L. C., and Silberman, M. S. 2013. “Turkopticon: Interrupting Worker Invisibility in Amazon Mechanical Turk,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Paris, pp. 611-620.

Jian, L., Li, Z., and Liu, T. X. 2017. “Simultaneous Versus Sequential All-Pay Auctions: An Experimental Study,” Experimental Economics (20:3), pp. 648-669.

Jiang, Z. Z., Huang, Y., and Beil, D. R. 2016. “The Role of Feedback in Dynamic Crowdsourcing Contests: A Structural Empirical Analysis,” Ross School of Business Paper No. 1334, University of Michigan.

Kahneman, D., and Tversky, A. 1979. “Prospect Theory: An Analysis of Decision Under Risk,” Econometrica (47), pp. 263-291.

Kim, Y., and Krishnan, R. 2015. “On Product-Level Uncertainty and Online Purchase Behavior: An Empirical Analysis,” Management Science (61:10), pp. 2449-2467.

Konrad, K. A., and Leininger, W. 2007. “The Generalized Stackelberg Equilibrium of the All-Pay Auction with Complete Information,” Review of Economic Design (11:2), pp. 165-174.

Lakhani, K. R., Jeppesen, L. B., Lohse, P. A., and Panetta, J. A. 2007. “The Value of Openness in Scientific Problem Solving,” Working Paper, Harvard Business School.

Liu, T. X., Yang, J., Adamic, L. A., and Chen, Y. 2014. “Crowdsourcing with All-Pay Auctions: A Field Experiment on Taskcn,” Management Science (60:8), pp. 2020-2037.

Mo, J., Sarkar, S., and Menon, S. 2018. “Know When to Run: Recommendations in Crowdsourcing Contests,” MIS Quarterly (42:3), pp. 919-944.

Norton, E. C., Wang, H., and Ai, C. 2004. “Computing Interaction Effects and Standard Errors in Logit and Probit Models,” Stata Journal (4:2), pp. 154-167.

Osborn, A. F. 1953. Applied Imagination, New York: Charles Scribner’s Sons.

Pavlou, P. A., Liang, H., and Xue, Y. 2007. Understanding and Mitigating Uncertainty in Online Exchange Relationships: A Principal–Agent Perspective,” MIS Quarterly (31:1), pp. 105-136.

Pfeffer, J., and Salancik, G. 1978. The External Control of Organizations: A Resource Dependence Perspective, New York: Harper & Row.

Rubin, D. B. 2001. “Using Propensity Scores to Help Design Observational Studies: Application to the Tobacco Litigation,” Health Services and Outcomes Research Methodology, (2:3), pp. 169-188.

Segev, E., and Sela, A. 2014. “Multi-Stage Sequential All-Pay Auctions,” European Economic Review (70), pp. 371-382.

Silberman, M. S., Ross, J., Irani, L., and Tomlinson, B. 2010. “Sellers’ Problems in Human Computation Markets,” in Proceedings of the ACM SIGKDD Workshop on Human Computation, Washington, DC, pp. 18-21.

Simon, H. A. 1973. “The Structure of Ill Structured Problems,” Artificial Intelligence (4), 4, pp. 181-201.

Terwiesch, C., and Xu, Y. 2008. “Innovation Contests, Open Innovation, and Multiagent Problem Solving,” Management Science (54:9), pp. 1529-1543.

von Hippel, E., and Tyre, M. J. 1995. “How Learning by Doing Is Done: Problem Identification in Novel Process Equipment,” Research Policy (24:1), pp. 1-12.

Walter, T., and Back, A. 2011. “Towards Measuring Crowdsourcing Success: An Empirical Study on Effects of External Factors in Online Idea Contest,” in Proceedings of the 6<sup>th</sup> Mediterranean Conference on Information Systems, Limassol, Cyprus.

Williamson, O. E. 1975. Markets and Hierarchies: Analysis and Antitrust Implications, New York: The Free Press.

Williamson, O. E. 1985. The Economic Institutions of Capitalism: Firms, Markets, Relational Contracting, New York: The Free Press.

Williamson, O. E. 1996. The Mechanisms of Governance, New York: The Free Press.

Wooten, J. O., and Ulrich, K. T. 2015. “The Impact of Visibility in Innovation Tournaments: Evidence from Field Experiments,” University of Pennsylvania Scholarly Commons.

Wooten, J. O., and Ulrich, K. T. 2016. “Idea Generation and the Role of Feedback: Evidence from Field Experiments with Innovation Tournaments,” Production and Operations Management (26:1), pp. 80-99.

Yang, Y., Chen, P.-Y., and Banker, R. 2010. “Impact of Past Performance and Strategic Bidding on Winner Determination of Open Innovation Contest,” in Proceedings of the 21<sup>st</sup> Workshop on Information Systems and Economics, pp. 11-12.

Yang, Y., Chen, P.-Y., and Pavlou, P. A. 2013. “Managing Open Innovation Contests in Online Market,” Working Paper, Temple University, Philadelphia, PA.

## About the Authors

Lian Jian is an assistant professor at the Annenberg School for Communication at the University of Southern California. She earned her Ph.D. from the University of Michigan, Ann Arbor. Her research focuses on crowdsourcing, crowdfunding, collective intelligence, and online rumoring. Her research has been published in journals such as Management Science, Experimental Economics, New Media and Society, and Journal of Computer-Mediated Communication.

Sha Yang is the Ernest Hahn Professor of Marketing at Marshall School of Business, University of Southern California. She received a B.A. in International Economics from Renmin University, China, and an M.S. in Statistics, M.A. in Marketing and Ph.D. in Marketing from the Ohio State University. Her primary research focuses on understanding and modeling consumer purchase behavior and market competition. Her recent research interest focuses on Internet advertising, social media and online marketing applications. Her research has been published in leading journals such as Marketing Science, Management Science, Journal of Marketing Research, Journal of Marketing, and Quantitative Marketing and Economics.

Sulin Ba is the Treibick Family Chair in Information Systems and Associate Dean of Academic and Research Support at the School of Business at the University of Connecticut. She holds a Ph.D. from the University of Texas at Austin. She has published in Management Science, Information Systems Research, MIS Quarterly, Journal of Management Information Systems, Production and Operations Management, Decision Support Systems, and other academic journals. She is a recipient of the prestigious Best Information Systems Publications Award (2010) (given by the Association for Information Systems and its Senior Scholars Consortium), the MIS Quarterly Best Paper Award (2000), UConn School of Business Research Excellence Award (2013), Best Paper Award (2009), Undergraduate Teaching Award (2008), and Teaching Innovation Award (2007). She has served as a senior editor for MIS Quarterly, Production and Operations Management, and Information Systems and e-Business Management. She also serves on the editorial board of Decision Support Systems.

Li Lu is an assistant professor at the Management Department at School of Business and Public Management at West Chester University. She received her M.S. from Cornell University and Ph.D. from University of Southern California. Her research focuses on group decision making and knowledge management. She has published in Personality and Social Psychology Review and Journal of Organizational Behavior.

Crystal Li Jiang is an associate professor in the Department of Communication at City University of Hong Kong. She received her Ph.D. from Cornell University. Her research focuses on interpersonal processes mediated by information and communication technology, message design, and narrative persuasion in health communication, and mediated perceptions for different gender and ethnic groups.

# MANAGING THE CROWDS: THE EFFECT OF PRIZE GUARANTEES AND IN-PROCESS FEEDBACK ON PARTICIPATION IN CROWDSOURCING CONTESTS

Lian Jian Annenberg School of Communication, University of Southern California, Los Angeles, CA 90089 U.S.A. {ljian@usc.edu}

Sha Yang Marshall School of Business, University of Southern California, Los Angeles, CA 90089 U.S.A. {shayang@marshall.usc.edu}

Sulin Ba School of Business, University of Connecticut, Storrs, CT 06268 U.S.A. {sulin.ba@uconn.edu}

Li Lu College of Business & Public Management, West Chester University, West Chester, PA 19383 U.S.A. {llu@wcupa.edu}

Li Crystal Jiang Department of Media and Communication, City University of Hong Kong, Hong Kong, CHINA {crystal.jiang@cityu.edu.hk}

## Appendix A

## Study Site Description

![](/api/attachments/NNUSRDKN/fulltext/images/337ff217ccb94f7398019c4c7a8aa074a860094d45b86dba551330d87cee28e9.jpg)

Figure A1. Timeline of a Typical Contest

<table><tr><td>Contest Title</td><td>Contest Holder</td><td>Ends</td><td>Entries</td><td>Package</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #1A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #1</td><td>14 hours</td><td>58</td><td>bronzeAU$299</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #2A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #2</td><td>15 hours</td><td>99</td><td>bronzeCA$299</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #3A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #3</td><td>15 hours</td><td>52</td><td>bronze$299guaranteed</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #4A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #4</td><td>16 hours</td><td>151</td><td>bronze$299</td></tr></table>

As of May 2016, the site we study has hosted more than 350,000 contests and paid more than \$100 million to participants. At the time of our data collection in June 2011, 125,527 users were registered on the platform, and more than 6 million designs had been submitted. On this site, a typical contest goes through three stages (see Figure A1): before, during, and after the contest. As soon as a contest is launched, any visitor to the site can discover it by clicking the “browse projects” link on the front page. All projects at various stages are shown on this page (see Figure A2), including the title of the task, the name of the contest host, the time left, the number of entries received, and the prize amount. If a contest’s prize is guaranteed, the word “guaranteed” appears under the prize amount. A visitor can sort the contests by the last three columns (i.e., the time left on the contest, the number of entries received, and the prize amount).

By default, the contests are sorted such that those closing the soonest appear on the top. During a contest, all the existing entries are displayed in descending order of their ratings (see Figure A3). Underneath the design, the entry number (indicating the order in which it was submitted), the screen name of the contestant, and the rating it received (if any) are displayed

## Appendix B

## Robustness Test of Using the Cumulative Number of Entries by Period t-1 as the Control Variable for the Current Level of Participation

The results of replacing the control variable Log(Contestants ) with $L o g ( E n t r i e s _ { i , t - 1 } )$ reported in Table B1. All the estimated coefficients are similar to those reported in Table 7 in their signs, magnitude, and statistical significance, except that the coefficient on Log(NegativeReview<sub>i,t-1</sub>) × Gua has become statistically significant while it was not in the main model in Table 7, thus providing support for H7a (effect of negative reviews moderated).

<table><tr><td rowspan="3"></td><td colspan="4"> $DV = NewEntries_{i,t}$ </td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td> $\text{Log}(\text{NegativeReview}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.07*</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{ReviewVolume}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>-0.13**</td><td>(0.04)</td></tr><tr><td> $\text{Log}(\text{HighReview}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.10*</td><td>(0.04)</td></tr><tr><td> $\text{Log}(\text{NegativeComments}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>-1.20</td><td>(0.76)</td></tr><tr><td> $\text{Log}(\text{CommentVolume}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>-0.29***</td><td>(0.08)</td></tr><tr><td> $\text{Log}(\text{HighComments}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.31*</td><td>(0.14)</td></tr><tr><td> $\text{Log}(\text{Entries}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.18***</td><td>(0.04)</td></tr><tr><td> $\text{Log}(\text{NegativeReview}_{i,t-1})$ </td><td>-0.05***</td><td>(0.01)</td><td>-0.08***</td><td>(0.02)</td></tr><tr><td> $\text{Log}(\text{ReviewVolume}_{i,t-1})$ </td><td>0.21***</td><td>(0.02)</td><td>0.25***</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{HighReview}_{i,t-1})$ </td><td>-0.30***</td><td>(0.02)</td><td>-0.36***</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{NegativeComments}_{i,t-1})$ </td><td>-0.94*</td><td>(0.43)</td><td>-0.08</td><td>(0.79)</td></tr><tr><td> $\text{Log}(\text{CommentVolume}_{i,t-1})$ </td><td>0.27***</td><td>(0.04)</td><td>0.36***</td><td>(0.06)</td></tr><tr><td> $\text{Log}(\text{HighComments}_{i,t-1})$ </td><td>-0.20**</td><td>(0.07)</td><td>-0.34***</td><td>(0.09)</td></tr><tr><td> $\text{Log}(\text{Entries}_{i,t-1})$ </td><td>-0.16***</td><td>(0.03)</td><td>-0.24***</td><td>(0.04)</td></tr><tr><td> $\text{Log}(\text{MedianSubmn}_{i,t-1})$ </td><td>0.05</td><td>(0.04)</td><td>0.08</td><td>(0.04)</td></tr><tr><td> $\text{Log}(\text{NewContests}_{i,t})$ </td><td>0.02</td><td>(0.01)</td><td>0.01</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.68</td><td colspan="2">0.67</td></tr><tr><td>LL</td><td colspan="2">-32,602.40</td><td colspan="2">-32,568.30</td></tr><tr><td>AIC</td><td colspan="2">65,250.81</td><td colspan="2">65,182.61</td></tr><tr><td>BIC</td><td colspan="2">65,423.82</td><td colspan="2">65,356.63</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the overdispersion parameter. “Gua” is short for Guarantee. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1 , ^ { \star \star } \mathsf { p } < 0 . 0 1$ ${ \star } _ { \mathsf { p } } < 0 . 0 5$

## Appendix C

Robustness Test of Dropping the Last Period  
![](/api/attachments/NNUSRDKN/fulltext/images/5d1f62cf9aac19d7466d8e2ba2ba8b3776ecfe40e7bee5baf00f28f43d11170d.jpg)  
Figure C1. The Number of New Entries Submitted During Each Period

Figure C1 plots the mean number of new submissions by period. Because a spike was observed in the last period, a robustness check was conducted by dropping the last period in the panel. Our analyses show that dropping the last period does not change our results qualitatively. The estimated coefficients as reported in Table C1 are similar to those produced by the main model (in Table 7) in terms of their signs, magnitude, and statistical significance, except that the interaction effect $L o g ( H i g h R e \nu i e w _ { i , t - 1 } ) $ × Gua has become marginally significant $\left( p = \right.$ 0.06).

<table><tr><td colspan="5">Table C1. Unconditional Negative Binomial Model with FE as Dummies Predicting the Number of New Entries During Period t in Contest i</td></tr><tr><td rowspan="3"></td><td colspan="4">DV = NewEntriesi,t</td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.06</td><td>(0.04)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.10*</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.09+</td><td>(0.05)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-1.53</td><td>(0.99)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.30**</td><td>(0.11)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.38*</td><td>(0.16)</td></tr><tr><td>Log(Entriesi,t-1) × Gua</td><td></td><td></td><td>0.24***</td><td>(0.05)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>-0.05*</td><td>(0.02)</td><td>-0.08**</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.12***</td><td>(0.03)</td><td>0.15***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.20***</td><td>(0.02)</td><td>-0.25***</td><td>(0.03)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-1.07**</td><td>(0.36)</td><td>0.01</td><td>(0.83)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.26***</td><td>(0.05)</td><td>0.37***</td><td>(0.08)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.18*</td><td>(0.08)</td><td>-0.37**</td><td>(0.12)</td></tr><tr><td>Log(Entriesi,t-1)</td><td>0.09</td><td>(0.06)</td><td>-0.03</td><td>(0.07)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>-0.12*</td><td>(0.05)</td><td>-0.09</td><td>(0.06)</td></tr><tr><td>Log(NewContestsi,t)</td><td>0.04**</td><td>(0.01)</td><td>0.03*</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">12,634</td><td colspan="2">12,634</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.68</td><td colspan="2">0.68</td></tr><tr><td>LL</td><td colspan="2">-28,355.70</td><td colspan="2">-28,322.07</td></tr><tr><td>AIC</td><td colspan="2">56,771.40</td><td colspan="2">56,704.13</td></tr><tr><td>BIC</td><td colspan="2">56,994.73</td><td colspan="2">56,927.46</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the over-dispersion parameter. “Gua” is short for Guarantee. $^ { \star \star \star } \mathsf { p } { < } 0 . 0 0 1 , ^ { \star \star } \mathsf { p } { < } 0 . 0 1$ ${ } ^ { \star } { \mathsf p } { < } 0 . 0 5 , { } + { \mathsf p } { < } 0 . 1$

## Appendix D

## Propensity Score Matching Diagnosis

Figure D1 demonstrates that the distributions of propensity scores among contests with and without guarantees exhibit substantial overlap, indicating sufficient matching.

![](/api/attachments/NNUSRDKN/fulltext/images/ce6808fbd4661647e7089d4c72d7a6500add400cb9bb7ff1f164b730b7f8447e.jpg)

Figure D1. Distribution of Propensity Scores Among Contests With and Without Prize Guarantees

## Appendix E

## Instrument Variable Analyses

Descriptive statistics of the instrument variables are reported in Table E1 and the first stage regression results are reported in Table E2.

<table><tr><td colspan="6">Table E1. Descriptive Statistics of Instrumental Variables</td></tr><tr><td>Variable</td><td>N</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td> $SimNegativeReview_{i,t-1}$ </td><td>13,665</td><td>4.25</td><td>12.89</td><td>0</td><td>479.14</td></tr><tr><td> $SimReviewVolume_{i,t-1}$ </td><td>13,665</td><td>11.85</td><td>13.99</td><td>0</td><td>94.17</td></tr><tr><td> $SimHighReview_{i,t-1}$ </td><td>13,665</td><td>2.13</td><td>6.31</td><td>0</td><td>277.11</td></tr><tr><td> $SimNegativeComments_{i,t-1}$ </td><td>13,665</td><td>0.0001</td><td>0.002</td><td>0</td><td>0.07</td></tr><tr><td> $SimCommentVolume_{i,t-1}$ </td><td>13,665</td><td>0.58</td><td>0.82</td><td>0</td><td>3.43</td></tr><tr><td> $SimHighComments_{i,t-1}$ </td><td>13,665</td><td>0.11</td><td>0.34</td><td>0</td><td>2.2</td></tr></table>

Table E2. First Stage Regression Results

<table><tr><td>DV</td><td colspan="2"> $Log(NegReview_{i,t-1})$ </td><td colspan="2"> $Log(ReviewVol_{i,t-1})$ </td><td colspan="2"> $Log(HighReview_{i,t-1})$ </td><td colspan="2"> $Log(NegComm_{i,t-1})$ </td><td colspan="2"> $Log(CommVol_{i,t-1})$ </td><td colspan="2"> $Log(HighComm_{i,t-1})$ </td></tr><tr><td> $Log(SimNegReview_{i,t-1})$ </td><td>0.35***</td><td>(0.02)</td><td>0.63***</td><td>(.01)</td><td>0.45***</td><td>(0.02)</td><td>0.00</td><td>(.00)</td><td>0.05**</td><td>(0.02)</td><td>0.00</td><td>(.01)</td></tr><tr><td> $Log(SimReviewVol_{i,t-1})$ </td><td>-0.06***</td><td>(0.01)</td><td>0.26***</td><td>(.00)</td><td>-0.04***</td><td>(0.01)</td><td>0.00*</td><td>(.00)</td><td>-0.04***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td></tr><tr><td> $Log(SimHighReview_{i,t-1})$ </td><td>0.39***</td><td>(0.02)</td><td>0.15***</td><td>(.01)</td><td>0.31***</td><td>(0.02)</td><td>0.00</td><td>(.00)</td><td>0.10***</td><td>(0.02)</td><td>0.01*</td><td>(.01)</td></tr><tr><td> $Log(SimNegComm_{i,t-1})$ </td><td>-2.80</td><td>(2.48)</td><td>-2.10*</td><td>(.87)</td><td>1.78</td><td>(2.45)</td><td>1.93***</td><td>(.10)</td><td>12.02***</td><td>(2.00)</td><td>-0.50</td><td>(.59)</td></tr><tr><td> $Log(SimCommVol_{i,t-1})$ </td><td>-0.02*</td><td>(0.01)</td><td>-0.03***</td><td>(.00)</td><td>0.13***</td><td>(0.01)</td><td>0.00*</td><td>(.00)</td><td>0.34***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td></tr><tr><td> $Log(SimHighComm_{i,t-1})$ </td><td>-0.01</td><td>(0.03)</td><td>-0.02</td><td>(.01)</td><td>0.21***</td><td>(0.03)</td><td>0.00</td><td>(.00)</td><td>1.81***</td><td>(0.03)</td><td>0.93***</td><td>(.01)</td></tr><tr><td> $Log(Contestants_{i,t-1})$ </td><td>0.12***</td><td>(0.01)</td><td>0.11***</td><td>(.00)</td><td>-0.13***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td><td>0.06***</td><td>(0.01)</td><td>-0.01</td><td>(.00)</td></tr><tr><td> $Log(MedianSubmn_{i,t-1})$ </td><td>-0.04***</td><td>(0.01)</td><td>0.03***</td><td>(.00)</td><td>0.06***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td><td>0.06***</td><td>(0.01)</td><td>0.01***</td><td>(.00)</td></tr><tr><td> $Log(NewContests_{i,t})$ </td><td>-0.01</td><td>(0.01)</td><td>-0.01*</td><td>(.00)</td><td>-0.02**</td><td>(0.01)</td><td>0.00</td><td>(.00)</td><td>-0.02**</td><td>(0.01)</td><td>0.00</td><td>(.00)</td></tr><tr><td>Contest-level FE</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td> $R^2$ </td><td colspan="2">0.49</td><td colspan="2">0.96</td><td colspan="2">0.55</td><td colspan="2">0.07</td><td colspan="2">0.58</td><td colspan="2">0.65</td></tr></table>

Standard errors in parentheses. Due to space limitations, abbreviations are used, including “Neg” = Negative; “Comm” = Comment or Comments; “Vol” = Volume. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

## Appendix F

## Robustness Test of Using Per-Period (i.e., Noncumulative) Independent Variables

We have added analyses by an alternative model in which the cumulative independent variables were replaced with per-period measures. In Table F1, we report results from an unconditional negative binomial model with fixed effects modeled as dummies. Overall, the results ar qualitatively similar to our main results. All the main effects of in-process feedback have retained their signs, magnitude, and statistical significance except for the coefficient on Log(NewNegativeComments ), which has retained the correct sign. The interaction effects have retained the expected signs but their statistical significance has changed. In particular, among the four moderating effects identified in the main model (Table 7), only the coefficient on Log(NewReviewVolume ) X Gua is still statistically significant. However, two other coefficients that were not statistically significant in the main model have become statistically significant: Log(NewNegativeReview ) × Gua and Log(NewNegativeComments ) × Gua. In summary, the results using per-period measures of independent variables are largely consistent with our main results.

<table><tr><td colspan="5">Table F1. Results of Robustness Tests Using Per-Period Independent Variables in an Unconditional Negative Binomial Model with FE as Dummies</td></tr><tr><td rowspan="3"></td><td colspan="4"> $DV = NewEntries_{i,t}$ </td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td> $\text{Log}(\text{NewNegativeReview}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.09***</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{NewReviewVolume}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>-0.09***</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{NewHighReview}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.06</td><td>(0.05)</td></tr><tr><td> $\text{Log}(\text{NewNegativeComments}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>29.00***</td><td>(1.72)</td></tr><tr><td> $\text{Log}(\text{NewCommentVolume}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>-0.10</td><td>(0.12)</td></tr><tr><td> $\text{Log}(\text{NewHighComments}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.22</td><td>(0.17)</td></tr><tr><td> $\text{Log}(\text{Contestants}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.06*</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{NewNegativeReview}_{i,t-1})$ </td><td>-0.07***</td><td>(0.02)</td><td>-0.12***</td><td>(0.02)</td></tr><tr><td> $\text{Log}(\text{NewReviewVolume}_{i,t-1})$ </td><td>0.22***</td><td>(0.02)</td><td>0.26***</td><td>(0.02)</td></tr><tr><td> $\text{Log}(\text{NewHighReview}_{i,t-1})$ </td><td>-0.16***</td><td>(0.02)</td><td>-0.19***</td><td>(0.04)</td></tr><tr><td> $\text{Log}(\text{NewNegativeComments}_{i,t-1})$ </td><td>-1.14</td><td>(0.85)</td><td>-29.90***</td><td>(2.02)</td></tr><tr><td> $\text{Log}(\text{NewCommentVolume}_{i,t-1})$ </td><td>0.33***</td><td>(0.05)</td><td>0.39***</td><td>(0.06)</td></tr><tr><td> $\text{Log}(\text{NewHighComments}_{i,t-1})$ </td><td>-0.20*</td><td>(0.10)</td><td>-0.31**</td><td>(0.12)</td></tr><tr><td> $\text{Log}(\text{Contestants}_{i,t-1})$ </td><td>0.10***</td><td>(0.03)</td><td>0.06</td><td>(0.09)</td></tr><tr><td> $\text{Log}(\text{MedianSubmn}_{i,t-1})$ </td><td>-0.14***</td><td>(0.03)</td><td>-0.13</td><td>(0.07)</td></tr><tr><td> $\text{Log}(\text{NewContests}_{i,t})$ </td><td>0.02**</td><td>(0.01)</td><td>0.02</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.66</td><td colspan="2">0.66</td></tr><tr><td>LL</td><td colspan="2">-32,545.46</td><td colspan="2">-32,536.65</td></tr><tr><td>AIC</td><td colspan="2">65,220.92</td><td colspan="2">65,095.30</td></tr><tr><td>BIC</td><td colspan="2">65,709.89</td><td colspan="2">65,178.05</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the over-dispersion parameter. “Gua” is short for Guarantee. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1 , ^ { \star \star } \mathsf { p } < 0 . 0 1$ ${ \star } _ { \mathsf { p } } < 0 . 0 5$

## Appendix G

## Robustness Test of Using Arellano-Bond Dynamic Panel-Data Estimator

The results of Arellano-Bond dynamic panel-data estimator with a lagged DV are reported in Table G1. All the coefficients reported in the main model (Table 7) have retained their signs, magnitude, and statistical significance, except the coefficient on Log(NegativeComments ) which has the expected sign but has lost its statistical significance.

<table><tr><td rowspan="3"></td><td colspan="4">DV = Log(NewEntriesi,t)</td></tr><tr><td colspan="4">Arellano-Bond Dynamic Panel-Data Estimator</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.12</td><td>(0.05)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.19*</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.08*</td><td>(0.06)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-3.20</td><td>(2.30)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.15**</td><td>(0.11)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.49*</td><td>(0.20)</td></tr><tr><td>Log(Contestantsi,t-1) × Gua</td><td></td><td></td><td>0.04**</td><td>(0.07)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>-0.22***</td><td>(0.03)</td><td>-0.26***</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.17***</td><td>(0.02)</td><td>0.24***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.50***</td><td>(0.03)</td><td>-0.52***</td><td>(0.04)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-3.81</td><td>(1.47)</td><td>-1.35</td><td>(0.58)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.18***</td><td>(0.05)</td><td>0.27***</td><td>(0.08)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.31*</td><td>(0.10)</td><td>-0.54**</td><td>(0.14)</td></tr><tr><td>Log(Contestantsi,t-1)</td><td>-0.61</td><td>(0.04)</td><td>-0.62*</td><td>(0.05)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>-0.21***</td><td>(0.03)</td><td>-0.22***</td><td>(0.03)</td></tr><tr><td>Log(NewContestsi,t)</td><td>-0.01</td><td>(0.01)</td><td>-0.01</td><td>(0.01)</td></tr><tr><td>Log(NewEntriesi,t-1)</td><td>0.09***</td><td>(0.02)</td><td>0.09***</td><td>(0.02)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period, day/night and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Wald  $\chi^2$ </td><td colspan="2">3810.55(24)</td><td colspan="2">3806.09(31)</td></tr></table>

Robust standard errors are in parentheses. “Gua” is short for Guarantee. For Wald $\chi ^ { 2 }$ tests, the degrees of freedom are reported in parentheses. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1$ $^ { \star \star } \mathsf { p } < 0 . 0 1$ ${ \star } _ { \mathsf { p } } < 0 . 0 5$

## Appendix H

## Contestant-Level Analysis

We conducted individual-level analysis to verify our main results obtained at the contest level. In this contest-contestant-period dataset, each observation focuses on the outcome variable, $n _ { i , j , t } ,$ , the number of submissions contestant j submits to contest i in period t. The dataset contain 1,031 contests and 5,545 contestants. An observation of contest i-contestant j-period t is included in the dataset only if contestant j has submitted at least an entry to contest i before or during period t. In-process feedback variables are added into the model together with thre sets of control variables, ContestantContro $l s _ { i , j , t - 1 } .$ , Contest $\mathrm { \gamma } _ { o n t r o l s _ { i , t - 1 } }$ , and $P e r i o d C o n t r o l s _ { i , t } ,$ as well as two fixed effects at the contest and contestant level respectively, $C _ { i }$ and $C _ { j } .$

$$
\begin{array}{r l} & {\log \left(n _ {i, j, t}\right) = \alpha_ {0} + \alpha_ {1} \log \left(N e g a t i v e R e v i e w _ {i, t - 1}\right) + \alpha_ {2} \log \left(R e v i e w V o l u m e _ {i, t - 1}\right)} \\ & {\qquad + \alpha_ {3} \log \left(H i g h R e v i e w _ {i, t - 1}\right) + \alpha_ {4} \log \left(N e g a t i v e C o m m e n t _ {i, t - 1}\right)} \\ & {\qquad + \alpha_ {5} \log \left(C o m m e n t R e v i e w _ {i, t - 1}\right) + \alpha_ {6} \log \left(H i g h C o m m e n t _ {i, t - 1}\right)} \\ & {\qquad + \alpha_ {7} C o n t e s t C o n t r o l s _ {i, t - 1} + \alpha_ {8} C o n t e s t a n t C o n t r o l s _ {i, t - 1}} \\ & {\qquad + \alpha_ {9} P e r i o d C o n t r o l s _ {i, t} + \delta_ {i} C _ {i} + \delta_ {j} C _ {j} + \varepsilon_ {i, j, t}} \end{array}\tag{3}
$$

The ContestControl $s _ { i , t - 1 }$ is a vector of contest-period specific variables, which includes only $E n t r i e s _ { i , t - 1 }$ (cumulative number of entries contest i receives by period t-1). $C o n t e s t a n t C o n t r o l s _ { i , j , t - 1 }$ includes three variables describing the cumulative reviews contestant j has received from contest i as of period t-1: SelfNegativeReview $\begin{array} { r } { \dot { \mathbf \Xi } _ { i , j , t - 1 } , } \end{array}$ SelfReview $V o l u m e _ { i , j , t - 1 } ,$ and $S e l f H i g h R e \nu i e w _ { i , j , t - 1 }$ These three variables were introduced because prior research has shown that direct feedback received by participants to their own submissions have strong effects on their subsequent submissions (Jiang et al. 2016; Wooten and Ulrich 2016; Yang et al. 2013). The PeriodControl is a vector of contest-period specific variables, which includes $W e e k e n d _ { i , t } , P e r i o d _ { t }$ , and NewContests . To examine the interaction effects, we add

$$
\alpha_ {k} = \alpha_ {k 0} + \alpha_ {k 1} G u a r a n t e e _ {i}\tag{4}
$$

where $\mathrm { k } = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 \}$ . That is, the first six independent variables in equation (3) are interacted with the variable Guarantee .

In Table H1, we report the results of contestant level analyses using two models: a linear model with both contest and contestant level fixed effects and an unconditional negative binomial model with contest-level fixed effects modeled as dummies. The results show that these two models yield results highly consistent in the sign and statistical significance of the coefficients. The results show that all our main results about in-process feedback are born out at the individual contestant level, except the main effect of negative comments (H3b), the effects of comment volume moderated (H5b) and high comments moderated (H7b).

<table><tr><td rowspan="3"></td><td colspan="4"> $DV = Log(NewEntries_{i,j,t})$ </td><td colspan="4"> $DV = NewEntries_{i,j,t}$ </td></tr><tr><td colspan="4">Linear</td><td colspan="4">Unconditional NB with FE as Dummies</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td><td colspan="2">Model (3)</td><td colspan="2">Model (4)</td></tr><tr><td> $Log(NegativeReview_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.00</td><td>(0.01)</td><td></td><td></td><td>0.01</td><td>(0.02)</td></tr><tr><td> $Log(ReviewVolume_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-0.06***</td><td>(0.01)</td><td></td><td></td><td>-0.13***</td><td>(0.03)</td></tr><tr><td> $Log(HighReview_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.03</td><td>(0.01)</td><td></td><td></td><td>0.12***</td><td>(0.02)</td></tr><tr><td> $Log(NegativeComments_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.27</td><td>(0.27)</td><td></td><td></td><td>0.14</td><td>(0.56)</td></tr><tr><td> $Log(CommentVolume_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-0.09</td><td>(0.07)</td><td></td><td></td><td>0.01</td><td>(0.11)</td></tr><tr><td> $Log(HighComments_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-0.03</td><td>(0.06)</td><td></td><td></td><td>-0.06</td><td>(0.10)</td></tr><tr><td> $Log(NegativeReview_{i,t-1})$ </td><td>-0.02**</td><td>(0.01)</td><td>-0.02*</td><td>(0.01)</td><td>-0.05***</td><td>(0.01)</td><td>-0.06***</td><td>(0.01)</td></tr><tr><td> $Log(ReviewVolume_{i,t-1})$ </td><td>0.12***</td><td>(0.01)</td><td>0.15***</td><td>(0.01)</td><td>0.22***</td><td>(0.01)</td><td>0.28***</td><td>(0.02)</td></tr><tr><td> $Log(HighReview_{i,t-1})$ </td><td>-0.07***</td><td>(0.01)</td><td>-0.08***</td><td>(0.01)</td><td>-0.19***</td><td>(0.01)</td><td>-0.24***</td><td>(0.02)</td></tr><tr><td> $Log(NegativeComments_{i,t-1})$ </td><td>-0.09</td><td>(0.09)</td><td>-0.35</td><td>(0.26)</td><td>-0.03</td><td>(0.18)</td><td>-0.19</td><td>(0.53)</td></tr><tr><td> $Log(CommentVolume_{i,t-1})$ </td><td>0.13***</td><td>(0.03)</td><td>0.19***</td><td>(0.05)</td><td>0.32***</td><td>(0.05)</td><td>0.31***</td><td>(0.09)</td></tr><tr><td> $Log(HighComments_{i,t-1})$ </td><td>-0.10***</td><td>(0.03)</td><td>-0.09</td><td>(0.05)</td><td>-0.19***</td><td>(0.05)</td><td>-0.16*</td><td>(0.08)</td></tr><tr><td> $Log(SelfNegativeReview_{i,j,t-1}) \times Gua$ </td><td></td><td></td><td>0.00</td><td>(0.01)</td><td></td><td></td><td>0.01</td><td>(0.01)</td></tr><tr><td> $Log(SelfReviewVolume_{i,j,t-1}) \times Gua$ </td><td></td><td></td><td>0.01</td><td>(0.01)</td><td></td><td></td><td>0.02*</td><td>(0.01)</td></tr><tr><td> $Log(SelfHighVolume_{i,j,t-1}) \times Gua$ </td><td></td><td></td><td>-0.03</td><td>(0.01)</td><td></td><td></td><td>-0.07***</td><td>(0.01)</td></tr><tr><td> $Log(Entries_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.05***</td><td>(0.01)</td><td></td><td></td><td>0.04</td><td>(0.02)</td></tr><tr><td> $Log(SelfNegativeReview_{i,j,t-1})$ </td><td>-0.02***</td><td>(0.00)</td><td>-0.02**</td><td>(0.01)</td><td>-0.04***</td><td>(0.01)</td><td>-0.04***</td><td>(0.01)</td></tr><tr><td> $Log(SelfReviewVolume_{i,j,t-1})$ </td><td>0.02***</td><td>(0.00)</td><td>0.02***</td><td>(0.01)</td><td>0.08***</td><td>(0.00)</td><td>0.08***</td><td>(0.01)</td></tr><tr><td> $Log(SelfHighVolume_{i,j,t-1})$ </td><td>0.09***</td><td>(0.01)</td><td>0.10***</td><td>(0.01)</td><td>0.09***</td><td>(0.01)</td><td>0.13***</td><td>(0.01)</td></tr><tr><td> $Log(Entries_{i,t-1})$ </td><td>-0.47***</td><td>(0.01)</td><td>-0.49***</td><td>(0.01)</td><td>-0.63***</td><td>(0.02)</td><td>-0.65***</td><td>(0.02)</td></tr><tr><td> $Log(NewContests_{i,t})$ </td><td>-0.01*</td><td>(0.00)</td><td>-0.01*</td><td>(0.00)</td><td>-0.03***</td><td>(0.01)</td><td>-0.03***</td><td>(0.01)</td></tr><tr><td>Individual-level fixed effects</td><td colspan="4">Yes</td><td colspan="4">No</td></tr><tr><td>Contest-level fixed effects</td><td colspan="4">Yes</td><td colspan="4">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="4">Yes</td><td colspan="4">Yes</td></tr><tr><td>Observations</td><td colspan="4">132,575</td><td colspan="4">132,575</td></tr><tr><td> $R^2$  or pseudo  $R^2$ </td><td colspan="2">0.0723</td><td colspan="2">0.0728</td><td colspan="2">0.0400</td><td colspan="2">0.0401</td></tr><tr><td>AIC</td><td colspan="2">334,692</td><td colspan="2">334,661</td><td colspan="2">270,417</td><td colspan="2">270,365</td></tr><tr><td>BIC</td><td colspan="2">345,006.10</td><td colspan="2">345,073</td><td colspan="2">280,760</td><td colspan="2">280,806</td></tr></table>

Robust standard errors are in parentheses. Dataset contains 1,031 contests and 5,545 contestants. “Gua” is short for Guarantee. For Wald Chi<sup>2</sup> tests, the degrees of freedom are reported in parentheses. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1 , ^ { \star \star } \mathsf { p } < 0 . 0 1 , ^ { \star } \mathsf { p } < 0 . 0 5 .$

## Appendix I

## Alternative DV: Number of New Contestants Entering Contest i in Period t

In our main results we focused on the number of new submissions as our dependent variable. An alternative measure of participation is the number of participants. It is important to test our model with this alternative dependent variable, for at least two reasons. First, it would potentially rule out an alternative hypothesis that in-process feedback led to more submissions simply because it encouraged more repeated submissions by the current participants (perhaps the direct receivers of the feedback), but not because it attracted more new participants. Second, the number of participants is of theoretical interest because in creative-design contests more participants might lead to more innovative ideas.

We retested our hypotheses by replacing the DV with Contestants (the total number of contestants) in the cross-sectional analysis and with NewContestants<sub>i,t</sub> (the number of participants who made their first submissions to contest i during period t) in the panel analysis. Contestants has a mean of 18.25 and a standard deviation of 25.77 and NewContestants has a mean of 1.84 and a standard deviation of 4.30.

To test the effect of Guarantee, we again report results from five estimates of treatment effects (i.e., PSM, NNM, RA, IPW, and IPWRA). Since the first stages (e.g., computing the propensity score or matching) were exactly the same as those used in the main model, their results as well as balance examinations are omitted. Treatment effects estimated across the five methods (Table I1) show that Guarantee had a positive effect on Contestants . The ATETs were estimated to range from 12.24 to 14.45.

<table><tr><td colspan="3">Table I1. Treatment Effects of Guarantee on Total Contestantsi</td></tr><tr><td></td><td>Estimated ATET</td><td>Observations</td></tr><tr><td>Propensity Score Matching (PSM)</td><td>12.62***(2.23)</td><td>644 treated and control</td></tr><tr><td>Nearest Neighbor Matching (NNM)</td><td>14.45***(1.94)</td><td>644 treated and control</td></tr><tr><td>Regression Adjustment (RA)</td><td>12.46***(1.96)</td><td>1,031</td></tr><tr><td>Inverse-Probability Weighting (IPW)</td><td>12.68***(1.96)</td><td>1,031</td></tr><tr><td>IPW Regression Adjustment (IPWRA)</td><td>12.24***(1.91)</td><td>1,031</td></tr></table>

Robust standard errors are in parentheses and for both PSM and NNM, robust Abadie-Imbens<sup>1</sup> standard errors are reported. For both PSM and NNM, the matching ratio was 1:1. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05.

Results about the main effects of in-process feedback (reported in Table I2) are largely consistent with results from our main model, with a few losing statistical significance. While our main model has yielded support for all the main effects (H2a–H4b), with NewContestants , H3a (effect of negative reviews), H3b (effect of negative comments), and H4b (effect of high comments), have lost support. For hypotheses regarding the interaction effects, the main model has yielded support for the following four hypotheses: H5a (effect of review volume moderated), H5b (effect of comment volume moderated), H7a (effect of high reviews moderated), and H7b (effect of high comments moderated). With this alternative DV (see AMEs reported in Table I3), all four coefficients have the correct signs, and H5a and H7a were supported (the coefficient supporting H7a was marginally significant).

Overall, the results predicting the number of new participants do not differ substantially with those predicting the number of new entries. The effect of Guarantee (H1) and the main effects of the review volume (H2a), comment volume (H2b), and high reviews (H4a) still hold. Two important interaction effects also hold, including the effect of review volume moderated (H5a) and the effect of high reviews moderated (H7a).

<table><tr><td colspan="5">Table I2. Unconditional Negative Binomial Model with FE as Dummies, Predicting the Number of New Contestants Who Entered Contest i During Period t</td></tr><tr><td rowspan="3"></td><td colspan="4">DV = NewContestantsi,t</td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.07*</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.11**</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.13**</td><td>(0.05)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-0.42</td><td>(6.59)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.26*</td><td>(0.11)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.33*</td><td>(0.14)</td></tr><tr><td>Log(Contestantsi,t-1) × Gua</td><td></td><td></td><td>0.23***</td><td>(0.05)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>0.04*</td><td>(0.02)</td><td>0.00</td><td>(0.02)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.04*</td><td>(0.02)</td><td>0.09***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.30***</td><td>(0.02)</td><td>-0.39***</td><td>(0.03)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-0.44</td><td>(0.57)</td><td>-0.25</td><td>(6.48)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.13**</td><td>(0.05)</td><td>0.22*</td><td>(0.10)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.16</td><td>(0.08)</td><td>-0.34**</td><td>(0.10)</td></tr><tr><td>Log(Contestantsi,t-1)</td><td>-0.22***</td><td>(0.05)</td><td>-0.34***</td><td>(0.04)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>0.02</td><td>(0.04)</td><td>0.05</td><td>(0.05)</td></tr><tr><td>Log(NewContestsi,t)</td><td>0.02*</td><td>(0.01)</td><td>0.02</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.29</td><td colspan="2">0.29</td></tr><tr><td>LL</td><td colspan="2">-20,135.14</td><td colspan="2">-24,852.01</td></tr><tr><td>AIC</td><td colspan="2">40,332.29</td><td colspan="2">40,216.32</td></tr><tr><td>BIC</td><td colspan="2">40,565.49</td><td colspan="2">40,359.25</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the overdispersion parameter. “Gua” is for Guarantee. $\star \star \star _ { \mathsf { p } } < 0 . 0 0 1$ ${ \star } { \star } _ { \mathsf { p } } < 0 . 0 1$ , \*p < 0.05.

Table 20. Average Marginal Effects of In-Process Feedback on NewContestants<sub>i,t</sub>

<table><tr><td rowspan="2"></td><td colspan="6">Average Marginal Effects of Feedback on NewContestants $_{i,t}$ </td></tr><tr><td colspan="2">Guarantee = 1</td><td colspan="2">Guarantee = 0</td><td colspan="2">Difference</td></tr><tr><td>Log(NegativeReview $_{i,t-1}$ )</td><td>0.21</td><td>(0.14)</td><td>0.00</td><td>(0.06)</td><td>0.21</td><td>(0.14)</td></tr><tr><td>Log(ReviewVolume $_{i,t-1}$ )</td><td>-0.07</td><td>(0.11)</td><td>0.26*</td><td>(0.11)</td><td>-0.33*</td><td>(0.17)</td></tr><tr><td>Log(HighReview $_{i,t-1}$ )</td><td>-0.79***</td><td>(0.39)</td><td>-1.14*</td><td>(0.50)</td><td>0.36+</td><td>(0.19)</td></tr><tr><td>Log(NegativeComments $_{i,t-1}$ )</td><td>-2.00</td><td>(1.39)</td><td>-0.72</td><td>(18.96)</td><td>-1.28</td><td>(19.43)</td></tr><tr><td>Log(CommentVolume $_{i,t-1}$ )</td><td>-0.11</td><td>(0.19)</td><td>0.64</td><td>(0.47)</td><td>-0.75</td><td>(0.56)</td></tr><tr><td>Log(HighComments $_{i,t-1}$ )</td><td>-0.01</td><td>(0.20)</td><td>-0.98</td><td>(0.61)</td><td>0.97</td><td>(0.62)</td></tr></table>

Average marginal effects calculated as the mean marginal effects evaluated at the variables’ values in the sample. Standard errors derived with the delta-method are reported in parentheses. ${ } ^ { \star \star \star } p < 0 . 0 0 1 , { } ^ { \star \star } p < 0 . 0 1 , { } ^ { \star } p < 0 . 0 5 , { } ^ { + } p < 0 . 1 0 .$

## Appendix J

## Code for Matching and Computing the Instrument Variables

```python
# coding: utf-8
import os
from datetime import datetime
import pandas as pd
import numpy as np
import csv
from operator import itemgetter

N_NEIGHBOR = 30

def compute_similarity_rated(contestid1, contestid2, day):
    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict[contestid2]['guaranteed']))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])

    simscore = gua_diff+prize_diff + weekend_diff + contestsheld_diff+averagefb_diff + daytime_diff
    return simscore

def compute_similarity_high(contestid1, contestid2, day):
    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict['guaranteed']))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])

    simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff
    return simscore

def compute_similarity_elim(contestid1, contestid2, day):
    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
```

```python
if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict[contestid2]['guaranteed']))*100
prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend']))*100
daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])

simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff
return simscore

def compute_similarity_comm(contestid1, contestid2, day):

    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict[contestid2]['guaranteed']))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback']])
    comm_diff = (abs(contestday_dict[contestid1]['evercomm'] - contestday_dict[contestid2]['evercomm']))*100

    simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff+comm_diff
return simscore

def compute_similarity_negcomm(contestid1, contestid2, day):

    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict{contestid2}[ˈguaranteed]))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict{contestid2}[day['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict{contestid2}[day['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict{contestid2}[ˈaverageFeedback'])
    comm_diff = (abs(contestday_dict[contestid1]['everncomm'] - contestday_dict{contestid2}[ˈeverncomm']))*100

    simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff+comm_diff
return simscore

def compute_similarity_highcomm(contestid1, contestid2, day):

    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday-dict[contestid2]['guaranteed']))*100
```

```python
prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize'])) / 10
weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend'])) * 100
daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime'])) * 100
contestsheld_diff = (abs(contest1_exp - contest2_exp)) * 100
averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])) 
comm_diff = (abs(contestday_dict[contestid1]['everhcomm'] - contestday_dict[contestid2]['everhcomm'])) * 100

simscore = gua_diff + prize_diff + weekend_diff + daytime_diff + contestsheld_diff + averagefb_diff + comm_diff
return simscore

def match_two_rows_rated(contestid1, contestid2, day):

    simscore = -1

    row = contestday_dict[contestid1]
    x = contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1

    if abs(row['delay'] - x['delay']) == 0:
    simscore = compute_similarity_rated(contestid1, contestid2, day)

    return simscore

def match_two_rows_high(contestid1, contestid2, day):

    simscore = -1

    row = contestday_dict[contestid1]
    x = contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1
    if contestday_dict[contestid2][day]['cumRated2Ystd'] == 0: return -1

    if abs(row['delay'] - x['delay']) == 0:
    simscore = compute_similarity_high(contestid1, contestid2, day)
    return simscore

def match_two_rows_elim(contestid1, contestid2, day):

    simscore = -1

    row = contestday_dict[contestid1]
    x = contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1
    if contestday_dict[contestid2][day]['cumRated2Ystd'] == 0: return -1

    if abs(row['delay'] - x['delay']) == 0: 
    simscore = compute_similarity_elim(contestid1, contestid2, day)

    return simscore

def match_two_rows_comm(contestid1, contestid2, day):
```

```python
simscore = -1

row=contestday_dict[contestid1]
x=contestday_dict[contestid2]

if (day not in contestday_dict[contestid2]): return -1

if row['evercomm'] == x['evercomm']:
    simscore = compute_similarity_comm(contestid1, contestid2, day)

return simscore

def match_two_rows_negcomm(contestid1, contestid2, day):

    simscore = -1

    row=contestday_dict[contestid1]
    x=contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1

    if row['evercomm'] == x['evercomm']:
    simscore = compute_similarity_negcomm(contestid1, contestid2, day)

    return simscore

def match_two_rows_highcomm(contestid1, contestid2, day):

    simscore = -1

    row=contestday_dict[contestid1]
    x=contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1

    if row['evercomm'] == x['evercomm']:
    simscore = compute_similarity_highcomm(contestid1, contestid2, day)

    return simscore

def find_sim_cases_rated(contestid, day):

    similarcases={'cumSimRatedYstd':0,'simcount':0}

    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = match_two_rows_rated(contestid1, contestid2, day)
```

```python
if simscore >= 0:
    cumSimRatedYstd = contestday_dict[contestid2][day]['cumRated2Ystd']
    cases_matched.append([simscore, cumSimRatedYstd])

# Pick the N nearest neighbors
cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimRatedYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)
return similarcases

def find_sim_cases_high(contestid, day):
    similarcases={'cumSimHighYstd_prop':0,'simcount':0}
    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = -1
    simscore = match_two_rows_high(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimHighYstd_prop=
    contestday_dict[contestid2][day]['cumHigh2Ystd]/contestday_dict[contestid2][day]['cumRated2Ystd']
    cases_matched.append([simscore, cumSimHighYstd_prop])

    # Pick the N nearest neighbors
    cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

    num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
    if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimHighYstd_prop'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

return similarcases
```

```python
def find_sim_cases_elim(contestid, day):
    similarcases = {'cumSimElimYstd_prop':0,'simcount':0}
    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = match_two_rows_elim(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimElimYstd_prop=
    contestday_dict[contestid2][day]['cumElim2Ystd]/contestday_dict[contestid2][day]['cumRated2Ystd']
    cases_matched.append([simscore, cumSimElimYstd_prop])

    # Pick the N nearest neighbors
    cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

    num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
    if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimElimYstd_prop'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

    return similarcases

def find_sim_cases_comm(contestid, day):
    similarcases = {'cumSimCommentsYstd':0,'simcount':0}
    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = match_two_rows_comm(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimCommYstd = contestday_dict[contestid2][day]['cumHolderCommentsYstd']
    cases_matched.append([simscore, cumSimCommYstd])

# Pick the N nearest neighbors
```

```python
cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimCommentsYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

return similarcases

def find_sim_cases_negcomm(contestid, day):

    similarcases = {'cumSimNegCommYstd':0,'simcount':0}

    cases_matched = []

    for key in contestday_dict:

    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue

    simscore = match_two_rows_negcomm(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimNegCommYstd = contestday_dict[contestid2][day]['cumNegCommYstd']
    cases_matched.append([simscore, cumSimNegCommYstd])

    # Pick the N nearest neighbors
    cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

    num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
    if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimNegCommYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

    return similarcases

def find_sim_cases_highcomm(contestid, day):

    similarcases = {'cumSimHighCommYstd':0,'simcount':0}

    cases_matched = []
```

```python
for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue

    simscore = match_two_rows_highcomm(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimHighCommYstd = contestday_dict[contestid2][day]['cumHighCommYstd']
    cases_matched.append([simscore, cumSimHighCommYstd])

# Pick the N nearest neighbors
cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimHighCommYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

return similarcases

def match_rated(row):
    contestid = row['contestID']
day = row['day']

    similarcases={}\ 
    row['cumSimRatedYstd'] = 0
row['simcount'] = 0

    similarcases=find_sim_cases_rated(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimRatedYstd'] = similarcases['cumSimRatedYstd']
    row['simcount'] = similarcases['simcount']
return row

def match_high(row):
    contestid = row['contestID']
day = row['day']

    similarcases={}\ 
    row['cumSimHighYstd'] = 0
```

```python
row['simcount'] = 0

similarcases=find_sim_cases_high(contestid, day)

if similarcases['simcount'] > 0:
    row['cumSimHighYstd'] = similarcases['cumSimHighYstd_prop'] * row['cumrated2ystd']
    row['simcount'] = similarcases['simcount']

return row

def match_elim(row):
    contestid = row['contestID']
    day = row['day']

    similarcases = {}
    row['cumSimElimYstd'] = 0
    row['simcount'] = 0

    similarcases=find_sim_cases_elim(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimElimYstd'] = similarcases['cumSimElimYstd_prop'] * row['cumrated2ystd']
    row['simcount'] = similarcases['simcount']

    return row

def match_comm(row):
    contestid = row['contestID']
    day = row['day']

    similarcases = {}
    row['cumSimCommentsYstd'] = 0
    row['simcount'] = 0

    similarcases=find_sim_cases_comm(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimCommentsYstd'] = similarcases['cumSimCommentsYstd']
    row['simcount'] = similarcases['simcount']

    return row

def match_negcomm(row):
    contestid = row['contestID']
    day = row['day']

    similarcases = {}
    row['cumSimNegCommYstd'] = 0
    row['simcount'] = 0
```

```python
if row['cumholdercommentsystd'] == 0:
    return row

similarcases=find_sim_cases_negcomm(contestid, day)

if similarcases['simcount'] > 0:
    row['cumSimNegCommYstd'] = similarcases['cumSimNegCommYstd']
    row['simcount'] = similarcases['simcount']

return row

def match_highcomm(row):

    contestid = row['contestID']
    day = row['day']

    similarcases = {}

    row['cumSimHighCommYstd'] = 0
    row['simcount'] = 0

    if row['cumholdercommentsystd'] == 0:
    return row

    similarcases=find_sim_cases_highcomm(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimHighCommYstd'] = similarcases['cumSimHighCommYstd']
    row['simcount'] = similarcases['simcount']

    return row
```

## References

Abadie, A.,and Imbens, G. W. 2006. “Large Sample Properties of Matching Estimators for Average Treatment Effects,” Econometrica (74:1), pp. 235-267.

Abadie, A.,and Imbens, G. W. 2011. “Bias-Corrected Matching Estimators for Average Treatment Effects,” Journal of Business and Economic Statistics (29:1), pp. 1-11.

Abadie, A.,and Imbens, G. W. 2016. “Matching on the Estimated Propensity Score,” Econometrica (84:2), pp. 781-807.

Jiang, Z. Z., Huang, Y., and Beil, D. R. 2016. “The Role of Feedback in Dynamic Crowdsourcing Contests: A Structural Empirical Analysis,” Ross School of Business Paper No. 1334, University of Michigan.

Wooten, J. O., and Ulrich, K. T. 2016. “Idea Generation and the Role of Feedback: Evidence from Field Experiments with Innovation Tournaments,” Production and Operations Management (26:1), pp. 80-99.

Yang, Y., Chen, P.-Y., and Pavlou, P. A. 2013. “Managing Open Innovation Contests in Online Market,” Working Paper, Temple University, Philadelphia, PA.

# MANAGING THE CROWDS: THE EFFECT OF PRIZE GUARANTEES AND IN-PROCESS FEEDBACK ON PARTICIPATION IN CROWDSOURCING CONTESTS

Lian Jian Annenberg School of Communication, University of Southern California, Los Angeles, CA 90089 U.S.A. {ljian@usc.edu}

Sha Yang Marshall School of Business, University of Southern California, Los Angeles, CA 90089 U.S.A. {shayang@marshall.usc.edu}

Sulin Ba School of Business, University of Connecticut, Storrs, CT 06268 U.S.A. {sulin.ba@uconn.edu}

Li Lu College of Business & Public Management, West Chester University, West Chester, PA 19383 U.S.A. {llu@wcupa.edu}

Li Crystal Jiang Department of Media and Communication, City University of Hong Kong, Hong Kong, CHINA {crystal.jiang@cityu.edu.hk}

## Appendix A

## Study Site Description

![](/api/attachments/NNUSRDKN/fulltext/images/7657a12cca1f4316472d08a0b6ffe9e68adcb655b8143d207e495adb1b2b39c6.jpg)

Figure A1. Timeline of a Typical Contest

<table><tr><td>Contest Title</td><td>Contest Holder</td><td>Ends</td><td>Entries</td><td>Package</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #1A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #1</td><td>14 hours</td><td>58</td><td>bronzeAU$299</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #2A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #2</td><td>15 hours</td><td>99</td><td>bronzeCA$299</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #3A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #3</td><td>15 hours</td><td>52</td><td>bronze$299guaranteed</td></tr><tr><td colspan="5"></td></tr><tr><td>Title of Contest #4A short description of the business, including its mission statement and its main products or services.</td><td>Screen name #4</td><td>16 hours</td><td>151</td><td>bronze$299</td></tr></table>

As of May 2016, the site we study has hosted more than 350,000 contests and paid more than \$100 million to participants. At the time of our data collection in June 2011, 125,527 users were registered on the platform, and more than 6 million designs had been submitted. On this site, a typical contest goes through three stages (see Figure A1): before, during, and after the contest. As soon as a contest is launched, any visitor to the site can discover it by clicking the “browse projects” link on the front page. All projects at various stages are shown on this page (see Figure A2), including the title of the task, the name of the contest host, the time left, the number of entries received, and the prize amount. If a contest’s prize is guaranteed, the word “guaranteed” appears under the prize amount. A visitor can sort the contests by the last three columns (i.e., the time left on the contest, the number of entries received, and the prize amount).

By default, the contests are sorted such that those closing the soonest appear on the top. During a contest, all the existing entries are displayed in descending order of their ratings (see Figure A3). Underneath the design, the entry number (indicating the order in which it was submitted), the screen name of the contestant, and the rating it received (if any) are displayed

## Appendix B

## Robustness Test of Using the Cumulative Number of Entries by Period t-1 as the Control Variable for the Current Level of Participation

The results of replacing the control variable Log(Contestants ) with $L o g ( E n t r i e s _ { i , t - 1 } )$ reported in Table B1. All the estimated coefficients are similar to those reported in Table 7 in their signs, magnitude, and statistical significance, except that the coefficient on Log(NegativeReview<sub>i,t-1</sub>) × Gua has become statistically significant while it was not in the main model in Table 7, thus providing support for H7a (effect of negative reviews moderated).

<table><tr><td rowspan="3"></td><td colspan="4">DV = NewEntriesi,t</td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.07*</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.13**</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.10*</td><td>(0.04)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-1.20</td><td>(0.76)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.29***</td><td>(0.08)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.31*</td><td>(0.14)</td></tr><tr><td>Log(Entriesi,t-1) × Gua</td><td></td><td></td><td>0.18***</td><td>(0.04)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>-0.05***</td><td>(0.01)</td><td>-0.08***</td><td>(0.02)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.21***</td><td>(0.02)</td><td>0.25***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.30***</td><td>(0.02)</td><td>-0.36***</td><td>(0.03)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-0.94*</td><td>(0.43)</td><td>-0.08</td><td>(0.79)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.27***</td><td>(0.04)</td><td>0.36***</td><td>(0.06)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.20**</td><td>(0.07)</td><td>-0.34***</td><td>(0.09)</td></tr><tr><td>Log(Entriesi,t-1)</td><td>-0.16***</td><td>(0.03)</td><td>-0.24***</td><td>(0.04)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>0.05</td><td>(0.04)</td><td>0.08</td><td>(0.04)</td></tr><tr><td>Log(NewContestsi,t)</td><td>0.02</td><td>(0.01)</td><td>0.01</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.68</td><td colspan="2">0.67</td></tr><tr><td>LL</td><td colspan="2">-32,602.40</td><td colspan="2">-32,568.30</td></tr><tr><td>AIC</td><td colspan="2">65,250.81</td><td colspan="2">65,182.61</td></tr><tr><td>BIC</td><td colspan="2">65,423.82</td><td colspan="2">65,356.63</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the overdispersion parameter. “Gua” is short for Guarantee. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1 , ^ { \star \star } \mathsf { p } < 0 . 0 1$ ${ \star } _ { \mathsf { p } } < 0 . 0 5$

## Appendix C

Robustness Test of Dropping the Last Period  
![](/api/attachments/NNUSRDKN/fulltext/images/268bdb356ee1d82b047b6bd67adc827dde49d8bb16842b57ee82056fc6b6340a.jpg)  
Figure C1. The Number of New Entries Submitted During Each Period

Figure C1 plots the mean number of new submissions by period. Because a spike was observed in the last period, a robustness check was conducted by dropping the last period in the panel. Our analyses show that dropping the last period does not change our results qualitatively. The estimated coefficients as reported in Table C1 are similar to those produced by the main model (in Table 7) in terms of their signs, magnitude, and statistical significance, except that the interaction effect $L o g ( H i g h R e \nu i e w _ { i , t - 1 } ) $ × Gua has become marginally significant $\left( p = \right.$ 0.06).

<table><tr><td colspan="5">Table C1. Unconditional Negative Binomial Model with FE as Dummies Predicting the Number of New Entries During Period t in Contest i</td></tr><tr><td rowspan="3"></td><td colspan="4">DV = NewEntriesi,t</td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.06</td><td>(0.04)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.10*</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.09+</td><td>(0.05)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-1.53</td><td>(0.99)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.30**</td><td>(0.11)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.38*</td><td>(0.16)</td></tr><tr><td>Log(Entriesi,t-1) × Gua</td><td></td><td></td><td>0.24***</td><td>(0.05)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>-0.05*</td><td>(0.02)</td><td>-0.08**</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.12***</td><td>(0.03)</td><td>0.15***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.20***</td><td>(0.02)</td><td>-0.25***</td><td>(0.03)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-1.07**</td><td>(0.36)</td><td>0.01</td><td>(0.83)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.26***</td><td>(0.05)</td><td>0.37***</td><td>(0.08)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.18*</td><td>(0.08)</td><td>-0.37**</td><td>(0.12)</td></tr><tr><td>Log(Entriesi,t-1)</td><td>0.09</td><td>(0.06)</td><td>-0.03</td><td>(0.07)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>-0.12*</td><td>(0.05)</td><td>-0.09</td><td>(0.06)</td></tr><tr><td>Log(NewContestsi,t)</td><td>0.04**</td><td>(0.01)</td><td>0.03*</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">12,634</td><td colspan="2">12,634</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.68</td><td colspan="2">0.68</td></tr><tr><td>LL</td><td colspan="2">-28,355.70</td><td colspan="2">-28,322.07</td></tr><tr><td>AIC</td><td colspan="2">56,771.40</td><td colspan="2">56,704.13</td></tr><tr><td>BIC</td><td colspan="2">56,994.73</td><td colspan="2">56,927.46</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the over-dispersion parameter. “Gua” is short for Guarantee. $^ { \star \star \star } \mathsf { p } { < } 0 . 0 0 1 , ^ { \star \star } \mathsf { p } { < } 0 . 0 1$ ${ } ^ { \star } { \mathsf p } { < } 0 . 0 5 , { } + { \mathsf p } { < } 0 . 1$

## Appendix D

## Propensity Score Matching Diagnosis

Figure D1 demonstrates that the distributions of propensity scores among contests with and without guarantees exhibit substantial overlap, indicating sufficient matching.

![](/api/attachments/NNUSRDKN/fulltext/images/d503c3a30e56800ac8d7cf64d01cd795a221950109ed5e9f2a7f7c3bee3e2894.jpg)

Figure D1. Distribution of Propensity Scores Among Contests With and Without Prize Guarantees

## Appendix E

## Instrument Variable Analyses

Descriptive statistics of the instrument variables are reported in Table E1 and the first stage regression results are reported in Table E2.

<table><tr><td colspan="6">Table E1. Descriptive Statistics of Instrumental Variables</td></tr><tr><td>Variable</td><td>N</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td> $SimNegativeReview_{i,t-1}$ </td><td>13,665</td><td>4.25</td><td>12.89</td><td>0</td><td>479.14</td></tr><tr><td> $SimReviewVolume_{i,t-1}$ </td><td>13,665</td><td>11.85</td><td>13.99</td><td>0</td><td>94.17</td></tr><tr><td> $SimHighReview_{i,t-1}$ </td><td>13,665</td><td>2.13</td><td>6.31</td><td>0</td><td>277.11</td></tr><tr><td> $SimNegativeComments_{i,t-1}$ </td><td>13,665</td><td>0.0001</td><td>0.002</td><td>0</td><td>0.07</td></tr><tr><td> $SimCommentVolume_{i,t-1}$ </td><td>13,665</td><td>0.58</td><td>0.82</td><td>0</td><td>3.43</td></tr><tr><td> $SimHighComments_{i,t-1}$ </td><td>13,665</td><td>0.11</td><td>0.34</td><td>0</td><td>2.2</td></tr></table>

Table E2. First Stage Regression Results

<table><tr><td>DV</td><td colspan="2"> $Log(NegReview_{i,t-1})$ </td><td colspan="2"> $Log(ReviewVol_{i,t-1})$ </td><td colspan="2"> $Log(HighReview_{i,t-1})$ </td><td colspan="2"> $Log(NegComm_{i,t-1})$ </td><td colspan="2"> $Log(CommVol_{i,t-1})$ </td><td colspan="2"> $Log(HighComm_{i,t-1})$ </td></tr><tr><td> $Log(SimNegReview_{i,t-1})$ </td><td>0.35***</td><td>(0.02)</td><td>0.63***</td><td>(.01)</td><td>0.45***</td><td>(0.02)</td><td>0.00</td><td>(.00)</td><td>0.05**</td><td>(0.02)</td><td>0.00</td><td>(.01)</td></tr><tr><td> $Log(SimReviewVol_{i,t-1})$ </td><td>-0.06***</td><td>(0.01)</td><td>0.26***</td><td>(.00)</td><td>-0.04***</td><td>(0.01)</td><td>0.00*</td><td>(.00)</td><td>-0.04***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td></tr><tr><td> $Log(SimHighReview_{i,t-1})$ </td><td>0.39***</td><td>(0.02)</td><td>0.15***</td><td>(.01)</td><td>0.31***</td><td>(0.02)</td><td>0.00</td><td>(.00)</td><td>0.10***</td><td>(0.02)</td><td>0.01*</td><td>(.01)</td></tr><tr><td> $Log(SimNegComm_{i,t-1})$ </td><td>-2.80</td><td>(2.48)</td><td>-2.10*</td><td>(.87)</td><td>1.78</td><td>(2.45)</td><td>1.93***</td><td>(.10)</td><td>12.02***</td><td>(2.00)</td><td>-0.50</td><td>(.59)</td></tr><tr><td> $Log(SimCommVol_{i,t-1})$ </td><td>-0.02*</td><td>(0.01)</td><td>-0.03***</td><td>(.00)</td><td>0.13***</td><td>(0.01)</td><td>0.00*</td><td>(.00)</td><td>0.34***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td></tr><tr><td> $Log(SimHighComm_{i,t-1})$ </td><td>-0.01</td><td>(0.03)</td><td>-0.02</td><td>(.01)</td><td>0.21***</td><td>(0.03)</td><td>0.00</td><td>(.00)</td><td>1.81***</td><td>(0.03)</td><td>0.93***</td><td>(.01)</td></tr><tr><td> $Log(Contestants_{i,t-1})$ </td><td>0.12***</td><td>(0.01)</td><td>0.11***</td><td>(.00)</td><td>-0.13***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td><td>0.06***</td><td>(0.01)</td><td>-0.01</td><td>(.00)</td></tr><tr><td> $Log(MedianSubmn_{i,t-1})$ </td><td>-0.04***</td><td>(0.01)</td><td>0.03***</td><td>(.00)</td><td>0.06***</td><td>(0.01)</td><td>0.00</td><td>(.00)</td><td>0.06***</td><td>(0.01)</td><td>0.01***</td><td>(.00)</td></tr><tr><td> $Log(NewContests_{i,t})$ </td><td>-0.01</td><td>(0.01)</td><td>-0.01*</td><td>(.00)</td><td>-0.02**</td><td>(0.01)</td><td>0.00</td><td>(.00)</td><td>-0.02**</td><td>(0.01)</td><td>0.00</td><td>(.00)</td></tr><tr><td>Contest-level FE</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td> $R^2$ </td><td colspan="2">0.49</td><td colspan="2">0.96</td><td colspan="2">0.55</td><td colspan="2">0.07</td><td colspan="2">0.58</td><td colspan="2">0.65</td></tr></table>

Standard errors in parentheses. Due to space limitations, abbreviations are used, including “Neg” = Negative; “Comm” = Comment or Comments; “Vol” = Volume. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

## Appendix F

## Robustness Test of Using Per-Period (i.e., Noncumulative) Independent Variables

We have added analyses by an alternative model in which the cumulative independent variables were replaced with per-period measures. In Table F1, we report results from an unconditional negative binomial model with fixed effects modeled as dummies. Overall, the results ar qualitatively similar to our main results. All the main effects of in-process feedback have retained their signs, magnitude, and statistical significance except for the coefficient on Log(NewNegativeComments ), which has retained the correct sign. The interaction effects have retained the expected signs but their statistical significance has changed. In particular, among the four moderating effects identified in the main model (Table 7), only the coefficient on Log(NewReviewVolume ) X Gua is still statistically significant. However, two other coefficients that were not statistically significant in the main model have become statistically significant: Log(NewNegativeReview ) × Gua and Log(NewNegativeComments ) × Gua. In summary, the results using per-period measures of independent variables are largely consistent with our main results.

<table><tr><td colspan="5">Table F1. Results of Robustness Tests Using Per-Period Independent Variables in an Unconditional Negative Binomial Model with FE as Dummies</td></tr><tr><td rowspan="3"></td><td colspan="4"> $DV = NewEntries_{i,t}$ </td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td> $\text{Log}(\text{NewNegativeReview}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.09***</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{NewReviewVolume}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>-0.09***</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{NewHighReview}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.06</td><td>(0.05)</td></tr><tr><td> $\text{Log}(\text{NewNegativeComments}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>29.00***</td><td>(1.72)</td></tr><tr><td> $\text{Log}(\text{NewCommentVolume}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>-0.10</td><td>(0.12)</td></tr><tr><td> $\text{Log}(\text{NewHighComments}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.22</td><td>(0.17)</td></tr><tr><td> $\text{Log}(\text{Contestants}_{i,t-1}) \times \text{Gua}$ </td><td></td><td></td><td>0.06*</td><td>(0.03)</td></tr><tr><td> $\text{Log}(\text{NewNegativeReview}_{i,t-1})$ </td><td>-0.07***</td><td>(0.02)</td><td>-0.12***</td><td>(0.02)</td></tr><tr><td> $\text{Log}(\text{NewReviewVolume}_{i,t-1})$ </td><td>0.22***</td><td>(0.02)</td><td>0.26***</td><td>(0.02)</td></tr><tr><td> $\text{Log}(\text{NewHighReview}_{i,t-1})$ </td><td>-0.16***</td><td>(0.02)</td><td>-0.19***</td><td>(0.04)</td></tr><tr><td> $\text{Log}(\text{NewNegativeComments}_{i,t-1})$ </td><td>-1.14</td><td>(0.85)</td><td>-29.90***</td><td>(2.02)</td></tr><tr><td> $\text{Log}(\text{NewCommentVolume}_{i,t-1})$ </td><td>0.33***</td><td>(0.05)</td><td>0.39***</td><td>(0.06)</td></tr><tr><td> $\text{Log}(\text{NewHighComments}_{i,t-1})$ </td><td>-0.20*</td><td>(0.10)</td><td>-0.31**</td><td>(0.12)</td></tr><tr><td> $\text{Log}(\text{Contestants}_{i,t-1})$ </td><td>0.10***</td><td>(0.03)</td><td>0.06</td><td>(0.09)</td></tr><tr><td> $\text{Log}(\text{MedianSubmn}_{i,t-1})$ </td><td>-0.14***</td><td>(0.03)</td><td>-0.13</td><td>(0.07)</td></tr><tr><td> $\text{Log}(\text{NewContests}_{i,t})$ </td><td>0.02**</td><td>(0.01)</td><td>0.02</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.66</td><td colspan="2">0.66</td></tr><tr><td>LL</td><td colspan="2">-32,545.46</td><td colspan="2">-32,536.65</td></tr><tr><td>AIC</td><td colspan="2">65,220.92</td><td colspan="2">65,095.30</td></tr><tr><td>BIC</td><td colspan="2">65,709.89</td><td colspan="2">65,178.05</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the over-dispersion parameter. “Gua” is short for Guarantee. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1 , ^ { \star \star } \mathsf { p } < 0 . 0 1$ ${ \star } _ { \mathsf { p } } < 0 . 0 5$

## Appendix G

## Robustness Test of Using Arellano-Bond Dynamic Panel-Data Estimator

The results of Arellano-Bond dynamic panel-data estimator with a lagged DV are reported in Table G1. All the coefficients reported in the main model (Table 7) have retained their signs, magnitude, and statistical significance, except the coefficient on Log(NegativeComments ) which has the expected sign but has lost its statistical significance.

<table><tr><td rowspan="3"></td><td colspan="4">DV = Log(NewEntriesi,t)</td></tr><tr><td colspan="4">Arellano-Bond Dynamic Panel-Data Estimator</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.12</td><td>(0.05)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.19*</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.08*</td><td>(0.06)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-3.20</td><td>(2.30)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.15**</td><td>(0.11)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.49*</td><td>(0.20)</td></tr><tr><td>Log(Contestantsi,t-1) × Gua</td><td></td><td></td><td>0.04**</td><td>(0.07)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>-0.22***</td><td>(0.03)</td><td>-0.26***</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.17***</td><td>(0.02)</td><td>0.24***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.50***</td><td>(0.03)</td><td>-0.52***</td><td>(0.04)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-3.81</td><td>(1.47)</td><td>-1.35</td><td>(0.58)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.18***</td><td>(0.05)</td><td>0.27***</td><td>(0.08)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.31*</td><td>(0.10)</td><td>-0.54**</td><td>(0.14)</td></tr><tr><td>Log(Contestantsi,t-1)</td><td>-0.61</td><td>(0.04)</td><td>-0.62*</td><td>(0.05)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>-0.21***</td><td>(0.03)</td><td>-0.22***</td><td>(0.03)</td></tr><tr><td>Log(NewContestsi,t)</td><td>-0.01</td><td>(0.01)</td><td>-0.01</td><td>(0.01)</td></tr><tr><td>Log(NewEntriesi,t-1)</td><td>0.09***</td><td>(0.02)</td><td>0.09***</td><td>(0.02)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period, day/night and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Wald  $\chi^2$ </td><td colspan="2">3810.55(24)</td><td colspan="2">3806.09(31)</td></tr></table>

Robust standard errors are in parentheses. “Gua” is short for Guarantee. For Wald $\chi ^ { 2 }$ tests, the degrees of freedom are reported in parentheses. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1$ $^ { \star \star } \mathsf { p } < 0 . 0 1$ ${ \star } _ { \mathsf { p } } < 0 . 0 5$

## Appendix H

## Contestant-Level Analysis

We conducted individual-level analysis to verify our main results obtained at the contest level. In this contest-contestant-period dataset, each observation focuses on the outcome variable, $n _ { i , j , t } ,$ , the number of submissions contestant j submits to contest i in period t. The dataset contain 1,031 contests and 5,545 contestants. An observation of contest i-contestant j-period t is included in the dataset only if contestant j has submitted at least an entry to contest i before or during period t. In-process feedback variables are added into the model together with thre sets of control variables, ContestantContro $l s _ { i , j , t - 1 } .$ , Contest $\mathrm { \gamma } _ { o n t r o l s _ { i , t - 1 } }$ , and $P e r i o d C o n t r o l s _ { i , t } ,$ as well as two fixed effects at the contest and contestant level respectively, $C _ { i }$ and $C _ { j } .$

$$
\begin{array}{r l} & {\log \left(n _ {i, j, t}\right) = \alpha_ {0} + \alpha_ {1} \log \left(N e g a t i v e R e v i e w _ {i, t - 1}\right) + \alpha_ {2} \log \left(R e v i e w V o l u m e _ {i, t - 1}\right)} \\ & {\qquad + \alpha_ {3} \log \left(H i g h R e v i e w _ {i, t - 1}\right) + \alpha_ {4} \log \left(N e g a t i v e C o m m e n t _ {i, t - 1}\right)} \\ & {\qquad + \alpha_ {5} \log \left(C o m m e n t R e v i e w _ {i, t - 1}\right) + \alpha_ {6} \log \left(H i g h C o m m e n t _ {i, t - 1}\right)} \\ & {\qquad + \alpha_ {7} C o n t e s t C o n t r o l s _ {i, t - 1} + \alpha_ {8} C o n t e s t a n t C o n t r o l s _ {i, t - 1}} \\ & {\qquad + \alpha_ {9} P e r i o d C o n t r o l s _ {i, t} + \delta_ {i} C _ {i} + \delta_ {j} C _ {j} + \varepsilon_ {i, j, t}} \end{array}\tag{3}
$$

The ContestControl $s _ { i , t - 1 }$ is a vector of contest-period specific variables, which includes only $E n t r i e s _ { i , t - 1 }$ (cumulative number of entries contest i receives by period t-1). $C o n t e s t a n t C o n t r o l s _ { i , j , t - 1 }$ includes three variables describing the cumulative reviews contestant j has received from contest i as of period t-1: SelfNegativeReview $\begin{array} { r } { \dot { \mathbf \Xi } _ { i , j , t - 1 } , } \end{array}$ SelfReview $V o l u m e _ { i , j , t - 1 } ,$ and $S e l f H i g h R e \nu i e w _ { i , j , t - 1 }$ These three variables were introduced because prior research has shown that direct feedback received by participants to their own submissions have strong effects on their subsequent submissions (Jiang et al. 2016; Wooten and Ulrich 2016; Yang et al. 2013). The PeriodControl is a vector of contest-period specific variables, which includes $W e e k e n d _ { i , t } , P e r i o d _ { t }$ , and NewContests . To examine the interaction effects, we add

$$
\alpha_ {k} = \alpha_ {k 0} + \alpha_ {k 1} G u a r a n t e e _ {i}\tag{4}
$$

where $\mathrm { k } = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 \}$ . That is, the first six independent variables in equation (3) are interacted with the variable Guarantee .

In Table H1, we report the results of contestant level analyses using two models: a linear model with both contest and contestant level fixed effects and an unconditional negative binomial model with contest-level fixed effects modeled as dummies. The results show that these two models yield results highly consistent in the sign and statistical significance of the coefficients. The results show that all our main results about in-process feedback are born out at the individual contestant level, except the main effect of negative comments (H3b), the effects of comment volume moderated (H5b) and high comments moderated (H7b).

<table><tr><td rowspan="3"></td><td colspan="4"> $DV = Log(NewEntries_{i,j,t})$ </td><td colspan="4"> $DV = NewEntries_{i,j,t}$ </td></tr><tr><td colspan="4">Linear</td><td colspan="4">Unconditional NB with FE as Dummies</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td><td colspan="2">Model (3)</td><td colspan="2">Model (4)</td></tr><tr><td> $Log(NegativeReview_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.00</td><td>(0.01)</td><td></td><td></td><td>0.01</td><td>(0.02)</td></tr><tr><td> $Log(ReviewVolume_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-0.06***</td><td>(0.01)</td><td></td><td></td><td>-0.13***</td><td>(0.03)</td></tr><tr><td> $Log(HighReview_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.03</td><td>(0.01)</td><td></td><td></td><td>0.12***</td><td>(0.02)</td></tr><tr><td> $Log(NegativeComments_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.27</td><td>(0.27)</td><td></td><td></td><td>0.14</td><td>(0.56)</td></tr><tr><td> $Log(CommentVolume_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-0.09</td><td>(0.07)</td><td></td><td></td><td>0.01</td><td>(0.11)</td></tr><tr><td> $Log(HighComments_{i,t-1}) \times Gua$ </td><td></td><td></td><td>-0.03</td><td>(0.06)</td><td></td><td></td><td>-0.06</td><td>(0.10)</td></tr><tr><td> $Log(NegativeReview_{i,t-1})$ </td><td>-0.02**</td><td>(0.01)</td><td>-0.02*</td><td>(0.01)</td><td>-0.05***</td><td>(0.01)</td><td>-0.06***</td><td>(0.01)</td></tr><tr><td> $Log(ReviewVolume_{i,t-1})$ </td><td>0.12***</td><td>(0.01)</td><td>0.15***</td><td>(0.01)</td><td>0.22***</td><td>(0.01)</td><td>0.28***</td><td>(0.02)</td></tr><tr><td> $Log(HighReview_{i,t-1})$ </td><td>-0.07***</td><td>(0.01)</td><td>-0.08***</td><td>(0.01)</td><td>-0.19***</td><td>(0.01)</td><td>-0.24***</td><td>(0.02)</td></tr><tr><td> $Log(NegativeComments_{i,t-1})$ </td><td>-0.09</td><td>(0.09)</td><td>-0.35</td><td>(0.26)</td><td>-0.03</td><td>(0.18)</td><td>-0.19</td><td>(0.53)</td></tr><tr><td> $Log(CommentVolume_{i,t-1})$ </td><td>0.13***</td><td>(0.03)</td><td>0.19***</td><td>(0.05)</td><td>0.32***</td><td>(0.05)</td><td>0.31***</td><td>(0.09)</td></tr><tr><td> $Log(HighComments_{i,t-1})$ </td><td>-0.10***</td><td>(0.03)</td><td>-0.09</td><td>(0.05)</td><td>-0.19***</td><td>(0.05)</td><td>-0.16*</td><td>(0.08)</td></tr><tr><td> $Log(SelfNegativeReview_{i,j,t-1}) \times Gua$ </td><td></td><td></td><td>0.00</td><td>(0.01)</td><td></td><td></td><td>0.01</td><td>(0.01)</td></tr><tr><td> $Log(SelfReviewVolume_{i,j,t-1}) \times Gua$ </td><td></td><td></td><td>0.01</td><td>(0.01)</td><td></td><td></td><td>0.02*</td><td>(0.01)</td></tr><tr><td> $Log(SelfHighVolume_{i,j,t-1}) \times Gua$ </td><td></td><td></td><td>-0.03</td><td>(0.01)</td><td></td><td></td><td>-0.07***</td><td>(0.01)</td></tr><tr><td> $Log(Entries_{i,t-1}) \times Gua$ </td><td></td><td></td><td>0.05***</td><td>(0.01)</td><td></td><td></td><td>0.04</td><td>(0.02)</td></tr><tr><td> $Log(SelfNegativeReview_{i,j,t-1})$ </td><td>-0.02***</td><td>(0.00)</td><td>-0.02**</td><td>(0.01)</td><td>-0.04***</td><td>(0.01)</td><td>-0.04***</td><td>(0.01)</td></tr><tr><td> $Log(SelfReviewVolume_{i,j,t-1})$ </td><td>0.02***</td><td>(0.00)</td><td>0.02***</td><td>(0.01)</td><td>0.08***</td><td>(0.00)</td><td>0.08***</td><td>(0.01)</td></tr><tr><td> $Log(SelfHighVolume_{i,j,t-1})$ </td><td>0.09***</td><td>(0.01)</td><td>0.10***</td><td>(0.01)</td><td>0.09***</td><td>(0.01)</td><td>0.13***</td><td>(0.01)</td></tr><tr><td> $Log(Entries_{i,t-1})$ </td><td>-0.47***</td><td>(0.01)</td><td>-0.49***</td><td>(0.01)</td><td>-0.63***</td><td>(0.02)</td><td>-0.65***</td><td>(0.02)</td></tr><tr><td> $Log(NewContests_{i,t})$ </td><td>-0.01*</td><td>(0.00)</td><td>-0.01*</td><td>(0.00)</td><td>-0.03***</td><td>(0.01)</td><td>-0.03***</td><td>(0.01)</td></tr><tr><td>Individual-level fixed effects</td><td colspan="4">Yes</td><td colspan="4">No</td></tr><tr><td>Contest-level fixed effects</td><td colspan="4">Yes</td><td colspan="4">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="4">Yes</td><td colspan="4">Yes</td></tr><tr><td>Observations</td><td colspan="4">132,575</td><td colspan="4">132,575</td></tr><tr><td> $R^2$  or pseudo  $R^2$ </td><td colspan="2">0.0723</td><td colspan="2">0.0728</td><td colspan="2">0.0400</td><td colspan="2">0.0401</td></tr><tr><td>AIC</td><td colspan="2">334,692</td><td colspan="2">334,661</td><td colspan="2">270,417</td><td colspan="2">270,365</td></tr><tr><td>BIC</td><td colspan="2">345,006.10</td><td colspan="2">345,073</td><td colspan="2">280,760</td><td colspan="2">280,806</td></tr></table>

Robust standard errors are in parentheses. Dataset contains 1,031 contests and 5,545 contestants. “Gua” is short for Guarantee. For Wald Chi<sup>2</sup> tests, the degrees of freedom are reported in parentheses. $^ { \star \star \star } \mathsf { p } < 0 . 0 0 1 , ^ { \star \star } \mathsf { p } < 0 . 0 1 , ^ { \star } \mathsf { p } < 0 . 0 5 .$

## Appendix I

## Alternative DV: Number of New Contestants Entering Contest i in Period t

In our main results we focused on the number of new submissions as our dependent variable. An alternative measure of participation is the number of participants. It is important to test our model with this alternative dependent variable, for at least two reasons. First, it would potentially rule out an alternative hypothesis that in-process feedback led to more submissions simply because it encouraged more repeated submissions by the current participants (perhaps the direct receivers of the feedback), but not because it attracted more new participants. Second, the number of participants is of theoretical interest because in creative-design contests more participants might lead to more innovative ideas.

We retested our hypotheses by replacing the DV with Contestants (the total number of contestants) in the cross-sectional analysis and with NewContestants<sub>i,t</sub> (the number of participants who made their first submissions to contest i during period t) in the panel analysis. Contestants has a mean of 18.25 and a standard deviation of 25.77 and NewContestants has a mean of 1.84 and a standard deviation of 4.30.

To test the effect of Guarantee, we again report results from five estimates of treatment effects (i.e., PSM, NNM, RA, IPW, and IPWRA). Since the first stages (e.g., computing the propensity score or matching) were exactly the same as those used in the main model, their results as well as balance examinations are omitted. Treatment effects estimated across the five methods (Table I1) show that Guarantee had a positive effect on Contestants . The ATETs were estimated to range from 12.24 to 14.45.

<table><tr><td colspan="3">Table I1. Treatment Effects of Guarantee on Total Contestantsi</td></tr><tr><td></td><td>Estimated ATET</td><td>Observations</td></tr><tr><td>Propensity Score Matching (PSM)</td><td>12.62***(2.23)</td><td>644 treated and control</td></tr><tr><td>Nearest Neighbor Matching (NNM)</td><td>14.45***(1.94)</td><td>644 treated and control</td></tr><tr><td>Regression Adjustment (RA)</td><td>12.46***(1.96)</td><td>1,031</td></tr><tr><td>Inverse-Probability Weighting (IPW)</td><td>12.68***(1.96)</td><td>1,031</td></tr><tr><td>IPW Regression Adjustment (IPWRA)</td><td>12.24***(1.91)</td><td>1,031</td></tr></table>

Robust standard errors are in parentheses and for both PSM and NNM, robust Abadie-Imbens<sup>1</sup> standard errors are reported. For both PSM and NNM, the matching ratio was 1:1. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05.

Results about the main effects of in-process feedback (reported in Table I2) are largely consistent with results from our main model, with a few losing statistical significance. While our main model has yielded support for all the main effects (H2a–H4b), with NewContestants , H3a (effect of negative reviews), H3b (effect of negative comments), and H4b (effect of high comments), have lost support. For hypotheses regarding the interaction effects, the main model has yielded support for the following four hypotheses: H5a (effect of review volume moderated), H5b (effect of comment volume moderated), H7a (effect of high reviews moderated), and H7b (effect of high comments moderated). With this alternative DV (see AMEs reported in Table I3), all four coefficients have the correct signs, and H5a and H7a were supported (the coefficient supporting H7a was marginally significant).

Overall, the results predicting the number of new participants do not differ substantially with those predicting the number of new entries. The effect of Guarantee (H1) and the main effects of the review volume (H2a), comment volume (H2b), and high reviews (H4a) still hold. Two important interaction effects also hold, including the effect of review volume moderated (H5a) and the effect of high reviews moderated (H7a).

<table><tr><td colspan="5">Table I2. Unconditional Negative Binomial Model with FE as Dummies, Predicting the Number of New Contestants Who Entered Contest i During Period t</td></tr><tr><td rowspan="3"></td><td colspan="4">DV = NewContestantsi,t</td></tr><tr><td colspan="4">Unconditional Negative Binomial with Dummy FE</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td>Log(NegativeReviewi,t-1) × Gua</td><td></td><td></td><td>0.07*</td><td>(0.03)</td></tr><tr><td>Log(ReviewVolumei,t-1) × Gua</td><td></td><td></td><td>-0.11**</td><td>(0.04)</td></tr><tr><td>Log(HighReviewi,t-1) × Gua</td><td></td><td></td><td>0.13**</td><td>(0.05)</td></tr><tr><td>Log(NegativeCommentsi,t-1) × Gua</td><td></td><td></td><td>-0.42</td><td>(6.59)</td></tr><tr><td>Log(CommentVolumei,t-1) × Gua</td><td></td><td></td><td>-0.26*</td><td>(0.11)</td></tr><tr><td>Log(HighCommentsi,t-1) × Gua</td><td></td><td></td><td>0.33*</td><td>(0.14)</td></tr><tr><td>Log(Contestantsi,t-1) × Gua</td><td></td><td></td><td>0.23***</td><td>(0.05)</td></tr><tr><td>Log(NegativeReviewi,t-1)</td><td>0.04*</td><td>(0.02)</td><td>0.00</td><td>(0.02)</td></tr><tr><td>Log(ReviewVolumei,t-1)</td><td>0.04*</td><td>(0.02)</td><td>0.09***</td><td>(0.03)</td></tr><tr><td>Log(HighReviewi,t-1)</td><td>-0.30***</td><td>(0.02)</td><td>-0.39***</td><td>(0.03)</td></tr><tr><td>Log(NegativeCommentsi,t-1)</td><td>-0.44</td><td>(0.57)</td><td>-0.25</td><td>(6.48)</td></tr><tr><td>Log(CommentVolumei,t-1)</td><td>0.13**</td><td>(0.05)</td><td>0.22*</td><td>(0.10)</td></tr><tr><td>Log(HighCommentsi,t-1)</td><td>-0.16</td><td>(0.08)</td><td>-0.34**</td><td>(0.10)</td></tr><tr><td>Log(Contestantsi,t-1)</td><td>-0.22***</td><td>(0.05)</td><td>-0.34***</td><td>(0.04)</td></tr><tr><td>Log(MedianSubmn i,t-1)</td><td>0.02</td><td>(0.04)</td><td>0.05</td><td>(0.05)</td></tr><tr><td>Log(NewContestsi,t)</td><td>0.02*</td><td>(0.01)</td><td>0.02</td><td>(0.01)</td></tr><tr><td>Contest-level fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Period and weekend dummies</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Observations</td><td colspan="2">13,665</td><td colspan="2">13,665</td></tr><tr><td>Number of contests</td><td colspan="2">1,031</td><td colspan="2">1,031</td></tr><tr><td>Alpha</td><td colspan="2">0.29</td><td colspan="2">0.29</td></tr><tr><td>LL</td><td colspan="2">-20,135.14</td><td colspan="2">-24,852.01</td></tr><tr><td>AIC</td><td colspan="2">40,332.29</td><td colspan="2">40,216.32</td></tr><tr><td>BIC</td><td colspan="2">40,565.49</td><td colspan="2">40,359.25</td></tr></table>

Bootstrapped standard errors are in parentheses. Alpha is the overdispersion parameter. “Gua” is for Guarantee. $\star \star \star _ { \mathsf { p } } < 0 . 0 0 1$ ${ \star } { \star } _ { \mathsf { p } } < 0 . 0 1$ , \*p < 0.05.

Table 20. Average Marginal Effects of In-Process Feedback on NewContestants<sub>i,t</sub>

<table><tr><td rowspan="2"></td><td colspan="6">Average Marginal Effects of Feedback on NewContestants $_{i,t}$ </td></tr><tr><td colspan="2">Guarantee = 1</td><td colspan="2">Guarantee = 0</td><td colspan="2">Difference</td></tr><tr><td>Log(NegativeReview $_{i,t-1}$ )</td><td>0.21</td><td>(0.14)</td><td>0.00</td><td>(0.06)</td><td>0.21</td><td>(0.14)</td></tr><tr><td>Log(ReviewVolume $_{i,t-1}$ )</td><td>-0.07</td><td>(0.11)</td><td>0.26*</td><td>(0.11)</td><td>-0.33*</td><td>(0.17)</td></tr><tr><td>Log(HighReview $_{i,t-1}$ )</td><td>-0.79***</td><td>(0.39)</td><td>-1.14*</td><td>(0.50)</td><td>0.36+</td><td>(0.19)</td></tr><tr><td>Log(NegativeComments $_{i,t-1}$ )</td><td>-2.00</td><td>(1.39)</td><td>-0.72</td><td>(18.96)</td><td>-1.28</td><td>(19.43)</td></tr><tr><td>Log(CommentVolume $_{i,t-1}$ )</td><td>-0.11</td><td>(0.19)</td><td>0.64</td><td>(0.47)</td><td>-0.75</td><td>(0.56)</td></tr><tr><td>Log(HighComments $_{i,t-1}$ )</td><td>-0.01</td><td>(0.20)</td><td>-0.98</td><td>(0.61)</td><td>0.97</td><td>(0.62)</td></tr></table>

Average marginal effects calculated as the mean marginal effects evaluated at the variables’ values in the sample. Standard errors derived with the delta-method are reported in parentheses. ${ } ^ { \star \star \star } p < 0 . 0 0 1 , { } ^ { \star \star } p < 0 . 0 1 , { } ^ { \star } p < 0 . 0 5 , { } ^ { + } p < 0 . 1 0 .$

## Appendix J

## Code for Matching and Computing the Instrument Variables

```python
# coding: utf-8
import os
from datetime import datetime
import pandas as pd
import numpy as np
import csv
from operator import itemgetter

N_NEIGHBOR = 30

def compute_similarity_rated(contestid1, contestid2, day):
    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict[contestid2]['guaranteed']))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])

    simscore = gua_diff+prize_diff + weekend_diff + contestsheld_diff+averagefb_diff + daytime_diff
    return simscore

def compute_similarity_high(contestid1, contestid2, day):
    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict['guaranteed']))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])

    simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff
    return simscore

def compute_similarity_elim(contestid1, contestid2, day):
    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
```

```python
if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict[contestid2]['guaranteed']))*100
prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend']))*100
daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])

simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff
return simscore

def compute_similarity_comm(contestid1, contestid2, day):

    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict[contestid2]['guaranteed']))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback']])
    comm_diff = (abs(contestday_dict[contestid1]['evercomm'] - contestday_dict[contestid2]['evercomm']))*100

    simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff+comm_diff
return simscore

def compute_similarity_negcomm(contestid1, contestid2, day):

    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday_dict{contestid2}[ˈguaranteed]))*100
    prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize']))/10
    weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict{contestid2}[day['weekend']))*100
    daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict{contestid2}[day['contest_daytime']))*100
    contestsheld_diff = (abs(contest1_exp - contest2_exp))*100
    averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict{contestid2}[ˈaverageFeedback'])
    comm_diff = (abs(contestday_dict[contestid1]['everncomm'] - contestday_dict{contestid2}[ˈeverncomm']))*100

    simscore = gua_diff+prize_diff + weekend_diff + daytime_diff + contestsheld_diff+averagefb_diff+comm_diff
return simscore

def compute_similarity_highcomm(contestid1, contestid2, day):

    contest1_exp = 0
    if (contestday_dict[contestid1]['contestsHeld]>0): contest1_exp=1
    contest2_exp = 0
    if (contestday_dict[contestid2]['contestsHeld]>0): contest2_exp=1

    gua_diff = (abs(contestday_dict[contestid1]['guaranteed'] - contestday-dict[contestid2]['guaranteed']))*100
```

```python
prize_diff = (abs(contestday_dict[contestid1]['prize'] - contestday_dict[contestid2]['prize'])) / 10
weekend_diff = (abs(contestday_dict[contestid1][day]['weekend'] - contestday_dict[contestid2][day]['weekend'])) * 100
daytime_diff = (abs(contestday_dict[contestid1][day]['contest_daytime'] - contestday_dict[contestid2][day]['contest_daytime'])) * 100
contestsheld_diff = (abs(contest1_exp - contest2_exp)) * 100
averagefb_diff = (abs(contestday_dict[contestid1]['averageFeedback'] - contestday_dict[contestid2]['averageFeedback'])) 
comm_diff = (abs(contestday_dict[contestid1]['everhcomm'] - contestday_dict[contestid2]['everhcomm'])) * 100

simscore = gua_diff + prize_diff + weekend_diff + daytime_diff + contestsheld_diff + averagefb_diff + comm_diff
return simscore

def match_two_rows_rated(contestid1, contestid2, day):

    simscore = -1

    row = contestday_dict[contestid1]
    x = contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1

    if abs(row['delay'] - x['delay']) == 0:
    simscore = compute_similarity_rated(contestid1, contestid2, day)

    return simscore

def match_two_rows_high(contestid1, contestid2, day):

    simscore = -1

    row = contestday_dict[contestid1]
    x = contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1
    if contestday_dict[contestid2][day]['cumRated2Ystd'] == 0: return -1

    if abs(row['delay'] - x['delay']) == 0:
    simscore = compute_similarity_high(contestid1, contestid2, day)
    return simscore

def match_two_rows_elim(contestid1, contestid2, day):

    simscore = -1

    row = contestday_dict[contestid1]
    x = contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1
    if contestday_dict[contestid2][day]['cumRated2Ystd'] == 0: return -1

    if abs(row['delay'] - x['delay']) == 0: 
    simscore = compute_similarity_elim(contestid1, contestid2, day)

    return simscore

def match_two_rows_comm(contestid1, contestid2, day):
```

```python
simscore = -1

row=contestday_dict[contestid1]
x=contestday_dict[contestid2]

if (day not in contestday_dict[contestid2]): return -1

if row['evercomm'] == x['evercomm']:
    simscore = compute_similarity_comm(contestid1, contestid2, day)

return simscore

def match_two_rows_negcomm(contestid1, contestid2, day):

    simscore = -1

    row=contestday_dict[contestid1]
    x=contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1

    if row['evercomm'] == x['evercomm']:
    simscore = compute_similarity_negcomm(contestid1, contestid2, day)

    return simscore

def match_two_rows_highcomm(contestid1, contestid2, day):

    simscore = -1

    row=contestday_dict[contestid1]
    x=contestday_dict[contestid2]

    if (day not in contestday_dict[contestid2]): return -1

    if row['evercomm'] == x['evercomm']:
    simscore = compute_similarity_highcomm(contestid1, contestid2, day)

    return simscore

def find_sim_cases_rated(contestid, day):

    similarcases={'cumSimRatedYstd':0,'simcount':0}

    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = match_two_rows_rated(contestid1, contestid2, day)
```

```python
if simscore >= 0:
    cumSimRatedYstd = contestday_dict[contestid2][day]['cumRated2Ystd']
    cases_matched.append([simscore, cumSimRatedYstd])

# Pick the N nearest neighbors
cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimRatedYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)
return similarcases

def find_sim_cases_high(contestid, day):
    similarcases={'cumSimHighYstd_prop':0,'simcount':0}
    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = -1
    simscore = match_two_rows_high(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimHighYstd_prop=
    contestday_dict[contestid2][day]['cumHigh2Ystd]/contestday_dict[contestid2][day]['cumRated2Ystd']
    cases_matched.append([simscore, cumSimHighYstd_prop])

    # Pick the N nearest neighbors
    cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

    num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
    if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimHighYstd_prop'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

return similarcases
```

```python
def find_sim_cases_elim(contestid, day):
    similarcases = {'cumSimElimYstd_prop':0,'simcount':0}
    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = match_two_rows_elim(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimElimYstd_prop=
    contestday_dict[contestid2][day]['cumElim2Ystd]/contestday_dict[contestid2][day]['cumRated2Ystd']
    cases_matched.append([simscore, cumSimElimYstd_prop])

    # Pick the N nearest neighbors
    cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

    num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
    if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimElimYstd_prop'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

    return similarcases

def find_sim_cases_comm(contestid, day):
    similarcases = {'cumSimCommentsYstd':0,'simcount':0}
    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue
    simscore = match_two_rows_comm(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimCommYstd = contestday_dict[contestid2][day]['cumHolderCommentsYstd']
    cases_matched.append([simscore, cumSimCommYstd])

# Pick the N nearest neighbors
```

```python
cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimCommentsYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

return similarcases

def find_sim_cases_negcomm(contestid, day):

    similarcases = {'cumSimNegCommYstd':0,'simcount':0}

    cases_matched = []

    for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue

    simscore = match_two_rows_negcomm(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimNegCommYstd = contestday_dict[contestid2][day]['cumNegCommYstd']
    cases_matched.append([simscore, cumSimNegCommYstd])

    # Pick the N nearest neighbors
    cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

    num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
    if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimNegCommYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

    return similarcases

def find_sim_cases_highcomm(contestid, day):

    similarcases = {'cumSimHighCommYstd':0,'simcount':0}

    cases_matched = []
```

```python
for key in contestday_dict:
    contestid1 = contestid
    contestid2 = key

    if contestid1 == contestid2: continue

    simscore = match_two_rows_highcomm(contestid1, contestid2, day)

    if simscore >= 0:
    cumSimHighCommYstd = contestday_dict[contestid2][day]['cumHighCommYstd']
    cases_matched.append([simscore, cumSimHighCommYstd])

# Pick the N nearest neighbors
cases_matched_sorted = sorted(cases_matched, key=itemgetter(0))

num_cases = min([N_NEIGHBOR, len(cases_matched_sorted)])
if num_cases > 0:
    index = num_cases
    total = 0
    while index > 0:
    index -= 1
    total += cases_matched_sorted[index][1]

    similarcases['cumSimHighCommYstd'] = total/num_cases
    similarcases['simcount']=len(cases_matched_sorted)

return similarcases

def match_rated(row):
    contestid = row['contestID']
day = row['day']

    similarcases={}\ 
    row['cumSimRatedYstd'] = 0
row['simcount'] = 0

    similarcases=find_sim_cases_rated(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimRatedYstd'] = similarcases['cumSimRatedYstd']
    row['simcount'] = similarcases['simcount']
return row

def match_high(row):
    contestid = row['contestID']
day = row['day']

    similarcases={}\ 
    row['cumSimHighYstd'] = 0
```

```python
row['simcount'] = 0

similarcases=find_sim_cases_high(contestid, day)

if similarcases['simcount'] > 0:
    row['cumSimHighYstd'] = similarcases['cumSimHighYstd_prop'] * row['cumrated2ystd']
    row['simcount'] = similarcases['simcount']

return row

def match_elim(row):
    contestid = row['contestID']
    day = row['day']

    similarcases = {}
    row['cumSimElimYstd'] = 0
    row['simcount'] = 0

    similarcases=find_sim_cases_elim(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimElimYstd'] = similarcases['cumSimElimYstd_prop'] * row['cumrated2ystd']
    row['simcount'] = similarcases['simcount']

    return row

def match_comm(row):
    contestid = row['contestID']
    day = row['day']

    similarcases = {}
    row['cumSimCommentsYstd'] = 0
    row['simcount'] = 0

    similarcases=find_sim_cases_comm(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimCommentsYstd'] = similarcases['cumSimCommentsYstd']
    row['simcount'] = similarcases['simcount']

    return row

def match_negcomm(row):
    contestid = row['contestID']
    day = row['day']

    similarcases = {}
    row['cumSimNegCommYstd'] = 0
    row['simcount'] = 0
```

```python
if row['cumholdercommentsystd'] == 0:
    return row

similarcases=find_sim_cases_negcomm(contestid, day)

if similarcases['simcount'] > 0:
    row['cumSimNegCommYstd'] = similarcases['cumSimNegCommYstd']
    row['simcount'] = similarcases['simcount']

return row

def match_highcomm(row):

    contestid = row['contestID']
    day = row['day']

    similarcases = {}

    row['cumSimHighCommYstd'] = 0
    row['simcount'] = 0

    if row['cumholdercommentsystd'] == 0:
    return row

    similarcases=find_sim_cases_highcomm(contestid, day)

    if similarcases['simcount'] > 0:
    row['cumSimHighCommYstd'] = similarcases['cumSimHighCommYstd']
    row['simcount'] = similarcases['simcount']

    return row
```

## References

Abadie, A.,and Imbens, G. W. 2006. “Large Sample Properties of Matching Estimators for Average Treatment Effects,” Econometrica (74:1), pp. 235-267.

Abadie, A.,and Imbens, G. W. 2011. “Bias-Corrected Matching Estimators for Average Treatment Effects,” Journal of Business and Economic Statistics (29:1), pp. 1-11.

Abadie, A.,and Imbens, G. W. 2016. “Matching on the Estimated Propensity Score,” Econometrica (84:2), pp. 781-807.

Jiang, Z. Z., Huang, Y., and Beil, D. R. 2016. “The Role of Feedback in Dynamic Crowdsourcing Contests: A Structural Empirical Analysis,” Ross School of Business Paper No. 1334, University of Michigan.

Wooten, J. O., and Ulrich, K. T. 2016. “Idea Generation and the Role of Feedback: Evidence from Field Experiments with Innovation Tournaments,” Production and Operations Management (26:1), pp. 80-99.

Yang, Y., Chen, P.-Y., and Pavlou, P. A. 2013. “Managing Open Innovation Contests in Online Market,” Working Paper, Temple University, Philadelphia, PA.
