---
otero_id: 26844
otero_key: "EAF3RBWG"
title: "A Semantic Approach to Secure Collaborative Inter-Organizational eBusiness Processes (SSCIOBP)"
authors: "Lakshmi Iyer; Fergle Aubeterre; Rahul Singh"
year: "2008"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00152"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 9 Issue 3

Article 6

4-2008

# A Semantic Appr   oach to Secur  e Collabor  ative Inter-Or  ganizational eBusiness Processes (SSCIOBP)

Lakshmi Iyer , Lsiyer@uncg.edu

Fergle D¡¯ Aubeterre , fjdaubet@uncg.edu

Rahul Singh

, rahul@uncg.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Special Issue

A Semantic Approach to Secure Collaborative Inter-Organizational eBusiness Processes (SSCIOBP)

Fergle D’Aubeterre Bryan School of Business and Economics The University of North Carolina at Greensboro fjdaubet@uncg.edu

Rahul Singh Bryan School of Business and Economics The University of North Carolina at Greensboro rahul@uncg.edu

Lakshmi Iyer Bryan School of Business and Economics The University of North Carolina at Greensboro Lsiyer@uncg.edu

## Abstract

The information supply chain (ISC) involves the exchange, organization, selection, and synthesis of relevant knowledge and information about production, purchase planning, demand forecasting, and inventory among collaborating business partners in a value chain. Information and knowledge sharing in an ISC occurs in a business process context. Seamless knowledge exchange within and across organizations involved in secure business processes is critically needed to “secure and cultivate the information supply chain." Extant literature does not explicitly consider or systematically represent component knowledge, process knowledge and security knowledge for business processes within and across organizations. As a result, organizations engaged in collaborative inter-organizational processes continue to be plagued with issues such as semantic conflict issues, lack of integration of heterogeneous systems, and lack of security knowledge regarding authorized access to resources. Without appropriate security controls, manual interventions lead to unauthorized access to resources. These problems motivate our Semantic Approach to Secure Collaborative Inter-Oraanizational eBusiness Processes (SSCiOBP). We follow a desian science paradiam to identify metarequirements of SSCIOBP and develop the design artifact. SSCIOBP is evaluated using observational and descriptive evaluation methods following Hevner et al. (2004). We apply our approach to show how the Collaborative Planning Forecasting and Replenishment (CPFR) industry standard models can be enhanced using the proposed design artifact. We apply SSCIOBP to a case study to illustrate its applicability in mapping core business processes of organizations to solve semantic inter-operability issues and systematically incorporate component, process and security knowledge in the design of secure business processes across the information supply chain

Keywords: design science, information supply chain, eBusiness processes, semantic web, component knowledge, process knowledge, security knowledge, secure systems design, Role-Based Access Control

# A Semantic Approach to Secure Collaborative Inter-Organizational eBusiness Processes (SSCIOBP)

## 1. Introduction

Businesses engaged in collaborative inter-organizational business processes need to share information and knowledge to increase their partners’ knowledge bases and competitiveness (Raghu and Vinze, 2007; Tallman et al., 2004; Loebecke et al., 1999; Lorange, 1996). Additional benefits of the seamless exchange of information and knowledge resources include reduced total inventory cost (Rai et al., 2006; Hult, 2004; Lee et al., 1997) and enhanced operational efficiencies through coordination of allocated resources, activities, and roles in a value chain (Lee et al., 2000). However, businesses engaged in collaborative inter-organizational business processes continue to face problems in implementing the seamless and secure flow of information and knowledge resources across their information supply chains (ISC). These problems arise due the lack of an integrative consideration for information and knowledge exchange about products and services, business processes, and security policies in the ISC. This creates difficulties in integrating heterogeneous systems within and across organizations. A 2004 study conducted by the National Institute of Standards and Technology (NIST) estimated annual interoperability costs for all business data flows among companies in the transportation, electronics and construction supply chains at \$5 billion, \$3.9 billion, and \$15.8 billion, respectively.

Semantic interoperability problems frequently lead to inter-organizational information and knowledge exchange being done manually and outside the systems for both routine processes and problem resolution (van der Aalst and Kumar, 2003). Without the appropriate security controls for these manual interventions, they lead to unauthorized access of resources. The 2006 CSI/FBI Computer Crime and Security Survey identify that authorization violations are the second largest cause of economic losses (Gordon et al., 2006). The lack of appropriate access control mechanisms on the information and knowledge exchange among business activities leaves organizations vulnerable to various information assurance threats and prevents them from engaging in collaborative eBusiness processes.

Current technologies do not provide a unifying model to secure and coordinate Inter-organizational eBusiness processes in a semantic manner. Firms are moving away from the dyadic Electronic Data Interchange (EDI) approaches to more extensible Web-based eBusiness models to improve their collaborative business capabilities (Segars and Chatterjee, 2003; Elgarah et al., 2005). While organizations can obtain cost savings from EDI, EDI does not provide a strategic advantage (Benjamin et al., 1990). EDI enables the exchange of transactional data among organizations, but cannot exchange detailed process-level information (van der Aalst and Kumar, 2003). Emerging eXtensive Markup Language (XML) standards such as the XML Common Business Library (xCBL) by CommerceOne; the Partner Interface Process (PIP) blueprints by RosettaNet; the Universal Description, Discovery and Integration (UDDI); and the Electronic Business XML (ebXML) address the exchange of data among multiple business partners. However, they do not take into account the control flow among them (van der Aalst and Kumar, 2003). A unifying model for workflow modeling is lacking in the literature (Basu and Kumar, 2002). Service Oriented Architecture (SOA) solutions do not provide dynamic integration and interoperability capabilities to secure coordinating activities that exchange heterogeneous information and knowledge resources involved in a business process. In setting an agenda for IT research in heterogeneous and distributed environments, March et al. (2000) recognize the need for research to address semantic conflict resolution for inter-organizational collaboration. Srinivasan et al. (2005) identify workflow management and the semantic web as rich areas of inquiry and challenge IS researchers to examine system modeling and design for interorganizational processes.

We assert that secure business processes that seamlessly exchange knowledge within and across organizations are critically needed to “secure and cultivate the information supply chain.” Software engineering methodologies conceptualize security requirements as an afterthought in the non functional requirements of systems (Mouratidis et al., 2005; Baskerville, 1988). As a result, security is not fully integrated in all systems development phases (Lee et al., 2002; Apvrille and Pourzandi,

2005). Requirements specification is the most consequential phase of systems development and forms the basis for subsequent systems analysis, modeling, and design (Agarwal et al., 1999). Existing methods for the design of secure systems lack a conceptualization of secure business processes.

In this research, we attempt to answer the following research questions:

1. How can we systematically incorporate the secure and coordinated exchange of information and knowledge resources in the design of business processes across the ISC?

2. How can we express and incorporate access control policies that comply with security requirements for activities and resources involved in business processes within and across organizations?

3. How can we represent information and knowledge resources in standardized and expressive formats to enable automated and integrated collaborative business processes across the ISC?

We follow the design science paradigm to answer these research questions and develop a Semantic approach to Secure Collaborative Inter-Organizational eBusiness Processes (SSCIOBP), where information and knowledge resources are exchanged in a secure and coordinated manner. Semantic conflict resolution needed for effective integration of knowledge across distributed and heterogeneous environments is addressed through semantic technologies (Ram and Park, 2004) including Description Logics (DL) and Web Ontology Language (OWL-DL). These standards-based knowledge representation mechanisms provide computationally feasible knowledge representation (KR) for business processes. We develop expressive knowledge representation of information and explicit (codifiable) knowledge resources in standardized and computationally-feasible knowledge representation languages. Specifically, we explicate mechanisms to represent component knowledge of resources (Tallman et al., 2004), process knowledge including workflow models used in process automation (van der Aalst and Kumar, 2003), and security knowledge of authorized access to resources (Sandhu et al., 1996) for collaborative inter-organizational business processes. Semantic conflict and unauthorized access to activities and resources must be addressed to foster knowledge exchange and integrate heterogeneous systems in the ISC. The process perspective allows us to integrate information resources with process and security knowledge in the business process. Our approach analyzes and models authorization requirements through role-based access control mechanisms that are incorporated in the business process models. This incorporates security as a functional requirement in the early analysis of business processes, which is critically needed in the development of methods for secure information systems design (Siponen et al., 2006).

Hevner et al. (2004) assert that the nature of the problem, characteristics of the artifact, and available resources dictate the selection of the evaluation method. March et al. (2000) recognize the complexity involved in sharing of knowledge within and across business organizations in establishing an agenda for IT research in heterogeneous and distributed environments and suggest the use of case studies (observational evaluation) to provide insights into such complex processes. Baskerville et al. (2007) advocate the use of “soft” methods, including case-studies and field studies that treat the problem as a complex phenomenon that should be studied in its natural environment.

We evaluate the utility of SSCIOBP in developing secure business processes using descriptive and observational methods. The Collaborative Planning Forecasting and Replenishment (CPFR) approach is an emergent industry standard, developed by industry to deal with demand uncertainty. It seeks to develop a collaborative relationship between buyers and sellers through co-managed processes and shared information (www.VICS.org). Its standards provide the templates for collaborative inter-organizational business processes in the ISC. Evaluating the applicability of our approach to CPFR process templates provides a level of generalizability, since its standards are developed and adopted by a wide array of firms, shown in Appendix A. CPFR guidelines do not include sharing process knowledge across partner organizations, and its technical specifications do not include security knowledge. We demonstrate how to model CPFR process templates as secure business processes using our approach. For observational evaluation, we conduct a detailed case study of SupplyCo,<sup>1</sup> a Fortune 100 organization. SupplyCo is plagued with semantic inter-operability issues that require multiple frequent manual interventions in the critical demand forecasting inter organizational process involving a key customer, which is a Fortune 50 retailer. We apply our approach to SupplyCo to illustrate its application in mapping the core business processes of organizations to resolve semantic conflicts and enable the exchange of component, process, and security knowledge. The design artifact is evaluated by multiple decision makers in the IT and other functional areas of SupplyCo. We report their comments on the utility of the design artifact compared to extant approaches used by the organization. Our results indicate the utility of the approach to secure the demand forecasting business process for the SupplyCo.

The paper is organized following the design science research guidelines provided by Hevner et al. (2004) and Walls et al. (1992). We first present a description of the SupplyCo case to illustrate relevant problems in securing and integrating the ISC and their importance to organizations in the ISC application domain. Following that, we develop the theoretical foundations and kernel theories from the application domain and IS knowledge domain. These kernel theories guide the conceptual development of the meta-requirements and the meta-design of the design artifact. The meta-design is presented in the subsequent section. We evaluate our proposed design artifact by illustrating its application to CPFR processes and to the inter-organizational demand forecasting processes from SupplyCo. Finally, we summarize our research in the context of design science research guidelines and present its limitations and future research directions.

## 2. SupplyCo: An illustrative Case Study

SupplyCo exemplifies many of the aforementioned problems. SupplyCo is a leader in the apparel industry with annual revenues of over \$1.2 billion. It designs and manufactures clothing that is distributed to warehouses and retailers throughout the world. SupplyCo’s demand is fragmented into a few large customers that account for approximately 65 percent of revenues. SupplyCo’s demand is highly sensitive to seasonal and fashion volatility, which is common in the apparel industry. We analyzed the demand forecast and capacity planning (DFCP) business processes for SupplyCo and its primary customer, reviewed documentation for its DFCP business processes, and conducted detailed interviews with senior managers in IT, planning, customer management, and operations.

SupplyCo’s DFCP processes require information and knowledge resources from multiple business units, including replenishment, forecasting, planning, and procurement, from within SupplyCo and across partner organizations. Further investigation of SupplyCo’s DFCP processes reveals the following issues in automating the secure and seamless exchange of information and knowledge resources across the information supply chain needed for the business processes.

SupplyCo and its primary customers are advocates of the CPFR approach. While they implement CPFR models to varying degrees of success, several practical impediments remain. CPFR guidelines do not include sharing process knowledge across partner organizations in a systematic manner and do not consider how private and proprietary information and knowledge can be systematically and securely shared while maintaining information assurance concerns. Paraphrasing the director of planning and replenishment, “Our organization is trying to have a collaborative process, but in reality we are struggling to make it happen.”

According to SupplyCo’s director of planning and replenishment, DFCP is very complex and requires integration of information from multiple business units of SupplyCo and its customers. It requires coordinated information exchange across the customer’s decision support system for point of sales (POS) data, a logistics system, and two CPFR systems. Currently, SupplyCo’s planning analysts use several spreadsheets to develop an annual demand and capacity plans for each Stock Keeping Unit (SKU) per week. There are seven product categories with hundreds of SKUs. Ten planning analysts maintain and analyze these spreadsheets and manually feed the forecasting systems. This literally requires using every column available in an Excel spreadsheet.

Frequent manual data entry interventions are needed to identify and record demand adjustments for every product due to seasonality and promotions. Bi-weekly meetings between the customer, planning analysts, and replenishment analysts are needed to analyze the differences between the real demand, the expected demand, and the historical demand forecast from the system. This “collaborative” demand forecasting process results in a final, agreed-upon, weekly demand per SKU. The customer development manager notes: “This process is very inefficient. We have to manually feed the seasonality and special offers indicators for each product into our systems and into the customer systems, and on top of that if any error occurs, we have to manually do the adjustment and absorb the cost, if any.”

Given the extent of manual processes and heterogeneous information systems, it is very difficult to develop and enforce security policies in a systematic manner. Manual and ad-hoc processes are difficult to secure and monitor, and almost impossible to audit. Separation of duty and nonreputation mechanisms has not been implemented at all. A single organizational log-in is used to access the primary customer’s systems with read and write privileges. This is exacerbated by sharing of the authorization credentials with various organizational roles due to the need for information and knowledge. While changes submitted to the customer’s system are subject to approval by the customer, a systematic method of non-repudiation and segregation of duty in identifying and adjusting exceptions to demand forecast is clearly lacking. As a result, critica information for demand forecasting is shared verbally in meetings or is not shared at all with customers.

SupplyCo does not have a single production forecasting system in place. Due to several mergers and acquisitions, production units have their own forecasting systems that range from customized packages to spreadsheets. Demand forecasts are manually input to each system on a weekly basis.

SupplyCo uses EDI with its primary customers. However, semantic conflicts stemming from new product descriptions, the customers’ promotion codes and packaging and bundling for SupplyCo’s promotions occur frequently. The customer development manager explained that SupplyCo distributes customer orders to various warehouses served by each customer’s logistics. These three business organizations each use different units of measurements for orders. A package for a warehouse system could be a pallet of thousands of items, while the package for customers could be a dozen items. SupplyCo has to determine the correct measurement unit for each order by analyzing its final destination. SupplyCo managers use lookup tables for units of measurement for various shipment types and manually translate from one type to another for recording as product moves from one business activity to another. Once conflicts are resolved, revisions are manually entered by customer development officers and approved by directors of planning and execution. “Can you imagine the kind of confusions and rework a simple error might produce if we didn’t spend time looking at each order?”

The above discussion is intended to exemplify the problems in cultivating and securing the ISC and provides a motivating problem for this research.

## 3. Theoretical Foundations

In this section, we present the kernel theories for the ISC application domain and IS kernel theories that inform the development of the meta-requirements and offer guidance on the development of the design artifact. In the kernel theories for the application domain, since security requirements are in the context of knowledge exchange for inter-organizational business process in a supply chain, we start with this context and then present the security knowledge discussion.

In this research, we take the view that knowledge is situated information in the context of a specific problem domain upon which action can be advised or taken (Davenport and Prusak, 1998). Newel (1982) provides a functional view of knowledge as “whatever can be ascribed to an agent, such that its behavior can be computed according to the principle of rationality.” This forms a basis for functional knowledge management using agents - human and software - using explicit, declarative knowledge. Standards-based knowledge representation languages can be processed using reasoning mechanisms to reach useful inferences.

The secure creation, storage, retrieval, exchange, and processing of domain-specific and actionable knowledge by human or software agents to enact business processes are central issues in this research. Specifically, we focus on three types of knowledge in this research:

i. Component knowledge including descriptions of skills, technologies, consumer, and product knowledge, is amenable to knowledge exchange (Hamel, 1991; Tallman et al., 2004).

ii. Process knowledge is typically embedded in the process models of workflow management systems or exists as coordination knowledge among human agents to coordinate complex processes (van der Aalst and Kumar, 2003).

iii. Security Knowledge including access control mechanisms used to permit or deny access to knowledge resources in distributed systems (Sandhu et al., 1996; Oh and Park, 2003).

We integrate multiple theoretical foundations in this research to develop a design artifact that includes component knowledge of resources involved in a process, process knowledge including process models, and security knowledge including access control. All knowledge cannot be explicated and effectively represented and reasoned with using decidable and complete computational techniques. It is useful to focus on explicit, declarative knowledge representation (KR) using computationally feasible KR languages to build useful systems. This research uses a limited, explicit definition of knowledge that is declarative enough for standards-based knowledge representation languages and can be processed using automated reasoning mechanisms to reach useful inferences.

## 3. 1. Kernel Theories for the Application Domain

## 3.1.1. Knowledge Exchange in the Information Supply Chain

Knowledge exchange is central to inter-organizational collaboration and can increase collaborating partners’ knowledge bases and their competitiveness (Loebecke et al., 1999; Lorange, 1996). Knowledge sharing, when knowledge is not systematically stored, is difficult and requires special communication and collaborative mechanisms (Raghu and Vinze, 2007). Simonin (1999) studies knowledge transfer in strategic alliances and its impacts on collaborative outcomes and explains that knowledge ambiguity negatively affects knowledge transfer. Tallman et al. (2004) show that knowledge transferability directly affects firm performance. Extant literature recognizes that knowledge exchange affects firms’ overall performance and competitiveness. However, little research shows how to systematically and securely exchange knowledge in inter-organizational business processes.

In eBusiness, information and knowledge exchange technology enables business activities within and across organizations to support decision making underlying these activities (Holsapple and Singh, 2000). eBusiness involves connectivity, transparency, sharing, and integration of the extended enterprise knowledge across partners, suppliers, and customers (Hackbarth and Kettinger, 2000). As organizations become increasingly distributed, their reliance on inter-organizational information and knowledge flows with partner organizations is integral to eBusiness processes. A central notion in this research is that knowledge exchange occurs in the context of a business process, and it is essential for cultivating and securing the ISC.

We focus on business processes in a value chain, where a network of collaborating firms share the business goal of creating value propositions for customers. This view is consistent with Porter’s framework (1985) of value activities in a value chain, and with Sawhney and Parikh’s view (2001) of inter-organizational processes in value networks. Organizational resources include all assets, capabilities, organizational processes, firm attributes, information, and knowledge that allow the firm to develop and implement strategies to improve its effectiveness (Daft, 1983). Knowledge resources must be shared to be useful and applicable for inter-organizational business processes (Raghu and Vinze, 2007); however, organizations are selective about the nature of knowledge resources shared. Managing cooperative relationships is frequently a process of managing knowledge flows (Badaracco, 1991). Central to this discussion is the nature and context of the knowledge exchange, what knowledge is to be shared and under what conditions (Loebecke et al. 1999). In this research, we recognize that eBusiness processes provide the context in which relevant information and knowledge exchange occurs so that business goal can be attained (Grant, 1996; Oh and Park, 2003). Specifically, we are interested in information and knowledge resources, which must be shared in a secure and systematic way with partner organizations in a value chain to achieve their shared objectives. In developing the design artifact, we consider knowledge exchange needed to achieve inter-organizational eBusiness processes objectives.

## 3.1.2. Process Knowledge and Inter-organizational Business Processes

A business process is “a logically related set of tasks performed to achieve a defined business outcome” (Davenport and Short, 1990, p.12). Consistent with extant literature, we view a business process as a set of coordinated activities, enacted by human or software agents that exchange knowledge resources to achieve business objectives. Inter-organizational processes involve communication among business partners over heterogeneous information systems. The lack of standard knowledge representation leads to partners’ processes and knowledge being hidden from one another (van der Aalst and Kumar, 2003). Mechanisms that ensure the semantic integrity of the information and rules for mapping it correctly are mandatory (Basu and Kumar, 2002). Process knowledge represents a business process as a network of activities and their relationships, criteria to indicate the start and the termination of the process, and information about the individual activities, including participants and data, and their coordination (WfMC, 1996). Our design artifact uses Process knowledge to coordinate disparate business activities within and across organizations. The proposed artifact enables the exchange of information and knowledge resources, including Component and Process Knowledge, among trading partners, while providing standard knowledge representation mechanism and flexible coordination and control flow mechanisms.

A workflow is a coordinated set of business activities performed by various actors or agents necessary to complete a business process within and across organizations. Coordination is embedded in workflows and workflow management systems as coordination of task-task and taskresource dependencies (Kishore et al., 2006). Here, workflows are subsumed in Process Knowledge through coordination relationships between dependent businesses activities. We posit that interorganizational business processes provide an integrative context to coordinate the exchange of knowledge resources needed to accomplish business goals in a coordinated and systematic manner.

Effective coordination of business activities, by managing their inter-dependencies, is critical for effective inter-organizational business processes. Business processes comprise activities and require coordination mechanisms to manage their dependencies (Malone et al., 1987). Coordinating complex inter-organizational eBusiness processes requires an integrated view of the complete eBusiness process and knowledge-driven coordination to determine decision authority over distributed knowledge resources (Anand and Mendelson, 1997). Crowston and Osborn (2003) show how coordination theory can be used to develop process descriptions and process redesign. Malone et al. (2003) define resources as anything that can be used or affected by activities and provide a taxonomy of dependencies among activities and resources shown in Table 1.

<table><tr><td colspan="2">Table 1: Dependencies among multiple activities and resources (Adapted from Malone et al. 2003)</td></tr><tr><td>Dependency Type</td><td>Description</td></tr><tr><td>Flow Dependency</td><td>Typical of producer/consumer dependence where resources may be produced or consumed by business activities.</td></tr><tr><td>Fit Dependency</td><td>Two activities result in a common resource, hence the notion of ‘fit’ dependency among activities and output resources.</td></tr><tr><td>Sharing Dependency</td><td>Two activities have the same resource as a precondition.</td></tr></table>

We use the notion of activity-resource dependency where activities have a sharing, flow, or fit dependency (Malone et al., 2003) with a resource and adopt the activity resource coordination mechanisms developed in Singh and Salam (2006). These coordination constructs are used to develop the activity-resource coordination in the process knowledge representation of collaborative inter-organizational eBusiness processes using semantic technologies.

## 3.1.3. Security Knowledge: Access Control for Activities and Resources

Sharing valuable information and knowledge resources entails the risk of unauthorized access, which may lead to foregone returns on information and knowledge assets. Common mechanisms used to overcome information security issues include authentication mechanisms, authorization, access control, non-repudiation, audit trials, and distributed enforcement of security policies. Access control focuses on relationships between activities and resources by addressing authorization, authentication, segregation of duty (SOD), and delegation (Joshi et al., 2001). Access control grants or denies the access based on business rules that reflect the design of the business process and its objectives. Access control must balance the equally important and opposing forces of information sharing and strong authorization (Oh and Park, 2003). Workflow systems must incorporate the organizational structure by representing rules and policies and ensure that security policies are not breached (Basu and Kumar, 2002). Our design artifact represents sophisticated access control and security requirements for eBusiness processes, while allowing information and knowledge exchange within and across systems and organizational boundaries. We focus on incorporating access control mechanisms for authorized access to information and knowledge resources in a business process while maintaining non-repudiation and segregation of duty. Specifically, the proposed artifact incorporates security knowledge, including business rules embedded in security policies that govern the access to knowledge resources within in and across collaborative partners.

Several access control models such as Discretionary Access Control (DAC) and Mandatory Access control (MAC) have been proposed to secure distributed applications. However, research on information assurance of distributed eBusiness processes from a business process perspective is lacking (Oh and Park, 2003). Centralized mechanisms for information assurance fail to capture the distributed nature of systems support needed for inter-organizational eBusiness processes. Carpenter and Janson (2004) note that cooperating organizations that want to exchange information and knowledge resources need to be able to specify which users should have what rights to access which resources, under what circumstances.

Role-based access control (RBAC) adds roles as a layer of abstraction to simplify the association between users/actors (agents) and permission. Access control policies that specify users’ permissions to specific system resources are defined through the relationships between users, roles, and permissions. A primary benefit of RBAC is its flexibility to accommodate the changing roles of users. Sandhu et al. (1996) define a family of RBAC models that includes role hierarchies and constraints for system administrators to assign users permissions to system resources using roles. Role hierarchies reflect the organizational structures and the hierarchy of responsibility in the organization. Constraints add pragmatic consideration and exceptions to the relationships within role hierarchies and are a useful tool in implementing organizational policy for access to system resources (Park et. al, 2001). The National Institute of Standards and Technology (NIST) adopted RBAC as a National Standard in 2004 (http://csrc.nist.gov/rbac). The security literature is rich in the mechanisms and extensions of RBAC (Sandhu et. al., 1996); however, RBAC does not incorporate the content and context of the information workflow and does not separate task from role. This makes it very difficult to adopt RBAC for enterprise and inter-organizational environments where tasks would be performed by different roles in different organizations. Thus, the task-role-based access control (T RBAC) model extends RBAC into an enterprise environment. Under T-RBAC, users are related to permission (access right) through a role and task; permissions are assigned to tasks, and task are assigned to roles (Oh and Park, 2003).

Our design artifact incorporates roles, permissions, access, and security of information and knowledge resources from a business process perspective. Security Knowledge relates to access control mechanisms used to permit or deny access to knowledge resources in distributed systems.

The proposed artifact incorporates security knowledge to allow for representation and enforcement of authorization and access control constraints to control appropriate access to information and knowledge resources for business activities.

## 3.2. Kernel Theories for the IS Knowledge Domain

A variety of kernel theories from the IS literature provide technical foundations for our design artifact. Wand and Weber (2002) identify conceptual modeling and ontologies in knowledge representation as a useful avenue for future research for applications that manage knowledge, particularly across organizations. Ontology-based representation of business processes provides specificity to knowledge representation. Developments in semantic technologies make semantic web content unambiguously computer-interpretable and amenable to agent interoperability and automated reasoning techniques (McIlraith et al., 2001). This allows for knowledge to be interpreted by software and shared using automated reasoning mechanisms to reach useful inferences. Built on Resource Description Framework (RDF) and Description Logics (DL), the Web Ontology Language (OWL) is a W3C standard for semantic knowledge representation. Web Services and Web Services Architecture provide envelope and transport mechanisms for information and knowledge exchange. We utilize these standardized technologies for knowledge representation and for the transparent and secure exchange of unambiguous machine-interpretable knowledge. Together, these technologies provide semantic knowledge representation and exchange mechanisms for secure semantic collaborative inter-organization eBusiness processes.

## 3.2.1. Semantic Technologies

In the Semantic Web, information is given “well-defined meaning” for machines to “process and understand” the information presented to them (Berners-Lee et al., 2001). The Semantic Web comprises ontologies for knowledge representation, and intelligent software agents to integrate heterogeneous systems and exchange semantically enhanced knowledge within and across organizational systems. Semantic eBusiness manages knowledge for coordination of eBusiness processes through the systematic application of Semantic Web technologies (Singh et al., 2005). Semantic eBusiness leverages Semantic Web technologies and concepts to support the transparent flow of semantically enriched information and knowledge and enable collaborative eBusiness processes within and across organizational boundaries.

## 3.2.2. Ontology

Ontologies provide a shared and common understanding of specific domains that can be communicated between disparate application systems (Guarino, 1995). This provides the means to integrate the knowledge used by online processes employed by organizations (Klein et al., 2001). Noy and McGuinness (2002) identified the following as the major purposes of ontologies:

● Enable a shared understanding of structure of information among people and agents.

● Enable information reuse in applications.

● Make the assumptions underlying an IS implementation explicit and well-understood.

Specify the knowledge embodied in an ontology at an appropriate level of granularity (universe, bounded universe, domain, operational).

It is useful to apply the ontological structures at different stages of IS development: analysis, conceptualization, and design (Kishore et al., 2006). Selecting the ontological implementation language is a crucial task in the ontology development process. Several ontology languages have been developed. The reader is referred to Gomez-Perez et al. (2004) for a comprehensive treatment of ontology languages. Ontology documents can be created using standardized content languages like BPEL, RDF, and OWL to generate standardized representations of the process knowledge (Sivashanmugam et al., 2004; Thomas et al., 2006). Here, we select SHIQ Descriptions logics, which are equivalent to DAML+OIL presented by Li and Horrocks (2004), to develop ontologies for our design artifact. Benefits of this selection include the ability to test completeness and decidability using automated tools and the ability to translate these representations into standardized Web ontology representation in OWL-DL.

## 3.2.3. Description Logics and Knowledge Representation

Description logics (DL) are logical formalisms for knowledge-representation (Li and Horrocks, 2004). DL derive descriptive power from enhanced expressiveness of complex descriptions and terminological axioms built using atomic concepts and relationships to describe how concepts and relationships are related to each other in the application domain. This creates a set of specific terminological axioms that define the inclusions (⊆) or the equivalence (≡) of entities in the problem domain. A DL system contains a T-BOX and an A-Box. T-Box (i.e., terminological component) consists of intentional knowledge in terminological form, and it is built through declarations that describe general properties of concepts. A-Box (i.e., assertion component) contains extensional knowledge specified by the individuals in the discourse domain (Baader et al., 2003; Gomez-Perez et al., 2004). DLs provide formal linear syntax to express descriptions of top-level concepts in the problem domain, their relationships, and the constraints imposed by pragmatic considerations in the domain of interest. Generalizations and specialization hierarchies of relationships express specialized relationships between derived concepts. The DL SHIQ provides basic DL and the negation of arbitrary concepts, (qualified) cardinality restrictions, role hierarchies, inverse roles, transitive roles, and data types (a restricted form of DL concrete domains). In this study, we adopt the SHIQ Descriptions logics presented by Li and Horrocks (2004). The OWL and OWL-DL W3C standards are based on the SH family of description logics.

The Web Ontology Language (OWL) is a World Wide Web Consortium Standard and a leading approach to semantic Web ontologies. OWL-Description Logics (OWL-DL) uses DL as its fundamental knowledge representation mechanism. Ontology descriptions are presented formally through description logics for theoretical soundness; and in machine readable format using an OWL-DL to provide practicality for our model. Software reasoners, such as Racer, support concept consistency checking, T-Box reasoning, and A-Box reasoning on models developed using SHIQ description logics translated into OWL-DL. These provide the basis for development of a knowledge base of machine interpretable knowledge representation, in OWL-DL format, that can be used for developing computational ontologies for knowledge integration in inter-organizational eBusiness processes.

In the proposed design artifact, agents are used for knowledge exchange and interpretation to support semantic collaborative inter-organizational eBusiness process activities. A fundamental implication is that knowledge must be available in formats that allow for processing by software agents. We develop DL-based semantic knowledge representation for activity resource coordination in semantic eBusiness processes. These provide machine-interpretable knowledge representation and computational ontologies in OWL-DL format to support knowledge integration in collaborative inter-organizational eBusiness processes. DL-based knowledge representation provides the formalism to express structured knowledge in a format amenable for normative reasoning by intelligent software agents.

Based on the characteristics of inter-organizational eBusiness processes, we identify the main shortcomings of the existing approaches and technologies and summarize them in Table 2.

## 4. Research Methodology and Meta-Design of the Artifact

## 4.1. Design Science Paradigm

Design science research addresses classes of problems that solve relevant and unsolved problems, or solve problems in a more effective and efficient manner (Hevner et al. 2004). The design artifact comprises ideas and capabilities to develop systematic solutions for the problem domain, including the construct vocabulary and symbols, models that provide abstraction and representations, methods, and prototypes (Hevner et al., 2004; March and Smith, 1995). The meta-design describes a class of artifacts and a set of systems principles to select systems features that meet meta-requirements (Markus et al. 2002). Kernel theories from the application domain are applied, modified, and/or extended (Hevner et al. 2004) to develop the theoretical basis for the meta-requirements and metadesign. Kernel theories from the application domain organize and structure constructs in the

<table><tr><td colspan="2">Table 2: Shortcomings of Existing Approaches and Technologies for Secure Semantic eBusiness Processes</td></tr><tr><td>Existing Approaches/Technologies</td><td>Shortcomings</td></tr><tr><td>EDI/ XML/ebXML /RosettaNet</td><td>Support only dyadic relationships using proprietary formatsDo not allow exchange of detailed process-level informationEnable only exchange of transactional dataDo not provide security requirements and policies representationDo not include sharing process knowledge across partner organizations</td></tr><tr><td>Workflows</td><td>Do not provide security requirements and policy representationDo not enable the integration of heterogeneous inter-organizational information systemsDo not allow for a fine grained segregation of duty specifications</td></tr><tr><td>CPFR</td><td>Does not include sharing process knowledge across partner organizationsDoes not consider how private and proprietary information and knowledge can be systematically and securely shared</td></tr><tr><td>Access Control (DAC/MAC/RBAC)</td><td>Fails to capture the distributed nature of systems support needed for eBusiness processesDoes not incorporate the content and context of the information workflow</td></tr><tr><td colspan="2">application domain, while kernel theories of IS Domain provide the representations and techniques that form the basis for artifact development. IS problem solving applies the IS domain knowledge and concepts to the theories of the application domain and advances knowledge in both domains (Khatri et al., 2006).In the next section, we integrate kernel theories from the application and IS knowledge domains to provide the theoretical foundations for developing the design artifact.4.2. Meta-Design for the Design ArtifactThrough analysis of the relevant extant literature, we develop the meta-requirements for our design artifact as:i. Security of resources must be ensured through access control policies that comply with requirements for secure activity resource coordination for business processes within and across organizations.ii. Agents must represent business enterprises to fulfill organizational roles and perform business activities in a coordinated manner to accomplish business process objectives.iii. Coordination of dependencies among business activities and information and knowledge resources must be supported.iv. Association between agents, resources, and permissions must be decoupled into roles, permissions, access, and security of information and knowledge resources from a business process perspective.v. Semantic inter-operability mechanisms that allow for integration of knowledge resources must be provided.vi. Information and knowledge resources must be described in unambiguous, computer-interpretable KR, amenable to agent-based reasoning.</td></tr><tr><td colspan="2">Kernel theories guide the development of our design artifact to meet these meta-requirements. Analysis of kernel theories reveals that collaborative inter-organizational business processes can be represented using the following atomic concepts: business enterprise, agent, role, activity, and resource. Those atomic concepts are consistent with extant research. Similarly, Singh and Salam (2006) propose that essential concepts to model eBusiness processes include business enterprise,</td></tr></table>

agent, business activity, resource, coordination, information, and knowledge. Kishore et al. (2006) propose eight minimal ontological foundation constructs for the Multi-Agent-Based Integrative Business Information (MIBIS) universe of discourse, including goal, role, interaction, task, information, knowledge, resource, and agent, based on literature in integrative business information systems and multi-agent systems domains. We propose that business enterprises engaged in collaborative interorganizational business processes can be represented by agents. Agents fulfill organizational roles and perform activities that consume and produce resources. Activities require access to resources to be performed. Roles de-couple the relationships and provide authorization constraints for agents and the individual activities that comprise the business process. Consistent with RBAC, resources, in our model, allow activities to be performed on them. Here, we consider only information and knowledge resources involved in business processes. They are used by agents in a business enterprise to perform their assigned activities in order to accomplish their goals. Dependencies among multiple resources and multiple activities are coordinated using flow, fit, or sharing coordination methods (adapted from Malone et al., 2003). Figure 1 shows the meta-design of the proposed design artifact, including the atomic concepts and their relationships needed to model business processes.

![](/api/attachments/EAF3RBWG/fulltext/images/1384ce0e3662b06bb8ed7c518555d3d5c93259ee8433336e91d1ca70f5c2bc82.jpg)

Figure 1. Semantic Approach for Secure Collaborative Inter-organizational eBusiness processes (extended from Singh and Salam, 2006 and Kishore et al., 2006)

DL representation of the design artifact describes the semantic schema through complex concepts specifications and relation expressions built upon atomic concepts and relations. Constructs are represented as unary predicate concept constructs, and relationships are the n-ary relations construct. These concepts and relationships define the contents of the T-Box Knowledge representation as terminological axioms for the design artifact, represented in DL shown in Table 3.

A business activity has permissions that allow it to perform operations on resources. Here, Permits and HasPermission are inverse relationships. Resource (Permits.BusinessActivity) BusinessActivity (HasPermission.Resource)

Activities and resources require coordination mechanisms to resolve dependencies. A resource is related to an activity through the Coordinates relationship. Resource (Coordinates.BusinessActivity) BusinessActivity (HasCoordination.Resource)

The Coordinates relationship is specialized in inheritance hierarchies as CoordinatesFlow, CoordinatesFit, or CoordinatesSharing relationships. Coordinates CoordinatesFlow CoordinatesFit CoordinatesSharing

<table><tr><td colspan="3">Atomic Concepts and Relationships</td></tr><tr><td colspan="2">Essential atomic concepts in the secure semantic eBusiness process domain include: i. Business Enterprise (BE) ii. Agent (Ag) iii. Role (RI) iv. Business Activity (Ac) v. Resource (Rs)</td><td>Essential atomic relationships in the secure semantic eBusiness process domain include: i. Represents ( ≡IsRepresentedBy) ii. Fulfills ( ≡IsFulfilledBy) iii. Performs ( ≡IsPerformedBy) iv. Permits ( ≡HasPermission) v. Coordinates( ≡HasCoordination) vi. Owns( ≡IsOwnedBy)</td></tr><tr><td>Business Enterprise</td><td>A Business Enterprise is represented by at least one Agent and owns at least one resource need in the business process.</td><td>BusinessEnterprise ⊆ (≥1 IsRepresentedBy ·Agent) ∧ (≥1 Owns ·Resource) ∧ (≥1 HasClassificationID ·StringData) ∧ (≥1 HasDescription ·StringData) ∧ (≥1 HasAddress ·Address) ∧ (≥1 HasProfile ·Profile)</td></tr><tr><td>Agent</td><td>An Agent represents a Business Enterprise and fulfills a Role for the Business Enterprise.</td><td>Agent ⊆ (=1 Represents ·BusinessEnterprise) ∧ (≥1 Fulfills ·Role)</td></tr><tr><td>Role</td><td>A Role concept is fulfilled by an Agent and performs at least one Business Activity</td><td>Role ⊆ (≥1 IsFullfilledBy ·Agent) ∧ (≥1 Performs ·Activity)</td></tr><tr><td>Business Activity</td><td>A Business Activity is performed by a Role, has at least one permission to a Resource, coordinates Resources and has a Begin Time and End Time.</td><td>Business Activity ⊆ (≥1 hasLabel ·StringData) ∧ (≥1 isPerformedBy ·Role) ∧ (≥1 hasPermission ·Resource) ∧ (≥1 isCoordinatedBy ·Resource) ∧ (=1 hasBeginTime ·DateTimeData) ∧ (=1 hasEndTime ·DateTimeData)</td></tr><tr><td>Resource</td><td>A Resource is a thing owned by exactly one Business Enterprise and permits Business Activities to perform operations on it and coordinates Business Activities</td><td>Resource ⊆ (=1 hasID ·StringData) ∧ (=1 IsOwnedBy ·Business Enterprise) ∧ (≥1 Permits ·BusinessActivity) ∧ (≥1 Coordinates ·BusinessActivity)</td></tr></table>

PermitCreate

PermitDelete

The inheritance hierarchy of the Permits relationship allows more specific relationships between Resources and Business Activities.

Resource

(≥0 PermitsRead.BusinessActivity)

(≥0 PermitsWrite.BusinessActivity)

(≥0 PermitsCreate.BusinessActivity)

(≥0 PermitsDelete.BusinessActivity)

Here we assume Information and Knowledge are the primary resources considered for the business process problem domain.

Information Resource

Knowledge Resource

These terminological axioms comprise a “T-Box” (i.e., terminological component) for the proposed design artifact, which includes concepts and their relationships in the meta-design. An “A-Box” (i.e., assertion component) contains specific instantiations of the TBox axioms. These provide instance level entities for verification, refinement, and implementation of the semantic data models. The terminological axioms, and their instantiations, form the DL-based KR system used to reason about the problem domain. Satisfiability and logical implication in SHIQ are ExpTime-complete (Baader et al., 2003). Protégé (protege.stanford.edu) and Racer (www.racer-systems.com) are automated tools for DL formalism verification and model consistency checks. Protégé generates standardized OWL-DL for schema and instance level documents for verification and implementation of semantic KR. Reasoning procedures and query processing in Racer allow inferencing from the schema and instance models.

## 5. Design Artifact Evaluation

In guidelines for evaluating design science research, Hevner et al. (2004) state that the “business environment establishes the requirements upon which the evaluation of the artifact is based” (p. 85). The nature of the problem, characteristics of the artifact, and available resources dictate the selection of the evaluation method. We base the evaluation of our design artifact on the needs for cultivating and securing the information supply chain. In establishing an agenda for IT research in heterogeneous and distributed environments, March et al. (2000) recognize the complexity involved in sharing of knowledge in business organizations. Consistent with Hevner et al. (2004), for such complex scenarios, they suggest the use of case study (type of observational evaluation) to provide insights into the development process.

The goals of the design artifact evaluation are to show the technical feasibility of the proposed IT artifact and to show how the proposed IT artifact provides value to critical inter-organizational eBusiness processes in the ISC. We evaluate the artifact through observational and descriptive methods including informed consent and case study. We use a form of descriptive evaluation, the informed consent method, to illustrate the artifact’s utility and application. Specifically, we apply our design artifact to enhance and map DFCP business process for the prevalent industry-developed CPFR approach. We then show how the proposed artifact can be applied to real DFCP business processes of SupplyCo, described earlier in this paper. Using real DFCP business processes, we capture both the information and knowledge, including component, process, and security knowledge related to the business processes and the richness of the organizational environment. We show how the proposed design artifact represents the information and knowledge resources involved in the DFCP business process in a standardized machine-readable format. Also, we illustrate how the proposed design artifact incorporates access control policies to enable the secure seamless exchange of information and knowledge needed to enact the DFCP business process.

We evaluated existing approaches using the SSCIOBP’s meta-requirements, which were identified from the problem domain and relevant literature, and present the result in Table 4.

<table><tr><td>Meta Requirement/Existing Approaches/Technologies</td><td>EDI/XML/ebXML/Rosetta Net</td><td>Work-flows</td><td>CPFR</td><td>Access Control (DAC/MAC/RBAC)</td><td>SSCIOBP</td></tr><tr><td>MR1: Security of resources must be ensured through access control policies that comply with requirements for secure activity resource coordination for business process within and across organization (RBAC-NITS 2004; Sandhu et al., 1996; ; Loebecke et al., 1999).</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+</td></tr><tr><td>MR2: Agents must represent business enterprises to fulfill organizational roles and perform business activities in a coordinated manner to accomplish business process objectives (Business Process and Inter-organizational Workflow, van der Aalst and Kumar, 2003; Singh, et al., 2005; Sikora and Shaw, 1998).</td><td>-</td><td>+</td><td>-</td><td>-</td><td>+</td></tr><tr><td>MR3: Coordination of dependencies among business activities and information and knowledge resources must be supported (Coordination Theory- Malone et al., 2003; Kishore et al., 2004).</td><td>-</td><td>+/-</td><td>-</td><td>-</td><td>+</td></tr><tr><td>MR4: Association between agents, resources and permissions must be decoupled into roles, permissions, access, and security of information and knowledge resources from a business process perspective (RBAC-NITS 2004; Sandhu et al., 1996; Oh and Park, 2003; Carpenter and Janson 2004).</td><td>-</td><td>-</td><td>-</td><td>+/-</td><td>+</td></tr><tr><td>MR5: Semantic Inter-operability mechanisms that allow for integration of knowledge resources must be provided (Semantic Web and DL/KR - Berners-Lee et al., 2001; Baader, 2003; Singh and Salam, 2006).</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+</td></tr><tr><td>MR6: Information and Knowledge resources must be described in unambiguous, computer-interpretable KR, amenable to agent-based reasoning (Semantic Web and DL/KR - Berners-Lee et al., 2001; Baader, 2003; Ram and Park, 2004).</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+</td></tr><tr><td colspan="6">Note: (-): The approach does not meet the particular meta-requirement; (+): The approach meets the particular meta-requirement; (+/-): The approach partially meets the particular meta-requirement</td></tr></table>

The remaining approaches do not meet the meta-requirements, because they fail to provide standard knowledge representation needed for describing resources in unambiguous, computer –interpretable format; semantic conflict resolution needed for effective integration of knowledge across distributed and heterogeneous environments; and a unifying model to secure and coordinate inter-organizationa eBusiness processes in a semantic manner.

## 5.1. Descriptive Evaluation: Collaborative Planning, Forecasting, and Replenishment (CPFR)

Successful supply chain management involves the coordination of activities performed by multiple independent companies to deliver a product or service to the end customer (Lee and Whang, 1998). Several factors affect the success of supply chains. Demand uncertainty has always been a topic of interest for the academic and practitioner communities. Swaminathan and Tayur (2003) explain that CPFR is a new and growing movement in industry to deal with demand uncertainty.

CPFR attempts to create collaborative relationships between buyers and sellers through co-managed processes and shared information (www.VICS.org). CPFR standards provide the templates for collaborative inter-organizational business processes in the ISC. CPFR aims to make pertinent information available to all member of the supply chain to improve its efficiency. In particular, seamless flow of information across the supply chain helps to coordinate and improve the accuracy of the critical demand forecasting and capacity planning information. According to the Voluntary Interindustry Commerce Standards Association (VICS), several leading retailers and manufacturers have successfully adopted CPFR and have obtained benefits such as reducing working capital and fixed capital, reducing operation expenses, improving technology ROI, and growing sales (www.VICS.org). Appendix A shows corporations at various positions in the supply chain that have adopted CPFR.

CPFR guidelines do not include sharing process knowledge across partner organizations and do not consider how private and proprietary information and knowledge can be systematically and securely shared while maintaining information assurance. CPFR technical specifications do not include security knowledge. In other words, the permissions about the kinds of activities agents can perform over resources are missing. Atallah et al. (2005) highlight the need to secure CPFR data flows through a Secure Multi-Party Computation framework.

CPFR specifies nine primary business processes and data flows needed to enable collaboration among business partners. We consider the Create Order Forecast and Generate Order business processes. These processes are of strategic and tactical importance (Caridi et al., 2005) and require a high degree of collaboration and integration. Figure 2 presents the dataflow in the Create Order Forecast and Generate Order processes. The Create Order Forecast dataflow describes the information exchanged in an initial order forecast for products within a planning period. The Generate Order dataflow shows the transmission of a “firm” order for products, based on an order forecast and an item management profile (CPFR Technical Specifications, VICS 1999).

We analyze these business processes using the meta-design of our design artifact (from Figure 1) and identify the following atomic concepts:

i) Business Enterprise: Buyer and Seller.

ii) Business Activities: Communicate POS Data; Communicate Forecast Events;

Communicate Inventory Strategy; Communicate Current Inventory; Communicate Order; Communicate Capacity Limitation; Communicate Historical Demand & Shipment; Communicate Order Shipment Data; Create Order Forecast; Generate Actual Order; and Receive Order. POS Data, Forecast Impact Events, Inventory Strategy, Current Inventory, Sales Forecast, Exception Resolution Data, Order Forecast, Capacity Limitation, Historical Demand & Shipment Data, Item Management Data, Order.

![](/api/attachments/EAF3RBWG/fulltext/images/39a1c0f1db878a6a35963bd408a0122e9e1234f6f5ee8b8e1b9b94e32bfca192.jpg)  
Figure 2: Create Order Forecast and Generate Order Processes Data Flow (Adapted from CPFR Technical Specifications, VICS 1999).

Our design artifact enhances CPFR by incorporating the roles-activities and resource-permissions needed in the business processes. Using RBAC (Sandhu et al., 1996), we show, in Table 5, the roleactivity-resource permissions for CPFR’s generate order business process. Appendixes B1-B4 show the DL for the following business activities and resources: 1) create order forecast activity, 2) order forecast resource, 3) generate order activity, 4) order resource. By applying the meta-design to the CPFR approach, we create DL formalisms for knowledge representation for business processes, which forms the basis for the development of machine interpretable knowledge representation in the OWL-DL format.

The atomic concepts and their relationships in the design artifact are used to map core business processes of CPFR and to incorporate security knowledge in the CPFR models and technical specifications. Figure 3 shows how the atomic concepts and relationships from the proposed design artifacts are used to develop the secure semantic activity-resource coordination mapping for the Create Order Forecast and Generate Order business processes discussed above.

A primary motivation of our design artifact is including security as a functional requirement in the early analysis of the business process. We show how our artifact can be used to analyze and represent granular security requirements for specific CPFR business processes. For instance, based on results of the analysis presented in Table 4, business and system analysts can recognize that the POS Data can only be read by the Communicate POS Data Activity, which can only be performed by the Buyer Role. This implies that if any other business activity tries to modify the POS Data, it would result in a security violation. The Role-Activity Resource permission analysis allows mapping organizational responsibilities into roles, fulfilled by specific agents. For instance, the seller agent, fulfilling the seller role, is responsible for executing the business activities identified in Table 5. If the Seller Agent, in the Seller role, executes a business activity not identified above, it is a security violation. These analyses, for all agents, roles, activities, and resources, can be used to develop security policies for the interorganization business process.

![](/api/attachments/EAF3RBWG/fulltext/images/8e16a3f24546c97741d195043ca9cdecf5fdad887a38cc21244c377a103a1218.jpg)

<table><tr><td colspan="5">Table 5: Security analysis for role-activity-resource permissions for the CPFR&#x27;s generate order business process</td></tr><tr><td>Agent</td><td>Role</td><td>Business Activity</td><td>Permission Type (Write, Read, Create, Delete)</td><td>Resource</td></tr><tr><td rowspan="5">Buyer Agent</td><td rowspan="5">Buyer Role</td><td>Communicate POS Data</td><td>Read</td><td>POS Data</td></tr><tr><td>Communicate Forecast Events</td><td>Read</td><td>Forecast Impact Events</td></tr><tr><td>Communicate Inventory Strategy</td><td>Read</td><td>Inventory Strategy</td></tr><tr><td>Communicate Current Inventory</td><td>Read</td><td>Current Inventory Data</td></tr><tr><td>Communicate Order</td><td>Read</td><td>Order</td></tr><tr><td rowspan="8">Seller Agent</td><td rowspan="8">Seller Role</td><td>Communicate Capacity Limitation</td><td>Read</td><td>Capacity Limitations</td></tr><tr><td>Communicate Historical Demand &amp; Shipment</td><td>Read</td><td>Historical Demand &amp; Shipment Data</td></tr><tr><td>Communicate Order Shipment Data</td><td>Read</td><td>Order Shipment Data</td></tr><tr><td rowspan="2">Create Order Forecast</td><td>Read</td><td>Order Forecast, Sales Forecast, Exception Resolution Data, Item Management Data, POS Data, Forecast Impact Events, Inventory Strategy, Current Inventory, Capacity Limitations, Historical demand &amp; Shipment Data, Order Shipment Data</td></tr><tr><td>Create/Write/Read</td><td>Order Forecast</td></tr><tr><td rowspan="2">Generate Actual Order</td><td>Read</td><td>Item Management Data, Order Forecast Order</td></tr><tr><td>Create/Write/Read</td><td>Actual Order</td></tr><tr><td>Receive Order</td><td>Read</td><td>Actual Order</td></tr></table>

## 5.2. Observational Evaluation of the Design Artifact: SupplyCo DFCP Business Processes

Industry standards, such as CPFR, provide guidelines and standards for business processes. As such, they are not intended to capture nuances of the real world. To further evaluate our design artifact, we conducted a field study for the DFCP business processes at SupplyCo. SupplyCo is an apparel industry leader that designs, manufactures, and distributes apparel all over the world. With the collaboration of senior managers in Supply Chain, IT, and customer development, along with their functional teams from SupplyCo, we identified core DFCP business processes that depend on collaborative, inter-organizational knowledge exchange for their effectiveness. Through detailed interviews, focus group discussions, and reviews of process and systems documentation, we collected information about SupplyCo’s order forecast business process, its current characteristics, and the challenges that the organization faces in securing and cultivating its information supply chain.

It is important to highlight that SupplyCo was a leader in the development of the CPFR approach. It has adopted the CPFR approach with its main customers, albeit with several modifications. In addition to the standard CPFR dataflows depicted on Figure 2, SupplyCo provides information about order adjustments, the event calendar, and cancellation to the buyer organizations. We analyzed multiple documents related to the demand forecasting system and identified several shortcomings in SupplyCo’s demand forecasting business process..

To effectively execute forecasting and replenishment business processes, integration and coordination of multiple heterogeneous systems should occur; however, this does not happen at SupplyCo. For example, the customer’s product category management and supply planning systems that provide POS data, a logistic system that coordinates warehouses, and two main CPFR systems are not integrated. Currently, demand planning analysts gather information from these systems and then must manually load it into SupplyCo’s forecasting system. Moreover, the information is dispersed and fragmented across different business units. Analysts resort to using several spreadsheets to manually integrate and reconcile information from these systems to make it conform to the requirements of their demand forecasting system.

The demand forecasting process takes several manual inputs. These include business critical factors that affect the demand forecast for a particular product at specific time periods. For example, the seasonality or special offers (sales) for a product affect the expected demand of the product, and it is normal for SupplyCo to make weekly manual adjustments for every product in the demand forecast processes. Users must rely on information and knowledge that are not captured by current systems. SupplyCo holds weekly meetings to analyze the differences and variations between the real and expected demand. These variations are then manually entered into the demand forecasting systems to capture an accurate demand forecast for every product category. The large number of items makes the process very time consuming and error prone.

An analysis of the DFCP business processes using the meta-design of the design artifact reveals the following atomic concepts:

i) Business Enterprise: Buyer and Seller.

ii) Business Activities: Communicate POS Data; Communicate Event Calendar; Communicate Inventory Strategy; Communicate Available Stock; Communicate Sales Forecast; Communicate Exception Resolution Data; Receive Adjustments; Communicate Adjustments; Communicate Historical Demand and Shipment Data; Communicate Order Shipment Data; Communicate CPFR policies; Communicate Item Management Data; Communicate Cancellations; Communicate Order (Promotions// New Products); Communicate Order Forecast; Create Order Forecast; Generate Order; Received Order. iii) Resources: POS Data; Event Calendar; Inventory Strategy; Available Stock; Sales Forecast; Exception Resolution Data; Adjustments; Historical Demand and Shipment Data; Order Shipment Data; CPFR policies; Item Management Data; Cancellations; Order (Promotions// New Products); Order Forecast.

Applying the design artifact leads to a design where agents can perform activities that were heretofore manual. Standardized ontologies represent component, process, and security knowledge for streamlining collaborative eBusiness processes, while semantic inter-operability problems are solved in a systematic manner that lends itself to automation. To identify the key organizational roles and functions associated with the Create Order Forecast, we interviewed the SupplyCo’s director of planning and replenishment. We gathered information about the roles and permissions that the different actors have in the Create Order Forecast process and analyzed them using RBAC (Sandhu et. al, 1996) to develop the role-activity-resource permissions shown in Table 6. Three primary roles − planning, replenishment, and demand forecast − are shown. It is noteworthy that the buyer organization presents similar roles to SupplyCo.

<table><tr><td colspan="5">Table 6: Security analysis for role-activity-resource permissions for the SupplyCo&#x27;s generate order business process</td></tr><tr><td>Agent</td><td>Role</td><td>Business Activity</td><td>Permission Type (Write, Read, Create, Delete)</td><td>Resource</td></tr><tr><td>Buyer Planning Agent</td><td>Planning Role</td><td>Receive Adjustments</td><td>Read</td><td>Adjustments</td></tr><tr><td></td><td></td><td>Communicate POS Data</td><td>Read</td><td>POS Data</td></tr><tr><td></td><td></td><td>Communicate Events Calendar</td><td>Read</td><td>Events Calendar</td></tr><tr><td></td><td></td><td>Communicate Available Stock</td><td>Read</td><td>Available Stock</td></tr><tr><td></td><td></td><td>Communicate Order (Promotions//New products)</td><td>Read</td><td>Order (Promotions//New products)</td></tr><tr><td>Buyer Replenishment Agent</td><td>Replenishment Role</td><td>Communicate Inventory Strategy</td><td>Read</td><td>Inventory Strategy</td></tr><tr><td></td><td></td><td>Communicate Sales Forecast</td><td>Read</td><td>Sales Forecast</td></tr><tr><td></td><td></td><td>Communicate Exception Resolution</td><td>Read</td><td>Exception Resolution Data</td></tr><tr><td>Seller Planning Agent</td><td>Planning Role</td><td>Communicate Adjustment</td><td>Read</td><td>Adjustment</td></tr><tr><td></td><td></td><td>Communicate CPFR Policies</td><td>Read</td><td>CPFR Policies</td></tr><tr><td></td><td></td><td>Communicate Item Management Data</td><td>Read</td><td>Item Management Data</td></tr><tr><td></td><td></td><td>Create Order Forecast</td><td>Read</td><td>POS Data, Events Calendar, Inventory Strategy, Available Stock, Sales Forecast, Exception Resolution Data, CPFR Policies, Item Management Data, Historical Demand &amp; Shipment Data</td></tr><tr><td></td><td></td><td></td><td>Create/Write/Read</td><td>Order Forecast</td></tr><tr><td>Seller Forecast Agent</td><td>Demand Forecast Role</td><td>Communicate Historical Demand &amp; Shipment</td><td>Read</td><td>Historical Demand &amp; Shipment Data</td></tr><tr><td></td><td></td><td>Communicate Order Shipment Data</td><td>Read</td><td>Order Shipment Data</td></tr><tr><td>Seller Replenishment Agent</td><td>Replenishment Rol0065</td><td>Receive Order</td><td>Read</td><td>Order</td></tr><tr><td></td><td></td><td>Communicate Item Management Data</td><td>Read</td><td>Item Management Data</td></tr><tr><td></td><td></td><td>Communicate Cancellations</td><td>Read</td><td>Cancellations</td></tr><tr><td></td><td></td><td>Generate Actual</td><td>Read</td><td>Order (Promotions</td></tr></table>

## Table 6: Security analysis for role-activity-resource permissions for the SupplyCo’s generate order business process

<table><tr><td>Agent</td><td>Role</td><td>Business Activity</td><td>Permission Type (Write, Read, Create, Delete)</td><td>Resource</td></tr><tr><td></td><td></td><td rowspan="2">Order</td><td></td><td>and New Products), Order Forecast, Item Management Data Cancellations</td></tr><tr><td></td><td></td><td>Create/Write/Read</td><td>Order</td></tr></table>

Using the atomics concepts from our artifact, we show how the Create Order Forecast and Generate Order processes can be mapped to the semantic activity-resource coordination of the design artifact. Figure 4 shows the secure semantic activity-resource coordination for the Create Order Forecast business process.

We show the ontological engineering using DL-based definitions for the activity resource coordination for SupplyCo. It is important to highlight that these demand requirement characteristics are intended to serve as examples, and they are not exhaustive. In the Create Order Forecast business process, the buyer business enterprise is represented by a buyer planning agent and by a buyer replenishment agent. The security of the SupplyCo’s Generate Order business process is incorporated through the role-activity-resource permissions mapping.

## PlanningRole

(=1 isRepresentedBy . BuyerPlanningrAgent )

(=1 Performs. ReceiveAdjustments)

(=1 Performs. CommunicatePOSData)

(=1 Performs. CommunicateEventsCalendar)

(=1 Performs. CommunicateInventoryStrategy)

(=1 Performs. CommunicateAvailableStock)

(=1 Performs. CommunicateOrder\_Promotions\_New Products)

(=1 Performs. CommunicateOrderForecast)

ReplenishmentRole

(=1 isRepresentedBy . BuyerReplenishmentAgent )

(=1 Performs. CommunicateSalesForecast)

(=1 Performs. CommunicateExceptionResolution)

The business activities: Receive Adjustments, Communicate Adjustments, and Create Order and the resources: Adjustments and Order Forecast, from Figure 4, are critical to this business process and their DL are shown in Appendixes B5-B9. The DL for the rest of the business activities and resources needed to complete the SupplyCo’s Create Order Forecast business process are available upon request.

It is important to highlight that the demand forecasting adjustments or variations had been manually entered into SupplyCo’s demand forecasting systems. By applying the design artifact, we provide a semantic wrapper that eliminates the manual process. The standard ontology is used to represent the information related to such adjustments, and activities are represented in a machine-readable format. This allows the activity to be automatically performed by seller and buyer agents while managing semantic inter-operability in a secure and coordinated manner.

![](/api/attachments/EAF3RBWG/fulltext/images/9309338bd7760e8ac5be1e512fc7667f76dc73a2a830ced53fc38c547e217a6f.jpg)

These DL formalisms provide computationally feasible knowledge representation mechanisms for business processes for both VICS-CPFR and the SupplyCo DFCP case study. This forms the basis for the development of machine interpretable knowledge representation in the OWL-DL format. We utilize DL as the knowledge representation formalism to express structured knowledge in a format amenable for intelligent software agents to reason with it in a normative manner. Understanding the inherent relationships among business processes within and between organizations is a key topic of the information systems field. Thus, we have shown that the design artifact, based on sound theoretical grounding, prescribes the models (meta-requirements), methods (development practices), and mechanism for instantiation (system solution) as suggested by Hevner et al. (2004) and Walls et al. (1992). All DL knowledge representations presented in this paper have been developed, validated, and checked for consistency using Protégé and Racer. These tools generate OWL-DL knowledge representations essential to development of semantic collaborative inter-organizational business processes incorporating reasoning and inferencing mechanisms based on DL-formalism. The use of standards semantic models such as W3C’s OWL (Web Ontology Language) and OWL-DL transforms this approach into a truly implementable framework without loss of theoretical robustness. These provide the basis for practitioners to initiate further development and evaluation of secure semantic eBusiness processes that are semantically rich, highly coordinated, and seamlessly integrated.

## 6. Discussion

The process analysis presented above formed the subject of multiple discussions with the CIO, the director of planning and replenishment, and the customer development manager at SupplyCo that are directly responsible for systems support for demand forecasting, capacity planning, and customer development. Specifically, the proposed artifact was evaluated with respect to the motivating problems mentioned in the introduction. The results show that the proposed artifact allows for mapping and representing security requirements of business processes leading to segregation of duties and non-repudiation of business activities. In addition, the proposed IT artifact lays the foundations for semantic conflict resolution and integrating multiple dispersed data and information sources by providing common semantics for distributed knowledge and information exchange. Here, we discuss the primary benefits of the approach from SupplyCo’s perspective.

A primary motivation of the IT artifact presented here is to analyze, express, and incorporate access control policies that comply with security requirements for activities and resources involved in business processes within and across organizations. SupplyCo management expressed that the proposed IT artifact requires them to analyze and define the relationships between organizational roles, and the activities that they perform. It allows for analysis of roles and the identification of issues with segregation of duties within and across the organization in the context of the eBusiness process. The analysis, with the resultant secure activity resource coordination mapping, provides everyone, including the customer organization, with a map of the inter-organizational business process. This includes the activities to be performed, the resources produced and consumed by the activities, and their inter-relationships. In addition, it provides an analysis of the organizational roles needed by both organizations. The artifact provides an understanding of the resources that are needed by the activities and the human or software agents that will have access to these resources. The mapping provides granular information about the organizational responsibilities associated with a particular role and allows process designers to incorporate a detailed analysis of the security requirements of the business process for partner organizations. This creates the foundations for incorporating security requirements as functional requirements in the early analysis of the business processes, which is critically needed in the development of methods for the design of secure information systems (Siponen et al., 2006).

It has been recognized that a central issue in inter-organizational knowledge sharing is the nature and context of the knowledge exchange, what knowledge is to be shared, and under what conditions. A desirable outcome of enforcing the relationships between agents, business activities and resources is accountability of resource utilization and non-repudiation of business activities. When agents fulfill organizational roles by performing business activities, their function is monitored for exceptions and logged for validation of authorization requirements. This affords the organization the ability for nonrepudiation of business activities in the business process. Roles specify organizational functions responsible for specific activities and provide mechanisms for non-repudiation and auditing. This is viewed by SupplyCo managers as particularly useful when activities are performed by the partner organization. The mapping allows us to have the big picture about the different agents and resources involved in the execution of the business processes. For example, SupplyCo will be able to provide documentation that exception reports were submitted and incorporated into the demand forecast adjustments sent to the customer organization. This is valuable information for compliance purposes as well as for providing justification for pricing and overhead cost decisions for irregular shipments. The director of planning and replenishment said, “In any kind of collaborating processes we have to have accountability mechanisms for not only our own employees but also players from the buyer organizations. This kind of granularity provided by the mapping can be easily used to trace back the actors.”

The artifact describes access control and security constructs that allow local and global entities to share and describe various security requirements in common semantics for distributed knowledge and information exchange. Paraphrasing the remarks of the CIO of SupplyCo, this helps the company understand the delicate balance between accessibility, transparency, and security and allows it to put documented security needs on the table in discussions with the customer organization.

Semantic inter-operability through semantic conflict resolution has significant impact on the integration of the heterogeneous systems within SupplyCo, as well as systems that exchange data between SupplyCo and its major customer in the DFCP business processes. Delineation of a common ontological structure for the information exchanged between the organizations provides a basis to move manual processes back into the systems. Implementing a common ontology of resources for these business activities will allow SupplyCo to move these activities from a timeconsuming and error prone manual process to a system that requires managerial oversight and approval. In this way, errors can be avoided, and significant amounts of time can be saved by managing the semantic conflict resolution as an exception rather than as the norm. SupplyCo currently hosts weekly meetings with the customer where managers sit with individual laptops and resolve issues with semantic conflicts for a variety of ad-hoc issues including new products, promotion codes for the customer organization, packaging issues for SupplyCo, and product bundling for promotions. When conflicts are resolved and agreements are reached, the revised information is manually entered by customer development officers and directors of planning and execution. The proposed IT artifact can be used to develop semantic wrappers to dynamically solve semantic conflicts and feed the subsequent systems. An overall view of the business process and its constituent business activities, along with semantically consistent ontological definitions of the various resources utilized in the business process, assists in developing a common vocabulary of terms used in the process. This saves valuable time and money, and reduces the chance of errors in data input in the affected business process. SupplyCo’s director of planning and replenishment said, “This kind of approach will help us to integrate multiple dispersed data and information sources, to reduce inaccurate information and errors, and definitively it will assist us in advancing toward having real collaborative processes.”

The DFCP business process we chose to analyze is a challenging, complex, and dynamic business process, critical to the organizations involved. Here, secure exchange of the information that provides access to the right people in an effective manner is a critical requirement. We believe that the approach is applicable to business processes where secure and effective knowledge exchange across heterogeneous and distributed environments is a key requirement for the business process to achieve its objectives.

Our analysis and discussions regarding CPFR and the case study presented here tell us that the proposed IT artifact has the potential to benefit organizations that are planning to adopt CPFR as well as organizations that have already adopted it. As mentioned earlier, CPFR technical guidelines do not consider security knowledge. Here, we have shown how the security of CPFR business processes can be enhanced by incorporating roles and permissions needed in coordinating and executing secure business processes. Additionally, since CPFR business processes require the integration of heterogeneous data sources, we provide the foundations to develop ontologies that form a standardized vocabulary to support transparent and secure exchange of unambiguous machineinterpretable knowledge across business partners in a value chain, for both dyadic and multi-party relationships. A key success factor for CPFR is to integrate CPFR processes into existing business processes. In this context, the proposed IT artifact can be used to develop semantic wrappers to dynamically feed CPFR data and information to MRP and other ERP systems. Although we have not applied our approach to the specific business processes of organizations that have developed and adopted the CPFR industry standard, demonstrating the applicability of the approach to model processes of an industry standard does provide a level of confidence that the approach presented here can be used by other companies’ business processes.

## 7. Summary, Limitations and Directions for Future Research

A central premise of our research is that information and knowledge sharing in an information supply chain occurs in the context of business process, and that knowledge is a strategic resource that must be shared to be useful and applicable for inter-organizational business processes in the ISC. We proposed a design artifact to secure and coordinate business processes in the information supply chain. In our artifact, information and knowledge resources are expressed in standardized, computationally-feasible knowledge representation languages and shared in a secure and coordinated manner in the business process. We illustrate mechanisms to incorporate the systematic representation of component knowledge (Tallman et al, 2004), process knowledge (van der Aalst and Kumar, 2003), and security knowledge (Sandhu et al., 1996) in the design of secure and coordinated eBusiness processes. From the evaluations presented here, it is our assertion that our approach contributes to the design of secure and coordinated business processes in the ISC.

The utility and application of SSCIOBP is demonstrated using multiple evaluation methods from the IS knowledge base. We not only show how the SSCIOBP approach can be used to map industry standards such as the Collaborative Planning Forecasting and Replenishment (CPFR), but also how SSCIOBP can be utilized to enhance the security and systematic integration of information flows and knowledge resources of inter-organizational business processes. Moreover, using a real-world case study, we illustrate how SSCIOBP provides a holistic framework to integrate component, process, and security knowledge that enables the sharing of information and knowledge resources in a coordinated and secure manner within and across organizations of a value chain. The design artifact was validated by mapping the real core business processes of a large retail organization. By using real core business processes, we capture both the information and knowledge, including component, process, and security knowledge related to the business processes and the richness of the organizational environment. The contributions of this research are two-fold. On one hand, we provide to practitioners the meta-design and relevant examples that can be used to systematically incorporate the secure and coordinated exchange of information and knowledge resources in the design of business processes across the ISC. Second, SSCIOBP contributes to solve semantic conflict issues, to prevent unauthorized access to resources, to foster knowledge exchange, and to integrate heterogeneous systems of an ISC.

We use Hevner et al. guidelines (2004) to summarize the main aspects of the design artifact in Table 7.

Although we diligently followed the design science guidelines proposed by Hevner et al. (2004), March and Smith (1995), Walls et al. (1992), and Vaishnavi et al. (2006), our research has some limitations. First, we base our evaluation on the CPFR industry standard and apply the design artifact to a relevant case of a complex business problem in a large organization. While CPFR models are used by numerous organizations, one must be careful in drawing generalizations to other organizations and industries. Single cases and analysis of industry standards have been used in research similar to ours. For example, Sikora and Shaw (1998) show the application of a multi-agent framework for coordination using a single case that illustrates a manufacturing problem in a printed circuit-boards facility. Soffer and Wand (2007) present a generic process model and demonstrate its utility by application to the Supply Chain Operations Reference-model (SCOR). Second, the CPFR

<table><tr><td colspan="2">Table 7: A Design Science approach for SSCIOBP</td></tr><tr><td>Guideline</td><td>SSCIOBP Description</td></tr><tr><td>Design as an Artifact</td><td>We develop the constructs, models, methods and instantiation for the SSCIOBP design artifact. The SSCIOBP design artifact defines the atomic concepts and the relationship among them.</td></tr><tr><td>Problem Relevance</td><td>We answer the research questions:1. How can we systematically incorporate the secure and coordinated exchange of information and knowledge resources in the design of business processes across the ISC?2. How can we express and incorporate access control policies that comply with security requirements for activities and resources involved in business processes within and across organizations?3. How can we represent information and knowledge resources in standardized and expressive formats to enable automated and integrated collaborative business processes across the ISC?The following speak to the relevance of the research questions:i. The ISC requires collaborating organizations to exchange information and knowledge resources in a coordinated and secure manner to efficiently conduct inter-organizational business processes. Seamless knowledge exchange within and across organizations involved in secure business processes is critically needed to “secure and cultivate the information supply chain”.ii. Organizations engaged in collaborative inter-organizational processes continue to be plagued with semantic conflict issues and a lack of integration in heterogeneous systems.iii. The lack of process visibility across organizations mitigates the development of trust between the partner organizations. This is confounded by the lack of security knowledge regarding authorized access to resources.iv. A holistic consideration in the design of information systems to support secure and coordinated business processes is critical to securing and cultivating the ISC. However, extant literature does not explicitly consider or systematically represent component knowledge of resources such as description of skills and product knowledge; process knowledge including process workflow models; and security knowledge of authorized access for activities to resources within and across organizations.</td></tr><tr><td>Design Evaluation</td><td>The utility and application of SSCIOBP was demonstrated using multiple evaluation methods from the IS knowledge base.i. We show how the Collaborative Planning, Forecasting, and Replenishment (CPFR) approach can be mapped and enhanced by applying the proposed IT artifact.ii. The design artifact was validated by mapping real core business processes of a large retail organization. By using real core business processes, we capture both the information and knowledge, including component, process, and security knowledge related to the business processes and the richness of the organizational environment.</td></tr><tr><td>Research Contribution</td><td>i. SSCIOBP provides mechanisms for the systematic representation of component knowledge (Tallman et al, 2004), process knowledge (van der Aalst and Kumar, 2003) and security knowledge (Sandhu et al., 1996) in the design of secure and coordinated eBusiness processes.ii. We provide to practitioners the meta-design and relevant examples that can be used to systematically incorporate the secure and coordinated exchange of information and knowledge resources in the design of business processes across the ISC.</td></tr></table>

model and the case study used in this paper show a dyadic supply chain. Therefore, to increase the validity of our design artifact, more complex relationships need to be analyzed. It is important to mention that this practice is a common one, given the difficulties in modeling multi-echelon supply chains; for instance, Nissen and Sengupta (2006) show how intelligent agents can enhance supply chain performance. Finally, we evaluated our artifact using two approaches, observational and descriptive. However, in order to increase the generalizability of the proposed artifact, we suggest that further evaluation is needed. Baskerville et al. (2007) advocate the use of “soft” methods including interpretive studies that treat the problem as a complex phenomenon that should be studied in its natural environment. They argue for the use of methods, including case studies and field studies in order to avoid errors in the evaluation of the artifact. We plan to conduct controlled experiments and simulations to further test our proposed artifact across multiple domains and using industry defined eBusiness processes in supply chains and eMarketplaces.

In this paper, we use an explicit, not tacit, definition of knowledge that is declarative enough for standards-based knowledge representation formalisms, such as DL and OWL. We recognize that this is a limitation of our research. It is particularly difficult for tacit knowledge to be explicated and effectively represented using computational techniques. While we provide the structure for representing explicit knowledge, we do not provide insight in incorporating tacit knowledge in this research. We take this pragmatic limitation on knowledge for practical reasons. To develop mechanisms to build knowledge-based systems that are viable and useful, it may be worthwhile to focus on declarative and explicit knowledge that can be represented using computationally feasible knowledge representation languages first.

Despite these limitations, the approach presented in this paper is well grounded in kernel theories and has been evaluated using a rigorous, multi-method approach. Our semantic approach to secure collaborative inter-organizational eBusiness processes (SSCIOBP) integrates streams of research in design science paradigm, eBusiness Process, authorization and Role-Based Access Control, ontology, DL, and Semantic Web technologies. A business process provides the context and globa perspective to information and knowledge sharing within and across organizational boundaries. This approach can be used to describe the roles, permissions, resources, and security requirements by creating a standardized vocabulary that describes access control and security for distributed information and knowledge sharing. It provides practitioners with the meta-design and relevant examples that can be used to develop semantically rich models of business processes that can be verified through DL formalisms and readily converted to standardized machine-interpretable knowledge representation. It provides an integrative mechanism for detailed analysis of business processes including the business enterprises and their agents involved, the roles they fulfill, the activities they perform, and coordination mechanism and access control policies with respect to knowledge resources of organizations in the information supply chain.

## Acknowledgements

A preliminary version of the paper was presented at the CABIT 2006 Symposium in Phoenix, Arizona. We thank the attendees of CABIT 2006 for their valuable comments. We also thank the anonymous reviewers and the editors for their encouraging remarks and constructive feedback that helped improve the paper significantly.

## References

Agarwal, R., De, P., and Sinha, A. (1999) “Comprehending Object and Process Models: An Empirical Study,” IEEE Transactions on Software Engineering, (25) 4, pp. 541-556.

Anand, K.S. and H. Mendelson (1997) “Information and Organization for Horizontal Multi-market Coordination,” Management Science, (43) 12, pp. 1609-1627.

Apvrille, A., and M. Pourzandi (2005) “Secure Software Development by Example,” IEEE Security and Privacy, (3) 4, pp.10-17.

Atallah, M., Blanton, M., Deshpande, V., Frikken, K., Li, J., and Schwarz, L. (2006) “Secure Collaborative Planning, Forecasting, and Replenishment (SCPFR),” In Proceedings of Multi-

Echelon Inventory Conference.

Baader, F., Calvanese, D., McGuinness, D., Nardi, D., and Patel-Schneider, P.F., (eds.) (2003) The Description Logic Handbook: Theory, Implementation and Applications. Cambridge: Cambridge University Press.

Badaracco, J. L. (1991) The Knowledge Link, Boston, MA; Harvard Business School Press.

Baskerville, R. (1998) Designing Information Systems Security, John Wiley & Sons, New York.

Baskerville, R., Pries-Heje, J., and Venable, J. (2007) “Soft Design Research: Extending the Boundaries of Evaluation in Design Research,” In Proceedings of the 2nd DESRIST Conference, May 13-15 2007, Pasadena, CA, pp. 19-38.

Basu, A., and A., Kumar (2002) “Research Commentary: Workflow and Management Issues in e-Business,” Information Systems Research, (13) 1, pp. 1-14.

Benjamin, R., I., De Long, D. W., and Scott Morton, M.C. (1990) “Electronic Data Interchange: How Much Competitive Advantage?,” Long Range Planning (UK), (23) 1, pp 28-40.

Berners-Lee, T., Hendler, J. and Lassila, O. (2001) “The Semantic Web,” Scientific American,pp.34- 43.

Caridi, M., Cigolini, R., De Marco, D. (2005) “Improving Supply-Chain Collaboration by Linkig Intelligent Agents to CPFR,” International Journal of Production Research, (43) 20, pp. 4191- 4218.

Carpenter, B., and P. Janson. (2004) “Abstract Interdomain Security Assertions: A Basis for Extra-Grid Virtual Organizations,” IBM Systems Journal, (43) 4, pp. 689-701.

Crowston, K. and Osborn, C. (2003) “The Interdisciplinary Study of Coordination,” in Malone, T. W., Crowston, K., and Herman, G. A., (eds.), Organizing business knowledge: the MIT process handbook, MIT Press, Cambridge, Massachusetts.

Daft, R. (1983) Organization Theory and Design. New York: West.

Davenport, T.H., and L. Prusak (1998) Working Knowledge: How organizations Manage What They Know, Harvard Business School Press. Boston, MA.

Davenport, T.H., Short, E.J. (1990), "The new industrial engineering: information technology and business process redesign", Sloan Management Review, pp.11-27.

Elgarah, W., Falaleeva, N., Saunders, C. C., Ilie, V., Shim, J. T., and Courtney, J. F. (2005) “Data Exchange in Interorganizational Relationships: Review through Multiple Conceptual Lenses,” SIGMIS Database, (36) 1, pp. 8-29.

Gomez-Perez, A., Fernandez-Lopez, M., and Corcho, O. (2004) Ontological Engineering. Springer, London.

Gordon, L., Loeb, M., Lucyshyn, W., and Richardson, R. (2006) Eleventh Annual CSI/FBI Computer Crime and Security Survey, Computer Security Institute.

Grant, R. (1996), “Toward a Knowledge-base Theory of the Firm,” Strategic Management Journal, 17, pp. 109-122.

Guarino, N. (1995) “Formal Ontology, Conceptual Analysis and Knowledge Representation,” International Journal of Human and Computer Studies, (43) 5/6, pp. 625-640.

Hackbarth, G. and W., Kettinger (2000) “Strategic Aspirations for Net-Enabled Business,” European Journal of Information Systems, (13), pp. 273-285.

Hamel, G. (1991) “Competition for Competence and Inter-Partner Learning with International Strategic Alliances,” Strategic Management Journal, (12), pp. 83-103.

Hevner, A., March, S.T., Park, J., and Ram, S. (2004) “Design Science Research in Information Systems,” MIS Quarterly, (28) 1, pp. 75-105.

Holsapple, C., and Singh, M. (2000) “Toward a Unified View of Electronic Commerce, Electronic Business, and Collaborative Commerce: A Knowledge Management Approach,” Knowledge and Process Management, (7) 3, pg. 159.

Hult, G., Ketchen, D., and Slater, S. (2004) “Information Processing, Knowledge Development, and Strategic Supply Chain Performance,” Academy of Management Journal, (47) 2, pp. 241-253.

Joshi, et al. (2001) “Security model for Web-based Applications,” Communication of the ACM (44) 2, pp. 38-44

Khatri, V., Vessey, I., Ramesh, V., Clay, P., and Park, S. (2006) “Understanding Conceptual Schemas: Exploring the Role of Application and IS Domain Knowledge,” Information Systems Research, (17) 1, pp.81-99.

Kishore, R., Zhang, H., and Ramesh, R. (2006) “Enterprise integration using the agent paradigm:

foundations of multi-agent-based integrative business information systems”, Decision Support Systems, (42) 1, pp. 48-78.

Klein, M., Fensel, D., van Harmelen, F., and Horrocks, I. (2001) “The Relation Between Ontologies and XML Schemas,” Electronic Transactions on Artificial Intelligence (ETAI), Linköping Electronic Articles in Computer and Information Science, (6) 4.

Lee, H., and S., Whang (1998) Information Sharing in a Supply Chain Research Paper Series, Graduate School of Business, Stanford University.

Lee, H., So, K., and Tang, C. (2000) "The Value of Information Sharing in a Two-level Supply Chain," Management Science (46) 5, pp 626-643.

Lee, H.L., Padmanabhan, V., and Whang, S. (1997) "Information Distortion in Supply Chain: The Bullwhip Effect," Management Science (43) 4, pp 546-558.

Lee, Y., Lee, J., and Lee, Z. (2002) “Integrating Software Lifecycle Process Standards with Security Engineering,” Computer and Security, (21) 4, pp. 345-355.

Li, L. and I., Horrocks (2004) “A Software Framework for Matchmaking Based on Semantic Web Technology,” International Journal of Electronic Commerce, (8) 4, pp. 39-60.

Loebecke, C., van Fenema, P. and Powell, P. (1999) “Co-Opetition and Knowledge Transfer,” Database for Advances in Information Systems, (30) 2, pp. 14-25.

Lorange, P. (1996) “Strategy at the Leading Edge –Interactive Strategy- Alliances and Partnership,” Long Range Planning, (29) 4, pp. 581-584.

Malone, T. W., Crowston, K., and Herman, G. A. (2003) editors, Organizing business knowledge: the MIT process handbook, MIT Press, Cambridge, Massachusetts.

Malone, T. W., Yates, J., and Benjamin, R. I. (1987) “Electronic Markets and Electronic Hierarchies,” Communications of the ACM, (30) 6, pp. 484-497.

March, S., Hevner, A., Ram, S. (2000) “Research Commentary An Agenda for Information Technology Research in Heterogeneous and Distributed Environments,” Information Systems Research, (11) 4, pp. 327-341.

March, S.T., and Smith, G. (1995) “Design and Natural Science Research on Information Technology,” Decision Support Systems, (15) 4, pp. 251-266.

Markus, M.L., Majchrzak, A., and Gasser, L. (2002) “A Design Theory for Systems that Support Emergent Knowledge Processes,” MIS Quarterly, (26) 3, pp. 179-212.

McIlraith, S., Son, T.C. and Zeng, H., (2001) “Semantic Web Services,” IEEE Intelligent Systems, pp. 46-53.

Mouratidis, H., Giorgini, P., and Manson, G. (2005) “When Security Meets Software Engineering: A Case of Modelling Secure Information Systems,” Information Systems (30), pp. 609-629.

Newell, A. (1982) “The Knowledge Level,” Artificial Intelligence, (18), pp. 87-127.

Nissen, M. and K., Sengupta (2006) “Incorporating Software Agents into Supply Chains: Experimental Investigation with a Procurement Task,” MIS Quarterly, (30), pp. 145-166.

Noy, N. F. and D. L. McGuinnss (2002) Ontology Development 101: A Guide to Creating Your First Ontology. Stanford University, Stanford, CA, Stanford Medical Informatics Report SMI-2002- 0880.

Oh, S. and Park, S. (2003) “Task-role-based Access Control Model,” Information Systems (28) 6, pp. 533-562.

Park, J. S., Sandhu, R., and Ahn, G. (2001) “Role-Based Access Control on the web”, ACM Transactions on Information and Systems Security, (4) 1, pp. 37-71.

Porter, M.E., Millar, V.E. (1985) “How Information Gives You Competitive Advantage”, Harvard Business Review, (63) 4.

Raghu, T.S. and A., Vinze (2007) “A Business Process Context for Knowledge Management,” Decision Support System, In press.

Rai, A., Patnayakuni, R., and Patnayakuni, N. (2006) “Firm Performance Impacts of Digitally Enabled Supply Chain Integration Capabilities,” MIS Quarterly, (30) 2, pp. 225-246.

Ram, S. and J. Park (2004) “Semantic Conflict Resolution Ontology (SCROL): An Ontology for Detecting and Resolving Data and Schema Level Conflicts", IEEE Transactions on Knowledge and Data Engineering, (16) 2, pp. 189-202.

Sandhu, R.S., Coyne, E.J., Feinstein, H.L., and Youman, C.E. (1996) “Role-Based Access Control Models,” IEEE Computer, (29) 2, pp. 38-47.

Sawhney, M., and D., Parikh (2001) “Where Value lies in a Networked World,” Harvard Business

Review, pp. 79-86.

Schwarz, L. (2004) “The State of Practice in Supply-Chain Management Perspective,” in Applications of Supply Chain Management and E-Commerce Research in Industry, E. Akcali, J. Geunes, P.M. Pardalos, H.E. Romeijn, and Z.J. Shen (eds.), Kluwer, Academic Publishers, Dordrecht, The Netherlands.

Segars, A.H., and Chatterjee, D. (2003). "An Overview of Contemporary Practices and Trends," in: Transformation of the Enterprise through eBusiness, Society for Information Management.

Sikora, R., and M.J., Shaw (1998) “A Multi-Agent Framework for the Coordination and Integration of Information Systems,” Management Science, (44) 11, pp. S65-S78.

Simonin, B. L. (1999) "Ambiguity and the process of knowledge transfer in strategic alliances", Strategic Management Journal, (20), pp. 595-623.

Singh, R. and Salam, A.F. (2006) "Semantic Information Assurance for Secure Distributed Knowledge Management: A Business Process Perspective" IEEE Transactions on Systems, Man and Cybernetics, (36) 3, pp. 472-486.

Singh, R., Iyer, L.S., and Salam, A.F. (2005) “Semantic eBusiness,” International Journal of Semantic Web and Information Systems, (1) 1, pp. 19-35.

Siponen, M., Baskerville, R., and Heikka, J. (2006) “A Design Theory for Secure Information Systems Design Methods, “Journal of the Association for Information Systems, (7) 11, pp. 725-770.

Sivashanmugam, K., Miller, J. A., Seth, A. P. and Verma, K. (2004) “Framework for Semantic Web Process Composition,” International Journal of Electronic Commerce, (9) 2, pp. 71-106.

Soffer, P. and Y., Wand (2007) “Goal-Driven Multi-Process Analysis,” Journal of the Association for Information Systems (8) 3, pp.175-203.

Srinivasan, A., March, A., and Saunders, C. (2005) “Information Technology and Organizational Contexts: Orienting Our Work Along Key Dimensions,” in Proceedings of The Twenty-Sixth International Conference on Information Systems, Las Vegas, NV, USA, pp. 991-1001.

Swaminathan, J., and S., Tayur (2003) “Models for Supply Chains in E-Business,” Management Science, (49) 10, pp. 1387-1406.

Tallman, S., Jenkins, M., Henry, N., Pinch, S. (2004) “Knowledge, Clusters and Competitive Advantage,” Academy of Management Review, (29) 2, pp. 258-271.

The National Institute of Standards and Technology (NIST),( 2004) available at http:// csrc.nist.gov/rbac. Accessed on November, 2006.

Thomas, M., Redmond, R. T., Yoon, V., and Singh, R. (2006) “A Semantic Approach to Monitoring Business Process Performance”, Communications of the ACM, (48) 12, pp. 55-59.

Vaishnavi, V. and B., Kuechler “Design Research in Information Systems,” http://www.isworld.org/Researchdesign/drisISworld.htm, Accessed December, 2006.

van der Aalst, W.M.P. and Kumar, A. (2003) “XML Based Schema Definition for Support of Inter-Organizational Workflow,” Information Systems Research, (14) 1, pp.23-46.

VICS, (1999), CPFR Technica Specifications, available at http://www.vics.org/standards/cpfr\_roadmap\_case\_studies/13\_5\_CPFR\_specifications.pdf. Accesses on November, 2006.

VICS, (2004), Voluntary Inter-industry Commerce Standards Association (VICS) -Collaborative Planning, Forecasting and Replenishment (CPFR®), available at http://www.vics.org/committees/cpfr/CPFR\_Overview\_US-A4.pdf. Accessed on November 2006.

Walls, J.G., Widmeyer, G.R., and El Sawy, O. A. (1992) “Building an Information System Design Theory for Vigilant EIS,” Information Systems Research, (3)1, pp. 36-59.

Wand, Y. and R., Weber (2002) "Research Commentary: Information Systems and Conceptual Modeling–A Research Agenda," Information Systems Research, (13) 4, pp. 363-376.

WfMC,(1996) Workflow Management Coalition, www.wfmc.org.

## Appendix A

## Appendices

<table><tr><td colspan="3">List of Buyers and Suppliers Participating in CPFR Partnerships</td></tr><tr><td colspan="3">Buyer Organizations</td></tr><tr><td>10 Internal Affiliates</td><td>4 Retailers</td><td>850 n-Tier Partners</td></tr><tr><td>Ace Hardware</td><td>Albertson&#x27;s</td><td>Best Buy</td></tr><tr><td>Canadian Tire</td><td>CVS</td><td>Dansk</td></tr><tr><td>Dealers</td><td>Delhaize le Lion</td><td>Distributors</td></tr><tr><td>Do It Best</td><td>Eckerd</td><td>Federated Department Stores</td></tr><tr><td>H.E. Butt</td><td>Home Depot</td><td>J.C. Penny</td></tr><tr><td>Jusco</td><td>Londis</td><td>Marshall Field&#x27;s</td></tr><tr><td>Match Supermarket</td><td>McDonald&#x27;s US/ McDonald&#x27;s France</td><td>Mijer</td></tr><tr><td>Mervyn&#x27;s</td><td>Radio Shack</td><td>RiteAid</td></tr><tr><td>Royal Ahold</td><td>RONA</td><td>Safeway/Safeway UK</td></tr><tr><td>Safe</td><td>Sainsbury</td><td>SAKS</td></tr><tr><td>Sears Roebuck</td><td>Somerfield</td><td>Sports Authority</td></tr><tr><td>Staples</td><td>Superdrug</td><td>Target</td></tr><tr><td>Tesco</td><td>Tru Value</td><td>Walgreens</td></tr><tr><td>Wal-Mart</td><td>Wickes Furniture</td><td>Woolworth UK</td></tr><tr><td colspan="3">Supplier Organizations</td></tr><tr><td>12 Suppliers</td><td>20+ Suppliers</td><td>Ashley Furniture</td></tr><tr><td>Ball Sports</td><td>Black &amp; Decker</td><td>Broyhill</td></tr><tr><td>Channel</td><td>Chapin</td><td>Colgate-Palmolive</td></tr><tr><td>Compaq</td><td>Eastman Chemicals</td><td>ECPG3</td></tr><tr><td>Eli Lily</td><td>Feather Fruit Growers&#x27; Cooperative</td><td>FujiFilm</td></tr><tr><td>GE Appliances</td><td>General Mills</td><td>Genovs</td></tr><tr><td>Georgia Pacific</td><td>Harley-Davidson</td><td>Hasbro</td></tr><tr><td>Heineken</td><td>Henkel</td><td>Herlitz</td></tr><tr><td>Hewlett-Packard</td><td>HYKo</td><td>Inland Paperboard &amp; Packaging</td></tr><tr><td>International Paper</td><td>John Deere</td><td>Johnson &amp; Johnson</td></tr><tr><td>Kao</td><td>Kimberly Clark</td><td>Kraft</td></tr><tr><td>Lever-Fabrege</td><td>Levi Strauss</td><td>Liquid Nails</td></tr><tr><td>Liz Claiborne</td><td>Manco</td><td>Mars</td></tr><tr><td>Master Lock</td><td>Meriat</td><td>Mitsubishi Motor</td></tr><tr><td>Nestle UK</td><td>New Balance</td><td>Panasonic</td></tr><tr><td>Philips Consumer</td><td>Pillowtex</td><td>Polo Ralph Lauren</td></tr><tr><td>Proctor &amp; Gamble</td><td>Reynolds Metal</td><td>Sara Lee</td></tr><tr><td>Schering-Plough</td><td>Solo Cup</td><td>Unilever Argentina</td></tr><tr><td>Vandemoortele of Belgium</td><td>Warner-Lambert</td><td>Woodstream</td></tr><tr><td colspan="3">Source: Schwarz, L. (2004)</td></tr></table>

```txt
Appendix B

Appendix B-1. Seller agent creates order forecast activity to coordinate order forecast
CreateOrderForecast ⊆ (BusinessActivity) ∧
(= 1 IsPerformedby.SellerRole) ∧
(= 1 HasCoordinationFlowConsumes. POSData) ∧
(= 1 HasCoordinationFlowConsumes. ForecastImpactEvents) ∧
(= 1 HasCoordinationFlowConsumes. InventoryStrategy ) ∧
(= 1 HasCoordinationFlowConsumes. CurrentInventory ) ∧
(= 1 HasCoordinationFlowConsumes. SalesForecast ) ∧
(= 1 HasCoordinationFlowConsumes. OrderForecast) ∧
(= 1 HasCoordinationFlowConsumes. ExceptionResolutionData ) ∧
(= 1 HasCoordinationFlowConsumes. ItemManagementData ) ∧
(= 1 HasCoordinationFlowConsumes. CapacityLimitations ) ∧
(= 1 HasCoordinationFlowConsumes. HistoricalDemandShipment ) ∧
(= 1 HasCoordinationFlowConsumes. OrderShipmentData ) ∧
(= 1 HasCoordinationFlowProduces. OrderForecast) ∧
(= 1 HasPermissionRead. POSData) ∧
(= 1 HasPermissionRead. ForecastImpactEvents) ∧
(= 1 HasPermissionRead. InventoryStrategy ) ∧
(= 1 HasPermissionRead. CurrentInventory ) ∧
(= 1 HasPermissionRead. SalesForecast ) ∧
(= 1 HasPermissionRead. OrderForecast) ∧
(= 1 HasPermissionRead. ExceptionResolutionData ) ∧
(= 1 HasPermissionRead. ItemManagementData ) ∧
(= 1 HasPermissionRead. CapacityLimitations ) ∧
(= 1 HasPermissionRead. HistoricalDemandShipment ) ∧
(= 1 HasPermissionRead. OrderShipmentData ) ∧
(= 1 HasPermissionRead. OrderForecast) ∧
(= 1 HasPermissionWrite. OrderForecast) ∧
(= 1 HasPermissionCreate. OrderForecast)

Appendix B-2. Sellers create their order forecast using standardized ontology for specifying the resource
OrderForecast ⊆ (Resource) ∧
(= 1 IsOwnedBy. Seller) ∧
(= 1 hasID .8) ∧
(=1 CoordinatesFlowProducedBy.CreateOrderForecast ) ∧
(= 1 CoordinatesFlowConsumedBy . GenerateOrder) ∧
(=1 Permits .CreateOrderForecast ) ∧
(= 1 Permits . GenerateOrder) ∧
(=1 hasCharacteristics. ForecastType) ∧
(=1 hasCharacteristics. GenerationDate) ∧
(=1 hasCharacteristics. StartDate) ∧
(=1 hasCharacteristics. EndDate) ∧
(=1 hasCharacteristics. ProductID) ∧
(=1 hasCharacteristics.Quantity) ∧
(=1 hasCharacteristics.ChangeRestrictionIndicator)

Appendix B-3. The seller agent generates order activity to coordinate order
GenerateOrder ⊆ (BusinessActivity) ∧
(= 1 IsPerformedby.SellerRole) ∧
(= 1 HasCoordinationFlowConsumes. Order) ∧
```

```txt
(= 1 HasCoordinationFlowConsumes. ItemManagementData) ∧
(= 1 HasCoordinationFlowConsumes. OrderForecast ) ∧
(= 1 HasCoordinationFlowProduces. Order) ∧
(= 1 HasPermissionRead. Order) ∧
(= 1 HasPermissionRead. ItemManagementData) ∧
(= 1 HasPermissionRead. OrderForecast) ∧
(= 1 HasPermissionRead. Order) ∧
(= 1 HasPermissionWrite. Order) ∧
(= 1 HasPermissionCreate. Order)

Appendix B-4. Sellers communicate their order data using standardized ontology for specifying the resource
Order ⊆ (Resource) ∧
(= 1 IsOwnedBy· Buyer) ∧
(= 1 hasID .9) ∧
(=1 CoordinatesFlowProducedBy.CommunicateOrder ) ∧
(= 1 CoordinatesFlowConsumedBy . GenerateOrder) ∧
(=1 Permits .CommunicateOrder ) ∧
(= 1 Permits . GenerateOrder)

Appendix B-5. Seller planning agent communicates adjustments to coordinate the Create Order Forecast activity
CommunicateAdjustments ⊆ (BusinessActivity) ∧
(= 1 IsPerformedby.SellerPlanningRole) ∧
(= 1 HasCoordinationFlowProduces. Adjustments) ∧
(= 1 Has PermissionRead. Adjustments) ∧
(= 1 HasPermissionWrite. Adjustments)

Appendix B-6. Buyers receive adjustments using standardized ontology for specifying the resource
Adjustments ⊆ (Resource) ∧
(= 1 IsOwnedBy· Buyer) ∧
(= 1 hasID .7) ∧
(= 1 CoordinatesFlowProducedBy . CommunicateAdjustments ) ∧
(= 1 CoordinatesFlowConsumedBy . ReceiveAdjustments) ∧
(= 1 Permits . CommunicateAdjustments) ∧
(= 1 Permits . ReceiveAdjustments) ∧
(>= 1 hasCharacteristics. ProductID) ∧
(>= 1 hasCharacteristics. RightQuantity) ∧
(>= 1 hasCharacteristics. Date)

Appendix B-7. The buyer planning agent receives adjustments to coordinate the Create Order Forecast activity
ReceiveAdjustments ⊆ (BusinessActivity) ∧
(= 1 IsPerformedby.BuyerPlanningRole) ∧
(= 1 HasCoordinationFlowConsumedBy. Adjustments) ∧
(= 1 Has PermissionRead. Adjustments)

Appendix B-8. Activity Creates Order Forecast, which is performed by the seller forecast agent
CreateOrderForecast ⊆ (BusinessActivity) ∧
(= 1 IsPerformedby.SellerForecastRole) ∧
```

```vba
(= 1 HasCoordinationFlowConsumes. POSData) ∧
(= 1 HasCoordinationFlowConsumes. EventsCalendar) ∧
(= 1 HasCoordinationFlowConsumes. InventoryStrategy ) ∧
(= 1 HasCoordinationFlowConsumes. AvailableStock ) ∧
(= 1 HasCoordinationFlowConsumes. SalesForecast ) ∧
(= 1 HasCoordinationFlowConsumes. OrderForecast) ∧
(= 1 HasCoordinationFlowConsumes. ExceptionResolutionData ) ∧
(= 1 HasCoordinationFlowConsumes. ItemManagementData ) ∧
(= 1 HasCoordinationFlowConsumes. HistoricalDemandShipment ) ∧
(= 1 HasCoordinationFlowConsumes. OrderShipmentData ) ∧
(= 1 HasCoordinationFlowConsumes. CPFRPolicies ) ∧
(= 1 HasCoordinationFlowProduces. OrderForecast) ∧
(= 1 HasCoordinationRead. POSData) ∧
(= 1 HasCoordinationRead. EventsCalendar) ∧
(= 1 HasCoordinationRead. InventoryStrategy ) ∧
(= 1 HasCoordinationRead. AvailableStock ) ∧
(= 1 HasCoordinationRead. SalesForecast ) ∧
(= 1 HasCoordinationRead. OrderForecast) ∧
(= 1 HasCoordinationRead. ExceptionResolutionData ) ∧
(= 1 HasCoordinationRead. ItemManagementData ) ∧
(= 1 HasCoordinationRead. HistoricalDemandShipment ) ∧
(= 1 HasCoordinationRead. OrderShipmentData ) ∧
(= 1 HasCoordinationRead. CPFRPolicies ) ∧
(= 1 HasPermissionWrite. OrderForecast) ∧
(= 1 HasPermissionCreate. OrderForecast)
```

```txt
Appendix B-9. Sellers create their order forecast using standardized ontology for specifying the resource
OrderForecast ⊆ (Resource) ∧
(= 1 IsOwnedBy · Seller) ∧
(= 1 hasID .12) ∧
(=1 CoordinatesFlowProducedBy.CreateOrderForecast ) ∧
(= 1 CoordinatesFlowConsumedBy . GenerateOrder) ∧
(=1 Permits .CreateOrderForecast ) ∧
(= 1 Permits . GenerateOrder) ∧
(=1 hasCharacteristics. ForecastType) ∧
(=1 hasCharacteristics. GenerationDate) ∧
(=1 hasCharacteristics. StartDate) ∧
(=1 hasCharacteristics. EndDate) ∧
(>=1 hasCharacteristics. ProductID) ∧
(>=1 hasCharacteristics. Quantity) ∧
(>=1 hasCharacteristics.MinQuantity) ∧
(>=1 hasCharacteristics.MaxQuantity) ∧
(>=1 hasCharacteristics.ChangeRestrictionIndicator)
```

## About the Authors

Fergle J. D’Aubeterre is a Ph.D. candidate in the Information Systems and Operations Management Department at The University of North Carolina at Greensboro. He obtained his MBA from Central Michigan University. His research interests include electronic commerce, business processes, Semantic Web, IT security and privacy, and global IT management. Fergle has published papers in journals such as Information Systems Journal; Electronic Government an International Journal; the Journal of Electronic Commerce Research; Encyclopedia of E-Commerce; E-Government, and Mobile Commerce; the Proceedings of the International Conference on Information Systems; the Proceedings of Americas Conference on Information Systems; the Proceedings of Global Information Technology Management; the Proceedings of the Design Science Research in Information Systems and Technology; and the Proceedings of the Decision Sciences Institute.

Rahul Singh is an Associate Professor in the Department of Information Systems and Operations Management, Bryan School of Business and Economics, at The University of North Carolina at Greensboro. He obtained his Ph.D. in Business from Virginia Commonwealth University. His research interests include Semantic eBusiness, Security of Systems, Secure Business Process Design, Knowledge Management, Intelligent Agents, Data mining and Machine learning. His research work has been published in leading IS Journals including IEEE Transactions on Systems, Man and Cybernetics, Communications of the ACM, Information Systems Management, eService Journal, International Journal of Semantic Web and Information Systems, International Journal of Intelligent Information Technologies, Information Resources Management Journal, International Journal of Production Engineering Socio-Economic Planning Sciences. He is the Editor-In-Chief for the Journal of Information Science and Technology (JIST). Dr. Singh is a member of the editorial board for the International Journal of Semantic Web and Information Systems, the International Journal for Intelligent Information Technologies, the Journal of Information Technology Theory and Applications, and the International Journal of Information Security and Privacy.

Lakshmi Iyer is an Associate Professor in the Information Systems and Operations Management Department, Bryan School of Business and Economics, at The University of North Carolina, Greensboro. She obtained her PhD from the University of Georgia, Athens. Her research interests are in the area of eBusiness Processes, eCommerce issues, IS privacy and security, IT and Healthcare, intelligent agents, Decision Support Systems and Knowledge Management. Her research work has been published in Communications of the ACM, eService Journal, Annals of OR, Decision Support Systems, Information Systems Management, International Journal of Semantic Web and Information Systems, Electronic Government an International Journal, Journal of Global Information Technology Management, and others. Dr. Iyer has served as a Guest Editor for Communications of the ACM and the Journal of Electronic Commerce Research. She is a Board member of Teradata University Network and also serves in the editorial board for the International Journal of Semantic Web and Information Systems and the International Journal of Information Security and Privacy.

Copyright © 2008, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Robert Kauffman</td><td>University of Minnesota, USA</td></tr><tr><td>Frank Land</td><td>London School of Economics, UK</td><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Yair Wand</td><td>University of British Columbia, Canada</td><td></td><td></td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Michael Barrett</td><td>University of Cambridge, UK</td></tr><tr><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td></tr><tr><td>Francois Bodart</td><td>University of Namur, Belgium</td><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Wynne Chin</td><td>University of Houston, USA</td><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College, USA</td><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td></tr><tr><td>Samer Faraj</td><td>University of Maryland, College Park, USA</td><td>Chris Forman</td><td>Carnegie Mellon University, USA</td></tr><tr><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td><td>Dennis Galletta</td><td>University of Pittsburg, USA</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bill Kettinger</td><td>University of South Carolina, USA</td><td>Rajiv Kohli</td><td>College of William and Mary, USA</td></tr><tr><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td><td>Ho Geun Lee</td><td>Yonsei University, Korea</td></tr><tr><td>Jae-Nam Lee</td><td>Korea University</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td><td>Ann Majchrzak</td><td>University of Southern California, USA</td></tr><tr><td>Ji-Ye Mao</td><td>Remnin University, China</td><td>Anne Massey</td><td>Indiana University, USA</td></tr><tr><td>Emmanuel Monod</td><td>Dauphine University, France</td><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Sudha Ram</td><td>University of Arizona, USA</td></tr><tr><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Raghu Santanam</td><td>Arizona State University, USA</td></tr><tr><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland, USA</td><td>Mani Subramani</td><td>University of Minnesota, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td></tr><tr><td>Richard T. Watson</td><td>University of Georgia, USA</td><td>Bruce Weber</td><td>London Business School, UK</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>J. Peter Tinsley</td><td>AIS, Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Robert Kauffman</td><td>University of Minnesota, USA</td></tr><tr><td>Frank Land</td><td>London School of Economics, UK</td><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Yair Wand</td><td>University of British Columbia, Canada</td><td></td><td></td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Michael Barrett</td><td>University of Cambridge, UK</td></tr><tr><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td></tr><tr><td>Francois Bodart</td><td>University of Namur, Belgium</td><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Wynne Chin</td><td>University of Houston, USA</td><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College, USA</td><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td></tr><tr><td>Samer Faraj</td><td>University of Maryland, College Park, USA</td><td>Chris Forman</td><td>Carnegie Mellon University, USA</td></tr><tr><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td><td>Dennis Galletta</td><td>University of Pittsburg, USA</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bill Kettinger</td><td>University of South Carolina, USA</td><td>Rajiv Kohli</td><td>College of William and Mary, USA</td></tr><tr><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td><td>Ho Geun Lee</td><td>Yonsei University, Korea</td></tr><tr><td>Jae-Nam Lee</td><td>Korea University</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td><td>Ann Majchrzak</td><td>University of Southern California, USA</td></tr><tr><td>Ji-Ye Mao</td><td>Remnin University, China</td><td>Anne Massey</td><td>Indiana University, USA</td></tr><tr><td>Emmanuel Monod</td><td>Dauphine University, France</td><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Sudha Ram</td><td>University of Arizona, USA</td></tr><tr><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Raghu Santanam</td><td>Arizona State University, USA</td></tr><tr><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland, USA</td><td>Mani Subramani</td><td>University of Minnesota, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td></tr><tr><td>Richard T. Watson</td><td>University of Georgia, USA</td><td>Bruce Weber</td><td>London Business School, UK</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>J. Peter Tinsley</td><td>AIS, Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
