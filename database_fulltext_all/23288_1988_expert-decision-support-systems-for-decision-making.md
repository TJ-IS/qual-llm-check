---
otero_id: 23288
otero_key: "KAKMSRZ6"
title: "Expert Decision-support Systems for Decision-making"
authors: "Daniel T Lee"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.16"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Expert Decision-support Systems for Decision-making

Daniel T. Lee, Pan American University, Edinburgh, Texas, USA

Abstract: Computers have made tremendous contributions towards transactional processing. However, the highest pay-off the computer can make is not in transactional processing but in decision-making. Recently, expert systems have just begun to be used in the decision-making process. Individual technologies alone are inadequate for an effective decision support. The purpose of this paper is to investigate the related issues in decision support and to develop an expert decision support system (EDSS) for combining decision support systems and expert systems into a unified whole for decision support. The emphasis will be on developing a DSS/ES model which can be used to integrate the traditional DSS database and ES knowledge-base for building a user-friendly EDSS.

## Introduction

Since the concept of computer decision-support systems was first articulated in the early 1970s by Scott-Morton, $^{36}$ it has evolved through two decades. Most decision-makers still infrequently use computers to support their decision-making activities. The reason is partly because of computer literacy of decision-makers and partly because of user-friendliness of computers. Now computer technology has advanced to an unprecedented level and the computer literacy of decision-makers has also been greatly enhanced. According to a 1984 study, top executives still do not personally use computers in their decision-making process. This may support the fact that even though individual technology has advanced tremendously, decision-makers may still need something else to enable them to use computers comfortably, and that is an integrated system because individual technologies may help but may also compound the problem. $^{41}$

A noticeable effort has been made in unifying individual technologies during the past two decades. For example, microelectronics and management science contribute greatly towards end-user computing. Micro-mini computers and data communication make distributed data processing possible. Now expert systems have suddenly emerged as one of the most important advancements in decision support. Unfortunately, they are not totally integrated into the decision-making process. The purpose of this paper is to investigate the decision-support movement and the individual technologies in the decision-making process. The emphasis will be on the integration process and developing an integration data model that can be used for combining decision-support systems (DSS), executive information systems (EIS), expert systems (ES), and other computer-based information systems (CBIS). This integrated data model will accommodate both the traditional DSS databases and ES knowledge bases. $^{16, 23}$

After a brief historical review of computer evolution, there will follow an overview of three systems in DSS, EIS and ES. Then technology integration for decision support will be intensively investigated followed by discussion of the integration data model. Finally the research findings are summarized.

## Historical development

Computers have evolved through many stages during the past four decades from electronic data processing (EDP), management information systems (MIS), decision-support systems (DSS), executive information systems (EIS), and now towards expert decision-support systems (EDSS). Each stage has carried out a mission either in transactional processing or in decision support. The last stage 'EDSS' is a new era of integrated systems for combining CBIS, DSS, EIS and ES for decision support. $^{6,1}$

The EDP era of transactional processing has made tremendous contributions towards human civilization in saving labour and automating paper work. MIS tried to unify the segmented individual programs for decision-making but was only partially successful. DSS was conceived to carry out this unfulfilled need by providing information to decision-makers in their decision-making process. Through two decades' efforts, progress has been made in each individual technology but it is still far behind the ultimate goal of integrating all elements of information technology for decision support. In the following three sections, a brief review will be given to DSS, EIS and ES for a thorough understanding of the major elements in the integrated system. $^{21, 18}$

![](/api/attachments/KAKMSRZ6/fulltext/images/5185cb03dc5790e4b693b87236e93e83c2c8d1eacb4b88d84f7698d4be731616.jpg)  
Figure 1. Structure of a decision support system

## Decision-support systems – an overview

## Definition

DSS was first defined by Scott-Morton as 'interactive computer-based systems, which help decision-makers utilize data and models to solve unstructured problems'. $^{36}$ Keen and Scott-Morton $^{15}$ define DSS as a computer-based support system for management decision-makers to improve the quality of decisions in semi-structured problems. These two definitions indicate several major characteristics of DSS:

1. They incorporate data and models, and query interactive interface.

2. They are designed to assist the decision-makers in solving semi-structured and unstructured problems.

3. They utilize individual judgement for improving the quality of decision-making. $^{18}$

Bonczek et al. define a DSS as a computer-based system consisting of a language system, a knowledge system and a problem-processing system. $^{5}$ This definition paves the way in integrating DSS and ES. Keen defines a DSS as the product of an adaptive process of learning and evolution. $^{19}$ This definition will contribute to the understanding of the intelligent DSS that is equivalent to integrated EDSS.

From the above definitions, though there is no consensus on what a DSS is, there is obviously an ideal list of characteristics for a decent DSS. It must support the decision-makers in their decision-making process rather than replace the decision-makers. It must be user friendly, flexible and adaptive. It should improve the effectiveness of decision-making and the productivity of the decision-makers.

## Components

According to Sprague and Carlson, a DSS is composed of four components: data management, model management, dialogue management, and the user. $^{40}$ The data management consists of databases and database management systems (DBMS). The model management contains model bases and model software packages for analytical purposes. The dialogue management is composed of interface software for user communication with the system. The last component is the end-user whose judgement and cognitive style are vitally important for a successful DSS.

The data in the DSS databases may contain internal transaction data, external sources data and private data. A DSS may have a separate extracted database for exclusive use. The extraction process is managed by the DBMS of the system.

The models in the model base are managed by the model base management system (MBMS). Traditionally, it is difficult for MBMS to decide 'which model should be used for what occasion?' because model selection requires expertise. If it is integrated with ES, the ES can assist the DSS. $^{2}$ The structure of a DSS is shown in Figure 1.

The user interface of a DSS is the software and hardware for facilitating user communication with the system. The dialogue process may consist of three parts: the action language for user communication and data input, the display or presentation language for what the user sees or hears, and the knowledge base for the information the user must know.

The users themselves are an important component of a DSS because different users have different needs in accordance with their organizational level, functional area, educational background, and need for analytical support. These sub-categories will influence DSS design and software and hardware selection.

## Software and hardware

The major hardware options are a time-sharing network, corporate mainframe, micro-mini computer, or a combination of the above. Time-sharing networks offer a variety of capabilities that are not available on an in-house system but that may be important to the DSS. Most time-sharing networks have an extensive set of DSS software packages. If the DSS is located in-house, a mainframe, micro-mini or personal computer might be used. A variety of factors can influence the choice of computer used, such as the type of decision support, the data needs, the computational power, the existing network and the software demands of the DSS.

## DSS development methodologies

DSS are designed for dealing with complex situations. They often must be custom-built to the specific use. Since it is almost impossible to identify all the information requirements before starting the design of the system, traditional system development life cycle (SDLC) methodology cannot be used in the development of DSS. An iterative approach is more appropriate for an ad hoc type of DSS because the development cycle is usually shorter. $^{40, 25}$

## Technological level

Sprague identified three levels of DSS technology: specific DSS, DSS generators and DSS tools. $^{39}$ The finished DSS that supports specific application is called a specific DSS. A generator is a software package which is used to build specific DSS, and DSS tools are the software utilities or tools that are used for developing DSS generators or specific DSS.

## End-user computing

Technology advancement of microelectronics has created a revolution in end-user computing. It is very natural that many end-users attempt to use and construct their own DSS. According to Rockart and Flannery, $^{35}$ the number of end-users is growing at a rate of 50 to 100 per cent annually. Many end-users, including executives, like to build their own DSS using Lotus 1-2-3, Symphony and Framework. $^{23}$

## Development tools

System development is time-consuming and expensive. Therefore, building a DSS from scratch is rare except for large complex systems. There are hundreds of software packages on the market that can be used as

DSS tools. A DSS consists of three basic components: database, model base, and dialogue subsystem. There are several construction tools that have to be geared towards these three components.

Computer and programming languages are needed for all three components. Graphics generators and visual interactive modelling packages are required for the dialogue subsystem. DBMS and fourth-generation software are needed for the database component. The model base component will consist of electronic spreadsheets, MBMS, financial modelling, statistical and analytical packages, as well as template and macro aids. In addition to these three basic component construction tools, there are several integrating tools that are also vital for DSS construction such as integrated micro systems, distributed DSS, data communication, software, DSS generators, and ready-made DSS. Detailed discussion of the above items is beyond this paper. Interested readers please refer to Turban, $^{46}$ Martin $^{30}$ and Lee. $^{26, 22}$

## The basics of executive information systems

## Characteristics

Most existing DSS support professionals and mid-managers, they are very seldom used by top executives directly. EIS is a new technology that emerged recently in response to this unfulfilled need. $^{34}$ Basically, EIS is a part of DSS. However, they are different but complementary products in a functional sense. EIS is an automated system used to keep the executives abreast of what is happening in the organization. This tracking is supposed to be done by the system itself without management efforts.

EIS are designed very differently from DSS. They are used for performing structured and repetitive analysis as well as exception tracking and reporting, as opposed to the unique ad hoc analysis of the traditional DSS. Therefore, the tools productive for DSS may be counterproductive for EIS. When more complex analysis is needed, DSS support EIS. Therefore, they are complementary. According to Fedorowicz, $^{12}$ a study released by MIT's Center for Information System Research in 1986 shows that about one-third of large US corporations now have EIS programs either installed or under way. It was also found that more than half of the EIS installed were used by top executives.

## Software

Software for EIS is an integration of office automation systems including wordprocessing and electronic mail. EIS are designed with less modelling capabilities and strong DBMS and data communication facilities. The construction is done with the aid of EIS generators such as Commander Center, which is built around a central database on the mainframe. Commander Center distributes processing between a mainframe computer and any number of IBM PCs. Thus, the user has the best of a quick response, highly interactive PCs, and a massive database service. EIS do not have model bases but they can receive data from DSS and other computer-based information systems (CBIS). There are many other EIS software such as Commander EIS, CEO, OPN, METAPHOR, etc which are commercially available. $^{2}$

## Hardware

EIS require at least a minicomputer and PC. Typical hardware will include a mainframe or a minicomputer like IBM VM/CMS, DEC VAX, Honeywell and user workstations which are compatible with the mainframe.

## Integration of DSS and EIS

It is very common for EIS to be used as a source of data for PC-based modelling products. Through upload and download, the executives can get on their EIS and see what is going on in the firm. This is a typical example of the complementary nature of EIS and DSS. EIS use the latest technology to improve management. EIS are used as an executive's filter causing information to be compressed and summarized in the form needed by the executives. The emergence of EIS signals a new era of computer revolution by integration of EIS, DSS and other CBIS.

## Fundamentals of expert systems

Artificial intelligence (AI) has dawned a new era which may have an unprecedented impact on human civilization in general, and organizational management in particular. Unfortunately, AI has not yet been integrated into the mainstream of the information revolution, but an encouraging movement of bringing the AI/ES into the mainstream is steadily underway.

## Definition

AI is a branch of computer science that deals with ways of representing knowledge and rules of thumb for processing information. $^{46}$ Levine et al. define AI simply as a way of making a computer think intelligently. By studying how people think in making decisions and solving problems, the designer designs a computer program that solves problems using the same thinking process. $^{28}$

ES are computer programs that attempt to imitate the reasoning process and knowledge of experts in solving specific types of problems. $^{46}$ Holsapple et al. $^{15}$ define ES as computer-based consultants that draw upon application-specific expertise in offering advice for solving problems. In other words, ES are systems that employ human knowledge captured in a computer to solve problems that usually require human expertise. Newell-Simon $^{32}$ proposed a model of human problem-solving that makes use of the analogy between computer processing and human information processing. The related disciplines in AI include: ES, natural language processing, robotics, computer vision, speech recognition and computer-aided instruction. $^{12}$

## The structure of ES

ES are composed of three basic components: a knowledge base (KB), an inference engine (IE) and a user interface (UI). The knowledge engineer acquires the knowledge from the experts for construction of the KB. The IE is a computer program that utilizes the knowledge stored in the KB for problem-solving. The knowledge stored in the KB consists of domain facts and inference rules. The UI is a language processor for friendly interface between the users and the system. This interface could best be carried out in a natural language. $^{48, 20}$ The structure of an ES is shown in Figure 2.

![](/api/attachments/KAKMSRZ6/fulltext/images/3ce4f400a063f25ae303277c3815d26e814ad18eb088a842128e205cb5323918.jpg)  
Figure 2. Structure of an Expert System

## Knowledge engineering

Knowledge engineering (KE) involves knowledge acquisition (KA), knowledge representation (KR), inference, and explanation. KA extracts knowledge from sources of expertise and then transfers it to the KB. Knowledge is a collection of domain facts, procedures and judgement rules. $^{12, 11}$

The techniques of KR are predicate calculus, production rules, semantic networks, frames, and object-and access-oriented programming. $^{45}$

The predicate calculus is that a predicate makes statements about objects that can be either true or false. This configuration permits the computer to draw conclusions not only in a specific case, but also if some conditions are changed. That is, the computer is programmed with general rules, using variables instead of specific values.

The production rule is that the procedural or factual knowledge is represented as rules in the form of a condition-action pair. It is increasingly popular in the production system and also very widely used in other areas of KR or ES such as DENDRAL, MYCIN, and PROSPECTOR. The reason it has become popular is because each rule in an ES is independent of other rules. Rules are not just a neat formalism to represent expert knowledge in a computer; rather, they represent a model of actual human behaviour.

The semantic networks are a natural and efficient way to organize knowledge. They are composed of nodes and links. Nodes describe facts like physical objects, concepts or situations. The links define relationships among the facts. Each node may point to a sub-node. 'IS A' and 'HAS A' are two common relationships in semantic networks that allow facts to be attached to classes of objects and inherited by specific objects in the class. Semantic nets are one of the best means of representing non-rule knowledge. Semantic net notation is similar to the terminology of database systems and best depicted diagrammatically. A number of ES like INTERMST and PROSPECTOR rely on network formalisms.

A frame is a data structure that includes all the knowledge about a particular object, stored and organized in a predefined manner. The frame is composed of slots (attributes) and fillers (values). Frames contain information about many aspects of objects or situations. A frame system organizes the objects and their relations into entities. It is highly similar to the notation of existing relational database systems.

Object-oriented programming languages (OOPL) use objects (entities) to combine both procedures and data into one unit, while conventional programming languages use procedures and data separately. Since AI and ES deal with ways of representing knowledge and rules of thumb for information processing, OOPL have become very popular because this method of knowledge representation can take care of both entities and rules at the same time. Often OOPL are used as add-ons to LISP or PROLOG. They are also found in regular simulations and in DSS. Besides, OOPL are related to frame representation and can be found in ES construction tools like KEE and KRL, and are also available as separate commercial tools such as LOOPS and SMALLTALK, in addition to ES-building tools. $^{46, 12}$

Access-oriented programming languages (AOPL) gather data that can cause procedures to be invoked. This complements object-oriented programming. These representation methods are supported by special software such as LOOPS and can be combined with a DSS generator and ES shells. $^{42}$

Knowledge representation should be able to support knowledge acquisition, retrieval and inference. Unfortunately, so far there is no single KR method that is ideally suited for all tasks. Production rules are simple, flexible and highly modular, but inefficient for large systems; not all knowledge can be expressed as rules. Semantic networks have an easy-to-follow hierarchy enabling the association among entities to be traced without difficulty, but they are ambiguous in attaching meaning to nodes and exception processing is difficult. Frames' attribute-value pair is versatile. It is easily related to the most popular relational database model, easy-to-create specialized procedures and easy-to-include default information. The problem of the method is that it is hard to program and difficult to draw inference.

The best choice now may be to adopt a hybrid KR method to combine the best features of both production rules and frames. The production rule is good at representing procedures or factual knowledge as rules, while the frame method provides a rich structural language for describing the objects referred to in the rules. Frame taxonomies can also be used to partition, index and organize a system's production rules. Frames allow the implementation of the relations among objects for deeper reasoning by abstraction and analogy. $^{42, 45, 12}$

## Development of ES

Construction of ES is a lengthy process. Most early commercial ES development required special-purpose computing hardware and experienced knowledge engineering. Most of the popular systems such as MYCIN, XCON and DENDRAL were built with many man-years of effort and millions of dollars. Recently, technology advancement in AI computers and knowledge engineering software tools has changed the picture. Selection of hardware is a problem only when large systems are built. Small ES systems are being developed on PCs. Even large systems can be developed on existing minicomputers.

Prototyping has been crucial to the development of many ES. A prototype ES is a small-scale system. If it is a rule-based system, the prototype may include less than a hundred rules that are sufficient to produce consultation of a limited nature. The construction cost is low and the effect can be seen quickly.

The software and hardware classification in ES is similar to that used with DSS. $^{6}$ It is divided into three major groups: specific ES, shells and tools. Building tools can be used to build shells and specific ES. Shells are integrated software packages used to construct specific ES. Most of the well-known shells developed in the 1970s, such as EMYCIN, KAS and EXPERT, are located mainly at universities and research institutions. They run on mainframes and embody only one reasoning mechanism and knowledge representation. Recently, several commercial knowledge engineering development tools have largely simplified the development process, eg GURU and KNOWLEDGE WORKBENCH are integrated commercial shells which can run on microcomputers. $^{46, 12, 48, 15}$

## Technology integration for decision-making

So far we have briefly reviewed DSS, EIS and ES individually. As pointed out earlier, individual technologies are inadequate for effective decision support. They must be integrated for a unified effort because the effect of an integrated system is larger than the sum of the individual technologies. Unfortunately, a satisfactory solution has not yet been reached though individual technologies are basically ready. The rest of the paper tries to trace all these individual technologies and to develop a data model that can be used for unifying the relevant technologies into an integrated system for decision support. Before presenting the proposed model, a brief review of related issues on integration will pave the way for the model construction. $^{15, 45, 24, 21}$

## Why is integration needed?

In addition to the above reason for integration, there are a couple of other important reasons: (1) An ES is usually applied to a narrow domain, whereas a DSS is usually broader in scope; therefore, several ES may be needed to support fully one DSS. This could be very expensive. However, an ES could be used to advise several DSS builders on model base selection, thus reducing the cost through sharing; (2) ES can make DSS more valuable because DSS/ES can answer 'why?' whereas DSS can only answer 'what if?'. $^{46, 15}$

## The synergetic effect of integration

A DSS is an interactive computer-based information system that utilizes decision rules, models and databases for supporting decision-making, while an ES is a computer program that includes a knowledge base and reasoning mechanism for rendering advice. In addition, an ES extends explanation and justification of the advice rendered. Most ES are being used as independent computerized systems for advising users on a specific problem area. As such, they are considered as intelligent DSS. Furthermore, ES fit the generic DSS nicely and exhibit three major characteristics of DSS.

They, however, also have several differences. Specifically, the objectives of the system are different. The DSS supports the decision-makers in making decisions while the ES operates as an advisor. The problem area attacked by the DSS is broad and complex while the ES is restricted to a narrow area. As a result, DSS is more suitable for dealing with ad hoc and unique situations while ES is more suitable for providing advice on narrow and repetitive problem areas. The database of DSS contains facts while the knowledge base of ES contains procedures in addition to facts. ES exhibit reasoning and explanation capabilities while DSS do not. ES are closed systems while DSS are open. Basically, an ES is qualified as a DSS, but only as a special class of DSS with unique characteristics. Therefore, they not only can be integrated but they are also complementary.

## The pattern of integration

In a certain problem area, both ES and DSS may have distinct advantages that, when combined, can have a synergetic effect. A DSS is composed of four basic components. An ES can be added to each component as a separate fifth component of a DSS.

When it is added to the database component of a DSS, according to Jarke and Vassiliou, $^{17}$ ES can interface with DBMS in two ways: first, the ES can be used to improve the construction, operation and maintenance of the DBMS; and second, the DSS database can provide the ES with the basic data. Basically, the ES can provide the DSS with the high-level semantic knowledge and deductive capabilities for reasoning operations on the data.

When added to the model base component, the ES can provide heuristics to the DSS, improve sensitive analysis and model management. $^{3, 10, 38}$ The DSS can also provide the ES with standard models and problem structure. $^{27}$

When added to the dialogue component, the ES provides the DSS with explanation, symbolic information, natural language interface, dynamic visual problem-solving and friendly interactive man-machine interface, while the DSS provides presentation to match individual cognitive styles. $^{4, 13, 47}$

In addition to being added to the various components of the DSS, the ES can act as a separate component of a DSS. The DSS user may direct the ES output to the

DSS and vice versa. $^{41, 37, 14}$ Basically, the ES plays the role of a human expert that the user can call upon when in need of expertise in strategy formulation. $^{10, 31}$

## Problems in integration

Integration is a very complicated phenomena. There are many roadblocks in the integration process. First, integration requires compatibility of hardware and software. For example, if the DSS currently runs on a microcomputer and the ES runs on a LISP machine, we may face compatibility problems. Secondly, the ES focuses on the cognitive process to mimic human behaviour while the DSS emphasizes personalities and abilities. Therefore, the explanations by the ES may not be tailored to specific individual users. Third, the adaptive and iterative design techniques of DSS can be applied to the design of ES, but the data structure in the database of DSS may not match that of the knowledge system of ES. The last one may be one of the most thorny problems in the DSS/ES synergy. We will come back to this problem later for a possible solution in developing a unified model that could be used in structuring both static domain data and dynamic procedures.

## Existing integrated systems

LMS (logistics management system) is a system developed by IBM for operation management. This system combines DSS, ES and other CBIS including simulation, computer-aided manufacturing and distributed data processing capabilities into a unified system for solving manufacturing and planning problems. $^{44}$ DSIM (DSS/decision simulation system) is a system that combines traditional DSS, ES, database management, statistics, query languages and natural language interfaces for model selection and problem-solving. $^{43}$

Currently, DSS and ES development tools are independent. However, some tools begin to combine the capabilities of others, such as the KNOWLEDGE WORKBENCH that includes a universal database and a natural language interface. GURU combines an ES's shell with a database processing package. EXSYS has interfaces to both DMBS and DSS generators. KEE consists of models for computation and simulation.

Recent movement in hardware and fifth-generation computers is in the direction of integration. The LISP Machine, Inc produces a computer that can serve both DSS and ES users simultaneously. The Japanese fifth-generation project is working towards total integration that combines databases, model bases, knowledge bases and inference systems with natural language interface. $^{7}$

Though the DSS/ES integration is definitely an inevitable trend, the difficulty confronting the integration developer in hardware and software disparity and data modelling is also real. Data modelling of DSS database and ES knowledge base is the most difficult job in DSS/ES integration. This is the topic of the next section.

## Integration model of DSS/ES synergy

## Existing techniques

As indicated earlier, the DSS database basically stores static domain facts while the ES knowledge base stores dynamic inference rules in addition to domain facts. So far there is no perfect solution in finding a data model that can be used for structuring both the static and dynamic rules and domain facts without conflict. The six knowledge representation techniques discussed earlier also found no solution. The only hopeful solution is to adopt a hybrid method for combining the features of several methods, such as the production rules and the frames.

## DSS/ES integration model (DEI)

The DEI model combines all the features of traditional relational databases, DSS databases and all the knowledge representation techniques, especially the techniques of production rules and frames. DEI can also accommodate an object-oriented data model. In a frame data structure, all knowledge is organized and stored in the knowledge base as a set of attribute-value pairs.

DEI is basically an object-oriented knowledge base model. This model is a collection of objects and the relationships among objects. Objects correspond to conceptual entities and the structures imposed on the data as well as the operations defined on the data. These will induce the static domain facts and the dynamic inference rules.

Each object corresponds to a relation that is identified by a unique key. The objects are unique entities and correspond to many types of objects, such as descriptor objects, abstract objects, domain objects, behavioural objects, text objects, image objects, and audio objects. $^{29}$ Objects in the DEI model are arranged in a hierarchy in accordance with the theory of the frame representation. Types are a named collection of objects. Objects belonging to the same type share common properties which are operations (functions) defined on types. A relationship can be defined by the object key or the object identifier. Relationships are special relations which can be operated as normal objects.

Objects and relationships are the basic concepts for information modelling and operation. The objects can be copied and moved from a knowledge base to a knowledge base. Mechanisms are provided to allow relationships to be established across KB boundaries.

DEI is a simple KB model for the specification of objects and relationships in a logical network of KB. Detailed discussion of object-oriented KB is beyond this paper. For further information, please refer to References 29, 2, 9 and 33.

## Concluding remarks

Computer technology has been a limiting factor for ES development for a while. Recently, in the area of technological advancement in VISI, parallel processing, fourth-generation languages, natural language processing, speech recognition, distributed data processing, and database management a new era of systems integration has dawned. This is really a second information revolution. This new revolution is being accelerated by the Fifth-Generation Project announced in 1982 by the Japanese Government, the Strategic Computing Program announced by the Defense Advanced Research Projects Agency (DARPA) in 1983, and the four projects currently engaged in by the MCC which was established in response to the Japanese challenge. $^{2}$

All these projects are currently engaging in high tech research and development involving fifth-generation computers, computer vision, speech recognition, natural language processing, AI/ES knowledge systems, VLSI/computer-aided design, database management systems, advanced computer architecture and human factor technology. The research results of these projects will no doubt have a revolutionary impact on systems integration. We can predict that though success is limited to date, the future is very promising in terms of systems integration.

The trend in DSS development will make the personal-computer-based DSS continue to grow at an unprecedented rate. Integrated micropackages will take on more functions. The trend towards distributed DSS will enhance the linkage between mainframe DSS and PC-based facilities. DSS products will begin to incorporate AI/ES techniques.

ES are still in an infant stage. It is unrealistic to expect immediate practical results. Yet, as many AI researchers started to deal with real-world problems they achieved some degree of success in application, even in difficult areas requiring intense effort. The shallow model, such as product rules, is limited in real-world application. The deeper model is hard to describe and use. Greater effort is needed in searching for a practical hybrid model. To date, no one has demonstrated a generalized model or tools that are comparable to the classical model. Knowledge engineering is still the bottleneck in ES and DSS/ES development. Today, we are far from being ready to supplant the knowledge engineer and expert with a system that automatically learns rules from experience and automatically improves the ES itself.

The technology for embedding ES in a microprocessor chip to form an integrated hardware-software package is already there, for example, the EEG Analysis system, an ES embedded in a Motorola MC6801 single-chip, eight-bit microcomputer designed to interpret electroencephalograms recorded from renal patients. The integrated ES could handle tasks such as monitoring and controlling equipment operations. The integrated ES can also be hard-wired into the equipment with a direct connection to sensors and switches that allow the ES to monitor and control the operation of equipment. The intelligent system will be useful when the equipment to be monitored forms a hierarchy of physical units arranged in some network structure. Each unit can then have an attached ES that monitors its own operation. An intelligent system has already been developed and put into commercial use. The SPE ES runs on a microprocessor inside Clini-Scan, Helena Laboratories' scanning densitometer. The ES interprets waves from the densitometer to determine which of several diseases a patient might have. $^{46}$

When will these integrated intelligent systems be widely used in the human decision-making process?

Many scholars and practitioners believe that it is a matter of time. No society or organization can afford to ignore this new era of information revolution – the age of systems integration.

So far, we have reviewed the computer revolution, the fundamentals of DSS, EIS and ES, and developed a DSS/ES integration model (DEI) that can be used in the integration process of DSS, EIS and ES for decision support. The future of integration is bright though there are many roadblocks that need further research, especially in the integration data model area.

## References

1. Alter, Steven L. (1980) Decision Support Systems. Addison-Wesley.

2. Bannerjee, J., Chou, H. T., Garza, J. F., Kim, W., Woelk, D., Ballou, N. and Kim, H. J. (1987) Data model issues for object-oriented applications. ACM TOOIS, 5, 1, Jan.

3. Basu, A. and Dutta, A. (1984) AI-based model management in DSS. Unpublished report, University of Rochester.

4. Bell, P. C., Parker, D. C. and Kirkpatrick, P. (1984) Visual interactive problem solving – A new look at management problems. Business Quarterly, Spring.

5. Bonczek, R. H., Holsapple, C. W. and Whinston, A. B. (1980) The evolving roles of models in decision support systems. Decision Sciences, 11, 2.

6. Bonczek, R. H., Holsapple, C. W. and Whinston, A. B. (1982) The Evolution from MIS to DSS: Extension of Data Management to Model Management. North-Holland, Amsterdam.

7. Bonczek, R. H., Holsapple, C. W. and Whinston, A. B. (1984) Developments in decision support systems. In Advances in Computers. Vol. 23. (M. Yoritz, ed.). Academic Press, New York.

8. Fedorowicz, J. (ed.) (1986) Transactions, DSS-86, 6th Annual Conference on DSS. April 21-24, Institute of Management Science, Washington DC.

9. Fishman, D. H., Beech, D., Cate, H. P., Chow, E. C., Connors, T., Davis, J. W., Derrtt, N., Hoch, C. G., Kent, W., Lyngbank, P., Mahbod, B., Neimat, M. A., Ryan, T. A. and Shan, M. C. (1987) Iris: An object-oriented database management system. ACM TOOIS, 5, 1, Jan.

10. Goul, M., Shane, B. and Tomge, F. (1984) Designing the expert component of a decision support system. Paper delivered at the ORSA/TIMS National meeting, San Francisco, May.

11. Harmon, P. and King, D. (1985) Expert Systems: Artificial Intelligence in Business. John Wiley and Sons.

12. Harmon, P., Mans, R. and Morrisey, W. (1988) Expert Systems: Tools and Applications. John Wiley and Sons.

13. Harris, L. R. (1984) Natural language front ends. In The AI Business (P. H. Winston and K. A. Prendergast, eds). MIT Press, Cambridge, Mass.

14. Hayes-Roth, F., Waterman, D. and Lenat, D. (1983) Building Expert Systems. Addison-Wesley, Reading, Mass.

15. Holsapple, C. W., Tam, K. Y. and Whinston, A. B. (1987) Expert system integration. In Expert Systems for Business (B. G. Silverman, ed.) Addison-Wesley.

16. Holsapple, C. W. and Whinston, A. B. (1987) Business Expert Systems. Richard D. Irwin.

17. Jarke, M. and Vassiliou, Y. (1984) Coupling expert systems with database management systems. In Artificial Intelligence Application for Business (W. Reitman, ed.) ABLEX Pub. Co., Norwood, N.J.

18. Keen, P. G. W. and Scott-Morton, M. S. (1978) Decision Support Systems, An Organizational Perspective. Addison-Wesley, Reading, Mass.

19. Keen, P. G. W. (1980) Adaptive design for decision support systems. Database 12, 1 & 2, Fall.

20. Keller, R. (1987) Expert System Technology: Development and Application. Yourd Press.

21. Lee, D. T. (1984) A unified method for information system development and database application. International Journal on Policy and Information, 8, 2, Dec.

22. Lee, D. T. (1985) A cohesive methodology of integrating technical and organizational issues for information systems and database design. International Journal on Policy and Information, 9, 1.

23. Lee, D. T. (1985) Personal computing for decision support. Oxford Surveys in Information Technology, Vol. 2, Jan.

24. Lee, D. T. (1985) Integrated systems for transactional processing and decision support. International Journal on Policy and Information, 9, 2.

25. Lee, D. T. (1987) Computer information system development methodologies – A comprehensive analysis. NCC '87 Conference Proceedings, Chicago.

26. Lee, D. T. (1987) Technological advancement and end-user computing for decision support—An integrated system approach. International Journal on Policy and Information, 11, 1, June 15.

27. Lehner, P. E. and Donnel, M. L. (1984) Building decision aids: exploiting the synergy between decision analysis and artificial intelligence. Paper presented at ORSA/TIMS National Meeting, San Francisco, May.

28. Levine, R. I., Drang, D. E. and Edelson, B. (1986) A Comprehensive Guide to AI and Expert Systems. McGraw-Hill.

29. Lyngback, P. and McLeod, D. (1984) Objected management in distributed information systems. ACM TOOIS, 2, 2, April.

30. Martin, J. (1984) Fourth Generation Languages. Prentice-Hall.

31. Meador, C. L., Keen, P. G. W. and Guyote, M. J. (1984) Personal computer and distributed decision support. Computerworld, 18, 19, May 7.

32. Newell, A. and Simon, H. A. (1972) Human Problem Solving. Prentice-Hall, Englewood Cliffs, N.J.

33. Purdy, A., Schuchardt, A. and Majer, D. (1987) Integration an object-saver with other worlds. ACM TOOIS, 5, 1, Jan.

34. Rockart, J. E. and Treacy, M. E. (1982) The CEO goes on-line. Harvard Business Review, Jan.-Feb.

35. Rockart, J. F. and Flannery, L. S. (1983) The management of end-user computing. Communications of ACM, 26, 10.

36. Scott-Morton, M. S. (1971) Management Decision Systems: Computer-Based Support for Decision making. Division of Research, Harvard University, Cambridge, Mass.

37. Scott-Morton, M. S. (1984) Expert decision support systems. Paper presented at a special DSS Conference, Planning Executive Institute and Information Technology Institute, New York, May 21-22.

38. Shannon, R. E. (1985) Expert systems and simulation. Simulation, June.

39. Sprague, R. H., Jr. (1980) A framework for the development of decision support systems. MIS Quarterly, Dec.

40. Sprague, R. H., Jr. and Carlson, E. D. (1982) Building Effective Decision Support Systems. Prentice-Hall, Englewood Cliffs, N.J.

41. Sprague, R. H. (1984) The role of expert systems in DSS. Paper presented at ORSA/TIMS Meeting, Dallas, Nov.

42. Stefik, M. J. et al. (1986) Integrated access-oriented programming into a multiparadigm environment. IEEE Software, Jan.

43. Sullivan, G. and Fordyce, K. (1984) Decision simulation, one outcome of combining AI and DSS. Working paper 42-395, IBM Corporation, Poughkeepsie, N.Y.

44. Sullivan, G. and Fordyce, K. (1985) The role of artificial intelligence in decision support systems. Paper delivered at the International Meeting of TIMS in Copenhagen, June.

45. Tanimoto, S. L. (1987) The Element of Artificial Intelligence. Computer Science Press.

46. Turban, E. (1988) Decision Support and Expert Systems. Macmillan Publishing Company.

47. Waltz, D. (1983) Artificial intelligence: An assessment of the state-of-the-art and recommendations for future directions. AI Magazine 4, Fall.

48. Waterman, D. A. (1986) A Guide to Expert Systems. Addison-Wesley.

Address for correspondence: School of Business Administration, MIS Program Development, Pan American University, 1201 West University Drive, Edinburg, Texas 78539, USA.
