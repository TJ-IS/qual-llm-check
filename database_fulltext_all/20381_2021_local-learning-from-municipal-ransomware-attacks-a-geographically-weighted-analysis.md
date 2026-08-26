---
otero_id: 20381
otero_key: "A5VQN9VW"
title: "Local learning from municipal ransomware attacks: A geographically weighted analysis"
authors: "Kent Marett; Misty Nabors"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103482"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Local learning from municipal ransomware attacks: A geographically weighted analysis

Kent Marett <sup>\*</sup>, Misty Nabors

Department of Management & Information Systems, College of Business, Mississippi State University, Box 9581, Mississippi State MS 39762, USA

## A R T I C L E I N F O

Keywords: Ransomware Spatial analysis Security behavior Local learning

## A B S T R A C T

The prevalence of security threats like ransomware continues to increase and victimize a wide range of targets, which includes municipal information systems. These attacks are commonly reported in media outlets available in attacked communities. This study seeks to understand how effective news reporting can be toward influencing the behavior of people who live within the proximity of the attack. The results suggest a geographic influence on individual behaviors that could well extend beyond the context of information security into other areas of behavioral IS research.

## 1. Introduction

Early in the morning of May 7, 2019, city leaders in Baltimore, Maryland, were alerted by their Office of Information Technology that internal files critical to the city’s normal operations were suddenly inaccessible. Within hours, the city received a digital demand from hackers who had encrypted important files on city computers using the “RobbinHood” ransomware, with 13 bitcoins to be paid as ransom (roughly the equivalent of \$76,000 US). Determined not to give in to the hackers’ demands, the city contracted with IT consultants to recover the files, ultimately costing Baltimore millions of dollars and weeks in time to restore order [1, 2]. Within days, dozens of articles appeared in local newspapers and reports broadcast over television and radio stations, which described the incident and the aftermath. As the story developed, media attention turned to actions Baltimore citizens should take to protect themselves. Local television station WBAL-TV featured two se curity professionals on their May 13 nightly news telecast who advised viewers to utilize virtual private networks, to change their passwords on a regular basis and to “always back up your data.” The July 2 edition of the Baltimore Sun ran an editorial that advised readers about preventative measures that can be taken before an attack takes place. Whether Baltimore residents took such advice remains to be seen, but attacks on municipal systems are not a singular event, and an increasing number of residents are learning about ransomware, if not by expert recommen dations, by suffering the consequences of each attack.

According to the Department of Homeland Security, ransomware attacks reached record-breaking levels in 2019, with over 200 federal.

state, municipal agencies, public schools, and universities being victimized. Though the cryptographic attack has been known to victimize individuals, medical facilities, and businesses, cities them selves are an appealing target for attackers because of the critical function they serve in all those venues [3]. Local governments have access to significant amounts of data about businesses and residents and with the advent of smart utilities and IoT devices, cities stand to collect even more sensitive data. Preventative measures are indeed the most practical means of reducing susceptibility to ransomware, but cash-strapped cities often lack the resources to allocate toward infor mation security beforehand [4], which is one of the factors increasing target suitability [5]. City-wide information systems are also commonly plagued by security vulnerabilities that include poor encryption (if any) of stored information, the use of unsecure legacy technology, a multi tude of interdependencies and interfaces, and poorly trained employees [6]. A ransomware attack on a municipality is of interest to everyone who lives or works there.

Much has been made of the disruptions that affect the residents of a city whose information systems are infected with ransomware, but what lessons do residents take away from the incident? Does it serve as a cautionary tale that encourages safe behaviors while they are online? Because of its scope, preventing ransomware at a city-wide level is arguably more difficult than it would be for an individual seeking to protect a single computer or home network. However, no prior research appears to have investigated whether the residents of a city fallen prey to ransomware learn cautionary lessons from the victimization of their local government. The research question guiding this study is: “Are individuals in communities targeted by cybersecurity attacks more likely to take precautionary measures to protect their own information assets than nonresidents?”

This study specifically looks at ransomware attacks on the public sector, but the results could apply to attacks on business entities as well. Combining geographical data with the responses from a national survey using a nonexperimental ex post facto study design, the results of this study show that people who live close to an attacked community are more likely to take preventive actions to reduce their susceptibility to ransomware, but the influence of the attack begins to wane beyond 20 miles of the incident. This study stands as an example of the importance of geographical data, which was analyzed here using statistical tools provided by ArcGIS 10.3.1 and GWR4. The results are discussed in relation to research on information security and the larger field of in formation systems.

## 2. Theory

One important conceit found in research on behavioral information security is the connection between awareness of security issues and motivation for individuals to engage in safe behaviors while online. Some studies have examined organizational resources that can be useful to increase awareness among employees [7,8], while others have investigated how individuals become aware of threats outside the workplace [9,10]. According to the Rational Choice Model of informa tion security, individuals determine whether they will either perform safe practices in the hopes of avoiding negative consequence or they will choose riskier behaviors to avoid inconveniences and additional costs [11]. This choice is considered to be guided heavily by the awareness of potential risks through information from outside sources, including but not limited to training, one’s peer group, and, of central interest to this study, news, and media attention.

Research on awareness campaigns and fear appeal messaging follows this line of thinking, and the need to determine effective means of communicating information about threats and countermeasures to in dividual computer users is chief among the goals of studies in this area. In that vein, local news outlets are among the main ways for organizers, consultants, and experts to direct communication toward an otherwise naive public [12,13]. When compared with network and cable news outlets, local news seems to be important for not only increasing awareness and engagement on a particular topic among the local populace, it is effective for developing knowledge transfer in frastructures throughout the community [14], or put differently, news spreading by “word of mouth.” For community residents to learn about the consequences of ransomware and ways to prevent its visit on them personally, local news outlets would seem to be a viable means for se curity experts to do so.

The premise behind this study is the concept of local learning, which is defined as the propensity to seek new knowledge from proximate neighbors as opposed to distant strangers [15]. Local sources of knowledge are preferred by many for learning purposes due to past experiences with one’s neighbors eventually leading to routinized (and convenient) searches [16,17]. Gallaud and Torre [18] speculated that geographical proximity to knowledge is perhaps its most meaningful influence during the early phases of learning when the hopeful learner, with interest level raised, is attempting to gain an initial foothold on a topic and casts about for local sources to mimic. This view fits the perspective taken by this study, that Internet users who reside in a community attacked by ransomware have their interest piqued by the attack and then are subsequently influenced by the actions taken by local leaders in the hopes of preventing a similar attack in the future.

![](/api/attachments/A5VQN9VW/fulltext/images/89583e62edcdb824032efef9cc20c47a9696ab759829829f587efa069c9691d8.jpg)  
Fig. 1. Conceptual Model.

One theory base that supports the concept of local learning is derived from Social Learning Theory, which itself helps explain how individuals in unknown situations can learn from observing how others behave in the same environmental conditions [19]. This “vicarious capability” is attractive because it allows for learning without expending the time, resources, and mobility that would otherwise be needed for experiential learning and personal trial and error [20]. Vicarious learning from others can certainly supplement one’s own personal experiences, but when personal experience and knowledge may be insufficient, vicarious learning serves to reduce uncertainty by searching for similar others choices and then to either attempt others’ successful actions or avoid others’ mistakes [21]. Thus, vicarious learning is influential during the assessment of an observed risk and subsequently, leads individuals to ward solutions meant to help mitigate the risk.

As with other concepts and theories used to explain IS phenomena, social learning theory and vicarious learning have been employed in studies crossing levels of analysis, and an examination of the literature helps contextualize the theory for use on the individual level [22]. For instance, previous organizational level literature reports that managers in firms learn from the failures of others and subsequently attempt to apply the knowledge gained from failures to their own processes and practices [23–25]. However, security researchers focusing on the indi vidual level security have stressed the importance of vicarious learning from others for supplementing individuals’ perceptions like self-efficacy and response efficacy in the face of preventing online threats [26,27]. Incorporating theory that has been used in previous studies focused on different levels of analysis can often be a concern, but because vicarious learning was originally developed in the context of individuals relying on similar others for best (and worst) practices as a roadmap on how to proceed in unfamiliar territory, there is no need to relax any assump tions related to the theory to fit the level of analysis for this study [28, 29].

Fig. 1 given below graphically depicts a conceptual model developed from the previous discussion and provides the foundation for the following hypotheses.

## 2.1. Hypotheses

For multiple reasons discussed below, this study argues that local victims of ransomware, particularly those in charge of civic government, can make effective cautionary tales for individuals to learn vicariously from. First, learning from other nearby sources reduces search costs associated with obtaining desired information [30]. A second reason is that potential learners also lean on local sources of information due to familiarity and repeated personal interactions with the subject [31]. Indeed, research on small businesses who hope to learn best practices to improve information security has shown that local entities can serve as the most attractive sources due to convenience [32]. Individuals simi larly draw from local sources for knowledge and examples of secure behavior, likely due to feelings of community support and solidarity when facing threats [33]. Finally, ransomware attacks tend to receive a great deal of media attention in its aftermath, and the disruption would be expected to be of interest to local citizens. On average, individuals tend to be more aware of a specific news event and the relevant details around it when it is proximate [34]. Construal level theory also supports the notion of local learning by positing that a decreased psychological distance of an incident leads the way for a low-level construal (more concrete) perception of the attack [35]. Thus, local interest in the subject of ransomware, how it was contracted, and how it can be prevented is likely heightened when an attack occurs locally.

What is not clear at this point is the geographical extent to which local learning (if it exists) can be expected to occur. To that end, GIS researchers have identified distance decay as a factor that can also limit the influence that a localized event has on perceptions, values, and motivations based on the distance between individuals and the event (e. g., [36,37]). Simply put, distance decay regards the increase of spatial dispersion between an individual and a geographical point of interest as a barrier that diminishes resource and attentional allocation [38]. Dis tance decay may not only erode interest in an event, it can also reduce the quality of information describing the event [39]. It should thus be expected that the motivation to behave cautiously, which results from a local ransomware attack will decay the further from the attack an in dividual resides. Thus:

Hypothesis 1. The level of precautionary behavior meant to prevent a ransomware attack will be higher for residents living in previously attacked communities than for individuals living outside the community.

This study also explores whether factors influencing an individual’s precautionary behavior are differently influential depending on the person's location. Should a factor like distance from an attacked city be identified as significantly influential toward precautionary behavior, that influence can subsequently be analyzed for spatial heterogeneity, which refers to the variance in a factor’s influence based on the location in which it was measured [40]. Traditional regression modeling follows the assumption that the influence of variables remains stationary across the area of a study and is not sensitive to local variations [41]. This assumption of stationary influence can be tempting for researchers to follow, as pointed out by Huang and Leung [42], “from the practical point of view, the simpler a model, the easier it can be applied and interpreted” (p.244). However, not determining whether the influence of variables can drift geographically can potentially omit explanatory power from a regression model. More to the point, traditional regression models produce parameter estimates that are global in nature, whereas geographically weighted models can produce local statistics that disaggregate the global estimates.

Although geographically weighted analyses have rarely been con ducted within the field of information systems, some IS researchers have found that regional and cultural differences can permeate attitudes that affect decision-making, behaviors, and ultimate usage of an information system [43–45]. With security behaviors in mind, an analysis of spatial heterogeneity would attempt to determine if security precautions taken by individuals in a particular locality are more influenced by explana tory variables such as distance from a ransomware attack than other locations. The rationale behind and subsequent explanation of whether or why the influence of a specific factor toward security precautions varies by location would be of obvious interest. Some research suggests that security priorities within a community are shaped by past crime frequency [46] or by the attitudes of one’s neighbors [31], but whether proximity to a ransomware attack can be predicted to influence security precautions differently across locations remains to be seen. To our knowledge, no existing theory informs a geographically weighted prediction.

In circumstances where no theoretical foundation would form the basis of geographically weighted directional predictions, significance testing would be most informative when the results of geographically weighted regression modeling are compared with those of a standard regression model [47,48]. It is recommended that, due to the explor atory nature of such a comparison, predictions should take the form of a null hypothesis that expects no significant improvement in the phe nomenon of interest due to the geographically weighted model. Therefore:

Hypothesis 2. The influence of distance from a previously attacked community on precautionary behavior to prevent a ransomware attack will not vary by location.

## 3. Methodology

The methods used to conduct this study involved a sequence of analysis techniques similar to those found in previous studies that feature spatial analysis [49–51]. To test Hypothesis 1, an ANCOVA was performed to compare groups of respondents classified by their distance in miles from the nearest victimized city on their precautionary behavior. The groups were organized using the Near function in ArcGIS Pro-and exported to SPSS 25 for mean comparison. The group of re spondents within a 20-mile radius of the attacked city was classified as “local residents.” Potential covariates were collected through a review of relevant security literature and, when found to correlate with security precautions, were retained for the analysis.

Multiple analyses were conducted to test Hypothesis 2. First, step wise regression through ordinary least squares (OLS) available in ArcGIS Pro-helped rule out alternative candidate variables, which is paramount for making causal inferences when independent variables have not been artificially manipulated. This not only controlled for the possible explanatory power of alternative variables and added robustness to the earlier correlational analysis, stepwise OLS also served to reduce the amount of variance explained by the independent variable of interest, while likewise reducing the likelihood of alternative explanations. The OLS ultimately produced a stationary regression model in which the influence of the candidate-independent variables could be bench marked. However, because the sample was composed of respondents located throughout the United States, subsequent analyses helped determine whether spatial heterogeneity was present in the data. This was done by calculating a statistic reporting the level of spatial auto correlation found in the overall population, Global Moran’s I, and by assessing other diagnostic statistics (e.g., Koenker’s BP) that can indicate spatial nonstationarity. Should nonstationarity be found, geographically-weighted regression (GWR) is employed to determine which variables in the regression model vary substantially based on the location of the data point.

## 3.1. Study design and sample

The research design is described as a comparative ex post facto con trol group study, a design which belongs to a subset of factorial designs typically employed for exploratory research in which pre-event phenomena cannot be observed due to the unpredictability of the event or experience [52]. The ex post facto design is appropriate when true experimental research is not possible to plan a priori as with phenomena occurring in natural settings [53]. Participants are compared based on naturally occurring comparative factors with little to no researcher control over the selection of participants nor over their assignment to treatment groups. Instead, a participant’s membership to a group has occurred before the study is initiated. This study design was selected here for two reasons. First, similar to other threats to information se curity, ransomware attacks occur with some frequency but the targets are seldom predictable. Second, participant proximity to the attacked cities serves as the comparable factor for analysis in this study, but the assignment of participants to treatment groups was based on their place of residence, which was determined beyond the bounds of this study. Random assignment to groups is not possible under these circumstances.

![](/api/attachments/A5VQN9VW/fulltext/images/003cb6b3a5f177b7f6f30043d1e2ed7a28eebc988a61d314ccb11fcb6d0a6559.jpg)  
Fig. 2. Map of US cities attacked by ransomware in 2019.

Participant data were collected through a cross-sectional survey of American Internet users over the age of 18 years. A company that spe cializes in survey panel research was contracted with to provide a nationwide sample. In all, 430 completed online surveys were received and used for data analysis. A nationwide sample was achieved as re sponses were received from 46 of the 50 states. The overall sample was composed of 50.9 percent female respondents with a mean age of 56.1 years. Respondents reported living an average of 22.4 years in their current community. Three respondents from Alaska were located over 1300 miles from the nearest attacked community; therefore, they were deemed as outliers and removed from the analysis.

A list of 112 municipalities whose public information systems were attacked with ransomware in 2019 was compiled from news articles originating from a number of different news sources, including National Public Radio, the New York Times, and CNET, but the most compre hensive source was an interactive map of victimized cities maintained by StateScoop.com. The attack period was limited to 2019 to reduce any possible decay effects due to time. Fig. 2 displays the municipalities infected with ransomware during that year. As the figure depicts, victimized cities were geographically spread across the country in 37 different states. All 112 attacked communities are located within the continental United States as no incidents were reported for the states of Alaska and Hawaii. The attacked cities ranged in size from major metropolitan areas like New York City, Boston, and Atlanta to rural towns like Roby, TX (population 619) and Sugar City, ID (population

1347).

The targets of the ransomware varied as well. The most frequently attacked municipal systems belonged to local public school districts (54 of the 112, or 48.2%), followed by city government systems (38), local law enforcement agencies (5), county offices, municipal libraries, and 9–1-1 emergency call centers (3 each). Two municipal airports suffered ransomware attacks, with the remaining solitary attacks on a parks and recreation system, a street department, a fire department, a city property appraiser, and a public defender’s office.

## 3.2. Data

The independent explanatory variable, proximity to municipal ran somware attacks, was based on the geographical location of each respondent. Using the coordinates associated with each returned survey and confirmed by each respondent’s zip code, respondents were iden tified as living within a 20, 50, or 100 mile radius of an attacked com munity. These distance ranges resulted in fairly equitable sample sizes for each group. The coordinates for the community itself were centered on the city hall or other main municipal building where civic leaders and decision makers would be expected to have offices. Respondents within 20 miles of this building were classified as “residents” of the attacked community, a radius that captures both the urban, downtown area and the average commute distance for people living in suburbs of larger American cities [54]. Several attacked communities, including Jeffer son, GA, Paris, TX, and Thompson Falls, MT, were not among the nearest incidents for any of the respondents.

The dependent variable, precautionary behavior, was composed of recommended preventative measures compiled from previous studies on ransomware [55,56]. The behaviors consisted of backing up files, stor ing files in a separate location, regularly patching operating systems, installing a host-level firewall, enabling filters on email accounts, cautiously opening email attachments only if expected, and not visiting unsolicited website addresses. Each behavior was measured through a 7-point Likert scale ranging from strongly disagree to strongly agree, with the behaviors then being averaged to represent the extent of pre cautionary behavior.

Other measures that represent candidate variables sought to capture other possible motivators of precautionary behavior. Candidate vari ables represent potential influences on the variance of the dependent variable of interest but whose relevance may or may not be known a priori [57]. To measure the respondent’s prior experience with security threats, Likert scale items were used to assess whether they had been personally victimized by ransomware, spyware, phishing, computer vi ruses, and unauthorized access to their computer. These particular threats are consistently identified by security firms as dangers to per sonal computer security and the National Conference of State Legisla tures specified these threats as the focus of criminal legislation across the United States, which exhibited their relevance to all survey respondents. To assess how respondents engage in personal information security learning efforts, Likert scale items appropriated from Wright and Marett [58] gauged the extent to which they read news about information se curity, discuss security issues with others, seek advice from technology websites, follow security issues on social media, and read about local security issues. Finally, self-reported demographic data for each respondent and community-level data for both victimized cities and the locale for each respondent was drawn from the US Census Bureau, and these measures were among those considered for possible control vari ables. Descriptive statistics and item weights for these candidate vari. ables are reported in Table 1.

Table 1  
Items and descriptive statistics for the dependent variable and the candidate variables included in the exploratory analysis. Means (standard deviations).

<table><tr><td>Dependent Variable: Precautionary Measures to Prevent Ransomware(composed from recommendations [55, 56])I currently take the following precautions with my computer:</td><td>M = 5.11SD = 1.25</td><td>ItemWeights(all p&lt;0.001)</td><td>VIF</td></tr><tr><td>I back up files from my computer on a regular basis.</td><td>4.78 (2.0)</td><td>0.235</td><td>2.76</td></tr><tr><td>I store my backup files in a separate location.</td><td>4.50 (2.1)</td><td>0.227</td><td>2.61</td></tr><tr><td>I update my computer&#x27;s operating system regularly with recommended patches.</td><td>5.21 (1.8)</td><td>0.230</td><td>1.78</td></tr><tr><td>I have installed a personal firewall on my computer.</td><td>4.58 (2.0)</td><td>0.207</td><td>1.70</td></tr><tr><td>I have enabled filters on my email account.</td><td>4.59 (1.8)</td><td>0.213</td><td>1.74</td></tr><tr><td>I cautiously open email attachments ONLY if I expect them to be sent to me.</td><td>5.94 (1.4)</td><td>0.166</td><td>1.48</td></tr><tr><td>I do not follow unsolicited website addresses that have been sent to me.</td><td>6.18 (1.3)</td><td>0.149</td><td>1.43</td></tr><tr><td>Candidate Variable: Personal Efforts to Learn about Information Security (adapted from [58])</td><td>M = 4.08SD = 1.38</td><td></td><td></td></tr><tr><td>I follow news and developments about information security.</td><td>4.56 (1.6)</td><td>0.258</td><td>2.51</td></tr><tr><td>I discuss with friends and people around me various security issues of the Internet.</td><td>3.90 (1.7)</td><td>0.267</td><td>2.39</td></tr><tr><td>I read about the problems of malicious software that intrude Internet users&#x27; computers.</td><td>4.56 (1.6)</td><td>0.266</td><td>2.71</td></tr><tr><td>I seek advice on computer websites about information security solutions.</td><td>3.84 (1.7)</td><td>0.254</td><td>2.02</td></tr><tr><td>I read about information security issues on social media.</td><td>3.52 (1.9)</td><td>0.191</td><td>1.35</td></tr><tr><td>Candidate Variable: Personal Experience with Security Threats (Formative)</td><td>M = 2.84SD = 1.48</td><td></td><td></td></tr><tr><td>I have had personal experience with spyware.</td><td>2.64 (1.9)</td><td>0.268</td><td>1.88</td></tr><tr><td>I have had personal experience with ransomware.</td><td>2.03 (1.6)</td><td>0.288</td><td>2.12</td></tr><tr><td>I have had personal experience with phishing.</td><td>3.36 (2.2)</td><td>0.261</td><td>1.74</td></tr><tr><td>I have had personal experience with computer viruses.</td><td>4.00 (2.2)</td><td>0.260</td><td>1.67</td></tr><tr><td>I have had personal experience with outsiders who access my computer without authorization.</td><td>2.16 (1.7)</td><td>0.237</td><td>1.48</td></tr></table>

## 3.3. Validity checks

Before analyzing the data, steps were taken to ensure the internal validity of the study. Respondents were asked whether the city in which they lived had been victimized by ransomware within the past 12 months, the time period represented by the study. The group of local residents was the most likely of the distance bands to be aware of an attack on their own city, though their affirmative responses were not unanimous as would be expected (78%).

To ensure that residents of each attacked municipality could have been exposed to news coverage of the ransomware event, we verified that each of the 112 municipalities were covered by local media outlets that include newspaper, television, and radio outlets in each market. The search was conducted with the help of news aggregation websites and reports archived on YouTube. At least one media outlet was identified in every case. Overall, 352 media outlets were identified for a total of 606 news stories on the ransomware attacks, for an average of 3.14 outlets and 5.41 stories for each attacked municipality. Figs. 1 and 2 in the Appendix display screencaps from example television news reports of ransomware attacks on their communities.

Because the particular factorial design used in this study could be susceptible to threats to internal validity, including but not limited to selection bias, steps were taken to determine whether pre-existing characteristics belonging to the participants could have led to incom parable groups and unduly swaying the results. First, each treatment group was compared based on the demographic variables collected from each response. This helps detect unintended “alternate independent variables” that serve to confound the results [59]. Chi-square tests on the basis of sex and race showed no disparities between groups, with the only significant difference found for education level was more “local residents” having a college degree than respondents living between 50 and 100 miles from an attacked city (p = 0.041). Similarly, one-way ANOVA confirmed that there was no significant difference in age be tween the groups, though one significant difference was found for tenure living in current location, with respondents living over 100 miles from an attacked city having less tenure (M = 17.9 years) than respondents living between 25 and 50 miles from an attacked city (M = 26.7 and p <

Interconstruct correlations. NOTE: \*\* p < 0.01.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td colspan="9">1. Distance</td></tr><tr><td>2. Personal Efforts to Learn</td><td>-0.02</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Previous Experience with Threats</td><td>-0.03</td><td>.45**</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Age</td><td>.04</td><td>-0.04</td><td>-0.06</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Sex</td><td>.01</td><td>-0.08</td><td>-0.09</td><td>-0.19**</td><td></td><td></td><td></td><td></td></tr><tr><td>6. Tenure in Community</td><td>-0.08</td><td>-0.01</td><td>-0.01</td><td>.25**</td><td>-0.01</td><td></td><td></td><td></td></tr><tr><td>7. Time Since Closest Attack</td><td>-0.05</td><td>.29**</td><td>.26**</td><td>-0.18**</td><td>-0.01</td><td>-0.01</td><td></td><td></td></tr><tr><td>8. Precautionary Behaviors</td><td>-0.06</td><td>.46**</td><td>.31**</td><td>-0.01</td><td>-0.10</td><td>-0.02</td><td>.11</td><td></td></tr></table>

Table 3  
ANCOVA results for precautionary behavior.

<table><tr><td>Distance from Nearest Attacked Community</td><td>N</td><td>Means (SD)</td><td>Group Comparison w/ Local Residents</td></tr><tr><td>Within 20 Miles (“Local Residents”)</td><td>102</td><td>5.36(1.1)</td><td>-</td></tr><tr><td>21–50 Miles</td><td>105</td><td>5.06(1.3)</td><td> $F = 2.09$ </td></tr><tr><td>51–100 Miles</td><td>109</td><td>5.04(1.2)</td><td> $F = 3.01$ </td></tr><tr><td>Outside 100 Miles</td><td>114</td><td>5.01(1.2)</td><td> $F = 4.27^{*}$ </td></tr></table>

NOTE: \* $\dot { p } < 0 . 0 5 .$

0.001). Neither of these isolated demographic differences seemed likely to undermine the subsequent analyses. Next, a Levene’s test of hetero geneity was also conducted to help assure that the behaviors in one of the treatment groups did not vary more than the behaviors in the other groups for some unforeseen reason. The Levene’s test was not significant (0.844 and p = 0.716), meaning that variances in the dependent variable were not significantly different between groups.

## 4. Results

To test Hypothesis 1, we first assessed bivariate correlations between individual demographics, personal efforts to learn about security, per sonal experience with threats, and the amount of time since the ran somware attack closest to them (whether a resident or not) with the dependent variable. The results of the interconstruct correlations are provided in Table 2. Variables with significant correlations with the dependent variable were then included in the analysis as covariates, and the subsequent ANCOVA removed the influence of those variables from the main effect comparison.

Precautionary behavior motivated by distance from the ransomware event was then analyzed through ANCOVA. The only significant corre lations between the individual and community-level variables with precautionary behavior were for efforts toward personal awareness (r = $0 . 4 5 9 ^ { * * } )$ and prior experience with security threats $( r = 0 . 3 0 8 ^ { \ast \ast } ) ;$ therefore, those two variables were retained as covariates. The time elapsed since the attack occurred, measured in months, was not significantly correlated with the dependent variable $( r = 0 . 0 1 0 )$ . After removal of the influence of the covariates, the omnibus ANCOVA model was significant $( F = 3 1 . 4 1 ^ { * * * } )$ . Bonferroni tests comparing precau tionary behaviors between the distance groups were then conducted to test Hypothesis 1. As displayed in Table 3, the only significant difference in precautionary behavior between residents and the other groups was with those respondents outside a 100-mile radius of the attacked com munity, though comparisons of local residents with the other two groups of nonresidents very nearly approached significance. The results provide partial support for Hypothesis 1.

Table 4 Results of OLS analysis.

<table><tr><td></td><td>Unstandardized Coefficient</td><td>Standard Error</td><td>t-statistic</td><td>VIF</td><td>Variance Explained</td></tr><tr><td>Distance (categorical)</td><td>-0.08*</td><td>0.04</td><td>-1.92</td><td>1.00</td><td>0.01</td></tr><tr><td>Prior Experience with Security Threats</td><td>0.10*</td><td>0.04</td><td>2.63</td><td>1.25</td><td>0.09</td></tr><tr><td>Personal Learning Efforts</td><td>0.36**</td><td>0.05</td><td>7.50</td><td>1.25</td><td>0.20</td></tr><tr><td colspan="6">F (3426) = 42.46** Wald-Stat = 118.45***</td></tr><tr><td colspan="6">R2 = 0.23 Adjusted R2 = 0.22</td></tr><tr><td colspan="6">Koenker BP = 25.09***</td></tr></table>

\*\*\* p < 0.001 \*\* p < 0.01 $^ { \ast } p < 0 . 0 5 .$

![](/api/attachments/A5VQN9VW/fulltext/images/6b7a1f7a7c4c1e6d0334d2e15956d56c0e660885f1d4ae162ba087a2797eecd9.jpg)  
Fig. 3. Sample map of standardized residuals within distance ranges.

Table 5  
ANOVA results comparing OLS and GWR models.

<table><tr><td>Source of Variation</td><td>SS</td><td>DF</td><td>MS</td><td>F</td></tr><tr><td>OLS Residuals</td><td>520.63</td><td>426</td><td></td><td></td></tr><tr><td>GWR Improvement</td><td>12.31</td><td>5</td><td>2.25</td><td></td></tr><tr><td>GWR Residuals</td><td>508.31</td><td>420</td><td>1.21</td><td> $1.86^{\dagger}$ </td></tr></table>

NOTE: † significant at the 0.10 level.

As discussed earlier, a regression analysis was conducted to deter mine the extent to which proximity affects the preponderance to take precautionary measures against ransomware as well as to statistically control for potential confounding variables. Two tests were conducted, with the first being OLS to identify potentially influential variables and to assess any spatial multicollinearity in the measures [60]. It is first recommended to check the dependent variable for spatial autocorrela tion, which indicates that the values of a variable are randomly distributed across a geographical area, by assessment of the Moran’s I statistic for the global regression model. A dependent variable with significant positive Global Moran’s I would be found in clusters where high values are proximate to high values and low values proximate to low values, while a significant negative score would exhibit high and low values interspersed in a predictable “checkerboard” pattern across the landscape [61]. However, the Global Moran’s I statistic here was not significant in either direction (z = 1.10 and $p = 0 . 2 6 )$ , which suggests that precautionary behavior appears to be distributed evenly across the country. Likewise, the low variance inflation factor (VIF) scores (all under 7.5) in the explanatory variables indicated that multicollinearity was also not an issue.

The results of the OLS analysis are reported in Table 4. An explor atory regression model showed that, as with the earlier correlational analysis, the demographic and community-level variables were again not significant; therefore, they were omitted from the final OLS model. No multicollinearity was present in either of the formative variables, with the VIF for both were reported as less than the 3.3 standard [62]. The corrected Akaike’s Information Criterion (AICc) serves as a measure of comparative model fit, with lower scores that suggest a more appropriate fit [62]. The AICc for the OLS model was 1312.80. The re siduals for each respondent were mapped for visual inspection using ArcGIS, and a sample map is displayed in Fig. 3. The residuals serve to identify whether the observed data are adequately explained by the predicted factors [63], and the figure displays the precautionary be haviors that occur within the distance band categories as predicted.

One statistic resulting from the OLS model, Koenker’s studentized Breusch-Pagan or KBP, was found to be statistically significant, indi cating that one or more of the independent variables may not maintain a consistent relationship with the dependent variable across geography. This, in turn, suggests that a geographically weighted model may be preferable to a stationary regression model [51,64]. Thus, the significant KBP makes the regression model an appropriate candidate for GWR analysis, which is concerned with the possibility that significant factors have differing degrees of influence depending on the geographical

location [47,65].

To achieve comparative results, the same variables entered in the OLS model were entered in the geographically weighted regression analysis available in the GWR4 software package [66]. The evaluation criteria for comparing the OLS and GWR models recommend a minimum three-point difference in the calculated AICc between the models, with larger R2s, lower residual sum of squares, and smaller Moran’s I for the residuals all indicating the preferred model [67,68]. The GWR analysis indicated a decrease of 3.6 in the AICc (1309.51) over the OLS model, which surpasses the recommended difference needed for further com parison. In terms of the comparative results, there was a slight increase in the variance explained (GWR $\mathrm { R } ^ { 2 } = 0 . 2 5$ vs. OLS $\boldsymbol { \mathrm { R } } ^ { 2 } = 0 . 2 3 )$ and a decrease in the Moran’s I (GWR 0.033, z = 0.29 vs. OLS 0.035, z = 0.31), which suggest that the GWR model better fits the data. Hypothesis 2 itself was tested using an ANOVA that compares the residual sums of squares of the OLS and GWR models [49,68]. The results of the ANOVA are reported in Table 5. While an improvement over the OLS (and thus, offering evidence of spatial variation in one or more independent vari ables), the GWR model as a whole only approached a statistically sig nificant improvement.

Upon examination of the independent variables under GWR, the source of the geographical bias appeared to be the personal learning variable as it was the only variable with a negative geographical dif ference criterion (− 4.89). In other words, personal learning seems to have a significantly different influence on precautionary behavior in some locations than in others. In contrast, the distance of the individual from the attacked municipality had a stationary effect on precautionary behavior regardless of where the survey respondent was located around the country. Based on the consistent stationary results for the distance variable alone, there is no evidence to reject the null Hypothesis 2.

We note the concerns with making strong inferences using GWR results [69], particularly with regard to the disparate numbers of ob servations across a geographical area and the lack of normal distribu tions in the independent variables that likely results from that. Thus, in keeping with the exploratory nature of the GWR approach, we hesitate from hypothesizing further about geographically weighted influence of each independent variable, an issue referred to as the “roving hypothesis test” [48]. Thus, following the recommendations of Fotheringham and Oshan [68], we followed up the significant GWR result for personal learning efforts by assessing the data for outliers. Anselin’s [40] Local Indicators of Spatial Autocorrelation (LISA) statistics were produced to map the respondents for clustering effects and outliers in the three in dependent variables, the results of which can be found in Appendix B. This post hoc assessment did not uncover evidence of undue autocorre lation in the GWR results for the three variables.

To summarize the results, an ANCOVA showed that residents who are within 20 miles from a community attacked by ransomware are significantly more likely to have taken precautionary measures for protection than individuals over 100 miles away. Though the other distance groups (people living 20–50 miles and people living 50–100 miles from the attacked city) were not significantly different than the resident group, the self-reported precautionary behavior was still, on average, higher for residents. Subsequent regression analyses indicated the distance from the attack, along with personal experience with cyberattacks and personal learning about cybersecurity, has a significant influence on the tendency to take precautionary measures. A geographically weighted analysis suggested that, among the three in dependent variables, only personal efforts to learn may have a varying influence that depends on the location.

## 5. Discussion

With regard to the research question stated earlier: “Are individuals in communities targeted by cybersecurity attacks more likely to take precautionary measures to protect their own information assets than nonresidents,” at best this study provides evidence that a relationship between distance and precautionary behaviors may indeed exist and at worst the relationship cannot be dismissed out of hand. As is discussed below, the question of causality remains, but given the unpredictable nature of ransomware attacks, the use of naturally pre-existing group assignments is the most viable study design available if ransomware is to be studied in the field. On the other side of the coin, experimental de signs could help establish a causal relationship but would leave aside the elements of realism and practicality [69]. This study makes the first meaningful effort to address the research question and provide a foun dation with which studies with alternative research methodologies can build upon, a methodical approach that is necessary in the social sciences.

The results here found that people living within 20 miles of the attack report behaving more cautiously than those living outside of a 20-mile radius and significantly more cautiously than people living beyond 100 miles. This finding came after removing the effects of prior expe rience with threats and personal efforts to independently learn about information security. Personal efforts toward learning about security appeared to explain the most variance in individual precautionary be haviors. Prior victimization had a smaller influence on precautionary behaviors than awareness effort, which parallels findings that one’s experience with cybercrime does not always encourage future precau tionary efforts [70]. However, the sample in this study had relatively low experience with ransomware, with less than seven percent of the respondents claiming to have fallen victim to that particular threat; therefore, a pool composed of more victimized respondents may exhibit a larger influence.

With regard to the effects of distance, the findings support the prior conceptualization of local learning that, while not focused on security breaches and their consequences, do argue for individuals making the use of proximate, convenient sources of knowledge, and best practices. Though none of the survey respondents in this study reported working for the local government, some of the self-reported data hinted that they were still aware of the attack on their municipality. For the overall sample, there was a significant correlation between precautionary behavior and regularly following local news (r = 0.24 and p < 0.001). This helps support why, of the people living within 20 miles of an attacked community (the “local residents”), only 22 percent incorrectly claimed that their community had not been held ransom.

## 5.1. Contribution to research

The contributions of this study to research, particularly in the area of information security, are two-fold. First, the results suggest an unex pected but beneficial consequence of ransomware, albeit a costly benefit. Residents of attacked communities did report taking more precautions to ward off the possibility of contracting ransomware, showing a meaningful improvement in personal information security over people living in their surrounding areas. This particular result ex pands on previous research on information security that posits that one’s social influences help motivate proactive security behaviors [71,72] by offering a spatial component to one’s circle of influences. Being geographically proximate to a victim of ransomware could be further motivation for an Internet user to take precautions. Even if the victim is not personally known to an Internet user, the fact that a fellow community member could be attacked increases the possibility that it could occur again more salient.

Other explanatory variables were uncovered in the analysis. Though distance from an attacked community was found to be a significant in fluence, it paled in comparison to the amount of variance explained by an individual’s personal efforts to independently learn how to prevent ransomware. With regard to the spatial variation found through the GWR analysis, it is worth noting that heterogeneity in the candidate factors was not found for a person’s distance from a community attacked by ransomware. No matter which region of the country, local residents living within 20 miles of an attacked community reported taking extra precautions to prevent ransomware afterward. Instead, the influence of a person’s independent efforts to personally learn more about ransom ware and similar attacks did vary based on geography. Observing the call to better account for spatial variations in information systems phenomena [43], the results of the GWR analysis indicated there are regional differences in how at least one of the model’s explanatory variables, personal learning efforts, influences individual precautionary behaviors. Future research examining this result would be helpful to ward investigating whether personal learning efforts could lead to the residents of a particular community becoming a more difficult target for future attackers.

The notion of local learning from a nearby incident is not without its critics. Wagner et al. [73] argue that favoring local sources of knowledge and best practices can lead to path dependencies that serve to limit subsequent options for individuals and organizations. With the liber ating effects of technology in mind, Torre [74] introduced the argument of “death of distance,” which suggests that online epistemic commu nities surrounding a particular topic of interest are a more practical way of spreading knowledge on a subject than mere physical proximity. For instance, as far as television news is concerned, more Americans claim to watch local news than network and cable news telecasts, but an increasing percentage of people now claim social media platforms as their main source for news and not necessarily the traditional local news outlets [75]. Whether social media offers a sufficient amount of local news coverage for a resident to be properly informed is arguable. Going a step further, the “death of time” may be equally important, given that interest in an attack may naturally wane as time elapses. The 24 h life span for news stories may lead to stories on ransomware being quickly forgotten. Future research would be much needed to test the decay ef fects of time and distance in the age of Internet news further [76].

The second main contribution to research made by this study is to serve as an example of addressing a geographical research topic with a geographical research approach, something that may not always be properly acknowledged in information systems research in general. As others have pointed out [43,77], phenomena occurring in the field of information systems are often assumed to be homogeneous across in dustries, organizations, cultures, and locales, but blindly accepting that assumption may exclude a large degree of our potential understanding about a subject. The results of this study show that assuming that American Internet users, no matter where they happen to reside, will learn from the individual cautionary tales played out in Atlanta, Balti more, and Lubbock is wishful thinking at best.

## 5.2. Contribution to practice

The results of this study are also noteworthy given that information security is not bound by geographic barriers, either natural or manmade. No mountain ranges or oceans prevent threats like ransomware from occurring in a particular locale, and national boundaries have likewise not been found to prevent ransomware [78,79]. Only foresight and preventative planning can effectively reduce the likelihood of many cybersecurity attacks being realized, and the proximal behavioral dif ferences found in this study that vicarious learning could be a worth while means of motivating individuals and businesses to consider improvements to their security planning. A related question that re mains unanswered is whether attackers using methods like ransomware have determined if attacking organizations in the same locale in suc cession is worth the effort if a previous attack has established a form of “vicarious immunity” within the community. If a municipality gains some degree of protection following a ransomware attack on its public information systems, civic leaders would do well to remember that the blame that they may receive for being vulnerable, fairly or not, can be accompanied by the benefit of local residents becoming more aware of online dangers and an increased likelihood of taking protective measures.

This study was conducted exclusively within the United States, but ransomware is a global problem. We were able to conduct this study due to the news reporting of attacks on American municipal targets, but similar reporting in other countries appears to be inconsistent at best. Future studies examining the aftermath of these attacks should consider cultural differences in security attitudes, starting with the tendencies of people to either be overconfident in their security behavior or under the belief that they themselves are not likely to be victimized [80]. Either of those attitudes are disputable and, if incorrect, can lead to severe con sequences. Other studies have found cross-cultural differences in secu rity behaviors displayed by employees even inside organizations that insist on compliance [81,82]; therefore, chances are that those differ ences are even more exaggerated between individuals outside the workplace. If the public reporting of ransomware attacks in other countries becomes more consistently available, future research that examines local learning and security behaviors across cultures could produce further insights into how individuals may differ when vicari ously observing the attacks perpetrated on others.

The results are not without their limitations, and any interpretations drawn from the results should acknowledge the following. The behav ioral data were collected through the use of a cross-sectional survey, which is limited in terms of inferring a causal influence due to the ransomware attack. We do know, however, that the ransomware attacks in this study predated the data collection, and efforts were made to account for alternative causes like experiential learning. Admittedly, to establish the temporal order of variables is not alone sufficient to claim causality. The presence of a significant relationship between the vari ables, the theoretical rationale predicting and explaining the relation ship, and evidence that alternative factors did not influence a spurious relationship between the hypothesized variables are also necessary, even if they can only provide “markers of casuality” [83]. Instead, the most that can responsibly be claimed from the results of this study is that one’s distance from an attacked community is associated with the like lihood one will take precautions, but whether the attack actually caused precautionary behavior is left for longitudinal surveys or experimental research to establish, however, unlikely that is to occur, given the unpredictability of ransomware attacks.

Another limitation of the study is that the extent of the precautionary behavior was also self-reported, which lacks the assurances that observing the behaviors can afford [84]. However, responses were kept anonymous in the hopes to remove social desirability bias and any perceptions of being judged. The study focused only on municipal ran somware attacks and did not account for attacks on public sector firms located in a particular area. As discussed earlier, municipal systems can be viewed as more suitable targets due to underfunding and under staffing information security efforts [5]. Also, attacks on businesses and nongovernmental organizations may not always be publicized in the way that those in this study are, most likely because of the negative public relations consequences and the determination of fault that could result [85,86]. However, news about attacks on private organizations does leak on occasion, and it would be remiss to believe that the publicity involved will have absolutely no impact on local citizens.

## 5.3. Conclusion

When larger cities like Atlanta and Baltimore suffer an attack, the subsequent interest in ransomware is probably heightened to a wider degree that attacks on smaller communities like Borger, TX and Thompson Falls, MT, could not reach. However, the results of this study indicate that proximity to the exploit can, at least, encourage local residents to take precautionary actions to reduce the likelihood that they will be victimized by ransomware attacks.

NOTE: This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## CRediT authorship contribution statement

Kent Marett: Conceptualization, Methodology, Software, Writing - original draft, Writing - review & editing, Validation, Supervision. Misty Nabors: Writing - original draft, Validation, Writing - review & editing.

## Appendix A

Figs. A1 and A2

![](/api/attachments/A5VQN9VW/fulltext/images/dbeac2099ccc869dbcbb3dd9de0478816476323b6bb3a9c0d01768b48a95176b.jpg)  
Fig. A1. News report on ransomware prevention by WDSU (archived on You Tube) following December 2019 Attack on New Orleans, LA City Government, posted January 28, 2020.

![](/api/attachments/A5VQN9VW/fulltext/images/85aac05482e49c6bba7b3d19919b6dd306ccaadfeacffd66a0b4e688dba5fb26.jpg)  
Fig. A2. News report on ransomware attack and security recommendation by WMAZ-TV (archived on YouTube) following September 2019 Attack on Perry, GA Municipal School District, posted September 24, 2019.

![](/api/attachments/A5VQN9VW/fulltext/images/a5d07437de5a08f8c0734171f37b80e53ddd264a0ec52175e8d21bcd66cf0eb5.jpg)

(3a) Significant clusters for experience.  
![](/api/attachments/A5VQN9VW/fulltext/images/dd74f61ff5f4126029a409ac22593c8a1d805aeae9ad83339ef4cd97fd975f9f.jpg)

(3b) Significant clusters for personal learning,  
![](/api/attachments/A5VQN9VW/fulltext/images/e40b5af413afe56da91058b04784c36d076b4d3fd4838f1ae3a3a1cdefdb21a6.jpg)  
(3c) Significant clusters for distance  
Fig. A3. a-c. Visual results of the Post Hoc outlier analysis.

## Appendix B

To check for possible outliers and clustering among the data, we analyzed the three independent variables using Anselin’s Local In dicators of Spatial Autocorrelation, particularly with the Local Moran’s I index of data homogeneity. The purpose of this post hoc assessment is to ensure that the results found in the GWR were not unduly biased by outliers of a number sufficient to exhibit significant spatial autocorre lation when it should not exist.

When placed on a scatterplot mapping the value of the independent variable with the local mean for the variable, each data point tends to fall in one of four quadrants that correspond to its Moran’s I value for a variable in relation to its nearest neighbors. Cases that contribute to positive autocorrelation are those that fall in the “low-low” and “highhigh" quadrants, while other cases that contribute to negative autocorrelation are found in the “high-low” and “low-high” quadrants. Fig. A3ac below show the clustering of each independent variable, with most of the observations exhibiting no significant difference from their local mean values.

While some degree of clustering is expected to always occur, cases with extreme values would be of concern. Upon examining the stan dardized z-scores for each observation, we found the following extreme values for the three independent variables. Personal experience ranged from − 1.24 to 2.80, personal efforts to learn ranged from − 2.23 to 2.11, and distance ranged from − 2.66 to 2.15. The vast majority of z-scores were found between +/- 1.96.

## References

[1] N. Chokshi, Hackers Are Holding Baltimore hostage: How they Struck and What’s Next, the New York Times, 2019. Published May 22available at https://nyti.ms/ 2VEPfUJ.

[2] T. Richman, After Crippling Ransomware Attack, Baltimore Council Members Look For Answers, the Baltimore Sun, 2019. Published Nov 6.

[3] M. Fernandez, D. Sanger, M.T. Martinez, Ransomware Attacks Are Testing Resolve of Cities across America, the New York Times, 2019. Published August 22available at, https://www.nytimes.com/2019/08/22/us/ransomware-attacks-hacking.html.

[4] C. Demrovsky, Why Ransomware Attacks On Local Government Matter, Forbes, 2019. Published August 2Zavailable at. https://www.forbes.com/sites/chloede mrovsky/2019/08/27/why-ransomware-attacks-on-local-government-matter/.

[5] X.R. Luo, H. Li, Q. Hu, H. Xu, Why Individual Employees Commit Malicious Computer Abuse: a Routine Activity Theory Perspective, J. Assoc. Inf. Syst. 21 (6) (2020) 1552–1593, 2020.

[6] M. Dodge, R Kitchin, The challenges of cybersecurity for smart cities, C. Coletta, L. Evans, L. Heaphy and R. Kitchin (eds.. Creating smart cities, Routledge, New York, NY, 2019.

[7] M. Jensen, M. Dinger, R. Wright, J. Thatcher, Training to mitigate phishing attacks using mindfulness techniques, J. Manag. Inf. Syst. 34 (2) (2017) 597–626.

[8] C. Posey, T.L. Roberts, P.B. Lowry, R.J. Bennett, J.F. Courtney, Insiders’ protection of organizational information assets: development of a systematics-based taxonomy and theory of diversity for protection-motivated behaviors, MIS Q. 37 (4) (2013) 1189–1210.

[9] C. Anderson, R. Agarwal, Practicing safe computing: a multimedia empirica examination of home computer user security behavioral intentions, MIS Q. 34 (3) (2010) 613–643.

[10] P. Menard, G. Bott, R. Crossler, User motivations in protecting information security: protection motivation theory versus self-determination theory, J. Manag. Inf, Syst, 34 (4) (2017) 1203–1230.

[11] K. Aytes, T. Connolly, Computer security and risky computing practices: a rational choice perspective, J. Org. End User Comput. 16 (3) (2004) 22–40.

[12] R. Mersey, Sense of community differs for print, online readers, Newsp. Res. J. 30 (3) (2009) 105–119.

[13] A.H. Tanner, D.B. Friedman, Y. Zheng, Influences on the construction of health news: the reporting practices of local television news health journalists, J. Broadcast. Electron. Media 59 (2) (2015) 359–376.

[14] N. Usher, Putting “place” in the center of journalism research: a way forward to understand challenges to trust and knowledge in news, J. Commun. Monogr. 21 (2 (2019) 84–146.

[15] K. Miller, M. Zhao, R Calantone, Adding interpersonal learning and tacit knowledge to March’s exploration-exploitation model, Acad. Manag. J. 49 (4) (2006) 709–722.

[16] R. Cyert, J. March, A Behavioral Theory of the Firm, Prentice-Hall, Englewood Cliffs, NJ USA, 1963.

[17] A. Jaffe, M. Trajtenberg, R. Henderson, Geographic localization of knowledge spillovers as evidenced by patent citations, Q. J. Econ. 108 (3) (1993) 577–598.

[18] D. Gallaud, A Torre, Geographical proximity and the diffusion of knowledge, in: G. Fuchs, P. Shapira (Eds.), Rethinking Regional Innovation and Change, Springer, New York, NY. 2005.

[19] A. Bandura, Social Learning Theory, Prentice-Hall, Englewood Cliffs, NJ, 1977.

[20] A. Bandura, Model of Causality in Social Learning Theory in Cognition and Psychotherapy, M. Mahoney and A. Freeman (eds.), Springer, Boston MA USA, 1985.

[21] J. Baum, S.X. Li, J. Usher, Making the next move: how experiential and vicarious 766-801.

[22] C. Avgerou, Contextual explanation: alternative approaches and persistent challenges, MIS Q. 43 (3) (2019) 977–1006.

[23] K. Lyytinen, D Robey, Learning failure in information systems development, Inf.

[24] P.M. Madsen, V. Desai, No firm is an island: the role of population-level actors in organizational learning from failure, Org. Sci. 29 (4) (2018) 739–753.

[25] T.O. Salge, R. Kohli, M. Barrett, Investing in information systems: on the behavioral and institutional search mechanisms underpinning hospitals’ IS investment decisions, MIS O. 39 (1) (2015) 61–89.

[26] H.-.S. Rhee, C. Kim, Y. Rvu, Self-efficacy in information security: its influence on end users' information security practice behavior, Comput. Sec. 28 (8) (2009) 816-826.

[27] M. Warkentin, A. Johnston, J. Shropshire. The influence of the informal social learning environment on information privacy policy compliance efficacy and intention, Eur. J. Inf. Syst. 20 (3) (2011) 267–284.

[28] W. Hong, F.K.Y. Chan, J.Y.L. Thong, L. Chasalow, G Dhillon, A framework and guidelines for context-specific theorizing in information systems research. Inf. Syst.

[29] A. Johnson, P. Di Gangi, J. Howard, J. Worrell, It takes a village: understanding the collective security efficacy of employee groups, J. Assoc. Inf. Syst. 20 (3) (2019) 186–212.

[30] R. Bennett, W. Bratton, P. Robson, Business advice: the influence of distance, Reg.

[31] M. Porter. Location, competition, and economic development: local clusters in a

[32] K. Marett. T. Barnett. Information security practices in small-to-medium sized businesses: a hotspot analysis, Inf Resour, Manag, J. 32 (2) (2019) 76–93.

[33] J. Hua, Y. Chen, X.R. Luo, Are we ready for cyberterrorist attacks? Examining the role of individual resilience, Inf. Manag. 55 (7) (2018) 928–938.

[34] L. Donnelly, Proximity, not story format, improves news awareness among readers, Newsp. Res. J. 26 (1) (2005) 59–65.

[35] Y. Trope, N. Liberman, Construal-level theory of psychological distance, Psychol. Rev. 117 (2) (2010) 440–463.

[36] J. Cheng, L. Bertolini, Measuring urban job accessibility with distance decay, competition, and diversity. J. Transp. Geogr. 30 (2013) 100–109.

[37] N. Soares, J. Dewalle, B. Marsh, Utilizing patient geographic information system data to plan telemedicine service locations, J. Am. Med. Inform. Assoc. 24 (5) (2017) 891–896.

[38] I. Bateman, B. Day, S. Georgiou, I. Lake, The aggregation of environmental benefit values: welfare measures, distance decay, and total WTP, Ecol. Econ. 60 (2) (2006) 450–460.

[39] E. Karahanna, A. Chen, Q. Liu, C. Serrano, Capitalizing on health information technology to enable digital advantage in U.S. hospitals, MIS Q. 43 (1) (2019) 113-140.

[40] L. Anselin, Local indicators of spatial association—LISA, Geogr. Anal. 27 (2) (1995) 93–115.

[41] X. Qian, S.V. Ukkusuri, Spatial variation of the urban taxi ridership using GPS data, Appl. Geogr, 59 (2015) 31–42.

[42] Y. Huang, Y. Leung, Analysing regional industrialisation in Jiangsu province using geographically weighted regression, J. Geogr. Syst. 4 (2) (2002) 233–249.

[43] D. Farkas, B. Hilton, J. Pick, H. Ramakrishna, A. Sarkar, N. Shin, A tutorial on geographic information systems: a ten-year update, Commun. Assoc. Inf. Syst. 38 (1) (2016) 190–234.

[44] S. Kisilevich, D. Keim, L. Rokach, A GIS-based decision support system for hotel room rate estimation and temporal price prediction: the hotel brokers’ context, Decis. Support Syst. 54 (2) (2013) 1119–1133.

[45] L. Raymond, Organizational characteristics and MIS success in the context of small business, MIS Q. 9 (1) (1985) 37–52.

[46] Y. Xue. D Brown. Spatial analysis with preference specification of latent decision makers for criminal event prediction, Decis. Support Syst. 41 (3) (2006) 560–573.

[47] A.S. Fotheringham, C. Brunsdon, M. Charlton, Geographically Weighted Regression: the Analysis of Spatially Varying Relationships, John Wiley & Sons, Chichester, West Sussex. UK. 2003

[48] C. Brunsdon, A. Fotheringham, M Charlton, Some notes on parametric significance tests for geographically weighted regression, J. Reg. Sci. 39 (3) (1999) 497–524.

[49] J. Gao, S. Li, Detecting spatially non-stationary and scale-dependent relationships between urban landscape fragmentation and related factors using Geographicall Weighted Regression, Appl. Geogr. 31 (1) (2011) 292–302.

[50] Y. Mou, Q. He, B. Zhou, Detecting the spatially non-stationary relationships between housing price and its determinants in China: guide for housing market sustainability. Sustainability 9 (10) (2017) 1826–1843.

[51] V.A. Sottini. E. Barbierato. I. Bernetti. I. Capecchi, S. Fabbrizzi. S. Menghini. Rural environment and landscape quality: an evaluation model integrating social media analysis and geostatistics techniques, Aestimum 74 (2019) 43–62.

[52] Y. Levy, T. Ellis, A guide for novice researchers on experimental and quasiexperimental studies in information systems research, Interdiscip. J. Inf., Knowl., Manage. 6 (1) (2011) 151–161.

[53] D. Chambliss, R. Schutt, Making Sense of the Social World: Methods of Investigation, 6th edition, Sage Publications, Thousand Oaks, CA USA, 2018.

[54] M.O. Emerson, K.T. Smilev, Market Cities, People Cities: The Shape of Our Urban Future. NYU Press, New York, NY USA. 2018.

[55] X. Luo, O. Liao, Awareness education as the key to ransomware prevention, Inf Syst. Secur. 16 (4) (2007) 195–202.

[56] R. Richardson, M. North. Ransomware: evolution, mitigation and prevention, Int

[57] V. Flack, P. Chang, Frequency of selecting noise variables in subset regression analysis: a simulation study. Am, Stat. 41 (1) (1987) 84–86.

[58] R. Wright, K. Marett, The influence of experiential and dispositional factors in phishing: an empirical examination of the deceived, J. Manage. Inf. Syst. 27 (1) (2010) 273–303.

[59] A. Edmonds, T. Kennedy, An Applied Guide to Research Design: Quantitative, Qualitative, and Mixed Methods, 2nd edition, Sage Publications, Thousands Oaks, CA USA, 2017.

[60] L. Scott, M. Janikas, Spatial statistics in ArcGIS, in: M.M. Fischer, A. Getis (Eds.), Handbook of Applied Spatial Analysis: Software Tools, Methods, and Applications Springer-Verlag, Berlin Heidelberg, 2010.

[61] T. Nishida, J. Pick, A. Sarkar, Japan’s prefectural digital divide: a multivariate and

[62] A. Diamantopoulos, J.A. Siguaw, Formative versus reflective indicators in organizational measure development: a comparison and empirical illustration. Br J. Manag. 17 (4) (2006) 263–282.

[63] D. Breuker, M. Matzner, P. Delfmann, J. Becker, Comprehensible predictive models

[64] D. O’Sullivan, D. Unwin, Geographic Information Analysis, John Wiley & Sons, Hoboken NJ USA, 2010.

[65] R. Koenker, A note on studentizing a test for heteroscedasticity, J. Econom, 17 (1) (1981) 107-112.

[66] T. Nakava, M. Charlton, P. Lewis, C. Brunsdon, J. Yao, S. Fotheringham, GWR4 user manual Windows Appl Geogr Weight Regres Model (2014)

[67] W. Wang, D. Li, Structure identification and variable selection in geographically weighted regression models, J. Stat. Comput. Simul. 87 (10) (2017) 2050–2068.

[68] A.S. Fotheringham, T. Oshan, Geographically weighted regression and multicollinearity: dispelling the myth, J. Geogr. Syst. 18 (4) (2016) 303–329.

[69] A. Dennis, J. Valacich, Conducting experimental research in information systems, Commun. Assoc. Inf. Syst. 7 (1) (2001).

[70] J. Wang, Y. Li, H.R. Rao, Overconfidence in phishing email detection, J. Assoc. Inf. Syst. 17 (11) (2016) 759–783.

[71] S. Chatterjee, S. Sarker, J. Valacich, The behavioral roots of information systems security: exploring key factors related to unethical IT use, J. Manag. Inf. Syst. 31 (4) (2015) 49–87.

[72] T. Herath, H.R. Rao, Encouraging information security behaviors in organizations: role of penalties, pressures and perceived effectiveness, Decis. Support Syst. 47 (2) (2009) 154–165.

[73] S. Wagner, K. Hoisl, G. Thoma, Overcoming localization of knowledge—The role of professional service firms, Strateg. Manag. J. 35 (11) (2014) 1671–1688.

[74] A. Torre, On the role played by temporary geographical proximity in knowledge transmission, Reg. Stud. 42 (6) (2008) 869–889.

[75] K.E. Matsa, E. Shearer, News use across social media platforms 2018, Pew Res. Center (2018). Available at: http://www.journalism.org/2018/09/10/news-us e-across-social-mediaplatforms-2018/.

[76] A. Kim, A Dennis, Says who? The effects of presentation format and source rating on fake news in social media, MIS Q. 43 (3) (2019) 1025–1039.

[77] A. Akande, P. Cabral, S. Casteleyn, Assessing the gap between technology and the environmental sustainability of European cities, Inf. Syst. Front. 21 (3) (2019) 581–604.

[78] X. Chen, D. Wu, L. Chen, J. Teng, Sanction severity and employees’ information security policy compliance: investigating mediating, moderating, and control variables, Inf. Manag. 55 (8) (2018) 1049–1060.

[79] I. Png, C.-.Y. Wang, Q.-.H. Wang, The Deterrent and Displacement Effects of Information Security Enforcement: international Evidence, J. Manag. Inf. Syst. 25 (2) (2008) 125–144.

[80] Y. Sawaya, M. Sharif, N. Christin, A. Kubota, A. Nakarai, A. Yamada, Self confidence trumps knowledge: a cross-cultural study of security behavior, in: the Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems, Denver CO USA, 2017, pp. 2202–2214.

[81] L. Connolly, M. Lang, D. Wall, Information security behavior: a cross-cultura comparison of Irish and US employees, Inf. Syst. Manag. 36 (4) (2019) 306–322.

[82] P. Menard, M. Warkentin, P.B. Lowry, The impact of collectivism and psychological ownership on protection motivation: a cross-cultural examination, Comput. Secur. 75 (2018) 147–166.

[83] W.A. Van der Stede, A manipulationist view of causality in cross-sectional survey research, Acc., Org. Soc. 39 (7) (2014) 567–574.

[84] Z. Tu, O. Turel, Y. Yuan, N. Archer, Learning to cope with information security risks regarding mobile device loss or theft: an empirical examination, Inf. Manag. 52 (4) (2015) 506–517.

[85] K. Renaud, S. Flowerday, M. Warkentin, P. Cockshott, C. Orgeron, Is the responsibilization of the cyber security risk reasonable and judicious? Comput. Secur, 78 (2018) 198–211

[86] T. Wang, K. Kannan, J. Ulmer, The association between the disclosure and the realization of information security risk factors, Inf. Syst. Res. 24 (2) (2013) 201–218.

Kent Marett is an Associate Professor of Business Information Systems and Robert Keil Fellow at Mississippi State University. He received his PhD in Management Information Systems from Florida State University. His research interests involve information security, deceptive communication, and business computing in geographically rural regions. His work has been published in the Journal of Management Information Systems, MIS Quarterly, the Journal of the AIS, and Information Systems Research, among other top journals.

Misty Nabors is a doctoral candidate in the Department of Management & Information Systems at Mississippi State University. She currently serves as the assistant director of the Office of Institutional Research & Effectiveness at MSU. Her research has been presented at several conferences in both the field of information systems and the field of secondary education.
