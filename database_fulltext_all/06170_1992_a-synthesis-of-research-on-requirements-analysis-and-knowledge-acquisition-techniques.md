---
otero_id: 6170
otero_key: "7F5N4MRW"
title: "A Synthesis of Research on Requirements Analysis and Knowledge Acquisition Techniques"
authors: "Terry Bird; Kathy Cossick; and Robert Zmud"
year: "1992"
journal: "MIS Quarterly"
doi: "10.2307/249704"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Synthesis of Research on Requirements Analysis and Knowledge Acquisition Techniques

By: Terry Anthony Byrd
Information and Management
Sciences
College of Business
Florida State University
Tallahassee, Florida 32306 U.S.A.

Kathy L. Cossick
College of Business Administration
University of Houston
Houston, Texas 77204 U.S.A.

Robert W. Zmud
Information and Management
Sciences
College of Business
Florida State University
Tallahassee, Florida 32306 U.S.A.

## Abstract

Requirements analysis (RA) involves end users and systems analysts interacting in an effort to recognize and specify the data and information needed to develop an information system. In the design of expert systems, a similar process of eliciting information, in this case human knowledge, has been studied under the banner of knowledge acquisition (KA). When examined closely, many entities and processes involved in RA and KA are almost identical. However, researchers in each area are seemingly unaware of the developments in the other area. In order to facilitate a merged awareness of both research streams, this article compares representative RA and KA techniques, which are grouped, according to elicitation mode, on three dimensions: communication obstacles, a technique's locus of control, and the nature of the understanding gained from using the technique. This comparison demonstrates that these two research streams have many things in common and that researchers in one area can benefit from developments in the other area. Additionally, this analysis leads to several suggested research areas: (1) rigorous examinations of these techniques as they are used to overcome communication obstacles and enrich understanding; (2) investigations into the seeming match between certain elicitation types and problem domain categories; (3) examinations into synergetic effects of elicitation techniques; (4) development of more techniques for eliciting information requirements to serve emerging needs; and (5) comparisons of the relative advantage of generalized versus specialized elicitation techniques.

Keywords: Information requirements determination, knowledge acquisition, information systems design, expert systems design, communication tools, system development techniques and tools

ACM Categories: D.2.1, D.2.2, I.2.6

## Introduction

It is well understood that the development of effective information systems (IS) requires thorough analyses of user information needs prior to IS design. This step in the process of systems development, generally referred to as requirements analysis (RA), typically involves an analyst (1) working with end users to establish an understanding of organizational information processing needs; (2) developing IS objectives; (3) designing and evaluating IS alternatives; (4) communicating the results of analyses to superiors, other analysts, and end users; and (5) performing a systems audit.

In the design of expert systems, a similar process of eliciting information, in this case human knowledge, has been studied under the banner of knowledge acquisition (KA) (Hayes-Roth, 1984a; 1984b). Knowledge acquisition is formally defined as the transfer and transformation of problem-solving expertise from some knowledge source to a computer program. As a part of the overall knowledge engineering process, knowledge acquisition often involves a knowledge entineer (KE) gaining both declarative and procedural knowledge from a human expert in a particular problem domain. Declarative knowledge includes facts about classifications and relationships, whereas procedural knowledge refers to the way declarative knowledge is manipulated as well as incorporated within control structures, which contain information about when and how to apply the knowledge in what is commonly called the “knowledge base” (Wright and Ayton, 1987).

There is a tendency for both researchers and practitioners to see knowledge elicitation through KA as a new phenomenon. It can be argued, however, that systems analysts have been doing a very similar process for years under the guise of RA. When examined closely, many entities and processes involved in RA and KA are almost identical. An in-depth comparison of the two processes is given below after each is individually described. The paper then categorizes representative techniques used to elicit IS or ES requirements through, respectively, RA and KA. This categorization scheme contrasts techniques according to (1) communication obstacles; (2) the nature of the understanding gained through their use; and (3) locus of control (i.e., whether the technique is analyst-driven, user-driven, or automated). The scheme places the techniques in groups, or types, according to five elicitation modes. The article concludes by suggesting a common set of research directions for these two research streams. These include a call for rigorous examinations of elicitation techniques as they apply to overcoming communication obstacles, investigations into how certain elicitation techniques seem to be better suited to certain problem domains, examinations of the synergistic effects of elicitation techniques, and developments of new elicitation techniques for emerging needs.

## Requirements Analysis

Requirements analysis (RA) seeks to identify the data and information needed (1) to automate some organizational tasks and (2) to support knowledge workers in their decision making in order to achieve the objectives of the organizations (Taggert and Tharp, 1977). Determining correct and complete information requirements is a vital part of designing an IS. Many IS failures can be attributed to a lack of clear and specific information requirements (Cooper and Swanson, 1979; Davis, 1982; Telem, 1988a). Proper identification of information needs early in the design process produces more successful systems and allows for early correction of errors while the cost of correction is lower (Mittermeir, et al., 1982). Boehm (1976; 1980; 1981), for example, graphically illustrates that costs for corrections made during RA are significantly lower than corrections made in later stages of the systems development life cycle. Further, a number of studies (Carter, et al., 1975; Galliers and Lyons, 1985; Taggart and Tharp, 1977; Wasserman, et al., 1983) have shown that senior managers believe that early identification of their true information requirements is a crucial factor in a successful implementation. Unfortunately, the recognized importance of the RA process has not been stressed in either practice or research (Galliers, 1987). As a result, systems continue to be designed that do not adequately support the activities that motivated them.

The overall sequence of RA activities, given in Figure 1, is commonly viewed as consisting of four processes (Zmud, 1983): (1) conceptual design; (2) logical design; (3) validation; and (4) formal specification. The first process, conceptual design, encompasses developing a normative model of the system. This model reflects critical factors affecting the system design (environmental forces, organization-wide goals and policies, current and anticipated problems and opportunities, product and service flows, etc.). In the logical design process, analysts assess the strengths and weaknesses of the conceptual design regarding a range of organizational (resources, maturity, attitudes, politics, priorities) and technological (existing systems capabilities, data availabilities, personnel) factors. The result of this process is a system design compatible with the organization's strengths and weaknesses. The third process, validation, is an attempt to determine if a valid set of requirements has been developed. Reviewers must inspect methods of data entry, outputs, and do other evaluations pertaining to the operations of the designed system. Finally, a document, the formal specification, is produced; this document clearly and completely specifies a complete set of information requirements—inputs, outputs, and processing environment—and explains how these objects are to be used. It is important to recognize that, depending on the strategy employed, the four processes may occur sequentially, iteratively, or quasi-simultaneously.

![](/api/attachments/7F5N4MRW/fulltext/images/5fa3a560aac71a59642f262cd9d5268a52adc65b9b2d86930b1fe307a526a008.jpg)  
Figure 1. Requirements Analysis Processes  
Source: Modified from Zmud (1983, p. 311).

## Knowledge Acquisition

A popular view of knowledge acquisition (KA) is that experts' minds are filled with "nuggets" of knowledge about their specialized domains. The knowledge engineer (KE) then "mines" these nuggets of knowledge from the head of the expert one nugget at a time (Feigenbaum and McCorduck, 1983). In reality, there is very little truth to this picture. Knowledge is seldom taken from experts in a bit-by-bit fashion. There is, in fact, no mystical process by which a KE communicates with an expert and removes hidden bits of knowledge from deep within the expert's brain. Rather, KA involves the following activities (Kidd, 1987):

1. The KE uses various communication techniques to elicit data and information from the expert.

2. The KE interprets these data and information (more or less skillfully) in order to draw conclusions on what might be the expert's underlying knowledge and reasoning processes.

3. The KE uses his or her conclusions to direct the construction of a model (and the implementation of this model into an ES shell or language), which describes the expert's knowledge and processes. An iterative process is carried out by the KE and expert as the ES model evolves into a functional system (Johnson, 1985).

Figure 2 gives a more formal representation of the KA processes (Buchanan, et al., 1983). During the identification process, first, the participants (KE, experts, users) are identified; second, the problem is identified and structured; third, the resources (knowledge sources, computing facilities, money) are specified; and finally, goals and objectives of the ES may be given. In the conceptualization process, the key concepts and relations from the first stage are made explicit. The formalization process maps the key concepts, subproblems, and information flow characteristics isolated in the previous stages into more formal knowledge representations, such as rules or frames. The fourth process, the implementation process, involves the actual programming of these rules or frames into a computer. The final process is the testing, where the ES is examined with examples and revised as necessary by repeating any of the earlier processes as indicated by the results. Again, these processes might occur sequentially, iteratively, or quasi-simultaneously.

Just as a complete, accurate specification of information needs is a key ingredient in successful

![](/api/attachments/7F5N4MRW/fulltext/images/534fb68d311bbb47c4e30e867ae81d23e122e71a4c81b3c5d97072738ca22b20.jpg)  
Figure 2. Knowledge Acquisition Processes  
Source: Modified from Buchanan, et al. (1983, p. 139).

MIS/DSS design and development, a complete, high-quality knowledge base is essential to successful ES development (Kim and Courtney, 1988; Waldron, 1986). If it is true that the power of an ES is primarily a function of the quality and completeness of the embedded knowledge, then extracting and formalizing the knowledge is a critical, if not the most critical, step in the ES development process.

## RA and KA: Two Sides of the Same Coin?

While much research has been undertaken regarding both RA and KA, neither research area seems aware of the other. This seems quite surprising given the similarities of the two activities: RA and KA both involve the elicitation of data and information from, respectively, end users and domain experts. A systems analyst interprets these data and information in order to develop an object system model and create an information system's structure. A KE performs a similar task in developing a domain knowledge map and creating an expert system's structure. In fact, many of the skills used by a systems analyst for RA are the same skills needed by a KE for KA (Fellers, 1987; Graham and Jones, 1988). A sampling of these includes rapport with the end users or experts involved in building the system, the ability to communicate and suggest solutions, the talent to conceptually map informal understanding into a formal information architecture, the skill to lead the knowledge worker from describing simplistic to more comprehensive models, and the knack of understanding the end user's or expert's motivations and concerns.

It is now well-understood that RA and KA processes both work best when end users of the resulting systems participate in the design process. Originally, it was believed that the KA process needed only a KE and an expert. However, researchers have discovered that the more successful implementations of ES have occurred where end users of the ES participate in the design process (Roth and Woods, 1989). This result follows the pattern of studies showing that end-user participation in RA (and other stages of the system development life cycle) increases the likelihood of success in the implementation of traditional IS (e.g., Franz, 1985; Franz and Robey, 1984; Ives and Olson, 1984). Such participation by end users, however, adds more pressure for good communication between the members of the development team.

Another similarity between RA and KA is that the end products of each can be used in basically the same ways: to automate specific functions, thus replacing workers; or to support workers in their work tasks. While this is well-recognized with traditional IS, it might not be as obvious to individuals unfamiliar with ESs, which are used to automate decision processes. Because ESs are programs that contain a condensed version of human expertise in a particular specialized domain, they can provide solutions to humans on problems in that narrow domain. ESs such as XCON (McDermott, 1981; 1982; Sviokla, 1990) and PDS (Hart, 1989) have replaced human workers in their respective domains. XCON configures VAX computer systems and PDS troubleshoots turbine generators based on the analysis of sensor data. However, ESs can also be used to support organizational workers. In fact, most ESs commonly used today are used in the support role (Roth and Woods 1989). Here ESs provide “action recommendations,” which need to be reviewed and approved by humans. For example, PUFF (Hayes-Roth, et al., 1983), a medical ES that concentrates on pulmonary disorders, might be used by a general practitioner to gain insight into the problems a patient might be having.

Another recent development has given even more importance to the desirability of merging research from RA and KA: the embedding of expert systems into what might best be termed “traditional IS.” Weitzel and Kerschberg (1989) indicate that the traditional systems development life cycle needs modification to acknowledge the new reality of embedding ES into traditional systems. In other studies, Meyer and Curley (1989; 1991b) developed a framework based on the two dimensions of knowledge and technology, both ranging from low to high. Based on these ranges, the framework is divided into four types of ES—personal productivity, technology-intensive, knowledge-intensive, and strategic impact.

Two of these ES types, technology-intensive and strategic impact, are of interest to this article because they combine elements of both traditional IS and ES. Technology-intensive systems have relatively simple knowledge bases but require substantial development effort in terms of traditional programming, systems integration, and systems administration. Strategic impact systems are complex in both knowledge-intensive and traditional technology. As a consequence, the successful development of such systems requires extensive efforts in both RA and KA. Meyer and Curley (1991a; 1991b) also found several systems that fit into each one of these categories. For example, a system called MegaFilex, a computer disk manufacturing advisor and planner, and XTEL, a telephone equipment configuration advisor for the post office, are two systems classified as technology-intensive. SOLEIL, a solar cell manufacturing advisor for alloying, and STAFA, a generic custom computer product configuration and cost advisor, are examples of strategic impact systems.

With the increase in complexity of hardware and software systems, developers of traditional IS have begun to feel the need for ES technology. Applications such as automated help desks and "lights-out" computer operations have helped convince systems analysts of the value of ES technology (Popolizio and Cappelli, 1989). A recent survey conducted by New Science Associates shows that 35 percent of the Fortune 500 companies had explicitly turned their ES developments over to their traditional MIS groups (Popolizio and Cappelli, 1989). Meyer and Curley (1991a; 1991b) also found that the development of four out of the 10 systems in the technology-intensive and strategic impact categories were controlled by the DP department. These studies indicate that, in a substantial number of cases, RA and KA are being performed by the same personnel; thus, the merging of these two processes seems a logical conclusion.

By the above discussion, it would seem that RA and KA are similar and that many of the activities involved in these elicitation processes overlap. Individual behaviors, as well as communication patterns among participants, have similar characteristics in both the RA and KA processes. In addition, there seems to be some evidence that the two processes may eventually merge into one process as the distinction between ES and traditional IS blurs. Therefore, research in either stream could benefit from knowledge gained in the other. Furthermore, studies addressing both RA and KA could lead to better understanding of the elicitation process in general. However, this type of combined effort has not occurred. In an effort to merge these two areas, this article investigates elicitation techniques developed in RA or KA and places them into a categorization scheme that can be used to guide research and provide guidelines to practitioners. The next section explains this categorization scheme.

## Categorization Scheme for RA and KA Techniques

In an attempt to understand the appropriate use of the representative RA and KA techniques and to guide research, a categorization scheme was developed on three dimensions: (1) communications obstacles; (2) the facilities for problem domain understanding gained from using the technique; and (3) a technique's locus of control. The origin of the technique (i.e., whether first used in RA or KA) is also included.

The selection of communications obstacles as one of the dimensions of our categorization scheme should be obvious. KEs and systems analysts both need to communicate throughout the development process. They communicate when extracting requirements or knowledge from the end users (or clients) and expert, respectively; in interacting with subordinates, peers, and superiors; and in echoing their understandings of problems and requirements back to the end users or clients. Many authors (e.g., Avery and Hoyle, 1974; Bostrom, 1984; 1989; Cronan and Means, 1984; Kaiser and King, 1982; Martin and Fuerst, 1984; Scharer, 1981) have stressed and presented evidence of the importance of effective communication in the determination of requirements and in the system development process in general. Likewise, other researchers (e.g., Evanson, 1988; Fellers, et al., 1988; Sviokla, 1986a; 1986b) have demonstrated that effective communication between KEs and experts is a key in developing successful ESs.

The main “task” pursued by KEs and analysts alike is studying and making discoveries about the application domain (Coad and Yourdon, 1990). This is the challenge of understanding the “problem space.” Consider this comment from Coad and Yourdon (1990) of an analyst developing an IS for air traffic control: “The analyst needs to immerse himself in that problem space, immerse himself so deeply that he begins to discover nuances that even those who live with air traffic control every day have not yet fully considered” (p. 10). It is crucial to the development process that the analyst possess tools to help him gain this domain understanding. The same is true of a KE developing an ES. Fellers, et al.

(1988) found in their study that “understanding of problem domain and jargon” by the KE ranked in importance right behind communications in the knowledge acquisition process. They indicate that this understanding will result in a faster, smoother acquisition process because the expert will not have to stop to explain every little nuance of the domain to the KE.

Meyer and Curley (1991a) and von Hippel (1986) have identified “locus of control” of system or product development as a key to success of the project. Here locus of control refers to the entity leading or controlling the development process. This is the final dimension in the framework used in this article. Innovation studies (e.g., Freeman 1968; Knight, 1963; von Hippel, 1976; 1977), including those related to information systems (Franz, 1985; Franz and Robey, 1984; Ives and Olson, 1984), have shown that the locus of control, whether with the developer or the user and depending on the circumstances involved, can play a significant role in the success of the innovation.

## Communication obstacles

Communication obstacles abound in both RA and KA and add to the complexity and uncertainty inherently present. Valusek and Fryback (1985) classify communication obstacles to success of RA into three categories: WITHIN, AMONG, and BETWEEN.

## WITHIN Obstacles

WITHIN obstacles involve the cognitive limitations of humans as information processors and problem solvers (Davis, 1982; Valusek and Fryback, 1985). Both end users and experts, as humans, are subject to these cognitive shortcomings. An end user attempting to specify information requirements is subject to limited memory and recall as well as information processing biases, such as selective perception or representativeness. Experts and end users involved in the knowledge acquisition process face these same difficulties as they try to fully understand and recall the processes and actions taken in their own decision-making activities (Edwards, 1987; Shaw, 1987; Waldron, 1986). Elicitation techniques that help overcome WITHIN obstacles are focused on enhancing recall and understanding a user's innate information processing activities and decision processes. These methods primarily aid the recognition and structuring of the user's mental models.

## BETWEEN Obstacles

Cognitive limitations also contribute to communication difficulties between systems analysts and end users and between KEs and experts. Further, recent evidence indicates that KEs must also communicate with end users when building ESs (Roth and Woods, 1989), causing the potential for more communication problems in building these systems. These communication difficulties are referred to as BETWEEN obstacles. The communication problems are not only caused by individual cognitive limitations but also by the lack of a common language (Davis, 1982; Valusek and Fryback, 1985). End users and systems analysts come from different backgrounds and have different mind sets (Oliver and Langford, 1984); this often leads to communication breakdown (Guitierrez, 1987; Mittermeir, et al., 1982). In the KA process, the interaction between the expert and the KE poses the same problem with language and vocabulary differences (Hart, 1989; Kidd, 1987). The expert uses specialized terminology about the problem domain that the KE is unable to completely comprehend. On the other hand, the expert does not fully understand the technological aspects of ES design (Edwards, 1987; Hayes-Roth, et al., 1983; Waldron, 1986). BETWEEN obstacles are addressed by elicitation techniques designed to aid the participants' communication process. Such techniques often attempt to create a mutually understood context or provide a means to otherwise facilitate the interaction process.

## AMONG Obstacles

Together, the problems associated with human limitations and communications difficulties make the process of eliciting data and information very difficult. Even if both of these problems were solved, however, the determination of information needs may still be confronted with obstacles associated with balancing the needs of multiple users. A system designed for multiple users must attempt to accommodate each user's needs, which are often in conflict or in competition for limited systems design resources. The AMONG obstacles involve tradeoffs and weighing of multiple needs after determining individual user requirements. In KA, a similar difficulty arises because the resulting ES will probably be used by a number of end users. In addition, more and more ES development projects involve multiple experts, each with his or her own viewpoints (Mittal and Dym, 1985). The elicitation techniques that address AMONG obstacles provide for the incorporation of varying views of distinct stakeholders and also provide mechanisms by which stakeholders can negotiate and reach an acceptable compromise regarding a “collective” set of needs.

RA and KA face essentially the same communication obstacles. A better understanding of these obstacles would improve the performance of either process. By indicating the communication obstacles addressed by the various elicitation techniques, systems analysts and KEs confronted with these obstacles can draw on specific techniques that have been previously applied to RA, KA, or both.

## Facilities for problem domain understanding

Elicitation techniques differ widely with regard to the issues each emphasizes in facilitating problem exploration and understanding. Table 1 defines and references a number of problem domain entities (e.g., displayed information, knowledge specification) believed to be critical in constructing an IS or ES. Most of these domain entities are similar to those that apply in framing general problem or decision structures, such as those used by Smith (1989). As a means to better compare techniques, these entities have been grouped into the following problem domain categories: information requirements, process understanding, behavior understanding, and problem frame understanding.

## Locus of control

Kim and Courtney (1988) classify KA elicitation techniques by the way the elicitation process is “driven.” With KA, processes are driven by either the KE, the expert, or the machine. The most common approach is for the KE to direct the process, meaning that the KE conducts the knowledge elicitation processes through interviews, protocol analysis, or other techniques.

Table 1. Definitions of Problem Domain Categories and Entities

<table><tr><td>Problem Domain Categories and Entities</td><td>Definition</td></tr><tr><td>Information Requirements</td><td>These facilities place emphasis on a complete and thorough analysis of the domain&#x27;s information requirements and their relationships.</td></tr><tr><td>Displayed Information Zmud (1983)</td><td>The data to be presented to end users.</td></tr><tr><td>Interface Design Zmud (1983)</td><td>The language and formats used in presenting “displayed information” to end users.</td></tr><tr><td>Process Understanding</td><td>These facilities place emphasis on an analysis of the “real world” activity as performed in the business world.</td></tr><tr><td>Knowledge Specification Smith (1989)</td><td>The facts, rules, beliefs, algorithms, procedures, etc. pertinent to the problem.</td></tr><tr><td>Difficulties, Constraints Smith (1989)</td><td>Factors that may prohibit design, development, and implementation of solutions.</td></tr><tr><td>Justification Hayes-Roth (1984a; 1984b)</td><td>Explanations of why specific actions are or are not to be taken.</td></tr><tr><td>Gap Specification Smith (1989)</td><td>Comparisons of current problem states against desired problem states.</td></tr><tr><td>Behavior Understanding</td><td>These facilities focus on the dynamic nature of the data and knowledge and the need to analyze and understand events in the environment that impact data and knowledge recorded in the system.</td></tr><tr><td>Mental Models Smith (1989)</td><td>Abstract representations of the problem domain maintained by experts and end users.</td></tr><tr><td>Operational Models Zmud (1983)</td><td>Abstract representation of input/output processes associated with the problem domain.</td></tr><tr><td>Problem Frame Understanding</td><td>These facilities focus on understanding the overall context in which the system is being developed.</td></tr><tr><td>Goal State Specification Smith (1989)</td><td>The particular global goals to be achieved by an implemented IS or ES.</td></tr><tr><td>Existing Support Environment Zmud (1983)</td><td>Description of the existing technological environment that can be applied to support the system to be developed.</td></tr></table>

This approach dominates because the expert with domain-specific knowledge usually does not possess the technical knowledge necessary to build a model of the knowledge domain, let alone an ES. In addition, the KE can use certain techniques to aid the expert in expressing clearly and completely the rules and processes used in expert decision making. At times, however, miscommunications and misinterpretations do result.

An expert-driven approach to KA could eliminate some of these problems by allowing experts to encode their expertise without relying on KEs as intermediaries. Problems with incomplete and unclear knowledge bases may still result due to the difficulty of expressing decision processes.

As a third possibility, a machine-driven approach may be followed for KA. Using this approach, the machine “learns” how problems are solved using a set of examples and the attributes considered in making those decisions. From this information, the machine induces rules from the problem-solving process.

In evaluating KA techniques, it is important to understand which entity is leading the interaction because different advantages and disadvantages will be associated with each type of interaction (Kim and Courtney 1988).

A similar pattern can be seen in traditional IS. Most systems development projects are led by systems analysts who interact to varying degrees with users to capture requirements. However, the advent of end-user computing and CASE (computer-assisted software engineering) tools has changed this simple model into a more complex one. More and more systems development efforts are being led by end users as their knowledge of computing grows (Baronas and Louis, 1988; Franz, 1985; Franz and Robey, 1984; Hirschheim and Klein, 1989). Similar to machine rule induction in knowledge acquisition, CASE tools provide the potential to automate the determination and documentation of information requirements (Hackathorn and Karimi, 1988; Henderson and Cooprider, 1990).

It is obvious from this discussion that RA and KA are similarly positioned in reference to locus of control. Both processes can alternately be controlled by the KE or analyst, the expert or user, or through automated machine procedures.

## Examination of representative elicitation techniques

In selecting techniques to contrast, the objective was to provide an extensive listing of the more commonly used elicitation techniques while minimizing redundancy. This listing was determined by searching the literature and using the knowledge and experience of the authors. Each technique is briefly discussed below. Then, an overall assessment of this set of elicitation techniques is given.

The RA and KA techniques are contrasted in three tables. Table 2 is divided into five elicitation types according to elicitation mode: observation techniques, unstructured elicitation techniques, mapping techniques, formal analysis techniques, and structured elicitation techniques (“elicitation types” will be used in the rest of this article for these groupings; “elicitation techniques” is used for individual techniques such as structured interviews or prototyping). Within any of the categories, the RA and KA elicitation techniques are further divided by the three dimensions: their origin, locus of control, and communication obstacles. Then the nature of the problem domain understanding gained from each technique is shown in Table 3, where the techniques are listed by type. The black dots in Table 3 match the techniques with the problem domains. Table 4 gives an indication of how the techniques ranged from more general to more specialized uses.

## Overview of RA and KA techniques

## Observation Techniques

Behavior analysis (Cleal and Heaton, 1988) is simply observing the user or expert while he or she is doing a specific task. This technique may involve watching a subject and making notes, or it could involve more sophisticated techniques such as analysis of videotaped episodes. Behavior analysis has been used mainly in KA and supports at least parts of three of the four major problem domain categories (See Table 4) and, as a result, can be described as moderate on a continuum from general to specialized approaches. Behavior analysis supports BETWEEN communication and is generally controlled by the analyst or KE.

Table 2. Categorization of RA and KA Techniques

<table><tr><td>Technique Category</td><td>Method</td><td>Origin</td><td>Approach</td><td>Communication Obstacle</td></tr><tr><td rowspan="3">Observation Techniques</td><td>Behavior AnalysisCleal and Heaton (1988)</td><td>KA</td><td>User/Expert Driven</td><td>Between</td></tr><tr><td>Protocol AnalysisBlanning (1984)Wright and Ayton (1987)</td><td>KA</td><td>User/Expert Driven</td><td>Between</td></tr><tr><td>PrototypingGoal and Tonge (1987)Luqui, et al. (1988)Sethi and Teng (1988)</td><td>KA/RA</td><td>Analyst/KE Driven</td><td>Within Between</td></tr><tr><td rowspan="4">Unstructured Elicitation Techniques</td><td>Teachback InterviewJohnson and Johnson (1987)</td><td>KA</td><td>User/Expert Driven</td><td>Between Among</td></tr><tr><td>Open InterviewDavis (1982)Cleal and Heaton (1988)</td><td>KA/RA</td><td>User/Expert Driven</td><td>Between</td></tr><tr><td>Brainstorming CollectiveDecision MakingTelem (1988a; 1988b)</td><td>RA</td><td>User/Expert Driven</td><td>Within Among</td></tr><tr><td>Goal-Oriented ApproachMunro and Davis (1977)King (1978)</td><td>RA</td><td>Analyst/KE Driven</td><td>Among Within</td></tr><tr><td rowspan="3">Mapping Techniques</td><td>Multidimensional ScalingWright and Ayton (1987)Gammack (1987)</td><td>KA</td><td>Analyst/KE Driven</td><td>Between Among</td></tr><tr><td>Cognitive MappingMontazemi andConrath (1986)</td><td>RA</td><td>User/Expert Driven</td><td>Within Between</td></tr><tr><td>Variance AnalysisHawgood, et al. (1978)</td><td>RA</td><td>Analyst/KE Driven</td><td>Between Among</td></tr><tr><td rowspan="3">Formal Analysis Techniques</td><td>Machine Rule InductionMingers (1986)Shaw (1987)</td><td>KA</td><td>Machine Driven</td><td>Between Among</td></tr><tr><td>Text AnalysisCleal and Heaton (1988)</td><td>KA</td><td>Analyst/KE Driven</td><td>Between</td></tr><tr><td>Repertory GridGutierrez (1987)Cleal and Heaton (1988)Gammack (1987)</td><td>KA/RA</td><td>Analyst/KE Driven</td><td>Within Between</td></tr><tr><td rowspan="5">Structured Elicitation Techniques</td><td>Card SortGammack (1987)</td><td>KA</td><td>Analyst/KE Driven</td><td>Within Between</td></tr><tr><td>Scenario TechniqueBoland (1984)Zmud, et al. (1990)Cleal and Heaton (1988)</td><td>KA/RA</td><td>User/Expert Driven</td><td>Within Among</td></tr><tr><td>Structured InterviewDavis (1982)Waldron (1986)</td><td>KA/RA</td><td>Analyst/KE Driven</td><td>Between</td></tr><tr><td>Critical Success FactorsRockart (1979)Boynton and Zmud (1987)</td><td>RA</td><td>Analyst/KE Driven</td><td>Within Between Among</td></tr><tr><td>Future AnalysisHawgood, et al. (1978)Land (1982)</td><td>RA</td><td>Analyst/KE Driven</td><td>Within Between Among</td></tr></table>

Another observation technique is protocol analysis (Blanning, 1984; Wright and Ayton, 1987). Protocol analysis requires that the expert "think aloud" while solving a problem. Verbalizing the steps involved may occur concurrently or retrospectively. This technique is driven by the expert and is primarily aimed at BETWEEN obstacles. Protocol analysis has its roots in KA and is not commonly used in RA. This technique is used almost exclusively to understand a domain's process or task; however, it does have some limited application to behavior understanding.

Prototyping has been used as a technique for both RA and KA (Alavi, 1984; Goul and Tonge, 1987; Luqui and Yeh, 1988; Sethi and Teng, 1988). Prototyping is an analyst-driven technique that involves the development of an executable pilot version of the system being developed. The prototype is generally only a partial representation of the entire system and is only effective for clarifying requirements and saving time that might otherwise be wasted on efforts to meet inappropriate requirements. Sethi and Teng (1988) suggest the use of prototyping to integrate ideas and settle differences resulting from traditional data and decision RA methods. In the case of KA, prototyping is useful for eliciting expert reaction leading to further KA if necessary (Goul and Tonge, 1987). This technique is useful for overcoming WITHIN and BETWEEN obstacles to both RA and KA and is particularly well-suited for problems in information requirements and process domains that may not be fully understood through some form of verbalization.

Table 3. Elicitation Technique/Problem Domain Matrix  
![](/api/attachments/7F5N4MRW/fulltext/images/6e540f8991f44fe9cf1fe960c04a91787ac71432729b305233513382d2973a65.jpg)  
Note: (O -- Observation, UE -- Unstructured Elicitation, M -- Mapping, FA -- Formal Analysis, SE -- Structured Elicitation)

Table 4. Elicitation Techniques and the Number of Domain Entities and the Categories for Which They Provide Understanding Facilities

<table><tr><td>Elicitation Technique</td><td>Number of Domain Entities</td><td>Number of Domain Categories</td></tr><tr><td>Structured Interview (KA/RA, SE)</td><td>9</td><td>4</td></tr><tr><td>Prototyping (KA/RA, O)</td><td>5</td><td>3</td></tr><tr><td>Open Interview (KA/RA, UE)</td><td>5</td><td>3</td></tr><tr><td>Variance Analysis (RA, M)</td><td>5</td><td>3</td></tr><tr><td>Protocol Analysis (KA, O)</td><td>5</td><td>2</td></tr><tr><td>Behavior Analysis (KA, O)</td><td>4</td><td>3</td></tr><tr><td>Critical Success Factors (RA, SE)</td><td>4</td><td>3</td></tr><tr><td>Cognitive Mapping (RA, M)</td><td>4</td><td>2</td></tr><tr><td>Scenario Technique (KA/RA, SE)</td><td>3</td><td>3</td></tr><tr><td>Future Analysis (RA, SE)</td><td>3</td><td>3</td></tr><tr><td>Teachback Interview (KA, UE)</td><td>3</td><td>2</td></tr><tr><td>Brainstorming Collective Decision Making (RA, UE)</td><td>2</td><td>2</td></tr><tr><td>Goal-Oriented Approach (RA, UE)</td><td>2</td><td>2</td></tr><tr><td>Machine Rule Induction (KA, FA)</td><td>2</td><td>2</td></tr><tr><td>Repertory Grid (KA/RA, FA)</td><td>2</td><td>2</td></tr><tr><td>Text Analysis (KA, FA)</td><td>2</td><td>1</td></tr><tr><td>Multidimensional Scaling (KA, M)</td><td>1</td><td>1</td></tr><tr><td>Card Sort (KA, SE)</td><td>1</td><td>1</td></tr></table>

Note: SE = Structured Elicitation; O = Observation; UE = Unstructured Elicitation; M = Mapping; FA = Formal Analysis.

## Unstructured Elicitation Techniques

Teachback interviewing (Johnson and Johnson 1987) is an elicitation technique that attempts to transform the investigator/respondent relationship into a participatory relationship. This KA technique is driven by a program of semi-structured interviews; this process has its basis in conversation theory (Pask, 1974). The program is carried out in three phases. The first simply surveys the experts and other related personnel. The second phase identifies the expert or experts with the necessary expertise to participate in the process and elicits task structure. Finally, in the third phase, results obtained by the KE are presented for criticism to the initial participants and an additional, independent population. Teachback can be classified as a specialized elicitation technique for understanding behavior models and overall goals. In teachback interviews, experts are treated as equals in the communication interchange, and, thus, this technique aids in overcoming both BETWEEN and AMONG obstacles.

The open interview (Graham and Jones, 1988) is the easiest interaction to conceive. The analyst simply goes in and allows the user or expert to talk about his or her task. This makes for a relaxed atmosphere. Due in part to this relaxed setting, an open interview can help move aside BETWEEN obstacles. Open interviews can be used for RA and KA and are useful for getting an overview of the task domain and for discovering global specifications. However, open interviews are not appropriate for obtaining detailed information requirements or operational models because uncued recall is often incomplete and unstructured.

Telem (1988a) presents a brainstorming collective decision-making approach (BCDA), which combines the use of both brainstorming and collective decision-making techniques to provide facilities for understanding problem domains. The technical aspects of the process are explained in Telem (1988b). A positive effect of BCDA is that it helps end users understand information technology and assists analysts in learning about organizational needs. The brainstorming technique is primarily aimed at WITHIN obstacles, while the collective decision-making technique addresses AMONG obstacles through collective compromise leading to agreement. BCDA is a rather specialized RA technique used mainly to overcome difficulties and constraints on task processes and to understand global goals.

A goal-oriented approach (Boland 1984; Zmud, et al., 1990) is often used when the domain is ill-structured. A wide variety of organizational personnel specify organizational goals without initially being concerned about the underlying activities to achieve the goals. By suppressing details, the participants are able to construct a consensual, although limited, model of the domain of interest. The goal-oriented approach helps overcome WITHIN and AMONG obstacles. This technique is limited mainly to obtaining overall goals of a project and has been used almost exclusively in RA.

## Mapping Techniques

Wright and Ayton (1987) present several techniques useful in knowledge acquisition, one of which is multi-dimensional scaling (MDS) to acquire conceptual structures. This technique visually represents psychological similarities between objects or experiences through the use of points on a scattergram. Spatial models help the expert overcome cognitive limitations (WITHIN obstacles). In addition, the process allows communication without the problems associated with language, thus helping to eliminate BETWEEN obstacles. MDS use is very specialized because the KA technique produces only conceptual structures.

An increasingly popular technique for requirements analysis is cognitive mapping (Montazemi and Conrath, 1986). Cognitive mapping enables the user to identify factors and determine cause-effect relationships in an effort to better understand a task or process. The use of this technique provides a structured method for the user to understand his or her cognitive processes and therefore helps overcome WITHIN obstacles to requirements analysis. In addition, the cognitive map provides a basis for communication between the user and analyst to alleviate some of the BETWEEN obstacles. Although this technique would seem extremely useful for KA, so far it has been used only for RA.

Variance analysis is an analyst-driven RA method using the existing system as a basis for determining new system requirements (Hawgood, et al., 1978). More specifically, a flow model of the existing system is evaluated to expose variances or deviations from desired standards and therefore expose operational problems. The variances are analyzed carefully by determining such things as where the variance originates, how it can be controlled, and what information is needed to control it. By presenting users with specific situations, this method reduces BETWEEN obstacles, such as miscommunication. In addition, AMONG obstacles are addressed when variances are traced through systems that encompass multiple user needs. Variance analysis is a fairly general approach to determining RA and can be used to understand the task or process, operational models, and the existing support environment.

## Formal Analysis Techniques

Mingers (1986) and Shaw (1987) both discuss the use of machine rule induction as a technique to help reduce the bottleneck associated with knowledge acquisition. Rule induction refers to the ES using a set of examples in order to induce a set of decision rules. The use of examples helps eliminate some of the communication problems during the expert/KE interaction process, reducing the BETWEEN obstacles faced. In addition, the induction process attempts to make sense of the different examples and aids in the effort to overcome AMONG obstacles. As would be expected, the use of machine induction is very limited and applies mainly to knowledge (rule) specification. Machine induction as defined here is exclusively a KA technique. However, a more liberal definition would allow for the inclusion of CASE tools used in RA.

Text analysis (Cleal and Heaton, 1988) is used only for understanding the overall problem domain. It is especially useful for systems where rules and regulations are the norm such as in law or tax systems. Because there is no direct information interaction, text analysis relieves some of the communication pressures between participants and thus aids in overcoming BETWEEN obstacles. The use of text analysis has been reported only in the KA literature, although it would seem it could also be a useful tool for RA.

Repertory grids are used to discover the distinctions between closely related concepts (Cleal and Heaton, 1988; Gammack, 1987; Gutierrez, 1987). An analyst elicits constructs and elements relevant to the system in order to form a matrix for the user to specify views regarding the system. This part of the process can be conducted by the user without much intervention by the analyst. The matrix provides a structured means for the user to express his or her thoughts and helps to eliminate WITHIN obstacles. In addition, the completed matrix forms a basis for communication between the user and analyst, therefore addressing BETWEEN obstacles. A computerized program can also be used for interpretation of the grid, thus further lessening the BETWEEN obstacles between user and analyst. Repertory grids are highly specialized tools for soliciting mental models and have proved to be useful in RA and KA.

## Structured Elicitation Techniques

Card sort (Gammack, 1987) is achieved by repeatedly sorting a deck of cards marked with specific elements. On each repeat, each pile is labeled according to its underlying concept. Rules can be extracted through classification matches. Card sort is a relatively easy elicitation method to use because people find sorting a natural and easy exercise to perform. Card sort helps the user or expert understand the concepts underlying his or her domain, thus overcoming WITHIN obstacles. It also aids in the communication between the participants, therefore combating BETWEEN obstacles. A specialized technique for discovering mental classification models, card sort has been used only in KA.

Boland (1984) introduces the scenario technique as an RA method to exploit in designing IS. Cleal and Heaton (1988) also recommend it as a method for knowledge acquisition. In the scenario technique, subjects are given some future desirable state and attempt to understand the events required to get there. Boland used the scenario technique to overcome AMONG barriers between participants in a strategic planning exercise. Imagining a particular scenario also helps participants overcome WITHIN obstacles. The scenario technique can be used as a facility for understanding problem domains across three of four problem domain categories.

Structured interviewing techniques (Edwards, 1987; Waldron, 1986; Wright & Ayton, 1987), or "asking" strategies (Davis, 1982), are suggested in order for the analyst or KE to direct the process. Strategic use of closed, open, probing, and leading questions can help overcome BETWEEN obstacles. Structured interviews are the most general elicitation approach, and a great deal of information can be gathered using the technique. Data to fill gaps, to resolve obstacles in building a system, and to support the existing environment, to name a few, can be obtained. Structured interviews have been used effectively in both RA and KA.

Critical success factors (CSFs) (Boynton and Zmud, 1984; Rockart, 1979) are the essential elements in an organization that must be given close and constant attention in order for the organization to survive and be successful. The CSF technique elicits managers' personal goals and critical success factors; it helps overcome BETWEEN obstacles by forcing the analyst to adopt the "language" used by the end users. This process is also useful for the manager's own recognition and understanding of personal goals and decision activities. In this way, WITHIN obstacles are also reduced through this technique. AMONG obstacles are addressed by combining CSFs from managers across functional areas and establishing a set of organizational CSFs. CSFs are a fairly general RA approach and can be used as an understanding facility for some aspects of all four problem domain categories.

Future analysis is one method to deal with the problem of designing systems to accommodate changing future needs (Hawgood, et al., 1979). Although the process is analyst-driven, it requires a group of representative organizational members to predict possible changes in the future that could affect the proposed system. This analysis includes both organizational and environmental changes, taking into account which elements of the system would be the most sensitive to change and how great an impact the changes would have on the organization. This collective approach is useful for reducing AMONG as well as BETWEEN obstacles to the RA process. WITHIN obstacles are also addressed by taking both a current and future oriented view of information needs. The use of future analysis is probably limited to discovering difficulties and constraints likely to be encountered in implementing a system and understanding overall goals.

## Scope of the techniques

In assessing the various techniques from the two research disciplines, it appears that the combined set does cover all of the issues that are important in eliciting an expert's knowledge or an end user's needs. For example, although the locus of control for the majority of the techniques was Analyst/KE-driven, there were some techniques where the expert or end user would lead the interaction. Typically, however, it was the unstructured elicitation techniques where the expert or end user would take the lead. The more formal techniques, such as formal analysis and structured elicitation, were always led by the analyst or KE, except for instances of one expert/user-led approach and one machine-driven approach. Moderately structured techniques, such as observation and mapping, had both types of "leadership" represented.

All of the communication obstacles were addressed by various combinations of the techniques presented. In fact, within each type—except one, the observation techniques—combinations of techniques could be put together to handle all communication obstacles presented. Every technique in observation, mapping, formal analysis, and structured techniques—along with two of the five unstructured techniques—could support BETWEEN communication.

Another observation brought out in our classification scheme is that techniques from RA and KA address very similar issues. In each elicitation type in Table 2, there are elicitation techniques that have been used in RA, KA, or both. Methods that originated in RA and are used to overcome a specific communication obstacle have counterparts originating in KA that can help overcome the same obstacle. For example, RA techniques such as future analysis and variance analysis are used to overcome the BETWEEN communication obstacle. KA techniques such as card sort and teachback interviewing are used to overcome this same communication obstacle. This pattern is generally true for the other two obstacles; however, card sort is the only “pure” KA technique used to overcome WITHIN communication obstacles.

In Table 3, the classification scheme allows for some very interesting observations regarding the relationship between the major elicitation types and the problem domain categories. These observations are indicated by the shaded areas in Table 3 grouping the techniques within the elicitation categories. To elicit information requirements, observation and structured elicitation techniques are mainly used. Observation, mapping, and structured elicitation techniques are used for process understanding. To understand the problem frame, unstructured, formal analysis, and structured elicitation techniques are used. Behavior understanding is brought about by using mainly unstructured, mapping, and structured techniques.

Finally, Table 4 gives the elicitation techniques in the order according to the number of problem domain entities and problem domain categories they address. This gives an indication of which techniques are general approaches and which are more specialized. The structured interview, which is used to understand nine of the 10 domain entities, is the most general technique. In contrast, multidimensional scaling and card sort are very specialized approaches; both address only one domain entity. It is interesting to note that the more general techniques have been used in both RA and KA, and the RA techniques, as a group, have a broader application than the KA techniques.

## Future Research Directions

This comparison of RA and KA techniques suggests numerous research possibilities. However, the five suggested research thrusts that follow seem to be both important and most likely to stimulate unanticipated research advances.

First, we need a rigorous examination of these techniques as they are used to overcome particular communication obstacles or to enrich understanding of selected problem domain entities. As mentioned earlier, little empirical research has been undertaken on which to base the entries of Tables 2 and 3. These entries were primarily based on anecdotal case histories or the authors' intuition and experience. For example, most of the techniques are declared by our scheme to overcome BETWEEN obstacles. Empirical tests need to be done to determine which of these techniques are the most effective in surmounting them. Another experiment might examine if the techniques grouped together in a domain category are more effective in overcoming BETWEEN obstacles than techniques in another category, and if they are, why. That is, what features or characteristics make them more effective in hurdling this particular obstacle? The same could be done for WITHIN and AMONG communication obstacles.

Second, it is clear that no single RA or KA technique resolves all the difficulties raised by particular problem situations. Four broad problem domain categories have been identified in this article. In assessing Table 3, it was observed that each problem domain category was supported by a combination of certain elicitation types. For example, information requirements were supported almost exclusively by observation and structured techniques. Research might be done to find the characteristics or features in the problem domain categories and the elicitation types to see why certain “category-type” combinations match so well together while others do not.

Third, related to the clustering of the elicitation types on certain problem domain categories, is the question of synergy among the techniques composing the type. Is it beneficial to use two or more techniques to better understand a particular domain category, or would this prove either costly or redundant? Would such a combination of techniques result in a “greater-than-additive” solution for the problem domain category? Using all the techniques in a cluster might very well provide views of a domain category that amplify the normal benefits provided by each. Similarly, it is important to discover if order effects exist between techniques in a type cluster, e.g., whether the order of use of certain techniques affects the realized understanding of specific domain categories. Additionally, Table 3 shows that structured techniques are the only type to support understanding in all four problem domain categories. The most domain categories supported for any other type are two. Research might be done to determine if structured techniques are really more robust than other elicitation techniques, and if so, why.

Fourth, Table 3 indicates that research directed at developing elicitation techniques for the information requirements domain category should be encouraged. The concern over constructing “user-friendly” interfaces featuring various colors, overlapping windows, pull-down windows, and motion video has heightened since more and more people are using computerized systems. Because the computer literacy of people using these systems is likely to vary quite extensively, different interfaces are appropriate for different people (Gerlach and Kuo, 1991). It is essential to have good elicitation techniques to capture this vital information.

Fifth, Table 4 provides some insight into the differences in the various techniques. The techniques that have been used exclusively in KA are, as a rule, the more specialized approaches. Another useful area of research, thus, might be to understand why specialized KA techniques seem to be more powerful than more general approaches. Do these specialized approaches really provide better facilities for domain understanding than the other approaches? This is a significant issue because if these specialized approaches do not add anything to the understanding of the problem domain, then there is little need to use them. A KE could always use the more general approaches, gain more overall understanding of the problem, save time, and also understand the one or two niche problem domain entities covered by the specialized approaches. This will become more important in the future because, as Meyer and Curley (1989, 1991a; 1991b) demonstrate, more ESs are integrating features found in traditional IS and, therefore, will need facilities to understand the other problem domain categories not addressed by these KA elicitation techniques.

## Conclusion

Requirements analysis and knowledge acquisition are the most critical steps in their respective systems development processes. It is consequently imperative that practitioners employ appropriate and sufficient tactics to improve these processes. This article presented an initial categorization scheme to facilitate the merging of research across these two areas. The scheme divides the techniques into groups by their overall method of elicitation. The matching of these elicitation types with the problem domain categories, with their locus of control, and with communication obstacles they help overcome has served to produce suggestions for a variety of research projects beneficial to both research streams.

This article has also demonstrated that techniques in RA and KA share similarities regarding characteristics and purpose. With ES adopting some of the features of IS, and vice versa, it seems imperative for KEs and analysts to be aware of a variety of elicitation techniques, regardless of their origin, to be able to develop advanced systems. It is hoped that this article will stimulate this increased awareness of the other research stream for both RA and KA researchers and practitioners.

Finally, the importance of the specific research directions presented should not be underestimated because of the importance of RA and KA in their respective development endeavors and the growing dependence of organizations on IS and ES. It is distressing, perhaps even shocking, that so little evaluation research has been undertaken on RA and KA elicitation techniques. We hope this article stimulates both IS and ES researchers to develop improved knowledge of these techniques being used to elicit the information that will form the basis of the computerized systems of tomorrow.

## References

Alavi, M. "An Assessment of the Prototyping Approach to Information Systems Development," Communications of the ACM (27:6), June 1984, pp. 556-583.

Avery, R.D. and Hoyle, J.C. "A Guttman Approach to the Development of Behaviorally-Based Rating Scales for Systems Analysts and Programmer Analysts," Journal of Applied Psychology (59:1), February 1974, pp. 61-68.

Baronas, A.K. and Louis, M.R. “Restoring a Sense of Control During Implementation: How User Involvement Leads to Systems Acceptance,” MIS Quarterly (12:1), March 1988, pp. 111-126.

Blanning, R.W. "Knowledge Acquisition and System Validation in Expert Systems for

Management," Human Systems Management (4:4), Autumn 1984, pp. 280-285.

Boehm, B.W. "Software Engineering," IEEE Transactions on Computers (C-25:12), December 1976, pp. 1226-1241.

Boehm, B.W. "Developing Small-Scale Application Software Products: Some Experimental Results," Proceedings of the IFIP 8th World Computer Congress, October 1980, pp. 321-326.

Boehm, B.W. Software Engineering Economics, Prentice-Hall, Englewood Cliffs, NJ, 1981.

Boland, R.J., Jr. "Sense-Making of Accounting Data as a Technique of Organizational Diagnosis," Management Science (30:7), July 1984, pp. 868-882.

Bostrom, R.P. "Development of Computer-Based Information Systems: A Communication Perspective," Computer Personnel (9:4), August 1984.

Bostrom, R.P. "Successful Application of Communication Techniques to Improve the Systems Development Process," Information and Management (16:5), May 1989, pp. 279-295.

Boynton, A.C. and Zmud, R.W. "An Assessment of Critical Success Factors," Sloan Management Review (25:4), Summer 1984, pp. 17-27.

Buchanan, B.G., Barstow, D., Bechtal, R., Bennett, J., Clancey, W., Kulikowski, C., Mitchell, T., and Waterman, D.A. "Constructing an Expert System," in Building Expert Systems, F. Hayes-Roth, D.A. Waterman, and D.B. Lenat (eds.), Addison-Wesley, Reading, MA, 1983, pp. 127-167.

Carter, D.M., Gibson, H.L., and Rademacher, R.A. "A Study of Critical Factors in Management Information Systems for the US Air Force," National Technical Information Service AD-A-009-647/9WA, Springfield, VA, March 1975.

Cleal, D.M. and Heaton, N.O. Knowledge-Based Systems: Implications for Human-Computer Interfaces, John Wiley and Sons, New York, NY, 1988.

Coad, P. and Yourdon, E. Object-Oriented Analysis, Prentice-Hall, Englewood, Cliffs, NJ, 1990.

Cooper, R.B. and Swanson, E.B. "Management Information Requirements Assessment: The State of the Art," Data Base (10:2), Fall 1979, pp. 5-16.

Cronan, T.P. and Means, T.L. "System Development: An Empirical Study of User Com-

munication," Data Base (15:3), Spring 1984, pp. 25-29.

Davis, G.B. “Strategies for Information Requirements Determination,” IBM Systems Journal (21:1), 1982, pp. 4-30.

Edwards, A. "Mining for Knowledge," Accountancy, April 1987, pp. 125-127.

Evanson, S.E. "How To Talk to an Expert," AI Expert (3:2), February 1988, pp. 36-42.

Feigenbaum, E.A. and McCorduck, P. The Fifth Generation, Addison-Wesley, Reading, MA, 1983.

Fellers, J.W. “Skills and Techniques for Knowledge Acquisition: A Survey, Assessment, and Future Directions,” Proceedings of the Eighth International Conference on Information Systems, Pittsburgh, PA, December 6-9, 1987, pp. 118-132.

Fellers, J.W., Bostrom, R.P., and Wynne, B.E. "An Exploratory Investigation of Critical Success Factors for Knowledge Acquisition in Expert Systems Development," paper presented at The Conference on the Impact of Artificial Intelligence on Business and Industry, Denton, TX, October 1988.

Franz, C.R. “User Leadership in the Systems Development Life Cycle: A Contingency Model,” Journal of Management Information Systems (2:2), Fall 1985, pp. 5-25.

Franz, C.R. and Robey, D. "An Investigation of User-Led System Design: Rational and Political Perspectives," Communications of the ACM (27:12), December 1984, pp. 1202-1209.

Freeman, C. "Chemical Process Plant: Innovation and the World Market," National Institute Economic Review (45), August 1968, pp. 29-57.

Galliers, R.D. (ed.). Information Analysis: Selected Readings, Addison-Wesley, Reading, MA, 1987.

Galliers, R.D. and Lyons, L.W. “Attitudes of Western Australian Managers to Computerized Information Systems. The Impact of IT on Managerial Work: A Survey of Western Australian Managers’ Attitudes,” working paper, Western Australian Institute of Technology, Perth, Western Australia, 1985.

Gammack, J.G. "Different Techniques and Different Aspects on Declarative Knowledge," in Knowledge Acquisition for Expert Systems: A Practical Handbook, A.L. Kidd (ed.), Plenum Press, New York, NY 1987, pp. 137-163.

Gerlach, J.H. and Kuo, F.Y. "Understanding Human-Computer Interaction for Information Systems Design," MIS Quarterly (15:4), December 1991, pp. 527-549.

Goul, M. and Tonge, F. "Project IRMA: Applying Decision Support System Design Principles to Building Expert-Based Systems," Decision Sciences (18:3), Summer 1987, pp. 448-467.

Graham, I. and Jones, P.L. Expert Systems: Knowledge, Uncertainty, and Decision, St. Edmundsbury Press Ltd., Bury St. Edmunds, Suffolk, England, 1988.

Gutierrez, O. "Some Aspects of Information Requirements Analysis Using A Repertory Grid Technique," in Information Analysis: Selected Readings, R.D. Galliers (ed.), Addison-Wesley, Reading, MA, 1987, pp. 347-362.

Hackathorn, R.D. and Karimi, J. "A Framework for Comparing Information Engineering Methods," MIS Quarterly (12:2), June 1988, pp. 203-220.

Hart, A. Knowledge Acquisition for Expert Systems, Billings and Son Ltd, Worcester, England, 1989.

Hawgood J., Land, F., and Mumford, E. "A Participative Approach to Forward Planning and System Change," Information Systems Methodology: Proceedings of the Second Conference of the European Cooperation in Informatics, Venice, Italy, October 10-12, 1978, pp. 39-81.

Hayes-Roth, F.D. "The Knowledge-Based Expert System: A Tutorial," IEEE Computer (17:9), September 1984a, pp. 11-28.

Hayes-Roth, F.D. "Knowledge-Based Expert Systems," IEEE Computer (17:10), October 1984b, pp. 263-273.

Hayes-Roth, F.D., Waterman, D.A., Lenat, D.B. (eds.). Building Expert Systems, Addison-Wesley, Reading, MA, 1983.

Henderson, J.C. and Cooprider, J.G. "Dimensions of I/S Planning and Design Aids: A Functional Model of CASE Technology," Information Systems Research (1:3), September 1990, pp. 227-254.

Hirschheim, R. and Klein, H.K. "Four Paradigms of Information Systems Development," Communications of the ACM (32:10), October 1989, pp. 1199-1216.

Ives, B. and Olson, M.H. "User Involvement and MIS Success: A Review of Research," Management Science (30:5), May 1984, pp.

586-603.

Johnson, L. "The Needs for Competence Models in the Design of Expert Systems," International Journal in Systems Research and Informational Science (1), 1985, pp. 23-36.

Johnson, L. and Johnson, N.E. "Knowledge Elicitation Involving Teachback Interviewing," in Knowledge Acquisition for Expert Systems, A. Kidd (ed.), Plenum Press, New York, NY, 1987, pp. 91-108.

Kaiser, K.M. and King, W.R. "The Manager-Analyst Interface in Systems Development," MIS Quarterly (6:1), March 1982, pp. 49-59.

Kidd, A. (ed.). Knowledge Acquisition for Expert Systems, Plenum Press, New York, NY, 1987.

Kim, J. and Courtney, J.F. "A Survey of Knowledge Acquisition Techniques and Their Relevance to Managerial Problem Domain," Decision Support Systems (4:3), September 1988, pp. 269-284.

Knight, K.E. A Study of Technological Innovation: The Evolution of Digital Computers, unpublished Ph.D dissertation, Carnegie Institute of Technology, Pittsburgh, PA, 1963.

Land, F.F. “Adapting to Changing User Requirements,” Information and Management (5:2), 1982, pp. 59-75.

Luqui, V.B. and Yeh, R.T. "A Prototyping Language for Real-Time Software," IEEE Transactions on Software Engineering (14:10), October 1988, pp. 1409-1423.

Martin, M.P. and Fuerst, W.L. "Communications Framework for System Design," Journal of Systems Management (35:3), March 1984, pp. 18-25.

McDermott, J. "R1: The Formative Years," AI Magazine (2:1), 1981, pp. 21-29.

McDermott, J. "R1: A Rule-Based Configurer of Computer Systems," Artificial Intelligence (19:1), September 1982, pp. 39-88.

Meyer, M.H. and Curley, K.F. "Expert Systems Success Models," Datamation, September 1989, pp. 35-38.

Meyer, M.H. and Curley, K.F. "Putting Expert Systems Technology to Work," Sloan Management Review (32:2), Winter 1991a, pp. 21-31.

Meyer, M.H. and Curley, K.F. "An Applied Framework for Classifying the Complexity of Knowledge-Based Systems," MIS Quarterly (15:4), December 1991b, pp. 455-472.

Mingers, J. "Expert Systems — Experiments with Rule Induction," Journal of the Operational

Research Society (37:11), November 1986, pp. 1030-1037.

Mittal, S. and Dym, C.L. "Knowledge Acquisition from Multiple Experts," AI Magazine (6:2), Summer 1985, pp. 32-36.

Mittermeir, R.T., Hsia, P., and Yeh, R.T. “Alternatives to Overcome the Communication Problem of Formal Requirements Analysis,” in Requirements Engineering Environments, M. Ohno (ed.), North-Holland, Amsterdam, 1982.

Montazemi, A.R. and Conrath, D.W. "The Use of Cognitive Mapping for Information Requirements Analysis," MIS Quarterly (10:1), March 1986, pp. 45-56.

Munro, M.C. and Davis, G.B. “Determining Management Information Needs: A Comparison of Methods,” MIS Quarterly (1:2), June 1977, pp. 55-67.

Oliver, I. and Langford, H. “Myths of Demons and Users,” in Information Analysis: Selected Readings, R. Galliers (ed.), Addison Wesley, Reading, MA, 1987, pp. 113-123.

Pask, G. Conversation, Cognition, and Learning: A Cybernetic Theory and Methodology, Elsevier, London, 1974.

Popolizio, J.J. and Cappelli, W.S. “New Shells for Old Iron,” Datamation, April 15, 1989, pp. 41-48.

Rockart, J.F. "Chief Executives Define Their Own Data Needs," Harvard Business Review (57:2), March/April 1979, pp. 81-91.

Roth, E.M. and Woods, D.D. “Cognitive Task Analysis: An Approach to Knowledge Acquisition for Intelligent System Design,” in Topics in Expert Systems Design: Methodologies and Tools, G. Guida and C. Tasso (eds.), North Holland, Amsterdam, 1989, pp. 233-264.

Scharer, L. "Pinpointing Requirements," Datamation (27:2), April 1981, pp. 139-140.

Sethi, V. and Teng, J.T. “Choice of an Information Requirements Analysis Method: An Integrated Approach,” INFOR (26:1), February 1988, pp. 1-16.

Shaw, M.J. “Applying Inductive Learning to Enhance Knowledge-Based Expert Systems,” Decision Support Systems (3:4), December 1987, pp. 319-332.

Shaw, M.L.G. and Gaines, B.R. "An Interactive Knowledge Elicitation Technique Using Personal Construct Technology," in Knowledge Acquisition for Expert Systems, A. Kidd (ed.), Plenum Press, New York, NY, 1987, pp. 109-136.

Smith, G.F. "Defining Managerial Problems: A Framework for Prescriptive Theorizing," Management Science (35:8), August 1989, pp. 963-981.

Sviokla, J.J. “Business Implications of Knowledge-Based Systems, Part I,” Data Base (17:4), Summer 1986a, pp. 5-19.

Sviokla, J.J. “Business Implications of Knowledge-Based Systems, Part II,” Data Base (18:1), Summer 1986b, pp. 5-19.

Taggart, W.M. and Tharp, M.O. “A Survey of Information Requirements Analysis Techniques,” Computing Surveys (9:4), December 1977, pp. 273-290.

Telem, M. "Information Requirements Specification I: Brainstorming Collective Decision-Making Approach," Information Processing and Management (24:5), 1988a, pp. 549-557.

Telem, M. "Information Requirements Specification II: Brainstorming Collective Decision-Making Approach," Information Processing and Management (24:5), 1988b, pp. 559-566.

Valusek, J.R. and Fryback D.G. "Information Requirements Determination: Obstacles Within, Among, and Between Participants," in Information Analysis: Selected Readings, R. Galliers (ed.), Addison Wesley, Reading, MA, 1987, pp. 139-151.

von Hippel, E. "The Dominant Role of Users in the Scientific Instrument Innovation Process," Research Policy (5), 1976, pp. 212-219.

von Hippel, E. "The Dominant Role of Users in Semiconductor and Electronic Process Innovation," IEEE Transactions on Engineering Management (24:2), May 1977, pp. 60-71.

von Hippel, E. "Lead Users: A Source of Novel Product Concepts," Management Science (32:7), July 1986, pp. 791-805.

Waldron, V.R. "Interviewing for Knowledge," IEEE Transactions on Professional Communications (29:2), June 1986, pp. 31-34.

Wasserman, A.I., Freeman, P., and Porcella, M. "Characteristics of Software Development Methodologies," in Information Systems Design Methodologies, T.W. Olle, H.G. Sol, and C.J. Tully (eds.), IFIP WG 8.1, York, North-Holland, Amsterdam, July 1983, pp. 5-7.

Weitzel, J.R. and Kerschberg, L. “Developing Knowledge-Based Systems: Reorganizing the System Development Life Cycle,” Communications of the ACM (32:4), April 1989, pp. 482-488.

Wright, G. and Ayton, P. "Eliciting and Model-

ling Expert Knowledge," Decision Support Systems (3:4), December 1987, pp. 13-26.

Zmud, R.W. Information Systems in Organizations, Scott, Foresman and Company, Glenview, IL, 1983.

Zmud, R.W., Anthony, W.P., and Stair, R. "The Use of Mental Imagery as a Technique for Eliciting Ill-Structured Requirements," working paper, Florida State University, Tallahassee, FL, 1992.

## About the Authors

Terry Anthony Byrd is assistant professor of MIS in the Information and Management Sciences Department at the College of Business, Florida State University. He holds a B.S. in electrical engineering from the University of Massachusetts-Amherst and a Ph.D in MIS from the University of South Carolina. His research has appeared or is forthcoming in Journal of Management Information Systems, Interfaces, International Journal of Production Research, Annals of Operations Research, and others. His research interests in clude technological innovations and organizational change, technology education and organizational learning, and information and knowledge processing in organizations.

Kathy L. Cossick is assistant professor of information systems at the University of Houston. She is currently completing her Ph.D. from Florida State University. Her research interests include the integration of psychological theories of human decision making into DSS design, and behavioral aspects of information systems.

Robert W. Zmud is professor and Thomas L. Williams, Jr., Eminent Scholar in Management Information Systems in the Information and Management Science Department at the College of Business, Florida State University. His current research interests focus on understanding the impact of information technology in organizations and on understanding the appropriateness of managerial strategies regarding IT-related policies, plans, controls, and related organizational arrangements. Both his Ph.D. (University of Arizona) and his S.M. (MIT) degrees are in management.
