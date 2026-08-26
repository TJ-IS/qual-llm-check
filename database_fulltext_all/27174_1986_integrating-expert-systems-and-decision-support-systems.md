---
otero_id: 27174
otero_key: "5HN9BY8M"
title: "Integrating Expert Systems and Decision Support Systems"
authors: "Efraim Turban; Paul R. Watkins"
year: "1986"
journal: "MIS Quarterly"
doi: "10.2307/249031"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Integrating Expert Systems and Decision Support Systems
Author(s): Efraim Turban and Paul R. Watkins
Source: MIS Quarterly, Vol. 10, No. 2 (Jun., 1986), pp. 121-136
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249031
Accessed: 08-01-2016 17:59 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Integrating Expert Systems and Decision Support Systems

By: Efraim Turban
Paul R. Watkins
University of Southern California
Los Angeles, California

## Abstract

Expert systems are emerging as a powerful tool for decision making. Integrating expert systems with decision support systems may enhance the quality and efficiency of both computerized systems. This article examines possible connections between the two technologies and discusses some issues related to their integration.

Keywords: Expert systems, decision support systems, artificial intelligence, database, natural language processors, interactive
ACM Categories: H.4.2, I.2.0

## Introduction

Expert systems represent one of the most exciting new developments in information technology. Emerging as a practical application of research in artificial intelligence (AI), expert systems combine knowledge of a particular application area with an inference capability, to enable the system to reach a level of decision making performance comparable to (or even exceeding) that of human experts in some specialized areas.

From applications in medical diagnosis, mineral exploration, and the configuration of computer hardware, expert systems (ES) are beginning to extend into business applications (e.g., [18, 28]). Prototype systems are now in use around the world. Major efforts are underway in industry, government, and science to exploit AI technology for practical use.

Although ES should be regarded as being in an embryonic phase, reports of successful commercial applications are increasing. The evolving ES industry, with several dozen competing companies, is projected to become a multi-billion dollar market before the end of the decade. $^{1}$

One of the most interesting questions underlying this development is how to integrate ES programs into an existing (or evolving) management information system, and specifically into a decision support system (DSS), in order to create even more powerful and useful computer-based systems.

The objective of this article is to describe and discuss some issues of DSS/ES integration. Attaining this goal will be difficult for the following reasons. First, there is no consensus on what an ES is, and what constitutes a DSS [8]. Second, there are varying opinions regarding the potential for integration of these technologies. This paper will summarize the current state of DSS/ES integration, and present two frameworks for integration: ES integration into the conventional DSS components, and ES as an additional component of DSS. Technical, behavioral and design issues of the integration will also be discussed.

## Is an Expert System a Decision Support System?

A DSS is an interactive, computer-based information system that utilizes decision rules and models, coupled with a comprehensive database. In comparison, an ES is a computer program that includes a knowledge base containing an expert's knowledge for a particular problem domain, and a reasoning mechanism for propagating inferences over the knowledge base. In addition, an ES contains an explanation and justification mechanism which provides the user of the ES with some detail of the reasoning process.

Most existing expert systems are being used as independent computerized systems, advising users on a specific problem area. As such, they are considered by many to be intelligent DSSs (e.g., [6]). Further, ESs nicely fit the generic DSS framework, as developed by Bonczek, et al., [4]. According to this framework, DSSs exhibit three major characteristics, all of which are present in ES. First, DSS aids a decision maker in solving unstructured (or semistructured) problems. Second, it possesses an interactive query facility. Finally, it uses an English-like dialogue language.

Additional support for this point of view can be found in Alter's [1] classification of DSS's into six major categories:

1. Retrieving a single item of information.

2. Providing a mechanism for ad hoc data analysis.

3. Providing prespecified aggregation of data in the form of reports.

4. Estimating the consequences of proposed decisions.

5. Proposing decisions.

6. Making decisions.

In contrast to this view of ES as an intelligent DSS, one can cite several fundamental differences between the two. Table 1 summarizes what we envision as the major differences between DSS and ES.

Specifically, the objectives of the system are different. The DSS supports the human who makes decisions; the ES operates as an advisor. DSS provides, in many cases, institutional support (e.g., when it is used for supporting long range planning), while ES acts as an advisor to an individual (or a group) in a narrow area.

The problem area attacked by DSS is broad and complex, while at least in the short run, ES is restricted to a much more structured and narrow domain. As a result, DSS is more suitable for dealing with ad hoc and unique situations, while ES is more suitable for providing advice on repetitive problem areas (such as diagnosis of malfunctions).

The database of DSS contains facts while its counterpart in ES, the knowledge base, contains, in addition to facts, also procedures for how to solve problems. ES, by definition, exhibits reasoning capability (e.g., deduction); while this capability is still limited, it is slowly being improved. DSS does not possess such a capability at all. Finally, some DSS provide limited explanation capabilities (e.g., how a solution is derived); ES, on the other hand, can also explain why a certain solution is recommended. Thus, ES has more powerful explanatory capabilities.

Additionally, ES typically involves a closed-system assumption, that is, the problem domain is circumscribed and the system's functions are confined to boundaries. In DSS contexts, the world is open. A DSS must be flexible and adaptive to meet the changing conditions in the environment and the evolving needs of the user [24].

The point to be made here is that even if an ES can be qualified as a DSS, it is certainly a special class of DSS with unique characteristics. Therefore, an ES can be a candidate for integration with a “traditional” DSS.

## The Logic and Benefits of the Integration

Most existing ES and DSS are not integrated. ES operate as independent expert consultation systems while DSS operate as support devices to decision makers. However, this situation is beginning to change. There is evidence (some of which will be presented later) that DSS/ES integrated systems are being developed and implemented at an increasing rate.

<table><tr><td>Attributes</td><td>DSS</td><td>ES</td></tr><tr><td>Objectives</td><td>Assist human decision maker</td><td>Replicate a human advisor and replace him/her</td></tr><tr><td>Who makes the recommendations (decisions)?</td><td>The human and/or the system</td><td>The system</td></tr><tr><td>Major orientation</td><td>Decision making</td><td>Transfer of expertise (human-machine-human) and rendering of advice</td></tr><tr><td>Major query direction</td><td>Human queries the machine</td><td>Machine queries the human</td></tr><tr><td>Nature of support</td><td>Personal, groups, and institutional</td><td>Personal and groups</td></tr><tr><td>Data manipulation method</td><td>Numerical</td><td>Symbolic</td></tr><tr><td>Characteristics of problem area</td><td>Complex, broad</td><td>Narrow domain</td></tr><tr><td>Type of problems treated</td><td>Ad-hoc, unique</td><td>Repetitive</td></tr><tr><td>Content of Database</td><td>Factual knowledge</td><td>Procedural and factual knowledge</td></tr><tr><td>Reasoning capability</td><td>No</td><td>Yes, limited</td></tr><tr><td>Explanation capability</td><td>Limited</td><td>Yes</td></tr></table>

Table 1. Differences Between ES and DSS

The benefits of the DSS/ES integration can be realized along several dimensions: ES contribution, DSS contribution, and the synergetic resulting from the DSS/ES combination. These benefits are summarized in Table 2, according to four specific areas: database, models, interfaces, and overall capabilities. The table also refers to research done in each area. Note that the benefits can be further classified into those that are achieved during the development of the systems vs. those achieved during the system's operation.

## The Synergy Between DSS and ES

In certain problem domains both ES and DSS may have distinct advantages that, when combined, can yield synergetic results. DSS typically gives full control to the decision maker regarding information acquisition, information evaluation, and the final decision. As research has shown, human judgemental biases may be present in complex decisions that are supported by a DSS (for a comprehensive review, see [13]). An ES, on the other hand, is free from acquisition, evaluation and judgemental biases, at least in the human sense (if the knowledge of the expert(s) is properly represented in the ES and if the ES is properly designed). The ES would serve to provide intelligence for a particular domain and would make a tentative decision. The decision maker could also utilize the DSS in the traditional sense and arrive at a tentative decision. The results of the ES and DSS could then be reconciled and evaluated, with a likelihood that the joint effort could produce better results than either approach independently. This approach is not necessarily constrained by the narrowness of the domain of the ES, since an operational DSS can also be domain specific, for example, DSS for routing vehicles in a textile company, or DSS for determining the allocation of IBM customer engineers to geographic territories.

<table><tr><td></td><td>ES Contribution</td><td>DSS Contribution</td></tr><tr><td>Database and Database Management Systems (DBMS)</td><td>Improves construction, operation and maintenance of DBMS [14]Improves accessibility to large databasesImproves DBMS capabilities [14]Permits symbolic representation of data</td><td>Database provides to ES [14]</td></tr><tr><td>Models and Model base Management System</td><td>Improves model management [2]Helps in selecting models [9, 10]Provides judgemental elements to modelsImproves sensitivity analysis [9]Generates alternative solutions [19]Provides heuristics [12]Simplifies building simulation modelsMakes the problem structure incrementally modifiableSpeeds up trial-and-error simulation</td><td>Provides initial problem structure [15]Provides standard models and computationsProvides facts (data) to modelsStores specialized models constructed by experts in the model base</td></tr><tr><td>Interface</td><td>Enables friendlier interface [11, 14, 27]Provides explanations [15]Provides terms familiar to user [12, 15]Acts as a tutor [9]Provides interactive, dynamic, visual problem solving capability [3]</td><td>Provide presentations to match individual cognitive styles</td></tr><tr><td>System Capabilities (Synergy)</td><td>Provides intelligent advice (faster and cheaper than human) to the DSS or its user [20]Adds explanation capability [12]Expands computerization of the decision making process [9, 17]</td><td>Provides experience in data collectionProvides experience in implementation [12]Provides individualized advice to users to match their decision styles</td></tr></table>

Table 2: Summary of Integration Benefits

While typical DSS support quantitative, mathematical, and computational reasoning, DSS should also be developed to support qualitative analysis based on methodologies such as analogical reasoning, pattern recognition, and content analysis. ES are particularly well suited for these types of methodologies, and thus may provide an important link to the DSS for providing more balance in supporting various types of decision processes.

## ES Integration Into DSS Components

A DSS is composed of four basic components: a database, a model base, an interface and a user. Theoretically, one can add an ES (or several ES) to each component. The proposed integration diagrammed in Figure 1 is usually considered a one way integration; in other words, the ES supports the DSS. However, this connection can sometimes work in reverse.

![](/api/attachments/5HN9BY8M/fulltext/images/c6cc807c3cb2e3be29d9d71f0db0f068d75a35303d8adb24d4a1a9ae53fecf3a.jpg)  
Figure 1. Integration of ES Into All DSS Components

## ES #1. Expert System's Interaction with Database Management Systems

According to a study performend by Jarke and Vassiliou [14], ES can interface with DBMS in two ways. First, the ES can be used to improve the construction, operation, and maintenance of the DBMS. Second, the DSS can provide the expert system with essential business data.

DBMS usually offer some basic capabilities — for example, summarization or categorization of data. However, the user would often like more sophisticated capabilities, such as the ability to perform some reasoning operations on the data. The high level of semantic knowledge and deductive capabilities provided by ES could make the DBMS more user-friendly and more efficient to operate and maintain.

A human expert frequently uses databases. It is reasonable to assume that a computerized expert would need to do the same. Therefore, the ES should be able to access the DSS database to obtain factual knowledge. Another possible coupling would be the inclusion of judgemental data obtained from experts in a DSS database.

Jarke and Vassiliou [14] describe the process of coupling an ES with a DBMS in the system of a life insurance firm, a prototype project which is being developed at NYU.

## ES #2. Expert System's Interaction with the Model Base

Human experts often use quantitative models to support their experience and expertise. For example, an expert may need to forecast the sales of a certain product or to estimate the future cash flow using a corporate planning model. Such a model can stand alone (meaning the expert can run the model on a computer as needed), or can be part of the DSS system used by several decision makers and experts. In the latter case, the model can be used by the ES (e.g., when certain IF-THEN rules call for it).

ES contribution in the area of models and model management can be demonstrated by examining the work of a consultant. A consultant is involved in the following steps:

1. Discussing with the manager (user) the nature of the problem,

2. Identifying and classifying the problem,

3. Constructing a mathematical model of the problem,

4. Solving the model,

5. Conducting sensitivity analysis with the model,

6. Recommending a specific solution, and

7. Assisting in implementing the solution. In this process, the system involves a decision maker, a consultant and a computer.

If we can codify the knowledge of the consultant in an ES, we can build a DSS/ES capable of the same process. Unfortunately, at this time relatively little is known about the nature of the cognitive skills that consultants use. However, interesting work is being done at Oregon State University, where Goul, et al., [9] have developed a DSS/ES system that attempts to replicate the manager-consultant-computer system. In this system:

1. The computer queries the manager to determine the general category of the problem (e.g., an allocation problem vs. inventory management),

2. The computer queries the manager to determine the exact nature of the problem (e.g., what kind of allocation problem), then

3. The computer suggests which management science model to use (e.g., dynamic programming vs. linear programming).

The manager can ask the system to define terminology to justify the recommendation made by the machine, and to explain the model used. The decision maker then can formulate the problem using the model, conduct “what-if” analysis, or use an alternate model. The ES, in this case, helps in identifying and classifying the managerial problem, acting as a tutor, providing illustrative examples and selecting the model(s) to be used.

Lehner and Donnel [15] claim there is a natural synergy between the prescriptive problem structuring techniques used in the DSS model base and the rule-based program architectures used in ES. In particular, the modeling procedures of the model base are suitable for initial problem structuring. Whereas, ES program architectures are suitable for (1) making the problem structure incrementally modifiable, and (2) developing a user interface that uses terms familiar to users.

Expert systems can be used as an interface between the user and the model base. Such an integration is demonstrated by BUMP, a statistical ES [10]. Large numbers of statistical packages are available on the market. These packages are being used both in industry and in educational institutions to support managerial decision making and research. They contain statistical tests and models that are included in the model base of a DSS. A major dilemma faced by a nonexpert user is to determine what statistical model to use for what purpose. This is where BUMP is brought into action. This ES selects the appropriate statistical procedure, and also guides the novice user in using the not-so-friendly statistical packages (such as MULTIVARIANCE and SPSS) that usually require a trained statisti-tion for their operation.

Other ES/DSS connections that relate to models and their management include:

\- ES that can provide heuristics to the DSS.

\- ES that can ease the task of building simulation models [21].

\- ES that can improve the DSS model management [2].

\- ES that can improve sensitivity analyses [9].

\- ES that can provide judgemental elements which are needed in using certain models. For example, a forecasting decomposition time-series model requires several judgemental decisions (e.g., which data to exclude when the seasonal component is computed). Such decisions are made only after the data are collected and analyzed. ES can be used as a consultant to determine what to do in specific cases.

\- A DSS model base that could include specialized models obtained from experts.

## ES #3. Expert System Interaction with the Interface

Making the interface friendlier is a major objective of any DSS. Expert systems and other AI technologies (such as speech recognition and natural language processors) have made a significant contribution in this area.

A critical obstacle to the use of DSS is the mismatch between the needs of end users and their ability to communicate these needs to the computer. The development of interfaces such as the spreadsheet and menu systems used on desktop computers are important steps toward the improvement of the manager-computer interface. For many problems, however, greater capabilities, flexibility and control are needed.

One of the most interesting applications of artificial intelligence is the natural language interface. Its major objective is to enable non-technical people to access complex databases. Natural language interface can be integrated into DSS and/or ES to considerably improve the interaction between managers and computers. In order to visualize the potential contribution of such a language, let us examine Figure 2.

The inverted triangle represents the number of people in each language category and their required training. The computer languages are listed on the right side. DSS languages are in the middle of the triangle, ranging from PL/1 and APL to RAMIS II and FOCUS (fourth generation computer languages). The natural language interface is aimed at users who do not know (or do not want to know) formal computer languages but still want to use the computer. Typical users in this category are managers, doctors, lawyers and other professionals. It should be noted, however, that only a few existing ES have natural language interfaces as front ends. Since natural language front-end systems, such an INTELLECT and CLOUT have been successfully applied to accessing complex databases it seems reasonable to assume that they will become an integral part of many DSS, ES and DSS/ES combined systems.

![](/api/attachments/5HN9BY8M/fulltext/images/22e2837f7d6785dce5ba31e3d19449a4a7b029bcc31117dcda0fea824215bfa3.jpg)  
Figure 2. Market for Natural Language  
Adapted from Harris, L.R. "Natural Language Front Ends," The AI Business, The MIT Press, 1984.

Another area where AI technology can make a significant contribution to DSS is the area of interactive visual modelling [1]. This technology enables the user to visually arrange models of certain management systems (e.g., factory layout) and determine all the necessary configurations. Then the user can observe the results (in terms of measures of performance) of different configurations. Furthermore, the configuration-results relationship can be observed in dynamic situations (e.g., one can see how a waiting line shrinks when the service rate increases). Such systems can support design and layout decisions, inventory, and scheduling, just to mention a few. A prototype of such a system is being developed by Intellicorp of Palo Alto, California.

Other possible areas of integration related to the man-machine interface include:

\- ES that can add the explanation capability to the DSS to allow the user to follow the reasoning behind certain recommendations.

\- ES that can manipulate symbolic information, thus making friendlier interfaces possible [27].

\- ES that can provide terms which are familiar to the user.

\- ES that can provide tutoring to the user [9].

## ES #4. Expert system as a consultant to the model builder

In addition to advice on constructing the various components of the DSS, one can visualize an ES which will give advice on how to structure a DSS, how to glue the various parts together, how to conduct a feasibility study, and how to execute the many activities which are involved in the construction of a DSS (as described by Sprague and Carlson [24]).

The same system may be used to advise the builder (or the user) how to change the DSS to fit the needs of the environment, or the specific scenario that the DSS describes.

## ES #5. Expert systems integration with the user

The user who is considered a component of a DSS may solicit the advice of an expert for complex issues such as the nature of the problem, the environmental conditions, or the possible implementation problems. For example, in a DSS designed to examine various proposals for reorganization, the user may ask an expert how the new structure will affect certain groups of employees. Instead of consulting an expert, the user may consult an ES. A user also may want an ES which will guide him (or her) how to use the DSS and its output. Another possible situation is for the user to seek advice on which specific DSS to use (if several are available).

## ES as a Separate Component in the DSS

As the reader may recall, a DSS is composed of four basic parts. It has been proposed $[23]$ that ES, and possibly other AI technologies, be added as a separate fifth component (see Figure 3). There are several possibilities for such integration.

## ES Output as Input to a DSS

DSS users may direct the ES output to the DSS. For example, the ES can be used during the intelligence phase of problem solving to determine the importance of the problem or project and to identify the problem. Then the problem is transferred to a DSS for possible solution.

## DSS Output as ES Input

In many cases the results of a computerized quantitative analysis provided by a DSS are forwarded to an individual or group of experts for the purpose of evaluation. Therefore, it would make sense to direct the output of a DSS into an ES which would perform the same function as an expert whenever it is cheaper and/or faster to do so (especially if the quality of the advice is also superior).

![](/api/attachments/5HN9BY8M/fulltext/images/4a18570513eb49c3040f5bf0168f729be980372282fa24cf7b56e1004d7c50e3.jpg)  
Figure 3. ES as a Component of DSS

## Sharing in the Decision Making Process

According to this approach, ES can complement DSS in one or more of the steps in the decision making process. An example for such an approach is proposed by Meador, et al., [17]. Decision making is viewed as an eight-step process consisting of:

1. Specification of objectives, parameters, probabilities.

2. Retrieval and management of data.

3. Generation of decision alternatives.

4. Inference of consequences of decision alternatives.

5. Assimilation of verbal, numerical, and graphical information.

6. Evaluation of sets of consequences.

7. Explanation and implementation of decisions.

8. Strategy formulation.

The first seven are typical DSS functions, while the last one, which requires judgement and creativity, can be done by an ES. Meador, et al., suggest that ES might supplement the DSS by using a built-in associative memory with knowledge of business and inferential rules.

Such an integration may be visualized as follows: The user works with the DSS following the first seven DSS steps. Upon reaching the strategy formulation phase he/she calls upon the ES, which will be a completely separate system although it may share the database and perhaps use some of the capabilities of the model base. To better understand this type of integration, we assume that the ES plays the role of a human expert which the user can call upon when in need of expertise in strategy formulation. The expert may give an answer immediately, or may conduct some analysis (e.g., forecasting). Such analysis can be accomplished by using the DSS database and its forecasting model.

## The Goul, Shane and Tonge Approach [9]

This approach views ES as an expert component in a DSS. The appropriate use of such a combination is in the intelligence or problem-finding phase of the strategic decision making process. The ES leads the decision maker to pertinent modes of reasoning. Therefore, it could offer conclusions with supportive justifications. This can also aid the decision maker in identifying objectives, diagnosing problems, and formulating models for analysis. The task of gathering data improves as the decision maker's scope is focused or expanded by the expert subsystem's requests for information. An additional outcome of this approach is that repeated use of the ES could reinforce effective decision making habits and teach new models of reasoning. It is logical to assume that the non-expert who repeatedly uses the expertise of an ES will learn and improve his decision making capabilities. $^{2}$

## Generating Alternative Solutions

Reitman [19] points out that most current DSSs help users evaluate and choose among potential courses of action (the choice phase of decision making). However, unlike a staff assistant these DSSs cannot suggest the alternative courses of action which should be considered (the design phase). He contends that this deficiency in existing DSS might be met by applying concepts and techniques taken from artificial intelligence.

Reitman describes an AI system that plays the game of Go. This system is able to work with non-numeric data to develop alternative game strategies, evaluate them, and select the best alternative. He provides a detailed description of the strategies employed by the system to find or develop courses of action:

— use of a network of experts at various levels of complexity of the game,

— successive refinement of problems from general to specific,

— assignment of priorities to situations, and

— use of an “expert and critic” structure. Reitman demonstrates how the system tests alternatives, and how it limits a search in order to keep the solution to a manageable task.

After describing the Go system, Reitman considers how AI-based DSS might be transferred to systems in a business context. For example, decisions regarding trading futures of commodities appear to be roughly of the same order of complexity as existing AI applications, and therefore appear to be a promising place to begin exploring the practical use of AI-based DSS.

## Problems and Issues in Integration

## Technical Issues

Integration will require compatibility of hardware and software. For example, if an existing ES runs on a Lisp type machine, and the DSS on a micro we may face some technical problems, such as the need to use different programming languages. Additionally, if we use generators, shells and other building blocks there could be problems finding skilled programmers for developing and combining the different parts. Such technical problems may be lessened in the future as both hardware and software containing DSS/ES capabilities continue to be developed.

## Behavioral Issues

Behavioral issues in DSS include consideration of the personal characteristics of decision makers, environmental or task characteristics, and related organizational issues. Behavioral research attempts to: (1) enhance the usefulness of information to the decision maker, (2) identify decision makers' information processing tendencies in order to tailor the database underlying the DSS to specific information processing styles, and (3) to provide insights into environmental and task characteristics that influence the decision. Since ES tend to draw conclusions and make recommendations, mimicking a human advisor, then certain aspects of the ES decision process do not directly benefit from much of the behavioral research accomplished to date in DSS. One reason for this is that ES focus on cognitive processes underlying the notion of expertise. These cognitive processes center on the long-term memory of the expert, and include perception, representation, retrieval, and reasoning [22]. In contrast, MIS and DSS behavioral research has tended to emphasize personality and abilities.

As discussed earlier, a desirable feature of ES is that it provides an explanation or justification for the decision reached. In practice, explanations of how ES arrive at their conclusions are not very convincing. One possible reason is that the explanations may not be tailored to specific individual users. The DSS behavioral literature concerning individual differences and the tailoring of information supplied by the DSS to individual decision makers could have relevance in tailoring the justification mechanism of ES. This is only one example for suggested research in this area.

## Design Issues

Several approaches to the design process for DSS can be borrowed from the construction of ES and vice versa. For example, the iterative DSS design approach $[1, 24]$ is also most suitable for ES construction. According to this approach, one uses a step-by-step dynamic approach to system development, as opposed to the systems life cycle approach commonly used in MIS system development.

Other design issues for expert systems or sub-systems pertain to limitations of current ES. One limitation is the fact that constructing an expert system may require several man-years of effort from an expert in ES design, while ES designers are currently in short supply. The expertise required on the part of the designer is: (1) knowledge of cognitive processes and the appropriate methodologies needed for extracting expertise from expert(s), and (2) programming skills in appropriate languages such as LISP, PROLOG, and/or the specialty dialects such as frame representation, natural language processors, and assembly languages. Note that these skills need not be provided by a single individual — a team approach is usually used. Typical DSS builders, including programmers and database experts, do not have the level of expertise necessary for building ES.

Thus, the construction time of a DSS, even when constructed with the aid of a DSS generator, can be stretched to an unacceptable length if an ES component is added. Commercially available “inference engines” and shells can reduce this problem by significantly decreasing the design and development time. Another possible relief to the problem is adding on “ready-made” expert systems to a specific DSS for advising in a general area of expertise.

Despite these (and possibly other) integration difficulties, there is evidence that DSS/ES integrated systems are being developed. Representative examples are given in the next section.

## Existing and Developing Integrated Systems

There are a growing number of integrated systems, as well as tools for integrated systems. Representative examples are presented below.

IBM's Integrated manufacturing system [26] — A system called Logistics Management System (LMS) was developed by IBM for operations management. The system combines ES, simulation, traditional DSS and computer-based information systems. In addition, the system includes computer aided manufacturing (CAM) and distributed data processing subsystems. It provides IBM's Burlington plant manufacturing management a tool to assist in resolving crises and in planning. A similar system is used at IBM by financial analysts to simulate long range financial planning, where an ES provides judgemental information and other pertinent factors.

DSS/Decision Simulation (DSIM) [25] — DSIM is the outcome of combining traditional DSS, statistics, operations research, database management, query languages, and artificial intelligence. AI, especially natural language interfaces and expert systems, provides three things to DSIM:

1. Ease of communication of pertinent information to the computational algorithm or display unit.

2. Assistance in finding the appropriate model, computational algorithm, or data set.

3. A solution to a problem where the computational algorithm(s) alone is not sufficient to solve the problem, a computational algorithm is not appropriate or applicable, and/or the AI creates the computational algorithm.

Promoter — This ES analyzes the effects of promotions and advertisements on sales in the packaged goods industry. It was developed by Management Decision Systems Inc. and it must be used together with their mainframe EXPRESS DSS generator.

## Engineering ES/DSS

This integrated system was designed to boost engineers' productivity. The DSS portion, called STRUDL (Structural Design Language), is essentially a passive tool thats effectiveness depends on the user's abilities. By supplying the proper data into the formula or the graphic modelling application, a design engineer can gain insight into his design prototype's potential. Unfortunately, STRUDL cannot help him decide what questions to ask or what data to key in, nor can it give any hints about further actions to take based on the results of an analysis. However, an expert system that assumes the role of teacher/partner was added on to do all this.

## Statistical ES/DSS

IFPS Optimum includes a logic component which identifies the nature of the problem. For example, in an allocation problem the package will identify if this is a linear or a nonlinear programming problem.

## Financial Services

A large financial services company already has a system which is close to being a working DSS/ES [20]. The company uses the system to match its various services with individual customers' needs (e.g. placing customers' assets into optimal investment packages).

Similar applications are being actively developed by large international accounting firms for combining analytical methods and judgement in auditing, and by other business entities for credit evaluation, strategic planning and related applications. General Dynamic Corp., for example, is using ES to support project management analysis.

REVEAL is a DSS generator with a strong modelling language designed mainly for financial and corporate planning (by Decision Products Inc.). It includes several typical ES capabilities. One important feature is approximate reasoning which is based on the mathematical theory of fuzzy sets. This capability enables representation of words such as “profitable,” and “fairly good” and “reasonably strong” which are frequently used by decision makers. In fact, creative decision making processes are unstructured, playful, and rambling. Fuzzy thinking can improve DSS by providing flexibility, and freeing the imagination.

## Developmental Tools

At the present time the developmental tools of DSS and ES are completely independent. However, there are some indications that such tools can be combined. Some ES developmental tools already possess DSS capabilities. For example, the Knowledge Workbench (from Silogic Corporation, Los Angeles) includes a universal database and a natural language interface. The M.1. (from Teknowledge, Inc., Palo Alto) includes a database interface. GURU, (from Micro Data Base Systems, Inc.), combines an expert system's shell with a database management system, a spreadsheet, graphics, communications, and a word processing package. Finally, KEE (from Intellicorp, Menlo Park) includes models for various computations and a system's simulation (regular and visual).

## Joint Hardware

Lisp Machines, Inc. produces a computer that can serve a DSS user and an expert system user (and possibly some additional users) simultaneously. Called “Lambda 2 x 2 Plus,” this system is equipped with a Lisp processor, a Unix processor, and the capability of adding a Prolog processor. Several other vendors are developing similar machines.

## The Fifth Generation Project (FGP)

Bonczek, et al., [5] cite the recent efforts of the Fifth Generation project as an example of the movement toward integrated DSS and ES. Figure 4 presents the conceptual diagram of the software system envisioned by the Japanese. As shown there, the key elements of the system are the knowledge base and its management system, which would incorporate the database, model base and the DBMS of current DSSs. The problem solving-inference system would be the ES aspect, and the intelligent interface system would encompass a natural language interface. In addition, intelligent systemization and utility systems would be developed. The basic application system would then interface with the rest of the components, much like current DSS.

## Conclusions

ES can make DSS a more active, and potentially more valuable participant in the decision process. Presently DSS is often used to answer the question “what if?” DSS/ES will also be able to answer the question “why?”

Scott Morton, who pioneered the concept of DSS, made the following remarks regarding the DSS/ES integration:

Conceptual Diagram of the Next Generation Computer Software System  
![](/api/attachments/5HN9BY8M/fulltext/images/425f2580e57553847a4c712e082ccfd9653d18e707a9b841ccea2776aab7a826.jpg)  
Reprinted by permission from the 1982 Proceedings of the Arthur Young Professors Roundtable, Arthur Young & Company, New York, New York, 1982.

"DSS as we know them may even become obsolete in the foreseeable future. They are being supplanted by expert decision support systems — EDSS. This next generation of DSS will combine existing DSS technology with the capabilities of Al. . . . The languages users input and the computer's response will virtually duplicate everyday human conversation, and the EDSS will be able to supply a variety of alternative solutions to problems ("if that doesn't work, try this. . . ."). EDSS will even warn users when they are proceeding under faulty assumptions ("Are you sure your figures for FY 1988 are accurate?") or supplying incomplete information (if the user inputs, "Give me the sales figures for Kansas City," the system will quickly reply, "Do you mean Kansas City, Missouri, or Kansas City, Kansas?")" [20, p. 12].

Despite the great potential of integration, one should not conclude that all future systems will be integrated. On the contrary, most DSSs (especially the small ones for personal use) will remain independent, at best sharing certain AI concepts and technologies with ES. Similarly, many ES will operate as independent systems, advising users on specific issues which are completely unrelated to any DSS.

There are several reasons why we believe that model 1 (ES integration into DSS components) will be most prevalent. First, there is evidence (which will be presented later) that some current design efforts are using this approach and several systems already are structured in this fashion. Second, an ES is usually applied to a narrow domain, while a DSS is usually broader in scope; therefore, it logically follows that several ES may be needed to fully support one DSS. This seems to be a very expensive arrangement. However, an expert system that specializes in one area (e.g., in a model base) could advise several DSS builders on model base issues (such as selection of a model), thus reducing the cost through sharing. Finally, recent developments in ES software tools (see Kinnucan [19]) could make the construction of a simple ES, in a very narrow domain, an inexpensive and rapid undertaking, i.e., it would be economically feasible to have several small ES exclusively serving one large, even ad hoc DSS.

While evaluating the potential integration of DSS and ES, one should not forget the potential difficulties of such integration and the many limitations of ES. As we described earlier, DSS have the flexibility to support the solution of a wide range of semi-structured and unstructured problems. ES are developed for very narrow domains. Thus the integration of a general problem support system (DSS) and a specific, narrow problem support system (ES) poses some difficulties. It is not clear that the expertise in ES is transferable across problem domains such as those potentially supported by a DSS, and thus research needs to be undertaken in this area. Also, today's ES fall short of the goal of performing at high levels of general intelligent behavior [11, 16]. Additional technical, behavioral, and design limitations and issues could provide a fertile ground for DSS/ES integration research. These limitations are spurring development of smarter systems, systems able to reason from what is called “deep knowledge.” But it may take several years before such systems are fully developed.

All of which is not to suggest that companies should refrain from integrating DSS and ES to wait until a trouble-free DSS/ES combination is available. Some experts contend that a state-of-the-art DSS could be upgraded today into an intelligent DSS with existing ES technology.

Recent studies from both the Boston-based Yankee Group and International Data Corporation in Farmingham, Massachusetts [20] show that decision support systems are currently being used by only two to three percent of non-DP/MIS executives and managers in U.S. companies. When the DSS/ES combination attain their full potential, and when executives are able to communicate with the computer by using their voice, these systems will be used by almost all managers and executives.

## References

[1] Alter, L. Decision Support Systems: Current Practices and Continuing Challenges, Addison-Wesley Publishing Com-

pany, Reading, Massachusetts, 1980.

[2] Basa, A. and Dutta, A. "AI-Based Model Management in DSS," Paper presented at ORSA/TIMS meeting, Dallas, Nov. 1984.

[3] Bell, P.C., Parker, D.C. and Kirkpatrick, P. "Visual Interactive Problem Solving — A New Look at Management Problems," Business Quarterly, Spring 1984, pp. 14-18.

[4] Bonczek, R.H., Holsapple, C. and Whinston, A. Foundations of Decision Support Systems, Academic Press, New York, New York, 1981.

[5] Bonczek, R.H., Holsapple, C. and Whinston, A. Developments in DSS. Research Report 1ST-8108519, MIS Research Center, Krannert Graduate School of Management, Purdue University, 1984.

[6] Davis, R. "A DSS for Diagnosis and Therapy," Data Base, Winter 1977.

[7] Dicken, H.K. and Newquist, H.P. AI Trends 85, DM Data Inc. Publishing, Scottsdale, Arizona, 1985.

[8] Ginzberg, M.J. and Stohr, E. “Decision Support Systems — An Overview,” in Decision Support Systems, M.J. Ginzberg, W. Rertman and E. Stohr (eds.), North Holland Publishing, Amsterdam, Holland, 1982.

[9] Goul, M., Shane, B., and Tonge, F. “Designing the Expert Component of a Decision Support System,” Paper delivered at the ORSA/TIMS meeting, San Francisco, May 1984.

[10] Hand, D.J. “Statistical Expert Systems: Design,” The Statistician, Volume 33, Number 10, October 1984, pp. 351-369.

[11] Harris, L.R. “Natural Language Front Ends,” in The AI Business, P.H. Winston and K.A. Prendergast (eds.), The MIT Press, Cambridge, Massachusetts, 1984.

[12] Hayes-Roth, F., Waterman, D. and Lenat, D. Building Expert Systems, Addison-Wesley, Reading, Massachusetts, 1983.

[13] Hogarth, R.M. and Makridakis, S. "Forecasting and Planning: An Evaluation," Management Science, Volume 27, Number 2, February 1981, pp. 115-138.

[14] Jarke, M. and Vassiliou, Y. "Coupling Expert Systems with Database Management Systems," in Artificial Intelligence Applications for Business, W. Reitman (ed.), APLEX Publishing Corporation, Nor-

wood, New Jersey, 1984.

[15] Lehner, P.E. and Donnel, M.L. “Building Decision Aids: Exploiting the Synergy Between Decision Analysis and Artificial Intelligence,” paper presented at the TIMS/ORSA National Meeting, San Francisco, California, May 1984.

[16] Martins, G.R. “The Overselling of Expert Systems,” Datamation, Volume 30, Number 18, November 1, 1984, pp. 76-80.

[17] Meador, C.L., Keen, P.G.W. and Guyote, M.J. "Personal Computer and Distributed Decision Support," Computerworld, Volume 18, Number 19, May 7, 1984, pp. ID7-ID16.

[18] Michaelson, R. and Michie, D. “Expert Systems in Business,” Datamation, Volume 29, Number 11, November 1983, pp. 240-246.

[19] Reitman, W. “Applying Artificial Intelligence to Decision Support,” in Decision Support Systems, M.J. Ginzberg, W. Reitman and E. Stohr (eds.), North Holland Publishing Co., Amsterdam, Holland, 1982.

[20] Scott Morton, M. “Expert Decision Support Systems,” a paper presented at the special DSS conference, Planning Executive Institute and Information Technology Institute, New York, New York, May 21-22, 1984.

[21] Shannon, R.E. “Expert Systems and Simulation,” Simulation, June 1985.

[22] Simon. H. The New Science of Management Decisions, Harper & Row, Publishing, New York, New York, 1960.

[23] Sprague, R. "The Role of Expert Systems in DSS," A paper presented at ORSA/TIMS Meeting, Dallas, Texas, November 1984.

[24] Sprague, Jr., R.H. and Carlson, E.D. Building Effective Decision Support Systems, Prentice Hall, Englewood Cliffs, New Jersey, 1982.

[25] Sullivan, G. and Fordyce, K. Decision Simulation, One Outcome of Combining AI and DSS, working paper #42-395, IBM Corporation, Poughkeepsie, New York, 1984.

[26] Sullivan, G. and Fordyce, K. “The Role of Artificial Intelligence in Decision Support Systems,” paper delivered at the International meeting of TIMS in Copenhagen,

Denmark, June 17-21, 1984.

[27] Waltz, D. “Artificial Intelligence: An Assessment of the State-of-the-Art and Recommendations for Future Directions,” The AI Magazine, Volume 4, Number 4,

Fall 1983, pp. 118-133.

[28] Winston, P.H. and Predergast, K.A. (ed.) The AI Business, MIT Press, Cambridge, Massachusetts, 1984.

## About the Authors

Dr. Efraim Turban is Professor of Systems Science and Director of Information Systems Research at the University of Southern California, Los Angeles. He has authored close to 50 papers in leading journals. In addition he authored eight books. His forthcoming book will be the first textbook to combine decision support systems and expert systems. He is co-recipient (with Paul Watkins) of the 1985 TIMS Roundtable award on artificial intelligence and management. His current research deals with expert systems shells for micros, as well as with further issues of DSS-expert systems integration.

Dr. Paul R. Watkins is Associate Professor of Accounting and Director of Computer Resources, School of Accounting, University of Southern California. He has published two monographs, systems related articles in leading international academic journals and serves as a referee and on the editorial board of a number of leading journals. He is a co-recipient (with Efraim Turban) of the 1985 TIMS Roundtable award on artificial intelligence and management. His current research is on analogical problem solving in expert systems, and the integration of management science models into intelligent systems.
