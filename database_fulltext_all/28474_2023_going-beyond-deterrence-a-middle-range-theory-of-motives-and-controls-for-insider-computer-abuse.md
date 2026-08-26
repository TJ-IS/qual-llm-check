---
otero_id: 28474
otero_key: "ZKB3M3MB"
title: "Going Beyond Deterrence: A Middle-Range Theory of Motives and Controls for Insider Computer Abuse"
authors: "A. J. Burns; Tom L. Roberts; Clay Posey; Paul Benjamin Lowry; Bryan Fuller"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1133"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Going Beyond Deterrence: A Middle-Range Theory of Motives and Controls for Insider Computer Abuse

A. J. Burns,<sup>a</sup> Tom L. Roberts,<sup>b</sup> Clay Posey,<sup>c</sup> Paul Benjamin Lowry,<sup>d,</sup>\* Bryan Fuller<sup>e</sup>

<sup>a</sup> Stephenson Department of Entrepreneurship and Information Systems, E. J. Ourso College of Business, Louisiana State University, Baton Rouge, Louisiana 70803; <sup>b</sup> Soules College of Business, The University of Texas at Tyler, Tyler, Texas 75799; <sup>c</sup> Information Systems Department Marriott School of Business, Brigham Young University, Provo, Utah 84602; <sup>d</sup> Business Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, Virginia 24061; <sup>e</sup> Department of Management, Louisiana Tech University, Ruston, Louisiana 71272 \*Corresponding author

Contact: ajburns@lsu.edu, https://orcid.org/0000-0001-8222-4144 (AJB); tomroberts@uttyler.edu, https://orcid.org/0000-0003-4480-0475 (TLR); clay.posey@byu.edu, https://orcid.org/0000-0001-6704-0750 (CP); paul.lowry.phd@gmail.com, https://orcid.org/0000-0002-0187-5808 (PBL); bfuller@latech.edu, https://orcid.org/0000-0002-3751-1993 (BF)

Received: January 23, 2020 Revised: April 22, 2021; February 3, 2022 Accepted: March 28, 2022 Published Online in Articles in Advance: May 10, 2022

https://doi.org/10.1287/isre.2022.1133

Copyright: © 2022 INFORMS

Abstract. Despite widespread agreement among practitioners and academicians that organizational insiders are a signi<sup>fi</sup>cant threat to organizational information systems security, insider computer abuse (ICA)—unauthorized and deliberate misuse of organizational information resources by organizational insiders—remains a serious issue. Recent studies have shown that most employees are willing to share con<sup>fi</sup>dential or regulated information under certain circumstances, and nearly one-third to half of major security breaches are tied to insiders. These trends indicate that organizational security efforts, which generally focus on deterrence and sanctions, have yet to effectively address ICA. Therefore, leading security researchers and practitioners have called for a more nuanced understanding of insiders in respect to deterrence efforts. We answer these calls by proposing a middle-range theory of ICA that focuses on understanding the inherent tensions between insider motivations and organizational controls. Our careful review distinguishes two categories of personal motives for ICA: (1) instrumental (i.e., <sup>fi</sup>nancial bene<sup>fi</sup>ts) and (2) expressive (i.e., psychological contract violations) motives. Our novel theory of ICA also includes the in<sup>fl</sup>uence of two classes of controls for ICA: (1) intrinsic (i.e., self-control) and (2) extrinsic (i.e., organizational deterrence) controls. We developed and empirically examined a research model based on our middlerange theory that explains a substantial portion of the variance in ICA. Speci<sup>fi</sup>cally, our results indicate that both instrumental and expressive motives are positively related to ICA. Moreover, intrinsic self-control exerted signi<sup>fi</sup>cant direct and moderating in<sup>fl</sup>uences in our research model, whereas extrinsic organizational deterrence failed to exhibit a direct effect on ICA and signi<sup>fi</sup>cantly moderated instrumental motives’ relationship with ICA only. Not only do our results show that self-control exerted a stronger effect on the model than deterrence did but they also help us identify the limits of deterrence in ICA research.

History: Ola Henfridsson served as the senior editor and Debabrata Dey served as associate editor for this article.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1133.

Keywords: cybersecurity organizational security information security insider computer abuse (ICA) self-control theory deterrence theory (DT) instrumental motives expressive motives

## 1. Introduction

Organizations expend considerable resources to shield their sensitive information and associated systems from security threats from both external and internal sources (D’Arcy and Hovav 2007, Lowry et al. 2017a). Internally, organizations are susceptible to acts committed by organizational insiders (i.e., individuals with legitimate access to information within the organization, including employees, contractors, board members, and suppliers; Posey et al. 2013), who are responsible for 25%–50% of all reported security breaches (PWC 2014, Ponemon Institute 2018). Such incidents can be costlier and more damaging than those caused by outsiders (Miller 2018), with recent reports identifying privilege abuse as the most common insider tactic.

Recent security events exemplify the seriousness of the risks posed by insiders committing insider computer abuse (ICA). For example, nation-state hackers recently sought to compromise Tesla’s network by offering an employee a large sum of money to install malware on the corporate network (Greenberg 2020). Moreover, a former General Electric employee recently pleaded guilty to illicitly downloading thousands of <sup>fi</sup>les containing

It is critical to note that we are not interested in mere employee carelessness or lack of policy compliance; our focus is on harmful insider behavior relating to organizational information assets that is unauthorized and deliberate (Straub 1990). Moreover, this behavior involves different motives and factors than employee errors and other forms of incidental noncompliance. Drawing on Straub’s early work (e.g., Straub 1990), the literature identi<sup>fi</sup>es such behavior as ICA (Posey et al. 2011; Willison and Lowry 2018; Willison et al. 2018a, b). Given the importance of preventing ICA, researchers have long endeavored to better understand it by conducting theoretical and empirical studies (e.g., Straub 1990; Straub and Nance 1990; Harrington 1996; Lee et al. 2004; D’Arcy et al. 2009; Lowry et al. 2013b, 2015; Willison et al. 2018a, b). Many researchers have employed research models based, at least in part, on deterrence theory (DT; e.g., Nagin 1998) as a means to thwart ICA (D’Arcy and Herath 2011, Willison et al. 2018a).

Despite their relatively widespread acceptance, a critical shortcoming of traditional deterrence-based studies is their singular focus on sanction perceptions. DT largely ignores other important motives and controls that may also in<sup>fl</sup>uence individuals’ ICA (D’Arcy and Herath 2011, Hu et al. 2011). As noted by Gottfredson (2011, p. 132),

Deterrence theory makes very little room for individ ual differences in responsiveness to sanctions, preferring instead to focus on aspects of sanctions that make them more or less effective.

Hence, security researchers are increasingly advocating for a broader consideration of insiders’ motives to engage in ICA, because traditional deterrence fails to address these crucial motivational precursors (Crossler et al. 2013; Willison and Warkentin 2013; Willison et al. 2018a, b). In response, we propose a middle-range theory to explain how ICA occurs and how it can be thwarted. To accomplish this goal, we begin our study with a thorough literature review to better understand extant ICA research. Our analyses highlight the need for an expanded view of ICA that addresses the natural tensions between insider motives and organizational controls. Drawing on criminological theory, we assert that these tensions pose two classic questions about ICA (Hirschi 2017): (1) Why do some insiders commit ICA? (2) Why do some insiders choose not to commit ICA?

The <sup>fi</sup>rst mechanisms in our ICA theory involve two distinct classes of motives: instrumental and expressive motives, which were proposed by Willison and Warkentin (2013) for addressing ICA but have yet to be used in empirical research on ICA. Consequently, the balanced consideration of these two factors is foundational to our theorizing. First, when ICA is committed as a means to achieve another objective, it is said to be fueled by instrumental motives (Willison and Warkentin 2013).<sup>3</sup> By contrast, expressive motives are described as fueling ICA aimed at expressing individuals’ emotions such that the ICA is performed for its own purposes as an end in itself (Willison and Warkentin 2013).<sup>4</sup> Thus, the key in distinguishing between instrumental and expressive motives lies in understanding the motivation behind the behavior, not the resulting ICA behaviors themselves.

Beyond the instrumental and expressive motives for committing ICA, the second mechanisms in our theory are intrinsic and extrinsic controls, which inhibit ICA motivations. As noted earlier, organizational deterrence is a form of extrinsic control that relies on individuals perceptions of the certainty, severity, and celerity (i.e., speed) of extrinsic sanctions to counteract any perceived bene<sup>fi</sup>ts of engaging in undesirable behavior (Yu 1994, Nagin 1998). Despite the clear contributions of research using the organizational deterrence foundation, intrinsic controls comprise an important complementary area of investigation for organizational security research (Crossler et al. 2013, Lowry et al. 2017a). A particularly promising intrinsic control for consideration is selfcontrol (Hu et al. 2011, 2015; Li et al. 2018), which has been de<sup>fi</sup>ned as “the ability to forgo immediate or nearterm pleasures that have some negative consequences” or simply “the ability to act in favor of longer-term interests” (Gottfredson 2017). Importantly, extant research indicates that differences in self-control help explain insiders’ reactions to stimuli and their subsequent decision-making processes regarding ICA (Hu et al. 2011, 2015; Li et al. 2018).

Given the compelling need to improve our understanding of the causes of ICA if we are to better thwart this behavior, we propose the motive–control (MoCo) theory of ICA. The MoCo theory addresses key shortcomings in deterrence theory by not only acknowledging a broader set of motives and controls than considered in DT, but also the complex interplay among these different motives and controls. In short, the MoCo theory offers a better, more complete, explanation of the key tensions that insiders experience when faced with the possibility of committing ICA than provided by prior theoretical frameworks. This middle-range theory distinguishes between the in<sup>fl</sup>uences of expressive and instrumental motives on ICA and explains how intrinsic (i.e., self-control) and extrinsic (i.e., organizational deterrence) controls moderate these relationships. As an initial test of the hypotheses inherent in the MoCo theory and the utility of this new theory, we used an online <sup>fi</sup>eld study of 532 full-time professionals and found that both instrumental (i.e., <sup>fi</sup>nancial bene<sup>fi</sup>ts) and expressive (i.e., psychological contract violations, or PCVs) motives drive ICA. Also, intrinsic control (i.e., self-control) exhibited both direct and moderating effects in our model, whereas the extrinsic control of organizational deterrence failed to exert a direct relationship with ICA and signi<sup>fi</sup>cantly moderated the relationship between our instrumental motive and ICA only. These <sup>fi</sup>ndings support the view that research in our <sup>fi</sup>eld needs to go beyond deterrence foundations when examining ICA and demonstrates that the MoCo theory represents an important advancement for both research and practice.

## 2. Proposal of a Middle-Range Theory of Insider Computer Abuse

Employees can exhibit many undesirable behaviors in the workplace. For example, previous organizational research identi<sup>fi</sup>es problematic behaviors such as sabotage (Wang et al. 2011), antisocial behavior (Robinson and O’Leary-Kelly 1998), counterproductive work behavior (Dalal 2005), organizational misbehavior (Vardi 2001), and organizational deviance (Bennett and Robinson 2000). In security research, phenomena such as cyberloa<sup>fi</sup>ng (Khansa et al. 2017), phishing victimization (Jensen et al. 2017), system misuse intentions (D’Arcy et al. 2009), unethical information technology (IT) use (Chatterjee et al. 2015), and cyber harassment (Lowry et al. 2016b, 2017b) have been investigated.

To better understand security-related phenomena, researchers have, for example, drawn on compliance theory (Chen et al. 2012), rational choice theory (RCT; Willison and Lowry 2018, D’Arcy and Lowry 2019), protection motivation theory (PMT; Boss et al. 2015, Johnston et al. 2015, Posey et al. 2015, Burns et al. 2017, Menard et al. 2018), fairness theory (Lowry et al. 2015), self-control theory (Hu et al. 2015), and DT (Straub 1990, D’Arcy et al. 2009, D’Arcy et al. 2014). However, not all undesirable workplace behaviors have the same causes and explanations, especially those related to security (e.g., D’Arcy et al. 2009, Boss et al. 2015, Willison and Lowry 2018). We focus on unauthorized and deliberate $\mathrm { I C A } ^ { 5 }$ because it is potentially the most destructive form of insider behavior, and as its motivations differ from unintentional or innocuous behaviors, it requires theorizing beyond mere compliance or deterrence (Willison and Warkentin 2013, Lowry et al. 2017a, Willison et al. 2018a).

Attempts to use organizational deterrence and its sanctions to thwart ICA are particularly challenging and have resulted in con<sup>fl</sup>icting explanations and outcomes, thus repeatedly leading to conclusions that deterrence alone is insuf<sup>fi</sup>cient or even detrimental (D’Arcy and Herath 2011, Hu et al. 2011, Willison and Warkentin 2013, Lowry et al. 2015, Willison et al. 2018a). Crucially, security researchers have overlooked what criminologists have long concluded: that deterrence is a form of control (Meier and Johnson 1977) and ICA decisions are in<sup>fl</sup>uenced by subjective assessments (Willison et al. 2018a). Thus, other forms of control and personal motivations should also be considered (Willison and Warkentin 2013, Willison et al. 2018a). Despite explicit calls for this more expansive view (Willison and Warkentin 2013, Willison et al. 2018a), relatively little ICA research has incorporated insiders’ personal motivations (e.g., instrumental and expressive motives) and intrinsic controls (e.g., self-control) with extrinsic controls (i.e., organizational sanctions) to gain a more encompassing understanding of ICA in actual organizational contexts. Even less attention has been given to the extent to which these motives and controls might outperform the more traditional extrinsic concepts of disincentives in decreasing ICA. Figure 1 exhibits our proposed framework of ICA motives and controls along with prototypical examples of key constructs.

Our framework re<sup>fl</sup>ects the philosophy that researchers must move beyond merely applying theories from reference disciplines to explain the tensions and contingencies involved in ICA. These theories often lack the unique contextual considerations to effectively address the well-known ICA problem. We contend that this research gap requires theories that leverage Merton’s (1968) theory of the middle range. Such middle-range theorization has shown great promise in information systems (IS) research (Tiwana 2009, 2015; Hassan and Lowry 2015; Park et al. 2017; Hassan et al. 2019). This paradigm also aligns with the growing IS research movement to embrace contextualization and focus on enhanced theoretical and practical contributions (Avgerou 2001, Hong et al. 2014, Davison and Martinsons 2016, Breward et al. 2017). Thus, these middle-range theories should not be confused with broader grand theories (e.g., Leidner and Tona 2021) or the midrange theories criticized by Grover and Lyytinen (2015). Essentially, rather than trying to develop a theory that is highly generalizable to various behaviors in many contexts (e.g., theory of planned behavior, DT, RCT, PMT), we focus on one context (i.e., organizational security concerns) and one behavior set (i.e., ICA) and tighten the boundary conditions and assumptions surrounding them. This approach allows a clear research discourse through which we can look deeply at speci<sup>fi</sup>c situational contingencies that give rise to ICA in organizations, allowing for a deeper theoretical understanding of our phenomena. IS and security researchers are increasingly advocating this kind of highly contextualized theorizing because this approach is crucial for bridging theory with actual meaningful recommendations that can improve practice.

Figure 1. Framework of ICA Motives and Controls  
![](/api/attachments/ZKB3M3MB/fulltext/images/69e07be567fd650ca34f82d87cc22c0962ba940657ea00023da6fcc30f3a50f4.jpg)

Figure 2. Motive–Control Theory of ICA  
![](/api/attachments/ZKB3M3MB/fulltext/images/ce35b311ee0e7812177786083b1a6a001bc96ec8e78d2baf2ee99a15e774f34d.jpg)

Thus, our aim is not simply theoretical, but also pragmatic. Following Gregor (2006, p. 613), we are interested in building theory as “statements of relationships among constructs that can be tested.” Our novel theory of ICA provides a model that will translate directly to practice and improve organizational information security. Like all middle-range theories, we are bound by the limits of the “range” of the theory, that is, “the conceptual and contextual assumptions under which the model was developed” (Rivard 2021, p. 317). For example, our theory is developed within the organizational context and assumes that organizational insiders have access and opportunity for ICA. However, given the ubiquity of today’s organizational IS, most insiders fall within the boundary of our research. Importantly, 8% of all data breaches stem from such insider attacks, and they are among the costliest for organizations, at an average of \$4.61 million per incident.<sup>6</sup> Although ICA is a broadrange topic within organizational IS security, we are not proposing a “grand theory” for understanding all forms of computer abuse. In the following sections, we describe the MoCo theory of ICA and link the conceptual elements of the theory to the speci<sup>fi</sup>c hypotheses in our proposed research model. Figure 2 exhibits the causal logic implied in our framework of ICA motives and controls. Our empirical research then operationalizes and tests these basic elements of the theory.

## 2.1. Instrumental and Expressive Motivations Facilitate Insider Computer Abuse

There are reasons why insiders may want to commit ICA despite their organizations not wanting them to do so. Theoretically, these reasons are categorized as instrumental and expressive motivations that facilitate or encourage ICA. In our context, we explain instrumental motivations in terms of career-related <sup>fi</sup>nancial bene<sup>fi</sup>ts and expressive motivations in terms of PCVs.

Brie<sup>fl</sup>y, the original conceptualizations of instrumental and expressive behavioral motives can be traced to Parsons and Bales’ (1955) use of the terms to explain different parenting behaviors. However, scholars today use the distinction between instrumental and expressive motives to gain insight into the origins of various behaviors, including supervisors’ fair treatment of subordinates (Qin et al. 2018), citizens’ support of political candidates (Brennan and Hamlin 1998), gang activities on social media (Storrod and Densley 2017), and criminal acts (Feshbach 1964). Notably, instrumental and expressive motives have been highlighted as a fruitful area of research to better understand ICA behaviors (Willison and Warkentin 2013).

2.1.1. Financial Benefits as a Primary Instrumental Motivation for Insider Computer Abuse. Instrumental motives can be thought of as extrinsic motives because they drive behavior that serves as a means to some extrinsic end or outcome (Leonard et al. 1999). People who display certain behavior for instrumental reasons do so because they are interested in that behavior’s future outcomes; that is, the behavior has value only because it is thought to be instrumental in obtaining some future bene<sup>fi</sup>t. For illustration, people may vote in an election because they are interested in the election’s consequences (Brennan and Hamlin 1998), commit arson to “hide evidence at a crime scene” (Wach et al. 2007, p. 30), or treat a subordinate fairly because the subordinate will work harder and exhibit more prosocial behavior, ultimately bene<sup>fi</sup>tting the supervisor (Qin et al. 2018).

Perhaps the most prototypical example of an instrumental motive is attaining a <sup>fi</sup>nancial bene<sup>fi</sup>t (Barbuto 2005). Individuals who are motivated by <sup>fi</sup>nancial bene<sup>fi</sup>ts will choose to act in ways that they believe will result in monetary gain that can be useful for achieving some other goal (e.g., paying bills, supporting family, or attaining higher social status). This expectation-driven motivation is similar to that predicted by other theoretical frameworks (e.g., Vroom 1964). Related to an expectancy-driven motivation, the perception of monetary bene<sup>fi</sup>ts can also increase the valence (i.e., preference) of goal-driven outcomes (Locke 1981).

However, instrumental motives can be potentially harmful when insiders perceive opportunities to gain <sup>fi</sup>nancial bene<sup>fi</sup>ts in ways that are at odds with organizational interests (Robinson and Bennett 1997, Ambrose et al. 2002). Examples of this in the realm of ICA range widely, from illegal behavior, such as an employee stealing credit card numbers or intellectual property to sell to a third party (Willison and Warkentin 2013), or stealing personal information for the purposes of identity theft, to intentional organizational policy violations aimed at increasing sales or attaining a higher bonus. As noted, the opportunities for <sup>fi</sup>nancial bene<sup>fi</sup>ts from ICA in contemporary organizations are numerous. Thus, we hypothesize the following.

Hypothesis 1. Insiders’ perceptions of financial benefits of committing ICA (an instrumental motive) are positively related to their ICA.

2.1.2. PCV as a Primary Expressive Motivation for Internal Computer Abuse. In contrast to instrumental motives, expressive motives drive behavior that is an end in and of itself rather than behavior that is a means to an objective. The bene<sup>fi</sup>t is intrinsic to the behavior itself, or the behavior is the direct expression of the individual’s goal (Youngs et al. 2016). For example, a citizen may vote in an election or support a political candidate because that behavior ful<sup>fi</sup>lls a civic responsibility or because it is an opportunity for self-expression (Brennan and Hamlin 1998). Another example would be when a supervisor treats his or her subordinates fairly because that behavior communicates the supervisor’s values, such as cooperation and benevolence (Qin et al. 2018). However, in situations where people feel they have been harmed, they are often motivated to exhibit aggressive or harmful behaviors that serve to “vent, release, or express one’s feelings of outrage, anger, or frustration” (Robinson and Bennett 1997, p. 16). Thus, the behavio is an emotionally driven retaliation against the party “who has caused harm to the actor” (Ambrose et al. 2002, p. 952).

A prototypical example of a negative expressive motivator is a PCV. A psychological contract is “made up of the employees’ beliefs about the reciprocal obliga tions between them and their organization” (Morrison and Robinson 1997, p. 226). Thus, a PCV occurs when employees perceive that their organization has failed to uphold its explicit and/or implicit obligations to them (Morrison and Robinson 1997, Pavlou and Gefen 2005, Zhao et al. 2007). This type of violation is an emotional experience that involves “feelings of betrayal and deeper psychological distress [whereby] … the victim experiences anger, resentment, a sense of injustice and wrongful harm” (Rousseau 1989, pp. 128–129).

PCVs have been linked to negative employee perceptions and behaviors, such as reduced trust toward employers, lower job satisfaction, reduced organizational commitment, and lower levels of citizenship behaviors (Morrison and Robinson 1997, Restubog et al. 2006, Zhao et al. 2007). Not surprisingly, as PCV elicits anger and even outrage (Morrison and Robinson 1997), it has been identi<sup>fi</sup>ed as an expressive motive for counterproductive workplace behaviors (Bordia et al. 2008) as well as interpersonal and organizational deviance (Chiu and Peng 2008). Thus, through its relationship with organizational deviance, PCV threatens “the well-being of an organization, its members, or both” (Robinson and Bennett 1995, p. 556). This is because employees who feel “let down” by their organization may express their dissatisfaction via behavior that works against the organization’s interests. For example, in the IS literature, PCV has been linked to resistance to the implementation of organizational systems (Lin et al. 2018).

As an example, related directly to ICA, a disgruntled systems administrator was convicted of sending malicious code to his employer, which led to over \$1 million in damage and a three-year sentence in federal prison.<sup>7</sup> According to the U.S. Department of Justice, the perpetrator was terminated shortly before he severely damaged the system by abusing his remote access to the plant where he had worked for many years. This is a clear example of an expressive motive because the individual had virtually nothing to gain by committing ICA. In fact, the potential repercussions for the employee were more signi<sup>fi</sup>cant than the damage in<sup>fl</sup>icted on the system. Yet this incident exempli<sup>fi</sup>es the type of damage insiders can in<sup>fl</sup>ict on systems through ICA when they feel the company has violated its psychological contract.

Likewise, in extant IS research, PCVs have been linked not only to feelings of violation but also to user resistance and deviance (Lin et al. 2018), and the similar phenomenon of perceptions of unfair treatment have been shown to relate to ICA (Posey et al. 2011, Lowry et al. 2015). Conversely, employee perceptions of their organizations’ contract ful<sup>fi</sup>llment have been linked to individuals’ information security policy compliance (Han et al. 2017). As PCVs tend to evoke negative emotions, PCV will likely be positively related to ICA because the behavior is an expression of insiders’ discontent and anger. Thus, we hypothesize the following.

Hypothesis 2. Insiders’ perceptions of PCV (an expressive motive) are positively related to their ICA.

## 2.2. Extrinsic and Intrinsic Controls Inhibit Insiders from Committing ICA

We have shown how instrumental and expressive motivations can lead insiders to commit ICA, but it is also vital to consider the countervailing tensions that push against such considerations; namely, theorization that includes multiple mechanisms for why individuals commit ICA alongside factors that inhibit such activity is required for a more encompassing view of this important organizational phenomenon. As such, our middle-range theory of ICA also includes both intrinsic (i.e., self-control) and extrinsic organizational controls (i.e., deterrence via sanctions).

2.2.1. Self-Control as a Primary Intrinsic Control that Inhibits Insider Computer Abuse. Apart from instrumental and expressive motives, researchers have noted various factors that can guide security-relevant behavior (Gottfredson and Hirschi 1990, Nagin and Paternoster 1993, Gottfredson 2017). These factors include stress and moral disengagement (D’Arcy et al. 2014), threat and coping appraisals (Johnston et al. 2016), and neutralization techniques (Siponen and Vance 2010). Security education, training, and awareness (SETA) programs have also been linked directly or indirectly to these important employee actions (D’Arcy et al. 2009).

Interestingly, although criminologists have identi-<sup>fi</sup>ed individual differences like self-control as a key construct in explaining individuals’ criminal behaviors and other noncriminal problematic behaviors (Gottfredson and Hirschi 1990, Gottfredson 2017), rel atively little research has investigated the in<sup>fl</sup>uence of insiders’ self-control on their willingness to engage in undesirable behaviors like ICA (Hu et al. 2015, Li et al. 2018). In fact, our review of information security publications in the Association for Information Systems (AIS) senior scholars’ basket that mention self-control or deterrence theory (see Online Appendix A) identi <sup>fi</sup>ed only a few studies that actually measured individuals’ self-control (i.e., Hu et al. 2015; Lowry et al. 2017b, 2019; Moody et al. 2018; Luo et al. 2020; Li et al. 2021). Given the potential in<sup>fl</sup>uence of self-control as a key individual difference in IS security research and lack of due attention, we explain its foundations and integrate it into the MoCo theory. In doing so, we expand on prior research to elevate self-control as a central construct that has a direct in<sup>fl</sup>uence on ICA as well as a powerful diminishing effect on both instrumental and expressive motives for ICA.

Self-control theory is a criminological theory that posits that people with low self-control are more likely than those with high self-control to commit a crime when presented with the opportunity (Gottfredson and Hirschi 1990). Self-control theory has been used to explain various criminal behaviors, such as fraud (Holtfreter et al. 2008), dating violence (Schreck et al. 2008), theft (Schreck 1999), and cyber harassment (Turanovic and Pratt 2014, Lowry et al. 2019). The causal mechanism involved in self-control in predicting problematic behavior is self regulation, or the ability to control one’s emotions and behaviors in seeking immediate grati<sup>fi</sup>cation (Gottfredson and Hirschi 1990, Murray and Kochanska 2002).

Self-control theory explains that people with low self-control are more emotionally driven and have more dif<sup>fi</sup>culty regulating their impulses toward grati <sup>fi</sup>cation than those with high self-control. Low self control is an absence of the capacity to self-regulate, thereby fostering deviant attitudes, beliefs, and intentions that lead to actual deviant behavior (Murray and Kochanska 2002). Seeking immediate grati<sup>fi</sup>cation can take several deviant forms, “whether the grati<sup>fi</sup>cation consists of pure hedonism, revenge, or the wielding of power” (Lowry et al. 2019, p. 1155). Nonetheless, this combination of low self-control and seeking immediate grati<sup>fi</sup>cation are crucial in the decision to commit a crime (Tibbetts and Gibson 2002), in violating widely held norms of conduct (Hu et al. 2011), and in repeatedly performing deviant acts (Turanovic and Pratt 2014). Conversely, individuals with higher self-control can better control their emotions and inclinations toward self-grati<sup>fi</sup>cation and are more rational and less reactionary, making them less inclined to commit ICA.

Moreover, research shows that as a key individual characteristic, self-control exists on a continuum within individuals (Tangney et al. 2004). Lower self-contro relates to greater impulsivity (Jones and Lynam 2009, Nagin and Pogarsky 2001), criminality, and deviance (Gottfredson and Hirschi 1990), and higher self-control relates to increased behavioral deliberation (Hu et al. 2015). For example, compared with their counterparts with higher self-control, individuals with lower selfcontrol often react quickly because they give less consideration to their behaviors before acting to derive near-term bene<sup>fi</sup>ts at the expense of longer-term payoffs (Hu et al. 2015). This shorter decision-making time horizon makes individuals more susceptible to perceived immediate bene<sup>fi</sup>ts that can harm them or their organizations in the longer term (Hu et al. 2011).

Time is thus a key consideration with self-control. The need for self-control can be explained through the principle of time discounting, whereby individuals perceive greater value in more immediately available benefits compared with future longer-term consequences of behavior (Ariely and Wertenbroch 2002). Lower self-control re<sup>fl</sup>ects a tendency to act with a “here and now” (i.e., immediate) mindset, whereas higher selfcontrol is oriented more toward longer-term goals (Nagin and Pogarsky 2001). Thus, lower self-control leads individuals to react quickly with limited thought given to a decision’s full implications (Hu et al. 2015), again pointing to issues with self-regulation around immediate grati<sup>fi</sup>cation. Hence, we hypothesize the following.

Hypothesis 3. Insiders’ self-control is negatively related to ICA.

A key aspect of middle-range theories is they often consider contingency effects to explain what is happening in a particular context (Hassan and Lowry 2015; Hassan et al. 2019; Park et al. 2017; Tiwana 2009, 2015). This improved explanatory power is due to the possible inclusion of associations that extend beyond simple linear relationships to more fully explain interesting phenomena, such as ICA (Willison and Warkentin 2013, Willison et al. 2018a). A natural contingency that must be considered for theoretical completeness is the attenuating effect of self-control on the relationship between motives and ICA.

Self-control often in<sup>fl</sup>uences how individuals calculate the bene<sup>fi</sup>ts of potential behaviors but may not necessarily motivate individuals to exhibit any speci<sup>fi</sup>c set of behaviors (Gottfredson 2017). For example, higher self-control enables an insider facing a personal affront in the workplace to better resist the urge to retaliate, whereas lower self-control exacerbates the urge (Lian et al. 2014). Individuals with higher self-control who experience vengeful cognition engage in less subsequent organizational deviance than their counterparts with lower self-control (Bordia et al. 2008). Additionally, re search shows that self-control moderates the relationship between perceived bene<sup>fi</sup>ts of personal internet use in the workplace and employees’ compliance with internet use policies at work (Li et al. 2018). Therefore, to better understand how ICA occurs in organizations, it is imperative to examine how self-control in<sup>fl</sup>uences the relationships between individual motives and behaviors in addition to possible direct relationships between selfcontrol and the behaviors of interest. Thus, we hypothesize the following.

Hypothesis 4. (a) Insiders’ self-control attenuates the relationship between financial benefits and ICA, and (b) insiders’ self-control attenuates the relationship between PCV and ICA.

2.2.2. Deterrence Perceptions as a Primary Extrinsic Control Inhibiting Insider Computer Abuse. Whereas self-control can be seen as a primary intrinsic control that inhibits ICA, we turn to DT and its tenets to build our primary extrinsic control that inhibits ICA, thereby completing the MoCo theory. DT, which originated in the criminology literature, explains that individuals weigh the expected bene<sup>fi</sup>ts from their behaviors against potential consequences of them (Bentham 1988, Gottfredson and Hirschi 1990, Gottfredson 2011). From this foundation, organizations (or societies) need only to foster expectations of negative consequences (i.e., sanctions) that outweigh potential bene<sup>fi</sup>ts to deter individuals’ undesirable behaviors. Traditional deterrence relies on perceptions of the certainty, severity, and celerity of sanctions to counteract any perceived bene<sup>fi</sup>ts from engaging in undesirable behavior (Yu 1994, Nagin 1998). Based on utilitarianism (Bentham 1988), the goal of these deterrents (via sanctions) is to make undesirable behavior an irrational choice.

In criminology, the in<sup>fl</sup>uence of deterrents (e.g., sanctions) is said to be twofold: (1) they can “prevent the person being punished from committing another crime” and (2) they can “prevent others who are contemplating crime from committing the act” (Piquero et al. 2011, p. 336). These two deterrent effects are called specific deterrence and general deterrence, respectively (Piquero et al. 2011). Whether general or speci<sup>fi</sup>c, to be successful, a deterrent requires that an action’s perceived costs (i.e., the deterrent) outweigh its perceived bene<sup>fi</sup>ts. However, bene<sup>fi</sup>ts and costs ultimately are not uniformly perceived: “Rewards and costs can come from ourselves, from those around us (friends, parents, teachers, employers, etc.), or from the act itself” (Andrews and Bonta 2010, p 187).

Since early seminal research on effective security (Straub 1990, Straub and Nance 1990), DT has become one of the most in<sup>fl</sup>uential theories in the organizational security literature (D'Arcy and Herath 2011). Online Appendix A identi<sup>fi</sup>es more than 60 articles that explicitly mention both “deterrence theory” and “information security” in the AIS senior scholars’ basket of eight IS journals (e.g., D’Arcy et al. 2009, 2014; Herath and Rao 2009; Guo et al. 2011; Chen et al. 2012; Johnston et al. 2015; Lowry et al. 2015; Johnston et al. 2016; Moody et al. 2018; Willison et al. 2018a, b). Thus, DT and its concepts are not new to the <sup>fi</sup>eld, and we brie<sup>fl</sup>y mention several notable examples in the extant research.

Several organizational security studies have leveraged DT’s components to explain various security phenomena. For example, Chen et al. (2012) examined the role of organizational punishment severity and certainty on employees’ compliance intentions. In the healthcare context, Foth (2016) examined the effects of punishment severity and detection certainty on healthcare workers’ intention to comply with data protection regulations. D’Arcy et al. (2014) included the role of perceived sanctions in their study on individuals’ violation intentions. Similarly, Johnston et al. (2015) and Siponen and Vance (2010) examined the roles of formal and informal sanctions in information security compliance intentions. Interestingly, Sojer et al. (2014) found that punishment severity indirectly in<sup>fl</sup>uenced software developers’ intention to reuse internet accessible code. Given the strong theoretical and empirical support for sanctions as a primary component of organizational deterrence efforts, we extend this work to our ICA context. Thus, we hypothesize the following.

Hypothesis 5. Insiders’ perceptions of organizational sanctions are positively related to their perceptions of organizational deterrence.

Hypothesis 6. Insiders’ perceptions of organizational deterrence are negatively related to their ICA.

Like the contingency effects proposed for our intrinsic control mechanism, deterrence perceptions also likely attenuate the extent to which instrumental and expressive motivations foster ICA. Speci<sup>fi</sup>cally, the presence of deterrents, primarily through sanctions, should reduce the attractiveness of deviant actions to individuals. Although instrumental and expressive motives can drive engagement in ICA, insiders’ perceptions of organizational deterrence will limit the in<sup>fl</sup>uence of their motives on their behavior owing to the greater chance that they will face sanctions if caught. This form of behavioral control has been illustrated in previous research that found sanctions moderate the relationship between organizational injustice and intentions to commit ICA (Willison et al. 2018b). Thus, we hypothesize the following.

Hypothesis 7. (a) Insiders’ perceptions of organizational deterrence attenuate the relationship between perceived financial benefits and ICA, and (b) insiders’ perceptions of organizational deterrence attenuate the relationship between PCV and ICA.

Summarizing this section, Figure 3 depicts our research model used to test the MoCo theory.

## 3. Methodology

To test our hypotheses, we hired a marketing research <sup>fi</sup>rm to collect anonymized data from insiders working in various industries in the United States. Collecting such data online is a widely accepted practice in organizational security research (e.g., Lowry et al. 2013a, 2016b; Posey et al. 2013; Vance et al. 2013), especially as long as key actions are taken to increase data quality (Lowry et al. 2016a, b). Our actions to increase data quality included (1) hiring marketing professionals who prescreened and quali<sup>fi</sup>ed our participants as legitimate full-time employees with knowledge of deterrence efforts and ICA at their <sup>fi</sup>rms, and (2) introducing attention traps and removing data that exhibited anomalies and/or hurried responses. According to the survey provider, 696 individuals initially received our survey, and 532 agreed to provide responses. After excluding incomplete responses and screening for nonconscientious responses (e.g., straight-ticket responding), our <sup>fi</sup>nal sample comprised 361 respondents. This <sup>fi</sup>gure equates to a usable-to-collected response rate of 67.9%, which meets or exceeds the rate of other similar research (e.g., D’Arcy et al. 2014).

Figure 3. Research Model to Operationalize and Test the MoCo Theory  
![](/api/attachments/ZKB3M3MB/fulltext/images/00e7c9b69f7659b6351f20b69ec2b15305d8047ab81c3dd1347c011c554a7082.jpg)

When conducted with careful controls, online panels are especially appropriate for collecting sensitive information from insiders because they provide anonymous, off-site access to the survey. Increasing anonymity, in turn, yields responses that are more candid and less susceptible to method bias (Podsakoff et al. 2003). The average age of surveyed insiders was 45.4 years, with an average organizational tenure of 10.8 years. Additionally, the sample was 49.0% female, with 66.5% of respondents holding at least a bachelor’s degree. Finally, 35.2% of respondents indicated that they have a managerial role in their organization, and13.6% reported working in their organization’s IT department. Our sample includes insiders working in a variety of job roles across numerous industries, including education, <sup>fi</sup>nance and insurance, healthcare, professional services, government, and retail, among others. Online Appendix D provides the full industry breakdown of our sample, and Table 1 summarizes our sample characteristics.

Table 1. Sample Characteristics

<table><tr><td>Characteristic</td><td>Statistic</td></tr><tr><td>Female</td><td>49.0%</td></tr><tr><td>Age</td><td>45.4 (average)</td></tr><tr><td>Organizational tenure</td><td>10.8 (average)</td></tr><tr><td>Education level</td><td>66.5% (at least a bachelor&#x27;s degree)</td></tr><tr><td>Managerial role</td><td>35.2%</td></tr><tr><td>IT role</td><td>13.6%</td></tr><tr><td>Organizational size</td><td></td></tr><tr><td>Very large (10,000+ computers)</td><td>23.0%</td></tr><tr><td>Large (1,000–10,000 computers)</td><td>24.4%</td></tr><tr><td>Medium (100–1,000 computers)</td><td>25.5%</td></tr><tr><td>Small (1–100 computers)</td><td>27.1%</td></tr></table>

## 3.1. Study Measures

As is standard practice, we leveraged previously developed measures whenever possible to operationalize the constructs in our research model. To assess individual differences associated with self-control, we measured trait-like self-control using four items from Tangney et al. (2004). An example of an item measuring selfcontrol is “I often act without thinking through all the alternatives” (reverse-worded item).

We measured PCV using six items from Robinson and Morrison (2000), such as “My employer has broken many of its promises to me even though I have upheld my side of the deal.” We measured insiders perceptions of <sup>fi</sup>nancial bene<sup>fi</sup>ts through ICA with three items adapted from Posey et al. (2015), such as “I could be rewarded <sup>fi</sup>nancially for choosing to abuse my organization’s computer systems.”

Insiders’ perceptions of organizational sanctions were measured with 10 items re<sup>fl</sup>ecting the certainty, severity, and celerity of organizational sanctions for ICA inspired by previous research (D’Arcy et al. 2009, Siponen and Vance 2010, D’Arcy and Herath 2011, Guo et al. 2011). Based on the treatment of these sanction-related percep tions in prior studies (e.g., Bulgurcu et al. 2010, Siponen and Vance 2010, D’Arcy and Herath 2011, Guo et al. 2011, Johnston et al. 2016, Xu et al. 2016), we considered organizational sanctions a higher-order factor comprising certainty, severity, and celerity. For example, Siponen and Vance (2010) and Guo et al. (2011) measured sanctions as a re<sup>fl</sup>ective construct comprising perceptions of both sanction certainty and severity. As DT pri marily discusses these perceptions separately, we chose to maintain these distinct but related subconstructs as part of a higher-order factor rather than collapse them into a single re<sup>fl</sup>ective construct. As methodologists (i.e., Hair et al. 2017) have explained, higher-order speci<sup>fi</sup>cations such as these are appropriate when a common factor explains correlations among the lower-order factors.

Items used to measure the deterrence constructs were based on prior studies on organizational deterrence (D’Arcy et al. 2009, Siponen and Vance 2010, D’Arcy and Herath 2011). An example of an item on certainty of sanction is “My organization will discipline those whom it believes are guilty of information security violations on its computer system.” An item measuring celerity of sanction is “My organization would immediately punish employees who commit information security violations on the computer system,” and an item measuring severity of sanction is “It is likely that the punishment given by my organization to employees who commit information security violations on the computer system would be severe.” We measured individuals’ perceptions of organizational deterrence from ICA with three items based on D’Arcy and Herath (2011), such as “My organization deters its employees from committing information security violations.” Finally, we used 12 items from Posey et al. (2011) to measure ICA, such as “I have purposely abused our organization’s computer systems.” The full set of items is included in Online Appendix B.

Table 2. Measurement Model Statistics

<table><tr><td>Latent constructs</td><td>ICA</td><td>PCV</td><td>FB</td><td>SC</td><td>OD</td><td>OS</td><td>CR</td><td>HTMT</td></tr><tr><td>Insider computer abuse</td><td>0.91</td><td></td><td></td><td></td><td></td><td></td><td>0.98</td><td>0.24</td></tr><tr><td>Psychological contract violation</td><td>0.37</td><td>0.91</td><td></td><td></td><td></td><td></td><td>0.96</td><td>0.18</td></tr><tr><td>Financial benefit (FB)</td><td>0.40</td><td>0.24</td><td>0.93</td><td></td><td></td><td></td><td>0.95</td><td>0.16</td></tr><tr><td>Self-control (SC)</td><td>-0.41</td><td>-0.35</td><td>-0.19</td><td>0.72</td><td></td><td></td><td>0.87</td><td>0.20</td></tr><tr><td>Organizational deterrence (OD)</td><td>-0.26</td><td>-0.28</td><td>-0.15</td><td>0.17</td><td>0.84</td><td></td><td>0.91</td><td>0.35</td></tr><tr><td>Organizational sanction (OS)</td><td>-0.15</td><td>-0.15</td><td>-0.07</td><td>0.10</td><td>0.79</td><td>0.86</td><td>0.97</td><td>0.33</td></tr></table>

Note. The square roots of AVEs are in bold. HTMT, Average heterotrait–monotrait ratio.

## 4. Analysis and Results

The research model was analyzed in a two-step procedure as recommended by methodologists (Gerbing and Anderson 1988). We used the partial least squares (PLS) structural equation modeling platform SmartPLS 3.2.8 (Ringle et al. 2015). PLS is appropriate for studies that examine complex relationships (Fornell and Bookstein 1982) that are exploratory or models in development that are not yet fully established in the literature (Henseler et al. 2014, Lowry and Gaskin 2014), thereby placing a premium on predictive validity (Hair et al. 2017).

## 4.1. Construct Validity

In the <sup>fi</sup>rst step, we examined the construct validity of the measures to be included in the structural model. First, we assessed the presence of collinearity by examining the predictor constructs’ variance in<sup>fl</sup>ation factors (VIFs) in the model. As the VIF values ranged from 0.289 to 1.974, none were above the conservative 3.3 level (Petter et al. 2007). Second, each construct’s composite reliabilities (CRs) were within the recommendations of prior research (Nunnally 1978). Additionally, each average variance extracted (AVE) was well above the recommended 0.50 level. Third, each pair of constructs met the Fornell and Larcker (1981) criterion, as indicated by a ratio of the square root of AVE to correlations. Fourth, the heterotrait–monotrait ratio between all constructs, except for the subdimensions of the higher-order sanctions construct, was below the recommended 0.90 value, averaging between 0.16 and 0.35 for each construct (Henseler et al. 2015). Finally, the standardized root mean square residual (SRMR) and root mean square residual covariance $\left( \mathrm { R M S } _ { \mathrm { t h e t a } } \right)$ <sup>fi</sup>t statistics indicated that the model has good <sup>fi</sup>t $( \mathrm { S R M R } = 0 . 0 6 1 , \mathrm { R M S _ { t h e t a } } = 0 . 1 1 9 ;$ ; Hu and Bentler 1999, Henseler et al. 2014). Table 2 shows the measurement model statistics. The full correlation table is in Online Appendix C.

For the higher-order organizational sanctions construct, we assessed the hierarchical component model as recommended by leading methodologists (Wetzels et al. 2009, Hair et al. 2017). Hair et al. (2017) speci<sup>fi</sup>ed two requirements of hierarchical component models: (1) the number of indicators should be similar across lower-order constructs, and (2) the re<sup>fl</sup>ective measurement model criteria (e.g., AVEs, CR) should be met at each level of the model—with the important exception that discriminant validity between the higher- and lower-order constructs, as well as between the lowerorder constructs in re<sup>fl</sup>ective hierarchical component models, need not be established (Hair et al. 2017).

We met the <sup>fi</sup>rst criterion with three to four indicators among the three subconstructs. The AVEs of lower-order components were above the 0.50 threshold and composite reliabilities were above the 0.70 cutoff point (Hair et al. 2017), indicating strong internal (convergent) reliability and validity. The crossloadings’ pattern supports the higher-order factor with the highest items’ loadings on the associated lower-order construct and relatively lower crossloadings on each other lower-order construct (average factor loading, 0.910; average cross loading, 0.764). Table 3 depicts the cross-loadings.

We note that our decision to model sanctions as a higher-order re<sup>fl</sup>ective construct is supported by prior research. For example, because of their positive interrelationships, many previous studies collapsed deterrence dimensions into a single construct (e.g., Bulgurcu et al. 2010, Siponen and Vance 2010, Guo et al. 2011, Johnston et al. 2016, Xu et al. 2016). Speci<sup>fi</sup>cally, Guo et al. (2011) measured perceived sanctions as a single re<sup>fl</sup>ective measure with separate items for severity, celerity, and certainty loading onto the same construct (loadings ranged from 0.77 to 0.93). Additionally, previous researchers found relatively high correlations and cross-loadings among deterrence-related constructs when including them separately in a research model. For instance, Siponen and Vance (2010) found that formal and informal sanctions were highly correlated (r <sub>-</sub> 0.76) and shared cross-loadings with a range of 0.61–0.75.

Table 3. Organizational Sanction Statistics

<table><tr><td>Item/label</td><td>Celerity</td><td>Certainty</td><td>Severity</td></tr><tr><td>AVE</td><td>0.735</td><td>0.873</td><td>0.880</td></tr><tr><td>CR</td><td>0.917</td><td>0.954</td><td>0.956</td></tr><tr><td>Celerity1</td><td>0.856</td><td>0.634</td><td>0.689</td></tr><tr><td>Celerity2</td><td>0.871</td><td>0.800</td><td>0.801</td></tr><tr><td>Celerity3</td><td>0.815</td><td>0.575</td><td>0.595</td></tr><tr><td>Celerity4</td><td>0.885</td><td>0.740</td><td>0.745</td></tr><tr><td>Certainty1</td><td>0.729</td><td>0.915</td><td>0.834</td></tr><tr><td>Certainty2</td><td>0.767</td><td>0.943</td><td>0.851</td></tr><tr><td>Certainty3</td><td>0.771</td><td>0.944</td><td>0.864</td></tr><tr><td>Severity1</td><td>0.726</td><td>0.793</td><td>0.917</td></tr><tr><td>Severity2</td><td>0.794</td><td>0.853</td><td>0.950</td></tr><tr><td>Severity3</td><td>0.814</td><td>0.909</td><td>0.947</td></tr></table>

## 4.2. Structural Model

We assessed the hypothesized relationships in the research model via SmartPLS 3.0 with 5,000 bootstrapped subsamples. To establish robustness, we included several controls in the assessment: age, gender, organizational tenure, and whether the insider had an IT/IS or a managerial position. Because some insiders might consider engaging in some forms of ICA a moral issue (D’Arcy et al. 2009, Myyry et al. 2009), we included a control for moral identity (Aquino and Reed 2002). As noted, moral identity can be regarded as a “self-regulatory mechanism that motivates moral action” (Aquino and Reed 2002, p. 1423). Finally, ICA actively works against the organization’s interests, thereby contradicting any SETA initiatives the organization employs. We also included a control for SETA awareness (D’Arcy et al. 2009). Both Table 4 and Figure 4 display the results of our structural assessment.

Our second-order perceived sanctions construct explained 62.7% of the variance in deterrence perceptions. The model also explained 46.2% of insiders’ self-reported ICA. All hypotheses except for Hypotheses 6 and 7(b) were supported. The relationship between our instrumental motive (i.e., <sup>fi</sup>nancial bene<sup>fi</sup>ts) and ICA was attenuated by our extrinsic inhibiting control (i.e., organizational deterrence; $\beta = - 0 . 1 5 5 , p = 0 . 0 0 1 )$ , but the relationship between our expressive motive (i.e., PCV) and ICA was not $( \beta = - 0 . 0 \hat { 4 } 0 )$ . However, our intrinsic inhibiting control of self-control was found to moderate, signi<sup>fi</sup>cantly and negatively, the relationship between both instrumental $( \beta ^ { \prime } = - 0 . 1 3 5 , p = 0 . 0 5 )$ and expressive $( \beta = - 0 . 1 4 1 , p = 0 . 0 1 )$ motives and ICA.

In addition to the model’s hypothesized relationships, we examined the effect sizes of our two inhibiting controls. Thus, we reran the model twice: once with self-control, PCV, and <sup>fi</sup>nancial bene<sup>fi</sup>ts (excluding organizational deterrence) and once with organizational deterrence, PCV, and <sup>fi</sup>nancial bene<sup>fi</sup>ts (excluding selfcontrol). Then we compared the results to the full model. Next, we calculated the two models’ effect sizes $( f ^ { 2 } )$ , such that $f ^ { 2 } = ( R _ { \mathrm { \ i n c l u d e d } } ^ { 2 } - R _ { \mathrm { \ e x c l u d e d } } ^ { 2 } ) / ( 1 - R ^ { 2 }$ <sub>included</sub>; Hair et al. 2017). The effect of adding intrinsic selfcontrol to the model was 0.195, a medium-size effect, whereas the effect of adding extrinsic deterrence to the model was 0.048, a small effect. Owing to the small effect size of deterrence, we also examined our analyses statistical power to ensure ample power to detect organizational deterrence’s in<sup>fl</sup>uence in a model including self-control. Our analysis supports our ability to detect a signi<sup>fi</sup>cant in<sup>fl</sup>uence from organizational deterrence, should one exist $( { \mathrm { i . e . , } } f ^ { 2 } = 0 . 0 4 8 , \alpha = 0 . 0 5 , { \mathrm { p o w e r } } = 0 . 9 4 8 ;$ Cohen 1988, Soper 2019).

Table 4. Structural Model Testing Results

<table><tr><td>Relationship</td><td> $\beta$ </td><td>t-statistic.</td><td>Bias-corrected CI</td></tr><tr><td>Hypothesis 1. Financial benefits  $\rightarrow$  ICA</td><td>0.232***</td><td>4.972</td><td>[0.143, 0.329]</td></tr><tr><td>Hypothesis 2. PCV  $\rightarrow$  ICA</td><td>0.124**</td><td>2.642</td><td>[0.028, 0.211]</td></tr><tr><td>Hypothesis 3. Self-control  $\rightarrow$  ICA</td><td>-0.118*</td><td>2.450</td><td>[-0.193, -0.013]</td></tr><tr><td>Hypothesis 4(a). Self-control  $\times$  Financial benefits  $\rightarrow$  ICA</td><td>-0.135*</td><td>2.485</td><td>[-0.251, -0.029]</td></tr><tr><td>Hypothesis 4(b). Self-control  $\times$  PCV  $\rightarrow$  ICA</td><td>-0.141**</td><td>2.702</td><td>[-0.244, -0.053]</td></tr><tr><td>Hypothesis 5. Organizational sanctions  $\rightarrow$  Organizational deterrence</td><td>0.794***</td><td>31.780</td><td>[0.735, 0.834]</td></tr><tr><td>Hypothesis 6. Organizational deterrence  $\rightarrow$  ICA</td><td>-0.079(n/s)</td><td>1.778</td><td>[-0.177, 0.005]</td></tr><tr><td>Hypothesis 7(a). Organizational deterrence  $\times$  Financial benefits  $\rightarrow$  ICA</td><td>-0.155***</td><td>3.626</td><td>[-0.235, -0.070]</td></tr><tr><td>Hypothesis 7(b). Organizational deterrence  $\times$  PCV  $\rightarrow$  ICA</td><td>-0.040(n/s)</td><td>1.011</td><td>[-0.110, 0.038]</td></tr><tr><td>Controls</td><td></td><td></td><td></td></tr><tr><td>Moral identity</td><td>-0.166**</td><td>3.105</td><td>[-0.269, -0.060]</td></tr><tr><td>SETA awareness</td><td>-0.030 (n/s)</td><td>0.483</td><td>[-0.106, 0.083]</td></tr><tr><td>IT position</td><td>0.038 (n/s)</td><td>0.916</td><td>[-0.042, 0.113]</td></tr><tr><td>Management position</td><td>0.037 (n/s)</td><td>0.875</td><td>[-0.047, 0.113]</td></tr><tr><td>Age</td><td>-0.087 (n/s)</td><td>1.740</td><td>[-0.175, 0.015]</td></tr><tr><td>Tenure</td><td>-0.037 (n/s)</td><td>0.985</td><td>[-0.115, 0.036]</td></tr><tr><td>Gender</td><td>-0.004 (n/s)</td><td>0.123</td><td>[-0.085, 0.074]</td></tr></table>

Notes. Bias-corrected con<sup>fi</sup>dence intervals (CIs) are 2.5%–97.5%. Interaction terms were standardized prior to calculation, and calculated using 5,000 subsamples. As recommended by methodologists (Henseler and Chin 2010, Hair et al. 2017), we used the two-stage approach to develop the interaction terms. Online Appendix E provides additional discussion and support for the moderation analyses. n/s, Not signi<sup>fi</sup>cant. $^ { * } p = 0 . 0 5 ; ^ { * * } p = 0 . 0 1 ; ^ { * * * } p = 0 . \dot { 0 } \dot { 0 } 1 .$

Figure 4. Visual Depiction of Structural Model Results  
![](/api/attachments/ZKB3M3MB/fulltext/images/8b909a6b6ab7e7e59ccea3a7316e171f8c81f58d273acd773648cc603f25d7f3.jpg)

We also examined organizational sanctions’ in<sup>fl</sup>uence on insiders’ perceptions of organizational deterrence. Again, DT postulates that perceptions of organizational sanctions drive perceptions of deterrence. Our results indicate that sanctions as a higher-order construct accounted for a signi<sup>fi</sup>cant portion of insiders’ perceptions of organizational deterrence, explaining 62.7% of its variance. However, organizational deterrence was not signi<sup>fi</sup>cantly related to ICA when self-control was included in the model, and deterrence exhibited a smaller effect than self-control in the model $( f _ { \mathrm { \ s e l f - c o n t r o l } } ^ { 2 } = 0 . 1 9 5 ;$ $f _ { \mathrm { \ o r g . \ d e t . } } ^ { 2 } = 0 . 0 4 8 )$

Finally, we included various controls, both demographic (i.e., gender, age, organizational tenure, and position) and substantive (i.e., SETA perceptions and moral identity). Of these controls, only moral identity was signi<sup>fi</sup>cantly related to ICA. As noted, moral identity is a mechanism of self-regulation (Aquino and Reed 2002). Thus, it is not surprising that moral identity was negatively related to ICA. However, moral identity and self-control are far from interchangeable and shared only 9% of their variance (r 0.30).

## 4.3. Post Hoc Analyses of Interaction Effects

To examine the hypothesized interaction effects, we plotted the simple slopes in Figures 5–8. As shown in Figures 5 and 6, insiders with relatively high self-control exhibited lower levels of ICA than their counterparts with low self-control when perceptions of <sup>fi</sup>nancial bene<sup>fi</sup>ts and contract violations were relatively high. There was little difference in ICA levels between individuals with low and high self-control when <sup>fi</sup>nancial bene<sup>fi</sup>ts and PCV were relatively low. Insiders who perceived relatively high organizational deterrence also exhibited lower levels of ICA when perceptions of <sup>fi</sup>nancial bene-<sup>fi</sup>ts were relatively high compared with those who perceived lower organizational deterrence (see Figure 7). However, as indicated by the nonsigni<sup>fi</sup>cant interaction effect, differences in perceptions of organizational deterrence did not appear to in<sup>fl</sup>uence the overall positive relationship between PCV and ICA (see Figure 8).

Figure 5. (Color online) Interaction of Self-Control and Financial Bene<sup>fi</sup>ts on ICA  
![](/api/attachments/ZKB3M3MB/fulltext/images/2b0850dd5897c51e7801fc4f8aa02b743087125f19ec360e3d657173f3b5cd61.jpg)  
— — Self-control at -1 SD  Self-control at Mean —  - Self-control at +1 SD

Figure 6. (Color online) Interaction of Self-Control and Psychological Contract Violation on ICA  
![](/api/attachments/ZKB3M3MB/fulltext/images/8db1bc80939a65a1a376fc9bf278c7633b86982639a74b0851eb2f9c78c8cbdf.jpg)  
— — Self-control at -1 SD  Self-control at Mean —  - Self-control at +1 SD

## 4.4. Common Method Variance

To ensure that our data did not suffer from harmful common method variance (CMV), we performed two analyses recommended by Schwarz et al. (2017): an unmeasured latent variable (UMLV) analysis (Liang et al. 2007) and a measured latent marker variable (MLMV) analysis (Chin et al. 2013). According to our UMLV assessment, the AVE by our substantive items was 77.8% and the AVE by the method’s unmeasured latent variable (i.e., method-based variance) was only 0.4%. Additionally, our MLMV assessment found little evidence of harmful CMV, with an average difference, in terms of beta weights, between the baseline CMV model and the MLMV model of 0.004. Therefore, our sample did not suffer from harmful CMV (Podsakoff et al. 2003, Schwarz et al. 2017). The full results from both CMV analyses are included in Online Appendix F.

Figure 7. (Color online) Interaction of Organizational Deterrence and Financial Bene<sup>fi</sup>ts on ICA  
![](/api/attachments/ZKB3M3MB/fulltext/images/e8520c03e19deb39247f60146cdbc7de1a361038d17165ee174e6489464faaba.jpg)

Figure 8. (Color online) Interaction of Organizational Deterrence and Psychological Contract Violation on ICA  
![](/api/attachments/ZKB3M3MB/fulltext/images/92b08d96785ce216370ce54530ebc448f22c97820e387ca2bbbd250b442d8c44.jpg)  
—Organizational Organizational - . - Organizational Deterrence at -1 SD Deterrence at Mean Deterrence at +1SD

## 5. Discussion and Contributions

As our MoCo theory proposes and our results con-<sup>fi</sup>rm, tensions exist between controls and insiders motives to commit ICA. This <sup>fi</sup>nding helps answer calls to challenge the extant organizational security focus in DT (e.g., Crossler et al. 2013; Willison and Warkentin 2013; Lowry et al. 2017a; Willison et al. 2018a, b) via more expansive approaches to information security theorizing (Moody et al. 2018, Dey et al. 2021). Interestingly, despite much of the discipline’s theoretical and rhetorical framing around DT (e.g., Straub 1990, D’Arcy et al. 2009, Johnston and Warkentin 2010, Johnston et al. 2015), we <sup>fi</sup>nd that, compared with intrinsic controls, organizational deterrence serves a much more limited role in thwarting ICA. Speci<sup>fi</sup>cally, we <sup>fi</sup>nd that organizational deterrence attenuates only one set of motives—instrumental motives.

This discovery represents a signi<sup>fi</sup>cant departure from the traditional view of IS security in DT-based research, which overlooks motivations. For example, D’Arcy et al. (2009) conducted a DT-based study of employees’ misuse of organizational IS resources that did not consider any motivations to perform the behavior itself—only external controls aimed at deterring it (i.e., organizational security-related sanctions, policies, programs, and monitoring). Siponen and Vance (2010) included DT-based sanctions in their study of security policy violations, but rather than study insiders’ motives, they investigated the role of neutralization (e.g., rationalization) strategies on the deterring effect of sanctions. Moody et al. (2018) found that organizational deterrents (i.e., punishments) did not explain policy violations and subsequently removed them from their proposed unified model of information security policy compliance (UMISPC). However, they did not examine the moderating effects of such punishments on instrumental motives.

By contrast, our research includes two major forms of employee motives and demonstrates that internal controls show broader applicability to ICA with direct and moderating effects; namely, insiders’ self-control reduced ICA in three ways: it negatively in<sup>fl</sup>uenced ICA directly and it weakened the in<sup>fl</sup>uence of both instrumental and expressive motives. Thus, our initial test of the MoCo theory suggests that self-control was the single most important factor for inhibiting ICA. In addition, effect size calculations indicate that the ability of extrinsic controls (i.e., organizational deterrence) to curb negative insider behavior $( f ^ { 2 } = 0 . 0 4 8 )$ is overshadowed by employees’ self-regulatory abilities (i.e., selfcontrol; $\dot { f } ^ { 2 } = \hat { 0 } . 1 \dot { 9 } 5 )$ . However, we do not wish to imply that organizational deterrence does not serve a role in thwarting ICA. Although deterrence did not signi<sup>fi</sup>- cantly attenuate the relationship between expressive motives and ICA, it did diminish the relationship between instrumental motives and ICA. It is thus likely that employees who view ICA as a means to attain some other goal (e.g., <sup>fi</sup>nancial gain) can be dissuaded to some degree through sanctions that drive deterrence perceptions. Unfortunately, deterrence appears to do little to halt ICA if an insider’s actions represent the end goal (e.g., to vent frustration).

We believe this <sup>fi</sup>nding re<sup>fl</sup>ects a fundamental difference between instrumental and expressive motives. Instrumental motives, which relate to extrinsic tangible outcomes (Barbuto 2005), are externally focused and in<sup>fl</sup>uenced by extrinsic controls (e.g., organizational deterrence). Alternatively, expressive motives are intrinsic in nature and re<sup>fl</sup>ect a desire to express oneself (Robinson and Bennett 1997). Therefore, extrinsic inhibiting controls, such as organizational deterrence, are unlikely to be effective at limiting the effects of expressive motivators, like PCV on ICA. This insight is crucial for organizational leaders as they seek to minimize ICA, and it indicates that insiders’ instrumental and expressive intentions are derived from distinct motives and must be managed differently. As criminologists have opined (e.g., Gottfredson and Hirschi 1990, Gottfredson 2017) and as has been theorized by ICA scholars (Willison and Lowry 2018, Willison et al. 2018a), one possibility is that although the genera idea of sanctions and overall deterrence is rational, many decisions are governed by bounded rationality, and pure rationality alone rarely explains why people act. Thus, it is rare for research to fully explain how to prevent negative behaviors like ICA through rational sanctions. This especially seems to be the case when considering ICA behavior with expressive motives.

## 5.1. Implications

Our MoCo theory of ICA provides unique and refreshing insight into a phenomenon that was introduced to our discipline more than three decades ago. This insight is possible because our theory pits two major types of motives that positively relate to ICA against two major types of controls that serve to attenuate the in<sup>fl</sup>uence of those motives. Although recent researchers have called for broader, more comprehensive approaches (e.g., Dey et al. 2021), we are not aware of research that examines ICA in this way. Consequently, our theory complements existing research and has major implications for future IS security research.

The <sup>fi</sup>rst major implication of our study is that IS security researchers should simultaneously account for the distinctions and interdependencies among insiders’ motives and controls, as explained by the MoCo theory, rather than studying these factors independently. Our results indicate that controls must be calibrated against the motives being managed for the controls to be ef<sup>fi</sup>cacious. Without considering these factors together, researchers will miss the true theoretical linkages among motives and controls—and, ultimately, behaviors. Thus, a major contribution of our study is that it demonstrates that controls attenuate the in<sup>fl</sup>uence of motives. Put another way, our research indicates that although controls can in<sup>fl</sup>uence behavior directly, they also function as regulation mechanisms for motives. However, when studied in isolation, such controls may appear to serve a motivational rather than a regulatory role.

To further underscore this matter, we found that self-control negatively in<sup>fl</sup>uences ICA directly and simultaneously moderates the in<sup>fl</sup>uence of instrumental (e.g., <sup>fi</sup>nancial bene<sup>fi</sup>ts) and expressive (e.g., PCV) motives for ICA. Conversely, deterrence only diminishes the in<sup>fl</sup>uence of perceived <sup>fi</sup>nancial bene<sup>fi</sup>ts on ICA. Thus, in the context of ICA, organizational deterrents (e.g., sanctions) themselves do not create new motives for ICA, but rather they weaken some already existing motives (e.g., <sup>fi</sup>nancial bene<sup>fi</sup>ts). As a counterexample, when an insider is not motivated to commit ICA, the insider likely does not consider the threat of sanction for actions they have no intention to commit. We believe this helps explain why prior researchers found very weak evidence for the in<sup>fl</sup>uence of deterrents on positive behaviors (e.g., compliance intentions; D’Arcy and Herath 2011). When an insider has compelling motives to comply with policy, the existence of a sanction for not complying likely has a limited in<sup>fl</sup>uence on their compliance intention. This may appear to be a subtle distinction, but it has powerfu implications for researchers and practitioners and may help explain the disparate <sup>fi</sup>ndings of prior DT research (see D’Arcy and Herath 2011).

The second major implication of our research derives from its contribution as a middle-range, theoretical framework for organizational and behavioral ICA research. Recently, Moody et al. (2018) and Dey et al. (2021) explained the need for more expansive theories in IS security. As Moody et al. (2018, p. 286) noted, “many of competing theories in IS [security] are often tested in isolation rather than in comparison with each other.” We largely agree with these sentiments but add that middle range theories, such as the MoCo theory, are often better viewed as complementary rather than competitive. To this end, and to illustrate the breadth and depth of our implications, we next explain the implications of the MoCo theory in comparison with these other recent works (i.e., Moody et al. 2018, Dey et al. 2021).

The implications of our MoCo theory are distinct, yet complement those of Moody et al. (2018) in several important ways. For instance, we provide a middlerange theory for ICA, whereas their study explains policy compliance by way of two distinct dependent variables: (1) intention to share a computer password and (2) reactance, which they de<sup>fi</sup>ne as “denying the possible [IS security] problem” (Moody et al. 2018, p. 305). Thus, our theory has novel implications for deliberate ICA that their study does not address, especially because these phenomena are only tangentially related. For example, to the extent that they studied positive motivations to violate policy (i.e., share a password), they studied them in the forms of habit and role values. Upon inspection, these are wholly unrelated to ICA. Habit re<sup>fl</sup>ects the fact that compliance is something an insider does “without thinking,” and role values indicate that the compliant or noncompliant behavior is “compatible with his/her work” (Moody et al. 2018, pp. A3–A4). The motives in the UMISPC are incompatible with ICA, which is deliberate, nonhabitual behavior. Also, as abusive behavior, ICA works against an organization’s interests and is incompatible with formal work roles. Moody et al. (2018) studied only the direct effect of deterrence (i.e., punishments) on intentions. When they found no signi<sup>fi</sup>cant direct relationship, they subsequently dropped deterrence from the UMISPC. As our results show, despite a nonsigni<sup>fi</sup>cant direct relationship, deterrence may moderate insiders’ instrumental motives for security-related behaviors. This clari<sup>fi</sup>cation further exempli<sup>fi</sup>es the complementary nature of our works.

Our also work uniquely complements Dey et al.’s (2021) recent <sup>fi</sup>ndings that shed light on important security-related tensions—those of organizational security education and enforcement. However, the tension between education and enforcement is distinct from the tension between motives and controls. In fact, one of the contextual factors at play in the study by Dey et al. (2021, p. 14) is organizational budgetary constraints, as they note:

Our work also sheds light on an organization’s planning and budgeting for IT security. As discussed earlier, most organizations operate within a fixed budget allocated to anticircumvention measures. A major shortcoming of a fixed budget is that investing more in one countermeasure can come only at the expense of cutting the other, which introduces an artificial substitutability where none exists.

Thus, one of the contributions of their microeconomic model is to help organizations with budget allocation across organizational countermeasures (or controls). In contrast, the MoCo theory of ICA sheds light on a distinct set of tensions: instrumental and expressive motives versus internal and external controls. Rather than being focused on states of circumvention across an organization, we are focused on the behavior of individuals, making these two works complementary. The microeconomic model of Dey et al. (2021) says nothing about any individual’s circumvention behavior, but rather generalizes to the level of circumvention prevalence across a <sup>fi</sup>rm (described as “states”). Conversely, our work does not describe or explain the state of ICA across a <sup>fi</sup>rm (i.e., a <sup>fi</sup>rm-level conceptual perspective), but rather explains ICA decisions of individual insiders.

Finally, the third major implication of our research is that practitioners can now call upon a much broader array of human resource management (HRM) practices to reduce ICA than indicated in prior research. Drawing on the rich history of research on the foundations of PCV, our study suggests that HRM practices that foster interpersonal relationships between supervisors and subordinates, increase congruency in perceived employer–employee obligations and values, and reduce sensitivity to perceived psychological contract breaches should effectively reduce PCVs, thereby reducing occurrences of ICA (Morrison and Robinson 1997). For example, using realistic job previews, providing more truthful and accurate prehire information (e.g., accurate recruiting videos and recruiter information sharing), and ensuring greater levels of interaction between the candidate and organization agents should result in a greater degree of congruence between candidate and employer schemata of the employment relationship (i.e., obligations, promises; Morrison and Robinson 1997, Robinson and Morrison 2000). Greater congruence between schemata decreases the likelihood of breaches occurring, thereby lessening the possibility of PCV. Furthermore, because the <sup>fi</sup>rst year of employment is when employees tend to realize that their prehire schemata of shared obligations are inaccurate, organizations can utilize intense formalized socialization processes that not only validate company values/beliefs proffered prehire but also transfer prehire promises to organization agents to operationalize (Robinson and Morrison 2000, Sutton and Grif<sup>fi</sup>n 2004).

In addition, it is important to acknowledge that psychological contracts can evolve over time. Accordingly, HRM practices can also be used to reduce the likelihood that changes in psychological contracts will lead to perceived contract violations (Morrison and Robinson 1997), thereby reducing the potential for ICA. These practices include hiring people with low levels of equity sensitivity and negative affect (Morrison and Robinson 1997, Kunze and Gower 2012), training leaders in procedural/interactional justice (Tekleab et al. 2005), placement for supervisor–subordinate <sup>fi</sup>t (Tekleab et al. 2005), and providing opportunities for participation in decision making (Rousseau 2004).

More important are the practical implications for using HRM practices to reduce ICA by increasing an organization’s stock of self-control capital. A clear takeaway from our research is that self-control is vital in moderating the in<sup>fl</sup>uence of both instrumental and expressive motives to commit ICA. Although organizational leadership cannot always prevent such insider motives from forming across their workforce, it is essential to maintain personnel with adequate selfcontrol to diminish the impact of such harmful motives should they arise. This is especially true for insiders in positions with increased opportunity to commit ICA. As such, perhaps the most obvious way to reduce ICA is to use trait measures of self-control as a screening tool in the selection process. Additionally, insiders self-control levels can be used to help determine whether an employee is a good <sup>fi</sup>t for a job where there is substantial potential for ICA. In short, companies that wish to reduce the occurrence of ICA have a wide variety of HRM practices at their disposal to solve the problem beyond the methods discussed in deterrencerelated models.

## 5.2. Limitations and Future Research

Inherent limitations exist in self-reported security research, although using online panels to collect data is accepted widely in security research (Boss et al. 2009; Johnston and Warkentin 2010; Posey et al. 2013; Lowry et al. 2016a, b; Burns et al. 2018). To minimize limitations in self-reporting, this study provided offsite surveys to insiders, thereby increasing their sense of anonymity, encouraging candid responses (Kays et al. 2012), and reducing response bias (Podsakoff et al. 2003). We also performed a formal test for CMV and found little evidence to indicate that harmfu CMV biased our results. Although this is an important <sup>fi</sup>rst step, ICA can take many individual forms, and future research should shed light on potential differences among individual ICA behaviors.

Our results present several other opportunities for future research. First, researchers should examine a broader set of factors that create instrumental and expressive motives to commit ICA. Such future studies will not only uncover new ground for ICA research but further re<sup>fi</sup>ne our emergent theory. Additionally, future research should examine how such instrumental and expressive motives develop over time. For example, our study indicates that insiders sometimes believe they could bene<sup>fi</sup>t <sup>fi</sup>nancially for abusing their organizations’ systems, and this perception can in<sup>fl</sup>uence their ICA; however, future research is needed to uncover the speci<sup>fi</sup>c situations or positions that create these opportunistic incentives.

Second, we found that PCV in<sup>fl</sup>uences ICA directly. As an expressive motivator, perceived contract violations can lead to acts of organizational sabotage, such as ICA. However, further research is needed to examine exactly how these perceptions emerge within insiders causally, particularly for situations in which contract violations lead to ICA. For example, future research can examine whether insiders’ positions within the organization play a role in their ICA as a reaction to PCV. This could be a fruitful avenue for future investigations because some positions may provide more opportunities to commit ICA than others. Understanding this causally will likely require the collection of longitudinal data. Furthermore, the potential for HRM practices to reduce ICA by diminishing PCV suggests a need for research aimed at better understanding expressive motives for ICA to determine how to reduce ICA’s occurrence. Such research should also explore contextual boundary conditions (e.g., a turbulent versus stable work environment) for when these HRM practices are and are not effective in reducing PCV and ICA.

Third, less than two-thirds of the variance in organizational deterrence was explained by insiders’ perceptions of organizational sanctions. Given DT’s prominence in driving organizational security programs and security research, future studies might examine what factors other than the certainty, severity, and celerity of sanctions in<sup>fl</sup>uence insiders’ perceptions of organizational deterrence. However, given the limited in<sup>fl</sup>uence of deterrence in our research model, future studies based solely on DT are ill advised, as suggested in extant literature (see Willison and Warkentin 2013, Willison et al. 2018a).

Finally, given the direct and moderating in<sup>fl</sup>uence of self-control on insiders’ ICA, further research is needed to better understand the role of self-control in regulating security-related behavior. In the workplace, this is especially important for insiders entrusted with access to valuable organizational information assets because their self-control plays a key role in reducing ICA intentions. Although we used a broad and relatively stable trait measure of self-control in our study, self-control has also been conceptualized as a <sup>fi</sup>nite resource that can be depleted by overwork or other demanding situations (Hagger et al. 2010, Gino et al. 2011), and scholars have shown that self-control resources can <sup>fl</sup>uctuate during the workday (Johnson et al. 2018). Future research should thus examine the role other conceptualizations of self-control play in ICA, such as state self-control, self-control effort, and self-control motivation (see Wehrt et al. 2020). It is also possible that there are situations in which a high level of self-control is required to commit ICA, such as with sophisticated multistage attacks (e.g., a situation in which an insider must perform detailed reconnaissance and wait patiently to strike at the opportune time). Future research should also examine whethe there are speci<sup>fi</sup>c contextual factors that lead to a positive relationship between self-control and ICA.

## 6. Conclusion

We extended the deterrence perspective in a new middle-range theory of ICA, termed the motive-control theory of ICA, that emphasizes both instrumental (e.g., <sup>fi</sup>nancial bene<sup>fi</sup>ts) and expressive (e.g., PCV) motives for ICA as well as intrinsic and extrinsic inhibiting controls— insiders’ self-control and perceptions or organizational deterrence, respectively—on ICA. Our results indicate that motives driven by insiders’ perceptions of <sup>fi</sup>nancial bene<sup>fi</sup>ts and PCV are strongly related to their ICA. Insiders’ self-control signi<sup>fi</sup>cantly moderates the relationship between certain instrumental and expressive motives. Finally, we found that deterrence moderates the relationship between <sup>fi</sup>nancial bene<sup>fi</sup>ts and ICA only, thereby failing to exhibit a signi<sup>fi</sup>cant direct relationship with ICA or a signi<sup>fi</sup>cant moderating relationship on the path between expressive motives and ICA.

Our study thus demonstrates that both instrumental and expressive motivations engender ICA within organizations and that intrinsic inhibiting controls, such as self-control, exhibit signi<sup>fi</sup>cant direct and moderating in<sup>fl</sup>uences in the model. Conversely, and despite their continued utilization in the <sup>fi</sup>eld, deterrence perceptions attenuated the in<sup>fl</sup>uence of outward-focused motives for ICA only, leaving the in<sup>fl</sup>uence of inward, expressive motives for ICA unaltered. Our study offers a greater theoretical and empirical understanding of the relationship between self-control and instrumental and expressive motivators while providing insights for when deterrence perceptions do and do not help minimize ICA.

## Endnotes

<sup>1</sup> See https://enterprise.verizon.com/resources/reports/2019-databreach-investigations-report.pdf.

<sup>2</sup> See https://www.fbi.gov/news/stories/two-guilty-in-theft-of-trade -secrets-from-ge-072920.

An example of an instrumental motive is when someone steals property or information to sell it for cash (Ambrose et al. 2002). Notably, instrumental motives can lead to various forms of ICA. For example, insiders acting out of instrumental motives might abuse their IT privileges for the chance to receive financial benefits, such as greater bonuses or higher commissions.

An example of an expressive motive is when someone steals property or information to destroy it to express dissatisfaction with something in the workplace (Ambrose et al. 2002). Again, expressive motives can result in various harmful behaviors, such as intentionally bending or breaking computer-related rules or policies. These can include but are not limited to revenge against a coworker, getting back at a boss for a mediocre performance evaluation, and so forth.

5 Other researchers have further constrained insiders’ computer abuse to also be malicious or harmful (Willison and Warkentin 2013, Willison and Lowry 2018). However, malice is defined as a “desire to cause pain, injury, or distress to another” (Merriam-Webster, s.v. “malice,” accessed March 11, 2021, https://www.merriam-webster. com/dictionary/malice), which implies motive. Because we were interested in examining motives separately, we removed this constraint from our definition of ICA. Furthermore, harm represents a consequence of behavior that is often unknown at the time of action. Likewise, the same ICA can inflict varying levels of harm depending on the circumstances. Thus, we adapted our formal definition of ICA from Straub’s (1990) original definition of deliberate and unauthorized ICA.

<sup>6</sup> Per the IBM (2021) Cost of a Data Breach Report 2021.

<sup>7</sup> See https://www.justice.gov/usao-mdla/pr/former-systems-adm inistrator-sentenced-prison-hacking-industrial-facility-computer.

## References

Ambrose ML, Seabright MA, Schminke M (2002) Sabotage in the workplace: The role of organizational injustice. Organ. Behav. Human Decision Processes 89(1):947–965.

Andrews DA, Bonta J (2010) The Psychology of Criminal Conduct (Matthew Bender & Company, New Providence, NJ).

Aquino K, Reed AII (2002) The self-importance of moral identity. J. Personality Soc. Psych. 83(6):1423–1440.

Ariely D, Wertenbroch K (2002) Procrastination, deadlines, and performance: Self-control by precommitment. Psych. Sci. 13(3): 219–224.

Avgerou C (2001) The signi<sup>fi</sup>cance of context in information systems and organizational change. Inform. Systems J. 11(1):43–63.

Barbuto JE (2005) Motivation and transactional, charismatic, and transformational leadership: A test of antecedents. J. Leadershi Organ. Stud. 11(4):26–40.

Bennett RJ, Robinson SL (2000) Development of a measure of work place deviance. J. Appl. Psych. 85(3):349–360.

Bentham J (1988) An Introduction to the Principles of Morals and Legislation (Prometheus Books, New York).

Bordia P, Restubog SLD, Tang RL (2008) When employees strike back: Investigating mediating mechanisms between psychological contract breach and workplace deviance. J. Appl. Psych. 93(5):1104–1117.

Boss SR, Galletta DF, Lowry PB, Moody GD, Polak P (2015) What do systems users have to fear? Using fear appeals to engende threats and fear that motivate protective security behaviors. MIS Quart. 39(4):837–864.

Boss SR, Kirsch LJ, Angermeier I, Shingler RA, Boss RW (2009) If someone is watching, I’ll do what I’m asked: Mandatoriness, control, and information security. Eur. J. Inform. Systems 18(2): 151–164.

Brennan G, Hamlin A (1998) Expressive voting and electoral equili brium. Public Choice 95(1):149–175.

Breward M, Hassanein K, Head M (2017) Understanding consumers’ attitudes toward controversial information technologies: A contextualization approach. Inform. Systems Res. 28(4):760–774.

Bulgurcu B, Cavusoglu H, Benbasat I (2010) Information security pol icy compliance: An empirical study of rationality-based beliefs and information security awareness. MIS Quart. 34(4):523–548.

Burns AJ, Posey C, Roberts TL, Lowry PB (2017) Examining the relationship of organizational insiders’ psychological capital with information security threat and coping appraisals. Comput. Human Behav. 68(March):190–209.

Burns AJ, Roberts TL, Posey C, Bennett RJ, Courtney JF (2018) Intentions to comply vs. intentions to protect: A VIE theory approach to understanding the in<sup>fl</sup>uence of insiders’ awareness of organizational SETA efforts. Decision Sci. 49(6):1187–1228.

Chatterjee S, Sarker S, Valacich JS (2015) The behavioral roots of information systems security: Exploring key factors related to unethical IT use. J. Management Inform. Systems 31(4):49–87.

Chen Y, Ramamurthy K, Wen KW (2012) Organizations’ information security policy compliance: Stick or carrot approach? J. Management Inform. Systems 29(3):157–188.

Chin WW, Thatcher JB, Wright RT, Steel D (2013) Controlling for common method variance in PLS analysis: The measured latent marker variable approach. Abdi H, Chin WW, Vinzi VE, Russolillo G, Trinchera L, eds. New Perspectives in Partial Least Squares and Related Methods (Springer, New York), 231–239.

Chiu SF, Peng JC (2008) The relationship between psychologica contract breach and employee deviance: The moderating role of hostile attributional style. J. Vocational Behav. 73(3):426–433.

Cohen J (1988) Statistical Power Analysis for the Behavioral Sciences, 2nd ed. (Lawrence Erlbaum Associates, Hillsdale, NJ)

Crossler RE, Johnston AC, Lowry PB, Hu Q, Warkentin M, Baskerville R (2013) Future directions for behavioral information security research. Comput. Security 32(February):90–101.

D’Arcy J, Herath T (2011) A review and analysis of deterrence theory in the IS security literature: Making sense of the dispa rate <sup>fi</sup>ndings. Eur. J. Inform. Systems 20(6):643–658.

D’Arcy J, Hovav A (2007) Deterring internal information systems misuse. Comm. ACM 50(10):113–117.

D’Arcy J, Lowry PB (2019) Cognitive-affective drivers of employees daily compliance with information security policies: A multilevel, longitudinal study. Inform. Systems J. 29(1):43–69.

D’Arcy J, Herath T, Shoss M (2014) Understanding employee responses to stressful information security requirements: A coping perspective. J. Management Inform. Systems 31(2): 285–318.

D’Arcy J, Hovav A, Galletta D (2009) User awareness of security countermeasures and its impact on information systems mis use: A deterrence approach. Inform. Systems Res. 20(1):79–98.

Dalal RS (2005) A meta-analysis of the relationship between organi zational citizenship behavior and counterproductive work behavior. J. Appl. Psych. 90(6):1241–1255.

Davison RM, Martinsons MG (2016) Context is king! Considering particularism in research design and reporting. J. Inform. Tech. 31(3):241–249.

Dey D, Ghoshal A, Lahiri A (2021) Circumventing circumvention: An economic analysis of the role of education and enforcement. Management Sci., ePub ahead of print August 11, 2021, https:// doi.org/10.1287/mnsc.2021.4027.

Feshbach S (1964) The function of aggression and the regulation of aggressive drive. Psych. Rev. 71(4):257–272.

Fornell C, Bookstein FL (1982) Two structural equation models: LIS-REL and PLS applied to consumer exit-voice theory. J. Marketing Res. 19(4):440–452.

Fornell C, Larcker DF (1981) Evaluating structural equation models with unobservable variables and measurement error. J. Market ing Res. 18(1):39–50.

Foth M (2016) Factors in<sup>fl</sup>uencing the intention to comply with data protection regulations in hospitals: Based on gender differences in behaviour and deterrence. Eur. J. Inform. Systems 25(2):91–109.

Gerbing DW, Anderson JC (1988) An updated paradigm for scale development incorporating unidimensionality and its assessment. J. Marketing Res. 25(2):186–192.

Gino F, Schweitzer ME, Mead NL, Ariely D (2011) Unable to resist temptation: How self-control depletion promotes unethical behavior. Organ. Behav. Human Decision Processes 115(2):191–203.

Gottfredson MR (2011) Sanctions, situations, and agency in control theories of crime. Eur. J. Criminology 8(2):128–143.

Gottfredson M (2017) Self-control theory and crime. Oxford Research Encyclopedia of Criminology. Retrieved September 6, https://oxfordre.com/criminology/view/10.1093/acrefore/978 0190264079.001.0001/acrefore-9780190264079-e-252.

Gottfredson M, Hirschi T (1990) A General Theory of Crime (Stanford University Press, Stanford, CA).

Greenberg A (2020) A Tesla employee thwarted an alleged ransomware plot. Wired (August 27), https://www.wired.com/story/ tesla-ransomware-insider-hack-attempt/.

Gregor S (2006) The nature of theory in information systems. MIS Quart. 30(3):611–642

Grover V, Lyytinen K (2015) New state of play in information systems research: The push to the edges. MIS Quart. 39(2):271–296.

Guo KH, Yuan Y, Archer NP, Connelly CE (2011) Understanding nonmalicious security violations in the workplace: A composite behavior model. J. Management Inform. Systems 28(2):203–236.

Hagger MS, Wood C, Stiff C, Chatzisarantis NLD (2010) Ego deple tion and the strength model of self-control: A meta-analysis. Psych. Bull. 136(4):495–525.

Hair JF, Hult GTM, Ringle CM, Sarstedt M (2017) A Primer on Partial Least Squares Structural Equations Modeling (PLS-SEM), 2nd ed. (SAGE, Thousand Oaks, CA).

Han J, Kim YJ, Kim H (2017) An integrative model of information security policy compliance with psychological contract: Exam ining a bilateral perspective. Comput. Security 66(May):52–65.

Harrington SJ (1996) The effect of codes of ethics and personal denial of responsibility on computer abuse judgments and intentions. MIS Quart. 20(3):257–278.

Hassan NR, Lowry PB (2015) Seeking middle-range theories in information systems research. Proc. Internat. Conf. Inform. Sys tems, December 13–18 (ICIS, Fort Worth, TX)

Hassan NR, Mathiassen L, Lowry PB (2019) The process of information systems theorizing as a discursive practice. J. Inform. Tech. 34(3):198–220.

Henseler J, Chin WW (2010) A comparison of approaches for the analysis of interaction effects between latent variables using partial least squares path modeling. Structural Equation Model. 17(1):82–109.

Henseler J, Ringle CM, Sarstedt M (2015) A new criterion for assessing discriminant validity in variance-based structural equation modeling. J. Acad. Marketing Sci. 43(1):115–135.

Henseler J, Dijkstra TK, Sarstedt M, Ringle CM, Diamantopoulos A, Straub DW, Ketchen DJ, Hair JF, Hult GTM, Calantone RJ (2014) Common beliefs and reality about PLS: Comments on Ronkk¨ o and Evermann (2013).¨ Organ. Res. Methods 17(2): 182–209.

Herath T, Rao HR (2009) Protection motivation and deterrence: A framework for security policy compliance in organisations. Eur. J. Inform. Systems 18(2):106–125.

Hirschi T (2017) Causes of Delinquency (Routledge, New York).

Holtfreter K, Reisig MD, Pratt TC (2008) Low self-control, routine activities, and fraud victimization. Criminology 46(1):189–220.

Hong W, Chan FKY, Thong JYL, Chasalow LC, Dhillon G (2014) A framework and guidelines for context-speci<sup>fi</sup>c theorizing in information systems research. Inform. Systems Res. 25(1): 111–136.

Hu L, Bentler PM (1999) Cutoff criteria for <sup>fi</sup>t indexes in covariance structure analysis: Conventional criteria vs. new alternatives. Structural Equation Model. 6(1):1–55.

Hu Q, West R, Smarandescu L (2015) The role of self-control in information security violations: Insights from a cognitive neuroscience perspective. J. Management Inform. Systems 31(4):6–48.

Hu Q, Xu Z, Dinev T, Ling H (2011) Does deterrence work in reducing information security policy abuse by employees? Comm. ACM 54(6):54–60.

IBM (2021) Cost of a data breach report 2021, Accessed November 11, 2021, https://www.ibm.com/security/data-breach.

Jensen ML, Dinger M, Wright RT, Thatcher JB (2017) Training to mitigate phishing attacks using mindfulness techniques. J. Man agement Inform. Systems 34(2):597–626.

Johnson RE, Lin SH, Lee HW (2018) Self-control as the fuel for effective self-regulation at work: Antecedents, consequences, and boundary conditions of employee self-control. Elliot AJ, ed. Advances in Motivation Science, vol. 5 (Elsevier, Cambridge, MA), 87–128.

Johnston AC, Warkentin M (2010) Fear appeals and information security behaviors: An empirical study. MIS Quart. 34(3): 549–566.

Johnston AC, Warkentin M, Siponen M (2015) An enhanced fear appeal rhetorical framework: Leveraging threats to the human asset through sanctioning rhetoric. MIS Quart. 39(1):113–134.

Johnston AC, Warkentin M, McBride M, Carter L (2016) Disposi tional and situational factors: In<sup>fl</sup>uences on information security policy violations. Eur. J. Inform. Systems 25(3):231–251.

Jones S, Lynam DR (2009) In the eye of the impulsive beholder: The interaction between impulsivity and perceived informal social control on offending. Criminal Justice Behav. 36(3):307–321.

Kays K, Gathercoal K, Buhrow W (2012) Does survey format in<sup>fl</sup>uence self-disclosure on sensitive question items? Comput Human Behav. 28(1):251–256.

Khansa L, Kuem J, Siponen M, Kim SS (2017) To cyberloaf or not to cyberloaf: The impact of the announcement of formal organizational controls. J. Management Inform. Systems 34(1): 141–176.

Kunze M, Gower K (2012) The in<sup>fl</sup>uence of subordinate affect and self monitoring on multiple dimensions of leader-member exchange. Internat. J. Management Marketing Res. 5(3):83–100.

Lee SM, Lee SG, Yoo S (2004) An integrative model of computer abuse based on social control and general deterrence theories. Inform. Management 41(6):707–718.

Leidner D, Tona O (2021) The CARE theory of dignity amid personal data digitalization. MIS Quart. 45(1b):343–370.

Leonard NH, Beauvais LL, Scholl RW (1999) Work motivation: The incorporation of self-concept-based processes. Human Relations 52(8):969–998.

Li H, Luo XR, Chen Y (2021) Understanding information security policy violation from a situational action perspective. J. Assoc. Inform. Systems 22(3):5.

Li H, Luo X, Zhang J, Sarathy R (2018) Self-control, organizational context, and rational choice in internet abuses at work. Inform. Management 55(3):358–367.

Lian H, Brown DJ, Ferris DL, Liang LH, Keeping LM, Morrison R (2014) Abusive supervision and retaliation: A self-control framework. Acad. Management J. 57(1):116–139.

Liang H, Saraf N, Hu Q, Xue Y (2007) Assimilation of enterprise systems: The effect of institutional pressures and the mediating role of top management. MIS Quart. 31(1):59–87.

Lin TC, Huang SL, Chiang SC (2018) User resistance to the implementation of information systems: A psychological contract breach perspective. J. Assoc. Inform. Systems 19(4):306–332.

Locke EA (1981) Goal setting and task performance: 1969–1980. Psych. Bull. 90(1):125–152.

Lowry PB, Gaskin J (2014) Partial least squares (PLS) structural equation modeling (SEM) for building and testing behavioral causal theory: When to choose it and how to use it. IEEE Trans. Professional Comm. 57(2):123–146.

Lowry PB, Dinev T, Willison R (2017a) Why security and privacy research lies at the centre of the information systems (IS) arte fact: Proposing a bold research agenda. Eur. J. Inform. Systems 26(6):546–563.

Lowry PB, Moody GD, Chatterjee S (2017b) Using IT design to pre vent cyberbullying. J. Management Inform. Systems 34(3):863–901.

Lowry PB, D’Arcy J, Hammer B, Moody GD (2016a) “Cargo cult” science in traditional organization and information systems survey research: A case for using nontraditional methods of data collection, including Mechanical Turk and online panels. J. Stra tegic Inform. Systems 25(3):232–240.

Lowry PB, Moody G, Galletta D, Vance A (2013a) The drivers in the use of online whistle-blowing reporting systems. J. Management Inform. Systems 30(1):153–189.

Lowry PB, Posey C, Bennett RJ, Roberts TL (2015) Leveraging fairness and reactance theories to deter reactive computer abuse following enhanced organisational information security poli cies: An empirical study of the in<sup>fl</sup>uence of counterfactual reasoning and organisational trust. Inform. Systems J. 25(3):193–273.

Lowry PB, Posey C, Roberts TL, Bennett RJ (2013b) Is your banker leaking your personal information? The roles of ethics and individual-level cultural characteristics in predicting organizational computer abuse. J. Bus. Ethics 121(3):385–401.

Lowry PB, Zhang J, Wang C, Siponen M (2016b) Why do adults engage in cyberbullying on social media? An integration of online disinhibition and deindividuation effects with the social structure and social learning model. Inform. Systems Res. 27(4): 962–986.

Lowry PB, Zhang J, Moody GD, Chatterjee S, Wang C, Wu T (2019) An integrative theory addressing cyberharassment in the light

of technology-based opportunism. J. Management Inform. Systems 36(4):1142–1178.

Luo XR, Li H, Hu Q, Xu H (2020) Why individual employees commit malicious computer abuse: A routine activity theory per spective. J. Assoc. Inform. Systems 21(6):1552–1593.

Meier RF, Johnson WT (1977) Deterrence as social control: Th legal and extralegal production of conformity. Amer. Sociol. Rev. 42(2):292–304.

Menard P, Warkentin M, Lowry PB (2018) The impact of collectivism and psychological ownership on protection motivation: A cross-cultural examination. Comput. Security 75(June):147–166.

Merton RK (1968) Social Theory and Social Structure (Free Press, New York).

Miller S (2018) 2017 U.S. state of cybercrime highlights. SEI Blog (January 17), https://insights.sei.cmu.edu/insider-threat/2018/ 01/2017-us-state-of-cybercrime-highlights.html.

Moody GD, Siponen M, Pahnila S (2018) Toward a uni<sup>fi</sup>ed model of information security policy compliance. MIS Quart. 42(1): 285–311.

Morrison EW, Robinson SL (1997) When employees feel betrayed: A model of how psychological contract violation develops. Acad. Management Rev. 22(1):226–256.

Murray KT, Kochanska G (2002) Effortful control: Factor structure and relation to externalizing and internalizing behaviors. J. Abnormal Child Psych. 30(5):503–514.

Myyry L, Siponen M, Pahnila S, Vartiainen T, Vance A (2009) What levels of moral reasoning and values explain adherence to information security rules? An empirical study. Eur. J. Inform. Systems 18(2):126–139.

Nagin DS (1998) Deterrence and incapacitation. Tonry M, ed. The Handbook of Crime and Punishment (Oxford University Press, New York). 345–368

Nagin DS, Paternoster R (1993) Enduring individual differences and rational choice theories of crime. Law Soc. Rev. 27(3):467–496.

Nagin DS, Pogarsky G (2001) Integrating celerity, impulsivity, and extralegal sanction threats into a model of general deterrence: Theory and evidence. Criminology 39(4):865–892.

Nunnally J (1978) Psychometric Theory (McGraw-Hill, New York)

Park Y, El Sawy OA, Fiss P (2017) The role of business intelligence and communication technologies in organizational agility: A con <sup>fi</sup>gurational approach. J. Assoc. Inform. Systems 18(9):648–686.

Parsons T, Bales RF (1955) Family, Socialization and Interaction Process (Free Press, Glencoe, IL)

Pavlou PA, Gefen D (2005) Psychological contract violation in online marketplaces: Antecedents, consequences, and moderating role. Inform. Systems Res. 16(4):372–399.

Petter S, Straub DW, Rai A (2007) Specifying formative constructs in information systems research. MIS Quart. 31(4):623–656.

Piquero AR, Paternoster R, Pogarsky G, Loughran T (2011) Elaborating the individual difference component in deterrence theory. Annu. Rev. Law Soc. Sci. 7(1):335–360.

Podsakoff PM, MacKenzie SB, Lee JY, Podsakoff NP (2003) Common method biases in behavioral research: a critical review of the litera ture and recommended remedies. J. Appl. Psych. 88(5):879–903.

Ponemon Institute (2018) 2018 cost of a data breach report: Global overview. accessed April 18, 2019, https://www.ibm.com/ downloads/cas/861MNWN2.

Posey C, Bennett RJ, Roberts TL (2011) Understanding the mindset of the abusive insider: An examination of insiders’ causal reasoning following internal security changes. Comput. Security 30(6):486–497.

Posey C, Roberts TL, Lowry PB (2015) The impact of organizational commitment on insiders’ motivation to protect organizational information assets. J. Management Inform. Systems 32(4):179–214

Posey C, Roberts TL, Lowry PB, Bennett RJ, Courtney JF (2013) Insiders’ protection of organizational information assets:

Development of a systematics-based taxonomy and theory of diversity for protection-motivated behaviors. MIS Quart. 37(4):1189–1210.

PWC (2014) Managing cyber risks in an interconnected world: Key <sup>fi</sup>ndings from the Global State of Information Security Survey 2015. Acccessed December 12, 2014, https://www.pwc.com/ gx/en/consulting-services/information-security-survey/assets/ the -global-state-of-information-security-survey-2015.pdf

Qin X, Huang M, Johnson RE, Hu Q, Ju D (2018) The short-lived bene<sup>fi</sup>ts of abusive supervisory behavior for actors: An investigation of recovery and work engagement. Acad. Management J. 61(5):1951–1975.

Restubog SLD, Bordia P, Tang RL (2006) Effects of psychological contract breach on performance of IT employees: The mediating role of affective commitment. J. Occupational Organ. Psych. 79(2):299–306.

Ringle CM, Wende S, Becker JM (2015) SmartPLS3. SmartPLS GmbH, Bonningstedt, Germany.¨

Rivard S (2021) Theory building is neither an art nor a science: It is a craft. J. Inform. Tech. 36(3):316–328.

Robinson SL, Bennett RJ (1995) A typology of deviant workplace behaviors: A multidimensional scaling study. Acad. Management J. 38(2):555–572.

Robinson SL, Bennett RJ (1997) Workplace deviance: Its de<sup>fi</sup>nition, its manifestations, and its causes. Lewicki RJ, Bies RJ, Sheppard BH, eds. Research on Negotiations in Organizations, vol. 6 (Elsevier, Amsterdam). 3-27.

Robinson SL, Morrison EW (2000) The development of psychologi cal contract breach and violation: A longitudinal study. J. Organ. Behav. 21(5):525–546.

Robinson SL, O’Leary-Kelly AM (1998) Monkey see, monkey do: The in<sup>fl</sup>uence of work groups on the antisocial behavior of employees. Acad. Management J. 41(6):658–672.

Rousseau DM (1989) Psychological and implied contracts in organi zations. Employee Responsibilities Rights J. 2(2):121–139.

Rousseau DM (2004) Psychological contracts in the workplace: Understanding the ties that motivate. Acad. Management Perspect. 18(1):120–127.

Schreck CJ (1999) Criminal victimization and low self-control: An extension and test of a general theory of crime. Justice Quart. 16(3):633–654.

Schreck CJ, Stewart EA, Osgood DW (2008) A reappraisal of the overlap of violent offenders and victims. Criminology 46(4): 871–906.

Schwarz A, Rizzuto T, Carraher-Wolverton C, Roldan JL, Barrera-´ Barrera R (2017) Examining the impact and detection of the urban legend of common method bias. ACM SIGMIS Database 48(1):93–119.

Siponen M, Vance A (2010) Neutralization: New insights into the problem of employee information systems security policy viola tions. MIS Quart. 34(3):487–502.

Sojer M, Alexy O, Kleinknecht S, Henkel J (2014) Understanding the drivers of unethical programming behavior: The inappropriate reuse of Internet-accessible code. J. Management Inform. Systems 31(3):287–325.

Soper D (2019) Post-hoc statistical power calculator for hierarchical multiple regression, version 4.0, Accessed January 16, 2019, https://www.danielsoper.com/statcalc/calculator.aspx?id=17.

Storrod ML, Densley JA (2017) “Going viral” and “Going country”: The expressive and instrumental activities of street gangs on social media. J. Youth Stud. 20(6):677–696.

Straub DW (1990) Effective IS security. Inform. Systems Res. 1(3): 255–276.

Straub DW, Nance W (1990) Discovering and disciplining computer abuse in organizations: A <sup>fi</sup>eld study. MIS Quart. 14(1):45–60.

Sutton G, Grif<sup>fi</sup>n MA (2004) Integrating expectations, experiences, and psychological contract violations: A longitudinal study of new professionals. J. Occupational Organ. Psych. 77(4):493–514.

Tangney JP, Baumeister RF, Boone AL (2004) High self-control predicts good adjustment, less pathology, better grades, and inter personal success. J. Personality 72(2):271–324.

Tekleab AG, Takeuchi R, Taylor MS (2005) Extending the chain of relationships among organizational justice, social exchange, and employee reactions: The role of contract violations. Acad. Management J. 48(1):146–157.

Tibbetts SG, Gibson CL (2002) Individual propensities and rational decision-making: Recent <sup>fi</sup>ndings and promising approaches. Piquero AR, Tibbetts SG, eds. Rational Choice and Criminal Behavior Recent Research and Future Challenges (Routledge, New York), 3–24.

Tiwana A (2009) Governance-knowledge <sup>fi</sup>t in systems development projects. Inform. Systems Res. 20(2):180–197.

Tiwana A (2015) Evolutionary competition in platform ecosystems Inform. Systems Res. 26(2):266–281.

Turanovic JJ, Pratt TC (2014) “Can’t stop, won’t stop”: Self-control, risky lifestyles, and repeat victimization. J. Quant. Criminol. 30(1): 29–56.

Vance A, Lowry PB, Eggett D (2013) Using accountability to reduce access policy violations in information systems. J. Management Inform. Systems 29(4):263–289.

Vardi Y (2001) The effects of organizational and ethical climates on misconduct at work. J. Bus. Ethics 29(4):325–337.

Vroom V (1964) Work and Motivation (Wiley, Oxford, UK).

Wachi T, Watanabe K, Yokota K, Suzuki M, Hoshino M, Sato A, Fujit G (2007) Offender and crime characteristics of female serial arsonists in Japan. J. Investigative Psych. Offender Profiling 4(1):29–52.

Wang M, Liao H, Zhan Y, Shi J (2011) Daily customer mistreatment and employee sabotage against customers: Examining emotion and resource perspectives. Acad. Management J. 54(2):312–334.

Wehrt W, Casper A, Sonnentag S (2020) Beyond depletion: Daily self-control motivation as an explanation of self-control failure at work. J. Organ. Behav. 41(9):931–947.

Wetzels M, Odekerken-Schroder G, Van Oppen C (2009) Using PLS path modeling for assessing hierarchical construct models: Guidelines and empirical illustration. MIS Quart. 33(1):177–196.

Willison R, Lowry PB (2018) Disentangling the motivations for organizational insider computer abuse through the rational choice and life course perspectives. ACM SIGMIS Database 49(S1):81–102.

Willison R, Warkentin M (2013) Beyond deterrence: An expanded view of employee computer abuse. MIS Quart. 37(1):1–20.

Willison R, Lowry PB, Paternoster R (2018a) A tale of two deterrents: Considering the role of absolute and restrictive deterrence in inspiring new directions in behavioral and organizational security. J. Assoc. Inform. Systems 19(12):1187–1216.

Willison R, Warkentin M, Johnston AC (2018b) Examining employe computer abuse intentions: Insights from justice, deterrence and neutralization perspectives. Inform. Systems J. 28(2):266–293.

Xu B, Xu Z, Li D (2016) Internet aggression in online communities: A contemporary deterrence perspective. Inform. Systems J. 26(6): 641–667.

Youngs D, Ioannou M, Eagles J (2016) Expressive and instrumental offending: Reconciling the paradox of specialisation and versatility. Internat. J. Offender Therapy Comparative Criminology 60(4): 397–422.

Yu J (1994) Punishment celerity and severity: Testing a speci<sup>fi</sup>c deterrence model on drunk driving recidivism. J. Criminal Jus tice 22(4):355–366.

Zhao H, Wayne SJ, Glibkowski BC, Bravo J (2007) The impact of psychological contract breach on work-related outcomes: A meta-analysis. Personnel Psych. 60(3):647–680.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
