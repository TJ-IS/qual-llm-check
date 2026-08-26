---
otero_id: 9258
otero_key: "FYFQQP4V"
title: "Research Note—An Exploration of Risk Characteristics of Information Security Threats and Related Public Information Search Behavior"
authors: "Jingguo Wang; Nan Xiao; H. Raghav Rao"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0581"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/FYFQQP4V/fulltext/images/a4593b222c00ec337f50289002ce51a8ef15cd41acf4127b3ae72f559de9ea67.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—An Exploration of Risk Characteristics of Information Security Threats and Related Public Information Search Behavior

Jingguo Wang, Nan Xiao, H. Raghav Rao

To cite this article:

Jingguo Wang, Nan Xiao, H. Raghav Rao (2015) Research Note—An Exploration of Risk Characteristics of Information Security Threats and Related Public Information Search Behavior. Information Systems Research

Published online in Articles in Advance 22 Jul 2015

http://dx.doi.org/10.1287/isre.2015.0581

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/FYFQQP4V/fulltext/images/c34f11714d698553a2d05e6d0fa520bb016ed4f90c024079a528d5ae4390a513.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# An Exploration of Risk Characteristics of Information Security Threats and Related Public Information Search Behavior

Jingguo Wang

Information Systems and Operations Management, College of Business, University of Texas at Arlington, Arlington, Texas 76019, jwang@uta.edu

Nan Xiao

Department of Information Systems, University of Texas Rio Grande Valley, Edinburg, Texas 78539, nan.xiao@utrgv.edu

H. Raghav Rao

Management Science and Systems, School of Management, State University of New York at Buffalo, Buffalo, New York 14260, mgmtrao@buffalo.edu

nformation security (IS) threats are increasingly pervasive, and search engines are being used by the public as Ithe primary tool for searching for relevant information. This research investigates the following two questions: (1) How can different IS threats be characterized and distinguished in terms of their risk characteristics? and (2) how are risk characteristics related to public searches for information on IS threats? Applying psychometric analysis, our analyses of survey data first show that unknown risk and dread risk are two underlying dimensions that can characterize different IS threats. Drawing broadly on the literature of information foraging theory, we examine the influence of risk characteristics on public searches for information on these threats. We utilize a search engine log to extract searches related to IS threats. We develop and estimate a system of equations with correlated individual-specific error terms using the Markov Chain Monte Carlo method. We find that the two risk characteristics exert differential impacts on information search behavior (including types of information sought, number of pages viewed, and length of query). The implications for IS research and practice are discussed.

Keywords: information-seeking behavior; information security threats; risk characteristics; psychometric analysis; Markov Chain Monte Carlo

History: Vijay Mookerjee, Senior Editor; Sabyasachi Mitra, Associate Editor. This paper was received July 23, 2013, and was with the authors 10 months for 4 revisions. Published online in Articles in Advance.

## 1. Introduction

Information security (IS) is a function of technology, policy, process, and users, among which users are often considered to be the weakest link (Spears and Barki 2010, Warkentin and Willison 2009). In response to increasingly pervasive IS threats, a growing body of literature has investigated end users’ IS behaviors, including protecting individual information assets at home and complying with IS policy in an organization (Anderson and Agarwal 2010, Herath and Rao 2009, Johnston and Warkentin 2010). However, research investigating how users proactively seek relevant threat information and what factors drive their searches remains sparse. An understanding of how users seek information on IS threats may help us find better ways to educate users to safeguard themselves from such threats.

This research intends to address two gaps in the literature. First, a variety of IS threats exist, and they differ in a number of risk attributes such as prevalence, impact, manifestation, novelty, and controllability. Prior studies, however, either focused on only one type of IS threat or treated IS threats in a generic manner, primarily investigating how users’ perceptions of magnitude and probability of the risk affect their reactions (Herath and Rao 2009, Johnston and Warkentin 2010). By contrast, research by cognitive psychologists has shown that laypersons’ estimation of risks is influenced by a number of other risk attributes besides consequence and probability (Boholm 1998). Characterizing IS threats with more risk attributes enables us to capture their differences and understand their nature (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987). It can further help us develop effective mitigation programs tailored to those threats. Therefore, the first research question is, How can different IS threats be characterized and distinguished in terms of their risk characteristics?

Second, prior studies have mainly sought to elucidate individuals’ intention to take protective/preventive actions against threats (D’Arcy et al. 2009, Herath and Rao 2009, Puhakainen and Siponen 2010, Straub and Welke 1998). However, IS threats grow increasingly complicated, and users may have to overcome barriers of knowledge deficiency as the first step toward improving IS security. Search engines are being used as an effective channel to acquire threat information (Wang et al. 2010, 2012). Searches for information on threats improve users’ knowledge and help regulate their negative emotions, such as fear, associated with the threats (Griffin et al. 1999, Kahlor 2007, ter Huurne et al. 2009). An investigation of the drivers of such searches will advance our understanding of users’ information needs, which will in turn facilitate the design of effective tools and programs to disseminate threat knowledge. Therefore, the second research question of the note is, How are risk characteristics related to public searches for information on IS threats?

This research makes two contributions. First, it introduces psychometric analysis (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987) as a means to characterize IS threats with a number of risk attributes and shows how 20 common IS threats differ from one another. Psychometric analysis has been widely used to understand public perception (i.e., perception shared among individuals) of hazards in many domains (Boholm 1998, Duff 2014, Ngo et al. 2013, Slovic 2000). This study extends the analysis to the field of IS and demonstrates that IS threats, following similar patterns observed in other types of hazards, can be characterized by two underlying dimensions, unknown risk and dread risk, which reflect the degree to which a risk is understood and the degree to which a risk evokes a feeling of anxiety and fear, respectively.

Second, this research is among the first (to our knowledge) to illustrate distinct users’ reactions to different threats, particularly their information seeking about IS threats. We draw broadly on information foraging theory (Pirolli 2007, Pirolli and Card 1999) to link risk characteristics of IS threats to public searches for related information via a search engine. Three aspects of search behavior we investigate include the number of terms in a query, the types of information sought 4i.e., protective information versus nonprotective information5, and the number of search results pages browsed. These three aspects of search behavior, which delineate search strategies that users adopt to meet their information needs, are captured by a search log from a large search engine. We show that the risk characteristics of threats drive users’ search behavior. Our study is also a response to a recent call for the utilization of new data sources, including search engine logs, in IS research (Mahmood et al. 2010).

## 2. Theoretical Background and Hypotheses

2.1. Psychometric Analysis on Risk Characteristics Psychometric analysis has been widely used as a basis to study risk communication and understand public reactions to various hazards (Sandman 1993). It encompasses a theoretical framework suggesting that individuals’ risk perception in regard to hazards is influenced by a wide array of risk characteristics (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987). Psychometric analysis identifies two underlying factors of risk characteristics—unknown risk and dread risk—that are shared among individuals and affect their risk perception (Marris et al. 1997). Unknown risk is broadly defined in terms of hazards that are deemed to be unobservable, unknown, and new. Dread risk is broadly defined in terms of hazards that are perceived to result in a lack of control, dread, catastrophic potential, and fatal consequences (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987). Psychometric analysis has been employed to identify the underlying factors of risk characteristics for natural, human-made, and technology-related hazards (such as nuclear power, smoking, and swimming) and to understand how these factors influence public reaction to hazards. It has become one of the most influential models in the field of risk analysis.

The research applies psychometric analysis (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987) to the domain of IS for two reasons. First, in contrast to traditional IS literature, which focuses primarily on the probability of occurrence and the magnitude of consequence of a threat (Herath and Rao 2009, Johnston and Warkentin 2010, Liang and Xue 2009), psychometric analysis considers a risk to be multidimensional, possessing characteristics other than its occurrence probability and severity, which allows for a richer description of IS threats. Second, prior studies have mainly focused on users’ perception of one type of IS threat or of IS threats in a generic manner (Herath and Rao 2009, Johnston and Warkentin 2010). Psychometric analysis enables us to compare the risk characteristics across a variety of IS threats based on the views shared among individuals. Such an analysis provides a foundation to subsequently use risk characteristics to explain distinct search behavior related to different threats.

## 2.2. Seeking Threat Information

To investigate the relationship between risk characteristics and users’ information search behavior, we broadly draw on information foraging theory, which provides a framework to understand the strategies that people adopt for information seeking and gathering (Pirolli 2007, Pirolli and Card 1999). Borrowing from the literature on biology and ecology, information foraging theory uses the analogy of animals’ hunting for food to study how people search for information online. It proposes that an understanding of users’ online search behavior includes both a rational analysis of search goals and an analysis of information seekers’ perception of the information environment (Pirolli 2007, Pirolli and Card 1999). Information foraging theory suggests that information seekers tend to optimize their search utilities by maximizing the expected value of knowledge gained and minimizing the expected cost of interaction with search engines. The subsequent gains are measured by the improvement of knowledge (i.e., the achievement of search goals), and the costs usually include information access, recognition, and handling costs. In addition, analogous to animals’ searches for food, during which they are watchful of the surrounding environment to avoid their predators, information foraging theory implies that uncertainty could force information seekers to modify their search strategies.

Following the guideline established by information foraging theory, we analyze users’ search for threat information from both a cost–benefit perspective and a risk coping and appraisal perspective. Individuals adopt optimal strategies by comparing the expected value of the information resource to the expected cost of accessing and extracting relevant information. We consider domain knowledge (or the level of knowledge on the topic being searched) to be one of the major factors influencing users’ ability to formulate proper search strategies (Holscher and Strube 2000, Kelly and Cool 2002), as well as their assessment of search costs and information values (Brucks 1985, Lion et al. 2002, Punj and Staelin 1983, Schmidt and Sprang 1996). Furthermore, searching for threat information can be considered part of a coping strategy that seeks to develop appraisal and protection mechanisms to reduce uncertainty and control negative psychological states associated with risks (Ybarra and Sumanb 2006). Therefore, individuals’ affective and emotional states (e.g., a feeling of dread) can determine both the information to which they choose to expose themselves (Zillmann and Bryant 1985) and the extent to which they conduct the search (Griffin et al. 1999, Hovick et al. 2011, Kahlor 2007, Kuttschreuter 2006, ter Huurne et al. 2009).

## 2.3. Hypothesis Development

We consider a typical information search via a search engine to proceed as follows. Having questions in mind, a user attempts to locate relevant online information via a search engine by submitting a query. The query reflects the user’s search needs and may be considered to be raised by the user with the intention of inducing a response from the search engine. Following a submitted query, search engines return a chunk of URL links and their brief descriptions, with the most relevant ones appearing at the top of the list. These results are presented to the users in organized pages. Users browse the results pages to look for needed information (Leroy et al. 2007, Pass et al. 2006).

Manipulating query length 4i.e., the number of terms5 allows users to feed more or less information to the search engine and, therefore, may result in differently oriented results generated by information retrieval algorithms (Baeza-Yates and Ribeiro-Neto 1999, Bailey et al. 2010). Manipulating query terms 4i.e., query content5 allows users to focus on different types of information about an IS threat, including threatappraisal information that presents threat characteristics (e.g., affected platforms, routes of infections, and infection symptoms) and threat-coping information that identifies protective measures against the threat (Neuwirth et al. 2000). Finally, the number of results pages browsed for a query indicates the extent of users’ search for relevant information. These three aspects of search behavior delineate search strategies that users adopt to meet their information needs.

We posit that when searching for an IS threat with high unknown risk, users tend to submit shorter queries (Hypothesis 1) and are more likely to focus on threat-appraisal information (such as threat characteristics) than on threat-coping information (such as protective measures) (Hypothesis 2). Regarding the effect of unknown risk on the number of pages browsed, we suggest two competing hypotheses (Hypotheses 3A and 3B)<sup>1</sup> since both positive and negative relationships have support in the literature. We also propose that when searching for an IS threat with high dread risk, users tend to submit longer queries (Hypothesis 4), are more likely to search for threat-coping information (Hypothesis 5), and browse more results pages (Hypothesis 6). Figure 1 depicts our research model and proposed hypotheses.

2.3.1. Unknown Risk and Search. We expect that when searching for a threat with high unknown risk, users are likely to submit queries with fewer terms due to a lack of the domain knowledge necessary for generating longer queries. Given a threat that has high unknown risk, users may possess less factual knowledge about the threat (or a lower domain knowledge level), which consequently constrains their ability to formulate search queries. Prior studies have suggested that users formulate their queries based on experiences, knowledge, and familiarity with the topic (Holscher and Strube 2000, Kelly and Cool 2002). The patterns of terms used in queries change over time as users’ domain knowledge changes (Wildmuth 2004). When users’ domain knowledge increases, their vocabulary representing the topic grows larger (Vakkari et al. 2003), and subsequently they employ more terms in queries (Zhang et al. 2005) and more search expressions (Allen 1991, Heit 1997). Therefore, we propose the following:

Figure 1 Research Hypotheses  
![](/api/attachments/FYFQQP4V/fulltext/images/1d68bdea30ecc04f683e6658b02a95c7f0e84c655523aee10d6fa603a4c1ec11.jpg)  
Individual search habit: A user's average number of queries per session; the number of days in which the user entered at least one query during the observation period; the average number of pages viewed per query; the average query length Contextual factors: A user's prior clicks on related topics; network attacks; search on weekday

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> Unknown risk is negatively related to the number of terms in search queries.

We expect that when searching for a threat with high unknown risk, users are more likely to search for threat-appraisal information (such as threat characteristics) than for threat-coping information (such as information on protective measures). When searching for threat information, users need information to build their confidence and, more importantly, to improve their competency to evaluate and comprehend advanced information (Brucks 1985, Lion et al. 2002). Compared with threat-appraisal information, threat-coping information is more advanced and complex in the sense that it requires more knowledge for comprehension and utilization. Consequently, for threats with high unknown risk, constrained by their domain knowledge level, users may have to limit their search to threat characteristics such as information on whether a particular security threat would affect their operating system and/or the consequences and symptoms of infection. Therefore, we propose the following:

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> Search for information regarding threats with high unknown risk is less likely to focus on threat-coping information than on threat-appraisal information.

We propose two competing hypotheses (H3A and H3B) regarding the effect of unknown risk on the number of results pages browsed. On one hand, we expect that when searching for information on an IS threat with high unknown risk, users are likely to browse fewer results pages. A lack of knowledge on the threat makes it difficult for users to come up with high-quality queries to reflect their search intention (Holscher and Strube 2000). Their constrained ability to formulate quality queries and the likelihood of making errors could lead to a higher search cost, as the results returned by the search engine may be less satisfactory or useful (Kulviwat et al. 2004). Furthermore, a lack of knowledge on a topic requires additional efforts to assess the relevance of search results and comprehend the information (Pirolli and Card 1995), which could pose significant cognitive challenges to information seeking. Such a high search cost may discourage users from continuing a search (Pirolli and Card 1995). Therefore, we propose the following:

<sup>Hypothesis</sup> <sup>3A</sup> <sup>(H3A).</sup> Unknown risk is negatively associated with the number of results pages browsed.

On the other hand, for a threat with low unknown risk, users may have less need to carry out an extensive search. The benefit of examining an additional

URL diminishes rapidly if users can make a decision using information about a threat already known to them (or stored in their memory by engaging in recall; Punj and Staelin 1983, Schmidt and Sprang 1996). In other words, if internally retrievable information regarding a threat is available for users in decision making, the information obtained via external search may degenerate rapidly, and the motivation for continuing to examine the results pages may diminish quickly. Consequently, fewer pages will be browsed. By contrast, when searching for a threat with high unknown risk, users may have a larger knowledge gap to fill using external sources and, therefore, may view more results pages. Therefore, we propose the following:

<sup>Hypothesis</sup> <sup>3B</sup> <sup>(H3B).</sup> Unknown risk is positively associated with the number of results pages browsed.

2.3.2. Dread Risk and Search. We expect that when searching for an IS threat with high dread risk, users tend to submit queries with more terms (or queries with high specificity). Individuals’ affective and emotional states (e.g., a feeling of dread) are determinants of the information to which they choose to expose themselves (Zillmann and Bryant 1985). A longer query could help retrieve more narrowly oriented information on a threat and help alleviate fear related to that threat. For an IS threat with high dread risk, users may desire information that directly addresses their specific information needs and controls fear, rather than a holistic view that may contain information provoking their fear of the threat (Jonas et al. 2006). This motivation could lead them to formulate longer queries when searching for a threat with high dread risk. Therefore, we propose the following:

<sup>Hypothesis</sup> <sup>4</sup> <sup>(H4).</sup> Dread risk is positively related to the number of terms in search queries.

We expect that when searching for an IS threat with high dread risk, users are more likely to search for threat-coping information than for threat-appraisal information. The fear associated with dread risk can lead users to seek and assess possible coping strategies to deal with the threat, to gain the feeling of control, and to avoid potential grave negative consequences (Neuwirth et al. 2000). When searching for a threat with high dread risk, users may be more eager to figure out how they can actively protect their systems rather than merely know what the threat is. Knowledge of threat-coping strategies helps users improve their response efficacy and self-efficacy, which in turn enables them to take effective coping actions against the threat. In the domain of health care, it has been shown that threat-coping information can reduce users’ anxiety, increase feelings of self-efficacy, improve the effectiveness of protection (Ybarra and

Sumanb 2006), and trigger exercise of self-care (Chou and Wister 2005). Therefore, we propose the following:

<sup>Hypothesis</sup> <sup>5</sup> <sup>(H5).</sup> Search for information on threats with high dread risk is more likely to focus on threat-coping information than on threat-appraisal information.

We expect that when searching for an IS threat with high dread risk, users are likely to view more results pages. The health information search literature as well as other literature (e.g., global warming) indicates that negative emotions such as fear of a threat increase users’ perceived information insufficiency about the threat, thereby motivating users to seek more extensive information (Griffin et al. 1999, Hovick et al. 2011, Kahlor 2007, Kuttschreuter 2006, ter Huurne et al. 2009). Neuwirth et al. (2000) found that fear of an environmental threat is positively associated with the effort to search for related information. Therefore, we propose the following:

<sup>Hypothesis</sup> <sup>6</sup> <sup>(H6).</sup> Dread risk is positively related to the number of results pages browsed.

2.3.3. Control Variables. As shown in Figure 1, we included a number of covariates to account for users’ search habits, learning effects, and other contextual factors that might have confounding impacts on information search behavior. First, we included (1) the user’s average number of queries per session, a variable that reflects users’ tendency of using multiple queries for a task, and (2) the number of days in which the user entered at least one query during the observation period. In addition, we included<sup>2</sup> (3) the average number of pages viewed per query, a variable that captures an individual’s propensity to view additional information when conducting a search, and (4) the average query length, a variable that captures an individual’s preference for search term brevity. Second, users’ knowledge may accumulate as they search on a topic, which could in turn have an impact on subsequent searches. We therefore controlled for this learning effect by including the total number of clicks that occurred in the search for security threats prior to current search. Third, prior studies show that the search occasion and external environment may influence users’ search behavior (Newman and Staelin 1972, Srinivasan 1990). In the context of IS threats, users’ searches may be affected by the threat level over the Internet. We thus included the number of network attacks on the date when the search was performed as a control variable. We derived the measurement of network attack intensity based on DShield data (www.DShield.org; Wang et al. 2010). Fourth, we included whether the search was conducted on a weekday or weekend/holiday as a control variable, because time constraints may vary for these two periods (Baye et al. 2009).

## 3. Data and Analyses

To test our hypotheses, we collected data in two steps: (1) we administered a survey to characterize 20 common IS threats, and (2) we analyzed a search engine log to capture public searches related to these threats. We then developed a system of equations with correlated individual-specific error terms to examine the effects of threat risk characteristics on search behavior and used the Markov Chain Monte Carlo (MCMC) method for estimation.

## 3.1. Risk Characteristics of IS Threats

We identified 20 common IS threats from a variety of sources, including academic papers (Whitman 2003), antivirus vendors’ reports (Turner et al. 2008), and cybercrime analysis reports (Braverman et al. 2006, Richardson 2008). Online Appendix A (available as supplemental material at http://dx.doi.org/ 10.1287/isre.2015.0581) lists the names of 20 common IS threats and their mapped threat categories based on Whitman’s (2003) work. Those threats, across an IS threat spectrum, affect users in different ways and have varied impacts on their systems. Consequently, they serve as good representatives of IS threats.

We carried out a survey to characterize these threats. The survey asked each participant to rate each threat using 10 items (on seven-point rating scales) that were adopted from the work of Fischhoff et al. (1978), Slovic (1987), and Slovic et al. (1980, 1987). These items reflect different risk attributes of the threats. Necessary adaptations were made to fit the items into the context of IS threats. To test the face validity of the survey, we conducted a pilot study among 31 graduate students recruited from a graduate information assurance class. We asked the students to complete the survey and provide us with feedback on the clarity of each item. The instructions and items in the questionnaire were further refined based on this feedback. Online Appendix B presents the final version of the items.

The respondents to our survey were university students. The use of university students as the sample in our study follows the practice in previous literature (Gordon et al. 1986, Jarvenpaa et al. 2004) and was conducted in accordance with the most recent guidelines on using student subjects in IS research (Compeau et al. 2012). The factor space characterized by unknown risk and dread risk has been replicated across different groups (e.g., students, laypersons, and experts) judging large and diverse sets of hazards, and no significant difference has been found among the groups (in terms of the positions of the threats in the twodimensional space) (Boholm 1998; Slovic 1987, 2000; Slovic et al. 1980, 1987). Furthermore, university students were deemed good representative subjects for this study because a great majority of them own computers and are Internet users (Jones 2002), and they are frequently susceptible to different IS threats (Johnston and Warkentin 2010). Therefore, IS and information search via a search engine are relevant topics for them. As a convenient sample to access, university students have been used as research subjects in a number of studies on IS behaviors (Johnston and Warkentin 2010) and risk characterization of different hazards (Boholm 1998).

We distributed the online survey to approximately 400 undergraduate business students at a major university in the northeastern United States.<sup>3</sup> The students received an invitation email including the link to the survey. Extra credit was offered for participation. An alternative opportunity was provided to those students who were not able to participate in the survey but needed the extra credit (as required for survey studies by the institutional review board). We received a total of 281 valid responses. Table 1 presents the demographics of our sample.

## 3.2. Public Information-Seeking Behavior

To capture public information-seeking behavior related to these threats, we utilized a search log from a large search engine. This log spanned three months and contained approximately 20 million records of searches initiated by more than 650,000 users. Each entry in the log included a deidentified user number, a query submitted by the user, the time at which the query was submitted, and the domain portion of the URL if the user clicked on a search result. The presence of a URL in a log entry also indicated whether a query was followed by a click-through. If a user clicked on more than one link in the results list returned from a single query, there would be multiple entries in the log with the same query and the same time stamp, but different domain names for the URLs clicked. If a user requested “next page” of results for a query, there would be a subsequent identical query with the same time stamp and domain name.

To identify the searches for IS threats, we retrieved all queries that contained the names of the 20 IS threats from the search log. A total of 11,708 queries were obtained. In addition, to identify queries related to IS threats, we gathered 200 names of viruses or malware that fell into the categories represented by these 20 IS threats. These 200 viruses or malware were either historically noticeable or prevalent during the period covered by our search engine log. An extensive examination revealed that very few queries contained those names, and it suggested that users rarely used the name of a specific virus or malware as a keyword for a search. Therefore, our final queries included only the general names of the 20 IS threats.

Table 1 Demographics of Our Sample

<table><tr><td>Gender</td><td>Respondents</td></tr><tr><td>Male</td><td>172</td></tr><tr><td>Female</td><td>107</td></tr><tr><td>Missing</td><td>2</td></tr><tr><td colspan="2">Age (years)</td></tr><tr><td>&lt;19</td><td>1</td></tr><tr><td>19–21</td><td>168</td></tr><tr><td>21–23</td><td>79</td></tr><tr><td>23–25</td><td>17</td></tr><tr><td>25–27</td><td>8</td></tr><tr><td>27–30</td><td>5</td></tr><tr><td>&gt;30</td><td>2</td></tr><tr><td>Missing</td><td>1</td></tr><tr><td colspan="2">On average, how much time per week do you spend on computers?</td></tr><tr><td>&lt;5 hours</td><td>9</td></tr><tr><td>6–10 hours</td><td>35</td></tr><tr><td>11–15 hours</td><td>49</td></tr><tr><td>16–20 hours</td><td>58</td></tr><tr><td>21–25 hours</td><td>52</td></tr><tr><td>26–30 hours</td><td>22</td></tr><tr><td>&gt;30 hours</td><td>56</td></tr><tr><td>Missing</td><td>0</td></tr><tr><td colspan="2">How many years ago did you first hear of IS threats?</td></tr><tr><td>&lt;1 year</td><td>1</td></tr><tr><td>1–2 years</td><td>9</td></tr><tr><td>3–4 years</td><td>55</td></tr><tr><td>5–6 years</td><td>88</td></tr><tr><td>7–8 years</td><td>64</td></tr><tr><td>9–10 years</td><td>36</td></tr><tr><td>&gt;10 years</td><td>28</td></tr><tr><td>Missing</td><td>0</td></tr><tr><td>How many years have you been using a computer?</td><td>Years</td></tr><tr><td>Average of using a computer</td><td>10.81</td></tr><tr><td>Standard deviation of using a computer</td><td>3.27</td></tr><tr><td>Missing</td><td>14</td></tr></table>

In addition, because a query that simply contains the names of IS threats may not necessarily be a search for IS, we manually screened all selected queries to determine whether they were truly intended to explicate the IS threats and which type of information users intended to search (threat-appraisal information versus threat-coping information). Two graduate student coders, who had more than two years of work experience in computer information systems, were recruited for coding. The coders were unaware of the research questions, which allowed for blind coding and thus reduced any biases stemming from coders’ knowledge of variables extraneous to the content analysis (Neuendorf 2002). Both coders were instructed to independently examine all queries to identify those related to IS threats. If a query was related to IS threats, they further determined whether the search was explicitly seeking threat-appraisal information (such as threat characteristics, coded as 0) or threat-coping information (such as protective measures, coded as 1). Queries were coded as searches for threat-coping information if they contained a specific countermeasure name (such as Spyware Doctor) or verbs such as protect, defend, mitigate, or remove or related nouns. The two coders were trained until they fully understood the coding protocol. Their final coding results showed that they agreed on the coding of most queries. All discrepancies were reconciled either by reaching a consensus on the coding or by discarding those queries that were ambiguous and whose search intentions could not be definitively determined.

Table 2 Descriptive Statistics of Dependent Variables

<table><tr><td>Variables</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Number of terms (excluding threat names)</td><td>0</td><td>46</td><td>1.46</td><td>1.89</td></tr><tr><td>Threat-coping information</td><td>0</td><td>1</td><td>0.58</td><td>0.49</td></tr><tr><td>Number of pages</td><td>1</td><td>30</td><td>1.19</td><td>0.89</td></tr></table>

A total of 5,570 queries (out of 11,708) related to the 20 IS threats were identified, coded, and used for final data analysis. These queries were submitted by 3,886 distinct users, among whom 332 (8.5%) submitted more than two queries in our log. Online Appendix C shows the search frequency for different IS threats. As one might expect, searches for certain threat keywords were more frequent than others. Our dependent variables were constructed based on these queries. The number of terms in a query was counted after the name of the security threat of interest was removed. If a query only contained the name of the security threat of interest, then the number of terms in the query was zero. The number of results pages browsed for a query was determined by how many pages of results were reviewed by a user. Table 2 presents the descriptive statistics of the dependent variables.

## 3.3. Factor Analysis of Risk Characteristics

Psychometric analysis (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987) was developed to identify perceived risk characteristics of hazards shared among individuals. The analysis has three main steps. First the mean rating of each risk characteristic for each threat is calculated based on survey responses. Then a bivariate correlation analysis among risk characteristics is performed. Finally a factor analysis is carried out to identify the underlying factors explaining the variance of the intercorrelations. This method has been applied in some recent studies to understand a wide range of risks in different domains such as technological hazards, environmental risks, genetically modified organisms, blood transfusions, and investment products (Duff 2014, Kim et al. 2014, Morris 2011, Ngo et al. 2013, Portell et al. 2014, Sachse et al. 2012, Wang et al. 2011).

Following the psychometric analysis procedure (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987), we first calculated the mean rating of each item for each threat. Online Appendix D summarizes the results. Ratings of these items tended to be highly intercorrelated (Online Appendix E), as found in prior studies (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987). The high intercorrelations suggest that these threats share certain basic underlying dimensions of risk characteristics.

To identify such underlying dimensions, we then conducted principal component factor analyses. Two orthogonal factors appeared sufficient to account for the intercorrelations. Table 3 shows the variance explained by the two factors and the rotated factor loadings (which were obtained by the varimax rotation method). The rotated factor loadings indicate the degree to which each item is correlated with each factor. The pattern of loadings indicates that the first factor is highly correlated with knowledge about risk at both personal and professional levels, newness, and observability, whereas the second factor is highly associated with immediacy of effect, dread, and severity of consequences. Personal control over risk, mitigating control over risk, and preventive control are associated with both factors. The communalities, which reflect the extent to which the two factors accounted for each of the ratings, have high values, as shown in Table 3. These results suggest the twofactor solution sufficiently represents the ratings of the 10 items, with Factor 1 representing unknown risk and Factor 2 representing dread risk.

For each threat, we calculated a score on both factors based on the principal component factor analysis.

Table 3 Factor Loadings Across Risk Characteristics

<table><tr><td>Items for risk characteristics</td><td>Factor 1 (unknown risk)</td><td>Factor 2 (dread risk)</td><td>Communality</td></tr><tr><td>Knowledge about risk (personal)</td><td>-0.94</td><td>0.16</td><td>0.90</td></tr><tr><td>Knowledge about risk (professional)</td><td>-0.97</td><td>0.09</td><td>0.95</td></tr><tr><td> $Newness^a$ </td><td>-0.94</td><td>0.13</td><td>0.90</td></tr><tr><td>Observability</td><td>-0.92</td><td>-0.13</td><td>0.87</td></tr><tr><td>Immediacy of  $effect^a$ </td><td>0.40</td><td>-0.87</td><td>0.91</td></tr><tr><td>Dread</td><td>-0.31</td><td>0.93</td><td>0.96</td></tr><tr><td>Severity of consequences</td><td>0.10</td><td>0.98</td><td>0.96</td></tr><tr><td>Personal control</td><td>-0.76</td><td>-0.63</td><td>0.97</td></tr><tr><td>Mitigating control</td><td>-0.61</td><td>-0.78</td><td>0.98</td></tr><tr><td>Preventive control</td><td>-0.64</td><td>-0.69</td><td>0.89</td></tr><tr><td>Variance explained (%)</td><td>52</td><td>41</td><td></td></tr><tr><td>Eigenvalues</td><td>5.46</td><td>3.83</td><td></td></tr></table>

Figure 2(a) plots all factor scores of 20 threats in a two-factor space, whereas Figure 2(b) visualizes the primary risk characteristics associated with the two factors. As one moves from left to right in Figure 2(a), the threats are judged to have higher unknown risk, occurring with less personal and professional knowledge and being newer, less observable, and less controllable. As one goes from the bottom to the top of Figure 2(a), the threats are judged to have higher dread risk, occurring with more immediate, more fearful, more severe, and less controllable consequences.

## 3.4. Data Modeling and Estimation Results

3.4.1. A System of Equations with Correlated Individual-Specific Error Terms. We developed a system of equations with three dependent variables (the number of terms in a query, the type of information sought, and the number of pages browsed). We incorporated a one-way random effects term for each dependent variable, considering unobserved heterogeneity among users in their search behavior (Hsiao 2003). We further introduced correlations among the individual-specific random effects terms.

Given that (a) the “number of terms” in a query and (b) the number of pages browsed are both count data, our analysis used negative binomial regression, a more general model than Poisson regression. We subtracted the number of pages browsed by 1 such that zeros are included for modeling purposes. Let $y _ { t i j }$ denote the two dependent variables, with $j = 1$ representing the number of terms in a query and $j = 2$ representing the number of pages browsed. The term ti indicates user i searched for threat t at some instance. The expected value of $y _ { t i j } ,$ positive and individual specific, is modeled as a function of a set of covariates

$$
E (y _ {t i j}) = e ^ {X _ {t} \beta_ {t j} + X _ {i} \beta_ {i j} + \eta_ {i j}},\tag{1}
$$

where $X _ { t }$ is a set of threat-related variables including $x _ { t 1 } , ~ x _ { t 2 }$ (unknown risk and dread risk, respectively), $X _ { i }$ is a set of individual-related variables, $\beta _ { t j }$ and $\beta _ { i j }$ $( j = 1 , 2 )$ are vectors of coefficients to be estimated, and $\eta _ { i j }$ is the random effects term related to user i.

We used a logistic regression model for (c) the third dependent variable, type of information sought. Let $y _ { t i 3 }$ be a binary variable (with 1 indicating search for threat-coping information and 0 otherwise) when user i searches for threat t at an instance. We consider $y _ { t i 3 }$ to follow a Bernoulli distribution with a success probability of $\pi _ { t i }$ for a search given user i for threat t, and

$$
\log \frac {\pi_ {t i}}{1 - \pi_ {t i}} = X _ {t} \beta_ {t 3} + X _ {i} \beta_ {i 3} + \eta_ {i 3}.\tag{2}
$$

We consider that $\eta _ { i 1 } - \eta _ { i 3 }$ follows a multivariate normal distribution with a mean of zero and a covariance matrix è.

Figure 2 Risk Characteristics of 20 IS Threats in Two-Factor Space  
![](/api/attachments/FYFQQP4V/fulltext/images/53ade706a8b17e1f6cadb7f6e0cf1efe0eba0ae49dcbefa2372bcefb1af08714.jpg)

![](/api/attachments/FYFQQP4V/fulltext/images/136dc3616ea69bde377da3b133f4a327020a73d14af7d2d5c7c4520c9741921a.jpg)

3.4.2. Estimation Method. Given the complexity of the model, the MCMC method was used to estimate the model and obtain posterior distributions of model parameters. The MCMC method is a Bayesian method. By running a carefully constructed Markov chain over a long period of time, it draws samples from the required distribution and then forms sample averages to approximate expectations for a model (Gelman et al. 2003). WinBUGS, a software package for performing Bayesian inference using Gibbs sampling (Spiegelhalter et al. 2003), was used for the estimation.

Gibbs sampling is applicable when the joint distribution is difficult to sample directly (e.g., because of the high number of parameters to be estimated, pronounced skewedness, or multimodal nature; Geman and Geman 1984). Following a “divide-and-conquer” approach, each step of the Gibbs sampling algorithm generates a random value for a parameter to be estimated from a one-dimensional distribution, conditional on the current values of the other parameters. The sampling process is repeated a number of times, starting from an initial state. The sequence of samples constitutes a Markov chain, and the stationary distribution of that Markov chain is the joint distribution of the parameters sought (Gelman et al. 2003).

Table 4 Correlation Coefficients

<table><tr><td></td><td>Query terms</td><td>Coping information</td><td>Results pages browsed</td><td>Unknown risk</td><td>Dread risk</td><td>Average number of queries/session</td><td>LG (active days)</td><td>Network attack intensity</td><td>Prior clicks on security</td><td>Weekday</td><td>Average pages per query</td><td>Average query length</td></tr><tr><td>Query terms</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Coping information</td><td>0.226**</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Results pages browsed</td><td>0.279**</td><td>0.096**</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Unknown risk</td><td>-0.011</td><td>0.453**</td><td>0.089**</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Dread risk</td><td>-0.041**</td><td>-0.098**</td><td>0.015</td><td>0.108**</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Average number of queries/session</td><td>0.162**</td><td>0.065**</td><td>0.040**</td><td>0.097**</td><td>0.024</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>LG (active days)</td><td>0.096**</td><td>-0.049**</td><td>-0.036**</td><td>-0.011</td><td>-0.061**</td><td>0.116**</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Network attack intensity</td><td>0.018</td><td>0.026</td><td>0.003</td><td>-0.028*</td><td>0.069**</td><td>-0.003</td><td>0.028*</td><td>1</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Prior clicks on security</td><td>0.354**</td><td>0.039**</td><td>0.086**</td><td>0.012</td><td>0.060**</td><td>0.118**</td><td>0.114**</td><td>0.001</td><td>1</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Weekday</td><td>-0.021</td><td>0.013</td><td>-0.032*</td><td>0.029*</td><td>0.011</td><td>-0.021</td><td>0.019</td><td>-0.138**</td><td>-0.024</td><td>1</td><td>—</td><td>—</td></tr><tr><td>Average pages per query</td><td>0.046**</td><td>-0.055**</td><td>0.187**</td><td>0.011</td><td>-0.026*</td><td>-0.035**</td><td>0.055**</td><td>-0.012</td><td>0.090**</td><td>0.026</td><td>1</td><td>—</td></tr><tr><td>Average query length</td><td>0.399**</td><td>0.176**</td><td>0.029*</td><td>0.117**</td><td>0</td><td>0.410**</td><td>0.223**</td><td>0.013</td><td>0.263**</td><td>-0.011</td><td>-0.059**</td><td>1</td></tr></table>

<sup>∗</sup>Significant at the 0.05 level; <sup>∗∗</sup>significant at the 0.01 level.

Uninformative but proper priors and hyperpriors were used in our model estimation (Ntzoufras 2009). In particular, the covariance matrix è of $\eta _ { i 1 } - \eta _ { i 3 }$ follows a Wishart distribution with a prior covariance matrix as the identity matrix. Each regression coefficient $\beta$ independently follows a normal distribution, having a mean of 0 and a variance of 100. We chose these commonly used prior distributions and their parameter values to represent high uncertainty or prior ignorance (Ntzoufras 2009). Given our large sample size, the prior distributions would not have much influence on the parameter estimates or on convergence (Sinharay 2004).

We simulated three chains. Each chain had 40,000 iterations, and the first 20,000 were discarded as an initial burn-in. We used the last 20,000 iterations of each chain to calculate the statistics of the posterior distributions of the model parameters. We plotted the traces of each estimated parameter for all chains to confirm the adequacy of convergence of the model. All plots showed convergence. The values of Gelman–Rubin convergence statistic (i.e., R-hat calculated by WinBUGS) for all estimated model parameters were approximately 1, suggesting the absence of chain effects and therefore convergence (Brooks and Gelman 1998).

3.4.3. Estimation Results. Correlation coefficients among all variables are summarized in Table 4. Tables 5–7 summarize the estimated parameters for the model, along with 95% credible intervals (i.e., the intervals bounded by the 2.5th and 97.5th percentiles of the posterior distributions and calculated from the MCMC simulations), posterior probabilities, and Bayes factors (BFs; i.e., posterior odds, calculated in favor of $\beta _ { i } > 0 ;$ Kass and Raftery 1995).<sup>4</sup>

The effects of control variables suggest that users’ search habits and search skills in general carry over to their searches for information on security threats, and there is a possible learning effect that spills over across users’ searches. The results also indicate that contextual variables such as network attacks and the day when a search is performed (weekday vs. weekend) affect search behavior. The effects of control variables are largely consistent with prior findings in the area of information search (Baye et al. 2009, Bucklin and Sismeiro 2003, Johnson et al. 2003, Wang et al. 2010).

The results in Table 5 indicate that unknown risk negatively impacts the number of terms used in a search query $\hat { ( \beta } = - 0 . 3 7$ with a BF in favor of $\beta _ { i } > 0$ equals to 0), supporting H1. Dread risk positively impacts the number of terms used in a search query ( = 0001 with a BF in favor of $\beta _ { i } > 0$ between 1 and 3), supporting H4. Table 6 reveals that unknown

IS threats pose significant risks to individuals and organizations (Mookerjee et al. 2011). Lack of necessary knowledge can hinder users from taking needed actions against IS threats. Users may seek related information through search engines. The information retrieved online can improve users’ knowledge of the threats and change their subsequent security behavior. This research suggests that IS threats differ in their risk characteristics, and such differences lead to users’ distinct information-seeking behavior. Risk characteristics of different IS threats can be characterized by two underlying factors: unknown risk and

## 4. Discussion and Conclusions

Table 5 Estimated Model Parameters for the Number of Terms in a Query 4n = 515705

<table><tr><td>Model parameters</td><td>Mean</td><td>Standard deviation</td><td>2.5%</td><td>25%</td><td>Median</td><td>75%</td><td>97.5%</td><td>Posterior probability of β &gt; 0</td><td>BF in favor of β &gt; 0</td></tr><tr><td>Intercept</td><td>-1.29</td><td>0.12</td><td>-1.54</td><td>-1.38</td><td>-1.29</td><td>-1.21</td><td>-1.09</td><td>0.00</td><td>0.00</td></tr><tr><td>Unknown risk</td><td>-0.37</td><td>0.03</td><td>-0.43</td><td>-0.39</td><td>-0.37</td><td>-0.35</td><td>-0.31</td><td>0.00</td><td>0.00</td></tr><tr><td>Dread risk</td><td>0.01</td><td>0.02</td><td>-0.04</td><td>-0.01</td><td>0.01</td><td>0.03</td><td>0.06</td><td>0.64</td><td>1.75</td></tr><tr><td>Average number of queries/session</td><td>-0.01</td><td>0.03</td><td>-0.06</td><td>-0.02</td><td>-0.01</td><td>0.01</td><td>0.04</td><td>0.40</td><td>0.65</td></tr><tr><td>LG (active days)</td><td>0.05</td><td>0.02</td><td>0.02</td><td>0.04</td><td>0.05</td><td>0.06</td><td>0.08</td><td>1.00</td><td>791.08</td></tr><tr><td>Network attack intensity</td><td>0.04</td><td>0.02</td><td>0.00</td><td>0.03</td><td>0.04</td><td>0.06</td><td>0.09</td><td>0.97</td><td>32.73</td></tr><tr><td>Prior clicks on security</td><td>0.10</td><td>0.01</td><td>0.07</td><td>0.09</td><td>0.10</td><td>0.11</td><td>0.13</td><td>1.00</td><td>∞</td></tr><tr><td>Weekday</td><td>-0.01</td><td>0.04</td><td>-0.08</td><td>-0.04</td><td>-0.01</td><td>0.02</td><td>0.06</td><td>0.39</td><td>0.64</td></tr><tr><td>Average pages per query</td><td>-0.02</td><td>0.06</td><td>-0.14</td><td>-0.06</td><td>-0.01</td><td>0.03</td><td>0.09</td><td>0.44</td><td>0.79</td></tr><tr><td>Average query length</td><td>0.42</td><td>0.02</td><td>0.38</td><td>0.40</td><td>0.42</td><td>0.43</td><td>0.45</td><td>1.00</td><td>∞</td></tr></table>

Table 6 Estimated Model Parameters for Seeking Threat-Coping Information 4n = 515705

<table><tr><td>Model parameters</td><td>Mean</td><td>Standard deviation</td><td>2.5%</td><td>25%</td><td>Median</td><td>75%</td><td>97.5%</td><td>Posterior probability of β &gt; 0</td><td>BF in favor of β &gt; 0</td></tr><tr><td>Intercept</td><td>-0.44</td><td>0.15</td><td>-0.74</td><td>-0.54</td><td>-0.44</td><td>-0.35</td><td>-0.16</td><td>0.00</td><td>0.00</td></tr><tr><td>Unknown risk</td><td>-0.81</td><td>0.07</td><td>-0.95</td><td>-0.85</td><td>-0.81</td><td>-0.76</td><td>-0.67</td><td>0.00</td><td>0.00</td></tr><tr><td>Dread risk</td><td>0.21</td><td>0.05</td><td>0.11</td><td>0.18</td><td>0.21</td><td>0.25</td><td>0.31</td><td>1.00</td><td>47,999.00</td></tr><tr><td>Average number of queries/session</td><td>-0.10</td><td>0.05</td><td>-0.21</td><td>-0.13</td><td>-0.10</td><td>-0.06</td><td>0.01</td><td>0.03</td><td>0.04</td></tr><tr><td>LG (active days)</td><td>-0.11</td><td>0.03</td><td>-0.17</td><td>-0.13</td><td>-0.11</td><td>-0.08</td><td>-0.04</td><td>0.00</td><td>0.00</td></tr><tr><td>Network attack intensity</td><td>0.30</td><td>0.04</td><td>0.21</td><td>0.27</td><td>0.30</td><td>0.33</td><td>0.38</td><td>1.00</td><td>∞</td></tr><tr><td>Prior clicks on security</td><td>0.24</td><td>0.08</td><td>0.10</td><td>0.19</td><td>0.24</td><td>0.30</td><td>0.42</td><td>1.00</td><td>5216.39</td></tr><tr><td>Weekday</td><td>-0.03</td><td>0.06</td><td>-0.16</td><td>-0.07</td><td>-0.03</td><td>0.01</td><td>0.10</td><td>0.32</td><td>0.47</td></tr><tr><td>Average pages per query</td><td>-0.09</td><td>0.13</td><td>-0.32</td><td>-0.19</td><td>-0.10</td><td>0.00</td><td>0.17</td><td>0.26</td><td>0.35</td></tr><tr><td>Average query length</td><td>0.28</td><td>0.04</td><td>0.20</td><td>0.26</td><td>0.28</td><td>0.31</td><td>0.37</td><td>1.00</td><td>∞</td></tr></table>

Table 7 Estimated Model Parameters for the Number of Results Pages Browsed 4n = 515705

<table><tr><td>Model parameters</td><td>Mean</td><td>Standard deviation</td><td>2.5%</td><td>25%</td><td>Median</td><td>75%</td><td>97.5%</td><td>Posterior probability of β &gt; 0</td><td>BF in favor of β &gt; 0</td></tr><tr><td>Intercept</td><td>-2.22</td><td>0.23</td><td>-2.66</td><td>-2.37</td><td>-2.22</td><td>-2.07</td><td>-1.78</td><td>0.00</td><td>0.00</td></tr><tr><td>Unknown risk</td><td>-0.38</td><td>0.11</td><td>-0.59</td><td>-0.45</td><td>-0.38</td><td>-0.31</td><td>-0.17</td><td>0.00</td><td>0.00</td></tr><tr><td>Dread risk</td><td>0.37</td><td>0.07</td><td>0.23</td><td>0.32</td><td>0.37</td><td>0.42</td><td>0.51</td><td>1.00</td><td>∞</td></tr><tr><td>Average number of queries/session</td><td>0.17</td><td>0.07</td><td>0.03</td><td>0.13</td><td>0.17</td><td>0.22</td><td>0.31</td><td>0.99</td><td>140.68</td></tr><tr><td>LG (active days)</td><td>-0.08</td><td>0.05</td><td>-0.17</td><td>-0.11</td><td>-0.08</td><td>-0.05</td><td>0.01</td><td>0.05</td><td>0.05</td></tr><tr><td>Network attack intensity</td><td>0.19</td><td>0.07</td><td>0.06</td><td>0.14</td><td>0.19</td><td>0.23</td><td>0.32</td><td>1.00</td><td>457.89</td></tr><tr><td>Prior clicks on security</td><td>0.16</td><td>0.04</td><td>0.08</td><td>0.13</td><td>0.16</td><td>0.19</td><td>0.25</td><td>1.00</td><td>34,284.71</td></tr><tr><td>Weekday</td><td>-0.27</td><td>0.10</td><td>-0.46</td><td>-0.34</td><td>-0.27</td><td>-0.21</td><td>-0.08</td><td>0.00</td><td>0.00</td></tr><tr><td>Average pages per query</td><td>1.35</td><td>0.12</td><td>1.12</td><td>1.27</td><td>1.35</td><td>1.43</td><td>1.60</td><td>1.00</td><td>∞</td></tr><tr><td>Average query length</td><td>-0.06</td><td>0.06</td><td>-0.18</td><td>-0.10</td><td>-0.06</td><td>-0.02</td><td>0.06</td><td>0.16</td><td>0.18</td></tr></table>

risk significantly reduces $( \beta = - 0 . 8 1$ with a BF in favor of $\beta _ { i } > 0$ equals to 0), whereas dread risk significantly increases the likelihood of actively searching for threat-coping information $( \beta = 0 . 2 1$ with a BF in favor of $\bar { \beta } _ { i } > \bar { 0 }$ greater than 150), supporting H2 and H5. Table 7 indicates that unknown risk negatively impacts the number of results pages browsed $( \beta = - 0 . { \bar { 3 } } 8$ with a BF in favor of $\beta _ { i } > 0$ equals to 0) supporting H3A, and dread risk positively affects the number of pages browsed $( \beta \doteq 0 . 3 7$ with a BF in favor of $\beta _ { i } > 0$ greater than 150), supporting H6. We performed a number of additional analyses to test the robustness of the results, as detailed in Online Appendix F.

dread risk. Threats with unknown risk, which are less understood, fairly new, and difficult to observe, drive searchers to use fewer query terms and browse fewer results pages, and are less likely to cause searchers to look for threat-coping information. By contrast, threats with dread risk, which have an immediate and severe impact and are more dreadful, lead to more search terms, the browsing of more pages, and a high likelihood of seeking for threat-coping information.

## 4.1. Theoretical Implications

By extending psychometric analysis from risk analysis fields to the domain of IS, this Research Note introduces a novel angle from which to understand IS threats. Because different threats pose varied levels of unknown and dread risk to end users, it is important for researchers to control for the risk characteristics besides perceived severity and probability when investigating end users’ behaviors in responding to security threats. Additionally, when comparing the results across studies, researchers should take into account the types of IS threats examined.

Although a number of studies in IS have investigated end users’ IS behaviors (Anderson and Agarwal 2010, Herath and Rao 2009, Johnston and Warkentin 2010), studies remain sparse on how users seek out relevant information and which factors act as drivers for their seeking behavior. Our study sheds light on this research direction by applying information foraging theory. Our analyses show that the two underlying factors characterizing IS threats exert differential effects on information-seeking behavior. When confronting different threats with distinct characteristics, users demonstrate different information needs and adopt different search strategies.

Prior studies on IS have emphasized users’ awareness and participation and alluded to the importance of information seeking. As suggested by Spears and Barki (2010, p. 509), “users demonstrated awareness by asking questions and proactively performing their security responsibilities.” Our study takes this one step further by showing that threat information seeking may be one of the critical components of users’ IS behavior, following the path of threat discovery to threat information seeking and collection to threat response. Information seeking may serve as the mediator between risk characteristics and actual threatresponse behaviors (Kievik and Gutteling 2011). Users may engage in different security behaviors to cope with these threats depending on what information they have obtained. Future research could explore the role that information seeking plays in people’s behavioral responses to IS threats.

Our study demonstrated that Web search logs could be viable data sources for future research on risk-information-seeking behavior. As search engines become increasingly powerful and more people use search engines to search for information, including risk-related information, search engine logs will provide a unique opportunity to observe what and how people are searching when confronted with risks in real life. As Mahmood et al. (2010, p. 433) suggested, search engine logs are “a rich source of data” and “can be identified and used as proxy data for research” in IS. Prior studies on risk-information-seeking behavior have primarily relied on interview, survey, and laboratory observations (Hovick et al. 2011, Kahlor 2007, Kuttschreuter 2006, ter Huurne et al. 2009). Search engine logs could complement these field studies by providing objective measures of users’ riskinformation-seeking behavior (Mahmood et al. 2010).

## 4.2. Practical Implications

Our study has a number of practical implications for the design of effective IS awareness programs and the dissemination of IS knowledge. Improving an organization’s IS requires cutting-edge detection and protection technologies and well-designed IS policies. Even where these technologies and policies have been in place, however, their effectiveness could be undermined by users’ lack of knowledge (Luo and Liao 2007, Spears and Barki 2010). Traditionally, user training and awareness programs are provided in a way that users take a rather passive role, by accepting knowledge pushed to them (Puhakainen and Siponen 2010). These programs may be less effective due to users’ diverse backgrounds and knowledge bases and the complexity of the IS field. This study suggests that organizations may motivate and actively engage users in knowledge discovery of IS.

Our study suggests that users have different information needs for different threats due to associated unknown risk and dread risk. The results point out the possibilities that organizations could design risk communication messages to improve the effectiveness of IS education. Using risk communication messages such as fear appeals is an important strategy motivating users to engage in responsible security behaviors (Johnston and Warkentin 2010). Such messages should be properly framed with the considerations of the effects of both unknown and dread risk to avoid users’ underestimating or misunderstanding of the risk, which might otherwise cause resistance to IS policies. Messages tailored based on risk characteristics may alter individuals’ risk perceptions toward security threats and subsequently motivate individuals to engage in learning as well as protective behavior.

Our study further indicates that in designing decision aids to augment search engines’ performance, the risk characteristics of the threats being searched for may be factored into the search results’ ranking. For example, if users search for a threat with a high dread risk, threat-coping information should be weighted as more relevant than threat-appraisal information when ranking the results. In other words, pages containing protective information could be ranked higher when a search engine sorts results for a query intended for a threat with high dread risk. Similarly, threat-appraisal information should be given more weight when users search for a threat with high unknown risk.

## 4.3. Limitations and Future Studies

Our study has a few limitations. First, following psychometric analysis (Fischhoff et al. 1978; Slovic 1987; Slovic et al. 1980, 1987), the study characterizes the threats by aggregating individuals’ survey responses. Although factor scores resulted from our survey conducted at two different time points are highly correlated, indicating that the characterizations are relatively stable over time, we call for more objective risk measures to be developed in the future to validate the results. In addition, psychometric analysis does not adequately consider individual differences (Kraus and Slovic 1988). Future research may investigate how and why individuals rated threats differently. Besides, the aggregation of individual responses may lose some information in the data. A factor analysis method based on individual responses (instead of using aggregated responses) might be developed to complement the current method. Given that each respondent rated all 20 threats repeatedly with a 10- item instrument, such a method needs to take account of unobserved individual heterogeneity (e.g., panel data analysis with random (or fixed) effects).

Second, the participants in our survey were all college students. Although student samples have been used frequently by prior studies to elucidate IS behavior and risk perceptions toward different hazards, we call for future studies to use larger and more diverse samples to validate the findings. Furthermore, our current survey focused on just 20 common IS threats. Because a range of IS threats exist and their number keeps growing, future research might consider including more threats to validate and generalize our findings.

Third, in this study we could not control for individual characteristics such as demographics, computer self-efficacy, and risk preference (e.g., risk seeking versus risk avoidance) when estimating our regression models due to the limitations of the search engine log. Future research could investigate how those variables impact information-seeking behavior for IS threats.

Fourth, although search engines have become major information-seeking tools, users may conduct their searches through other channels. For example, they may go directly to antivirus vendors’ websites or other professional websites, or even contact their systems administrators for IS advice. Future research might investigate how unknown risk and dread risk could affect the IS search through these channels.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0581.

## Acknowledgments

The authors thank the senior editor, associate editor, and review team for critical comments that greatly improved this paper. The authors also thank Dr. Bernardo Huberman, HP Senior Fellow, for various comments that helped guide this work. This research was supported in part by the National Science Foundation [Grants 1227353, 1419856, and 1420758]. The usual disclaimer applies.

## References

Allen BL (1991) Topic knowledge and online catalog search formulation. Library Quart. 61(2):188–213.

Anderson CL, Agarwal R (2010) Practicing safe computing: A multimethod empirical examination of home computer user security behavioral intentions. MIS Quart. 34(3):613–643.

Baeza-Yates R, Ribeiro-Neto B (1999) Modern Information Retrieval (Addison Wesley, New York).

Bailey P, White RW, Liu H, Kumaran G (2010) Mining historic query trails to label long and rare search engine queries. ACM Trans. Web 1(2):1–25.

Baye MR, Gatti JRJ, Kattuman P, Morgan J (2009) Clicks, discontinuities, and firm demand online. J. Econom. Management Strategy 18(4):935–975.

Boholm Å (1998) Comparative studies of risk perception: A review of twenty years of research. J. Risk Res. 1(2):135–163.

Braverman M, Williams J, Mador Z (2006) Microsoft security intelligence report. Microsoft, Redmond, WA.

Brooks S, Gelman A (1998) General methods for monitoring convergence of iterative simulations. J. Comput. Graphical Statist. 7(4):434–455.

Brucks M (1985) The effects of product class knowledge on information search behavior. J. Consumer Res. 12(1):1–16.

Bucklin RE, Sismeiro C (2003) A model of Web site browsing behavior estimated on clickstream data. J. Marketing Res. 40(3): 249–267.

Chou PHB, Wister AV (2005) From cues to action: Information seeking and exercise self–care among older adults managing chronic illness. Canadian J. Aging 24(4):395–408.

Compeau D, Marcolin B, Kelley H, Higgins C (2012) Generalizability of information systems research using student subjects— A reflection on our practices and recommendations for future research. Inform. Systems Res. 23(4):1093–1109.

D’Arcy J, Hovav A, Galletta D (2009) User awareness of security countermeasures and its impact on information systems misuse: A deterrence approach. Inform. Systems Res. 20(1):79–98.

Duff DE (2014) A comparative study of nuclear power risk perceptions with selected technological hazards. Unpublished doctoral dissertation, North Dakota State University, Fargo.

Fischhoff B, Slovic P, Lichtenstein S, Read S, Combs B (1978) How safe is safe enough? A psychometric study of attitudes towards technological risks and benefits. Policy Sci. 9(2):127–152.

Gelman A, Carlin JB, Stern HS, Rubin DB (2003) Bayesian Data Analysis, 2nd ed. (Chapman and Hall/CRC, Boca Raton, FL).

Geman S, Geman D (1984) Stochastic relaxation, Gibbs distributions, and the Bayesian restoration of images. IEEE Trans. Pattern Anal. Machine Intelligence 6(6):721–741.

Gordon ME, Slade LA, Schmitt N (1986) The “Science of the Sophomore” revisited: From conjecture to empiricism. Acad. Management Rev. 11(1):191–207.

Griffin R, Dunwoody S, Neuwirth K (1999) Proposed model of the relationship of risk information seeking and processing to the development of preventive behaviors. Environ. Res. 80(2): S230–S245.

Heit E (1997) Knowledge and concept learning. Lamberts K, Shanks D, eds. Knowledge, Concepts, and Categories (Psychology Press, Hove, UK), 7–41.

Herath T, Rao HR (2009) Protection motivation and deterrence: A framework for security policy compliance in organizations. Eur. J. Inform. Systems 18(2):106–125.

Holscher C, Strube G (2000) Web search behavior of Internet experts and newbies. Comput. Networks 33(1–6):337–346.

Hovick SR, Freimuth VS, Johnson-Turbes A, Chervin DD (2011) Multiple health risk perception and information processing among African Americans and whites living in poverty. Risk Anal. 31(11):1789–1799.

Hsiao C (2003) Analysis of Panel Data, 2nd ed. (Cambridge University Press, New York).

Jarvenpaa SL, Shaw TR, Staples DS (2004) Toward contextualized theories of trust: The role of trust in global virtual teams. Inform. Systems Res. 15(3):250–267.

Johnson EJ, Bellman S, Lohse GL (2003) Cognitive lock-in and the power law of practice. J. Marketing 67(2):62–75.

Johnston AC, Warkentin M (2010) Fear appeals and information security behavior: An empirical study. MIS Quart. 34(3): 549–566.

Jonas E, Graupmann V, Frey D (2006) The influence of mood on the search for supporting versus conflicting information: Dissonance reduction as a means of mood regulation? Personality Soc. Psych. Bulletin 32(3):3–15.

Jones S (2002) The Internet goes to college: How students are living in the future with today’s technology. Pew Internet and American Life Project, Washington, DC.

Kahlor LA (2007) An augmented risk information seeking model: The case of global warming. Media Psych. 10(3):414–435.

Kass RE, Raftery AE (1995) Bayes factors. J. Amer. Statist. Assoc. 90(430):773–795.

Kelly D, Cool C (2002) The effects of topic familiarity on information search behavior. 2nd ACM/IEEE-CS Joint Conf. Digital Libraries (ACM, Portland, OR), 74–75.

Kievik M, Gutteling JM (2011) Yes, we can: Motivate Dutch citizens to engage in self-protective behavior with regard to flood risks. Natural Hazards 59(3):1475–1490.

Kim K, Kim HJ, Song DJ, Cho YM, Choi J (2014) Risk perception and public concerns of electromagnetic waves from cellular phones in Korea. Bioelectromagnetics 35(4):235–244.

Kraus NN, Slovic P (1988) Taxonomic analysis of perceived risk: Modelling individual and group perceptions. Risk Anal. 8(3): 435–455.

Kulviwat S, Guo C, Engchanil N (2004) Determinants of online information search: A critical review and assessment. Internet Res. 14(3):245–253.

Kuttschreuter M (2006) Psychological determinants of reactions to food risk messages. Risk Anal. 26(4):1045–1057.

Leroy G, Xu J, Chung W, Eggers S, Chen H (2007) An end user evaluation of query formulation and results review tools in three medical meta-search engines. Internat. J. Medical Informatics 76(11):780–789.

Liang H, Xue Y (2009) Avoidance of information technology threats: A theoretical perspective. MIS Quart. 33(1):71–90.

Lion R, Meertens RM, Bot I (2002) Priorities in information desire about unknown risks. Risk Anal. 22(4):765–776.

Luo X, Liao Q (2007) Awareness education as the key to ransomware prevention. Inform. Systems Security 16(4):195–202.

Mahmood MA, Siponen M, Straub D, Rao HR, Raghu T (2010) Moving toward black hat research in information systems security: An editorial introduction to the special issue. MIS Quart. 34(3):431–433.

Marris C, Langford I, Saunderson T, O’Riordan T (1997) Exploring the “psychometric paradigm”: Comparisons between aggregate and individual analyses. Risk Anal. 17(3):303–312.

Mookerjee V, Mookerjee R, Bensoussan A, Yue WT (2011) When hackers talk: Managing information security under variable attack rates and knowledge dissemination. Inform. Systems Res. 22(3):606–623.

Morris EJ (2011) A semi-quantitative approach to GMO risk-benefit analysis. Transgenic Res. 20(5):1055–1071.

Neuendorf KA (2002) The Content Analysis Guidebook (Sage, Thousand Oaks, CA).

Neuwirth K, Dunwoody S, Griffin RJ (2000) Protection motivation and risk communication. Risk Anal. 20(5):721–734.

Newman JW, Staelin R (1972) Prepurchase information seeking for new cars and major household appliances. J. Marketing Res. 9(3):249–257.

Ngo LT, Bruhn R, Custer B (2013) Risk perception and its role in attitudes toward blood transfusion: A qualitative systematic review. Transfusion Medicine Rev. 27(2):119–128.

Ntzoufras I (2009) Bayesian Modeling Using WinBUGS (John Wiley & Sons, Hoboken, NJ).

Pass G, Chowdhury A, Torgeson C (2006) A picture of search. First Internat. Conf. Scalable Inform. Systems 4INFOSCALE ’065 (ACM, New York).

Pirolli P (2007) Information Foraging Theory: Adaptive Interaction with Information (Oxford University Press, New York).

Pirolli P, Card S (1995) Information foraging in information access environments. Conf. Human Factors Comput. Systems (ACM, New York), 51–58.

Pirolli P, Card S (1999) Information foraging. Psych. Rev. 106(4): 643–675.

Portell M, Gil RM, Losilla JM, Vives J (2014) Characterizing occupational risk perception: The case of biological, ergonomic and organizational hazards in Spanish healthcare workers. Spanish J. Psych. 17(e51):1–12.

Puhakainen P, Siponen M (2010) Improving employees’ compliance through information systems security training: An action research study. MIS Quart. 34(4):757–778.

Punj GN, Staelin R (1983) A model of consumer information search behavior for new automobiles. J. Consumer Res. 9(4):366–380.

Richardson R (2008) CSI computer crime and security survey, Computer Security Institute, New York.

Sachse K, Jungermann H, Belting JM (2012) Investment risk—The perspective of individual investors. J. Econom. Psych. 33(3): 437–447.

Sandman PM (1993) Responding to Community Outrage: Strategies for Effective Risk Communication (American Industrial Hygiene Association, Fairfax, VA).

Schmidt JB, Sprang RA (1996) A proposed model of external consumer information search. J. Acad. Marketing Sci. 24(3): 246–256.

Sinharay S (2004) Experiences with Markov chain Monte Carlo convergence assessment in two psychometric examples. J. Educational Behavioral Statist. 29(4):461–488.

Slovic P (1987) Perception of risk. Science 236(4700):280–285.

Slovic P (2000) The Perception of Risk (Earthscan, Sterling, VA).

Slovic P, Fischhoff B, Lichtenstein S (1980) Facts and fears: Understanding perceived risk. Schwing R, Albers WA, eds. Societal Risk Assessment: How Safe Is Safe Enough? (Plenum, New York), 181–216.

Slovic P, MacGregor DG, Kraus NN (1987) Perception of risk from automobile safety defects. Accident Anal. Prevention 19(5): 359–373.

Spears JL, Barki H (2010) User participation in information systems security risk management. MIS Quart. 34(3):503–522.

Spiegelhalter D, Thomas A, Best N, Lunn D (2003) WinBUGS user manual. MRC Biostatistics Unit, Institute of Public Health, Cambridge, UK.

Srinivasan N (1990) Pre-purchase external search for information. Zeithaml VA, ed. Review of Marketing (American Marketing Association, Chicago), 153–189.

Straub DW, Welke RJ (1998) Coping with systems risk: Security planning models for management decision making. MIS Quart. 22(4):441–469.

ter Huurne EFJ, Griffin RJ, Gutteling JM (2009) Risk information seeking among U.S. and Dutch residents: An application of the

model of risk information seeking and processing. Sci. Commun. 31(2):215–237.

Turner D, Fossi M, Johnson E, Mack T, Blackbird J, Entwisle S, Low MK, McKinney D, Wueest C (2008) Internet security threat report. Symantec Corporation, Cupertino, CA.

Vakkari P, Pennanen M, Serola S (2003) Changes of search terms and tactics while writing a research proposal: A longitudinal case study. Inform. Processing Management 39(3):445–463.

Wang J, Xiao N, Rao HR (2010) Drivers of information security search behavior: An investigation of network attacks and vulnerability disclosures. ACM Trans. Management Inform. Systems 1(1):Article 3.

Wang J, Xiao N, Rao HR (2012) An exploration of risk information search via a search engine: Queries and clicks in healthcare and information security. Decision Support Systems 52(2):395–405.

Wang M, Keller C, Siegrist M (2011) The less you know, the more you are afraid of—A survey on risk perceptions of investment products. J. Behavioral Finance 12(1):9–19.

Warkentin M, Willison R (2009) Behavioral and policy issues in information systems security: The insider threat. Eur. J. Inform. Systems 18(2):101–105.

Whitman ME (2003) Enemy at the gate: Threats to information security. Commun. ACM 46(8):91–95.

Wildmuth BM (2004) The effects of domain knowledge on search tactic formulation. J. Amer. Soc. Inform. Sci. Technol. 55(3): 246–258.

Ybarra ML, Sumanb M (2006) Help seeking behavior and the Internet: A national survey. Internat. J. Medical Informatics 75(1): 29–41.

Zhang X, Anghelescu HGB, Yuan X (2005) Domain knowledge, search behaviour, and search effectiveness of engineering and science students: An exploratory study. Inform. Res. 10(2): Paper 217. http://InformationR.net/ir/10-2/paper217.html.

Zillmann D, Bryant J (1985) Affect, mood, and emotion as determinants of selective exposure. Zillmann D, Bryant J, eds. Selective Exposure to Communication (Lawrence Erlbaum, Hillsdale, NJ).
