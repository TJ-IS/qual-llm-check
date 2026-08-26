---
otero_id: 10704
otero_key: "KDR4N6PM"
title: "<b>Research Note</b>—Applying the Randomized Response Technique to Elicit Truthful Responses to Sensitive Questions in IS Research: The Case of Software Piracy Behavior"
authors: "Samuel S. K. Kwan; Mike K. P. So; Kar Yan Tam"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0271"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/KDR4N6PM/fulltext/images/9412dd0041760e12cb8120c01861abcfcf57e326cb7ee6db9b27c49132098e7c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Note—Applying the Randomized Response Technique to Elicit Truthful Responses to Sensitive Questions in IS Research: The Case of Software Piracy Behavior

Samuel S. K. Kwan, Mike K. P. So, Kar Yan Tam,

## To cite this article:

Samuel S. K. Kwan, Mike K. P. So, Kar Yan Tam, (2010) Research Note—Applying the Randomized Response Technique to Elicit Truthful Responses to Sensitive Questions in IS Research: The Case of Software Piracy Behavior. Information Systems Research 21(4):941-959. http://dx.doi.org/10.1287/isre.1090.0271

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/KDR4N6PM/fulltext/images/efcfe96a44e4e8d101ed7eb714808257cbc6735545f7dc73ad3570bd4a8c9ce7.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Applying the Randomized Response Technique to Elicit Truthful Responses to Sensitive Questions in IS Research: The Case of Software Piracy Behavior

Samuel S. K. Kwan, Mike K. P. So, Kar Yan Tam

Department of Information Systems, Business Statistics and Operations Management, Hong Kong University of Science and Technology (HKUST), Clear Water Bay, Hong Kong {samuel.kwan@ust.hk, immkpso@ust.hk, kytam@ust.hk}

R<sup>esearch</sup> <sup>on</sup> <sup>software</sup> <sup>piracy</sup> <sup>often</sup> <sup>relies</sup> <sup>on</sup> <sup>self-reports</sup> <sup>by</sup> <sup>individual</sup> <sup>users</sup> <sup>and</sup> <sup>thus</sup> <sup>suffers</sup> <sup>from</sup> <sup>possible</sup>response distortion attributable to a variety of human motivations. Conclusions drawn directly from distorted self-reports may misguide managerial and policy decisions. The randomized response technique (RRT) was proposed as a remedy to response distortion. In this paper, a model based on RRT was used to illustrate how truthful responses to sensitive questions can be empirically estimated. The model was tested in two empir ical studies on software piracy. Consistent with our expectations, respondents responding to RRT were more willing to disclose sensitive information about their attitudes, intentions, and behaviors on software piracy. Nontrivial distortions were demonstrated in causal relationships involving sensitive and nonsensitive variables. The study extends RRT to multivariate analysis and illustrates the feasibility and usefulness of the method in studying sensitive behavioral issues in the information systems (IS) domain.

Key words: response distortion; software piracy; randomized response technique; unrelated question design; method of moments; socially desirable responding; structural equation modeling

History: Accepted by Soon Ang, Senior Editor; H. Raghav Rao, Associate Editor. This paper was received on November 15, 2006, and was with the authors 5 months for 2 revisions. Published online in Articles in Advance March 1, 2010.

## 1. Introduction

Response distortion has long been a recognized problem in behavioral research that relies on self-reported data (Himmelfarb 1993). It generally refers to situations where the answer provided by a subject does not accurately reflect his genuine opinion, belief, feeling, intention, or behavior. Conceivably, such distortions are likely consequences when respondents find questions or answers sensitive or when a response might incur legal liability (Locander et al. 1976). Response distortion poses serious difficulties for behavioral research in at least two ways. First, it threatens the validity of the conclusions of such research. Substantive conclusions could be biased if response distortion is not taken into consideration. Second, researchers may resort to studying less relevant variables if the variables of primary interest are extremely sensitive and susceptible to response distortion that cannot be properly accounted for. Ironically, this may result in a lack of research in areas where objective investigations are badly needed.

Modern information technology (IT) is having a growing impact on the lifestyle and social behavior of individuals. More and more sensitive behavioral issues pertaining to the use of IT have come to light. Two decades ago, Mason (1986) advocated four principles<sup>1</sup> to guide the ethical uses of IT. Unfortunately, these principles are not universally observed. There is mounting evidence on the unethical uses of IT as reflected in the increasing activities related to software piracy, cyberslacking,<sup>2</sup> unauthorized online gambling, web pornography, etc. Though investigations into these activities are highly warranted because of their societal impact, research in these areas is likely impeded by response distortion due to the research’s sensitive nature.

Our study focuses on problems related to response distortion and illustrates the resolution of those problems in the context of software piracy. The Business Software Alliance (BSA) reported that piracy costs the industry more than U.S.\$48 billion a year (BSA 2007). Over the past 20 years, there has been a continuous (and expanding) stream of research on software piracy, using self-reported data solicited from individuals. It is not uncommon for information systems (IS) researchers to acknowledge response distortion as a limitation of their empirical findings (e.g., Cheng et al. 1997, Christensen and Eining 1991, Limayem et al. 2004, Moores and Chang 2006, Seale 2002, Sims et al. 1996, Taylor and Shim 1993). However, little effort has been expended to resolve this problem.

In this study, the randomized response technique (RRT) is applied to model the causal relationships in software piracy. Randomized response is a technique that was first conceived by Warner (1965) and has been deployed to study sensitive topics in many areas. However, the vast majority of applications have involved simple univariate analysis. The current work extends the application of RRT to multivariate analysis. Our intention is not to develop another behavioral model on software piracy or refute existing ones, but to suggest ways to alleviate the methodological limitations that undermine empirical research in this area. The current work aims at introducing RRT to the IS community, especially to researchers working on sensitive issues pertaining to the development and usage of IT services.

## 2. Respondent Confidentiality by Design

2.1. Assuring Respondents of Confidentiality Traditionally, researchers soliciting self-reports on sensitive topics provide confidentiality assurance to respondents. This is usually accomplished by convincing respondents that the survey is completely anonymous and confidential. Over the years, numerous survey practices (e.g., physical separation of respondents, promises of confidentiality, emphasis on truthful responding rather than a “right” answer) have been advanced for different types of survey administration (see Paulhus 1991). Confidentiality assurance, if successfully implemented, is a very powerful strategy and should eliminate most of the undesirable motivations leading to response distortion. Its success hinges on whether or not the respondent is convinced by the assurance. When questions are considered sensitive, embarrassing, or threatening, the credibility of such a confidentiality assurance should be of prime importance and respondents will demand more convincing assurance.

## 2.2. The Randomized Response Technique

RRT was introduced to provide the assurance necessary to induce truthful responses to sensitive questions. It asks questions in ways that incorporate respondent confidentiality by design. It was first conceived by Warner (1965) and since then various forms of RRT have been proposed to solicit truthful responses to difficult or embarrassing questions (Fox and Tracy 1986, Greenberg et al. 1969, Himmelfarb and Lickteig 1982, Warner 1965). The core idea of RRT is to assure the complete confidentiality of a participant’s response by contaminating it with random “noise” with known statistical properties.

In the “unrelated question” variant of RRT (Greenberg et al. 1969), respondents are instructed to choose between a pair of questions to answer according to a randomizing device they control privately (e.g., flipping a coin). Each sensitive question is paired with another unrelated and innocuous (i.e., nonsensitive) question such that the respondent answers one of them depending on the outcome of the privately performed random choice procedure. Because the researcher has no way of knowing exactly which question was answered, complete confidentiality can be assured. This helps to dilute any stigma or embarrassment caused by the sensitive question and results in more truthful responses. Because the probabilities associated with the random choice procedure are known, distribution of the answers to the sensitive question can be estimated.

Previous research has shown that using RRT can lead to greater candor about sensitive personal attributes or behaviors (Armacost et al. 1991). Validation studies with participants whose sensitive attributes were known in advance also revealed that RRT outperformed other techniques in soliciting valid responses to sensitive questions (Hosseini and Armacost 1993, Lensvelt-Mulders et al. 2005, Scheers 1992, Umesh and Peterson 1991).

Though RRT has shown promise in reducing response distortion, a number of issues still need to be considered. First, because the data it generates contain random noise, the overall measurement reliability is inevitably reduced. Larger samples are required. Statistical power depends on the probability of respondents answering the sensitive questions truthfully, so researchers have to strike a balance between perceived confidentiality and data collection efficiency (Fox and Tracy 1986). Hosseini and Armacost (1993) concluded that RRT should be used only for sensitive questions. Obviously, questions pertaining to software piracy behavior belong to this category.

Second, the complexity due to the random choice procedure may sometimes result in the answering process not being completely understood by respondents. This can lead to incorrect responses or missing data. In addition, respondents who do not understand the procedure may not be convinced of the confidentiality protection that is built into the method; this can undermine RRT’s benefits. In the case of software piracy studies, target respondents are computer users. These people are more likely to be capable of understanding the procedure.

It is important to note, however, that though RRT is a procedural improvement that should increase the credibility of assurances of response confidentiality (Podsakoff et al. 2003), there may still be untruthful responding. The amount of distortion should, however, be much lower than with direct self-reports. In a validation study of RRT, van der Heijden et al. (2000) compared the proportions of respondents admitting to income fraud using different questioning methods. The study revealed that RRT increased the percentage of truthful responses to 43%, up from 25% with face-to-face direct questioning and from 19% with computer-assisted self-interviews. Although RRT is not a complete cure for the problem of response distortion, it helps to improve the likelihood of truthful responses.

## 2.3. RRT in Multivariate Analysis

In its original form, RRT was limited to two-choice questions only but was later extended to multiplechoice and other types. In particular, the quantitative answers often required in modern behavioral research can be obtained using the unrelated question design of Greenberg et al. (1971). However, the majority of the literature on RRT focuses on univariate analysis (e.g., the proportion of people committing a certain criminal behavior, the mean value of a sensitive characteristic, etc.) and there is a common misunderstanding that RRT is limited in its use to univariate analysis.<sup>3</sup> This is not true in principle, although more sophisticated statistical estimators would be required for multivariate analysis.

Fox and Tracy (1984) developed a method to estimate the correlation between randomized responses obtained from an unrelated question design. Their model treats the random choice procedure as a source of measurement error with known statistical properties. They showed that the true underlying correlation between the randomized responses can be estimated simply by eliminating the measurement errors. However, apart from the basic assumption that the innocuous questions are unrelated to the sensitive questions, there are two additional assumptions in Fox and Tracy’s (1984) analysis: (1) the innocuous questions are unrelated to each other; and (2) the statistical properties of the answers to the innocuous questions are known. These assumptions are not easy to satisfy, and they make the technique less practical because they significantly increase the difficulty of choosing an appropriate set of innocuous questions. Fox and Tracy (1984) did not report any empirical evidence for the feasibility and applicability of their method, but despite its shortcomings their work demonstrates that, in principle, it is possible to apply RRT in analyzing correlated responses to different questions.

The aim of the present study is to deploy RRT in multivariate causal analysis of software piracy behavior without being constrained by Fox and Tracy’s (1984) two assumptions. In the next two sections, a basic univariate analysis is first used to measure respondents’ attitudes, intentions, and behaviors with respect to software piracy. The basic model is then extended to multivariate analysis of data collected in a large-scale online survey. The findings demonstrate how research findings on software piracy can be substantively different when response distortion is mitigated by the application of RRT.

## 3. Basic Model: The Unrelated Question Design

The unrelated question design proposed by Greenberg et al. (1971) was used to solicit quantitative answers to sensitive questions. In the unrelated question design, respondents are presented with a pair of unrelated questions consisting of a sensitive and an innocuous question. They are instructed to conduct a private random choice procedure and then follow the outcome to choose a question from the pair to answer. A simple illustration using coin flipping as the random choice procedure is shown below:

Instruction: Please flip a coin and answer Question X if it is heads: otherwise, please answer Question Y  
Question X: I like to browse pornographic web sites. Question Y: I like to browse online newspaper web sites.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Strongly disagree</td><td>Disagree</td><td>Slightly disagree</td><td>Neutral</td><td>Slightly agree</td><td>Agree</td><td>Strongly agree.</td></tr></table>

In practice, if no prior knowledge of the distribution of answers to the innocuous question is assumed, it is necessary to collect two samples using different probabilities in the random choice procedure in order to estimate the unknown variables using the method of moments.

## 3.1. Model Definition and Mean Estimator

Consider a pair of questions $q _ { X }$ and $q _ { Y } .$ , where $q _ { X }$ is sensitive and $q _ { Y }$ is innocuous. The design requires that two samples differing in the probability of answering the sensitive question be collected. For notational clarity, all variables pertaining to the first and second samples will be subscripted by $( 1 )$ and $_ { ( 2 ) } ,$ respectively. Assume that the probability of answering the sensitive question is $p _ { ( 1 ) }$ for the first sample and $p _ { ( 2 ) }$ for the second. By design, $p _ { ( 2 ) } \neq p _ { ( 1 ) }$

Denote Z as the observed response, and X and Y as the underlying responses to $q _ { X }$ and $q _ { Y } ,$ respectively. By design, the random variables X and Y are related to $Z$ as follows:

$$
\left\{ \begin{array}{l} Z _ {(1)} = I _ {(1)} X + (1 - I _ {(1)}) Y \\ Z _ {(2)} = I _ {(2)} X + (1 - I _ {(2)}) Y, \end{array} \right.\tag{1}
$$

where $I _ { ( 1 ) }$ and $I _ { ( 2 ) }$ are independent indicator variables such that

$$
\begin{array}{l} I _ {(1)} = \left\{ \begin{array}{l l} 1 & \text { with   probability } p _ {(1)} \\ 0 & \text { with   probability } 1 - p _ {(1)} \end{array} \right. \\ I _ {(2)} = \left\{ \begin{array}{l l} 1 & \text { with   probability } p _ {(2)} \\ 0 & \text { with   probability } 1 - p _ {(2)} \end{array} \right. \quad \text { and } \quad p _ {(1)} \neq p _ {(2)}. \end{array}
$$

Equation (1) is the basic model for the unrelated question design. Its use of the indicator variables $I _ { ( 1 ) }$ and $I _ { ( 2 ) }$ allows convenient parameter estimation based on the method of moments because their expected values are simply the corresponding probabilities $p _ { ( 1 ) }$ and $p _ { ( 2 ) }$

Proposition 1. The method-of-moments estimators for the population means of the underlying variables X and $\boldsymbol { Y } ,$ namely, $\mu _ { X }$ and $\mu _ { Y } ,$ are<sup>4</sup>

$$
\hat {\mu} _ {X} = \frac {(1 - p _ {(2)}) \bar {Z} _ {(1)} - (1 - p _ {(1)}) \bar {Z} _ {(2)}}{p _ {(1)} - p _ {(2)}},\tag{2}
$$

$$
\hat {\mu} _ {Y} = \frac {p _ {(1)} \bar {Z} _ {(2)} - p _ {(2)} \bar {Z} _ {(1)}}{p _ {(1)} - p _ {(2)}}.\tag{3}
$$

Proposition 2. The distributions of the underlying variables X and Y are

$$
\begin{array}{l} \operatorname * {P r} [ X = m ] \\ = \frac {(1 - p _ {(2)}) \operatorname * {P r} [ Z _ {(1)} = m ] - (1 - p _ {(1)}) \operatorname * {P r} [ Z _ {(2)} = m ]}{p _ {(1)} - p _ {(2)}}, \end{array}\tag{4}
$$

$$
\operatorname * {P r} [ Y = m ] = \frac {p _ {(1)} \operatorname* {P r} [ Z _ {(2)} = m ] - p _ {(2)} \operatorname* {P r} [ Z _ {(1)} = m ]}{p _ {(1)} - p _ {(2)}}.\tag{5}
$$

The proofs of Propositions 1 and 2 are shown in Appendix A.

$^ 4 \bar { Z } _ { ( 1 ) }$ and ${ \bar { Z } } _ { ( 2 ) }$ are the sample means of the observed variable in the first and second samples, respectively.

## 3.2. Variance of the Mean Estimator

Consider the sampling variance of the mean estimators in (2) and (3). Because the two samples are independent, the sampling variances of these estimators become

$$
\begin{array}{c} \operatorname{var} (\hat {\mu} _ {X}) = \frac {1}{(p _ {(1)} - p _ {(2)}) ^ {2}} \bigg [ \frac {(1 - p _ {(2)}) ^ {2} \operatorname{var} (Z _ {(1)})}{n _ {(1)}} \\ + \frac {(1 - p _ {(1)}) ^ {2} \operatorname{var} (Z _ {(2)})}{n _ {(2)}} \bigg ], \end{array}\tag{6}
$$

$$
\begin{array}{l} \operatorname{var} (\hat {\mu} _ {Y}) = \frac {1}{(p _ {(1)} - p _ {(2)}) ^ {2}} \\ \qquad \cdot \left[ \frac {p _ {(2)} ^ {2} \operatorname{var} (Z _ {(1)})}{n _ {(1)}} + \frac {p _ {(1)} ^ {2} \operatorname{var} (Z _ {(2)})}{n _ {(2)}} \right], \end{array}\tag{7}
$$

where $\mathrm { v a r } ( Z _ { ( 1 ) } )$ and $\operatorname { v a r } ( Z _ { ( 2 ) } )$ are the variances of the observed responses $Z _ { ( 1 ) }$ and $Z _ { ( 2 ) } ,$ and $n _ { ( 1 ) }$ and $n _ { ( 2 ) }$ are the respective sample sizes.<sup>5</sup> Becasue $\hat { \mu } _ { X }$ and $\hat { \mu } _ { Y }$ are linear combinations of the two sample means, asymptotic normality can be assumed. This enables conventional statistical inferences about the estimated means.

## 3.3. Choice of Probability Values

To administer a survey using the unrelated question design, the researcher needs to choose two different probability values for use with the two independent samples. In practice, a high probability of answering the sensitive question would tend to deter respondents from giving truthful answers. Also, the assigned probability needs to be made known to the respondents to avoid suspicion. To help respondents understand the method, the random choice procedure is usually a simple task such as flipping a coin or throwing a die. Therefore, the chance of answering the sensitive question is often expressed as a simple fraction. Fox and Tracy (1986) have described how a common misconception about randomness might be exploited in this situation: “One of the advantages of a 0.5 selection probability, particularly when using unsophisticated or skeptical populations, is that many people wrongly believe that 0.5 is random and that anything else is “stacked” (p. 25). In other words, a transparent probability of 0.5 can be a very good choice to allay respondents’ suspicions. However, because two different probabilities are needed, values other than 0.5 must be considered. Furthermore, extreme values also cause respondents’ suspicion; therefore, a probability higher than 0.75 may not be suitable. Appendix B shows a detailed analysis of the statistical considerations involved in minimizing the sampling variance shown in (6). In summary, the following two criteria can be used:

1. The difference between the two probability values should be as large as practicable; and

2. Once one of the probability values and the spread between the two probability values are determined, the other probability value should be chosen from the larger side of the first probability value.

Balancing psychological considerations with statistical considerations suggests two possible strategies. First, a disparate pair of probability values, neither higher than 0.75, may be used. An example would be $( p _ { ( 1 ) } = 0 . 2 5 , p _ { ( 2 ) } = 0 . 7 5 )$ . Alternatively, we may choose 0.5 for one sample and a probability value between 0.5 and 0.75 for the other. An example is the choice of $( p _ { ( 1 ) } = 0 . 7 5 , ~ p _ { ( 2 ) } = 0 . 5 )$ . The first strategy emphasizes statistical efficiency while the second aims to reduce respondents’ worries and suspicions. In any case, researchers are advised to strike a good balance between statistical and psychological considerations.

## 3.4. Sample Size

The sampling variance of the mean estimator as shown in (6) reveals that the sampling variance is a strictly decreasing function of the sample sizes $n _ { ( 1 ) }$ and $n _ { ( 2 ) } .$ . However, it is unclear how the sampling variance is affected by the relative magnitudes of $n _ { ( 1 ) }$ and $n _ { ( 2 ) }$ . Rewrite the sampling variance using two new parameters N and k, where N is the total number of randomized responses and k is the ratio between the two sample sizes. By definition,

$$
\left\{ \begin{array}{l} N = n _ {(1)} + n _ {(2)} \\ k = \frac {n _ {(1)}}{n _ {(2)}} \end{array} \right. \Rightarrow \left\{ \begin{array}{l} n _ {(1)} = \frac {k N}{(1 + k)} \\ n _ {(2)} = \frac {N}{(1 + k)}. \end{array} \right.\tag{8}
$$

Substituting $n _ { ( 1 ) }$ and $n _ { ( 2 ) }$ with N and k in (6) yields $\mathrm { v a r } ( \hat { \mu } _ { X } )$

$$
= \frac {(1 + k) [ (1 - p _ {(2)}) ^ {2} \operatorname{var} (Z _ {(1)}) + k (1 - p _ {(1)}) ^ {2} \operatorname{var} (Z _ {(2)}) ]}{k N (p _ {(1)} - p _ {(2)}) ^ {2}}.\tag{9}
$$

Table 1 Pairing of Sensitive and Innocuous Questions (Study 1)

<table><tr><td>Variable</td><td>Sensitive question</td><td>Innocuous question</td><td>Scale</td></tr><tr><td>Control</td><td>To me, singing at a karaoke bar is:</td><td>To me, dining at an expensive restaurant on a holiday is:</td><td>1–7 (Good-Bad)</td></tr><tr><td>Attitude1</td><td>To me, unauthorized copying of software is:</td><td>To me, killing an insect at home is:</td><td>1–7 (Not guilty-Guilty)</td></tr><tr><td>Attitude2</td><td>To me, unauthorized copying of software is:</td><td>To me, recording daily expenses in detail is:</td><td>1–7 (Foolish-Wise)</td></tr><tr><td>Attitude3</td><td>To me, unauthorized copying of software is:</td><td>To me, taking vitamin pills every day is:</td><td>1–7 (Helpful-Harmful)</td></tr><tr><td>Intention1</td><td>I may copy software without authorization in the future.</td><td>I think Chinese osteopathy is best for treating sprains.</td><td>1–7 (Agree-Disagree)</td></tr><tr><td>Intention2</td><td>If I have the opportunity, I would copy software without authorization.</td><td>I think the pace of people in Hong Kong is too fast.</td><td>1–7 (Agree-Disagree)</td></tr><tr><td>Intention3</td><td>I would copy software without authorization.</td><td>I would travel to Mainland China or Macau in the coming year.</td><td>1–7 (Agree-Disagree)</td></tr><tr><td>Behavior1</td><td>How much computer application software that you use is pirated?</td><td>How often do you take public transportation?</td><td>1–7 (None-All)</td></tr><tr><td>Behavior2</td><td>How much computer application software that you give to others is pirated?</td><td>How often would you have rice for dinner?</td><td>1–7 (None-All)</td></tr><tr><td>Behavior3</td><td>How much computer application software that you copy is pirated?</td><td>How often do you spend your weekend with your family?</td><td>1–7 (None-All)</td></tr></table>

As with the choice of probability values, the problem of choosing sample sizes can be framed as choosing N and k to minimize the sampling variance. Appendix C provides a detailed analysis of the effects of N and k on $\mathrm { v a r } ( \hat { \mu } _ { X } )$ . Confirming our expectation, sampling variance decreases as the total sample size N increases. On the other hand, Equation (C5) in Appendix C shows that the optimal choice of k depends on four factors: the sample variances of the observed responses $( \mathrm { i . e . , ~ \ v a r } ( Z _ { ( 1 ) } )$ and $\mathrm { v a r } ( Z _ { ( 2 ) } ) )$ as well as the probability values chosen. All of these factors are positively related to the optimal sample size.<sup>6</sup>

## 3.5. Study 1: Piracy Attitudes, Intentions, and Behavior

The estimators presented in §3.1 were tested in a self-administered online survey (Study 1) on software piracy. Study 1 was also intended to verify whether or not the unrelated question design is operationally feasible in an uncontrolled online environment. The domain of Study 1 included a set of sensitive questions about a respondent’s attitudes, intentions, and behaviors pertaining to software piracy, though this pejorative term was avoided in the questions posed. Three versions of the online questionnaire were prepared. Direct questioning (DQ) was used in the first version while the second and third utilized RRT. In all three versions, the academic nature of the study as well as strict respondent confidentiality was emphasized. The ordering of questions was the same for all three versions. Table 1 shows the set of sensitive questions as well as their paired innocuous questions.

An important consideration for choosing innocuous questions is respondent privacy, that is, earning complete trust by respondents. Those who answer the sensitive question and admit sensitive attributes must not be easily identifiable from their observed responses. For example, consider the question pair for “behavior3” in Table 1. An honest answer to the sensitive question, say $" 7 , "$ essentially admits piracy behavior. On the other hand, we anticipated that it is common to have the answer $" 7 "$ to the innocuous question $( \mathrm { i . e . , }$ always spending one’s weekend with one’s family). Therefore, even observing a response of $" 7 "$ does not make the respondent appear to have admitted to committing software piracy.

Also, all innocuous questions were selected by three researchers who judged them to be unrelated to the sensitive questions. A small-scale pretest was then conducted to determine if there was any significant correlation between answers to the sensitive and innocuous questions. Inappropriate innocuous questions were pruned.

Because Study 1 was self-administered and conducted online, the private random choice procedure presented a special challenge. It was accomplished with a two-step procedure. First, respondents were asked to select a number between one and four and keep it to themselves. Second, the online questionnaire system generated a random number between one and four. Depending on whether the generated random number matched their privately selected number, respondents were instructed to answer either the sensitive or the innocuous question.

In the second survey, the probability of answering the sensitive question was set to $0 . 2 5 \ : ( p _ { ( 1 ) } = 0 . 2 5 )$ . This was achieved by instructing respondents to answer the sensitive question only when the generated random number matched their privately selected number. In the third version, the probability was set to 0.75 $( p _ { ( 2 ) } = 0 . 7 5 )$ and respondents were instructed to answer the innocuous question only when the generated random number did not match their privately selected number.

A total of 714 respondents were recruited from members of a public portal site in Hong Kong and assigned to one of the three trials: 124 to the first trial; 474 to the second; and 116 to the third. Posthoc analysis based on the findings in Appendix B showed that such a ratio achieves relatively satisfactory efficiency in data collection. All respondents to the second and third questionnaires were required to confirm that they understood the RRT procedure before they were allowed to proceed.

Using Equations (2), (6), and (4), the mean estimator for each sensitive question and its sampling variance as well as the probability distribution of sensitive answers could be determined as follows:

$$
\hat {\mu} _ {X} = 1. 5 \bar {Z} _ {(2)} - 0. 5 \bar {Z} _ {(1)},\tag{10}
$$

$$
\mathrm{var} (\hat {\mu} _ {X}) = 2. 2 5 \frac {S _ {Z _ {(2)}} ^ {2}}{1 1 6} + 0. 2 5 \frac {S _ {Z _ {(1)}} ^ {2}}{4 7 4},\tag{11}
$$

$$
\operatorname * {P r} [ X = m ] = 1. 5 \operatorname * {P r} [ Z _ {(2)} = m ] - 0. 5 \operatorname * {P r} [ Z _ {(1)} = m ].\tag{12}
$$

## 3.6. Differences Between Direct and Randomized Responses

The estimated means based on direct responses (i.e., answers to the first questionnaire) and randomized responses (i.e., answers to the second and third questionnaires) are shown in Table 2. There was no significant difference between the means estimated from the direct and randomized responses to the nonsensitive control question. This helps to allay the concern that using RRT might introduce method bias. Through the sensitive questions about piracy attitudes, intentions, and behavior, statistically significant differences between direct and RRT responses were observed in most cases. More specifically, respondents in the randomized response groups expressed significantly less guilt about piracy (i.e., “attitude 1”) and less agreement that harm was being done through piracy (i.e., “attitude 3”) than those who responded directly. RRT respondents admitted significantly higher software piracy intentions (“intentions 1 to 3”) and dealt with pirated software more often (“behaviors 1 to 3”) than did their directly questioned counterparts.

Table 2 Estimated Means Based on Direct and Randomized Responses (Study 1)

<table><tr><td>Variable</td><td>Mean (RRT)</td><td>Mean (DQ)</td><td>Means diff. (RRT – DQ)</td><td>Student&#x27;s T</td><td>p-value</td><td>Standard error (RRT)</td><td>S.E. (DQ)</td></tr><tr><td>Control</td><td>2.797</td><td>2.347</td><td>0.4509</td><td>1.7957</td><td>0.0735</td><td>0.2503</td><td>0.0207</td></tr><tr><td>Attitude1</td><td>3.823</td><td>4.535</td><td>-0.7115</td><td>-2.9819</td><td>0.0031</td><td>0.2373</td><td>0.0245</td></tr><tr><td>Attitude2</td><td>3.885</td><td>3.901</td><td>-0.0157</td><td>-0.0688</td><td>0.9452</td><td>0.2274</td><td>0.0193</td></tr><tr><td>Attitude3</td><td>3.844</td><td>4.733</td><td>-0.8883</td><td>-4.1645</td><td>0.0000</td><td>0.2127</td><td>0.0164</td></tr><tr><td>Intention1</td><td>3.647</td><td>4.752</td><td>-1.1053</td><td>-4.8197</td><td>0.0000</td><td>0.2278</td><td>0.0264</td></tr><tr><td>Intention2</td><td>3.784</td><td>5.050</td><td>-1.2658</td><td>-5.3363</td><td>0.0000</td><td>0.2356</td><td>0.0274</td></tr><tr><td>Intention3</td><td>3.743</td><td>4.931</td><td>-1.1872</td><td>-4.5994</td><td>0.0000</td><td>0.2564</td><td>0.0300</td></tr><tr><td>Behavior1</td><td>3.514</td><td>2.891</td><td>0.6234</td><td>2.2611</td><td>0.0245</td><td>0.2742</td><td>0.0287</td></tr><tr><td>Behavior2</td><td>3.975</td><td>2.505</td><td>1.4696</td><td>4.9793</td><td>0.0000</td><td>0.2937</td><td>0.0288</td></tr><tr><td>Behavior3</td><td>3.646</td><td>2.554</td><td>1.0912</td><td>3.8197</td><td>0.0002</td><td>0.2842</td><td>0.0286</td></tr></table>

Judging from the directions of the differences, a general pattern of underreporting of software piracy attitudes, intentions, and behaviors is found in the direct response group when compared with the two randomized groups. These distortions appear to be more serious in self-reports of intentions and behavior compared with attitudes toward pirated software. Table 3 shows the estimated distribution of the underlying responses. In general, RRT respondents showed greater willingness to report politically incorrect or illegal attitudes, intentions, and behaviors.

These findings support the use of RRT as a measure to reduce response distortion in surveys on sensitive topics such as software piracy. One may argue that underreporting of sensitive attitudes, intentions, and behaviors is expected even without resorting to RRT. However, estimating to what extent such underreporting may lead to distortions in causal relationships is not a trivial matter, especially when the extent of the distortions differs across different variables.

Table 3 Percentages of Responses by the DQ and Combined RRT Groups (Study 1)

<table><tr><td></td><td>1(%)</td><td>2(%)</td><td>3(%)</td><td>4(%)</td><td>5(%)</td><td>6(%)</td><td>7(%)</td><td>≤3(%)</td><td>4(%)</td><td>≥5(%)</td></tr><tr><td colspan="11">DQ group</td></tr><tr><td>Control</td><td>37</td><td>28</td><td>13</td><td>15</td><td>5</td><td>1</td><td>2</td><td>8</td><td>15</td><td>77</td></tr><tr><td>Attitude1</td><td>5</td><td>6</td><td>12</td><td>27</td><td>18</td><td>24</td><td>9</td><td>50</td><td>27</td><td>23</td></tr><tr><td>Attitude2</td><td>8</td><td>10</td><td>10</td><td>41</td><td>23</td><td>6</td><td>3</td><td>32</td><td>41</td><td>28</td></tr><tr><td>Attitude3</td><td>0</td><td>3</td><td>11</td><td>37</td><td>21</td><td>17</td><td>12</td><td>50</td><td>37</td><td>14</td></tr><tr><td>Intention1</td><td>2</td><td>4</td><td>17</td><td>32</td><td>7</td><td>17</td><td>22</td><td>46</td><td>32</td><td>23</td></tr><tr><td>Intention2</td><td>2</td><td>3</td><td>14</td><td>26</td><td>10</td><td>16</td><td>30</td><td>55</td><td>26</td><td>19</td></tr><tr><td>Intention3</td><td>3</td><td>3</td><td>16</td><td>28</td><td>8</td><td>12</td><td>31</td><td>50</td><td>28</td><td>22</td></tr><tr><td>Behavior1</td><td>28</td><td>25</td><td>11</td><td>13</td><td>15</td><td>9</td><td>0</td><td>24</td><td>13</td><td>63</td></tr><tr><td>Behavior2</td><td>47</td><td>13</td><td>8</td><td>14</td><td>14</td><td>5</td><td>0</td><td>19</td><td>14</td><td>67</td></tr><tr><td>Behavior3</td><td>43</td><td>17</td><td>7</td><td>17</td><td>10</td><td>7</td><td>0</td><td>17</td><td>17</td><td>66</td></tr><tr><td colspan="11">RRT group</td></tr><tr><td>Control</td><td>23</td><td>33</td><td>15</td><td>13</td><td>7</td><td>5</td><td>4</td><td>16</td><td>13</td><td>71</td></tr><tr><td>Attitude1</td><td>6</td><td>19</td><td>25</td><td>12</td><td>21</td><td>15</td><td>4</td><td>39</td><td>12</td><td>49</td></tr><tr><td>Attitude2</td><td>9</td><td>6</td><td>21</td><td>33</td><td>18</td><td>7</td><td>6</td><td>30</td><td>33</td><td>36</td></tr><tr><td>Attitude3</td><td>7</td><td>9</td><td>23</td><td>32</td><td>17</td><td>10</td><td>3</td><td>30</td><td>32</td><td>38</td></tr><tr><td>Intention1</td><td>11</td><td>13</td><td>20</td><td>26</td><td>19</td><td>7</td><td>4</td><td>30</td><td>26</td><td>44</td></tr><tr><td>Intention2</td><td>6</td><td>18</td><td>18</td><td>31</td><td>10</td><td>8</td><td>8</td><td>26</td><td>31</td><td>42</td></tr><tr><td>Intention3</td><td>9</td><td>19</td><td>19</td><td>23</td><td>8</td><td>12</td><td>9</td><td>29</td><td>23</td><td>48</td></tr><tr><td>Behavior1</td><td>19</td><td>23</td><td>3</td><td>17</td><td>22</td><td>17</td><td>0</td><td>39</td><td>17</td><td>44</td></tr><tr><td>Behavior2</td><td>27</td><td>9</td><td>5</td><td>4</td><td>21</td><td>24</td><td>11</td><td>55</td><td>4</td><td>40</td></tr><tr><td>Behavior3</td><td>25</td><td>17</td><td>3</td><td>8</td><td>16</td><td>27</td><td>2</td><td>46</td><td>8</td><td>46</td></tr></table>

The basic model has its limitations because only the first moments of the randomized responses were estimated. It was not possible to estimate the effect sizes of the differences between the direct and randomized responses because computation of Cohen’s d index (Cohen 1988) requires variance in the randomized responses. To address this, the basic model was extended to multivariate analysis for a large-scale empirical study on software piracy in which causal relationships were considered.

## 4. Multivariate Analysis

Assume that there are two sensitive questions $q _ { X _ { 1 } }$ and $q _ { X _ { 2 } }$ in a survey. They are paired with two unrelated and innocuous questions $q _ { Y _ { 1 } }$ and $q _ { Y _ { 2 } . }$ , respectively. The design dictates that the set of sensitive questions are unrelated to the set of innocuous questions. Denote $Z _ { 1 }$ and $Z _ { 2 }$ as the observed responses, $X _ { 1 }$ and $X _ { 2 }$ as the underlying responses to $q _ { X _ { 1 } }$ and $q _ { X _ { 2 } } ,$ , and $Y _ { 1 }$ and $Y _ { 2 }$ as the underlying responses to $q _ { Y _ { 1 } }$ and $q _ { Y _ { 2 } }$ . By design, these random variables are related in the following way:

$$
\left\{ \begin{array}{l} Z _ {1 (1)} = I _ {1 (1)} X _ {1} + (1 - I _ {1 (1)}) Y _ {1} \\ Z _ {2 (1)} = I _ {2 (1)} X _ {2} + (1 - I _ {2 (1)}) Y _ {2} \\ Z _ {1 (2)} = I _ {1 (2)} X _ {1} + (1 - I _ {1 (2)}) Y _ {1} \\ Z _ {2 (2)} = I _ {2 (2)} X _ {2} + (1 - I _ {2 (2)}) Y _ {2}, \end{array} \right.\tag{13}
$$

where ${ \cal I } _ { 1 ( 1 ) } , { \cal I } _ { 2 ( 1 ) } , { \cal I } _ { 1 ( 2 ) } ,$ , and $I _ { 2 ( 2 ) }$ are independent indicator variables such that

$$
\begin{array}{c} I _ {1 (1)}, I _ {2 (1)} = \left\{ \begin{array}{l l} 1 & \text {with probability p_{(1)}} \\ 0 & \text {with probability 1 - p_{(1)}} \end{array} \right., \\ I _ {1 (2)}, I _ {2 (2)} = \left\{ \begin{array}{l l} 1 & \text {with probability p_{(2)}} \\ 0 & \text {with probability 1 - p_{(2)}} \end{array} \right. \\ p _ {(1)} \neq p _ {(2)}. \end{array}
$$

and

## 4.1. Method-of-Moments Estimators

Equation (13) is an extended multivariate model for the unrelated question design. It facilitates the use of the method of moments to obtain estimators for population variances and covariances of the underlying responses in terms of the sample statistics of the observed responses.

Proposition 3. The method-of-moments estimators for the population variances and covariances of the underlying variables $X _ { 1 } , X _ { 2 } , Y _ { 1 }$ , and $Y _ { 2 }$ are

$$
\begin{array}{r l} \hat {\sigma} _ {X _ {i}} ^ {2} = & ((p _ {(1)} - p _ {(2)}) [ (1 - p _ {(2)}) S _ {Z _ {i (1)}} ^ {2} - (1 - p _ {(1)}) S _ {Z _ {i (2)}} ^ {2} ] \\ & - (1 - p _ {(1)}) (1 - p _ {(2)}) (\bar {Z} _ {i (1)} - \bar {Z} _ {i (2)}) ^ {2}) \\ & \cdot ((p _ {(1)} - p _ {(2)}) ^ {2}) ^ {- 1} \quad i = 1, 2 \end{array}\tag{14}
$$

$$
\hat {\sigma} _ {Y _ {i}} ^ {2} = \frac {(p _ {(1)} - p _ {(2)}) (p _ {(1)} S _ {Z _ {i (2)}} ^ {2} - p _ {(2)} S _ {Z _ {i (1)}} ^ {2}) - p _ {(1)} p _ {(2)} (\bar {Z} _ {i (1)} - \bar {Z} _ {i (2)}) ^ {2}}{(p _ {(1)} - p _ {(2)}) ^ {2}}
$$

$$
i = 1, 2\tag{15}
$$

$$
\hat {\sigma} _ {X _ {1} X _ {2}} ^ {2} = \frac {(1 - p _ {(2)}) ^ {2} S _ {Z _ {1 (1)} Z _ {2 (1)}} ^ {2} - (1 - p _ {(1)}) ^ {2} S _ {Z _ {1 (2)} Z _ {2 (2)}} ^ {2}}{(p _ {(1)} + p _ {(2)} - 2 p _ {(1)} p _ {(2)}) (p _ {(1)} - p _ {(2)})}\tag{16}
$$

$$
\hat {\sigma} _ {Y _ {1} Y _ {2}} ^ {2} = \frac {p _ {(1)} ^ {2} S _ {Z _ {1 (2)} Z _ {2 (2)}} ^ {2} - p _ {(2)} ^ {2} S _ {Z _ {1 (1)} Z _ {2 (1)}} ^ {2}}{(p _ {(1)} + p _ {(2)} - 2 p _ {(1)} p _ {(2)}) (p _ {(1)} - p _ {(2)})}.\tag{17}
$$

The proof of Proposition 3 is in Appendix A.

## 4.2. Covariance Between a Randomized Response and a Direct Response

The above covers two sensitive items in the same survey that were measured using RRT. In practice, it is also common to have other nonsensitive items in the same survey, and these nonsensitive items are measured by direct questioning rather than RRT. Assume $q _ { X _ { 3 } }$ to be a nonsensitive question that is asked directly in the same survey that deploys RRT for another sensitive question $q _ { X _ { 1 } }$ . Denote $X _ { 3 }$ as the observed response to $q _ { X _ { 3 } }$ and $p$ as the probability of answering the sensitive question $q _ { X _ { 1 } } . ^ { 7 }$ By design,

$$
\begin{array}{l} Z _ {1} X _ {3} = [ I X _ {1} + (1 - I) Y _ {1} ] X _ {3}, \\ \text { where } I = \left\{ \begin{array}{l l} 1 & \text { with   probability } p \\ 0 & \text { with   probability } 1 - p. \end{array} \right. \end{array}\tag{18}
$$

Proposition 4. The method-of-moments estimator for the population covariance between $X _ { 1 }$ and $X _ { 3 }$ is their sample covariance divided by p:

$$
\hat {\sigma} _ {X _ {1} X _ {3}} ^ {2} = \frac {S _ {Z _ {1} X _ {3}} ^ {2}}{p}.\tag{19}
$$

The proof of Proposition 4 is shown in Appendix A. To recap, starting with a representation of the relationships among the random variables using indicator variables, we have developed method-of-moments estimators for the means, variances, and covariances for any two variables (direct or randomized responses). A covariance matrix can thus be constructed based on the estimation of variance terms and the pairwise estimation of covariance terms. Such a matrix can be used to perform various multivariate analyses.

## 4.3. Study 2: Determinants of Piracy Attitudes, Intentions, and Behaviors

Study 2 was a large-scale online survey examining the determinants of software piracy behavior using a causal modeling framework. Recent work by Peace et al. (2003) on software piracy was adapted to produce the simplified causal model for Study 2 as depicted in Figure 1. It is important to note that the current analysis was not intended to validate or refute existing theories on piracy attitude. Rather, the adapted Peace et al. (2003) model was used to illustrate RRT’s applicability in structural equation modeling (SEM) analysis.

The causal model incorporated four constructs, all of which except for “piracy behavior” were measured by items adapted from Peace et al. (2003) (shown in Appendix D). The additional construct “piracy behav-$\mathrm { i o r ^ { \prime \prime } }$ was measured using three items refined from Study 1. The items measuring “attitude” and “piracy behavior” were considered sensitive and were paired with innocuous questions. The other two constructs were not. As in to Study 1, these sensitive questions were paired with unrelated and innocuous questions as shown in Table 4.

In this study, three surveys were conducted: one using direct questioning and two using RRT for the sensitive questions. The overall survey administration was similar to Study 1 except that the probability of answering the sensitive question was 0.75 in the second survey and 0.5 in the third.

Figure 1 Causal Model of Software Piracy  
![](/api/attachments/KDR4N6PM/fulltext/images/38a6667605b9ca03687dc580d26b8c7b74329bfb91431168b047d09e5df57a5b.jpg)

Table 4 Pairing of Sensitive and Innocuous Questions (Study 2)

<table><tr><td>Construct/variable</td><td>Sensitive question</td><td>Innocuous question</td><td>Scale</td></tr><tr><td>Control</td><td>E-banking service is safe.</td><td>I will feel ashamed because of my poverty.</td><td>1–7 (Strong disagree–Strong agree)</td></tr><tr><td>Attitude</td><td></td><td></td><td></td></tr><tr><td>1</td><td>To me, unauthorized copying of software is:</td><td>I find detective stories:</td><td>1–7 (Very unattractive–Very attractive)</td></tr><tr><td>2</td><td>To me, unauthorized copying of software is:</td><td>To me, taking vitamin pills every day is:</td><td>1–7 (Very harmful–Very beneficial)</td></tr><tr><td>3</td><td>To me, unauthorized copying of software is:</td><td>I find recording daily expenses in detail is:</td><td>1–7 (Very foolish–Very wise)</td></tr><tr><td>Piracy behavior</td><td></td><td></td><td></td></tr><tr><td>1</td><td>Among the software that I often use, most are copied without authorization.</td><td>I often take public transportation.</td><td>1–7 (Strong disagree–Strong agree)</td></tr><tr><td>2</td><td>I often copy the software that I want without authorization.</td><td>I often have dinner at home.</td><td>1–7 (Strong disagree–Strong agree)</td></tr><tr><td>3</td><td>I have a lot of software that was copied without authorization.</td><td>I like holidays.</td><td>1–7 (Strong disagree–Strong agree)</td></tr></table>

Respondents in Study 2 were members of a Hong Kong government website.<sup>8</sup> Participation in a lucky draw was offered as an incentive for participation to those who finished the online questionnaire. Participants were unaware of the topic of the study at the time of recruitment and were randomly assigned to one of the three online surveys in the ratio of 1:1.5:1.5. Posthoc analysis based on the findings in Appendix C showed that such a ratio achieves relatively satisfactory efficiency in data collection. A total of 3,896 complete and valid responses<sup>9</sup> were received—1,002 to the first survey, 1,449 to the second, and 1,445 to the third $( p _ { ( 1 ) } = 0 . 7 5 , \ n _ { ( 1 ) } = 1 , 4 4 9$ and $p _ { ( 2 ) } = 0 . 5 ,$ $n _ { ( 2 ) } = 1 , 4 4 5 )$

The corresponding method-of-moments estimators based on Equations (2), (14), (16), and (19) are shown below. These estimators were used to construct a covariance matrix from the randomized responses:

$$
\hat {\mu} _ {X _ {1}} = 2 \bar {Z} _ {1 (1)} - \bar {Z} _ {1 (2)}\tag{20}
$$

$$
\hat {\sigma} _ {X _ {1}} ^ {2} = 2 S _ {Z _ {1 (1)}} ^ {2} - S _ {Z _ {1 (2)}} ^ {2} - 2 (\bar {Z} _ {1 (2)} - \bar {Z} _ {1 (1)}) ^ {2}\tag{21}
$$

$$
\hat {\sigma} _ {X _ {1} X _ {2}} ^ {2} = 2 S _ {Z _ {1 (1)} Z _ {2 (1)}} ^ {2} - 0. 5 S _ {Z _ {1 (2)} Z _ {2 (2)}} ^ {2}\tag{22}
$$

$$
\hat {\sigma} _ {X _ {1} X _ {3}} ^ {2} = \frac {4}{3} S _ {Z _ {1 (1)} X _ {3 (1)}} ^ {2} \quad (\text { the   first   sample   with }
$$

$$
\text { a   larger   probability   is   used }).\tag{23}
$$

All participants who responded using RRT were presented with a concise explanation of the rationale behind RRT and an illustration of how it should be applied in the survey. A two-step procedure similar to that outlined for Study 1 was deployed. $p _ { ( 2 ) } = 0 . 5$ was used for the third survey. Respondents were first asked to select either one or two and keep it to themselves. The online questionnaire system then randomly generated either a one or a two and respondents were instructed to answer the sensitive or innocuous question depending on whether or not the generated random number matched their privately selected number. All respondents to RRT questionnaires were required to confirm that they understood the RRT procedure before they were allowed to proceed.

Table 5 Estimated Statistics for the Direct (DQ) and Randomized (RRT) Responses (Study 2)

<table><tr><td>Construct/variable</td><td>Mean (RRT)</td><td>Mean (DQ)</td><td>Means diff. (RRT – DQ)</td><td>Student&#x27;s T</td><td>p-value</td><td>S.E. (RRT)</td><td>S.E. (DQ)</td><td>Var (RRT)</td><td>Var (DQ)</td><td>Cohen&#x27;s d</td></tr><tr><td>Control</td><td>4.035</td><td>4.065</td><td>-0.0302</td><td>-0.3234</td><td>0.7464</td><td>0.0934</td><td>0.0023</td><td>2.3221</td><td>2.2685</td><td>0.0200</td></tr><tr><td>Attitude</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>4.373</td><td>4.127</td><td>0.2458</td><td>2.7449</td><td>0.0061</td><td>0.0895</td><td>0.0021</td><td>2.5722</td><td>2.1048</td><td>0.1607</td></tr><tr><td>2</td><td>3.831</td><td>3.556</td><td>0.2755</td><td>3.0775</td><td>0.0021</td><td>0.0895</td><td>0.0021</td><td>2.5433</td><td>2.0973</td><td>0.1809</td></tr><tr><td>3</td><td>3.802</td><td>3.527</td><td>0.2753</td><td>3.3184</td><td>0.0009</td><td>0.0830</td><td>0.0013</td><td>1.7312</td><td>1.3105</td><td>0.2233</td></tr><tr><td>Piracy behavior</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>4.127</td><td>3.369</td><td>0.7582</td><td>6.7837</td><td>0.0000</td><td>0.1117</td><td>0.0023</td><td>3.4030</td><td>2.2991</td><td>0.4490</td></tr><tr><td>2</td><td>3.538</td><td>3.051</td><td>0.4876</td><td>4.5231</td><td>0.0000</td><td>0.1078</td><td>0.0021</td><td>3.0951</td><td>2.0963</td><td>0.3026</td></tr><tr><td>3</td><td>3.946</td><td>2.942</td><td>1.0036</td><td>8.4848</td><td>0.0000</td><td>0.1183</td><td>0.0019</td><td>3.6313</td><td>1.9427</td><td>0.6012</td></tr></table>

## 4.4. Differences Between Direct and Randomized Responses

The estimated means and variances of the randomized and direct responses are shown in Table 5. As in Study 1, there was no statistically significant difference for the nonsensitive control question, but statistically significant differences were observed for the sensitive questions on piracy attitudes and behavior. Cohen’s d effect size indices (Cohen 1988) were calculated by $| \hat { \mu } _ { \mathrm { R R T } } - \hat { \mu } _ { \mathrm { D Q } } | / \sqrt { ( \hat { \sigma } _ { \mathrm { R R T } } ^ { 2 } + \hat { \sigma } _ { \mathrm { D Q } } ^ { 2 } ) / 2 }$ , where $\hat { \mu } _ { \scriptscriptstyle \mathrm { R R T } } ,$ $\hat { \mu } _ { \mathrm { D Q } } ,$ $\widehat { \sigma } _ { \mathrm { R R T } } ^ { 2 } ,$ and $ { \hat { \sigma } } _ { \mathrm { D Q } } ^ { 2 }$ are the mean and variance estimates for the RRT and DQ groups, respectively.

Table 5 shows that the effects for the attitude items are mostly small (i.e., around 0.2) whereas those for actual piracy behaviors approach medium size (i.e., around 0.5). Respondents giving randomized responses described software piracy as significantly more beneficial and attractive than did those who responded directly. The former also claimed to deal with pirated software significantly more than did the latter. Consistent with Study 1, a larger discrepancy was observed in self-reports of behaviors as compared to attitudes. This could be explained by a higher perceived threat of sanctions resulting from admitting to having behaved in a certain way compared to the mere expression of an attitude.

Table 6 compares the estimated distributions of the underlying responses for the RRT groups with those of the direct respondents. In general, responses estimated for the RRT groups showed a greater tendency to report sensitive attitudes and behavior.

Table 6 Percentages of Responses for the DQ and Combined RRT Groups (Study 2)

<table><tr><td></td><td>1 (%)</td><td>2 (%)</td><td>3 (%)</td><td>4 (%)</td><td>5 (%)</td><td>6 (%)</td><td>7 (%)</td><td>≤3 (%)</td><td>4 (%)</td><td>≥5 (%)</td></tr><tr><td colspan="11">DQ group</td></tr><tr><td>Control</td><td>4</td><td>14</td><td>23</td><td>15</td><td>24</td><td>20</td><td>1</td><td>40</td><td>15</td><td>45</td></tr><tr><td colspan="11">Attitude</td></tr><tr><td>1</td><td>4</td><td>14</td><td>7</td><td>33</td><td>23</td><td>16</td><td>2</td><td>26</td><td>33</td><td>42</td></tr><tr><td>2</td><td>6</td><td>25</td><td>15</td><td>30</td><td>14</td><td>9</td><td>1</td><td>45</td><td>30</td><td>25</td></tr><tr><td>3</td><td>5</td><td>17</td><td>13</td><td>54</td><td>7</td><td>3</td><td>1</td><td>35</td><td>54</td><td>11</td></tr><tr><td colspan="11">Piracy behavior</td></tr><tr><td>1</td><td>9</td><td>29</td><td>13</td><td>24</td><td>15</td><td>8</td><td>1</td><td>51</td><td>24</td><td>24</td></tr><tr><td>2</td><td>11</td><td>35</td><td>15</td><td>21</td><td>11</td><td>5</td><td>1</td><td>62</td><td>21</td><td>17</td></tr><tr><td>3</td><td>13</td><td>36</td><td>14</td><td>23</td><td>10</td><td>3</td><td>1</td><td>63</td><td>23</td><td>14</td></tr><tr><td colspan="11">RRT group</td></tr><tr><td>Control</td><td>4</td><td>17</td><td>14</td><td>20</td><td>26</td><td>16</td><td>2</td><td>36</td><td>20</td><td>44</td></tr><tr><td colspan="11">Attitude</td></tr><tr><td>1</td><td>4</td><td>15</td><td>6</td><td>19</td><td>27</td><td>23</td><td>5</td><td>26</td><td>19</td><td>55</td></tr><tr><td>2</td><td>7</td><td>18</td><td>17</td><td>24</td><td>19</td><td>11</td><td>5</td><td>41</td><td>24</td><td>34</td></tr><tr><td>3</td><td>5</td><td>12</td><td>16</td><td>42</td><td>16</td><td>6</td><td>2</td><td>33</td><td>42</td><td>25</td></tr><tr><td colspan="11">Piracy behavior</td></tr><tr><td>1</td><td>8</td><td>19</td><td>9</td><td>17</td><td>19</td><td>16</td><td>11</td><td>36</td><td>17</td><td>46</td></tr><tr><td>2</td><td>11</td><td>27</td><td>14</td><td>14</td><td>14</td><td>15</td><td>3</td><td>52</td><td>14</td><td>33</td></tr><tr><td>3</td><td>11</td><td>19</td><td>13</td><td>15</td><td>17</td><td>14</td><td>11</td><td>43</td><td>15</td><td>42</td></tr></table>

Table 7 Covariance Matrix for the DQ Group

<table><tr><td>N=1,002</td><td>Cost1</td><td>Cost2</td><td>Cost3</td><td>Cert1</td><td>Cert2</td><td>Att1</td><td>Att2</td><td>Att3</td><td>Behave1</td><td>Behave2</td><td>Behave3</td></tr><tr><td>Cost1</td><td>1.12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost2</td><td>0.68</td><td>1.64</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost3</td><td>0.56</td><td>0.55</td><td>1.04</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cert1</td><td>-0.19</td><td>-0.16</td><td>-0.16</td><td>2.06</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cert2</td><td>-0.11</td><td>-0.18</td><td>-0.08</td><td>0.74</td><td>1.35</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Att1</td><td>0.33</td><td>0.24</td><td>0.29</td><td>-0.65</td><td>-0.43</td><td>2.10</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Att2</td><td>0.23</td><td>0.25</td><td>0.19</td><td>-0.73</td><td>-0.50</td><td>1.20</td><td>2.10</td><td></td><td></td><td></td><td></td></tr><tr><td>Att3</td><td>0.23</td><td>0.23</td><td>0.20</td><td>-0.58</td><td>-0.47</td><td>0.89</td><td>1.09</td><td>1.31</td><td></td><td></td><td></td></tr><tr><td>Behave1</td><td>0.27</td><td>0.18</td><td>0.28</td><td>-0.63</td><td>-0.39</td><td>1.05</td><td>1.27</td><td>0.92</td><td>2.30</td><td></td><td></td></tr><tr><td>Behave2</td><td>0.25</td><td>0.14</td><td>0.23</td><td>-0.66</td><td>-0.31</td><td>0.93</td><td>1.17</td><td>0.88</td><td>1.58</td><td>2.09</td><td></td></tr><tr><td>Behave3</td><td>0.21</td><td>0.12</td><td>0.18</td><td>-0.59</td><td>-0.36</td><td>0.81</td><td>1.08</td><td>0.90</td><td>1.54</td><td>1.57</td><td>1.94</td></tr></table>

4.5. Pairwise Construction of a Covariance Matrix A total of 11 items were used to measure the 4 constructs in the model shown in Figure 1. Table 7 shows the sample covariance matrix based on data from the first survey in which only direct questioning was used (the DQ group).

The estimators in Equations (21), (22), and (23) were used to estimate the variance terms and pairwise covariance terms for the sensitive items in the second and third surveys (the RRT groups). For nonsensitive items, the corresponding direct responses in the two surveys were pooled. The resulting covariance matrix is shown in Table 8. A potential problem in pairwise construction of the covariance matrix is that the resulting matrix may not be positivedefinite due to sampling errors in the component terms. A nonpositive-definite covariance matrix essentially indicates internal contradictions among the component terms and poses difficulties in multivariate analysis (Wothke 1993). In general, the chance of encountering such a problem can be minimized if the sampling error associated with each term in the matrix is small, which is usually achievable by increasing the sample size. In this study, fairly large samples were used for the RRT group and the covariance matrix constructed by pairwise estimation was verified to be positive-definite and suitable for use in multivariate analysis.

## 4.6. Causal Modeling Based on Direct Questioning and RRT

With the above covariance matrices, the model in Figure 1 was empirically tested using covariance-based

Table 8 Covariance Matrix by Pairwise Estimation (RRT Group)

<table><tr><td>N=1,809</td><td>Cost1</td><td>Cost2</td><td>Cost3</td><td>Cert1</td><td>Cert2</td><td>Att1</td><td>Att2</td><td>Att3</td><td>Behave1</td><td>Behave2</td><td>Behave3</td></tr><tr><td>Cost1</td><td>1.19</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost2</td><td>0.69</td><td>1.52</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost3</td><td>0.67</td><td>0.61</td><td>1.12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cert1</td><td>-0.27</td><td>-0.21</td><td>-0.23</td><td>2.10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cert2</td><td>-0.15</td><td>-0.25</td><td>-0.11</td><td>0.82</td><td>1.43</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Att1</td><td>0.44</td><td>0.34</td><td>0.27</td><td>-0.71</td><td>-0.50</td><td>2.56</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Att2</td><td>0.37</td><td>0.34</td><td>0.19</td><td>-0.73</td><td>-0.31</td><td>1.27</td><td>2.54</td><td></td><td></td><td></td><td></td></tr><tr><td>Att3</td><td>0.38</td><td>0.30</td><td>0.23</td><td>-0.71</td><td>-0.38</td><td>0.95</td><td>1.15</td><td>1.72</td><td></td><td></td><td></td></tr><tr><td>Behave1</td><td>0.48</td><td>0.29</td><td>0.31</td><td>-0.63</td><td>-0.20</td><td>1.19</td><td>0.96</td><td>0.95</td><td>3.38</td><td></td><td></td></tr><tr><td>Behave2</td><td>0.31</td><td>0.29</td><td>0.26</td><td>-0.73</td><td>-0.25</td><td>1.11</td><td>1.35</td><td>1.16</td><td>2.10</td><td>3.09</td><td></td></tr><tr><td>Behave3</td><td>0.40</td><td>0.27</td><td>0.33</td><td>-0.79</td><td>-0.41</td><td>1.04</td><td>1.21</td><td>1.12</td><td>1.87</td><td>2.09</td><td>3.63</td></tr></table>

Note. Bold figures were estimated using the method-of-moments estimators in Equations (12), (14), and (17).

![](/api/attachments/KDR4N6PM/fulltext/images/777e381273c4ebfcb85000615f4c28a3e8ae8baa4a238d2afe20f1bb2eb38aa2.jpg)

Figure 2 Causal Modeling Results Using the DQ and RRT Samples

<table><tr><td>DQ sample</td><td>RRT sample</td></tr><tr><td> $\chi^2=120.31 df=40 n=1,002$ </td><td> $\chi^2=278.89 df=40 n=1,809$ </td></tr><tr><td>RMSEA = 0.045 90%-CI = (0.036, 0.054)</td><td>RMSEA = 0.057 90%-CI = (0.051,0.064)</td></tr><tr><td>NFI = 0.98 NNFI = 0.99 CFI = 0.99</td><td>NFI = 0.97 NNFI = 0.97 CFI = 0.98</td></tr><tr><td>GFI = 0.98 AGFI = 0.96</td><td>GFI = 0.97 AGFI = 0.95</td></tr></table>

Note. Figures in shade are for RRT sample.

SEM.<sup>10</sup> Figure 2 shows the results for the DQ and RRT groups. It also presents overall model fit statistics as well as standardized path loadings. Assessment of the overall model fit was based primarily on the 90% confidence interval (CI) for the root mean square of error approximation (RMSEA) of the approximate fit statistics, as recommended by Mac-Callum et al. (1996).<sup>11</sup> This was supplemented by a number of heuristics-based descriptive fit indices suggested by Gefen et al. (2000) for IS research. In both groups, the 90% CI fell below the 0.08 threshold, indicating a fair model fit (Browne and Cudeck 1993). The descriptive fit indices, including the network fit index (NFI), goodness-of-fit index (GFI), and adjusted goodness-of-fit-index (AGFI), were higher than the recommended 0.90 or 0.80 levels (Gefen et al. 2000, Hu and Bentler 1999), indicating satisfactory overall model fit.

Table 9 shows the composite reliabilities and average variance explained (AVE) for both groups. The composite reliabilities of most constructs were above 0.7, suggesting satisfactory internal consistency of these constructs.<sup>12</sup>

Though the AVEs of “software cost” and “punishment certainty” fall slightly below 0.5 for the DQ group, all constructs for the RRT group were found to have an AVE equal to or greater than 0.5. This suggests that convergent validities of the concerned constructs are largely acceptable. Discriminant validity was tested by comparing the $\chi ^ { 2 }$ of the original model with an alternative model where the constructs in question are united as one construct (Gefen et al. 2000). We tested all possible pairings of the four constructs and the difference in $\chi ^ { 2 }$ was found to be highly significant in all cases. Overall, the construct validities are regarded as acceptable.

In comparing the effect sizes, note that the relationship between “attitude” and “piracy behavior” is very similar in the DQ group (a standardized path loading of 0.77) and the RRT group (a standardized path loading of 0.74). However, there are more notable differences in the relationships between “punishment certainty” or “software cost” and “attitude.” The standardized relationship of “punishment certainty” was <sub>−</sub>0 58 in the DQ group but <sub>−</sub>0 47 in the RRT group. That of “software cost” was 0.17 in the DQ group and increased to 0.26 in the RRT group.

Table 9 Construct Reliability and Validity (Study 2)

<table><tr><td></td><td colspan="2">Software cost</td><td colspan="2">Punishment certainty</td><td colspan="2">Attitude</td><td colspan="2">Piracy behavior</td></tr><tr><td>Composite reliability</td><td>0.74</td><td>0.77</td><td>0.62</td><td>0.68</td><td>0.82</td><td>0.75</td><td>0.90</td><td>0.82</td></tr><tr><td>AVE</td><td>0.49</td><td>0.52</td><td>0.45</td><td>0.52</td><td>0.60</td><td>0.50</td><td>0.75</td><td>0.61</td></tr><tr><td colspan="9">Interconstruct correlation (diagonal item shows the square root of the AVE of the corresponding construct)</td></tr><tr><td>Software cost</td><td>0.70</td><td>0.72</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Punishment certainty</td><td>-0.21</td><td>-0.24</td><td>0.67</td><td>0.72</td><td></td><td></td><td></td><td></td></tr><tr><td>Attitude</td><td>0.29</td><td>0.37</td><td>-0.61</td><td>-0.53</td><td>0.77</td><td>0.71</td><td></td><td></td></tr><tr><td>Piracy behavior</td><td>0.23</td><td>0.28</td><td>-0.47</td><td>-0.40</td><td>0.77</td><td>0.74</td><td>0.86</td><td>0.78</td></tr></table>

Note. Figures for the RRT group are bold.

To determine if the structural paths of the DQ group and the RRT group do differ significantly, we used multigroup SEM by treating the two groups as two independent samples for fitting against the same theoretical model. We performed two multigroup analyses using different constraints on the structural paths. Structural paths were allowed to vary across the groups in the first analysis but were assumed to be equal in the second one (resulting in eight more degrees of freedom). Because the two analyses are nested, the difference in the “global $\chi ^ { 2 }$ statistics” between the two analyses reveals if the estimated structural paths in the DQ group do differ significantly from those in the RRT group (Steiger et al. 1985). The global $\chi ^ { 2 }$ was found to be 878.26 df 85 for the first analysis and 1,003.04 df 93 for the second one. Because the difference in $\chi ^ { 2 } \left( \Delta \chi ^ { 2 } ( 8 ) = 1 2 4 . 7 8 \right.$ $p < 0 . 0 0 0 1 )$ is highly significant, we conclude that the structural paths do differ significantly across the DQ group and RRT group.

## 5. Discussion

This study empirically examined the use of RRT to solicit truthful self-reports in two empirical studies on software piracy. Comparing direct and randomized responses confirmed consistent underreporting of sensitive attitudes, intentions, and behaviors by respondents using the traditional, direct questioning approach. These findings complement those from previous research (e.g., Armacost et al. 1991) that respondents are more willing to admit to sensitive behaviors with randomized responses. Moreover, responses to the nonsensitive control question deliberately inserted into the two studies showed no significant difference between direct and randomized responses. The feasibility of using RRT in an online survey was also demonstrated.

Although underreporting of sensitive attitudes, intentions, and behaviors could be anticipated in direct questioning, the magnitude of distortion is not clear. It is also unclear to what extent such underreporting may lead to distorted conclusions about causal relationships, especially when the extent of the distortion differs across variables. The results of this study revealed that distortion was less severe when reporting attitudes as opposed to intentions and behaviors. Such differences are reasonable given the higher risk of prosecution, but they may also account for nontrivial and convoluted distortions in research findings. As revealed in Study 2, the influences of attitudes and punishment certainty may be overreported whereas that the effect of cost may be underreported.

These findings have at least two important implications. First, they demonstrate that a covariancebased SEM can be analyzed using data collected using RRT approach. Our results demonstrate how a selfadministered piracy survey can be conducted using the unrelated question design in an online setting. The empirical findings suggest that the RRT is feasible and effective. Second, response distortion was detected in two empirical studies of software piracy using RRT. Our work represents a pioneering effort to provide empirical evidence to substantiate the worries of many previous researchers about response distortion in software piracy research. With better understanding of the extent of response distortion and its effects on causal relationships, efforts to combat piracy could be more precisely directed.

Furthermore, using method-of-moments estimators for variance and covariance allows us to relax two impractical assumptions about the set of innocuous questions. Namely, the model does not assume that these innocuous questions are independent of each other, and it does not presume prior knowledge of the statistical properties of the responses. The results of the two studies demonstrate the feasibility and usefulness of the method. Putting the method to real use has enriched our understanding of its feasibility through tackling issues such as conducting private random choice procedures online and estimating the covariance between direct and randomized responses.

More investigations of the statistical properties (e.g., sampling properties) of the method-of-moments estimators are certainly warranted. Also, the pairwise construction of the covariance matrix can be further improved by a full information estimation<sup>13</sup> approach such that inadmissible solutions can be pruned completely. Researchers are encouraged to consider possible extensions of the current approach and other applications of RRT in the IS domain.

## 6. Conclusions

The results show that response distortion can be a real threat in research on software piracy that relies on self-reports. This problem may not be limited to the domain of software piracy research but may also exist in the context of other sensitive topics such as data privacy, cyberslacking, hacking, online gambling, and pornography viewing. RRT is recommended as a method to tackle response distortion in research related to sensitive topics. In view of its potential, more investigation aimed at improving the application of RRT in IS research is warranted.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their constructive comments on early versions of the paper. The authors are also indebted to the valuable comments and suggestions made by participants in PACIS 2007 and research seminars organized at HKUST. This project was partially funded by a grant from the Business Software Alliance and the Research Center for Electronic Commerce at HKUST.

## Appendix A

Proof of Proposition 1. Taking expectations on both sides of (1) yields the following set of moment equations:

$$
\left\{ \begin{array}{l} E Z _ {(1)} = p _ {(1)} \mu_ {X} + (1 - p _ {(1)}) \mu_ {Y} \\ E Z _ {(2)} = p _ {(2)} \mu_ {X} + (1 - p _ {(2)}) \mu_ {Y}. \end{array} \right.
$$

(A1)

By equating ${ \bar { Z } } _ { ( 1 ) }$ and ${ \bar { Z } } _ { ( 2 ) }$ with the right-hand sides of (A1), we obtain a system of two equations containing the method-of-moments estimators of $\mu _ { X }$ and $\mu _ { Y }$ as follows:

$$
\left\{ \begin{array}{l} \bar {Z} _ {(1)} = p _ {(1)} \hat {\mu} _ {X} + (1 - p _ {(1)}) \hat {\mu} _ {Y} \\ \bar {Z} _ {(2)} = p _ {(2)} \hat {\mu} _ {X} + (1 - p _ {(2)}) \hat {\mu} _ {Y}. \end{array} \right.\tag{A2}
$$

Solving (A2) for $\hat { \mu } _ { X }$ and $\hat { \mu } _ { Y } ,$ we have

$$
\begin{array}{c} \hat {\mu} _ {X} = \frac {(1 - p _ {(2)}) \bar {Z} _ {(1)} - (1 - p _ {(1)}) \bar {Z} _ {(2)}}{p _ {(1)} - p _ {(2)}}, \\ \hat {\mu} _ {Y} = \frac {p _ {(1)} \bar {Z} _ {(2)} - p _ {(2)} \bar {Z} _ {(1)}}{p _ {(1)} - p _ {(2)}}. \end{array}\tag{A3}
$$

Proof of Proposition 2. By design, the probability of observing a certain response is related to the underlying probabilities of the respondent giving that particular response to the sensitive and innocuous questions, as follows:

$$
\left\{ \begin{array}{l} \operatorname * {P r} [ Z _ {(1)} = m ] = p _ {(1)}   \operatorname * {P r} [ X = m ] + (1 - p _ {(1)})   \operatorname * {P r} [ Y = m ] \\ \operatorname * {P r} [ Z _ {(2)} = m ] = p _ {(2)}   \operatorname * {P r} [ X = m ] + (1 - p _ {(2)})   \operatorname * {P r} [ Y = m ]. \end{array} \right.\tag{A4}
$$

Solving (A4) for PrX <sub>=</sub> m and PrY <sub>=</sub> m, we have

$$
\begin{array}{l} \operatorname * {P r} [ X = m ] \\ = \frac {(1 - p _ {(2)}) \operatorname * {P r} [ Z _ {(1)} = m ] - (1 - p _ {(1)}) \operatorname * {P r} [ Z _ {(2)} = m ]}{p _ {(1)} - p _ {(2)}}, \end{array}\tag{A5}
$$

$$
\operatorname * {P r} [ Y = m ] = \frac {p _ {(1)} \operatorname* {P r} [ Z _ {(2)} = m ] - p _ {(2)} \operatorname* {P r} [ Z _ {(1)} = m ]}{p _ {(1)} - p _ {(2)}}.\tag{A6}
$$

Proof of Proposition 3. Based on Equation (13), we can write a set of 10 moment equations using $Z _ { 1 ( 1 ) } , Z _ { 1 ( 2 ) } , Z _ { 2 ( 1 ) } ,$ and $Z _ { 2 ( 2 ) }$ as well as their square and product terms first, then further rewrite them in terms of 10 unknown distribution parameters as follows:<sup>14</sup>

$$
\left\{ \begin{array}{l} E Z _ {1 (1)} = p _ {(1)} \mu_ {X _ {1}} + (1 - p _ {(1)}) \mu_ {Y _ {1}} \\ E Z _ {2 (1)} = p _ {(1)} \mu_ {X _ {2}} + (1 - p _ {(1)}) \mu_ {Y _ {2}} \\ E Z _ {1 (2)} = p _ {(2)} \mu_ {X _ {1}} + (1 - p _ {(2)}) \mu_ {Y _ {1}} \\ E Z _ {2 (2)} = p _ {(2)} \mu_ {X _ {2}} + (1 - p _ {(2)}) \mu_ {Y _ {2}} \\ E Z _ {1 (1)} ^ {2} = p _ {(1)} (\sigma_ {X _ {1}} ^ {2} + \mu_ {X _ {1}} ^ {2}) + (1 - p _ {(1)}) (\sigma_ {Y _ {1}} ^ {2} + \mu_ {Y _ {1}} ^ {2}) \\ E Z _ {2 (1)} ^ {2} = p _ {(1)} (\sigma_ {X _ {2}} ^ {2} + \mu_ {X _ {2}} ^ {2}) + (1 - p _ {(1)}) (\sigma_ {Y _ {2}} ^ {2} + \mu_ {Y _ {2}} ^ {2}) \\ E Z _ {1 (2)} ^ {2} = p _ {(2)} (\sigma_ {X _ {1}} ^ {2} + \mu_ {X _ {1}} ^ {2}) + (1 - p _ {(2)}) (\sigma_ {Y _ {1}} ^ {2} + \mu_ {Y _ {1}} ^ {2}) \\ E Z _ {2 (2)} ^ {2} = p _ {(2)} (\sigma_ {X _ {2}} ^ {2} + \mu_ {X _ {2}} ^ {2}) + (1 - p _ {(2)}) (\sigma_ {Y _ {2}} ^ {2} + \mu_ {Y _ {2}} ^ {2}) \\ E Z _ {1 (1)} Z _ {2 (1)} = p _ {(1)} ^ {2} (\sigma_ {X _ {1} X _ {2}} ^ {2} + \mu_ {X _ {1}} \mu_ {X _ {2}}) \\ \qquad + p _ {(1)} (1 - p _ {(1)}) (\mu_ {X _ {1}} \mu_ {Y _ {2}} + \mu_ {X _ {2}} \mu_ {Y _ {1}}) \\ \qquad + (1 - p _ {(1)}) ^ {2} (\sigma_ {Y _ {1} y _ {2}} ^ {2} + \mu_ {Y _ {1}} \mu_ {Y _ {2}}) \\ E Z _ {1 (2)} Z _ {2 (2)} = p _ {(2)} ^ {2} (\sigma_ {X _ {1} X _ {2}} ^ {2} + \mu_ {X _ {1}} \mu_ {X _ {2}}) \\ \qquad + p _ {(2)} (1 - p _ {(2)}) (\mu_ {x _ {1}} \mu_ {y _ {2}} + \mu_ {X _ {2}} \mu_ {Y _ {1}}) \\ \qquad + (1 - p _ {(2)}) ^ {2} (\sigma_ {{Y} _{1} Y_{2}} ^{2} + \mu_ {{Y} _{1}} \mu_ {{Y} _{2}}). \end{array} \right.\tag{A7}
$$

The 10 unknown parameters can be estimated by solving (A7) after substituting sample moments for the population moments. The resulting method-of-moments estimators are consistent estimators of the population parameters. We further rewrite the sample moments of the square and product terms in terms of sample statistics as shown below:

<table><tr><td>Square/product terms</td><td>Sample moments</td><td>Square/product terms</td><td>Sample moments</td></tr><tr><td> $Z_{1(1)}^{2}$ </td><td> $S_{Z_{1(1)}}^{2} + (\bar{Z}_{1(1)})^{2}$ </td><td> $Z_{1(2)}^{2}$ </td><td> $S_{Z_{1(2)}}^{2} + (\bar{Z}_{1(2)})^{2}$ </td></tr><tr><td> $Z_{2(1)}^{2}$ </td><td> $S_{Z_{2(1)}}^{2} + (\bar{Z}_{2(1)})^{2}$ </td><td> $Z_{2(2)}^{2}$ </td><td> $S_{Z_{2(2)}}^{2} + (\bar{Z}_{2(2)})^{2}$ </td></tr><tr><td> $Z_{1(1)}Z_{2(1)}$ </td><td> $S_{Z_{1(1)}Z_{2(1)}}^{2} + \bar{Z}_{1(1)}\bar{Z}_{2(1)}$ </td><td> $Z_{1(2)}Z_{2(2)}$ </td><td> $S_{Z_{1(2)}Z_{2(2)}}^{2} + \bar{Z}_{1(2)}\bar{Z}_{2(2)}.$ </td></tr></table>

We obtain the method-of-moments estimators as follows:

$$
\begin{array}{c} \hat {\mu} _ {X _ {i}} = \frac {(1 - p _ {(2)}) \bar {Z} _ {i (1)} - (1 - p _ {(1)}) \bar {Z} _ {i (2)}}{p _ {(1)} - p _ {(2)}}, \\ \hat {\mu} _ {Y _ {i}} = \frac {p _ {(1)} \bar {Z} _ {i (2)} - p _ {(2)} \bar {Z} _ {i (1)}}{p _ {(1)} - p _ {(2)}} \quad i = 1, 2; \end{array}\tag{A8}
$$

<sup>14</sup> Note that multiplying an indicator variable by its complement would always yield zero, i.e., $I _ { i ( j ) } ( 1 - I _ { i ( j ) } ) = 0 \ \forall \ : i , j .$ Squaring an indicator variable also yields itself, i.e., $I _ { i ( j ) } ^ { 2 } = I _ { i ( j ) }$ and $( 1 - I _ { i ( j ) } ) ^ { 2 } =$ $( 1 - I _ { i ( j ) } ) \ \forall \ : i , j .$ . Furthermore, $X _ { 1 }$ and $X _ { 2 }$ are unrelated to $Y _ { 1 }$ and $Y _ { 2 }$ by design and, thus, $E X _ { 1 } Y _ { 2 } = E X _ { 1 } E Y _ { 2 }$ and $E X _ { 2 } Y _ { 1 } = E X _ { 2 } E Y _ { 1 }$

$$
\begin{array}{c} \hat {\sigma} _ {X _ {i}} ^ {2} = ((p _ {(1)} - p _ {(2)}) [ (1 - p _ {(2)}) S _ {Z _ {i} (1)} ^ {2} - (1 - p _ {(1)}) S _ {Z _ {i (2)}} ^ {2} ] - (1 - p _ {(1)}) \\ \cdot (1 - p _ {(2)}) (\bar {Z} _ {i (1)} - \bar {Z} _ {i (2)}) ^ {2}) \cdot ((p _ {(1)} - p _ {(2)}) ^ {2}) ^ {- 1} \quad i = 1, 2; \end{array}\tag{A9}
$$

$$
\hat {\sigma} _ {Y _ {i}} ^ {2} = \frac {(p _ {(1)} - p _ {(2)}) (p _ {(1)} S _ {Z _ {i} (2)} ^ {2} - p _ {(2)} S _ {Z _ {i (1)}} ^ {2}) - p _ {(1)} p _ {(2)} (\bar {Z} _ {i (1)} - \bar {Z} _ {i (2)}) ^ {2}}{(p _ {(1)} - p _ {(2)}) ^ {2}}
$$

$$
i = 1, 2;\tag{A10}
$$

$$
\begin{array}{r} \hat {\sigma} _ {X _ {1} X _ {2}} ^ {2} = \frac {(1 - p _ {(2)}) ^ {2} S _ {Z _ {1 (1)} Z _ {2 (1)}} - (1 - p _ {(1)}) ^ {2} S _ {Z _ {1 (2)} Z _ {2 (2)}} ^ {2}}{(p _ {(1)} + p _ {(2)} - 2 p _ {(1)} p _ {(2)}) (p _ {(1)} - p _ {(2)})}, \\ \hat {\sigma} _ {Y _ {1} Y _ {2}} ^ {2} = \frac {p _ {(1)} ^ {2} S _ {Z _ {1 (2)} Z _ {2 (2)}} ^ {2} - p _ {(2)} ^ {2} S _ {Z _ {1 (1)} Z _ {2 (1)}} ^ {2}}{(p _ {(1)} + p _ {(2)} - 2 p _ {(1)} p _ {(2)}) (p _ {(1)} - p _ {(2)})}. \end{array}\tag{A11}
$$

Proof of Proposition 4. Taking expectations on both sides of (18) yields

$$
\begin{array}{c} E Z _ {1} X _ {3} = p E X _ {1} X _ {3} + (1 - p) E X _ {3} Y _ {1} \\ \Rightarrow E Z _ {1} X _ {3} - E Z _ {1} E X _ {3} = p E X _ {1} X _ {3} + (1 - p) E X _ {3} Y _ {1} - E Z _ {1} E X _ {3} \\ = p E X _ {1} X _ {3} + (1 - p) E X _ {3} Y _ {1} \\ \qquad - E [ I _ {1} X _ {1} + (1 - I _ {1}) Y _ {1} ] E X _ {3} \\ = p E X _ {1} X _ {3} + (1 - p) E X _ {3} Y _ {1} \\ \qquad - p E X _ {1} E X _ {3} - (1 - p) E X _ {3} E Y _ {1} \\ = p (E X _ {1} X _ {3} - E X _ {1} E X _ {3}) \\ \qquad + (1 - p) (E X _ {3} Y _ {1} - E X _ {3} E Y _ {1}) \end{array}\tag{⇒}
$$

$$
\sigma_ {Z _ {1} X _ {3}} ^ {2} = p \sigma_ {X _ {1} X _ {3}} ^ {2} (\sigma_ {X _ {3} Y _ {1}} ^ {2}
$$

in an unrelated question design)

⇒

$$
\hat {\sigma} _ {X _ {1} X _ {3}} ^ {2} = \frac {S _ {Z _ {1} X _ {3}} ^ {2}}{p} (\text { estimate } \sigma_ {Z _ {1} X _ {3}} ^ {2} \text { by } S _ {Z _ {1} X _ {3}} ^ {2}).\tag{A12}
$$

## Appendix B. Choice of Probability Values

A major statistical consideration in choosing $p _ { ( 1 ) }$ and $p _ { ( 2 ) }$ is that the sampling variance of the resulting estimators should be minimized. Equation (6) gives the sampling variance of the mean estimator for the underlying sensitive answer $X ,$ and it may be further expanded by writing var $( Z _ { ( 1 ) } )$ and $\mathbf { v a r } ( Z _ { ( 2 ) } )$ in terms of the population means $\mu _ { X }$ and $\mu _ { Y }$ of the sensitive and innocuous questions as well as their population variances $\sigma _ { X } ^ { 2 }$ and $\sigma _ { Y } ^ { 2 }$ . Thus,

$$
\begin{array}{r l} & {\mathrm{var} (Z _ {(1)}) = E (Z _ {(1)} ^ {2}) - E (Z _ {(1)}) ^ {2}} \\ & {\qquad = p _ {(1)} (\sigma_ {X} ^ {2} + \mu_ {X} ^ {2}) + (1 - p _ {(1)}) (\sigma_ {Y} ^ {2} + \mu_ {Y} ^ {2})} \\ & {\qquad \qquad - [ p _ {(1)} \mu_ {X} + (1 - p _ {(1)}) \mu_ {Y} ] ^ {2},} \\ & {\mathrm{var} (Z _ {(2)}) = p _ {(2)} (\sigma_ {X} ^ {2} + \mu_ {X} ^ {2}) + (1 - p _ {(2)}) (\sigma_ {Y} ^ {2} + \mu_ {Y} ^ {2})} \\ & {\qquad \qquad - [ p _ {(2)} \mu_ {X} + (1 - p _ {(2)}) \mu_ {Y} ] ^ {2}.} \end{array}\tag{B1}
$$

(B2)

Substituting (B1) and (B2) into (6) yields

$$
\begin{array}{l} \operatorname{var} (\hat {\mu} _ {X}) = \frac {1}{(p _ {(1)} - p _ {(2)}) ^ {2}} \\ \qquad \cdot \bigg \{\frac {(1 - p _ {(2)}) ^ {2} [ \sigma_ {Y} ^ {2} + p _ {(1)} (\sigma_ {X} ^ {2} - \sigma_ {Y} ^ {2}) + p _ {(1)} (1 - p _ {(1)}) (\mu_ {X} - \mu_ {Y}) ^ {2} ]}{n _ {(1)}} \\ \qquad + \frac {(1 - p _ {(1)}) ^ {2} [ \sigma_ {Y} ^ {2} + p _ {(2)} (\sigma_ {X} ^ {2} - \sigma_ {Y} ^ {2}) + p _ {(2)} (1 - p _ {(2)}) (\mu_ {X} - \mu_ {Y}) ^ {2} ]}{n _ {(2)}} \bigg \}. \end{array}\tag{B3}
$$

With (B3), consider how the sampling variance $\operatorname { v a r } ( \hat { \mu } _ { X } )$ can be minimized with respect to $p _ { ( 1 ) }$ and $p _ { ( 2 ) }$ . In particular, simplify the problem by considering the choice of $p _ { ( 1 ) }$ when $p _ { ( 2 ) }$ is given. It can be seen that var $( \hat { \mu } _ { X } )$ becomes excessively large as $p _ { ( 1 ) }$ approaches $p _ { ( 2 ) }$ . To minimize $\operatorname { v a r } ( \hat { \mu } _ { X } )$ , consider its first derivative with respect to $p _ { \left( 1 \right) } \colon$

$$
\begin{array}{l} \frac {\partial \mathrm{var} (\hat {\mu} _ {X})}{\partial p _ {(1)}} = \frac {1}{- (p _ {(1)} - p _ {(2)}) ^ {3}} \\ \qquad \qquad \times \bigg \{\frac {1}{n _ {(2)}} (2 (1 - p _ {(1)}) (1 - p _ {(2)}) [ (1 - p _ {(2)}) \sigma_ {Y} ^ {2} + p _ {(2)} \sigma_ {X} ^ {2} \\ \qquad \qquad \qquad + p _ {(2)} (1 - p _ {(2)}) (\mu_ {X} - \mu_ {Y}) ^ {2} ]) + (1 - p _ {(2)}) ^ {2} \\ \qquad \qquad \times \frac {1}{n _ {(1)}} ((1 - p _ {(1)} + 1 - p _ {(2)}) \sigma_ {Y} ^ {2} + (p _ {(1)} + p _ {(2)}) \sigma_ {X} ^ {2} \\ \qquad \qquad + [ p _ {(1)} (1 - p _ {(2)}) + p _ {(2)} (1 - p _ {(1)}) ] (\mu_ {X} - \mu_ {Y}) ^ {2}) \bigg \}. \end{array}\tag{B4}
$$

It can be seen that all terms on the right-hand-side of (B4) are always positive except for the first denominator term $- ( p _ { ( 1 ) } - \dot { p } _ { ( 2 ) } ) ^ { 3 }$ . In other words, the sign of $\partial \mathrm { v a r } ( \hat { \mu } _ { X } ) / \partial p _ { ( 1 ) }$ is equal to the sign of $- ( p _ { ( 1 ) } - p _ { ( 2 ) } )$ . It follows that

$$
\begin{array}{l} p _ {(1)} > p _ {(2)} \Rightarrow \frac {\partial \mathrm{var} (\hat {\mu} _ {X})}{\partial p _ {(1)}} <   0, \\ p _ {(1)} <   p _ {(2)} \Rightarrow \frac {\partial \mathrm{var} (\hat {\mu} _ {X})}{\partial p _ {(1)}} > 0. \end{array}\tag{B5}
$$

In other words, $\operatorname { v a r } ( \hat { \mu } _ { X } )$ is monotonically decreasing in $p _ { ( 1 ) }$ when $p _ { ( 1 ) } > p _ { ( 2 ) }$ and monotonically increasing in $p _ { ( 1 ) }$ when $p _ { ( 1 ) } < p _ { ( 2 ) }$ . This property indicates that the sampling variance will be reduced by choosing $p _ { ( 1 ) }$ to be far from $p _ { ( 2 ) } .$ It follows that the sampling variance would be at its minimum when the distance between $p _ { ( 1 ) }$ and $p _ { ( 2 ) }$ is largest, i.e., $| p _ { ( 1 ) } - p _ { ( 2 ) } | = 1$ . However, this is not feasible because it means that respondents in one of the samples would always be answering the sensitive question.

Given $p _ { ( 2 ) }$ and $| p _ { ( 1 ) } - p _ { ( 2 ) } | ,$ , we further consider whether it might be better to choose $\textbf { a } p _ { ( 1 ) }$ larger than $p _ { ( 2 ) } ( \mathrm { i . e . , }$ $p _ { ( 2 ) } < p _ { ( 1 ) } < 1 )$ . From (B3), whether a larger or smaller $p _ { ( 1 ) }$ would lead to a smaller $\operatorname { v a r } ( \hat { \mu } _ { X } )$ depends on the relative magnitudes of $\mu _ { X } , \ \mu _ { Y } , \ \sigma _ { X } ^ { 2 } ,$ , and $\sigma _ { Y } ^ { 2 }$ . Consider a simplified situation where the population means and variances of the sensitive and innocuous answers are similar $( \sigma _ { X } ^ { 2 } \approx \sigma _ { Y } ^ { 2 }$ and $\mu _ { X } \approx \mu _ { Y } )$ . In fact, this is an appropriate situation for RRT because the confidence of the respondents would be high. In such a situation, (B3) can be approximated by

$$
\operatorname{var} \left(\hat {\mu} _ {X}\right) = \frac {\sigma_ {X} ^ {2}}{\left(p _ {(1)} - p _ {(2)}\right) ^ {2}} \left[ \frac {(1 - p _ {(2)}) ^ {2}}{n _ {(1)}} + \frac {(1 - p _ {(1)}) ^ {2}}{n _ {(2)}} \right].\tag{B6}
$$

From (B6), it can be seen that $p _ { ( 1 ) }$ nv exerts its influence on $\mathrm { v a r } ( \hat { \mu } _ { X } )$ essentially through two terms: the denominator term $( p _ { ( 1 ) } - p _ { ( 2 ) } ) ^ { 2 }$ and the numerator term $( 1 - p _ { ( 1 ) } ) ^ { 2 }$ . Though choosing $p _ { ( 1 ) }$ either larger or smaller than $p _ { ( 2 ) }$ with the same deviation would result in the same effect on the denominator term $( p _ { ( 1 ) } - p _ { ( 2 ) } ) ^ { 2 }$ , choosing $p _ { ( 1 ) }$ larger (holding $p _ { ( 2 ) }$ fixed) will always lead to a smaller numerator term $( 1 - p _ { ( 1 ) } ) ^ { 2 }$ . This means that the sampling variance $\mathrm { v a r } ( \hat { \mu } _ { X } )$ is best minimized by choosing $p _ { ( 1 ) }$ to be larger than $p _ { ( 2 ) }$

## Appendix C. Choice of Sample Sizes

Equation (6) facilitates examining the effect of total sample size by taking the partial derivative of $\operatorname { v a r } ( \hat { \mu } _ { X } )$ with respect to N :

$$
\begin{array}{l} \frac {\partial \operatorname{var} \left(\hat {\mu} _ {X}\right)}{\partial N} = - \frac {(1 + k) \left[ \left(1 - p _ {(2)}\right) ^ {2} \operatorname{var} \left(Z _ {(1)}\right) + k \left(1 - p _ {(1)}\right) ^ {2} \operatorname{var} \left(Z _ {(2)}\right) \right]}{k N ^ {2} \left(p _ {(1)} - p _ {(2)}\right) ^ {2}} \\ <   0. \end{array} \tag {C1}
$$

As expected, $\operatorname { v a r } ( \hat { \mu } _ { X } )$ is strictly decreasing in N because var $\left( \hat { \mu } _ { X } \right) / \partial N$ is always negative. Though it is obvious that a larger total sample size helps reduce the sampling variance, researchers need to decide wisely on the proportion of respondents to be assigned to each of the two samples. Given $N ,$ they seek the optimal proportion k that would lead to the minimum sampling variance. Consider the partial derivative of $\operatorname { v a r } ( \hat { \mu } _ { X } )$ with respect to k:

$$
\frac {\partial \operatorname{var} (\hat {\mu} _ {X})}{\partial k} = \frac {k ^ {2} \operatorname{var} (Z _ {(2)}) (1 - p _ {(1)}) ^ {2} - \operatorname{var} (Z _ {(1)}) (1 - p _ {(2)}) ^ {2}}{k ^ {2} N (p _ {(1)} - p _ {(2)}) ^ {2}}.\tag{C2}
$$

Because $\partial \mathrm { v a r } ( \hat { \mu } _ { X } ) / \partial k$ can be positive or negative, it suffices that we find whether or not there exists a k that leads to a minimum $\mathbf { v a r } ( \hat { \mu } _ { X } )$ . The first-order condition (FOC) and second-order condition (SOC) are

$$
\mathrm{FOC:} k ^ {2} \mathrm{var} (Z _ {(2)}) (1 - p _ {(1)}) ^ {2} - \mathrm{var} (Z _ {(1)}) (1 - p _ {(2)}) ^ {2} = 0\tag{C3}
$$

$$
\text { SOC: } \quad 2 \frac {\operatorname{var} (Z _ {(1)}) (1 - p _ {(2)}) ^ {2}}{k ^ {3} N (p _ {(1)} - p _ {(2)}) ^ {2}} > 0.\tag{C4}
$$

Because the SOC is always positive, var $( \hat { \mu } _ { X } )$ would reach its minimum when the FOC is satisfied, specifically, when

$$
k = \sqrt {\frac {\operatorname{var} (Z _ {(1)})}{\operatorname{var} (Z _ {(2)})}} \frac {(1 - p _ {(2)})}{(1 - p _ {(1)})}.\tag{C5}
$$

Appendix D. Measurement Items for Study 2

<table><tr><td>Construct</td><td>Measurement item</td><td colspan="2">Standardized loading</td></tr><tr><td colspan="4">Software cost</td></tr><tr><td>1</td><td>Licensed software is expensive.</td><td>0.79</td><td>0.81</td></tr><tr><td>2*</td><td>The price of licensed software nowadays is cheap.</td><td>0.64</td><td>0.64</td></tr><tr><td>3</td><td>If I need to buy licensed software, I need to pay a lot.</td><td>0.66</td><td>0.71</td></tr><tr><td colspan="4">Punishment certainty</td></tr><tr><td>1*</td><td>If I copy software without authorization, the chance of getting punished is very low.</td><td>0.72</td><td>0.87</td></tr><tr><td>2</td><td>If I copy software without authorization, I would easily get punished.</td><td>0.62</td><td>0.54</td></tr><tr><td colspan="4">Attitude</td></tr><tr><td>1</td><td>To me, unauthorized copying of software is: (Very Unattractive... Very Attractive).</td><td>0.68</td><td>0.65</td></tr><tr><td>2</td><td>To me, unauthorized copying of software is: (Very Harmful... Very Beneficial).</td><td>0.82</td><td>0.72</td></tr><tr><td>3</td><td>To me, unauthorized copying of software is: (Very Foolish... Very Wise).</td><td>0.81</td><td>0.75</td></tr><tr><td colspan="4">Piracy behavior</td></tr><tr><td>1</td><td>Among the software that I often use, most are copied without authorization.</td><td>0.84</td><td>0.74</td></tr><tr><td>2</td><td>I often copy the software that I want without authorization.</td><td>0.87</td><td>0.87</td></tr><tr><td>3</td><td>I have a lot of software that was copied without authorization.</td><td>0.88</td><td>0.73</td></tr></table>

Notes. 1. All responses were on a 7-point scale. Those marked with an asterisk were reverse coded with respect to the corresponding constructs.  
2. Unless specified otherwise, responses spanned 7 points from “strongly disagree” (1) to “strongly $\mathrm { { a g r e e ^ { \prime \prime } \ ( 7 ) } }$  
3. Standardized loadings for randomized responses are in boldface.

## References

Armacost, R. L., J. C. Hosseini, S. A. Morris, K. A. Rehbein. 1991. An empirical comparison of direct questioning, scenario, and randomized response methods for obtaining sensitive business information. Decision Sci. 22(5) 1073–1090.

Bagozzi, R. P., Y. Yi. 1988. On the evaluation of structural equation models. J. Acad. Marketing Sci. 16 74–94.

Browne, M. W., R. Cudeck. 1993. Alternative ways of assessing model fit. K. A. Bollen, J. S. Long, eds. Testing Structural Equation Models. Sage Publishing, Newbury Park, CA, 136–162.

BSA. 2007. 5th Annual BSA and IDC Global Software Piracy Study.

Cheng, H. K., R. R. Sims, H. Teegen. 1997. To purchase or to pirate software: An empirical study. J. Management Inform. Systems 13(4) 49–60.

Christensen, A. L., V. Eining. 1991. Factors influencing software piracy: Implications for accountants. J. Inform. Systems 5(1) 67–80.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences, 2nd ed. Lawrence Erlbaum Associates, Hillsdale, NJ.

Diamantopoulos, A., J. A. Siguaw. 2000. Introducing LISREL. Sage Publications, Newbury Park, CA.

Fox, J. A., P. E. Tracy. 1984. Measuring associations with randomized response. Soc. Sci. Res. 13 188–197.

Fox, J. A., P. E. Tracy. 1986. Randomized Response: A Method for Sen sitive Surveys. Sage Publications, Newbury Park, CA.

Gefen, D., D. W. Straub, M. C. Boudreau. 2000. Structural equation modeling and regression: Guidelines for research practice. Comm. Assoc. Inform. Systems 4(1) Article 7, http://aise.aisnet .org/cais/vol4/iss1/7.

Greenberg, B. G., A. A. Abul-Ela, W. R. Simmons, D. G. Horvitz. 1969. The unrelated question randomized response model: Theoretical framework. J. Amer. Statist. Assoc. 64(326) 520–539.

Greenberg, B. G., R. R. Kuebler, J. R. Abernathy, D. G. Horvitz. 1971. Application of the randomized response technique in obtaining quantitative data. J. Amer. Statist. Assoc. 66(334) 243–250.

Himmelfarb, S. 1993. The measurement of attitudes. A. H. Eagly, S. Chaiken, eds. The Psychology of Attitudes. Wadsworth Publishing, Florence, KY, 23–87.

Himmelfarb, S., C. Lickteig. 1982. Social desirability and the randomized response technique. J. Personality Soc. Psych. 43(4) 710–717.

Hosseini, J. C., R. L. Armacost. 1993. Gathering sensitive information in organizations. Amer. Behavioral Scientist 36 443–471.

Hu, L. T., P. M. Bentler. 1999. Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. Structural Equation Model 6(1) 1–55.

Lensvelt-Mulders, G. J. L. M., J. J. Hox, P. G. M. van der Heijden, C. J. M. Maas. 2005. Meta-analysis of randomized response research: Thirty-five years of validation. Sociol. Methods Res. 33(3) 319–348.

Limayem, M., M. Khalifa, W. W. Chin. 2004. Factors motivating software piracy: A longitudinal study. IEEE Trans. Engrg. Man agement 50(4) 414–425.

Locander, W., S. Sudman, N. Blackburn. 1976. An investigation of interview method, threat and response distortion. J. Amer. Statist. Assoc. 71(354) 269–275.

MacCallum, R. C., M. W. Browne, H. M. Sugawara. 1996. Power analysis and determination of sample size for covariance structure modeling. Psych. Methods 1(2) 130–149.

Mason, R. O. 1986. Four ethical issues of the information age. MIS Quart. 10(1) 5–12.

Moores, T., J. Chang. 2006. Ethical decision making in software piracy: Initial development and test of a four-component model. MIS Quart. 30(1) 167–180.

Paulhus, D. L. 1991. Measurement and control of response bias. J. P. Robinson, P. R. Shaver, L. S. Wrightsman, eds. Measures of Personality and Social Psychological Attitudes. Academic Press, San Diego, 17–59.

Peace, A. G., D. F. Galletta, J. Y. L. Thong, 2003. Software piracy in the workplace: A model and empirical test. J. Management Inform. Systems 20(1) 153–177.

Podsakoff, P. M., S. B. MacKenzie, J. Y. Lee, N. P. Podsakoff. 2003. Common method biases in behavioral research: A critical review of the literature and recommended remedies J. Appl. Psych. 88(5) 879–903.

Scheers, N. J. 1992. A review of randomized response techniques. Measurement Eval. Counseling Development 25(1) 27–41.

Seale, D. A. 2002. Why do we do it if we know it’s wrong? A structural model of software piracy. A. Salehnia, ed. Ethical Issues of Information Systems. IRM Press, Hershey, PA, 120–144.

Sims, R. R., H. K. Cheng, H. Teegen. 1996. Toward a profile of student software piraters. J. Bus. Ethics 15(8) 839–849.

Steiger, J. H., A. Shapiro, M. W. Browne. 1985. On the multivariate asymptotic distribution of sequential chi-square statistics. Psychometrika 50(3) 253–263.

Sudman, S., N. M. Bradburn. 1982. Asking Questions: A Practical Guide to Questionnaire Design. Jossey-Bass, San Francisco.

Taylor, G. S., J. P. Shim. 1993. A comparative examination of attitudes toward software piracy among business professors and executives. Human Relations 46(4) 419–433.

Umesh, U. N., R. A. Peterson. 1991. A critical evaluation of the randomized response method: Applications, validation, and research agenda. Sociol. Methods Res. 20 104–138.

van der Heijden, P. G. M., G. van Gils, J. Bouts, J. J. Hox. 2000. A comparison of randomized response, computer-assisted selfinterview, and face-to-face direct questioning: Eliciting sensitive information in the context of welfare and unemployment benefit. Sociol. Methods Res. 28(4) 505–537.

Warner, S. L. 1965. Randomized response: A survey technique for eliminating evasive answer bias. J. Amer. Statist. Assoc. 60 63–69.

Wothke, W. 1993. Nonpositive definite matrices in structural modeling. K. A. Bollen, J. S. Long, eds. Testing Structural Equation Models. Sage Publications, Newbury Park, CA, 256–293.
