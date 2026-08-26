---
otero_id: 7342
otero_key: "TQT2VN5M"
title: "Decisional Guidance for Computer-Based Decision Support"
authors: "Mark Silver"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/249441"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decisional Guidance for Computer-Based Decision Support $^{1}$

By: Mark S. Silver
Information Systems
Anderson Graduate School of Management
University of California
Los Angeles, California 90024

## Abstract

In the course of interacting with a decision support system (DSS), decision makers may have numerous opportunities for exercising judgment. Some judgments pertain to what to do next; others require predictions or evaluations. Either deliberately or inadvertently, a DSS may guide its users in performing these judgments. This article lays a foundation and proposes an agenda for researching such “decisional guidance.” Studying decisional guidance matters for two reasons. First, deliberately incorporating guidance in a system offers the potential of more supportive systems while raising a number of design questions. Second, understanding the consequences of guidance—deliberate or not—contributes to comprehending how DSSs affect decision-making behavior. This article examines three aspects of decisional guidance: (1) when and why system designers should provide decisional guidance, considering the opportunities, motives, and means for guiding; (2) how designers can provide guidance, introducing a three-dimensional typology for deliberate guidance; and (3) the consequences of decisional guidance—that is, its effects and effectiveness. This article provides a coherent approach to a set of behavioral questions just now beginning to be addressed by researchers in a fragmented, technologically oriented manner.

Keywords: Decision support systems, decision-making process, decision making, decisional guidance, human judgment, meta-support, meta-choice

ACM Categories: H.0, H.4.2, H.1.2

## Introduction

The outputs of a decision support system (DSS), such as data displays, statistical analyses, modeling results, and graphs, are intended to support the human judgment involved in making decisions. But often, those outputs are themselves produced from the judgmental inputs of the system's users. While interacting with a DSS, users may have numerous opportunities for exercising judgment and making choices. Some judgments concern what to do next: Should I run the same analysis again with different parameters? Should I peruse the database? Should I run a regression on the data? Other judgments are predictive: What will inflation be in the third quarter of this year? What is the likelihood that the prime interest rate will exceed 10 percent by year-end? How many units of my product will I sell this month? Still others are evaluative: Is this level of profit satisfactory? What is the acceptable trade-off between short-term profit and long-run market share?

Any interactive computer-based system must provide a means for users to communicate their judgmental inputs. Menus, command interpreters, fill-in tables, and question-answer dialogs are used widely for this purpose. When analyzing a DSS, a key issue is whether these input mechanisms affect the substance of users' judgmental inputs. A related issue, equally important, is whether the system contains special mechanisms whose roles are to guide users' judgments. Consider some examples:

\- Menus may lead to order effects. Because the order in which information is presented to human decision makers can affect its salience, users may tend to select the first and last items on menus.

\- Context-sensitive help messages, commonly used to explain the options available to users, may provide information that helps users differentiate substantively the options they confront.

\- Intelligence or expertise may be embedded in a system such that it recommends actions and responses to its users.

Each example illustrates a different kind of guidance. In the first one, the guidance is a consequence—perhaps inadvertent—of using a traditional input mechanism. The second example's help facility, unlike many others that describe only the mechanics of selecting an input, provides its users with insight into the judgmental task. And in the third case, a new mechanism has been introduced into the system for the purpose of advising the user. In each example, the system guides the decision maker as he or she responds to its requests for judgments or choices.

Although inadvertent decisional guidance deserves attention as well, this article concentrates mostly on guidance deliberately provided by the system designer. We can think of such guidance as “meta-support” for judgmental activities because it supports more effective use of a system that itself supports more effective decision making. Just as a DSS supports the judgments required enroute to making decisions, decisional guidance can support the judgments required in the course of operating the DSS.

Deliberate decisional guidance is rarely found in today's DSSs. The meta-support we now find in DSS is better termed "mechanical" than "decisional" because its guidance mechanisms—such as pull-down menus and help screens—are oriented more toward the mechanics of operating the system's features than toward the decisional and judgmental tasks at hand. Nonetheless, a number of recent research projects have begun to develop decisional guidance mechanisms.

The research to date is fragmented and mostly technologically oriented. Each project is independent of the others, with its own objectives, vocabulary, and methods. Most projects focus on developing meta-support mechanisms rather than on examining the behavioral effects of these devices. We can expect to see more and more such research projects. Now is the critical time, therefore, to establish a unified approach, one that recognizes the importance of both technological and behavioral issues. This article's purpose is to present such a unified approach by laying a foundation and proposing an agenda for research on decisional guidance.

Following a brief introduction that defines decisional guidance, the body of the article is divided into three sections (see Table 1). The first section explores the design question of when and why system designers should provide decisional guidance, considering the opportunities, motives, and means for guiding. The next section covers another design question, how designers can provide guidance. It presents a three-dimensional typology for deliberate decisional guidance. The last of these sections considers the consequences of decisional guidance—that is, the effects and effectiveness of guidance—a topic that has implications both for DSS design and for understanding how DSSs affect decision making. Each section includes its own agenda for research. These agendas are interrelated, with the study of consequences playing the key role that ties the others together.

Why is researching decisional guidance and its effects so important? For DSS designers, decisional guidance represents a host of new design opportunities and a concomitant set of design concerns. For researchers, the study of guidance provides a coherent approach to a set of behavioral questions just now beginning to be

## Table 1. Key Issues for Studying Decisional Guidance

<table><tr><td>When and why to provide deliberate decisional guidanceThe opportunities for guidingThe motives for guidingThe means for guidingHow to build deliberate decisional guidance into DSSThe targets of guidanceThe forms of guidanceThe modes of guidanceWhat the consequences of decisional guidance areThe effects of inadvertent decisional guidanceThe effects of deliberate decisional guidanceThe effectiveness of deliberate decisional guidance</td></tr></table>

addressed in a fragmented, technologically oriented manner. By adopting a unified approach—a common foundation and agenda—we can build a cumulative knowledge base that can lead to better understanding of decisional guidance and more effective support for decision makers.

## Decisional Guidance Defined

If and how a DSS guides its users' judgmental inputs, intentionally or not, is clearly an important attribute of that system. I shall refer to this attribute as decisional guidance, defined formally as follows:

Decisional Guidance: how a decision support system enlightens or sways its users as they structure and execute their decision-making processes—that is, as they choose among and use the system's functional capabilities.

Decisional guidance is one of several system attributes that can help us understand better the effects DSSs have on the decision-making processes of their users (Silver, 1988b). Silver (1990) briefly describes this attribute in its role as a contributor to individual or organizational change. The current article presents decisional guidance as an attribute worthy of serious study in its own right.

Note several key aspects of the definition (summarized in Table 2): First, the term decisional guidance is not limited to instances where a designer purposefully includes guidance mechanisms in a system. Indeed, we can distinguish two kinds of decisional guidance: inadvertent and deliberate. Inadvertent guidance is an unintended consequence of the system's design and is not planned by the system designer. Order effects not anticipated by a menu's designer exemplify this kind of guidance. In contrast, deliberate guidance is intentionally built into a system by its designer. Help facilities that inform users and embedded intelligence that advises users are examples of this case.

Second, even when guidance is deliberate, it is not necessarily intended to steer decision makers in a given direction. Deliberate guidance provides meta-support for judgmental activities. It can be

## Table 2. Key Distinctions in the Definition of Decisional Guidance

<table><tr><td>Mechanical versus Decisional Guidance</td></tr><tr><td>• Mechanical guidance helps users with the mechanics of operating a system&#x27;s features, often a matter of knowing when to push which buttons.</td></tr><tr><td>• Decisional guidance helps users deal with the decision-making concepts involved in choosing among and interacting with a system&#x27;s information-processing capabilities.</td></tr><tr><td>Inadvertent versus Deliberate Decisional Guidance</td></tr><tr><td>• Inadvertent decisional guidance is an unintended consequence of the system&#x27;s design and is not planned by the system designer.</td></tr><tr><td>• Deliberate decisional guidance is intentionally built into a system by its designer.</td></tr><tr><td>Suggestive Decisional Guidance versus Informative Decisional Guidance</td></tr><tr><td>• Suggestive guidance makes judgmental recommendations (what to do, what input values to use) to the decision maker.</td></tr><tr><td>• Informative guidance provides pertinent information that enlightens the decision maker&#x27;s judgment, without suggesting how to act.</td></tr><tr><td>Decisional Guidance for Structuring versus Decisional Guidance for Executing the Decision-Making Process</td></tr><tr><td>• Guidance for structuring the decision-making process affects how users choose which operators to invoke and the order in which to invoke them.</td></tr><tr><td>• Guidance for executing the process affects how decision makers perform the evaluative and predictive judgments necessary when executing the chosen operators.</td></tr></table>

suggestive, making judgmental recommendations to users, but it may simply be informative, providing them with unbiased, pertinent information.

Third, the word “decisional” is significant. Much of the meta-support available today helps users with the mechanics of operating a system’s features, often a matter of knowing when to push which buttons. In contrast, decisional guidance helps users deal with the decision-making concepts involved in choosing among and interacting with a system’s information-processing capabilities. For example, while a “mechanical” help screen might simply list each available option and how to invoke it, decisional guidance might identify the strengths and weaknesses of each alternative.

Lastly, the definition divides decisional guidance into two classes based upon the locus of its effects. Guidance for structuring the decision-making process affects how users choose which operators to invoke and the order in which to invoke them. Guidance for executing the process affects how decision makers perform the evaluative and predictive judgments necessary when executing the chosen operators.

Decisional guidance can be viewed from two perspectives. From one viewpoint, it is an opportunity to design better DSSs by introducing a new class of mechanisms into our systems. From the other, it is a system attribute that helps us understand better how DSSs affect the decision-making behavior of their users. The next two sections adopt primarily the first viewpoint, considering the design questions of when designers should, and how designers can, deliberately include guidance in a DSS. The following section, which examines the consequences of decisional guidance, reflects both perspectives because studying the effects and effectiveness of guidance is important both for improving design and for understanding better how DSSs affect decision making.

## Providing Decisional Guidance: When and Why

What do we know today about whether a system's designer should build decisional guidance into a DSS? Let us consider the opportunities, the motives, and the means for doing so.

## Opportunity: are there significant occasions for providing guidance?

A prerequisite for providing decisional guidance is having the opportunity to do so. Not all DSSs present many or significant occasions for users to make discretionary judgments. In the absence of such judgmental situations, the opportunities for offering decisional guidance are minimal. That is, decisional guidance may have little or no role in a simple system whose use entails limited user discretion.

Since the opportunity to provide decisional guidance arises when users need to make discretionary judgments, how much decisional guidance a system can provide depends, in part, on how much discretion that system grants its users. More specifically, decisional guidance interacts with another system attribute, “system restrictiveness” (Silver, 1988a), which is the way a DSS limits its users’ decision-making processes. Very restrictive systems are not likely to have very much decisional guidance. For instance, if a system supports few decision-making processes, then the opportunities for guiding process structuring are minimal. Similarly, if a system’s operators (functions) require few judgmental inputs from their users, then the occasions for guiding predictive and evaluative judgments are limited. In general, the more restrictive a DSS, the less the opportunity for providing guidance. Consequently, the interaction between restrictiveness and guidance leads to a design trade-off: For each judgmental opportunity, the designer must decide whether to restrict the decision-making process, to guide it, or to do neither.

## Motive: why should a system guide?

Given the opportunity, what are the reasons for or against providing decisional guidance? One can easily identify two sets of issues that affect the desirability of providing guidance: concerns about supporting decision makers and concerns about influencing them. Each set of concerns can create a significant motive for providing decisional guidance but can also bring forth reasons for not doing so.

## Supporting Decision Makers

One motive for providing decisional guidance is to build a more supportive DSS, one that helps users exercise judgment as they interact with the system and confront its complexities. As the frequency, complexity, and importance of the judgments demanded from them increase, decision makers may require—or, at least, desire—computer-based facilities that provide meta-support for the judgments they must make. The greater the needs of decision makers for this added support, the greater the motivation for providing guidance.

The need for decisional guidance is a function of both the system and its users. In general, the more complex a DSS and the less structured its users' perceptions of the decision-making task, the greater the need for guidance. More specifically, we can hypothesize that a number of factors contribute to the need:

\- Some users require guidance more than others. Novices at making a given type of decision require more guidance than those who have confronted similar decisions many times in the past. Infrequent users of a DSS require more guidance than frequent users.

\- The greater the degree of structure either inherent in the task or perceived by the decision maker, the less the required guidance. In particular,

\- Organizational environments that promote standard solution techniques need less structural guidance from their DSS.

\- Environments with well-defined objectives need less assistance in performing evaluative judgments.

\- Organizations facing less uncertainty and risk need less guidance for making predictive judgments.

\- Systems composed of many high-level operators have different needs for guidance than those with predominantly low-level primitives. When a system has many high-level operators, the need for guidance is to help choose among competing solution techniques or among alternative methods of processing information. In contrast, when most operators are low-level primitives, guidance is needed to enable decision makers to form an appropriate decision-making process from these operators.

Although motivated by the objective of supporting decision makers better, decisional guidance may sometimes have the opposite effect. For example, decisional guidance might overload users with information, making the system more difficult and time-consuming to use. Similarly, the guidance mechanisms may themselves make the system more complex, hence, more difficult to learn and operate.

## Influencing Decision Makers

Wanting to influence users' decision-making behavior can motivate designers to provide decisional guidance, such as when a system serves as an agent for directed change (Silver, 1990). While the system allows its users to do as they please, the guidance can serve as a vehicle for encouraging given behavior. The objective may not be to point decision makers toward specific decisions but to influence the way they reach a decision. For instance, Elam and Mead (1987) suggest that a DSS whose purpose is to enhance creativity should provide feedback with "depth and positive tenor" to encourage prolonged alternative generation and delayed judgment. Such feedback could be in the form of decisional guidance.

We can hypothesize that many of the reasons for influencing decision makers are the same as those for building more restrictive DSSs (Silver, 1988a):

• To prescribe a given process or approach,

• To proscribe a given process or approach, or

• To foster structured learning.

Indeed, any decision-making process that can be imposed on users via a restrictive DSS might instead be recommended to decision makers by way of decisional guidance. For instance, to cause decision makers to refine their budget projections to bring deficits immediately into balance, the budget balancing operator could be the only one suggested after a deficit is projected.

That decisional guidance might influence decision makers' behavior is also a reason for excluding it from a system. If a system's objective is not to influence behavior, then fear of inadvertently biasing decision makers or unintentionally reducing their freedom might argue against providing decisional guidance.

## Means: can decisional guidance be implemented?

Given opportunity and motive, providing decisional guidance also depends on having the means to do so. Ironically, those systems offering the greatest opportunity and motivation may be the ones for which presenting meaningful guidance is the most problematic. For instance, in situations where DSS users are unclear how to proceed and need decisional guidance, DSS designers may be equally unclear how to guide them. Builders may find that incorporating many functional capabilities into a system is much easier than guiding a decision maker concerning their use.

Much of the difficulty follows from trying to provide guidance that is both context-sensitive and of high quality. If a system is to provide meaningful assistance to users deciding what to do next, that assistance must reflect what they have done already. Similarly, if a DSS provides meaningful assistance to users responding to questions, that assistance needs to reflect how they have responded to earlier questions. A complex, minimally restrictive DSS that allows its users to follow many paths and to choose among numerous options in arriving at a decision might present an excellent opportunity for decisional guidance, but the number of distinct contexts requiring support is vast. Imagine trying to anticipate so many different situations and produce well-suited guidance for each.

Creating the content of the decisional guidance is only part of the problem. Means must also be constructed for delivering that guidance to the user. Although creating the guidance may be the more difficult task, tracking user behavior and ensuring that context-sensitive messages are presented at the appropriate junctures in the process are also not easy endeavors.

For many systems today, providing meaningful decisional guidance may not be feasible because our knowledge of the means for constructing and delivering such guidance is limited. The prototype systems discussed later in this article, however, represent significant steps toward overcoming these barriers. As needed research proceeds on both the development and delivery fronts, the range of systems for which we are able to provide guidance should expand.

## The research agenda

The foregoing analysis suggests that not all systems may be candidates for decisional guidance. Very simple systems may not present opportunities for offering decision makers meaningful guidance, whereas very complex systems may not be feasible for including guidance. Between these extremes, however, we find a significant middle range of systems for which decisional guidance might be appropriate. We need to understand better whether or not it should be provided in a given situation. Among the more prominent research questions are the following:

\- When are decision makers' needs for guidance greatest? How great is the risk of degrading support by overwhelming users with too much guidance?

\- When should a DSS designer act as an agent for directed change, using decisional guidance to influence the decision maker?

\- Are there other motives for providing decisional guidance?

\- When is it best to accomplish design objectives by restricting decision makers, by guiding them, or by doing neither?

\- Given the difficulty of providing guidance, when does the cost of providing guidance exceed the benefits?

Some of these questions are ready for immediate investigation, but most depend on another set of research issues:

\- What are the effects of decisional guidance, both inadvertent and deliberate, on decision-making behavior?

\- How effective is deliberate guidance at accomplishing its objectives?

Clearly, the effects of deliberate guidance are relevant for deciding whether to build decisional guidance into a system. But the effects of inadvertent guidance matter, too, because deciding whether or not to provide guidance is essentially a choice between accepting the effects of inadvertent guidance and opting to guide deliberately. Indeed, trying to offset inadvertent guidance effects may be the reason for choosing to guide deliberately.

Studying the effects and effectiveness of decisional guidance depends on yet another set of research issues:

\- What are the means for providing decisional guidance? What kinds of decisional guidance can designers build into a system? What is the content of the guidance? How do the guidance mechanisms operate?

These issues are the questions addressed in the next section, and the consequences of guidance are returned to in the section after that.

## How Can Designers Build Guidance into a DSS?

Having considered the reasons and conditions for guiding, it is necessary to discuss the substance of the guidance itself. In this section, a three-dimensional typology of the ways that designers can build guidance into a DSS is presented. The typology, outlined in Table 3, is derived from analyses and extrapolations of approaches to decisional guidance proposed in the literature. Each dimension distinguishes types of guidance by posing a different question:

\- What is the target of the guidance? That is, what distinct aspect of decision making does the guidance enlighten or sway?

\- What is the form of the guidance? That is, what does the guidance offer decision makers that might enlighten or sway them?

\- What is the mode of the guidance? That is, how does the guidance mechanism work?

Targets of guidance: structuring and executing the process

To study the content of guidance, we must begin by identifying what is being guided. What do decision makers do with a DSS that could benefit

## Table 3. A Typology of Deliberate Decisional Guidance

Targets (which aspects of decision making the guidance addresses)

\- Structuring the Decision-Making Process (Choosing Operators)

\- Executing the Decision-Making Process (Using Operators)

Forms (what the guidance offers decision makers)

\- Suggestive Guidance

• Informative Guidance

Modes (how the guidance mechanism works)

\- Predefined

\- Dynamic

\- Participative

from decisional guidance? What judgmental activities can we aim to support?

We can distinguish two aspects of decision making: structuring and executing the decision-making process. Structuring the process involves selecting a problem representation and then defining and ordering the set of information-processing and problem-solving activities to be performed. Structuring the process can be seen as deciding how to decide, an activity that goes by many names: meta-choice (Kleindorfer, et al., 1991), meta-decision (Mintzberg, et al., 1976), predecision (Wedley and Field, 1984), secondary decision (White, 1975), and strategy selection (Beach and Mitchell, 1978). Executing the process entails actually performing the various information-processing and problem-solving activities.

For example, in a multi-attribute problem such as buying a car, renting an apartment, or choosing a college, structuring the process might be accomplished by deciding to use a conjunctive elimination rule to reduce the set of alternatives and then to employ a scoring method to select a winner. Once this meta-choice is made, the process is executed and the decision made by performing the elimination and running the scoring model.

Each of these aspects of decision making, structuring and executing the process, requires human judgment; each can be the target of guidance.

## Structuring the decision-making process

Guidance for structuring the decision-making process is support for meta-choice, often the most difficult and critical activity in solving a problem. Sometimes the challenge is to choose among competing techniques, such as the many methods proposed for solving multi-attribute problems or the numerous models developed for forecasting time series. Other times, problems are less-structured, and the task is to combine an amorphous set of capabilities into a coherent approach for reaching a solution. In either situation, the system can guide its users in selecting and combining system functions. As systems become increasingly complex, with more operators, models, and data sets, such guidance becomes increasingly important.

Supporting meta-choice means more than just guiding users as they navigate through a complex system. It means helping users answer the decisional questions they confront when selecting capabilities. Given a specific multi-attribute problem, for instance, should a serial approach be used, where solutions are generated and evaluated one at a time, or should a parallel process be employed, where a set of competing alternatives is generated and evaluated as a whole? If the parallel approach is adopted, should a compensatory or non-compensatory rule be used to choose among the alternatives? Providing such guidance is not easy; it requires knowledge of the decisional properties of operators and the decisional relationships among them.

Decision makers' needs for guidance may be expressed in general or specific terms. At a general level, decision makers must find an approach to solving their problem. More specifically, decision makers may need help choosing operators. They must decide what to do next, or, if they are just starting out, what to do first. This problem raises two questions for a decision maker: What do I need an operator to do, and which of several competing operators should I use to do it? For example, should I begin with a forecast, a graph of historical data, or a tabular display of my current position? Then, if I elect forecasting, which of a dozen different extrapolation methods should I use?

## Executing the Decision-Making Process

However difficult and important it may be, constructing the decision-making process is only one step toward reaching a solution. The chosen solution method must be executed. Here, too, decisional guidance has a place. The same DSS operators whose outputs (data displays, modeling results, statistical analyses, and graphic representations) support human judgment often require human judgments as inputs. The judgments might be predictions of future conditions (inflation rates, unemployment rates, sales, droughts, strikes, and so forth) or evaluations of preferences (acceptable profit levels, desirable warehouse locations, and trade-offs between costs and benefits, among others). A DSS might simply prompt users for these inputs, or it might guide users as they make the necessary judgments.

Consider a DSS that supports the elimination by aspects process. A simple system might prompt users to enter attributes and acceptable ranges for their values, producing a list of those alternatives satisfying the specified criteria. Although the system aids decision makers by performing the necessary database searches, it does not participate in the critical judgmental tasks of choosing and ordering attributes and defining acceptable ranges. Another system might provide such decisional guidance.

## Forms of guidance: suggestive versus informative

We are now prepared to ask, "What can guidance offer decision makers?" The answer: decisional guidance can support users in two very different ways. Suggestive guidance makes judgmental recommendations (what to do, what input values to use) to the decision maker. In contrast, informative guidance provides pertinent information that enlightens the decision maker's judgment without suggesting how to act. A DSS may contain instances of both forms of guidance.

In fact, at any point of judgment, a system may offer suggestions, pertinent information, or both.

## Suggestive Guidance

As its name suggests, “suggestive guidance” recommends how users can respond to the judgmental opportunities they encounter. For structuring the decision-making process, such guidance recommends which operators and inputs (data and models) to use. Recommendations might be a single operator (“use linear regression”), a small set of operators (“use linear regression or discriminant analysis”), or a rank-ordered list of operators (“linear regression is your best option, otherwise use discriminant analysis”). Alternatively, the DSS might recommend not using certain operators.

For executing the process, suggestive guidance recommends parameter and other input values. The DSS might recommend a specific value (“set the inflation rate to 4.2 percent”), a set of (ordered or unordered) values (“set the inflation rate to 4.2 percent, 4.8 percent, or 5.4 percent”), or a range of values ("set the inflation rate between 4 percent and 5 percent"). The guidance might also advise against using certain values.

The left-hand side of Figure 1 summarizes the types of suggestions just enumerated. The DSS literature describes a number of examples of these kinds of suggestive guidance:

Lee, et al. (1985) propose a “third generation multiple criteria decision support System” (3G-MCDSS), one of whose purposes is to guide decision makers in choosing among different approaches to solving multi-objective problems. Their prototype, which contains 13 techniques for generating solutions to multi-objective problems, embeds a small expert system that suggests a technique based on a combination of user responses to specific questions (for instance, “Do you want to reach the final solution iteratively?”), information about the problem already supplied by the user, and rules predefined by the system’s designers.

Form of Guidance

<table><tr><td rowspan="2">Target of Guidance</td><td>Suggestive Guidance</td><td>Informative Guidance</td></tr><tr><td>Recommended operatorSet of recommended operatorsOrdered list of recommended operatorsSet of operators not recommended</td><td>Description/analysis of operatorsComparison of operatorsMap of relationships among operatorsRecord of behavior in similar contextsHistory of activity this session</td></tr><tr><td>Structuring the Process</td><td></td><td></td></tr><tr><td>Executing the Process</td><td>Recommended valuesSet of recommended valuesOrdered list of recommended valuesSet of values not recommended</td><td>Definitions of required input valuesDescriptions of how inputs will be usedTables, graphs, or analyses of dataRecord of behavior in similar contextsHistory of activity this session</td></tr></table>

Figure 1. Examples of Decisional Guidance

Wedley and Field (1984) describe a “predecision support system” that helps users structure their decision making by suggesting decision styles, solution methods, and participants. The system asks its users as many as 10 questions about their problem before recommending one or more sets of styles, methods, and participants.

Kobashi (1984) observes that some computer-based decision aids for multi-attribute problems march users step-by-step through the multi-attribute utility approach. Noting that experienced decision makers might benefit from more flexibility in interacting with the system and data, he proposes a decision aid that allows all users more freedom in interacting with the data table but also makes suggestions to help novice users determine what to do next.

Collopy and Armstrong (1989) consider the meta-decision of choosing a forecasting technique for extrapolating time series data. Statisticians have proposed numerous forecasting methods, and studies (Hogarth, 1979; Lopes, 1983; Makridakis et al., 1982; Makridakis and Hibon, 1979) have found that the relative accuracy of the methods depends upon the interaction of the method with the series being forecast. Collopy and Armstrong used interviews and protocol analysis to develop an expert system for choosing which method or weighted combination of methods to use for a given time series. Within a DSS that supports many extrapolation techniques, one might embed their system as a “mini-expert” that provides suggestive guidance on which forecasting technique(s) to employ for a given set of data.

Stabell (1983) uses the term “decision channeling” to refer to the property of systems that “serves to both support and shift the decision process” (p. 251). Although Stabell uses the term to refer to features of the interface architecture, channeling can also be accomplished through suggestive guidance. The system would give users a choice of using features consistent with the old or new decision-making approaches but would recommend those favoring the new one.

## Informative Guidance

Without offering suggestions, informative guidance provides decision makers with pertinent information that enlightens their judgment and use of the system. Help screens are usually informative in nature, describing the available options without recommending any one of them. Most help screens we find today, however, do not offer decisional guidance; they provide only information about the mechanics of choosing among options. The important question to ask, then, is what information could be provided that would help users with the judgments involved in making their selections?

For structuring the process, detailed analyses of the operators, including their advantages and disadvantages, might be pertinent information. Although currently less common than descriptions of individual operators, comparisons of operators with respect to their decisional properties can be particularly helpful. For example, if a user must select one of several choice rules, he or she could be informed of which rules are compensatory and which are not.

For systems having complex relationships among their operators, users might be given a “map” showing how the operators are related. For instance, such guidance could address the following questions: Which operators are logically consistent so that they can be used as part of the same coherent decision-making process? Which operators are substitutes? What are the precedence relationships that control the logical order in which operators are used?

For executing the process, informative guidance might include clear definitions of the required input values and descriptions of how the operators will use them. Tables, graphs, or statistical analyses of relevant data are also useful references for decision makers choosing input values for operators.

For both structuring and executing the process, a history of how the user—or other users—behaved in similar contexts can be provided. Knowledge of what was done on previous occasions might motivate a user to behave in either the same or a different way in the current instance. The history would be even more informative if it included an indication of the concomitant outcomes; this more complete history might lead to different user behavior. Along the same lines, decision makers might be given a record of the path they traversed to reach their current location in the system. Knowing which operators they invoked and input values they supplied might influence their judgments on which operators and input values they should use next.

The right-hand column of Figure 1 summarizes the types of pertinent information just described. The DSS literature also reports on a number of examples of informative guidance:

Studer (1983) describes an adaptable DSS interface that supports selecting suitable operators for a given purpose, constructing more complex operators from those the system offers, and executing operators. Central to his approach is the concept of an “application model,” which provides a graph-based description of the structure of a problem and the operators that can be used to solve it. In particular, the model identifies the relationships among components of the problem as well as those among different operators. The interface allows users to navigate through the graphs as a way of seeing the application’s structure and the operators available (navigation mode), to acquire detailed information about components of the application (information mode), to execute the operators and specify input data (execution mode), and to create complex operators from more basic ones (operator definition mode). Each of these modes guides users by enlightening either their choice or their use of operators.

Brennan and Elam (1986) identify a number of ways in which the modeling components of DSS are currently deficient, including their inability to help users uncover possibly interesting future analyses. Among the enhanced capabilities Brennan and Elam propose is a generalized form of sensitivity analysis that might address “[w]hat to do next” by providing “clues as to interesting or important changes to the model structure or parameters” (p. 136). Such clues constitute informative guidance for structuring the decision-making process.

## Modes of guidance: predefined, dynamic, participative

Speaking glibly about systems guiding their users with suggestions and pertinent information is easy. But how is the guidance generated? How do the guidance mechanisms arrive at the suggestions they offer the decision maker? How do they determine what information is pertinent for the judgment at hand? In short, how do the guidance mechanisms work?

Guidance mechanisms operate in one of three modes: predefined, dynamic, or participative. In the first case, the designer predefines the specific suggestions or the particular information displays and builds them into the guidance mechanism. In the other two cases, the designer constructs the guidance mechanism only; the mechanism then generates the suggestions and informational displays either itself by learning dynamically over time or with the active participation of the decision maker.

## Predefined Guidance

A guidance mechanism is referred to as pre-defined when the system designer prepares a set of recommendations or informational displays and embeds these directly into the system. The suggestions and information might be based upon the designer's own preferences, upon preferences of the client who commissioned the system, or upon normative views of experts and others who have studied the problem. For instance, given several options for graphing historical sales data, a designer might recommend a graph he or she finds especially useful, a graph the client is known to prefer, or a graph consistent with research findings on information display. Whatever his or her rationale, the designer has predefined the substantive content of the guidance. The help screens found in many systems today, for example, are mechanisms that typically function in this mode (although the guidance they offer is more “mechanical” than “decisional”).

Predefining the content of guidance does not necessarily mean that the same recommendations and information are always given. The designer may need to anticipate the various contexts that may occur, prepare guidance for each, and create a mechanism that displays the appropriate predefined message in each context. Taken narrowly, context might be defined by the set of options the user confronts; taken broadly, context would include the path the user traversed to reach this set of options. In this case, the mechanism must track user behavior to determine the context and display the appropriate guidance.

Consider a simple example, a DSS organized by a main menu containing several operators. After an operator is executed, the user is always returned to the same main menu. Designers might predefine context-sensitive guidance that suggests which operator to use next, given which one was used last. Designers might predefine guidance that encourages users to try each operator, a different one on each iteration. Or they might predefine guidance that suggests running the same operator repeatedly, systematically varying its inputs.

Just as contextual information may be needed to determine which predefined guidance to present, some interaction with the user may be required to resolve which suggestions to make or information to display. The designer may embed logic in the guidance mechanism that asks the user key questions and then, based on the user's responses, presents the appropriate guidance.

We have already encountered examples of such guidance mechanisms. Lee, et al.'s (1985) 3G-MCDSS asked users as many as 13 questions as the basis for suggesting a multi-objective method. Wedley and Field's (1984) predecision support system asked users as many as 10 questions to derive suggested styles, methods, and participants. In each system, designers predefined the logic that determined what would be suggested. But this logic required responses from the users.

## Dynamic Guidance

By constructing adaptive mechanisms that "learn" as the system is used, designers can build decisional guidance into a DSS without predefining its content. The suggestions offered and information displayed are generated by the mechanism dynamically, not by the designer in advance. A number of approaches have been proposed for developing these dynamic guidance mechanisms:

Fjelstad and Konsynski (1986) describe the spreadsheet manager to illustrate how cognitive responsibilities can be “reapportioned” from the user to the system. Among its capabilities, the system assists users in selecting appropriate spreadsheet models or templates by guiding them through a structured query. To users, this guidance appears much the same as that offered by the 3G-MCDSS and the predecision support system. A distinctive feature of the spreadsheet manager, however, is that the knowledge base underlying the content of the guidance is not predefined by the designer but is constructed dynamically by the system as its resources evolve—that is, as new spreadsheets are added to the model base or as existing spreadsheets are applied to new problems.

Liang and Jones (1987) propose a design for a self-evolving DSS, where the system records and analyzes user behavior to reset default policies and default values automatically in a way that optimizes some performance measure. In their example, the system tracks whether decision makers use sensitivity analysis and which visual representation (bar chart, line chart, or table) they prefer. Based on the objective of minimizing expected user effort, the system derives default policies for these two options.

Liang and Jones's approach, intended to manage system defaults, can be applied to generating decisional guidance dynamically. The system can track user selections but, instead of resetting defaults, it can suggest that users select what they have selected most recently or most often. Or, the system might recommend the option selected most often by some other user or by the full set of users. In contrast, the DSS might recommend an option the user systematically overlooks. If the DSS were also able to track outcomes, it might recommend the options that have been associated with the best performance in the past. As an alternative to these kinds of suggestive guidance, a DSS might analyze system use and display the analysis, without a recommendation, as informative guidance.

Manheim (1988) uses the term “active” systems to refer to DSSs that provide decision makers with support independent of explicit user direction. He calls the subset of these systems that maintain a model of the user’s cognitive processes to engage in a user-machine partnership “symbiotic” systems. His architecture for building symbiotic systems includes components for both user-directed and computer-directed information processing.

We can regard a DSS having decisional guidance capabilities as a special—perhaps limited—case of an active system. More importantly, components of the symbiotic architecture can be useful for generating and delivering guidance. In a symbiotic DSS, a “history recorder” tracks all processing, noting, in particular, which input data generated which outputs. Based on a schematic model of human problem-working processes, a "history inference processor" maintains an up-to-date representation of the user's image of the problem. In terms of the architecture, this representation is the basis for directing the computer to process information without explicit human involvement. But the recorder and inference processor also seem ideal for generating informative and suggestive guidance. Indeed, Manheim notes that the architecture can "provide information potentially useful to the user" (p. 363) and "make suggestions to the user about things she should consider doing" (p. 361).

## Participative Guidance

Both predefined and dynamic mechanisms generate guidance with little direct input from, and no direct control by, the user. But designers can devise mechanisms where users participate heavily in determining the content of the guidance they receive. These participative guidance mechanisms facilitate users' deriving their own recommendations or defining for themselves the information they need.

Suggestive guidance for meta-choice offers a good illustration. Consider a decision maker choosing among operators that serve the same purpose. Perhaps these are choice rules, forecasting techniques, or solution generators. A DSS can support the decision maker's meta-choice by providing a list of these operators and their associated properties. For instance, Kleindorfer, et al. (1991) suggest that in different situations, different “legitimation criteria” are appropriate for justifying the choice of a problem-solving technique. In some situations, optimality may be the dominant or only criterion, whereas in others, understandability, defendability, simplicity, and accuracy may play important roles. Moreover, different problem-solving techniques may be justified by different legitimation criteria. A linear program might rate high when judged in terms of optimality and accuracy but not in terms of understandability and simplicity. A table, such as Table 4, which rates the problem-solving techniques with respect to legitimation criteria, could therefore guide decision makers.

By itself, the table offers predefined, informative guidance. When functions are added that empower users to manipulate the table (by rank ordering the techniques or selecting one of them), the enhanced table becomes a participative, suggestive guidance mechanism. Compare it with predefined, suggestive guidance; the balance of responsibility for generating suggestions has shifted from the designer to the user. In the 3G-MCDSS and the predecision support system, the logic underlying the suggestions was predefined by the designers, with answers to some questions provided by the user; here, the designer provides some functionality and basic information, but the user determines how it is applied to generate suggestions. The balance can be shifted still further

Table 4. An Example of Using Legitimation Criteria in Decisional Guidance

<table><tr><td rowspan="2">Operators</td><td colspan="5">Legitimation Criteria</td></tr><tr><td>Optimality</td><td>Understand-ability</td><td>Defendability</td><td>Simplicity</td><td>Accuracy</td></tr><tr><td>Operator “A”</td><td>5</td><td>3</td><td>7</td><td>3</td><td>4</td></tr><tr><td>Operator “B”</td><td>4</td><td>3</td><td>8</td><td>8</td><td>6</td></tr><tr><td>Operator “C”</td><td>9</td><td>5</td><td>3</td><td>4</td><td>6</td></tr><tr><td>Operator “D”</td><td>8</td><td>8</td><td>8</td><td>2</td><td>7</td></tr></table>

Notes: In this example, “A,” “B,” “C,” and “D” are the names of the DSS’s operators. In an actual DSS, these might be “Multi-Attribute Utility,” “Elimination by Aspects,” “Lexicographic Sort,” “LP Solver,” “Regress,” “Project,” and so forth.

The numbers in the cells rate each operator with respect to each criterion. In this example, the scale is from 0 to 10.

by increasing the user's participation in defining the table (being able to add techniques, add legitimation criteria, or change ratings).

Some concluding comments motivated by the three modes of guidance are in order. First, because guidance frequently must be context-sensitive to be meaningful, even predefined guidance mechanisms can become quite complex. Second, although designers build the guidance mechanisms, they do not necessarily define the substantive content of the guidance the user receives (the specific suggestions or information), which may be defined dynamically or participatively. And lastly, guidance need not be a message or display that the system simply hands to the user; it may follow from active user participation.

## The research agenda

In this section, a three-dimensional typology of how designers can build guidance into a system has been presented. Taken together, the targets (structuring and executing the process), forms (suggestions and information), and modes (pre-defined, dynamic, and participative) define a dozen types of guidance. An important research task that follows naturally from this analysis is to develop guidance mechanisms of the various types. For designers, the mechanisms may be useful candidates for inclusion in their systems. And for researchers, the mechanisms represent tangible artifacts that can be studied.

In contrast with the individualistic, haphazard style of the past, development must now be approached systematically. The motives for developing guidance mechanisms are the same as those for guiding, so each development project should focus on a particular motive, enabling a set of mechanisms to be accumulated for each. The typology described in this article can further organize development efforts. Concentrating initially on a single type or on relatively few types of guidance might be fruitful. That way, it is possible to develop and compare a variety of mechanisms all with the same basic characteristics (same motives and types).

Another research task is to consider the behavioral consequences of each type of guidance, understanding their effects on decision-making behavior and their effectiveness at accomplishing design objectives. This topic is addressed in the following section.

## The Effects and Effectiveness of Decisional Guidance

If decisional guidance is seen as an opportunity to design better DSSs by introducing a new class of mechanisms into systems, then these mechanisms must certainly be evaluated to determine their effects on behavior and their effectiveness at accomplishing their objectives. And if decisional guidance is thought of as an attribute of the system, then studying the effects of guidance is part of the broader issue of studying how DSSs affect decision making. So, from either perspective, evaluating the consequences of decisional guidance is an important research task.

The effects of deliberate and inadvertent guidance must each be studied differently. For deliberate guidance, one focuses on the mechanisms designed specifically to guide. For inadvertent guidance, however, one looks at all the other system components—the functional capabilities and the interfaces to them—to see how users might be swayed unintentionally.

## Inadvertent guidance

Do DSSs really guide inadvertently? Behavioral decision theory suggests that they may. Numerous studies (see Hogarth, 1980, or Sage, 1981, for reviews) have found that limitations of human information-processing capabilities may lead to systematic biases in how people acquire and process information. By fostering such systematic cognitive biases, a system's features—say, its interface or functional capabilities—may inadvertently sway users' judgments. For example, not only might the order effects of menu items bias users' selections, but the common practice of highlighting the item chosen the last time a menu appeared may reinforce people's heuristic bias to rely on habit in decision making. The cognitive biases reported in the literature may shed light on how DSSs guide inadvertently, but if so, they also present a mammoth challenge. Sage enumerates no fewer than 27 such biases. Trying to uncover all the ways that DSSs guide inadvertently seems to be a formidable, albeit important, endeavor.

Studying the inadvertent effects of DSSs on users' judgmental inputs has significant implications for DSS design. If DSS designers understand how and when such guidance can occur, they can take steps to avoid the unintended consequences, perhaps by offsetting them with deliberate guidance. And, of course, studying the inadvertent effects is also central to understanding how DSSs affect decision-making behavior. Were we to concentrate only on systems' intended consequences, we might misunderstand their impacts on decision-making performance.

## Deliberate guidance

We begin by asking what, if any, are the effects of deliberate guidance on decision-making behavior? How does decisional guidance affect the way people use the system and the way they make decisions? Are the consequences of providing decisional guidance positive, negative, or neutral, as seen from the perspectives of the decision maker, the system designer, and the organization? More specifically, consider the following research questions:

\- When do decision makers find decisional guidance useful and when do they find it bothersome?

\- When decision makers say they find decisional guidance useful, how do they use it? Does the guidance affect the operators and tools they select or the responses they enter?

\- How do decision makers process the information provided by informative guidance? How do they react to the recommendations made by suggestive guidance? In particular, do they recognize that such recommendations are not requirements?

\- Does decisional guidance affect how much time the decision maker spends using a system? Does guidance make a system easier to use? Does increased ease of use translate into increased frequency of use?

\- When and how does decisional guidance bias decision makers? When are such biases desirable and when are they deleterious?

\- And the bottom line: When does decisional guidance improve decision-making performance and when does it degrade it?

Beyond answering questions such as these about the full set of guidance's effects, we need to study the effectiveness of decisional guidance in achieving its objectives, such as being more supportive of decision makers or influencing their decision-making behavior. Does guidance succeed in accomplishing the objectives that motivate it? Does guidance cause negative side effects that may offset the benefits it produces? More specifically:

\- How effective is each form of guidance at accomplishing each objective? We might expect that informative guidance would be most effective at supporting decision makers and suggestive guidance at influencing them. Is this so? Can carefully constructed informative guidance influence decision makers effectively? Can suggestive guidance make the DSS more effective at supporting decision makers?

\- How effective is each mode of guidance (predefined, dynamic, and participative) at accomplishing each objective (supporting and influencing the decision maker)? Does mode interact with form of guidance (informative versus suggestive) or with target of guidance (structuring versus executing the decision-making process)?

\- Can decisional guidance debias decision makers exhibiting systematic cognitive or motivational biases? What are the risks of trying to do so?

\- When do the costs of learning the guidance mechanisms exceed the benefits of using them?

Trying to address these two collections of research questions broadly is premature at this time. Given the many variations in the content of decisional guidance and the motives for providing it, generalizing across all types of decisional guidance, or even all instances of a given type, is not now feasible. We need, instead, to approach these questions in a bottom-up fashion.

We could begin with individual guidance mechanisms, studying their effects—both good and bad—and their effectiveness, while systematically varying user and task characteristics. We could then take a collection of mechanisms, all of the same type or all serving the same purpose, and compare them with respect to their effects and effectiveness. After significant work along these lines, we might be prepared to generalize across mechanisms, drawing conclusions about specific types of guidance or contrasting different types of guidance. Then ultimately, perhaps, we may reach some global conclusions about the effects and effectiveness of decisional guidance.

Can anything be said, a priori, about the likely effects of decisional guidance? Behavioral decision theory may again offer insights. On the one hand, a guidance mechanism might foster cognitive biases, in which case the effect would be to bias users' judgments systematically. On the other hand, a guidance mechanism might debias—that is, it might reduce or eliminate the effects of systematic biases—in which case, the guidance leads to less-biased judgments. Consider a few examples:

\- Informative guidance may present decision makers with information, in a unified and readily accessible form, for which they would otherwise have to search sequentially. Such guidance might reduce the “availability,” “selective perception,” and “confirmation” biases that lead to decision makers not acquiring or not weighting appropriately all relevant information. But the guidance might promote other biases that follow from order effects in the presentation of the information, from the mixing of quantitative and qualitative data, or from decision makers relying too greatly on the guidance to the exclusion of other relevant information.

\- Decision makers who are asked to predict a series of values, say the Dow-Jones closing average for each of the next ten weeks, often do so by beginning with a given point—an anchor—and adjusting it to create the remaining elements of the series. When using this “anchoring and adjustment” heuristic, decision makers often fail to adjust sufficiently; their predictions tend to be too close to the anchor. On the one hand, informative guidance might foster such biases by making such anchors (in the form of historical data) readily available. On the other hand, suggestive guidance might warn the decision maker of this bias and attempt to push him or her further from the anchor.

\- Decision making is often strongly influenced by habit. If we make a decision in a given way once and the results are acceptable, we may use the same approach repeatedly in the future without studying whether this is in fact the best way to proceed. Providing guidance that simply reminds users of their selections on previous occasions, therefore, might foster such a bias. Providing users with more detailed analysis of and feedback on these decisions, however, might offset the bias of relying on habit.

The examples show that, based on what we know about human information processing, arguments can be constructed for both types of effects. Each type of guidance and each specific guidance mechanism must be studied empirically to arrive at a conclusion.

## Summary

From both perspectives—that of designing DSS and that of understanding them—studying the consequences of decisional guidance is the critical item on the research agenda. From the design perspective, the other two principal research issues depend on this one. Knowing when to provide guidance hinges on understanding the potential effects and effectiveness of guidance; developing successful guidance mechanisms relies on feedback from evaluating the performance of guidance mechanisms. From the perspective of understanding how DSSs affect decision-making behavior, studying the consequences of decisional guidance is the principal research question.

## Conclusion

In this article, many illustrations of decisional guidance from the recent DSS research literature are presented. Some describe prototype systems, while others describe concepts waiting to be implemented. Some are technology-driven ("How can I apply expert systems to DSS?"); others concentrate on a given problem domain. Only a few address the more general issue of supporting judgmental activities without being limited to a specific technology or domain.

At first glance, the examples in the literature seem to have little in common. They use different terminology, cite different references, rarely cite one other, and concentrate on different domains. Yet, they have a great deal in common. They are all instances of decisional guidance, all attempts to provide meta-support for the various judgments that users of decision support systems must make. As technology advances further, we can expect to see even more research along these lines.

Each of these research efforts individually and the field of computer-based decision support as a whole would benefit from an integrated approach to addressing these issues. We could then compare results, build a cumulative knowledge base of guidance techniques, and study the trade-offs among the various kinds of guidance. The means of creating and delivering meaningful, context-sensitive guidance could be developed more rapidly, and a better understanding of how DSSs affect decision making could be acquired.

The study of decisional guidance is that integrated approach. The foundation and agenda presented here can unite the currently disparate research efforts. Pursued vigorously and systematically, research on decisional guidance can lead to far greater support for decision making.

## Acknowledgments

I am indebted to Lynne Markus, Burt Swanson, Sidne Ward, the associate editor, and the reviewers for their helpful comments on earlier versions of this article.

## References

Beach, L.R. and Mitchell, T.R. "A Contingency Model for the Selection of Decision Strategies," Academy of Management Review (3:3), July 1978, pp. 439-449.

Brennan, J.J. and Elam, J. "Enhanced Capabilities for Model-Based Decision Support Systems," in Decision Support Systems: Putting Theory into Practice, R.J. Sprague, Jr. and H.J. Watson (eds.), Prentice-Hall, Englewood Cliffs, NJ, 1986, pp. 130-137.

Collopy, F. and Armstrong, J.S. "Toward Computer-Aided Forecasting Systems:

Gathering, Coding, and Validating The Knowledge," DSS-89 Transactions, San Diego, CA, June 12-15, 1989, pp. 103-119.

Elam, J.J. and Mead, M. "Designing for Creativity: Considerations for DSS Design," Information and Management (13:5), December 1987, pp. 215-222.

Fjelstad, O.D. and Konsynski, B.R. "The Role of Cognitive Apportionment in Information Systems," Proceedings of the Seventh International Conference on Information Systems, San Diego, CA, December 15-17, 1986, pp. 84-98.

Hogarth, R. "Discussion of the Paper by Professor Makridakis and Dr. Hibon," Journal of the Royal Statistical Society, Series A (14:2), 1979, p. 136.

Hogarth, R.M. Judgement and Choice, John Wiley and Sons, Chichester, England, 1980.

Kleindorfer, P., Kunreuther, H., and Schoemaker, P. Decision Science: An Integrative Perspective, Cambridge University Press, Cambridge, England, 1991.

Kobashi, Y. "The Use of Suggestions in a Tables-Oriented Decision Aid," Knowledge Representation for Decision Support Systems, Proceedings of the IFIP WG 8.3 Working Conference, Durham, England, July 24-26, 1984, pp. 221-225.

Lee, J.K., Hurst, E.G., Jr., and Lee, J.S. "The Third Generation Multiple Criteria Decision Support Systems," Working Paper 85-04-04, Department of Decision Sciences, Wharton School, University of Pennsylvania, Philadelphia, PA, 1985.

Liang, T.P. and Jones, C.V. "Design of a Self-Evolving Decision Support System," Journal of Management Information Systems (4:1), Summer 1987, pp. 59-82.

Lopes, L.L. "Pattern, Pattern-Who's Got the Pattern?" Journal of Forecasting (2:3), July-September 1983, pp. 269-272.

Makridakis, S., Andersen, A., Carbone, R., Fildes, R., Hibon, M., Lewandowski, R., Newton, J., Parzen, E., and Winkler, R. "The Accuracy of Extrapolation (Time Series) Methods: Results of a Forecasting Competition," Journal of Forecasting (1:2), April-June 1982, pp. 111-153.

Makridakis, S. and Hibon, M. "Accuracy of Forecasting: An Empirical Investigation," Journal of the Royal Statistical Society, Series A (142:2), 1979, pp. 97-145.

Manheim, M.L. "An Architecture for Active DSS," Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences, vol. III, Kona, HI, January 5-8, 1988, pp. 356-365.

Mintzberg, H., Raisinghani, D., and Theoret, A. "The Structure of Unstructured Decision Processes," Administrative Science Quarterly, (21:2), June 1976, pp. 246-275.

Sage, A.P. "Behavioral and Organizational Considerations in the Design of Information Systems and Processes for Planning and Decision Support," IEEE Transactions on Systems, Man, and Cybernetics (SMC-11:9), September 1981, pp. 640-678.

Silver, M.S. "On the Restrictiveness of Decision Support Systems," Organizational Decision Support Systems, Proceedings of the IFIP WG 8.3 Working Conference, Como, Italy, June 20-22, 1988a, pp. 259-270.

Silver, M.S. "Descriptive Analysis for Computer-Based Decision Support," Operations Research (36:6), November-December 1988b, pp. 904-916.

Silver, M.S. "Decision Support Systems: Directed and Nondirected Change," Information Systems Research (1:1), January-March 1990, pp. 47-70.

Stabell, C.B. "A Decision-Oriented Approach to Building DSS," in Building Decision Support Systems, J.L. Bennett (ed.), Addison-Wesley Publishing Company, Reading, MA, 1983, pp. 221-260.

Studer, R. "An Adaptable User Interface for Decision Support Systems," Proceedings of the Sixteenth Annual Hawaii International Conference on System Sciences, vol. I, 1983, pp. 490-499.

Wedley, W.C. and Field, R.H.G. "A Predecision Support System," Academy of Management Review (9:4), October 1984, pp. 696-703.

White, D.J. "Coordinating Paper: The Nature of Decision Theory," in The Role and Effectiveness of Theories of Decision in Practice, D.J. White and K.C. Bowen (eds.), Hodder and Stoughton, London, England, 1975, pp. 3-16.

## About the Author

Mark S. Silver is assistant professor of information systems at the Anderson Graduate School of Management at the University of California at Los Angeles. He received his Ph.D. from the Wharton School of the University of Pennsylvania. his current research interests focus on studying how decision support systems affect managerial decision-making processes and on analyzing the restrictiveness of information systems. Professor Silver has published articles in Information Systems Research, Operations Research, and the Journal of Management Information Systems. he is the author of the forthcoming book Systems that Support Decision Makers: Description and Analysis.
