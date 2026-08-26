---
otero_id: 14024
otero_key: "4NRX2JGU"
title: "Continued use of process modeling grammars: the impact of individual difference factors"
authors: "Jan Recker"
year: "2010"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2010.5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Continued use of process modeling grammars: the impact of individual difference factors

Jan Recker

Queensland University of Technology, Information Systems Program, Brisbane, Australia

Correspondence: Jan Recker, Queensland University of Technology, Information Systems Program, 126 Margaret Street, Brisbane, QLD 4000, Australia. Tel: +61 7 3138 9479: Fax: þ 61 7 3138 9390

## Abstract

Process modeling grammars are used by analysts to describe information systems domains in terms of the business operations an organization is conducting. While prior research has examined the factors that lead to continued usage behavior, little knowledge has been established as to what extent characteristics of the users of process modeling grammars inform usage behavior. In this study, a theoretical model is advanced that incorporates determinants of continued usage behavior as well as key antecedent individual difference factors of the grammar users, such as modeling experience, modeling background and perceived grammar familiarity. Findings from a global survey of 529 grammar users support the hypothesized relationships of the model. The study offers three central contributions. First, it provides a validated theoretical model of post-adoptive modeling grammar usage intentions. Second, it discusses the effects of individual difference factors of grammar users in the context of modeling grammar usage. Third, it provides implications for research and practice.

Keywords: process modeling; continuance; user characteristics; usage behavior

## Introduction

Information systems (IS) analysts and designers need to have an understanding about the domain in which the system is meant to operate, and the functions it has to perform (Maes & Poels, 2007). To address this task, analysts and designers typically create models of the relevant business domains of IS. Over recent years, analysts have started to specify these domains in the form of the processes that are run by an organization, in order to assess or build IS that are ‘process-aware’. And indeed, the exercise of ‘process modeling’ has emerged as a primary reason to engage in conceptual modeling (Davies et al., 2006) and is now considered a key instrument for the analysis and design of process-aware IS (Dumas et al., 2005), service-oriented architectures (Erl, 2005) and web services (Ouyang et al., 2008) alike.

Process models are specified using process modeling grammars (sets of graphical constructs and a set of rules how to combine these constructs, as per Wand & Weber, 2002). The type of grammar used for modeling defines the language and its grammatical rules that can be used to articulate and communicate details about the real-world domain, and thus determines the outcomes of the modeling process (Siau & Rossi, 2010). A wide selection of process modeling grammars is available to organizations, ranging from simple flowcharts (Ramsey et al., 1983) and typical business modeling grammars like Event-driven Process Chains (Scheer, 2000) to highly formalized and technically oriented grammars such as WS-BPEL (Leymann & Roller, 2006) or YAWL (van der Aalst & ter Hofstede, 2005) that are capable of process simulation and/or execution. However, despite the proliferation of process modeling grammars in general (Recker et al., 2009), only few have been widely accepted and continuously used by the IS community. Indeed, the recent emergence of the Business Process Modeling Notation (BPMN) grammar (BPMI.org & OMG, 2006) as an industry standard for process modeling has been characterized as adoption success without a body of knowledge explaining this phenomenon (Recker, 2010). In fact, IS research has yet to uncover the factors leading to successful adoption of process modeling grammars on an organizational level, and to continued usage of such grammars on an individual level.

The objective of our research is to develop an understanding of the factors that influence the continued usage of process modeling grammars. The present study focuses on the reasons why individual process modelers are willing to continue to use a process modeling grammar after its initial adoption, which, often, is an organizational decision. This is important because individual modelers do in fact sometimes decide not to use a modeling grammar even if there has been an organizational decision to adopt it (e.g., Orlikowski, 1993).

To that end, this study reports on the development and empirical testing of a theoretical model that explains how individual users form continuance intentions associated with the use of a process modeling grammar, and how individual difference factors of the grammar users inform the key beliefs associated with continuance behavior.

We proceed as follows. The next section provides a background to our research, before we outline the theory underlying our study and advance a range of hypotheses contained in our research model. Next, we describe the research method employed in our empirical study. We then discuss operationalization and validation of measurements used, before the next section presents our data analysis and the results. Next, we provide a discussion of the results. We describe some opportunities for future research and then present the implications of our study for practice. We conclude this paper by briefly recapitulating the contributions of our work.

## Process modeling grammars and individual differences

## Process modeling

Process modeling is widely used within organizations as a method to increase awareness and knowledge of organizational operations, and to support the design or re-design of business processes. It is an approach for describing how businesses conduct their operations, be it as part of an effort to understand or analyze current ‘as is’ operations, or be it as part of an effort to design improved blueprints for future operations (‘to be’ modeling). In either case, process modeling typically includes graphical depictions of at least the activities, events/states and control flow logic that constitute a business process (Curtis et al., 1992). Additionally, process models may also include information regarding the involved data, organizational/IT resources and potentially other artifacts such as external stakeholders and performance metrics to name just a few (Scheer, 2000).

In considering how to model business processes, the type of grammar to be used for process modeling is an important decision to make (Rosemann et al., 2006). Different modeling grammars emphasize different aspects of process domains, for instance activity sequencing, resource allocations, information flows or organizational responsibilities (Soffer & Wand, 2007). From a broad perspective, process modeling grammars fall into two categories (Phalp, 1998). Business-oriented modeling grammars, such as Event-driven Process Chains (EPCs), are mostly concerned with capturing and understanding processes for project scoping tasks, and for discussing business requirements and process improvement initiatives with subject matter experts. Conversely, technically oriented process modeling grammars, such as BPMN, are based on formal specifications and are typically used for process analysis (Verbeek et al., 2007) or process execution (van der Aalst & ter Hofstede, 2005), and can facilitate experimentation with process scenarios (Gregoriades & Sutcliffe, 2008).

Similar to the differences in the grammars that can be used for process modeling tasks, there are also differences to be considered between the types of users working with such grammars. Prior research on modeling (e.g., Batra & Davis, 1992; Sutcliffe & Maiden, 1992; Shanks, 1997) uncovered noticeable differences between modelers with different levels of experience in the way conceptual modeling was being conducted and applied for modeling-related tasks. Similarly, Khatri et al. (2006) showed empirically that users with different levels of method and domain knowledge performed modeling-related tasks differently. Effects of individual difference factors, such as cognitive style (Agarwal & Karahanna, 2000), experience (Castan˜eda et al., 2007) or training (Lee & Truex, 2000), have further been shown to effect usage and adoption beliefs. Yet, to date very little knowledge has been established about the relationships that link such individual difference factors to the formation of continued usage beliefs. Accordingly, our interest in this study is to examine empirically whether individual differences between the users working with process modeling grammars also manifest in their post-adoptive usage behavior associated with these grammars.

## Post-adoptive usage behavior

The research stream examining the adoption and continued use of IT by its users has evolved into one of the richest and most mature research streams in the IS field. We focus on the phenomenon of post-adoptive usage behavior, also known as continued acceptance or continuance (Bhattacherjee, 2001), a phenomenon that has in recent years emerged as an important stream of IS research that complements existing technology acceptance research.

Post-adoptive behavior occurs after an IS artifact has been implemented, made accessible to the user and applied by the user in accomplishing his/her work activities (Jasperson et al., 2005). This behavior may be quite different from the behavior in initial adoption stages. For instance, a user of a particular process modeling grammar may start using only a subset of the graphical constructs contained in the grammar. Over time, however, she may choose to explore – and use – other grammar constructs and use them for the process modeling tasks at hand. Or, users of a process modeling grammar may choose, over time, to use a set of grammar constructs in a way that deviates from the originally specified semantics.

In most organizations, the use of a specific process modeling grammar is mandated (Recker et al., 2006). However, how exactly the process modeling grammar is continued in its use by an individual (independent from a potential usage mandate) is up to the discretion of the modeler. Prior studies (e.g., Orlikowski, 1993; Khalifa & Verner, 2000; Brown et al., 2002) have shown that individual modelers do in fact sometimes decide not to use a modeling grammar even if there has been an organizational decision to adopt it. While some parts of such decision processes have been linked to the individual beliefs about the utility of the artifact at hand (e.g., usefulness, satisfaction or ease of use), to date, it remains unclear as to how individual difference factors of the users (e.g., prior experience or familiarity) inform such a decision, which has motivated the research presented in this paper.

## Theory and hypotheses

Our conceptualization of the factors influencing postadoptive usage behavior associated with process modeling grammars involves two levels of analysis (see Figure 1). We consider the determinants of the continuance decision, as well as the key antecedent factors of these determinants. We focus on one group of antecedent factors specifically, namely individual difference factors pertaining to the users working with process modeling grammars. This is important, because how a grammar is used for a particular process modeling task may vary depending on the abilities of the individual that performs the modeling task. Generally, individuals who are more competent, better trained, more experienced or more familiar with their tasks and/or use of IS artifacts are typically better in accomplishing task objectives and meeting job requirements (e.g., Goodhue, 1995). Our contention in this study is to examine whether the formation of an intention to continue working a process modeling grammar is also informed by such individual difference factors.

In developing our research model we first synthesize findings from prior research on continued usage behavior. Consistent with the established body of research based on, and integrating, theories of technology acceptance (Davis, 1989) and expectation-confirmation behavior (Bhattacherjee, 2001), we expect that perceived usefulness (PU), perceived ease of use (PEOU) and satisfaction (SAT) are direct determinants of grammar usage intentions (ItU).

PU captures performance beliefs (for instance, whether or not using a grammar improves the quality of the process modeling or the overall success of the initiative), and reflects expected effectiveness and efficiency gains (Davis, 1989). PU is a salient cognitive determinant of ItU because users perceiving a grammar to be useful are more likely to believe that its usage will lead to process modeling performance achievements. Hence they can be expected to be willing to continue to use the grammar. Accordingly, we have:

H1: Process modelers’ perceived usefulness of a process modeling grammar is positively associated with their intention to continue using the grammar.

![](/api/attachments/4NRX2JGU/fulltext/images/6e8699316e974a6e69026b4c6639f5d733fbb2b99b70f1987fa8967c8eade564.jpg)  
Figure 1 Research model.

PEOU captures attitudes and beliefs about the effort that is needed to apply a grammar (Davis, 1989). The more a user perceives a process modeling grammar to be easy to work with, the greater the user’s sense of efficacy and personal control regarding her ability to carry out process modeling tasks. This situation, in turn, suggests that PEOU will directly determine ItU. Hence, the following hypothesis:

## H2: Process modelers’ perceived ease of use of a process modeling grammar is positively associated with their intention to continue using the grammar.

SAT with a process modeling grammar can stem from positive usage beliefs (for instance, the PU and PEOU) and beliefs stemming from pre-usage periods (for instance, whether or not pre-usage expectations can be confirmed through usage experiences, see Bhattacherjee, 2001). Satisfied users of a process modeling grammar typically have positive first-hand experiences about the use of a process modeling grammar and are thus likely motivated to continue working with the grammar, while dissatisfied users would discontinue their use. Hence, we have:

H3: Process modelers’ level of satisfaction with process modeling grammar use is positively associated with their intention to continue using the grammar.

Following Davis (1989), PU is partly determined by PEOU. PEOU suggests that users of a process modeling grammar achieve performance gains faster. Efforts saved due to improved ease of use may be redeployed, enabling a grammar user to accomplish more process modeling work for the same effort. This in turn, may lead to an increased perception of the usefulness of the grammar, as the performance gains achieved through the grammar use increase due to improved ease of its use. Accordingly:

H4: Process modelers’ perceived ease of use of a process modeling grammar is positively associated with their perceived usefulness of a process modeling grammar.

PEOU is also expected to influence SAT with the use of a grammar. PEOU suggests that users can learn and apply a grammar with little effort, leading to the achievement of results in a faster way. Such a situation potentially increases the SAT about the use of the process modeling grammar (e.g., Mahmood et al., 2000). Accordingly:

H5: Process modelers’ perceived ease of use of a process modeling grammar is positively associated with their level of satisfaction with process modeling grammar use.

Bhattacherjee (2001) further suggests that SAT is also determined through positive beliefs about PU, and through the confirmation of pre-usage expectations through actual usage experiences. PU captures the instrumentality of process modeling grammar use. PU is positively related to SAT with process modeling grammar use because it implies realization of expected benefits from grammar use (such as assistance in meeting process modeling objectives, provision of all constructs required to depict desired real-world phenomena and so forth). Confirmation (CON) captures beliefs about the extent to which pre-usage expectations are positively (dis-) confirmed through actual usage experiences (Bhattacherjee, 2001). If a process modeling grammar in use outperforms initial expectations (that may have been influenced by others’ opinions, or by information disseminated through mass media and other communication channels), post-adoption SAT will result. If an artifact falls short of expectations the user is likely to be dissatisfied (Oliver, 1980). These suggested links can be specified in the two following hypotheses:

H6: Process modelers’ perceived usefulness of a process modeling grammar is positively associated with their level of satisfaction with process modeling grammar use.

H7: Process modelers’ extent of confirmation is positively associated with their level of satisfaction with process modeling grammar use.

Following Bhattacherjee (2001), a link between CON and PU may also be present. Users may have low initial usefulness perceptions of a new process modeling grammar because they are unsure what to expect from its use. Nonetheless, they may still want to use it with the intent of making their usage experience a basis for forming more realistic perceptions. Although low initial usefulness perceptions are easily confirmed, such perceptions may increase over time as a result of the CON experience, if users realize that their initial perceptions were unrealistically low. Rational users may try to remedy the resulting dissonance by modifying their usefulness perceptions in order to be more consistent with reality. CON of expectations thus tends to elevate users’ PU, while disconfirmation of expectations will reduce such perceptions. We thus suggest the following hypothesis:

H8: Process modelers’ extent of confirmation is positively associated with their perceived usefulness of a process modeling grammar.

These eight hypotheses suggest a basic model of the determinants of process modeling grammar continuance on basis of an established body of knowledge in the context of IT usage studies (e.g., Kim & Malhotra, 2005; SeJoon et al., 2006; Thong et al., 2006; Premkumar & Bhattacherjee, 2008). This model is shown on the righthand side of Figure 1. In the following, we extend this model by considering individual difference factors that we extracted from prior literature on human factors in IT usage and process modeling.

For the purpose of this study, individual difference factors include those situational variables that are attributed to personal circumstances (such as experience and training). The notion that such individual difference factors play a key role in forming acceptance and usage behaviors is widely recognized (e.g., Chau, 1996; Shanks, 1997; Agarwal & Prasad, 1999; Lee & Truex, 2000; Gemino & Wand, 2005). Yet, to date, research has not comprehensively examined the relationships that link individual difference factors to post-adoptive continued usage behavior.

The most prevalent individual difference factor that has been investigated is that of experience. Different studies in both modeling (e.g., Batra & Davis, 1992; Agarwal et al., 1996b; Shanks, 1997) and IT usage domains (e.g., Agarwal & Prasad, 1999; Castan˜eda et al., 2007) investigated user-experience levels (e.g., novice vs expert) across different task settings. These studies found noticeable links between user experience and task conduct as well as task performance. Similar situations have also been noted in the process modeling context specifically (Green & Rosemann, 2001; Recker et al., 2006). Experienced modelers often possess a repertoire of workarounds for challenging modeling situations, and can often refer to their previous experiences and knowledge about modeling when applying a grammar for a complex modeling tasks. Less experienced modelers, on the other hand, often lack such knowledge, which, in turn, may affect their perceptions about the utility of the grammar at hand.

Resource allocation theory (Kanfer et al., 1994) suggests that when users build up experience in modeling, their demands for cognitive attentional effort required to perform the modeling tasks with a grammar is reduced, thereby freeing cognitive resources that can be allocated to improving task skills and outcome production. This situation would suggest that experienced modelers can use a grammar with less effort. This allows the modelers to redirect freed effort to model faster, thereby potentially improving perceptions about the ease of use of the grammar. The freed efforts can further be redeployed to improve the effectiveness of grammar use, because more effort can be dedicated to the objective of creating highquality process models with the grammar. In turn, the user’s perception of the relative utility (i.e., the usefulness) of the grammar is also likely to be improved. Accordingly, we speculate:

H9: Process modelers’ extent of process modeling experience is positively associated with their perceived usefulness of a process modeling grammar.

H10: Process modelers’ extent of process modeling experience is positively associated with their perceived ease of use of a process modeling grammar.

Aside from actual modeling experience, it is important to consider the level of grammar familiarity that users of a process modeling grammar bring to bear. Gemino & Wand (2004) suggested to consider that some participants may have high levels of self-perceived modeling grammar knowledge, leading to different behaviors in the modeling process. For example, technical analysts typically possess a high level of familiarity with the particular grammar they already use (Morris et al., 1999). Similarly, Parsons & Cole (2005) showed empirically how familiarity can affect modeling results under some treatment conditions.

Familiarity with a modeling grammar is closely related to the notion of self-efficacy. It measures what individuals believe about their own levels of modeling capability with a given grammar. Self-efficacy theory shows how self-beliefs about skills and abilities affects individual performance and the development of behavioral beliefs (e.g., Gist & Mitchell, 1992; Johnson & Marakas, 2000; Yi & Davis, 2003), which suggests that self-perceived familiarity may also affect individual beliefs associated with the usage of a process modeling grammar.

Specifically, congruent with prior research (e.g., Thompson et al., 1994; Igbaria et al., 1995) we expect a positive association between familiarity with ease of use. Users that deem themselves knowledgeable and experienced with a grammar are more likely to find the grammar less complex in its use. Similarly, we expect that more familiar grammar users will be more likely to be satisfied with the use of the grammar. This is because users with high grammar familiarity are more likely to believe that they can realize expected benefits from the grammar use more quickly, leading to increased SAT beliefs. We summarize these observations in the following two hypotheses:

H11: Process modelers’ perceived process modeling grammar familiarity is positively associated with their perceived ease of use of a process modeling grammar.

H12: Process modelers’ perceived process modeling grammar familiarity is positively associated with their level of satisfaction with process modeling grammar use.

Last, we consider the background of the process modeler (e.g., business analyst vs technical analyst) working with the grammar at hand. Our own experiences and observations of process modeling practice indicate that the analyst teams are typically composed of users with either an IT-oriented study and work experience background (viz., technical analysts, system designer, IT managers and the like), or with users from a business background (viz., business analysts, HR managers, department directors and the like).

Theoretically, the educational background of a modeler is indicative of the user’s extent of previous domain knowledge (Shaft & Vessey, 1998; Khatri et al., 2006). It was found that different types of background knowledge influence the way problem-solving tasks such as computer program comprehension (Shaft & Vessey, 1998) or, indeed, modeling (Khatri et al., 2006) are being conducted. Similar situations have been also noted in the process modeling literature (Dehnert & van der Aalst, 2004; Rosemann, 2006). These findings suggest that differences in modelers’ background knowledge could also manifest in different post-adoptive usage behaviors when working with process modeling grammars. For instance, Green & Rosemann (2001) found in their study of process modeling practice that the individual background of the modelers they interviewed influenced the way process modeling was being applied, and the way the process modeling grammar under observation was being used. Similarly, Recker et al. (2006) found in their interviews of process modeling grammar adopters that the background of a user, that is, whether the modeler had a business- or IT-oriented background, determined their understanding and interest towards process modeling, as well as their actual usage of the process modeling grammar under observation. Most notably, in the interviews conducted, Recker et al. (2006) uncovered that differences in the individual backgrounds manifested in different perceptions about the strengths of weaknesses of the process modeling grammar in use.

Similar to the differences in background knowledge between the grammar users, the grammars to be used for process modeling also are either IT- or business-oriented (Phalp, 1998; Rosemann et al., 2006; Recker, 2007; Soffer & Wand, 2007). This means, available grammars were either developed for more business-oriented application areas such as training, stakeholder communication, process improvement or business analysis, or for more IT-oriented application areas such as process simulation, workflow implementation or IT systems design (Dehnert & van der Aalst, 2004). The BPMN grammar, for example, was explicitly intended to support IT-oriented application areas, such as, for instance, to facilitate zero-code workflow implementation (Ouyang et al., 2009) or web service design (Rabhi et al., 2007).

We expect that perceptions about the usage of the grammar will be influenced by the extent to which the application orientation (business- vs IT-oriented) of a process modeling grammar matches the type of background knowledge (again, business- vs IT-oriented) of the grammar user. More specifically, in the case of the BPMN grammar we consider in our study, we expect that the more technical orientation of the grammar will resonate more positively with grammar users from an IT-oriented background. We expect thus that IT-oriented modelers will have higher perceptions of the usefulness and ease of use of the grammar. Generally, we expect that if the application orientation of a process modeling grammar matches the abilities and skills of a grammar user, then perceptions of the utility of the grammar (i.e., its usefulness and ease of use) are likely to improve:

H13: Process modelers with IT-oriented background knowledge show a positive association with their perceived ease of use of the IT-oriented BPMN process modeling grammar.

H14: Process modelers with IT-oriented background knowledge show a positive association with their perceived usefulness of the IT-oriented BPMN process modeling grammar.

We also contend that the different user communities (business- vs IT-oriented users) may have different expectations towards the use of a grammar. For instance, users with a business background may have low initial usage expectations of an IT-oriented grammar. This may be because they expect a steep learning curve in applying an IT-oriented grammar, or because they expect that an IT-oriented grammar may not be useful for businessoriented application areas such as process documentation, knowledge management or organizational re-design. Such initial expectations will be positively or negatively (dis-) confirmed through actual usage experiences. Indeed, if the grammar proves to be oriented towards technical application areas, then low expectations will be positively confirmed by business-oriented users. Conversely, high expectations by IT-oriented users may be positively confirmed if an IT-oriented grammar proves to be useful for IT-oriented modeling tasks such as process simulation or workflow specification. Accordingly, the following hypothesis is suggested:

H15: Process modelers with IT-oriented background knowledge show a positive association with their perceived confirmation of expectation about the use of the IT-oriented BPMN process modeling grammar.

In summary, the research model shown in Figure 1 suggests a comprehensive model of process modeling grammar continuance, and synthesizes prior research on IS continuance with research on individual difference factors pertinent to process modeling.

## Research method

To test our research model, we collected empirical data through a field survey of users of the process modeling grammar BPMN (BPMI.org & OMG, 2006). We selected the survey research method because it facilitates rigorous hypothesis testing through a sample size bigger than, for example, case studies (Gable, 1994). Also, survey research has the potential to produce generalizable results that can be applied to populations other than the sample tested (King & He, 2005). This can be of benefit to the present study to draw conclusions about process modeling grammar users in general. Pinsonneault & Kraemer (1993) state that survey research is appropriate when clearly identified independent and dependent variables exist, and a specific model is present that theorizes the relationships between the variables. This situation is given in the present study.

Data were collected globally from BPMN grammar users via a web-based instrument during 2007 and 2008. Webbased surveys are advantageous over paper-based surveys in several ways. Specifically, there is empirical evidence to suggest that web-based surveys are cheaper than postal surveys and yield responses that are faster, more complete and more accurate (Schaefer & Dillman, 1998; Klassen & Jacobs, 2001). Also, web-based surveys offer the potential of overcoming geographical boundaries and collecting data globally. This was deemed of relevance to the present study, to incorporate the viewpoints of BPMN users from a wide variety of cultural, national, organizational and personal settings. This was deemed important due to the specific focus of this research on individual difference factors of grammar users. Last but not least, web-based surveys offer the additional advantages of real-time response validation and automated data entry, which were deemed beneficial to the execution of this research. All these advantages have resulted in web-based surveys becoming widely used in IS research (e.g., Bhattacherjee, 2001; Castan˜eda et al., 2007), as well as being the research method of choice in the present study.

We selected the BPMN grammar as a target grammar to study for several reasons. BPMN has been ratified as an official industry standard through the standards body Object Management Group, in cooperation with the industry consortium BPMI.org. Since its release in 2006, BPMN has quickly become a widely adopted standard for process modeling (zur Muehlen & Recker, 2008; Recker, 2010). BPMN is widely supported by both free and commercial process modeling tools (e.g., Pega, Sparxsystems, Telelogic, Intalio, itp-commerce, Tibco, IBM Websphere, Sungard). BPMN education is integrated into the curriculum of many education providers (e.g., Widener University, Queensland University of Technology and Howe School of Technology Management), and part of the offerings of modeling coaches and consultants (e.g., Object Training, BPM-Training.com and BPMInstitute .org). Even other standardization bodies (e.g., the Workflow Management Coalition – WfMC) have revised their standard development efforts to incorporate BPMN (Workflow Management Coalition, 2008). All these characteristics make BPMN a suitable target for the present study.

It is important to note that BPMN was developed primarily for technical application areas, including tasks such as web services specification, workflow design, systems implementation and the like (BPMI.org & OMG, 2006; Ouyang et al., 2008; Ouyang et al., 2009). Recent reports (Recker, 2010), however, suggest that BPMN has also enjoyed significant uptake in businessoriented process modeling communities, and is also used for tasks such as staff training, process documentation or organizational re-engineering.

Because of the objective of the study to evaluate the differences between business- and IT-oriented users of the BPMN grammar that was primarily designed for technical application areas, the target population for this study were both business and technical analysts engaged in process modeling initiatives that had knowledge of, and usage experience with, the BPMN grammar specifically. Users were invited globally to participate in the online survey through advertisements made in online forums and blogs (e.g., WordPress, BPM-research.com, Column2), through modeling tool vendor announcements (e.g., itp-Commerce, IDS Scheer, Casewise, Tibco, Intalio) and through practitioner magazines and communities (e.g., BPTrends.com, ABPMP, BPM-Netzwerk). Participants were informed about type and nature of the study and were offered incentives for participations, including a summary of the results and the chance to win a free textbook.

In total, 529 usable responses were obtained. Table 1 summarizes key organizational and personal demographics of the respondent population. The geographic distribution of these respondents mirrors the general distribution of process practitioners worldwide (Wolf & Harmon, 2006). Europe, North America and Oceania account for almost three quarters of all responses (see Table 1). Almost 60% of respondents worked for private sector companies. More than 40% of respondents worked in large organizations with more than 1000 employees, while 22.7% and 26.8% of respondents work for middleand small-sized organizations, respectively. The organizational distribution of BPMN modelers closely mirrors the survey of process practitioners reported in Wolf & Harmon (2006), who report a somewhat similar organizational distribution (28%, 33% and 41%, respectively, for small-, medium- and large-sized organizations). The size of the process modeling team, in which respondents work as process modelers, ranges from less than 10 members (64.4% of respondents) to more than 50 members (3.8% of respondents). This would suggest that, even in large corporations, the team of employees dedicated to BPMN modeling is small.

Table 1 Participant demographic data

<table><tr><td>Aspect</td><td>Values</td><td># of responses</td></tr><tr><td colspan="3">Organizational demographics</td></tr><tr><td rowspan="2">Type</td><td>Public sector</td><td>186</td></tr><tr><td>Private sector</td><td>343</td></tr><tr><td rowspan="3">Size</td><td>Less than 100</td><td>158</td></tr><tr><td>Between 100 and 1000</td><td>134</td></tr><tr><td>More than 1000</td><td>237</td></tr><tr><td rowspan="3">Size of modeling team</td><td>Less than 10</td><td>379</td></tr><tr><td>Between 10 and 50</td><td>128</td></tr><tr><td>More than 50</td><td>22</td></tr><tr><td colspan="3">Personal demographics</td></tr><tr><td rowspan="6">Continent of origin</td><td>Africa</td><td>14</td></tr><tr><td>Asia</td><td>36</td></tr><tr><td>Europe</td><td>175</td></tr><tr><td>North America</td><td>133</td></tr><tr><td>Oceania</td><td>131</td></tr><tr><td>South America</td><td>40</td></tr><tr><td rowspan="7">Type of training</td><td>Formal/certified course</td><td>56</td></tr><tr><td>Internal/in-house course</td><td>30</td></tr><tr><td>University course</td><td>24</td></tr><tr><td>On the job training</td><td>78</td></tr><tr><td>Learnt by myself</td><td>212</td></tr><tr><td>Read the specification</td><td>116</td></tr><tr><td>Other</td><td>13</td></tr></table>

In terms of process modeling experience, Table 2 shows that respondents appear to fall into four equally large clusters, those with very little experience, with some experience, with substantial experience and with great experience. The distribution of these categories roughly matches the distribution of conceptual modelers in terms of modeling experience, as reported in (Davies et al., 2006). The reported average amount of experience in process modeling was 6.4 years. Experience in modeling with BPMN specifically ranged from 15 days to 5 years (with an average of 9 months and a median of 4 months). Interestingly, roughly half of the responses were obtained from modelers with less than 6 months experience in the grammar. The limited amount of BPMN experience is most likely due to its only recent release as an OMG standard. While BPMN has been available in version 0.9 since 2002, ratification as a standard was only finalized in late 2006 (BPMI.org & OMG, 2006). Hence, it was to be expected that the distribution of respondents in terms of BPMN experience would somewhat deviate from their distribution in terms of overall experience.

Before administering the field study we ran a pre-test and a pilot test. In the pre-test four academics with knowledge of the study were asked to complete a paperbased version of the survey instrument in face-to-face meetings. During survey completion, notes were taken based on comments received. After instrument revision, the measurement instrument was pilot-tested with a sample of 41 post-graduate students with knowledge of the BPMN grammar. After exploratory factor analysis, changes were made to the design of the survey instrument and to those scales that indicated problems in meeting required psychometric properties. Attention was specifically paid to the scales that were newly constructed for this study (i.e., modeling experience and background knowledge).

## Operationalization and validation

## Construct measurement

Seven of the eight constructs specified in our research model were measured using three-item perceptual Likerttype scales, drawn from pre-validated measures where possible. Modeling experience was measured by using respondents’ self-reported estimates. All scale items were phrased to relate specifically to the case of BPMN process modeling grammar use. The appendix lists all scale items used.

The scale for familiarity was adopted from Gemino & Wand’s (2005) familiarity with an analysis method scale. The scale assesses familiarity with the (BPMN) process modeling grammar in a sense of generally felt familiarity (FAM1), self-perceived competence (FAM2) and selfperceived confidence (FAM3). All items are worded in the form of a statement to which a respondent can be asked to indicate his/her extent of agreement on a 7-point Likert scale with the end points ‘strongly disagree’ and ‘strongly agree’.

Experience is a well-established variable in conceptual modeling studies. Four measures are typically used: selfassessment by the respondents, classification of respondents by the researcher, number of models developed and years of experience. Of these, only the latter two are of relative objectiveness, and avoid – to some extent – individual response bias. In addition to these two measurements, Gemino & Wand (2004) comment that in reality, there is a wide degree of variation in the level of modeling experience exhibited by practitioners. For example, a business analyst may be experienced with one modeling grammar but possess little or no knowledge of others. They thus recommend including a measure of the modeler’s expertise with a particular grammar under observation, in addition to general measures of overall modeling experience. Accordingly, in line with similar studies in other conceptual modeling domains (Gemino & Wand, 2005; Davies et al., 2006), three measures were used in the present study to operationalize modeling experience:

Table 2 Participant experience in process modeling and with BPMN

<table><tr><td>Type of experience</td><td>Frequency</td><td>Min</td><td>Max</td><td>Median</td><td>Mean</td><td>SD</td></tr><tr><td>Years of experience in process modeling overall</td><td>529</td><td>0.2</td><td>30</td><td>5</td><td>6.399</td><td>5.803</td></tr><tr><td>Less than 2 years experience</td><td>159</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Between 2 and 5 years experience</td><td>164</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Between 5 and 10 years experience</td><td>116</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>More than 10 years experience</td><td>90</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Months of experience in process modeling with BPMN</td><td>529</td><td>0.5</td><td>60</td><td>4</td><td>8.987</td><td>11.095</td></tr><tr><td>Less than 6 months experience</td><td>294</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Between 6 and 12 months experience</td><td>133</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Between 12 and 24 months experience</td><td>62</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>More than 24 months experience</td><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Number of BPMN models created</td><td>529</td><td>1</td><td>1800</td><td>15</td><td>52.308</td><td>150.852</td></tr><tr><td>Less than 10 models created</td><td>170</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Between 10 and 25 models created</td><td>167</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Between 25 and 50 models created</td><td>99</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>More than 50 models created</td><td>93</td><td></td><td></td><td></td><td></td><td></td></tr></table>

\- Self-reported approximate number of years experience in process modeling overall (EXP1);

\- self-reported approximate number of months experience with a particular process modeling grammar (EXP2); and

\- self-reported approximate number of process models created with a particular process modeling grammar (EXP3).

Regarding background knowledge, prior studies as well as our own experiences and observations suggest that process modelers can be separated in two broad categories, viz., process modelers coming from an IT-oriented background (aka technical analysts) and process modelers coming from a business-oriented background (aka business analysts). Accordingly, a three-item scale was developed to differentiate respondents into these two categories, based on the self-perception of their role in a process modeling initiative (BGD1), the orientation of their expertise in process modeling (BGD2) and their educational background in process modeling (BGD3). All items were worded in the form of a statement to which a respondent can be asked to indicate his/her extent of agreement on a 7-point Likert scale with the end points ‘Business-oriented’ (coded as a ‘1’) and ‘IT-oriented’ (coded as a ‘7’) and, with a middle anchor point ‘both’.

PU was measured using three items adopted from Davis’ (1989) original scale. One item (PU1) taps into an overall judgment of usefulness while the remaining two items assess usefulness (in a sense of effectiveness) in explicit relation to the domain substrata process modeling purpose (PU2) and objective (PU3).

PEOU was measured using three items adopted from Davis’ (1989) original scale. PEOU embraces two domain substrata ‘effort of use’ and ‘effort of learning’. Effort of use relates to the physical and mental efforts required to build process models by means of the process modeling grammar in use while ease of learning taps into the efforts required for remembering how to perform tasks, how to use an artifact and how to use a manual if existent. Accordingly, the three selected items include one item to measure the effort of applying a process modeling grammar for process modeling in relation to the intended use (PEOU1), one item to measure the effort of learning how to apply a process modeling grammar (PEOU2) and one item to measure the effort of performing process modeling tasks with the grammar, that is, the effort of building process models (PEOU3).

CON was measured using three items adopted from Bhattacherjee & Premkumar’s (2004) scale. CON refers to the extent to which respondents’ pre-usage expectations of usage are contravened during actual usage experiences. Expected benefits from process modeling grammar use are captured in the three items of the PU scale (usefulness overall, in relation to purpose, in relation to objectives), and CON is assessed using three perceptual items that compare respondents’ realized levels of each usefulness item (as a surrogate for expected benefits) against their pre-usage expected levels.

SAT was measured using three items adopted from the overall SAT scale suggested by Spreng et al. (1996). Their scale was originally designed to assess users’ SAT with camcorder use but has since been validated in the IS context (e.g., Bhattacherjee, 2001; Bhattacherjee & Premkumar, 2004; Premkumar & Bhattacherjee, 2008). The adopted scale captures respondents’ SAT levels (both in intensity and direction) along three semantic dimensions of SAT, these being contention (SAT1), satisfaction (SAT2) and delightedness (SAT3).

Intention to continue to use was measured using three items adopted from Bhattacherjee’s (2001) scale. Three domain substrata are included in the scale. One item (ItU1) captures respondents’ intention to continue process modeling grammar use, one item (ItU2) measures future usage intentions by using future tense and one item (ItU3) measures continuance intention in relation to potentially available alternative process modeling grammars.

## Scale validation

Scale reliability and validity for the eight considered constructs was assessed via confirmatory factor analysis (CFA) techniques implemented in LISREL Version 8.80. CFA is recommended over exploratory factor analysis in cases with strong a priori theory, a focus on theory testing and pre-validated scales, as were mostly the case in the present study (Bagozzi & Phillips, 1982). All scale items were modeled as reflective indicators of their hypothesized latent constructs. All constructs were allowed to covary in the CFA model. Table 3 gives the CFA results, Table 4 displays scale properties and Table 5 gives the corresponding factor correlation matrices.

Based on the data obtained and displayed in Tables 3, 4 and 5, four tests can be performed. Regarding unidimensionality, Cronbach’s a should be greater than or equal to 0.7 to consider items to be uni-dimensional and to be combinable in an index (Nunnally & Bernstein, 1994). Table 4 shows that all constructs have a of at least 0.8, thereby meeting the test of uni-dimensionality. Note that Cronbach’s a was not computed for the Experience (EXP) construct due to the continuous nature of the scale. However, a separate Principal Component Analysis showed that all EXP scale items loaded higher own the

Table 3 Confirmatory factor analysis (CFA) results

<table><tr><td>Scale item</td><td>Item mean</td><td>Item SD</td><td>Item loading</td><td>Sig.</td></tr><tr><td>EXP1</td><td>6.39</td><td>5.810</td><td>0.715</td><td>0.000</td></tr><tr><td>EXP2</td><td>9.01</td><td>11.108</td><td>0.637</td><td>0.000</td></tr><tr><td>EXP3</td><td>52.45</td><td>151.121</td><td>0.626</td><td>0.000</td></tr><tr><td>BGD1</td><td>3.61</td><td>1.673</td><td>0.825</td><td>0.000</td></tr><tr><td>BGD2</td><td>3.91</td><td>1.646</td><td>0.899</td><td>0.000</td></tr><tr><td>BGD3</td><td>3.80</td><td>1.693</td><td>0.873</td><td>0.000</td></tr><tr><td>FAM1</td><td>5.46</td><td>1.226</td><td>0.927</td><td>0.000</td></tr><tr><td>FAM2</td><td>5.21</td><td>1.329</td><td>0.942</td><td>0.000</td></tr><tr><td>FAM3</td><td>5.42</td><td>1.326</td><td>0.946</td><td>0.000</td></tr><tr><td>PU1</td><td>6.04</td><td>1.015</td><td>0.822</td><td>0.000</td></tr><tr><td>PU2</td><td>5.94</td><td>1.031</td><td>0.813</td><td>0.000</td></tr><tr><td>PU3</td><td>5.50</td><td>1.580</td><td>0.776</td><td>0.000</td></tr><tr><td>SAT1</td><td>5.22</td><td>1.244</td><td>0.807</td><td>0.000</td></tr><tr><td>SAT2</td><td>5.12</td><td>1.268</td><td>0.811</td><td>0.000</td></tr><tr><td>SAT3</td><td>4.79</td><td>1.453</td><td>0.787</td><td>0.000</td></tr><tr><td>CON1</td><td>4.98</td><td>1.174</td><td>0.848</td><td>0.000</td></tr><tr><td>CON2</td><td>5.00</td><td>1.248</td><td>0.864</td><td>0.000</td></tr><tr><td>CON3</td><td>4.93</td><td>1.273</td><td>0.851</td><td>0.000</td></tr><tr><td>PEOU1</td><td>5.17</td><td>1.292</td><td>0.787</td><td>0.000</td></tr><tr><td>PEOU2</td><td>5.10</td><td>1.330</td><td>0.872</td><td>0.000</td></tr><tr><td>PEOU3</td><td>5.10</td><td>1.314</td><td>0.875</td><td>0.000</td></tr><tr><td>ItU1</td><td>6.04</td><td>0.928</td><td>0.800</td><td>0.000</td></tr><tr><td>ItU2</td><td>6.06</td><td>0.877</td><td>0.824</td><td>0.000</td></tr><tr><td>ItU3</td><td>5.62</td><td>1.292</td><td>0.738</td><td>0.000</td></tr></table>

Table 4 Scale properties

<table><tr><td>Construct</td><td>Mean</td><td>SD</td><td>Cronbach&#x27;s α</td><td> $\rho_c$ </td><td>AVE</td></tr><tr><td>EXP</td><td>67.69</td><td>154.230</td><td>N/A</td><td>0.672</td><td>0.823</td></tr><tr><td>BGD</td><td>11.33</td><td>4.435</td><td>0.863</td><td>0.807</td><td>0.890</td></tr><tr><td>FAM</td><td>16.08</td><td>3.673</td><td>0.943</td><td>0.900</td><td>0.946</td></tr><tr><td>PU</td><td>17.48</td><td>3.294</td><td>0.865</td><td>0.824</td><td>0.910</td></tr><tr><td>SAT</td><td>15.14</td><td>3.719</td><td>0.929</td><td>0.871</td><td>0.939</td></tr><tr><td>CON</td><td>14.91</td><td>3.535</td><td>0.953</td><td>0.911</td><td>0.957</td></tr><tr><td>PEOU</td><td>15.37</td><td>3.600</td><td>0.902</td><td>0.842</td><td>0.918</td></tr><tr><td>ItU</td><td>17.72</td><td>2.830</td><td>0.882</td><td>0.838</td><td>0.921</td></tr></table>

EXP construct, as theorized, than on any other construct, thereby also meeting the requirement of uni-dimensionality (Tabachnick & Fidell, 2001).

Reliability refers to the internal consistency of a measurement instrument. Again, the most widely used test for internal consistency is Cronbach’s $\alpha ,$ which – as a measure of reliability – should be higher than 0.8 (Nunnally & Bernstein, 1994). A second test uses the composite reliability measure $\rho _ { c } ,$ which represents the proportion of measure variance attributable to the underlying trait. Scales with $\rho _ { c }$ greater than 0.5 are considered to be reliable (Jo¨reskog et al., 2001). Table 4 shows that all constructs obtained a of at least 0.8 and also well exceed the required $\rho _ { c }$ cut-off value of 0.5. Again note the case of the EXP. While a was not computed, it met the test of composite reliability $( \rho _ { c } { = } 0 . 6 7 2 )$ . These results suggest adequate reliability.

Table 5 Inter-construct correlations

<table><tr><td></td><td>EXP</td><td>BGD</td><td>FAM</td><td>PU</td><td>SAT</td><td>CON</td><td>PEOU</td><td>ItU</td></tr><tr><td>EXP</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BGD</td><td>0.365</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FAM</td><td>0.255</td><td>0.212</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PU</td><td>0.544</td><td>0.326</td><td>0.375</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>SAT</td><td>0.657</td><td>0.489</td><td>0.350</td><td>0.634</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>CON</td><td>-0.093</td><td>-0.085</td><td>0.047</td><td>-0.099</td><td>-0.065</td><td>1.000</td><td></td><td></td></tr><tr><td>PEOU</td><td>0.457</td><td>0.137</td><td>-0.013</td><td>0.413</td><td>0.507</td><td>-0.032</td><td>1.000</td><td></td></tr><tr><td>ItU</td><td>0.444</td><td>0.101</td><td>0.263</td><td>0.351</td><td>0.373</td><td>-0.169</td><td>0.288</td><td>1.000</td></tr></table>

Convergent validity tests if measures that should be related are in fact related. Convergent validity can be tested using three criteria suggested by Fornell & Larcker (1981): (1) all indicator factor loadings (l) should be significant and exceed 0.6, (2) construct composite reliabilities $\rho _ { c }$ should exceed 0.8 and (3) average variance extracted (AVE) by each construct should exceed the variance due to measurement error for that construct (i.e., AVE should exceed 0.500). Table 3 shows that all factor loadings (l) are significant at $P { = } 0 . 0 0 0$ and exceed the recommended threshold of 0.6. In terms of composite reliabilities, Table 4 shows that $\rho _ { c }$ exceeded 0.8 for all constructs but EXP. As reported in Table $^ { 4 , }$ AVE for each construct is higher than 0.8 suggesting that for all constructs AVE well exceeded the variance due to measurement error. Overall, it is concluded that the conditions for convergent validity were met – only EXP remained a problematic case. However, given that EXP well exceeded the recommended $\rho _ { c }$ value of 0.5 for composite reliability, and given that EXP well passed the remaining two tests for convergent validity, it was decided to retain the construct – also due to its expected importance to the suggested theoretical model.

Discriminant validity tests if measures that should not be related are in fact unrelated. Fornell & Larcker (1981) recommend a test of discriminant validity, where the AVE for each construct should exceed the squared correlation between that and any other construct considered in the factor correlation matrix.

In the present study, the factor correlation matrix reported in Table 5 indicates that the largest squared correlation between any pair of constructs within the measurement model is 0.657 (between SAT and EXP). The smallest obtained AVE value is 0.823 (EXP). These results suggest that the test of discriminant validity is met.

## Data analysis and results

Our data analysis concerned the examination of the introduced research model, in terms of the significances and effect sizes (b) for each hypothesized path and variance explained $( R ^ { 2 } )$ for each dependent variable. Data analysis was carried out using structural equation modeling (SEM) implemented in LISREL Version 8.80 ( Jo¨reskog & So¨rbom, 2001). SEM is particularly appropriate for testing theoretically justified models (Gefen et al., 2000), as was the case in this study. Each indicator was modeled in a reflective manner (as in the measurement model), and the theoretical constructs were linked as hypothesized (see Figure 1). Results of our examinations of the suggested hypotheses are presented in Figure 2. Goodness of fit statistics for the model are reported in Table $^ { 6 , }$ and suggest adequate fit of the model to the data, as well as a comparison to the determinants model alone.

The research model explained 55.7% of the variance in intention to continue using the process modeling grammar, 60.3% of the variance in SAT with process modeling grammar use, 38.8% of the variance in ${ \mathrm { P U } } ,$ 27.3% of the variance in PEOU and 12.2% of the variance in CON of expectations.

Examining the 15 hypothesized paths in the model, we find that all but one (the link between modeling experience and PEOU) hypothesized paths were statistically significant, with one path (between modeler background and PEOU) being significant at $P { < } 0 . 0 5 ,$ three paths (between modeler background and CON and PU, respectively, and between modeling experience and PU) being significant at $P { < } 0 . 0 1$ and all other paths being significant at $P { < } 0 . 0 0 1$ . The directionality (positive or negative) of all but two paths were also as hypothesized, with the links between modeler background and PEOU, and CON, showing a negative directionality – contrary to our expectations.

Intention to continue to use the BPMN process modeling grammar was predicted positively by PU $( \beta = 0 . 4 8 6 )$ , PEOU $( \beta = 0 . 2 5 6 )$ and SAT $( \beta = 0 . 1 7 4 )$ , lending support to hypotheses H1 – H3. These results confirm earlier findings (SeJoon et al., 2006; Thong et al., 2006; Premkumar & Bhattacherjee, 2008) that speculated the relative importance of SAT beliefs as well as utility beliefs (i.e., PU and PEOU) to the formation of continuance behaviors.

SAT was predicted by CON (b ¼ 0.424), PU $( \beta = 0 . 2 3 7 )$ Familiarity $( \beta = 0 . 1 9 9 )$ and PEOU $( \beta = 0 . 1 8 1 )$ , as hypothesized in H5 – H7 and H13. PU was predicted by CON $( \beta = 0 . 5 0 1 )$ PEOU (b ¼ 0.225), Modeling Experience $( \beta = 0 . 1 6 2 )$ and Modeler Background $( \beta = 0 . 1 2 6 )$ , providing support for hypotheses H4, H8, H9 and H14. PEOU was positively predicted by Familiarity $( \beta = 0 . 5 1 9 )$ , as speculated in hypothesis H11, but not by Modeling Experience $( \beta = 0 . 0 5 9 , P { > } 0 . 0 5 )$ , thereby refuting hypothesis H10. Modeler Background had a negative direct effect on PEOU $( \beta = - 0 . 1 0 0 )$ contrary to the directionality suggested in hypothesis H13. Similarly, Modeler Background had a negative direct effect on CON $( \beta = - 0 . 1 0 0 )$ contrary to the directionality suggest in hypothesis H15.

Finally, we were interested in comparing the suggested extended continuance model with the basic continuance determinants model as suggested, for instance, in SeJoon et al. (2006) and Thong et al., 2006), and as shown in the right-hand side of Figure 2. The data obtained indicate that the extended model outperforms the original determinants model in terms of its explanatory power $( \mathrm { i . e . , }$ the $R ^ { 2 }$ value for intention to continue to use was higher at 0.557 compared to 0.413). To examine whether this increase is statistically significant, we conducted a nested F-test comparing the ${ \bf \ddot { \boldsymbol { R } } } ^ { 2 }$ value of the extended model with that of the determinants model alone. The F-test is the typical approach to compare nested models (Premkumar & Bhattacherjee, 2008). It evaluates the trade-off between a better fit and more complicated model (i.e., the increase in $R ^ { 2 }$ against the increase in degrees of freedom). It is computed as $F \ ( R _ { \mathrm { o u t e r } } ^ { 2 } { - } R _ { \mathrm { i n n e r } } ^ { 2 } ) /$ $[ ( 1 - R _ { \mathrm { i n n e r } } ^ { 2 } ) / d f _ { \mathrm { d i f f e r e n c e } } ]$ . We found the $R ^ { 2 }$ improvement of the extended model to be statistically significant from the determinants model alone (F (233, 152) ¼ 42.4668, Po0.0001). These findings attest to an improved explanatory ability of the extended model over and above the original determinants model.

![](/api/attachments/4NRX2JGU/fulltext/images/3655248548beb2f9c5ffbab2acbc1eac8a5d15b21c73c879afcd8d1f722bca20.jpg)  
Path Significance: \*\*\* p < 0.001, \*\* p< 0.01, \* p < 0.05, <sup>ns</sup> p > 0.05  
Figure 2 Summary of model results.

Table 6 Goodness of fit statistics

<table><tr><td>Fit index</td><td>Suggested value</td><td>Determinants model alone</td><td>Extended model</td></tr><tr><td>GFI</td><td>&gt;0.900</td><td>0.941</td><td>0.924</td></tr><tr><td>AGFI</td><td>&gt;0.900</td><td>0.913</td><td>0.907</td></tr><tr><td>NFI</td><td>&gt;0.900</td><td>0.985</td><td>0.967</td></tr><tr><td>NNFI</td><td>&gt;0.900</td><td>0.986</td><td>0.974</td></tr><tr><td>CFI</td><td>&gt;0.900</td><td>0.989</td><td>0.978</td></tr><tr><td>SRMR</td><td>&lt; 0.050</td><td>0.0451</td><td>0.0482</td></tr><tr><td>RMSEA</td><td>&lt; 0.080</td><td>0.0625</td><td>0.0597</td></tr><tr><td> $\chi^2 (df, p)$ </td><td>—</td><td>253.003 (81,0.00)</td><td>703.212 (233,0.00)</td></tr><tr><td> $\chi^2 / df$ </td><td>approx. 3</td><td>3.123</td><td>3.018</td></tr><tr><td> $R^2 for ItU$ </td><td>—</td><td>0.413</td><td>0.557</td></tr></table>

## Discussion

The objective of this study was to examine the utility of an extended model of continued process modeling grammar usage behavior. Data collected from an online survey of 529 current BPMN process modeling grammar users were used to test the model. The theoretical model demonstrated adequate fit with the data. Most causal relationships in the model were found to be significant as hypothesized. We identify a number of interesting results.

First, our findings are consonant with prior literature on technology acceptance and expectation-confirmation in that the prevalent determinant model of continuance behavior also holds in the domain of process modeling grammar continued usage behavior. The results of the study confirm earlier findings (e.g., Roca et al., 2006; SeJoon et $a l . ,$ 2006; Thong et al., 2006; Liao et al., 2007; Premkumar & Bhattacherjee, 2008) that suggested a hybrid model comprising constructs from technology acceptance and expectation-confirmation theories to be best for explaining and predicting post-adoptive usage intentions. The results indicate that the model suggested in Figure 1 provides a detailed understanding of the postadoptive behavior that unfolds during process modeling grammar usage experience. The model combines the strengths of both of its reference theories and hence provides support for the claim that a hybrid model is more useful for researchers interested in a deeper understanding of the process of continued usage experience. Specifically, the results confirm the relative importance of utility beliefs (usefulness and ease of use) to the formation of continued ItU, with SAT also being a strong predictor. The results further indicate a relative importance of the confirmation of initial expectations, which has strong implications to building SAT with use, as well as usefulness perceptions, in the process modeling context.

Second, the inclusion of individual difference factors significantly improved the explanatory power of the basic determinants model of process modeling grammar continuance. The extended model suggested in this study overall received good support from the data, with six of seven hypotheses being supported, with two hypotheses having a different directionality than expected. More specifically, we showed that familiarity with a process modeling grammar has significant influence on PEOU and SAT with the use, suggesting the importance of grammar knowledge to the experience of complexity in grammar application, and the formation of satisfactory usage experiences. We also showed that modeler experi ence has significant effects on the beliefs about the usefulness of a grammar, suggesting the relative importance of experience to the formation of positive instrumentality and utility beliefs about a grammar. Interestingly, modeling experience showed no significant effect on ease of use, suggesting that beliefs about the complexity of learning or usage associated with a grammar are not informed by the individual user, but instead can be speculated to be a function of the nature, feature or characteristics of the grammar itself.

Overall, these findings attest to the importance of adequate training in process modeling. Training serves to reduce uncertainty about a grammar by providing information about the features, nature and characteristics of the grammar. Greater learning thereby can amplify perceptions about the usage of a grammar in a positive direction. Also, greater learning can establish self-efficacy beliefs in the users, which also helps rectifying potential problems in the use of the grammar (as shown by the moderating effect of grammar familiarity). Our study suggests that it could be possible for organizations and individuals alike to increase user abilities in process modeling with the view to establishing positive usage beliefs.

We also showed significant effects of the type of modeler background (business- vs IT-oriented) on beliefs of ease of use, usefulness and confirmation of expectations. High values in modeler background (i.e., more IToriented users) tended to have lower perceptions about the ease of use of the BPMN grammar, and also showed a negative effect on the confirmation of their expectations. These findings suggest that, contrary to our expectations, and contrary to the voiced intention of the BPMN grammar to be designed for technical process modeling application areas (BPMI.org & OMG, 2006), it was especially business-oriented users that had positive ease of use beliefs and that were able to positively (dis-) confirm their pre-usage expectations. Conversely, our data suggest that modelers with an IT-oriented background had increased usefulness perceptions, that is, they found the BPMN grammar to be particularly useful for their (IT-oriented) process modeling tasks. Overall, these empirical findings provide some evidence for earlier speculations (Green & Rosemann, 2001; Dehnert & van der Aalst, 2004; Alter & Browne, 2005) that suggested that different types of process modelers approach process modeling tasks differently, use grammars differently and consequently have different beliefs about usage, performance and instrumentality.

## Future research

In this paper we have provided some evidence that theoretical models typically associated with the IS usage and acceptance domains can also be applied to reason about process modeling practice. Still, the findings from this study should be interpreted in light of its limitations. In our study we adopted constructs from prior literature (e.g., Davis, 1989; SeJoon et al., 2006; Premkumar & Bhattacherjee, 2008) and our own experience in the process modeling context. We contend that other antecedent factors of process modeling grammar continuance may exist that were not included in this study. For instance, individual difference factors such as self-efficacy (Ryan et al., 2000), habit (Limayem et al., 2007) or motivation (Venkatesh, 2000) have been shown to influence post-adoptive usage and may be expected to inform process modeling practice also. We also see a need to extend the research model further to also include factors pertaining to the nature of the grammar at hand, or the task-based setting in which a grammar is used. For instance, grammar characteristics such as correctness (Batra et al., 1990), structural complexity (Rossi & Brinkkemper, 1996) or ontological expressiveness (Recker et al., 2009) could inform differences in usage behaviors. Similarly, task characteristics such as organizational interventions (Orlikowski et al., 1995) or non-routineness (Goodhue, 1995) may warrant further attention.

Given the lack of pre-validated scales for modeling experience and modeler background, we created our own scales based on careful inspection of conceptual modeling and process modeling literature. Our operationalization was conducted specifically for the process modeling domain, which may limit the generalizability of the scales to other domains.

We also identify the choice of the target grammar (BPMN) as a potential source of limitation. Findings from the study relate to the chosen sample of BPMN grammar users and may not generalize to other process modeling grammar user groups as these user groups may perform different tasks, have different backgrounds or different usage beliefs about the grammars they use.

Our measurement strategy may further be susceptible to common method bias (Podsakoff et al., 2003). In particular, the data collection instrument makes large use of self-report measures, most notably in the context of measuring process modeling experience. However, it was attempted to overcome method bias by collating three different measures of modeling experience (years of modeling experience, months of grammar experience and number of models created) and explicitly separating experience from self-perceived experience (familiarity). Still, to further address this potential issue, alternative measures such as archival measures, primary or secondary observation, or process trace techniques could be employed in follow-up studies.

Last, we note that future studies could examine the utility, or integration, of other prevalent IS adoption, acceptance or usage theories in this domain. Theories of interest could include, for instance, task-technology-fit theory (Goodhue & Thompson, 1995) or cognitive fit theory (Vessey & Galletta, 1991). Prior research in the modeling domain (e.g., Agarwal et al., 1996a; Recker, 2007) has indicated the relevance notion of matchmaking, or fit (e.g., between user abilities and application orientation of the grammar, or between modeling artifact and application purpose) in the process modeling context, which could be further examined on the basis of the work presented in this paper.

## Practical implications

There are significant implications for the practitioner community of process modelers and their ecosystems including, among others, business analysts, workflow engineers, tool vendors as well as providers of training and developers of modeling grammars. The study findings provide an important contextualization of a fundamental decision – whether or not a process modeling grammar should be continued in its use. The study informs organizations how to set up a modeling environment in which analysts can work effectively and efficiently with a grammar. For example, organizations should be aware of usage expectations. The extent to which expectations can be confirmed – or not – has a significant impact on an individual’s willingness to continue working with this grammar. In general, the process modeling environment should be shaped in a way that it is easy for the analysts to learn and employ a process modeling grammar, so as to warrant satisfaction with its use. Furthermore, organizations should monitor how their analysts feel about the usefulness and effort of a modeling grammar in order to be able to make amendments or adjustments that increase the effectiveness or efficiency. This ongoing monitoring will ultimately lead to satisfied end users, who will hence work more willingly with a process modeling grammar.

Furthermore, the impact of training and grammar familiarity will be key to the development of perceptions about the usability and ease of a process modeling grammar. This situation should entice organizations to critically assess the modeling capabilities brought to bear by their analysts, and also the level of training they are able to – or seek to – provide. A second factor of relevance may well be the background of the individual modeler. Organizations should carefully monitor the domain and educational background brought to work in order to understand how these modelers feel about their use of a process modeling grammar.

## Conclusions

In this study, we contribute to post-adoptive usage research by providing empirical evidence of the utility of an extended continued usage model in the domain of

## About the author

Dr. Jan Recker is Senior Lecturer in the Information Systems Discipline and Leader of the Process Design research program at Queensland University of Technology. He received a B.Sc. IS and M.Sc. IS from the University of Muenster, Germany in 2004 and a Ph.D. in Information Systems from Queensland University of Technology in 2008. His main areas of research include methods and extensions for business process design and the usage of process design in organizational practice. He

AGARWAL R and KARAHANNA E (2000) Time flies when you’re having fun: cognitive absorption and beliefs about information technology usage. MIS Quarterly 24(4), 665–694.

## References

AGARWAL R and PRASAD J (1999) Are individual differences germane to the acceptance of new information technologies. Decision Sciences 30(2), 361–391.

AGARWAL R, SINHA AP and TANNIRU M (1996a) Cognitive fit in requirements modeling: a study of object and process methodologies. Journal of Management Information Systems 13(2), 137–162.

AGARWAL R, SINHA AP and TANNIRU M (1996b) The role of prior experience and task characteristics in object-oriented modeling: an empirical study. International Journal of Human-Computer Studies 45(6), 639–667.

ALTER S and BROWNE GJ (2005) A broad view of systems analysis and design: implications for research. Communications of the Association for Information Systems 16(50), 981–999.

BAGOZZI RP and PHILLIPS LW (1982) Representing and testing organizational theories: a holistic construal. Administrative Science Quarterly 27(3), 459–489.

BATRA D and DAVIS JG (1992) Conceptual data modelling in database design: similarities and differences between expert and novice designers. International Journal of Man-Machine Studies 37(1), 83–101.

BATRA D, HOFFLER JA and BOSTROM RP (1990) Comparing representations with relational and eer models. Communications of the ACM 33(2), 126-139.

process modeling. This study pushes the frontier of IS post-adoptive usage research further out to the process modeling domain, and provides this domain with the first reported empirical study of usage behaviors associated with modeling grammars. We examined the role of individual difference factors in the process of forming continued usage intentions. This study is the first reported attempt to extend theoretical models of postadoptive usage behavior based on expectation-confirmation theory with an analysis of individual difference factors. Our findings lead to an enhanced understanding of post-adoptive usage behaviors. In summation, our study has uncovered a rich and comprehensive first explanation of process modeling grammar usage behavior in the post-adoption stages, which can stimulate and guide further empirical research in this emerging relevant domain of IS practice.

BHATTACHERJEE A (2001) Understanding information systems continuance: an expectation-confirmation model. MIS Quarterly 25(3), 351–370.

has been the author of more than 75 journal articles and conference papers on these topics, including publications in the Journal of the Association for Information Systems, Information Systems, the Communications of the Association for Information Systems, the Australasian Journal of Information Systems, the Scandinavian Journal of Information Systems, and others. Dr. Recker is a member of the editorial board of two international journals and serves on the program committee of various IS conferences.

BHATTACHERJEE A and PREMKUMAR G (2004) Understanding changes in belief and attitude toward information technology usage: a theoretical model and longitudinal test. MIS Quarterly 28(2), 229–254.

BPMI.ORG AND OMG (2006) Business Process Modeling Notation specification. Final Adopted Specification. Object Management Group. [WWW document] http://www.bpmn.org.

BROWN SA, MASSEY AP, MONTOYA-WEISS MM and BURKMAN IR (2002) Do I really have to? User acceptance of mandated technology. European Journal of Information Systems 11(4), 283–295.

CASTAN<sup>˜</sup> EDA JA, MUN<sup>˜</sup> OZ-LEIVA F and LUQUE T (2007) Web acceptance mode (WAM): moderating effects of user experience. Information & Management 44(4), 384–396.

CHAU PYK (1996) An empirical investigation on factors affecting the acceptance of case by systems developers. Information & Management 30(6), 269–280.

CURTIS B, KELLNER MI and OVER J (1992) Process modeling. Communications of the ACM 35(9), 75–90.

D I, G P, R M, I M and G S (2006) How do practitioners use conceptual modeling in practice? Data & Knowledge Engineering 58(3), 358–380.

DAVIS FD (1989) Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly 13(3), 319–340.

DEHNERT J and VAN DER AALST WMP (2004) Bridging the gap between business models and workflow specifications. Internationgl lourngl of Cooperative Information Systems 13(3), 289–332.

DUMAS M, VAN DER AALST WMP and TER HOFSTEDE AHM (Eds) (2005) Process Aware Information Systems: Bridging People and Software Through Process Technology. John Wiley & Sons, Hoboken, New Jersey.

ERL T (2005) Service-Oriented Architecture: Concepts, Technology, and Design. Prentice Hall, Upper Saddle River, New Jersey.

FORNELL C and LARCKER DF (1981) Evaluating structural equations with unobservable variables and measurement error. Journal of Marketing Research 18(1), 39–50.

GABLE GG (1994) Integrating case study and survey research methods: an example in information systems. European Journal of Information Systems 3(2), 112–126.

GEFEN D, STRAUB DW and BOUDREAU M-C (2000) Structural equation modeling and regression: guidelines for research practice. Communications of the Association for Information Systems 4(7).

GEMINO A and WAND Y (2004) A framework for empirical evaluation of conceptual modeling techniques. Requirements Engineering 9(4), 248–260.

GEMINO A and WAND Y (2005) Complexity and clarity in conceptual modeling: comparison of mandatory and optional properties. Data & Knowledge Engineering 55(3), 301–326.

GIST ME and MITCHELL TR (1992) Self-efficacy: a theoretical analysis of its determinants and malleability. Academy of Management Review 17(2), 183–211.

GOODHUE DL (1995) Understanding user evaluations of information systems. Management Science 41(12), 1827–1844.

GOODHUE DL and THOMPSON RL (1995) Task-technology fit and individual performance. MIS Quarterly 19(2), 213–236.

GREEN P and ROSEMANN M (2001) Ontological analysis of integrated process models: testing hypotheses. Australasian Journal of Information Systems 9(1), 30–38.

GREGORIADES A and SUTCLIFFE AG (2008) A socio-technical approach to business process simulation. Decision Support Systems 45(4), 1017–1030.

IGBARIA M, GUIMARAES T and DAVIS GB (1995) Testing the determinants of microcomputer usage via a structural equation model. Journal of Management Information Systems 11(4), 87–114.

JASPERSON J, CARTER PE and ZMUD RW (2005) A comprehensive conceptualization of post-adoptive behaviors associated with information technology enabled work systems. MIS Quarterly 29(3), 525–557.

JOHNSON RD and MARAKAS GM (2000) Report: the role of behavioral modeling in computer skills acquisition – toward refinement of the model. Information Systems Research 11(4), 402–417.

Jo¨RESKOG KG and So¨RBOM D (2001) Lisrel 8: User’s Reference Guide. Scientific Software International, Lincolnwood, Illinois.

Jo¨ KG, So¨ D, D T S and D T M (2001) Lisrel 8: New Statistical Features. Scientific Software International, Lincolnwood, Illinois.

K R, A PL, M TC, D B and N L (1994) Goa setting, conditions of practice, and task performance: a resource allocation perspective. Journal of Applied Psychology 79(6), 826–835.

K M and V JM (2000) Drivers for software development method usage. IEEE Transactions on Engineering Management 47(3), 360–369.

KHATRI V, VESSEY I, RAMESH V, CLAY P and SUNG-JIN P (2006) Understanding conceptual schemas: exploring the role of application and is domain knowledge. Information Systems Research 17(1), 81–99.

KIM SS and MALHOTRA NK (2005) A longitudinal model of continued is use: an integrative view of four mechanisms underlying postadoption phenomena. Manggement Science 51(5). 741–755.

KING WR and HE J (2005) External validity in is survey research. Communications of the Association for Information Systems 16(45), 880–894.

KLASSEN RD and JACOBS J (2001) Experimental comparison of web, electronic, and mail survey technologies in operations management. Journal of Operations Management 19(6), 713–728.

LEE J and TRUEX DP (2000) Exploring the impact of training in ISD methods on the cognitive structure of novice information systems developers. Information Systems lournal 10(4), 347–367.

LEYMANN F and ROLLER D (2006) Modeling business processes with BPEL4WS. Information Systems and e-Business Management 4(3), 265–284.

LIAO C, CHEN J-L and YEN DC (2007) Theory of planning behavior (TPB) and customer satisfaction in the continued use of e-service: an integrated model. Computers in Human Behavior 23(6), 2804–2822.

LIMAYEM M, HIRT SG and CHEUNG CMK (2007) How habit limits the predictive power of intention: the case of information systems continuance. MIS Quarterly 31(4), 705–737.

MAES A and POELS G (2007) Evaluating quality of conceptual modelling scripts based on user perceptions. Data & Knowledge Engineering 63(3), 769–792.

MAHMOOD MA, BURN JM, GEMOETS LA and JACQUEZ C (2000) Variables affecting information technology end-user satisfaction: a meta-analysis of the empirical literature. International Journal of Human-Computer Studies 52(4), 751–771.

MORRIS MG, SPEIER C and HOFFER JA (1999) An examination of procedural and object-oriented systems analysis methods: does prior experience help or hinder performance? Decision Sciences 30(1), 107–136.

NUNNALLY JC and BERNSTEIN IH (1994) Psychometric Theory. McGraw-Hill, New York.

OLIVER RL (1980) A cognitive model for the antecedents and consequences of satisfaction. Journal of Marketing Research 17(4), 460–469.

ORLIKOWSKI WJ (1993) Case tools as organizational change: investigating incremental and radical changes in systems development. MIS Quarterly 17(3), 309–340.

ORLIKOWSKI WJ, YATES J, OKAMURA K and FUJIMOTO M (1995) Shaping electronic communication: the metastructuring of technology in use. Organization Science 6(4), 423–444.

OUYANG C, DUMAS M, TER HOFSTEDE AHM and VAN DER AALST WMP (2008) Pattern-based translation of BPMN process models to BPEL web services. International Journal of Web Services Research 5(1), 42–61.

OUYANG C, VAN DER AALST WMP, DUMAS M, TER HOFSTEDE AHM and MENDLING J (2009) From business process models to process-oriented software systems. ACM Transactions on Software Engineering Methodology 19(1), 2–37.

PARSONS J and COLE L (2005) What do the pictures mean? Guidelines for experimental evaluation of representation fidelity in diagrammatical conceptual modeling techniques. Data & Knowledge Engineering 55(3), 327–342.

PHALP KT (1998) The cap framework for business process modelling. Information and Software Technology 40(13), 731–744.

PINSONNEAULT A and KRAEMER KL (1993) Survey research methodology in management information systems: an assessment. Journal of Management Information Systems 10(2), 75–105.

P PM, M SB, L J-Y and P NP (2003) Common method bias in behavioral research: a critical review of the literature and recommended remedies. Journal of Applied Psychology 88(5), 879–903.

PREMKUMAR G and BHATTACHERJEE A (2008) Explaining information systems usage: a test of competing models. Omega 36(1), 64–75.

RABHI FA, YU H, DABOUS FT and WU SY (2007) A service-oriented architecture for financial business processes: a case study in trading strategy simulation. Information Systems and E-Business Management 5(2), 185–200.

RAMSEY HR, ATWOOD ME and VAN DOREN JR (1983) Flowcharts versus program design languages: an experimental comparison. Communications of the ACM 26(6), 445–449.

RECKER J (2007) A socio-pragmatic constructionist framework for understanding quality in process modelling. Australasian Journal of Information Systems 14(2), 43–63.

RECKER J (2010) Opportunities and constraints: the current struggle with BPMN. Business Process Management Journal 16(1), in press.

RECKER J, INDULSKA M, ROSEMANN M and GREEN P (2006) How good is BPMN really? Insights from theory and practice. In 14th European Conference on Information Systems (LJUNGBERG J and ANDERSSON M, Eds), pp 1582–1593, Association for Information Systems, Goeteborg, Sweden.

RECKER J, ROSEMANN M, INDULSKA M and GREEN P (2009) Business process modeling: a comparative analysis. lourngl of the Associgtion for Information Systems 10(4), 333–363.

ROCA JC, CHIU C-M and MARTINEZ FJ (2006) Understanding e learning continuance intention: an extension of the technology acceptance

model. International Journal of Human-Computer Studies 64(8), 683–696.

ROSEMANN M (2006) Potential pitfalls of process modeling: part A. Business Process Management Journal 12(2), 249–254.

ROSEMANN M, RECKER J, INDULSKA M and GREEN P (2006) A study of the evolution of the representational capabilities of process modeling grammars. In Advanced Information Systems Engineering – Caise 2006 (DUBOIS E and POHL K, Eds), pp 447–461, Springer, Luxembourg, Grand-Duchy of Luxembourg.

ROSSI M and BRINKKEMPER S (1996) Complexity metrics for systems development methods and techniques. Information Systems 21(2), 209–227.

RYAN SD, BORDOLOI B and HARRISON DA (2000) Acquiring conceptual data modeling skills: the effect of cooperative learning and self-efficacy on learning outcomes. ACM SIGMIS Database 31(4), 9–24.

SCHAEFER DR and DILLMAN DA (1998) Development of a standard e-mail methodology: results of an experiment. Public Opinion Quarterly 62(3), 378–397.

SCHEER A-W (2000) Aris – Business Process Modeling. Springer, Berlin, Germany.

SEJOON H, THONG JYL and TAM KY (2006) Understanding continued information technology usage behavior: a comparison of three models in the context of mobile internet. Decision Support Systems 42(3), 1819–1834.

SHAFT TM and VESSEY I (1998) The relevance of application domain knowledge: characterizing the computer program comprehension process. Journal of Management Information Systems 15(1), 51–78.

SHANKS G (1997) Conceptual data modelling: an empirical study of expert and novice data modellers. Australasian Journal of Information Systems 4(2), 63–73.

SIAU K and ROSSI M (2010) Evaluation techniques for systems analysis and design modelling methods – a review and comparative analysis. Information Systems Journal 20, [WWW document] DOI: 10.1111/j .1365-2575.2007.00255.x.

SOFFER P and WAND Y (2007) Goal-driven multi-process analysis. Journal of the Association for Information Systems 8(3). 175–202.

S RA, M SB and O RW (1996) A reexamination of the determinants of consumer satisfaction. Journal of Marketing 60(3), 15–32.

SUTCLIFFE AG and MAIDEN NAM (1992) Analysing the novice analyst: cognitive models in software engineering. International Journal of Man-Machine Studies 36(5), 719–740.

TABACHNICK BG and FIDELL LS (2001) Using Multivariate Statistics. Allyn & Bacon, Boston, Massachusetts.

THOMPSON RL, HIGGINS CA and HOWELL JM (1994) Influence of experience on personal computer utilization: testing a conceptual model. Journa of Management Information Systems 11(1), 167–187.

THONG JYL, SEJOON H and TAM KY (2006) The effects of post-adoption beliefs on the expectation-confirmation model for information technology continuance. International Journal of Human-Computer Studies 64(9), 799–810.

VAN DER AALST WMP and TER HOFSTEDE AHM (2005) YAWL: yet another workflow language. Information Systems 30(4), 245–275.

VENKATESH V (2000) Determinants of perceived ease of use: integrating control, intrinsic motivation, and emotion into the technology acceptance model. Information Systems Research 11(4), 342–365.

VERBEEK HMV, VAN DER AALST WMP and TER HOFSTEDE AHM (2007) Verifying workflows with cancellation regions and or-joins: an approach based on relaxed soundness and invariants. The Computer Journal 50(3), 294–314.

VESSEY I and GALLETTA DF (1991) Cognitive fit: an empirical study of information acquisition. Information Systems Research 2(1), 63–84.

WAND Y and WEBER R (2002) Research commentary: information systems and conceptual modeling – a research agenda. Information Systems Research 13(4), 363–376.

WOLF C and HARMON P (2006) The State of Business Process Management – 2006, www.BPTrends.com.

WORKFLOW MANAGEMENT COALITION (2008) Workflow management coalition workflow standard. Process definition interface – XML process definition language. Document number wfmc-tc-1025. WfMC.

YI MY and DAVIS FD (2003) Developing and validating an observational learning model of computer software training and skill acquisition. Information Systems Research 14(2), 146–169.

ZUR MUEHLEN M and RECKER J (2008) How much language is enough? Theoretical and practical use of the business process modeling notation. In Advanced Information Systems Engineering – Caise 200 (LONARD M and BELLAHSNE Z, Eds), pp 465–479, Springer, Montpellier, France.

## Appendix

See Table A1.

Table A1 Measurement items for constructs

<table><tr><td>Theory construct</td><td>No</td><td>Item definition</td></tr><tr><td rowspan="3">Modeling experience</td><td>EXP1</td><td>Over your working life, roughly, how many years experience do you have in process modeling overall?</td></tr><tr><td>EXP2</td><td>For how long have you been using BPMN for process modeling?</td></tr><tr><td>EXP3</td><td>Over your working life, roughly, how many process models do you think you have created with BPMN?</td></tr><tr><td rowspan="3">Modeler background</td><td>BGD1</td><td>In process modeling initiatives my role is mostly ...</td></tr><tr><td>BGD2</td><td>In process modeling initiatives I consider myself having expertise that is mostly ...</td></tr><tr><td>BGD3</td><td>I consider myself having a process modeling background that is mostly ...</td></tr><tr><td rowspan="3">Perceived grammar familiarity</td><td>FAM1</td><td>I feel very familiar with BPMN.</td></tr><tr><td>FAM2</td><td>I feel very competent in using BPMN for process modeling.</td></tr><tr><td>FAM3</td><td>I feel very confident in using BPMN for process modeling.</td></tr><tr><td rowspan="3">Perceived usefulness</td><td>PU1</td><td>Overall, I find BPMN useful for modeling processes.</td></tr><tr><td>PU2</td><td>I find BPMN useful for achieving the purpose of my process modeling.</td></tr><tr><td>PU3</td><td>I find BPMN helps me in meeting my process modeling objectives.</td></tr><tr><td colspan="3">Table A1 Continued</td></tr><tr><td>Theory construct</td><td>No</td><td>Item definition</td></tr><tr><td rowspan="3">Perceived satisfaction</td><td>SAT1</td><td>I feel extremely contented about my overall experience of using BPMN for process modeling.</td></tr><tr><td>SAT2</td><td>I feel extremely satisfied about my overall experience of using BPMN for process modeling.</td></tr><tr><td>SAT3</td><td>I feel extremely delighted about my overall experience of using BPMN for process modeling.</td></tr><tr><td rowspan="3">Confirmation of expectations</td><td>CON1</td><td>Compared to my initial expectations, the ability of BPMN to help me model processes was much better than expected.</td></tr><tr><td>CON2</td><td>Compared to my initial expectations, the ability of BPMN to help me achieve the purpose of my process modeling was much better than expected.</td></tr><tr><td>CON3</td><td>Compared to my initial expectations, the ability of BPMN to help me meet my process modeling objectives was much better than expected.</td></tr><tr><td rowspan="3">Perceived ease of use</td><td>PEOU1</td><td>I find it easy to model processes in the way I intended using BPMN.</td></tr><tr><td>PEOU2</td><td>I find learning BPMN for process modeling is easy.</td></tr><tr><td>PEOU3</td><td>I find creating process models using BPMN is easy.</td></tr><tr><td rowspan="3">Intention to continue to use</td><td>ItU1</td><td>If I retain access to BPMN, my intention would be to continue to use it for process modeling.</td></tr><tr><td>ItU2</td><td>In the future, I expect I will continue to use BPMN for process modeling.</td></tr><tr><td>ItU3</td><td>I prefer to continue to use BPMN for process modeling over other process modeling grammars.</td></tr></table>
