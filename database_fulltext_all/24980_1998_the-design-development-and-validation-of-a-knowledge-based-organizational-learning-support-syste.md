---
otero_id: 24980
otero_key: "6AWPRS6J"
title: "The Design, Development, and Validation of a Knowledge-Based Organizational Learning Support System"
authors: "Michael J. Hine; Michael Goul"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518211"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Design, Development, and Validation of a Knowledge-Based Organizational Learning Support System

Michael J. Hine & Michael Goul

To cite this article: Michael J. Hine & Michael Goul (1998) The Design, Development, and Validation of a Knowledge-Based Organizational Learning Support System, Journal of Management Information Systems, 15:2, 119-152, DOI: 10.1080/07421222.1998.11518211

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518211

![](/api/attachments/6AWPRS6J/fulltext/images/19aa0537759e1ae70a03fd9bfd852d86de8540c2ffed5281330d7efc82cd9355.jpg)

Published online: 07 Dec 2015.

![](/api/attachments/6AWPRS6J/fulltext/images/7ef0efc7e5c2c89ab76a4636cc6b39c6a6a411575fb41867d6a35ecaa49d3193.jpg)

Submit your article to this journal

![](/api/attachments/6AWPRS6J/fulltext/images/174a2cfebbe2dd6d745cc2560eb78054576307eac9152cdf03984c17d6a595e6.jpg)

View related articles

![](/api/attachments/6AWPRS6J/fulltext/images/26c6df146e60139da6f02a60ed617eed1e612a52474e3864cdff4c94e4632b18.jpg)

Citing articles: 1 View citing articles

# The Design, Development, and Validation of a Knowledge-Based Organizational Learning Support System

MICHAEL J. HINE AND MICHAEL GOUL

MICHAEL J. HINE is an Adjunct Faculty member with the Employment Support Institute at Virginia Commonwealth University. He is also Vice President of the Monster Consulting Group, Inc. Dr. Hine is currently designing and developing decision support software that will assist persons with disabilities and their advocates to make well-informed choices with regard to the benefits of return to work. He has published numerous articles in the area of knowledge-based DSS. His current research interests include knowledge-based organizational support systems, mental modeling, and the visual representation of cognitive constructs.

MICHAEL GOUL is an Associate Professor of Computer Information Systems and serves as Director of Information Technology for the College of Business at Arizona State University. His recent research interests integrate the disciplines of decision support, distributed artificial intelligence, and Web search agents. His research has been published in a wide range of academic and practitioner journals, including Decision Support Systems, Organizational Computing, IEEE Expert, Communications of the A CM. Journal of Managament Information Systems, and others. Dr. Goul is currently Vice President for Member Activities of the Association for Information Systems.

ABSTRACT: It is generally agreed that organizational learning involves the processes of developing and exchanging organizational members' underlying opinions, assumptions, and interpretations of the environment. This exploratory research applies innovative information technology (IT) to support and facilitate organizational learning. The organizational learning process is defined, and inhibitors to the process are identified and translated into system requirements for the design and development of the Organizational Learning Support System (OLSS) toolkit. The OLSS toolkit uses a knowledge-based system to elicit initial interpretations of the environment from organizational members and automatically detects where organizational members' interpretations conflict and where they are in consensus. It uses a heuristic approach to order the presentation of the conflicts to the organizational members. A validation in the form of a pilot study is included.

KEY WORDS AND PHRASES: knowledge-based decision support systems, organizational decision support systems, organizational learning.

TODAY'S ORGANIZATIONS FACE DYNAMIC ENVIRONMENTS THAT NEED TO BE constantly monitored and evaluated. The continuous shifting of environments and the resulting complexities have fostered the realization that a high capacity to learn is a critical requirement for effective operation of an organization [I, 13]. The information technology (IT) discipline has recognized this. Organizationalleaming has been identified as an increasingly significant issue to be addressed by IT research [4, 5, 9, 37].

Two themes of organizational learning have emerged: the systems-structural perspective and the interpretive perspective [7]. The systems-structural perspective emphasizes acquisition and distribution of information required for an orgamzation to learn about its environment. Alternatively, the interpretive perspective emphasizes the underlying purpose and meaning of environmental events. While the systemsstructural perspective has received attention in recent literature, the interpretive perspective remains underaddressed [7].

Interpretive organizational learning is defined as the process of generating cognitive interpretations of environmental events, and the development of shared understandings of interpretations. Interpreting an environmental event involves explaining to oneself the meaning of that event. To understand another manager's interpretation of an event involves comprehending the meaning intended by that manager. While a unified interpretation may be the goal of interpretative organizational learning, it is the process of surfacing, sharing, and understanding various interpretations that characterizes interpretive organizationalleaming. Huber [24, p. 102] states:

It seems reasonable to conclude that more learning has occurred when more and more varied interpretations have been developed .... It also seems reasonable to conclude that more learning has occurred when more of the organization's units understand the nature of the various interpretations held by other units.

Thus, interpretive organizational learning is not dependent on achieving consensus in various perspectives, but it focuses on generating and understanding different interpretations.

Surfacing and understanding the underlying meaning of environmental perspectives posited by managers means that equivocality reduction is a requirement for an interpreting, and therefore a learning, organization [7, 29]. Equivocality is present when there are multiple and conflicting interpretations [60]. It is reduced when managers exchange opinions, perceptions, and judgments [7]. Daft and Huber [7] maintain that IT research needs to involve the design, development, and validation of effective interpretation systems. This study focuses on a description and operationalization of a methodology for the design and development of an IT -based conflict detection organizational learning support system (OLSS) toolkit.

IT research in organizational learning is likely to proceed from an exploratory research framework, that is, a prototyping approach. This approach is consistent with the applications tradition of DSS research (e.g., [21 D. Proceeding requires the selection of a domain where results have impact, that is, a domain where interpretive organizational learning is critical. An appropriate domain is strategic management. One major premise of strategic management is the alignment of the organization with its environment [20]. Alignment implies the ability to learn [13]. When organizations are misaligned with their environment, they cannot remain competitive and often fail (e.g., [34, 53]). This misalignment is frequently attributed to misinterpretation of equivocal environmental cues [7].

Environmental assessment is the critical initial step in the strategic management process [ 17]. We view environmental assessment as a cognitive conflict task. A cognitive conflict task deals with addressing conflict of viewpoint [33]. For example, managers may interpret information differently, identifY different strategic variables, and disagree about causal relationships among strategic variables. The purpose of OLSS in this context is to assist organizational members in interpreting and facilitating the development of a common understanding of the strategic environment.

This paper describes in detail a methodology for the design and development of an interpretive organizational learning support system. It also describes the resulting OLSS toolkit and some preliminary results from the use of the system. A review of interpretation systems is presented first. This is followed by an explanation and operationalization of the traditional prototype-oriented DSS development methodology within the context of organizational learning and strategic management. Fundamental OLSS requirements and the design of the OLSS toolkit are described. Initial results from a pilot study are presented and discussed. Conclusions, limitations, and future research related to the OLSS end the paper.

## Technology to Support Interpretive Organizational Learning

SEVERAL ESPOUSED THEORIES AND MODELS EXIST ABOUT HOW individuals and organizations interpret organizational events that provide a discussion context of existing IT to support the interpretation process [10, 16,25,35]. However, we do not limit discussion to the nuances of a single model; instead, we examine existing IT to support interpretation within a widely accepted context. The interpretation process involves translating events and developing shared understanding and conceptual schemes of the environment among top management team members. Thus, the interpretation process can be thought of as supporting/facilitating/assisting first, the development and representation of individual environmental interpretations, and second, the exchange and comparison of interpretations, opinions and underlying environmental assumptions. Table I summarizes existing IT to support the two interpretation stages.

The main issue in discussing IT to support individual interpretations is how to represent an interpretation. Abundant throughout the management cognition literature are studies that use causal modeling to represent managers' strategic interpretations of their environments [2, 3, 14,28,61]. This literature base was used in IT-supported systems utilizing causal modeling to represent interpretations. For this literature review, the term "causal modeling" refers to the process of representing a set of strategic elements and the causal representation between the elements. Cognitive maps, influence diagrams, and mind maps are all approaches consistent with this type of knowledge organization [40].

Lee, Courtney, and O'Keefe [29] focus on the design of a system to support organizational learning. They define several system requirements for an organizational learning system (OLS). Their system, Collective Cognitive Mapping System (CoCoMap), not only supports individual maps, but both detects differences in maps and allows for knowledge sharing and construction of a collective cognitive map. Individual and derived maps can be stored as cases that can be retrieved to analyze new situations. Similarly, Pool2 allows the derivation of a global cognitive map (primary cognitive map [PCM]) from mUltiple experts [62]. The PCM is analyzed by a cognitive mapping understanding subsystem that enforces cognitive integrity, clarifies implications, and resolves inconsistencies and results in an advanced cognitive map (ACM). The ACM can be used by the decision analysis subsystem to respond to users' queries regarding the cognitive structure.

Table 1. Infonnation Technology Supporting Interpretation

<table><tr><td>Development and representation of individual interpretations</td><td>Exchange/comparison of interpretations, opinions, and assumptions</td></tr><tr><td>Causal modeling</td><td>Causal modeling</td></tr><tr><td>CoCoMap [29]</td><td>CoCoMap</td></tr><tr><td>Pool2 [62]</td><td>Pool2</td></tr><tr><td>COPE [11]</td><td>COPE</td></tr><tr><td>MIND [42]</td><td></td></tr><tr><td>GISMO [40]</td><td></td></tr><tr><td></td><td>Group support systems</td></tr><tr><td>Others</td><td>Cognitive conflict GSS [48]Software-aided meeting management (SAMM) [59]</td></tr><tr><td>VISION [6]</td><td>GroupSystems [36]</td></tr><tr><td>KBS [18]</td><td></td></tr></table>

Another cognitive mapping system is COPE [11]. This system allows groups of managers to create individual maps of their strategies in the fonn of goals, options, and concepts. COPE allows for the synthesis of individual cognitive maps into global "strategic maps." Concepts can be heuristically ranked in importance, and specific lines of arguments can be displayed.

Ramaprasad and Poon [42] developed a computerized system for eliciting, mapping, and interpreting influence diagrams (MIND). In MIND, strategic elements are categorized as decision elements, objective elements, and environmental elements. MIND eliminates the tedious process of manually identifYing and interrelating a large number of strategic elements, thus allowing the strategists to concentrate on strategic issues.

The Graphical Interactive Structural Modeling Option (GISMO) focuses on helping to fonnulate a graphical definition of the problem at hand, maintain that image, access and manipulate the problem models, and finally to analyze the structures [40]. The fundamental premise of GISMO is that a user's understanding ofa complex problem is enhanced through the "natural feeling" provided by an interactive visual-based system.

Causal-based modeling seems to be the dominant method of representing interpretations, but other approaches are available. Carlson [6] uses cognitive-complexity theory to describe and organize managers' knowledge. He uses the cognitive complexity "concepts" of dimensions, discrimination, differentiation, and integration as the cornerstones of the VISION system. VISION uses a filebox-filecard metaphor along with an object-oriented method to represent and store knowledge.

One promising approach to help interpretation and sense making is the use of knowledge-based systems. Studies of strategic experts conclude that experts have complex structures to recognize and interpret environmental signals and events [31]. These structures contain many links among strategic elements and hence contain more elements than less experienced strategists [8, 30). It is apparent that strategists formulating directions for an organization operating within a dynamic, ambiguous environment would benefit from access to broad-based expert advice. To this extent, research by Goul, Shane, and Tonge [19] focused on the development and use ofa knowledge-based system to support the assessment (interpretation) of an individual user's strategic environment. Individuals with access to the generic strategy knowledge interpreted their environment better than did individuals without access to the knowledge-based system.

Other avenues exist for the development and representation of environmental interpretations. Rockart and DeLong [43] use executive support systems (ESS) to develop, clarify, or enhance managers' mental models of organizations' environments. The goal of ESS is to provide upper-level management easy access to relevant decision-making information. Vandenbosch and Higgins suggest that ESS can contribute to two types of individual learning: mental model maintenance and mental model building [58).Jt appears that current ESS can affect a manager's interpretation through access to high-quality information and analysis capabilities, but ESS do not support the representation of the interpretations.

In addition to the cognitive mapping systems discussed above, the discipline of group support systems (GSS) provides approaches for the exchange ofinterpretations, opinions, and assessments. While GSS are not designed to be OLSS, the relevant features and findings pertaining to OLSS design are summarized here. First, however, it is important to note that, while GSS typically prove support for the exchange of opinions and interpretations, typically little is provided in the way of automatically detecting and surfacing disagreements and/or conflicts in complex models of a strategic environment. In this sense, current GSS are "shallow" in contrast to the "deep" knowledge structures of the OLSS toolkit developed and discussed here. The following GSS research is summarized as it pertains to the design ofOLSS:

1. Sengupta and Te'eni [48] studied the effects of cognitive feedback on cognitive conflict. Two constructs were used to assess cognitive conflict: cognitive control and strategy convergence. The results showed a significant positive relationship between cognitive feedback and strategy convergence. The implication of this finding is that OLSS need "deep" knowledge structures that are capable of providing cognitive feedback beyond that provided in more "shallow" GSS.

2. Watson, DeSanctis, and Poole [59] attempted to assess pre- and postmeeting conflict between group members using an instrument in Spillman, Bezdek, and Spillman [51]. The results of this study indicate that a structured approach to surfacing both agreement and conflict within a group, whether system supported or manually introduced, was preferable. The implication of this finding is that OLSS need "deep" knowledge structures capable of structuring agendas for surfacing both agreement and conflict in a group.

3. Miranda and Bostrom [36] conducted a longitudinal study on group conflict and conflict management designed to differentiate between issue-based and interpersonal conflict. The findings were consistent with those of [59], although system-supported groups had less issue-based conflict than did manually supported groups. This implies that properly designed OLSS can enable better performance than non--system-supported groups. In addition, it indicates that the use of GSS voting tools often prematurely cuts off discussions (e.g., [38]) before potentially conflicting viewpoints have been addressed by a group. This implies that OLSS toolkit features need to be designed to "speed up the discovery" of conflicting viewpoints so that issue-based conflicts will not be prematurely cut off by a voting process supported by a GSS.

Technology support for the process of interpretation is inconclusive. While GSS provides innovations that facilitate the exchange of ideas and opinions on issues, the information communicated is shallow. Topics of discussion are a function of some preformulated task rather than issues generated from managers' models of reality. Alternatively, some work has been done in the generation and representatIon of interpretations. While several of these approaches allow for the comparison of models (CoCoMap, Pool2, SPS, COPE, MIND, GISMO), fewer provide a formal methodology for eliciting the complex interpretations that managers so often cannot formulate (COPE, MIND, GISMO, KBS), and a smaller subset (COPE) use the knowledge resulting from the comparison process actively to facilitate interaction between group members. The research presented here:

I. Extends Goul, Shane, and Tonge's initial work [19] on the use of know 1- edge-based systems to generate and represent individual interpretations;

2. Provides "deep" comparisons of the interpretations and;

3. Uses the interpretation comparison knowledge intelligently to guide interaction of managers in the goal of better understanding their competitive environment.

## Initial OLSS Requirements

THE PROCESS TO BE SUPPORTED (INTERPRETIVE ORGANIZATIONAL LEARNING) is defined, and inhibitors to the process are identified and translated into an initial set of OLSS requirements. This is consistent with a prototype-oriented DSS development methodology [52]. Figure I shows the process of organizational learning in a strategy methodology [52]. Figure I shows the process of organizationalleaming in a strategy context.

![](/api/attachments/6AWPRS6J/fulltext/images/91b8e4e132047c50c0927ef6e6723a9cefc09d8ed66b0aaab71077047f77e30d.jpg)  
Figure 1. Process of Organizational Learning

Managers scan their environments through various knowledge sources for information that is distributed among relevant strategists. Individual assessments and interpretations of the strategic environment are developed from environmental cues, organizational memory (past policies, procedures, strategies, and organizational culture), and existing knowledge. Managers exchange their underlying assumptions, perceptions, and interpretations toward the goal of improving their understanding of the competitive environment and to move toward consensus. This process involves identifying where interpretations overlap and conflict. Conflicts must be addressed so that an organizational interpretation can be developed. An organization's interpretation of its environment becomes part of organizational memory and is used in future sessions.

Group cognition literature has found that top management teams often simplify both the problem under consideration and the environment in which they operate, resulting in the exclusion from their interpretations of potentially viable alternatives and important environment variables [12]. Further, it has been found that groups whose interpretive templates were more integratively complex than others displayed significantly better decision performance [55]. Literature on strategic experts states that experts have complex structures that allow the recognition and interpretation of environmental signals and events [31] and that these structures are more complex, contain more links among strategic elements, and hence contain more elements than less-experienced strategists [8, 30]. It is apparent that, when interacting with a dynamic, ambiguous environment, support for the development of complex interpretations and identification of potentially important domain concepts is beneficial and facilitates interpretive organizational learning.

Based on the process of organizational learning and the identified inhibitor, an initial set of operational requirements for an OLSS includes: the development of complex internally consistent individual interpretations, the sharing of individual and group interpretations, the detection of conflicts and commonalities among the individual and group interpretations, and, finally, the consolidation of multiple interpretations into an internally consistent global interpretation. An organized statement of these requirements follows:

I. Interpreting the environment: The complexity and ambiguity of the environment can be detrimental to the learning process. To support interpretive organizational learning in a dynamic environment properly, a method for formalizing the environment through a theoretical model would be desirable. The purpose is to provide a common context and grammar in which to discuss the strategic environment.

2. Individual interpretations: Critical to interpretive organizational learning are an individual's underlying assumptions and interpretations. From an IT perspective, tools and methods that surface assumptions and underlying views are required. Further, a knowledge representation scheme for the interpretations is required. This scheme will provide the basis for intraindividual comparison and synthesis. Finally, the interpretations should be internally consistent.

3. Comparison of interpretations: Individual managers must exchange their assumptions, theories, and interpretations of the environment. Conflicts in individual interpretations must be surfaced and addressed. The impacts of the exchange must be assessed and manager's interpretations updated. Germane to interpretation update is research in problem restructuring, which has focused on the ability to change a problem representation when an agent's perception of the problem evolves [49]. This area of research has been pursued with different approaches and methodologies in several well-developed negotiation support systems such as MEDIATOR [50], NEGOPLAN [27], and PERSUADER [54]. While much of this research focused on negotiation tasks, its implications are relevant to cognitive conflict tasks. Cognitive conflict tasks can have an emerging problem or interpretation structure. In the context of the OLSS, as managers exchange individual interpretations, their perceptions of the environment may change, and these modifications need to be represented in the emerging organizational interpretation. As interpretations are updated, different conflicts and overlap may surface. Dynamic recompilation of individual interpretations to restructure the form and content of the emerging global interpretation is desirable.

Researchers have encouraged building decision conflict into group activities to facilitate the definition and elicitation of underlying environmental assumptions. Schweiger and Sandberg [45] and Schweiger, Sandberg, and Rechner [46] found that both dialectical inquiry and devil's advocacy (two conflict-based approaches) yielded better decisions than more traditional consensus-based methods. Further, Schwenk [47] found that devil's advocacy improved decision making over an expert-based approach. The drawback to forcing conflict into the decision process is that it may cause animosity among group members. Focusing on common assumptions and theories may reduce this animosity and strengthen the bond among members of the group. Further, Sambamurthy and Poole found that the inclusion of consensus structures with communication structures in GSS resulted in higher levels of confrontation and consensus than did GSS with only communication structures [44]. It thus seems appropriate to make both conflicts and commonalities between initial individual interpretations explicit.

4. Synthesis of interpretations: Automatic synthesis should occur when interpretations are not in conflict. However, when conflicts are substantial, meetings should be triggered to address assumptions and conflicting issues. As the degree of conflict changes, the system should allow for updating of the global interpretation.

5. Development and maintenance of organizational memory: Huber [24] posits that the inclusion of computer technology as part of organizational memory has potential for assisting organizations in "knowing what they know." It follows that capabilities for storing and retrieving interpretations should be a requirement for IT-based OLSS.

## Initial OLSS Toolkit

AN INITIAL KNOWLEDGE REPRESENTATION SCHEME AND TOOLKIT have been designed and developed based on the above requirements. This section discusses in detail the components of the OLSS toolkit, the representations used by the toolkit, and the process involved in its use.

<table><tr><td>REQUIREMENT</td><td rowspan="2">Satisfied By</td><td>BASE MODULE</td><td>AVAILABLE SECONDARY MODULE</td></tr><tr><td>Generation and Representation of Interpretations</td><td>Environmental Interpretation Generator</td><td>Cognitive Conflict Detector, Focuser, Knowledge Updater</td></tr><tr><td>Comparison of Interpretations</td><td>Satisfied By</td><td>Interpretation Correlator</td><td>Alarmer, Focuser, Knowledge Updater</td></tr><tr><td>Synthesis of Interpretations</td><td>Satisfied By</td><td>Interpretation Synthesizer</td><td>Focuser, Knowledge Updater</td></tr><tr><td>Building Organizational Memory</td><td>Satisfied By</td><td>Interpretation Generator, Interpretation Correlator, Interpretation Synthesizer</td><td>Alarmer, Cognitive Conflict Detector, Focuser, Knowledge Updater</td></tr></table>

Figure 2. OLSS Toolkit Modules

## Overview of the OLSS Toolkit Modules

The initial OLSS toolkit consists of a set of base and secondary modules. Figure 2 shows the modules and their correspondence to the system requirements. The first column of the figure contains the fundamental system requirements. The second column shows the base modules of the toolkit. Each base module is shown directly to the right of the system requirement it is designed to satisfy. Secondary modules are shown in the third column and are available only when one of its corresponding base modules is operating. For example, the interpretation corre/ator must be active for the alarmer to be used. The base and secondary modules to support the building of organizational memory are simply an aggregation of the modules designed to support the previous requirements. The base modules include an environmental interpretation generator, an interpretation correia tor, and an interpretation synthesizer. The secondary modules include a cognitive conflict detector, a focuser, an alarmer, and a know/edge updater.

Figure 3 shows a conceptual model of the OLSS. The two major functions provided by the toolkit are individual interpretation generation and interpretation correlation and synthesis. The toolkit modules are discussed within the context of these two functions.

## Generating Individual Interpretations

The environmental interpretation generator uses a knowledge-based run-time shell system to surface an individual interpretation. Recall that research by Goul, Shane, and Tonge [19] successfully developed and used a knowledge-based system to support the assessment (interpretation) of an individual user's strategic environment. Extending this individual manager orientation, this study uses a knowledge-based system to surface initial interpretations of the environment that become inputs into conflict and consensus detection system modules. The knowledge-based elicitation approach is appropriate because:

![](/api/attachments/6AWPRS6J/fulltext/images/862808aa5b4acaa53a96adb1009b4c794570948d4b945c962f663449d2d3fad0.jpg)

KEY direct flow ---\~ conditional flow \~/ cognitive conflict loop

Figure 3. Conceptual Model ofOLSS

1. It helps overcome cognitive limitations of managers by supporting the elicitation of a complex interpretation;

2. It provides a common grammar for interpretation comparison, interpretation synthesis, and for manager discussion (the presence of a common grammar has been identified by Weick [60] as a necessary requirement for equivocality reduction); and

3. It provides a method for giving meaning to the data currently known about the strategic environment.

The present study uses the CoEx architecture [19]. Co Ex is a GSS designed to support a host of cooperating experts in the development and maintenance of a distributed knowledge-based system. To date, a partitioned strategic management knowledge base has been designed, developed, and validated. The current knowledge base, based on Porter's [39] competitive strategy model, contains approximately one hundred questions that are logically partitioned into twelve different folders. Sample questions and answers from the most accessed folders are shown in Table 2.

Each user initially answers all the questions in the diagnostics questions folder. Depending on the answers provided, the system determines which other folders are relevant to the user's line of inquiry. The system heuristically orders the presentation of the folders. Thus, managers may be directed into different folders and presented with different questions. The system provides knowledge-based advice based on the users' answers to the questions.

Table 2. Sample Folders, Questions, and Answers from Strategy Knowledge Base

<table><tr><td>Folder</td><td>Example question</td><td>Answers</td></tr><tr><td>Diagnostic questions</td><td>The number of firms competing for the company&#x27;s markets are:</td><td>A. Increasing noticeablyB. Fluctuating, but relatively constantC. Decreasing noticeably</td></tr><tr><td>Emerging industries</td><td>Costs of opening a new market are:</td><td>A. HighB. LowC. Cannot determine</td></tr><tr><td>Capacity expansion</td><td>Do substitutes exist for the product(s)?</td><td>A. YesB. NoC. Cannot determine</td></tr><tr><td>Buyers and suppliers</td><td>The major product/service is best characterized as:</td><td>A. UndifferentiatedB. DifferentiatedC. Cannot determine</td></tr><tr><td>Industry evolution</td><td>Currently, product innovations are:</td><td>A. RapidB. SlowC. Cannot determine</td></tr><tr><td>Competitive actions</td><td>What is the industry&#x27;s competitive history?</td><td>A. Long history of direct competitionB. Lack of any continual competitionC. Cannot determine</td></tr></table>

The advice is general--its purpose is to surface possible situations, actions, and relationships that may exist or occur within the strategic environment. It is intended to stimulate and facilitate lateral thinking. An example of a question, answer, and resulting piece of fired advice is shown in Table 3. The bold text indicates the inference chain.

An individual interpretation consists of a trace of which folders the user accessed, how he or she answered the questions posed by the system, and the resulting advice fired by the system. The advice from the trace is represented as a set of primitive semantic nets. The representation scheme determines the granularity at which comparisons of interpretations can be made. Figure 4 shows an example representation of part of the emerging industry net. The displayed net is a partial composite of person's PI ... P5 output of their individual knowledge-based session grouped by folder (emerging industry).

The derivation of the semantic net scheme is analogous to developing a content analysis category system. Content analysis is a general procedure for objectively identifying textual material [26]. Similarly, we developed a semantic net scheme, consisting of a set of semantic representations (arcs), from which advice from a knowledge-based system (textual material) could be represented. We followed an adapted version ofHolsti' s guidelines for constructing content analysis categories [23] in developing our semantic net scheme.

Table 3. Example Question, Answer, and Resulting Advice

<table><tr><td>Question</td><td>Answers</td><td>Advice</td></tr><tr><td>Are technological advances made by industry suppliers:</td><td>A. RapidB. SlowC. Cannot determine</td><td>The greater the chance that technological change will make early investments obsolete, the more risky is early entry into a market.WHY? Firms entering later will have the advantage of the newest processes without paying the development costs for early technologies.</td></tr><tr><td colspan="3">Source: [39], p. 233.</td></tr></table>

I. Scheme should reflect purpose of the research. The purpose of the research is to help managers better understand one another's interpretations of their environments through automatic detection of conflicts and overlaps in interpretations. To this extent, the semantic net scheme should allow for a sufficiently complex breakdown of the strategy advice to detect overlaps and conflicts.

2. Scheme should be exhaustive. Each piece of strategy advice in the existing knowledge base should be able to be represented with the semantic net scheme.

3. Scheme should provide mutually exclusive representation. Given the semantic net scheme, no piece of advice from the strategy knowledge base should be able to be represented in more than one way.

4. Scheme should be independent. The conversion of one piece of advice into a particular semantic representation should not affect the conversion of any other piece of advice.

Based on these guidelines, and on an iterative analysis of the current strategy knowledge base, a semantic net scheme was developed. Each representation (arc) between two nodes can be of the following types:

I. IS-A: The lower-level node IS-A higher-level node. For example, economies of scale IS-A entry barrier.

2. IN-A: The lower-level node is IN-A higher-level node. For example, buyers IN-A emerging industry.

3. Describe: The higher-level node is Described by the lower-level node. For example, early entry (higher-level node) is more appropriate (lower-level node).

![](/api/attachments/6AWPRS6J/fulltext/images/695b71d4fbfe4cbfc6803ed34ae4f7d103b81fd568c43faac10160a82138ff29.jpg)

## Figure 4. Advice Net

4. Operate: If the link directly above the higher-level node under consideration is an IN-A relationship, then the higher-level node performs some operation described by the lower-level node. For example, buyers IN-A emerging industry (higher-level nodes) create early market segments (lower-level node).

If the link directly above the higher-level node under consideration is not an IN-A relationship, then the lower-level node is an operation that takes place within the higher-level node. For example, early entry (lower-level node) taking place within an emerging industry (higher-level node).

5. Response: The lower-level node is a Response to the statement generated by all nodes above it. Note that a single response represents one side of a possible conflict that exists in the knowledge base. For example, no (cannot create) is a Response to the statement "buyers in an emerging industry create early market segments?" Note that the statement is built from the nodes above the response node.

6. Effect: The Effect of the operation created by the higher-level nodes results in the lower-level node. For example, adding capacity can have the Effect of overcapacity.

The matrices at the bottom of the figure are interpreted as follows: Advice numbers A5, A6, and A 7 all said that "early entry into an emerging industry is more appropriate" and are thus considered common. Alternatively, advice A8, A17, and AI8 all said that "early entry into an emerging industry is not more appropriate." However, each piece of common advice is derived from a different question/answer pair. For example, advice A5 was the result of the following question/answer pair:

Question: Are purchasers generally brand-loyal in the targeted market segment? Answer: Yes.

Alternatively, advice A6 results from the following question/answer pair:

Question: Can the organizational learning from developing products be protected?

Answer: Yes.

An "X" in the matrix indicates that piece of advice fired for a particular person during his or her individual knowledge-based session. For example, advice A5 fired for persons P I and P3 had, and advice A6 fired for person P2.

While generating an interpretation, the cognitive conflict detector can be used to determine when the interpretation is internally inconsistent. That is, it determines when advice fired by the system contradicts itself.

Upon detection of cognitive conflict, thefocuser can access the question and answer pair(s) that fired the advice under consideration and present the pair(s) to the user. The knowledge updater allows a user to change his or her answer to a question ifhe or she feels that it is necessary. The inference engine can then recompile the "question and answer set" to update the interpretation. The knowledge updater also allows a user to attach context-specific information to a question-and-answer pair during individual interpretation building.

## Interpretation Correlation and Synthesis

Figure 5 shows a detailed flowchart of the interpretation correlation and synthesis process. Interpretations are compared using the interpretation correia tor. Interpretations are of types individual, subgroup, or group and are either previously stored on disk (organizational memory) or currently evolving or evolved. Each type of interpretation can be correlated against one another. The semantic nets are fed into the conflict and commonality knowledge base, which draws inferences on the nets and determines where interpretations conflict and where they are in consensus.

Measures of interpretational overlap and interpretational conflict are computed. Each measure will have an "amount" component and a "strength" component. The "amount" component is a function of the number of pairwise comparisons of conflicting interpretations at each semantic net node. The strength component is a weighted ratio of how much knowledge-based advice is in conflict with the total amount of possible conflict that could occur. The appendix contains these measures along with several necessary definitions.

![](/api/attachments/6AWPRS6J/fulltext/images/398f6fc91dee7d2983239a57d1765844622146f99484946573a9c819db559e6d.jpg)  
Figure 5. Interpretation Correlation and Synthesis

The interpretation prunes the nodes and relationships where there is global consensus and stores them as an evolving global interpretation. When conflict is significant, the alarmer will fire, indicating that the issues of concern should be addressed in a meeting. The hardware configuration of the OLSS for meetings is similar to a traditional GSS. A large screen that will display information for all members to view is controlled by a facilitator. Each group member has a terminal. The purpose of the meeting is to address the conflict detected by the system. Aggregation of the conflict is based on the folder from which the "fired" advice originated. The presentation order of the conflict is determined by the amount and strength of conflict between the knowledge-base-generated interpretations for each folder. Amount of conflict has precedence over strength of conflict--that is, the conflict with the greatest amount will be analyzed first. A sort module generates several files to be used by the OLSS. The folder conflict and commonality files contain an ordered list of folders to be analyzed. The conflict and commonality files contain ordered lists ofthe conflicts and commonalities to be addressed.

![](/api/attachments/6AWPRS6J/fulltext/images/26af84f489756026f4f4025694b70dd703bb43fe2d4b66391be3f96a38599f99.jpg)  
Figure 6. Abstraction of Conflicting Advice

The strategic decision-making group has the option of either a guided or a nonguided session. Using the sorted files discussed above, the guided system session automatically determines the order in which to view the folders and the conflicts and commonalities within the folders. Alternatively, in a nonguided session, the group determines which folder to enter and which conflict or commonality to address. Further, the group must determine whether they wish to enter the conflict or commonality module. For the purpose of this paper, we focus on the system-guided conflict module.

Conflicts are iteratively read from the folder conflict file until none exist. This information is displayed on the large public screen. The purpose of the conflict abstraction is to establish the presence of conflict and to provide an overall context for the individual advice presentation and resulting group discussion, Figure 6 shows an example of a high-level abstraction of conflicting advice. Conflict 2 refers to the second conflict within the active folder. Side A refers to a particular side ofa conflict. In this example, there are only two sides to the conflict, but the system will display multiple sides of conflicts if they exist. The total possible advice value indicates the number of pieces of advice in the complete strategy knowledge base that are consistent with the high-level abstraction statement. In this example, Richard and Greg each had one piece of advice fire that stated that early entry into an emerging industry is less appropriate.

![](/api/attachments/6AWPRS6J/fulltext/images/77f8a6e817f9e4edaa245f098d42361e7e4b89b492b812f1fed41a44ca245b72.jpg)

![](/api/attachments/6AWPRS6J/fulltext/images/84c0cc314f0ec0afbc3e125487569256404dbf3536e10a01509b77e465dfa6f6.jpg)  
Figure 7. Individual Users' Advice  
Top: Greg's Advice. Bottom: Richard's Advice. Opposite page: Rachel's Advice

The actual "fired advice" from the individual manager's interpretation generation sessions are displayed on the individual screens. Figure 7 shows the individual manager's screens. The number preceding the advice is a unique advice identifier that is used by the facilitator to access the question-and-answer pair(s) that caused the conflict.

![](/api/attachments/6AWPRS6J/fulltext/images/4fa64c4623df5a0d5f7218904db5e736bf63abb9add6a237b34dd24c26e99fa4.jpg)  
FIgure 7. Continued

A randomly selected group member was asked to read his or her advice out loud and then discuss the advice in the context of the case being studied. Other group members were encouraged to respond. Once discussion subsided, other conflicting advice was presented and discussed in a similar fashion. Table 4 presents sample dialog benveen OLSS users when presented with the displays shown in figure 7. Note that the occurrence of" ... " indicates that a portion of the dialog has been removed. Dialog was removed to improve clarity and to reduce space requirements. In no way were the "flavor" or "context" of the discussion altered.

Once the group members have discussed the advice-based conflict, the j'ocllser can be used to access the question-and-answer pair(s) that caused the advice-based conflict. Figure 8 shows an example of an OLSS screen of the question(s) that caused the conflict and how each person in the group answered the question. This is displayed by the faci lilator on the large public display. The Question! Answer dialog box contains a question and all the possible responses to the answer. The overlaid "Information" dialog box shows how each group member answered the pertinent question and, if relevant, the resulting advice key. In the example, Richard and Greg answered question 6 with answer 2, which resulted in advice 10. Alternatively, Rachel answered with I, resulting in advice 9. Individual users are prompted to justify their answers to each other.

Table 5 shows sample dialog that took place within the OLSS group after they were shown the screen shown in figure 8.

After discussing the question(s), managers can change their answer(s), using the

Table 4. Sample Dialog from Advice Presentation

GREG: It's a highly technical field, and I think that there would be a strong learning curve. RICHARD: Especially when they're working with technology that a lot of the times it's pioneering technology.

GREG: Leading edge of technology produced by their own Rand D.

RACHEL: I would have to think they're not very easily imitated because it's so technologically advanced.

RICHARD: Isn't there a lot of-Oon't they share their technology pretty openly in thiS industry? ...

GREG: Well, they sometimes eventually share technology, but how rapid the implementation following the leader's position would indicate how easily imitated the learning curve is. How rapid is the rest of the industry following the leader and adapting technological advancements?

RACHEL: I would think, at this point, if AT&T and Northern Telecom are the two companies that are really running neck and neck, it would be important for Northern Telecom to maintain a position, to keep being the one to first introduce technology and do it well. Because if AT&T is able to get a leg up on [Northern Telecom] just in one thing, they may be so close that could Northern Telecom's edge.

GREG: Well, first let me say that I agree with Rachel. From some marketing statements that are mentioned in here, it would support what Rachel just said. RICHARD: Yeah, you and I agree possibly, but if this could go wrong, I mean, if there's a huge learning curve, could AT&T learn from Northern Telecom? I'm not sure if that's possible or not. But if they could, Northern Telecom would make a huge capital investment in something and AT&T would learn from them and do it a lot cheaper a few years later.

GREG: Once it is imitated, are the products coming out of these products; or how the switching incentives or likelihood of switching by the customer to other companies' products, to different vendors, how much loyalty there is and how much switching goes on.

RACHEL: At this point, it may be easier for both [AT&T and Northern Telecom] to pursue, you know, different type of niche markets and have their own learning curves in their own niches, kind of realizing that it's not maybe-maybe it would be a more profitable strategy for them to do that than for them to keep trying to beat each other out on the same technology for the same customers.

knowledge updater. Figure 9 demonstrates this process. In our example, Greg's answer is about to be changed. If the group does not wish to update their answer(s), the next conflict is read and presented from the conflict file. If answers were changed, the interpretation files are updated and the system recompiles the individual interpretations and detects the conflicts and commonalities within the interpretations.

To date, all the base modules and thefocuser and the knowledge updater have been fully implemented. The system has been implemented on IBM compatible PCs. The core of the interpretation generator has been implemented in the EXSYS expert system shell. It has been augmented with batch files and C code to handle the folder fragmentation. The algorithms for contlict and commonality detection and calculating amount and strength measures were all written in C. The/oeuser, knOlv{edge updater, and the remaining parts of the system were written in C++ and Turbo Vision. The OLSS has been pilot-tested (see [22]), and a full empirical study assessing the impact of the OLSS on interpretive organizational learning will be undertaken in the near future.

![](/api/attachments/6AWPRS6J/fulltext/images/91cabbfd2dcd0848dc7256dd44e535da78dcd66ceef5814fcbc03d3aab7145c4.jpg)  
Figure 8. Question and Answers

![](/api/attachments/6AWPRS6J/fulltext/images/e283dc83cb4e8545da79b2945e59a964ea31d8767fb80d1681d89d2047cd7202.jpg)  
Figure 9. Knowledge Updater

RICHARD: Okay. Now, this is, in my mind, for some reasorr-I don't know what makes me think this, and I don't even remember if I read it in here-but I thought that in the telecommunications-type industry, it's very hard to protect your technology. In fact, I thought maybe they even had to share their technology. I don't know why. GREG: Insurance companies share a lot of things. RICHARD: And so that's why I said: Can our position, learning from developing products, be protected? I thought it's pretty common knowledge how they're doing things and it's really hard to keep that from them. I think that I thought regulation is the key reason why it's so open, because of government involvement. RACHEL: That wouldn't surprise me. I think the reason why I tend more towards saying yes is because I thought, well, if it wasn't that protected, kind of getting back, well, wouldn't there be more competitors? Wouldn't it be easier to get in? It wouldn't just be Northern Telecom and AT&T and a bunch of larger ones internationally, but smaller ones in the U.S. market. I thought it seems like it would be more open. But again, if it's-if the information is that readily available, then maybe it's a case where you better have huge economies of scale to even survive because you aren't going to have vfC3i¥ many secrets that your competitors don't know about. FACILITATOR: Okay. All right. Well, based on her discussion, does anybody want to change their answer? RICHARD: I don't think I do.

Table 5. Sample Dialog from Questioni Answer Presentation

GREG: There's a lot of factors, you know, that could affect that that wouldn't-were not disclosed in the case. And I originally answered no because-just because of the high-tech nature of the products and the fact that the products will become available to the competitors who could then, by analyzing the product, extract the learning that went into the development of the high-tech product and, therefore, bypass or shorten the learning curve for themselves. But that might not necessarily be a given, and I think I would tend to switch to NO.3.

RACHEL: I would switch more to 3, too, only because if what Richard said is right, I would definitely-l mean, because of the high level of regulation in the industry, there may be some requirements that they do have to share their technology.

## Initial Results

## Treatments

FOUR DIFFERENT OLSS TREATMENTS WERE TESTED. Two groups of three persons were randomly assigned to each treatment. Groups of this size are consistent with other initial exploratory studies assessing the impact of emerging technologies on groups (e.g., see [15]). Table 6 shows the treatments representing the various levels of technology support. The full OLSS configuration has all the capabilities as described in the previous section. Subjects in the no-OLSS treatment are provided no technology support. Partial<sub>2</sub> OLSS provides support for the generation of individual interpretations but no support for conflict or overlap detection and strategic information presentation (i.e., no technology supported presentation of results from individual knowledge-based sessions). A partial 1 OLSS treatment was included to control for the embedded process of strategic information presentation existing within the full OLSS treatment. Groups within the partial 1 treatment were given a random subset of the advice that fired from their individual knowledge-based sessions, and given the option of using thefoeuser and knowledge updater as described in the previous section. The only difference between partial <sub>l</sub> OLSS and full OLSS is that conflicts and overlaps were not automaticalIy detected and presented to the group members in the partial <sub>l</sub> condition.

Table 6. Levels of Technology Support

<table><tr><td>Treatment</td><td>Individual interpretation generation</td><td>Conflicts generated</td><td>Strategic information presentation</td><td>Reports provided</td></tr><tr><td>Full OLSSn = 2</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Partial1 OLSSn = 2</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Partial2 OLSSn = 2</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>No OLSS n = 2</td><td>No</td><td>No</td><td>No</td><td>No</td></tr></table>

## Methodology

Twelve nighttime M.B.A. students enrolIed in an infonnation systems technology class pilot-tested the OLSS. All subjects individually read a case on Northern Telecom and then participated in the interpretation generation process (i.e., they individually answered questions from the strategy knowledge base). Groups in the full and partial<sub>l</sub> OLSS treatments took part in technology-supported group meetings. Trained facilitators guided the meetings. The facilitators did not offer opinions about the strategic infonnation but rather guided the meeting through the use of the technology. Groups in the full OLSS treatment were presented system-detennined conflicts and used the OLSS capabilities to address the conflicts. Groups in the partial 1 OLSS were presented a random generation of a subset of the advice that fired from their individual knowledge-based sessions. They then used the OLSS technology as described above to address the strategic infonnation. The meetings were videotaped, transcribed, and coded into an equivocality management content analysis scheme. The scheme chosen for this research is adapted from Putnam and Sorenson [41] and is explained in Table 7. The shortest meeting transcript provided a baseline for the amount of coding that was perfonned from the longer meeting transcripts. Two coders were trained and their interrater reliability was assessed. A Cohen's Kappa value of 0.81 was calculated-- this exceeds the recommended guideline ofO.80.

All groups then had a non--technology-supported meeting to perfonn the task of problem, opportunity, and crises identification. Groups in the full, partial 1 ' and $\mathsf { p a r t i a l } _ { 2 }$ treatment levels were provided reports to assist in the task. Full OLSS groups were provided a report that identified all the conflicts and overlaps in the advice fired, along with discrepancies in how questions were answered. Partial 1 OLSS groups reports reflected any updates made during their groups sessions. Partial<sub>2</sub> OLSS groups reports were the trace files from their individual knowledge-based sessions. The identified problems, opportunities, and crises were then matched with a list generated from expert judgments. The expert list was compiled from a review ofthe literature perti nent to the Northern Telecom case. If any portion ofthe subject's identification set matched that of an expert's, then the relationship was recorded for measurement. This approach is consistent with Goul, Shane, and Tonge [19]. All individuals were given a postcase questionnaire.

Table 7. Equivocality Management Scheme (Adapted from [41])

<table><tr><td>Categories</td><td>Explanation</td></tr><tr><td>Decrease equivocality</td><td>Statements that add new information to the discussion that are not explicitly contradictory to previous explicated viewpoints, or, statements that put a new interpretation on previously presented information. For example, “At the time global competitors were entering the switch market, sales growth was increasing in the domestic market but not at an increasing rate,” or, “I interpreted increasing rate of sales growth to mean . . .”</td></tr><tr><td>Maintain equivocality</td><td></td></tr><tr><td>No modification</td><td>Accepts statement without any modification. For example, “Yes, I understand what increasing sales growth means.”</td></tr><tr><td>Seek clarification</td><td>Initiates communication cycle aimed at clarifying statement. For example, “What do you mean by increasing rate of sales growth?”</td></tr><tr><td>Increase equivocality</td><td>Statements that explicitly contradict previous explicated viewpoints or interpretations. For example, “I disagree completely with your interpretation of increasing rate of sales growth.”</td></tr></table>

## Outcomes of System Use

## Equivocality Management

It was evident from the videotape and paper transcripts that the full OLSS groups were more inquisitive and interested in understanding and defending rationale for the way they interpreted and answered system-generated questions than the partial) OLSS groups. The richer, more detailed interaction within the full OLSS groups is reflected in transcript length. Even though the same amount of strategic information was presented to full and partial) OLSS groups, the transcripts for the full OLSS groups were much longer. The full OLSS groups averaged 10,500 words, while the partial) OLSS groups averaged 6,000 words.

The previous observations are further supported by the content analysis of the transcripts, summarized in figure 10. There was essentially no difference between the within-treatment summed means across the two maintain equivocality categories, yet the analysis at the individual category level provided large differences. While both sets of groups verbalized an equal percentage of utterances that maintained equivocality, groups within the full OLSS had a much higher percentage of utterances that "sought clarification" and a much lower percentage of utterances coded as "no modification." This is consistent with work by Mason and Mitroff [32], and Schweiger, Sandberg, and Rechner [46], who found that the use of conflict-based decisionmaking approaches yielded richer interaction than traditional consensus-based methods.

![](/api/attachments/6AWPRS6J/fulltext/images/1aeb090e75192b5fb5ac7a2a53577fdbae8c2db795508dcbe440fea8b14c62d0.jpg)  
Figure 10. Results of Content Analysis

Research by Valacich and Schwenk [56] found that different problem-solving processes were invoked for devil's advocacy, dialectical inquiry, and expert-based approaches. Specifically, they suggest devil's advocacy groups were more focused on questioning the strengths of an alternative because they may have felt a greater need to develop a viable solution than groups in using the other approaches. A similar effect may be present in this study. Because the full OLSS groups were presented conflicts, they may have felt a need to reduce or eliminate the conflict and thus put more effort toward understanding each other's opinions and assumptions.

## Problem, Opportunity, and Crises Identification

The use of expert-advice-based reports in identifying problems, opportunities, and crises proved inconclusive. Most people found the advice in the reports believable but not helpful in performing the task. There were no distinct differences in the number of problems, opportunities, and crises identified by the various groups. From verbal discussions with participants, there were indications that it was too time-consuming to extrapolate and apply the broad strategy advice to the Northern Telecom case.

Several people also indicated that there was too much advice and some of it was not relevant, indicating that the strategy knowledge may need to be filtered at a lower level of granularity. This can be accomplished by partitioning the knowledge base into more folders and adding more rules to the diagnostic questions folder.

Goul, Shane, and Tonge [19] used problem, opportunity, and crises identification to assess individual (not group) differences in environmental understanding. They found that individuals who had access to knowledge-based advice reports identified significantly more problems than individuals who did not have access to the reports. It may be that the effect size attributed to the presence of the knowledge base found in the Goul, Shane, and Tonge study-and best isolated and captured within the partial OLSS treatment level, but also incorporated within full and partial, OLSS treatment levels in this study-was nullified by the change in the size of the experimental unit. That is, the effect on problem identification due to using a group of three, rather than an individual, outweighs the effect of the presence of the knowledge base.

## Summary ofOLSS Use

Results from the postcase questionnaire indicated that almost all individuals using the OLSS technology to support their meetings found that (I) presentation of expert advice stimulated discussion that insight into the case, (2) presentation of question/answer pairs stimulated discussion that added insight into the case, (3) being placed in conflict with other group members stimulated discussion that added insight into the case, and (4) the group technology experience was positive. In an open-ended comment section at the end of the questionnaire, several users stated that the OLSS technology helped them consider several different environmental factors that would otherwise have been overlooked.

It appears promising that the automatic detection of conflicts will facilitate/stimulate richer and more meaningful group interaction than a more passive approach of Just presenting topical information for discussion. Further, the fact that the conflict is presented to groups objectively and in a common grammar by an automated computer system may reduce some of the dysfunctional interaction that can occur when group conflict is personal and emotional [57]. While the use of the OLSS did not translate into tangible differences in task performance for the various groups, there are several areas related to the knowledge base design and content that can be modified. These issues are addressed in the following section.

## Conclusions, Limitations, and Future Research

THIS RESEARCH IS AN INITIAL ATTEMPT AT OPERATIONALIZING basic interpretive learning concepts within an intelligent IT-based environment. It has accomplished this by (1) detailing a methodology for designing and developing a knowledge-based OLSS, (2) developing an OLSS with the aforementioned methodology, and (3) pilot testing the OLSS. The design and development effort is a fundamental and necessary step toward a research platform to study the appropriateness and effectiveness of IT on interpretive organizational learning. This research has also extended the application of knowledge-based systems in strategic management to the group paradigm.

While the OLSS appeared to stimulate discussion and interaction among participants, the current OLSS prototype has several limitations. First, the overall impact and usefulness of the system is dependent on the content and structure of the current strategy knowledge base. While the current knowledge base is very broad (offers advice on a variety of topics), it is not very deep (rules are generally based on a single question/answer pair rather than on a combination of several question/answer pairs). The result is that a large number of individual inference chains and very few complex inference chains are generated during an individual user's knowledge-based session. Since one of the major contributions of the application of innovative technology to complex problems is that the technology can assist in overcoming the cognitive limitations of participants, multiple knowledge bases of varying complexities should be tested. Further, the major complaints about the system were related to the content of the system, not to the structure or process enforced by the OLSS. Some participants found the "grammar" of the advice (Porter) hard to understand and also found it hard to apply to the Northern Telecom case. It is thus recommended that the system be manually tested with paper-and-pencil sessions very early in the design ofthe semantic nets. Further, if possible, the process should be applied to mUltiple cases. This will ensure that grammar issues are ironed out and abstractions of the advice can be adjusted so that they are sufficiently "semantically close" to the cases to which they will be applied.

The prototype is currently limited to the analysis and diagnosis phase of strategic management. Future efforts will be directed toward supporting the choice phase along with testing knowledge bases of different domains. The current prototype does not provide an easy mechanism for dynamic recompilation of updated interpretations and automated redetection of conflicts and overlaps. In the initial test of the OLSS, conflicts and overlaps were detected and participants used the OLSS to address the conflicts. However, it may take several iterations of conflict and overlap detection and OLSS use to address the conflicts before managers' interpretations stabilize.

To date, limited testing of the prototype has been undertaken. Until a rigorous empirical study is performed, no concrete conclusions can be made about the overall effectiveness of the OLSS. Currently, our efforts are directed toward a full empirical study of the effects of the OLSS on interpretive organizational learning. If the tool proves effective under more rigorous testing, the question of managerial practicality must be addressed. Will managers find the OLSS useful in assessing their environment? This question cannot be answered until field tests are performed. Further evaluation of the OLSS as an educational tool in support of case analysis in both face-to-face and distributed meetings is required.

Many issues remain unresolved and many opportunities exist for conceptual and physical extensions to the OLSS. An overriding goal of flexibility and modularity has guided the work to date and will continue to be a primary concern. That is, our goal is to continue the development ofa flexible testbed to study interpretive organizational learning.

An evaluation of the impact of variables such as team composition and structure, group size, team history, and coordination metaphors on interpretive organizational learning wilI need to be performed. The effects of dynamicalIy restructuring the individual and emerging group interpretations during OLSS meetings still needs to be addressed and explored. Further use and experimentation of the organizational memory component are required. Potential topics of exploration using the organizational memory component include:

J. Tracing the temporal shifts of individual, group, and organizational interpretations.

2. Performing hindsight evaluation of interpretations. Areas where an organization is consistently misinterpreting could be identified and addressed. Areas of misinterpretation and correct interpretation could be traced to individual managers, subgroups and groups. This capability could be used in a training capacity in simulated environments and/or for tracing actual interpretation alignment.

3. Intelligent interpretation agents could be developed and stored in memory. The effect of different role-playing agents could be assessed. For example, agents that consistently conflict with managers' interpretations (devil' s advocate), and agents who change their opinions randomly (space cadet), agents who always agree with managers' interpretations (rubber stamp) could be developed. Research in active DSS can add insight into potential "agent personalities."

Further efforts wilJ be initiated to add a graphical cognitive mapping layer on top of the current system. Conflicts can then be represented visually rather than textually, and holistic views of the interpretations will be available for viewing.

While interpretive organizational learning has been identified as an increasingly significant issue to be addressed by IT research, few systems have been designed and developed to support the interpretive organizational learning process. To further synthesize IT and interpretive organizational learning, the design, development, and validation of exploratory and experimental systems, such as the one described in this paper, are critical. Because strategic environments are becoming increasingly dynamic and volatile, it is more critical than ever for organizations to interpret their environment correctly if they wish to remain competitive. It is our belief that organizational tools such as the OLSS wilJ become common in future knowledge-based organizations.

## REFERENCES

1. Bedeian, A.G. Contemporary challenges in the study of organizations. Journal of Management, 12, 2, (1986), 195-201.

2. Bougon, M.G. Congregate cognitive maps: a unified dynamic theory of organization and strategy. Journal of Management Studies, 29, 3, (1992), 369--389.

3. Bougon, M.G.; Weick, K.E.; and Binkhorst, D. Cognition in organizations: an analysis of the Utrecht Jazz Orchestra. Administrative Science Quarterly, 22,4 (1977),606-639.

4. Boynton, A.C., and Zmud, R.W. Information technology planning in the 1990s: directions for practice and research. MIS Quarterly, 11, I (1987), 59--71.

5. Brancheau, J.C., and Wetherbe, J.c. Key issues in information systems management. MIS Quarterly, 11, I (1987),23-45.

6. Carlson, D.A. Cognitive models of strategic management. Proceedings of the Twenty-Sixth Annual Hawaii International Conference on Systems Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1993, pp. 282-29 \.

7. Daft, R.L., and Huber, G.P. How organizations learn: a communication framework. Research in the Sociology of Organizations, 5 (1987), 1-36.

8. Day, D.V., and Lord, R.G. Expertise and problem categorization: the role of expert processing in organizational sense-making. Journal of Management Studies, 29, I (1992), 35-47.

9. Dickson, G.W.; Leitheiser, R.L.; and Wetherbe, J.C. Key information systems issues for the 1980s. MIS Quarterly, 8, 3 (1984),135-159.

10. Dutton, J.E., and Jackson, S.E. Categorizing strategic issues: links to organizational action. Academy of Management Review, 12, I (1987), 76-90.

II. Eden, C., and Ackermann, F. Strategic options development and analysis (SODA)-- using a computer to help with the management of strategic vision. In G. Doukidis, F. Land, and G. Miller (eds.), Knowledge-Based Management Support System. Chichester, UK: Ellis Horwood, 1989, pp. 198-207.

12. Fahey, L., and Narayanan, V. Linking changes in revealed causal maps and environmental change: an empirical study. Journal of Management Studies, 26,4 (1989), 361-377.

13. Fiol, C.M., and Lyles, M.A. Organizational learning. Academy of Management Review, 10, 4 (1985), 803-8 \3.

14. Ford, J.D., and Hegarty, W.H. Decision makers' beliefs about the causes and effects of structure: an exploratory study. Academy of Management Journal, 27,2 (1984), 271-29\.

15. Gallupe, R.B.; DeSanctis, G.; and Dickson, G.W. Computer-based support for group problem-finding: an experimental investigation. MIS Quarterly, 12, 2 (1988), 277-296.

16. Ginsberg, A. Connecting diversification to performance: a sociocognitive approach. Academy of Management Review, 15,3 (1990), 514-535.

17. Glueck, W.F. Business Policy and Strategic Management. New York: McGraw-Hill, 1980.

18. Goul, K.M.; Philippakis, A.; Richards, S.; Sandman, T.; and Schamp, A. Project CoEx: a distributed artificial intelligence orientation to the design of a cooperating experts' electronic meeting system. Proceedings of the Twenty- Third Annual Hawaii International Conference on Systems Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1990, pp. 130-140.

19. Goul, K.M.; Shane, B.; and Tonge, F.M. Using a knowledge-based decision support system in strategic planning decisions: an empirical study. Journal of Management Information Systems, 2, 4 (1986), 70-84.

20. Hambrick, D.C. Some tests of the effectiveness and functional attributes of Miles and Snow's strategic types. Academy of Management Journal, 26, I (1983), 5-26.

21. Henderson, J.C. Finding synergy between DSS and expert systems research. Decision Sciences, 19,3 (1987), 333-349.

22. Hine, M.J. The design, development and validation of knowledge-based organizational learning support system. Ph.D. dissertation, Arizona State University, 1993.

23. Holsti, O.R. Content Analysis for the Social Sciences and Humanities. Reading, MA: Addison-Wesley, 1969.

24. Huber, G. Organizational learning: the contributing processes and the literatures. Organization Science, 2, I (1991),88-115.

25. Isabella, L.A. Evolving interpretations as a change unfolds: how managers construe key organizational events. Academy of Management Journal, 33, I (1991), 7-4 \.

26. Jones, R.A. Research Methods in the Social and Behavioral Sciences. Sunderland, MA: Sinauer Associates, 1985.

27. Kersten, G.E.; Michalowski, W.; Szpakowicz, S.; and Koperczak, Z. Restructurable representations of negotiation. Management Science, 37, \0 (1991), 1269-1290.

28. Langfield-Smith, K. Exploring the need for a shared cognitive map. Journal ofManagement Studies, 29, 3 (1992), 349-367.

29. Lee, S.; Courtney, J.F., Jr.; and O'Keefe, R.M. A system for organizational learning using cognitive maps. Omega, 20, I (1992),23-36.

30. Lurigio, A.J., and Carrol, J.S. Probation officers' schemata of offenders: content, development and impact of treatment decisions. Journal of Personality and Social Psychology, 48, 5 (1985),1112-1126.

31. Lyles, M.A., and Schwenk, C.R. Top management, strategy and organizational knowledge structures. Journal of Management Studies, 29, 2 (1992), 155-174.

32. Mason, R.O., and Mitroff, 1. Challenging Strategic Planning Assumptions. Reading, MA: Addison-Wesley, 1981.

33. McGrath, J. GROUPS Interaction and Performance. Englewood Cliffs, NJ: Prentice-Hall, 1984.

34. Merwin, J. The limits of tradition. Forbes, 135, II (1985), 112-115.

35. Milliken, FJ. Perceiving and interpreting environmental change: an examination of college administrators' interpretation of changing demographics. Academy of Management Journal, 33, I (1 990), 42\~3.

36. Miranda, S.M., and Bostrom, R.P. The impact of group support systems on group conflict and conflict management. Journal of Management Information Systems, 10, 3 (1993),63-95.

37. Niederman, F.; Brancheau, lC.; and Wetherbe, J.C. Information systems management issues for the I 990s. MIS Quarterly, 15,4 (1991),475-500.

38. Poole, M.S.; Holmes, M.; and DeSanctis, G. Conflict management in a computersupported meeting environment. Management Science, 37, 8 (1991), 926-953.

39. Porter, M.E. Competitive Strategy. New York: Free Press, 1980.

40. Pracht, W.E. GISMO: a visual problem-structuring and knowledge-organization tool. IEEE Transactions on Systems, Man, and Cybernetics, SMC-16, 2 (1986),265-270.

41. Putnam, L.L., and Sorenson, R.L. Equivocal messages in organizations. Human Communication Research, 8, 2 (1982), 114-132.

42. Ramaprasad, A., and Poon, E. A computerized interactive technique for mapping influence diagrams (MIND). Strategic Management Journal, 6,4 (1985), 377-392.

43. Rockart, IF., and DeLong, D.W. Executive Support Systems: The Emergence of Top Management Computer Use. Homewood, IL: Dow Jones-Irwin, 1988.

44. Sambamurthy, V., and Poole, M.S. The effects of variations in capabilities of GDSS designs on management of cognitive conflict in groups. Information Systems Research, 3, 3 (1992),224-251.

45. Schweiger, D.M., and Sandberg, W.R. The utilization of individual capabilities in group approaches to strategic decision-making. Strategic Management Journal, 10, I (1989), 31--43.

46. Schweiger, D.M.; Sandberg, W.R.; and Rechner, P.L. Experiential effects of dialectical inquiry, devil's advocacy and consensus approaches to strategic decision making. Academy of Management Journal, 32,4 (1989), 745-772.

47. Schwenk, C.R. Effects of devil's advocacy and dialectical inquiry on decision making: a meta-analysis. Organizational Behavior and Human Decision Processes, 47, I (1990), 161-175.

48. Sengupta, K., and Te'eni, D. Cognitive feedback in GDSS: improving control and convergence. MIS Quarterly, 17, I (1993),87-109.

49. Shakun, M.F. Evolutionary Systems Design: Policy Making under Complexity and Group Decision Support Systems. Oakland, CA: Holden-Day, 1988.

50. Shakun, M.F. Airline buyout: evolutionary systems design and problem restructuring in group decision and negotiation. Management Science, 37, 10 (1991), 1291-1303.

51. Spillman, 8.; Bezdek, J; and Spillman, R. Development of an instrument for the dynamic measurement of consensus. Communication Monographs, 46, I (1979), 1-12.

52. Stabell, C.B. A decision-oriented approach to building DSS. In l L. Bennet (ed.), Building Decision Support Systems. Reading, MA: Addison-Wesley, 1983, pp. 25--42.

53. Starbuck, W.H. Organizations as action generators. American Sociological Review, 48, 1(1983),91-\02.

54. Sycara, K.P. Problem restructuring in negotiation. Management Science, 37, 10 (1991), 1248-1268.

55. Tuckman, B. Personality, structure, group composition, and group functioning. SocIOmetry, 27, 4 (1964), 469--487.

56. Valacich, J.S., and Schwenk, C. Devil's advocacy and dialectical inquiry effects on face-to-face and computer-mediated group decision making. Organizational Behavior and

Human Decision Processes, 63,2 (1995), 158-171.

57. Valacich, l.S., and Schwenk, C. Structuring conflict in individual, face-to-face, and computer-mediated group decision making: carping versus objective devil's advocacy. Decision Sciences, 26, 3 (1995), 369-393.

58. Vandenbosch, B., and Higgins, C. Executive support systems and learning: a model and empirical test. Journal of Management Information Systems, 12, 2 (1995), 99-130.

59. Watson, R.T.; DeSanctis, G.; and Poole, M.S. Using a GDSS to facilitate group consensus: some intended and unintended consequences. MIS Quarterly, 12,3 (1988),463--477.

60. Weick, K.E. The Social Psychology of Organizing. Reading, MA: Addison-Wesley, 1979.

61. Weick, K.E., and Bougon, M.G. Organizations as cognitive maps: charting ways to success and failure. In H. Sims and D. Gioia (eds.), The Thinking Organization: Dynamics of Organizational Cognition. San Francisco, CA: Jossey-Bass, 1986, pp. 103-135.

62. Zhang, W.R.; Chen, S.S.; and Bezdek, J.c. Pool2: a generic system for cognitive map development and decision analysis. IEEE Transactions on Systems, Man, and Cybernetics, 19, I (1989),31-39.

## ApPENDIX

## Definitions

## PLEASE REFER TO FIGURE A.I.

A particular piece of advice is "attached" to a node if it is represented by that node and its precluded branch. For example, the advice A5 and A6 are attached to the node "yes" in the (yes; early entry; more appropriate) branch.

A piece of advice is "attached" to a particular person if the advice resulted from his or her knowledge-based session. For example, advice A5 is "attached" to persons PI and P3, and advice A6 is "attached" to person P2.

A person is "attached" to a particular node ifhe or she had advice "attached" to that particular node. For example, persons PI, P2, and P3 are "attached" to the "yes" node in the (yes; early entry; more appropriate) branch, while persons P4 and P5 are "attached" to the "no" node in the (no; early entry; more appropriate) branch.

The nomenclature for the overlap and conflict measures consists of two major types: operators and units of analyses. An operator performs a certain function upon the designated unit of analyses.

operator (unit of analysis) = op(ua);

op= {NA; NP}

NA(ua): the number of pieces of non-mutually exclusive advice "attached" to a particular unit of analysis. Pieces of advice are not mutuaIly exclusive if different questions are part of the inference chain that caused the advice to fire. For example, in figure A.I, advice A5, A6, and A 7 are the result of answering the same question differently. Thus, they are mutually exclusive, and no one person can have more than one of those pieces of advice fire at a given point in time. Therefore, in figure A.I, NA (side I of conflict 2) equals I because the maximum number of pieces of advice fired for any one person at a given point of time for side I of conflict 2 is I.

![](/api/attachments/6AWPRS6J/fulltext/images/a29456f8c857e58cd6f754d9f927cd5c550401e9c0cca0bf4f40eb09b7d2d813.jpg)  
Figure A.I. Advice Net with Nomenclature

NP(ua): the number of persons attached to a particular unit of analysis

$$
u a \neq N _ {i, t} \quad u a \neq C o n _ {j, v, t _ {v}};
$$

$$
u a = \{N _ {i}; N _ {i t}; C o n _ {j}; C o n _ {j, v}; C o n _ {j, v, t _ {v}};
$$

$N _ { i } .$ a node $" \vec { \imath } ^ { \ " }$ in the knowledge base trees that has advice attached to it; i varies from I to $r ;$

$N _ { i , i } .$ a person $" t "$ attached to a node "i," t varies from I to p where $p = N P ( N _ { i } )$

Coni parent node of conflict $" \vec { \jmath } ^ { 3 }$ in knowledge base tree;} varies from I to $s ;$

$C o n _ { j , \nu } \mathrm { ; }$ one side "v" of conflict $" j " ;$ v varies from I to z; $C o n _ { j , \nu } \subseteq N _ { i } ;$

$C o n _ { j , \nu , t _ { \nu } }$ : a person $" t _ { \nu } "$ attached to one side "v" of conflict $\cdots ; v \colon ; t _ { v }$ varies from I to m

where $m = N P ( C o n _ { j , \nu } ) ;$

$C o n _ { j , x , t _ { x } ^ { \ast } }$ a person $" t _ { x } "$ attached to one side $" x "$ of conflict "j." Note that side $\ " x \ "$ is thus in conflict with side $" \nu _ { \cdot } \ ' _ { t _ { x } }$ varies from 1 to n where $n = N P ( C o n _ { j , ~ x } )$

ov: the number of nodes in the knowledge base tree where overlap exists between group members; $o \nu \Leftarrow r$

$^ { c : }$ the number of nodes in the knowledge base tree where conflict exists between group members; $c \Leftarrow s$

## Conflict and Overlap Measures

Recall that overlap and conflict are comprised of an amount component and a strength component. The amount component is derived from the number of persons in agreement or in conflict. The amount of overlap for a group of persons is directly comparable to the amount of overlap for another group, assuming group sizes are the same. Similarly, amount measures for conflict are directly comparable. However, the amount of overlap for a group is not directly comparable to amount of conflict for the same or different groups because the overlap and conflict measures are based on different scales. The strength component is derived from weighted combinations of amounts of knowledge base advice attached to persons and nodes.

Overlap Measures

Amount of Overlap for a Particular $N _ { i } .$

$$
\frac {N P (N _ {i}) \times (N P (N _ {i}) - 1)}{2}.
$$

For the example in figure A.I, the amount of overlap for $N _ { 3 }$ is 3. Amount of Overlap for Complete Interpretation:

$$
\sum_ {i = 0} ^ {o v} \frac {N P (N _ {i}) \times (N P (N _ {i}) - 1)}{2}
$$

For the example in figure A.I, this measure is 4.

Strength of Overlap for a Particular $N _ { i } .$

$$
\sum_ {t = 1} ^ {n} \left[ \frac {1}{N P (N _ {i})} \times \left[ \frac {N A (N _ {i , t}}{N A (N _ {i})} \right] \right] = \frac {1}{p} \sum_ {t = 1} ^ {n} \frac {N A (N _ {i , t}}{N A (N _ {i})} = \frac {1}{p} \times \frac {1}{N A (N _ {i})} \sum_ {t = 1} ^ {n} N A (N _ {i, t}).
$$

For the example in figure A.I, the strength of overlap for $N _ { 3 }$ would be I.

Strength of Overlap for Complete Interpretation:

$$
\frac {1}{o v} \sum_ {i - 1} ^ {o v} \sum_ {t = 1} ^ {n} \left[ \frac {1}{N p (N _ {i})} \times \left[ \frac {N A (N _ {i , t}}{N A (N _ {i})} \right] \right].
$$

For the example in figure A.I, this measure would be 11112.

Conflict Measures

Amount for a Particular Conflict:

$$
\sum_ {v = 1} ^ {z - 1} \sum_ {x = v +} ^ {z} \left[ N P \left(C o n _ {j, v}\right) \times N P \left(C o n _ {j, x}\right) \right].
$$

For the example in figure A.I, the amount measure for conflict number two is 6.

Amount of Conflict for a Complete Interpretation:

$$
\sum_ {j = 1} ^ {s} \sum_ {v = 1} ^ {z - 1} \sum_ {x = v + 1} ^ {z} \left[ N P \left(C o n _ {j, v}\right) \times N P \left(C o n _ {j, x}\right) \right].
$$

For the example in figure A.I, this measure is also 6 since only one conflict is presented.

Strength of Conflict for a Particular $C o n _ { j }$

$$
\sum_ {v = 1} ^ {z - 1} \sum_ {x = v + 1} ^ {z} \sum_ {t _ {v} = 1} ^ {m} \sum_ {t _ {x} = 1} ^ {n} \left[ \frac {1}{N P (C o n _ {j , v}) \times N P (C o n _ {j , x})} \times \left[ \frac {N A (C o n _ {j , , v , t _ {v}}) \times N A (C o n j , x , t _ {v})}{N A (C o n _ {j , v}) \times N A (C o n _ {j , x})} \right] \right].
$$

For the example in figure A.I, this measure is $5 / 6$

Strength of Conflict for a Complete Interpretation:

$$
\frac {1}{C} \sum_ {j = 1} ^ {c} \sum_ {v = 1} ^ {z - 1} \sum_ {x = v + 1} ^ {z} \sum_ {t _ {v} = 1} ^ {m} \sum_ {t _ {x} = 1} ^ {n} \left[ \frac {1}{N P (C o n _ {j , v}) \times N P (C o n _ {j , x})} \times \left[ \frac {N A (C o n _ {j , v , t _ {v}}) \times N A (C o n j , x , t _ {v})}{N A (C o n _ {j , v}) \times N A (C o n _ {j , x})} \right] \right].
$$

For the example in figure A.I, this measure is also 5/6 since there only one conflict is presented.
