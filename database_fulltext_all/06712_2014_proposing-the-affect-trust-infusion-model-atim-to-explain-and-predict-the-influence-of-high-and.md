---
otero_id: 6712
otero_key: "TDRJDNZ6"
title: "Proposing the Affect-Trust Infusion Model (ATIM) to explain and predict the influence of high and low affect infusion on Web vendor trust"
authors: "Paul Benjamin Lowry; Nathan W. Twyman; Matt Pickard; Jeffrey L. Jenkins; Quang “Neo” Bui"
year: "2014"
journal: "Information & Management"
doi: "10.1016/j.im.2014.03.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Proposing the Affect-Trust Infusion Model (ATIM) to Explain and Predict the Influence of High- and Low-Affect Infusion on Web-Vendor Trust

Author: Paul Benjamin Lowry Nathan Twyman Matt Pickard Jeffrey L. Jenkins Qang Neo Bui

![](/api/attachments/TDRJDNZ6/fulltext/images/1bebb1a280818b884f0abc9cf5b710ba999c458ea88d4cae39f16ba6629b1767.jpg)

PII: S0378-7206(14)00032-9

DOI: http://dx.doi.org/doi:10.1016/j.im.2014.03.005

Reference: INFMAN 2708

To appear in: INFMAN

Received date: 11-4-2012

Revised date: 28-1-2013

Accepted date: 22-3-2014

Please cite this article as: P.B. Lowry, N. Twyman, M. Pickard, J.L. Jenkins, Q.N. Bui, Proposing the Affect-Trust Infusion Model (ATIM) to Explain and Predict the Influence of High- and Low-Affect Infusion on Web-Vendor Trust, Information & Management (2014), http://dx.doi.org/10.1016/j.im.2014.03.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Proposing the Affect-Trust Infusion Model (ATIM) to Explain and Predict the Influence of High- and Low-Affect Infusion on Web-Vendor Trust

Paul Benjamin Lowry Associate Professor Department of Information Systems City University of Hong Kong 83 Tat Chee Avenue P7912, Academic Building 1 Hong Kong, People’s Republic of China +852-3442-7771 Paul.Lowry.PhD@gmail.com

Nathan Twyman Center for the Management of Information University of Arizona nwt611@gmail.com

Matt Pickard Computer Information Systems Georgia State University matthew.david.pickard@gmail.com

Jeffrey L. Jenkins Center for the Management of Information University of Arizona jljenk@gmail.com

Qang Neo Bui Bentley University neo.hawaii@gmail.com

Proposing the Affect-Trust Infusion Model (ATIM) to Explain and Predict the Influence of High- and Low-Affect Infusion on Web-Vendor Trust

## ABSTRACT

Trust is just as essential to online business as it is to offline transactions but can be more difficult to achieve— especially for newer Web sites associated with unknown Web vendors. Research explains that Web vendor trust can be created by cognitive and affective influences. But under what circumstances will emotion more powerfully impact trust and when will cognition be more powerful? Theory-based answers to these questions can help online Web vendors design better Web sites that account for unleveraged factors that will increase trust in the Web vendor. We adapt the Affect Infusion Model to propose the Affect-Trust Infusion Model (ATIM) that explains and predicts how and when cognition, through perceived Web site performance (PWP), and positive emotion (PE) each influence Web vendor trust. ATIM explains the underlying causal mechanisms that determine the degree of affect infusion and the subsequent processing strategy that a user adopts when interacting with a new Web site. Under high-affect infusion, PE acts as a mediator between PWP and vendor trust; under low-affect infusion, PWP primarily impacts trust and PE is dis-intermediated. We review two distinct, rigorously validated experiments that empirically support ATIM. To conclude, we detail several promising research opportunities that can leverage ATIM and show how it can help to guide user-centered design (UCD) as example practical application.

## KEYWORDS

Website design, trust, emotion, affect, affect infusion, Web site performance, Affect-Trust Infusion Model (ATIM)

## 1.0 INTRODUCTION

One of the greatest challenges to the growth of e-commerce is improving trust in online vendors [7]. Accordingly, several recent studies have sought methods for increasing and accelerating e-commerce trust formation [22, 27, 39, 44, 84, 86, 117]. Of particular interest to our study, trust strongly impacts purchase intentions [30], but trust is difficult to establish—especially with lesser-known brands or unknown Web vendors [10, 64]. Creating trust usually requires a substantial passage of time, which typically involves several interactions before a consumer feels comfortable conducting a transaction [17]. This time requirement creates a substantial entrepreneurial impediment to millions of new Web sites and Web vendors that have economic value to offer but have little time or opportunity to sell their value statement before caving in to economic pressures. Finding novel ways to quickly develop trust in unknown Web vendors is thus of great value—particularly for the millions of owners of emerging Web sites that have much economic value to offer but do not have established brands and reputations [64].

This article joins this research conversation and specifically focuses on the phenomenon of Web vendor trust. Web vendor trust is an individual’s trusting beliefs<sup>i</sup> toward a Web vendor<sup>ii</sup> and is typically built through the vendor’s Web site [64, 68, 69, 85]. Web vendor trust is a particularly important form of trust that motivates this study because this type of trust is closely equivalent to offline trust, which can involve offline activities such as direct sales or other communication and transactions that are critical to a deeper business relationship [99]. For multichannel organizations that maintain online and offline activities, Web vendor trust is thus a particularly important phenomenon of interest to engender. Of further importance, Web vendor trust generally drives purchases, online disclosures, and deeper relationships of loyalty, which are primary goals of most e-commerce Web sites; interaction alone is insufficient [69, 85].

This study examines how and when trust in a new Web vendor is most strongly enhanced by users’ cognitive evaluations of the vendor’s Web site versus when users’ emotional responses play a more prominent role. Cognitive and affective system evaluations have separately exhibited important related system-relevant outcomes, providing impetus for advancing understanding their relative impact on Web vendor trust: Cognitive evaluations have been shown to influence user behavior and evaluations in a variety of settings, including increasing Web site use [114], perceptions of quality [18], purchase intentions [47, 48], affective involvement [47], and attitude toward the Web site [21, 61]. Emotion has also been shown to positively influence user behavior such as promoting increased self-

efficacy [8], improved tasking performance [8], enhanced creativity in problem solving [46], increased sociability [45], augmented cooperation [45], increased self-disclosure [121], stronger purchase intentions [32, 78, 80, 103], higher IT evaluation [123, 124], increased system adoption [109], and continued system use [43].

Though the literature indicates potential for both perceived Web site performance (PWP) evaluations and positive emotion (PE) to increase Web vendor trust, our study demonstrates that PWP and PE do not always have the same impact. Namely, PWP and PE do not always influence human behavior and evaluation equally, and their influence depends heavily on context. Key contextual factors within a user interaction likely determine whether PWP or PE is most salient in affecting Web vendor trust. A deeper understanding of the relative impact of cognition versus affect on Web vendor trust is a research opportunity that is not yet addressed. Given this compelling theoretical gap and opportunity, this study answers the following research question:

RQ: How and when will PWP or PE influence Web vendor trust in the context of users

initially interacting with unknown Web sites and unknown Web vendors?

The remainder of this paper provides the necessary theoretical background to answer this question, and proposes a new model termed the Affect-Trust Infusion Model (ATIM). We test our ATIM using two empirical experiments. We then explain the significant contributions of this work to research and practice—including proposing a new methodology that can be used to enhance user-centered design (UCD) with the ATIM.

## 2.0 THEORY ON HOW AND WHEN PWP AND PE IMPACT TRUST

Here, we propose a new theoretical model, the Affect-Trust Infusion Model (ATIM), to address our research question. We first conceptually define affect, PE, and PWP, and explain how PWP impacts PE. Next, we propose the ATIM model, which employs the Affect Infusion Model (AIM), to explain when PE will increase trust in a Web site vendor and when PE will be less relevant. AIM was proposed by Forgas [35] to explain how affect or emotion influence cognitive social judgments (e.g., trust) in different affect-infused situations (e.g., high versus low) [35]. At the core of ATIM, we propose that, in high-affect infusion contexts PE will primarily drive the development of Web vendor trust by acting as a mediator between PWP and trust; whereas in low-affect infusion contexts, PWP will primarily drive the development of Web vendor trust—dis-intermediating PE

## 2.1 EXPLAINING HOW PERCEIVED WEB SITE PERFORMANCE (PWP) IMPACTS PE

We begin by explaining our adopted conceptualization of perceived positive Web site performance (PWP) and positive emotion (PE). We then explain the theoretical ties between the two.

The objective of proposing AIM, and our related empirical work, is not to extensively conceptualize and test all possible PWP measures. Instead, the focus is on how pragmatic conceptualizations and measures of PWP might influence Web vendor trust in both low- and high-AFI (low- and high-affect infusion) scenarios while accounting for PE. We thus carefully chose a PWP conceptualization (and related measures) that (1) are relevant to the systems contexts in both experiments and (2) allowed us to test AIM. Because testing scores of possible PWP measures in one study is impractical and theoretically unnecessary, the practice of selectively choosing sub-dimensions of PWP is common in leading information systems literature [e.g., 30, 64, 113, 120, 126].

Based on a large literature base [e.g., 18, 47, 48, 61], we define and decide the scope of our use of PWP as positive cognitive evaluations of an interaction with a Web site. As the literature addresses various related constructs, we include a description of these constructs in Appendix 4 to delineate them from our use of PWP. These positive cognitive judgments are formed or solidified during the interaction, and are a strong predictor of other cognition, attitudes, and future behavior. For example, a Web site user may determine that he or she had little ability to perform desired tasks—a judgment that would decrease the likelihood of future Web site use [61]. Evaluations of a Web site interaction have been shown to impact other cognitive judgments such as perceptions of quality [18] and purchase intentions [47, 48], and affective responses, such as affective involvement [47] and attitude toward the Web site [21,

#

Turning from PWP, we now explain our use of PE in ATIM. Disagreement exists in the psychology literature about the exact definitions of affect and related terms such as emotion and mood [36, 95]. In spite of affect’s fuzzy boundaries, it is important to study because of affect’s strong influences on behavior [32, 35, 78, 80, 103, 121].

Throughout the psychology literature, affect has been conceptualized in several ways. Russell refers to core affect as a superset of states that include emotions [95]. In contrast, Forgas [35] conceptualizes affect as encompassing moods and emotions, another commonly used conceptualization in the literature that is more congruous to our theoretical purposes. In particular, compared to emotions, moods tend to be relatively enduring and of a lower intensity whereas emotions “usually have a definite cause and clear cognitive content” (i.e., are associated with particular cognitions toward an object) [34, p. 230]. Because moods are more inherent and stable in a person’s general disposition, and not easily manipulated, the useful part of affect fundamental to the AIM and the typical focus of empirical studies is the emotional component, not the mood component [35]. Importantly, Russell [95] also congruently emphasizes that the emotional portion of core affect likewise can be manipulated by an external stimulus and the resulting evaluation.

For these reasons, we narrow the scope of the ATIM to focus on the emotion component of affect because PE is what we intend to manipulate, explain, predict, and measure—not one’s general mood, which is more conflated, enduring, not the result of cognitive evaluation, and thus not easy to directly manipulate [35, 95]. This theoretical scope decision is particularly useful for our purposes because ATIM focuses on the emotional result (i.e., PE) of a cognitive performance evaluation of an unknown Web site (i.e., PWP) and the result of that PE on cognitive trust. Pragmatically speaking, Web site designers have virtually no control over the general mood that users bring to a Web site interaction, but designers do have control over design considerations that create cognitive evaluations that affect PE from Web site interaction.

For modeling simplicity, we also limit our current theoretical consideration to PE—excluding negative emotion. Though PE and negative emotions are related, they are separate constructs that are not the opposite of each other and do not share the same antecedents [8, 28, 46, 74, 96, 110, 124]. Our pragmatic research focus is to help Web site designers create positive, not negative, experiences for Web site users. Our parsimonious focus on PE has been commonly used in other studies for the same basic reason that PE is the desired emotional experience that fosters positive outcomes such as consumer satisfaction, and increased Web site use [e.g., 8, 45, 46, 79, 81, 96, 98, 103].

More formally, ATIM assumes use of PE that results from cognitive evaluation of an object [35, 95]—that is, a Web site.

Now that we have defined our use of PWP and PE, we explain how PWP directly affects PE. First, the emotional component of affect can be changed or manipulated by external stimuli and the resulting evaluation, as demonstrated in [35, 95]. Assuming these results hold in a Web site context, during an interaction with a new Web site, a user’s PWP can thus act as a stimulus that drives the user’s resulting PE.

Supporting this assumption, consumer psychology and marketing research have often relied on performance evaluations to predict and explain changes in emotion. Several cognition-based theories explain specific emotions that result from cognitive processing. Example theories in the IS literature include the Theory of Reasoned Action [4] and the Theory of Planned Behavior [3], which predict that beliefs drive a person’s attitude. Expectation-Disconfirmation Theory [79] similarly predicts changes in satisfaction as a direct result of performance evaluations. The same relationship is seen throughout the related Met-Expectations Theory literature [12, 13, 67, 80, 103]. Moreover, because attitude and satisfaction have strong emotional components [3, 79], it logically follows that PE can at least be partially created by positive cognitive evaluations.

Several other similar studies further point to this potential link between perceived performance and PE. In satisfaction research, performance has been shown to influence consumer emotions [57, 73]. Specifically, according to Oliver [81], each cognitively evaluated attribute of a service or product may serve as a potential source of positive (or negative) emotion. Oliver also posits that in general perceived performance influences emotion [81]. Liljander and Strandvik [57] found significant empirical support for the link between perceived performance and PE. Finally, in the context of service recovery satisfaction, Schoefer [98] showed that interactional, procedural, and distributive justice—all forms of perceived performance that are cognitively evaluated from the customer’s viewpoint— influence positive and negative emotion. Given this strong theoretical and empirical evidence,

H1. An increase in PWP increases a user’s PE.

## 2.2 WHEN PE AND PWP MOST INFLUENCE TRUST AND WHEN THEY DO NOT

The idea that perceived performance impacts trust has been well established [e.g., 64, 68, 69, 85]. Likewise, in proposing H1 we give substantial evidence why the PE stemming from a Web site interaction should influence trust judgments. What has yet to be explained in the literature are the factors of Web site use that would cause perceived

#

performance, through users’ cognitive judgments, to have greater impact on trust judgments and the factors that cause PE to have greater impact on trust judgments. To address this theoretical gap in the literature, we use the Affect Infusion Model (AIM) to explain and predict when PE will positively impact Web vendor trust and when PWP will have the most impact.

Although many studies have focused on a specific type of PE such as enjoyment [e.g., 25, 26, 100, 116, 118] or satisfaction [e.g., 5, 12, 14, 63, 67, 79] to predict trust responses, AIM more comprehensively explains how one’s emotions can influence cognitive judgment in general [35]. General predictions thus based on the AIM should have greater explanatory potential than more narrow predictions for specific emotional states such as enjoyment or satisfaction alone. Important to ATIM, AIM posits that affect (and the subset of PE)—although distinct from cognitive processes—can exert influence on cognitive social judgments (e.g., trust) under certain conditions [35]. Other trust research has hypothesized [70] and empirically validated [28] that trusting beliefs can be influenced by PE. We believe the AIM provides the strongest explanation why this is the case and when this is the case. Again, AIM was built for more general affect, which includes PE. Consistent with our decisions about scope, we adopt our AIM focus on PE instead of more general affect.

AIM posits affect infusion (AFI) as the underlying causal mechanism process “whereby affectively loaded information exerts an influence on and becomes incorporated into the judgmental process, entering into the judge's deliberations and eventually coloring the judgmental outcome” [35, p. 39]. Under low-affect infusion (low-AFI), cognitive evaluations are the main drivers of judgments. Under high-affect infusion (high-AFI), PE is the main driver of judgments [35]. Critical to AIM, experiencing high levels of PE does not necessarily mean high-AFI occurs; neither do low levels of PE mean that low-AFI will occur. Namely, if high PE is present when a low-AFI strategy is employed, PE will still exhibit little influence on cognitive judgments. Instead, the degree of AFI varies depending on the cognitive processing strategy used to make the judgment, and this strategy is determined by the target characteristics, judge characteristics, and situational factors, explained as follows.

Based on the target, judge/user, and situation features, AIM identifies four processing strategies one can engage in— direct access, motivational, heuristic, and substantive. Two of the strategies (heuristic and substantive) have high-AFI and two (direct access and motivational) have low-AFI. These strategies represent a spectrum of the likelihood that PE will impact cognition from the lowest to the highest likelihood of impact:

1. Direct access processing is a low-AFI processing strategy and is the scenario in which PE is least likely to exert influence on cognition. This strategy is most likely used when several of the following contextual features apply [35]: (1) target features are familiar, typical, and/or low in complexity; (2) the judge/user features include low personal relevance, low motivational goals, low affective state, and/or low cognitive capacity; and (3) situation features that cause little need for accuracy, high availability of criteria, and/or low social desirability. Direct access processing typically involves simply reproducing a stored reaction of what was done in the same scenario in the past, and thus PE plays little to no role.

For example, if a person is navigating to an online banking portal and has used the banking portal many times in the past without trouble (thus, high familiarity/typicality), the person would likely not stop to think about potential security vulnerabilities or other factors that would inhibit trust and thereby use. Rather, the person would recall prior performance evaluations of the banking portal and rely on these as a cognitive pattern without additional elaboration. These crystallized judgments are robust and resistant against affective states, and thus the direct access processing strategy has low-AFI [35]. Users will form new judgments based on PWP, and these judgments will act as inputs for future evaluations via direct processing. This evolutionary approach to refining one’s pre-stored judgments is predicted in the expectancy value theory, which explains that one’s attitude is the summation of one’s beliefs [33]. As one receives new beliefs, one’s attitude evolves [33]. Previous high PWP would thus increase expectation of positive trust judgments in the future.

2. Motivated processing is a low-AFI processing strategy, representing the second least likely scenario in which PE impacts cognition. This strategy is most likely used when several of the following contextual features apply [35]: (1) target features are familiar, typical, and/or low in low complexity; (2) when judge/user features include high personal relevance, high motivational goals, low affective state, and/or high cognitive capacity; and (3) situation features that cause high need for accuracy, high availability of criteria, and/or low social desirability. This kind of processing is especially common when motivational goals pressure for a specific judgmental outcome—specifically, if the person has a targeted search goal that is clear and knows what information is needed to achieve that goal [35]. For example, when one needs to find a specific book at a library, one likely uses the electronic catalog system with almost no generative, constructive elaboration as long as one has had previous searching with a similar system. The information searching patterns associated with the outcome of the judgment are guided by a priori motivational goal (e.g., to find the book) and are thus resistant to the influence of PE. Accordingly, motivated processing has a low likelihood of AFI although slightly more so than in direct access

#

processing [35]; in our context, PWP should thus directly influence trust in the Web site vendor. If a Web site cannot help a user achieve his or her interaction goals, or makes the experience unnecessarily difficult when the interaction is pre-judged as a straightforward task, then a user’s perception of the system’s competency should decrease—undermining a defining characteristic of trust [69, 105].

3. Heuristic processing is a high-AFI strategy representing the second most likely scenario of PE impacting cognition. This strategy is most likely used when several of the following contextual features apply [35]: (1) target features lack familiarity, have low typicality, or are high complexity; (2) judge/user features include low personal relevance, lack of motivational goals, high affective state, or limited cognitive capacity; and (3) situation features cause little need for accuracy, low availability of criteria, or high social desirability [35]. Heuristic processing provides a quick alternative to more elaborate cognitive processing by relying on cues such as one’s affective state. People are motivated toward this processing based on the affect-as-information principle [36], which posits that affect can be used as shortcuts to make decisions under conditions requiring fast judgment processing, lack of information, lack of familiarity, and the like. When using heuristic processing, people “ask themselves: ‘How do I feel about it?’ [and] in doing so, they may mistake feelings due to a pre-existing state as a reaction to the target” [36]. Hence, the heuristic processing strategy has a high likelihood of AFI [35].

4. Substantive processing is the high-AFI strategy where PE is most likely to influence cognition. This strategy is most likely used when several of the following contextual features apply [35]: (1) target features include low familiarity, low typicality, and high complexity; (2) judge/user features include high personal relevance, high motivation, high affective state, and/or high cognitive capacity; (3) situational features cause a need for accuracy, where there is a low availability of criteria, and/or where there is high social desirability. This strategy typically involves much constructive processing and is used in complex or atypical decision-making situations, requiring accurate or detailed consideration [35]. In these complex decision-making situations, a person draws on much information to make the decision, including performance evaluations and one’s affective states. Substantive processing is based on the affect priming theory, which suggests that affect increases access to congruent memories [74, 122]. PE thus will give greater recall to positive memories and therefore bias judgments in the direction of those memories [35]. Substantive processing thus is the highest AFI processing strategy.

As illustration, if a person navigates to an unfamiliar online banking portal, the person will carefully examine cues on the Web site to formulate trust beliefs. If the cues induce PE (e.g., the Web site is visually appealing), these cues and the associated PE will give greater recall of other Web sites that the user has had positive experience and trust with. The user will then be more likely to attribute trust to the current Web site. This process was shown in a study on the negative effect of presentation flaws in unknown Web sites on trust [30]. Yet, another study using the network associative model of memory showed how interactions with well-designed unknown Web sites, with positive branding images, causes users to associate the unknown Web site with previously known, positive Web site interactions, and thus increase trust [64].

The Psychology-based concept of trust transference helps explain how trust resulting from a Web site interaction transfers to a Web vendor. Trust transference occurs when a user or consumer projects the trust he or she has for a known target as the source of trust in an unknown target [51, 56, 64, 105]. Trust transference has been demonstrated between a wide array of sources and targets, such as using known individuals as sources of trust to transfer trust to unknown individuals as targets of trust [108, 115], trust in an industry association being transferred to trust in an unknown salesperson [72], trust in a traditional retail channel, and trust in known Web sites being transferred to trust in an unknown Web site [105]. The underlying mechanism that creates trust transference is the perceived link to, interaction with, and similarity between the source and the target [105]. To the extent these links are considered highly related, a user will consider the source and target to together have high entitativity, which occurs when a user mentally places the unknown target in the same grouping as the known source [105]. In a Web vendor context, the known entity is the Web site for which PE and initial trust have been created (even for the very first time); the unknown entity is the Web vendor. In a context where the Web vendor is new, the only perceptions about the vendor will stem from the Web site interaction, creating a perception of high entitativity and facilitating trust transference. Table 1 summarizes the four processing strategies that are used in low- and high-AFI that would be applied for Web vendor trust. Under the low-AFI strategies, PWP would affect trust more than PE; under the high-AFI strategies, PE would affect trust more than PWP. In summary:

H2. In low-AFI contexts, an increase in PWP—not PE—increases Web vendor trust.

H3a. In high-AFI contexts, an increase in PE—not positive Web site performance— increases Web vendor trust.

H3b. In high-AFI contexts, PE will fully mediate the relationship between PWP and Web vendor trust.<sup>iii</sup>

Figure 1 depicts ATIM, which encapsulates the hypotheses proposed in this section.

## 3.0 METHODOLOGY

To improve the generalizability of the results, we tested the model using two distinct experiments to simulate lowand high-AFI—specifically inducing motivated processing and heuristic processing. The purpose of the twoexperiment design was not to directly compare results from one study to another, but rather to cross validate our results in two different and distinct contexts—one with high affect-infusion and one with low affect-infusion. If the model holds in both scenarios, this represents a significant contribution to theory as previous theories have yielded seemingly conflicting results in these two contexts regarding the influence of PWP and PE on trust [e.g., 52, 90]. Additionally, for increased testability, we tested ATIM only in instances in which high entitativity between the Web site and the vendor would be expected (e.g., a novel Web site and novel Web vendor). The perception of high entitativity was reinforced by informing respondents that the Web site and the hypothetical Web vendor were highly related to each other. This manipulation thus encouraged respondents to mentally associate the two entities so that the initial trust formed by interacting

Table 1. Summary of Contextual Features that Drive Affect-Infusion Strategies and PE Low AFI (Low PE) Strategies: High AFI (High PE) Strategies:

<table><tr><td colspan="2">Primary contextual features that drive the AFI strategy</td><td>Direct access processing (PE least likely)</td><td>Motivated processing (PE  $2^{nd}$  least likely)</td><td>Heuristic processing (PE  $2^{nd}$  most likely)</td><td>Substantive processing (PE most likely)</td></tr><tr><td rowspan="3">Trust target features</td><td>Familiarity</td><td>High familiarity</td><td>High familiarity</td><td>Low familiarity</td><td>Low familiarity</td></tr><tr><td>Typicality</td><td>High typicality</td><td>High typicality</td><td>Low typicality</td><td>Low typicality</td></tr><tr><td>Complexity</td><td>Low complexity</td><td>Low complexity</td><td>High complexity</td><td>High complexity</td></tr><tr><td rowspan="4">Trustor features</td><td>Personal relevance</td><td>Low personal relevance</td><td>High personal relevance</td><td>Low personal relevance</td><td>High personal relevance</td></tr><tr><td>Motivational goals</td><td>Low motivational goals</td><td>High motivational goals</td><td>Low motivational goals</td><td>High motivational goals</td></tr><tr><td>Affective state</td><td>Low affective state</td><td>Low affective state</td><td>High affective state</td><td>High affective state</td></tr><tr><td>Cognitive capacity</td><td>Low cognitive capacity</td><td>High cognitive capacity</td><td>Low cognitive capacity</td><td>High cognitive capacity</td></tr><tr><td rowspan="2">Situation features</td><td>Need for accuracy</td><td>Low need for accuracy</td><td>High need for accuracy</td><td>Low need for accuracy</td><td>High need for accuracy</td></tr><tr><td>Availability of criteria</td><td>High availability of criteria</td><td>High availability of criteria</td><td>Low availability of criteria</td><td>Low availability of criteria</td></tr></table>

#

Social desirability

Low social desirability

Low social desirability

High social desirability

High social desirability

![](/api/attachments/TDRJDNZ6/fulltext/images/bb2402e13cd5e8748ceb516e94a2aa40e5d1ce7f90cc9af66bea858840e4dda0.jpg)  
Figure 1. Newly Proposed Affect-Trust Infusion Model (ATIM)

with the Web site would transfer to the Web site’s vendor. The dual-experiment design allows us to discover the different effects of PWP and PE on trust in a low- versus high-AFI online interaction. Through the collective testing of the three hypotheses, we were also able to empirically confirm that Study 1 involved low-AFI while Study 2 involved high-AFI, as explained in the Results section.

## 3.1 STUDY 1: DESIGN

This study was a field experiment designed to test ATIM. Specifically, we used a free-response experiment to let the participants experience a real Web site and tested their reactions to the experience through structural equation modeling, as has been done in related studies [64]. Though we were testing a path model, we manipulated color preferences to further create PE variation in the model, as also has been done in related studies [64]: Half of the subjects had the Web site set up with their favorite Web site color combinations, and half received their least favorite color combinations, as determined with a pre-experiment survey. The purpose of the color manipulation was to generate a range of PE that helps further demonstrate that the mere presence of PE does not drive AFI—instead, if the AIM holds, the underlying processing strategy chosen drives AFI. No other manipulations or experimental treatments were used.

## 3.2 STUDY 1: PARTICIPANTS

A total of 213 participants from sections of a large history course required of all sophomore-level students at a large private university in the western United States volunteered to participate. Out of 213 responses, 6 were removed due to significant missing data (more than 30% of the questions), leaving 207 valid responses. The participants represented a broad spectrum of majors. Gender was distributed as follows: 50.7% were male, and 49.3% were female. Ethnicity was distributed as follows: 88.7% were Caucasian, 3.8% were Hispanic, 2.3% were Asian, and 5.2% were other ethnicities. The gender and ethnicity distributions closely represented the overall distributions at the university. No additional course credit or payment was provided for participation; instead, participants were entered in a drawing to win iPods. However, the readings task the participants performed was part of the normal readings for the course, so the respondents’ participation in the study had an impact on their course grade through the degree to which they understood the readings and associated course concepts that the participants were tested on. Institutional Review Board approvals were granted, and all rules were followed.

## 3.3 STUDY 1: TOOL AND TASK

The history course from which we solicited volunteers had a series of somewhat arcane historical readings required of all students. We asked the participants to perform three of their normally required readings using a Web site that we created to provide the readings electronically; the Web site also included an online dictionary integrated with the

#

text to provide definitions for much of the arcane language used in the readings. Because the participants had a reasonably clear idea of what information they needed to retrieve and were given a specific system to use (it was simple and familiar, like Google and online dictionaries), they were able to employ specific and targeted search strategies. The participants were also able to intuitively know if they understood a word or not and decide when the needed help with a definition.

The participants used their experiences with this Web site to evaluate their Web site experiences. The dictionary tool itself was particularly useful to the participants because the readings involved were old and often used arcane language with which many of the participants were not likely to be familiar but had an important relationship to learning the course concepts on which the participants were graded. When participants discovered an unfamiliar word, they double-clicked on the word to see the definition alongside the reading. Participants were allowed to use this feature with the frequency they desired. Considering this background, we believe that Study 1 most likely induced motivated processing in the participants, as summarized in Table 2.

## 3.4 STUDY 1: PROCEDURES

Participants were invited to participate and given a URL for a Web site that explained the details of the study. Volunteers were given three weeks to complete the pre-experiment questionnaire (with a minimum of 10 days required to complete the pre-experiment questionnaire before starting the experiment), read the articles on the experimental site, and complete the post-experiment questionnaire. This block of time was allotted to reduce monomethod bias and instrumentation fatigue. Participants were advised that they had to fully participate in the experiment and do their best to answer the questions carefully to be eligible to participate in the drawing for iPods. The participants were also strictly prohibited, as a violation of the experiment, from discussing their answers or experiences with other

Table 2. Why Study 1 Most Likely Induced Motivated Processing in the Participants

<table><tr><td colspan="2">Primary contextual features that drive the AFI strategy</td><td>Target levels of features for motivated processing</td><td>Manipulation to induce motivated processing</td></tr><tr><td rowspan="3">Trust target features</td><td>Familiarity</td><td>High familiarity</td><td>Search feature similar to Google and online dictionaries; readings in a familiar layout and format.</td></tr><tr><td>Typicality</td><td>High typicality</td><td>Search feature similar to Google and online dictionaries; readings used were typical of all the readings in the course.</td></tr><tr><td>Complexity</td><td>Low complexity</td><td>Very simple search feature—e.g., enter word, get integrated results in context of the readings.</td></tr><tr><td rowspan="4">Trustor features</td><td>Personal relevance</td><td>High personal relevance</td><td>Task is part of a graded, required introductory course; participants need to understand the readings and associated terminology to do well in the course.</td></tr><tr><td>Motivational goals</td><td>High motivational goals</td><td>Assuming participants wanted to pass and do well in the course and move on to upper-level coursework, motivation should have been high because task helped them with readings. Also provided prizes of great value and interest to the students (iPods).</td></tr><tr><td>Affective state</td><td>Low affective state</td><td>The task is straightforward with a clear path and objective that is focused on reading comprehension.</td></tr><tr><td>Cognitive capacity</td><td>High cognitive capacity</td><td>These college-level readings were complex and involved arcane language that challenged the participants&#x27; reading comprehension.</td></tr><tr><td rowspan="3">Situation features</td><td>Need for accuracy</td><td>High need for accuracy</td><td>To be able to understand the readings, the participants needed to understand everything in context—especially the arcane language, which can provide key insights into understanding.</td></tr><tr><td>Availability of criteria</td><td>High availability of criteria</td><td>The criteria for the participants were simple: Did I understand the readings or not? Did the definition make sense or not?</td></tr><tr><td>Social desirability</td><td>Low social desirability</td><td>This was an individual task with no social or group interaction.</td></tr></table>

participants until the experimental period had been completed.

Our site tracked each volunteer’s usage; once a volunteer had completed three of his or her readings with the tool, the post-experiment survey was made available, at which time he or she was required to complete it. No particular level of tool use was required other than accessing the readings online with the tool. The experimental data were periodically checked to ensure that the participants were doing the readings and using the tool; participants were

#

reminded about the experiment requirements when the participants lagged behind on the readings and tool use.

## 3.5 STUDY 1: MEASURES

The operationalization of PWP is dependent on the type and purpose of a website. The purpose of the website used in Study 1 is to provide users with quality information relevant to their readings in an interactive fashion. Hence, in conceptualizations of PWP used in previous studies. For example, interactivity has been suggested as an important component of PWP [82] and has been used to evaluate the performance of websites with the purpose of facilitating positive interaction [6]. This theoretically salient, pragmatic use of interactivity is highly congruent with AIM and our study’s constructs: Extensive IS and marketing literature has established that Web site or systems interactivity indicates the degree to which users are cognitively and emotionally involved in a Web site; the degree to which they find it compelling, usable, and effective to use; and thus can strongly positively influence desirable outcomes such as continued involvement, sense of presence, trust, collaboration, positive attitude, satisfaction, loyalty, purchase intentions [15, 16, 18, 21, 23, 32, 37, 47, 48, 55, 59-61, 64, 71, 102, 111, 126].

Given that interactivity provides an exceptionally strong theoretical fit to our study, we then chose the most established interactivity measures. The three most established reflective subconstructs of interactivity that we used are pragmatic and generalizable PWP measures in our experiments because both systems used in our experiments (1) allow the user to control the interaction (e.g., navigating the documents and choosing words to define or navigating the virtual world and choosing actions to perform); (2) provide two-way communication through displaying responses based on information requested (e.g., providing definitions for words or rendering virtual world experiences); and (3) provide synchronous or immediate responses based information requested. Importantly, our chosen interactivity measures reflect PWP generally, and are not specific to accomplishing a particular task; thus, they are generalizable to both of our studies. Again, these three subconstructs have been widely used in previous studies to measure system performance in a wide variety of tasks and contexts [15, 16, 18, 21, 23, 32, 37, 47, 48, 55, 59-61, 64, 71, 102, 111, 126]. Because Study 1 included an information search task (highly congruous with motivated processing), the study included a measure of information quality received during the interaction to further represent this PWP aspect of interaction [67].

PE was adapted from Zhang and Li [124] as a general measurement of positive emotion that encompasses more

#

specific instantiations such as perceived enjoyment and satisfaction. Content validity of PE was established through rigorous instrument development procedures described in [124] to insure it could sufficiently represent the domain. Although similarities exist between the PE instrument and these specific instantiations, PE is generalizable to all positive emotion and not limited to any specific instantiation. In our study, we had participants self-report their positive emotions<sup>vii</sup>. Based on deep evolutionary roots, an emotion is a conscious but subjective experience that manifests itself by psychophysiological expressions, biological reactions, and mental states; and thus emotions are the driving force of positive or negative motivations [87]. Though emotion is complex, it is readily measured through self-report because it is easily recalled and closely integrated with cognition [97]. The trusting beliefs measures were adapted from McKnight et al. [69] to focus on conducting future online transactions with the vendor that owned the Web site. See Appendix 2 for measurement detail.

## 3.6 STUDY 2: DESIGN

Study 2 was a controlled laboratory experiment involving two different virtual world experiences. Because of the hedonic nature of virtual world systems, which require high interaction, a laboratory experiment was a suitable choice as this experiment provides the most control over confounding variables and an environment for user-system immersion. Similar to the color manipulation in Study 1, we created one virtual world designed to induce a range of measurable PE. Each participant was randomly assigned to one of the two conditions. Like Study 1, the manipulation’s purpose was to further demonstrate that AFI is not driven by PE but by a user’s processing strategy in his or her contextual environment.

## 3.7 STUDY 2: PARTICIPANTS

110 participants participated; all were from a large private university in the western United States. Participants came from several sophomore- and junior-level IS, business, and general education courses. The demographic information of our participants is summarized as follows: age $( \mu = 2 2 . 9 2 , \mathrm { S D } = 5 . 4 5 )$ and number of years of college education $( \mu = 2 . 4 4 , \mathrm { S D } = 1 . 1 7 )$ . Gender was distributed as follows: 68.2% male, 30.9% female, and 0.9% not reported. Instructors of the participating sections gave token extra credit, but no evaluation criteria were given to the participants to receive the extra credit—they could participate or not, and their participation was not evaluated. We also provided a drawing for three iPods and several movie passes. All human-subjects protocols were followed, and IRB approval was given. Participation was voluntary, and alternatives were available to earn the extra credit.

#

## 3.8 STUDY 2: RULES AND CONTROLS

Study 2 had strong laboratory experiment controls. Like Study 1, Study 2 was refined with a pilot test. Participants were randomly assigned to a laboratory session that included only one virtual world experience (positive or negative). Before participants were exposed to their treatment, all were shown the same scripted instructional video that introduced them to the virtual world. This video was intentionally created to provide a “baseline” expectation of their experience, and thus showed some of the basic features of the virtual world without our positive or negative manipulations.

After the video was shown, participants were given either a positive or a negative virtual world experience. The positive-treatment participants used avatars such that each had a unique appearance and name. Male participants were given male avatars, and female participants were given female avatars. In the negative treatment, all participants used male avatars with the exact same appearance dressed in bright, distracting colors; each avatar had the same name with a different number appended to the end of the name. Furthermore, avatars in the positive treatment were given full navigation control while avatars in the negative treatment were given limited and awkward controls (e.g., left-arrow key for a right turn, up-arrow key for moving backward).

The virtual world interaction included two experiences that had a logical relationship with each other, and the experiences were designed to have no utilitarian or important goal or criteria by which the task could be measured. The first experience involved watching a video in a virtual apartment and then exploring the apartment. The video in the positive treatment was humorous while the video in the negative treatment was dull and repetitive. The apartment in the positive treatment was large, fully furnished, aesthetically pleasing, and easy to navigate while the apartment in the negative treatment was dark, empty, and difficult to navigate.

In the second experience, participants’ avatars teleported to a dance floor and interacted with the other participants to help induce social influence. They were given instructions on how to perform various dance moves and on how to chat with others but with no indicated goals. The positive dance experience was on an aesthetically pleasing island; in the negative experience, the dance moves were limited, the music was repetitive, and the colors were annoying. In summary, we believe that Study 2 most likely induced heuristic processing, as summarized in Table 3.

## 3.9 STUDY 2: MEASURES

As in Study 1, the pre-experiment data were gathered 10 days before the treatments. This data collection was accomplished as part of a sign-up process to reduce test-retest fatigue, to reduce testing threats to validity, to decrease mono-method bias, and to assign experimental conditions randomly in a balanced fashion. The same measures were used in Study 2 as in Study 1 with the exception of information quality, as there was no informationrelated interaction in Study 2. PWP was again operationalized as Web site interactivity because the primary purpose of this website’s design is to promote positive interaction. The same trusting beliefs measures used in Study 1 were used in Study 2.

Table 3. Why Study 2 Most Likely Induced Heuristic Processing in the Participants

<table><tr><td colspan="2">Primary contextual features that drive the AFI strategy</td><td>Target level of features for heuristic processing</td><td>Manipulation to induce heuristic processing</td></tr><tr><td rowspan="3">Trust target features</td><td>Familiarity</td><td>Low familiarity</td><td>First-time exposure to this virtual world environment</td></tr><tr><td>Typicality</td><td>Low typicality</td><td>Very atypical virtual world setup</td></tr><tr><td>Complexity</td><td>High complexity</td><td>Completely unrelated and illogical tasks with high vivid media that increased environment complexity; the tasks were also unfamiliar and abnormal</td></tr><tr><td rowspan="4">Trustor features</td><td>Personal relevance</td><td>Low personal relevance</td><td>Little relevance to anything in their daily lives</td></tr><tr><td>Motivational goals</td><td>Low motivational goals</td><td>Little motivation: received token extra credit whether they were highly involved or not; no impact on any course or grades, and no evaluation involved</td></tr><tr><td>Affective state</td><td>High affective state</td><td>A high affective state was induced through two conditions that made the experience either fun or very annoying</td></tr><tr><td>Cognitive capacity</td><td>Low cognitive capacity</td><td>Conducting the tasks themselves required low cognitive capacity</td></tr><tr><td rowspan="3">Situation features</td><td>Need for accuracy</td><td>Low need for accuracy</td><td>Because the subjects did not know what the purpose of the experience, and they were not evaluated on their experience, there was little inducement to worry about accuracy</td></tr><tr><td>Availability of criteria</td><td>Low availability of criteria</td><td>Because the subjects did not know what the purpose of the experience was and it was complex and confusing, they would not readily know what criteria would be useful and what would not be</td></tr><tr><td>Social desirability</td><td>High social desirability</td><td>Because there were others in the virtual world with whom the subjects were allowed to interact, there was potential for social influence and the ability to be embarrassed if they did not know how to finish a task, did not know how to chat, said something that others did not agree with, and so on.</td></tr></table>

## 4.0 ANALYSIS AND RESULTS

We used partial least squares (PLS), using SmartPLS version 2.0 [93] for model analysis. Pre-analysis was conducted for five tests before final analysis: (1) factorial validity, (2) reliability, (3) multicollinearity, (4) commonmethods bias, and (5) mediation. These details are as follows: We followed standard practices for establishing the factorial validity of reflective constructs. According to Gefen and Straub [29], “convergent validity is shown when each of the measurement items loads with a significant t-value on its latent construct” (p. 93). To do so, we generated a bootstrap with 500 resamples. We then examined the t-values of the outer model loadings; all of the

outer loadings were significant at the .05 α level (see Table A2.1 in online Appendix 2 for both studies). These results indicate convergent validity for the constructs.

To establish the discriminant validity of our reflective indicators, we used two established techniques: (1) correlating the latent variable scores against the indicators (Table A2.2a and Table A2.2b)<sup>viii</sup> and (2) calculating the average variance extracted (AVE) (Table A2.3a and Table A2.3b)<sup>ix</sup>. The first analysis indicated very strong discriminant validity with only three items removed in Study 1 and one item removed in Study 2 to conservatively improve discriminant validity. The AVE analysis for both studies showed very strong discriminant validity for all subconstructs and thus further confirmed our item choices.

We then established the reliability<sup>x</sup> of the reflective constructs. PLS computes a composite reliability<sup>xi</sup> score as part of the integrated model analysis (see Table A2.4). Each reflective construct in our research model demonstrated high levels of reliability that more than met the standard thresholds.

Multicollinearity within constructs can undermine the validity of the results of a structural equation model, and thus should be assessed before analysis is conducted [41, 53]. For reflective constructs, low levels of multicollinearity are usually indicated with levels of the variance inflation factor (VIF) below 10. All of the indicators’ VIFs in Study 1 were below this standard threshold, with the exception of three items that were subsequently removed for extra caution. Study 2 had 10 items slightly above this threshold, and thus, they too were removed to ensure conservative analysis.

Common methods variance (CMV) is an important risk to consider in an analysis. Although many post-hoc analytical procedures have been proposed to minimize or remedy CMV, the most effective methods are procedures built into data collection procedures to prevent it in the first place [88]. To diminish the likelihood of common methods bias occurring in our data collection, we collected the pre-test and post-test responses several days apart. We also randomized items within the instrument so that participants would be less apt to detect underlying constructs, another potential source of CMV [19, 107]. An examination of the correlation matrix of the constructs revealed no correlations above 0.90, the presence of which would be strong evidence that common methods bias exists [83].<sup>xii</sup> Measurement model statistics are summarized in Table 4 and Table 5, and in no case were the correlations near this threshold. We thus conclude that the analyses for both Study 1 and 2 have negligible influence due to common methods bias.

Table 4. Measurement Model Statistics for Study 1

<table><tr><td>Measure</td><td>μ</td><td>SD</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Disposition to trust (1)</td><td>5.1</td><td>0.6</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Institution-based trust (2)</td><td>4.4</td><td>1.0</td><td>0.257</td><td></td><td></td><td></td><td></td></tr><tr><td>Trusting beliefs (3)</td><td>5.3</td><td>0.8</td><td>0.152</td><td>0.252</td><td></td><td></td><td></td></tr><tr><td>Interactivity (4)</td><td>5.0</td><td>0.8</td><td>-0.001</td><td>-0.064</td><td>0.244</td><td></td><td></td></tr><tr><td>Information quality (5)</td><td>6.0</td><td>0.7</td><td>0.136</td><td>0.144</td><td>0.375</td><td>0.316</td><td></td></tr><tr><td>PE (6)</td><td>4.7</td><td>1.9</td><td>0.037</td><td>0.052</td><td>0.281</td><td>0.333</td><td>0.336</td></tr></table>

Table 5. Measurement Model Statistics for Study 2

<table><tr><td>Measure</td><td>μ</td><td>SD</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Disposition to trust (1)</td><td>5.0</td><td>0.8</td><td></td><td></td><td></td><td></td></tr><tr><td>Institution-based trust (2)</td><td>4.9</td><td>0.9</td><td>.443</td><td></td><td></td><td></td></tr><tr><td>Trusting beliefs (3)</td><td>4.5</td><td>1.2</td><td>.281</td><td>.159</td><td></td><td></td></tr><tr><td>Interactivity (4)</td><td>4.2</td><td>1.4</td><td>.131</td><td>-.104</td><td>.452</td><td></td></tr><tr><td>PE (5)</td><td>3.9</td><td>1.8</td><td>.149</td><td>-.082</td><td>.501</td><td>.775</td></tr></table>

We then tested whether users’ PE mediated the effect of PWP on Web vendor trust based on the standard mediation tests by Baron and Kelly [9] that have been extended to PLS, as seen in [63]. Using a mediation test of both models is an elegant approach to testing our AIM-based model, because in cases of systematic processing, PE should be disintermediated (or greatly diminished) by PWP as the key factor that determines cognitive trust; conversely, in cases of heuristic processing, PE should act as a strong mediator between PWP and cognitive trust. Here, we explain the logic and detail of these analyses.

A variable functions as a mediator when the variable meets the following conditions: variations in levels of the independent variable significantly account for variations in the presumed mediator (i.e., Path A), variations in the mediator significantly account for variations in the dependent variable (i.e., Path B), and when paths A and B are controlled, a previously significant relationship between the independent and dependent variables is no longer significant (Path C), with the strongest demonstration of mediation occurring when Path C is zero [9]. Notably, Paths A, B, and C must be present and significant on their own in order for a model to be a candidate for mediation. We performed these tests for Study 1 and Study 2 as follows:

Study 1. As the baseline requisite condition for a model to be a candidate for the presence of a mediator and to test for mediation, all standalone paths were statistically significant when analyzed separately: Standalone Path A between the IV (PWP) and the potential mediator (PE) had a β of 0.598 and was significant at $t _ { ( 1 , 2 1 2 ) } = 1 7 . 0 0 7$ Standalone Path B between the potential mediator (PE) and DV (trust) had a β of 0.131 and was significant at t<sub>(1,</sub> <sub>212)</sub> = 4.084. Standalone Path C between the proposed IV (PWP) and DV (trust) had a β of 0.431 and was significant at $t _ { ( 1 , 2 1 2 ) } = 9 . 3 8 5$ . Given that the model was an appropriate candidate for the potential presence of mediation, the final step was to test Path C while controlling for Path A and Path $\mathbf { B } ^ { \mathrm { x i i i } }$ . The result of this analysis was as follows: Path A had a significant β of 0.596 at $t _ { ( 1 , 2 1 2 ) } = 1 7 . 5 0 6 $ ; Path B had an insignificant β of 0.091 a $t _ { ( 1 , 2 1 2 ) } = 1 . 9 1 4 ;$ ; Path C had a β of 0.377 at $t _ { ( 1 , 2 1 2 ) } = 5 . 5 8 8$ . This analysis indicates that in Study 1 (the systematic processing condition), PE drops out as a significant factor in predicting trust—deferring to the stronger influence of PWP. This disintermediation is fully consistent with ATIM and supports our overall predictions.

Study 2. First, the standalone paths again met the requisite conditions for the model to be eligible for a mediation test: Path A had a significant β of 0.788 at $t _ { ( 1 , 1 0 9 ) } = 5 4 . 9 3 0$ , Path B had a significant β of 0.330 at $t _ { ( 1 , 1 0 9 ) } = 8 . 0 1 5$ , and Path C had a significant β of 0.247 at $t _ { ( 1 , 1 0 9 ) } = 5 . 4 1 3$ . Second, we tested for all paths together, which resulted in the following: Path A had a significant β of 0.787 at $t _ { ( 1 , 1 0 9 ) } = 4 6 . 6 5 6$ , Path B had a significant β of 0.426 at $t _ { ( 1 , 1 0 9 ) } =$ 7.682, and Path C had an insignificant β of 0.076 at $t _ { ( 1 , 1 0 9 ) } = 1 . 2 8 7$ . This analysis indicates that in Study 2 (the heuristic processing condition), PE acts as full mediator between PWP and trust because the path between PWP and trust drops out of the model. This mediation is also fully consistent with ATIM and supports our overall predictions. See Table 6.

Table 6. Summary of the Results of the Mediation Tests for Both Studies

<table><tr><td>Mediation test step</td><td>Test Condition</td><td>Study 1</td><td>Study 2</td></tr><tr><td>1</td><td>Standalone Path A (PWP → PE) significant?</td><td>Yes</td><td>Yes</td></tr><tr><td>2</td><td>Standalone Path B (PE → trust) significant?</td><td>Yes</td><td>Yes</td></tr><tr><td>3</td><td>Standalone Path C (PWP → trust) significant?</td><td>Yes</td><td>Yes</td></tr><tr><td>4</td><td>Does study&#x27;s model meet required conditions for potential mediation?</td><td>Yes (continue to Steps 5—7)</td><td>Yes (continue to Steps 5—7)</td></tr><tr><td>5</td><td>Controlled Path A (PWP → PE) significant?</td><td>Yes</td><td>Yes</td></tr><tr><td>6</td><td>Controlled Path B (PE → trust) significant?</td><td>No</td><td>Yes</td></tr><tr><td>7</td><td>Controlled Path C (PWP → trust) significant?</td><td>Yes</td><td>No</td></tr><tr><td rowspan="2"></td><td>Summary of findings:</td><td>PE is dis-intermediated by PWP</td><td>PE fully mediates PWP and trust</td></tr><tr><td>Supports our model and AIM?</td><td>Yes; as expected with systematic processing</td><td>Yes; as expected with heuristic processing</td></tr></table>

Finally, Figure 2 depicts the analysis results for Study 1 (low-AFI) juxtaposed against the results for Study 2 (high-$\mathrm { A F I } ) ^ { \mathrm { x i v } }$ . The variance explained is indicated inside each construct. The path coefficients, or betas (βs), are indicated on the paths between two constructs, along with their direction and significance. The significance of the path

estimates was calculated using a bootstrap technique with 200 resamples. Table 7 and Table 8 summarize the hypotheses, the path coefficients, and the t-values for each path for Study 1 and Study 2, respectively. Online Appendix 3 Figure A3.1 and A3.2 depict the full measurement-model results exploded to the indicator level for Study 1 and Study 2, respectively.

![](/api/attachments/TDRJDNZ6/fulltext/images/343e1ce79545ce668cf855924d6cfe53dbaba1c7c6bd6ee0de0c5a35b90cdedb.jpg)  
Figure 2. Study 1 Results (Low-Affect Infusion) vs. Study 2 Results (High-Affect Infusion)

Table 7. Study 1 Summary of Hypotheses, Path Coefficients, and Significance Level

<table><tr><td>Tested paths(S1 = Study 1 (low-AFI); S2 = Study 2 (high-AFI)</td><td>Path coefficient</td><td>t-value</td><td>Supports ATIM?</td></tr><tr><td colspan="4">Hypotheses</td></tr><tr><td>H1 (S1): PWP → PE</td><td>0.596</td><td>17.506***</td><td>Yes</td></tr><tr><td>H2 (S1): PWP → Web vendor trust</td><td>0.377</td><td>5.588***</td><td>Yes</td></tr><tr><td>H3a (S1): PE → Web vendor trust</td><td>0.091</td><td>1.914 (n/s)</td><td>Yes+</td></tr><tr><td colspan="4">Trust Nomological Validity Covariates</td></tr><tr><td>Covariate (S1) Disposition to trust → Web vendor trust</td><td>0.069</td><td>1.416 (n/s)</td><td>No</td></tr><tr><td>Covariate (S1) Disposition to trust → Institution-based trust</td><td>0.272</td><td>7.271***</td><td>Yes</td></tr><tr><td>Covariate (S1) Institution-based trust → Web vendor trust</td><td>0.187</td><td>4.301***</td><td>No</td></tr></table>

\*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001, n/s = not significant; +Supports ATIM because of projected differences in mediation between low- and high-affect infusion

Table 8. Study 2 Summary of Hypotheses, Path Coefficients, and Significance Level

<table><tr><td>Tested paths(S1 = Study 1 (low-AFI); S2 = Study 2 (high-AFI)</td><td>Path coefficient</td><td>t-value</td><td>Supports ATIM?</td></tr><tr><td colspan="4">Hypotheses</td></tr><tr><td>H1 (S2): PWP → PE</td><td>0.787</td><td>46.656***</td><td>Yes</td></tr><tr><td>H2 (S2): PWP → Web vendor trust</td><td>0.076</td><td>1.287(n/s)</td><td>Yes+</td></tr><tr><td>H3a (S2): PE → Web vendor trust</td><td>0.426</td><td>7.682***</td><td>Yes</td></tr><tr><td colspan="4">Trust Nomological Validity Covariates</td></tr><tr><td>Covariate (S2) Disposition to trust → Web vendor trust</td><td>0.226</td><td>5.457***</td><td>Yes</td></tr><tr><td>Covariate (S2) Disposition to trust → Institution-based trust</td><td>0.344</td><td>10.293***</td><td>No</td></tr><tr><td>Covariate (S2) Institution-based trust → Web vendor trust</td><td>0.157</td><td>4.021***</td><td>Yes</td></tr><tr><td colspan="4">*p&lt;0.05, **p&lt;0.01, ***p&lt;0.001, n/s = not significant; +Supports ATIM because of projected differences in mediation between low- and high-affect infusion</td></tr></table>

mediation between low- and high-affect infusion

## 5.0 DISCUSSION

This study proposed a new model, ATIM, which explains and predicts how and when PE will increase Web vendor trust. ATIM predictions are differentiated between two contexts: low- and high-AFI. In high-AFI, users engage in either heuristic or substantive processing when making a judgment of trust, and thereby trust is influenced primarily by PE. In low-AFI, users engage in either motivational or direct access processing when making a judgment of trust, and thereby trust is influenced by PWP, not PE.

## 5.1 SUMMARY OF FINDINGS

Study 1 presented users with a low-AFI scenario intended to encourage motivational processing. In this context, PWP strongly influenced trusting beliefs (H2 fully supported), but PE dropped out of the model (H3a rejected). The opposite phenomenon occurred in Study 2 where users experienced a high-AFI scenario intended to induce heuristic processing: PWP completely dropped out of the model (H2 rejected), but PE strongly influenced trusting beliefs (H3a fully supported). Finally, H3b was fully supported in the high-AFI scenario: namely, full mediation occurred among PWP, PE, and trust. These results provide support for AIM being the theoretical driver of the ATIM, and that the impact of PE on subsequent Web vendor trust is something that can be directly and strongly manipulated by Web site design and Web site usage context.

## 5.2 CONTRIBUTIONS TO RESEARCH AND THEORY

Our key theoretical contribution is the introduction of the AIM into Web vendor trust research via our newly proposed model, ATIM. Our data support the prediction that the AFI context (high or low) is the key driver of whether PWP or the resulting PE from a Web site is the primary driver of Web vendor trust. ATIM can be leveraged to help predict trust formation in a full range of cognitive processing scenarios that systematically vary in the level of AFI involved—from the two low-AFI processing strategies<sup>xv</sup> to the two high-AFI processing strategies<sup>xvi</sup>. Moreover, one’s processing strategy, and thus the degree of AFI, can be more finely predicted using theory-based orthogonal components that directly predict which of the four major cognitive processing strategies will be used in scenarios involving cognitive judgment toward a target. Because the underlying causal mechanisms of Web vendor trust involve cognition, the ATIM should be extendable to other Web-oriented studies involving cognitive judgment. These components include target features<sup>xvii</sup>, judge or user features<sup>xviii</sup>, and situation features<sup>xix</sup>. Using these features in an experimental setting, researchers can manipulate context to be high-AFI or low-AFI as was done in our two experiments.

Our research provides an additional theoretical base to support studies showing emotion influences trust [28, 44, 70, 123, 125]. Notably, our research could help account for apparently contradicting findings on the influence of PWP and PE on trust. For example, Kim et al. [52] found that firm reputation associated with past performance was not a predictor of initial trust; yet, Qureshi et al. [90] found that reputation associated with past performance was a predictor of trust. ATIM thus may be able to explain these contradictions as follows: In the Kim et al. study, the phenomenon of interest was initial trust for an unfamiliar mobile banking system. Hence, in this unfamiliar environment (without existing knowledge or relationships), users would most likely engage in heuristic or substantive processing to assess initial trust—depending on task complexity. They would then experience high-AFI when interacting with the mobile application. It is thus possible that the PE experienced during the system

interaction drove users’ underlying system trust, which was then transferred to the vendor.

Meanwhile, in the Qureshi et al. [90] study, respondents were required to have past purchasing experience of the Web site. In this scenario, because they were familiar with the Web site, users would have more likely engaged in a direct-access processing strategy, which involves low-AFI. In such strategies, performance is expected to be a significant predictor of trust. This trust would initially be based on the users’ PWP and then transferred to the Web vendor as long as the new interaction demonstrated effective and expected PWP, based on previous interactions. Of course, these suggested explanations rooted in ATIM require additional controlled experimentation to test. Accordingly, we suggest that researchers should carefully consider context and specifically AFI in interpreting past studies that infer a relationship between PWP and PE with a social judgment such as trust. Contradictions in these findings point to opportunities to collect further data that illuminate the findings based on our new model. Likewise, future Web vendor trust studies should consider including PE as a mediating variable between PWP social judgment variables.

Web vendor trust resulting from Web site perceptions is also consistent with trust transference literature [e.g., 51, 58, 105]. PE experienced while using a novel Web site positively influenced the cognitive trusting beliefs toward the vendor associated with the site (likely as a result of entitativity). Entitativity could help address Kim’s [51] finding that the effectiveness of branding and referrals is highly dependent on an individual’s underlying cultural dispositions through consideration of the potential (or lack thereof) for trust transference between known and unknown objects.

## 5.3 IMPLICATIONS FOR PRACTICE: LINKING TO USER-CENTERED DESIGN

Assuming our results hold in other empirical settings, the implications for practice are potentially profound and yet can be pragmatically integrated with current leading practices of user-centered design (UCD). Namely, the ATIM can guide Web vendors in adjusting their Web site designs to improve the user experience and further induce Web vendor trust. Based on the target features, judge features, and situation features, Web vendors can identify the possible level of AFI for different situations and different kinds of users. The Web vendor would need to consider not only the experience level of a user (e.g., a new visitor or a highly loyal user) but also the target goals involved in a user’s request (e.g., is he or she searching, browsing, purchasing, or malingering?). This could be a particularly powerful way for unknown Web vendors with new Web sites to get over the trust hurdle that can cause new sites to fail.

Specifically, we posit that great gains in design practice may result if the theoretical orthogonal components of ATIM (i.e., target features, judge or user features, and situation features) that predict cognitive processing strategies are introduced into personalization practices of UCD [e.g., 50, 54, 66, 75, 119]. For example, in a high-AFI context, Web vendors can utilize tools such as multimedia, social networking, and visually appealing wizards to promote PE. The same can be done if a person is casually browsing through a product catalog—specifically not conducting a targeted search. However, if a Web site user is highly experienced with the site, the Web vendor can use personalization to further refine the Web site to improve the user’s targeted use. For example, the Web site could suggest quick transactions for search, purchasing, and the like, which are built based on the user’s last few visits. Rather than wizards, the system could suggest additional information that the user would likely want to consider based on his or her previous requests, product returns, concerns raised with the product support department, and so on. Such improvements can enhance control, interactivity, and two-way communication to further support the focused outcome-orientation of the user.

Extending UCD, designers should understand the mental models of a Web site’s users and then map these models against the actual contextual features that drive their AFI strategies (Table 1). Done systematically, this enhanced UCD-based process could dramatically improve personalization strategies to increase Web vendor trust. Mapping these components to mental models is a logical extension of our work because user mental models are critical to design<sup>xx</sup>.

We complete this section by illustrating how Web designers can systematically understand the mental models of a Web site’s users and then how the designers can systematically map these mental models against the actual contextual features that drive the AFI strategy (Table 1). We explain this process with a hypothetical case as follows: Suppose a new Web vendor wants to tap into the cloud computing market by providing scalable, completely Web-based small-business accounting. Suppose the two primary target markets for this software are (1) small-business entrepreneurs who have little accounting experience and do not have the resources to hire full-time bookkeeping and accounting support and (2) small-business entrepreneurs who have accounting knowledge but simply want to create a highly virtual organization that has as few functional-support employees as possible. The first step in our proposed methodology is to discover the actual requirements for what these users want in a system, but just as important is figuring out the mental models that best fit how the users visualize and understand these requirements. To systematically discover these requirements and mental models, the practitioner would simply

#

follow a traditional UCD-based series of methodologies designed to elicit the target users’ requirements and mental models. These standard methodologies that are well described in the practitioner and academic literature include approaches such as participatory design using techniques such as paper prototyping and high-fidelity throw-away contextual inquiry, usability testing, heuristic evaluation, and so on [e.g., 2, 11, 20, 31, 42, 62, 65, 75, 76, 89, 94, 101].

Based on the derived mental models and requirements, the Web designers would then systematically go through the list of contextual features in Table 1 and map the requirements and models to these features, a process that will indicate key elements necessary in design to evoke specific processing strategies. Once everything is mapped out for a Web site, the designer can go through the actual values represented for the target Web site, and discover the column that best fits the intended Web site use. The column best represented would then most likely represent the AFI strategy that a typical user would employ when using a Web site, and thus highlight whether to put increased emphasis on PWP-focused features or PE-focused features. This process can also help designers make further refinements if their designs send signals that would confuse—not aid—AFI in conjunction with the users’ actual mental models. For example, if half of the features of a Web site showed up in the direct-access processing column (least likely for AFI) and the other half showed up in the substantive processing column (most likely for AFI), this is a signal to the designer that something is incongruous with the Web site design and, if left uncorrected, could signal counterbalancing, crossed signals that will not aid trust development.

In our proposed UCD-based process, the ultimate point would be to make sure that when these choices are corrected they specifically match the users’ mental models so that the underlying AFI processing strategy is congruous with the users’ mental models. Namely, to create congruous UCD and to evoke the greatest improvements in usability and trust, Web site designers must fit the Web site’s design model with the target user’s mental models. This then has the added additional design benefit of being able to know which of the four processing strategies the target users are most likely to engage in.

For example, in our hypothetical case, these two potential major segments of the market would almost certainly create a potential split in the trust-target features, trustor features, and situation features—depending on the level of accounting knowledge the entrepreneur actually has. These differences would thus create different processing strategies for the two target markets. To adhere to fundamental principles of UCD that will enhance usability and

#

trust, the designers must personalize the system in a manner that creates different interfaces for the different mental models that will drive the processing strategies. If the likely processing strategies invoke bi-polar AFI scenarios, then the designers must create radically different designs. In some scenarios, if the likely processing strategies are close on the AFI spectrum and there is a lot of overlap in the features, a designer could conceivably refocus one set of designs to push both target markets into exactly the same processing strategy.

As illustration, consider the importance of whether the target users not only have accounting experience but also the kinds of accounting packages with which users are familiar. The most common small-firm accounting package on the market is QuickBooks™. Hence, for users who are familiar with QuickBooks, the interface needs to be similar to this accounting package if the designer wants the user to experience low complexity, high familiarity, and high typicality; otherwise, the designer is by default creating an experience for these users that has low familiarity, low typicality, and high complexity.

A similar trade-off exists for users who do not have knowledge of a particular package but have knowledge of accounting. For those who understand accounting, terms such as “credits” and “debits” would be familiar, and thus, there would be typical and atypical ways to work with these terms that could tie to a user’s underlying mental models—such as depicting these terms in a tabular form found in a standard introductory-level accounting book. Those unfamiliar with accounting would have no familiarity with these terms and thus no useful mental models. Worse, the typical accounting textbook depiction of debits and credits would have a high likelihood of confusing, not aiding, a user with no accounting experience because of the lack of mental models that relate to these concepts. For such users, eliminating the use of typical design models of “credits” and “debits” altogether may be necessary through hiding these underlying ideas within mental models that the users understand and are comfortable with such as a checkbook ledger.

As an example, in this simple accounting scenario the motivational goals of the two target markets would likely depend on the time of the year and whether they are seeking a cash infusion into their firm. A typical entrepreneur is primarily motivated on a daily basis on market development, sales, customer service, and the like. Accounting would rarely be a primary motivator on a daily basis, but could be strong focus during the close of year-end financials or when seeking external funding. For brevity, we do not continue through every contextual feature and potential mental model for our accounting case, but we conclude with a summary table of what this might look like (see Table 8). If conducted systematically, use of ATIM with the contextual features that drive AFI strategies can

#

improve leading UCD practices.

## 5.4 LIMITATIONS AND FUTURE RESEARCH

A key limitation is that our empirical studies have limited generalizability. First, the results of our study are limited to those websites for which performance can be measured through interactivity and information quality. Furthermore, the studies examined only two Web site scenarios—specifically testing only two of four judgmentprocessing scenarios (heuristic processing and motivated processing) proposed by AIM. However, we believe this was actually a powerful choice for testing our underlying model because these two chosen processing scenarios are the closest on the AFI spectrum. Given that the ATIM held for these two scenarios, ATIM should logically and theoretically hold for direct access and substantive processing because they are the furthest apart on the AFI spectrum—the former being the least likely of the four strategies to infuse PE and the latter being the most likely of the four strategies to infuse PE. Nevertheless, we acknowledge the possibility of alternative situations in which low-AFI strategy accommodates high PE context and vice versa. Testing those scenarios is an opportunity for future theoretical development and empirical research. Furthermore, we acknowledge the need to test the generalizability of our theory to websites for which performance is best measured through constructs other than interactivity or information quality.

Future research should also directly test the moderating influence of affect infusion between the influences of PWP and web vendor trust, and PE and web vendor trust. We conducted two different experiments—one in a high-affect infusion context and one in a low-affect infusion context. Although this design has the strength of demonstrating the model holds in contexts that have traditionally yielded seemingly contradictory results, it does not allow us to easily and directly compare the results between the two experiments. One way to address this need is to manipulate affect infusion within the same experiment. Half of the participants could be randomly assigned to a low-affect infusion group and half of the participants could be randomly assigned to the high-affect infusion group. One could then measure the degree of affect infusion and model it as a moderator in the analysis.

T<sub>a</sub>bl<sub>e</sub> 8<sub>.</sub> A UCD E<sub>xa</sub>m<sub>p</sub>l<sub>e</sub> <sub>o</sub>f C<sub>o</sub>nt<sub>ex</sub>t<sub>ua</sub>l F<sub>ea</sub>t<sub>u</sub>r<sub>es</sub> th<sub>a</sub>t Dri<sub>ve</sub> AFI Str<sub>a</sub>t<sub>eg</sub>i<sub>es</sub> <sub>a</sub>nd S<sub>u</sub>b<sub>seque</sub>nt C<sub>og</sub>niti<sub>ve</sub> Pr<sub>ocess</sub>in<sub>g</sub>

<table><tr><td rowspan="2" colspan="2">Contextual features</td><td colspan="2">Low AFI (Low PE) Strategies:</td><td colspan="2">High AFI (High PE) Strategies:</td></tr><tr><td>Direct access processing</td><td>Motivated processing</td><td>Heuristic processing</td><td>Substantive processing</td></tr><tr><td rowspan="3">Trust target features</td><td>Familiarity</td><td>High if they have an accounting background and/or QuickBooks experience</td><td>High if they have an accounting background and/or QuickBooks experience</td><td>Low with no accounting background and/or no QuickBooks experience</td><td>Low with no accounting background and/or no QuickBooks experience</td></tr><tr><td>Typicality</td><td>High typicality with accounting background and standard accounting system models; or with QuickBooks experiences and a similar interface model is used.</td><td>High typicality with accounting background and standard accounting system models; or with QuickBooks experiences and a similar interface model is used.</td><td>Low typicality w/o accounting background if standard accounting system models used; or w/o QuickBooks experience and a similar interface model is used.</td><td>Low typicality if they do not have an accounting background and accounting mental models are used; or if they do not have QuickBooks experience and similar interface and design models are used that do not match the users&#x27; mental models</td></tr><tr><td>Complexity</td><td>Low with accounting background and/or QuickBooks experience; and/or if firm is a sole-proprietorship with single-state taxation</td><td>Low with accounting background and/or QuickBooks experience; and/or if firm is a sole-proprietorship with single-state taxation</td><td>High w/o accounting background and/or QuickBooks experience); and/or if firm is a complex partnership with multi-state taxation</td><td>High w/o accounting background and/or QuickBooks experience); and/or if firm is a complex partnership with multi-state taxation</td></tr><tr><td rowspan="4">Trustor Features</td><td>Personal relevance</td><td>n/a</td><td>High because they own the company and it is their money</td><td>n/a</td><td>High because they own the company and it is their money</td></tr><tr><td>Motivational goals</td><td>Low for day-to-day operations</td><td>High at end of quarter, end of year, and seeking capital</td><td>Low for day-to-day operations</td><td>High at end of quarter, end of year, and seeking capital</td></tr><tr><td>Affective state</td><td>Low would be a given as this is a mundane task</td><td>Low would be a given as this is a mundane task</td><td>High is possible only through additional design intervention</td><td>High is possible only through additional design intervention</td></tr><tr><td>Cognitive capacity</td><td>Low assumed for those without accounting experience</td><td>High assumed for those with accounting experience</td><td>Low assumed for those without accounting experience</td><td>High assumed for those with accounting experience</td></tr><tr><td rowspan="3">Situation features</td><td>Need for accuracy</td><td>n/a</td><td>High need for accuracy is a given with accounting</td><td>n/a</td><td>High need for accuracy is a given with accounting</td></tr><tr><td>Availability of criteria</td><td>High is likely: the books are balanced or not; the transactions are reconciled or not; there are outstanding payments to be made or not...</td><td>High is likely: the books are balanced or not; the transactions are reconciled or not; there are outstanding payments to be made or not...</td><td>n/a</td><td>n/a</td></tr><tr><td>Social desirability</td><td>Low if no one they know is using the system</td><td>Low if no one they know is using the system</td><td>High possible if close friends, associates, vendors, or clients are using the system</td><td>High possible if close friends, associates, vendors, or clients are using the system</td></tr></table>

Our study did not consider other contextual factors that could impact cognitive trust and trust transference toward a Web site, which are further limitations and opportunities. Such an attempt would be unwieldy and unrealistic for one study but offer interesting opportunities for further generalization and testing of the ATIM. We believe that other uncertainty [24]; computer anxiety, computer self-efficacy, and personal innovativeness with IT [112]; and so forth. For example, in light of Kim’s [51] recent findings on the cultural differences in the salience and effectiveness of branding and referrals, it would be useful to see if cultural differences drive PWP. Future research should examine the influence of these contextual factors on PE, cognitive trust, and trust transference.

Finally, our covariate results point to several possibilities of research. In our context, the covariate findings suggest the possibility that under high-AFI disposition to trust and institution-based trust are additional predictors of Web vendor trust, in addition to PE; yet, this relationship was not shown in the low-AFI context. Further research should consider whether these results represent a potentially important theoretical extension that needs to be added to ATIM. As a possible theoretical explanation for these findings, our high-AFI was induced through factors that encouraged heuristic processing. Notably, in the scenario of heuristic processing that we evoked, the user should have been put in a situation that is not goal-driven and where the trust judgment has little personal relevance or risk and where accuracy in the trust judgment is not necessary. Perhaps because of this less-relevant trust judgment, one’s cognition may be inclined to use one’s personal trusting disposition and institution-based trust rather than systematically creating trusting beliefs for the Web vendor.

## 6.0 CONCLUSION

In conclusion, our study introduced PE and PWP as sources of initial trusting beliefs toward unknown Web site vendors. We proposed a new model, ATIM, which builds on AIM to explain how PWP and PE influence cognitive trusting beliefs depending on whether one is engaged in a low- or high-AFI processing strategy. Our empirical findings from two studies support ATIM, Indicating that ATIM can further inform practice on how to extend leading UCD-based Web site design to maximize Web vendor trust. We thus suggest a methodology that couples UCD and ATIM to further improve extant practice of improving Web vendor trust.

## REFERENCES

1. Agarwal, R. and Karahanna, E. Time flies when you're having fun: Cognitive absorption and beliefs about information technology usage. MIS Quarterly, 24, 4 (2000), 665–694.

2. Agarwal, R. and Venkatesh, V. Assessing a firm's Web presence: A heuristic evaluation procedure for the measurement of usability. Information Systems Research, 13, 2 (2002), 168-186.

3. Ajzen, I. The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50, 2 (1991), 179–211.

4. Ajzen, I. and Fishbein, M. Attitudinal and normative variables as predictors of specific behaviors. Journal of Personality and Social Psychology, 27, 1 (1973), 41-57.

5. Au, N.; Ngai, E. W. T.; and Cheng, T. C. E. Extending the understanding of end user information systems satisfaction formation: An equitable needs fulfillment model approach. MIS Quarterly, 32, 1 (2008), 43–66.

6. Auger, P. The impact of interactivity and design sophistication on the performance of commercial websites for small businesses. Journal of Small Business Management, 43, 2 (2005), 119-137.

7. Ba, S. L. and Pavlou, P. A. Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quarterly, 26, 3 (2002), 243-268.

8. Baron, R. A. Environmentally induced positive affect: Its impact on self-efficacy, task performance, negotiation, and conflict. Journal of Applied Social Psychology, 20, 5 (1990), 368-384.

9. Baron, R. B. and Kenny, D. A. The moderator mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. Journal of Personality and Social Psychology, 51, 6 (1986), 1173-1182.

10. Bart, Y.; Shankar, V.; Sultan, F.; and Urban, G. L. Are the drivers and role of online trust the same for all web sites and consumers? A large-scale exploratory empirical study. Journal of Marketing, 69, 4 (2005), 133-152.

11. Beyer, K. and Holtzblatt, H., Contextual Design: Defining Customer-Centered Systems. San Francisco, CA, USA: Morgan Kaufmann, 1998.

12. Bhattacherjee, A. Understanding information systems continuance: An expectationconfirmation model. MIS Quarterly, 25, 3 (2001), 351–370.

13. Brown, E.; Hobbs, M.; and Gordon, M. A virtual world environment for group work. International Journal of Web-Based Learning and Teaching Technologies, 3, 1 (2008), 1- 12.

14. Brown, S. A.; Venkatesh, V.; Kuruzovich, J.; and Massey, A. P. Expectation confirmation: An examination of three competing models. Organizational Behavior and Human Decision Processes, 105, 1 (2008), 52–66.

15. Burgoon, J. K.; Bonito, J. A.; Bengtsson, B.; Cederberg, C.; Lundeberg, M.; and Allspach, L. Interactivity in human-computer interaction: A study of credibility, understanding, and influence. Computers in Human Behavior, 16, 6 (2000), 553–574.

16. Burgoon, J. K.; Bonito, J. A.; Ramirez, A.; Dunbar, N. E.; Kam, K.; and Fischer, J. Testing the interactivity principle: Effects of mediation, propinquity, and verbal and nonverbal modalities in interpersonal interaction. Journal of Communication, 52, 3 (2002), 657–677.

17. Chae, M. and Kim, J. Do size and structure matter to mobile users? An empirical study of the effects of screen size, information structure, and task complexity on user activities with standard web phones. Behaviour & Information Technology, 23, 3 (2004), 165-181.

18. Chen, K. and Yen, D. C. Improving the quality of online presence through interactivity. Information & Management, 42, 1 (2004), 217-226.

19. Cook, T. D. and Campbell, D. T., Quasi-Experimentation: Design and Analysis for Field

Settings. Chicago: Rand McNally, 1979.

20. Costantine, L. L. and Lockwood, L. A. D., Software For Use - A Practical Guide to the Models and Methods of Usage-Centered Design. Reading, MA, USA: Addison-Wesley, 1999.

21. Coyle, J. R. and Thorson, E. The effects of progressive levels of interactivity and vividness in web marketing sites. Journal of Advertising, 30, 3 (2001), 65-77.

22. Cyr, D. Modeling Web site design across cultures: Relationships to trust, satisfaction, and e-loyalty. Journal of Management Information Systems, 24, 4 (2008), 47-72.

23. Cyr, D.; Head, M.; and Ivanov, A. Perceived interactivity leading to e-loyalty: Development of a model for cognitive-affective user responses. International Journal of Human Computer Studies, 67, 10 (2009), 850-869.

24. Datta, P. and Chatterjee, S. The economics and psychology of consumer trust in intermediaries in electronic markets: the EM-Trust Framework. European Journal of Information Systems, 17, 1 (2008), 12-28.

25. Davis, F. D.; Bagozzi, R. P.; and Warshaw, P. R. Extrinsic and intrinsic motivation to use computers in the workplace. Journal of Applied Social Psychology, 22, 14 (1992), 1111- 1132.

26. Dickinger, A.; Arami, M.; and Meyer, D. The role of perceived enjoyment and social norm in the adoption of technology with network externalities. European Journal of Information Systems, 17, 1 (2008), 4-11.

27. Dinev, T.; Bellotto, M.; Hart, P.; Russo, V.; Serra, I.; and Colautti, C. Privacy calculus model in e-commerce: A study of Italy and the United States. European Journal of Information Systems, 15, 4 (2006), 389-402.

28. Dunn, J. R. and Schweitzer, M. E. Feeling and believing: The influence of emotion on trust. Journal of Personality and Social Psychology, 88, 5 (2005), 736–748.

29. Ermi, L. and Mäyrä, F., Fundamental components of the gameplay experience: Analysing immersion. Presented at Changing Views: Worlds in Play, DiGRA conference, Vancouver, Canada, 2005, pp. 15-27.

30. Everard, A. P. and Galletta, D. F. How presentation flaws affect perceived site quality, trust, and intention to purchase from an online store. Journal of Management Information Systems, 22, 3 (2006), 56-95.

31. Faulkner, C., The Essence of Human-Computer Interaction. Hempstead, UK: Prentice Hall, 1998.

32. Fiore, A. M.; Jin, H.-J.; and Kim, J. For fun and profit: Hedonic value from image interactivity and responses toward an online store. Psychology & Marketing, 22, 8 (2005), 669-694.

33. Fishbein, M. and Ajzen, I., Belief, Attitude, Intention, and Behavior: An Introduction to Theory and Research. Reading, MA, USA: Addison-Wesley, 1975.

34. Forgas, J. P., Affect in social judgments and decisions: A multiprocess model. In. Zanna, Ed.Advances in Experimental Social Psychology, 25. San Diego, CA, USA: Academic Press, 1992, pp. 227-275.

35. Forgas, J. P. Mood and judgment: The affect infusion model (AIM). Psychological Bulletin, 117, 1 (1995), 39–66.

36. Forgas, J. P., The affect infusion model (AIM): An integrative theory of mood effects on cognition and judgments. In. Clore; and Martin, Eds.Theories of Mood and Cognition: A User's Handbook. Mahwah, NJ, USA: Lawrence Erlbaum Associates, 2001, pp. 99–134.

37. Gao, Q.; Rau, P.-L. P.; and Salvendy, G. Perception of interactivity: Affects of four key variables in mobile advertising. International Journal of Human-Computer Interaction, 25, 6 (2009), 479-505.

38. Gefen, D. and Straub, D. W. A practical guide to factorial validity using PLS-Graph: Tutorial and annotated example. Communications of the AIS, 16, 5 (2005), 91-109.

39. Goo, J. and Huang, C. D. Facilitating relational governance through service level agreements in IT outsourcing: An application of the commitment-trust theory. Decision Support Systems, 46, 1 (2008), 216-232.

40. Goodwin, G. and Johnson-Laird, P. N. Reasoning about relations. Psychological Review, 112, 2 (2005), 468-493.

41. Hair, J. F.; Anderson, R. E.; and Tatham, R. L., Multivariate data analysis. New York, NY: Macmillan, 1987.

42. Hix, D. and Hartson, H. R., Developing User Interfaces - Ensuring Usability through Product and Process. New York, NY, USA: John Wiley & Sons, 1993.

43. Hsu, M. H.; Chiu, C. M.; and Ju, T. L. Determinants of continued use of the WWW: An integration of two theoretical models. Industrial Management & Data Systems, 104, 9 (2004), 766–775.

44. Hwang, Y. J. and Kim, D. J. Customer self-service systems: The effects of perceived Web quality with service contents on enjoyment, anxiety, and e-Trust. Decision Support Systems, 43, 3 (2007), 746-760.

45. Isen, A. M., Positive affect, cognitive processes, and social behavior. In. Berkowitz, Ed.Advances in Experimental Social Psychology, 20. New York, NY, USA: Academic Press, Inc., 1987, pp. 203-253.

46. Isen, A. M.; Daubman, K. A.; and Nowicki, G. P. Positive affect facilitates creative problem solving. Journal of Personality and Social Psychology, 52, 6 (1987), 1122-1131.

47. Jiang, Z.; Chan, J.; Tan, B.; and Chua, W. Effects of interactivity on website involvement and purchase intention. Journal of the Association for Information Systems, 11, 1 (2010), 34-59.

48. Jiang, Z. H. and Benbasat, I. Investigating the influence of the functional mechanisms of online product presentations. Information Systems Research, 18, 4 (2007), 454-470.

49. Johnson-Laird, P. N., Mental models in thought. In. Holyoak; and Sternberg, Eds.The Cambridge Handbook of Thinking and Reasoning. Cambridge, UK: Cambridge University Press, 2005, pp. 179-212.

50. Karat, J. Evolving the scope of user-centered design. Communications of the ACM, 40, 7 (1997), 33-38.

51. Kim, D. J. Self-perception-based versus transference-based trust determinants in computermediated transactions: A cross-cultural comparison study. Journal of Management Information Systems, 24, 4 (2008), 13-45.

52. Kim, G.; Shin, B.; and Lee, H. G. Understanding dynamics between initial trust and usage intentions of mobile banking Information Systems Journal, 19, 3 (2009), 283-311.

53. Kline, R. B., Principles and practice of structural equation modeling. New York, NY: The Guilford Press, 1998.

54. Kramer, J.; Noronha, S.; and Vergo, J. A user-centered design approach to personalization. Communications of the ACM, 43, 8 (2000), 44-48.

55. Lee, T. The impact of perceptions of interactivity on customer trust and transaction intentions in mobile commerce. Journal of Electronic Commerce Research, 6, 3 (2005),

165-180.

56. Liao, C. C.; Chen, J. L.; and Yen, D. C. Theory of planning behavior (TPB) and customer satisfaction in the continued use of e-Service: An integrated model. Computers in Human Behavior, 23, 6 (2007), 2804–2822.

57. Liljander, V. and Strandvik, T. Emotions in service satisfaction. International Journal of Service Industry Management, 8, 2 (1997), 148-169.

58. Lim, K. H.; Sia, C. L.; Lee, M. K. O.; and Benbasat, I. Do I trust you online, and if so, will I buy? An empirical study of two trust-building strategies. Journal of Management Information Systems, 23, 2 (2006), 233-266.

59. Liu, Y. Developing a scale to measure the interactivity of websites. Journal of Advertising Research, 43, 2 (2003), 207–216.

60. Liu, Y. and Shrum, L. J. What is interactivity and is it always such a good thing? Implications of definition, person, and situation for the influence of interactivity on advertising effectiveness. Journal of Advertising, 31, 4 (2002), 53–64.

61. Liu, Y. and Shrum, L. J. A dual process model of interactivity effects. Journal of Advertising, 38, 2 (2009), 53-68.

62. Lowry, P. B.; Roberts, T. L.; Dean, D.; and Marakas, G. M. Toward building self sustaining groups in PCR-based tasks through implicit coordination: The case of heuristic evaluation. Journal of the Association for Information Systems, 10, 3 (2009), 170-195.

63. Lowry, P. B.; Romano, N. C.; Jenkins, J. L.; and Guthrie, R. W. The CMC interactivity model: How interactivity enhances communication quality and process satisfaction in leanmedia groups. Journal of Management Information Systems, 26, 1 (2009), 155-195.

64. Lowry, P. B.; Vance, A.; Moody, G.; Beckman, B.; and Read, A. Explaining and predicting the impact of branding alliances and web site quality on initial consumer trust of ecommerce web sites. Journal of Management Information Systems, 24, 4 (2008), 199-224.

65. Lucas, E. J. and Ball, L. J. Think-aloud protocols and the selection task: Evidence for relevance effects and rationalization processes. Thinking and Reasoning, 11, 1 (2005), 35- 66.

66. Mao, J.-Y.; Vredenburg, K.; Smith, P. W.; and Carey, T. The state of user-centered design practice. Communications of the ACM, 48, 3 (2005), 105-109.

67. McKinney, V.; Kanghyun, Y.; and Fatemeh, Z. The measurement of Web-customer satisfaction: An expectation and disconfirmation approach. Information Systems Research, 13, 3 (2002), 296–315.

68. McKnight, D. H. and Chervany, N. L. What trust means in e-commerce customer relationships: An interdisciplinary conceptual typology. International Journal of Electronic Commerce, 6, 2 (2001), 35-59.

69. McKnight, D. H.; Choudhury, V.; and Kacmar, C. Developing and validating trust measures for e-commerce: An integrative typology. Information Systems Research, 13, 3 (2002), 334-359.

70. McKnight, D. H.; Cummings, L. L.; and Chervany, N. L. Initial trust formation in new organizational relationships. Academy of Management Review, 23, 3 (1998), 473-490.

71. McMillan, S. J.; Jang-Sun, H.; and Guiohk, L. Effects of structural and perceptual factors on attitudes toward the website. Journal of Advertising Research, 43, 4 (2003), 400-409.

72. Milliman, R. E. and Fugate, D. L. Using trust-transference as a persuasion technique: An empirical field investigation. Journal of Personal Selling and Sales Management, 8, 2 (1988), 1-7.

73. Muller, T. E.; Tse, D. K.; and Venkatasubramaniam, R. Post-consumption emotions: Exploring their emergence and determinants. Journal of Consumer Satisfaction, Dissatisfaction and Complaining Behavior, 4, 1991 (1991), 13-20.

74. Murphy, S. T. and Zajonc, R. B. Affect, cognition, and awareness: Affective priming with optimal and suboptimal stimulus exposures. Journal of Personality and Social Psychology, 64, 5 (1993), 723-739.

75. Nielsen, J., Usability engineering. Boston, MA, USA: Academic Press, 1993.

76. Norman, D., The Design of Everyday Things. New York, NY, USA: Doubleday/Currency, 1988.

77. Novak, T. P.; Hoffman, D. L.; and Yiu-Fai, Y. Measuring the customer experience in online environments: A structural modeling approach. Marketing Science, 19, 1 (2000), 22–42.

78. Oliver, R. L. Effect of expectation and disconfirmation on postexposure product evaluations: An alternative interpretation. Journal of Applied Psychology, 62, 4 (1977), 480–486.

79. Oliver, R. L. A cognitive model of the antecedents and consequences of satisfaction decisions. Journal of Marketing Research, 17, 4 (1980), 460–469.

80. Oliver, R. L. Measurement and evaluation of satisfaction processes in retail settings. Journal of Retailing, 57, 3 (1981), 25-48.

81. Oliver, R. L. Cognitive, affective, and attribute bases of the satisfaction response. Journal of Consumer Research, 20, 3 (1993), 418-430.

82. Palmer, J. Web site usability, design, and performance Metrics. Information Systems Research, 13, 2 (2002), 151-167.

83. Pavlou, P.; Liang, H.; and Xue, Y. Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quarterly, 31, 1 (2007), 105- 136.

84. Pavlou, P. A. Consumer acceptance of electronic commerce: Integrating trust and risk with the technology acceptance model. International Journal of Electronic Commerce, 7, 3 (2003), 101-134.

85. Pavlou, P. A. and Fygenson, M. Understanding and predicting electronic commerce adoption: An extension of the theory of planned behavior. MIS Quarterly, 30, 1 (2006), 115-143.

86. Pavlou, P. A. and Gefen, D. Building effective online marketplaces with institution-based trust. Information Systems Research, 15, 1 (2004), 37-59.

87. Plutchik, R. The nature of emotions. American Scientist, 89, 4 (2001), 344-350.

88. Podsakoff, P. M.; MacKenzie, S. B.; Lee, J. Y.; and Podsakoff, N. P. Common method biases in behavioral research: A critical review of the literature and recommended remedies. Journal of Applied Psychology, 88, 5 (2003), 879-903.

89. Preece, J., Human-Computer Interaction. Reading, MA, USA: Addison-Wesley, 1994.

90. Qureshi, I.; Fang, Y.; Ramsey, E.; Mccole, P.; Ibbotson, P.; and Compeau, D. Understanding online customer repurchasing intention and the mediating role of trust: An empirical investigation in two developed countries European Journal of Information Systems, 18, 3 (2009), 205-222.

91. Rafaeli, A. and Vilnai-Yavetz, I. Emotion as a connection of physical artifacts and organizations. Organization Science, 15, 6 (2004), 671-686.

92. Raykov, T. and Grayson, D. A test for change of composite reliability in scale

development. Multivariate behavioral research, 38, 2 (2003), 143-159.

93. Ringle, C. M.; Wende, S.; and Will, S. SmartPLS 2.0 (M3) Beta. (2005), Date last accessed: September 17, 2010, retrieved from http://www.smartpls.de

94. Rubin, J., Handbook of Usability Testing. New York, NY, USA: John Wiley & Sons, 1994.

95. Russell, J. A. Core affect and the psychological construction of emotion. Psychological Review, 110, 1 (2003), 145–172.

96. Russell, J. A.; Weiss, A.; and Mendelsohn, G. A. Affect grid: A single-item scale of pleasure and arousal. Journal of Personality and Social Psychology, 57, 3 (1989), 493-502.

97. Scherer, K. R. What are emotions? And how can they be measured? Social Science Information, 44, 4 (2005), 695-729.

98. Schoefer, K. The role of cognition and affect in the formation of customer satisfaction judgments concerning service recovery encounters. Journal of Consumer Behaviour, 7, 3 (2008), 210-221.

99. Shankar, V.; Urban, G. L.; and Sultan, F. Online trust: A stakeholder perspective, concepts, implications, and future directions. Journal of Strategic Information Systems, 11, 2002 (2002), 325-344.

100. Sherry, J. Flow and media enjoyment. Communication Theory, 14, 4 (2004), 328-347.

101. Shneiderman, B., Designing the User Interface - Strategies for Effective Human-Computer Interaction, 4th ed. Reading, MA, USA: Addison-Wesley, 1998.

102. Song, J. H. and Zinkhan, G. M. Determinants of perceived web site interactivity. Journal of Marketing, 72, 2 (2008), 99-113.

103. Spreng, R. A.; MacKenzie, S. B.; and Olshavsky, R. W. A reexamination of the determinants of consumer satisfaction. Journal of Marketing, 60, 3 (1996), 15–32.

104. Staples, D. S.; Hulland, J. S.; and Higgins, C. A. A self-efficacy theory explanation for the management of remote workers in virtual organizations. Organization Science, 10, 6 (1999), 758-776.

105. Stewart, K. J. Trust transfer on the World Wide Web. Organization Science, 14, 1 (2003), 5-17.

106. Straub, D. W. Validating instruments in MIS research. MIS Quarterly, 13, 2 (1989), 147- 169.

107. Straub, D. W.; Boudreau, M. C.; and Gefen, D. Validation guidelines for IS positivist research. Communications of the AIS, 14, 2004 (2004), 380-426.

108. Strub, P. J. and Priest, T. B. Two patterns of establishing trust: The marijuana user. Sociological Focus, 9, 4 (1976), 399-411.

109. Sun, H. and Zhang, P. Causal relationships between perceived enjoyment and perceived ease of use: An alternative approach. Journal of the Association for Information Systems, 7, 9 (2006), 618-645.

110. Sun, H. and Zhang, P., The role of affect in information systems research: A critical survey and a research model. In. Zhang; and Galletta, Eds.Human-Computer Interaction and Management Information Systems: Foundations. Armonk, NY, USA: M.E. Sharpe, 2006.

111. Teo, H.-H.; Oh, L.-B.; Liu, C.; and Wei, K.-K. An empirical study of the effects of interactivity on web user attitude. International Journal of Human-Computer Studies, 58, 3 (2003), 281-305.

112. Thatcher, J. B.; Loughry, M. L.; Lim, J.; and McKnight, D. H. Internet anxiety: An empirical study of the effects of personality, beliefs, and social support. Information & Management, 44, 4 (2007), 353-363.

##

113. Tung, L. L.; Xu, Y.; and Tan, F. B. Attributes of Web site usability: A study of Web users with the repertory grid technique. International Journal of Electronic Commerce, 13, 4 (2009), 97-126.

114. Udo, G. J. and Marquis, G. P. Factors affecting e-commerce web site effectiveness Journal of Computer Information Systems, 42, 2 (2001), 10-16.

115. Uzzi, B. The sources and consequences of embeddedness for the economic performance of organizations: The network effect. American Sociological Review, 61, 4 (1996), 674-698.

116. van der Heijden, H. User acceptance of hedonic information systems. MIS Quarterly, 28, 4 (2004), 695–704.

117. Verhagen, T.; Meents, S.; and Tan, Y.-H. Perceived risk and trust associated with purchasing at electronic marketplaces. European Journal of Information Systems, 15, 6 (2006), 542-556.

118. Vorderer, P.; Klimmt, C.; and Ritterfeld, U. Enjoyment: At the heart of media entertainment. Communication Theory, 14, 4 (2004), 388-408.

119. Vredenberg, K.; Isensee, S.; and Righi, C., User-Centered Design: An Integrated Approach. Saddle River, NJ, USA: Prentice Hall, 2001.

120. Webster, J. and Ahuja, J. S. Enhancing the design of Web Navigation Systems: The Influence of user disorientation on engagement and performance. MIS Quarterly, 30, 3 (2006), 661-678.

121. White, T. B. Consumer disclosure and disclosure avoidance: A motivational framework. Journal of Consumer Psychology, 14, 1/2 (2004), 41-51.

122. Zajonc, R. B. Feeling and thinking: Preferences need no inferences. American Psychologist, 35, 2 (1980), 151-175.

123. Zhang, P. and Li, N., Love at first sight or sustained effect? The role of affective quality on users' cognitive reactions to information technology. in Twenty-Fifth International Conference on Information Systems. Washington, DC, USA, 2004, pp. 283–296.

124. Zhang, P. and Li, N., Positive and negative affect in IT evaluation: A longitudinal study. Presented at Proceedings of the Sixth Annual Workshop on HCI Research in MIS, Montreal, Canada, 2007, pp. 1–5.

125. Zhang, P.; Li, N.; and Sun, H., Affective quality and cognitive absorption: Extending technology acceptance research. Presented at 39th Hawaii International Conference on System Sciences, Kauai, HI, USA, 2006, pp. 201-210.

126. Zhu, L.; Benbasat, I.; and Jiang, Z. H. Let's shop online together: An empirical investigation of collaborative online shopping support. Information Systems Research, 21, 4 (2010), 872-891.

# ENDNOTES FOR REVIEW PROCESS AND ONLINE SUPPLEMENT

<sup>v</sup> Synchronicity refers to the quality of an interaction that reflects an immediacy of response, simultaneous exchange of information, high interaction speed, real-time interaction, synchronous response, and lack of a time lag [60, 63, 77].

<sup>vi</sup> Two-way communication is a form of reciprocal communication where one or more senders and one or more receivers (human or system) communicate with each other [e.g., 15, 16, 47, 63, 111].

<sup>vii</sup> Our implicit assumption is that if a user reports a perception toward a system, there is a high probability that the user is experiencing such an affective state toward that system. For example, if a system is considered exciting by a user, there is a high probability that the user is experiencing such excitement toward that system. Our assumption further supported by studies such as Rafaeli and Vilnai-Yavetz [91] that suggested a connection between emotions toward organizational artifacts and emotions toward the organization.

<sup>ix</sup> “Conceptually, the AVE test is equivalent to saying that the correlation of the construct with its measurement items should be larger than its correlation with the other constructs” [38, p. 94], which is similar to correlation tests with multi-trait multi-method matrices. The AVE is calculated by computing the variances shared by the items of a particular construct (the AVE square roots are represented as the bold and underlined diagonal elements). Off-diagonal elements in the table represent the correlations between the constructs. To establish discriminant validity, the diagonal elements must be greater than the off-diagonal elements for the same row and column [104].

x Reliability refers to the degree to which a scale yields consistent and stable measures over time [106].

<sup>xi</sup> The composite reliability score is similar to Cronbach’s α in that they are both measures of internal consistency. Specifically, composite reliability is an index that reflects the impact of error on the measure [92].

<sup>xii</sup> The traditional approach to establishing lack of common methods bias is to conduct a Harman’s single factor test; however, the validity of this approach is increasingly under attack, and thus, we used an alternative method [83].

<sup>xiii</sup> In SEM, this is simply done by analyzing all of the paths at the same time in their potential mediation network.

#

<sup>xiv</sup> Again, for nomological validity, we included disposition to trust and institution-based trust as potential covariates with trusting beliefs, because these had previously been shown to be important predictors of trusting beliefs [69].

xv Again, these two low-AFI processing strategies are direct access processing and motivated processing.

<sup>xvi</sup> Again, these two high-AFI processing strategies are heuristic processing and substantive processing.

<sup>xvii</sup> For example, these include familiarity, typicality, and complexity.

<sup>xviii</sup>For example, these include personal relevance, motivational goals, affective state, and cognitive capacity.

<sup>xix</sup> For example, these include the need for accuracy, availability of criteria, and social desirability.

<sup>xx</sup> A user’s mental model of a system is how the user believes a system will work based on his or her past experience with systems and even everyday objects that have nothing to do with systems (e.g., a VCR, remote control, elevator buttons). The importance of users’ mental models is demonstrated not just in applied HCI research for practice [e.g., 76, 89] but also in highly theoretical mental models research rooted in psychology [e.g., 40, 49].

Scores of studies and practitioner guides have shown perceived system usability and satisfaction are diminished when a system’s design—particularly, its models of how things work (e.g., icons, graphics, menus, organization, and any kind of representations)—is not in alignment with a user’s mental models of how he or she thinks a target system should work [e.g., 2, 11, 20, 31, 42, 62, 75, 76, 89, 94, 101]. Hence, a substantial gain in usability results when a system’s design model matches the target users’ mental models. For example, Google™ search is so deeply ingrained in how users search that when Web sites provide a drastically different approach to search, the new search model more often than not conflicts with the users’ expected mental search model, and thus creates substantially decreased perceived usability and satisfaction.
