---
otero_id: 20951
otero_key: "Y8PJV42B"
title: "The Greta system: organizational politics introduced to the garbage can"
authors: "G.Michael McGrath; Elizabeth More"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00130-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Greta system: organizational politics introduced to the garbage can

G. Michael McGrath<sup>)</sup>, Elizabeth More

DiÕision of ICS, Macquarie UniÕersity, North Ryde, 2109 Sydney, Australia

## Abstract

A decision-making model, in the tradition of the ‘garbage can’ and its variants, is introduced. The model also draws heavily on concepts drawn from research into the power-political model of organizational decision making. In particular, the critical dependencies at the core of the power-political model drive an organizational communications network. This network, in turn, is the principal determinant of the outcomes of political activity. The objective is to extend previous explications of the garbage can by putting some real substance into the problems, decision alternatives and actions facing problem solvers. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Decision models; Garbage cans; Power and politics; Simulation

## 1. Introduction

Decision-making is far removed from the coolly logical appraisal and selection of alternatives. Rather, it is at the centre of political machinations and intrigue, the true nature of which is not always fully recognized, even by those involved ŽRef. 18 : p. 298 .<sup>w</sup> <sup>x</sup> .

A current revival of interest in organizational and managerial decision making goes hand-in-hand with the growing concern with managing complexity, ambiguity, accelerating competition, and rapid globalisation. It also coincides with renewed vigour in organization studies, with the increasing acceptance of alternate paradigms and frames for viewing organizational life, just at a time when computing technology itself can provide enormous assistance in clarifying diverse and innovative approaches to grappling with the increasingly difficult phenomenon of organizing and organizations into the twenty-first century.

An excellent example of this is the recent, renewed interest in the use of computational simulations in the investigation of organizational phenomena. As Prietula et al. 23,24 have noted, such<sup>w</sup> <sup>x</sup> simulations have the potential to assist practising managers considerably in many important tasks, including i organizational analysis, design andŽ . reengineering; ii assessing the potential impacts of Ž . new technologies; iii investigating whether non-lin- Ž . earities in system behaviour occur as scope conditions are extended i.e., whether systems ‘scale up’ Ž effectively ; and iv the exploration of dynamic. Ž . processes and configurations that are difficult or impossible to investigate with other methods.

Here, we introduce a model of organizational decision making and its implementation as the computer system, Greta. Our work draws heavily on the garbage can decision-making model, first presented by Cohen, March and Olsen CMO in the earlyŽ . 1970s 4 and investigated and extended by many<sup>w</sup> <sup>x</sup> other organization and management theory researchers since that time. The distinguishing feature of our variant is that we focus on organizational power and politics 21,22 , with the motive of putting<sup>w</sup> <sup>x</sup> some real substance into the problems, decision alternatives and actions facing the actors within our system as well as its users . The garbage can was Ž . originally designed for organized anarchies 3 and<sup>w</sup> <sup>x</sup> we recognise that some may view this decision-making model and the power-political model as being mutually exclusive. However, because of what we see as major overlaps between the two models, we consider our variant to be a natural extension of the garbage can and argue the case for this in theŽ following section ..

In the short-term, we see Greta being used mainly Ž . in management games mode as a pedagogical aid. In the medium-term, we aim to utilise it to investigate various organizational phenomena particularlyŽ in the areas above . Note, however, that we believe. our system might be used to best effect if employed in combination with other decision support aids— specifically, computational tools designed to support systems dynamics modelling 30 and social network<sup>w</sup> <sup>x</sup> analysis 34 .<sup>w</sup> <sup>x</sup>

In Section 2, we provide some theoretical background on managerial and organizational decision making and then, in Section 3, we introduce the garbage can model, our particular variant and our computerised implementation, Greta. In Section 4, we present an example, in the form of the retro-Ž spective application of our model and system to an . actual change management exercise, reported originally by McGrath et al. 17 . Section 5 contains<sup>w</sup> <sup>x</sup> concluding comments.

## 2. Organizational decision making: background

Garvin 8 , in a recent article, provides a unifying<sup>w</sup> <sup>x</sup> framework for thinking about the processes that constitute the reality of organizations and managerial behaviour. He focuses on dividing his task into three approaches—work processes, behavioural process, and change processes—and ties these together as interconnected sets. Among these, the cognitive and interpersonal aspects of work characterise behavioural processes and it is within this approach that we can clearly locate concerns about decision making, an area that has been well attended by numerous scholars. Among these, many perceive decision making as a solitary management exercise but importantly, others emphasise that it can and often actually does involve many individuals across an organization.

Morgan 19 delineates the early work of Simon<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 26 on decision-making in terms of understanding organizations through the brain metaphor with ‘organizations as kinds of institutionalized brains that fragment, routinize, and bound the decisionmaking process to make it manageable’ Ref. 26 : p. Ž <sup>w</sup> <sup>x</sup> 79 . Studies of decision making have ranged across a . wide array of disciplines, paradigms, theoretical perspectives and methodologies in organization studies, often eliciting conflicting approaches to central tenets of rationality, coping with uncertainty and complexity, and, to varying degrees, have attempted to uncover the real issues of power and organizational politics involved in the process. The traditional emphasis on management concern with rational decision making for the effective organization exists within the still dominant theoretical paradigm of structural functionalism 18 .

More recent writers have followed Simon’s partner, March 12 , in exploring alternatives to the<sup>w</sup> <sup>x</sup> assumptions of rationality in decision making and the nature of the process in increasingly uncertain times. Not surprisingly today, many have invoked concepts of emotion and intuition 1,6 . Others have adopted a pluralist position. They have focused on the struggle for political action, conflict, negotiating, bargaining, suppression, and the pursuit of supremacy and power in decision-making processes. In addition, they have highlighted non-decisions, expertise, access to information, agenda setting and participation in decision making as critical issues for consideration 18 .<sup>w</sup> <sup>x</sup>

Garvin 8 suggests that past research on decision<sup>w</sup> <sup>x</sup> making has led scholars to accept the multilevel nature of decision-making processes—simplicity giving way to attempts to grapple with the complexity and richness of the process itself; and to acknowledge how managers themselves are responsible for shaping and influencing decision processes. Furthermore, examples such as the Bay of Pigs 9 , under-<sup>w</sup> <sup>x</sup> lines the collective nature of decision-making processes and the need for conflict and diverse perspectives being involved in the process. As he puts it: ‘ . . . decision-making processes are lengthy, complex, and slow to change. They involve multiple, often overlapping stages, engage large numbers of people at diverse levels, suffer from predictable biases and perceptual filters, and are shaped by the administrative, structural, and strategic context’ Ref.Ž <sup>w</sup> <sup>x</sup> 9 : p. 38 . Cooksey 5 , as if echoing this, within his. <sup>w</sup> <sup>x</sup> ‘complex dynamic decision perspective’, identifies over 100 factors that can have an impact on the decision process and that current decision support systems based as they are on a restricted range ofŽ research paradigms and perspectives are overly sim-. plistic and exclude much important contextual detail.

Given this, alongside the growing interest in linking chaos theory to the complexities of organizational life, it is little wonder then that this seems to have prompted renewed interest in the perceptive garbage can model of decision making in organized anarachies of CMO 4 . In this model, there is clear<sup>w</sup> <sup>x</sup> recognition of real complexity and of the fact that many decisions are not based on simple, linear, rational processes. Proponents of the garbage can and many of its variants see, for example, Ref. 24 Ž  . argue that, despite the seeming irrationality that appears characteristic of much organizational activity, many sensible and reasonable decisions are made. Moreover, while chance plays some part in this, it is not the prime driver. That is, there is some kind of alternative logic that underpins this seemingly chaotic behaviour.

Warglien and Masuch 33 : p. 6 contend that it Ž<sup>w</sup> <sup>x</sup> . is ‘patterns of interaction’ that are at the core of this alternative logic. Thus, organization structure for- Ž mal and informal is a major driver of all variants of. the garbage can – from the original CMO model Žbased on numerical algorithms and implemented in Fortran to the more recent network learning model. of Warglien 32 represented and implemented using<sup>w</sup> <sup>x</sup> Ž advanced neural network technology . We do not .

deny the importance of the formal organization structure and take it into account in our model but seeŽ . organizational power, as a major determinant of the informal communication network. That is, power, derived from critical dependencies, will have a major impact on parties’ levels-of-access to each other and on the outcomes of political activity. Parties’ credibility will increase or decrease depending on these power play outcomes and these, in turn, will have a further impact on the communication network.

In contrast to many organizational decision making model classifications see, for example, Ref.Ž Ž <sup>w</sup> <sup>x</sup> 21 : pp. 18–33 , we do not view the organized . anarchy and power-political models as being separate and mutually exclusive. In fact, we see considerable overlap between the two models. In particular: Ž .i both models assume the absence of any overarching goal or, even if such a goal exists, decisions taken will not necessarily be consistent with the attainment of that goal; ii the organized anarchy Ž . model assumes unclear technology and processes, while the power-political model assumes widely differing views on technology and processes often Ž leading to ambiguity and confusion—i.e., a lack of clarity ; and iii fluid participation in decision mak-. Ž . ing is characteristic of both models. Fluid participation, in turn, is largely driven by the communication network and the power source distribution within an organization is a major determinant of the informal communication network.

The key feature that distinguishes the two models is intention: specifically, in organized anarchies, events are not dominated by intention while, in power-political situations, actors do have preferences Žwhich are liable to be pluralistic, inconsistent and, oftentimes, very different from stated organization goals . However, even here the distinction is not as . clear-cut as might at first appear. That is, preferences in a power-political environment do often change substantially over time, stated preferences are frequently rationalised after decisions have been made and, regardless of preferences, chance is also a determinant of the outcomes of political activity as it is Ž in organized anarchies ..

Thus, we see our approach of embedding specific power-political decision making detail within a garbage can framework as a quite legitimate perspective to take. In essence, the power-political component infuses both content and context into the garbage can, thereby enriching it. We see the major test of our model as its usefulness in the pedagogical and decision modelling and analysis spheres referred to earlier. We trust the reader might gain a better understanding of these potential uses after having read the description of our model and its implementation, plus the example of its application, presented in the following two sections. Table 1 compares the essential elements of our approach with the original CMO model and the more recent contribution of Masuch and LaPotin 14 .<sup>w</sup> <sup>x</sup>

Table 1  
Greta compared with the CMO and Masuch<sup>r</sup>LaPotin model

<table><tr><td></td><td>CMO</td><td>Masuch and LaPotin</td><td>Greta</td></tr><tr><td colspan="4">Underlying theory</td></tr><tr><td>Rational choice</td><td>N</td><td>N</td><td>N</td></tr><tr><td>Organized anarchies</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>Power-political</td><td>N</td><td>N</td><td>Y</td></tr><tr><td colspan="4">Conceptual model</td></tr><tr><td>Stochastic</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>Symbolic</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td>Declarative</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td>Granularity</td><td>Coarse</td><td>Medium</td><td>Fine</td></tr><tr><td>Decision complexity</td><td>N/A</td><td>Low</td><td>High</td></tr><tr><td colspan="4">Implementation</td></tr><tr><td>Procedural language</td><td>Y</td><td>Y</td><td>N</td></tr><tr><td>Objects/frames</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td>Rules</td><td>N</td><td>Y</td><td>Y</td></tr></table>

## 3. Greta: a brief introduction

## 3.1. Garbage cans

In the classic, rational decision-making tradition <sup>w</sup> <sup>x</sup> 29 : i decision alternatives, constraints and conse- Ž . quences are known; ii consequences are evaluated Ž . in terms of well-defined objectives; and iii the bestŽ . alternative is established and chosen. As discussed in the previous section, much organizational decision making does not conform to this neat logical view, founded as it is in economics theory. Thus, over the years our view of the rational organization has been gradually eroded. However, as Warglien and Masuch <sup>w</sup> <sup>x</sup> 33 have noted, it is important to distinguish between organizational anarchy and organized anarchy. The former term is used to describe an organization in chaos while the latter term recognises that, despite the seeming irrationality and confusion present in many organizations, these are often underpinned by order and intelligence—or, as they describe it, an alternative ‘underlying behavioral logic’ Ref. 2 : p.Ž <sup>w</sup> <sup>x</sup> 3 . CMO’s garbage can model represents one of the. more influential attempts to define such an alternative decision-making logic. They view:

. . . a choice opportunity as a garbage can into which various kinds of problems and solutions are dumped by participants as they are generated. The mix of garbage in a single can depends on the mix of cans available, on the labels attached to the alternative cans, on what garbage is currently being produced, and on the speed with which garbage is collected and removed from the scene ŽRef. 2 : p. 2 .<sup>w</sup> <sup>x</sup> .

Thus, from this perspective, an organization can be viewed as largely independent streams of choice opportunities looking for problems, problems looking for decision situations, solutions looking for problems to which they might attach themselves and decision makers looking for or avoiding work.Ž . Decisions, made when elements of all four streams come together, are of three styles: i resolution, Ž . where a problem is worked through until it is solved Žthe style which most closely matches rational choice decision-making methods ; ii oversight, where de-. Ž . cisions that do not really address any problem are made; and iii flight, where persistent, unsolved Ž . problems move from one decision-making arena Ž . garbage can to a new, more attractive choice opportunity another garbage can . Solutions are only re-Ž . ally effective when the first of these styles resolu- Ž tion is employed..

CMO implemented their model as a Fortran computer program and used it to simulate and analyse some interesting properties of emergent decisionmaking processes 4 . Their work aroused a great <sup>w</sup> <sup>x</sup> deal of interest and a number of extensions to the garbage can were modelled and implemented through the remainder of the 1970s and 1980s. Warglien and

Masuch 33 : pp. 18–23 present a summary of the Ž<sup>w</sup> <sup>x</sup> . more significant of these developments and note that all models share a decision making strategy based principally on numerical algorithms. In order to extend the simulation capabilities of the garbage can and to overcome problems experienced with numerically based models including a lack of model clarityŽ and transparency, and the application of many simplifying assumptions , Masuch and LaPotin 14. <sup>w</sup> <sup>x</sup> adopted a modelling approach based on artificial intelligence AI techniques. Their implementation Ž . represents a significant advance, as it allows the explicit and largely declarative representation of Ž . organization structures, issues and problems, actors attributes and feasible decision alternatives.

Here, we present further extensions to the garbage can model in an effort to improve its utility as an analysis tool and as a decision making and pedagogical aid. We focus particularly on problem content and action alternatives, and do so within a powerpolitical framework. We employ much of the original CMO model and our use of AI techniques is very much in the tradition of Masuch and LaPotin 14 .<sup>w</sup> <sup>x</sup> We also draw heavily on the particular interpretation and representation of organizational power presented by Pfeffer 21,22 . Our choice of model focus was informed by what we perceived to be a lack of any real ‘meat’ in the problems and decision alternatives used to explicate previous representations of the garbage can and its variants.

## 3.2. Our extension to the garbage can

As noted above, the CMO model employs numerical algorithms to simulate decision-makers and their actions. As a result, these are only represented implicitly in their model. Furthermore, an ‘additive energy’ and further simplifying assumptions, related to problem solvers’ capabilities and the allocation of problems to choices, mean that decisions are made when an organization musters enough collectiveŽ . energy to remove a problem from the scene—‘ . . . not unlike the interaction of supply and demand in the marketplace’ 14 : p. 42 . Most real-world problemsŽ<sup>w</sup> <sup>x</sup> . do not present decision-makers with a continuous problem space and, instead, require symbolic data structures, inference, search strategies and pattern matching.

To address these limitations, Masuch and LaPotin <sup>w</sup> <sup>x</sup> 14 endow their actors with various attributes—including: bounded rationality where decisions areŽ ‘satisfied’ rather than optimised ; aspiration levels. Ž . determined by prior experience ; basic skills; motivation; and commitment to other actors and theŽ organization . However, problems are either not rep-. resented explicitly as in the CMO numerical mod-Ž elling tradition or are very routine and more suited. to bureaucratic methods. For example, Masuch and LaPotin represent problems as issues but the only concrete instance they quote is memo preparation, involving the skill set draft, type, edit, approve —  4 activities that hardly display the uncertainty, problematic preferences, unclear technology and fluid participation characteristic of organized anarchies.

What does display this better is the issue of diverse change situations and dynamics that determine the nature of decision-making processes managers are able to utilise. As Stacey 28 suggests, the <sup>w</sup> <sup>x</sup> closed and contained change situations that exist in equilibrium systems are a far cry indeed from openended change of real uncertainty and ambiguity. For him:

. . . the characteristics of open-ended change make it impossible to apply rational, orderly decisionmaking techniques that rely on some ability to foresee the consequences of present actions. We must expect something messier and more opportunistic, involving political interaction and learning in groups 28 : p. 72 .Ž<sup>w</sup> <sup>x</sup> .

Thus, a distinguishing feature of our approach is that users of our implemented system play the part of change agents and are faced with a non-trivial problem, which they must resolve by choosing appropriate tactics to deal with power-political issues associated with the problem. An entity-relationship representation somewhat simplified of our model isŽ . presented in Fig. 1. Many tactics can be associated with a single problem. During each simulated pe-Ž . riod, a selected tactic is invoked by the user. Parties may be involved in issues arising from many tactics and the one tactic may involve many parties, as indicated by the party–tactic involvement pti rela-Ž . tionship. Note that there is an indirect link from pti back to selected tactic, so that all parties involved in the resolution of a specific tactic may be derived. A selected tactic may succeed or fail the outcome .Ž . The result depends partly on chance but also on both the level-of-access that parties have to each other and on the general attitude to the tactic derived fromŽ attributes of pti entities . Level-of-access LOA is. Ž . an attribute of the party–party involvement ppi Ž . relationship the value of each involvement being determined largely by: i an initial value; and iiŽ . Ž . tactic outcomes, linked to loa-variants and attitudevariants, which are, in turn, applied to ppi and pti relationships at the completion of each simulated period an attribute of selected-tactic . Finally, noteŽ . that the party–role involvement pri relationshipŽ . indicates that each party may play a number of roles Ž . i.e., occupy a number of organization positions during the course of a simulation.

![](/api/attachments/Y8PJV42B/fulltext/images/d512dfc6d106f12e592ff79983e03021a52268e20a102644508936258bfeedc7.jpg)  
Fig. 1. Greta—conceptual data model.

A process-oriented view of our approach is presented in Fig. 2. Essentially, the Change Agent’s aim should be to raise his or her mean access level to a point where a selected tactic is likely to succeed. When this occurs, access levels will generally increase and the converse also applies. Failure to get the necessary parties together following a tactic selection will also result in a decrease in change agent access levels. During the simulation, users may retrieve the latest details on access levels and attitudesŽ to tactics . As a general rule, selection of a tactic.

where access levels are low is not recommended. However, as noted by Cohen 2 , there are circum- <sup>w</sup> <sup>x</sup> stances where rewards are extremely high where aŽ . decision maker may be justified in taking significant risks of this sort. Ways in which users’ performance may be assessed are discussed is Section 4. In general, high level-of-access values and tactic success rates indicate that a sound change management strategy has been employed.

## 3.3. The communication network

Once a tactic is selected, the probability that involved parties will actually meet to resolve the issues raised depends principally on the strength of ties between the involved parties levels-of-access Ž . and the number of parties involved.

Communication between parties can, of course, be both formal and informal. Formal communication is based on lines of command, as exhibited in our case study organization structure see Fig. 4 . TheŽ . level of informal access that party x has to party y depends mainly on xs credibility with y. Credibility, in turn, is based on ys interpretation of previous encounters with x and dependencies derived from power sources: notably, provision of resources, which can include funds, equipment, information expert knowledge, as well as prestige, personal attributes, rewards and sanctions, empathy and friendship.

![](/api/attachments/Y8PJV42B/fulltext/images/d2fb883fa1349e2c380e9edf0e055eaee9519f0c6e986f9c685cae1d869eea44.jpg)  
Fig. 2. Greta—a process view.

An initial, informal tie strength, InfAxs , must <sub>x y</sub> be declared for each pair of parties in both direc-Ž tions . The scale used is 0–1, a strong tie is 0.8, an . average tie is 0.6 and a weak tie is 0.4. Initial assignments will vary from case to case and, for the most part, these will be consistent with power dependency relationships. Note, however, that exceptions must be made from time to time. For example, in the case study discussed in the following section, party 1 Ž . the change agent has very weak access to party 4 Ž . Ž . the GM operations , and very weak mutual links have been specified between the billing and service orders project managers parties 7 and 8 . Finally,Ž . note that specified, informal ties are between parties and not positions roles .Ž .

During any time period, t, the level-of-access Ž . informal is simply the average of the values of the ties between parties occupying positions involved in the issue under consideration. Thus:

$$
\operatorname{LoaInf} _ {t} = \left[ \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \operatorname{InfAxs} _ {i j} / P _ {2} ^ {n} \right] t
$$

where $P _ { 2 } ^ { n }$ is the total number of ties.

The informal access level is calculated at the beginning of each simulated period and stored in the current loa inf slot of the tactic frame. Demons and<sub>– –</sub> rules are attached to this slot, such that each time the slot is updated these will be automatically invoked in order to factor in the impact of: i the formalŽ . communication network; and ii the number of posi- Ž . tions involved.

We account for formal communication network effects in a relatively unsophisticated way. Our basic assumption is that, if senior executives are involved in issue resolution, then the likelihood of other parties participating will increase. Hence, the level-ofaccess formal and informal at timeŽ . t is specified as:

$$
\operatorname{Loa} _ {t} = \operatorname{LoaInf} _ {t} + (1 - \operatorname{LoaInf} _ {t}) (L - \max (L)) / L
$$

where L is the maximum number of levels in the organizational hierarchy and maxŽ . L is the highest level that has a position involved in resolution of Ž . the current issue. The rule-based and data-driven programming approaches that underpin our application architecture greatly facilitate future extensions to cope with more complex access strategies.

While, up to a certain point, a group’s problem solving ability improves with increased size 25 , a key moderating variable is the degree of difficulty involved in getting large numbers of people together. Thus, the level of access varies inversely with size. Specifically, our revised level-of-access, Loa , for a <sub>t</sub> given tactic selection:

v is 1 100% when only one party is involved; Ž .

v is increased by 1Ž . <sup>y</sup> Loa .0.5 where two to three parties are involved;

v is unchanged where four to five parties are involved; and

v is decreased by 10% where six or more parties are involved.

## 3.3.1. Greta architecture

The architecture of our system is illustrated in Fig. 3. As indicated in the meta-model at the left of the diagram, Greta consists of generic and casespecific components. The generic component was derived from the garbage can literature and can be applied to any area of organizational life where the concepts that underpin this model appear to be both relevant and useful. Specific applications within these areas represent cases and, for each case, Greta must be customised with concepts and facts taken from the domain and specific problem under investiga- Ž . tion. To a large extent, this involves specifying: iŽ . access levels between parties; ii parties’ attitudes to Ž . tactics; and iii details of actions to be taken whenŽ . specific tactics succeed or fail.

The software platform we have employed for our prototype implementation is the Flex expert system shell 11 . This has allowed us to take advantage of<sup>w</sup> <sup>x</sup> object-oriented concepts and techniques, as well as declarative, non-deterministic, rule-based programming. Part of our object hierarchy is displayed in Fig. 3. At the top, we see party, tactic, ppi party– Ž party involvement and party–tactic involvement pti . Ž . represented as objects or object classes while, be-Ž . low the dotted line, case-specific details are represented as instances of these objects. Here, we have chosen to use p1, p2 and t1 to identify two of our parties and one tactic, but we could just as easily have utilised actual party and tactic names e.g.,Ž John Smith and Form a coalition . One advantage of. generic identifiers is that they aid reusability – even at the case-specific level. Note also that the genericlevel object hierarchy is mirrored many times overŽ . at the instance level.

![](/api/attachments/Y8PJV42B/fulltext/images/6f694590406c058d7145abedb85c0de99d26765ca8524e1616cebb3a82233adb.jpg)  
Fig. 3. Greta—system architecture.

One significant benefit of our software platform is that it has enabled us to make extensive use of data-driven programming. That is, rather than having to program complex control flows, we can attach demons to objects as well as to their instances andŽ attributes and then specify the conditions under. which they should be activated. Demons are represented as rules. An example of a generic rule is:

demon tactic 01

when the result of selected tactic changes then update relevant ppis with loa variants<sub>– –</sub> and update relevant ptis with attitude variants. <sub>– –</sub>

and an example of a case-specific rule is:

demon tactic 3 01<sub>– –</sub>

when the result of t3 changes to success then replace ‘GMF’ with ‘CIO’ in the roles of p5

and replace ‘CIO’ with ‘GMF’ in the roles of p6.

The former rule is attached to the selected-tactic object and specifies that, once the result of a tactic invocation is known, then the relevant party–party and party–tactic involvements are to be updated with the appropriate access level and attitude variants, respectively. While the actual values for these variants are definitely case-specific and must be prespecified, the rule itself remains unchanged regardless of case. The latter rule, however, is designed specifically for the case discussed in the following section and, in essence, specifies that if tactic, t3, succeeds then parties, p5 and p6, are to swap positions see the discussion under Tactic 3 in Section Ž 4.2 for more detail ..

Obviously, we have designed our system in this way so that we can minimise the amount of rework necessary as we move from domain to domain andŽ to specific cases within each domain . The bulk of. the Greta code resides within the generic component but this is not to say that customisation is a trivial exercise. In particular, determining and loading initial access level and attitude values is a time-consuming exercise. However, these values can be quite conveniently set up within Excel spreadsheets and we have developed a small module that allows a user to automatically initialise Greta object instance slots Ž . attributes from these pre-formatted spreadsheets.

## 4. Example: a change management exercise

## 4.1. Background

Our example is derived from earlier research into a major strategic information systems planning SISPŽ . study undertaken at a large Australian company within the utilities sector which we shall call Gi- Ž gante . This earlier work looked at the development . and implementation of a corporate-wide information systems strategy from a power-political perspective. Accounts of this largely unsuccessful and expen- Ž sive exercise have been reported in Refs. 15,17 .. <sup>w</sup> <sup>x</sup>

Historically, within Gigante, information systems were sponsored and ‘owned’ by functional areas. Ž . Almost inevitably, this led to a situation where there were major inconsistencies between the data of different systems and considerable data redundancy 13 . <sup>w</sup> <sup>x</sup> In addition, Gigante’s core systems had been developed using a variety of DBMS platforms. The net result was an inflexible IT architecture, considerable waste, excessive costs and perhaps, most importantly, managers did not trust their systems sufficiently to utilise them when making major decisions. Consequently, the SISP study team’s central recommendation was that Gigante’s existing, fragmented set of systems should be migrated to a data-centred, integrated IS environment, underpinned by standard application and processing architectures. One of the highest priority projects identified within the strategy was the replacement of the existing service orders Ž . SO and billing systems with a single customer support system CSS .Ž .

The relevant portion of Gigante’s organization chart is illustrated in Fig. 4. Further detail on positions identified in the chart and involved parties is presented in Section 4.2, but here we note that the change agent position was established as the direct result of the SISP exercise and the occupant was made responsible for facilitating the implementation of strategy recommendations and projects. Importantly, although the change agent reported directly to the chief executive officer CEO , the position hadŽ . no direct line control over any of the other positions within the structure. Note also, the dotted lines from the general manager operations GMO and the gen- Ž . eral manager finance GMF to the SO and billing Ž . project managers respectively. These indicate that, while all technical systems’ activity was undertaken within the information systems department headedŽ by the chief information officer—CIO , system own-. ers the GMO and GMF were responsible for allŽ . major system decisions—e.g., those relating to funding levels and the establishment of maintenance and enhancement priorities. The third GM, the general manager marketing GMM owned no major, corpo-Ž . rate systems. Finally, Gigante had a transfer pricing system in place and stakeholdings in core systems Žthrough ownership, development, maintenance and processing responsibilities and activities were used. to generate substantial levels of internal funds. Consequently, most stakeholders tended to respond less than enthusiastically to suggestions that their systems should be eliminated or replaced. Naturally, this did not make the change agent’s job any easier.

## 4.2. The exercise

Users, interacting with Greta, take the part of the change agent and their task is to successfully implement the new CSS system. At the beginning of each simulation cycle, they are presented with the menu displayed in Fig. 5 and asked to select a tactic. Greta then calculates: i the overall level of access LoaŽ . Ž . for all parties involved in resolution of problems generated by invocation of the selected tactic; and Ž . ii $P _ { t } ,$ the probability that the selected tactic will succeed. Processes, based on random number generation are then employed in conjunction with Loa Ž and $P _ { t } )$ to determine whether the necessary choice opportunities do, in fact, eventuate and, if so, whether the selected tactic succeeds or fails.

![](/api/attachments/Y8PJV42B/fulltext/images/a46c107bc803893ccd3205cb913441687fe77927edbf61315d6112b42ade9d84.jpg)  
Fig. 4. Gigante organization structure partial . Ž .

In selecting tactics, users have access to a variety of menu options that, when selected, provide details on current access levels, probabilities and attitudes to tactics. They may also interrogate a help system to obtain further details on tactics and parties, party– party relationships and other relevant information. The help window is also displayed in Fig. 5 and, to achieve a reasonable result, it is essential that the user is familiar with the following information.

## 4.2.1. Tactics 1 and 2: use of the media or a study

Here, the intention is to boost internal support for the CSS project through the media or by using

Ž . supposedly independent external consultants to conduct a study with terms of reference phrased inŽ such a way that a favourable outcome is almost assured Ref. 21 : pp. 142–146 . There are risksŽ <sup>w</sup> <sup>x</sup> . associated with these tactics: in particular, if support is at a low ebb or people feel that they are being manipulated, the situation may only worsen.

## 4.2.2. Tactic 3: CIO-GMF position swap

The GMF is highly supportive of both the broad strategy and the CSS project and has close ties with the change agent. She also believes that the IS function is not being handled well and would welcome the opportunity to try her hand at the CIO job. Serendipitously, the incumbent CIO would very much like a transfer to a general manager’s job in a functional area. Given that the CIO has to be involved whatever tactic is chosen, the change agent would dearly like to see the current GMF in the CIO’s chair. However, while the CEO is not entirely happy with his CIO’s performance, the GMO would certainly oppose a direct position swap. Given that the GMO has very good access to and influenceŽ with the CEO, any early move with this tactic. would likely fail. A couple of ‘ wins’ with other tactics would greatly improve the chances of success. Finally, the tradition within Gigante is to consult lower-level staff when significant personnel changes are under consideration.

![](/api/attachments/Y8PJV42B/fulltext/images/5595bb12695e8892ae2e3c97bed90307a900160839b5c1d1ba13c17148864bc4.jpg)  
Fig. 5. Greta—run time environment.

## 4.2.3. Tactic 4: migrate the serÕice orders system to Oracle

For CSS to be successfully implemented, the support of the IS department’s technical staff is essential. This applies particularly to the project managers, the most influential of these being the project manager of the service orders system the PM SO .Ž Ž .. However, her links with the GMO are very strong and, consequently, she has some sympathy with his view that the CSS proposal and, indeed, the whole Ž strategy are ill-conceived and doomed to failure.. The PM SO and her team, though, are very un- Ž . happy with the ancient technology used to support their system and, if handled in the right way, might welcome a move to the popular DBMS, Oracle.

Naturally, this would not entirely displease the CEO Ž . Oracle either—a regular golf partner of Gigante’s CEO.

## 4.2.4. Tactic 5: giÕe CSS to the PM SO( )

For this to have any chance of success, the change agent must both establish credibility with the PM Ž . SO and weaken the links between her and the GMO.

## 4.2.5. Tactic 6: giÕe billing ownership to the GMM

The GMM is very dependent on both the GMO and GMF—because she needs considerable information out of these systems to do her job something Ž she has done very effectively, earning her considerable kudos with the CEO . While she has occasion-. ally expressed some dissatisfaction with Gigante’s systems she has, to date, indicated no interest in taking on a more significant IS role. She has adopted a ‘wait and see’ approach to the strategy and CSS:

i.e., she has some sympathy with the organization’s new IS objectives, but suspects that Gigante’s notorious internal politics may strangle any major initiative.

## 4.2.6. Tactic 7: offer CSS ownership to the GMM See comments under Tactic 6 above.

## 4.2.7. Tactic 8: tie CSS to a new product release

Here, use is made of what Lindner 10 refers to<sup>w</sup> <sup>x</sup> as a ‘deadline-based change anchor’. Specifically, the change agent obtains agreement from the CEO that code to support an important new product release will be included in the CSS system. Since the product release date is firm, the organization is now committed to having a version of CSS in place by that date. The danger here is that even the strategy’s strongest supporters may feel that they are being manipulated and, consequently, the tactic could backfire i.e., the change agent’s access levels andŽ credibility could suffer even if CSS is successfully implemented ..

## 4.2.8. Tactic 9: promote the PM Billing ( )

The PM Billing is not particularly happy in hisŽ . current position and this is reflected in a fairly disinterested attitude to all IS issues. Both the GMF and the CIO would be more than happy to see him moved out of the way. As it happens, the manager research job is currently vacant. This job is not too demanding, the manager’s major function being to represent Gigante on the AIRC the Australian In-Ž dustry Research Council . This might appeal to the . PM Billing , however, as he is very status-conscious Ž . and would probably value mixing with senior industry and academic representatives. A further benefit of this ‘symbolic’ promotion Ref. 21 : pp. 215–219Ž <sup>w</sup> <sup>x</sup> . is that the technical leader of the billing system TLŽ

Ž .. Billing would almost certainly be promoted to fill the consequential vacancy. Whereas the current PM Ž . Ž . SO and PM Billing have been long-time antagonists, the TL Billing is a close ally of the PM SO .Ž . Ž .

## 4.2.9. Tactics 10 and 11: coalition formation

Coalition formation is an appropriate political tactic where lateral relationships are involved and where there is strong organization unit inter-dependence 7 . <sup>w</sup> <sup>x</sup> The change agent, the GMF, the CEO Oracle , andŽ . the GMM all have much to offer each other but it is probably unlikely that the GMM would wish to be too closely associated with the strategy and CSS in the early stages.

Parameters can be set so that the simulation runs for a fixed number of cycles or to cause termination when specified access levels and tactic attitude limits are breached. Performance may be assessed using final access levels particularly the change agent’s ,Ž . attitudes to tactics, the number of tactics that succeeded, and access attempts and tactic invocation success rates. It is essential, however, that some degree of caution is applied here as, the nature of the garbage can model is such, that even well-planned change management strategies may sometimes fail. We discuss this in more detail in the following section.

## 4.3. Sample results and discussion

Examples of three simulation trials are presented in Table 2. Tactic order is the order in which tactics were selected, the Final CA LOA is the change agent’s average level-of-access informal to all otherŽ . parties at the completion of the simulation while final attitude is the mean of the attitudes to all tactics Ž . again at completion of the simulation .

Table 2  
Sample results of simulation trials

<table><tr><td rowspan="2"></td><td colspan="3">Trial 1</td><td colspan="3">Trial 2</td><td colspan="3">Trial 3</td></tr><tr><td>Total</td><td>Success</td><td>Success (%)</td><td>Total</td><td>Success</td><td>Success (%)</td><td>Total</td><td>Success</td><td>Success (%)</td></tr><tr><td>Access attempts</td><td>11</td><td>11</td><td>100</td><td>15</td><td>7</td><td>46.7</td><td>25</td><td>15</td><td>60</td></tr><tr><td>Tactic invocations</td><td>11</td><td>11</td><td>100</td><td>7</td><td>1</td><td>14.3</td><td>15</td><td>4</td><td>26.7</td></tr><tr><td>Tactic order</td><td colspan="3">4, 9, 10, 5, 2, 3, 6, 11, 1, 7, 8</td><td colspan="3">3, 7, 6, 4, 9, 5, 8</td><td colspan="3">4, 9, 10, 5, 2, 3, 6, 11, 1, 7, 8</td></tr><tr><td>Final CA LOA</td><td colspan="3">0.82</td><td colspan="3">0.23</td><td colspan="3">0.38</td></tr><tr><td>Final attitude</td><td colspan="3">0.87</td><td colspan="3">0.02</td><td colspan="3">0.21</td></tr></table>

Pfeffer 22 : pp. 227–245 has emphasised that inŽ<sup>w</sup> <sup>x</sup> . organizational politics ‘timing is almost every-Ž . thing’. In trial 1, the order in which tactics were selected was close to optimal although, other combi-Ž nations can also yield very good results . The key to. success here is that the user has taken great care to establish credibility before employing tactics that are potentially high-return but also high-risk if the nec-Ž essary ground work has not been laid . Specifically,. the initial general attitude to tactic 4 migrating the Ž SO system to Oracle was very favourable and, thus, . had quite a reasonable chance of succeeding—in spite of the initial low change agent average levelof-access value 0.47 . When it did succeed, severalŽ . benefits ensued: i the change agent’s access to Ž . almost all parties improved; ii the influential CEOŽ . Ž . Oracle was particularly happy, as were the PM Ž . Ž SO and her team thus making them more amenable to any further initiatives involving them ; iii the. Ž . strengthening of the change agent’s link with the PM Ž . SO resulted in a corresponding weakening of the GMO–PM SO link; and iv once the remainder ofŽ . Ž . the organization saw that the change agent could deliver on a key initiative, the general attitude to all other tactics improved. Following up with tactic 9 Ž Ž . promotion of the PM Billing was also timely, as his replacement was closely allied to the PM SO .Ž . From there, quite a few other tactics had a reasonable chance of succeeding, although leaving all tactics involving the GMM until later was also an astute move.

In contrast, the order of tactic selection in trial 2 could hardly have been worse. Commencing with tactic 3 the CIO–GMF swap was ambitious enough,Ž . but the attempt to coopt the GMM tactics 6 and 7Ž . so early in the simulation meant that failure was almost inevitable. Essentially, with three failures from as many attempts, the change agent’s credibility had sunk so low that CSS and the wider ISŽ strategy was dead from that point on. Even when . one later tactic tactic 9 succeeded, this was dueŽ . more to sheer luck than anything else and the change agent was accorded little credit for its success.

Note however that, despite the sound strategy adopted, the results obtained from trial 1 are something of an anomaly: specifically, 100% success rates in both access attempts and tactic invocations are exceptional and only occur when the user has been very lucky. At the other extreme, in trial 3, the user was very unlucky. In this case, the tactic selection order is exactly the same as in trial 1 but the results are quite poor. Earlier we noted that, while chance is not the prime driver of the garbage can model, it does have an impact. In this extreme and unusualŽ . case, its consequences have been major. Thus, here we have a classic case in the ‘best laid plans going astray’ tradition and, as such, a useful example for any management student.

More broadly, strategic change today, as Pettigrew and Whipp 20 assert, rarely moves neatly<sup>w</sup> <sup>x</sup> across a succession of stages from analysis to implementation, essentially because of the potent forces within an organization. These, often relating to the economic, personal, and political imperatives driving change, tend to produce dilemma and the need for continuous assessments, ongoing diverse adjustments, and repeated choices. This is clear in the exercise discussed herein. According to Stace and Dunphy 27 : p. 202 : ‘The message is clear: one- Ž<sup>w</sup> <sup>x</sup> . stop change interventions, panaceas, the latest ‘buzzologies,’ and change Band-aids, are rarely successful. Change agents need to aim for change interventions, which are targeted and focused on critical variables, but which are comprehensive enough in their scope and depth to achieve results’.

## 5. Conclusion

If we agree that traditional rational choice models of decision making have rightly been contested by more realistic approaches, incorporating the powerpolitical dimensions, especially in group decision making, then our input may be considered a useful contribution. Given the constant presence of power in organizational life and processes, it is not surprising that decision making under conditions of extreme uncertainty—that is, in times of change—encourage an even greater flurry of political activity. This is essentially because, during organizational change, stakeholder positions are jealously guarded, sectional interests are paramount, and power bases strongly defended and utilised in efforts to influence process, resource allocation, and outcomes.

We have in this paper focused our discussion on dimensions of complexity, ambiguity, and change as they relate to decision making broadly in contemporary organizational life. In so doing, however, it is acknowledged that we have not dealt with many other variables of importance, one for example being that of national culture and its effect on the decision making process e.g., Ref. 18 . Nor have we tack-Ž <sup>w</sup> <sup>x</sup>. led the vital concern of time pressures on decisionmaking processes to any great extent 31 . As noted,<sup>w</sup> <sup>x</sup> these are only two of a great many factors that impact on organizational decisions 5 . We believe <sup>w</sup> <sup>x</sup> that many of these factors could usefully be incorporated into our model and have identified this as an area for further research. Our immediate aim, however, is to thoroughly test our model in both pedagogical and simulation-based experimental settings. Ž . We view the first of these as being particularly important, as there appears to be an appalling lack of computer-based management games that move beyond strictly quantitative bases to include the critical and, in many respects much more interesting, ‘softer factors 16 .<sup>w</sup> <sup>x</sup>

## References

<sup>w</sup> <sup>x</sup> 1 W. Agor Ed. , Intuition in Organizations, Sage, London, Ž . 1989.

<sup>w</sup> <sup>x</sup>2 M.D. Cohen, Organizational learning of routines: a model from the garbage can family,The Logic of Organizational Disorder, de Gruyter, Berlin, 1995.

<sup>w</sup> <sup>x</sup> 3 M.D. Cohen, J.G. March, Leadership and Ambiguity: The American College President, McGraw-Hill, New York, 1974.

<sup>w</sup> <sup>x</sup> 4 M.D. Cohen, J.G. March, J.P. Olsen, A garbage can model of organizational choice, Administrative Science Quarterly 17 Ž . Ž . 1 1972 .

<sup>w</sup> <sup>x</sup> 5 R.W. Cooksey, The complex dynamic texture of managerial decision making, Proceeedings of the Twelfth Internationa Conference of the Australian and New Zealand Academy of Management Adelaide, South Australia, 6–9 Dec. 1998 . Ž .

<sup>w</sup> <sup>x</sup> 6 S. Fineman Ed. , Emotion in Organizations, Sage, London, Ž . 1993.

<sup>w</sup> <sup>x</sup> 7 P.J. Frost, Power, politics and influence, in: F.M. Jablin, L.L. Putnam, K.H. Roberts, L.W. Porter Eds. , Handbook ofŽ . Organizational Communication: An Interdisciplinary Perspective, Sage, Beverly Hills, CA, 1987.

<sup>w</sup> <sup>x</sup> 8 D. Garvin, The processes of organization and management, Sloan Management Review 39 4 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 I. Janis, Victims of Groupthink, Houghton Mifflin, Boston, 1972.

<sup>w</sup> <sup>x</sup>10 J.C. Lindner, Information Technology: Fit and Change, MISR Course Handout, Harvard Business School, Boston, MA, July, 1989.

<sup>w</sup> <sup>x</sup> 11 LPA-Flex Expert System Toolkit: Technical Reference— Version 1.2, Logic Programming Associates, London, 1992.

<sup>w</sup> <sup>x</sup> 12 J.G. March, H. Simon, Organizations, Wiley, New York, 1958.

<sup>w</sup> <sup>x</sup> 13 J. Martin, Strategic Data-Planning Methodologies, Prentice-Hall, New Jersey, 1982.

<sup>w</sup> <sup>x</sup> 14 M. Masuch, P. LaPotin, Beyond garbage cans: an AI model of organizational choice, Administrative Science Quarterly 34 1989 .Ž .

<sup>w</sup> <sup>x</sup> 15 G.M. McGrath, An implementation of a data-centred information systems strategy: a power<sup>r</sup>political perspective, International J. Failure and Lessons Learned in Information Technology Management 1 1 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup>16 G.M. McGrath, R.J. Offen, Undergraduate students and the management–technology interface: a multi-disciplinary education program,Proceedings of the Third Australasian Conference on Computer Science Education, Brisbane, 8–10 July 1998.

<sup>w</sup> <sup>x</sup> 17 G.M. McGrath, C.N.G. Dampney, E. More, Planning for information systems integration: some key challenges, Journal of Information Science 20 3 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 S. Miller, D. Hickson, D. Wilson, Decision-making in organizations, in: W. Clegg, C. Hardy, W. Nord Eds. , Hand-Ž . book of Organization Studies, Sage, London, 1996.

<sup>w</sup> <sup>x</sup> 19 G. Morgan, Images of Organization, Sage, London, 1997.

<sup>w</sup> <sup>x</sup> 20 A. Pettigrew, R. Whipp, Managing Change for Competitive Success, Blackwell, London, 1993.

<sup>w</sup> <sup>x</sup> 21 J. Pfeffer, Power in Organizations, Pitman, Marshfield, MA, 1981.

<sup>w</sup> <sup>x</sup> 22 J. Pfeffer, Managing with Power: Politics and Influence in Organisations, Harvard Business School Press, Boston, MA, 1992.

<sup>w</sup> <sup>x</sup> 23 M.J. Prietula, K.M. Carley, L. Gasser, Introduction: a computational approach to organizations and organizing,Simulating Organizations, The MIT Press, Cambridge, MA, 1998.

<sup>w</sup> <sup>x</sup> 24 M.J. Prietula, K.M. Carley, L. Gasser Eds. , SimulatingŽ . Organizations, The MIT Press, Cambridge, MA, 1998.

<sup>w</sup> <sup>x</sup> 25 S.P. Robbins, R. Bergman, I. Stagg, Management, Prentice-Hall, Sydney, 1997.

<sup>w</sup> <sup>x</sup> 26 H. Simon, The New Science of Management Decision, Prentice-Hall, New Jersey, 1960.

<sup>w</sup> <sup>x</sup> 27 D. Stace, D. Dunphy, Beyond the Boundaries, McGraw-Hill, Sydney, 1994.

<sup>w</sup> <sup>x</sup> 28 R. Stacey, Strategic Management and Organisational Dynamics, Pitman, London, 1993.

<sup>w</sup> <sup>x</sup> 29 F.W. Taylor, The Principles of Scientific Management, Harper and Row, New York, 1911.

<sup>w</sup> <sup>x</sup> 30 J.A.M. Vennix, Group Model Building: Facilitating Team Learning Using System Dynamics, Wiley, Chichester, UK, 1996.

<sup>w</sup> <sup>x</sup> 31 V.H. Vroom, A.G. Jago, The New Leadership: Managing Participation in Organizations, Prentice-Hall, Englewood Cliffs, NJ, 1988.

<sup>w</sup> <sup>x</sup>32 M. Warglien, Learning in a Garbage Can Situation: A Network Model, The Logic of Organizational Disorder, de Gruyter, Berlin, 1995.

<sup>w</sup> <sup>x</sup> 33 M. Warglien, M. Masuch, The Logic of Organizational Dis-

order: An Introduction, The Logic of Organizational Disorder, de Gruyter, Berlin, 1995.

<sup>w</sup> <sup>x</sup> 34 R.T. Wigand, Communication network analysis: history and overview, in: G. Goldhaber, G. Barnett Eds. , Handbook ofŽ . Organizational Communication, Ablex, Newstead, NJ, 1998.

Dr. G. Michael McGrath gained his PhD in Computer Science from Macquarie University, Sydney, in 1993. He is currently the Deputy Director of the CSIRO-Macquarie University Joint Research Centre for Advanced Systems Engineering JRCASE ,Ž . where he heads a research strand focusing on socio-technica aspects of systems and software engineering. He has over 20 years experience in the IT industry—mostly at Australia’s largest PTC, Telstra, where he worked in a variety of technical and management positions. His current research interests include strategic information systems planning, business data and process modelling, knowledge base systems, software requirements elicitation, simulations of organisational decision-making processes, and ecommerce applications. Recent publications have appeared in the journals of Management Development, Communication Management and Intelligent Systems in Accounting, Finance and Management, and the Australian Computer Journal.

Dr. Elizabeth More is a Professor of Management and Director of the Graduate School of Management at Macquarie University and Director of MGSM. She has a BA and PhD from the University of NSW and a Graduate Diploma in Management from the University of Central Queensland. She has presented numerous conference papers and published widely, both locally and internationally, her latest books being Managing Changes, JAI Press, Connecticut, USA 1998 , and, with co-author, Dr. McGrath,Ž . The PeCC Story — Collaboration in an E-Commerce Business Alliance to be published by the National Office of the Information Economy, Canberra 2000 . Her key research and teaching areasŽ . are strategic behavior, knowledge management, organisational communication, organisational collaboration, and communications technology and policy. In addition to her academic work, Professor More has extensive experience in consulting to both private and public sector organisations. She was also appointed by the Commonwealth Government in 1992 for a 5-year term as a member of the Government’s Telecommunications Industry Development Authority DIST ; appointed to the Tax Concession Ž . Committee of the IR&D Board from 1996–1998; and appointed to the NSW Government’s Council on the Cost of Government in December 1999.
