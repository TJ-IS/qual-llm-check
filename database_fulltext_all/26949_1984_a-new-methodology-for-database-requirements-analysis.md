---
otero_id: 26949
otero_key: "VH4QBBQT"
title: "A New Methodology for Database Requirements Analysis"
authors: "Prabuddha De; Arun Sen"
year: "1984"
journal: "MIS Quarterly"
doi: "10.2307/248665"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A New Methodology for Database Requirements Analysis
Author(s): Prabuddha De and Arun Sen
Source: MIS Quarterly, Vol. 8, No. 3 (Sep., 1984), pp. 179-193
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248665

Accessed: 08/05/2014 18:31

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A New Methodology for Database Requirements Analysis

By: Prabuddha De
College of Administrative Science
The Ohio State University
Columbus, Ohio 43210

By: Arun Sen
College of Business Administration
University of South Carolina
Columbia, South Carolina 29208.

## Abstract

This article presents a systematic methodology for requirements analysis in database design. The procedure begins with an interview with the user/decision maker. The responses collected during the interview are analyzed to represent, by means of a diagram, the data and processing requirements for the activity under consideration. The diagram uses two fundamental constructs, events and states, as building blocks. It depicts any temporal or causal relationships, as well as logical operators, that may be present in the process underlying the activity. The representation is compact and easy to follow. An experimental study is described to illustrate the applicability of the methodology.

Keywords: Information requirements analysis, database requirements analysis, data, decision and activity analyses, events, states, temporal and causal relationships, logical operators.

ACM Categories: D.2.1, H.1.0, H.2.0

## Introduction

Although a fair number of articles have appeared over the years dealing with information requirements analysis in general, a relatively small amount of work has so far been reported that addresses the issue specifically in terms of database design. Database researchers, with few exceptions, have not paid much attention to it, perhaps because it is usually unstructured, cumbersome in nature, and traditionally manual. To many of them it is more of an art than a science and does not deserve a great deal of scientific attention. Nevertheless, it is the first step in any database design and, if this step is not carried out properly, the entire design is likely to be faulty. Hence, the importance of this task must not be overlooked or underestimated. A systematic (and perhaps standardized) procedure is needed for information requirements analysis in order to ensure an effective design. Such a procedure is presented here.

This article discusses various approaches that have been suggested for information requirements analysis in general. A comparison of these approaches is then made, which leads to a proposed model for requirements analysis in the context of database design. Finally, an experimental study is described to show the applicability of the methodology.

## Previous Work on Requirements Analysis

The need for a formal way of documenting data requirements has long been recognized. A close scrutiny of the literature in the area reveals that the techniques suggested so far follow three main avenues $^{1}$ : data analysis, decision analysis, and activity analysis.

## Data analysis

According to Munro et al. [23], the data analysis approach is characterized by examining reports, files, and other information sources which management currently uses for decision-making. The manager is then asked to state any additional information requirements. The resulting collection of data is analyzed from the standpoint of perceived needs, and the portion of the data for which there is no perceived need is discarded.

This approach is the traditional bottom up approach and has been in use for a long time. While Munro examines the merits of this methodology, Chadler, et. al., [9] provide a procedure for its practical use. In their procedure, the organization under consideration is decomposed into several functions, and documents are collected for each function. By decomposing the documents further, by means of “tree explosion,” it is possible to get to the data elements needed in the organization.

## Decision analysis

Decision analysis is characterized by its focus on decisions at the managerial level of the organization. For each management-oriented application, this approach requires identification of the critical decisions. Once these critical decisions are identified, each of them is thoroughly discussed with the responsible manager and then carefully analyzed and modeled, usually by a decision flowchart. The decision flowchart indicates a set of discrete steps which the decision maker takes to make the decision. An analysis of these steps determines the information required.

Typically, the decision analysis approach is supported by those who hold the belief that decisions define all information requirements, and that an effective design is only possible if a model of the decision process is developed first. Ackoff [1] cites several erroneous assumptions made by systems analysts that result in improperly designed systems, and recommends decision analysis as part of the solution. Keen and Scott Morton [18] emphasize the need to identify “key decisions” as the first stage in decision support system (DDS) design. They feel that “if one then assesses the quality of informational and analytical aids for each key decision, one can begin to get a sense of potential priorities for more detailed analysis”

[18, p. 173]. King and Cleland [19] also use a decision analysis approach in determining the information requirements for strategic planning in a police department.

## Activity analysis

Activity analysis is characterized by identifying managerial activities in an organization. In a widely accepted analysis, Anthony [2] classified organizational activities into three different levels: strategic planning, managerial control, and operations control. Strategic planning is the process of deciding the objectives of the organization, the resources to be used to attain these objectives, and policies that govern the acquisition, use, and disposition of these resources. So, strategic planning is the process of formulating long-range plans and policies that determine the character of an organization. Management control is the process by which managers ensure that resources are obtained and used effectively in the accomplishment of the organization's objectives. Finally, operations control is the process of ensuring that specific tasks are carried out efficiently. While most researchers perceive these different levels of management activities in an organization, the boundaries between them may not be very distinct. Nevertheless, these levels have proven to be useful in the analysis of information systems.

Anthony's typology allows for the description of information needs for all levels of management activities. The information needed by the strategic planners is aggregate; the scope and variety of this information varies extensively. By contrast, the information needs of operations people are well defined, narrow in scope, and require detailed statements. The information requirements for management control fall between those of strategic planning and operations control. In the literature, activity analysis is used for analyzing information needs both directly and indirectly.

## Motivation for the Proposed Work

Sometimes it may not be clear from the literature what is actually meant by requirements analysis. This apparent confusion stems from the fact that certain terms are used rather loosely in this area. For example, one seldom makes a distinction between information requirements analysis (IRA) $^{2}$ and database requirements analysis (DBRA) although, strictly speaking, they are quite different. IRA refers to the analysis of user requirements in terms of designing an entire system. This analysis is broad, and triggers all types of systems analysis — even evaluation of hardware and software. DBRA, on the other hand, is concerned with the database only. Its aim is to perform a detailed analysis of the problem environment in the real world from the point of view of database users in order to capture their data and processing needs. Typically, it is the first step in the database design process, as shown in Figure 1.

A large body of literature exists for IRA. Only recently, however, has research been reported in the DBRA area in particular. Nijssen [25, 26], in his coexistence model, argues that different users prefer different mental models in their universe of discourse and, consequently, a conceptual model for information structure should allow different data models to coexist. The basic building blocks of his framework are atomic objects, roles these objects play, names, classifications, atomic sentences, and constraints. Bachman [3, 4] emphasizes the need of data structure models. Gerritsen [14] uses CODASYL-type structures in designing his tools for the automatic design of databases. Hubbard and Raver [16, 28] utilize data elements, attributes, and their relationships as fundamental constructs, in the database design aid (DBDA) software. Wiederhold and El-Masri [35] offer a structural model which is an extension of the relational model, but which also captures information about relationships so that the various relationships can be connected to one another.

As Kahn [17] points out, an effective mechanism for DBRA must consider the information structure as well as the process structure. The information structure depicts the natural data relationships in the system, while the process structure describes how various types of data are used in order to facilitate and satisfy the processing requirements in the organization. A major shortcoming of all the approaches described above is that they typically concentrate on the information structure only.

![](/api/attachments/VH4QBBQT/fulltext/images/b87760f07d95ae51f28e6d30024af2ac92837c8a04cc03ba53aa7593e822aa72.jpg)  
Figure 1  
Source: Navathe, S.B. and M. Schkolnick, "View Representation in Logical Data Base Design," Proceedings of ACM SIGMOD, June 1978, pp. 144-156.

Recently, however, some DBRA researchers have made an attempt to incorporate the process structure in their approach. At the system design level this can be found in the research on PSL/PSA [29, 30, 33], and later in the work of Konsynski, et al., [20]. At the data design level similar attempts have been made by Bubenko [7, 8], Brachi, et al. [6], and Hsu, et al. [15]. They all agree that a data model should contain objects (or entities), their properties, and their associations (relationships) with one another. The process structure is introduced by means of an entity, called an event, which is basically used as a timestamp. The aim is to capture the semantics of a process in terms of its key events. However, none of these authors goes into the details of formalizing a complete model. Furthermore, since events are treated merely as timestamps, such a model could only handle temporal relationships. The model to be presented in this article not only represents temporal relationships, but depicts causal relationships as well. In addition, it incorporates logical operations.

In order to generate a formal model for DBRA, the first and foremost issue that needs to be resolved is the following: Where do we start? Do we use data analysis, decision analysis, or activity analysis?

According to Munro [22], data analysis is not directly linked to management behavior. This approach is also highly dependent on the ability of a manager to articulate his or her information needs accurately. It is generally accepted that managers often do not know their information needs precisely, so data analysis may not be a useful starting point for DBRA.

Several criticisms can be raised against the decision analysis approach also. It is usually quite difficult to predict future decisions, but if a database is designed based on current decisions only any subsequent change in decisions would require a change in the database structure. Designing a database for a specific set of decisions not only reduces the number of decisions it can support, but it also leads to an increased overall cost. Actually, decision-oriented database design will produce a database that is effective only for a short period of time and for a small scale operation. This is because only under these circumstances can most future decisions be forecasted effectively. For a larger system with a longer estimated life, this approach may not even be workable.

We need to isolate critical decisions, but how do we do that in practice? Do we consider only those decisions that are important now, or the ones that may become important later, or both? Finally, how many decisions have to be analyzed to build a good database? Apparently, the number of such decisions is quite large for a moderate sized system and, consequently, the analysis is likely to be a formidable task. Because of these inherent shortcomings, decision analysis is perhaps not the proper starting point for DBRA.

Some of the same questions might also arise for activity analysis, but the task is much simpler in this case since activities are more stable than decisions. Data requirements for an activity are more predictable and change less frequently [13]. Activity analysis appears to be a better starting point for DBRA.

As mentioned earlier, several authors [10, 17, 21, 29-33] have alluded to activity analysis either indirectly or directly. Most of them, such as Ross [29], speak of “functional specifications” for activity definitions. Teichroew [32] provides a list of several “requirement statement languages (RSL)” that use functional specifications. However, all of these are designed for IRA as a whole, and do some DBRA only as a component. Typically, these projects are too ambitious, take a long time for development, and often get abandoned rather quickly. This is evident from the table provided by Teichroew [32, p. 1210] which classifies only 3 RSL’s to be in use out of the 24 reviewed.

This discussion suggests that some type of activity analysis should be developed to deal only with DBRA. Miller [21] provides a conceptual model of graphs for determining information requirements. The graph uses nodes to represent managerial actions, operations, inputs, outputs, and factors influenced. The arcs are used to represent effects and influences of management. The idea is appealing, but it suffers from the fact that the graph is very detailed and involved, and probably will be extremely large even for a small problem. A similar model is needed at a more macro level. The purpose of the next section is to formalize such a model.

## The Proposed Model

The proposed model, to be called an Event-State (ES) model, is based on the following concepts.

## Events

An event is an occurrence or happening of something in the environment under consideration. An order arrives, the meeting ends, or a plan is finalized, are examples of events. Events have the following characteristics:

1. An event represents an action of some kind, so it is typically described by means of a verb, such as arrive, stop, finalize, etc.

2. Every event $E_{i}$ has a start time $t_{S}(E_{i})$ and a finish time $t_{f}(E_{i})$ . The duration of the event is given by $t_{f}(E_{i}) - t_{S}(E_{i})$ .

3. An event can have zero duration, i.e., it is possible to have $t_f(E_i) = t_s(E_i)$ . For example, the event (a supply arrives) may be caused by something outside the environment under consideration. However, when it is considered for that environment, its start time appears to be the same as its finish time. In other words, the event is instantaneous.

4. Events typically do not have any information content. They are used mainly to capture the dynamics of an environment.

## States

A state is a static portion of the environment. For example, a plan, an order form, or a balance sheet are all states since they represent components of the overall static picture for the environment at a given point of time. States have the following characteristics:

1. A state represents a component or item so it is typically described by a noun (or a noun phrase).

2. Every state $S_{i}$ has a start time $t_{\mathrm{S}}(S_{i})$ . However, it does not have any finish time since states are static by nature. $t_{\mathrm{S}}(S_{i})$ acts as a datestamp for $S_{i}$ .

3. States usually have some information content.

## ES relationships

An ES relationship $R_{ij}$ is a binary relationship between the ordered pair, $(X_{i}, X_{j})$ , $i \neq j$ , where $X_{i}$ (or $X_{j}$ ) can either be an event or a state. The restriction $i \neq j$ implies that an event (or a state) is not allowed to relate to (or initiate) itself. Two types of ES relationships are considered here — THEN and CAUSE.

## THEN Relationship

This is used to indicate a temporal ordering. In other words, $R_{ij}$ is THEN if $X_{j}$ directly follows $X_{i}$ in time. The restriction “directly” is imposed to avoid any transitive relationship. Thus, if $X_{i}$ , $X_{j}$ , and $X_{k}$ are connected by two THEN relationships $R_{ij}$ and $R_{jk}$ , then the temporal connection between $X_{i}$ and $X_{k}$ is regarded to be an indirect one and the transitive THEN relationship between them is discarded.

Evidently, the start and finish times of $X_{i}$ and $X_{j}$ are related as follows: $t_{f}(X_{i}) \leq t_{s}(X_{j})$ when $X_{i} = E_{i}$ , and $t_{s}(X_{i}) \leq t_{s}(X_{j})$ when $X_{i} = S_{i}$ . Figure 2(a) shows an example of a THEN relationship.

![](/api/attachments/VH4QBBQT/fulltext/images/b58654b01a7d007cf196b5d8b6bbb5de51bc1d668c64061ad5f06ec3810f67c9.jpg)  
CAUSE Relationship

If $X_{i}$ provides a direct reason for the occurrence of $X_{j}$ , then $X_{i}$ and $X_{j}$ are said to be connected by a CAUSE relationship. Again, the restriction “direct” is used to avoid transitive relationships. Figure 2(b) shows an example of a CAUSE relationship.

![](/api/attachments/VH4QBBQT/fulltext/images/af1ed7c885ab50ff87345ce1f683b399557e922a779c4ab9f894bde8d4f4c471.jpg)  
At first sight, a CAUSE relationship may appear to be nothing but a more stringent version of the THEN relationship. This is because if $X_{j}$ is caused by $X_{i}$ , then one may expect that $X_{j}$ will also follow $X_{i}$ in time. Strictly speaking, however, CAUSE cannot always be treated as a special case of THEN. As an illustration, suppose $X_{i} (= E_{i})$ is “the water is heated” and $X_{j} (= E_{j})$ is “the water evaporates.” Here $X_{j}$ is caused by $X_{i}$ . But the evaporation may start well before the heating is finished. In other words, the condition $t_{f}(X_{j}) \leq t_{s}(X_{j})$ , required for a THEN relationship, with $X_{i} = E_{i}$ , is not satisfied here.

Occasionally, with $X_{j}$ completely following $X_{i}$ in time, it may be difficult to figure out whether $X_{j}$ has actually caused the occurrence of $X_{j}$ or not. In such cases of doubt, the designer must consult with the user/decision maker for further clarification. If the causal connection is still unclear, we suggest that a THEN relationship should be used rather than a CAUSE.

## ES operators

Besides the two ES relationships, THEN and CAUSE, there are also two logical operators — AND and EXCLUSIVE OR.

## AND Operator

Sometimes two or more events or states work in conjunction with one another. Either they jointly bring about another event or state, or they are jointly brought about by another event or state. Such a situation is expressed by means of an AND operator.

Consider Figure 3(a): here, $E_{3}$ can occur when either $E_{1}$ or $E_{2}$ is complete. This is because the man can enter the house either by opening the front door or by opening the back door. Thus, we do not need the combined involvement of $E_{1}$ and $E_{2}$ to bring about $E_{3}$ ; either one will suffice. However, in Figure 3(b) the situation is different. In order for Tom and Linda to get married to each other, Tom should want to marry Linda at the same time Linda should want to marry Tom (hopefully!). Simultaneous occurrences of $E_{1}$ and $E_{2}$ are now required for the occurrence of $E_{3}$ , so an AND operator is needed in this case. An angular notation will be used to represent this operation, as shown in Figure 3(b).

![](/api/attachments/VH4QBBQT/fulltext/images/94a02b1e17b1d093f1344cd05b5dbab6df94d7c1bda42e60e51510b4c32b5784.jpg)  
Figure 3(a)

![](/api/attachments/VH4QBBQT/fulltext/images/615b28b3a4eca819e3be1e31473518afaf81c65a1a8c83f12443237fc338770d.jpg)  
Figure 3(b)

## EXCLUSIVE OR Operator

Occasionally two or more events or states work to the mutual exclusion of one another. That is, either each one individually brings about an event or state, but not in conjunction with the others, or each one is individually brought about by another event or state, but not in conjunction with the others. Such a situation is expressed with the help of an EXCLUSIVE OR operator.

In Figure 3(c), $E_{1}$ can bring about either $E_{2}$ or $E_{3}$ , but not both since the two situations represented by $E_{2}$ and $E_{3}$ are mutually exclusive. An EXCLUSIVE OR operator is indicated by a double angular notation, as shown in Figure 3(c).

Note that the situation in Figure 3(a) actually represents a regular OR (or inclusive OR) operation. No special notation is used for this operation; it will be indicated by the absence of angular and double angular notations.

![](/api/attachments/VH4QBBQT/fulltext/images/8086d6e171f5700a4e5d5b3d11585ba8994c9bf4566368e3b4489331beff06fe.jpg)  
Figure 3(c)

## ES diagram

An activity can be defined as the job or service a user (or a group of users) performs. The objective of an ES diagram is to describe the database requirements for a given activity. An ES diagram for the kth activity ( $A^{k}$ ) of an organization is a directed graph consisting of:

1. A set of nodes $X^k = \{X_i^k\}$ ,

2. A set of directed edges $\mathsf{R}^{\mathsf{k}} = \{\mathsf{R}_{\mathsf{jj}}^{\mathsf{k}}\}$ .

$$
\begin{array}{l} X ^ {k} = \{X _ {i} ^ {k} \}, \\ \text {ed edges R} ^ {k} = \{R _ {i i} ^ {k} \} \end{array}
$$

3. A set of angular or double angular notations $O^{k} = \{O_{i}^{k}\}$ ,

where $X_{i}^{k}$ is either an event or a state; $R_{ij}^{k}$ represents an ES relationship between the ordered pair $(X_{i}^{k}, X_{j}^{k})$ , $i \neq j$ ; and $O_{i}^{k}$ represents an ES operator. Each of the three sets described above contains all possible elements.

## Generation of the ES diagram

The following steps outline a procedure for designing an ES diagram for a given activity.

Step 1: Conduct an interview with a user to find out how he or she describes the process underlying the activity under consideration. Keep detailed records of the interview.

Step 2: Analyze these records critically in order to determine the major data and processing requirements.

Step 3: Identify and list the events and states.

Step 4: Identify and list the ES relationships and ES operators.

Step 5: Draw the ES diagram.

Step 6: Show the diagram to the user interviewed, and explain everything in detail. Find out if he/she suggests any changes in the process depicted in the diagram.

Step 7: Modify the diagram on the basis of these suggestions.

Steps 6 and 7 are introduced in order to reduce the inherent subjectivity of the process.

One may envision the development of a computer-aided tool that will automate the above procedure. The user will feed in the description of the activity, perhaps through an interactive system. The description should either follow a specified, structured format, or some sort of a natural language processor will be needed in order to extract the desired information from an unstructured description. Although the development of such a language processor is admittedly difficult, it is plausible in view of the recent advances in artificial intelligence. In any event, once the required information about the underlying process is collected, the identification and listing of events, states, ES relationships, and ES operators, as well as the formation of the ES diagram can be automated in a fairly straightforward manner.

## Use of the ES Diagram

Although the ES diagram has been described here in terms of an activity, in practice there may be several ES diagrams corresponding to the same activity. Different users may perceive an activity in slightly different ways, and consequently they may use different sets of events, states, relationships, or operators to describe the activity. As a result, their ES diagrams for that activity may look different. Each of these ES diagrams will represent a view of the activity as perceived by an individual user/respondent (or by a group of users/respondents). Thus, following Figure 1, ES diagrams translate the database design process from the requirements analysis phase to the view modeling phase.

There are various other uses for these diagrams. For instance, they can be used to represent all preconditions and postconditions inherent in the system (as defined by Tsichritzis [34]). The concept of time can be abstracted and used in data models. THEN and CAUSE relationships can be utilized to regulate proper update propagations in the database. As an example, if we update a state called “order,” it should trigger an update in another state called “supply” when a CAUSE relationship acts from “order” to “supply.”

At first glance, ES diagrams may appear to be similar to CPM (or PERT) charts. There are actually considerable differences between the two. The CPM (or PERT) diagram is simply a temporal diagram, and consists only of events at each node (or edge). ES diagrams, on the other hand, depict both temporal and causal relationships, and contain two distinct types of nodes — events and states. They incorporate logical operations, consequently, their information content is much higher.

## A Case Study

Two junior colleges in the southern U.S. were used as representative organizations for the study. As mentioned earlier, activities in any organization can be grouped in three broad categories: strategic planning, management control, and operations control. Database requirements for these three levels of activities are usually different. In order to capture this difference in requirements, three activities were chosen for this study, one from each level. The activities were as follows:

1. Campus Development: planning for and construction of campus buildings.

2. Class Scheduling: process of deciding which courses will be taught, who will teach them, and when and where they will be taught.

3. Grade Processing and Reporting: process of collecting, processing, recording, and reporting grades of the student body at the end of a term.

The organizational structures for both colleges indicated that the first activity fell under strategic planning, the second one under management control, and the third one under operations control.

One may expect that a person at any given level of the organizational hierarchy would be able to describe the requirements more accurately for the activity he or she performs, rather than activities at another level. To test if it is really so, three ES diagrams were generated for each of the activities mentioned above on the basis of the responses from three different employees, one from each level. The president, division chairman of science, and registrar were selected at each college.

Interviews were arranged with these employees in order to collect their views about the data and processing structures of the activities mentioned. These interviews did not follow a rigid format; they were open ended and controlled as needed. The purpose was to make the respondent comfortable, and at the same time collect as much information as possible. All responses were carefully noted.

These responses were then analyzed to generate events and states. The analysis was done for each (activity, employee) combination, i.e., for nine cases in each college, or eighteen cases altogether. Tables 2 through 4 list the results for three of these eighteen cases, namely, the ones for the campus development activity for the first college. The other fifteen cases are not presented here to avoid excessive length.

For each case we tried to figure out all ES relationships and ES operators that might be present in the system. Once that was done, ES diagrams were drawn for each case. The respondents were met with again and asked to evaluate the extent to which these ES diagrams depicted the activities as they perceived them. Any suggestions they made to amend these diagrams were taken into consideration. The final diagrams are shown in Figures 4 through 6. Again, for the sake of brevity, the other fifteen diagrams are not shown here.

One may anticipate that the more knowledge a person has about an activity, the more elaborate will be his/her ES diagram. Also, as indicated before, a person is expected to be more knowledgeable about a job at his/her own level of the organization hierarchy than about jobs in other levels. So for campus development, which is a strategic planning level activity, the ES diagram for the president should be more elaborate than those for the division chairman or the registrar. As evidenced by the figures, that really was the case. This phenomenon generally held true for the other activities as well. In other words, for the class scheduling activity, the ES diagram was most elaborate for the division chairman; and for grade processing and reporting, it was so for the Registrar. All these results were found to hold for both colleges studied.

Table 1

<table><tr><td></td><td>Activity: Campus Development Respondent: President</td></tr><tr><td> $S_{1}^{1}$ </td><td>= Legal and environmental problems</td></tr><tr><td> $S_{2}^{1}$ </td><td>= Campus appearance</td></tr><tr><td> $S_{3}^{1}$ </td><td>= Enrollment projections by various breakdowns</td></tr><tr><td> $S_{4}^{1}$ </td><td>= People&#x27;s opinion of current buildings</td></tr><tr><td> $S_{5}^{1}$ </td><td>= Inadequacy of current facilities</td></tr></table>

$\mathsf{S}_6^1 = \mathsf{Space utilization information}$

$\mathsf{S}_7^1 = \mathsf{Administration's suggestions}$

$\mathsf{S}_8^1 = \mathsf{Survey result}$

$\mathsf{S}_9^1 =$ Long-range campus master plan

$S_{10}^{1} = \text{Bids}$

$E_{1}^{1}$ = Administration considers possibilities for campus development

$E_{2}^{1}$ = Administration looks into current operating cost information

$E_{3}^{1}$ = Administration looks into county area plan

$\mathsf{E}_4^1 = \text{Administration decides what to do}$

$E_{5}^{1}$ = Administration prepares a suggestion for continued review by long-range planning committee (LRPC)

$E_6^1 = \text{Administration cancels the idea}$

$E_{7}^{1}$ = Administration sends the suggestion information to LRPC

$E_{8}^{1}$ = LRPC receives the suggestion information from administration

$E_{9}^{1}$ = LRPC surveys students, faculty, etc., asking for ideas and reactions to possible facility changes

$E_{10}^{1}=$ LRPC employs professional planning firm

$E_{11}^{1}=$ LRPC looks at the feasibility of additional facility being part of the campus in the future

$E_{12}^{1}=$ LRPC considers the possibility whether president should make a recommendation to board of trustees' building and grounds committee

$E_{13}^{1}=$ President recommends to building and grounds committee

## Table 1 (cont.)

$E_{14}^{1} =$ President does not recommend

$E_{15}^{1}=$ Building and grounds committee decides whether to make a recommendation to the Board

$E_{16}^{1}=$ Building and grounds committee okays the recommendation

$E_{17}^{1}=$ Building and grounds committee rejects the recommendation

$E_{18}^{1}=$ Board acts on the recommendation

$E_{19}^{1}=$ Board includes the recommendation in the long-range campus master plan

$E_{20}^{1} =$ Board rejects the recommendation

$E_{21}^{1} = Finance committee of board sets priorities for development$

$E_{22}^{1}=$ Finance committee sets a dollar “trigger” so that president will know when to proceed with planning of a particular facility

$E_{23}^{1} = \text{Fund raising proceeds based on priorities set out in master plan and by finance committee}$

$E_{24}^{1}=$ The planning “trigger” has been reached

$E_{25}^{1}=$ President obtains architectural and engineering schematics

$E_{26}^{1}=$ President and the architect work with building and grounds committee of board

$E_{27}^{1}=$ Board sets an implementation “trigger” amount

$E_{28}^{1}=$ The implementation “trigger” amount has been reached

$E_{29}^{1}=$ President instructs the architect to request bids for construction

$E_{30}^{1} =$ Bids are received

![](/api/attachments/VH4QBBQT/fulltext/images/d2e35732c92473a5c0da10da6e4e55142d9f1656e4f45f7f5f61a5e44959ef8a.jpg)

Table 2
Activity: Campus Development
Respondent: Division Chairman for Sciences

$S_{1}^{1}$ = Inadequacy of current facilities

$S_{2}^{1}$ = Money available from donors or government

$E_{1}^{1}$ = President and long-range planning committee develop a recommendation that a new facility needs to be built

$E_{2}^{1}$ = President takes the recommendation to a board committee

$E_{3}^{1}$ = Committee studies the recommendation and decides whether to make a recommendation to the board

$E_{4}^{1}$ = Committee accepts the recommendation

$E_5^1 =$ Committee rejects the recommendation

$E_6^1 =$ Board considers the recommendation

$E_7^1 =$ Board considers financing possibilities

$\mathsf{E}_8^1 = \text{Board makes a decision}$

$E_{9}^{1}$ = President starts making decisions about what the building will contain

$E_{10}^{1}=$ Board rejects

$E_{11}^{1} =$ President chooses an architect

$E_{12}^{1}=$ President and the architect complete the specifications

$E_{13}^{1}=$ President and the architect look at government regulations on safety

$E_{14}^{1}=$ Board makes the final decision to build or not

$E_{15}^{1} =$ Bids are received

$E_{16}^{1} =$ Board rejects the building decision

$E_{17}^{1}=$ President decides (with the help of advisors) what bids to accept

![](/api/attachments/VH4QBBQT/fulltext/images/e1a982fd75a037fb09a6ce559b65569ef2aa9afd5f823e992b0eea16538879bb.jpg)

## Table 3 Activity Campus Development Respondent: Registrar

$E_{1}^{1}$ = Change in demand for a program

$E_{2}^{1} = \text{People express opinions to president}$

$E_{3}^{1}$ = President considers the need for a change

$E_{4}^{1}$ = President uses information about enrollment trends, condition of current buildings, environmental and legal forces

$E_{5}^{1}$ = President checks the long-range development plan

$E_{6}^{1}$ = President asks involved parties for additional information

$E_{7}^{1}$ = President finds out whether funds are available

$E_{8}^{1}$ = President informs and involves all campus community

$E_{9}^{1}$ = President meets with board of trustees

$E_{10}^{1} =$ Board decides whether to build

![](/api/attachments/VH4QBBQT/fulltext/images/775a295ec3e73b2f2483fd05843021088826b2fe2b87811b8c71966402c11277.jpg)

## Summary

This article presents a procedure for database requirements analysis. The objective of the procedure is to capture all data and processing requirements for the activity under consideration, and depict them in terms of a simple, yet comprehensive diagram. The information required to generate the diagram is gathered through interviews with end users.

The diagram is actually a network. Each node of the network represents one of two fundamental constructs defined in the article, namely, events and states. Arcs of the network represent the inherent temporal and causal relationships among these events and states. Logical operations are represented by angular notations. The network can be easily modified in order to incorporate any changes in the underlying process. A case study illustrates the methodology and indicates that the network generated conforms to Anthony's hierarchy of organizational activities [2].

## References

[1] Ackoff, R.L. "Management Misinformation Systems," Management Science, Volume 14, Number 4, December 1967, pp. 147-156.

[2] Anthony, R.N. Planning and Control Systems: A Framework for Analysis, Division of Research, Graduate School of Business Administration, Harvard University, Boston, Massachusetts, 1965.

[3] Bachman, C.W. "Data Structure Diagrams," Data Base, Volume 1, Number 3, Winter 1969, pp. 4-10.

[4] Bachman, C.W. “Trends in Database Management,” Proceedings of National Computer Conference, Anaheim, California, May 1975, pp. 569-576.

[5] Bentley, T.J. “Defining Management’s Information Needs,” Proceedings of National Computer Conference, New York City, New York, June 1976, pp. 869-876.

[6] Brachi, G., Furtado, A., and Pelagatti, G. "Constraint Specification in Evolutionary Data Base Design," Formal Models and Practical Tools for Information Systems Design, H.J. Schneider (ed.), North-Holland, Amsterdam, Netherlands, 1979, pp. 149-165.

[7] Bubenko, J.A. "IAM: Inferential Abstract Modeling — An Approach to the Design of Information Models for Large Shared Data Bases," IBM Technical Report: RC-6343, Yorktown Heights, New York, 1977.

[8] Bubenko, J.A. "Information Modeling in the Context of System Development," Information Processing 80, S. Lavington (ed.), North-Holland, Amsterdam, Netherlands, 1980, pp. 395-411.

[9] Chadler, E.W. and Nador, P. "A Technique for Identification of Users' Systems Design," Information Processing 71, C.V. Freiman (ed.), North-Holland, Amsterdam, Netherlands, 1972, pp. 819-826.

[10] Chen, P.P. "The Entity-Relationship Model: A Basis for the Enterprise View of Data," Proceedings of National Computer Conference, Dallas, Texas, June 1977, pp. 77-84.

[11] Cooper, R.B. and Swanson, E.B. "Management Information Requirements Assessment: The State of the Art," Data Base, Volume 11, Number 2, Fall 1979, pp. 5-16.

[12] Davis, G.B. “Strategies for Information Requirements Determination,” IBM Systems Journal, Volume 21, Number 1, 1982, pp. 4-30.

[13] De, P. and Sen, A. "Data Requirements Planning for an MIS: An Activity-Oriented Approach," Proceedings of Hawaii International Conference on System Sciences, Honolulu, Hawaii, January 1982, Volume 1, pp. 874-879.

[14] Gerritsen, R. “Tools for the Automation of Database Designs,” Proceedings of NYU Symposium on Database Design, New York City, New York, 1978, pp. 91-109.

[15] Hsu, J. and Roussopoulos, N. "Database Conceptual Modeling," ER Approach to Systems Analysis and Design, P.P.S. Chen (ed.), North-Holland, Amsterdam, Netherlands, 1980, pp. 259-275.

[16] Hubbard, G.U. “A Technique for Automated Logical Database Design,” Proceedings of NYU Symposium on Database Design, New York City, New York, 1978, pp. 91-109.

[17] Kahn, B.K. "A Method for Describing Information Required by the Database Design Process," Proceedings of ACM SIGMOD Conference, Washington, D.C., June

1976, pp. 53-64.

[18] Keen, P.G.W. and Scott Morton, M.S. Decision Support Systems: An Organizational Approach, Addison-Wesley, Reading, Massachusetts, 1978.

[19] King, W.R. and Cleland, D.E. "The Design of Management Information Systems: An Information Analysis Approach," Management Science, Volume 22, Number 3, November 1975, pp. 286-297.

[20] Konsynski, B.R. and Manning, M. "Information Resource Specification and Design Language," ER Approach to Systems Analysis and Design, P.P.S. Chen (ed.), North-Holland, Amsterdam, Netherlands, 1980, pp. 339-351.

[21] Miller, J.C. "Conceptual Models for Determining Information Requirements," Proceedings of AFIPS Spring Joint Computer Conference, Washington, D.C., 1964, pp. 609-620.

[22] Munro, M.C. “Determining the Manager’s Information Needs,” Journal of Systems Management, Volume 29, Number 6, June 1978, pp. 34-39.

[23] Munro, M.C. and Davis, G.B. “Determining Management Information Needs: A Comparison of Methods,” MIS Quarterly, Volume 1, Number 2, June 1977, pp. 55-67.

[24] Navathe, S.B. and Schkolnick, M. "View Representation in Logical Data Base Design," Proceedings of ACM SIGMOD Conference, Austin, Texas, June 1978, pp. 144-156.

[25] Nijssen, G.M. "A Gross Architecture for the Next Generation Data Base Management Systems," Modeling in Data Base Management Systems, G.M. Nijssen (ed.), North-Holland, Amsterdam, Netherlands, 1976, pp. 1-24.

[26] Nijssen, G.M. “Current Issues in Conceptual Schema Concepts,” Architecture and Models in Data Base Management Systems, G.M. Nijssen (ed.), North-Holland, Amsterdam, Netherlands, 1977, pp. 31-66.

[27] Nolan, R.L. “System Analysis for Computer-Based Information Systems Design,” Data Base, Volume 3, Number 3, Winter 1971, pp. 1-10.

[28] Raver, N. and Hubbard, G.U. "Automated Logical Data Base Design: Concepts and

Applications," IBM Systems Journal, Volume 16, Number 3, 1977, pp. 287-312.

[29] Ross, D.T. “Structured Analysis (SA): A Language for Communicating Ideas,” IEEE Transactions on Software Engineering, Volume 3, Number 1, January 1977, pp. 16-40.

[30] Ross, D.T. and Schoman, K.E., Jr. "Structured Analysis for Requirements Definition," IEEE Transactions on Software Engineering, Volume 3, Number 1, January 1977, pp. 6-15.

[31] Sen, A. and De, P. "A Formal Procedure for Requirement Analysis in Data Base Design," Proceedings of Hawaii International Conference on Systems Sciences, Honolulu, Hawaii, January 1981, Volume 1, pp. 127-136.

[32] Teichroew, D. "A Survey of Languages for Stating Requirements for Computer-based Information Systems," Proceedings of AFIPS Fall Joint Computer Conference, Montvale, New Jersey, 1972, pp. 1203-1220.

[33] Teichroew, D. and Hershey, E.A. "PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems," IEEE Transactions on Software Engineering, Volume 3, Number 1, January 1977, pp. 41-48.

[34] Tsichritzis, D.C. and Lochovsky, F.H. Data Models, Prentice-Hall, Englewood Cliffs, New Jersey, 1982.

[35] Wiederhold, G. and El-Masri, R. "The Structured Model for Database Design," ER Approach to Systems Analysis and Design, P.P.S. Chen, (ed.), North-Holland, Amsterdam, Netherlands, 1980, pp. 237-257.

[36] Zani, W.M. "Blueprint for MIS," Harvard Business Review, Volume 48, Number 6, November-December 1970, pp. 95-100.

## About the Authors

Prabuddha De is an Associate Professor of Accounting and MIS at Ohio State University. He received his Ph.D. from Carnegie-Mellon University. His publications have appeared in Decision Sciences, Information Systems, Operations Research and various other journals. He spent the 1983-84 academic year at Cornell University as a Visiting Associate Professor of MIS.

Arun Sen is an Assistant Professor of Management Science at the University of South Carolina. He received an M.S. in computer science and a Ph.D. in business administration from Pennsylvania State University. He has published in a number of journals including Computers and Operations Research, Information and Management, and Information Systems.
