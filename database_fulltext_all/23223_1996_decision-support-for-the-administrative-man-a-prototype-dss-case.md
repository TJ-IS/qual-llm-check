---
otero_id: 23223
otero_key: "3VQUG774"
title: "Decision support for the administrative man: a prototype DSS case"
authors: "JA Sena; DH Olson"
year: "1996"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.1996.8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for the administrative man: a prototype DSS case

JA Sena $^{1}$ and DH Olson $^{2}$

$^{1}$ College of Business, California Polytechnic State University, San Luis Obispo, CA 93407, USA and $^{2}$ Agder College, Kristansand, Norway

In this paper we focus on the practical and conceptual design factors and implementation features of a prototype decision support system for a typical ‘administrative man’. We discuss the parameters and design principles that we found significant for the creation, inclusion and visualisation of mental models to aid the change management process for a particular manager. In related research we formulated a prescriptive model for this manager. Using this formulation we created a design for the change management subset of the decision maker’s environment. Our goal is to provide a framework that supports decision situations where complexity and vagueness constrain the decision making process.

## Introduction

We view change management to be a multidimensional, time-based process. In the short term, managers must focus on crisis management. To support the handling of crises and opportunities, a manager needs to develop a set of mental models to assist in the ‘what if’ or scenario management deliberation. In the long term, managers need to address the change planning process. This is an ongoing endeavour whereby they integrate historical and current decision cases with current and future planning requirements. Using the change planning and crisis management processes, the manager constructs a set of models for the handling of change; addressing crises and incorporating the mental models for handling and planning of change.

In this paper we discuss the practical design aspects to support the change management process for a particular manager in a dynamic decision making environment. We assert that the design approach we have constructed can be generalisable to decision makers in many organizations.

Mintzberg (1973) provides an extensive perspective on how managers actually behave. Their worlds are characterised by brevity, fragmentation (a number of problems are dealt with during a day, and particular problems get short spans of attention over longer periods) and variety (there is a wide range of problems and decisions).

In our work we employ the term, ‘the administrative man’, to describe how a typical decision maker solves his problems. What behavioural characteristics should we then expect to find? To answer this question, we have adopted the following propositions about the decision maker's behaviour from Wall (1993):

\- Decision making is dominated by the effects of complexity on the limited abilities of humans to process large amounts of information. Thus, information processing tends to be parsimonious, and solutions are simple-minded.

\- New solutions are synthesised by modifying the current implemented one; so search is local.

\- Alternatives are considered one at a time, not simultaneously, so search is sequential.

\- The search for a new and better solution is undertaken only when it is deemed necessary; when it is observed that goals are not being met.

\- A satisfiable mode is used in searching; the first solution that is ‘good enough’ is implemented.

\- Goals are stated in terms of aspirations, and these are formed by adaptation and learning from experience.

\- Search strategies are developed on the basis of learning and adaptation through experience.

\- The attention the decision maker pays to the environment is the product of learning and adaptation driven by experience.

We suggest that these propositions are an accurate description of how most decision makers work, and especially the particular decision maker that we targeted in this study. Our implicit proposition is that the decision making behaviour in this study is typical for a large number of managers in many kinds of enterprises. The goal of the decision support systems (DSS) should be to contribute to a better decision process. Instead of decision making we consider unfolding a decision in the Japanese sense with emphasis on the process rather than on the act of making a decision (Zeleny, 1982). Procedural knowledge is a key element in understanding the current decision behaviour and in improving the quality of the decisions made.

We have based our design on four relational concepts from Cyert and March (1992) to identify how actual decision making differs from effective decision making. In their work, they provide both theory and empirical support for decision making in organizations. These concepts gave us a guide for diagnosing decision making behaviour. The concepts are:

\- Local rationality. There is a tendency for the individual subunits, or the individual decision makers to deal with a confined set of problems and a limited set of goals. Through delegation, the organization has reduced a complex set of interrelated problems and conflicting goals to a number of uncomplicated problems. This implies that many decisions are inconsistent and suboptimal.

\- Uncertainty avoidance. Organizations tend to avoid uncertainty. Managers prefer working with shorter time horizons in solving problems, rather than working with projections about long-run uncertainty. Urgent problems get higher priority than long-run strategies. Plans are emphasised in settings where they can be made self-fulfilling through control mechanisms. Instead of treating the environment as exogenous and predictable, they seek ways to eliminate the uncertainty and enforce control.

\- Local search. Search is typically stimulated by specific problems, and directed toward solving that problem. The search is relatively shallow and advances on the basis of a simple model of causality until forced to a more complex model. The search will typically be confined to the neighbourhood of the problem symptom and the current alternative. A cause will be discovered near its consequence and the new solution will be close to an old one.

\- Simple learning. Organizations as well as the individual decision makers learn. The change of goals, shift of attention and revision of search procedures are contingent upon experience. There is a tendency to use relatively simple routines for adjustments of aspirations rather than to develop better understanding. Decision makers may not be conscious in systematising and relating incidents as they occur.

These four concepts describe decision making as it differs from the prescriptions of the rational choice model (Simon, 1976).

## A conceptual basis

An unstructured decision problem is a task where the decision maker is unfamiliar with the initial position, the goal position or the set of procedures that will lead from the initial to the goal position. The decision maker may have a clear perception of his preferences, and be able to establish a dominating criterion. On the other hand, the decision maker's preferences may be complex and only possible to describe through several criteria. In addition there may be lack of clarity in the understanding and the interpretation of objectives. Likewise, the consequences that are expected to result from possible actions may be well understood and possible to rank. Or they may be dominated by uncertainty in causality, and it may therefore be difficult to estimate consequences or the preferences between them.

Thompson (1964) presented a two-dimensional grid for the structuring of decision problems where uncertainty in objectives and/or consequences is expressed as either high or low. If both consequences and objectives are low in uncertainty the problem is considered to be computational. Here we find a preferred alternative when the problem is well defined. Uncertainties are negligible, and it is possible to establish a dominating criterion. When the objective is established, for example the optimisation of a parameter, the remaining problem is exclusively mathematical.

When the consequence uncertainty is high and the objective is low the manager is likely to use judgement. In this situation it would not be possible to give precise quantitative assessments for the alternatives in terms of the objective. A typical judgement-based problem is utility maximisation where the goal is well defined but it is difficult to quantify the utility attached to the different alternatives. To model judgement-based decision making it will often be necessary to study empirical data and a large number of decision situations.

Compromise is used when uncertainty in objectives is high and consequences are low. This implies a balance between competing objectives, or even between fuzzy perceptions of the objectives. It will be easy to represent the consequences of the alternatives, but it will be difficult to represent which consequences should be preferred.

Finally when both consequence and objective uncertainty is high, inspiration or intuition is commonly employed. This frequently is the situation at the highest decision level in organizations. In these situations there will be competing criteria and lack of clarity in causality. In addition to competing criteria, there may also be a lack of clarity in the comprehension and the interpretation of objectives. Vague objectives are typically seen in the earliest stages of a decision process and in the formulation of strategic goals. It therefore becomes important to develop a general view and to account for creativity in the formulation of alternatives and new objectives.

## Research motivation

The motivation for our research is to demonstrate that recent developments in end-user and front-end computer software tools can now be used as enablers to enhance the development of new forms of DSS. These supports are envisaged to assist decisions that rely on judgement, compromise, inspiration, and intuition. Our prototype DSS is envisaged to serve a decision maker that typifies the administrative man. We use a specific manager to illustrate our work and one component of his work environment that we deem to be appropriate for most managers. This is the change management component of the manager's decision environment. We focus particularly on the support for decision framing and for the unfolding of complex and unstructured decision tasks.

The problem of providing decision support is a problem of providing support for the decision process. We envisage a major part of the gain from implementing this DSS to be the improvement of the user's mental model and his modeling capacity. We want to demonstrate that there are methods to enhance the effectiveness as well as the efficiency of the administrative man through the use of DSS tools.

A major part of the gain from implementing this DSS is the improvement of the user's mental model and his modeling capacity to address his boundary spanning requirements. The use of our system ought to contribute to a typical user's learning with respect to solving problems in a wide sense. To overcome the shortcomings noted in Cyert and March's four concepts design, we added the following desirable characteristics for the administrative man to our prototype:

● learning to see his problems in a more global organizational view;

● learning to master uncertainty better;

\- increasing his understanding of appropriate levels of information search and exchange; and

\- increasing his learning from and about primary decision problems.

While the system is designed to support existing decision processes, the use of the system ought to stimulate and channel behaviour toward prescriptive processes.

## DSS approach

According to Turban (1995) a DSS is

... an interactive, flexible and adaptable computer-based information system, specially designed for supporting the solution of non-structured management problems related to improving decision making. It utilises data, provides an easy user interface, and allows for the decisions maker's own insights.

## Further, the more sophisticated DSS

... also utilise models built by an interactive process (frequently by end users) to support all of the phases of decision making and include a knowledge base.

Executive information systems (EIS) are

... computer based information systems that provide executives with easy access to high-level strategic information about a company's current status (Frolick, 1994).

Out of necessity, the more recent trend in EIS is toward what is called management support systems, a combination of the earlier EIS and the analytical capabilities of office automation systems.

Decision support tools that focus on end users (managers and their staff) are crucial components in ‘unlocking the wealth of data that companies collect’ (United Communications Group, 1995). In the past, users had to rely on the information systems department to write custom queries and produce reports. Contemporary decision support tools empower users to generate their own queries. However, user buy-in and support is critical for the successful deployment and acceptance of these DSS.

Experience with DSS over the past 20 years or so has led researchers to propose a number of frameworks in order to isolate the important factors in successful DSS design (eg Gorry & Scott Morton, 1971; Keen & Scott Morton, 1978; Keen, 1980; Sprague & Carlson, 1982; Bennett, 1983; Mittra, 1986; Holsapple & Whinston, 1987; Klein & Methlie, 1990 and Turban, 1990). Other researchers have concentrated on observing the impacts of DSS usage and empirical and experimental environments (eg Keen, 1981; Hogue & Watson, 1983; Rockart & DeLong, 1988; Benbasat et al, 1991 and Courtney et al, 1993).

Rockart and DeLong's research on computer use by senior managers in US, Canada and the UK, grouped the systems used by the managers into three categories (pp 41–42):

\- Systems generally associated with office support, including electronic mail and word processing.

\- Systems which support the organizations' planning and control processes.

\- Systems which develop, clarify, or enhance the individual manager's mental model of the firm's business environment.

Holtham (1992, p 275) noted that there was a gap between the development of research frameworks for decision support on the one hand and development of commercial systems on the other. He verified that the major part of the commercial development and investment in DSS for senior managers fell in the second group described by Rockart and DeLong (1988). These systems have been heavily dominated by the planning and control framework. Very few of the systems have been built explicitly on models of managerial work other than traditional three level pyramids (Anthony, 1965, pp 16–19). Our DSS development falls in the third group. We want to enhance the manager's mental model of the company's environment, and we illustrate and demonstrate a system for abstract conceptualisation and reflection through a prototype DSS.

Recently, Angehrn and Jelassi (1994) criticised the strong legacy of Simon's three decision making steps on the DSS theory and practice:

The wide adoption of Simon's model - which has provided a sound conceptual basis for developing the first generation of DSS - has become a serious obstacle for the evolution of DSS theory and practice.

They suggest that different types of DSS can emerge from adopting alternative perspectives, for example:

1) 'Relaxing' the basic assumption that managerial behaviour is guided by deductive logics and full or bounded rationality as suggested by Simon's model.

2) 'Shifting' the focus from the choice phase to other phases such as structuring/framing, creativity and idea processing, post decisional analysis, feedback analysis, etc.

Benbasat et al (1991, 1993) described and summarised empirical studies in the use of three information technologies to support managerial activities, among them DSS. They identified:

Empirical research on DSS design for individuals suggest that DSS usage is higher, and user satisfaction, attitude, and perceptions are more favourable when prototyping and iterative design are used. These methods necessitate a higher degree of user involvement in system design. Consistent with these results, studies of user involvement in design have found that higher user participation results in favourable perceptions of result as well as lower rates of system rejection. However, this research does not show that actual decision maker performance with a support system is affected by user participation in design. In general, we have found that the interest in DSS design research has waned in recent years. Contributions to theory building and testing have been limited, except in cases dealing with user involvement and participation in design (Benbasat et al, p 410).

The foundation of DSS is the descriptive model of the decision maker. Benbasat et al found in their study that the methods and information collection techniques best suited to study managerial support systems have been addressed extensively.

There is no single best strategy. The selection of a particular strategy depends, among other things, on the amount of existing knowledge, the resources available to the researcher, the purpose of the research, and the nature of the topic researched. (Benbasat et al, p 424).

Consequently, we want to use a qualitative approach, which attempts to provide an in-depth understanding of a single case. In this case we used indirect knowledge acquisition methods; two different interview techniques for eliciting information (we have used the term ‘information’ in a broader sense not specifically tied to a domain. We interpret ‘knowledge’ to be more restricted in domain). This case method is suited for exploration and discovery when our understanding is new. A main objective is also to investigate and describe the nature and complexity of the processes that have taken place.

As we developed our design, we predicated our DSS approach on the decision research techniques advocated by Stabell (1983, 1987) and treated in Fuglseth and Stabell's (1983, Fuglseth, 1989) work. For our particular case study we needed to understand the current decision processes of this manager before we could propose any improvements. The manager has accumulated expertise through years of working in his trade. There are many qualitative elements that one as an outsider cannot fully comprehend or appreciate in the course of a research project such as ours. We should expect that there are facets of the manager's knowledge that are ‘uncodifiable’. He may not be aware that he actually uses certain knowledge, or he may not be able to express verbally exactly what pieces of knowledge he uses.

## Our approach

The case material is based on interviews and data collected from the manager of a purchasing division in the Norwegian wood-processing industry. The purchasing division is a decentralised unit that functions as a standard cost centre. The division is responsible for buying and supplying other units of the company with roundwood and industrial wood chips. The roundwood market is characterised by a large number of small suppliers that receive a small portion of their income from the supply of roundwood. Other important parameters for the roundwood market are climate and topographic characteristics. Therefore, the roundwood market operates under a significant degree of uncertainty.

Our particular manager has a unique role within his organization. He operates as a strategic manager, a middle manager, and as a quasi-independent contractor. He communicates and works directly with vendors. His customers are the company units themselves. This decision maker typifies an increasing emphasis on boundary spanners between organizations. The performance of such a decision maker is essential to the efficient and effective operation of the organization (Mintzberg, 1973). Much of the administration in complex organizations is the management and exchange across organizational boundaries.

Based on our diagnosis and interpretation of the data collected (by means of a series of interviews), we arrived at a set of observations about the manager. He appears to have a good set of notions about supply and a weaker set about the market. The manager has a good causal understanding from the supply side, where he appears to be able to incorporate different perspectives. From the supply side he is more of a leader than a middle manager, whereas from the market side he is more of a middle manager. The manager's reception of signals under crisis situations is strong.

In our design we tried to assist him in forming an opinion about what is happening and what steps are to be taken to prepare for the anticipated effects. The manager is aware that uncertainty exists in many of his activities and that his work is influenced by uncertainty. He has tried to quantify uncertainty but he is not able to incorporate this quantification into a model. Overall the manager has only a general picture of his decision making environment. He is able to see only part of it at a time. He appears to have a problem in perceiving the total effect. We believe that he needs to have mechanisms available that can identify gaps and deficiencies in this environment.

## System design objectives

From the diagnosis of the purchasing manager's decision processes, we established a list of symptoms. This list is a compilation of the characteristics of the decision making processes. For the design we focused on which decision support needs we could infer from this list. The symptoms and the support needs are shown in Figure 1.

Many of the characteristics in Figure 1 point toward a need for cognitive support to handle complex problems. Major goals have a significant long term perspective and a low degree of operationality. Therefore, the manager needs to structure problems in a way that allows him to assess long term possible outcomes. He needs to be able to visualise long term effects of immediate decisions and to assess and manage uncertainty. He should therefore have a DSS module whereby he can construct or unfold a problem from scratch (starting from a notion of a problem) and then gradually expand and unfold the influences and causalities. It would also be beneficial for him to be able to simulate the effects of altered conditions.

Our design objectives included giving the user the possibility to structure problems graphically. He ought to be able to attach appropriate information to a map in the form of uncertainty estimates, experiences, future estimates or any suitable comments. To visualise economic consequences and effective constraints, we wanted to create a design that gives the user the possibility to explore scenarios. The system ought to allow him to visualise connections and causalities with other parts of the company and the suppliers and facilitate the unfolding of information about any effects on other parts of the company.

We envisioned the DSS to be able to stimulate the user's information retrieval, and contribute to his conscious analysis of information requirements. We tried to incorporate a means to encourage him to state the reasons for his assumptions, and for the data that he enters into the model based on these assumptions. We also wanted to allow the manager to visualise uncertainties by encouraging him to justify and think through his assumptions.

The change management module was one of three decision support modules created for this manager. The other modules supported budgeting, contracting and value chain analysis. Together the three modules were designed to complement each other and to support major decision support needs.

## Change management conceptualization

## Initial steps

For our software foundation we elected to use Visual Basic under a Microsoft Windows environment. Using Visual Basic we were able to adopt a component-oriented approach that permitted us to present or unfold aspects of the system as they were developed or used (Pountain & Szyperski, 1994; Udell, 1994). The software enabled us to incorporate standard Windows objects and controls into our applications. We decided upon a common screen layout with regard to the use of menus, buttons, diagrams and information access.

As part of the formulation of a prescriptive model for the DSS we created a series of hierarchical charts describing the various activities. The hierarchy chart for change management is shown in Figure 2.

To begin our conceptual design we created a two-dimensional table which contrasted the four dimensions or characteristics that we theorised would address Cyert and March's four descriptors (uncertainty mastery; global rationality, information search and exchange, and learning) with the change management decision processes (crisis management, change handling, and change planning). Using diagnosis results, and the support needs revealed there, we created a list of important support needs and possibilities for each combination of dimensions and decision processes.

Our table consisted of combination elements that addressed the decision processes at their fundamental levels. In the hierarchy chart we divided the processes into sub processes, and so forth. Under crisis handling there were two sub processes: crisis handling and crisis planning. In turn, within crisis handling we specified four fundamental processes: problem identification, problem analysis, action plan development, and implementation. For each of these fundamental processes we stated decision support needs and possibilities related to the four dimensions.

Our next step was to translate the table into a concrete form by specifying what information was needed and how the interaction between the user and the change management module should work. To perceive better the process in using the change management module, three decision process charts were constructed. The decision process chart for crisis management is shown in Figure

![](/api/attachments/3VQUG774/fulltext/images/6b6ce74cc750c700b4438427ff8557eaedbe96dbe385be1df1b603782fb118de.jpg)  
Figure 1 Manager's support needs. (PM = Purchasing Manager).

3. On this chart we depict the crisis management sequence of operations that the manager would most likely take. It begins with a scan or the reception of a signal and ends with the selection of some preferred strategy. We used these charts as an additional cognitive aid to create a uniform layout for the support of the decision processes for crisis management, change handling, and change planning.

## Flexible structuring facility

One of our major diagnostic conclusions was that this decision maker needs a problem structuring tool. The decision problems he faces are typically quite complex. His decision making is constrained by his difficulty in perceiving a problem in its entirety. He ought to be able to start at the point of perceiving a signal, sensing a problem, or wanting to achieve an objective. He should

![](/api/attachments/3VQUG774/fulltext/images/9b2acf3006ad1f4598992822c6b99199ae89a8ce68612ccc485588fc52b53a70.jpg)  
Figure 2 Change management hierarchy chart.

![](/api/attachments/3VQUG774/fulltext/images/4d4ebf1d2b99a9fa3dd8812907bb4d2997b02e9204cfe2df626fa1d4063efd22.jpg)  
Figure 3 Decision process chart for crisis management.

then be able to unfold the problem gradually, and, in the process, build his understanding, his mental model, of the problem. We further concluded that the structuring system should have a high degree of flexibility. We conjecture that a visual interactive structuring in the form of boxes, each representing an item (event, signal, action, etc.) that are moveable about the screen and able to be linked to other boxes, would be an appropriate design mechanism.

To address these conclusions and observations, we tested various possibilities, with list boxes and with text boxes in Visual Basic. We settled on a design approach with separate boxes each containing one item. These boxes could be linked and the information in the case saved in a case database. We found it appropriate to have the boxes contain only very brief descriptions. A more extensive description utility can be attached, which could be activated by the user.

It was also appropriate to let the system tag which case the user selected as the most likely, and have it accessible throughout the system. Unfolding an actual problem in the crisis management would be considered crisis handling, while unfolding a hypothetical case would be considered crisis planning or making a contingency plan. Correspondingly, for change management and change planning, the user would have cases corresponding to the likely course of events, and other cases corresponding to less probable courses of events.

By designing a high degree of flexibility into the system, we can allow the user to model things we did not anticipate in our treatment of support needs; we wanted the system to be self-adapting. Suppose, for example, that we did not think of Rosenhead's robustness analysis (Rosenhead, 1989), and that the user now wanted to use the system according to that formalism. This would be possible. He could start with the initial decision, unfold the possible decision states in the next period, and so on further into the future. He would then be more able to see future ranges of effects, and what actions to take today to prune away certain branches and retain others.

It was revealed in the diagnosis that the manager needed support in thinking through signals, causes and events that may affect his performance. We concluded that we should stimulate the manager in unfolding causal relationships. Signals, causes and events were chosen to be the first item category. We wanted these to stand out so we assigned them to a category, with their own button and default colour for the boxes, in order to be conspicuous. Therefore this will be a category where the manager will be concerned about making appropriate entries. The item boxes, when generated as signals, causes or events, were designed to appear appropriately spaced on the left part of the screen.

The manager usually needs to link the items (signals, causes and events) to the effects. We chose the effects to be the second item category. These are the effects that the manager perceives to come from the signals, causes and events. By having effects as a separate category, we expect to stimulate the user's search for items of this kind. Effects item boxes are generated, as the manager specifies particular effects, at an appropriate distance to the right of the first item category boxes. We now have the following possible unfolding of causes and events as shown in the first part of Figure 4. Note than an effect can be linked to more than one signal, cause, or event.

The next category was designated to be actions. In the crisis handling mode, this category typically would be actions employed to deal with crisis situations. For the crisis planning mode we perceive actions to be possible contingency plan actions. In reality, the difference between these two modes may only be that one case is chosen as the most likely; and others are kept as hypothetical cases to be used as contingency plan cases. In the change handling and change planning modes, the actions would be tactical plans and strategic plans, respectively.

In this context the user therefore would be stimulated to associate actions with critical dimensions as shown in the second part of Figure 4. We did, however, see the need for adding more structure. By using certain item categories, it was perceived that we could stimulate the manager to think through possible entries that could be placed in that category. By making the boxes moveable around the screen, the user can construct complex causal chains, such as that shown in the last part of Figure 4. There we see that one effect is linked to another effect, and so forth.

The next category that we examined was the total effects of the events and the actions taken. This should stimulate the user to consider how the important parameters may be affected; for example, what are the effects on the supply of lumber. We decided to name this item category, prognosis, to make it clear that we intended it for a different role than that of the effect category. This category should be linked to the previous prognoses. The user should have the option of updating the prognoses with the numbers that he finds appropriate, directly from within the case.

We expect the manager to become gradually more competent in using the system. He would initially have a low complexity handling ability. The maps that he generates would then be quite simple but complete. As the user becomes more competent his complexity handling ability ought to increase, and thereby the complexity of the maps. Old cases can be used as support for generating new and more elaborate ones, they can be complemented by adding new items, and parts of these cases can be inherited. The system supports using simple maps, extending maps and copying parts of maps over to new cases. We also envisioned incorporating the facility to scroll through lists of items so that the user can search for case descriptions as a function of particular items; for example, to look for cases where a special signal or event has occurred.

## Prognosis making facility

The change management module should also take care of the prognosis making. The system should support and stimulate the establishing of medium and long term prognoses. Prognoses are very closely related to key assumptions. Making appropriate assumptions about the future developments in logging, production and sales is an important part of change management. We conjecture that the process can be supported much like we support the general creation of cases. The manager may place one or more of the prognosis boxes in the right part of the screen, and then place appropriate boxes for assumptions he wants to specify, events he foresees, signals he sees, and actions he plans to take. In this way, we can structure the process of establishing prognoses just like the process of creating a case. Selecting a prognosis box should bring up a form containing a graphical representation of the prognosis, facilities for manipulating the values, and a list of the assumptions made related to the case. This form should be the same as that which would be retrieved when prognoses are accessed from other modules in the system. This process is presented in Figure 5.

![](/api/attachments/3VQUG774/fulltext/images/3732da1e11c09e7dd7b7bbf0bceb12e900431037373474d2769519853575e2b8.jpg)

![](/api/attachments/3VQUG774/fulltext/images/6a9439cf9b6af95a443f9e6eab0e1626782f1ddd7902999d76e14fd575e5ecb1.jpg)

![](/api/attachments/3VQUG774/fulltext/images/b55d6de98e5dd98e8cfc1eacf3d3ea70b2ab824bdd69edba7de2a69d6e47e991.jpg)  
Figure 4 Linking of signals, causes, effects and actions.

We decided upon two prognosis time frames of fifteen periods (the year is divided into thirteen periods) and fifteen years (including previous years) as appropriate for the change handling and the change planning modes. The use of the short term prognosis in the change management module would typically be used to make revisions.

The effects of the prognosis, in our case example, upon stock levels in the medium term would be shown in a stock level form. This form sums the in- and outflows in each period and displays the stock levels. We also designed the form to support the addition or deletion of contributing flows. Adding a flow would then retrieve or make a new record field that would be added to the stock level computation.

![](/api/attachments/3VQUG774/fulltext/images/5e6e98811f7341a31ae3f9fd0fff43b89ea00cba4a1b4ec5cb93c9097aa081ac.jpg)  
Figure 5 Selecting a prognosis process.

## Support for modeling and operationalising goals

We revealed in the diagnosis that the manager needs support in modeling and operationalising goals. We saw a low degree of operationality in his goal treatment. This means that it may also be difficult to evaluate goal achievements. He may not have a clear conception about what is achievable. We concluded that the change management module should support the manager's goal formulation and the specification of achievement levels. The system should aid or stimulate the manager to specify tactical and strategic goals and target achievement levels. He should be stimulated to make goals more operational. Only when goals are properly stated can the manager get a good conception of his own goal achievement. A low degree of operationality makes it important to aid the goal formulation process.

We conjectured that we needed a button on each of the change management screens which would facilitate the retrieval of a hierarchy of goal statements from the database. By having the button conspicuously located, he would be stimulated to think about how the case he is presently working on is related to the goals. Thereby, he will also be induced to have an updated and comprehensive goal statement hierarchy. Goal statements should also be possible to place as boxes into the case screen. We conjectured that probably only one or two goals would be entered into each case. We decided to place these boxes at the lower central part of the screen when generated. We perceived that the manager may want to structure goals and subgoals as a case in itself, perhaps even linked to critical success factors (CSFs). The goal utility also covers CSFs. Goals and CSFs are created with separate buttons, and have different colour codes.

## Case structure

As we designed the system to deal with different types of cases we realised that these different types of cases needed to be stored separately or tagged so that the use can retrieve a list of cases of each kind. Our diagnosis revealed a need to support uncovering, handling and building of awareness about uncertainty. We perceived several ways of representing uncertainty. Statements or numbers may be entered as part of the assumption items, event items, as separate items or as statements directly in the prognosis screens. A second issue related to the form of the likelihood statements. The natural way for us, as analysts, was to facilitate quantitative and numerical representations. We could stimulate the user to identify uncertainty, assess magnitude and effects, and require quantitative inputs for the magnitudes. We have however hesitated to do this. We may easily get a problem with the completeness, or the user's perception of completeness. Some of the items would not be possible to assess quantitatively or the user may not feel comfortable with doing this.

We must take great care that the process involved in assessing uncertainty does not become too tedious. Neither should we require too many quantitative inputs. Stimulating the manager to go through the process of quantifying uncertainties is of great support. It also makes it easy for use to calculate and display uncertainties and probabilities. But we hesitated to require such inputs. It is more important that the manager feels comfortable with the system, that it is transparent and that he feels that his modeling is complete. We were worried that making the manager assess a number of probabilities and variances in quantitative terms may make the manager less comfortable with the system; he is making qualified guesses, but still guesses. We conjectured that there may be a high likelihood that he may not continue using the system in such a case. He may discard the uncertainty assessment altogether and only focus on the most likely case. Fuglseth (1989) reported such a finding; leaders would pursue and assess different scenarios for a short while after being told that they should do this, then gradually reduce their focus to the most likely course of events. It is more important that we focus on the manager's mental model of the problems and uncertainties. He needs to pursue and think through certain alternative courses of events. We wanted to stress the importance of the manager perceiving that he has ownership of what is being modeled. The value of this approach is less that it provides accurate forecasts than that it draws attention to the specification of the reasonable (or even unreasonable, but not ignorable) assumptions.

We conjectured that having certain cases that represent possible deviations from the expected prognosis would be sufficient, and conceptually more natural for the manager to unfold. The most natural flow of the manager's logic is first to address possible events and deviations and then address the effects. By having first addressed the likely deviations, he would also implicitly have addressed how large the deviations would be (as a part of the case). The contingency cases would also be available when the manager is working with the prognosis form. These cases should have unfolded and estimated the contingent effects.

We want to stimulate the manager to play with alternative scenarios and thereby build his mental model of the problem and also, therefore, about the uncertainties, likelihoods of alternative courses of events and the possible consequences. We thus stimulate the manager to pursue ideas, think through possibilities, and thereby gain a better perception of how likely they are.

We decided not to have uncertainty as separate item boxes. The user's perception of the uncertainties should prevail from the cases. Contingency case creation would be closely tied to the user's perception of possible events and outcomes and their likelihoods.

The manager should be stimulated to state his assumptions, and to play with assumptions. An important objective with the change management module was to make the manager conscious of his current assumptions, and thereby make him aware of alternative assumptions. The manager should be explicit about important assumptions. Instead of scrolling through an extensive list of possible assumptions, one should probably focus on a small number of central topics.

Important assumptions are of concern in every module of the system, and should be accessible anywhere in the system. The current assumptions should be tagged. Other assumptions, made as part of hypothetical cases should only be saved as part of these cases. The current case, or the main case, can be viewed as an assumption in itself. This case should be accessible throughout the system. We may see assumptions at two levels. First, each case when unfolded, will contain certain central assumptions. The case may be perceived as a higher level assumption in itself in a nested fashion. The manager would typically identify a small number of important assumptions, assumptions that he wants to stress by entering as items in the case. The contingency cases will then typically be covering the courses of events under relaxed or different assumptions.

The main short term crisis handling case may itself be seen as an assumption about how the problem will develop and the effects of the manager's actions. The main medium term change handling case contains assumptions about how things would develop in the medium term. Likewise, the main long term change planning case contains assumptions about how things would develop in the long term.

## Change management design and implementation

Figure 6 shows parts of the change management specific DSS. The title and the menu bar are displayed as well as the buttons along the bottom of the screen. Each screen in the prototype DSS adheres to certain standards.

The change management main screen is the starting point for any kind of change activity. Using the case option on the menu the manager can create a new scenario or case, or retrieve any existing case. The case option relates to generating, retrieving and saving cases. If a new scenario or case is selected, the working section of the screen remains blank until the manager begins to unfold a new problem.

Situated along the bottom of the main change management screen are five horizontal buttons. These buttons assist the user in unfolding causal relationships. The first two buttons refer to the signals and effects while the fourth and fifth buttons refer to the actions and prognoses. The middle button, entitled link, can be selected by the manager to establish links between any of the four kinds of items. The link tool, as implemented on this screen, permits linking of any item with any other item. The five buttons have been given colour codes that correspond to the colour of the item boxes.

At the bottom of the main screen are four buttons, positioned vertically in a rectangle, on the right side. These commands are secondary or supplementary means to record data about a sencario or case. For a manager these may be very relevant descriptors (eg assumptions and goals). They are not necessarily directly related to any specific relationship. Instead, they may refer to the case as a whole.

We created a case structure for the change management module. Six different case categories were implemented. We considered these categories to be appropriate representations of possible case types. The first three categories refer to the short, medium and long term decision horizons. These categories encompass the typical cases related to the running unfolding of crisis situations, contingency plans, other kinds of plans, prognoses and strategic assessments. Two other categories were designed to complement the three above. The goal hierarchy category was designed to facilitate the manager's construction of goal hierarchy cases. These goal hierarchies serve to help the manager integrate a systematic goal and value focus (Keeney, 1992) into the change management. The robustness analysis category was designed to be a category of a special set of cases related to the unfolding of complex decision trees. We found Rosenhead's robustness analysis (Anthony, 1965) approach to be appropriate for our manager's decision environment.

These cases would then unfold different decision paths, and evaluate the possible effects on a time horizon. This would promote the analysis of complex decision problems where successive decisions have a high degree of interdependency. He would then be more able to see future ranges of effects, and what actions to take today to prune away certain branches and retain others. We also created a general category for all cases that do not fit in any of the above categories. For example, the Thinking Aloud Event Protocol charts would be saved as general cases.

![](/api/attachments/3VQUG774/fulltext/images/71e76d6a284da63ee4215c6f307c8006859897d408d1e4f0dd336481f1c0da2c.jpg)  
Figure 6 Parts of the change management screen.

The manager unfolds the scenario by specifying signals, effects, actions, and prognoses. This specification is done by depressing the appropriate buttons. The manager is expected to give a name or title to the item and a description or comment associated with the item. Figure 7 presents an example of an unfolded case.

The manager can continue to enter items pertaining to the problem complex. At some stage he will need to establish linkages among these items, as indicated by lines in Figure 7. He can specify multiple links from and to items. For each one-to-one relationship he has the opportunity to enter a comment or description pertaining to the nature of the link.

The prognosis specification (and new prognosis generation) form displays the selected prognosis in both tabular and a graphical form. This screen is flexible with respect to displaying and editing prognoses.

This form, as shown in Figure 8, facilitates the creation of a prognosis for one of the entities (eg transport, logging, etc) and at the same time allows the manager to view a template from another case (for the same kind of prognosis). Using the template, the manager can modify the values to forecast or prognosticate the future values given the signals, effects, and actions linked to this prognosis.

## Summary and conclusions

In this paper we have described the design of a change management module for a decision support system. We envisioned a system to stimulate and support the user's unfolding and structuring of complex and unstructured decision problems. Key dimensions are improving the decision maker's mental model and his modeling capacity, as well as stimulating learning. This learning is in the following dimensions: learning to see his problems in a more global organizational view, learning to master uncertainty better, increasing his understanding of appropriate levels of information search and exchange, and increasing his learning from and about the primary decision problems.

To address decision makers such as the one we have

![](/api/attachments/3VQUG774/fulltext/images/f2851f89fb711612587e0ac563a2e46ebf30e7f27a0efa21af87bc80d162c685.jpg)  
Figure 7 Change management case screen.

![](/api/attachments/3VQUG774/fulltext/images/6ca53b55594801d06ac252707122c906e840bedcd76fc84f4273ab4de85ee1b2.jpg)  
Figure 8 Prognosis form.

described in this paper and the administrative man, Landry (1994) noted that while a clear definition of organizational DSS is somewhat elusive, the concept emphasises the need for flexible tool kits to support organization-wide decisions, which become increasingly problematic as the interactions become more complex. In a working paper, Stokke et al (1993) noted that:

current systems for developing competitive strategies share a common weakness. Although they set forth ample theoretical information about the type of analysis to perform, none provides practical guidelines for processing large amounts of domain-specific information required for developing such strategies in real life business environments.

We assert that our system addresses and aids this process.

The visualisation of the signals, causes, effects, goals, prognoses, linkages and their strength, is a tool for the manager to appraise how the effects of the linkages influence the result of his goals, both short term and long term. He appraises in what way his decisions and enterprises exploit the positive effects of the linkages among the value activities and diminish the influence of the negative effects. This process stimulates him to explore future possible developments between his division and the other entities in the value system. The change management module gives the manager an aid in constructing mental models of long term goals and perceiving decision making in terms of these goals.

Working partnerships in which better coordination of tasks and activities are essential, require increasingly more coordination and mutual adjustments. As goods and services move along the value-added chain, increasingly a major component is the exchange of information. The emergence of new ways of packaging or organizing information suggests the importance of information itself as a key variable for analysis. Given our prototype DSS we view our system to be both a mechanism and an enabler that can give rise to a higher quality of information to be used by this manager in his exchange processes.

We have given this manager a system wherein he is stimulated to identify certain of his decision environment aspects in a causal form. We are giving him a tool with which we want to stimulate him to identify and describe

decision elements and their linkages. Our system at this point has the beauty of simplicity and generalisability to a variety of ‘administrative man’ managers. Following the formulation and initial prototype implementations we re-visited the purchasing manager. On these occasions we presented and demonstrated the software. His response was quite enthusiastic to the point that he has requested to employ one of the developers to complete the full DSS.

A major benefit for the organization using the DSS system is the acquisition and storage of knowledge in the system. This capturing of the manager's knowledge in the system empowers the organization and gives them an edge against the potential loss of a valued decision maker.

## References

ANGEHRN A and JELASSI T (1994) DSS research and practice in perspective. Decision Support Systems, 12(4/5), 267–275.

ANTHONY RN (1965) Planning and Control Systems: A Framework for Analysis. Division of Research, Harvard Business School, Boston, Massachusetts.

BENBASAT I, DESANCTIS G and NAULT BR (1991) Empirical Research in Managerial Support Systems: A Review and Assessment. NATO Advanced Study Institute on Recent Developments in Decision Support Systems, June. Tuscany, Italy.

BENBASAT I, DESANCTIS G and NAULT BR (1993) Empirical Research in Managerial Support Systems: A Review and Assessment. In Recent Developments in Decision Support Systems (HOLSAPPLE, CW and WHINSTON AB, Eds). Springer, US.

BENNET JL (1983) Building Decision Support Systems. Addison-Wesley, Reading.

COURTNEY JF, DESANCTIS G and KASPER GM (1983) Continuity in MIS/DSS Laboratory Research: The Case for a Common Gaming Simulator. Decision Sciences, 14, 419–439.

CYERT RM and MARCH JG (1992) A Behavioral Theory of the Firm, Second Edition. Prentice-Hall, Englewood Cliffs, New Jersey.

FROLICK MN (1994) Management Support Systems and Their Evolution from Executive Information Systems. Information Strategy: The Executive's Journal, 31–38.

FUGLSETH AM (1989) Beslutningsstøtte: metode for diagnose av ledernes informasjons- og situasjonsoppfatninger, Avhandling for graden dr.oecon., Norges Handelshøgskole.

FUGLSETH AM and STABELL CB (1983) Capture, Representation, and Diagnosis of User Information Perception. Working paper. The Norwegian School of Management.

GORRY A and SCOTT MORTON MS (1971) A Framework for Management Information Systems. Sloan Management Review 13(1), 55–70.

HOGUE JT and WATSON H (1983) Management's Role in the Approval and Administration of Decision Support Systems. MIS Quarterly, 7(2), 15–26.

HOLSAPPLE C and WHINSTON AB (1987) Artificially Intelligent Decision Support Systems – Criteria for Tool Selection. In Decision Support Systems: Theory and Application (HOLSAPPLE C and WHINSTON AB, Eds), pp 185–213. Springer Verlag.

HOLTHAM C (1992) Architectures for executive support systems – towards a prototype top manager workstation. In Decision Support Systems: Experiences and Expectations (JELASSI T, KLEIN MR and MAYON-WHITE BV, Eds), pp 275–290. Elsevier Science Publishers B.V. (North-Holland).

KEEN PGW AND SCOTT MORTON MS (1978) Decision Support Systems: An Organizational Perspective. Addison-Wesley, Reading.

KEEN PGW (1980) Decision Support Systems: Translating Analytical Techniques into Useful Tools. Sloan Management Review, 21, 33–44.

## About the authors

James Sena is Professor of Management Information Systems at California Polytechnic State University.

KEEN PGW (1981) Value Analysis: Justifying Decision Support Systems. MIS Quarterly 5(1), 1–15.

KEENEY RL (1992) Value-Focused Thinking: A Path to Creative Decisionmaking. Harvard University Press, Cambridge, Mass.

KLEIN M and METHLIE LB (1990) Expert Systems: A Decision Support Approach. Addison-Wesley, Reading.

LANDRY JR (1994) Efficient Boundaries of Organizational Decision Support Systems. Proceedings of the Twenty-Seventh Annual Hawaii International Conference on Information System Science, 775–784.

MINTZBERG H (1973) The Nature of Managerial Work. Harper & Row, New York.

MITTRA SS (1986) Decision Support Systems: Tools and Techniques. John Wiley & Sons, New York.

POUNTAIN D and SZYPERSKI C (1994) Extensible Software Systems. Byte May, 57–62.

ROCKART JF and DELONG DW (1988) Executive Support Systems. The Emergence of Top Management Computer Use. Dow Jones-Irwin, Homewood, Illinois.

ROSENHEAD J (1989) Rational analysis for a Problematic World. Problem Structuring Methods for Complexity, Uncertainty and Conflict. John Wiley & Sons, Chichester.

SIMON HA (1976) Administrative Behavior. The Free Press, New York.

SPRAGUE RH AND CARLSON E (1982) Building Effective Decision Support Systems. Prentice-Hall, Englewood Cliffs, New Jersey.

STABELL CB (1983) A Decision-oriented Approach to Building Decision Support Systems. In Building Decision Support Systems (BENNET J, Ed). Addison-Wesley, Reading, Massachusetts.

STABELL CB (1987) Decision Support System: Alternative Perspectives and Schools. Decision Support Systems 3, 243–251.

STOKKE P, REVE T and BOYCE TA (1993) Knowledge Engineering and Information Processing for Competitive Strategy Analysis. Working Paper No. 102 November 1993, Foundation for Research in Economics and Business Administration, Norwegian School of Economics and Business Administration, Bergen.

THOMPSON JD (1964) Decision-making, the Firm and the Market. In New Perspectives in Organization Research (COOPER WW, LEAVITT HJ and SHELLY II, MW Eds), Wiley.

TURBAN E (1995) Decision Support Systems and Expert Systems, 4th Edition, p 84. Prentice Hall, Englewood Cliffs, New Jersey.

TURBAN E (1990) Decision Support and Expert Systems: Management Support Systems, Second Edition. Macmillan, New York.

UDELL J (1994) Componentware. Byte May, 46–56.

UNITED COMMUNICATIONS GROUP (1995) I/S Analyzer for information systems management, Case Studies, 34(4), April.

WALL KD (1993) A Model of Decision making under bounded rationality. Journal of Economic Behavior and Organization, 21, 331–351.

ZELENY M (1982) Multiple Criteria Decision Making. McGraw-Hill Book Company, US.

Dag Olson is an Associate Professor of Information Systems at Agder College.
