---
otero_id: 23032
otero_key: "X2YE6THT"
title: "Communicative action‐based business process and information systems modelling with DEMO"
authors: "Victor E. Van Reijswoud; Hans B. F. Mulder; Jan L. G. Dietz"
year: "1999"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.1999.00055.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Communicative action-based business process and information systems modelling with DEMO

Victor E. van Reijswoud, Hans B. F. Mulder\* and Jan L. G. Dietz

Delft University of Technology, Department of Information Systems, PO Box 356, 2600 AJ
Delft, The Netherlands, email: vreijsw@is.twi.tudelft.nl, or dietz@is.twi.tudelft.nl, and
\*Essential Action Engineers b.v., VIAgroep n.v., PO Box 58, 2280 AB Rijswijk, The Netherlands, email: hans.mulder@eae.nl

Abstract. The field of communicative action-based modelling of business processes and information systems has attracted more and more attention in recent years. Inspired by the seminal work of Winograd and Flores, researchers have proposed several modelling approaches. In this article we discuss communicative action-based modelling approaches in general and the DEMO (dynamic essential modelling of organizations) approach in particular. Besides establishing the theoretical foundations of this modelling approach, we also apply DEMO to a case study, and we discuss how the resulting models can be used for information systems design and business process optimization.

Keywords: Business analysis, business process redesign/re-engineering, communicative action-based modelling, information systems design, speech acts

## INTRODUCTION

Approaches for information systems development (ISD) have evolved through different stages and on different foundations. Hirschheim et al. (1995) describe seven generations that have evolved: from the developer's private methodological approach in the mid-1950s, through life cycle, structured, evolutionary, participative and emancipatory approaches to the currently emerging approaches that are based on communicative actions. The way of thinking dominant in the second and third generation of ISD (the life cycle and structured philosophy) has become a leading methodological paradigm in information modelling. Paradoxically, this way of thinking is also a source of many problems when applied to designing information systems in dynamic and emergent organizations because the systems built within this paradigm are too rigid (Hirschheim et al., 1995).

The increasing turbulence of a globalizing business market and the rapid succession of technological developments in the 1990s have forced organizations to constantly change the way in which business is conducted (Scott Morton, 1991). In this dynamic environment the information systems built on the structured paradigm prove to be inflexible, their development is too time-consuming. In response to these problems the fourth generation of ISD approaches was developed, the so-called evolutionary approaches, such as prototyping and rapid application development (Martin, 1987). Although these approaches dramatically increased the speed of ISD, the increase in flexibility was not sufficient (Beek et al., 1997). Also, a sound understanding of business processes and organizational change was lacking. This organizational change perspective was highlighted in the fifth and sixth generations of ISD, such as Soft Systems Methodology (Checkland, 1981; Checkland & Scholes, 1990) and ETHICS (Effective Technical and Human Implementation of Computer Systems; Mumford, 1983, 1985).

From the business perspective, the increasing turbulence in the business market and the rapid changes in information technology (IT) led to the development of business process approaches such as the value chain (Porter, 1985; Porter & Millar, 1985). These approaches have received a lot of attention and have been developed further by, for example, Hammer (1990), Scott Morton (1991), Davenport (1993) and Donovan (1994). However, these approaches are not suitable for ISD (Dietz & Mulder, 1998). At present, there is a gap between approaches for modelling business processes and those for modelling information systems. Owing to this gap, the translation of the business processes into an information system (and vice versa) and consequently the alignment of business and IT has become difficult.

Hirschheim et al. (1995) identify a seventh generation of ISD approaches, which promotes a more situational understanding of communication and organizational change. The approaches address the organizational issues that are related to using IS; they do not emphasize technology anymore. This currently emerging generation gets considerable attention in both the professional and academic literature. Although these approaches are a controversial topic in the field, they also offer new perspectives on ISD (livari et al., 1997). Methodologies for information systems analysis and design within the seventh generation that have received increasing attention in the past years are methodologies that are founded on the language/action perspective (see Dignum et al., 1996; Dignum & Dietz, 1997). The language/action perspective, which was introduced in the field of information systems by Flores and Ludlow in the early 1980s, constitutes a new basic paradigm in the information systems arena (livari et al., 1996). In contrast to traditional views of ‘data flow’, the language/action perspective emphasizes what people DO while communicating, how they create a common reality by means of language and how communication brings about the co-ordination of their activities. Recently, the term ‘communicative action paradigm’ has been coined as a more accurate characterization (Dietz et al., 1998).

In this article, we will discuss a modelling methodology, based on the communicative action paradigm, called DEMO (dynamic essential modelling of organizations). DEMO provides a theory for understanding the working of an organization and an explanation of its business activities. The DEMO theory is extended with an integrated facility for modelling communication, information and action that provides the basis for both ISD and business process optimization. This simultaneous approach to business processes and information processes is a necessary precondition for business–IT alignment in dynamic organizations'. In 'Communicative action-based modelling approaches, we briefly introduce the speech act theory from which the basic principles of the communicative action paradigm are derived, then we discuss some approaches that have been founded on this paradigm. In 'Modelling with the DEMO methodology', we discuss the fundamentals of DEMO methodology. In this section we also elaborate on the areas where DEMO can be applied. The fourth section illustrates by means of a case study how the modelling facility of DEMO is to be applied and what conclusions can be drawn for ISD and business process optimization. Finally, some general conclusions are discussed.

## COMMUNICATIVE ACTION-BASED MODELLING APPROACHES

The focus on communication as the key concept for understanding and modelling organizations requires a theory that explains communication and language as its means. The speech act theory (Austin, 1962; Searle, 1969; Searle, 1979; Searle & Vanderveken, 1985) has proven to be a strong frame of reference for this purpose (e.g. Flores & Ludlow, 1981; Winograd & Flores, 1986; Taylor & Cameron, 1987; Winograd, 1988; Taylor, 1993). The main characteristic of the speech act theory is that it considers the use of language as a form of rule-governed behaviour. Uttering a sentence is the performance of an act, a so-called speech act.

The most important type of speech act in an organizational context is the illocutionary act. Falling through the prism of the speech act theory, instances of saying something spread out a spectrum of illocutionary acts, which are classified into illocutionary kinds. These kinds specify how the utterance in question is intended to be taken, i.e. what natural effect (cognitive, motive, social or legal) it is intended to have, and, accordingly, in what dimensions (truth, feasibility, propriety and so on) it is supposed to be assessed. For instance, an utterance can convey a statement, a warning, a promise, an order, and so forth (Vendler, 1967).

Following the example of Searle, several researchers classified speech acts. Among them are Ballmer & Brennenstuhl (1981) and Janson & Woo (1992). Important criticism of Searle's speech act theory was provided by Habermas through his theory of communicative action. He argued that Searle's taxonomy failed to explain co-ordination of action and proposed a taxonomy based on validity claims (Habermas, 1984, 1988). It is not our purpose to provide another classification, but to clarify which illocutionary kinds are relevant to DEMO. Therefore in Figure 1 we present a matrix in which the taxonomy of Searle and the taxonomy of Habermas are compared. This matrix is a slight adaptation of the one presented in (Dietz & Widdershoven, 1991). The categories of Searle are placed on the horizontal axis, those of Habermas on the vertical axis. Figure 1 also shows how the illocutionary categories of DEMO correspond with those of Searle and Habermas. All performative actions (request, promise, state and accept) fall into Habermas' category of regulativa, the kind of acts by which social relationships are initiated and maintained. All informative acts (question and answer) in the category of constativa, the kind of acts that are used to state information about the reality we live in.

The speech act theory has been the foundation of a number of theories and modelling approaches in the area of information systems. These approaches consider the utterance of speech acts to be the backbone of business processes, and consequently their modelling effort focuses on speech acts. The initial impetus to a speech-based conceptualization of organizations has been the work of Flores & Ludlow (1981). They proposed perceiving organizations as networks of interrelated commitments created by pairs of directives and commissives, and assertives and declaratives, as shown on the horizontal axis of Figure 1.

![](/api/attachments/X2YE6THT/fulltext/images/e282560aec497ecb421f308fce964b4b5fcedc102561716db14af51e87c7b287.jpg)  
Figure 1. Comparison of Searle's Speech Act Theory and Habermas' Theory of Communicative Action.

The ‘commitment analysis’ of Flores & Ludlow (1981) was extended in great detail by Winograd & Flores (1986). According to this approach, conversation for action (CfA) is the central co-ordinating structure for human organization. CfA is conceptualized as an interplay of requests and commissives directed to explicit co-operative action. Next to the conversation for action, conversations for clarification, possibility and orientation are identified. For more details on the different types of conversations the reader is referred to Winograd (1988).

The conversation for action theory has been developed into a fully grown speech act-based modelling approach within the business design language by action technologies (Medina-Mora et al., 1992; Schäl & Zeller, 1993; Schäl, 1996). The basic modelling unit is the four-step action workflow protocol. A comparison between DEMO and action workflow is presented in (Reijswoud, 1996).

Another early speech act-based modelling approach is SAMPO (Speech Act-based Modelling aPprOach; Lehtinen & Lyytinen, 1986; Auramäki et al., 1988, 1991; Auramäki & Lyytinen, 1996). SAMPO studies organizational activities as a series of speech acts that create, maintain, modify, report and terminate commitments. By means of two graphical representations, the discourse graph and the conversation graph, SAMPO describes institutionalized networks of acts and help to detect:

1 principles needed in the set-up and control of commitments;

2 inconsistencies in the co-ordination of commitments;

3 possibilities for organizational development that simplify communication and control mechanisms.

The optimized communication networks form the starting point for the information analysis of organizations. A comparison between DEMO and SAMPO for the purpose of ISD and business process optimization is presented in Reijswoud & Rijst (1995b) and Rijst & Reijswoud (1995)

A third approach towards modelling business activities based on the analysis of communicative actions, is BAT (business action theory) (Goldkuhl, 1996). BAT proposes a generic model of business communication that explains business processes as action and interaction. The model components used to apply BAT are derived from the SIMM (Situation adaptable work and Information systems Modelling Method) methodology (see, for example, Goldkuhl, 1992, 1996; Goldkuhl & Röstlinger, 1993). Although the main purpose of BAT is to describe and explain business interaction, it can also be used as a theoretical lens for developing business processes for organizational change. Thus, the theory can be used as an interpretative framework when reconstructing, evaluating and redesigning different business processes. In such situations of change it should be supplemented by congruent change methods (e.g. Goldkuhl & Röstlinger 1993). A comparison between DEMO and BAT is presented in (Reijswoud & Lind, 1998)

In the next section we introduce the DEMO methodology. Contrary to CfA/business design language, SAMPO and BAT, the theoretical basis of DEMO is primarily founded in Habermas' theory of communicative action. This theoretical basis is extended for the purpose of ISD and business process optimization.

## MODELLING WITH THE DEMO METHODOLOGY

DEMO constitutes a cross-disciplinary theory describing and explaining the communicational dynamics of organizations, and a modelling facility based on this theory. Descriptions of DEMO can be found in Dietz, (1994a,b, 1996a,b), Dietz & Mulder (1996, 1998) Reijswoud (1996) and Reijswoud & Rijst (1995a).

In DEMO, the functioning of organizations is viewed from three levels: the documental, the informational and the essential level. At the documental level, an organization is regarded as a system of operators that produce, store, transport and destroy documents. In other words, at the documental level the substance and form through which co-ordination becomes visible is considered. At the informational level this substance and form is abstracted from, and the focus is put on the contents of the documents. At this level an organization is considered as a system of processors that send and receive information, and perform calculations on this information in order to create derived information. At the essential level an organization is conceptualized as a system of (social) actors that are engaged in the execution of business transactions. Here organizations are considered to be networks of interrelated business transactions, which in turn are composed of interrelated communicative acts.

The business transaction is the core concept in DEMO (Steuten, 1998; Reijswoud, 1996). A transaction is a pattern of activity that is performed by two actors: the initiator and the executor. It is important to note that actors are roles performed by social individuals. A transaction is composed of three phases: (1) the order phase, in which two actors come to an agreement about the future execution of some action; (2) the execution phase, in which the negotiated action is executed; and (3) the result phase, in which the actors negotiate the agreement about the result brought about in the execution phase. The successful execution of a transaction in the social world (the world of communication) results in a change in the object world (the world of facts) in which the actors exist. The basic pattern of a transaction is displayed in Figure 2 [for a more extensive description of the possible communication patterns in a business transaction, the reader is referred to van Reijswoud (1996) and Steuten & van Reijswoud (1996)].

The execution of a transaction can be described and modelled at all three levels of abstraction. At the essential level the transaction is described as a pattern of performative communication (the ‘regulativa’ as depicted in Figure 1). At the informational level the execution of a transaction is described as the exchange of information (the ‘constativa’ as depicted in Figure 1), and at the documental level the materialization of the transaction in tangible objects (documents, files, etc.) is described. In the DEMO approach it is assumed that the transaction at the essential level allows multiple realizations at the informational level and at the documental level. It is important to realize that these realizations are ideally deliberate organizational choices. The main idea is displayed in Figure 3.

The modelling facility of DEMO provides a graphical representation of the transactional structure of organizations. This transactional structure is represented in five partial models: the action model, the interaction model, the process model, the fact model and the interstriction model. The models are developed incrementally. The interaction model displays the transaction types and the initiating and executing actors in an organization. The business process model displays the causal and conditional relationships between the transaction types and its constituting phases. The fact model provides a complete and precise specification of the state space of the object world. The interstriction model displays the actors and the information banks they need access to in order to execute a transaction. Finally, DEMO includes an action model of an organization. The action model is called the 'mother of the models' because it provides the most detailed specification of the transaction structure of an organization. It also allows specification of transactions at the essential, the informational and the documental level. A diagram type with the same name graphically represents every model type.

![](/api/attachments/X2YE6THT/fulltext/images/7da3fe9633cbdd6655bb2a6c1e19122f3d699fd5b97a65da935880a9a2294efd.jpg)  
Figure 2. The basic pattern of the DEMO transaction.

![](/api/attachments/X2YE6THT/fulltext/images/e18ea38e9c7a4a824f2c5c69d2043efa0ec76bbf0b2bb444c30928a7db479abf.jpg)  
Figure 3. Transaction design and the levels of abstraction.

To illustrate the modelling facility of the DEMO methodology, we will consider the purchasing department of the Ford case as presented in Hammer (1990). The essence of the way in which the purchasing department of Ford works is formulated as follows by Hammer:

'When Ford's purchasing department wrote a purchase order, it sent a copy to accounts payable. Later, when material control received the goods, it sent a copy of the receiving document to accounts payable. It was up to accounts payable, then, to match the purchase order against the receiving document and the invoice. If they matched, the department issued payment.'

If the DEMO methodology is used, the first step is to consider the organization at the essential level. This means that the supporting tools and the supporting documents are deleted from the analysis. At the essential level we identify the business transactions as the means by which the actors co-ordinate their actions. In the case of Ford we have identified two business transaction types. Table 1 displays the transaction types, the initiating and the executing actors, and the transaction result.

On the basis of the transaction table, the interaction diagram is drawn. The interaction diagram is the graphical representation of the interaction model. The actors are represented by squares, and the transaction types by the combined diamond-and-disk symbol. The relationships between the phases of the transaction types are represented in the process diagram. The process diagram is the graphical representation of the business process model. The transaction phases are represented by (stretched) disks and the relationships by arrows. The interstriction is represented in the interstriction diagram. In this diagram the conversations by which actors retrieve information transaction banks are displayed by dotted links. The interaction diagram and the interstriction diagram may be combined in the communication diagram. In the fact diagram, which is the graphical representation of the fact model, the resulting transaction facts are represented by means of objects and fact types. Finally, we have the action diagram, which represents the action model in a procedural graphical language per transaction phase. The models and diagrams for the purchasing department of Ford are displayed below.

Table 1. The transaction table of Ford's purchasing department

<table><tr><td>Transaction type</td><td>Result fact type</td><td>Initiator</td></tr><tr><td>T1 Delivering_order</td><td>F1 Orderis delivered</td><td>A2 Purchase</td></tr><tr><td>T2 Paying_order</td><td>F2 Orderis paid</td><td>A1 Supplier</td></tr></table>

A more detailed explanation of the diagrams and symbols is provided in the SGC case study presented in the next section.

The DEMO models serve as a basis for two main application areas: business process optimization and information systems design (Figure 4).

## Business process optimization

The introduction of the term business processes redesign (BPR) has led to several approaches for business process optimization under different names (Keen, 1991; Scott Morton, 1991; Davenport, 1993; Hammer & Champy, 1993). BPR lacks a commonly accepted definition, but its underlying claim is clear: organizational change is necessary to keep a business flexible and competitive (Davenport, 1995; Teng et al., 1992). By introducing the three levels of abstraction, the DEMO approach provides a differentiated and well-founded definition of BPR, and its models provide a structured working approach for BPR. For example, organizational change can focus on the documental level, i.e. the production, storage, transportation and destruction of documents performed by the organizational system of operators (the D-system). In DEMO this is called automation. Change can also focus on the informational level: information systems redesign. This means that the system of processors (the I-system) that send, receive, calculate and derive information in an organization is changed. It is, however, important to realize that changes at the informational level necessarily involve changes at the documental level. In line with this reasoning, organizational changes can also focus on the essential level. DEMO locates BPR at this level. The changes at the essential level focus on the system of actors (the B-system) that are engaged in the execution of the business transactions. These changes are the most drastic ones because they also effect the informational and documental structure of the organization. Figure 5 shows the characterization of the change activities. A dotted arrow between two boxes means that the box to which it points is a ‘realization’ of the box from which the arrow departs.

Business process optimization with DEMO primarily focuses on changing the (essential) transaction design of the organization. On the basis of the interaction model, decisions can be made about adding or deleting transaction types. These changes have a major impact on the organization. The business process model can be used to reduce the cycle time of the entire business processes. Cycle times can, for example, be reduced by parallelization of transaction types or by changes to the conditional and optional relationships between the transaction types or the constituting transaction phases. For a more in-depth discussion of the these redesign principles the reader is referred to van Reijswoud (1999).

![](/api/attachments/X2YE6THT/fulltext/images/99ba3845f78f3289b30ceec4998e8147c83b97930afee8540b534a7b98b2c84a.jpg)  
Figure 4. DEMO models and diagrams for the purchasing department of Ford.

![](/api/attachments/X2YE6THT/fulltext/images/2c3aa9a43bf5eff73efc7d911972e6c5338dff01646cda9c8b017e0217721bcc.jpg)  
Figure 5. Characterization of organizational transformation activities in DEMO.

## Information system design

Modelling for the purpose of designing information systems is a well-developed area (e.g. Lundeberg et al., 1981; Yourdon, 1989, 1993; Checkland & Scholes, 1990). However, modelling on the basis of speech act models is hardly explored (Hirschheim et al., 1995). Most endeavours in this area have been aimed at understanding and optimizing business processes (e.g. Dietz, 1994a,b; Denning & Medina-Mora, 1995). Because the DEMO approach integrates models of both the social world and the object world, it is well suited for the design of information systems.

When the DEMO approach is used for designing information systems, the aim is to develop a blueprint for an information system. This blueprint contains a description of the essential (core) information for conducting the business, as well as the 'location', i.e. the transaction type, where this information is created. The blueprint also specifies the external information, that is the information created outside the system under consideration. The fact model describes the core information of the business; it provides a complete and precise specification of this information so it contains the basic specification of the data model of an organization. The interstriction model describes the 'location' of the information and the actors that make use of it. The blueprint can be used to determine the fundamentals of a new information system, but, more importantly, it can be used to assess the value of existing information systems. When the essential information in an organization is determined, criteria for evaluating the design of existing systems become available.

In the this section we will introduce a case study that has been analysed, redesigned and automated on the basis of DEMO. The possibilities to use the DEMO models as a basis for business process optimization and ISD are explained in more detail in the discussion of the case study.

The Conciliation Board for Consumers (in Dutch abbreviated to SGC) is a non-profit organization aiming at negotiating quick, inexpensive and simple solutions for disagreements between customers and suppliers. SGC mediates for approximately 30 branches, each supported by an organizational unit with a different informational and documental realization. For suppliers, participation in a Conciliation Board for Consumers is an important part of the quality management. Optimal mediation of the board in consumer–supplier disputes requires optimal availability of internal and external information.

The initial request from SGC was to replace their 1970s mini-computing system and to re-engineer the internal and external information-handling processes of the organization. Automation of the processes in a workflow management system was one of the possibilities they wanted to have investigated. The first step taken was to analyse the current way of working. DEMO was used to describe the current situation at SGC. Before the DEMO analysis of SGC is presented, the current way of working at SGC is briefly described.

## A description of the current way of working

A request to the SGC for mediation begins with a letter explaining the nature of the complaint (whether it concerns housing, computers, travels, etc.) and its magnitude. The SGC receives about 12 000 letters every year. When a letter arrives, a file is opened. The file is assigned a unique identification number, the number of the complaint. It also contains the name of the committee the complaint relates to, the name of the complainer and the date the complaint was submitted. In the course of the procedure the file is used to archive additional information. On the basis of the first letter, a decision is made whether the complaint is taken into consideration or not.

When the complaint is taken into consideration (about 70% of the complaints), the complainer is requested to fill out a questionnaire, to pay a complaint fee (based on the amount of the invoice), and to deposit the remaining amount of the invoice. At the same time, the supplier is requested to supply a bank guarantee. As soon as the questionnaire is returned, the money is transferred by the complainer, and the bank guarantee is provided by the supplier, and the procedure continues. If the complainer fails to meet (one of) these conditions within 1 month, the meditation request is turned down.

Besides exclusion on the basis of failing to meet the standard requirements, there are other reasons why SGC can turn down a request for mediation. A request is turned down if the article the complaint relates to is used for professional purposes, or has caused physical injury, or if the supplier has already gone bankrupt, or if the supplier is not a member of a branch organization.

When the request for mediation by SGC is granted, the supplier is informed by mail, and the execution of the procedure is filed in the so-called complaint book. This complaint book was set up for the purpose of progress monitoring. At the same time the supplier is given the file documents and is requested to supply a defence or to propose a settlement. In addition to the complaint of the customer and the defence of the supplier, the board can initiate an investigation by an expert.

All the documents of the customer, supplier and possibly the experts form the input for a meeting of a special committee of the board, to which all parties involved are invited. In this meeting the committee reaches a decision. About 1 month after the meeting the parties involved are informed by mail about the judgement of the committee.

After the judgement of the committee, financial matters between the customer and the supplier are settled, including the complaint fee, the deposits, and the expenses of the members of the committee and the experts. If the supplier fails to comply with his terms of payment, the consumer can appeal to a regulatory body that assures payment. At the same time the branch organization of the supplier is informed. Then, the file is closed.

## The DEMO analysis of SGC

The first step in the DEMO analysis of the SGC is describing the activities at the essential level. This means that the business is described as a network of interrelated business transactions. These transactions are formulated at type level and are displayed in a transaction table (Table 2), which includes the types of the object world facts resulting from these transactions. The resulting facts are represented in a high-level manner, called the case-type level. More detailed information of the case type is revealed in the fact model. The case type for SGC is the complaint. (Time variables, such as the date the complaint is submitted, or the date the committee passes judgement, have been left out for reasons of clarity.)

Figure 6 shows the combined representation (for the sake of brevity) of the interaction model and the interstriction model called the communication diagram. The actors are represented by numbered A-squares. The grey S-squares represent complex (external) actors. We do not know (or do not want to know yet) how they are composed. A T-numbered disk in the diamond represents a transaction type. The actor that connects to such a transaction symbol by a line with an arrowhead is the executor of the transaction type, whereas the plain line connects the initiator to the transaction symbol. The dotted lines represent informative links between actors and transaction types. These links are part of the interstriction model. They represent an actor's need for (some of) the information stored in the information banks for the execution of its own transactions. For example, for checking the mediation requirements, and thus the possible initiation of the transactions as a result of which the supplier is requested to provide a defence, the actor A6 needs the resulting facts that are stored in T1, T2, T3 and T4 relating to a particular complaint Co. The communication diagram also contains an external fact bank (EB1). This bank contains the rules for the mediation that are laid down in the regulations of SGC. For more syntactic and semantic details on the graphical notation of the communication diagram see (Dietz, 1996a,b; van Reijswoud, 1996).

Table 2. The transaction table of the current way of working at SGC

<table><tr><td>Transaction type</td><td>Result case type</td></tr><tr><td>T1 Admitting_complaint declared to be admissible</td><td>F1 The complaintis declared to be admissible</td></tr><tr><td>T2 Mediating_complaint</td><td>F2 The complaintis mediated</td></tr><tr><td>T3 Paying_consumer_fee</td><td>F3 The consumer complaint fee concerning complaintis paid</td></tr><tr><td>T4 Depositing_invoice_amount</td><td>F4 The remaining invoice amount of complaintis deposited</td></tr><tr><td>T5 Depositing_bank_guarantee</td><td>F5 The bank guarantee concerning complaintis deposited</td></tr><tr><td>T6 Dealing_with_complaint</td><td>F6 The complaintis dealt with</td></tr><tr><td>T7 Defending_complaint</td><td>F7 The complaintis defended</td></tr><tr><td>T8 Obtaining_expert_advice</td><td>T8 The advice from expertconcerning complaint is obtained</td></tr><tr><td>T9 Passing_judgement</td><td>F9 The judgement concerning complaintis passed</td></tr><tr><td>T10 Paying_supplier fee</td><td>F10 The supplier complaintfee concerning complaint is paid</td></tr></table>

![](/api/attachments/X2YE6THT/fulltext/images/967c538f468e4b963855ebf2ea8dc3df738d7cfaf2c718e70c47af9c8a91fd25.jpg)  
Figure 6. Communication diagram of SGC.

The DEMO communication diagram provides an overview of the organization as a network of communicative commitments. However, it does not show the precedence relationships, both causally and conditionally, between the transaction types. The process model is used to highlight these relationships.

The process diagram (Figure 7) that shows the relationships between the transaction types of SGC is presented below. Circles or ovals represent transaction types. A small circle represents the point of initiation. Solid arrows represent causal relationships, whereas dotted arrows represent conditional relationships. Optional relationships are indicated with a small horizontal line on the causal relationship arrow. The different stages of a transaction (order, execution and result phase) are represented as an extension to the identifier of the transaction type.

Looking at relationships between the transaction types of SGC creates a deeper understanding of the working of the organization. We can see that not all of them need to be executed for successful mediation. Transactions T4 (depositing\_invoice\_amount), T5 (depositing\_bank\_guarantee), T8 (obtaining\_expert\_advice), and T10 (paying\_supplier\_fee) are optional. For example, if the complainer has already paid the total amount of the invoice, the payment of a deposit is not requested. Similarly, if the committee decides that the complaint of the consumer is not valid, the supplier does not have to pay for the mediation.

![](/api/attachments/X2YE6THT/fulltext/images/181663b4aeba543ffdbef912269a7c3d3009f809e1df1d320880a6ab534443d3.jpg)  
Figure 7. Process diagram of SGC.

Insight into the object world of SGC is obtained using the fact model (Figure 7). This model provides a complete and precise specification of the (essential) fact types associated with the case type that are created and/or used as well as the external fact types needed. The fact model is represented by means of the ORM/NIAM-like fact diagram [for details on Object Role Modelling and NIAM (Natural language Information Analysis Method) see Nijssen & Halpin (1989) and Halpin (1998); the fact diagram is explained in Dietz (1996b), van Reijswoud (1996) and Rijst & van Reijswoud (1995)]. The notation has been chosen because of its natural language-based philosophy. In Figure 8, a small part of the fact diagram of SGC is presented.

In Figure 8, the fact diagram of actor A1 is presented. The circles denote object classes; the class names are written above the circles. Fact types are represented by one or more adjacent rectangles and are identified by a fact-type number (F#). The objects play different roles in a fact. In the fact diagram these roles are indicated by numbers in rectangles and referred to in the sentences below the roles. Figure 8 shows the fact types constituting the case types, which are used and/or created by actor 2, mediation of SGC. In the centre of the diagram is the object class complaint. The fact diagram also shows that a description is related to a complaint (this is a special object class containing textual description of the complaint), that a request for mediation is performed on a particular date and has been completed on a particular date, that a complaint is mediated by a particular committee, and finally that a complaint is submitted by a complainer and relates to a particular supplier. The uniqueness constraints, which are the bold lines above the roles, show that every complaint is unique (identified through a unique identification number in everyday practice of SGC) and thus may not appear more than once in the extension.

![](/api/attachments/X2YE6THT/fulltext/images/1fa995cb65839da6c66fe70a9a976133939c148b8bf59d56413c4a5317c87ecb.jpg)  
Figure 8. Part of the fact diagram of SGC.  
© 1999 Blackwell Science Ltd, Information Systems Journal 9, 117–138

The action model of DEMO provides a detailed procedure of acting for the actors in the system under consideration. The action model not only represents the transactional structure of an organization at the essential level, but also allows inclusion of the specification of the realizations of the essential transactions at the informational and documental levels.

Figure 9 shows the procedure of the execution phase of 'T2 mediating\_complaint' (T2/E in Figure 7). The arrows represent precedence relationships. The first white box on the left-hand side shows the communicative act by which SGC requests the complainer to pay the complaint fee. The waiting condition below indicates that the complaint fee has to be paid before the procedure can continue. The two elements next to the initiation of T3 are optional. T4 and T5 are only initiated if the question in the triangular shapes is answered with 'Yes', otherwise the procedure continues to the synchronization (the upside-down triangle). After the synchronization the execution procedure of transaction T2 proceeds to initiation of transaction T6. At this point the procedure will halt until the transactions T7, T9 and the optional T8 and T10 as part of T6 are completed. The execution of the transactions is described in the action diagram of actor

![](/api/attachments/X2YE6THT/fulltext/images/c232a46c3824a5f529d0217852b37de4eacf015656f346b2128a9bc471b27367.jpg)  
Figure 9. Action diagram of the execution phase of transaction T2.

A6, handle-complaint. When T6 is carried out, the actual objective action of T2, the mediation of the complaint, is executed. Lastly, the result of the execution of this objective action is stated to the consumer, realized in the notification (statement) of the outcome of the mediation of actor A2. Normally, this becomes tangible in a notification letter from SGC to the consumer.

## Discussion of SGC

The high-level analysis of SGC with DEMO allowed the representation of the 30 different branch-specific mediation procedures in one business model. Although every organizational unit required a specific realization at the informational and documental level, essentially all units performed the same transaction types. On the basis of these models, in which the transactional structure of the organization is described, an implementation project is started in two directions.

## Business process optimization

The DEMO models of SGC suggest several ways in which the efficiency and the effectiveness of the business processes can be optimized. First, the communication diagram shows that transaction T1, admitting\_complaint, can be deleted, because the consumer can use the questionnaire to begin the mediation procedure (T2). Second, the process diagram makes clear that the process can be shortened, by moving the conditional relationships between T3, T4, T5 and T6/O (see Figure 7) to T9, so that the committee only meets in order to pass judgement if the customer has paid the complaint fee and the deposit, and if the supplier has given a bank guarantee. Third, we suggest that the individual transaction processes of T1 and T2 can be optimized by the introduction of standardized (electronic) forms for requesting mediation.

## Information system design

If the DEMO analysis of the case study is taken as a starting point, we can determine the blueprint of an information system. The information needed for this blueprint is specified by the fact diagrams of the two actors (like the one in Figure 8). Some of this information is created by the actor as a result of the successful execution of a transaction, and some of the information is obtained from other sources, such as the regulations of the SGC, which supply the rules for mediation. The communication diagram (Figure 6) shows that the facts resulting from the successful execution of transactions T1–T4 are important for actor A6. For the architecture of the information system, this implies that this information needs to be made available to the persons in the organization who perform the role ‘checking mediation requirements’.

The goal of a DEMO analysis for information systems design is to create a conceptual scheme of the information system and to describe the information architecture. In this way DEMO supplies the starting point from which the informational (e.g. derived and aggregated information such as management information) and the documental (e.g. user interface)

realizations of an information system can be determined. In the case of SGC the business transaction types form the basis for the specification of a workflow management system that can be configured for all existing and new mediation procedures.

## CONCLUSIONS

In this article we have introduced and illustrated a communicative action-based methodology for modelling business processes and information systems in the seventh generation of ISD. Because it combines business modelling with information modelling, it provides a sound basis for business–IT alignment in dynamic organizations. The communicative action-based modelling methodology DEMO provides an understanding of organizations that augments information and document-oriented modelling approaches. By focusing on the communication that constitutes the business processes, we obtain a rich understanding of the dynamics of an organization. Because the information systems' blueprint is directly derived from the business communication processes, we can establish a stronger relationship between the business and its information systems.

The DEMO approach supports modelling of an organization from different perspectives. The distinction between the essential level on the one hand and the informational and documental levels on the other presents a new perspective on both business process optimization and on engineering of information systems and infrastructure. It creates a direct relationship with the core of the business (the essential level) and the informational and documental realizations of the core. The different models also allow different interrelated perspectives at the essential level. The interaction model describes an organization as a structure of customers and suppliers, and products/services, whereas the process model describes the organization as a structure of activities. The fact model and the interstriction model are concerned with the information-producing and information-storing characteristics of an organization. Finally, the action model highlights the organization as a decision-making system. Together, these models of DEMO provide a more detailed and richer description of an organization than other communicative action-based modelling approaches do.

The DEMO modelling approach has been applied to some large-scale projects and to several smaller ones. Examples of large-scale projects are Dutch Telecom and the Rotterdam Police Force. Smaller projects are projects like SGC, but there are also some small (production) companies (most of the reports on these cases are in Dutch and in most cases confidential, but the authors can be contacted for English summaries). The purpose of the projects is diverse. In the case of SGC, DEMO was applied as a means for business process optimization and information systems development. However, in other projects a DEMO analysis was used to perform business function redefinition, the evaluation of the current information systems from a business perspective and organizational redesign, i.e. the reallocation of responsible individuals to identified actors. DEMO has been applied successfully both in the production industry and in the service industry. Because of its focus on communication, the methodology has proven to be equally applicable in both areas.

The application of the DEMO methodology also revealed some pitfalls. Firstly, different perspectives of the organizational members may result in different definitions of transaction types. To overcome this problem, participation of personnel with business responsibility in the project team is required. Secondly, the time needed to understand the way of thinking and modelling of DEMO has proven to be short; in the case of SGC this took 2 days. However, the application of DEMO methodology takes a considerable longer period because it requires a sound understanding of both the business and the IS perspective in order to translate the models into solutions. Finally, there are no tools that support the translation of DEMO models in informational, technical and organizational realizations.

To integrate the DEMO methodology with dominant modelling approaches at the informational and documental level, current research focuses on the development of interfaces between DEMO and the unified modelling language and between DEMO and the petri-net modelling of workflow processes. Also, research aims at establishing the relationship between DEMO and the specification of component-based software architectures. Furthermore, research is conducted on the development of a supporting modelling and simulation tool.

## REFERENCES

Auramäki, E. & Lyytinen, K. (1996) On the success of speech acts and negotiating commitments. In: Communication Modeling – the Language/Action Perspective, Dignum, F., Dietz, J., Verharen, H. & Weigand E. (eds). Electronic Workshops in Computing. Springer. http://www.springer.co.uk/ewic/workshops/CM96/.

Auramäki, E., Lehtinen, E. & Lyytinen, K. (1988) A speech act based office modeling approach. ACM Transactions on Office Information Systems, 6 (2), 126–152.

Auramäki, E., Hirschheim R., & Lyytinen, K. (1991) Modeling offices through discourse analysis: the SAMPO approach. The Computer Journal, 35, 342–352.

Austin, J.L. (1962) How to Do Things with Words. Clarendon Press, Oxford.

Ballmer, Th. & Brennenstuhl, W. (1981) Speech Act Classification, Springer-Verlag, New York.

Beek, A.J.J., Mulder, J.B.F. & van Reijswoud, V.E. (1997) Rapid application development in dynamic organisations with business modelling: a practitioner's point of view. In: The Proceedings of the Caise'97/IFIP8 1 International Workshop on Evaluation of Modelling Methods in Systems Analysis and Design, Barcelona

Checkland, P. (1981) Systems Thinking, Systems Practice.
John Wiley, Chichester.

Checkland, P. & Scholes, J. (1990) Soft Systems Methodology in Action. John Wiley, Chichester.

Davenport, T.H. (1993) Process Innovation. Harvard Business School Press, Boston.

Davenport, T.H. (1995) Business process reengineering: where it's been, where it's going. In: Business Process Change: Reengineering Concept, Methods and Technologies, Grover, V. & Kettinger, W.J. (eds), pp. 1–13. Idea Group Publishing, Harrisburg,

Denning, P.J. & Medina-Mora, R. (1995) Completing the loops. Interfaces, 25 (3), 42–57.

Dietz, J.L.G. (1994a) Business modeling for business redesign. Proceedings of the 27th Hawaii International Conference on System Sciences, pp. 723–732. IEEE Computer Society Press, Los Alamitos.

Dietz, J.L.G. (1994b) Modelling business processes for the purpose of redesign. In: Proceedings of the IFIP TC8 Open Conference on Business Process Re-Engineering: Information Systems Opportunities and Challenges, Glasson, B.C., Hawryszkiewycs, I.T., Underwood, B.A. & Weber, R.A. (eds), pp. 249–258. Elsevier, Amsterdam.

Dietz, J.L.G. (1996a) The what and the why of modelling business processes. In: Dynamic Enterprise Modeling, van Es, R.M. & Post A. (eds). Kluwer Bedrijfsinformatie, Deventer.

Dietz, J.L.G. (1996b) Introductie tot DEMO: Van informatietechnologie naar organisatietechnologie. Samson, Alphen a/d Rijn.

Dietz, J.L.G. & Mulder H.B.F. (1996) Realising Strategic Reengineering Objectives with DEMO. In: Proceedings of the International Symposium on Business Process Modelling, Springer-Verlag, New York.

Dietz, J.L.G. & Mulder H.B.F. (1998) Transformation of organisations requires constructional knowledge of business systems. Proceedings of the 31st Hawaii International Conference on Systems Sciences. IEEE Computer Society Press, Los Alamitos, CA.

Dietz, J.L.G., Goldkuhl, G., Lind, M., & van Reijswoud, V.E. (1988) The Communicative action paradigm for business modelling – a research agenda. In: Proceedings of the Third International Workshop on the Language/Action Perspective, Jonkoping International Business School, Department of Informatics, Goldkuhl G. & Lind M. (eds), pp. 59–70.

Dignum, F. & Dietz, J.L.G. (1997) Communication modeling – the language/action perspective. Proceedings of the First International Workshop on Communication Modeling, Computer Science Reports. Eindhoven University of Technology. http://www.win.tue.nl/win/cs.

Dignum, F., Dietz, J., Verharen, E. & Weigand H. (eds) (1996) Communication Modeling – the Language/Action Perspective, Proceedings of the First International Workshop on Communication Modeling, Electronic Workshops in Computing Springer, http://www.springer.co.uk/ewic/workshops/CM96/.

Donovan, J.J. (1994) Business Reengineering with Information Technology. Prentice Hall, Englewood Cliffs.

Flores, F. & Ludlow, J.J. (1981) Doing and speaking in the office. In: Decision Support Systems: Issues and Challenges, Fick, G. & Spraque, H. Jr. (eds), pp. 95–118. Pergamon Press, New York.

Goldkuhl, G. (1992) Contextual activity modelling of information systems. Proceedings of the 3rd International Working Conference on Dynamic Modelling of Information Systems, Noordwijkerhout

Goldkuhl, G. (1996) Generic business frameworks and action modelling. In: Communication Modeling – the Language/Action Perspective, Proceedings of the First International Workshop on Communication Modeling, Dignum, F., Dietz, J., Verharen, E., Weigand H. (eds), Electronic Workshops in Computing Springer, http://www.springer.co.uk/ewic/workshops/CM96/.

Goldkuhl, G.A., Röstlinger (1993) Joint elicitation of problems: An important aspect of change analysis. In: Human, Organizational Social Dimensions of Information Systems Development, Avison, D.E., Kendal, J.E. & DeGross, J.I. (eds). Elsevier, North-Holland.

Habermas, J. (1984) Theory of Communicative Action: Reason and Rationalization of Society. Polity Press, Cambridge.

Habermas, J. (1988) Bemerkungen zu J. Searle's 'Meaning, Communication and Representation'. In: Nachme-

taphysisches Denken, pp. 137–149. Suhrkamp-Verlag, Frankfurt am Main.

Halpin, T. (1998). Object Role Modeling (ORM/NIAM). Handbook on Information Systems Architectures. Springer-Verlag (in press).

Hammer, M. (1990) Reengineering work: don't automate, obliterate. Harvard Business Review, July–August, 104–112.

Hammer, M. & Champy, J.A. (1993) Reengineering the Corporation: a Manifesto for Business Revolution. Nicholas Brealy, London.

Hirschheim, R., Klein, H.K. & Lyytinen, K (1995) Information Systems Development and Data Modelling: Conceptual and Philosophical Foundations. Cambridge University Press, Cambridge.

livari, J., Hirschheim, R. & Klein, H.K. (1997) A comparison of five alternative approaches to information systems development. Australian Journal of Information Systems, 5, 3–29.

Janson, M.A. & Woo, C.C., (1992) Investigating information and knowledge gathering methods, a. speech act lexicon perspective. In: Information Systems Concepts: Improving the Understanding. Falkenberg, E.D., Rolland, C. & El-Sayed, E.N. (eds), pp. 239–257. Elsevier, North-Holland.

Keen, P.G.W. (1991) Shaping the Future: Business Design Through Information Technology. Harvard Business School Press, Harvard.

Lehtinen, E. & Lyytinen, K. (1986) Action based model of information system. Information Systems, 11, 299–317.

Lundeberg, M., Goldkuhl, G. & Nilson, A. (1981) Information Systems Development: a Systematic Approach. Prentice Hall, Englewood Cliffs.

Martin, J. (1987) Information Engineering. Savant, Lancaster.

Medina-Mora, R., Winograd, T., Flores, R., & Flores, F. (1992) The action workflow approach to workflow management technology. In: Proceedings of the 4th Conference on Computer Supported Cooperative Work, Turner, J. & Kraut R. (eds). ACM, New York.

Mumford, E. (1983) Designing Human Systems. Manchester Business School, Manchester.

Mumford, E. (1985) Defining systems requirements to meet business needs: a case study example. The Computer Journal, 28, (2), 97–104.

Nijssen, G.M. & Halpin, T.A. (1989) Conceptual Schema and Relational Database Design: a Fact Oriented Approach. Prentice Hall, Sidney.

Porter, M.E. (1985) Competitive Advantage, Creating and Sustaining Superior Performance. The Free Press, New York.

Porter, M.E. & Millar, V.E. (1985) How information gives you competitive advantages. Harvard Business Review July–August, 149–160.

van Reijswoud, V.E. (1996) The structure of business communication: theory, model and application. PhD Thesis, Delft University of Technology, Delft.

van Reijswoud, V.E. (1999) Model based business system transformation. Proceedings of the European Conference on information Systems (ECIS'99), Copenhagen.

van Reijswoud, V.E. & Lind, M (1998) Comparing two business modelling approaches in the language action perspective. In: Goldkuhl G. & Lind M. (eds), Proceedings of the Third International Workshop on Communication Modelling: LAP'98, Stockholm.

van Reijswoud, V.E. & van der Rijst N.B.J. (1995a) Modelling business communication as a foundation for business process redesign: a case of production logistics. In: Proceedings of the 28th Hawaii International Conference on Systems Sciences, pp. 841–850. IEEE Computer Society Press, Los Alamitos CA

van Reijswoud, V.E. & van der Rijst, N.B.J. (1995b) Modeling business communication for the purpose of business process reengineering. In: Information Systems Methodologies 1995: Third Conference on Information Systems Methodologies of the British Computer Society Information Systems Methodologies Specialist Group, Jayaratna, N., Miles, R., Merali, Y. & Probert, S. (eds), pp. 173–184. NEWI, Wrexham.

van der Rijst, B.J. & van Reijswoud V.E. (1995) Comparing two speech act based modeling approaches for the purpose of information systems development. In: Proceedings of the Third European Conference on Information Systems, ECIS'95, Athens, Doukidis, G., Galliers, R., Jelassi, T., Krcmar, H. & Land F. (eds), pp. 353–365.

Schäl, T. (1996) Workflow Management Systems for Process Organisations. Lecture Notes in Computer Science 1096. Springer, Berlin.

Schäl, T. & Zeller, B. (1993) Workflow management systems for financial services. Proceedings of the Conference on Organizational Computing Systems, COOCS'93. pp. 142–153. ACM, New York.

Scott Morton, M.S. (1991) The Corporation of the 1990s: Information Technology and Organizational Transformation, Sloan School of Management. Oxford University Press, New York.

Searle, J.R. (1969) Speech Acts: an Essay in the Philosophy of Language. Cambridge University Press, Cambridge.

Searle, J.R. (1979) Meaning and Expression. Cambridge University Press, Cambridge.

Searle, J.R. & Vanderveken, D. (1985) Foundations of Illocutionary Logic. Cambridge University Press, Cambridge.

Steuten, A.A.G. (1998) A contribution to the linguistic analysis of business conversations within the language/action perspective. PhD Thesis, Delft University of Technology, Delft.

Steuten, A.A.G. & van Reijswoud V.E. (1996). The interpretation of business communication. The application of functional grammar and the transaction process model. In: Proceedings of the First International Workshop on Communication Modeling, the Language/Action Perspective, Electronic Workshops in Computer Science. Springer-Verlag, London.

Taylor, J.R. (1993) Rethinking theory of Organizational Communication: How to Read an Organization. Ablex, Norwood.

Taylor, T.J. & Cameron, D. (1987) Analysing Conversation: Rules and Units in the Structure of Talk. Pergamon Press, Oxford.

Teng, J.T.C., Kettinger, W.J., & Guha, S. (1992) Business process redesign and information architecture: establishing the missing links. In: Proceedings of the International Conference on Information Systems, DeGross, J.I., Becker, J.D, Elam. J.J. (eds). ICIS, Dallas.

Vendler, Z. (1967) Linguistics in Philosophy. Cornell University Press, Ithaca, NY.

Winograd, T. (1988) A language/action perspective on the design of cooperative work. In: Computer Supported Cooperative Work: A Book of Readings. Greif, I. (ed.). Morgan Kaufmann, San Mateo.

Winograd, T. & Flores, F. (1986) Understanding Computers and Cognition: A New Foundation for Design. Ablex, Norwood NJ.

Yourdon, E. (1989) Modern Structured Analysis. Prentice Hall, Englewood Cliffs.

Yourdon, E. (1993) Yourdon Systems Method: Model Driven Systems Development. Prentice Hall, Englewood Cliffs.

## Biographies

Victor E. van Reijswoud is assistant professor at the department of information systems of Delft University of Technology. He holds a MPhil in the Philosophy of Health Sciences from Maastricht University in the Netherlands and the University of Bath in the UK, and a PhD in Information Systems from Delft University of Technology. He has presented his research work on business process modelling and business process optimization at a large number of national and international conferences. Dr van Reijswoud is also employed as project advisor by the Dutch consulting company Essential Action Engineers b.v.

Hans B. F. Mulder is a Member of the Board of Venture Informatising Adviesgroep n.v., a consortium of enterprises in the Dutch IT industry. He is also managing director of Essential Action Engineers b.v., a consultancy company specializing in business processes and information systems. He has held several positions, which range from software developer to project manager. He received his Bachelors Degree in Informatics from the polytechnics in The Hague, and his Masters Degree in General Management from Nijenrode University in 1994. Since 1995 he has published several articles and case studies on the subject of business and information modelling and is currently working on his PhD thesis at the Delft University of Technology.

Jan L. G. Dietz started his scientific career in 1980 at the Faculty of Industrial Engineering of Eindhoven University of Technology, after having worked as a practitioner since 1970. In 1987 he obtained his Doctoral Degree on the subject of modelling and specifying information systems. In January 1988 he was appointed Professor of Management Information Systems at the University of Maastricht in the Faculty of Economics and Business Administration. Since September 1994 he has been Professor of Information Systems at Delft University of Technology in the Faculty of Information Technology and Systems.
