---
otero_id: 21371
otero_key: "R86T2BG2"
title: "Using client-broker-server architecture for Intranet decision support"
authors: "Sulin Ba; Ravi Kalakota; Andrew B. Whinston"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00055-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using client-broker-server architecture for Intranet decision support

Sulin Ba $^{a}$ , Ravi Kalakota $^{b}$ , Andrew B. Whinston $^{c,*}$

$^{a}$ School of Business Administration, University of Southern California, Los Angeles, CA 90089-1421, USA

$^{b}$ Simon School of Business Administration, University of Rochester, Rochester, NY 14627, USA

$^{c}$ Department of Management Science and Information Systems, CBA 5.202, The University of Texas at Austin, Austin, TX 78712, USA

Received 30 June 1995; revised 15 February 1996; accepted 30 May 1996

## Abstract

Electronic commerce is emerging as a key enabler in changing the way companies do business. This paper focuses on the aspects of electronic commerce that are pertinent to Intranet decision support and tries to develop the theory and technical requirements that will drive the implementation of such a decision support system. The main objective is to achieve information integration using the brokers, World Wide Web, and structured documents. The implementation of a prototype system is described and results from its usage are presented.

Keywords: Decision support systems; Intranets; MIS broker; Intermediation

## 1. Introduction

Electronic commerce is emerging as a key enabler in changing the way companies do business. For the purpose of this paper, we define electronic commerce as the ability to carry out “information-related” transactions between clients, intermediaries, and servers over computer networks $[18]$ . Electronic commerce is expected to allow firms to cut costs while, at the same time, improving the quality of goods and services, and increasing the speed of service delivery. While the statement remains to be proven empirically, early results demonstrated in this paper and $[20]$ seem positive.

In this paper, we focus on the aspects of electronic commerce that are pertinent to organizational decision support, which is very decisive for companies around the world as they transform themselves for competition that is based on information $[21]$ . The computing model behind electronic commerce and concomitant decision support systems is quickly changing. Even as the organizational decision support world struggles to move to client/server computing, a new model based on the World Wide Web $[5]$ has emerged: network centric computing. In this model, computing, communication, and distributed databases converge, and the integration of these elements becomes the focal point. Within this scenario, several key decision support research trends are becoming important:

\- Faster access to a diverse set of content as well as improvements in the underlying infrastructure have caused an increase in complexity with which end users are faced. This requires new ways of modeling of users, tasks, and information so that software can decide what to search for and how to integrate search results.

\- The magnitude of content available is so great that it is hard to process, resulting in an increase in information overload for the end user. This requires new methods of organizing information that are appropriate for the decision support task and for the computing environment in which it is carried out.

\- The problem of displaying information to the user is complicated by the user's mobility, the wide range of display devices that may be available, and the constraint that task execution not be adversely impacted. Determining the most appropriate methods of display through format negotiation, translating between one representation and another, and integrating new information in the framework of documents are all challenging research problems.

Apparently, the delegation of tasks is an important response to the above trends, because through delegation the desktop, server, and the middle-ware (underlying network infrastructure) can assume more of the end user's work. For example, software can enable tasks to be carried out on behalf of users, with guidance rather than direct control by the user. Also, software can take on the responsibility for content search, retrieval and filtering. It can also personalize human-computer interaction. Increasingly, software agents (or brokers) are the intermediaries which implement this delegation, thus managing complexity and information overload, and supporting user mobility. Web-based brokers can best be thought of as a design model, much like client/server computing, rather than a technology or a product offering. Though integration of brokers into decision support applications or services requires a mindset change, this new model is expected to be one of the key computing paradigms [17].

The focus, in this paper, is on the development of a client–broker–server architecture that will enhance the ability of managers to conduct effective and coordinated operations that are fundamentally determined by their ability to access and utilize the right information at the right time. Managers need to be able to understand as accurately as possible all important factors regarding their own situation, including but not limited to the disposition of competitors. The totality of the information relevant to management is referred to as the operational / strategic picture [19]. The broker idea is developed to encapsulate the notion of intermediation between distributed information sources and information users, the task of which is carried out by a centralized MIS group who is equipped with software agents that perform various broker functions. We call this MIS group the “MIS broker” [1]. This paper focuses on the decision support aspect of the MIS broker. The objective of our client–server–broker architecture is to provide managers with the most accurate, comprehensive, and consistent picture that technology will allow, under the presumption that the improved operational/strategic picture will improve the ability of the company to conduct operations effectively and efficiently.

The rest of the paper is organized as follows. Section 2 explains the roles that Intranets, intermediation, and structured documents play in our framework. Section 3 explains the concept of the MIS broker and lays out the client–broker–server infrastructure needed for Intranet decision support. The agent technology and the use of software agents in our design are explained in Section 4. Section 5 addresses the issue of how to find information using various directories. In Section 6, we discuss how to organize the knowledge base and how to represent information using the structured document method. Then in Section 7 we demonstrate through an example how the system composes decision models to answer user queries. Section 8 concludes the paper with future research directions.

## 2. Intranets, intermediation, and documents

Future decision support applications will clearly have the capability to draw upon varied and voluminous sources of data and documents that might potentially have relevance to corporate planning, crisis management, or day-to-day operations. In addition to conventional sources of information such as text messages and data such as manufacturing/production data, managers will have access to the burgeoning “infosphere” of publicly-accessible documents (e.g., product specifications, financial accounting data – Securities and Exchange Commission’s EDGAR database) and proprietary company-specific information databases (e.g., financial, manufacturing, customer data) that the interconnected internal and external networks are rapidly making available. Rapidly improving data acquisition capabilities will be able to collect enormous quantities of information regarding conditions in the business environment. This information, together with the vast information resources linked to the Intranets, represents a data mining, filtering, and display problem of substantial magnitude. It is not the objective of this paper to devise the technology for amassing information, but rather to maximize the utility of existing information to managers. The three technical elements that need to be understood in maximizing the utility of distributed information include: Intranets, intermediation, and documents.

## 2.1. Intranets and decision support

Intranets are corporate TCP/IP networks with World Wide Web (WWW) servers inside a firewall. Intranets, with the large bandwidth they have available, seem an ideal environment for applications that assume a high degree of business process integration while allowing decoupling of software functionality so that cross-platform client/server applications are a reality. Many corporations have been quick to realize the benefits of the World Wide Web architecture (such as easy and rich information access for customers) and that the same methods and techniques can be applied to the internal distribution of their corporate or departmental information. Consequently, there has been an explosion of internal Web sites and servers – behind the corporate firewall.

Intranet applications generally fit into the following categories [31]:

1. Electronic publishing. One-to-many communications where teams, departments, or individuals can set up HTML (HyperText Markup Language) pages where they post information, reducing bulky, easily outdated paper-based information. For instance, Intranets are used for the publication of corporate information, such as product review meeting minutes, telephone lists, personnel information, product specifications, and price sheets. These applications reduce the costs of producing, printing, shipping, and updating corporate information.

2. Collaborative applications. Many-to-many interactions, for example, WWW-based chatrooms, newsgroups, and collaboratories, that facilitate direct exchanges of information between members of a group, making information available to others within the group.

3. Transaction applications. Two-way interactions, such as interacting with legacy data, downloading software, or information inquiry. The goal of transaction applications is the seamless linking of multiple legacy databases with Web access at the front end. With such applications, corporate databases will be available from anywhere, and individual pieces of data coming out of one database will be identified as hyperlinks which will pull related information out of another database.

While categories (1) and (2) have seen a majority of the implementations, category (3) which essentially falls under decision-support, has been relatively unexplored. Intranet decision support is becoming increasingly complex and is motivated by operational requirements such as rapid response to customer orders (reduced restocking time), global sourcing and procurement, quick resolution of supply chain management problems, and high levels of customer service (firefighting). Clearly, operational decision-making and the data needed to back those decisions have assumed a crucial role in every organization. It appears safe to conjecture that an important part of Intranet-based electronic commerce implementations will be aimed at corporate decision support [18]. Unfortunately, while the business requirements and constraints for operational decision-making are becoming increasingly stringent, very little prior work has been done in developing the theory and technical requirements that will drive the implementation of the next generation of Intranet decision support for on-line analytical processing. In this paper, we address these issues.

Clearly, one of the challenges for building Intranet decision support is finding ways to integrate information across the enterprise. Information integration, while a major research problem in the past, does seem to be less daunting in the presence of new technologies such as the World Wide Web $[5]$ and sophisticated browsers such as Netscape $[16]$ . It is especially true when organizational knowledge becomes more and more embedded in multimedia documents and enterprise computing becomes more document oriented. The transparency of the integration process is what makes the WWW technology so effective. This transparency is further enhanced by the use of the intermediation concept.

## 2.2.Intermediation

To facilitate information integration and transfer from the information sources to the clients, we propose the notion of intermediation. Intermediaries are economic brokers that stand between the parties of a contract (or transaction), usually buyers (clients) and sellers (servers), and perform functions necessary to the fulfillment of a contract. A strict interpretation of the definition of an intermediary generally includes most firms in the financial service sector: banks, insurance companies, mutual funds, and venture capital firms. In the financial world, intermediaries or brokers have existed for many years, and, in fact, they have become an indispensable part of many financial transactions. The proliferation of financial brokers is based upon the efficiency with which they can serve the needs of both would-be lenders and would-be borrowers $[10,27,29]$ . The efficiency comes from the many resources the brokers can pool together, which helps them develop specialized knowledge and achieve the economy of scale.

Whether a strict financial or electronic interpretation is adopted, it is clear that intermediaries comprise a very significant portion of any on-line economy. Early examples of intermediation in electronic commerce can be seen in the information search (e.g., Lycos – http://www.lycos.com) and payment processing areas (e.g., First Virtual Payment System). Clearly, understanding the forces that give rise to the demand for intermediaries as well as the characteristics and the structure of intermediated on-line markets is crucial to the overall understanding of the operation of electronic markets.

Fig. 1 illustrates the extension of work in intermediation to the DSS field. We develop the intermediation idea to encapsulate the notion of MIS groups that will act as a central brokerage and serve as the intermediary between distributed information sources and information users. The key insight is that companies, through the MIS broker, will be able to effectively integrate and automate the processes underlying decision support tasks.

![](/api/attachments/R86T2BG2/fulltext/images/e132cb7b541feb949ec81baa8917fdb21ed789c924e7d8b23f46e939d38e0139.jpg)  
Fig. 1. MIS organization as a broker.

The MIS broker provides a centralization of key functionality that may be useful to several departments. This centralization is important as it avoids the duplication of effort and provides economy of scale.

The need for an MIS broker is apparent when one acknowledges that organizational knowledge is dispersed across many locations and on many different computing platforms. These knowledge entities were not developed to fit one particular requirement but a broad set of problems. Current decision support technologies take whatever the user submits and answer very ad hoc questions. However, in many decision situations, the user does not necessarily know where the relevant information resides that is critical for problem solving. The system, therefore, needs to have the capability to find the information and pulls the information together in a meaningful way. Therefore, it is able to serve its customers, i.e., the functional departments, with a knowledge that those customers are not likely to possess. That is why we need to have an MIS broker that is capable of mediating information finding and problem solving.

## 2.3. Structured and compound documents

Organizations have become more and more distributed, ensuing in dispersed information sources. In this environment, management needs to make decisions quickly based on limited and often incomplete information fragments. It is important to note that these managerial decisions are not done in isolation (or cannot be ad hoc) and will require later justification as decisions might have ramifications. However, using on-line information for decision making is made more challenging by the heterogeneity of the underlying document formats, retrieval protocols and client front-ends.

Why are documents important in developing decision support systems? Over the years, digital documents have become more feature laden, varied, and mission-critical for organizational work. The term digital document has come to encompass a wide variety of knowledge forms including text (reference volumes, books, journals, newspapers, etc.), illustrations, tables, mathematical equations, scientific data, scanned images, video, voice, hypertext links, and animation $[8]$ . A document need not be a single file, but rather a collection of pointers to data objects, images, and so on. An example of such a document type is HTML documents. More recently, with advances in applet design and implementation $[9]$ , the components of a document can be dynamically linked to remote documents and updated with fresh content. In short, it is quite clear that documents are no longer merely an electronic analogy to paper, but rather dynamic, multimedia knowledge bases.

However, decision support systems research has largely ignored digital documents as a processable entity. [33] estimates that at least 80 percent of corporate information is in the form of digital documents, as opposed to structured database records. Traditionally, document management systems were designed to help individuals, workgroups and large enterprises manage their documents stored in electronic form. These systems provide a means to store, easily locate and retrieve, and exercise control over document-based information through the document's life cycle within the context of a group or large organization. However, there exists a gap as document management systems do not deal with decision support requirements. Clearly, any Intranet decision support system that seeks to provide accurate view of the operations must incorporate document management functions. In this paper, we provide insights into how such integration might occur.

## 2.3.1. Documents as a representational framework

Documents serve as a representational framework for decision models. This includes model generation and model visualization. In most of the existing decision support systems, mathematical models are tightly integrated with the execution environments such as SAS, SPSS, Mathematica, spreadsheets, optimization systems, or linear programming systems such as GAMS. This tight integration has two drawbacks: (1) models are not interoperable and (2) models cannot be reused or customized easily. Although prior work has tried to address this problem $[4,6,7,12,22]$ , no consistent body of knowledge has emerged due to difficulty of creating generic model representations that can be mapped onto target environments at runtime.

The growing need for customization forces developers to represent models as documents that are structured in a way that document elements not only can be used as building blocks in other models but also can be transformed into the target formats for execution and visualization. An example of documents being used for interoperable model representation is Virtual Reality Modeling Language (VRML). VRML $[32]$ allows the development of 3D models on the World Wide Web. The rationale for this can be gleaned from the statement by Negroponte $[30]$ :

In the long run, model-based image transmission and encoding are better than transmission of pictures alone. Mathematical models of a scene can describe the spatial relations of the objects in it and maneuver them through space. The idea of capturing a picture with a camera is obsolete if one can instead capture a realistic model from which the receiver can generate any picture. For instance, from a real-time model of a baseball game, a fan watching at home could get the view from anywhere in the ballpark – including the perspective of the baseball.

There are three issues involved in how to find a generic document representation that would allow the decision models generated on the fly to fit the demands and needs of target environments. First, how to represent the content and the logical structure of a document? Second, how to use documents or document components as building blocks to generate decision models? Third, how to negotiate an appropriate format so that the decision model would fit into the target environment?

To address the first two questions, we need to look at the implementation framework of decision models – the structured compound documents. The third question will be addressed in Section 4 where we talk about interface agents.

## 2.3.2. Structured documents as an implementation framework

Because of the heterogeneity of the Web in terms of both applications and computing platforms, structured documents (e.g., HTML) are being used to describe a wide variety of content. The structured document is a data encoding mechanism that allows the information in documents to be shared, for example, by applications for electronic delivery, database management, computer-aided design, or manufacturing $[15]$ . This method recognizes that data, structure, and format are separable elements. It preserves the data and the structure, but does not specify the format of the document, recognizing that format should be optimized to user requirements at the time of delivery. Therefore, by tagging data with their role and any other useful identifiers, structured documents allow information to be readily located and reused. That is, document reusability and interoperability of applications are the key benefits that structured documents allow as evident in the success of the World Wide Web.

In decision support systems, structured documents serve as an implementation framework that helps build knowledge bases or corporate digital libraries $[2,14,24,25,35]$ . These knowledge bases facilitate inter-application information exchange as more and more corporate information is being stored in documents format rather than relational databases. By implementing corporate knowledge bases centered around structured documents, companies are better able to provide fast-cycle responses with integrated information sources. We will explain in Section 6 how to internally represent structured documents to facilitate information integration.

## 2.3.3. Documents as a compound entity

Recently, documents are being used as an organizational framework to encapsulate distributed objects. Examples of this approach include Microsoft's Object Linking and Embedding (OLE), Apple's OpenDOC, and Common Object Request Broker Architecture (CORBA). The major difference between structured and compound documents lies in the content that can be embedded in each. Structured documents are primarily representational structures whereas compound documents are more active entities and often link the data to a remote parent application.

Prior work has shown that the organizational knowledge base is a repository of documents whose purpose is to provide a resource of sharable and reusable document fragments for helping to better understand, explain, and predict organizational phenomena in a variety of different situations. The notion of compound documents is especially useful when one considers the fact that constructing large monolithic documents in the organizational knowledge base is not a practical solution. In the context of DSS, compound documents can be decision models that are linked to decision support systems that process the models.

However, to be really effective a flexible decision support system is needed that composes decision models in the framework of compound documents in response to user queries. In other words, the system should be able to construct compound documents from documents and model fragments that serve as the basic building blocks. The better utilization of documents and the effective composition of documents in strategic and operational decision making processes involve effective on-line search and retrieval of documents in a distributed environment.

Prior work has been done on how to organize a distributed organizational knowledge base and how to compose compound documents for decision models. Ba et al. [3] developed a framework, based on the compositional modeling approach [13], that shows how to improve model building and how to extract the relevant document fragments from the knowledge base to compose a compound document in response to a user query. Knowledge pieces are in some way related to each other. Documents normally have their own application context. Logical links need to be created in the knowledge base among documents. When one document or some part of a document is pulled out, supporting information will also be presented to users. For example, when compound documents are assembled to answer user queries, underlying assumptions (which is the supporting information) have to be taken into account for each document. Sometimes, multiple compound documents (decision models) might be built to answer one single query. Then evaluation mechanisms become necessary to evaluate alternative compound documents and give explanations or justification to each decision model. More work is needed in DSS that examines the provision of strong explanations and justification. In sum, a compound document, as a compositional entity, should be able to capture all and only the relevant information for each decision problem.

## 3. The client-broker-server architecture for Intranet DSS

To address some of the issues put forth in last section, we present in Fig. 2 a client-broker-server DSS architecture that revolves around the notion of the MIS broker that performs value added services by linking information together with services. The need for an MIS broker is obvious when one considers the deficiencies of current technologies (WWW, gopher, and even anonymous FTP) that make reproduction and transmission of data fairly fast and cheap, but do little or nothing to help decision support systems find or execute documents. All of them present basically the same abstraction, namely a hierarchy of files, but do nothing to help the application understand the structure of a file within a hierarchy. Clearly, existing information services provide little in terms of services that organize and structure the underlying document collection. Also, every server site is different in the way the documents are structured. But even if every site on the Intranet organized its document collection identically, it would not be enough, because every site also has its own conventions for naming files, indicating data formats, and making searchable indices.

![](/api/attachments/R86T2BG2/fulltext/images/43c5006c8a688fae1b1c205d806200b2cbe59e85a9590c4a313a1002556ef6a8.jpg)  
Fig. 2. The client-broker-server architecture for Intranet decision support.

To alleviate the above problem, the MIS broker maintains enterprise wide knowledge about what information is available and where, and how various information sources are organized. It acts as a central knowledge facilitator that interacts not only with each functional department within the company, but also with outside brokers from other companies when outside information is needed. Clearly, information organization/integration is central to broker effectiveness.

The broker provides three distinct forms of integration. The first form of integration is the ability to link data provided by different servers by using Uniform Resource Locator (URL) $^{1}$ . Broker-based documents, expressed in HTML, can contain the URLs of other documents. Browsers typically display these references, called hyperlinks, as special regions called anchors. An anchor can be a section of highlighted text or an icon. When the user clicks on an anchor, the browser retrieves the document referenced by the underlying URL. The newly retrieved document can come from a server located across the globe both from the client and from the server that provided the document containing the anchor.

The second form of integration is the ability to provide clients with data from diverse sources. Brokers integrate diverse sources of data by supporting several Internet data access protocols in addition to HTTP (Hypertext Transfer Protocol). Web servers and Web browsers support this form of integration in different ways. Web servers integrate diverse data sources of data by allowing Common Gateway Interface (CGI) programs to run in response to client requests; CGI programs perform general computations including accepting form data, communicating with other computers, and creating dynamic pages. This way, for instance, a Web server can provide clients with data obtained by running transactions on a legacy mainframe system. In such a scenario the Web server acts as a gateway, translating from the new standard for interactive information access (HTTP) to a previous one (3270 terminal protocols).

The third form of integration is the ability to encompass new types of data. The HTTP protocol borrows a design for extensible data typing and type negotiation from the Multipurpose Internet Mail Extensions (MIME) standard. Browsers are designed to support new data types via helper applications that a user can add to the browser. This is how Web browsers deliver audio, video, and PostScript data to users today. The broker needs to be prepared for whatever new data types that become important in the future.

However, the information organization problem is complicated by the need to have access control mechanisms to protect company confidential information and to eliminate unwarranted access. This would require constantly monitoring or auditing: Who in the company have authorization to access certain types of information? What information can be provided to the workforce? This requires Web-based directory structures that have embedded access control mechanisms much like Lotus Notes.

In sum, the broker acts as the intermediary between information and information users. It handles all the queries transparent from users and gathers information from different servers before returning a sensible result to the end user. There are five basic elements in our architecture:

\- Web clients equipped with a Web browser (interface agent) (for example, Netscape, HotJava) for information display. Each client could be a PC, a Mac, or a UNIX machine.

\- Software agents (information retrieval agents and gateway agents) that use, gather, and compute information.

\- Directories that facilitate information retrieval processes. They contain model information, solver information, and data information (structured documents, relational database, etc.).

\- The knowledge base that is a distributed library of DSS related documents and databases. Each functional department in the company maintains its own server that contains the department specific information. For example, in Fig. 2, Server 1 could be an accounting server that is located in New York, Server 2 could be a manufacturing server located in Malaysia.

\- The MIS broker that maintains directories of enterprise wide information and facilitates information integration.

The role of the broker becomes clearer after examining the following procedure that shows how a typical query is processed.

1. The end user initiates a query from a client interface agent that parses the query and sends it to the broker;
2. The information retrieval agent on the broker checks the directories (to find out what information is needed for the query and which servers contain the necessary information) and extracts the relevant information to a temporary file, then the broker initiates HTTP requests to the servers that need to be contacted;

3. Upon receiving the requests, each HTTPD server starts up the gateway agent and passes the input to the gateway agent, who then processes the request, checks its local directories (either data directory, model directory, or solver directory) on the server to get the detailed information needed, and returns the result (an HTML document, a set of data from a database, or a URL address, etc.) to the broker;

4. The broker composes compound documents as decision models, executes the models using appropriate solvers, and returns the results to the end user.

We will explain the different components of this architecture in the next few sections.

## 4. Software agents as brokers

Software agents play a very important role in our Intranet DSS framework. They help minimize major information problems that hamper decision-making efficiency in the networked environment. Basically, a software agent is a program that embeds knowledge that drives its actions. This knowledge is described in the form of goals that lay out both the objectives for the agent and the manner in which it will perform its tasks $[28,34,36]$ . The software agent should also contain the supporting information that may include the type of data and the languages that the agent understands. In our architecture, we have three kinds of agents: interface agents, information retrieval agents, and gateway agents.

## 4.1. Interface agents

Sitting on each client is an interface agent or a set of interface agents that is responsible for knowledge base query and information presentation, the problem of which is complicated by the wide range of display devices that may be available. In other words, the interface agents need to perform two tasks: query processing and information presentation.

On the query processing side, ideally, we would like to have interface agents that are capable of handling natural language queries. Users can enter their query in an appropriate HTML form from which the interface agent extracts key requirements and passes them over to the broker as the basis for query processing. Research in the artificial intelligence area has made significant progress on natural language processing $[11,37]$ that could serve as the starting point for our interface agents in terms of handling user queries. For now, we can have a set of HTML query forms that may be somewhat ad hoc but are easier for interface agents to process.

For information presentation, we need to realize that multimedia information may be retrieved in many forms, some of which may not be suitable for display on available devices. For example, some devices may be unable to display pictures, while others may not provide audio. Determining the most appropriate methods of display, translating between one representation and another, and integrating new information with the existing information are the tasks of interface agents which involve content negotiation.

Content negotiation is the process whereby a WWW server provides different data depending upon the capabilities of the browser and preferences of the user. The data may take the form of different graphics and sound formats or different HTML pages.

Why is this an important problem? The Intranet is on the verge of exploding its content base with a slew of new data types. Today, most Web sites are not much more than HTML pages with GIF's and maybe an audio or MPEG file. This is rapidly changing. We are seeing Adobe Acrobat, Standard Generalized Markup Language (SGML), Virtual Reality Modeling Language (VRML), and Java, and other data formats take hold as support for them in popular browsers emerges. We will also see decision model formats emerge as more and more DSS take advantage of the Web architecture. Therefore, with an explosion of data types, there is a need for a way for browsers and servers to negotiate for content. Negotiation is a way for browsers to tell servers, for instance, “I know how to render MRP data files”, and also a way for servers to tell browsers “There are two versions of this data files available (MRP 1 and MRP 2) – take your pick”.

There are two main ways of deciding what material a browser can interpret: Accept Headers and User Agent Header.

Accept Headers is the type of content negotiation currently supported by the Apache HTTP servers and almost all browsers. This header field is sent to the server to inform it what types of data the browser can view. This allows a server to provide data that the browser can use. This is normally used to send data when graphics formats are involved. This mechanism does not allow for more complex interaction such as providing data based on whether the browser supports HTML tables.

User Agent Header is an alternative method of determining what features a browser supports. The User Agent Header can be used to determine what browser an end user is using. However, any further details of the browser must be looked up in a database. This method has two problems. First, with constantly evolving browsers, the local scripts or databases will have to be constantly updated to keep up with browser innovation. This puts enormous strain on people managing the servers. Furthermore, with plug-ins, the server can not always know just from the User Agent Header what the browser can handle. For example, just because a server receives a hit from a Windows Netscape 2.0 does not mean the server can be sure that they have the Java plug-in. In sum, content negotiation is necessary to maximize the utility of the Web architecture and to prevent content wars.

## 4.2. Information retrieval agents

Information is not very useful if the agent cannot find it. It is well known that navigating over the Internet can be a very time-consuming task, resulting in a rather high search cost for the user, especially when the user has to access many servers for the right data that matches the query. To solve this problem, we need information retrieval agents that interact with different directory services to help minimize information search costs for the end user in a distributed environment. Currently, there are already some information retrieval agents (also called search engines) on the WWW which search Web sites world-wide, for example, Yahoo and Lycos. These search engines return all the documents that contain the keywords submitted by the end user. They, however, do not indicate how relevant the documents are or whether there are any connections among the documents returned, which creates a very difficult task for the end user. That is, the end user has to go through all the documents to determine which ones are related to his particular query, whether the documents are related to each other, and if so, how are they related to each other. In a distributed decision support system for the electronic marketplace where fast or even real time problem solving is crucial, the information retrieval agents with only the primitive functions are simply not adequate.

Therefore, one fundamental requirement for the information retrieval agent in our framework is that it be able to interact with different directory services in a way that it finds not only the documents or data that contain the keywords in the query, but also the supporting documents that provide possibly different perspectives in answering the query. Moreover, the relationship among the documents should be indicated as well to the end user. To accomplish the above tasks, sophisticated directories will be required to accompany the information retrieval agent.

## 4.3. Gateway agents

The platform on which our framework is built, i.e., the World Wide Web, requires that the information sources on different servers be directly TCP/IP-accessible or fit the Web environment. However, this is often not the case because a large component of our knowledge base may consist of data that comes from relational database, for example, an Oracle database, or the data may be generated dynamically. Therefore, appropriate gateway agents, i.e., external programs, are needed to make an information source such as an Oracle database file which does not fit the Web mold look to the Web browser like a file on the Web server $[26]$ . That is, gateway agents provide a collection of services that supply basic functions for interacting with the Internet. Common Gateway Interface (CGI) is the mechanism that allows users to run the gateway agents under an information server, such as a Web server. They can send e-mail, generate HTML outputs, or return the URL address of another file. In practice, gateway agents are programs that handle information requests and return an appropriate document or generate a document on the fly.

For example, if a user at the accounting department of the company is to input some data into a relational database using the Web interface, which is the client interface for our client–broker–server architecture, he would fill out an HTML form that will be parsed by a CGI gateway agent into an SQL call which in turn will be sent to the relational database. When end users need to retrieve data from this database, another CGI gateway can format the output of the database query as an HTML document and pass it along to the user for viewing through the HTML browser.

## 5. Directories

Earlier, we pointed out that information retrieval agents are needed to find information. For the agent to perform efficiently and effectively, it must have the knowledge of what is available and where. This takes the form of directories which tell the agent where information is located in the vast network environment. Directory structures containing the “what-is-where” information need to be imposed on the collections of information which not only indicate which information sources may have the information being sought, but also how the information is related to the query.

There are four kinds of directories in our approach: (1) the broker directory, (2) data directories, (3) model directories, and (4) tool directories.

The broker directory, as the term suggests, is a directory that is maintained by the MIS broker and serves as a starting point for query processing. It is the main directory that keeps information on what documents, what data, or what decision models are available, where they are located, and how they are related. That is, it keeps track of company wide information which enables the MIS broker to provide end users with enterprise wide, rather than localized, perspectives in their decision making process.

The data directories, model directories, and tool directories could be located on either the broker server (i.e., the server maintained by the MIS broker) or the individual departmental servers. While those on the broker server cut across functional boundaries, the ones on individual servers could be specific to a particular functional department within the company. For example, on the server maintained by the engineering department, these three directories only contain information that is related to engineering models, data, and solvers, while accounting models are recorded in the model directory sitting on the accounting server.

To be more specific, data directories maintain information on what data is available and where, how recent the data is, data attributes information (for example, format, content), and what the access price is if the data is from outside.

Model directories contain information on previously built decision models that can be used as building blocks for new problem model formulations. They describe the location of the models, the modeling contexts, and what data is needed to solve the model.

Tool directories maintain a list of solvers (for example, SAS solver, SPSS solver, LINDO solver) with their attributes, that is, the address of each solver and the data formats each solver accepts. These directories describe the problem domain of each solver, solver characteristics, and its access price. To solve a decision making problem, the information retrieval agent will access DSS tool directories that present a choice of different tools available in different domains, with each domain containing possibly many different tools. For example, one solver may include optimal methods but it may be running on a relatively slow server that will jeopardize the response time. Others may run on a massively parallel machine so that large scale problems can be solved in real time but this increases the total cost. Different tools will also require different data formats and data sources. The directories maintain information such as the compatibility between tools and data sources, limitations of each tool, accuracy of the data, etc. They also contain availability information about each solver so that waiting time on the client's side will be minimized.

The ability to define solvers allows several applications to share resources more effectively in a networked environment. Solvers provide general purpose capabilities useful in a wide range of DSS applications. The idea behind solvers is to consolidate processing in one area for reusing the programs or sharing between multiple clients. Defining solvers also allows the decoupling of applications from solvers. For instance, an application need not hard code specifics of a solver. It should be able to specify something generic like “math-solver” that then is bound by the DSS tool directory to a target machine and solver.

## 6. DSS knowledge base

The knowledge base is a distributed digital library of DSS related documents and databases that will be retrieved by the MIS broker to solve decision problems imposed by end users. We have to acknowledge the fact that information generated in a company is dispersed. The idea of a centralized knowledge base that keeps every piece of information generated in the company in one place is simply not practical. Therefore, the organizational knowledge base is a decentralized one with each functional department maintaining their own department specific knowledge (Fig. 3). For example, the accounting department maintains its own server containing information that is related to accounting, such as annual reports, balance sheets, cash flow statements, and basic accounting models. The manufacturing department, on the other hand, will keep on their server the inventory data and scheduling models. The documents on these different servers, nevertheless, can still be logically connected. For example, as shown in Fig. 3, documents f21 and f24 are located on the accounting server, while documents f14 and f10 are located on the marketing server. But document f14 is related to document f21. The logical connection is reflected in the broker directory.

![](/api/attachments/R86T2BG2/fulltext/images/f2c1c0c2d6845be02ad736000c6a5dba162661790cd6a3123b03b923f3f285f0.jpg)  
Fig. 3. Distributed knowledge base.

However, the data formats on each server may be independent of the formats on other servers, and different solvers often require different data formats. Then when the MIS broker composes and executes a decision model which is a compound document consisting of several document fragments from different sources, what data format should the MIS broker use? How to convert the format into one that meets solver requirements? This essentially boils down to the problems of interoperability and inter-application information exchange, to achieve which a key issue becomes to find a generic representation for documents. SGML has been adopted as an official international standard for the electronic interchange of information by the aerospace, defense, and some other industries. However, companies have not yet looked into the possibilities of applying SGML to the business domain to help achieve document reusability and interoperability of applications. In this section, we intend to bridge the gap by showing how to use SGML to represent documents.

## 6.1. Standard generalized markup language

Conventional documents are often structured in such a way that document content is hard to access and manipulate. One approach to solving this problem is to separate the logical structure of the document from the physical structure. Although the logical structure of documents may be arbitrarily complex, some regularities can be captured with descriptive markup languages, such as SGML $[15]$ . One main strategy emerging for making documents computable across applications and platforms is tagging languages. So far, the most widely used tagging language is SGML. It is a document encoding mechanism designed to provide a method for describing the relationship between the structure and the content of a document, enabling the “markup” of information content of documents. A basic design goal of SGML was to ensure platform independence, that is, documents encoded according to its provisions should be transportable from one hardware/software environment to another without loss of information. The structure of documents therefore can be understood or interpreted by other software applications that have SGML data interpretation capability.

A subset of SGML, but a more familiar and widespread concept, is HTML, used to create documents for the World Wide Web. The success of HTML shows the importance of the ideas behind SGML. SGML is far more flexible than HTML because it allows users to define their own tags. Therefore, with SGML, users will be able to refine their information searches using not only keywords but also their context in the documents.

The notion of document type definition (DTD) introduced by SGML enables documents to be formally defined by their constituent parts and their structures, in other words, DTDs include a specification of which elements and attributes can occur in a document and in what order. For example, a document designer might write a DTD that enables the analytical discussion of a mathematical paper to be marked up as such. The primary purpose is that the text identified as forming part of a paper's analytical discussion can then be organized in a particular way when the SGML source document is combined with other SGML documents, giving explanations for the particular model derived. If, at some later date, it is decided that this part of analytical discussion is useful in another context, it is easily done to combine it with other documents by extracting this part.

## 6.2. Using SGML to represent structured documents

As we discussed in Section 2, structured documents will serve as the knowledge representation scheme for our distributed DSS. The heart of the system depends heavily on the choice of the document structure. Recognizing that decision models most likely will contain relationships (e.g., a linear programming model, a quantitative or qualitative equation, etc.) and the context (i.e., assumptions and conditions) under which these relationships hold, we have defined the following document structure as a generic representation scheme for the documents in our distributed knowledge base (see [3] for a detailed discussion of the structure).

## document

name

each document name is a unique identifier of the document

input

output

description

description of the functionality

context

assumptions and/or conditions under which the relationships hold

relationships

relationships between the input and the output

end

The following DTD specifies the elements of this document, for example, name, input, output, descriptions, etc., the order in which these elements can occur, and the data type each element can have. Documents in the knowledge base need to conform to this DTD to be valid documents. This, however, does not imply that too strict requirements are imposed on the structure and the elements of the documents, because, as shown in the explanation below, this DTD is flexible enough to encompass most document types in the enterprise knowledge base.

<!DOCTYPE DSS\_DOCUMENT>

<!ENTITY % OR\_model “(Linear\_Programming|Integer\_Programming|Probability)+”>

<!ENTITY % Economic\_model “(Dynamic\_Programming|Game\_Theory)+”>

<!ENTITY % Functions “(Qualitative\_Relations | Mathematical\_Equations) + ”

<!-- The above three parameter entities defined here allow models in the DTD to be made more explicit. We could, of course, define other model types as well.-

<!ELEMENT document\_fragment -- (name, input+, output+, description?, context+, relationships+))

<!-- Document fragments consist of a name, one or more input, one or more output, an optional description, the conditions of usage, and the relationships ->

<!-- The hyphen “-” indicates that both the start tag and the end tag must be present in every occurrence of the element concerned, which is document\_fragment in this case ->

<!-- The plus sign means that there may be one or more occurrences of the elements: input, output, context, and relationships -

<!-- The question mark means that there may be at most one and possibly no occurrence of the elements "description" ->

<! ELEMENT (name, input, output, context) - O (#PCDATA) +

(!- This line indicates that the elements being defined (name, input, output and context) may contain any valid character data, specified as #PCDATA here, and these elements must appear in the order specified in the parentheses. The letter 0 indicates that the end tag may be omitted -

```txt
<!-- The "description" element can contain figures, video, as well as character data ->
```

<!-- The "relationships" element could contain an OR model, an economic model, some mathematical functions, as defined at the beginning of the DTD ->

According to this DTD, a structured document fragment in the knowledge base will be marked up as the following with the internal representation language SGML:

```xml
<document_fragment>
<name>f28
<input>Cost
<input>Revenue
<output>Net Income
<description>
Accounting model describing the quantitative relationship between cost, revenue, and net income.
<context>
Ontological Assumption=cash flow
Time Scale=medium
Operating Assumption=quantitative
<relationships>
Net Income=Revenue - Cost
</document_fragment>
```

The SGML tags separate the different elements of the document, enabling the MIS broker to extract the elements as needed by identifying the tagged elements in the query search process. For example, a user query could specify that, in addition to other search conditions, only documents with a qualitative operating assumption should be chosen, a requirement not difficult to meet since the SGML tag $\langle context\rangle$ makes this refined search easy to execute. When multiple document fragments are required to answer one single query, the MIS broker will compose a compound document that contains all the relationships elements of those document fragments. The composition process is also made possible by the SGML tags. Moreover, models in the relationships element could be further tagged, allowing the models to be converted to a different format at the run time, if needed.

## 7. Example: Execution of a query

We have implemented our architecture on the World Wide Web using the agent technology and the structured document technology. The agents are written in Perl $^{2}$ , a scripting language. HTML forms are used to enter information (directory information, document fragments, etc.) to servers. Document fragments entered in HTML forms are translated by a gateway agent to SGML documents that are stored in the knowledge base.

![](/api/attachments/R86T2BG2/fulltext/images/6a03e224c0d9337dd59295e9afdd65a7d60d482b4082988bf7d5b54bf85310e8.jpg)  
Fig. 4. The graphical representation of the directory.

As the first step in developing the broker directory, we have identified some organizational variables and document fragments that contain those variables. The broker directory shows what is available in the knowledge base, how document fragments are related to each other, and where each document fragment resides. Fig. 4 is a graphical representation of the broker directory that helps the reader understand how the directory is structured. The nodes in the graph represent organizational variables and the arcs connecting two nodes indicate the existence of a relationship between the two corresponding variables. Arc labels identify document fragments containing such relationships. The specification of a relationship cannot be obtained directly from the directory, but must be retrieved from the corresponding document fragment residing on individual servers, for example, the accounting server. Each time a document fragment is added to the knowledge base, the broker directory needs to be updated. The updating takes place on the broker server, which means that each time a document fragment is added to the knowledge base on a departmental server, the broker needs to be notified automatically and the corresponding document information needs to be added to the directory with the URL address of the document fragment (see [3] for a discussion of the graph).

The knowledge base consists of all the information available on each individual server within the company. Each functional department maintains its own servers and is responsible for adding to the server the new knowledge generated in the department. Since we have defined a document structure for the knowledge base, every functional department will follow the same structure, for the sake of interoperability. The HTML form shown in Fig. 5 will be used as the interface that takes the document fragments. Then the information submitted in the form will be processed by a gateway agent into an SGML document to be stored in the knowledge base.

Let's suppose that we have a scenario where the marketing department of a company initiates a query “How does an increase in price affect net income?” To answer this query, we need to have an interface agent that is capable of parsing the query. Conceptually based on natural language processing, the interface agent would analyze the query and derive from it a set of modeling terms, such as variables and operations, which would serve as the starting point for the broker to evaluate the query. In the absence of such a sophisticated interface agent, we could simply use the Netscape browser. A set of HTML query forms, though rather restricted at this point, take the query input for the broker to identify document fragments of interest, where each of these has a referent in the broker directory.

![](/api/attachments/R86T2BG2/fulltext/images/7793ed7dbda175b745046faee57ea497a96bc156fdae4512953cd1b8b9c08c08.jpg)  
Fig. 5. The HTML form for entering document fragment to the knowledge base.

The query process starts with the following form (Fig. 6) that asks the user to identify him/herself first (name, password, department), as a simple mechanism for access control. If the user is an authorized user, the query submitted will be processed. In this simplified query form, the user is only asked to input the modeling terms of interest, that is, Price as the starting node and Net Income as the end node, in this case.

To find all the relevant document fragments for our query “How would an increase in Price affect Net Income?” the information retrieval agent of the broker first goes through the broker directory to find all the relevant document fragments. The algorithm that enables the information retrieval agent to accomplish the task is shown below and has been implemented in Perl:

![](/api/attachments/R86T2BG2/fulltext/images/8896deac4b1bbc420607bf838d1282cea7d8e678b90ce4ca38d9331737b94910.jpg)  
Fig. 6. The query form.

```txt
Procedure Interaction_graph_search (START_NODE, END_NODE)
Begin
COMPLETE_PATH := []; PATH := []; LASTPATH := null;
END := FALSE; CURRENT_NODE := START_NODE;
% initialize
Recurse
    If CURRENT_NODE = END_NODE
    Then
    add PATH to COMPLETE_PATH;
    END := TRUE;
    Else
    push LASTPATH to PATH stack;
Loop:
    Begin
    If (there are more paths and END is FALSE)
    Then
    CURRENT_NODE := next node;
    call Recurse;
```

Else

END := FALSE;

End;

Remove last item from PATH stack;

End;

This script would collect all the paths that lead from the starting node to the end node, which are Price and Net Income, respectfully, in our example. However, since different document fragments have different application context, only those compound documents that have the same assumptions are consistent ones. Any other documents will be pruned out.

![](/api/attachments/R86T2BG2/fulltext/images/92a0b4f965db7d2089f772763e41df388a23c59d3f70eda68cb0f80b51cddd96.jpg)  
Fig. 7. The decision models for the query.

The consistent compound documents composed by the MIS broker as decision models are shown in Fig. 7, an HTML document returned to the client browser. All four decision models answer the same query. However, if we take a closer look at those models, we will see that these models differ from each other in terms of their complexity. The simplest one which contains two equations (Revenue = M + (Price) and NetIncome = M + (Revenue)) and three variables (Price, Revenue and NetIncome) is a classic accounting model with which the accounting department can come up. The most complex one, however, consists of six equations and seven variables, some of which are not accounting variables, but marketing variables (marketing position, goodwill) or customer support variables (customer satisfaction) instead. This model provides a broader view to look at the same decision problem. That is, it gives the end user an enterprise wide perspective and a cross-functional analysis, which each functional department alone is not able to achieve.

The outputs of these models should serve as inputs to some solver, the QSIM $^{3}$ solver in this case, determined by the broker according to the solver directory because of the qualitative nature of the analysis. The output of the QSIM solver should be the final results returned to the end user who initiated the query. If another type of analysis were required of the broker, the broker should be able to choose a corresponding solver.

## 8. Conclusions and future research directions

The central thesis of this paper is how to achieve information integration using the MIS broker, WWW, and structured documents. Specifically, our approach satisfies three key goals of information integration. First, it allows end users easy and consistent access to the large amount of data and digital documents that are becoming available on corporate Web servers. Second, it enables the integration of the structured document or data representation languages and data transport protocols to facilitate inter-application data exchange. Third, it provides a stable repository for long term knowledge archiving. Specifically, we illustrated the nature of a distributed DSS for electronic commerce and provided an overview of the architecture of the DSS that is required to meet three goals:

• To use structured documents as an underlying basis for Intranet decision support.

\- To develop a client–broker–server framework that serves as the basis for enterprise wide computing. This paper develops the notion of a software broker that ties together the document databases, services, and users of information. This broker also allows heterogeneous DSS applications to interoperate, a feature that is particularly important in a networked environment.

\- To organize and structure knowledge to support organizations in terms of building and linking corporate knowledge bases using the notion of directories.

The software broker architecture is based on the Web technology and the agent technology. The successful implementation of a prototype system based upon this architecture clearly indicates that this is the direction toward which enterprise computing should go. There are still several other issues that arise in order for this architecture to be fully functional in an organizational setting. We conclude with an abbreviated list of issues that need to be addressed in future research:

\- The development of more refined directories that facilitate better information organization and information retrieval.

\- The network security concerns. Two fundamental capabilities need to be developed for secure communication in the WWW decision support architecture. First is the ability to authenticate the source of a message or network connection, so that the identity of a (potential) user can be assured. Second is the ability to have secure communication with that user, without anyone else being able to eavesdrop or modify the conversation. These capabilities require not only the deployment of cryptographic software but also the development of an infrastructure for determining document identity and validity.

\- Pricing issues for accessing information and/or computing technologies, including the prices the broker needs to pay to acquire information from within the company and outside, and the prices each functional department needs to pay the broker to use the broker services. An appropriate pricing structure would provide incentive for the MIS broker to better serve the user community.

## References

[1] S. Ba and A.B. Whinston, A Market-Oriented MIS Broker for Enterprise Wide Computing, proceedings of the Thirteenth Hawaii International Conference on Systems Sciences, Hawaii (1997).

[2] S. Ba, A. Hinkkanen and A.B. Whinston, Digital Library as a Foundation for Decision Support Systems, Proceedings of the First Annual Conference on the Theory and Practice of Digital Libraries, College Station, Texas (June 19–21, 1994).

[3] S. Ba, K.R. Lang and A.B. Whinston, Enterprise Modeling and Decision Support, forthcoming in Decision Support Systems.

[4] A. Basu and R. Blanning, Model Integration Using Metagraphs, Information Systems Research 5, No. 3 (1994).

[5] T. Berners-Lee, R. Cailliau, A. Luotonen, H.F. Nielsen and A. Secret, The World Wide Web, Communications of the ACM 37, No. 8 (1994).

[6] H.K. Bhargava and S.O. Kimbrough, Model Management: An Embedded Languages Approach, forthcoming in Decision Support Systems.

[7] H.K. Bhargava, S.O. Kimbrough and R. Krishnan, Unique Names Violations, a Problem for Model Integration or You Say Tomato, I Say Tamahto, ORSA Journal on Computing 3, No. 2 (1991).

[8] E.A. Bier and A. Goodisman, Documents as User Interfaces, in: EP90: Proceedings of the International Conference on Electronic Publishing, Document Manipulation and Typography, Gaithersburg, Maryland (September), edited by R. Furuta, Cambridge University Press, Cambridge (1990).

[9] J.S. Bozman, Sun's HotJava Bubbles Up for Net Cruising, Computerworld, No. 20 (May 29, 1995).

[10] R. Bryant, International Financial Intermediation, Brookings Institution, Washington, D.C. (1987).

[11] R.S. Crouch and S.G. Pulman, Time and Modality in a Natural Language Interface to a Planning System, Artificial Intelligence 63, No. 1–2 (1993).

[12] D.R. Dolk and J.E. Kottemann, Model Integration and a Theory of Models, Decision Support Systems 9, No. 1 (1993).

[13] B. Falkenhainer and K.D. Forbus, Compositional Modeling: Finding the Right Model for the Job, Artificial Intelligence 51 (1991).

[14] E.A. Fox, Digital Libraries, Communications of ACM 38, No. 4 (1995).

[15] C.F. Goldfarb, The SGML Handbook (Clarendon Press, Oxford, 1990).

[16] S. Greengard, Using Internal Web Sites to Automate HR User Friendly, Personnel Journal 74, No. 6 (1995).

[17] IBM, White Paper: Intelligent Agent Strategy (1996).

[18] R. Kalakota and A.B. Whinston, Frontiers of Electronic Commerce (Addison-Wesley, 1996).

[19] R. Kalakota and A.B. Whinston, Manager's Guide to Electronic Commerce (Addison-Wesley) (forthcoming).

[20] R. Kalakota, J. Stallaert and A.B. Whinston, Solving Operations Research Problems Using a Global Client/Server Architecture, forthcoming in Organizational Computing and Electronic Commerce.

[21] R. Kaplan and D. Norton, Using the Balanced Scorecard as a Strategic Management System, Harvard Business Review (January–February 1996).

[22] R. Krishnan, P. Piela and A. Westernberg, On Supporting Reuse in Modeling Environments, Working Paper, School of Urban and Public Affairs and Engineering Design, Carnegie Mellon University (1991).

[23] B. Kuipers, Qualitative Simulation, Artificial Intelligence 29 (1986).

[24] C. Lagoze, Dienst: An Architecture for Distributed Document Libraries, Communications of ACM 38, No. 4 (1995).

[25] D.M. Levy, Going Digital: A Look at Assumptions Underlying Digital Libraries, Communications of ACM 38, No. 4 (1995).

[26] C. Liu, J. Peek, R. Jones, B. Buus and A. Nye, Managing Internet Information Services, O'Reilly and Associates, Inc. Setastopol, CA (1994).

[27] R.D. MacMinn and A. Sanders, Imperfect Information and Financial Intermediation, Working Paper, Department of Finance, College of Business Administration University of Texas at Austin (1989).

[28] P. Maes, Agents that Reduce Work and Information Overload, Communications of the ACM 35, No. 11 (1994).

[29] A. McLeod, The Principles of Financial Intermediation (University Press of America, Lanham, MD, 1984).

[30] N.P. Negroponte, Products and Services for Computer Networks, Scientific American 265, No. 3 (1991).

[31] Netscape, White Paper – Intranets, Netscape Communications (1996).

[32] M. Pesce, Connective, Collective, Corrective: The Future of VRML, VR World (1995).

[33] A. Reinhardt, Managing the New Document, Byte (August 1994).

[34] M. Roesler, Intelligent Agents: Software Servants for an Electronic Information World, Online 18, No. 4 (July 1994).

[35] G. Wiederhold, Digital Libraries, Value, and Productivity, Communications of ACM 38, No. 4 (1995).

[36] B.G. Yovovich, Smart Agents Do the Shopping: Software Programs Will Compare Prices Online, Advertising Age 66, No. 30 (July 1995).

[37] J. Zelle and R. Mooney, Learning Semantic Grammars with Constructive Inductive Logic Programming, Proceedings of the Eleventh National Conference of the American Association for Artificial Intelligence, Washington, D.C. (July 1993).

![](/api/attachments/R86T2BG2/fulltext/images/1008223b451431295acd5ad20ea23c35a997b9b8a31be5f2c0a8700df2af3ca0.jpg)

Sulin Ba is an Assistant Professor in the Department of Information and Operations Management at the University of Southern California. Her areas of research interest include management of intra-organizational electronic commerce, re-engineering of MIS, and decision support systems. She received a Master's degree in Information Sciences in 1992 and a Ph.D. in Management Information Systems in 1996 from the University of Texas at Austin.

Ravi Kalakota is the Xerox Assistant Professor of Information Systems in The William E. Simon Graduate School of Business Administration at the University of Rochester.

![](/api/attachments/R86T2BG2/fulltext/images/61bc13a44213b5b9c8ebc68aa627de50bdc38a20fc1afbbe3229822f34b66ea6.jpg)

Andrew B. Whinston is the Cullen Chair Professor of Information Systems, Computer Science and Economics, IC2 Fellow, and Director of the Center for Information Systems Management at the University of Texas at Austin.
