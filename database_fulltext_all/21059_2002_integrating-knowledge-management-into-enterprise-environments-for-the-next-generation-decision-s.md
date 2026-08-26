---
otero_id: 21059
otero_key: "AEW9Y66E"
title: "Integrating knowledge management into enterprise environments for the next generation decision support"
authors: "Narasimha Bolloju; Mohamed Khalifa; Efraim Turban"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00142-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating knowledge management into enterprise environments for the next generation decision support

Narasimha Bolloju\*, Mohamed Khalifa, Efraim Turban

Department of Information Systems, City University of Hong Kong, Kowloon Tong, Kowloon, Hong Kong, China

## Abstract

Decision support and knowledge management processes are interdependent activities in many organizations. In this paper, we propose an approach for integrating decision support and knowledge management processes using knowledge discovery techniques. Based on the proposed approach, an integrative framework is presented for building enterprise decision support environments using model marts and model warehouses as repositories for knowledge obtained through various conversions. This framework is expected to guide further research on the development of the next generation decision support environments. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Knowledge management; Decision support; Model marts; Model warehouses

## 1. Introduction

Organizations are becoming increasingly complex with emphasis on decentralized decision making. This trend necessitates enterprise decision support systems (DSS) for effective decision making with processes and facilities that support the use of knowledge management. Kivijarvi [21] highlights the characteristics of such organizational DSS and discusses challenges in design, development and implementation of such systems as compared to one-function or one-user DSS. Ba et al. [3], in their paper on enterprise decision support, point out the knowledge management principles that are necessary to achieve intra-organizational knowledge bases as (i) the use of corporate data to derive and create higher-level information and knowledge, (ii) integration of organizational information to support all departments and end-users, and (iii) provision of tools to transform scattered data into meaningful business information.

In the process of decision-making, decision makers combine different types of data (e.g., internal data and external data) and knowledge (both tacit knowledge and explicit knowledge) available in various forms in the organization. The decision-making process itself results in improved understanding of the problem and the process, and generates new knowledge. In other words, the decision-making and knowledge creation processes are interdependent. Despite such interdependencies, the research in the fields of decision support systems (DSS) and knowledge management systems (KMS) has not adequately considered the integration of such systems.

Proper integration of DSS and KMS will not only support the required interaction but will also present new opportunities for enhancing the quality of support provided by each system. A synergy can be created through the integration of decision support and knowledge management, as these two processes consist of activities that complement each other. More specifically, the knowledge acquisition, storage and distribution activities in knowledge management enable the dynamic creation and maintenance of decision models, in this way, enhancing the decision support process. In return, the application and evaluation of various decision models and the documentation of decision instances, supported by DSS, provide the means for acquiring and storing the tacit and explicit knowledge of different decision makers and facilitate the creation of new knowledge. Such integration is expected to enhance the quality of support provided by the system to decision makers and also to help in building up organizational memory and knowledge bases. The integration will result in decision support environments for the next generation as explained later in this paper. However, there is hardly any guidance, framework or research related to the integration of the interdependent aspects of decision-making and knowledge management. The purpose of this paper is to address this void.

In Section 2, we briefly review the decision-making and knowledge management processes and identify certain similarities and interactions between the two processes. In Section 3, we describe our proposed approach for incorporating knowledge management facilities into a decision support environment. A framework for developing enterprise decision support environments according to the proposed approach is presented in Section 4. In Section 5, we discuss the implications of the proposed approach and propose a framework for conducting research in the fields of decision support and knowledge management.

## 2. Decision making and knowledge management processes

Typical decision making processes are often described as consisting of intelligence, design, choice and an implementation phases [37,41]. Decision makers, individuals responsible for solving problems for the purpose of attaining a goal or goals, expect support in these four phases. Support provided to decision makers by typical DSS, in this regard, has evolved from simple predefined reports to complex intelligent agent-based support. In general, the type of support provided is relatively passive because decision makers are expected to scan internal and external data, and find discrepancies and deviations from expectations invoking ad hoc queries and reports that run on operational databases. Executive information systems (now called Enterprise Information Systems, EIS), have simplified this process by providing data organized at different levels with drill-down facilities through high-level graphical user interfaces. Online analytical processing (OLAP) on data warehouses and data marts [17] provides analytical capabilities required for exploratory information retrieval and problem formulation. Nowadays, OLAP capabilities are being merged with enterprise resource planning (ERP) tools, corporate portals, etc. [38]. Active form of support to decision makers is provided using triggers and alarms on specific attribute values in the databases. Intelligent artificial agent-based support [18,19] is an active form of support where certain manual tasks such as searching and scanning for discrepancies are delegated to software agents. Intelligent agents can be used to support strategic management [10,24], electronic commerce [25,27], and other decision support activities [38]. Data mining techniques assist decision makers in finding interesting relationships or associations that may in turn help in the identification of problems.

Decision makers take decisions based on the information obtained through various means as described above or through DSS built for certain types of decision problems. Fig. 1 illustrates various components of decision making environments and the associated knowledge management activities. Data from internal and external sources, spread across operational databases, data warehouses and data marts are accessed by decision makers using tools supporting OLAP, data mining, EIS, and queries. Decision makers, through the experience of using such tools and techniques, gain new knowledge pertaining to the specific problem area. Specific decision support systems are built using data extracted from various data sources and models extracted from various knowledge sources. Knowledge from internal and external sources may be categorized into functional or general domain knowledge, organizational knowledge, and problem-specific knowledge. Decision makers employ their problem-specific knowledge, in addition to the information and knowledge derived from internal and external data sources using appropriate tools, in arriving at solutions to decision problems. When solutions are evaluated and found effective, the acquired knowledge can be externalized and then embedded into the organizational knowledge, in the form of best practices for example.

![](/api/attachments/AEW9Y66E/fulltext/images/f493d76b879f9f5e023a059a6ec158bad9c72961e0cf15143b23827d6cf912d6.jpg)  
Fig. 1. Decision support and knowledge management activities.

## 2.1. Organizational knowledge creation

The importance of knowledge as an organizational asset that enables sustainable competitive advantage explains the increasing interest of organizations in knowledge management. Many organizations are developing KMS designed specifically to facilitate the sharing and integration of knowledge as opposed to data or information. According to Alavi and Leidner [2], knowledge is not radically different from information. The processing of information in the mind of an individual produces what Polanyi [31] refers to as tacit knowledge. When articulated and communicated, this tacit knowledge becomes information or what Nonaka [28] refers to as explicit knowledge. As organizational knowledge is derived from individual knowledge, KMS must support the acquisition, organization and communication of both tacit and explicit knowledge of employees.

Although KMS supports not only the creation, but also the gathering, organization and dissemination of knowledge, we will focus our discussion on the knowledge creation process, as it integrated with all the others. In order to assist the creation of new knowledge effectively, KMS must support the gathering, organization and dissemination of existing knowledge. Nonaka [28] proposes that new organizational knowledge is created by a dialectical relationship between tacit and explicit knowledge, which emerges into a spiral of knowledge creation consisting of four types of knowledge conversions: socialization, externalization, combination and internalization (see Fig. 2).

![](/api/attachments/AEW9Y66E/fulltext/images/3d85d09674548e76f5ae3bd6adbe722dec2ca7e2a8b1f66b277ae73ade187070.jpg)  
Fig. 2. Nonaka’s model of knowledge creation (adapted from Ref. [28]).

Knowledge externalization refers to the conversion of tacit knowledge into explicit knowledge. This takes place when individuals use ‘‘metaphors’’ to articulate their own perspectives in order to reveal hidden tacit knowledge that is otherwise hard to communicate. Knowledge elicitation techniques can be used to help individuals to articulate tacit knowledge. For example, interviews and focus groups with experienced loan officers can help to externalize certain subjective aspects of the loan approval process that these officers may have never articulated before.

The second type of knowledge conversion, socialization, refers to the creation of new tacit knowledge from shared tacit knowledge. Individuals can acquire tacit knowledge by observation, imitation and practice. In the loan application-processing example, a loan officer trainee can acquire tacit knowledge about the loan approval process by observing other loan officers, or by studying previous applications and their outcome.

Knowledge combination refers to the creation of new knowledge through the exchange and combination of explicit knowledge held by individuals in the organization. The exchange of explicit knowledge could be done through information sharing, e.g., shared documents, databases and model bases. It could also happen through interactions, e.g., meetings, e-mail and casual conversations. The integration of the exchanged knowledge and its reconfiguring through sorting, adding, recategorizing and re-contextualizing can help to create new explicit knowledge. For example, by evaluating externalized loan approval processes followed by different loan officers in terms of risk performance, managers can develop better procedures for processing loan applications.

The fourth type of knowledge conversion, internalization, takes place when explicit knowledge becomes tacit. Nonaka [28] views this conversion as somewhat similar to the traditional notion of learning. Individuals integrate shared explicit knowledge with their prior knowledge in order to update their mental models and produce new tacit knowledge.

## 2.2. Similarities and interactions between KMS and DSS

Certain similarities and interactions can be observed between the decision support environments and Nonaka’s model of organizational knowledge creation.

These similarities and interactions, as we discuss later, form the basis for integration of KMS and DSS. According to Nonaka’s model, the knowledge externalization involves the conversion of tacit knowledge to explicit knowledge. In the context of DSS, this can be viewed as similar to the process of decision modeling, which involves elicitation of problem-solving knowledge from the decision maker and its representation. Similarities can also be found in the combination type of knowledge conversion that generates new explicit knowledge from existing explicit knowledge and the process of model integration in DSS. Knowledge internalization corresponds to the adoption and use of explicit organizational knowledge by individuals. It can be compared to building DSSs using elicited decision models. Last, the socialization type of knowledge conversion may be considered as analogous to sharing information pertaining to decisions made by different decision makers, as such information reflects the tacit models followed by these decision makers (e.g., through group discussions). The interaction between the KMS and DSS includes the application of explicit knowledge created (e.g., decision models) for future decision making and/or for building DSS, and the generation of new knowledge (e.g., best practices) through the use of DSS.

## 3. Proposed approach for the next generation decision support environments

As described in the previous section, decision support and knowledge management are two interrelated and interacting processes in any organization. Integration of DSS and KMS, therefore, is expected to result in several benefits that cannot be realized with any one system. Research related to such integration can identify specific needs and solutions for building the next generation enterprise decision support environments.

Our proposed approach for integrating decision support and knowledge management processes has the three following characteristics that facilitate knowledge conversions through suitable automated techniques:

 it applies knowledge discovery techniques (KDT) for knowledge externalization,

 it employs repositories for storing externalized knowledge, and

 it extends KDT for supporting various types of knowledge conversions.

We elaborate these characteristics using the four types of knowledge conversions in Nonaka’s model described in Section 2. In our proposed approach, we use model externalization, model combination, model internalization and model socialization processes to reflect the integration of decision support and knowledge management aspects. Among these four processes, model externalization is generally considered as the most difficult and time-consuming. Difficulties associated with the model combination process may vary depending on the modeling paradigm used for representation of the explicit knowledge. The other two types of processes, i.e., model socialization and model internalization, are relatively easier to support.

## 3.1. Model externalization

Data in databases, data warehouses and data marts capture a significant amount of tacit models, which are represented by sets of related attribute values pertaining to various decisions. Part of this data consists of decision instances that describe various decisions taken by different decision makers for different decision problems at different times. The model externalization process converts such tacit models (data and decision instances) into explicit models (discovered knowledge and decision models).

The tacit models can be externalized into explicit models by either traditional externalization methods or KDT. Traditional methods require analysts to interact directly with decision makers in order to elicit problem-solving knowledge from them and represent it as part of explicit models using typical knowledge elicitation/acquisition techniques. A second type of method enables the decision maker to externalize their tacit models without the assistance of analysts, using intelligent tools. Some examples of such methods include the usage of knowledge-based tools for model formulation and protocol analysis [5,7,32,34,37,39]. These methods eliminate the tedious and less efficient process of elicitation and representation of the knowledge of multiple decision makers performed by analysts. Using KDT, it is possible to derive decision models using decision instances that represent decision makers’ tacit models. For example, loan approval decisions, recorded in operational databases as business transactions with details of relevant attribute values, can be used for discovering loan approval decision making processes using KDT.

To illustrate the model externalization aspect of the integration, let us consider a classification problem such as categorizing a set of loan applications into approve and reject classes. Let us also assume that application details are available in a database. The decision maker defines the decision problem as a classification problem and identifies the input and output attributes and possible class identifiers. The integrated system guides the decision maker during the problem definition stage. Then, the decision maker starts the task of classifying each application manually and creating the decision instances (applying tacit models). As the decision maker performs the classifications, the system acquires the classification problem-solving knowledge, and tests the acquired knowledge. Once the system learns with sufficient reliability, it classifies the rest of the applications, and presents the acquired knowledge (explicit models) to the decision maker. Any exceptions in the manual classifications made during the process of learning will also be reported. The system finally catalogues the decision problem and the associated explicit knowledge for later reference and use. The entire classification process can span a number of days or weeks or years. The system adapts to the continually changing decision making patterns during longer periods. This type of problem-solving process and support provided can be extended to multiple decision makers working on the same type of decision problem (e.g., loan approval in different branches of a bank) or interdependent decision problems. By combining numerous explicit models of decision making processes of different decision makers, it is possible to generate more complex explicit models.

## 3.2. Model combination

Different explicit models, corresponding to different data and to multiple decision makers solving one or more decision problems, can be combined to generate new explicit models. Model combination in the context of decision making can be performed in two different ways: generalization and integration.

The generalization process aims at abstracting a set of specific explicit models to a generic explicit model for multiple decision problems of similar type. This process reduces the number of models, which in turn can minimize the cognitive load on the users of such knowledge. This is required especially when there is a large number of models representing the various approaches followed by different decision makers for solving the same type of problem. However, it is important to strike a balance between generalization and faithful representation of subjectivity. Generalized models, naturally, may not adequately represent decision makers’ subjectivity, i.e., differences across different models. O’Leary [29] suggests verifying that decision makers have similar views before aggregating individual judgments. A solution to this problem is to cluster or group similar decision models and then generalize within each cluster [9].

The complexity of this generalization task depends largely on the modeling paradigm used. The complexity is least, when all models employ the same paradigm and are generated based on a given set of input and output attributes. Otherwise, generalization needs to be performed either using models of the same paradigm or by translating the models to a common modeling paradigm. It should also be noted that certain modeling paradigms, e.g., multi-attribute utility theory and AHP, are more amenable to generalization than others (e.g., decision trees, fuzzy rules). Treating the decision instances corresponding to a set of decision makers (in a cluster) to generate a generalized explicit model for that group can be a possible solution for generalizing such models. Another difficulty in the generalization process is related to the semantic and structural differences in various model attributes. For example, if different decision makers employ different sets of factors in defining AHP models for evaluating loan applications then it is necessary to unify or resolve the differences prior to the generalization process. This type of difficulty will not arise if a common set of attributes are used (e.g., from a given database schema) in model specification.

While the generalization process creates new explicit models through the abstraction of specific models into generic ones to deal with similar problems, the integration process creates new explicit models by combining different models (generalized or not) that can even be from different domains to deal with more complex problems. Research related to model integration in the field of DSS can be applied for this purpose. Integrating generalized explicit models from different domains provides a better understanding of the interactions between knowledge components belonging to different domains. Explicit models created through model externalization and combination processes will be inputs to the model internalization process.

## 3.3. Model internalization

Model internalization refers to the conversion of shared explicit models into tacit models held by individual decision makers. This is a learning process that results in the modification and possible improvement of the individual tacit models based on best practices. We identify four important activities for supporting internalization. First, the dissemination of explicit models to the decision makers is a requirement for internalization. The effectiveness of this activity depends on the usage of appropriate knowledge presentation methods. Second, facilitating exploratory retrieval of explicit models can help in the provision of relevant knowledge wherever and whenever required. Third, model analysis/evaluation capabilities such as sensitivity analysis (or what-if analysis) that enable the decision maker to compare the effectiveness of alternative models can facilitate the adoption of explicit models and their subsequent internalization. Fourth, assisting the decision maker in adapting and applying shared explicit models. This can be done by building and maintaining the model base component of a DSS for specific decision-making activities. In this particular case, the internalization process becomes more systematic. It is also possible to make this systematic internalization approach continuous by providing realtime adaptive decision support through a dynamic update of the model base.

## 3.4. Model socialization

While model internalization allows decision makers to share, learn, adopt and apply each other’s explicit models, socialization enables them to acquire new tacit models by sharing each other’s tacit models. The knowledge conversion process of socialization refers to the transfer of tacit knowledge through shared experiences. In the proposed framework of

![](/api/attachments/AEW9Y66E/fulltext/images/859f4a72b3f95d68a15536d23dccc92b8d75f1633985c6dbce46fa6268d86ce6.jpg)  
Fig. 3. Proposed framework for enterprise decision support environment with knowledge management.

DSS and KMS integration, decision instances documented in databases, represent the experiences reflecting the tacit knowledge of different decision makers. The documented decisions enable the decision makers to learn from each other’s experiences and modify their own tacit models. For example, in processing a loan application, a loan officer can look for similar cases and their related decisions (documented in the databases) in order to make a decision that is more consistent with previous cases. In doing so, the loan officer is acquiring a new tacit model based on decision instances reflecting the tacit models of other loan officers.

## 4. Enterprise decision support environments with knowledge management

In this section, we present a framework for developing enterprise decision support environments that include knowledge management, for supporting the approach described in the previous section. We elaborate, as part of this framework, on the representation and conversion of the tacit and explicit knowledge, and identify possible difficulties and solutions in various types of conversions. The major focus of this framework is the application and extensions of KDT to support knowledge conversions and enhanced access to knowledge represented by explicit models.

The proposed framework (Fig. 3) integrates the four types of knowledge conversions (see Fig. 2) into various decision support and knowledge management activities (see Fig. 1). The tacit models of different decision makers, represented by decision instances and associated data, are normally stored in operational databases. The relevant data from such databases are used for building an organizational data warehouse employing processes such as extract, filter, condition, scrub, load, etc. [14]. The data warehouse contains information about problems and the corresponding decision instances reflecting the historical and current tacit models of different decision makers in different problem domains. Data marts are subsets of data warehouses created for efficient use of different functional domains. In certain cases, a data mart can be a small stand-alone data warehouse specializing in one area, such as customer data.<sup>1</sup>

In order to facilitate repositories for explicit knowledge created using externalization and combination processes, we propose to use model marts and model warehouses as part of the functional and organizational knowledge bases. We use the terms model mart and model warehouse to define concepts similar to data mart and data warehouse, respectively. However, an essential difference between these parallel concepts is related to the process of building these components. As shown in Fig. 3, data warehouses are usually used to populate data marts, whereas model marts are used to build model warehouses. We propose to use model marts to store the explicit models arrived at using the methods discussed above. These model marts store explicit models of different decision problems belonging to a particular domain (e.g., sales, production). In addition, the model marts also contain the decision models pertaining to different time periods. In other words, we can think of each model mart as capturing the knowledge discovered from data and the problemsolving knowledge of one or more decision makers dealing with one or more decision problems in a certain period. This is becoming important now since companies are using ‘decision matrices’ to empower employees to make decisions in decentralized locations.

Model marts<sup>2</sup> and model warehouses, thus, act as a repository for currently operational and historical decision models, similar to the data marts and data warehouses. The operational models, however, will be in the model base component of various DSS. Each model mart acts as a repository of models belonging to a specific decision-making domain (e.g., inventory management and capital budgeting). Thus, functional knowledge bases include model marts and other forms of knowledge pertaining to the specific functional domain. Similarly, organizational knowledge base includes model warehouse and other forms of integrated knowledge across different functional domains. Problem-specific knowledge bases include model bases of current DSS (e.g., internalized models). These knowledge bases also include necessary meta knowledge (or metal models) required for model manipulation. In the remaining part of this section, we elaborate on the support that can be provided in various knowledge conversions.

## 4.1. Model externalization support

A variety of KDT such as decision trees, rule discovery, neural networks, rough sets, genetic algorithms, nearest neighbor techniques, fuzzy rule discovery, clustering, and link analysis techniques can be used for the externalization purpose. The effectiveness of such an approach using a neuro-fuzzy classifier to discovery fuzzy rules modeling employment selection is illustrated in Ref. [8]. A successful application of the Bayesian network learning model in building and improving a real-time telemarketing DSS application is reported in Ref. [1]. The data mining and knowledge discovery website (http://www.kdnuggets.com/software/index.html) provides links to a number of tools that can be used for discovering rules or models from decision instances.

In our proposed framework, we are concerned about the conversion of tacit models (available in the form of data in databases, data warehouses and data marts) into explicit models. A major part of these explicit models consists of knowledge discovered from large volumes of data. The other part consists of various decision models discovered using the decision instances. In applying KDT to model externalization using decision instances, we should consider certain differences from the traditional application of KDT in databases, which is often performed on large volumes of transaction data such as product sales, service usage, etc. Traditional applications of KDT emphasize the representation, accuracy, interesting results, and efficiency [13]. Important challenges of KDT in such situations include handling of massive data sets, high dimensionality, user-interaction and prior knowledge, missing data, managing changes in data and knowledge, etc. [12]. In model externalization, however, the data set is relatively small, but may contain a large number of attributes reflecting the complexity of tacit models, which often contain both objective and subjective components. Consequently, the emphasis and challenges of KDT for this type of model externalization should be different. Since the data volumes are relatively small, the effectiveness of the process is more important as compared to the efficiency of the process. Accuracy of the explicit model may not be very important because of inconsistencies in tacit models used for discovery. Simplicity of model representation is particularly relevant if the discovered explicit models are to be internalized by decision makers. In this regard, soft computing, which aims to achieve tractability, robustness, low solution cost and high machine intelligence quotient (MIQ) through complementarity of fuzzy logic, neural networks and probabilistic reasons [41], has potential to contribute towards generating concise and easily understandable explicit models.

Two model externalization examples involving discovery of classification decision rules from two different types of data sets representing decisions concerning credit worthiness of applicants and employment preference are illustrated in Appendix A.

A typical model mart, at this stage, may include models representing the decision making processes of one or more decision makers discovered by one or more KDTs and models that are defined manually by decision makers/DSS builders or exported from operational DSS.

Extensible Markup Language (XML) can provide a common structure for representing explicit models of different modeling paradigms. XML databases (http:// www.rpbourret.com/xml/XMLDatabaseProds.htm) can be used for the purpose of creating model marts and model warehouses.

## 4.2. Model combination support

New explicit models can be composed from existing models in model marts and model warehouses using generalization and integration techniques. Generalization should deal with inconsistencies, conflicts, and decision makers’ subjectivity represented in explicit models. As part of the generalization, it may be necessary to unify different explicit models. Unification refers to the process of resolving structural and semantic differences among decision models of the same or different decision problems. This process requires (a) resolving differences between different models of the same modeling paradigm for the same type of decision problem, and (b) integrating different models of the same or different modeling paradigms for decision problems belonging to different domains. We can adapt schema integration and database interoperability approaches [4,23] for this purpose. Johannesson and

Jamil [20] present an approach to integrate two different database schemas by structural and terminological standardization before schema comparison and merging. They contend that knowledge discovery and machine learning can be used to facilitate schema integration. Similar approaches can be applied to the task of unification of model arguments belonging to different domains for integration. Ba et al. [3] review the role of artificial intelligence in model management and model building, and in reasoning with multiple models. In certain cases, it is possible to solve the unification problem involving models of different paradigms by rediscovering the decision models using a specific KDT.

Model marts and model warehouses may include, in addition to the two types identified above, the following as well:

explicit models belonging to a specific domain after resolving the structural and semantic differences with links to the original model,

 abstractions of different explicit models corresponding to a specific type of decision problem, and

 integrated models of different decision problems within a specific domain.

A model warehouse can be built using models belonging to different model marts. In addition, a model warehouse contains models defining further integration across different domains. Unification of model parameters may be required prior to this integration. The model warehouse and model marts support analysis and integration of decision making patterns occurring at different, but related, domains across the organization, cause–effect relationships among different domains, etc.

Implementation of the model marts and model warehouses can be done either as a simple database with tables to describe models together with full text or binary representations of models, or as an objectoriented repository with models represented as objects with the associated behavior. The former type of implementation merely provides storage of models as used/exported by the KDT employed for model discovery. Therefore, any form of analysis involving the contents of the model should also be provided by the KDT. The latter type of implementation, as discussed below, can support more versatile forms of analysis in discovering patterns and trends in models. However, the implementation is dependent on the structure of models and it should provide for relevant operations on the models.

## 4.3. Model internalization support

In Section 3, we have identified important activities that can enhance the internalization process, i.e., dissemination, exploration, analysis/evaluation, and dynamic application of explicit models. These activities enable decision makers to become aware of, understand, learn, adapt and apply each other’s explicit decision models. In doing so, they acquire new tacit models. A number of tools can be used to support the internalization activities. The model dissemination and exploration activities can be supported by model representation and visualization tools as well as intelligent agents that are versatile and autonomous (e.g., [30,42]) for automated discovery of patterns in explicit decision models represented in the model warehouse and model marts. The model analysis/evaluation acti vities can be aided by model analysis systems [11,17, 22,36]. These systems enhance the decision maker’s understanding of the environment represented by the model by assisting in the interpretation and manipulation of the output of the model solvers and in the analysis of existing knowledge and/or extraction of new knowledge concerning the environment represented by the model. By improving the decision maker’s understanding of explicit models, model analysis systems support not only the selection of an appropriate model for the problem at hand, but the learning and subsequent internalization of the selected model as well. Further, evaluation of decisions made and the decision models can result in identifying best practices. Finally, the model application activities can be supported by DSS and adaptive DSS. The usage of a DSS to solve problems is a learning experience by itself that enables the decision maker to acquire new tacit decision models. In addition to specialized tools for supporting the specific activities described above, intelligent tutors can also be used to enhance the overall learning process associated with internalization.

Additional requirements in such decision support environments can be grouped under user interface and interface between various components. The user interface should provide facilities for specification of details to various discovery processes such as inputs, outputs, and tools used for discovery. The ability to specify objectives for model discovery activity (e.g., maximum number of models, minimum level of accuracy) will also be required. In general, the user interface should provide interaction with the system from operational and exploratory perspectives. The operational perspective should provide facilities that are common to many DSS (e.g., data visualization in data warehouses/data marts, finding interesting patterns and associations in data). The exploratory perspective should provide similar facilities on models in model marts and model warehouses. Common facilities between these two modes include intelligent assistance in various tasks, visual specification environment, intuitive graphical user interface, etc. Assistance through intelligent agents that are versatile and autonomous [30,42] for automated discovery of patterns in data and decision models may also be considered. Corporate intranets can both provide an effective medium for dissemination of various types of knowledge.

Facilities for interfacing with other systems should include importing and exporting models discovered to other existing systems, and access to a variety of knowledge discovery and data mining techniques. Approaches such as DecisionNet [6] and the Open DSS protocol [16] for accessing and invoking data mining and decision mining tools over the Internet would be helpful in evaluating and employing suitable tools and techniques.

## 4.4. Model socialization support

The socialization process consists of the creation of new tacit models based on the sharing and integration of existing tacit models. This is mainly achieved through the sharing decision experiences. The experience sharing can be through participation in the decision making process or through the sharing of information documenting the process and its outcome. Therefore, tools for collaborative decision making (e.g., GroupSystems for Windows) and tools for data retrieval and interpretation (e.g., intelligent agents, OLAP and case-based reasoning) can be very useful. The information stored in the data warehouse and data marts representing past problems and the associated decisions can be explored through intelligent agents and examined through OLAP tools in order to identify patterns reflecting tacit decision making processes. Case-based reasoning can also enable decision makers to identify cases similar to the problem at hand and adapt the associated solutions.

## 5. Conclusion

In this paper, we presented an approach for integrating decision support and knowledge management to enhance the quality of support provided to decision makers. A framework for integrating these highly interrelated decision support and knowledge management processes is proposed. Some of the benefits of integrating DSS and KMS include (i) enhanced quality of support provided to decision makers in the direction of real-time adaptive active decision support, (ii) supporting knowledge management functions such as acquisition, creation, exploitation and accumulation, (iii) facilitating discovery of trends and patterns in the accumulated knowledge, and (iv) supporting means for building up organizational memory.

## 5.1. Implications for research

We have described the complementing roles of DSS and KMS in our proposed framework that integrates the research in the respective fields. The approach and the framework proposed in this paper require significant integration of research from various fields, e.g., knowledge discovery in databases, model management in DSS, knowledge-based systems, soft computing, case-based reasoning, intelligent agents, and data warehouses. Some of the challenges in this integration include: (i) representation and storage mechanisms for different types of explicit models, (ii) discovering patterns in explicit models, which is a complex task compared to discovering patterns in databases, (iii) visualization of explicit models and changes in explicit models, (iv) defining taxonomy to assist combination of explicit models of different modeling paradigms to create new models, and (v) extending the applicability of the proposed approach to other types of decision-making situations.

## 5.2. Implications for practice

Many findings and developments in the field of DSS over the past couple of decades and in the field of KMS in recent years are not yet fully exploited. One possible reason for this is the difficulties associated with externalization or modeling process. The approach presented in this paper illustrates the means for automating this difficult task. Using such an approach, it is possible to build integrated DSS and KMS that are better tuned to individual decisionmaking styles. Although this approach poses challenges in integrating different tools and technologies, it helps designers and builders of DSS in minimizing the time and effort required for developing DSS applications. DSS developed following the proposed framework will also enhance the chances of acceptance by decision makers because their subjectivity in decision making is reflected in the decision models.

The externalization process in the proposed approach assumes that the decision instances are available and approximately represent tacit models of decision makers. The models externalized using such instances of a decision maker can, therefore, be expected to result in decisions that are close to or similar to those taken by that decision maker.

Model marts and model warehouses can, in addition to providing decision makers a better understanding of decisions taken, help other decision makers at higher organizational levels to understand current decision patterns and analyze changes in those patterns over long periods of time. Organizations can also use such information for validation of decisions, verification of consistency in decision making, alignment of decisions with organizational objectives and goals, and for training new staff. The proposed framework has potential to support building e-commerce and m-commerce application that are capable of abstracting and generalizing relevant data (e.g., purchase decisions of a customer based on his/her profile) into explicit modes and provide customized response to both existing and prospective customers. Exploiting recent developments in these interdisciplinary fields can lead to the building of enterprise-wide support environments for the next generation that enhance the quality of support provided by DSS and KMS. Considering the three mutually reinforcing trends in data mining speculated by Mitchell [26], the proposed integration could be considered feasible in this decade.

## Appendix A. Examples of model externalization from classification decisions

## A.1. Customer Credit Rating

This example illustrates model externalization using 200 randomly selected decision instances describing customer credit rating provided with Sipina-W for Windows (http://eric.univ-lyon2.fr/ \~ricco/sipina.html). The credit rating data set has 1000 instances with 7 numeric and 13 categorical attributes. Customer profile is captured by attributes such as status of checking account, credit history, purpose of loan application, amount, saving, present employment, etc. A categorical attribute captures the customer credit rating (GOOD or BAD). The following set of rules have been generated using CART method of Sipina-W resulting 69% accuracy on the remaining 800 instances.

R1: if Balance in Checking Account < 0

then Credit Rating = BAD; 75% confidence.

R2: if Balance in Checking Account > = 0 and < 200

then Credit Rating = BAD; 63% confidence.

R3: if Balance in Checking Account > = 200

then Credit Rating = GOOD; 73% confidence.

R4: if Customer has NO Checking Account then Credit Rating = GOOD; 75% confidence.

## A.2. Employment Preference

A neuro-fuzzy classifier, NEFCLASS-PC (2.04 http: //fuzzy.cs.uni-magdeburg.de/nefclass/nefclass.html) was used to extract rules from a small data set consisting of 20 employment offers each with three numeric attributes and a categorical attribute indicating preference for that offer by a final year undergraduate student. The numeric attributes include monthly salary, status of organization and job relevance. The neurofuzzy classifier has generated the following set of fuzzy rules using this data set. The classifier also generated the membership functions (large, medium and small for each input attribute).

R1: if salary is small and orgstat is large and jobrel is large

then preference = hesitate

R2: if salary is large and orgstat is large and jobrel is medium

THEN preference = accept

R3: if salary is large and orgstat is small and jobrel is small

THEN preference = hesitate

R4: if salary is small and orgstat is large and jobrel is medium

THEN preference = hesitate

R5: if salary is small and orgstat is large and jobrel is small

THEN preference = hesitate

R6: if salary is small and orgstat is small and jobrel is small

THEN preference = reject

## References

[1] J.-H. Ahn, K.J. Ezawa, Decision support for real-time telemarketing operations through Bayesian network learning, Decision Support Systems 21 (1997) 17– 27.

[2] M. Alavi, D. Leidner, Knowledge management systems: emerging views and practices from the field, Communications of the AIS 1 (Article 7) (1999).

[3] S. Ba, K.R. Lang, A.B. Whinston, Enterprise decision support using intranet technology, Decision Support Systems 20 (1997) 99– 134.

[4] C. Batini, M. Lenzerini, S.B. Navathe, A comparative analysis of methodologies for database schema integration, ACM Computing Surveys 18 (4) (1986) 323– 364.

[5] H.K. Bhargava, R. Krishnan, Computer-aided model construction, Decision Support Systems 9 (1993) 91 – 111.

[6] H.K. Bhargava, R. Krishnan, R. Muller, Decision support on demand: emerging electronic markets for decision technologies, Decision Support Systems 19 (1997) 193 – 214.

[7] N. Bolloju, Formulation of qualitative models using fuzzy logic, Decision Support Systems 17 (1996) 275 – 298.

[8] N. Bolloju, Decision model formulation of subjective classification problem-solving knowledge using a neuro-fuzzy classifier and its effectiveness, International Journal of Approximate Reasoning 21 (1999) 197– 213.

[9] N. Bolloju, Aggregation of analytic hierarchy process models based on similarities in decision makers’ preferences, European Journal of Operational Research 128 (2001) 499– 508.

[10] C. Carlsson, P. Walden, Strategic management with a hyperknowledge support system, Proceedings of the HICSS’27 Conference, IEEE Computer Society Press, Los Alamitos, CA, 1995.

[11] D.R. Dolk, A generalized model management system for mathematical programming, ACM Transactions on Mathematical Software 12 (2) (June 1986) 92– 126.

[12] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, The KDD process for extracting useful knowledge from volumes of data, Communications of the ACM 39 (11) (1996) 27 – 34.

[13] W.J. Frawley, G. Piatetsky-Shapiro, C.J. Matheus, in: G. Piatetsky-Shapiro, W.J. Frawley (Eds.), Knowledge Discovery in Databases, AAAI Press, Mewlo Park, CA, 1991, pp. 1 – 27.

[14] S.R. Gardener, Building the data warehouse, Communications of the ACM 41 (9) (1998) 52– 60.

[16] D.G. Gregg, M. Goul, A proposal for an open DSS protocol, Communications of the ACM 42 (11) (1999) 91–96.

[17] W.H. Inmon, The data warehouse and data mining, the KDD process for extracting useful knowledge from volumes of data, Communications of the ACM 39 (11) 1996, pp. 49– 50.

[18] N.R. Jennings, M.J. Wooldridge, Applications of intelligent agents, in: N.R. Jennings, M.J. Wooldridge (Eds.), Agent Technology Foundations, Applications, and Markets, Springer-Verlag, New York, NY, 1998.

[19] N.R. Jennings, K. Sycrara, M.J. Wooldridge, A roadmap of agent research and development, Autonomous Agents and Multi-Agent Systems, vol. 1, Kluwer Academic Publishing, Boston, Mass, 1998, 7 – 38.

[20] P. Johannesson, M.H. Jamil, Semantic interoperability: context, issues, and research directions, in: M. Brodie, et al (Eds.), Proceedings of the Second International Conference on Cooperative Information Systems, IEEE Press, Los Alamitos, 1994, pp. 180– 191.

[21] H. Kivijarvi, A substance – theory-oriented approach to the implementation of organizational DSS, Decision Support Sys tems 20 (1997) 215– 241.

[22] R. Krishnan, Model management: survey, future research directions and a bibliography, ORSA CSTS Newsletter 14 (1) (1993) 1 – 22.

[23] W. Litwin, L. Mark, N. Roussopoulos, Interoperability of multiple autonomous databases, ACM Computing Surveys 22 (3) (1990) 267– 293.

[24] S. Liu, Business environment scanner for senior managers: towards active executive support with intelligent agents, Expert Systems with Applications 15 (1998) 111 – 121.

[25] P. Maes, et al, Agents that buy and sell, Communications of the ACM 42 (3) (1999) 81 – 91.

[26] T. Mitchell, Machine learning and data mining, Communications of the ACM 42 (11) (1999) 30 – 36.

[27] R. Murch, T. Johnson, Intelligent Software Agents, Prentice-Hall, Upper Saddle River, WJ, 1999.

[28] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5 (1) (1994) 14 – 37.

[29] D.E. O’Leary, Determining differences in expert judgement: implications for knowledge acquisition and validation, Decision Sciences 24 (2) (1993) 395– 407.

[30] S.D. Pinson, J.A. Louca, P.A. Moraitis, Distributed decision support system for strategic planning, Decision Support Systems 20 (1997) 35– 51.

[31] M. Polanyi, Personal Knowledge: Toward a Post-Critical Philosophy, Harper Torchbooks, New York, 1962.

[32] S. Raghunathan, R. Krishnan, J.H. May, MODFORM: a knowledge-based tool to support the modeling process, Information Systems Research 4 (4) (1993) 331 – 358.

[34] A. Sen, A.S. Vinze, S.F. Liou, Construction of a model formulation consultant: the AEROBA experience, IEEE Transactions on SMC 22 (5) (1992) 1220 – 1232.

[36] D.M. Steiger, Enhancing user understanding in a Decision Support System: a theoretical basis and framework, Journal of Management Information Systems 15 (2) (1998) 199– 220.

[37] S.-F. Tseng, Diverse reasoning in automated model formulation, Decision Support Systems 20 (4) (1997) 357 – 383.

[38] E. Turban, J. Aronson, Decision Support Systems and Intelligent Systems, Prentice-Hall, Upper Saddle River, WJ, 1998.

[39] A.S. Vinze, A. Sen, S.F. Liou, AEROBA: a blackboard approach to model formulation, Journal of Management Information Systems 9 (3) (1992) 123 – 143.

[41] L.A. Zadeh, Fuzzy logic, neural networks and soft computing, Communications of the ACM 37 (3) (1994) 77 – 84.

[42] N. Zhong, S. Ohsuga, C. Liu, Y. Kakemoto, X. Zhang, On meta levels of an organized society of KDD agents, in: J. Komorowski, J. Zytkow (Eds.), Principles of Data Mining and Knowledge Discovery, Proceedings of PKDD ’97, Springer-Verlag, New York, NY, 1997, pp. 367 – 375.

![](/api/attachments/AEW9Y66E/fulltext/images/a4252d8ce89cd14b06c08d12923eee46943a76bafb63afd3b7eabfa42db61462.jpg)

Narashima Bolloju is an Associate Professor of Information Systems at the City University of Hong Kong. Dr. Bolloju received his PhD in Computer Science from the University of Hyderabad, India. He has over 13 years of experience in the IT industry on many information systems development projects in India, Syria, Egypt and Mauritius prior to joining City University in 1993. His current research interests are in decision modeling,

knowledge discovery and data mining, knowledge management, and object-oriented systems. He has published articles in European Journal of Operational Research, Journal of Database Management, Decision Support Systems, and Journal of Object-Oriented Programming.

![](/api/attachments/AEW9Y66E/fulltext/images/044a8272a8ebfda32de10fa3768e6bd035e9d10a6628fe1f071bc2ec70649364.jpg)

Efraim Turban is a Visiting Professor of Information Systems at City University of Hong Kong. Previously, he served on the faculty of several universities including the University of Southern California and Florida International University. Dr. Turban is the author of several major textbooks in Decision Support Systems, Information Technology for Management, and Electronic Commerce. He has pub-

lished close to 100 papers in leading journals such as Management Science, MIS Quarterly, and the Journal of MIS. Dr. Turban’s current research interests are in the development and use of electronic commerce applications.

![](/api/attachments/AEW9Y66E/fulltext/images/5a0391ce1fac29610a0fe1c2c5b323e0cbabf857b8bfcbbb334439d87b6976c2.jpg)

Mohamed Khalifa was educated at the Wharton Business School of the University of Pennsylvania and received degrees in MA in Decision Sciences and a PhD in Information Systems. His work experience includes 4 years as a business analyst and over 10 years as an academic in the United States, Canada, China and Hong Kong. At present, he is an associate professor at the Information Systems Department of City

University of Hong Kong. His research interests include innovation adoption, electronic commerce and IT-enabled innovative learning. He has published books and articles in journals such as Communications of the ACM, IEEE Transactions on Engineering Management, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems, Data Base and Information and Management.
