---
otero_id: 25905
otero_key: "Y45FRYXY"
title: "Negotiation support systems: roots, progress and needs"
authors: "C W Holsapple; H Lai; A B Whinston"
year: "1991"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1991.tb00060.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Negotiation support systems: roots, progress and needs

C W Holsapple, $^{*}$ H Lai $^{\dagger}$ and A B Whinston $^{\ddagger}$

\*University of Kentucky, Lexington, Kentucky, †National Sun Yat-Sen University, Kaoshiung, Taiwan, China and ‡The University of Texas at Austin, Austin, Texas, USA

Abstract. This paper identifies game theories and social behavior science as important roots for negotiation support systems (NSS) research. As these are not typically cited in the NSS literature, summary reviews of them are provided with indications of their relevance to NSS study. On the other hand, neither offers a sufficiently general-purpose formal model of negotiation that could serve as a backbone for NSS research. A survey of that research is provided, indicating that progress to date has been somewhat eclectic and devoid of such a model. Our central contention is that a theoretical foundation for NSS study is much needed. Desirable characteristics of a suitable negotiation model are identified as guidance for future research that will aim to devise (and subsequently apply and test) such a model.

Keywords: negotiation, negotiation support, negotiation support systems.

## INTRODUCTION

Accompanying the rapid growth of organizations, are the distributed decision activities in which negotiation is a common and important activity. According to Lax & Sebenius (1986b), an organization is a complex network of agreement among its members and with outside parties. Within an organization, an entity may contact subordinates for task-assignment, evaluation, or command purposes; contact peers for co-operation, mutual obligation, or conflict resolution; contact superiors about compensation plans, allocation of budgets, new projects, and so forth. All of these activities are candidates for negotiations and perhaps for computer-based negotiation support.

A negotiation involves two or more participants who represent either themselves or others (e.g. a project team). Negotiation may result from conflict and competition, or be undertaken for some potential gain expected from co-operation among negotiators or those they represent. The negotiators may or may not gather in a meeting room. They may or may not make explicit offers or counter-offers (Bazerman, 1986). The resultant agreements can range from informal understandings to formal contracts. These agreements guide and shape organization behavior in the face of changing external and internal environments (Lax & Sebenius, 1986b).

As negotiation is a widespread, multifaceted, and complex phenomenon, it has been researched in such disciplines as economics, industrial relations, political science, social psychology, organizational management, and applied mathematics. It has been seen as an art as well as a science. It has been explored in terms of the broad practical maxims of social behaviour science and the more narrow abstractions of game theory.

There have been some efforts at developing and using computerized systems to support negotiation activities. These have come to be known as negotiation support systems (Jelassi & Foroughi, 1989). As workers in organizations have limited abilities and time to engage in negotiation, they (and their organizations) could benefit greatly from computerized systems that facilitate more efficient or effective negotiation.

This paper reviews existing roots for negotiation support system (NSS) research and NSS progress that has been made, as a basis for proposing what needs to be done in the NSS research realm. How does effort in the previously noted disciplines help people in negotiation activities? Do or can they help developers of NSSs? From a NSS standpoint, are there gaps in that research effort? If there are, then what is needed to aid a systematic advance in the NSS area? Some answers to such questions are provided here.

In the section entitled ‘Roots for NSS research’, we review important aspects of negotiation study from the fields of game theory and social behaviour science. Developments in computer-based support of negotiation are then reviewed in the following section. This includes relevant work in the areas of decision support systems, group decision support systems, and computer-supported co-operative work systems. It culminates in an examination of negotiation support system efforts. The section entitled ‘An important NSS research need’ argues that there is an important NSS research need for a theoretical model of negotiation phenomena. In the final section, we indicate characteristics that a negotiation model should possess if it is to aid in making substantial progress in developing NSSs.

## ROOTS FOR NSS RESEARCH

Two major realms of negotiation research are examined here. Because they yield insights into the nature of negotiation, it would seem that they may have considerable value for NSS research and development. Existing NSS literature tends not to deal with either area in any great depth. The first area is comprised of game theory. We shall interpret game theory in a broad sense that encompasses bargaining theory. Social behaviour science is the second related area, including such topics as labour relations, political science, management, and social psychology. Although research in these two areas does not focus on support of negotiation activities via computerized systems, it does provide a relevant foundation for studying potential negotiation support system features and uses.

## Game theory and bargaining theory

Basically, game theory tries to use mathematical models to describe and explain phenomena of conflict and co-operation among intelligent rational decision makers and/or find some prescriptive rules for them (Myerson, 1984). From the contention of Lax & Sebenius (1986b) that negotiation is ‘a process of potentially opportunistic interaction by which two or more parties with some apparent conflict, seek to do better through jointly decided action than they could otherwise’, it is clear that bargaining is inherent in some kinds of games.

Traditional game theory can be seen from two perspectives: descriptive and prescriptive. Descriptive theory tries to explain phenomena of games and bargaining in the real world and predict their outcomes. Prescriptive theory tries to build normative rules for successful gaming and bargaining to guide people involved in these activities. From either viewpoint, there are various models in the voluminous research for this area.

Typically, models begin by considering two-person games and are then extended to n-person games (e.g. Chin et al., 1974; Deegan & Packel, 1978; Sutton, 1986). Given a certain number of players, there are various ways to characterize games. For instance, zero-sum vs. non-zero-sum or zero-sum vs. constant-sum are common distinctions. Descriptions of these can be found in standard game theory books (e.g. Luce & Raiffa, 1957; Friedman, 1986). The co-operative vs. non-co-operative distinction is another common dimension for characterizing games (e.g. Nash, 1950; Pearce, 1984; Sutton, 1986). Generally, game theory literature tends to emphasize conflict more than co-operation. Discussions of co-operation tend to focus on formation of a coalition among a subset of players. It analyses what payoffs individuals and coalitions are able to achieve. A further issue in co-operative games is whether the utility is transferable among players who form a coalition (e.g. Myerson, 1984; Friedman, 1986).

Other issues examined in game theory include the timing of responses (e.g. Fudenberg & Tirole, 1983; Rubinstein, 1982, 1985; Cramton, 1985), completeness of information (e.g. Fudenberg & Tirole, 1983; Myerson, 1984; Rubinstein, 1985), number of time periods (e.g. Fundenberg et al., 1985), and existing of time-independence (e.g. Friedman, 1986). Some models are developed by focusing on multiple dimensions, resulting in non-co-operative zero-sum games, sequential bargaining with incomplete information, infinite-horizon with incomplete information, and so forth. However, existing models do not tend to consider all the important dimensions simultaneously.

The above theoretical issues have been discussed in terms of abstract mathematical models. In order to let the formalization be feasible or facile, there are some common assumptions. For instance, it is often assumed that players are rational and expect others to be rational, allowing a player to conjecture about other players' behaviour. A further common assumption is that each player attempts to maximize its own gain or utility. This assumption allows the detection of a players' strategy choice from its payoff or utility function. Each player's utility for each alternative settlement is typically assumed to be common knowledge.

However, such assumptions are impractical. First, players may not be rational or may have different interpretations of rationality. Second, a player may not attempt to maximize its own gain or utility due to difficulty in examining all possible alternatives. In addition, if there are multi-dimensional issues, it may not be possible or practical to reduce them to a single payoff number. Third, each player's utility for each alternative settlement may not be common knowledge and may change over time. Under such unrealistic assumptions, derived results are suspect.

Researchers have recognized the impracticality of such assumptions and tried to relax some of them. For example, in initial development of game theory, a rational decision maker who does not make mistakes has been a common assumption. This was the case of the Nash equilibrium. Researchers have tried to relax this assumption, pursuing perfect equilibrium (Selten, 1975) and sequential equilibrium (Kreps & Wilson, 1982) instead of the original Nash equilibrium. However, such efforts need a series of conjectures regarding future interaction, for the purpose of finding characteristics of an equilibrium state. If any conjecture is not realized, characteristics of that state are wrong.

Raiffa (1982) said that he did not use techniques of game theory when he was a negotiator in real life, though its concepts and ideas are helpful. Aside from practicality concerns, research in game theory neglects some important factors that are difficult to quantify. These include organizational norms, communication structure, type of response, and negotiator power, influence, and persuadability. However, going beyond traditional game theory, some of the foregoing limitations have been at least somewhat addressed by work on metagames and hypergames.

Metagames analysis is concerned with studying scenarios that could result as interacting participants establish positions, move to new positions, and attempt to cope with problems of credibility (Howard, 1989). It characterizes interaction in terms of a list of participants and the options available to each. Options are not mutually exclusive, meaning that each of the plans open to a participant could include the choice of multiple options. By picking exactly one feasible plan from each participant we define a scenario. The set of feasible scenarios, together with related threats and promises, can be represented graphically in a strategic map, which is then interpreted to judge the credibility of the threats and promises as a basis for determining the strategy and tactics that a participant will elect to pursue. A computer-based system (called CONAN) has been implemented to aid in storing information about an interactive situation and in strategic map interpretation.

Hypergame analysis is a means for analysing interactive decision making in which there is at least a potential for conflict among participants, each of whom can impact others in pursuing its own aims (Bennett et al., 1989). Importantly, it is recognized that participants can hold disparate views of the situation that relates them and that each participant can be enmeshed simultaneously in multiple situations involving related decisions. Rather than focusing on a single game, the analysis involves a collection of games — with different games for different participants. This requires a specification of strategies and preferences each participant believes each other (and itself) to have. Multiple methods for representing such hypergames have been developed.

Thus, the metagame and hypergame models relax some of the non-descriptive assumptions inherent in traditional game theory models. They also aim to consider simultaneously more of the important practical dimensions of bargaining. Coupled with the base of traditional game theory, they appear to furnish a starting point for beginning to formalize negotiation phenomena as a foundation for NSS research, development, and practice.

## Social behaviour science

Because negotiation activity is an interactive multiparticipant phenomenon, research in social behaviour science is concerned with such activities. In the field of labour relations, negotiation has long been discussed (e.g. Rukeyser, 1968; Kochan, 1980; Zack & Block, 1983). Political science is concerned with negotiation that occurs between levels of government within a country or among countries, involving such issues of contention as international trade regulations and arms control (e.g. Kapoor, 1975; Fisher, 1980). Of course, when people are involved, psychology is a consideration. As Spector (1978) says, negotiation can be regarded ‘as a psychological process’.

Negotiation has increasingly been seen as an important and necessary skill for effective management (Mintzberg, 1980; Bazerman & Lewicki, 1983; Brooks & Odiorne, 1984; Lax & Sebenius, 1986b; Lewicki et al., 1986; Johnson, 1990). It is contended that negotiating is a way of life for managers (Lax & Sebenius, 1986b). Furthermore, it is now recognized by many researchers that negotiation skill is important not only for managers, but for everyone in any organization.

Consequently, a number of 'How to' works on negotiation have been published (e.g. Scott, 1982; Kennedy et al., 1987). Compared to research in game theory, research in social behaviour science tends to be more empirical and practically oriented. It often attempts to summarize and interpret phenomena of negotiation activities observed in the real world or experiments. It sometimes aims to give advice for participants in negotiation. However, research coming from different disciplines tends to have different foci.

Research from the labour relations field emphasizes collective bargaining and how to maintain good relations between labour unions and managers. Political science research emphasizes achievement of political benefits through negotiation. Management research emphasizes how to have efficient and effective management via negotiation. Research in social psychology emphasizes prediction of possible interactions and understanding of possible intentions behind these interactions. Nevertheless, the common objective is to aid negotiators in doing well. Due to this common objective, these social behaviour research streams overlap. Thus, the review in this section is topic-oriented rather than discipline-oriented. Topics considered here include negotiator power, benefits, strategies, tactics, nature of negotiation, and third parties.

Negotiator power is a common research topic (e.g. McCarthy, 1985; Lewicki & Litterer, 1985; Bacharach & Lawler, 1981, 1986; Law & Sebenius, 1986b). It gives a basis for a negotiator to determine its strategies and tactics. There are several forms of power such as information power, reward power, coercive power, legitimate power, referent power, and expert power (e.g. Mintzberg, 1980; Lewicki & Litterer, 1985). Each can have benefits and drawbacks.

The nature of a power relationship is multidimensional and it can fluctuate over time (e.g. Lewicki & Litterer, 1985; Bacharach and Lawler, 1986). In addition, power relationships have a variables-sum, rather than a zero-sum nature. Interdependence is a major factor influencing power, a negotiator's dependence on another negotiator being a measure of the latter's power (Lewicki & Litterer, 1985; Bacharach & Lawler, 1986; Greenhalgh, 1987). When negotiators have long-term relationships, a power creation strategy should be based on short-term, as well as long-term, considerations.

Power relationships are more or less subjectively experienced. The way a negotiator defines the relationship, the experienced roles of a negotiation, and the time horizon are important factors influencing power relationships among negotiators. Negotiator personality is another important issue as successful negotiation requires one to understand the personality and power of other negotiators as well as his or her own (Lewicki & Litterer, 1985; Gilkey & Greenhalgh, 1986).

Benefits resulting from negotiation are a major concern of negotiators. Tangible versus intangible benefits are a common classification. The measure of benefits should not be limited to some obvious tangible interests, but also include more subtle intangibles such as reputation, precedent, relationships, strategy, fairness, and so on (Lax & Sebenius, 1985, 1986a, b; Kennedy et al., 1987). Further, Lax & Sebenius (1985, 1986a) classify interests into the instrumental versus intrinsic, depending on whether they have effects on subsequent dealings. This implies that consideration of benefits should be based on both long-term and short-term interests. As with power and personality, a negotiator should assess interests of other negotiators as well as its own.

Design and selection of both negotiation strategies and tactics are widely discussed (e.g. Nierenberg, 1973; Bacarach & Lawler, 1981; Raiffa, 1982, 1985; Lewicki & Litterer, 1985; Lax & Sebenius, 1986b; Kennedy et al., 1987). The nature of negotiation is the first major consideration in designing and selecting strategies and tactics. There are various angles from which to analyse the nature of a negotiation. These include single-shot vs. repetitive (Raiffa, 1982; Lax & Sebenius, 1986b), integrative vs. distributive (i.e. co-operative vs. competitive, win-win vs. win-lose) (Bacharach & Lawler, 1981; Raiffa, 1982; Lewicki & Litterer, 1985; Lax & Sebenius, 1986a, b), single-issue vs. multi-issue (Raiffa, 1982), two participant vs. many-participant (Raiffa, 1982; Lewicki & Litterer, 1985). Given a particular nature of negotiation factors of negotiators' personalities, power relationships, and expected interests influence design and selection of strategies and tactics.

Researchers have identified third party intervention in negotiation as an important issue (e.g. Raiffa, 1982; Rubin, 1983). A third party can be a facilitator, a mediator, an arbitrator, or a rule manipulator (Raiffa, 1982). Mediation seems to be the most common subject in intervention research (e.g. Moore, 1986; Pruitt, 1986; Carnevale, 1986; Brett et al., 1986; Murnighan, 1986; Coulson, 1988; Honeyman, 1988). Such work discussed the structure and effectiveness of mediation. It explored the strategies, attitude, and style of mediators.

Overall, negotiation research has evolved from addressing highly formal official negotiations to informal negotiations, from particular applications (such as industrial relations and international relations) to greater generality, and from one-shot negotiation to long-term (or even indefinite) negotiation. Such research provides many maxims that negotiators could practice and commit to memory. Compared to game theory, in which negotiation is regarded more as a science, negotiation in the social behaviour disciplines tends to be regarded more as an art. Therefore, these maxims tend to be expressed informally.

Unless such maxims are fully understood and accepted, it is very easy for negotiators to forget them in the heat of the argument. It may turn out that NSSs will be of some aid in this regard. This will depend on a consistent, unified, integrated formalization of the negotiation parameters and maxims identified in social behaviour science. Formalism is essential for computerization. Thus, the findings of social behaviour science have a substantial potential for feeding NSS research.

## PROGRESS IN COMPUTER-BASED SUPPORT OF NEGOTIATIONS

Each entity participating in a negotiation needs to make a series of decisions during a negotiation process. An outcome of negotiation can be regarded as a multiparticipant decision, agreed to by all the involved entities. The nature of a negotiation process may involve co-operation as well as competition. Therefore, decision support system (DSS) research and research into computer-supported co-operative work (CSCW) systems are relevant developments in the progression toward more advanced NSSs. This section examines four major developments: decision support systems, group DSS, CSCW systems, and negotiation support systems.

## Decision support systems

DSSs have been developed to deal with semi-structured and even non-structured tasks faced by individuals in the course of decision making (Bonczek et al., 1981; Sprague & Carlson, 1982; Klein & Hirschheim, 1985; Sprague, 1987; Holsapple & Whinston, 1988a). They focus on improving the effectiveness of decisions and/or the efficiency of decision makers. Because an individual entity makes a number of decisions in a negotiation, a DSS could be regarded as NSS when it aids in such decision making. Thus, progress in the DSS arena has contributed to the advance of NSS research.

Because decision making often involves multiple participants who might be at different organizational levels, solve one or more subproblems individually, jointly work on some problems simultaneously, DSS researchers have begun to work at developing theories for distributed decision making (Burns et al., 1987; Holsapple & Whinston, 1987, 1988b; Ching, 1988; Applegate et al., 1991). Such a theory could be an important foundation for designing systems that support decision making distributed across multiple-participants. As negotiating entities collectively aim to reach an agreement (i.e. a kind of multiparticipant decision), this theoretical DSS work would appear to contribute to NSS progress. Indeed, Jarke (1986) indicates that a multiperson decision process can be characterized by knowledge sharing and negotiation.

## Group decision support systems

Since the mid-1980s, researchers have become increasingly interested in DSSs that support group decision makers as wholes, rather than just supporting individuals (e.g. Huber, 1984; Rathwell & Burns, 1985; DeSanctis & Gallupe, 1985, 1987; Jarke, 1986; Bui & Jarke, 1986; Gray, 1987; Nunamaker et al., 1987, 1988). Developing a group decision support system (GDSS) is motivated by the common phenomenon of decisions being made by a group (e.g. a jury) rather than a single person. DeSanctis & Gallupe (1985) state that a 'group decision support system (GDSS) is an interactive computer-based system which facilitates solution of unstructured problems by a set of decision makers working together as a group'.

GDSS research has focused on computerized support for people meeting to reach a decision as a group. It has not considered support of hierarchic teams or mixed types of organizations (Bonczek et al., 1979; Holsapple, 1989). A GDSS attempts to facilitate interactive sharing and use of information not only between group members and the computer, but also among group members (Huber, 1984). As Huber says, a GDSS operates in the context of decision-related meetings by facilitating information retrieval, information sharing, and information use among participants.

Some GDSSs can be regarded as NSSs in the sense that some of their features can facilitate negotiation processes that happen within groups. Some aspects of GDSS architectures (e.g. for handling multiparticipant communications) would seem to be applicable to NSS design. In general, however, GDSSs tend not to be strictly oriented toward supporting negotiation activity. While GDSS research efforts have touched on some aspects of negotiation in various ways, they include little in the way of a formal examination of the nature of negotiation and how to support it.

Sometimes it is claimed that NSSs are special cases of GDSSs (e.g. Foroughi & Jelassi, 1990). However, a NSS is not necessarily a GDSS. It would seem NSSs could be designed with the intent of supporting negotiation among participants who do not constitute a group, but rather a hierarchic team or other organizational form. Such systems would need to be conceived with an understanding that participants can have widely divergent degrees of authority, play various specialized roles, operate under structured communication restrictions, and participate across multiple negotiation episodes.

## Co-operative work systems

Outside the DSS area, there is a sizable body of research concerned with development of computerized tools that support co-operative work. Commonly known as computer-supported co-operative work (CSCW) systems, they are concerned with means for co-ordinating and integrating the individual efforts of multiple participants with respect to some multiparticipant task (e.g. authoring a document). If the task of interest could be negotiation, then it would seem that a CSCW tool might be able to function as a NSS. While this particular task received little attention in the CSCW literature, a brief sampling of CSCW research reveals ways in which it may contribute to NSS construction.

One example of a CSCW system is a co-ordinator system to support collaborative idea-generation activity (Johnson et al., 1986). This system provides two frameworks for communication: conversation for possibilities and conversation for action. It would seem that these two modes of communication may be usefully supported in negotiations. Another study attempted to measure the effectiveness of a CSCW system, called The Co-ordinator, as a communication tool (Carasik & Grantham, 1988). Finding a negative cognitive shift, the researchers suggest that an improved interface, more flexible terminology, and better implementation support may be needed to make the CSCW system viable. We may expect similar phenomena in the study of particular NSSs.

Quilt is another CSCW tool. It was designed to provide a mechanism to enhance the communication and information sharing of persons collaborating on the preparation of a document (Fish et al., 1988). A distinguishing characteristic of Quilt is that it provides mechanisms for defining, changing, and enforcing the social roles of the participants and their associated rights and responsibilities. Such mechanisms would seem to be relevant to the construction of NSSs.

The IBIS (Issue-Based Information System) method of structured argumentation has been developed to aid multiple persons involved in large and complex design problems (Kunz & Rittel, 1970). Computer-based implementations of this method include glBIS (graphical IBIS), which has been designed to support collaborative construction of issue nets by co-operating persons via a local area network (Conklin & Begeman, 1988). Such CSCW systems that help structure issues and debate would seem to have potential in the NSS realm, particularly in conjunction with features of a metagame system like CONAN.

## Negotiation support systems

While DSSs, GDSSs, and CSCW systems may in some ways offer negotiation support, this has not been the prime motive or interest of such research. There is a small but growing literature concerned with direct and explicit study of NSSs. Among the earliest published examples was the Conflict Analysis Program, developed to provide support for an arbitrator during prenegotiation strategy formulation (Fraser & Hipel, 1981). It would help arbitrators eliminate infeasible agreements, order feasible ones according to players' preferences, and assess stability of agreement.

DECISION CONFERENCING is a system that aims to help participants disaggregate complex issues, create new alternatives, anticipate others' positions, and facilitate communication among negotiators (Quinn et al., 1985). Another example is NEGO designed to help negotiators change their strategies, form coalitions, and evaluate compromises (Kersten, 1985). Negoplan is an expert system shell for negotiation support (Matwin et al., 1989). It uses a rule-based system in representing negotiation issues and decomposing negotiation goals to help a participant examine consequences of different negotiation scenarios.

Jarke et al. (1987) propose a system, MEDIATOR, to support a human mediator in a negotiation activity by using view integration to build a joint problem representation. Afterwards, consensus seeking proceeds by adaptive changes to a feasible set and target set. The system is designed to provide 'user-friendly' interfaces, efficient access to data and models, and structured communication facilities for both the players and the mediator.

A model that formalizes participants' influence and persuadability has been introduced to support nemawashi, the process of gaining consensus through persuasion and negotiation in Japanese organizations (Watabe et al., 1988). Partially based on multiple criteria decision methods, this model accommodates various strategies of co-ordination by accounting for participant preference and influence in varied ways. A useful characteristic of the model is that it allows a co-ordinator to understand on which points there are differences among participants' targets and the co-ordinator's own target plus how great those differences are.

Experimental investigations have begun to appear in the NSS literature. One example examines impacts of computer support during negotiation in situations of both high and low conflict (Jones & Jelassi, 1989). The computer supports negotiation as an intervenor, presenting three suggestions simultaneously 12 minutes after the start of bargaining and displaying them throughout the remainder of the bargaining process. Although this is an extremely primitive type of NSS in which communication between the computer and the players is one-way and one-time only, results appear to show that even so simple a NSS can be of value in both high and low conflict situations.

## AN IMPORTANT NSS RESEARCH NEED

We have seen that game theory and social behaviour science provide valuable insights for understanding negotiation. They form roots for NSS research, even though they are not frequently cited in the NSS literature. However, in these roots we do not find a ready-made model of negotiation phenomena sufficiently general and formal to offer a unified theoretical backbone for systematic NSS research and development. Nor do we find such a model in NSS literature.

The central contention of this paper is that a general-purpose, formal model of negotiation is needed for a more systematic and rapid advance of NSS research and development. Although various NSS researchers have built computerized systems to support negotiation, they tend to take a case-by-case approach. This is more or less an ad hoc type of effort, grounded on what has been observed as being potentially helpful in a particular negotiation situation or on adaptation of some mathematical method (or computer technology) to some negotiation aspect.

There is little evidence of NSSs having been developed on the basis of a comprehensive model or theory of negotiation. Hence, a NSS might be fine for a particular problem in a particular organization, but may not be relevant to some other organizations or even to some other negotiation problems in the same organization. Moreover, the absence of a guiding model can lead to design oversights, a lack of feature integration, and a failure to recognize NSS possibilities.

For example, some NSSs are adaptations of multicriteria decision methods to negotiation (e.g. Jarke, 1986; Bui & Jarke, 1986; Fraser & Hipel, 1981). But, these methods hardly constitute a model of the full phenomena of negotiation. Some NSSs are intended to help participants in a group negotiation. They may be of little use where participants constitute a hierarchic team or complex organization. In the case of MEDIATOR, we have a NSS that does not address negotiations that lack a mediator. It also makes assumptions about each participant having a personal DSS. This may not be valid in many negotiation situations. Negoplan is interesting in its use of a rule-based system to represent and decompose negotiation goals, but does not consider coalition possibilities or possible intervenors.

Important factors such as organizational norms, communication structures, interaction modes, negotiator power, influence, and persuadability are not typically considered in existing NSSs. Even where negotiator influence and persuadability have been formalized, the focus is only on decision-making processes in the context of nemawashi. Important factors such as the nature of an issue and a negotiator's strategy are absent in that formalism. Perhaps a main reason for such NSS gaps is that we do not have a conceptual, general-purpose, formalized theory or model precisely characterizing the nature and process of negotiation.

Lacking a general-purpose, formalized model of negotiation, NSSs tend to be based on sensed needs of various negotiation situations by various developers. Thus the applicability and extensibility of developed NSSs are limited. Another result is the lack of a standard language for discussion, comparing, and contrasting NSSs. Until we have a precise and global appreciation of negotiation activities, the routine construction of flexible, practical, full-feature NSSs will be hampered.

## CHARACTERISTICS OF A NEGOTIATION MODEL FOR NSS RESEARCH

Although research in game theory and social behaviour science does not give the negotiation model we seek, it does provide a starting point for devising such a model. The developed model should synthesize concepts found there, identifying important factors that characterize the nature and process of negotiation. It should formalize aspects of negotiation that are easy to quantify, as well as aspects that are difficult to quantify (e.g. communication structure, response type, negotiators power, reputation, persuadability, and learning processes). It should specify types and natures of settlements.

The model should be sufficiently flexible to describe all or most of the possible structures of negotiation and possible dynamic interactions under any given structure. For example, it should account for metagame, hypergame, nemawashi, and other models. It should be capable of being applied to (or even suggesting) uncommon negotiation phenomena, as well as the commonplace. Moreover, it should be able to describe negotiation within groups, teams, or organizations between those extremes. It should be independent of the number of negotiators. It should be created in such a way that it is not only internally consistent. It should allow us to identify and classify the universe of NSS possibilities. It should not only be descriptive, but its language should be sufficiently rich to allow researchers to state hypotheses and prescriptions.

The model will consist of an integrated set of negotiation constructs and principles, systematically expressed in terms of a parametric formal language. Its major contribution will be to define the field of NSS possibilities. It will give researchers and NSS developers a vehicle for exploring the alternative types and issues of negotiation support in a flexible, practical, and integrated way rather than in an ad hoc manner. While delimiting the NSS field, it will also give a basis for further, more refined, theoretical research within those bounds. It will give empirical researchers an organized means for conceiving experimental and field studies. Such a model is an essential basis for the advance of NSS research.

## CONCLUSION

This paper has considered the roots, progress, and a central need of NSS research. A review of existing NSSs shows that, while progress is being made, they are not derived from a comprehensive, general-purpose, formalized model. Such a model could accelerate progress in the NSS field. Game theory and social behaviour science do not offer the needed model, but can serve as important roots for its creation. We intend to posit such a model and encourage others to join in this effort. The results of this work should lead to an exploration of implications for studying and developing NSSs. These implications may be concerned with such topics as NSS architecture, alternative realizations of NSS functions, NSS typologies, and traits of NSS development tools.

## ACKNOWLEDGEMENT

This work has been supported in part by the National Science Foundation, Grant No. IRI-8921603.

## REFERENCES

Applegate, L., Ellis, C., Holsapple, C., Radermacher, F. & Whinston, A. (1991) Organizational computing: definition and issues Organization Computing, 1, 1–10.

Bacharach, S. & Lawler, E. (1981) Bargaining: Power, Tactics, and Outcomes. Jossey-Bass Publishers, San Francisco, California.

Bacharach, S. & Lawler, E. (1986) Power dependence and power paradoxes in bargaining. Negotiation Journal, 2, 167–174.

Bazerman, M. (1986) Managerial Decision Making, John Wiley & Sons, Inc, New York.

Bazerman, M.H. and Lewicki, R.J. (eds) (1963) Negotiating in Organizations. Sage Publications Inc, Beverly Hills, California.

Bennett, P., Cropper, S. & Huxham, C. (1989) Modelling interactive decisions: the hyergame focus. In: Rational Analysis for a Problematic World, Rosenhead, J. (ed), pp. 283–314. New York.

Bonczek, R., Holsapple, C. & Whinston, A. (1979) Computer-based support of organizational decision making. Decision Sciences, 10, 268–291.

Bonczek, R., Holsapple, C. & Whinston, A. (1981) Foundations of Decision Support Systems, Academic Press Inc., New York.

Brett, J., Drieghe, R. & Shapiro, D. (1986) Mediator style and mediation effectiveness. Negotiation Journal, 2, 277–285.

Brooks, E. & Odiorne, G. (1984) Managing by Negotiations.
Van Nostrand Reinhold Co, New York.

Bui, T. & Jarke, M. (1986) Communications design for co-op: a group decision support system. ACM Transactions on Office Information Systems, 2, 81–103.

Burns, A., Rathwell, M. & Thomas, R. (1987) A distributed system for decision making. Decision Support Systems, 3, 121–131.

Carasik, K. & Grantham, C. (1986) A case study of CSCW in a dispersed organization. Proceedings of CHI '88, Human Factors in Computing Systems, 61–66.

Carnevale, P. (1986) Strategic choice in mediation. Negotiation Journal, 2, 41–56.

Chin, H., Parthasarathy, T. & Raghavan, T. (1974) Structure of equilibria in N-person non-cooperative games. International journal of game theory, 3, 1–19.

Ching, C. (1988) A General Theory of Distributed Decision Making PhD thesis, Purdue University, West Lafayette, Indiana.

Conklin, J. & Begeman, M. (1988) glBIS: a hypertext tool for exploratory policy discussion. Proceedings of CSCW '88, 140–152.

Coulson, R. (1988) Must mediated settlements be fair? Negotiation Journal, 4, 15–17.

Cramton, P. (1985) Sequential bargaining mechanisms. In: Game-Theoretic Models of Bargaining, Roth, A. (ed), pp. 89–104. Cambridge University Press.

Deegan, J. & Packet, E. (1978) A new index of power for Simple n-Person Games. International Journal of Game Theory, 7, 113–123.

DeSanctis, G. & Gallupe, R. (1985) Group decision support systems: a new frontier. Data Base, 8, 3–10.

DeSanctis, G. & Gallupe, R. (1987) A foundation for the study of group decision support systems. Management Science, 33, 589–609.

Fish, R., Kraut, R. & Leland, M. (1988) Quilt: a collaborative tool for cooperative writing. Conference on Office Information Systems, 206–215.

Fisher, G. (1980) International Negotiation: A Cross-Cultural Perspective. International Press, Chicago.

Foroughi, A. & Jelassi, M. (1990) NSS solutions to major negotiation stumbling blocks. Proceedings of Hawaiian International Conference on Systems Sciences, Kona, Hawaii.

Fraser, N. & Hipel, K. (1981) Computer assistance in labor-management negotiation. Interface, 11, 22–29.

Friedman, J. (1986) Game Theory with Applications to Economics, Oxford University Press, Oxford.

Fudenberg, D., Levine, D. & Tirole, J. (1985) Infinite-horizon models of bargaining with one-sided incomplete information. In: Game-Theoretic Models of Bargaining. Roth, A. (ed.). Cambridge University Press.

Fudenberg, D. & Tirole, J. (1983) Sequential bargaining with incomplete information. Review of Economic Studies, 50, 221–247.

Gilkey, R. & Greenhalgh, L. (1986) The role of personality in successful negotiating. Negotiation Journal, 2, 245–256.

Gray, P. (1987) Group decision support systems. Decision Support Systems, 3, 233–242.

Greenhalgh, L. (1987) Relationships in negotiations. Negotiation Journal, 3, 235–243.

Holsapple, C. (1989) Decision support in multiparticipant decision makers, Kentucky initiative for knowledge management. Research paper No. 12, (forthcoming in Journal of Computer Information Systems).

Holsapple, C. & Whinston, A. (1987) Knowledge-based organizations. Information Society, 5, 77–90.

Holsapple, C. & Whinston, A. (1988a) The Information Jungle Dow Jones-Irwin, Homewood, Illinois.

Holsapple, C. & Whinston, A. (1988b) Distributed decision making: a research agenda. SIGOIS Bulletin, 9, 1.

Honeyman, C. (1988) Five elements of mediation. Negotiation Journal, 4, 149–160.

Howard, N. (1989) The manager as politician and general: the metagame approach to analysing cooperation and conflict. In: Rational Analysis for a Problematic World, Rosenhead, J. (ed.), pp. 239–262. Wiley, New York.

Huber, G. (1984) Issues in the design of group decision support systems. MIS Quarterly, 8, 195–204.

Jarke, M. (1986) Knowledge sharing and negotiation support in multiperson decision support systems. Decision Support Systems, 2, 93–102.

Jarke, M., Jelassi, M. & Shakun, M. (1987) MEDIATOR: towards a negotiation support system. European Journal of Operational Research, 31, 314–334.

Jelassi, M. & Foroughi, A. (1989) Negotiation support systems: an overview of design issues and existing software. Decision Support Systems, 5, 2.

Johnson, B., Weaver, G., Olson, M., Dunham, R. & McGonagill, G. (1986) Using a computer-based tool to support collaboration: a field experiment. MCC Conference on Computer Support for Cooperative Work. Austin, Texas, December.

Johnson, M. (1990) How you can outsmart opponents in negotiation. Investor's Daily, 7, 4–12.

Jones, B. & Jelassi, M. (1989) Negotiation Support: The Effects of Computer Intervention and Conflict Level on Bargaining Outcome. INSEAD Paper 89/03, January. Fountainbleau.

Kapoor, A. (1975) Planning for International Business Negotiations. Ballinger Publishing Co, Cambridge, Maryland.

Kennedy, G., Benson, J. & McMillan, J. (1987) Managing Negotiations, (3rd edn). Guernsey Press Co Ltd, London, Great Britain.

Kersten, G. (1985) NEGO—group decision support system. Information and Management, 8, 237–246.

Klein, H. & Hirschheim, R. (1985) Fundamental issues of decision support systems: a consequentialist perspective. Decision Support Systems, 1, 5–24.

Kochan, T. (1980) Collective Bargaining and Industrial Relations: From Theory to Policy and Practice. R.D. Irwin, Homewood, Illinois.

Kreps, D. & Wilson, R. (1982) Sequential equilibrium Econometrica, 50, 863–894.

Kunz, W. & Rittel, H. (1970) Issues of elements of information systems. Working Paper 131, Center for Planning and Research Development, Institute of Urban and Regional Development, University of California, Berkeley.

Lax, D. & Sebenius, J. (1985) The power of alternatives or the limits to negotiation. Negotiation Journal, 1, 163–179.

Lax, D. & Sebenius, J. (1986a) Interests: the measure of negotiation. Negotiation Journal, January, 73–92.

Lax, D. & Sebenius, J. (1986b) The Manager as Negotiator: Bargaining for Cooperation and Competitive Gain. The Free Press, New York.

Lewicki, R., Sheppard, B. & Bazerman, M. (eds) (1986) Research on Negotiation in Organizations, Vol. 1 JAI Press Inc, Greenwich, Connecticut.

Lewicki, R. & Litterer, J. (1985) Negotiation. R.D. Irwin Inc, Homewood, Illinois.

Luce, R. & Raiffa, H. (1957) Games and Decisions: Introduction and Critical Survey. John Wiley & Sons, Inc, New York.

Matwin, S., Szpakowicz, S., Koperczak, Z., Kersten, G. & Michałowski, W. (1989) Negoplan: an expert system shell for negotiation support. IEEE EXPERT, 4, 50–62.

McCarthy, W. (1985) The role of power and principle in getting to yes. Negotiation journal, 1, 59–66.

Mintzberg, H. (1980) The Nature of Managerial Work. Prentice-Hali, Englewood Cliffs, New York.

Moore, C. (1986) The Mediation Process: Practical Strategies for Resolving Conflict. Jossey-Bass Publishers, San Francisco, California.

Murnighan, J. (1986) The structure of mediation and intravention: comments on Carnevale's strategic choice model. Negotiation Journal, 2, 351–356.

Myerson, R. (1984) An introduction to game theory. Discussion Paper No. 623, The Center for Mathematical Studies in Economics and Management Science, Northwestern University, September.

Nash, J. (1950) Two-person competitive games. In: Bargaining: Formal Theories of Negotiation, Young, O (ed.), University of Illinois Press, Urbana, Illinois.

Nierenberg, G. (1973) Fundamentals of Negotiating. Hawthorn Books Inc, New York.

Nunamaker, J., Applegate, L. & Konsynski, B. (1987) Facilitating group creativity, experience with a group decision support system. Journal of Management Information Systems, 3, 5–19.

Nunamaker, J., Applegate, L. & Konsynski, B. (1987) Computer-aided deliberation: model management and group decision support. Operations Research, 36, 826–848.

Pearce, D. (1984) Rationalizable strategic behavior and the problem of perfection. Econometrica, 52, 1029–1050.

Pruitt, C. (1986) Trends in the scientific study of negotiation and mediation. Negotiation Journal, 2, 237–244.

Quinn, R., Rohrbaugh, J. & McGrath, M. (1985) Automated decision conferencing: how it works. Personnel, 62, 49–55.

Raiffa, H., (1982) The Art and Science of Negotiation, Belknap Press of Harvard University Press, Cambridge, Maryland.

Raiffa, H. (1985) Creative compensation: maybe 'In My Backyard'. Negotiation Journal, July, 197–203.

Rathwell, M. & Burns, A. (1985) Information systems support for group planning and decision-making activities. MIS QUARTERLY, September, 157–169.

Rubin, T. (1983) The use of third parties in organizations: a critical response. In: Negotiating in Organizations, Bazerman, M. and Lewicki, R. (eds). Sage Publications Inc, Beverly Hills, California.

Rubinstein, A. (1982) Perfect equilibrium in a bargaining model. Econometrica, 50, 97–109.

Rubinsten, A. (1985) A bargaining model with incomplete information about time preferences. Econometrica, 53, 1151–1172.

Rukeyser, M. (1968) Collective bargaining: the power to destroy; new and better ways to industrial place. Delacorte Press, New York.

Scott, W. (1982) The Skills of Negotiating. Gower Publishing Co. Limited, England.

Selten, R. (1975) Reexamination of the perfect concept for equilibrium points in extensive games. International Journal of Game Theory, 4, 25–55.

Spector, B. (1978) Negotiation as a psychological process. In: The Negotiation Process: Theories and Application, Zartman, I. (ed.). Sage Publications Inc, Beverly Hills, California.

Sprague, R. (1987) DSS in context. Decision Support Systems, 3, 197–202.

Sprague, R. & Carlson, E. (1982) Building Effective Decision Support Systems. Prentice-Hall, Englewood Cliffs, New Jersey.

Starr, M. & Zeleny, M. (eds) (1977) Multiple Criteria Decision Making. North Holland, New York.

Sutton, J. (1986) Non-cooperative bargaining theory: an introduction. Review of Economic Studies, 53, 709–724.

Watabe, K., Holsapple, C. & Whinston, A. (1988) Coordinator support in a Nemawashi decision process, Kentucky initiative for knowledge management, Research paper 4, (forthcoming in Decision Support Systems).

Zack, A. & Bloch, R. (1983) Labor Agreement in Negotiation and Arbitration. Bureau of National Affairs, Washington, D.C.

Zartman, I. (1988) Common elements in the analysis of the negotiation process. Negotiation Journal, 4, 31–43.

## Biographies

Clyde W. Holsapple is Professor of Decision Science and Information Systems and holds the Endowed Chair in Management Information Systems at the University of Kentucky. In addition to his books on the decision support system, data base management, and expert system areas, he has many research articles published in such journals as Decision Support Systems, Operations Research, The Computer Journal, Organization Science, Decision Sciences, IEEE Expert, Financial Management, Policy Sciences and Recherche Operationnelle. Dr Holsapple is the DSS Area Editor for ORSA Journal on Computing and Associate Editor for Organizational Computing and Management Science.

Hsiangchu Lai is Associate Professor of Information Management at National Sun Yat-Sen University in the Republic of China. Her doctoral dissertation was one of the earliest extensive examinations of negotiation support system possibilities. Dr Lai's current research interests include topics of computer-based support for negotiation and decision making.

Andrew Whinston is Professor of Information Systems, Computer Science, and Economics at the University of Texas (Austin), where he also holds the John B. Harbin Centennial Chair in Business. His hundreds of publications include many books, plus articles in the leading journals of such fields as management science, business computing, computer science, economics, accounting, and manufacturing systems. His former doctoral students now hold dozens of faculty positions at major universities. Dr Whinston serves on numerous editorial boards and is Editor of both Organizational Computing and Decision Support Systems. Along with Dr Holsapple, he co-directs the International Society for Decision Support Systems.
