---
otero_id: 13618
otero_key: "M9HRECXE"
title: "An Empirical Study of Strategic Opacity in Crowdsourced Evaluations"
authors: "Linli Xu; Qi Xie; Gordon Burtch"
year: "2025"
journal: "MIS Quarterly"
doi: "10.25300/misq/2024/17441"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# AN EMPIRICAL STUDY OF STRATEGIC OPACITY IN CROWDSOURCED EVALUATIONS<sup>1</sup>

Linli Xu Carlson School of Management, University of Minnesota – Twin Cities Minneapolis, MN, U.S.A. {linlixu@umn.edu}

Qi Xie College of Business, Oregon State University Corvallis, OR, U.S.A. {qi.xie@oregonstate.edu}

Gordon Burtch Questrom School of Business, Boston University Boston, MA, U.S.A. {gburtch@bu.edu}

Crowd-voting mechanisms are commonly used to implement scalable evaluations of crowdsourced creative submissions. Unfortunately, the use of crowd-voting also raises the potential for gaming and manipulation. Manipulation is problematic because (1) submitters’ motivation depends on their belief that the system is meritocratic, and (2) manipulated feedback may undermine learning, as submitters seek to learn from received evaluations and those of peers. In this work, we consider a design approach to addressing the issue, focusing on the notion of strategic opacity, i.e., purposefully obfuscating evaluation procedures. On the one hand, opacity may reduce the incentive and thus the prevalence of vote manipulation, and submitters may instead dedicate that time and effort to improving their submission quantity or quality. On the other hand, because opacity makes it difficult for submitters to discern the returns to legitimate effort, submitters may also reduce their submission effort or simply exit the market. We explored this tension via a multimethod study employing field experiments at 99designs and a controlled experiment on Amazon Mechanical Turk. We observed consistent results across all experiments: opacity leads to reductions in gaming in these crowdsourcing contests and significant increases in the allocation of effort toward legitimate vs. illegitimate activities, with no discernible influence on contest participation. We discuss boundary conditions and the implications for contest organizers and contest platform operators.

Keywords: Crowdsourcing, evaluation, voting, strategic opacity, gaming, manipulation

## Introduction

Crowdsourcing offers a useful avenue for firms to solicit creative, innovative content from a widely dispersed base of individual contributors (the crowd). In many applications, the evaluation of crowdsourced submissions is straightforward, based on objective performance characteristics. However, in domains where the quality of submissions is more subjective, or a matter of taste, evaluation is more difficult. In such settings, scalable evaluation of submissions often takes the form of a crowd-voting mechanism (Chen et al., 2020). Unfortunately, crowd-based voting mechanisms are a challenge to manage for platform operators and contest organizers because they have the potential to be manipulated (Mukherjee et al., 2018). This potential raises two issues: First, if members of the crowd believe the evaluation mechanism is subject to manipulation, their incentive to make submissions will decline. Second, submitters rely on these feedback mechanisms to learn and improve (e.g., Huang et al., 2014; Zhang et al., 2019). To the extent that the feedback is biased by manipulation, submitters’ learning will be impeded, and overall submission quality will suffer.

One potential solution that we explore here is the notion of strategic opacity (Ederer et al., 2018). In the context of crowdsourced evaluations, strategic opacity would amount to the intentional withholding of information about evaluation procedures that take crowd votes as input. While the benefits of strategic opacity have received theoretical consideration, with attention paid to the conditions under which opacity may be desirable, little work has examined the efficacy of such a policy in practice, nor specifically in the context of creative crowdsourcing. While strategic opacity in performance evaluation has been considered in paid work generally, creative crowdsourcing is unique because performance evaluations are inherently subjective, making it difficult to predict the effects of opacity.

Given the above, we sought to address the following research question: What influence does a policy of strategic opacity in crowd-evaluations have on contestants’ allocation of time and effort in crowdsourced creative design contests? Specifically, we considered how a policy of opacity affected rates of contest participation and contestants’ allocation of effort toward legitimate activities (i.e., submission quantity or time invested) vs. illegitimate activities (i.e., vote manipulation).

Further, we considered how different contextual factors can interact with strategic opacity. We first explored the contextual moderators of illegitimate effort, namely the influence of contest competition, which has been frequently shown to have a large effect on contestant motivation (e.g., Boudreau et al., 2011, 2016). In the context of our policy choice, greater competition may reduce the baseline tendency toward manipulation if contestants perceive that the returns to cheating are uncertain. In turn, competition is thus likely to moderate the effects of strategic opacity on contestants’ effort allocation. Second, we considered boundary conditions for the effectiveness of opacity. In practice, the scope of opacity in evaluation rules can vary. For example, a contest organizer might obfuscate how crowd-voted ratings are aggregated and might also obfuscate the extent to which other inputs are considered, e.g., evaluators might draw on their own expertise or other outside sources of information, beyond crowd ratings.

We addressed these questions via a series of experiments, both in the field and in a controlled setting. We began with a series of field experiments conducted at 99designs, a global freelancing platform that hosts graphic design contests on behalf of businesses. We examined the effect of randomly assigned strategic opacity (vs. transparency) in the evaluation of design submissions in tandem with randomly manipulated levels of competition. We observed no statistically significant effects of opacity on contestants’ decisions to participate in a contest. However, we did find evidence that opacity significantly shifted participants’ allocation of effort toward legitimate activities (i.e., submission effort) and away from illegitimate activities (i.e., attempts at vote manipulation). Further, we showed that the effects were moderated by competition, as the reduction in participants’ attempts to manipulate votes was moderated by the degree of competition they faced, and we observed that the impact of opacity on participants’ allocation of effort toward legitimate rather than illegitimate activities increased with the scope of opacity.

Next, we report the results of a controlled experiment conducted at Amazon Mechanical Turk (AMT), wherein we organized a contest around a different type of submission, namely an ideation task. We broadly replicated the main findings; again, we found no significant effects on subjects decision to participate, yet again found that opacity causally increased participants’ investment of effort toward legitimate rather than illegitimate activities.

Our findings bear important implications for policy and platform design in creative crowdsourcing contexts as well as broader contexts involving contract design in creative work. Insights gleaned from our study can inform platform operators in the design and maintenance of evaluation mechanisms, indicating the response that may be expected to certain policies and the aggregated impact that such policies may have on the distribution of crowd contributions.

## Related Work

## Gaming in Performance Evaluations

The prospect of performance evaluations can elicit two forms of effort from agents: “legitimate,” which focuses on improving an underlying factor of interest to the evaluator, and “illegitimate,” which focuses on gaming or manipulating the evaluator’s performance metrics (Ziewitz, 2019). Such illegitimate effort is far from superfluous; it often comes at the cost of legitimate activities, yielding negative impacts on a broader system or work environment. As a simple example, firm performance is negatively affected by managers’ attempts to “manipulate their numbers” (Courty & Marschke, 2004; Benson, 2015). This dichotomy between legitimate and illegitimate effort arises across a variety of settings of interest. Notable examples include search engine optimization (Ziewitz, 2019), reputation management systems (Luca & Zervas, 2016; He et al., 2022), and evaluations based on machine-learning classifiers in general (Kleinberg & Raghavan, 2020; Wang et al., 2023).

Ample work has explored factors that contribute to individuals’ investment of illegitimate rather than legitimate effort. Competition is a particularly well-studied driver. Prior work observes that greater variation in wages can induce uncooperative behavior when workers’ pay is tied to peer comparisons (Lazear, 1989), particularly among individuals of lower ability (Schwieren & Weichselbaumer, 2010). Competition can even induce uncooperative behavior when pay is not tied to relative performance if individuals believe that peer comparisons will nonetheless determine outcomes (Charness et al., 2014).

Trust (or the lack thereof) is also a key driver of illegitimate effort (Gibbs et al., 2004, 2005; Peters et al., 2020), being particularly important when evaluation schemes involve a subjective component (Baker et al., 1994), as is the case in design-oriented crowdsourcing. Because subjective evaluations may be perceived as biased, unfair, or unpredictable (Gill et al., 2013; Takahashi et al., 2021), workers are most receptive when they have had more (positive) experiences with the evaluator (Gibbs et al., 2004). Workers may also take cues from their peers: Perceiving that others are behaving well, and thus presumably trusting the evaluator, workers may follow suit (Zuo et al., 2016). Conversely, if workers believe peers are gaming the system, they may tend to do so as well (Yang et al., 2021). Absent trust in the evaluation procedure, workers may also simply quit (Takahashi et al., 2021).

Though ample research has addressed this topic, creative crowdsourcing differs from the contexts considered in past literature (regular employees, their managers, students, or consumers) in several important respects. First, evaluations in creative crowdsourcing often involve an extreme degree of subjectivity because the quality of work is naturally a matter of taste, i.e., “beauty is in the eye of the beholder” (Burtch et al., 2021). Second, in creative crowdsourcing, workers’ behaviors are based on beliefs and perceptions about the fairness, trustworthiness, and predictability of multiple evaluators, both the contest organizer and the voting crowd. Third, workers’ behavior will be influenced by their trust and faith in the voting process itself, which may be undermined by a perception that peers are exerting illegitimate effort. Fourth, creative crowdsourcing work is fluid in that the barriers to entry (and exit) are relatively low compared with traditional work.

The above points raise a variety of salient considerations for the use or design of vote-based evaluation schemes in creative crowdsourcing contexts (Chen et al., 2020). By relying on open crowd-voting systems, workers are presented with an opportunity to engage in illegitimate effort (manipulating votes). The question thus arises of how crowd-voting should be incorporated into an evaluation process. One approach proposed in prior literature to mitigate illegitimate effort is to make performance evaluation criteria less transparent to workers, a possibility we focus on in this work.

This notion, termed “strategic opacity,” purposefully blurs the association between agents’ inputs and the evaluation outputs (Ederer et al., 2018). This approach can be expected to reduce gaming attempts on the part of crowd submitters by raising the cost of said gaming. Under an opacity regime, participants lack knowledge of exactly what to game and how to game it, as the returns to manipulation are noisy. Further, contestants may believe that their peers will face similar challenges and may thus be more confident that the overall evaluation process is authentic and meritocratic—an important factor in individuals’ decision to participate (Basu et al., 2019). Together, these factors can induce greater participation and investment in legitimate contest activities.

At the same time, however, in the absence of transparency about specific decision rules, participants may instead exhibit reduced confidence in the fairness of the evaluation process, particularly if they lack trust in the platform or the contest organizer. If contestants find it more difficult to assess the marginal returns to their legitimate effort, a policy of strategic opacity may have the counterproductive effect of inducing submitters to reduce their effort investment altogether, to the point they may even decide not to participate (Takahashi et al., 2021). Indeed, Rahman (2021) reports some evidence of this in the context of an online labor market, observing that opaque evaluation algorithms create the perception of an “invisible cage” that constrains workers’ activities.

The relative influence of these various mechanisms is difficult to discern a priori in the context of creative crowdsourcing because submission quality and submitter performance evaluation are inherently subjective (Burtch et al., 2021). As a result, it is not entirely clear how submitters may perceive the returns to legitimate effort. Further, given this subjectivity, as well as the potential for vote manipulation, it is not clear whether submitters perceive crowd evaluations to be particularly meritocratic. These factors make it challenging to anticipate what effects opacity may have on crowdsourcing participation or participants allocation of effort between legitimate submission activities versus attempts at vote manipulation.

Our work thus extends prior literature, offering a first investigation of the efficacy of strategic opacity in the context of creative crowd-sourcing contests, which bear a variety of novel characteristics. We provide evidence that a policy of opacity reduces illegitimate effort and increases legitimate effort and show that these benefits increase with the degree of competition at play and the scope of opacity.

## Crowdsourced Evaluation

Prior research has delved into the architecture of crowdsourcing systems, focusing on system design and crowd motivations (Malone et al., 2010). In online crowdsourcing contests specifically, financial incentives and competition levels have been found to play a large role in determining the quality of submissions (Boudreau et al., 2011, 2016). Crowdvoting is often used to evaluate submissions in these settings. While scalable, crowd-voting is prone to several biases, including underreporting (Hu et al., 2009), social influence (Aral, 2014), and outright manipulation (Mayzlin et al., 2014; Luca & Zervas, 2016). Several studies have pursued approaches to reducing these biases. For instance, Fradkin et al. (2021) designed a review system to combat underreporting at Airbnb, and Greenstein et al. (2021) suggested that bias correction methods and larger crowd involvement help to address these problems at Wikipedia.

Our work centers on reducing bias specifically arising from attempts at manipulation. Prior work in this space has examined approaches to detecting manipulation (Ott et al., 2013; He et al., 2022) and mechanism design to mitigate it (Kamar & Horvitz, 2012). Notably, Kamar and Horvitz (2012) proposed a paid incentive system to align evaluator and host interests, though their approach is financially challenging to scale. We contribute to this literature by exploring the potential of strategic opacity to mitigate vote manipulation in favor of legitimate effort in crowdsourced tasks while also considering its possible parallel influence on contest participation and the potential moderating influence of competition.

## Field Experiment: Logo Design Contests

We begin by presenting the design and analysis for our field experiments, wherein we focused on the relationship between strategic opacity in crowd-voting evaluations and submitters’ propensity to participate, as well as submitters’ subsequent investment of legitimate (submission quantity) vs. illegitimate (vote manipulation) effort.

## Experimental Context

Our randomized field experiments were implemented on 99designs.com, a global contest platform that connects graphic designers with clients who need to complete certain creative projects. After clients launch a contest, they may allow open competition or they can invite specific designers to participate, providing a link to the contest page via private message. We leveraged the targeted invitation mechanism for our purposes, as this feature provided us with complete control over which designers could view a contest and submit designs. Further, by adjusting the content of private messages, we were able to deliver randomly assigned informational treatments.

On the contest page, the client needed to post a design brief, including the company’s name, a simple description of the business and its target audience, any preferences or requirements for the design, and the prize amount that the winning designer would receive. If a designer accepted the invitation, they could submit one or multiple entries over a 3- day open window.<sup>2</sup> Once the open period ended, the client had 2 weeks to review the submissions and select a winner.<sup>3</sup>

The design review process could be undertaken entirely by the client. Alternatively, the client could choose to employ a crowd-evaluation mechanism provided by 99designs.com, known as “white-label presentations.” Using this feature, the client identified a set of design submissions and incorporated them into a poll. The polling link could then be distributed for voting to any individuals the client wished; these individuals could then provide ratings between 1 and 5 stars and optional textual comments on any of the designs. Notably, when providing votes, a voter was not provided with any information on other votes or comments that may have been entered. The client had full control over the list of designs that appeared in the poll, and the client could also create multiple polls incorporating different sets of design submissions. We also leveraged this crowd-evaluation feature in our experiment and exploited the option to create multiple polls to exogenously vary the perception of competition (by randomly adjusting the number of submissions appearing in the poll alongside a particular designer’s submission) and to identify submitters’ attempts at voting manipulation, as we describe next in more detail.

## Experimental Design and Procedures

We began by creating a pair of invitation-only contests on 99designs.com. Each contest was ostensibly created to support a new consulting company that would “launch shortly,” whose target audience would include start-ups and small businesses. The stated contest objective was to design a company logo with a winning prize of \$190.<sup>4</sup> Since the only difference between the contests was the company’s name, the two contests were launched during two separate time windows to avoid suspicion from the platform participants. We employed features native to the platform that prevent participating designers from being able to view others’ submissions prior to the contest ending and prevent the contest from being indexed by search engines. Figure 1 presents the flowchart of our experimental procedure. We next explain each step in detail.

We identified the pool of designers (subjects) to invite to our contests by filtering on those who indicated experience/interest in completing “English” language “Logo & identity” designs, for “Business and consulting.” Applying these filters to the candidate pool left us with 8,334 candidate designers.

Among this group, we randomly selected 1,000 designers to invite to each of our two contests, the maximum number of invitations we could send within 24 hours. When running the second contest, we excluded the 1,000 designers invited to the first. Because 33 designers deactivated their accounts or had their profiles configured to block contest invitations, our final set of subjects included 1,967 unique designers. In the invitation message, we briefly described why the designer was selected and included a link to the contest and a link to the company’s website, created using Google Sites. Unbeknownst to the designers, each designer received a link to a unique copy of the company website, enabling us to trace their visit and associated activities on the site (via Google Analytics). In the invitation message, we also indicated that to streamline the final selection process, we would select a subset of submissions for inclusion in a crowd-based vote over a threeday evaluation period. Lastly, we informed the designer how the final winner would be selected, randomly manipulating whether the provided explanation of the decision rule was opaque or transparent.<sup>5</sup>

Under the transparent condition, designers were told: “Our selection of the winning submission will ultimately be based on the results of the vote, i.e., the design that receives the highest average score.” Under the opaque condition, designers were told: “Our selection of the winning submission will be based on an internal evaluation, which will also consider the results of the vote.” Thus, our opacity intervention obfuscated the evaluation rule and the complete set of inputs that were considered in the evaluation. Figure 2 presents the invitation message under these two conditions, respectively. Designers were randomly assigned to one of the two conditions at the time of invitation.

![](/api/attachments/M9HRECXE/fulltext/images/da2999ba30d476157ba15cf4f8df09eb6392f81ec9da09f66061e680bb383314.jpg)

could explain the overall low participation rate. However, the participation rate between the two evaluation conditions ultimately did not differ, as we show in the Experimental Results section.

![](/api/attachments/M9HRECXE/fulltext/images/c62ae024620db1e5f9958409df17debad14124fa54ae98e73f8cee47a4a6d78e.jpg)

## Figure 2a. Field Experiment: Contest Invitation Message, Transparent Condition

![](/api/attachments/M9HRECXE/fulltext/images/9363e42d38ff02f7e0dda07554e122ebe10d7d9253355c69e22aae01b1de8425.jpg)

https://99designs.com/logo-design/c...ny-1167790

## Figure 2b. Field Experiment: Contest Invitation Message, Opaque Condition

Each designer could decide whether to participate in the contest and how many entries to submit during the 3-day open window. Once the open window closed, we created voting pages using the “white-label presentations” feature of 99designs (discussed above in the Experimental Context section). These voting pages were, again, designer-specific and were embedded in the designer’s unique copy of the company website. On each designer-specific voting page, we displayed the eventual “winning” design (chosen up-front from the set of all submissions based on best fit with the contest brief), one of the designer’s own submissions (chosen at random from their submission set), and a random selection of other entries supplied by other designers. The winning design needed to be included on all voting pages; thus, we selected it before the voting stage started.

After the submission stage, we sent another private message to each participant, notifying them that one of their entries had been selected for entry into the short list for the crowd-voting process. A link to the designer-specific copy of the company website was again included in the reminder message. We also reminded participants about the final selection rule using the same wording noted earlier (see Figure 2), maintaining the same transparent or opaque language. Because the voting page was specific to a given designer, we could clearly identify any votes they entered to attempt manipulation, one of our major outcomes of interest.<sup>6</sup> It is worth noting that some votes may have reflected true feelings about certain submissions. However, the observed votes suggested upvoting for one’s own design and downvoting for competitors’ designs.

Beyond the main effect of opacity on participants’ attempts at manipulation, we considered the moderating role of competition. To assess this, we independently manipulated the level of competition intensity, varying the number of other design submissions that appeared on a given designer’s voting page alongside their own. That is, at the voting stage, we randomly assigned subjects in the transparent condition to either low or high competition and did the same for subjects in the opaque condition. Under low competition, eight designs (i.e., the focal designer’s submission, the “final winning” design, and six other randomly selected submissions) were presented. Under high competition, 16 designs (i.e., the focal designer’s submission, the “final winning” design, and 14 other randomly selected submissions) were displayed. All entries were presented vertically on the voting page. To avoid the influence of ordering effects, each subject’s own entry was fixed at the fourth spot, and the “final winning” design was listed in the fifth spot.<sup>7</sup>

At the end of the 3-day voting period, we removed the embedded voting link on all company websites and stopped accepting new responses on all voting pages. We then awarded the prize to the designer whose submission was selected upfront as the “winning” design.

## Data

The first logo design contest, hosted on behalf of a fictitious company named DAIE, was launched on May 29, 2022. The second contest, on behalf of a company named WEIV, began on June 16, 2022. In total, 279 (out of 1,967) invited designers chose to participate in our contests, submitting at least one entry. Among these participants, 47% (132) were under the transparent condition and 53% (147) were under the opaque condition. As noted earlier, the participants of each condition were then block-randomized into high and low competition treatments.

We began by evaluating randomization efficacy by comparing designer characteristics across experimental conditions. To achieve this, we scraped designer profile information for the entire set of 8,334 qualified designers before our first contest launch. The information included a platform-defined measure of ability (entry\_level, mid\_level, top\_level), <sup>8</sup> designer tenure, and measures of project experience (repeat\_clients, 1-on-1\_projects, runner\_up, contests\_won, stars, reviews). Table 1 presents the definitions of these designer characteristics and mean comparisons between the transparent and opaque conditions across various groups of designers.

Recall that the random assignment to experimental conditions was performed at the invitation stage. We therefore compare designer characteristics between the invited designers assigned to the transparent condition and those assigned to the opaque condition, in the first column of Table 1. The results indicate that our randomization was broadly effective, as we observed no statistically significant differences between the two groups for all measures except one: entry\_level (p-value = 0.01). Recognizing that some of our outcomes of interest were only defined conditional on the decision to participate, we also compared average designer characteristics between the two conditions among those who chose to participate in our contests (Table 1, Column 2). Here, the only difference we observed that was statistically significant is contests\_won (pvalue = 0.04).

Importantly, for each of these tests, we note that applying a correction for multiple comparisons, e.g., Bonferroni, Benjamini-Hochberg, caused the observed differences to become statistically insignificant.<sup>9</sup> Finally, we also observed no statistically significant imbalance when we performed similar comparisons between the high- and low-competition conditions. Thus, in sum, the results of the randomization checks are consistent with effective randomization.

The design of our field experiment allowed us to measure several key outcome variables that captured contestants participation and effort. We measured legitimate efforts using the number of submissions. Further, we operationalized illegitimate efforts based on vote manipulation. We also obtained separate measures reflecting whether the designer engaged in vote manipulation targeted toward their own design or those submitted by others. Table 2 provides definitions of these measures.

## Experimental Results

We first examined the relationship between designer participation, the allocation of effort toward legitimate vs. illegitimate activities, and the opacity of the selection rule. We then explored the moderating role of competition intensity and how effect magnitudes vary with the scope of opacity.

Table 1. Field Experiment: Randomization Check

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Description</td><td colspan="3">Invited designers (N = 1967)</td><td colspan="3">Participating designers (N = 279)</td></tr><tr><td>Mean (SD)(Transparent)</td><td>Mean(SD)(Opaque)</td><td>p-value</td><td>Mean (SD)(Transparent)</td><td>Mean (SD)(Opaque)</td><td>p-value</td></tr><tr><td>Entry_level</td><td>Dummy variable, 1 if a designer is assigned as entry level</td><td>0.31 (0.46)</td><td>0.37(0.48)</td><td>0.01</td><td>0.42(0.50)</td><td>0.51(0.50)</td><td>0.15</td></tr><tr><td>Mid_level</td><td>Dummy variable, 1 if a designer is assigned as mid-level</td><td>0.40 (0.49)</td><td>0.36(0.48)</td><td>0.11</td><td>0.48(0.50)</td><td>0.42(0.50)</td><td>0.29</td></tr><tr><td>Top_level</td><td>Dummy variable, 1 if a designer is assigned as top level</td><td>0.29 (0.46)</td><td>0.27(0.45)</td><td>0.3</td><td>0.09(0.29)</td><td>0.07(0.25)</td><td>0.48</td></tr><tr><td>Repeat_clients</td><td>Total number of clients who hired a designer more than once</td><td>11.06 (41.09)</td><td>16.40(116.63)</td><td>0.18</td><td>4.72(7.55)</td><td>3.34(8.67)</td><td>0.16</td></tr><tr><td>1-to-1_projects</td><td>Total number of 1-to-1 projects that a designer has completed</td><td>32.16 (114.15)</td><td>51.63(415.95)</td><td>0.16</td><td>9.55(33.94)</td><td>8.31(33.84)</td><td>0.76</td></tr><tr><td>Runner_up</td><td>Total number of times that a designer was named as a contest finalist but did not win</td><td>82.61 (113.93)</td><td>76.98(116.34)</td><td>0.28</td><td>71.67(80.46)</td><td>62.24(82.32)</td><td>0.34</td></tr><tr><td>Contests_won</td><td>Total number of contest prize awards paid to a designer</td><td>38.39 (52.10)</td><td>35.87(51.67)</td><td>0.28</td><td>28.79(31.88)</td><td>21.59(26.69)</td><td>0.04</td></tr><tr><td>Tenure</td><td>The number of days elapsed since a designer joined 99designs.com</td><td>2724.05(1180.50)</td><td>2674.89(1166.12)</td><td>0.35</td><td>2597.73(1172.35)</td><td>2475.35(1150.63)</td><td>0.38</td></tr><tr><td>Stars</td><td>The average star rating received by a designer</td><td>4.97 (0.07)</td><td>4.97(0.06)</td><td>0.66</td><td>4.97(0.06)</td><td>4.96(0.06)</td><td>0.26</td></tr><tr><td>Reviews</td><td>The total number of public client reviews received by a designer</td><td>41.71 (57.99)</td><td>45.99(89.39)</td><td>0.29</td><td>27.02(28.21)</td><td>24.75(35.20)</td><td>0.64</td></tr></table>

<table><tr><td colspan="2">Table 2. Field Experiment: Variable Descriptions</td></tr><tr><td>Variable</td><td>Description</td></tr><tr><td>Participation</td><td>A binary indicator, equals 1 if a subject submitted at least one logo design.</td></tr><tr><td>Number of Submissions (or NS)</td><td>A count measure, the number of logo designs a participant submitted.</td></tr><tr><td>Number of Vote Self (or NVS)</td><td>A count measure, the number of votes a participant submitted on their own submission.</td></tr><tr><td>MaxNumVoteOthers (or MNVO)</td><td>A count measure, the maximum number of votes a participant submitted on the other competing entries presented on the participant&#x27;s voting page.*</td></tr></table>

Note: \*Alternatively, we also considered the average number of votes for all competing entries; the results remained consistent across all analyses.

<table><tr><td colspan="3">Table 3. Field Experiment: Treatment Effect on Participation</td></tr><tr><td></td><td>(1) LPM Estimate (SE)</td><td>(2) Logistic Estimate (SE)</td></tr><tr><td>Opaque condition</td><td>0.01 (0.02)</td><td>0.12 (0.13)</td></tr><tr><td>Constant</td><td>0.13*** (0.01)</td><td>-1.86*** (0.09)</td></tr><tr><td>Observations</td><td>1,967</td><td>1,967</td></tr><tr><td>F-test</td><td>0.89</td><td></td></tr><tr><td>Log likelihood</td><td></td><td>-802.66</td></tr><tr><td>LR  $\chi^2$ </td><td></td><td>0.89</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

Note: $^ { \star } p < 0 . 1 ; ^ { \star \star } p < 0 . 0 5 ; ^ { \star \star \star } p < 0 . 0 1 .$

## Treatment Effect of Strategic Opacity

We began by examining whether and how opacity in evaluation procedures affects individuals’ decisions to participate and their allocation of effort toward legitimate vs. illegitimate submission activities. We first estimated the effect of the opacity treatment on the binary indicator of participation, ?????????????????????????? , using a linear probability model (LPM) and logistic regression, as in Equation (1). ?????????????????? is a binary indicator that equals 1 if participant i was exposed to the opaque selection rule, and 0 otherwise. The estimated results reported in Table 3 (above), Columns 1 and 2, indicate that, on average, opacity did not significantly influence designers’ likelihood of participating in a contest, and the estimated effect is a rather precise null.

$$
P a r t i c i p a t i o n _ {i} = \alpha_ {1} + \beta_ {1} * T r e a t m e n t _ {i} + \varepsilon_ {1 i}\tag{1}
$$

We next turned our attention to the effect of opacity on participants’ decisions to engage in illegitimate versus legitimate effort. We first explored how this effort ratio varied, on average, under alternative winner selection rules, replacing the outcome in Equation (1) with our ratio of illegitimate to legitimate effort, i.e., $( N V S _ { i } + M N V O _ { i } ) / N S _ { i }$ . The distribution of this ratio was right-skewed, ranging from 0 to 138; thus, we also considered its logarithm.

The results of this estimation, which were necessarily limited to the sample of participating designers, appear in Table 4. Under both specifications, we observed a statistically significant, negative effect, indicating that individuals’ allocation of effort toward illegitimate effort declined in favor of legitimate effort.<sup>10</sup> We also explored the effects of our opacity treatment on our legitimate and illegitimate effort measures separately and observed consistent results on each outcome: Legitimate effort rose, and illegitimate effort declined. These expanded results are omitted from the manuscript for brevity but are available upon request.

## The Moderating Role of Competition Intensity on Illegitimate Effort

Having established how strategic opacity influences participants’ participation and allocation of effort between legitimate and illegitimate activities, we sought to explore the role that competition plays in moderating the effect on vote manipulation specifically. Given that our outcomes were count measures, ??????????????????????(??????) and ????????????????????????ℎ?????? (????????), we employed Poisson regression and introduced the independently manipulated competition treatment as a moderating variable. Our regression was thus a generalized linear model, which expressed the log of the expected value of these outcomes as a linear function of our treatment indicators:

$$
\begin{array}{l} \log (E (Y | x)) = \alpha_ {2} + \beta_ {2} \times \text { Treatment } + \gamma \times \text { Competition } + \\ \eta \times \text { Treatment } \times \text { Competition } \end{array} \tag {2}
$$

where ?? ∈ {??????, ????????}. ?????????????????????? is a binary indicator equalling 1 if a participant was exposed to the highcompetition condition (16 designs in total on the voting page), and 0 under the low-competition condition (eight designs on the voting page). The parameter of interest is ??, capturing the moderating role of competition. We also explored a bivariate Poisson regression, jointly modeling vote counts on participants’ own designs and those of competitors.

Table 5 shows the estimates from these regressions. Two findings from Columns 1 and 2 are worth noting: (1) The opacity of the selection rule did not significantly reduce the number of votes that contestants submitted on their own submission when competition was low, and (2) high competition made participants cheat more when the selection rule was transparent and cheat less when the rule was opaque. We also considered a bivariate Poisson model, allowing the two count measures to be jointly determined. Those estimates are shown in Column 3. The estimates continue to suggest that the competition level affected the extent to which participants manipulated votes for their own and competitors’ submissions under different selection rules. We also confirmed that our results held by employing negative binomial regression.

Table 4. Field Experiment: Treatment Effect on Ratio of Illegitimate to Legitimate Effort

<table><tr><td></td><td>(1) OLS Estimate (SE)</td><td>(2) Log-OLS Estimate (SE)</td></tr><tr><td>Opaque condition</td><td>-3.22** (1.56)</td><td>-0.34** (0.13)</td></tr><tr><td>Constant</td><td>5.88*** (1.14)</td><td>0.89*** (0.09)</td></tr><tr><td>Observations</td><td>279</td><td>279</td></tr><tr><td>F-test</td><td>4.27</td><td>6.90</td></tr></table>

<table><tr><td colspan="5">Table 5. Field Experiment: Moderating Effects of Competition Intensity</td></tr><tr><td rowspan="2">Variables</td><td>(1) Poisson</td><td>(2) Poisson</td><td colspan="2">(3) Bivariate Poisson</td></tr><tr><td>NVS</td><td>MNVO</td><td>NVS</td><td>MNVO</td></tr><tr><td>Opaque condition ( $\beta_4$ )</td><td>0.02 (0.07)</td><td>-0.48*** (0.17)</td><td>0.01 (0.02)</td><td>-0.04 (0.09)</td></tr><tr><td>High-competition ( $\gamma$ )</td><td>0.87*** (0.06)</td><td>0.79*** (0.13)</td><td>0.68*** (0.04)</td><td>0.62*** (0.10)</td></tr><tr><td>Opaque × High-competition ( $\eta$ )</td><td>-1.67*** (0.11)</td><td>-1.57*** (0.26)</td><td>-0.70*** (0.04)</td><td>-0.67*** (0.11)</td></tr><tr><td>Constant</td><td>1.67*** (0.05)</td><td>0.28*** (0.11)</td><td>1.86*** (0.02)</td><td>0.52*** (0.07)</td></tr><tr><td>Observations</td><td>279</td><td>279</td><td colspan="2">279</td></tr><tr><td>Log likelihood</td><td>-2866.29</td><td>-776.66</td><td colspan="2">-3129.39</td></tr><tr><td>LR  $\chi^2$ </td><td>582.59***</td><td>182.08***</td><td colspan="2">323.96***</td></tr></table>

Note: Standard errors in parentheses. $^ { \star } p < 0 . 1 ; ^ { \star \star } p < 0 . 0 5 ; ^ { \star \star \star } p < 0 . 0 1 .$

These results imply that strategic opacity in evaluation procedures is more effective in reducing vote manipulation when competition is high. A possible explanation is that as the competition level increases under the opaque rule, the uncertain return of cheating grows even more uncertain, which in turn decreases contestants’ interest in manipulating votes.

## Varying the Degree/Scope of Opacity

We next explored boundary conditions, particularly regarding the scope of what is made opaque to the designers. To do this, we conducted an additional round of contests on 99designs.com. Recall that, in the first round, the opacity treatment involved both the evaluation threshold and the identity of the evaluator. In this round, we limited our opacity intervention such that it obfuscated on the evaluation threshold. Specifically, we created logo design contests following the same procedures presented in Figure 1, with the only difference relating to the explanation of the selection rule presented in the messages we sent to the designers.

Under the transparent condition, designers were informed: “To streamline the selection process, we will identify a subset of entries that will be put up for a public vote on our website for three days. Entries receiving at least 20 votes with an average score of 4 or above will form a shortlist for final selection.” Under the opaque condition, designers were told: “Entries with a competitive average score will form a shortlist for final selection.”

This round of experiments consisted of three logo design contests that were sequentially launched on 99designs from March to April 2024. Among the 3,000 invited designers, 311 participated, with 150 in the transparent condition and 161 in the opaque condition. We first conducted a randomization check between the two groups of invited designers, comparing their average characteristics; we observed no statistically significant differences.

We then conducted analyses similar to those in the previous section. As in the prior experiment, we once again found that our opacity intervention exhibited no statistically significant influence on participation.<sup>11</sup> Further, as can be seen in Table 6, we observed effects from the treatment that were directionally consistent with those reported in the first round of contests, finding that the effects specifically on our effort allocation measure (the ratio of illegitimate to legitimate effort) were, once again, statistically significant. That said, we found that, broadly, the magnitude of the observed effects was diminished, relative to those observed in the first experiment, where we employed a more intense form of opacity, which was broader in scope.<sup>12</sup>

These findings indicate that the benefit of opacity in crowd evaluations may increase with the scope or intensity of the obfuscation. It appears that simply making the decision rules opaque (i.e., obfuscating the threshold applied to votes) is sufficient to induce participants to reallocate effort toward more legitimate activities. When both the decision rules and the sources of decision inputs are jointly obfuscated, this results in an even stronger effort shift.

## AMT Controlled Experiment: Brand Name Contests

Our field experiment showed that using an opaque evaluation rule, when associated with other components, can effectively induce more submissions and reduce crowd-vote manipulation. Further, we showed that the latter is particularly true when the level of competition is high. We thus sought to replicate our baseline finding in a more controlled environment (Amazon Mechanical Turk, or AMT), exploring more granular measures of legitimate effort, namely the time contestants spend crafting their submissions.

![](/api/attachments/M9HRECXE/fulltext/images/e1a825afede65f2ecf3e6308bfe286a5f64c188018abae3187523dd52b09d1d9.jpg)

<table><tr><td colspan="6">Table 6. Field Experiment: Threshold Opacity Treatment Effect on Effort Allocation</td></tr><tr><td rowspan="2">Variables</td><td>(1) OLS</td><td>(2) Log-OLS</td><td>(3) Log-OLS</td><td>(4) Log-OLS</td><td>(5) Log-OLS</td></tr><tr><td>Effort ratio</td><td>Effort ratio</td><td>NVS</td><td>MNVO</td><td>NS</td></tr><tr><td>Opaque condition</td><td>-1.88** (0.94)</td><td>-0.20* (0.11)</td><td>-0.20 (0.13)</td><td>-0.60 (0.07)</td><td>-0.04 (0.06)</td></tr><tr><td>Constant</td><td>4.18*** (0.68)</td><td>0.77*** (0.08)</td><td>0.94*** (0.09)</td><td>0.32*** (0.05)</td><td>1.19*** (0.04)</td></tr><tr><td>Observations</td><td>311</td><td>311</td><td>311</td><td>311</td><td>311</td></tr><tr><td>F-test</td><td>3.97</td><td>3.08</td><td>2.45</td><td>0.69</td><td>0.56</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

## WHAT WE ARE DOING:

We are a market research firm currently helping several of our clients create brand names for the new products they are planning to launch soon. Studies have shown the best ideas often come from the crowds. As a result, we are soliciting suggestions for brand names that are simple, memorable, and original. Brief descriptions of each product (5 in total) will be provided on the next page.

After we collect a number of submissions, a crowd-based voting process will take place concurrently on a separate site. The voting site will be shared with you at the end. Your own suggestions will be posted there in 1-2 minutes after you submit. You are also welcome to participate in voting the brand names you love!

A panel of research associates will closely monitor the submissions. To streamline the final selection process, brand names receiving less than three votes within the first 6 hours will be dropped from the contest. Once the voting period ends (in 24 hours), we will then choose two finalists for each product and the corresponding authors will each receive a \$25 bonus payment via Amazon Mechanical Turk!

Figure 3a. AMT Experiments: Introduction Page, Transparent Condition

## WHAT WE ARE DOING:

We are a market research firm currently helping several of our clients create brand names for the new products they are planning to launch soon. Studies have shown the best ideas often come from the crowds. As a result, we are soliciting suggestions for brand names that are simple, memorable, and original. Brief descriptions of each product (5 in total) will be provided on the next page.

After we collect a number of submissions, a crowd-based voting process will take place concurrently on a separate site. The voting site will be shared with you at the end. Your own suggestions will be posted there in 1-2 minutes after you submit. You are also welcome to participate in voting the brand names you love

A panel of research associates will closely monitor the submissions. To streamline the final selection process, a number of submissions will be dropped within the first 6 hours. Multiple factors will be used to determine if a brand name stays in the contest, including an independent evaluation of the quality of the proposed brand names (e.g., creativity, match with client reguirement) by the research associates and the number of votes received on the voting site, Once the voting period ends (in 24 hours), we will then choose two finalists for each product and the corresponding authors will each receive a \$25 bonus payment via Amazon Mechanical Turk!

Figure 3b. AMT Experiments: Introduction Page, Opaque Condition

## Experimental Design

Given that AMT workers are less likely to specialize in graphic design, the second experiment involved a crowdsourced ideation contest to solicit brand names for five (artificial) new products: a yoga exercise ball, green tea, a product line of kids’ eco-friendly toys, wireless headphones, and a cooking app. Each worker was allowed to submit up to five brand name suggestions (one per product) but had to submit at least one suggestion to receive their base pay (\$2) for the task. The final winners each received additional compensation in the form of a \$25 AMT bonus payment.

On the contest introduction page, we informed the workers that all brand name suggestions would be automatically entered into a concurrent crowd-based voting process on a separate site. The voting link was provided at the end of the task, and the brand names were posted on the voting site within one to two minutes of submission. Like the second round in the field experiment, the evaluation rule acted as a screening mechanism to quickly filter or eliminate low-quality submissions (in this case, within the first six hours). As shown in Figure 3, the same information was presented to all participants on the opening page of the ideation contest, the only difference being the explanation of the filtering rule.

Each participant was randomly assigned to one of the two filtering rules. Under the transparent rule, participants were told: “Brand names receiving less than three votes within the first 6 hours will be dropped from the contest.” Under the opaque rule, participants were told that “a number of submissions” would be dropped based on multiple factors, including the number of votes received and an independent evaluation of the quality of the proposed brand names (e.g., creativity, match with client requirement).

After reading the task introduction, participants proceeded to the product descriptions and brand name requirements before submitting their suggestions. We also collected information about relevant work experience, namely whether they had worked in marketing or branding and whether they had participated in a crowdsourcing contest before. On the final page, workers were reminded about the filtering rule (using the same wording as on the first page, shown in Figure 3) and could choose to click on the hyperlink directing them to the crowd-voting site.

The voting sites were set up in the same fashion as our field experiment. Unbeknownst to the participants, each worker received a link to a unique copy of the voting site, allowing us to directly measure vote manipulation attempts by each worker. The voting sites were set up using Google Forms and updated dynamically every 1 to 2 minutes to incorporate any newly collected brand name submissions from AMT participants, via API. Thus, upon submitting brand name suggestions, workers could see their submissions appear for voting in near real time.

To avoid an overwhelming number of brand name suggestions being displayed on the voting page, we conducted the experiment in waves, with multiple rounds involving 20 to 30 subjects per round (note that the opacity treatment was randomly assigned at the worker level, not the contest level).<sup>13</sup> At the 24-hour mark following the last submission for a round, we stopped accepting new responses and then collected the number of votes entered on each site.

We recruited 285 workers for over 10 rounds. Among them, 48 dropped out after the first page. The remaining 237 participants (119 under the transparent rule and 118 under the opaque rule) completed the experiment, submitting a total of 986 distinct brand name suggestions.

## Data Description and Descriptive Evidence

We considered a few key outcome measures, analogous to those in our field experiment, including whether a worker participated in the contest (i.e., submitted at least one brand name), whether a participant voted for their own submission(s),<sup>14</sup> and whether a participant invested a high level of effort in the brand name submission task. Regarding the effort measures, we counted the number of self-votes to capture the illegitimate effort of cheating and computed the average time spent per brand name as a measure of legitimate effort.<sup>15</sup> Specifically, high effort is defined as the average time spent per brand name falling in the top quartile (2.16 minutes).<sup>16</sup> The key independent variable of interest was a binary indicator reflecting subjects’ random assignment to the opacity (versus transparency) treatment. Table 7 presents the definitions of these variables, and Table 8 reports their mean comparisons between the experimental conditions.

Broadly, we observed descriptive results consistent with our field experiments. The average time and effort dedicated to the task were higher in the opaque condition (though these differences were not statistically significant). Further, subjects assigned to the transparent condition were significantly more likely to vote for their own submission(s) (??-value = 0.012)<sup>17</sup> and voted 0.8 times more, on average (p-value = 0.048). Thus, transparent evaluation rules have no material effect on participation but induce more time and effort in gaming, at the expense of legitimate effort. We further estimated more nuanced regression models that considered workers’ joint decision-making process.

<table><tr><td colspan="2">Table 7. AMT Experiment: Variable Descriptions</td></tr><tr><td>Variable</td><td>Description</td></tr><tr><td>Participation</td><td>A binary indicator, equals 1 if a subject submitted at least one brand name</td></tr><tr><td>VoteSelf (VS)</td><td>A binary indicator, equals 1 if a subject voted on their own submission(s)</td></tr><tr><td>HighEffort (HE)</td><td>A binary indicator, equals 1 if a subject invested high effort in submitting brand name(s)</td></tr><tr><td>NumVoteSelf (NVS)</td><td>A count measure, the number of votes a participant submitted on their own submission(s)</td></tr><tr><td>AvgTimeSpent (AvgTime)</td><td>The average time a subject spent on submitting one brand name, in minutes</td></tr></table>

was then computed as the total time spent on the page divided by the number of submitted brand names. Alternative measures of the workers’ legitimate effort were also considered: i.e., the number of brand names submitted by each participant and the total time spent on the submission page. The key findings reported in the next section are largely qualitatively unchanged. <sup>16</sup> For those who exited the experiment without submitting any brand names, we treated their time spent on submissions and the number of submissions as zeros.

<table><tr><td colspan="6">Table 8. AMT Experiment: Manipulation Comparisons</td></tr><tr><td></td><td>Variable</td><td>Transparent</td><td>Opaque</td><td>t-statistics</td><td>p-value</td></tr><tr><td rowspan="2">Recruited workers</td><td>N_obs</td><td>142</td><td>143</td><td></td><td></td></tr><tr><td>Participation (percentage)</td><td>83.80%</td><td>82.52%</td><td>0.29</td><td>0.39</td></tr><tr><td rowspan="5">Participants</td><td>N_obs</td><td>119</td><td>118</td><td></td><td></td></tr><tr><td>VS (percentage)</td><td>42.02%</td><td>27.97%</td><td>2.27</td><td>0.012</td></tr><tr><td>HE(percentage)</td><td>29.41%</td><td>30.51%</td><td>-0.18</td><td>0.43</td></tr><tr><td>NVS (mean)</td><td>2.15</td><td>1.39</td><td>1.67</td><td>0.048</td></tr><tr><td>AvgTimeSpent (mean)</td><td>1.90</td><td>2.35</td><td>-0.95</td><td>0.17</td></tr></table>

<table><tr><td colspan="5">Table 9. AMT Experiment: Estimation Results of the Multinomial Choice Model</td></tr><tr><td rowspan="2"></td><td colspan="4">Decision choice</td></tr><tr><td>NP</td><td>P_HE_VS</td><td>P_LE_VS</td><td>P_LE_NVS</td></tr><tr><td>Opaque condition</td><td>-0.404 (0.450)</td><td>-0.914* (0.494)</td><td>-0.928** (0.453)</td><td>-0.351 (0.390)</td></tr><tr><td>Wkdy</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>-14.169*** (0.293)</td><td>-0.276 (0.747)</td><td>-0.677 (0.848)</td><td>0.472 (0.581)</td></tr><tr><td>Observations</td><td colspan="4">285</td></tr><tr><td>Log likelihood</td><td colspan="4">-408.628</td></tr><tr><td>AIC</td><td colspan="4">865.255</td></tr><tr><td>LR test</td><td colspan="4">31.767 (df = 24)</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01. The reference decision choice is P\_HE\_NVS.

## Empirical Approach and Results

To examine the trade-offs that workers make between participation, the legitimate effort to invest, and the effort to invest in manipulation under opaque versus transparent evaluation rules, we estimated a multinomial logit regression. Specifically, a worker, i, could choose among five alternatives: (1) to not participate (“NP”); or, if choosing to participate, (2) to invest high effort in both providing submissions and manipulating votes by voting for their own submission(s) (“P\_HE\_VS”); (3) to invest high effort in providing submissions but not in manipulating votes (“P\_HE\_NVS”); 4) to invest low effort in providing submissions and manipulating votes (“P\_LE\_VS”); or (5) to invest low effort in providing submissions and not manipulate votes $( { } ^ { 6 6 } P \_ L E \_ N V S ^ { 3 } )$ . This model provides a structural interpretation of the estimates from a discrete choice utility maximization framework. However, we acknowledge that the model assumes that workers make all three decisions (whether to participate in the contest, whether to invest a high/low level of effort in providing submissions; whether to manipulate votes) simultaneously. This is a reasonable reflection of the workers’ decision process because all three choices were presented to the workers on the first page of the experiment introduction page (Figure 3).

The probability of worker i choosing alternative j is assumed to take the following form:

$$
P r (C h o i c e _ {i} = j) = \frac {e x p (\alpha_ {j} + \beta_ {j} T r e a t _ {i} + \gamma_ {j} W k d y _ {i})}{\sum_ {k \in J} e x p (\alpha_ {k} + \beta_ {k} T r e a t _ {i} + \gamma_ {k} W k d y _ {i})} \forall j \in J,\tag{3}
$$

where the choice set $J = \{ N P , P \_ H E \_ V S , P \_ H E \_ N V S , P \_ L E \_$ 2 ????, ??\_????\_??????} and $T r e a t _ { i }$ is a binary indicator of the experimental condition, which equals 1 if worker i was exposed to the opaque filtering rule and 0 under the transparent rule. We also included controls for the day of week that worker i entered the experiment $( ^ {  } W k d y _ { i } ^ {  } )$ , to account for possible shifts in participant composition over time on AMT.

Table 9 reports our results, taking the high-effort/nomanipulation (“P\_HE\_NVS”) option (the ideal behavior) as reference. Relative to subjects exposed to a transparent evaluation rule, we observed that subjects exposed to an opaque rule were significantly less likely to engage in manipulation (“P\_LE\_VS”, “P\_HE\_VS”). Further, we observed that strategic opacity was associated with a reduced incidence of low-effort, non-gaming responses $( { } ^ { 6 6 } P \_ L E \_ N V S ^ { 3 } )$ , and a reduction in non-participation responses $\big ( \mathrm { \sp { 6 6 } } N P \mathrm { \sp { 3 7 } } \big ) .$ , relative to the reference choice (“P\_HE\_NVS”), which is consistent with our field experiment—though neither estimate is statistically significant at conventional thresholds. In general, we observed a pattern of results consistent with our field experiment.

## Discussion & Conclusion

Employing a series of experiments, we explored the impact of employing strategic opacity in creative crowdsourcing as a means of mitigating the gaming and manipulation of crowdvoting processes and encouraging greater legitimate effort from contestants. Our results provide consistent evidence that opaque evaluation rules reduce illegitimate effort in favor of legitimate effort without a significant effect on participation. We show that these benefits are particularly pronounced in highly competitive contests and when the scope of obfuscation is broader.

Our finding that strategic opacity not only curtails gaming but also enhances the quality of crowd work complements prior findings in the literature. Burtch et al. (2021) showed that quality assurance processes in crowd-work have less influence on the market when the work is creative in nature. Burtch et al. demonstrated that because they lack confidence that the platform operator will agree with their evaluation of work quality, employers on Freelancer.com place more weight on workers’ reputation and ratings when hiring for creative tasks. Under strategic opacity, submitters do not need to place as much trust in third-party evaluations, and our findings suggest that contestants prefer this scenario.

Our work is subject to some limitations. Most notably, to examine the effect of strategic opacity on both participation and designers’ effort allocation, we performed randomized assignment at the invitation stage rather than at the participation stage. Given the design, it is important to note that selection bias may have influenced our estimates of effort allocation decisions, as these outcomes were only observed conditional on the decision to participate. We took several measures to mitigate this possibility<sup>18</sup> in order to optimize the comparability of the treatment and control groups. Nonetheless, future research could seek to address this issue by modifying the experimental design, implementing a randomized treatment following contestants’ participation decision.

Our findings also suggest opportunities for future work. For example, future research could explore how different contextual factors, such as the cost and visibility of gaming behaviors, may interact with strategic opacity. Further, our experiments indicate that opacity in this setting does not meaningfully deter participation. However, additional work is needed to understand how explicitly stating the rationale for opacity might influence effort and participation, particularly among low-ability agents, who may be most likely to cease participating in the absence of clear evaluation rules.

## Acknowledgments

We are grateful to the anonymous reviewers and editors for their insightful comments and constructive feedback, which have greatly improved this paper. We also appreciate the valuable suggestions provided by participants at the 42nd ISMS Marketing Science Conference and the 31st POMS Annual Conference. This research was supported in part by the Dean’s Small Research Grant from the Carlson School of Management at the University of Minnesota and the National Natural Science Foundation of China (Grants 72442017 and 722372140).

## References

Aral, S. (2014). The problem with online ratings. MIT Sloan Management Review, 55(2), 47. https://sloanreview.mit.edu/ article/the-problem-with-online-ratings-2/

Athey, S., & Imbens, G. W. (2017). The econometrics of randomized experiments. In Handbook of economic field experiments (Vol. 1, pp. 73-140). North-Holland.

Baker, G., Gibbons, R., & Murphy, K. J. (1994). Subjective performance measures in optimal incentive contracts. The Quarterly Journal of Economics, 109(4), 1125-1156. https://doi.org/10.2307/2118358

Basu, A., Bhaskaran, S., & Mukherjee, R. (2019). An analysis of search and authentication strategies for online matching platforms. Management Science, 65(5), 2412-2431. https://doi.org/10.1287/ mnsc.2018.3056

Benson, A. (2015). Do agents game their agents’ behavior? Evidence from sales managers. Journal of Labor Economics, 33(4), 863-890. https://doi.org/10.1086/681107

Boudreau, K. J., Lacetera, N., & Lakhani, K. R. (2011). Incentives and problem uncertainty in innovation contests: An empirical analysis. Management Science, 57(5), 843-863. https://doi.org/10.1287/ mnsc.1110.1322

Boudreau, K. J., Lakhani, K. R., & Menietti, M. (2016). Performance responses to competition across skill levels in rank‐order tournaments: field evidence and implications for tournament design. The RAND Journal of Economics, 47(1), 140-165. https://doi.org/10.1111/1756-2171.12121

Burtch, G., Hong, Y., & Kumar, S. (2021). When does dispute resolution substitute for a reputation system? Empirical evidence from a service procurement platform. Production and Operations Management, 30(6), 1565-1582. https://doi.org/10.1111/poms. 13341

Charness, G., Masclet, D., & Villeval, M. C. (2014). The dark side of competition for status. Management Science, 60(1), 38-55. https://doi.org/10.1287/mnsc.2013.1747

Chen, L., Xu, P., & Liu, D. (2020). Effect of crowd voting on participation in crowdsourcing contests. Journal of Management Information Systems, 37(2), 510-535. https://doi.org/10.1080/0742 1222.2020.1759342

Courty, P., & Marschke, G. (2004). An empirical investigation of gaming responses to explicit performance incentives. Journal of Labor Economics, 22(1), 23-56. https://doi.org/10.1086/380402

Ederer, F., Holden, R., & Meyer, M. (2018). Gaming and strategic opacity in incentive provision. The RAND Journal of Economics, 49(4), 819-854. https://doi.org/10.1111/1756-2171.12253

Fradkin, A., Grewal, E., & Holtz, D. (2021). Reciprocity and unveiling in two-sided reputation systems: Evidence from an experiment on

Airbnb. Marketing Science, 40(6), 1013-1029. https://doi.org/ 10.1287/mksc.2021.1311

Gibbs, M. J., Merchant, K. A., Van der Stede, W. A., & Vargus, M. E. (2005). The benefits of evaluating performance subjectively. Performance Improvement, 44(5), 26-32. https://doi.org/10.1002/ pfi.4140440508

Gibbs, M., Merchant, K. A., Van der Stede, W. A., & Vargus, M. E. (2004). Determinants and effects of subjectivity in incentives. The Accounting Review, 79(2), 409-436. https://doi.org/10.2308/accr. 2004.79.2.409

Gill, D., Prowse, V., & Vlassopoulos, M. (2013). Cheating in the workplace: An experimental study of the impact of bonuses and productivity. Journal of Economic Behavior & Organization, 96, 120-134. https://doi.org/10.1016/j.jebo.2013.09.011

Greenstein, S., Gu, G., & Zhu, F. (2021). Ideology and composition among an online crowd: Evidence from Wikipedians. Management Science, 67(5), 3067-3086. https://doi.org/10.1287/ mnsc.2020.3661

He, S., Hollenbeck, B., Overgoor, G., Proserpio, D., & Tosyali, A. (2022). Detecting fake-review buyers using network structure: Direct evidence from Amazon. PNAS, 119(47), Article e2211932119. https://doi.org/10.1073/pnas.2211932119

Hu, N., Zhang, J., & Pavlou, P. A. (2009). Overcoming the J-shaped distribution of product reviews. Communications of the ACM, 52(10), 144-147. https://doi.org/10.1145/1562764.1562800

Huang, Y., Singh, P. V., & Srinivasan, K. (2014). Crowdsourcing new product ideas under consumer learning. Management Science, 60(9), 2138-2159. https://doi.org/10.1287/mnsc.2013.1879

Kamar, E., & Horvitz, E. (2012, June). Incentives for truthful reporting in crowdsourcing. In Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems. https://dl.acm.org/doi/10.5555/2343896.2343988

Kleinberg, J., & Raghavan, M. (2020). How do classifiers induce agents to invest effort strategically? ACM Transactions on Economics and Computation, 8(4), 1-23. https://doi.org/10.1145/3417742

Lazear, E. P. (1989). Pay equality and industrial politics. Journal of Political Economy, 97(3), 561-580. https://doi.org/10.1086 261616

Luca, M., & Zervas, G. (2016). Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Science, 62(12), 3412-3427. https://doi.org/10.1287/mnsc.2015.2304

Malone, T. W., Laubacher, R., & Dellarocas, C. (2010). The collective intelligence genome. MIT Sloan Management Review. https://sloanreview.mit.edu/article/the-collective-intelligencegenome/

Mayzlin, D., Dover, Y., & Chevalier, J. (2014). Promotional reviews: An empirical investigation of online review manipulation. American Economic Review, 104(8), 2421-2455. https://doi.org 10.1257/aer.104.8.2421

Mukherjee, A., Xiao, P., Wang, L., & Contractor, N. (2018). Does the opinion of the crowd predict commercial success? Evidence from Threadless. In Academy of Management Proceedings. https://doi.org/10.5465/ambpp.2018.12728abstract

Ott, M., Cardie, C., & Hancock, J. T. (2013). Negative deceptive opinion spam. In Proceedings of the Conference of the North

American Chapter of the Association for Computational Linguistics: Human Language Technologies (pp. 497-501).

Rahman, H. A. (2021). The invisible cage: Workers’ reactivity to opaque algorithmic evaluations. Administrative Science Quarterly, 66(4), 945-988. https://doi.org/10.1177/00018392211010118

Schwieren, C., & Weichselbaumer, D. (2010). Does competition enhance performance or cheating? A laboratory experiment. Journal of Economic Psychology, 31(3), 241-253. https://doi.org/ 10.1016/j.joep.2009.02.005

Takahashi, S., Owan, H., Tsuru, T., & Uehara, K. (2021). Multitasking incentives and the informative value of subjective performance evaluations. ILR Review, 74(2), 511-543. https://doi.org/10.1177/ 0019793919891980

Wang, Q., Huang, Y., Jasin, S., & Singh, P. V. (2023). Algorithmic transparency with strategic users. Management Science, 69(4), 2297-2317. https://doi.org/10.1287/mnsc.2022.4475

Yang, G., Cavaliere, M., Zhu, C., & Perc, M. (2021). Strategically positioning cooperators can facilitate the contagion of cooperation. Scientific Reports, 11(1), Article 1127. https://doi.org/10.1038/ s41598-020-80770-8

Young, A. (2019). Channeling Fisher: Randomization tests and the statistical insignificance of seemingly significant experimental results. The Quarterly Journal of Economics, 134(2), 557-598. https://doi.org/10.1093/qje/qjy029

Zhang, S., Singh, P. V., & Ghose, A. (2019). A structural analysis of the role of superstars in crowdsourcing contests. Information Systems Research, 30(1), 15-33. https://doi.org/10.1287/isre.2017.0767

Ziewitz, M. (2019). Rethinking gaming: The ethical work of optimization in web search engines. Social Studies of Science, 49(5), 707-731. https://doi.org/10.1177/0306312719865607

Zuo, X., Gandy, C., Skvoretz, J., & Iamnitchi, A. (2016). Bad apples spoil the fun: Quantifying cheating in online gaming. In Proceedings of the International AAAI Conference on Web and Social Media, 10(1), 496-505. https://doi.org/10.1609/icwsm.v10i1.14745

## About the Authors

Linli Xu joined the Carlson School of Management, University of Minnesota in 2012, after receiving a Ph.D. from the University of Southern California. Her research interests focus on advertising and digital platforms and specialize in the automotive market. Her work has been published in Marketing Science, Management Science, Quantitative Marketing and Economics, and Journal of Marketing. Xu was named a Young Scholar by the Marketing Science Institute (MSI) in 2019, a biennial award given to the most promising scholars in marketing and closely related fields whose work suggests they are potential leaders of the next generation of marketing academics. Her research was funded by an MSI grant and the Carlson School Dean’s Small Research Grant. While at USC, she was awarded the 2010 James S. Ford/Commerce Associate PhD Fellowship in recognition of her outstanding scholastic achievement and research. Linli Xu holds a B.A. in economics from Jilin University (China) and an M.A. in economics from the University of British Columbia (Canada).

Qi Xie is an assistant professor of marketing at the Oregon State University College of Business. Before joining Oregon State University, she received a bachelor’s degree in economics from Peking University, an M.S. in business analytics from the University of Rochester, and a Ph.D. in business administration from the University of Minnesota. Qi’s research mainly focuses on understanding user behavior on digital platforms to derive insights that can guide platform designs. In her work, Qi employs a combination of methodologies, including econometric modeling, difference-in-difference estimators, and field experiments.

Gordon Burtch is the Allen and Kelli Questrom Professor in Information Systems at Boston University’s Questrom School of Business. His primary research interests pertain to the design, management, and consequences of digital platforms and associated technologies. His work has been published in several leading academic outlets (PNAS, Science Advances, Management Science, and Harvard Business Review, among others), cited by numerous outlets in the popular press (The New York Times, The Wall Street Journal, Los Angeles Times, TIME Magazine, Wired), and funded with more than \$2 million by various private and non-profit entities (NSF, Kauffman Foundation, Meta, Adobe, Microsoft). Gordon is a past recipient of the Best Paper, Best Reviewer, and Best Associate Editor (×2) awards from Information Systems Research, the Best Associate Editor award from Management Science’s IS Desk, and the AIS and INFORMS ISS Early Career awards. He holds a Ph.D. in business administration from Temple University’s Fox School of Business and M.B.A. and bachelor’s of engineering degrees from McMaster University. Before entering academia, Gordon worked as a hardware design engineer, an IT systems auditor, and, most recently, a technology consultant with Accenture Canada. He is currently employed as a consulting researcher by Meta, a role he previously held with Microsoft.
