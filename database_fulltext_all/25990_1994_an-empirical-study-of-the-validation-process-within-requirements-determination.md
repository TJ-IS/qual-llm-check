---
otero_id: 25990
otero_key: "46X3K447"
title: "An empirical study of the validation process within requirements determination"
authors: "D. J. Flynn; R. Warhurst"
year: "1994"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1994.tb00051.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An empirical study of the validation process within requirements determination

D. J. Flynn & R. Warhurst

Department of Computation, University of Manchester Institute of Science and Technology (UMIST), Manchester M60 1QD, UK

Abstract. An empirical investigation into the validation process within requirements determination is described in which systems analysts were asked to complete a questionnaire concerning important validation issues. We describe the major validation activities, a set of major problems experienced by the respondents, factors affecting the process and hypotheses for problem explanations. The levels of experience of the respondents and the organizations for which they work appear to be significant.

Analysts employ a very traditional approach, expressing the specification mainly in English, and they experience problems in using over-formal notations in informal situations with users, as well as problems in deriving full benefit from notations when building the specification and detecting its properties. Not all of the specification is validated and tool use is not widespread and does not appear to be effective.

We define the concepts of formal and informal view, and suggest that method and tool use will not necessarily increase in organizations as it is apparent that research into the more effective application of formal notations is necessary. In addition, it is clear that the factors that affect the validation process are not only technical, but individual and organizational, necessitating the development of suitable informal activities which take these factors into account.

Keywords: design process, method, requirements determination, software development process, software process model, tool, validation.

## INTRODUCTION

There is a growing emphasis on the early stages of the systems development process in an attempt to overcome problems of system quality. This has been stimulated by the need to provide applications that are embedded in organizational structure and individuals' behaviour (Bubenko, 1986) or to take system usability into account as early on as possible (Gould & Lewis, 1985).

Validation is an important component of the development process, as users can check that their requirements have been captured correctly, as well as allowing for the refinement and articulation of those requirements as part of an iterative learning process. However, this area has been rather neglected in traditional development approaches and CASE tools, which, with a few exceptions, have emphasized the building or modelling aspects of requirements.

The work reported here is to carry out an empirical investigation into those activities in the early stages concerned with the validation of requirements. That is, we asked analysts about their current practices for checking whether the specification they were building was correct. Our aims were to gain a deeper understanding of the validation process, to identify problems experienced and to put forward hypotheses that may account for the problems and features of the validation process that we identified.

In this respect, our work differs from previous accounts of validation. The characteristics of validation are discussed on a very general level in, for example, Wileden (1985), and descriptions are given concerning various techniques and themes such as prototyping (Harker, 1988), validation problems (Kirby et al., 1988) and types of notation used (Nosek & Schwartz, 1988). The growing awareness of the importance of validation has led to several techniques being incorporated in more recent process models (Boehm, 1985) and system development environments such as Statemate (Harel et al., 1988). However, validation is, in general, regarded as an intuitive 'black box' process. Empirical work has tended to focus on more general aspects of systems development (Newman & Rosenberg, 1985; Necco et al., 1987; Salaway, 1987; Srinivasan & Kaiser, 1987; Curtis et al., 1988; Rosson et al., 1988; Soloway et al., 1988).

The structure of the rest of the paper is as follows: we describe the method we followed and then give an overview of the major validation activities found. The next section analyses the questionnaire responses. We then present the results, detailing the problems that arose, some characteristics that may affect the process and major findings, suggesting hypotheses for problem explanations. We integrate some aspects of our work in a discussion and then draw the main conclusions, discussing implications for practice and research.

## METHOD

The research approach we adopted was intended to be open-ended, to identify broad approaches to validation, to discover problems experienced and to set up hypotheses for exploration in subsequent studies. This type of approach may be viewed as theory development rather than theory testing (Soloway et al., 1988), and one characteristic is that it attempts to investigate areas of significant interest by conducting research within a realistic environment, rather than, for example, isolating a restricted range of variables and examining these under controlled experimental conditions. Such an approach has been termed ‘ecological’ (Shneiderman & Carroll, 1988) or ‘interactionist’ (Curtis et al., 1988).

We found that there were four methodological problems to which we had to provide solutions. The first problem was how were we to obtain information about the little-understood area of validation from busy analysts that was neither too general nor too specific. This had also to take account of the type of access available to project members. The solution was to base our approach on a factor rather than a process model (Newman & Robey, 1992), in that we would identify problems and develop hypotheses that certain problems were the outcomes of certain factors. As the validation process is not well understood, we decided on a two-phase questionnaire-based approach, with a general task analysis phase followed by a more validation-specific phase.

The task analysis phase was based on a largely open-ended questionnaire which was administered in an interview session, with one project member interviewing an analyst and one acting as scribe. The questions, which were aimed at establishing the tasks carried out by analysts, covered a wide range, including acquisition and modelling as well as validation, and a list of validation-oriented activities resulted. Interview sessions lasted between 1 and 2 hours, and nine analysts were questioned from three of the participating organizations.

In phase two, a shorter questionnaire was constructed on the basis of the results from the previous phase, with most of the emphasis on the validation process, the activities from phase 1 forming the basis of the questions with closed responses. The intention was to discover how these activities were carried out. In addition, problem areas had emerged from phase 1, and questions with open responses were designed to obtain more details of these and any solutions. The questionnaire was first of all piloted with staff from Data Logic Ltd, an organization collaborating in the research, and then the final version was sent by post to 29 analysts to complete, and all responded. Prior agreement for their participation had been obtained from organizational contacts. The questionnaire, including responses to closed questions, has been included in the appendix.

The primary factor determining the make-up of the group of analysts was the availability of access to the organizations for which they worked; however, we attempted to vary analyst factors such as depth of experience, use of a particular method and type of organization. The mean number of years' experience in requirements determination was just under 5, with values ranging from 1 to 21 years. Eighteen per cent of this experience was gained from working on large systems, 45% from medium systems and 37% from small systems. Eleven were Jackson system development (JSD) analysts, in that JSD was the main or exclusive structured (as opposed to informal) method that they used for building and validating a model of requirements. No single method was used by the other 18 analysts, and methods, notations and tools such as entity-relationship diagrams, dataflow diagrams, structured systems analysis, SSADM, LSDM, SQL design dictionary, Speedbuilder, Excelerator and Information Engineering were used. Analysts had a mean of just under 2 years' experience of such methods, but with wide deviations, as six analysts had no experience of methods, while 10 analysts had 3 or more years' experience. Some care should be exercised in interpreting these figures, as it is a fairly common practice to consider 2 years of method experience to result from one calendar year, if two projects running concurrently during that year use different methods.

Six organizations were used in the survey. Organization A (10 respondents) was a high street bank; organization B (five respondents) was a metropolitan police authority; organization C (two respondents) was then a public sector utility organization; organization D (six respondents) was in the retail, mail-order sector; organization E (five respondents) was a private sector software house, and organization F (one respondent) was a leisure and foods organization. Typical job titles were: systems analyst (junior/senior/principal), analyst programmer, consultant, systems team leader, business analyst and information planning manager. Analysts were not asked, as in Rosson et al. (1988), to select a recent project on which they had worked as the basis for their questionnaire responses. Replies, therefore, should be taken as being the result of their total analysis experience.

Discussion of the composition of the group raises the second methodological problem we faced, that of the significance of the results. The group of 29 respondents is relatively small and, as the key characteristics of 'analysts as validators' are not known, it was not possible to construct a representative sample. Hence, although the results can only be safely interpreted with respect to the group itself, we regard the results as preliminary hypotheses from an exploratory study, which are useful for providing indications as well as a basis for future work. Some care, however, was taken over the presence of variability with respect to the group factors mentioned above, as we (subjectively) felt these to be important in shaping respondents' views. The reason for including closed-question responses in the questionnaire in the appendix is to show the basis for the hypotheses that we have drawn.

The third problem concerned the analysis of questionnaire results. Safeguards against interviewer bias had been achieved in phase 1 by having structured questions and tandem interviewing, and, to minimize errors of interpretation, the number of open responses had been reduced in the final questionnaire. Two analyses of the results from the final questionnaire were conducted independently and then merged. Guarding against respondent bias, achieved in phase 1 by methods such as repeated questioning or answer comparison with peers, was not possible in phase 2 as postal questionnaires were used.

Finally, to present the results, we: (1) give an overview of the main validation activities that we found, accompanying this with an analysis of responses to questions for each activity; (2) analyse the problems found, presenting hypotheses for problem explanations and possible problem solutions; (3) analyse respondent characteristics; and (4) highlight major findings.

## QUESTIONNAIRE OVERVIEW

The context of the questionnaire, as explained in its introduction, is that of an early, requirements determination stage in the systems development process, in which a user requirement is being transformed into a specification and then validated with the user, and the focus of the questionnaire is the validation of that specification. The nature of the specification is user oriented rather than computer oriented, and validation is being investigated only on one level (which may be considered to be the level of abstraction of a conceptual schema), and not on subsequent levels.

The structure of the questionnaire is based on the main activities of transformation and validation, which emerged jointly from the earlier task analysis survey. Transformation activities (also referred to as activities which build the specification) consist of acquisition (acquiring knowledge from a user) and documenting (mapping that knowledge into a specification using a specification language). To simplify the questionnaire, we decided to concentrate, in the main, on those activities which take place person to person in an interview.

Although we were mainly concerned with validation, we included the transformation activities for two reasons. Firstly, in order to clarify our view of validation, we wanted to present its activities in relation to those of transformation. Validation activities may be more completely understood if we know that, for example, the specification is only informally defined. Secondly, it was felt necessary to make the context of the questionnaire more complete and familiar, leading in responders to questions on validation by including the prior activities of acquisition and documenting. The model that has emerged of the requirements determination process under consideration is based on these activities and may be seen in Fig. 1.

In Fig. 1 the main components of the process are represented by activity names in rectangles and the order of the activities by arrowed edges. The central ellipse labelled 'specification' represents a documentation facility or specification that is built, validated and refined by iteration. Dashed arrowed edges represent knowledge being put into, or taken out of, the specification. We are not suggesting that the specification must be a centralized knowledge repository; it may be an ad hoc collection of different types of document expressed in different forms.

The model is idealized in that an analyst could be performing several activities at different points within the process concurrently, each activity being concerned, for example, with a different part of the specification. Similarly, the model does not necessarily imply that the same part of a specification is built, validated and corrected all in one cycle.

![](/api/attachments/46X3K447/fulltext/images/c75e7f2bb1b2235c77d57fabc7c3f1dacc7325f4e79dcd3e951d09c0bcad9381.jpg)  
Figure 1. An empirical study of the validation process within requirements determination.

## ANALYSIS OF QUESTIONNAIRE RESPONSES

The aim of this section is to analyse the questionnaire responses using the framework of activities in Fig. 1. Where applicable, the activities will be refined, related problems discussed and references made to related work. Italics refer to options of closed questions.

## Initial domain knowledge

Before discussions begin with the user, the analyst acquires background knowledge of the user or of the application domain. This knowledge is termed domain knowledge and is used as a starting point to acquire knowledge of the application in question.

## Question A

Analysts were asked two questions about acquiring domain knowledge and the first concerned the domain knowledge with which they start a project.

The most common initial source of domain knowledge was found to be in customer documentation. This may refer to the initial statement of requirements or to a set of forms or procedures obtained from the customer. One respondent stated that he used existing system documentation and another that he used narrative feasibility reports. The next most common source was considered by respondents to be only in your head, that is the domain knowledge that comes from the analyst's own expertise.

Only some of this knowledge is held in an electronic form, for example, CASE tools or word-processing documents. It was, however, felt that this form would be used if it was available. It was not popular to hold domain knowledge in the form of analysis notations, such as dataflow diagrams.

The second question asked what domain knowledge is available to analysts in their own organizations, knowledge which would be available, in theory, at any time during a project. The most common source of domain knowledge was from in-house domain experts, followed closely by documents of the customer's business structure. This is consistent with the idea that, following a request for a system, the analyst's peers will be consulted for information about the customer or the business as well as requesting more information from the customer. All the sources in the question were used sometimes by many analysts, and one analyst said that he acquired domain knowledge from users of existing systems.

A conclusion may be drawn that domain knowledge is fragmented, in different forms, with different individuals, and in different physical locations. The lack of analyst domain knowledge was quoted as a problem by only two respondents. In an artificial intelligence (AI) approach, Barstow (1987), remarking that requirements analysis largely consists of learning about the domain, advocates computer representation of domain knowledge.

## Acquire user knowledge

This activity aims to acquire knowledge from the user to be used for building the specification.

## Question B

As the emphasis of the questionnaire was on validation, this question addressed only the techniques used to acquire user knowledge within an interview. Almost all analysts used documented questions, but a model of the domain was also used sometimes. The forms used were: dataflow diagrams (10 respondents), JSD diagrams (5), entity-relationship diagrams (3) and general, informal diagrams such as flow-charts (5).

## Record/Check

Question D seeks to establish the form or notation used to record findings during the interview sessions, while question E addresses the treatment of facts that the analyst feels may require validation. The different techniques used during interviews to ensure that responses have been correctly interpreted are investigated in question C.

## Question C

The analyst may wish to check responses before they are recorded, and the most common technique was generation of realistic examples, with the least popular being, by a considerable margin, generation of a model that can be discussed, as well as re-asking of the same question at different times. Asking questions to identify contradictions and questioning facts believed to be true were the second most common techniques. For other techniques, one method mentioned was summarizing previous responses at the end of a session (five respondents).

An informal validation process is thus taking place at this stage, with the acquired knowledge being expressed (see next question) in English, mainly using realistic examples as the medium for discussion.

## Question D

The majority of respondents recorded their findings in English long-hand. Annotating the specification was popular and structured answer sheets were least popular (14 respondents never used them). Two respondents mentioned tape recording the interview.

## Question E

During the interview, analysts may want to mark facts to be checked later, and 15 respondents said that they recorded these facts in a special way. Five respondents used a means of highlighting the fact, for example underlining or highlighter pens, while others used separate lists. The respondent who recorded interviews said that he made a note of the tape counter with the question and the time it was asked.

## Document findings

At this point in the process the analyst has finished a session with the user and needs to document the interview findings.

## Question F

This concerns the adding of recorded findings (and any later changes) to the specification and asks about the form that the specification takes. The most popular specification forms were English long-hand followed by as lists of requirements. The least popular forms were in a notation or a development method and as dataflow diagrams. Almost all the JSD analysts replied in a notation. Other notation methods mentioned were entity-relationship diagrams, structured English and SSADM diagrams.

The responses imply that a typical specification built by a respondent is a largely unintegrated, informal set of documents, which may be expressed in a variety of notations. In addition, answers to questions D and E make it likely that even relatively precise notations, such as JSD, may be annotated informally by analysts.

It may be noted that this approach is contrary to an approach, based upon a central conceptual schema for the specification (Stenning, 1987; Olle et al., 1988), expressed in a precise specification language. Several respondents commented on the disadvantages of the lack of a formalized method for documenting knowledge.

## Pre Validation

Having partially built a specification, the analyst will examine this and identify those areas which require validation. The questions concern the proportion of the specification that is identified for validation (question H), how a need for validation is determined (questions I, J and M) and how areas to be validated are indicated (questions K and L).

## Question H

In this question, respondents' views on the proportion of the specification they found necessary to validate with the user were sought, and the mean of the values extracted from the open responses was 81% of the specification, with a standard deviation of 20%. As we felt that this was an important question, we asked it again, in a rather disguised way, in question S.

Thirteen respondents suggested that all of the specification was validated, although their replies were often qualified by remarks such as 'in an ideal world' and 'if you want to be sure'. Ten respondents validated between 85% and 51%, and four replied in the range 50–20%, with one respondent suggesting '20% at project start — then a fall-off to 0' and another 'as much as reasonably possible'.

Parts of the specification, therefore, are not validated by the user. However, this does not preclude validation by other analysts, or self-validation, in which the analyst's domain knowledge is such that user validation is seen as unnecessary, and it was suggested that ‘critical areas’ should be highlighted, and that validation could depend ‘on the reliability of the source’.

## Question I

This question asked the analyst what particular areas of the specification usually require validation. No specific areas emerged as favourite, although JSD analysts usually mentioned entity structure diagrams. Responses ranged over many areas, for example: interface specifications (screen, report layout, security and audit), volumes and system timescales, entity-relationship models, exceptions and updates.

However, respondents mentioned other factors which often indicated a need for validation. For example, when geographically separate users existed (leading to potential inconsistency), when information came from a source not directly connected with the workings of the existing system (raising questions as to reliability of the source) or when documentation of existing procedures was at variance with actual practice. One respondent would validate any detailed calculations and technical areas.

## Question J

Analysts were asked to specify the criteria they use when identifying areas for validation. Almost all analysts used inconsistency, ambiguity and uncertainty, although a comment was that 'spotting these is the problem'. Feeling and notes were also used extensively. Ease of validation was not popular as a criterion (18 never responses).

## Question K

Fifteen of the respondents said that their method helped them to identify a need for validation in some way, and six gave no specific area, stating that the method helped to highlight ambiguities or inconsistencies in general. Others referred to particular areas, such as optional/mandatory data items. Other areas were action processing, entities with no common actions, entity life histories or entities with no relationships to other entities as being helpful for identifying areas for validation.

## Question L

This question asked the analysts how they mark or note areas which they select for validation between sessions with the customer, and respondents used English long-hand slightly more than they annotated specifications, both methods being very common. For responses to the open part of the question, dataflow diagrams, annotations to unspecified diagrams and JSD development tools were mentioned.

## Question M

Any approaches to determining a need for validation that had not been covered in the earlier questions were sought here, in addition to any problems respondents encountered in this area. Problem areas mentioned include the reliability of the information source, which can entail a 'lack of confidence in the user', and changes to old systems with no specification. Two respondents mentioned the need for tracing between related parts of the specification. Analyst domain knowledge was cited as being important for deciding a need for validation.

Conflicts and inconsistencies between users ('conflicts with interviewee's peers') occurred in responses to this question. Curtis et al. (1987) suggest that conflicting customers often require a separate, prespecification phase, which may be similar to the view integration process in many database design methods (Batini et al., 1986).

## Perform validation

This activity is investigated by questions which ask for techniques used and problems found, and which also attempt to establish metrics involving the time spent and the proportion of specification validated.

## Question N

Analysts used a variety of approaches when performing validation with users, and the most useful were create realistic examples, followed by ask a set of questions. All approaches were used to some extent, with the least useful being giving the customer English notes to comment on. Prototyping techniques were not mentioned. Although notations were used directly by some analysts, a frequently cited problem was that this was an unsatisfactory method. The need for a system overview facility was also mentioned.

One analyst said that he would not use formal diagrams in an interview, although he would use simple 'cartoon' diagrams in a presentation. He stated that 'users get turned off by boxes, arrows and buzzwords'. Another stated that 'some users will not become involved with diagrammatic techniques'. In contrast, one respondent mentioned that structured methods used to walk through with the customer were very useful, while another remarked (in response to question H) that 'surely the point of JSD is that it provides a communications tool with which to validate all gathered facts and requirements with the customer'.

## Question G

Validation models may be left with the user to validate without the analyst being present, and this question asks analysts to specify the forms that these models may take. Most popular were screen/report layouts, with questions regarding requirements also popular. Thirteen respondents left test results. JSD analysts sometimes left entity structure diagrams, but system specifications were unpopular. Again, notations are not widely used, with models which are close to an eventual system, or natural language, being most popular. This may not entail interpretation, as these forms may comprise part of the specification. In open response, analysts mentioned draft specifications or notes, user documentation and pilot systems.

## Question O

This question is aimed at eliciting areas of the specifications that are difficult to validate. Although three JSD analysts emphasized entity structures, the majority of respondents' difficulties were not directly connected to areas of the specification at all.

Respondents chiefly reported difficulties relating to the quality of knowledge in the specification. For example, inconsistencies between users, completeness or not of the current specification, fluctuating requirements ('users do not like change!') or 'those areas where the user is not even sure what his requirement is'. Nine respondents also mentioned the difficulties in comparing the specification with certain aspects of requirements, for example, company policy and procedures, future requirements, interfaces to other systems and eventual system performance.

## Post Validation

As a result of a previous validation session, the specification needs to be updated to indicate success or failure of validation, and changes need to be identified, including implied changes that will result from correcting information. Question T concerns the major problems encountered in this activity. Question U asks for the factor(s) which cause the validation cycle to terminate, shown by the exit on this activity in Fig. 1.

## Question T

In this question, analysts were asked to give the major problems they face after a validation session. Most respondents considered all the problems mentioned in the question to be major, with the largest problem being consistency and completeness checking. General documentation problems were least problematic.

Open responses included: contradictory information from other validation sessions, changing requirements and 'lack of a structured methodology to guide inexperienced analysts'. One respondent said that the closed responses covered the main problems and that CASE tools eased these problems.

## Question U

Analysts were asked for the factors that determine the end of validation. The most common factor was requirements and specification are valid, followed by customer sign-off. Customer not prepared to continue and lack of resources were cited by about half the respondents. One respondent mentioned that one factor was ‘deadlines which cannot be moved’.

## General questions

## Question S

Analysts were asked about the proportion of the specification that is validated, and the mean of the responses was 82% with a standard deviation of 25%. This figure is very close to the mean from question H (81%). Analysts were also asked for the proportion of the specification that is validated specifically with the customer, and the mean of the responses was 75% with a standard deviation of 25%.

## Questions P and Q

Question P asked analysts to estimate the proportion of time they spend on validation of the specification, in relation to the total time spent in building and validating, and the mean of the responses was 44%, with a standard deviation of 21%. This value assumes that those responders who answered 'over 50%' spend 75.5% of their time validating. Assuming a value of 50% for these respondents would give a mean of about 38%.

Question Q asked for the time spent on each of the three main validation tasks, as a proportion of total validation time. The results are as follows:

(a) Pre validation — mean 27% and standard deviation 12%,

(b) Perform validation — mean 43% and deviation 15%,

(c) Post validation — mean 26%, deviation 12%.

## Question V

Analysts were asked to comment upon the validation process, particularly with regard to any areas which they felt could benefit from automated tool support. Three respondents perceived a problem with changing requirements. 'The main difficulty I find with validation is getting the end user to identify business requirements that are complete and accurate and stick to them', but 'having customers involved in analysis seems to overcome this'.

Just under half (14) of the respondents had experience with automated tools (Speedbuilder, Excelerator and SQL design dictionary being quoted), and responses were positive about the benefits expected from such support, although some stressed that diagramming support was necessary, as otherwise the 'end result is no better than a mass of text'. The main advantages given were a reduction in the volume of paper generated and the use of tools to accomplish inconsistency flagging, completeness checking, global change facilities and impact analysis.

## RESULTS

## Problems found

In an ideal situation, knowledge that is certain and unambiguous is acquired by the analyst and documented without error, requirements do not change and problems do not occur. However, this is the exception rather than the rule, and an important result from the survey is the set of major problems found in the validation process. We defined a major problem as a problem cited in open response or one receiving a rating of often, 1 or 2 in closed response. The mean of the number of major problems (ranging from 1 to 8) for all respondents is 4.3, and the problems together with the percentage of respondents who experience them is shown in Table 1.

Table 2 shows similar problems found in other studies. The fact that analyst domain knowledge was a major problem in the Curtis et al. (1988) study may be because all their respondents were concerned with real-time systems, which possibly demand greater analyst knowledge than information systems. We classified the Table 1 problems into three areas.

## Problem type A: nature of the knowledge in the specification

(A1) Detection and resolution of inconsistency. Inconsistencies may be caused by users learning and refining requirements between validation sessions, differences between users concerning the nature of the requirements, analyst error or fluctuating requirements due to external factors. In a large specification, it is hard to detect inconsistency, particularly if the specification is expressed in natural language. Some simple inconsistencies may be resolved in Pre Validation using notations, but the resolution of more major inconsistencies is usually undertaken within perform validation, when the analyst may need to resolve differences between more than one user.

Table 1. Major problems experienced by respondents

<table><tr><td rowspan="2">Code</td><td colspan="2">Major problems</td><td rowspan="2">Per cent</td></tr><tr><td>Statement</td><td>Number of respondents</td></tr><tr><td>A1</td><td>Detection and resolution of inconsistency</td><td>26</td><td>90</td></tr><tr><td>B1</td><td>Users have difficulty expressing their requirements to analysts</td><td>22</td><td>76</td></tr><tr><td>C1</td><td>Determination of the impact of changes on the specification</td><td>16</td><td>55</td></tr><tr><td>C2</td><td>Performing global changes on the specification</td><td>14</td><td>48</td></tr><tr><td>C3</td><td>Manual management of the volume of data in a specification</td><td>11</td><td>38</td></tr><tr><td>B2</td><td>Users are not available during validation</td><td>11</td><td>38</td></tr><tr><td>A2</td><td>Detection of ambiguity and incompleteness</td><td>10</td><td>34</td></tr><tr><td>B3</td><td>Analysts have difficulty expressing the specification to users</td><td>5</td><td>17</td></tr><tr><td>A3</td><td>Detection of critical or unreliable areas</td><td>4</td><td>14</td></tr><tr><td>D1</td><td>Changing requirements</td><td>3</td><td>10</td></tr><tr><td>D2</td><td>Analysts lack knowledge or experience</td><td>2</td><td>7</td></tr><tr><td>D3</td><td>Lack of structured guidance</td><td>1</td><td>4</td></tr><tr><td>D4</td><td>Users specify how as well as what</td><td>1</td><td>4</td></tr></table>

Table 2. Similar major problems reported by other studies

<table><tr><td>Problem</td><td>Source</td></tr><tr><td>Thin spread of application domain knowledge</td><td>Curtis et al. (1988)</td></tr><tr><td>Communication and coordination breakdowns</td><td></td></tr><tr><td>Fluctuating and conflicting requirements</td><td></td></tr><tr><td>Documentation not consistent or complete</td><td>Necco et al. (1987)</td></tr></table>

(A2) Detection of ambiguity and incompleteness. If requirements or the specification are expressed in natural language it is often the case that ambiguities will exist. The specification may also be incomplete, and this may not be realized until several different parts are related and analysed in Pre Validation.

(A3) Detection of critical or unreliable areas. A few respondents comment that it is important to decide on the most critical part of an application, to make sure that this receives emphasis in validation. Some respondents also feel that there may be certain users who give unreliable information, for example because they are out of date with the way in which the current system operates. Both these properties of the specification require judgment for their detection.

## Problem type B: user-analyst communication

(B1) Users have difficulty expressing their requirements to analysts. A frequent complaint is that users cannot adequately explain their requirements, which may be because users find difficulty in choosing an appropriate medium for the expression of the requirements, or they do not devote sufficient time to communicate the requirements to the analyst. A pertinent comment was: 'Occasionally get the customer who knows but cannot express and his manager who can express but doesn't know'. Alternatively, if users are learning their requirements, as occurs frequently, then analysts may perceive the user as having difficulty in expressing the requirements.

(B2) Users are not available during validation. If users do not commit enough of their resources to perform validation, then some of the specification may not be validated, or may not be validated as well as is necessary. The survey results only provide hints for explanations of this problem, such as the absence of management support for user participation, user unwillingness to participate or the fact that users are geographically dispersed and it may be difficult or impossible for them to be available.

(B3) Analysts have difficulty in expressing the specification to users. The survey implies that this is because users do not tend to understand or to be sympathetic towards analyst notations, even in diagrammatic form, and we may conjecture that this is because notations are unfamiliar or too computer oriented, users preferring to discourse within their own frames of reference. Analysts therefore avoid using notations as the basis for validation models.

This result is perhaps surprising, but the survey suggests that analysts prefer realistic models, which, as prototyping aids are absent, they create themselves using verbal means and informal pictures, i.e. informal as opposed to analytic methods (Rosson et al., 1988) are preferred. Problem type B is evident in Perform Validation.

## Problem type C: dealing manually with an unintegrated specification

(C1) Determination of the impact of changes on the specification. For a large specification, it is difficult to predict all the implications of changes, and it is easy for an incomplete specification to result.

(C2) Performing global changes on the specification. This problem concerns the time-consuming and error-prone revision of large parts of a specification to incorporate changes.

(C3) Manual management of the volume of data in a specification. This is a slow manual task, and mistakes may be made in areas such as version control. Type C problems occur in Post Validation.

## Other problems

Some problems could not be categorized and appear to be relevant to any of the three validation activities. Changing requirements is a well-known problem in the development process, caused by users refining their requirements, external changes or infeasible implementation. Many of the other problems in Table 1 are exacerbated by this problem. The low percentages received by problems such as changing requirements and lack of structured guidance may reflect the fact that these problems were not available as options in closed responses.

## Intra-sample analysis

We found several linkages between a variety of cognitive, organizational, technical and managerial respondent factors and survey findings. Our results should be treated with caution owing to the small subsets of the sample involved.

## Problems found

Level of experience. The mean level of requirements determination experience was 4.8 years, and the commonsense assumption that respondents with most experience had least problems was borne out by the results, as all but one respondent with experience above the mean had fewer problems than the mean. However, it was not the case that all those with least experience had most problems, perhaps because an analyst with little experience may be unaware of some problems.

Type of organization. There was a suggestion that respondents in public sector organizations had more problems than those in the private sector, as the two public sector organizations had problems above the mean. However, it was noted that the means of the number of years experience of the respondents for organizations A and F (who had problems below the mean) were above the mean for all respondents. There was also a suggestion that respondent sex might be involved.

Sex. Of the 29 respondents, seven were female, and we found that they experienced fewer problems than their male counterparts, with a mean number of problems of 3.7, compared with the mean for all respondents of 4.3. However, we would not like to suggest that organizations can reduce their problems simply by employing more female analysts; it is more likely that respondent factors interact, as we found that the female respondents with a high mean number of problems worked for a public sector organization, whereas those with a low mean number of problems also had more experience than the mean.

Problem type. For problem type and respondent characteristics we found:

\- Type B. Three of the five respondents who had problem B3 (expressing the specification to users) worked for the same organization, organization B. We did not find the female respondents had fewer type B ('communications') problems.

\- Type C. Those respondents with problems of type C were mostly the respondents who had tools experience, implying that tools may be inadequate for this type of problem.

Other respondent factors. We did not find any relationship between the number of problems and respondent factors such as systems size experience, tools experience or level of structured experience, determined by adding the number of years' experience respondents had of development methods/notations, of which the mean was just under 2 years.

## Validation of specification

Experience. We found that there was an indication that those with least experience validated more of the specification and spent most time in validation; however, there was no indication that those with most experience validated the least. Inexperienced analysts may believe that they should validate all or almost all of the specification with the user; as they gain in experience, some of them reduce the amount, but many do not.

Organization. There was some indication of an organizational policy towards validation, as the respondents of two organizations gave similar responses for the percentage of the specification validated. If such a policy existed, it was either absent or not being followed in the other organizations.

## Multifactor relationships

We found that four of the six respondents with no structural experience all belonged to organization A, which had the fewest problems, indicating perhaps that acquiring structured experience may not necessarily result in problem reduction. We felt that there was some aspect of organization A, concerning which we had no data, that was possibly influencing this problem level. In addition, the two organizations which appeared to have the strongest management policy for using structured methods (JSD) also had problems above the mean, suggesting that the existence of such a policy does not necessarily result in fewer problems.

## Major findings

The findings which we believe to have major implications for future method and tool design and use are:

1 The specification is unintegrated and is mainly in the form of written English. A variety of method notations are known to the respondents but they do not appear to be used extensively to build the specification. This causes problems with the detection of specification properties such as ambiguity and inconsistency. Possible explanations are: (a) methods do not cover all areas of requirements, (b) analysts find methods ineffective for detecting inconsistency and ambiguity, (c) management does not provide support for methods, (d) the inflexibility of notations in a climate of rapidly changing requirements or (e) the fact that users need to validate the specification means that analysts may feel it necessary to express the specification in a language that users can understand.

2 There are problems in communicating between user and analyst. Analysts perceive users as being unable to express their requirements effectively and, as users find analyst notations unfamiliar and are unhappy with their use, analysts have to use informal means for explaining the specification to users.

3 Only 75% of the specification is user validated. In addition, half the respondents allow validation to finish before they are satisfied that the specification is valid. This may explain the occurrence of many quality problems, as analysts may make subjective decisions that parts of the specification do not need to be validated with the user. There may be several reasons for this, for example: (a) the user is not available, (b) the analyst's domain knowledge is deemed sufficient or (c) the analyst uses domain experts in his or her organization for validation.

4 Tools, although available, are not used widely. Those respondents with tool experience are dissatisfied with their use. Among the reasons for this problem may be that: (a) tools emphasize building and not validation activities, (b) tools do not cover all areas of requirements, (c) management does not support tool use or (d) as suggested in HECTOR (1990), tools do not improve quality, only productivity.

## Formal and informal views of validation

An important issue that arises from the survey centres around the concept of whether validation may be viewed as a relatively formal or as an informal process. Our definition of the formal view of the process is that it consists of well-defined activities, uses predefined accessible knowledge and acts on well-defined objects. An example of a formal activity is the use of the JSD method to check for inconsistencies in the specification. In contrast, the informal view considers the process as being made up of undefined activities, based on individual judgment and experience and acting on undefined objects, and an informal activity might be the use of a realistic, dialogue-based model to explain the specification to a user.

The survey has established that analysts carry out formal as well as informal activities. The views are complementary as they are both required to describe the process (we recognize that other views may be required to describe other dimensions of the process, but we only consider the informal/formal views here). The fact that these two views of the process exist does not necessarily mean that either view may be applicable in any given situation, and we believe that our first two major findings are characterized by the fact that there is a mismatch between view and situation.

## Mismatch between view and situation

An example of a mismatch concerning an informal activity is the problem analysts find when explaining the specification to users (problem B3), when the users find notations too formal and computer-oriented, and the survey shows that many analysts are using informal, realistic models as an alternative. Examples of one type of approach to address this problem are development methods which incorporate group sessions to help resolve conflicts between user groups (Mantei & Teorey, 1989), prototyping aids which generate appropriate validation models for users (Warhurst & Flynn, 1990) and work in the Human–Computer Interaction (HCI) area to establish procedures and types of validation model required (Harker, 1988).

Such work may lead to the emergence of a view which occupies a point on the spectrum between the formal and the informal views — such a view may be termed a structured view and it would consist of activities that are not left completely to analyst intuition, but are not precisely defined.

For formal activities, the survey suggests that methods and tools which may assist these activities are not being used to their full potential. Although building a specification would appear suited to the use of formal activities, the mismatch occurs because the specification is still expressed mainly in English.

## CONCLUSIONS

Validation is important as it is one of the two main processes in requirements determination, the other consisting of building the specification. It is becoming more widely accepted that to provide information systems that meet user requirements necessitates an iterative, validation process involving a significant degree of learning between analyst and user (Avison & Wood-Harper, 1990; Hales, 1991).

The surveys shows that the specification is expressed mostly in English and that it consists of a set of unintegrated documents, some textual and some diagrammatic. This poses problems of ambiguity as well as difficulties in detecting inconsistency. During validation, analysts perceive users as being unable to express their requirements adequately; in addition, analysts have to employ informal, realistic examples to explain the specification as users do not feel comfortable with method notations. Users are often unavailable for validation, and analysts often have to resolve inconsistencies between different users.

After a validation session, analysts try to predict implications of proposed changes to the specification, and then apply these changes. Available tools do not provide much help for this activity. A sizeable proportion of the specification is not validated with the user, and validation often finishes before the analyst feels it is complete. If the main objective of validation is to ensure that a specification correctly captures the user requirements then the survey indicates that this objective is not being fully achieved.

## Recommendations for practice

The problems in Table 1 may be used to provoke debate or reflection amongst developers and their management concerning ways for addressing or avoiding those problems. In addition, some of the specific findings may be used as a focus for the debate. For example, the finding that more experienced analysts have fewer problems is unsurprising; the fact that the length of experience in structured methods is unrelated to the number of problems is perhaps less so. Management might therefore expect that such experience is only one part of an analyst's skills. Another resource-related factor is that female analysts appear to have fewer problems than male analysts, and subsequent work is required to confirm this rather interesting finding.

Public sector organizations have more problems than those in the private sector, and public sector employees may benefit from the knowledge that they are working in an environment that is relatively more error prone, and may therefore take extra steps to attempt to combat this. A factor related to the management of the validation process concerns the fact that those organizations which appear to have a strong policy for the use of methods do not have fewer problems, implying that it is not sufficient only to emphasize the formal view of validation, but that other views, such as the informal view, should also be supported. Finally, we found that CASE tools are not rated highly by those that use them.

## Recommendations for research

Many of the results we obtained gave us pointers to more detailed questions we would have liked to have asked, and we briefly discuss below some factors, wider than those considered in our research, that future studies may consider.

## Validation process factors

Table 1 is useful as it contains 13 problems that may be used to ask analysts explicitly about the problems they experience. It would also be useful to obtain an overall rating of the perceived effectiveness of the validation process, perhaps obtaining separate ratings for each of the three main activities. In addition, there are three issues which deserve emphasis from future investigators, the first two concerning the applicability of formal or informal views in the process and the third concerning analysts' attitudes.

The first issue is concerned with building the specification. Why do respondents use informal languages in this situation when formal languages, such as method notations, would seem more appropriate? In the practical situation, there may be problems preventing the successful use of these technologies, and we suggested several explanatory hypotheses for future investigation. If a significant part of the specification cannot be expressed in a precise language, then the usefulness of methods and tools is limited.

The second issue concerns the perception that users have difficulty expressing their requirements. We feel that this problem may hide several problems, for example the user cannot understand analyst notation, the user keeps on changing requirements, the analyst cannot understand the user's means of expression or the analyst has insufficient domain knowledge. If the user cannot understand analyst notations then less formal languages and models need to be developed. Alternatively, if the problem is due to analyst domain knowledge then analyst training is a more appropriate solution.

The third issue is this: do analysts term requirements ‘inconsistent’ when users change the requirements between sessions? We suspect that our respondents are not very sympathetic to users who change requirements, and they may not fully understand the reasons behind such changes or appreciate the nature of validation as a learning process for the user. Analysts may be assuming that requirements are known and fixed prior to the start of a project. This attitude, particularly if held by management who are engaged in project planning, may seriously affect the resources assigned to a project and thus its productivity.

## Respondent factors

We felt that factors in the respondent working environment could affect validation, and for the development environment, factors may concern the type of development methods the respondent has experienced, the type of systems worked on and the extent of user participation. In the management environment, policies, procedures, user participation and training may be important. Finally, for the organizational environment, relevant factors may include organization sector, size and budget of IT department, reporting structure of IT director/manager and the level of computer awareness of organizational users with whom respondents deal.

## Multidimensional factors affecting the validation process

Formal activities involving methods and tools currently receive a lot of attention in the literature and in the marketplace. However, this survey has raised a question concerning their usefulness in situations, for example in building the specification, to which they are apparently suited. The results do not indicate that single technical factors, such as the level of respondent structured experience or the availability of CASE tools, which might be expected to influence formal activities, are positively related to the number of problems that respondents experience.

Instead, the hypotheses we have advanced to explain the relevant problems indicate that formal activities may depend for their effectiveness on a range of psychological, sociocultural, organizational and environmental factors. Hence, the prediction in Necco et al. (1987) of increasing take-up methods and tools may be slower than envisaged, as merely adding to their numbers without understanding the problems they are required to solve may increase some problems.

We also found problems with the use of formal languages in informal situations, and we recommended that more emphasis should be placed on informal (or less formal) activities for use in this type of situation. Effective informal activities will also require a wide range of factors to be taken into account, and increased understanding of the validation process is thus likely to be in terms of such a set of multidimensional factors.

Our respondents use very traditional methods for systems development, and solutions to the problems they experience may result in radical method redesign, with more of an emphasis on 'soft' psychological and sociological issues. We advocate the type of research which attempts to understand the issues, problems and relevant factors in the process by empirical means, leading to recommendations for solutions which address those problems.

## ACKNOWLEDGEMENTS

The help and assistance of the participating organizations and individuals was crucial to the success of this work and we would like to thank all concerned. Early work on questionnaire design was carried out by Dermot Browne and Bob Summersgill of Data Logic. The suggestions of the referees have been very useful for improving the paper. Assistance from the Science and Engineering Research Council is gratefully acknowledged.

## REFERENCES

Avison, D. & Wood-Harper, A.T. (1990) Multiview: an Exploration in Information Systems Development. Blackwell Scientific Publications, Oxford.

Barstow, D. (1987) Artificial intelligence and software engineering. In: Proceedings of the 9th International Conference on Software Engineering, Monterey, California, March 30–April 2, pp. 200–211.

Batini, C., Lenzerini, M. & Navathe, S. (1986) A comparative analysis of methodologies for database schema integration. ACM Computing Surveys, 18(4), 323–364.

Boehm, B.W. (1985) A spiral model of software develop-

ment and enhancement. In: Proceedings of an International Workshop on the Software Process and Software Environments, Coto de Caza, Trabuco Canyon, California, March 27–29, Wileden, J.C. and Dowson, M. (eds.) reprinted in ACM SIGSOFT Software Engineering Notes 11(4), August 1986, 22–42.

Bubenko, J.A. (1986) Information system methodologies — a research view. In: Information Systems Methodologies: Improving the Practice, Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) pp. 289–318, Elsevier, Amsterdam.

Curtis, W., Krasner, H., Shen, V. & Iscoe, N. (1987) On building software process models under the lamppost. In: Proceedings of 9th International Conference on Software Engineering, Monterey, California, March 30–April 2, pp. 97–105.

Curtis, W., Krasner, H. & Iscoe, N. (1988) A field study of the software design process for large systems. Communications of the ACM 31, 1268–1287.

Gould, J.D. & Lewis, C. (1985) Designing for usability: key principles and what designers think. Communications of the ACM, 28, 300–311.

Hales, M. (1991) A human resource approach to information systems development — the ISU (information systems use) design model. Journal of Information Technology, 6, 140–161.

Harel, D., Lachover, H., Naamad, A. et al. (1988) STATE-MATE: a working environment for the development of complex reactive systems. In: Proceedings of 10th International Conference on Software Engineering, Singapore, April 11–15, pp. 396–406.

Harker, S. (1988) The use of prototyping and simulation in the development of large-scale applications. The Computer Journal, 31, 420–425.

HECTOR (1990) HECTOR Market Assessment UK Country Report, HECTOR Esprit project number 2082, available from KPMG Peat Marwick McLintock, 8 Salisbury Square, London EC4Y 8BB.

Kirby, M.A.R., Fowler, C.J.H. & Macaulay, L.A. (1988) Overcoming obstacles to the validation of user requirement specifications. In: People and Computers IV, Jones, D.M. and Winder, R. (eds), pp. 111–122, Cambridge University Press, Cambridge.

Mantei, M.M. & Teorey, T.J. (1989) Incorporating behavioral techniques into the systems development life cycle, MIS Quarterly, 13, 256–273.

Necco, C.R., Gordon, C.L. & Tsai, N.W. (1987) Systems analysis and design: current practices. MIS Quarterly, 11, 461–475.

Newman, M. & Robey, D. (1992) A social process model of user-analyst relationships. MIS Quarterly, 16, 249–265.

Newman, M. & Rosenberg, D. (1985) Systems analysts and the politics of organizational control, Omega, 13, 393–406.

Nosek, J.T. & Schwartz, R.B. (1988) User validation of information system requirements: some empirical results. IEEE Transactions on Software Engineering, SE-14, 1372–1375.

Olle, T.W., Verrijn-Stuart, A.A. & Bhabuta, L. (eds) (1988) Computerised Assistance during the Information

Systems Life Cycle (Proceedings CRIS 88 conference, London, UK), Elsevier, Amsterdam.

Rosson, M.B., Maass, S. & Kellogg, W.A. (1988) The designer as user; building requirements for design tools from design practice. Communications of the ACM, 31, 1288–1297.

Salaway, G. (1987) An organizational learning approach to information systems development, MIS Quarterly, 11, 245–264.

Shneiderman, B. & Carroll, J.M. (1988) Ecological studies of professional programmers, Communications of the ACM, 31, 1256–1258.

Soloway, E., Pinto, J., Letovsky, S., Littmann, D. & Lampert, R. (1988) Designing documentation to compensate for delocalized plans. Communications of the ACM, 31, 1259–1267.

Srinivasan, A. & Kaiser, K.M. (1987) Relationships between selected organizational factors and systems development. Communications of the ACM, 30, 556–562.

Stenning, V. (1987) On the role of an environment. In: Proceedings of 9th International Conference on Software Engineering, Monterey, California, March 30–April 2, pp. 30–34.

Warhurst, R. & Flynn, D.J. (1990) Validating JSD specifications by executing them, Information and Software Technology, 32, 598–612.

Wileden, J.C. (1985) This is IT, Proceedings of an International Workshop on the Software Process and Software Environments, Coto de Caza, Trabuco Canyon, California, March 27–29, Wileden, J.C. and Dowson, M. (eds), reprinted in ACM SIGSOFT Software Engineering Notes, 11, August 1986, 11–16.

## Biographies

Dr Donal Flynn is a member of the information systems group and a senior lecturer in the Department of Computation, University of Manchester Institute of Science and Technology (UMIST), Manchester, M60 1QD. His research interests are in the areas of information systems and conceptual modelling.

Robin Warhurst worked for the Ford Motor Company for over 5 years, has completed an MSc in information systems prototyping research at UMIST, and is currently working as an analyst for ICL in Manchester.

## I Interpretation of questionnaire responses

The questionnaire shown below has been edited and compressed for publication purposes. In addition, the frequencies of the responses to the closed questions have been given in the appropriate response box. The following indicates the meaning of these responses for each question:

<table><tr><td>Question(s)</td><td>Meaning</td></tr><tr><td>A-G,J,L,P,T,U</td><td>The frequency of the responses is shown for each question or part of question. For example, to question A1, 27 responses were ‘yes’ and one was ‘no’ (as there are 29 responders in all, there was one nil response to this question).In another example, question A2 — only in your head — nine responders replied ‘often’, 13 ‘sometimes’ and five ‘never’.</td></tr><tr><td>K</td><td>Although there were only seven ‘yes’ responses, there were 15 responses given to the last (IF YES) part of the question.</td></tr><tr><td>N,Q</td><td>The values in the boxes are the response frequencies, while the values in parentheses are derived means.</td></tr><tr><td>R</td><td>The values in the boxes are the frequencies for ‘1’ or ‘2’ responses.</td></tr><tr><td>S</td><td>The first values shown are the response frequencies, the values in parentheses are response means.</td></tr></table>

## II Questionnaire

A. Presumably, at the start of a project, validation does not take place during your first encounter with the customer or customer's representatives. Nevertheless, during initial sessions you may have a lot of knowledge that you wish to clarify or check. For instance, you may have previous experience of the customer's business or working practices. Such knowledge will be referred to as 'domain knowledge' throughout this questionnaire.

1 At the start of any project, have you begun analysis using existing domain knowledge to structure your initial fact gathering with customers?

YES 27
NO 1

if NO go to question B.

2 In what form has your domain knowledge been held?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>Only in your head</td><td>9</td><td>13</td><td>5</td></tr><tr><td>In customer documentation</td><td>13</td><td>14</td><td>1</td></tr><tr><td>In an electronic form at your company</td><td>5</td><td>12</td><td>8</td></tr><tr><td>In a notation such as dataflow diagrams</td><td>2</td><td>13</td><td>11</td></tr><tr><td>Another form (please specify)</td><td></td><td></td><td></td></tr><tr><td></td><td>□</td><td>3</td><td></td></tr></table>

3 What type of existing in-house domain knowledge do you have access to?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>In-house domain experts.</td><td>14</td><td>13</td><td>1</td></tr><tr><td>The customer&#x27;s business structure.</td><td>7</td><td>19</td><td>0</td></tr><tr><td>Similar requirements for a different system.</td><td>5</td><td>17</td><td>3</td></tr><tr><td>The customer&#x27;s manufacturing or information handling procedures.</td><td>6</td><td>16</td><td>5</td></tr><tr><td>Other knowledge (please specify)</td><td>3</td><td></td><td></td></tr></table>

B. During your initial analysis with the customer do you begin with any of the following? It may help to think of a particular analysis project you have worked on recently.

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>Documented questions requiring answers.</td><td>16</td><td>10</td><td>2</td></tr><tr><td>A model of the domain that acts as a framework for discussion during interviews.</td><td>3*</td><td>15*</td><td>5</td></tr><tr><td>Something else (please specify)</td><td>1</td><td>1</td><td></td></tr><tr><td>* if OFTEN or SOMETIMES then please specify form of the model</td><td></td><td></td><td></td></tr></table>

C. Do you use any of the following techniques to ensure you have interpreted responses correctly?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>Re-asking of the same question at different times during an interview</td><td>7</td><td>13</td><td>9</td></tr><tr><td rowspan="2">Generation of a model during an interview that can be discussed</td><td>7</td><td>13</td><td>9</td></tr><tr><td>12</td><td>15</td><td>1</td></tr><tr><td>Asking questions that may identify contradictions</td><td></td><td></td><td></td></tr><tr><td>Generation of realistic examples that provide a test of your understanding</td><td>19</td><td>8</td><td>0</td></tr><tr><td>Generation of questions which query facts believed to be true</td><td>14</td><td>13</td><td>1</td></tr><tr><td>Other techniques (please specify)</td><td>5</td><td>3</td><td></td></tr></table>

D. During your sessions with the customer, how do you record your findings?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>On a structured answer sheet.</td><td>3</td><td>10</td><td>14</td></tr><tr><td>Annotating the specification.</td><td>9</td><td>14</td><td>3</td></tr><tr><td>Using a graphical notation.</td><td>9</td><td>9</td><td>7</td></tr><tr><td>English long-hand.</td><td>18</td><td>10</td><td>0</td></tr><tr><td>Other.</td><td>1</td><td>1</td><td></td></tr></table>

E. During interviews you may gather facts that you wish to check on a future occasion. For instance, a new fact may contradict a previously recorded fact. Would you record such a fact in a special way?

YES 15 NO 13 if Yes please specify how they are recorded.

F. Having completed an interview session, how do you document your findings?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>In a notation or a development method (e.g. JSD)....</td><td>7</td><td>3</td><td>8</td></tr><tr><td>As dataflow diagrams....</td><td>5</td><td>14</td><td>6</td></tr><tr><td>As lists of requirements and constraints....</td><td>14</td><td>10</td><td>3</td></tr><tr><td>English long-hand....</td><td>18</td><td>10</td><td>0</td></tr><tr><td>Other....</td><td>4</td><td>4</td><td></td></tr></table>

G. Do you ever leave any of the following with customers, for them to critique or supply answers to?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>Questions regarding sequence of process.</td><td>9</td><td>13</td><td>5</td></tr><tr><td>Questions regarding requirements.</td><td>14</td><td>13</td><td>2</td></tr><tr><td>Entity structure diagrams</td><td>6</td><td>9</td><td>13</td></tr><tr><td>System specification diagrams</td><td>1</td><td>8</td><td>15</td></tr><tr><td>Screen/report layouts</td><td>22</td><td>5</td><td>2</td></tr><tr><td>Test results.</td><td>6</td><td>7</td><td>10</td></tr><tr><td>Others (please specify)</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>3</td><td></td></tr></table>

H. Can you give us a feeling for how much of the gathered facts and requirements you find it necessary to validate with the customer?

I. Are there specific areas of the specification or gathered facts that are usually identified as prime candidates for validation, and if so what are they?

J. Which of the criteria specified below do you use for identifying areas to be validated?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>Inconsistency</td><td>23</td><td>6</td><td>0</td></tr><tr><td>Ambiguity</td><td>24</td><td>5</td><td>0</td></tr><tr><td>Uncertainty</td><td>23</td><td>6</td><td>0</td></tr><tr><td>A ‘feeling’ that an area has problems</td><td>12</td><td>14</td><td>1</td></tr><tr><td>Notes made during fact gathering</td><td>15</td><td>13</td><td>1</td></tr><tr><td>Anticipated ease of validation</td><td>2</td><td>6</td><td>18</td></tr><tr><td>Others (please specify)</td><td>3</td><td>2</td><td></td></tr></table>

K. Does the method you use for recording your findings provide a mechanism for identifying where validation is required? NO 6 YES 7 (15)

If YES, how does it help (e.g. does it draw attention to impossible sequencing?)

L. Between sessions with the customer how do you 'note' facts/information etc. that will need to be validated at a later stage?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>Annotating specifications</td><td>17</td><td>9</td><td>1</td></tr><tr><td>English long-hand</td><td>20</td><td>7</td><td>1</td></tr><tr><td>Other (please specify)</td><td>3</td><td>2</td><td>0</td></tr></table>

M. Can you tell us a little about how you identify a need for validation, if you feel that this has not been covered by the above questions? Are there any other aspects of the information you collect or the specification you create that might give you cause for concern?

N. Please could you give an indication of how useful you find the techniques listed below, by rating them on a scale from 1 to 5 (5 being most useful).

Create realistic examples for the customer to comment on .... 28 (4)
Perform dataflow walk-throughs for the customer to comment on .... 29 (2.5)
Ask a set of questions determined prior to the interview.... 28 (3.5)
Ask previous questions in a new way .... 27 (2.9)
Ask previous questions and supply the original answers in order to gain clarification.... 28 (3)
Show the customer entity structure diagrams and perform a walk-through.... 26 (2.8)
Give the customer English notes to comment on.... 28 (2.2)
Other techniques (please specify)

O. Please indicate those particular areas that you find most difficult to validate.

P. At a guess what percentage of your time, before you start physical design, is spent performing validation? Approximately

0–15% 0
16–25% 6
26–35% 7
36–50% 8
Over 50% 8

Q. For the three main validation tasks (1) identify area of validation (2) perform validation, (3) post-validation, can you estimate the time spent on each, as a proportion of your total validation time?

<table><tr><td></td><td>PERCENTAGE OF TIME</td></tr><tr><td>Identify area of validation</td><td>28 (27)</td></tr><tr><td>Perform validation.</td><td>28 (43)</td></tr><tr><td>Post-validation</td><td>28 (26)</td></tr></table>

R. What are the major problems you encounter when performing validation? (If more than one please rank in order of importance) (1=most problematic).

<table><tr><td>Customers not understanding your questions</td><td>4</td></tr><tr><td>Customers not being able to express their ‘world’ or requirements</td><td></td></tr><tr><td rowspan="2">Customers’ lack of understanding of your notation</td><td>22</td></tr><tr><td>2</td></tr><tr><td>Inconsistency between customers’ replies</td><td>14</td></tr><tr><td>Lack of access to knowledgeable customers</td><td>11</td></tr><tr><td>Educating customers in your notation</td><td>0</td></tr><tr><td>Other problems (please specify)</td><td></td></tr></table>

S. Of the total specification and gathered facts, what proportion is actually validated? PROPORTION VALIDATED . . . 28 (82%) ..... (%)

How much of the specification and gathered facts is validated with the customer as opposed to in-house? PROPORTION VALIDATED WITH CUSTOMER. . . 27 (75%)....(%)

T. What are the major problems you encounter after a validation session?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td colspan="4">Manual updating of specifications to incorporate changes</td></tr><tr><td></td><td>13</td><td>12</td><td>2</td></tr><tr><td>Consistency and completeness checking</td><td>18</td><td>10</td><td>0</td></tr><tr><td>General documentation problems because of the volume of data</td><td>11</td><td>12</td><td>4</td></tr><tr><td>Impact of a change on rest of specification</td><td>15</td><td>12</td><td>1</td></tr><tr><td colspan="4">Other problems (please specify)</td></tr><tr><td></td><td>1</td><td>2</td><td></td></tr></table>

U. What factor usually determines that no more validation will take place?

<table><tr><td></td><td>OFTEN</td><td>SOMETIMES</td><td>NEVER</td></tr><tr><td>Lack of project resources</td><td>4</td><td>14</td><td>9</td></tr><tr><td>You have satisfied yourself that the requirements and specification are valid</td><td>15</td><td>13</td><td>1</td></tr><tr><td>The customer is not prepared to continue</td><td>4</td><td>11</td><td>11</td></tr><tr><td>Customer sign-off</td><td>14</td><td>8</td><td>4</td></tr><tr><td>Other factors (please specify)</td><td>2</td><td>1</td><td></td></tr></table>
