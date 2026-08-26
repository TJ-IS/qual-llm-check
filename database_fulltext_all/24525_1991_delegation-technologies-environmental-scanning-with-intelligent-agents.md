---
otero_id: 24525
otero_key: "C3B48TP3"
title: "Delegation Technologies: Environmental Scanning with Intelligent Agents"
authors: "Gregg Elofson; Benn Konsynski"
year: "1991"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1991.11517910"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Delegation Technologies: Environmental Scanning with Intelligent Agents

Gregg Elofson & Benn Konsynski

To cite this article: Gregg Elofson & Benn Konsynski (1991) Delegation Technologies: Environmental Scanning with Intelligent Agents, Journal of Management Information Systems, 8:1, 37-62, DOI: 10.1080/07421222.1991.11517910

To link to this article: https://doi.org/10.1080/07421222.1991.11517910

![](/api/attachments/C3B48TP3/fulltext/images/12ef03fb3390831d67937c5681a5e96437be25b2acf170d5a949dc5be6dcbf37.jpg)

Published online: 18 Dec 2015.

![](/api/attachments/C3B48TP3/fulltext/images/20e949317694a3b5bcd43691e7834329d7d051e39ae48de821391e3327259352.jpg)

Submit your article to this journal ↗

![](/api/attachments/C3B48TP3/fulltext/images/086ee0b226b4b7d69f58d839d70f1c2724196de0d7598b27e8bc486e84588835.jpg)

Citing articles: 12 View citing articles ↗

# Delegation Technologies: Environmental Scanning with Intelligent Agents

GREGG ELOFSON and BENN KONSYNSKI

GREGG ELOFSON is Assistant Professor of Computer Information Systems in the College of Business Administration at the University of Miami. He holds a Ph.D. in MIS from the University of Arizona. His research interests include the relationships between organizational learning, attention, design, and information technology; distributed decision making; and knowledge-based systems. He has published conference proceedings and book chapters, and has served as a staff scientist in the artificial intelligence architectures group for Science Applications International Corp., and as a consultant for Andersen Consulting.

BENN KONSYNSKI is a Visiting Professor at the Harvard Business School. Prior to that he was a professor at the University of Arizona, where he was cofounder of the university's group decision support laboratory. He received his Ph.D. in computer science from Purdue University. His current research interests are organizational and information systems design issues. He has published in such diverse journals as Communications of the ACM, Harvard Business Review, IEEE Transactions on Communications; MIS Quarterly, Journal of Management Information Systems, among many others.

ABSTRACT: Identification and evaluation of relevant trends and patterns are critical steps in an organization's business environment monitoring. Not surprisingly, the “experts” that perform this evaluation are seldom skilled in all the disciplines necessary to accomplish a thorough evaluation of the environmental indicators. While one expert may be skilled at recognizing the potential for political turmoil in a foreign nation, another at Motorola is skilled at recognizing how Japanese government deregulation is meant to complement the development of new products. Moreover, these experts often benefit from each other’s skills and knowledge in assessing activity in the organization’s environment. Often the interchange among variously skilled analysts becomes a distributed problem-solving activity that creates the high-quality, interdisciplinary analysis essential for an effective environmental monitoring activity. Problems in the environmental monitoring process often occur when a particular expertise, an agent in the problem-solving network, is unavailable, and knowledge from that domain does not play a role in the analysis. The focus of this paper is on the distribution of expertise and the sharing of knowledge in the critical process of environmental monitoring. A technical approach is adapted in this effort—an architecture and a prototype of “delegation technologies” are described that provide the capability of capturing, organizing, and distributing knowledge that may be used by experts in classifying patterns of qualitative indicators in the business environment. The redistribution of responsibilities through the delegation to, and coordination of, intelligent agents is examined.

KEY WORDS AND PHRASES: blackboard model, delegation technology, environmental scanning.

AMERICAN CORPORATIONS KNOWN TO COLLECT business intelligence include Ford Motor Co., Westinghouse Electric, General Electric, Emerson Electric, Rockwell International, Celanese, Union Carbide, and Gillette. Also, Digital Equipment Corp. and Wang Laboratories both have environmental monitoring groups. The list of organizations goes on to include (not exhaustively) Chemical Bank, the USV Laboratory subsidiary of Revlon, Del Monte, General Foods, Kraft, and J.C. Penney. $^{1}$ At Westinghouse, for example, environmental monitoring personnel act as information consultants and are involved in all phases of monitoring projects, ranging from defining intelligence objectives to ensuring effective dissemination and utilization of results. At General Mills, all members of the organization have been given basic training in recognizing and tapping sources of competitor intelligence [33].

The first step an organization takes in monitoring the external business environment for threats and opportunities often entails identifying and evaluating patterns of qualitative indicators [4, 24, 34]. From a multiplicity of sources such as online databases, Freedom of Information Act sources [22], news clippings, financial reports, and others, experts and senior managers from a variety of backgrounds scan and evaluate information that, taken together, may suggest an early warning of threats or opportunities. For example, Berry Cash, vice-president of semiconductor producer Mostek Corp., says the following: “It’s up to each product manager to keep up with what the competition is doing . . . [for example] personnel looks at what kind of engineers they’re hiring. You start seeing aggressive quotations for parts. We talk about these things every Monday at staff meetings. It’s almost a form of gossip.”² Such tasks form a continuous activity performed by organizations, but often draw on little support from the information technology of the organization.

Not surprisingly, the experts who make these assessments are not equally adept across all disciplines [16], and often they benefit from “comparing notes.” For example, a particular expert may notice that a competitor has recently severed longstanding relations with foreign distributors—as well as having acquired a sizable interest in a foreign manufacturing facility. This competitor appears to be making aggressive moves, preparing to enter new and perhaps sensitive markets. With the help of another expert, one familiar with the geopolitical makeup of the area in question, the fact that the foreign government in question is making serious efforts at economic expansion—requiring foreign business to increase participation in the country’s development—may explain the competitor’s activities.

The director of a well-developed environmental monitoring unit summed up his department's activities as follows: “It’s like putting together a puzzle . . . my people contribute pieces, and after awhile a pattern of what’s going on out there starts to form.” $^{3}$ Within his department, insights and conclusions are shared among others. But, as with many activities that require expert assistance, work stops when the expert is unavailable and can’t share his or her knowledge. This knowledge extends to questions asked, as well as including determining and interpreting the answers given. Also, the expert or senior manager may leave the firm—in which case the continuity of aggregate knowledge or expertise available to the firm is interrupted. At other times, the expert may be unavailable to others requiring her assistance, simply because she is on the phone, at lunch, or in a meeting—making communication difficult, if not impossible.

This paper focuses on multiple agents sharing knowledge in the distributed problem-solving activity of monitoring the business environment. Here, the knowledge to be distributed is not only that which an expert or senior manager uses to identify a pattern of indicators suggesting a threat or opportunity to the organization, but also the knowledge of exactly what indicators are particularly pertinent to the classification problem of current concern. Not only is it important to provide an assessment of information once the right questions have been asked, but it is also useful to know just what those “right questions” are.

In approaching this knowledge-sharing problem, we first discuss environmental monitoring and the methods used to realize it. Second, we present the process of monitoring as an instance of distributed problem solving, and use the theoretical characteristics of distributed problem solving as a point from which to identify research opportunities. Finally, we describe a prototype and an architecture that ameliorates some of the problems that arise when an agent (an expert) in a network of problem solvers is either permanently removed or otherwise unavailable.

## Environmental Monitoring

ENVIRONMENTAL MONITORING FALLS under the aegis of organizational attention—the process of perceiving and interpreting both the internal and external environment for the purpose of making appropriate operational, tactical, and strategic decisions that help to ensure the success of the firm. From these three points of concern (strategic, tactical, operational), there are issues pertaining to individual, group, and organizational performance. Instances of these issues include the following:

\- Bounded rationality and cognitive reapportionment: are there methods available for reducing the limited capacity of individuals in assessing environmental queues and reapportioning them to a technology platform?

\- The phenomenology of enactment: can technology be used to shape the expectations of individuals in recognizing threats and opportunities in both crisis and noncrisis situations?

\- Span of control: can advanced technology provide greater span of control without information loss?

\- Organizational learning, vigilance, and design: how can technology and design aid levels of vigilance and learning in the organization?

\- Boundary-spanning technologies: can shared technological platforms be used as sources of meaningful information?

\- Information refineries: how can the organization better channel and harness the ocean of data and information in which it finds itself?

Environmental monitoring typically matches the capabilities of individuals and groups in identifying strategically relevant events external to the organization. In a series of discussions with personnel from several environmental monitoring units, we found that monitoring in large organizations often requires the cooperative effort of many individuals. In addition, the skills of these individuals fall into two broad categories: (1) those who are adept at finding and evaluating singular pieces of information; and (2) those who are adept at looking at patterns of indicators and recognizing whether those patterns represent relevant threats or opportunities to the organization. The first group of individuals fall under the rubric of “intelligence analysts.” The second group, the experts in some aspect of the external environment such as political events, regulatory measures, competitor financial status, etc., are “area specialists.”

Based on the current goals of the organization, the area specialists decide upon the monitoring of a set of qualitative indicators that might provide insight into various threats and opportunities to the organization. Once the indicators are chosen, the area specialists request estimates from the intelligence analysts of the indicators' values. It is the task of the intelligence analysts to locate and interpret information that will shed light on the disposition of the indicators in question.

In continually evaluating the competitive position of another firm, the area specialist may look for patterns over attributes such as bidding behavior, R&D expenditures or hiring, new manufacturing methods, or suppliers. The area specialist may use his expertise to infer that a very low bid on the competitor's part may indicate several conditions: (1) the competitor's backlog is very low; or (2) the competitor has made a leap in manufacturing methods and can reasonably meet their bid; or (3) the competitor has made a gross error in judgment; or (4) the competitor has linked with a new supplier that, itself, can provide materials at a much lower cost [23]. If R&D hiring has recently increased, and the competitor has invested in a new manufacturing site, technological innovation may be the best explanation for the very low bid. Conversely, if it is known that R&D expenditures have recently been cut and that there has been a hiring freeze, then the area specialist will likely infer that either the competitor's backlog is low or there was a gross error in judgment.

Historically, the scope of these activities represents a distinct departure from the 1960s and early 1970s, when environmental monitoring was largely an informal activity in corporations that relied on personal contacts to capture market/sales-related information [1]. Somewhat more recently (by the mid-1970s), work being produced in the area reflected increased organizational awareness of environmental factors in strategic planning [2, 36]. And, through the 1980s, interest in environmental monitoring has grown, along with the vast increase in the amount of publicly available information about the competitive environment [18, 35].

Still, while research has been done to aid planners in enumerating potential threats and opportunities $[24, 27]$ , analyzing the results of monitoring $[29]$ , and disseminating environmental monitoring conclusions $[9]$ , less attention has been devoted to monitoring patterns of indicators in the external environment. While El Sawy $[11]$ has discussed the activities of CEOs doing their own environmental monitoring, specifically for small to medium-sized firms, a literature search into the application of information technology in the support of the monitoring activity has revealed that there has been little activity beyond providing an E-mail facility to simplify some communication tasks.

## Environmental Monitoring and Distributed Problem Solving

OUR ASSESSMENT OF ENVIRONMENTAL MONITORING entails the recognition that many aspects of distributed problem solving are evident in this process. This section discusses the nature of distributed problem solving and how it relates to environmental monitoring. Further, by examining monitoring from this perspective, research opportunities for IS are identified and elucidated.

Durfee et al. [8] describe distributed problem solving as the outcome of several agents communicating with each other, providing solutions to subproblems, and integrating these subproblem solutions into an overall solution. Generally, each agent has some kind of problem-solving skill at which it is most adept (as well as other, less refined, skills). Moreover, these agents typically share solutions in their endeavor to solve both subproblems as well as “larger problems.”

Generally, there are three dominant approaches to distributed problem solving: (1) multiagent planning $[13]$ ; (2) negotiation $[7]$ ; and (3) the functionally oriented, cooperative approach $[21]$ . Multiagent planning entails the selection of a central planning agent who is given all pertinent information from which to generate a plan. In this scenario, the chosen agent forms a multiagent plan and distributes the plan to the remaining agents in the problem-solving network. Here, a global view of the problem is available and allows activities between agents to be predicted and synchronized.

The negotiation approach accounts for the decomposition of a task into subtasks and the delegation of these subtasks to other agents through some kind of negotiation or bidding protocol. Here, bidding allows specialization, in that agents choose subtasks that are best matched to their capabilities. The subtasks are offered for evaluation to the agents sequentially, making it possible for an agent to commit to a subtask prematurely (in that a subtask offered later might suit its abilities better, but having already committed to another subtask, it cannot take up the current one to which it is better suited).

In a functionally accurate, cooperative approach, agents cooperate by exchanging tentative, partial solutions based on their limited view of the problem-solving network. By exchanging their sometimes inconsistent and inaccurate partial solutions, they converge on a solution. For improved cooperation, these agents need to be made aware of what partial solutions must be exchanged in the future to allow them to alter problem-solving activities to form compatible partial solutions in a timely fashion.

Distributed problem-solving activities like those described above frequently occur in organizations. For example, in keeping with activities that involve the exchange of knowledge and information, the business planning group at SRI has weekly meetings where the individuals doing business intelligence work exchange information and conclusions with their peers (in addition to informal meetings as an ongoing process). $^{4}$ In a similar vein, the environmental monitoring groups at NCR have recently joined activities under one department head in order to better coordinate their efforts in putting together the environmental “puzzle.”

These organizational efforts suggest a tacit confirmation of the theoretical characterization of distributed problem solving. That is, according to Durfee et al.,

better predictions [i.e., plans] in these [distributed problem-solving] approaches have been achieved through organization: by providing nodes with organizational information (the general capabilities and responsibilities of other nodes, the communication patterns between nodes), the agents have a general understanding of each other and can therefore make better predictions.

Furthermore, Reinhardt [30] notes that without proper coordination, 80 percent of the scanning activity may be focusing on only 30 percent of important environmental indicators.

As distributed problem solvers, intelligence analysts and area specialists interact to contribute environmental monitoring information to the organization. As Figure 1 illustrates, intelligence analysts are fully connected to one another in the process of finding information for the area specialists. Moreover, they interact with every area specialist inasmuch as they are all ostensibly available for the purpose of answering information requests. Likewise, the area specialists are fully connected with one another during the process of detecting threats and opportunities to the organization. And, in addition, once a threat or opportunity has been detected, the information is reported by the area specialists to the strategic planning function.

The activities of this particular problem-solving network fit the three most common models of distributed problem solving in the following ways:

Multiagent planning: The strategic planning function acts as a multiagent planner here. Given the goals of the organization, potential threats and opportunities may be identified $[27]$ and then distributed to the various area specialists according to their abilities.

Negotiation: When area specialists send an information request to the intelligence analysts, there may be an opportunity for the analysts to choose which request to expedite. As in the negotiation approach, it is possible for an analyst to commit to a particular request only to find later that another request fits his or her search expertise better than the one originally chosen.

Functionally accurate, cooperative approach: As mentioned earlier, common practice among area specialists includes the sharing of knowledge and solutions, and this is characterized by the functionally accurate, cooperative approach. Here, partial solutions and conclusions are shared, with the intent of reaching conclusions about threats and opportunities to the organization.

In addition to these characterizations of the problem-solving strategies across various parts of the monitoring network, other variants most likely apply. For instance, there are probably some negotiation elements to the process of assigning tasks from the strategic planning function to the area specialists, etc., resulting, in some cases, in a rich mix of distributed problem-solving strategies throughout the network.

Within these distributed problem-solving activities, two levels of activity are evident—one implicit; the other explicit. First, there is a performance perspective implicit in the discussion of problem-solving networks. Specifically, each agent is assumed to be present and operational throughout the duration of the problem-solving process. Second, there is the explicit perspective of planning—that planning is improved through better communication and knowledge of the capabilities of the other agents in the network.

![](/api/attachments/C3B48TP3/fulltext/images/f6cbbec2057246a52332f15626a30ad703fa3bb0dd810b2f05be82e1e6386257.jpg)  
Figure 1. A Distributed Problem-Solving Network for Environmental Monitoring

With respect to this perspective, our primary interest is in addressing both the implicit and explicit opportunities and problems that arise in this kind of organization. That is, we consider both the operational and planning characteristics of the distributed problem-solving process, discussing them in terms of continuity and communication, in sharing knowledge over the network.

## Knowledge-sharing Problems

AN IDEAL DISTRIBUTED PROBLEM-SOLVING ENVIRONMENT, within the context of environmental monitoring, might entail having all area specialists available at all times. The organization would never be without the talents of its monitoring personnel. There would be no telephone tag, no one out to lunch, no turnover or need to retrain. But such a scenario is highly unlikely, both now and in the future.

The fact is, employees do leave the organization, and they do become unavailable because they are on the phone, in a meeting, or out to lunch. When an area specialist leaves the firm, her experience often goes with her, and the continuity of the organization's aggregate knowledge is interrupted [26]. This is particularly difficult for the environmental monitoring unit, since usually no records of the decisions made by the area specialists are kept, $^{5}$ and similar expertise may not be readily available. The choices and recommendations made are neither collected nor catalogued. Moreover, while the area specialists are with the environmental monitoring unit, many of their efforts are often repeated and no “audit trail” of their choices is kept.

While the specialist may be able to contact the knowledgeable party between meetings, that person may be unable to help, or may be unavailable at the necessary times. The problem may be further exacerbated when the desired specialist might, in turn, need to look for yet another specialist with complementary expertise. This form of telephone tag, this interruption in the communication between experts and their planning capabilities, is counterproductive. The end result is often that the requisite information is not provided and the monitoring process suffers.

## Opportunities

By examining the nature of the exchanges between area specialists and intelligence analysts, and the advantages to the organization of acquiring and sharing knowledge, several opportunities for adding value to the monitoring process present themselves. Area specialists typically have the option of using electronic mail to convey their requests for attribute-value data and supporting explanations from an intelligence analyst's findings. This activity can serve as the jumping-off point for adding value via information technology. The specific areas of opportunity that have been identified are:

\- With the comings and goings of area specialists, the performance of the problem-solving network is diminished, the continuity of overall organizational knowledge fluctuates, and the ability of the organization to meet its monitoring requirements suffers. How can information technology help to gather and distribute this knowledge?

\- The inability of several area specialists to coordinate their efforts, through an understanding of the organization's capabilities, to plan their efforts in a reliable and timely manner, hampers the smooth and efficient execution of the monitoring process. How can information technology facilitate communication of this knowledge?

The proprietors of this knowledge are the area specialists themselves; they decide what information to look for and how to interpret findings and observations. Presently, the analysts share their decisions—but not their knowledge—with the organization. An evaluation of possible technologies that might enable managers quickly and unobtrusively to transfer their knowledge to the organization and to delegate some of the more routine tasks to machine subordinates has resulted in the development of the Knowledge Cache architecture presented below.

The Knowledge Cache Approach

situations leads the designer to consider expert systems as a core technology for the representation of monitoring knowledge and in the facilitation of the judgment and analysis activities. It is a premise of expert systems technology that an expert's knowledge about a particular subject can be codified and used in solving a given problem automatically. In the case of augmenting the abilities of an area specialist in performing environmental monitoring, an expert system, in some idyllic sense, would perform the following:

\- decide what information to look for, what attribute-values to acquire;

\- ask the intelligence analyst about the monitoring information required;

\- evaluate the answers and either provide a conclusion or opportunistically decide on what attribute-value to search for next;

\- continue asking questions until a classification of the attribute-values was found;

•inform the area specialist of its conclusions, providing an explanation of the findings.

Concerning this list of requirements, it appears that an expert system might serve to alleviate many of the problems of continuity and communication. For example, if the classification knowledge held by area specialists were to be codified into an expert system, so that the expert system had “expertise” in detecting, say, potential political turmoil, then the system might conduct a dialog with the intelligence analyst, asking the right questions about such attributes as relative deprivation, belief in violence, etc.—classifying the answers using the expert’s knowledge and distributing the answers to those most interested. In considering this goal, available IS technologies such as traditional expert system shells and knowledge acquisition tools have been evaluated for the purpose of identifying useful approaches to alleviating some of the knowledge-sharing difficulties encountered in the monitoring process. To date, current “knowledge-oriented” technologies are not sufficiently robust to address the synchronic and diachronic knowledge-management tasks posed by the environmental monitoring problem. A synchronic problem with the expert system approach, the perspective of the expert system at a fixed point in time, is that the knowledge base is typically monolithic—massive, uniform, and intractable—and would, without modifications. have to examine an excessive number of possible threats and opportunities to an organization, regardless of their level of priority or the frequency with which they should be monitored. From the diachronic perspective, which takes into account the lifetime of the expert system, problems of knowledge acquisition and maintenance exist. Despite the fact that important inroads have been made in speeding up the knowledge acquisition process (using tools such as MOLE [12] and ETS [3]), to build the knowledge base required by the expert system approach would take many hours away from the area specialists—precisely those hours that they would be using to monitor the environment—simply exacerbating the problem to be solved. In addition, the problem of knowledge-base maintenance occurs because, periodically, the goals of the organization change—and with them, the pertinent threats and opportunities to be monitored by the organization. That is, as the organization’s goals change, new threats and opportunities must be monitored. With an expert systems approach, this means that more knowledge acquisition would have to be done—once again taking the area specialists away from their tasks.

To overcome the problems in the expert systems approach, the system in question must be able automatically to assimilate the area specialist's knowledge, organizing it by classes or categories. Also, the necessary system must have the ability to deliver the area specialist's knowledge to other area specialists in a usable form. The system must unobtrusively learn the concepts that the area specialist uses in monitoring the environment, and must make those concepts available to the organization. To address the information technology needs associated with the environmental monitoring activity, the authors introduce a new knowledge-management architecture, termed a "Knowledge Cache" (see Figure 2).

The responsibility of the Knowledge Cache is to learn to gather, classify, and distribute environmental monitoring knowledge that may be used by experts in their day-to-day activities. The Knowledge Cache is a collection of semiautonomous agents, machine subordinates, termed “Apprentices.” These Apprentices act on behalf of a given expert, asking the same questions the experts would normally ask, and to the extent of their previous training, classifying the answers to those questions according to whether a potential threat or opportunity is being presented to the organization. The Apprentice architecture uses some well-known techniques from the artificial intelligence community: a machine learning algorithm $[19]$ , a knowledge base of rules and search heuristics, and a hybrid blackboard architecture.

## Problem-specific Apprentices

The Apprentice's orientation is problem-specific. For example, one Apprentice would be concerned only with recognizing the potential for political turmoil, while another would be concerned only with identifying new technology threats. An Apprentice takes the place of e-mail messages. Instead of using electronic mail messages to communicate questions to an intelligence analyst, an area specialist will use a structured message backed by a semiautonomous agent—an Apprentice.

The functional characteristics of an Apprentice can best be described by an organization doing a particular monitoring activity. For example, when an organization monitors the political climate of a foreign country, the area specialist initiates a request for information by passing a structured message to a particular Apprentice, in fact, creating a new apprentice. The message would state the following:

a) attributes for which the area specialist requires values and the name of the Apprentice—which corresponds to the threat or opportunity being monitored, for example:

Variable: belief-in-coercive-force.

b) an explanation or elucidation of the attributes to better clarify the nature of each attribute being requested, for example:

Explanation: To what degree do mass-antiregime actors believe that coercive force will allow them to achieve their political goals?

![](/api/attachments/C3B48TP3/fulltext/images/3e9d5d7221747cceab97e6635fdd9197edbba577b37602bc9df05e840e9a6c8f.jpg)  
Figure 2. Overview of a Knowledge Cache

c) scaling information specifying the values that are acceptable as answers to the attribute request, for example:

Very strong belief
Strong belief
Some belief
No belief

The questions about the attribute values, together with the explanations and scaling information, are given by the Apprentice to the intelligence analyst. To each of the attribute questions the intelligence analyst responds with a value corresponding to one of the scaled values provided by the Apprentice. In addition, the intelligence analyst may provide a written explanation of why he or she chose a particular scaled value.

Once this is done, the Apprentice carries its new information back to the area specialist. Upon returning to the area specialist with its new information, the Apprentice shows the specialist the answers to the specified questions and asks for a classification. In response, the area specialist may ask for an explanation of one of the intelligence analyst's answers, or may give the Apprentice an assessment, a classification, of the information. With the answer, the Apprentice forms an initial concept that is represented as a collection of attribute-value pairs and a classification.

The next time the area specialist needs information about the same threat or opportunity, it is not necessary to restate the questions, explanations, or scaling information. All the area specialist has to do is send the Apprentice to do its work—it already has the questions and other requisite information. From that point, the Apprentice proceeds to the intelligence analyst, as before, and asks the same questions and receives a new set of answers. With these new answers, the Apprentice returns to the area specialist, and, if the Apprentice has a concept that matches the answers provided by the intelligence analyst, it reports its classification to the specialist. Otherwise, it again asks the area specialist for a classification. And the specialist provides another classification which the Apprentice uses to augment its concepts and make further generalizations.

What is taking place here is that the Apprentice is gathering information from the intelligence analyst and knowledge from the area specialist. The Apprentice asks questions and receives answers from the intelligence analyst, and, in so doing, gathers information. When the Apprentice asks the area specialist what a particular set of attribute-value pairs means, and receives a classification with which to form a concept, the Apprentice is gathering knowledge from the area specialist. In addition, the Apprentice is classifying information supplied by the intelligence analyst inasmuch as when information supplied by the intelligence analyst matches with one of the concepts held by the Apprentice, that information is given the concept's classification.

Besides gathering and classifying information and knowledge, the Apprentice distributes the information and knowledge. The Apprentice distributes the information by delivering it to the requestor. Moreover, in the absence of the area specialist who created a particular Apprentice, that same Apprentice can deliver/distribute both information and classifications to other area specialists requiring such assistance.

## Apprentice Architecture

A PROTOTYPE OF THE APPRENTICE has been developed on a MAC II using Allegro Common Lisp. An Apprentice is made up of three layers (see Figure 3), which together perform the tasks of: (1) gathering, classifying, and distributing the information provided by the intelligence analyst, and (2) gathering, classifying, and distributing the knowledge used by area specialists. The three layers are the concept formation layer, the knowledge source layer, and the blackboard layer.

The concept formation layer makes use of groups of attribute-value pairs, together with the classifications provided by the area specialist, to form generalizations based on regularities in those groups. The knowledge source layer receives knowledge from the output of the concept formation layer. That is, the tree generated by the concept formation layer is parsed to yield a distinct set of concepts that become the knowledge sources for the Apprentice. The blackboard layer acts as the inference engine for the Apprentice, using the search information provided by the knowledge sources to query opportunistically the intelligence analyst for specific values of chosen attributes. A description of the nature and functionality of each of an Apprentice's layers is given in the following section.

## The Concept Formation Layer

The algorithm chosen for the concept formation layer was Unimem [19]. Unimem is a similarity-based learning algorithm that creates a hierarchy of feature-vectors from inputs of labeled sets of attribute-value pairs. Thus, with each new piece of data, Unimem updates its hierarchy.

![](/api/attachments/C3B48TP3/fulltext/images/08622df38edb9f616252ac954facad181105a82bbec80239caf0a8df9197844a.jpg)  
Figure 3. Three Layers of an Apprentice

The classifications of the feature-vectors are identified by either a single label or a disjunction of labels. Within the hierarchy created by Unimem, those feature-vectors close to the root are more general (having fewer attribute-value pairs and more labels) than those near the leaves. Also, the arcs pointing to the nodes in Unimem's hierarchy have predictive attribute-values associated with them. And these predictive attribute-values provide heuristic search information to the blackboard.

Unimem gathers its new inputs of classified attribute-value pairs from the question-answer dialog between the area specialist and the intelligence analyst. The question posed by the area specialist to the intelligence analyst is the attribute, and the answer the intelligence analyst gives is the value. The classification of this information, the judgment call made by the area specialist about the returned information, becomes the label of the attribute-value data.

## Knowledge Source Layer

The knowledge source level is constructed by parsing the hierarchy formed from Unimem. The result is a number of hypotheses that correspond to each of the hierarchy's nodes, together with the arc-labels pointing to them. Thus, a given hypothesis will contain information about both its predictive and predictable attribute-values, as well as the classification given to it. The actual representation appears as follows:

((a red)(c very-fast)((b medium-weight)(d expensive)) (Ferrari Testarossa)

Here, from left to right, there are three groups in this hypothesis: predictive values; predictable values; and a classification label. In this example, if the object in question is red and very fast, it is likely that it is also medium-weight and expensive—more particularly, a Ferrari Testarossa. The values “red” and “very fast” are the predictive values—their presence suggests the presence of the predictable values “medium-weight” and “expensive.” Using this hypothesis, if all four attribute-value pairs are matched, then the conclusion is that the object is a Ferrari Testarossa.

## The Hybrid Blackboard Layer

In the case of environmental monitoring, physical data are not being represented, and the problems under consideration are not organized by multiple levels of granularity. Hence, while a blackboard will be used for the purpose of exhibiting global data to the various knowledge sources, neither multiple levels nor links will be employed. The knowledge sources correspond directly to the concepts developed by the concept formation level of the Apprentice. And, using the predictive information provided by the concept formation level, along with the varying degrees of specificity of the knowledge sources (the more attribute-value pairs that describe the concept, the more specific it is), the control or search method is opportunistic.

Together, these three layers affect the required functionality of the Apprentice. The concept formation layer is put to use when the Apprentice “asks” the area specialist about the meaning of a classification. The classification given is used, along with the attribute-values provided by the intelligence analyst, to augment the concepts via the learning algorithm. The output of Unimem is put into the knowledge sources, which are used by the blackboard to conduct the dialog with the intelligence analyst. Thus, different parts of the Apprentice’s architecture are used according to the individual with whom the Apprentice is interacting. The blackboard and knowledge sources are used with the intelligence analyst, and the concept formation layer is used with the area specialist.

## Case Study

TO ILLUSTRATE THE FUNCTIONAL CHARACTERISTICS of an Apprentice in a “real-world” application, an archival case study $^{6}$ was performed concerning a multinational corporation $^{7}$ monitoring the political climate of Poland in the summer of 1980 [10]. Here, an “area specialist” monitored the political climate of Poland in the summer of 1980 while an Apprentice captured knowledge about how to act in the absence of that same “area specialist.”

The actual area specialist used was a composite of attributes, values, and rules employed by political analysts in identifying the likelihood of political turmoil. A well-known approach to analyzing the political climate of a country was developed by Gurr [15]. His model takes into account a number of qualitative indicators to assess a country's political well-being or the likelihood of an outbreak of political violence. These attributes were used in illustrating how an area specialist would seek and classify information about Poland. They are explained in Table 1.

With these variables, the area specialist in the case study projected the likelihood and type of violence that might have occurred in Poland. The events that are relevant to this case study take place in a short period of time—two months. The “high points” of this period of time are chronicled in Table 2 $^{8}$ [6, 37].

Applying the variables from Table 1 to the events in Table 2, with an analysis performed every week and the area specialist classifying the feature-vectors he received via an Apprentice, the Apprentice generated the knowledge base shown in Figure 4 (as of August 23). There are three possible classifications of the likelihood of political turmoil in this knowledge base thus far: somewhat likely; likely; and highly likely. The attribute values in the top layer of the tree are the predictive values used by the blackboard in selecting a search strategy. The values in the middle layer of the tree are the predictable values that follow from the occurrence of the predictable values. If all values match the available information, then the appropriate classification at the bottom of the tree is chosen.

Using this knowledge base, the Apprentice was allowed to do its own analysis of the events up to and including August 24 (the assumption being that the “area specialist” had taken a vacation). In this case, when it was the Apprentice’s “turn” to classify the political information (see Table 3), the Apprentice noted that the information fit two classifications: “PT: somewhat likely” and “PT: likely.” Had the area specialist been present, undoubtedly only one classification would have been provided. This fact supports what we would intuitively believe of an Apprentice—that is, after “existing” for only six weeks and having seven learning experiences, it is not going to be as good at classifications as an established expert. Nevertheless, the Apprentice was able to provide a useful indication of what the pattern of qualitative political data meant. The strategy of an Apprentice is conservative. It identifies only what it has already observed or some subset of what it has already observed. If it is confronted with a pattern completely unlike anything it has come across before, it defers “judgment” and asks for a classification.

This case illustrates how an Apprentice can be successfully used to capture knowledge about “real-world” information and established methods of classifying that information. At any time during the period discussed above, the other area specialists of this hypothetical organization also had access to the Apprentice monitoring political violence in Poland. For example, during the Solidarity movement, the stock market fell over a period of time while the price of gold rose. Investment personnel might have chosen to use the Apprentice as one of the inputs to their investment decisions—and they could continue using it in the originating area specialist’s absence. Finally, had the area specialist responsible for the creation of the political violence Apprentice

Pro-Regime Relative Deprivation—a measure of the extent to which members characterized as pro-regime feel frustrated regarding their economic condition and general welfare.

Anti-Regime Relative Deprivation—a measure of the extent to which members characterized as anti-regime feel frustrated regarding their economic condition and general welfare.

Pro-Regime Belief in Violence—a measure of the extent to which members characterized as pro-regime believe that, given the practical opportunities and limitations of the current political situation, violence is justified on either pragmatic grounds, or on moral, doctrinal, and historical grounds.

Anti-Regime Belief in Violence—a measure of the extent to which members characterized as anti-regime believe that, given the practical opportunities and limitations of the current political situation, violence is justified on either pragmatic grounds, or on moral, doctrinal, and historical grounds.

Coercive Support for Pro-Regime—a measure of the extent to which pro-regime members are supported, in terms of equipment, training, size, strategic location, and loyalty of armed manpower, from within and without the country.

Coercive Support for Anti-Regime—a measure of the extent to which anti-regime members are supported, in terms of equipment, training, size, strategic location, and loyalty of armed manpower, from within and without the country.

Institutional Support for Pro-Regime—a measure of the extent to which pro-regime members are supported, in terms of organizational cohesion and the size and geographic location of their resources, as well as psychological, economic, and political support short of coercive force, in achieving their objectives.

Institutional Support for Anti-Regime—a measure of the extent to which anti-regime members are supported, in terms of organizational cohesion and the size and geographic location of their resources, as well as psychological, economic, and political support short of coercive force, in achieving their objectives.

Success of Anti-Regime Movements Outside of Country—a measure of the extent to which anti-regime members outside of the country have succeeded in achieving their own political objectives.

left the firm, instead of just being away on vacation, his replacement would have had an immediate starting point, using the Apprentice, from which to continue his predecessor's work.

## Planning and Performance Effects

FIGURE 5 ILLUSTRATES AN INSTANCE of the problem-solving network when an unavailable area specialist has Apprentices acting in her place. From a distributed problem-solving perspective, one of the concerns being addressed through this kind

July 1: The Central Committee announces a large hike in meat prices.

July 2: The first strike breaks out in the Ursus plant near Warsaw. The strike was for higher wages to cover the increased meat prices.

July 9: Central Committee First Secretary Gierek makes a public statement that no broader wage increases will be allowed, but workers continue striking.

July 16: Strikes spread to nearby Lublin.

July 27: Gierek goes on holiday to Moscow, and does not return until August 14.
August 15: Telephone lines to Gdansk are cut.

August 16: Representatives from twenty-one enterprises convene in Gdansk to form the interfactory strike committee (MKS), a group formed to coordinate strike action, promote solidarity, and begin broadening demands to include political concessions.

August 18: The MKS continues to grow, while Gierek makes a television speech that no political concessions will be made with the strikers.

August 19: Dissidents are arrested on a widespread basis.

August 23: Barcikowski, the deputy prime minister, begins talks with the MKS on national television.

August 24: Four top Central Committee members are relieved of their posts.

August 30: The Gdansk agreement is signed, guaranteeing the right to strike and self-governing trade unions.

of temporary replacement, through the development of numerous Apprentices, is performance. Because the area specialist cannot always be available to answer to the needs of her peers, performance will suffer without the addition of these surrogates. Thus, as other area specialists can send an Apprentice to work on monitoring without the presence of the Apprentice's author, the continuity in the aggregate level of organizational knowledge is somewhat restored.

Also of concern are the planning capabilities that are enhanced by the addition of the Apprentices. The ability of area specialists to browse through the contents of their peers' Apprentices affords them a greater understanding of the location and strength of the organization's knowledge-oriented resources. Thus, making plans with either the negotiation or functionally accurate/cooperative approach is, by definition, more easily realized.

## Conclusion

WITH THE SPEED OF ACTION AND REACTION in the business environment, the future role of efficient and effective environmental monitoring will be increasingly important. While information technologies have, to date, played only a minor role in the support of the monitoring process, this situation is changing [5]. If the organization should decide to address the problems of continuity and communication in the realm of environmental monitoring, the approach discussed offers some potential for structuring an environment where information plays an active role in both the management of knowledge and the active search, interpretation, and judgment processes that occur in the environmental monitoring process.

![](/api/attachments/C3B48TP3/fulltext/images/610fa06720cd4d1f76ee2e5de5db3ad8e6502ca37789c07adf8cd716463ed0b7.jpg)  
Figure 4. Knowledge Base of an Apprentice

Table 3 Attributes, Values, and Explanations for Political Events on August 24

<table><tr><td>Pro-Regime Relative Deprivation</td><td>Low</td><td>The pro-regime party has enjoyed special privileges for some time</td></tr><tr><td>Anti-Regime Relative Deprivation</td><td>High</td><td>The economic conditions of the workers have not improved, but declined over the past decade</td></tr><tr><td>Pro-Regime Belief in Violence</td><td>Moderate</td><td>Gierek agreed to unions holding secret elections on the 25th - indicating continued efforts at cooperation</td></tr><tr><td>Anti-Regime Belief In Violence</td><td>Moderate</td><td>Continued success of MKS in getting secret elections will further convince strikers of soundness of organized approach</td></tr><tr><td>Pro-Regime Coercive Force Available</td><td>Strong</td><td>The Polish Army and Police are supportive of the party and the Central Committee</td></tr><tr><td>Anti-Regime Coercive Force Available</td><td>Not Strong</td><td>The Polish workers are not armed and little armed support for them exists outside of their country</td></tr><tr><td>Pro-Regime Institutional Support</td><td>Low</td><td>Gierek&#x27;s concessions to the unions will only further polarize the already divided party and Central Committee</td></tr><tr><td>Anti-Regime Institutional Support</td><td>Strong</td><td>Achievement of political gains in terms of secret elections will further strengthen the resolve of the strikers</td></tr></table>

The Knowledge Cache approach also lends itself to other complex analysis problems that involve continuous monitoring and interpretation activities by multiple experts. For example, in a recent Harvard case study $[28]$ , a major software vendor planned to ease the workload on its customer service representatives with the introduction of expert system technology. The vendor received over 330,000 calls annually, and wished to create bulletin board software that kept clients abreast of new company products as well as an e-mail service to get help from the service representatives. The plan included having customers interact with an expert system instead of with the service representative, and if the expert system could not provide an answer, then the representative would take over by entering into the e-mail dialog.

![](/api/attachments/C3B48TP3/fulltext/images/eeabbdcbb1d860b921c9cb3117ea3ac94e160beff3bbd301854418b214d80c8c.jpg)  
Figure 5. Problem-Solving Network with Apprentices

Besides differentiating themselves from their competitors, the firm believed that the expert system would help reduce the service representatives' workload and encourage them to remain at their jobs longer (their average length of job service was twenty months, and the cost of retraining was viewed as significant). Thus, the plan found encouragement from many individuals within the company. Unfortunately, the endeavor ultimately failed because of the large knowledge acquisition effort required to bring the project online, along with meeting resistance on the part of the service representatives to spend additional time helping to build the system.

If the project leader had had access to the Knowledge Cache approach, the project might have been successfully completed. Time for accomplishing knowledge acquisition would not have been required of the service representatives because the Apprentices would learn by observing the problem-solving process: watching the customer report the nature of the problem (e.g., “I’ve got an abend”); watching the questions asked of the customer by the service representative (e.g., “Was it a system abend?

A user abend? Was there a console message? none of the above?”); and noting the classification to the problem. The process is a redundant one and there are ample opportunities for learning to classify these questions and answers as attribute-value pairs.

This example, of the firm that sought to apply expert systems technology to the customer service problem, is one where the generalizable characteristics of the Knowledge Cache could be used. The organization wished to reduce its service representative turnover as well as its training costs. It had periodic gaps in the continuity of knowledge available to the firm because of the employee turnovers. Furthermore, by allowing the Apprentices to look after the more routine tasks, the service representatives could have had more time to address the tougher, more challenging problems. Here, as with the environmental monitoring problem, the Knowledge Cache would be used to capture and reuse the knowledge of experts where a “traditional” expert systems approach lacks feasibility. Finally, it is hoped that other applications with similar characteristics will be amenable to a Knowledge Cache approach.

The application of information technologies to support the reapportionment of cognitive responsibilities is an emerging theme in organization design. Such redesign of organization responsibilities and restructuring of authorities suggests a review of the notion of span of control. The technologies discussed earlier can play a critical role in the reassessment of roles and responsibilities, and can enable organization learning that may impact the long-term structure and performance of the enterprise. With the application of these technologies in boundary-spanning systems and information refineries, we may be able to revisit many aspects of strategy and structure.

## NOTES

10. Elofson, G.S. Facilitating knowledge sharing in organizations: semi-autonomous

monitoring the political climate of foreign countries as part of their daily operations.

8. It should be noted that this information was widely available during this time period. For example, from July to November, the New York Times printed a front-page story on Poland every 2.5 days.

## REFERENCES

1. Aguilar, F. Scanning the Business Environment. New York: Macmillan, 1967.

2. Ansoff, H.I. Managing strategic surprise by response to weak signals. California Management Review, 18, 2 (Winter 1975), 21-33.

3. Boose, John H. A knowledge acquisition program for expert sztems based on personal construct psychology. International Journal of Man-Machine Studies, 23 (1985), 495-525.

4. Cleland, D.L., and King, W.R. Competitive business intelligence systems. Business Horizons (December 1975), 19-28.

5. Clippinger, J.H., and Konsynski, B.R. Information refineries: electronically distilling business' raw material to make it more useful. Computerworld, August 28, 1989, 73-77.

6. Cynkin, T. Soviet and American Signalling in the Polish Crisis. Hong Kong: Macmillan, 1988.

7. Davis, R., and Smith, R.G. Negotiation as a metaphor for distributed problem solving. Artificial Intelligence, 20 (1983), 63-109.

8. Durfee, E.H.; Lesser, V.R.; and Corkill, D.D. Cooperation through communication in a distributed problem solving network. In Michael N. Huhns, ed., Distributed Artificial Intelligence. Los Altos, CA: Morgan Kaufman Publishing, 1987, 29-58.

9. Eels, R., and Nehemikis, P. Corporate Intelligence and Espionage. New York: Macmillan, 1984.

agents that learn to gather, classify, and distribute environmental scanning knowledge. Ph.D. dissertation, University of Arizona, 1989.

11. El Sawy, O.A. Personal information systems for strategic scanning in turbulent environments: can the CEO go on-line? MIS Quarterly (March 1985), 53-60.

12. Eshelman, L., and McDermott, J. MOLE: a knowledge acquisition tool that uses its head. Proceedings AAAI-86, August 1986, Philadelphia, PA, 950-955.

13. Georgeff, M. Communication and interaction in multi-agent planning. Proceedings of

the Eighth International Joint Conference on Artificial Intelligence, August 1983, 125-129.

15. Gurr, T.R. The conditions of civil violence; first tests of a causal model. Princeton University, Center of International Studies, Research Monograph no. 28, 1967.

16. Hambrick, D.C. Specialization of environmental scanning activities among upper level executives. Journal of Management Studies, 18, 3 (1981), 299-320.

17. Heuer, R.J., Jr. Quantitative Approaches to Political Intelligence: The CIA Experience. Boulder, CO: Westview Press, 1978.

18. Kennedy, C., Jr. The external environment–strategic planning interface: U.S. multinational corporate practices in the 1980's. Journal of International Business Studies (Fall 1984), 99-108.

19. Lebowitz, M. Generalization from natural language text. Cognitive Science, 7 (1983), 1-40.

20. Lebowitz, M. Classifying numeric information from generalization. Cognitive Science, 9 (1985), 285-308.

21. Lesser, V.R., and Corkill, D.R. Functionally-accurate, cooperative distributed systems.

IEEE Transactions on Systems, Man, and Cybernetics, SMC-11, 1 (January 1981), 81-96.

22. Montgomery, D.B. The freedom of information act: strategic opportunities and threats. Sloan Management Review (Winter 1978), 1-13.

23. Montgomery, D.B., and Weinberg, C.B. Towards strategic intelligence systems. Journal of Marketing (Fall 1979), 41-52.

24. Nanus, B. QUEST—quick environmental scanning technique. Long Range Planning

(September 1982), 39-45.

25. Neubauer, F.F., and Soloman, N. A managerial approach to environmental assessment. Long Range Planning (April 1977), 13-20.

26. Neustadt, R.E., and May, E.R. Thinking in Time: The Uses of History in Decision Making. New York: Free Press, 1986.

27. Nunamaker, J.F.; Weber, E.S.; and Minder, C. Organizational crisis management systems: planning for action. Journal of Management Information Systems, 4, 3 (Spring 1989), 7-32.

28. Porter, L. McDonald and Denny, Inc.: the Keeps Project. Harvard Case Series, No. 9-187-001, 1986.

29. Porter, M. Competitive Strategy. New York: Free Press, 1980.

30. Reinhardt, W.A. An early warning system for strategic planning. Long Range Planning, 17, 5 (1984), 25-34.

31. Rosner, M.M. Administrative controls and innovation. Behavior Science, 13 (1968), 36-43.

32. Selznik, P. TVA and the Grass Roots. Berkeley: University of California Press, 1949.

33. Smith, D.C., and Prescott, J.E. Demystifying competitive analysis. Planning Review (September/October 1987), 8-13.

34. Terry, P.T. Mechanisms for environmental scanning. Long Range Planning, 10, 3 (June 1977), 2-9.

35. Thomas, P.S. Environmental scanning—the state of the art. Long Range Planning, 13 (February 1980), 20-25.

36. Wall, J. What the competition is doing: your need to know. Harvard Business Review (November/December 1974), 22-38.

37. Weydenthal, J. The Polish Drama: 1980-82. Lexington, MA: Lexington Books, 1983.
38. Zink, D. The Political Risks for Multinational Enterprises in Developing Countries. New York: Praeger, 1973.

APPENDIX: Some Notes on the Implementation

of the Knowledge Cache

## Distributing Knowledge

THE APPRENTICE SYSTEM HAS BEEN IMPLEMENTED on a MAC II using Allegro Common Lisp, and is capable of learning to gather attribute-values from an intelligence analyst as well as classifying information; additional capabilities are being provided to make it possible for the system to deliver classification services to the area specialist who requests them. The primary components of this architecture are the files of Apprentices and the ISO X.400—electronic envelope—communications protocol (Figure A1). Each file holds the Apprentices belonging to any given area specialist, and the files are open to all other specialists. This means that area specialists have access to another's Apprentices. That is, they may send them and receive them. But only the owner of an Apprentice may make classifications for that Apprentice. Thus, in the absence of a particular area specialist, others may use his Apprentice to identify threats and opportunities to the organization.

The X.400 protocol allows an Apprentice to be sent back and forth, from area specialist to intelligence analyst and back. The components of this protocol are the User Agent (UA), the Message Store (MS), and the Message Transfer Agent (MTA). The responsibility of the UA is to accept and “package” an Apprentice for routing to other individuals. The UA delivers the Apprentice to the MS, which has the task of acting as an intermediary between the UA and the MTA. The MS has the responsibility of storing and permitting retrieval of delivered messages. It allows the submission from and alerts to the UA. The MTA takes care of the actual transfer of messages from one message store to another—so that the MTA takes an Apprentice from a sender's MS and delivers it to a receiver's MS. Moreover, the receiving MS alerts its UA of the incoming message. Thus, with this basic architecture, the users of the system are able to select, create, and send Apprentices throughout the system.

## Structuring Messages

While there is flexibility in generating an Apprentice, there is also a need for structure. For example, why must the Apprentice have a structured message? The answer is simple: there is really no other satisfactory way of identifying the attributes used by the area specialist. If the area specialist were to use an unstructured message, the attributes could not be identified. Moreover, scaling information is required of the area specialist to limit the number of answers that an intelligence analyst can provide. The number of synonyms that different intelligence analysts could conceivably use to express the same opinion is potentially very large, and the simple matching procedure used by an Apprentice is unable to recognize that two answers might be synonymous.

In keeping with this approach of generating structured messages, several alternatives are available to the user of the Knowledge Cache:

1. Make a new Apprentice: enacts the sequence of screens that permits an area specialist to create a new Apprentice.

2. Give Apprentice attributes: requires the area specialist to name the new Apprentice and set down the attributes for which values will be sought.

3. Provide explanation of attribute: requires a brief written explanation of each attribute name, to be read by an information analyst in case the attribute name is not self-explanatory.

4. Provide scaling values: requires a list of acceptable responses for each attribute request.

5. Analyst reads/answers message: allows the information analyst to receive Apprentice requests and to provide responses with required attributes.

6. Analyst explains answer: for each scaled value provided, the information analyst gives an explanation.

7. Area specialist reads attribute values: the attributes, together with the values and explanation provided by the information analyst, may be read by the area specialist.

8. Area specialist reads and classifies information: a classification of the Apprentice's information is provided by the area specialist, given that the Apprentice does not have a classification of its own.

In choosing to approach the synonym problem this way, it was assumed that an area specialist and an intelligence analyst would be able to adapt to this small change. Eels and Nehemikis [9] have analysts scale their estimates of political conditions, indicating that this assumption was warranted. In the event that an individual using the available scaled values was unsure of whether their meaning was being properly communicated, a facility for adding an explanation was made available. Thus, when an intelligence analyst answers a question with one of the supplied values, he has the option of elaborating his findings in the “remarks” section of the suggested interface—making clear exactly what he meant to the area specialist. This feature of making remarks has the additional role of reducing the magnitude of change between using an Apprentice and using the standard e-mail message—where the intelligence analyst could always explain his answers.

![](/api/attachments/C3B48TP3/fulltext/images/019be8e1037134d13a5835d140dfae02207c4a4bbdb60f0813513675b519f0e0.jpg)  
Figure A1. Supporting Architecture of a Knowledge Cache

## Contending with a Surfeit of Knowledge

Some decisions on particular characteristics of the Knowledge Cache will be largely dependent on the working environment in which it is housed. For example, it is conceivable that two area specialists will have overlapping expertise, and that two Apprentices could be made that perform, primarily, the same function. Under these circumstances, the question of which Apprentice is best to use may arise. Which Apprentice will provide the best answer? The problem is not entirely unlike the problem of having two watches and not knowing what time it is. Still, it may be necessary to choose between the two Apprentices. In this case, the monitoring group may make the choice based on several criteria: (1) which one has shown the “best” performance (“best” being a measure of prediction accuracy); or (2) which one is the cheapest to use (as in which one requires the lowest cost for gathering information); or (3) which Apprentice has been in existence longer (where duration of existence is a measure of goodness). The list of considerations could conceivably be quite long, and the final choice would probably reflect the implicit and explicit policies and preferences of the environmental monitoring unit in question.

Another consideration whose resolution would probably be largely dependent on the environmental monitoring unit in question is the presence of “too many Apprentices.” This hypothetical problem would occur when a coworker wished to use another’s Apprentices, because that other person was unavailable, and the number of Apprentices under that person’s charge was too large to be used readily. Here, there would be either so many Apprentices to choose from, or two or more Apprentices would appear to be so similar that a user would be unable to make an intelligent choice. Again, the choices made to ameliorate this problem would reflect the preferences, policies, and probably the budget of the environmental monitoring unit. One approach would be to provide a hypertext-like interface to the Apprentices, such that they could be chosen through a hierarchy of categories—presumably with the help of an individual whose job is to maintain this extra system, and possibly with only the cooperation of the area specialists. Another way might be to add a key word list to each agent, specifying the threats and opportunities for which they have been built.

Finally, the typical information request of an area specialist is for qualitative data, and the Apprentices have been constructed with this in mind. There may, however, be instances where an area specialist requests quantitative data. For example, an area specialist may want to know the current oil production, in barrels, for a particular geographic region. In this case, while the intelligence analyst could answer, say, 5,000 barrels, the Apprentice would probably not find the answer very useful. In other words, for the purposes of matching and learning, “5,000 barrels” would be regarded as different from “5,001 barrels”—but to the area specialist these two numbers would, for all practical purposes, be the same.

The inability of an Apprentice to cluster numeric data is a limitation of the system. If it became necessary at some point in time to add this capability, Lebowitz [19] provided an algorithm that clusters numeric data and also works with Unimem. Of course, it would be possible for the area specialist to use his or her choice of scaling data to create artificial clusters. For example, in asking for oil production, she could specify that the replies must be as follows: 0–5,000; 5,001–25,000; 25,001–100,000; more than 100,000 barrels per day.
