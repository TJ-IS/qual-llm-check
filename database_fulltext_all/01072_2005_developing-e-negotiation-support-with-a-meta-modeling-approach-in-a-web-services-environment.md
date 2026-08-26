---
otero_id: 1072
otero_key: "GUKHJ4BC"
title: "Developing e-Negotiation support with a meta-modeling approach in a Web services environment"
authors: "Dickson K.W. Chiu; S.C. Cheung; Patrick C.K. Hung; Sherina Y.Y. Chiu; Andriy K.K. Chung"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.04.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Developing e-Negotiation support with a meta-modeling approach in a Web services environment

Dickson K.W. Chiu<sup>a,</sup>\*, S.C. Cheung<sup>b</sup>, Patrick C.K. Hung<sup>b</sup>, Sherina Y.Y. Chiu<sup>c</sup>, Andriy K.K. Chung<sup>c</sup>

<sup>a</sup> Dickson Computer Systems, 7A Victory Avenue 4th floor, Homantin, Kowloon, Hong Kong <sup>b</sup> Department of Computer Science, Hong Kong University of Science and Technology, Hong Kong Department of Computer Science and Engineering, The Chinese University of Hong Kong, Hong Kong

Available online 18 May 2004

## Abstract

Motivated by frequently repeated activities of negotiating similar sales contracts and inadequate studies of business-tobusiness (B2B) negotiation processes, we formulate a meta-model of e-Negotiation based on a practical meta-model for e-Contract template and template variables to allow flexible support for a variety of negotiation processes. Based on our metamodels, we develop an effective implementation framework with contemporary Web services technology. We illustrate our methodology with three typical kinds of sales e-Negotiation processes, namely, bargaining, auction, and request for proposals (RFPs). As a result, B2B, business-to-customer (B2C), or even customer-to-customer (C2C) negotiation can be systematically supported in a unified pragmatic framework for both human and programmatic access. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Cross-organizational workflow; e-Negotiation; e-Contract templates; Meta-modeling; Web services

## 1. Introduction

Negotiation is a decision process in which two or more parties make individual decisions and interact with each other for mutual gain [38]. Traditionally, negotiation is usually associated with contracts as an outcome [31]. A contract is a binding agreement between two or more parties, defining the set of obligations and rewards in a business process. This reduces uncertainty associated with the interactions between the parties. An e-Contract is a contract in electronic format, regulating cross-organizational business processes over the Internet. As such, contracts are important for attaining interoperability of business processes and enforcing their proper enactment. In the USA [32], the federal government spends about USD\$200 billion annually buying goods and services from over 300,000 vendors. A typical supermarket chain requires negotiating annually contracts of over 50,000 product items. In general, negotiation processes can be classified into bidding and bargaining. An extended form of bargaining is to have a prelude phase of requirement and candidate identification in processes of request for proposals (RFPs) [25].

Most studies on negotiation focus on interactive bargaining but not on business-to-business (B2B) negotiation processes. In order to address this problem, we have conducted a preliminary study on the different requirements for different modes of negotiation [8] and an implementation framework for bargaining based on Web services [9]. In this paper, we consolidate our experience, focusing on negotiation processes in ecommerce that are more structural (as opposed to political and governmental negotiations) but are often repeatable. We employ a meta-modeling approach for the development of negotiation support in a Web services environment. It provides a generic support of the negotiation processes as required in different scenarios, such as bargaining, auction, and RFP. In contrast to our previous paper on the development of negotiation protocols [6,7], this paper focuses on the development of a flexible platform for B2B negotiation support. The contributions of this paper are as follows: (i) We propose a meta-model of e-Negotiation (i.e., performing negotiation activities over the Internet) to allow for rapid development of a flexible negotiation support system (NSS) for a variety of negotiation processes [21]. (ii) In particular, we propose a practical meta-model for e-Contract template and template variables, based on which different e-Negotiation processes could be facilitated. (iii) We present an implementation platform based on contemporary Web services technology so that negotiation processes for both programmatic and human users. (iv) Our methodology is illustrated with three typical kinds of negotiation processes, namely, bargaining, auctions, and RFP, based on a running example of a sale contract in an e-commerce Web services environment.

The remainder of this paper is organized as follows: Section 2 discusses background and related work. Section 3 outlines our meta-modeling approach to e-Negotiation process support, including our metamodels for e-Contract templates, template variables, and e-Negotiation of contracts. Section 4 presents our implementation framework with contemporary Web services technology and discusses how to facilitate three typical negotiation scenarios (namely, bargaining, auctions, and RFP) based on our meta-model. Section 5 concludes the paper with prospective future work.

## 2. Background and related work

Traditionally, negotiation binds with contracts as an outcome [31]. Similarly, negotiation of contracts also involves two or more parties multilaterally bargaining for mutual gain in order to achieve a mutual beneficial agreement, but each of them may have conflicting interests [7]. In many cases, the parties are searching for an integrative agreement. In particular, integrative agreements are likely to contribute to business effectiveness [29]. During negotiation, proposals are sent to the other parties, and a new proposal may be generated after receiving a counter proposal. From another aspect, the order of a negotiation process should guide the actual business interactions. The process continues until an agreement or a deadlock is reached, or even one or more parties quit. During the process, each party needs to determine reactions of the other parties and obtain their responses, while estimating the outcomes that counter-parties would like to achieve. Whereas each party has its own utility function, they tend to be ignorant of the others’ values and strategies, especially in a non-cooperative environment. As a result, negotiations may involve high transaction costs and therefore has to be streamlined, especially in high volume e-commerce environments.

By performing negotiation activities over the Internet, which has recently become a global communication platform, both transaction costs and time can be greatly reduced. The Internet allows organizations and individuals to communicate among each other, to carry out various commercial activities, and to provide value-added services. Many business activities become automated as electronic transactions. However, negotiation of contracts is often still performed manually unsupported by computer systems or just by email. The main problem of this is its slowness, which is further complicated by issues of culture, ego, and pride [38]. In this paper, e-Negotiation of contracts is the computerized facilitation of contract negotiation over the Internet with the assistance of a set of NSSs and an e-Contract generator. A successful e-Negotiation leads to an e-Contract. An NSS within expanded functionality (such as matching) in an e-Marketplace is often referred to as an e-Negotiation portal [39].

In general, negotiation processes can be classified into bidding and bargaining [25]. Bidding is a multilateral distributive negotiation, and it is a formal, competitive procurement procedure. Bidding offers to supply goods, works, or services, which are solicited, received, and evaluated. Bidding ends with a contract awarded to the bidder whose offer is the best in terms of price and other factors that should be taken into account in the evaluation of bids. A bargaining process involves two parties. Each party has a single but opposing objective such as paying less or being paid more. This is called divergence of interest between two parties. It means that the parties have incompatible preferences among a set of available options. Both parties have opposing preferences and the parties differ in their utility ordering for at least some of the options under consideration [30]. The difficulty of the bargaining process lies in learning the best value, which the opponent still would accept, and in obtaining this value. In general, the degree of divergence of interest is a joint function of the parties’ needs and the alternatives under consideration. However, it is usual for the parties to discover new alternatives that reduce or even eliminate a prior divergence of interest [30]. Thus, a flexible NSS needs to support a variety of negotiation processes, and therefore we aim at developing such negotiation support with a meta-modeling approach in this paper.

Computer applications were first employed for negotiation support in the 1960s. In the 1980s, computer-based NSS emerged, and they were typically used for training and research in a laboratory environment but were rarely used in practice [11]. In general, NSSs have the following basic features [22]: (1) a formalism to describe the negotiation activity in terms of choices and outcomes, (2) a way to generally characterize the associated outcome probabilities, and (3) a methodology for processing the model to evaluate the expected values of choice alternatives. NSSs normally assist negotiators to assess situations, generate and evaluate options, and implement decisions. However, most NSSs do not consider the generation of contracts, which we consider to be the primary aim of negotiation in ecommerce, as an outcome of negotiation process. For example, NEGOTIATOR [5] seeks to guide negotiators to move their individual goals and judg ments to enhance the chance of achieving a common solution. It supports problem adaptation through information sharing, concession making, and problem restructuring. However, NEGOTIATOR only helps the negotiators make decisions without any support to other entities involved in negotiation, such as contracts. INSPIRE (InterNeg Support Program for Intercultural Research) [24] is a Web-based prototype for supporting inter-cultural as well as intra-cultural negotiations. It can conduct negotiation anonymously, evaluate the goodness of an offer, and review the history of a negotiation. INSPIRE supports the communication among negotiators by exchanging messages, but we propose direct interactions among different entities with Web services.

Recently, researchers are developing negotiation protocols for agent automation in e-commerce environments. Bartolini et al. [1] develop an agent-based software framework for automated negotiation, aiming for reuse. Tamma et al. [36] further propose negotiation protocols to be expressed in terms of shared ontology among agents. However, they only showed an example protocol for English auction in the paper with rule-based axioms and did not detail their negotiation process support and management environment. Neither did they present Web services implementation frameworks that support both human and programmatic users as in this paper. Griffel et al. [17] present an application of contract negotiation by mobile agents. A contract is represented as an object that can be accessed by the negotiation parties. Each party has the opportunity to change or insert clauses. They only provide a conceptual view of their approach, without any supporting formal model.

Modeling of e-Contracts can be dated back to the Contract Net Protocol [35] on low-level transaction aspects. In traditional Computer Science communities, the focus of e-Contract-based systems is on contract enactment and transactional support, but not on negotiation as proposed in this paper. Further examples include Karlapalem et al. [23], who propose a metamodel for e-Contracts with Entity-Relationship diagrams and generation of workflows to support e-Contracts, but do not consider the notion of commitments in e-Contracts. Crossflow [16] models virtual enterprises based on a service provider –consumer paradigm, in which organizations (service consumers) may delegate tasks in their workflows to other organizations (service providers). Virtual organizations are dynamically formed by contract-based matching between service providers and consumers. In addition, Yu and Mylopoulus [40] consider dependencies of business goals but have not been applied to practical details of variable dependencies of contract negotiation as proposed in this paper.

Contracts are also extensively modeled with logic for requirements engineering, but usually their links to contract enactment or negotiation process management have not been emphasized. Grosof et al. [18] introduces a declarative approach to business rules in ecommerce contracts by combining Courteous Logic Program and XML. Marjanovic and Milosevic [26] give a contract model based on deontic logic for contract clauses, including obligation, permission, and prohibition. Tan and Thoen [37] propose a logical formalism to represent the content of business contracts based on the Formal Language for Business Communication (FLBC) for negotiating and processing contracts based on the event semantics. Gisler et al. [15] present a framework for legal contracts, but not a mechanism for modeling e-Contracts as presented in the next section. These researches do not provide conceptual or logical model for flexible negotiation process management as presented in this paper.

In summary, although there have been a lot of studies on NSS and electronic contracting, respectively, research on development methodologies for negotiation support of e-Contracts has not been adequately addressed, especially in B2B e-commerce environments.

## 3. A meta-modeling approach to e-Negotiation process support

As current trends in e-commerce may accelerate the widespread use of e-Contracts in the business world [27], the ability of an e-commerce system to quickly create mutually beneficial e-Contracts will become a critical success factor for organizations. An automated e-Contract negotiation system should be able to create values, by interacting with different parties to reach mutually acceptable deals. This is particularly applicable to e-commerce processes, which usually have a certain business model, a certain scope, and a set of operation policies, but yet need to provide flexibilities in order to be competitive. New e-Contracts for these business interactions can be defined based on standard contract templates. Specific business interactions not covered by the clauses in standard contract templates can be provided as contract variations or contract escalations.

A contract template is a reference document, based on which new contracts can be negotiated. A contract template consists of a number of contract clauses, each addressing a specific concern during business interactions. Each contract clause contains a set of template variables whose values are to be negotiated. The following gives an example of a contract clause in a sales contract template, which is typically required in e-commerce processes. The brackets identify template variables in the clause. We propose e-Negotiation of contracts based on the negotiation of template variables. This can avoid uncontrolled openness of issues, and therefore improves effectiveness and efficiency of negotiation activities. An example contract template is as follows

‘‘The PURCHASER shall send a Letter of Credit for the GOODS to the SUPPLIER in the currency of [ ] within [ ] days of the invoice date. The SUPPLIER shall on receipt of the Letter of Credit ships the GOODS to the PURCHASER within [ ] days and provides the PURCHASER with shipment details’’.

Referring to Fig. 1, our overall methodology to e-Negotiation process management proposed in this paper can be summarized into the following four phases, with reference to an e-Negotiation portal implementation presented in the next section:

1. Planning Phase: Based on policies and requirements of users, administrators or analysts formulate and design contract templates (with variables), with reference to existing contracts used in the organization or similar ones in relevant industry domains.

2. Generating Phase: A contract template is then modeled as an e-Contract template according to our meta-model, as described in Sections 3.1, 3.2, and 3.3.

3. Matching Phase: Suitable e-Negotiation processes are designed based on our meta-model for e-Negotiation processes, as described in Section 3.3. Section 4 illustrates some sample e-Negotiation processes, such as bargaining, auctions, and RFP.

4. Executing Phase: Designed e-Negotiation processes are executed with the support of an e-Negotiation portal. Each successful e-Negotiation will lead to an e-Contract.

![](/api/attachments/GUKHJ4BC/fulltext/images/aaaff83424ec24992a6b7fe41fdcbfe8dc3d0b3766137664d819b7b3dee33e2b.jpg)  
Fig. 1. The proposed approach for e-Negotiation of contracts.

It should be noted that the work done in the prenegotiation phase (i.e., planning, generating, and matching phases) can be stored in a repository and is expected to be heavily reused. This is especially applicable to e-commerce processes, such as sales activities, in which negotiations are relatively structured with less open issues and are repeated very often. In addition, these designed processes are most probably repeatable and reusable for different e-commerce activities and for different organizations. Thus, a meta-modeling approach is required to cope with generality, flexibility, and reusability.

## 3.1. A meta-model for e-Contract templates

Fig. 2 presents a meta-model of an e-Contract template in Unified Modeling Language (UML) [28], which is a modeling language for visualizing, specifying, constructing, and documenting the artifacts of a software-intensive system. UML offers a standard way to write a system’s blueprints, including conceptual things such as business processes and system functions, as well as concrete things such as programming language statements, database schemas, and reusable software components. Note that UML standardizes only the notation, leaving software engineers the freedom to adopt their own software development process [13].

![](/api/attachments/GUKHJ4BC/fulltext/images/65098d3d6cd9537f78238b3ed99b78d53b8858334dac206bd4d147ae997d75ec.jpg)  
Fig. 2. Meta-model of an e-Contract template.

An e-Contract, which involves at least two parties, is a refinement of an e-Contract template. A template consists of a number of contract clauses, each of which concerns some parties to be bound by the e-Contract. Typical contract clauses include obligation, permission, and prohibition [19,26]. For example, a buyer is obliged to pay according to the payment terms and a supplier is not allowed to cancel the order once committed. A complex contract clause may consist of several simpler clauses. In an e-Contract template, a contract clause may contain a number of template variables as discussed before, such as the product, price, and quantity. These variables are to be refined in an e-Contract through negotiations.

Based on related contracts and requirements, an organization can abstract common clauses and differentiate the parameters to create contract templates, according to this meta-model. This template provides a basis on which negotiations may take place as described in the next section. A contract template can provide guidance in negotiation processes, thus improving the effectiveness of negotiation. The most common contract being used for e-commerce is probably a sales contract. A template variable may depend on another variable as shown in Fig. 2.

![](/api/attachments/GUKHJ4BC/fulltext/images/83646cfeccfa3ad0f5a6a49b9cd65cac1f1fc8f2a32b70c17002b88f0e49c2bf.jpg)  
Fig. 3. A sales e-Contract template as an instance of the meta-model.

Fig. 3 further gives an example sales e-Contract template instantiated from the meta-model in Fig. 2. The sales e-Contract consists of four contract clauses; each in turn contains one or two template variables. Directed lines represent ‘‘depend’’ relationships in the meta-model. For example, unit price, quantity, and delivery date are variables, which depend on each other and, thus, they will be discussed altogether during e-Negotiation. On the other hand, the insurance premium depends on the quantity of goods ordered and the unit price, while the unit price depends on the purchase volume. Therefore, the insurance premium issue should be discussed after the decision on the quantity and unit price. Thus, these dependencies are critical to the derivation of an e-Negotiation plan.

## 3.2. e-Negotiation conceptual model

Whereas much research has focused on supporting negotiation activities with various information technologies, our proposed approach concentrates on the e-Negotiation for a new e-Contract based on an e-Contract template. We proceed to present an e-Negotiation conceptual model and a process meta-model to support it.

Fig. 4 presents the e-Negotiation conceptual model and its relationships to the e-Contract conceptual model. The right-hand side is an extraction of the e-Contract conceptual model, while the left-hand side represents a conceptual model of an e-Negotiation. An e-Negotiation is made of up tasks, each of which aims at resolving an issue or a collection of co-related issues. For instance, issues in sales negotiation include delivery date, inclusion of freight, and the deposit to be paid by the buyer (if any). Each of these issues maps to a set of variables and their relationships. An e-Negotiation plan can be formulated based on the relationships across variables [6]. The plan presents a strategy to drive and organize various tasks in an e-Negotiation. Multiple offers and counter offers are made in a task, until a consensus has been reached.

![](/api/attachments/GUKHJ4BC/fulltext/images/96ef2c3f37d2b38701c44402d49fc2ec407b013f84250e348c666dc590295dcf.jpg)  
Fig. 4. Conceptual model of e-Negotiation and e-Contract.

A task in an e-Negotiation represents some work that needs to be executed by a set of parties that can be a negotiator, or even a NSS to resolve a specific issue. Further, there may be a set of criteria to be enforced in the set of tasks. These criteria [2] can be classified into three classes: static, dynamic, and hybrid. Static criteria can be verified at the e-Negotiation of contracts specification and used in the matching procedure. For example, the supplier can set criteria to seek potential buyers who do not have a bad credit. Dynamic criteria are those whose conformance cannot be checked without executing the e-Negotiation of contracts. For example, the supplier can set a time limit (e.g., a month) for seeking the potential buyers in some kinds of trading operation. Hybrid criteria can be checked during the specification or the e-Negotiation of the contracts. If they are found to be inconsistent during preliminary consistency verification, they will certainly not be satisfied in subsequent execution.

## 3.3. e-Negotiation process meta-model

Fig. 5 depicts our e-Negotiation process metamodel in UML activity diagram. This negotiation process is driven by our e-Contract templates metamodel, as described in the previous sections. When an e-Negotiation process is initiated for execution from the task ‘‘Start,’’ two parallel dependent tasks ‘‘Define issues and criteria’’ and ‘‘Select e-Contract template’’ follow. As there is a contract template for a particular type of negotiation, this set of issues corresponds to the variables in the contract template. Every issue has a set of alternatives (i.e., quantitative, qualitative or mixed), such as price, quantity, etc. After all the information is finalized, the task ‘‘Derive variable relations’’ is executed in order to generate the template variables and their relations for the contract. Then, two parallel dependent tasks ‘‘Formulate plan’’ and ‘‘Validate consistency’’ will interact with each other or even rollback to the previous task ‘‘Derive variable relations’’ for generating an e-Contract template. After the e-Contract template is created, the task ‘‘Organize tasks’’ can then generate a detailed negotiation process specification from the derived negotiation plan for execution. These negotiation process specifications can then be stored in a repository for reuse.

At this state, the activity ‘‘Make offer and counter offer’’ realizes this process for the actual negotiation.

![](/api/attachments/GUKHJ4BC/fulltext/images/834115747321218a08498132a71dbe62e177f417300a50afb860dc5b37e5512f.jpg)  
Fig. 5. A meta-model of e-Negotiation process in UML activity diagram.

If the negotiation is successful, then it leads to ‘‘Creation of an e-Contract,’’ otherwise, no contract can be arrived at. Finally, the e-Negotiation activity is completed at task ‘‘End.’’

## 4. Facilitating the e-Negotiation processes

In this section, we present our implementation framework for facilitating e-Negotiation process in a Web services environment based on our e-Negotiation meta-model. We then illustrate our development methodology for three common negotiation scenarios (namely, bargaining, auction, and RFP) that are common in e-commerce processes. As such, these three different types of e-Negotiation processes can easily be facilitated in a unified manner.

## 4.1. Implementation framework

Web services allow e-commerce activities to be carried out based on a set of XML standards such as Simple Object Access Protocol (SOAP), Universal Description, Discovery and Integration (UDDI) and Web services Description Language (WSDL). Traditional business-to-business applications connect trading partners through non-standardized architecture. A major drawback is the lack of interoperability where setting up connections with a new trading partner can be costly and time consuming. In contrast, the benefits of adopting Web services include faster time to production, convergence of disparate business functionalities, a significant reduction in total cost of development, and easy-todeploy business applications for trading partners. In addition, Web services provide a flexible, highly coherent, and loosely coupled interface, which supports both programmatic and human users, thereby further facilitating the realization of our meta-models.

Fig. 6 presents the implementation architecture designed to support e-Negotiation processes instantiated from the e-Negotiation conceptual model in Fig. 4 and the process meta-model in Fig. 5. The design aims to provide the flexibility and reusability of components as required a Web services infrastructure. The architecture consists of three subsystems. The e-Contract Template Generation Subsystem allows negotiation parties to specify and edit their negotiation criteria and issues. The search engine selects the most appropriate e-Contract template based on a given set of criteria and issues. The retrieved e-Contract template may be further revised using an e-Contract editor to address all major required criteria and issues. Revised e-Contract templates and the template variables thus derived may be stored at the archive for later

Negotiation Clients

![](/api/attachments/GUKHJ4BC/fulltext/images/b18425ffcfc55e96a050adda4cecd731e76c92446541138f3cc630284bb0fd6a.jpg)  
Fig. 6. Implementation architecture.

retrieval. These data will be used by the e-Negotiation Matching Subsystem to determine an e-Negotiation process based on the variable dependency supplied. The selected e-Negotiation process is then enacted through the e-Negotiation Executing Subsystem.

## 4.2. Example scenario 1—bargaining

Bargaining is the most interactive form of negotiation. This example refers to bargaining processes in e-commerce which more structural (as opposed to political and governmental negotiations). It is often required when negotiations involve high value or customized products/services. Either suppliers or buyers may initiate the process after they identify each other. Usually, a bargaining process can be thought of involving one supplier and one buyer at a time. Though the buyer may be bargaining with other suppliers at the same time (while the supplier may also be bargaining with other buyers, too), the details of each bargaining are usually not disclosed to the other parties. Participants may place offers into the NSS or search for offers to respond to. So, the following Web services are necessary.

Service Name: placeNewBargainOffer

 Input: Item Description, Contract Template ID, Proposed Template Variable Values, Additional Requirement List

 Response: Offer ID

Service Name: withdrawOffer

 Input: Offer ID

 Response: Confirmation

Service Name: searchOffer

 Input: Search Criteria

 Response: List of Offer ID and Descriptions

## 4.2.1. Select e-Contract template and define issues and criteria

The administrator or analyst may derive sales contract templates from its business experience, formally from its old sale contracts, or informally from quotations, purchase orders, invoices, or other correspondences with its buyers. These e-Contract templates are stored into a repository for reuse. Users may then search for relevant templates from the repository and adapt it if necessary. Typical contract template variables include product models, unit price, quantity, delivery date, freight, payment terms, deposit, etc. For some products (e.g., equipment), contract template variables may also include return policy, insurance premium, warranty, maintenance terms, and so on. These contract template variables are common issues in a sales negotiation. The following Web services are therefore required.

Service Name: searchContractTemplate

 Input: Search Criteria

 Response: XML Contract Template Summaries

Service Name: downloadContractTemplate

 Input: Contract Template ID

 Response: XML Contract Template

Service Name: uploadContractTemplate

 Input: XML Contract Template

 Response: Contract Template ID

## 4.2.2. Formulate plan

Referring to Fig. 7, typical sales contract negotiation involves the evaluation of several variables and of several values per variable. As a result, a large combination of values has to be evaluated by negotiators. The evaluation of a large combination of variables is time consuming and could be difficult for decision makers from a cognitive perspective. Most of the related work in contract negotiation takes the consideration of template variables in isolation. Decision makers are assumed to consider these variables one at a time, in a stepwise fashion, instead of integrating multiple template variables into a single package so that potential tradeoffs can be recognized [14]. We have shown that contracts with related attributes can be evaluated similarly [6]. Our approach is summarized by illustration with the sales contract example.

Some issues are mutually inter-related and therefore must be negotiated together, such as unit price, quantity, and delivery date. This cluster of issues is also the most important ones and therefore usually negotiated first. Similarly, payment terms and deposit are often inter-related issues, which are then to be negotiated as the second cluster. Return policy (and/or other technique issues) may be negotiated in parallel with the second cluster, because this is an independent issue and may be discussed by technical departments of the two companies. Because the amount of freight usually depends on the quantity of goods, it can only be determined after the quantity reaches agreement. Similarly, insurance premium depends on the nature of the product, its total amount, etc. As for who pay the insurance and freight, this issue is usually less important than unit price, quantity, and delivery date, and therefore can be discussed after consensus have been reached the more important issues.

In summary, when we formulate a negotiation plan, we need to take in account of the dependencies among the issues, their relative importance and whether we are able to carry them out in parallel. The formulated plan is then to be enacted in the process of ‘‘Make offer and counter offer.’’ The formulated negotiation plans can again be stored in the repository for reuse. The following Web services are therefore required.

Service Name: downloadNegotiationPlan

 Input: Contract Template ID

 Response: XML Negotiation Plans in the Repository for the specified contract template

![](/api/attachments/GUKHJ4BC/fulltext/images/ad431c54c660af5c32f6c4d86d071fba94186e69348b8b679d88990d37d6bff8.jpg)  
Fig. 7. Some typical details of the negotiation plan for bargaining.

Service Name: uploadNegotiationPlan

 Input: Contract Template ID, XML Negotiation Plan

 Response: Negotiation Plan ID

## 4.2.3. Make offer and counter offer

Fig. 8 describes an implementation of the ‘‘Make offer and counter offer’’ activity for bargaining that we have implemented. The implementation is designed to support negotiation plans formulated according to our contract template meta-model (such as the one discussed in the previous sub-section). Each party will set their own criteria before carrying out the negotiation. Each negotiation cycle starts with the identification of a set of interrelated issues to be next negotiated, according an agreed negotiation plan (as discussed in the previous sub-section). Each party will then prepare the reservation prices of these issues. After that, they may either make an offer to or wait for some offers from counterparties. If counterparty is not satisfied with the (counter-) offer, another counteroffer or a failure message will be received. A negotiation cycle finishes successfully if an acceptance notification of previous (counter-) offer is received. Finally, the negotiation is successful when all issues have been successfully negotiated. The following are the required Web services to support the ‘‘Make offer and counter offer’’ activity in a bargaining scenario.

Service Name: initNegotiationSession

 Input: Offer ID Responded to, Negotiation Plan ID, Counteroffer Template Variable Values, Comments

 Response: Session ID

Service Name: updateNegotiationSession

 Input: User ID, Session ID, Counteroffer Template Variable Values, Comments

 Response: Outstanding Variables Not Agreed or Successful Negotiation

Service Name: abortNegotiationSession

 Input: Session ID

 Response: Confirmation

![](/api/attachments/GUKHJ4BC/fulltext/images/338f2c0ffb2ee375895b6b497e4ac836f58fd9cc7fd3a2aabb486940248c0c90.jpg)  
Fig. 8. An implementation of activity ‘‘Make offer and counter offer’’ for bargaining.

## 4.3. Example scenario 2—auction

When the supplier has limited amount of goods, the supplier will sell to those to maximize the profit. Auction is an economic mechanism for determining the price of an item and hence the ownership of the item. Auction provides an effective, alternative means of price discovery, especially when sellers do not know the buyers’ valuations [3]. This process is usually initiated by supplier, and may be carried out through its own portal or an external e-Marketplace. Many (potential) buyers will bid at a time. Therefore, auction is a multilateral distributive negotiation process, and it is a formal, competitive procurement procedure. One of the most popular types of auction is English auction. In English auction, auctioneer solicits progressively higher bids from the bidders until only one bidder is left [33]. It is also known as an open outcry and ascending auction. Bidders have a dominant strategy of bidding up to their private valuation. Further, a bidder can update his or her reservation price (maximum acceptable price) during the auction. Usually, a bidder’s strategy is to bid a small amount more than the previous highest bid until the bidder reaches its reservation price. This is because the bidder always wants to pay the lowest possible price that is also less than his reservation price. In addition, a bidder can observe other players and the price at which the competition abandons the bidding. Rothkopf and Park [34] provided an excellent review of different types of auction (such as English and Dutch auctions) and related issues. On the other hand, tendering can be considered as a reversed situation, where the buyer wants to buy a limited number of items (or services) and the supplier with the lowest bid will win.

## 4.3.1. Select e-Contract template and define issues and criteria

Usually, a contract template for auction has much less parameters than those applicable to bargaining, because the supplier often fixes the product to be sold. Price is often the only negotiable issue. Sometimes, quantity can be an issue, when a lot of same items are sold to different buyers who bid price for the quantity that they are going to buy. Very occasionally, some auctions may involve multiple issues, using a scoring rule (formula) to specify the evaluation of the variables.

The supplier can usually define the contract (template) easily according to its own business experiences.

## 4.3.2. Formulate plan

In contrast to bargaining, plan formulation for an auction is mainly to specify the rules and parameters for the bidding process, instead of determining the dependencies and importance of the issues. Typical parameters for the bidding process include the following three categories:

(1) Format—This includes Dutch or English auction, maximum rounds of bidding (if any), deadline for last bid (if any), maximum time between each bid (if any), whether bids are sealed or open, etc.

(2) Rules of bidding—This includes starting price, (minimum) price increment for each bid (if any), reserve price (sealed or open), etc.

(3) Administration—This includes the start time and location (physical location, or URL in the case of electronic auction) of the bidding, entry fee (if any), deposit (if any), penalty for bidder default (if any), who may bid, etc.

The following additional Web service is necessary as auction parameters are different from those of bargaining (though the removeOffer Web service could be the same, taking an Offer ID as parameter).

Service Name: placeNewAuctionOffer

 Input: Item Description, Contract Template ID, Proposed Template Variable Values, Additional Requirement List, Auction Parameters

 Response: Offer ID

## 4.3.3. Organize tasks

Organizing tasks for an auction is an important factor for the success of an action. Before bidding, the supplier usually needs to do a lot of preparations. First, potential bidders have to be identified. Then, announcements and publicity of the auction are performed to attract these potential bidders, such as items for sale and their quantity, auction format, rule of bidding of price, and other administration procedures. Finally, the planned admission procedures, such as admitting and registering valid bidders, charging entry fee and deposit (if any), etc., needs to be enacted. Here, we omit the required Web services as this is more related to marketing activities than to negotiation processes.

## 4.3.4. Make offer and counter offer

Finally, when the start time for bidding comes, the activity ‘‘Make offer and counter offer’’ for auction is executed. Our implementation of this activity is depicted in Fig. 9. The NSS receives valid bids (as defined by rules of bidding when we formulate the bidding process) until nobody is bidding within a valid time, or bidding time or round limit is exceeded. If the final price exceeds the reservation price, the auction is successful. Otherwise, if the final price is lower than the reservation price or if there are no bidders at all, the auction fails. The corresponding Web service for bidding is as follows:

## Service Name: placeAuctionBid

 Input: User ID, Session ID, Counteroffer Template Variable Values, Comments

 Response: ValidAInvalid

## 4.4. Example scenario 3—request for proposal

When buyers want to buy an item, they have some requirements about the item in mind. Given that, many issues in the requirements could still be left open. In this case, the item cannot be concretely identified. The buyer (usually big companies or government) may then advertise an RFP, aiming to attract suppliers to reply with the details of their solutions, i.e., providing concrete information and properties of the requested item.

4.4.1. Select e-Contract template and define issues and criteria

As the buyer has some requirements, but with a lot of open issues, the buyer often has only a rough or partial E-contract template, formulated from other roughly related items that have been procured before. The buyer can only define some issues that they know for the potential contract, and some criteria of product/ service. The rest of the contract template is to be constructed based on the information from potential suppliers in their proposals.

## 4.4.2. Formulate plan

The buyer then identifies which issues and criteria to be disclosed to RFP candidates. The buyer may directly identify specific candidates from its own partner list, search with some criteria of valid candidate suppliers (such license holders for some engineering works) through external directories, or attract potential suppliers with the specified criteria through open advertisements. The buyer may also need to determine various administration procedures for the RFP, such as deadline, submission procedures, etc.

## 4.4.3. Organize tasks

Organizing tasks for RFP is quite similar to auction. Announcements (or invitations) are made to attract potential suppliers, and then admission procedures, such as admitting and registering valid candidates, are carried out. As RFP is usually much more complicated than auctions, there are usually more enquiries to be handled. Enquiries can be made with emails directly among the users. The following Web service illustrates the parameters required for placing a new RFP.

![](/api/attachments/GUKHJ4BC/fulltext/images/68ae52be695551de2cd0df42953f0d4eac03a77fb74990f887cc65c476a7672e.jpg)  
Fig. 9. An implementation of activity ‘‘Make offer and counter offer’’ for auction.

## Service Name: placeNewRFP

 Input: Item Description, Contract Template ID, Proposed Template Variable Values, Additional Requirement List

 Response: Offer ID

## 4.4.4. Make offer and counter offer

Candidate suppliers have to submit their proposals before the deadline. The following Web service is required for this activity.

## Service Name: replyRFP

 Input: OfferID, Contract Template ID, Proposed Template Variable Values, Additional Requirement List

 Response: AcceptARejectARevisedOfferID

Upon receiving the proposals, the buyer evaluates them according to the criteria previously defined. The buyer may need to further interact with the candidates for clarifications and extra supporting information. The buyer may shortlist or rank candidates, or the buyer may also directly select a successful candidate. By this time, the buyer will have much more understanding on the details of product/service requirements, their issues, and thus also in the potential contract. Then, the buyer can negotiate further issues and criteria with the candidate(s) by following the detailed procedures of scenario 1—bargaining, as discussed in the previous subsections.

## 4.5. Negotiation process monitoring and session management

Based on our negotiation meta-model and the process models for bargaining, auction, and RFP worked out in the previous sections, we have clearly elicited the requirements for a flexible NSS. As our system supports multiple concurrent negotiation sessions with a session manager, we provide monitoring summary information of negotiation progress for the administrators of the organization. The Web services for monitoring the sessions are as follows.

![](/api/attachments/GUKHJ4BC/fulltext/images/9741ae5d77896e6270f3f8fe6c9f2e7dbacb82f288c430bf94f8293cb3b31561.jpg)  
Fig. 10. Session manager summarizing multiple concurrent negotiation sessions.

Service Name: sessionListforOfferor

 Input: Offer ID

 Response: List of Sessions, Each with Agreed Template Variable Values and the Different Values of Other Variables from Both Parties.

Service Name: sessionLogList

 Input: Session ID

 Response: List of Counteroffers and Comments in Chronological Order

As shown in Fig. 10, we have also built a Web-based client upon the above Web services. The information will be updated automatically to provide timely and accurate information during the negotiation process.

In our prototyping project, we have chosen the Java Web Services Developer Pack (WSDP) package for deploying the Web services [12]. The Java WSDP package includes all Java APIs for XML in the Java XML Pack, the Apache Tomcat server and other components needed to provide an environment for developing and testing Web services. Figs. 11 and 12 depict the registration of our negotiation Web services in a UDDI registry.

## 5. Conclusions and future work

In this paper, we have presented a practical approach to e-Negotiation of contracts based on e-

![](/api/attachments/GUKHJ4BC/fulltext/images/8def0ba73f0b8da5e58d5b4e4bbb11e383e896fdf0abe04f02f77c4a2e8a2d32.jpg)  
Fig. 11. UDDI registry for our prototype.

D.K.W. Chiu et al. / Decision Support Systems 40 (2005) 51–69

<table><tr><td>Port Name</td><td>Status</td><td>Information</td></tr><tr><td>NegotiationTP</td><td>ACTIVE</td><td>Address: http://localhost:8080/negotiation/nsWSDL: http://localhost:8080/negotiation/ns?WSDLPort QName: {http://negotiation.org/wsdl}NegotiationIFPortRemote interface: ns.NegotiationIFImplementation class: ns.NegotiationImplModel: http://localhost:8080/negotiation/ns?model</td></tr></table>

Fig. 12. Sample Web service.

Contract templates. We have formulated two metamodels for this approach, a meta-model for e-Contract templates with the notion of template variables and their dependencies as well as a flexible meta-model for e-Negotiation processes. We have highlighted our implementation architecture with contemporary Web services technologies and illustrated our methodology with typical e-Negotiation processes (namely, bargaining, auctions, and request for proposals) for sales contracts in ecommerce environments. Our meta-models help elicit the requirements of a flexible and expandable NSS. As a result, we can build such a NSS rapidly with the contemporary Web services technologies, which provides a unified interface across organizations for both human and programmatic access. This NSS is applicable to enterprises and e-Marketplaces, supporting B2B, business-to-customer (B2C), and even customer-to-customer (C2C) negotiations, and is a significant improvement over traditional manual or email based negotiation processes. Once such a NSS is built, the components and subsystems can be customized or plugged into existing EISs or e-Marketplaces for reuse, thus reducing development costs and time. The application of flexible, loosely coupled, and highly coherent Web service technologies are in line with the flexibility, generality, and reusability objectives of our meta-model and vice versa.

In summary, our approach helps capture knowledge and experience from previous contracts and negotiations, in particular, with previous contract templates and negotiation logs. Contract templates and negotiation plans can be reused, further reducing administration as well as software development and maintenance costs. In particular, service negotiation is still an outstanding issue in Web services and is therefore a potential application of our negotiation model. There are increasing demands and discussions about negotiation technologies for different Web services applications.

This work can be expanded in several directions. We are looking into further details of contract template dependencies [6] and the application of our methodology to more complex negotiations. In this paper, we have only discussed the scenario of one-to-one (two parties) negotiation of contract (other than auctions). We are currently investigating the integration of negotiation support with EIS as well as the participation of different roles and individuals in an organization to negotiation processes. We are also looking into other scenarios of one-to-many (more than two parties at one time) negotiation of contract. In addition, we are investigating the ranking of different types of issues and criteria [4] for logrolling issues [7,20]. We are also investigating in mobile adaptation for service negotiation and multiple platform support [10]. Overall, this provides opportunities to gain insight into the relationships between e-Negotiation and e-Contracts for the real-life negotiation practice. On the other hand, we are looking into further issues of e-Marketplaces, especially those related to mobile clients.

## Acknowledgements

The work was supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China, Project No. HKUST6170/03E.

## References

[1] C. Bartolini, C. Preist, N.R. Jennings, Architecting for reuse: a software framework for automated negotiation, Proceedings of the 3rd International Workshop on Agent-Oriented Software Engineering (AOSE 2002). Springer LNCS 2585, 2002 July 15, pp. 88 – 100, Bologna, Italy.

[2] E. Bertino, E. Ferrari, V. Atluri, The specification and enforcement of authorization constraints in workflow management systems, ACM Transactions on Information and System Security 2 (1) (1999) 209– 240.

[3] M. Bichler, A roadmap to auction-based negotiation protocols for electronic commerce, Proceedings of the 33th Hawaii International Conference on System Sciences Big Island, Hawaii, IEEE Computer Society Press, Los Alamitos, California, 2000, CD-ROM.

[4] S.J. Brams, D.M. Kilgour, Fallback bargaining, Group Decision and Negotiation 10 (2001) 287 – 316.

[5] T.X. Bui, M.F. Shakun, Negotiation processes, evolutionary systems design, and negotiator, Group Decision and Negotiation 5 (1996) 339– 353.

[6] S.C. Cheung, P.C.K. Hung, D.K.W. Chiu, A meta-model for e-Contract template variable dependencies facilitating e-Negotiation, Proceedings of the 21st International Conference on Conceptual Modeling (ER2002), Springer LNCS 2503 Tampere, Finland, Springler-Berlin, Germany, 2002 Oct., pp. 55 – 64.

[7] S.C. Cheung, P.C.K. Hung, D.K.W. Chiu, On e-Negotiation of unmatched logrolling views, Proceedings of the 36th Hawaii International Conference on System Sciences Big Island, Hawaii, IEEE Computer Society Press, Los Alamitos, California, 2003 Jan., CD-ROM.

[8] D.K.W. Chiu, S.C. Cheung, P.C.K. Hung, A meta-model for contract template driven e-Negotiation processes, Proceedings of the 6th Pacific Asia Conference on Information Systems (PACIS ’02) 2002 Sept., CD-ROM.

[9] D.K.W. Chiu, S.C. Cheung, P.C.K. Hung, Developing e-Negotiation process support with web services, Proceedings of the First International Conference on Web services (ICWS’03), CSREA Press, Las Vegas, USA, 2003 June, pp. 97– 103.

[10] D.K.W. Chiu, S.C. Cheung, E. Kafeza, H.F. Leung, A threetier view methodology for adapting m-services, IEEE Transactions on Systems, Man and Cybernetics: Part A. Systems and Humans 36 (6) (2003) 725–741.

[11] M.M. Delaney, A. Foroughi, W.C. Perkins, An empirical study of the efficacy of a computerized negotiation support system (NSS), Decision Support Systems 20 (3) (1977) 185 – 197.

[12] H.M. Dietel, P.J. Dietel, J.P. Gadzik, K. Lomeli, S.E. Santry, S. Zhang, Java Web Services for Experienced Programmers, Prentice-Hall, Upper Saddle Valley, NJ, USA, 2003.

[13] H.-E. Erikson, M. Penker, Business Modeling with UML: Business Patterns at Work, Wiley, New York, 2000.

[14] A. Foroughi, M.T. Jelassi, NSS solutions to major negotiation stumbling blocks, Proceedings of the 23rd Hawaii International Conference on System Sciences 4 (1990) 2 – 11.

[15] M. Gisler, K. Stanoevska-Slabeva, M. Greunz, Legal aspects of electronic contracts, Proceedings of the CAiSE\*00 Workshop of Infrastructures for Dynamic Business-to-Business Service Outsourcing (IDSO’00), 2000.

[16] P. Grefen, K. Aberer, Y. Hoffner, H. Ludwig, Crossflow: cross-organizational workflow management in dynamic virtual enterprises, International Journal of Computer Systems Science and Engineering 15 (5) (2000) 277 – 290.

[17] F. Griffel, M.T. Tu, M. Munke, M. Merz, W. Lamersdorf, M.M. da Silva, Electronic contract negotiation as an application niche for mobile agents, Proceedings of the First International Enterprise Distributed Object Computing Workshop Gold Coast, Australia, IEEE Computer Society Press, Los Alamitos, California, 1997, pp. 354 – 365.

[18] B.N. Grosof, Y. Labrou, H.Y. Chan, A declarative approach to business rules in contracts: courteous logic programs in XML, Proceedings of the First ACM Conference on Electronic Commerce (EC99) Denver, CO, USA, ACM Press, New York, USA, 1999 Nov., pp. 68– 77.

[19] C. Herring, Z. Milosevic, Implementing B2B contracts using biztalk, Proceedings of the 34th Hawaii International Conference on System Sciences Big Island, Hawaii, IEEE Computer Society Press, Los Alamitos, California, 2001, pp. 4078 – 4087.

[20] P.C.K. Hung, A primitive study of logrolling in e-Negotiation, Proceedings of the Thirty-Sixth Hawaii International Conference on System Sciences Big Island, Hawaii, IEEE Computer Society Press, Los Alamitos, California, 2003, CD-ROM.

[21] P.C.K. Hung, J.Y. Mao, Modeling e-Negotiation activities with petri nets, Proceedings of the 35th Hawaii International Conference on System Sciences Big Island, Hawaii, IEEE Computer Society Press, Los Alamitos, California, 2002, CD-ROM.

[22] InterNeg, For and about Negotiations, http://interneg.carleton. ca, 2000.

[23] K. Karlapalem, A.R. Dani, P.R. Krishna, A frame work for modeling electronic contracts, Proceedings of the International Conference on Conceptual Modeling (ER2001) Yokohama, Japan, LNCS 2224, Springler-Berlin, Germany, 2001, pp. 193– 207.

[24] G.E. Kersten, S.J. Noronha, WWW-based negotiation support: design, implementation, and use, Decision Support Systems 25 (2) (1999) 135 – 154.

[25] A.R. Lomuscio, M. Wooldridge, N.R. Jennings, A classification scheme for negotiation in electronic commerce, Agent-Mediated Electronic Commerce: A European Perspective, Springer Verlag, Berlin, Germany, 2000, pp. 19 – 33.

[26] O. Marjanovic, Z. Milosevic, Towards formal modeling of e-Contracts, Proceedings of 5th IEEE International Enterprise Distributed Object Computing Conference, IEEE Computer Society Press, Los Alamitos, California, 2001, pp. 59 – 68.

[27] R.A. Nabil, Y. Yesha, Electronic Commerce: Current Research Issues and Applications, Springer Verlag, Berlin, Germany, 1996.

[28] Object Management Group (OMG), Foreword UML Specifi cation 1.4, http://www.omg.org (2001).

[29] D.G. Pruitt, Negotiation Behavior, Academic Press, New York, USA, 1981.

[30] D.G. Pruitt, P.J. Carnevale, A.S. Manstead (eds.), Negotiation in Social Conflict, Taylor & Francis Group, London, UK, 1993.

[31] H. Raiffa, The Art and Science of Negotiation, Harvard Univ. Press, Cambridge, UK, 1982.

[32] W.N. Robinson, Electronic brokering for assisted contracting of software applets, Proceedings of the 30th Hawaii International Conference on System Sciences 4 (1997) 449– 458.

[33] D. Ross, Stanford Encyclopedia of Philosophy: Game Theory, http://www.plato.stanford.edu/entries/game-theory/#Mot (2001).

[34] M.H. Rothkopf, S. Park, An elementary introduction to auctions, Interface 31 (6) (2001) 83 – 97.

[35] R.G. Smith, The contract net protocol: high level communi cation and control in a distributed problem solver, IEEE Transactions on Computers 29 (12) (1980) 1104– 1113.

[36] V. Tamma, M. Wooldridge, I. Dickinson, An ontology based approach to automated negotiation, Proceedings of the 4th workshop on Agent Mediated Electronic Commerce (AMEC IV), Bologna, Italy, 2002.

[37] Y.H. Tan, W. Thoen, Using event semantics for modeling

contracts, Proceedings of the 35th Hawaii International Conference on System Sciences Big Island, Hawaii, IEEE Computer Society Press, Los Alamitos, California, 2002, CD-ROM.

[38] L. Thompson, The Mind and Heart of the Negotiator, Prentice-Hall, Upper Saddle Valley, NJ, USA, 1998.

[39] E. Turban, Electronic Commerce: A Managerial Perspective, 2nd ed., Prentice Hall, Upper Saddle Valley, NJ, USA, 2002.

[40] E. Yu, J. Mylopoulous, Using goals, rules, and methods to support reasoning in business process reengineering, International Journal of Intelligent Systems in Accounting Finance and Management 5 (1) (1996) 1 –13.

![](/api/attachments/GUKHJ4BC/fulltext/images/ec199a22f2d90e01597e6e491a373777aee0861424e512abe8b361faf4584798.jpg)

Dickson K.W. Chiu was born in Hong Kong in 1966. He received his BS (Comp. St.) degree from the University of Hong Kong in 1987. He received his MSc (1994) and PhD (2000) degrees in Computer Science from the Hong Kong University of Science and Technology, where he worked as a Visiting Assistant Lecturer after graduation. He also started his own computer company while studying part-time. From 2001 to 2003, he visited the Department of

Computer Science at the Chinese University of Hong Kong as Assistant Professor. His research interest is in Information Systems Engineering for e-/m-commerce with a cross-disciplinary approach, involving Internet technologies, software engineering, agents, workflows, information system management, security, and databases. His research results have been published in more than 40 technical papers in international journals and conference proceedings. He received a best paper award in the 37th Hawaii International Conference on System Sciences in 2004. Dr. Chiu is a Senior member of IEEE as well as a member of the ACM and Hong Kong Computer Society.

![](/api/attachments/GUKHJ4BC/fulltext/images/0acb0903f2186712a507b6e04a1812b014a244d407749e00a52ad66fb6196b5d.jpg)

S.C. Cheung received his BS degree in engineering from the University of Hong Kong in 1984. He received his MSc and PhD degrees in computing from the Imperial College of Science, Technology and Medicine, University of London, London, UK, in 1988 and 1994, respectively. He is an Associate Professor of Computer Science and Associate Director of Cyber-Space Center at the Hong Kong University of Science and Technology. He has served

actively on the program committees of international conferences on software engineering, distributed systems and Web technologies. His research interests include software engineering, workflows, service-oriented computing, negotiation, information systems, and security.

![](/api/attachments/GUKHJ4BC/fulltext/images/a61e6b92bdd3587e8bb8a06b528cd5daf51cd61a780ed7f148d98baf9104443d.jpg)  
Patrick C.K. Hung is currently a Visiting Assistant Professor at the Department of Computer Science in the Hong Kong University of Science and Technology (HKUST). Patrick will join the Business School as an Assistant Professor at a newly formed university in Canada called the University of Ontario Institute of Technology in July 2004. Before that, he was a Research Scientist in the Commonwealth Scientific and Industrial Research Organization

(CSIRO), Australia. He has prior industrial experience in e-business projects in North America and Hong Kong. Since 2000, Patrick has been serving as a panelist of the Small Business Innovation Research (SBIR) and Small Business Technology Transfer (STTR) programs of the National Science Foundation (NSF) in the USA. He is an executive committee member of the newly formed IEEE Technical Community of Services Computing (TCSC) and the Publicity Cochair of the IEEE International Conference on Web Services (ICWS), a W3C member at the P3P Working Group. He also serves as Associate Editor and editorial board member in several international journals. Patrick received his PhD and Master of Philosophy Science degrees, both in Computer Science, from the Hong Kong University of Science and Technology, Hong Kong. Further, he received a Master of Applied Science degree in Management Sciences from the University of Waterloo, Ontario, Canada. He received his Bachelor of Science degree in Computer Science from the University of New South Wales, Sydney, Australia.

![](/api/attachments/GUKHJ4BC/fulltext/images/f414680c573b70a2c112f0fa88d44aefc44871e18979eb43bc2571a54313dccf.jpg)

Sherina Y.Y. Chiu was born in Hong Kong in 1981. She received her BEng (Computer Engineering) degree from the Chinese University of Hong Kong in 2003. She got distinction in her final year project for implementing the prototype in this paper. She is currently working as a programmer in a logistics company. Her research interests include Artificial Intelligence, Network Security, Database, Software Engineering, and Col-

laboration Support Systems.  
![](/api/attachments/GUKHJ4BC/fulltext/images/1baf1ebc57b75df09af67368ecc1a2fdc8208e75e364b3a29a518837b147c4ea.jpg)

Andriy K.K. Chung received his BEng (Computer Engineering) degree from the Chinese University of Hong Kong in 2003. He got distinction in his final year project for implementing the prototype in this paper. He is currently working as a programmer in an international bank. His research interests include Collaboration Support Systems, Artificial Intelligence, Network Security, Database, and Software Engineering.
