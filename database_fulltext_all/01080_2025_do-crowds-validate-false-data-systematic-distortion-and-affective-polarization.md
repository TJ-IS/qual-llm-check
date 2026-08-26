---
otero_id: 1080
otero_key: "648BV57T"
title: "Do Crowds Validate False Data? Systematic Distortion and Affective Polarization"
authors: "Daniel A. Pienta; Sriram Somanchi; Nishant Vishwamitra; Nicholas Berente; Jason Bennett Thatcher"
year: "2025"
journal: "MIS Quarterly"
doi: "10.25300/misq/2024/17482"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DO CROWDS VALIDATE FALSE DATA? SYSTEMATIC DISTORTION AND AFFECTIVE POLARIZATION<sup>1</sup>

Daniel A. Pienta Department of Accounting and Information Management Haslam College of Business, University of Tennessee, Knoxville, TN, U.S.A. {dpienta@utk.edu}

Sriram Somanchi Department of Information Technology, Analytics, and Operations, Mendoza College of Business, University of Notre Dame, South Bend, IN, U.S.A. {somanchi.1@nd.edu}

Nishant Vishwamitra Department of Information Systems and Cyber Security, Alvarez College of Business, University of Texas at San Antonio, San Antonio, TX, U.S.A. {nishant.vishwamitra@utsa.edu}

Nicholas Berente Department of Information Technology, Analytics, and Operations, Mendoza College of Business, University of Notre Dame, South Bend, IN, U.S.A. {nberente@nd.edu}

Jason Bennett Thatcher Leeds School of Business, University of Colorado Boulder, Boulder, CO, U.S.A., and Alliance Manchester Business School, University of Manchester, Manchester, U.K. {jason.thatcher@colorado.edu}

This research note examines how sociocognitive influences can systematically distort crowdsourced ground truth in event-centric data through subgroups. The “wisdom of the crowd” is based on the assumption that consensus drives accuracy. While existing research addresses the tendencies of the overall crowd, this research note shows that identifiable subgroups within the crowd can systematically influence crowdsource validation. We conducted an immersive experiment to investigate whether crowd consensus can be systematically distorted by subgroup-based sociocognitive influences, such as affective polarization. In the experiment, raters from a range of subgroups with varying levels of affective polarization were asked to view and validate crisis data from a violent public riot in the year 2020. Relying in part on double debiased machine learning techniques, we analyzed heterogeneous treatment effects across subgroups. The results show that affective polarization and more extreme raters, via the constructs of loyalty and betrayal, distort consensus-based ground truth in different ways. This research note demonstrates how subgroup-based sociocognitive influences can systematically distort the results of consensus-based crowdsourced validation. Additionally, it provides guidance for research and practice on how to account for identifiable subgroups in the crowd. These findings challenge key assumptions about the wisdom of crowds and the accuracy of crowdsourced ground truth in event-centric situations.

Keywords: Sociocognitive influences, subgroups, crowdsourcing, data validation, double debiased machine learning

## Introduction

In the era of false news and deepfakes, accurate, real-time validation of event-centric data is critical for managing events as serious as riots or as mundane as the daily commute. Decision makers are increasingly turning to crowdsourced validation of such data to secure ground truth on events (Ahmad et al., 2022; Brynjolfsson et al., 2016; Palmer et al., 2017). By leveraging many raters, crowdsourced validation helps to assess images and videos to glean accurate assessments of events as they unfold in real time (Oh et al., 2013; Tim et al., 2017). The premise behind crowdsourced validation is that consensus among raters, also called the wisdom of the crowd, offers trustworthy evaluations of data and accurate descriptions of events (Avudaiappan et al., 2017; Surowiecki, 2005).

However, the accuracy of the crowd is influenced by its composition (Greenstein & Zhu, 2018), and different aspects of crowd composition can introduce a variety of biases (Becker et al., 2017; Coleman et al., 2009; Hutter et al., 2015; Lasecki et al., 2014). Existing crowdsource validation literature attends to this bias by either focusing on how rater characteristics at an aggregate level or an individual level influence the consensus of the crowd overall (Dissanayake et al., 2019; Taylor & Joshi, 2019; Ye & Kankanhalli, 2017). Such focus overlooks identifiable subgroups in a crowd that may systematically distort crowdsourced validation patterns at a level greater than individuals but lower than the aggregate level of the crowd.

One way to explain the influence of subgroups on the wisdom of the crowd is through sociocognitive theory, which suggests that sociocognitive factors, such as subgroup influences, shape individual cognition (Bandura, 1969; Kunda, 1999). Sociocognitive theory suggests that subgroup influences could impact the veracity of ratings of event-centric data in regular and discernable ways. Subgroups refer to peer groups, communities, and organizations that are comprised of individuals who often share experiences and, consequently, relatively consistent patterns of human cognition (Bandura, 1986; Fiske & Taylor, 1991). Such subgroups in a crowd may introduce biases that can go unobserved in the crowd’s consensus, rendering crowdsourced data validation problematic. If crowdsource validation patterns can be associated with identifiable subgroups, then future research needs to consider how to accurately manage this diversity and its influence. Therefore, we investigate whether sociocognitive influences of subgroups systematically bias crowdsourced validation.

We explore sociocognitive influences by drawing on affective polarization, which describes politically partisan subgroups (Iyengar et al., 2019). Affective polarization refers to how individuals in political subgroups respond to emotional, politically charged issues typically marked by hostility toward an opposing political party. Affective polarization occurs along a political spectrum, with individuals identifying at more or less extreme levels with their political party (Mooijman et al., 2018). Typically, the spectrum of affective polarization is associated with progressive (left) to conservative (right) and involves “partisan shifts” toward, or away from, one’s group (Iyengar et al., 2019; Kitchens et al., 2020). Strong partisan shifts toward one’s group may be associated with extremism (Luttig et al., 2017). Extremism manifests through feelings of group loyalty and betrayal. By understanding affective polarization in terms of the spectrum of identification and partisan shifts and feelings of group loyalty and betrayal, we can gain a sense of how subgrouprelated activity may introduce systematic biases in crowdsourced validation.

To understand the impact of affective polarization, we conducted an online, scenario-based experiment to explore crowdsourced validation behavior. We found that affectively polarized cues influence patterns of crowdsourced validation across subgroups in identifiable ways. Specifically, we show that affective polarization, loyalty, and betrayal are mechanisms that produce partisan shifts found in validation patterns of event-centric data. By showing sociocognitive influences are a source of subgroup bias in crowdsourced validation of ground truth, we contribute a new perspective to crowdsourcing research and practice. Further, we offer an approach for identifying the influence of subgroups and adjusting for potential bias in results of crowdsourced validation using double debiased machine learning.

## Theoretical Background

## Crowdsource Data Validation Distortion

The crowdsource data validation literature in information systems (IS) research focuses on mechanisms to correct sources of ground truth distortion due to crowd characteristics, task attributes, or cognitive influences (Lukyanenko et al., 2014). Characteristics of the crowd influence the accuracy and quality of their data validation. For example, expertise and experience of the crowd improve the accuracy of ratings (Wang et al., 2017; Feller et al., 2012; Abbasi et al., 2019), and their absence can compromise data quality (Chen et al., 2019; Lukyanenko et al., 2017, 2019). Further, large, heterogeneous crowds generally have better outcomes than small, homogenous crowds due to the informational impact of diverse perspectives on crowd consensus (Yin et al., 2021).

In addition to the characteristics of the crowd, attributes of the task also influence how raters validate data. For example, the platform’s interface, design, and governance influence validation accuracy (Lukyanenko et al., 2014; Blohm et al., 2016; Gol et al., 2019; Majchrzak & Malhotra, 2013). Incentives, effort, and how raters interact with a task can all influence accuracy (Robert, 2019; Mo et al., 2018). Further, crowds have been found to favor information that is more salient to a situation, referred to as “salience bias,” leading to inferior or less comprehensive outcomes in crowdsourcing (Lee et al., 2018). Clearly, crowds can be biased, deliberately or inadvertently.

## Sociocognitive Influences, Subgroups, and Crowdsourced Data Validation:

Sociocognitive theory informs us that individual cognition is shaped, in part, by the cultural norms and expectations of groupings (Bandura, 1986). Social groupings provide the categories, schema, scripts, and affective positions that shape individual cognition and the resulting behavior (Fiske & Taylor, 1991; Kunda, 1999; Stein, 1997). Sociocognitive influences result from shared experiences and observations of behaviors that shape patterns of thoughts and feelings of people within a group (Fiske & Taylor, 1991; Kunda, 1999; Stein, 1997), which contribute to individual cognition and behavior (Bandura, 1986; Nisbett et al., 2001; Turner, 1981/2010). For example, sociocognitive influences tied to the family transmit important determinants of behavior such as national, religious, and cultural values; diverse social groups such as peer groups, organizations, and educational or political institutions influence the cognition of the individuals in systematic ways (Bandura, 1969). The range of group influences on cognition is dramatic. Social groups, such as national cultures, have been shown to influence how people think (more analytical in the West, more dialectical in the East, see Nisbett et al., 2001). Social groups shape how people think broadly about roles, such as gender and professional practice, but also how people should behave in particular situations, such as at restaurants, sports events, and job interviews (Fiske & Taylor, 1991). Within organizations, groups such as departments or professional associations can shape the way people “know”—how they recognize, address, solve problems, and innovate (Boland & Tenkasi, 1995). Indeed, the impact of groups on social cognition is so pronounced that some consider group cognition to be a form of cognition in its own right (Larson & Christensen, 1993). Thus, one would expect group identifications to matter for how crowds perceive, make sense of, and validate data. In the contemporary landscape, perhaps no social grouping is more salient than political identity, which has led to polarization worldwide (Gidron et al., 2019). We therefore draw on the concept of “affective polarization” to explore how subgrouprelated sociocognitive influences impact data validation.

## Subgroup Data Validation and Affective Polarization

Individuals divide the world into in-groups (i.e., our group) and out-groups (i.e., the other group) and have strong positive feelings about the in-group and negative feelings about the out-group. Individuals constantly evaluate the meaning of their group affiliation and its consistency with their past, present, and future selves (Moreland & McMinn, 1999) and refer to these evaluations when making decisions (Levine et al., 2018; Levine & Moreland, 1994; Moreland et al., 2001). Partisan group identification tends to exert a powerful influence on individual cognition and emotion (Carter & Grover, 2015; Iyengar et al., 2019), as well as shaping decision-making and behavioral responses to social situations (Roth et al., 2017). One such sociocognitive influence that can influence subgroup data validation is affective polarization.

Affective polarization can inform research into how sociocognitive influences could systematically distort crowdsourced validation through subgroups. Affective polarization results from emotional aspects of identification with a social group (e.g., political party). Sociotechnical environments, such as online echo chambers, further enhance feelings toward an in-group, which reinforces or exacerbates affective polarization, leading to more extreme ideologies. Raters who consume social media content in echo chambers are exposed to more limited, less diverse content (Kitchens et al., 2020), which promotes biases that reinforce existing views (Barberá et al., 2015; Greenstein & Zhu, 2018) and may impact their validation of event-centric data during politicized events. As ideologies become more partisan, extremists emerge that can change how individuals understand what it means to be part of an in-group and what they consider appropriate behavior (Luttig et al., 2017). In such circumstances, individuals’ extremism can drive partisan shifts in their behavior (Kitchens et al., 2020).

In affectively polarized environments, such as politicized events, extremism, and partisan shifts can relate to feelings of loyalty or betrayal. Loyalty refers to “adherence to a social unit to which one belongs, as well as its goals, symbols, and beliefs” (Carney, 1994) p. 179). Loyalty typically results from positive experiences, which result in feelings of commitment (Levine et al., 2018; Moreland et al., 2001). Research has shown that loyalty influences decision-making (Moreland & McMinn, 1999; Gibson & Caldeira, 2009). In contrast to loyalty, betrayal involves a violation of mutual expectations of behavior by trusted groups (Elangovan & Shapiro, 1998). Betrayal typically results in negative affect, biased decisions, and malicious behavior in the group toward the betrayers (Elangovan & Shapiro, 1998; Koehler & Gershoff, 2003).

<table><tr><td colspan="4">Affective polarization treatment</td></tr><tr><td colspan="4">During this portion of the study, it is important to visualize yourself as witnessing the events in this video as if you were there in person. Please imagine that you are watching this scene unfold in person.In-group &amp; out-group treatment: You are outside observing a protest and a member of a &lt;conservative Proud Boys, progressive ANTIFA&gt; group engages in a violent act that escalates into group violence.Control group treatment: You are outside observing a protest and an individual engages in a violent act that escalates into group violence.</td></tr><tr><td colspan="4">Image validation series</td></tr><tr><td>True information</td><td>True information (different angle)</td><td>False information (deepfake)</td><td>False information (from different event)</td></tr><tr><td><img src="/api/attachments/648BV57T/fulltext/images/b344a84a2d3178d8e8dea54743cf8c3369970f21fb95950a1a7745a44a1687df.jpg"/></td><td><img src="/api/attachments/648BV57T/fulltext/images/6b8e85ec671349c1b36c35552c7e137f5b00ca61f249c70b74b42cffabf98700.jpg"/></td><td><img src="/api/attachments/648BV57T/fulltext/images/26618816ee53ec107320e025463df325d46ff7e4ef5561fe484920e450577438.jpg"/></td><td><img src="/api/attachments/648BV57T/fulltext/images/12966255dddfd80bd43e6c15794decad2eced6e7c07015bba3744853e7f5c15e.jpg"/></td></tr><tr><td>Image extracted directly from the video of the event shown to participants</td><td>Image extracted from a different video of the same event providing a different angle</td><td>Image generated with deepfake artificial intelligence</td><td>Image from an entirely different event</td></tr><tr><td colspan="4">Figure 1. Experimental Treatments</td></tr></table>

By examining raters in an affectively polarized context, we can identify how different types of affectively polarized subgroups, defined by extremism, loyalty, and betrayal, distort crowdsourced validation of politicized events. Politicized events, such as protests, often represent power struggles between groups—clashes between collective identities and shared interests (Simon & Klandermans, 2001). If validation behaviors are biased systematically and predictably across extremist subgroups, then understanding these patterns will provide opportunities for future IS research to account for such distortions in polarized contexts.

## Research Method

We study the impact of subgroup influences using an immersive, exploratory, online experiment using the experimental vignette method (EVM) with a violent protest as the context (Bapna et al., 2017; Franklin, 2005). EVM is appropriate for understanding the effects of manipulated variables on real-time processes and decisions in difficult-tocapture real-world situations such as violent protests. This method is appropriate for studying contexts involving violence because manipulating participants during an actual crisis could be unethical and harmful (Aguinis & Bradley, 2014; Shepherd et al., 2013). Hence, we constructed situations to represent a combination of crisis characteristics (Aguinis & Bradley, 2014; Atzmüller & Steiner, 2010). We asked raters to evaluate footage from political protests in Portland, Oregon, in 2020. Social crises, such as violent protests, provide a uniquely polarizing context for research. Unlike natural disasters, which can bring a community together, social crises are often rife with discord between polarized groups (Quarantelli, 1993). Extreme views can escalate situations and lead to violence (Mooijman et al., 2018; Nassauer, 2018), making it essential to validate data in ways that inform appropriate real-time responses.

Following an inductive, computationally intensive approach (Berente et al., 2019), we analyzed the experimental data with a technique that uses, in part, double debiased machine learning (DML) (see Chernozhukov et al., 2018) to analyze participants ratings and identify subgroups. We used “affective polarization”—that is, political identification with progressives or conservatives—to operationalize subgroup influences using affective cues from groups from the opposition associated with these protests. Further, the constructs of loyalty and betrayal to and by a specific group were used to measure extremism with polarized groups associated with the political left (i.e., progressive) and right (i.e., conservative).

## Experimental Procedure

Our experiment used a 3×3×4 stratified randomized repeated measures design. We used a stratified sampling technique based on political affiliation (progressive, independent, and conservative) and the identification of extreme group affiliation (Proud Boys and ANTIFA). To ensure realism (Aguinis & Bradley, 2014; Karahanna et al., 2018), participants in our EVM were asked to validate a series of images through an immersive experience (Figure 1). Participants viewed all images in random order.

![](/api/attachments/648BV57T/fulltext/images/499c2c78e1dedaefbd872bb5320fed63bcbcdc9f74cc3abf01af0a0643e5dad4.jpg)  
Figure 2. Experimental 3×3×4 Data Representation

Each participant viewed the same video of protestors physically assaulting an individual, which escalated into mob violence. They were asked to imagine that they were present at the protest. Participants were asked to validate (yes/no) the truthfulness of two true images (i.e., from the video or a different angle of the actual event) and two false images (i.e., a deepfake and an image not from the event). We generated deepfake images using machine learning techniques (i.e., auto-encoders and generative adversarial networks: (Goodfellow et al., 2014; Kingma & Welling, 2013), face swapping, and attribute manipulation (Tolosana et al., 2020). We manipulated the affiliated group that committed the act of violence as ANTIFA or the Proud Boys (Klein, 2019; Stern, 2019). The Proud Boys is associated with the political right (Southern Poverty Law Center, 2020), and ANTIFA with the political left (Anti-Defamation League, 2017). Violence at protests has been attributed to both groups (DeCook, 2018; Klein, 2019; Kutner, 2020; LaFree, 2018; Stern, 2019).

We used a stratified sampling technique to distribute the 423 participants by political affiliation (i.e., progressive, independent, and conservative) into treatment groups—i.e., Proud Boys violence (N = 125, cons = 64, prog = 53, ind = 39); ANTIFA violence (N = 156, cons = 51, prog = 40, ind = 34); Control (N = 142, cons = 54, prog = 43, ind = 45). After validation, participants completed a short survey that captured loyalty, betrayal, and political identification (1 = progressive, 2 = somewhat progressive, 3 = lean progressive, 4 = independent, 5 = lean conservative, 6 = somewhat conservative, 7 = conservative) (Mooijman et al., 2018). After completing the survey, participants were debriefed.

## Participants, Manipulation Checks, and Data Screening

We recruited 470 participants from Amazon Mechanical Turk and excluded those who acknowledged having already seen the video. We used two one-item manipulation checks (Willison et al., 2018): (1) “<the Proud Boys, ANTIFA, Unknown> committed the act of violence” and (2) “I think the group behaving violently was <the Proud Boys, ANTIFA, Unknown>.” We also included several attention checks and different scales to detect careless responses (Lowry et al., 2016). For example, we asked, “Are you a robot?” and “Please answer strongly agree to this question.” We removed 47 unusable responses: 18 participants did not complete the survey, 18 failed the attention checks, and 11 failed the manipulation checks. For the final sample (N = 423), 40.5 was the average age, 37.4% of participants were women, and the sample included 136 progressives, 118 independents, and 169 conservatives.

## Data Analysis and Results

We iteratively explored relationships across the conditions and treatments of our stratified sample (Figure 2). To understand heterogeneity in the treatment effect, we used “double debiased machine learning” (DML) methods for causal inference to tease out the relative impact of subgroups. We combined this with logistic regression to understand whether extremists validate images based on group loyalty and betrayal and conducted a series of robustness checks.

## Data Validation in the Context of Affective Polarization

We began with a series of direct logistic regressions on the type of information validated (i.e., true, true different angle, false deepfake, false different event) as an outcome and two predictors: treatment (i.e., Proud Boys, ANTIFA, Control) and political identification. A test of the full model for each type of information with all predictors against a constant-only model was not statistically significant in most cases (overall results: true information $\chi 2 \left( 5 , N = 4 2 3 \right) = 7 . 3 0 , p < 0 . 1 9 9 ;$ true different angle $\chi 2 \ ( 5 , \ : N = 4 2 3 ) = 0 . 9 0 , \ : p < 0 . 9 7 0 ;$ false information deepfake $\chi 2 \left( 5 , N = 4 2 3 \right) = 3 . 1 6 , p < 0 . 6 8$ ; false information different event $\chi 2 \left( 5 , N = 4 2 3 \right) = 8 . 8 7 , p < 0 . 1 1 )$ indicating that the predictors, as a set, did not reliably distinguish between the rater validation behaviors of our event-centric data. However, the logistic regression results, while not always statistically significant, did seem to imply certain patterns $( \mathrm { e . g . }$ , the direction of coefficients), and we suspected that the lack of statistical significance resulted from our sample size. We also needed to account for other observable characteristics (e.g., age, gender, education level) in our comparison, and the relationship between these observations and their validation could have been nonlinear. Thus, traditional regression-based techniques may not be able to adequately deal with the variation of validation decisions across political identification subgroups. Therefore, we used DML methods (Athey et al., 2019; Chernozhukov et al., 2018; Nie & Wager, 2021).

In randomized experiments, DML methods estimate conditional average treatment effects by varying a given control variable. DML-based models have several benefits over traditional regression-based techniques. First, DML methods help when the effect of control variables on the treatment and the outcome cannot be satisfactorily modeled by parametric functions (Chernozhukov et al., 2018). Second, the cross-fitting technique (Chernozhukov et al., 2018) employed in these methods can improve the estimation of the effects with a smaller sample (the finite population convergence rates are faster). Finally, they help identify heterogeneous treatment effects on observed characteristics. These heterogeneous treatment effects help discover subgroups in the data at a more granular level than the stratified sampling we employed in the data collection. This discovery of subgroups is important because crowds may have systematic, unknown biases attributable to subgroup memberships, and DML helps identify fracture lines that affect ratings. DML methods have been applied to elicit heterogeneity in randomized experiments (Simester et al., 2020).

DML methods first build two predictive models using classic machine learning models to (1) predict the outcome from a set of control variables and (2) predict the treatment from the control variables. The predictive models built in the first stage are then used in the second stage of estimation to build a model of the heterogeneous treatment effect. Two types of control variables can be used in the DML methods. The first set of variables (??) are those where we further explore the heterogeneity of the treatment effect (e.g., political identification), and the second set of variables (??) are covariates (e.g., age, gender, education level, etc.). Formally, the DML models assume the following structural equations on data generation:

$$
\begin{array}{l} {Y ^ {k} = \theta^ {k} (X) \cdot T + g (X, W) + \epsilon_ {1}} \\ {T = f (X, W) + \epsilon_ {2},} \end{array}
$$

where $T$ is the treatment (Proud Boys or $\operatorname { A N T I F A } ) , Y ^ { k }$ is the outcome of validation of an image $\iota ( k = 1 , 2 , 3 , 4$ for each of the true information, true information different angle, deepfake, and false information images), and $\theta ^ { k } ( X )$ is the conditional average treatment effect (CATE). There are further assumptions that $E [ \boldsymbol { \epsilon } _ { 1 } \cdot \boldsymbol { \epsilon } _ { 2 } | \boldsymbol { X } , \boldsymbol { W } ] = 0$ to make a valid inference. There are no further parametric assumptions on $_ g$ and $f ,$ and they are estimated using machine learning methods, which makes them attractive for capturing nonlinear relationships. Therefore, DML models build two predictive machine learning models in the first stage (1) predicting the outcome ?? from the variables ??, ?? and (2) predicting the treatment ?? from the variables ??, ??. The residuals from these two predictive models in the first stage feed into the second stage to estimate CATE ${ \widehat { \theta } } ^ { k } ( X )$ . We used linear DML models, where the second stage is a linear model that performs well when the variables used for heterogeneity identification are in a low dimensional space (Chernozhukov et al., 2018). See the Appendix for details of the DML approach. Figure 3 describes the heterogeneity of the treatment effect based on political identification and shows the effect of political identification (x-axis) on the treatment effect (y-axis) for the four types of images for the Proud Boys and ANTIFA treatments compared to the control group and each other. The band provides the 95% confidence interval of the estimated treatment effect. If the treatment effect is positive, the group validates more than the control group based on political identification.

When presented with true information, our DML analysis revealed that rater political identification influences validation decisions in the presence of affectively polarized cues. When we attributed the violence to the Proud Boys, compared to the control condition, raters who identified as stronger progressives were more likely to correctly validate true information than raters who identified as stronger conservatives. In our true information condition attributing the violence to ANTIFA, compared to the control condition, both stronger progressives and conservatives validated less than the control group. When comparing ANTIFA and Proud Boy

conditions, results show that both parties validate true images in favor of their in-group. One striking finding is that conservatives validate less, regardless of whether the attributed group aligns with their polarization, particularly for false data. Also, affective cues have little to no impact on progressives’ validation of false data, but affective cues reduce the likelihood that conservatives validate data. To understand whether this involves mechanisms of loyalty and betrayal, we next examine extremism, where such forces should be most evident.

<table><tr><td rowspan="2">True information</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td></tr><tr><td>TRUE Treatment Effect</td><td>TRUE Treatment Effect</td><td>TRUE Treatment Effect</td></tr><tr><td rowspan="2">True information (different angle)</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td></tr><tr><td>DIFANG Treatment Effect</td><td>DIFANG Treatment Effect</td><td>DIFANG Treatment Effect</td></tr><tr><td rowspan="2">False information (deepfake)</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td></tr><tr><td>DPK Treatment Effect</td><td>DPK Treatment Effect</td><td>DPK Treatment Effect</td></tr><tr><td rowspan="2">False information (not from crisis)</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td></tr><tr><td>FLSE Treatment Effect</td><td>FLSE Treatment Effect</td><td>FLSE Treatment Effect</td></tr><tr><td rowspan="4">N of subgroups</td><td></td><td>Proud Boys</td><td>ANTIFA</td></tr><tr><td>Progressives</td><td>53</td><td>40</td></tr><tr><td>Independents</td><td>39</td><td>34</td></tr><tr><td>Conservatives</td><td>64</td><td>51</td></tr><tr><td colspan="4">Note: PB = Proud Boys, PIDE = political identification (1 = progressive, 2 = somewhat progressive, 3 lean progressive, 4 = independent, 5 = lean conservative, 6 = somewhat conservative, 7 = conservative)</td></tr></table>

## Extremism and Group Loyalty and Betrayal

Following existing studies (Dinas, 2014; Gibson & Caldeira, 2009; Van Vugt & Hart, 2004), we include loyalty and betrayal measures based on the referent treatment group (i.e., ANTIFA, N = 125; Proud Boys, N = 154). This consisted of a subsample of the experiment of only treatment group participants. For example, if a rater was in the ANTIFA (Proud Boys) treatment group, they were only asked about loyalty and betrayal vis-à-vis ANTIFA (Proud Boys). This preserved in-group and out-group dynamics and reduced response bias concerns (Furnham, 1986).

We evaluated loyalty and betrayal in relation to either the Proud Boys or ANTIFA (full measures are presented in Appendix Table A1). We also examined the correlations between loyalty, betrayal, and political identification to validate whether group and political identification were distinct concepts. Our analysis showed that ANTIFA loyalty $( r \left( 1 5 4 \right) = - 0 . 1 4 , p = 0 . 0 8 )$ and betrayal $( r \left( 1 2 3 \right) = - 0 . 2 7 , p \leq$ 0.001) had weak correlations with political identification. Additionally, Proud Boys’ loyalty (r (123) = 0.20, p = 0.03) and betrayal (r (123) = -0.10, p = 0.29) also had weak correlations with political identification. Thus, our results indicate that political identification is different from loyalty. Further, we conducted logistic regressions and found no significant differences between conservatives and progressives on the impact of loyalty and betrayal on validation behaviors. Therefore, we aggregated extremists from both sides. (Note: research has found that extremists on either side have more in common with each other than with moderates—see Luttig et al., 2017.)

Treatments with a referent group (ANTIFA and Proud Boys, N = 279) were used to determine how group loyalty and betrayal influence the validation of ground truth by extreme raters, controlling for gender and age. Confirmatory factor analysis fit statistics were acceptable (Kline, 2015; see Table A1). We ran a binary logistic regression (Table 1). We converted results to odds, probabilities, and marginal effects (Table 2). Results show significant relationships between group loyalty and the validation of both true and false information. When raters were asked to identify true information, we found significant contrasting relationships between loyalty $( B = - 0 . 3 4 , p = 0 . 0 2 )$ and betrayal $( B = 0 . 3 3 , p = 0 . 0 4 )$ on validation decisions. This indicates that when individuals are loyal to a group, they are more likely to not validate true information. When individuals feel betrayed, they are more likely to validate true information. The marginal effect of loyalty (-0.02) indicates an instantaneous change of 2.0% in not validating true information for every unit increase in loyalty. The marginal effect of betrayal (0.02) indicates an instantaneous change of 2.0% in validating true information for every unit increase in betrayal. When raters were asked to identify false information from a deepfake, group loyalty had a significant positive relationship $( B = 0 . 2 1 , p =$ 0.03) with validating false information. The marginal effect of loyalty (0.04) indicates that for every unit increase in loyalty, there was an instantaneous change of 4.0% in validating deepfakes. Our control variable of age was also significant for deepfakes $( B = - 0 . 0 3 , p = 0 . 0 1 )$ . When individuals were asked to identify false information from events, loyalty had a significant positive relationship $( B = 0 . 7 0 , p \leq 0 . 0 1 )$ with the validation of false information. The marginal effect of loyalty (0.05) indicates an instantaneous change of 5.0% in validating false information for every unit increase in loyalty. A post hoc result indicated no difference in loyalty or betrayal when controlling for each subgroup.

As a robustness check, we ran a repeated-measures, hierarchal linear model, which revealed how much variance resides within the different types of information and between participants. This showed an interclass correlation of 1.0% in the interceptonly model, indicating that most variance resides at the Level 1 variable (type of information), not the Level 2 variables (within the individual). We conducted a post hoc chi-square test on selfidentified political affiliation (i.e., conservative, progressive, independent) and the treatment to confirm that extreme identification provided a better explanation than political identification. Our results show chi-square tests were insignificant (p > 0.05) for self-identified political affiliation.

## Discussion

In this research note, we found that subgroup-based sociocognitive influences systematically distort the wisdom of the crowd for event based data. This suggests that subgroup-based sociocognitive influences such as affective polarization can distort crowdsourced validated ground truth (Zade et al., 2018).

Interestingly, we found that raters behave asymmetrically across the affective polarization spectrum—subgroups have different in-group and out-group validation patterns. This is an important observation. Different subgroups likely have different sociocognitive patterns and may behave differently. However, we also found that extremists in different groups validate in similar ways in their responses to feelings of loyalty and betrayal, indicating that subgroup differences can be quite nuanced and complex. To establish accurate ground truth based on the wisdom of the crowd, we need to understand and adjust for subgroup-based crowd biases. This requires a granular understanding of distinctions in validation patterns across differentiated subgroups. As a result, our findings suggest future work investigating subgroup tendencies to inform how we identify and adjust for subgroups in the crowd.

<table><tr><td colspan="8">Table 1. Results of Binary Logistic Regression</td></tr><tr><td colspan="4"></td><td colspan="2">95% CI for odds ratio</td><td></td><td rowspan="2">p-value</td></tr><tr><td>Predictor</td><td>B</td><td>SE B</td><td>Odds ratio</td><td>Lower</td><td>Upper</td><td>df</td></tr><tr><td colspan="8">True information</td></tr><tr><td>Constant</td><td>3.35</td><td>1.23</td><td>28.50</td><td>0.94</td><td>5.76</td><td>1</td><td></td></tr><tr><td>Loyalty</td><td>-0.34</td><td>0.15</td><td>0.71</td><td>-0.63</td><td>-0.05</td><td>1</td><td>0.02</td></tr><tr><td>Betrayal</td><td>0.33</td><td>0.16</td><td>1.39</td><td>0.02</td><td>0.65</td><td>1</td><td>0.04</td></tr><tr><td>Gender</td><td>0.47</td><td>0.55</td><td>1.60</td><td>-0.61</td><td>1.54</td><td>1</td><td>0.39</td></tr><tr><td>Age</td><td>-0.03</td><td>0.02</td><td>0.97</td><td>-0.07</td><td>0.01</td><td>1</td><td>0.12</td></tr><tr><td colspan="8">Note:  $X^2$  288.79 df = 273, N = 279, log likelihood = -55.81, -2LL = 10.80,  $R^2_L$ = 0.09</td></tr><tr><td colspan="8">True information (different angle)</td></tr><tr><td>Constant</td><td>1.67</td><td>0.74</td><td>5.31</td><td>0.21</td><td>3.13</td><td>1</td><td></td></tr><tr><td>Loyalty</td><td>-0.05</td><td>0.10</td><td>0.95</td><td>-0.24</td><td>0.15</td><td>1</td><td>0.63</td></tr><tr><td>Betrayal</td><td>0.16</td><td>0.09</td><td>1.17</td><td>-0.02</td><td>0.34</td><td>1</td><td>0.07</td></tr><tr><td>Gender</td><td>0.06</td><td>0.32</td><td>1.06</td><td>-0.57</td><td>0.69</td><td>1</td><td>0.86</td></tr><tr><td>Age</td><td>-0.02</td><td>0.01</td><td>0.98</td><td>-0.04</td><td>0.01</td><td>1</td><td>0.26</td></tr><tr><td colspan="8">Note:  $X^2$  277.95, df = 273, N = 279, log likelihood = -124.18, -2LL = 4.28,  $R^2_L$ = 0.02</td></tr><tr><td colspan="8">Deepfake</td></tr><tr><td>Constant</td><td>1.60</td><td>0.63</td><td>4.95</td><td>0.36</td><td>2.84</td><td>1</td><td></td></tr><tr><td>Loyalty</td><td>0.21</td><td>0.09</td><td>1.23</td><td>0.03</td><td>0.39</td><td>1</td><td>0.03</td></tr><tr><td>Betrayal</td><td>0.11</td><td>0.07</td><td>1.12</td><td>-0.04</td><td>0.25</td><td>1</td><td>0.16</td></tr><tr><td>Gender</td><td>-0.23</td><td>0.27</td><td>0.79</td><td>-0.75</td><td>0.30</td><td>1</td><td>0.40</td></tr><tr><td>Age</td><td>-0.03</td><td>0.01</td><td>0.97</td><td>-0.05</td><td>-0.01</td><td>1</td><td>0.01</td></tr><tr><td colspan="8">Note:  $X^2$  275.58, df = 273, N = 279, log likelihood = -158.75, -2LL = 16.17,  $R^2_L$ = 0.05</td></tr><tr><td colspan="8">False information (from different event)</td></tr><tr><td>Constant</td><td>-4.96</td><td>1.25</td><td>0.01</td><td>-7.41</td><td>-2.50</td><td>1</td><td></td></tr><tr><td>Loyalty</td><td>0.70</td><td>0.14</td><td>2.01</td><td>0.43</td><td>0.97</td><td>1</td><td>0.00</td></tr><tr><td>Betrayal</td><td>0.15</td><td>0.14</td><td>1.16</td><td>-0.13</td><td>0.43</td><td>1</td><td>0.30</td></tr><tr><td>Gender</td><td>0.05</td><td>0.44</td><td>1.05</td><td>-0.81</td><td>0.91</td><td>1</td><td>0.91</td></tr><tr><td>Age</td><td>-0.01</td><td>0.02</td><td>0.99</td><td>-0.05</td><td>0.03</td><td>1</td><td>0.70</td></tr></table>

Note: X<sup>2</sup> 329.71 df = 273, N = 279 (2 of 281 raters in the Proud Boys Treatment did not complete a response for loyalty and betrayal), log likelihood = -64.62, -2LL = 34.20, R<sup>2</sup> = 0.21

<table><tr><td colspan="5">Table 2. Logit, Odds, Probability, Marginal Effects for Significant Predictor</td></tr><tr><td>Predictor</td><td>Logit</td><td>Odds</td><td>Probability</td><td>Marginal effects</td></tr><tr><td colspan="5">True information</td></tr><tr><td>Loyalty</td><td>-0.34</td><td>0.71</td><td>0.42</td><td>-0.02</td></tr><tr><td>Betrayal</td><td>0.33</td><td>1.39</td><td>0.58</td><td>0.02</td></tr><tr><td colspan="5">Deepfake</td></tr><tr><td>Loyalty</td><td>0.21</td><td>1.23</td><td>0.55</td><td>0.04</td></tr><tr><td colspan="5">False information (from different event)</td></tr><tr><td>Loyalty</td><td>0.70</td><td>2.01</td><td>0.67</td><td>0.05</td></tr></table>

## Theoretical Contributions & Future Directions

This research note has implications for crowdsourced validation research. First, we show that sociocognitive influences associated with subgroup-based variability in crowd validation patterns systematically undermine the principle of consensus. While IS research accounts for distortion among individuals in the crowd and the crowd as a whole (Lukyanenko et al., 2014, 2019), this research note draws attention to opposing subgroups in the crowd. If subgroups are unaccounted for, consensusbased crowdsourced validation techniques may produce false positives or negatives with real-world consequences. The granular patterns that we identify show differences and similarities in subgroup validation patterns, underscoring the need for further research to consider how the sociotechnical context (Sarker et al., 2019) shapes subgroups, crowd validation patterns, perceptions of information, and the distortion of ground truth.

Further, this work shows that the type of information, true or false, introduces variability in how raters validate data. The results show that sociocognitive influences manifest differently in subgroups depending on the type of information presented. For example, legacy data, such as true data presented to raters, compared to emergent forms of disinformation, such as deepfakes presented to raters, elicit different validation patterns. IS research shows that individuals can unknowingly be exposed to political ideologies and disinformation on digital platforms (Greenstein & Zhu, 2018; Kitchens et al., 2020) and seek out or trust disinformation with similar opinions (Gu et al., 2014). Further, political science shows that partisan news outlets intentionally provide content about political identification that can cause hostility (Arceneaux et al., 2012). It is critical to unpack further how affective polarization, other sociocognitive influences, and technical variability in the type of information presented to raters distort validation patterns. Understanding how subgroups interact with the type of information further highlights the limitations of crowdsourced validation in an age of deepfakes and generative artificial intelligence and its exacerbation by modern digital platforms’ move to more algorithmic-based recommendation tools (Del Vicario et al., 2016; Kitchens et al., 2020). Regarding emergent information, IS research is well positioned to shed a more detailed light on subgroup tendencies and design interventions in order to adjust distorted ground truth estimates in different contexts (e.g., fake news, chatbots, misinformation).

Further, this research highlights the importance for designers and decision makers to understand subgroups in crowds, and these insights may inform design work, not only in emergent situations (Majchrzak et al., 2007; Tim et al., 2017) but also, potentially, in less time-sensitive contexts such as factchecking (Pinto et al., 2019), media bias (Färber et al., 2020), citizen science (Lukyanenko et al., 2019), and false news (Sethi, 2017; Tschiatschek et al., 2017). Decision makers must also consider the fact that crowds are comprised of raters with different motivations, leading to different validation tendencies (Lasecki et al., 2014), which introduces distortion (Dittus et al., 2017). Future IS research can look to identify subgroups that systematically distort ground truth based on identifiable biased validation patterns to inform real-time solutions that attempt to predict or manage adverse events (Lasecki et al., 2014).

The choice of affective polarization, loyalty, and betrayal as the constructs of interest to operationalize subgroup sociocognitive influences is a compelling domain for studying the wisdom of the crowd in contexts with opposition groups. While we examine only affective polarization in the U.S., these findings can offer insights globally. Affective polarization manifests in many countries, such as France, Finland, Australia, the U.K., etc. (Gidron et al., 2019). When affective polarization is extreme, violence can escalate quickly—not just in the U.S. but also in Brazil, the European Union, Canada, and beyond (Bisserbe & Dalton, 2023; Cabral, 2023; Fassihi, 2022). Distorted data validation due to affective polarization can lead to partial truths or outright falsehoods and exacerbate inappropriate subgroup data validation and subsequent responses (Huang & Billen, 2020; Starbird et al., 2014). Researchers should consider how sociocognitive influences and those related to loyalty and betrayal, such as morals, values, and allegiances, related to validation decisions can undermine ground truth. Future work should also consider how the distortion of information by extremists can shape crowd opinions, particularly in potentially violent contexts (Mooijman et al., 2018; Nassauer, 2018).

Finally, this study illustrates how to integrate traditional research design with a novel method to realize an advanced understanding of subgroup-related patterns. This is one of the first studies to combine an exploratory behavioral experiment with DML. Traditionally, DML is applied to massive datasets with much larger numbers of responses. This study shows that a robust research design can make computationally intensive methods useful for understanding complex social phenomena, even with relatively few responses. Using machine learning techniques can help researchers overcome assumptions about homogeneity and capitalize on the heterogeneity of subgroups to increase the veracity and nuance of generalizations from crowdsourcing and data gleaned from other sources, such as e-commerce sites or social media.

## Implications for Practice

Our findings suggest that organizations using crowdsourcing to increase the accuracy of ground truth should proceed with caution if subgroups remain hidden. Currently, most eventcentric ground-truth data is estimated manually by trained moderators in non-real time (Wilson & Starbird, 2021). When processing massive amounts of data generated by a crowd (Prabhu et al., 2021), we urge decision makers to focus on uncovering potential patterns due to sociocognitive influences. First, detecting subgroups and associated validation patterns can help to identify sources of distortion in crowdsourced validation. Second, systematic adjustment needs to be performed, which could involve learning weights for the identified subgroups through batch active learning algorithms (Zhuang & Young, 2015), such that there is less bias in the reweighted crowdsourced validation. Making these adjustments calls attention for organizations to ensure that their teams have the expertise to understand the context (e.g., presence of sociocognitive influences), the composition of the crowd (e.g., subgroups), and the ability to accurately present information to avoid the distortion of ground truth. This could mean assembling expert teams with intimate knowledge of subgroups, such as those on extremes, that might be able to point to contextual factors to control their validation tendencies and adjust for emergent disinformation. By purposefully identifying more and less extreme subgroups and emergent forms of disinformation, organizations may be able to correct distortion in near real time to offer more accurate estimates of ground truth.

Further, since machine learning algorithms can detect patterns in data, organizations that use crowdsourced data could explore machine learning techniques to detect subgroups and associated validation patterns in data. For example, techniques that detect the problem of concept drift (Lu et al., 2018) could be applied to detect such patterns, and debiasing techniques (Mehrabi et al., 2021) could be used to remove the effect of biases in machine learning models. Crowdsource validation system designers may wish to incorporate the ability to add contextual knowledge into alert and reporting systems. Although less-controlled information can often lead to further misinformation or the generation of too much information to process in real time, a contextual approach might be beneficial. While time is critical, and systems often present more simplified versions of data (e.g., suspect description, binary/defined user choices), IS research has shown that openended information can improve CrowdIQ (Lukyanenko et al., 2014; Lukyanenko et al., 2019) and that less binary choice leads to improved data veracity (Becker et al., 2022). Practitioners designing crowdsourced rating systems may need to consider the design trade-offs of more nuanced choices for raters, such as limited text-based content, confidence ratings (e.g., accuracy percentage sliders), or other design mechanisms to identify subgroups.

## Limitations

This study has limitations. Although immersive, this study uses EVM to portray a riot at a protest, which may have limited ecological validity. Additional work is needed to probe our questions about crowdsourced data validation in other crises and contexts. Also, our sample includes some raters that identify strongly with either the Proud Boys or ANTIFA. While it might be argued that they introduce bias to the study, we believe it is evidence that our stratified sampling approach worked and that we captured the full range of political views in the U.S. Finally, our work only looked at one possible instance of sociocognitive distortion in crowdvalidated data. In future work, it would be interesting to examine how intersectionality—that is, the interplay between political views, gender, religion, and other known drivers of affective polarization—distorts how raters evaluate eventcentric data in the context of other types of event-based data (e.g., COVID-19, Hurricane, Brexit, Ukraine, and Iranian social movements).

## Acknowledgments

The authors thank the reviewers, the associate editor, and the senior editor for their helpful comments. The second and third authors contributed equally.

## References

Anti-Defamation League. (2017). Who are ANTIFA? https://www.adl.org/resources/backgrounder/who-are-antifa

Aguinis, H., & Bradley, K. J. (2014). Best practice recommendations for designing and implementing experimental vignette methodology Studies. Organizational Research Methods, 17(4), 351-371. https://doi.org/10.1177/1094428114547952

Abbasi, A., Li, J., Adjeroh, D., Abate, M., & Zheng, W. (2019). Don’t mention it? Analyzing user-generated content signals for early adverse event warnings. Information Systems Research,30(3), 1007-1028. https://doi.org/10.1287/isre.2019.0847

Ahmad, F., Abbasi, A., Kitchens, B., Adjeroh, D. A., & Zeng, D. (2022). Deep learning for adverse event detection from web search. IEEE Transactions on Knowledge and Data Engineering, 34(6), 2681-2695. https://doi.org/10.1109/TKDE.2020.3017786

Arceneaux, K., Johnson, M., & Murphy, C. (2012). Polarized political communication, oppositional media hostility, and selective exposure. The Journal of Politics, 74(1), 174-186. https://doi.org/10.1017/S002238161100123X

Athey, S., Tibshirani, J., & Wager, S. (2019). Generalized random forests. The Annals of Statistics, 47(2), 1148-1178. https://doi.org/ 10.1214/18-AOS1709

Atzmüller, C., & Steiner, P. M. (2010). Experimental vignette studies in survey research. Methodology: European Journal of Research Methods for the Behavioral and Social Sciences, 6(3), 128-138. https://doi.org/10.1027/1614-2241/a000014

Avudaiappan, N., Herzog, A., Kadam., S., Du, Y., Thatcher, J., Safro, I. (2017). Detecting and summarizing emergent events in microblogs and social media streams by dynamic centralities. In Proceedings of the IEEE International Conference on Big Data (1627-1634). https://doi.org/10.1109/BigData.2017.8258097

Bandura, A. (1969). Social-learning theory of identificatory processes. In D. A. Goslin (Ed.), Handbook of socialization theory and research (pp. 213-262). Rand McNally & Company.

Bandura, A. (1986). The explanatory and predictive scope of selfefficacy theory. Journal of Social and Clinical Psychology, 4(3), 359-373. https://doi.org/10.1521/jscp.1986.4.3.359

Bapna, R., Gupta, A., Rice, S., & Sundararajan, A. (2017). Trust and the strength of ties in online social networks: An exploratory field experiment. MIS Quarterly, 41(1), 115-130. https://www.jstor. org/stable/26629639

Barberá, P., Jost, J. T., Nagler, J., Tucker, J. A., & Bonneau, R. (2015). Tweeting from left to right: Is online political communication more than an echo chamber? Psychological Science, 26(10), 1531-1542. https://doi.org/10.1177/0956797615594620

Becker, J., Brackbill, D., & Centola, D. (2017). Network dynamics of social influence in the wisdom of crowds. PNAS, 114(26), E5070- E5076. https://doi.org/10.1073/pnas.1615978114

Becker, J. A., Guilbeault, D., & Smith, E. B. (2022). The crowd classification problem: Social dynamics of binary-choice accuracy.

Management Science, 68(5), 3949-3965. https://doi.org/10.1287/ mnsc.2021.4127

Berente, N., Seidel, S., & Safadi, H. (2019). Research commentary— Data-driven Computationally Intensive Theory Development. Information Systems Research, 30(1), 50-64. https://doi.org/ 10.1287/isre.2018.0774

Bisserbe, N., & Dalton, M. (2023). French workers mount new strike against Macron’s pension overhaul. The Wall Street Journal. https://www.wsj.com/articles/france-workers-strike-macronretirement-age-11675157389

Blohm, I., Riedl, C., Füller, J., & Leimeister, J. M. (2016). Rate or trade? Identifying winning ideas in open idea sourcing. Information Systems Research, 27(1), 27-48. http://dx.doi.org/ 10.1287/isre.2015.0605

Boland, R. J., Jr., & Tenkasi, R. V. (1995). Perspective making and perspective taking in communities of knowing. Organization Science, 6(4), 350-372. https://doi.org/10.1287/orsc.6.4.350

Brynjolfsson, E., Geva, T., & Reichman, S. (2016). Crowd-Squared. MIS Quarterly, 40(4), 941-962. https://www.jstor.org/stable/ 26629683

Cabral, S. (2023). Sri Lanka’s anti-government protests have gone silent—for now. BBC. https://www.bbc.com/news/world-asia-64142694

Carney, R. M. (1994). The enemy within: A social history of treason. In T. R., Sarbin, R. M. Carney, & C. Eoyang (Eds.), Citizen espionage: Studies in trust and betrayal. Praeger.

Carter, M., & Grover, V. (2015). Me, my self, and I(T). MIS Quarterly 39(4), 931-958. https://www.jstor.org/stable/26628658

Chen, H., Hu, Y. J., & Huang, S. (2019). Monetary incentive and stock opinions on social media. Journal of Management Information Systems, 36(2), 391-417. https://doi.org/10.1080/07421222.2019. 1598686

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., & Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. Oxford University Press. https://doi.org/10.1111/ectj.12097

Coleman, D., Georgiadou, Y., & Labonte, J. (2009). Volunteered geographic information: The nature and motivation of produsers. International Journal of Spatial Data Infrastructures Research, 4(4), 332-358.

DeCook, J. R. (2018). Memes and symbolic violence: #proudboys and the use of memes for propaganda and the construction of collective identity. Learning, Media and Technology, 43(4), 485-504. https://doi.org/10.1080/17439884.2018.1544149

Del Vicario, M., Vivaldo, G., Bessi, A., Zollo, F., Scala, A., Caldarelli, G., & Quattrociocchi, W. (2016). Echo chambers: Emotional contagion and group polarization on Facebook. Scientific Reports, 6(1), 1-12. https://doi.org/10.1038/srep37825

Dinas, E. (2014). Does choice bring loyalty? Electoral participation and the development of party identification. American Journal of Political Science, 58(2), 449-465.

Dissanayake, I., Nerur, S., Singh, R., & Lee, Y. (2019). Medical crowdsourcing: Harnessing the “wisdom of the crowd” to solve medical mysteries. Journal of the Association for Information Systems, 20(11), 1589-1610. https://doi-org.utk.idm.oclc.org/ 10.1111/ajps.12044open\_in\_new

Dittus, M., Quattrone, G., & Capra, L. (2017). Mass participation during emergency response: Event-centric Crowdsourcing in Humanitarian mapping. In Proceedings of the 2017 ACM conference on computer supported cooperative work and social

computing (pp. 1290-1303). http://dx.doi.org/10.1145/2998181. 2998216

Elangovan, A. R., & Shapiro, D. L. (1998). Betrayal of trust in organizations. The Academy of Management Review, 23(3), 547- 566. https://doi.org/10.2307/259294

Färber, M., Burkard, V., Jatowt, A., & Lim, S. (2020, October). A multidimensional dataset based on crowdsourcing for analyzing and detecting news bias. In Proceedings of the 29th ACM international conference on information & knowledge management (pp. 3007-3014). https://doi.org/10.1145/3340531. 3412876

Fassihi, F. (2022). Iran cracks down as protests show no sign of easing. The New York Times. https://www.nytimes.com/2022/11/15/ world/middleeast/iran-protests-tehran-metro-shooting.html

Feller, J., Finnegan, P., Hayes, J., & O’Reilly, P. (2012). “Orchestrating” sustainable crowdsourcing: A characterisation of solver brokerages. The Journal of Strategic Information Systems, 21(3), 216-232. https://doi.org/10.1016/j.jsis.2012.03.002

Fingerhut, N., Sesia, M., & Romano, Y. (2022). Coordinated double machine learning. arXiv. https://doi.org/10.48550/2206.00885

Fiske, S. T., & Taylor, S. E. (1991). Social cognition. Mcgraw-Hill.

Franklin, L. R. (2005). Exploratory experiments. Philosophy of Science, 72(5), 888-899. https://doi.org/10.1086/508117

Furnham, A. (1986). Response bias, social desirability and dissimulation. Personality and Individual Differences, 7(3), 385- 400. https://doi.org/10.1016/0191-8869(86)90014-0

Gibson, J. L., & Caldeira, G. A. (2009). Confirmation politics and the legitimacy of the US Supreme Court: Institutional loyalty, positivity bias, and the Alito nomination. American Journal of Political Science, 53(1), 139-155. https://doi.org/10.1111/j.1540- 5907.2008.00362.x

Gidron, N., Adams, J., & Horne, W. (2019). Toward a comparative research agenda on affective polarization in mass publics. APSA Comparative Politics Newsletter, 29, 30-36.

Gol, E. S., Stein, M. K., & Avital, M. (2019). Crowdwork platform governance toward organizational value creation. The Journal of Strategic Information Systems, 28(2), 175-195. https://doi.org 10.1016/j.jsis.2019.01.001

Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., ... & Bengio, Y. (2014). Generative adversarial nets. In Proceedings of the 28th International Conference on Neural Information Processing Systems.

Greenstein, S., & Zhu, F. (2018). Do experts or crowd-based models produce more bias? Evidence from Encyclopedia Britannica and Wikipedia. MIS Quarterly, 42(3), 945-960. https://doi.org/ 10.25300/MISQ/2018/14084

Gu, B., Konana, P., Raghunathan, R., & Chen, H. M. (2014). Research note—The allure of homophily in social media: Evidence from investor responses on virtual communities. Information Systems Research, 25(3), 604-617. https://doi.org/10.1287/isre.2014.0531

Hill, J. L. (2011). Bayesian nonparametric modeling for causal inference. Journal of Computational and Graphical Statistics, 20(1), 217-240. https://doi.org/10.1198/jcgs.2010.08162

Huang, Y., & Billen, C. (2020). Information verification for humanitarians: A critical review. arXiv. https://doi.org/10.48550 2008.05174

Hutter, K., Füller, J., Hautz, J., Bilgram, V., & Matzler, K. (2015). Machiavellianism or morality: which behavior pays off in online innovation contests? Journal of Management Information Systems, 32(3), 197-228. https://doi.org/10.1080/07421222.2015.1099181

Imbens, G. W., & Rubin, D. B. (2015). Causal inference in statistics, social, and biomedical sciences. Cambridge University Press.

Iyengar, S., Lelkes, Y., Levendusky, M., Malhotra, N., & Westwood, S. J. (2019). The origins and consequences of affective polarization in the United States. Annual Review of Political Science, 22, 129- 146. https://doi.org/10.1146/annurev-polisci-051117-073034

James, K., & Cropanzano, R. (1994). Dispositional group loyalty and individual action for the benefit of an ingroup: Experimental and correlational evidence. Organizational Behavior and Human Decision Processes, 60(2), 179-205. https://doi.org/10.1006/obhd. 1994.1080

Jones, W. H., & Burdette, M. P. (1994). Betrayal in relationships. In A. L. Weber & J. H. Harvey (Eds.), Perspectives on close relationships (pp. 243-262). Allyn & Bacon.

Karahanna, E., Benbasat, I., Bapna, R., & Rai, A. (2018). Editor’s comments: Opportunities and challenges for different types of online experiments. MIS Quarterly, 42(4), iii-x. https://www.jstor. org/stable/26635069

Kingma, D. P., & Welling, M. (2013). Auto-encoding variational Bayes. arXiv. https://doi.org/10.48550/arXiv.1312.6114

Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption. MIS Quarterly, 44(4), 1619-1649. https://doi.org/10.25300/MISQ/ 2020/16371

Klein, A. (2019). From Twitter to Charlottesville: Analyzing the fighting words between the alt-right and Antifa. International Journal of Communication, 13, 297-318.

Kline, R. B. (2015). Principles and practice of structural equation modeling. Guilford Publications.

Koehler, J. J., & Gershoff, A. D. (2003). Betrayal aversion: When agents of protection become agents of harm. Organizational Behavior and Human Decision Processes, 90(2), 244-261. https://doi.org/10.1016/S0749-5978(02)00518-6

Kunda, Z. (1999). Social cognition: Making sense of people. MIT Press.

Künzel, S. R., Sekhon, J. S., Bickel, P. J., & Yu, B. (2019). Metalearners for estimating heterogeneous treatment effects using machine learning. Proceedings of the National Academy of Sciences, 116(10), 4156-4165. https://doi.org/10.1073/pnas. 1804597116

Kutner, S. (2020). Swiping right: The allure of hyper masculinity and cryptofascism for men who join the Proud Boys. International Centre for Counter-Terrorism.

LaFree, G. (2018). Is Antifa a terrorist group? Society, 55(3), 248-252.

Larson, J. R. Jr., & Christensen, C. (1993). Groups as problem‐solving units: Toward a new meaning of social cognition. British Journal of Social Psychology, 32(1), 5-30. https://doi.org/10.1111/j.2044- 8309.1993.tb00983.x

Lasecki, W. S., Teevan, J., & Kamar, E. (2014). Information extraction and manipulation threats in crowd-powered systems. In Proceedings of the 17th ACM conference on Computer supported cooperative work & social computing (pp. 248-256). http://dx.doi.org/10.1145/2531602.2531733

Lee, H. C. B., Ba, S., Li, X., & Stallaert, J. (2018). Salience bias in crowdsourcing contests. Information Systems Research, 29(2), 401-418. https://doi.org/10.1287/isre.2018.0775

Levine, E. E., Bitterly, T. B., Cohen, T. R., & Schweitzer, M. E. (2018). Who is trustworthy? Predicting trustworthy intentions and

behavior. Journal of Personality and Social Psychology, 115(3), 468-494. https://doi.org/10.1037/pspi0000136

Levine, J. M., & Moreland, R. L. (1994). Group socialization: Theory and research. European Review of Social Psychology, 5(1), 305- 336. https://doi.org/10.1080/14792779543000093

Lowry, P. B., D’Arcy, J., Hammer, B., & Moody, G. D. (2016). “Cargo cult” science in traditional organization and information systems survey research: A case for using nontraditional methods of data collection, including Mechanical Turk and online panels. The Journal of Strategic Information Systems, 25(3), 232-240. https://doi.org/10.1016/j.jsis.2016.06.002

Lu, J., Liu, A., Dong, F., Gu, F., Gama, J., & Zhang, G. (2018). Learning under concept drift: A review. IEEE Transactions on Knowledge and Data Engineering, 31(12), 2346-2363. https://doi.org/10.1109/TKDE.2018.2876857

Lukyanenko, R., Parsons, J., & Wiersma, Y. F. (2014). The IQ of the crowd: Understanding and improving information quality in structured user-generated content. Information Systems Research, 25(4), 669-689. https://doi.org/10.1287/isre.2014.0537

Lukyanenko, R., Parsons, J., Wiersma, Y., Wachinger, G., Huber, B., & Meldt, R. (2017). Representing crowd knowledge: Guidelines for conceptual modeling of user-generated content. Journal of the Association for Information Systems, 18(4), 297-339. https://doi.org/10.17705/1jais.00456

Lukyanenko, R., Parsons, J., Wiersma, Y. F., & Maddah, M. (2019). Expecting the unexpected: Effects of data collection design choices on the quality of crowdsourced user-generated content. MIS Quarterly, 43(2), 623-648. https://doi.org/10.25300/MISQ/2019/ 14439

Luttig, M. D., Federico, C. M., & Lavine, H. (2017). Supporters and opponents of Donald Trump respond differently to racial cues: An experimental analysis. Research & Politics, 4(4), https://doi.org/ 10.1177/2053168017737411

Majchrzak, A., Jarvenpaa, S. L., & Hollingshead, A. B. (2007). Coordinating expertise among emergent groups responding to disasters. Organization Science, 18(1), 147-161. https://doi.org/ 10.1287/orsc.1060.0228

Majchrzak, A., & Malhotra, A. (2013). Towards an information systems perspective and research agenda on crowdsourcing for innovation. The Journal of Strategic Information Systems, 22(4), 257-268. https://doi.org/10.1016/j.jsis.2013.07.004

Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). A survey on bias and fairness in machine learning. ACM Computing Surveys, 54(6), 1-35. https://doi.org/10.1145/3457607

Mo, J., Sarkar, S., & Menon, S. (2018). Know when to run. MIS Quarterly, 42(3), 919-944. https://doi.org/10.25300/MISQ/2018 14103

Mooijman, M., Hoover, J., Lin, Y., Ji, H., & Dehghani, M. (2018). Moralization in social networks and the emergence of violence during protests. Nature Human Behaviour, 2(6), 389-396. https://doi.org/10.1038/s41562-018-0353-0

Moreland, R. L., Levine, J. M., & McMinn, J. G. (2001). Selfcategorization and work group socialization. In M. A. Hogg & D. J. Terry (Eds.), Social identity processes in organizational contexts (pp. 87-100). Psychology Press

Moreland, R. L., & McMinn, J. G. (1999). Gone but not forgotten: Loyalty and betrayal among ex-members of small groups. Personality and Social Psychology Bulletin, 25(12), 1476-1486. https://doi.org/10.1177/01461672992510004

Nassauer, A. (2018). Situational dynamics and the emergence of violence in protests. Psychology of Violence, 8(3), 293. https://doi.org/10.1037/vio0000176

Nie, X., & Wager, S. (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika, 108(2), 299-319. https://doi.org/10. 1093/biomet/asaa076

Nisbett, R. E., Peng, K., Choi, I., & Norenzayan, A. (2001). Culture and systems of thought: holistic versus analytic cognition. Psychological Review, 108(2), 291. https://doi.org/10.1037/0033- 295X.108.2.291

Oh, O., Agrawal, M., & Rao, H. R. (2013). Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37(2), 407-426. https://doi.org/10.25300/MISQ/2013/37.2.05

Palmer, J. R. B., Oltra, A., Collantes, F., Delgado, J. A., Lucientes, J., Delacour, S., Bengoa, M., Eritja, R., & Bartumeus, F. (2017). Citizen science provides a reliable and scalable tool to track disease-carrying mosquitoes. Nature Communications, 8, Article 916. https://doi.org/10.1038/s41467-017-00914-9

Pienta, D., Thatcher, J. B., Wright, R. T., & Roth, P. L. (2024). An empirical investigation of the unintended consequences of vulnerability assessments leading to betrayal. Journal of the Association for Information Systems, 25(4), 1079-1116. https://doi.org/10.17705/1jais.00875

Pinto, M. R., de Lima, Y. O., Barbosa, C. E., & de Souza, J. M. (2019). Towards fact-checking through crowdsourcing. In The Proceedings of the IEEE 23rd International Conference on Computer Supported Cooperative Work in Design (pp. 494-499). https://doi.org/10.1109/CSCWD.2019.8791903

Prabhu, A., Guhathakurta, D., Subramanian, M., Reddy, M., Sehgal, S., Karandikar, T., Gulati, A., Arora, U., Shah, R. R., & Kumaraguru, P. (2021). Capitol (Pat) riots: A comparative study of Twitter and Parler. arXiv. https://doi.org/10.48550/arXiv. 2101.06914

Quarantelli, E. L. (1993). Community crises: An exploratory comparison of the characteristics and consequences of disasters and riots. Journal of Contingencies and Crisis Management, 1(2), 67-78. https://doi.org/10.1111/j.1468-5973.1993.tb00009.x

Rai, A. (2020). Editor’s comments—The COVID-19 pandemic: Building resilience with IS research. MIS Quarterly, 44(2), iii-vii.

Reiljan, A. (2020). “Fear and loathing across party lines” (also) in Europe: Affective polarisation in European party systems. European Journal of Political Research, 59(2), 376-396. https://doi.org/10.1111/1475-6765.12351

Robert, L. P. (2019). Crowdsourcing controls: A review and research agenda for crowdsourcing controls used for macro-tasks. In V. J. Khan, K. Papangelis, I. Lykourentzou, & P., Markopoulos (Eds.) Macrotask crowdsourcing: Engaging the crowds to address complex problems (pp. 45-126). Springer

Roth, P. L., Goldberg, C. B., & Thatcher, J. B. (2017). The role of political affiliation in employment decisions: A model and research agenda. Journal of Applied Psychology, 102(9), 1286-1304. https://doi.org/10.1037/apl0000232

Sarker, S., Chatterjee, S., Xiao, X., & Elbanna, A. (2019). The sociotechnical axis of cohesion for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly, 43(3), 695-720. https://doi.org/10.25300/MISQ/2019/13747

Sethi, R. J. (2017). Crowdsourcing the verification of fake news and alternative facts. In Proceedings of the 28th ACM Conference on

Hypertext and Social Media (pp. 315-316). https://doi.org/ 10.1145/3078714.3078746

Shepherd, D. A., Patzelt, H., & Baron, R. A. (2013). “I care about nature, but…”: Disengaging values in assessing opportunities that cause harm. Academy of Management journal, 56(5), 1251-1273. https://doi.org/10.5465/amj.2011.0776

Simester, D., Timoshenko, A., & Zoumpoulis, S. I. (2020). Targeting prospective customers: Robustness of machine-learning methods to typical data challenges. Management Science, 66(6), 2495-2522. https://doi.org/10.1287/mnsc.2019.3308

Simon, B., & Klandermans, B. (2001). Politicized collective identity: A social psychological analysis. American Psychologist, 56(4), 319-331. https://doi.org/10.1037/0003-066X.56.4.319

Southern Poverty Law Center. (2020). Proud boys. https://www. splcenter.org/fighting-hate/extremist-files/group/proud-boys

Starbird, K., Maddock, J., Orand, M., Achterman, P., & Mason, R. M. (2014). Rumors, false flags, and digital vigilantes: Misinformation on Twitter after the 2013 Boston Marathon bombing. In IConference Proceedings. https://doi.org/10.9776/14308

Stein, J. (1997). How institutions learn: a socio-cognitive perspective. Journal of Economic Issues, 31(3), 729-740. https://doi.org/ 10.1080/00213624.1997.11505962

Stern, A. M. (2019). Proud boys and the White ethnostate: How the altright is warping the American imagination. Beacon Press.

Surowiecki, J. (2005). The wisdom of crowds. Anchor.

Taylor, J., & Joshi, K. D. (2019). Joining the crowd: The career anchors of information technology workers participating in crowdsourcing. Information Systems Journal, 29(3), 641-673. https://doi.org/ 10.1111/isj.12225

Tim, Y., Pan, S. L., Ractham, P., & Kaewkitipong, L. (2017). Digitally enabled disaster response: The emergence of social media as boundary objects in a flooding disaster. Information Systems Journal, 27(2), 197-232. https://doi.org/10.1111/isj.12114

Tolosana, R., Vera-Rodriguez, R., Fierrez, J., Morales, A., & Ortega-Garcia, J. (2020). Deepfakes and beyond: A survey of face manipulation and fake detection. arXiv. https://doi.org/10.48550 arXiv.2001.00179

Tschiatschek, S., Singla, A., Gomez Rodriguez, M., Merchant, A., & Krause, A. (2017). Detecting fake news in social networks via crowdsourcing. arXiv. https://doi.org/10.48550/1711.09025

Turner, J. C. (2010). Towards a cognitive redefinition of the social group. In T. Postmes & N. R. Branscombe (Eds.), Rediscovering social identity (pp. 210-234). Psychology Press. (Original work published 1981)

Van Vugt, M., & Hart, C. M. (2004). Social identity as social glue: The origins of group loyalty. Journal of Personality and Social Psychology, 86(4), 585-598. https://doi.org/10.1037/0022-3514. 86.4.585

Wang, J., Ipeirotis, P. G., & Provost, F. (2017). Cost-effective quality assurance in crowd labeling. Information Systems Research, 28(1), 137-158. https://doi.org/10.1287/isre.2016.0661

Willison, R., Warkentin, M., & Johnston, A. C. (2018). Examining employee computer abuse intentions: Insights from justice, deterrence and neutralization perspectives. Information Systems Journal, 28(2), 266-293. https://doi.org/10.1111/isj.12129

Wilson, T., & Starbird, K. (2021). Cross-platform information operations: Mobilizing narratives & building resilience through both “big” & “alt” tech. Proceedings of the ACM on Human-Computer Interaction, 5(CSCW2), Article 345. https://doi.org/ 10.1145/3476086

Ye, H. J., & Kankanhalli, A. (2017). Solvers’ participation in crowdsourcing platforms: Examining the impacts of trust, and benefit and cost factors. The Journal of Strategic Information Systems, 26(2), 101-117. https://doi.org/10.1016/j.jsis.2017.02.001

Yin, J., Luo, J., & Brown, S. A. (2021). Learning from crowdsourced multi-labeling: A variational Bayesian approach. Information Systems Research, 32(3), 752-773. https://doi.org/10.1287/isre. 2021.1000

Zade, H., Shah, K., Rangarajan, V., Kshirsagar, P., Imran, M., & Starbird, K. (2018). From situational awareness to actionability: Towards improving the utility of social media data for crisis response. Proceedings of the ACM on human-computer interaction, 2(CSCW), Article 195. https://doi.org/10.1145/ 3274464

Zhuang, H., & Young, J. (2015). Leveraging in-batch annotation bias for crowdsourced active learning. In Proceedings of the Eighth ACM International Conference on Web Search and Data Mining (pp. 243-252). https://doi.org/10.1145/2684822.2685301

## About the Authors

Daniel A. Pienta (ORCID: 0000-0002-0171-6372) is an assistant professor in the Department of Accounting and Information Management and a research fellow of the Neel Corporate Governance Center at the University of Tennessee, Knoxville. His research interests include information security and privacy, crowds, and civil unrest. Before academics, he consulted some of the largest U.S. financial institutions on due diligence and cybersecurity. He earned his Ph.D. from Clemson University, M.B.A. from Cleveland State University, and B.A. from The Ohio State University. He serves as an associate editor for the Journal of the Association for Information Systems. His research has appeared in journals such as MIS Quarterly, Information Systems Research, Journal of Management Information Systems, and Journal of the Association for Information Systems.

Sriram Somanchi (ORCID: 0000-0002-3153-1248) is an associate professor of business analytics in the Mendoza College of Business at the University of Notre Dame. He received his Ph.D. in information systems and management from Heinz College at Carnegie Mellon University. He is a graduate of the Machine Learning Department at CMU and earned an M.E. in computer science from the Indian Institute of Science, Bangalore, India. His research harnesses the power of large-scale data and machine learning to discover subgroups that are statistically robust and theoretically grounded. He showcases the wide applicability of subgroup discovery methods to address important issues in healthcare, digital experimentation, crowdsourcing, behavioral economics, and service operations. His research has been published in MIS Quarterly, Journal of Machine Learning Research, the Journal of Computational and Graphical Statistics, ACM Transactions of Information Systems, Manufacturing and Service Operations Management, and Production and Operations Management. His research draws on a rich foundation in social science and statistical machine learning to develop and deploy methods that bridge these related but distinct disciplines.

Nishant Vishwamitra (ORCID: 0000-0002-3728-1921) is an assistant professor at the University of Texas at San Antonio. He received his Ph.D. in computer science and engineering from the University at Buffalo. His primary research areas are artificial intelligence, cybersecurity, online abuse defense, crowds, and disaster management. He has extensive experience in AI model design and development, information system design and development, and empirical studies. His work has appeared in MIS Quarterly and in the proceedings of several international conferences. His research is currently supported by the National Science Foundation.

Nicholas Berente (ORCID: 0000-0002-1403-4696) is a professor of IT, analytics, and operations at the University of Notre Dame’s Mendoza College of Business. He received his Ph.D. from Case Western Reserve University. His research interests include digital innovation, artificial intelligence, and institutional change in organizations. He is a senior editor at MIS Quarterly and at Information and Organization.

Jason Bennett Thatcher (0000-0002-7136-8836) holds the Tandean Rustandy Esteemed Professorship in the Division of Organizational Leadership and Information Analytics of the Leeds School of Business at the University of Colorado Boulder. He also has an appointment as full professor at Alliance Manchester Business School, University of Manchester. He received degrees from the University of Utah and Florida State University. His work appears in MIS Quarterly, Information Systems Research, Journal of the Association for Information Systems, Journal of Management Information Systems, and Journal of Applied Psychology. He is a current senior editor at MIS Quarterly and past senior editor at Information Systems Research. Jason’s days are filled with diverse pursuits. From remembering moments with Max the Wonder Dog to indulging in daydreams of the Alps in springtime, he finds inspiration in the simplicity of everyday life.

## Appendix

## Double/Debiased Machine Learning (DML)

In this section, we provide details about our application of DML for identifying subgroups. We included standard procedures, guidance, and conditions for the DML technique and the reasons we chose DML to discover subgroups, and robustness checks (i.e., nonlinear DML) in our analysis.

## Formulation of DML for Identifying Subgroups

Our analysis employed DML methods to investigate the heterogeneity of the validation decisions and find subgroups based on political identification. DML methods are state-of-the-art techniques to estimate conditional treatment effects in randomized experiments. This section formally introduces the notation and formulation of the DML model. Let ?? be the set of variables on which treatment effect heterogeneity is explored. In our case, ?? captures the self-identified political identification on a scale from 1 to $^ { 7 , }$ where 1 represents progressives and 7 represents conservatives. Let ?? be the set of other control variables such as age, gender, and education level that describe the participants. Each participant validates four kinds of images in our settings—true information, true information at a different angle, deepfake, and false information. Let $Y ^ { k }$ be the validation decision each participant provides for $k = 1 , 2 , 3 ,$ 4 for each kind of image. Finally, let $T ^ { P }$ and $T ^ { A }$ be the Proud Boys and ANTIFA binary treatments, respectively. If we formulate the DML models for one of the treatments, say $T ^ { P }$ , and the formulation remains the same for other treatment $T ^ { A }$ . DML models assume the following structural equations for data generation:

$$
\begin{array}{r l} & Y ^ {k} = \theta^ {k} (X) \cdot T ^ {P} + g (X, W) + \epsilon_ {1} \\ & T ^ {P} = f (X, W) + \epsilon_ {2}, \end{array}
$$

where $\theta ^ { k } ( X )$ is the conditional average treatment effect (CATE) for a given set of values for $X = x ~ ( \mathrm { e . g . } ,$ , a given scale of political identification in our case). Further, it is assumed $E [ \epsilon _ { 1 } \mid X , W ] = 0 , E [ \epsilon _ { 2 } \mid X , W ] = 0 ,$ and $E [ \epsilon _ { 1 } \cdot \epsilon _ { 2 } \mid X , W ] = 0$ in order to make a valid inference. One of the main reasons we used DML methods is that we did not have to assume a functional form (e.g., a linear function) for the functions $g$ and $f$ in the above structural equation models, thereby reducing model misspecification and reducing bias. Furthermore, DML methods provide an unbiased and root n-consistent (finite sample convergence) estimation of CATE $\theta ^ { k } ( X )$ . This faster convergence, along with the cross-fitting technique (Nei & Wagar, 2021), helped in our setting as we had a limited participant sample.

The above structural equations can be rewritten as follows to estimate CATE with

$$
Y - E [ Y | X, W ] = \theta^ {k} (X) \cdot (T - E [ T | X, W ]) + \epsilon ,
$$

where we can learn conditional expectation functions $E [ Y | X , W ]$ and $E [ T | X , W ]$ non-parametrically using machine learning techniques. These are the two machine learning models that DML methods build: (1) predict the outcome from the set of control variables $X , W$ and (2) predict the treatment from the set of control variables $X , W$ . Once we learn the conditional expectations, we can find the residual

$$
\tilde {Y} = Y - E [ Y | X, W ]
$$

$$
\tilde {T} = T - E [ T | X, W ]
$$

Finally, we ran a regression model as follows to estimate CATE $\theta ^ { k } ( X )$ (Nie & Wagar, 2021):

$$
\tilde {Y} = \theta^ {k} (X) \cdot \tilde {T} + \epsilon .
$$

The estimate of ${ \widehat { \theta } } ^ { k } ( X )$ from the above regression equation can then identify the treatment effect for a given value of $X = x .$ . In our case, this helped us understand the treatment effect for a given scale of self-identified political identification. Note that the treatment effect in this study is the difference in the validation probability between the treatment group and the control group. For instance, for the true information image, if the treatment effect is positive for Proud Boys $( T ^ { P } )$ for a given subgroup, then that specific subgroup validates the information more compared to the same subgroup under control settings.

## DML Prechecks and Implementation Details

Before applying DML, we ran logistic regression to understand if there was heterogeneity in the data. Specifically, we ran logistic regressions on the type of information validated (i.e., true, true different angle, false deepfake, false different event) as an outcome and two predictors: treatment (i.e., Proud Boys, ANTIFA, control) and political identification (PIDE). As explained, these models did not reveal significant results, though the interaction coefficient terms direction showed interesting patterns. We suspect this could be because there was a nonlinear relationship between control variables and the outcome and treatment. Therefore, we used the DML technique, which can capture such nonlinear relationships in the first stage and provide an unbiased estimate of the treatment effects. Second, as explained earlier, DML can help identify heterogeneity in smaller sample data due to cross-fitting techniques. Finally, even after capturing the nonlinear relationships, linear DML can reveal how the treatment effect varies linearly with PIDE, which makes it easily interpretable. This makes DML a more attractive technique than others to identify heterogeneous treatment effects, such as meta-learners (Künzel et al., 2019).

After cleaning the data, we identified PIDE as the variable (??) to explore the heterogeneity of data validation. We then included other control variables (??), such as age, gender, and education level, in our DML models. Since our outcome variable (??) and treatment variable (??) were binary, we built a random forest classifier in the first stage to compute the conditional expectations ??[?? | ??, ??] and ??[??| ??, ??]. Our results are robust to other choices of classifiers (such as gradient boosted forests or multilayer perceptron) in this first stage of the DML model. We then used a Linear DML model for the second stage to extract heterogeneity of the political identification on validation patterns. We chose Linear DML to elicit more interpretable results. Our pattern of results is robust to nonlinear DML models, as shown below. In order to obtain an unbiased estimation, ideally, data splitting should be performed for building the first and second stages of DML. However, the disadvantage of data splitting is the reduction in sample size. Therefore, as suggested by (Chernozhukov et al., 2018), we used a cross-fitting technique where the DML procedure is repeated multiple times (say, ???? times). The data is split into disjoint ???? subsets $\{ s _ { 1 } , s _ { 2 } , \ldots , s _ { c v } \}$ for each run ?? of the DML procedure; the first stage is built on the dataset $\boldsymbol { s } = \cup _ { j = 1 , j \neq i } ^ { c v } s _ { j } .$ , and the second stage is built on the dataset ??

The final treatment effect estimated is average across ???? runs of the DML procedure. Therefore, this cross-fitting technique helped us in estimating unbiased treatment effects without needing large datasets. We used ???? = 3 in our analysis as we wanted to balance the data for the first and second stages of DML. However, our results are robust to the modification of this parameter. Once we fit the DML model using the cross-fitting technique, we visualized the heterogeneity of the treatment effect for the political identification variable, as shown in Figure 3. We used DML methods implemented in the econml Python package.

There are more recent techniques (C-DML) that further reduce the bias in treatment effects estimated by DML (Fingerhut et al., 2022). The main idea of these models is to simultaneously estimate the outcome and treatment models in the first stage. However, such techniques require more data to be able to estimate the two models simultaneously. Therefore, we opted to show our results using the linear DML model. Future research could explore the use of C-DML models in experimental data to further reduce the bias in treatment effect estimation.

Finally, before applying the DML technique, it is essential to ensure the data used to identify the heterogeneous treatment effects is from a randomized experiment. Though the DML technique can be applied in observational data under the conditional ignorability or unconfoundedness assumption (i.e., observed covariates fully explain the relationship between treatment and outcome—no unobserved covariates), it is important to note that this assumption is untestable. Also, even in randomized experiments, if there is an imbalance in the number of observations between treatment and control, it can be hard to estimate the treatment effects with DML correctly. In such cases, it is crucial to verify the covariate balance between treatment and control units (Imbens & Rubin, 2015). Overall, we believe the DML technique is useful for analyzing experimental and observational data to estimate CATE that can further elicit subgroups in the data. The discovery of these subgroups through DML and similar techniques (Hill, 2011; Künzel et al., 2019) can help researchers obtain a nuanced understanding of behavioral patterns. Note that these techniques are only helpful for analyzing observational data when the goal is to understand the effect of a treatment on an outcome, given a set of observed covariates.

## Robustness of Results of the DML Model

We performed robustness checks for the choices we made in the DML models. First, as we discussed earlier, our results remain robust to the different choices of classifiers (such as gradient-boosted forests or multilayer perceptron) in the first stage. Second, our results remain robust to the modification to the cross-validation parameter ????. Third, we used nonlinear models in the second stage of the DML instead of the linear models we used in our main analysis. Specifically, we used causal forest models (Athey et al., 2019) in the second stage, which are tree-based techniques that are known to extract nonlinear relationships. Similar to earlier analysis, we used random forest classifiers in the first stage and then used a causal forest in the second stage. We used a cross-fitting technique with ???? = 3 and visualized the heterogeneity of the treatment effect for the political identification variable. The results are shown in Figure A1. Because we modeled the second stage as a causal forest model, there is nonlinearity in the treatment effect across various values of the PIDE variable. However, the overall pattern, in terms of the direction of increase/decrease of treatment effect with respect to PIDE and its significance, is similar to the linear DML model (Figure 3).

<table><tr><td rowspan="2">True information</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td><td></td></tr><tr><td>0.4TRUE Treatment Effect</td><td>0.0TRUE Treatment Effect</td><td>0.0TRUE Treatment Effect</td><td></td></tr><tr><td rowspan="2">True information (different angle)</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td><td></td></tr><tr><td>0.4DIFANG Treatment Effect</td><td>0.0DIFANG Treatment Effect</td><td>0.0DIFANG Treatment Effect</td><td></td></tr><tr><td rowspan="2">False information (deepfake)</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td><td></td></tr><tr><td>0.4DIFK Treatment Effect</td><td>0.0DIFK Treatment Effect</td><td>0.0DIFK Treatment Effect</td><td></td></tr><tr><td rowspan="2">False information (not from crisis)</td><td>PB vs Control</td><td>ANTIFA vs Control</td><td>ANTIFA vs PB</td><td></td></tr><tr><td>0.4FLSE Treatment Effect</td><td>0.0FLSE Treatment Effect</td><td>0.0FLSE Treatment Effect</td><td></td></tr><tr><td rowspan="4">N of subgroups</td><td></td><td>Proud Boys</td><td>ANTIFA</td><td>Control</td></tr><tr><td>Progressives</td><td>53</td><td>40</td><td>43</td></tr><tr><td>Independents</td><td>39</td><td>34</td><td>45</td></tr><tr><td>Conservatives</td><td>64</td><td>51</td><td>54</td></tr><tr><td colspan="5">Note: PB = Proud Boys, PIDE = political identification (1 = progressive, 2 = somewhat progressive, 3 lean progressive, 4 = independent, 5 = lean conservative, 6 = somewhat conservative, 7 = conservative)</td></tr></table>

Figure A1. DML Heterogeneity Analysis using Causal Forest in the Second Stage

<table><tr><td colspan="2">Table A1. Measures for Loyalty and Betrayal</td></tr><tr><td>Adapted Loyalty Scale (James &amp; Cropanzano, 1994)AVE = 0.82, CR = 0.98 ,  $\text{AVE}^{2}$  = 0.90, Correlation = 0.61 , VIF = 1.00</td><td>Factor loadings</td></tr><tr><td>I defend the honor ofat all times if unfairly criticized.</td><td>0.79</td></tr><tr><td>I always support all the actions of.</td><td>0.90</td></tr><tr><td>I will perform unpleasant tasks if required by.</td><td>0.87</td></tr><tr><td>I remember my loyalty to &lt; the Proud Boys, ANTIFA &gt; at all times.</td><td>0.94</td></tr><tr><td>I take an active role in part of affairs.</td><td>0.96</td></tr><tr><td>I always work hard to improve the prestige and status of.</td><td>0.95</td></tr><tr><td>Adapted Betrayal Scale (Jones &amp; Burdette, 1994; Pienta et al., 2024)AVE = 0.86, CR = 0.99,  $\text{AVE}^{2}$  = 0.93, Correlation = 0.61 , VIF = 1.00</td><td></td></tr><tr><td>I feel betrayed by &lt; the Proud Boys, ANTIFA&gt;.</td><td>0.92</td></tr><tr><td>I feel cheated by.</td><td>0.93</td></tr><tr><td>I feel lied to by.</td><td>0.94</td></tr><tr><td>I feelintended to take advantage of me.</td><td>0.95</td></tr><tr><td>I feeldouble-crossed me.</td><td>0.90</td></tr><tr><td>I feelviolated my trust.</td><td>0.93</td></tr></table>

Note: Model Fit: x<sup>2</sup> <sup>=</sup> 133.67, df = 53, p < 0.001, CFI = 0.97, RMSEA = 0.07, 90% Confidence Interval 0.06, 0.08, SRMR = 0.04 Scale: (1 =“ Strongly Disagree” to 7 = “Strongly Agree”)
