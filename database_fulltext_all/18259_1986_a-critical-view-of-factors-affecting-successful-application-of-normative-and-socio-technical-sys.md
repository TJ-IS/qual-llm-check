---
otero_id: 18259
otero_key: "XWD6D8JP"
title: "A critical view of factors affecting successful application of normative and socio-technical systems development approaches"
authors: "Charles E. Paddock"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90059-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Critical View of Factors Affecting Successful Application of Normative and Socio-Technical Systems Development Approaches \*

Charles E. Paddock

Department of Decision and Information Systems, College of Business, Arizona State University, Tempe, AZ 85281, USA

The approaches and tools used to develop information systems are often key factors in the ultimate success of these systems. Approaches may be classified as traditional, socio-technical, process automation, and alternative; tools are descriptive or normative. While the traditional approach and descriptive tools still dominate information system development, socio-technical approaches and normative tools are gaining favor. Process automation and alternative methodologies are, for the most part, experimental.

This paper describes two socio-technical approaches and two normative tools, and presents six potential problems that could hinder their success; information requirements determination; system evaluation, maintenance, and modification; conflict; user/designer roles; short-term focus on success: and post-implementation synchronization of social and technical systems.

As yet, there is no formal framework for relating problem characteristics and environment to appropriate approaches and tools. To realize this framework, research must address specific questions regarding approach and tool application. Therefore, the problems noted above are stated as propositions for investigation that should lead to better understanding of the conditions for applying socio-technical development and normative tools. The propositions also serve as examples of the types of issues which should be considered in research leading to the aforementioned framework.

Keywords: Systems Development, Traditional Development, Descriptive Tools, Normative Tools, Process Automation, Socio-Technical Development, Socio-Technical Systems Approach, Alternative Methodologies, Heuristic Development, Prototyping, Rep Test, Organization Development Techniques.

## 1. Introduction

The approaches and tools used to develop information systems are often key factors in the ultimate success of these systems. They can be divided into several categories, as shown in Table 1. The Traditional Approach is based on the Systems Development Life Cycle (SDLC), one version of which is shown in Figure 1. In support of this approach, a number of tools have been developed. These can be subdivided into two categories: Descriptive and Normative. Descriptive tools are those that assist in organizing and communicating that which is known about an operational system or one under development. A discussion of these tools can be found in [8], and a framework within which several descriptive tools are analyzed is in [7]. More recently, however, criticisms of the tradiational approach and associated descriptive tools have arisen [3] [4] [13]. To address these criticisms, a set of normative tools has been proffered. These generally address the difficulties inherent in such tasks as project definition, information requirements determination, and arriving at the command structure used in system access. They are normative in the sense that they prescribe a procedure for discovering unknowns, which may then be organized and communicated using descriptive tools.

![](/api/attachments/XWD6D8JP/fulltext/images/18c8317ef90b030dcce926b6bfc262033a592ef93469448d0f767de4d5658c58.jpg)

Table 1  
Classification of Systems Development Tools/Approaches

<table><tr><td>Classification</td><td>Definition/Examples</td></tr><tr><td>Traditional</td><td>Follows the Systems Development Life Cycle (SDLC). See Figure 1 [20]</td></tr><tr><td>Descriptive Tools</td><td>Mechanisms for displaying, clarifying, and/or organizing that which is already known about an old/proposed system; e.g., those mentioned by [8], plus data flow diagrams, decision tables, etc. Supports the traditional approach.</td></tr><tr><td>Normative Tools</td><td>Mechanisms for arriving at unknowns in the development process. Supports the traditional approach.</td></tr><tr><td>Socio-Technical Development</td><td>Approaches that explicitly account for the need to plan both the social and technical systems involved; e.g., [5] [6] [11].</td></tr><tr><td>Process Automation</td><td>Approaches that seek to (1) automate part of the development process [12], or (2) transfer part of the responsibility for development to the user [16].</td></tr><tr><td>Alternative Methodologies</td><td>Methods that claim significant departure from conventional approaches; e.g., the Operational Approach [22].</td></tr></table>

The other categories in Table 1, including some normative tools, represent various levels of departure from the traditional approach. For Socio-Technical Development, the departure is manifested by splitting social and technical development, each under the guidance of a professional. The approach may be simply to acquire the services of a behavioral specialist who will employ a set of techniques for managing changes [11], or it may involve a more formally integrated approach to both social and technical development [5,6].

![](/api/attachments/XWD6D8JP/fulltext/images/b2831dd24e969f2a9f5a74840bef252badaee1da105da509a9118052c34ed9c8.jpg)  
Figure 1. The Traditional Systems Development Cycle (adapted from [20]).

Process Automation encompasses two advancements. The first posits a future for application development that resembles a “software factory…that through the preselection of product features and capabilities, (establishes) a prototype that can be rapidly transformed into a unique, yet standardized, end product.” [12]. Full implementation of this philosophy will apparently be some time in coming. The second advancement is “application generation without programmers” [16]. This approach permits users to employ very high level languages to bypass the need for professional programmers. To the extent that end-users are not professional programmers, the language involved must automate much of the work normally associated with developing applications. These end-user-oriented fourth generation languages range from simple personal computer tools (e.g.,

Symphony and Framework) to more complex application generators (e.g., Focus and Nomad 2) [17].

The final category, Alternative Methodologies, represents the most significant departure from the traditional lifecycle approach. For example, the “operational” approach [22], an as yet untried approach to software development, organizes such ideas as executable specifications and program transformations. The author’s major complaint with the conventional approach is that requirements specifications describing the external behavior of a system are independent of the internal structure that generates the behavior. According to [22], the operational approach is ”... based on separation of problem-oriented from implementation-oriented concerns, and all its features can be derived from that philosophy”.

Nontraditional approaches and tools (sociotechnical development, process automation, alternative methodologies, and some normative tools) have the potential to relieve many of the difficulties associated with traditional approaches. But their use is, at present, limited. One obstacle to their more widespread use is the lack of a framework or model useful in relating problem characteristics and environment to development approaches. The lack of a framework makes it difficult for both practitioners and researchers to recognize the applicability of an approach or tool to the resolution of a particular problem via an information system. Formulating this framework involves, in part, more critical and detailed investigation of specific issues related to approach and tool application.

Using several entries in two of the categories of Table 1 (Socio-Technical Development and Normative Tools), this paper describes six issues which may be important in examining any approach and/or tool: complete determination of information requirements; system evaluation, maintenance, and modification; conflict resolution; changing user/designer roles; short-term focus on success; and post-implementation synchronization of social and technical systems. The two categories to be discussed were chosen because they include approaches that represent the least deviation from the traditional approach and are possessed of a literature that describes their application, implementation, and use. This is not generally true of Process Automation and Alterna tive Methodologies. Two approaches from each category will receive comment:

Normative Tools
Prototyping [2,4,13]
The Role Construct Repertory (Rep) Test [14]

Socio-Technical Development
The Socio-Technical Systems (STS) Approach [5,6]
Organizational Development (OD) Techniques [11]

These four were chosen because they have received recent attention in the literature, including descriptions of their application.

The next section briefly describes each approach. The section that follows the next one will then note potential problems, stated in the form of propositions, that may be useful for further investigation. The final section briefly summarizes the discussion.

## 2. Description of Tools and Approaches

## 2.1. Normative Tools

## 2.1.1. Prototyping

The problem of effectively determining information requirements is a significant one in the design process. It has been pointed out in [4] that traditional design approaches tend to reinforce the misconception that a manager knows what is needed [1]. It has also been suggested that a traditional approach delays both the delivery of tangibles to users and recognition of problems [4].

![](/api/attachments/XWD6D8JP/fulltext/images/b2e001592d0c95a0f3b2d9a01df9a89f9e5c4085d88bc88c582919512f00503e.jpg)  
Figure 2. Prototyping (adapted from [13]).

Prototyping (Figure 2) is offered as a way to effectively elicit user information requirements and output formats, speed the development process, and provide the user with experience in operating the system before a major development effort is undertaken. Heuristic Development (HD) [4] is a prototyping approach that allows designers “to heuristically define users’ information requirements while designing and developing an output system.” The authors of [4] recommend that it be integrated with the traditional systems development cycle, and describe a procedure for doing this. They note that HD also appears to be less threatening to users and allows designers to gain better insight to user cognitive styles and information preferences. In the case studies cited by [4], the technique was implemented by allowing users to experiment with data base management system query capabilities to determine information needs before designers actually developed proper data input systems. The general reaction reported was favorable. However, the prototyping approach in general is not without its faults [2]: it can be oversold, it is difficult to manage and control, it is difficult to use in developing large information systems, and it is difficult to maintain user enthusiasm.

## 2.1.2. The Role Construct Repertory (Rep) Test

Another method for addressing the information requirements determination problem is the Rep Test [14]. It does not, however, include a vehicle for actual design of output. For a particular task (the example in [14] is an operation control problem), the Rep Test is implemented in several steps. Step one uses an information resources questionnaire. Managers are asked to provide real sources for 15 generic information sources, three of which are listed below:

1. A source of information which is too detailed.

2. A source of information which is not understood.

3. A source of information which is not detailed enough.

The second step is rather involved, but its result is a set of bipolar adjective scales customized to each manager for scaling the information sources determined in the first step. Examples of adjective scales are: timely/untimely, accurate/inaccurate, and accessible/inaccessible.

Step three involves actual placement of information sources on the adjective scales. Managers determine scale intervals, and also decide whether a source is pertinent to a particular scale.

The last step is construction of multidimensional cognitive maps of information sources for each manager using the adjective scales as dimensions and a technique called multidimensional scaling (MDS). In [14], the technique was applied to determine educational needs of decision-makers, and to elicit information needs that had never before been formally identified.

According to [14], the entire procedure is time-consuming and must be adapted to fit the situation, but needs fewer resources than a direct modeling approach which requires observation of the decision-making process. The Rep Test is intended to be useful in systems involving groups of individuals where the criteria for forming the various groups are their cognitive maps [14].

## 2.2. Socio-Technical Development

## 2.2.1. Organizational Development (OD)

Organizational development techniques are intended to improve interpersonal communication and human decision-making, facilitate conflict resolution, and increase trust and openness in organizations [18]. In [11], it is suggested that since the failure to institutionalize change is a major road-block to successful system implementation, use of OD techniques increases the probability of a system's success. Several specific techniques are suggested as apropos to MIS projects: survey feedback, group diagnostic meetings, communication training, laboratory training, training sessions, role negotiation, and the organizational mirror technique [11]. These address such behavioral problems as user resistance and ignorance, and MIS/management conflict. They are useful in building project teams, improving work groups, and in problem diagnosis and resolution [18].

Implementing OD techniques requires professional expertise; therefore, an OD consultant (a behavioral scientist) is recommended as a member of the project team [11]. Under this arrangement, MIS professionals would focus on technical aspects of the system, while the OD professional(s) would concentrate on the social system (user resistance, communication, attitude, etc.). OD techniques appear to be most needed when there is: extensive use of the MIS in organization, a negative view of MIS, user resistance, conflict between MIS and management, MIS change that is expected to be dramatic, and when there is a system targeted for middle and/or upper management [11].

## 2.2.2. The Socio-Technical Systems (STS) Approach

Organization development techniques and the Socio-Technical Systems Approach [5] [6] share a philosophy: it is desirable to proceed in the systems development task along two dimensions - technical and social. STS advocates a three-phase approach to the systems development task. Phase I is the Strategic Design Process, and its purpose "...is to make the goals and responsibility for the project explicit." [6] This phase calls for MIS and user personnel to form a steering committee that defines problems and system boundaries, decides upon system ownership, tests the organizational climate for change, and formulates implementation strategies.

![](/api/attachments/XWD6D8JP/fulltext/images/bfeab67e822dfe6e60b5281dfbafe52d03c8b016b2a61dadaa03723367996e6f.jpg)  
Figure 3. Relationship of Approaches.

Phase II is the Socio-Technical System Design Process. It is divided into four parts:

II.1 technical system analysis;

II.2. social system analysis;

II.3. design/redesign phase;

II.4. management of the change process.

The first three steps are performed in the order listed, with the analysis activities of the first two steps providing input to the third. Management of change - the fourth step - is an ongoing process that permeates the entire approach.

The final phase, Phase III - Ongoing Management Process, involves constant monitoring and adjustment of the new system to ensure that it meets its goals. The approach assumes that as soon as the system is implemented, its consequences warrant a need for redesign.

The approach is described as “...especially useful in evaluating...design alternatives to determine if...technology that seems economically desirable will have counterproductive effects on work relationships and lead to negative human and social costs.” [19].

Figure 3 roughly illustrates the correspondence of these normative tools and socio-technical development approaches to the traditional approach and each other.

## 3. Problems and Propositions

Descriptions of the tools and approaches in the previous section enumerate a set of relatively broad circumstances under which they might be useful. The propositions noted in this section are offered to encourage detailed and critical investigation of specific weaknesses which may limit the usefulness of Normative and Socio-Technical development methods. The premise of this devil's advocate view is that any eventual framework relating problem characteristics and environment to tools and approaches must give explicit attention to both strengths and weaknesses.

## 3.1. Normative Tools

Proposition 1. Neither prototyping (HD) nor the Rep Test is alone sufficient to wholly determine information requirements.

Prototyping, as described in [4], seems most useful in designing output formats and allowing users to proceed in guided self-determination of information requirements. Prototyping does not appear to directly address problematic information sources. For example, useful information that is not readily available or that the user does not understand may not surface with prototyping. On the other hand, the strength of the Rep Test is its ability to force users into giving in-depth consideration to information requirements. But it does not offer a vehicle for organizing and presenting information. The two methods, therefore, seem complementary. Hypothetically, use of the Rep Test to define sets of useful information, followed by heuristic development of output could be a powerful method for designing an output system.

Proposition 2. Maintenance and modification of systems developed using normative tools may differ from those developed traditionally.

Program specification, design, cost, understandability, and quality are some of the issues that arise during the course of software development. It is not clear what impact normative tools have on these issues. This is particularly true of prototyping. Ideally, a prototype should lead to a complete system that will be better (more useful and acceptable) than one designed using orthodox means. But a highly successful prototype may, for example, be pressed into premature service, thereby short-circuiting the remainder of the development cycle, resulting in a potentially incomplete system. Studies of prototyping tend to describe in detail the conduct of the information and processing requirements design phase of the systems development cycle, and then shift to a post-project description of system success via short-term user satisfaction. In the longer-term, questions of software understandability maintainability, quality, and cost will arise as these prototyped systems require maintenance and modification.

Another potentially troubling aspect of maintenance and modification is the procedure for accomplishing these tasks. Specifically, is maintenance and modification of a system developed using normative tools approached traditionally, or is it desirable to reapply normative tools as part of the maintenance function? The connection, if any, between a system's original development approach and subsequent limitations imposed on the maintenance function has not been established. However, such difficulties have been noted with ADS (Accurately Defined System), an early descriptive tool, leading to the development of Automated ADS [9] [10].

## 3.2. Socio-Technical Development

Proposition 3. Dividing development into technical and social systems, with the associated need for a behavioral scientist / OD professional, may increase the level of conflict present in a project and/or shift its focus.

Dividing the analysis step into social and technical analyses raises some questions regarding conflict resolution. Figure 4 shows a schematic of the communication lines implied by a technical/social split. Under a more traditional approach, the three paths are collapsed to one between the designer (MIS) and user. The tacit three-way link in Figure 4 relegates technical issues to the MIS/user path, behavioral issues to the OD/user path, and design resolution issues to the MIS/OD path. While adding an OD consultant may serve to reduce conflict (-) along the traditional link, it opens the possibility of friction (+) along the two new ones. For example, users may not understand the sometimes abstract relationship between current time spent in application of behavioral techniques and future returns vis-a-vis a “better” system; and MIS professionals may find technical resolution of some behavioral issues frustrating.

If Proposition 3 is true, and it can also be assumed that the services of a behavioralist are indeed valuable, then that individual must be selected with care. For example, it has been suggested that successful project teams should have a balance of (Jungian) personality types [21]. This implies three scenarios for building a project team. First, an OD professional should be chosen whose personality rounds out the team. Second, it may be that a particular type of personality is desirable for the OD and/or MIS members, and that the remainder of the team must be carefully selected. The third possibility is that the results in [21] are not applicable when an OD member is included on the project team. More study is needed to establish the circumstances under which expert behavioral skills lead to successful systems development.

![](/api/attachments/XWD6D8JP/fulltext/images/a159a1781cc4af544ee6ef2112778e3d50a7ece14f9bb5bd4e084dceb142dc7d.jpg)  
Figure 4. MIS/User/OD Communication.

As an aside, this topic arose at a recent panel session conducted by the Decision Systems Research Center of the College of Business, Arizona State University. Of the nine corporate information systems managers present, only one felt that the services of a behavioral consultant might be of value. The rest held to the belief that information systems management should perform this function and has been lax in doing so. The social development task was viewed as one of selling rather than as one of paving the way for change.

Proposition 4. Socio-technical development may change user/designer roles in the systems development process.

Socio-technical development implies a negotiation process, as shown in Figure 5. MIS personnel in conjunction with users arrive at a set of technical goals and options; OD consultant(s) in conjunction with users arrive at a set of social goals and options. The first level of negotiation, therefore, is between MIS/users and OD/users. The second negotiation level is one of reconciling options to arrive at an acceptable system. At this second level, it is conceivable that in attaining acceptance, the user's customary role as co-negotiator with the designer under a traditional model could evolve into one of mediator between MIS and OD professionals in accommodating technical and social goals and options. This role shift may be undesirable from the user's standpoint, causing them undue pressure by calling for more knowledge than they may have, putting them at a disadvantage with both the MIS and OD professionals. Therefore, if the role shift is more than semantic, users may need to be trained to accept and function effectively in the new role.

It is also conceivable that the MIS professional's role could change. To the role of technical negotiator with users would be added one of “co-reconciler” of social and technical issues with the OD professional. As with the user, the MIS professional may find this to be undesirable, requiring additional expertise and training.

![](/api/attachments/XWD6D8JP/fulltext/images/af1c76d2677f7ce2df35442c5a73ee2d68c22332de37f50c54e303acd545f069.jpg)  
Figure 5. Negotiation of an Acceptable System Under Socio-Technical Development.

Both role shifts (user and MIS professional) may affect, perhaps negatively, the atmosphere within which a system is developed.

Proposition 5. Short-term measures of success may lead to distorted assumptions about the long-term success of systems developed using socio-technical approaches.

Research to date has been somewhat short-term in its focus on system success. This may result in a misleading view of the relationship between socio-technical development and system success, causing one to perhaps believe that both the initial and long-term level of success is higher than it is using a traditional approach, as shown in Figure 6. While there is intuitive appeal to this expectation, there is no empirical support for it. It is not difficult to envision a set of alternatives to Figure 6 that would cause doubts about the longterm advocacy of socio-technical development. For example, the two lines in Figure 6 may converge more rapidly than depicted, or may show little divergence at all.

![](/api/attachments/XWD6D8JP/fulltext/images/a6cc46368891755b8b6c819eb2f5d60b95daa070486c9380ecce65626a500ad6.jpg)  
Figure 6. Expectations of Success Duration: Traditional Versus Nontraditional Development.

Proposition 6. In the long run, the synchronization of technical and social systems may be no better under socio-technical development than it is under traditional development.

It is not clear whether socio-technical development methods are transferable to the evaluation and maintenance task so that both social and technical systems remain in tune. Conventional evaluation and maintenance typically uses a scaled-down version of the traditional development cycle and deals chiefly with technical maintenance. Is such downsizing possible or desirable with socio-technical development, or is it necessary to revert to more traditional approaches? The implication of reversion is that social systems, once developed, are not formally maintained, resulting in a technical and social system that diverge over time.

## 4. Summary

Nontraditional methodologies have the potential to relieve some of the difficulties associated with traditional approaches - designer/user communication, information requirements definition, and behavioral considerations. But at present, the methods reviewed in this article have seen only limited use. One hindrance to more widespread use of them is the lack of a framework or model useful in relating problem characteristics and environment to development methods. This is true even for the most widely used approach discussed, prototyping, as pointed out in [15]. To realize this framework, research must address specific questions regarding approach and tool application, in addition to describing implementation and general measures of success. The propositions in this paper are examples of the types of issues which should be considered in research leading to the aforementioned framework. Empirical investigation of the propositions raised in this article will lead to a better understanding of nontraditional methods and their impact on systems, which should further lead to improved knowledge of problem characteristics and environment amenable to these methods.

## References

[1] R.L. Ackoff, “Management Misinformation Systems,” Management Science, December 1967, pp. B147-B156.

[2] M. Alavi, “An Assessment of the Prototyping Approach to Information Systems Development,” Computing Practices, 27:6, June 1984, pp. 556-563.

[3] M. Alavi and J.C. Henderson, “An Evolutionary Strategy for Implementing a Decision Support System,” Management Science, 27:11, November 1981, pp. 1309-1322.

[4] T. Berrisford and J. Wetherbe, “Heuristic Development: A Redesign of Systems Design,” MIS Quarterly, 3:1, March 1979, pp. 11-19.

[5] R.P. Bostrom and J.S. Heinen, “MIS Problems and Failures: A Socio-Technical Perspective/Part I: The Causes,” MIS Quarterly, 1:3, September 1977a, pp. 17-32.

[6] R.P. Bostrom and J.S. Heinen, “MIS Problems and Failures: A Socio-Technical Perspective/Part II: The Application of Socio-Technical Theory,” MIS Quarterly, 1:4, December 1977b, pp. 11-28.

[7] M.A. Colter, “A Comparative Examination of Systems Analysis Techniques,” MIS Quarterly, 8:1, March 1984, pp. 51-66.

[8] J.D. Couger, “Evolution of Business Systems Analysis Techniques,” Computing Surveys, 5:3, September 1973, pp. 167-198.

[9] J.D. Couger, “Second Generation Development Techniques For Computer-Based Systems,” in Advanced System Development/Feasibility Techniques, ed. J.D. Couger, M.A. York, 1982a.

[10] J.D. Couger, "Third Generation Development Techniques For Computer-Based Systems," in Advanced System Development/Feasibility Techniques, ed. J.D. Couger, M.A. York, 1982b.

[11] G. DeSanctis and J.F. Courtney, “Toward Friendly User MIS Implementation,” Communications of the ACM, 26:10, October 1983, pp. 732-738.

[12] F.J. Grant, “Twenty-First Century Software,” Datamation, April 1, 1985, pp. 123-130.

[13] L.L. Gremillion and P. Pyburn, “Breaking the Systems Development Bottleneck,” Harvard Business Review, 61:2, March-April 1983, pp. 130-137.

[14] G. Grudnitski, “Eliciting Decision-Makers’ Information Requirements,” Journal of MIS, 1:1, Summer 1984, pp. 11-32.

[15] J.M. Kraushaar and L.E. Shirland, “A Prototyping Method for Applications Development by End Users and Information Systems Specialists,” MIS Quarterly, 9:3, September 1985, pp. 189-197.

[16] J. Martin and C. McClure, Software Maintenance: The Problem and Its Solutions, Prentice-Hall, Inc., New Jersey, 1983.

[17] P. Mimno, "Power to the Users," Computerworld, April 8, 1985, pp. ID/19-ID/28.

[18] J.M. Nicholas, “Organization Development in Systems Management,” Journal of Systems Management, 30:11, November 1979, pp. 24-30.

[19] A.W. Smith, Management Systems: Analyses and Applications, The Dryden Press, New York, 1982.

[20] J.C. Wetherbe, Systems Analysis and Design: Traditional

Structured and Advanced Concepts and Techniques, Second Edition, West Publishing Co., St. Paul, Minnesota, 1979.

[21] K.B. White, “MIS Project Teams: An Investigation of Cognitive Style Implications,” MIS Quarterly, 8:2, June 1984, pp. 95-101.

[22] P. Zave, “The Operational Versus the Conventional Approach to Software Development,” Communications of the ACM, 27:2, February 1984, pp. 104-118.
