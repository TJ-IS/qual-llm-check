---
otero_id: 9432
otero_key: "WSCU4Q7J"
title: "How are C-suite executives different? A comparative empirical study of the survival of American chief information officers"
authors: "Gregory S. Dawson; Man-Wai Ho; Robert J. Kauffman"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.03.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How are C-suite executives different? A comparative empirical study of the survival of American chief information of<sup>fi</sup>cers

Gregory S. Dawson <sup>a,</sup>⁎, Man-Wai Ho <sup>b</sup>, Robert J. Kauffman <sup>c</sup>

<sup>a</sup> Department of Information Systems, W.P. Carey School of Business, Arizona State University, United States

<sup>b</sup> Department of Mathematics and Statistics, Hang Seng Management College, Hong Kong, China

<sup>c</sup> School of Information Systems, Singapore Management University, Singapore

## a r t i c l e i n f o

Article history: Received 10 July 2012 Received in revised form 15 February 2015 Accepted 19 March 2015 Available online 27 March 2015

Keywords: CIO Job tenure Kaplan–Meier estimator Non-parametric estimation Parametric survival model Proportional hazards model

## a b s t r a c t

This research employs non-parametric, semi-parametric, and parametric survival analysis methods to explore theory-based aspects of CIO and other C-suite executives' job tenures. We analyze a large data set of C-suite executives, including 400 CIOs, drawn from the public and private sectors, including federal, state, county and city agencies, and Fortune 500 <sup>fi</sup>rms. The data span 1994 to 2009, and include the job start and <sup>fi</sup>nish dates of the different executives, as well as relevant variables for the individual, organizational, market and technological environments that permit us to assess the patterns of their survivability. We report evidence to suggest that CIOs have more in common regarding survivability with other C-suite executives than is widely believed, We also report differences based on individual characteristics (gender, education, income, time in position), organization type (government versus Fortune 500), organization size, and reactions to changes in the stock market. In addition, CIO job tenures have grown longer from the early 1990s to the present day. Though there are few differences due to CIO gender, the relatively rare presence of female executives is associated with shorter job tenures for male executives.

Published by Elsevier B.V.

## 1. Introduction

Numerous studies have demonstrated how leaders achieve positive organizational outcomes [4,17] and effective leadership can explain 25% to 45% of the variance in organizational performance [44]. The positive impacts of senior executives also apply to the chief information of-<sup>fi</sup>cer (CIO). This is not surprising: an effective CIO can reduce operational costs and inventory cycle time, make supply chain management more effective, and foster development of strategic products and services [41]. Financial markets respect effective CIOs, and there is a link between new private sector CIO position announcements and higher market valuations re<sup>fl</sup>ected in post-announcement stock prices for <sup>fi</sup>rms [12].

Though CIOs create value, their job tenures are believed to be short. Some observers have pointed to the rapidity of technological change as the culprit [43]. This suggests other executives – chief executive of<sup>fi</sup>cers (CEOs), chief <sup>fi</sup>nancial of<sup>fi</sup>cers (CFOs) and chief operating of<sup>fi</sup>cers (COOs) – are somehow immune to change. But all leaders face environmental challenges (e.g., declining <sup>fi</sup>nancial markets for the CEO, and Sarbanes–Oxley requirements for the CFO), so it is unlikely that technological change is any more dif<sup>fi</sup>cult to manage for CIOs than change impacting other business functions.

The job tenures of CIOs have been observed to span a wide range of durations, suggesting the importance of their organizational roles and the people in those positions. In 1995, Paul Strassmann [45] estimated the median duration of American CIOs at about 15 months – their halflife as executives, with a 30-month average tenure. For 2002 and 2003, Strassmann estimated the one-year rate of attrition for CIOs at about 21% to 34% [46]. In contrast, Iyengar [21] reported the average CIO job tenure approached 6 years and 8 months based on 107 corporate respondents. In both cases though, the estimated job tenures were solely based on private sector CIOs. Although no studies that we know of have examined CIO tenure relative to organizational performance, there is a plethora of evidence linking longer tenures – up to 7 to 9 years – with positive organizational outcomes [17]. Therein lies our interest for this research.<sup>1</sup>

Our research compares the job tenures of CIOs to other top management team members to reveal and explain differences among and across the public and private sectors. We emphasize survivability, which allows us to compare relative job durations across the positions. This is the <sup>fi</sup>rst empirical study that we are aware of which compares the job tenures of CIOs with other senior executives in an extensive manner. Our goal is not just to establish numbers for median survival, but also to apply theory to understand the reasons for similarities and differences in CIO and other C-suite executives' job tenures.

Table 1  
Key studies comparing government to private industry executive leadership

<table><tr><td>Authors</td><td>Approach and setting</td><td>Findings</td></tr><tr><td>Banfield [6]</td><td>Empirical; federal government and business firms</td><td>Govt.: less authority; admin., personnel processes differ</td></tr><tr><td>Blumenthal [8]</td><td>Empirical; federal government and business executives</td><td>Federal execs: less control; organizations more diverse</td></tr><tr><td>Buchanan [10]</td><td>Empirical; federal government and private firms</td><td>Public mgrs.: weak authority/commitment, more diverse</td></tr><tr><td>Downs [16]</td><td>Theoretical analysis only</td><td>Govt. agencies: bureaucracies, politics, higher rigidity</td></tr><tr><td>Meyer [33]</td><td>Empirical study; state, local</td><td>State, local leaderships conform to higher authorities</td></tr><tr><td>Warwick [53]</td><td>Case study, U.S. State Dept.</td><td>Public orgs. are hierarchical; rules resistant to change</td></tr></table>

Note. Contents adapted from Perry and Rainey [39].

We ask: (1) How does the CIO's survivability compare to other C-suite executives? How are they different? (2) Can we offer an insightful reading of the explanation for the patterns in job tenures that are observed? (3) Are the patterns of executive survival similar for large versus small organizations or for public versus private organizations? (4) How can robust answers to these questions be established? To answer these questions, we apply non-parametric, semi-parametric and parametric methods in survival analysis to new data on senior management job tenures from the U.S. for data from 1994 to 2009.

This article is organized as follows. Section 2 presents relevant theoretical background on C-suite executive job tenures. Section 3 discusses the new data set on C-suite executive job tenures used in this research. It presents empirical regularities results for their survival in different kinds of organizations using pooled data and a non-parametric survival time estimator. Section 4 extends the empirical analysis through the use of semi-parametric and fully-parametric survival models, which involve the estimation of models that aim to provide explanations for the observed empirical regularities. Section 5 discusses and interprets the key <sup>fi</sup>ndings, and Section 6 concludes with the contributions and limitations of this research.

## 2. Theoretical background

Executive jobs involve leadership, which is the use of non-coercive methods to manage the activities of members in a group to achieve common goals [31]. Effective leadership improves performance through critical organizational outcomes: quality, innovation, pro<sup>fi</sup>t, and ethics. Effective leaders typically adopt systems and technical processes required for high performance [4]. However, achievement of high performance often depends on environmental characteristics that affect the organization, the market and its customers, and different kinds of leadership may be successful as a result.

2.1. Why executive job tenures might be influenced by public versus private sector posting

Inattention to sector differences leads to false conclusions about how management can be effective, and some have suggested that the distinctive characteristics of the public sector can be set aside [9,33,39]. However, others have argued that public sector management is different though, and so it is important to distinguish between public and private sector organizations [6,8,16]. (See Table 1.)

2.2. Why executive job tenures may be different for different executive types and genders

## 2.2.1. Executive types

We noted that CIOs are believed to have shorter tenures than other leaders due to the complexity of managing rapidly evolving technology. This idea is underlain with the belief that technology is more dif<sup>fi</sup>cult to manage than other business functions, but there have been no empirical studies to date that support this view. What may be true is that CIOs, in the course of implementing large projects, experience unacceptable failure rates, and this leads to poor performance and termination [35].<sup>2</sup>

Project success may also be a source of CIO turnover, however. Firms may be able to achieve competitive advantage when they have valuable, rare, inimitable and non-substitutable resources, for example, effective information systems [51]. Additionally, IS managerial skills may provide the organization with a competitive advantage [29,40]. Thus, other organizations may try to poach a successful CIO, though, increasing executive turnover and decreasing their survival times with speci<sup>fi</sup>c organizations.

## 2.2.2. Gender

Another relevant issue to consider is gender differences. Some argue that women and men in the top management team are similar in key personal and professional characteristics, so gender differences are not critical [2]. The con<sup>fl</sup>icting viewpoint is that men and women have differentiated skill sets that lead to gender differences in promotion, performance, and pay [36]. This, it has been argued, explains higher female turnover in periods of instability and change, and such gender differences are more often seen in the private sector than in public sector IS workplaces [26].

Despite strides by women into the boardroom, few have made it to the executive suite.<sup>3,</sup> <sup>4</sup> Although a number of <sup>fi</sup>rms have launched initiatives to increase the number of female executives, most have failed to produce results. This failure has been linked to unsupportive corporate cultures. A McKinsey [30] study reported that corporate culture is twice as important as a female executive's personal assessment of whether she can be successful – though this view varies based on educational level [5,22].

2.3. Why job tenures may be influenced by environmental turbulence and organization size

## 2.3.1. Turbulence

Executives represent the <sup>fi</sup>rm in its external environment and environmental turbulence re<sup>fl</sup>ects the unpredictability of the environment in which they operate [38]. Internal turbulence, like Steve Jobs' death, affects one organization only, while external turbulence like terrorism may affect many organizations at the same time. Turbulence can be recurring or unexpected and may be rising (positive), falling (negative) or stationary (neutral), and it may be proxied by stock market performance.

Different types of turbulence affect CIOs. When turbulence is positive (as in times of general economic growth), CEOs search for other skilled C-suite executives and offer them higher salaries to change jobs. This may open up employment opportunities and increase the probability that they will leave, thus decreasing survival. Negative turbulence (e.g., when interest rates rise) should have the opposite effect. There are fewer jobs available and fewer opportunities to leave, thus lengthening survival. So more turnover should occur in periods of positive turbulence and less with neutral or negative turbulence.

Table 2  
Descriptive statistics for the C-suite executives data set.

<table><tr><td>Variables</td><td>All executives</td><td>CIOs only</td></tr><tr><td>Population</td><td>1784 (544 CEO, 407 COO,433 CFO, 400 CIO)</td><td>400</td></tr><tr><td>OrgType</td><td>States: 856; Fed: 398; F500: 389; Cty: 141</td><td>States: 171; Fed: 83; F500: 107; Cty: 39</td></tr><tr><td>Gender</td><td>Males: 1357; females: 427</td><td>Males: 305; females: 95</td></tr><tr><td>OrgSize</td><td>Small: 444; medium: 450; large: 890</td><td>Small: 78; medium: 103; large: 219</td></tr><tr><td>Duration (years)</td><td>Min: 1; median: 3; max: 30</td><td>Min: 1; median: 3; max: 25</td></tr><tr><td>Turbulence (stock market index)</td><td>Min: -51%; median: 3%; max: 25%</td><td>Min: -51%; median: 3%; max: 25%</td></tr><tr><td>DepartEpoch</td><td>Early: 256; middle: 409; late: 1109</td><td>Early: 50; middle: 93; late: 238</td></tr><tr><td>FemaleLeaders</td><td>None: 317; low: 557; med: 543; high: 336</td><td>None: 78; low: 128; med: 115; high: 78</td></tr><tr><td># Executives by Start Year</td><td>Pre-1994: 337; 1995–1999: 509; 2000–2004: 508; 2005–2009: 430</td><td>Before 1994: 62; 1995–1999: 113; 2000–2004: 123; 2005–2009: 102</td></tr><tr><td># Executives by Leave Year</td><td>Pre-1994: 19; 1995–1999: 324; 2000–2004: 449; 2005–2009: 992(a)</td><td>Before 1994: 2; 1995–1999: 60; 2000–2004: 98; 2005–2009: 240(a)</td></tr></table>

Note. Cty = cities, counties; F500 = Fortune 500 <sup>fi</sup>rms. <sup>(a)</sup>Some data were right-censored in 2005 to 2009: some executives remained in their positions. There were publicized involuntary turnover events: one CIO was terminated for falsifying his background; another was terminated due to allegations of bribery.

## 2.3.2. Organization size

To our knowledge, no studies have compared CIO turnover in organizations of different sizes. Yet there is evidence at the staff level of a strong relationship between organization size and turnover, which decreases as the size of an organization increases [55]. Another consideration is the source of C-suite executives for large organizations. Few large organizations would be willing to hire senior executives who lack proven capabilities in leadership – a quali<sup>fi</sup>cation that they can obtain through service to a smaller <sup>fi</sup>rm [47,48]. Thus, becoming a CIO at a small or a medium-sized organization may provide a steppingstone for a CIO who wants to be an executive in a large organization. As a result, there may be shorter tenures for CIOs at small and mediumsized organizations.

## 3. Results I: non-parametric analysis of executive job tenures

We next describe the research context and analyze the data using non-parametric methods. (For the modeling approaches and methods that we used and analysis that we performed, see Appendix A.)

## 3.1. The research context and data

The sample included 1784 CEOs, COOs, CFOs, and CIOs, with 400 CIOs, with data for federal, state and county government leaders, and Fortune 500 executives. (See Table 2).

Our data span 15 years from 1994 to 2009 for male and female C-suite executives in small, medium, and large organizations.<sup>5</sup> The term CIO <sup>fi</sup>rst appeared in the late 1980s, but was not widely used until the mid-1990s [14] and this led us to choose 1994 as our start date. The executives worked from 1 to 30 years, with a median of 3 years prior to departure.<sup>6</sup> The data include executive start and departure dates, and we identi<sup>fi</sup>ed several epochs into which these dates are classi<sup>fi</sup>ed. We excluded a number of observations for various reasons, which resulted in a data set of 1628 data points for analysis. (See Appendix B for a summary of the coding of our variables, organization descriptions and data issues.)

While the private sector typically identi<sup>fi</sup>es the CEO, COO, CFO, and CIO as members of the top management team, the public sector uses other titles, and it makes more sense to identify what has been called the dominant coalition [15]. The dominant coalition identi<sup>fi</sup>es the equivalent executives in government, including the Agency Director (CEO), Director of Administration (COO), Chief Budget Of<sup>fi</sup>cer (CFO), and the CIO. The roles represent the individuals who form its interface, and who are powerful in the organization's operations, and thus they parallel the executives within the private sector.<sup>7</sup>

## 3.2. Non-parametric survival analysis via the Kaplan–Meier (KM) estimator

Survival analysis is widely used in public health [25] and other areas. Medical researchers study the lifespan of patients, economists study unemployment, and operations managers model the incidence of operational breakdowns with it. IS researchers study artist survival on the music charts [7], outsourcing contract duration [18], and product adoption involving viral contagion and homophily on Facebook [3].

The occurrence of a focal event is of interest in this research: the departure of an executive from a <sup>fi</sup>rm. Because different executives chose to leave their positions at different types, survival analysis emphasizes the duration of time leading up to an executive's departure. If an executive has not departed by the end of the observation timeline, then it is right-censored. The survival function identi<sup>fi</sup>es the probability that the event will occur by some time, for example, the end of Year 1. Failure events can be explained in this way.

We de<sup>fi</sup>ne duration as the number of years between an executive's start and end years in a position in an organization. An event occurs when the executive exits his or her current position. Executives who remain in their position at the end of the study period are right-censored. Since we know the start date of all the executives, we do not have any left-censored data. The methods permit us to explain the job tenure durations that executives remain in their positions.

Most survival analyses adopt a non-parametric approach. These do not require assumptions about data normality nor do they require speci<sup>fi</sup>c variables or hypotheses to explain the likelihood of failure or the shape of the likelihood function that characterizes failure [32]. Instead, they emphasize the empirical regularities of survival data. The methods also support comparisons via hypothesis tests. They further permit the discovery of useful information about the survival patterns through estimation of pooled and strati<sup>fi</sup>ed samples, based on variables that classify the data in meaningful ways. The Kaplan–Meier (KM) estimator uses observed event times to establish the time to an event of interest [1]. The method plots survival percentages over time, and yields a left-to-right, downward-sloping, step function. KM curves can be compared to identify statistical differences in the patterns of the phenomena under study. They also can be used for further strati<sup>fi</sup>cation analyses, based on the availability of observable variables that an analyst believes are essential drivers of the relevant behavior in the underlying survival process.

Table 3  
C-suite executives' pooled survival estimation results (in years).

<table><tr><td>Survival</td><td>CEO</td><td>COO</td><td>CFO</td><td>CIO</td><td>All</td></tr><tr><td>Mean</td><td>4.35</td><td>3.62</td><td>4.57</td><td>4.32</td><td>3.82</td></tr><tr><td>Std. Dev.</td><td>3.51</td><td>2.85</td><td>3.81</td><td>3.38</td><td>2.79</td></tr></table>

Note. For all executives, the minimum job duration was 1 year and maximum was 15 years.

## 3.3. Baseline results by KM estimator with pooled data on C-suite executives

We analyzed pooled data for all C-suite executives from all organization types, using the KM estimator and log-rank tests. (See Table 3.) The mean duration was 3.82 years for the job tenures of all C-suite executives across all organization types (std. dev. = 2.79 years, min. = 1 year; max. = 15 years). The variation suggests why observers reported divergent estimates for CIO survival and may be related to different reports that were focused on a single sector.

Until the early 1990s, the senior IT person was likely to be viewed either as a data processing manager or was focused on providing information to management. Though valuable to the organization, they had narrow responsibilities. It wasn't until the mid-1990s that the CIO role shifted focus from data processing to enterprise-wide computing strategy, a more strategic role. As a result of this role maturation [37], it is not surprising that CIO survival has come to match the other C-suite executives' survival.

## 3.4. Baseline results by KM estimator, stratified by individual variables

## 3.4.1. Executive type

We strati<sup>fi</sup>ed the data into sub-samples. (See Fig. 1.) We identi<sup>fi</sup>ed differences in the durations by executive type (ExecType). The differences between types were assessed with log-rank comparisons of equality with the Mantel–Cox statistic. COOs had the shortest survival and CFOs the longest (p b .021). Our data did not con<sup>fi</sup>rm that CIOs experienced shorter survival times than other executives. Instead, CIOs had comparable tenures to CEOs and CFOs, and longer survival than COOs.

## 3.4.2. Organization type

We aggregated the government data and compared it to the Fortune 500 data for organization type (OrgType). We found a signi<sup>fi</sup>cant difference (p b .001) between survival in Fortune 500 (5.0 years) and government organizations (3.53 years). We subdivided the government category into federal, states (CA, MA, VA), and cities, counties, and compared them to the Fortune 500 <sup>fi</sup>rms.

We also identi<sup>fi</sup>ed differences between the Fortune 500, and state and Federal governmental entities, but not among the governmental entities. The states (CA, MA, VA) had no signi<sup>fi</sup>cant differences though. C-suite executives in federal government positions had average tenures of 3.38 years, while the state and city–county counterparts had average tenures of 3.43 and 4.44 years. (See Fig. 1.) This suggests the importance of considering the government organization-private firm divide in executive studies. Transferring best practices from the private to public sector may be problematic, given the differences in leader survival though.

## 3.4.3. Departure epoch

We also compared turnover by departure epoch (DepartEpoch). We found a statistically signi<sup>fi</sup>cant difference (p b .001) for executives who left between 1994 and 1999 (2.37 years), between 2000 and 2004 (3.56 years), and between 2005 and 2008 (4.91 years). 1994 to 1999 were years of rising opportunities in a growth economy, with many start-ups. In contrast, 2000 to 2004 were marked by a downturn in the high-tech economy. Then, 2006 to 2008 were years of economic growth, with industry changes that may explain the longer executive job tenures.

Concurrently, a generational shift of C-suite job tenures appears to have occurred and all executives seem to have remained in their positions longer.

## 3.4.4. Gender

We next compared turnover by gender for men and women (Gender), and found no signi<sup>fi</sup>cant difference between the tenures of female (3.70 years) and male leaders (3.87 years). Although men appear to have had very slightly longer survival times, our gender parity results suggest that there may be no need to treat men and women differently in survival studies of executive leadership. For this reason, we will no longer consider Gender in our subsequent semi-parametric and parametric analyses.

## 3.4.5. Female leadership

We further compared executive turnover based on the extent of female leaders (FemaleLeaders) in different organizations, and found signi<sup>fi</sup>cant differences (p b .001) among them, with a high (3.65 years), medium (3.42 years), or low level (3.69 years) of female leadership, in comparison to no female leadership (5.22 years). (See Fig. 1.) The data are unmistakable in suggesting that male executives in organizations with no female leaders during 1994 to 2008 had much longer job tenures than organizations with a low, medium or high extent of female leadership. This group with no females in leadership covers 302 organizations, roughly the same number as 355 others with a high extent of female leadership. So we cannot claim that a small number of <sup>fi</sup>rms with no female leaders skewed the results.<sup>9</sup>

## 3.4.6. Organization size

We compared survival by organization size (OrgSize) and found signi<sup>fi</sup>cant differences also (p b .001). C-suite executives stayed longest at small organizations (4.19 years), a shorter time at large organizations (4.03 years), and a much shorter time at medium-size organizations (3.09 years). Medium-sized organizations acted as stepping-stones for executives who sought larger organizations to lead [48]. They probably were paid more, so there would have been greater <sup>fi</sup>nancial bene<sup>fi</sup>ts for moving to a large organization. A leader also may have understood that his or her skills were better suited for larger organizations, while those who were suited to smaller ones likely joined and stayed with them instead.

## 3.4.7. Environmental turbulence

We compared the impacts of environmental turbulence (Turbulence) based on yearly stock market returns on C-suite executives' job tenures and observed signi<sup>fi</sup>cant differences (p b .001). Their survival was the longest during years with negative turbulence (4.56 years), shorter with neutral turbulence (4.05 years) and the shortest with positive turbulence (3.32 years). If the economy was growing, executives had more opportunities to switch organizations, and perhaps this re<sup>fl</sup>ects executives' decision to “leave for greener pastures.” The results bear out Leaver's [28] approach to executive leadership: sit tight, take fewer risks, and let the tough times pass.

## 3.4.8. Summary

The analyses based on the KM estimator identi<sup>fi</sup>ed signi<sup>fi</sup>cant differences in job tenures for several factors. Contrary to popular lore, CIOs did not have the shortest survival: rather, COOs had the shortest job tenures, while CIOs, CEOs, and CFOs had similar survival durations. Durations for government executives were shorter than for Fortune 500 executives, and this was consistent across all types of government. We saw a lengthening of survival time for all executives across the different departure epochs too. Duration more than doubled from the early to the late departure epochs. Although we saw no differences in survival based on executive gender, we saw striking differences based on how much female leadership was present. Job tenures were the longest when no female leaders were present during our 15-year study period. They dropped noticeably with any level of female leadership, and their survival was the longest in small and large organizations. Finally, survival was the longest during periods of negative or neutral market turbulence.

![](/api/attachments/WSCU4Q7J/fulltext/images/788589d8eefe5f027e5b2b6df4cb699c8b8b2c8a9da3ea4c3be5f54d41c824d1.jpg)

![](/api/attachments/WSCU4Q7J/fulltext/images/6291efc276a067d8c031b9c4e40c2a39bb37db5e7a0eea031d1dadbcf1d0b40a.jpg)

(c) By FemaleLeaders (\*\*\*)  
![](/api/attachments/WSCU4Q7J/fulltext/images/9a71c88c91dca3901012d3620263b5fbc62ac23fe0630b4c547df1c20d0dfd85.jpg)  
Fig. 1. Executive survival % as a function of duration for stratifying covariates.

3.5. Extended non-parametric results with two-variable and three-variable KM estimators

## 3.5.1. Stratified results for all C-suite executives

We also estimated the survival functions for selected two-variable and three-variable strati<sup>fi</sup>ed sub-samples of our data to identify differences in job tenures between CIOs and other executives. We suppressed graphical presentation of the results in lieu of the explanations below.

3.5.1.1. By organization type and executive type. We compared the job tenures of CIOs, CEOs, COOs, and CFOs, based on whether they worked in government or private industry (Public). Government CIOs had survival times similar to other government leaders (CIO: 3.64 years, CEO: 3.81 years, COO: 3.51 years and CFO: 3.71 years); and Fortune 500 CIOs had similar survival to other Fortune 500 C-suite executives (4.71 vs. 5.10 years). While there were signi<sup>fi</sup>cant differences among different organization types (p b .001), there were no signi<sup>fi</sup>cant differences within them.<sup>10</sup> Signi<sup>fi</sup>cant differences (p b .001) across different sized organizations were present too, but the patterns for CIOs versus non-CIOs were not different. Given the variability in tenure of elected of<sup>fi</sup>cials, the government seems to have been different from the private sector but the differences were not linked to the election cycle. This supports the argument that simply porting best practices from private organizations into governmental organizations does not work well. Instead, key differences are likely to exist, and need to be taken into account.

3.5.1.2. By departure epoch and executive type. We compared CIO and non-CIO survival based on the epoch of their departure and found signi<sup>fi</sup>cant differences (p b .001). The same pattern appeared for CIOs and non-CIOs within each departure epoch: there was a lengthening in survival over time for each group. CIOs and non-CIOs had longer survival durations in 2004 (4.89 years) to 2008 (4.91 years) than in 2000 (3.80 year) to 2004 (3.51 years), or in 1994 (2.26 years) to 1999 (2.39 years). C-suite executives experienced a lengthening in job tenures, and there was a parallel maturing of IT use and the CIO position over this time. Some of the lengthening of CIO job tenure may have been due to this maturation.

3.5.1.3. By gender and executive type. We next compared CIO versus non-CIO survival based on gender. While differences existed by gender (female CIOs: 3.28 years, male CIOs: 4.16 years; female non-CIOs: 3.79 years, male non-CIOs: 3.79 years), they were not statistically signi<sup>fi</sup>cant. Thus, even when we more <sup>fi</sup>nely sliced the gender data, no signi<sup>fi</sup>cant differences were apparent.

3.5.1.4. By environmental turbulence and executive type. We compared the survival of CIOs to non-CIOs in years with positive, neutral, and negative market performance to proxy for environmental turbulence. Some signi<sup>fi</sup>cant differences occurred (p b .001), but none between CIOs and non-CIOs for differing levels of turbulence. CIOs and non-CIOs had similar job tenures under positive (3.53 vs. 3.27 years), neutral (4.15 vs. 4.02 years), and negative turbulence (4.46 vs. 4.58 years). The differences were pronounced for all executives in the presence of positive market turbulence. This, again, may have been because of the greater number of new job opportunities that became available for senior executives in years with positive turbulence.

Based on our data, CIOs appear to have far more in common with other executives than they have differences. While we saw statistical differences based on organization type, CIOs had similar job tenures in government versus Fortune 500 organizations. We also saw a difference based on departure epoch, although CIOs and other executives' job tenures had similar patterns. Executive gender for CIOs and other executives did not yield signi<sup>fi</sup>cant differences. CIOs and non-CIOs had similar negative impacts on their job tenures due to the arrival of female executives. With a single female executive in an organization over our 15 years of data coverage, survival dropped signi<sup>fi</sup>cantly for all executives. Finally, although there were differences by organization size, CIOs and non-CIOs had similar leadership duration patterns.

## 3.5.2. Stratification results for the CIOs only

We conclude our non-parametric analysis with three-factor strati<sup>fi</sup>cations to assess the joint explanatory power of the factors that in<sup>fl</sup>uenced CIO job tenures. The mean job tenure for CIOs was 3.78 years (std. dev. = 2.84 years). The minimum was one and maximum was 14 years.

3.5.2.1. By organization type, and gender and extent of female leadership. Male CIOs stayed longest at Fortune 500 <sup>fi</sup>rms (4.88 years), and there was a weak difference (p b .07) for male CIOs in government (3.78 years) or female CIOs in Fortune 500 <sup>fi</sup>rms (3.89 years) or female CIOs in government (3.28 years). Our data once again offered evidence that male and female CIOs had similar job tenure durations.<sup>11</sup> The longest job tenures for CIOs were at government agencies (5.36 years) and Fortune 500 organizations (5.22 years) when both had no female leadership. Our data represent mostly government agencies (\~80%). Eleven government agencies in our sample had no female leadership, and 34 Fortune 500 <sup>fi</sup>rms had none also. Thus, the government appears to have been more open to women leaders, though the reaction to female leadership was unmistakably negative for both government and Fortune 500 organizations.

3.5.2.2. By organization type, environmental turbulence and size. We compared CIOs by organization type and environment turbulence around their departure, and found no signi<sup>fi</sup>cant results. We were not surprised to see more variation in Fortune 500 turnover (Negative: 6.58 years; Neutral: 4.97 years; Positive: 3.27 years) than in government organizations (Negative: 3.50 years; Neutral: 3.72 years; Positive: 3.63 years)

though. Fortune 500 executives probably were rewarded during years with positive turbulence, and punished during years with negative turbulence. When we compared organization type and size, we found signi<sup>fi</sup>cant differences (p b .003): large Fortune 500 <sup>fi</sup>rm CIOs (4.72 years) and small government agency CIOs (4.76 years) were similar in having longer job tenures. Also, CIOs at both large (3.42 years) and medium-size agencies (3.19 years) had similar survival durations. There may be a salary-based explanation here: larger <sup>fi</sup>rms pay their executives more than smaller <sup>fi</sup>rms do. Fortune 500 <sup>fi</sup>rms CIOs have reached the pinnacle of CIO achievement and likely have salaries to re<sup>fl</sup>ect this. So there may be few other places that a Fortune 500 executive may go to increase income.

The story is likely to be different for government agencies.<sup>12</sup> For example, in California, the salary differences between the CIO of the largest and smallest agencies was only \$22,000 in 2008. As a result, there is very little <sup>fi</sup>nancial reward for running a much larger and more complex agency rather than a very small one. The job satisfaction and manageability of a small agency may outweigh the \$22,000 average salary increase for running a large agency. This may explain why survival is longer at large commercial <sup>fi</sup>rms and small government agencies – along with differences in the work, bonuses, and bene<sup>fi</sup>ts.

3.5.2.3. By organization type and departure epoch. We found statistical differences in CIO survival based on organization type and departure epoch (p b .001) also. For government and Fortune 500 organizations, survival was longest in the late epoch (Govt: 4.61 years; Fortune500: 5.17 years), shorter in the middle epoch (Govt: 3.55 years; Fortune500: 4.71 years) and shortest for the early epoch (Govt: 2.29 years; Fortune500: 2.25 years). This is a shift in CIO survival around the dotcom bubble, but as the bubble burst and the economy fell, the high salaries faded. This may explain the longer CIO job tenures.

## 3.5.3. Other empirical regularities

There were differences by gender and female leadership (p b .026). Male CIOs in organizations that had no female leadership during the study period had the longest survival (5.35 years). The pattern of reaction to female leadership differed by gender though. Female CIOs had longer survival when female leadership in their organizations was high (3.86 years) or low (3.47 years) in comparison to organizations with a medium level of female leadership (2.57 years). Male CIOs had a negative reaction to more female leadership. Survival was longest when there were no female leaders (5.35 years), and shorter for low (4.05), medium (3.48 years), and high female leadership (3.45 years).<sup>13,</sup> <sup>14</sup>

CIO survival was different when we considered environmental turbulence and departure epoch (p b .001). It was longest in times of positive turbulence in the late epoch (5.09 years) and shortest with negative turbulence in the middle epoch (2.50 years). The <sup>fi</sup>rst epoch only had positive and neutral turbulence; there was no negative turbulence then. Positive turbulence in the late epoch supported the longest survival. This suggests a halo effect. If the economy is performing well, in-place executives likely will be perceived as contributing to their success. Boards of directors will give CIOs incentives to remain. Economic prosperity may lengthen job tenures, and CIO survival clearly is shortest in the presence of negative turbulence.

Thus, there are differences in how CIOs reacted to the environmental factors. Though there are differences in turnover by gender and organization type, they were not signi<sup>fi</sup>cant. This is consistent with our previous analysis and suggests survival by gender is not so relevant. We saw signi<sup>fi</sup>cant differences in turnover by organization type and turbulence though. Fortune 500 CIOs have much more variable survival times based on changes in turbulence. We saw only minor differences in turnover by turbulence in government organizations. Yet we observed signi<sup>fi</sup>cant differences by organization type and size; salary issues likely drive this in Fortune 500 <sup>fi</sup>rms. We also observed a generational shift in CIO turnover over time but less sharp patterns in public organizations. When we examined organization type with the extent of female leadership, we were disheartened again to see that more progress toward female leadership has not been made in Fortune 500 <sup>fi</sup>rms. Also, in government and Fortune 500 <sup>fi</sup>rms, executive survival was longest with no female leaders. Female CIOs experienced a smaller “survival bump” based on their departure epoch. Finally, survival differed by turbulence and departure epoch, and organizational size and departure epoch. Single-factor strati<sup>fi</sup>cation would have produced neglected heterogeneity in our results.

## 4. Results II: semi-parametric and parametric models for C-suite executive job tenure

None of our assertions based on the KM estimator results indicate the extent to which any single variable or combination of variables affects survival duration in a statistical way. For this, we use explanatory models: the stratified Cox proportional hazards model for C-suite executives, and Cox proportional hazards and Weibull regression models for CIOs only. We next discuss our empirical model speci<sup>fi</sup>cations.

## 4.1. Model specification: Cox/stratified Cox proportional hazards models, and Weibull regression model

The Cox proportional hazards (PH) model has hazard function $h ( t | \pmb { x } ) = h _ { 0 } ( t , \pmb { \alpha } )$ exp(β<sup>T</sup>x) for departure of C-suite executives [25]. The term h (t, α) is the baseline hazard, which is a parametric function of time t and other variables α. The term exp(β<sup>T</sup>x) depends on q explanatory variables (or predictors) x, and $\beta ^ { T } = \overline { { ( \beta _ { 1 } , . . . , \beta _ { q } ) } }$ is the vector transpose of their coef<sup>fi</sup>cients.<sup>15</sup> When the PH assumptions are valid, the effect of a one-unit change in a predictor in the model leads to a proportional, multiplicative or scaled effect on the hazard function. The hazard function speci<sup>fi</sup>es the rate at which the event occurs at time t, conditioned on the event of interest not having occurred prior to that time. When the PH assumptions do not hold, it is possible to use the strati<sup>fi</sup>ed Cox proportional hazards model, $h ( t | \pmb { x } , s ) = h _ { s } ( t , \pmb { \alpha } )$ exp $\mathbf { \Omega } ( { \boldsymbol { \beta } } ^ { T } \mathbf { z } )$ , which permits estimation of the β parameters.

The Weibull regression model assumes that the hazard function is $h ( t | \pmb { x } ) = \alpha \eta ^ { \alpha } t ^ { \alpha - 1 }$ , where $\eta = \lambda \Bigl [ e x p \left( \beta ^ { T \pmb { x } } \right) \Bigr ] ^ { 1 / \alpha }$ . The duration of time until an executive leaves, T, can be expressed as a log-linear model of the form $Y = l n ( T ) = \mu + \gamma ^ { T } { \pmb x } + \sigma Z ,$ where $\boldsymbol { \gamma } ^ { T } = ( \gamma _ { 1 } , . . . , \gamma _ { q } )$ , and Z has a standard extreme value distribution. The parameters in the hazard function can be expressed in terms of the parameters in the log-linear model for T via $\alpha = 1 / \sigma , \lambda = e ^ { - \mu } ,$ , and $\beta _ { i } = - \gamma _ { i } / \mathbf { \sigma } \mathbf { \sigma } .$ The parameters in β are the PH coef<sup>fi</sup>cients.<sup>16</sup>

We ran correlations for: CIO (1 for CIO, 0 for other executives); Public (1 for public, 0 for private <sup>fi</sup>rms); Gender (1 for males, 0 for females); FemaleLeaders (LOW, MED, NONE; HIGH is base case); OrgSize (MED, SMALL; LARGE); Turbulence (Neutral, Positive, Negative); DepartEpoch (LATE, MID; EARLY); StartYrStockMkt; StartEpoch (LATE, MID; EARLY); HSGrad; CollegeGrad; and Income; and other variables. They were not too highly correlated, with one exception.<sup>17</sup>

## 4.2. Analysis by stratified Cox proportional hazards model for all C-suite executives

We <sup>fi</sup>rst analyzed the data for all the C-suite executives. This gave us freedom to specify a rich model to probe the effects of female leadership, the starting epoch for executives, the sector and size of their organizations, and environmental turbulence. After <sup>fi</sup>tting a Cox PH model, we saw that the PH assumptions did not hold though [19]. So we estimated a strati<sup>fi</sup>ed Cox PH model by stratifying by StartEpoch. 18

This yielded three different stratum-speci<sup>fi</sup>c baseline hazard functions that depend on time t. The hazard functions are h (t), h (t), and $h _ { L A T E } \left( t \right)$ . With the use of the strati<sup>fi</sup>ed model, the hazards for executives who joined their organizations during the different epochs all depend on their different individual baseline hazard functions, and the same set of variables for estimation of the β parameters.<sup>19</sup>

We estimated a model with 31 predictors, including the main effects variables (CIO, Public, OrgSize, Turbulence, DepartEpoch, StartYrStockMkt, HSGrad, CollegeGrad and Income) beyond the base cases, and various two-factor interaction terms.<sup>20</sup> Table 4 presents the estimated coef<sup>fi</sup>cients, the hazard ratios exp(β), standard errors for the estimated coef<sup>fi</sup>cients, Z-scores for coef<sup>fi</sup>cient signi<sup>fi</sup>cance, and p-values for the related two-sided Z-tests.

## 4.2.1. Observations on the coefficient and variable interaction estimates

There were many variables and interaction terms that were signi<sup>fi</sup>cant at the 5% or 10% level in the <sup>fi</sup>tted model, and the model <sup>fi</sup>tted the data quite well. Several observations are important related to the main effects. Those with signi<sup>fi</sup>cant positive effects on departure include OrgSizeSmall (estimate: 6.182, p = 0.026), TurbulencePositive (3.090, p = 0.012), HSGrad (5.542, p = 0.027), CollegeGrad (4.769, $p < 0 . 0 0 1 $ , StartYrStockMkt (43.220, p b 0.001), and Income (4.322, $p = 0 . 0 6 4 )$ . A signi<sup>fi</sup>cant negative effect was Public (−1.108, p = 0.008). TurbulenceNEUTRAL (1.799, $p \ = \ 0 . 1 4 8 )$ , DepartEpochLATE (3.358, p = 0.182), and DepartEpochMID (3.862, p = 0.158) were not signi<sup>fi</sup>cant. (We used these values below for hazard ratio inferences.)

Strati<sup>fi</sup>ed Cox proportional hazards model for all executives.

<table><tr><td>Variables</td><td> $\beta (Coef.)$ </td><td>Hazard ratio</td><td>Std. Err.</td><td>Z</td><td>Pr(X &gt; |Z|)</td></tr><tr><td colspan="6">• Main effects</td></tr><tr><td>CIO</td><td>-0.148**</td><td>0.86</td><td>0.083</td><td>-1.796</td><td>0.073</td></tr><tr><td>OrgSizeMEDIUM</td><td>-2.971</td><td>0.05</td><td>2.293</td><td>-1.296</td><td>0.195</td></tr><tr><td>OrgSizeSMALL</td><td>6.182**</td><td>483.70</td><td>2.778</td><td>2.225</td><td>0.026</td></tr><tr><td>Public</td><td>-1.018*</td><td>0.36</td><td>0.385</td><td>-2.648</td><td>0.008</td></tr><tr><td>TurbulenceNEUTRAL</td><td>1.799</td><td>6.04</td><td>1.244</td><td>1.446</td><td>0.148</td></tr><tr><td>TurbulencePOSITIVE</td><td>3.090**</td><td>21.97</td><td>1.226</td><td>2.520</td><td>0.011</td></tr><tr><td>DepartEpochLATE</td><td>3.348</td><td>28.44</td><td>2.512</td><td>1.322</td><td>0.182</td></tr><tr><td>DepartEpochMID</td><td>3.863</td><td>47.61</td><td>2.738</td><td>1.411</td><td>0.158</td></tr><tr><td>StartYrStockMkt</td><td>0.030***</td><td>1.03</td><td>0.007</td><td>4.342</td><td>0.001</td></tr><tr><td>HSGrad</td><td>5.542**</td><td>255.20</td><td>2.502</td><td>2.215</td><td>0.027</td></tr><tr><td>CollegeGrad</td><td>4.769***</td><td>117.80</td><td>1.228</td><td>3.882</td><td>0.001</td></tr><tr><td>Income</td><td>43.220*</td><td>0.86</td><td>23.370</td><td>1.850</td><td>0.064</td></tr><tr><td colspan="6">• Two-variable interaction terms</td></tr><tr><td>CIO × StartYrStockMkt</td><td>0.012*</td><td>1.01</td><td>0.006</td><td>2.043</td><td>0.041</td></tr><tr><td>DepartEpochLATE × HSGrad</td><td>-7.978***</td><td>0.00</td><td>2.768</td><td>-2.774</td><td>0.006</td></tr><tr><td>DepartEpochMID × HSGrad</td><td>-5.997**</td><td>0.00</td><td>2.981</td><td>-2.012</td><td>0.044</td></tr><tr><td>OrgSizeMEDIUM × HSGrad</td><td>5.206*</td><td>182.40</td><td>2.883</td><td>1.806</td><td>0.071</td></tr><tr><td>OrgSizeSMALL × HSGrad</td><td>-6.289*</td><td>0.00</td><td>3.658</td><td>-1.719</td><td>0.086</td></tr><tr><td>DepartEpochLATE × Income</td><td>-43.360**</td><td>0.00</td><td>17.810</td><td>-2.434</td><td>0.015</td></tr><tr><td>DepartEpochMID × Income</td><td>-48.160**</td><td>0.00</td><td>21.800</td><td>-2.209</td><td>0.027</td></tr><tr><td>TurbulenceNEUTRAL × Income</td><td>-17.560</td><td>0.00</td><td>18.140</td><td>-0.968</td><td>0.332</td></tr><tr><td>TurbulencePOSITIVE × Income</td><td>-59.960***</td><td>0.00</td><td>18.700</td><td>-3.207</td><td>0.001</td></tr><tr><td>DepartEpochLATE × StartYrStockMkt</td><td>-0.019**</td><td>0.98</td><td>0.008</td><td>-2.448</td><td>0.014</td></tr><tr><td>DepartEpochMID × StartYrStockMkt</td><td>0.007</td><td>1.01</td><td>0.009</td><td>0.842</td><td>0.400</td></tr><tr><td>OrgSizeMEDIUM × CollegeGrad</td><td>-3.279***</td><td>0.04</td><td>1.217</td><td>-2.695</td><td>0.007</td></tr><tr><td>OrgSizeSMALL × CollegeGrad</td><td>-2.323</td><td>0.10</td><td>1.450</td><td>-1.602</td><td>0.109</td></tr><tr><td>OrgSizeMEDIUM × DepartEpochLATE</td><td>-0.500**</td><td>0.61</td><td>0.210</td><td>-2.377</td><td>0.017</td></tr><tr><td>OrgSizeSMALL × DepartEpochLATE</td><td>-0.901***</td><td>0.41</td><td>0.217</td><td>-4.148</td><td>0.001</td></tr><tr><td>OrgSizeMEDIUM × DepartEpochMID</td><td>-0.279</td><td>0.74</td><td>0.215</td><td>-1.392</td><td>0.163</td></tr><tr><td>OrgSizeSMALL × DepartEpochMID</td><td>-0.703***</td><td>0.50</td><td>0.232</td><td>-3.030</td><td>0.002</td></tr><tr><td>Public × DepartEpochLATE</td><td>1.266***</td><td>3.55</td><td>0.306</td><td>4.139</td><td>0.001</td></tr><tr><td>Public × DepartEpochMID</td><td>1.458***</td><td>4.30</td><td>0.371</td><td>3.927</td><td>0.001</td></tr><tr><td>Public × TurbulenceNEUTRAL</td><td>0.210</td><td>1.23</td><td>0.297</td><td>0.709</td><td>0.479</td></tr><tr><td>Public × TurbulencePOSITIVE</td><td>1.032***</td><td>2.81</td><td>0.299</td><td>3.455</td><td>0.001</td></tr><tr><td>TurbulenceNEUTRAL × CollegeGrad</td><td>-1.762</td><td>0.17</td><td>1.389</td><td>-1.269</td><td>0.204</td></tr><tr><td>TurbulencePOSITIVE × CollegeGrad</td><td>-4.796***</td><td>0.01</td><td>1.318</td><td>-3.638</td><td>0.001</td></tr></table>

Notes. Model: strati<sup>fi</sup>ed Cox proportional hazards model. 1628 obs.; all C-suite executives; 31 variables. The base-cases for the variables that we estimated are: OrgSizeLARGE, TurbulenceNEGATIVE, and DepartEpochEARLY. Signif: \* = p b 0.010; \*\* = p b 0.05; \*\*\* = p b 0.01. The hazard ratio column contains the estimated values of exp(β) for each of the variables.

4.2.1.1. Positive and negative effects of interactions. There were signi<sup>fi</sup>cant positive interactions at the 5% level involving CIO × StartYrStockMkt, Public × DepartEpochLATE, Public × DepartEpochMID, and Public × TurbulencePOSITIVE, and negative interactions also. Examples of negative interaction effects on departure relate to an executive's Income via the estimates of DepartEpochLATE × Income (−43.380, p = 0.015), DepartEpochMID × Income (−48.160, p = 0.027), and TurbulencePOSITIVE × Income (−59.960, p b 0.001). Higher income levels seem to have diminished the likelihood of executive departure, in spite of the other impacts of the middle or later departure epoch, or the presence of positive market turbulence.

4.2.1.2. Effect of CIO title. The estimated coef<sup>fi</sup>cient of CIO × StartYrStockMkt is 0.012 (p = 0.041), while the main effect of CIO is −0.148 (p b 0.073). For executives who joined an organization in any year with same stock market returns of r% during the same StartEpoch, the risk of departure for a CIO was exp(−0.148 + 0.012r) times the risk of departure for other kinds of C-suite executives.

4.2.1.3. Selected interaction effects and inferences via the hazard ratio. There were a number of salient effects of OrgSize on the job tenures of C-suite executives related to variables involving education, HSGrad and CollegeGrad. and the different levels of DepartEpoch. With the other variables held <sup>fi</sup>xed, during the late departure epoch (DepartEpochLATE), the risk of departure of a C-suite executive (either CIO or non-CIO) at a medium-size organization (OrgSizeMEDIUM) was exp(−7.678 + 5.206 · HSGrad + 3.279 · CollegeGrad) times the risk of departure of an executive of the same group at a large-size organization (OrgSizeLARGE). This is valid for C-suite executives of the same group who joined the organization during the same StartEpoch. In comparison, the risk of departure for a C-suite executive at a small organization (OrgSizeSMALL) was exp(−2.819 − 6.289 · HSGrad − 2.323 · CollegeGrad) times as likely compared to an executive of the same group at a large organization (OrgSizeLARGE). Again, they must have joined in the same StartEpoch.<sup>21</sup>

There also were meaningful interactions between Public and DepartEpoch, and between Public and Turbulence. The estimated coef<sup>fi</sup>cients for Public × DepartEpochLATE (1.266, p b 0.001), for Public ×DepartEpochMID (1.458, p b 0.001), and for Public × TurbulencePOSITIVE (1.03, p b 0.001) were all signi<sup>fi</sup>cant. Although there were too many different combinations of variables to analyze and report on here, the key take-away in this segment of the analysis is that it was possible to produce many re<sup>fi</sup>ned estimates of the number of times that an executive was more likely to depart from a speci<sup>fi</sup>c type of organization, at some point in time, in years with some given level of turbulence, and so on – compared to another type of executive, all else held equal. The information can be obtained directly from the semi-parametric strati<sup>fi</sup>ed Cox PH model that we have reported.

We further note that the effects of a posting at a Public organization on the job tenure of C-suite executives can be determined based on nine different combinations of levels of DepartEpoch and Turbulence, with reference to each of the variables' different levels (EARLY, MID, LATE; and POSITIVE, NEUTRAL, NEGATIVE, respectively). We can infer useful information about executive departures from the interactions, for example, the combination of DepartEpochLATE interacted separately with TurbulenceNEUTRAL and then TurbulencePOSITIVE. Holding the values of the other variables constant, during the DepartEpochLATE period with a TurbulenceNEUTRAL market (calm market), any C-suite executive of the same kind (either CIO or non-CIO) in a Public organization had a 58.1% higher risk of departure than an executive of the same kind in a Private organization, provided that they joined their organizations during the same StartEpoch period (EARLY, MID, LATE). We can make this inference on the basis of the hazard ratio once again: $\exp ( - 1 . 0 1 8 + 1 . 2 6 6 + 0 . 2 1 0 ) = e ^ { 0 . 4 5 8 } = 1 . 5 8 1$ suggests a 58.1% higher risk. With TurbulencePOSITIVE characterizing the market during the DepartEpochLATE period, based on a hazard ratio of $\exp ( - 1 . 0 1 8 \ + \ 1 . 0 2 6 6 \ + \ 1 . 0 3 2 ) \ = \ e ^ { 1 . 2 8 } \ = \ 3 . 5 9 7$ , the C-suite executive's relative risk of departure from her position rose by 259.7%. (See Appendix C, Tables C1 and C2, for the full set of departure risk changes.)

## 4.3. Analysis by semi-parametric and fully-parametric models for CIOs only

## 4.3.1. Analysis by semi-parametric Cox PH model

We estimated this model for CIOs only. We con<sup>fi</sup>rmed that the PH assumptions were met. The <sup>fi</sup>tted model was $h ( t | \pmb { x } ; s = \mathrm { C I O s } \ \mathrm { o n l y } ) =$ $h _ { C I O } ( t ; \alpha ) \times \exp ( \beta ^ { T } { \pmb x } )$ . It has ten predictors, and they represent the main effects of the variables, StartEpoch, Turbulence, DepartEpoch, Public, OrgSize, Turbulence, and StartYrStockMkt. Table 5 presents the estimated coef<sup>fi</sup>cients, hazard ratios $\exp ( \beta _ { i } ) ( \mathrm { o r } e ^ { \beta i } )$ , standard errors of the coef<sup>fi</sup>cients, the Z-scores for coef<sup>fi</sup>cient signi<sup>fi</sup>cance, and p-values of the related two-sided Z-tests. The model <sup>fi</sup>tted the data quite well, and eight out of ten predictors were signi<sup>fi</sup>cant at the 5% level.

4.3.1.1. Effect of stock market returns during the year the CIO joined. The estimated coef<sup>fi</sup>cient for StartYrStockMkt for the data was 0.029 $\left( { p < 0 . 0 0 1 } \right)$ . So the risk of departure of a CIO who started working in a new position in a year with stock market returns of $( r + \nu ) \%$ was exp(0.029v) times compared to other CIOs who joined their organizations in a year with stock market returns of r%.

4.3.1.2. Effects of OrgSize and OrgType. The estimated coef<sup>fi</sup>cients were as follows: for $O r g S i z e M E D I U M - 0 . 0 7 1 ~ ( p = 0 . 6 7 5 )$ and for OrgSizeSMALL $- 0 . 3 9 5 \ ( p = 0 . 0 3 6 )$ . Holding the other variables <sup>fi</sup>xed, the risk of departure for a CIO from a medium-sized organization was 6.9% $( \stackrel { \cdot } { = } 1 - e ^ { - 0 . 0 7 1 } )$ lower than that for a CIO from a large organization. The risk of departure for a CIO from a small organization was 32.7% $( = 1 - e ^ { - 0 . 3 9 5 } )$ lower than that for a CIO in a large organization. The estimated coef<sup>fi</sup>cient for Public was 0.567 $\left( p < 0 . 0 0 2 \right)$ . With the other variables <sup>fi</sup>xed, the risk of departure for a CIO from public organizations was about $7 6 . 3 \% ( = e ^ { 0 . 5 6 7 } - \dot { 1 } )$ higher than that for a CIO from a private <sup>fi</sup>rm.

4.3.1.3. Effects of Turbulence, StartEpoch, and DepartEpoch. The estimated coef<sup>fi</sup>cients were as follows: for TurbulenceNEUTRAL 0.242 $( p =$ 0.297) and for TurbulencePOSITIVE −1.491 (p b 0.001). Holding the other variables <sup>fi</sup>xed, a weak estimate (due to the lack of signi<sup>fi</sup>cance of the variable) suggests that the risk of departure for CIOs during a period with neutral turbulence was 27.4% $( = 1 - e ^ { 0 . 2 4 2 } )$ higher than that during a period with negative turbulence (the base case). In contrast, the risk of job departure for CIOs during a period with positive turbulence was $2 2 . 5 \% ( = e ^ { - 1 . 4 9 1 } )$ of that during a period with negative turbulence.

Cox proportional hazards model for CIOs only.

<table><tr><td>Variables</td><td> $\beta$  (COEF.)</td><td>Hazard ratio</td><td>STD. ERR.</td><td>Z</td><td>Pr(X&gt;|Z|)</td></tr><tr><td>StartEpochLATE</td><td>3.437***</td><td>31.101</td><td>0.348</td><td>9.870</td><td>&lt; 0.001</td></tr><tr><td>StartEpochMID</td><td>2.069***</td><td>7.915</td><td>0.249</td><td>8.322</td><td>&lt; 0.001</td></tr><tr><td>TurbulenceNEUTRAL</td><td>0.242</td><td>1.274</td><td>0.232</td><td>1.043</td><td>0.297</td></tr><tr><td>TurbulencePOSITIVE</td><td>-1.491***</td><td>0.225</td><td>0.230</td><td>-6.508</td><td>&lt; 0.001</td></tr><tr><td>DepartEpochLATE</td><td>-4.626***</td><td>0.010</td><td>0.336</td><td>-13.763</td><td>&lt; 0.001</td></tr><tr><td>DepartEpochMID</td><td>-2.817***</td><td>0.060</td><td>0.287</td><td>-9.816</td><td>&lt; 0.001</td></tr><tr><td>Public</td><td>0.567**</td><td>1.763</td><td>0.184</td><td>3.090</td><td>0.002</td></tr><tr><td>StartYrStockMkt</td><td>0.029***</td><td>1.029</td><td>0.007</td><td>3.926</td><td>&lt; 0.001</td></tr><tr><td>OrgSizeMEDIUM</td><td>-0.071</td><td>0.931</td><td>0.170</td><td>-0.419</td><td>0.675</td></tr><tr><td>OrgSizeSMALL</td><td>-0.396*</td><td>0.673</td><td>0.189</td><td>-2.098</td><td>0.036</td></tr></table>

Notes. Model: semi-parametric Cox proportional hazards model. 378 obs.; CIOs only; 10 variables. Signif: \* = < 0.010; \*\* = 0.05; \*\*\* = < 0.01. The Hazard Ratio column contains the estimated values of exp( ) for <sup>p</sup> <sup>p</sup> <sup><</sup> <sup>p</sup> each of the variables. The base–case variables are: , , <sup>StartEpochEARLY TurbulenceNEGATIVE DepartEpoch–</sup>, and The data diagnostics for the results suggest that this model is able to <sup>EARLY Private,</sup> <sup>OrgSizeLARGE.</sup> return useful information on the variables. The variables in rows with gray cells will no longer be used since they did not show statistical significance at the 05 level. With a relatively small number of observations (less than 400 CiOs in the original full sample), we did not seek to identify the effects of interactions between the explanatory variables. The data do not support this, so we have focused on the main effect variables instead.

The estimated coef<sup>fi</sup>cients for StartEpochLATE (3.437, p b 0.001) and StartEpochMID (2.069, p b 0.001) were highly signi<sup>fi</sup>cant. With the other variables held <sup>fi</sup>xed, the risk of departure for CIOs who joined an organization in the late StartEpoch was about 31 (= $\bar { e } ^ { 3 . 4 3 7 } )$ times that for CIOs who joined in the early StartEpoch, whereas the risk of job departure for CIOs who joined an organization in the middle StartEpoch was about 8 $( = e ^ { \breve { 2 } . 0 7 9 } )$ times that for CIOs who joined in the early StartEpoch – evidence of an old-timer effect. The estimated coef<sup>fi</sup>cients for DepartEpochLATE $( - 4 . 6 2 6 , p < 0 . 0 0 1 )$ and DepartEpochMID $( - 2 . 8 1 7 , p < 0 . 0 0 1 )$ were highly signi<sup>fi</sup>cant too. Departure risk for CIOs during the late epoch was less than 1% $( = e ^ { - 4 . 6 \bar { 2 } 6 } )$ of that during the early epoch in the observation timeline compared to the middle epoch, which was 5.98% $( = e ^ { - 2 . 8 1 7 } )$ of the early epoch.

This analysis shows that a number of key variables had signi<sup>fi</sup>cant effects on the likelihood of CIOs to have left their jobs over the period of our data coverage. For example, the effect of a job start in the late epoch (StartEpochLATE) was a likelihood of departure of about 31 times that for a CIO who started in the early epoch. Similarly, a CIO who started in the middle epoch (StartingEpochMID) was about 8 times as much – all else are equal in both cases. But a CIO who worked in a Public, but not a Private organization had a 76.3% greater risk of departure over her timeline of employment, as reported in the press [54].

4.3.1.4. Effects of OrgSize, Turbulence, and StartYrStockMkt. Organization size generally had signi<sup>fi</sup>cant negative effects based on our model. CIOs who worked at small <sup>fi</sup>rms and agencies experienced a 32.7% lower risk of departure than CIOs at large organizations. Similarly, positive market turbulence was associated with a 22.5% risk of a CIO's departure, compared to a period with negative turbulence. Finally, we noted a highly signi<sup>fi</sup>cant coef<sup>fi</sup>cient estimate for the StartYrStockMkt variable of 0.029. This implies that the higher was the stock market return in the year a CIO joined an organization, the higher was the risk of subsequent departure.

The main take-away is the extent to which the interaction effects create a basis for different results, requiring more nuanced conclusions about the effects of female leadership. They are not as obvious as one might conclude from the non-parametric analysis alone. Parametric analysis, thus, is valuable here.

## 4.3.2. Analysis by parametric Weibull regression mode

Finally, we present other results by <sup>fi</sup>tting the Weibull regression model for CIOs only. The model yielded estimates through a somewhat different process for the effects of <sup>fi</sup>ve of the main effects that we have been considering on job tenure for CIOs. (We eliminated variables that the prior estimations suggested were not needed.) This model missed out identifying the signi<sup>fi</sup>cant effect of OrgSize that the semi-parametric model identi<sup>fi</sup>ed. (See Table 6.)

The validity of the Weibull regression model is questionable, though many of the estimated coef<sup>fi</sup>cients were highly signi<sup>fi</sup>cant. We made this assessment based on some diagnostics checks, especially the results from various plots of the Cox–Snell residuals and deviance residuals. A plot of the estimated cumulative hazard function of the Cox–Snell residuals against the Cox–Snell residuals themselves did not reveal a straight line through the origin with a slope 1, as expected when the parametric assumption is valid. Nor did a deviance residuals plot against time show the typical random pattern. Thus, we caution the reader that this model, though attractive from an analytical viewpoint, may not be valid. For this reason, we will not comment further on the model's quantitative <sup>fi</sup>ndings, nor attempt to compare the <sup>fi</sup>ndings to other results we obtained.

## 5. Key <sup>fi</sup>ndings and discussion

Several <sup>fi</sup>ndings deserve further discussion. First, generally speaking, CIO survival matched the survival of the CEO and CFO, and was longer than for the COO. This provides evidence that the CIO shares similar characteristics to other C-suite executives. CIOs do not appear to be too different based on organization type, departure epoch, gender, demographic characteristics, extent of female leadership, organization size or environmental turbulence. In addition, CIOs reacted similarly to different types of environmental turbulence as other executives did. Second, many environmental factors impact executive survival and certain combinations of factors also impact survival in slightly different ways, as our non-parametric, semi-parametric, and fully-parametric models suggest. This highlights the value of the view that “environment matters,” and offers promise for better understanding interactions among different variables through the advanced techniques that we demonstrated.

Second, the differences by organization type are profound; and, in particular, they highlight that government is not simply a poorly performing cousin to Fortune 500 <sup>fi</sup>rms. This raises questions about simply porting Fortune 500 practices to the government. For the CIOs, their briefer survival duration may result from shorter periods of time to transform technology in the government sector. Given the length of time necessary to budget and implement major technology initiatives within government, these projects may experience turnover in the CIO's position between the conceptualization of a project and its ultimate implementation. This may be a causal factor in the failure of technology projects within government agencies. At a minimum, it shortens the governmental CIO's time horizon to plan and implement.

Fully-parametric Weibull regression model for CIOs only

<table><tr><td>Variables</td><td> $\beta$  (Coef.)</td><td>Std. Err.</td><td>Z</td><td>Pr(X &gt; |Z|)</td></tr><tr><td>StartEpochLATE</td><td>-1.513***</td><td>0.108</td><td>-13.972</td><td>&lt;0.001</td></tr><tr><td>StartEpochMID</td><td>-0.862***</td><td>0.876</td><td>-9.820</td><td>&lt;0.001</td></tr><tr><td>TurbulenceNEUTRAL</td><td>-0.090**</td><td>0.102</td><td>-0.886</td><td>0.038</td></tr><tr><td>TurbulencePOSITIVE</td><td>0.615***</td><td>0.103</td><td>5.979</td><td>&lt;0.001</td></tr><tr><td>DepartEpochLATE</td><td>1.940***</td><td>0.108</td><td>18.018</td><td>&lt;0.001</td></tr><tr><td>DepartEpochMID</td><td>1.183***</td><td>0.113</td><td>10.414</td><td>&lt;0.001</td></tr><tr><td>Public</td><td>-0.206***</td><td>0.072</td><td>-2.858</td><td>&lt;0.001</td></tr><tr><td>StartYrStockMkt</td><td>-0.012***</td><td>0.003</td><td>-3.917</td><td>&lt;0.001</td></tr><tr><td> $\mu$ </td><td>0.696***</td><td>0.148</td><td>4.718</td><td>&lt;0.001</td></tr><tr><td>ln( $\sigma$ )</td><td>-0.799***</td><td>-0.053</td><td>-15.332</td><td>&lt;0.001</td></tr></table>

Notes. Model: fully-parametric Weibull regression model. 378 obs.; CIOs only; 8 variables The base-case variables are: Start EpochEARLY, TurbulenceNEGATIVE, and DepartEpochEARLY.

Third, longer C-suite executive job tenures are seen in the departure epochs of executives in our data. This suggests that executives are taking a longer view of their positions and are less attracted by the quick turnover opportunities seen in the 1990s. It may also re<sup>fl</sup>ect a weak economy and a lack of job alternatives. For CIOs, this should help them to stay focused on planning and implementing major technology projects.

Although the time horizon is shorter for government agencies, the gradual lengthening of job tenures should result in more consistency in technology leadership over time and higher maturity of technology within the organization and of the CIO role itself. It may also re<sup>fl</sup>ect that all C-suite executives now have a more realistic view of the timing and results of technology projects. Or it may simply be, as Jerry Luftman of New Jersey Institute of Technology presciently suggested over ten years ago, that CIOs are doing better to establish themselves as business managers [48].

Fourth, gender issues remain. Male and female C-suite executives, including CIOs, now have similar job tenures. But we are far more concerned with the negative reaction to increasing levels of female leadership. In both government and Fortune 500 organizations, a greater extent of female leadership shortened the survival of all executives, including CIOs. In addition, the impact of female leadership was more severe at Fortune 500 <sup>fi</sup>rms. Female leadership seems to impact male leaders' survivability in a negative way, although we have not been able to discover in this research what is the primary operative mechanism that may cause this. This opens up the possibility of conducting structural modeling research in the future to understand the micro-foundations of the aggregate behavior that we have observed. This will create the possibility to ask questions involving counterfactuals, such as: What mechanism is at work that leads to the reduced survivability of C-suite executives and the CIO under different conditions, including those that we can observe, and those that may emerge later, but cannot be observed now? Additionally, the survival of male CIOs has lengthened dramatically over time, while the number of female CIOs and their job tenures have not increased much. Women still have substantial gains to make, no question, but what will more care given to the micro-foundations of aggregate behavior that we observe be able to tell us?

Fifth, organization size impacts all C-suite executives and their survival seems to be the longest at small and large <sup>fi</sup>rms. We suggested that medium-sized <sup>fi</sup>rms may be seen as stepping-stones to larger <sup>fi</sup>rms and so were not surprised to see U-shaped job tenures based on <sup>fi</sup>rm size. Survival also differed based on organization size for different organization types. Survival appears to have been the longest at the Fortune 500 <sup>fi</sup>rms. Perhaps this re<sup>fl</sup>ects the relative scarcity of other large <sup>fi</sup>rms to provide a landing spot for departing C-suite executives. Survival was longest for government executives at small agencies though. It is tempting to argue that this is a lifestyle choice, since there is little difference in CIO pay for large versus small government agencies. Nevertheless, it seems like large government agency CIO positions may be a feeder to the higher-paying world of Fortune 500 companies, and this has shortened their job tenures. We need additional data to nail down whether this is truly the case.

Sixth, external environmental turbulence impacts C-suite executives. Our data show differences based on positive, negative, and neutral turbulence, with differences across all of the related environmental factors. The differences may drive the ability of an organization to successfully roll out and use technology, which may create more targeted impacts on CIOs, and have less in<sup>fl</sup>uence on other C-suite executives.

Finally, studying the interactions among the different variables in our data set using semi-parametric models offered insights enriched our understanding of C-suite executive job tenures beyond the <sup>fi</sup>ndings we obtained from non-parametric models – and especially so for CIOs. There are substantial negative turnover consequences associated with the interaction between departure epoch and the type of environmental turbulence (e.g., positive versus negative). Clearly, executives are reacting differently now to environmental turbulence versus in earlier epochs. Executives may have learned hard lessons from moving in reaction to the stock market and have become more cautious as a result. And there are many opportunities for interactions among all different levels of female leadership, and small and medium-sized organizations.

Small and medium organizations may be more accepting of female leadership, and if the extent of female leadership is large, negative survivability may result. It may also be the case that female leadership is more entrenched in large organizations and the greater numbers of female leaders are simply ignored. Further, organization size and turbulence, and organization size and departure epoch were signi<sup>fi</sup>cant. Thus, survivability is different at small and medium organizations. Apparently executives move for much different reasons at small and medium organizations as opposed to large ones.

## 6. Conclusion

We applied non-parametric, semi-parametric, and fullyparametric models in survival analysis to study the duration of CIO job tenures. The methods are of increasing interest in the domain of IS research [24] and within the scope of Decision Support Systems [11]. They handle the evaluation of events, and when they occur. Chen et al. [13] have argued that data analytics and business intelligence are central to the IS <sup>fi</sup>eld. This is increasingly true as IS researchers gain greater capabilities to study data streams in which detection and analysis of key events are central to understanding the decision-making, operational and strategic environments. Not only will explanatory, causal models be of interest, but so will predictive models that dominate the mainstream of the physical sciences [42]. With the Cox PH and strati<sup>fi</sup>ed Cox PH models, we have shown how <sup>fi</sup>ne-grained analysis can reveal the conclusions that can be drawn within the limitations of the data. The fully-parametric Weibull regression model was less informative though.

We note several limitations in this research though. First, despite the number of data points we obtained, we have no way of knowing if our data are representative of all executives or even the executives within a given industry. Additional data are truly hard to obtain. We performed robustness checks to validate some of the data's desirable statistical properties though. Second, we focused on a few environmental factors and acknowledge that other factors may exist and impact survival (e.g., industrial sector). Finally, we did not investigate the relationship between CIO departure and the timing of the departure of other executives. An anonymous reviewer suggested this will be a fruitful area for additional research.

The topic of executive survival, particularly CIO job tenures, is a promising area to explore using the kinds of data analytic techniques that we chose. They allow us to <sup>fi</sup>nd robust answers to our research questions. Our empirical results show that environmental factors, either alone or in combination, can have a profound impact on C-suite executive job tenures, and these impacts on survival vary based on the executive type and size of the organization involved. As we sought to understand, similar patterns do exist for different organizations. The impacts of these patterns seem strong and there are some differences between CIOs' and other executives' survivability. Additionally, we observed a profound shift in executive survival over the last several years, and this suggests the need for additional research to uncover the details and rami<sup>fi</sup>cations of this apparent shift. Something big has been happening, and management and technology scholars have not yet thoroughly investigated it.

## Acknowledgments

An earlier version of this research was presented at the 2011 International Conference on Information Systems in Shanghai, China. The authors are grateful to the anonymous reviewers, area editor, and editor-in-chief of Decision Support Systems for providing useful input and guidance, as well as colleagues Hank Lucas, Sunil Mithas, Pulak Ghosh, Dan Ma, and Martin Yu. Rob Kauffman acknowledges the W.P. Carey Chair in IS at Arizona State University, and the Lee Kong Chian Faculty Fellowship for Research Excellence at Singapore Management University for generous support. Gregory Dawson acknowledges the support of the W.P. Carey School of Business as well as the Center for Organization Research and De sign (CORD), both at Arizona State University. We also appreciated assistance from the many respondents from U.S. federal, state and municipal government agencies, who were instrumental in the success of our data collection.

## Appendix A. The modeling and estimation processes

1. Baseline and Extended Non-Parametric Model Analyses  
![](/api/attachments/WSCU4Q7J/fulltext/images/11c1081b28c1a458b3f8d731e71495ccdeca3a69165a5e4e9a1e281f545466f5.jpg)

## 3. Results Evaluation and Comparisons

Goals for the different kinds of analysis:

• Non-parametric models: Establish empirical regularity results without explanation

• Semi-parametric models: Establish variables’ effects for the baseline hazard function

Fully-parametric model: Establish variables’ incremental impacts on the baseline hazard function, and other variables for which we can establish explanatory finding

## Appendix B. Data collection, sample, and coding

## B.1. Data sources

Data on C-suite executives come from: (1) the CA, VA, and MA state governments, and Agency Directors (AD), Deputy Directors of Administration (DDA), Chief Budget Of<sup>fi</sup>cers (CBO), and CIOs; (2) U.S. cities and counties, for ADs, DDa, CBOs, and CIOs; (3) U.S. Federal Government, for Federal ADs, DDAs, CBOs, and CIOs; and (4) Fortune 500 s, for CEOs, COOs, CFOs, and CIOs. These sources represent a wide diversity in terms of industry size, organization size, and geographic dispersion. Public sector data were available on agency websites. We sent Freedom of Information Act (FOIA) requests for data when it was not available. Agency provided data within 72 hours, which is normal for FOIA requests. Fortune 500 data were obtained via SEC reports.

## B.2. Study period, 1994 to 2009

This period showed several turnover events for executives in our data set. The title of CIO was not much used until the mid-1990s in the U.S. Third, this period in the U.S. had events that created environmental turbulence, especially due the dotcoms rise (1996–2000) and fall (2000–2002) Also 2000, “Y2k,” occurred, as well as the enactment of the Sarbanes–Oxley Act of 2002. There were <sup>fi</sup>nancial market upswings (1997–2000, 2004–2006) and downswings (2000–2002, 2008–2009). This allows the comparisons that we will make.

## B.3. Sample properties

The sample is balanced across executive types (400–544 obs. in each category). 1395 (78.2%) are from public organizations, with 389 (21.8%) from the Fortune 500. 856 state executives accounted for 48%; and 141 city and county executives made up 8%. By gender, there were 1357 (76%) men and 427 (24%) women. Our sample contained 400 CIOs, and fewer came from the private sector. The median number of years of survival for CIOs is the same as for all C-suite executives: 3 years. The average duration of job tenure is 3.97 years for CIOs and 3.79 years for all executives. This excludes survival for currently serving executives.

## B.4. Data set exclusions

Via outlier analysis on job tenure, we discovered that some executives' tenures were more than three standard deviations from the mean. We chose to exclude them, resulting in 141 fewer records, reducing the data set from 1784 to 1643 observations. We also removed executives who remained in their positions as of the end of the period of coverage of our data. This permitted us to focus on executives with known beginning and ending dates. The data points fell further to 1069, for which we found in-range skewness (1.419) and kurtosis (1.181).

## B.5. Data coding procedures for ExecType

For executives' records, we coded a PersonName and StartYear. We also coded DepartYear when the individual left the position, and Gender. We assigned gender based on the typical gender for that particular name. For names used for both genders, such as Chris or Pat, we searched for individual bio sketches to uncover additional information. For Executive, we used titles in Fortune 500 <sup>fi</sup>rm SEC <sup>fi</sup>lings. Most used the CEO, COO, CFO, and CIO nomenclature. For the public sector, we identi<sup>fi</sup>ed Agency Directors as CEO-equivalents, Deputy Directors of Administration as COOs, and Chief Budget Of<sup>fi</sup>cers as CFOs. CIOs were called CIOs. We identi<sup>fi</sup>ed interim appointments and coded these with Interim. We used a right-censored <sup>fl</sup>ag if a person was in the executive position as of 2009. We knew the start dates of all executives, so there was no left-censoring. We intended to code for ExecutiveTransitions, when someone took a new job in the same organization. All transitions in our data were in Fortune 500 <sup>fi</sup>rms with COOs becoming CEOs. No CIOs took other positions.

## B.6. Data coding procedures for organizations

We coded organization types: State for the states, Cty for cities and counties, Fed for U.S. federal agencies, and F500 for Fortune 500s. Their annual budgets during the time period of our study represent OrgSize. We coded all Fortune 500 companies as large.

## B.7. Data coding procedure for environmental turbulence

For environmental Turbulence, we focused on external environmental turbulence and used yearly changes in the NASDAQ and New York Stock Exchange market indices for that period and coded Positive (N5%), Neutral $( - 5 \% \ t 0 \ + 5 \% )$ , and Negative (b−5%). The stock market is a proxy, re<sup>fl</sup>ecting economic turbulence, and so it is a reasonable choice.

## B.8. Data coding procedure for departure epoch

We were interested in when executives left their positions, so our coding identi<sup>fi</sup>es the DepartYear for each executive's job tenure too. We coded DepartEpoch based on DepartYear and used EARLY (1994–1999), MID (2000–2004), and LATE (2005–2009). These epochs are divided into approximately equal time periods. They re<sup>fl</sup>ect a period of technology boom (1994–1999), technology retrenchment (2000–2004) and a more balanced view of technology (2005–2009). Additionally, each epoch included at least two of the codes for environmental turbulence (EARLY only has neutral and positive turbulence while MID and LATE have all three types of turbulence), and thus captures a different dynamic. Varying the epoch de<sup>fi</sup>nitions did not reveal dramatic differences or suggest to us that we could have improved our coding of temporal differences.

## B.9. Data coding procedures for female leadership

We also created a variable called FemaleLeaders based on the percentage of female executives over the 15-year study period for a given organization. We measured this for the number of female leaders in any private or public sector organization C-suite position. We created four categories: None (no female executives in 15 years), Low (1% to 10% female leadership), Medium (11% to 25%), and High (N25%).

## Appendix C. Semi-parametric hazard ratio-based statistical inferences

Effects of StartYrStockMkt returns and DepartEpoch on executive type departure risk.

<table><tr><td>DepartEpoch</td><td>Return</td><td>Hazard ratio</td><td>Departure risk Δ</td></tr><tr><td colspan="4">EARLY DepartEpoch comparison</td></tr><tr><td>• CIO</td><td>r+1%</td><td> $\exp[(0.030 + 0.012)(r + 1 - r)] = e^{0.042} = 1.043$ </td><td>1.043 → 4.3% more risk</td></tr><tr><td>• Non-CIOs</td><td>r%</td><td> $\exp[0.030(r + 1 - r)] = e^{0.03} = 1.03$ </td><td>1.030 → 3% more risk</td></tr><tr><td colspan="4">MID DepartEpoch comparison</td></tr><tr><td>• CIO</td><td>r+1%</td><td> $\exp[(0.030 + 0.012 + 0.007)(r + 1 - r)] = e^{0.049} = 1.05$ </td><td>1.050 → 5% more risk</td></tr><tr><td>• Non-CIOs</td><td>r%</td><td> $\exp[(0.030 + 0.007)(r + 1 - r)] = e^{0.037} = 1.038$ </td><td>1.038 → 3.8% more risk</td></tr><tr><td colspan="4">LATE DepartEpoch comparison</td></tr><tr><td>• CIO</td><td>r+1%</td><td> $\exp[(0.030 + 0.012 - 0.019)(r + 1 - r)] = e^{0.022} = 1.022$ </td><td>1.022 → 2.2% more risk</td></tr><tr><td>• Non-CIOs</td><td>r%</td><td> $\exp[(0.030 - 0.012)(r + 1 - r)] = e^{0.01} = 1.01$ </td><td>1.010 → 1% more risk</td></tr></table>

Note: this table illustrates the comparison within three DepartEpoch periods (EARLY, MID, LATE) of the effects of StartYrStockMkt returns (r + 1%) for CIO versus non-CIO executive job departures during a year with StartYrStockMkt returns of k%. All of the executives must have begun their jobs in the same StartEpoch period. With StartYrStockMkt returns of (r + 1)%, a CIO will have a higher departure risk (of 4.3%, 5% and 2.2%) relative to non-CIOs, who will have a lower departure risk (3%, 3.8% and 1%). It is all made possible by the use of statistical inferences from our semi-parametric survival model. Note that the base market return values r% cancel out, making it possible to obtain a real-valued de parture risk for any value of base market return.

Public OrgType effect on departure, for nine crosses of DepartEpoch and Turbulence.

<table><tr><td>Turbulence</td><td>Hazard ratio</td><td>Departure risk Δ</td></tr><tr><td colspan="3">EARLY DepartEpoch comparison</td></tr><tr><td>Positive</td><td> $exp(-1.018 + 1.032) = e^{-0.014} = 1.010$ </td><td>1.010 → 1.0% more risk</td></tr><tr><td>Neutral</td><td> $exp(-1.018 + 0.210) = e^{-0.81} = 0.445$ </td><td>0.445 → 55.5% less risk</td></tr><tr><td>Negative</td><td> $exp(-1.018) = e^{-1.02} = 0.363$ </td><td>0.363 → 63.7% less risk</td></tr><tr><td colspan="3">MID DepartEpoch comparison</td></tr><tr><td>Positive</td><td> $exp(-1.018 + 1.458 + 1.032) = e^{1.47} = 4.349$ </td><td>4.349 → 334.9% more risk</td></tr><tr><td>Neutral</td><td> $exp(-1.018 + 1.458 + 0.210) = e^{0.65} = 1.916$ </td><td>1.916 → 91.6% more risk</td></tr><tr><td>Negative</td><td> $exp(-1.018 + 1.458) = e^{0.44} = 1.553$ </td><td>1.553 → 55.3% more risk</td></tr><tr><td colspan="3">LATE DepartEpoch comparison</td></tr><tr><td>Positive</td><td> $exp(-1.018 + 1.266 + 1.032) = e^{1.28} = 3.597$ </td><td>3.602 → 260.2% more risk</td></tr><tr><td>Neutral</td><td> $exp(-1.018 + 1.266 + 0.210) = e^{0.46} = 1.584$ </td><td>1.584 → 58.4% more risk</td></tr><tr><td>Negative</td><td> $exp(-1.018 + 1.266) = e^{0.25} = 1.284$ </td><td>1.284 → 28.4% more risk</td></tr><tr><td colspan="3">Note: Departure risk comparisons are relative to the base case for the variables:DepartEpochEARLYand TurbulenceEARLY. The gray row represents the base case for both variables. There are nine combinations ofDepartEpoch and Turbulencelevels in the market that are depicted. The method that is used to establish the statistical inference is again based on the analysis of the stratified Cox proportional hazards semi-parametric survival model, which yields information from the estimated coefficients, to support instantiation of theDepartEpochand market Turbulence-level variable interactions. The more significant are the variables that an analyst uses for these computations, the better will be the departure risk Δ inferences that can be made.</td></tr></table>

## References

[1] O.O. Aalen, Ø. Borgan, H.K. Gjessing, Survival and Event History Analysis, Springer, NY, 2008.

[2] S.M. Adams, A. Gupta, D.M. Daughton, J. Leith, Gender differences in CEO compensation, Women in Management Review 22 (3) (2007) 208–224.

[3] S. Aral, D. Walker, Creating social contagion through viral product design: a randomized trial of peer in<sup>fl</sup>uence in networks, Management Science 57 (9) (2011) 1623–1639.

[4] C.P. Armstrong, V. Sambamurthy, Information technology assimilation in <sup>fi</sup>rms: the influence of senior leadership and IT infrastructures Information Systems Research 10 (4)(1999).304–327

[5] O.H. Ayaba, K. Ittonen, Chief executive of<sup>fi</sup>cer's (CEO's) educational background and <sup>fi</sup>rm performance: an empirical study on manufacturing and IT listed <sup>fi</sup>rms in the Stockholm Stock Exchange, Umeå University, Sweden, 2012.

[6] E. Ban<sup>fi</sup>eld, Corruption as a feature of government organization, Journal of Law and Economics 18 (3) (1975) 587–605.

[7] S. Bhattacharjee, R. Gopal, K. Lertwachara, J. Marsden, R. Telang, The effect of digital sharing technologies on music markets: a survival analysis of albums on ranking charts, Management Science 53 (9) (2007) 1359–1374.

[8] J.M. Blumenthal, Candid re<sup>fl</sup>ections of a businessman in Washington, in: J. Perry, K. Kraemer (Eds.). Public Management: Public and Private Perspectives, Mayfield. Palo Alto, CA. 1983.

[9] B. Bozeman, H. Rainey, Org. rules and bureaucratic personality, American Journal of Political Science 50 (5) (1998) 536–545

[10] B. Buchanan, Red tape and the service ethic: some unexpected differences between public and private managers, Administration and Society 6 (4) (1985) 423–438.

[11] R. Chang, R.J. Kauffman, Y. Kwon, Understanding the paradigm shift to computational social science in the presence of big data, Decision Support Systems 63 (2014) 67–80.

[12] D. Chatterjee, V.J. Richardson, R.W. Zmud, Examining the shareholder wealth effects of announcements of newly created CIO positions, MIS Quarterly 25 (1) (2001) 43–70.

[13] H. Chen, R. Chiang, V. Storey, Business intelligence and analytics: from big data to big impact, MIS Quarterly 36 (4) (2012) 1165–1188.

[14] B. Connolly, How the CIO came to be, CIO, Jan 23 2013.

[15] R. Cyert. I. March, A Behavioral Theory of the Firm, Prentice-Hall. Englewood Cliffs. NJ, 1963.

[16] A. Downs, Inside Bureaucracy, Little Brown, Boston, MA, 1967.

[17] S. Finkelstein, D.C. Hambrick, A.A. Cannella, Strategic Leadership: Theory and Research on Executives, Top Management Teams, and Boards, Oxford University Press, New York, NY, 2009.

[18] J. Goo, R. Kishore, K. Nam, R. Rao, Y. Song, An investigation of factors that in<sup>fl</sup>uence the duration of IT outsourcing relationships, Decision Support Systems 42 (4) (2007) 2107–2125.

[19] P. Grambsch, T. Therneau, Proportional hazards tests and diagnostics based on weighted residuals Biometrika 81 (3) (1994) 515–526

[20] D.M. Grant, F.C. Payton, Career staging for girls moving toward (away) from computing careers Proc, 2008 Comp. Pers. Res. Conf ACM Press New York NY 2008 pp, 43–49

[21] K.P. Iyengar. 2007. The effect of leadership style on CIO effectiveness, unpublished doctoral dissertation, School of Bus. Admin., U. Texas, Arlington, TX.

[23] Janco Associates, Chief information of<sup>fi</sup>cer job tenure, eJobDescription.com, 2012, (Park City, UT).

[24] R.J. Kauffman, A. Techatassanasoontorn, B. Wang, Event history, spatial analysis and count data methods for empirical research in information systems, Information Technology and Management 13 (3) (2012) 115–147.

[25] I.P. Klein, M.J., Moeschberger, Survival Analysis: Technigues for Censored and Truncated Data, 2nd ed, Springer, New York, NY, 2005.

[26] H. Krishnan, What causes turnover among women on top management teams? Journal of Business Research 62 (11) (2008) 1181–1186.

[27] M.D. Levi, K. Li, F. Zhang, Deal or no deal: hormones and the mergers and acquisitions game, Management Science 56 (9) (2010) 1462–1483.

[28] S. Leaver, CIO job tenure rises: long term trend or <sup>fl</sup>eeting phase? CIO, Mar. 19 2010.

[29] F.J. Mata, W.L. Fuerst, J.B. Barney, Information technology and sustained competitive advantage: a resource-based analysis, MIS Quarterly 19 (4) (1995) 487–505.

[30] McKinsey and Co., Women matter 2013: gender diversity in top management — moving corporate culture and moving boundaries, New York, NY, 2013.

[31] J.R. Meindl, S.B. Ehrlich, J.M. Dukerich, The romance of leadership, Administrative Science Quarterly 30 (1) (1985) 78–102.

[32] S.A. Melnyk, M. Pagell, G. Jorae, A.S. Sharpe, Applying survival analysis to operations management: analyzing differences in donor classes in the blood donation process Journal of Operations Management 13 (4) (1995) 339–356

[33] M.W. Meyer, Change in Public Bureaucracies, Cambridge U. Press, London, UK, 1979.

[34] K.S. Nash, Average CIO tenure slips but still more than four years, CIO, Nov. 11 2007.

[35] K.S. Nash, One in four CIOs <sup>fi</sup>red for performance, CIO, Mar. 11 2009.

[36] M. Niederle, L. Vesterlund, Do women shy away from competition? do men compete too much? Quarterly Journal of Economics 122 (3) (2007) 1067–1101.

[37] L. Ostrowski, M. Helfert, What's next for the CIO? a maturity-based approach, Proc. United Kingdom Academy for Information Systems, Oxford, UK, 2011.

[38] P.A. Pavlou, O.A. El Sawy, The third hand: IT-enabled competitive advantage in turbulence through improvisational capabilities, Information Systems Research 21 (3) (2010) 443–471.

[39] J.L. Perry, H.G. Rainey, A public–private distinction in organization theory: a critique and research strategy, Academy of Management Review 13 (2) (1988) 182–201.

[40] T.C. Powell, A. Dent-Micallef, Information technology as competitive advantage: the role of human, business and technology resources, Strategic Management Journal 18 (5) (1997) 375–405.

[41] J.W. Ross, D.F. Feeny, The evolving role of the CIO, in: R. Zmud (Ed.), Framing the Domains of IT Management: Projecting the Future Through the Past, Pinna<sup>fl</sup>ex, Cincinnati, OH, 2003, pp. 385–402.

[42] G. Shmueli, O. Koppius, Predictive analytics in IS research, MIS Quarterly 35 (3) (2011) 553–572.

[43] D.H. Smaltz, V. Sambamurthy, R. Agarwal, The antecedents of CIO role effectiveness in organizations: an empirical study in the healthcare sector, IEEE Transactions on Engineering Management 53 (2) (2006) 207–222.

[44] J.E. Smith, K.P. Carson, R.A. Alexander, Leadership: it can make a difference, Academy of Management Journal 37 (4) (1984) 765–776.

[45] P.A. Strassmann, The Politics of Information Management, Info. Econ. Press, New Canaan CT 1995

[46] P.A. Strassmann, The cost of short-term CIOs, ComputerWorld, May 5 2004

[47] P. Thibodeau, Why CIOs don't stick around for too long, ComputerWorldUK, Mar 23 2003.

[48] W. Todaro, Want to be a CEO? stay put, Forbes.com, Mar 31 2003.

[49] E. Trauth, J.L. Quesenberry, H. Huang, Cross-cultural in<sup>fl</sup>uences on women in the IT workforce, Proc. SIGMIS Comp. Pers. Res. Conf, ACM Press, New York, NY. 2006.

[50] L. Tucci, IT executive jobs average 6.3 years, a testament to IT and business, SearchCIO Dec 10 2009.

[51] M. Wade, J. Hulland, The resource-based view and information systems research: review, extension and suggestions for future research, MIS Quarterly 28 (1) (2004)107-142

[52] T. Wailgum, The truth about CIO tenure, CIO, Dec. 9 2009.

[53] K. Warwick, A Theory of Public Bureaucracy, Cambridge U. Press, London, UK, 1975.

[54] C. Wood, Government CIO salaries lag behind, contribute to turnover, Government Technology, Aug 17 2011

[55] C. Zheng, D. Lamond, Organisational determinants of employee turnover for multinational companies in Asia, Asia Paci<sup>fi</sup>c Management Journal 27 (2010) 423–443.

Gregory S. Dawson is an Assistant Professor at the W.P. Carey School of Business and is also a Senior Faculty Associate at the Center for Organization Research and Design in the College of Public Programs at Arizona State University. He is a former Partner with PricewaterhouseCoopers (PwC) in the government consulting practice and was also a Director in Gartner's State and Local Government practice. His Ph.D. is from the University of Georgia. His research has appeared in a number of top academic journals including Organization Science and Journal of Management Information Systems as well as in practition er outlet like InformationWeek and Brookings Institution.

Robert J. Kauffman is Associate Dean (Research), Deputy Director of the Living Analytics Research Center, and Professor of Information Systems and Management at Singapore Management University. His M.S. and Ph.D. degrees are from Carnegie Mellon University. He serves as faculty leader for the Area of Excellence on Analytics for Business, Consumer and Social Insights, and teaches in the Masters of IT in Business (Financial Services) on banking products and processes. He recently visited the Tuck School of Business at Dartmouth, was W.P. Carey Chair in IS at Arizona State University, and also was Professor and Chair (Information and Decision Science), and Director (MIS Research Center) at the University of Minnesota, He was on the faculty of the Stern School NYU where he initiated courses on financial IS and technology, His research appears in Operations Research Letters Telecommunications Policy the Review of Economics and Statistics JEEF

Transactions on Software Engineering and IEEE Transactions on Engineering Management, in addition MIS Quarterly, Management Science, Information Systems Research, the Jour nal of Management Information and this journal.

Man-Wai Ho is a senior lecturer at Department of Statistics and Applied Probability at National University of Singapore, and will join Department of Mathematics and Statistics at the Hang Seng Management College in Hong Kong as an Assistant Professor in August

2015. His Ph.D. degree is from Hong Kong University of Science and Technology. He teaches a variety of modules in Statistics and Probability. His research appears in Annals of Statistics, Journal of the American Statistical Association, Journal of Computational and Graphical Statistics, Computational Statistics and Data Analysis, and Annals of the Institute of Statistical Mathematics.
