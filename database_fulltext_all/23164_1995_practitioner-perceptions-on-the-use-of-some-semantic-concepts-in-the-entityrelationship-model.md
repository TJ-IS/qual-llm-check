---
otero_id: 23164
otero_key: "WVNVN6YP"
title: "Practitioner perceptions on the use of some semantic concepts in the entity–relationship model"
authors: "S. Hitchman"
year: "1995"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.1995.4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Practitioner perceptions on the use of some semantic concepts in the entity–relationship model

S. HITCHMAN

Faculty of Business and Social Studies, Cheltenham & Gloucester College of Higher Education, Cheltenham, Gloucs. GL50 4AZ, UK

This paper seeks to show that aspects of the entity–relationship data modelling method, for the analysis of systems, are not well understood in the commercial domain. Practitioner knowledge of available semantic constructs in the entity–relationship model is measured, together with practitioner perceptions of analyst and client data modelling knowledge. A set of criteria is used to establish practitioner perceptions concerning the usability of data models within the analysis process. The findings provide evidence that practitioners do not understand some key semantic constructs and perceive that other analysts and clients have an incomplete understanding of available model semantics. This empirical evidence from the commercial domain may be useful in improving the effectiveness of the data modelling method through training and further research.

## Introduction

Entity–relationship modelling is a ubiquitous data modelling method in methodologies, for example in MERISE (Tardieu et al., 1984), SSADM (NCC, 1986) and information engineering (Martin & Finkelstein, 1981), and has been in use for at least ten years. Standards used for entity–relationship modelling and the semantic constructs (Date, 1990) employed vary. For example, the entity–relationship standard used in SSADM changed in its version 4 which introduced more semantic constructs (Hitchman, 1990). NIAM (Nijssen & Halpin, 1989), by contrast, represents one of the few methodologies which do not utilise the entity–relationship model, preferring the use of the fact oriented model.

The author began the research described in this paper with an unsubstantiated opinion that some available semantic constructs of the entity–relationship model are not well understood in the commercial domain. This opinion was prompted by involvement in entity–relationship modelling projects and by comments from data administrators who themselves had good modelling understanding. Goldstein and Storey (1990, p 9) have questioned the assertions that the entity–relationship model is:

\- simple and easily understood by non-specialists (Konsynski, 1979);

\- easily conceptualised (Yao et al., 1982);

\- composed of basic constructs which are highly intuitive and provide a very natural way of representing a user's information requirements (Brodie et al., 1984);

\- a model that describes a world in terms of entities and attributes, and is thus the most suitable for computer-naive end-users (Berman, 1986).

Goldstein and Storey claim that these views contradict unsupported assertions that educators find the entity–relationship approach difficult to teach. Their research method was to study transcripts of user discussions with an expert system, and compare the initial and final versions of the data model developed by the user to represent their own business domain. The users were not specifically trained in modelling, and the model is used explicitly for database design. They found discrepancies between entity and relationship definitions and the final database view, concluding that their study supports the assertion that data models are only useful once the user properly understands them. This contradicts the assertions made about the ‘naturalness, intuitiveness and general ease of use’ of the entity–relationship model (Goldstein & Storey, 1990, p 23).

The lack of clarity and detail concerning some semantic constructs in some entity-modelling texts would support the view that information concerning some semantic constructs is not readily available. One example of this concerns recursive relationships. Barker (1989) and Veryard (1992) consider these to be fully optional in business scenarios. Examples of a lack of clarity in describing either the construct or the optionality issue, where the reader could be left with the impression that recursive relationships are mandatory, can be found in Downs (1988, p 89, Figure 3.14c), Longworth (1992, pp 90–91), Skidmore et al. (1992, p 158), Martin and McClure (1988, p 332) and Kroenke (1992, p 103). Texts with detailed and clear statements can be found (Barker, 1989; Martin, 1990; Veryard, 1992). Many texts do not address the issue at all. The research question here is how well are the available semantic constructs of the entity–relationship model understood in the commercial domain? This question can be usefully combined with an examination of the perceived usability and effectiveness of the method for the analysis of systems.

The methodology context for the entity–relationship model raises research difficulties, which are illustrated in Figure 1, a diagram adapted from Jayaratna (1993). The creator, interpreter and user each perceive and apply a potentially different methodology, which means that the research information, and particularly quantitative information, may vary and may be difficult to generalise. Furthermore, the methodology may change with each use. Research into data modelling as a method may be subject to the same problems, and in any case the method will be affected by the methodology context. This paper attempts to use a restricted view of aspects of the data modelling method such that R1, R2 and R3 are more likely to be the same. This is achieved by concentrating research on some of the available semantic constructs. There are other aspects of the data modelling method which are not addressed in this paper.

Empirical work on the use of semantic constructs may improve data modelling effectiveness, since the constructs used in the entity–relationship model represent a key element in requirements specification. Many authors perceive a ‘software crisis’ as motivation for the study of systems analysis. Finkelstein (1989), for example, suggests that in many organizations only 20–30% of programmer resource is available for new application development. Ince (1988) quotes a range of general design causes, with 17% of errors attributed to the need to change data structures. Swatman and Swatman (1992) suggest that Boehm’s study (1976) is the most recent source of empirical data on this issue. Without up-to-date empirical data we cannot be certain where the causes of these problems lie. Swatman and Swatman consider that the improvement of the requirements determination and specification process is perhaps the most important approach to solving these problems. This is supported by Finkelstein (1989), who quotes DeMarco (1982) to show that most errors occur in requirements specifications (56% generally of all errors). These errors account for 82% of correction effort, implying that any improvement to the data model as a systematic specification would be important.

![](/api/attachments/WVNVN6YP/fulltext/images/cd6f67204fab0b43a5d5534d1196cf01b77a8f631ce4d89af557d69a97553fb8.jpg)  
Figure 1 The methodology research context, adapted from Jayaratna (1993).  
M1, M2 and M3 represent different methodologies.  
Factors at M2 or especially M3 cannot be controlled.  
Research is represented by R1, R2 and R3.  
R1 information may differ from R2 and R3 information.

## Research into the usability of the entity–relationship model

Tsichritzis and Lochovsky (1982, p 17) state that:

There has been a good deal of controversy about what is a 'good' or what is the 'best' data model . . . The debate is similar to arguing the relative merits of programming languages. It is very difficult to argue persuasively that one data model is best uniformly. Each data model has its advantages, depending on who is doing the schema design and the realm in which one is working.

This debate emerged with comparisons of logical database models (Lochovsky & Tsichritzis, 1977; Brosey & Shneiderman, 1978; Hoffer, 1982). Brosey and Shneiderman (1978), for example, found that users of the hierarchical model performed better in aspects including comprehension. Hoffer (1982) found that research subjects used a variety of logical data models.

Later research (Juhn & Naumann, 1985; Ridjanovic, 1986; Shoval & Even-Chaime, 1987; Jarvenpaa & Machesky, 1989; Batra et al., 1990) also compared different data modelling approaches, generally in the context of student experiments which look at how easy data models are to learn, and what should be learnt. The research tends to compare different models, measuring ‘correct’ models from given scenarios to produce quantitative results. This approach is criticised by Veryard (1992) since it does not measure modelling effectiveness in a commercial context. The authors do not justify their data modelling standards from a commercial perspective.

Another example of the problem of researching the usability of data models is demonstrated in a recent paper by Campbell (1992), an example of a theoretical argument for the adoption of a ‘better’ diagramming standard than the Chen standard (Chen, 1976, 1983). Campbell argues that the current use of data models, with reference to the Chen standard, is for effective design rather than for effective analysis. The problem with this research is that we do not know whether his arguments will hold with, say, the Oracle data modelling standard, which may offer significant advantages for user communication, and these may or may not outweigh Campbell’s proposed diagramming advantages.

The problem of demonstrating model effectiveness is also illustrated through NIAM. Nijssen shows that the fact oriented and entity–relationship models are complementary in their semantics, but is unable to show or prove that the fact oriented model is more effective. Halpin and Orlowska (1992, p 112) state that fact oriented modelling ‘appears to offer advantages’ generally, but support this with anecdotal evidence. The evidence is based on ‘very positive’ feedback from NIAM users who like the fact that the ‘notation is richer and more intuitive’ than the entity–relationship model.

## Research objectives

Research has not revealed much about the pragmatic and semantic nature of modelling (Beynon-Davies, 1992) in the commercial domain. This paper describes research with the following objectives:

\- To provide empirical work which avoids the issue of what is the ‘best’ model by establishing practitioner knowledge of some available semantic constructs in the entity–relationship model.

\- To establish practitioner perceptions of analyst and client data modelling knowledge.

\- To propose a set of criteria for evaluating entity–relationship modelling and use these to establish practitioner perceptions concerning the usability of data models within analysis projects.

\- To establish which entity–relationship modelling standards are currently used in the commercial domain. Many academic papers cite a Chen standard and use this to draw comparisons. It is important to know if this reflects commercial usage since usability may be affected by the data modelling standard.

## Evaluation criteria

A set of criteria was required to establish practitioner perception of the model usability. According to Kent (1990) models supporting information processing technologies can be judged by pragmatic measures of usefulness, if not correctness. However, despite the widespread use of data modelling, there are only sparsely documented evaluation criteria and these have not been applied to measure the usefulness of specific data modelling standards.

Wilson (1980) provides a measurement of usability for design models. This was an analytical procedure which he used to compare the usability of system R, DBTG (a network model) and NDB (a binary relationship model). Wilson measured the complexity of the concepts used in the data models, from a directed graph of the model concepts. He showed that the relational table model was the least complex, but did not directly conclude that this gave the model higher usability. Wilson referred to the work of Miller (1971), who had looked at factors including the time to learn, time to relearn (for casual users) and time to perform selected application tasks. Wilson suggests that the semantic complexity approach needed to be validated against existing methods of measuring usability.

Veryard (1992, pp 22–23) is perhaps the only source of criteria for a modelling method, accompanied by a clear epistemology. These criteria are stated as a list of general ‘characteristics’. Navathe (1992) cites eight ‘qualities’ proposed by Batini et al. (1992, p 140) that are typical of a conceptual schema but, as these are illustrated by reference to a domain entity–relationship model drawn to Chen standards, they are not used to evaluate the modelling standard.

Martin (1987, pp 56–60) proposes a summary of all that 'good' diagramming techniques should be. While this is concerned with diagrams generally, there are criteria which apply to data models. Sources of criteria for evaluating methodologies also exist (Waserman et al., 1983; Jayaratna, 1986; STARTS, 1987; Law, 1988; Martin & McClure, 1988; Navathe, 1992).

This paper proposes a set of criteria drawn as a synthesised list from all of these sources. These criteria are not presented as complete, but may form a useful starting point for a set of evaluative criteria for data modelling. The final list of 38 criteria is shown in Figure 10. In this figure the criteria are shown in rank order, after analysis of survey response, the original survey coding being maintained.

## Data modelling survey

Against this background, a survey of data modelling was undertaken among data modellers in the UK. The survey targeted practitioners involved in data modelling in the commercial domain by using a mailing list purchased from a national computing magazine which purported to identify a large database administration (DBA)/data administration (DA) group of readers. This list represented a national free weekly circulation, and as a widely read magazine should be representative of practitioners in the UK. A list which separated purely DA job categories or otherwise identified data modellers could not be obtained.

The survey was in two sections. The first section contained questions to elicit information about the respondent, together with five scenarios which respondents were asked to model. These were considered by the questionnaire designer to be clear statements of particular semantic constructs – for example, ‘Employees may manage one or more other employees. An employee only has one manager’. This was expected to elicit a fully optional recursive relationship on employee. Other respondent models which were judged valid were also accepted – for example, some respondents sub-typed employee, in which case one end of the recursive relationship became mandatory. Veryard’s (1992) comments on scenario use advise caution with the use of scenarios. The scenario statements were not designed to test skill against a business domain, rather, they were designed to test knowledge of particular semantic constructs. This is an important point because information concerning the respondents’ ability to model a business domain, using the data model as method, involve more than a knowledge of semantic constructs. In this section respondents were also asked to comment on perceptions of their own, other analysts’ and clients’ understanding of model semantics. In the second section, respondents were asked to complete a grid of 38 criteria. The survey was piloted with several data administrators, which resulted in changes to the wording of both the scenarios and the questions. Some criteria were also dropped at this stage, since they were judged ambiguous or inappropriate.

## Survey respondents

The survey used a list of 736 contacts, about 1% of the total subscription of the national computing magazine. There were 80 completed questionnaires, representing a total response rate of 10.5%. The contacts list was found to contain a large proportion of job categories which were not in the DBA/DA category, together with a large number of names that could not be traced. To confirm that the response was not biased, and to attempt to increase the response rate, a telephone follow up was conducted using 603 names from the list. Figure 2 shows an analysis of this telephone survey.

<table><tr><td>% Response</td><td>Category of response</td></tr><tr><td>21.3</td><td>Non-existent contact</td></tr><tr><td>12.5</td><td>No longer a valid contact (moved)</td></tr><tr><td>2.0</td><td>Company policy not to respond</td></tr><tr><td>32.5</td><td>Non-respondent – not obtainable (holiday etc.)</td></tr><tr><td>12.4</td><td>Phone response from non-data modeller</td></tr><tr><td>3.0</td><td>Phone response from data modeller as survey non-responder</td></tr><tr><td>4.1</td><td>Non-responder despite telephoned promise to respond to survey</td></tr><tr><td>12.2</td><td>Respondent – filled in form</td></tr></table>

Figure 2 Phone response analysis.

This analysis was of a sufficiently large group to show that around 54% of the list (at best) represented the target data modellers. The true response rate is therefore around 20%. This compares favourably with the response rate recently reported for a survey of 41 EIS characteristics (Bergeron & Raymond, 1992). For each question analysed there were consistently at least 75 completed responses. In the following analysis, ‘respondent’ refers to the written survey respondent. A breakdown of respondents’ background is shown in Figure 3, and as in other diagrams n defines the number of cases.

Respondents had a varying, though surprisingly small, number of formal data modelling training days, as shown in Figure 4.

This formal training reflected a wide range of experience measured in years of data modelling, as shown in Figure 5.

![](/api/attachments/WVNVN6YP/fulltext/images/4341dbd17a44cf07580839f0cb01ab69ee10c25f373dd0ff6294de88955c04a0.jpg)  
Figure 3 Respondents' job categories (n = 80).

![](/api/attachments/WVNVN6YP/fulltext/images/1fd6d67d99e80d281836bb8b61285ff10fa2f6db1c4a0a739c41d6c3a97f2d14.jpg)  
Figure 4 Number of days formal data modelling training (n = 76).

![](/api/attachments/WVNVN6YP/fulltext/images/b29575d63b2d4df41eb8a2ebebd54965ba450c3c4c55ad8261899fd60e95c20d.jpg)  
Figure 5 Number of years data modelling experience (n = 79).

The telephone survey confirmed that many non-respondents were not data analysts. A comparison of data modelling experience clearly showed that the majority of non-responders had no data modelling experience.

## Respondents' perceptions of data model use

Data model usage on projects in the workplace was surprising – only 32% of respondents always used data models on projects, 55% sometimes used them, and 13% reported that data models were never used on projects in the workplace. The use of data models with project clients (Figure 6) shows very low levels of client training together with a weak use of models on projects; 40% of clients are not involved in building models, although they are more likely to be asked to 'walkthrough' a model. The information in Figure 6 leads to the conclusion that although project analysts fare better than clients, there is a general lack of understanding of data models. This leads to the assertions that analysts and clients do not find data models generally intuitive in use and that data models are not widely used with active client involvement.

![](/api/attachments/WVNVN6YP/fulltext/images/4ecb9cb8c66f709a00c5c31687acde9de1b96c695f6abf0178fec3fcd519a42c.jpg)  
Figure 6 The use of data models (n > 76).

## Respondents' knowledge of model semantic constructs

Section one of the questionnaire asked for models corresponding to five scenarios. The diagrams for the scenarios were coded according to the author's understanding of the model presented by the respondent. The model was 'registered' if the survey analyst could clearly recognise that the semantic constructs in the diagram modelled the given scenario. The results are used to categorise the diagramming standards used by respondents, together with the knowledge of the respondent about the semantic constructs of the given scenario.

The scenarios were designed to be simple descriptions of recursion, entity sub-types, orthogonal entity sub-types and exclusivity. The research does not consider simple binary relationships in detail, but seeks to establish knowledge of the available constructs required for the analysis of business domains and not the constructs just required for, say, relational structure design. It certainly does not follow that simply the knowledge of semantic constructs will make a 'good' data modeller, since other skills such as political astuteness, interviewing, dealing with multiple realities and facilitating consensus may be important, but are unmeasured in this survey.

Most modellers used the crow's foot to indicate cardinality, and rectangles were widely used for entity boxes. Only 5% of the sample used more than a line to show relationships (in the Chen standard a diamond shape is used). This indicates that academic comparisons with the Chen standard, and discussions of the usability of the Chen standard, may be inappropriate. Half the modellers did not name their relationships, and only 29% named both ends of the relationship. Two-way naming is considered to improve model effectiveness (Barker, 1989), particularly since it offers advantages for client ‘walkthroughs’.

Although 62% of the sample registered the one-to-many recursive relationship, 76% of these made the relationship mandatory at least at one end (or did not clearly show optionality). A recursive relationship was registered by a slightly larger number (79%) for the many-to-many recursive relationship scenario although fewer, 60%, registered the many-to-many cardinality. Of those who registered recursion for the many-to-many scenario, 75% showed mandatory relationships or did not clearly show optionality. The conclusion is that there is a lack of knowledge concerning optionality in recursive relationships, reflecting the informal findings from text sources, and indicating that practitioners do not have a solid grasp of model semantics.

Entity sub-types were clearly modelled by 62% of respondents, who used the syntax representations shown in Figure 7. The 'box in box' notation is standard for IE (Martin, 1990) and Oracle (Barker, 1989). More respondents preferred an arc for each relationship line, rather than a single arc across two relationship lines. The survey provides information that different approaches are roughly equally apparent. However, it is surprising that nearly 40% of respondents could not model sub-types. Some informal discussion with data modellers suggests that there is a 'camp' that deliberately chooses not to use the semantic concept, believing that it is not useful. Several CASE tools do not support the semantic construct, and any response may be within the context of a particular CASE tool. The survey response thus indicates that usability aspects of this single model semantic concept are not clear.

Orthogonal sub-types caused real problems for respondents. Only 29% managed to register these. This supports both informal findings from texts, where few contain information about orthogonal sub-types, and from informal knowledge of modelling course material, which often does not cover this modelling aspect. It could be argued that the effect of not understanding that an entity-type can be partitioned in several different ways means that modellers are not using the method to greatest effect. The information from the survey indicates that only a minority of modellers know about orthogonal sub-typing.

Exclusive relationships were registered by 53% of respondents; 26% were judged to have made an invalid attempt and 15% made no attempt. Some 6% of respondents were judged to have modelled this scenario using another valid representation – which demonstrates the difficulty of framing quantitative research even in scenarios that are constrained. The score here is lower than for single sub-typing, and again reinforces the impression from the previous scenarios that a substantial number of respondents do not understand available semantic constructs.

Respondents were asked to comment on the understanding of the recursive relationship and sub-type semantic constructs by analysts and clients, in addition to a self-appraisal. Figure 8 shows the perceived understanding for the recursive relationship scenario and Figure 9 the results for the sub-type scenario. The modellers' own perception of their understanding of sub-typing agreed with the research analysis of their model. On the other hand, several modellers did not produce the correct models for the recursive scenario but still believed they understood the scenario. In both cases there is a surprisingly strong perception that other analysts and clients will not understand these semantics. The respondents were asked 'Would . . . generally understand the above model?'. The answers thus reflect a perception that these model semantics will be difficult to interpret both during a 'walkthrough' and during involvement in building the model.

![](/api/attachments/WVNVN6YP/fulltext/images/255934ca045e051622fc6e406dda90fbf4689ea44d37fc6453ca9a7e3ee58683.jpg)  
Figure 7 Entity sub-type representation (n = 51).

![](/api/attachments/WVNVN6YP/fulltext/images/e73f94371fd10178a0d217a9462a6b13672e75b5ab536dd83a1bd7e394e31182.jpg)  
Figure 8 Respondent perceptions of recursive relationship scenario understanding (n = 75).

On the overall question of ‘Do you think your current standard of data modelling elicits enough information during analysis to facilitate design?’, around 60% of respondents agreed. About 30% expressed problems in mapping the data model to the physical database objects.

Only five respondents produced diagrams that were judged to represent correctly all of the scenarios. This is a key finding since the scenarios were designed as clearly stated examples of particular modelling semantics. It should be emphasised that the interpretation of ‘correct’ was strict. Mandatory recursive relationships, for example, were not included as ‘correct’. Modellers could be expected to be precise in simple scenarios. Correct data modellers were all engaged in producing relational design specifications, and their experience ranged from 2 to 8 years, with between 0 and 10 formal days of training.

![](/api/attachments/WVNVN6YP/fulltext/images/9717e89f1ea4622d4fbad2bc1e874a583d74e87440507554fc9e98b0d6fe2f8b.jpg)  
Figure 9 Respondent perceptions of sub-type scenario understanding (n = 75).

Thus, the analysis of this first survey section suggests that there are very few modellers in the sample who understand all of the available semantic constructs of models and can apply these accurately to simple scenarios. Arguably, even if practitioners choose not to use such semantics, they should be expected to know about them. Information from the survey also gives very strong evidence to support the assertions that data modelling is poorly understood by analysts and especially by clients. This seems to contradict the commonly held academic proposition that data models are easy to build and understand, and confirms the findings of both informal discussions with data administrators, and of Goldstein and Storey (1990). On the other hand, 60% of modellers believed that they obtained enough information for design, using their data model, making it a viable method. This indicates that the data model is perceived to be a useful method, and information from the grid of perceptions, contained in the second section of the survey, provides information to build on this argument, pointing to where the data model has advantages and weaknesses.

## Respondents' perceptions of modelling usability for analysis

Analysis of perception response will reflect something about modelling in the methodology context. Respondents were asked to comment on the usefulness and usability of data models using the criteria, presented as 'perceptions', discussed in the previous section. The ranked list of criteria is shown in Figure 10 and the original survey code, allocated to each criteria, is used for cross-reference to Figures 12 and 13. Codes also indicate some classification of the criteria. Respondents were asked to consider the model in two analysis phases: the business information strategy phase and the analysis phase. Interpretation of 'business information strategy phase' was not controlled. An information engineer would view this as similar to the information strategy planning phase of information engineering. Respondents were given a clear option to avoid scoring the business information strategy phase if they felt they had inadequate knowledge or experience and around 60% of respondents exercised this option. However, analysis of perceptions of this phase is beyond the scope of this paper, because it raises issues which are beyond the constraints set by seeking to make R1, R2 and R3 the same.

<table><tr><td>Perception</td><td>Code</td></tr><tr><td>As a basis for database generation</td><td>6</td></tr><tr><td>An aid to clear thinking</td><td>1.8</td></tr><tr><td>Encourages good analysis practice</td><td>1.9</td></tr><tr><td>Clearly specifying requirements for design</td><td>6.1</td></tr><tr><td>Relevant in meeting the needs of those involved in the project</td><td>1</td></tr><tr><td>Quality improver</td><td>2.4</td></tr><tr><td>Clear visual logic</td><td>4.6</td></tr><tr><td>Teachable and transferable to team members</td><td>4.8</td></tr><tr><td>Minimum number of types of symbol</td><td>4.5</td></tr><tr><td>Elegant – generating a powerful sense of comprehension</td><td>1.5</td></tr><tr><td>Easy to draw on paper</td><td>4.9</td></tr><tr><td>Communications for the analysis project</td><td>4</td></tr><tr><td>An efficient method</td><td>2</td></tr><tr><td>Consistently effective over many uses</td><td>2.2</td></tr><tr><td>Defining boundaries</td><td>1.3</td></tr><tr><td>Easy to understand</td><td>4.1</td></tr><tr><td>Effective in solving complex problems</td><td>1.7</td></tr><tr><td>Formalised to enable validity checks</td><td>2.6</td></tr><tr><td>Finding and modelling the relevant system</td><td>1.1</td></tr><tr><td>To facilitate client (end) user project involvement</td><td>5</td></tr><tr><td>Ensures that the products of analysis are correct</td><td>2.1</td></tr><tr><td>Meaningful – results are clear, simple and unambiguous</td><td>4.3</td></tr><tr><td>Facilitates computer aided thinking</td><td>7</td></tr><tr><td>Assertive</td><td>4.4</td></tr><tr><td>Readable using English sentences</td><td>4.7</td></tr><tr><td>Facilitates client understanding of the analysis area</td><td>5.1</td></tr><tr><td>An aid to client (end) user communication</td><td>4.2</td></tr><tr><td>Elegant – ingeniously simple</td><td>1.6</td></tr><tr><td>Reducing the cost of projects</td><td>2.5</td></tr><tr><td>Direct work saver</td><td>2.3</td></tr><tr><td>Facilitates client diagnosis of ‘where we are now’</td><td>5.2</td></tr><tr><td>Identifying and involving participants</td><td>1.2</td></tr><tr><td>Facilitates client prognosis of ‘where we want to be and why’</td><td>5.3</td></tr><tr><td>Facilitates stability analysis</td><td>1.4</td></tr><tr><td>As a soft systems thinking conceptual model</td><td>8.1</td></tr><tr><td>For facilitating soft systems thinking</td><td>8</td></tr><tr><td>Facilitates client to identify and define notional systems</td><td>5.4</td></tr><tr><td>Robust, resilient to misuse</td><td>3</td></tr></table>

Figure 10 Ranked analysis perceptions.

Respondents were asked to score each criteria, together with the level of confidence in their answer. The scoring system is shown in Figure 11. These scoring systems are adapted from Law (1988) and STARTS (1987). The information provided may be useful in identifying more precisely which criteria to use when assessing data modelling.

KEY Please score each

criterion by ringing one of

the following values:

0 Makes things worse

1 No support/no effect

2 Poor support/not very beneficial

3 Good support/very beneficial

4 Excellent/ideal support

Please indicate your level of

confidence in answering each

question by ringing one of the

following values:

1 Inadequate basis

2 Limited confidence

3 Confidence based on practical experience

4 Very confident, based on considerable experience in a wide range of situations

Figure 11 Scoring and confidence criteria.

The results indicate a general feeling that data models offer good support and are very beneficial. This is stronger in some perceptions than in others. Most average scores over 2.4 carry modal scores of 3. Figure 12 shows the perception rankings for data models used in the analysis phase of projects, together with the mean confidence scores. The model as a design specification scores highly, clearly being perceived as a basis for database generation. The model is perceived as generally relevant, being an aid to clear thinking and encouraging good analysis practice. Clear visual logic, teachability and transferability also rate highly. However, communications with project clients scores lower, and the model is not popular as an ‘assertive’ tool. Confidence dips sharply with stability analysis and with soft systems aspects. Interestingly the model scores lowest on ‘robust and resilient to misuse’. This seems to give further support to perceptions that other analysts will not understand some model semantics.

Figure 13 shows a comparison of scores for three groups, drawn against the general analysis score. The three groups consist of DBAs, ‘correct data modellers’ and a combination of data administrator and specialist data modellers (the ‘specialists’) categories from the job factor. There are overlaps in these groups. Clearly both specialists and correct modellers perceived the data model to be generally more useful. Many of these differences were significant and the trend is clear. Correct modellers have notable differences from specialists, perceiving the model to be more of a quality improver, but not regarding the model so highly for being meaningful, clear, simple and unambiguous. This is an interesting conflict, and could reflect the fact that the model tends to encourage quality, while having weaknesses. To illustrate this, consider the cross-tabulation of recognition of orthogonal sub-types with the perceptions of relevance (1) and client communication (4.2). Those respondents who registered orthogonal sub-types rated the model significantly higher for relevance, but gave a lower rating for communication. Arguably the knowledge of the orthogonal sub-type could be seen as reinforcing the relevance aspect of the model. Conversely this will diminish the ease of use for communication – the knowledge of orthogonal sub-types could indicate that the model is complex and so less easy to use for communicating.

![](/api/attachments/WVNVN6YP/fulltext/images/b01bb0f569fc5d43dc8d4d652761500554707bd68468f95cd5abb4425a44a96f.jpg)  
Figure 12 Mean scores for analysis perceptions, together with confidence ( $n \simeq 73$ ).

![](/api/attachments/WVNVN6YP/fulltext/images/464e98c9acaee8ab8ce0092b96e8e0694cd66d1e9db0141d80902c2d47bb7287.jpg)  
Figure 13 A comparison of best, modellers' $(n\simeq 5)$ , DBAs' $(n\simeq 26)$ , specialist + data administrator's $(n\simeq 27)$ scores.

The DBA's scored the model lower than both the specialists and the correct modellers, although DBAs regarded the model as generally useful for specifying a database. The notable difference is the DBA's ranking of the model as not particularly relevant to meeting the needs of those involved in the project. This could be interpreted as their own dissatisfaction with the semantic content of the model, or their dissatisfaction with the method.

## Conclusions

A significant number of practitioners do not seem to understand some available semantic constructs of the entity–relationship model. More particularly there is a general perception that analysts and particularly users lack understanding of these semantic constructs. Given the ubiquitous and lengthy use of the model, this implies that the model lacks usability.

A possible explanation for this is that the concepts discussed are not found, explicitly, in the relational model. If the entity–relationship model is seen as a data structure method then, arguably, the findings do not show that respondents could not produce relational data structures. For example, the correct identification of the fully optional ‘one-to-many’ recursive relationship does not result in a relational structure different from a recursive relationship which is mandatory at the 'one' end. The issue discussed is whether the analysis participants will obtain an effective understanding of the business domain using the available semantic constructs of the model. Thus one interpretation of the findings is that the semantic constructs examined may be supporting more subtle aspects of the analysis process. For example, an explicit understanding of orthogonal sub-types may not aid in pragmatic relational table design (other than by identifying null attributes), but would facilitate understanding of the business domain.

If the participants in the analysis process improved their knowledge and understanding of these semantic constructs then more effective analysis is potentially available. This improvement is against a background in which the model seems to be rated highly against usability criteria. Respondents with the greatest knowledge of the semantic constructs tended to rate the model more highly, suggesting that the usability of the model may be enhanced by training analysts and users, although the quality of the training, rather than the number of training days, seems to be an issue. The usability scores have also ranked the criteria, highlighting the most useful aspects of the model. This may also help to make the model more effective by increasing understanding of how the model supports the analysis process.

The research has demonstrated that even when constrained by a particular method, the skills and knowledge of practitioners and other analysis participants will vary, as will perceptions concerning usability. This supports the view of methodology research shown in Figure 1. The findings also indicate that research based on, for example, the particular syntax of a diagramming standard, such as Chen, may not reflect the situation in the commercial domain. It would be interesting to examine why some users are always involved in building and reading data models. Is this due to some common perspective?

## References

BARKER R (1989) Case\*Method: Entity Relationship Modelling. Addison-Wesley, Reading, Massachusetts.

BATINI C, CERI S and NAVATHE S B (1992) Conceptual Database Design: An Entity Relationship Approach. Benjamin Cummings, California.

BATRA D, HOFFE J A and BOSTROM R P (1990) Comparing representations with relational and EER models. Communications of the ACM 33(2), February, 126–139.

BERGERON F and RYMOND L (1992) Evaluation of EIS from a management perspective. Journal of Information Systems 2, 45–60.

BERMAN S (1986) A semantic data model as the basis for an automated database design tool. Information Systems 11(2), 149–165.

BEYNON-DAVIES P (1992) The realities of database design. Journal of Information Systems 2, 207–220.

BOEHM B W (1976) Software engineering. IEE Transactions on Computers 12, 1226–1241.

BRODIE M L, MYLOPOULOS J and SCHMIDT J W (Eds) (1984) On Conceptual Modelling. Springer-Verlag, New York.

BROSEY M and SHNEIDERMAN B (1978) Two experimental comparisons of relational and hierarchical database models. Journal of Man–Machine Studies 10, 625–637.

CAMPBELL D (1992) Entity–relationship modelling: one style suits all? Database Summer, 12–18.

CHEN P P-S (1976) The entity relationship model: towards a unified view of data. ACM Transactions on Database Systems 1(1), March, 9–36.

CHEN P P-S (1983) A preliminary framework for entity relationship models. In Entity Relationship Approach to Modelling and Analysis, Proceedings of the Second International Conference on Entity-Relationship Approach (CHEN P P-S, Ed.). Elsevier Science, Amsterdam.

DATE C J (1990) An Introduction to Database Systems, Vol. 1, 5th edn. Prentice-Hall, Englewood Cliffs, New Jersey.

DEMARCO T (1982) Software Systems Development. Yourdon Press, Englewood Cliffs, New Jersey.

DOWNS E (Ed.) (1988) SSADM, Application and Context. Prentice-Hall, Maidenhead, UK.

FINKELSTEIN C (1989) An Introduction to Information Engineering: From Strategic Planning to Information Systems. Addison-Wesley, Reading, Massachusetts.

GOLDSTEIN R C and STOREY V C (1990) Some findings on the intuitiveness of entity–relationship constructs. In Entity–Relationship Approach to Database Design and Querying (LOCHOVSKY F H, Ed.). Elsevier Science, Amsterdam.

HALPIN T A and ORLOWSKA M E (1992) Fact oriented modelling for data analysis. Journal of Information Systems 2, 97–119.

HITCHMAN S (1990) Data modelling standards. Computing 11 October 1990, pp 44–46.

HOFFER J A (1982) An empirical investigation into individual differences in database models. In Proceedings of the Third International Conference on Information Systems, December 1982, pp 153–168.

INCE D (1988) Software Development: Fashioning the Baroque. Oxford University Press.

JARVENPAA S L and MACHESKY J (1989) Data analysis and learning: an experimental study of data modelling tools. International Journal of Man-Machine Studies 31, 367–391.

JAYARATNA N (1986) Normative information model-based systems analysis and design (NIMSAD): a framework for understanding and evaluating methodologies. Journal of Applied Systems Analysis 13, 73–87.

JAYARATNA N (1993) Methodological challenge for information systems. In Proceedings, Conference on the Theory, Use and Integrative Aspects of IS Methodologies (JAYARATNA N, PATON G, MERALI Y and GREGORY F, Eds), Heriot-Watt University, Edinburgh, 1–3 September. British Computer Society Information Systems Methodologies Specialist Group.

JUHN S and NAUMANN J D (1985) The effectiveness of data representation characteristics on user validation. In Proceedings of the Sixth International Conference on Information Systems, pp 212–226.

KENT W (1990) The leading edge of database technology. In Entity-Relationship Approach to Database Design and Querying (LOCHOVSKY F H, Ed.), pp 3–7. Elsevier Science, Amsterdam.

Konsynski B R (1979) Data Base Driven Systems. University of Arizona.

KROENKE D M (1992) Database Processing. Macmillan, New York.

LAW D (1988) Methods for Comparing Methods, Techniques in Software Development. NCC, Manchester.

LOCHOVSKY F H and TSICHRITZIS D C (1977) User performance

## About the author

Steve Hitchman is a senior lecturer in the Faculty of Business and Social Studies, teaching data modelling modules to undergraduate students and to practitioners, as well as providing data modelling consultancy. His research interests

considerations in DBMS selection. In Proceedings of ACM SIGMOD, August, pp 128–134.

LONGWORTH G (1992) A User's Guide to SSADM Version 4. NCC Blackwell, Oxford.

MARTIN J (1987) Recommended Diagramming Standards for Analysts and Programmers. Prentice-Hall, Englewood Cliffs, New Jersey.

MARTIN J (1990) Information Engineering - A Trilogy. Prentice-Hall, New York.

MARTIN J and FINKELSTEIN C (1981) Information Engineering, Vols 1 and 2. Prentice-Hall, Englewood Cliffs, New Jersey.

MARTIN J and McCLURE C (1988) Structured Techniques: The Basis for Case. Prentice-Hall, Englewood Cliffs, New Jersey.

MILLER R B (1971) Human Ease of Use Criteria and their Tradeoffs. IBM Poughkeepsie Technical Report TR 00.2185, April.

NAVATHE S B (1992) Evolution of data modelling for databases. Communications of the ACM 35(9), September, 112–125.

NCC (1986) SSADM Manual. National Computing Centre, Manchester.

NIJSSEN G M and HALPIN T A (1989) Conceptual Schema and Relational Database Design: A Fact Oriented Approach. Prentice-Hall, Sydney.

RIDJANOVIC D (1986) Comparing Quality of Data Representations Produced by Non-Experts Using Logical Data Structure and Relational Data Models. PhD Dissertation, University of Minnesota. Reported in Batra et al. (1990).

SHOVAL P and EVEN-CHAIME M (1987) Data base schema design: an experimental comparison between normalisation and information analysis. Data Base, Spring, 30–39.

SKIDMORE S, FARMER R and MILLS G (1992) SSADM Version 4 Models and Methods. NCC Blackwell, Oxford.

STARTS (1987) The STARTS Guide, 2nd edn. NCC, Manchester.

SWATMAN P A and SWATMAN P M C (1992) Formal specification – an analytic tool for (management) information systems. Journal of Information Systems 2(2), April, 121–160.

TARDIEU H, ROCHFELD A, COLLETTI R and LESOURNE J (1984) La Methode Merise: principles et outils. Les editions d'organisation.

Tsichritzis D and Lochovsky F (1982) Data Models. Prentice-Hall, Englewood Cliffs, New Jersey.

VERYARD R (1992) Information Modelling: Practical Guidance. Prentice-Hall (BCS Practitioner Series), Englewood Cliffs, New Jersey.

WASERMAN A et al. (1983) Characteristics of software development methodologies. In Proceedings of IFIP TC8 Working Conference on Feature Analysis of Information System Design Methodologies (OLLE et al., Eds), York, UK, July.

WILSON M L (1980) The measurement of usability. In Entity Relationship Approach to Systems Analysis and Design, pp 75–101 (CHEN P P-S, Ed.). North-Holland, Amsterdam.

YAO S B, NAVATHE S B and WELDON J L (1982) An integrative approach to database design. In Database Design Techniques I: Requirements and Logical Structures Proceedings (YAO S B, NAVATHE S B and WELDON J L, Eds), May. Also in Lecture Notes in Computer Science (GOOS G and HARTMANIS J, Eds). Springer-Verlag, New York.

include the use of knowledgebase models for the analysis of commercial systems and the development and implementation of data modelling standards and policies within commercial MIS departments.
