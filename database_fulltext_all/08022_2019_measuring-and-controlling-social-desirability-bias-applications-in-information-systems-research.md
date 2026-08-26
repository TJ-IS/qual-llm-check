---
otero_id: 8022
otero_key: "6Q6Z9548"
title: "Measuring and Controlling Social Desirability Bias: Applications in Information Systems Research"
authors: "Dong-Heon Kwak; Philipp Holtkamp; and Sung S. Kim"
year: "2019"
journal: "Journal of the Association for Information Systems"
doi: "10.17005/1jais.00537"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
4-29-2019

# Measuring and Controlling Social Desirability Bias: Applications in Information Systems Research

Dong-Heon Kwak , dkwak@kent.edu

Philipp Holtkamp , philipp.holtkamp@wartsila.com

Sung S. Kim , skim@bus.wisc.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Measuring and Controlling Social Desirability Bias: Applications in Information Systems Research

Dong-Heon Kwak<sup>1</sup>, Philipp Holtkamp<sup>2</sup>, Sung S. Kim<sup>3</sup>

<sup>1</sup>Kent State University, USA, dkwak@kent.edu <sup>2</sup>Wartsila Corporation, Finland, philipp.holtkamp@wartsila.com <sup>3</sup>University of Wisconsin, USA, skim@bus.wisc.edu

## Abstract

Despite the potential risks that social desirability (SD) bias poses to the validity of information systems (IS) research, little is known about the extent of such bias. This study examines the extent of SD bias in the IS domain and compares alternative techniques for measuring it. Our findings suggest that despite the popularity of the Marlowe-Crowne scale in IS research, the impression management scale functions better in assessing the extent of SD bias. We also found that under certain circumstances, SD bias can threaten the validity of IS research. This study contributes to the IS literature by showing the difference in SD bias across IS contexts and suggesting an effective way to test for the presence of SD bias.

Keywords: Social Desirability Bias, Social Desirability Scale, Indirect Questioning, Covariance Technique, SNS Addiction, Digital Piracy

Traci Carte was the accepting senior editor. This research article was submitted on August 30, 2016, and went through three revisions.

## 1 Introduction

Response bias is a systematic tendency to answer a range of survey items in a certain way without regard for the content of a specific item (Paulhus, 1991). Among various response biases, social desirability (SD) bias is considered one of the most prominent in survey research (Hart, Ritchie, Hepper, & Gebauer, 2015; Steenkamp, De Jong, & Baumgartner, 2010). SD bias<sup>1</sup> is a tendency for subjects to distort their selfreporting by overestimating socially desirable behaviors (e.g., helping others) and by underestimating socially undesirable behaviors (e.g., downloading illegal software) (Arnold, Feldman, & Purbhoo, 1985; Barger, 2002; Paulhus, 1991). SD bias is problematic because it can affect the means and relationships of research variables and eventually lead to invalid theoretical or practical conclusions (Fisher, 1993). This is especially relevant in research disciplines that typically rely on self-report surveys. Consequently, numerous efforts have been made to assess and control SD bias across disciplines such as psychology (Crowne & Marlowe, 1964), management (Arnold et al., 1985), business ethics (Randall & Fernandes, 1991), marketing (Mick, 1996), and medicine (Herbert, Clemow, Pbert, Ockene, & Ockene, 1995).

Information systems (IS) researchers continue to try to assess the extent of SD bias to ensure that their work is free of it (e.g., Sojer, Alexy, Kleinknecht, & Henkel, 2014; Soror, Hammer, Steelman, Davis, & Limayem, 2015; Turel, Serenko, & Giles, 2011; Turel & Serenko, 2012; Vance, Lowry, & Eggett, 2015). The most popular assessment approach has been to use an SD scale in a survey and then examine the correlation(s) between it and research variables (Bagozzi, 2011; Paulhus, 1991). These IS studies have generally used the short form of the Marlowe-Crowne (MC) scale (e.g., Soror et al., 2015; Turel et al., 2011). Their results have mostly indicated that SD bias was not a problem. Meanwhile, numerous methods have been proposed in other disciplines to assess and control SD bias. One of these methods is indirect questioning, in which subjects are asked to answer questions from another person’s perspective (Fisher, 1993; Fisher & Tellis, 1998; Robertson & Joselyn, 1974). In addition, several other SD scales have been evaluated for efficiency and effectiveness (Blake, Valdiserri, Neuendorf, & Nemeth, 2006; Paulhus, 1984, 1991). This stream of research generally suggests that SD bias is a serious threat to the validity of research findings and that some techniques for assessing it are inadequate. Thus, an interesting question is how the popular MC method used in IS research compares with these alternatives. More important, it is necessary to evaluate the extent of SD bias across different contexts in the IS domain, but especially through alternative techniques.

In our effort to fill the gap in the IS literature on SD bias, we have three objectives. Our first is to examine indirect questioning and then compare it with direct questioning to evaluate the extent of SD bias across different IS settings. Indirect questioning has been shown to reduce the level of SD bias. Thus, it is less prone to SD bias (Fisher, 1993). Although a few IS studies have used indirect questioning to lessen SD bias (Posey et al., 2011; Snow et al., 2007), our study is one of only a few that have compared the effectiveness of indirect and direct questioning in identifying SD bias in IS research. Our second objective is to examine the balanced inventory of desirable responding (BIDR) (Paulhus, 1984) as a possible alternative to the MC scale. Both have been popular SD scales in other disciplines (Hart et al., 2015) in which the BIDR has been shown to outperform the MC scale (Steenkamp et al., 2010). However, the BIDR has not been used in IS research. Thus, its efficacy in the IS field is unknown. Finally, our third objective is to determine if contextual differences affect SD bias. SD bias is increasingly an important issue in such areas of IS research as technology addiction and information security (e.g., Turel et al., 2011; Vance et al., 2015). We are interested in evaluating any differences in SD bias across different IS contexts.

This paper is organized as follows. The next section is a review of techniques for measuring and controlling SD bias. Next is an examination of current practices in addressing SD bias in IS research. Following that, we pose our research questions, which is followed by a presentation of two research models for testing SD bias and by a discussion of our methods, data analyses, and results. Finally, we conclude with a discussion of our theoretical, methodological, and practical contributions, along with noting the limitations of our study and outlining directions for future research.

## 2 Techniques for Measuring SD Bias

In evaluating various techniques for measuring and controlling SD bias, we will first discuss indirect questioning and its characteristics as a tool for assessing SD bias. Then we will review existing SD scales designed to capture SD bias and compare their performance.

## 2.1 Indirect Questioning Versus Direct Questioning

Indirect questioning is a projective technique in which respondents are asked to answer from the perspective of another person or group (Robertson & Joselyn, 1974). Typically, indirect questions are used to ask respondents to predict the thoughts or actions of others similar to themselves (Fisher & Tellis, 1998). A key assumption is that respondents will project their own behavior onto the other person or group and thus reveal their own attitudes (Fisher, 1993). The use of indirect questions helps reduce the distortion that private opinions can introduce (Fisher & Tellis, 1998) and allows respondents to answer from an impersonal position (Simon & Simon, 1974). In three distinct studies, Fisher (1993) found a significant difference on socially sensitive variables between the respondents ratings for themselves and their ratings for others. However, no difference was identified for variables that could be understood as socially insensitive. These findings indicate that, compared with direct questioning, indirect questioning shows significantly different results for socially sensitive variables and would reduce SD bias on sensitive questions.

To show the validity of indirect questioning, Fisher and Tellis (1998) used estimated true scores and Reynolds’ (1982) short form of the MC scale. More specifically, Fisher and Tellis (1998) examined how strongly these measures correlated with indirect and direct questions. The results showed the SD scale was associated significantly with direct questions, but not with indirect questions. Additionally, the correlation of indirect questions with the estimated true scores (r = .93) was significantly higher than the correlation of direct questions with the estimated true scores $( r =$ .61). These findings strongly support the superiority of indirect questioning vis-à-vis direct questioning as a proxy for an underlying true value.

Indirect questioning has been used widely in business ethics, marketing, accounting, and consumer behavior (e.g., Cohen, Pant, Sharp, & Holder-Webb, 2006; Keep, 2009; Miller & Thomas, 2005; Sierra & Hyman, 2006; Sinha & Mandel, 2008). For example, Neeley and Cronley (2004) conducted two studies to examine the effects of SD bias in consumer research. The results showed that indirect questioning led to higher scoring responses for socially undesirable behavior and lower scoring responses for socially desirable behavior. In the IS discipline, several studies exist that used indirect questioning (e.g., Posey, Bennett, Roberts, & Lowry, 2011; Snow, Keil, & Wallace, 2007). Snow et al. (2007) analyzed the effects of biases on software project status reports. In addition, Posey et al. (2011) examined the effect of privacy invasion and organizational injustice on computer abuse. Yet none of these studies explicitly compared direct and indirect questioning. This omission still leaves us uncertain of the extent of SD bias when this earlier research used direct questioning.

In summary, indirect questioning has been shown to reduce the amount of SD bias by allowing respondents to project their own attitudes onto others they consider similar to themselves. Accordingly, indirect questioning is widely regarded as a reasonable estimate, compared with direct questioning, of the true scores of socially sensitive variables. However, little research has been done in the IS discipline on the difference in results, if any, between direct and indirect questioning.

## 2.2 Self-Report Measures of Social Desirability

A nonsignificant correlation between an SD scale and research variables implies a piece of evidence suggesting lack of SD bias (Fisher, 1993; Hart et al., 2015; Paulhus, 1991). Many scales have been proposed as tools for assessing the extent of SD bias (see Paulhus, 1991 for a review). In particular, the MC scale (Crowne & Marlowe, 1960) has been the most frequently used scale for assessing SD bias (Barger, 2002; Fisher & Tellis, 1998; Hart et al., 2015). A large number of papers have also confirmed the reliability and validity of the scale on a variety of different population groups (Loo & Loewen, 2004). As an SD scale used extensively in the literature, the MC scale is considered useful for comparing the findings of alternative studies.

The original MC scale is long, with 33 items. Because of the length of the original scale, various shorter forms of only 10 to 20 items have been proposed. Table 1 summarizes the original and popular shortened versions of the MC scale.<sup>2</sup> Despite their popularity, the MC scale and its short forms have limitations. First, the MC scale includes insensitive items; thus, it is considered ineffective in assessing SD bias (Ballard & Crino, 1988; Hart et al., 2015). More importantly, research suggests that the MC scale, which is intended to represent a single concept, actually reflects multiple concepts (Barger, 2002; Leite & Beretvas, 2005; Paulhus, 1984; Steenkamp et al., 2010). For example, prior research shows that the MC scale consists of two components: (1) attribution, which refers to one’s tendency to attribute socially desirable characteristics to oneself, and (2) denial, which is one’s tendency to deny having socially undesirable characteristics (Millham, 1974; Ramanaiah, Schill, & Leung, 1977). Meanwhile, Paulhus and Reid (1991) argued for a three-factor model: (1) self-deception enhancement, which is an unconscious tendency to think of oneself positively; (2) self-deception denial, which is an unconscious tendency to deny one’s negative characteristics; and (3) impression management, which is a deliberate attempt to give inflated self-descriptions to others. However, the current literature lacks agreement on the exact dimensional structure of the MC scale. Because of this lack of clarity, some researchers even argue for an end to the use of the MC scale (Barger, 2002; Steenkamp et al., 2010).

Much research suggests that the context of SD bias has two distinct dimensions (Paulhus, 1984; Paulhus & John, 1998; Randall & Fernandes, 1991; Steenkamp et al., 2010). Unlike the MC scale, the BIDR is designed to separate these dimensions. Specifically, the BIDR is a multidimensional instrument composed of 20 items on the self-deception enhancement (SDE) scale and 20 items on the impression management (IM) scale. Despite its enhanced standing with researchers, this 40-item BIDR is still cumbersome to administer. Several attempts have been made to shorten it (Hart et al., 2015; Steenkamp et al., 2010). Table 1 contains descriptions of the original BIDR and some of its subsequent versions.

Table 1. The MC scale and the BIDR: Original and Short Forms

<table><tr><td>Origin</td><td>Scale</td><td>Form</td><td>No. of Items</td><td>Range of Reported Reliabilities</td><td>Source</td></tr><tr><td rowspan="7">MC</td><td>MC</td><td>Original</td><td>33</td><td>.88</td><td>Crowne &amp; Marlowe (1960)</td></tr><tr><td>MC Form X1</td><td>Short</td><td>10</td><td>.59 - .70</td><td>Strahan &amp; Gerbasi (1972)</td></tr><tr><td>MC Form X2</td><td></td><td>10</td><td>.49 - .75</td><td></td></tr><tr><td>MC Form XX</td><td></td><td>20</td><td>.73 - .83</td><td></td></tr><tr><td>MC Form C</td><td>Short</td><td>13</td><td>.76</td><td>Reynolds (1982)</td></tr><tr><td>MC Composite</td><td>Short</td><td>13</td><td>.70</td><td>Ballard (1992)</td></tr><tr><td>SDS-17</td><td>Modified</td><td>17</td><td>.74</td><td>Stöber (2001)</td></tr><tr><td rowspan="3">BIDR</td><td>BIDR</td><td>Original</td><td>SDE: 20IM: 20</td><td>SDE: .73IM: .74</td><td>Paulhus (1984)</td></tr><tr><td>BIDR-20</td><td>Short</td><td>SDE: 10IM: 10</td><td>SDE: .49 - .76IM: .67 - .77</td><td>Steenkamp et al. (2010)</td></tr><tr><td>BIDR-16</td><td>Short</td><td>SDE: 8IM: 8</td><td>SDE: .64 - .69IM: .71 - .73</td><td>Hart et al. (2015)</td></tr><tr><td colspan="6">Note: hyphens indicate a range of values, and there are several different intermediate values between the endpoints.</td></tr></table>

Table 2. Reported Correlations with the MC Scale and the BIDR

<table><tr><td>Variable</td><td>MC</td><td>SDE</td><td>IM</td><td>BIDR</td><td>Source</td></tr><tr><td>Edward SD scale</td><td>.24</td><td>.41</td><td>.07</td><td></td><td>Paulhus (1984)</td></tr><tr><td>Wiggins Sd scale</td><td>.40</td><td>-.04</td><td>.48</td><td></td><td>Paulhus (1984)</td></tr><tr><td>Self-reported ethical behavior</td><td>.24</td><td>.10</td><td>.53</td><td>.42</td><td>Randall &amp; Fernandes (1991)</td></tr><tr><td>Desirability of ethical behavior</td><td>.26</td><td>.11</td><td>.49</td><td>.39</td><td>Randall &amp; Fernandes (1991)</td></tr><tr><td>Overclaiming scale</td><td>.18</td><td>.14</td><td>.11</td><td>.13</td><td>Randall &amp; Fernandes (1991)</td></tr><tr><td>Ruch &amp; Newstron&#x27;s ethics scale</td><td>-.17</td><td>-.05</td><td>-.24</td><td>-.19</td><td>Randall &amp; Fernandes (1991)</td></tr><tr><td>Materialism</td><td>-.40</td><td>-.17</td><td>-.36</td><td></td><td>Mick (1996)</td></tr><tr><td>Self-esteem</td><td>.26</td><td>.53</td><td>.21</td><td></td><td>Mick (1996)</td></tr><tr><td>Compulsive buying</td><td>-.31</td><td>-.22</td><td>-.22</td><td></td><td>Mick (1996)</td></tr><tr><td>Vividness of visual imagery</td><td>-.18</td><td>-.35</td><td>-.11</td><td></td><td>Allbutt et al. (2011)</td></tr><tr><td>Average of absolute values</td><td>.26</td><td>.21</td><td>.28</td><td>.28</td><td></td></tr></table>

Whereas the SDE scale measures an individual’s tendency to attribute positive qualities to oneself, the IM scale assesses an individual’s tendency to present a socially desirable self-image to others (Paulhus, 1984). The SDE and IM subscales of the BIDR basically reflect two different personal aspects (Paulhus, 2002; Paulhus & John, 1998; Steenkamp et al., 2010). The SDE reflects a tendency to exaggerate one’s worth in terms of social and intellectual status; it occurs when people emphasize individuality, personal striving, uniqueness, and accomplishment (Paulhus, 2002; Paulhus & John, 1998).

The IM reflects a tendency to reject impulses seen as socially deviant and to exaggerate positive features associated with being a good person in a society; it arises when people highlight relationships, intimacy, affiliations, and benefits to others and to society (Paulhus, 2002; Paulhus & John, 1998). Table 2 lists earlier studies that showed the sensitivity of MC and BIDR (or its subscales) and their effectiveness in detecting SD bias. As shown in Table 2, although the MC scale performs generally well, the BIDR and its subscales outdid the MC scale, at least in some cases.

Thus, it is possible that the BIDR or its subscales may perform better in some IS research contexts. Despite the potential of the BIDR, our literature review shows that it has not been used in IS research. Existing IS research (e.g., Chan & Lai, 2011; Sojer et al., 2014; Soror et al., 2015; Turel et al., 2011) used only Reynolds’ short form of the MC scale and found that SD bias is not a serious concern. However, considering the previously mentioned limitations of the MC scale, the results of its use in IS research cannot be considered conclusive. Thus, it is still an open question as to whether the BIDR is comparable to the MC scale as a technique for assessing SD bias in the IS domain and whether, when evaluated with a new scale, the results of prior studies will remain unchanged.

## 3 Social Desirability Bias in IS Research

Our review of the status of SD bias in IS research begins by reviewing IS research that addressed SD bias in terms of context and reduction, correction, and control methods. Second, we examine the research on IT use and addiction and how SD has been assessed in this context. Third, we examine the literature on information privacy and security and discuss how SD is treated in this context. Finally, we propose three research questions concerning (1) the extent of SD bias in the IS contexts examined in this study, (2) the contextual effects on SD bias, and (3) the relative efficacy of SD scales.

## 3.1 Review of SD Bias in IS

Our goal in the review is to identify how IS research has addressed SD bias. To conduct the review, we narrowed our search to six leading journals: MIS Quarterly (MISQ), Information Systems Research (ISR), Journal of the Association for Information Systems (JAIS), Journal of Management Information Systems (JMIS), European Journal of Information Systems (EJIS), and Information Systems Journal (ISJ). These journals have been regarded as the top publication outlets for IS research. Based on Gergely and Rao (2014), we considered only those empirical studies that addressed SD bias in terms of reduction, detection, or control methods. A total of 1679 papers were published from 2011 to 2017 in the Basket of Six IS journals. We found that 26% of the papers used selfreported measures (432), but only 5% of the surveybased papers (22) attempted to address SD bias, and 2% of them (8) used formal detection or control methods. These results suggest that SD bias is rarely investigated in IS literature, and even for the exceptional cases in which SD bias was mentioned, it was not properly dealt with. Table 3 shows all of the empirical studies (22 papers plus 12 before 2011) that attempted to reduce, detect, or control SD bias in the IS journals mentioned previously.

Table 3 indicates that the authors of 13 articles took steps to detect SD bias, and the authors of seven used an SD scale. Interestingly, all of these seven articles used the MC scale. In addition, all of the researchers who used detection methods concluded that SD bias was not a serious concern. However, as we mentioned earlier, the results of the MC scale are inconclusive because of its several limitations. Thus, it is necessary to use different methods to reevaluate the earlier results. For this reevaluation, we introduce in the following sections two IS domains (i.e., IT addiction and information security) that we suspect are prone to SD bias.

## 3.2 IT Use and Addiction

Most IS researchers have been interested in examining the usability or productivity of an IT application and its impact on IT usage (DeLone & McLean, 1992; Song & Zahedi, 2005; Venkatesh, Thong, & Xu, 2012). For example, the technology acceptance model (TAM) (Davis, Bagozzi, & Warshaw, 1989) has been the most widely used and popular model in the IS domain. This model posits that perceived usefulness (PU) and perceived ease of use (PE) determine a person’s initial use of a new IT tool.

The focus in IS research has been shifting from initial use to continued use. Unlike IT acceptance, postadoption research covers complex phenomena such as habitual, excessive, and pathological use (Ma, Kim, & Kim, 2014; Turel & Serenko, 2010).

Table 3. SD Bias in IS Research

<table><tr><td>Authors</td><td>Year</td><td>Journal</td><td>Context</td><td>Reduction, Detection and Control Methods</td></tr><tr><td>Webster &amp; Martocchio</td><td>1992</td><td>MISQ</td><td>Microcomputer use</td><td>† Examined the relationship between the MC scale and a key variable</td></tr><tr><td>Jarvenpaa &amp; Staples</td><td>2001</td><td>JMIS</td><td>Organizational ownership</td><td>* Indirect questioning</td></tr><tr><td>Peace, Galletta, &amp; Thong</td><td>2003</td><td>JMIS</td><td>Software piracy</td><td>* Used intention as a proxy of behavior</td></tr><tr><td>Al-Natour, Benbasat, &amp; Cenfetelli</td><td>2006</td><td>JAIS</td><td>Online shopping assistant</td><td>† Examined variance of the sensitive variable of ICC score</td></tr><tr><td>Dinev &amp; Hart</td><td>2006</td><td>ISR</td><td>Personal information provision</td><td>* Anonymity</td></tr><tr><td>Pavlou &amp; El Sawy</td><td>2006</td><td>ISR</td><td>New product development</td><td>* Asked subjects to select a familiar work unit. † Examined the mean of sensitive variables</td></tr><tr><td>Dinev &amp; Hu</td><td>2007</td><td>JAIS</td><td>Protective technology adoption</td><td>* Anonymity</td></tr><tr><td>Hulland, Wade, &amp; Antia</td><td>2007</td><td>JMIS</td><td>Retailer&#x27;s online channel development efforts</td><td>* Used proxy ratio variables to generate a composite measure of online commitment</td></tr><tr><td>Tiwana &amp; Bush</td><td>2007</td><td>JMIS</td><td>IT outsourcing decision</td><td>* Conjoint research design</td></tr><tr><td>Iacovou, Thompson, &amp; Smith</td><td>2009</td><td>MISQ</td><td>IS project status reporting</td><td>* Frequency of reporting was used for selective reporting</td></tr><tr><td>Kwan, So, &amp; Tam</td><td>2010</td><td>ISR</td><td>Software piracy</td><td>* Anonymity * Randomized response technique † Direct questioning compared with randomized response technique in subsequent studies</td></tr><tr><td>Pavlou &amp; El Sawy</td><td>2010</td><td>ISR</td><td>New product development</td><td>* Asked subjects to select a familiar work unit † Examined the mean of sensitive variables</td></tr><tr><td>Benlian, Koufaris, &amp; Hess</td><td>2011</td><td>JMIS</td><td>SaaS adoption and use</td><td>* Asked participants to fill out questionnaire regarding one specific SaaS application type</td></tr><tr><td>Chan &amp; Lai</td><td>2011</td><td>EJIS</td><td>Software piracy</td><td>* Anonymity † Examined correlations between the MC scale and other study variables</td></tr><tr><td>Lee &amp; Benbasat</td><td>2011</td><td>ISR</td><td>Product recommendation agent</td><td>* A sensitive construct was measured from content analysis</td></tr><tr><td>Turel et al.</td><td>2011</td><td>MISQ</td><td>eBay addiction</td><td>* Anonymity † Examined correlation between the MC scale and study variables</td></tr><tr><td>Wang &amp; Haggerty</td><td>2011</td><td>JMIS</td><td>Individual virtual competence</td><td>* Careful wording † Examined mean and standard deviation of sensitive variables. † The MC scale was used as a control variable</td></tr><tr><td>Xu, Dinev, &amp; Smith</td><td>2011</td><td>JAIS</td><td>Institutional privacy assurance</td><td>* Anonymity</td></tr><tr><td>Turel &amp; Serenko</td><td>2012</td><td>EJIS</td><td>Habitual use of social networking site</td><td>† Examined correlation between the MC scale and study variables</td></tr><tr><td>Dinev, Xu, Smith, &amp; Hart</td><td>2013</td><td>EJIS</td><td>Information privacy</td><td>* Anonymity * Asked respondents to answer the questions honestly</td></tr><tr><td>Hansen &amp; Walden</td><td>2013</td><td>JAIS</td><td>Unauthorized file sharing</td><td>* Anonymity</td></tr><tr><td>Lowry, Moody, Galletta, &amp; Vance</td><td>2013</td><td>JMIS</td><td>Online whistle-blowing reporting systems for reporting computer abuse</td><td>* Anonymity</td></tr><tr><td>Majchrzak, Wagner, &amp; Yates</td><td>2013</td><td>MISQ</td><td>Knowledge contribution to organizational Wiki</td><td>* Anonymity</td></tr></table>

Table 3. SD Bias in IS Research

<table><tr><td>Brown, Venkatesh, &amp; Goyal</td><td>2014</td><td>MISQ</td><td>Software acceptance</td><td>* Used duration of system use as a measure of use</td></tr><tr><td>D’Arcy, Herath, &amp; Shoss</td><td>2014</td><td>JMIS</td><td>Information security policy violation</td><td>* Anonymity† A five-item subset of the MC scale was used as a control variable and examined its significance</td></tr><tr><td>Sojer et al.</td><td>2014</td><td>JMIS</td><td>Unethical programming behavior</td><td>* Anonymity† Examined cross loading between the MC scale and other study variables‡ Marker variable approach in PLS (Chin et al. 2013)</td></tr><tr><td>Johnston, Warkentin, &amp;Siponen</td><td>2015</td><td>MISQ</td><td>Password security</td><td>* Anonymity</td></tr><tr><td>Lowry &amp; Moody</td><td>2015</td><td>ISJ</td><td>Information security policy</td><td>* Anonymity</td></tr><tr><td>Lowry, Posey, Bennett, &amp; Roberts</td><td>2015</td><td>ISJ</td><td>Computer abuse</td><td>* Anonymity</td></tr><tr><td>Posey, Roberts, &amp; Lowry</td><td>2015</td><td>JMIS</td><td>Organizational information security</td><td>* Anonymity</td></tr><tr><td>Soror et al.</td><td>2015</td><td>ISJ</td><td>Habitual phone use</td><td>† Examined correlation between the MC scale and study variables‡ The MC scale was used as a control variable</td></tr><tr><td>Srivastava, Chandra, &amp; Shirish</td><td>2015</td><td>ISJ</td><td>Employee technostress</td><td>* Forced choice, Anonymity</td></tr><tr><td>Vance et al.</td><td>2015</td><td>MISQ</td><td>System access policy violation</td><td>* Anonymity† Compared parameter estimates between an original model and a model without a sensitive variable</td></tr><tr><td>Kordzadeh &amp; Warren</td><td>2017</td><td>JAIS</td><td>Sharing of personal health information in virtual health community</td><td>* Asked respondents to answer the questions honestly</td></tr><tr><td colspan="5">Notes: * reduction methods, † detection methods; ‡ control methods</td></tr></table>

Specifically, Turel et al. (2011) examined how people use an auction website and demonstrated that addictive use of an online auction distorts an online user’s perceptions of the usefulness and ease of use of the online service. Online addiction, defined as a compulsive and uncontrollable need to use an online service, is widely known to reduce productivity and damage interpersonal relationships (Byun et al., 2009; Kakabadse, Porter, & Vance, 2007). In such an extreme case of postadoption IT use, people tend to be hesitant to reveal their degree of dependency. Thus, the issue of SD bias could arise.

To capture the addiction factor, Turel et al. (2011) incorporated various scales of addiction, including unidimensional and multidimensional measures. They used the short form of the MC scale (Reynolds, 1982) to examine the extent of SD bias. They found that this SD scale marginally correlated with some measures of addiction (the highest Spearman’s rho = -.13, p < .05) and had no significant correlations with the other constructs of PU and PE. Soror et al. (2015) used the short form of the MC scale in a similar way in a study of habitual use of mobile phones.

The results showed that the MC scale had no significant correlations with any research constructs except self-regulation (r = .17, p < .01), which captures individuals’ perception of their ability to control their behavior. These results indicated, as expected, that the MC scale correlates with socially undesirable (e.g., addiction) and desirable (e.g., self-regulation) constructs. However, in those studies, the degrees of correlations were not substantial. Consequently, SD bias was not considered a serious concern (Soror et al., 2015; Turel et al., 2011). However, as discussed previously, the MC scale is said to have some weaknesses; accordingly, it is important to reevaluate the earlier results by using alternative techniques.

## 3.3 Information Privacy and Security

Information privacy has been an important topic in the IS discipline because personal information is stored and exchanged through a variety of online services such as electronic mail, online shopping, and online banking (Hong & Thong, 2013; Malhotra, Kim, & Agarwal, 2004; Sheng, Nah, & Siau, 2008). IS researchers have often attempted to understand individuals’ concerns about information privacy and the impact such concerns have on a person’s willingness to reveal personal information (Bansal, Zahedi, & Gefen, 2015). In these studies, respondents have little reason to disguise their true feelings about their concerns for information privacy and their intention to release personal information. Thus, SD bias has not been a serious issue in information privacy research.

In contrast, information security regularly involves sensitive issues. When people are responsible for fair use of others’ information or copyrighted materials, they are likely to be defensive in explaining their behavior. Research on information security has focused on numerous sensitive topics that include, but are not limited to, digital piracy (Peace et al., 2003), IS misuse (D’Arcy et al., 2009), security software adoption (Johnston & Warkentin, 2010), and compliance with information security policies (Johnston et al., 2015). Despite the sensitivity of the topics examined in information security research, SD bias has gotten little attention (Gergely & Rao, 2014). Unfortunately, few attempts have been made to systematically assess SD bias in information security research. Consequently, we remain uncertain of the extent of SD bias in this research area.

## 3.4 Research Questions

As discussed previously, SD has become an important issue in IS research as the weaknesses of commonly applied self-report surveys have been unveiled. Another factor has been the increasing amount of attention given to the more sensitive and negative aspects of IS and IS usage, such as obsessive use of an IT application (e.g., addiction) and fair use of others’ data (e.g., information security). Our literature review shows that several methods have been used to assess SD bias, and the MC scale was the primary tool used in measuring it. However, so far, little solid evidence has emerged to prove the existence of SD bias. Because of this lack of evidence, several questions remain.

First, it is important for IS researchers to reevaluate SD bias through alternative SD scales (Barger, 2002; Steenkamp et al., 2010). Second, although addictive use of an online service is personally embarrassing to discuss publicly, it does not have immediate legal consequences as in the case, for example, of mishandling copyrighted information. Thus, we questioned whether such a contextual difference would lead to distinct levels of SD bias. Finally, to the best of our knowledge, no research exists in the IS discipline that compares the efficacy of alternative SD scales such as the MC scale, the SDE scale, the IM scale, and the BIDR. It would be interesting to evaluate how these competing tools compare when they are applied to different IS contexts. Thus, we raise the following three research questions:

Research Question 1: What is the extent of SD bias in the areas of technology addiction and information security?

Research Question 2: Is there any difference in SD bias among the different IS contexts?

Research Question 3: Is there any difference among alternative SD scales in terms of their performance in identifying SD bias?

## 4 Methods

## 4.1 Research Settings and Models

We used two separate sets of surveys for IT addiction and information security. For IT addiction, social networking sites (SNS) were selected as a specific empirical setting for two reasons. First, SNS (e.g., Facebook) are familiar to most Internet users, and as of 2016, 79% of online adults used SNS (Greenwood, Perrin, & Duggan, 2016). Second, such symptoms of addiction as neglect of others, lack of self-control, and concealing negative consequences are known to exist among excessive users of SNS (Kuss & Griffiths, 2011). For information security, we chose digital piracy because more than half of Internet users are known to have had encounters with digital piracy (Epstein, 2012). In addition, unlike SNS addiction, which itself is not necessarily illegal, digital piracy often has legal consequences. Moreover, SNS addiction and digital piracy are sensitive topics that are commonly measured through self-report surveys. Accordingly, these two topics are well-suited to represent constructs susceptible to SD bias.

We selected two research models: the IT addiction model for SNS addiction and the threat model of information security behavior for digital piracy. Both are well-established in IS research and considered appropriate for our settings. The IT addiction model (Turel et al., 2011) proposes that IT addiction determines PU, PE, and perceived enjoyment, which in turn, influence behavioral intention. Because our purpose is not to replicate the models but to test the extent of SD bias, we simplified the research models. For SNS addiction (Figure 1A), we examined PU and PE as consequences of SNS addiction because TAM constructs have been well-established but hardly used in SD bias. For digital piracy (Figure 1B), we examined perceived threat severity (SEV) and perceived threat susceptibility (SUS) as predictors of digital piracy intention (DPI). SEV and SUS were chosen because prior information security research has commonly found that users’ perceptions of severity and susceptibility (or certainty) determine users behaviors related to security (D’Arcy et al., 2009; Herath & Rao, 2009; Johnston & Warkentin, 2010; Johnston et al., 2015; Peace et al., 2003).

## 4.2 Measures

Measures were adapted from previously validated scales. Specifically, we prepared two surveys for the two different research contexts, each of which includes direct questions, indirect questions, SD scales, and demographic questions. The appendix contains the survey items used in this study.

In SNS addiction, we used the unidimensional SNS addiction scale adapted from Turel et al. (2011). The items for measuring PU were adapted from Kim and

Son (2009). We measured PE using items adapted from Venkatesh et al. (2012). SNS addiction was used for both direct and indirect questioning because addiction is considered sensitive to SD bias, but TAM constructs are not (Turel et al., 2011). A sample item of direct questioning is “I am addicted to SNS”. In the indirect questioning, subjects were asked to predict the likely responses of “a typical SNS user” based on Fisher (1993). A sample item of indirect questioning is “A typical SNS user is addicted to SNS”.

![](/api/attachments/6Q6Z9548/fulltext/images/d15152eb24bb8521355ada0adf1bd7dee67ac662e7b6021dfefb50a2e88687e5.jpg)  
Figure 1. Research Models

In digital piracy, SEV, SUS, and DPI were adapted from Johnston and Warkentin (2010). DPI is associated with moral and legal issues and thus considered sensitive to SD bias. Thus, DPI was used for direct and indirect questioning. A sample item of direct questioning is “If I had the opportunity, I would commit digital piracy”. For indirect questioning, participants were required to guess the likely responses of “a typical Internet user” (Fisher, 1993). A sample item is “If a typical Internet user had the opportunity, he/she would commit digital piracy”.

We used two sets of SD scales: 13 items of the MC scale (Reynolds, 1982) and 16 items of the BIDR-16 (Hart et al., 2015). The BIDR-16 includes two subsets: 8 items of the SDE scale and 8 items of the IM scale. The MC scale uses a series of scored “yes” or “no” questions with seven reverse coded items (i.e., socially undesirable questions). After converting the reverse coded items, the scales were added together. Therefore, the total scores on the MC scale can range from 0 to 13. The BIDR-16 incorporates a 7-point scale anchored with “not true” and “very true”. After reversing the socially undesirable questions, one point was added for each extreme response (6 or 7). Ranges of total scores on the SDE scale, the IM scale, and the BIDR are 0-8, 0-8, and 0-16, respectively. This scoring ensures that only participants who give exaggeratedly desirable responses get high scores (Paulhus, 1994, 1998).

Finally, both surveys included demographic and background information such as gender, age, education level, employment status, marital status, frequency of SNS usage, and frequency of Internet use.

## 4.3 Data Collection

After the initial versions of the questionnaires were developed, they were pretested by several faculty members and doctoral students who gave feedback on the clarity and content validity of the questionnaires. Their feedback included a recommendation that we give examples of SNS and a definition of digital piracy. Accordingly, we added examples of SNS (Facebook, Twitter, Instagram, etc.) and a definition of digital piracy (unauthorized reproduction or use of a copyrighted book, movie, piece of music, software program, etc.) to the appropriate survey.

After the pretest, we did field studies to collect the data necessary to examine the extent of SD bias. We considered the population of interest to be composed of adult SNS users for SNS addiction and adult Internet users for digital piracy. Then, the database of a market research firm was used to create a nationwide sample frame of panel members ages 18 or older. The market research firm selected two panels with identical demographic backgrounds and sent an email invitation to each person to solicit participation in the web-based survey.

We collected 265 responses for SNS addiction and 279 responses for digital piracy. To test for response bias, we examined whether early and late respondents differed statistically. We found no significant difference in gender (SNS addiction: $\chi ^ { 2 } = 1 . 1 9 , p = . 2 7 ;$ digital piracy: $\chi ^ { 2 } = . 3 6 , p = . 5 5 )$ or age (SNS addiction: F = 2.22, p = .14; digital piracy: $F = . 0 1 , p = 1 . 0 0 )$ . To ensure that only current SNS users were included in data analysis, we excluded nine responses of nonusers in SNS addiction. We also discarded three responses in SNS addiction and four responses in digital piracy because of missing data or failure to follow instructions. These adjustments yielded 251 usable observations in SNS addiction and 278 in digital piracy.

In the final data sets of SNS addiction and digital piracy, average ages were 41.6 and 42.3, and percentages of females were 56% and 51%, respectively; 49% and 40% of subjects spent more than seven hours a week on SNS; and 51% and 53% of subjects spent more than 21 hours a week on the Internet.

## 5 Results

## 5.1 Measurement Models

For measurement models, we conducted a confirmatory factor analysis (CFA) using AMOS 22.0. We examined model fit through various fit criteria. Specifically, the six fit indices used in the current study were the Tucker-Lewis Index (TLI), the comparative fit index (CFI), the goodness-of-fit index (GFI), the adjusted goodness of fit (AGFI), the standardized root mean square residual (SRMR), and the root mean square error of approximation (RMSEA) (Gefen et al., 2000; Hu & Bentler, 1999). As Table 4 shows, the various overall fit indices of the two measurement models suggested a good fit of the models to the data; most of the indices were at or exceeded the recommended thresholds.

Table 4. Goodness of Fit of the Measurement Models

<table><tr><td></td><td> $\chi^2 (DF)$ </td><td> $\chi^2/DF$ </td><td>TLI</td><td>CFI</td><td>GFI</td><td>AGFI</td><td>SRMR</td><td>RMSEA</td></tr><tr><td>Good model fit ranges</td><td></td><td>&lt; 3.00</td><td>&gt;0.90</td><td>&gt;0.90</td><td>&gt;0.90</td><td>&gt;0.80</td><td>&lt; 0.08</td><td>&lt; 0.08</td></tr><tr><td>SNS addiction</td><td>581.525 (339)</td><td>1.715</td><td>0.945</td><td>0.957</td><td>0.866</td><td>0.816</td><td>0.046</td><td>0.053</td></tr><tr><td>Digital piracy</td><td>181.634 (112)</td><td>1.622</td><td>0.961</td><td>0.977</td><td>0.936</td><td>0.881</td><td>0.033</td><td>0.048</td></tr></table>

The measurement quality of constructs was examined further by assessing the validity and reliability of the scales. First, convergent validity is established if the factor loading of an item is .60 (Chin, Gopal, & Salisbury, 1997) or more strictly .707 (Hair, Tatham, Anderson, & Black, 2009). Although the overall fit indices indicate reasonable fit of the model, we dropped ADDi8 (A typical SNS user thinks that he/she is addicted to SNS) in SNS addiction because of low standardized factor loading (.52). We also dropped ADD8 to compare direct questioning with indirect questioning. After conducting a second CFA, the various overall fit indices of the revised model also suggested a good fit of the model to the data.

The reliability of each construct was assessed with Cronbach’s alpha, composite reliability (CR), and average variance extracted (AVE) (Hair et al., 2009). The literature suggests the cut-off values for Cronbach’s alpha, CR, and AVE as .70, .70, and .50, respectively (Hair et al., 2009; Nunnally & Bernstein, 1994). All of these values were satisfactory in our study (see Table 5).

Table 5. Descriptive Statistics, Validity, and Reliability

<table><tr><td rowspan="2">Context</td><td rowspan="2">Items</td><td rowspan="2">Mean</td><td rowspan="2">S.D.</td><td colspan="4">Initial model</td><td colspan="4">Revised model</td></tr><tr><td>Factor loading</td><td>Alpha</td><td>CR</td><td>AVE</td><td>Factor loading</td><td>Alpha</td><td>CR</td><td>AVE</td></tr><tr><td rowspan="24">SNS addiction</td><td>ADDi1</td><td>4.159</td><td>1.761</td><td>.904</td><td rowspan="9">.940</td><td rowspan="9">.942</td><td rowspan="9">.647</td><td>.905</td><td rowspan="9">.947</td><td rowspan="9">.947</td><td rowspan="9">.693</td></tr><tr><td>ADDi2</td><td>4.175</td><td>1.664</td><td>.871</td><td>.871</td></tr><tr><td>ADDi3</td><td>4.294</td><td>1.707</td><td>.846</td><td>.848</td></tr><tr><td>ADDi4</td><td>3.745</td><td>1.582</td><td>.773</td><td>.771</td></tr><tr><td>ADDi5</td><td>4.004</td><td>1.589</td><td>.745</td><td>.740</td></tr><tr><td>ADDi6</td><td>3.900</td><td>1.596</td><td>.804</td><td>.802</td></tr><tr><td>ADDi7</td><td>4.331</td><td>1.694</td><td>.842</td><td>.844</td></tr><tr><td>ADDi8</td><td>3.235</td><td>1.616</td><td>.522</td><td>Deleted</td></tr><tr><td>ADDi9</td><td>4.088</td><td>1.659</td><td>.866</td><td>.868</td></tr><tr><td>ADD1</td><td>2.681</td><td>1.774</td><td>.889</td><td rowspan="9">.953</td><td rowspan="9">.953</td><td rowspan="9">.693</td><td>.888</td><td rowspan="9">.947</td><td rowspan="9">.947</td><td rowspan="9">.692</td></tr><tr><td>ADD2</td><td>2.594</td><td>1.716</td><td>.875</td><td>.881</td></tr><tr><td>ADD3</td><td>3.024</td><td>1.897</td><td>.825</td><td>.824</td></tr><tr><td>ADD4</td><td>2.247</td><td>1.568</td><td>.798</td><td>.792</td></tr><tr><td>ADD5</td><td>2.625</td><td>1.754</td><td>.835</td><td>.829</td></tr><tr><td>ADD6</td><td>2.259</td><td>1.603</td><td>.813</td><td>.819</td></tr><tr><td>ADD7</td><td>2.494</td><td>1.721</td><td>.781</td><td>.785</td></tr><tr><td>ADD8</td><td>2.693</td><td>1.867</td><td>.833</td><td>Deleted</td></tr><tr><td>ADD9</td><td>2.657</td><td>1.805</td><td>.835</td><td>.829</td></tr><tr><td>PU1</td><td>3.422</td><td>1.639</td><td>.939</td><td rowspan="3">.959</td><td rowspan="3">.959</td><td rowspan="3">.887</td><td rowspan="18" colspan="4"></td></tr><tr><td>PU2</td><td>3.319</td><td>1.740</td><td>.932</td></tr><tr><td>PU3</td><td>3.355</td><td>1.663</td><td>.954</td></tr><tr><td>PE1</td><td>5.012</td><td>1.674</td><td>.923</td><td rowspan="3">.936</td><td rowspan="3">.937</td><td rowspan="3">.833</td></tr><tr><td>PE2</td><td>4.809</td><td>1.724</td><td>.870</td></tr><tr><td>PE3</td><td>5.016</td><td>1.647</td><td>.944</td></tr><tr><td rowspan="12">Digital piracy</td><td>DPIi1</td><td>4.650</td><td>1.576</td><td>.867</td><td rowspan="3">.894</td><td rowspan="3">.896</td><td rowspan="3">.742</td></tr><tr><td>DPIi2</td><td>4.440</td><td>1.614</td><td>.898</td></tr><tr><td>DPIi3</td><td>3.980</td><td>1.699</td><td>.817</td></tr><tr><td>DPI1</td><td>2.530</td><td>1.918</td><td>.923</td><td rowspan="3">.953</td><td rowspan="3">.954</td><td rowspan="3">.873</td></tr><tr><td>DPI2</td><td>2.450</td><td>1.907</td><td>.966</td></tr><tr><td>DPI3</td><td>2.230</td><td>1.817</td><td>.914</td></tr><tr><td>SEV1</td><td>4.770</td><td>1.841</td><td>.928</td><td rowspan="3">.958</td><td rowspan="3">.958</td><td rowspan="3">.884</td></tr><tr><td>SEV2</td><td>5.010</td><td>1.719</td><td>.948</td></tr><tr><td>SEV3</td><td>4.960</td><td>1.765</td><td>.945</td></tr><tr><td>SUS1</td><td>5.160</td><td>1.768</td><td>.845</td><td rowspan="3">.775</td><td rowspan="3">.788</td><td rowspan="3">.556</td></tr><tr><td>SUS2</td><td>4.560</td><td>1.940</td><td>.727</td></tr><tr><td>SUS3</td><td>5.680</td><td>1.455</td><td>.653</td></tr></table>

Table 6. Correlation Matrix

<table><tr><td colspan="2">SNS addiction</td><td>#</td><td>Mean</td><td>S.D.</td><td>ADDi</td><td>ADD</td><td>PU</td><td>PE</td><td>MC</td><td>SDE</td><td>IM</td><td>BIDR</td><td>Gen-der</td><td>Age</td><td>EDU</td><td>EMP</td><td>MAR</td></tr><tr><td colspan="2">ADDi</td><td>8</td><td>4.087</td><td>1.415</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">ADD</td><td>8</td><td>2.573</td><td>1.479</td><td>.491</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">PU</td><td>3</td><td>3.365</td><td>1.616</td><td>-.042</td><td>.266</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">PE</td><td>3</td><td>4.946</td><td>1.584</td><td>.347</td><td>.160</td><td>.284</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">SD scales</td><td>MC</td><td>13</td><td>6.350</td><td>3.034</td><td>-.205</td><td>-.189</td><td>.045</td><td>-.092</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SDE</td><td>8</td><td>2.150</td><td>1.956</td><td>-.156</td><td>-.297</td><td>-.039</td><td>.038</td><td>.443</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IM</td><td>8</td><td>2.880</td><td>2.190</td><td>-.195</td><td>-.342</td><td>-.101</td><td>-.055</td><td>.572</td><td>.596</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BIDR</td><td>16</td><td>5.030</td><td>3.706</td><td>-.198</td><td>-.359</td><td>-.080</td><td>-.012</td><td>.572</td><td>.880</td><td>.906</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">Controls</td><td>Gender</td><td>1</td><td>1.558</td><td>.498</td><td>.002</td><td>-.081</td><td>-.093</td><td>.028</td><td>-.132</td><td>-.046</td><td>.038</td><td>-.002</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Age</td><td>1</td><td>41.634</td><td>11.913</td><td>-.036</td><td>-.100</td><td>-.013</td><td>-.146</td><td>.263</td><td>.197</td><td>.293</td><td>.277</td><td>-.204</td><td>1</td><td></td><td></td><td></td></tr><tr><td>EDU</td><td>1</td><td>3.582</td><td>1.022</td><td>.021</td><td>.065</td><td>.169</td><td>.091</td><td>.000</td><td>-.014</td><td>-.114</td><td>-.075</td><td>-.129</td><td>-.191</td><td>1</td><td></td><td></td></tr><tr><td>EMP</td><td>1</td><td>1.685</td><td>.465</td><td>.012</td><td>.094</td><td>.120</td><td>.106</td><td>-.014</td><td>.000</td><td>-.132</td><td>-.078</td><td>-.016</td><td>-.185</td><td>.244</td><td>1</td><td></td></tr><tr><td>MAR</td><td>1</td><td>1.757</td><td>.430</td><td>.011</td><td>-.004</td><td>.016</td><td>.043</td><td>.042</td><td>.058</td><td>.036</td><td>.052</td><td>.038</td><td>-.019</td><td>.205</td><td>.116</td><td>1</td></tr><tr><td colspan="2">Digital piracy</td><td>#</td><td>Mean</td><td>S.D.</td><td>DPIi</td><td>DPI</td><td>SEV</td><td>SUS</td><td>MC</td><td>SDE</td><td>IM</td><td>BIDR</td><td>Gen-der</td><td>Age</td><td>EDU</td><td>EMP</td><td>MAR</td></tr><tr><td colspan="2">DPIi</td><td>3</td><td>4.357</td><td>1.481</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">DPI</td><td>3</td><td>2.404</td><td>1.799</td><td>.339</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">SEV</td><td>3</td><td>4.194</td><td>1.705</td><td>-.019</td><td>-.337</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">SUS</td><td>3</td><td>5.135</td><td>1.440</td><td>.022</td><td>-.342</td><td>.676</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">SD scales</td><td>MC</td><td>13</td><td>6.190</td><td>2.838</td><td>-.138</td><td>-.180</td><td>.152</td><td>.086</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SDE</td><td>8</td><td>2.240</td><td>1.995</td><td>-.039</td><td>-.217</td><td>.246</td><td>.296</td><td>.332</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IM</td><td>8</td><td>2.610</td><td>2.151</td><td>-.040</td><td>-.358</td><td>.253</td><td>.343</td><td>.485</td><td>.532</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BIDR</td><td>16</td><td>4.850</td><td>3.630</td><td>-.045</td><td>-.331</td><td>.285</td><td>.366</td><td>.470</td><td>.865</td><td>.885</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">Controls</td><td>Gender</td><td>1</td><td>1.510</td><td>.501</td><td>-.045</td><td>-.048</td><td>-.067</td><td>-.040</td><td>-.043</td><td>-.147</td><td>-.015</td><td>-.090</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Age</td><td>1</td><td>42.300</td><td>11.831</td><td>-.310</td><td>-.349</td><td>.171</td><td>.179</td><td>.148</td><td>.215</td><td>.220</td><td>.249</td><td>-.151</td><td>1</td><td></td><td></td><td></td></tr><tr><td>EDU</td><td>1</td><td>3.690</td><td>1.037</td><td>.101</td><td>.127</td><td>-.166</td><td>-.172</td><td>-.058</td><td>.018</td><td>-.132</td><td>-.068</td><td>-.099</td><td>-.102</td><td>1</td><td></td><td></td></tr><tr><td>EMP</td><td>1</td><td>1.730</td><td>.442</td><td>.054</td><td>.106</td><td>-.018</td><td>-.054</td><td>-.024</td><td>-.052</td><td>-.110</td><td>-.094</td><td>-.002</td><td>-.244</td><td>.258</td><td>1</td><td></td></tr><tr><td>MAR</td><td>1</td><td>1.710</td><td>.455</td><td>-.046</td><td>.010</td><td>-.029</td><td>-.070</td><td>-.023</td><td>.029</td><td>-.028</td><td>.000</td><td>-.057</td><td>.060</td><td>.010</td><td>-.022</td><td>1</td></tr><tr><td colspan="18">Notes:• ADDi: indirect questioning of SNS addiction; ADD: direct questioning of SNS addiction; PU: perceived usefulness; PE: perceived ease of use; DPIi: indirect questioning of digital piracy intention; DPI: direct questioning of digital piracy intention; SEV: perceived threat severity; SUS: perceived threat susceptibility.• Gender: (1) Male, (2) Female; EMP (employment status): (1) No, (2) Yes; MAR (marital status): (1) No, (2) Yes; EDU (education).• Because BIDR is a combination of SDE and IM, high correlations between BIDR and its subscales are expected. Also, our results are consistent with prior research. For example, Randall and Fernandes (1991) showed that BIDR is highly correlated with SDE (.76) and IM (.88).</td></tr><tr><td></td><td colspan="17">Used for mean comparison between direct and indirect questioning to identify SD bias (see Table 7).</td></tr><tr><td></td><td colspan="17">Used for correlation comparison between direct and indirect questioning to examine the performance of SD scales (see Table 8).</td></tr></table>

Discriminant validity was assessed by comparing the square root of AVE for each construct with the correlations it had with other constructs (Gefen & Straub, 2005). The square root of the AVE for each construct was found to exceed its correlations with other constructs, further demonstrating the discriminant validity of the latent constructs in SNS addiction and in digital piracy (see Table 6).

The reliability of the four SD scales was examined by using Cronbach’s alpha. It is important to note that (short forms of) the MC scale and the BIDR sometimes have low reliability with an alpha < .70 (Cronbach, 1951). Thus, it is not uncommon for the internal consistency of the scales to be less than .70 (Beretvas, Meyers, & Leite, 2002; Hart et al., 2015; Li & Bagger, 2007). Our results from the Cronbach’s alpha (MC: .73 and .68; SDE: .70 and .70; IM: .74 and .74; BIDR: .82, and .81 in SNS addiction and digital piracy, respectively) were near or more than .70, suggesting acceptable internal consistency of the four SD scales.

Table 7. Mean Comparison Between Direct and Indirect Questioning

<table><tr><td rowspan="2">Variable</td><td colspan="2">Direct questioning</td><td colspan="2">Indirect questioning</td><td colspan="2">Difference</td><td colspan="2">Paired t-test</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td><td>t</td><td>p-value</td></tr><tr><td>SNS Addiction</td><td>2.573</td><td>1.479</td><td>4.087</td><td>1.415</td><td>1.514</td><td>1.463</td><td>16.400</td><td>.000</td></tr><tr><td>Digital Piracy Intention</td><td>2.404</td><td>1.799</td><td>4.358</td><td>1.481</td><td>1.954</td><td>1.928</td><td>16.808</td><td>.000</td></tr></table>

Table 8. Correlation Comparisons Between Direct and Indirect Questioning

<table><tr><td rowspan="3">Context</td><td rowspan="2" colspan="3">Variables</td><td colspan="3">Correlations for</td><td rowspan="2" colspan="2">Difference test</td></tr><tr><td colspan="2">Comparison</td><td>Unshared variable</td></tr><tr><td>j</td><td>k</td><td>h</td><td> $r_{jk}$ </td><td> $r_{jh}$ </td><td> $r_{kh}$ </td><td>Z score</td><td>p-value</td></tr><tr><td rowspan="4">SNS Addiction (N=251)</td><td>MC</td><td rowspan="4">ADD</td><td rowspan="4">ADDi</td><td>-.189</td><td>-.205</td><td rowspan="4">.491</td><td>.256</td><td>.399</td></tr><tr><td>SDE</td><td>-.297</td><td>-.156</td><td>-2.285</td><td>.011</td></tr><tr><td>IM</td><td>-.342</td><td>-.195</td><td>-2.417</td><td>.008</td></tr><tr><td>BIDR</td><td>-.359</td><td>-.198</td><td>-2.660</td><td>.004</td></tr><tr><td rowspan="4">Digital Piracy (N=275)</td><td>MC</td><td rowspan="4">DPI</td><td rowspan="4">DPIi</td><td>-.180</td><td>-.138</td><td rowspan="4">.339</td><td>-.613</td><td>.270</td></tr><tr><td>SDE</td><td>-.217</td><td>-.039</td><td>-2.581</td><td>.004</td></tr><tr><td>IM</td><td>-.358</td><td>-.040</td><td>-4.776</td><td>.000</td></tr><tr><td>BIDR</td><td>-.331</td><td>-.045</td><td>-4.267</td><td>.000</td></tr></table>

Notes: j: shared variable; k: direct questioning; h: indirect questioning

## 5.2 Extent of SD Bias

To assess the extent of SD bias, we used a paired t-test to examine the mean difference between direct and indirect questioning. Fisher (1993) noted that indirect questioning is a technique to reduce SD bias on selfreport measures. Our results indicated significant differences between direct and indirect questioning in

SNS addiction $( t = 1 6 . 4 0 , p < . 0 0 1 )$ and digital piracy $( t = 1 6 . 8 1 , p < . 0 0 1 )$ (see Table 7). These results are consistent with those of Fisher (1993), who tested for the difference in a between-subject design. Overall, it is reasonable to conclude that SNS addiction and digital piracy are sensitive topics and that the respondents tended to underreport their actual behavior.<sup>3</sup>

## 5.3 Performance of Alternative SD scales

To assess the efficacy of alternative SD scales, we examined how these scales correlated with (1) direct and indirect questioning, and (2) sensitive factors such as SNS addiction (ADD) and digital piracy intention (DPI). Drawing upon Steiger (1980), we used the methodology of Lee and Preacher (2013) to test for the differences between two dependent correlations with one common variable in a within-subject design.

First, we examined the performance of SD scales in terms of direct and indirect questioning. As mentioned earlier, indirect questioning is less susceptible to SD bias than direct questioning (Fisher, 1993). Thus, the correlation between SD scales and direct questioning is expected to exceed the correlation between SD scales and indirect questioning. However, as shown in Table 8, the correlation between the MC scale and direct questioning does not differ significantly from the correlation between the MC scale and indirect questioning. Nevertheless, the SDE scale, the IM scale, and the BIDR show significant differences. These results imply that at least in these contexts, the MC scale is less effective than the alternatives in detecting SD bias.

Second, we compared the SD scales in terms of their correlations with sensitive factors such as ADD and DPI (see Table 9). We found that the MC’s correlations with the sensitive variables (i.e., ADD and DPI) (r<sub>ADD.MC</sub> = -.189; r<sub>DPI.MC</sub> = -.180) were significantly less than the correlations between the sensitive variables and the other SD scales. These results suggest that the MC scale is less sensitive than the alternatives in detecting SD bias.

Table 9. Correlation Comparisons Between SD Scales

<table><tr><td rowspan="3">Context</td><td rowspan="2" colspan="3">Variables</td><td colspan="3">Correlations for</td><td rowspan="2" colspan="2">Difference test</td></tr><tr><td colspan="2">Comparison</td><td>Unshared variables</td></tr><tr><td>j</td><td>k</td><td>h</td><td> $r_{jk}$ </td><td> $r_{jh}$ </td><td> $r_{kh}$ </td><td>Z score</td><td>p-value</td></tr><tr><td rowspan="6">SNS Addiction (N=251)</td><td rowspan="6">ADD</td><td rowspan="3">MC</td><td>SDE</td><td rowspan="3">-.189</td><td>-.297</td><td>.443</td><td>1.680</td><td>.046</td></tr><tr><td>IM</td><td>-.342</td><td>.572</td><td>2.738</td><td>.003</td></tr><tr><td>BIDR</td><td>-.359</td><td>.572</td><td>3.056</td><td>.001</td></tr><tr><td rowspan="2">SDE</td><td>IM</td><td rowspan="2">-.297</td><td>-.342</td><td>.596</td><td>.823</td><td>.205</td></tr><tr><td>BIDR</td><td>-.359</td><td>.880</td><td>2.121</td><td>.017</td></tr><tr><td>IM</td><td>BIDR</td><td>-.342</td><td>-.359</td><td>.906</td><td>.662</td><td>.254</td></tr><tr><td rowspan="6">Digital Piracy (N=275)</td><td rowspan="6">DPI</td><td rowspan="3">MC</td><td>SDE</td><td rowspan="3">-.180</td><td>-.217</td><td>.332</td><td>.543</td><td>.294</td></tr><tr><td>IM</td><td>-.358</td><td>.485</td><td>3.055</td><td>.001</td></tr><tr><td>BIDR</td><td>-.331</td><td>.470</td><td>2.538</td><td>.006</td></tr><tr><td rowspan="2">SDE</td><td>IM</td><td rowspan="2">-.217</td><td>-.358</td><td>.532</td><td>2.548</td><td>.005</td></tr><tr><td>BIDR</td><td>-.331</td><td>.865</td><td>3.790</td><td>.000</td></tr><tr><td>IM</td><td>BIDR</td><td>-.358</td><td>-.331</td><td>.885</td><td>-.993</td><td>.160</td></tr><tr><td colspan="9">Note: j: shared variable</td></tr></table>

Then, we compared the SDE scale, the IM scale, and the BIDR. Our results show that overall, the IM scale and the BIDR are more sensitive than the SDE scale, but the IM scale and the BIDR are not statistically different. Therefore, taking into account both sensitivity and convenience (i.e., number of items), the IM scale would be a more practical choice to determine SD bias than any of the others.

## 5.4 Causal Relationships After Controlling for SD Bias

Covariance technique is one of the methods used to control the influence of SD bias (Paulhus, 1991). Covariance technique includes an SD scale along with measures of research variables. Then SD bias is partialled out of the correlations between research variables to control for spurious correlations. In our study, this covariance technique relies on partial correlations after explicitly controlling or adjusting for any potentially inflated correlations because of SD bias. This approach has been used in other studies of method bias such as common method variance (e.g., Malhotra, Kim, & Patil, 2006) and the halo effect (e.g., Mossholder & Giles, 1983).

We first examined the differences between the original correlations and the partial correlations calculated differently according to the four SD scales (see Table 10). To formally compare original and partial correlations, we conducted a chi-square difference test (Bollen, 1989; Malhotra et al., 2006). Specifically, an original correlation value was replaced with its partial correlation value and examined as to whether the substitution significantly worsened fit $( \Delta \chi ^ { 2 } \left( 1 \right) > 3 . 8 4 ,$ p < .05). No original correlations differed significantly from their partial correlation counterparts, suggesting that SD bias is not substantial. Despite the results of the chi-square difference test, we found few differences in correlations were shown in SNS addiction (i.e., a maximum 12.7% increase), whereas some meaningful differences were found in digital piracy (i.e., a maximum 26.7% decrease).

Table 10: Differences Between Original and Partial Correlations

<table><tr><td rowspan="2">Context</td><td rowspan="2">Factor correlation</td><td rowspan="2">Original correlation</td><td colspan="8">Partial correlation</td></tr><tr><td>MC</td><td> $\Delta r$ </td><td>SDE</td><td> $\Delta r$ </td><td>IM</td><td> $\Delta r$ </td><td>BIDR</td><td> $\Delta r$ </td></tr><tr><td rowspan="3">SNS addiction</td><td>r(ADD, PU)</td><td>.267***</td><td>.282***</td><td>.015</td><td>.267***</td><td>.000</td><td>.248***</td><td>-.019</td><td>.255***</td><td>-.012</td></tr><tr><td>r(ADD, PE)</td><td>.157***</td><td>.142*</td><td>-.015</td><td>.177**</td><td>.020</td><td>.147*</td><td>-.010</td><td>.164*</td><td>.007</td></tr><tr><td>r(PU, PE)</td><td>.283***</td><td>.289***</td><td>.006</td><td>.285***</td><td>.002</td><td>.280***</td><td>-.003</td><td>.283***</td><td>.000</td></tr><tr><td rowspan="3">Digital piracy</td><td>r(SEV, DPI)</td><td>-.335***</td><td>-.317***</td><td>-.018</td><td>-.298***</td><td>-.037</td><td>-.271***</td><td>-.064</td><td>-.266***</td><td>-.069</td></tr><tr><td>r(SUS, DPI)</td><td>-.342***</td><td>-.333***</td><td>-.009</td><td>-.299***</td><td>-.043</td><td>-.251***</td><td>-.091</td><td>-.253***</td><td>-.089</td></tr><tr><td>r(SEV, SUS)</td><td>.680***</td><td>.675***</td><td>-.005</td><td>.658***</td><td>-.022</td><td>.654***</td><td>-.026</td><td>.648***</td><td>-.032</td></tr><tr><td colspan="11">Notes:• *** p &lt; .001; ** p &lt; .01; * p &lt; .05•  $\Delta r$ : Correlation difference• Indirect questioning and control variables are not included here.</td></tr></table>

This contextual difference seems to be because in the context of SNS addiction only one factor (i.e., addiction) was sensitive to SD bias, but in the context of digital privacy, several factors were associated simultaneously with SD bias. Specifically, the mean of the addiction factor changed because of SD bias, but its correlations with other constructs such as PU and PE remained relatively unchanged because the SD bias rarely affected PU and PE. However, in the case of digital privacy, SD bias had a wide-ranging effect on all of the research variables (i.e., DPI, SEV, and SUS), and thus their correlations changed considerably.

Second, we conducted structural equation modeling by using original and partial correlations in two contexts.

Uncorrected estimates of the SNS addiction model (see Table 11) showed that ADD had significant effects on PU $( \beta = . 2 7 , p < . 0 0 1 )$ and PE $( \beta = . 1 6 , p < . 0 5 )$ Addiction explained 7.1% of the variance in PU and 2.5% in PE. Bias-adjusted estimates showed similar results. We then examined the $\mathbf { R } ^ { 2 }$ changes between uncorrected and adjusted models. Table 11 shows that the R<sup>2</sup> changes were very small (e.g., maximum ΔR<sup>2</sup> is -1.0%). Subsequently, we added control variables to see if the results without control variables remained consistent with the results with control variables. As shown in Table 11, the results were consistent, and the R<sup>2</sup> differences were small as well (e.g., the maximum ΔR<sup>2</sup> is 1.1%). Our results suggest that SD bias does not seriously distort our inferences in SNS addiction.

Table 11: SEM Results for SNS Addiction

<table><tr><td rowspan="2">IV</td><td rowspan="2">DV</td><td colspan="5">Models without controls: A</td><td colspan="5">Models with controls: B</td></tr><tr><td>(A1)</td><td>(A2)MC</td><td>(A3)SDE</td><td>(A4)IM</td><td>(A5)BIDR</td><td>(B1)</td><td>(B2)MC</td><td>(B3)SDE</td><td>(B4)IM</td><td>(B5)BIDR</td></tr><tr><td colspan="2"> $R^2$ </td><td>7.1%</td><td>7.9%</td><td>7.1%</td><td>6.1%</td><td>6.5%</td><td>10.2%</td><td>10.7%</td><td>10.1%</td><td>9.2%</td><td>9.6%</td></tr><tr><td colspan="2">Change in  $R^2$ </td><td>-</td><td>.8%</td><td>0%</td><td>-1.0%</td><td>-.6%</td><td></td><td>.5%</td><td>-.1%</td><td>-1.0%</td><td>-.6%</td></tr><tr><td>ADD</td><td rowspan="6">PU</td><td>.267***</td><td>.282***</td><td>.267***</td><td>.248</td><td>.255***</td><td>.250***</td><td>.261***</td><td>.246***</td><td>.235***</td><td>.238***</td></tr><tr><td>Gender</td><td rowspan="5" colspan="5"></td><td>-.044</td><td>-.035</td><td>-.043</td><td>-.044</td><td>-.044</td></tr><tr><td>Age</td><td>.042</td><td>.020</td><td>.036</td><td>.040</td><td>.036</td></tr><tr><td>EDU</td><td>.137</td><td>.134*</td><td>.137*</td><td>.137*</td><td>.137*</td></tr><tr><td>EMP</td><td>.071</td><td>.069</td><td>.070</td><td>.071</td><td>.072</td></tr><tr><td>MAR</td><td>-.016</td><td>-.020</td><td>-.018</td><td>-.017</td><td>-.018</td></tr><tr><td colspan="2"> $R^2$ </td><td>2.5%</td><td>2.0%</td><td>3.1%</td><td>2.2%</td><td>2.7%</td><td>4.9%</td><td>4.2%</td><td>6.0%</td><td>4.8%</td><td>5.6%</td></tr><tr><td colspan="2">Change in  $R^2$ </td><td>-</td><td>-.5%</td><td>.6%</td><td>-.5%</td><td>.2%</td><td>-</td><td>-.7%</td><td>1.1%</td><td>-.1%</td><td>.7%</td></tr><tr><td>ADD</td><td rowspan="6">PE</td><td>.157*</td><td>.142*</td><td>.177**</td><td>.147*</td><td>.164*</td><td>.139*</td><td>.129†</td><td>.165*</td><td>.143*</td><td>.158*</td></tr><tr><td>Gender</td><td rowspan="5" colspan="5"></td><td>.023</td><td>.019</td><td>.027</td><td>.021</td><td>.022</td></tr><tr><td>Age</td><td>-.106</td><td>-.094</td><td>-.124†</td><td>-.113†</td><td>-.124†</td></tr><tr><td>EDU</td><td>.042</td><td>.043</td><td>.040</td><td>.043</td><td>.043</td></tr><tr><td>EMP</td><td>.061</td><td>.062</td><td>.055</td><td>.062</td><td>.061</td></tr><tr><td>MAR</td><td>.024</td><td>.026</td><td>.018</td><td>.022</td><td>.019</td></tr><tr><td colspan="12">Goodness of fit indices</td></tr><tr><td> $\chi^2$ </td><td rowspan="2">Good Fits</td><td>198.45</td><td>192.06</td><td>198.81</td><td>194.59</td><td>195.89</td><td>285.25</td><td>280.04</td><td>286.67</td><td>284.28</td><td>285.24</td></tr><tr><td>DF</td><td>74</td><td>74</td><td>74</td><td>74</td><td>74</td><td>129</td><td>129</td><td>129</td><td>129</td><td>129</td></tr><tr><td> $\chi^2/DF$ </td><td>&lt; 3.00</td><td>2.682</td><td>2.595</td><td>2.687</td><td>2.630</td><td>2.647</td><td>2.211</td><td>2.171</td><td>2.222</td><td>2.204</td><td>2.211</td></tr><tr><td>TLI</td><td>&gt;.90</td><td>.954</td><td>.955</td><td>.952</td><td>.953</td><td>.952</td><td>.939</td><td>.940</td><td>.936</td><td>.936</td><td>.936</td></tr><tr><td>CFI</td><td>&gt;.90</td><td>.962</td><td>.964</td><td>.961</td><td>.962</td><td>.961</td><td>.954</td><td>.955</td><td>.952</td><td>.952</td><td>.952</td></tr><tr><td>GFI</td><td>&gt;.90</td><td>.895</td><td>.899</td><td>.894</td><td>.896</td><td>.895</td><td>.892</td><td>.894</td><td>.891</td><td>.892</td><td>.891</td></tr><tr><td>AGFI</td><td>&gt;.80</td><td>.851</td><td>.856</td><td>.850</td><td>.853</td><td>.852</td><td>.841</td><td>.844</td><td>.839</td><td>.840</td><td>.840</td></tr><tr><td>SRMR</td><td>&lt; .08</td><td>.055</td><td>.053</td><td>.055</td><td>.054</td><td>.055</td><td>.045</td><td>.044</td><td>.046</td><td>.046</td><td>.046</td></tr><tr><td>RMSEA</td><td>&lt; .08</td><td>.082</td><td>.080</td><td>.082</td><td>.081</td><td>.081</td><td>.070</td><td>.068</td><td>.070</td><td>.069</td><td>.070</td></tr><tr><td colspan="12">Notes: *** p &lt; .001; ** p &lt; .01; * p &lt; .05; † p &lt; .10 Models (A1) and (B1): Uncorrected estimates; Models (A2)-(A5) and (B2)-(B5): Adjusted estimates using partial correlations to control for SD scales.</td></tr></table>

Meanwhile, uncorrected estimates in digital piracy (see Table 12) indicate that SEV $( \beta = . 1 9 , p < . 0 5 )$ and SUS $( \beta = . 2 1 , p < . 0 5 )$ significantly influenced DPI. In this case, SEV and SUS jointly explained 13.7% of the variance in DPI. However, bias-adjusted estimates show different results in terms of statistical significance. For example, in the case of the IMadjusted model, SUS did not exert a significant effect on DPI $( \beta = . 1 3 , p > . 0 5 )$ . In addition, $\mathbf { R } ^ { 2 }$ changes between uncorrected and adjusted models suggest that the R<sup>2</sup> change was noteworthy (e.g., maximum $\Delta { \sf R } ^ { 2 }$ is -5.5%). As noted earlier, these changes may result from the influence of SD bias on multiple constructs. These results generally imply that although it is not a problem in SNS addiction, SD bias could still lead to an altered interpretation of the phenomena because of the change in statistical significance in digital piracy.

Table 12: SEM Results for Digital Piracy

<table><tr><td rowspan="2">IV</td><td rowspan="2">DV</td><td colspan="5">Models without controls: a</td><td colspan="5">Models with controls: b</td></tr><tr><td>(A1)</td><td>(A2)MC</td><td>(A3)SDE</td><td>(A4)IM</td><td>(A5)BIDR</td><td>(B1)</td><td>(B2)MC</td><td>(B3)SDE</td><td>(B4)IM</td><td>(B5)BIDR</td></tr><tr><td colspan="2"> $R^2$ </td><td>13.7%</td><td>12.6%</td><td>10.7%</td><td>8.3%</td><td>8.2%</td><td>23.0%</td><td>21.2%</td><td>19.8%</td><td>16.4%</td><td>16.6%</td></tr><tr><td colspan="2">Change in  $R^2$ </td><td>-</td><td>-1.1%</td><td>-3.0%</td><td>-5.4%</td><td>-5.5%</td><td>-</td><td>-1.8%</td><td>-3.2%</td><td>-6.6%</td><td>-6.4%</td></tr><tr><td>SEV</td><td rowspan="7">DPI</td><td>-.191*</td><td>-.169†</td><td>-.179*</td><td>-.187*</td><td>-.177*</td><td>-.173*</td><td>-.159†</td><td>-.166*</td><td>-.174*</td><td>-.166*</td></tr><tr><td>SUS</td><td>-.213*</td><td>-.218*</td><td>-.181†</td><td>-.129</td><td>-.138</td><td>-.169†</td><td>-.175†</td><td>-.145</td><td>-.106</td><td>-.112</td></tr><tr><td>Gender</td><td rowspan="5" colspan="5"></td><td>-.108†</td><td>-.103†</td><td>-.118*</td><td>-.112†</td><td>-.123*</td></tr><tr><td>Age</td><td>-.298**</td><td>-.287**</td><td>-.285**</td><td>-.277**</td><td>-.274**</td></tr><tr><td>EDU</td><td>.023</td><td>.021</td><td>.031</td><td>.013</td><td>.027</td></tr><tr><td>EMP</td><td>.015</td><td>.017</td><td>.013</td><td>.005</td><td>.008</td></tr><tr><td>MAR</td><td>.005</td><td>.007</td><td>.008</td><td>.002</td><td>.007</td></tr><tr><td colspan="12">Goodness of fit indices</td></tr><tr><td> $\chi^2$ </td><td rowspan="2">Good Fits</td><td>49.50</td><td>44.76</td><td>49.40</td><td>49.44</td><td>49.02</td><td>93.43</td><td>87.18</td><td>93.37</td><td>94.61</td><td>94.80</td></tr><tr><td>DF</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td><td>54</td><td>54</td><td>54</td><td>54</td><td>54</td></tr><tr><td> $\chi^2/DF$ </td><td>&lt; 3.00</td><td>2.062</td><td>1.865</td><td>2.058</td><td>2.060</td><td>2.043</td><td>1.730</td><td>1.614</td><td>1.729</td><td>1.752</td><td>1.756</td></tr><tr><td>TLI</td><td>&gt;.90</td><td>.983</td><td>.986</td><td>.982</td><td>.981</td><td>.982</td><td>.971</td><td>.975</td><td>.969</td><td>.968</td><td>.967</td></tr><tr><td>CFI</td><td>&gt;.90</td><td>.988</td><td>.990</td><td>.988</td><td>.988</td><td>.988</td><td>.983</td><td>.985</td><td>.982</td><td>.981</td><td>.981</td></tr><tr><td>GFI</td><td>&gt;.90</td><td>.954</td><td>.963</td><td>.959</td><td>.959</td><td>.960</td><td>.952</td><td>.956</td><td>.953</td><td>.952</td><td>.952</td></tr><tr><td>AGFI</td><td>&gt;.80</td><td>.923</td><td>.931</td><td>.924</td><td>.924</td><td>.924</td><td>.908</td><td>.915</td><td>.908</td><td>.907</td><td>.907</td></tr><tr><td>SRMR</td><td>&lt; .08</td><td>.031</td><td>.0299</td><td>.033</td><td>.032</td><td>.0327</td><td>.030</td><td>.028</td><td>.031</td><td>.031</td><td>.032</td></tr><tr><td>RMSEA</td><td>&lt; .08</td><td>.062</td><td>.056</td><td>.062</td><td>.062</td><td>.062</td><td>.052</td><td>.047</td><td>.052</td><td>.052</td><td>.053</td></tr><tr><td colspan="12">Notes:***p &lt; .001; **p &lt; .01; *p &lt; .05; †p &lt; .10Models (A1) and (B1): Uncorrected estimatesModels (A2)-(A5) and (B2)-(B5): Adjusted estimates using partial correlations to control for SD scales</td></tr></table>

## 6 Discussion and Conclusions

This study yields insight into the existence of SD bias and the use of different approaches to measure its presence in IS research. Specifically, we compared the popular MC scale with other techniques for assessing SD bias. In this study, SD bias was examined in two different IS contexts—namely, SNS addiction and digital piracy. Our findings show that unlike the claims made for prior research, SD bias cannot be ignored, especially when evaluated with proper and effective tools. Specifically, we found that, under certain circumstances, SD bias can threaten the validity of IS research. This study is unique because it documents the first empirical evidence of the difference in SD bias across IS contexts and suggests an effective way to test for the presence of SD bias.

## 6.1 Theoretical and Methodological Contributions

The MC scale has been the most popular measurement of SD bias in IS research (e.g., Soror et al., 2015; Turel et al., 2011). Despite its widespread use, it has limitations. First, the items are known to be insensitive and ineffective in differentiating the degrees of SD (Ballard & Crino, 1988; Hart et al., 2015). Second, although the MC scale was designed to capture a unidimensional construct (Crowne & Marlowe, 1964), it has been found to be confounded by a multitude of other factors (Ballard, 1992; Barger, 2002). Consistent with these arguments, our findings suggest that the MC scale is ineffective at distinguishing between indirect questioning and direct questioning. Furthermore, our comparisons between alternative SD scales show that the MC scale performs no better than competing scales in the contexts examined in this study. The discussion mentioned previously leads us to conclude that exclusive reliance on the MC scale as a tool for assessing SD bias could be problematic, and IS researchers are encouraged to use alternative scales in addition to this popular scale.

Interestingly, our study shows that the BIDR, especially the IM scale, outperforms the MC scale in identifying SD bias. Although researchers in other disciplines have used the BIDR extensively (e.g., Randall & Fernandes, 1991; Steenkamp et al., 2010), IS researchers have rarely used it. In general, our findings indicate that, at least in the context of SNS addiction and digital piracy, the IM scale and the BIDR capture SD bias better than either the MC scale or the SDE scale. Because the IM scale is shorter than the BIDR, it would be a more programmatic choice than the BIDR. This study is meaningful in that it introduces a relatively new scale, the BIDR, to IS research and shows the efficacy of the IM scale visà-vis the SDE scale as an effective and efficient measure for capturing SD bias.

We found that SD bias cannot be ignored in IS research and that under certain circumstances, it could be especially threatening. Specifically, our results show distinct contextual patterns: (1) the context of SNS addiction in which only one construct is sensitive to SD bias, and (2) the context of digital piracy in which multiple constructs are sensitive to SD bias. In the case of SNS addiction, we found that the mean of the sensitive construct changes slightly because of SD bias, but its correlations with PU and PE remain relatively unchanged. Thus, in such a simple case, controlling for SD bias hardly affects the results of the model. In contrast, in the case of digital piracy, SD bias affects not only DPI but also SEV and SUS. As a result, the path coefficients and their statistical significance sometimes undergo considerable changes after SD bias is controlled for. More important, after controlling for SD bias, some of these significant paths even became nonsignificant. Thus, researchers should be cautious in interpreting their results, especially when SD bias influences multiple constructs simultaneously. These insights into the contextual differences in SD bias are an important contribution of our study.

## 6.2 Practical Contributions

This research presents different practical implications for managers and professionals. For example, in situations in which managers collect sensitive data while evaluating employees’ fair use of organizational computing resources, managers are encouraged to control for SD bias to ensure they minimize the impression management conveys to respondents. Our research has shown that indirect questioning is a suitable approach to reducing SD bias. By using both direct and indirect questioning, managers can measure the extent of SD bias as presented in this article. To alternatively assess the extent of SD bias, managers can use SD scales. Specifically, SD bias can be inferred from the correlations of SD scales with sensitive factors. Although the MC scale is widely used, our research indicates that the IM scale and the BDIR are superior in identifying SD bias. Because the IM scale contains fewer questions than the BIDR, it has better applicability in practice. Therefore, managers are encouraged to apply the IM scale to measure the tendency of a person to be perceived as socially desirable and to analyze whether the data contains SD bias.

## 6.3 Limitations

Several limitations of this study should be considered in interpreting our results. First, instead of measuring actual behavior, we used indirect questioning as a proxy for actual behavior. The literature suggests that indirect questioning, despite shortcomings, is one of the best approaches for reducing SD bias (Dalal & Hakel, 2016; Fisher & Tellis, 1998). Nevertheless, although indirect questioning is considered a relatively reasonable way to capture true scores, our findings should be interpreted cautiously. Second, although we examined SD bias in multiple contexts, our findings may not generalize to other contexts such as online gaming, online shopping, and organizational use of IT applications. Thus, interpretations of our findings outside the contexts we studied should be made with caution. Third, this study focused on SD bias, which is only one of the many possible common method biases that include, but are not limited to, consistency motif, common scale formats, scale length, and intermixing (Podsakoff, MacKenzie, Lee, & Podsakoff, 2003). In the IS discipline, little is known about the effects of such common method biases and their interaction with SD bias. Thus, our findings related to SD bias need to be reassessed from a fresh viewpoint after taking into account the main and moderating effects (e.g., Carte & Russell, 2003) of these method biases. Fourth, our study focused on false negatives with regard to SD bias (i.e., failing to detect SD bias that actually exists) to identify a better SD scale than the MC scale in detecting SD bias. Although our research examined false negatives in using the MC scale, we cannot rule out the possibility of false positives (i.e., finding incorrect SD bias by detecting what seems to be SD bias but is actually some other form of measurement error). Thus, future research needs to investigate false positives in SD bias.

Digital piracy is rather formal jargon for the illegal downloading or use of books, movies, music, software, etc. We used the keywords directly in the measurement scale in a deliberate attempt to shorten the length of the item. Yet our approach is consistent with that of prior research, which used the rather technical term to measure various aspects of digital piracy (e.g., Al-Rafee & Cronan, 2006). In addition, to avoid any confusion, we provided an operational definition of digital piracy at the very start of the survey questionnaire. Furthermore, we were careful in collecting data only from adults age 18 or older to further reduce the possibility of misinterpreting the meaning of digital piracy. Overall, we believe that our scale conveyed a similar meaning to the respondents; nevertheless, care should be taken in interpreting our results before the research model is reevaluated using items with everyday wording. Finally, the scale of PU in this study was operationalized in a general way not pertinent to a specific goal (e.g., “Using SNS enhances my effectiveness”). This general approach was deliberately chosen because unlike organizational IT use, personal use of online services encompasses all aspects of everyday activities. However, it could have been alternately operationalized in a way specific to certain goals as is typically done in TAM-related research (e.g., “Using SNS enhances my effectiveness at staying in touch with friends”). Thus, caution should be exercised in generalizing our findings until they are thoroughly corroborated with alternative forms of the scales used in the present study.

## 6.4 Further Research Directions

Opportunities for further research are abundant. First, indirect questioning was used as a proxy for true scores. Because indirect questioning may also contain SD bias, researchers should address how well indirect questioning represents true scores in different domains. Second, prior research suggests that different types of studies (e.g., experiments and surveys) are influenced by SD bias for different reasons (Nederhof, 1985). For example, social cues from a researcher in experimental research and item wording in survey research can increase SD bias (Nederhof, 1985). However, little research exists on the variation in the amount of SD bias between different types of research (e.g., experimental vs. quasi-experimental). Future research should compare the degree of SD bias in different types of studies. Third, some researchers argue that a nonsignificant correlation between an SD scale and research variables suggest that the study is free of SD bias (Fisher 1993; Hart et al., 2015; Paulhus, 1991). However, it is still possible that SD bias is still present for a small group of people rather than the majority. In other words, existence of SD bias can depend on the proportion of subgroups (Steenkamp et al., 2010). Thus, future research should expand the search for SD bias by examining each of the subsamples separately. Fourth, prior research has treated SD as a source of SD bias, paying little attention to the difference between SD and SD bias (Hart et al. 2015; Nederhof, 1985; Podsakoff et al. 2003; Randall & Fernandes 1991). However, people with high SD may provide their responses based on their true socially desirable beliefs/behavior. In this case, the high correlations between SD scales and true response scores do not suggest any SD bias. Thus, future research needs to develop SD scales which can distinguish between true socially desirable beliefs/behavior and SD bias. Finally, although the MC scale is shown in this study as less sensitive than the BIDR in detecting SD bias, the MC scale could perform better if it were specified as a multidimensional factor. Recent research indicates that the MC scale is better represented as a multidimensional factor (Barger, 2002; Leite & Beretvas, 2005; Loo & Lowen, 2004), and thus one of these SD factors could be more sensitive to the BIDR in general and to the IM in specific. This study did not treat SD as a multidimensional construct because there is little agreement on its specific dimensionality—i.e., whether it is a two-, three-, or even four-factor structure (Crowne & Marlowe, 1960; Paulhus, 1984; Paulhus & Reid, 1991). But researchers are encouraged to examine the multidimensional nature of SD and the performance of each subdimension in terms of detecting SD bias.

## 6.5 Concluding Remarks

Despite the potential risks related to SD bias, IS researchers have only recently attempted to assess or control for it. As a result, the IS community has not reached a consensus on the techniques to assess and control for the extent of SD bias. To address the state of uncertainty this engenders, we systematically examined SD bias in the contexts of SNS addiction and digital piracy. Our results suggest that despite the popularity of the MC scale in IS research, the IM scale would be a better option. Our study also suggests that under certain circumstances SD bias could be a threat to the validity of research. As IS research matures, it continues to explore the uncharted and uncertain territories in which SD bias would most likely be problematic (e.g., online gambling, online gaming, and virtual reality). We hope that this study will provide helpful insight into the nature of SD bias in both existing and newly emerging areas of IS research.

## Acknowledgments

The authors would like to thank Professor Traci Carte (senior editor) for her valuable advice on improving the manuscript. We are also deeply appreciative of the high-quality feedback from the three reviewers whose insights helped many aspects of our work. The authors thank J. Stanford Fisher for his editorial help.

## References

Allbutt, J., Ling, J., Rowley, M., & Shafiullah, M. (2011). Vividness of visual imagery and social desirable responding: Correlations of the vividness of visual imagery questionnaire with the balanced inventory of desirable responding and the Marlowe-Crowne scale. Behavioral Research Methods, 43, 791-799.

Al-Natour, S., Benbasat, I., & Cenfetelli, R. T. (2006). The role of design characteristics in shaping perceptions of similarity: The case of online shopping assistants. Journal of the Association for Information Systems, 7(12), 821-861.

Al-Rafee, S., & Cronan, T. P. (2006). Digital piracy: Factors that influence attitude toward behavior, Journal of Business Ethics, 63(3), 237-259.

Arnold, H. J., Feldman, D. C., & Purbhoo, M. (1985). The role of social-desirability response bias in turnover research. Academy of Management Journal, 28(4), 955-966.

Bagozzi, R. P. (2011). Measurement and meaning in information systems and organizational research: Methodological and philosophical foundations. MIS Quarterly, 35(2), 261-292.

Ballard, R. (1992). Short forms of the Marlowe-Crowne social desirability scale. Psychological Reports, 71, 1155-1160.

Ballard, R., & Crino, M. D. (1988). Social desirability response bias and the Marlowe-Crowne social desirability scale. Psychological Reports, 63, 227-237.

Bansal, G., Zahedi, F. M., & Gefen, D. (2015). The role of privacy assurance mechanisms in building trust and the moderating role of privacy concern. European Journal of Information Systems, 24(6), 624-644.

Barger, S. D. (2002). The Marlowe-Crowne affair: Short forms, psychometric structure, and social desirability. Journal of Personality Assessment, 79(2), 286-305.

Benlian, A., Koufaris, M., & Hess, T. (2011). Service quality in software-as-a-service: Developing the SaaS-Qual measure and examining its role in usage continuance. Journal of Management Information Systems, 28(3), 85-126.

Beretvas, S. N., Meyers, J. L., & Leite, W. L. (2002). A reliability generalization study of the Marlowe-Crowne social desirability scale. Educational and Psychological Measurement, 62(4), 570-589.

Blake, B. F., Valdiserri, J., Neuendorf, K. A., & Nemeth, J. (2006). Validity of the SDS-17 measure of socially desirability in the American context. Personality and Individual Differences, 40, 1625-1636.

Bollen, K. A. (1989). Structural equation modeling with latent variables. New York, NY: Wiley

Brown, S. A. Venkatesh, V., & Goyal, S. (2014). Expectation confirmation in information systems research: A test of six competing models. MIS Quarterly, 38(3), 729-756.

Byun, S., Ruffini, C., Mills, J. E., Douglas, A. C., Niang, M., Stepchenkova, S., Lee, S. K., Loutfi, J., Lee, J. K., Atallah, M., & Blanton, M. (2009). Internet addiction: Metasynthesis of 1996-2006 quantitative research. Cyberpsychology & Behavior, 12(2), 203-207.

Carte, T. A., & Russell, C. J. (2003). In pursuit of moderation: Nine common errors and their solutions. MIS Quarterly, 27(3), 479-501.

Chan, R. Y., & Lai, J. W. (2011). Does ethical ideology affect software piracy attitude and behaviour? An empirical investigation of computer users in China. European Journal of Information Systems, 20(6), 659-673.

Charlton, J. P. (2002). A factor-analytic investigation of computer “addiction” and engagement. British Psychological Society, 93(3), 329-344.

Chin, W. W., Gopal, A., & Salisbury, W. D. (1997). Advancing the theory of adaptive structuration: The development of a scale to measure faithfulness of appropriation. Information Systems Research, 8(4), 342-367.

Chin, W. W., Thatcher, J. B., Wright, R. T., & Steel, D. (2013). Controlling for common method variance in PLS analysis: The measured latent marker variable approach. In H. Abdi, W. W. Chin, V. Esposito Vinzi, G. Russolillo, & L. Trinchera (Eds.), New perspectives in partial least squares and related methods (pp. 231- 239). New York, NY: Springer

Cohen, J. R., Pant, L. W., Sharp, D. J., & Holder-Webb, L. (2007). The effect of perceived fairness on opportunistic behaviour. Contemporary Accounting Research, 22(4), 1119-1138.

Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. Psychometrika, 16(8), 297-334.

Crowne, D. P., & Marlowe, D. (1960). A new scale of social desirability independent of psychopathology. Journal of Consulting Psychology, 24(4), 349-354.

Crowne, D. P., & Marlowe, D. (1964). The approval motive. New York, NY: Wiley.

Dalal, D. K., & Hakel, M. D. (2016). Experimental comparisons of methods for reducing deliberate distortions to self-report measures of sensitive constructs. Organizational Research Methods, 19(3), 475-505.

D’Arcy, J., Herath, T., & Shoss, M. K. (2014). Understanding employee responses to stressful information security requirements: A coping perspective. Journal of Management Information Systems, 31(2), 285-318.

D’Arcy, J., Hovav, A., & Galletta, D. (2009). User awareness of security countermeasures and its impact on information systems misuse: A deterrence approach. Information Systems Research, 20(1), 79-98.

Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1989). User acceptance of computer technology: A comparison of two theoretical models. Management Science, 35(8), 982-1002.

DeLone, W. H., & McLean, E. R. (1992). Information systems success: The quest for the dependent variable. Information Systems Research, 3(1), 60-95.

Dinev, T., & Hart, P. (2006). An extended privacy calculus model for e-commerce transactions. Information System Research, 17(1), 61-80.

Dinev, T., Xu, H., Smith, J. H., & Hart, P. (2013). Information privacy and correlates: An empirical attempt to bridge and distinguish privacy-related concepts. European Journal of Information Systems, 22, 295-316.

Epstein, Z. (2012). Arrest half the world: More than 50% of computer users pirate software, study finds. Retrieved from http://bgr.com/2012/05/31/ digital-piracy-bsa-study-2011/.

Fisher, R. J. (1993). Social desirability bias and the validity of indirect questioning. Journal of Consumer Research, 20(2), 303-315.

Fisher, R. J., & Tellis, G. J. (1998). Removing social desirability bias with indirect questioning: Is the cure worse than the disease? Advances in Consumer Research, 25(1), 563-567.

Gefen, D., & Straub, D. (2005). A practical guide to factorial validity using PLS-Graph: Tutorial and annotated example. Communications of the Association for Information Systems, 16, 91- 109.

Gefen, D., Straub, D. W., & Boudreau, M.-C. (2000). Structural equation modeling and regression: Guidelines for research practice.

Communications of the Association for Information Systems, 4, 1-78.

Gergely, M., & Rao, V. S. (2014). Social desirability bias in software piracy research. Proceedings of the European Conference on Information Systems.

Hair, J. F., Tatham, R. L., Anderson, R. E., & Black, W. (2009). Multivariate data analysis. Englewood Cliffs, NJ: Prentice-Hall.

Hansen, J. M., & Walden, E. (2013). The role of restrictiveness of use in determining ethical and legal awareness of unauthorized file sharing. Journal of the Association for Information Systems, 14(9), 521-549,

Hart, C. M., Ritchie, T. D., Hepper, E. G., & Gebauer, J. E. (2015). The balanced inventory of desirable responding short form. SAGE Open, 5(4), 1-9.

Herath, T., & Rao, H. R. (2009). Encouraging information security behaviors in organizations: Role of penalties, pressures and perceived effectiveness. Decision Support Systems, 47, 154-165.

Herbert, J. R., Clemow, L., Pbert, L., Ockene, I. S., & Ockene, J. K. (1995). Social desirability bias in dietary self-report may compromise the validity of dietary intake measures. International Journal of Epidemiology, 24(2), 389-398.

Hong, W., & Thong, J. Y. L. (2013). Internet piracy concerns: An integrated conceptualization and four empirical studies. MIS Quarterly, 37(1), 275-398.

Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. Structural Equation Modeling, 6(1), 1-55.

Hulland, J., Wade, M. R., & Antia, K. D. (2007). The impact of capabilities and prior investments on online channel commitment and performance. Journal of Management Information Systems, 23(4), 109-142.

Iacovou, C. L., Thompson, R. L., & Smith, H. J. (2009). Selective status reporting in information systems projects: A dyadic-level investigation. MIS Quarterly, 33(4), 785-810.

Jarvenpaa, S. L., & Staples, D. S. (2001). Exploring perceptions of organizational ownership of information and expertise. Journal of Management Information Systems, 18(1), 151- 183.

Johnston, A. C., & Warkentin, M. (2010). Fear appeals and information security behaviors: An empirical study. MIS Quarterly, 34(3), 549-566.

Johnston, A. C., Warkentin, M., & Siponen, M. (2015). An enhanced fear appeal rhetorical framework: Leveraging threats to the human asset through sanctioning rhetoric. MIS Quarterly, 39(1), 113- 134.

Kakabadse, N., Porter, G., & Vance, D. (2007). Addicted to technology. Business Strategy Review, 18(4), 81-85.

Keep, W. (2009). Furthering organizational priorities with less than truthful behaviour: A call for additional tools. Journal of Business Ethics, 86(1), 81-90.

Kim, S. S., & Son, J. (2009). Out of dedication or constraint? A dual model of post-adoption phenomena and its empirical test in the context of online services. MIS Quarterly, 33(1), 49- 70.

Kordzadeh, N., & Warren, J. (2017). Communicating personal health information in virtual health communities: An integration of privacy calculus model and affective commitment. Journal of the Association for Information Systems, 18(1), 45-81.

Kuss, D. J., & Griffiths, M. D. (2011). Excessive online social networking: Can adolescents become addicted to Facebook? Education and Health, 29, 63-66.

Kwan, S. S., So, M. K., & Tam, K. Y. (2010). Applying the randomized response technique to elicit truthful responses to sensitive questions in IS research: The case of software piracy behavior. Information Systems Research, 21(4), 941-959.

Lee, I. A., & Preacher, K. J. (2013). Calculation for the test of the difference between two dependent correlations with one variable in common. [Computer software] Retrieved from http://quantpsy.org/corrtest/corrtest2.htm.

Lee, Y. E., & Benbasat, I. (2011). The Influence of trade-off difficulty caused by preference elicitation methods on user acceptance of recommendation agents across loss and gain conditions. Information Systems Research, 22(4), 867-884

Leite, W. L., & Beretvas, N. (2005). Validation of scores on the Marlowe-Crowne social desirability scale and the balanced inventory of desirable responding. Educational and Psychological Measurement, 65(1), 140-154.

Li, A., & Bagger, J. (2007). The balanced inventory of desirable responding (BIDR): A reliability

generalization study. Educational and Psychological Measurement, 67(3), 525-544.

Lowry, P. B., & Moody, G. D. (2015). Proposing the control‐reactance compliance model (CRCM) to explain opposing motivations to comply with organisational information security policies. Information Systems Journal, 25(5), 433-463.

Lowry, P. B., Moody, G. D., Galletta, D. F., & Vance, A. (2013). The drivers in the use of online whistle-blowing reporting systems. Journal of Management Information Systems, 30(1), 153- 190.

Lowry, P. B., Posey, C., Bennett, R. B. J., & Roberts, T. L. (2015). Leveraging fairness and reactance theories to deter reactive computer abuse following enhanced organisational information security policies: An empirical study of the influence of counterfactual reasoning and organisational trust. Information Systems Journal, 25(3), 193-273.

Ma, X., Kim, S. H., & Kim, S. S. (2014). Online gambling behavior: The impacts of cumulative outcomes, recent outcomes, and prior use. Information Systems Research, 25(3), 511- 527.

Majchrzak, A., Wagner, C., & Yates, D. (2013). The impact of shaping on knowledge reuse for organizational improvement with Wikis. MIS Quarterly, 37(2), 455-469.

Malhotra, N. K., Kim, S. S., & Agarwal, J. (2004). Internet users’ information privacy concerns (IUIPC): The construct, the scale, and a causal model. Information Systems Research, 15(4), 336-355.

Malhotra, N. K., Kim, S. S., & Patil, J. (2006). Common method variance in IS research: A comparison of alternative approaches and a reanalysis of past research. Management Science, 52(12), 1865-1883.

Mick, D. G. (1996). Are studies of dark side variables confounded by socially desirable responding? The case of materialism. Journal of Consumer Research, 23(2), 106-119.

Miller, D. L., & Thomas, S. (2005). The impact of relative position and relational closeness on the reporting of unethical acts. Journal of Business Ethics, 61(4), 315-328.

Millham, J. (1974). Two components of need for approval score and their relationship to cheating following success and failure. Journal of Research in Personality, 8, 378-392.

Mossholder, K. W, & Giles, W. P. (1983). The use of partial correlation to control halo in performance ratings. Educational and Psychological Measurement, 43, 977-984.

Nederhof, A. J. (1985). Methods of coping with social desirability bias: A review. European Journal of Social Psychology, 15(3), 263-280.

Neeley, S. M., & Cronley, M. L. (2004). When research participants don’t tell it like it is: Pinpointing the effects of social desirability bias using self vs. indirect questioning. Advances in Consumer Research, 31, 432-433.

Nunnally, I. H., & Bernstein, J. C. (1994). Psychometric Theory, New York, NY: McGraw-Hill.

Paulhus, D. L. (1984). Two-component models of socially desirable responding. Journal of Personality and Social Psychology, 46(3), 598- 609.

Paulhus, D. L. (1991). Measurement and control of response bias. In J. Robinson, P. Shaver, & L. Wrightsman (Eds.), Measures of personality and social psychological attitudes (pp. 17-59). San Diego, CA: Academic.

Paulhus, D. L. (1994). Balanced inventory of desirable responding: Reference manual for BIDR version 6 (unpublished manuscript). University of British Columbia, Vancouver, Canada.

Paulhus, D. L. (1998). Manual for the Paulhus Deception Scales: BIDR Version 7. Toronto, Canada: Multi-Health Systems.

Paulhus, D. L. (2002). Socially desirable responding: The evolution of a construct. In H. Brown, D. Jackson, & D. Wiley (Eds.), The role of constructs in psychological and educational measurement (pp. 67-88). Hillsdale, NJ: Erlbaum.

Paulhus, D. L., & John, O. P. (1998). Egoistic and moralistic biases in self-perception: The interplay of self-deceptive styles with basic traits and motives. Journal of Personality, 66(6), 1025-1060.

Paulhus, D. L., & Reid, D. B. (1991). Enhancement and denial in socially desirable responding. Journal of Personality and Social Psychology, 60(2), 307-317.

Pavlou, P. A., & El Sawy, O. A. (2006). From IT leveraging competence to competitive advantage in turbulent environments: The case of new product development. Information Systems Research, 17(3), 198-227.

Pavlou, P. A., & El Sawy, O. A. (2010). The “third hand”: IT-enabled competitive advantage in turbulence through improvisational capabilities. Information Systems Research, 21(3), 443-471.

Peace, G., Galletta, D. F., & Thong, J. Y. L. (2003). Software piracy in the workplace: A model and empirical test. Journal of Management Information Systems, 20(1), 153-177.

Greenwood, S., Perrin, A., & Duggan, M. (2016). Social media update 2016. Retrieved from http://www.pewinternet.org/2016/11/11/socialmedia-update-2016/.

Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method bias in behavioral research: A critical review of the literature and recommended remedies. Journal of Applied Psychology, 88(5), 879-903.

Posey, C., Bennett, R. J., Roberts, T. L., & Lowry, P. B. (2011). When computer monitoring backfires: Invasion of privacy and organizational injustice as precursors to computer abuse. Journal of Information System Security, 7(1), 24-47.

Posey, C., Roberts, T. L., & Lowry, P. B. (2015). The impact of organizational commitment on insiders’ motivation to protect organizational information assets. Journal of Management Information Systems, 32(4), 179-214.

Ramanaiah, N. V., Schill, T., & Leung, L. S. (1977). A test of the hypothesis about the twodimensional nature of the Marlowe-Crowne social desirability scale. Journal of Research in Personality, 11, 251-259.

Randall, D. M., & Fernandes, M. F. (1991). The social desirability response bias in ethics research. Journal of Business Ethics, 10(11), 805-817.

Reynolds, W. M. (1982). Development of reliable and valid short forms of the Marlowe-Crowne social desirability scale. Journal of Clinical Psychology, 38(1), 119-125.

Robertson, D. H., & Joselyn, R. W. (1974). Projective techniques in research. Journal of Advertising Research, 14(5), 27-31.

Sheng, H., Nah, F. F.-H., & Siau, K. (2008). An experimental study on ubiquitous commerce adoption: Impact of personalization and privacy concerns. Journal of Association for Information Systems, 9(6), 344-376.

Sierra, J. J., & Hyman, M. R. (2006). A dual-process model of cheating intentions. Journal of Marketing Education, 28(3), 193-204.

Simon, J. L., & Simon, R. J. (1974). The effect of money incentives on family size: A hypothetical-question study. Public Opinion Quarterly, 38(4), 585-595.

Sinha, R. K., & Mandel, N. (2008). Preventing digital music piracy: The carrot or the stick? Journal of Marketing, 72(1), 1-15.

Snow, A. P., Keil, M., & Wallace, L. (2007). The effects of optimistic and pessimistic biasing on software project status reporting. Information and Management, 44, 130-141.

Sojer, M., Alexy, O., Kleinknecht, S., and Henkel, J. (2014) Understanding the drivers of unethical programming behavior: The inappropriate reuse of internet-accessible code. Journal of Management Information Systems, 31(3), 287- 925.

Song, J., & Zahedi, F. M. (2005). A theoretical approach to web design in e-commerce: A belief reinforcement model. Management Science, 51(8), 1219-1235.

Soror, A. A., Hammer, B. I., Steelman, Z. R., Davis, F. D., & Limayem, M. M. (2015). Good habits gone bad: Explaining negative consequences associated with the use of mobile phones from a dual-systems perspective. Information Systems Journal, 25, 403-427.

Srivastava, S. C., Chandra, S., & Shirish, A. (2015). Technostress creators and job outcomes: Theorising the moderating influence of personality traits. Information Systems Journal, 25(4), 355-401.

Steenkamp, J.-B. E. M., De Jong, M. G., & Baumgartner, H. (2010). Socially desirable response tendencies in survey research. Journal of Marketing Research, 47(2), 199-241.

Steiger, J. H. (1980). Tests for comparing elements of a correlation matrix. Psychological Bulletin, 87, 245-251.

Stöber, J. (2001). The Social Desirability Scale-17 (SDS-17): Convergent validity, discriminant validity, and relationship with age. European

Journal of Psychological Assessment, 17, 222- 232.

Strahan, R., & Gerbasi, K. C. (1972). Short, homogeneous versions of the Marlow-Crowne social desirability scale. Journal of Clinical Psychology, 28(2), 191-193.

Tiwana, A., & Bush, A. A. (2007). A comparison of transaction cost, agency, and knowledge-based predictors of IT outsourcing decisions: A U.S.- Japan cross-cultural field study. Journal of Management Information Systems, 24(1), 259- 300.

Turel, O., & Serenko, A. (2012). The benefits and dangers of enjoyment with social networking websites. European Journal of Information Systems, 21(5), 512-528

Turel, O., Serenko, A., & Giles, P. (2011). Investigating technology addiction and use: An empirical investigation of online auction users. MIS Quarterly, 35(4), 1043-1061.

Vance, A., Lowry, P. B., & Eggett, D. (2015). Increasing accountability through userinterface design artifacts: A new approach to addressing the problem of access-policy violations. MIS Quarterly, 39(2), 345-366.

Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. MIS Quarterly, 36(1), 157-178.

Wang, Y., & Haggerty, N. (2011). Individual virtual competence and its influence on work outcomes. Journal of Management Information Systems, 27(4), 299-334.

Webster, J., & Martocchio, J. J. (1992). Microcomputer playfulness: Development of a measure with workplace implications. MIS Quarterly, 16(2) 201-226.

Xu, H., Dinev, T, & Smith, J. (2011). Information privacy concerns: Linking individual perceptions with institutional privacy assurances. Journal of the Association for Information Systems, 12(12), 798-824.

## Appendix: Measurement

## 1. SNS Addiction

1.1. SNS Addiction (Charlton, 2002; Turel et al., 2011)

ADD1. I sometimes neglect important things because of my interest in SNS.

ADD2. My life has sometimes suffered because of me interacting with SNS.

ADD3. Using SNS sometimes interfered with other activities.

ADD4. When I am not using SNS I often feel agitated.

ADD5. I have made unsuccessful attempts to reduce the time I interact with SNS.

ADD6. I am sometimes late for engagements because I interact with SNS.

ADD7. Arguments have sometimes arisen because of the time I spend on SNS.

ADD8. I think that I am addicted to SNS.

ADD9. I often fail to get enough rest because I interact with SNS.

## 1.2. Perceived Usefulness (Kim & Son, 2009)

PU1: Using SNS enhances my effectiveness.

PU2: Using SNS enhances my productivity.

PU3: Using SNS improves my performance.

## 1.3. Perceived Ease of Use (Davis et al., 1989)

PE1: Learning how to use SNS is easy for me.

PE2: My interaction with SNS is clear and understandable.

PE3: It is easy for me to become skillful at using SNS.

## 1.4. SNS Addiction (Indirect Questioning) (Charlton, 2002; Turel et al., 2011)

ADDi1. A typical SNS user sometimes neglects important things because of my interest in SNS.

ADDi2. A typical SNS user’s life has sometimes suffered because of him/her interacting with SNS.

ADDi3. Using SNS sometimes interfered with other activities of a typical SNS user.

ADDi4. When a typical SNS user is not using SNS, he/she often feel agitated.

ADDi5. A typical SNS user has made unsuccessful attempts to reduce the time he/she interacts with SNS.

ADDi6. A typical SNS user is sometimes late for engagements because he/she interacts with SNS.

ADDi7. Arguments have sometimes arisen because of the time a typical SNS user spends on SNS.

ADDi8. A typical SNS user thinks that he/she is addicted to SNS.

ADDi9. A typical SNS user often fails to get enough rest because he/she interacts with SNS.

## 2. Digital Piracy

## 2.1. Perceived Threat Severity (Johnston & Warkentin, 2010)

If I were caught committing digital piracy, the consequences would be

Journal of the Association for Information Systems

SEV1: severe

SEV2: serious

SEV3: significant

## 2.2. Perceived Threat Susceptibility (Johnston & Warkentin, 2010)

SUS1: To me, committing digital piracy is at risk of being caught

SUS2: It is likely to be caught if I commit digital piracy.

SUS3: It is possible to be caught if I commit digital piracy.

## 2.3. Digital Piracy Intention (Johnston & Warkentin, 2010)

DPI1: I may commit digital piracy in the future.

DPI2: If I had the opportunity, I would commit digital piracy.

DPI3: I intend to commit digital piracy in the future.

## 2.4. Digital Piracy Intention (Indirect Questioning) (Johnston & Warkentin, 2010)

DPIi1: A typical Internet user may commit digital piracy in the future.

DPIi2: If a typical Internet user had the opportunity, he/she would commit digital piracy.

DPIi3: A typical Internet user intends to commit digital piracy in the future.

## 3. Social Desirability Scales

## 3.1. Marlowe-Crowne Scale (Reynolds, 1982)

Please indicate whether the statements below are true or false with respect to yourself.

MC1. It is sometimes hard for me to go on with my work if I am not encouraged. (F)

MC2. I sometimes feel resentful when I don’t get my way. (F)

MC3. On a few occasions, I have given up doing something because I thought too little of my ability. (F)

MC4. There have been times when I felt like rebelling against people in authority even though I knew they were right. (F)

MC5. No matter who I’m talking to, I’m always a good listener. (T)

MC6. There have been occasions when I took advantage of someone. (F)

MC7. I’m always willing to admit it when I make a mistake. (T)

MC8. I sometimes try to get even, rather than forgive and forget. (F)

MC9. I am always courteous, even to people who are disagreeable. (T)

MC10. I have never been irked when people expressed ideas very different from my own. (T)

MC 11. There have been times when I was quite jealous of the good fortune of others. (F)

MC 12. I am sometimes irritated by people who ask favors of me. (F)

MC 13. I have never deliberately said something that hurt someone’s feelings. (T)

(F) Items keyed in the negative direction.

## 3.2. Balanced Inventory of Desirable Responding-16 (Hart et al., 2015)

Please answer the following questions with respect to yourself (1: Not true – 7: Very true)

## 3.2.1. Self-Deception Enhancement

SDE1: I have not always been honest with myself. (R)

SDE2: I always know why I like things.

SDE3: It’s hard for me to shut off a disturbing thought. (R)

SDE4: I never regret my decisions.

SDE5: I sometimes lose out on things because I can’t make up my mind soon enough. (R)

SDE6: I am a completely rational person.

SDE7: I am very confident of my judgments.

SDE8: I have sometimes doubted my ability as a lover. (R)

Add one point for every “6” or “7” (minimum = 0: maximum = 8)

(R) Items keyed in the “False” (negative) direction.

## 3.2.2. Impression Management

IM1: I sometimes tell lies if I have to. (R)

IM2: I never cover up my mistakes.

IM3: There have been occasions when I have taken advantage of someone. (R)

IM4: I sometimes try to get even rather than forgive and forget. (R)

IM5: I have said something bad about a friend behind his or her back. (R)

IM6: When I hear people talking privately, I avoid listening.

IM7: I never take things that don’t belong to me.

IM8: I don’t gossip about other people’s business.

Add one point for every “6” or “7” (minimum = 0: maximum = 8)

(R) Items keyed in the “False” (negative) direction.

## About the Authors

Dong-Heon (Austin) Kwak is an assistant professor of information systems at Kent State University. He received his PhD in management information systems from the University of Wisconsin-Milwaukee. He has published in Journal of the Association for Information Systems, Computers in Human Behavior, Computers & Education, and elsewhere.

Philipp Holtkamp is the general manager of innovation at Wärtsilä Corporation. He received his PhD in business economics from the University of Jyväskylä, Finland. He has published in Journal of System and Software, Journal of Software Evolution and Process, Information Technology & People, and elsewhere.

Sung S. Kim is the Peter T. Allen Professor in the Department of Operations and Information Management at the University of Wisconsin School of Business. He holds a PhD in information technology management from the Georgia Institute of Technology. His work has appeared in Management Science, Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Journal of the Association for Information Systems, and Decision Sciences.

Copyright © 2019 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints or via email from publications@aisnet.org.
