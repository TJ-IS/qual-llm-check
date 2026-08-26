---
otero_id: 20875
otero_key: "CB6VP8CX"
title: "INCAS: a legal expert system for contract terms in electronic commerce"
authors: "Yao-Hua Tan; Walter Thoen"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00085-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# INCAS: a legal expert system for contract terms in electronic commerce<sup>q</sup>

Yao-Hua Tan<sup>)</sup>, Walter Thoen

Erasmus UniÕersity Research Institute for Decision and Information Systems EURIDIS and Erasmus Center for Electronic Commerce( ) ( ) ECEC , Erasmus UniÕersity Rotterdam, P.O. Box 1738, 3000 DR Rotterdam, Netherlands

## Abstract

Electronic commerce is doing business via electronic networks. Paper-based trade documents such as, for example, request for quotation, purchase order or invoice are replaced by electronic messages, in particular Electronic Data Interchange EDI messages. These electronic messages are not only transmitted much faster than paper-based documents,Ž . but they can also be processed automatically by computers. An example of this automated processing of electronic messages is electronic contracting and negotiation where the actual trade contract is on-line negotiated and concluded via an electronic network. We present the legal expert system INCAS that can provide on-line explanations about the use of Incoterms in trade contracts. Incoterms stipulate which party buyer or seller is responsible for arranging and paying transport of theŽ . goods, and arranging the documents necessary for this transport e.g. export and import clearance documents, certification ofŽ origin, quality certificates etc. . INCAS is implemented in the programming language Prolog. We also explain how the. defeasible reasoning capability of Prolog is essential for modelling the reasoning about the Incoterms. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic commerce; Regulations; Trade procedures; Incoterms; Legal reasoning; Deontic logic; Defeasible logic

## 1. Introduction

Electronic commerce is doing business via electronic networks. Paper-based trade documents such as, for example, request for quotation, purchase order or invoice are replaced by electronic messages, in particular Electronic Data Interchange EDI mes- Ž . sages. These electronic messages are not only transmitted much faster than paper-based documents, but they can also be processed automatically by computers. For the efficiency gain of electronic versus paper-based messages this automated processing is perhaps more important than the electronic transmission of the message see Ref. 13 . Currently, theŽ <sup>w</sup> <sup>x</sup>. automated processing of electronic messages is restricted to automated entering of data in the company’s database and simple processing such as, for example, automatic invoicing or calculation and payment of VAT. But one can imagine more advanced types of processing. For example, basic legal inferences could be made from an electronic message. For example, if one becomes the new owner of a good by receiving an ownership document for this good, it might be convenient that the processing system automatically makes the inference that as new owner you are liable in case of damage incurred by the goods, and that from this observation it subsequently infers automatically that insurance has to be arranged for these goods. A more sophisticated type of automated processing of electronic messages is electronic contracting and negotiation where the actual trade contract is on-line negotiated and concluded via an electronic network. In principle this negotiation process could be done by autonomous software agents that are instructed by a human user how to negotiate for him. However, in most cases the electronic negotiation process will probably be semi-automated where the human user is also involved and takes the final decision. Also, here automated processing can be very helpful, for example where the computer analyses the content of the contract and provides what-if analyses to explain to the user what his liabilities and risks are if he agrees to a proposed contract. For example, in most cases trade contracts contain terms for the type of delivery of the traded goods. These terms, the so-called Incoterms, stipulate which party buyer or seller isŽ . responsible for arranging and paying transport of the goods and arranging the documents necessary for this transport e.g. export and import clearance docu-Ž ments, certification of origin, quality certificates, etc. . There are 13 different terms. Usually, these. terms are included in the contract only by reference to an abbreviated code without any further explanation. For example, the term EXW Ž . AEx WorksB says that the seller has the obligation to make the goods available at his premises to the buyer. The buyer is obliged to arrange and pay transport of the goods from the seller’s premises to his own premises. Furthermore, under EXW the buyer bears all the risks of damage of the goods during transport. A very popular term is FOB Ž . AFree On BoardB , which says that the seller is responsible for transport of the goods until they have passed ship’s rail at the named port of shipment. The seller is also responsible for clearing the goods for export, and bears all the risks of damage of the goods during transport until the goods have passed the ship’s rail. After the ship’s rail all obligations for transport of the goods and arranging the necessary documents are for the buyer. Differences between Incoterms can be very subtle.

For example, the only difference between FOB and FAS Ž . AFree Alongside ShipB is that under FOB the seller is responsible for everything until the goods have passed the ship’s rail, whereas under FAS he is responsible for everything until just before the ship’s rail. Hence, under FOB the seller has to arrange export clearance of the goods, but not under FAS. For further details on the Incoterms the reader is referred to Appendix A. When negotiating the delivery terms of a contract on-line it would be very helpful when the negotiator could consult an on-line automated expert system that gives some explanation about the meaning of the specific delivery term proposed in the contract. In this article we present the system INCAS that provides this service.

Incoterms were developed by the International Chamber of Commerce ICC . In 1936, when In-Ž . coterms were first published, the initial objective of the ICC was to make available to traders a means to avoid the worst causes of friction resulting from the diversity of interpretation of legal terms in international commerce. The ICC is not the only organisation to offer standard legal terms for international commerce. National rules like those included in the US Uniform Commercial Code are also used in international commerce.

Some forms of electronic commerce, e.g. open EDI, support the use of standard business procedures. Open EDI enables short term or ad hoc commercial transactions between organisations. A business procedure is the set of mutually agreed upon rules that governs the activities of all parties involved in a set of related business transactions. Business procedures in electronic commerce are envisaged to be publicly available, remotely accessible and directly executable 2, pp. 84–87 19, pp. 27–30 .<sup>w</sup> <sup>xw</sup> <sup>x</sup> When designing trade procedures it is essential to take into account certain legal considerations that interrelate with the type of the transactions in question. Since Incoterms have been so widely accepted and in some cases constitute part of commercial practice, they should be taken into consideration when designing these procedures 14 .<sup>w</sup> <sup>x</sup>

The emergence of electronic commerce applications has sparked yet more ICC initiatives 10,12 18,<sup>w</sup> <sup>xw</sup> pp. 249–259 19, pp. 249–264 24 . ETERMS, an <sup>xw</sup> <sup>xw</sup> <sup>x</sup> initiative of the ICC, aims at putting legal problems of electronic commerce into a broader perspective and addressing the legal questions of electronic commerce transactions. The ETERMS project aims at making available a Repository of commercial terms for electronic commerce, like terms and agreements contributed by users of electronic commerce. ETERMS can be used to communicate generally accepted terms and agreements, such as Incoterms, specialised terms and agreements that do not necessarily reflect current trade use, electronic commerce conventions, guidelines and rules as well as international conventions on electronic commerce. A second kind of ETERMS is Recognised Practice Terms for electronic commerce, as they will be contributed by an appointed group of legal experts. Lessons learned and techniques applied in INCAS can be re-used for the further development of the ETERMS Repository.

INCAS INCoterms Advise system is a Prolog-Ž . based expert system that gives advice to users about the use of Incoterms delivery terms in trade contracts. This expert system has been developed at EURIDIS under the supervision of Yao-Hua Tan. INCAS provides users with several types of information about Incoterms. Firstly, INCAS can explain Incoterms to the user. Secondly, it can reason with the Incoterms knowledge about specific situations and give customised advice in specific problem situations. For example, if a seller is trading goods X under a specific Incoterm Y, and the goods are damaged in port Z, then the system can inform the seller whether he is liable for this damage or not. Thirdly, INCAS can also support the negotiation of delivery terms in a sales contract between buyer and seller. If the buyer and seller tell the system what responsibilities each of the parties is prepared to take in the trade transaction, then the system can propose the optimal Incoterm that is best for both buyer and seller. This negotiation process is considered to be a barrier in international trade, because it requires an expert knowledge about Incoterms that most smalland medium-size companies cannot afford. INCAS is a system that aims at adapting Incoterms to the requirements of electronic commerce. Having tools that explain Incoterms to newcomers in electronic commerce can substantially improve the opportunities of these users to participate in electronic commerce. The ICC published the Guide to Incoterms 1990, which is an explanation of the Incoterms for users without legal expertise. This publication turned out to be highly successful and very helpful, in particular for small- and medium-size companies. However, it still requires a considerable effort to familiarise oneself with the content of this book. INCAS is essentially an electronic version of the Guide to Incoterms that can be available via the Internet. Although, the system has been developed as a stand-alone application, it could also be developed into an automatic expert system that can be accessed via a World Wide Web browser that is connected to an electronic network like the Internet. We see a potential for INCAS as an on-line help service that facilitates electronic commerce.

The implementation of INCAS is based on a formal specification of the Incoterms in the logicbased programming language Prolog. A special feature of logic-based programming languages is that the execution of a program is similar to human reasoning. This makes these languages very suitable for implementing advice tasks, which are often based on reasoning tasks. The use of Prolog to build legal expert systems is not new. For example, an expert system based on a Prolog implementation of the British Nationality Act was already given in Ref. <sup>w x</sup> <sup>w x</sup> 15 and in Ref. 27 the Prolog-based deontic expert system shell DX was introduced. It has been hotly debated whether Prolog is adequate for implementing legal domains. We analyse to what extent the criticism applies to the Prolog formalisation of Incoterms in INCAS.

The Incoterms domain has a large number of interesting and complicated examples of defeasible reasoning. By defeasibility we mean that a rule is overruled by another rule or fact. For example, in Incoterms there is a rule that says that under certain terms the buyer is liable for damage to the traded goods when the goods have left the port of origin. But this rule can be overruled if the seller did not package the goods adequately. In that case the liability is transferred from the buyer to the seller. It has been a controversial issue to what extent defeasibility really occurs in legal domains. Some researchers claim that there is no defeasibility in legal domains, and that apparent cases of defeasibility are actually cases of complementary rules. In other words, it is not the case that there is a rule that is overruled by another rule, but there are simply two rules with different application domains; one rule that applies to the adequate packaging situation, and then the buyer is liable, and the other rule that applies to the inadequate packaging situation, and then the seller is liable. A closer look at Incoterms shows that there is real defeasibility in this domain. We also discuss in detail how this defeasibility is implemented in IN-CAS.

This article is organised as follows. In Section 2 the basic notions of the Incoterms are addressed. In Section 3 the functionality of INCAS is described. In Section 4 the technical details of the implementation of INCAS are discussed. In Section 5 the defeasible reasoning aspects of INCAS are discussed. In Section 6 the analysis of the logical aspects of INCAS is given. In Section 7 an example of the user’s interaction with INCAS is given. Finally, Section 8 contains the conclusions.

## 2. Basic notions of the Incoterms

In Incoterms, basic notions are those necessary definitions that refer to commercial transactions regulated by Incoterms. This part addresses some basic notions necessary to understanding the structure and functionality of Incoterms. Transport, delivery point, cost, risk, documents, clearance and mode of transport are the most important ones. To transport the goods means to make the goods available to the buyer at the agreed point of destination. The transport of goods can be divided into three parts:

<sup>Ø</sup> from the premises of the seller to the border of the country of origin pre-carriage ;Ž .

<sup>Ø</sup> from the border of the country of origin to the border of the country of destination main car- Ž riage ;.

<sup>Ø</sup> from the border of country of destination to the premises of the buyer on-carriage . Ž .

According to the classification of Incoterms there can be several different delivery points. The delivery point is essential for the transfer of risk and costs between the buyer and seller. Crucial delivery points are the following:

1. the door of the seller’s depot;

2. the point where the goods are in custody of the carrier, cleared for export;

3. the point at the quay where the goods are placed alongside the ship, waiting to be cleared for export;

4. the point where the goods are placed on board the ship, cleared for export;

5. the point where the goods are at the border of the country of origin, waiting to be cleared for export;

6. the point where the goods are on board the ship at the destination, waiting to be cleared for import;

7. the point where the goods are at the quay at the destination, cleared for import;

8. the point where the goods are at the door of the buyer’s depot, waiting to be cleared for import;

9. the point where the cleared goods are at the buyer’s door.

Cost includes all the expenses that the parties are aware of when making an agreement. Costs can be categorised as follows:

<sup>Ø</sup> Direct transport costs to bring the goods to the point where they are handed over to the buyer. Direct costs can be divided between the trading partners to deliver the goods to the quay, to bring the goods on board the ship, to ship the goods, to unload them and deliver them to the buyer’s premises.

<sup>Ø</sup> Costs that are made to obtain export and import clearances, like duties, VAT, administrative charges etc.

<sup>Ø</sup> Costs that are related to the provision of services and assistance.

<sup>Ø</sup> Insurance costs.

Risk is a generic commercial term that is not only linked to Incoterms. Although risk is a term often used in Incoterms, it is not explicitly explained therein. The party that takes care of the main-carriage is liable for the goods during the voyage and bears all risks. Risk is an issue for the trading partners when the parties perform an erroneous act, when they fail to perform a prescribed action and when unforeseen dangers emerge. In Incoterms, risk refers to covering the physical loss or damage. The notion of risk in Incoterms does not include other related dangers such as delay or non-fulfilment of obligations that the trading parties often undertake.

Insurance is a remedy to minimise the consequences of risk. The transfer of risk is closely related to the transfer of the liability for the goods. When insuring against risk the trading parties should consider the commercial practice and custom that applies in the line of trade in which they are involved.

Documents that are meaningful in the context of Incoterms are messages that are used to notify the buyer of the exact time of the delivery of the goods, licences that show that the goods are ready for export<sup>r</sup>import, documents proving ownership, a contract of carriage and proof of delivery.

Clearing the goods in customs is an issue essential to the use of Incoterms. Incoterms specify who does what to obtain licences, pay duties and taxes and who bears the risk in case of misfortune. Incoterms are concerned only with the mode of transport of the main-carriage.

Incoterms can be classified according to the mode of transport they can be used for. Goods can be transported in different modes by sea, inland waterway, road, rail, or air. The terms EXW, CPT, CIP, DAF, DDU and DDP can be used for multi-modal transport, although the parties can agree to use these terms for other forms of transport. Multi-modal transport includes a combination of modes to have the goods delivered. Full details of the Incoterms are given in the Appendix A Incoterms. In the following sections we discuss the functionality and implemen tation of INCAS. We look at what kind of advice INCAS can give the user. We illustrate the functionality by discussing several questions the user can ask INCAS and what information the answers give the user. After having discussed the functionality of INCAS we investigate how this functionality is implemented in INCAS. Finally, we show how the natural language clauses of Incoterms are represented in Prolog code.

## 3. INCAS: functionality

We distinguish three ways of using INCAS:

1. The first use of INCAS is to give the buyer and the seller a tool for determining the Incoterm that best suits their respective wishes. This tool is especially useful when the buyer and the seller negotiate a contract.

2. The second use of INCAS is to determine the responsibilities and liabilities of the buyer and the seller. For this use of INCAS an important distinction has to be made between reasoning about normal situations, where nothing is exceptional, and situations where exceptional circumstances apply. This second use can, therefore, be divided in:

2.1. using INCAS to determine the responsibilities and liabilities in normal situations

2.2. using INCAS to determine the responsibilities and liabilities in case of exceptional circumstances. Examples of exceptional circumstances are: an export ban, inadequate packaging by the seller, the vessel did not arrive on time, etc.

The distinction between the uses 2.1 and 2.2 is important because of the difference in complexity. The use 2.2 is more complicated and requires more legal expertise from the user. When INCAS is used to reason about situations with exceptional circumstances INCAS shows on which assumptions the conclusion is based. These assumptions are an important part of the argumentation that justifies the conclusion. By comparing the assumptions with the real world information the user can refine the argumentation and also the conclusion. Instead of adjusting the assumptions to the real world information it is also possible to make Awhat-ifB analyses by using hypothetical assumptions.

We discuss some sample questions to illustrate the functionality of INCAS.

## Example Question 1:

Question: Given the following lists of actions the parties are willing to perform, what are the best Incoterms to use?

Seller: provide goods, packaging, export <sub>–</sub>

Buyer: contract of carriage, import, insurance <sub>– –</sub> Answer: FOB

So, in case the seller is willing to provide the goods, package the goods and take care of the export formalities and the buyer is willing to contract a freight forwarder for the carriage of the goods to his premises, take care of the import formalities and insure the goods, then the best Incoterm to chose is Free On Board FOB .Ž .

## Example Question 2:

Question: Who bears the risk for damage of the goods under the FOB term when the goods are stored in the port of shipment?

Answer: The seller bears the risk

INCAS yields this answer by application of the following rule.

## Clause A.5:

Subject to the provisions of B.5, the seller bears all risks of loss of or damage to the goods until such time as they have passed the ship’s rail at the named port of shipment

And using the assumption that: The provisions of B.5 do not apply. An example of a provision of B.5 is that if the vessel named by the buyer fails to arrive on time, then all risks are transferred to the buyer.

The following question shows that INCAS does not only reason about Incoterms, but also about contracts, which include an Incoterm. Reasoning about contracts adds a new complexity, because a contract can contain clauses that supersede Incoterms clauses.

## Example Question 3:

Question: Who bears the risk for damage at open sea under contract AO97002B that contains FOB as delivery term?

Answer: The buyer bears the risk of damage.

INCAS yields this answer by applying the same clause A.5 as in the previous example. Ž .

The answer is based on the assumption that: The seller did package the goods properly.

Using the INCAS trace the user can examine the assumptions made. If an assumption proves to be incorrect, the user can add the corresponding fact, i.e. the fact that the seller did not package the goods properly, to the database and pose the question again. The answer then changes from the buyer bearing the risk of damage to the seller bearing the risk of damage.

## Example Question 4:

Question: Who bears the risk for damage at open sea under contract AO97002B that contains FOB as delivery term, given the extra information that the seller did not package the goods properly? Answer: The seller bears the risk of damage.

INCAS yields this answer by applying the same clause A.5 as in the previous example. Ž .

The answer is based on the exception that: The seller did not package the goods properly.

The answer is based on the extra assumptions that:

1. The inadequate packaging caused the damage.

2. The buyer did give the seller proper information about the voyage the goods were going to make.

The reader may note that extra assumptions are needed to support the use of the exception in the argument. The underlying idea is that excusing the buyer from bearing the risk of damage only makes sense if the inadequate packaging by the seller did indeed cause the damage. A similar idea underlies the other extra assumption. The following question shows that if one of the extra assumptions is falsified, then the answer changes too.

## Example Question 5:

Question: Who bears the risk for damage at open sea under contract AO97002B that contains FOB as delivery term, given the extra information that the seller did not package the goods properly, and that this inadequate packaging caused damage to the goods and that the buyer did not inform the seller properly?

Answer: The buyer bears the risk of damage.

INCAS yields this answer by applying the same clause A.5 as in the previous example. Ž .

The answer is based on the exception that:

1. The seller did not package the goods properly.

2. The inadequate packaging caused the damage.

3. The buyer did not give the seller proper information about the voyage the goods were going to make.

Questions 3, 4 and 5 clearly demonstrate the impact assumptions about exceptional circumstances have on the conclusion INCAS reaches. In the normal situation the buyer bears the risk of damage, and in the case of exceptional circumstances it can be either the buyer or the seller who bears this risk. Question 5 shows that we even have situations with exceptions to exceptions. Because of this impact of assumptions the user has to examine them carefully. The following example shows that Incoterms are sometimes overruled by other legal rules.

## Example Question 6:

Question: Under a contract with FOB as delivery term. What actions should the seller take with respect to export formalities?

Answer: The seller is obliged to obtain an export license or other official authorisation and carry out all customs formalities necessary for the exportation of the goods.

This answer might be replaced by another one when the contract contains clauses that overrule the answer. For example, the guide to Incoterms stipulates that under the 1980 ConÕention on International Sale of Goods Ž . CISG and corresponding provisions in national provisions, unforeseen or reasonably unforeseeable export prohibitions may relieve the seller from his obligation under the contract of sale Ref. 11 .<sup>w</sup> <sup>x</sup>

## Example Question 7:

Question: Under a contract with FOB as delivery term, what actions should the seller take with respect to export formalities, given the extra information that the government issued an export ban for the type of goods mentioned in the contract?

Answer: The seller is not obliged to obtain an export license or other official authorisation and nor to carry out all customs formalities necessary for the exportation of the goods.

As we show later, this exception in the case of an unforeseen or reasonably unforeseeable export prohibition has been implemented in INCAS. We implemented the export ban exception to show that important or frequent exceptions based on other law sources can be added to INCAS. However, it is important to note that not all such exceptions based on other legal sources are implemented in INCAS. The INCAS system is built to provide answers based on reasoning about Incoterms. Including all related legal sources in the INCAS reasoning is not feasible. The user of INCAS should therefore always keep in mind that the answers might be overruled by other law sources to which the contract refers.

## 4. INCAS: implementation

## 4.1. Prolog preliminaries

In this section we provide a very short explanation about Prolog. For a more detailed explanation of Prolog the reader is referred to Ref. 3 . Reasoning in<sup>w</sup> <sup>x</sup> Prolog is done by applying Aif –thenB rules to facts. An example of such a rule in Prolog notation is

$$
\begin{array}{c} \text {mortal(X) IF} \\ \text {man(X).} \end{array}
$$

which means that to prove that X is mortal it is sufficient to prove that X is a man. When this rule is applied to the fact that Socrates is a man, i.e. man Socrates , then Prolog can automatically deriveŽ . that Socrates is mortal, i.e. mortal Socrates . Usu-Ž . ally, this reasoning is implemented as a querying mechanism. A specific formula is presented as a query to Prolog and given to a database with rules and facts. Prolog answers yes if the formula can be derived from the database, and it answers no if no such derivation can be made. Given the database mortal XŽ . Ž . Ž . IF man X , man Socrates Prolog an- 4 swers yes to the question if mortal Socrates is true, Ž .

and no to the question if mortal Plato is true, be-Ž . cause man Plato is not included in the database.Ž .

A special feature of Prolog is how it reasons about negations. The negation, denoted in Prolog notation by the symbol no, is interpreted as a socalled negation-by-failure. This means that a formula no f is evaluated true, if the formula f is not deriv-Ž . able. In the example above this means that the query no mortal Plato gets the answer yes, because mor-Ž Ž .. tal Plato is not derivable. Negation-by-failure has Ž . the remarkable property that it is not persistent under growth of information. For example, if we add the extra formula man Plato to the database above, then Ž . in Prolog we get the answer no to the query whether no mortal Plato is true.Ž Ž ..

Another example, if nothing is known in the database about exception a , then the negation no ex- Ž . Ž ception a is automatically true in Prolog. Hence, Ž .. normality Ž . <sup>s</sup> not exceptional is automatically assumed by Prolog. However, if we add as new information to the database exception a , then no excep-Ž . Ž tion a is no longer true. This loss of conclusionsŽ .. due to extra information is called non-monotonicity. Due to this non-monotonicity Prolog is very suitable to represent defeasible reasoning. In the following sections we will see that this negation by failure plays an important role in the representation of defeasible reasoning about Incoterms. An example of conjunction, which we denote here by AANDB ŽProlog denotes conjunction by A,B ., is

mortal XŽ . IF man XŽ . AND no superman X . Ž Ž ..

which means that to prove that X is mortal it is sufficient to prove that X is a man and X is not superman. An example of a disjunction, which we denote here by AORB ŽProlog denotes disjunction by A;B ., is

mortal XŽ . IF man XŽ . OR animal X .Ž .

which means that to prove that X is mortal it is sufficient to prove that X is a man or that X is an animal. This rule could also have been expressed using the two rules

mortal XŽ . IF man X . Ž . mortal XŽ . IF animal X .Ž .

We use the convention that variable terms in the logic begin with an upper case letter, whereas constant terms begin with a lower case letter. Sometimes we also use quoted upper case letters, e.g. AFOBB, as constant terms. The variable Term will range over the terms of Incoterms, Contract over contracts, ContractTerm over contracts or Incoterms, and Party over seller or buyer. In addition to these constants and variables we also use the list notation $\big [ t _ { 1 } , \dots , t _ { n } \big ] ,$ where $t _ { 1 } , \ldots , t _ { n }$ are either constants, variables or again lists. A special notation for a list is $[ t _ { 1 } \mid t _ { 2 } ] ,$ where $t _ { 1 }$ represents the first element of the list, the so-called AheadB, and $t _ { 2 }$ another list, the so-called Atail.B An example of this notation is a<sup>w</sup> <sup>w</sup> <sup>xx</sup> <sup>N</sup> b,c , which is equivalent to a,b,c . <sup>w</sup> <sup>x</sup>

## 4.2. Deontic predicates

INCAS distinguishes between three kinds of obligation:

1. Obligation to Perform an Action

2. Obligation to Pay for Costs.

Paying for costs is an action. However, because of the special attention Incoterms pay to the division of costs, obligations to pay costs are distinguished from obligations to perform other actions.

3. Obligation to Bear Risks.

Because bearing risk is not really an action an agent can perform, it is distinguished from obligations to perform an action.

Three predicates are used in INCAS to represent these different kinds of obligation. These predicates have the following general structures.

oblige act Action, Party, ContractTerm<sub>–</sub> ( ). The interpretation is that Party seller or buyer is obligedŽ . to perform Action under a certain Contract or Term.

oblige pay For, Party, ContractTerm<sub>–</sub> ( ). The interpretation is that Party is obliged to pay for For under a certain Contract or Term. For represents actions only in this case.

oblige risk For, Party, ContractTerm<sub>–</sub> ( ). The interpretation is that Party is obliged to bear the risks for For under a certain Contract or Term. For represents actions as well as situations likeŽ .AdamageB in this case. The predicate in list is used in INCAS to find out whether an Incoterm is a member of a certain list. in list<sub>–</sub> Ž $t \mid [ t _ { 1 } , \ldots , t _ { n } ] )$ checks whether t is an element of the list $\big [ t _ { 1 } , \dots , t _ { n } \big ] .$ . For example, in<sub>–</sub> list FOB, EXW, . . . ,DDP checks if the IncotermŽ <sup>w</sup> <sup>x</sup>. FOB is an element of the list EXW, . . . ,DDP .<sup>w</sup> <sup>x</sup>

The following Prolog code gives an example of the predicate oblige act: <sub>–</sub>

oblige act export, buyer, Term <sub>–</sub> Ž . IF

in list Term, <sub>–</sub> Ž <sup>w</sup> <sup>x</sup> AEXWB, AFASB, ADEQB ..

oblige act export, seller, Term <sub>–</sub> Ž . IF

in list Term,<sub>–</sub> Ž <sup>w</sup>AFCAB,AFOBB,ACFRB,

ACIFB,ACPTB,ACIPB,ADAFB,ADESB,

ADDUB,ADDPB <sup>x</sup>..

These two rules say that the buyer is obliged to arrange export under the terms EXW, FAS and

DEQ, whereas the seller is obliged to arrange export under the other terms.

The following Prolog code gives an example of the predicate oblige pay. The predicate fact is used<sub>–</sub> in INCAS to represent facts about the world, e.g. contracts:

oblige pay contract price, buyer, ContractŽ <sub>– –</sub>

Term, Price, When. IF

fact price, ContractTerm, Price Ž . AND

ŽŽ Ž When<sup>s</sup> now, performed delivery, seller,

ContractTerm.. OR

Ž Ž When<sup>s</sup>if delivered, no performed<sub>–</sub>

Ž .... delivery, seller, ContractTerm .

This rule says that under contract Contract or Incoterm Term the buyer is obliged to pay the contract price Price. Price has to be paid now if the seller has performed the delivery. Otherwise the buyer can wait until the seller has performed the delivery. The predicate performed is explained in detail when the dynamic features of INCAS are discussed.

In this article we use, for readability, a simplified representation of the actual rules in INCAS. The actual rule in INCAS is

o pay contract price, buyer, ContractTerm, Price, When<sub>– –</sub>Ž<sup>w</sup> <sup>w</sup> <sup>xx</sup> <sup>N</sup> K<sup>N</sup>L . IF

fact price, ContractTerm, PriceŽ<sup>w</sup> <sup>x</sup>. AND

ŽŽ Ž When <sup>s</sup> now, performed delivery, seller, ContractTerm <sup>w</sup> <sup>x</sup> <sup>N</sup> L .. OR

Ž Ž Ž When <sup>s</sup> if delivered, no performed delivery, seller, ContractTerm <sup>w</sup> <sup>x</sup> <sup>N</sup> L . .... <sub>–</sub>

Here the arguments in the predicates are not a fixed number of arguments, but one single list. The advantage of this list is that we can vary the number of arguments of a predicate arbitrarily, simply by making the list longer or shorter. This is necessary, because the number of arguments we have to consider for a given predicate depends on the specific Incoterm we are considering. For example, typically the predicate performed has three arguments: Action, Party, ContractTerm, but in some cases it is also important to specify in what manner the action has been performed, e.g. if the packaging was done normally or in a special manner for difficult weather conditions. In that case we need four arguments, i.e. performed Action, Party, ContractTerm, Manner . Ž<sup>w</sup> <sup>x</sup>. In some cases we need up to a dozen extra arguments. Since we do not discuss these more complicated examples in this article, we do not need this variable list notation here, and we can do it with fixed numbers of arguments in the predicates.

permit Action, Party, ContractTerm ( ). Incoterms also assign permissions to the buyer and the seller. In order to model these permissions the predicate permit is used in INCAS. The general structure of this predicate is permit Action, Party, Contract-Ž Term , meaning that Party is permitted to do Action.

under a certain Contract or Term. The following rule gives an example of the use of permit:

permit request, buyer, ContractTermŽ . IF fact term, ContractTerm,Ž . AFOBB .

The rule states that under the FOB term the buyer is permitted to request a pre-shipment inspection. Besides permissions assigned to the buyer and the seller by Incoterms we also use the following rule:

permit X, Y, Z Ž . IF oblige act X .Ž . <sub>–</sub>

This rule states that if an action is obliged then this action is also permitted. This rule is part of most deontic formalisms.

## 4.3. EÕent predicates

INCAS distinguishes between two types of events. Firstly, there are events that occur beyond the control of the buyer and the seller. An example of such an event is a governmental decision to impose an export ban on goods that include the ordered ones. Secondly, there are events that are under the control of the buyer and the seller. Actions the buyer and the seller perform or fail to perform are part of this type of events. Also the actions, other agents might perform as a result of an influence by the buyer or the seller, are part of this type of events. The seller might, for example, subcontract a freight forwarder to transport the goods to a port of departure. If the freight forwarder actually transports the goods this is an event. However, in INCAS we only have two agents, the buyer and the seller. Therefore, the actions performed by other agents are considered to be actions of either the buyer or the seller, based on who influenced the third agent to perform the action. So, if the freight forwarder, contracted by the seller, transports the goods, we say that the seller transported the goods. To model the actions of the buyer and the seller we use two predicates:

performed. For example, the fact performed de- Ž livery, seller, A097002B, 23<sup>r</sup>09<sup>r</sup>97 states that the. seller delivered the goods belonging to contract O97002 on 23 September 1997.

failure. For example, the fact failure delivery,Ž seller, A097002B, 23<sup>r</sup>09<sup>r</sup>97, Agoods not produced yetB. states that the seller failed to deliver the goods belonging to contract O97002 before the agreed delivery date of 23 September 1997 due to the fact that the goods have not been produced yet.

All failures are inferred automatically by INCAS. For example, the following two rules state that if the seller has delivered the goods, but did not pack the goods properly , then the seller failed to pack the Ž . goods properly. The second rule states that this failure to package properly also leads to the failure of the delivery.

failure packaging, Party, Contract Ž . IF performed delivery, seller, ContractŽ . AND oblige act packaging, Party, Contract,Ž <sub>–</sub> Extent. Ž Ž AND no performed packaging, Party, Contract, Extent ...

failure delivery, Party, ContractŽ . IF failure packaging, Party, Contract . Ž .

Not every non-performance of an action is a failure. For example, if the seller did not deliver the goods belonging to contract Contract, but he still has time to do so before the agreed delivery date, he did not fail to perform the delivery. The inclusion of performed delivery, seller, Contract in the first ruleŽ . ensures this. A failure to package can only be inferred after the seller has performed the delivery. Before the seller has delivered the goods he can still package the goods properly so the non-performance is not a failure yet. Fortunately, we do not have to add a fact to INCAS for every action that has not been performed yet. Because of the negation-byfailure property of Prolog this fact can be inferred automatically. If a fact like performed delivery,Ž seller, A097002B, 23<sup>r</sup>09<sup>r</sup>97 is not present in the . INCAS database, Prolog will assume by virtue ofŽ negation by failure that it is not true. In other words,. Prolog will assume that the seller did not deliver the goods. The fact that an agent performed a certain action will have to be asserted by the user of INCAS. A failure of an agent to perform can be asserted by the user and in some cases INCAS can infer this automatically. For example, in the case where the seller was obliged under contract O97002 to deliver the contract goods before 23 September 1997 IN-

CAS can infer a failure if the system date is after 23 September 1997 and performed delivery, seller,Ž A097002B, 23<sup>r</sup>09<sup>r</sup>97 is not true not present in the. Ž database ..

Events that occurred beyond the control of the buyer and seller are modelled in a different way. Because we do not model actions of agents, other than the buyer and seller, and we cannot attribute this type of actions to either the buyer or the seller, we model the results of the event directly instead of modelling the action. So, if the event, where the government declares an export ban as described above, occurs we do not model the declaration by the government, i.e. performed declared export ban,Ž <sub>– –</sub> government, 23<sup>r</sup>09<sup>r</sup>97 , but instead we add the fact . that an export ban now exists for the goods that the seller was supposed to deliver under contract O97002, fact export ban, seller,Ž . <sub>–</sub> AO97002B .

As described above, the occurrence of events leads to dynamic behaviour of the INCAS system. As a result of this dynamic behaviour INCAS becomes non-monotonic. In other words, INCAS might give a different answer, if we add new facts to the database. A simple form of non-monotonic behaviour occurs when an agent performs an obliged action. For example, assume that under the contract O97002 the seller is obliged to arrange all export formalities. If the seller has actually arranged all export formalities on 24 September 1997, we add the fact performed arrange export formalities, seller,Ž <sub>– –</sub> AO97002B, 24<sup>r</sup>09<sup>r</sup>97 to the database. After we. have added this fact to the database INCAS will conclude that the seller has no obligation to arrange export formalities for contract O97002. Whereas if we had asked the same question before we added the fact, INCAS would have concluded that the seller did have an obligation under contract O97002 to arrange all export formalities. So adding a new fact might lead to a different answer to the same question.

## 4.4. Defeasibility predicates

This section presents the defeasibility predicates of INCAS.

exception. INCAS can reason about situations that deviate from the normal situation. The user can assert that a situation deviates from the normal situation using the exception predicate. For example, exception arrange export form, seller, 999, buyer Ž <sub>– – –</sub> failure asserts that, for the seller, an exception ap- . plies to the action arrange export form. The reason<sub>– –</sub> for this exception is a failure by the buyer.

exception 2<sub>–</sub> . It is also possible in INCAS to reason about exceptions to exceptions. An exception to an exception is asserted using the exception 2<sub>–</sub> predicate.

Because of the importance of defeasible reasoning Section 5 is entirely devoted to this subject. A detailed description of how to use the exception and exception 2 predicates is given there.<sub>–</sub>

## 4.5. Prolog representation of Incoterm clauses

We now give some example of how Incoterm clauses are represented in Prolog using the described predicates. The FOB, CFR and CIF Incoterm stipulate as obligation for the seller:

Deliver the goods on board the vessel named by the buyer at the named port of shipment on the date or within the period stipulated and the manner customary at the port. Clause A.4Ž .

This clause is represented in INCAS by the following rules:

oblige act delivery, seller, ContractTerm, on board, Date, Vessel, Port, MannerŽ . IF extra delivery, seller, ContractTerm, MannerŽ . AND fact term, ContractTerm, Term Ž . AND in list Term,<sub>–</sub> Ž <sup>w</sup> <sup>x</sup> AFOBB, ACFRB, ACIFB . AND fact vessel, ContractTerm, VesselŽ . AND fact port of shipment, ContractTerm, PortŽ . <sub>– –</sub> AND fact date of delivery, ContractTerm, DateŽ . <sub>– –</sub> AND no exception delivery, seller, ContractTerm .Ž Ž ..

Incoterms are just a part of the terms used in a commercial contract. Additional terms are often added. Such an addition can be represented by the predicate extra. For example, the formula extra de-Ž livery, seller, ContractTerm, Manner expresses that. in addition to the Incoterm ContractTerm there is the additional requirement that the seller must deliver the goods in a certain manner.

oblige act delivery, seller, ContractTerm, on board, Date, Vessel, Port, Manner<sub>– –</sub>Ž . IF no extra delivery, seller, ContractTermŽ Ž .. AND fact term, ContractTerm, TermŽ . AND in list Term,Ž <sup>w</sup> <sup>x</sup>AFOBB, ACFRB, ACIFB . AND fact vessel, ContractTerm, VesselŽ . AND fact port of shipment, ContractTerm, PortŽ . <sub>– –</sub> AND fact date of delivery, ContractTerm, DateŽ . <sub>– –</sub> AND fact custom of port, Port, deliver, seller, MannerŽ . <sub>– –</sub> AND no exception delivery, seller, ContractTerm .Ž Ž ..

The difference between the two rules is that the first rule only applies if an extra clause about the manner of delivery is included in the contract. So, the first rule applies in case the contract parties have agreed upon a specific arrangement, whereas the second rule applies when no such arrangement has been agreed upon. Note that both rules can be overruled by an exception.

The CFR, CIF, CPT, CIP, DES, DEQ, DDU and DDP Incoterms stipulate that the seller must:

Unless otherwise agreed, at his own expense provide the buyer without delay with the usual transport document for the agreed port of destination.

This clause is represented in INCAS by the following rules:

oblige act transport doc, seller, ContractTerm<sub>– –</sub>Ž . IF fact term, ContractTerm, TermŽ . AND in list Term,Ž <sup>w</sup> <sup>x</sup>ACFRB, ACIFB, ACPTB, ACIPB, ADESB, ADEQB, ADDUB, ADDPB .. oblige pay transport doc, seller, ContractŽ . IF fact term, Contract, TermŽ . AND in list Term,Ž <sup>w</sup> <sup>x</sup> ACFRB, ACIFB, ACPTB, ACIPB, ADESB, ADEQB, ADDUB, ADDPB ..

The FOB Incoterm stipulates that the seller must:

. . . , render the buyer, at the latter’s request, risk and expense, every assistance in obtaining a transport document for the contract of carriage. Clause Ž A.8.

Note that this clause deals with all of the following concepts: the division of costs, the division of liability, obligation and permission. The clause is represented in INCAS by the following rules:

If the contract Contract does not contain extra arrangements, then the seller has to assist the buyer, if requested to do so.

oblige act assist, seller, Contract, if requested Ž <sub>– –</sub> <sub>–</sub>by, buyer. IF no extra assist, seller, Contract .Ž Ž ..

If a party Other Party is obliged to assist the <sub>–</sub> other party Party, because of a request to do so by the latter, then the requestor Party bears the risk for this assistance.

oblige risk assist, Party, Contract, Ž <sub>–</sub> if requested by, Other party<sub>– – –</sub> . IF oblige act assist, Other party, Contract, Ž <sub>– –</sub> if requested by, Party .. <sub>– –</sub>

Under the FOB Incoterm the buyer is permitted to request the assistance of the seller in contracting for carriage. The conditions Condition of the contract ofŽ carriage should be standard liner conditions liner<sub>–</sub> cond.

permit request assist, buyer, ContractTerm, Ž <sub>–</sub> contract of carriage, Condition<sub>– –</sub> . IF fact term, ContractTerm,Ž . AFOBB AND Condition<sup>s</sup>liner cond.<sub>–</sub>

If a party Party bears the risk of assistance by the other party Other Party, then it has to pay for the <sub>–</sub> assistance.

oblige pay assist, Party, Contract, Ž <sub>–</sub> if requested by, Other party<sub>– – –</sub> . IF oblige risk assist, Party, Contract, Ž <sub>–</sub> if requested by, Other party .. <sub>– – –</sub>

## 5. Defeasible reasoning in INCAS

This section presents the defeasibility reasoning features of INCAS. We first analyse the reasoning that INCAS performs to obtain the answers to the questions 6 and 7 that we presented in Section 3. Consider the following example from the Incoterms.

Under FOB the seller is responsible to arrange the export formalities. In the case of an exception he may be excused. An exception may be a failure of the buyer to give the seller the right information, documents or whatever is needed for clearance, or a reasonably unforeseen export ban.

This text and also the ones in the next sections are not literal quotes from the Incoterms, but abstracts compiled from Ref. 11 . This is represented in the following Prolog code, where exception is a predicate. Exception is a variable representing the type of exceptions and the constant term arrange export<sub>– –</sub> form denotes the action to arrange the export formalities required to export the goods. The constant term export ban denotes that a ban on the export of the <sub>–</sub> goods mentioned in the contract was issued by the government, hence these goods cannot be exported. The first rule expresses that the seller is obliged to arrange export formalities, if the term in the contract is FOB, and there are no exceptional circumstances. The second and third rules indicate two types of exceptional circumstances that are explicitly mentioned in Incoterms. The first exceptional circumstance is that there is an export ban for the goods mentioned in the contract. The second exceptional circumstance is that the buyer failed to perform his part of the contract; e.g. because he did not provide to the seller the necessary information documentation that is needed to arrange the export formalities.

oblige act arrange export form, seller, Contract <sub>– – –</sub>Ž . IF fact term, Contract, Ž . AFOBB AND no exception arrange export form, seller, Contract, Exception . Ž Ž .. <sub>– –</sub> exception arrange export form, seller, Contract, export ban Ž . <sub>– – –</sub> IF fact export ban, seller, Contract .Ž . <sub>–</sub> exception arrange export form, seller, Contract, buyer failureŽ . <sub>– – –</sub> IF failure arrange export form, buyer, Contract . Ž . <sub>– –</sub>

Due to the negation by failure Prolog concludes automatically that the seller is obliged to arrange the export formalities, unless, for example, fact exportŽ <sub>–</sub> ban, seller, 999 or failure arrange export form,. Ž buyer, 999 is added to the database. fact export ban,. Ž <sub>–</sub> seller, 999 says that for the seller in contract 999. there is an export ban for the goods mentioned in <sub>–</sub> this contract. These three rules constitute a clear example of defeasible reasoning. The two exceptions, however, constitute a different type of defeasibility. The rule that an export ban leads to an exception to the obligation of the seller to arrange for export is not part of the Incoterms book. This rule is based on the 1980 United Nations Convention on International Sale of Goods CISG . The rule, there-Ž . fore, only applies when the contract parties are somehow bound by this international convention. Because of the large number of countries that signed the convention we have assumed the rule to apply to all contracts analysed with INCAS. This shows that the rules of the Incoterms book can be overruled by legal rules that have a higher status. This type of defeasibility is called Lex Superior. In Section 6 we give a more detailed analysis of the various types of defeasibility, and their respective roles in the Incoterms domain.

We analyse the reasoning that INCAS performs to obtain the answers in Examples 3, 4 and 5 that were presented in Section 3. Consider the following example from Incoterms:

The seller is obliged to package the goods properly. Under FOB the buyer is liable for damage of the cargo during main-carriage, unless the damage was the result of insufficient packaging by the seller. This exceptional circumstance is itself exempted if the damage was due to extreme conditions and the buyer failed to inform the seller that the goods had to be packaged for these extreme conditions.

What makes this example interesting is that it presents an exception that overrules another exception. We call this an exception-to-an-exception. The general default rule under FOB is that the buyer is liable for damage to the goods on the open sea. The built-in predicate var argument checks whether theŽ . argument is a variable, and it is false if the argument is not a variable.

oblige risk bear risk, Party, Contract, damage, Position<sub>– –</sub>Ž . Ž . IF not var Position AND fact term, Contract, TermŽ . AND oblige risk bear risk, Party, Term, damage, PositionŽ . AND no exception bear risk, Party, Contract, damage .Ž Ž .. <sub>–</sub>

An exception to this rule is that this damage was the result of insufficient packaging by the seller. In that case the seller is liable for damage on the open sea.

exception bear risk, buyer, Contract, damage Ž . <sub>–</sub> IF failure packaging, seller, Contract Ž . AND no exception 2 packaging, seller, Contract, damage .Ž Ž .. <sub>–</sub>

An exception to an exception occurs if the buyer did not tell the seller that the goods had to be packaged AtightlyB but instead the seller just packed normally. The predicate failure notice voyage,Ž <sub>–</sub> buyer, Contract denotes that the buyer did not in-. form the seller adequately about extreme conditions during the voyage of the goods, mentioned in the contract. In that case the buyer is again liable for damage on the open sea.

exception 2 packaging, seller, Contract, damage<sub>–</sub> Ž . IF failure notice voyage, buyer, Contract Ž . <sub>–</sub> AND performed packaging, seller, Contract . Ž .

In these examples we first derived the conclusion that the buyer is liable for damage of the goods on the open sea. Subsequently, if we know that the goods were not properly packaged by the seller, the liability is switched from the buyer to the seller. Finally, the liability is switched back from the seller to the buyer if it can be shown that the buyer did not properly inform the seller about the roughness of the transport conditions. In the latter case the lack of adequate packaging by the seller was so to say excused by the lack of information from the buyer. This switching of conclusions due to adding extra information is typical for defeasible reasoning.

## 6. INCAS as a logical analysis of Incoterms

The logical analysis of Incoterms that we present in this paper shows that a Prolog representation of it is feasible. The Prolog prototype system INCAS can answer questions such as AGiven a specific location of the goods under a certain Incoterm, is the seller or the buyer liable for damage?B and AGiven a specific contract with a specific Incoterm, which part of the journey has to be paid by the seller and which by the buyer?B Slightly more complicated questions that INCAS can answer are AWhich Incoterm should I use as seller, if I do not want to have any liability in port $X ? ^ { \dag }$ or AWhich Incoterm should I use as buyer, if I do not want to be responsible for the arrangements of documents in the port of origin?B Furthermore, INCAS can also answer optimisation questions. For example, the seller and buyer can each feed their own requirements list into the expert system, and the system tries to find the optimal Incoterms if there is any that satisfies both require-Ž . ment’s lists. Clearly, such an expert system would be a great support for electronic contracting. Since electronic contracting is one of the key topics in electronic commerce, it is also clear that this expert system would facilitate electronic commerce. Given the restricted objective we think the Prolog implementation of Incoterms is successful.

INCAS is not supposed to work completely autonomously in the sense that it could replace human legal experts. One of the things that makes INCAS dependent on a human user is that legal terminology is not explained by the system. INCAS does not explain frequently used notions such as AdamageB or Aliability.B To paraphrase Ref. 26 , INCAS is just <sup>w</sup> <sup>x</sup> doing symbolic processing on bit strings, and does not know what it is reasoning about. It is the user who has to decide whether a certain term such as, for example, AdamageB applies to a particular situation in the real world. The system is completely blind in this semantic respect. Interestingly, the Incoterms book has the same blind spot concerning legal terminology. The foreword of the guide to Incoterms states explicitly that no explanations are given in the book about legal notions such as AdamageB or AliabilityB <sup>w</sup> <sup>x</sup> 11 . The user of this book is supposed to be familiar with this terminology. INCAS inherits this Asemantic blindnessB, so to speak from the Incoterms book. Only the human that uses INCAS can solve the vagueness of open texture character of terminology in Incoterms, not the system itself or the Incoterms book.

The most minimalistic description of the functionality of INCAS is that it gives easy access to the content of the Guide to Incoterms 1990 book and that it makes this book available electronically and interactively. Instead of browsing through the book, the user can simply type in his question and INCAS gives an answer. As such, it is an advice tool for human users about Incoterms. In particular, it could be used as an on-line help facility on the Internet that users can consult when they want to have information about Incoterms. However, INCAS is more than just a database of rules, because it not only selects rules but also applies them to the data about specific real world situations that are fed in by the user.

Hence, INCAS performs a simple type of reasoning about the given data.

Leith 16 severely criticises the idea that a Prolog<sup>w</sup> <sup>x</sup> formalisation of legal code is possible at all. As an example he critically analyses the Prolog formalisation of the British Nationality Act as given in Ref. <sup>w</sup> <sup>x</sup> 5 see also Ref. 27 . Leith quotes Sergot et al. as Ž <sup>w</sup> <sup>x</sup>. saying that

The formalisation of the British Nationality Act is an axiomatic theory similar, for example, to an axiomatisation of Euclidean geometry. In principle, any logical consequence of the axiomatisation can be generated and tested mechanically by means of a computer-based theorem-prover.

Leith understands this as a claim that the complete legal practice concerning the application of the British Nationality Act is axiomatised by Sergot et al.’s Prolog representation of this act. In particular, this means that any conclusion that a human legal expert draws when applying this act to a particular situation could have been produced mechanically by the Prolog program. In this view the Prolog program could replace the human legal expert. Leith criticises this idea that the complete legal practice can be axiomatised by a set of rules. He claims that we cannot consider a legal rule in isolation, but we have to consider it within a social context, since it depends for its interpretation upon the context in which it is applied. He illustrates this claim with a number of convincing examples from the legal practice.

We agree with Leith that a legal practice can never be captured completely by a set of axioms. In particular, we do not claim that INCAS axiomatises the complete legal practice of the Incoterm, but neither does the Incoterms book for that matter. The Incoterms book itself is, of course, only a part of the complete legal practice, and so is INCAS. Other important components are the semantic component that connects Incoterms terminology to the real world, and dispute resolution about Incoterms rules at court. Many disputes about legal rules are based on different interpretations of the rules. The Incoterms book does not tell the user which interpretation of a rule is the right one, and neither does INCAS solve these interpretation problems. Answers about disputes cannot be found in the Incoterms book, but have to be decided by humans in court. The fact that no written text can determine its own interpretation has already been argued extensively by linguistic philosophers Žsee for example Ref. 33 .<sup>w</sup> <sup>x</sup>.

With respect to the defeasibility aspect of INCAS we can conclude that our logical analysis shows that there are clear examples of defeasible rules in Incoterms. The occurrence of sophisticated defeasibility is especially interesting with exceptions to exceptions; i.e. the exception about cargo that was inadequately packed by the seller, which might be overruled by another exception that this fault of the seller was excusable because the buyer did not inform the seller about the rough transport conditions. This analysis provides support for the claim that defeasible non-monotonic logics are useful for representing the legal domain. Similar claims are also studied by others see for example Refs. 6–9,17,20– Ž <sup>w</sup> 23,28–32 . For an overview of non-monotonic log- <sup>x</sup>. ics see Ref. 4 .<sup>w</sup> <sup>x</sup>

The defeasibility cases in Incoterms are based on well-known strategies such as Lex Specialis, Lex Posterior Žthe later rule is preferred to the earlier one and . Ž Lex Superior the constitutional higher rule is preferred to the lower one . The Lex Specialis or. Ž Specificity heuristic says that in the case of conflict- . ing rules, the more specific rule is preferred to the more general one. An example of Lex Superior in INCAS is the overruling of FOB by an export ban. In this case an Incoterm is overruled by a superior law, namely the UN ConÕention on the International Sale of Goods Ž . CISG rules on contract law. An application of Lex Posterior is that in some cases it is explicitly stated that Incoterms 1990 are used, and then the rules overrule Incoterms versions of earlier dates.

## 7. User interaction with INCAS

In this section we demonstrate how the user interacts with the INCAS advise system. We use the Example Question 1 see Section 3 as example. TheŽ . question was AGiven the following lists of actions the parties are willing to perform, what are the best Incoterms to use?B This question requires the user to

specify the list of actions that the buyer and the seller are willing to take responsibility for. Fig. 1 shows the INCAS screen that allows the user to select the actions. In this case the user has indicated that the seller is willing to take responsibility for the actions: provide goods, export, contract of car-<sub>– – –</sub>

![](/api/attachments/CB6VP8CX/fulltext/images/8f01a682dec2ceb134e03c1b2a76914df58abd543e83cc724a8fb5ad60588bf5.jpg)  
Fig. 1.

##

<table><tr><td>[CIF, [provide_goods, export, contract_of_carriage, commercial_invoice, insurance_policy, packaging]]CIP [provide_goods, export, contract_of_carriage, commercial_invoice, insurance_policy, packaging]</td><td></td></tr></table>

riage, commercial invoice, pre carriage, insu- <sub>– –</sub> rance policy, packaging. In other words, the seller is willing to provide the goods, to arrange the transport of the goods to the port pre carriage and to theŽ . <sub>–</sub> country of destination contract of carriage , to ar-Ž . <sub>– –</sub> range the export of the goods export , to take out an Ž . insurance policy for the goods insurance policy , toŽ . <sub>–</sub> package the goods packaging and to send the buyerŽ . a commercial invoice commercial invoice . TheŽ . buyer is willing to take responsibility for the carriage of the goods from the port of destination to his premises on carriage , for taking care of the import Ž . <sub>–</sub> formalities import , and to take delivery of the Ž . goods take del . INCAS also allows the user toŽ . <sub>–</sub> specify which Incoterms should be considered. In the example INCAS will consider all Incoterms.

The answer is presented in Fig. 2. In the first box INCAS lists the Incoterms that are optimal from the seller’s perspective. In this case the Incoterms CIF Ž . Ž ACost Insurance FreightB and CIP ACarriage and Insurance Paid ToB. are optimal. The solution CIF,<sup>w</sup> <sup>ww</sup> <sup>w</sup> seller, provide goods, export, contract of car- <sub>– – –</sub> riage, commercial invoice, insurance policy, pack-<sub>– –</sub> aging , for instance, states that under the Incoterm CIF six out of the seven actions that the seller was willing to perform, are obligations for the seller.

In the second box INCAS lists the terms that are optimal from the buyer’s perspective. In the third box INCAS shows those Incoterms that are optimal if we combine the wishes of the seller and the buyer. It is clear that the Incoterms CIF and CIP, which occur in the seller’s box and in the buyer’s box, are the optimal choices. Thus, the solution presented by INCAS is CIF, seller, provide goods, export, con-<sup>w</sup> <sup>ww</sup> <sup>w</sup> <sub>–</sub> tract of carriage, commercial invoice, insurance<sub>– – – –</sub> policy, packaging , buyer, on carriage, import, <sup>xx</sup> <sup>w</sup> <sup>w</sup> <sub>–</sub> take del , CIP, seller, provide goods, export, <sup>xxxx</sup> <sup>w</sup> <sup>ww</sup> <sup>w</sup> <sub>– –</sub> contract of carriage, commercial invoice, insur- <sub>– – –</sub> ance policy, packaging , buyer, on carriage, im- <sup>xx</sup> <sup>w</sup> <sup>w</sup> <sub>– –</sub> port, take del . <sup>xxxx</sup> <sub>–</sub>

## 8. Conclusions

An expert system like INCAS can be used as an assistant to those electronic commerce users that are little or not at all acquainted with current business practice. Incoterms have been highlighted as being appropriately ready to use in forms of electronic commerce, like EDI 25 . The widespread ability to<sup>w</sup> <sup>x</sup> conduct electronic commerce should be matched with spreading tools that make it safe and secure to users to transact so. An on-line trader can combine his automated ordering system with information that IN-CAS provides to select the most appropriate Incoterm for the case and conclude the transaction.

In electronic commerce, Incoterms prevail as global terms that can be used for international transactions and that are readily available to the users. INCAS diminishes the gap between comprehending and using the most appropriate Incoterm. In open electronic commerce spreading information can assist more potential users to transact in an open global market. A specialised system like INCAS can become more effective if integrated in an automated information retrieval and legal expert system that supports electronic commerce transactions.

In the context of electronic commerce, INCAS is also significant as a working prototype to formalise the recognised practice terms when the ETERMS Repository becomes available. From the ETERMS perspective the experience of analysing and reasoning about Incoterms is valuable. It would be interesting to link together the recognised practice terms and Incoterms to provide integrated information to individual users of electronic commerce. INCAS can be seen as a template for structuring and representing similar legal domains.

We also analysed which role defeasible reasoning plays in the representation of Incoterms. We showed that there are many interesting examples of defeasibility in Incoterms. There were even examples of defeasibility with exceptions to exceptions. The general rule, under the FOB term, that the buyer is liable for damage on the open sea, can be overruled by the exception that the seller did not package the goods properly. But this exception can be overruled by another exception that the seller did not package properly, because he was not informed adequately by the buyer about extreme transport conditions of the goods. In the Prolog implementation of INCAS it was shown in detail how the negation-by-failure of Prolog was essential to model these different types of defeasibility in Incoterms.

## Acknowledgements

We thank Arjan Foekens and Andreas Mitrakas for their contributions to the development of INCAS.

## Appendix A. The Incoterms

In the 1990 version of Incoterms 10 , great effort <sup>w</sup> <sup>x</sup> was dedicated to making the terms as comprehensive as possible. The 13 Incoterms are arranged in four groups, namely E, F, C, D. This section presents an overview of the grouped terms.

The group code named E contains only one term, Ex Works EXW . To use this term the seller mustŽ . make the goods available at his premises. This is the minimum obligation the seller can take. In this case, the intentions of the buyer with respect to the goods are not of interest to the seller. The seller, however, may extend his assistance to the buyer with respect to formalities related to export procedures.

To use a term from group F the seller must hand over the goods to a nominated carrier free of risk and expenses to the buyer. The seller has to make arrangements for the carriage of goods up to the delivery point. The point of delivery also constitutes the critical point for the transfer of risk from the buyer to the seller. In practice, however, the seller may also make transport arrangements that the buyer will pay and bear the risk for. There is no generally agreed practice as to what obligations the parties have with respect to these arrangements.

The terms of group C stipulate that the seller undertakes to ship the goods, make all arrangements and pay for the main carriage up to the final destination. Under C terms the seller fulfils his obligation to deliver the goods by handing over the goods for shipment in his country. This constitutes delivery to the buyer. Under a C term, there are two critical points, one coinciding with the point of shipment under an F term and the other up to which the seller pays for carriage and insurance.

To use a term from group D the seller should make sure that the goods arrive at the stated destination 1, pp. 103–104 . This is often interesting to<sup>w</sup> <sup>x</sup> sellers who need to control and plan their cargo as well as the delivery at the prescribed destination. The

13 Incoterms of the 1990 version are presented in the list below:

A.1. The E group: seller makes goods aÕailable at his premises

EXW Ž . AEx WorksB : the seller fulfils his obligation to deliver when he makes the goods available to the buyer at his premises. The buyer bears all the risks from there on.

A.2. The F group: seller arranges and pays for pre-carriage in country of export

FCA Ž . AFree CarrierB : the seller fulfils his obligation to deliver when he has handed over the goods, cleared for export, into the charge of the carrier named by the buyer at the named place or point. If the buyer has not indicated any point, the seller may choose one within the place or range where the carrier shall take the goods into his charge. If, according to commercial practice or at the request of the buyer the seller contracts with a carrier, he does so at the expense and risk of the buyer. This term can be used for any mode of transport.

FAS Ž . AFree Alongside ShipB : the seller fulfils his obligation to deliver when he has placed the goods alongside the ship on the quay or in lighters at the named port of shipment. The buyer is responsible for clearing the goods for export. This term can be used for sea or inland waterway transport.

FOB Ž . AFree On BoardB : the seller fulfils his obligation to deliver when the goods have crossed the ship’s rail at the named port of shipment. The seller is responsible for clearing the goods for export. This term can be used for sea or inland waterway transport.

## A.3. The C group: seller arranges and pays for main carriage, without assuming the risk on it

CFR Ž . ACost and FreightB : the seller pays the costs and freight necessary to transport the goods to the named port of destination but the risk and any additional costs are transferred to the buyer when the goods cross the ship’s rail at the named port of shipment. The seller is responsible for clearing the goods for export. This term can only be used for sea or inland waterway transport.

CIF Ž . ACost, Insurance and FreightB : the seller pays the costs and freight and insurance for the cargo necessary to transport the goods to the named port of destination. The risk and any additional costs are transferred to the buyer when the goods cross the ship’s rail at the named port of shipment. The seller must make the arrangements for insurance, pay the premium and clear the goods for export. This term can only be used for sea or inland waterway transport.

CPT Ž . ACarriage Paid ToB : the seller pays the freight to transport the goods to the named port of destination. The risk and any additional costs are transferred to the buyer when the goods have been delivered into the custody of the carrier. The seller is responsible for clearing the goods for export. This term can be used for any mode of transport.

CIP Ž . ACarriage and Insurance Paid ToB : the seller pays the freight and insurance to transport the goods to the named port of destination. The seller must make the arrangements for insurance, pay the premium and clear the goods for export. This term can be used for any mode of transport.

## A.4. The D group: seller bears costs and risks up to arriÕal at destination

DAF Ž .ADelivered At FrontierB : the seller fulfils his obligation to deliver when the goods have been made available and cleared for export at the named point and placed at the frontier but before the customs border of that country. This term can be used mainly for goods carried by rail or road, but it may also be used for other modes of transport.

DES Ž . ADelivered Ex ShipB : the seller fulfils his obligation to deliver when the goods have been made available to the buyer on board the ship but not yet uncleared for import at the named port of destination. The seller bears all costs and risks involved in bringing the goods to the named port of destination. This term can only be used for sea or inland waterway transport.

DEQ Ž . ADelivered Ex QuayB : the seller fulfils his obligation to deliver when the goods have been made available to the buyer on the quay at the named port of destination, cleared for importation. The seller bears all risks and costs including duties, taxes and other charges to deliver the goods. This term should not be used if the seller is unable directly or indirectly to obtain the import licence. This term can only be used for sea or inland waterway transport.

DDU Ž .ADelivered and Duty UnpaidB : the seller fulfils his obligation to deliver when the goods have been made available to the buyer at the named place in the country of importation. The seller bears all risks and costs excluding duties, taxes and other Ž charges and risks to pass through customs formalities . The buyer must pay any additional costs and . bear any risks caused by his failure to clear the goods for import in time. This term can be used for any mode of transport.

DDP Ž . ADelivered and Duty PaidB : the seller fulfils his obligation to deliver when the goods have been made available to the buyer at the named place in the country of importation. The seller bears all risks and costs including duties, taxes and other charges to deliver the goods cleared for importation. This term should not be used if the seller is unable directly or indirectly to obtain the import licence. This term can be used for any mode of transport. While EXW represents the minimum obligation for the seller, DDP represents the maximum obligation.

In Incoterms 1990, the obligations of the parties for each term are grouped under the same main headings entitled ATHE SELLER MUST . . . B and ATHE BUYER MUST . . . B There are ten obligations that the parties must fulfil as explained in the table below Ref. 11, p. 11 .<sup>w</sup> <sup>x</sup>

Obligations of the trading partners according to Incoterms 1990

<table><tr><td></td><td>Obligations of the seller</td><td></td><td>Obligations of the buyer</td></tr><tr><td>A1</td><td>Provide goods according to the contract of sale</td><td>B1</td><td>payment of the price</td></tr><tr><td>A2</td><td>Make arrangements for licences,authorisations and formalities</td><td>B2</td><td>make arrangements for licences,authorisations and formalities</td></tr><tr><td>A3</td><td>Contract of carriage and insurance</td><td>B3</td><td>Contract of carriage</td></tr><tr><td>A4</td><td>Delivery</td><td>B4</td><td>Taking of delivery</td></tr><tr><td>A5</td><td>Transfer of risks</td><td>B5</td><td>Transfer of risks</td></tr><tr><td>A6</td><td>Division of costs</td><td>B6</td><td>Division of costs</td></tr><tr><td>A7</td><td>Notice to the buyer</td><td>B7</td><td>Notice to the seller</td></tr><tr><td>A8</td><td>Proof of delivery, transport document or equivalent electronic message</td><td>B8</td><td>Proof of delivery, transport transport document or equivalent electronic message</td></tr><tr><td>A9</td><td>Check, pack and mark</td><td>B9</td><td>Inspect the goods</td></tr><tr><td>A10</td><td>Other obligations</td><td>B10</td><td>Other obligations</td></tr></table>

## References

<sup>w</sup> <sup>x</sup> 1 R. Battersby, Incoterms and the single market, in: C. Debattista Ed. , Incoterms in Practice, ICC Publication 505 Inter-Ž . national Chamber of Commerce Publishing, Paris, 1995.

<sup>w</sup> <sup>x</sup> 2 R. Bons, Designing trustworthy trade procedures for open electronic commerce: a methodology for the automated auditing of inter-organisational controls, PhD dissertation No. 27, Rotterdam School of Management, 1997.

<sup>w</sup> <sup>x</sup> 3 I. Bratko, Prolog Programming for Artificial Intelligence, Addison-Wesley Publishing, Reading, MA, 1986.

<sup>w</sup> <sup>x</sup> 4 G. Brewka, Nonmonotonic Reasoning: Logical Foundations of Common Sense Reasoning, Springer, Berlin, 1991.

<sup>w</sup> <sup>x</sup> 5 H.T. Cory, P. Hammond, R. Kowalski, F. Kriwaczek, F. Sadri, M. Sergot, The British Nationality Act as a Logic Program, Department of Computing, Imperial College, London, 1984.

<sup>w</sup> <sup>x</sup> 6 T. Gordon, The importance of nonmonotonicity for legal reasoning, in: H. Fiedler, F. Haft, R. Traunmuller Eds. , ¨ Ž . Expert Systems in Law,1988, pp. 110–126, Tubingen. ¨

<sup>w</sup> <sup>x</sup> 7 T. Gordon, The Pleadings Game. An Artificial Intelligence Model of Procedural Justice, Kluwer Academic Publishing, Netherlands, 1995.

<sup>w</sup> <sup>x</sup> 8 N. Den Haan, Automated Legal Reasoning, PhD thesis, Faculty of Law, University of Amsterdam, 1996.

<sup>w</sup> <sup>x</sup> 9 J.F. Horty, Deontic logic as founded in nonmonotonic logic, Annals of Mathematics and Artificial Intelligence 9 1993Ž . 69–91.

<sup>w</sup> <sup>x</sup> 10 International Chamber of Commerce, Incoterms, International Chamber of Commerce Publishing, Paris, 1990.

<sup>w</sup> <sup>x</sup> 11 International Chamber of Commerce, Guide to Incoterms, International Chamber of Commerce Publishing, Paris, 1990.

<sup>w</sup> <sup>x</sup> 12 International Chamber of Commerce, ETERMS Repository Guidebook, Document No. E100<sup>r</sup>INT.3, Paris, 1996.

<sup>w</sup> <sup>x</sup> 13 R. Kalakota, A. Whinston, Frontiers of Electronic Commerce, Addison-Wesley Publishing, Reading, MA, 1996.

<sup>w</sup> <sup>x</sup> 14 R. Lee, INTERPROCS: a Java-based prototyping environment for distributed electronic trade procedures, Proceedings of the 31st Hawaii International Conference on Systems Sciences

Ž . HICSS’98 , IEEE Computer Society Press, Los Alamitos, 1998.

<sup>w</sup> <sup>x</sup> 15 R.M. Lee, Y.U. Ryu, DX: a deontic expert system, Journal of Management Information Systems 1996 .Ž .

<sup>w</sup> <sup>x</sup> 16 P. Leith, Fundamental errors in legal logic programming, The Computer Journal 29 6 1986 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 L.T. McCarty, Defeasible deontic reasoning, Fundamenta Informaticae 21 1994 125–148.Ž .

<sup>w</sup> <sup>x</sup> 18 A. Mitrakas, The proposed ETERMS Repository of the International Chamber of Commerce, EDI Law Review 3 4Ž . Ž .1997 Dordrecht.

<sup>w</sup> <sup>x</sup> 19 A. Mitrakas, Open EDI and Law in Europe: A Regulatory Framework, Kluwer Law International, The Hague, 1997.

<sup>w</sup> <sup>x</sup> 20 H. Prakken, Logical Tools for Modelling Legal Argument, PhD thesis, Faculty of Law, Free University Amsterdam, 1993.

<sup>w</sup> <sup>x</sup> 21 H. Prakken, G. Sartor, A system for defeasible argumentation, with defeasible priorities, Proceedings of the International Conference on Formal and Applied Practical Reasoning FAPR’96 , Lecture Notes in Artificial Intelligence vol.Ž . 1085 Springer, Berlin, 1996.

<sup>w</sup> <sup>x</sup> 22 H. Prakken, G. Sartor, Argument-based extended logic programming with defeasible priorities, Journal of Applied Non-Classical Logics 7 1997 .Ž .

<sup>w</sup> <sup>x</sup> 23 H. Prakken, M. Sergot, Contrary-to-duty obligations, Studia Logica 57 1996 91–115.Ž .

<sup>w</sup> <sup>x</sup> 24 C. Prins, EDI standardisatie: voorwaarden, eigenschappen en juridische implicaties, EDI standardisation: conditions prop-<sup>w</sup> erties and legal implications in: R. Esch van, C. Prins Eds. ,<sup>x</sup> Ž . Recht en EDI, Kluwer Academic Publishing, Deventer, 1993.

<sup>w</sup> <sup>x</sup> 25 J. Ramberg, Incoterms in the era of Electronic Data Interchange, Forum Internationale 1988 November.Ž .

<sup>w</sup> <sup>x</sup> 26 J.R. Searle, Minds, brains, and programs, The Behavioral and Brain Sciences 3 1980 .Ž .

<sup>w</sup> <sup>x</sup> 27 M. Sergot, F. Sadri, R. Kowalski, F. Kriwaczek, P. Hammond, The British Nationality Act as a logic program, Communications of the ACM 29 5 1986 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 D.B. Skalak, E.L. Rissland, Argument moves in a rule-guided domain, Proceedings of the International Conference on Arti-

ficial Intelligence and Law ICAIL’98 , ACM Press, Oxford, Ž . 1991, pp. 1–11.

<sup>w</sup> <sup>x</sup> 29 Y.H. Tan, L.W.N. van der Torre, Why defeasible deontic logic needs a multi-preference semantics, Proceedings of the 3rd European Conference on Symbolic and Quantitative Approaches to Reasoning and Uncertainty ECSQARU’95 ,Ž . Springer, Berlin, 1995.

<sup>w</sup> <sup>x</sup> 30 L.W.N. van der Torre, Y.H. Tan, Cancelling and overshadowing: two types of defeasibility in defeasible deontic logic, Proceedings of the 10th International Joint Conference on Artificial Intelligence IJCAI’95 , Kaufmann Publishers,Ž . 1995.

<sup>w</sup> <sup>x</sup> 31 L.W.N. van der Torre, Y.H. Tan, The many faces of defeasibility in defeasible deontic logic, in: D. Nute Ed. , Defeasi-Ž . ble Deontic Logic Kluwer Academic Publishing, Netherlands, 1997.

<sup>w</sup> <sup>x</sup> 32 B. Verheij, J.C. Hage, H.J. van den Herik, An integrated view on rules and principles, Artificial Intelligence and Law, 1997.

<sup>w</sup> <sup>x</sup> 33 L. Wittgenstein, Philosophical Investigations, MacMillan, New York, 1958.

Yao-Hua Tan y.tan@fac.fbk.eur.nl studied mathematical logicŽ . and computer science at the universities of Amsterdam and Groningen in the Netherlands, and received his PhD from the department of Mathematics and Computer Science of the Free University of Amsterdam. He is currently an associate professor at the Rotterdam School of Management and associate director of EURIDIS at the Erasmus University Rotterdam. He is also scientific director of the Erasmus Center for Electronic Commerce Ž . ECEC of the Erasmus University. He served as the Reynolds Visiting Professor at the Wharton School of the University of Pennsylvania. His current research focuses on formal models for electronic contracting and automated auditing of electronic trade procedures.

Walter Thoen wthoen@fac.eur.nl studied business informatics atŽ . the Erasmus University in Rotterdam. In 1997 he founded the DEON Company, which develops software to support electronic procurement systems for the petrochemical industry. He is also doing research at EURIDIS on electronic contracting.
