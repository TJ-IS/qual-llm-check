---
otero_id: 23884
otero_key: "CQSDBUG4"
title: "An analysis of expert systems for business decision making at different levels and in different roles"
authors: "J S Edwards; Y Duan; P C Robins"
year: "2000"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000344"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.stockton-press.co.uk/ejis

# An analysis of expert systems for business decision making at different levels and in different roles

JS Edwards<sup>1</sup>, Y Duan<sup>2</sup> and PC Robins<sup>1</sup>

<sup>1</sup>Aston Business School, Aston University, Birmingham, B4 7ET, UK; <sup>2</sup>Luton Business School, University of Luton, LU1 3JU, UK

This paper begins by analysing decision making activities and information requirements at three organizational levels and the characteristics of expert systems (ESs) intended for the two different roles of support ing and replacing a decision maker. It goes on to review the evidence from many years of commercia use of ESs at different levels and in different roles, and to analyse the evidence obtained from a pilot experiment involving developing ESs to fulfil two different roles in the same domain. The research finds that ESs in a replacement role prove to be effective for operational and tactical decisions, but have limi tations at the strategic level. ESs in a support role, as advisory systems, can help to make better decisions, but their effectiveness can only be fulfilled through their users. In the experiments, an expert advisory system did not save a user’s time, contrary to the expectations of many of its users, but an ES in a replacement role did improve the efficiency of decision making. In addition, the knowledge bases of the ESs in the different roles need to be different. Finally, the practical implications of the experience gained from developing and testing two types of ESs are discussed.

## Introduction

Expert systems (ESs) were among the earliest branches of artificial intelligence (AI) to be commercialised and still constitute a growing segment of computer-based information systems (Moody et al, 1998). Many organizations have leveraged the technology to increase productivity and profits through better business decisions (Durkin, 1996), even if the impact of ESs has not achieved the levels predicted in the 1980s. Although there have been some failures (O’Keefe & Rebne, 1993; Wong, 1996), recent research (Yoon et al, 1995; Kunnathur et al, 1996) shows that there are many companies who remain enthusiastic proponents of the technology and continue to develop important ES applications. As Gill (1995) has found, successes in several ESs have amply demonstrated the technology’s capability both to generate huge financial returns and to contribute to the strategic goals of the firm. However, Tsai et al (1994) argue that the benefits of ESs are often oversold to the business community by supporters and vendors. The performance of implemented ESs frequently does not measure up to the unrealistic expectations of the users and managers; thus, they view claims for ES benefits with scepticism and disappointment. Clearly there remains a divergence of attitude towards the use of expert systems.

In these circumstances, the need to assess the value of ESs and assure implementation success becomes even more important (Yoon et al, 1995). At the start of the decade, the ES field was characterised as having a wide range of theoretical viewpoints, but an absence of generally accepted theory in many important areas (Bramer, 1990). This is still particularly true when discussing the use of ESs in the business decision making area. This paper addresses two key issues regarding the application of ESs, which may be stated as follows:

(1) At which organizational level? A commonly adopted framework suggests that the decision making activities in an organization can be divided into three levels: strategic, tactical and operational. The problems encountered generally vary from unstructured to structured between strategic and operational levels. A source of confusion is whether the level is that of the decision or that of the decision maker.

(2) In what roles? ESs can be designed for two different purposes, to support or replace a decision maker. An ES in a support role is also known as an expert advisory system; the two terms will be used interchangeably here.

Two ESs with different roles were developed for this research, using a business game as a simulated organization. One (EXGAME) was designed to replace a human in decision making, while the other (ADGAME) was an advisory system to support human decision makers. The two ESs were built to mimic decision making in a business game environment which simulates a manufacturing company. The evaluation of EXGAME provides some insight into the ES’s ability to work successfully at different organizational levels. The tests of ADGAME shed some light on the effectiveness of an expert advisory system and users’ opinions and behaviour towards using it. Detailed descriptions of EXGAME’s and ADGAME’s development, experiment design, research hypothesis and result analysis are presented elsewhere (Duan et al, 1995, 1998).

This paper concentrates on issues associated with differences in organizational level, and differences between two ESs performing in different roles in the same domain. It is intended that this analysis will provide a more systematic and a better understanding of the development and use of different kinds of ESs for business decision making.

## Theoretical framework

There is no doubt that the success of an organization depends on the ability of its managers to make good decisions, and to make them at the appropriate time. However, both the managers and their decisions span a range of types, and in this section we introduce a framework for viewing organizational decision making as a means of looking at them.

## A framework for analysing decision making in organizations

Anthony (1965) identified three levels of decision making, which are closely associated with levels of managerial responsibility. He called them strategic planning, management control and operational control, although more recently the terms strategic, tactical and operational decisions are often used instead.

Strategic planning is designed to answer for the longterm integrity of the organization as a whole, in effect defining the goals and nature of the organization. In ‘for profit’ organizations, this is the truly entrepreneurial aspect of management where, for example, the decision to move to a related area of activity is made. The range of possible moves, the requirement for information from sources external to the organization, and the use of criteria that originate in general business aspirations rather than specific organization concerns has led to these decisions being typically referred to as unstructured (Simon, 1977).

At the management control or tactical decision level, strategic goals are interpreted into targets and operating criteria. Compared to the strategic level, this process has relatively clear boundaries, set by the strategic choice made, and so decisions at this level tend to be more structured.

At the operational control level, the decisions involved are even more precise and limited in range, being concerned with managing the day-to-day activities of an individual division in the light of criteria established at the management control level. The decisions tend to be still more structured, relying mainly on information sources internal to the organization.

The boundaries between these three categories are often not clear. Below them there is a fourth level of activity, usually called transaction processing in the information systems literature, in which ‘decisions’ are not required; everything is fully programmed/structured, in the sense of Simon (1977).

Figure 1, based on the work of Gorry and Scott Morton (1971), shows a general framework presenting the nature of decision making activities in an organization related to the three levels of decision making proposed by Anthony. Although decisions can, in principle, appear anywhere in the framework, it has been suggested by Barrett and Beerel (Beerel, 1987; Barrett & Beerel, 1988) and Silver (1991), among others, that they tend to cluster towards the diagonal, i.e. that most strategic planning decisions are unstructured, while most operational control decisions are structured. If it is accepted that Anthony’s categories provide a framework that becomes increasingly organization-specific at the lower levels, this result would be expected. It also reflects the level of challenge for knowledge engineers building ESs, this time in the reverse order, and might therefore be reflected in observed developments.

Gorry and Scott Morton’s framework has been used by a number of authors in the DSS/ES area (e.g. O’Leary & Turban, 1987; Doukidis, 1988; Er, 1988; Turban & Aronson 1998), although it is by no means the only framework that has been used to consider organizational implications of ESs. For example, Perrow’s framework for technology analysis, based on a classification of technology/transformational process, was used by O’Keefe and Rebne (1993) to discuss ES applications in accounting and finance. By contrast, Gill (1996) uses a two-level task-change model, based on job design theory, to examine ES use both at the task-level and the job-level.

The analysis and discussion of ES usage in this paper follows the general framework based on Anthony and shown in Figure 1, for two main reasons. The first is that the majority of the previous literature on ESs applications is based on either Anthony’s three control levels or Simon’s structured and unstructured decisions (see analysis in next section). The use of the same framework should make it much easier to classify and analyse the previous results. Secondly, the chosen framework reflects both the structure of the simulated business environment (the business game), and the way in which the topic of management decision making had been taught (in a different module) to the students who were concerned in the experiments. This should thus minimise any problems due to misunderstanding of the terminology used.

![](/api/attachments/CQSDBUG4/fulltext/images/4a287e01c525e496bb4978b44e806aadf5d9ddc2ff7949654e34036b1b75c990.jpg)  
Figure 1 A framework for analysing decision making activities in organizations.

## The use of expert systems at different organizational levels

We begin this section by looking at the range of expectations shown in the 1980s. Gibson and Vedder (1989) explained that as ESs are impervious to pressure and provide timely, consistent, and uniform help for making decisions, they could assist at all three organizational decision levels. Barrett and Beerel (1988), by contrast, saw the most evident use for ESs as being in the middle level, i.e. addressing problems which are neither highly structured nor totally unstructured. O’Leary and Turban (1987) pointed out that since ESs are designed for tasks in narrow domains, the greatest use of ESs would occur in operational control decisions, and ESs would be used least readily in strategic planning because many tasks in strategic planning involve broad domains and many variables. Lin (1986) reached the same opinion by a slightly different route. He argued that since routine, repetitive decisions are the best candidates for ESs, and there are more routine, repetitive decisions at the lower levels of management, it could be predicted that many ESs would be for operational planning and control; few systems would be designed for strategic planning which is not highly repetitive.

The reported use of ESs appears to be principally at the operational level. Table 1 presents three sets of survey results on the proportion of ES applications at different decision making levels. Other surveys (Coakes & Merchant, 1996; Eom, 1996) do not specifically identify percentages, but their results follow a similar pattern. The question of whether the level is that of the decision or the decision maker is also important here. All the surveys so far cited appear to have been based on the level of the decision. Connell and Powell (1990), by contrast, looked at the decision maker, i.e. the user. Their conclusion was that most users of ESs were at junior levels of responsibility. It is perhaps significant that the largest published catalogue of expert system applications (Durkin, 1993) does not classify them by the level of the decision or the type of user at all.

Table 1 ES applications at different decision making levels

<table><tr><td>Decision making level</td><td>Doukidis (1988)</td><td>Vijayaraman &amp; Osyk (1994)</td><td>Wong &amp; Monaco (1995)</td></tr><tr><td>Strategic</td><td>3%</td><td>8%</td><td>7%</td></tr><tr><td>Tactical</td><td>24%</td><td>19%</td><td>34%</td></tr><tr><td>Operational</td><td>78%</td><td>73%</td><td>59%</td></tr></table>

As Wong and Monaco (1995) point out, the small proportion of ESs for strategic level decisions may suggest that either ESs are not good at the strategic level or that their potential has yet to be realised. A third possibility is that there are few experts in strategic planning whose expertise may be used in an expert system. On the other hand, since decision support systems usually focus on the higher organizational levels, it should be reasonable to expect that ESs can be used at the higher levels in a support role. In practice, they have not been reported to be in common use at that level. However, Connell and Powell (1990) found a pattern in the responses they received from senior management that could be interpreted as ‘if I use it myself, it is a decision support system; if my subordinates use it, it’s an ES’.

To summarise, there are, after all, more operational control decisions to be made than strategic planning ones, and in most organizations more people will be involved in making similar decisions at the lower managerial levels than the higher ones. It is not surprising therefore that ESs for the operational decision level are the most numerous. The pure counting strategies of these surveys have thus only provided a partial answer to the question ‘at what level is an ES most useful?’

## Expert systems in different roles

At any organizational level, ESs can be developed for performing two fundamentally different roles: one is a support role, such as giving advice or suggesting a solution to a problem, and the other is a replacement role, actually making the decision.

In a support role, the system may be designed to support non-experts (in most cases) or to support experts. It assists human beings in making decisions but it does not replace them; the human still makes the decision.

In a replacement role, it is the system, not the end user, that makes the final decision. Note that this does not necessarily mean that it leaves a human without a job; often a replacement ES simply enables the job to be done by a different, ‘less expert’ person. However, an ES may sometimes be used to replace an expert, or to replace an assistant or non-expert who formerly worked with the expert.

Example of ESs in different roles suggested in the literature are shown in Table 2.

As Table 2 shows, the majority of functions envisaged for ESs in the literature fall under the heading of a support role, rather than a replacement one. All the ESs in a replacement role appear to retain a human user except for the function identified as task automation by Coursey and Shangraw (1989) and automaton by Edwards (1991).

Table 2 ES functions in different roles suggested in the literature

<table><tr><td>Suggested by</td><td>Replacement role</td><td>Support role</td></tr><tr><td>Basden (1984)</td><td>Consultancy Training</td><td>ChecklistRefining expertiseCommunicationmediaDemonstrationvehicle</td></tr><tr><td>Ernst and Ojha (1986)</td><td>Action</td><td>ExpertiseAdviceCheck-list</td></tr><tr><td>Barrett and Beerel (1988)</td><td>To replace an expert</td><td>An additional expertAn adviserAn assistantA knowledge servant</td></tr><tr><td>Coursey and Shangraw (1989)</td><td>Task automationExpert replicationTraining</td><td>ConsultativeExploratory systemConventional taskInterface</td></tr><tr><td>Edwards (1991)</td><td>Expert consultantTutorAutomaton</td><td>AssistantCriticSecond opinion</td></tr><tr><td>Underwood (1992)</td><td>Stand-alone system</td><td>Embedded systemExpert assistantsystem</td></tr></table>

In the 1980s work, opinions differed about what the role of an ES should be. Many authors saw ESs almost entirely in a support role. For example, ‘it should be stressed that ESs are most sensibly used as tools to assist rather than to replace.’ (Hart, 1989); and ‘ESs are not intended to replace the decision maker but to assist people in dealing with various problems’ (Cheng & Bizruchak, 1991). Ow and Smith (1987), on the other hand, argued that in certain cases ESs may replace people in their jobs (though they did not mention what the cases were), but that more frequently, they play the role of intelligent consultants in decision making—again a support role.

It is worth noting at this point that experience with other types of information systems suggests there may be a long time lag between the introduction of the system and its effect on jobs. For example, the UK retail banking sector had computerised most of its processing by the mid-1970s, but large-scale redundancies of clerical staff did not begin until around 1990, because efficiency did not become an important objective for UK banks until the sector was opened up to wider competition in 1987. Nevertheless, the information systems helped to make the later redundancies possible (Morris & Westbrook, 1996).

A survey carried out by Doukidis in 1988 found that of 67 ES applications investigated, 87% were in a support role (supplying expert advice) while the remaining 13% were in a replacement role (replacing human experts but not the end users). Another survey carried out by The Systems International/es (Connect) (1989) found that 8% of the surveyed ESs were to replace humans. These surveys appear to contradict the comments of Hart, Barrett and Beerel, but this may be due to how they define and understand ‘replacement’; whether the expert is replaced completely, or whether some of the expert’s functions can be replaced by an ES.

Unfortunately, no recent surveys have attempted to identify the roles of ESs. On the basis of those ESs reported in the literature, it appears that most ESs may be designed for a support role, while some of them— around 10%—are built for a replacement role, with a non-expert human end-user ‘feeding’ the system. The use of an ES to replace humans completely is rare, but a few systems of this type do exist, mostly self-diagnosing machines (Hui et al, 1996; Guan & Graham, 1996), or process planning systems which automatically convert the design specification of a product into a process plan without human intervention (Joshi et al, 1988).

## Evaluating expert systems

Evaluation is used here as the overall term covering all aspects of assessing an ES. It includes within it verification, validation and user acceptance (Preece, 1990).

Verification checks the internal correctness and consistency of the system. O’Keefe and Preece (1996) define verification of an ES as being to demonstrate that the system has been built in conformance with a number of well-defined properties, chiefly freedom from logical conflict, redundancy, and deficiency.

Validation checks the correctness of the system with respect to the user’s requirement (Grogono, 1991).

Much has been written on the importance of user acceptance in ES implementations (Madni, 1988; Rees, 1992; Suh & Suh, 1993; Yoon et al, 1995; Gill, 1996; Yoon et al 1998). Gill’s study found that user commitment to ESs could be assured by enhancing intrinsic motivators of control, arousal, and achievement. These ‘more motivating’ systems continued to thrive for at least five years after they were built.

Gill’s study was based on 52 ESs in which the task performer before and after the introduction of the ES was the same; by definition, these ESs must all be in a support role. User acceptance is likely to play a less significant part for ESs in a replacement role than for those in a support role, because of the nature of the user interaction. Indeed, for a replacement ES intended to automate the task completely, user acceptance is largely irrelevant, as there is no user in the normal sense. Nevertheless, automated systems (like all systems) must fit into the wider organizational systems, and be accepted there.

Evaluation as a whole, and especially validation, needs careful consideration of whether the main concern is with effectiveness, efficiency, or both. Decision support systems are generally regarded as being intended to improve the effectiveness of decision making rather than its efficiency (Turban & Aronson, 1998), although there are some dissenters from this view. Accordingly, an ES in a support role must also be primarily intended to improve the effectiveness of decision making. The ES literature agrees (Schumann et al, 1989; Oz et al, 1993) that an expert advisory system is able to improve the effectiveness of the user’s decision making, but some disagreement exists as to whether an ES in a support role should improve the efficiency of decision making or not. Hadden (1986) suggested that speeding up the decision making process was a typical benefit of an expert advisory system, but Townsend and Feucht (1986) argued that the question-and-answer dialogue used in KBSs/ESs was often slow. Schumann et al, (1989) and Oz et al (1993) felt this issue was still in question. This view seems to be justified, because two more recent papers in the same journal issue came to opposite conclusions about saving time for ESs in support roles. An ES for a credit union halved the time for each assessment (Agarwal et al, 1994); yet an expert system for diagnosing tropical diseases increased the time taken for each consultation (Doukidis et al, 1994).

However, an ES in a replacement role, especially automation, must clearly be able to work efficiently as well as effectively. It is generally agreed (Turban & Watkins, 1987; Ansari & Modarress, 1990) that ESs replacing a human decision maker can make decisions not only as well as a human but also faster.

The confusion persists: a recent paper on ES in banking (Shao, 1998) found that the use of ESs could improve both effectiveness and efficiency, but did not indicate what roles these banking ESs played in decision making.

Process aspects ought also to be taken into account in evaluating ESs acting in a support role; in particular, does the system enable the users to learn to make better decisions in the future? There have been anecdotes circulating in the ES community for at least a decade about advisory ESs that were taken out of use after a period because the users had learned how to do the job without them, but no account of such a case appears to have been published.

## Research hypotheses

As discussed above, the previous literature on ESs has failed to provide a clear picture on the effectiveness and efficiency of ESs, especially in different roles and at different levels. Therefore, we hypothesised that both EXGAME and ADGAME would improve both effectiveness and efficiency (H1, H2 and H3). In terms of the knowledge base required for ESs in different roles in the same domain, since no research has been conducted on this topic, we postulated that ESs in a supporting role would use the same knowledge base as ESs in a replacement role (H4). Finally, we wished to test whether the users of ESs in a supporting role did in fact believe they learned from the use of the ES (H5).

In the light of above assumptions, the following research hypotheses were formulated:

H1a EXGAME would improve the effectiveness of decision making at the strategic level.

H1b ADGAME would improve the effectiveness of decision making at the strategic level.

H2a EXGAME would improve the effectiveness of decision making at the tactical and operational levels.

H2b ADGAME would improve the effectiveness of decision making at the tactical and operational levels.

H3a EXGAME would improve the efficiency of decision making.

H3b ADGAME would improve the efficiency of decision making.

H4 Both EXGAME and ADGAME would perform well with the same knowledge base, i.e. there would be no need for different knowledge bases for ESs in different roles.

H5 ADGAME users would believe that they had learned from using it.

## Research method

The research adopted an experimental method, using ESs in a simulated business environment. An experimental study helps to assess ES benefits more objectively. It also provides more realistic and convincing evidence for ES developers and business practitioners and thus helps to avoid unrealistic user expectations. Experimental testing of ESs in a real organization presents difficulties, however. An experiment with an ES in a replacement role, especially one for strategic level decisions, would be quite risky, because of the problem of anticipating its possible effects. For an advisory system, if the ES’s use is compulsory, then an experiment cannot reveal the differences between aided and unaided users unless nothing else is changing over time, which is unlikely; while in many applications it would be operationally dubious to make the use of the ES optional. So, using an ES in an artificial environment enables the experimenter to have better control of the tests, repeat some tests easily, and do them more quickly.

However, in fully controlled ‘laboratory’ experiments involving human subjects, there is a problem of ensuring that the subjects perform as they would in the real world. Small numbers of subjects may be given an incentive in the form of payment, but for larger numbers working in teams, as in two of the experiments in this case, the choice was made to use a business game that was part of students’ course work in order to provide ‘external’ motivation that would be more comparable to that in the real business world. A fully controlled experiment in such circumstances would not have been fair to the students; we chose to make this trade-off in the direction of realistic motivation and imperfect control rather than perfect control in an unrealistic situation.

## Experiments with ESs

The complex real organizational environment was replaced by the more limited and controllable conditions of a business game, ‘[a] realistic, dynamic simulation of the actual business operation of a company’ (Broom, 1969).

The game in question simulates a small manufacturing organization that makes vehicle exhaust systems from sheet metal which is purchased as raw material. In each running of the game, six teams compete with each other over twelve periods. Each team ‘manages’ one company and must make decisions in each period in five functional areas: production, sales, marketing, personnel and R&D. There are seventeen decisions (comprising 43 decision parameters) to be entered into the game computer system each period. The game is normally played annually by students as part of a Bachelor’s degree in management, which made the competition of ESs against human rivals possible.

Two ESs were built to operate in this (simulated) domain. The first is EXGAME, which manages the simulated organization itself with little user intervention; a replacement role. To maintain relevance to the realworld of business, EXGAME was built without the benefit of access to the computer-based algorithms which calculate the effects of the game players’ decisions. The second ES, ADGAME, is intended to act as an advisor and not as a decision maker; a support role. A more technical description of EXGAME may be found in Duan et al (1998) and one of ADGAME in Duan et al (1995).

Three experiments were conducted, referred to here as experiments A, B and C. Experiments A and B were carried out along with undergraduate students’ course work; experiment C was conducted purely for this research. The experiments A and B were conducted in different academic years, and involved all undergraduates who took the management course in that year. The participants in experiment C were paid to do so and included experienced student game players and a game tutor. EXGAME was used in all three experiments and was assigned to play one team in all experimental groups, except group d in experiment A, in which the EXGAME developer played instead of EXGAME; ADGAME was used in experiments B and C only. A brief description of the three experiments is shown in Table 3. Detailed information on experiment design may be found in Duan et al, 1995 and 1998.

Students’ performance in playing the game is measured along three dimensions:

I their ability to run the company at a profit;

I the quality of their decision making process;

the general state of the company at the end of the game, especially avoiding the use of an ‘end of the world’ strategy to artificially inflate profits in the final period(s).

EXGAME was therefore measured on the same criteria, as were the users’ achievements with the support of ADGAME. As discussed above, a survey of user opinion was carried out for ADGAME, but not for EXGAME because of its automaton role.

## Results analysis and discussion

H1a EXGAME would improve the effectiveness of decision making at the strategic level.

H1b ADGAME would improve the effectiveness of decision making at the strategic level.

The first part of this hypothesis is not supported by the experiments. EXGAME could not effectively replace decision makers at the strategic level. In this research, the authors initially attempted to design EXGAME to replace the player completely, but found that it was too difficult for EXGAME to make all the strategic decisions. Firstly, there are many factors that would have to be covered when designing the rules for strategic decisions, especially the behaviour of competitors. Secondly, even in the simplified environment of a business game, there is no ‘correct’ or ‘best’ strategy; it is context dependent. So, both EXGAME and ADGAME helped the user to select strategic policies for the game company instead of letting the system select them automatically. (For EXGAME, the knowledge engineer set the policy at the start of each experiment.)

The second part of the hypothesis is supported, in that teams using ADGAME generally followed more effective strategies (detailed performance analysis is given in the following section). However, it should be noted that ADGAME did not have a wide enough choice of strategic policies for some of the potential users ‘. . . ADGAME was not able to advise in view of what our aim and strategy was’ (Experiment B, team d4). We conclude that an ES here can only act as a support tool rather than as a replacement for strategic planning personnel.

The work of Yoon and Guimaraes (1997), which appeared after the experiments reported here had been carried out, confirms the ‘severe limitations’ of conventional ESs in supporting strategic level decisions, and proposes a hybrid of ES and case-based reasoning approaches as being potentially more effective.

Table 3 Summary of profit making in three experiments

<table><tr><td rowspan="2">Experiment</td><td rowspan="2">Group</td><td colspan="2">Best Team</td><td colspan="2">Next Best</td></tr><tr><td>Team</td><td>Profit</td><td>Team</td><td>Profit</td></tr><tr><td colspan="6">Experiment A</td></tr><tr><td rowspan="4">About 180 students were divided into four groups. Three EXGAMEs were used in three groups and the ES developer played in another group</td><td>a</td><td>EXGAME</td><td>212329</td><td>a3</td><td>-28557</td></tr><tr><td>b</td><td>EXGAME</td><td>64537</td><td>b1</td><td>-12104</td></tr><tr><td>c</td><td>EXGAME</td><td>276719</td><td>c3</td><td>-235651</td></tr><tr><td> $d^a$ </td><td>d4</td><td>-474</td><td> $d2^b$ </td><td>-215376</td></tr><tr><td colspan="6">Experiment B</td></tr><tr><td rowspan="2">About 170 students were divided into five groups. Five EXGAMEs were used.</td><td>a</td><td>EXGAME</td><td>603668</td><td>a6</td><td>416326</td></tr><tr><td>b</td><td>EXGAME</td><td>653042</td><td>b3</td><td>287972</td></tr><tr><td rowspan="3">ADGAME was used by six teams from five groups from the middle period of the game playing</td><td>c</td><td>EXGAME</td><td>624478</td><td>c3</td><td>455337</td></tr><tr><td>d</td><td>EXGAME</td><td>729538</td><td>d3</td><td>313100</td></tr><tr><td>e</td><td>EXGAME</td><td>568539</td><td>e6</td><td>-87765</td></tr><tr><td colspan="6">Experiment C</td></tr><tr><td rowspan="2">Ten individual players divided into two groups participated. Two EXGAMEs were used and four people consulted with ADGAME</td><td>f</td><td> $f1^c$ </td><td>659078</td><td>EXGAME</td><td>585329</td></tr><tr><td>g</td><td>EXGAME</td><td>571207</td><td> $g2^d$ </td><td>300967</td></tr></table>

<sup>a</sup>No EXGAME used in this group.  
<sup>b</sup>Company managed by one of the authors.  
<sup>c</sup>Company managed by an experienced person with the help of the expert advisory system ADGAME.  
<sup>d</sup>Company managed by a novice with the help of the expert advisory system ADGAME.

H2a EXGAME would improve the effectiveness of decision making at the tactical and operational levels.

H2b ADGAME would improve the effectiveness of decision making at the tactical and operational levels.

Both parts of this hypothesis are supported by the results of the experiments. In terms of profit-making, the companies managed by EXGAME all made larger profits than the companies managed by human players, except for one experienced player in Experiment C group f, who was using ADGAME. A summary of the results may be seen in Table 3. To test for significant differences, a non-parametric test needs to be used, as the distribution of profits is not normal. Using the Kruskal– Wallis one-way analysis of variance by ranks (Cohen & Holliday, 1982), the difference between EXGAME companies’ profits and those of all other players is significant at the P = 0.0001 level. In experiment A, EXGAME performance varied among groups, as did that of the student teams, but EXGAME still outperformed the student teams significantly (see differences with ‘next best’ team in Table 3). Some improvements were made to EXGAME after experiment A, which accounts for EXGAME’s performance being more stable in experiment B. Student performance in experiment B also did not differ significantly except one team e6. ADGAME enabled novices to perform much better than most unaided players. The Kruskal–Wallis test here gives a significant result at the P = 0.1 level. ADGAME also appeared to improve the performance of experienced players to the ‘expert’ level, although the numbers here are too small for statistical tests to be carried out (more detailed discussion on this is in Duan et al, 1995).

The other two dimensions of performance measurement are more subjective, so the detail is not shown here, but the results were very similar. EXGAME companies secured a significant competitive advantage early on and maintained it throughout, with the exception again of Experiment C group f, where one ADGAME-assisted player temporarily gained the upper hand, although his company finished the game in a worse state than that of EXGAME. EXGAME, and ADGAME-assisted players, also made much more consistent decisions than the unassisted human players. Neither EXGAME nor ADGAME has any concept of a final period, thus avoiding ‘end of the world’ strategies.

H3a EXGAME would improve the efficiency of decision making.

H3b ADGAME would improve the efficiency of decision making.

The first part of this hypothesis is supported by the experimental results, but the second is not. EXGAME could make decisions much faster than human decision makers, but ADGAME did not save users’ time.

Efficiency in this research is considered solely in terms of time savings, as this was the most relevant criterion in the experiments. Other dimensions of efficiency, such as cost or the amount of computer storage required, may be relevant to other ES applications.

It is generally agreed that an ES may save the expert’s time, especially in a replacement role. In this research, EXGAME was able to make the decisions for one period of the game much faster than human players, even an individual human player with only one set of opinions to consider.

However, this increased efficiency did not apply to ADGAME. In fact, players and teams using ADGAME spent more time in decision making than those not using it; more than twice as long, on average, supporting the point made by Townsend and Feucht (1986). This was not what the users themselves had expected; many ADGAME users (46% in Experiment B) had expected that it would save them time. This result that an advisory ES does not save a user’s time is consistent with the belief that decision support systems in general aim to improve effectiveness rather than efficiency. However, it may depend more on the extent to which the ES is integrated with other systems than the fact that an ES is being used. Neither ADGAME nor the ES reported by Doukidis et al (1994) were tightly integrated, and neither saved time, but the more integrated system reported by Agarwal et al (1994) did save the users’ time.

H4 Both EXGAME and ADGAME would perform well with the same knowledge base, i.e. there would be no need for different knowledge bases for ESs in different roles.

This was not supported by the experiments. ADGAME was developed from EXGAME, and so at first the knowledge bases of both systems were similar. However, when used by students in Experiment B from the middle of the game (the seventh period), the knowledge base ADGAME had inherited from EXGAME proved to be insufficient, because some companies were in a very bad state and the players needed specific advice for guiding them out of such a position. EXGAME had been designed to take over the game company at the beginning of the game, and so was only required to be able to manage the company smoothly. On the other hand, the situations ADGAME confronted were quite different. The users normally looked for help from ADGAME when they thought they were in trouble. ADGAME thus needed more knowledge about what it should do when the game company was in an extremely bad position, in this case because of the poor decisions students had already made. Its final knowledge base therefore contains more knowledge for ‘emergency’ help than EXGAME’s does.

We believe it may also be true in other domains that the tasks an expert advisory system needs to handle are more difficult and complex than those facing an ES in a replacement role in the same domain, especially where the replacement ES acts as an automaton, or the users of the advisory system have a very low level of knowledge of the domain.

H5 ADGAME users would believe that they had learned from using it.

This hypothesis is not supported by the experimental results. In both Experiments B and C, ADGAME users rated ‘improve users’ management skill’ bottom of a list of potential benefits, although their performance and comments implied that some learning may have taken place, at least for some. The effectiveness of ESs as a learning aid has been demonstrated elsewhere (Oz et al, 1993), but this was not perceived by ADGAME users in these experiments. The issue of whether the users really had learned from using ADGAME would have required extensive pre- and post-use testing, which might also have biased their choice of whether to use ADGAME or not.

## Further discussion

## Discretionary use of an advisory expert system

For an ES in a support role, the fact that effectiveness can only be achieved through the users complicates the position. Some people may be reluctant to rely upon an advisory system if its use is optional; one survey response, for example, was: ‘It is affective (sic), but it stops you from making your own decisions, which results in you not knowing how well you could do’ (Experiment B, team e4). Even those who do use it may become bored with it ‘. . . once the company was running smoothly, it was very much the same old thing (Experiment C, team g2).

It is important to note a point in this context about who chose to use ADGAME in Experiment B, when it was made available as an option in the middle of the game. Common sense might indicate that the weakest users would be most likely to seek the help of the ES. However, none of the teams who were worst placed in their group when ADGAME became available chose to use it. The teams who did use ADGAME were in fact performing somewhat better than average before ADGAME became available, although the difference in profit between those who became ADGAME users and those who did not was not significant at that point at the P = 0.05 level. Less surprisingly, those who did use ADGAME felt that it was most useful early on and in difficult situations. A further consequence of these observations is that even if the use of an advisory ES were compulsory, then the typical practice of asking for volunteer users to be involved in system development might well fail to bring in those most in need of the support provided by the ES.

## Consistency and learning

One reason why EXGAME performed well was its ability to make consistent decisions. However, the very fact that an ES is more predictable and consistent may also provide the answer to why an experienced player aided by ADGAME performed better than EXGAME in some aspects in Experiment C. The player concerned, when asked in the survey to rate the various benefits that a user can gain from ADGAME, gave the highest score to ‘improve users’ management skill’. This suggests that he had learned from ADGAME, and was gaining an advantage because he could use his knowledge more flexibly than EXGAME. People can learn and change quickly, but ESs cannot. This is a classic limitation of current ESs. Other types of knowledge-based system, such as case-based reasoning systems or neural networks, may avoid this difficulty more successfully, but discussion of this is beyond our scope here.

## The role and level of ES

The results of using EXGAME and ADGAME show that an ES can do a good job at the operational and tactical levels, and to some extent can replace the decision makers and work as a subordinate to human senior managers at strategic level. The experience appears to support the viewpoint of O’Leary and Turban (1987) and Lin (1986) and is consistent with the survey results discussed earlier, that a substantial majority of ES applications will be for operational level decisions. It may indeed be that this is the case even where the user is a senior manager with strategic level responsibilities.

EXGAME was used in a support role at the strategic level and in a replacement role at the tactical and operational level. The implementations of EXGAME and ADGAME suggest that ESs can be applied at any organizational level, but will be more effective and easier to develop at the operational level than the strategic level. A proposed framework for ESs in an organization is shown in Figure 2.

## Conclusions

Despite the widespread use and increasing importance of ES technology, little research has been done to test and evaluate ESs for business decision making at different levels and in different roles. This research offers some experimental evidence on these issues. Two ESs performing different roles in the same domain were tested against five research hypotheses. The experimental results reveal that:

ESs in a replacement role are effective at the operational and tactical decision levels, but have limitations at the strategic level. Expert systems in a support role can help users make better decisions at all three decision making levels, but their effectiveness can only be fulfilled through their users.

![](/api/attachments/CQSDBUG4/fulltext/images/954a33987fdc677366d6794d5149e449da0641cdfc1b54e30f07d2d5c7fe256d.jpg)  
Figure 2 The use of expert systems in organizations.

An ES acting in a support role (an expert advisory system) does not necessarily save a user’s time, but an ES in a replacement role does improve the efficiency of decision making in this way.

When used in the same domain but performing different roles, the knowledge base of an ES as an advisor needs to be different from that of an ES as a human replacement. The knowledge base of an advisory system must cover the wider range of problems users may confront and provide effective help in more difficult situations; thus more effort may be required in building an expert advisory system than an ES for a replacement role.

The users of an advisory ES did not believe that they had learned from using the system.

Moving to the real world, when implementing ESs in organizations, it is anticipated that organizations will benefit from improved decision making effectiveness by using ESs either to replace experts in operational and tactical decision making, or to support/advise their staff in decisions at all three organizational levels. It appears to be impossible to replace managers for strategic planning decisions, and difficult to develop a satisfactory advisory system to help with such decisions, due to the high uncertainty and complexity involved at this level.

Turning from effectiveness to efficiency, organizations cannot expect that an ES in a support role will necessarily improve the efficiency of a decision maker. How this latter point matches the expectations of the users and their managers is an issue that requires further research. An additional problem is that the users who volunteer to help in ES development and testing may not be the ones who most need support in the worst situations. This may be one reason for the perceived problem of unrealistic expectations; if the users who most need support are not involved in development, then it should be no surprise if the ES is less effective than anticipated. Finally, one thing is certain, the time is not yet ripe for the prediction by Harmon and King (1985)

that ‘problem solving and decision making will be automated just as surely as production lines are . . . and ESs will be the ‘robots’ of middle management’.

## References

Agarwal R, Brown S and Tanniru M (1994) Assessing the impact of an expert system: the experiences of a small firm. Expert Systems with Applications 7(2), 249–257.

Ansari A and Modarress B (1990) Commercial use of expert systems in the U.S. Journal of Systems Management 41(12), 10–13.

Anthony RN (1965) Planning and Control Systems: A Framework for Analysis. Harvard University Press, Boston.

Barrett ML and Beerel AC (1988) Expert Systems in Business: Practical Approach. Ellis Horwood, Chichester.

Basden A (1984) On the application of expert systems. In Developments in Expert Systems (Coombs MJ, Ed), pp 59–75, Academic Press, London.

Beerel AC (1987) Expert Systems: Strategic Implications and Applications. Ellis Horwood, Chichester.

Bramer M (Ed) (1990) Practical Experience in Building Expert Systems. Wiley, Chichester.

Broom HN (1969) Business Policy and Strategic Action: Text, Cases, and Management Game. Prentice Hall, Englewood Cliffs, New Jersey.

Cheng TCE and Bizruchak D (1991) Expert systems and production/operations management. International Journal of Production Economics 22(3), 249–257.

Coakes E and Merchant K (1996) Expert systems: a survey of their use in UK business. Information & Management 30(5), 223–230.

Cohen L and Holliday M (1982) Statistics for Social Scientists. Harper and Row, London.

Connell NAD and Powell PL (1990) A comparison of potential applications of expert systems and decision support systems. Journal of the Operational Research Society 41(5), 431–440.

Coursey DH and Shangraw RF Jr. (1989) Expert system technology for managerial applications: a typology. Public Productivity Review 7(5), 237–262.

Doukidis GI (1988) Decision support system concepts in expert systems: an empirical study. Decision Support Systems 4(3), 345–354.

Doukidis GI, Cornford T and Forster D (1994) Medical expert systems for developing countries: evaluation in practice. Expert Systems with Applications 7(2), 221–233.

Duan Y, Edwards JS and Robins PC (1995) An analysis of users reactions towards using an expert advisory system. Expert Systems with Applications 9(4), 271–282.

Duan Y, Edwards JS and Robins PC (1998) Experiences with EXGAME: an expert system for playing a competitive business game. International Journal of Intelligent Systems in Accounting, Finance and Management 7(1), 1–19.

Durkin JD (1993) Expert Systems Catalogue of Applications. Intelligent Computer Systems, Akron, Ohio.

Durkin JD (1996) Expert systems: a view of the field. IEEE Expert 11(2), 56–63.

Edwards JS (1991) Building Knowledge-Based Systems: Towards a Methodology. Pitman, London.

Eom SB (1996) A survey of operational expert systems in business (1980–1993). Interfaces 26(5), 50–70.

Er MC (1988) Decision support systems: a summary, problems and future trends. Decision Support Systems 4(4), 355–363.

Ernst ML and Ojha H (1986) Business applications of artificial intelligence knowledge based expert systems. Future Generations Computer Systems 2(3), 173–185.

Gibson ML and Vedder RG (1989) Tools and techniques for use in decision support systems. Decision Support System 6(2), 42–50.

Gill TG (1995) Early expert systems: where are they now? MIS Quarterly 19(1), 51–81.

Gill TG (1996) Expert systems usage: task change and intrinsic motivation. MIS Quarterly 20(3), 301–323.

Gorry GA and Scott Morton MS (1971) A framework for management information systems. Sloan Management Review 13(1), 55–70.

Grogono P et al (1991) Expert system evaluation techniques: a selected bibliography. Expert Systems 8(4), 227–239.

Guan J and Graham JH (1996) An integrated approach for fault diagnosis with learning. Computers in Industry 32(1), 33–51.

Hadden SG (1986) Intelligent advisory systems for managing and disseminating information. Public Administration Review 46 (November, special issue), 572–578.

Harmon P and King D (1985) Expert Systems. Wiley, Chichester.

Hart A (1989) Knowledge Acquisition for Expert Systems. Kogan Page. London.

Hui Y, Qin Y and Morita S (1996) An artificial intelligence systems of trouble diagnosis for aircraft engines. Computers & Industrial Engineering 31(3–4), 797–801.

Joshi S, Vissa NN and Chang TC (1988) Expert process planning system with solid model interface. International Journal of Production Research 26(5), 863–885.

Kunnathur AS, Ahmed MU and Charles RJS (1996) Expert systems adoption: an analytical study of managerial issues and concerns. Information & Management 30(1), 15–25.

Lin E (1986) Expert systems for business applications: potentials and limitations. Journal of Systems Management 37(7), 18–21.

Madni AM (1988) The role of human factors in expert systems design and acceptance. Human Factors 30(4), 395–414.

Moody J, Blanton J and Will R (1998) Capturing expertise from experts: the need to match knowledge elicitation techniques with expert system types. Journal of Computer Information Systems 39(2), 89–95.

Morris T and Westbrook R (1996) Technical innovation and competitive advantage in retail financial services: a case study of change and industry response. British Journal of Management 7(1), 45–61.

O’Keefe RM and Preece AD (1996) The development, validation and implementation of knowledge-based system. European Journal of Operational Research 92(3), 458–473.

O’Keefe RM and Rebne D (1993) Understanding the applicability of expert systems. International Journal of Applied Expert Systems 1(1), 3–24.

O’Leary D and Turban E (1987) The organisational impact of expert systems. Human Systems Management 7(1), 11–19.

Ow PS and Smith SF (1987) Two design principles for knowledgebased systems. Decision Science 18(3), 430–447.

Oz E, Fedorowicz J and Stapleton T (1993) Improving quality, speed and confidence in decision making: Measuring expert system benefits. Information & Management 24(2), 71–82.

Preece AD (1990) Towards a methodology for evaluating expert systems. Expert Systems 7(4), 215–223.

Rees PL (1992) User evaluation of expert systems. Industrial Management and Data Systems 92(6), 17–23.

Schumann M et al (1989) business strategy advisor: an expert systems implementation. AI and Expert Systems 16(2), 16–24.

Shao YP (1998) Perceived impact and diffusion of expert systems in banking: an exploratory investigation. International Journal of Information Management 18(2), 139–156.

Silver MS (1991) Systems that Support Decision Makers: Description and Analysis. Wiley, Chichester.

Simon HA (1977) The New Science of Management Decision. Prentice Hall, Englewood Cliffs, New Jersey.

Suh CK and Suh EH (1993) Using human factor guidelines for developing expert systems. Expert Systems 10(3), 151–156.

The Systems International/es (Connect) (1989) Expert systems trends revealed. Systems International 17(7), 12–14.

Townsend C and Feucht D (1986) Designing and Programming Per-

sonal Expert Systems. TAB Books, Blue Ridge Summit, Pennsylvania.

Tsai N, Necco CR and Wei G (1994) An assessment of current expert systems: are your expectations realistic? Journal of Systems Man agement 45(11), 28–32.

Turban E and Watkins PR (1987) The impact of emerging management support systems. Human Systems Management 7(1), 7–10.

Turban E and Aronson JE (1998) Decision Support Systems and Intelligent Systems (5th edition). Prentice Hall, Upper Saddle River, New Jersey.

Underwood D (1992) Expert systems at mutual life: a three-pronged approach. Journal of Systems Management 43(1), 13–16.

Vijayaraman BS and Osyk BA (1994) An empirical study on the usage of intelligent technologies. Journal of Computer Information Systems 35(1), 35–40.

## About the authors

John S Edwards (PhD) is Senior Lecturer in Operational Research and Systems at Aston Business School. His principal research interests are knowledge-based systems and decision support systems, especially methods for their development and their significance in knowledge management. He has written more than 30 research papers on these topics, and two books, Building Knowledge-based Systems and Decision Making with Computers.

Yanqing Duan (PhD) is a Senior Research Fellow at Luton Business School, University of Luton. She obtained her PhD

Wong BK and Monaco JA (1995) Expert system applications in business: a review and analysis of the literature (1977–1993). Information & Management 29(3), 141–152.

Wong BK (1996) The role of top management in the development of expert systems. Journal of Systems Management 47(4), 36–40.

Yoon Y, Guimaraes T and O’Neal Q (1995) Exploring the factors associated with expert systems success. MIS Quarterly 19(1), 83– 106.

Yoon Y and Guimaraes T (1997) Assessing ES development approaches to support executive decisions. Technology Management: Strategies and Applications 3(3), 173–188.

Yoon Y, Guimaraes T and Clevenson A (1998) Exploring expert system success factors for business process reengineering. Journal of Engineering Technology Management 15(2–3), 179–199.

from Aston University. Her research interests include the use of decision support systems and expert systems for business decision making and marketing planning. She is also interested in E-commerce and its implementation in SMEs.

Paul Robins (PhD) is a Lecturer in Operational Research at Aston Businesss School. He has a background in environmental sciences and the study of methods of providing technical information to support organizational decision making. He teaches information system development and problem solving methods to business students.
