---
otero_id: 23058
otero_key: "5A9VJKWQ"
title: "Behavioural effects of attitudes toward constraint in CASE: the impact of development task and project phase"
authors: "Donald L. Day"
year: "2000"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.2000.00073.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Behavioural effects of attitudes toward constraint in CASE: the impact of development task and project phase

Donald L. Day

Computer and Information Sciences Department, Towson University, Baltimore, MD, USA, email: d.day@acm.org

Abstract.This paper examines the effects of systems development task and phase upon individuals’ attitudes and behaviour while using computer-aided systems engineering (CASE) tools. A previous empirical study of developers in several countries is revisited. Findings indicate that the mediating effects of task and phase upon the relationship among constraints, attitudes and behaviour are weak. They thereby support earlier research, which claims significance between attitudes and behaviour, by eliminating the potentially mediating effects of task and phase. Findings also indicate that CASE tool users associate implementation, integration and maintenance in terms of tasks and constraints, suggesting a reassessment of traditional life cycle models.

Keywords: CASE, constraint, life cycle, task, user behaviour

## INTRODUCTION

This paper examines the potentially mediating effects of development task and project phase upon software developers’ reactions to constraint in computer-aided systems engineering (CASE) tools. Following a problem statement and definition of terms, supporting research is reviewed. Study methods are described, including scaling techniques, by which response items on a questionnaire were grouped into constructs for examination. Finally, results of an analysis of variance are addressed, and findings are discussed.

## Problem statement

Systems design is a complex process that includes the negotiation of constraints that must be satisfied if software is to satisfy appropriate and necessary standards.

This paper refines our understanding of developers’ constraint negotiation behaviour, by qualifying the findings of an earlier study (Day, 1996). It evaluates the influence of development task and phase upon the relationship between developers’ attitudes towards constraint and their reported behaviour.

The earlier study by Day (1994) found that developers’ attitudes towards constraint and their perceptions of constraint in CASE tools significantly affect their satisfaction with and use of such tools. In a critique of that study, Venkatesh (1995) suggested that variations in activity context (task or phase) could mediate observed effects significantly. This paper examines whether such mediation is indeed a factor.

Constraints are intrinsic to design problem-solving, regardless of whether automated tools are used. In software engineering, constraints vary from interelement consistency checks (Vessey et al., 1992) to complex, inter-related and interacting rules of style and procedure (Scott et al., 1998). Examples include everything from the number of entities considered desirable in an ERD to controls over whether bottom-up design is to be permitted. Constraints materially affect how systems are designed and implemented, especially when CASE tools are used.

Day’s earlier study did not evaluate the potential mediating effects of task and phase. In the current context, ‘task’ refers to one of a series of distinct activities undertaken according to local best practice, as part of a software development phase. A ‘phase’ is a large group of such tasks associated (for example) with a stage in the classic waterfall model (requirements analysis, logical design, etc.).

The current study refines Day’s earlier research by posing the following research question: to what extent does development task and phase mediate the impact of tool users’ attitudes towards constraints upon their behaviour with CASE tools?

This question is relevant because it lies at the heart of whether Day’s findings are generalizable for all CASE-based software development or, instead, are applicable only during certain phases or even only when a limited set of tasks is being performed. Task and phase were not controlled in Day’s original analysis. Therefore, it is possible that the driving influence of attitude and perception upon satisfaction and behaviour might disappear if a more controlled, structured analysis were performed. In other words, it is possible that the impact of user attitudes and perceptions may be different in the context of one task or phase vs. another.

Resolution of this question may lower one barrier to the application of Day’s findings to improve CASE user productivity and software quality (Day et al., 1997). If Day’s findings can be validated, CASE tool builders might be advised to find some means of accommodating users’ attitudes towards constraints as they (the builders) create the next generation of automated software design tools. On the other hand, if the result of this study is that task and phase mediate the impact of constraints, tool builders may want to apply Day’s findings in only limited circumstances.

Definitions key to the interpretation of this work are presented in Table 1.

## Supporting research

There has been little previous work directly related to constraint negotiation behaviour and related user attitudes, perceptions, satisfaction and behaviour. Darses (1990, 1991) and Laurel (1991) examined the ways in which constraints frame creative design tasks. Silver (1988) identified design objectives that favour either greater or lesser restrictiveness (constraint) in decision support tools. Akin (1994) suggested that the freedom to restructure problems by altering constraints is intrinsic to design (although not to engineering).

Table 1. Key definitions

<table><tr><td>Constraint</td><td>A rule that defines the range of options available in performance of a task</td></tr><tr><td>Negotiation</td><td>The process of deciding upon and taking action in response to a constraint that appears to affect some goal or objective</td></tr><tr><td>Task</td><td>A set of actions undertaken to accomplish a specific effect in support of a goal or objective</td></tr><tr><td>Phase</td><td>The sequential, time-based interval in a product development cycle characterized by the non-exclusive performance of multiple tasks</td></tr><tr><td>Attitude</td><td>The amount of effect for or against some object, measured on a bipolar evaluative scale</td></tr><tr><td>Behaviour</td><td>Overt acts that are studied in their own right, not as indicators of belief, attitude or satisfaction</td></tr><tr><td>Developer</td><td>The professional user of a CASE tool, tasked with the design of a software application</td></tr><tr><td>Builder</td><td>The professional programmer tasked with the design and implementation of a CASE tool for use by developers in the creation of application software</td></tr></table>

The definitions for attitude and behaviour are taken from Fishbein & Ajzen (1975).

Sheridan (1980) suggested a scale to assess system restrictiveness (constraint). Silver (1991) observed that systems may appear to be relatively unconstrained to some, yet very constrained to others. He pointed out that it is users’ perceptions of restrictiveness, not objective restrictiveness independent of the user, that determines how users react to a tool.

Vessey et al. (1992) evaluated consistency constraints in 12 CASE tools. They concluded that CASE constraints are implemented arbitrarily, resulting in tools that may be either restrictive, guided or flexible. Jankowski (1997) examined the effects of techniques for notifying users of constraint violations. In a series of studies, Orlikowski described three major effects of CASE: social impact (1989), process control (1991a) and technological innovation (1991b). (In the current work, process control is of primary interest.)

The impact of constraint implementation in CASE tools was also examined by Day (1996). The constraint negotiation strategies described in that work form part of the constructs addressed in this paper. These constructs were refined and extended by Parchkova & Day (1998), from which the following list was taken.

The constraint negotiation strategies are as follows:

• in avoidance, the user modifies his task approach pre-emptively, realizing that to do otherwise would trigger a constraint condition;

• in compliance, the user modifies his task approach to suit the limitations imposed by a constraint;

• in deferral, the user declines to modify his task approach, with the knowledge that subsequent system or human review may reverse, modify or accept his decision to over-ride the constraint;

• in subversion, the user modifies his task approach to take advantage of known weaknesses in the tool, over-riding the spirit, but not the mechanism, by which the constraint is implemented (also known as ‘work-around’);

• in negation, the user declines to modify his task approach, unconditionally over-riding the constraint (if possible);

• in path-seeking, the user modifies his task approach to find the least constraining path.

The constraint negotiation strategies may be illustrated by the following case, which describes a developer using data flow diagrams (DFDs) to model a system. We can presume that normally the tool insists that all processes must be labelled and that the appropriate data flows must be indicated, before the developer is allowed to progress with the design.

• In avoidance, the developer who might otherwise want to label the diagram only partially (in order to get on with some other element in the design) will decide not to do so, knowing in advance that the tool will constrain him, disallowing that path. In other words, the developer will behave pre-emptively.

In compliance, the developer may attempt to move to another element without labelling all processes. The tool will notify him of the violation, after which the developer will obey, by completing the required detail.

• In deferral, the developer may decide not to label all processes, perhaps intending to return later to decide upon that detail. The tool will allow this, but the developer will make his decisions knowing that either a human or the tool itself may review the decisions later, possibly disallowing them, thereby forcing the developer to redo substantial amounts of work.

In subversion, the developer may perform a work-around in which the tool’s constraints appear to be satisfied, but are in fact thwarted. This violation of the spirit but not the letter of a constraint might be achieved, for example by providing nonsense labels that the developer might plan to replace at a later stage. But his immediate intent would be only to satisfy the constraint and to get on with the design.

In negation, the developer may refuse to provide labelling details, instead moving on with other tasks in design. In this instance, the tool might only issue a warning notice, but otherwise allow the violation. Further, in this case, the user would not expect a later review that might reverse his decision.

• In path-seeking, a developer may select from a list of default labels offered by the tool, even though he realizes that the labels are not optimal. He would have no intention of returning later to substitute more meaningful labels. He would not be trying to subvert the constraint, but rather to find an alternative means to accomplish the same goal.

These strategies are related to the current study in that it was felt that user behaviour may vary depending upon the task or phase under way when a constraint is encountered. For example, if instead of labelling DFDs, the user were using the tool to validate a requirements matrix (another task), he might have different reactions to roughly equivalent levels of constraint. Henceforth in this paper, this is referred to as the effects of task and phase. Before evaluating these effects, in the next section, we review the methods applied in Day’s original study (in addition to those used here).

## METHOD

## Subjects

Responses discussed here are from 129 professional CASE tool builders and users in North America (68.1%), Europe (21.0%) and New Zealand (5.8%). Most subjects (65.6%) worked in industry, although a substantial minority (27.5%) were employed academics (not students).

Subjects for 12 structured interviews that preceded questionnaire data collection were nominated by managers in three companies. Questionnaire respondents were self-nominated, in response to solicitations in electronic discussion groups and bulletin boards. About half of these respondents were sent hard-copy versions of the questionnaire; the other half responded online by editing ASCII email files for return. Subsequent analysis showed no significant difference in responses resulting from medium (hard copy vs. email). No attempt was made to qualify subjects in terms of either the tool they used or the types of organizations they represented, or to compare academics with subjects from industry. The sample clearly suffered from self-selection bias, in that no attempt was made to examine the universe of CASE tool users systematically (e.g. by clustering on tool user attributes). However, the sample was genuinely random.

## Materials and design

Data were collected using an eight-page survey questionnaire. The instrument included 61 questions related to workplace context, characteristics of CASE use, behaviour in response to constraint, attitudes towards constraint and individual differences (demographics).

The self-administered, self-report questionnaire was constructed from concerns expressed by interviewees, apparently relevant topics from the literature and effects predicted by the research model. It was refined before use by correcting problems noted in a pretest. In that pretest, the instrument was distributed via email to 32 tool users who had volunteered in response to bulletin board calls for participation. The fact that respondents were asked to vol unteer in advance of instrument distribution (thereby creating a commitment to participate) was considered an important part of the methodology (and of data validity). It was felt that such individuals would be less likely to submit frivolous or partial responses. (The response rate was nearly total, after follow-up contact of slow respondents.) Responses to the pretest were used not only to refine the instrument, but also to trial analysis-scale development methods to be applied in the main study (DeVellis, 1991).

Also, because of respondents’ pretest remarks about question wording and meaning, the final instrument included several definitions of key concepts. These were added to increase reliability (by ensuring that items measured the same phenomena across subjects and between subjects and researchers). The questionnaire also included several proven items closely adapted from other studies (e.g. Chin et al., 1988). Finally, an analysis of missing pretest data (non-responses) was conducted. As a result, several apparently confusing or objectionable questions were deleted from the final questionnaire.

![](/api/attachments/5A9VJKWQ/fulltext/images/efd247c46a381c5f9b06d34968464ede38bf4cb0e5e9eeb42adebe653151b840.jpg)  
Figure 1. Research model.

The research model for the current paper is presented in Figure 1. It is an abstraction of the design from Day (1995), which addressed in part the effects of ‘A’ upon ‘B’. This paper examines the mediating effects of ‘T’ and ‘P’ upon the ‘A’ to ‘B’ relationship.

## Procedure

In order to answer the research question (see Problem statement in the Introduction), it was necessary first to perform several grouping and refinement operations to ensure that constructs were coherent. These included creating activity sets of development tasks, ensuring orthogonality of development phases and engineering scales to represent attitudes and behaviour. After ensuring construct coherence, the construct validity of activity sets and development phases was evaluated via correlational reliability analysis (DeVellis, 1991). For the purposes of this study, the appropriate grouping of tasks and phases was not necessarily that commonly thought to be true either by non-study academics or by practitioners. It was based solely upon the associations and perceptions of subjects in Day’s sample. (Discrepancies between subjects’ perceptions of relevant task or phase characteristics and those recognized by the industry might have important implications for future engineering of the design process.)

## Activity sets

In order to assess the impact of tasks upon attitude and behaviour, tasks were first organized into groups (‘activity sets’) defined by intertask associations. (An ‘association’ occurred if a respondent indicated that two specific tasks, taken as indicator variables, were performed using CASE at his or her workplace.) The premise was that the various constellations of tasks for which CASE is used (in the work context) may affect user attitude and behaviour.

Table 2. Activity sets and development phases

<table><tr><td>Activity sets</td></tr><tr><td>Planning, analysis and design: analysis and design, documentation, requirements prototyping, business area analysis, enterprise modelling, information systems planning, re-engineering, reverse engineering, task estimation</td></tr><tr><td>Implementation: code generation, interface development, maintenance, test and evaluation, debugging, configuration management</td></tr><tr><td>Development phases</td></tr><tr><td>Design, requirements definition, specification, implementation*, maintenance*, feasibility analysis, integration*, project planning</td></tr></table>

\* Indicates phases merged into integration to improve coherence as a result of the analysis (see text).

In order to improve the validity of findings, groups of tasks representing constructs must be coherent and must overlap one another as little as possible (i.e. be orthogonal). Overlap among constructs may confound observed effects. Starting from groups based on the information engineering model, activity sets were constructed. After all tasks were crosscorrelated, sets were formed from those tasks that had statistically significant correlations with one another.

This grouping of tasks by activity sets is featured in Table 2. The two sets thus defined attain marginal to acceptable coherence, with Cronbach alphas of 0.65 and 0.71 (see the discussion of scales below). In this context, Cronbach alpha is a measure of the degree to which response items correlate with one another and, therefore, possibly measure a common underlying construct. Items that correlate only weakly with a group that otherwise has relatively high internal cohesion are not included in the composite variable finally created in scale development. In addition to creating single constructs amenable to statistical analysis, this process improves validity by increasing orthogonality among the composite variables used for analysis (DeVellis, 1991). It is coincidental that the activity sets determined by such analysis corresponded roughly to groups of tasks that are normally identified as upper vs. lower CASE in software development.

## Orthogonality

In a procedure identical to that used for tasks, phases were cross-correlated. This analysis suggested the need to merge implementation and integration (r = 0.49, P < 0.00) in terms of the way developers group such phases (i.e. they perceived a similarity of tasks performed). As maintenance correlated relatively highly with implementation (r = 0.58, P = 0.00) and integration (r = 0.47, P < 0.00), it was merged as well.

The result was an implementation phase construct that combined implementation, integration and maintenance for the purposes of CASE use in the workplace (Table 2). This combination of constructs contradicts conventional wisdom about the organization of software design activity, which presumes that maintenance is materially different from phases in the software development life cycle identified with ‘original’ design and implementation. It also suggests the need to re-examine traditional development models if user behaviour is to be accommodated in future systems development. It may be, for example, that procedures, tools and quality criteria should be similar for all three of the merged phases.

## Scales

In order to clarify analysis and moderate response bias among items, reliability analysis was also used to develop coherent scales representing the constructs attitude and behaviour. In each case, five questions were grouped to create a composite scale.

Before the coherence and reliability of such scales can be judged, it was necessary to normalize responses. This was accomplished by inverting responses for those questions whose direction of meaning is opposite to that of other questions in the potential scale. This ensures, for example, that a high score on any item in the potential behaviour scale will indicate conformist behaviour, regardless of how the question was worded. Inverted values are used only for reliability analysis (not for descriptive statistics).

After normalization, cohesion was strengthened by removing items that correlated poorly with others. The result is a coherent scale, suitable for use as a construct. This procedure and its rationale are discussed in DeVellis (1991). The resulting attitude scale (normative attitudes towards constraint behaviour) had a Cronbach alpha of 0.68; the behaviour scale (reported constraint negotiation behaviour) scored 0.73. According to DeVellis (1991), these levels are considered respectable.

## Construct validity

In order to confirm the construct validity of activity sets and phase groupings, an association matrix was built (Table 3). This matrix was based upon statistically significant (although low) correlations among tasks and phases. Effective correlations averaged 0.25 for the planning, analysis and design activity set and 0.34 for implementation (the overall mean was 0.28).

All tasks assigned to the implementation activity set were associated with the life cycle implementation phase. This supported the construct validity of this activity set. Likewise, respondents who reported performing planning, analysis and design tasks with their CASE tools also reported that those tools were used primarily in early life cycle phases. The final statistical procedure was to correlate constructs and to conduct an analysis of variance to evaluate effects (i.e. validate the research model).

## R E S U LT S

## Validity of the research model

Validation of the research model (Figure 1) was attempted by correlating, first, activity sets, then development phases with attitude and behaviour. Analysis revealed no statistically significant associations among planning, analysis and design tasks and either attitude or behaviour (Table 4).

Table 3. Association matrix of tasks and phases

<table><tr><td>Tasks/phases</td><td>Design</td><td>Requirements definition</td><td>Specification</td><td>Implement</td><td>Feasibility</td><td>Planning</td></tr><tr><td>Analysis</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td></tr><tr><td>Documentation</td><td></td><td></td><td>x</td><td></td><td></td><td>x</td></tr><tr><td>Prototyping</td><td>x</td><td>x</td><td>x</td><td></td><td>x</td><td></td></tr><tr><td>Business area analysis</td><td></td><td>x</td><td></td><td></td><td>x</td><td></td></tr><tr><td>Enterprise modelling</td><td></td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>Information systems planning</td><td></td><td>x</td><td></td><td></td><td>x</td><td>x</td></tr><tr><td>Re-engineering</td><td></td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>Task estimation</td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Code generation</td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Interface development</td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Maintenance</td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Test and evaluation</td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Debugging</td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Configuration management</td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr></table>

There were no significant correlations between reverse engineering and any phase.

Table 4. Correlations, task activity set with attitude and behaviour

<table><tr><td colspan="2"></td><td>Attitude</td><td>Behaviour</td></tr><tr><td rowspan="2">Planning, analysis and design</td><td>Correlation</td><td>0.05</td><td>0.10</td></tr><tr><td>Significance</td><td>0.57</td><td>0.28</td></tr><tr><td rowspan="2">Implementation</td><td>Correlation</td><td>0.21</td><td>0.26</td></tr><tr><td>Significance</td><td>0.02*</td><td>0.00*</td></tr></table>

\* Indicates significance at P < 0.05.  
Attitude mean = 3.90, SD = 1.40, median = 4.  
Behaviour mean = 3.99, SD = 1.63, median = 4.  
Attitude ¥ behaviour r = 0.76, P < 0.00.

However, significant (but low) correlations were observed between the implementation activity set and both attitude and behaviour $( r = 0 . 2 1 , P = 0 . 0 2 ; r = 0 . 2 6 , P = 0 . 0 0 )$ . Those who executed implementation (lower CASE) tasks seemed to favour (and engage in) conformist behaviour more than did those who performed upper CASE planning, analysis and design tasks. This may imply that constraint flexibility is felt to be more crucial to system design than to system implementation.

In contrast to these task results, no significant effects were observed among phases and either attitude or behaviour (Table 5). [It might be noted that Day’s (1995) study found a significant influence of attitude upon behaviour.]

Table 5. Correlations, phase with attitude and behaviour

<table><tr><td></td><td></td><td>Attitude</td><td>Behaviour</td></tr><tr><td rowspan="2">Project planning</td><td>Correlation</td><td>-0.10</td><td>-0.06</td></tr><tr><td>Significance</td><td>0.28</td><td>0.53</td></tr><tr><td rowspan="2">Feasibility analysis</td><td>Correlation</td><td>-0.02</td><td>-0.12</td></tr><tr><td>Significance</td><td>0.87</td><td>0.19</td></tr><tr><td rowspan="2">Requirements definition</td><td>Correlation</td><td>-0.03</td><td>0.08</td></tr><tr><td>Significance</td><td>0.77</td><td>0.39</td></tr><tr><td rowspan="2">Specification</td><td>Correlation</td><td>-0.10</td><td>-0.04</td></tr><tr><td>Significance</td><td>0.25</td><td>0.67</td></tr><tr><td rowspan="2">Design</td><td>Correlation</td><td>0.01</td><td>-0.13</td></tr><tr><td>Significance</td><td>0.88</td><td>0.15</td></tr><tr><td rowspan="2">Implementation</td><td>Correlation</td><td>0.14</td><td>0.14</td></tr><tr><td>Significance</td><td>0.11</td><td>0.11</td></tr></table>

Table 6. Two-way ANOVA, developer attitudes and constraint negotiation behaviour

<table><tr><td rowspan="2">Source of variation</td><td rowspan="2">SS</td><td rowspan="2">d.f.</td><td rowspan="2">MS</td><td rowspan="2">F</td><td rowspan="2">Significance</td><td colspan="2">Least-square means</td></tr><tr><td>Level 1</td><td>Level 2</td></tr><tr><td colspan="8">Consequent variable: attitude</td></tr><tr><td>(T)ask implement</td><td>16.97</td><td>1</td><td>16.97</td><td>9.29</td><td>0.00*</td><td>3.69</td><td>4.12</td></tr><tr><td>(P)hase implement</td><td>3.44</td><td>1</td><td>3.44</td><td>1.88</td><td>0.17</td><td>3.62</td><td>4.19</td></tr><tr><td>T-P interaction</td><td>4.46</td><td>1</td><td>4.46</td><td>2.44</td><td>0.12</td><td></td><td></td></tr><tr><td colspan="8">Consequent variable: behaviour</td></tr><tr><td>(T)ask implement</td><td>36.46</td><td>1</td><td>36.46</td><td>15.19</td><td>0.00*</td><td>3.62</td><td>4.49</td></tr><tr><td>(P)hase implement</td><td>1.21</td><td>1</td><td>1.21</td><td>0.50</td><td>0.48</td><td>3.85</td><td>4.26</td></tr><tr><td>T-P interaction</td><td>4.70</td><td>1</td><td>4.70</td><td>1.96</td><td>0.16</td><td></td><td></td></tr></table>

\*Indicates significance at P < 0.05.

## Analysis of variance

The observed correlations among the implementation activity set and developer attitude and behaviour led to an analysis of variance. For this analysis, task and phase were divided at their means to create classification levels. (In the absence of theory suggesting skewed distributions, this division was deemed reasonable.)

Development task exhibited a significant main effect on both developer attitude and behaviour (Table 6), confirming results of the earlier correlational analysis. Development phase (as represented by implementation) had no significant effect on either of the consequent constructs. Also, there was no significant interaction effect between development task and development phase, for either attitude or behaviour.

## DISCUSSION

The main goal of this paper was to examine whether task or phase mediates how attitude towards constraint affects developers’ software development behaviour, when they use automated design tools.

## Findings

In terms of the research question, the use of CASE for planning, analysis and design tasks did not appear to influence attitude or behaviour significantly. The development phase in which CASE is used also appeared to have no discernible influence. (Both findings decrease the likelihood that these potential confounds colour Day’s original claims that attitudes towards constraint impact developer behaviour.) The use of CASE for implementation tasks did seem to have an influence, although the strength of association was low.

In summary, task and phase did not appear to play a mediating role between attitude and behaviour. The only factor demonstrating significant ANOVA association with developer attitude and constraint negotiation behaviour was the implementation task, and that association was weak. Respondents indicated that CASE tools were used relatively infrequently for such tasks, limiting their practical influence. In this population, CASE tools were used mostly for planning, analysis and design tasks, followed by documentation and code generation. They were applied most often in the design phase, with requirements definition and specification phases secondary. In general, tools were used less frequently in lower CASE activities.

Developers favoured non-conformist constraint negotiation behaviour (but not outright resistance to process constraints). The behaviour they reported engaging in themselves followed this norm. Also, those using CASE for implementation tasks favoured conformance more than those who were involved in planning, analysis and design.

## Contributions

In addition to reinforcing the findings of previous research, this paper raised an intriguing question that might be the focus of future research: what are the underlying characteristics of implementation, integration and maintenance that cause CASE tool users to associate them in the context of constraints, and how might both CASE tools and software development methods be better designed to capitalize on such common characteristics?

This paper also developed scales relevant to software task and phase activities that may be useful for further research into human–computer interaction with computerized design tools. The somewhat unconventional activity sets, reconstituted development phases, association of tasks to phases and scales for attitude and behaviour were validated to minimal levels of reli ability. With additional validation, these elements may also be useful in future research. In the study of developer behaviour, it may prove to be the association of task types rather than traditional phase sequence that is most important to refinement of the software development process.

By eliminating two factors (task and phase) that might have confounded main effects, the current study strengthened the validity of Day’s original study. Therefore, as a result of this analysis, confidence in the role of attitudes about constraint in explaining tool user behaviour is strengthened.

In terms of the practical impact upon systems development, the analysis reported here suggests that managers might pay particular attention to tool user attitudes about constraint during planning, analysis and design activities. The findings suggest, however, that the influence of attitudes is largely independent of task or phase, implying that constraint is a real issue in systems development with CASE tools, regardless of why and how such tools are applied.

In terms of CASE tool design, the results of this analysis add weight to earlier work suggesting that appropriate levels of constraint are important to tool users. Therefore, it is possible that CASE tools should be designed to achieve appropriate (and therefore variable) levels of constraint.

## Limitations

The key limitations of this paper include the small sample size, the use of potentially unreliable self-report and the predominance of subjects from North America. It could be said that the sample size is responsible for the failure of task and phase to demonstrate significant impact. However, Day (1996) found significance, using the same data.

Self-report bias is a difficult issue, which can be resolved only by the use of a different research design: one in which extensive testing of attitude patterns and in situ observations of actual developer behaviour are used. The North American bias would be most easily eliminated by extension of the study to qualified respondents from other regions.

## REFERENCES

Akin, O. (1994) Creativity in design. Performance Improvement Quarterly, 7, 9–21.

Chin, J., Diehl, V. & Norman, K. (1988) Development of an instrument measuring user satisfaction of the human–computer interface. In: Human Factors in Computing Systems. Soloway, E., Frye, D. & Sheppard, S. (eds), pp. 213–218. Proceedings of the 1988 SIGCHI Annual Meeting. ACM, New York.

Darses, F. (1990) Constraints in design: towards a methodology of psychological analysis based on AI formalisms. In: Human–Computer Interaction – INTERACT ’90. Diaper, D. et al. (eds), pp. 135–139. Elsevier, Amsterdam.

Darses, F. (1991) The constraint satisfaction approach to design: a psychological investigation. Acta Psychologica, 78, 307–325.

Day, D. (1994) Behavioral and perceptual responses to the constraints of computer-mediated design. In: Human–Machine Communication for Educational Systems Design. Brouwer-Janse, M. & Harrington, T. (eds), pp. 99–106. ASI Series F, Vol. 129. Springer-Verlag, Berlin.

Day, D. (1995) User Responses to Constraints in Computerized Design Tools. Unpublished Doctoral Dissertation, UMI 95-44905. Syracuse University, Syracuse, NY.

Day, D. (1996) User responses to constraints in computerized design tools: an extended abstract. Software Engineering Notes, 21, 47–50.

Day, D., Ahuja, M. & Scott, L. (1997) Constraints in design engineering: problem solving with CASE tools. In: Proceedings of the Eighth Australian Conference on Information Systems, 29 Sept.–2 Oct, pp. 509–516.

University of South Australia, Adelaide. Available online: http://business.city.unisa.edu.au/acis97/

DeVellis, R. (1991) Scale Development: Theory and Appli cations. Applied Social Research Methods Series, Vol. 26. Sage Publishers, Newbury Park, CA.

Fishbein, M. & Ajzen, I. (1975) Belief, Attitude, Intention and Behavior: an Introduction to Theory and Research. Addison-Wesley, Reading, MA.

Jankowski, D. (1997) Computer-aided systems engineering methodology support and its effect on the output of structured analysis. Empirical Software Engineering, 2, 11–38.

Laurel, B. (1991) Computers as Theatre. Addison-Wesley, Reading, MA.

Orlikowski, W. (1989) Division among the ranks: the social implications of CASE tools for system developers. In: Proceedings, Tenth International Conference on Information Systems, Boston, 4–6 December, pp. 199–210.

Orlikowski, W. (1991a) Integrated information environment or matrix of control? The contradictory implications of information technology. Account, Management and Information Technology, 1, 9–42.

Orlikowski, W. (1991b) Radical and Incremental Innovations in Systems Development: An Empirical Investigation of CASE Tools. Center for Information Systems Research Working Paper 221. Massachusetts Institute of Technology, Cambridge, MA.

Parchkova, M. & Day, D. (1998) Negotiating Constraints in Computerised Design Tools: A Taxonomy of User Behaviour. Revision under consideration by Behaviour & Information Technology.

Scott, L., Horvath, L. & Day, D. (2000) Characterising CASE constraints. Communications of the ACM (in press).

Sheridan, T. (1980) Computer control and human alienation. Technology Review, 83, 65–730.

Silver, M. (1988) On the restrictiveness of decision support systems. In: Organizational Decision Support Systems. Lee, R., McCosh, A. & Migliarese, P. (eds), pp. 259–270. Elsevier, Amsterdam.

Silver, M. (1991) Systems That Support Decision Makers. Wiley, Chichester, UK.

Venkatesh, M. (1995) Critique of ‘User responses to constraints in computerized design tools’ (personal communication). School of Information Studies, Syracuse University, Syracuse, NY.

Vessey, I., Jarvenpaa, S. & Tractinsky, N. (1992) Evaluation of vendor products: CASE tools as methodology companions. Communications of the ACM, 35, 90– 105.

## Biography

Donald L. Day is an assistant professor of information systems at Towson University, Baltimore, USA. His primary research interests are cultural aspects of technology acceptance and user responses to constraints in computerized design tools. He holds graduate degrees from American University (Washington, DC) and Syracuse University (Syracuse, NY). He has been a member of the Human Sciences Special Editorial Board of the journal Interacting with Computers since 1996, and is active internationally in the internationalization of products and systems.
