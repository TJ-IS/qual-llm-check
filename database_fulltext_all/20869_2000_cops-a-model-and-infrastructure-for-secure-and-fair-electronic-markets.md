---
otero_id: 20869
otero_key: "ZKTDESX5"
title: "COPS: a model and infrastructure for secure and fair electronic markets"
authors: "Alexander W. Röhm; Günther Pernul"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00082-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# COPS: a model and infrastructure for secure and fair electronic markets

Alexander W. Rohm<sup>)</sup> ¨ ¨, Gunther Pernul

Department of Information Systems, UniÕersity of Essen, Wirtschaftsinformatik, UniÕeritatsstr. 9, 45141 Essen, Germany

## Abstract

Open electronic markets on the Internet have many advantages compared to traditional markets. A variety of new business models, types of markets and digital products emerge, because they potentially generate revenues. In order to support the realization of secure and fair electronic markets, it is important to address the security risks without lowering the advantages of the Internet. In this work, we describe a model for secure and fair markets, which supports this integrated approach. It considers security and fairness of market transactions, different market forms, digital goods and the impact of different business models. Based on our market model, we developed the COPS infrastructure that provides a framework for designing market transactions, an execution environment for market transactions, different trusted and non-trusted servicesŽ . and appropriate security mechanisms to realize secure and fair electronic markets. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic markets; Security; Fairness; Infrastructure; Market transaction specification

## 1. Introduction

There are lots of advantages in using electronic markets. Electronic markets, seen as mechanisms for coordinating the allocation of goods, are supposed to reduce the transaction costs, especially when the traded goods are digitally represented 7,19 . As a <sup>w</sup> <sup>x</sup> consequence, electronic markets in the Internet are expected to produce lower prices and bigger margins than traditional ways of trading. Existing markets become more efficient and new types of markets and new opportunities emerge. By its interactive character, the Internet supports more effective ways of marketing 34 . Its openness sets almost no limits to <sup>w</sup> <sup>x</sup> growth, and entrance barriers for suppliers and demanders are very low 5 .<sup>w</sup> <sup>x</sup>

Openness is one of the Internets biggest advantages. But it also introduces huge risks for information security to the Internet. Messages sent through the Internet using TCP<sup>r</sup>IP may be intercepted or changed. Thus, confidentiality, integrity and authenticity of messages cannot be guaranteed. Generally, in open electronic markets, there is no trust relationship between business partners 6 . Looking from the<sup>w</sup> <sup>x</sup> user’s perspective, the insecurity and uncertainty seems overwhelming.

Facing these problems, researchers and industries developed solutions in some areas, like adding security mechanisms to EDI<sup>1</sup> for a standardized data exchange, SET for secure electronic payment 21 ,<sup>w</sup> <sup>x</sup> cryptography for ensuring some degree of security and privacy, mechanisms for performing digital signatures, contracting tools or electronic agents for negotiation support. Most of them are not easy to integrate and in many cases, are not very flexible and gained not much interest and trust in practice so far.

Our hypothesis is that users want to have integrated tools guaranteeing privacy, security and fair trade, that are embedded in a legal system, which protects from criminal behavior and technical failure. On the other hand, users, and especially, suppliers, want to freely choose and, eventually, change after some time the market structure in which they are trading their digital goods. In our opinion, these are electronic markets’ key requirements, which are vital for future electronic markets. In order to meet these requirements, we are developing the infrastructure Commercial Protocols and Services COPS for se-Ž . cure and fair electronic markets, which is described in this work.

The outline of this paper is as follows: in Section 2, we elaborate a model for secure and fair electronic markets. In Section 3, we discuss the mentioned key requirements in more detail.

Some insights into the COPS architecture and how markets can be built with the COPS infrastructure will be given in Section 4. Previous and related work on cryptographic issues, security and electronic markets is commentated in Section 5. Section 6 summarizes the state of current work on the COPS project and gives directions for further research.

## 2. Electronic market model

In this section, we elaborate the COPS market model. After an introductory description of the general model, a more detailed description of the different roles of the participants on electronic markets, of the phases of market transactions and of the concept Adigital goodB will follow.

## 2.1. General model

Market-based coordination can be classified into four categories: direct-search markets where the fu-Ž ture partners seek out one another , brokered markets. Ž .with the brokers assuming the search function , dealer markets with the dealers holding inventoriesŽ against which they buy and sell , and the auction. markets 11,35 . From this classification, we derive<sup>w</sup> <sup>x</sup> four electronic market player roles: demander, supplier, electronic intermediary cybermediary and Ž . trusted third party. Together with the information services, five roles of participants are considered in the COPS market model.

It is a common practice to structure a market transaction into at least three phases: the information phase, the negotiation phase and the execution phase Ž . or settlement phase . Fig. 1 illustrates the COPS market model. The three levels I, N, E show theŽ . three phases, while the corner elements represent the different participants and their business processes conducted during a market transaction.

The planes in between the corner elements are the different protocols coordinating the activities of the different players. These protocols are specific for each particular type of market, for the type of payment and for the digital good that is traded.Ž .

In the following subsections, we discuss the dimensions of the model in deeper detail. First, the market players and their roles, then the purpose of the transaction phases, and finally, the concept of digital goods will be discussed.

![](/api/attachments/ZKTDESX5/fulltext/images/c505fef3786487f5e9953e7a150452e1690c5906918f3a7bf4fcaf0bd6f14df3.jpg)  
Fig. 1. COPS market model.

## 2.2. Market players

<sup>Ø</sup> The demander is the driving force of a market transaction. Only in the information phase it might be that the supplier initiates the phase by offering his products. All other phases are initiated by the demander. It is on the demander’s side, where many preconditions for success or failure of an electronic market are set 10 . All variables that play a role in<sup>w</sup> <sup>x</sup> the consumers’ decision should be considered when realizing an electronic market. For example, an infrastructure has to preserve the open character of the Internet. In particular, no or less technical or organisational preconditions should exist that hinder a demander to participate. The use of the system should be easy and comfortable. Ideally, the demander acts intuitively not being aware of the complexity of the underlying system. Another important field is the various aspects of privacy and anonymity.

<sup>Ø</sup> The supplier has the choice to offer his<sup>r</sup>her goods either on a direct search market through cybermediaries, or on an electronic auction market. The choice will depend on the supplier’s preferences on the type of the good offered and on other strategic considerations. For the supplier, it must be easy to build an electronic market according to the marketing decisions. Because markets change daily, market strategies change daily, too. As a consequence, changing the coordination type of an electronic market must be very easy.

<sup>Ø</sup> An electronic intermediary<sup>2</sup> is trading information about products like their prices or quality. He offers product evaluation, quality assurance, or special combinations of products e.g. travel agency .Ž . There are quite different understandings of electronic intermediaries. All agree, that intermediaries will survive despite the fact that direct producer–buyer Ž relationships are becoming easier and cheaper in. electronic markets, because they are able to produce an added value to electronic goods 29 .<sup>w</sup> <sup>x</sup>

<sup>Ø</sup> Trusted third parties are participants in electronic markets in whom other participants have to trust, because they perform sensible tasks. Such sensible tasks occur in many situations for different reasons. Besides the trusted third parties, which are necessary to implement digital signatures, secure timestamps and attribute certificates, there is a need for trusted third parties that are directly involved in the market transaction as a business partner. To illustrate this and to show the difference to an intermediary, we give the example of an anonymous mediated market scenario. On that market, a supplier S offers a certain quantity of a good at the price of ECU100 and a demander D demands the same amount, but is willing to pay ECU125. An intermediary would take the chance and earns ECU25. Intermediaries have own interests on the market, while trusted third parties are supposed to act according to fixed rules transparently to S and D. For example, simply reporting offers, or in an exchange market, meeting all matching demands. In our understanding, the distinguishing mark is that intermediaries do have personal interests and follow own goals on the same market they act, but trusted third parties are neutral.

An important role for trusted third parties as part of a security infrastructure is their use for public-key certification. Due to this, they offer an infrastructure to support legal binding of electronic documents, as requested by digital signature laws, i.e. 12 . This is<sup>w</sup> <sup>x</sup> practically important for contracting, and also, for digital goods, which often need authenticity, originality and similar properties.

<sup>Ø</sup> Information serÕices provide technical information about the market infrastructure and the network. Examples are certificate directories 15 or a special<sup>w</sup> <sup>x</sup> host, which processes inquiries like: Awhat is the network address of a trusted third party issuing secure time stamps?B Again, the distinction between trusted third parties and information services is important. The certification authority CA and the Ž . certificate are trusted rather then certificate directories.

## 2.3. Market transaction phases

The three transaction phases have different properties and requirements. In this subsection, we want to discuss the characteristics of the phases in a more detailed way.

When we look at the past developments in electronic markets, we see how electronic markets themselves are exposed to competition 20 . Unlike exam-<sup>w</sup> <sup>x</sup> ples in the past electronic markets, the Internet now addresses the consumer demander directly. For thisŽ . reason, it might be worth considering traditional consumer behavior models, when looking at the transaction phases. Consumer behavior models are meta-models for the research about the decision making process of consumers. They try to explain which variables have an impact on the consumer’s decisions and how variables interrelate. Therefore, their focus is on the information phase. In the Engel–Kollat–Blackwell EKB model the variableŽ . choice is part of the negotiation phase 9 . In the <sup>w</sup> <sup>x</sup> execution phase the, consumers get the product delivered. The EKB model describes feedback to the next transaction with the variables outcome, satisfaction and dissonance.

<sup>Ø</sup> During the information phase, the parties search their proper business partners especially supplier, Ž intermediary . Demanders, for example, search sup- . pliers who can satisfy their demands. In the global Internet, the search may result in a lot of information, especially in a direct-search market. This brings uncertainty. Therefore, new types of value adding intermediaries, who can help the demander with product and brand evaluations,<sup>3</sup> will appear in the information phases of future electronic market transactions. The demander cannot trust the potential business partners, because he does not know who is the person behind the offer in the web. Even if authenticity of an offer is granted and the identity of the business partner is provable, in many cases, there is no basis for trust in appropriate behavior.

<sup>Ø</sup> In the negotiation phase, the supplier and the demander have to find an agreement. Many details of the contract have to be fixed, like the method of payment and the method of shipping. All obligations for all business partners have to be mentioned in this contract.

The negotiation phase may have different forms. On a direct search market, it begins with the direct contact of demander and supplier. In the case they find an agreement, it ends with the completion of a contract. On an electronic auction market, the negotiation phase works according to the detailed rules of the auction mechanism and the supplier is generally not involved in the negotiation between the auctioneer and the demander. Also, in the other mediated market structures especially dealer and broker mar-Ž kets , the negotiation takes either place between. demander and intermediary or between supplier and intermediary.

<sup>Ø</sup> During the execution phase, both the demander and the supplier have to meet the obligations described and fixed in the contract they have made in the negotiation phase. In most markets, there are two sub-phases: the payment and the delivery of goods. How they are carried out strongly depends on the type of the good.

## 2.4. Digital goods

Today, trading immaterial goods in most cases means sending and receiving documents which describe rights or obligations. But there are also new forms of digital goods, which are inherently carrying their value. Examples are digital cash or digital represented audio and video data. These examples show that new types of goods with new requirements occur and that others may appear in the near future.

Most people are not even sure what electronic property is, because it somehow depends on common sense. The worth of a digital good depends on the Ž . interpretation and the individual opinion on what is valuable and what is not. The same problem people in ancient time had with paper money. But when we talk about digital goods, we mean bits that are somehow valuable and that have to be protected from losing their value. This protection becomes more important then in traditional markets, because the ethic rules of real life are not applicable to the cyberspace and the inherent protection of matter does not apply to bits 8 .<sup>w</sup> <sup>x</sup>

Ownership in general is defined by rights that an owner has: Awhat is owned are socially recognized rights of actionB <sup>w</sup> <sup>x</sup> 1 . A general definition of digital goods may therefore be the following: a digital good is a good, that allows to transfer and use its ownership rights in an electronic way. Those rights of the owner have to be protected by an infrastructure for secure electronic market transactions, especially during the execution phase.

There is an interesting interplay between the business model and the protection of digital goods as we can see by the following examples. In some cases, it might be part of the business model to allow groups to share a digital good purchased by a group member, because this increases revenues of the supplier <sup>w</sup> <sup>x</sup> 4 . Sometimes, digital goods may be copied freely after a certain amount of time. An example is news services, where customers pay for actuality of information. After some time, the information loses its value and may be copied freely.<sup>4</sup> When trading digital emission permits, on the other hand, a permit should only be usable to emit toxins, when it is an original. It must not be possible to use a license twice, because otherwise, the system will miss its goal 27 . <sup>w</sup> <sup>x</sup>

## 3. Key requirements

In our opinion, the key requirements on electronic market infrastructures are privacy, security, fair trade, acting in an appropriate legal system and the possibility of dynamic market structures. In this work, we leave out the problem of dynamic market structures, which we discuss in Ref. 22 . In the following<sup>w</sup> <sup>x</sup> sections, we resume the definitions of privacy, security and fair trade and, whenever necessary, extend them to better fit in the context of electronic markets for digital goods. This is followed by a discussion about the properties an appropriate legal system should have.

## 3.1. Security

The term security describes the capability of an IT system to ensure confidentiality, integrity and authenticity of transmitted and stored data against threads or attacks 23 . While the definition of confi-<sup>w</sup> <sup>x</sup> dentiality and authenticity is obvious, integrity depends on the context. Integrity, as usually used in a network security context, means that a message was received unchanged. If we extend it to describe the situation, that a system represents a consistent view of the reality, we get a more adequate definition of integrity in electronic commerce. Providing integrity of digital goods means protecting bits from losing their value. Each digital good has its own integrity properties and in some cases like, e.g. copyrightŽ protection of documents , a whole set of protocols. and services of an electronic market infrastructure can be involved to protect the digital good from losing its value.

The way how security is realized has a great impact on the user. It may be a precondition for trust, when the user believes his interests are kept <sup>w</sup> <sup>x</sup> 18 . On the other hand, it must be easy to use. If the user has to enter name and password whenever he enters a new market place, he will soon demand simpler systems.

## 3.2. Legal system

Today’s legal systems are faced with new challenges. New forms of property, communication and agreements are appearing in the cyberspace. Simultaneously, great risks are coming up for the participants of electronic markets. The main problem with digital documents is that they are easy to forge and to copy. Therefore, they cannot have a binding character for their authors. For electronic markets, additional technical mechanisms and legal regulations for legal binding of digital documents are necessary.

The digital signature plays the technical part in the solution of this problem. It is an application of public-key cryptography as introduced by Rivest et al. in 1978 25 . A digital signature placed on a<sup>w</sup> <sup>x</sup> digital document indicates that this document was written by someone who owns a secret-key. The digital signature can be verified, if the public-key belonging to the secret-key is available. That a public-key belongs to a person is usually certified by a trusted third party, the so-called CA.

The legal binding of a digital signature depends on the strength of the digital signature algorithm, the reliability of the certification infrastructure 14 , and <sup>w</sup> <sup>x</sup> the regulating laws. In Germany, the Digital Signature Act includes regulations, which allow digital signatures to be a piece of evidence 12 .<sup>w</sup> <sup>x</sup>

Subject of legal binding with digital signatures may be contracts, orders and guarantees of authenticity, quality or the integrity of digital goods. Digital signatures do have different semantics. Therefore, the $\mathbf { W } ^ { 3 } \mathbf { C } ^ { \prime } \mathbf { s }$ digital signature initiative proposed to annotate labels to digital signatures 17,33 .<sup>w</sup> <sup>x</sup>

## 3.3. PriÕacy

Several organizations and initiatives like AFree SpeechB were founded as a reaction to the US government, which tried to restrict the use of cryptography. This was an impressive expression of the individual’s demand for privacy rights. Obviously, this will be demanded of electronic markets in the Internet, too. It is expected that users of electronic payment systems prefer anonymity 32 . Beside user<sup>w</sup> <sup>x</sup> demands and political implications, anonymity, in some cases, also has economic relevance, for example, in some auction mechanisms, participants must be anonymous when biting.

## 3.4. Fair trade

The term fairness can generally be used for a series of exchanged messages or goods between two parties A and B in which the messages depend on each other, so that neither A nor B has the possibility to cheat. It should not happen in a market transaction, that either A has paid and B does not deliver the paid goods, or vice versa. Additionally, sometimes, more than two parties are involved. Fairness then means that either each party has received what it has expected at the end of a transaction or no party received anything 2 . Equivalent problems are si-<sup>w</sup> <sup>x</sup> multaneously signing a contract, certified mail and payment with receipt.

Fairness also means being informed which security and privacy services are available for a transaction, and having the ability to choose or to negotiate which service will be used. For example, when trading original documents, it is possible to hide either the seller’s or the buyer’s identity from the trusted third party 27 . <sup>w</sup> <sup>x</sup>

## 3.5. Secure and fair market transactions

Each phase of a market transaction has special security demands. They cannot be generalized, but there are some very common and specific security demands within each phase.

<sup>Ø</sup> During the information phase, it is necessary that a demander can rely on offers he<sup>r</sup>she has received. Beside this, the communication during the information phase sometimes has to be secure against taping or manipulation by competitors. These properties refer to the basic security services integrity, authenticity and confidentiality. An additional requirement is non-repudiation, which refers to the fact that parties cannot deny having participated in a communication. The economic importance of the information phase for real markets 24 will lead to further security needs. For example, the supplier has to prove the ownership of the goods he wants to sell to the auctioneer before the goods are offered.

<sup>Ø</sup> During the negotiation phase, the legal binding of contracts is an important security demand. For contracts signed with digital signatures, this implies that public-key certification and legal regulations are needed. The legal regulations must describe the way how digital signatures should be applied in order to be acceptable as a piece of evidence.

Besides security, fairness has to be provided by a protocol for contract signing. There are some standards and proposals. Some of them use a trusted third party in the signing process of some work without trusted third parties 2 . In an auction mar-<sup>w</sup> <sup>x</sup> ket, the auctioneer is a trusted third party per definition. This enables a technical solution to provide secure, fair and anonymous contracting on auction markets. All other markets benefit from protocols that do not involve trusted third parties in the signing process.

<sup>Ø</sup> During the execution phase, the integrity of the digital goods has to be guaranteed and payment has to be conducted in a secure way. A large number of secure electronic payment mechanisms in the Internet were proposed, but electronic payment still is an obstacle for electronic commerce 3,16 . The large<sup>w</sup> <sup>x</sup> number of proposals, no integration, no standards, no familiarity of users with the systems might be reasons that contribute to this situation. However, an important part of an infrastructure for electronic markets will be an integrated and secure solution for electronic payment.

An example of market transaction on an open market for free trade with original and anonymous emission permits realized in COPS can be found in Ref. 28 .<sup>w</sup> <sup>x</sup>

## 4. The COPS project

In order to conduct secure and fair market transactions, COPS provides basic security services and fair security protocols. These must be combined to build fair and secure market transactions. As argued above, the business models and security of market transaction cohere. Consequently, it may not always be the security expert who is responsible for designing the market transaction. So, an infrastructure has to support the non-expert with the specification and realization of the transaction.

Altogether, we suggest four components of an infrastructure for secure and fair electronic markets:

1. a framework which supports the designer of a market transaction,

2. an execution environment for specified market transactions,

3. different basic trusted and non-trusted servicesŽ . in the network, and

4. appropriate security mechanisms provided through an API.

The goal of the COPS project is to provide all four aspects mentioned above, where the focus is on the parts that have not been addressed in other electronic commerce security research projects. Before, we describe the specification and realization of market transactions in COPS; we now discuss a few secure electronic commerce projects and products in Section 4.1.

## 4.1. PreÕious and related work

There are some projects related to the work we do within COPS, which are concerned with open electronic commerce, security and fairness.

A consortium of industry, as well as partners from academia, backed by the European Union, started the project Secure electronic marketplace for Europe Ž . SEMPER in 1995. Although SEMPER has a flexible architecture, it does not implement different electronic markets structures. It does not include trusted services so far 31 . It is based on an API, which<sup>w</sup> <sup>x</sup> allows a programmer to realize secure and fair market transactions. There are some related commercial products that realize secure transactions for specific electronic commerce applications in the Internet. Examples are:

<sup>Ø</sup> Brokat www.brokat.de offers Internet bankingŽ . solutions and uses cryptography to secure the communications.

<sup>Ø</sup> OpenMarket www.openmarket.com has severalŽ . products for secure electronic transactions, such as Transact, LiveCommerce and SecureLink.

<sup>Ø</sup> Java electronic Commerce Framework of Sun Microsystems www.javasoft.com is planned toŽ . be a developer platform which provides security services.

Commercial solutions are either based on a centralized concept where the suppliers’ server must be a trusted, or is designed to be a developer platform that provides secure communication services.

In this work, we left out the whole field of electronic payment systems. There are a lot of proposals and even commercial products such as SET, CyberCash and eCash. For an overview, we refer to Refs. 3,16 . A good solution for the integration of<sup>w</sup> <sup>x</sup> different payment systems was found in the SEM-PER project, too.

## 4.2. Designing market transactions

The way from defining a business model for a digital good to the realization of the corresponding market transaction, and finally, its execution includes three steps. The first step is to define the market transaction on an abstract level. Given the digital good, the business model and the marketing strategies, some basic questions about the market transaction have to be answered. Which coordination form will be used, which security requirements have to be considered and how far will privacy and fairness be provided? In this step, all roles on the future market have to be considered. Eventually, the result of this step is a semiformal description of the market transaction. We propose a workflow-like method, which allows modeling of application-dependent security semantics 26 . This specification must be translated <sup>w</sup> <sup>x</sup> into a formal representation in a next step. In this step, the knowledge about protocols and security services enters the specification of the market transaction. The user has to select the appropriate security mechanisms and has to combine them in a way that the market transaction fulfills the specification from the first step. This would normally take a security expert to perform. Which mechanisms are providing which level of protection against which attack and how they are combinable with each other without weakening the security properties are generally nontrivial questions. The third step is the transformation to an executable format, which finally implements the market transaction. We developed A Language for Modeling Secure Business Transactions Ž . ALMO\$T 28 , which is designed to be executed in<sup>w</sup> <sup>x</sup> the COPS infrastructure.

The designer of a market transaction has to be supported by a security expert or a tool where security mechanisms and services have to be selected and combined in the right way. For this task, we develop a graphical editor, which supports this process. By using a graphical representation of ALMO\$T, the user formulates the processing steps and protocol steps of the transaction. This editor is shown in Fig. 2. In the right part of the editor window, the control flow of the designed market transaction is shown. Suppose we have a document in the private environment upper right part of Fig. 2 and the semiformal Ž . description of the market transaction requires confidentiality, the user can browse through a tree structure in the left part of the editor window to find the right solution for the problem. He simply has to browse to AconfidentialityB and gets a range of mechanisms that provide confidentiality. To apply a mechanism to the document, he simply drag-n-drop the icon of the mechanism to the icon representing the document indicated by the arrow in Fig. 2 .Ž .

This way is not only used to select basic security mechanisms; the editor is also able to store more complex solutions, like single transaction phases or even whole market transactions. For example, when a user has specified a negotiation phase with a secure vickery auction, he stores the specification under the keywords auctions and vickery. When the next case occurs, where a secure vickery auction is needed, he simply drag-n-drop the specification from the tree. Another example may be the protocol for fair exchange, which has been developed within the SEM-PER project 2 . Such protocols are integrated into <sup>w</sup> <sup>x</sup> the COPS infrastructure by implementing them in ALMO\$T. Once this has been done, they are provided by the COPS infrastructure and may be re-used as building blocks for further market transactions.

![](/api/attachments/ZKTDESX5/fulltext/images/5d319db0353b6cc216899b5b47f2ca911981458c96f76f6be0a95892bd8cfd94.jpg)  
Fig. 2. The ALMO\$T editor.

There is a minimal set of basic elements which are essential for the designing process. They are provided by the infrastructure and are accessible through the browser in the editor. They are either realized in the COPS library see Section 4.4 or areŽ . services offered by other parties on the Internet seeŽ Section 4.3 ..

The ALMO\$T editor automatically transforms the specification into the ALMO\$T language, which can be executed in the COPS infrastructure in order to conduct market transactions according to the specification. The graphical example in Fig. 2 looks, in textual ALMO\$T representation, like the following line:

## RSA.encrypt(pKeyring.get(t),doc).

It has the semantic that a document is encrypted with the RSA algorithm by using the public-key of T, which is looked up in the public key ring.

## 4.3. SerÕices

COPS services can be divided into different classes. Services are either basic or complex, they are either local or part of the global infrastructure, and finally, they are either trusted or not.

Basic services are predefined and transparent parts of COPS. They are realized in the COPS prototype architecture, which is described in Section 4.4. Combining basic services may result in a new security service, which is then a complex COPS service. For example, a public key cryptographic mechanism is the basic service and the digital signature is the complex service.

Many things, like for example, the encryption of a document, can be done locally. But beside these local services, services provided by other parties are also needed in an electronic market infrastructure. Examples for global services are public key directories, secure time stamp services or registration services for copyright protection of documents.

It was argued that the distinction between trusted and not trusted services is important when global services are involved in a market transaction.

## 4.4. Prototype architecture

The basic services are realized in the COPS library and can be referenced in ALMO\$T through an object-oriented interface. ALMO\$T specifications are executed in the ALMO\$T interpreter. Together,

![](/api/attachments/ZKTDESX5/fulltext/images/910d46b188e7ee353b0546971846d0d04e1f345995886166c06134b8be22f451.jpg)  
Fig. 3. General COPS prototype architecture.

<sup>Ø</sup> the COPS library, and

<sup>Ø</sup> the ALMO\$T Interpreter

build the prototype architecture of COPS. The architecture of the COPS library is shown in Fig. 3. At the lowest level, the COPS architecture uses Internet transport protocols for communication, and database systems functionality to store, manage and retrieve data.

With the two layers in the middle of the architecture, we tried to find abstraction levels that allow to integrate different security solutions, like SSL at the communications layer or to add new cryptographic systems at the security mechanism layer. Up to now, the second layer includes the Cryptix library 30 and <sup>w</sup> <sup>x</sup> some additional security mechanisms that are implemented by our own, but it is planned to use other products at this layer, too. The Security Mechanism Abstraction Layer SMAL is the layer that offersŽ . security services in a transparent way and allows to use cryptographic mechanisms from the second layer without knowledge about their implementation. This makes it easy to change implementation without changing other parts of software and makes COPS more flexible for the case when new standards will arise or stronger cryptographic mechanisms are found.

On top of the SMAL, the predefined ALMO\$T objects are realized at the services layer SL . Global Ž . services at the SL are, for example, information services, public-key certificate directories and certification authorities. They are part of the global services infrastructure.

Secure markets may be built by specifying secure market transactions by ALMO\$T programs on top of that layer.

## 4.5. Secure realization of different market structures

A market transactions specification consists of multiple complementary objects, where each object realizes a specific role in a market transactions phase.

Fig. 4 displays a sample setting of ALMO\$T specifications distributed over the network. In the figure, the network appears as a line in the middle.

![](/api/attachments/ZKTDESX5/fulltext/images/a57e1939fc2a9054d45384835f1b3a8960e48f4afcc8aa4cc86ae23ae8aa124a.jpg)  
Fig. 4. Distributed ALMO\$T objects in the COPS infrastructure.

Each box connected to the network stands for the host of a party participating in the market supplier,Ž broker, directory and demander . The cubes within. the boxes are objects, which are either data objects Žlike the private environment holding the secret key at the demanders host , services like the directory . Ž object d. or realizations of the role the party plays in a certain market transaction phase. With the exception of the objects in the private environment, all objects have an ALMO\$T interface, which allows their invocation in an instantiation of a market transaction. When such an invocation is initiated, the ALMO\$T interpreter loads and executes the object.

The example in Fig. 4 contains all needed objects to realize an auction market for selling a digital good doc. The demander first instantiates the negotiation phase object Ž . I . When he found the auctioneer who offers the desired good, he pushes a button in order to participate in the auction. Triggered by this event, the object for the auction mechanism N is invoked at both parties. Now, the demander participates at the auction. If he is the winner, the negotiation phase ends and automatically, the execution phase objectŽ E. get started. This happens simultaneously at the suppliers, the auctioneers and the demanders’ host. To prove digital signatures during the different phases, the directory d has to be involved to provide the public-key certificates.

A market maker of an auction market uses ALMO\$T to describe the information phase, the negotiation phase and the execution phase for the digital good that will be traded on the electronic market. He does that for every role participating in the transaction. For the market maker, it is easy to change the market structure, e.g. by changing the specifications. He can also easily change the business model by altering the specification of the execution phase.

## 4.6. COPS security

An open and flexible electronic commerce infrastructure is best realized with an architecture of distributed objects. The COPS infrastructure is therefore based on distributed objects. This unfortunately introduces new risks.

In the COPS infrastructures, two types of communication may occur. First, the participants may communicate directly, by using the methods of the object net for example: net.send (Issuer, License). Second, through calling a method of an object, which provides a special service on the network, for example: d.getCertificate (Issuer). Each participant has a private environment, which is visualized with the black box in Fig. 4. In this part of the environment, objects contain sensible data, as for example, the private key of a participant.

There are three aspects of security in the COPS infrastructure:

<sup>Ø</sup> calling distributed objects,

<sup>Ø</sup> communication over the network viaŽ . net , and

<sup>Ø</sup> storing and retrieving private data to or from the private environment.

Each of these aspects has a specific solution to the security demands in COPS. When an object is called over the Internet, the ALMO\$T interpreter automatically provides integrity and confidentiality of the call, especially the handed parameters. This is not only necessary when ALMO\$T objects are calling each other, it is also relevant when using services like databases. If you look, for example, at the Oracle 7.2 JDBC interface, it forces you to send passwords in plain text over the network. By using the methods of the object net, the application layer security aspects we discussed are relevant. Consequently, providing security is part of the designing process of the market transaction. The sensible objects in the participants’ private environment are stored encrypted and are only accessible after identification and strong authentication. Otherwise, this would be the weakest link in the chain and weaken all other efforts to provide security.

## 5. Conclusion and further work

In this work, we presented a model for secure and fair electronic markets that considers different business models, market structures and digital products that may emerge. This model justifies our approach for an infrastructure enabling secure and fair electronic markets. We further introduced the concepts and ideas of the COPS infrastructure.

The status of the COPS-project is as follows: security requirements are collected and evaluated in an electronic commerce scenario focusing on anonymous digital trade of tradable emission permits 27 .<sup>w</sup> <sup>x</sup> Basic cryptographic mechanisms are collected in the SMAL class library. The library will serve in experimenting with certification authorities, labeled digital signatures, confidentiality and privacy issues. It is the basis for the realization of the different COPS services and protocols.

Currently, we are implementing COPS modules in Java by using the Cryptix 2.0 library 30 , which<sup>w</sup> <sup>x</sup> provides basic public-key cryptography RSA Ž . mechanisms and a collection of cryptographic mech anisms such as DES, IDEA, Blowfish, MD5, MD4 and SHA. All further cryptographic mechanisms in the SMAL are implemented by our own. In the first prototype, we will use PGP 2.6.3i message and file formats for compatibility reasons. For the certificate directory, we use an Oracle 7.2 database with a jdbc Ž . product of i-kenetics Java interface and CORBA <sup>w</sup> <sup>x</sup> 13 . The CA, which is currently under development, will provide X.509v3 15 certificates and support <sup>w</sup> <sup>x</sup> the ISO certification infrastructure 14 . The <sup>w</sup> <sup>x</sup> ALMO\$T graphical editor and the object browser are written in Java using the SWING library provided by Sun. These parts are in a first prototype status and will be integrated in the next step.

## 6. Uncited reference

<sup>w</sup> <sup>x</sup> <sub>21</sub>

## References

<sup>w</sup> <sup>x</sup> 1 A. Alchian, H. Demsetz, The property rights paradigm, in: N. Rosenberg Ed. , Journal of Economic History vol. 33, 1973.Ž .

<sup>w</sup> <sup>x</sup> 2 N. Asokan, M. Schunter, M. Waidner, Optimistic protocols for fair exchange, in: T. Matsumoto Ed. , Proc. of the 4thŽ . ACM Conference on Computer and Communications Security, ACM Press, 1997, pp. 8–17.

<sup>w</sup> <sup>x</sup> 3 N. Asokan, P. Janson, M. Steiner, M. Waidner, State of the art in electronic payment systems, IEEE Computer 30 9Ž . Ž .1997 28–35.

<sup>w</sup> <sup>x</sup> 4 Y. Bakos, E. Brynjolfson, D. Lichtmann, Shared information goods, Journal of Law and Economics 1998 April.Ž .

<sup>w</sup> <sup>x</sup> 5 R Benjamin, R. Wigand, Electronic markets and virtual value chains on the information superhighway, Sloan Management Review, 1995, pp. 62–72, Winter.

<sup>w</sup> <sup>x</sup> 6 R.W.H. Bons, Designing Trustworthy Trade Procedures for Open Electronic Commerce, PhD-Series in General Management 27, Rotterdam School of Management, 1997.

<sup>w</sup> <sup>x</sup> 7 S.Y. Choi, D.O. Stahl, A.B. Whinston, The Economics of Electronic Commerce, Macmillan, London, 1997.

<sup>w</sup> <sup>x</sup> 8 B. Cox, What if there is a silver bullet and the competition gets it first? Journal of Object-oriented Programming Ž . 1992 . http:<sup>rr</sup>www.virtualschool.edu<sup>r</sup>mon<sup>r</sup>Cox<sup>r</sup> CoxWhatIfSilverBullet.html, last accessed 5Ž . <sup>r</sup>1998 , June.

<sup>w</sup> <sup>x</sup> 9 J.F. Engel, R.D. Blackwell, D.T. Kollat, Consumer Behaviour, The Dryden Press, Hinsdale, IL, 1978.

<sup>w</sup> <sup>x</sup>10 T. Fong, D. Fowler, P.M.C. Swatman, Success and failure factors for implementing effective electronic markets, International Journal of Electronic Markets 8 1 1998 45–47.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 K. Gabade, Securities Markets, McGraw-Hill, New York, 1982.

<sup>w</sup> <sup>x</sup> 12 German Digital Signature Act: Beschluß des Bundeskabinetts, IuKDG Informations-und Kommunikationsdienste Gesetz, DuD Datenschutz und Datensicherheit 21, Verlag Vieweg, Wiesbaden, 1997 in German .Ž .

<sup>w</sup> <sup>x</sup> 13 I-Kinetics, http:<sup>rr</sup>www.i-kinetics.com<sup>r</sup>Žlast accessed 9<sup>r</sup> 1997 ..

<sup>w</sup> <sup>x</sup> 14 International Organisation for Standardization ISO , Infor-Ž . mation processing systems — Guidelines for the Use and Management of Trusted Third Parties — Part 2: Technical Aspects, International Standard ISO<sup>r</sup>IEC Working Draft 14516-2, Geneva, 1995.

<sup>w</sup> <sup>x</sup> 15 International Telecommunication Union, Information Technology — Open Systems Interconnection — The Directory, Authentication Framework, ITU-T Recommendation X.509, 1993.

<sup>w</sup> <sup>x</sup> 16 P. Janson, M. Waidner, Electronic payment systems, Datenschutz und Datensicherheit 6<sup>r</sup>96, Vieweg-Verlag, Wiesbaden, 1996.

<sup>w</sup> <sup>x</sup> 17 P. Lipp, A. Sterbenz, The digital signature initiative, in: S. Katsikas Ed. , Proceedings of Communications and Multi-Ž . media Security ’97, Chapman & Hall, London, 1997.

<sup>w</sup> <sup>x</sup> 18 E. Lorenz, Trust, contract and economic cooperation, Cambridge Journal of Economics 23 3 1999 301–315, Pub-Ž . Ž . lished on behalf of the Cambridge Political Economy Society by Oxford University Press, Oxford.

<sup>w</sup> <sup>x</sup>19 T. Malone, J. Yates, R. Benjamin, Electronic markets and electronic hierarchies, Communications of the ACM 30 6Ž . Ž .1987 484–497.

<sup>w</sup> <sup>x</sup> 20 T. Malone, J. Yates, R. Benjamin, The logic of electronic markets, Harvard Business Review, 1989, pp. 166–171, May–June.

<sup>w</sup> <sup>x</sup>21 MasterCard, VISA, Secure electronic Transaction SETŽ . Specification, Book 1: Business Description, 1996, http:<sup>rr</sup> www.visa.com<sup>r</sup>cgi-bin<sup>r</sup>vee<sup>r</sup>sf<sup>r</sup>set<sup>r</sup>intro.html last ac-Ž cessed 8<sup>r</sup>1996 ..

<sup>w</sup> <sup>x</sup> 22 G. Pernul, A.W. Rohm, Different electronic markets technos- ¨ tructures, Fourth Research Symposium on Electronic Markets ’98, 1998.

<sup>w</sup> <sup>x</sup> 23 C.P. Pfleeger, Security in Computing, 2nd edn., Prentice-Hall, Englewood Cliffs, NJ, 1997.

<sup>w</sup> <sup>x</sup> 24 A. Picot, C. Bortenlaenger, H. Roehrl, The automation of capital markets, Journal of Computer-Mediated Communication 1 3 1995 . http: Ž . Ž . <sup>rr</sup>shum.cc.huji.ac.il<sup>r</sup>jcmc<sup>r</sup>vol1<sup>r</sup> issue3<sup>r</sup>picot.html, last accessed 8Ž . <sup>r</sup>1997 .

<sup>w</sup> <sup>x</sup> 25 R.L. Rivest, A. Shamir, L. Adleman, A method for obtaining digital signatures and public key cryptosystems, Communications of the ACM 21 2 1978 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 A.W. Rohm, G. Pernul, G. Herrmann, Modelling secure and¨ fair electronic commerce, Proc. of IEEE Annual Computer Security Applications Conference, ACSAC ’98, 1998.

<sup>w</sup> <sup>x</sup> 27 A.W. Rohm, M. Gerhard, A secure electronic market for¨ anonymous transferable emission permits, Proceedings of Thirty-First Hawaii International Conference on System Sciences, HICSS-31, 1998.

<sup>w</sup> <sup>x</sup> 28 A.W. Rohm, G. Herrmann, G. Pernul, Modelling secure¨ electronic business transactions in ALMO\$T, Proc. of IEEE Annual Computer Security Applications Conference, AC-SAC ’99, 1999.

<sup>w</sup> <sup>x</sup>29 M.B. Sarkar, B. Butler, C. Steinfield, Intermediaries and cybermediaries: a continuing role for mediating players in the electronic marketplace, Journal of Computer-Mediated Communication 1 3 1995 . http:Ž . Ž . <sup>rr</sup>www.usc.edu<sup>r</sup>dept<sup>r</sup> annenberg<sup>r</sup>vol1<sup>r</sup>issue3<sup>r</sup>vol1no3.html, last accessed 8 Ž <sup>r</sup> 1997 ..

<sup>w</sup> <sup>x</sup> 30 Systemics, www.systemics.com<sup>r</sup>software<sup>r</sup>cryptix-java<sup>r</sup> Ž . last accessed 9<sup>r</sup>1997 .

<sup>w</sup> <sup>x</sup> 31 M. Waidner, Development of a secure electronic marketplace for Europe, Proceedings of ESORICS ’96, LNCS, Springer, 1996.

<sup>w</sup> <sup>x</sup> 32 R.M. Weiler, Money, transactions, and trade on the Internet, Imperial College London, 1995, http:<sup>rr</sup>graph.ms.ic.ac.uk<sup>r</sup> results last accessed 8Ž .<sup>r</sup>1997 .

<sup>w</sup> <sup>x</sup> 33 World Wide Web Consortium, Dsig 1.0 Signature Lables-Using PICS 1.1 Lables for Digital Signatures, W3C Working Draft 5-June-97, 1997, http:<sup>rr</sup>www.w3.org<sup>r</sup>WWW<sup>r</sup>TR Ž . last accessed 8<sup>r</sup>1997 .

<sup>w</sup> <sup>x</sup> 34 P. Zellweger, Web-based sales: defining the cognitive buyer, International Journal of Electronic Markets 7 3 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 35 V. Zwass, Electronic commerce: structures and issues, International Journal of Electronic Commerce 1 1 1996 M.E.Ž . Ž . Sharp.

![](/api/attachments/ZKTDESX5/fulltext/images/962bda06cb4ad1a28c3eaefcfe81f77fc36a301ad250e2803b52376a0fbe2a4c.jpg)

Alexander W. Rohm received his¨ diploma degree in 1996 from the faculty of Electrical Engineering and Computer Science at the University of Siegen, Germany. Since 1996, he has been serving as a researcher with the Department of Information Systems at the University of Essen, Germany. The research fields to which he contributed by journal articles, books and talks at internationa conferences, include electronic commerce, IT-security, cryptography and

environmental informatics. His PhD thesis is about multilateral secure electronic market transactions for digital goods. He is a member of board of the special interest group on IT-security of the German Informatics Society, since 1997.

![](/api/attachments/ZKTDESX5/fulltext/images/a70133756587ab62ddf0f01c634fa68aa6a8889a6c1d54fc2a4f47c26f3ac658.jpg)

Gunther Pernul received the diploma de-¨ gree from the University of Vienna in 1985 and the doctorate degree with honours from the University of Vienna in 1989. Currently, he is Full Professor at the Department of Information Systems at the University of Essen, Germany. Prior to that, he was with the Department of Applied Computer Sciences at the University of Vienna, Austria. During 1990 and 1991, he was post doctoral scholar at the Database Systems Re-

search and Development Centre at the University of Florida, Gainesville, FL, as well as at the College of Computing at the Georgia Institute of Technology, Atlanta, GA. His research interests are electronic commerce and new media, information systems security, advanced database applications and applied cryptography.
