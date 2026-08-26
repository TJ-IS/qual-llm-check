---
otero_id: 17220
otero_key: "XD9MJ9AH"
title: "Group decision support with the Analytic Hierarchy Process"
authors: "Robert F. Dyer; Ernest H. Forman"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90003-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Group decision support with the Analytic Hierarchy Process

Robert F. Dyer and Ernest H. Forman
George Washington University, Washington, DC 20052, USA

The Analytic Hierarchy Process (AHP) is well suited to group decision making and offers numerous benefits as a synthesizing mechanism in group decisions. This paper explains why AHP is so well-suited to group decision making, shows how AHP can be applied in a variety of group decision contexts, and discusses four applications of AHP in group decisions. A tutorial on AHP is included as an appendix.

Keywords: Analytic Hierarchy Process, Group decision making, Multi-criteria, Conflict, Compromise, Consensus, Decision support, Goals, Objectives, Criteria, Alternatives, Bounded rationality, Decision making contexts, Pairwise comparisons, Resource allocation.

![](/api/attachments/XD9MJ9AH/fulltext/images/fb327b46314d678261a0060a4c89e48713e29fa63024c1aeb8b817d405c58676.jpg)

Robert F. Dyer is Associate Dean and Professor of Business Administration at the George Washington University. His teaching and research specialties are in the fields of consumer psychology, marketing research and marketing decision support systems. He holds a B.B.A. and M.B.A from Bowling Green and a D.B.A. with a specialization marketing from the University of Maryland. His articles have appeared in the Journal of Marketing, Journal of Marketing Research, Journal of

Consumer Research, Journal of Marketing and Public Policy and the Journal of Advertising Research among others. He is co-author with Ernest Forman of An Analytic Approach to Marketing Decisions, (Prentice-Hall, 1991).

![](/api/attachments/XD9MJ9AH/fulltext/images/5db17259b10cdb7e100f34183c6345399c0666f749fc8d13be0c87d6d08f2895.jpg)

Ernest H. Forman is Professor of Management Science at the George Washington University. His teaching and research specialties are in the fields of multi criteria decision making, operations management, statistics, cost benefit analysis, employee evaluation, group decision making, conflict resolution and strategic planning. His articles have appeared in journals such as Decision Science, European Journal of Operational Research, Telematics and Informatics,

IEEE Transactions on Reliability, and the Journal of the American Statistical Association. He is co-author with Robert Dyer of An Analytic Approach to Marketing Decisions (Prentice-Hall, 1991) and is co-developer with Thomas Saaty of Expert Choice.

## Introduction

Many DSS researchers and practitioners have pointed out that the fundamental model of DSS – the lonely decision maker striding down the hall at high noon to make a decision – is true only in rare cases (Turban [29]). In most organizations decisions are made collectively, regardless of whether the organization is public or private, national or international. It is sometimes difficult to achieve consensus among group members, or for all members of a group to meet. Group decision support systems (GDSS) are an emerging area of interest intended to support the group decision process. Typical definitions of GDSS are:

"A GDSS consists of a set of software, hardware, language components and procedures that support a group of people engaged in a decision-related meeting" (Turban [29]).

“A GDSS is an interactive, computer-based system that facilitates the solution of unstructured problems by a set of decision makers working together as a group” (DeSanctis and Gallupe [5]).

“A GDSS aims to improve the process of group decision making by removing common communication barriers, providing techniques for structuring decision analysis, and systematically directing the pattern, timing, or content of discussion” (DeSanctis and Gallupe [6]).

Nunamaker, Applegate and Konsynski [23], in expressing the need for better support of deliberation and judgment to enable more structured problem solving and decision making, cite Church and Eisenbert, who in 1969 said:

“It seems obvious that we cannot solve present day major political and organizational problems simply by grinding through a mathematical model or computer algorithm. What we require besides is the design of better deliberation and judgment” [4].

Nunamaker et al. cite numerous researchers who have expressed the need for future decision support systems designs to focus on supporting the decision process instead of isolated tasks. Simon [28] characterized three phases of the decision process – intelligence, design, and choice. To date, the emphasis with DSS and GDSS has been on the intelligence and design phases, with relatively little attention given to the choice phase. The Analytic Hierarchy Process developed by Thomas Saaty [24], is a process that focuses on the choice phase of decision making. AHP helps decision makers structure complex decisions, develop measures of utility, and synthesize measures of both tangibles and intangibles with respect to numerous competing objectives inherent in almost any decision. As such, it is well suited for a GDSS as defined by Turban [29] and DeSanctis [5], [6] and provides the type of support for deliberation and judgment referred to by Nunamaker [23]. This paper contains a discussion of how AHP expands the scope of GDSS to provide support for complex and unstructured decision problems. After presenting some background on AHP we will examine a basic approach to group decision making with AHP. Following that, we will look at alternative ways of applying AHP in different group decision making contexts.

## Background on AHP

The Analytic Hierarchy Process, developed by Saaty in the 1970's (see Saaty [24], [25]), is an approach to multi-criteria decision making problems of choice and prioritization. The development of Expert Choice (EC), the microcomputer software adaptation of AHP, (see Forman et al. [10]) has led to a growing number of applications of AHP in a variety of decision problems (see for example Golden et al. [12], [13] and Zahedi [33]).

The AHP enables decision makers to structure a complex decision in the form of a hierarchy. Each factor and alternative can be identified and evaluated with respect to other related factors. The ability to structure a complex decision and then focus attention on individual components amplifies a group's decision making capabilities. Judgments are solicited from members of the group about each facet of the decision problem. The methodology goes beyond conventional decision analysis techniques by not requiring numerical guesses. Subjective judgments on aspects of a problem for which no scale of measurement exists are easily accommodated. The judgments are used in deriving ratio scale priorities for the decision criteria and alternatives.

As noted by Saaty [24], AHP is based on three principles: decomposition, comparative judgments, and synthesis of priorities. The first stage in AHP model building is to decompose the overall decision problem into a hierarchy. A variety of basic hierarchical structures is available to fit a wide variety of decisions and environments. One usually begins with the simplest structure, consisting of the goal, criteria (and possibly subcriteria), and alternatives. The need to expand the model with scenarios and/or actors becomes readily apparent as one progresses with the analysis. Forman [11] provides a list of typical hierarchical structures:

\- Goal, criteria, alternatives

\- Goal, criteria, subcriteria, alternatives

\- Goal, scenarios, criteria, (subcriteria), alternatives

\- Goal, actors, criteria, (subcriteria), alternatives

\- Goal, ... subcriteria, levels of intensities (many alternatives)

A description of what the authors have found to be typical of many group decision meetings will help in understanding AHP's contribution to group decision making.

After an introduction to the decision at hand, a discussion (generally unstructured) ensues with members of the group speaking as the opportunity presents itself. Some members of the group speak more than others, possibly preventing or dissuading other members, who may have something significant to contribute, from speaking at all. $^{1}$ Because the discussion is unstructured, some aspects of the decision are addressed several times while other aspects are not discussed at all. Some group members have already made up their minds and use the discussion to support their position rather than share ideas and information and gain a better insight into the tradeoffs that must be made. Instead of discussing the pros and cons of each alternative, the pros of favored alternatives and the cons of competing alternatives are revisited time and time again. The discussion continues until the scheduled adjourning time approaches, at which point the leader attempts to obtain a consensus on the best alternative. There is little assurance that all available and pertinent information has been considered or that the consensus choice is the one most likely to achieve the organization's stated objectives.

In fact, there is often good reason to doubt that the best choice has been made, since, as summarized by Hogarth [17], it is well known that,

"A key aspect in choice is limited human ability to process information. We simply cannot handle all the information inherent in complex decision problems and, in particular to make the many kinds of tradeoffs implied by choices involving several conflicting dimensions. Intuitive judgment is deficient and requires ‘decision aids’."

Decision aids can take a variety of forms ranging from common simplistic strategies (see Janis [18]), to sophisticated computer supported decision analysis methodologies. Janis discusses three categories of common simplistic strategies: cognitive decision rules (seat of the pants approaches);

affiliative decision rules; and self serving and emotive rules.

The cognitive decision rules include satisficing; use of analogs and adages; nutshell briefings; incremental change (sticking closely to last decision bearing on the issue, making only slight changes to take care of the most urgent aspects of the problem currently at hand); and consensus. According to Janis, such rules are

“used to cope with cognitive limitations of the human mind, insufficient time for deliberation, limited organizational resources for information gathering, and related problem-solving constraints. These rules simplify the intellectual tasks posed by the complicated problems that confront executives who make important decisions.”

## Janis argues that

“Relying on a few such rules of thumb might generally work out fairly well when making routine choices or dealing with minor relatively unimportant decisions; however, when executives rely upon such rules to make important decisions, they save time and effort at the cost of risking being stuck with an ill-conceived choice entailing disastrous consequences that could have been avoided.”

In Simon's concept of bounded rationality [28], people do not optimize (i.e., choose the best of all possible alternatives) but satisfy by seeking a “satisfactory” alternative. Hogarth [17] explains that people simplify making a choice by using aspiration levels to characterize whether alternatives are acceptable. A cognitive decision rule that selects the first alternative that satisfies all aspiration levels is much easier to implement but often with less desirable results than a thorough evaluation of alternative tradeoffs with respect to all relevant criteria.

Affiliative decision rules identified by Janis include “avoiding punishment (CYA)”; “following the party line”; “rigging meetings to suppress the opposition”; and “preserving group harmony.” The self serving and emotive rules identified by Janis include “serving self interests”; “relying on gut feelings” (which depends on ones present mood); “retaliating”; “feeling that we ‘Can Do!’”, and “giving in to the ‘Wow! Grab It!’ feeling of elation." As with the cognitive decision rules, relying on the affiliative or emotive decision rules might work out in some routine choices or when dealing with relatively unimportant decisions, but can be disastrous when used for important, complex decisions.

Hogarth [17] categorizes ‘decision rules’ for choice into two groups: strategies that avoid conflicts inherent in a choice situation and strategies that confront such conflicts. Whereas conflict-avoiding strategies are non-compensatory, i.e., do not allow tradeoffs, conflict-confronting strategies are compensatory, i.e., allow a tradeoff of a low value on one dimension against a high value on another. The non-compensatory strategies have the advantage of being easier to execute cognitively, and parallel the common simplistic strategies discussed by Janis. The compensatory strategies, which are essential in the evaluation and selection phase of decision making if one is to achieve what Janis calls a “vigilant problem solving approach to decisionmaking” [18], are much less commonly employed since they have, until recently, been more difficult to implement.

Advances have been made in methodologies and technologies that help reduce or eliminate the above difficulties. The Analytic Hierarchy Process is one such methodology. Coupled with the power of today's personal computers, AHP enables decision making groups to overcome many limitations heretofore present in making important, complex decisions. Use of AHP is growing rapidly and AHP is today a widely used decision analysis methodology in the United States (for examples see Golden [13] and Zahedi [33]) as well as worldwide (for examples see Liu [21] and Vachnadze and Markozashvili [30]).

The Analytic Hierarchy Process is a compensatory methodology for evaluation and choice. AHP can accommodate both tangibles and intangibles, individual values and shared values. AHP helps to structure a group decision so that the discussion centers on objectives rather than on alternatives. Doing so eliminates the need for participants to resort to common simplistic decision strategies. Since an AHP analysis involves structured discussion, every topic or factor relevant to the decision is addressed in turn – in contrast to drifting from topic to topic which results in addressing some factors many times and others not at all. Individual group members with information, knowledge and expertise relative to a specific factor are naturally presented with the opportunity to make their views known; strong members of the group can not continuously bring the conversation back to their area of expertise. Because the analysis is structured, discussion continues until all available and pertinent information has been considered $^{2}$ and a consensus choice of the alternative most likely to achieve the organizations stated objectives is achieved – in contrast to not knowing when enough discussion has taken place and arbitrarily terminating at some scheduled adjourning time. One example of the ability of AHP to improve group decision was recently cited by Bard and Souskin an article “A Tradeoff Analysis for Rough Terrain Cargo Handlers Using the AHP: An Example of Group Decision Making” [3], where they observed

“From the standpoint of consensus building, the AHP methodology provides an accessible data format and a logical means of synthesizing judgment. The consequences of individual responses are easily traced through the computations and can be quickly revised when the situation warrants.

Readers unfamiliar with AHP are referred to an Appendix which contains a detailed example of the application of AHP to a site selection decision and illustrates many of the benefits discussed above.

## Group Decision Making Contexts

Saaty [25] [26] has described group decision making with AHP, including suggestions for assembling the group, running the decision-making session, trying to get the group to agree, inequalities of power, concealed or distorted preferences, and implementing the results. Although the preferred size and composition of the group is very much context dependent, some general guidelines are emerging. Mitchell and Wasil [22] observed that in applications at Woods Gordon, a Canadian management consulting firm, smaller decision groups were more efficient but that larger groups are often required for effective decision making so that all stakeholders are represented and the final decision accepted and implementation is facilitated.

We propose that there is a continuum of decision making contexts ranging from (1) common objectives – contexts where all parties have (basically) the same objectives, to (2) non-common objectives – contexts in which parties (or groups of parties) have non-shared (and sometimes hidden) objectives, to (3) conflict – contexts in which parties seek concessions from opposing parties. A conflict may involve retribution whereby the parties may seek retribution from one another for being harmed in the past. AHP can be applied in a variety of ways, depending on the context.

## Common Objectives Context

Four ways that AHP can be applied to the common objectives context include (1) consensus, (2) voting or compromising, (3) forming the geometric mean of individuals' judgments, and (4) combining results from individual models or parts of a model.

1. Consensus – If the members of a group have (basically) the same objectives, then it is advisable to have the members meet as a group and strive for consensus in both constructing the hierarchy and making judgments. This approach is attractive for two reasons. First, the discussion is beneficial to help ensure that relevant information possessed by any of the group members, either objective or subjective, is made available to the entire group. Second, consensus is desirable so that group members feel that they are “owners” of the decision and will make their best efforts to assure a successful implementation. In some decisions, being able to arrive at a consensus may be more important than the choice of the alternative, particularly if the alternatives are not drastically different from one another and the success of the decision depends on subsequent implementation efforts of the decision makers. The consensus approach was illustrated in the previous section.

2. Vote or Compromise - If a consensus cannot be obtained on a particular judgment then the group may choose to vote or compromise on an intermediate judgment. Either of these works well with the AHP methodology because the redundancy inherent in the pairwise comparisons assures that priorities change very little when small changes are made to any one judgment. When group members are made aware of this property they are more amenable to compromising instead of getting bogged down on a particular judgment.

3. Geometric Mean - If a consensus cannot be obtained and the group is unwilling to vote or to compromise on a judgment then a geometric mean (average) of the individuals' judgments can be calculated. Aczel and Saaty [1] have shown that the geometric mean is the uniquely appropriate rule for combining judgments since it preserves the reciprocal property of the judgment matrix. The Expert Choice implementation of AHP can calculate the geometric mean of a group of individual judgments.

4. Separate Models or Players – If group members have significantly different objectives or outlooks, or cannot meet to discuss the decision, each group member (or perhaps sub-groups) can make judgments separately. Questionnaires and protocols such as delphi and nominal group techniques can be used in conjunction with AHP either to structure the model, and/or to make judgments. Larreche and Montgomery [20] reported the result of a Delphi study undertaken to elicit criteria, subcriteria, and judgments concerning management science models' applicability to marketing. Saaty discusses the basic differences between AHP and the conventional (stand alone) Delphi, concluding that while both improve the quality of judgments, the hierarchy method better fits the human cognitive style because of the way it decomposes the problem and synthesizes the results. Additionally, with AHP, the group determines the important set of variables and therefore has better confidence in the relevance of their judgments. $^{3}$

Judgments by individual group members can be accommodated and processed in either of two ways:

4a. Separate models - Each group member enters judgments into a separate model. The priorities resulting from these models can then be averaged. $^{4}$

![](/api/attachments/XD9MJ9AH/fulltext/images/093b87b08083dad896720c038da43cdf0e1648b41f44138e807b278e6026ec1b.jpg)

FINANC'L --- FINANCIAL PROJECTIONS OF INVESTMENT, COSTS, REVENUES.
MFG FIT --- MANUFACTURING FIT WITH EXISTING PRODUCTS
MKT FIT --- FIT WITH OTHER PRODUCTS BEING MARKETED
MKT SHRE --- MARKET SHARE
PRESIDNT --- PRESIDENT
PROD. A --- ALTERNATIVE PRODUCT A
PROD. B --- ALTERNATIVE PRODUCT B
PROD. C --- ALTERNATIVE PRODUCT C
VP FINAN --- VICE PRESIDENT OF FINANCE
VP MFG --- VICE PRESIDENT OF MANUFACTURING
VP MKT --- VICE PRESIDENT OF MARKETING

Fig. 1. Model with Players.

4b. Players - A combined model consisting of a level of "players" below the goal node is constructed (see Figure 1). The criteria and subcriteria below each player need not be the same. Each group member evaluates those factors in their part of the combined model. $^{5}$ In using a player's level in an AHP model, consideration must be given to the weights attached to the players. This can be done in any of the following four ways:

4b1. Each player is assumed to be equally important. This assumption is equivalent to proceeding as in 4a above. Although this assumption may be interesting from a “what-if” perspective, it is seldom a reasonable assumption.

4b2. Players are first assumed to be equally important as in 4b1, and then a sensitivity analysis is performed to investigate the effect of varying player importance. If there is no significant effect then the equal player importance assumption is adequate even though it may not be realistic.

4b3. Pairwise comparisons about the relative importance of the players can be made. The question of who makes these judgments may stir controversy, particularly in the noncommon objective context. The approach in 4b4 (below) will both help to alleviate this controversy as well as help to determine realistic priorities for player importance.

4b4. Saaty [24] observed – “How to represent group judgment in a satisfactory way when people’s experience and judgments differ, and whose opinions should be taken more seriously and why, is a major problem in social study and conflict analysis”. He suggests that the AHP method be used “to derive priorities for the several individuals involved according to the soundness of their judgment”, and that “the factors affecting judgment may be: relative intelligence (however measured), years of experience, past record, depth of knowledge, experience in related fields, personal involvement in the issue at stake, and so on.” This can be done as part of an AHP model or in a subsidiary AHP model constructed for evaluating player importance. An example of such a subsidiary model in which experience, responsibility, past performance and education are used to determine the relative importance of the players is shown in Figure 2). The subsidiary model can be made more detailed by including sub-criteria and scenarios. The resulting player priorities can then be entered into the overall model (such as the one shown in Figure 1).

![](/api/attachments/XD9MJ9AH/fulltext/images/795bdd357450dd6bf61b2492eafb495cab1de4b548ef7fadaca68a4cd96b0dc8.jpg)  
Fig. 2. Model to Evaluate Player Importance.

The mediating effects on group member participation is an important consideration in GDSS. DeSanctis [6] observed that a “change in the otherwise natural (unsupported) distribution of member participation in group discussion may yield both positive and negative effects on decision quality and other outcomes.” Saaty [25] noted that “groups are often composed of people with different levels of status, knowledge, and experience. A superior might be unwilling to participate in a process that equalizes his or her judgment with that of subordinates.” If this is the case, the superior could ask the subordinates to evaluate the lower levels of the hierarchy and reserve the right to make judgments about the major objectives, and to alter lower level judgments. Vroom [32] discusses three “decision styles” available to a leader – authoritarian, consultative, and group. A leader must carefully choose the style appropriate for a particular decision. Factors relevant for choosing the style include decision quality, decision commitment, and control, each of which can have numerous sub-factors. The choice of a style might itself be sufficiently important and difficult to warrant a rational analysis with a technique such as AHP.

## Non-Common Objectives Context

For those contexts in which parties (or groups of parties) have non-shared (and sometimes hidden) objectives, it is obviously not possible to reach a consensus on all aspects of the decision. Suppose, for example, that a decision making group consisted of the many departments of a large corporation. The primary, shared, objective, is the well being of the corporation and its contribution to society. However, each department will have subsidiary interests which may not be common and may conflict with interests of other departments. Thus, although consensus might be possible on many aspects of the decision, consensus will not be on all aspects.

Where consensus is not possible, each of the latter three AHP approaches presented above are applicable. Each of these approaches help the parties focus on interests (objectives), rather than positions (alternatives). In Getting to Yes, Roger Fisher and William Ury [9] advise that “A negotiating position often obscures what you really want. Compromising between positions is not likely to produce an agreement which will effectively take care of the human needs that led people to adopt those positions.” Instead, they advise parties to focus on interests rather than positions, as interests really define the problem and a wise solution will reconcile interests rather than positions. AHP provides the framework for parties to do just that.

## Conflict Context

The conflict context is markedly different. In a theory of retributive conflict resolution developed in 1986, Saaty noted “In a conflict, particularly one of long duration, reason rarely prevails. Positions become entrenched and people seek not only to satisfy their own needs, but also to punish their opponents for having opposed them – or, at least, to pay a price for their opposition” [27]. One approach to retributive conflict’ resolution that has been successfully applied involves the evaluation of party concessions considering both costs and benefits from each party’s perspectives. Each conflicting party evaluates both those concessions that it might make to the opposing party, as well as those concessions it might receive in exchange. The evaluation includes each side’s perception of (1) the benefits it will accrue from the other’s concessions, (2) the costs the opponent will pay for making concessions (part of which may be punishment of the opponent), (3) the benefits the other party will gain from receiving concessions, and (4) its costs for making concessions (part of which may be punishment inflicted by the opponent.) AHP models for evaluating the perceptions of the benefits and costs of the concessions can contain both quantitative and qualitative factors that each side perceives as relevant. The evaluations are performed from each side's own value system as well as its perception of its opponent's value system. This approach enables an individual (or group) to identify and sharpen their personal values. It enables each side to develop a perspective of their needs and how these needs can be satisfied along with those of their opponent. By allowing people to factor their perceptions of the opponents value system into the solution, they are led to showing more empathy and purpose in defining their opponent's needs and can better grapple with how both side's needs can be satisfied in the overall solution of the conflict.

![](/api/attachments/XD9MJ9AH/fulltext/images/2f98cff166ad2ac8ef101eb08bcf3f50ab3969100ef4ad4787594d813e56e02f.jpg)

```txt
GOAL
NPV
RISK
MGT CRTL
ENVRMNT
VULNERBL
RELIABLT
DESIGN C-
FLEXBLTY-
LEVERAGE-
AGREEMNT-
ECP
EQUITY P-
3RD PRTS-
SOCIAL-
PHYSICAL-
NORTH
SOUTH
WEST
3RD PRTS --- THIRD PARTIES
AGREEMNT --- MANAGEMENT CONTROL IN ESTABLISHING AGREEMENTS
DESIGN C --- DESIGN COMPLEXITY
ENVRMNT --- ENVIRONMENTAL IMPACT
EQUITY P --- EQUITY PARTNERS
FLEXBLTY --- FLEXIBILITY TO ADAPT TO CHANGES IN FUTURE DEMANDS
GUERILLA --- VULNERABILITY TO GUERRILLAS
LANDSLID --- VULNERABILITY TO LANDSLIDES
LEVERAGE --- LEVERAGE IN INFLUENCING OPERATING DECISIONS
MGT CRTL --- MANAGEMENT CONTROL (FLEXIBILITY, LEVERAGE, AGREEMENTS)
NORTH --- NORTHERN ROUTE TO COVENAS
NPV --- NPV OF ALTERNATIVES INCLUDING INIT. OPER, REVENUE 10YR
OTHERS --- RELATIONSHIPS WITH OTHERS (ECP, EQUITY PARTNERS, 3RD PARTIES)
PHYSICAL --- PHYSICAL IMPACT ON ENVIRONMENT
RELIABLT --- RELIABILITY DURING OPERATIONS
RISK --- VULNERABILITY, MGT CONTROL AGRMNTS, RELIAB, DESIGN COMPLEXITY
SOCIAL --- SOCIAL IMPACT
SOUTH --- SOUTHERN ROUTE TO ORITO
VULNERBL --- VULNERABILITY (LANDSLIDES, GUERRILLAS, ..)
WEST --- WESTERN ROUTE TO BAHIA
```  
Fig. 3. Selecting the Best Pipeline Route.

Saaty and Alexander [27] have reported on the application of the AHP retributive conflict methodology to the apartheid conflict in South Africa, the free trade negotiations between Canada and the U.S., and to the conflict in the Punjab. Al-Awadi [2] has studied the application of the retributive conflict methodology to the Iraq-Iran war. Additional details of the methodology for resolving retributive conflicts are still under development. Some questions remain as to the best way to generate the concession lists, how to trade off sets of concessions that are acceptable to both sides in order to obtain a “comprehensive” settlement, what is meant by a “comprehensive” settlement, and what is the role of a mediator in achieving a comprehensive settlement.

## Typical Applications

To date, the majority of AHP applications have been in group settings. One reason for this may be that, according to B. Aubrey Fisher, groups often have an advantage over individuals when there exists a significant difference between the importance of quality in the decision and the importance of time in which to obtain the decision. $^{6}$ Another reason may be (as described in one of the six steps in the “reflective thinking” model that Fisher cites as the most common prescriptive approach to group decision making) the best alternative is selected by comparing alternative solutions, testing against selected criteria, a task ideally suited for AHP. Other reasons we suspect are the obvious needs for sharing ideas, consensus building, and justification purposes in group decisions. Despite of the many applications of AHP in group settings, most have tended to be kept proprietary, sometimes for reasons of competitive advantage, and sometimes because of the sensitive nature of the value judgments contained therein. The following are a few AHP applications in group settings that are typical of the hundreds AHP applications known to the authors. $^{7}$

$^{7}$ A forthcoming dictionary of hierarchies edited by Saaty and Forman, called a Hierarcon, will contain summaries of three to four hundred AHP applications.

## Oil Pipeline Route Selection

A South American oil company had to choose among three locations for construction of an oil pipeline (see Figure 3). The southerly and westerly route alternatives terminated on the western side of the Panama canal and the northern route terminated on the eastern side, resulting in a \$1/barrel difference in profit due to transportation costs. While this was a factor affecting NPV, management had to balance their profit motives with concerns for the environment, managerial control, and the riskiness of the venture. Risks included such factors as the vulnerability to landslides and guerilla attacks. This decision is an instance of a group with common objectives. Discussions among executives, engineers, and operat-

![](/api/attachments/XD9MJ9AH/fulltext/images/c961c398432d920dd2ba6bb8f8cb79036c210bf296a590c7ef51d80f51591350.jpg)

ADMIN --- ADMINISTRATION
APPLIED --- APPLIED RESEARCH
BASIC --- BASIC RESEARCH
CAPABLTY --- MAINTAIN/IMPROVE SCIENTIFIC CAPABILITIES
CENTER --- CENTER OF EXPERTISE FOR FISHERY SCIENCE
COORDNT --- COORDINATION
CRED/IMG --- CREDIBILITY/IMAGE
ENVIRNMT --- ENVIRONMENT
FACILT'S --- FACILITIES
FISHER'S --- FISHERIES
FUT PROF --- INFLUENCE AND OR TRAIN FUTURE PROFESSIONALS
INFO DIS --- INFORMATION DISSEMINATION
MGMTNEFC --- MANAGEMENT OF NEFC
MONITRNG --- MONITORING OF FISHERIES, POPULATION AND ENVIRONMENT
PERSONNL --- PERSONNEL
PLAN/EVA --- PLANNING AND EVALUATION
POPULA'N --- POPULATION
PUBLIC I --- PUBLIC INFORMATION
RESEARCH --- BASIC AND APPLIED RESEARCH
SAT HDQ --- SATISFY HEADQUARTERS (INCLUDING FIREFIGHTING)
SCI ADVI --- SCIENTIFIC ADVICE
SCI RESL --- SCIENTIFIC RESULTS
SCINT'TS --- MAINTAIN/IMPROVE SCIENTISTS
TECHNLGY --- TECHNOLOGY

Fig. 4. Evaluating NEFC Activities.

ing managers were open and frank, with each group member eager to learn from the others' information and insights. There was no difficulty in reaching consensus.

## Allocating Resources Amid Budget Reductions

In light of the looming problem of a severe budget crisis, the Research Planning and Coordination (RPAC) staff of the Northeast Fisheries Center (NEFC) sought a comprehensive and rational methodology for supporting its evaluations and budget recommendations relative to Center research programs. With the consent of the Center management, they adopted the Analytical Hierarchy Process as that methodology. The AHP was subsequently used in a study designed to provide the Science and Research Director with Recommendations for FY91 Center Research Program budget allocations.

Discussions were held as several meetings, including preliminary meetings of the RPAC staff to lay the groundwork for the process, and subsequent meetings with RPAC Planning and Evaluation Staff, Division Chiefs and Staff Chiefs.

The model shown in Figure 4 was developed at the initial meeting of the division chiefs. $^{8}$

As can be seen from this model, projects are evaluated with respect to the importance of basic and applied research, the need to monitor the fisheries environment and populations, ability to disseminate information, contribution to the credibility and image of the NEFC, and the concerns of the NEFC managerial staff.

Because of the large number of projects being evaluated, a ratings approach was used; instead of comparing each project with every other project, each project was rated according to how much it contributes to each of the center's objectives and subobjectives. The values of the intensities used to rate the projects ranged from EXTREME to a TAD are derived as a ratio level measures using the typical pairwise relative comparison procedure of AHP. Projects not making any contribution in a specific area receive no rating and hence no value for that area. The total value for each project reflects the overall relative contribution of that project to the center's mission. The project values are ratio level measures so that a project with a total value of twice that of another project in essence is contributing twice the amount to the center's mission. The project priorities were then used in an integer linear programming model to determine the best combination of project funding levels subject to budgetary and other managerial constraints, including constraints to assure that each project received some minimal percentage of last years expenditures, to assure that projects do not grow by more than a specified percentage, and to recognize the dependencies within and between specific project activities.

## University Budget Advisory Committee

The budget advisory committee of George Washington University's School of Business and Public Management used the model shown in Figure 5 to derive recommendations to the Dean for the allocation of funds for improving the school's effectiveness. Priorities were derived for educational programs and innovations, research activities, service contributions to community and professional organizations, facilities for educational and administrative faculty, support functions of education and research activities, compensation of new and current staff, and revenue enhancement activities. Priorities were developed by considering the school's current environment and approximate funding levels, and by asking where discretionary funds would best be allocated, and in what proportions. As might be expected, departmental committee representatives had some differences in objectives and views. This led to redefining several factors and subfactors that were originally proposed. Somewhat surprisingly, a consensus was possible on most judgments, usually after an open discussion of the problems and opportunities that department representatives expressed about the specific factor under consideration. On only a few occasions was it necessary to use the geometric average because a consensus could not be achieved.

## Faculty Member Selection

One of the author's faculty had interviewed numerous candidates for a new tenure track posi-

```txt
PROGRAMS
MARKETING-
CUR. DEV-
NEW PGMS-
METHODS
RESEARCH
SUMMER $
AWARDS
C.REL'F-
SPACE
EQUIP.
SERVICE
COMMUNTY-
PROF ORG-
FACILT'S
ED FACIL-
ADMIN F-
F OFFICE
SUPPORT
SYSTEMS-
STAFF
TRAVEL
SCHOLRSH-
COMPENSA
STAFF
CUR FCLT-
FUT FCLT-
REV. ENH
FUND RAI-
ENTERPRI-
ADMIN F --- ADMINISTRATIVE FACILITIES
AWARDS --- BOTH FINANCIAL AND NON FINANCIAL
C.REL'F --- COURSE RELIEF
COMMUNTY --- COMMUNITY SERVICE
COMPENSA --- COMPENSATION OF STAFF, CURRENT FACULTY, NEW FACULTY RECRUITMENT
CUR FCLT --- CURRENT FACULTY
CUR. DEV --- CURRICULUM DEVELOPMENT
ED FACIL --- EDUCATIONAL FACILITIES
ENTERPRI --- ENTERPRISES
EQUIP. --- EQUIPMENT FOR RESEARCH
F OFFICE --- FACULTY OFFICES
FACILT'S --- EDUCATIONAL, ADMINISTRATIVE AND FACULTY OFFICE FACILITIES
FUND RAI --- FUND RAISING
FUT FCLT --- RECRUITING FUTURE FACULTY
MARKETNG --- MARKET OUR PROGRAMS
METHODS --- NEW METHODS OF TEACHING
NEW PGMS --- NEW PROGRAMS
PROF ORG --- SERVICE TO PROFESSIONAL ORGANIZATIONS
PROGRAMS --- EDUCATIONAL PROGRAMS AND INNOVATIONS
RESEARCH --- RESEARCH ACTIVITIES
REV. ENH --- SCHOOL REVENUE ENHANCEMENT
SCHOLRSH --- SCHOLARSHIPS
SERVICE --- SERVICE CONTRIBUTIONS TO COMMUNITY AND PROFESSIONAL ORGANIZATIONS
SPACE --- SPACE FOR RESEARCH
STAFF --- STAFF
SUMMER $ --- SUMMER SUPPORT
SUPPORT --- SUPPORT OF EDUCATION, RESEARCH AND SERVICE ACTIVITIES
SYSTEMS --- TEACHING DELIVERY SYSTEMS, STUDENT TRACKING SYSTEMS ETC.
TRAVEL --- TRAVEL TO CONFERENCES, ETC.
```  
Fig. 5. Allocation of Funds.

tion. The applicants were of very high quality and our appointment promotion and tenure committee (comprised of professors from management science, organizational dynamics, and management of science and technology areas) had narrowed the field to three candidates, all of which were highly desirable. We met to discuss the three candidates. The discussion drifted for about half an hour, each candidate being cited as very strong in specific ways, but with no candidate gaining support at the expense of the others. I resisted the temptation to suggest using AHP, sensing that some members of the committee, not familiar with AHP, might feel that the selection of a faculty member was too qualitative and value laden a methodology using “measurement”. Finally, one of the other members of the committee who was familiar with AHP suggested that we develop an AHP model. It took about ten minutes to identify the criteria and to begin making relative judgments about criteria importance when – eureka!, almost simultaneously we all “knew” which candidate we wanted most. By thinking clearly about the relative importance of the criteria, we quickly came to a decision without even completing the judgments in the model.

## Summary and Conclusions

Current GDSS includes both data management and model management, providing better access to data and the analysis of data, as it is needed, on an ad hoc basis. The focus is presently on models, reflecting what Nunamaker $[23]$ cites as “a growing migration from the data centered view to a recognition that models are the sources of assertions and assumptions that give meaning to data relations.” We suggest the focus should now migrate to a decision centered view, recognizing that the complexities of most decisions require the synthesis of possibly several models, in addition to qualitative considerations. The Analytic Hierarchy Process is a methodology that can provide such a synthesis.

AHP supports what DeSantis defines as the aims of a GDSS, “to improve the process of group decision making by removing common communication barriers, [structuring] the decision analysis and systematically directing the pattern, timing, [and] content of discussion” [5]. AHP helps center a discussion around objectives, rather than alternatives. There is no need for participants to resort to common simplistic decision strategies even when there is a multitude of information and conflicting objectives. Because the discussion is structured, addressing each facet of the decision in turn, group participants are guaranteed the opportunity to contribute their expertise. Judgments can be based on hard data, results of other mathematical and simulation models, as well as general knowledge and experience. Instead of drifting from topic to topic, the group progresses toward a resolution of the decision as ratio scale priorities are developed for each aspect of the problem. An AHP model can be easily modified as additional information or insights become available. Because AHP is structured, yet flexible, it is a powerful and straightforward methodology that can be integrated into almost any group decision support system.

## Appendix

## AHP Applied to a Site Location Decision

This appendix provides a step by step description of how AHP is applied to a typical multi-criteria decision. Assume that a group of decision makers is meeting to determine the best retail site within a geographic area for a small ice cream store catering to teenagers, young children and families. Also assume that they have narrowed down the site alternatives to three locations: The first one is in a suburban shopping center. The second site is on Main Street (the main business district area of the city). The third is a suburban shopping mall. Details regarding each of these sites follow.

## Suburban Shopping Center

A vacant store that was formerly a pizza shop is available for \$28 per square foot per month in a neighborhood strip shopping center at a busy highway intersection. The area is populated with forty-five thousand (mostly middle income, young family) residents who live in townhouses id single family dwellings. The strip center is constantly busy with retail customers of a major supermarket chain, a drug store, a hardware store, a hair stylist/barber shop, and several other small businesses sharing the location. No ice cream shops are located in the community.

## The Mall

This location would cost \$45 per square foot per month. We would be in the main food area of a major suburban mall with seventy five retail shops and three magnet stores, Sears and two other large department stores. The Mall is frequented by teens, young mothers, and families, especially on weekend days and weekday nights. There are three ice cream stores at various locations within the mall.

## Main Street

For \$32 per square foot per month we can locate our store in the ground level of a

![](/api/attachments/XD9MJ9AH/fulltext/images/3f47a0e7995b44259aab8a576890ed2df48fbb47944e104eef49364d55e6b42e.jpg)

COMPET'N --- COMPETITION--# OF COMPETITIVE STORES IN SAME TRADING AREA
COST --- COST PER SQUARE FOOT OF RETAIL SPACE
CUST.FIT --- CUSTOMER FIT--SITE'S CUSTOMER TRAFFIC VS. TARGET MARKET SPEC'S
MAIN ST. --- MAIN STREET--CENTER CITY, OFFICE & RETAIL COMPLEX SITE
SUB.CTR. --- SUBURBAN STRIP SHOPPING CENTER
THE MALL --- SUBURBAN SHOPPING MALL SITE
VISIBLE --- VISIBILITY OF STORE FRONT

Fig. 6. Basic AHP Model with Goal, Criteria and Alternatives.

large high rise office and retail complex The shop would be in a slightly out of the way corner of the building. The majority of the people frequenting the building and the surrounding area are young professionals who are in the area Monday through Friday only. There is one ice cream store within a ten block radius of this location.

Inconventional group discussions about a decision such as this, data is analyzed and presented and the group members discuss the advantages and disadvantages of the alternatives. If the group is well organized and thorough it might prepare a summary such as the following:

While The Mall is best in terms of both customer-fit and visibility, it is the most expensive and has the most competition. The Suburban Center location is both the least costly and best in terms of competition, yet it does not have as good visibility nor as good a customer-fit as The Mall location. Perhaps the easiest part of the decision is with respect to the Main Street location, which, when compared to either of the other two alternatives, is not very attractive. $^{9}$

Assuming that the information given is accurate and relevant, and assuming that a reasonable analysis of the information is made to produce such a summary, the group still will have difficulty resolving conflicts between the competing objectives. This difficulty can be managed by using the information about the three candidate sites to construct a basic AHP model for the analysis.

An analysis of a decision using AHP involves several steps: (1) decomposing the problem into a hierarchical structure, (2) making comparative judgments in order to establishing priorities for the elements of the hierarchy, and (3) performing a synthesis of various competing factors. Additionally, a thorough analysis involves (4) investigation of the sensitivity of the results, and (5) iteration to assure that all relevant aspects of the problem have been considered.

## Step 1 - Decomposing the problem

The first step in using AHP is to develop a hierarchy by organizing the problem into its basic components. The three major levels of a hierarchy for a basic AHP model, as shown in Figures 6 and 7, are the goal, criteria, and alternatives. $^{10}$

SELECT THE BEST RETAIL SITE

![](/api/attachments/XD9MJ9AH/fulltext/images/f1e0500c3fd4190a3eaf24852dcc74114a55a34b8710590e6c823f3d723fceb5.jpg)

\- The basic AHP model includes goal, criteria, alternatives:

GOAL - a statement of the overall objective; in our example: to select the best retail site.

CRITERIA – A goal is achieved by satisfying (to the maximum extent possible) objectives. Criteria will be used to evaluate how well each alternative satisfies the decision objectives. Although the words criteria and objectives are not synonymous lexicographically, they can be used synonymously in an AHP analysis. The objectives in our simple example include Cost, Visibility, Customer Fit, and Competition.

ALTERNATIVES – The (feasible) alternatives that are available to reach the ultimate goal; in our example: Suburban Shopping Center, The Mall, and Main Street.

![](/api/attachments/XD9MJ9AH/fulltext/images/e30f3980672d7514cf79bca386246f8af8a77186b7e8091c639fff17fb66f983.jpg)  
Fig. 8. AHP Model with Subcriteria.

AHP can easily support more complex hierarchies containing subcriteria, scenarios, uncertainties, and players.

\- SUBCRITERIA – Subcrieria are used to introduce more specificity in the model. The addition of subcriteria (or sub-objectives) further details the objectives. The addition of subcriteria may add improved content validity and precision to the alternative evaluation process. The need for certain subcriteria may be evident when first constructing a model, while others may become evident during the evaluation process. For example, in comparing two alternative sites with respect to cost, it may be difficult to state which is preferable because one is preferred with respect to initial fixup costs while the other is preferred with respect to subsequent rental costs. Figure 8 shows how subcriteria fixup and rent can be added under the Cost criterion. Alternatively, a financial model could be constructed that includes both initial cost and rental costs. The financial model could then be used to calculate measures such as total discounted cost and initial investment required. These could be included as subcriteria under cost.

The above discussion illustrates a “top down” way of thinking. A “bottom up” approach would consist of identifying every possible criterion for the decision, and then structuring them into clusters, sub-clusters, and so on. The highest level clusters would be the criteria, those below the sub-criteria, those below the sub-sub criteria, finishing with the alternatives.

\- SCENARIOS FOR UNCERTAINTIES. The importance of different criteria or the Preference for alternatives may depend on conditions that may be uncertain. Uncertainty can be represented by including SCENARIOS. Scenarios representing three possible states of the economy – gloomy economy, boom economy, and status quo – are shown in Figure 9. The addition of scenarios permits the evaluation of criteria importance or alternative preference to be made with respect to the uncertain outcomes. When criteria appear at the level below scenarios, the decision maker is essentially basing the importance of the criteria on conditional probabilities. For example, if the outlook for the economy were gloomy, cost might be of more importance than if the economy were booming.

![](/api/attachments/XD9MJ9AH/fulltext/images/e66a087ffc523103ae0dd3d7c7501c9380120e74175cfccf20d06b25e31190d7.jpg)  
Fig. 9. AHP Model with Environmental Scenarios.

Environmental scenarios are also examined through the pairwise comparison process; the only difference is that comparisons are made about the likelihoods of the occurrence of the environmental scenarios. It is possible to incorporate executive intuition as well as the results of a variety of forecasting techniques, such as time series analysis, regression analysis, or consensus of experts into an AHP model when evaluating the likelihoods of occurrence of the various scenarios. This can be done in the model itself or in a subsidiary model. $^{11}$ This ability to combine executive intuition with hard results from quantitative forecasting techniques is a hallmark of advanced decision support capability.

\- PLAYERS. Decisions are often made through group consensus, yet sometimes it is difficult for all members of a group to meet or for each member's opinions to be heard during a meeting. A level of PLAYERS can be added to an AHP model as was illustrated in the paper body and will be illustrated later in this appendix.

## Step 2-Comparative Judgments To Establish Priorities

After the problem is arranged in a hierarchical fashion, the next step is to evaluate relative preferences for the alternatives with respect to each of the criteria and to evaluate the relative importance of the criteria with respect to the overall goal. The basic approach for deriving priorities with AHP is by way of pairwise relative comparisons. $^{12}$ When pairwise comparisons are used in AHP, priorities are derived based on the comparisons instead of being arbitrarily assigned as is done in many weights and scores methodologies. The derived priorities are easier to justify and arc usually more accurate, as will be discussed below. In deriving the priorities, the utility curve of the decision makers is implicitly taken into account. Pairwise comparisons of the elements at each level of an AHP model are made in terms of one of the following:

\- Importance – when comparing criteria or players with respect to their relative importance.

\- Preference – when comparing the preference of alternatives with respect to their specific qualities relative to a criterion.

\- Likelihood – when comparing uncertain events or scenarios with respect to the probability of their occurrence.

Almost every decision involves at least one criterion for which no quantifiable scale exists. In fact, the higher the level of decision making within an organization, the more important these non-quantifiable criteria become and the greater the benefits of a process like AHP which can derive ratio scale priorities from verbal comparisons of criteria that are typically thought of as nonquantifiable and subjective.

The Expert Choice software implementation of AHP accommodates pairwise comparisons either verbally, numerically, or graphically. The verbal mode uses a nine point scale consisting of five words (equal, moderate, strong, very-strong and extreme) and four intermediate levels (e.g., between moderate and strong). There are important advantages in being able to use a comparative verbal mode to express judgments. Pairwise relative judgments are easier to make than absolute judgments. For example, it is much easier to estimate how much larger a basketball is than a baseball, then it is to estimate how large a basketball is (e.g., how many cubic inches) or how large a baseball is. Pairwise relative verbal judgments are also easier to discuss, justify, and agree on. If, for example, in discussing the relative importance of the criteria in the site selection example, a group member might have difficulty justifying his or her judgment that cost is 3 times as important as visibility. Why not 2.9 or 3.1 times as important? Why not twice as important? Or five times as important? It is easier to justify the opinion that cost is “moderately” more important than visibility by using a variety of arguments including both hard data and past experience. Using inexact words alleviates the discomfort than many people feel when forced to put hard numbers to subjective feelings. Furthermore, the use of inexact words makes it easier for group members to compromise and reach a consensus. There is, however, one important obstacle to overcome. How to combine judgments expressed in words about different aspects of a decision?

Numbers can (and have) been “put behind” words in a computer program that subsequently performs some algebraic manipulations. But there is no assurance that the numbers accurately reflect the meaning a group had in mind when it made verbal judgments. A word can mean different things to different individuals and to different groups. Even if the group itself attempts to “assign” numbers to words, the group members may have difficulty agreeing on the numerical values to be assigned to the words, and later remembering what these values were. Assigning numbers to words conceals but does not eliminate the difficulty of making judgments about imprecise or subjective factors.

AHP uses a straightforward yet powerful approach for deriving “accurate” ratio scale priorities from imprecise verbal comparisons. Priorities are derived by calculating eigenvalues and eigenvectors of reciprocal matrices representing pairwise comparisons. (See [24], for details). Because more comparisons are made (and entered into a matrix of comparisons) than are required to calculate relative priorities, the comparison matrix is said to contain some redundancy. This redundancy is, in a sense, used to “average” errors of judgment in a manner analogous to averaging errors when estimating a population mean. The errors of judgment include errors in translating from imprecise words to the numbers that are used to represent these words in the algorithm. Consequently, if two groups were to estimate the relative sizes of some objective set of objects, they will arrive at approximately the same results regardless of whether one group tends to use more extreme words than the other group. In numerous tests with this methodology, involving subjects visually comparing areas of geometric shapes using verbal judgments, the average root mean square error of the resulting priorities was only

![](/api/attachments/XD9MJ9AH/fulltext/images/004d1aa75e1273dc76ed9554ca37927a2e9973c7d31a128ac0053533fcae56ba.jpg)  
Fig. 10. Verbal Pairwise Comparison.

2.4%. $^{13}$ Saaty conducted an experiment in which he placed chairs different distances from a light source and asked people to judge the relative brightness of the chairs. The results matched the inverse square law of physics almost exactly (Saaty [24]). Thus, pairwise comparisons with redundancy, as used in the Analytic Hierarchy Process, enables those involved in group decision making to both improve measures of things they already know how to measure as well as develop measures for things they have difficulty measuring, namely qualitative and subjective factors.

While a decision hierarchy is defined top down, it is often evaluated bottom up because an examination of the considerations involved in the lower level comparisons of alternative preferences helps the group better understand the tradeoffs that must be made at the higher levels of the hierarchy. $^{14}$ At the lowest level, the relative preferences of the alternatives with respect to each (sub)criterion can be derived using a mode most appropriate to the (sub)criterion. For example, when determining the relative preferences for

Main Street, The Mall, and the Suburban Center with respect to cost, the group may choose to use an absolute mode since cost is an objective criterion and priorities can be determined to be inversely proportional to the costs of the sites. This, of course assumes a linear utility, which is the exception rather than the rule. Therefore, a pairwise numerical, or even pairwise verbal mode of comparisons might be used. When discussing the relative preferences for the sites with respect to visibility, the pairwise verbal mode would be the most appropriate. We will assume that judgments have already been made about the lower level of our sample hierarchy and illustrate the solicitation of pairwise verbal judgments in deriving priorities for the relative importance of the decision criteria.

In deriving the priorities for the criteria (cost, visibility, customer fit, and competition), verbal pairwise comparisons will be made about the relative importance of each criterion when compared to every other criterion. We will assume that the group has already examined the three alternatives under consideration, having discussed the trade offs using both hard data and intuition. The first judgment to be made is about the relative importance of cost vs. visibility. In addition to looking at the information given for each of the sites, the group's intuition might tell them that many customers will find the shop through promotion, word of mouth, and so on, even if the storefront lacks high visibility. Their financial analysis, which includes the rent of the sites, makes it clear that cost is more important, since they would be stressed a bit financially if they chose the high visibility, more costly location. Following a discussion, the group consensus might be that an affordable location is moderately more important than one that is highly visible. This consensus is represented in Figure 10 and can be read as: With respect to the goal, cost is moderately more important than visibility.

![](/api/attachments/XD9MJ9AH/fulltext/images/6d36a25a471214d4296eb2e68390a157d6ac4a031997a0154145cb43324d53ff.jpg)  
Fig. 11. Judgments and Resulting Priorities.

Comparisons of the relative importance between each of the other pairs of criteria are made in a similar fashion. These comparisons form a set of judgments that is used as the basis for deriving the relative priorities of the criteria with respect to the goal. In general, if there are N factors being considered, there will be $N \times (N-1)/2$ judgments, which can be represented in a numerical form and displayed as the upper diagonal of a matrix, as can be seen at the top of Figure 11. This set of judgments contains redundancy since only N-1 judgments are required to solve for priorities using simple algebra. The redundancy is very useful, however, as it improves accuracy in a manner somewhat analogous to estimating a quantity by taking the average of repeated (and hence redundant) observations.

The increased accuracy permits priorities to be calculated even for less accurate or imprecise judgments, such as when words are used instead of numbers. An additional property related to the redundancy of judgments is a measure of consistency, which will be discussed shortly.

The priorities are derived from the matrix ${}^{15}$ of judgments by using an eigenvector approach as described in [24]. Harker and Vargas [16] discuss the merits of this approach. The priorities derived from the judgments in the matrix are shown at the bottom of Figure 11. Notice that cost is only about twice as important as visibility although the verbal judgment “moderate” was represented numerically as 3 times more important. This illustrates that the priorities are derived from a complete set of judgments, not just one, and is the reason that imprecise words can be used to derive meaningful priorities as discussed above.

The primary drawback of the paired comparison mode of AHP is obviously the time it takes to make the paired comparisons, particularly when the comparison matrix becomes larger. There are several ways to save time and still use pairwise comparisons. One approach is based on Harker's research $[15]$ that calculates priorities even with one or more missing judgments. The tradeoff is one between accuracy and time. The fewer the judgments, the less accurate are the results. In considering this tradeoff the group should consider the importance of the decision being analyzed and realize that a few hours invested in a thorough decision analysis are often more than warranted.

GOAL: SELECT THE BEST RETAIL SITE
With respect to
GOAL

<table><tr><td colspan="4">COMPET&#x27;N :COMPETITION--# OF COMPETITIVE STORES IN SAME TRADING AREAis 5.0 TIMES (STRONGLY) MORE IMPORTANT THANCOST :COST PER SQUARE FOOT OF RETAIL SPACE</td></tr><tr><td>COST</td><td>VISIBLE</td><td>CUST.FIT</td><td>COMPET&#x27;N</td></tr><tr><td>COST</td><td>3.0</td><td>3.0</td><td> $\uparrow > 5.0<$ </td></tr><tr><td>VISIBLE</td><td></td><td>1.0</td><td>5.0</td></tr><tr><td>CUST.FIT</td><td></td><td></td><td>1.0</td></tr><tr><td>COMPET&#x27;N</td><td></td><td></td><td></td></tr></table>

Fig. 12. Inverted Judgment.

## Evaluating Inconsistency

The theory of AHP does not demand perfect consistency. Instead, it provides, in the form of an inconsistency ratio, a measure of how much inconsistency there is in each set of judgments. (See Saaty [24] for details). An inconsistency ratio of 0 means that a set of judgments is perfectly consistent, while an inconsistency ratio of 1.0 (or 100%) means that the inconsistency is equivalent to what would be expected from random judgments. While it is natural for a group to want to be consistent, consistency does not mean that things are correct. Allowing some inconsistency permits a group to communicate better and learn from each other. As a rule of thumb, an inconsistency ratio of about 10 percent or less is usually considered “acceptable”, but the particular circumstance may warrant the acceptance of a higher value. $^{16}$ An inconsistency ratio of 0.098 is displayed at the bottom of Figure 11 for the judgments about the relative importance of the criteria.

There are several reasons why inconsistency occurs as well as some useful information that the inconsistency ratio conveys. A common cause of a high inconsistency is a clerical error. When entering one or more judgments into a computer, the wrong value or perhaps the inverse of what was intended may be entered. Suppose a clerical error was made in our example by inverting the judgment about the relative importance of Cost and Competition, that is by specifying that Competition was strongly more important than Cost, instead of the vice versa. This inverted judgment is shown in Figure 12 and the resulting priorities and inconsistency ratio are shown in Figure 13.

![](/api/attachments/XD9MJ9AH/fulltext/images/d95af285a1f0276d3ccbf57354f37f3392e61057457c05177f7c45cbbbf7765b.jpg)  
Fig. 13. Priorities with Inverted Judgment.

Notice that the clerical error has caused the inconsistency ratio, which was only 0.099 (in Figure 11) without the clerical error, to rise to 0.854, a sure indication that something is wrong. AHP software like Expert Choice can help in finding the most inconsistent judgment(s).

A second cause of inconsistency is lack of information. If there is little information or experience about the factors being compared, then judgments will appear to be more random and a high inconsistency ratio will result.

A third cause of inconsistency is lack of focus or concentration during the judgment process. The group making judgments can fail to concentrate if they are not really interested in the decision or become fatigued (at which point the process should be suspended to resume at a later time). It is a good idea to schedule time formally in blocks not exceeding two hours or so, and in an atmosphere conducive to discussion and contemplation.

A fourth cause of a high inconsistency ratio is a reflection that the real world is rarely perfectly consistent. Professional sports are a good example. It is not uncommon for Team A to defeat Team B, after which Team B defeats Team C, after which Team C defeats Team A! Such inconsistencies may be explained as being due to random fluctuations or to underlying causes (such as match-ups of personnel), or a combination. Regardless of the reasons, real world inconsistencies do exist and thus will appear in a group's judgments.

A final cause of inconsistency is inadequate model structure. Ideally, a group should structure a complex decision in a hierarchical fashion such that factors at any level are comparable within an order of magnitude (or so) to other factors at that level. Practical considerations, for instance, a desire to keep a model as simple as possible in order to save time, might preclude such a structuring. Still, it is possible to get reliable results. Suppose, for example, we compared several items that differed by two orders of magnitude. One might erroneously conclude that the AHP scale is incapable of capturing the differences, since the scale ranges from 1 to 9. However, because the resulting priorities are based upon second, third, and higher order dominances, AHP can produce priorities far beyond an order of magnitude. For example, if A is nine times B, and B is nine times C, then the second order dominance of A over C is 81 times. A higher than usual inconsistency ratio will result because of the extreme judgments necessary. If one recognizes this factor as the cause (rather than a clerical error, for example), one can accept the inconsistency ratio even though it is greater than 10 percent.

It is important that a low inconsistency not become the goal of the decision making process. A low inconsistency is necessary but not sufficient for a good decision.

## Step 3 - Synthesizing To Obtain Overall Priorities

The priorities that are derived from each set of judgments are called “local” priorities to convey the fact that they are the priorities relative to the parent node. The priority of a node relative to the overall goal is called a “global” priority. The local priority of a node determines what percentage of the parent’s global priority is allocated to that node. As can be seen in Figure 14, the global priority of a node is derived by multiplying a node’s local priority by the global priority of its parent. The sum of the local priorities of a set of branch nodes is always one, while the sum of the global priorities of a set of branch nodes is always equal to the global priority of its parent.

An important contribution of AHP is that all priorities are ratio scale numbers, and thus can be meaningfully synthesized (through multiplications and additions) to derive an overall prioritization and ranking. The details of the synthesis and overall results for the retail site model are shown in Figure 15.

For this example the synthesis shows The Mall to be the best retail site. We can examine the details of this decision to see that this site alternative is best overall because it is most visible and has the best customer fit. Although The Subur-

Sorted Synthesis of Leaf Nodes with respect to GOAL

SUB.CTR. --- SUBURBAN STRIP SHOPPING CENTER

THE MALL --- SUBURBAN SHOPPING MALL SITE

L --- LOCAL PRIORITY: PRIORITY RELATIVE TO PARENT

G --- GLOBAL PRIORITY: PRIORITY RELATIVE TO GOAL

SELECT THE BEST RETAIL SITE  
![](/api/attachments/XD9MJ9AH/fulltext/images/678ddc80f70e471ecc3cfac62f26131b999668a9ebf1e59243feaa9220f7f020.jpg)  
COMPET'N --- COMPETITION--# OF COMPETITIVE STORES IN SAME TRADING AREA  
CUST.FIT --- CUSTOMER FIT--SITE'S CUSTOMER TRAFFIC VS. TARGET MARKET SPEC'S  
MAIN ST. --- MAIN STREET--CENTER CITY, OFFICE & RETAIL COMPLEX SITE  
Fig. 14. Local and Global Priorities.

OVERALL INCONSISTENCY INDEX = 0.07  
![](/api/attachments/XD9MJ9AH/fulltext/images/f1ae9fb1333dc810661a23aeeee2d4044fc1a6f918e916ecd1580cf82e1e3a40.jpg)  
MAIN ST. --- MAIN STREET--CENTER CITY, OFFICE & RETAIL COMPLEX SITE  
SUB.CTR. --- SUBURBAN STRIP SHOPPING CENTER  
THE MALL --- SUBURBAN SHOPPING MALL SITE  
Fig. 15. Synthesis for Site Location Problem.

![](/api/attachments/XD9MJ9AH/fulltext/images/b5848057b98a4ca0d34d09a81009be92cb8f644091a557a47c7c66594a721a65.jpg)  
Fig. 16. Gradient Sensitivity Analysis for Cost Criterion.

ban Center location is less costly and has less competition, the AHP evaluation helped determine that these were not commensurate with the better visibility and better customer fit of The Mall location.

## Step 4 - Sensitivity Analysis

Sensitivity analysis assists with questions about the relative importance of information or about how possible changes in information will affect results. $^{17}$ Sensitivity analysis is also conducted in order to gain a better understanding of a decision analysis. According to Von Winterfeldt and Edwards [31], the goals of sensitivity analysis are:

1. to gain insights in the nature of the problem, its relation to the formalizations that have occurred to you, and the model,

2. to find a simple and elegant structure that does justice to the problem, and

3. to check both the correctness of the numbers and the need for precision in refining them.

A sensitivity analysis also can be used to suggest that a decision be postponed, or that one live with a sensitive (and hence vulnerable) decision, monitoring actual results closely.

A sensitivity analysis can be performed to see how sensitive the alternatives are to changes in the importance of the criteria, players, or environmental scenarios. Figure 16 shows a “gradient sensitivity” of the alternative priorities with respect to changes in the importance of the Cost criterion. The vertical dashed line shows that the current priority of cost is a little greater than 0.50. The height of the intersection of this dashed line with the alternative lines determines the alternatives’ priorities, if the importance of the cost criterion remains unchanged. Thus, The Mall is the preferred alternative. If cost were to become more important (i.e., the dashed vertical line moved to the right), the overall preference for The Mall would decrease, while those of the other two alternatives would increase. If the priority of cost were to increase above 0.59, then The Suburban Center would be the preferred alternative.

![](/api/attachments/XD9MJ9AH/fulltext/images/6996317751a180a22e8b86c9d9a4cc28be13faebae994b45405411c1c2908777.jpg)  
Fig. 17. Dynamic Sensitivity Analysis.

Another way to see this is with a dynamic sensitivity analysis. Figure 17 shows both the criteria importance (on the left) and the alternative priorities (on the right). Using a dynamic sensitivity analysis, the length of any criterion can be lengthened or shortened (making the criterion more or less important) to see what effect that would have on the priorities of the alternatives. The importance of the other criteria are also changed in direct proportion to their current values.

![](/api/attachments/XD9MJ9AH/fulltext/images/5c22ea504f7b8c6b06c52537d2adc91482e351059b9ce8e8e8da28a26c4b104a.jpg)  
Fig. 18. Increasing the Importance of Cost.

After the length of the Cost criterion is lengthened significantly, The Suburban Center becomes the preferred alternative, as seen in Figure 18.

The corresponding change to the gradient sensitivity analysis plot is shown in Figure 19.

A third sensitivity analysis available with the Expert Choice implementation of AHP, called a performance sensitivity, is shown in Figure 20 and depicts how well each alternative performs on each criterion. In essence, this analysis displays for each alternative the unweighted components that make up the overall priority as well as the overall alternative priority given the criteria weightings currently in effect.

![](/api/attachments/XD9MJ9AH/fulltext/images/1109ad8d1344e12ce9d97e3b44811dc1896ce1d3855fcd6d933d41ae9fa72113.jpg)  
Fig. 19. Importance of Cost Increased.

![](/api/attachments/XD9MJ9AH/fulltext/images/ae9ad0639afb7a23005fd22ace0a476a13588998770153f5e146d79da938564f.jpg)  
Fig. 20. Performance Sensitivity Analysis.

The overall priorities in Figure 20 reflect the increased importance given to Cost a moment ago. We can see from Figure 20 that The Mall location is least preferred with respect to Cost. Thus if we decreased the importance of the Cost criterion (to its original value), we would expect The Mall alternative to become most preferable. This is precisely what happens to the overall priorities as can be seen in Figure 21. (Notice that the component priorities do not change, just the overall priorities.) We can also see that the Main St. alternative does not perform best on any criterion and, in fact, is completely dominated by the Suburban Center alternative on every criterion.

![](/api/attachments/XD9MJ9AH/fulltext/images/350ad4526c85808950213ee0701c4f22854156c8abdb5a65d05150521ffbad9f.jpg)  
Fig. 21. After Decreasing Cost to Original Importance.

## Step 5 - Iteration

Decision making is a process as opposed to an event; a process that requires iteration. Iteration might be required when – during the choice phase – the group discovers that viable and possibly attractive alternatives were not identified during the design phase of the decision process. Or perhaps, someone in the group recognizes that the decision being addressed should be reformulated; or that a more important decision should be addressed first. Insights gained during a sensitivity analysis often suggest that part of the decision analysis be revisited, more information be collected, or additional criteria be considered.

Finally, and perhaps most importantly, the tentative solution to the decision should always be checked against human intuition. If one or more group members intuitively feel that the analytic solution is not the best, the reason or reasons should be delineated. For example, someone might argue that the alternative that ranked second in the analysis is intuitively the best, and will give one or more reasons or factors that support the argument. If these reasons or factors were already in the model, the judgments, and information relative to the judgements should be examined to see if they are reasonable. If some judgments are not reasonable, they should be changed, or more information should be sought before the decision is made.

If all the reasons or factors were not included in the model, the model should be revised to include them, and an iteration should be performed with the revised model to see if the results are any different. Usually after just one or two iterations, intuition and the model results will agree. The agreement may occur because the model's results have changed to agree with the original intuitive conclusion, in which case the model's primary value is in increased confidence and ability to justify the decision, or the insights gained by the analysis may have resulted in learning, which alters intuition, and avoids making a "poor" intuitive decision. Decision analytic methods are usually thought of as left-brained or analytic approaches as opposed to right-brained or intuitive approaches to problem solving. The Analytic Hierarchy process bridges the left brained – right brained dichotomy by accommodating both analytical and intuitive thinking in model construction, evaluation, and iteration.

## References

[1] J. Aczel and T.L. Saaty, Procedures for Synthesizing Ratio Judgments, Journal of Mathematical Psychology 27 (1983) 93–102.

[2] M. Al-Awadi, The Use of the Analytical Hierarchy Process in Conflict Analysis: Application to The Iraq–Iran War, Ph.D. dissertation (George Washington University, School of Government and Business Administration, Washington, DC, 1989).

[3] J.F. Bard and S.F. Sousk, A Tradeoff Analysis for Rough Terrain Cargo Handlers Using the AHP: An Example of Group Decision Making, IEEE Transactions on Engineering Management 37, No 3 (Aug 1990) 222–227.

[4] C.W. Churchman and H.B. Eisenberg, Chapter 3: Deliberation and Judgment, in: M.W. Shelly II and G.L. Bryan, Eds.), Human Judgments and Optimality, (Wiley, New York, 1969).

[5] G. DeSanctis and R.B. Gallupe, Group Decision Support Systems: A New Frontier, Data Base (Winter 1985) 3.

[6] G. DeSanctis and R.B. Gallupe, A Foundation for the Study of Group Decision Support Systems, Management Science 33, No. 5 (1987) 589–605.

[7] R.F. Dyer and E.H. Forman, AHP as a Tool for Selecting or Combining Forecasts, Proceedings of the International Conference on Forecasting, (Paris, 1986).

[8] B. Aubrey Fisher, Small Group Decision Making (McGraw-Hill, New York, 1980).

[9] Roger Fisher and W. Ury, Getting to YES (Penguin Books, London, 1983).

[10] E.H. Forman, Decision Support for Executive Decision Makers, Information Strategy: The Executive's Journal 1 (1985).

[11] E.H. Forman, T.L. Saaty, M.A. Selly, R. Waldron, Expert Choice, (Decision Support Software, McLean, VA, 1983).

[12] B.L. Golden and Q. Wang, 1989. An Alternate Measure of Consistency. in: B. Golden, E. Wasil and P.T. Harker, Eds., The Analytic Hierarchy Process: Applications and Studies (Springer-Verlag, New York, 1989).

[13] B.L. Golden, E.A. Wasil and P.T. Harker, Eds, The Analytic Hierarchy Process: Applications and Studies. (Springer-Verlag, New York, 1989).

[14] B.L. Golden, E.A. Wasil and D.E. Levy, Applications of the Analytic Hierarchy Process: A Categorized Annotated Bibliography, in: B. Golden, E. Wasil and P.T. Harker, Eds., (Springer-Verlag, New York, 1989).

[15] P.T. Harker, 1987. Alternative Modes of Questioning in the Analytic Hierarchy Process, Mathematical Modelling 9, No 3-5 (1987) 355.

[16] P.T. Harker and L.G. Vargas, Theory of Ratio Scale Estimation: Saaty's Analytic Hierarchy Process, Management Science 33 (1987) 1383–1403.

[17] R. Hogarth, Judgment and Choice. (Wiley, New York, 1987).

[18] I.L. Janis, Crucial Decisions - Leadership in Policymaking and Crisis Management (The Free Press, New York, 1989).

[19] E.F. Lane and W.A. Verdini, A Consistency test for AHP Decision Makers, Decision Sciences 20 (1989).

[20] C. Larreche and D. Montgomery, A Framework for the Comparison of Marketing Models: A Delphi Study, Journal of Marketing Research (Nov 1977) 487–498.

[21] B. Liu and S. Xu. Development of the Theory and Methodology of the Analytic Hierarchy Process and its Application in China, Mathematical Modelling 9, No. 3-5 (1987) 179-184.

[22] K.H. Mitchell and E.A. Wasil, AHP in Practice: Applications and Observations from a Management Consulting Perspective, in: B. Golden, E. Wasil and P.T. Harker, Eds., The Analytic Hierarchy Process: Applications and Studies (Springer-Verlag, New York, 1989.

[23] J.F. Nunamaker, L.M. Applegate and B.R. Konsynski, Computer-Aided Deliberation: Model Management and Group Decision Support, Operations Research 36, No. 6 (1988) 826–848.

[24] T.L. Saaty, The Analytic Hierarchy Process (McGraw Hill, New York, 1980).

[25] T.L. Saaty, Decision Making for Leaders (Lifetime

Learning Publications divisions, Wadsworth, Belmont, CA, 1982).

[26] T.L. Saaty, Group Decision Making and the AHP in: B. Golden, E. Wasil and P.T. Harker, Eds., The Analytic Hierarchy Process: Applications and Studies Springer-Verlag, New York, 1989).

[27] T.L. Saaty and J.M. Alexander, Conflict Resolution (Praeger, New York, 1989).

[28] H.A. Simon, The New Science of Management Decision (Harper and Brothers, New York, 1960) 40–43.

[29] E. Turban, Decision Support and Expert Systems: Managerial Perspectives (Macmillan, New York, 1988) 95–99.

[30] R.G. Vachnadze and N.I. Markozashvili, Some Applications of the Analytic Hierarchy Process (In the Soviet Union), Mathematical Modeling, 9, No. 3–5 (1987) 185–191.

[31] D. Von Winterfeldt and W. Edwards, Decision Analysis and Behavioral Research. (Cambridge University Press, New York, 1986) 387.

[32] V.H. Vroom and P.W. Yetton, Leadership and Decision-Making (University of Pittsburgh Press, Pittsburgh, PA, 1973).

[33] F. Zahedi, The Analytic Hierarchy Process - A Survey of the Method and its Applications, Interfaces 16 (1986) 96-108.
